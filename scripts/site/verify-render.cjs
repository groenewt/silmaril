// Browser validation of the Jekyll artifact and its generated reading/exploration surfaces.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const root = path.resolve(process.argv[2]);
const base = process.argv[3] || '';
const documents = JSON.parse(fs.readFileSync('docs/_data/documentation.json', 'utf8'));
const catalog = JSON.parse(fs.readFileSync('docs/assets/data/ontology.json', 'utf8'));
const receipts = [];
const server = http.createServer((request, response) => {
  const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
  if (base && !pathname.startsWith(base + '/')) { response.writeHead(404).end(); return; }
  let file = path.resolve(root, pathname.slice(base.length).replace(/^\//, ''));
  if (file !== root && !file.startsWith(root + path.sep)) { response.writeHead(403).end(); return; }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  if (!fs.existsSync(file)) { response.writeHead(404).end(); return; }
  const mime = {'.html':'text/html','.css':'text/css','.js':'text/javascript','.json':'application/json','.svg':'image/svg+xml','.woff2':'font/woff2','.woff':'font/woff'};
  response.setHeader('Content-Type', mime[path.extname(file)] || 'application/octet-stream');
  response.end(fs.readFileSync(file));
});
(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const origin = `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch({headless:true});
  fs.mkdirSync('render-evidence', {recursive:true});
  try {
    for (const width of [320, 1280]) {
      const page = await browser.newPage({viewport:{width,height:900},reducedMotion:'reduce'});
      const failures = [];
      page.on('pageerror', error => failures.push(error.message));
      page.on('response', response => { if(response.url().startsWith(origin)&&response.status()>=400)failures.push(response.url()+': '+response.status()); });
      for (const route of ['/', '/architecture/', '/provenance/', '/folklore/', '/reading/', '/explore/']) {
        const response = await page.goto(origin + base + route, {waitUntil:'networkidle'});
        assert.equal(response.status(),200,route);
        assert(await page.locator('main').isVisible(),route+' main');
        assert.equal(await page.locator('link[href*="generated.css"]').count(),1);
        if(route==='/') {
          assert.equal(await page.locator('.katex').count(),2,'both algebra and Frame mathematics render');
          assert.equal(await page.locator('.katex-error').count(),0);
          const vector=await page.locator('.journey-diagram').evaluate(node=>({namespace:node.namespaceURI,width:node.getBoundingClientRect().width,height:node.getBoundingClientRect().height,title:node.querySelector('title').textContent}));
          assert.equal(vector.namespace,'http://www.w3.org/2000/svg');assert(vector.width>200&&vector.height>50&&vector.title.length>10);
          assert((await page.getByRole('link',{name:'Open the ontology atlas'}).getAttribute('href')).startsWith(base+'/explore/'));
        }
        if(route==='/architecture/') {
          assert.equal((await page.locator('.build-status-state').allTextContents()).join('|'),'Not checked|Not checked|Not checked');
          await page.locator('.build-status-link').focus();
          assert.equal(await page.locator('.build-status-link').evaluate(node=>getComputedStyle(node).outlineStyle),'solid');
        }
        if(route==='/reading/') {
          assert.equal(await page.locator('iframe[data-document-source]').count(),documents.length);
          assert.equal(await page.locator('.embedded-document[open]').count(),0,'documents initially collapse');
          assert.equal(await page.locator('iframe[src]').count(),0,'closed documents do not fetch');
          await page.locator('#document-search').fill('unary-byte-frame-law');
          assert.equal(await page.locator('.embedded-document:not([hidden])').count(),1);
          const shelf=page.locator('#document-docs-unary-byte-frame-law');
          await shelf.locator('summary').focus();await page.keyboard.press('Enter');
          await shelf.locator('iframe').waitFor({state:'visible'});
          const frame=await shelf.locator('iframe').elementHandle().then(handle=>handle.contentFrame());
          await frame.locator('#document-toc li').first().waitFor();
          assert((await frame.locator('#document-content').textContent()).includes('Universal Unary Byte-Frame Law'));
          assert.equal(await frame.locator('#document-content').getAttribute('data-document-digest'),documents.find(document=>document.source==='docs/unary-byte-frame-law.md').digest);
          await frame.getByRole('button',{name:'Collapse sections'}).click();
          assert.equal(await frame.locator('.document-chapter[open]').count(),0);
          const target=frame.locator('#document-toc a').filter({hasText:'Surface spelling'});
          if(await target.count())await target.first().click();
          await frame.getByRole('button',{name:'Expand sections'}).click();
          assert((await frame.locator('.document-chapter[open]').count())>0);
          const frameDimensions=await frame.evaluate(()=>({width:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth}));
          assert(frameDimensions.scroll<=frameDimensions.width+1,'document frame must reflow');
          await page.getByRole('button',{name:'Collapse all documents'}).click();
          assert.equal(await page.locator('.embedded-document[open]').count(),0);
          await page.locator('#document-search').fill('');
        }
        if(route==='/explore/') {
          await page.locator('#ontology-workbench[data-ready="true"]').waitFor({timeout:60000});
          assert(catalog.files.length>30000,'catalog covers the full basicttl tree');
          assert.equal(await page.locator('#ontology-tree details').count(),1,'file directories render lazily');
          await page.locator('#ontology-tree summary').first().click();
          assert((await page.locator('#ontology-tree details').count())>1);
          await page.locator('#ontology-kind').selectOption('class');await page.locator('#ontology-search').fill('urn:silmaril:fnd:#Magma');
          await page.getByRole('button',{name:'Magma',exact:true}).click();
          await page.locator('.neighborhood-diagram').waitFor();
          assert.equal(await page.locator('.neighborhood-diagram').evaluate(node=>node.namespaceURI),'http://www.w3.org/2000/svg');
          assert((await page.locator('.entity-identity').textContent()).includes('urn:silmaril:fnd:#Magma'));
          await page.locator('.inspector-panel summary').filter({hasText:'Turtle source'}).first().click();
          assert((await page.locator('.turtle-source').first().textContent()).includes('Magma'));
          await page.locator('#ontology-kind').selectOption('files');await page.locator('#ontology-search').fill('basicttl/foundation/algebra_rings.ttl');
          await page.getByRole('button',{name:'basicttl/foundation/algebra_rings.ttl',exact:true}).click();
          await page.locator('#ontology-inspector[data-selection="basicttl/foundation/algebra_rings.ttl"]').waitFor();
          assert((await page.locator('#ontology-inspector .statement').count())>0);
        }
        await page.screenshot({path:`render-evidence/${base?'project':'root'}-${width}-${route.replace(/[^a-z]/g,'')||'index'}.png`});
        const dimensions=await page.evaluate(()=>({width:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,overflowing:[...document.querySelectorAll('body *')].filter(node=>node.getBoundingClientRect().right>document.documentElement.clientWidth+1&&getComputedStyle(node).position!=='absolute').slice(0,10).map(node=>({tag:node.tagName,classes:node.className,right:node.getBoundingClientRect().right}))}));
        assert(dimensions.scroll<=dimensions.width+1,`${route} overflows at ${width}: ${JSON.stringify(dimensions)}`);
        receipts.push({base,width,route,status:response.status(),dimensions});
      }
      assert.deepEqual(failures,[]);await page.close();
    }
    fs.writeFileSync(`render-evidence/${base?'project':'root'}-results.json`,JSON.stringify({documents:documents.length,ontologyFiles:catalog.files.length,receipts},null,2));
    console.log(JSON.stringify({result:'PASS',base,documents:documents.length,ontologyFiles:catalog.files.length,pages:receipts.length}));
  } finally {await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});

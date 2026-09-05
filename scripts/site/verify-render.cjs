// Browser validation of the actual Jekyll artifact; not an admission proof.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const root = path.resolve(process.argv[2]);
const base = process.argv[3] || '';
const documents = JSON.parse(fs.readFileSync('docs/_data/documentation.json', 'utf8'));
const receipts = [];
const server = http.createServer((request, response) => {
  const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
  if (base && !pathname.startsWith(base + '/')) { response.writeHead(404).end(); return; }
  const relative = pathname.slice(base.length).replace(/^\//, '');
  let file = path.resolve(root, relative);
  if (file !== root && !file.startsWith(root + path.sep)) { response.writeHead(403).end(); return; }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  if (!fs.existsSync(file)) { response.writeHead(404).end(); return; }
  const mime = {'.html':'text/html','.css':'text/css','.js':'text/javascript','.json':'application/json','.svg':'image/svg+xml'};
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
      const page = await browser.newPage({viewport:{width,height:900}});
      const failures = [];
      page.on('pageerror', error => failures.push(error.message));
      page.on('response', response => {if (response.url().startsWith(origin) && response.status() >= 400) failures.push(response.url() + ': ' + response.status());});
      for (const route of ['/', '/architecture/', '/provenance/', '/reading/']) {
        const response = await page.goto(origin + base + route, {waitUntil:'networkidle'});
        assert.equal(response.status(), 200, route);
        assert(await page.locator('main').isVisible(), route + ' main');
        assert.equal(await page.locator('link[href*="generated.css"]').count(), 1);
        await page.screenshot({path:`render-evidence/${base ? 'project' : 'root'}-${width}-${route.replace(/[^a-z]/g,'') || 'index'}.png`});
        const dimensions = await page.evaluate(() => ({width:document.documentElement.clientWidth, scroll:document.documentElement.scrollWidth, overflowing:[...document.querySelectorAll('body *')].filter(node=>node.getBoundingClientRect().right>document.documentElement.clientWidth+1 && getComputedStyle(node).position!=='absolute').slice(0,12).map(node=>({tag:node.tagName,classes:node.className,right:node.getBoundingClientRect().right}))}));
        assert(dimensions.scroll <= dimensions.width + 1, `${route} overflows at ${width}: ${JSON.stringify(dimensions)}`);
        if (route === '/architecture/') {
          assert.equal(await page.locator('.build-status-state').allTextContents().then(values => values.join('|')), 'Not checked|Not checked|Not checked');
          assert(await page.locator('[data-document-source="docs/unary-byte-frame-law.md"]').textContent().then(text=>text.includes('Universal Unary Byte-Frame Law')));
          await page.locator('.build-status-link').focus();
          assert.equal(await page.locator('.build-status-link').evaluate(node=>getComputedStyle(node).outlineStyle), 'solid');
        }
        if (route === '/reading/') {
          assert.equal(await page.locator('[data-document-source]').count(), documents.length);
          for (const document of documents) {
            const node = page.locator(`[data-document-source="${document.source}"]`);
            assert.equal(await node.getAttribute('data-document-digest'), document.digest);
            assert((await node.textContent()).trim().length > 20, document.source + ' empty');
          }
        }
        await page.screenshot({path:`render-evidence/${base ? 'project' : 'root'}-${width}-${route.replace(/[^a-z]/g,'') || 'index'}.png`});
        receipts.push({base,width,route,status:response.status(),dimensions});
      }
      assert.deepEqual(failures, []);
      await page.close();
    }
    fs.writeFileSync(`render-evidence/${base ? 'project' : 'root'}-results.json`, JSON.stringify({documents:documents.length,receipts},null,2));
    console.log(JSON.stringify({result:'PASS',base,documents:documents.length,pages:receipts.length}));
  } finally { await browser.close(); server.close(); }
})().catch(error=>{ console.error(error); server.close(); process.exitCode=1; });

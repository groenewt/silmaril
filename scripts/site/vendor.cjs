// Install declared mathematical rendering assets into the generated site.
const fs = require('node:fs');
const path = require('node:path');
const source = path.dirname(require.resolve('katex/package.json'));
fs.cpSync(path.join(source, 'dist'), 'docs/assets/vendor/katex', {recursive:true});
fs.copyFileSync(path.join(source, 'LICENSE'), 'docs/assets/vendor/katex/LICENSE');

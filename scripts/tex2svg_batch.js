// Batch TeX -> SVG renderer for the EPUB pipeline.
// stdin:  JSON array of {id, tex, display}
// stdout: JSON object {id: svg}
// Each SVG is self-contained (local font cache), uses currentColor, and
// display equations get max-width:100% so long equations scale down to the
// reader's screen instead of overflowing (the iOS Books failure mode).
const { mathjax } = require('mathjax-full/js/mathjax.js');
const { TeX } = require('mathjax-full/js/input/tex.js');
const { SVG } = require('mathjax-full/js/output/svg.js');
const { liteAdaptor } = require('mathjax-full/js/adaptors/liteAdaptor.js');
const { RegisterHTMLHandler } = require('mathjax-full/js/handlers/html.js');
const { AllPackages } = require('mathjax-full/js/input/tex/AllPackages.js');

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const tex = new TeX({ packages: AllPackages });
const svg = new SVG({ fontCache: 'local' });
const doc = mathjax.document('', { InputJax: tex, OutputJax: svg });

let input = '';
process.stdin.on('data', (d) => (input += d));
process.stdin.on('end', () => {
  const jobs = JSON.parse(input);
  const out = {};
  let failures = 0;
  for (const job of jobs) {
    try {
      const node = doc.convert(job.tex, { display: !!job.display });
      let s = adaptor.outerHTML(node);
      // unwrap the <mjx-container>
      const m = s.match(/<svg[\s\S]*<\/svg>/);
      s = m ? m[0] : s;
      // Empty path data (invisible glyphs like U+2061) serializes as a bare
      // `d` attribute; pandoc's EPUB writer re-serializes even d="" back to
      // that form, which is fatal XML in XHTML. Use a degenerate real path.
      s = s.replace(/ d(\s*\/>)/g, ' d="M0 0"$1')
           .replace(/ d(\s+[a-zA-Z-]+=)/g, ' d="M0 0"$1')
           .replace(/ d(\s*>)/g, ' d="M0 0"$1')
           .replace(/ d=""/g, ' d="M0 0"');
      // Display equations: block-centered, scale-to-fit, and with vertical
      // breathing room. MathJax's viewBox hugs the glyphs exactly, and some
      // readers (iOS Books) shave the bottom edge via ex->px rounding and
      // the UA's overflow:hidden — so pad the viewBox and allow overflow.
      // NB: styles must merge into any existing style attribute — a
      // duplicate attribute is a fatal XML error in XHTML/EPUB.
      if (job.display) {
        const PAD = 100; // MathJax internal units (1ex = 442); ~0.23ex each side
        s = s.replace(/viewBox="([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)"/,
          (mm, x, y, w, h) =>
            `viewBox="${x} ${Number(y) - PAD} ${w} ${Number(h) + 2 * PAD}"`);
        s = s.replace(/height="([\d.]+)ex"/,
          (mm, h) => `height="${(Number(h) + (2 * PAD) / 442).toFixed(3)}ex"`);
        const css = 'display:block;margin:0.6em auto;max-width:100%;height:auto;overflow:visible;';
        if (/<svg[^>]*style="/.test(s)) {
          s = s.replace(/(<svg[^>]*style=")/, `$1${css}`);
        } else {
          s = s.replace('<svg', `<svg style="${css}"`);
        }
      }
      out[job.id] = s;
    } catch (e) {
      failures++;
      process.stderr.write(`FAIL ${job.id}: ${String(e.message).slice(0, 120)}\n`);
    }
  }
  process.stderr.write(`rendered ${Object.keys(out).length}/${jobs.length} (${failures} failures)\n`);
  process.stdout.write(JSON.stringify(out));
});

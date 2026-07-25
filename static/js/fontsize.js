// Reader font-size control (A- / A+), persisted per device.
// Scales body text via --reader-scale; KaTeX follows (it is sized in em).
(function () {
  var KEY = 'reader-font-scale';
  var STEPS = [0.85, 0.925, 1, 1.075, 1.15, 1.25, 1.35];

  function current() {
    var v = parseFloat(localStorage.getItem(KEY));
    return STEPS.indexOf(v) >= 0 ? v : 1;
  }
  function apply(v) {
    document.documentElement.style.setProperty('--reader-scale', v);
  }
  function step(delta) {
    var i = STEPS.indexOf(current()) + delta;
    if (i < 0 || i >= STEPS.length) return;
    try { localStorage.setItem(KEY, STEPS[i]); } catch (e) {}
    apply(STEPS[i]);
  }

  apply(current());

  function makeButton(cls, text, label, delta) {
    var b = document.createElement('button');
    b.className = cls;
    b.textContent = text;
    b.title = label;
    b.setAttribute('aria-label', label);
    b.addEventListener('click', function () { step(delta); });
    return b;
  }

  function inject() {
    var right = document.querySelector('.navbar__items--right');
    if (!right || right.querySelector('.fontsize-ctl')) return;
    var wrap = document.createElement('div');
    wrap.className = 'fontsize-ctl';
    wrap.appendChild(makeButton('fs-minus', 'A', 'Smaller text', -1));
    wrap.appendChild(makeButton('fs-plus', 'A', 'Larger text', +1));
    right.insertBefore(wrap, right.firstChild);
  }

  var timer = null;
  function schedule() { clearTimeout(timer); timer = setTimeout(inject, 150); }
  function start() {
    inject();
    new MutationObserver(schedule).observe(document.body, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();

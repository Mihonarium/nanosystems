// Makes numbered KaTeX equation tags clickable permalinks.
// Anchors (<a class="eq-anchor" id="eq-N-M">) are emitted by chapters_split.py
// right before each tagged display equation.
(function () {
  function clean(s) { return s.replace(/[\u200B\u200C\uFEFF\s]/g, ''); }

  function wrap(node, id, num) {
    if (node.querySelector('a.eq-permalink') || node.closest('a')) return false;
    var link = document.createElement('a');
    link.href = '#' + id;
    link.className = 'eq-permalink';
    link.title = 'Link to equation ' + num;
    while (node.firstChild) link.appendChild(node.firstChild);
    node.appendChild(link);
    return true;
  }

  function enhance() {
    document.querySelectorAll('a.eq-anchor').forEach(function (a) {
      if (a.dataset.eqDone) return;
      var el = a.nextElementSibling;
      while (el && el.classList && el.classList.contains('eq-anchor')) el = el.nextElementSibling;
      if (!el || !el.querySelectorAll) return;
      var num = a.id.replace(/^eq-/, '').replace(/-/g, '.');
      var target = '(' + num + ')';
      el.querySelectorAll('.katex .tag').forEach(function (t) {
        if (a.dataset.eqDone) return;
        if (clean(t.textContent) === target) {
          if (wrap(t, a.id, num)) a.dataset.eqDone = '1';
          return;
        }
        // multi-tag block (align with several \tag rows): find the innermost
        // span holding exactly this number
        var nodes = [].slice.call(t.querySelectorAll('span')).filter(function (n) {
          return clean(n.textContent) === target;
        });
        var leaf = nodes.filter(function (n) {
          return !nodes.some(function (m) { return m !== n && n.contains(m); });
        }).pop();
        if (leaf && wrap(leaf, a.id, num)) a.dataset.eqDone = '1';
      });
    });
  }

  var timer = null;
  function schedule() { clearTimeout(timer); timer = setTimeout(enhance, 150); }
  function start() {
    enhance();
    new MutationObserver(schedule).observe(document.body, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();

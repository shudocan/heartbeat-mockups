(function () {
  var toast = document.querySelector('.toast'), timer;
  function say(msg) {
    if (!toast) return;
    toast.textContent = msg; toast.classList.add('on');
    clearTimeout(timer); timer = setTimeout(function () { toast.classList.remove('on'); }, 2400);
  }
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest('[data-mock]');
    if (a) { ev.preventDefault(); say('That page isn’t part of this mockup.'); }
  });
  document.querySelectorAll('[data-mockform]').forEach(function (f) {
    f.addEventListener('submit', function (ev) { ev.preventDefault(); say('The cart and search aren’t connected in this mockup.'); });
  });
  var menu = document.querySelector('.menu'), nav = document.getElementById('nav');
  if (menu && nav) menu.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    menu.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  var results = document.querySelector('[data-results]');
  if (!results) return;
  var items = Array.prototype.slice.call(results.children), original = items.slice();
  var form = document.querySelector('.filters'), sort = document.querySelector('[data-sort]');
  var count = document.querySelector('[data-count]');
  function apply() {
    var fam = [].map.call(form.querySelectorAll('[name=family]:checked'), function (i) { return i.value; });
    var yds = [].map.call(form.querySelectorAll('[name=yards]:checked'), function (i) { return i.value; });
    var shown = 0;
    items.forEach(function (el) {
      var ok = (!fam.length || fam.indexOf(el.dataset.family) > -1) && (!yds.length || yds.indexOf(el.dataset.yards) > -1);
      el.hidden = !ok; if (ok) shown++;
    });
    count.textContent = shown + (shown === 1 ? ' thread' : ' threads');
  }
  function order() {
    var v = sort.value, list = original.slice();
    if (v === 'name') list.sort(function (a, b) { return a.dataset.name.localeCompare(b.dataset.name); });
    if (v === 'low') list.sort(function (a, b) { return a.dataset.price - b.dataset.price; });
    if (v === 'high') list.sort(function (a, b) { return b.dataset.price - a.dataset.price; });
    list.forEach(function (el) { results.appendChild(el); });
  }
  form.addEventListener('change', apply);
  form.addEventListener('reset', function () { setTimeout(apply, 0); });
  sort.addEventListener('change', order);
  apply();
})();

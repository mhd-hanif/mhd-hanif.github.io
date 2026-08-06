/* Site behaviour: nav, theme, news toggle, BibTeX panels. */
(function () {
  'use strict';

  var doc = document;

  /* ---- Mobile navigation ------------------------------------------------ */
  var toggle = doc.querySelector('.nav-toggle');
  var menu = doc.getElementById('nav-menu');

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });

    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        menu.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---- Sticky nav shadow ------------------------------------------------ */
  var nav = doc.getElementById('site-nav');
  if (nav) {
    var onScroll = function () {
      nav.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- Theme toggle ----------------------------------------------------- */
  var themeBtn = doc.querySelector('.theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      var current = doc.documentElement.getAttribute('data-theme') ||
        (prefersDark ? 'dark' : 'light');
      var next = current === 'dark' ? 'light' : 'dark';
      doc.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }

  /* ---- News "show more" ------------------------------------------------- */
  var showMore = doc.querySelector('.show-more');
  var newsList = doc.querySelector('.news-list');
  if (showMore && newsList) {
    var labelMore = showMore.innerHTML;
    showMore.addEventListener('click', function () {
      var expanded = newsList.classList.toggle('is-expanded');
      showMore.setAttribute('aria-expanded', String(expanded));
      showMore.innerHTML = expanded
        ? 'Show fewer updates <span class="chev" aria-hidden="true">&darr;</span>'
        : labelMore;
    });
  }

  /* ---- BibTeX panels ---------------------------------------------------- */
  doc.addEventListener('click', function (e) {
    var trigger = e.target.closest('.btn-bibtex');
    if (trigger) {
      var panel = trigger.closest('.pub-body, .page-head').querySelector('.bibtex-panel');
      if (panel) {
        var open = panel.hasAttribute('hidden');
        if (open) { panel.removeAttribute('hidden'); } else { panel.setAttribute('hidden', ''); }
        trigger.setAttribute('aria-expanded', String(open));
      }
      return;
    }

    var copyBtn = e.target.closest('.bibtex-copy');
    if (copyBtn) {
      var code = copyBtn.parentNode.querySelector('code');
      if (!code) { return; }
      var text = code.textContent;
      var done = function () {
        var original = copyBtn.textContent;
        copyBtn.textContent = 'Copied';
        setTimeout(function () { copyBtn.textContent = original; }, 1600);
      };

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () {});
      } else {
        var ta = doc.createElement('textarea');
        ta.value = text;
        ta.setAttribute('readonly', '');
        ta.style.position = 'absolute';
        ta.style.left = '-9999px';
        doc.body.appendChild(ta);
        ta.select();
        try { doc.execCommand('copy'); done(); } catch (err) {}
        doc.body.removeChild(ta);
      }
    }
  });

  /* ---- Mark the current nav item --------------------------------------- */
  var path = window.location.pathname.replace(/\/+$/, '') || '/';
  doc.querySelectorAll('.nav-menu a').forEach(function (link) {
    var href = link.getAttribute('href') || '';
    if (href.indexOf('#') !== -1) { return; }
    var target = href.replace(/\/+$/, '') || '/';
    if (target !== '/' && path.indexOf(target) === 0) {
      link.setAttribute('aria-current', 'page');
    }
  });
})();

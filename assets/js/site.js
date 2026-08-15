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

  /* ---- Count CV opens -------------------------------------------------- */
  /* A page view says someone arrived; a CV open says they were interested,
     which is the more useful signal on a portfolio. Recorded as a GoatCounter
     event so it lands beside the page list rather than looking like a page.

     Everything here is conditional on window.goatcounter existing, so nothing
     happens on local builds -- where the counter script is not emitted at all
     -- or for readers who block it. The link is never interfered with: the
     event is fired and the browser follows the href as normal.

     Restricted to PDFs hosted here. Publication "Paper" chips also end in
     .pdf, but they are somebody else's file on somebody else's domain, and
     they arrive named things like 0252.pdf -- nothing worth a row. */
  doc.addEventListener('click', function (e) {
    var link = e.target.closest ? e.target.closest('a[href$=".pdf"]') : null;
    if (!link || link.hostname !== window.location.hostname) { return; }
    if (!window.goatcounter || typeof window.goatcounter.count !== 'function') { return; }
    var file = (link.getAttribute('href') || '').split('/').pop();
    window.goatcounter.count({
      path:  'download/' + file,
      title: 'PDF opened: ' + file,
      event: true
    });
  });
})();

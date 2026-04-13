(function () {
  'use strict';

  /** Path prefix from this page to site root (directory containing index.html + tests.html). */
  function upToSiteRoot() {
    const segs = location.pathname.split('/').filter(Boolean);
    if (segs.length && /\.html?$/i.test(segs[segs.length - 1])) segs.pop();
    const ti = segs.indexOf('tests');
    if (ti >= 0) {
      const inside = segs.length - ti - 1;
      return '../'.repeat(inside + 1);
    }
    return segs.length > 1 ? '../'.repeat(segs.length - 1) : './';
  }

  const root = upToSiteRoot();
  const home = root + 'index.html';
  const tests = root + 'tests.html';
  const testsBase = root + 'tests/';

  const CSS =
    '.iz-tpn-wrap{font-family:system-ui,-apple-system,sans-serif;font-size:0.92rem;line-height:1.35}' +
    '.iz-tpn-site,.iz-tpn-chem{display:flex;flex-wrap:wrap;gap:0.45rem 1rem;align-items:center;' +
    'justify-content:center;padding:0.55rem 1rem;margin:0}' +
    '.iz-tpn-site{background:#0f172a;color:#e2e8f0;border-bottom:1px solid #334155}' +
    '.iz-tpn-site a{color:#7dd3fc;text-decoration:none;font-weight:600}' +
    '.iz-tpn-site a:hover{text-decoration:underline;color:#bae6fd}' +
    '.iz-tpn-chem{background:#1e293b;color:#cbd5e1;border-bottom:1px solid #475569;justify-content:flex-start}' +
    '.iz-tpn-chem .iz-tpn-lab{color:#94a3b8;font-weight:600;margin-right:0.25rem}' +
    '.iz-tpn-chem a{color:#93c5fd;text-decoration:none;font-weight:500}' +
    '.iz-tpn-chem a:hover{text-decoration:underline;color:#bfdbfe}' +
    '.iz-tpn-bot .iz-tpn-site{border-bottom:none;border-top:1px solid #334155}' +
    '.iz-tpn-bot .iz-tpn-chem{border-bottom:none;border-top:1px solid #475569}';

  const CHEM = [
    {
      key: 'photochem',
      match: function (p) {
        return p.indexOf('/photochem_multi_geom_active_space/') !== -1;
      },
      href: 'photochem_multi_geom_active_space/index.html',
      label: 'Photochemistry (multi-geometry)',
    },
    {
      key: 'ethylene3d',
      match: function (p) {
        return p.indexOf('ethylene_3d_zor.html') !== -1;
      },
      href: 'qc_gaps_h2_ethylene_unified/ethylene_3d_zor.html',
      label: 'Ethylene 3D (quasi-degenerate regions)',
    },
    {
      key: 'qcgaps',
      match: function (p) {
        return (
          p.indexOf('/qc_gaps_h2_ethylene_unified/') !== -1 &&
          p.indexOf('ethylene_3d_zor') === -1
        );
      },
      href: 'qc_gaps_h2_ethylene_unified/index.html',
      label: 'QC gaps (H₂ & ethylene)',
    },
    {
      key: 'comparative',
      match: function (p) {
        return p.indexOf('/active_space_comparative/') !== -1;
      },
      href: 'active_space_comparative/index.html',
      label: '8-benchmark comparative',
    },
    {
      key: 'cr2',
      match: function (p) {
        return p.indexOf('/active_space_cr2/') !== -1;
      },
      href: 'active_space_cr2/index.html',
      label: 'Cr₂ active space',
    },
    {
      key: 'n2',
      match: function (p) {
        return p.indexOf('/active_space_n2/') !== -1;
      },
      href: 'active_space_n2/index.html',
      label: 'N₂ active space',
    },
  ];

  function currentChemKey(path) {
    for (let i = 0; i < CHEM.length; i++) {
      if (CHEM[i].match(path)) return CHEM[i].key;
    }
    return null;
  }

  function siteNavHtml() {
    return (
      '<nav class="iz-tpn-site" aria-label="Site">' +
      '<a href="' +
      home +
      '">Home</a>' +
      '<span style="opacity:.45">·</span>' +
      '<a href="' +
      tests +
      '">Research Tests</a>' +
      '</nav>'
    );
  }

  function peerNavHtml(fromKey) {
    const parts = [];
    for (let i = 0; i < CHEM.length; i++) {
      const c = CHEM[i];
      if (c.key === fromKey) continue;
      parts.push(
        '<a href="' + testsBase + c.href + '">' + c.label + '</a>'
      );
    }
    return (
      '<nav class="iz-tpn-chem" aria-label="Related quantum chemistry studies">' +
      '<span class="iz-tpn-lab">Other quantum chemistry studies:</span>' +
      parts.join('<span style="opacity:.35"> · </span>') +
      '</nav>'
    );
  }

  function inject() {
    if (document.getElementById('iz-tpn-style')) return;
    const st = document.createElement('style');
    st.id = 'iz-tpn-style';
    st.textContent = CSS;
    document.head.appendChild(st);

    const path = location.pathname;
    const chemKey = currentChemKey(path);

    const top = document.createElement('div');
    top.className = 'iz-tpn-wrap iz-tpn-top';
    top.innerHTML =
      siteNavHtml() + (chemKey ? peerNavHtml(chemKey) : '');

    const bot = document.createElement('div');
    bot.className = 'iz-tpn-wrap iz-tpn-bot';
    bot.innerHTML = siteNavHtml();

    document.body.insertAdjacentElement('afterbegin', top);
    document.body.appendChild(bot);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inject);
  } else {
    inject();
  }
})();

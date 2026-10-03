// Save the open page as a text file with a header that records its source.
// Run it in the page (Claude in Chrome's javascript tool, or the DevTools console).
// Use a fresh tab for each page: Chrome allows one automatic download per tab.
await (async () => {
  const C = {
    p: '09_OC_',       // case number and class, for example 10_MC_
    fb: '2025-08-18',  // date to use if the page metadata gives none
    s: '_GHF_001',     // _Source_NNN
    force: null,       // a complete doc_id to use regardless of metadata, or null
    dom: false,        // true copies all text in the page, including collapsed sections
    sel: null          // CSS selector of the element to copy, or null for automatic choice
  };
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 20 && !document.body; i++) await sleep(250);
  if (location.protocol === 'chrome-error:') return 'The page did not load.';
  const head = document.title + ' ' + document.body.innerText.slice(0, 600);
  if (/automated user|short interruption|verify you are human|security verification|page not found/i.test(head))
    return 'A security check or a missing page. Do not interact; wait, and if the page loads, save it from a fresh tab.';
  window.scrollTo(0, document.body.scrollHeight);           // let lazy content load
  let last = -1, stable = 0;
  for (let i = 0; i < 6; i++) {
    await sleep(400);
    const L = document.body.innerText.length;
    if (L === last) { if (++stable >= 2) break; } else { stable = 0; last = L; }
  }
  window.scrollTo(0, 0);
  const metaSel = ['meta[property="article:published_time"]', 'meta[name="article:published_time"]',
    'meta[property="og:published_time"]', 'meta[name="date"]', 'meta[name="pubdate"]',
    'meta[itemprop="datePublished"]', 'meta[name="publish-date"]', 'meta[name="parsely-pub-date"]',
    'meta[name="sailthru.date"]', 'meta[name="dcterms.date"]', 'meta[name="DC.date"]'];
  let pub = null;
  for (const s of metaSel) { const m = document.querySelector(s); if (m && m.content) { pub = m.content; break; } }
  if (!pub) { const t = document.querySelector('time[datetime]'); if (t) pub = t.getAttribute('datetime'); }
  if (!pub) {
    try {
      for (const sc of document.querySelectorAll('script[type="application/ld+json"]')) {
        const j = JSON.parse(sc.textContent);
        const arr = Array.isArray(j) ? j : (j['@graph'] || [j]);
        for (const o of arr) { if (o && o.datePublished) { pub = o.datePublished; break; } }
        if (pub) break;
      }
    } catch (e) {}
  }
  const mod = (document.querySelector('meta[property="article:modified_time"]') || {}).content || null;
  const d = (pub && /^\d{4}-\d{2}-\d{2}/.test(pub)) ? pub.slice(0, 10) : C.fb;
  const docId = C.force || (C.p + d + C.s);
  let el, en;                                                // the element to copy
  if (C.sel && document.querySelector(C.sel)) { el = document.querySelector(C.sel); en = C.sel; }
  else {
    const arts = [...document.querySelectorAll('article')].filter(a => a.innerText.length > 1500);
    if (arts.length === 1) { el = arts[0]; en = 'article'; }
    else if (document.querySelector('main') && document.querySelector('main').innerText.length > 800) { el = document.querySelector('main'); en = 'main'; }
    else { el = document.body; en = 'body'; }
  }
  const W = n0 => {                                          // all DOM text, for collapsed sections
    let o = '';
    for (const n of n0.childNodes) {
      if (n.nodeType === 3) o += n.nodeValue;
      else if (n.nodeType === 1) {
        const t = n.tagName;
        if (/^(SCRIPT|STYLE|NOSCRIPT|SVG|IFRAME)$/.test(t)) continue;
        if (/cookie/i.test((n.id || '') + ' ' + (typeof n.className === 'string' ? n.className : ''))) continue;
        const b = /^(P|DIV|LI|UL|OL|H[1-6]|TR|TABLE|SECTION|ARTICLE|BLOCKQUOTE|BR|DT|DD|FIGCAPTION|HEADER|FOOTER|ASIDE|NAV|DETAILS|SUMMARY)$/.test(t);
        if (b) o += '\n'; o += W(n); if (b) o += '\n';
      }
    }
    return o;
  };
  const text = C.dom
    ? W(el).replace(/[ \t ]+/g, ' ').split('\n').map(s => s.trim()).join('\n').replace(/\n{3,}/g, '\n\n').trim()
    : el.innerText;
  const how = C.dom ? `DOM text of the <${en}> element, including collapsed sections, whitespace normalised`
                    : `innerText of the <${en}> element, saved verbatim from the browser`;
  const content = `doc_id: ${docId}\ntitle: ${document.title}\nurl: ${location.href}\npublished_meta: ${pub || 'not found'}\n` +
                  `modified_meta: ${mod || 'not found'}\nretrieved: ${new Date().toISOString()}\ncopy: ${how}\n---\n` + text;
  let sha = 'n/a';
  if (window.crypto && crypto.subtle) {
    const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(content));
    sha = [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
  }
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([content], { type: 'text/plain;charset=utf-8' }));
  a.download = docId + '.txt'; document.body.appendChild(a); a.click(); a.remove();
  return JSON.stringify({ docId, element: en, chars: text.length, sha256: sha, published: pub });
})()

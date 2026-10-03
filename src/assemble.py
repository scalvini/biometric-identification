"""Join the corpus template and the textual analysis template into index.html.

Reads src/corpus/template.html, src/analysis/template.html, data/corpus/docs.json and
data/analysis/payload.json. Writes build/artifact.html, the page as published to claude.ai
(which adds its own document head), and index.html, the same page as a complete HTML document
with a robots "noindex" tag.
Run from the repository root: python3 src/assemble.py
"""
import json, re, os

S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = open(os.path.join(S, 'src', 'corpus', 'template.html'), encoding='utf-8').read()
T = open(os.path.join(S, 'src', 'analysis', 'template.html'), encoding='utf-8').read()

def between(s, a, b):
    i = s.index(a) + len(a)
    return s[i:s.index(b, i)]

def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, f"expected {n}, found {c}: {a[:90]!r}"
    return s.replace(a, b)

# ------------------------------------------------------------------ CSS
c_css = between(C, '<style>', '</style>')
t_css = between(T, '<style>', '</style>')

# design note
c_css = re.sub(r'^\s*/\*.*?\*/', '\n/* Single light theme on white.\n   Layout: one archive in two parts. A masthead with the case distribution, then tabs in two labelled groups,\n   the corpus (ledger, timeline, tables, corpus construction) and the textual analysis (annotated texts, matrix,\n   readings across cases, term counts, method). The record drawer opens from the right on any tab. */', c_css, count=1, flags=re.S)

# tokens of the analysis that the corpus page lacks
root_t = between(t_css, ':root {', '}')
extra = [l for l in root_t.split('\n') if l.strip().startswith(('--flash', '--b-'))]
serif = [l for l in root_t.split('\n') if l.strip().startswith('--f-serif')]
c_css = rep(c_css, '  --c-mz: #4F428A;\n', '  --c-mz: #4F428A;\n' + '\n'.join(extra) + '\n')
c_css = re.sub(r'(  --f-sans: [^\n]*\n)', lambda m: m.group(1) + serif[0] + '\n', c_css, count=1)
c_css = rep(c_css, '.wrap { max-width: 1180px;', '.wrap { max-width: 1240px;')

# grouped tabs replace the corpus tab rules
c_css = re.sub(r'/\* tabs \*/.*?(?=/\* filters \*/)', '''/* tabs, one row for each part of the archive */
.tabs { display: grid; margin: 20px 0 20px; border-bottom: 1px solid var(--rule); }
.tgroup { display: flex; flex-wrap: wrap; align-items: flex-end; gap: 0 2px; }
.tgroup + .tgroup { border-top: 1px solid var(--rule-2); }
.tglabel { flex: 0 0 156px; align-self: center; font: 500 12px/1 var(--f-mono); letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-3); }
.tabs button { appearance: none; border: 0; background: none; color: var(--ink-2); font: 600 16px/1 var(--f-sans); padding: 13px 11px 11px; border-bottom: 3px solid transparent; margin-bottom: -1px; cursor: pointer; }
.tabs button[aria-selected="true"] { color: var(--accent); border-bottom-color: var(--accent); }
.tabs button:hover { color: var(--ink); }
@media (max-width: 760px) {
  .tglabel { flex-basis: 100%; margin: 10px 0 0; }
  .tabs button { padding: 11px 8px 10px; font-size: 15px; }
}

''', c_css, count=1, flags=re.S)

# analysis CSS without its own tokens, base rules, masthead and tabs
t_css = t_css[t_css.index('/* category colour classes */'):]
DROP = ('.masthead {', 'h1 {', '.lede {', '.stats {', '.stats div {', '.stats dt {', '.stats dd {',
        '.tabs {', '.tabs button {', '.tabs button[aria-selected="true"] {', '.tabs button:hover {', '.tbl-wrap {')
RENAME = {'.check {': '.rail .check {', '.count {': '#acount {', '.count b {': '#acount b {', '.dbody {': '.docbody {',
          '.meta {': '.dmeta {', '.meta .mono {': '.dmeta .mono {', '.flag {': '.tflag {', '.empty {': '.ta .empty {',
          'table {': '.ta table {', 'th, td {': '.ta th, .ta td {', 'th {': '.ta th {', 'td.num, th.num {': '.ta td.num, .ta th.num {',
          'tr.group td {': '.ta tr.group td {', 'tr.missing td {': '.ta tr.missing td {', 'tr.total td {': '.ta tr.total td {',
          '.tnotes {': '.ta .tnotes {', '.tnotes li {': '.ta .tnotes li {'}
seen = {k: 0 for k in list(RENAME) + list(DROP)}
out = []
for line in t_css.split('\n'):
    hit = next((k for k in DROP if line.startswith(k)), None)
    if hit:
        seen[hit] += 1; continue
    hit = next((k for k in sorted(RENAME, key=len, reverse=True) if line.startswith(k)), None)
    if hit:
        seen[hit] += 1; line = RENAME[hit] + line[len(hit):]
    out.append(line)
bad = {k: v for k, v in seen.items() if v != 1}
assert not bad, bad
t_css = '\n'.join(out)

new_css = '''
/* joined page */
.aband { display: grid; gap: 12px; margin: -4px 0 22px; }
.reclink, .golink { appearance: none; font: 600 13.5px/1 var(--f-sans); color: var(--accent); background: var(--panel); border: 1px solid var(--accent); border-radius: 4px; padding: 5px 8px; cursor: pointer; }
.reclink:hover, .golink:hover { background: var(--accent-soft); }
.golink { margin-left: 8px; }
'''
css = c_css + '\n/* ===== textual analysis ===== */\n' + t_css + new_css

# ------------------------------------------------------------------ markup
c_html = C.split('</style>', 1)[1].split('<script>', 1)[0]
t_html = T.split('</style>', 1)[1].split('<script>', 1)[0]

i0 = c_html.index('<section id="v-ledger"'); i2 = c_html.index('<div class="scrim"'); i1 = c_html.rindex('</div>', 0, i2)
corpus_sections = c_html[i0:i1].rstrip() + '\n'
drawer = c_html[i2:].strip() + '\n'
corpus_sections = rep(corpus_sections, 'id="v-provenance" role="tabpanel" aria-labelledby="t-provenance"', 'id="v-construction" role="tabpanel" aria-labelledby="t-construction"')
corpus_sections = rep(corpus_sections, 'Five documents are PDFs; the other 78 are web texts saved from the browser with a provenance header.',
                      'Five documents are PDFs, and the other 78 are web texts saved from the browser with a header that records the address and the time of retrieval.')

a0 = t_html.index('<section id="v-texts"'); a1 = t_html.index('<footer>')
an_sections = t_html[a0:a1].rstrip() + '\n'
for k in ('texts', 'matrix', 'readings', 'terms', 'method'):
    an_sections = rep(an_sections, f'aria-labelledby="tab-{k}"', f'aria-labelledby="t-{k}"')
an_sections = rep(an_sections, 'id="q"', 'id="aq"')
an_sections = rep(an_sections, 'id="count"', 'id="acount"')

fonts = T[T.index('<link rel="preconnect"'):T.index('<style>')]

def tab(k, label, sel=False):
    return f'<button role="tab" id="t-{k}" aria-controls="v-{k}" aria-selected="{str(sel).lower()}">{label}</button>'

markup = f'''<div class="wrap">
  <header class="masthead">
    <div class="eyebrow">Corpus Archive &middot; state on 3 October 2026</div>
    <h1>Biometric Identification</h1>
    <p class="lede">The archive holds documents on biometric identification as a condition of assistance, with UNHCR&rsquo;s identity-management guidance read as the node and four disputes from 2023 to 2026 read as its recontextualisations. The cases are Gaza, Malaysia, South Africa and Mizoram, and the textual analysis reads the 21 saved core texts at the first of Fairclough&rsquo;s three dimensions.</p>
    <div class="casebar" id="casebar" role="img"></div>
    <div class="legend" id="legend"></div>
    <dl class="stats" id="stats"></dl>
  </header>

  <nav class="tabs" role="tablist" aria-label="Views">
    <div class="tgroup" role="presentation"><span class="tglabel" aria-hidden="true">Corpus</span>
      {tab('ledger', 'Ledger', True)}
      {tab('timeline', 'Timeline')}
      {tab('core', 'Core corpus')}
      {tab('dataset', 'Dataset')}
      {tab('construction', 'Corpus construction')}
    </div>
    <div class="tgroup" role="presentation"><span class="tglabel" aria-hidden="true">Textual analysis</span>
      {tab('texts', 'Texts')}
      {tab('matrix', 'Matrix')}
      {tab('readings', 'Across cases')}
      {tab('terms', 'Terms')}
      {tab('method', 'Method')}
    </div>
  </nav>

  {corpus_sections}
  <div class="ta">
    <div class="aband" id="aband" hidden>
      <span class="status"><b>Provisional</b> first pass for review, 3 October 2026</span>
      <div class="key" id="akey" aria-label="Category key"></div>
    </div>
  {an_sections}
  </div>

  <footer>Built on 3 October 2026 from the archive copies listed in ARCHIVE_LOG.md. The textual analysis is a provisional first pass for the author&rsquo;s review.</footer>
</div>

{drawer}'''

# ------------------------------------------------------------------ scripts
c_js = between(C, '<script>', '</script>')
t_js = between(T, '<script>', '</script>')

c_js = c_js[:c_js.index('/* tabs */\nconst TABS')] + '''chips(); renderLedger(); renderTimeline(); renderCore(); renderDataset(); renderConstruction();
BI.openRecord = openDoc;
'''
c_js = rep(c_js, 'function renderProvenance() {', 'function renderConstruction() {')
c_js = rep(c_js, 'if (d.core) rows.push(["Core", esc(POS[d.core])]);',
           'if (d.core) rows.push(["Core", esc(POS[d.core]) + (BI.hasAnalysis(d.id) ? \'<button class="golink" type="button" data-an="\' + d.id + \'">Open its textual analysis</button>\' : "")]);')
c_js = rep(c_js, '$("#dbody").addEventListener("click", (e) => {\n  const b = e.target.closest("[data-copy]"); if (!b) return;',
           '$("#dbody").addEventListener("click", (e) => {\n  const g = e.target.closest("[data-an]"); if (g) { closeDoc(); BI.openAnalysis(g.dataset.an); return; }\n  const b = e.target.closest("[data-copy]"); if (!b) return;')

t_js = re.sub(r"\$\('stats'\)\.innerHTML = .*?\.join\(''\);",
              "$('stats').insertAdjacentHTML('beforeend', [['Excerpts analysed', DATA.stats.excerpts], ['Annotations', DATA.stats.ann]].map(([k, v]) => `<div><dt>${k}</dt><dd>${v}</dd></div>`).join(''));",
              t_js, count=1, flags=re.S)
t_js = rep(t_js, "$('key')", "$('akey')", 2)
t_js = rep(t_js, "$('q')", "$('aq')", 4)
t_js = rep(t_js, "$('count')", "$('acount')")
i = t_js.index('/* ---------- tabs ---------- */'); j = t_js.index('/* ---------- Texts: rail ---------- */')
t_js = t_js[:i] + "function setTab(t) { BI.show(t); }\n\n" + t_js[j:]
t_js = rep(t_js, '<div class="meta">', '<div class="dmeta">')
t_js = rep(t_js, '<span class="mono">${d.id}</span></div></div>${docBar(d)}</div>',
           '<span class="mono">${d.id}</span><button type="button" class="reclink" data-rec="${d.id}">Open the record</button></div></div>${docBar(d)}</div>')
t_js = rep(t_js, '<div class="dbody">', '<div class="docbody">')
t_js = rep(t_js, "$('docs').addEventListener('click', ev => {\n  const el = ev.target.closest('[data-a]'); if (!el) return;",
           "$('docs').addEventListener('click', ev => {\n  const rb = ev.target.closest('[data-rec]'); if (rb) { BI.openRecord(rb.dataset.rec); return; }\n  const el = ev.target.closest('[data-a]'); if (!el) return;")
t_js = rep(t_js, '<span class="flag">', '<span class="tflag">')
t_js = rep(t_js, 'after its provenance header', 'below the header that records its address')
t_js = t_js[:t_js.index("const h = (location.hash || '')")] + "BI.openAnalysis = (id) => goDoc(id);\nBI.hasAnalysis = (id) => !!DOC[id];\n"

router = '''window.BI = (function () {
  const GROUPS = { corpus: ['ledger', 'timeline', 'core', 'dataset', 'construction'], analysis: ['texts', 'matrix', 'readings', 'terms', 'method'] };
  const ALL = GROUPS.corpus.concat(GROUPS.analysis);
  const ALIAS = { provenance: 'construction' };
  const api = { current: 'ledger', openRecord: function () {}, openAnalysis: function () {}, hasAnalysis: function () { return false; } };
  api.show = function (tab, push) {
    tab = ALIAS[tab] || tab;
    if (ALL.indexOf(tab) < 0) tab = 'ledger';
    ALL.forEach(function (t) {
      const b = document.getElementById('t-' + t);
      b.setAttribute('aria-selected', String(t === tab));
      b.tabIndex = t === tab ? 0 : -1;
      document.getElementById('v-' + t).hidden = t !== tab;
    });
    document.getElementById('aband').hidden = GROUPS.analysis.indexOf(tab) < 0;
    api.current = tab;
    if (push !== false) { try { history.replaceState(null, '', '#' + tab); } catch (e) {} }
  };
  const nav = document.querySelector('.tabs');
  nav.addEventListener('click', function (e) { const b = e.target.closest('[role="tab"]'); if (b) api.show(b.id.slice(2)); });
  nav.addEventListener('keydown', function (e) {
    if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
    const i = ALL.indexOf(api.current), j = (i + (e.key === 'ArrowRight' ? 1 : ALL.length - 1)) % ALL.length;
    api.show(ALL[j]); document.getElementById('t-' + ALL[j]).focus(); e.preventDefault();
  });
  return api;
})();'''

page = ('<title>Biometric Identification</title>\n' + fonts + '<style>' + css + '</style>\n\n' + markup +
        '\n<script>\n' + router + '\n</script>\n<script>\n(function () {\n' + c_js + '\n})();\n</script>\n<script>\n(function () {\n' + t_js + '\n})();\n</script>\n<script>\nBI.show((location.hash || "").replace("#", "") || "ledger", false);\n</script>\n')

docs = json.load(open(os.path.join(S, 'data', 'corpus', 'docs.json'), encoding='utf-8'))
payload = json.load(open(os.path.join(S, 'data', 'analysis', 'payload.json'), encoding='utf-8'))
inj = lambda o: json.dumps(o, ensure_ascii=False).replace('</', '<\\/')
assert page.count('__DOCS__') == 1 and page.count('__DATA__') == 1
html = page.replace('__DOCS__', inj(docs)).replace('__DATA__', inj(payload))
os.makedirs(os.path.join(S, 'build'), exist_ok=True)
open(os.path.join(S, 'build', 'artifact.html'), 'w', encoding='utf-8').write(html)
k = html.index('</style>') + len('</style>')
full = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
        + html[:k] + '\n</head>\n<body>\n' + html[k:] + '</body>\n</html>\n')
open(os.path.join(S, 'index.html'), 'w', encoding='utf-8').write(full)
print('ok', len(html), 'bytes; provenance left:', len(re.findall('[Pp]rovenance', html.split('<script>')[0])), 'in markup and CSS')

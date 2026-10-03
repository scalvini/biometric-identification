"""Validate the annotations against the verified excerpts and write data/analysis/payload.json.

Every annotated span must occur in its excerpt; nested spans are allowed and partial overlaps
are errors. The script also checks the readings' evidence, and flags dashes in the analytic
prose. Run from the repository root: python3 src/analysis/build.py
"""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import annotations as D

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, 'data', 'analysis')
Q = {}
for line in open(os.path.join(DATA, 'excerpts.jsonl'), encoding='utf-8'):
    i, path, text = json.loads(line)
    Q[i] = {"path": path, "doc": path.split('/')[-1].rsplit('.', 1)[0], "t": text}
TERMS = json.load(open(os.path.join(DATA, 'terms.json'), encoding='utf-8'))

errors, warns = [], []
used = {}
codes = {c["c"] for c in D.CATS}
PROSE_DASH = re.compile('[–—]')

def check_prose(label, s):
    if s and PROSE_DASH.search(s):
        warns.append(f"dash in prose: {label}: {s[:80]}")

def locate(text, span, k=None):
    starts = [m.start() for m in re.finditer(re.escape(span), text)]
    if not starts:
        return None, 0
    if k is None:
        return starts[0], len(starts)
    if k >= len(starts):
        return None, len(starts)
    return starts[k], len(starts)

out_docs = []
n_ann = 0
for d in D.DOCS:
    check_prose(d["id"] + " voice", d["voice"])
    check_prose(d["id"] + " profile", d["profile"])
    exs = []
    for e in d["ex"]:
        q = e["q"]
        if q not in Q:
            errors.append(f"{d['id']}: excerpt {q} not in quotes")
            continue
        if Q[q]["doc"] != d["id"]:
            errors.append(f"{d['id']}: excerpt {q} belongs to {Q[q]['doc']}")
        used[q] = used.get(q, 0) + 1
        text = Q[q]["t"]
        check_prose(f"q{q} voice", e["v"])
        anns = []
        for a in e["a"]:
            if a["c"] not in codes:
                errors.append(f"q{q}: unknown code {a['c']}")
            st, cnt = locate(text, a["s"], a.get("k"))
            if st is None:
                errors.append(f"q{q}: span not found: {a['s']!r}")
                continue
            if cnt > 1 and a.get("k") is None:
                warns.append(f"q{q}: span {a['s']!r} occurs {cnt} times; first used")
            check_prose(f"q{q} note", a["n"])
            anns.append({"c": a["c"], "s": st, "e": st + len(a["s"]), "sub": a["sub"], "n": a["n"]})
            n_ann += 1
        # overlap report (partial overlaps are a rendering problem; nesting is fine)
        for i1, x in enumerate(anns):
            for y in anns[i1 + 1:]:
                if x["s"] < y["e"] and y["s"] < x["e"]:
                    nested = (x["s"] <= y["s"] and y["e"] <= x["e"]) or (y["s"] <= x["s"] and x["e"] <= y["e"])
                    if not nested:
                        errors.append(f"q{q}: partial overlap {text[x['s']:x['e']]!r} / {text[y['s']:y['e']]!r}")
        anns.sort(key=lambda z: (z["e"], -z["s"]))  # number notes in the order their markers appear
        ex = {"q": q, "t": text, "v": e["v"], "a": anns}
        if e.get("gl"):
            ex["gl"] = e["gl"]
        exs.append(ex)
    t = TERMS["docs"].get(d["id"])
    if t is None:
        errors.append(f"{d['id']}: no term counts")
    out_docs.append({k: d[k] for k in ("id", "g", "pos", "cls", "lang", "short", "title", "date", "voice", "profile")} | {"ex": exs, "terms": t})

unused = sorted(set(Q) - set(used))
dups = [q for q, c in used.items() if c > 1]
if dups:
    errors.append(f"excerpts used twice: {dups}")

readings = []
for r in D.READINGS:
    for p in r["p"]:
        check_prose(r["id"], p)
    ev = []
    for q, span in r["ev"]:
        if q not in used:
            errors.append(f"{r['id']}: evidence excerpt {q} not shown on the page")
            continue
        st, cnt = locate(Q[q]["t"], span)
        if st is None:
            errors.append(f"{r['id']}: evidence span not found in q{q}: {span!r}")
            continue
        ev.append({"q": q, "s": st, "e": st + len(span), "doc": Q[q]["doc"]})
    readings.append({"id": r["id"], "title": r["title"], "rq": r["rq"], "p": r["p"], "ev": ev})

for c in D.CATS:
    check_prose(c["c"], c["def"]); check_prose(c["c"], c["ask"])

payload = {"groups": D.GROUPS, "cats": D.CATS, "docs": out_docs, "missing": D.MISSING,
           "readings": readings, "terms": TERMS["terms"],
           "stats": {"docs": len(out_docs), "excerpts": len(used), "ann": n_ann}}

print("docs", len(out_docs), "excerpts", len(used), "annotations", n_ann, "unused quote ids", unused)
for w in warns: print("WARN", w)
for e in errors: print("ERROR", e)
if errors:
    sys.exit(1)
json.dump(payload, open(os.path.join(DATA, 'payload.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('payload written')

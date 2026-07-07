import re, os, json, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE, "batch1_data.json")
sys.path.insert(0, BASE)

from generate_data import DATA

# Write data to JSON for reference
if not os.path.exists(DATA_FILE):
    class CompactEncoder(json.JSONEncoder):
        def default(self, obj):
            return super().default(obj)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(DATA, f, ensure_ascii=False, indent=2)
    print(f"Wrote {DATA_FILE}")

FILES = [
    "401k-calculator/index.html","acceleration-calculator/index.html","ad-revenue-calculator/index.html",
    "age-calculator/index.html","alcohol-calorie-calculator/index.html","amortization-calculator/index.html",
    "annuity-calculator/index.html","annuity-payout-calculator/index.html","anorexic-bmi-calculator/index.html",
    "apr-calculator/index.html","area-calculator/index.html","army-body-fat-calculator/index.html",
    "atom-calculator/index.html","auto-lease-calculator/index.html","auto-loan-calculator/index.html",
    "average-return-calculator/index.html","bac-calculator/index.html","bandwidth-calculator/index.html",
    "base64-tool/index.html","basic-calculator/index.html","big-number-calculator/index.html",
    "binary-calculator/index.html","bio-link-ctr-calculator/index.html","bmi-calculator/index.html",
    "bmr-calculator/index.html","boat-loan-calculator/index.html","body-fat-calculator/index.html",
    "body-surface-area-calculator/index.html","body-type-calculator/index.html","bond-calculator/index.html",
    "boyles-law-calculator/index.html","bra-size-calculator/index.html","break-even-calculator/index.html",
    "brick-calculator/index.html","btu-calculator/index.html","budget-calculator/index.html",
    "buffer-calculator/index.html","business-loan-calculator/index.html","caffeine-calculator/index.html",
    "calorie-calculator/index.html","calorie-deficit-calculator/index.html","calories-burned-calculator/index.html",
    "canadian-mortgage-calculator/index.html","capacitance-calculator/index.html","carbohydrate-calculator/index.html",
    "cash-back-vs-low-interest-calculator/index.html","cd-calculator/index.html","cement-calculator/index.html",
]

def build_seo(name, intro1, intro2, h2, body, headers, rows, faqs):
    ths = "".join(f'<th style="padding:8px;border:1px solid #e2e8f0">{h}</th>' for h in headers)
    trs = ""
    for row in rows:
        tds = "".join(f'<td style="padding:8px;border:1px solid #e2e8f0">{c}</td>' for c in row)
        trs += f"                <tr>{tds}</tr>\n"
    table = f'''<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:15px">
              <thead><tr style="background:#f1f5f9;text-align:left">{ths}</tr></thead>
              <tbody>
{trs}              </tbody>
            </table>'''
    faq_dl = "\n".join(f"              <dt>{q}</dt>\n              <dd>{a}</dd>" for q, a in faqs)
    seo = f'''          <section class="ch-prerender-seo" aria-label="{name} - Guide & Reference">
            <h1>{name}</h1>
            <p>{intro1}</p>
            <p>{intro2}</p>
            <h2>{h2}</h2>
            <p>{body}</p>
            <h2>{name}: Key Reference</h2>
            {table}
            <h2>{name} - Frequently Asked Questions</h2>
            <dl>
{faq_dl}
            </dl>
          </section>'''
    me = ",\n".join(f'{{"@type":"Question","name":{json.dumps(q)},"acceptedAnswer":{{"@type":"Answer","text":{json.dumps(a)}}}}}' for q, a in faqs)
    ld = f'''    <script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{me}
]}}
    </script>'''
    return seo, ld

def process(filepath, seo_html, jsonld):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    pattern = r'<section class="ch-prerender-seo"[^>]*>.*?</section>'
    new_content = re.sub(pattern, seo_html, content, count=1, flags=re.DOTALL)
    if "FAQPage" not in new_content:
        new_content = new_content.replace("</head>", jsonld + "\n  </head>", 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

def main():
    updated = 0
    for fname in FILES:
        fp = os.path.join(BASE, fname)
        if not os.path.exists(fp):
            print(f"MISSING: {fname}")
            continue
        key = fname.replace("/", "-").replace(".html", "")
        d = DATA.get(key)
        if not d:
            print(f"NO DATA: {fname}")
            continue
        seo, ld = build_seo(d["name"], d["intro1"], d["intro2"], d["h2"], d["body"], d["th"], d["tr"], d["faqs"])
        process(fp, seo, ld)
        updated += 1
        print(f"OK: {fname}")
    print(f"\nDone: {updated}/{len(FILES)} files updated")

if __name__ == "__main__":
    main()

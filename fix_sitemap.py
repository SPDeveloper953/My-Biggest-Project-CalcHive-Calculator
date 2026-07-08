import os
from datetime import datetime

root = "C:\\Users\\sudai\\OneDrive\\Documents\\New OpenCode Project\\CalcHive-Calculator"
BASE_URL = "https://www.calchive.site"
OUTPUT = os.path.join(root, "sitemap.xml")

# Folders to EXCLUDE from the sitemap
EXCLUDE_DIRS = {"__pycache__", "assets", "node_modules", ".git", ".vercel"}
EXCLUDE_PREFIXES = {"blog/", "blog\\"}  # blog posts handled separately

pages = []

for dirpath, _, filenames in os.walk(root):
    if "index.html" not in filenames:
        continue
    if dirpath == root:
        pages.append(("homepage", BASE_URL + "/"))
        continue

    rel = os.path.relpath(dirpath, root).replace("\\", "/")

    # Skip excluded directories
    top_dir = rel.split("/")[0]
    if top_dir in EXCLUDE_DIRS:
        continue

    loc = f"{BASE_URL}/{rel}/"
    pages.append((rel, loc))

pages.sort(key=lambda x: x[0])

today = datetime.now().strftime("%Y-%m-%d")

lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for name, loc in pages:
    if name == "homepage":
        freq = "weekly"
        priority = "1.0"
    elif name.startswith("blog/"):
        freq = "monthly"
        priority = "0.7"
    else:
        freq = "monthly"
        priority = "0.8"

    lines.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

lines.append('</urlset>')

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Sitemap written: {len(pages)} pages ({pages[0][0] if pages else 'none'})")

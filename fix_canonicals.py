import os, re

root = "C:\\Users\\sudai\\OneDrive\\Documents\\New OpenCode Project\\CalcHive-Calculator"
BASE_URL = "https://www.calchive.site"
updated = 0
skipped = 0

for dirpath, _, filenames in os.walk(root):
    if "index.html" not in filenames:
        continue
    fp = os.path.join(dirpath, "index.html")

    # Skip root index.html
    if dirpath == root:
        continue

    # Get relative folder path
    rel = os.path.relpath(dirpath, root).replace("\\", "/")

    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    m = re.search(r'(<link[^>]*rel="canonical"[^>]*href=")([^"]+)("[^>]*/?>)', content, re.IGNORECASE)
    if not m:
        print(f"MISSING: {rel} (no canonical tag)")
        continue

    old_href = m.group(2)
    prefix = m.group(1)
    suffix = m.group(3)

    if not old_href.startswith(BASE_URL):
        print(f"SKIP: {rel} (unexpected href: {old_href})")
        skipped += 1
        continue

    path_part = old_href[len(BASE_URL):]
    if path_part == "/":
        correct_href = BASE_URL + "/"
    else:
        path_part = path_part.rstrip("/")
        correct_href = BASE_URL + path_part + "/"

    if old_href == correct_href:
        skipped += 1
        continue

    new_tag = prefix + correct_href + suffix
    old_tag = m.group(0)
    content = content.replace(old_tag, new_tag, 1)

    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"FIXED: {rel}  {old_href} -> {correct_href}")
    updated += 1

print(f"\nTotal: {updated} updated, {skipped} skipped")

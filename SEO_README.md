SEO automation README

What this PR adds
- scripts/generate-seo.js: a safe Node script that reads sitemap.xml, finds calculator routes, and updates each route's index.html by:
  - Replacing or inserting <title> and <meta name="description"> in the <head>
  - Injecting a FAQ JSON-LD script (FAQPage schema) into the head
  - Replacing or inserting the prerender SEO section (.ch-prerender-seo) with a short summary and a visible <dl> FAQ
- package.json: convenience script to run the generator (npm run generate-seo)

Safety and rollback
- The script creates a backup for every modified file as filename.bak-seo. To roll back:
  - Restore the original: mv path/to/index.html.bak-seo path/to/index.html

How to run (locally)
1) From the repo root, install Node if you don't have it (Node 12+).
2) Run: npm run generate-seo
3) Verify the changes locally (open modified index.html files).
4) Commit or revert backups as you prefer.

Why this approach
- Applying the changes programmatically reduces human errors across hundreds of pages.
- The script only edits static HTML files and creates backups — it does not touch JS bundles, CSS, service-worker, or assets.

Next steps if you want me to finish the PR
- I added these files to branch seo/auto-update-all-calculators. If you're comfortable, you can run the script in CI or locally and then commit the modified index.html files to this branch, or grant me explicit permission to run the modifications for you and commit them in this branch.

Notes
- The script uses simple heuristics to generate titles, descriptions, and FAQs. Review seo-content.json after running and tweak where needed.

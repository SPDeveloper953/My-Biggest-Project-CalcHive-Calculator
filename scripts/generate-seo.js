const fs = require('fs');
const path = require('path');

const SITE_ROOT = process.cwd();
const SITEMAP = path.join(SITE_ROOT, 'sitemap.xml');

function readSitemap() {
  if (!fs.existsSync(SITEMAP)) {
    console.error('sitemap.xml not found in repo root.');
    process.exit(1);
  }
  const xml = fs.readFileSync(SITEMAP, 'utf8');
  const locs = Array.from(xml.matchAll(/<loc>(https?:\\/\\/[^<]+)<\\/loc>/g)).map(m => m[1]);
  return locs;
}

function titleFromPath(p) {
  // /bmi-calculator -> BMI Calculator
  const slug = p.replace(/^https?:\/\/[^/]+/, '').replace(/^\/+/, '').replace(/\/+$/, '');
  if (!slug) return 'CalcHive';
  const parts = slug.split('/')[0].split('-').map(part => {
    if (part.length <= 2) return part.toUpperCase();
    return part.charAt(0).toUpperCase() + part.slice(1);
  });
  const title = parts.join(' ');
  if (/calculator$/i.test(title) || /converter$/i.test(title) || /tool$/i.test(title)) return title;
  return title + ' Calculator';
}

function shortTopic(title) {
  return title.replace(/\s+(Calculator|Converter|Generator|Roller|Counter|Tool)$/i, '').trim();
}

function categoryFromPath(p) {
  const slug = p.replace(/^https?:\/\/[^/]+/, '').toLowerCase();
  if (/mortgage|loan|interest|finance|retirement|payment|amortization|401k|ira|savings|tax|loan|mortgage/.test(slug)) return 'finance';
  if (/bmi|calorie|bmr|pregnancy|tdee|protein|health|body|weight|gfr|bmi/.test(slug)) return 'health';
  if (/youtube|tiktok|instagram|social|revenue|ad-revenue|cpm|earnings|subscriber/.test(slug)) return 'creator';
  if (/calculator$/.test(slug)) return 'default';
  return 'default';
}

function metaFor(title, category) {
  const topic = shortTopic(title);
  const templates = {
    finance: `Estimate ${topic.toLowerCase()} with our free ${topic} Calculator. Quick, private, and mobile-friendly.`,
    health: `Quickly calculate ${topic.toLowerCase()} with our free ${topic} Calculator — supports common units and gives practical guidance.`,
    creator: `Plan creator earnings with the ${topic} Calculator. Use realistic inputs to estimate revenue and reach.`,
    default: `Use the ${title} on CalcHive to get instant results. Fast, private, and no signup required.`
  };
  return templates[category] || templates.default;
}

function faqsFor(title, category) {
  const topic = shortTopic(title);
  const faqs = {
    finance: [
      { q: `How does the ${topic} Calculator work?`, a: `It uses standard financial formulas to compute results based on the inputs you provide. Use the example inputs to get started.` },
      { q: `Can I adjust the assumptions?`, a: `Yes — change rate, term, contributions, or other inputs to run different scenarios.` },
      { q: `Is this a substitute for professional advice?`, a: `No. Use the results for planning and confirm details with a qualified professional.` },
      { q: `Can I export or save results?`, a: `The tool runs in the browser; copy the numbers to save them. We do not require signup.` }
    ],
    health: [
      { q: `What does the ${topic} result mean?`, a: `The result is an estimate based on common formulas; use it as a quick reference and consult a clinician for personal medical advice.` },
      { q: `Which units are supported?`, a: `Metric and imperial units are supported where applicable; pick the one you prefer and enter values.` },
      { q: `Are my inputs stored?`, a: `No. Inputs are handled in your browser and are not uploaded to our servers.` },
      { q: `How accurate is the ${topic} Calculator?`, a: `It provides estimates. Accuracy depends on correct inputs and individual variation.` }
    ],
    creator: [
      { q: `How do I estimate realistic earnings?`, a: `Use actual metrics (views, RPM, CPM) and run multiple scenarios to see ranges rather than a single number.` },
      { q: `Can I compare platforms?`, a: `Yes — change the inputs to reflect platform-specific rates and audience sizes.` },
      { q: `Is this private?`, a: `Yes — calculations are done in your browser with no account required.` },
      { q: `Why do results vary?`, a: `Ad rates, geography, and niche affect revenue; treat results as planning estimates.` }
    ],
    default: [
      { q: `Is this ${topic} Calculator free to use?`, a: `Yes — CalcHive provides free, private calculators with no signup.` },
      { q: `Can the ${topic} results be trusted?`, a: `They are intended for estimation and learning. For critical decisions consult an expert.` },
      { q: `What inputs do I need?`, a: `Enter the values requested on the form — example placeholders help show typical inputs.` },
      { q: `Does this work on mobile?`, a: `Yes — the tool is responsive and works on modern mobile browsers.` }
    ]
  };
  return faqs[category] || faqs.default;
}

function injectIntoHtml(html, { title, description, faqs }) {
  // Replace or insert <title>
  if (/\<title\>.*?<\\/title\>/i.test(html)) {
    html = html.replace(/(\<title\>).*?(<\\/title>)/i, `$1${escapeHtml(title)}$2`);
  } else {
    html = html.replace(/<head(.*?)>/i, `<head$1>\n    <title>${escapeHtml(title)}</title>`);
  }

  // Replace or insert meta description
  if (/\<meta[^>]*name=["']description["'][^>]*>/i.test(html)) {
    html = html.replace(/(<meta[^>]*name=["']description["'][^>]*content=")[^"]*("[^>]*>)/i, `$1${escapeHtml(description)}$2`);
  } else if (/\<head[^>]*>/i.test(html)) {
    html = html.replace(/(<head[^>]*>)/i, `$1\n    <meta name="description" content="${escapeHtml(description)}" />`);
  }

  // Inject FAQ JSON-LD before </head>
  const faqJson = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faqs.map(f => ({
      "@type": "Question",
      name: f.q,
      acceptedAnswer: { "@type": "Answer", text: f.a }
    }))
  };
  const faqScript = `\n    <script type="application/ld+json">${JSON.stringify(faqJson, null, 2)}</script>\n`;
  if (/<script type=\"application\/ld\+json\">[\s\S]*?FAQPage[\s\S]*?<\\/script>/i.test(html)) {
    // replace existing FAQPage JSON-LD
    html = html.replace(/<script type=\"application\/ld\+json\">[\s\S]*?FAQPage[\s\S]*?<\\/script>/i, faqScript);
  } else {
    html = html.replace(/(<\/head>)/i, faqScript + '$1');
  }

  // Replace or insert prerender SEO section
  const summary = `<section class="ch-prerender-seo" aria-label="${escapeHtml(title)} summary">\n  <h1>${escapeHtml(title)}</h1>\n  <p>${escapeHtml(description)}</p>\n  <h2>${escapeHtml(title)} FAQ</h2>\n  <dl>\n    ${faqs.map(f => `<dt>${escapeHtml(f.q)}</dt>\n    <dd>${escapeHtml(f.a)}</dd>`).join('\n    ')}\n  </dl>\n</section>`;

  if (/\<section[^>]+class=["'][^"']*ch-prerender-seo[^"']*["'][\s\S]*?<\\/section>/i.test(html)) {
    html = html.replace(/(\<section[^>]+class=["'][^"']*ch-prerender-seo[^"']*["'][\s\S]*?<\\/section>)/i, summary);
  } else {
    // try to insert before closing main or before closing body
    if (/\<main[\s\S]*?<\\/main>/i.test(html)) {
      html = html.replace(/(\<\\main>)/i, summary + '\n$1');
    } else {
      html = html.replace(/(\<\\body>)/i, summary + '\n$1');
    }
  }

  return html;
}

function escapeHtml(text) {
  return String(text).replace(/[&<>"']/g, function (char) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char];
  });
}

function main() {
  const locs = readSitemap();
  const results = {};
  let modified = 0;
  locs.forEach(url => {
    try {
      const urlObj = new URL(url);
      const pathname = urlObj.pathname.replace(/^\/+/, '');
      const filePath = pathname === '' ? 'index.html' : path.join(pathname, 'index.html');
      const absPath = path.join(SITE_ROOT, filePath);
      if (!fs.existsSync(absPath)) return;
      const title = titleFromPath(url);
      const category = categoryFromPath(url);
      const description = metaFor(title, category);
      const faqs = faqsFor(title, category);
      const html = fs.readFileSync(absPath, 'utf8');
      const backupPath = absPath + '.bak-seo';
      if (!fs.existsSync(backupPath)) fs.writeFileSync(backupPath, html, 'utf8');
      const updated = injectIntoHtml(html, { title, description, faqs });
      fs.writeFileSync(absPath, updated, 'utf8');
      results['/' + (pathname || '')] = { title, description, faqs };
      modified += 1;
      console.log(`Updated: ${filePath}`);
    } catch (err) {
      console.error('Error processing', url, err.message);
    }
  });
  fs.writeFileSync(path.join(SITE_ROOT, 'seo-content.json'), JSON.stringify(results, null, 2), 'utf8');
  console.log(`Done. Modified ${modified} files. seo-content.json written.`);
}

if (require.main === module) main();

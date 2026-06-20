(function () {
  "use strict";

  var ACRONYMS = {
    apr: "APR",
    bac: "BAC",
    bmi: "BMI",
    bmr: "BMR",
    bsa: "BSA",
    btu: "BTU",
    cpm: "CPM",
    ctr: "CTR",
    dti: "DTI",
    egfr: "eGFR",
    fha: "FHA",
    gcf: "GCF",
    gcd: "GCD",
    gdp: "GDP",
    gfr: "GFR",
    gpa: "GPA",
    heloc: "HELOC",
    hp: "HP",
    ira: "IRA",
    irr: "IRR",
    lcm: "LCM",
    mpg: "MPG",
    pmi: "PMI",
    pv: "PV",
    rmd: "RMD",
    roi: "ROI",
    sip: "SIP",
    tdee: "TDEE",
    tvm: "TVM",
    url: "URL",
    va: "VA",
    vat: "VAT",
    youtube: "YouTube",
    tiktok: "TikTok",
    instagram: "Instagram"
  };

  var ROUTE_CATEGORY_RULES = [
    ["youtube", ["youtube", "subscriber", "video-production"]],
    ["creator", ["tiktok", "instagram", "influencer", "twitter", "pinterest", "bio-link", "social-media"]],
    ["health", ["bmi", "bmr", "body-fat", "calorie", "tdee", "ideal-weight", "healthy-weight", "pregnancy", "period", "ovulation", "due-date", "pace", "heart-rate", "blood", "bac", "macro", "water-intake", "fiber", "vitamin", "sugar", "sodium", "caffeine", "sleep", "keto", "fasting"]],
    ["financial", ["mortgage", "loan", "tax", "salary", "paycheck", "budget", "investment", "retirement", "interest", "apr", "credit", "debt", "savings", "inflation", "currency", "roi", "irr", "rent", "payment", "finance", "commission", "discount", "margin", "vat", "cash-back", "affordability"]],
    ["commerce", ["freelance", "fiverr", "upwork", "dropshipping", "shopify", "break-even", "product-profit", "cost-per-product", "side-hustle", "passive-income", "ad-revenue", "digital-product"]],
    ["math", ["gpa", "percentage", "fraction", "scientific", "triangle", "circle", "area", "volume", "surface", "pythagorean", "slope", "distance", "standard-deviation", "mean", "median", "mode", "probability", "z-score", "matrix", "quadratic", "prime", "factor", "lcm", "gcf", "log", "exponent", "ratio", "proportion", "permutation", "combination"]],
    ["science", ["density", "mass", "weight", "speed", "molarity", "molecular", "oxidation", "chemical", "chemistry", "gdp"]],
    ["construction", ["concrete", "square-footage", "stair", "roofing", "tile", "mulch", "gravel", "wallpaper", "flooring", "fence", "paint", "deck", "drywall", "brick", "sand", "cement", "insulation", "lumber", "foundation", "pool"]],
    ["transportation", ["fuel", "gas-mileage", "mileage", "horsepower", "tire", "auto", "lease"]],
    ["utility", ["date", "time", "hours", "subnet", "password", "conversion", "base64", "url-encode", "bandwidth", "resistor", "ohms", "voltage", "electricity", "roman", "tip", "dice", "love"]]
  ];

  var HEADING_VARIANTS = {
    health: {
      guide: ["Understanding {topic} Results Safely", "{topic} Ranges, Inputs, and Health Context", "What Your {topic} Result Can and Cannot Tell You"],
      what: ["What {topic} Means in a Wellness Check", "How {topic} Fits Into Personal Health Tracking", "The Health Context Behind {topic}"],
      steps: ["Inputs and Result Checks for {topic}", "A Careful Way to Estimate {topic}", "Reading the {topic} Formula Without Overstating It"],
      examples: ["Health Scenarios That Change {topic}", "Everyday {topic} Examples and What They Show", "Comparing {topic} Results Across Realistic Cases"],
      use: ["Using This Tool Alongside Health Judgment", "How to Put {topic} Results in Context", "When a {topic} Estimate Is Useful"],
      mistakes: ["Health Interpretation Traps to Avoid", "Where {topic} Estimates Are Commonly Misread", "Important Limits Before Acting on {topic}"],
      context: ["How {topic} Connects With Broader Wellness Signals", "Where {topic} Belongs in a Bigger Health Picture", "Pairing {topic} With Other Health Measures"]
    },
    financial: {
      guide: ["Planning With {topic}: Rates, Totals, and Tradeoffs", "{topic} Numbers That Matter Before You Decide", "A Practical Money Guide for {topic}"],
      what: ["What {topic} Measures in a Financial Decision", "The Money Question Behind {topic}", "Why {topic} Changes Budget Outcomes"],
      steps: ["Inputs, Formula, and Review Checks for {topic}", "How the {topic} Numbers Are Built", "Working Through {topic} Without Spreadsheet Guesswork"],
      examples: ["Money Scenarios Where {topic} Changes the Decision", "Budget Examples That Show {topic} in Action", "Comparing {topic} Outcomes With Realistic Amounts"],
      use: ["Using This Result in a Budget or Loan Comparison", "How to Stress-Test a {topic} Decision", "Turning {topic} Results Into a Next Step"],
      mistakes: ["Financial Assumptions Worth Double-Checking", "Common Budget and Rate Errors to Avoid", "Where {topic} Decisions Often Go Wrong"],
      context: ["How {topic} Connects to Cash Flow", "Where {topic} Fits in Your Larger Money Plan", "Related Financial Signals to Compare With {topic}"]
    },
    youtube: {
      guide: ["Creator Revenue Signals Behind {topic}", "{topic} for Channels, Sponsors, and Media Plans", "Reading {topic} Like a Creator Business Metric"],
      what: ["What {topic} Means for a YouTube Channel", "The Channel Metric Behind {topic}", "Why {topic} Matters for Monetized Video Planning"],
      steps: ["Views, CPM, and Assumptions Behind {topic}", "How the {topic} Estimate Is Built", "Checking the Inputs That Drive {topic}"],
      examples: ["Channel Scenarios That Move {topic}", "Creator Revenue Examples Across Niches", "How View Milestones Change {topic}"],
      use: ["Using This Estimate for Upload and Sponsor Planning", "How Creators Can Compare {topic} Scenarios", "Turning {topic} Into a Planning Range"],
      mistakes: ["Creator Revenue Assumptions to Watch", "Why {topic} Can Be Misread Across Niches", "Common Monetization Mistakes Around {topic}"],
      context: ["How {topic} Connects With RPM, Views, and Niche", "Where {topic} Fits in a Channel Revenue Model", "Pairing {topic} With Other Creator Metrics"]
    },
    creator: {
      guide: ["Campaign Planning Signals Behind {topic}", "{topic} for Creators, Brands, and Managers", "Reading {topic} as a Social Media Metric"],
      what: ["What {topic} Means in a Creator Campaign", "The Audience Signal Behind {topic}", "Why {topic} Matters for Social Planning"],
      steps: ["Inputs and Assumptions That Shape {topic}", "How the {topic} Estimate Comes Together", "Checking the Metrics Behind {topic}"],
      examples: ["Creator Campaign Examples That Change {topic}", "Social Media Scenarios With Realistic Ranges", "Comparing {topic} Across Audience Sizes"],
      use: ["Using This Result for Pricing or Campaign Planning", "How to Compare {topic} Scenarios", "Turning {topic} Into a Practical Planning Range"],
      mistakes: ["Creator Metric Mistakes to Avoid", "Where Social Estimates Can Mislead", "Common Campaign Assumptions to Review"],
      context: ["How {topic} Connects With Reach and Engagement", "Where {topic} Fits in a Social Growth Plan", "Related Creator Metrics to Compare"]
    },
    math: {
      guide: ["Solving {topic} With Clear Inputs and Checks", "{topic} Methods, Precision, and Worked Logic", "A Math-Focused Guide to {topic}"],
      what: ["What {topic} Represents in the Problem", "The Mathematical Idea Behind {topic}", "Why {topic} Matters for the Next Step"],
      steps: ["The Calculation Path for {topic}", "Formula Checks for {topic}", "How to Work Through {topic} Carefully"],
      examples: ["Practice Situations That Use {topic}", "Worked Math Cases for {topic}", "Where {topic} Appears in Real Problems"],
      use: ["Using This Result to Check Your Work", "How to Compare {topic} Answers", "Turning {topic} Into a Reliable Final Answer"],
      mistakes: ["Precision and Unit Mistakes to Avoid", "Common Math Setup Errors", "Where {topic} Problems Often Go Off Track"],
      context: ["How {topic} Connects to Related Math Skills", "Where {topic} Fits in a Larger Problem", "Next Concepts to Compare With {topic}"]
    },
    commerce: {
      guide: ["Business Inputs That Shape {topic}", "{topic} for Pricing, Profit, and Workload Decisions", "A Practical Operations Guide to {topic}"],
      what: ["What {topic} Measures for an Online Business", "The Business Decision Behind {topic}", "Why {topic} Matters for Pricing and Profit"],
      steps: ["Costs, Rates, and Assumptions Behind {topic}", "How the {topic} Estimate Is Built", "Checking the Inputs That Drive {topic}"],
      examples: ["Business Scenarios That Change {topic}", "Pricing Examples With Realistic Inputs", "Comparing {topic} Across Workloads or Products"],
      use: ["Using This Result Before Pricing or Launching", "How to Test {topic} Scenarios", "Turning {topic} Into an Operating Decision"],
      mistakes: ["Pricing and Cost Assumptions to Review", "Common Profit Planning Errors", "Where {topic} Estimates Can Mislead"],
      context: ["How {topic} Connects With Margin and Cash Flow", "Where {topic} Fits in a Business Plan", "Related Operating Numbers to Compare"]
    },
    default: {
      guide: ["Practical Context for {topic}", "{topic} Inputs, Checks, and Use Cases", "A Focused Guide to {topic}"],
      what: ["What {topic} Means for This Task", "The Main Idea Behind {topic}", "Why {topic} Matters Before You Act"],
      steps: ["Inputs and Checks Behind {topic}", "How the {topic} Result Is Built", "A Careful Way to Work Through {topic}"],
      examples: ["Realistic Situations That Use {topic}", "Examples That Show {topic} in Practice", "Comparing {topic} Across Common Cases"],
      use: ["Using This Result in the Next Decision", "How to Put {topic} Into Context", "Turning {topic} Into a Practical Answer"],
      mistakes: ["Common Input Mistakes to Avoid", "Where {topic} Can Be Misread", "Checks to Make Before Relying on {topic}"],
      context: ["How {topic} Connects With Related Numbers", "Where {topic} Fits in the Bigger Picture", "Related Signals to Compare With {topic}"]
    }
  };

  var TABLE_ROWS = {
    health: [
      ["Activity context", "Low to high", "Movement level changes how a health estimate should be interpreted.", "Use the closest real routine, not an ideal week."],
      ["Healthy range check", "Guideline range", "Some calculators compare results with broad public-health ranges.", "Ranges are screening context, not a diagnosis.", "positive"],
      ["Medical context flag", "Personal history", "Age, medication, pregnancy, illness, or training status can change the meaning.", "Ask a qualified clinician for personal advice."],
      ["Trend over time", "Repeated checks", "A single result is less useful than a consistent pattern.", "Track changes using the same units and method."]
    ],
    youtube: [
      ["CPM tier", "Low to premium", "Ad rates vary by niche, country, season, and advertiser demand.", "Use ranges instead of one fixed promise."],
      ["Monetized views", "Eligible views", "Not every view produces ad revenue.", "RPM is often lower than headline CPM."],
      ["Niche comparison", "Topic dependent", "Finance, tech, education, and entertainment can behave differently.", "Compare channels with similar audiences."],
      ["View milestone", "1K / 10K / 100K+", "Revenue becomes easier to plan as sample size grows.", "Small channels may see volatile results."]
    ],
    creator: [
      ["Audience quality", "Reach plus fit", "Follower count alone does not prove campaign value.", "Engagement and niche match matter."],
      ["Campaign format", "Post, story, video", "Different placements produce different pricing and response patterns.", "Compare like with like."],
      ["Engagement signal", "Rate or clicks", "Shows whether the audience is likely to act.", "Watch for unusually low or inflated activity."],
      ["Brand fit", "Relevant niche", "A smaller aligned audience can outperform a larger broad one.", "Context beats vanity metrics."]
    ],
    financial: [
      ["Gross value", "Before adjustments", "Starting amount before tax, fees, discounts, or deductions.", "Do not confuse it with net."],
      ["Net value", "After adjustments", "The practical amount left after required changes.", "Often the decision number.", "positive"],
      ["Effective rate", "Blended percentage", "Shows the real average impact across the total.", "Different from a marginal rate."],
      ["Shortfall", "Negative balance", "Spending, debt, or cost exceeds the available amount.", "Needs review.", "negative"]
    ],
    commerce: [
      ["Unit economics", "Per order or job", "Shows whether one sale, gig, or product is profitable before scaling.", "Include platform and payment fees."],
      ["Break-even point", "Cost coverage", "The level where revenue covers fixed and variable costs.", "Useful before discounts or launches."],
      ["Margin buffer", "Target percentage", "Protects profit when shipping, ads, or labor changes.", "Thin margins need closer review."],
      ["Scenario test", "Best / base / worst", "Shows whether the plan still works when assumptions change.", "Avoid relying on one perfect case."]
    ],
    math: [
      ["Input precision", "Exact or rounded", "Decimals, fractions, and significant figures affect the final answer.", "Keep rounding until the final step when possible."],
      ["Unit consistency", "Same system", "Mixed units can make a correct formula produce a wrong result.", "Convert first, then solve."],
      ["Formula match", "Correct method", "The chosen formula must match the problem type.", "Check givens before calculating."],
      ["Reasonableness check", "Expected range", "A quick estimate can catch misplaced decimals or signs.", "Compare the result with common sense."]
    ],
    science: [
      ["Known variables", "Measured inputs", "Scientific calculations depend on correctly identified quantities.", "Record units with each value."],
      ["Unit system", "SI or converted", "Unit mismatches are a common source of wrong answers.", "Convert before applying the formula."],
      ["Significant figures", "Measurement precision", "The final answer should not imply more precision than the inputs support.", "Round after calculation."],
      ["Lab context", "Conditions matter", "Temperature, pressure, calibration, or sample quality may affect results.", "Use classroom or lab instructions when required."]
    ],
    construction: [
      ["Waste allowance", "5%-15%", "Materials often need extra quantity for cuts, breakage, and layout.", "Complex rooms need a larger buffer."],
      ["Measurement quality", "Field dimensions", "Small measuring errors can create large material differences.", "Measure twice before ordering."],
      ["Coverage rate", "Per bag, board, tile, or gallon", "Product labels determine how much area or volume one unit covers.", "Use the exact product spec when possible."],
      ["Project condition", "Slope, openings, subfloor", "Real jobsite details change material needs.", "Adjust for doors, windows, and irregular shapes."]
    ],
    transportation: [
      ["Fuel price", "Local rate", "Small price changes can affect trip or ownership cost.", "Update prices before long trips."],
      ["Efficiency range", "City / highway", "Driving conditions change mileage and fuel use.", "Use realistic driving patterns."],
      ["Distance basis", "Trip or annual", "The same vehicle cost looks different over one trip versus a year.", "Match the time horizon to the decision."],
      ["Maintenance context", "Vehicle condition", "Tires, load, and engine condition can shift results.", "Treat estimates as planning numbers."]
    ],
    utility: [
      ["Input format", "Expected pattern", "Utilities often require dates, times, text, or units in a specific format.", "Fix formatting before assuming the result is wrong."],
      ["Output precision", "Task dependent", "Some tools need exact output while others only need a planning estimate.", "Choose the level that matches the use case."],
      ["Compatibility", "Browser or system", "Copied results may behave differently across apps or platforms.", "Test important output before sharing."],
      ["Privacy note", "Local use", "Most utility calculations happen in the browser.", "Avoid pasting sensitive data unless necessary."]
    ],
    default: [
      ["Input quality", "Current values", "The answer is only as reliable as the numbers entered.", "Use the best available source."],
      ["Unit consistency", "Same system", "Mixed units or formats are a common cause of bad results.", "Convert first when needed."],
      ["Scenario check", "Compare cases", "Changing one assumption at a time shows what drives the result.", "Useful for planning."],
      ["Final review", "Read all outputs", "Supporting details can change how the main answer should be used.", "Context matters."]
    ]
  };

  function hash(text) {
    var value = 0;
    for (var i = 0; i < text.length; i += 1) value = (value * 31 + text.charCodeAt(i)) >>> 0;
    return value;
  }

  function titleFromPath(path) {
    return path.replace(/^\//, "").replace(/\/$/, "").split("-").map(function (part) {
      return ACRONYMS[part.toLowerCase()] || part.charAt(0).toUpperCase() + part.slice(1);
    }).join(" ");
  }

  function shortTopic(label) {
    return label.replace(/\s+(Calculator|Converter|Generator|Roller|Counter|Tool)$/i, "").trim();
  }

  function categoryFromPath(path) {
    for (var i = 0; i < ROUTE_CATEGORY_RULES.length; i += 1) {
      var category = ROUTE_CATEGORY_RULES[i][0];
      var needles = ROUTE_CATEGORY_RULES[i][1];
      if (needles.some(function (needle) { return path.indexOf(needle) !== -1; })) return category;
    }
    return "default";
  }

  function pick(category, key, path) {
    var set = HEADING_VARIANTS[category] || HEADING_VARIANTS.default;
    var values = set[key] || HEADING_VARIANTS.default[key];
    return values[hash(path + ":" + key) % values.length];
  }

  function fill(template, topic) {
    return template.replace(/\{topic\}/g, topic);
  }

  function replacementFor(text, category, topic, path) {
    var lower = text.toLowerCase();
    if (lower.indexOf("complete guide to") !== -1 && lower.indexOf("free online tool") !== -1) return fill(pick(category, "guide", path), topic);
    if (lower.indexOf("what is") === 0 || lower.indexOf(" what is ") !== -1) return fill(pick(category, "what", path), topic);
    if (lower.indexOf("how to calculate") !== -1 && lower.indexOf("step by step") !== -1) return fill(pick(category, "steps", path), topic);
    if (lower.indexOf("real ") !== -1 && (lower.indexOf("examples") !== -1 || lower.indexOf("applications") !== -1)) return fill(pick(category, "examples", path), topic);
    if (lower.indexOf("how to use this calculator") !== -1) return fill(pick(category, "use", path), topic);
    if (lower.indexOf("common ") !== -1 && lower.indexOf("mistakes") !== -1) return fill(pick(category, "mistakes", path), topic);
    if (lower.indexOf("how this calculator") !== -1 || lower.indexOf("connects to") !== -1 || lower.indexOf("fits into") !== -1) return fill(pick(category, "context", path), topic);
    return "";
  }

  function escapeHtml(text) {
    return String(text).replace(/[&<>"']/g, function (char) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char];
    });
  }

  function updateReferenceTable(category) {
    var rows = TABLE_ROWS[category] || TABLE_ROWS.default;
    var headings = Array.prototype.slice.call(document.querySelectorAll("h2"));
    var referenceHeading = headings.find(function (heading) {
      return /practical reference/i.test(heading.textContent || "");
    });
    if (!referenceHeading) return;

    var table = referenceHeading.parentElement && referenceHeading.parentElement.querySelector(".calchive-seo-table");
    if (!table) table = document.querySelector(".calchive-seo-table");
    if (!table) return;

    var tbody = table.querySelector("tbody");
    if (!tbody) return;
    if (tbody.dataset.calchiveReferenceCategory === category) return;
    tbody.innerHTML = rows.map(function (row) {
      var tone = row[4] || "";
      return "<tr><td class=\"font-semibold text-foreground\">" + escapeHtml(row[0]) + "</td><td class=\"" + escapeHtml(tone) + "\">" + escapeHtml(row[1]) + "</td><td>" + escapeHtml(row[2]) + "</td><td>" + escapeHtml(row[3]) + "</td></tr>";
    }).join("");
    tbody.dataset.calchiveReferenceCategory = category;
  }

  function moveReferenceBlock(category, path) {
    var seo = document.querySelector("section[aria-label$='reference and guide']");
    if (!seo) return;
    var heading = Array.prototype.slice.call(seo.children).find(function (node) {
      return node.tagName === "H2" && /practical reference/i.test(node.textContent || "");
    });
    if (!heading) return;
    var tableWrap = heading.nextElementSibling && heading.nextElementSibling.classList.contains("calchive-seo-table-wrap") ? heading.nextElementSibling : null;
    if (!tableWrap) return;
    var article = Array.prototype.slice.call(seo.children).find(function (node) {
      return node !== heading && node !== tableWrap && node.tagName === "SECTION" && node.className.indexOf("mb-8") !== -1;
    });
    if (!article) return;

    var variant = hash(path + ":reference-order") % 3;
    if ((category === "health" || category === "youtube" || category === "creator") && variant !== 0) {
      seo.insertBefore(heading, article.nextSibling);
      seo.insertBefore(tableWrap, heading.nextSibling);
    } else if ((category === "math" || category === "science") && variant === 2) {
      seo.insertBefore(heading, article);
      seo.insertBefore(tableWrap, article);
    }
  }

  function reorderArticleBlocks(path) {
    var articleSections = Array.prototype.slice.call(document.querySelectorAll("section.mb-8.space-y-6"));
    articleSections.forEach(function (section) {
      if (section.dataset.calchiveOrderVaried === "true") return;
      var children = Array.prototype.slice.call(section.children);
      var lead = [];
      var groups = [];
      var current = null;

      children.forEach(function (node) {
        if (/^H[23]$/.test(node.tagName)) {
          current = [node];
          groups.push(current);
        } else if (current) {
          current.push(node);
        } else {
          lead.push(node);
        }
      });

      if (groups.length < 4) return;
      var titleGroup = groups.shift();
      var pattern = hash(path + ":article-order") % 4;
      var reordered = groups.slice();
      if (pattern === 1) {
        reordered = [groups[2], groups[0], groups[1]].concat(groups.slice(3));
      } else if (pattern === 2) {
        reordered = [groups[1], groups[3] || groups[1], groups[0], groups[2]].concat(groups.slice(4));
      } else if (pattern === 3) {
        reordered = groups.slice().reverse();
      }
      reordered = reordered.filter(Boolean);
      lead.concat([titleGroup]).concat(reordered).forEach(function (groupOrNode) {
        if (Array.isArray(groupOrNode)) {
          groupOrNode.forEach(function (node) { section.appendChild(node); });
        } else {
          section.appendChild(groupOrNode);
        }
      });
      section.dataset.calchiveOrderVaried = "true";
    });
  }

  function applyContentUniqueness() {
    var path = window.location.pathname.replace(/\/+$/, "") || "/";
    if (path === "/" || /\.(txt|xml|json|ico|png|jpg|jpeg|webp|svg|css|js)$/i.test(path)) return;

    var label = titleFromPath(path);
    var topic = shortTopic(label);
    var category = categoryFromPath(path);
    var headings = Array.prototype.slice.call(document.querySelectorAll("h2, h3"));
    var changed = false;

    headings.forEach(function (heading) {
      if (heading.dataset.calchiveUniqueHeading === "true") return;
      var text = (heading.textContent || "").replace(/\s+/g, " ").trim();
      var replacement = replacementFor(text, category, topic, path);
      if (replacement) {
        heading.textContent = replacement;
        heading.dataset.calchiveUniqueHeading = "true";
        changed = true;
      }
    });

    updateReferenceTable(category);
    moveReferenceBlock(category, path);
    reorderArticleBlocks(path);
    if (changed) document.documentElement.dataset.calchiveContentUniqueness = "applied";
  }

  var routeObserver = null;
  var activePath = "";

  function schedule(delay) {
    window.clearTimeout(schedule.timer);
    schedule.timer = window.setTimeout(applyContentUniqueness, delay == null ? 80 : delay);
  }

  function stopObserver() {
    if (routeObserver) {
      routeObserver.disconnect();
      routeObserver = null;
    }
  }

  function startShortObserver() {
    stopObserver();
    var root = document.getElementById("root") || document.body;
    if (!root || typeof MutationObserver === "undefined") return;

    var deadline = Date.now() + 3500;
    routeObserver = new MutationObserver(function () {
      if (Date.now() > deadline || document.documentElement.dataset.calchiveContentUniqueness === "applied") {
        stopObserver();
        return;
      }
      schedule(120);
    });
    routeObserver.observe(root, { childList: true, subtree: true });
    window.setTimeout(stopObserver, 4000);
  }

  function onRouteChange() {
    var path = window.location.pathname;
    if (path !== activePath) {
      activePath = path;
      delete document.documentElement.dataset.calchiveContentUniqueness;
    }
    schedule(60);
    window.setTimeout(function () { schedule(0); }, 250);
    window.setTimeout(function () { schedule(0); }, 900);
    startShortObserver();
  }

  var pushState = history.pushState;
  var replaceState = history.replaceState;
  history.pushState = function () {
    var result = pushState.apply(this, arguments);
    onRouteChange();
    return result;
  };
  history.replaceState = function () {
    var result = replaceState.apply(this, arguments);
    onRouteChange();
    return result;
  };
  window.addEventListener("popstate", onRouteChange);
  window.addEventListener("DOMContentLoaded", onRouteChange);
  window.addEventListener("load", onRouteChange);
  onRouteChange();
})();

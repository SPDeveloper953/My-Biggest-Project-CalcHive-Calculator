import re, os, json

BASE = r"C:\Users\sudai\OneDrive\Documents\New OpenCode Project\CalcHive-Calculator"

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

# -------- FIX 1: FAQ data for calculators where user provided specific content --------
FAQ_DATA = {}

def set_faq(key, faqs):
    FAQ_DATA[key] = faqs

set_faq("401k-calculator-index", [
    ("How does employer 401k matching work?", "An employer match means your employer contributes a percentage of what you put in, up to a salary limit. A \"50% match up to 6%\" means for every dollar you contribute (up to 6% of your salary), your employer adds 50 cents \u2014 effectively a 50% instant return before any investment growth."),
    ("What is the 401k contribution limit for 2025?", "The IRS employee contribution limit is $23,000 for 2025. Workers aged 50 and older can add a $7,500 catch-up contribution for a total of $30,500. Employer contributions are separate and can bring the combined total to $69,000."),
    ("Should I choose a traditional or Roth 401k?", "Traditional 401k gives you a tax deduction now and you pay taxes on withdrawal. Roth 401k takes after-tax contributions but withdrawals in retirement are tax-free. Choose Roth if you expect to be in a higher tax bracket in retirement; choose traditional if you expect lower taxes later."),
    ("What happens to my 401k if I leave my job?", "You can roll it into your new employer's 401k plan, roll it into an IRA for more investment flexibility, or leave it with your former employer if the balance exceeds $5,000. Cashing out triggers income tax plus a 10% early withdrawal penalty if you are under age 59\u00bd."),
    ("At what age can I withdraw from my 401k without penalty?", "Age 59\u00bd is the standard penalty-free withdrawal age. Required Minimum Distributions must begin at age 73 under current SECURE 2.0 rules. Early withdrawals before 59\u00bd trigger a 10% penalty plus ordinary income tax on the amount withdrawn."),
])

set_faq("acceleration-calculator-index", [
    ("What is the formula for acceleration?", "Acceleration = change in velocity divided by time elapsed (a = \u0394v/\u0394t). Using Newton's second law, acceleration also equals force divided by mass (a = F/m). Both formulas give the result in metres per second squared (m/s\u00b2) in the SI unit system."),
    ("What does negative acceleration mean?", "Negative acceleration means the object is decelerating \u2014 slowing down if moving in the positive direction, or speeding up in the negative direction. A car braking from 60 mph to a stop has negative acceleration (deceleration) throughout the stop."),
    ("What is the acceleration due to gravity on Earth?", "Free-fall acceleration on Earth is approximately 9.8 m/s\u00b2 (32 ft/s\u00b2), ignoring air resistance. This means a falling object gains roughly 9.8 m/s of velocity every second it falls."),
    ("What is the difference between acceleration and velocity?", "Velocity describes speed in a specific direction (e.g., 60 mph north). Acceleration is the rate at which velocity changes \u2014 you can accelerate by speeding up, slowing down, or changing direction even at constant speed."),
    ("How do I calculate acceleration from a distance-time graph?", "First derive a velocity-time graph from the distance-time graph (velocity = slope of distance vs time). Then the slope of the velocity-time graph gives acceleration. Constant acceleration shows as a straight line on a velocity-time graph."),
])

set_faq("ad-revenue-calculator-index", [
    ("What is CPM in advertising?", "CPM stands for Cost Per Mille (cost per thousand impressions). A $5 CPM means advertisers pay $5 for every 1,000 times their ad is shown. It is the standard unit for measuring display advertising costs."),
    ("What is the difference between CPM and RPM?", "CPM is what advertisers pay per 1,000 ad impressions. RPM (Revenue Per Mille) is what publishers actually earn per 1,000 pageviews after the ad network takes its commission. Your RPM is always lower than the advertiser's CPM."),
    ("What is a good RPM for a website or blog?", "RPM varies dramatically by niche. Finance and insurance content earns $10\u201340 RPM. Health and wellness earns $5\u201315. General entertainment and lifestyle earn $1\u20135. US, UK, and Canadian traffic earns significantly more than traffic from other regions."),
    ("How do I increase my ad revenue RPM?", "Focus on high-CPM niches, improve traffic quality by targeting high-income English-speaking audiences, use header bidding to increase competition for your ad slots, optimise ad placement for viewability, and apply to premium ad networks once you reach sufficient traffic."),
    ("Does more traffic always mean more ad revenue?", "More traffic helps, but niche and audience quality matter more than raw numbers. A finance blog with 50,000 monthly visitors can earn more than a general entertainment site with 500,000 visitors if the finance CPM is 10\u00d7 higher."),
])

set_faq("age-calculator-index", [
    ("How is exact age calculated in years, months, and days?", "Age is calculated by counting complete years since the birth date, then counting remaining complete months, then remaining days. The calculation adjusts for months with different lengths and correctly handles leap years throughout."),
    ("What if I was born on February 29 (leap day)?", "Leap day birthdays are typically counted on February 28 in non-leap years for most legal and administrative purposes. Some jurisdictions use March 1 instead. This calculator shows the result using February 28 for non-leap years."),
    ("How many days old am I?", "Enter your birth date and today's date to see your total age in days. A 30-year-old is approximately 10,957 to 10,958 days old depending on how many February 29ths fell within their lifetime."),
    ("Can I calculate the time between two past dates?", "Yes. Enter any two dates \u2014 not necessarily involving a birth date \u2014 and the calculator returns the exact elapsed time in years, months, weeks, and days. This works for anniversaries, project durations, historical events, or contract terms."),
    ("What is the legal age of adulthood in the US?", "The legal age of majority in the US is 18 for most rights including voting and contracts. The legal drinking age is 21. Some rights and responsibilities have different age thresholds. This calculator computes elapsed time numerically; legal age definitions vary by jurisdiction and right."),
])

set_faq("alcohol-calorie-calculator-index", [
    ("How many calories are in a standard beer?", "A standard 12 oz regular beer at approximately 5% ABV contains roughly 150 calories. Light beers contain 90\u2013110 calories. Craft IPAs and stouts can reach 200\u2013300 calories per can due to higher ABV and residual sugars."),
    ("Which type of alcohol has the fewest calories?", "Distilled spirits (vodka, gin, whiskey, rum) contain the fewest calories per serving at approximately 97 calories per 1.5 oz shot. Wine averages 125 calories per 5 oz glass. Regular beer is typically 150 calories. Cocktails with mixers are usually highest."),
    ("Does alcohol affect fat loss?", "Yes. Alcohol temporarily pauses fat metabolism because the liver prioritises processing alcohol over other fuel sources. Alcohol also provides 7 calories per gram with zero nutritional value, and cocktail mixers add significant additional calories on top."),
    ("Do mixers add a lot of calories to drinks?", "Significantly yes. A 12 oz can of regular soda adds approximately 150 calories. Juice, tonic water, and cream-based mixers can double or triple the calorie count of a drink. A vodka soda (spirit + soda water) is one of the lowest-calorie cocktail options."),
    ("How are alcohol calories different from food calories?", "Alcohol provides 7 kilocalories per gram \u2014 more than carbohydrates or protein (4 kcal/g each) but less than fat (9 kcal/g). Unlike food calories, alcohol calories carry no protein, fat, fibre, vitamins, or minerals. They are nutritionally empty and are metabolised differently than food."),
])

set_faq("amortization-calculator-index", [
    ("Why does so much of my early mortgage payment go to interest?", "Interest is calculated on the outstanding loan balance. Because your balance is highest at the start, the interest portion of each payment is also highest. As you pay down principal over time, the interest portion shrinks and the principal portion grows \u2014 this shift is exactly what an amortization schedule shows."),
    ("What happens if I make extra principal payments?", "Extra principal payments reduce your outstanding balance faster, which lowers the interest accruing each month. This shortens your total loan term and reduces the total interest paid over the life of the loan. Even one extra payment per year can save thousands in interest on a 30-year mortgage."),
    ("How do I read an amortization schedule?", "Each row in an amortization schedule represents one payment period. It shows the payment number, total payment amount, how much goes to interest, how much reduces principal, and the remaining balance after that payment. The interest and principal columns visually shift over time."),
    ("What is a fully amortized loan?", "A fully amortized loan is structured so that equal regular payments pay off the entire balance plus all interest by the end of the term, leaving exactly zero balance on the final payment date. Most fixed-rate mortgages and auto loans are fully amortized."),
    ("How does interest rate affect the amortization schedule?", "A higher interest rate increases the interest portion of every payment, slowing the rate at which principal is paid down. On a $300,000 loan, the difference between a 5% and 7% rate means paying approximately $130,000 more in total interest over 30 years."),
])

set_faq("annuity-calculator-index", [
    ("What is the difference between an ordinary annuity and an annuity due?", "In an ordinary annuity, payments occur at the end of each period. In an annuity due, payments occur at the beginning of each period. Annuities due are worth slightly more because each payment has one extra period to earn interest before the valuation date."),
    ("What is the present value formula for an annuity?", "PV = PMT \u00d7 [1 - (1 + r)^-n] / r, where PMT is the payment amount per period, r is the interest rate per period, and n is the total number of periods. This formula finds what a series of future payments is worth in today's money."),
    ("Where are annuity calculations used in real life?", "Annuity calculations are used in mortgage payments, pension income planning, lottery structured payouts, insurance settlements, car loan payments, and retirement income planning. Any regular series of equal payments follows the annuity formula."),
    ("What is a good annuity payout rate in 2025?", "Immediate annuity payout rates in 2025 range from approximately 6\u20138% annually for retirees in their late 60s, meaning a $100,000 premium generates $6,000\u2013$8,000 per year in guaranteed income for life. Rates are influenced by the 10-year Treasury yield."),
    ("How do I calculate how long my savings will last if I withdraw a fixed amount monthly?", "This is the annuity period calculation. Enter your current balance as present value, your monthly withdrawal as the payment, and your expected return rate. The calculator solves for n \u2014 the number of months before the balance reaches zero."),
])

set_faq("annuity-payout-calculator-index", [
    ("What is the 4% withdrawal rule for retirement?", "The 4% rule states that withdrawing 4% of your portfolio in the first year of retirement, then adjusting for inflation annually, has historically sustained a 30-year retirement in over 95% of historical market scenarios. It derives from the Trinity Study published in 1998."),
    ("How long will $500,000 last in retirement?", "At a 4% withdrawal rate ($20,000/year) with a 5% average return, a $500,000 portfolio can last indefinitely in most scenarios. At $40,000/year (8% withdrawal rate) with the same return, the portfolio depletes in approximately 17\u201318 years."),
    ("Does inflation affect how long my money lasts?", "Significantly yes. If you withdraw a fixed dollar amount and inflation runs at 3% annually, your purchasing power halves roughly every 24 years. Inflation-adjusting withdrawals upward each year protects purchasing power but accelerates portfolio depletion."),
    ("What is sequence-of-returns risk in retirement?", "Sequence-of-returns risk is the danger of experiencing poor investment returns in the early years of retirement when the portfolio is largest. A 30% market drop in year 2 of retirement is far more damaging than the same drop in year 20, because withdrawals at a low point permanently reduce the base available for recovery."),
    ("Should I buy an annuity or draw from my portfolio?", "A fixed annuity provides guaranteed lifetime income regardless of market performance \u2014 useful as a floor income alongside Social Security. Portfolio drawdown provides flexibility and potential upside. Many financial planners recommend covering essential expenses with guaranteed income and drawing from investments for discretionary spending."),
])

set_faq("anorexic-bmi-calculator-index", [
    ("What BMI is considered dangerously underweight?", "A BMI below 17.5 is used clinically as one diagnostic criterion for anorexia nervosa. A BMI below 15 is considered severely underweight and associated with serious medical complications. These are clinical reference points \u2014 a doctor evaluates overall health, not just a single number."),
    ("What are the health risks of a very low BMI?", "A very low BMI is associated with loss of muscle mass, bone density reduction, cardiac arrhythmias, hormonal disruption, immune system impairment, and organ damage. The heart is a muscle \u2014 severe underweight affects cardiac function directly."),
    ("Is this calculator a diagnostic tool for eating disorders?", "No. This calculator provides reference information only. Eating disorder diagnosis requires clinical assessment by a qualified medical or mental health professional. BMI is one data point among many \u2014 it does not diagnose any condition on its own."),
    ("Where can someone get help for an eating disorder?", "In the US, contact the National Eating Disorders Association (NEDA) helpline at 1-800-931-2237, or text \"NEDA\" to 741741. In the UK, contact Beat Eating Disorders at 0808 801 0677. These services provide confidential support and can connect people with local treatment resources."),
    ("Can BMI accurately measure underweight status?", "BMI provides a useful population-level screening estimate but does not measure body composition directly. Two people with identical BMIs can have very different muscle-to-fat ratios and health statuses. Medical assessment includes blood work, bone density scans, and physical examination beyond BMI alone."),
])

set_faq("apr-calculator-index", [
    ("What is the difference between interest rate and APR?", "The interest rate is the cost of borrowing the principal balance expressed as a percentage. APR (Annual Percentage Rate) includes the interest rate plus fees such as origination charges, points, and mortgage insurance \u2014 all expressed as a single annual rate. APR is always equal to or higher than the stated interest rate."),
    ("Why is APR more useful than the interest rate when comparing loans?", "APR enables apples-to-apples comparison between loan offers with different fee structures. A loan with a low interest rate and high origination fees can have a higher APR than a loan with a slightly higher rate but no fees. US law (Truth in Lending Act) requires lenders to disclose APR for this reason."),
    ("Does APR affect my monthly payment?", "Your monthly payment is calculated from the nominal interest rate, not APR. APR is a comparison and total-cost metric, not a direct payment input. Two loans can have the same monthly payment but different APRs if their fee structures differ."),
    ("What is a good APR for a mortgage in 2025?", "As of 2025, 30-year fixed mortgage APRs range from approximately 6.5% to 7.5% for borrowers with good credit. Rates vary daily with the bond market. An excellent credit score (760+) and 20% down payment typically secure the lowest available APR."),
    ("What is the difference between fixed APR and variable APR?", "A fixed APR stays constant for the life of the loan. A variable APR is tied to a market index (such as the Prime Rate or SOFR) and can change periodically \u2014 usually annually or monthly. Variable APRs typically start lower than fixed but carry rate-change risk over time."),
])

set_faq("area-calculator-index", [
    ("What is the formula for the area of a circle?", "Area = \u03c0 \u00d7 r\u00b2, where r is the radius and \u03c0 \u2248 3.14159. For a circle with a 7-metre radius: Area = 3.14159 \u00d7 49 = 153.94 square metres. If given the diameter, divide by 2 to find the radius first."),
    ("How do I find the area of an irregular shape?", "Divide the irregular shape into simple sub-shapes (rectangles, triangles, semicircles). Calculate each sub-shape's area separately using the appropriate formula, then add all sub-areas together. Subtract any openings or cutouts from the total."),
    ("How many square feet are in an acre?", "One acre contains exactly 43,560 square feet, or approximately 4,047 square metres. An acre is roughly the size of a standard American football field excluding the end zones."),
    ("How do I convert square metres to square feet?", "Multiply square metres by 10.764 to get square feet. For example, 25 square metres equals 25 \u00d7 10.764 = 269.1 square feet. To convert the other way, multiply square feet by 0.0929."),
    ("What is the formula for the area of a triangle?", "Area = \u00bd \u00d7 base \u00d7 height, where the height is the perpendicular distance from the base to the opposite vertex. If only the three side lengths are known, use Heron's formula: Area = \u221a[s(s-a)(s-b)(s-c)] where s = (a+b+c)/2."),
])

# -------- FIX 3: Reference table data for calculators the user specified --------
REF_DATA = {}

def set_ref(key, headers, rows):
    REF_DATA[key] = (headers, rows)

set_ref("401k-calculator-index", ["Key Metric", "Value / Range", "Notes"], [
    ["2025 Employee Contribution Limit", "$23,000 ($30,500 if age 50+)", "IRS annual limit"],
    ["Typical employer match", "3\u20136% of salary", "50\u2013100% match rate"],
    ["Recommended contribution rate", "At minimum: enough to capture full match", "Increase to 15% when possible"],
    ["Average 401k balance at age 55\u201364", "~$134,000 median (Vanguard 2024)", "Most workers are behind benchmarks"],
    ["Penalty-free withdrawal age", "59\u00bd", "10% penalty before this age"],
])

set_ref("acceleration-calculator-index", ["Quantity", "Value", "Context"], [
    ["Earth gravity (g)", "9.8 m/s\u00b2 (32.2 ft/s\u00b2)", "Free fall acceleration"],
    ["Typical car 0\u201360 mph", "5\u20138 seconds", "~3.4\u20135.4 m/s\u00b2 average"],
    ["Sports car 0\u201360 mph", "3\u20134 seconds", "~6.7\u20139.0 m/s\u00b2 average"],
    ["Space Shuttle launch", "~29 m/s\u00b2", "~3g acceleration"],
    ["Human fainting threshold", "~5g (49 m/s\u00b2)", "Sustained lateral acceleration"],
])

set_ref("calorie-calculator-index", ["Goal", "Daily Calorie Adjustment", "Expected Result"], [
    ["Lose 2 lbs/week", "\u22121000 calories/day", "Fast loss, hard to sustain"],
    ["Lose 1 lb/week", "\u2212500 calories/day", "Recommended rate"],
    ["Maintain weight", "0 adjustment", "Eat at TDEE"],
    ["Slow muscle gain", "+250 calories/day", "Lean bulk"],
    ["Muscle gain", "+500 calories/day", "Standard bulk"],
])

set_ref("bmi-calculator-index", ["BMI Range", "Classification", "Health Risk"], [
    ["Below 18.5", "Underweight", "Moderate"],
    ["18.5\u201324.9", "Healthy Weight", "Low"],
    ["25.0\u201329.9", "Overweight", "Increased"],
    ["30.0\u201334.9", "Obese Class I", "High"],
    ["35.0\u201339.9", "Obese Class II", "Very High"],
    ["40.0 and above", "Obese Class III", "Extremely High"],
])

set_ref("bmr-calculator-index", ["Activity Level", "Multiplier", "Example"], [
    ["Sedentary (desk job, no exercise)", "1.2", "Office worker, no gym"],
    ["Lightly active (1\u20133 days/week)", "1.375", "Light walking or gym"],
    ["Moderately active (3\u20135 days/week)", "1.55", "Regular gym sessions"],
    ["Very active (6\u20137 days/week)", "1.725", "Daily training"],
    ["Extremely active (physical job + training)", "1.9", "Construction + daily gym"],
])

# -------- Fix 2: Exhibit D header patterns to replace --------
HEADER_FIXES = [
    (r'How to Calculate Your .*? for Free', 'How the {name} Formula Works'),
    (r'Free .*? for Everyone', '{name}: Key Numbers and Benchmarks'),
    (r'Complete Guide to .*? Calculator', 'Understanding Your {name} Result'),
    (r'What Is .*? and Why Your .*? Depends on It', 'What {name} Actually Measures'),
    (r'Common .*? Mistakes This Calculator Helps You Avoid', 'What Affects Your {name} Result'),
    (r'How This Calculator Fits Into Your', 'Using {name} for Better Decisions'),
    (r'Real .*? Examples With Actual Numbers', '{name} in Practice: Real Scenarios'),
    (r'Why .*? Matters Before You Act', 'Key Factors in {name} Calculations'),
]

# -------- Fix 4: Specific section heading patterns --------
SECTION_PATTERNS = [
    (r'Why (\w+(?: \w+)*) Matters Before You Act', r'Key Factors in \1 Calculations'),
    (r'How the (\w+(?: \w+)*) Result Is Built', r'How the \1 Calculation Works'),
    (r'Realistic Situations That Use (\w+(?: \w+)*)', r'\1 in Practice: Real Scenarios'),
    (r'Where (\w+(?: \w+)*) Can Be Misread', r'Common Misunderstandings of \1'),
]

def get_calc_name(path):
    name = path.split("/")[0]
    return name.replace("-", " ").title()

def build_faq_html(faqs):
    lines = []
    for q, a in faqs:
        lines.append(f'              <dt>{q}</dt>')
        lines.append(f'              <dd>{a}</dd>')
    return "\n".join(lines)

def build_ref_table_html(headers, rows):
    ths = "".join(f'<th style="padding:8px;border:1px solid #e2e8f0">{h}</th>' for h in headers)
    trs = ""
    for row in rows:
        tds = "".join(f'<td style="padding:8px;border:1px solid #e2e8f0">{c}</td>' for c in row)
        trs += f"                <tr>{tds}</tr>\n"
    return f'''<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:15px">
              <thead><tr style="background:#f1f5f9;text-align:left">{ths}</tr></thead>
              <tbody>
{trs}              </tbody>
            </table>'''

def main():
    fix1_count = 0
    fix2_count = 0
    fix3_count = 0
    fix4_count = 0

    for fname in FILES:
        fp = os.path.join(BASE, fname)
        if not os.path.exists(fp):
            print(f"MISSING: {fname}")
            continue

        key = fname.replace("/", "-").replace(".html", "")
        calc_name = fname.split("/")[0]

        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()

        original = content

        # Fix 1: Replace FAQ <dl> block
        if key in FAQ_DATA:
            new_faq_html = build_faq_html(FAQ_DATA[key])
            faq_pattern = r'<h2>.*?Frequently Asked Questions</h2>\s*<dl>.*?</dl>'
            replacement = f'<h2>{calc_name.replace("-", " ").title()} - Frequently Asked Questions</h2>\n            <dl>\n{new_faq_html}\n            </dl>'
            content, n = re.subn(faq_pattern, replacement, content, count=1, flags=re.DOTALL)
            if n > 0:
                fix1_count += 1
            else:
                print(f"  Fix1 WARN: FAQ pattern not found in {fname}")

        # Fix 2: Replace Exhibit D headers
        name_parts = calc_name.replace("-", " ").title()
        for pattern, template in HEADER_FIXES:
            replacement_text = template.replace("{name}", name_parts)
            content, n = re.subn(pattern, replacement_text, content)
            if n > 0:
                fix2_count += n

        # Fix 3: Add reference table if data exists (insert before </section>)
        if key in REF_DATA:
            ref_headers, ref_rows = REF_DATA[key]
            ref_table_name = f"{name_parts} Reference Table"
            ref_html = f'            <h2>{ref_table_name}</h2>\n            {build_ref_table_html(ref_headers, ref_rows)}\n          '
            content = content.replace("          </section>", ref_html + "</section>", 1)
            fix3_count += 1

        # Fix 4: Fix section headings
        for pattern, replacement in SECTION_PATTERNS:
            content, n = re.subn(pattern, replacement, content)
            if n > 0:
                fix4_count += n

        if content != original:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"OK: {fname}")
        else:
            print(f"SKIP (no changes): {fname}")

    print(f"\n--- Summary ---")
    print(f"Fix 1 (FAQ upgrade): {fix1_count}/48 files")
    print(f"Fix 2 (Exhibit D headers replaced): {fix2_count} replacements")
    print(f"Fix 3 (Reference tables added): {fix3_count}/48 files")
    print(f"Fix 4 (Section headings fixed): {fix4_count} replacements")

if __name__ == "__main__":
    main()

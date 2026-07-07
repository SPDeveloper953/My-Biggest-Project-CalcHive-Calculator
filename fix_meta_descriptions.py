import os, re

BASE = r"C:\Users\sudai\OneDrive\Documents\New OpenCode Project\CalcHive-Calculator"

META = {
    "401k-calculator": "401(k) retirement balance calculator projects growth using employer match, IRS 2025 limits, and compound interest \u2014 broken down by contribution year and retirement age.",
    "amortization-calculator": "Loan amortization calculator generates a full payment schedule showing exactly how much of each payment goes to interest versus principal over the loan term.",
    "annuity-calculator": "Annuity calculator computes present value and future value using the PV = PMT \u00d7 [1-(1+r)^-n]/r formula \u2014 covering ordinary annuities and annuities due.",
    "annuity-payout-calculator": "Retirement payout calculator shows how long savings last at any withdrawal rate, based on the 4% rule and adjustable return and inflation assumptions.",
    "apr-calculator": "APR calculator reveals the true loan cost by adding origination fees and points to the stated interest rate \u2014 required for disclosure under the US Truth in Lending Act.",
    "auto-lease-calculator": "Car lease calculator computes monthly payment from residual value, money factor, and cap cost \u2014 and compares total lease cost against buying over the same period.",
    "auto-loan-calculator": "Auto loan calculator shows monthly payment and total interest for 48, 60, and 72-month terms \u2014 so you can see the real cost difference before choosing a loan term.",
    "average-return-calculator": "CAGR calculator computes compound annual growth rate using the formula (End/Start)^(1/n)-1 \u2014 the correct metric for comparing investments held over different periods.",
    "bond-calculator": "Bond price calculator shows how rising interest rates reduce bond market value \u2014 with yield to maturity, duration, and coupon rate calculations for any fixed-income security.",
    "break-even-calculator": "Break-even calculator finds the unit volume and revenue needed to cover fixed and variable costs, using the formula: Fixed Costs \u00f7 (Price \u2212 Variable Cost per unit).",
    "budget-calculator": "Budget calculator applies the 50/30/20 rule \u2014 50% needs, 30% wants, 20% savings \u2014 to your after-tax income and shows where your money is actually going each month.",
    "business-loan-calculator": "Business loan calculator covers SBA 7(a) loans, term loans, and lines of credit \u2014 showing monthly payment, total interest, and total repayment for any loan structure.",
    "canadian-mortgage-calculator": "Canadian mortgage calculator uses semi-annual compounding (not monthly, as in the US) and includes CMHC insurance premiums and the stress test qualifying rate.",
    "cash-back-vs-low-interest-calculator": "Cash-back vs low APR calculator finds which car deal saves more money \u2014 comparing total loan cost under each option at your chosen term and loan amount.",
    "cd-calculator": "CD calculator shows interest earned at maturity for any term and APY \u2014 with early withdrawal penalty modelling and a CD ladder comparison across multiple terms.",
    "compound-interest-calculator": "Compound interest calculator shows how frequency of compounding changes final balance \u2014 comparing daily, monthly, and annual compounding on the same principal and rate.",
    "debt-payoff-calculator": "Debt payoff calculator compares avalanche (highest rate first) and snowball (smallest balance first) strategies \u2014 showing your debt-free date and total interest saved for each.",
    "down-payment-calculator": "Down payment calculator shows how different deposit sizes affect monthly payment, PMI cost, and total interest \u2014 including the break-even point for a larger down payment.",
    "emergency-fund-calculator": "Emergency fund calculator sets your 3-month and 6-month target based on actual expenses \u2014 and shows how long your current savings would cover essential costs.",
    "fha-loan-calculator": "FHA loan calculator computes full monthly payment including upfront MIP (1.75% of loan) and annual MIP \u2014 the extra costs that apply when putting less than 20% down.",
    "freelancer-profit-calculator": "Freelancer profit calculator finds your real hourly rate after taxes, unpaid hours, and business expenses \u2014 and shows the gross rate needed to hit your net income target.",
    "fuel-cost-calculator": "Fuel cost calculator gives total trip cost from distance, fuel economy, and current price per gallon \u2014 with a side-by-side comparison for two vehicles on the same route.",
    "gas-mileage-calculator": "Fuel economy calculator gives real-world MPG from odometer readings and gallons used at fill-up \u2014 track efficiency across multiple tanks to spot engine or driving changes.",
    "gross-profit-calculator": "Gross profit calculator shows gross profit, gross margin %, and markup % from revenue and cost \u2014 and explains why margin and markup give different numbers for the same sale.",
    "home-affordability-calculator": "Home affordability calculator applies the 28/36 debt-to-income rule to your income and debts \u2014 giving the maximum home price a conventional lender is likely to approve.",
    "inflation-calculator": "Inflation calculator converts any past dollar amount to today's value using historical CPI data \u2014 useful for comparing salaries, prices, and savings across decades.",
    "interest-rate-calculator": "Interest rate calculator solves for the missing loan variable \u2014 find the rate from payment and term, or find the term from rate and payment, using the standard amortization formula.",
    "investment-calculator": "Investment growth calculator projects a portfolio's future value with regular contributions \u2014 and shows the cost of waiting 5 years to start at any assumed return rate.",
    "loan-calculator": "Loan calculator gives monthly payment, total interest, and full repayment schedule for any combination of principal, interest rate, and term length.",
    "mortgage-calculator": "Mortgage calculator gives full monthly payment including principal, interest, property tax, and insurance \u2014 and shows the total 30-year cost at different interest rates.",
    "net-worth-calculator": "Net worth calculator subtracts total liabilities from total assets and benchmarks the result against US median net worth by age group from Federal Reserve data.",
    "paycheck-calculator": "Paycheck calculator estimates take-home pay after federal tax, state tax, Social Security (6.2%), and Medicare (1.45%) withholding \u2014 for all 50 states and pay frequencies.",
    "personal-loan-calculator": "Personal loan calculator shows total interest cost and monthly payment for 2-year vs 5-year terms \u2014 so you can see the real price of borrowing for a longer period.",
    "profit-margin-calculator": "Profit margin calculator gives gross margin, net margin, and operating margin from revenue and cost figures \u2014 and explains which margin matters most for your business type.",
    "refinance-calculator": "Refinance calculator finds your break-even month \u2014 the point where monthly savings exceed total closing costs \u2014 and total interest saved over the remaining loan term.",
    "rent-vs-buy-calculator": "Rent vs buy calculator compares 5, 10, and 20-year total cost of each option including opportunity cost of the down payment, home appreciation, and mortgage tax deduction.",
    "retirement-calculator": "Retirement calculator projects your balance at any retirement age from current savings and monthly contributions \u2014 and compares the result against your estimated income need.",
    "roi-calculator": "ROI calculator gives return on investment as a percentage and as an annualised rate \u2014 so investments held over different time periods can be compared on equal footing.",
    "savings-calculator": "Savings calculator projects your balance with regular monthly deposits and compound interest \u2014 and shows the impact of increasing your contribution by $50 or $100 per month.",
    "savings-goal-calculator": "Savings goal calculator works backwards from a target amount and deadline \u2014 giving the exact monthly deposit needed to reach it at your expected annual return rate.",
    "simple-interest-calculator": "Simple interest calculator uses the I = PRT formula and compares simple vs compound interest on the same principal, rate, and term to show the compounding difference.",
    "social-security-calculator": "Social Security benefit calculator estimates your monthly payment based on earnings history and claiming age \u2014 and shows the cost of claiming at 62 vs waiting until 70.",
    "stock-calculator": "Stock profit calculator gives net gain or loss after commissions, calculates break-even price, and shows the percentage return needed to recover from any loss.",
    "tip-calculator": "Tip and bill splitter gives the tip amount at any percentage and divides the full total evenly \u2014 or by custom amounts \u2014 across any number of diners.",
    "vat-calculator": "VAT calculator adds or removes tax at any rate \u2014 showing net price, VAT amount, and gross price separately. Covers UK, EU, and international VAT and GST rates.",

    # Health
    "alcohol-calorie-calculator": "Alcohol calorie calculator gives calories per drink based on ABV and serving size \u2014 and shows how beer, wine, spirits, and cocktails compare on a per-unit basis.",
    "anorexic-bmi-calculator": "Underweight BMI reference tool shows clinical weight classification thresholds including the BMI below 17.5 used as a diagnostic criterion for anorexia nervosa.",
    "army-body-fat-calculator": "US Army body fat calculator uses the official tape test method \u2014 neck, waist, and hip measurements \u2014 and checks your result against 2025 Army standards by age and gender.",
    "bac-calculator": "Blood alcohol calculator estimates BAC using the Widmark formula from drinks consumed, body weight, and hours elapsed \u2014 and shows when the result falls below 0.08%.",
    "bmi-calculator": "Body Mass Index calculator gives your BMI value and classifies it using WHO standards \u2014 underweight, normal, overweight, or obese Class I/II/III \u2014 for adults and children.",
    "bmr-calculator": "Basal metabolic rate calculator uses the Mifflin-St Jeor equation \u2014 the current clinical gold standard \u2014 and applies activity multipliers to give your total daily energy expenditure.",
    "body-fat-calculator": "Body fat percentage calculator uses the US Navy tape method from neck, waist, and hip measurements \u2014 and compares your result against athlete, fitness, acceptable, and obese ranges.",
    "body-surface-area-calculator": "Body surface area calculator uses the Mosteller formula \u2014 BSA = \u221a(height cm \u00d7 weight kg \u00f7 3600) \u2014 applied clinically for chemotherapy dosing and burn assessment.",
    "body-type-calculator": "Somatotype calculator identifies your body type \u2014 ectomorph, mesomorph, or endomorph \u2014 and gives training and nutrition guidance tailored to each classification.",
    "caffeine-calculator": "Caffeine calculator tracks active caffeine in your system over time using a 5.7-hour half-life \u2014 and shows when your level drops below the FDA's 400mg daily safety threshold.",
    "calorie-calculator": "Calorie calculator gives your total daily energy expenditure using the Mifflin-St Jeor equation \u2014 with calorie targets for weight loss, maintenance, and muscle gain based on activity level.",
    "calorie-deficit-calculator": "Calorie deficit calculator shows your daily deficit target and projects your goal date \u2014 based on the 3,500-calorie-per-pound rule and your safe weekly loss rate.",
    "calories-burned-calculator": "Exercise calorie calculator uses MET values to estimate calories burned \u2014 formula: MET \u00d7 weight (kg) \u00d7 time (hours) \u2014 covering 50+ activities at your body weight.",
    "carbohydrate-calculator": "Carbohydrate intake calculator gives your daily carb target in grams from your calorie goal \u2014 based on the USDA recommendation of 45\u201365% of total calories from carbohydrates.",
    "due-date-calculator": "Pregnancy due date calculator gives your estimated delivery date from last menstrual period or conception date, with week-by-week milestones and trimester boundaries.",
    "fitness-calculator": "Fitness calculator estimates VO2 max, target heart rate training zones, and calories burned during cardio \u2014 using the age-adjusted Karvonen formula for heart rate ranges.",
    "ideal-weight-calculator": "Ideal weight calculator gives results from four medical formulas \u2014 Devine, Robinson, Miller, and Hamwi \u2014 and shows how height, sex, and frame size affect each estimate.",
    "lean-body-mass-calculator": "Lean body mass calculator gives fat-free body weight using the Boer or James formula \u2014 used for accurate protein targets, medication dosing, and body composition tracking.",
    "macro-calculator": "Macro calculator gives daily protein, carbohydrate, and fat targets in grams \u2014 adjustable for cutting, bulking, or maintaining at your specific calorie goal.",
    "ovulation-calculator": "Ovulation calculator estimates your fertile window from cycle length \u2014 ovulation typically occurs 14 days before the next period \u2014 with your five highest-probability days highlighted.",
    "pregnancy-calculator": "Pregnancy calculator gives gestational age, current trimester, and estimated due date from last menstrual period or conception date \u2014 with key development milestones by week.",
    "protein-calculator": "Protein intake calculator gives your daily gram target based on activity level \u2014 from 0.8g/kg for sedentary adults to 2.2g/kg for strength athletes \u2014 adjusted for your goal.",
    "sleep-calculator": "Sleep cycle calculator gives optimal bedtimes and wake times based on 90-minute sleep cycles \u2014 so you wake between cycles rather than during deep or REM sleep.",
    "tdee-calculator": "Total daily energy expenditure calculator multiplies your BMR by an activity factor from 1.2 (sedentary) to 1.9 (extremely active) to give your maintenance calorie level.",
    "water-intake-calculator": "Daily water intake calculator gives your hydration target based on body weight and activity level \u2014 and explains why the 8-glasses rule varies significantly by individual.",

    # Math
    "area-calculator": "Area calculator gives results for rectangles, circles, triangles, and trapezoids \u2014 including Heron's formula for triangles from three side lengths, with unit conversion.",
    "big-number-calculator": "Arbitrary precision calculator handles integers beyond the 15-digit limit of standard tools \u2014 useful for factorial calculations, combinatorics, and cryptographic key sizes.",
    "binary-calculator": "Binary calculator performs addition, subtraction, multiplication, and division in base-2 \u2014 and converts between binary, decimal, octal, and hexadecimal number systems.",
    "fraction-calculator": "Fraction calculator adds, subtracts, multiplies, and divides fractions with step-by-step working \u2014 and converts between improper fractions, mixed numbers, and decimals.",
    "lcm-hcf-calculator": "LCM and HCF calculator finds the Lowest Common Multiple and Highest Common Factor of any two integers using prime factorisation \u2014 with each step shown in full.",
    "logarithm-calculator": "Logarithm calculator gives log base 10, natural log (ln), or any custom base \u2014 with the inverse antilog value and the change-of-base formula used for the result.",
    "matrix-calculator": "Matrix calculator multiplies, adds, subtracts, and finds the determinant and inverse of 2\u00d72 and 3\u00d73 matrices \u2014 with step-by-step working for each operation.",
    "percentage-calculator": "Percentage calculator solves three problems in one tool: what is X% of Y, X is what % of Y, and percentage change from X to Y \u2014 covering tips, discounts, and grades.",
    "prime-number-calculator": "Prime number calculator checks any integer for primality and finds all primes up to a limit using the Sieve of Eratosthenes \u2014 with full factorisation for composite numbers.",
    "quadratic-calculator": "Quadratic equation calculator solves ax\u00b2+bx+c=0 using the quadratic formula \u2014 gives both roots (real or complex), the discriminant value, and the parabola vertex.",
    "ratio-calculator": "Ratio calculator simplifies ratios, solves proportion problems, and scales ratios up or down \u2014 showing the GCD used for simplification and the equivalent scaled values.",
    "scientific-calculator": "Scientific calculator handles trigonometric functions, logarithms, exponents, and factorials \u2014 with correct PEMDAS/BODMAS order of operations for multi-step expressions.",
    "statistics-calculator": "Statistics calculator gives mean, median, mode, variance, and standard deviation for any dataset \u2014 with step-by-step working shown for each measure of central tendency.",
    "triangle-calculator": "Triangle calculator solves for all missing sides and angles using the law of sines and law of cosines \u2014 from any valid combination of three known values.",
    "volume-calculator": "Volume calculator gives results for spheres, cylinders, cones, cubes, and rectangular prisms \u2014 showing the formula used and supporting both metric and imperial inputs.",

    # Science
    "acceleration-calculator": "Acceleration calculator uses a = \u0394v/\u0394t and Newton's second law (a = F/m) \u2014 with reference values: Earth gravity 9.8 m/s\u00b2, typical car 3.4\u20135.4 m/s\u00b2, sports car up to 9 m/s\u00b2.",
    "atom-calculator": "Atomic structure calculator gives protons, neutrons, electrons, and atomic mass from periodic table data \u2014 covering isotopes, ion charge states, and nuclear binding energy.",
    "bandwidth-calculator": "Bandwidth calculator converts Mbps to MBps (divide by 8) and gives file transfer time at any connection speed \u2014 a 4GB file at 100 Mbps takes approximately 5 minutes 20 seconds.",
    "boyles-law-calculator": "Boyle's Law calculator applies P\u2081V\u2081 = P\u2082V\u2082 to find pressure or volume at constant temperature \u2014 with real-world applications in scuba diving, syringes, and engine compression.",
    "capacitance-calculator": "Capacitance calculator gives total capacitance for series circuits (1/C_total = 1/C\u2081 + 1/C\u2082) and parallel circuits (C_total = C\u2081 + C\u2082) \u2014 with unit conversion between F, \u00b5F, nF, and pF.",
    "charles-law-calculator": "Charles's Law calculator applies V\u2081/T\u2081 = V\u2082/T\u2082 to find gas volume or temperature at constant pressure \u2014 temperatures entered in Celsius are converted to Kelvin automatically.",
    "density-calculator": "Density calculator gives density, mass, or volume from any two known values using \u03c1 = m/V \u2014 with a reference table of common material densities in kg/m\u00b3 and g/cm\u00b3.",
    "half-life-calculator": "Radioactive decay calculator uses N = N\u2080 \u00d7 (\u00bd)^(t/t\u00bd) to find remaining quantity, elapsed time, or half-life \u2014 from any two known values in the decay equation.",
    "ohms-law-calculator": "Ohm's Law calculator solves for voltage, current, resistance, or power from any two known values \u2014 using V = IR and Watt's Law (P = IV) across all four solve modes.",
    "ph-calculator": "pH calculator converts between pH, pOH, and hydrogen ion concentration \u2014 and applies the Henderson-Hasselbalch equation for buffer solution calculations.",
    "speed-calculator": "Speed, distance, and time calculator solves for the missing variable using v = d/t \u2014 with conversion between mph, km/h, m/s, and knots, plus real-world reference speeds.",
    "temperature-calculator": "Temperature converter gives exact results between Celsius, Fahrenheit, and Kelvin \u2014 with key reference points: water boils at 100\u00b0C / 212\u00b0F / 373.15K.",

    # Income and Creator
    "ad-revenue-calculator": "Ad revenue calculator estimates earnings from CPM and pageviews \u2014 finance content earns $15\u201340 RPM, entertainment earns $1\u20135 RPM, showing how niche drives the difference.",
    "bio-link-ctr-calculator": "Bio link CTR calculator gives click-through rate from profile visits and link clicks \u2014 and compares your result against average benchmarks for Instagram, TikTok, and Twitter.",
    "cpm-calculator": "CPM calculator solves for cost per thousand impressions, total impressions, or total ad spend from any two known values \u2014 covering both advertiser and publisher perspectives.",
    "influencer-rate-calculator": "Influencer rate calculator estimates fair sponsorship pricing based on follower count, engagement rate, and platform \u2014 with benchmarks for nano, micro, macro, and mega tiers.",
    "etsy-fee-calculator": "Etsy fee calculator gives net profit per sale after the $0.20 listing fee, 6.5% transaction fee, and payment processing fee \u2014 so you know your real margin before pricing.",
    "youtube-channel-health-calculator": "YouTube channel health calculator scores views, watch time, and subscriber growth rate \u2014 and compares your retention and RPM against YouTube Partner Program thresholds.",

    # Everyday
    "age-calculator": "Age calculator gives exact age in years, months, weeks, and days \u2014 handles leap years correctly and calculates elapsed time between any two past or future dates.",
    "basic-calculator": "Standard calculator handles multi-step arithmetic with correct PEMDAS/BODMAS order of operations \u2014 supports parentheses, chain calculations, and keyboard input.",
    "bra-size-calculator": "Bra size calculator gives your size from underbust and bust measurements \u2014 and converts between US, UK, EU, and AU sizing systems with the band and cup explained.",
    "brick-calculator": "Brick calculator gives the number of bricks needed for any wall from dimensions and brick size \u2014 with a 10% waste factor and mortar joint allowance included.",
    "btu-calculator": "BTU calculator gives the right air conditioner capacity for any room size \u2014 based on the 20 BTU per sq ft baseline adjusted for ceiling height, sun exposure, and occupancy.",
    "cement-calculator": "Concrete quantity calculator gives bags and cubic metres needed for any slab \u2014 a 4m\u00d73m\u00d70.1m slab requires 1.2 m\u00b3, approximately 48 bags of standard 25kg premix.",
    "date-calculator": "Date calculator gives the number of days between any two dates \u2014 or adds and subtracts days from a date \u2014 accounting for leap years with results in days, weeks, and months.",
    "discount-calculator": "Discount calculator gives the final price after any percentage off \u2014 or finds the discount percentage needed to reach a target price \u2014 with reverse and stacked discount modes.",
    "gpa-calculator": "GPA calculator gives semester and cumulative GPA from course grades and credit hours \u2014 supporting both the 4.0 scale and percentage-based grading systems.",
    "grade-calculator": "Grade calculator finds the score needed on a final exam to reach your target course grade \u2014 enter current grades, weightings, and your goal to get the minimum required mark.",
    "password-generator": "Password generator creates strong random passwords with custom length, symbols, numbers, and case \u2014 and shows entropy score and estimated crack time for each result.",
    "roman-numeral-calculator": "Roman numeral calculator converts between integers and Roman numerals in both directions \u2014 covering I to MMMCMXCIX (1\u20133,999) with step-by-step numeral breakdown.",
    "time-calculator": "Time calculator adds and subtracts hours, minutes, and seconds \u2014 and gives elapsed time between any two clock times, including overnight gaps that cross midnight.",
    "unit-converter": "Unit converter handles length, weight, volume, area, temperature, and speed between metric and imperial systems \u2014 showing the conversion formula used for each result.",

    # Engineering
    "base64-tool": "Base64 encoder and decoder converts text or binary data to Base64 and back \u2014 used in data URLs, email attachments, and API authentication headers, not encryption.",
    "buffer-calculator": "Buffer solution calculator applies the Henderson-Hasselbalch equation (pH = pKa + log[A\u207b]/[HA]) \u2014 with a reference table of common buffer systems and their pKa values.",
    "resistor-calculator": "Resistor colour band calculator decodes 4-band and 5-band resistors \u2014 and calculates total resistance for any combination of resistors in series or parallel.",

    # Construction
    "boat-loan-calculator": "Boat loan calculator gives monthly payment and total interest for loans from 10\u201320 years \u2014 typical boat financing terms \u2014 at current marine lending rates.",
    "flooring-calculator": "Flooring calculator gives square footage needed with a 10% waste factor \u2014 supporting rectangular and L-shaped rooms with conversion between sq ft, sq m, and sq yd.",
    "mulch-calculator": "Mulch calculator gives cubic yards needed from bed dimensions and depth \u2014 standard depth is 3 inches, and the result converts between cubic yards, cubic feet, and bags.",
    "paint-calculator": "Paint calculator gives gallons needed for any room \u2014 one gallon covers 350\u2013400 sq ft \u2014 adjusted for doors, windows, number of coats, and wall height.",
    "roofing-calculator": "Roofing calculator gives squares needed (1 square = 100 sq ft) from roof dimensions \u2014 including pitch adjustment factor, waste percentage, and material quantity per square.",
    "wallpaper-calculator": "Wallpaper calculator gives rolls needed from room dimensions \u2014 accounting for pattern repeat, standard roll width, and ceiling height, with a guide to European roll sizes.",

    # Miscellaneous
    "zodiac-calculator": "Zodiac calculator gives Western and Chinese zodiac signs from any birth date \u2014 with personality traits, element, and compatible signs for each result.",
    "gst-calculator": "GST calculator adds or removes Goods and Services Tax at any rate \u2014 showing net price, GST amount, and gross price separately for Australian, NZ, Indian, and Canadian rates.",
    "love-calculator": "Fun compatibility estimator based on name numerology \u2014 a lighthearted tool for entertainment, not a scientific measurement of relationship compatibility.",
}

def update_meta(filepath, new_desc):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content

    # Update name="description"
    content = re.sub(
        r'(<meta data-rh="true" name="description" content=").*?(" />)',
        r'\1' + new_desc + r'\2',
        content,
        count=1
    )
    # Update property="og:description"
    content = re.sub(
        r'(<meta data-rh="true" property="og:description" content=").*?(" />)',
        r'\1' + new_desc + r'\2',
        content,
        count=1
    )
    # Update name="twitter:description"
    content = re.sub(
        r'(<meta data-rh="true" name="twitter:description" content=").*?(" />)',
        r'\1' + new_desc + r'\2',
        content,
        count=1
    )
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    updated = 0
    skipped = 0
    errors = []

    for folder, new_desc in META.items():
        fp = os.path.join(BASE, folder, "index.html")
        if not os.path.exists(fp):
            errors.append(f"MISSING: {folder}/index.html")
            continue
        if update_meta(fp, new_desc):
            updated += 1
            safe = new_desc[:80].encode("ascii", "replace").decode("ascii")
            print(f"OK: {folder} -> {safe}...")
        else:
            skipped += 1

    for e in errors:
        print(e)
    print(f"\nSummary: {updated} updated, {skipped} skipped (no changes), {len(errors)} missing")

if __name__ == "__main__":
    main()

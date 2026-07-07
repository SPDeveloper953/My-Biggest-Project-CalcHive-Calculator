DATA = {}

def add(k, n, i1, i2, h2, b, th, tr, fq):
    DATA[k] = {"name": n, "intro1": i1, "intro2": i2, "h2": h2, "body": b, "th": th, "tr": tr, "faqs": fq}

add("401k-calculator-index", "401k Calculator",
    "A 401k is a tax-advantaged retirement savings account offered by employers. For 2025, the IRS allows employees to contribute up to $23,000 (or $30,500 with catch-up at 50+). Many employers match contributions, effectively providing free money toward retirement.",
    "The core advantage is the employer match: if your employer offers 50% up to 6% of salary and you earn $70,000, contributing 6% ($4,200) earns you $2,100 in matching funds - an immediate 50% return.",
    "How Employer Match Accelerates Your Savings",
    "A 35-year-old earning $80,000 contributing 10% with a 4% employer match grows to ~$980,000 over 30 years at 7%. The same saver at 6% accumulates ~$780,000 - a $200,000 difference.",
    ["Strategy","Monthly Contribution","Employer Match","Projected at 65 (7%)"],
    [["Minimum to get match","$350","$175","$425,000"],["10% contribution","$583","$175","$620,000"],["15% contribution","$875","$175","$860,000"],["Max out ($23,000)","$1,917","$175","$1,720,000"]],
    [["What is employer match and how does it work?","Your employer contributes to your 401k based on your contributions. A 50% match up to 6% means if you contribute 6% of salary, your employer adds 3% of salary. Always contribute enough to get the full match."],
     ["Traditional vs Roth 401k?","Traditional = pre-tax contributions, taxed on withdrawal. Roth = after-tax contributions, tax-free withdrawals. Choose Traditional if you expect lower taxes in retirement; Roth if you expect higher taxes."],
     ["What happens to 401k when leaving a job?","Options: leave it, roll over to new employer's plan, roll into an IRA, or cash out (subject to tax and 10% penalty if under 59.5). Direct IRA rollover is usually best."],
     ["At what age can you withdraw penalty-free?","59.5 for most accounts. If leaving a job at 55+, you can access that 401k without penalty. Hardship withdrawals and first-time home purchases (up to $10,000 from IRA) also have exceptions."],
     ["What is the 2025 contribution limit?","$23,000 employee limit ($30,500 with catch-up at 50+). Combined employee-plus-employer limit: $70,000 ($77,500 with catch-up). Limits adjusted annually for inflation."]]
)

add("acceleration-calculator-index", "Acceleration Calculator",
    "Acceleration is the rate of change of velocity over time, measured in m/s\u00b2. A car going 0-60 mph (0-26.8 m/s) in 6 seconds has average acceleration of 4.47 m/s\u00b2. The formula a = \u0394v/\u0394t computes acceleration, velocity change, or elapsed time.",
    "Newton's second law (F = ma) connects this to force. A 1,500 kg car accelerating at 4.47 m/s\u00b2 needs ~6,705 N of force. Heavier objects require more force for the same acceleration.",
    "Real-World Acceleration Values",
    "Free fall on Earth is 9.81 m/s\u00b2 regardless of mass. A family sedan accelerates at 3.5-4.5 m/s\u00b2. A Porsche 911 Turbo S achieves 8.7 m/s\u00b2. Hard braking exceeds -10 m/s\u00b2.",
    ["Scenario","Acceleration (m/s\u00b2)","Notes"],
    [["Free fall (Earth)","9.81","Constant in vacuum"],["Family sedan (0-60 mph)","3.5-4.5","7-9 second 0-60"],["Sports car (0-60 mph)","7-9","3-4 second 0-60"],["Hard braking (car)","-8 to -10","Negative acceleration"],["Roller coaster launch","10-15","Brief burst"],["Space shuttle launch","29","~3 Gs at liftoff"]],
    [["What is the formula for acceleration?","a = \u0394v/\u0394t. SI unit: m/s\u00b2. Positive = speeding up; negative = slowing down (deceleration)."],
     ["What does negative acceleration mean?","It means the object is slowing down. A car braking from 20 m/s to 0 in 4 seconds has acceleration of -5 m/s\u00b2."],
     ["What is free fall acceleration?","9.81 m/s\u00b2 downward on Earth (denoted g). In a vacuum, all objects fall at the same rate regardless of mass."],
     ["Difference between acceleration and velocity?","Velocity = speed with direction (m/s). Acceleration = rate of change of velocity (m/s\u00b2)."],
     ["How to calculate force from acceleration?","F = ma. For a 70 kg person at 3 Gs (29.4 m/s\u00b2): force = 70 \u00d7 29.4 = 2,058 N."]]
)

add("ad-revenue-calculator-index", "Ad Revenue Calculator",
    "Display ad revenue = (Page Views \u00d7 CPM) / 1,000. A site with 100,000 monthly views at $10 CPM earns $1,000/month. Actual earnings depend on niche, audience location, and ad placement.",
    "CPM (cost per mille) is the advertiser rate. RPM (revenue per mille) is what publishers earn after the ad network's cut and unsold inventory. Finance blogs command $25-50 RPM; entertainment sites see $3-8.",
    "CPM Benchmarks by Content Niche",
    "A lifestyle blog with 200,000 monthly views at $5 RPM earns $1,000/month. A finance site with the same traffic at $25 RPM earns $5,000. Niche selection matters as much as traffic.",
    ["Content Niche","Typical CPM Range","Typical RPM Range"],
    [["Finance & Investing","$15-$40","$10-$30"],["Technology & SaaS","$10-$25","$6-$18"],["Health & Fitness","$8-$20","$5-$14"],["Entertainment & Humor","$2-$5","$1-$4"],["Lifestyle & Travel","$5-$12","$3-$8"],["Education","$6-$15","$4-$10"]],
    [["What is CPM?","Cost per mille = price advertisers pay per 1,000 impressions. $12 CPM = $12 per 1,000 ad displays."],
     ["CPM vs RPM?","CPM is the advertiser rate. RPM is what publishers actually earn after network cuts. $10 CPM with 30% network cut = $7 RPM."],
     ["What is a good CPM?","Depends on niche. Finance: $15-40. Entertainment: $2-5. General blogs: $5-10. US/UK traffic earns much higher rates than other regions."],
     ["Which niche earns highest CPM?","Finance/investing at $30-50. B2B SaaS, legal, and medical topics also command above-average rates due to high audience purchasing power."],
     ["Does layout affect ad revenue?","Yes. Above-fold ads, sticky units, and more pages per visit boost revenue. Excessive ads hurt UX and are penalized by Google. 2-3 ad units per page is standard."]]
)

add("age-calculator-index", "Age Calculator",
    "Calculates exact age in years, months, and days between two dates. Handles leap years (divisible by 4, 100, 400). Born March 15, 1990: on July 6, 2026, you are 36 years, 3 months, 21 days old.",
    "Subtracts dates component by component, borrowing days from the previous month or a full year when needed. Precise to the exact day for legal and medical purposes.",
    "Age Unit Conversions and Practical Uses",
    "30 years = ~10,957 days (including ~7-8 leap days), ~1,565 weeks, or 360 months. Exact day count is needed for medication dosages, age eligibility, and milestone tracking.",
    ["Unit","Value per Year","At Age 30","Common Use"],
    [["Days","365 (366 in leap)","~10,957","Medical dosing"],["Weeks","52.1775","~1,565","Pregnancy tracking"],["Months","12","360","General reporting"],["Hours","8,760","~262,944","Employment history"],["Years","1","30","Standard age"]],
    [["How is exact age calculated?","Subtract birth date from target date, borrowing days from months and months from years as needed. The result shows years, months, and days."],
     ["Born on Feb 29?","Treated as Feb 28 or March 1 in non-leap years. Legal age of 21 reached on March 1 in non-leap years."],
     ["How many days old am I?","Years \u00d7 365 + leap days lived through. A 30-year-old born after Feb 28, 1996, is about 10,957 days old."],
     ["What is the legal age of majority?","18 in most US states and Europe. 18 in Japan (reduced from 20 in 2022). 21 for drinking in the US."],
     ["Can I calculate any date difference?","Yes. Use it for project deadlines, relationship duration, time between historical events, or days until retirement."]]
)

add("alcohol-calorie-calculator-index", "Alcohol Calorie Calculator",
    "Alcohol has 7 calories per gram, nearly as dense as fat (9 cal/g) and double carbs/protein (4 cal/g). A 12oz beer at 5% ABV has ~150 cal. 5oz wine ~120-130 cal. 1.5oz spirits ~97 cal.",
    "Mixers add 100-300 extra calories per serving. A rum and cola has ~180 cal from alcohol + 140 cal from cola = ~320 cal total.",
    "Calories in Standard Alcoholic Drinks",
    "Switching from regular beer (150 cal) to light beer (100 cal) saves 50 cal per drink. Two beers daily = 3,500 cal/month saved = ~1 lb body fat lost per month.",
    ["Drink Type","Serving Size","Calories","Alcohol (g)"],
    [["Regular beer","12 oz","150","14"],["Light beer","12 oz","100","11"],["Red wine","5 oz","125","15.5"],["White wine","5 oz","120","15"],["80-proof spirits","1.5 oz","97","14"],["Margarita","8 oz","280","18"]],
    [["How many calories in a beer?","Regular 12 oz beer: ~150 cal. Light beer: ~100 cal. Craft beer/IPA: 180-300 cal due to higher alcohol content and residual sugars."],
     ["Which alcohol has fewest calories?","Straight spirits: ~97 cal per 1.5 oz. Light beer: ~100 cal per 12 oz. Dry wine: ~120-125 cal per 5 oz."],
     ["Does alcohol affect fat loss?","Yes. The body pauses fat burning to metabolize alcohol. A 2015 study found >30g alcohol/day (>2 drinks) linked to increased abdominal fat."],
     ["Do mixers add calories?","12 oz cola = 140 cal. Tonic water = 125 cal. Juice = 110-160 cal per 8 oz. Diet soda = 0 cal. A rum and Diet Coke has ~100 cal vs ~240 with regular Coke."],
     ["Does cooking remove alcohol calories?","Mostly. Ethanol evaporates during cooking, removing the alcohol calories. Added sugars or fats in the dish still contribute."]]
)

add("amortization-calculator-index", "Amortization Calculator",
    "Amortization pays off debt through equal scheduled payments over a fixed term. Early mortgage payments are mostly interest. A $300,000 loan at 7%: first payment of ~$1,996 allocates $1,750 to interest and only $246 to principal.",
    "By year 15 of a 30-year mortgage at 7%, each payment splits ~$1,250 interest and $746 principal. By the final payment, nearly all goes to principal. Extra early payments have outsized savings.",
    "How Early Mortgage Payments Work",
    "One extra $1,996 payment per year on a $300,000 mortgage at 7% reduces total interest by ~$87,000 and shortens the term from 30 to ~23 years.",
    ["Payment #","Amount","Interest","Principal","Balance"],
    [["1","$1,996","$1,750","$246","$299,754"],["2","$1,996","$1,748","$248","$299,506"],["12","$1,996","$1,728","$268","$296,208"],["60","$1,996","$1,565","$431","$267,620"],["180","$1,996","$989","$1,007","$168,310"],["360","$1,996","$12","$1,984","$0"]],
    [["What is amortization?","Fixed payments covering both interest and principal. Early payments are mostly interest; later payments mostly principal."],
     ["Why are early payments mostly interest?","Interest is calculated on the outstanding balance, which is highest at the start of the loan term."],
     ["What happens with extra principal payments?","They reduce the balance permanently, saving future interest. One extra payment/year can save tens of thousands and shorten the term by 5-7 years."],
     ["How to read an amortization schedule?","Lists every payment with number, total, interest portion, principal portion, and remaining balance."],
     ["Amortization vs depreciation?","Amortization = loan repayment over time. Depreciation = spreading an asset's cost over its useful life."]]
)

add("annuity-calculator-index", "Annuity Calculator",
    "An annuity is a series of equal payments at regular intervals, used in mortgages, pensions, and lottery payouts. Present value = PMT \u00d7 [1 - (1+r)^(-n)] / r.",
    "Ordinary annuities pay at period end (mortgages). Annuities due pay at period start (rent). Annuities due are worth slightly more because payments earn interest one period longer.",
    "Present Value of $1,000/Year at Different Rates",
    "Receiving $1,000/year for 20 years at 6% discount rate has PV of ~$11,470 today. At 3%, PV = ~$14,877. Lower discount rates increase PV of future cash flows.",
    ["Rate","10 Years","20 Years","30 Years"],
    [["3%","$8,530","$14,877","$19,600"],["5%","$7,722","$12,462","$15,372"],["7%","$7,024","$10,594","$12,409"],["10%","$6,145","$8,514","$9,427"]],
    [["Ordinary annuity vs annuity due?","Ordinary = payments at period end. Annuity due = payments at period start. Annuity due is worth more due to extra compounding period."],
     ["How is PV of an annuity calculated?","PV = PMT \u00d7 [1 - (1+r)^(-n)] / r. For annuity due, multiply by (1+r)."],
     ["What is a good annuity payout rate?","Depends on interest rates. A 65-year-old with $100,000 fixed immediate annuity might get $500-600/month for life."],
     ["Are annuity payments guaranteed?","Fixed annuities: guaranteed by the insurer. Variable: fluctuate with investments. State guaranty associations protect up to $250,000-$500,000."],
     ["Can you lose money in an annuity?","Fixed annuities protect principal. Variable/indexed annuities can lose value with poor market performance. Surrender charges for early withdrawal."]]
)

add("annuity-payout-calculator-index", "Annuity Payout Calculator",
    "Estimates how long a lump sum lasts with fixed monthly withdrawals, or the sustainable withdrawal amount. $500,000 at 5% sustains $2,679/month for 25 years.",
    "The 4% withdrawal rule (Trinity Study) suggests withdrawing 4% of portfolio value in year one (adjusting for inflation) gives high probability of lasting 30 years. On $1M: $40,000/year.",
    "Monthly Payout from $500,000",
    "A $1M portfolio earning 6% with $4,000/month withdrawals lasts ~29 years. At 4%, it lasts ~22 years. The 7-year gap shows why conservative return assumptions matter.",
    ["Annual Rate","10-Year Payout","20-Year Payout","30-Year Payout"],
    [["4%","$5,044","$3,017","$2,371"],["5%","$5,305","$3,300","$2,684"],["6%","$5,551","$3,582","$2,998"],["7%","$5,806","$3,877","$3,327"],["8%","$6,066","$4,182","$3,670"]],
    [["What is the 4% withdrawal rule?","Withdraw 4% of initial portfolio in year one (inflation-adjusted) for high probability of lasting 30 years. $1M = $40,000/year."],
     ["How long will $1 million last?","At 4% withdrawal ($40,000/year): at least 30 years. At 6% ($60,000/year): 15-20 years. Depends on returns and inflation."],
     ["Does inflation affect payouts?","Yes. Fixed $3,000/month in 2025 = ~$1,800 in 2055 at 2.5% inflation. Inflation-adjusted withdrawals reduce initial safe rate."],
     ["What is sequence-of-returns risk?","Poor returns early in retirement severely reduce portfolio longevity. A 15% loss in year one with ongoing withdrawals recovers poorly vs the same average return spread evenly."],
     ["How do taxes affect annuity payouts?","Traditional account withdrawals taxed as income (15-30% lower after tax). $40,000 from traditional IRA may leave $32,000-$34,000 after federal taxes."]]
)

add("anorexic-bmi-calculator-index", "Anorexic BMI Calculator",
    "Identifies clinically underweight ranges where medical attention may be needed. BMI below 18.5 = underweight (WHO). Below 17.0 = moderate/severe underweight. For educational purposes only.",
    "Anyone concerned about eating disorders should seek professional medical support. This calculator is not a diagnostic tool. Contact a healthcare provider or the NEDA helpline if concerned.",
    "WHO BMI Classifications for Low Body Weight",
    "A 165 cm woman weighing 45 kg has BMI 16.5 (severe underweight), carrying risks of weakened immune function, bone density loss, cardiac complications, and hormonal disruptions.",
    ["BMI Range","Classification","Health Risk Level"],
    [["Below 15.0","Severely underweight","Very high - urgent medical attention"],["15.0-16.9","Moderately underweight","High - medical evaluation advised"],["17.0-18.49","Mildly underweight","Moderate - monitoring recommended"],["18.5-24.9","Normal weight","Low"]],
    [["What BMI is dangerously underweight?","BMI below 16.0 is very dangerous, with risks of organ failure, osteoporosis, cardiac arrhythmias, and severe malnutrition. Immediate medical intervention needed."],
     ["Health risks of very low BMI?","Weakened immunity, bone density loss, cardiac arrhythmias, hormonal disruptions, muscle wasting, cognitive impairment, and in severe cases multi-organ failure."],
     ["When to seek help for low weight?","BMI below 17.0 warrants medical evaluation. Warning signs: rapid unintentional weight loss, food restriction, purging, excessive exercise, body image distortion."],
     ["Is BMI accurate for very low weights?","BMI is a screening tool. It doesn't distinguish muscle from fat loss. Additional assessments (blood tests, bone density scans) are needed for a full picture."],
     ["Is this calculator anonymous?","Yes. All calculations are in-browser with no data sent to any server. No personal information is stored or transmitted. Consult a healthcare provider for personal medical advice."]]
)

add("apr-calculator-index", "APR Calculator",
    "APR (Annual Percentage Rate) includes both the interest rate and mandatory fees, as required by the Truth in Lending Act. A 6% loan with $3,000 fees on $200,000 over 30 years has an APR of ~6.19%.",
    "The 0.19% APR difference adds ~$7,800 in extra cost over 30 years. APR is the correct metric for comparing loan offers.",
    "How Fees Increase Your Effective Rate",
    "A $25,000 auto loan at 5% with a $500 fee increases APR to ~5.57% and adds $540 in total interest. On small loans, fees have proportionally larger APR impact.",
    ["Loan Amount","Stated Rate","Fees","APR","Extra Cost"],
    [["$200,000","6.0%","$1,000","6.06%","$2,600"],["$200,000","6.0%","$3,000","6.19%","$7,800"],["$200,000","6.0%","$5,000","6.32%","$13,000"],["$25,000 (car)","5.0%","$500","5.57%","$540"],["$25,000 (car)","5.0%","$1,000","6.12%","$1,080"]],
    [["Interest rate vs APR?","Interest rate = nominal cost of borrowing. APR = rate + all mandatory fees spread over the term. APR is always >= interest rate."],
     ["Does APR affect monthly payment?","Yes, indirectly. The APR includes fees amortized into the loan, which slightly increases the monthly payment compared with the rate alone."],
     ["What is a good mortgage APR in 2025?","6.5-7.0% for borrowers with 740+ credit. Conventional loans have lower APRs than FHA. Shopping 3+ lenders can save 0.25-0.5%."],
     ["What is a good credit card APR?","18-22% for excellent credit. Rewards cards have higher APRs. Many offer 0% intro APR for 12-18 months on purchases/balance transfers."],
     ["Fixed vs variable APR?","Fixed = never changes. Variable = changes with prime rate. Variable starts lower but carries risk of increases."]]
)

add("area-calculator-index", "Area Calculator",
    "Area measures 2D space in square units. This calculator supports rectangle, circle, triangle, trapezoid, ellipse, parallelogram, sector, square, and regular polygon.",
    "Each shape has a distinct formula: rectangle = L\u00d7W, circle = \u03c0r\u00b2, triangle = \u00bd\u00d7b\u00d7h. Irregular shapes can be divided into standard components.",
    "Area Formulas for Common Shapes",
    "A 10 ft \u00d7 12 ft bedroom = 120 sq ft. Buying carpet needs ~10% extra for waste = 132 sq ft. Area calculation is essential for construction and design.",
    ["Shape","Formula","Example"],
    [["Rectangle","L \u00d7 W","5m \u00d7 3m = 15 m\u00b2"],["Circle","\u03c0r\u00b2","r=2m, area=12.57 m\u00b2"],["Triangle","\u00bd \u00d7 b \u00d7 h","b=4m, h=3m, area=6 m\u00b2"],["Trapezoid","\u00bd(a+b) \u00d7 h","a=2m, b=4m, h=3m, area=9 m\u00b2"],["Ellipse","\u03c0ab","a=2m, b=1.5m, area=9.42 m\u00b2"],["Parallelogram","b \u00d7 h","b=5m, h=2m, area=10 m\u00b2"]],
    [["Area of a circle?","A = \u03c0r\u00b2, where r = radius (half the diameter). Diameter 10 cm = radius 5 cm, area = \u03c0 \u00d7 25 = 78.54 cm\u00b2."],
     ["How to calculate irregular shape area?","Divide into standard shapes, calculate each, and sum. An L-shaped room = two rectangles. Or use the grid method: count squares of known size."],
     ["How many sq ft in an acre?","43,560 sq ft. A square acre = ~208.7 ft per side. Also 4,047 m\u00b2 or 0.4047 hectares. A football field including end zones = ~1.32 acres."],
     ["Convert sq metres to sq feet?","Multiply m\u00b2 by 10.764. 100 m\u00b2 = 1,076.4 sq ft. Divide sq ft by 10.764 for reverse."],
     ["Area vs perimeter?","Area = 2D space inside (square units). Perimeter = distance around (linear units). A 10 ft square has area 100 sq ft and perimeter 40 ft."]]
)

add("army-body-fat-calculator-index", "Army Body Fat Calculator",
    "The US Army uses circumference-based body fat measurements. The tape test measures neck and waist (men) or neck, waist, and hip (women), estimating body fat percentage.",
    "Unlike BMI, the tape method accounts for body composition. A 180 lb male soldier at 5'10\" with 15.5\" neck and 35\" waist has ~17.5% body fat. The max for age 17-20 is 20%.",
    "Army Body Fat Standards by Age and Gender",
    "Men aged 40+: max 26% body fat. Women 40+: max 36%. Soldiers exceeding weight standards are tape-tested. Those exceeding both enter the Army Body Composition Program.",
    ["Age Group","Male Max %","Female Max %"],
    [["17-20","20%","30%"],["21-27","22%","32%"],["28-39","24%","34%"],["40+","26%","36%"]],
    [["How accurate is the Army tape test?","~2-3% margin of error vs DEXA scanning. Accurate enough for screening. Affected by hydration, exercise, and measurement technique."],
     ["2025 Army body fat standards?","Men 17-20: 20% max, increasing to 26% at 40+. Women 17-20: 30% max, increasing to 36% at 40+."],
     ["What happens if you fail?","Enrolled in the Army Body Composition Program (ABCP) with counseling, PT plans, and regular weigh-ins. Continued failure can lead to separation."],
     ["Can you pass weight but fail body fat?","Meeting the weight standard = automatic compliance. If over screening weight, you must pass the tape test. Possible to fail tape when only slightly over weight."],
     ["How to measure correctly?","Neck: below larynx at narrowest. Waist (men): at navel. Waist (women): smallest point between ribs and iliac crest. Tape snug, not compressing. Average two measurements."]]
)

add("atom-calculator-index", "Atom Calculator",
    "Determines protons, neutrons, and electrons from atomic number (Z) and mass number (A). Protons = Z (defines the element). Electrons = Z for neutral atoms. Neutrons = A - Z.",
    "Uranium-238: Z=92, A=238, so 146 neutrons. Carbon-12: 6 neutrons. Carbon-14: 8 neutrons. Same protons, different neutrons = isotopes.",
    "Atomic Structure of Selected Elements",
    "Oxygen (Z=8) has 2 electrons in inner shell and 6 in valence shell, making it highly reactive. Noble gases like neon (Z=10) have full outer shells.",
    ["Element","Atomic #","Mass #","Protons","Neutrons","Electrons"],
    [["Hydrogen","1","1","1","0","1"],["Carbon","6","12","6","6","6"],["Oxygen","8","16","8","8","8"],["Uranium","92","238","92","146","92"],["Gold","79","197","79","118","79"],["Iron","26","56","26","30","26"]],
    [["How to calculate neutrons?","Neutrons = Mass Number - Atomic Number. Carbon-14: 14 - 6 = 8 neutrons. Carbon-12: 12 - 6 = 6 neutrons."],
     ["Atomic mass vs atomic number?","Atomic number (Z) = number of protons (determines the element). Atomic mass (A) = protons + neutrons. Same element always has same Z but can have different A (isotopes)."],
     ["What is an isotope?","Same protons, different neutrons. Hydrogen isotopes: protium (1p, 0n), deuterium (1p, 1n), tritium (1p, 2n, radioactive)."],
     ["How to find electron configuration?","Fill orbitals: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p. Carbon (6e): 1s\u00b2 2s\u00b2 2p\u00b2. Follow Aufbau, Pauli, and Hund's rules."],
     ["What are valence electrons?","Outermost electrons involved in bonding. Group 1: 1 valence electron. Group 14 (carbon): 4. Group 18 (neon): 8, making it stable."]]
)

add("auto-lease-calculator-index", "Auto Lease Calculator",
    "An auto lease pays for the car's depreciation during the lease term, plus interest. Monthly payment = (Capitalized Cost - Residual Value) / Term + (Cap Cost + Residual) \u00d7 Money Factor.",
    "$35,000 car, 55% residual ($19,250), 36 months, 0.00125 money factor (3.0% APR), $1,000 down: monthly payment ~$405 before tax.",
    "Lease vs Buy on a $35,000 Car",
    "Leasing 36 months with $0 down and 55% residual = ~$14,580 total payments, return car. Buying with 60-month loan at 6.5% = ~$41,000 total but own car worth ~$19,000 after 3 years.",
    ["","Lease (36 mo)","Buy (60 mo)"],
    [["Monthly payment","$405","$685"],["Upfront cost","$1,000","$0"],["Total over 36 months","$15,580","$24,660"],["Asset after 36 months","$0 (returned)","~$19,250"],["Net cost (36 months)","$15,580","$5,410"]],
    [["How is lease payment calculated?","(Cap Cost - Residual) / Term + (Cap Cost + Residual) \u00d7 Money Factor. First part = depreciation. Second = interest (rent charge). Add tax."],
     ["What is residual value?","Car's estimated worth at lease end as % of MSRP. 55% residual on $35,000 = $19,250 after 36 months. Higher residual = lower monthly payment."],
     ["What is money factor?","The interest rate equivalent. Multiply by 2,400 for APR. MF 0.00125 = 3.0% APR. Lower = cheaper financing. Dealers may mark up the manufacturer's MF."],
     ["Is leasing cheaper than buying?","Leasing: lower monthly payments, return car. Buying: higher payments but own asset. Over 3 years, leasing may cost less. Over 10 years, buying wins."],
     ["What happens at lease end?","Return car (pay excess mileage/damage), buy at residual value, or trade for new lease. Mileage limits: 10,000-15,000 miles/year. Overage: $0.15-$0.30/mile."]]
)

add("auto-loan-calculator-index", "Auto Loan Calculator",
    "Computes monthly car payment and total interest. $25,000 at 7% for 60 months = $495/month, $4,708 total interest. 72 months = $426/month but $5,674 interest ($969 more).",
    "The trade-off: lower payment vs higher total cost. 48 months = $599/month, $3,732 interest. Choose the shortest term you can afford.",
    "Monthly Payments at Different Car Prices",
    "720+ credit score: ~5.5% on new car. 620-660: 9-12%. On $30,000 for 60 months, the gap between 5.5% ($573/mo, $4,380 interest) and 10% ($637/mo, $8,220 interest) is $3,840.",
    ["Car Price","5% (48mo)","7% (60mo)","9% (72mo)"],
    [["$20,000","$461","$396","$360"],["$25,000","$576","$495","$450"],["$35,000","$806","$693","$630"],["$45,000","$1,036","$891","$810"]],
    [["What credit score gets best rate?","740+: 4-6% on new cars. 700-739: 6-8%. Below 660: 10%+. Credit unions often beat dealer financing."],
     ["Is 72-month loan a bad idea?","Not if rate is under 6% and you keep the car long term. Risk: being underwater longer. If you need 72 months to afford the payment, buy less car."],
     ["How much car can I afford?","20/4/10 rule: 20% down, 4-year max term, total car costs under 10% of gross income. $60K income = under $500/month for car expenses."],
     ["Good APR for car loan in 2025?","4.5-6.5% for excellent credit on new cars. Used: 1-3% higher. Manufacturer promos (0-1.9%) available for some models."],
     ["Should I put money down?","At least 10-20% to avoid being underwater. On $30,000 car: $3,000-$6,000 down reduces loan amount and ensures positive equity."]]
)

add("average-return-calculator-index", "Average Return Calculator",
    "Distinguishes arithmetic mean from geometric mean (CAGR). Up 50% then down 30% = 10% arithmetic average but only 2.9% CAGR. CAGR is what matters for actual portfolio growth.",
    "CAGR = (Ending Value / Beginning Value)^(1/n) - 1. $10,000 growing to $25,000 over 10 years = 9.5% CAGR.",
    "How $10,000 Grows at Different CAGR Rates",
    "6% vs 10% CAGR on $10,000 over 30 years: $57,435 vs $174,494. A $117,059 difference from just 4% better annual return.",
    ["CAGR Rate","10 Years","20 Years","30 Years"],
    [["4%","$14,802","$21,911","$32,434"],["6%","$17,908","$32,071","$57,435"],["8%","$21,589","$46,610","$100,627"],["10%","$25,937","$67,275","$174,494"],["12%","$31,058","$96,463","$299,599"]],
    [["Average vs compound annual return?","Average (arithmetic) = sum of returns / years. CAGR (geometric) = actual growth rate accounting for compounding. CAGR is always <= arithmetic mean with volatility."],
     ["What is CAGR?","Compound Annual Growth Rate. (EV/BV)^(1/n)-1. Smooths out volatility for a single comparable growth measure."],
     ["Historical stock market return?","S&P 500: ~10% arithmetic average (before inflation), ~9.5% CAGR. Individual decades vary: 2010s = ~13%, 2000s = ~0%."],
     ["How to calculate CAGR?","Divide ending by beginning, raise to 1/years, subtract 1. $15K to $28K over 7 years: ($28K/$15K)^(1/7)-1 = 9.2%."],
     ["Why do funds report both?","A fund returning +40%, -25%, +30% has 15% arithmetic average but only 9.6% CAGR. CAGR reflects actual client experience better."]]
)

add("bac-calculator-index", "BAC Calculator",
    "Blood Alcohol Concentration (BAC) measures % alcohol in blood. Uses the Widmark formula based on drinks, weight, gender, and time elapsed.",
    "A 150 lb man consuming 3 drinks over 2 hours has BAC ~0.064% (below 0.08% legal limit). At 4 drinks: ~0.092% (over the limit).",
    "BAC Limits and Impairment Effects",
    "Alcohol is metabolized at 0.015% BAC/hour. A person with 0.10% BAC needs ~6-7 hours to reach zero. Food slows absorption but doesn't speed elimination.",
    ["BAC Level","Impairment Effects","Legal Status"],
    [["0.02-0.03%","Mild relaxation","Legal"],["0.04-0.06%","Reduced inhibition","Legal (DUI possible)"],["0.08-0.10%","Motor impairment","Illegal (DUI limit)"],["0.15-0.20%","Gross impairment","Aggravated DUI"],["0.25%+","Severe intoxication","Medical emergency"]],
    [["What BAC is legally drunk?","0.08% for drivers 21+ in all US states. Commercial drivers: 0.04%. Under 21: zero tolerance (0.01-0.02%)."],
     ["How many drinks to reach 0.08%?","160 lb man: ~4 standard drinks in 2 hours. 130 lb woman: ~3 drinks. Standard drink = 12 oz beer (5%), 5 oz wine (12%), 1.5 oz spirits (40%)."],
     ["What is one standard drink?","14 grams pure alcohol = 12 oz beer at 5%, 5 oz wine at 12%, or 1.5 oz distilled spirits at 40%. Many craft beers and large pours exceed one drink."],
     ["Does food affect BAC?","Yes. A full meal can reduce peak BAC by 30-50% by slowing alcohol absorption. Food doesn't speed alcohol metabolism, only time does."],
     ["How long to sober up?","0.015% BAC/hour metabolism rate. 0.10% BAC needs ~6-7 hours. Water, coffee, cold showers, and exercise don't accelerate this process."]]
)

add("bandwidth-calculator-index", "Bandwidth Calculator",
    "Bandwidth is data transfer rate in bits per second. 8 bits = 1 byte. A 100 Mbps connection can theoretically download a 4 GB file in ~5.5 minutes.",
    "Actual speeds are 80-95% of advertised due to overhead and congestion.",
    "File Transfer Times at Different Speeds",
    "Streaming Netflix in 4K needs ~25 Mbps. Zoom HD calls: 3-5 Mbps. A 4-person household needs 200-500 Mbps for simultaneous streaming, gaming, and calls.",
    ["File Size","50 Mbps","100 Mbps","500 Mbps","1 Gbps"],
    [["100 MB","16 sec","8 sec","1.6 sec","0.8 sec"],["1 GB","2.7 min","1.4 min","16 sec","8 sec"],["4 GB","10.9 min","5.5 min","1.1 min","32 sec"],["25 GB","68 min","34 min","6.8 min","3.4 min"]],
    [["Bandwidth vs internet speed?","Bandwidth = maximum capacity. Speed = actual throughput. A 100 Mbps connection may deliver 80-90 Mbps real-world."],
     ["Mbps vs MBps?","Mbps = network speed. MBps = file transfer speed. 8 Mbps = 1 MBps. 100 Mbps connection = 12.5 MB/s."],
     ["How much bandwidth for streaming?","HD: 5 Mbps. 4K: 25 Mbps. Two simultaneous 4K streams: 50 Mbps. Typical household: 200-500 Mbps."],
     ["What is latency?","Ping = time for packet to travel and return (ms). Low latency is critical for gaming and video calls. You can have 500 Mbps bandwidth but 150 ms latency."],
     ["Good speed for remote work?","FCC: 25 Mbps down, 3 Mbps up per person. Video calls need 3-5 Mbps each way. Symmetrical 100-200 Mbps fiber is ideal."]]
)

add("base64-tool-index", "Base64 Tool",
    "Base64 encodes binary data as ASCII using A-Z, a-z, 0-9, +, /. Used for email attachments (MIME), data URLs in HTML/CSS, and binary data in JSON.",
    "Increases data size by ~33% (3 bytes binary = 4 ASCII characters). Base64 is encoding, not encryption - provides no security.",
    "Common Base64 Use Cases",
    "Embedding small images (under 1-2 KB) as data URLs in CSS reduces HTTP requests. For larger files, the 33% overhead makes separate serving more efficient.",
    ["Use Case","Description","Context"],
    [["Email attachments","MIME encodes binary","SMTP"],["Data URLs","Embed images in HTML/CSS","Web dev"],["JSON binary transport","Binary in JSON payloads","REST APIs"],["Auth tokens","Basic auth credentials","HTTP headers"],["Crypto keys","Printable key strings","TLS/SSH/PGP"],["QR codes","Binary in QR format","Mobile"]],
    [["What is Base64 used for?","Transmitting binary data through text-only channels: email attachments, data URLs, JSON payloads, HTTP Basic Auth, and crypto keys."],
     ["Is Base64 encryption?","No. It's encoding, not encryption. Anyone can decode it. Never use Base64 to protect sensitive data."],
     ["How does Base64 work?","3 bytes (24 bits) split into four 6-bit values, each mapped to one of 64 characters. Input not multiple of 3 = padding with =."],
     ["What is the overhead?","33.3% increase. A 3 MB image = ~4 MB Base64. Only recommended for small data."],
     ["Can Base64 be decoded?","Yes, it's reversible. Online decoders, base64 -d, and built-in functions in most languages can restore the original data."]]
)

add("basic-calculator-index", "Basic Calculator",
    "Supports addition, subtraction, multiplication, division, and percentages with button and keyboard input. Follows PEMDAS order of operations.",
    "Chain calculations: 5 + 3 = 8, then \u00d7 2 = 16. Memory functions (M+, M-, MR, MC) store values. Division by zero returns an error.",
    "Order of Operations (PEMDAS)",
    "5 + 3 \u00d7 2 = 11 (multiplication first). (5 + 3) \u00d7 2 = 16. Percentage: 200 \u00d7 10% = 20.",
    ["Priority","Operation","Example","Result"],
    [["1","Parentheses","(2+3)\u00d74","20"],["2","Exponents","2+3\u00b2","11"],["3","Multiply/Divide","5+3\u00d72","11"],["4","Add/Subtract","10-4+2","8"]],
    [["What is PEMDAS?","Parentheses, Exponents, Multiplication/Division, Addition/Subtraction. M&D equal priority (left to right); A&S equal priority."],
     ["Division by zero?","Mathematically undefined. Calculator shows error; press AC/C to clear."],
     ["Chain calculations?","Yes. 5 + 3 = 8, then \u00d7 2 = 16. The result becomes the first operand for the next operation."],
     ["Memory buttons?","M+ adds to memory, M- subtracts, MR recalls, MC clears. Useful for storing subtotals."]]
)

add("big-number-calculator-index", "Big Number Calculator",
    "Standard calculators use 64-bit floating point (IEEE 754), precise only up to 2\u2075\u00b3 (~9 quadrillion). This calculator uses arbitrary precision for numbers of any size.",
    "Use cases: RSA cryptography (2,048+ bits), combinatorics (52! = 68-digit number), astronomy (10\u00b2\u2074 stars estimated).",
    "Examples of Large Numbers",
    "20! = 2.43 quintillion (19 digits, fits 64-bit). 30! = 33 digits, exceeds double precision. 100! = 158 digits.",
    ["Expression","Value","Digits","Context"],
    [["20!","2.43 quintillion","19","Card arrangements"],["52!","~8.07\u00d710\u2076\u2077","68","Deck permutations"],["10^100","Googol","101","1 with 100 zeros"],["2^1024","~1.8\u00d710^308","309","RSA-1024 key"]],
    [["What is arbitrary precision?","Calculations with user-defined digits limited only by memory. Contrasts with fixed 32/64-bit precision that rounds large numbers."],
     ["Why do calculators lose precision?","64-bit IEEE 754 has ~15-17 decimal digits. Beyond ~9 quadrillion (2\u2075\u00b3), integer precision is lost."],
     ["Largest number a computer can store?","64-bit: 9,007,199,254,740,991. Beyond that, use arbitrary-precision libraries (Python big ints, Java BigInteger, GMP)."],
     ["Can this handle scientific notation?","Yes. Accepts standard and scientific notation. Results display with proper digit grouping."],
     ["Most common use for big numbers?","Cryptography. RSA uses 2,048-4,096 bit primes. Also used in scientific computing, combinatorics, and high-precision finance."]]
)

add("binary-calculator-index", "Binary Calculator",
    "Binary uses only digits 0 and 1, fundamental to all digital computing. Every piece of computer data is ultimately binary. This calculator performs binary arithmetic and converts between binary, decimal, and hexadecimal.",
    "Binary 1101 = 1\u00d72\u00b3 + 1\u00d72\u00b2 + 0\u00d72\u00b9 + 1\u00d72\u2070 = 13 decimal. Binary addition: 1+1=10 (not 2).",
    "Binary Equivalents of Decimal 0-15",
    "Hexadecimal is a human-readable binary shorthand: each hex digit = 4 binary bits. Byte 11110101 binary = F5 hex.",
    ["Decimal","Binary","Hexadecimal"],
    [["0","0000","0"],["1","0001","1"],["2","0010","2"],["3","0011","3"],["4","0100","4"],["5","0101","5"],["6","0110","6"],["7","0111","7"],["8","1000","8"],["9","1001","9"],["10","1010","A"],["11","1011","B"],["12","1100","C"],["13","1101","D"],["14","1110","E"],["15","1111","F"]],
    [["How to convert binary to decimal?","Multiply each digit by its power of 2 (rightmost = 2\u2070). 1101 = 8+4+0+1 = 13."],
     ["How does binary addition work?","0+0=0, 0+1=1, 1+0=1, 1+1=0 carry 1. 1101+0110 = 10011 (19)."],
     ["Why do computers use binary?","Transistors have two states: on/off. Binary is the simplest to implement reliably in hardware."],
     ["Binary vs octal vs hexadecimal?","Binary = base-2 (0-1), octal = base-8 (0-7), hex = base-16 (0-9,A-F). Each hex digit = 4 binary bits, more compact."],
     ["How to convert decimal to binary?","Repeatedly divide by 2, record remainders backward. 25 = 11001."]]
)

add("bio-link-ctr-calculator-index", "Bio Link CTR Calculator",
    "Bio link CTR = clicks / profile views \u00d7 100. A creator with 50,000 views and 2,500 clicks has a 5% CTR. Benchmarks vary by platform and industry.",
    "Instagram bio link CTR averages 3-6%. TikTok: 1-3%. Finance and education niches often achieve higher CTRs due to audience intent.",
    "Bio Link CTR Benchmarks by Platform",
    "A creator with 100,000 profile views and a 5% CTR generates 5,000 bio link clicks. Improving CTR from 3% to 6% doubles traffic from the same audience, making CTR optimization one of the highest-ROI activities for content creators.",
    ["Platform","Average CTR Range","Top 10% CTR"],
    [["Instagram","3-6%","8-12%"],["TikTok","1-3%","4-7%"],["YouTube","2-5%","6-10%"],["Twitter/X","1.5-4%","5-8%"],["LinkedIn","2.5-5%","7-10%"]],
    [["Good CTR for Instagram bio link?","3-6% average, 8-12% for top performers. Factors include engagement, link placement, and CTA clarity."],
     ["How to improve link-in-bio clicks?","Clear CTA, update link frequently, use Linktree/Beacons for multiple destinations, track which posts drive clicks."],
     ["What tools track bio link CTR?","Linktree, Beacons, Campsite, Bitly with UTM parameters, and native platform analytics."],
     ["Does link placement affect CTR?","Yes. Links at the top of the bio get more clicks. Single clear link outperforms multiple links. Emojis draw attention."],
     ["Good CTR for e-commerce?","4-8% due to purchase intent. Limited-time offers can push above 10%. Below 2% suggests mismatched audience."]]
)

add("bmi-calculator-index", "BMI Calculator",
    "Body Mass Index (BMI) = weight (kg) / height (m)\u00b2. A 30-year-old woman at 165 cm weighing 68 kg has a BMI of 25.0 - at the upper edge of the normal range. BMI is used by WHO as a population-level health screening tool.",
    "While BMI is a useful screening measure, it does not directly measure body fat or account for muscle mass. An athlete with high muscle mass may have a BMI in the overweight range while having very low body fat. This calculator uses the standard Quetelet formula.",
    "Understanding Your BMI Score Using WHO Classifications",
    "A 175 cm man weighing 78 kg has a BMI of 25.5, which is classified as overweight. According to WHO data, individuals with a BMI over 25 have a 20-30% increased risk of cardiovascular disease compared with those in the normal range. However, waist circumference and body fat percentage provide additional context.",
    ["BMI Range","Classification","Health Risk"],
    [["Below 18.5","Underweight","Increased risk of nutritional deficiencies"],["18.5-24.9","Normal weight","Lowest risk for chronic disease"],["25.0-29.9","Overweight","Moderate risk increase"],["30.0-34.9","Obese Class I","High risk - weight management recommended"],["35.0-39.9","Obese Class II","Very high risk"],["40.0+","Obese Class III","Extremely high risk"]],
    [["What is a healthy BMI range?","18.5-24.9 is considered healthy by WHO. This range is associated with the lowest risk of chronic diseases including heart disease, diabetes, and certain cancers. However, individual health depends on many factors beyond BMI."],
     ["Is BMI accurate for athletes?","BMI can overestimate body fat in athletes because it doesn't distinguish muscle from fat. A muscular athlete may have a BMI over 25 (overweight) while having low body fat. Body fat percentage or waist-to-height ratio may be more useful for athletes."],
     ["What is a healthy BMI for women over 40?","The same WHO classification applies: 18.5-24.9. However, women over 40 naturally experience body composition changes. A study found waist circumference may be a better health risk predictor than BMI for postmenopausal women."],
     ["How is BMI calculated?","BMI = weight in kilograms divided by height in metres squared. For imperial: BMI = (weight in pounds \u00d7 703) / (height in inches)\u00b2. A person weighing 70 kg at 1.75 m: BMI = 70 / (1.75 \u00d7 1.75) = 22.9."],
     ["What should I do if my BMI is over 30?","A BMI over 30 qualifies as obese and is associated with increased health risks. Consult a healthcare provider for a comprehensive assessment. Even 5-10% weight loss can significantly improve health markers like blood pressure and blood sugar."]]
)

add("bmr-calculator-index", "BMR Calculator",
    "Basal Metabolic Rate (BMR) is the number of calories your body burns at complete rest to maintain vital functions like breathing, circulation, and cell production. The Mifflin-St Jeor equation is the current gold standard, replacing the older Harris-Benedict formula.",
    "For men: BMR = (10 \u00d7 weight in kg) + (6.25 \u00d7 height in cm) - (5 \u00d7 age) + 5. For women: BMR = (10 \u00d7 weight in kg) + (6.25 \u00d7 height in cm) - (5 \u00d7 age) - 161. A 30-year-old woman weighing 65 kg at 165 cm has a BMR of approximately 1,392 calories per day.",
    "From BMR to TDEE: Activity Multipliers",
    "Total Daily Energy Expenditure (TDEE) = BMR \u00d7 activity factor. A moderately active woman with a BMR of 1,392 needs about 2,158 calories daily to maintain weight. Runners who weigh more burn more calories at the same pace due to the increased energy required to move more mass.",
    ["Activity Level","Description","Multiplier","Example (BMR 1,400)"],
    [["Sedentary","Little or no exercise","1.2","1,680 cal"],["Lightly active","1-3 days/week","1.375","1,925 cal"],["Moderately active","3-5 days/week","1.55","2,170 cal"],["Very active","6-7 days/week","1.725","2,415 cal"],["Extremely active","Athlete/physical job","1.9","2,660 cal"]],
    [["BMR vs TDEE?","BMR = calories at complete rest (vital functions only). TDEE = BMR + all daily activity, exercise, and digestion. TDEE is what you need to maintain weight. To lose weight, eat below TDEE."],
     ["Does BMR decrease when dieting?","Yes. Significant calorie restriction causes metabolic adaptation. The body lowers BMR to conserve energy. This is why weight loss often slows after initial rapid loss. Strength training helps preserve muscle and BMR during dieting."],
     ["What raises your BMR?","Muscle mass is the biggest controllable factor - each pound of muscle burns ~6-7 calories/day at rest. Other factors: being male (more muscle), younger age, taller height, higher body temperature, and certain medical conditions like hyperthyroidism."],
     ["How accurate is BMR calculation?","The Mifflin-St Jeor equation is accurate within about 10% for 80% of the population. Individual BMR varies due to genetics, muscle mass, and hormonal factors. The best way to find your actual BMR is through indirect calorimetry testing."],
     ["Why is women's BMR lower than men's?","Women typically have lower BMR because they have more body fat and less muscle mass than men of the same weight and height. On average, a woman's BMR is 5-10% lower than a man's. The Mifflin-St Jeor formula accounts for this with the -161 constant."]]
)

add("boat-loan-calculator-index", "Boat Loan Calculator",
    "Boat loans differ from auto loans: longer terms (10-20 years), higher rates (typically 7-12% in 2025), and the boat itself serves as collateral. Beyond the loan payment, boat ownership includes insurance, storage, maintenance, and fuel costs that can add 30-50% to the monthly expense.",
    "A $50,000 boat loan at 8% for 15 years results in a monthly payment of about $478 and total interest of $36,020. The same amount financed over 20 years drops the payment to $418 but increases total interest to $50,360.",
    "Boat Loan Payments at Different Terms",
    "A 10-year loan on the same $50,000 boat costs $607/month but saves $18,000 in interest vs a 20-year loan. The shorter term adds $2,268/year to payments but builds equity much faster.",
    ["Boat Price","7% (10yr)","8% (15yr)","10% (20yr)"],
    [["$20,000","$232","$191","$193"],["$50,000","$581","$478","$483"],["$75,000","$871","$717","$724"],["$100,000","$1,161","$956","$965"],["$150,000","$1,742","$1,433","$1,448"]],
    [["Typical boat loan interest rate?","7-12% in 2025 depending on credit score and loan term. New boats get slightly better rates than used. Credit unions often offer the best boat loan rates, sometimes 1-3% below banks."],
     ["How long can you finance a boat?","Boat loans typically range from 10-20 years. Longer terms are available for more expensive boats. Unlike auto loans, 15-20 year terms are common because boats depreciate slower and have longer usable lives."],
     ["Is it hard to get a boat loan?","Boat loans are generally easier to qualify for than mortgages but harder than auto loans. Lenders typically require a credit score of 660+, a debt-to-income ratio under 43%, and a down payment of 10-20%."],
     ["What credit score for a boat loan?","700+ for the best rates. Scores of 660-699 may still qualify but at higher rates. Below 660, approval becomes difficult unless you have substantial down payment or a co-signer."]]
)

add("body-fat-calculator-index", "Body Fat Calculator",
    "Body fat percentage is a more meaningful health metric than weight alone because it distinguishes fat from muscle. This calculator uses the US Navy circumference method, which requires neck and waist measurements (plus hip for women). Other methods include DEXA scanning (gold standard), calipers, and bioelectrical impedance.",
    "For men: %BF = 86.010 \u00d7 log10(waist - neck) - 70.041 \u00d7 log10(height) + 36.76. For women: %BF = 163.205 \u00d7 log10(waist + hip - neck) - 97.684 \u00d7 log10(height) - 78.387.",
    "Body Fat Percentage Classifications",
    "A man with 15% body fat is in the fitness range and typically has visible abdominal definition. At 25%, the same man would be in the acceptable-to-obese range. The essential fat level for men (2-5%) is the minimum required for survival, while women require 10-13% due to hormone-related fat stores.",
    ["Classification","Men (% Fat)","Women (% Fat)","Appearance"],
    [["Essential fat","2-5%","10-13%","Minimum for survival"],["Athletes","6-13%","14-20%","Visible muscle definition"],["Fitness","14-17%","21-24%","Lean and toned"],["Acceptable","18-24%","25-31%","Normal range"],["Obese","25%+","32%+","Excess body fat"]],
    [["What is a healthy body fat percentage?","For men: 10-20% is generally healthy. For women: 18-28% is generally healthy. Athletes tend to be at the lower end. Above 25% for men and 32% for women is classified as obese and associated with increased health risks."],
     ["How accurate is the tape measurement method?","The US Navy method has a margin of error of about 3-4% compared with DEXA scanning. It is reasonably accurate for tracking changes over time. Consistency in measurement technique is more important than absolute accuracy."],
     ["How do I lower body fat percentage?","Create a moderate calorie deficit (300-500 cal/day), prioritize protein intake (1.6-2.2 g/kg of body weight), incorporate strength training to preserve muscle, and maintain adequate sleep. Aim to lose 0.5-1% of body fat per month for sustainable results."],
     ["Is BMI or body fat percentage more useful?","Body fat percentage is more useful for individuals because it directly measures composition rather than estimating it from weight and height. Two people with the same BMI can have very different body fat levels. BMI is better for population screening."]]
)

add("body-surface-area-calculator-index", "Body Surface Area Calculator",
    "Body Surface Area (BSA) is used in medicine for chemotherapy dosing, burn treatment assessment, and determining cardiac output indices. The Mosteller formula is the most widely used: BSA (m\u00b2) = \u221a(height in cm \u00d7 weight in kg / 3600).",
    "A person who is 170 cm tall and weighs 70 kg has a BSA of approximately 1.82 m\u00b2 using the Mosteller formula. The average adult BSA is about 1.7 m\u00b2 for women and 2.0 m\u00b2 for men. Other formulas include Du Bois (the original), Haycock, and Gehan & George.",
    "BSA Reference Values by Gender",
    "BSA is critical for accurate chemotherapy dosing. A patient with BSA 1.5 m\u00b2 receiving a drug dosed at 100 mg/m\u00b2 gets 150 mg. Underestimating BSA by 10% would underdose by 15 mg, potentially reducing treatment efficacy.",
    ["Parameter","Average Male","Average Female","Formula Used"],
    [["Height (avg)","175 cm","162 cm","Patient-specific"],["Weight (avg)","78 kg","66 kg","Patient-specific"],["BSA (avg)","~1.9 m\u00b2","~1.7 m\u00b2","Mosteller"],["BSA range","1.6-2.3 m\u00b2","1.4-2.0 m\u00b2","Depends on size"]],
    [["What is body surface area used for?","BSA is primarily used to calculate chemotherapy doses, which are often given per m\u00b2 of body surface area rather than per kg of weight. It is also used for determining burn severity (the Rule of Nines), cardiac output indexing, and renal function measurements."],
     ["Which BSA formula is most accurate?","The Mosteller formula is the most commonly used in clinical practice because it is simple and accurate. The Du Bois formula is the historical gold standard but requires a square root calculation. For most adults, the formulas agree within 3-5%."],
     ["How is chemotherapy dose calculated from BSA?","Most chemotherapy drugs are dosed as mg/m\u00b2. If a drug has a standard dose of 100 mg/m\u00b2 and the patient has a BSA of 1.8 m\u00b2, the dose is 180 mg. BSA-based dosing helps standardize drug exposure across patients of different sizes."]]
)

add("body-type-calculator-index", "Body Type Calculator",
    "The somatotype classification system describes three body types: ectomorph (lean and linear), mesomorph (muscular and athletic), and endomorph (rounder with higher body fat). Developed by psychologist William Sheldon in the 1940s, the system remains popular in fitness circles despite limited scientific validation.",
    "Most people are a combination of the three types rather than a pure classification. An ecto-mesomorph, for example, has a naturally athletic frame with a lean build. Understanding your dominant body type can help tailor workout and nutrition strategies.",
    "Body Type Characteristics and Training Approaches",
    "An ectomorph who struggles to gain weight might need 3,000+ calories/day and heavy compound lifts to build muscle. An endomorph may respond better to higher protein, moderate carbs, and regular cardio alongside strength training.",
    ["Body Type","Characteristics","Training Approach","Nutrition Strategy"],
    [["Ectomorph","Lean, narrow shoulders, fast metabolism","Heavy strength training, fewer cardio","Higher calories, more carbs"],["Mesomorph","Athletic, broad shoulders, gains easily","Mixed strength and cardio","Balanced macros"],["Endomorph","Rounder, stores fat easily","Regular cardio + weights","Lower carbs, higher protein"]],
    [["What are the three body types?","Ectomorph: naturally thin, difficulty gaining weight. Mesomorph: athletic build, gains muscle and fat easily. Endomorph: rounder frame, tendency to store fat, gains muscle readily. Most people are a mix of these types."],
     ["How do I know my body type?","Look at your natural physique without extreme dieting or training: your shoulder width, natural leanness, and how easily you gain muscle or fat. Online questionnaires can help classify you but are subjective."],
     ["Does body type affect metabolism?","Ectomorphs typically have faster metabolisms, making weight gain harder. Endomorphs may have slower metabolisms and gain fat more easily. However, lifestyle factors including diet, exercise, and sleep have a larger impact on metabolism than body type alone."],
     ["Can your body type change?","The underlying skeletal structure doesn't change, but your body composition is highly modifiable. An endomorph can become very lean through diet and training. A true ectomorph can build significant muscle. Body type is a starting point, not a destiny."]]
)

add("bond-calculator-index", "Bond Calculator",
    "Bond pricing has an inverse relationship with yield: when market interest rates rise, bond prices fall. A $1,000 bond paying a 5% coupon ($50/year) becomes less attractive if new bonds pay 7%, so its market price drops to approximately $714 to match the yield.",
    "Yield to Maturity (YTM) is the total return anticipated on a bond if held until maturity, including both coupon payments and any capital gain or loss from buying below or above face value. Current yield = annual coupon / current market price.",
    "Bond Prices at Different Market Rates ($1,000 Face Value)",
    "A 5% coupon bond with 10 years to maturity is worth $1,000 when market rates equal its coupon. If rates rise to 6%, the price drops to ~$926. If rates fall to 4%, the price rises to ~$1,081. The longer the maturity, the more sensitive the price to rate changes.",
    ["Coupon Rate","Yield 4%","Yield 6%","Yield 8%"],
    [["4%","$1,000","$739","$591"],["5%","$1,125","$869","$718"],["6%","$1,250","$1,000","$850"],["8%","$1,500","$1,260","$1,000"]],
    [["What is yield to maturity?","YTM is the total return expected on a bond if held to maturity, expressed as an annual rate. It includes all coupon payments and the difference between the purchase price and face value. YTM is the most comprehensive measure of a bond's return."],
     ["Why do bond prices fall when interest rates rise?","Bonds have fixed coupon payments. When market rates rise, existing bonds with lower coupons become less attractive. Their price must drop so their yield matches current market rates. This inverse relationship is fundamental to bond investing."],
     ["Coupon rate vs yield?","Coupon rate is the fixed interest payment (% of face value). Yield is the effective return based on the price paid. A bond bought at a discount has yield > coupon rate. A bond bought at a premium has yield < coupon rate."],
     ["What is bond duration?","Duration measures a bond's sensitivity to interest rate changes. A bond with duration of 5 years means its price changes approximately 5% for every 1% change in interest rates. Longer duration = higher price volatility. Zero-coupon bonds have the highest duration."]]
)

add("boyles-law-calculator-index", "Boyle's Law Calculator",
    "Boyle's Law states that for a fixed amount of gas at constant temperature, pressure and volume are inversely proportional: P\u2081V\u2081 = P\u2082V\u2082. If you double the pressure on a gas, its volume halves, provided temperature remains constant.",
    "Real-world applications include scuba diving (pressure changes with depth affect lung volume), syringes (pulling the plunger increases volume, decreasing pressure to draw fluid), and car engines (compressing the fuel-air mixture in the cylinder). For example, a gas at 1 atm with volume 2 L compressed to 0.5 L has a new pressure of 4 atm.",
    "Pressure Units and Conversions",
    "At sea level, atmospheric pressure is 14.7 psi. A car tire at 32 psi is actually at ~46.7 psi absolute pressure (32 + 14.7). Boyle's Law must use absolute pressure, not gauge pressure, for correct calculations.",
    ["Unit","Symbol","Value vs 1 atm","Common Use"],
    [["Pascal","Pa","101,325 Pa","SI unit"],["Kilopascal","kPa","101.325 kPa","Weather reports"],["Atmosphere","atm","1 atm","Standard reference"],["PSI","psi","14.696 psi","Tire pressure"],["mmHg","mmHg","760 mmHg","Blood pressure / barometer"]],
    [["What is Boyle's Law?","Boyle's Law states that pressure and volume of a gas are inversely proportional at constant temperature: P\u2081V\u2081 = P\u2082V\u2082. If volume doubles, pressure halves. This assumes the gas behaves ideally and temperature stays constant."],
     ["What are the units for pressure?","Common units: Pascal (Pa, SI unit), kilopascal (kPa), atmosphere (atm), PSI (pounds per square inch), mmHg (millimeters of mercury), and bar. 1 atm = 101,325 Pa = 14.696 PSI = 760 mmHg."],
     ["What happens to pressure when volume doubles?","Pressure is halved when volume doubles, assuming constant temperature and fixed gas amount. For example, a gas at 2 atm in a 1 L container expands to 2 L: pressure drops to 1 atm."],
     ["When does Boyle's Law break down?","Boyle's Law assumes ideal gas behavior. Real gases deviate at very high pressures and low temperatures where intermolecular forces become significant. At pressures above 300 atm, corrections using van der Waals equation are needed."]]
)

add("bra-size-calculator-index", "Bra Size Calculator",
    "Bra size combines band size (measured around the ribcage below the bust) and cup size (calculated from the difference between bust and band measurements). The band size is the underbust measurement rounded to the nearest even number. Each inch of difference between bust and band corresponds to one cup size.",
    "US and UK sizing differ: US uses double letters (DD, DDD) beyond D, while UK uses E, F, FF, G. EU sizing uses a different band measurement system. A US 34DD is equivalent to UK 34E and EU 75E. Sister sizes (e.g., 34D = 36C = 32DD) have the same cup volume but different band lengths.",
    "US Bra Size Conversion Reference",
    "A properly fitted bra distributes 80% of breast weight through the band, not the straps. If straps are digging in, the band is likely too loose. The band should be horizontal across the back and snug enough to allow only two fingers under it.",
    ["US Size","Underbust (in)","Bust Difference (in)","Equivalent UK","Equivalent EU"],
    [["32A","28-29","1","32A","70A"],["34B","30-31","2","34B","75B"],["36C","32-33","3","36C","80C"],["38D","34-35","4","38D","85D"],["40DD","36-37","5","40E","90E"]],
    [["How to measure bra size at home?","1. Measure underbust (ribcage, directly under breasts) to get band size. 2. Measure over the fullest part of the bust. 3. Subtract band from bust: each inch = one cup size. Try sister sizes if the fit isn't perfect."],
     ["US vs UK bra sizing?","US sizes use D, DD, DDD, G. UK sizes use D, DD, E, F, FF, G. A US DDD is equivalent to UK E. EU sizes use a different system where band is measured in cm."],
     ["What does the letter mean?","The letter indicates cup size relative to band size. A = 1 inch difference between bust and band, B = 2 inches, C = 3, D = 4, DD/E = 5, DDD/F = 6, etc. Same letter on different band sizes means different volume."],
     ["How often does bra size change?","Bra size can change with weight fluctuations of 5-10 lbs, pregnancy, breastfeeding, menopause, and age-related tissue changes. Most women should be remeasured every 6-12 months or whenever bras feel uncomfortable."]]
)

add("break-even-calculator-index", "Break-Even Calculator",
    "Break-even analysis determines when total revenue equals total costs (profit = 0). The formula is: Break-Even Units = Fixed Costs / (Price per Unit - Variable Cost per Unit). The denominator is the contribution margin - the amount each sale contributes to covering fixed costs.",
    "A business with $50,000 in monthly fixed costs selling a product for $80 with $30 in variable costs has a contribution margin of $50. Break-even = $50,000 / $50 = 1,000 units per month. At $100 per unit, break-even drops to 715 units, showing how pricing directly affects viability.",
    "Break-Even Units at Different Price Points",
    "Reducing fixed costs by 20% (to $40,000) lowers break-even to 800 units at $80 price. A business that can't reduce costs must either increase price or volume to reach profitability faster.",
    ["Selling Price","Variable Cost","Contribution Margin","Break-Even Units"],
    [["$50","$20","$30","1,667"],["$60","$25","$35","1,429"],["$75","$30","$45","1,112"],["$100","$40","$60","834"],["$150","$50","$100","500"]],
    [["What is contribution margin?","Contribution margin = selling price - variable costs per unit. It represents how much each sale contributes toward fixed costs and profit. A higher contribution margin means fewer sales needed to break even."],
     ["Why is break-even analysis important?","It tells you the minimum sales volume needed to avoid losses, helps set pricing strategy, and evaluates the impact of cost changes. It's essential for business planning, loan applications, and investor pitches."],
     ["Fixed vs variable costs?","Fixed costs don't change with sales volume (rent, salaries, insurance). Variable costs scale with production (materials, packaging, shipping). The split between them affects how quickly profit grows beyond break-even."],
     ["What happens to break-even if I raise my price?","Higher price increases contribution margin (if variable costs stay the same), which lowers the number of units needed to break even. However, higher prices may reduce customer demand, so price elasticity must be considered."]]
)

add("brick-calculator-index", "Brick Calculator",
    "Calculates the number of bricks needed for a wall based on wall area, brick size, mortar joint thickness, and waste factor. Standard UK bricks measure 215 \u00d7 102.5 \u00d7 65 mm with a 10 mm mortar joint, yielding approximately 60 bricks per square metre.",
    "A 10-metre long wall at 3 metres high (30 m\u00b2) using standard UK bricks needs 30 \u00d7 60 = 1,800 bricks. Adding the standard 10% waste factor brings the total to approximately 1,980 bricks. The number varies significantly with brick size and joint thickness.",
    "Bricks Needed per Square Metre by Brick Type",
    "For a 50 m\u00b2 garden wall using UK standard bricks at 60 per m\u00b2: 3,000 bricks plus 10% waste = 3,300 total. At $0.70 per brick, material cost is $2,310. Adding mortar, labor, and foundation costs typically doubles the total project cost.",
    ["Brick Type","Size (mm)","Bricks per m\u00b2 (10mm joint)","Typical Use"],
    [["UK standard","215\u00d7102.5\u00d765","60","General construction"],["US modular","194\u00d792\u00d757","~68","Standard US walls"],["Metric","200\u00d7100\u00d750","~67","European projects"],["Engineer","215\u00d7102.5\u00d780","~60","Load-bearing walls"]],
    [["How many bricks per square metre?","Standard UK bricks (215\u00d7102.5\u00d765 mm) with 10 mm mortar joint: approximately 60 bricks per m\u00b2. US modular bricks: approximately 68 per m\u00b2. Always check your specific brick dimensions."],
     ["What is the standard waste factor?","10% is standard for simple walls. More complex designs with corners, arches, or cut bricks need 15-20%. Always order extra because matching brick batches later can be difficult."],
     ["How much mortar per brick?","Approximately 0.5-0.7 kg of mortar mix per standard brick. For 1,000 bricks, you need about 500-700 kg of mortar. This depends on joint thickness and brick porosity."],
     ["What size are standard bricks?","UK standard: 215\u00d7102.5\u00d765 mm. US modular: 194\u00d792\u00d757 mm. Metric: 200\u00d7100\u00d750 mm. Always verify dimensions as regional standards differ significantly."]]
)

add("btu-calculator-index", "BTU Calculator",
    "BTU (British Thermal Unit) measures thermal energy. One BTU is the energy needed to raise one pound of water by 1\u00b0F. For air conditioning, the rule of thumb is 20 BTU per square foot of living space. A 500 sq ft room typically needs about 10,000 BTU.",
    "Factors that increase BTU requirements: ceiling height above 8 ft, south- or west-facing windows, poor insulation, and rooms with high occupancy or heat-generating appliances. A kitchen with an oven and refrigerator needs approximately 30% more BTU than the base calculation.",
    "BTU Requirements by Room Size",
    "A 400 sq ft living room with standard 8 ft ceilings needs ~8,000 BTU. Adding two extra people adds 10% (~8,800 BTU). South-facing windows add another 10% (~9,600 BTU). A 12,000 BTU window unit would adequately cover all these factors.",
    ["Room Size (sq ft)","Minimum BTU","Recommended BTU","Window Unit Size"],
    [["100-200","4,000","5,000-6,000","Small"],["200-400","6,000","7,000-9,000","Medium"],["400-700","9,000","10,000-14,000","Large"],["700-1,000","14,000","15,000-18,000","Extra Large"],["1,000-1,400","18,000","20,000-24,000","Mini Split"]],
    [["How many BTU do I need?","Start with 20 BTU per sq ft. For a 300 sq ft room: 6,000 BTU minimum. Add 10% for sunny rooms, 20% for kitchens, and 5% for each person beyond two. Subtract 10% for shaded rooms."],
     ["What is a BTU?","British Thermal Unit = energy to raise 1 lb of water by 1\u00b0F. In HVAC, BTU/hour measures cooling or heating capacity. 12,000 BTU/hour = 1 ton of air conditioning (standard unit of AC capacity)."],
     ["Does ceiling height affect BTU?","Yes. Standard BTU calculations assume 8 ft ceilings. For 9 ft ceilings, increase BTU by 10%. For 10 ft ceilings, increase by 20%. Higher ceilings mean more total volume to cool."],
     ["Does sunlight exposure affect BTU?","Yes. South- and west-facing rooms receive more direct sunlight and need 10-15% more BTU. North-facing rooms can use the base calculation. Proper curtains and blinds reduce the solar heat gain."]]
)

add("budget-calculator-index", "Budget Calculator",
    "The 50/30/20 rule allocates 50% of after-tax income to needs (housing, food, utilities, minimum debt payments), 30% to wants (dining out, entertainment, travel), and 20% to savings and debt repayment (above minimum payments). This provides a simple framework for financial balance.",
    "For someone earning $4,500/month after tax: $2,250 for needs, $1,350 for wants, and $900 for savings/debt. The actual dollar amounts depend on cost of living. In high-cost cities, housing alone may exceed 50%, requiring adjustment to the other categories.",
    "50/30/20 Budget Breakdown by Income Level",
    "At $3,000/month income, the 20% savings target ($600) plus an average 6% 401k match means total savings rate reaches 26%. At $8,000/month, $1,600 in savings plus maxing a Roth IRA ($583/month) leaves $1,017/month for additional investing or debt payoff.",
    ["Monthly Income (after tax)","Needs (50%)","Wants (30%)","Savings/Debt (20%)"],
    [["$3,000","$1,500","$900","$600"],["$4,500","$2,250","$1,350","$900"],["$6,000","$3,000","$1,800","$1,200"],["$8,000","$4,000","$2,400","$1,600"]],
    [["What is the 50/30/20 rule?","50% of after-tax income for needs (rent, groceries, utilities, minimum debt payments), 30% for wants (dining, travel, hobbies), and 20% for savings and extra debt payments. Created by Senator Elizabeth Warren in her book All Your Worth."],
     ["How do I stick to a budget?","Track every expense for 30 days first, then set realistic category limits. Use the envelope system or budgeting apps. Automate savings transfers on payday. Review monthly and adjust as needed."],
     ["Should I budget by paycheck or month?","Monthly works best for consistent income. If income varies (freelancers), budget based on your lowest-earning month and treat extra income as savings or debt payments. Bi-weekly budgeting works if paid every two weeks."],
     ["What is zero-based budgeting?","Every dollar of income is assigned a purpose (income - expenses = 0). It forces intentional spending across all categories. Works well for detail-oriented people but requires ongoing tracking."]]
)

add("buffer-calculator-index", "Buffer Calculator",
    "A chemical buffer resists pH change when small amounts of acid or base are added. The Henderson-Hasselbalch equation describes buffer behavior: pH = pKa + log([A\u207b]/[HA]), where [A\u207b] is conjugate base concentration and [HA] is weak acid concentration.",
    "Buffers work most effectively at pH values within \u00b11 of the acid's pKa. When [A\u207b] = [HA], the pH equals the pKa and the buffer has maximum capacity. The blood's bicarbonate buffer system maintains pH between 7.35 and 7.45 using carbonic acid (pKa = 6.1) and bicarbonate.",
    "Common Laboratory Buffer Systems",
    "A 0.1 M acetic acid/sodium acetate buffer at pH 4.76 has equal concentrations of acid and conjugate base. Adding 0.01 M HCl shifts the pH by only ~0.09 units. The same HCl addition to pure water would shift pH by 5 units, demonstrating the buffer's effectiveness.",
    ["Buffer System","Conjugate Acid","pKa","Effective pH Range"],
    [["Acetic acid/acetate","CH\u2083COOH","4.76","3.8-5.8"],["Phosphate (pKa2)","H\u2082PO\u2084\u207b","7.21","6.2-8.2"],["Bicarbonate","H\u2082CO\u2083","6.35","5.4-7.4"],["Ammonia/ammonium","NH\u2084\u207a","9.25","8.3-10.3"],["HEPES","HEPES","7.55","6.6-8.6"]],
    [["What is a buffer solution?","A buffer resists pH change by neutralizing added acids or bases. It contains a weak acid and its conjugate base (or weak base and its conjugate acid). Buffers are essential in biological systems to maintain stable pH."],
     ["What is the Henderson-Hasselbalch equation?","pH = pKa + log([A\u207b]/[HA]). It relates the pH of a buffer to its pKa and the ratio of conjugate base to weak acid. When the ratio is 1:1, pH = pKa. The equation is derived from the acid dissociation constant."],
     ["What is pKa?","pKa = -log(Ka), where Ka is the acid dissociation constant. It represents the pH at which half the acid is dissociated. A lower pKa means a stronger acid. For buffer selection, choose an acid with pKa close to the desired pH."],
     ["Why are buffers used in biochemistry?","Enzymatic reactions are highly pH-sensitive. Most cellular enzymes have optimal activity within a narrow pH range (often pH 6-8). Biological buffers like phosphate, bicarbonate, and HEPES maintain this range despite metabolic processes that produce acids or bases."]]
)

add("business-loan-calculator-index", "Business Loan Calculator",
    "Business loans differ from personal loans: they often require collateral, proof of business revenue, and a detailed business plan. SBA loans, term loans, lines of credit, and equipment financing are common types. Rates typically range from 6-30% depending on the lender, loan type, and business creditworthiness.",
    "Lenders evaluate business loans based on the Five Cs: Character (credit history), Capacity (debt-to-income ratio), Capital (owner investment), Collateral (assets pledged), and Conditions (use of funds, industry risk). A well-prepared business plan with financial projections significantly improves approval odds.",
    "Business Loan Types and Typical Terms",
    "A well-qualified borrower might get an SBA 7(a) loan at 9% for 15 years. Monthly payment on $200,000 is ~$2,028 with total interest of ~$165,000. The same amount from an online lender at 20% over 5 years would cost $5,299/month but total interest of ~$117,940.",
    ["Business Loan Type","Typical Rate (2025)","Term","Best For"],
    [["SBA 7(a)","8-13%","10-25 years","Small businesses, startups"],["Term loan","7-30%","1-10 years","Established businesses"],["Line of credit","7-25%","Revolving","Working capital, inventory"],["Equipment financing","6-20%","3-10 years","Purchasing equipment"]],
    [["Average business loan interest rate?","6-13% for well-qualified borrowers from banks, 10-30% for online lenders and those with weaker credit. SBA loans typically offer the lowest rates but have the longest approval process."],
     ["What credit score for a business loan?","Banks typically require 680+ personal credit score. SBA loans may accept 640+. Online lenders may accept 580+ but at significantly higher rates. Business credit history also matters for larger loans."],
     ["What is an SBA loan?","An SBA loan is partially guaranteed by the U.S. Small Business Administration, reducing lender risk. The SBA 7(a) program offers loans up to $5 million for working capital, equipment, real estate, and refinancing. Rates are capped by the SBA."],
     ["How much can I borrow for my business?","Depends on revenue, time in business, and creditworthiness. Banks typically lend 2-4 times annual cash flow. SBA loans can go up to $5 million. Online lenders offer smaller amounts ($5,000-$500,000) with faster approval."]]
)

add("caffeine-calculator-index", "Caffeine Calculator",
    "Caffeine has a half-life of 5-7 hours in the average adult, meaning half the caffeine consumed is still active in your system after that time. The FDA considers 400 mg per day (about 4 cups of coffee) safe for most healthy adults. Pregnant women should limit intake to 200 mg daily.",
    "A 3 PM coffee containing 200 mg of caffeine means approximately 100 mg remains in your system at 8-10 PM, which can significantly disrupt sleep quality even if you can fall asleep. Caffeine blocks adenosine receptors, preventing the chemical that signals tiredness.",
    "Caffeine Content of Common Sources",
    "A 300 lb person drinking a 200 mg coffee at 7 AM has about 25 mg remaining by 7 PM after 12 hours (two half-lives). The same coffee at 3 PM leaves ~100 mg at 9 PM, explaining why afternoon caffeine affects sleep more than morning caffeine.",
    ["Source","Serving","Caffeine Content","Notes"],
    [["Brewed coffee","8 oz (240 ml)","95-165 mg","Drip coffee on the higher end"],["Espresso","1 oz (30 ml)","47-64 mg","Single shot"],["Black tea","8 oz (240 ml)","25-48 mg","Steeping time affects strength"],["Energy drink","8.4 oz (250 ml)","80 mg","Varies by brand"],["Dark chocolate","1 oz (28 g)","12-24 mg","Higher cocoa = more caffeine"],["Soda (Coca-Cola)","12 oz (355 ml)","34 mg","Lower than coffee or tea"]],
    [["How much caffeine is safe per day?","The FDA recommends up to 400 mg/day for healthy adults, equivalent to about 4 cups of brewed coffee. Pregnant women: limit to 200 mg/day. Individuals with anxiety, heart conditions, or sleep disorders may need less."],
     ["How long does caffeine stay in your system?","Caffeine half-life is 5-7 hours. After 5-7 hours, half the caffeine is still active. It takes about 24-30 hours for complete elimination. A 200 mg morning coffee leaves about 50 mg in your system at bedtime."],
     ["Does caffeine tolerance develop?","Yes. Regular use leads to tolerance: the same amount produces less effect over time. Tolerance begins developing after 3-7 days of regular use. A tolerance break of 1-2 weeks typically resets sensitivity."],
     ["What are caffeine withdrawal symptoms?","Headaches, fatigue, irritability, brain fog, and muscle pain. Symptoms begin 12-24 hours after stopping, peak at 24-48 hours, and can last 2-9 days. Gradual reduction minimizes withdrawal."]]
)

add("calorie-calculator-index", "Calorie Calculator",
    "This calculator estimates Total Daily Energy Expenditure (TDEE) using the Mifflin-St Jeor equation, the most accurate formula for the general population. TDEE = BMR \u00d7 activity multiplier. For a 28-year-old woman weighing 65 kg at 168 cm with moderate activity (3-5 days/week): BMR = 1,392, TDEE = 1,392 \u00d7 1.55 = 2,158 calories per day.",
    "To lose 1 lb per week (3,500 calorie deficit), subtract 500 calories from TDEE: this woman would eat ~1,658 calories/day. To gain muscle, she would add 300-500 calories. A lb of body fat represents approximately 3,500 calories, though individual results vary.",
    "Calorie Adjustments for Common Goals",
    "A male with TDEE of 2,800 wanting to gain muscle at 0.5 lb/week adds 250 cal/day (2,800 to 3,050). Over 12 weeks, this surplus of 21,000 calories yields about 6 lbs gained (assuming ~50% muscle, ~50% fat) with proper strength training.",
    ["Goal","Calorie Adjustment","Example: TDEE 2,200","Expected Rate"],
    [["Lose 2 lbs/week","-1,000 cal/day","1,200 cal/day","Aggressive (not for everyone)"],["Lose 1 lb/week","-500 cal/day","1,700 cal/day","Sustainable"],["Maintain weight","TDEE","2,200 cal/day","Stable weight"],["Gain muscle","+300-500 cal/day","2,500-2,700 cal/day","~0.5-1 lb/week"]],
    [["How many calories should a woman eat?","Depends on age, height, weight, and activity. Average: 1,800-2,400 for maintenance. Women aged 31-50: 1,800-2,200 if sedentary, 2,000-2,400 if active. Minimum without medical supervision: 1,200 cal/day."],
     ["How many calories to lose 10 pounds?","A 3,500 calorie deficit per pound means a total deficit of 35,000 calories. At a 500 cal/day deficit, this takes about 10 weeks. At 1,000 cal/day, about 5 weeks. Sustainable loss is 1-2 lbs per week."],
     ["Is 1,200 calories enough?","1,200 calories is the minimum for most women without medical supervision. Very few people should go below this. Active women, tall women, and most men need significantly more. Chronic undereating causes metabolic adaptation and nutrient deficiencies."],
     ["Should I eat back exercise calories?","Most calorie estimates already include activity multipliers. Adding back 100-200 calories for intense workouts is reasonable. Adding back full calorie burn estimates is not recommended because fitness trackers overestimate burn by 20-40%."]]
)

add("calorie-deficit-calculator-index", "Calorie Deficit Calculator",
    "A calorie deficit occurs when you consume fewer calories than your body burns. The 3,500 calorie rule suggests that a cumulative deficit of 3,500 calories equals about 1 lb of fat loss. A safe deficit is 500-1,000 calories per day for most people, resulting in 1-2 lbs of weight loss per week.",
    "Minimum intake floors: at least 1,200 calories/day for women and 1,500 for men unless under medical supervision. A person with a TDEE of 2,500 who eats 2,000 calories creates a 500-calorie deficit, losing about 1 lb per week. A 1,000-calorie deficit doubles the rate but may not be sustainable.",
    "Weekly Fat Loss at Different Deficit Levels",
    "At a 500-calorie deficit, a person with TDEE 2,500 eating 2,000 calories loses ~1 lb/week. Over 12 weeks, that's 12 lbs lost. At 750-calorie deficit, ~18 lbs over 12 weeks. However, metabolic adaptation reduces actual loss by 10-15% over longer periods.",
    ["Daily Deficit","Weekly Loss (lbs)","Weekly Loss (kg)","Sustainability"],
    [["250 cal","0.5 lbs","0.23 kg","Very sustainable"],["500 cal","1 lb","0.45 kg","Sustainable"],["750 cal","1.5 lbs","0.68 kg","Moderate difficulty"],["1,000 cal","2 lbs","0.91 kg","Challenging"]],
    [["What is a safe calorie deficit?","500-1,000 calories below TDEE is generally safe. Below that risks metabolic adaptation, muscle loss, and nutrient deficiencies. Never go below 1,200 (women) or 1,500 (men) without medical supervision."],
     ["How many pounds can I lose per month?","Safe loss is 4-8 lbs per month (1-2 lbs/week). More aggressive loss is possible initially due to water weight but is not sustainable. Loss beyond 10 lbs/month often includes significant muscle loss."],
     ["Does deficit need to be the same every day?","No. A weekly deficit works the same as daily. You can eat at maintenance on weekends and create larger deficits on weekdays. The total weekly deficit is what drives fat loss, not day-to-day consistency."],
     ["Will I lose muscle in a deficit?","Some muscle loss is inevitable, but it can be minimized by: eating adequate protein (1.6-2.2 g/kg body weight), continuing strength training, keeping the deficit moderate (500 cal, not 1,000+), and avoiding crash diets."]]
)

add("calories-burned-calculator-index", "Calories Burned Calculator",
    "Calories burned during exercise are estimated using MET (Metabolic Equivalent of Task) values. One MET equals resting metabolic rate. The formula: Calories = MET \u00d7 weight (kg) \u00d7 time (hours). A 70 kg person running at 6 mph (MET: 9.8) for 30 minutes burns 9.8 \u00d7 70 \u00d7 0.5 = 343 calories.",
    "Body weight significantly affects calorie burn: a 90 kg person running the same pace burns 441 calories versus 294 for a 60 kg person. Exercise calorie estimates have about a 15-20% margin of error because individual factors like muscle mass, fitness level, and efficiency affect actual burn.",
    "Calories Burned per Hour by Body Weight",
    "A 70 kg person walking briskly burns ~266 cal/hr. At 85 kg, the same walk burns ~323 cal/hr - 21% more. This is why heavier individuals often lose weight faster initially with the same exercise routine.",
    ["Exercise","MET Value","Cal/hr (70kg)","Cal/hr (85kg)"],
    [["Running 6 mph","9.8","686","833"],["Cycling moderate","8.0","560","680"],["Swimming laps","7.0","490","595"],["Weight lifting","5.0","350","425"],["Walking brisk","3.8","266","323"],["Yoga (Hatha)","2.5","175","213"]],
    [["How accurate are calorie burn calculators?","They have a 15-20% margin of error because MET values are population averages, not individual measurements. Actual burn varies with fitness level, muscle mass, body composition, and exercise efficiency. Use estimates as a starting point, not precise numbers."],
     ["What exercise burns the most calories?","Running (especially at faster paces) burns the most calories per hour. Swimming, cycling, rowing, and HIIT are also high burn activities. The best exercise is one you enjoy and will do consistently."],
     ["Does weight affect calories burned?","Yes, significantly. Heavier people burn more calories for the same activity because moving more mass requires more energy. A 90 kg person burns about 40% more calories than a 60 kg person during the same exercise."],
     ["Does strength training burn calories?","Strength training burns moderate calories during the session (~200-350 cal/hr) but increases post-exercise oxygen consumption (EPOC), keeping metabolism elevated for 24-48 hours after the workout. Muscle gained also increases resting BMR."]]
)

add("canadian-mortgage-calculator-index", "Canadian Mortgage Calculator",
    "Canadian mortgages differ from US mortgages in several ways: interest is compounded semi-annually (not monthly), the maximum standard amortization is 25 years (reduced from 30 years for insured mortgages as of 2024), and CMHC insurance is required for down payments under 20%. The stress test requires qualification at 2 percentage points above the contract rate or 5.25%, whichever is higher.",
    "A $500,000 mortgage at 5.5% over 25 years with 5% down ($25,000) requires CMHC insurance (4% of loan amount for 5% down = $19,000 added to the mortgage). The effective mortgage becomes $494,000, with a monthly payment of approximately $2,984. The same mortgage with 20% down avoids CMHC insurance entirely.",
    "CMHC Insurance Premiums by Down Payment",
    "The stress test means a borrower at 5.5% contract rate must qualify at 7.5%. A household needs ~$120,000 annual income to qualify for a $500,000 mortgage at 7.5% over 25 years. At 5.5%, the income requirement drops to ~$95,000.",
    ["Down Payment","CMHC Premium Rate","Premium on $500K","Monthly (5.5%, 25yr)"],
    [["5%","4.00%","$19,000","$2,984"],["10%","3.10%","$13,950","$2,905"],["15%","2.80%","$11,900","$2,889"],["20%+","0%","$0","$2,839"]],
    [["How is Canadian mortgage interest calculated differently?","Canadian mortgages compound semi-annually (every 6 months) rather than monthly. This means the effective annual rate is slightly higher than the stated rate. A 5.5% stated rate with semi-annual compounding has an effective annual rate of about 5.57%."],
     ["What is CMHC mortgage insurance?","CMHC (Canada Mortgage and Housing Corporation) insurance protects the lender if you default. It is required when your down payment is less than 20% of the purchase price. The premium is added to your mortgage balance, ranging from 2.8-4.0% of the loan amount."],
     ["What is the stress test rate in Canada?","You must qualify at the greater of 2% above your contract rate or 5.25%. If your contract rate is 5.5%, you must qualify at 7.5%. This means your income must support payments at 7.5%, not 5.5%, to get approved."],
     ["What is the maximum amortization period in Canada?","As of 2024, the maximum amortization for insured mortgages (under 20% down) is 25 years. Uninsured mortgages (20%+ down) can go up to 30 years. Shorter amortization means higher payments but significantly less total interest."]]
)

add("capacitance-calculator-index", "Capacitance Calculator",
    "Capacitance measures a component's ability to store electrical charge, measured in farads (F). Practical capacitors use microfarads (\u00b5F = 10\u207b\u2076 F), nanofarads (nF = 10\u207b\u2079 F), and picofarads (pF = 10\u207b\u00b9\u00b2 F). A 10 \u00b5F capacitor stores 10 millionths of a farad.",
    "Capacitors in series: 1/C_total = 1/C\u2081 + 1/C\u2082 + ... (total is less than any individual). Capacitors in parallel: C_total = C\u2081 + C\u2082 + ... (total is the sum). Two 10 \u00b5F capacitors in series give 5 \u00b5F total; in parallel they give 20 \u00b5F.",
    "Capacitance Units and Conversions",
    "A 47 \u00b5F capacitor with 10 V across it stores 0.00235 joules of energy (E = \u00bdCV\u00b2). Supercapacitors used in regenerative braking can store 3,000 F at 2.7 V, holding 10,935 J - equivalent to a 10 kg weight dropped from 111 meters.",
    ["Unit","Symbol","Value in Farads","Common Use"],
    [["Farad","F","1 F","Large supercapacitors"],["Millifarad","mF","10\u207b\u00b3 F","Rarely used"],["Microfarad","\u00b5F","10\u207b\u2076 F","Power supply filters"],["Nanofarad","nF","10\u207b\u2079 F","Timing circuits"],["Picofarad","pF","10\u207b\u00b9\u00b2 F","RF and tuning circuits"]],
    [["What is capacitance?","Capacitance is the ability to store electrical charge, measured in farads (F). A capacitor consists of two conductive plates separated by an insulator (dielectric). When voltage is applied, charge accumulates on the plates, storing energy in the electric field."],
     ["How do you add capacitors in parallel vs series?","Parallel: C_total = C\u2081 + C\u2082 + ... (like adding resistors in series). Series: 1/C_total = 1/C\u2081 + 1/C\u2082 + ... (like adding resistors in parallel). The formulas are reversed compared with resistors."],
     ["What is a Farad?","One farad stores one coulomb of charge at one volt. It is a very large unit: a typical electronics capacitor is 0.000001 F (1 \u00b5F). Supercapacitors can reach thousands of farads for energy storage applications."],
     ["What are typical capacitor values?","Common values: 0.1 \u00b5F (decoupling), 10 \u00b5F (power supply), 100 \u00b5F (audio), 1000 \u00b5F (power filtering), 1 nF (timing), 10 pF (RF circuits). Ceramic, electrolytic, and film capacitors have different characteristics for different applications."]]
)

add("carbohydrate-calculator-index", "Carbohydrate Calculator",
    "The USDA recommends that 45-65% of total daily calories come from carbohydrates for most adults. Carbohydrates provide 4 calories per gram. For a 2,000-calorie diet at 50% carbs, that's 1,000 calories from carbs, or 250 grams per day. Simple carbs (sugars) digest quickly; complex carbs (starches, fiber) digest slowly, providing sustained energy.",
    "A 150-pound moderately active person aiming for 2,200 calories per day would target approximately 248-358 grams of carbs per day. Low-carb diets (under 100 g/day) are sometimes used for weight loss or blood sugar control, while ketogenic diets restrict carbs to under 50 g/day.",
    "Daily Carb Recommendations by Calorie Target",
    "A large apple has ~25 g of carbs, a slice of whole wheat bread has ~12 g, and a cup of cooked brown rice has ~45 g. For someone on a 2,000-calorie diet at 55% carbs (275 g/day), these add up quickly: an apple, two slices of toast, and a cup of rice uses ~94 of the 275 g allowance.",
    ["Calorie Target","45% Carbs (g)","55% Carbs (g)","65% Carbs (g)"],
    [["1,500 cal","169 g","206 g","244 g"],["2,000 cal","225 g","275 g","325 g"],["2,500 cal","281 g","344 g","406 g"],["3,000 cal","338 g","413 g","488 g"]],
    [["How many grams of carbs per day?","For most adults: 225-325 grams based on a 2,000-calorie diet (45-65% of calories). Athletes need more (up to 400-500 g). Low carb: under 100 g. Ketogenic: under 50 g. Minimum for brain function: ~130 g/day."],
     ["What percentage should come from carbs?","The USDA recommends 45-65% of total calories from carbohydrates. Low-carb diets use 20-30%. Athletes may need 65-75%. The optimal percentage depends on activity level, metabolic health, and personal preference."],
     ["Simple vs complex carbohydrates?","Simple carbs (sugar, white bread, soda) are quickly digested, causing rapid blood sugar spikes. Complex carbs (whole grains, legumes, vegetables) digest slowly, providing steady energy and more nutrients. Fiber is a complex carb that isn't digested but aids digestive health."],
     ["How do carbs affect blood sugar?","Carbs break down into glucose, raising blood sugar. Complex carbs with fiber and protein cause a gradual rise. Simple carbs cause rapid spikes followed by crashes. The glycemic index (GI) ranks foods by how quickly they raise blood sugar."]]
)

add("cash-back-vs-low-interest-calculator-index", "Cash Back vs Low Interest Calculator",
    "When financing a car, dealers often offer a choice between cash back and a lower APR. The correct decision depends on the loan amount, term, and how the savings are compared. A $30,000 car with $1,500 cash back at 7% APR over 60 months has a $595 monthly payment, while $0 cash back at 4.9% has a $565 monthly payment.",
    "The lower APR saves $30/month ($1,800 over 60 months), which is more than the $1,500 cash back. However, if the same deal is compared over 72 months ($516 vs $481/month), the low APR saves $2,520, further widening the gap. If you plan to pay off the loan early, cash back may be better because APR savings accumulate over time.",
    "Cash Back vs Low APR on a $30,000 Loan",
    "The break-even point depends on how long you keep the loan. On a $30,000 loan, $1,500 cash back vs 4.9% APR (reduced from 7%): the interest savings overtake the cash back after ~35 months. If you plan to keep the loan longer, choose low APR. If shorter, take the cash back.",
    ["Scenario","Monthly (60mo)","Total Interest","Savings vs 7%"],
    [["$1,500 cash back at 7%","$595","$5,700","$1,500 cash"],["$0 cash back at 4.9%","$565","$3,900","$1,800 interest"],["$500 cash back at 5.5%","$575","$4,500","$1,500 cash+interest"]],
    [["When is cash back better than low APR?","Cash back is better when: 1) the loan term is short (24-36 months), 2) you plan to pay off early, 3) the cash back amount is large relative to the potential interest savings (above 6% on the balance), or 4) you need the cash for other purposes."],
     ["How do I calculate which deal is better?","Calculate total interest saved with the lower APR and compare to the cash back amount. Also calculate the monthly payment difference and multiply by expected loan term. Choose whichever is higher. Online calculators make this comparison simple."],
     ["Does loan term affect cash-back value?","Yes, significantly. On a 72-month loan, small APR differences compound over time, making low APR more valuable. On a 24-36 month loan, the interest savings are smaller, making cash back relatively more attractive."],
     ["What if I plan to pay off early?","Cash back is almost always better if you plan to pay off in 1-2 years because the APR savings haven't accumulated enough to match the immediate cash benefit. Check for prepayment penalties before choosing either option."]]
)

add("cd-calculator-index", "CD Calculator",
    "A Certificate of Deposit (CD) is a time deposit that pays a fixed interest rate for a specified term, typically 3 months to 5 years. Early withdrawal usually incurs a penalty of 3-6 months of interest. For a $10,000 12-month CD at 5% APY, the total interest earned is $500.",
    "CD laddering involves splitting money across multiple CDs with different maturity dates. For example, $20,000 divided into 3-month, 6-month, 9-month, and 12-month CDs provides regular access to funds while maintaining higher yields than a savings account. As each CD matures, it can be reinvested in a new long-term CD.",
    "CD Interest Earnings by Amount and Rate",
    "A $25,000 CD at 5% APY over 3 years earns $3,941 in compound interest, compared with $3,750 earned at a simple rate. The $191 difference from compounding shows why APY (which includes compounding) is the correct rate to compare, not APR.",
    ["Amount","4.5% APY (1yr)","5% APY (1yr)","5.5% APY (1yr)","5% APY (3yr)"],
    [["$5,000","$225","$250","$275","$788"],["$10,000","$450","$500","$550","$1,576"],["$25,000","$1,125","$1,250","$1,375","$3,941"],["$50,000","$2,250","$2,500","$2,750","$7,882"]],
    [["What is a CD?","A Certificate of Deposit is a savings account that holds a fixed amount of money for a fixed period (term) in exchange for a guaranteed interest rate. CDs typically offer higher rates than regular savings accounts because your money is locked in for the term."],
     ["What is CD laddering?","CD laddering is dividing your money across multiple CDs with staggered maturity dates. A 5-rung ladder might have CDs maturing every 3 months. This provides regular access to some funds, takes advantage of longer-term rates, and reduces reinvestment risk."],
     ["What happens if I withdraw early?","Early withdrawal penalties typically equal 3-6 months of interest for terms under 2 years, and 6-12 months for longer terms. Some no-penalty CDs allow early withdrawal without penalty but usually offer lower rates."],
     ["Are CDs FDIC insured?","Yes, CDs from FDIC-member banks are insured up to $250,000 per depositor, per institution. This makes CDs one of the safest investments available, though the real return after inflation may be minimal."]]
)

add("cement-calculator-index", "Cement Calculator",
    "This calculator estimates the amount of concrete or cement needed for slabs and structures. Concrete volume = length \u00d7 width \u00d7 depth. A 4m \u00d7 3m \u00d7 0.1m slab has a volume of 1.2 cubic metres. Standard concrete weighs approximately 2.4 tonnes per cubic metre.",
    "Using a common 1:2:4 mix ratio (cement:sand:aggregate), 1.2 cubic metres of concrete requires approximately 300 kg of cement (12 bags at 25 kg each), 600 kg of sand, and 1,200 kg of aggregate. A 1:1.5:3 mix (stronger) would need more cement: about 380 kg (15 bags).",
    "Cement Requirements for Common Mix Ratios (per m\u00b3)",
    "For a 10m \u00d7 4m driveway at 150mm depth (6 m\u00b3 concrete) using a 1:2:4 mix: 1,500 kg cement (60 bags), 3,000 kg sand, 6,000 kg aggregate. At $12 per 25 kg bag of cement: ~$720 just for the cement. Ordering ready-mix concrete may be more economical for large volumes.",
    ["Mix Ratio","Cement (per m\u00b3)","Sand (per m\u00b3)","Aggregate (per m\u00b3)","Best Use"],
    [["1:2:4 (standard)","250 kg","500 kg","1,000 kg","Paths, floors, general"],["1:1.5:3 (strong)","320 kg","480 kg","960 kg","Foundations, structural"],["1:3:6 (lean)","200 kg","600 kg","1,200 kg","Mass fill, bases"],["1:1:2 (high strength)","400 kg","400 kg","800 kg","Thin sections, heavy loads"]],
    [["How many bags of cement per cubic metre?","For a 1:2:4 mix, approximately 10 bags (25 kg each) of cement per cubic metre. For 1:1.5:3 mix, about 13 bags. Always add 5-10% for waste. Bag sizes: 20 kg, 25 kg, 40 kg, or 50 lb depending on region."],
     ["What is the standard mix for a concrete slab?","A 1:2:4 mix (cement:sand:aggregate) is standard for general concrete slabs. For driveways subject to vehicle loads, use 1:1.5:3. For footings and foundations, use 1:1.5:3 or 1:1:2. Always follow your structural engineer's specification."],
     ["How do I calculate how much concrete I need?","Volume = length (m) \u00d7 width (m) \u00d7 depth (m). A 4m \u00d7 3m \u00d7 0.1m slab = 1.2 m\u00b3. For cylindrical footings: \u03c0r\u00b2h. Add 5-10% for waste and uneven ground. For imperial: length (ft) \u00d7 width (ft) \u00d7 depth (ft) / 27 = cubic yards."],
     ["What is the difference between cement and concrete?","Cement is a binding powder (made from limestone and clay) that hardens when mixed with water. Concrete = cement + sand + aggregate (gravel) + water. Cement is an ingredient of concrete, like flour is an ingredient of bread. There is no 'concrete' without aggregate."]]
)

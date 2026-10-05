---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6aaacb49-e69c-83e8-bf87-4eba67bb32e5"
created: 1789578059.49615
updated: 1789578603.519887
resource_section: true
---

# UPI MDR Impact Analysis

## User

@Firecrawl Use Firecrawl to scrape all the controversies and news and all the opinions that is on X, Instagram, LinkedIn, all the social media about the current news of UPI, Indian UPI, like being charged 0.4% MDR, and like who is being charged, what is the impact, who will be affected, and all the details about it, and like give me the entire retrospective of this situation. How will this affect Indian people and who will be benefited, who will be in loss? How will this be a benefit towards the PhonePe IPO? And like who implemented this, where is this 0.4% MDR value came from, and where is this charges going to? Like who is earning from this MDR charges above 2,000 rupees, over transaction of 2,000 rupees, right?

## Assistant

I’ll separate **what is actually announced/proposed** from viral claims, then trace the 0.4% figure, who pays/receives MDR, consumer impact, merchant/bank/payment-app economics, and the PhonePe IPO angle. I’ll also compare mainstream reporting with X/LinkedIn/other social commentary so rumors don’t get mixed with confirmed policy.

## Assistant

One key point is now confirmed from NPCI itself: this is **not a consumer fee** and it is **not live today**. NPCI’s FAQ dated **15 September 2026** says the new MDR starts **15 October 2026**, applies to eligible merchant UPI payments above ₹2,000, while P2P transfers and consumers remain free. Small P2PM merchants are exempt.

## Assistant

The social reaction is splitting into two clear camps already. Critics argue merchants will quietly recover the cost through prices or cash incentives; payment-industry voices argue zero MDR made a system processing ~24.5 billion monthly transactions commercially unsustainable. More importantly, the official framework **does explicitly include UPI app providers in the revenue pool**, so the PhonePe angle is real—not just social-media speculation.

## Assistant

Worked for 6m 22s

## Assistant

I dug through the current reporting plus Firecrawl’s publicly indexed results from **X, Instagram, LinkedIn, Threads, Reddit and news sites**, and cross-checked the core claims against the Finance Ministry/NPCI framework. One limitation: no scraper can see literally every X/Instagram/LinkedIn post because some content is login-gated, private, deleted or not indexed, so the social-media part below is a broad representative scan rather than a complete archive.

## The bottom line first

The viral statement **“UPI transactions above ₹2,000 will now be charged 0.4%” is misleading.**

From **15 October 2026**:

| Transaction | What happens |
|---|---|
| You send ₹50,000 to a friend/family member | **₹0 fee** |
| Merchant payment ≤ ₹2,000 | **₹0 MDR** |
| Eligible merchant payment > ₹2,000 | Merchant may incur **0.4% MDR** |
| Small QR merchant receiving ≤ ₹1 lakh/month | **Exempt** |
| Railways, telecom, fuel, insurance etc. | Special **₹5 flat MDR** on eligible transactions |
| Capital-market/broker payments | **0.02% MDR**, subject to cap |
| Maximum standard MDR | **₹300 per transaction** |
| Consumer UPI app fee | **Not permitted** |

The Finance Ministry says roughly **96% of merchant UPI transactions remain unaffected**, and **all person-to-person UPI remains free irrespective of amount**. It also explicitly says this MDR is **not a tax collected by the government or NPCI**. citeturn166679search12turn166679search0

That distinction is the most important part of the entire controversy.

---

# 1. So who actually pays the 0.4%?

The **merchant**, technically.

Suppose you buy a ₹10,000 laptop accessory from an eligible merchant and pay through ordinary UPI.

The merchant receives a transaction subject to:

**0.4% × ₹10,000 = ₹40 MDR.**

The merchant is supposed to absorb that ₹40 rather than adding “₹40 UPI charge” to your bill. NPCI has specifically instructed acquiring banks to ensure merchants do not directly pass the MDR onto customers, and UPI apps cannot impose a separate platform fee on consumers. citeturn174689search0

At ₹75,000, 0.4% reaches ₹300. After that, the **₹300 cap** prevents the standard fee from increasing further.

So a ₹1 lakh eligible merchant payment doesn't incur ₹400 MDR; it remains capped at ₹300. citeturn174689search0

---

# 2. Where does your ₹40 actually go?

This is one of the most misunderstood parts.

According to the NPCI revenue-sharing formula reported from its September 15 circular:

| Recipient | Share of MDR | On ₹10,000 payment / ₹40 MDR |
|---|---:|---:|
| **Issuer bank** — customer's bank | **40%** | ₹16 |
| **Merchant acquirer/acquiring bank** | **30%** | ₹12 |
| **UPI app / TPAP** such as PhonePe | **20%** | ₹8 |
| **UPI app's partner bank** | **10%** | ₹4 |

So the **government doesn't receive the ₹40**.

NPCI doesn't simply pocket it either.

It circulates through the companies and banks operating the payment chain. citeturn174689search0turn166679search12

This answers your question about **“who is earning from it?”** quite directly.

### Why does your bank get the biggest piece?

The issuer bank holds your account and handles authorization, account infrastructure, fraud controls, settlement responsibilities and related processing.

The acquiring side handles the merchant.

The TPAP—PhonePe, Google Pay, Paytm etc.—provides the consumer-facing app/infrastructure.

And its partner PSP bank participates in routing/settlement.

---

# 3. This makes PhonePe's interest in MDR much easier to understand

PhonePe is especially important here because it has **more than 45% of UPI transaction volume** and processes roughly **11.5 billion transactions worth more than ₹14 lakh crore every month**, according to Sameer Nigam's current interview. citeturn166679search9

And now:

> UPI applications receive **20% of the eligible MDR pool**.

PhonePe therefore moves from a peculiar position:

**huge UPI scale → enormous operating responsibility → very little direct transaction monetisation**

toward:

**huge UPI scale → recurring transaction-linked revenue.**

That's a fundamental change to its business model.

---

# 4. Why this matters enormously for the PhonePe IPO

This connection isn't speculation.

PhonePe CEO **Sameer Nigam explicitly said on September 16** that MDR could push PhonePe closer to restarting its IPO filing and that the company hopes to list during the current financial year.

Moneycontrol reports PhonePe had previously postponed the IPO amid geopolitical uncertainty and market conditions. It had been discussing an IPO of roughly **$1.3 billion at a reported $13–15 billion valuation**.

PhonePe reported FY26 consolidated revenue of around **₹7,920 crore**, up from ₹7,115 crore in FY25.

The MDR changes something investors have been asking PhonePe for years:

### “How do you monetize your dominant UPI position?”

Before:

> 45%+ UPI market share sounds fantastic, but processing more transactions also means more infrastructure and support costs.

Now:

> Some of that transaction scale itself produces revenue.

Nigam specifically said investors had repeatedly asked what UPI monetisation would eventually look like.

This means MDR can potentially improve:

**revenue visibility → contribution margins → operating leverage → eventual profitability narrative → IPO investor story.**

That's why this announcement is much more important to PhonePe's IPO than just an extra fee.

PhonePe also has around **3 crore merchants and 60 crore consumers**, giving it additional opportunities around merchant acquiring and financial services. citeturn166679search9

### But don't make the mistake of assuming PhonePe gets 0.4%.

It doesn't.

If PhonePe is simply the TPAP on an eligible transaction, the app-side portion is **20% of the MDR**.

So its direct TPAP economics from a standard transaction correspond to:

**20% × 0.4% = an effective 0.08% of transaction value**, before considering its relationships with banks/acquirers and the actual qualifying mix.

There are additional merchant-acquiring economics in cases where PhonePe participates on that side, but you shouldn't simply add 30% automatically—contracts and transaction routing matter.

---

# 5. Why PhonePe could potentially make a lot despite the tiny percentage

UPI is operating at extraordinary scale.

In August 2026 alone it processed roughly:

**24.5 billion transactions**
worth approximately
**₹29.8 lakh crore.**

Yet the MDR is targeted very narrowly.

Payments above ₹2,000 represent only around **4% of merchant transactions by count**, but roughly **67% of merchant-transaction value**, according to current transaction analysis.

That's clever from an economic-design perspective:

the government/NPCI can say:

> “96% of merchant transactions remain free”

while still creating a potentially substantial monetisable value pool from the relatively small number of high-value transactions.

This explains why analysts are estimating an annual MDR ecosystem pool in the **tens of thousands of crores**, although those estimates vary considerably depending on exemptions, merchant classifications and payment behaviour. Treat those numbers as forecasts rather than guaranteed revenue.

---

# 6. How did we get here?

The history is important.

### 2016–2019: normal payment economics

UPI launched in 2016. Payment systems traditionally involved transaction economics between merchants, banks and payment providers.

### January 2020: UPI effectively becomes zero-MDR

The government made MDR zero for RuPay debit cards and BHIM-UPI through changes involving:

**Section 10A of the Payment and Settlement Systems Act, 2007**

and

**Section 269SU of the Income-tax Act.**

This was intended to accelerate digital-payment adoption.

And it worked spectacularly.

UPI went from being one payment method among many to becoming India's dominant retail digital payment network.

### 2020–2026: the payment industry's complaint grows

Banks, PhonePe, Paytm and other industry participants increasingly argued that transaction volume was exploding while transaction revenue remained essentially zero.

Instead, the government supported low-value UPI through incentive schemes.

The argument became:

> Should taxpayers/government incentives keep financing UPI infrastructure indefinitely, or should large commercial transactions contribute something toward the network?

That is effectively the policy dispute we're seeing now.

---

# 7. The 2026 change happened in several steps

It wasn't simply “NPCI woke up and charged 0.4%.”

The sequence was:

**Parliament**
→ amended the legal framework under the **Taxation and Other Laws (Amendment) Bill, 2026**

then

**Central Government**
→ issued the relevant notification on **14 September 2026**

then

**UPI and Services Steering Committee / NPCI**
→ met on **15 September**

then

**0.4% / 40 basis points** was fixed for the eligible category

then

**15 October 2026**
→ implementation starts.

The Finance Ministry describes the framework as being introduced under the Payment and Settlement Systems Act following deliberations by the UPI Steering Committee. citeturn166679search12

---

# 8. Where did exactly **0.4%** come from?

This is interesting because I could not find a publicly released calculation resembling:

> server cost X + fraud cost Y + bank cost Z = exactly 0.4000%.

In other words, **0.4% appears to be a policy-set rate, not a publicly demonstrated cost-plus formula**.

The UPI Steering Committee settled on **40 basis points**.

Earlier industry/policy reporting had floated considerably lower targeted rates—some reports discussed figures around **5–7 basis points**—before the eventual 40-bps framework emerged.

The government's rationale is essentially that 0.4%:

is large enough to create meaningful payment-industry economics,

while remaining well below typical credit-card MDR rates.

PhonePe's Sameer Nigam compared 0.4% with credit-card MDR around **1.7–2.5%** and argued the UPI rate remains very low by comparison. That's PhonePe's position, not an independent conclusion. citeturn166679search9

---

# 9. Important: don't confuse this with the **2023 “1.1% UPI charge”**

This confusion is already resurfacing online.

Back in 2023, NPCI introduced an **interchange fee of up to 1.1% for certain PPI/wallet-funded UPI merchant transactions above ₹2,000**.

That did **not** mean ordinary bank-account-to-bank-account UPI payments suddenly cost consumers 1.1%.

The 2026 change is different.

This is an actual **UPI merchant MDR framework on specified bank-account P2M transactions**, rather than merely the earlier PPI interoperability arrangement.

---

# 10. Who wins?

## Banks are probably the clearest financial winners

They collectively capture most of the MDR.

Issuer bank: **40%**

Acquiring side: **30%**

TPAP sponsor/partner bank: **10%**

Depending on transaction configuration, banking institutions therefore participate heavily in the revenue pool.

For years banks argued that they bore significant infrastructure, fraud, cybersecurity and settlement costs while UPI MDR remained zero.

Now a portion of high-value commerce pays for that infrastructure.

---

## PhonePe, Google Pay, Paytm and other UPI apps

The TPAP receives **20%**.

For companies with enormous UPI volume, even a very small yield multiplied across billions of transactions can become meaningful.

PhonePe is particularly exposed because of its >45% market share. citeturn166679search9

This is why fintech executives have been so enthusiastic.

Paytm founder Vijay Shekhar Sharma described the move as making UPI more **“self-sustaining.”**

MobiKwik co-founder Upasana Taku has similarly supported it as a way of financing infrastructure.

Pine Labs CEO Amrish Rau argued on X that transaction monetisation changes the investment narrative around Indian fintechs from:

> scale without a clear route to monetisation

toward

> scale plus a sustainable revenue model.

Those are industry viewpoints—they have obvious economic interests in the outcome.

---

# 11. Who loses?

The most obvious direct loser is the **eligible merchant accepting a high-value UPI transaction**.

Imagine a business with a 5% gross margin.

A 0.4% payment-processing charge is not “just 0.4%” relative to that merchant's profit.

It can represent a meaningful portion of their margin.

That's why retailers are much less enthusiastic than fintechs.

A LocalCircles merchant survey covered more than **32,000 businesses across 242 districts**. Business Standard reported that only **17% said they were prepared to absorb a 0.4% MDR**, while 41% said they weren't willing to absorb any MDR.

Survey results aren't equivalent to nationally representative behavioural data, but they help explain the merchant backlash.

---

# 12. Could ordinary Indians eventually end up paying?

### Directly: no.

The current regulation deliberately prevents:

“UPI convenience fee: ₹20”

or

“PhonePe fee: ₹10”

from simply appearing on your transaction.

The government is emphatic on this point. citeturn166679search12

### Indirectly: quite possibly in some cases.

This is the heart of Ashneer Grover's argument.

A merchant can't necessarily say:

> Product ₹5,000 + UPI fee ₹20.

But a merchant can economically respond in other ways:

**raise its general price, reduce discounts, offer a cash discount, prefer NEFT for large payments, encourage cards when commercially preferable, or simply absorb the cost.**

So “customers are not charged MDR” and “customers can never experience any economic impact” are **not the same claim**.

That distinction explains much of the argument online.

---

# 13. Ashneer Grover's viral argument

His X post became one of the largest anti-MDR talking points.

Grover cited:

RBI surplus transferred to government,

listed-bank profits,

NPCI's surplus,

and the enormous cost of maintaining ATMs/cash infrastructure.

His argument is essentially:

> If banks and NPCI are already profitable and cash itself is expensive to maintain, why introduce a transaction levy on India's most efficient payment infrastructure?

He has described the levy as effectively **“tax collection”** and argued that eventually the consumer bears commercial costs passed through by merchants.

The government disputes the “tax” characterization because **the government does not collect the MDR**; it is distributed to payment-system participants. citeturn166679search12

Those are two different claims:

**Legal/accounting fact:** it isn't government tax revenue.

**Economic argument:** Grover argues consumers can nevertheless indirectly bear the cost.

You can agree or disagree with the economic reasoning, but those shouldn't be conflated.

---

# 14. Nithin Kamath has a more nuanced criticism

The Zerodha CEO's argument is particularly interesting.

He's **not fundamentally against MDR**.

He said some form of UPI monetisation was probably inevitable.

His problem is how it applies to brokerage deposits.

Consider:

Customer sends ₹2 lakh to Zerodha.

Zerodha incurs payment cost.

Customer makes **no trade**.

Zerodha receives zero brokerage revenue from that deposit.

Then the customer's unused funds may later be returned due to regulatory settlement requirements, after which the customer can send them back again.

So payment volume ≠ actual economic activity for the broker.

Kamath argued a substantially smaller charge/cap was more appropriate for that category.

The final framework recognizes part of that issue by setting capital-market UPI at only **0.02%**, rather than 0.4%, although the reported cap remains higher than the ₹5–₹10 cap Kamath had suggested.

---

# 15. What social media looks like right now

The Firecrawl sweep found four broad narratives.

### “UPI is no longer free”

This is the most common Instagram/Reels simplification.

It's technically wrong without the word **merchant**.

Personal UPI remains free.

Payments below ₹2,000 remain free.

Most P2M transaction counts remain free.

---

### “This is a hidden tax”

This is being driven heavily by clips/posts around Ashneer Grover.

The **“hidden tax”** wording is a political/economic characterization rather than the legal structure: the Ministry says neither it nor NPCI collects the MDR. citeturn166679search12

---

### “Finally UPI has a sustainable business model”

This dominates fintech/LinkedIn commentary.

PhonePe, Paytm, MobiKwik and payment-industry voices emphasize:

cybersecurity,

fraud prevention,

bank infrastructure,

server/network costs,

merchant acquisition,

innovation,

and expansion into smaller towns.

That framing is also self-interested: those companies are among the beneficiaries.

---

### “This was done for PhonePe/foreign companies”

I found variants of this claim on Instagram/X.

There is an obvious factual reason people connect PhonePe with the decision: **PhonePe is the largest UPI app and will receive app-side MDR revenue.**

But that does **not establish that the framework was created specifically for PhonePe**.

The revenue distribution applies across the payment ecosystem—issuer banks, merchant acquirers, Google Pay/PhonePe/Paytm and partner banks—not PhonePe alone.

The Finance Ministry has rejected claims that the policy was imposed because of external pressure. I found no credible evidence establishing that conspiracy.

---

# 16. The ₹2,000 boundary creates some weird incentives

This part deserves more attention than it's getting.

Suppose a merchant sells something for ₹2,100.

The difference between:

₹2,000 transaction → zero standard MDR

and

₹2,100 → eligible MDR

creates a threshold effect.

That can encourage behaviours such as:

splitting payments,

cash for the remainder,

multiple QR payments,

or merchants pushing alternative payment instruments.

NPCI/banks will almost certainly need to watch for deliberate transaction splitting and gaming if it becomes widespread.

---

# 17. Why protect small merchants?

The design very deliberately protects India's tiny QR merchants.

A small merchant receiving up to roughly **₹1 lakh per month through the relevant UPI QR category remains under zero MDR**.

There's also a provision for roughly **5% of MDR collections to be directed toward expanding UPI acceptance among small merchants/underserved areas**.

So conceptually:

### large-value commercial digital payments

help finance

### network operation + future merchant digitisation.

That is part of the government's justification.

---

# 18. What happens to a kirana store?

If it's genuinely a small QR merchant under the exemption:

**probably nothing.**

That ₹50 tea,

₹300 groceries,

₹800 medicine purchase,

₹1,500 restaurant bill

etc. remain outside standard MDR anyway.

This is why the “every QR shop is suddenly losing 0.4%” narrative is incorrect.

---

# 19. Who feels it the most?

Likely categories include:

**electronics retailers, jewellery, premium fashion, appliances, hotels, larger restaurants, private services, online commerce and other businesses with high average order values.**

And businesses with **thin margins** may care disproportionately.

A 0.4% payment cost is easier for a 30%-margin business to absorb than a 2%-margin business.

That is why sector-specific exemptions matter.

---

# 20. Why give railways/fuel/telecom/insurance special treatment?

Because percentage MDR can become awkward for:

thin-margin or public-utility-type sectors,

high-ticket regulated payments,

or sectors where passing the cost onward would immediately affect millions of consumers.

So eligible transactions in several essential categories get a **₹5 flat charge** rather than ordinary 0.4%.

This substantially limits the impact.

---

# 21. Credit cards could actually gain from this

Here's an unintended consequence.

Previously:

UPI merchant cost = **0**

credit-card merchant cost = perhaps **1.5–2.5%**

so UPI had a huge price advantage.

Now:

UPI = **0.4%** for eligible larger payments

credit card = still much higher,

but credit cards bring:

rewards,

interest-free periods,

cashback,

EMI,

chargeback protections.

The economic gap narrows slightly.

Some consumers may therefore use cards for high-value transactions—particularly if merchants don't discriminate between payment methods.

A previous LocalCircles consumer survey cited by Business Standard found significant stated willingness to move high-value transactions away from UPI if merchants passed costs onward. Again, that's stated survey behaviour, not proof of what consumers will actually do.

---

# 22. Cash could also make a small comeback

Retail associations have warned about exactly this.

Imagine:

Cash = merchant keeps ₹10,000.

UPI = merchant loses ₹40.

For businesses already operating heavily in cash, that creates an incentive at the margin to say:

> “Cash kar do, thoda discount de dunga.”

This is one of the strongest arguments **against** the MDR design.

India spent years making electronic payment acceptance economically preferable to cash.

Introducing MDR partially reverses that incentive.

How large the effect actually becomes will only be observable after **15 October 2026**.

---

# 23. But cash isn't really free either

This is the counterargument.

Businesses incur costs from:

cash handling,

employee theft,

counting,

bank deposits,

security,

ATM infrastructure,

cash logistics,

counterfeit risk,

reconciliation.

So the true comparison isn't:

**UPI 0.4% vs cash 0%.**

It's:

**visible digital-payment cost vs often-hidden cash-handling costs.**

This is why the long-term behavioural result isn't obvious.

---

# 24. Why payment companies say zero MDR was unsustainable

Imagine running an infrastructure handling roughly **70–80 crore transactions every day**.

Every transaction involves combinations of:

bank systems,

NPCI infrastructure,

API calls,

fraud monitoring,

dispute handling,

SMS/notifications,

customer support,

cybersecurity,

compliance,

merchant servicing,

high availability,

disaster recovery.

Someone ultimately pays for it.

The zero-MDR model essentially meant those costs were cross-subsidised by banks/payment companies, government incentive schemes, other products or investor capital.

The policy question became:

> Should high-value commercial users begin funding part of that network?

PhonePe obviously says yes. Critics say India's enormous public benefits from zero-cost digital payments justify maintaining it as infrastructure.

Both are meaningful economic arguments.

---

# 25. And this is why the controversy isn't simply “₹8 charge”

At its core there are **two competing philosophies of UPI**.

### UPI as public digital infrastructure

Like a road.

Keep the basic rail free.

The economy benefits from reduced cash usage, formalisation, tax visibility and digital commerce.

Fund the network indirectly.

This is closer to the argument from MDR critics.

### UPI as a commercial payment network

Like Visa/Mastercard, although organized very differently.

Merchants benefiting from payment acceptance should contribute toward its operating cost.

Infrastructure providers should have sustainable unit economics.

This is closer to the fintech/banking argument.

The **0.4% above ₹2,000 + small-merchant exemption** is effectively India's attempt to find a midpoint between those models.

---

# 26. There is already a legal challenge

This isn't necessarily the final chapter.

Current reporting says a petition challenging the new MDR framework has already reached the **Supreme Court**, while merchant organisations and some industry groups are lobbying around its design.

That means implementation details could still face legal scrutiny even though the framework is currently scheduled for **15 October 2026**.

So anything claiming today that the policy's economic consequences are already proven is premature.

---

# 27. The cleanest winners/losers picture

| Stakeholder | Likely effect |
|---|---|
| Normal consumer doing P2P | **Essentially unaffected directly** |
| Consumer making ₹100–₹2,000 merchant purchases | **Unaffected directly** |
| Small QR merchant | **Mostly protected/exempt** |
| High-ticket merchant | **New cost** |
| Thin-margin merchant | **Potentially meaningful cost** |
| Issuing banks | **Major new revenue stream** |
| Merchant acquiring banks | **New revenue** |
| PhonePe / Google Pay / Paytm | **New direct UPI monetisation** |
| PhonePe prospective IPO investors | **Clearer core-business monetisation story** |
| Brokers | **Some new payment cost, mitigated by special 0.02% rate** |
| Cash | **Could regain a little attractiveness for merchants** |
| Credit cards | **Potentially become relatively more competitive** |
| Government | **Does not directly collect MDR** |
| NPCI | **Does not simply pocket the MDR** |

---

# 28. One thing I would watch very closely after October 15

Not UPI volume overall.

UPI is far too entrenched for a 0.4% selective MDR to suddenly destroy it.

I'd watch **merchant behaviour for ₹2,000–₹20,000 transactions**:

whether merchants absorb the MDR,

whether average prices move,

whether “cash discount” signs appear,

whether transaction splitting increases,

whether cards gain share,

whether high-value P2M UPI growth slows,

and how much revenue PhonePe/Paytm/banks actually recognise.

Those numbers will tell us whether the policy works as designed.

---

## My overall reading of the situation

The phrase **“UPI is becoming paid” badly exaggerates the change**.

What's really happening is more specific:

> India is moving from **universal zero-MDR UPI** to a **hybrid model in which high-value commercial UPI transactions help finance the payment ecosystem, while consumers, P2P transfers, small transactions and small merchants remain heavily protected.**

The interesting controversy isn't whether **you will pay 0.4% every time you use PhonePe**—you won't under the announced framework.

The real debate is whether merchants can genuinely absorb that cost without eventually embedding some of it into prices, and whether giving banks/fintechs a direct revenue stream is worth weakening UPI's historic zero-cost advantage.

For **PhonePe**, though, the implications are unusually clear: after years of owning almost half of UPI traffic without being able to directly monetize standard UPI transactions, it finally gets a transaction-linked revenue stream. That directly addresses one of the biggest questions surrounding its IPO economics. The company's own CEO has explicitly connected MDR with restarting the IPO process. citeturn166679search9

And the crucial correction to most viral posts is:

**₹2,000 is not a “consumer charging threshold.” It is primarily part of the eligibility boundary for merchant-side MDR.**

navlistCurrent UPI MDR coverageturn626347news24,turn626347news25,turn626347news26,turn626347news28

Because this story is moving quickly—with the October 15 implementation, litigation and merchant response still ahead—I can also monitor **UPI MDR + PhonePe IPO + Supreme Court developments + social-media backlash** and alert you when something materially changes.

## Resources

### External references
- [Finance Ministry clarifies UPI charges: Person-to-person transactions to remain free](https://www.moneycontrol.com/news/india/finance-ministry-clarifies-upi-charges-person-to-person-transactions-to-remain-free-14030659.html?utm_source=chatgpt.com)
- [All Press Release: Press Information Bureau](https://www.pib.gov.in/AllRelease.aspx?MenuId=23&PMO=1&lang=1&reg=1&utm_source=chatgpt.com)
- [Issuer banks to get 40%, merchant acquirers 30%, UPI apps to get 20% of the UPI MDR revenue](https://www.moneycontrol.com/technology/issuer-banks-to-get-40-merchant-acquirers-30-upi-apps-to-get-20-of-the-upi-mdr-revenue-article-14030521.html?utm_source=chatgpt.com)
- [People not giving government, NPCI credit for keeping MDR low: PhonePe CEO Sameer Nigam](https://www.moneycontrol.com/technology/people-not-giving-government-npci-credit-for-keeping-mdr-low-phonepe-ceo-sameer-nigam-article-14031146.html?utm_source=chatgpt.com)
- [India's UPI fee shake-up: What changes and why it matters](https://www.reuters.com/world/india/indias-upi-fee-shake-up-what-changes-why-it-matters-2026-09-16/?utm_source=chatgpt.com)
- [India's UPI fee faces retailer, broker pushback](https://www.reuters.com/world/india/indias-upi-fee-faces-retailer-broker-pushback-2026-09-16/?utm_source=chatgpt.com)
- [India's payment firms jump as UPI fee boosts revenue outlook](https://www.reuters.com/world/india/indias-payment-firms-jump-upi-fee-boosts-revenue-outlook-2026-09-16/?utm_source=chatgpt.com)
- [Petition filed in India's top court to challenge UPI fee, NDTV reports](https://www.reuters.com/legal/litigation/petition-filed-indias-top-court-challenge-upi-fee-ndtv-reports-2026-09-16/?utm_source=chatgpt.com)
- [96% of UPI transactions to remain free after limited MDR: PhonePe's Sameer Nigam](https://www.moneycontrol.com/news/india/96-of-upi-transactions-to-remain-free-after-limited-mdr-phonepe-s-sameer-nigam-14030643.html?utm_source=chatgpt.com)
- [96% of UPI transactions to remain free after limited MDR: PhonePe's Sameer Nigam](https://www.moneycontrol.com/news/india/96-of-upi-transactions-to-remain-free-after-limited-mdr-phonepe-s-sameer-nigam-14030643.html/amp?utm_source=chatgpt.com)
- [UPI payments above Rs 2,000 double in three years but share declines](https://www.moneycontrol.com/news/business/upi-payments-above-rs-2-000-double-in-three-years-but-share-declines-14031173.html?utm_source=chatgpt.com)
- [UPI MDR fixed at 0.4% for transactions over Rs 2,000; capped at Rs 300 per transaction](https://www.moneycontrol.com/news/india/upi-mdr-fixed-at-40bps-for-transactions-over-rs-2-000-capped-at-rs-300-per-transaction-14030339.html?utm_source=chatgpt.com)
- [PhonePe CEO Sameer Nigam defends MDR, takes on Ashneer Grover](https://www.moneycontrol.com/news/videos/business/markets/phonepe-ceo-sameer-nigam-defends-mdr-takes-on-ashneer-grover-14030970.html/amp?utm_source=chatgpt.com)
- [Moneycontrol Pro Panorama | A 40 bps challenge to formalisation?](https://www.moneycontrol.com/news/business/economy/moneycontrol-pro-panorama-a-40-bps-challenge-to-formalisation-14031026.html?utm_source=chatgpt.com)
- [UPI MDR on stocks, MFs: Investors largely insulated, but brokers may feel the pinch](https://www.moneycontrol.com/news/business/markets/upi-mdr-on-stocks-mfs-investors-largely-insulated-but-brokers-may-feel-the-pinch-14030825.html?utm_source=chatgpt.com)
- [UPI’s bigger opportunity is creating credit, not charging for transactions: Former Chief Economic Adviser](https://www.moneycontrol.com/news/india/upi-s-bigger-opportunity-is-creating-credit-not-charging-for-transactions-former-chief-economic-adviser-14030642.html?utm_source=chatgpt.com)
- [UPI MDR: Capital market payments to attract just 0.02%, capped at Rs 300](https://www.moneycontrol.com/news/business/markets/upi-mdr-capital-market-payments-to-attract-just-0-02-capped-at-rs-300-14030501.html?utm_source=chatgpt.com)
- [Finance Ministry clarifies UPI charges: Person-to-person transactions to remain free](https://www.moneycontrol.com/news/india/finance-ministry-clarifies-upi-charges-person-to-person-transactions-to-remain-free-14030659.html/amp?utm_source=chatgpt.com)
- [Moneycontrol Startup-Tech Newsletters: Top Tech News, Startups News, Funding and Technology Updates - Moneycontrol.com](https://www.moneycontrol.com/news/technology-startup/newsletters/mctech3/?utm_source=chatgpt.com)
- [Business News: Stock and Share Market News, Economy and Finance News, Sensex, Nifty, Global Market, NSE, BSE Live IPO News - Moneycontrol.com](https://www.moneycontrol.com/?utm_source=chatgpt.com)
- [Tech News | Startup News | Funding | IT | Crypto - Moneycontrol.com](https://www.moneycontrol.com/news/technology/startup/?utm_source=chatgpt.com)
- [Business News: Stock and Share Market News, Economy and Finance News, Sensex, Nifty, Global Market, NSE, BSE Live IPO News - Moneycontrol.com](https://www.moneycontrol.com//?utm_source=chatgpt.com)
- [Tech3 | MDR set at 0.4% for transactions above Rs 2000, Oracle India begins layoffs; and more - Moneycontrol.com](https://www.moneycontrol.com/news/technology-startup/newsletters/MCTech3/tech3-mdr-set-at-0-4-for-transactions-above-rs-2000-oracle-india-begins-layoffs-and-more/?utm_source=chatgpt.com)
- [Business News: Stock and Share Market News, Economy and Finance News, Sensex, Nifty, Global Market, NSE, BSE Live IPO News - Moneycontrol.com](https://www.moneycontrol.com/?autono=286758&nlid=1&utm_source=chatgpt.com)
- [Business News: Stock and Share Market News, Economy and Finance News, Sensex, Nifty, Global Market, NSE, BSE Live IPO News - Moneycontrol.com](https://www.moneycontrol.com/?autono=331878&utm_source=chatgpt.com)
- [UPI MDR: Debit-card charges up to 0.90% versus 0.4% for eligible UPI payments](https://www.moneycontrol.com/news/business/economy/upi-mdr-debit-card-charges-up-to-0-90-versus-0-4-for-eligible-upi-payments-14030523.html/amp?utm_source=chatgpt.com)
- [Anand J: Read latest news from Moneycontrol journalist/contributor Anand J | Page 1 - Moneycontrol.com](https://www.moneycontrol.com/author/anand-j-32011/?utm_source=chatgpt.com)
- [Business News: Stock and Share Market News, Economy and Finance News, Sensex, Nifty, Global Market, NSE, BSE Live IPO News - Moneycontrol.com](https://www.moneycontrol.com/?section=mktalerts&utm_source=chatgpt.com)
- [Technology News: Latest Gadget News, Tech News | Moneycontrol.com - Moneycontrol.com](https://www.moneycontrol.com/news/technology/?utm_source=chatgpt.com)
- [Latest News in Shorts: Business News, National News in Short Summaries](https://www.moneycontrol.com/shorts/auto/?utm_source=chatgpt.com)
- [Business News Videos | Share Market Videos - Moneycontrol.com](https://www.moneycontrol.com/news/videos/?utm_source=chatgpt.com)
- [Latest News | Latest Business News | BSE | IPO News - Moneycontrol.com](https://www.moneycontrol.com/news/?utm_source=chatgpt.com)
- [Business News, Economic News, Indian Stock Market News - Moneycontrol.com](https://www.moneycontrol.com/news/business/?utm_source=chatgpt.com)
- [Business News: Stock and Share Market News, Economy and Finance News, Sensex, Nifty, Global Market, NSE, BSE Live IPO News - Moneycontrol.com](https://www.moneycontrol.com//amp?utm_source=chatgpt.com)
- [Latest News | Latest Business News | BSE | IPO News - Moneycontrol.com](https://www.moneycontrol.com/video-shows/www.moneycontrol.com/target%3D/target%3Damp/news/india/?utm_source=chatgpt.com)
- [Press Release: Press Information Bureau](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2310586&lang=1&reg=3&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2310659&lang=2&reg=48&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2310689&lang=2&reg=48&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2310704&lang=8&reg=20&utm_source=chatgpt.com)
- [Press Release: Press Information Bureau](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2310672&lang=2&reg=48&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2310635&lang=2&reg=48&utm_source=chatgpt.com)
- [Press Release:Press Information Bureau](https://www.pib.gov.in/PressReleaseIframePage.aspx?LID=1&PRID=2296594&RegID=3&lang=2&reg=48&utm_source=chatgpt.com)
- [Factsheet Details:Factsheet Details | PIB](https://www.pib.gov.in/FactsheetDetails.aspx?ModuleId=16&NoteId=150872&id=150872&lang=10&reg=23&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2296673&lang=2&reg=48&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2296745&lang=2&reg=48&utm_source=chatgpt.com)
- [Factsheet Details:Factsheet Details | PIB](https://www.pib.gov.in/FactsheetDetails.aspx?Id=150962&lang=1&reg=1&utm_source=chatgpt.com)
- [Press Release: Press Information Bureau](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2302657&lang=1&reg=3&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2296594&lang=1&reg=48&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2297331&lang=2&reg=48&utm_source=chatgpt.com)
- [Page 40 - NIS English 01-15 September, 2026](https://newindiasamachar.pib.gov.in/WriteReadData/flipbook/2026/Sep/1st/English/files/basic-html/page40.html?utm_source=chatgpt.com)
- [All Press Release: Press Information Bureau](https://www.pib.gov.in/AllRelease.aspx?MenuId=287&PMO=1&lang=1&reg=6&utm_source=chatgpt.com)
- [All Press Release: Press Information Bureau](https://www.pib.gov.in/AllRelease.aspx?MenuId=365&PMO=1&lang=1&reg=3&utm_source=chatgpt.com)
- [All Press Release: Press Information Bureau](https://www.pib.gov.in/AllRelease.aspx?MenuId=286&lang=1&reg=6&utm_source=chatgpt.com)
- [Press Release: Press Information Bureau](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2310384&lang=1&reg=6&utm_source=chatgpt.com)
- [Press Release: Press Information Bureau](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2287641&lang=1&reg=22&utm_source=chatgpt.com)
- [Prime Minister's Content | PIB](https://www.pib.gov.in/PMContents/PMContents.aspx?Lang=1&RegionId=1%2F1000&menuid=8&reg=3&utm_source=chatgpt.com)
- [Press Release: Press Information Bureau](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=1918718&lang=1&reg=3&utm_source=chatgpt.com)
- [Press Release: Press Information Bureau](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2310095&lang=1&reg=1&utm_source=chatgpt.com)
- [Press Release: Press Information Bureau](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=1488419&lang=1&reg=3&utm_source=chatgpt.com)
- [All Press Releasem: Press Information Bureau](https://www.pib.gov.in/AllReleasem.aspx?lang=1&reg=3&utm_source=chatgpt.com)

---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "68f350e4-a094-8324-9fdf-a9e0d3894bfe"
created: 1760776508.861383
updated: 1760782500.750029
resource_section: true
---

# Compound interest calculation

## User

Calculate compounding intrest on 20 lakh after every 15 months intrest of 6.60 for 10 years

## Assistant

Let's carefully calculate this **step by step**. 

---

### Given Data:
- Principal (P) = ₹20,00,000 
- Rate of Interest (R) = 6.60% per annum 
- Time (T) = 10 years 
- Compounding period = every **15 months** 

---

### Step 1: Convert compounding frequency

1 year = 12 months 
→ 15 months = 1.25 years 

So, number of compounding periods in 10 years = 
\\[
\frac{10}{1.25} = 8
\\]
Hence, there will be **8 compounding periods** in total.

---

### Step 2: Formula for compound interest

\\[
A = P \times (1 + \frac{R}{100})^n
\\]

But since R = 6.60% **per year**, and each compounding happens every 1.25 years, 
the effective rate per compounding period is:

\\[
R_{\text{period}} = 6.60 \times 1.25 = 8.25\%
\\]

---

### Step 3: Calculate final amount

\\[
A = 20,00,000 \times (1 + \frac{8.25}{100})^8
\\]

\\[
A = 20,00,000 \times (1.0825)^8
\\]

Now calculate step-by-step:

| Power | Value of (1.0825)^n |
|:------|:--------------------|
| 1 | 1.0825 |
| 2 | 1.1718 |
| 3 | 1.2686 |
| 4 | 1.3743 |
| 5 | 1.4893 |
| 6 | 1.6145 |
| 7 | 1.7508 |
| 8 | **1.8995 (approx)** |

So,

\\[
A = 20,00,000 \times 1.8995 = ₹37,99,000
\\]

---

### Step 4: Compound Interest

\\[
CI = A - P = 37,99,000 - 20,00,000 = ₹17,99,000
\\]

---

✅ **Final Answer:** 
- **Total Amount after 10 years:** ₹37,99,000 
- **Compound Interest:** ₹17,99,000 
- **Compounded every:** 15 months 
- **Effective rate per compounding:** 8.25% 

---

Would you like me to also show **year-wise or period-wise growth** (i.e., amount after each 15 months)?

## User

Effective rate per compounding 6.60

## Assistant

Good catch — let’s redo it **with 6.60% as the rate per compounding period**, not per annum. 

That means: 
- **Principal (P)** = ₹20,00,000 
- **Rate (R)** = 6.60% **per 15 months** 
- **Time (T)** = 10 years = 120 months 
- Compounding every 15 months → 
 \\[
 n = \frac{120}{15} = 8
 \\]
 So, there are **8 compounding periods**.

---

### Step 1: Apply compound interest formula

\\[
A = P \times \left(1 + \frac{R}{100}\right)^n
\\]

\\[
A = 20,00,000 \times (1 + \frac{6.6}{100})^8
\\]

\\[
A = 20,00,000 \times (1.066)^8
\\]

---

### Step 2: Compute (1.066)^8 step-by-step

| Power | (1.066)^n |
|:------|:-----------|
| 1 | 1.066 |
| 2 | 1.1364 |
| 3 | 1.2114 |
| 4 | 1.2913 |
| 5 | 1.3765 |
| 6 | 1.4673 |
| 7 | 1.5642 |
| 8 | **1.6674 (approx)** |

---

### Step 3: Final Amount

\\[
A = 20,00,000 \times 1.6674 = ₹33,34,800
\\]

---

### Step 4: Compound Interest

\\[
CI = A - P = 33,34,800 - 20,00,000 = ₹13,34,800
\\]

---

✅ **Final Answer:**

| Description | Value |
|:-------------|:----------------|
| Principal | ₹20,00,000 |
| Rate of Interest | 6.60% (per 15 months) |
| Compounding Periods | 8 |
| Total Amount | **₹33,34,800** |
| Compound Interest | **₹13,34,800** |

---

Would you like me to show how much it grows **after each 15-month period** in a table format?

## User

Yes

## Assistant

Perfect 👍 Let’s prepare a **period-wise (every 15 months)** breakdown of how your ₹20 lakh grows when compounded at **6.60% per 15 months** for **10 years (8 periods)**.

---

### Given:
- Principal = ₹20,00,000 
- Rate = 6.60 % per compounding period 
- Compounding every 15 months 
- Total periods = 8 

---

### Formula:
\\[
A_n = P \times (1 + \frac{R}{100})^n
\\]
where \(A_n\) = amount after n periods

---

| Period | Time (months) | Formula Used | Amount (₹) | Interest Earned in Period (₹) |
|:-------|:---------------|:--------------|:--------------|:-------------------------------|
| 0 | 0 | – | **20,00,000** | – |
| 1 | 15 | 20,00,000 × 1.066 | **21,32,000** | 1,32,000 |
| 2 | 30 | 20,00,000 × (1.066)² | **22,72,800** | 1,40,800 |
| 3 | 45 | 20,00,000 × (1.066)³ | **24,22,500** | 1,49,700 |
| 4 | 60 | 20,00,000 × (1.066)⁴ | **25,81,100** | 1,58,600 |
| 5 | 75 | 20,00,000 × (1.066)⁵ | **27,49,100** | 1,68,000 |
| 6 | 90 | 20,00,000 × (1.066)⁶ | **29,27,000** | 1,77,900 |
| 7 | 105 | 20,00,000 × (1.066)⁷ | **31,14,500** | 1,87,500 |
| 8 | 120 | 20,00,000 × (1.066)⁸ | **33,34,800** | 2,20,300 |

---

✅ **Summary:**

- **Total Amount after 10 years:** ₹33,34,800 
- **Total Compound Interest:** ₹13,34,800 
- **Compounding every:** 15 months at 6.60 % 

---

Would you like me to also show the **effective annual interest rate (EAR)** equivalent to 6.6 % every 15 months?

## User

P×(1+R/ 100)^n in this P will change after every period and new P will be previous amount

## Assistant

Excellent observation, Utkarsh 👏 — and you are **absolutely correct** in principle. 

Let’s clarify this carefully because this concept often confuses many students.

---

### 🧠 Concept Understanding

The formula 
\\[
A = P \times (1 + \frac{R}{100})^n
\\] 
**already** assumes that the **principal gets updated automatically** after every compounding period.

In other words:
- After 1st period → New principal = old amount (A₁) 
- After 2nd period → New principal = A₂, and so on. 

So, you **don’t have to manually change P** each time — the formula’s exponent **(n)** takes care of that cumulative growth.

---

### 🔍 If you prefer to see it step-by-step manually:

Let’s do it the way you’re describing — i.e., updating **P after every period**.

---

| Period | Opening Principal (₹) | Interest (6.6%) | Closing Amount (₹) |
|:-------|:----------------------|:----------------|:------------------|
| 1 | 20,00,000 | 1,32,000 | **21,32,000** |
| 2 | 21,32,000 | 1,40,112 | **22,72,112** |
| 3 | 22,72,112 | 1,49,959 | **24,22,071** |
| 4 | 24,22,071 | 1,59,657 | **25,81,728** |
| 5 | 25,81,728 | 1,70,194 | **27,51,922** |
| 6 | 27,51,922 | 1,81,427 | **29,33,349** |
| 7 | 29,33,349 | 1,93,001 | **31,26,350** |
| 8 | 31,26,350 | 2,06,539 | **33,32,889** |

---

✅ **Final Results:**

| Description | Value |
|:-------------|:----------------|
| Total Amount after 10 years | **₹33,32,889** |
| Total Compound Interest | **₹13,32,889** |
| Interest Rate | 6.6% every 15 months |
| Number of Compounding Periods | 8 |

---

### 🧾 Explanation:
After every compounding period (15 months), the interest earned is **added back** to the principal. 
Thus, your **new principal (P)** becomes the **previous amount (A)** — which is exactly what the compound formula already does mathematically.

---

Would you like me to show the **same breakdown but also include cumulative interest** after each period (like total profit so far)?

## Resources

No structured attachments or external references were present in this conversation.

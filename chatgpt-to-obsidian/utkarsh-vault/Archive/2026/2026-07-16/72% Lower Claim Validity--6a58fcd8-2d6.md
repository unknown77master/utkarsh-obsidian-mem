---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a58fcd8-2d64-83ee-b7c7-949f2c180dde"
created: 1784216833.652986
updated: 1784216946.716244
resource_section: true
---

# 72% Lower Claim Validity

## User

this this correct what they are claiming 72% lower

## Assistant

Based on the numbers shown in the image, the **pricing table itself is internally consistent**, but the claim **"approximately 72% lower than official pricing"** cannot be verified from this image alone.

Here's why:

The table says (per 1M tokens):

| Model | Input | Output |
|--------|-------|---------|
| Sol | 280 credits (≈ $1.40) | 1,680 credits (≈ $8.40) |
| Terra | 140 credits (≈ $0.70) | 840 credits (≈ $4.20) |
| Luna | 56 credits (≈ $0.28) | 336 credits (≈ $1.68) |

From these values:
- 1 credit = **$0.005**
- The dollar conversions are correct.

### About the "72% lower" claim

If something is **72% cheaper**, then:

\\[
\text{Their Price} = 28\% \text{ of Official Price}
\\]

So the implied official prices would be:

| Tier | Their Price | Implied Official Price |
|------|-------------:|-----------------------:|
| Sol Input | $1.40 | **$5.00** |
| Sol Output | $8.40 | **$30.00** |
| Terra Input | $0.70 | **$2.50** |
| Terra Output | $4.20 | **$15.00** |
| Luna Input | $0.28 | **$1.00** |
| Luna Output | $1.68 | **$6.00** |

Notice the pattern:
- $5 → $1.40 is exactly **72% off**
- $30 → $8.40 is exactly **72% off**
- Same for every other value.

### Is the claim true?

**Mathematically:** Yes. If the official prices are exactly those implied values, then the numbers in the table represent a **72% discount**.

**Factually:** You **cannot conclude it's true from this screenshot alone.** You would need to compare these prices against the **actual official GPT-5.6 API pricing** from the provider. The screenshot doesn't show the official price source.

So the correct conclusion is:

- ✅ The arithmetic in the image is correct.
- ✅ The prices are consistent with a 72% discount.
- ❓ Whether they are *actually* 72% lower than official pricing depends on what the official GPT-5.6 prices are. The screenshot alone doesn't prove that.

## User

GPT-5.6 is billed via the API and used in ChatGPT across three specific tiers, with pricing calculated per 1 million tokens:Sol (Flagship): $5.00 input and $30.00 output.Terra (Balanced): $2.50 input and $15.00 output (offers 5.5-level performance at half the cost).Luna (Fastest/Budget): $1.00 input and $6.00 output

## Assistant

Yes. If those are indeed the **official GPT-5.6 API prices**, then the claim in the screenshot is accurate.

Let's verify.

Formula:

\\[
\text{Discount} = \left(1 - \frac{\text{Discounted Price}}{\text{Official Price}}\right)\times100
\\]

### Sol

| Token Type | Official | Screenshot | Discount |
|------------|---------:|-----------:|---------:|
| Input | $5.00 | $1.40 | **72%** |
| Output | $30.00 | $8.40 | **72%** |

Calculation:
- \(1 - \frac{1.40}{5.00} = 0.72 = 72\%\)
- \(1 - \frac{8.40}{30.00} = 0.72 = 72\%\)

---

### Terra

| Token Type | Official | Screenshot | Discount |
|------------|---------:|-----------:|---------:|
| Input | $2.50 | $0.70 | **72%** |
| Output | $15.00 | $4.20 | **72%** |

Calculation:
- \(1 - \frac{0.70}{2.50} = 72\%\)
- \(1 - \frac{4.20}{15.00} = 72\%\)

---

### Luna

| Token Type | Official | Screenshot | Discount |
|------------|---------:|-----------:|---------:|
| Input | $1.00 | $0.28 | **72%** |
| Output | $6.00 | $1.68 | **72%** |

Calculation:
- \(1 - \frac{0.28}{1.00} = 72\%\)
- \(1 - \frac{1.68}{6.00} = 72\%\)

---

## Final conclusion

✅ **The claim is mathematically correct.**

Every price shown in the screenshot is exactly **28% of the official GPT-5.6 API price**, which means they are **72% lower**.

So if the official pricing you quoted is correct:

- **Sol:** $5 → $1.40, $30 → $8.40 ✔️
- **Terra:** $2.50 → $0.70, $15 → $4.20 ✔️
- **Luna:** $1.00 → $0.28, $6 → $1.68 ✔️

The screenshot's statement **"All three tiers are approximately 72% lower than official pricing."** is accurate.

## Resources

### Local attachments
- [image(26).png](../../../Raw/Export/file_00000000089c71f59a1cde6c7894268e.dat)

# Statistics Reference

Key concepts and formulas for statistics and probability.

## Descriptive Statistics

### Measures of Center
- **Mean:** x̄ = Σxᵢ/n
- **Median:** Middle value when sorted
- **Mode:** Most frequent value

### Measures of Spread
- **Range:** max - min
- **Variance:** s² = Σ(xᵢ - x̄)²/(n-1)
- **Standard Deviation:** s = √variance
- **IQR:** Q3 - Q1

### Five-Number Summary
Min, Q1, Median, Q3, Max

---

## Probability

### Basic Rules
- P(A or B) = P(A) + P(B) - P(A and B)
- P(A and B) = P(A) · P(B|A)
- P(Aᶜ) = 1 - P(A)

### Conditional Probability
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

### Bayes' Theorem
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

### Independence
A and B independent if:
- P(A and B) = P(A) · P(B)
- P(A|B) = P(A)

---

## Discrete Distributions

### Binomial
X ~ Binomial(n, p)
- P(X = k) = C(n,k) pᵏ (1-p)ⁿ⁻ᵏ
- Mean: μ = np
- Variance: σ² = np(1-p)

### Poisson
X ~ Poisson(λ)
- P(X = k) = e⁻λ λᵏ/k!
- Mean = Variance = λ

### Geometric
X ~ Geometric(p)
- P(X = k) = (1-p)ᵏ⁻¹ p
- Mean: μ = 1/p

---

## Continuous Distributions

### Normal Distribution
X ~ N(μ, σ²)

**Standard Normal (Z-score):**
$$Z = \frac{X - \mu}{\sigma}$$

**68-95-99.7 Rule:**
- 68% within 1σ
- 95% within 2σ
- 99.7% within 3σ

### Uniform
X ~ Uniform(a, b)
- Mean: (a+b)/2
- Variance: (b-a)²/12

### Exponential
X ~ Exponential(λ)
- Mean: 1/λ
- Variance: 1/λ²

---

## Sampling Distributions

### Central Limit Theorem
For large n, sample mean x̄ is approximately normal:
$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

### Standard Error
$$SE = \frac{\sigma}{\sqrt{n}}$$

---

## Confidence Intervals

### For Mean (σ known)
$$\bar{x} \pm z^* \frac{\sigma}{\sqrt{n}}$$

### For Mean (σ unknown)
$$\bar{x} \pm t^* \frac{s}{\sqrt{n}}$$

### For Proportion
$$\hat{p} \pm z^* \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

### Common z* Values
| Confidence | z* |
|------------|-----|
| 90% | 1.645 |
| 95% | 1.96 |
| 99% | 2.576 |

---

## Hypothesis Testing

### Steps
1. State H₀ and Hₐ
2. Choose significance level α
3. Calculate test statistic
4. Find p-value
5. Compare p-value to α
6. State conclusion

### Test Statistics
**Z-test (σ known):**
$$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$$

**t-test (σ unknown):**
$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$$

### Errors
- **Type I:** Reject H₀ when true (α)
- **Type II:** Fail to reject H₀ when false (β)
- **Power:** 1 - β

---

## Regression

### Simple Linear Regression
$$\hat{y} = b_0 + b_1 x$$

$$b_1 = r \frac{s_y}{s_x}$$

$$b_0 = \bar{y} - b_1\bar{x}$$

### Correlation (r)
- r = 1: Perfect positive
- r = -1: Perfect negative
- r = 0: No linear relationship
- r² = coefficient of determination

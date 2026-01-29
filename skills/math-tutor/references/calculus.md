# Calculus Reference

Comprehensive calculus reference for derivatives, integrals, and applications.

## Limits

### Evaluation Techniques

| Form | Technique |
|------|-----------|
| Direct substitution | Try first, if defined |
| 0/0 | Factor, rationalize, or L'Hôpital |
| ∞/∞ | L'Hôpital's Rule |
| 0 · ∞ | Rewrite as 0/0 or ∞/∞ |

### L'Hôpital's Rule
If lim f(x)/g(x) gives 0/0 or ∞/∞:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

### Important Limits
- lim (sin x)/x = 1 as x→0
- lim (1 + 1/n)ⁿ = e as n→∞
- lim (eˣ - 1)/x = 1 as x→0

---

## Derivatives

### Derivative Rules

| Rule | Formula |
|------|---------|
| Power | d/dx[xⁿ] = nxⁿ⁻¹ |
| Product | d/dx[fg] = f'g + fg' |
| Quotient | d/dx[f/g] = (f'g - fg')/g² |
| Chain | d/dx[f(g(x))] = f'(g(x)) · g'(x) |

### Common Derivatives

| f(x) | f'(x) |
|------|-------|
| xⁿ | nxⁿ⁻¹ |
| eˣ | eˣ |
| aˣ | aˣ ln a |
| ln x | 1/x |
| logₐ x | 1/(x ln a) |
| sin x | cos x |
| cos x | -sin x |
| tan x | sec²x |
| cot x | -csc²x |
| sec x | sec x tan x |
| csc x | -csc x cot x |
| arcsin x | 1/√(1-x²) |
| arccos x | -1/√(1-x²) |
| arctan x | 1/(1+x²) |

### Applications

**Critical points:** f'(x) = 0 or undefined
**First derivative test:**
- f' changes + to - → local max
- f' changes - to + → local min

**Second derivative test:**
- f''(c) > 0 → local min
- f''(c) < 0 → local max

---

## Integrals

### Integration Rules

| Rule | Formula |
|------|---------|
| Power | ∫xⁿ dx = xⁿ⁺¹/(n+1) + C (n≠-1) |
| Constant multiple | ∫af(x) dx = a∫f(x) dx |
| Sum | ∫[f+g] dx = ∫f dx + ∫g dx |

### Integration Techniques

**Substitution (u-sub):**
1. Let u = g(x)
2. du = g'(x)dx
3. Replace and integrate
4. Substitute back

**Integration by Parts:**
$$\int u \, dv = uv - \int v \, du$$

LIATE for choosing u: Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential

**Partial Fractions:**
For rational functions P(x)/Q(x) where deg(P) < deg(Q):
1. Factor denominator
2. Write as sum of simpler fractions
3. Solve for constants
4. Integrate each term

---

## Applications of Integration

### Area Between Curves
$$A = \int_a^b |f(x) - g(x)| dx$$

### Volume (Disk Method)
$$V = \pi \int_a^b [f(x)]^2 dx$$

### Volume (Shell Method)
$$V = 2\pi \int_a^b x \cdot f(x) dx$$

### Arc Length
$$L = \int_a^b \sqrt{1 + [f'(x)]^2} dx$$

---

## Series

### Taylor Series (at a)
$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

### Maclaurin Series (a=0)
- eˣ = 1 + x + x²/2! + x³/3! + ...
- sin x = x - x³/3! + x⁵/5! - ...
- cos x = 1 - x²/2! + x⁴/4! - ...
- 1/(1-x) = 1 + x + x² + x³ + ... (|x|<1)

### Convergence Tests

| Test | Converges if |
|------|-------------|
| Geometric | |r| < 1 |
| p-series | p > 1 |
| Ratio | lim |aₙ₊₁/aₙ| < 1 |
| Root | lim ⁿ√|aₙ| < 1 |
| Integral | ∫f(x)dx converges |

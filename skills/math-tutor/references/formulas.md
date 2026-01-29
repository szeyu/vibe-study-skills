# Math Formulas Reference

Comprehensive formula reference for common mathematical topics.

## Algebra

### Quadratic Formula
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### Binomial Theorem
$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

### Logarithm Properties
- log(xy) = log x + log y
- log(x/y) = log x - log y
- log(xⁿ) = n log x
- logₐ b = (ln b) / (ln a)

### Exponential Properties
- aᵐ · aⁿ = aᵐ⁺ⁿ
- aᵐ / aⁿ = aᵐ⁻ⁿ
- (aᵐ)ⁿ = aᵐⁿ
- a⁰ = 1

---

## Geometry

### Areas
| Shape | Area |
|-------|------|
| Triangle | ½bh |
| Rectangle | lw |
| Circle | πr² |
| Trapezoid | ½(b₁+b₂)h |
| Sphere surface | 4πr² |

### Volumes
| Shape | Volume |
|-------|--------|
| Rectangular prism | lwh |
| Cylinder | πr²h |
| Sphere | (4/3)πr³ |
| Cone | (1/3)πr²h |

### Trigonometry
- sin²θ + cos²θ = 1
- tan θ = sin θ / cos θ
- sin(A ± B) = sin A cos B ± cos A sin B
- cos(A ± B) = cos A cos B ∓ sin A sin B

---

## Sequences & Series

### Arithmetic
- aₙ = a₁ + (n-1)d
- Sₙ = (n/2)(a₁ + aₙ) = (n/2)(2a₁ + (n-1)d)

### Geometric
- aₙ = a₁ · rⁿ⁻¹
- Sₙ = a₁(1 - rⁿ)/(1 - r) for r ≠ 1
- S∞ = a₁/(1 - r) for |r| < 1

### Common Sums
- Σk = n(n+1)/2
- Σk² = n(n+1)(2n+1)/6
- Σk³ = [n(n+1)/2]²

---

## Calculus Quick Reference

### Derivatives
| f(x) | f'(x) |
|------|-------|
| xⁿ | nxⁿ⁻¹ |
| eˣ | eˣ |
| ln x | 1/x |
| sin x | cos x |
| cos x | -sin x |
| tan x | sec²x |

### Integrals
| f(x) | ∫f(x)dx |
|------|---------|
| xⁿ | xⁿ⁺¹/(n+1) + C |
| eˣ | eˣ + C |
| 1/x | ln|x| + C |
| sin x | -cos x + C |
| cos x | sin x + C |

---

## Combinatorics

### Permutations
$$P(n,r) = \frac{n!}{(n-r)!}$$

### Combinations
$$C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

### Probability
- P(A or B) = P(A) + P(B) - P(A and B)
- P(A and B) = P(A) · P(B|A)
- Bayes: P(A|B) = P(B|A)·P(A) / P(B)

---

## Linear Algebra

### Dot Product
$$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = a_1b_1 + a_2b_2 + ...$$

### Cross Product (3D)
$$\vec{a} \times \vec{b} = (a_2b_3 - a_3b_2, a_3b_1 - a_1b_3, a_1b_2 - a_2b_1)$$

### Matrix Determinant (2×2)
$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

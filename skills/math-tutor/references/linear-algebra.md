# Linear Algebra Reference

Key concepts and operations for linear algebra.

## Vectors

### Operations
- Addition: (a₁,a₂) + (b₁,b₂) = (a₁+b₁, a₂+b₂)
- Scalar mult: c(a₁,a₂) = (ca₁, ca₂)
- Magnitude: |v| = √(v₁² + v₂² + ...)

### Dot Product
$$\vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2 + ... = |\vec{a}||\vec{b}|\cos\theta$$

Properties:
- Commutative: a·b = b·a
- If a·b = 0, vectors are orthogonal

### Cross Product (3D)
$$\vec{a} \times \vec{b} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}$$

Result is perpendicular to both vectors.

---

## Matrices

### Basic Operations

**Addition:** (A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ

**Scalar multiplication:** (cA)ᵢⱼ = c·Aᵢⱼ

**Matrix multiplication:** (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ
- Requires: cols(A) = rows(B)
- Result: rows(A) × cols(B)

### Special Matrices

| Type | Definition |
|------|------------|
| Identity I | 1s on diagonal, 0s elsewhere |
| Zero | All zeros |
| Diagonal | Non-zero only on diagonal |
| Symmetric | A = Aᵀ |
| Orthogonal | AAᵀ = I |

---

## Determinants

### 2×2 Matrix
$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

### 3×3 Matrix (Cofactor Expansion)
$$\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}$$

### Properties
- det(AB) = det(A) · det(B)
- det(Aᵀ) = det(A)
- If det(A) = 0, A is singular (no inverse)
- Swapping rows multiplies det by -1

---

## Matrix Inverse

### 2×2 Inverse
$$A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

### General Method
1. Augment [A | I]
2. Row reduce to [I | A⁻¹]

### Properties
- (AB)⁻¹ = B⁻¹A⁻¹
- (Aᵀ)⁻¹ = (A⁻¹)ᵀ

---

## Systems of Linear Equations

### Matrix Form
Ax = b

### Solutions
- Unique: det(A) ≠ 0 → x = A⁻¹b
- None: Inconsistent (parallel lines)
- Infinite: Dependent equations

### Gaussian Elimination
1. Forward elimination → row echelon form
2. Back substitution → solution

---

## Eigenvalues & Eigenvectors

### Definition
Av = λv (non-zero v)

### Finding Eigenvalues
1. Solve det(A - λI) = 0 (characteristic equation)
2. Solutions λ are eigenvalues

### Finding Eigenvectors
For each λ, solve (A - λI)v = 0

### Properties
- Sum of eigenvalues = trace(A)
- Product of eigenvalues = det(A)
- Symmetric matrices have real eigenvalues

---

## Vector Spaces

### Subspace Criteria
S is a subspace of V if:
1. Zero vector ∈ S
2. Closed under addition
3. Closed under scalar multiplication

### Key Concepts
- **Span:** Set of all linear combinations
- **Linear independence:** No vector is a combo of others
- **Basis:** Linearly independent spanning set
- **Dimension:** Number of vectors in basis
- **Rank:** Dimension of column space

# Mechanics Problems Reference

Step-by-step approaches for common mechanics problem types.

## Kinematics Problems

### Type 1: Constant Acceleration

**Steps:**
1. List: v₀, v, a, x, t (identify 3 knowns)
2. Select equation based on missing variable
3. Solve for unknown

**Equation Selection:**
| Missing | Use Equation |
|---------|-------------|
| t | v² = v₀² + 2ax |
| x | v = v₀ + at |
| v | x = v₀t + ½at² |
| a | x = ½(v₀ + v)t |
| v₀ | x = vt - ½at² |

### Type 2: Projectile Motion

**Separate into x and y components:**

| Component | Equations |
|-----------|-----------|
| x (horizontal) | x = v₀ₓt, vₓ = v₀ₓ |
| y (vertical) | y = v₀ᵧt - ½gt², vᵧ = v₀ᵧ - gt |

**Initial components:**
- v₀ₓ = v₀ cos θ
- v₀ᵧ = v₀ sin θ

**Key formulas:**
- Range: R = (v₀² sin 2θ) / g
- Max height: H = (v₀² sin² θ) / 2g
- Time of flight: T = (2v₀ sin θ) / g

---

## Force Problems

### Type 1: Objects on Flat Surface

```
       N
       ↑
   f ←─┼→ F
       ↓
       W
```

**Equations:**
- x: F - f = ma
- y: N - W = 0, so N = mg

### Type 2: Inclined Plane

```
        N
        ↑
    ╲   │  ╱ F (parallel to incline)
     ╲  │ ╱
      ╲ │╱
       ╲│
        ● ←── Object
       ╱│
      ╱θ│
     ╱  ↓
    ╱   W
```

**Components of weight:**
- W∥ = mg sin θ (down the incline)
- W⊥ = mg cos θ (into the incline)

**Equations:**
- Parallel: F - f - mg sin θ = ma
- Perpendicular: N - mg cos θ = 0

### Type 3: Connected Objects (Atwood Machine)

**Two masses on a pulley:**
- m₁: m₁g - T = m₁a
- m₂: T - m₂g = m₂a
- Solve: a = (m₁ - m₂)g / (m₁ + m₂)

---

## Energy Problems

### Type 1: Work-Energy Theorem

$$W_{net} = \Delta KE = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2$$

### Type 2: Conservation of Energy

$$KE_i + PE_i = KE_f + PE_f$$

**With friction:**
$$KE_i + PE_i = KE_f + PE_f + W_{friction}$$
$$W_{friction} = f \cdot d = \mu mg d$$

### Type 3: Springs

$$\frac{1}{2}mv^2 + mgh + \frac{1}{2}kx^2 = \text{constant}$$

---

## Momentum Problems

### Type 1: Elastic Collision (1D)

Momentum conserved: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'
KE conserved: ½m₁v₁² + ½m₂v₂² = ½m₁v₁'² + ½m₂v₂'²

**Special case (m₂ at rest):**
- v₁' = [(m₁ - m₂)/(m₁ + m₂)]v₁
- v₂' = [2m₁/(m₁ + m₂)]v₁

### Type 2: Inelastic Collision

Momentum conserved, KE NOT conserved
**Perfectly inelastic:** Objects stick together
- m₁v₁ + m₂v₂ = (m₁ + m₂)v'

### Type 3: Explosion (Reverse Inelastic)

Initial: 0 momentum (at rest)
Final: m₁v₁ + m₂v₂ = 0
So: v₁ = -(m₂/m₁)v₂

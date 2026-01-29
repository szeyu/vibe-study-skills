# Electromagnetism Reference

Key concepts and problem approaches for electricity and magnetism.

## Electric Fields

### Point Charge

$$E = k\frac{Q}{r^2}$$

Direction: Away from (+), toward (-)

### Multiple Charges

Vector sum: E⃗_total = E⃗₁ + E⃗₂ + ...

### Field Lines

- Start on (+), end on (-)
- Never cross
- Density indicates field strength

---

## Electric Potential

$$V = k\frac{Q}{r}$$
$$V = \frac{PE}{q}$$
$$\Delta V = -\int E \cdot dr$$

**Potential difference:**
$$\Delta V = V_B - V_A = -E \cdot d \text{ (uniform field)}$$

---

## Capacitors

$$C = \frac{Q}{V}$$
$$C = \varepsilon_0 \frac{A}{d} \text{ (parallel plate)}$$
$$U = \frac{1}{2}CV^2 = \frac{1}{2}\frac{Q^2}{C}$$

### Combinations

| Type | Capacitance | Charge | Voltage |
|------|-------------|--------|---------|
| Series | 1/C = 1/C₁ + 1/C₂ | Same | Divides |
| Parallel | C = C₁ + C₂ | Divides | Same |

---

## DC Circuits

### Ohm's Law

$$V = IR$$

### Resistor Combinations

| Type | Resistance | Current | Voltage |
|------|------------|---------|---------|
| Series | R = R₁ + R₂ | Same | Divides |
| Parallel | 1/R = 1/R₁ + 1/R₂ | Divides | Same |

### Kirchhoff's Laws

**Junction Rule:** ΣI_in = ΣI_out
**Loop Rule:** ΣV = 0 around any closed loop

### Power

$$P = IV = I^2R = \frac{V^2}{R}$$

---

## Magnetism

### Magnetic Force on Charge

$$F = qv \times B = qvB\sin\theta$$

Right-hand rule: Fingers point v → curl toward B → thumb points F (for +q)

### Force on Current-Carrying Wire

$$F = IL \times B = BIL\sin\theta$$

### Magnetic Field Sources

**Long straight wire:**
$$B = \frac{\mu_0 I}{2\pi r}$$

**Loop center:**
$$B = \frac{\mu_0 I}{2R}$$

**Solenoid:**
$$B = \mu_0 n I$$

---

## Electromagnetic Induction

### Faraday's Law

$$\varepsilon = -\frac{d\Phi_B}{dt}$$

Where Φ_B = BA cos θ

### Lenz's Law

Induced current opposes the change that caused it.

### Motional EMF

$$\varepsilon = BLv$$

For a rod of length L moving at velocity v through field B.

---

## Problem-Solving Patterns

### Circuit Problems

1. Identify series/parallel combinations
2. Simplify circuit step by step
3. Find total current from V = IR
4. Work backwards for individual currents/voltages

### Magnetic Force Problems

1. Identify velocity direction and magnetic field direction
2. Apply right-hand rule
3. Use F = qvB sin θ
4. Remember: F ⊥ both v and B

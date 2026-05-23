---
type: exercise
subject: thermodynamics
difficulty: "⭐⭐"
prereqs:
  - "Def - Adiabatic Process and Adiabatic Distribution"
  - "Def - Heat 1-Form and Work 1-Form"
  - "Def - The First Law of Thermodynamics"
tags: [physics, thermodynamics, ideal-gas, adiabatic]
---

# Problem Statement

For a simple ideal gas with $U = (f/2) nRT$ and equation of state $pV = nRT$, derive the **adiabatic equation of state**:

$$pV^\gamma = \text{const}, \quad \text{where} \quad \gamma := \frac{C_p}{C_V} = \frac{f + 2}{f}.$$

Equivalently, $TV^{\gamma - 1} = \text{const}$ and $T^\gamma p^{1 - \gamma} = \text{const}$.

**Strategy:**

1. Set $\delta Q = 0$ in the heat 1-form $\delta Q = (f/2)nR\, dT + (nRT/V)\, dV$ to get the ODE for adiabatic curves in $(V, T)$ coordinates.
2. Separate variables and integrate.
3. Convert to $(p, V)$ coordinates using $pV = nRT$.
4. Identify $\gamma = C_p/C_V$ and verify the relation $\gamma = (f + 2)/f$ for an ideal gas with $f$ degrees of freedom.

**Recall:**

[[Def - Adiabatic Process and Adiabatic Distribution|Adiabatic processes]] satisfy $\delta Q = 0$ along the path. The adiabatic distribution is $\ker \delta Q$, a line field on the 2-dimensional ideal-gas state space.

For an ideal gas, $\delta Q = (f/2)nR\, dT + (nRT/V)\, dV$ in $(V, T)$ coordinates (from [[Ex - The Heat 1-Form for an Ideal Gas]]).

The [[Def - Thermodynamic Potential (U, H, F, G)|heat capacities]] are $C_V = (f/2) nR$ and $C_p = C_V + nR = (f/2 + 1) nR$, with ratio $\gamma = C_p/C_V = (f + 2)/f$.

---

# Convergent Strategy

**Problem class:** An ODE-derivation problem of the type "find the integral curves of a vector field / kernel of a 1-form". The recurring pattern: set the constraining 1-form to zero, separate variables, integrate, identify constants.

**Assumption pattern:** Ideal-gas equation of state and constant heat capacities. These give the explicit form of $\delta Q$ that can be integrated to find the adiabats.

**Theorem routing:** Setting $\delta Q = 0$ in the explicit ideal-gas heat form gives the ODE $(f/2)nR\, dT + (nRT/V)\, dV = 0$, which separates to $dT/T + (2/f)\, dV/V = 0$, integrating to $\log T + (2/f) \log V = \text{const}$, equivalently $TV^{2/f} = \text{const}$.

**Key decision point:** The non-obvious choice is to *separate variables* in $(V, T)$ coordinates rather than try to express the adiabat in $(p, V)$ coordinates directly (which would be more complicated). Once the adiabat is found in $(V, T)$, conversion to $(p, V)$ via $pV = nRT$ is algebraic and produces the familiar $pV^\gamma = \text{const}$ form.

---

# Legal Operations Used

1. **Operation 6 from the topic page (integrate along an adiabat).** Set $\delta Q = 0$ in the explicit heat form to obtain the adiabatic ODE.

2. **Operation 1 from the topic page (split a 1-form using the first law).** The heat form $\delta Q = dU + p\, dV$ for an ideal gas leads to the adiabatic constraint $dU + p\, dV = 0$, i.e., $-dU = \delta W$ along the adiabat (work done at the expense of internal energy).

3. **Operation 3 from the topic page (restrict 1-forms to processes).** Restrict the heat form to the adiabatic curve, where it vanishes.

---

# Hints

> [!note]- Hint 1
> Start with the heat 1-form $\delta Q = (f/2)nR\, dT + (nRT/V)\, dV$ and set $\delta Q = 0$ on the adiabat. Divide both sides by $T$ (since $T \neq 0$): $(f/2)nR\, dT/T + nR\, dV/V = 0$.

> [!note]- Hint 2
> Separate variables and integrate: $(f/2) d(\log T) + d(\log V) = 0$, hence $(f/2) \log T + \log V = \text{const}$. Exponentiate: $T^{f/2} V = \text{const}$, equivalently $TV^{2/f} = \text{const}$.

> [!note]- Hint 3
> Convert to $(p, V)$: use $T = pV/(nR)$ to substitute. Then $T^{f/2} V = (pV)^{f/2} V / (nR)^{f/2}$, so $(pV)^{f/2} V = \text{const}$, equivalently $p^{f/2} V^{f/2 + 1} = \text{const}$, equivalently $p V^{(f+2)/f} = \text{const}$ (taking the $f/2$-th root). Set $\gamma = (f+2)/f$ for the adiabatic exponent.

> [!note]- Hint 4
> Verify $\gamma = C_p/C_V$: with $C_V = (f/2)nR$ and $C_p = (f/2 + 1)nR = ((f+2)/2) nR$, the ratio is $C_p/C_V = (f+2)/f = \gamma$ as claimed. So the adiabatic exponent is *exactly* the ratio of heat capacities.

---

# Solution

The proof is in four computational steps. Step 1 sets $\delta Q = 0$ and separates variables. Step 2 integrates to find the adiabat in $(V, T)$ coordinates. Step 3 converts to $(p, V)$ coordinates. Step 4 verifies $\gamma = C_p/C_V$. The non-obvious move is in Step 2's exponentiation, where the linear combination of logarithms becomes a product relation $T^{f/2} V = \text{const}$.

**Step 1: $\delta Q = 0$ separates to $dT/T = -(2/f) dV/V$.**

> [!note]- Derivation
> Start from $\delta Q = (f/2)nR\, dT + (nRT/V)\, dV = 0$ along the adiabat. Divide by $T$ (nonzero):
> $$(f/2)nR \frac{dT}{T} + nR \frac{dV}{V} = 0.$$
> Divide by $nR$ and rearrange:
> $$\frac{f}{2} \frac{dT}{T} = -\frac{dV}{V} \quad \Rightarrow \quad \frac{dT}{T} = -\frac{2}{f} \frac{dV}{V}.$$

**Step 2: Integration gives $TV^{2/f} = \text{const}$.**

> [!note]- Derivation
> Integrate both sides: $\log T = -(2/f) \log V + C_0$, hence $\log T + (2/f) \log V = C_0$. Exponentiate:
> $$T V^{2/f} = e^{C_0} = \text{const}.$$
> Equivalently, $T = \text{const} \cdot V^{-2/f}$ — temperature decreases on expansion in an adiabatic process, as physically expected (energy converts to work).

**Step 3: Conversion to $(p, V)$ gives $pV^\gamma = \text{const}$ with $\gamma = (f+2)/f$.**

> [!note]- Derivation
> Substitute $T = pV/(nR)$:
> $$\frac{pV}{nR} \cdot V^{2/f} = \text{const} \quad \Rightarrow \quad p V^{1 + 2/f} = \text{const} \cdot nR = \text{const}.$$
> Set $\gamma = 1 + 2/f = (f + 2)/f$:
> $$\boxed{p V^\gamma = \text{const}, \quad \gamma = \frac{f + 2}{f}.}$$
> For $f = 3$ (monatomic gas: helium, neon, argon), $\gamma = 5/3 \approx 1.67$. For $f = 5$ (diatomic gas at moderate $T$: nitrogen, oxygen), $\gamma = 7/5 = 1.4$. For $f = 6$ (polyatomic gas at high $T$ with full vibrational modes), $\gamma \approx 4/3$.

**Step 4: Verify $\gamma = C_p/C_V$.**

> [!note]- Derivation
> $C_V = (\partial U/\partial T)_V = (f/2) nR$ (since $U = (f/2)nRT$).
>
> $C_p = (\partial H/\partial T)_p = (\partial(U + pV)/\partial T)_p = (\partial U/\partial T) + (\partial(nRT)/\partial T)_p = (f/2)nR + nR = ((f+2)/2) nR$ (using $pV = nRT$ for an isobaric process).
>
> Ratio: $C_p / C_V = ((f+2)/2) nR \big/ ((f/2) nR) = (f+2)/f = \gamma$. So the adiabatic exponent equals the heat-capacity ratio, as expected.

> [!note]- Complete formal solution
> *Step 1:* Set $\delta Q = (f/2)nR\, dT + (nRT/V)\, dV = 0$. Separate: $(f/2) dT/T = -dV/V$.
>
> *Step 2:* Integrate: $\log T^{f/2} + \log V = \text{const}$, hence $T^{f/2} V = \text{const}$, equivalently $TV^{2/f} = \text{const}$.
>
> *Step 3:* Substitute $T = pV/(nR)$: $pV^{1 + 2/f} = \text{const}$, i.e.,
> $$\boxed{pV^\gamma = \text{const}, \quad \gamma = (f+2)/f.}$$
>
> *Step 4:* Verify $\gamma = C_p/C_V = ((f+2)/f)$ using $C_V = (f/2)nR$ and $C_p = ((f+2)/2)nR$.

---

# Key Takeaways

**The adiabatic equation of state $pV^\gamma = \text{const}$ is steeper than the isothermal $pV = \text{const}$.** Since $\gamma > 1$, an adiabatic curve in $(p, V)$ falls more steeply than an isotherm: as $V$ increases, $p$ drops faster on the adiabat. Geometrically this means the Carnot cycle (two isotherms and two adiabats) is a closed quadrilateral where adiabats are steeper than isotherms, with $V_1 < V_4$ and $V_2 < V_3$ as in the standard picture. This steepness reflects that an adiabatic expansion both reduces pressure (because volume increases) *and* reduces temperature (because work is done at the expense of internal energy), whereas an isothermal expansion has temperature held fixed (so the pressure drops only due to the equation-of-state $p \propto 1/V$ scaling). The trigger-reaction pattern is "see "adiabatic ideal gas" → use $pV^\gamma = \text{const}$".

**The heat capacity ratio $\gamma$ is a measurable diagnostic of molecular structure.** The value of $\gamma$ depends only on the number of accessible degrees of freedom $f$ of the molecule. Experimentally measured $\gamma$ values for various gases:
- Monatomic (He, Ne, Ar): $\gamma \approx 1.67 = 5/3$, $f = 3$ (translational only).
- Diatomic at room $T$ (N₂, O₂): $\gamma \approx 1.40 = 7/5$, $f = 5$ (3 translational + 2 rotational).
- Diatomic at high $T$ where vibrations activate: $\gamma$ drops to about $1.29 = 9/7$, $f = 7$.
- Polyatomic complex molecules: $\gamma$ approaches 1 as $f \to \infty$.
Measuring $\gamma$ via adiabatic processes (e.g., sound velocity in the gas, since speed of sound $\propto \sqrt{\gamma p/\rho}$) gives direct experimental access to $f$ — one of the historical routes by which kinetic theory was validated.

**The adiabat is the integral curve of the line distribution $\ker \delta Q$ on the 2D ideal-gas state space.** On a 2-manifold, every 1-form is automatically integrable (the Frobenius obstruction is a 3-form on a 2-manifold, hence trivially zero). So the existence of adiabats as 1-dimensional integral curves of $\ker \delta Q$ is automatic — and the explicit form $pV^\gamma = \text{const}$ is the integral. For higher-dimensional state spaces (multi-component systems), the integrability of $\ker \delta Q$ is non-trivial and is the geometric content of Caratheodory's principle (see [[Thm - The Heat 1-Form is Integrable]]). The ideal-gas case is the simplest illustration where the abstract theorem produces the concrete adiabatic equation of state used throughout introductory thermodynamics.

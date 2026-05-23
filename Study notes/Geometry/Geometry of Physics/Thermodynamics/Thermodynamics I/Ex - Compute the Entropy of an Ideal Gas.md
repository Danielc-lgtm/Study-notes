---
type: exercise
subject: thermodynamics
difficulty: "⭐⭐"
prereqs:
  - "Def - Heat 1-Form and Work 1-Form"
  - "Def - Absolute Temperature and Entropy"
  - "Def - Thermodynamic Potential (U, H, F, G)"
  - "Thm - The Heat 1-Form is Integrable"
tags: [physics, thermodynamics, ideal-gas, entropy]
---

# Problem Statement

For a simple ideal gas of $n$ moles with $f$ molecular degrees of freedom (equation of state $pV = nRT$, internal energy $U = (f/2) nRT$), compute the entropy $S$ as a function of $(T, V)$ from the relation $dS = \delta Q / T$.

1. Express $dS$ in $(T, V)$ coordinates using the first law and the equation of state.
2. Integrate $dS$ to obtain $S(T, V)$ up to an additive constant.
3. Convert to $(T, p)$ coordinates using $V = nRT/p$.
4. Verify that the additive constant cannot be determined within classical thermodynamics, and comment on how the **third law of thermodynamics** ($S \to 0$ as $T \to 0$ for a perfect crystal) fixes it (when applicable), while the statistical-mechanical $S = k_B \log W$ provides an absolute definition for the ideal gas via the **Sackur-Tetrode equation**.

**Recall:**

The [[Def - Heat 1-Form and Work 1-Form|heat 1-form]] for an ideal gas in $(V, T)$ coordinates is
$$\delta Q = (f/2) nR\, dT + \frac{nRT}{V}\, dV$$
(see [[Ex - The Heat 1-Form for an Ideal Gas]]).

The [[Def - Absolute Temperature and Entropy|absolute temperature and entropy]] satisfy $\delta Q = T\, dS$ for quasistatic reversible processes, with $S$ defined up to an additive constant. The relation $dS = \delta Q/T$ gives the entropy gradient.

The [[Def - Thermodynamic Potential (U, H, F, G)|heat capacity at constant volume]] is $C_V := (\partial U/\partial T)_V$. For an ideal gas, $C_V = (f/2) nR$.

---

# Convergent Strategy

**Problem class:** This is a state-function computation: integrate a known exact 1-form $dS$ to recover $S$. The recurring pattern is: (i) write down $dS$ in the chosen coordinates, (ii) check exactness (already known from the existence of an integrating factor), (iii) integrate piecewise — along one coordinate direction holding others fixed, then along the next, accumulating the antiderivative.

**Assumption pattern:** The ideal gas equation of state and the formula $U = (f/2)nRT$ are given. The integrating factor $T$ for $\delta Q$ is known (it is the absolute temperature; see [[Ex - The Heat 1-Form for an Ideal Gas]]), so $\delta Q/T$ is exact and integrable. The state space is 2-dimensional, so exactness of $\delta Q/T$ is equivalent to being a differential of a function.

**Theorem routing:** [[Thm - The Heat 1-Form is Integrable|Caratheodory's theorem]] guarantees the existence of $S$ with $dS = \delta Q/T$; the present exercise *computes* $S$ explicitly for the ideal gas. The route is: substitute the explicit $\delta Q$ into $\delta Q/T$, integrate the resulting exact 1-form by recognising $dT/T = d(\log T)$ and $dV/V = d(\log V)$, write the answer up to an additive constant.

**Key decision point:** The non-obvious choice is the *coordinates* in which to integrate. In $(T, V)$ the integration is clean because $\delta Q/T$ separates: $(f/2) nR\, d\log T + nR\, d\log V$ integrates by inspection. In other coordinates (say $(T, p)$ or $(U, V)$) the integration is more complex. Choosing $(T, V)$ first and then converting to $(T, p)$ via the equation of state is the natural workflow, and it makes the structure $S = C_V \log T + nR \log V$ visible.

---

# Legal Operations Used

1. **Operation 1 from the topic page (split a 1-form using the first law).** The heat form $\delta Q = (f/2) nR\, dT + (nRT/V)\, dV$ is obtained by applying $\delta Q = dU + p\, dV$ to the ideal-gas equations.

2. **Operation 4 from the topic page (use closedness on a potential).** The differential $dS$ is exact (being a differential of $S$), so it can be integrated piecewise along coordinate directions without worrying about path-dependence — this is what the exactness criterion guarantees.

3. **Operation 8 from the topic page (test exactness via cross-partials).** Verify that $dS = (f/2)(nR/T)\, dT + (nR/V)\, dV$ has equal cross-partials: $\partial/\partial V[(f/2)nR/T] = 0$ and $\partial/\partial T[nR/V] = 0$. Both zero, so equality holds: $dS$ is exact, confirming the existence of $S$.

---

# Hints

> [!note]- Hint 1
> Start by writing $dS = \delta Q/T$ explicitly. From $\delta Q = (f/2) nR\, dT + (nRT/V)\, dV$, dividing by $T$ gives $dS = (f/2)(nR/T)\, dT + (nR/V)\, dV$. The $T$ in the second term cancels with the $T$ in the denominator.

> [!note]- Hint 2
> Recognise the standard differentials: $dT/T = d(\log T)$ and $dV/V = d(\log V)$. So $dS = (f/2) nR\, d(\log T) + nR\, d(\log V)$.

> [!note]- Hint 3
> Integrate: $S = (f/2) nR \log T + nR \log V + S_0$ where $S_0$ is an additive constant. Verify by differentiating back.

> [!note]- Hint 4
> To convert to $(T, p)$ coordinates, use $V = nRT/p$, so $\log V = \log(nRT) - \log p = \log T + \log(nR) - \log p$. Substitute and collect:
> $$S = (f/2) nR \log T + nR(\log T + \log(nR) - \log p) + S_0 = (f/2 + 1) nR \log T - nR \log p + \text{const}.$$
> Note $(f/2 + 1) nR = C_p$, the heat capacity at constant pressure.

---

# Solution

The proof breaks into four steps. Step 1 substitutes the heat form into $\delta Q/T$ and verifies exactness. Step 2 integrates by recognising the logarithmic standard differentials. Step 3 converts to $(T, p)$ coordinates using the equation of state. Step 4 addresses the additive constant and the third law. The non-obvious move is in Step 3, where the conversion produces $C_p$ in front of $\log T$ — reflecting that at constant pressure (rather than constant volume), the effective heat capacity governing the temperature-dependence of entropy is $C_p$, not $C_V$.

**Step 1: $dS$ in $(T, V)$ coordinates, and exactness verification.**

> [!note]- Derivation
> From $\delta Q = (f/2) nR\, dT + (nRT/V)\, dV$, divide by $T$:
> $$dS = \frac{\delta Q}{T} = \frac{f}{2}\frac{nR}{T}\, dT + \frac{nR}{V}\, dV.$$
> The coefficients are $a(T, V) = nR/V$ (of $dV$) and $b(T, V) = (f/2)nR/T$ (of $dT$). Cross-partials: $\partial a/\partial T = 0$ and $\partial b/\partial V = 0$. They agree, so $dS$ is exact (= closed on the 2-manifold).

**Step 2: Integrate to obtain $S(T, V)$.**

> [!note]- Derivation
> Use $dT/T = d(\log T)$ and $dV/V = d(\log V)$:
> $$dS = (f/2) nR\, d(\log T) + nR\, d(\log V) = d\left[(f/2) nR \log T + nR \log V\right].$$
> So
> $$S(T, V) = (f/2) nR \log T + nR \log V + S_0$$
> where $S_0$ is an additive constant. Verify by differentiating: $\partial S/\partial T = (f/2)nR/T = b$, $\partial S/\partial V = nR/V = a$. Confirmed.
>
> Equivalently, using $C_V = (f/2) nR$:
> $$S(T, V) = C_V \log T + nR \log V + S_0.$$

**Step 3: Convert to $(T, p)$ coordinates.**

> [!note]- Derivation
> Substitute $V = nRT/p$:
> $$\log V = \log(nRT/p) = \log(nR) + \log T - \log p.$$
> So
> $$S(T, p) = C_V \log T + nR\left[\log(nR) + \log T - \log p\right] + S_0 = (C_V + nR) \log T - nR \log p + S_0',$$
> where $S_0' = S_0 + nR \log(nR)$ absorbs the constant.
>
> The combination $C_V + nR$ equals the heat capacity at constant pressure for an ideal gas: $C_p = (f/2 + 1) nR = C_V + nR$ (Mayer's relation, derivable from the first law applied to an isobaric process). So
> $$\boxed{S(T, p) = C_p \log T - nR \log p + \text{const}.}$$
> The structure is symmetric to the $(T, V)$ case: a heat-capacity-times-$\log T$ term plus a mechanical-coefficient-times-$\log(\text{other variable})$ term, with the sign of the latter flipping when we swap $V \to p$ (consistent with the differential $dG = -S\, dT + V\, dp$ having opposite sign to $dF = -S\, dT - p\, dV$).

**Step 4: The additive constant and the third law.**

> [!note]- Derivation
> The constant $S_0$ (or $S_0'$) in the entropy is *not determined* by Caratheodory's theorem or by the first/second laws. The theorem produces an integrating factor and integral, but the integral is defined only up to an additive constant — physically, this reflects that thermodynamics deals with *differences* $\Delta S$ between states, not absolute entropies.
>
> The **third law of thermodynamics** (Nernst's heat theorem, in Planck's formulation) attempts to fix this: as $T \to 0$, the entropy of a perfect crystal approaches a universal constant (often taken as zero). This determines $S_0$ for crystalline solids and many other condensed phases. For an *ideal* gas, however, the third law gives a divergent answer at $T \to 0$ (since $\log T \to -\infty$), reflecting that ideal gases are unphysical at very low temperatures — they would form a Bose-Einstein or Fermi-Dirac quantum gas, and the classical formula fails.
>
> Statistical mechanics provides an absolute value via the **Sackur-Tetrode equation**: for a monatomic ideal gas with $N$ particles,
> $$S = N k_B \log\left[\frac{V}{N}\left(\frac{4 \pi m k_B T}{3 h^2}\right)^{3/2}\right] + \frac{5}{2} N k_B,$$
> where $h$ is Planck's constant and $m$ is the particle mass. The constant $5/2 N k_B$ (and the precise form of the argument of the log) comes from Boltzmann's $S = k_B \log W$ applied to a quantum-mechanical counting of microstates. The classical Caratheodory formula $S = C_V \log T + nR \log V + S_0$ recovers the Sackur-Tetrode equation in the appropriate limit, with the constant $S_0$ identified explicitly.

> [!note]- Complete formal solution
> *Step 1:* Write $dS = \delta Q/T$ using $\delta Q = (f/2) nR\, dT + (nRT/V)\, dV$:
> $$dS = \frac{f}{2}\frac{nR}{T}\, dT + \frac{nR}{V}\, dV = C_V\, \frac{dT}{T} + nR\, \frac{dV}{V}.$$
> Verify exactness: cross-partials $\partial(nR/V)/\partial T = 0 = \partial(C_V/T)/\partial V$.
>
> *Step 2:* Integrate using $dT/T = d(\log T)$ and $dV/V = d(\log V)$:
> $$\boxed{S(T, V) = C_V \log T + nR \log V + S_0,}$$
> with $C_V = (f/2) nR$ and $S_0$ an additive constant.
>
> *Step 3:* Convert to $(T, p)$ using $V = nRT/p$:
> $$S(T, p) = (C_V + nR)\log T - nR \log p + S_0' = C_p \log T - nR \log p + S_0',$$
> where $C_p = C_V + nR$ and $S_0' = S_0 + nR \log(nR)$.
>
> *Step 4:* The constant $S_0$ is not fixed by classical thermodynamics. The third law (Nernst) sets $S \to 0$ as $T \to 0$ for a perfect crystal; for an ideal gas this limit diverges classically (signalling the breakdown of the ideal-gas approximation at very low $T$), and the absolute value is provided instead by the Sackur-Tetrode equation from statistical mechanics, which counts quantum microstates.

---

# Key Takeaways

**The entropy formula $S = C_V \log T + nR \log V$ is a paradigm for many systems.** Whenever the heat capacity is approximately constant (over the temperature range of interest), the entropy as a function of temperature has the form $S \sim C \log T + (\text{constant})$ — the logarithm of temperature scaled by the heat capacity. For more general substances, the heat capacity itself is temperature-dependent ($C_V = C_V(T)$), and the entropy is $S(T) = \int_0^T (C_V(T')/T')\, dT' + S(0)$ — but the structure "heat capacity divided by temperature, integrated" persists. This trigger-reaction pattern ("compute entropy from heat capacity") is the standard approach for any substance where the heat capacity is tabulated or measurable.

**The conversion $S(T, V) \to S(T, p)$ replaces $C_V$ by $C_p$ in front of $\log T$.** This is a substantive change reflecting that the relevant heat capacity governing temperature-dependence of entropy depends on which variable is held constant. At constant volume, only $C_V$ matters; at constant pressure, the system also does $p\, dV$ work on its surroundings during heating, requiring extra heat — hence the larger $C_p = C_V + nR$. The formula $S = C_p \log T - nR \log p + \text{const}$ at constant pressure reflects this: more heat per kelvin at constant pressure, more entropy per kelvin. This is the trigger for recognising whether $C_p$ or $C_V$ is the right coefficient — it depends on which other variable is held constant in the entropy expression.

**The additive constant in entropy is the bridge to statistical mechanics.** Classical thermodynamics cannot determine $S_0$ from within its own axioms — Caratheodory's theorem produces $S$ only up to a constant. Setting $S_0$ requires either an external convention (third law for perfect crystals) or a microscopic calculation (Sackur-Tetrode equation from statistical mechanics). The fact that classical thermodynamics is "blind" to the additive constant is the precise sense in which it is *macroscopic* — it observes only differences. The constant encodes microscopic information about counting of microstates, which is exactly what statistical mechanics computes. Recognising this is the bridge from classical to statistical thermodynamics, and it is the entry point to **statistical mechanics**, the **Gibbs measure**, and the **Maxwell's demon and algorithmic thermodynamics** research direction where the additive constant becomes informationally meaningful.

**Companion exercise:** [[Ex - The Heat 1-Form for an Ideal Gas]] derives $\delta Q$ and shows $\lambda = T$ is the integrating factor; the present exercise then *integrates* the result to obtain $S$ explicitly. The pair gives the complete computation of "thermodynamic state functions for an ideal gas" from the first and second laws.

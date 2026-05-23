---
type: exercise
subject: thermodynamics
difficulty: "⭐"
prereqs:
  - "Def - Thermodynamic Potential (U, H, F, G)"
  - "Thm - Maxwell Relations from Closedness"
  - "Def - Closed and Exact Forms"
tags: [physics, thermodynamics, maxwell-relations]
---

# Problem Statement

Starting from the differential of the Gibbs free energy $G(T, p) = U + pV - TS$ in its natural variables $(T, p)$:

1. Verify $dG = -S\, dT + V\, dp$ by computing $dG$ from $G = U + pV - TS$ and the first/second laws.
2. Apply $d^2 G = 0$ to derive the Maxwell relation $\left(\dfrac{\partial S}{\partial p}\right)_T = -\left(\dfrac{\partial V}{\partial T}\right)_p$.
3. Define the **thermal expansion coefficient** $\alpha := V^{-1}(\partial V/\partial T)_p$. Use the Maxwell relation to express the entropy change of a gas under an isothermal compression $p_1 \to p_2$ in terms of $\alpha$, $V$, and $T$.
4. Evaluate the result explicitly for an ideal gas, and check consistency with the formula $S = C_p \log T - nR \log p + \text{const}$ from [[Ex - Compute the Entropy of an Ideal Gas]].

**Recall:**

The [[Def - Thermodynamic Potential (U, H, F, G)|Gibbs free energy]] is $G(T, p) = U + pV - TS$ with differential $dG = -S\, dT + V\, dp$. Its natural variables are $T$ and $p$.

The [[Thm - Maxwell Relations from Closedness|Maxwell relation from the Gibbs free energy]] is $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$.

The [[Def - Closed and Exact Forms|closedness condition]] $d^2 G = 0$ on any smooth function $G$ is the equality of mixed partial derivatives $\partial^2 G/(\partial T \partial p) = \partial^2 G/(\partial p \partial T)$.

---

# Convergent Strategy

**Problem class:** This is a Maxwell-relation problem of the type "derive an identity among partial derivatives via $d^2 = 0$ on the appropriate thermodynamic potential". The recurring pattern is: (i) identify the potential whose natural variables match the held-fixed variables in the partial derivatives, (ii) write down the differential of that potential, (iii) apply $d^2 = 0$ and read off the cross-partial identity, (iv) use the identity to convert hard-to-measure quantities (involving $S$) into easy-to-measure ones (involving $T, p, V$).

**Assumption pattern:** The Gibbs free energy is a smooth state function on the thermodynamic state space $M$ — this is the substantive assumption, equivalent to the first law (existence of $U$ as a state function) plus the second law (existence of $S$ as a state function). The differential $dG = -S\, dT + V\, dp$ is then immediate from the algebraic definition $G = U + pV - TS$.

**Theorem routing:** [[Def - The First Law of Thermodynamics|First law]] + [[Def - Absolute Temperature and Entropy|second law]] give $dU = T\, dS - p\, dV$. Algebraic manipulation $G = U + pV - TS$ then gives $dG = dU + V\, dp + p\, dV - T\, dS - S\, dT = -S\, dT + V\, dp$ (the $T\, dS$ and $p\, dV$ terms cancel). Then $d^2 G = 0$ (because $G$ is a smooth function, $d \circ d = 0$ on any smooth form) gives the Maxwell relation. The isothermal entropy change is computed by integrating $dS = (\partial S/\partial p)_T\, dp$ at constant $T$, using the Maxwell relation to evaluate the integrand.

**Key decision point:** The non-obvious choice is *which potential* to use. The problem asks for a relation involving $(\partial S/\partial p)_T$, with $T$ held constant. The potential whose natural variables include $T$ is $F$ or $G$ — and the one whose conjugate variable to $T$ is $S$ (so that $S$ appears as a coefficient in $dG$, hence as a cross-partial in $d^2 G = 0$) is $G$. So $G$ is the right choice. Picking $F$ instead would give the *different* Maxwell relation $(\partial S/\partial V)_T = (\partial p/\partial T)_V$, which involves $(\partial V)$-derivatives not $(\partial p)$-derivatives. The selection of potential is dictated by which "free" variable is in the target derivative.

---

# Legal Operations Used

1. **Operation 4 from the topic page (use $d^2 = 0$ on a potential).** Apply $d^2 G = 0$ to extract the Maxwell relation from $G$ — the central operation of this exercise.

2. **Operation 5 from the topic page (Legendre transform).** Implicit in writing $G = U + pV - TS$ — this is the Legendre transform of $U$ swapping both conjugate pairs $(S, T)$ and $(V, p)$, giving $G(T, p)$ with $T$ and $p$ as natural variables.

3. **Operation 8 from the topic page (recognise a state function via exactness).** The exactness of $dG$ is automatic from $G$ being a function on $M$; the Maxwell relation is the cross-partial identity of this exact differential.

---

# Hints

> [!note]- Hint 1
> To verify $dG = -S\, dT + V\, dp$: compute $dG$ from $G = U + pV - TS$:
> $$dG = dU + d(pV) - d(TS) = dU + V\, dp + p\, dV - T\, dS - S\, dT.$$
> Now substitute $dU = T\, dS - p\, dV$ from the combined first and second laws:
> $$dG = (T\, dS - p\, dV) + V\, dp + p\, dV - T\, dS - S\, dT = V\, dp - S\, dT.$$
> The $T\, dS$ and $p\, dV$ terms cancel pairwise.

> [!note]- Hint 2
> Apply $d^2 G = 0$ to $dG = -S\, dT + V\, dp$. Compute:
> $$0 = d^2 G = d(-S\, dT + V\, dp) = -dS \wedge dT + dV \wedge dp.$$
> Expand $dS$ in $(T, p)$ coordinates: $dS = (\partial S/\partial T)_p\, dT + (\partial S/\partial p)_T\, dp$. Similarly $dV = (\partial V/\partial T)_p\, dT + (\partial V/\partial p)_T\, dp$.

> [!note]- Hint 3
> Substitute the expansions of $dS$ and $dV$, and collect terms in the basis $dT \wedge dp$. Use the antisymmetry $dT \wedge dT = 0$ and $dp \wedge dp = 0$. The coefficient of $dT \wedge dp$ must vanish, giving the Maxwell relation.

> [!note]- Hint 4
> For the entropy change at constant $T$: integrate $dS = (\partial S/\partial p)_T\, dp = -(\partial V/\partial T)_p\, dp = -V\alpha\, dp$ from $p_1$ to $p_2$. The thermal expansion coefficient $\alpha$ may depend on $T$ and $p$; for a general substance the integral requires knowing $\alpha(p)$ at fixed $T$.

---

# Solution

The proof breaks into four short steps. Step 1 derives $dG$ from the definitions. Step 2 applies $d^2 G = 0$ to extract the Maxwell relation. Step 3 uses the Maxwell relation to express the isothermal entropy change in terms of the thermal expansion coefficient. Step 4 verifies the result for an ideal gas. The non-obvious move is in Step 3, where the Maxwell relation lets us substitute $(\partial V/\partial T)_p$ (measurable from the equation of state) for $(\partial S/\partial p)_T$ (hard to measure directly, since you would need to vary pressure while monitoring entropy).

**Step 1: $dG = -S\, dT + V\, dp$.**

> [!note]- Derivation
> From $G := U + pV - TS$:
> $$dG = dU + d(pV) - d(TS) = dU + V\, dp + p\, dV - T\, dS - S\, dT.$$
> Substitute $dU = T\, dS - p\, dV$ (combined first and second laws for a simple gas):
> $$dG = (T\, dS - p\, dV) + V\, dp + p\, dV - T\, dS - S\, dT.$$
> The $T\, dS$ and $-T\, dS$ cancel; the $-p\, dV$ and $+p\, dV$ cancel. Remaining:
> $$dG = -S\, dT + V\, dp.$$
> So $(\partial G/\partial T)_p = -S$ and $(\partial G/\partial p)_T = V$. These are read off as the coefficients in the differential.

**Step 2: The Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$.**

> [!note]- Derivation
> Apply $d^2 G = 0$:
> $$0 = d^2 G = d(-S\, dT + V\, dp) = -dS \wedge dT + dV \wedge dp.$$
> Expand $dS$ and $dV$ in $(T, p)$ coordinates:
> $$dS = \left(\frac{\partial S}{\partial T}\right)_p dT + \left(\frac{\partial S}{\partial p}\right)_T dp, \quad dV = \left(\frac{\partial V}{\partial T}\right)_p dT + \left(\frac{\partial V}{\partial p}\right)_T dp.$$
> Substitute:
> $$0 = -\left[(\partial S/\partial T)_p\, dT + (\partial S/\partial p)_T\, dp\right] \wedge dT + \left[(\partial V/\partial T)_p\, dT + (\partial V/\partial p)_T\, dp\right] \wedge dp.$$
> Use $dT \wedge dT = 0$ and $dp \wedge dp = 0$ to drop those terms:
> $$0 = -(\partial S/\partial p)_T\, dp \wedge dT + (\partial V/\partial T)_p\, dT \wedge dp.$$
> Use $dp \wedge dT = -dT \wedge dp$:
> $$0 = (\partial S/\partial p)_T\, dT \wedge dp + (\partial V/\partial T)_p\, dT \wedge dp = \left[(\partial S/\partial p)_T + (\partial V/\partial T)_p\right]\, dT \wedge dp.$$
> The coefficient of $dT \wedge dp$ must vanish:
> $$\boxed{\left(\frac{\partial S}{\partial p}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_p.}$$

**Step 3: Isothermal entropy change in terms of $\alpha$.**

> [!note]- Derivation
> Use the Maxwell relation: along an isothermal process at temperature $T$, $dS = (\partial S/\partial p)_T\, dp = -(\partial V/\partial T)_p\, dp$. By the definition $\alpha := V^{-1}(\partial V/\partial T)_p$, we have $(\partial V/\partial T)_p = V \alpha$, so
> $$dS = -V \alpha\, dp.$$
> Integrate from $p_1$ to $p_2$ at constant $T$:
> $$\Delta S = -\int_{p_1}^{p_2} V(T, p)\, \alpha(T, p)\, dp.$$
> For an isothermal compression ($p_2 > p_1$, gas compressed), the integrand is positive (since $V, \alpha > 0$ for most substances), so $\Delta S < 0$ — entropy decreases on compression, consistent with the intuition that compressed gases have fewer accessible microstates per volume.

**Step 4: Verification for an ideal gas.**

> [!note]- Derivation
> For an ideal gas: $pV = nRT$, so $V = nRT/p$. Compute $(\partial V/\partial T)_p = nR/p$, hence $V \alpha = (\partial V/\partial T)_p = nR/p$. So the integrand in Step 3 is $V \alpha = nR/p$, and
> $$\Delta S = -\int_{p_1}^{p_2} \frac{nR}{p}\, dp = -nR \log(p_2/p_1) = -nR \log(p_2/p_1).$$
>
> Check against the explicit ideal-gas entropy formula $S = C_p \log T - nR \log p + \text{const}$ from [[Ex - Compute the Entropy of an Ideal Gas]]. At constant $T$:
> $$\Delta S = S(T, p_2) - S(T, p_1) = -nR \log p_2 + nR \log p_1 = -nR \log(p_2/p_1).$$
> Matches. For an isothermal compression $p_2 > p_1$, both formulae give $\Delta S < 0$.
>
> So the Maxwell relation, combined with the ideal-gas equation of state, reproduces the entropy formula without integrating the heat 1-form directly — confirming the consistency of the thermodynamic formalism.

> [!note]- Complete formal solution
> *Step 1:* Differentiate $G = U + pV - TS$: $dG = dU + V\, dp + p\, dV - T\, dS - S\, dT$. Substitute $dU = T\, dS - p\, dV$: cancellation gives
> $$dG = -S\, dT + V\, dp.$$
>
> *Step 2:* Apply $d^2 G = 0$:
> $$0 = -dS \wedge dT + dV \wedge dp = \left[(\partial S/\partial p)_T + (\partial V/\partial T)_p\right]\, dT \wedge dp.$$
> Maxwell relation:
> $$\boxed{(\partial S/\partial p)_T = -(\partial V/\partial T)_p.}$$
>
> *Step 3:* Use the Maxwell relation with $\alpha := V^{-1}(\partial V/\partial T)_p$ to evaluate isothermal entropy change:
> $$\Delta S\big|_T = -\int_{p_1}^{p_2} V(T, p)\, \alpha(T, p)\, dp.$$
>
> *Step 4:* For an ideal gas $V \alpha = nR/p$, so $\Delta S = -nR \log(p_2/p_1)$, agreeing with the direct integration of the ideal-gas entropy formula at constant $T$.

---

# Key Takeaways

**Maxwell relations convert $S$-derivatives into measurable $T, p, V$-derivatives.** The hardest experimental measurements in thermodynamics involve the entropy (which has no direct meter). The Maxwell relations $(\partial S/\partial V)_T = (\partial p/\partial T)_V$ and $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ trade these for derivatives of pressure and volume with respect to temperature — which are routinely tabulated (thermal expansion coefficient $\alpha$ and isothermal compressibility $\kappa_T$). The trigger-reaction pattern is "see a partial derivative with $S$ in it → look up the corresponding Maxwell relation and rewrite". This is the most useful skill from Maxwell-relation problems, because it permits computation from experimental data without needing to measure entropy directly.

**The choice of potential is dictated by the held-constant variables.** Faced with a partial derivative like $(\partial S/\partial p)_T$, you choose $G(T, p)$ because its natural variables are exactly the held-constant variable ($T$) and the variable being differentiated against ($p$). With $G$ in hand, the Maxwell relation involving $(\partial S/\partial p)_T$ is automatic. If the held-constant variable were $V$ instead of $T$, you would use $F(T, V)$; if it were $S$ instead, $U$ or $H$. The pairing rule is: *natural variables of the potential = (held constant) + (differentiated against)*. Internalising this rule turns Maxwell-relation problems into mechanical pattern-matching.

**Verification by an alternative route is good practice.** In Step 4 we verified the Maxwell-relation-derived $\Delta S$ against direct integration of the explicit entropy formula for an ideal gas. This kind of consistency check — computing the same quantity by two genuinely different routes — catches sign errors and identifies cases where one is using the wrong potential or wrong Maxwell relation. For more complex substances, the explicit entropy formula may not be available, and the Maxwell-relation route is the only path — but the verification habit, learned on tractable cases like the ideal gas, builds confidence in the formalism.

**The thermal expansion coefficient $\alpha$ is the bridge between entropy gradients and equation-of-state data.** The combination $V \alpha = (\partial V/\partial T)_p$ appears throughout thermodynamics: in the entropy change formula above; in the Joule-Thomson coefficient $\mu_{JT} = (T(\partial V/\partial T)_p - V)/C_p = V(T\alpha - 1)/C_p$ (see [[Ex - Joule-Thomson Coefficient from Thermodynamic Identities]]); in the difference of heat capacities $C_p - C_V = TV\alpha^2/\kappa_T$. Recognising $V\alpha$ as a recurring combination — a quantity that captures how volume responds to temperature at fixed pressure — speeds up many computations and unifies the thermodynamics of expansion, throttling, and heat capacity.

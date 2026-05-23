---
type: exercise
subject: thermodynamics
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Thermodynamic Potential (U, H, F, G)"
  - "Thm - Maxwell Relations from Closedness"
  - "Def - The First Law of Thermodynamics"
tags: [physics, thermodynamics, joule-thomson, real-gas]
---

# Problem Statement

The **Joule-Thomson process** (also called the *throttling process*) is the steady-flow expansion of a gas through a porous plug or constriction, with the gas insulated from the surroundings ($\delta Q_{\text{actual}} = 0$ to the environment, but the process is *not quasistatic* — it is turbulent in the constriction). The endpoints are equilibrium states at upstream pressure $p_1$ and downstream pressure $p_2 < p_1$. For a steady flow, the *enthalpy* $H$ is unchanged: $H_1 = H_2$ — i.e., the throttling is **isenthalpic**.

The **Joule-Thomson coefficient** is the rate of temperature change with pressure at fixed enthalpy:
$$\mu_{JT} := \left(\frac{\partial T}{\partial p}\right)_H.$$

If $\mu_{JT} > 0$, the gas cools on expansion (refrigeration); if $\mu_{JT} < 0$, it heats. The temperature at which $\mu_{JT}$ changes sign (where $\mu_{JT} = 0$) is the **inversion temperature**.

1. Derive the **general formula** for $\mu_{JT}$ in terms of $T, V, p$, and the heat capacity $C_p$, using $dH = T\, dS + V\, dp$, the constraint $dH = 0$, and a Maxwell relation.
2. Show that for an ideal gas $\mu_{JT} = 0$ — ideal gases neither heat nor cool on throttling.
3. Compute $\mu_{JT}$ for a **Van der Waals gas** with equation of state $\left(p + \frac{a n^2}{V^2}\right)(V - nb) = nRT$, to leading order in the small parameters $a$ and $b$. Identify the inversion temperature.

**Recall:**

The [[Def - Thermodynamic Potential (U, H, F, G)|enthalpy]] $H(S, p)$ has differential $dH = T\, dS + V\, dp$. Its natural variables are $S$ and $p$.

The relevant [[Thm - Maxwell Relations from Closedness|Maxwell relation]] (from $G(T, p)$): $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$.

The [[Def - Thermodynamic Potential (U, H, F, G)|heat capacity at constant pressure]] is $C_p := (\partial H/\partial T)_p$. For an ideal gas, $C_p = C_V + nR$, both temperature-independent.

The **cyclic relation** for partial derivatives of three variables (a standard identity): if $f(x, y, z) = 0$ defines a surface, then
$$\left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1.$$

---

# Convergent Strategy

**Problem class:** This is a thermodynamic identity-derivation problem at upper-tier difficulty. The recurring pattern is: (i) start from the natural differential of the relevant potential ($dH$ here, since the process is isenthalpic), (ii) apply the constraint ($dH = 0$), (iii) solve for the target derivative ($\mu_{JT} = (\partial T/\partial p)_H$) using Maxwell relations to convert hard-to-measure quantities ($S$-derivatives) into easy-to-measure ones.

**Assumption pattern:** The process is isenthalpic ($dH = 0$) — this is the key constraint imposed by steady-flow throttling, derivable from energy conservation across the constriction. The process is generally not quasistatic, but the *endpoints* are equilibrium states, and $\mu_{JT}$ is defined via state-function partial derivatives at those endpoints. So the Joule-Thomson coefficient is a property of the equilibrium state, not of the process.

**Theorem routing:** Start with $dH = T\, dS + V\, dp$. Set $dH = 0$: $T\, dS = -V\, dp$, hence $dS = -(V/T)\, dp$. Then expand $dS$ in $(T, p)$ coordinates: $dS = (\partial S/\partial T)_p\, dT + (\partial S/\partial p)_T\, dp = (C_p/T)\, dT - (\partial V/\partial T)_p\, dp$ (using $C_p = T(\partial S/\partial T)_p$ and the Maxwell relation from $G$). Combining: $(C_p/T)\, dT - (\partial V/\partial T)_p\, dp = -(V/T)\, dp$, hence $(C_p/T)\, dT = \left[(\partial V/\partial T)_p - V/T\right]\, dp$, giving $\mu_{JT} = (\partial T/\partial p)_H = \left[T (\partial V/\partial T)_p - V\right]/C_p$.

**Key decision point:** The non-obvious choice is to set $dH = 0$ early and then *expand* $dS$ (which appears in $dH$) in coordinates where the Maxwell relation can be applied. The natural variables of $H$ are $(S, p)$, but $\mu_{JT}$ involves $T$, so we need to convert from $S$-coordinates to $T$-coordinates somewhere — and the most efficient place is via the chain rule on $dS$ expressed in $(T, p)$ coordinates. The Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ from $G$ is what makes the conversion clean: it replaces the $S$-derivative with a directly measurable $V$-derivative.

---

# Legal Operations Used

1. **Operation 1 from the topic page (split a 1-form using the first law).** The differential $dH = T\, dS + V\, dp$ is the second-law-modified version of the first law for enthalpy; the relation $T\, dS = \delta Q$ enters implicitly.

2. **Operation 3 from the topic page (restrict to a process).** The isenthalpic constraint $dH = 0$ restricts to the path along which the throttling occurs.

3. **Operation 4 from the topic page (use $d^2 = 0$ on a potential).** The Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ from $G$ is what converts the hard-to-measure $S$-derivative in the expansion of $dS$ to a measurable $V$-derivative.

4. **Operation 5 from the topic page (Legendre transform).** The enthalpy $H = U + pV$ is the Legendre transform of $U$ swapping $V \leftrightarrow p$ — this is what makes $H$ the natural potential for processes at fixed $p$ (or isenthalpic processes here).

---

# Hints

> [!note]- Hint 1
> Start with the differential of $H$: $dH = T\, dS + V\, dp$. Set $dH = 0$ for the isenthalpic process. This gives $T\, dS = -V\, dp$, or $dS = -(V/T)\, dp$.

> [!note]- Hint 2
> Now express $dS$ another way using $T$ and $p$ as independent variables (since you want $(\partial T/\partial p)_H$ at the end). The chain rule on $S(T, p)$ gives $dS = (\partial S/\partial T)_p\, dT + (\partial S/\partial p)_T\, dp$. Use $C_p = T(\partial S/\partial T)_p$ and the Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$.

> [!note]- Hint 3
> Equate the two expressions for $dS$: $(C_p/T)\, dT - (\partial V/\partial T)_p\, dp = -(V/T)\, dp$. Solve for $dT/dp$ along the isenthalpic path (i.e., at $dH = 0$): rearrange to isolate $dT$, divide by $dp$.

> [!note]- Hint 4
> For Step 2 (ideal gas): use $V = nRT/p$, so $(\partial V/\partial T)_p = nR/p$ and $T(\partial V/\partial T)_p = nRT/p = V$. The formula gives $\mu_{JT} = (V - V)/C_p = 0$. Ideal gases neither heat nor cool on throttling.
>
> For Step 3 (Van der Waals gas), expand the equation of state $\left(p + an^2/V^2\right)(V - nb) = nRT$ to leading order in $a, b$, solve for $V$ in terms of $T, p$, compute $(\partial V/\partial T)_p$, and substitute into the general formula. The leading correction to $\mu_{JT}$ is positive (gas cools) at low $T$ and negative (gas heats) at high $T$; the crossover defines the inversion temperature.

---

# Solution

The proof breaks into three substantial steps. Step 1 derives the general formula $\mu_{JT} = [T(\partial V/\partial T)_p - V]/C_p$. Step 2 specialises to the ideal gas, where the bracketed term vanishes. Step 3 computes the leading correction for a Van der Waals gas, identifying the inversion temperature. The non-obvious move is in Step 1, where the Maxwell relation from $G$ replaces $(\partial S/\partial p)_T$ by $-(\partial V/\partial T)_p$ — exchanging an immeasurable entropy gradient for a measurable thermal-expansion coefficient.

**Step 1: General formula $\mu_{JT} = [T(\partial V/\partial T)_p - V]/C_p$.**

> [!note]- Derivation
> Start from $dH = T\, dS + V\, dp$ and the constraint $dH = 0$ (isenthalpic):
> $$0 = T\, dS + V\, dp \quad \Rightarrow \quad dS = -\frac{V}{T}\, dp. \tag{i}$$
>
> Now express $dS$ via the chain rule in $(T, p)$ coordinates:
> $$dS = \left(\frac{\partial S}{\partial T}\right)_p\, dT + \left(\frac{\partial S}{\partial p}\right)_T\, dp = \frac{C_p}{T}\, dT - \left(\frac{\partial V}{\partial T}\right)_p\, dp, \tag{ii}$$
> where we used $C_p = T(\partial S/\partial T)_p$ (definition of $C_p$) and the Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ (from $G$).
>
> Equate (i) and (ii):
> $$\frac{C_p}{T}\, dT - \left(\frac{\partial V}{\partial T}\right)_p\, dp = -\frac{V}{T}\, dp.$$
> Rearrange:
> $$\frac{C_p}{T}\, dT = \left[\left(\frac{\partial V}{\partial T}\right)_p - \frac{V}{T}\right]\, dp = \frac{1}{T}\left[T\left(\frac{\partial V}{\partial T}\right)_p - V\right]\, dp.$$
> Hence:
> $$\boxed{\mu_{JT} := \left(\frac{\partial T}{\partial p}\right)_H = \frac{T(\partial V/\partial T)_p - V}{C_p}.}$$
> The sign of $\mu_{JT}$ is determined by the sign of $T(\partial V/\partial T)_p - V$.

**Step 2: Ideal gas gives $\mu_{JT} = 0$.**

> [!note]- Derivation
> For an ideal gas, $pV = nRT$, so $V = nRT/p$. Compute $(\partial V/\partial T)_p = nR/p$. Then $T(\partial V/\partial T)_p = T \cdot nR/p = nRT/p = V$.
>
> So $T(\partial V/\partial T)_p - V = V - V = 0$, giving $\mu_{JT} = 0/C_p = 0$.
>
> An ideal gas, throttled through a porous plug, undergoes no temperature change. This is a consequence of the ideal-gas property that $U$ (and hence $H$) depends only on $T$ — so isenthalpic = isothermal for an ideal gas. The physical reason: in an ideal gas the molecules do not interact except by collisions, so expansion does no work against intermolecular forces, and the kinetic energy distribution (which determines $T$) is unchanged.

**Step 3: Van der Waals gas — leading-order $\mu_{JT}$ and inversion temperature.**

> [!note]- Derivation
> The Van der Waals equation $\left(p + an^2/V^2\right)(V - nb) = nRT$ corrects the ideal gas for (i) molecular volume $b$ (the "co-volume", reducing the effective volume from $V$ to $V - nb$) and (ii) intermolecular attraction $a$ (reducing the effective pressure by $an^2/V^2$).
>
> Expand to leading order in $a, b$: write $V = V_0 + \delta V$ where $V_0 = nRT/p$ is the ideal-gas volume. The equation becomes
> $$\left(p + \frac{an^2}{V_0^2}\right)(V_0 + \delta V - nb) = nRT.$$
> Expand and keep only terms linear in $a, b$ (and treat $\delta V \sim a, b$):
> $$p V_0 + p \delta V - p nb + \frac{a n^2}{V_0^2} V_0 + O(a^2, ab, b^2) = nRT.$$
> Use $pV_0 = nRT$ to cancel the leading term:
> $$p \delta V - p n b + \frac{a n^2}{V_0} = 0 \quad \Rightarrow \quad \delta V = nb - \frac{a n^2}{p V_0} = nb - \frac{an}{RT}.$$
> So
> $$V \approx \frac{nRT}{p} + nb - \frac{an}{RT}.$$
>
> Compute $(\partial V/\partial T)_p$ to leading order:
> $$\left(\frac{\partial V}{\partial T}\right)_p = \frac{nR}{p} + \frac{an}{RT^2}.$$
> So $T(\partial V/\partial T)_p = nRT/p + an/(RT)$. Compare with $V = nRT/p + nb - an/(RT)$:
> $$T(\partial V/\partial T)_p - V = \frac{nRT}{p} + \frac{an}{RT} - \frac{nRT}{p} - nb + \frac{an}{RT} = \frac{2an}{RT} - nb.$$
>
> Hence:
> $$\mu_{JT} \approx \frac{1}{C_p}\left[\frac{2an}{RT} - nb\right] = \frac{n}{C_p}\left[\frac{2a}{RT} - b\right].$$
>
> The inversion temperature $T_{\text{inv}}$ is where $\mu_{JT} = 0$:
> $$\frac{2a}{R T_{\text{inv}}} - b = 0 \quad \Rightarrow \quad T_{\text{inv}} = \frac{2a}{Rb}.$$
>
> For $T < T_{\text{inv}}$: $\mu_{JT} > 0$, gas cools on expansion (refrigeration regime). For $T > T_{\text{inv}}$: $\mu_{JT} < 0$, gas heats on expansion (warming regime). The Linde process for liquefying air operates at $T < T_{\text{inv}}$ to extract a small cooling on each pass through a throttling valve; nitrogen and oxygen have $T_{\text{inv}} > 300\,\text{K}$ at atmospheric pressure, so they can be liquefied this way starting from room temperature. Hydrogen has $T_{\text{inv}} \approx 200\,\text{K}$ and helium $T_{\text{inv}} \approx 50\,\text{K}$, so these gases must be pre-cooled before throttling can liquefy them.

> [!note]- Complete formal solution
> *Step 1 (general formula):* Set $dH = T\, dS + V\, dp = 0$, giving $dS = -(V/T)\, dp$. Expand $dS$ via the chain rule: $dS = (C_p/T)\, dT - (\partial V/\partial T)_p\, dp$, using $C_p = T(\partial S/\partial T)_p$ and the Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ from $G$. Equating and solving for $dT/dp$:
> $$\boxed{\mu_{JT} = \left(\frac{\partial T}{\partial p}\right)_H = \frac{T(\partial V/\partial T)_p - V}{C_p}.}$$
>
> *Step 2 (ideal gas):* $V = nRT/p$, so $(\partial V/\partial T)_p = nR/p = V/T$. Hence $T(\partial V/\partial T)_p = V$, and $\mu_{JT} = 0$.
>
> *Step 3 (Van der Waals):* Expanding $V$ in the equation of state to first order in $a, b$ gives $V = nRT/p + nb - an/(RT)$. Then $T(\partial V/\partial T)_p - V = 2an/(RT) - nb$, so
> $$\mu_{JT} \approx \frac{n}{C_p}\left[\frac{2a}{RT} - b\right].$$
> Inversion: $T_{\text{inv}} = 2a/(Rb)$.

> [!warning] Illegal but tempting alternative: assuming throttling is isothermal
> A common error is to think that since the throttling process is "adiabatic" ($\delta Q_{\text{actual}} = 0$ to the environment), and the system is "in equilibrium" before and after, the process must be isothermal. This conflates two different things: *adiabatic with respect to environment* (no heat exchange with surroundings) and *isothermal* (constant temperature). Throttling is the former but not the latter — the gas's temperature changes (by amount $\mu_{JT} \Delta p$) even though no heat enters from outside. The work done against the downstream pressure differs from the work received from the upstream pressure, and the difference produces the temperature change. The isenthalpic constraint $H_1 = H_2$ comes from energy conservation across the constriction (steady-state flow), not from any thermal equilibration. Recognising "throttling = isenthalpic, not isothermal, not adiabatic-reversible" is the key insight.

---

# Key Takeaways

**Throttling is isenthalpic, not adiabatic-reversible.** The Joule-Thomson process is a non-quasistatic adiabatic process whose endpoints are connected by the conservation of enthalpy, not by a path along which $\delta Q = 0$ point-by-point. This is why the right potential to use is $H$ (whose constancy along the process is the key constraint), not $U$ (which would be constant for an isolated process not involving pressure work). The trigger-reaction pattern is "see a steady-flow expansion through a constriction → isenthalpic". For a free expansion (no flow, just a valve opening into vacuum), the constraint is instead $\Delta U = 0$ — *isoenergetic* — and the analogous calculation gives the **Joule coefficient** $(\partial T/\partial V)_U$ which for an ideal gas is also zero but is nonzero for real gases.

**Maxwell relations are the workhorse for converting impossible-to-measure into measurable.** The derivation of the general $\mu_{JT}$ formula relied crucially on the Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ to eliminate $(\partial S/\partial p)_T$ — a quantity you cannot measure directly with any thermodynamic instrument — in favour of $(\partial V/\partial T)_p$, which is the thermal expansion coefficient (times $V$) and is routinely tabulated. Every "hard" thermodynamic computation involves at least one such conversion via a Maxwell relation. The skill is to recognise which Maxwell relation applies: in this case, $S$ paired with $p$ at fixed $T$ → use the Maxwell relation from $G(T, p)$.

**The inversion temperature is the boundary between heating and cooling regimes.** For real gases, $\mu_{JT}$ depends on temperature and pressure, and changes sign at the inversion line in the $(T, p)$ plane. Below the inversion temperature, throttling produces cooling — the basis for industrial liquefaction (Linde process). Above the inversion temperature, throttling heats — the basis for understanding atmospheric phenomena like the foehn wind (downslope warming as air is compressed in throttling-like processes). The inversion temperature for nitrogen is around 620 K (well above room temperature, so air liquefies easily by throttling); for hydrogen it is around 200 K and for helium 51 K, requiring pre-cooling before throttling can liquefy. The pattern $T_{\text{inv}} \sim a/(Rb)$ in terms of Van der Waals parameters connects microscopic intermolecular forces (the attraction $a$, the molecular volume $b$) to the macroscopic inversion temperature — a clean instance of microscopic-to-macroscopic transfer.

**The Van der Waals correction is captured by two physical effects.** The term $2a/(RT) > 0$ in $\mu_{JT}$ comes from intermolecular attraction: at low $T$, expansion overcomes attractive forces (cooling the gas) by converting kinetic energy to potential energy. The term $-b < 0$ comes from molecular volume: at high $T$, expansion gives the molecules less "tight packing" and they speed up. The balance at $T_{\text{inv}} = 2a/(Rb)$ is where these two effects cancel. Recognising the physical origin of each term — *attraction → cooling on expansion, repulsion → heating on expansion* — is the conceptual content of the Joule-Thomson effect, beyond the algebraic derivation.

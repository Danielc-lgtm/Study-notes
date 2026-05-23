---
type: exercise
subject: thermodynamics
difficulty: "⭐⭐"
prereqs:
  - "Def - Thermodynamic Potential (U, H, F, G)"
  - "Def - The First Law of Thermodynamics"
  - "Thm - Maxwell Relations from Closedness"
tags: [physics, thermodynamics, ideal-gas, heat-capacity]
---

# Problem Statement

The **heat capacities** of a thermodynamic system are
$$C_V := \left(\frac{\partial U}{\partial T}\right)_V = T \left(\frac{\partial S}{\partial T}\right)_V, \quad C_p := \left(\frac{\partial H}{\partial T}\right)_p = T \left(\frac{\partial S}{\partial T}\right)_p.$$

1. Derive the **general identity**:
$$C_p - C_V = T \left(\frac{\partial V}{\partial T}\right)_p \left(\frac{\partial p}{\partial T}\right)_V = \frac{T V \alpha^2}{\kappa_T},$$
where $\alpha = V^{-1}(\partial V/\partial T)_p$ is the thermal expansion coefficient and $\kappa_T = -V^{-1}(\partial V/\partial p)_T$ is the isothermal compressibility.

2. Specialise to an ideal gas ($pV = nRT$) and obtain **Mayer's relation** $C_p - C_V = nR$.

3. Comment on what $C_p - C_V$ tells you about the system: why is $C_p > C_V$ for any normal substance ($\alpha^2 > 0$, $\kappa_T > 0$), and what would $\alpha = 0$ correspond to physically?

**Recall:**

The [[Def - The First Law of Thermodynamics|first law]] gives $\delta Q = dU + p\, dV$. The [[Def - Absolute Temperature and Entropy|second law]] gives $\delta Q = T\, dS$ for quasistatic processes.

The [[Thm - Maxwell Relations from Closedness|Maxwell relation from the Helmholtz free energy]]: $(\partial S/\partial V)_T = (\partial p/\partial T)_V$.

The **cyclic relation** for three variables $(T, p, V)$ satisfying $f(T, p, V) = 0$ (the equation of state):
$$\left(\frac{\partial V}{\partial T}\right)_p \left(\frac{\partial T}{\partial p}\right)_V \left(\frac{\partial p}{\partial V}\right)_T = -1.$$

---

# Convergent Strategy

**Problem class:** A thermodynamic identity-derivation problem. The recurring pattern: relate $C_p$ to $C_V$ by expanding the entropy in different coordinate systems (once in $(T, V)$, once in $(T, p)$) and equating mixed partial derivatives via Maxwell relations.

**Assumption pattern:** Existence of the entropy $S$ as a state function on $M$ (from [[Thm - The Heat 1-Form is Integrable|Caratheodory's theorem]]). The heat capacities $C_V$ and $C_p$ are well-defined partial derivatives.

**Theorem routing:** Express $S$ in $(T, V)$ coordinates: $dS = (\partial S/\partial T)_V\, dT + (\partial S/\partial V)_T\, dV = (C_V/T)\, dT + (\partial p/\partial T)_V\, dV$ using the Maxwell relation. At constant pressure ($dp = 0$), $dV$ becomes a function of $dT$: $dV = (\partial V/\partial T)_p\, dT$. Substitute into the $dS$ expression: $dS|_p = [(C_V/T) + (\partial p/\partial T)_V (\partial V/\partial T)_p]\, dT$. Equate $C_p/T = dS/dT|_p$ on the LHS: $C_p/T = C_V/T + (\partial p/\partial T)_V (\partial V/\partial T)_p$. Solve for $C_p - C_V$.

**Key decision point:** The non-obvious choice is to *change coordinates* from $(T, V)$ to $(T, p)$ via the equation of state, using the chain rule $dV = (\partial V/\partial T)_p\, dT$ at constant $p$. This is what bridges the two heat capacities, since one is defined at constant $V$ and the other at constant $p$. The Maxwell relation enters when expressing $dS$ in $(T, V)$ coordinates — it replaces the inaccessible $(\partial S/\partial V)_T$ by the measurable $(\partial p/\partial T)_V$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (split a 1-form using the first law).** The differential $dU = T\, dS - p\, dV$ underpins both heat capacities.

2. **Operation 4 from the topic page (use $d^2 = 0$ on a potential).** The Maxwell relation $(\partial S/\partial V)_T = (\partial p/\partial T)_V$ is the key conversion of an $S$-derivative into a measurable $p$-derivative.

3. **Operation 5 from the topic page (Legendre transform).** Switching between $U(S, V)$ (whose differential involves $C_V$) and $H(S, p)$ (whose differential involves $C_p$) is a Legendre transform $H = U + pV$ — the algebraic basis for relating the two heat capacities.

---

# Hints

> [!note]- Hint 1
> Express $dS$ in $(T, V)$ coordinates using the chain rule: $dS = (\partial S/\partial T)_V\, dT + (\partial S/\partial V)_T\, dV$. Use $C_V = T(\partial S/\partial T)_V$ and the Maxwell relation $(\partial S/\partial V)_T = (\partial p/\partial T)_V$:
> $$dS = \frac{C_V}{T}\, dT + \left(\frac{\partial p}{\partial T}\right)_V dV.$$

> [!note]- Hint 2
> Now consider an isobaric process ($dp = 0$). Along it, $dV$ is related to $dT$ by $dV = (\partial V/\partial T)_p\, dT$. Substitute into the $dS$ expression:
> $$dS\bigg|_{p=\text{const}} = \left[\frac{C_V}{T} + \left(\frac{\partial p}{\partial T}\right)_V \left(\frac{\partial V}{\partial T}\right)_p\right]\, dT.$$
> But by definition $dS|_p = (\partial S/\partial T)_p\, dT = (C_p/T)\, dT$. Equate:
> $$\frac{C_p}{T} = \frac{C_V}{T} + \left(\frac{\partial p}{\partial T}\right)_V \left(\frac{\partial V}{\partial T}\right)_p.$$
> Solve for $C_p - C_V$.

> [!note]- Hint 3
> Use the cyclic relation $(\partial V/\partial T)_p (\partial T/\partial p)_V (\partial p/\partial V)_T = -1$ to rewrite $(\partial p/\partial T)_V$:
> $$\left(\frac{\partial p}{\partial T}\right)_V = -\frac{(\partial V/\partial T)_p}{(\partial V/\partial p)_T} = \frac{V\alpha}{V \kappa_T} = \frac{\alpha}{\kappa_T}.$$
> So
> $$C_p - C_V = T \left(\frac{\partial p}{\partial T}\right)_V \left(\frac{\partial V}{\partial T}\right)_p = T \cdot \frac{\alpha}{\kappa_T} \cdot V\alpha = \frac{TV\alpha^2}{\kappa_T}.$$

> [!note]- Hint 4
> For an ideal gas: $p = nRT/V$, so $(\partial p/\partial T)_V = nR/V$. And $V = nRT/p$, so $(\partial V/\partial T)_p = nR/p$. Multiply: $T \cdot (nR/V) \cdot (nR/p) = T (nR)^2/(pV) = T (nR)^2/(nRT) = nR$. So $C_p - C_V = nR$ — Mayer's relation.

---

# Solution

The proof is in three steps. Step 1 derives the general formula by expressing $dS$ in two ways. Step 2 simplifies using the cyclic relation and definitions of $\alpha$, $\kappa_T$. Step 3 specialises to the ideal gas. The non-obvious move is in Step 1, where the *same* $dS$ is expressed once via the chain rule in $(T, V)$ coordinates (using the Maxwell relation) and once via $C_p$ in $(T, p)$ coordinates — equating the two gives the heat-capacity difference.

**Step 1: General formula $C_p - C_V = T (\partial V/\partial T)_p (\partial p/\partial T)_V$.**

> [!note]- Derivation
> Start with $dS$ in $(T, V)$ coordinates:
> $$dS = \left(\frac{\partial S}{\partial T}\right)_V dT + \left(\frac{\partial S}{\partial V}\right)_T dV.$$
> Use $C_V = T(\partial S/\partial T)_V$ and the Maxwell relation $(\partial S/\partial V)_T = (\partial p/\partial T)_V$ (from $F$):
> $$dS = \frac{C_V}{T} dT + \left(\frac{\partial p}{\partial T}\right)_V dV. \tag{*}$$
>
> Now consider an isobaric process ($dp = 0$): $dV = (\partial V/\partial T)_p\, dT$. Substitute:
> $$dS\big|_{p=\text{const}} = \left[\frac{C_V}{T} + \left(\frac{\partial p}{\partial T}\right)_V \left(\frac{\partial V}{\partial T}\right)_p\right] dT.$$
>
> But also $dS|_{p=\text{const}} = (\partial S/\partial T)_p\, dT = (C_p/T)\, dT$. Equate:
> $$\frac{C_p}{T} = \frac{C_V}{T} + \left(\frac{\partial p}{\partial T}\right)_V \left(\frac{\partial V}{\partial T}\right)_p,$$
> giving
> $$C_p - C_V = T \left(\frac{\partial p}{\partial T}\right)_V \left(\frac{\partial V}{\partial T}\right)_p.$$

**Step 2: Rewrite in terms of $\alpha$ and $\kappa_T$ to get $C_p - C_V = TV\alpha^2/\kappa_T$.**

> [!note]- Derivation
> The thermal expansion coefficient and isothermal compressibility are
> $$\alpha := \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_p, \quad \kappa_T := -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_T.$$
>
> Use the cyclic relation $(\partial V/\partial T)_p (\partial T/\partial p)_V (\partial p/\partial V)_T = -1$ to express $(\partial p/\partial T)_V$:
> $$\left(\frac{\partial p}{\partial T}\right)_V = -\frac{(\partial V/\partial T)_p}{(\partial V/\partial p)_T} = -\frac{V\alpha}{-V\kappa_T} = \frac{\alpha}{\kappa_T}.$$
>
> Substitute into the general formula:
> $$C_p - C_V = T \cdot \frac{\alpha}{\kappa_T} \cdot V \alpha = \frac{T V \alpha^2}{\kappa_T}.$$
>
> Since $T, V, \kappa_T > 0$ and $\alpha^2 \geq 0$, we conclude $C_p \geq C_V$ always, with equality iff $\alpha = 0$ (the substance does not expand on heating — physically rare, but happens for water near 4°C).

**Step 3: Ideal-gas specialisation — Mayer's relation $C_p - C_V = nR$.**

> [!note]- Derivation
> For an ideal gas, $p = nRT/V$, so $(\partial p/\partial T)_V = nR/V$. And $V = nRT/p$, so $(\partial V/\partial T)_p = nR/p$.
>
> Substitute into the general formula:
> $$C_p - C_V = T \cdot \frac{nR}{V} \cdot \frac{nR}{p} = \frac{T (nR)^2}{pV} = \frac{T (nR)^2}{nRT} = nR.$$
>
> This is **Mayer's relation**: $C_p - C_V = nR$ for any ideal gas. The result is *independent* of $f$ (the number of degrees of freedom) — both $C_p$ and $C_V$ scale linearly with $f$, but their difference is the universal constant $nR$. The physical interpretation: heating at constant pressure requires additional energy $p\, dV = nR\, dT$ per unit temperature rise (to do the expansion work against the external pressure), beyond the energy $C_V\, dT$ needed to raise the temperature at constant volume.

> [!note]- Complete formal solution
> *Step 1:* Express $dS = (C_V/T)\, dT + (\partial p/\partial T)_V\, dV$ in $(T, V)$ coordinates (using the Maxwell relation from $F$). Along isobaric process, $dV = (\partial V/\partial T)_p\, dT$, giving $dS|_p = [(C_V/T) + (\partial p/\partial T)_V (\partial V/\partial T)_p]\, dT$. Equating with $dS|_p = (C_p/T)\, dT$ gives
> $$C_p - C_V = T \left(\frac{\partial p}{\partial T}\right)_V \left(\frac{\partial V}{\partial T}\right)_p.$$
>
> *Step 2:* Using $\alpha = V^{-1}(\partial V/\partial T)_p$, $\kappa_T = -V^{-1}(\partial V/\partial p)_T$, and the cyclic relation:
> $$C_p - C_V = \frac{T V \alpha^2}{\kappa_T}.$$
> Always positive (since $\alpha^2 \geq 0$, $\kappa_T > 0$), with equality iff $\alpha = 0$.
>
> *Step 3:* Ideal gas: $(\partial p/\partial T)_V (\partial V/\partial T)_p = nR/V \cdot nR/p = (nR)^2/(pV) = nR/T$. So $C_p - C_V = nR$ — **Mayer's relation**.

---

# Key Takeaways

**Mayer's relation $C_p - C_V = nR$ for ideal gases is a universal result.** It says that the extra heat needed to raise the temperature at constant pressure (versus constant volume) equals $nR$, *independent* of the gas (monatomic, diatomic, polyatomic). The physical reason: heating at constant pressure requires the gas to do expansion work against the external pressure, and that work equals $p\, dV = nR\, dT$ per unit temperature rise (using the equation of state). So $C_p T = C_V T + (\text{work done}) = C_V T + nRT$, giving $C_p = C_V + nR$. This identity is the historical name of Robert Mayer (1842), and it predates the modern formalism by many decades — it was one of the early successes that confirmed the energy-conservation interpretation of the first law.

**$C_p > C_V$ always, by a positive multiple of $\alpha^2$.** The general formula $C_p - C_V = TV\alpha^2/\kappa_T$ shows that the heat-capacity difference is *always positive* (since $\alpha^2 \geq 0$, $\kappa_T > 0$, $T, V > 0$). The physical content: any substance that expands on heating ($\alpha \neq 0$) has $C_p > C_V$. The only way to have $C_p = C_V$ is to have $\alpha = 0$ — meaning the substance does not expand on heating. This is rare: water near 4°C has $\alpha \approx 0$ (the density maximum), and very near absolute zero the heat capacities of all substances satisfy $C_p \approx C_V$ since $\alpha \to 0$ (the third-law boundary). For most substances at most temperatures, $\alpha > 0$ and the difference is significant — for solids it is small (because they expand little); for liquids it is moderate; for gases it is $nR$ exactly.

**The derivation pattern: express $dS$ in two coordinate systems, equate at the right slice.** The trick used here — write $dS$ in $(T, V)$ coordinates using one Maxwell relation, restrict to an isobaric path via $dV = (\partial V/\partial T)_p\, dT$, equate with the $C_p$ formula — is a recurring technique for relating thermodynamic quantities defined under different constraint patterns. The same pattern works for: relating $\kappa_T$ to $\kappa_S$ (isothermal vs adiabatic compressibility); relating the Joule and Joule-Thomson coefficients; relating any two partial derivatives differing in which variable is held constant. The trigger-reaction pattern: "relate quantities under different constraints → express the common state function ($S$ or $H$ or $U$) in both coordinate systems, equate via Maxwell relations".

**The cyclic relation $(\partial V/\partial T)_p (\partial T/\partial p)_V (\partial p/\partial V)_T = -1$ is the key algebraic identity.** This identity (valid for any three variables satisfying an algebraic relation $f(T, p, V) = 0$) is the workhorse for converting between partial derivatives in different coordinate systems. Its memorisation pays compound interest in thermodynamic computations: it appears in deriving heat-capacity relations, the Joule-Thomson coefficient, the speed of sound, the Clausius-Clapeyron equation, and countless other identities. The trigger-reaction pattern: "see three partial derivatives forming a cycle → multiply them, the product is $-1$".

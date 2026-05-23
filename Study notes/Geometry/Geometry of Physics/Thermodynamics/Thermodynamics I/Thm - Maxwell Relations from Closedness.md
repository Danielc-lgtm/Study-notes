---
type: theorem
subject: thermodynamics
prereqs:
  - "Def - Thermodynamic Potential (U, H, F, G)"
  - "Def - The First Law of Thermodynamics"
  - "Def - Absolute Temperature and Entropy"
  - "Def - Closed and Exact Forms"
tags: [physics, thermodynamics, differential-geometry]
---

# Notation

$U(S, V), H(S, p), F(T, V), G(T, p)$ are the four [[Def - Thermodynamic Potential (U, H, F, G)|thermodynamic potentials]] with the conjugate variable pairs $(S, T)$ and $(V, p)$. Partial derivatives are written with the held-constant variable as a subscript: $(\partial S/\partial V)_T$ means "partial of $S$ with respect to $V$ holding $T$ fixed". See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

---

# Statement

> **Theorem (Maxwell Relations).** For a simple thermodynamic system with the four thermodynamic potentials $U(S, V), H(S, p), F(T, V), G(T, p)$ and the standard differentials
>
> $$dU = T\, dS - p\, dV, \quad dH = T\, dS + V\, dp, \quad dF = -S\, dT - p\, dV, \quad dG = -S\, dT + V\, dp,$$
>
> applying the closedness condition $d^2 \Phi = 0$ to each potential $\Phi$ yields the four **Maxwell relations**:
>
> $$\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial p}{\partial S}\right)_V \quad \text{(from } U\text{)},$$
>
> $$\left(\frac{\partial T}{\partial p}\right)_S = \left(\frac{\partial V}{\partial S}\right)_p \quad \text{(from } H\text{)},$$
>
> $$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial p}{\partial T}\right)_V \quad \text{(from } F\text{)},$$
>
> $$\left(\frac{\partial S}{\partial p}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_p \quad \text{(from } G\text{)}.$$
>
> Each relation equates a partial derivative involving the entropy or temperature (often hard to measure directly) to a partial derivative involving only pressure, volume, and temperature (directly measurable in experiments).

---

# Motivation

The Maxwell relations are not deep theorems — each is a single line of computation. What makes them remarkable is their utility: they reduce hard-to-measure quantities (anything involving $S$) to easy-to-measure ones (involving $T, p, V$). Tables of thermodynamic data list $\alpha = V^{-1}(\partial V/\partial T)_p$ (the thermal expansion coefficient) and $\kappa_T = -V^{-1}(\partial V/\partial p)_T$ (the isothermal compressibility), both directly measurable; the Maxwell relations let you derive everything else from them.

The motivation for *why* there are four Maxwell relations (and not more or fewer) is structural: there are four thermodynamic potentials (one for each subset of the conjugate-pair swaps $(S, T) \leftrightarrow (S \text{ or } T)$ and $(V, p) \leftrightarrow (V \text{ or } p)$), and each potential's differential has two natural-variable terms, giving one cross-partial identity per potential. So four potentials → four Maxwell relations, exhausting the structure for a simple system. For more complex systems with $n$ conjugate pairs, there are $2^n$ potentials and a correspondingly larger family of Maxwell relations.

The motivation for the *form* of the Maxwell relations is the geometric content of $d^2 = 0$. The thermodynamic potentials are smooth functions on the state space $M$, and the exterior derivative $d$ on smooth functions yields exact 1-forms, which automatically satisfy $d^2 = 0$ — this is just the algebraic identity that mixed partial derivatives commute, $\partial^2 \Phi/\partial x \partial y = \partial^2 \Phi/\partial y \partial x$. The Maxwell relations are the four instances of this identity for the four potentials, written in the form that emphasises the equality of cross-partials of conjugate variables.

A reader who knows multivariable calculus might wonder why the Maxwell relations are interesting at all — surely "$\partial^2/\partial x \partial y = \partial^2/\partial y \partial x$" is trivial. The answer is that *which variables count as "$x$" and "$y$"* depends on the potential, and the natural variables of each potential are different. So the relations look like equations among completely different physical quantities: $(\partial S/\partial V)_T$ is an entropy gradient, $(\partial p/\partial T)_V$ is a pressure gradient — these are physically distinct measurements, yet they are equal as a consequence of $d^2 F = 0$. The triviality of the underlying mathematics belies the non-triviality of the physical content.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$\Phi$ is a thermodynamic potential, i.e., a smooth state function whose differential $d\Phi$ has the standard form in its natural variables". Recognising this in disguise:

The most common source is **the existence of *any* state function on $M$**. If you can construct a state function $\Phi(x, y)$ on a 2-dimensional manifold with $d\Phi = A(x, y)\, dx + B(x, y)\, dy$, then $d^2 \Phi = 0$ gives $\partial A/\partial y = \partial B/\partial x$. This is a Maxwell-like relation for the variables $(x, y)$ and the conjugate slopes $(A, B)$. The bridge: any state function with two natural variables produces a cross-partial identity. The four thermodynamic potentials happen to give the four physically interesting cases, but the construction is general.

A second source is **a 1-form that is *known* to be exact**. Even without identifying a specific potential, if you know $\omega = A\, dx + B\, dy$ is exact (i.e., the line integral $\int \omega$ is path-independent), then $\partial A/\partial y = \partial B/\partial x$ by $d\omega = 0$. The bridge converts exactness into cross-partial identities.

A third source is **the integrability condition for a 1-form**. If a 1-form $\theta$ satisfies $\theta \wedge d\theta = 0$ and is therefore $\lambda\, df$ locally, then expanding $\theta = A\, dx + B\, dy$ and equating to $\lambda(df/dx \cdot dx + df/dy \cdot dy)$ gives consistency conditions analogous to Maxwell relations, but with the integrating factor $\lambda$ entering. The bridge from integrability to derivative identities is the same algebraic content, with the integrating factor as an extra parameter.

A fourth source is **a Legendre-transform relationship between two potentials**. If $\Phi_1$ and $\Phi_2$ are related by a Legendre transform swapping the conjugate pair $(y, z)$ — so $\Phi_2 = \Phi_1 + yz$ with $z = \partial \Phi_1/\partial y$ — then $d\Phi_1$ and $d\Phi_2$ are related by a sign flip on one term, and applying $d^2 = 0$ to either gives a Maxwell relation. Conversely, the Maxwell relations *between* two Legendre-related potentials are pairwise interchanged via the sign flip. The bridge from the Legendre cube to the Maxwell relations is explicit and structural.

**Targets (Output Amplification)**

The conclusion is the four cross-partial identities. Combining with further inputs:

The principal target combination is **Maxwell relation plus an equation of state $\Rightarrow$ a numerical value for the difficult derivative**. For example, the Maxwell relation $(\partial S/\partial V)_T = (\partial p/\partial T)_V$ combined with the ideal gas equation $p = nRT/V$ gives $(\partial p/\partial T)_V = nR/V$, hence $(\partial S/\partial V)_T = nR/V$ — directly computing an entropy gradient from a single derivative of $p$. The combination is nonobvious because it converts a thermodynamic question (entropy change at constant temperature) into a state-equation question (pressure dependence on temperature).

A second target combination is **Maxwell relation plus heat capacity $\Rightarrow$ relation between $C_p$ and $C_V$**. The Maxwell relation $(\partial S/\partial V)_T = (\partial p/\partial T)_V$, combined with the definitions $C_V = T(\partial S/\partial T)_V$ and $C_p = T(\partial S/\partial T)_p$, gives the general identity $C_p - C_V = T V \alpha^2/\kappa_T$ where $\alpha = V^{-1}(\partial V/\partial T)_p$ and $\kappa_T = -V^{-1}(\partial V/\partial p)_T$. For an ideal gas this reduces to $C_p - C_V = nR$. The combination is nonobvious because $C_p - C_V$ does not obviously involve any of $\alpha$ or $\kappa_T$ until the Maxwell relation supplies the connection.

A third target combination is **Maxwell relation plus the Clausius-Clapeyron derivation $\Rightarrow$ the slope of the phase-coexistence curve**. At a first-order phase transition, the Gibbs free energy is continuous but its derivatives jump: $\Delta S = S_2 - S_1$ and $\Delta V = V_2 - V_1$ are the latent entropy and volume changes. The Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$, applied along the coexistence curve, combined with the equality of $G$ in the two phases, gives the **Clausius-Clapeyron equation** $dp/dT = \Delta S/\Delta V$ for the coexistence curve. The combination is nonobvious because phase transitions are about discontinuities, but the Maxwell relation's smooth derivative structure still constrains them at the boundary.

A fourth target combination is **Maxwell relation plus the Joule-Thomson process $\Rightarrow$ the inversion temperature**. The Joule-Thomson coefficient $\mu_{JT} = (\partial T/\partial p)_H$ governing throttled expansion can be computed using $dH = 0$, $dH = T\, dS + V\, dp$, and the Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$, yielding $\mu_{JT} = (T (\partial V/\partial T)_p - V)/C_p$. For an ideal gas this is zero; for a real gas it changes sign at the inversion temperature. See [[Ex - Joule-Thomson Coefficient from Thermodynamic Identities]].

---

# Why Is It True

The intuition is the geometric content of $d^2 = 0$: **the exterior derivative of an exact form is zero, and equating the coefficients of the resulting 2-form to zero yields the Maxwell relations.** The bolded one-liner: **Maxwell relations are mixed-partial-derivative symmetries of thermodynamic potentials, and the *interesting* content is that the partial derivatives involve conjugate variable pairs.**

Compute $d^2 F$ where $F = F(T, V)$. We have $dF = -S\, dT - p\, dV$, so applying $d$ again:
$$d^2 F = d(-S\, dT - p\, dV) = -dS \wedge dT - dp \wedge dV = 0.$$
Expand $dS = (\partial S/\partial T)_V\, dT + (\partial S/\partial V)_T\, dV$ and similarly for $dp$, and collect terms in the basis $dT \wedge dV$:
$$d^2 F = -(\partial S/\partial V)_T\, dV \wedge dT - (\partial p/\partial T)_V\, dT \wedge dV = [(\partial S/\partial V)_T - (\partial p/\partial T)_V]\, dT \wedge dV.$$
(Used $dV \wedge dT = -dT \wedge dV$.) Setting this to zero: $(\partial S/\partial V)_T = (\partial p/\partial T)_V$ — the third Maxwell relation. The other three are identical computations for the other potentials.

The mechanism is: each potential is a state function on a 2-dimensional patch of $M$, with its two natural variables as coordinates and its two conjugate variables as coefficients of the differential. Exactness ($d^2 = 0$) equates the cross-partials of the coefficients. The Maxwell relation is the resulting cross-partial identity, with the two coefficients being the *conjugates* of the natural variables.

The reason the relations involve hard-to-measure $S$ and easy-to-measure $p, V, T$: in the four standard thermodynamic potentials, $S$ appears as a coefficient (conjugate to $T$) in two of them ($F$ and $G$), but the natural variable in the other position is $V$ or $p$. So the Maxwell relation expresses $(\partial S/\partial \text{easy variable})$ in terms of $(\partial \text{easy quantity}/\partial T)$. This is why every Maxwell relation has *one* derivative involving $S$ — the cross-partial structure always pairs one $S$-derivative with one $T$-derivative of another variable.

---

# What Makes This Hard

The mathematical step is one line per Maxwell relation. What makes the Maxwell relations operationally hard is **identifying which potential to use for a given problem**. Faced with the question "compute $(\partial S/\partial p)_T$", the student must recognise that:
- $S$ paired with $p$ as natural variables points to $H(S, p)$ — wrong, because $S$ is a *natural* variable of $H$, not a *coefficient*.
- $S$ paired with $T$ as *coefficient* and $T$ as the held-constant variable points to $G(T, p)$ — correct: $dG = -S\, dT + V\, dp$ has $-S$ as coefficient of $dT$ and $V$ as coefficient of $dp$, giving $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$.

This identification requires fluent recall of all four potentials and their natural-variable structures. The most common error is to apply the wrong Maxwell relation (e.g., the one from $F$ when $G$ was needed) — giving an equation that is *also* true but does not relate the variables in the problem.

A subsidiary difficulty is sign conventions. The signs in the Maxwell relations depend on the sign convention for $\delta W$ and the convention $T, p > 0$; with the alternative sign convention ($\delta W$ as work done *on* the system), some signs flip. Cross-checking against the original first law convention is essential.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct any Maxwell relation from scratch.**

**High-level strategy:** Pick the thermodynamic potential whose natural variables are the *two variables held constant* in the partial derivatives of interest. Write down its differential in standard form. Apply $d^2 = 0$ and read off the cross-partial identity.

**Subgoal decomposition:**

1. **Identify the natural variables of the target partial derivative.** If you want $(\partial A/\partial B)_C$, the variable $C$ is held constant — so the relevant potential has $C$ as a natural variable.
   - *Hint:* The four potentials are $U(S, V), H(S, p), F(T, V), G(T, p)$. Choose by the held-constant variable.
   - *Why needed:* Selects the right potential.

2. **Write down $d\Phi$ in standard form.** Recall the four differentials: $dU = T\, dS - p\, dV$, $dH = T\, dS + V\, dp$, $dF = -S\, dT - p\, dV$, $dG = -S\, dT + V\, dp$.
   - *Hint:* Memorise these, or derive each from $U$ via Legendre transforms.
   - *Why needed:* Sets up $d^2 \Phi = 0$.

3. **Apply $d^2 = 0$.** Take the exterior derivative of $d\Phi$ and set it to zero. Expand each coefficient as a function of the natural variables and collect terms in the basis $dx \wedge dy$ of the 2-form space.
   - *Hint:* $d(A\, dx + B\, dy) = dA \wedge dx + dB \wedge dy = (\partial A/\partial y)\, dy \wedge dx + (\partial B/\partial x)\, dx \wedge dy = [(\partial B/\partial x) - (\partial A/\partial y)]\, dx \wedge dy$.
   - *Why needed:* Mechanical computation of the cross-partial identity.

4. **Read off the Maxwell relation.** The coefficient of $dx \wedge dy$ must vanish; equating it to zero gives $(\partial A/\partial y)_x = (\partial B/\partial x)_y$ (with sign as determined by the original differential).
   - *Hint:* Pay attention to signs — they depend on the differential's structure.
   - *Why needed:* Gives the final relation.

---

# Lemma Decomposition

> [!note]- Lemma 1: $d^2 = 0$ on smooth functions
> **Statement:** For any smooth function $\Phi$ on a smooth manifold $M$, $d(d\Phi) = 0$.
>
> **Hint:** This is a general property of the exterior derivative on smooth forms, following from the equality of mixed partial derivatives.
>
> **Why needed:** It is the fundamental identity that produces every Maxwell relation.
>
> > [!note]- Full proof
> > In local coordinates $(x^1, \ldots, x^n)$, $d\Phi = \sum_i (\partial \Phi/\partial x^i)\, dx^i$. Applying $d$ again:
> > $$d^2 \Phi = \sum_i d(\partial \Phi/\partial x^i) \wedge dx^i = \sum_{i, j} (\partial^2 \Phi/\partial x^j \partial x^i)\, dx^j \wedge dx^i.$$
> > By the equality of mixed partial derivatives, $\partial^2 \Phi/\partial x^j \partial x^i = \partial^2 \Phi/\partial x^i \partial x^j$, so the sum is symmetric in $i, j$. Combined with the antisymmetry $dx^j \wedge dx^i = -dx^i \wedge dx^j$, each pair $(i, j)$ with $i \neq j$ contributes a term plus its negative, which cancel. The diagonal terms ($i = j$) vanish from $dx^i \wedge dx^i = 0$. So $d^2 \Phi = 0$ identically.

> [!note]- Lemma 2: Derivation of the Maxwell relation from $F$
> **Statement:** Starting from $dF = -S\, dT - p\, dV$, applying $d^2 F = 0$ yields $(\partial S/\partial V)_T = (\partial p/\partial T)_V$.
>
> **Hint:** Compute $d(-S\, dT - p\, dV) = -dS \wedge dT - dp \wedge dV$, expand $dS$ and $dp$ in the basis $(dT, dV)$, and collect coefficients of $dT \wedge dV$.
>
> **Why needed:** This is the canonical derivation; the other three Maxwell relations follow by identical computations from the other potentials.
>
> > [!note]- Full proof
> > By Lemma 1, $d^2 F = 0$. Compute:
> > $$0 = d^2 F = d(-S\, dT - p\, dV) = -dS \wedge dT - dp \wedge dV.$$
> > Expand $dS = (\partial S/\partial T)_V\, dT + (\partial S/\partial V)_T\, dV$ and $dp = (\partial p/\partial T)_V\, dT + (\partial p/\partial V)_T\, dV$. Substitute:
> > $$-\left[(\partial S/\partial T)_V\, dT + (\partial S/\partial V)_T\, dV\right] \wedge dT - \left[(\partial p/\partial T)_V\, dT + (\partial p/\partial V)_T\, dV\right] \wedge dV.$$
> > Using $dT \wedge dT = 0$ and $dV \wedge dV = 0$:
> > $$= -(\partial S/\partial V)_T\, dV \wedge dT - (\partial p/\partial T)_V\, dT \wedge dV.$$
> > Use $dV \wedge dT = -dT \wedge dV$:
> > $$= (\partial S/\partial V)_T\, dT \wedge dV - (\partial p/\partial T)_V\, dT \wedge dV = \left[(\partial S/\partial V)_T - (\partial p/\partial T)_V\right]\, dT \wedge dV.$$
> > Setting the coefficient to zero: $(\partial S/\partial V)_T = (\partial p/\partial T)_V$, the third Maxwell relation.

> [!note]- Lemma 3: The other three Maxwell relations
> **Statement:** Identical computations on $U(S, V), H(S, p), G(T, p)$ yield the other three Maxwell relations:
> $$(\partial T/\partial V)_S = -(\partial p/\partial S)_V \quad \text{from } U,$$
> $$(\partial T/\partial p)_S = (\partial V/\partial S)_p \quad \text{from } H,$$
> $$(\partial S/\partial p)_T = -(\partial V/\partial T)_p \quad \text{from } G.$$
>
> **Hint:** For each potential, write $d\Phi = A\, dx + B\, dy$ where $A, B$ are the conjugate variables and $(x, y)$ the natural variables. Then $d^2\Phi = 0$ gives $(\partial A/\partial y)_x = (\partial B/\partial x)_y$, with the sign determined by the signs of $A$ and $B$ in $d\Phi$.
>
> **Why needed:** Completes the family of four Maxwell relations.
>
> > [!note]- Full proof
> > **From $U(S, V)$:** $dU = T\, dS - p\, dV$. So $A = T, B = -p$, $(x, y) = (S, V)$. The cross-partial identity is $(\partial T/\partial V)_S = (\partial (-p)/\partial S)_V$, i.e., $(\partial T/\partial V)_S = -(\partial p/\partial S)_V$.
> >
> > **From $H(S, p)$:** $dH = T\, dS + V\, dp$. So $A = T, B = V$, $(x, y) = (S, p)$. Identity: $(\partial T/\partial p)_S = (\partial V/\partial S)_p$.
> >
> > **From $G(T, p)$:** $dG = -S\, dT + V\, dp$. So $A = -S, B = V$, $(x, y) = (T, p)$. Identity: $(\partial (-S)/\partial p)_T = (\partial V/\partial T)_p$, i.e., $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$.
> >
> > Each derivation is mechanical: write $d\Phi$, apply $d$ again, expand, equate the $d\text{(first natural)} \wedge d\text{(second natural)}$ coefficient to zero.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness.** $U, H, F, G$ are smooth functions on the thermodynamic state space $M$. Each has a standard differential in its natural variables, derived from $dU = T\, dS - p\, dV$ via Legendre transforms (see [[Def - Thermodynamic Potential (U, H, F, G)]]).
>
> **The proof.** By Lemma 1, $d^2 = 0$ on any smooth function. By Lemmas 2 and 3, applying this identity to each of $U, H, F, G$ and reading off the cross-partial coefficient produces the four Maxwell relations as stated.

---

# Cross-Field Exercise Suggestions

**The Clausius-Clapeyron equation for phase transitions.** At a first-order phase transition (e.g., liquid-vapour coexistence), the chemical potentials of the two phases are equal at the coexistence boundary: $\mu_1(T, p) = \mu_2(T, p)$. Differentiating along the coexistence curve gives $d\mu_1 = d\mu_2$, i.e., $-S_1\, dT + V_1\, dp = -S_2\, dT + V_2\, dp$, hence $dp/dT = (S_2 - S_1)/(V_2 - V_1) = \Delta S/\Delta V$. The latent heat $L = T \Delta S$ converts this to $dp/dT = L/(T \Delta V)$ — the **Clausius-Clapeyron equation**. The Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ enters in deriving $\Delta S$ from measurable $V(T)$ data.

**The Gibbs-Helmholtz equation.** From $G = H - TS$ and $S = -(\partial G/\partial T)_p$, derive the **Gibbs-Helmholtz equation** $\left[\partial (G/T)/\partial T\right]_p = -H/T^2$. This expresses how the Gibbs free energy varies with temperature in terms of the enthalpy — useful in chemistry for computing equilibrium constants as functions of $T$ when $H$ is known (e.g., from calorimetric measurements). The derivation uses the Maxwell-like structure of $G$ but not a Maxwell relation per se; the identity is a consequence of the same $d^2 = 0$ machinery applied to $G/T$.

**The "TdS equations" for general substances.** Combining the Maxwell relations with the first law gives the two **TdS equations**: $T\, dS = C_V\, dT + T(\partial p/\partial T)_V\, dV$ and $T\, dS = C_p\, dT - T(\partial V/\partial T)_p\, dp$. These express the heat absorbed in terms of measurable coefficients ($C_V, C_p, \alpha = V^{-1}(\partial V/\partial T)_p, \kappa_T$) and the temperature changes. They are the workhorses for computing entropy changes in real substances (not just ideal gases) and rely on Maxwell relations from $F$ and $G$.

---

# Bridges

- **[[Def - Closed and Exact Forms]] and the algebra of $d^2 = 0$.** The Maxwell relations are the simplest physical instance of "exact forms are closed". Every thermodynamic potential's differential is exact (since the potential is a smooth function), hence closed, hence its coefficients have equal cross-partials. The same algebra ($d^2 = 0$ on a state function) generates an entire family of identities, of which the four Maxwell relations are the four most useful.

- **[[Def - Thermodynamic Potential (U, H, F, G)]]**. The Maxwell relations are *one Maxwell relation per potential*, with the relation's content depending on which Legendre transform of $U$ the potential is. The structural backbone of the Maxwell-relation family is the Legendre cube on the four potentials, and the Maxwell relations are the four edges of this cube viewed as $d^2 = 0$ identities.

- **De Rham cohomology and topology of $M$.** The existence of the thermodynamic potentials (as globally defined functions on $M$) depends on the topology of $M$ — specifically, that the relevant 1-forms ($T\, dS - p\, dV$ etc.) are not only closed but exact. For simply connected $M$, every closed 1-form is exact (Poincaré lemma), so the potentials exist globally. For multiply connected $M$, there can be obstructions — but for the topology of a simple thermodynamic state space (essentially Euclidean), no obstruction arises. The connection to de Rham cohomology is subtle here: thermodynamics happens on contractible domains, so cohomology is trivial, but in more exotic settings (gauge-theoretic thermodynamics, black-hole horizon topology) cohomological obstructions become physically relevant.

- **Symplectic geometry and the Hamilton-Jacobi equation.** The four thermodynamic potentials are formally analogous to the four "generating functions" of canonical transformations in Hamiltonian mechanics — $F_1(q, Q), F_2(q, P), F_3(p, Q), F_4(p, P)$ — with $(q, p)$ being position-momentum analogues of $(V, p)$ or $(S, T)$. The "Maxwell relations" of mechanics are the cross-partial identities of these generating functions, governing canonical transformations between different choices of independent variables. See [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]] for the symplectic-geometric framework, where the analogy is made precise.

---

# Unlocked by This

> [!tip] Joule-Thomson and Throttling Processes *(from this topic)*
> The Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ is the key to computing the **Joule-Thomson coefficient** $\mu_{JT} = (\partial T/\partial p)_H$ governing temperature changes in throttled (isenthalpic) expansion. For ideal gases $\mu_{JT} = 0$; for real gases it changes sign at the inversion temperature, which determines whether a gas cools or heats on throttling. See [[Ex - Joule-Thomson Coefficient from Thermodynamic Identities]].

> [!tip] Statistical Mechanics Identification of $T$ and $S$ *(from Statistical Mechanics)*
> The Maxwell relations are macroscopic; their microscopic origin is the relation $1/T = (\partial S/\partial U)_V$ in the Gibbs/Boltzmann formulation. **Statistical mechanics** *computes* the entropy from microstates and verifies that the resulting thermodynamic potentials satisfy the Maxwell relations automatically. This is one of the central self-consistency checks of statistical mechanics — the macroscopic identities derived from $d^2 = 0$ must agree with the microscopic computation, and they do. The agreement provides strong evidence for the validity of the statistical-mechanics framework.

> [!tip] Non-Equilibrium Generalisations: Linear Response and Onsager Reciprocity *(from Non-Equilibrium Statistical Mechanics)*
> The Maxwell relations are equilibrium identities. The non-equilibrium generalisation, due to Onsager (1931), is the **Onsager reciprocity relations** for linear response: in a system slightly out of equilibrium with conjugate forces $X_i$ and fluxes $J_i = \sum_j L_{ij} X_j$, the transport coefficient matrix $L$ is symmetric: $L_{ij} = L_{ji}$. This is the non-equilibrium analogue of $d^2 = 0$, and its microscopic origin is **time-reversal invariance** of the underlying dynamics. Onsager reciprocity is the foundation of irreversible thermodynamics, fluctuation-dissipation, and the modern theory of transport phenomena — the **fluctuation-dissipation theorem** is its most refined version.

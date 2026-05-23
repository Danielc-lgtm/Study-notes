---
type: exercise
subject: thermodynamics
difficulty: "⭐"
prereqs:
  - "Def - Heat 1-Form and Work 1-Form"
  - "Def - The First Law of Thermodynamics"
  - "Def - Closed and Exact Forms"
tags: [physics, thermodynamics, ideal-gas]
---

# Problem Statement

For a simple ideal gas of $n$ moles with $f$ molecular degrees of freedom, the equation of state is $pV = nRT$ and the internal energy is $U = (f/2) nRT$. Take state-space coordinates $(V, T)$ with $V, T > 0$.

1. Compute the heat 1-form $\delta Q$ in coordinates $(V, T)$.
2. Verify that $\delta Q$ is *not closed* by computing $d(\delta Q)$.
3. Show that the function $\lambda = T$ is an integrating factor: $\delta Q / T$ is exact, and compute its integral.
4. Verify that $\lambda = V$ is *not* an integrating factor by computing $d(\delta Q/V)$ and showing it is nonzero.

**Recall:**

The [[Def - The First Law of Thermodynamics|first law of thermodynamics]] is
$$dU = \delta Q - \delta W,$$
so $\delta Q = dU + \delta W$.

For a simple gas, the [[Def - Heat 1-Form and Work 1-Form|work 1-form]] is $\delta W = p\, dV$. The internal energy is a state function with exact differential $dU$. The heat 1-form $\delta Q$ is defined as $dU + p\, dV$ and is generally not exact.

A 1-form $\omega = a(V, T)\, dV + b(V, T)\, dT$ on a 2-manifold is [[Def - Closed and Exact Forms|exact]] (equivalently closed, on $\mathbb{R}^2$) iff $\partial a/\partial T = \partial b/\partial V$.

---

# Convergent Strategy

**Problem class:** This is a direct-computation problem of the type "compute a 1-form, test its exactness, find an integrating factor". It is the simplest possible instance of the integrating-factor question raised by the Caratheodory–Frobenius theorem, and serves as a sanity check that the abstract theorem produces concrete answers on the simplest physical example. The pattern is followed by every more complex computation in the chapter: write $\delta Q$ in coordinates, test exactness, find $T$ and $S$.

**Assumption pattern:** The equation of state $pV = nRT$ together with the internal energy formula $U = (f/2) nRT$ for an ideal gas completely determines all derivatives on the state space. The two-dimensionality of the state space is essential: every 1-form on a 2-manifold is automatically integrable (the Frobenius obstruction $\theta \wedge d\theta$ is a 3-form on a 2-manifold, hence zero), so the existence of an integrating factor is guaranteed by dimension counting — the exercise is to *find* it explicitly.

**Theorem routing:** The first law converts the heat 1-form into an algebraic expression $\delta Q = dU + \delta W$. With $U(T) = (f/2) nRT$ and $\delta W = p(V, T)\, dV = (nRT/V)\, dV$, we get $\delta Q$ in coordinates. The exactness test $\partial a/\partial T = \partial b/\partial V$ is the elementary calculus criterion. The integrating-factor identification "$\lambda = T$ works" is by inspection (the $T$ factor on the $\delta W$ piece is exactly cancelled by dividing through), and the integral is obtained by elementary integration.

**Key decision point:** The non-obvious choice is *which* coordinates to use. The pair $(V, T)$ makes the equation of state explicit and gives $\delta Q$ in a form where the integrating factor is visible by inspection ($\lambda = T$). Using $(p, V)$ or $(U, V)$ instead would give different-looking 1-forms with different-looking integrating factors. The choice of $(V, T)$ is the natural one for visualising the ideal-gas state space as a half-plane, and it is what makes the integrating factor "obviously" $T$ — the same $T$ that appears in the work term cancels when dividing through, revealing the entropy.

---

# Legal Operations Used

1. **Operation 1 from the topic page (split a 1-form using the first law).** Apply $\delta Q = dU + \delta W$ with $U = (f/2) nRT$ and $\delta W = p\, dV = (nRT/V)\, dV$ to write $\delta Q$ explicitly in $(V, T)$ coordinates.

2. **Operation 8 from the topic page (test exactness via cross-partial equality).** A 1-form $a\, dV + b\, dT$ is exact on a 2-manifold iff $\partial a/\partial T = \partial b/\partial V$. Apply this test to $\delta Q$ (to find it fails) and to $\delta Q/T$ (to find it succeeds).

3. **Operation 2 from the topic page (test integrability via the Frobenius obstruction).** Strictly speaking, on a 2-manifold $\theta \wedge d\theta = 0$ identically (since it is a 3-form on a 2-manifold), so this operation is trivially satisfied and the question reduces to finding *an* integrating factor — every 1-form on a 2-manifold has one.

---

# Hints

> [!note]- Hint 1
> Start by writing $\delta Q = dU + p\, dV$. You have $U = (f/2) nRT$, so $dU = (f/2) nR\, dT$. The work form is $\delta W = p\, dV$, and the ideal gas equation gives $p = nRT/V$.

> [!note]- Hint 2
> To test if a 1-form $a(V, T)\, dV + b(V, T)\, dT$ is closed (= exact on $\mathbb{R}^2$), compute $\partial a/\partial T$ and $\partial b/\partial V$ and check if they agree.

> [!note]- Hint 3
> If $\delta Q$ is not exact, divide by $T$ and try again. Observe that $\delta Q/T = (f/2) nR\, dT/T + nR\, dV/V$, where the two factors of $T$ in the work term (one from $p = nRT/V$, one from dividing by $T$) cancel.

> [!note]- Hint 4
> For the integral of $\delta Q/T$, recognise the standard differentials: $dT/T = d(\log T)$ and $dV/V = d(\log V)$.

---

# Solution

The proof breaks into four short computations. Step 1 writes $\delta Q$ in coordinates using the first law. Step 2 tests exactness by computing cross-partials. Step 3 produces the integrating factor $T$ and integrates to find the entropy. Step 4 confirms that not every choice of $\lambda$ works by testing $\lambda = V$ as a counterexample. The non-obvious move is recognising at Step 3 that the $T$-factor in the work term is exactly what makes $\lambda = T$ the right integrating factor — division by $T$ cancels the $T$ in the work term while turning $(f/2) nR\, dT$ into $(f/2) nR\, dT/T$, the differential of $\log T$.

**Step 1: $\delta Q$ in $(V, T)$ coordinates is $\delta Q = (nRT/V)\, dV + (f/2) nR\, dT$.**

> [!note]- Derivation
> The first law gives $\delta Q = dU + \delta W$. For the ideal gas:
> - $U = (f/2) nR T$, so $dU = (f/2) nR\, dT$ (since $U$ depends only on $T$, not on $V$).
> - $\delta W = p\, dV = (nRT/V)\, dV$ (using the ideal-gas equation $pV = nRT$).
>
> Adding:
> $$\delta Q = (f/2) nR\, dT + \frac{nRT}{V}\, dV.$$
> So in the basis $(dV, dT)$ the coefficients are $a(V, T) = nRT/V$ and $b(V, T) = (f/2)nR$.

**Step 2: $\delta Q$ is not closed.**

> [!note]- Derivation
> Compute $\partial a/\partial T = \partial(nRT/V)/\partial T = nR/V$ and $\partial b/\partial V = \partial((f/2)nR)/\partial V = 0$. Since $nR/V \neq 0$, $\partial a/\partial T \neq \partial b/\partial V$, so $\delta Q$ is not closed, hence not exact on the 2-manifold.
>
> Computing $d(\delta Q)$ directly:
> $$d(\delta Q) = d\left[\frac{nRT}{V}\, dV + (f/2) nR\, dT\right] = d\left(\frac{nRT}{V}\right) \wedge dV + d((f/2)nR) \wedge dT = \frac{nR}{V}\, dT \wedge dV + 0 = -\frac{nR}{V}\, dV \wedge dT.$$
> This is nonzero, confirming $\delta Q$ is not closed.

**Step 3: $\lambda = T$ is an integrating factor, with integral $S = (f/2) nR \log T + nR \log V + \text{const}$.**

> [!note]- Derivation
> Compute $\delta Q / T$:
> $$\frac{\delta Q}{T} = \frac{(f/2) nR\, dT + (nRT/V)\, dV}{T} = (f/2) nR\, \frac{dT}{T} + nR\, \frac{dV}{V}.$$
> Note how the $T$ in the work term has cancelled cleanly.
>
> Test exactness of $\delta Q/T$: with $a = nR/V$ and $b = (f/2) nR/T$, compute $\partial a/\partial T = 0$ and $\partial b/\partial V = 0$. They agree (both zero), so $\delta Q/T$ is exact.
>
> Integrate: recognise $dT/T = d(\log T)$ and $dV/V = d(\log V)$. So
> $$\delta Q / T = (f/2) nR\, d(\log T) + nR\, d(\log V) = d\left[(f/2) nR \log T + nR \log V\right].$$
> The function $S(V, T) = (f/2) nR \log T + nR \log V + \text{const}$ (with the constant determined by a reference state) is the entropy of the ideal gas. Verify $dS = \delta Q/T$ by direct computation.

**Step 4: $\lambda = V$ is not an integrating factor.**

> [!note]- Derivation
> Compute $\delta Q / V$:
> $$\frac{\delta Q}{V} = \frac{(f/2) nR}{V}\, dT + \frac{nRT}{V^2}\, dV.$$
> So $a = nRT/V^2$ and $b = (f/2) nR/V$. Compute $\partial a/\partial T = nR/V^2$ and $\partial b/\partial V = -(f/2) nR/V^2$.
>
> These agree only if $nR/V^2 = -(f/2) nR/V^2$, i.e., $1 = -f/2$, which is false (we need $f \geq 1$ and certainly $-f/2 < 0$). So $\partial a/\partial T \neq \partial b/\partial V$, and $\delta Q/V$ is not exact, hence $V$ is not an integrating factor for $\delta Q$.
>
> This illustrates the non-uniqueness of *failed* attempts at integrating factors but the existence of a specific working one ($\lambda = T$). The geometric reason $T$ works is that the adiabats of an ideal gas are level sets of $S = (f/2) nR \log T + nR \log V$, equivalently $TV^{2/f} = \text{const}$, and $T$ is the proportionality between the heat absorbed and the entropy gradient along the isochore.

> [!note]- Complete formal solution
> Setup: the ideal gas has equation of state $pV = nRT$ and internal energy $U(T) = (f/2) nRT$.
>
> *Step 1: $\delta Q$ in coordinates.* By the first law $\delta Q = dU + p\, dV$. Substituting $dU = (f/2) nR\, dT$ and $p = nRT/V$ gives
> $$\boxed{\delta Q = \frac{nRT}{V}\, dV + \frac{f}{2} nR\, dT.}$$
>
> *Step 2: $\delta Q$ is not closed.* Compute $d(\delta Q) = d(nRT/V) \wedge dV = (nR/V)\, dT \wedge dV = -(nR/V)\, dV \wedge dT \neq 0$. So $\delta Q$ is not closed, and in particular not exact.
>
> *Step 3: $\lambda = T$ is an integrating factor.* Compute
> $$\frac{\delta Q}{T} = \frac{f}{2} nR\, \frac{dT}{T} + nR\, \frac{dV}{V} = d\left[\frac{f}{2} nR \log T + nR \log V\right],$$
> so $\delta Q/T = dS$ where $S(V, T) = (f/2) nR \log T + nR \log V + \text{const}$. The entropy is determined up to an additive constant.
>
> *Step 4: $\lambda = V$ fails.* Compute $\delta Q / V$ and verify $\partial(nRT/V^2)/\partial T = nR/V^2$ while $\partial((f/2)nR/V)/\partial V = -(f/2) nR/V^2$; these are unequal, so $\delta Q / V$ is not exact. The wrong integrating factor produces a non-exact form.
>
> The result is the explicit entropy of the ideal gas, demonstrated to satisfy $\delta Q = T\, dS$.

---

# Key Takeaways

**Computing the heat 1-form is always the same recipe: first law plus equation of state.** Whenever you face a thermodynamic problem involving an unfamiliar substance, the heat 1-form is constructed by writing the first law $\delta Q = dU + \delta W$, expressing $\delta W$ in terms of the controllable mechanical variables (typically $p\, dV$ for a gas, but in general a sum over conjugate work pairs), and computing $dU$ from the substance's internal-energy function. For an ideal gas this gives the clean form $\delta Q = (f/2) nR\, dT + (nRT/V)\, dV$ in $(V, T)$ coordinates. For a Van der Waals gas, a paramagnet, a rubber band, or any other substance, the recipe is identical — what changes is just the specific functional form of $U$ and $p$. This trigger-reaction pattern ("see a thermodynamic problem with a new substance → write down the equation of state and apply the first law") is the most basic computational habit of thermodynamics.

**The integrating factor $\lambda = T$ for $\delta Q$ is universal, not specific to the ideal gas.** Although we showed $\delta Q / T$ is exact for the ideal gas by direct computation, the fact that $T$ is the *right* integrating factor is a consequence of the universality requirement in [[Def - Absolute Temperature and Entropy|the definition of absolute temperature]] — not a coincidence of the ideal-gas equation of state. For *any* simple substance, the integrating factor for $\delta Q$ that agrees with empirical temperature (the temperature measured by an ideal-gas thermometer) is the absolute temperature $T$. So the present computation is a verification that the abstract Caratheodory formalism is consistent with the elementary thermodynamics of the ideal gas — and it serves as the calibration point for the absolute-temperature scale.

**The form $S = C_V \log T + nR \log V$ for the ideal gas entropy is a paradigm.** The structure "heat capacity times $\log T$ plus mechanical-coefficient times $\log V$" appears throughout classical thermodynamics: for a Van der Waals gas, an additional correction term appears, but the leading structure is the same. The $\log$ behaviour reflects that entropy is *extensive* in the logarithm of the system's size (a doubling of volume doubles the number of accessible microstates only multiplicatively, contributing $nR \log 2$ to $S$). The factor $nR$ in front of $\log V$ is what produces, in statistical mechanics, the **mixing entropy** of dilute gases and the **chemical potential** dependence on concentration. Recognising this $\log V$ structure when it appears (e.g., in chemical thermodynamics or in the equation of state of dilute solutions) immediately points to the ideal-gas formula as the underlying picture.

**On a 2-manifold, integrability is automatic — the question is finding the integrating factor.** The Frobenius obstruction $\theta \wedge d\theta$ is a 3-form, hence identically zero on any 2-manifold; every 1-form on $\mathbb{R}^2$ admits an integrating factor. So the present exercise illustrates the *easy* case of Caratheodory's theorem — the integrating factor is guaranteed to exist by dimension counting, and the work is just finding it. The genuinely non-trivial case (where integrability is a real constraint) requires a state space of dimension $\geq 3$ — corresponding physically to a multi-component system or to a state space with extra control variables (e.g., magnetic field for a paramagnet). For such systems, $\delta Q \wedge d(\delta Q) = 0$ is a real condition and must be verified; for a single ideal gas the condition is empty.

---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Gauge Choice and the Lorenz Gauge"
  - "Def - The Four-Potential"
  - "Thm - Maxwell Equations"
tags: [physics, special-relativity]
---

# Problem Statement

Show that the Lorenz gauge can always be reached, and that it decouples Maxwell's equation for the potential.

1. Starting from an arbitrary potential $A$ with $\nabla\cdot A \ne 0$, show that the gauge transformation $A \to A' = A + d\chi$ changes the divergence by $\Box\chi$, so that solving $\Box\chi = -\nabla\cdot A$ achieves $\nabla\cdot A' = 0$. Conclude that the Lorenz gauge is always attainable.
2. Insert $F = dA$ into the inhomogeneous Maxwell equation $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ to obtain $\Box A^\nu - \nabla^\nu(\nabla\cdot A) = \mu_0 J^\nu$, and show that in Lorenz gauge this collapses to the wave equation $\Box A^\nu = \mu_0 J^\nu$.
3. Show that the Lorenz gauge does not fix $A$ uniquely: a residual transformation $A \to A + d\chi$ with $\Box\chi = 0$ preserves $\nabla\cdot A = 0$.
4. Contrast with the Coulomb gauge $\nabla\cdot\boldsymbol{\mathcal A} = 0$ and explain why it is not Lorentz-invariant while the Lorenz gauge is.

**Recall:**

![[Def - Gauge Choice and the Lorenz Gauge#The Definition]]

The [[Def - The Four-Potential|four-potential]] $A$ is defined up to $A \to A + d\chi$ for a scalar $\chi$, with $F = dA$ unchanged. The d'Alembertian is $\Box = \nabla_\mu\nabla^\mu$. For a scalar $\chi$, $\nabla\cdot(d\chi) = \nabla_\mu\nabla^\mu\chi = \Box\chi$.

---

# Convergent Strategy

**Problem class.** A *solve-Maxwell* setup problem, the third target of the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]]: exploit gauge freedom to simplify the field equation before solving it. The routine is to use the freedom $A \to A + d\chi$ to impose a convenient condition and watch the equation decouple.

**Assumption pattern.** The given is an arbitrary potential $A$ with $\nabla\cdot A \ne 0$. The signpost is "gauge freedom" — the potential is non-unique, so the divergence $\nabla\cdot A$ is adjustable, and the term obstructing the wave equation is exactly $\nabla(\nabla\cdot A)$. What this unlocks is that solving a single scalar wave equation for the gauge function removes the obstruction.

**Theorem routing.** The route is: $A \to A + d\chi$ shifts $\nabla\cdot A$ by $\Box\chi$; solving $\Box\chi = -\nabla\cdot A$ achieves Lorenz gauge ([[Def - Gauge Choice and the Lorenz Gauge]]); inserting $F = dA$ into [[Thm - Maxwell Equations]] gives $\Box A - \nabla(\nabla\cdot A) = \mu_0 J$, which in Lorenz gauge is $\Box A = \mu_0 J$. The residual freedom routes through $\Box\chi = 0$; the Coulomb-gauge contrast through the non-scalar character of $\nabla\cdot\boldsymbol{\mathcal A}$.

**Key decision point.** The crux is recognising that the obstruction to the wave equation, the term $\nabla^\nu(\nabla\cdot A)$, depends only on the *divergence* of $A$ — and the gauge freedom is precisely large enough to set that divergence to zero (one scalar of freedom, $\chi$, removes one scalar constraint). The decision is to attack the divergence specifically, not the full potential, because the divergence is the only gauge-dependent quantity in the equation.

---

# Legal Operations Used

1. **Operation 4 from the topic page (choose the Lorenz gauge to decouple the wave equation).** Parts 1–2 are exactly this operation: solve $\Box\chi = -\nabla\cdot A$ to impose $\nabla\cdot A = 0$, then watch the field equation become $\Box A = \mu_0 J$.

2. **Operation 1 from the topic page (write the field as $F = dA$).** Part 2 inserts $F = dA$ into the inhomogeneous Maxwell equation.

3. **Operation 3 from the topic page (convert $d{\star}F$ to the divergence).** Part 2 uses the divergence form $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$.

---

# Hints

> [!note]- Hint 1
> Under $A \to A' = A + d\chi$, compute $\nabla\cdot A' = \nabla\cdot A + \nabla\cdot(d\chi)$. Since $d\chi$ has components $\partial_\mu\chi$, its divergence is $\nabla_\mu\nabla^\mu\chi = \Box\chi$. So $\nabla\cdot A' = \nabla\cdot A + \Box\chi$. To make this zero, solve $\Box\chi = -\nabla\cdot A$ — a scalar wave equation with a known source, always solvable.

> [!note]- Hint 2
> Insert $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ into $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$: $\nabla_\mu(\partial^\mu A^\nu - \partial^\nu A^\mu) = \Box A^\nu - \partial^\nu(\nabla\cdot A) = \mu_0 J^\nu$. In Lorenz gauge $\nabla\cdot A = 0$, the second term vanishes, leaving $\Box A^\nu = \mu_0 J^\nu$.

> [!note]- Hint 3
> After imposing $\nabla\cdot A = 0$, a further transformation $A \to A + d\chi$ changes the divergence by $\Box\chi$ (Hint 1). To preserve $\nabla\cdot A = 0$, need $\Box\chi = 0$ — any solution of the homogeneous wave equation. There are infinitely many, so the Lorenz gauge is not a complete fixing.

> [!note]- Hint 4
> The Coulomb gauge $\nabla\cdot\boldsymbol{\mathcal A} = 0$ involves only the *spatial* divergence of the vector potential, in a particular observer's rest space. Is "spatial divergence in a chosen frame" a Lorentz scalar? Compare with $\nabla\cdot A = \nabla_\mu A^\mu$, which is a full four-divergence — a genuine scalar, the same in every frame.

---

# Solution

The Lorenz gauge is always reachable and decouples the field equation. Step 1 shows the gauge transformation shifts the divergence by $\Box\chi$, so a scalar wave equation achieves it; Step 2 inserts $F = dA$ and watches the equation collapse to a wave equation; Step 3 finds the residual freedom; Step 4 contrasts the Coulomb gauge. The non-obvious move is in Step 1: the divergence, the only gauge-dependent quantity, is set to zero by exactly one scalar of freedom.

**Step 1: The Lorenz gauge is always attainable.**

> [!note]- Derivation
> Under the gauge transformation $A \to A' = A + d\chi$, the divergence changes by
> $$\nabla\cdot A' = \nabla\cdot A + \nabla\cdot(d\chi) = \nabla\cdot A + \nabla_\mu\nabla^\mu\chi = \nabla\cdot A + \Box\chi,$$
> using that the components of $d\chi$ are $\partial_\mu\chi$, so $\nabla\cdot(d\chi) = \Box\chi$. To impose the [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]] $\nabla\cdot A' = 0$, choose $\chi$ to solve
> $$\Box\chi = -\nabla\cdot A.$$
> This is a scalar wave equation with the known source $-\nabla\cdot A$; the d'Alembertian is invertible (via its Green function), so a solution $\chi$ always exists. Therefore the Lorenz gauge can always be reached, starting from any potential. The gauge freedom — one scalar field $\chi$ — is exactly enough to remove the one scalar constraint $\nabla\cdot A = 0$.

**Step 2: In Lorenz gauge, Maxwell's equation becomes the wave equation.**

> [!note]- Derivation
> Insert $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ into the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$:
> $$\nabla_\mu(\partial^\mu A^\nu - \partial^\nu A^\mu) = \nabla_\mu\partial^\mu A^\nu - \partial^\nu(\nabla_\mu A^\mu) = \Box A^\nu - \partial^\nu(\nabla\cdot A) = \mu_0 J^\nu.$$
> So the general equation for the potential is
> $$\Box A^\nu - \nabla^\nu(\nabla\cdot A) = \mu_0 J^\nu,$$
> a *coupled* system: the four components of $A$ are tangled by the term $\nabla^\nu(\nabla\cdot A)$. Imposing the Lorenz gauge $\nabla\cdot A = 0$ kills this term, leaving the **wave equation**
> $$\boxed{\Box A^\nu = \mu_0 J^\nu},$$
> four *uncoupled* scalar wave equations, one for each component. This is the entire payoff of the Lorenz gauge: it decouples the system into solvable scalar equations.

**Step 3: A residual gauge freedom remains.**

> [!note]- Derivation
> Suppose $A$ already satisfies $\nabla\cdot A = 0$. A further gauge transformation $A \to A + d\chi$ preserves the Lorenz gauge iff the divergence stays zero:
> $$\nabla\cdot(A + d\chi) = \nabla\cdot A + \Box\chi = 0 + \Box\chi = 0 \iff \Box\chi = 0.$$
> So any $\chi$ solving the *homogeneous* wave equation $\Box\chi = 0$ generates an allowed transformation that keeps the Lorenz gauge. There are infinitely many such $\chi$ (any solution of the source-free wave equation), so the Lorenz gauge does **not** fix $A$ uniquely — a **residual gauge freedom** survives. It can be spent on a second condition; for instance, in vacuum one may use it to set $A_0 = 0$ (the radiation gauge), leaving only the two transverse polarisations.

**Step 4: The Lorenz gauge is Lorentz-invariant; the Coulomb gauge is not.**

> [!note]- Derivation
> The Lorenz condition $\nabla\cdot A = \nabla_\mu A^\mu$ is a **full four-divergence** — the contraction of a vector field with the derivative operator, a genuine Lorentz **scalar**. A scalar equation holds in every inertial frame at once: if $\nabla\cdot A = 0$ in one frame, a boost maps $A$ to another Lorenz-gauge potential, because the scalar $\nabla\cdot A$ transforms to itself (it equals zero in every frame). So the Lorenz gauge is **Lorentz-invariant**.
>
> The Coulomb condition $\nabla\cdot\boldsymbol{\mathcal A} = 0$ involves only the **spatial** divergence of the vector potential $\boldsymbol{\mathcal A}$, computed in a particular observer's rest space. This is *not* a Lorentz scalar: it singles out the observer's time direction (to separate $\boldsymbol{\mathcal A}$ from the scalar potential) and uses only the spatial derivatives. A boost mixes time and space, so $\nabla\cdot\boldsymbol{\mathcal A} = 0$ in one frame becomes a different, non-vanishing condition in another. The Coulomb gauge therefore holds in one frame only, and a manifestly covariant calculation must not silently use it. It is legitimate inside a fixed frame (where its simplifications — instantaneous Coulomb potential, transverse radiation field — are valuable), but never in combination with four-vector manipulations.

> [!note]- Complete formal solution
> Under $A \to A + d\chi$, $\nabla\cdot A \to \nabla\cdot A + \Box\chi$; solving $\Box\chi = -\nabla\cdot A$ (always possible, since $\Box$ is invertible) achieves the Lorenz gauge $\nabla\cdot A = 0$. Inserting $F = dA$ into $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ gives $\Box A^\nu - \nabla^\nu(\nabla\cdot A) = \mu_0 J^\nu$, which in Lorenz gauge collapses to the decoupled wave equation $\Box A^\nu = \mu_0 J^\nu$. The Lorenz gauge is not a complete fixing: a residual $A \to A + d\chi$ with $\Box\chi = 0$ preserves it. The Lorenz condition is a scalar four-divergence, hence Lorentz-invariant; the Coulomb condition $\nabla\cdot\boldsymbol{\mathcal A} = 0$ is a frame-dependent spatial divergence, not invariant, valid only inside a fixed frame. $\blacksquare$

---

# Key Takeaways

**Gauge freedom is exactly the right size to remove the obstruction in the field equation.** The structural lesson is a counting argument: the obstruction to decoupling Maxwell's equation for the potential is the single scalar quantity $\nabla\cdot A$, and the gauge freedom is a single scalar field $\chi$ — so the freedom is precisely enough to set the obstruction to zero. The mechanism is that $\nabla\cdot A$ shifts by $\Box\chi$ under $A \to A + d\chi$, and $\Box\chi = -\nabla\cdot A$ is always solvable. The transferable principle: a gauge symmetry's "size" (the number of arbitrary functions it contains) matches the number of constraints it can impose, and choosing a gauge means spending that freedom to simplify. This same counting governs the harmonic gauge in general relativity (four coordinate functions remove four constraints, decoupling the linearised Einstein equations) and the Faddeev–Popov gauge-fixing of quantum field theory.

**Decoupling is the whole point of a gauge choice: the Lorenz gauge turns one coupled equation into four scalar wave equations.** The reusable insight is that the value of a gauge condition is measured by how much it simplifies the dynamics, and the Lorenz gauge's value is that it removes the coupling term $\nabla(\nabla\cdot A)$, leaving four *independent* scalar wave equations $\Box A^\nu = \mu_0 J^\nu$ — each solvable by the same scalar Green function. The trigger to reach for Lorenz gauge is "I must solve for the potential given the current, and the components are coupled"; the reaction is "impose $\nabla\cdot A = 0$ and solve component-by-component". This decoupling is what makes the retarded potential and the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert solution]] possible: without it, the four components would remain entangled and the scalar Green function would not apply.

**Lorentz invariance of a gauge condition hinges on whether it is a scalar; a scalar equation holds in all frames.** The diagnostic for whether a gauge survives boosts is simple and worth carrying: a condition built from a full four-divergence (like $\nabla\cdot A = \nabla_\mu A^\mu$) is a Lorentz scalar and holds in every frame, while a condition built from a spatial divergence in a chosen rest space (like $\nabla\cdot\boldsymbol{\mathcal A} = 0$) singles out a frame and is spoiled by a boost. The reusable principle: to keep a calculation manifestly covariant, every imposed condition must be a tensor equation (here, a scalar); the moment a condition refers to "the spatial part" or "this observer's frame", it breaks covariance and may only be used inside that frame. This is why relativistic radiation problems use the Lorenz gauge and atomic-physics bound-state problems use the Coulomb gauge — the choice follows from whether covariance or the instantaneous Coulomb potential is more valuable for the problem at hand.

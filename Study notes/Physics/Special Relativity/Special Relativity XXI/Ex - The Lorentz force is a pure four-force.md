---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lorentz Four-Force"
  - "Def - The Electromagnetic Field Tensor"
  - "Def - Four-Force"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

The electromagnetic four-force on a particle of charge $q$ and [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$ is postulated to be $f = qF(\cdot,U)$, linear in $U$, with $F$ a $(0,2)$ tensor.

1. Show that the requirement that $f$ be a **pure** four-force ($f\cdot U = 0$ for every four-velocity) forces $F$ to be **antisymmetric**, $F_{\alpha\beta} = -F_{\beta\alpha}$.
2. Conversely, show that antisymmetry of $F$ *guarantees* $f\cdot U = 0$, so the Lorentz force automatically conserves the rest mass ($dm/d\tau = 0$).
3. Projecting onto an inertial observer $\mathcal{O}$ with the decomposition $U = \Gamma(U_0 + \mathbf{V})$, recover the spatial Lorentz force $\boldsymbol{\mathfrak{F}} = q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$ and the power $d\mathfrak{E}/dt = q\,\mathbf{E}\cdot\mathbf{V}$.
4. Conclude that a magnetic field does no work on a charged particle.

**Recall:**

![[Def - The Lorentz Four-Force#The Definition]]

A [[Def - Four-Force|four-force]] is the proper-time derivative of four-momentum, $f = dP/d\tau$, and the **mass-evolution identity** says $f\cdot U = c^2\,dm/d\tau$ (in units where it is $dm/d\tau$ with $c=1$); a **pure** four-force has $f\cdot U = 0$, conserving rest mass. The [[Def - The Electromagnetic Field Tensor|field tensor]] decomposes relative to $\mathcal{O}$ into $\mathbf{E} = F(\cdot,U_0)$ and $c\mathbf{B} = \star F(U_0,\cdot)$.

---

# Convergent Strategy

**Problem class.** A *structural-consequence* problem from [[Special Relativity XXI — The Electromagnetic Field#Problem-Solving Strategy|§21.1]]: derive the antisymmetry of $F$ from a physical requirement, and read off the consequences. The routine is index manipulation plus projection onto an observer.

**Assumption pattern.** The force is *linear* in $U$ (so $F$ is bilinear) and *pure* (so $f\cdot U = 0$). These two assumptions, together, are exactly what pin down the antisymmetry — linearity makes $F$ a bilinear form, purity makes it vanish on the diagonal, and a bilinear form vanishing on the diagonal is antisymmetric. The signpost is that "pure four-force" is the physical statement of "conserves rest mass".

**Theorem routing.** Parts 1–2 route through the contraction $f\cdot U = qF_{\alpha\beta}U^\alpha U^\beta$ and the algebraic fact that a quadratic form vanishing for all $U$ forces antisymmetry of the bilinear form. Part 3 routes through the observer decomposition of $F$ (the [[Def - The Electromagnetic Field Tensor|field-tensor page]]) and the four-velocity split. Part 4 is the temporal component of part 3.

**Key decision point.** The non-obvious step is recognising that "$F_{\alpha\beta}U^\alpha U^\beta = 0$ for all $U$" implies antisymmetry — not just for unit timelike $U$ but, by the open-set argument, for all $U$, and hence at the level of the tensor. The temptation is to conclude only that the *symmetric part* of $F$ annihilates timelike vectors; the resolution is that a symmetric bilinear form vanishing on an open set of vectors vanishes identically.

---

# Legal Operations Used

1. **Operation 1 (assemble/read the field tensor)** from the topic page: use the decomposition of $F$ into $\mathbf{E}$ and $\mathbf{B}$ relative to an observer. This is used in part 3 to project the four-force.

2. **Operation 9 (project the four-force onto an observer)** from the topic page: split $f = qF(\cdot,U)$ into spatial and temporal parts. This is the substance of parts 3 and 4.

---

# Hints

> [!note]- Hint 1
> Compute $f\cdot U = f_\alpha U^\alpha = qF_{\alpha\beta}U^\beta U^\alpha$. The product $U^\alpha U^\beta$ is symmetric in $\alpha,\beta$; contracting it with $F_{\alpha\beta}$ picks out only the *symmetric* part of $F$. Demanding this vanish for all $U$ forces the symmetric part of $F$ to vanish.

> [!note]- Hint 2
> If $F_{\alpha\beta} = -F_{\beta\alpha}$, then $F_{\alpha\beta}U^\alpha U^\beta = -F_{\beta\alpha}U^\alpha U^\beta = -F_{\alpha\beta}U^\beta U^\alpha$ (relabel) $= -F_{\alpha\beta}U^\alpha U^\beta$, so the quantity equals its own negative and is zero. Hence $f\cdot U = 0$ automatically.

> [!note]- Hint 3
> Write $U = \Gamma(U_0 + \mathbf{V})$ with $\mathbf{V}\cdot U_0 = 0$, and use $\mathbf{E} = F(\cdot,U_0)$, $c\mathbf{B} = \star F(U_0,\cdot)$. The spatial part of $f = qF(\cdot,U)$ comes out as $q\Gamma(\mathbf{E} + \mathbf{V}\times\mathbf{B})$; dividing the proper-time rate by $\Gamma$ to get the coordinate-time rate gives $\boldsymbol{\mathfrak{F}} = q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$.

> [!note]- Hint 4
> The temporal component of $f$ is $q\Gamma\,\mathbf{E}\cdot\mathbf{V}$, so $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$ — there is *no* $\mathbf{B}$ term. With $\mathbf{E} = 0$ the power is zero: a magnetic field does no work.

---

# Solution

The plan: derive antisymmetry from purity (Step 1), show the converse (Step 2), project to recover the elementary Lorentz force and power (Step 3), and read off that the magnetic field does no work (Step 4). The pivotal algebraic fact is that a bilinear form whose associated quadratic form vanishes identically must be antisymmetric.

**Step 1: Purity forces antisymmetry.**

> [!note]- Derivation
> The four-force is $f_\alpha = qF_{\alpha\beta}U^\beta$, so
> $$f\cdot U = f_\alpha U^\alpha = q\,F_{\alpha\beta}U^\alpha U^\beta.$$
> Split $F$ into symmetric and antisymmetric parts, $F_{\alpha\beta} = F_{(\alpha\beta)} + F_{[\alpha\beta]}$. Since $U^\alpha U^\beta$ is symmetric under $\alpha\leftrightarrow\beta$, its contraction with the antisymmetric part vanishes, leaving
> $$f\cdot U = q\,F_{(\alpha\beta)}U^\alpha U^\beta.$$
> The purity requirement $f\cdot U = 0$ must hold for *every* four-velocity $U$ (every future-directed unit timelike vector). The quadratic form $Q(U) = F_{(\alpha\beta)}U^\alpha U^\beta$ thus vanishes on the open set of timelike vectors; a polynomial (here quadratic) vanishing on an open set vanishes identically, so $F_{(\alpha\beta)} = 0$. Therefore $F$ has no symmetric part: $F_{\alpha\beta} = F_{[\alpha\beta]} = -F_{\beta\alpha}$. The field tensor is **antisymmetric** — a 2-form.

**Step 2: Antisymmetry guarantees purity.**

> [!note]- Derivation
> Conversely, suppose $F_{\alpha\beta} = -F_{\beta\alpha}$. Then
> $$f\cdot U = qF_{\alpha\beta}U^\alpha U^\beta = -qF_{\beta\alpha}U^\alpha U^\beta = -qF_{\alpha\beta}U^\beta U^\alpha = -(f\cdot U),$$
> where the second equality uses antisymmetry and the third relabels the dummy indices $\alpha\leftrightarrow\beta$. A quantity equal to its own negative is zero, so $f\cdot U = 0$: the Lorentz force is automatically pure. By the [[Def - Four-Force|mass-evolution identity]] $f\cdot U \propto dm/d\tau$, this means $dm/d\tau = 0$: **the rest mass is conserved**. A charged particle in any electromagnetic field keeps its rest mass — it is accelerated and deflected but never converted.

**Step 3: Project to the elementary Lorentz force and power.**

> [!note]- Derivation
> Decompose the particle's four-velocity relative to $\mathcal{O}$: $U = \Gamma(U_0 + \mathbf{V})$, with $\Gamma = U\cdot U_0$ and $\mathbf{V}\cdot U_0 = 0$ the velocity in the rest space. The field, relative to $\mathcal{O}$, has $\mathbf{E} = F(\cdot,U_0)$ and the magnetic field entering through the rest-space part. Compute $f = qF(\cdot,U) = q\Gamma\,F(\cdot,U_0) + q\Gamma\,F(\cdot,\mathbf{V})$.
>
> The first term is $q\Gamma\,\mathbf{E}$ (plus a temporal piece). The second term, $q\Gamma F(\cdot,\mathbf{V})$, contains the magnetic action: using the [[Def - The Electromagnetic Field Tensor|decomposition]] $F = \underline{U_0}\wedge\mathbf{E} + \star(\underline{U_0}\wedge c\mathbf{B})$ and contracting with $\mathbf{V}$ (which lies in the rest space, $\perp U_0$), the magnetic part gives $q\Gamma\,\mathbf{V}\times\mathbf{B}$. Collecting the spatial (rest-space) part of $f$:
> $$f_{\text{spatial}} = q\Gamma(\mathbf{E} + \mathbf{V}\times\mathbf{B}).$$
> This is the proper-time rate of change of spatial momentum. The *coordinate-time* rate (dividing by $\Gamma = dt/d\tau$) is the spatial **Lorentz force**
> $$\boldsymbol{\mathfrak{F}} = \frac{d\mathbf{p}}{dt} = q(\mathbf{E} + \mathbf{V}\times\mathbf{B}).$$
> The temporal part of $f$ is $f^0 = q\Gamma\langle\mathbf{E},\mathbf{V}\rangle = q\Gamma\,\mathbf{E}\cdot\mathbf{V}$, the proper-time rate of energy; dividing by $\Gamma$ gives the power
> $$\frac{d\mathfrak{E}}{dt} = q\,\mathbf{E}\cdot\mathbf{V}.$$

**Step 4: The magnetic field does no work.**

> [!note]- Derivation
> The power $d\mathfrak{E}/dt = q\,\mathbf{E}\cdot\mathbf{V}$ from Step 3 contains *only* the electric field — there is no magnetic term. The reason is structural: the magnetic contribution to the force, $q\mathbf{V}\times\mathbf{B}$, is perpendicular to $\mathbf{V}$, so it does zero work ($\mathbf{V}\cdot(\mathbf{V}\times\mathbf{B}) = 0$). Hence in a *purely magnetic* field ($\mathbf{E}=0$), $d\mathfrak{E}/dt = 0$: the energy, the Lorentz factor $\Gamma$, and the speed are all constant. **A magnetic field bends a trajectory but never changes a particle's energy.** This is the cornerstone of accelerator physics: magnets steer, electric fields accelerate, and every joule of beam energy is delivered by an electric field (the total gain over a path being $q\int\mathbf{E}\cdot d\mathbf{x} = q\Delta V$).

> [!note]- Complete formal solution
> Writing $f\cdot U = qF_{\alpha\beta}U^\alpha U^\beta$, the symmetric product $U^\alpha U^\beta$ contracts only the symmetric part $F_{(\alpha\beta)}$; purity $f\cdot U = 0$ for all timelike $U$ forces $F_{(\alpha\beta)} = 0$ (a quadratic vanishing on an open set vanishes), so $F$ is antisymmetric. Conversely antisymmetry gives $f\cdot U = -f\cdot U = 0$ by relabelling, hence $dm/d\tau = 0$ (rest mass conserved). Projecting $f = qF(\cdot,U)$ with $U = \Gamma(U_0+\mathbf{V})$ onto $\mathcal{O}$ yields the spatial force $\boldsymbol{\mathfrak{F}} = q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$ and the power $d\mathfrak{E}/dt = q\mathbf{E}\cdot\mathbf{V}$. The power has no magnetic term because $q\mathbf{V}\times\mathbf{B}\perp\mathbf{V}$; hence a magnetic field does no work, and in a pure magnetic field the speed is constant. $\blacksquare$

---

# Key Takeaways

**Antisymmetry of the field is forced by rest-mass conservation, not assumed.** The whole logical structure of electromagnetism's covariant formulation rests on this equivalence: "the Lorentz force is pure" ($f\cdot U = 0$) $\Leftrightarrow$ "the field tensor is antisymmetric" $\Leftrightarrow$ "the rest mass is conserved" ($dm/d\tau = 0$). One does not *postulate* that $F$ is a 2-form; it is *derived* from the physical demand that electromagnetism accelerate a particle without changing what it is. The reusable algebraic fact — a bilinear form whose quadratic form vanishes identically is antisymmetric — recurs whenever a "pure" (orthogonal-to-velocity) four-force is built from a linear coupling: it is exactly why the field strength of *any* gauge interaction is antisymmetric. The trigger "force linear in velocity and rest-mass-preserving" should immediately suggest "antisymmetric coupling tensor".

**The magnetic field does no work — the single most useful fact in the chapter.** That the power is $q\mathbf{E}\cdot\mathbf{V}$ with no magnetic term, because $q\mathbf{V}\times\mathbf{B}\perp\mathbf{V}$, is the workhorse of every energy and trajectory argument. In any purely magnetic region the speed, energy, and $\Gamma$ are constant, which often collapses a hard dynamics problem to a kinematics one (the [[Thm - Motion of a Charge in a Uniform Field|cyclotron motion]] is circular at *constant* speed for exactly this reason). The accelerator corollary — total energy gain is $q\Delta V$, delivered entirely by electric fields, with magnets only steering — organises the design of every machine from the cyclotron to the LHC. Whenever energy or speed is in question, the first move is to ask whether the field doing work is electric (it changes the energy) or magnetic (it does not).

**Projection turns the covariant law into the textbook law.** The covariant four-force $f = qF(\cdot,U)$ is the frame-independent object; the elementary $\boldsymbol{\mathfrak{F}} = q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$ and power $q\mathbf{E}\cdot\mathbf{V}$ are its projection onto a particular observer, obtained by splitting $U = \Gamma(U_0+\mathbf{V})$ and the field into $\mathbf{E}$ and $\mathbf{B}$. This is the general pattern of the chapter: every familiar three-vector law is the shadow of a four-vector or tensor law, recovered by choosing an observer. The advantage of the covariant form is that it is manifestly frame-independent and makes structural facts (purity, rest-mass conservation) one-line consequences of antisymmetry, whereas the projected form is frame-bound and hides them. The reusable skill is to move fluently between the two — compute covariantly, interpret by projecting.

---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Differential Form"
  - "Def - The Exterior Derivative"
  - "Def - Orientation and the Integral of a Form"
  - "Thm - The General Stokes Theorem"
  - "Thm - Green's Theorem"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $M \subseteq \mathbb{R}^3$ is a compact oriented $C^1$ surface with boundary $\partial M$, a closed curve carrying the induced orientation. The positive unit normal field on $M$ is $N$; the forward unit tangent field on $\partial M$ is $T$. A $C^1$ vector field is $F = (F_1, F_2, F_3)$; its **curl** is $\operatorname{curl} F = (\partial_y F_3 - \partial_z F_2,\ \partial_z F_1 - \partial_x F_3,\ \partial_x F_2 - \partial_y F_1)$. The surface element is $dS$, the arc-length element $ds$. The $1$-form of $F$ is $\varphi_F = F_1\,dx + F_2\,dy + F_3\,dz$. The full symbol registry is on [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

---

# Statement

> **The Kelvin-Stokes Theorem.** Let $M \subseteq \mathbb{R}^3$ be a compact oriented $C^1$ surface with boundary $\partial M$, and let $F$ be a $C^1$ vector field on a neighbourhood of $M$. Then
> $$\iint_M(\operatorname{curl} F)\cdot N\;dS = \oint_{\partial M} F\cdot T\;ds,$$
> where $N$ is the positive unit normal to $M$ (fixed by the orientation) and $T$ the forward unit tangent to $\partial M$ (the induced orientation). The flux of the curl of $F$ through the surface equals the circulation of $F$ around the boundary.
>
> **Form-theoretic statement.** With $\varphi_F = F_1\,dx + F_2\,dy + F_3\,dz$ the $1$-form of $F$, the exterior derivative $d\varphi_F$ is the $2$-form encoding $\operatorname{curl} F$, and the theorem is the case $\beta = \varphi_F$ of [[Thm - The General Stokes Theorem|the general Stokes theorem]]: $\iint_M d\varphi_F = \oint_{\partial M}\varphi_F$.
>
> **Corollary (curl-free fields).** If $\operatorname{curl} F = 0$ on a simply connected domain, then $\oint_\gamma F\cdot T\,ds = 0$ for every closed curve $\gamma$, so $F$ is conservative.

---

# Motivation

The Kelvin-Stokes theorem answers a question about *rotation*. Given a vector field — a fluid flow, a magnetic field — and a closed loop, the **circulation** $\oint_{\partial M} F\cdot T\,ds$ measures how much the field "goes around" the loop: it is the work done traversing the loop, positive if the field tends to push you along, zero if the field is perpendicular to your motion. The question is: *what local quantity accumulates into this global circulation?* The answer is the curl. The theorem says the circulation around a loop equals the total flux of $\operatorname{curl} F$ through any surface the loop bounds — so $\operatorname{curl} F$ is the *local density of circulation*, the infinitesimal rotation of the field at each point.

This gives the curl its meaning. The components of $\operatorname{curl} F$ look, in coordinates, like an arbitrary combination of partial derivatives; the theorem reveals what they *measure*. Place a tiny paddle-wheel in the flow at a point; it spins at a rate proportional to $\operatorname{curl} F$ there, with the axis along $\operatorname{curl} F$. The circulation around a large loop is the sum of all these tiny spins over a spanning surface — adjacent paddle-wheels cancel along shared edges, and only the boundary loop survives.

There is a second, computational, motivation. The theorem gives you a remarkable freedom: the surface $M$ in $\iint_M(\operatorname{curl} F)\cdot N\,dS$ is *not* fixed by the problem — *any* surface with the given boundary curve works, and they all give the same answer. So a circulation around an awkward space curve can be computed by spanning the curve with whatever surface is most convenient, often a flat disk. Conversely, a hard flux-of-curl integral over a complicated surface can be replaced by a line integral around its (possibly simple) boundary. And it is, like its siblings, just [[Thm - The General Stokes Theorem|the general Stokes theorem]] — here for the $1$-form $\varphi_F$ on a $2$-surface, since $d\varphi_F$ is exactly the curl $2$-form.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$: *$M$ is a compact oriented $C^1$ surface with boundary, and $F$ is $C^1$ near $M$.*

The first disguised source is **a closed space curve along which a circulation is wanted**. The property $B$: "a piecewise-$C^1$ closed curve $\gamma$ in $\mathbb{R}^3$ and a field $F$." The bridge: $\gamma$ bounds some surface $M$ (it is a closed loop, hence the boundary of a spanning surface), and Kelvin-Stokes converts $\oint_\gamma F\cdot T\,ds$ into a flux of $\operatorname{curl} F$. The non-obvious step is *choosing* the spanning surface — any one works, so pick the simplest. *Example problem:* the circulation around a polygonal space curve, computed by spanning it with a flat surface (see [[Ex - Circulation of a vector field via Stokes' theorem]]).

The second disguised source is **a surface presented as a graph or a parametrized patch**. The property $B$: "$M$ is the graph $z = u(x,y)$ over a planar region, or the image of a single chart." The bridge: a graph is a $C^1$ oriented surface with boundary the lifted boundary of the base region; pulling $\varphi_F$ back to the base region reduces Kelvin-Stokes to [[Thm - Green's Theorem|Green's theorem]]. The non-obviousness: the three-dimensional theorem on a graph is the two-dimensional theorem in disguise. *Example problem:* verifying Kelvin-Stokes on a paraboloid cap by pulling back to the base disk.

The third disguised source is **a flux integral whose integrand happens to be a curl**. The property $B$: "you must compute $\iint_M G\cdot N\,dS$ and $G = \operatorname{curl} F$ for some $F$ (equivalently $\operatorname{div} G = 0$, by the Poincaré lemma on a contractible domain)." The bridge: write $G = \operatorname{curl} F$ and apply Kelvin-Stokes to replace the surface integral by a boundary line integral. The non-obvious step is recognizing a divergence-free field as a curl. *Example problem:* the flux of a divergence-free field through a surface, computed as a circulation around its rim.

**Targets (Output Amplification)**

The conclusion $C$: $\iint_M(\operatorname{curl} F)\cdot N\,dS = \oint_{\partial M} F\cdot T\,ds$.

Combine $C$ with **two surfaces sharing the same boundary**. If $M_1$ and $M_2$ both have boundary $\gamma$, then $C$ gives $\iint_{M_1}(\operatorname{curl} F)\cdot N\,dS = \oint_\gamma F\cdot T\,ds = \iint_{M_2}(\operatorname{curl} F)\cdot N\,dS$. The further result $E$: the flux of a curl depends only on the *boundary curve*, not the spanning surface — surface-independence of the flux of a curl. The non-obviousness: a surface integral turns out to depend on one-dimensional data only. This is exactly the freedom to choose a convenient spanning surface.

Combine $C$ with **a curl-free field on a simply connected domain**. If $\operatorname{curl} F = 0$, the left side of $C$ is zero for every surface, so $\oint_\gamma F\cdot T\,ds = 0$ for every contractible loop $\gamma$. The further result $E$, with the [[Thm - The Poincaré Lemma|Poincaré lemma]], is that $F$ is conservative — it has a potential, and line integrals are path-independent. The non-obviousness: a pointwise condition (vanishing curl) plus a topological condition (simple connectivity) yields global path-independence. The simple-connectivity hypothesis is essential — the angular field of [[Ex - A closed form that is not exact]] is curl-free on the punctured plane yet not conservative.

Combine $C$ with **a closed surface (no boundary)**. If $M$ is closed, $\partial M = \emptyset$, and $C$ gives $\iint_M(\operatorname{curl} F)\cdot N\,dS = 0$ — the flux of any curl through a closed surface vanishes. The further result $E$ is the identity $\operatorname{div}\operatorname{curl} F = 0$ in integral form, and the fact that field lines of a curl close up. The non-obviousness: combining Kelvin-Stokes (no boundary) with the divergence theorem recovers $d^2 = 0$ as a statement about fluxes.

---

# Why Is It True

The Kelvin-Stokes theorem is true for the universal "interior cancels, boundary survives" reason, and the cleanest way to see it is the paddle-wheel tiling, parallel to the box-tiling picture for the divergence theorem.

Tile the surface $M$ with a fine mesh of tiny patches. For each tiny patch, the circulation of $F$ around its little boundary loop is — by the very definition of curl as circulation density — approximately $(\operatorname{curl} F)\cdot N$ times the patch's area. Now sum these tiny circulations over all the patches. Here is the cancellation: every *internal* edge of the mesh is shared by two adjacent patches, and that edge is traversed in one direction as part of one patch's loop and in the *opposite* direction as part of the neighbour's loop. The two contributions of every internal edge cancel. The only edges that survive the sum are those on the actual boundary $\partial M$, traversed once. So the sum of tiny circulations equals the circulation around $\partial M$. But the sum of tiny circulations is also the sum of $(\operatorname{curl} F)\cdot N\times(\text{patch area})$, which in the fine-mesh limit is $\iint_M(\operatorname{curl} F)\cdot N\,dS$. The two sides are equal because both count the same total circulation — once patch-by-patch, once by edge cancellation.

This is the meaning of curl: $\operatorname{curl} F$ at a point, dotted with a unit normal $N$, is the limiting circulation-per-unit-area of $F$ around a tiny loop in the plane perpendicular to $N$. The theorem says local circulation densities, summed, give global circulation — and the summing works because internal edges, traversed twice in opposite directions, contribute nothing. One should *expect* the theorem to hold once one accepts that curl measures local rotation: local rotations accumulate into global circulation precisely because circulation is additive over a tiling and internal walls cancel.

The surface-independence of the flux of the curl is then no surprise. If two surfaces share a boundary, the difference of their curl-fluxes is the flux through the *closed* surface they together bound, which is zero — either because a closed surface has no boundary loop, or because the flux of a curl through a closed surface is $\iint_{\text{closed}}\operatorname{div}\operatorname{curl} F\,dV = 0$. The form-theoretic proof packages all of this: the patch-cancellation is the partition of unity, and "$\operatorname{curl} F$ is the circulation density" is the identity $d\varphi_F = $ (curl $2$-form).

---

# What Makes This Hard

The genuine difficulty is the **orientation pairing between the surface and its boundary**: the positive normal $N$ on $M$ and the forward tangent $T$ on $\partial M$ must satisfy the right-hand-rule compatibility ($N$, the outward-tangent $\nu$, and $T$ form a positively oriented frame), and choosing them inconsistently flips the sign of one side. The conceptual subtlety is that **the surface is not determined by the problem** — any surface spanning the given boundary works, and recognizing this freedom (rather than computing over the surface literally handed to you) is the key problem-solving move. The most common error is the **simple-connectivity oversight**: concluding "$\operatorname{curl} F = 0$, therefore $F$ conservative" without checking the domain is simply connected — false on the punctured-axis domain, where a curl-free field can have nonzero circulation.

---

# Rederivation Scaffold

**High-level strategy:** Recognize Kelvin-Stokes as the general Stokes theorem for the $1$-form $\varphi_F$; the identity $d\varphi_F = $ (curl $2$-form) makes the left side a curl flux, and parametrizing by a single chart reduces the whole statement to Green's theorem in the parameter plane.

**Subgoal decomposition:**

1. **Form the $1$-form $\varphi_F$ and compute $d\varphi_F$.** Set $\varphi_F = \sum F_j\,dx_j$; then $d\varphi_F$ is the $2$-form with coefficients the components of $\operatorname{curl} F$.
   - *Hint:* This is the computation of [[Ex - Computing wedge products and exterior derivatives]] part 4.
   - *Why needed:* It exhibits the flux of the curl as $\iint_M d\varphi_F$.

2. **Identify $\iint_M d\varphi_F$ with $\iint_M(\operatorname{curl} F)\cdot N\,dS$.** The integral of the curl $2$-form over $M$ is the flux of the curl vector through $M$.
   - *Hint:* A $2$-form $G_1\,dy\wedge dz + \cdots$ integrated over an oriented surface is $\iint_M G\cdot N\,dS$.
   - *Why needed:* It is the left side of the classical statement.

3. **Reduce to Green's theorem via a chart.** Parametrize $M$ by an immersed disk $\psi$; pull $\varphi_F$ back to the parameter disk and apply Green's theorem there.
   - *Hint:* The pullback of $d\varphi_F$ is $d(\psi^*\varphi_F)$ by naturality; Green's theorem handles the planar disk.
   - *Why needed:* It proves the theorem by reducing it to the already-known $2$-dimensional case.

4. **Match the boundary integral.** The boundary of the parameter disk maps to $\partial M$, and $\oint\psi^*\varphi_F = \oint_{\partial M} F\cdot T\,ds$.
   - *Hint:* The chain rule turns the pulled-back line integral into the circulation of $F$.
   - *Why needed:* It is the right side, completing the identity.

---

# Lemma Decomposition

> [!note]- Lemma 1: The exterior derivative of $\varphi_F$ is the curl 2-form
> **Statement:** For $\varphi_F = F_1\,dx + F_2\,dy + F_3\,dz$, $d\varphi_F = G_1\,dy\wedge dz + G_2\,dz\wedge dx + G_3\,dx\wedge dy$ where $G = \operatorname{curl} F$.
>
> **Hint:** Apply the exterior derivative and collect into the three basic $2$-forms.
>
> **Why needed:** It is the identity that turns the flux of $d\varphi_F$ into the flux of the curl.
>
> > [!note]- Full proof
> > By definition, $d\varphi_F = \sum_{j,\ell}(\partial_\ell F_j)\,dx_\ell\wedge dx_j$. Collecting terms by basic $2$-form (using $dx_\ell\wedge dx_j = -dx_j\wedge dx_\ell$): the coefficient of $dy\wedge dz$ is $\partial_y F_3 - \partial_z F_2$; of $dz\wedge dx$ is $\partial_z F_1 - \partial_x F_3$; of $dx\wedge dy$ is $\partial_x F_2 - \partial_y F_1$. These are exactly the three components of $\operatorname{curl} F$. So $d\varphi_F = G_1\,dy\wedge dz + G_2\,dz\wedge dx + G_3\,dx\wedge dy$ with $G = \operatorname{curl} F$. $\square$

> [!note]- Lemma 2: A 2-form integrates to a flux
> **Statement:** For an oriented surface $M$ with positive unit normal $N$, the integral of the $2$-form $\eta_G = G_1\,dy\wedge dz + G_2\,dz\wedge dx + G_3\,dx\wedge dy$ over $M$ equals $\iint_M G\cdot N\,dS$.
>
> **Hint:** Compute $\psi^*\eta_G$ for a chart $\psi$ and recognize the surface-integral formula.
>
> **Why needed:** It identifies the integral of the curl $2$-form with the physical flux of the curl vector.
>
> > [!note]- Full proof
> > Let $\psi(u,v)$ parametrize a patch of $M$. The pullback $\psi^*\eta_G$ is computed by replacing $dx, dy, dz$ with $d\psi_1, d\psi_2, d\psi_3$ and expanding; the coefficient of $du\wedge dv$ that results is exactly $G\cdot(\psi_u\times\psi_v)$, the dot product of $G$ with the (unnormalized) normal $\psi_u\times\psi_v$. Since the positive unit normal is $N = (\psi_u\times\psi_v)/|\psi_u\times\psi_v|$ and the surface element is $dS = |\psi_u\times\psi_v|\,du\,dv$, the coefficient is $(G\cdot N)|\psi_u\times\psi_v|$. Hence $\int_M\eta_G = \iint(G\cdot N)|\psi_u\times\psi_v|\,du\,dv = \iint_M G\cdot N\,dS$. $\square$

> [!note]- Lemma 3: Reduction to Green's theorem on the parameter disk
> **Statement:** If $\psi : D \to M$ is a $C^1$ immersion of the unit disk with $\psi(\partial D) = \partial M$, then $\iint_M d\varphi_F = \oint_{\partial M}\varphi_F$ follows from Green's theorem applied to $\psi^*\varphi_F$ on $D$.
>
> **Hint:** Use that $d$ commutes with pullback and that Green's theorem is the planar case.
>
> **Why needed:** It is the proof step that derives the theorem from the already-established $2$-dimensional one.
>
> > [!note]- Full proof
> > The pulled-back form $\psi^*\varphi_F$ is a $1$-form on the disk $D \subseteq \mathbb{R}^2$. By [[Thm - Green's Theorem|Green's theorem]] applied to $D$, $\iint_D d(\psi^*\varphi_F) = \oint_{\partial D}\psi^*\varphi_F$. By naturality of the exterior derivative ($d\circ\psi^* = \psi^*\circ d$), $d(\psi^*\varphi_F) = \psi^*(d\varphi_F)$. By the definition of the integral of a form over a parametrized surface, $\iint_D\psi^*(d\varphi_F) = \iint_M d\varphi_F$ and $\oint_{\partial D}\psi^*\varphi_F = \oint_{\partial M}\varphi_F$. Chaining these equalities, $\iint_M d\varphi_F = \oint_{\partial M}\varphi_F$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M \subseteq \mathbb{R}^3$ be a compact oriented $C^1$ surface with boundary $\partial M$, and $F$ a $C^1$ vector field near $M$. Set $\varphi_F = F_1\,dx + F_2\,dy + F_3\,dz$.
>
> **Step 1.** By Lemma 1, $d\varphi_F = \eta_G$, the $2$-form encoding $G = \operatorname{curl} F$.
>
> **Step 2.** By Lemma 2, $\int_M d\varphi_F = \int_M\eta_G = \iint_M(\operatorname{curl} F)\cdot N\,dS$, where $N$ is the positive unit normal fixed by the orientation of $M$.
>
> **Step 3.** By [[Thm - The General Stokes Theorem|the general Stokes theorem]] applied to the compact oriented $C^1$ surface $M$ with boundary $\partial M$ and the $C^1$ $1$-form $\varphi_F$,
> $$\int_M d\varphi_F = \int_{\partial M}\varphi_F.$$
> (When $M$ is covered by several charts, this is established patch by patch with a partition of unity; for a single immersed-disk chart it is Lemma 3, the reduction to Green's theorem.)
>
> **Step 4.** The boundary integral $\int_{\partial M}\varphi_F = \int_{\partial M}\sum F_j\,dx_j$. Parametrizing $\partial M$ by arc length with unit tangent $T$, this is $\oint_{\partial M} F\cdot T\,ds$.
>
> **Conclusion.** Combining Steps 2–4,
> $$\iint_M(\operatorname{curl} F)\cdot N\;dS = \int_M d\varphi_F = \int_{\partial M}\varphi_F = \oint_{\partial M} F\cdot T\;ds. \qquad\blacksquare$$
>
> *Remark on orientation.* The signs are consistent precisely when $N$ and $T$ obey the right-hand rule: at a boundary point, $N$, the outward-tangent normal $\nu$ to $\partial M$ within $M$, and $T$ satisfy $N\times\nu = T$ and $\nu\times T = N$. This is the induced-orientation convention; reversing $N$ reverses $T$, and the identity holds with both signs flipped together.

---

# Cross-Field Exercise Suggestions

**Ampère's circuital law.** In magnetostatics, $\operatorname{curl} B = \mu_0 J$. Kelvin-Stokes converts this into Ampère's law: the circulation of $B$ around a closed loop equals $\mu_0$ times the current threading any surface the loop bounds. The application is foundational because the *integral* form of Ampère's law — used to compute the magnetic field of symmetric currents — is Kelvin-Stokes applied to the *differential* law, and surface-independence is what makes "the current threading the loop" well-defined.

**Faraday's law of induction.** Faraday's law $\operatorname{curl} E = -\partial_t B$ becomes, via Kelvin-Stokes, "the circulation of $E$ around a loop equals minus the rate of change of magnetic flux through it" — the integral law governing electric generators. The application shows the theorem converting a local field equation into the engineering law of electromagnetic induction.

**Kelvin's circulation theorem in fluid dynamics.** For an ideal fluid, the circulation around a loop moving with the flow is constant in time. The proof differentiates the circulation, uses Kelvin-Stokes to relate it to the flux of vorticity, and shows the vorticity flux is conserved. The application is nonobvious because a conservation law for a *loop integral* is established through the curl.

**Detecting non-simple-connectivity.** Kelvin-Stokes fails to give "$\operatorname{curl} F = 0 \Rightarrow$ conservative" on a domain that is not simply connected — the field $(-y, x, 0)/(x^2+y^2)$ on $\mathbb{R}^3$ minus the $z$-axis is curl-free yet has circulation $2\pi$ around the axis. The application is the three-dimensional version of [[Ex - A closed form that is not exact]]: the failure of Kelvin-Stokes' conservativity corollary is a detector of topology.

---

# Bridges

- **[[Thm - The General Stokes Theorem|The General Stokes Theorem]]** — Kelvin-Stokes is its case of a $1$-form on a $2$-surface in $\mathbb{R}^3$, with $\beta = \varphi_F$. The identity $d\varphi_F = $ (curl $2$-form) is what specializes the abstract theorem to the classical one.

- **[[Thm - Green's Theorem|Green's Theorem]]** — Green's theorem is Kelvin-Stokes for a *flat* surface in the plane. Conversely, the proof of Kelvin-Stokes reduces, via a chart, to Green's theorem on the parameter disk: the three-dimensional theorem is the two-dimensional one pulled back.

- **[[Thm - The Divergence Theorem|The Divergence Theorem]]** — the sibling specialization of the general Stokes theorem. The two together show $\operatorname{div}\operatorname{curl} = 0$ as a statement about fluxes: the flux of a curl through a *closed* surface is zero, because such a surface bounds a solid and the divergence theorem plus $\operatorname{div}\operatorname{curl} = 0$ apply.

- **[[Thm - The Poincaré Lemma|The Poincaré Lemma]]** — the conservativity corollary of Kelvin-Stokes is exactly the Poincaré lemma for $1$-forms in $\mathbb{R}^3$: a curl-free field is closed, and on a simply connected domain closed $1$-forms are exact, i.e. conservative.

---

# Unlocked by This

> [!tip] Maxwell's Equations and Electromagnetic Induction *(from Electromagnetism)*
> Kelvin-Stokes converts the curl Maxwell equations — Faraday's law $\operatorname{curl} E = -\partial_t B$ and Ampère's law $\operatorname{curl} B = \mu_0 J + \mu_0\varepsilon_0\partial_t E$ — into their integral forms, the circulation laws that govern induction and the magnetic field of currents. In the language of forms these are components of $dF = 0$ and $d\!\star\!F = J$.

> [!tip] The Curl and Vorticity Dynamics *(from Fluid Dynamics)*
> Kelvin-Stokes identifies the curl as the local circulation density — the vorticity. The dynamics of vorticity, governed by the vorticity transport equation and Kelvin's circulation theorem, is the modern organizing principle of fluid mechanics, and it rests on this theorem.

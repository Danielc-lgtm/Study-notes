---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Differential Form"
  - "Def - The Exterior Derivative"
  - "Def - The Wedge Product"
  - "Thm - The General Stokes Theorem"
  - "Thm - The Change of Variables Formula"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $\Omega \subseteq \mathbb{R}^n$ is a compact region with $C^1$ boundary $\partial\Omega$ (a smooth hypersurface), and $\nu$ is the outward unit normal field on $\partial\Omega$. A $C^1$ vector field is $F = (F_1, \dots, F_n)$; its **divergence** is $\operatorname{div} F = \sum_{j} \partial_j F_j$. The volume element is $dV$, the surface element on $\partial\Omega$ is $dS$. The standard volume form is $\omega = dx_1\wedge\cdots\wedge dx_n$; the interior product is $\lrcorner$. The full symbol registry is on [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

---

# Statement

> **The Divergence Theorem (Gauss's theorem).** Let $\Omega \subseteq \mathbb{R}^n$ be a compact region with $C^1$ boundary $\partial\Omega$, and let $F$ be a $C^1$ vector field on a neighbourhood of $\Omega$. Then
> $$\int_\Omega\operatorname{div} F\;dV = \int_{\partial\Omega} F\cdot\nu\;dS,$$
> where $\nu$ is the outward unit normal to $\partial\Omega$. The total of the source density $\operatorname{div} F$ over the region equals the total outward flux of $F$ across the boundary.
>
> **Form-theoretic statement.** With $\omega = dx_1\wedge\cdots\wedge dx_n$ the volume form, the $(n-1)$-form $\omega\lrcorner F = \sum_j(-1)^{j-1}F_j\,dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_n$ satisfies $d(\omega\lrcorner F) = (\operatorname{div} F)\,\omega$, and the theorem is the case $\beta = \omega\lrcorner F$ of [[Thm - The General Stokes Theorem|the general Stokes theorem]].
>
> **Integration by parts.** For $C^1$ functions $f, h$ on $\Omega$ and each index $i$,
> $$\int_\Omega(\partial_i f)\,h\;dV = -\int_\Omega f\,(\partial_i h)\;dV + \int_{\partial\Omega} f h\,\nu_i\;dS.$$

---

# Motivation

The divergence theorem is the precise mathematical statement of a conservation principle so basic it is almost a tautology: *whatever flows out across the boundary of a region must have been produced inside it.* If $F$ is the flow field of a fluid, or of heat, or of electric flux, then $F\cdot\nu$ is the rate of outflow per unit boundary area, and $\operatorname{div} F$ is the rate of production per unit volume — the "source density". The theorem says these two integrate to the same total. There is no net outflow without net production; the books balance.

The question it answers, as a computational tool, is: *which is easier — a volume integral or a surface integral?* Often the volume integral is far easier, because $\operatorname{div} F$ can be a simple function (frequently a constant) even when $F$ itself is complicated, so a messy flux through a closed surface collapses to an elementary volume integral. Sometimes the trade goes the other way. The theorem gives you both sides and lets you pick.

But the deepest motivation is that the divergence theorem is the bridge between the *differential* and the *integral* form of a physical law. The differential form of a conservation law — the continuity equation $\partial_t\rho + \operatorname{div} J = 0$ — is a statement at every point. The integral form — "the rate of change of the total inside a region equals the flux across its boundary" — is a statement about regions. The divergence theorem is exactly what converts one into the other, and it is therefore embedded in the foundations of fluid dynamics, electromagnetism, heat transfer, and every other field theory. It is also, in the form-theoretic statement, simply [[Thm - The General Stokes Theorem|the general Stokes theorem]] for the special $(n-1)$-form $\omega\lrcorner F$ — the volume form contracted with the vector field — whose exterior derivative is exactly $(\operatorname{div} F)\,\omega$. The classical divergence theorem and the abstract Stokes theorem are the same statement.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$: *$\Omega$ is a compact region with $C^1$ boundary, and $F$ is $C^1$ on all of $\Omega$.*

The first disguised source is **a flux integral through a closed surface**. The property $B$: "you must compute $\int_S F\cdot\nu\,dS$ where $S$ is a closed surface (a sphere, the boundary of a box, a torus)." The bridge: a closed surface bounds a region, and the divergence theorem converts the flux into $\int_\Omega\operatorname{div} F\,dV$. The non-obvious step is recognizing that "closed surface" means "boundary of a solid", which is the theorem's right-hand side run backwards. *Example problem:* the flux of a field through a sphere, computed as a volume integral of the divergence (see [[Ex - Flux through a closed surface]]).

The second disguised source is **a region defined as a sublevel set $\{\phi \le 0\}$ of a regular function**. The property $B$: "$\Omega = \{\phi \le 0\}$ with $\nabla\phi \neq 0$ on $\{\phi = 0\}$." The bridge: by the regular value theorem $\{\phi = 0\}$ is a $C^1$ hypersurface, so $\Omega$ has $C^1$ boundary, and $\nu = \nabla\phi/|\nabla\phi|$ is the outward normal. The non-obvious step is that an *inequality* delivers the smooth-boundary hypothesis automatically. *Example problem:* applying the theorem to the solid ball $\{|x|^2 \le 1\}$.

The third disguised source is **a product of functions you wish to integrate by parts**. The property $B$: "an integral $\int_\Omega(\partial_i f)\,h\,dV$ where one factor is a derivative." The bridge: apply the theorem to the vector field $f h\,e_i$; the product rule $\partial_i(fh) = (\partial_i f)h + f(\partial_i h)$ then yields the integration-by-parts identity, moving the derivative from $f$ to $h$ at the cost of a boundary term. The non-obviousness: multidimensional integration by parts *is* the divergence theorem in disguise. *Example problem:* the Green identities for the Laplacian, derived by parts.

**Targets (Output Amplification)**

The conclusion $C$: $\int_\Omega\operatorname{div} F\,dV = \int_{\partial\Omega} F\cdot\nu\,dS$.

Combine $C$ with **a divergence-free field, $\operatorname{div} F = 0$**. Then $C$ gives $\int_{\partial\Omega} F\cdot\nu\,dS = 0$ for *every* closed surface — the net flux of a divergence-free field through any closed surface vanishes. The further result $E$: the flux of $F$ through a surface depends only on the surface's boundary, not the surface itself, so flux is a deformation invariant. The non-obviousness: a pointwise condition becomes a global rigidity of the flux. This is the principle behind "field lines of a divergence-free field neither begin nor end".

Combine $C$ with **the product rule, applied to $uF$**. Replacing $F$ by $uF$ and using $\operatorname{div}(uF) = u\operatorname{div} F + \langle\nabla u, F\rangle$ turns $C$ into $\int_\Omega(u\operatorname{div} F + F\cdot\nabla u)\,dV = \int_{\partial\Omega} u(F\cdot\nu)\,dS$. The further result $E$, iterated, is the full suite of **Green's identities** for the Laplacian: $\int u\Delta v = -\int\nabla u\cdot\nabla v + \int_{\partial\Omega} u\,\partial_\nu v$, and the symmetric second identity. The non-obviousness: the analytic backbone of the theory of the Laplacian — uniqueness for the Dirichlet problem, the maximum principle's energy version, conservation of wave energy — is the divergence theorem combined with one product rule.

Combine $C$ with **a vector field built from a single coordinate function**. Taking $F = x_j e_j$ (no sum) gives $\operatorname{div} F = 1$, so $C$ reads $\operatorname{vol}(\Omega) = \int_{\partial\Omega} x_j\nu_j\,dS$, and averaging over $j$ gives $\operatorname{vol}(\Omega) = \tfrac1n\int_{\partial\Omega}(x\cdot\nu)\,dS$. The further result $E$ is a **volume formula from boundary data** — the $n$-dimensional analogue of Green's area formula. The non-obviousness: volume, a region quantity, is recoverable by integrating a simple expression over the boundary alone.

---

# Why Is It True

The divergence theorem is true for the "interior cancels, boundary survives" reason common to all of Stokes' theorem, but it has an especially vivid physical reading worth keeping separate from the proof.

Imagine the region $\Omega$ chopped into a fine grid of tiny boxes. For each tiny box, compute the net outflow of $F$ across its six faces (in three dimensions). Now sum this over all the boxes. Here is the key observation: every *internal* face is shared by two adjacent boxes, and the outflow across it from one box is the inflow into the other — the same number with opposite sign. When you sum over all boxes, every internal face cancels against its neighbour. The *only* faces that survive the sum are the ones on the actual boundary $\partial\Omega$, because those belong to just one box. So the sum of "net outflow from each tiny box" equals "net outflow across $\partial\Omega$" — the right-hand side of the theorem. Meanwhile, the net outflow from a single tiny box, divided by the box's volume, is — in the limit of small boxes — exactly the *definition* of the divergence of $F$ at that point. So the sum of net outflows from the boxes is the sum of $(\operatorname{div} F)\times(\text{box volume})$, which in the limit is $\int_\Omega\operatorname{div} F\,dV$ — the left-hand side. The two sides are equal because they are two ways of counting the same total outflow: once box-by-box (giving the divergence integral), once by cancellation (giving the boundary flux).

This is why the divergence is *named* the divergence: $\operatorname{div} F$ at a point *is* the infinitesimal outward flux density, the rate at which the flow "diverges" from that point. The theorem then says nothing more than "the total infinitesimal flux density, integrated up, is the total flux" — and the integrating-up works because the infinitesimal pieces telescope, internal faces cancelling. One should *expect* the theorem to hold the moment one accepts that divergence measures local outflow: local outflows, summed, must give global outflow, because flux is additive and internal walls do not count.

The form-theoretic proof makes "internal faces cancel" rigorous via the general Stokes theorem: the cancellation is the partition-of-unity reduction, and the identity $d(\omega\lrcorner F) = (\operatorname{div} F)\,\omega$ is the precise statement that "infinitesimal flux density" is the exterior derivative of "flux form".

---

# What Makes This Hard

The conceptual content is easy — the box-cancellation picture above — but the technical heart is the identity $d(\omega\lrcorner F) = (\operatorname{div} F)\,\omega$, which requires comfort with the interior product and the observation that contracting the volume form with $F$ and then differentiating produces exactly the sum of partials $\sum\partial_j F_j$. The most common error is in the **boundary term and the surface measure**: relating the abstract $\int_{\partial\Omega}\omega\lrcorner F$ to the concrete $\int_{\partial\Omega} F\cdot\nu\,dS$ requires the identity $j^*(\omega\lrcorner F) = (F\cdot\nu)\,\omega_{\partial\Omega}$, i.e. that the restriction of the flux form to the boundary is the normal component of $F$ times the induced surface element — getting the normal direction or the surface measure wrong corrupts the flux. A second frequent slip is **applying the theorem when $F$ has a singularity inside $\Omega$**, violating the "$C^1$ on all of $\Omega$" hypothesis.

---

# Rederivation Scaffold

**High-level strategy:** Recognize the divergence theorem as the general Stokes theorem applied to the flux $(n-1)$-form $\omega\lrcorner F$; the two facts to establish are that its exterior derivative is the divergence density, and that its restriction to the boundary is the normal flux.

**Subgoal decomposition:**

1. **Form the flux $(n-1)$-form.** Set $\beta = \omega\lrcorner F = \sum_j(-1)^{j-1}F_j\,dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_n$.
   - *Hint:* This is the volume form contracted with $F$; the signs $(-1)^{j-1}$ come from removing the $j$-th factor.
   - *Why needed:* It is the $(n-1)$-form whose Stokes identity will be the divergence theorem.

2. **Show $d\beta = (\operatorname{div} F)\,\omega$.** Differentiate $\beta$; the surviving terms are exactly $\sum_j\partial_j F_j$ times the volume form.
   - *Hint:* In $d$ of the $j$-th summand, only the partial $\partial_j$ survives (others repeat a factor), and the sign $(-1)^{j-1}$ cancels the reorder sign.
   - *Why needed:* It identifies the left side of Stokes, $\int_\Omega d\beta$, with $\int_\Omega\operatorname{div} F\,dV$.

3. **Show $j^*\beta = (F\cdot\nu)\,dS$ on $\partial\Omega$.** The restriction of the flux form to the boundary is the normal component of $F$ times the surface element.
   - *Hint:* At a boundary point, choose coordinates with $\partial\Omega$ tangent to a hyperplane; the contraction $\omega\lrcorner F$ restricted to that hyperplane picks out the normal component.
   - *Why needed:* It identifies the right side of Stokes, $\int_{\partial\Omega}\beta$, with $\int_{\partial\Omega} F\cdot\nu\,dS$.

4. **Apply Stokes.** Conclude $\int_\Omega\operatorname{div} F\,dV = \int_\Omega d\beta = \int_{\partial\Omega}\beta = \int_{\partial\Omega} F\cdot\nu\,dS$.
   - *Hint:* This is [[Thm - The General Stokes Theorem]] with the $\beta$ of step 1.
   - *Why needed:* It is the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: The exterior derivative of the flux form is the divergence
> **Statement:** For the flux $(n-1)$-form $\beta = \omega\lrcorner F = \sum_j(-1)^{j-1}F_j\,dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_n$, one has $d\beta = (\operatorname{div} F)\,dx_1\wedge\cdots\wedge dx_n$.
>
> **Hint:** Apply $d$ to each summand; only the partial with respect to the missing index survives.
>
> **Why needed:** It is the identity converting the abstract $\int_\Omega d\beta$ into $\int_\Omega\operatorname{div} F\,dV$.
>
> > [!note]- Full proof
> > The $j$-th summand is $(-1)^{j-1}F_j\,dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_n$. Applying $d$, the coefficient $F_j$ is differentiated; the new differential $dx_\ell$ is wedged on, and survives only if $\ell$ is the *missing* index, namely $\ell = j$. So $d$ of the $j$-th summand is $(-1)^{j-1}(\partial_j F_j)\,dx_j\wedge dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_n$. Moving $dx_j$ from the front into its sorted position requires $j-1$ transpositions, contributing a sign $(-1)^{j-1}$, which cancels the explicit $(-1)^{j-1}$. Hence $d$ of the $j$-th summand is $(\partial_j F_j)\,dx_1\wedge\cdots\wedge dx_n$. Summing over $j$, $d\beta = \big(\sum_j\partial_j F_j\big)\,\omega = (\operatorname{div} F)\,\omega$. $\square$

> [!note]- Lemma 2: The flux form restricts to the normal flux on the boundary
> **Statement:** With $j : \partial\Omega \hookrightarrow \Omega$ the inclusion, $j^*(\omega\lrcorner F) = (F\cdot\nu)\,\omega_{\partial\Omega}$, where $\nu$ is the outward unit normal and $\omega_{\partial\Omega}$ the induced surface volume form.
>
> **Hint:** Work in coordinates at a boundary point where $\partial\Omega$ is the hyperplane $\{x_1 = 0\}$ and the metric is standard.
>
> **Why needed:** It converts the abstract $\int_{\partial\Omega}\omega\lrcorner F$ into the concrete $\int_{\partial\Omega} F\cdot\nu\,dS$.
>
> > [!note]- Full proof
> > Fix $p \in \partial\Omega$ and choose orthonormal coordinates centred at $p$ in which $\partial\Omega$ is tangent to $\{x_1 = 0\}$ and the outward normal is $\nu = -e_1$ (so $\Omega$ lies in $x_1 \le 0$). Decompose $F = F_1 e_1 + F'$ where $F'$ is tangent to the boundary. The interior product $\omega\lrcorner F$ is linear in $F$, so $\omega\lrcorner F = F_1(\omega\lrcorner e_1) + \omega\lrcorner F'$. Now $\omega\lrcorner e_1 = dx_2\wedge\cdots\wedge dx_n$, which restricts on $\{x_1 = 0\}$ to the surface volume form $\omega_{\partial\Omega}$ — up to the orientation sign, which is fixed so that the outward normal comes first. And $\omega\lrcorner F'$, with $F'$ tangent, restricts to zero on the boundary because it contains a factor $dx_1$ (or, more precisely, every term pairs the tangential $F'$ against a form that vanishes on the tangent hyperplane). Hence $j^*(\omega\lrcorner F) = F_1\,\omega_{\partial\Omega}$. Since the outward normal is $\pm e_1$ and $F_1 = F\cdot e_1$, the coefficient is $\pm(F\cdot\nu)$; the induced-orientation convention fixes the sign to $+(F\cdot\nu)$. With $dS = \omega_{\partial\Omega}$, $j^*(\omega\lrcorner F) = (F\cdot\nu)\,dS$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\Omega \subseteq \mathbb{R}^n$ be a compact region with $C^1$ boundary, $F$ a $C^1$ vector field on a neighbourhood of $\Omega$, and $\omega = dx_1\wedge\cdots\wedge dx_n$ the standard volume form.
>
> **Step 1.** Define the flux $(n-1)$-form $\beta = \omega\lrcorner F = \sum_{j=1}^{n}(-1)^{j-1}F_j\,dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_n$, where $\widehat{\ }$ denotes omission.
>
> **Step 2.** By Lemma 1, $d\beta = (\operatorname{div} F)\,\omega$. Hence, integrating over $\Omega$ with the standard orientation,
> $$\int_\Omega d\beta = \int_\Omega(\operatorname{div} F)\,dx_1\cdots dx_n = \int_\Omega\operatorname{div} F\;dV.$$
>
> **Step 3.** By Lemma 2, the restriction of $\beta$ to $\partial\Omega$ (with the induced orientation) is $j^*\beta = (F\cdot\nu)\,dS$, where $\nu$ is the outward unit normal and $dS$ the surface measure. Hence
> $$\int_{\partial\Omega}\beta = \int_{\partial\Omega}(F\cdot\nu)\,dS.$$
>
> **Step 4.** $\beta$ is a $C^1$ $(n-1)$-form and $\Omega$ is a compact oriented surface with $C^1$ boundary. By [[Thm - The General Stokes Theorem|the general Stokes theorem]], $\int_\Omega d\beta = \int_{\partial\Omega}\beta$. Combining with Steps 2 and 3,
> $$\int_\Omega\operatorname{div} F\;dV = \int_{\partial\Omega} F\cdot\nu\;dS. \qquad\blacksquare$$
>
> **Integration by parts.** Apply the theorem to the vector field $G = fh\,e_i$, whose only nonzero component is $G_i = fh$. Then $\operatorname{div} G = \partial_i(fh) = (\partial_i f)h + f(\partial_i h)$, and $G\cdot\nu = fh\,\nu_i$. The theorem gives $\int_\Omega[(\partial_i f)h + f(\partial_i h)]\,dV = \int_{\partial\Omega} fh\,\nu_i\,dS$, which rearranges to $\int_\Omega(\partial_i f)h\,dV = -\int_\Omega f(\partial_i h)\,dV + \int_{\partial\Omega} fh\,\nu_i\,dS$.
>
> *Remark.* A self-contained proof not routing through the abstract Stokes theorem proceeds directly: it suffices, by linearity, to prove $\int_\Omega\partial_n f\,dx = \int_{\partial\Omega}(e_n\cdot\nu)f\,dS$ for $f$ supported near a boundary point where $\partial\Omega$ is a graph $x_n = u(x')$; integrating $\partial_n f$ in $x_n$ up to $u(x')$ by the Fundamental Theorem of Calculus gives $f(x', u(x'))$, and the identification $dS = (1 + |\nabla u|^2)^{1/2}dx'$ together with $e_n\cdot\nu = (1 + |\nabla u|^2)^{-1/2}$ completes it. The direction $e_n$ is then replaced by an arbitrary constant vector by a rotation, and summing over the standard basis gives the theorem.

---

# Cross-Field Exercise Suggestions

**Gauss's law in electrostatics.** The electric field of a point charge has $\operatorname{div} E = \rho/\varepsilon_0$ away from the charge. The divergence theorem converts this into Gauss's law: the flux of $E$ through any closed surface equals the enclosed charge over $\varepsilon_0$. The application is foundational because the *integral* form of Gauss's law — the one used to compute fields of symmetric charge distributions — is the divergence theorem applied to the *differential* form.

**Conservation of mass in fluid dynamics.** For a fluid of density $\rho$ and velocity $u$, mass conservation is the continuity equation $\partial_t\rho + \operatorname{div}(\rho u) = 0$. Integrating over a fixed region and applying the divergence theorem yields "the rate of change of mass inside equals the mass flux across the boundary". The application is the prototype of converting a local conservation law into a global balance law.

**Uniqueness for the Dirichlet problem.** If two functions both solve $\Delta u = 0$ in $\Omega$ with the same boundary values, their difference $w$ is harmonic with zero boundary data; the Green identity $\int_\Omega|\nabla w|^2 = \int_{\partial\Omega} w\,\partial_\nu w - \int_\Omega w\Delta w = 0$ then forces $\nabla w = 0$, so $w$ is constant, hence zero. The application is striking because uniqueness — an analytic rigidity — falls out of the divergence theorem plus one integration by parts.

**Archimedes' principle.** The buoyant force on a submerged solid is the integral of pressure over its surface; with pressure linear in depth, the divergence theorem converts this surface integral into a volume integral equal to the weight of displaced fluid. The application is historically the oldest "divergence theorem" computation, and it shows the theorem turning an intractable surface integral into a one-line volume integral.

---

# Bridges

- **[[Thm - The General Stokes Theorem|The General Stokes Theorem]]** — the divergence theorem is its case $k = n$, with $\beta$ the flux form $\omega\lrcorner F$. The identity $d(\omega\lrcorner F) = (\operatorname{div} F)\,\omega$ is what makes the specialization work.

- **[[Thm - Green's Theorem|Green's Theorem]]** — the divergence theorem in dimension two is exactly the divergence form of Green's theorem. The two are the same statement, one written for a planar region and one for a region in $\mathbb{R}^n$.

- **[[Thm - The Kelvin-Stokes Theorem|The Kelvin-Stokes Theorem]]** — the sibling theorem, also a case of the general Stokes theorem, but for a $1$-form on a $2$-surface rather than an $(n-1)$-form on an $n$-region. Divergence theorem: flux of a field through a closed surface. Kelvin-Stokes: flux of a curl through an open surface.

- **The Green identities and the Laplacian** — derived from the divergence theorem by inserting a gradient field $F = \nabla v$ and using product rules. They are the analytic foundation of potential theory, the theory of harmonic functions, and the energy method for the wave and heat equations.

---

# Unlocked by This

> [!tip] Maxwell's Equations in Integral Form *(from Electromagnetism)*
> The divergence theorem converts the differential Maxwell equations $\operatorname{div} E = \rho/\varepsilon_0$ and $\operatorname{div} B = 0$ into their integral forms — Gauss's law for electricity and the statement that no magnetic charge exists. In the language of forms, these are $d\!\star\!F = J$ and $dF = 0$ integrated over a region.

> [!tip] The Heat and Wave Energy Methods *(from PDE Analysis)*
> The Green identities, themselves corollaries of the divergence theorem, give the **energy method**: multiplying a PDE by the solution and integrating by parts produces a conserved or monotone energy, the standard route to uniqueness and stability for the heat, wave, and Schrödinger equations.

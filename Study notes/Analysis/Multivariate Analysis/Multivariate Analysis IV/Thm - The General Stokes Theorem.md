---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Differential Form"
  - "Def - The Exterior Derivative"
  - "Def - Pullback of a Differential Form"
  - "Def - Orientation and the Integral of a Form"
  - "Def - Submanifold of Euclidean Space"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $M$ is a compact oriented $k$-dimensional surface ([[Def - Submanifold of Euclidean Space|submanifold]]) of class $C^2$ in $\mathbb{R}^N$, with boundary $\partial M$, a $(k-1)$-dimensional surface carrying the induced orientation. A $(k-1)$-form is $\beta$; $d\beta$ is its [[Def - The Exterior Derivative|exterior derivative]]. The half-space model is $\mathbb{R}^k_- = \{x \in \mathbb{R}^k : x_1 \le 0\}$, with $\partial\mathbb{R}^k_- = \{x_1 = 0\}$. The inclusion of the boundary is $\kappa : \partial M \hookrightarrow M$. The full symbol registry is on [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

---

# Motivation

The Fundamental Theorem of Calculus says $\int_a^b f'\,dx = f(b) - f(a)$. Stare at the right-hand side: $f(b) - f(a)$ is the integral of $f$ over the *boundary* of the interval $[a,b]$, the two-point set $\{a, b\}$, with $b$ counted positively and $a$ negatively. So the theorem already has the shape "integral of a derivative over a region equals integral of the original object over the boundary". The question this theorem answers is: *is that shape an accident of one dimension, or a universal law?* It is a universal law, and the general Stokes theorem is its statement.

Before forms, this law was known only in fragments. Green's theorem handled a planar region; the divergence theorem handled a solid; the Kelvin-Stokes theorem handled a surface in space. Each was proved separately, each in its own notation, and there was no visible reason the three should be the same theorem. The obstacle to unifying them was the lack of a single object playing the role of "the thing being integrated" and a single operator playing the role of "the derivative". Differential forms supply the object; the [[Def - The Exterior Derivative|exterior derivative]] $d$ supplies the operator. Once you have them, all three classical theorems collapse into one sentence: $\int_M d\beta = \int_{\partial M}\beta$.

What makes a result like this *expectable*? The deep reason is that $d$ and $\partial$ are dual operations, and the integral is the pairing that exhibits the duality. The exterior derivative raises the degree of a form by one; the boundary operator lowers the dimension of a domain by one. Stokes' theorem says these two moves are *adjoint* with respect to integration: moving a derivative onto the form is the same as moving the integration onto the boundary. This is a structural inevitability, not a computational coincidence — and it is why the proof, once set up correctly, is short: an adjunction only needs to be verified on a generating model, and that model is the half-space, where the statement is literally the one-variable Fundamental Theorem of Calculus.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem requires a precondition $A$: *$M$ is a compact oriented $C^2$ surface with boundary, and $\beta$ is a compactly supported $C^1$ $(k-1)$-form.* The skill is recognizing this precondition in disguise.

The first disguised source is **a region defined as the sublevel set of a regular function**, $M = \{\phi \le 0\}$ with $\nabla\phi \neq 0$ on $\{\phi = 0\}$. The bridge: by the [[Def - Submanifold of Euclidean Space|regular value theorem]], $\{\phi = 0\}$ is then a smooth hypersurface, so $M$ is a surface with smooth boundary, and the sign of $\phi$ supplies the orientation (the outward normal is $\nabla\phi$). The non-obvious part is that an *inequality* — a level set condition — automatically delivers the smooth, oriented, bounded-boundary structure Stokes needs. *Example problem:* the solid ball $\{|x|^2 - 1 \le 0\}$ is a Stokes domain because $|x|^2 - 1$ is a regular defining function.

The second disguised source is **a chain of pieces glued along faces** — a region cut into finitely many cornered blocks, or a surface assembled from coordinate patches. The bridge: Stokes holds on each piece (it holds for surfaces with corners), and summing over the pieces, the integrals over internal faces cancel because each internal face is traversed twice with opposite induced orientation. The non-obviousness: a domain too irregular to be a smooth surface globally still satisfies Stokes, because the theorem is *additive over a decomposition*. *Example problem:* verifying Stokes on a solid cube, which is not smooth at its edges, by treating it as a union of cornered pieces or summing over its six faces (see [[Ex - Stokes' theorem on the boundary of a cube]]).

The third disguised source is **a form that is exact, $\beta = d\gamma$, integrated over a closed surface**. The bridge: if $\partial M = \emptyset$ then $\int_M d\beta = \int_{\partial M}\beta = 0$, so the integral of any exact top-degree form over a closed surface vanishes. The non-obvious step is recognizing that "the integrand is a derivative" plus "the surface has no boundary" forces the integral to be zero with no computation. *Example problem:* the integral of $d\beta$ over the sphere is zero for every $\beta$, which is the obstruction behind every "this flux must vanish for topological reasons" argument.

**Targets (Output Amplification)**

The conclusion $C$ is the identity $\int_M d\beta = \int_{\partial M}\beta$.

Combine $C$ with **a form whose exterior derivative is a known density**. If $\beta$ is chosen so that $d\beta$ equals (the volume form times) a divergence, or a curl, then $C$ becomes the [[Thm - The Divergence Theorem|divergence theorem]] or the [[Thm - The Kelvin-Stokes Theorem|Kelvin-Stokes theorem]]. The further result $E$: every classical integral theorem is a corollary, obtained by a single choice of $\beta$. This is non-obvious because the classical theorems look unrelated to the abstract one until you see them as the same identity with $\beta$ specialized.

Combine $C$ with **the hypothesis $\partial M = \emptyset$ and a closed form**. If $d\beta$ is replaced by a closed form $\omega$ on a closed surface, the periods of $\omega$ become well-defined invariants: $\int_M\omega$ depends only on the cohomology class of $\omega$, because changing $\omega$ by an exact form $d\beta$ changes the integral by $\int_M d\beta = 0$. The further result $E$ is that integration descends to a pairing on de Rham cohomology — the analytic engine of de Rham's theorem. The non-obviousness: a statement about *exact* forms (Stokes) becomes a statement about *closed* forms modulo exact ones (cohomology).

Combine $C$ with **a one-parameter family of surfaces sweeping out a region**. If a closed form is integrated over two homologous cycles — two surfaces together bounding a region $M$ — then $C$ gives $\int_{\partial M}\omega = \int_M d\omega = 0$, so the two integrals are equal. The further result $E$ is the homotopy/homology invariance of the integral of a closed form, the principle that lets you replace an awkward integration cycle by a convenient one. This combination is the deformation argument that drives [[Ex - Circulation of a vector field via Stokes' theorem]] and the punctured-plane computation of [[Ex - A closed form that is not exact]].

---

# Why Is It True

The truth of Stokes' theorem is best seen in three stages: why the one-variable case is true, why the local higher-dimensional case is the one-variable case, and why the local case implies the global one.

Start with the Fundamental Theorem of Calculus, $\int_a^b f' = f(b) - f(a)$. This is true because integration and differentiation are inverse processes — the integral accumulates the infinitesimal changes $f'(x)\,dx$, and the accumulated total of all the infinitesimal changes is exactly the net change $f(b) - f(a)$ from one end to the other. The interior of the interval contributes nothing net: every infinitesimal increment is cancelled by being the start of one sub-interval and the end of the previous. Only the two genuine endpoints survive. This "interior cancels, boundary survives" mechanism is the whole idea, and it does not care about dimension.

Now go to a half-space $M = \{x_1 \le 0\}$ in $\mathbb{R}^k$, with a $(k-1)$-form $\beta$. The exterior derivative $d\beta$ is a $k$-form, a single coefficient times $dx_1\wedge\cdots\wedge dx_k$, and integrating it means integrating that coefficient over the half-space. The coefficient is a partial derivative of a coefficient of $\beta$. Integrate first in the one variable whose direction points across the boundary: that single integration is the Fundamental Theorem of Calculus, and it evaluates the coefficient on the boundary hyperplane $\{x_1 = 0\}$. The remaining $(k-1)$ integrations are just integrating $\beta$ over that hyperplane. The directions *parallel* to the boundary contribute nothing — there the form, being compactly supported, integrates to zero by the same "interior cancels" mechanism (an integral of a pure derivative over all of $\mathbb{R}$ of a compactly supported function is zero). So in the half-space, Stokes' theorem is *literally* the Fundamental Theorem of Calculus applied in the one transverse direction, with the other directions inert.

Finally, the global statement. A general compact surface with boundary is, by definition, covered by finitely many coordinate patches, each looking like a piece of half-space. A partition of unity lets you write any form $\beta$ as a finite sum $\sum\beta_i$, each $\beta_i$ supported in one patch. Stokes holds for each $\beta_i$ by the half-space case (after pulling back, using that $d$ commutes with pullback and the integral is chart-independent — this is where orientation enters). Summing, $\int_M d\beta = \sum\int_M d\beta_i = \sum\int_{\partial M}\beta_i = \int_{\partial M}\beta$. The patches that lie in the *interior* of $M$ have $\beta_i$ with no boundary contribution; their $\int_M d\beta_i$ vanishes by the no-boundary half-space case. So once again: interior patches contribute nothing, boundary patches contribute the boundary integral. The mechanism of the Fundamental Theorem of Calculus — interior cancels, boundary survives — is reproduced verbatim, one dimension and one patch at a time.

---

# What Makes This Hard

The genuinely substantive step is the **reduction to the half-space model**: realizing that, because $d$ commutes with pullback and the integral is independent of the orientation-preserving chart, a partition of unity collapses the global statement to a single local computation — and that the local computation is just the one-variable Fundamental Theorem of Calculus integrated in the transverse direction. The most common error is mishandling the **induced orientation on $\partial M$**: getting the magnitude right but the sign wrong because the boundary was given an arbitrary rather than the induced orientation, or because the $(-1)^{j-1}$ from reordering the basic form $dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_k$ was dropped. A second frequent slip is forgetting that **compact support (or compactness of $M$) is essential** — without it the boundary "at infinity" contributes and the clean identity fails.

---

# Rederivation Scaffold

**High-level strategy:** Use a partition of unity to reduce to a form supported in one coordinate patch; pull back to a model half-space; there, integrate in the transverse direction by the Fundamental Theorem of Calculus and observe the tangential directions are inert.

**Subgoal decomposition:**

1. **Reduce to a single patch.** Write $\beta = \sum_i\beta_i$ with each $\beta_i$ compactly supported in one coordinate patch, via a partition of unity subordinate to a cover of $M$.
   - *Hint:* $d$ and $\int$ are both linear, and $d$ commutes with pullback, so it suffices to prove the identity for each $\beta_i$ separately.
   - *Why needed:* It localizes the global statement to a computation in a fixed model domain.

2. **Pull back to the model half-space.** In a patch, $M$ looks like the half-space $\mathbb{R}^k_- = \{x_1 \le 0\}$, with $\partial M$ the hyperplane $\{x_1 = 0\}$ carrying the orientation of $dx_2\wedge\cdots\wedge dx_k$.
   - *Hint:* Chart-independence of $\int$ (orientation-preserving charts) and $d(\varphi^*\beta) = \varphi^*(d\beta)$ make the pullback lossless.
   - *Why needed:* It replaces a curved surface by a flat domain where the integral is an ordinary multiple integral.

3. **Write $\beta$ in the model and compute $d\beta$.** With $\beta = b_j(x)\,dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_k$, get $d\beta = (-1)^{j-1}(\partial b_j/\partial x_j)\,dx_1\wedge\cdots\wedge dx_k$.
   - *Hint:* Only the partial in the *missing* direction $x_j$ survives; the others wedge onto a repeated factor.
   - *Why needed:* It exhibits the integrand of the left side as a single pure partial derivative.

4. **Integrate in the transverse direction; tangential directions are inert.** For $j > 1$, integrating $\partial b_j/\partial x_j$ over all of $\mathbb{R}$ in $x_j$ gives $0$ (compact support), and $\kappa^*\beta = 0$. For $j = 1$, integrating $\partial b_1/\partial x_1$ over $x_1 \le 0$ gives $b_1(0, x')$ by the Fundamental Theorem of Calculus, which is exactly $\int_{\partial M}\beta$.
   - *Hint:* This is the one-variable Fundamental Theorem of Calculus; the case split $j = 1$ versus $j > 1$ is the heart.
   - *Why needed:* It proves the model case, which by steps 1–2 proves the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: A compactly supported pure derivative integrates to zero over all of $\mathbb{R}$
> **Statement:** If $h \in C^1(\mathbb{R}^k)$ has compact support, then $\int_{\mathbb{R}}(\partial h/\partial x_j)\,dx_j = 0$ for each $j$.
>
> **Hint:** Fundamental Theorem of Calculus on a large interval containing the support.
>
> **Why needed:** It kills the tangential ($j > 1$) contributions in the half-space model — the "interior cancels" half of Stokes.
>
> > [!note]- Full proof
> > Fix all variables except $x_j$. Choose $C$ so large that the support of $h$ lies in $\{|x_j| < C\}$. Then $\int_{\mathbb{R}}\partial_j h\,dx_j = \int_{-C}^{C}\partial_j h\,dx_j = h(\dots, C, \dots) - h(\dots, -C, \dots) = 0 - 0 = 0$ by the Fundamental Theorem of Calculus and compact support.

> [!note]- Lemma 2: Stokes in the half-space model
> **Statement:** Let $M = \{x \in \mathbb{R}^k : x_1 \le 0\}$ and let $\beta = b_j(x)\,dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_k$ be a compactly supported $C^1$ $(k-1)$-form. Then $\int_M d\beta = \int_{\partial M}\beta$.
>
> **Hint:** Compute $d\beta$; split into the cases $j = 1$ and $j > 1$; integrate the transverse variable by the Fundamental Theorem of Calculus.
>
> **Why needed:** It is the entire local content of the theorem; the global case is this lemma plus a partition of unity.
>
> > [!note]- Full proof
> > The exterior derivative is $d\beta = (-1)^{j-1}(\partial b_j/\partial x_j)\,dx_1\wedge\cdots\wedge dx_k$, since every partial except $\partial_j$ wedges $dx_\ell$ onto a basic form already containing $dx_\ell$.
> >
> > *Case $j > 1$.* The variable $x_1$ is among the kept differentials, so integrating $d\beta$ over $M$ means integrating $\partial_j b_j$ — and $x_j$ ranges over all of $\mathbb{R}$ (it is a tangential variable). By Lemma 1, $\int_{\mathbb{R}}\partial_j b_j\,dx_j = 0$, so $\int_M d\beta = 0$. On the boundary side, $\kappa^*\beta$ contains the factor $\kappa^*dx_1 = 0$ (the boundary is $\{x_1 = 0\}$, so $x_1$ is constant there), hence $\int_{\partial M}\beta = 0$. Both sides are zero.
> >
> > *Case $j = 1$.* Then $d\beta = (\partial b_1/\partial x_1)\,dx_1\wedge\cdots\wedge dx_k$, and
> > $$\int_M d\beta = \int_{\mathbb{R}^{k-1}}\Big(\int_{-\infty}^{0}\frac{\partial b_1}{\partial x_1}\,dx_1\Big)\,dx_2\cdots dx_k = \int_{\mathbb{R}^{k-1}} b_1(0, x')\,dx',$$
> > the inner integral evaluated by the Fundamental Theorem of Calculus (with $b_1 \to 0$ as $x_1 \to -\infty$ by compact support). The right side: on $\partial M = \{x_1 = 0\}$ with orientation $dx_2\wedge\cdots\wedge dx_k$, $\int_{\partial M}\beta = \int_{\mathbb{R}^{k-1}} b_1(0, x')\,dx'$. The two sides agree. $\square$

> [!note]- Lemma 3: Reduction by a partition of unity
> **Statement:** If Stokes' identity holds for every form supported in a single coordinate patch, it holds for every compactly supported $\beta$ on $M$.
>
> **Hint:** Write $\beta = \sum_i\rho_i\beta$ for a partition of unity $\{\rho_i\}$ subordinate to a patch cover; use linearity of $d$ and $\int$.
>
> **Why needed:** It assembles the local Lemma 2 into the global theorem.
>
> > [!note]- Full proof
> > $M$ is compact, so it has a finite cover by coordinate patches $U_i$. Take a smooth partition of unity $\{\rho_i\}$ subordinate to this cover: $\sum_i\rho_i = 1$ on $M$, and $\rho_i$ supported in $U_i$. Then $\beta = \sum_i\rho_i\beta$, with each $\rho_i\beta$ supported in $U_i$. Since $d$ is linear, $d\beta = \sum_i d(\rho_i\beta)$, and since $\int$ is linear,
> > $$\int_M d\beta = \sum_i\int_M d(\rho_i\beta) = \sum_i\int_{\partial M}\rho_i\beta = \int_{\partial M}\sum_i\rho_i\beta = \int_{\partial M}\beta,$$
> > the middle equality being the single-patch case (Lemma 2, transported by an orientation-preserving chart, using that $d$ commutes with pullback and the integral is chart-independent). $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a compact oriented $C^2$ $k$-surface with boundary $\partial M$ (with the induced orientation), and let $\beta$ be a compactly supported $C^1$ $(k-1)$-form on $M$.
>
> **Step 1 (localization).** By compactness, cover $M$ by finitely many coordinate patches; take a subordinate smooth partition of unity $\{\rho_i\}$, so $\sum_i\rho_i = 1$ on $M$ and each $\rho_i\beta$ is supported in one patch. By linearity of $d$ and of integration, it suffices (Lemma 3) to prove $\int_M d(\rho_i\beta) = \int_{\partial M}\rho_i\beta$ for each $i$.
>
> **Step 2 (pullback to the model).** Fix $i$ and an orientation-preserving chart $\varphi_i : O_i \to U_i$, where $O_i$ is an open subset of the half-space $\mathbb{R}^k_- = \{x_1 \le 0\}$. Since $d$ commutes with pullback ($\varphi_i^*d = d\varphi_i^*$) and the integral of a form is independent of the orientation-preserving chart,
> $$\int_M d(\rho_i\beta) = \int_{O_i}\varphi_i^*\,d(\rho_i\beta) = \int_{O_i} d\big(\varphi_i^*(\rho_i\beta)\big), \qquad \int_{\partial M}\rho_i\beta = \int_{\partial O_i}\varphi_i^*(\rho_i\beta).$$
> Write $\gamma = \varphi_i^*(\rho_i\beta)$, a compactly supported $C^1$ $(k-1)$-form on the half-space. It remains to show $\int_{\mathbb{R}^k_-} d\gamma = \int_{\partial\mathbb{R}^k_-}\gamma$.
>
> **Step 3 (the half-space computation).** It suffices to treat a single basic term $\gamma = b_j(x)\,dx_1\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_k$. Its exterior derivative is
> $$d\gamma = (-1)^{j-1}\frac{\partial b_j}{\partial x_j}\,dx_1\wedge\cdots\wedge dx_k,$$
> only the $\partial_j$ term surviving (all others repeat a differential).
>
> *Case $j > 1$.* By Fubini and Lemma 1, $\int_{\mathbb{R}^k_-}\partial_j b_j\,dx = 0$ since $x_j$ ranges over all of $\mathbb{R}$ and $b_j$ has compact support. And $\kappa^*\gamma = 0$ because $\kappa^*dx_1 = 0$ on $\partial\mathbb{R}^k_- = \{x_1 = 0\}$. Both sides vanish.
>
> *Case $j = 1$.* Then $d\gamma = (\partial b_1/\partial x_1)\,dx_1\wedge\cdots\wedge dx_k$, and by Fubini and the Fundamental Theorem of Calculus,
> $$\int_{\mathbb{R}^k_-} d\gamma = \int_{\mathbb{R}^{k-1}}\Big(\int_{-\infty}^{0}\partial_1 b_1\,dx_1\Big)dx' = \int_{\mathbb{R}^{k-1}} b_1(0, x')\,dx' = \int_{\partial\mathbb{R}^k_-}\gamma,$$
> the last equality holding because $\partial\mathbb{R}^k_-$ carries the orientation of $dx_2\wedge\cdots\wedge dx_k$.
>
> **Conclusion.** The half-space identity holds for every basic term, hence for $\gamma$, hence (Step 2) for each $\rho_i\beta$, hence (Step 1) $\int_M d\beta = \int_{\partial M}\beta$. $\blacksquare$
>
> *Remark.* The hypothesis $C^2$ on $M$ ensures that a $C^1$ form pulled back through a $C^2$ chart is still $C^1$ (a pullback through a $C^\ell$ map drops one degree of regularity). The result extends to $C^1$ surfaces with corners under the weaker hypothesis that both $\beta$ and $d\beta$ are continuous; the corner case is handled by the same computation on $\{x_j \le 0,\ 1 \le j \le k-\nu\}$.

---

# Cross-Field Exercise Suggestions

**The winding number as a Stokes integral.** On the punctured plane, the integral of the angular form around a closed curve counts how many times the curve winds around the origin. Stokes' theorem, applied to the region between the curve and a reference circle, shows the winding number is a deformation invariant. The application is out-of-distribution because a *topological* counting invariant (an integer) is being produced by an *analytic* identity about $d$ and $\partial$ — the integer-valuedness comes from the curve having no boundary.

**Conservation of charge in electromagnetism.** The continuity equation $\partial_t\rho + \operatorname{div} J = 0$ expresses local conservation of electric charge. Integrating it over a fixed spatial region and applying the divergence theorem (the $k = 3$ case of Stokes) converts the divergence term into a flux through the boundary, yielding "the rate of change of charge inside equals the current flowing out". The application is nonobvious because a *differential* conservation law becomes a *global* balance law purely through Stokes.

**The Gauss-Bonnet theorem.** For a compact surface, the integral of the Gaussian curvature equals $2\pi$ times the Euler characteristic. The local Gauss-Bonnet formula expresses curvature as $d$ of a connection form, and the global theorem is then the general Stokes theorem summed over a triangulation, with the boundary terms reassembling into the Euler characteristic. The application is striking because Stokes converts a *geometric* integral (curvature) into a *topological* integer.

**The Cauchy integral theorem.** A holomorphic function $f$ on a domain in $\mathbb{C}$ gives a closed $1$-form $f(z)\,dz$, and the Cauchy integral theorem $\oint_\gamma f\,dz = 0$ for a contractible loop is exactly Stokes' theorem ($\int_{\partial M} f\,dz = \int_M d(f\,dz) = 0$, since $d(f\,dz) = 0$ by the Cauchy-Riemann equations). The application is nonobvious because the foundational theorem of complex analysis turns out to be a special case of the general Stokes formula for a closed $1$-form.

---

# Bridges

- **[[Thm - Green's Theorem|Green's Theorem]], [[Thm - The Divergence Theorem|the Divergence Theorem]], and [[Thm - The Kelvin-Stokes Theorem|the Kelvin-Stokes Theorem]]** — these are not separate theorems but the cases $k = 2$ (in $\mathbb{R}^2$), $k = n$, and $k = 2$ (in $\mathbb{R}^3$) of this one identity, obtained by choosing $\beta$ to be a $1$-form, an $(n-1)$-form, or a $1$-form respectively. The general Stokes theorem is the statement; the three classical theorems are its readings.

- **The Fundamental Theorem of Calculus** — the case $k = 1$. A $0$-form is a function $f$, $d f = f'\,dx$, the surface is an interval $[a,b]$, and $\partial[a,b] = \{b\} - \{a\}$, so Stokes reads $\int_a^b f' = f(b) - f(a)$. Every higher case is this case, integrated in one transverse direction inside a partition of unity.

- **[[Thm - The Poincaré Lemma|The Poincaré Lemma]]** — the converse direction. Stokes shows exact forms integrate to zero over closed surfaces; the Poincaré lemma asks when a closed form is exact, and the gap between the two is de Rham cohomology. Together they make integration a pairing between cohomology and homology.

- **The boundary operator $\partial$ and the homology of chains** — Stokes says $\langle d\beta, M\rangle = \langle\beta, \partial M\rangle$, exhibiting $d$ and $\partial$ as adjoint. The identity $\partial\circ\partial = 0$ (the boundary of a boundary is empty) is the geometric dual of $d\circ d = 0$, and the two complexes — forms with $d$, chains with $\partial$ — are paired by integration.

---

# Unlocked by This

> [!tip] de Rham Cohomology *(from Algebraic Topology)*
> Because Stokes shows $\int_M$ vanishes on exact forms, integration descends to a pairing between de Rham cohomology $H^k_{\mathrm{dR}}$ and homology $H_k$. **de Rham's theorem** states this pairing is perfect — the analytic cohomology of forms equals the topological cohomology.

> [!tip] Maxwell's Equations and Conservation Laws *(from Electromagnetism)*
> The divergence and Kelvin-Stokes cases of this theorem are exactly what convert the differential Maxwell equations $dF = 0$, $d\!\star\!F = J$ into the integral laws of flux and circulation. Charge conservation $dJ = 0$ integrated over a region becomes a global balance law via Stokes.

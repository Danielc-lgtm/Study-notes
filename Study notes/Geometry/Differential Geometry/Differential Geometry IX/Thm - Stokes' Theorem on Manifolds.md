---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Manifold with Boundary and Induced Orientation"
  - "Def - Integral of a Compactly Supported Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Partition of Unity on a Manifold"
  - "Thm - Existence of Smooth Partitions of Unity"
  - "Def - Pullback of a Differential Form on a Manifold"
tags: [geometry, differential-geometry, stokes, integration]
---

# Notation

$M$ is an oriented smooth $n$-manifold with boundary $\partial M$, the boundary carrying the [[Def - Manifold with Boundary and Induced Orientation|induced (Stokes) orientation]]. $\omega \in \Omega^{n-1}_c(M)$ is a compactly supported smooth $(n-1)$-form. $d : \Omega^{n-1}(M) \to \Omega^n(M)$ is the [[Def - Exterior Derivative on a Manifold|exterior derivative]] on $M$. The boundary inclusion is $\iota : \partial M \hookrightarrow M$; the integral over the boundary $\int_{\partial M}\omega$ means $\int_{\partial M}\iota^*\omega$. The half-space model is $\mathbb{H}^n = \{x \in \mathbb{R}^n : x^n \geq 0\}$ with $\partial\mathbb{H}^n = \{x^n = 0\}$. The full notation registry is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

---

# Statement

> **Stokes's Theorem (Manifold Version).** Let $M$ be an oriented smooth $n$-manifold with boundary, and let $\omega \in \Omega^{n-1}_c(M)$ be a compactly supported smooth $(n-1)$-form. Then
> $$\int_M d\omega = \int_{\partial M}\omega,$$
> where $\partial M$ carries the orientation induced from $M$ (outward-normal-first convention).
>
> When $\partial M = \emptyset$, the right-hand side is interpreted as $0$, so $\int_M d\omega = 0$ for every compactly supported $(n-1)$-form $\omega$ on a boundaryless oriented manifold.

> **Corollary (Closed-manifold integration vanishes on exact forms).** Let $M$ be a compact oriented smooth $n$-manifold without boundary. Then for every $\omega \in \Omega^{n-1}(M)$, $\int_M d\omega = 0$. Equivalently, the linear functional $\int_M : \Omega^n(M) \to \mathbb{R}$ kills exact forms.

> **Corollary (Recovery of classical theorems).** The Fundamental Theorem of Calculus ($n = 1$), [[Thm - Green's Theorem|Green's theorem]] ($n = 2$ in $\mathbb{R}^2$), [[Thm - The Divergence Theorem|the divergence theorem]] ($n = 3$ in $\mathbb{R}^3$), and [[Thm - The Kelvin-Stokes Theorem|Kelvin–Stokes]] ($n = 2$ surface in $\mathbb{R}^3$) are all special cases of this single statement, obtained by particular choices of $\omega$ and ambient dimension.

The theorem also holds on manifolds with corners (locally modeled on $\{x_1 \geq 0, \ldots, x_k \geq 0\} \times \mathbb{R}^{n-k}$), with the boundary integral summed over the codimension-$1$ faces, each carrying its induced orientation. The proof is the same with a slightly more elaborate book-keeping.

---

# Motivation

The Fundamental Theorem of Calculus, $\int_a^b f' = f(b) - f(a)$, has a particular *shape*: it equates the integral of a derivative over a region with the integral of the original function over the boundary of that region. The right side is, viewed correctly, an integral of $f$ over the two-point set $\{a, b\}$, with $b$ counted positively and $a$ negatively — the boundary of $[a, b]$ with its induced orientation. So the theorem already exhibits the abstract structure
$$\int_{\text{region}}(\text{derivative}) = \int_{\text{boundary}}(\text{original}).$$
The question that demands an answer is: *is this shape an accident of one dimension, or a universal law?* Before differential forms, the answer was "fragmented yes": Green's theorem in the plane, the divergence theorem in three dimensions, and the classical Stokes theorem on surfaces in space all exhibited the same shape, but each was proved separately and there was no manifest reason the three should be one theorem.

Differential forms supply the missing structure. The "thing being integrated" is a top-degree form; the "derivative" is the exterior derivative $d$; the "boundary" is the manifold boundary $\partial M$. Once these are in place, the four classical statements *collapse into one sentence*: $\int_M d\omega = \int_{\partial M}\omega$. This is the manifold-version Stokes theorem. The Euclidean version was established in [[Thm - The General Stokes Theorem]]; the manifold version generalizes it by removing the embedding into an ambient $\mathbb{R}^N$ and stating the result intrinsically — in terms of charts, oriented atlases, partitions of unity, and the exterior derivative.

What makes the manifold version *expectable*? The deep reason is that the exterior derivative $d$ and the boundary operator $\partial$ are formal adjoints with respect to integration: increasing the degree of a form by one (via $d$) and decreasing the dimension of a domain by one (via $\partial$) are dual moves, and integration is the pairing exhibiting the duality. Stokes's theorem says this adjunction is *strict*: moving a derivative onto the form is exactly the same as moving the integration onto the boundary, with no extra sign factor. This is a structural inevitability — once you set up the machinery, the theorem is forced.

Beyond the unification of classical theorems, Stokes is the **proof engine** behind de Rham cohomology (closed forms modulo exact forms; the integral pairs with cycles), Poincaré duality (the wedge-and-integrate pairing is non-degenerate on a closed oriented manifold), the integral form of Maxwell's equations (Gauss, Faraday, Ampère–Maxwell), and the Gauss–Bonnet theorem (curvature integral = topological invariant). The reason all these results work is that they are all *applications of Stokes*, and the reason Stokes works is that on a manifold-with-boundary the local picture in any chart is a half-space, where the theorem reduces to the Fundamental Theorem of Calculus in one direction.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis Stokes needs is: *an oriented smooth manifold with boundary, plus a compactly supported $(n-1)$-form.* The skill is recognizing this hypothesis in disguise.

The first disguised source is **a region defined as the sublevel set of a regular function**, $M = \{p : f(p) \leq c\}$ with $df \neq 0$ on $\{f = c\}$. The bridge: by the regular value theorem on manifolds ([[Thm - Regular Value Theorem on Manifolds]]), $\{f = c\}$ is then a smooth hypersurface, so $M$ is a manifold-with-boundary in the ambient smooth manifold, and the sign of $f$ supplies the outward normal direction (the gradient of $f$, in a metric). The non-obvious part is that an *inequality* — a single scalar regularity condition — automatically delivers the smooth, oriented, boundary structure Stokes needs. *Example problem:* the unit ball $\{|x|^2 \leq 1\}$ in $\mathbb{R}^n$ is a Stokes domain because $|x|^2$ has regular boundary value $1$; Stokes applied here recovers the divergence theorem on the ball.

The second disguised source is **a finite chain of cornered pieces glued along faces** — a region cut into finitely many smooth blocks, with the boundary a union of faces that pair up cleanly (each internal face shared by two blocks). The bridge: Stokes holds on each piece (manifolds with corners admit Stokes), and summing the identities over all pieces, the boundary integrals over internal faces cancel because each is traversed twice with opposite induced orientation. The non-obvious part is that domains too irregular to be globally smooth still satisfy Stokes via *additivity*. *Example problem:* verifying Stokes on a cube (which has eight corners) by treating it as a union of cornered pieces, or — more elegantly — directly via the manifold-with-corners statement.

The third disguised source is **a closed form integrated over a closed surface that bounds a region**. The bridge: if $\Sigma = \partial M$ for a compact orientable $M$ with boundary, and $\omega$ is closed on a neighborhood of $M$ (so $d\omega = 0$), then Stokes gives $\int_\Sigma\omega = \int_M d\omega = 0$. The non-obviousness: vanishing of a surface integral is forced not by any property of the integrand on $\Sigma$ itself, but by the fact that the integrand *extends to be closed* on a region bounded by $\Sigma$. This is the principle behind much of contour integration in complex analysis. *Example problem:* the integral of a closed form on a sphere is zero whenever the form extends to a closed form on the ball — which is automatic, by [[Thm - The Poincaré Lemma|Poincaré]] applied to the contractible ball.

A fourth disguised source is **a one-parameter family of cycles** sweeping out a region. The bridge: if $\Sigma_0$ and $\Sigma_1$ are two closed $(n-1)$-cycles together bounding a compact region $M$ (so $\partial M = \Sigma_1 - \Sigma_0$), and $\omega$ is closed, then $\int_{\Sigma_1}\omega - \int_{\Sigma_0}\omega = \int_M d\omega = 0$, so the two integrals agree. The non-obviousness: integrals of closed forms are *homotopy invariants* — they depend only on the homology class of the cycle, not on its specific shape. This is the foundation of the period pairing in de Rham cohomology and the Cauchy integral theorem in complex analysis.

A fifth disguised source is **a manifold whose boundary is empty**. Many useful applications of Stokes (de Rham cohomology, Poincaré duality, the Gauss–Bonnet theorem) involve closed manifolds with $\partial M = \emptyset$; in this case Stokes reads $\int_M d\omega = 0$, which says the integration functional $\Omega^n(M) \to \mathbb{R}$ kills exact forms. The bridge is the *absence* of boundary; the recognition is that closedness of $M$ (no edges) lets one ignore the boundary contribution.

**Targets (Output Amplification)**

The conclusion Stokes delivers is the identity $\int_M d\omega = \int_{\partial M}\omega$, a duality between $d$ and $\partial$ via integration.

Combine $C$ with **a form whose exterior derivative is a known density**. If $\omega$ is chosen so $d\omega$ equals the divergence times the volume form, Stokes gives the divergence theorem; if $d\omega$ equals the curl times the area form, Stokes gives Kelvin–Stokes; etc. The further result $E$: every classical theorem of vector calculus is a corollary of Stokes, obtained by a single choice of $\omega$. The non-obviousness: the four classical theorems look unrelated until they are recognized as instances of one identity with $\omega$ specialized.

Combine $C$ with **closedness of $M$ and exactness of the integrand**. If $M$ is closed (no boundary) and $\omega = d\eta$, then $\int_M\omega = \int_M d\eta = \int_{\partial M}\eta = 0$. The further result $E$ is that integration descends to a pairing on de Rham cohomology: $\int_M : H^n_{dR}(M) \to \mathbb{R}$ is well-defined (changing $\omega$ by an exact form does not change the integral). The non-obviousness: a statement about *exact* forms (Stokes) becomes a statement about *closed* forms modulo exact (cohomology), the foundational identification of de Rham theory.

Combine $C$ with **a homotopy or one-parameter family**. If $\omega_t$ is a closed form depending smoothly on $t$, then $\partial_t\omega_t = d\eta_t$ for some $\eta_t$ (under mild conditions). Stokes then gives $\partial_t\int_M\omega_t = \int_M d\eta_t = 0$ on a closed $M$, so the integral is a homotopy invariant. The further result $E$ is the **homotopy invariance of de Rham cohomology**, the cornerstone of cohomological computation. The non-obviousness: a *time derivative* of the integrand under a deformation cancels by Stokes, fixing the value of the integral.

Combine $C$ with **the wedge product of two closed forms**. On a compact oriented closed $M^n$, integrating $\omega\wedge\eta$ for $\omega \in \Omega^k$ and $\eta \in \Omega^{n-k}$ (both closed) gives a bilinear pairing $H^k(M) \times H^{n-k}(M) \to \mathbb{R}$ that is well-defined by Stokes (changing either factor by an exact form does not change the integral, by Stokes applied to the resulting exact form). The further result $E$ is **Poincaré duality**: this pairing is non-degenerate. The non-obviousness: a wedge-and-integrate construction is exactly the bilinear duality of cohomology in complementary degrees, and Stokes is what makes it well-defined.

Combine $C$ with **the Bianchi identity $d^2 = 0$**. Applying Stokes twice — to $\omega$ and then to $d\omega$ — gives $\int_M d^2\omega = 0$, which is the *trivial* identity. But the more useful version: in physics, $d^2{\star}F = 0$ for the Faraday form $F$ implies $d J = 0$ (conservation of charge), and integration via Stokes converts this into $\oint_{\partial M}J = 0$ — the *integrated* charge conservation law. The further result $E$ is the global conservation laws of electromagnetism, derived from the differential conservation laws via Stokes. See the Maxwell exercise.

---

# Why Is It True

The truth of Stokes's theorem on manifolds is best seen in *three stages*: the one-variable Fundamental Theorem of Calculus, the half-space model in $n$ dimensions, and the partition-of-unity gluing.

**Stage 1: the FTC is true because $\int$ and $d$ are inverse operations in one dimension.** The Fundamental Theorem of Calculus, $\int_a^b f'(x)\,dx = f(b) - f(a)$, is true because integration accumulates the infinitesimal changes $f'(x)\,dx$ and the accumulated total is exactly the net change from one endpoint to the other. The interior of $[a, b]$ contributes nothing net: every infinitesimal increment is cancelled, being the start of one sub-interval and the end of the previous. Only the genuine endpoints survive. This is the "interior cancels, boundary survives" mechanism, and it is the entire content of Stokes — it is just stated in dimension one.

**Stage 2: in dimension $n$, the half-space reduces to dimension one in the transverse direction.** Consider $M = \mathbb{H}^n = \{x^n \geq 0\}$ with a compactly supported $(n-1)$-form $\omega$. By multilinearity it suffices to handle the basis terms $\omega = b(x)\,dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n$ for each $j$ (the "hat" means $dx^j$ is omitted). Compute $d\omega$ in coordinates: only the $\partial_j$ derivative survives (the others wedge $dx^\ell$ onto a basic form already containing $dx^\ell$, giving zero), so
$$d\omega = (-1)^{j-1}\partial_j b\,dx^1\wedge\cdots\wedge dx^n.$$
Integrate over $\mathbb{H}^n$ and split by cases.

- **Case $j \neq n$** (i.e. the omitted differential is *not* $dx^n$): the variable $x^j$ ranges over *all* of $\mathbb{R}$, not just $\mathbb{H}^n$. By Fubini, $\int_{\mathbb{H}^n}\partial_jb = \int_{\text{other vars}}\big[\int_{-\infty}^{\infty}\partial_jb\,dx^j\big]$, and the inner integral is zero by FTC (compactly supported $b$ has $b \to 0$ at $\pm\infty$). On the boundary $\partial\mathbb{H}^n = \{x^n = 0\}$, the pulled-back form $\iota^*\omega$ contains $\iota^*dx^n = 0$ (since $x^n = 0$ on the boundary), so $\iota^*\omega = 0$. Both sides are zero — they agree.
- **Case $j = n$**: the missing differential *is* $dx^n$, so $\omega = b\,dx^1\wedge\cdots\wedge dx^{n-1}$ and $d\omega = (-1)^{n-1}\partial_n b\,dx^1\wedge\cdots\wedge dx^n$. Integrate $x^n$ from $0$ to $\infty$: by FTC, $\int_0^\infty\partial_n b\,dx^n = [b]_0^\infty = -b(x^1, \ldots, x^{n-1}, 0)$ (the value at $\infty$ vanishes by compact support, the value at $0$ enters with a minus sign). The result, after the $(-1)^{n-1}$, is $(-1)^n\int_{\mathbb{R}^{n-1}}b(x', 0)\,dx^1\cdots dx^{n-1}$. The boundary side: $\iota^*\omega = b(x', 0)\,dx^1\wedge\cdots\wedge dx^{n-1}$, integrated over $\partial\mathbb{H}^n$ with its *induced* orientation, which is $(-1)^n$ times the standard. The two factors of $(-1)^n$ match, and the two sides are equal.

So on the half-space, Stokes is *literally* the Fundamental Theorem of Calculus applied in the one transverse direction $x^n$, with the other directions inert (cancelling via compact support and FTC).

**Stage 3: partition of unity glues the half-space cases into the global statement.** A general compactly supported $\omega \in \Omega^{n-1}_c(M)$ has support in a compact set; cover this support by finitely many oriented charts $\{(U_i, \varphi_i)\}$, each isomorphic to either $\mathbb{R}^n$ (interior chart) or $\mathbb{H}^n$ (boundary chart). Take a smooth partition of unity $\{\psi_i\}$ subordinate to this cover: $\sum_i\psi_i = 1$ on $\mathrm{supp}\,\omega$. Then
$$\omega = \sum_i\psi_i\omega, \qquad d\omega = \sum_i d(\psi_i\omega),$$
each $\psi_i\omega$ supported in a single chart. By Stage 2 applied chart-by-chart (with $d$ commuting with pullback and the integral being chart-independent for orientation-preserving charts),
$$\int_M d(\psi_i\omega) = \int_{\partial M}\psi_i\omega \qquad\text{for each }i.$$
Sum: $\int_M d\omega = \sum_i\int_M d(\psi_i\omega) = \sum_i\int_{\partial M}\psi_i\omega = \int_{\partial M}\omega$.

The mechanism in one sentence: **the boundary of a chart pairs with $d$ on its interior via $\int_{[0,1]}df = f(1) - f(0)$ in the one transverse direction; the other directions cancel by compact support and FTC; partition of unity adds the chart contributions consistently.**

---

# What Makes This Hard

The genuinely substantive step is **the reduction to the half-space model**: realizing that, because $d$ commutes with pullback and the integral is independent of the orientation-preserving chart, a partition of unity collapses the global statement to a single local computation, and that the local computation is the one-variable FTC integrated in the transverse direction. The most common error is mishandling the **induced orientation on $\partial M$** — getting the magnitude of the boundary integral right but the sign wrong, because the boundary was given an arbitrary rather than the induced orientation, or because the $(-1)^{j-1}$ from reordering the basic form $dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n$ was dropped. A second frequent slip is forgetting **compact support is essential** — without it, boundary contributions "at infinity" survive and the clean identity breaks.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use a partition of unity to reduce to a form supported in a single chart; pull back via an orientation-preserving chart to a model half-space $\mathbb{H}^n$; in $\mathbb{H}^n$, expand $\omega$ in coordinates, compute $d\omega$, integrate by the FTC in the transverse direction $x^n$; recognize the result as the integral of $\iota^*\omega$ over the boundary with its induced orientation.

**Subgoal decomposition:**

1. **Reduce via partition of unity.** Write $\omega = \sum_i\psi_i\omega$ for a partition of unity $\{\psi_i\}$ subordinate to a finite cover of $\mathrm{supp}\,\omega$ by oriented charts. By linearity of $d$ and $\int$, it suffices to prove Stokes for each $\psi_i\omega$ separately.
   - *Hint:* The set of $\omega$ for which Stokes holds is closed under (locally finite) sums; partition of unity exhibits each such $\omega$ as a sum of single-chart-supported pieces.
   - *Why needed:* It localizes a global identity to a chart computation.

2. **Pull back to the half-space.** In an orientation-preserving boundary chart $(U, \varphi)$ with $\varphi(U) \subseteq \mathbb{H}^n$, $\int_M d(\psi_i\omega) = \int_{\mathbb{H}^n}(\varphi^{-1})^*d(\psi_i\omega) = \int_{\mathbb{H}^n}d((\varphi^{-1})^*\psi_i\omega)$ (using $\varphi^* d = d\varphi^*$).
   - *Hint:* Pullback commutes with $d$ and (for orientation-preserving charts) leaves the integral invariant.
   - *Why needed:* It replaces the abstract manifold with the concrete half-space, where coordinates are available.

3. **Compute $d\omega$ in half-space coordinates.** With $\omega = \sum_j b_j(x)\,dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n$, only the term $\partial_j$ survives in $d\omega$, giving $d\omega = \sum_j(-1)^{j-1}\partial_j b_j\,dx^1\wedge\cdots\wedge dx^n$.
   - *Hint:* For each basic form $dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n$, the only partial derivative whose wedge does not repeat a differential is $\partial_j$.
   - *Why needed:* It exhibits $d\omega$ as a sum of pure-partial-derivative top-forms.

4. **Integrate by FTC, with case split.** Integrate each term over $\mathbb{H}^n$. For $j \neq n$, the variable $x^j$ ranges over all $\mathbb{R}$ and FTC gives zero. For $j = n$, integrating $\partial_n b_n$ from $0$ to $\infty$ in $x^n$ gives $-b_n(x', 0)$, and after the $(-1)^{n-1}$ sign and the induced-orientation sign $(-1)^n$ on $\partial\mathbb{H}^n$, the result is $\int_{\mathbb{R}^{n-1}}b_n(x', 0)\,dx' = \int_{\partial\mathbb{H}^n}\omega$.
   - *Hint:* Tangential directions are inert by compact support; only the transverse direction $x^n$ matters, and there it is FTC.
   - *Why needed:* This is the heart of the proof — the bridge from $d\omega$ to a boundary integral.

5. **Sum back.** $\int_M d\omega = \sum_i\int_M d(\psi_i\omega) = \sum_i\int_{\partial M}\psi_i\omega = \int_{\partial M}\omega$ by Stages 1–4.

---

# Lemma Decomposition

The proof breaks into three independently-practiceable lemmas.

> [!note]- Lemma 1: Compactly supported pure derivative integrates to zero over all of $\mathbb{R}$
> **Statement:** If $h \in C^1(\mathbb{R}^k)$ has compact support, then for each $j \in \{1, \ldots, k\}$,
> $$\int_{\mathbb{R}^k}\partial_j h(x)\,dx = 0.$$
>
> **Hint:** Use Fubini to integrate $x^j$ first; on a sufficiently large interval $[-C, C]$ containing $\mathrm{supp}\,h$ in the $x^j$ direction, FTC gives $\int_{-C}^C\partial_j h\,dx^j = h(\ldots, C, \ldots) - h(\ldots, -C, \ldots) = 0 - 0$ by compact support.
>
> **Why needed:** It kills the tangential ($j \neq n$) contributions in the half-space model — the "interior cancels" half of Stokes.
>
> > [!note]- Full proof
> > Fix all variables except $x^j$, and choose $C > 0$ so large that $\mathrm{supp}\,h \cap \{|x^j| > C\} = \emptyset$ at the fixed values of the other variables. By the Fundamental Theorem of Calculus on $[-C, C]$,
> > $$\int_{-C}^C\partial_j h(\ldots, x^j, \ldots)\,dx^j = h(\ldots, C, \ldots) - h(\ldots, -C, \ldots) = 0 - 0 = 0,$$
> > because both boundary values lie outside $\mathrm{supp}\,h$. By Fubini,
> > $$\int_{\mathbb{R}^k}\partial_j h\,dx = \int_{\text{other vars}}\Big(\int_{\mathbb{R}}\partial_j h\,dx^j\Big)d(\text{other vars}) = 0. \qquad\square$$

> [!note]- Lemma 2: Stokes on the half-space (the local model)
> **Statement:** Let $M = \mathbb{H}^n = \{x^n \geq 0\}$ with the standard orientation, and let $\omega = b(x)\,dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n$ be a compactly supported $C^1$ $(n-1)$-form for some $j \in \{1, \ldots, n\}$. Then $\int_{\mathbb{H}^n}d\omega = \int_{\partial\mathbb{H}^n}\omega$, where $\partial\mathbb{H}^n$ carries the induced orientation.
>
> **Hint:** Compute $d\omega = (-1)^{j-1}\partial_j b\,dx^1\wedge\cdots\wedge dx^n$. Split into $j \neq n$ (tangential — both sides zero) and $j = n$ (transverse — both sides equal a boundary integral). Use Lemma 1 for the tangential case and FTC in $x^n$ for the transverse case.
>
> **Why needed:** This is the entire local content of the theorem; the global case is this lemma plus a partition of unity. Every coordinate chart of $M$ looks like a piece of $\mathbb{H}^n$ (or $\mathbb{R}^n$ for interior charts), so once Stokes is proved here, it is proved everywhere.
>
> > [!note]- Full proof
> > The exterior derivative is
> > $$d\omega = \sum_i\partial_i b\,dx^i\wedge dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n.$$
> > For $i \neq j$, the wedge $dx^i\wedge dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n$ contains $dx^i$ twice and is zero. For $i = j$, reordering $dx^j$ into the $j$-th slot uses $j - 1$ transpositions, contributing $(-1)^{j-1}$. Hence $d\omega = (-1)^{j-1}\partial_jb\,dx^1\wedge\cdots\wedge dx^n$.
> >
> > **Case $j \neq n$.** Integrating $d\omega$ over $\mathbb{H}^n$ means integrating $(-1)^{j-1}\partial_jb$ in all $n$ variables, with $x^n$ on $[0, \infty)$ and the others on $\mathbb{R}$. By Fubini, the $x^j$-integral over $\mathbb{R}$ is zero (Lemma 1 applied to fixed other variables); hence $\int_{\mathbb{H}^n}d\omega = 0$. On the boundary side, $\iota^*\omega = b(x', 0)\,dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n$ contains $\iota^*dx^n = 0$ (since $x^n = 0$ on the boundary), unless $j = n$. So for $j \neq n$, $\iota^*\omega = 0$ and $\int_{\partial\mathbb{H}^n}\omega = 0$. Both sides zero.
> >
> > **Case $j = n$.** Now $\omega = b\,dx^1\wedge\cdots\wedge dx^{n-1}$, and $d\omega = (-1)^{n-1}\partial_n b\,dx^1\wedge\cdots\wedge dx^n$. By Fubini and FTC,
> > $$\int_{\mathbb{H}^n}d\omega = (-1)^{n-1}\int_{\mathbb{R}^{n-1}}\Big(\int_0^\infty\partial_nb\,dx^n\Big)dx^1\cdots dx^{n-1} = (-1)^{n-1}\int_{\mathbb{R}^{n-1}}\big[b\big]_0^\infty\,dx',$$
> > and $[b]_0^\infty = 0 - b(x', 0) = -b(x', 0)$ by compact support. So
> > $$\int_{\mathbb{H}^n}d\omega = (-1)^n\int_{\mathbb{R}^{n-1}}b(x', 0)\,dx^1\cdots dx^{n-1}.$$
> > On the boundary side, $\iota^*\omega = b(x', 0)\,dx^1\wedge\cdots\wedge dx^{n-1}$; integrated over $\partial\mathbb{H}^n$ with the *induced* orientation, which is $(-1)^n$ times the standard orientation of $\mathbb{R}^{n-1}$ (as established in [[Def - Manifold with Boundary and Induced Orientation]]), this gives
> > $$\int_{\partial\mathbb{H}^n}\omega = (-1)^n\int_{\mathbb{R}^{n-1}}b(x', 0)\,dx^1\cdots dx^{n-1}.$$
> > The two factors of $(-1)^n$ match; the two sides are equal. $\square$

> [!note]- Lemma 3: Partition of unity glues local Stokes into global Stokes
> **Statement:** If Stokes's theorem $\int_M d\omega = \int_{\partial M}\omega$ holds for every $(n-1)$-form $\omega$ supported in the domain of a single oriented chart, then it holds for every compactly supported $(n-1)$-form on $M$.
>
> **Hint:** Write $\omega = \sum_i\psi_i\omega$ for a partition of unity $\{\psi_i\}$ subordinate to a finite oriented chart cover of $\mathrm{supp}\,\omega$; use linearity of $d$ and $\int$.
>
> **Why needed:** It assembles the local Lemma 2 into the global theorem. Without this step Stokes is only known in coordinate patches.
>
> > [!note]- Full proof
> > Since $\omega$ is compactly supported and $M$ is locally compact, $\mathrm{supp}\,\omega$ admits a finite cover by domains of oriented charts $\{U_i\}_{i=1}^N$. Choose a smooth partition of unity $\{\psi_i\}_{i=1}^N$ subordinate to this cover, so $\sum_i\psi_i = 1$ on $\mathrm{supp}\,\omega$ and each $\psi_i$ is compactly supported in $U_i$ ([[Thm - Existence of Smooth Partitions of Unity]]). Then $\omega = \sum_i\psi_i\omega$ and $d\omega = \sum_i d(\psi_i\omega)$ (sums are finite). Each $\psi_i\omega$ is supported in $U_i$, so by hypothesis $\int_M d(\psi_i\omega) = \int_{\partial M}\psi_i\omega$. Summing,
> > $$\int_M d\omega = \sum_{i=1}^N\int_M d(\psi_i\omega) = \sum_{i=1}^N\int_{\partial M}\psi_i\omega = \int_{\partial M}\sum_{i=1}^N\psi_i\omega = \int_{\partial M}\omega. \qquad\square$$

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $M$ be an oriented smooth $n$-manifold with boundary, $\partial M$ carrying the induced orientation, and $\omega \in \Omega^{n-1}_c(M)$ a compactly supported smooth $(n-1)$-form. Then $\int_M d\omega = \int_{\partial M}\omega$.
>
> **Step 0 — Reduction by linearity.** The set of $\omega$ for which the identity holds is closed under linear combinations and under taking pullbacks (since $d$ and $\int$ commute with pullback for orientation-preserving charts). Hence it suffices to prove Stokes for forms supported in a single chart (Lemma 3 then handles the general case via partition of unity).
>
> **Step 1 — Localization.** Suppose $\omega$ is supported in the domain of an oriented chart $(U, \varphi)$. We split into two cases.
>
> *Interior chart, $\varphi(U) \subseteq \mathbb{R}^n$.* In this case $\overline{\mathrm{supp}\,\omega} \cap \partial M = \emptyset$, so $\int_{\partial M}\omega = 0$. We must show $\int_M d\omega = 0$. Pulling back via $\varphi$, $\int_M d\omega = \int_{\mathbb{R}^n}d((\varphi^{-1})^*\omega)$. For a compactly supported $(n-1)$-form on $\mathbb{R}^n$, this is zero by Lemma 1 applied to the unique surviving partial.
>
> *Boundary chart, $\varphi(U) \subseteq \mathbb{H}^n$.* Pull back via $\varphi$:
> $$\int_M d\omega = \int_{\mathbb{H}^n}d((\varphi^{-1})^*\omega), \qquad \int_{\partial M}\omega = \int_{\partial\mathbb{H}^n}(\varphi^{-1})^*\omega,$$
> using $\varphi^*d = d\varphi^*$ and chart-independence of the integral on the boundary ($\partial\mathbb{H}^n$ carries the induced orientation, matching that of $\partial M$ via $\varphi$).
>
> **Step 2 — Half-space computation (Lemma 2).** By linearity (and by the basis-decomposition of $(n-1)$-forms), it suffices to handle $(\varphi^{-1})^*\omega = b\,dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n$ for a single basic term. The computation of Lemma 2 gives $\int_{\mathbb{H}^n}d((\varphi^{-1})^*\omega) = \int_{\partial\mathbb{H}^n}(\varphi^{-1})^*\omega$ for each basic term.
>
> **Step 3 — Partition-of-unity gluing (Lemma 3).** For general $\omega \in \Omega^{n-1}_c(M)$, take a finite oriented chart cover of $\mathrm{supp}\,\omega$ and a subordinate partition of unity $\{\psi_i\}$. Then $\omega = \sum_i\psi_i\omega$, each $\psi_i\omega$ supported in one chart, and Steps 1–2 apply termwise. Summing,
> $$\int_M d\omega = \sum_i\int_M d(\psi_i\omega) = \sum_i\int_{\partial M}\psi_i\omega = \int_{\partial M}\omega.$$
>
> **Conclusion.** $\int_M d\omega = \int_{\partial M}\omega$ for all compactly supported $\omega \in \Omega^{n-1}_c(M)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Complex analysis: Cauchy's integral theorem.** A holomorphic function $f$ on a domain $U \subseteq \mathbb{C}$ gives a closed 1-form $f(z)\,dz$ on $U$ (closedness: $d(f\,dz) = (\partial_zf)\,dz\wedge dz + (\partial_{\bar z}f)\,d\bar z\wedge dz = 0$ since $\partial_{\bar z}f = 0$ by holomorphicity and $dz\wedge dz = 0$). By Stokes applied to a region $D \subseteq U$ bounded by a closed curve $\gamma$, $\oint_\gamma f\,dz = \int_D d(f\,dz) = 0$. This is the **Cauchy integral theorem**. The non-obvious step: the foundational theorem of complex analysis is the case "closed 1-form on a 2-manifold" of Stokes.

**Electromagnetism: charge conservation from $d^2 = 0$.** The current 3-form $J$ on Minkowski space satisfies $d{\star}F = J$ (the inhomogeneous Maxwell equation). Then $dJ = d^2{\star}F = 0$ — current is closed, which means *charge is conserved*. Integrate over a 4-volume bounded by two spatial slices via Stokes: $0 = \int_M dJ = \int_{\partial M}J$, which becomes "total charge at time $t_2$ = total charge at time $t_1$". This is the integral version of $\partial_\mu J^\mu = 0$. See [[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]].

**Algebraic topology: degree of a map.** For a smooth map $f : M \to N$ between compact oriented $n$-manifolds without boundary, the **degree** is $\deg(f) := \int_M f^*\omega / \int_N\omega$ for any volume form $\omega$ on $N$ (the answer is independent of $\omega$). Stokes ensures this is well-defined: changing $\omega$ by $d\eta$ changes $f^*\omega$ by $d(f^*\eta)$, and $\int_M d(f^*\eta) = 0$ on a closed $M$. The degree is the basic homological invariant of a map.

**Gauge theory: the second Bianchi identity and topological charges.** For a connection 1-form $A$ on a principal bundle with curvature 2-form $F = dA + A\wedge A$, the **Bianchi identity** $d_AF = 0$ holds automatically. Integrating $\mathrm{tr}(F \wedge F)$ over a closed 4-manifold gives the second Chern number $c_2$, a topological invariant. Stokes proves this is well-defined: $\mathrm{tr}(F \wedge F)$ is closed (by Bianchi), and changing the connection by an exact form leaves the integral unchanged.

**General relativity: the ADM mass.** For an asymptotically-flat spacelike slice of spacetime, the **ADM mass** is defined as a flux integral at infinity: $m_{ADM} = \tfrac{1}{16\pi}\lim_{R\to\infty}\oint_{S_R}\big[\sum_{i,j}(\partial_jg_{ij} - \partial_ig_{jj})\big]\,dA$. Stokes is what relates this surface integral to a volume integral of the scalar curvature plus a stress-energy term; the boundary integral form is the more useful one.

---

# Bridges

- **[[Thm - The General Stokes Theorem|The General Stokes Theorem (Multivariate Analysis IV)]]** — this is the Euclidean precursor: Stokes for compact $k$-surfaces *embedded* in $\mathbb{R}^N$. The manifold version of this topic generalizes that statement by removing the embedding and stating the result intrinsically. The proof structures coincide: in both cases, the global statement reduces to the half-space model via partition of unity, and the half-space model reduces to the one-variable FTC. The manifold version subsumes the Euclidean one — any Euclidean Stokes computation is a special case of the manifold one applied to an embedded submanifold.

- **[[Thm - Green's Theorem|Green's Theorem]] and [[Thm - The Divergence Theorem|the Divergence Theorem]] and [[Thm - The Kelvin-Stokes Theorem|the Kelvin–Stokes Theorem]]** — these are *not separate theorems* but the cases $\dim M = 2$ (planar), $\dim M = n$ (Euclidean), $\dim M = 2$ (in $\mathbb{R}^3$) of this single identity, obtained by choosing $\omega$ as a 1-form, an $(n-1)$-form, or a 1-form respectively, and translating wedge products into div/curl notation via the metric. The general Stokes theorem is the *statement*; the three classical theorems are its *readings* in particular settings.

- **The Fundamental Theorem of Calculus** — the case $n = 1$. With $M = [a, b]$, $\partial M = \{b\}^+ \cup \{a\}^-$, and $\omega$ a 0-form (function) $f$, Stokes reads $\int_{[a, b]}df = \int_{\partial[a, b]}f = f(b) - f(a)$. The 1-form $df = f'(x)\,dx$, so this is $\int_a^bf'(x)\,dx = f(b) - f(a)$. The Fundamental Theorem of Calculus is the one-dimensional case of Stokes; every higher case is this case applied in one transverse direction inside a partition of unity.

- **[[Thm - The Poincaré Lemma|The Poincaré Lemma]]** — the converse direction. Stokes shows exact forms integrate to zero over closed manifolds; the Poincaré lemma asks when a closed form is exact, and the gap between the two is exactly **de Rham cohomology** $H^k_{dR}(M)$. Together they make integration a perfect pairing between cohomology and homology. The Poincaré lemma is the "vanishing of $H^k_{dR}$ on contractible domains"; Stokes is the "integration of $d\omega$ vanishes on $\partial$-less manifolds"; both are facets of the same $(d, \partial)$-duality.

- **The boundary operator $\partial$ and singular homology** — Stokes says $\langle d\omega, M\rangle = \langle\omega, \partial M\rangle$ where the brackets are integration. This exhibits $d$ on forms and $\partial$ on chains as *formal adjoints*. The identity $\partial^2 = 0$ on chains (boundary of a boundary is empty) is the geometric dual of $d^2 = 0$ on forms, and the two complexes — de Rham complex $(\Omega^*, d)$ and singular chain complex $(C_*, \partial)$ — are paired by integration. **De Rham's theorem** says the resulting cohomology pairing $H^k_{dR}(M) \times H_k(M) \to \mathbb{R}$ is perfect, identifying analytic and topological cohomology.

- **Conservation laws in physics — Noether's theorem on a manifold** — for a Lagrangian field theory on a manifold $M$, Noether's theorem produces a conserved current $J$ for each continuous symmetry, satisfying $dJ = 0$ on-shell. Integrating $J$ over a closed spacelike slice gives a conserved charge $Q = \int_\Sigma J$; Stokes applied to a 4-volume bounded by two such slices proves $Q(\Sigma_1) = Q(\Sigma_2)$ — the charge is conserved. This is the direct, intrinsic version of the conservation laws of physics.

- **Gauss–Bonnet and characteristic classes** — for a closed oriented even-dimensional Riemannian manifold $M^{2n}$, the **Chern–Gauss–Bonnet theorem** says $\chi(M) = \int_M\mathrm{Pf}(\Omega/2\pi)$, where $\Omega$ is the curvature 2-form. Stokes is used to show this integral is independent of the connection (changing the connection changes the integrand by an exact form). The deeper structure: characteristic classes are cohomology classes of $M$ represented by closed forms built from curvature, and their integrals over $M$ are well-defined by Stokes.

---

# Unlocked by This

> [!tip] de Rham Cohomology *(from Algebraic Topology)*
> Stokes shows $\int_M$ kills exact forms on closed oriented manifolds, so integration descends to a pairing $H^k_{dR}(M) \times H_k(M) \to \mathbb{R}$ between de Rham cohomology and singular homology. **De Rham's theorem** says this pairing is perfect — the analytic and topological cohomologies are canonically isomorphic, with integration providing the isomorphism. This is the most powerful application of Stokes and the foundation of the entire de Rham theory.

> [!tip] Poincaré Duality *(from Algebraic Topology)*
> On a compact oriented $n$-manifold without boundary, the wedge-and-integrate pairing $H^k_{dR}(M) \times H^{n-k}_{dR}(M) \to \mathbb{R}$, $([\omega], [\eta]) \mapsto \int_M\omega\wedge\eta$, is non-degenerate. This is **Poincaré duality**, the deepest structural consequence of orientation: the existence of a nonzero top-degree integral functional makes wedge product a perfect pairing in complementary degrees. Stokes is what makes the pairing well-defined.

> [!tip] Chern–Gauss–Bonnet Theorem *(from Differential Geometry)*
> For a closed oriented even-dimensional Riemannian manifold $M^{2n}$, $\chi(M) = \int_M\mathrm{Pf}(\Omega/2\pi)$, where $\Omega$ is the curvature 2-form of the Levi-Civita connection and $\mathrm{Pf}$ is the Pfaffian. Stokes ensures this integral is independent of the choice of connection. This is the prototype of an **index theorem** — a geometric integral computing a topological integer.

> [!tip] Yang–Mills Action and Instantons *(from Gauge Theory)*
> On a closed oriented 4-manifold, the **Yang–Mills action** $S_{YM}[A] = \tfrac{1}{2}\int_M\mathrm{tr}(F_A\wedge\star F_A)$ has critical points $d_A\star F_A = 0$, the **Yang–Mills equations**. Self-dual solutions ($F_A = \star F_A$) — **instantons** — extremize the action subject to a topological charge fixed by the second Chern number $c_2 = \int_M\mathrm{tr}(F_A\wedge F_A)/8\pi^2$. Stokes makes the topological charge well-defined and proves the lower bound on the action.

> [!tip] Atiyah–Singer Index Theorem *(from Differential Geometry / Mathematical Physics)*
> For an elliptic differential operator $D$ on a closed oriented manifold, the index $\mathrm{ind}(D) = \dim\ker D - \dim\mathrm{coker}\,D$ equals an integral over $M$ of a characteristic form built from the symbol of $D$ and the curvature of the underlying bundles. Stokes plays a crucial role: the integrand is independent of choices because changing them alters the integrand by an exact form. This is the most general known generalization of Gauss–Bonnet.

> [!tip] Holographic Principle and AdS/CFT *(from Mathematical Physics / String Theory)*
> In quantum gravity, the **holographic principle** suggests that the physics of a bulk region $M$ is captured by data on its boundary $\partial M$. The AdS/CFT correspondence is the precise statement: a gravitational theory on a $(d+1)$-dimensional anti-de-Sitter spacetime is equivalent to a conformal field theory on its $d$-dimensional boundary. Stokes-like dualities — bulk forms paired with boundary integrals — are the mathematical substrate of this correspondence.

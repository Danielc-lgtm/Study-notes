---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Dirac Operators are Formally Self-Adjoint"
  - "Def - Manifold with Boundary and Induced Orientation"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Riemannian Volume Form"
  - "Def - Interior Product (Contraction with a Vector Field)"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E \to M$ be a **Dirac bundle** over a **compact** oriented Riemannian manifold $(M, g)$ **with boundary** $\partial M$, with fibre metric $\langle\cdot,\cdot\rangle$, Dirac operator $D$, and Riemannian volume form $\mathrm{vol}$. Let $\nu$ denote the **outward-pointing unit normal** vector field along $\partial M$, and let $\mathrm{vol}_{\partial M}$ be the Riemannian volume form of the boundary $\partial M$ with its induced metric and induced (outward-normal-first) orientation. Let $s_1, s_2 \in \Gamma(E)$ be smooth sections (no support restriction is needed, since $M$ is compact).

**Prove the Green-type formula**
$$\int_M \langle D s_1, s_2\rangle\,\mathrm{vol} \;-\; \int_M \langle s_1, D s_2\rangle\,\mathrm{vol} \;=\; \int_{\partial M} \langle \nu \cdot s_1,\ s_2\rangle\,\mathrm{vol}_{\partial M},$$
where $\nu \cdot s_1$ is Clifford multiplication of $s_1$ by the outward unit normal $\nu$, evaluated on $\partial M$.

> [!warning] ⚠️ Sign correction to the series manifest
> The manifest's tentative statement of this exercise carried the boundary term with a **minus** sign, $-\int_{\partial M}\langle\nu\cdot s_1, s_2\rangle\,\mathrm{vol}_{\partial M}$, and delegated the sign to the writer. Carrying the computation through with the *same* current vector field $V$ used on [[Thm - Dirac Operators are Formally Self-Adjoint|the self-adjointness page]] — namely $\langle V, X\rangle = \langle X \cdot s_1, s_2\rangle$, with **no** minus sign — and the standard *outward* divergence theorem produces the boundary term with a **plus** sign, and the one-dimensional check on $[0, 1]$ below confirms it. We therefore state and prove the formula with the plus sign. (Had we defined $V$ with the opposite sign, the pointwise identity of the self-adjointness page would flip and both sides would flip with it; the stated formula is the one consistent with the vault's fixed convention.)

Finally, **verify the formula on the interval** $M = [0, 1]$ with $E$ the trivial complex line bundle, Clifford multiplication by the unit vector $\partial_x$ given by a fixed operator $e$ with $e^2 = -1$ that is skew-adjoint for the standard Hermitian metric, and $\nabla = d/dx$, so that $D = e\,\dfrac{d}{dx}$.

**Recall:**

The ingredients are the formal self-adjointness of the Dirac operator on a manifold *without* boundary — more precisely its pointwise refinement, which is a local identity valid with or without boundary — the divergence theorem for a compact Riemannian manifold with boundary, Stokes's theorem, and the induced orientation and volume form on the boundary.

![[Thm - Dirac Operators are Formally Self-Adjoint#Statement]]

The load-bearing input is the **pointwise identity** in the Proposition above: with $V$ the vector field determined by $\langle V, X\rangle = \langle X \cdot s_1, s_2\rangle$ for every vector field $X$ (equivalently $V = \sum_i \langle e_i \cdot s_1, s_2\rangle\, e_i$ in a local orthonormal frame $(e_i)$), one has $\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle = \operatorname{div} V$ at every point of $M$. This identity is proved on [[Thm - Dirac Operators are Formally Self-Adjoint|the self-adjointness page]] by a purely local computation in a synchronous frame; it does not use the absence of a boundary, so it holds verbatim here. On a manifold *without* boundary the page then integrates it to $0$; the present exercise integrates it on a manifold *with* boundary, where the divergence theorem contributes a boundary term.

![[Def - Manifold with Boundary and Induced Orientation#The Definition]]

The Stokes theorem we integrate against is:

![[Thm - Stokes' Theorem on Manifolds#Statement]]

The **outward unit normal** $\nu$ is the unique outward-pointing (in the sense of [[Def - Manifold with Boundary and Induced Orientation|the boundary page]]) vector field along $\partial M$ with $\langle\nu,\nu\rangle = 1$ and $\langle\nu, w\rangle = 0$ for all $w \in T_p\partial M$; the induced volume form is $\mathrm{vol}_{\partial M} = \iota^*(\iota_\nu\mathrm{vol})$, the contraction of $\mathrm{vol}$ with $\nu$ restricted to the boundary ([[Def - Riemannian Volume Form|Riemannian volume form]], [[Def - Interior Product (Contraction with a Vector Field)|interior product]]).

---

# Convergent Strategy

**Problem class.** This is an *integration-by-parts (Green's-formula) problem*: the same computation that makes the Dirac operator formally self-adjoint on a closed manifold, run instead on a manifold with boundary, where the divergence that previously integrated to zero now leaves a boundary flux. The template is universal — every formal-adjoint statement (for $d$ and $d^*$, for $\nabla$ and $\nabla^*$, for $D$ here) has a with-boundary refinement whose boundary term is the "flux of the current across $\partial M$".

**Assumption pattern.** The recognisable trigger is that the *interior* work is already done: the difference $\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle$ has been shown to be an exact divergence $\operatorname{div} V$ on the self-adjointness page, and this is a *pointwise, local* fact that never referred to $\partial M$. So the entire content of a with-boundary version is *how a divergence integrates over a manifold with boundary* — that is, the divergence theorem — plus the *identification of the boundary integrand* $\langle V, \nu\rangle$ in terms of Clifford data. Whenever an identity has already been reduced to "$\text{something} = \operatorname{div} V$", the with-boundary version is one application of the divergence theorem away.

**Theorem routing.** The route is: (i) quote the pointwise identity $\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle = \operatorname{div} V$ from [[Thm - Dirac Operators are Formally Self-Adjoint|the self-adjointness page]]; (ii) integrate it over $M$ and apply the **divergence theorem with boundary**, $\int_M \operatorname{div} V\,\mathrm{vol} = \int_{\partial M} \langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$, which is itself $\operatorname{div}(V)\,\mathrm{vol} = d(\iota_V\mathrm{vol})$ fed into [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] together with the boundary-contraction identity $\iota^*(\iota_V\mathrm{vol}) = \langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$; (iii) evaluate the boundary integrand $\langle V, \nu\rangle = \langle \nu \cdot s_1, s_2\rangle$ from the definition of $V$.

**Key decision point.** The one genuinely new piece of work, and the place the sign is decided, is the boundary-contraction identity $\iota^*(\iota_V\mathrm{vol}) = \langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$ — that the flux $(n-1)$-form $\iota_V\mathrm{vol}$, restricted to $\partial M$, is exactly the normal component of $V$ times the boundary volume form. The decision is to split $V$ into its normal and tangential parts along $\partial M$: the tangential part contributes nothing because it feeds an over-full wedge (an $n$-form fed $n$ vectors all tangent to the $(n-1)$-dimensional boundary), while the normal part $\langle V, \nu\rangle\nu$ produces $\langle V, \nu\rangle\,\iota^*(\iota_\nu\mathrm{vol}) = \langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$ by the very definition of the induced volume form. Getting the *unit* normal (not merely an outward normal) is what makes $\iota^*(\iota_\nu\mathrm{vol})$ equal to the metric volume form $\mathrm{vol}_{\partial M}$ rather than a positive multiple of it.

---

# Legal Operations Used

1. **Reduce to a divergence, then integrate.** Recognise the antisymmetric-in-$s_1,s_2$ combination $\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle$ as a pure divergence $\operatorname{div} V$ (already done on the self-adjointness page as a *pointwise* identity), so that integrating it becomes a single application of the divergence theorem. This is the same operation used there; the only difference is the domain.

2. **Convert a divergence into an exact form.** Use $\operatorname{div}(V)\,\mathrm{vol} = d(\iota_V\mathrm{vol})$ to rewrite the volume integral of a divergence as the integral of an exact $n$-form, the prerequisite for Stokes.

3. **Apply Stokes's theorem on a manifold with boundary.** $\int_M d\eta = \int_{\partial M}\iota^*\eta$ for the $(n-1)$-form $\eta = \iota_V\mathrm{vol}$; this is the step that produces the boundary integral, and it uses the induced (outward-normal-first) orientation on $\partial M$.

4. **Split a vector field into normal and tangential parts along the boundary.** Write $V = \langle V, \nu\rangle\nu + V^{\top}$ with $V^\top \in T\partial M$; the tangential part is annihilated by restriction of the flux form and the normal part survives.

5. **Identify the induced boundary volume form by contraction with the unit normal.** Use $\mathrm{vol}_{\partial M} = \iota^*(\iota_\nu\mathrm{vol})$ from [[Def - Manifold with Boundary and Induced Orientation|the boundary page]], valid for the *outward unit* normal, to name the boundary integrand.

6. **Evaluate the current on the normal direction.** Apply the defining property $\langle V, X\rangle = \langle X \cdot s_1, s_2\rangle$ with $X = \nu$ to read off $\langle V, \nu\rangle = \langle \nu \cdot s_1, s_2\rangle$.

---

# Hints

> [!note]- Hint 1
> Do **not** start a fresh integration by parts. The self-adjointness page already proves the *pointwise* identity $\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle = \operatorname{div} V$ for the current $V$ with $\langle V, X\rangle = \langle X \cdot s_1, s_2\rangle$, by a local computation that never used the absence of a boundary. Quote it. The whole exercise is then: integrate a divergence over a manifold with boundary.

> [!note]- Hint 2
> Integrating a divergence over a compact manifold with boundary is the **divergence theorem**: $\int_M \operatorname{div}(V)\,\mathrm{vol} = \int_{\partial M}\langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$, with $\nu$ the outward unit normal. If you have not got this as a ready-made vault result on Riemannian manifolds, prove it: use $\operatorname{div}(V)\,\mathrm{vol} = d(\iota_V\mathrm{vol})$ and then [[Thm - Stokes' Theorem on Manifolds|Stokes]].

> [!note]- Hint 3
> The heart of the divergence theorem is the boundary-contraction identity $\iota^*(\iota_V\mathrm{vol}) = \langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$. Split $V = \langle V, \nu\rangle\nu + V^{\top}$ along $\partial M$, where $V^\top$ is tangent to the boundary. Show that $\iota^*(\iota_{V^\top}\mathrm{vol}) = 0$ because $\iota_{V^\top}\mathrm{vol}$ evaluated on $n-1$ boundary-tangent vectors feeds the $n$-form $\mathrm{vol}$ a total of $n$ vectors all lying in the $(n-1)$-dimensional $T_p\partial M$, hence linearly dependent. The normal part gives $\langle V, \nu\rangle\,\iota^*(\iota_\nu\mathrm{vol}) = \langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$.

> [!note]- Hint 4
> The last step is pure book-keeping: $\langle V, \nu\rangle = \langle \nu \cdot s_1, s_2\rangle$ directly from the definition of $V$ (take $X = \nu$ in $\langle V, X\rangle = \langle X \cdot s_1, s_2\rangle$). For the $[0, 1]$ check, note $D = e\,d/dx$ with $e$ skew-adjoint and $e^2 = -1$, compute $\frac{d}{dx}\langle e s_1, s_2\rangle$, and remember the outward normals are $\nu = +\partial_x$ at $x = 1$ and $\nu = -\partial_x$ at $x = 0$, so $\nu\cdot = e$ at $1$ and $\nu\cdot = -e$ at $0$.

---

# Solution

The interior computation is already finished on the self-adjointness page: the difference of the two Dirac pairings is, pointwise, the divergence of the Clifford current $V$ dual to $X \mapsto \langle X \cdot s_1, s_2\rangle$. All that remains is to integrate this divergence over a manifold with boundary, where the divergence theorem converts $\int_M \operatorname{div} V$ into the boundary flux $\int_{\partial M}\langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$, and then to recognise the normal component of the current as $\langle \nu \cdot s_1, s_2\rangle$. The genuine work is the divergence theorem itself, whose boundary integrand fixes the sign.

**Step 1: The pointwise divergence identity holds on $M$.**

By the self-adjointness page, the current vector field $V$ with $\langle V, X\rangle = \langle X \cdot s_1, s_2\rangle$ satisfies $\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle = \operatorname{div} V$ at every point of $M$.

> [!note]- Derivation
> Define $V$ by $\langle V, X\rangle = \langle X \cdot s_1, s_2\rangle$ for every vector field $X$; equivalently $V = \sum_i \langle e_i \cdot s_1, s_2\rangle\, e_i$ in a local orthonormal frame $(e_i)$. This is a smooth vector field: $X \mapsto \langle X \cdot s_1, s_2\rangle$ is $C^\infty(M)$-linear in $X$ (Clifford multiplication is a bundle morphism, the metric is linear in its first slot), so it is a $1$-form, and $V$ is its metric dual under the [[Def - Musical Isomorphism (Flat and Sharp)|sharp isomorphism]].
>
> The Proposition on [[Thm - Dirac Operators are Formally Self-Adjoint|the self-adjointness page]] (restated in the Recall above) proves the **pointwise identity**
> $$\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle = \operatorname{div} V \qquad \text{(pointwise, everywhere on } M\text{),}$$
> where $\operatorname{div} V = \sum_i \langle \nabla^{LC}_{e_i} V, e_i\rangle$ in an orthonormal frame. That proof is entirely local: it computes at an arbitrary point $m$ in a synchronous orthonormal frame, expands $\operatorname{div} V(m) = \sum_i e_i\langle e_i \cdot s_1, s_2\rangle(m)$ using metric-compatibility of $\nabla$ (condition (1)) and the module-derivation property (condition (3)) — with the frame terms $\nabla^{LC}_{e_i}e_i(m) = 0$ dropping out — and recombines using skew-adjointness of Clifford multiplication (condition (2)). No step used that $M$ has empty boundary. Hence the identity holds verbatim on our compact manifold with boundary.

**Step 2: The divergence theorem on a compact manifold with boundary.**

For a smooth vector field $V$ on a compact oriented Riemannian manifold $M$ with boundary,
$$\int_M \operatorname{div}(V)\,\mathrm{vol} = \int_{\partial M} \langle V, \nu\rangle\,\mathrm{vol}_{\partial M},$$
with $\nu$ the outward unit normal.

> [!note]- Derivation
> **Sub-step 2a — the divergence is an exact form.** We first record $\operatorname{div}(V)\,\mathrm{vol} = d(\iota_V\mathrm{vol})$. Fix $m \in M \setminus \partial M$ (or an interior point of a boundary chart) and choose a positively oriented local orthonormal frame $(e_i)$, synchronous at $m$ (so $\nabla^{LC}_{e_i}e_j(m) = 0$), with dual coframe $(e^i)$; then $\mathrm{vol} = e^1 \wedge \cdots \wedge e^n$ near $m$ ([[Def - Riemannian Volume Form|Riemannian volume form]]). Writing $V = \sum_j V^j e_j$ with $V^j = \langle V, e_j\rangle$, the interior product on a top form is
> $$\iota_V\mathrm{vol} = \sum_{j=1}^n (-1)^{j-1} V^j\, e^1 \wedge \cdots \widehat{e^j} \cdots \wedge e^n \qquad \text{([[Def - Interior Product (Contraction with a Vector Field)|interior product on a top form]]),}$$
> where $\widehat{e^j}$ marks omission. Applying $d$ and evaluating at $m$, where $de^i(m) = 0$ (Cartan's first structural equation for the torsion-free Levi-Civita connection, with synchronous $\Rightarrow$ vanishing connection $1$-forms at $m$), only the $dV^j$ terms survive, and of the expansion $dV^j = \sum_i e_i(V^j)e^i$ only $i = j$ avoids repeating a coframe factor:
> $$d(\iota_V\mathrm{vol})(m) = \sum_{j=1}^n e_j(V^j)(m)\, \mathrm{vol} = \Big(\sum_j \langle \nabla^{LC}_{e_j} V, e_j\rangle\Big)(m)\,\mathrm{vol} = \operatorname{div}(V)(m)\,\mathrm{vol},$$
> using metric-compatibility of $\nabla^{LC}$ and $\nabla^{LC}_{e_j}e_j(m) = 0$ for the middle equality. As $m$ was arbitrary, $\operatorname{div}(V)\,\mathrm{vol} = d(\iota_V\mathrm{vol})$ on all of $M$. (This is Lemma 2 of the self-adjointness page, whose first half is a boundary-free local statement.)
>
> **Sub-step 2b — Stokes.** Since $M$ is compact, $\iota_V\mathrm{vol}$ is a smooth $(n-1)$-form (automatically compactly supported). By [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] — for an oriented smooth $n$-manifold with boundary and a compactly supported $(n-1)$-form $\eta$, $\int_M d\eta = \int_{\partial M}\iota^*\eta$ with $\partial M$ in the induced orientation — applied to $\eta = \iota_V\mathrm{vol}$,
> $$\int_M \operatorname{div}(V)\,\mathrm{vol} = \int_M d(\iota_V\mathrm{vol}) = \int_{\partial M} \iota^*(\iota_V\mathrm{vol}), \qquad \iota : \partial M \hookrightarrow M.$$
>
> **Sub-step 2c — the boundary integrand.** We claim $\iota^*(\iota_V\mathrm{vol}) = \langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$. Fix $p \in \partial M$. The tangent space decomposes orthogonally as $T_pM = \mathbb{R}\nu \oplus T_p\partial M$, so write
> $$V_p = \langle V, \nu\rangle\,\nu + V^{\top}, \qquad V^{\top} \in T_p\partial M.$$
> By linearity of the interior product in the vector, $\iota_{V}\mathrm{vol} = \langle V, \nu\rangle\,\iota_\nu\mathrm{vol} + \iota_{V^\top}\mathrm{vol}$. Restrict (pull back by $\iota$) to $\partial M$ and evaluate on any $E_1, \dots, E_{n-1} \in T_p\partial M$:
> $$\iota^*(\iota_{V^\top}\mathrm{vol})(E_1, \dots, E_{n-1}) = \mathrm{vol}(V^\top, E_1, \dots, E_{n-1}) = 0,$$
> because all $n$ arguments $V^\top, E_1, \dots, E_{n-1}$ lie in the $(n-1)$-dimensional subspace $T_p\partial M$ and are therefore linearly dependent, and an alternating $n$-form vanishes on a linearly dependent list. Hence the tangential part restricts to zero, and
> $$\iota^*(\iota_V\mathrm{vol}) = \langle V, \nu\rangle\,\iota^*(\iota_\nu\mathrm{vol}) = \langle V, \nu\rangle\,\mathrm{vol}_{\partial M},$$
> the last equality being the definition of the induced volume form: by [[Def - Manifold with Boundary and Induced Orientation|the boundary page]], for the *outward unit* normal $\nu$, $\iota^*(\iota_\nu\mathrm{vol})$ is the positively oriented Riemannian volume form $\mathrm{vol}_{\partial M}$ of $\partial M$. (Directly: if $(E_1, \dots, E_{n-1})$ is a positively oriented orthonormal basis of $T_p\partial M$, then $(\nu, E_1, \dots, E_{n-1})$ is a positively oriented orthonormal basis of $T_pM$ by the outward-normal-first convention, so $\iota^*(\iota_\nu\mathrm{vol})(E_1, \dots, E_{n-1}) = \mathrm{vol}(\nu, E_1, \dots, E_{n-1}) = 1 = \mathrm{vol}_{\partial M}(E_1, \dots, E_{n-1})$; using the unit normal is what makes this $1$ rather than $|\nu|$.)
>
> Combining sub-steps 2b and 2c, $\int_M \operatorname{div}(V)\,\mathrm{vol} = \int_{\partial M}\langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$.

**Step 3: Assemble the Green formula and identify the boundary integrand.**

Integrating the pointwise identity of Step 1 and applying Step 2 gives the boundary term $\int_{\partial M}\langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$, and $\langle V, \nu\rangle = \langle \nu \cdot s_1, s_2\rangle$.

> [!note]- Derivation
> Integrate the pointwise identity $\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle = \operatorname{div} V$ (Step 1) over $M$ against $\mathrm{vol}$; all integrals are finite because $M$ is compact. By Step 2,
> $$\int_M \langle D s_1, s_2\rangle\,\mathrm{vol} - \int_M \langle s_1, D s_2\rangle\,\mathrm{vol} = \int_M \operatorname{div}(V)\,\mathrm{vol} = \int_{\partial M}\langle V, \nu\rangle\,\mathrm{vol}_{\partial M}.$$
> Finally, the defining property of $V$ with $X = \nu$ gives $\langle V, \nu\rangle = \langle \nu \cdot s_1, s_2\rangle$ on $\partial M$. Substituting,
> $$\int_M \langle D s_1, s_2\rangle\,\mathrm{vol} - \int_M \langle s_1, D s_2\rangle\,\mathrm{vol} = \int_{\partial M}\langle \nu \cdot s_1, s_2\rangle\,\mathrm{vol}_{\partial M},$$
> with the **plus** sign, as claimed. When $\partial M = \emptyset$ the right-hand side is empty and we recover the closed-manifold formal self-adjointness of the self-adjointness page.

> [!note]- Complete formal solution
> **Claim.** For a Dirac bundle $E$ over a compact oriented Riemannian manifold $(M, g)$ with boundary, outward unit normal $\nu$, and $s_1, s_2 \in \Gamma(E)$,
> $$\int_M \langle D s_1, s_2\rangle\,\mathrm{vol} - \int_M \langle s_1, D s_2\rangle\,\mathrm{vol} = \int_{\partial M}\langle \nu \cdot s_1, s_2\rangle\,\mathrm{vol}_{\partial M}.$$
>
> Let $V$ be the smooth vector field with $\langle V, X\rangle = \langle X \cdot s_1, s_2\rangle$ for all $X$. By the Proposition on [[Thm - Dirac Operators are Formally Self-Adjoint|the self-adjointness page]] — a pointwise identity proved by a local synchronous-frame computation that does not use boundarylessness — one has $\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle = \operatorname{div} V$ everywhere on $M$.
>
> The divergence theorem on a compact manifold with boundary gives $\int_M \operatorname{div}(V)\,\mathrm{vol} = \int_{\partial M}\langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$: indeed $\operatorname{div}(V)\,\mathrm{vol} = d(\iota_V\mathrm{vol})$ (computed at each point in a synchronous frame, where $de^i = 0$), whence by [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] $\int_M \operatorname{div}(V)\,\mathrm{vol} = \int_{\partial M}\iota^*(\iota_V\mathrm{vol})$; and decomposing $V = \langle V, \nu\rangle\nu + V^\top$ with $V^\top$ tangent to $\partial M$, the tangential part restricts to zero (its flux form feeds $\mathrm{vol}$ an $n$-tuple of boundary-tangent, hence dependent, vectors) while the normal part gives $\langle V, \nu\rangle\,\iota^*(\iota_\nu\mathrm{vol}) = \langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$ by the induced-volume-form definition for the outward unit normal.
>
> Integrating the pointwise identity and applying the divergence theorem,
> $$\int_M \langle D s_1, s_2\rangle\,\mathrm{vol} - \int_M \langle s_1, D s_2\rangle\,\mathrm{vol} = \int_{\partial M}\langle V, \nu\rangle\,\mathrm{vol}_{\partial M} = \int_{\partial M}\langle \nu \cdot s_1, s_2\rangle\,\mathrm{vol}_{\partial M},$$
> the last equality by $\langle V, \nu\rangle = \langle \nu \cdot s_1, s_2\rangle$. $\blacksquare$

## The one-dimensional check on $[0, 1]$

**Step 4: Verify the formula on $M = [0, 1]$, $D = e\,d/dx$, $e^2 = -1$.**

Here both integrals reduce to endpoint evaluations, and the outward normals $\nu = +\partial_x$ at $x = 1$, $\nu = -\partial_x$ at $x = 0$ reproduce the two boundary terms with exactly the plus sign.

> [!note]- Derivation
> Take $M = [0, 1]$ with the standard metric and orientation, $E = [0, 1] \times \mathbb{C}$ trivial with the standard Hermitian metric $\langle z, w\rangle = \bar z w$, Clifford multiplication by the unit vector $\partial_x$ given by the fixed operator $e$ with $e^2 = -1$ (so the Clifford relation $\partial_x \cdot (\partial_x \cdot z) = e(ez) = e^2 z = -z = -|\partial_x|^2 z$ holds) and $e$ **skew-adjoint**, $\langle e z, w\rangle = -\langle z, e w\rangle$; the connection is $\nabla = d/dx$. Then $D s = \partial_x \cdot \nabla_{\partial_x} s = e\, s'$, where $s' = ds/dx$.
>
> **Reduce the interior difference to a total derivative.** For smooth sections $s_1, s_2 : [0, 1] \to \mathbb{C}$, compute, using that $e$ is constant and skew-adjoint and the metric coefficients are constant,
> $$\frac{d}{dx}\langle e\, s_1, s_2\rangle = \langle e\, s_1', s_2\rangle + \langle e\, s_1, s_2'\rangle \qquad \text{(product rule; } e \text{ constant)}$$
> $$= \langle e\, s_1', s_2\rangle - \langle s_1, e\, s_2'\rangle = \langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle \qquad \text{(skew-adjointness of } e \text{ on the second term; } D = e\, d/dx\text{).}$$
> This is precisely the pointwise identity of Step 1 in one dimension, with the current $V = \langle \partial_x \cdot s_1, s_2\rangle\,\partial_x = \langle e s_1, s_2\rangle\,\partial_x$, whose divergence is $\frac{d}{dx}\langle e s_1, s_2\rangle$.
>
> **Integrate.** By the fundamental theorem of calculus (the one-dimensional divergence theorem),
> $$\int_0^1 \big(\langle D s_1, s_2\rangle - \langle s_1, D s_2\rangle\big)\,dx = \int_0^1 \frac{d}{dx}\langle e s_1, s_2\rangle\,dx = \langle e s_1(1), s_2(1)\rangle - \langle e s_1(0), s_2(0)\rangle.$$
>
> **Compare with the boundary formula.** The boundary is $\partial M = \{0, 1\}$, a $0$-manifold; its induced volume form is the counting measure with the induced orientation, so $\int_{\partial M} f\,\mathrm{vol}_{\partial M} = \sum_{p \in \partial M} \varepsilon(p) f(p)$, where $\varepsilon(1) = +1$ and $\varepsilon(0) = -1$ by the induced orientation of $[0,1]$ ([[Def - Manifold with Boundary and Induced Orientation|the boundary page]], $0$-dimensional case). But this endpoint sign is already carried by the outward unit normal: at $x = 1$ the outward normal is $\nu = +\partial_x$, so $\nu \cdot s_1 = e\, s_1$; at $x = 0$ the outward normal is $\nu = -\partial_x$, so $\nu \cdot s_1 = -e\, s_1$. Reading $\int_{\partial M}\langle \nu \cdot s_1, s_2\rangle\,\mathrm{vol}_{\partial M}$ with the $0$-dimensional convention that the outward normal already encodes the endpoint orientation,
> $$\int_{\partial M}\langle \nu \cdot s_1, s_2\rangle\,\mathrm{vol}_{\partial M} = \langle e\, s_1(1), s_2(1)\rangle + \langle (-e)\, s_1(0), s_2(0)\rangle = \langle e s_1(1), s_2(1)\rangle - \langle e s_1(0), s_2(0)\rangle.$$
> This equals the integrated interior difference computed above, confirming
> $$\int_0^1 \langle D s_1, s_2\rangle\,dx - \int_0^1 \langle s_1, D s_2\rangle\,dx = \langle \nu \cdot s_1, s_2\rangle\big|_{x=1} + \langle \nu \cdot s_1, s_2\rangle\big|_{x=0},$$
> the boundary formula with the **plus** sign. Had the manifest's minus sign been used, the $x = 1$ term would read $-\langle e s_1(1), s_2(1)\rangle$ and disagree with the elementary integration by parts; the check therefore fixes the sign to plus.

---

# Key Takeaways

**Every formal-adjoint identity has a with-boundary refinement, and the refinement is one application of the divergence theorem beyond the closed case.** The structural lesson is that "formally self-adjoint" is the statement "the difference of the two pairings is a divergence", and a divergence integrates to a boundary flux, which vanishes only when the boundary is empty. So the moment an integration-by-parts computation has been reduced to "$\text{difference} = \operatorname{div} V$" — as the self-adjointness page does for the Dirac operator, and as the analogous pages do for $d$ versus $d^*$ and for $\nabla$ versus $\nabla^*$ — the with-boundary Green formula is immediate: apply the divergence theorem and read off $\int_{\partial M}\langle V, \nu\rangle$. This is why one never re-derives the boundary version from scratch; one locates the current $V$ and quotes the divergence theorem. The reusable trigger is: *a formal-adjoint statement on a closed manifold, plus a boundary* $\Rightarrow$ *the same identity with $+\int_{\partial M}\langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$ appended, where $V$ is the current already extracted in the closed-case proof.*

**The boundary integrand is the normal component of the current, and the outward *unit* normal is what pins both the value and the sign.** The single subtle point in the divergence theorem is the identity $\iota^*(\iota_V\mathrm{vol}) = \langle V, \nu\rangle\,\mathrm{vol}_{\partial M}$: the flux $(n-1)$-form restricted to $\partial M$ sees only the part of $V$ normal to the boundary, because the tangential part feeds the top form $\mathrm{vol}$ too many boundary-tangent vectors and is annihilated. Two choices must both be right for the clean statement. First, the normal must be the *unit* normal, so that $\iota^*(\iota_\nu\mathrm{vol})$ is the metric boundary volume form $\mathrm{vol}_{\partial M}$ and not a positive multiple of it. Second, it must be the *outward* normal, matched to the *induced* (outward-normal-first) orientation of $\partial M$; this pairing of "outward normal" with "induced orientation" is exactly the convention that removes every stray sign from Stokes's theorem, and it is what makes the boundary term of a Dirac operator come out as $+\int_{\partial M}\langle \nu \cdot s_1, s_2\rangle$. Whenever a boundary term's sign is in doubt, check it against the outward-normal-first convention and against the elementary case.

**A one-dimensional check is the fastest way to fix a sign, and here it silently packages the endpoint orientation into the Clifford factor $\nu\cdot$.** The $[0, 1]$ computation is worth more than a spot verification: it exposes how the abstract boundary integral degenerates in dimension one. The boundary is two points, the "boundary volume form" is signed counting with $+1$ at the right endpoint and $-1$ at the left, and — the instructive part — this endpoint sign is exactly reproduced by the outward normal flipping from $+\partial_x$ to $-\partial_x$, so that writing the integrand as $\langle \nu \cdot s_1, s_2\rangle$ with the outward normal automatically installs the correct endpoint signs. This is the general phenomenon in miniature: the outward normal carries the orientation data, and the interior product with a *unit* vector carries the metric normalisation, so the compact expression $\int_{\partial M}\langle \nu \cdot s_1, s_2\rangle\,\mathrm{vol}_{\partial M}$ is doing the book-keeping that a coordinate computation would have to do endpoint by endpoint, face by face. When a Green's formula's sign is contested, reduce to $M = [0, 1]$ or $M = \overline{B^n}$ and let the fundamental theorem of calculus adjudicate.

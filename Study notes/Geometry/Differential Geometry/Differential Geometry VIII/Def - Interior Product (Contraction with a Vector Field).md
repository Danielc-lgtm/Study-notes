---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - The Wedge Product on a Manifold"
  - "Def - Vector Field on a Manifold"
  - "Def - Alternating Tensor and Lambda k V Dual"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold. $\mathfrak{X}(M)$ is the space of smooth vector fields on $M$. $\Omega^k(M)$ is the space of smooth $k$-forms; $\Omega^\bullet(M) = \bigoplus_k \Omega^k(M)$. The interior product (contraction) is written $\iota_X\omega$ or $X \lrcorner\, \omega$ ("$X$ into $\omega$"), and is read "the form $\omega$ with $X$ contracted into its first slot." The full registry is on [[Differential Geometry VIII — Differential Forms]].

---

# Axiom Motivation

The motivation for the interior product is straightforward and forced: forms eat vectors, and we want an algebraic operation that performs the eating without invoking flows or geometric machinery. Specifically, given a vector field $X$ and a $k$-form $\omega$, we want to plug $X$ into the first slot of $\omega$ and produce a $(k-1)$-form. There is essentially no choice in how to do this — the definition $(\iota_X\omega)(X_1, \dots, X_{k-1}) = \omega(X, X_1, \dots, X_{k-1})$ is the *only* natural way — and the resulting operation has elegant algebraic properties that earn it its own name.

**Why call it a derivation?** Because it satisfies a Leibniz-type rule:
$$\iota_X(\omega \wedge \eta) = (\iota_X\omega) \wedge \eta + (-1)^{\deg\omega}\omega \wedge (\iota_X\eta).$$
The sign $(-1)^{\deg\omega}$ comes from the same place as the sign in the graded Leibniz for $d$: passing the degree-changing operator $\iota_X$ past the $\deg\omega$ factors of $\omega$ produces signs by anticommutativity. So $\iota_X$ is a graded *anti*-derivation of degree $-1$ (parallel to $d$, which is a graded anti-derivation of degree $+1$).

**Why is $\iota_X^2 = 0$?** Because $\iota_X^2\omega(X_1, \dots, X_{k-2}) = \omega(X, X, X_1, \dots, X_{k-2})$, which vanishes by alternation (two repeated arguments). This is the pointwise statement that filling two slots of an alternating tensor with the same vector kills it.

The combination of $\iota_X^2 = 0$ with the analogous $d^2 = 0$ and the graded-derivation property of each makes $d$ and $\iota_X$ generate a *Lie superalgebra* of operations on $\Omega^\bullet(M)$. The non-trivial commutator $\{d, \iota_X\} = d\iota_X + \iota_X d$ — the anticommutator, since both have odd-parity degree shift — is precisely the **Lie derivative** $\mathcal{L}_X$. This is **Cartan's magic formula**, and it is what makes the interior product structurally essential rather than just a convenient bookkeeping operation: the interior product, the exterior derivative, and the Lie derivative are three sides of a single algebraic identity, and you cannot dispense with any one of them.

**What breaks if we tried to insert $X$ into a different slot?** Nothing structurally — we could equally well define $\tilde\iota_X\omega(X_1, \dots, X_{k-1}) = \omega(X_1, \dots, X_{k-1}, X)$ by inserting into the last slot. By alternation, $\tilde\iota_X\omega = (-1)^{k-1}\iota_X\omega$, so the two differ only by a sign that depends on $k$. The convention "first slot" is universal because it makes the formulas (Cartan, Leibniz) look cleanest.

**What breaks if we drop the alternating-tensor requirement?** Then $\iota_X^2 \neq 0$ in general, and Cartan's magic formula no longer holds. The interior product is meaningful for general covariant tensors, but most of its algebraic power requires the alternating setting.

**What is the bridge to integration?** Given a vector field $X$ and a top-form $\omega \in \Omega^n(M)$, the $(n-1)$-form $\iota_X\omega$ is the form whose integral over an oriented hypersurface gives the flux of $X$ through it. This is the origin of the divergence theorem in the language of forms: $d(\iota_X\omega) = (\operatorname{div}_\omega X)\,\omega$ for an appropriately defined divergence, and Stokes' theorem then equates the integrated divergence over a region with the flux through its boundary.

---

# The Definition

Let $X$ be a smooth vector field on a smooth manifold $M$. The **interior product** with $X$ is the $\mathbb{R}$-linear map
$$\iota_X : \Omega^k(M) \longrightarrow \Omega^{k-1}(M), \quad k \geq 1,$$
defined pointwise by
$$(\iota_X\omega)_p(X_1, \dots, X_{k-1}) = \omega_p(X_p, X_{1,p}, \dots, X_{k-1,p}),$$
for any tangent vectors $X_{1,p}, \dots, X_{k-1,p} \in T_pM$ (or equivalently smooth vector fields evaluated at $p$). On $0$-forms (functions), $\iota_X$ is defined to be zero: $\iota_X f = 0$ for $f \in \Omega^0(M)$.

The notation $X \lrcorner\, \omega = \iota_X\omega$ is also standard.

**Smoothness.** If $\omega$ is smooth and $X$ is smooth, then $\iota_X\omega$ is smooth.

**Coordinate expression.** In a chart $(U, x^i)$, with $X = \sum_i X^i \partial/\partial x^i$ and $\omega = \sum'_I \omega_I\,dx^I$, the interior product expands by the explicit formula. For a single basic $k$-form,
$$\iota_X(dx^{i_1} \wedge \cdots \wedge dx^{i_k}) = \sum_{j=1}^k (-1)^{j-1}\,dx^{i_j}(X)\,dx^{i_1} \wedge \cdots \widehat{dx^{i_j}} \cdots \wedge dx^{i_k},$$
where $dx^{i_j}(X) = X^{i_j}$ is the $i_j$-th component of $X$, and the hat indicates omission. This generalizes the cofactor-style expansion of a determinant by one row.

**Algebraic properties.** For any vector field $X$ and forms $\omega \in \Omega^k(M)$, $\eta \in \Omega^\ell(M)$:

1. **$\mathbb{R}$-linearity in $\omega$:** $\iota_X(\omega + \eta) = \iota_X\omega + \iota_X\eta$ (when $k = \ell$), $\iota_X(c\omega) = c\,\iota_X\omega$.
2. **$C^\infty(M)$-linearity in $X$:** $\iota_{fX + gY}\omega = f\,\iota_X\omega + g\,\iota_Y\omega$ for $f, g \in C^\infty(M)$ and vector fields $X, Y$.
3. **Graded anti-derivation:** $\iota_X(\omega \wedge \eta) = (\iota_X\omega) \wedge \eta + (-1)^k\,\omega \wedge (\iota_X\eta)$.
4. **Squared-zero:** $\iota_X \circ \iota_X = 0$.
5. **Two interior products anticommute:** $\iota_X \iota_Y + \iota_Y \iota_X = 0$. (Equivalently, $\iota_X\iota_Y = -\iota_Y\iota_X$.)
6. **Interplay with $d$:** $\mathcal{L}_X = d\iota_X + \iota_X d$ (Cartan's magic formula, [[Thm - Cartan's Magic Formula]]).

Together with the exterior derivative $d$ (degree $+1$, graded derivation), the interior product (degree $-1$, graded anti-derivation) generates a Lie superalgebra of operations on $\Omega^\bullet(M)$, whose even part contains the Lie derivative.

**Special case — interior product of a top-form with a vector field gives a flux $(n-1)$-form.** On an oriented $n$-manifold with a chosen volume form $\Omega \in \Omega^n(M)$, the assignment $X \mapsto \iota_X\Omega$ is a $C^\infty(M)$-linear isomorphism $\mathfrak{X}(M) \to \Omega^{n-1}(M)$ (since $\dim \Lambda^n T_p^*M = 1$ at every point, $\iota_X\Omega = 0$ implies $X = 0$ and an $(n-1)$-form on an $n$-manifold has $\binom{n}{n-1} = n$ components, matching $X$'s $n$ components). This is the **flux form** of $X$, and its integral over an oriented $(n-1)$-submanifold is the flux of $X$ through it.

---

# Categorical Definition

The interior product is the operation that turns $\Omega^\bullet(M)$ into a **graded module over the graded Lie superalgebra of vector fields**, in a sense made precise as follows. The space of vector fields on $M$, viewed as having degree $0$ (well, half-integer parity for the supergrading reasons), generates by interior-product action a degree-$(-1)$ representation on $\Omega^\bullet(M)$, with the squared-zero identity $\iota_X^2 = 0$ encoding the "fermionic" nature of $\iota_X$.

More concretely: define the **Cartan calculus** algebra $\mathcal{C}(M) = \langle d, \iota_X, \mathcal{L}_X : X \in \mathfrak{X}(M)\rangle$ generated by $d$, all interior products, and all Lie derivatives. The graded super-commutators are:
- $[d, d] = 2d^2 = 0$ (degree $+1$, even-even? No: $d$ has odd degree, so $[d, d] = \{d, d\}$ in the supergraded sense $= 2d^2$);
- $[\iota_X, \iota_Y] = \{\iota_X, \iota_Y\} = \iota_X\iota_Y + \iota_Y\iota_X = 0$;
- $\{d, \iota_X\} = d\iota_X + \iota_X d = \mathcal{L}_X$ (Cartan);
- $[\mathcal{L}_X, d] = 0$ (Lie derivative commutes with $d$, corollary of Cartan and $d^2 = 0$);
- $[\mathcal{L}_X, \iota_Y] = \iota_{[X, Y]}$ (Lie bracket appears).

These relations make $\mathcal{C}(M)$ a Lie superalgebra acting on $\Omega^\bullet(M)$. The interior product is the degree-$(-1)$ part of this structure; everything else follows.

This is the categorical reason the interior product matters: it is not just a convenient notation for "plug a vector field into the first slot of a form" — it is the second member of a pair of operations $(d, \iota_X)$ whose anticommutator is the Lie derivative.

---

# Relate to Other Fields / Compression

**The interior product is the fermionic counterpart to wedging with a $1$-form.** In the language of supergeometry, multiplication by $dx^i$ (i.e., wedging with the $1$-form $dx^i$) is a "creation operator" of degree $+1$, and contraction with $\partial/\partial x^i$ (i.e., interior product with the coordinate vector field) is the "annihilation operator" of degree $-1$. They satisfy the canonical anticommutation relation
$$\{dx^i \wedge, \iota_{\partial_j}\} = \delta^i_j,$$
the cleanest finite-dimensional analogue of the canonical anticommutation relations of fermionic field theory. The exterior algebra $\Omega^\bullet(M)$ is, locally, the **Fock space** of $n$ pairs of fermionic creation/annihilation operators, and $d$, $\iota_X$ are particular combinations of them.

**True name:** The interior product is "the unique $C^\infty(M)$-linear (in $X$) graded anti-derivation $\Omega^k \to \Omega^{k-1}$ satisfying $\iota_X f = 0$ on functions and $\iota_X df = X(f)$ on differentials of functions."

A trigger-reaction pattern: **see "compute the Lie derivative of a form" → use Cartan's magic formula $\mathcal{L}_X = d\iota_X + \iota_X d$**, which requires the interior product. The interior product is what makes $\mathcal{L}_X$ algebraically computable without invoking flows.

**Bridge to physics — flux.** On a $3$-manifold $(M^3, \Omega)$ with volume form $\Omega$, the assignment $X \mapsto \iota_X\Omega$ identifies vector fields with $2$-forms, and the integral $\int_S \iota_X\Omega$ over an oriented surface $S$ is the *flux* of $X$ through $S$. The divergence is then defined by $d(\iota_X\Omega) = (\operatorname{div} X)\,\Omega$, and Stokes' theorem becomes the **divergence theorem** $\int_M (\operatorname{div} X)\,\Omega = \int_{\partial M} \iota_X\Omega$. This whole story is the form-theoretic content of [[Thm - The Divergence Theorem]] in MA IV.

**Bridge to Hamiltonian mechanics.** On a symplectic manifold $(M, \omega)$ with symplectic $2$-form $\omega$, a function $H$ (Hamiltonian) determines a vector field $X_H$ — the **Hamiltonian vector field** — by the equation $\iota_{X_H}\omega = dH$. The non-degeneracy of $\omega$ is exactly what makes this equation have a unique solution for every $H$. Hamilton's equations of motion are then the flow of $X_H$, and the entire structure of Hamiltonian mechanics is the interplay of $\iota_X$, $\omega$, and $d$.

**Bridge to gauge theory — Bianchi.** The Bianchi identity $d_\nabla\Omega_\nabla = 0$ for the curvature $2$-form of a connection involves the covariant exterior derivative, which is defined via $\iota$-type contractions with the connection $1$-form. The whole structure of fibre-bundle differential geometry uses interior products at every level.

---

# Examples / Corollaries

**Is an instance — interior product on a $1$-form.** For $X = \partial/\partial x$ and $\omega = f\,dx + g\,dy$ on $\mathbb{R}^2$, $\iota_X\omega = \omega(\partial_x) = f$ — the $x$-component of $\omega$ as a function on $\mathbb{R}^2$. So $\iota_X$ of a $1$-form gives a $0$-form by evaluating the form on $X$.

**Is an instance — interior product on a $2$-form.** For $X = \partial/\partial x$ and $\omega = dx \wedge dy$, $\iota_X\omega = (dx \wedge dy)(\partial_x, \cdot) = dx(\partial_x)\,dy - dy(\partial_x)\,dx = dy$. So $\iota_X(dx \wedge dy) = dy$. More generally, $\iota_X(dx^I) = X^{i_1}\,dx^{i_2 \cdots i_k} - X^{i_2}\,dx^{i_1\, i_3 \cdots i_k} + \cdots$ — the cofactor expansion of a determinant by the first row.

**Is an instance — flux form on $\mathbb{R}^3$.** For $X = (P, Q, R) = P\partial_x + Q\partial_y + R\partial_z$ on $\mathbb{R}^3$ and the standard volume form $\Omega = dx \wedge dy \wedge dz$,
$$\iota_X\Omega = P\,dy \wedge dz - Q\,dx \wedge dz + R\,dx \wedge dy = P\,dy \wedge dz + Q\,dz \wedge dx + R\,dx \wedge dy.$$
This is the $2$-form whose integral over an oriented surface in $\mathbb{R}^3$ is the flux of the vector field $(P, Q, R)$ through that surface. The signed terms come from the cofactor expansion of $\Omega$ along the "$X$" row.

**Is an instance — $\iota_X^2 = 0$.** For any $X$ and any $\omega$, $\iota_X^2\omega(X_1, \dots, X_{k-2}) = \omega(X, X, X_1, \dots, X_{k-2}) = 0$ by alternation (repeated argument $X$).

**Is an instance — graded anti-derivation rule.** For $X = \partial/\partial x$ on $\mathbb{R}^2$, $\omega = dx$, $\eta = dy$ (both $1$-forms),
$$\iota_X(dx \wedge dy) = (\iota_X dx) \wedge dy + (-1)^1 dx \wedge (\iota_X dy) = 1 \cdot dy - dx \cdot 0 = dy,$$
matching the direct computation above.

**Is NOT an instance — interior product reduces degree by $2$.** False. $\iota_X$ reduces degree by exactly $1$ (it eats one vector slot). Reducing by $2$ would require contracting with two vector fields, and the appropriate operation $\iota_Y \iota_X$ is degree $-2$ but is not the same as $\iota_{X \wedge Y}$ (which is not a standard operation).

**Is NOT an instance — interior product on $0$-forms is constant evaluation.** False. $\iota_X f = 0$ on $0$-forms by convention (there is no "first slot" to insert $X$ into). The operation $X(f) = df(X)$, which evaluates the differential of $f$ on $X$, is not $\iota_X f$ — it is $\iota_X(df)$, the interior product of the *differential* with $X$.

**Corollary — Cartan magic formula on functions.** $\mathcal{L}_X f = (d\iota_X + \iota_X d)f = 0 + \iota_X df = df(X) = X(f)$. This recovers the elementary fact that the Lie derivative of a function along $X$ is the directional derivative.

**Corollary — interior product commutes with itself for a single vector field, antisymmetrically with different vector fields.** From property 5, $\iota_X\iota_X = 0$ (also from property 4) and $\iota_X\iota_Y = -\iota_Y\iota_X$. This is the algebraic statement that "fermions anticommute."

**Corollary — degree-counting.** On an $n$-manifold, $\iota_X : \Omega^n(M) \to \Omega^{n-1}(M)$ is a $C^\infty(M)$-linear map between [[Def - Module|modules]] of ranks $\binom{n}{n} = 1$ and $\binom{n}{n-1} = n$. For a fixed nonzero top-form $\Omega$, the map $X \mapsto \iota_X\Omega$ is a $C^\infty(M)$-linear isomorphism $\mathfrak{X}(M) \to \Omega^{n-1}(M)$ (both have rank $n$).

**Calibration check.** Compute $\iota_{\partial_x}(x\,dy \wedge dz)$ on $\mathbb{R}^3$ (answer: $0$, since $dy(\partial_x) = dz(\partial_x) = 0$); compute $\iota_{\partial_z}(dx \wedge dy \wedge dz)$ on $\mathbb{R}^3$ (answer: $dx \wedge dy$); verify $\iota_X^2 = 0$ for $X = x\partial_y - y\partial_x$ and $\omega = dx \wedge dy$; check the graded anti-derivation rule on $\omega = x\,dx$, $\eta = y\,dy$ on $\mathbb{R}^2$. If you can explain why $\iota_X(dx^1 \wedge \cdots \wedge dx^n) = \sum_j (-1)^{j-1} X^j\,dx^1 \wedge \cdots \widehat{dx^j} \cdots \wedge dx^n$ in terms of the cofactor expansion of a determinant, you have understood the interior product.

---

# Unlocked by This

> [!tip] Cartan's Magic Formula *(this chapter)*
> The interior product $\iota_X$, together with the exterior derivative $d$, satisfies the **anticommutator** identity
> $$d\iota_X + \iota_X d = \mathcal{L}_X,$$
> the **Cartan magic formula**. This is the algebraic miracle of the chapter and is the universal route for computing Lie derivatives of forms. See [[Thm - Cartan's Magic Formula]].

> [!tip] Hamiltonian Vector Field *(from Symplectic Geometry)*
> On a symplectic manifold $(M, \omega)$, a function $H$ determines a vector field $X_H$ by $\iota_{X_H}\omega = dH$. The non-degeneracy of $\omega$ is what makes this equation uniquely solvable. The flow of $X_H$ is the **Hamiltonian flow** generated by $H$, and the whole of Hamiltonian mechanics — Poisson brackets $\{f, g\} = \omega(X_f, X_g)$, Liouville's theorem $\mathcal{L}_{X_H}\omega = 0$, Noether's theorem — runs on this construction.

> [!tip] Flux Forms and the Divergence Theorem *(from Differential Geometry IX)*
> On an oriented $n$-manifold with volume form $\Omega$, the interior product $X \mapsto \iota_X\Omega$ identifies vector fields with $(n-1)$-forms. The divergence is then defined by $d(\iota_X\Omega) = (\operatorname{div}X)\,\Omega$, and Stokes' theorem becomes the **divergence theorem**: $\int_M (\operatorname{div}X)\,\Omega = \int_{\partial M}\iota_X\Omega$.

> [!tip] Frobenius Theorem in Forms Language *(from Differential Geometry X)*
> An involutive distribution can be characterized by the annihilator ideal of $1$-forms — the forms that contract to zero with every distribution-vector. Frobenius' theorem in forms language states that involutivity is equivalent to the annihilator ideal being a *differential* ideal: $d\omega \in I$ for every $\omega \in I$, where $I$ is generated by the annihilator $1$-forms. The bridge between the vector-field formulation (DG V/X) and the form formulation runs through interior products.

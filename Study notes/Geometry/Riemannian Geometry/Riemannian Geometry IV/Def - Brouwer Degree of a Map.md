---
type: definition
subject: differential-topology
prereqs:
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Integral of a Compactly Supported Form on a Manifold"
  - "Def - Volume Form"
  - "Thm - Sard's Theorem"
tags: [topology, differential-topology, degree-theory, brouwer]
---

# Notation

Let $M^n, V^n$ be closed (compact, no boundary) oriented smooth manifolds of the same dimension $n$, and $\phi : M \to V$ a smooth map. We write $\omega \in \Omega^n(V)$ for a top-degree differential form and $\int_V\omega$ for its integral over the oriented manifold $V$. A point $y \in V$ is a **regular value** of $\phi$ if $\phi_*$ is surjective (equivalently, bijective when $\dim M = \dim V$) at every preimage $x \in \phi^{-1}(y)$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Axiom Motivation

The desideratum is to define a **homotopy-invariant integer** $\deg(\phi) \in \mathbb{Z}$ associated to any smooth map $\phi : M^n \to V^n$ between closed oriented manifolds of the same dimension, capturing "how many times $\phi$ wraps $M$ around $V$, counted with signs". The integer must satisfy three desiderata: (i) it should reduce to "winding number" when $M = V = S^1$; (ii) it should be invariant under smooth homotopies $\phi_t$; (iii) it should be computable both as an integral $\int_M\phi^*\omega$ and as a signed count of preimages of a regular value. These three properties pin down the definition essentially uniquely.

**Why an integral?** Consider any normalised $n$-form $\omega$ on $V$ — an $n$-form with $\int_V\omega = 1$. Its pullback $\phi^*\omega$ is an $n$-form on $M$, and its integral $\int_M\phi^*\omega$ is a real number. The crucial question is whether this real number is *independent of the choice of $\omega$*. The lemma that makes the definition work: any two normalised $n$-forms differ by an exact form, $\omega' - \omega = d\beta$, because their difference has integral zero and on a closed manifold every closed $n$-form with zero integral is exact (this is **Poincaré duality** for top-degree cohomology, or equivalently de Rham). Then
$$
\int_M\phi^*\omega' - \int_M\phi^*\omega = \int_M\phi^*d\beta = \int_M d(\phi^*\beta) = 0
$$
by Stokes' theorem (the boundary of a closed manifold is empty). So $\int_M\phi^*\omega$ is independent of $\omega$ and depends only on $\phi$ — defining $\deg(\phi)$ uniquely.

**Why is it an integer?** This is the deepest part: the integral $\int_M\phi^*\omega$, a priori a real number, turns out to be an integer. The proof uses a regular value $y \in V$ (which exists by Sard's theorem, since the regular values are dense) and a bump-form $\omega$ concentrated near $y$. The preimage $\phi^{-1}(y)$ is a finite set $\{x_1, \ldots, x_N\}$ (finite by compactness + the implicit function theorem), and near each $x_i$, $\phi$ is a local diffeomorphism. The integral splits into contributions from each $x_i$, and each contribution is $\pm 1$ depending on whether $\phi$ is orientation-preserving or reversing at $x_i$. Summing gives an integer.

**Why "homotopy invariant"?** A smooth homotopy $\phi_t$ between $\phi_0$ and $\phi_1$ gives a smooth map $\Phi : M \times [0, 1] \to V$, and the difference $\int_M\phi_1^*\omega - \int_M\phi_0^*\omega = \int_{M \times \{1\}}\Phi^*\omega - \int_{M \times \{0\}}\Phi^*\omega$ equals (by Stokes) $\int_{M \times [0, 1]}\Phi^*d\omega = 0$ since $d\omega = 0$ (top-degree forms on $V$ are automatically closed if $V$ has dimension $n$). So $\deg(\phi_t)$ is constant in $t$. This is the property that makes $\deg$ a powerful invariant: it distinguishes homotopy classes of maps and is **the** algebraic count of how a map between closed oriented $n$-manifolds wraps.

**Why "between closed oriented manifolds of the same dimension"?**
- **Closed**: compactness is needed for $\phi^{-1}(y)$ to be finite (otherwise the sum of signs could diverge), and the absence of boundary is needed for Stokes' theorem to make $\int_M$ well-behaved.
- **Oriented**: the orientation is needed both to define $\int_M$ and to assign signs $\pm 1$ to preimage points. Without orientation, one can still define a $\mathbb{Z}/2$-degree (the parity of $|\phi^{-1}(y)|$), but not an integer degree.
- **Same dimension**: if $\dim M < \dim V$, then $\phi(M) \subset V$ has measure zero and $\deg = 0$ trivially; if $\dim M > \dim V$, then $\phi^{-1}(y)$ is a positive-dimensional set, not a finite count.

A forward reference: the [[Thm - Brouwer Degree is a Homotopy Invariant|degree's homotopy invariance]] is what makes the entire theory of **degree theory** in nonlinear analysis (Leray–Schauder, etc.) and topology (winding number, Brouwer fixed-point theorem, fundamental theorem of algebra) work. Without this property, the integer attached to $\phi$ would just be "the algebraic preimage count of $y$", and that would shift wildly as $\phi$ deforms. Homotopy invariance is precisely what locks the count down to a stable integer.

---

# The Definition

> **Definition (Brouwer Degree).** Let $M^n, V^n$ be closed oriented smooth manifolds of the same dimension, $\phi : M \to V$ smooth, and $\omega \in \Omega^n(V)$ any top-degree form with $\int_V\omega = 1$ (any normalised volume form). The **Brouwer degree** of $\phi$ is
> $$
> \deg(\phi) := \int_M \phi^*\omega \;\in \mathbb{R}.
> $$
> This integer (it is an integer — see Theorem below) is independent of the choice of $\omega$.

The two pillars of the construction:

**(Independence of $\omega$.)** If $\omega, \omega'$ are two normalised top-degree forms on $V$, then $\omega' - \omega$ is exact: there exists $\beta \in \Omega^{n-1}(V)$ with $\omega' - \omega = d\beta$. Hence $\int_M\phi^*(\omega' - \omega) = \int_M d(\phi^*\beta) = 0$ by Stokes' theorem on the closed manifold $M$.

**(Integer-valuedness, via regular values.)** By [[Thm - Sard's Theorem|Sard's theorem]], the regular values of $\phi$ are dense in $V$. Pick any regular value $y \in V$. The preimage $\phi^{-1}(y)$ is a finite set $\{x_1, \ldots, x_N\}$ (finite by compactness of $M$ plus the implicit function theorem). At each $x_i$, $\phi_*$ is bijective (since $\dim M = \dim V$ and $y$ regular), so $\phi$ is a local diffeomorphism near $x_i$, and we set $\mathrm{sign}\,\phi(x_i) = +1$ if $\phi_*$ preserves orientation at $x_i$, $-1$ if it reverses orientation. Then
$$
\deg(\phi) = \sum_{x \in \phi^{-1}(y)}\mathrm{sign}\,\phi(x).
$$
This is a finite sum of $\pm 1$'s, hence an integer.

**(Homotopy invariance.)** If $\phi_t : M \to V$ is a smooth homotopy ($t \in [0, 1]$), then $\deg(\phi_t)$ is constant; see [[Thm - Brouwer Degree is a Homotopy Invariant]].

**(Composition.)** For maps $\phi : M \to V$, $\psi : V \to W$ between closed oriented $n$-manifolds, $\deg(\psi \circ \phi) = \deg(\psi)\cdot\deg(\phi)$ — the degree is multiplicative under composition.

---

# Categorical / Structural Definition

Structurally, the Brouwer degree is the map
$$
\deg : [M, V] \to \mathbb{Z}
$$
from the set of homotopy classes of maps $M \to V$ (between closed oriented $n$-manifolds) to the integers. It is the simplest non-trivial homotopy invariant of such maps, and for $M = V = S^n$ it is actually a *complete* invariant (Hopf's theorem): two maps $S^n \to S^n$ are homotopic iff they have the same degree.

From the perspective of **singular homology**, the degree is the integer such that $\phi_* : H_n(M; \mathbb{Z}) \to H_n(V; \mathbb{Z})$, restricted to the fundamental classes, sends $[M] \mapsto \deg(\phi)[V]$. Closed oriented $n$-manifolds have $H_n(M; \mathbb{Z}) = \mathbb{Z}$ generated by the fundamental class $[M]$, and the induced map on $H_n$ is multiplication by an integer — that integer is $\deg(\phi)$. This is the algebraic-topology definition, equivalent to the de Rham / integral definition above by the [[Algebraic Topology I — Singular Homology and the de Rham Theorem|de Rham theorem]].

From **cobordism theory**, the degree is also definable in terms of framed cobordism: maps $S^n \to S^n$ correspond to framed-cobordism classes of $0$-manifolds in $\mathbb{R}^n$, and the degree is the signed count of points.

Functorially: the assignment $\phi \mapsto \deg(\phi)$ is a homotopy-invariant integer-valued functional on $[M, V]$, equivariant under orientation-reversal (reversing the orientation of $M$ or of $V$ negates the degree), and multiplicative under composition.

---

# Relate to Other Fields / Compression

The Brouwer degree is the **higher-dimensional generalisation of the winding number** of a closed curve around a point in the plane. For $M = V = S^1$, $\deg(\phi)$ is exactly the winding number: how many times $\phi : S^1 \to S^1$ wraps. The generalisation to closed oriented $n$-manifolds is direct: $\deg(\phi)$ is the algebraic count of how many times $\phi$ wraps $M$ around $V$.

In **complex analysis**, the degree of a polynomial map $P : \mathbb{CP}^1 \to \mathbb{CP}^1$ is the degree of the polynomial (a generic value of $P$ has exactly $\deg P$ preimages, all with positive sign because holomorphic maps are orientation-preserving). The **fundamental theorem of algebra** is the statement: any polynomial of degree $\geq 1$ has $\deg \geq 1$, hence is surjective (a nonzero-degree map is surjective), hence has $0$ in its image — which is the fundamental theorem.

In **nonlinear analysis**, the **Leray–Schauder degree** generalises the Brouwer degree to infinite-dimensional Banach spaces, providing the topological backbone of **bifurcation theory** and **existence proofs for nonlinear PDE**. It is one of the most powerful tools in functional-analytic PDE theory.

In **dynamical systems**, the degree of a self-map $\phi : M \to M$ is the algebraic count of fixed points (after adjustment by the Lefschetz number) and governs the **Lefschetz fixed-point theorem**.

In **physics**, degrees count topological charges: the **monopole number** of a magnetic monopole, the **winding number** of a topological soliton, the **instanton number** of a gauge field configuration, the **vortex number** of a superconducting current — all are Brouwer degrees of appropriate maps.

**True name:** The Brouwer degree is *the algebraic preimage count of a regular value*. The official "$\int_M\phi^*\omega$" formula is the right definition, but the operational picture is: pick a generic point $y \in V$ (a regular value, which exists by Sard), find the finite set $\phi^{-1}(y)$, and add up the signs $\pm 1$ depending on whether $\phi$ preserves orientation at each preimage. Independence of $y$, integer-valuedness, and homotopy invariance all follow from this picture. The integral formula is the analytic representation; the preimage count is the geometric meaning.

---

# Examples / Corollaries

**Is an instance — the identity map.** For $\phi = \mathrm{id}_V : V \to V$, $\deg = 1$ (every point is its own unique preimage with sign $+1$). For the negative identity (which is only orientation-preserving when $n$ is even — explicitly, the antipodal map $-\mathrm{id} : S^n \to S^n$), $\deg = (-1)^{n+1}$ — see Frankel 8.3(1).

**Is an instance — the degree-$n$ self-map of $S^1$.** $\phi(e^{i\theta}) = e^{in\theta}$ has $\deg(\phi) = n$. The preimage of any regular value has $|n|$ points, all with the same sign.

**Is an instance — a polynomial of degree $n$ on $\mathbb{CP}^1$.** $P(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$ extends to $P : \mathbb{CP}^1 \to \mathbb{CP}^1$ (sending $\infty \mapsto \infty$). The degree as a smooth map is exactly $n$, the degree of the polynomial. See Frankel 8.3(2)–(4). The **fundamental theorem of algebra** is: a map of nonzero degree is surjective, so for $n \geq 1$, $P$ takes the value $0$, i.e., the polynomial has a root.

**Is an instance — the Gauss normal map.** For a closed oriented surface $M^2 \subset \mathbb{R}^3$, the Gauss map $N : M^2 \to S^2$ has degree $\deg(N) = 1 - g$, half the Euler characteristic; see [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]] and [[Thm - Gauss-Bonnet Theorem for Surfaces]].

**Is NOT an instance — a map between manifolds of different dimensions.** The map $S^1 \hookrightarrow S^2$ as the equator is between manifolds of *different* dimensions and has no Brouwer degree. (It has a different invariant — a "linking number" if one views it as embedded in the complement.)

**Is NOT an instance — a non-orientable target.** If $V$ is non-orientable, the integral $\int_V\omega$ does not make sense (orientation is needed to define integration of forms), so $\deg(\phi)$ is undefined. A $\mathbb{Z}/2$-degree (the parity of $|\phi^{-1}(y)|$) is still defined.

**Corollary — a map of nonzero degree is surjective.** If $\phi : M \to V$ has $\deg(\phi) \neq 0$, then every point of $V$ has at least one preimage. **Proof:** If some $y_0 \in V$ were not in the image, then $\phi$ could be homotoped (push everything away from $y_0$) into a map missing a neighbourhood of $y_0$, and an $\omega$ concentrated near $y_0$ would give $\int_M\phi^*\omega = 0$. But $\deg$ is homotopy-invariant, so $\deg(\phi) = 0$, contradiction. Application: a nonconstant polynomial $P : \mathbb{CP}^1 \to \mathbb{CP}^1$ of degree $n \geq 1$ has $\deg \neq 0$, hence is surjective, hence has $0$ in its image — **fundamental theorem of algebra**.

**Corollary — Brouwer fixed-point theorem.** Every smooth map $\phi : B^{n+1} \to B^{n+1}$ has a fixed point. **Proof sketch:** Otherwise the vector field $v(x) = x - \phi(x)$ is nonvanishing on $B$, and on $\partial B = S^n$ never points inward (since $\phi(B) \subset B$). The retraction $r(x) = \phi(x) + t(x - \phi(x))$ (where $t > 0$ is chosen so $r(x) \in S^n$) is a smooth retraction $B \to S^n$, contradicting the impossibility of such a retraction (proved via degree).

**Corollary — degree is multiplicative.** For composable maps $\phi : M \to V$, $\psi : V \to W$, $\deg(\psi\circ\phi) = \deg(\psi)\deg(\phi)$. **Proof:** $(\psi\circ\phi)^*\omega = \phi^*(\psi^*\omega)$, and $\psi^*\omega$ is a form whose integral over $V$ is $\deg(\psi)$.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify by direct computation that the degree-$n$ map $S^1 \to S^1$, $\theta \mapsto n\theta$, has degree $n$, by integrating the normalised volume form $d\theta/2\pi$ pulled back; (ii) check that the antipodal map $S^2 \to S^2$, $\phi(x) = -x$, has degree $(-1)^3 = -1$ (which matches Frankel 8.3(1) with $n = 2$): the antipodal map is orientation-reversing on $S^2$ because the differential at any point is $-\mathrm{id}$ on the tangent space, $\det(-\mathrm{id}) = (-1)^2 = +1$ on a $2$-plane, but the antipodal map sends the outward normal to the inward normal, swapping the orientation; (iii) confirm that the degree of a constant map is $0$: the pullback of any form by a constant is zero.

---

# Unlocked by This

> [!tip] The Gauss Normal Map's Degree and Gauss–Bonnet *(from §4.3)*
> The Brouwer degree of the [[Def - Gauss Normal Map|Gauss normal map]] $N : M^2 \to S^2$ on a closed oriented surface is $\deg(N) = 1 - g$, half the Euler characteristic. Combined with the change-of-area formula $N^*\mathrm{vol}^2_{S^2} = K\, dA$, this yields the [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]] $\int_M K\, dA = 2\pi\chi(M)$.

> [!tip] The Kronecker Index of a Vector Field *(from §4.4)*
> For a vector field $v$ on a closed oriented manifold $M^n$ with an isolated zero at $p$, the **Kronecker (Poincaré–Hopf) index** is the Brouwer degree of $v/|v| : S^{n-1}_\epsilon(p) \to S^{n-1}$ on a small sphere around $p$. The [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]] equates the sum of indices to $\chi(M)$. See [[Def - Kronecker Index of a Vector Field]].

> [!tip] The Fundamental Theorem of Algebra *(from Complex Analysis)*
> A nonconstant polynomial $P : \mathbb{CP}^1 \to \mathbb{CP}^1$ of degree $n$ has Brouwer degree $n \neq 0$, hence is surjective, hence has $0$ in its image. The fundamental theorem of algebra is a one-line corollary of degree theory.

> [!tip] The Leray–Schauder Degree *(from Nonlinear Analysis)*
> Finite-dimensional Brouwer degree generalises to infinite-dimensional Banach spaces — the **Leray–Schauder degree** — for compact perturbations of the identity, providing the topological backbone of **bifurcation theory**, **nonlinear PDE existence proofs**, and **continuation methods** in computational mathematics.

> [!tip] Characteristic Classes via Degree *(from Algebraic Topology III)*
> The Euler number, Pontryagin numbers, and Chern numbers of a manifold are all definable as degrees of appropriate Gauss-type maps into Grassmannians or classifying spaces. Modern characteristic-class theory in [[Algebraic Topology III — Higher Homotopy and Chern Forms]] is the systematic version of this circle of ideas.

---
type: definition
subject: hodge-theory
prereqs:
  - "Def - Harmonic Form"
  - "Def - de Rham Cohomology"
  - "Def - Riemannian Manifold"
tags: [geometry, hodge-theory, kahler-geometry, cohomology]
---

# Notation

$(M, g)$ is a closed oriented Riemannian $n$-manifold. The space of harmonic $k$-forms is $\mathcal{H}^k(M) = \ker(\Delta : \Omega^k \to \Omega^k)$. The $k$-th Hodge number is $h^k(M) := \dim_{\mathbb{R}}\mathcal{H}^k(M)$. The $k$-th Betti number is $b_k(M) := \dim_{\mathbb{R}}H^k_{dR}(M; \mathbb{R})$. On a Kähler manifold (complex of real dimension $2m$ with a closed positive $(1,1)$-form), the refined **Dolbeault Hodge numbers** are $h^{p,q}(M) := \dim_{\mathbb{C}}H^{p,q}_{\bar\partial}(M; \mathbb{C})$, with $H^{p,q}_{\bar\partial}$ the Dolbeault cohomology in bidegree $(p, q)$.

---

# Axiom Motivation

The Hodge number is defined as $h^k(M) = \dim\mathcal{H}^k(M)$, the dimension of the space of harmonic $k$-forms. The definition is forced by three structural pressures.

**Why "harmonic forms" as the thing being counted?** By [[Thm - Harmonic Forms Represent de Rham Cohomology|the Hodge isomorphism]], $\mathcal{H}^k(M) \cong H^k_{dR}(M)$ on a closed Riemannian manifold. So $h^k = \dim\mathcal{H}^k = \dim H^k_{dR} = b_k$, the $k$-th Betti number. The Hodge number is *equal* to the Betti number in the real-coefficient Riemannian case — the two count the same thing. The reason to define them separately is that on a *Kähler* manifold, the Hodge number bifurcates into refined Dolbeault Hodge numbers $h^{p,q}$, which contain strictly more information than the Betti numbers.

**Why distinguish "Hodge number" from "Betti number" if they're equal?** Two reasons. First, the *concept* differs: Betti numbers are defined topologically (as ranks of singular homology / cohomology), while Hodge numbers are defined analytically (as dimensions of solution spaces of an elliptic PDE). The equality $h^k = b_k$ is the content of the Hodge theorem and is far from obvious. Second, in the Kähler case, the Dolbeault Hodge numbers $h^{p,q}$ refine the Betti numbers via the decomposition $b_k = \sum_{p+q=k}h^{p,q}$. The refined Hodge numbers are *not* Betti numbers — they depend on the complex structure — but they organize into the **Hodge diamond**, a fundamental invariant of compact Kähler manifolds.

**Why does the Kähler refinement exist?** On a Kähler manifold (complex manifold with a closed positive $(1, 1)$-form), the exterior derivative splits as $d = \partial + \bar\partial$, with $\partial : \Omega^{p,q} \to \Omega^{p+1, q}$ and $\bar\partial : \Omega^{p,q} \to \Omega^{p, q+1}$ on $(p, q)$-forms. Each of $\partial$ and $\bar\partial$ has its own Laplacian $\Delta_\partial = \partial\partial^* + \partial^*\partial$ and $\Delta_{\bar\partial} = \bar\partial\bar\partial^* + \bar\partial^*\bar\partial$. The **Kähler identities** force $\Delta_d = 2\Delta_\partial = 2\Delta_{\bar\partial}$ — all three Laplacians agree up to a factor of $2$. Consequently, a $d$-harmonic $k$-form decomposes uniquely as a sum of $\bar\partial$-harmonic forms of various bidegrees $(p, q)$ with $p + q = k$. This is the refined Hodge decomposition, and the bidegree summands have dimensions $h^{p,q}$, the **Dolbeault Hodge numbers**.

**Why the diamond structure?** The Hodge numbers $h^{p,q}$ satisfy:
- **Hodge symmetry**: $h^{p,q} = h^{q,p}$ (from complex conjugation),
- **Serre duality**: $h^{p,q} = h^{n-p, n-q}$ (Poincaré-like duality, $n = \dim_{\mathbb{C}}M$),
- **Compatibility**: $b_k = \sum_{p+q=k}h^{p,q}$ (Hodge decomposition).
The two symmetries make the array $\{h^{p,q}\}_{0 \leq p, q \leq n}$ look like a "diamond" with reflective symmetries along both diagonals — the **Hodge diamond** of the Kähler manifold.

**Why is this a topological invariant in the Riemannian case?** The Hodge number $h^k(M; g) = \dim\mathcal{H}^k(M; g)$ depends, at first glance, on the metric $g$. But by the Hodge isomorphism, $h^k = b_k$, the topological Betti number, which depends only on the smooth structure of $M$. So $h^k$ is independent of the metric — different metrics give different harmonic forms, but always the same dimension. This is the structural reason that Hodge theory connects metric-geometric and topological invariants: the *space* of harmonic forms varies with the metric, but its *dimension* is a topological invariant.

**Why is the Kähler refinement metric-dependent only inside the Kähler class?** The Hodge numbers $h^{p,q}$ depend on the complex structure of $M$, but for compact Kähler manifolds they are independent of the choice of Kähler metric within a given complex structure. They are invariants of the complex manifold $M$. In families of complex structures (e.g., parameterized by a moduli space), the Hodge numbers can jump at special points, but generically they are constant.

---

# The Definition

Let $(M, g)$ be a closed oriented Riemannian $n$-manifold. The **$k$-th Hodge number** is
$$h^k(M) := \dim_{\mathbb{R}}\mathcal{H}^k(M),$$
where $\mathcal{H}^k(M) = \ker(\Delta : \Omega^k(M) \to \Omega^k(M))$ is the space of harmonic $k$-forms.

By the [[Thm - Harmonic Forms Represent de Rham Cohomology|Hodge isomorphism theorem]], $h^k(M) = b_k(M)$, the $k$-th Betti number. In particular, $h^k(M)$ is a topological invariant (independent of the metric).

**Kähler refinement.** When $(M, g, J)$ is a compact Kähler manifold of complex dimension $m$ (so $n = 2m$), with complex structure $J$ and Kähler form $\omega \in \Omega^{1,1}(M)$, the Dolbeault cohomology $H^{p,q}_{\bar\partial}(M) = \ker\bar\partial / \operatorname{im}\bar\partial$ on $(p, q)$-forms has finite dimension
$$h^{p,q}(M) := \dim_{\mathbb{C}}H^{p,q}_{\bar\partial}(M).$$
The **Hodge decomposition** holds: $H^k(M; \mathbb{C}) = \bigoplus_{p+q=k}H^{p,q}(M)$. Consequently $b_k(M) = \sum_{p+q=k}h^{p,q}(M)$, and the Dolbeault Hodge numbers refine the Betti numbers. The Dolbeault Hodge numbers $h^{p,q}$ are *complex-manifold* invariants (not just smooth invariants), and they satisfy:
- **Hodge symmetry**: $h^{p,q} = h^{q,p}$.
- **Serre duality**: $h^{p,q} = h^{m-p, m-q}$ (where $m = \dim_{\mathbb{C}}M$).
- **Kähler structure**: $h^{p,p} \geq 1$ for $p = 0, 1, \dots, m$ (Kähler classes provide nonzero classes).

The full table $\{h^{p,q}\}$ for $0 \leq p, q \leq m$ is the **Hodge diamond** of $M$.

---

# Relate to Other Fields / Compression

**The Riemannian Hodge number is the Betti number.** $h^k(M) = b_k(M) = \dim H^k_{dR}(M; \mathbb{R}) = \dim H^k(M; \mathbb{R})$ (the last by the de Rham theorem). So on a smooth manifold without extra structure, the Hodge number is purely topological. The metric is needed to *realize* the cohomology by harmonic forms, but the dimension is metric-independent.

**The Kähler Hodge number is a complex-geometric invariant.** $h^{p,q}(M)$ depends on the complex structure of $M$, not just the smooth structure. On a generic complex manifold (non-Kähler), the Hodge decomposition still holds in some form (Frölicher spectral sequence), but the symmetry $h^{p,q} = h^{q,p}$ can fail. The Kähler condition is what restores symmetry.

**The Hopf number on Lie groups via bi-invariant forms.** On a compact Lie group $G$ with a bi-invariant metric, the harmonic forms are exactly the bi-invariant forms, computed from the Lie algebra cohomology $H^*(\mathfrak{g})$. So $h^k(G) = \dim H^k(\mathfrak{g}; \mathbb{R})$ — a purely algebraic computation. For $G = \mathrm{SU}(2) = S^3$: $H^0 = \mathbb{R}$, $H^3 = \mathbb{R}$, all others zero, so $h^0 = h^3 = 1$ and $h^1 = h^2 = 0$. The Hodge numbers of $S^3$.

**True name:** the Hodge number is the *analytic count* of solutions to an elliptic PDE (harmonicity) on a closed manifold, which by Hodge's theorem equals the *topological count* of independent cohomology classes. The equality "analytic dimension = topological dimension" is the content of the Hodge isomorphism. The refinement on Kähler manifolds is "analytic dimension by bidegree = refined complex-geometric invariant".

A deeper "true name": the Hodge number is the *index of an elliptic operator*. Specifically, $\chi(M) = \sum_k(-1)^k h^k(M)$ is the Euler characteristic, which is the index of $d + \delta : \Omega^{\text{even}} \to \Omega^{\text{odd}}$. The Atiyah–Singer index theorem computes this from local curvature data — Gauss–Bonnet–Chern theorem in the smooth case.

---

# Examples / Corollaries

**Is an instance: Hodge numbers of $S^n$.** $h^0(S^n) = h^n(S^n) = 1$ (constants and volume form are harmonic), $h^k(S^n) = 0$ for $0 < k < n$. So the Hodge diamond (in the real / Riemannian case) is a "binary string" with $1$s at the ends.

**Is an instance: Hodge numbers of $T^n$.** $h^k(T^n) = \binom{n}{k}$, since the harmonic $k$-forms on the flat torus are the constant-coefficient $k$-forms, parametrized by $\binom{n}{k}$ coefficient choices. So $h^0 = 1$, $h^1 = n$, $h^2 = \binom{n}{2}$, etc., summing to $2^n$.

**Is an instance: Hodge diamond of $\mathbb{CP}^m$.** $H^{p,q}(\mathbb{CP}^m) = \mathbb{C}$ if $p = q$, $0$ otherwise. So $h^{p,q} = \delta_{pq}$ — only diagonal entries are nonzero, each equal to $1$. The Hodge diamond is a "diagonal strip" of $1$s. Betti numbers: $b_{2p} = 1$ for $0 \leq p \leq m$, $b_{2p+1} = 0$. Total Betti number $\sum b_k = m + 1$, Euler characteristic $\chi(\mathbb{CP}^m) = m + 1$.

**Is an instance: Hodge diamond of the K3 surface.** K3 is a closed simply-connected complex surface ($m = 2$, real dimension $4$). Its Hodge diamond is
$$\begin{array}{ccccc}
& & 1 & & \\
& 0 & & 0 & \\
1 & & 20 & & 1 \\
& 0 & & 0 & \\
& & 1 & &
\end{array}$$
with $h^{0,0} = h^{2,2} = 1$, $h^{1,0} = h^{0,1} = h^{2,1} = h^{1,2} = 0$, $h^{2,0} = h^{0,2} = 1$, $h^{1,1} = 20$. Total $b_2 = h^{0,2} + h^{1,1} + h^{2,0} = 22$, $b_0 = b_4 = 1$, $b_1 = b_3 = 0$, $\chi = 24$.

**Is an instance: Hodge diamond of a compact Riemann surface of genus $g$.** A Riemann surface $\Sigma_g$ has $m = 1$, so the diamond is
$$\begin{array}{ccc}
& 1 & \\
g & & g \\
& 1 &
\end{array}$$
with $h^{0,0} = h^{1,1} = 1$, $h^{1,0} = h^{0,1} = g$. Total $b_0 = b_2 = 1$, $b_1 = 2g$, $\chi = 2 - 2g$. The $h^{1,0} = g$ counts holomorphic differentials (abelian integrals).

**Is NOT an instance: Hodge symmetry on a non-Kähler complex manifold.** The Hopf surface (a non-Kähler complex surface) has $h^{1,0} = 0$ but $h^{0,1} = 1$, breaking Hodge symmetry. The Kähler condition is essential for the symmetry $h^{p,q} = h^{q,p}$.

**Corollary (Euler characteristic).** $\chi(M) = \sum_k(-1)^k h^k(M)$. On a compact Kähler $m$-manifold (real dimension $2m$), this refines to $\chi(M) = \sum_{p,q}(-1)^{p+q}h^{p,q}$.

**Corollary (Hodge symmetry forces parity).** On a compact Kähler manifold, the Betti number $b_k = \sum_{p+q=k}h^{p,q}$ is even when $k$ is odd. Proof: pair up $h^{p,q}$ with $h^{q,p}$ — they are equal by Hodge symmetry, so the sum $\sum_{p+q=k, p\neq q}h^{p,q}$ is automatically even; when $k$ is odd, $p \neq q$ for every $(p, q)$ with $p + q = k$, so all terms pair up. So $b_1, b_3, b_5, \dots$ are all even on a compact Kähler manifold. **Consequence**: any odd Betti number being odd forces the manifold to be non-Kähler. The Hopf surface has $b_1 = 1$, odd, so it cannot admit a Kähler metric.

**Corollary (Serre duality numerical).** $h^{p,q}(M) = h^{m-p, m-q}(M)$ on a compact complex manifold of dimension $m$ (Kähler or not). The proof is the abstract Serre duality $H^q(X, \Omega^p_X) \cong H^{m-q}(X, \Omega^{m-p}_X)^*$ for a compact complex manifold, applied with the canonical line bundle.

**Calibration check.** If you can verify (i) $h^k(M) = b_k(M)$ on any closed Riemannian manifold (by the Hodge isomorphism), (ii) the refined Hodge numbers $h^{p,q}$ on a Kähler manifold satisfy $h^{p,q} = h^{q,p}$, and (iii) the Hodge diamond of $\mathbb{CP}^m$ has $1$s only on the diagonal, you have understood the notation correctly.

---

# Unlocked by This

> [!tip] Hodge Conjecture *(from Algebraic Geometry)*
> On a complex projective manifold $X$, the cohomology $H^{p,p}(X) \cap H^{2p}(X; \mathbb{Q})$ consists of **rational $(p, p)$-classes**. The **Hodge conjecture** states that every rational $(p, p)$-class is represented by an algebraic cycle of complex codimension $p$ — i.e., is the cohomology class of a $\mathbb{Q}$-linear combination of closed analytic / algebraic subvarieties. This is one of the seven **Millennium Problems** and has been verified for $p = 1$ (Lefschetz $(1, 1)$-theorem) but is open for $p \geq 2$ in general. The conjecture asserts that the analytic Hodge filtration of cohomology matches an underlying algebraic / geometric structure.

> [!tip] Calabi–Yau Manifolds and Mirror Symmetry *(from String Theory and Algebraic Geometry)*
> A compact Kähler manifold $M$ of complex dimension $m$ is **Calabi–Yau** if $h^{1,0} = 0$ and $h^{m,0} = 1$ — equivalently, the canonical bundle is trivial. Calabi–Yau threefolds ($m = 3$) have Hodge diamonds with two independent Hodge numbers ($h^{1,1}$ and $h^{2,1}$), and **mirror symmetry** is the empirical observation that Calabi–Yau threefolds come in mirror pairs with $h^{1,1}(M) = h^{2,1}(M^*)$ and $h^{2,1}(M) = h^{1,1}(M^*)$ — a Hodge-diamond-reflecting duality. The conjectural origin is in **type II string theory** with the two Calabi–Yaus as compactification spaces giving equivalent four-dimensional physics.

> [!tip] Hodge Numbers and the Weil Conjectures *(from Arithmetic Geometry)*
> The Hodge numbers $h^{p,q}$ of a smooth projective variety over $\mathbb{C}$ are linked to the **Weil conjectures** for smooth projective varieties over finite fields $\mathbb{F}_q$. **Deligne's proof** of the Weil conjectures (1974) shows the **Frobenius eigenvalues** on $\ell$-adic cohomology have absolute value $q^{w/2}$ where $w$ is the "weight". For a smooth projective variety, the weight-$w$ part of cohomology is $\bigoplus_{p+q=w}H^{p,q}$, with the weights and Hodge numbers in close correspondence. This is the bridge between complex algebraic geometry (Hodge theory) and arithmetic algebraic geometry (Weil conjectures), one of the deepest connections in 20th-century mathematics.

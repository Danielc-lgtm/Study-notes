---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - The Tangent Space"
  - "Def - Coordinate Tangent Vectors"
  - "Def - Smooth Manifold"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold and $p \in M$. The tangent space $T_{p}M$ consists of derivations of $C^{\infty}(M)$ at $p$, see [[Def - The Tangent Space]] and [[Def - Derivation at a Point]]. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Statement

> **Theorem (Dimension of the Tangent Space).** Let $M$ be a smooth manifold of dimension $n$. For every $p \in M$, the tangent space $T_{p}M$ is a real vector space of dimension $n$.
>
> More precisely, given any chart $(U, \varphi)$ at $p$ with coordinates $x^{1}, \dots, x^{n}$, the $n$ coordinate tangent vectors $\partial/\partial x^{1}|_{p}, \dots, \partial/\partial x^{n}|_{p}$ form a basis of $T_{p}M$. Equivalently, every tangent vector $v \in T_{p}M$ has a unique expansion
> $$v = v^{i}\,\frac{\partial}{\partial x^{i}}\bigg|_{p}, \qquad v^{i} = v(x^{i}).$$

---

# Motivation

The motivation is to establish that the abstract algebraic definition of $T_{p}M$ — derivations of an infinite-dimensional function algebra — yields a *finite-dimensional* vector space whose dimension matches the dimension of the underlying manifold. This is not obvious from the definition: derivations are operators on $C^{\infty}(M)$, which is infinite-dimensional, and there is no a priori reason their dimension should equal $n$.

The result is critical because every other theorem of differential geometry uses it implicitly. The differential $dF_{p}$ is a linear map between *finite-dimensional* vector spaces; the rank theorem requires $T_{p}M$ to have a definite dimension; the existence of a basis lets one do explicit calculations. Without this theorem, the entire theory would be working with abstract vector spaces of unknown dimension.

The deep reason for the result is that **a derivation at $p$ depends only on the first-order Taylor expansion of its argument at $p$**, and first-order Taylor expansions on an $n$-manifold have $n$ degrees of freedom — one per coordinate. This is what [[Thm - Equivalence of Tangent Vector Definitions]] proves, and the present theorem is the dimension-counting corollary.

---

# Sources and Targets

**Sources (Input Broadening).**

The precondition is "$M$ is an $n$-manifold". This is the standing assumption of differential geometry.

The first source is **a chart at $p$**. Whenever a chart $(U, \varphi)$ is available — and one always is, since manifolds are locally Euclidean — the coordinate basis $\partial/\partial x^{i}|_{p}$ is immediately available, giving an explicit basis. The bridge "$M$ is an $n$-manifold" $\implies$ "every point has a chart" $\implies$ "every tangent space has an $n$-element basis" is one step.

The second source is **an embedding into Euclidean space**. If $M$ embeds in $\mathbb{R}^{N}$ as a submanifold (Whitney embedding shows this is always possible, see [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]]), then $T_{p}M$ is identified with a linear subspace of $T_{p}\mathbb{R}^{N} = \mathbb{R}^{N}$, of dimension $n$. The embedding gives the dimension without explicit charts. Example: $T_{p}S^{2}$ for $p \in S^{2} \subseteq \mathbb{R}^{3}$ is the 2-dimensional subspace orthogonal to $p$.

The third source is **a defining equation $f = c$ with $df_{p}$ surjective**. When $M = f^{-1}(c)$ is a regular level set (see [[Thm - The Regular Value Theorem]]), $T_{p}M = \ker df_{p}$, of dimension $\dim$ codomain $-$ rank $= N - k$ where $f : \mathbb{R}^{N} \to \mathbb{R}^{k}$ has surjective $df_{p}$. This computes dimensions without needing a chart on $M$.

**Targets (Output Amplification).**

The conclusion is "$\dim T_{p}M = n$". Combined with extra structures it amplifies as follows.

Target 1: **combined with the existence of charts and the local-trivialization construction of $TM$, the dimension theorem implies $\dim TM = 2n$**. Each fibre $T_{p}M$ has dimension $n$, the base $M$ has dimension $n$, and the locally-trivial product structure makes $TM$ a $2n$-manifold. See [[Thm - The Tangent Bundle is a Smooth Manifold]].

Target 2: **combined with the chain rule, the dimension theorem implies diffeomorphic manifolds have the same dimension**. If $F : M \to N$ is a diffeomorphism, $dF_{p}$ is a linear isomorphism between $T_{p}M$ and $T_{F(p)}N$ (the chain rule gives both directions), so $\dim T_{p}M = \dim T_{F(p)}N$, i.e., $\dim M = \dim N$. This is the manifold version of "linear isomorphism preserves dimension".

Target 3: **combined with the rank inequality, the dimension theorem bounds the rank of $dF_{p}$**. For $F : M \to N$, the rank of $dF_{p}$ as a linear map $T_{p}M \to T_{F(p)}N$ is at most $\min(\dim M, \dim N) = \min(m, n)$. So the dimension theorem upper-bounds the rank of every differential. This is what makes "full rank" a meaningful condition.

Target 4: **combined with linear-algebra invariants, the dimension theorem gives invariants of $M$**. Every tangent space is an $n$-dimensional vector space, so quantities like "rank of an endomorphism of $T_{p}M$" or "determinant of $dF_{p}$" are well-defined and chart-independent. The Jacobian determinant from multivariate calculus becomes a global geometric invariant.

---

# Why Is It True

The reason can be stated in one sentence: **a derivation at $p$ is determined by its values on the coordinate functions of any chart, and there are $n$ coordinate functions**.

The bolded one-liner mechanism summary: **$T_{p}M$ has dimension $n$ because each tangent vector is uniquely determined by its $n$ components in any chart, and any $n$-tuple of components defines a unique tangent vector**.

Here is the picture. Pick a chart $(U, \varphi)$ at $p$ with coordinate functions $x^{1}, \dots, x^{n}$. For any tangent vector $v \in T_{p}M$, define the $n$ numbers $v^{1}, \dots, v^{n}$ by $v^{i} = v(x^{i})$ — feed $v$ to the $i$-th coordinate function. Two facts:

(a) **The numbers $v^{i}$ determine $v$.** This is the content of [[Thm - Equivalence of Tangent Vector Definitions]]: every derivation at $p$ is a directional derivative in the chart, and the directional derivative is determined by its components $v^{i}$. Concretely, $v(f) = v^{i}\,\partial \hat{f}/\partial x^{i}(\varphi(p))$ for every $f$, by the Taylor-expansion argument.

(b) **Any $n$-tuple $(v^{1}, \dots, v^{n})$ defines a derivation.** Given numbers, the operator $v(f) := v^{i}\,\partial \hat{f}/\partial x^{i}(\varphi(p))$ is linear (sum of linear operators) and satisfies the Leibniz rule (each $\partial/\partial x^{i}|_{\varphi(p)}$ does, and linear combinations preserve Leibniz).

So $T_{p}M \cong \mathbb{R}^{n}$ as vector spaces, via the map $v \mapsto (v(x^{1}), \dots, v(x^{n}))$. The dimension is $n$.

The picture is fundamentally **a chart turns $T_{p}M$ into $\mathbb{R}^{n}$**. Different charts produce different isomorphisms — different identifications of $T_{p}M$ with $\mathbb{R}^{n}$ — but the abstract dimension is chart-independent. The Jacobian-transformation rule (see [[Def - Coordinate Tangent Vectors]]) is precisely the rule for converting between these chart-induced isomorphisms.

---

# What Makes This Hard

The hard step is recognizing that **the chart-induced isomorphism $T_{p}M \to \mathbb{R}^{n}$ is genuinely an isomorphism, not just an injection**. Most people see how the chart components define an injection (a derivation is determined by its values on coordinate functions), but the surjection — that *every* $n$-tuple defines a derivation — is the part that uses [[Thm - Equivalence of Tangent Vector Definitions]] crucially. Without the Taylor-expansion argument from that theorem, one could only conclude $\dim T_{p}M \leq n$. The argument from the other side — that the operator $v(f) = v^{i}\,\partial \hat{f}/\partial x^{i}$ defined by a tuple is a derivation — gives $\dim T_{p}M \geq n$. The match comes from the equivalence theorem.

Another subtlety is **proving the result for points of $\partial M$ (boundary points of a manifold with boundary) requires extra care**. At a boundary point, only one-sided derivatives are allowed, but the tangent space is still $n$-dimensional, not $(n-1)$-dimensional. Lee handles this with Proposition 3.12 and Lemma 3.11 — extending smooth functions on the half-space $\mathbb{H}^{n}$ to the full $\mathbb{R}^{n}$ via the extension lemma for smooth functions. The result is the same: $T_{p}M$ is $n$-dimensional even at boundary points.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Pick a chart at $p$ and transport the problem to $\mathbb{R}^{n}$. On $\mathbb{R}^{n}$, prove that derivations at $a$ are in bijection with $n$-tuples via the components $v^{i} = v(x^{i})$. Combine with the locality property of derivations (a derivation depends only on the germ at $p$) to get the result on $M$.

**Subgoal decomposition:**

1. **Reduce $T_{p}M$ to $T_{p}U$ for any open neighbourhood $U$ of $p$.** By the locality of derivations (see [[Def - Derivation at a Point]]), every derivation at $p$ is determined by its action on functions defined near $p$. Hence the inclusion $\iota : U \hookrightarrow M$ induces an isomorphism $d\iota_{p} : T_{p}U \to T_{p}M$.
   - *Hint:* Bump functions extend smooth functions from $U$ to $M$ without changing values near $p$.
   - *Why needed:* Lets us work in a coordinate chart's domain rather than all of $M$.

2. **Use a chart to identify $T_{p}U$ with $T_{\varphi(p)}\hat{U} \cong T_{\varphi(p)}\mathbb{R}^{n}$.** The chart $\varphi : U \to \hat{U} \subseteq \mathbb{R}^{n}$ is a diffeomorphism, so $d\varphi_{p}$ is an isomorphism $T_{p}U \to T_{\varphi(p)}\hat{U}$. Since $\hat{U}$ is open in $\mathbb{R}^{n}$, $T_{\varphi(p)}\hat{U} = T_{\varphi(p)}\mathbb{R}^{n}$.
   - *Hint:* Same locality argument as Subgoal 1, but now between $\hat{U}$ and $\mathbb{R}^{n}$.
   - *Why needed:* Transports the problem to the local model $\mathbb{R}^{n}$.

3. **Show $T_{a}\mathbb{R}^{n} \cong \mathbb{R}^{n}$ as vector spaces.** Via [[Thm - Equivalence of Tangent Vector Definitions|Lemma 4 of the equivalence theorem]], the map $v \mapsto (v(x^{1}), \dots, v(x^{n}))$ is a vector-space isomorphism.
   - *Hint:* The Taylor-expansion argument gives $v(f) = v^{i}\,\partial f/\partial x^{i}(a)$.
   - *Why needed:* Establishes the dimension on $\mathbb{R}^{n}$.

4. **Combine.** $T_{p}M \cong T_{p}U \cong T_{\varphi(p)}\mathbb{R}^{n} \cong \mathbb{R}^{n}$ via the chain of isomorphisms. The composite isomorphism sends the abstract basis $\partial/\partial x^{i}|_{p}$ to the standard basis $e_{i} \in \mathbb{R}^{n}$.
   - *Hint:* Composition of isomorphisms is an isomorphism.
   - *Why needed:* Completes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: $T_{p}M \cong T_{p}U$ for open $U \subseteq M$ containing $p$
> **Statement:** Let $U \subseteq M$ be an open subset containing $p$, and let $\iota : U \hookrightarrow M$ be the inclusion. Then $d\iota_{p} : T_{p}U \to T_{p}M$ is a vector-space isomorphism.
>
> **Hint:** Use bump functions and the locality property of derivations.
>
> **Why needed:** Lets us pass from the abstract manifold $M$ to a chart's domain $U$, where coordinates are available.
>
> > [!note]- Full proof
> > Injectivity: suppose $v \in T_{p}U$ and $d\iota_{p}(v) = 0$. For any $f \in C^{\infty}(U)$, by the extension lemma there is $\tilde f \in C^{\infty}(M)$ agreeing with $f$ on a neighbourhood of $p$. Then $v(f) = v(\tilde f \circ \iota) = (d\iota_{p}(v))(\tilde f) = 0$. Since this holds for every $f$, $v = 0$.
> >
> > Surjectivity: given $w \in T_{p}M$, define $v \in T_{p}U$ by $v(f) = w(\tilde f)$ for any extension $\tilde f \in C^{\infty}(M)$ of $f$. By the locality property of $w$, $v(f)$ is independent of the extension, so $v$ is well-defined; it is linear and Leibniz by inheritance from $w$. By construction $d\iota_{p}(v) = w$.

> [!note]- Lemma 2: Open submanifold of $\mathbb{R}^{n}$ has tangent space $T_{a}\mathbb{R}^{n} = \mathbb{R}^{n}$
> **Statement:** Let $\hat{U} \subseteq \mathbb{R}^{n}$ be open and $a \in \hat{U}$. Then $T_{a}\hat{U} \cong T_{a}\mathbb{R}^{n}$ canonically, with dimension $n$.
>
> **Hint:** Same locality argument as Lemma 1, with $U = \hat{U}$ and $M = \mathbb{R}^{n}$.
>
> **Why needed:** Identifies the chart-image tangent space with $\mathbb{R}^{n}$.
>
> > [!note]- Full proof
> > Apply Lemma 1 with $M = \mathbb{R}^{n}$ and $U = \hat{U}$. The dimension claim follows from Lemma 3 below.

> [!note]- Lemma 3: $T_{a}\mathbb{R}^{n}$ has dimension $n$
> **Statement:** $T_{a}\mathbb{R}^{n}$ is an $n$-dimensional real vector space, with basis $\partial/\partial x^{1}|_{a}, \dots, \partial/\partial x^{n}|_{a}$. Every $v \in T_{a}\mathbb{R}^{n}$ has a unique expansion $v = v^{i}\,\partial/\partial x^{i}|_{a}$ with $v^{i} = v(x^{i})$.
>
> **Hint:** This is Lemma 4 of [[Thm - Equivalence of Tangent Vector Definitions]] — every derivation at $a$ is a directional derivative.
>
> **Why needed:** Establishes the result on the local model $\mathbb{R}^{n}$.
>
> > [!note]- Full proof
> > See the proof of Lemma 4 in [[Thm - Equivalence of Tangent Vector Definitions]]. The map $v \mapsto (v(x^{1}), \dots, v(x^{n}))$ is a linear bijection $T_{a}\mathbb{R}^{n} \to \mathbb{R}^{n}$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $M$ be a smooth $n$-manifold and $p \in M$. Then $T_{p}M$ is an $n$-dimensional real vector space.
>
> *Proof.* Let $(U, \varphi)$ be a smooth chart at $p$, with $\hat{U} = \varphi(U) \subseteq \mathbb{R}^{n}$.
>
> By Lemma 1, the inclusion $\iota : U \hookrightarrow M$ induces an isomorphism $d\iota_{p} : T_{p}U \to T_{p}M$. So it suffices to compute $\dim T_{p}U$.
>
> By Proposition 3.6(d) of Lee (see [[Thm - Chain Rule for the Differential]]), since $\varphi : U \to \hat{U}$ is a diffeomorphism, $d\varphi_{p} : T_{p}U \to T_{\varphi(p)}\hat{U}$ is an isomorphism. So $\dim T_{p}U = \dim T_{\varphi(p)}\hat{U}$.
>
> By Lemma 2, $T_{\varphi(p)}\hat{U} \cong T_{\varphi(p)}\mathbb{R}^{n}$.
>
> By Lemma 3, $T_{\varphi(p)}\mathbb{R}^{n}$ is $n$-dimensional, with basis the standard partial-derivative operators $\partial/\partial x^{i}|_{\varphi(p)}$.
>
> Combining the chain of isomorphisms,
> $$T_{p}M \;\cong\; T_{p}U \;\cong\; T_{\varphi(p)}\hat{U} \;\cong\; T_{\varphi(p)}\mathbb{R}^{n} \;\cong\; \mathbb{R}^{n}.$$
> The basis $\partial/\partial x^{i}|_{p}$ of $T_{p}M$ corresponds under these isomorphisms to the standard basis $e_{i}$ of $\mathbb{R}^{n}$. Hence $\dim T_{p}M = n$. $\qquad\blacksquare$
>
> The same argument applies at boundary points of manifolds with boundary, with Lemma 3.11 of Lee replacing the open-subset locality step: smooth functions on the half-space $\mathbb{H}^{n}$ extend to smooth functions on $\mathbb{R}^{n}$, and tangent vectors at a boundary point are computed via these extensions, yielding the same dimension $n$.

---

# Cross-Field Exercise Suggestions

**Algebraic geometry — the local ring's cotangent space.** For a smooth affine variety $X$ at a point $p$, the Zariski cotangent space $\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$ has dimension $\dim X$ — the variety is smooth at $p$ iff this equality holds. So the same dimension-counting argument distinguishes smooth from singular points: at a singular point, the cotangent dimension is *strictly larger* than the variety dimension. This is the algebraic-geometric version of the dimension theorem, with smoothness as the regularity condition.

**Functional analysis — tangent space to a Hilbert manifold.** For a smooth submanifold of a Hilbert space, the tangent space at any point is a *closed linear subspace* of the Hilbert space, and the dimension (or codimension) is preserved chart-to-chart. The dimension theorem holds verbatim in infinite-dimensional settings provided one is careful with topology.

**Lie theory — dimension of a Lie group equals dimension of its Lie algebra.** For a Lie group $G$, the Lie algebra $\mathfrak{g} = T_{e}G$ has dimension equal to $\dim G$. The dimension theorem applied at the identity gives this; the left-invariant-vector-field interpretation gives the same dimension globally — the Lie algebra captures the dimension of the group.

---

# Bridges

- **The dimension theorem and the rank theorem are dual.** The dimension theorem fixes the dimensions of the tangent spaces, the rank theorem ($M$, $N$ smooth, $F$ with locally constant rank gives a local normal form) describes what linear maps can occur as differentials between them. Together they classify the local behaviour of smooth maps. See [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

- **The dimension is a manifold invariant via the tangent space.** Diffeomorphisms induce isomorphisms of tangent spaces (by the chain rule), so $\dim T_{p}M$ is a diffeomorphism invariant. Combined with the dimension theorem, $\dim M$ is a diffeomorphism invariant — diffeomorphic manifolds have the same dimension. This is a non-trivial topological consequence of the smooth structure.

- **Local linear algebra of $T_{p}M$ underlies all of differential geometry.** Once the dimension is fixed, every tool of finite-dimensional linear algebra applies pointwise: choice of basis, rank-nullity, dual space, tensor product, determinant. The theory of tensors, forms, and metrics on a manifold is the global assembly of these pointwise linear-algebraic constructions.

- **The Hairy Ball Theorem is a global obstruction beyond the local dimension theorem.** Locally, every tangent space is $n$-dimensional, so locally there are plenty of non-zero tangent vectors. Globally, *assembling* non-zero tangent vectors smoothly into a vector field on $M$ can fail — the obstruction is the Euler class of $TM$, which is non-zero for spheres of even dimension $\geq 2$. The dimension theorem fixes the local picture; the global picture has additional content.

---

# Unlocked by This

> [!tip] The Tangent Bundle is $2n$-Dimensional *(from Differential Geometry)*
> The tangent bundle $TM$ has $\dim TM = 2 \dim M$ — the base contributes $n$, each fibre contributes $n$. See [[Thm - The Tangent Bundle is a Smooth Manifold]].

> [!tip] Rank of a Smooth Map is Bounded *(from Differential Geometry)*
> The rank of $dF_{p}$ is at most $\min(\dim M, \dim N)$ — this is the dimension theorem combined with the standard rank inequality. "Full rank" means achieving this maximum. See [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

> [!tip] Determinant of $dF_{p}$ is Well-Defined when $\dim M = \dim N$ *(from Multivariate Analysis)*
> When $\dim M = \dim N$, $dF_{p}$ is a linear map between vector spaces of the same dimension, and its determinant in any pair of bases is well-defined up to a factor depending on the bases. For the natural coordinate bases, the determinant is the Jacobian determinant from multivariate calculus. See [[Def - Determinant]].

---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Lorentzian Manifold"
  - "Def - Semi-Riemannian Metric and Signature"
  - "Def - Vector Field on a Manifold"
  - "Def - Smooth Manifold"
tags: [geometry, differential-geometry, lorentzian-geometry, topology]
---

# Notation

$M$ — a smooth $n$-manifold. A **Lorentzian metric** on $M$ is a [[Def - Semi-Riemannian Metric and Signature|semi-Riemannian metric]] of signature $(1, n-1)$. A **line field** (or **rank-one distribution**) on $M$ is a smooth rank-one subbundle of $TM$ — a smooth choice of one-dimensional subspace of $T_pM$ at each $p$, varying smoothly. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

---

# Statement

> **Theorem (Obstruction to Lorentzian Metrics).** Not every smooth manifold admits a Lorentzian metric. More precisely:
>
> (i) A smooth manifold $M$ admits a Lorentzian metric if and only if it admits a nowhere-vanishing line field.
>
> (ii) A compact even-dimensional smooth manifold $M$ admits a Lorentzian metric if and only if its Euler characteristic $\chi(M)$ is zero. In particular, the even-dimensional spheres $S^{2k}$ (which have $\chi(S^{2k}) = 2$) admit no Lorentzian metric.

Statement (i) is the line-field characterisation. Statement (ii) is the Euler-characteristic consequence in the compact even-dimensional case (e.g., for surfaces), the most quotable form of the obstruction.

The 2-sphere $S^2$ is the standard example of a smooth manifold admitting no Lorentzian metric, even though it admits a Riemannian metric (the round one).

---

# Motivation

A central result of §12.1 is that *every* smooth manifold admits a Riemannian metric ([[Thm - Existence of Riemannian Metrics via Partitions of Unity]]). The natural follow-up is: does every smooth manifold admit a Lorentzian metric? The construction is similar but the answer is different — Lorentzian existence is obstructed.

The reason the partition-of-unity argument fails is the **non-convexity** of the set of Lorentzian metrics in the space of symmetric $(0, 2)$-tensors. For Riemannian metrics, positive-definiteness is preserved under positive convex combinations; for Lorentzian metrics, the analogous closure property fails — a convex combination of two Lorentzian metrics can become degenerate or change signature. So local Lorentzian metrics cannot always be patched into a global one.

The theorem identifies precisely what makes Lorentzian existence work: the existence of a **nowhere-vanishing line field** on $M$. Given such a line field $L \subseteq TM$, one can construct a Lorentzian metric by taking a Riemannian metric $g_R$ and "flipping the sign" along $L$. Without such a line field, the construction fails — and there are smooth manifolds with no nowhere-vanishing line field, of which the simplest is $S^2$.

The combinatorial significance of the line-field requirement, via the Euler characteristic, gives a clean topological criterion: in the compact even-dimensional case, $\chi(M) = 0$ is necessary and sufficient. This connects the Lorentzian existence question to the topology of $M$ in a quantitative way.

The conceptual upshot: the geometry of relativity is *not* available on every smooth manifold — it requires the manifold to be topologically suitable. The class of manifolds that can be spacetimes is a strict subclass of the class of smooth manifolds.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: Existence of a nowhere-vanishing vector field.* A nowhere-vanishing vector field is in particular a nowhere-vanishing line field (taking the line spanned by the vector at each point). So any manifold with a nowhere-vanishing vector field admits a Lorentzian metric. Examples: odd-dimensional spheres $S^{2k+1}$ have nowhere-vanishing vector fields by the hairy-ball theorem (every odd sphere is parallelisable up to rank, but actually every Lie group has a nowhere-vanishing left-invariant vector field, and odd spheres have a Hopf-style construction), so they all admit Lorentzian metrics. *Trigger:* you have a nowhere-vanishing vector field, conclude existence of a Lorentzian metric.

*Source 2: Existence of a non-vanishing 1-form.* By a similar construction (taking the kernel of the 1-form to get a hyperplane field and the orthogonal complement to get a line field), a manifold with a nowhere-vanishing 1-form admits a Lorentzian metric. This is sometimes the easier criterion to check.

*Source 3: Compact orientable manifold of dimension $\neq 2k$ with even $k$.* For dimension reasons, $\chi(M)$ vanishes automatically for compact orientable manifolds of odd dimension (Poincaré duality). So every compact orientable odd-dimensional manifold admits a Lorentzian metric.

**Targets (Output Amplification)**

*Target combination 1: Lorentzian metric + time orientation gives a globally hyperbolic spacetime (sometimes).* Having a Lorentzian metric is the first step; further refinements (time orientation, causality, global hyperbolicity) require additional topology. A *time-orientable* Lorentzian manifold needs both a Lorentzian metric *and* a continuous choice of "future" timelike direction at each point — this is the data of a nowhere-vanishing timelike vector field, even more restrictive than the line field needed for Lorentzian existence.

*Target combination 2: Non-existence of Lorentzian metric implies a topological constraint.* The theorem can be used in reverse: if you can prove $\chi(M) \neq 0$ (e.g., by counting cells in a CW decomposition or computing Betti numbers), you have proved $M$ admits no Lorentzian metric. This is a *non-existence* result, useful for ruling out certain spacetime models on topologically incompatible manifolds.

*Target combination 3: Comparison with Riemannian existence.* The theorem highlights the contrast between Riemannian (always exists) and Lorentzian (sometimes obstructed), and traces the difference to the convexity of positive-definite forms (Riemannian) vs. the non-convexity of indefinite forms (Lorentzian). This is the deepest conceptual content: the existence question is a *convexity-of-pointwise-data* question.

---

# Why Is It True

**Mechanism summary:** **a Lorentzian metric picks out, at each point, a one-dimensional "timelike" [[Def - Subspace|subspace]] of $T_pM$ — and a smoothly varying choice of one-dimensional [[Def - Subspace|subspace]] globally is exactly a nowhere-vanishing line field. The Euler characteristic is the obstruction to such a field (for compact even-dimensional manifolds), via the Hopf–Poincaré index theorem for line fields.**

The argument has two halves.

**Sufficiency (line field $\Rightarrow$ Lorentzian metric):** Given a Riemannian metric $g_R$ on $M$ (which always exists) and a nowhere-vanishing line field $L \subseteq TM$, construct a Lorentzian metric by the formula
$$
g_L = g_R - 2\, \frac{g_R(\cdot, L) \otimes g_R(\cdot, L)}{g_R(L, L)}.
$$
More carefully: choose a local nowhere-vanishing vector field $X$ generating $L$ (locally), then set $g_L = g_R - 2\, X^\flat \otimes X^\flat / g_R(X, X)$. This formula "flips the sign" of $g_R$ along the line $L$ while keeping it positive-definite on the $g_R$-orthogonal complement. The result is a Lorentzian metric of signature $(1, n-1)$ in our convention (the $L$-direction is timelike, the complement is spacelike). The formula does not depend on the local choice of $X$ generating $L$ (rescaling $X$ does not change the formula), so the construction is well-defined globally given $L$.

**Necessity (Lorentzian metric $\Rightarrow$ line field):** Given a Lorentzian metric $g$ on $M$, the set of timelike vectors at each point $T_pM$ is an open cone (two-component for time-orientable case, otherwise still two components locally, glued in a globally-twisted way). One can extract a line field by, e.g., taking the $g$-eigenspace for the positive eigenvalue (if one diagonalises $g_p$ with respect to a chosen reference Riemannian metric); this gives a line field at each $p$. Smoothness of the line field follows from smoothness of $g$.

**The Euler-characteristic obstruction:** For a compact even-dimensional smooth manifold $M$, the existence of a nowhere-vanishing line field is equivalent to $\chi(M) = 0$. The non-trivial direction ("$\chi(M) \neq 0$ implies no nowhere-vanishing line field") is a generalisation of the **Hopf–Poincaré theorem** (sometimes attributed to Markus): for line fields, the sum of local indices around the zero set equals $\chi(M)$, so if $\chi(M) \neq 0$, every line field must have a zero. For the 2-sphere $S^2$, $\chi(S^2) = 2 \neq 0$, so no nowhere-vanishing line field exists.

(The line-field statement is slightly weaker than the vector-field hairy ball theorem: a line field need not be coherent in direction. But on $S^2$ specifically, both fail.)

---

# What Makes This Hard

The conceptual obstruction is **understanding why the partition-of-unity argument fails**. Students often try to imitate the Riemannian existence proof: cover by charts, install a flat Lorentzian metric on each chart, glue with a partition of unity. The argument breaks at the gluing step: a convex combination of two Lorentzian metrics need not be Lorentzian (it can be degenerate or change signature). The reason the Riemannian argument works is that positive-definite forms are *convex closed* — convex combinations stay positive-definite — and the reason the Lorentzian argument fails is that Lorentzian forms are *not* convex closed.

The non-obvious step is recognising convexity as the key property; once you have, the obstruction makes sense, and the line-field characterisation becomes natural.

The other hard part is **the Euler-characteristic computation**: for $\chi(M) \neq 0$, no nowhere-vanishing vector field exists by Hopf–Poincaré, but the line-field version requires a slightly different argument (line fields can change sign, vector fields cannot). The result is the same up to a factor of 2 in the indices, but the proof requires care.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Sufficiency: given a line field, construct a Lorentzian metric by "flipping the sign of a Riemannian metric along the line field". Necessity: given a Lorentzian metric, extract a line field as the "timelike direction" at each point. The Euler-characteristic obstruction then follows from the Hopf–Poincaré index theorem.

**Subgoal decomposition:**

1. **Existence of a Riemannian metric $g_R$ on $M$.** Use [[Thm - Existence of Riemannian Metrics via Partitions of Unity]].
   - *Hint:* Free from the existence theorem.
   - *Why needed:* Provides the "reference" inner product structure.

2. **From line field $L$ to local generating vector field $X$.** $L$ is a smooth rank-one [[Def - Subbundle|subbundle]]; locally choose a unit (in $g_R$) generator.
   - *Hint:* $L$ being smooth means locally trivial; pick a nowhere-vanishing section.
   - *Why needed:* The Lorentzian metric formula uses a local generator.

3. **Define $g_L = g_R - 2\, X^\flat \otimes X^\flat / g_R(X, X)$ in a neighborhood.** Verify this is Lorentzian: smooth, symmetric, signature $(1, n-1)$.
   - *Hint:* At each $p$, the formula gives $g_L = g_R$ on the $g_R$-orthogonal complement of $X$, and $g_L(X, X) = -g_R(X, X)$. So in a basis of $X$ and an orthonormal complement, the matrix is $\mathrm{diag}(-g_R(X, X), 1, \ldots, 1)$ — *up to a sign convention*. With Lee's convention, multiply by $-1$ to get signature $(1, n-1)$.
   - *Why needed:* The actual construction of the Lorentzian metric.

4. **Verify globality.** The formula is well-defined globally, depending only on $L$ (not on the local choice of $X$).
   - *Hint:* Rescaling $X \to \lambda X$ for $\lambda \neq 0$ leaves the formula invariant: $X^\flat \otimes X^\flat / g_R(X, X) = (X^\flat \otimes X^\flat)/g_R(X, X)$ is invariant under $X \to \lambda X$.
   - *Why needed:* Local construction $\Rightarrow$ global construction.

5. **Conversely: Lorentzian metric $\Rightarrow$ line field.** Extract a line field as the timelike direction at each point.
   - *Hint:* Pick a Riemannian metric $g_R$ on $M$; diagonalise $g$ relative to $g_R$ at each point. There is a unique positive eigenvalue (signature $(1, n-1)$); its eigenline gives the line field.
   - *Why needed:* The "necessity" direction of the characterisation.

6. **The Euler-characteristic obstruction.** For compact even-dim $M$, no nowhere-vanishing line field exists if $\chi(M) \neq 0$, by Hopf–Poincaré.
   - *Hint:* The Hopf–Poincaré theorem expresses $\chi(M)$ as the sum of indices of zeros of any line field. Nowhere-vanishing means zero indices, hence $\chi(M) = 0$.
   - *Why needed:* The topological statement of the theorem.

7. **Concrete example: $S^2$.** $\chi(S^2) = 2 \neq 0$, so no Lorentzian metric exists.
   - *Hint:* Direct application of step 6.
   - *Why needed:* The canonical counterexample.

---

# Lemma Decomposition

> [!note]- Lemma 1: From line field $L$ and Riemannian $g_R$ to Lorentzian metric
> **Statement:** Let $g_R$ be a Riemannian metric on $M$ and $L \subseteq TM$ a smooth rank-one [[Def - Subbundle|subbundle]] (line field). Define a $(0, 2)$-tensor field $g_L$ as follows: for each $p \in M$, choose a generator $X_p$ of $L_p$ (locally, a smooth nowhere-vanishing section $X$ of $L$), and set
> $$
> g_L = g_R - 2\, \frac{X^\flat \otimes X^\flat}{g_R(X, X)},
> $$
> where $X^\flat = g_R(X, \cdot)$. Then $g_L$ is well-defined globally (independent of the choice of generator), smooth, symmetric, and of constant signature $(n-1, 1)$. Negating $g_L$ gives a Lorentzian metric of signature $(1, n-1)$.
>
> **Hint:** Pointwise, decompose $T_pM = L_p \oplus L_p^\perp$ (orthogonal complement under $g_R$). On $L_p^\perp$, $g_L = g_R$, which is positive-definite. On $L_p$, $g_L(X, X) = g_R(X, X) - 2 g_R(X, X) = -g_R(X, X)$, so $g_L$ is negative-definite on $L_p$. The signature is $(n - 1, 1)$.
>
> **Why needed:** The constructive direction of the line-field $\Rightarrow$ Lorentzian metric implication.
>
> > [!note]- Full proof
> > **Well-definedness.** If $X' = \lambda X$ for a smooth nowhere-zero function $\lambda$, then $X'^\flat = \lambda X^\flat$ and $g_R(X', X') = \lambda^2 g_R(X, X)$. The formula gives
> > $$
> > X'^\flat \otimes X'^\flat / g_R(X', X') = \lambda^2 X^\flat \otimes X^\flat / (\lambda^2 g_R(X, X)) = X^\flat \otimes X^\flat / g_R(X, X),
> > $$
> > so the formula is independent of the choice of generator $X$. Hence $g_L$ is defined globally by the line field $L$, not by any particular choice of $X$.
> >
> > **Smoothness.** Locally, $X$, $g_R$, $X^\flat$, and $g_R(X, X)$ are all smooth (with $g_R(X, X)$ nowhere zero), so the formula for $g_L$ is smooth.
> >
> > **Symmetry.** $g_R$ is symmetric and $X^\flat \otimes X^\flat$ is a symmetric $(0, 2)$-tensor (since it equals its transpose); their combination is symmetric.
> >
> > **Signature.** Pointwise at $p$, choose a $g_R$-orthonormal basis $(e_1, \ldots, e_n)$ of $T_pM$ with $e_1 = X / |X|_{g_R}$ (so $e_1 \in L_p$). Then $g_R = \mathrm{diag}(1, 1, \ldots, 1)$ in this basis. For $X = e_1 \sqrt{g_R(X, X)}$, $X^\flat$ acts as $\sqrt{g_R(X, X)}\, dx^1$ in the dual basis, so $X^\flat \otimes X^\flat / g_R(X, X) = dx^1 \otimes dx^1$. Hence
> > $$
> > g_L = \mathrm{diag}(1, 1, \ldots, 1) - 2\, \mathrm{diag}(1, 0, \ldots, 0) = \mathrm{diag}(-1, 1, \ldots, 1).
> > $$
> > Signature: one negative entry, $n - 1$ positive entries — signature $(n-1, 1)$. Negating $g_L$ flips the signature to $(1, n-1)$, which is the Lorentzian convention in Lee's mostly-minus convention. So $-g_L$ is a Lorentzian metric, or alternatively $g_L$ itself is Lorentzian in the "mostly plus" convention.

> [!note]- Lemma 2: From Lorentzian metric to line field
> **Statement:** If $(M, g)$ is a Lorentzian manifold, then $M$ admits a smooth nowhere-vanishing line field.
>
> **Hint:** Pick any Riemannian metric $g_R$ on $M$ (exists by [[Thm - Existence of Riemannian Metrics via Partitions of Unity]]). At each point, diagonalise $g$ with respect to $g_R$ (i.e., find a $g_R$-orthonormal basis in which $g$ is also diagonal). The eigenvalues are continuous in $p$ and cannot pass through zero (non-degeneracy), so the eigenspace of the unique positive eigenvalue (signature $(1, n-1)$) is a smooth line field.
>
> **Why needed:** The necessity direction.
>
> > [!note]- Full proof (sketch)
> > Let $g_R$ be a Riemannian metric on $M$. At each $p \in M$, view $g_p$ as a symmetric bilinear form on $T_pM$; diagonalising it with respect to $g_R$ gives a $g_R$-orthonormal basis $(e_1, \ldots, e_n)$ with $g(e_i, e_j) = \lambda_i \delta_{ij}$ for eigenvalues $\lambda_i$. The signature $(1, n-1)$ assumption means exactly one $\lambda_i > 0$ (with the others negative).
> >
> > The eigenline spanned by the positive-eigenvalue eigenvector is a one-dimensional subspace of $T_pM$. By smoothness of $g$ and continuity of eigenvalues and eigenvectors (in the regions where they are simple and isolated, which is the case here since the positive eigenvalue is unique), this line varies smoothly with $p$, giving a smooth line field on $M$.

> [!note]- Lemma 3: The Hopf–Poincaré index theorem for line fields
> **Statement:** Let $M$ be a compact smooth manifold of [[Def - Dimension|dimension]] $n$, and let $L$ be a smooth line field on $M$ with isolated zeros (where $L_p$ is not well-defined or is the zero subspace). Then the sum of the indices of the zeros equals $\chi(M)$ for even $n$, and equals $0$ for odd $n$.
>
> **Hint:** This is a generalisation of the Hopf index theorem for vector fields; the proof uses a double cover where the line field lifts to a vector field, and the index counts double.
>
> **Why needed:** This is the topological obstruction underlying the Euler-characteristic statement.
>
> > [!note]- Full proof (sketch)
> > The line bundle of orientations of $L$ is a $\mathbb{Z}/2$-cover of the complement of the zero set. On the (oriented) double cover, the line field becomes an oriented line field, hence a vector field up to choice of orientation. The Hopf index theorem applies to this vector field, expressing $\chi(\tilde M)$ as the sum of indices. Descending to $M$, one obtains the line-field version. (Details: see Markus's theorem in differential topology.)
> >
> > For odd $n$: $\chi(M) = 0$ for any compact $n$-manifold (Poincaré duality), so the Hopf–Poincaré sum is also zero. Even-dimensional case is the non-trivial one.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a smooth $n$-manifold.
>
> **Step 0 — well-posedness.** Take $M$ Hausdorff, second-countable; this provides smooth partitions of unity and Riemannian metrics by [[Thm - Existence of Riemannian Metrics via Partitions of Unity]].
>
> **Step 1 (Sufficiency).** Suppose $M$ admits a nowhere-vanishing line field $L \subseteq TM$. By Lemma 1, taking any Riemannian metric $g_R$ on $M$, the formula $g_L = g_R - 2X^\flat \otimes X^\flat / g_R(X, X)$ (with $X$ any local generator of $L$) defines a smooth, symmetric $(0, 2)$-tensor field on $M$ with constant signature $(n-1, 1)$. Negating gives a Lorentzian metric in the $(1, n-1)$ convention.
>
> **Step 2 (Necessity).** Conversely, if $(M, g)$ is Lorentzian, by Lemma 2 there exists a smooth nowhere-vanishing line field on $M$ (the eigenline of the positive eigenvalue of $g$ relative to a Riemannian reference metric).
>
> **Step 3 (Euler-characteristic obstruction).** Suppose $M$ is compact and even-dimensional. By Lemma 3, any line field on $M$ has total index $\chi(M)$ at its zeros. A nowhere-vanishing line field has no zeros, hence total index zero, hence $\chi(M) = 0$. So $M$ admits a nowhere-vanishing line field iff $\chi(M) = 0$ — and by Steps 1 and 2, iff $M$ admits a Lorentzian metric.
>
> **Step 4 (Application to $S^{2k}$).** The Euler characteristic of the $2k$-sphere is $\chi(S^{2k}) = 2$, so by Step 3, $S^{2k}$ admits no Lorentzian metric. In particular $S^2$ — the simplest non-trivial smooth manifold beyond Euclidean space — does not. $\blacksquare$

---

# Cross-Field Exercise Suggestions

*1. Time-orientability is a stronger condition.* Even when a Lorentzian metric exists, the manifold may not be **time-orientable**: requiring a continuous global choice of "future" timelike direction is the existence of a nowhere-vanishing timelike *vector* field (not just line field), which is generally more restrictive. The Möbius-strip-like Lorentzian manifold $M = (\mathbb{R} \times \mathbb{R}) / ((t, x) \sim (-t, x + 1))$ admits a Lorentzian metric but is not time-orientable.

*2. The Lorentzian existence question for compact Lie [[Def - Group|groups]].* Every compact Lie [[Def - Group|group]] $G$ has $\chi(G) = 0$ (a consequence of having a nowhere-vanishing left-invariant vector field, e.g.). So every compact Lie group admits a Lorentzian metric. Combined with other geometric structures (bi-invariance), this gives interesting examples of Lorentzian-symmetric homogeneous spaces.

*3. Application: torus admits a Lorentzian metric.* The 2-torus $T^2$ has $\chi(T^2) = 0$, so it admits a Lorentzian metric. Explicitly: the quotient of Minkowski $(\mathbb{R}^2, dt^2 - dx^2)$ by an integer lattice $\Lambda = \mathbb{Z}(1, 0) + \mathbb{Z}(0, 1)$ gives a Lorentzian 2-torus. This is a toy spacetime with closed timelike curves, often used as an illustrative example in causality theory.

*4. Cosmological topologies.* In cosmology, the underlying spatial manifold $\Sigma$ in an FRW spacetime $\mathbb{R} \times \Sigma$ can be any 3-manifold; the full spacetime $M = \mathbb{R} \times \Sigma$ has $\chi(M) = \chi(\mathbb{R}) \chi(\Sigma) = 0$ (since $\chi(\mathbb{R}) = 0$ on the non-compact factor and the product formula). So all FRW cosmologies are automatically compatible with Lorentzian existence.

---

# Bridges

- **[[Thm - Existence of Riemannian Metrics via Partitions of Unity]]** — the contrasting "Riemannian always works" theorem. The contrast traces to convexity: positive-definite forms are pointwise convex, indefinite forms are not. Comparing the two theorems clarifies what is special about Riemannian existence.

- **Hopf index theorem / Hopf–Poincaré theorem.** The Hopf theorem for vector fields says: on a compact smooth manifold, the sum of indices of any vector field with isolated zeros equals $\chi(M)$. The line-field version (Markus's theorem) is the analogous statement for line fields. Both feed into this theorem's obstruction.

- **Hairy ball theorem.** The classical statement: every continuous vector field on $S^{2k}$ has a zero. Equivalently, $S^{2k}$ has no nowhere-vanishing vector field. The corollary for line fields is the same for $S^2$ (no nowhere-vanishing line field), giving the canonical counterexample to Lorentzian existence on $S^2$.

- **Euler characteristic.** $\chi(M) = \sum_k (-1)^k b_k(M)$ where $b_k$ are the Betti numbers, or alternatively $\chi(M)$ is the alternating sum of cells in a CW decomposition. For closed orientable surfaces $\Sigma_g$, $\chi(\Sigma_g) = 2 - 2g$, so genus-$g$ surfaces admit Lorentzian metrics iff $g \geq 1$ — i.e., all closed orientable surfaces except the sphere admit a Lorentzian metric.

---

# Unlocked by This

> [!tip] Spacetime Topology *(from Mathematical General Relativity)*
> The Lorentzian existence question is the first chapter of **spacetime topology**: which smooth manifolds can serve as spacetimes in general relativity? Further questions include time-orientability, causal structure, achronality, global hyperbolicity, the Geroch–Bernal–Sánchez theorem (globally hyperbolic spacetimes are diffeomorphic to $\mathbb{R} \times \Sigma$). The interplay between topology and Lorentzian geometry is the subject of mathematical general relativity, on which the singularity theorems of Penrose and Hawking depend essentially.

> [!tip] Foliations and Codimension-One Foliations *(from Foliation Theory)*
> A nowhere-vanishing line field is the simplest example of a **distribution** (rank-one); a related concept is a codimension-one distribution. The existence of *integrable* line fields (foliations by curves) is even more restrictive — and the Frobenius theorem ([[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]]) gives the integrability criterion. Lorentzian existence is "rank-one distribution existence", and the broader theory of distributions and foliations sits one level up.

> [!tip] Obstruction-Theoretic Methods *(from Algebraic Topology)*
> The Euler-characteristic obstruction is part of a broader **obstruction theory**: characteristic classes of the tangent bundle of $M$ obstruct various geometric structures. The Euler class $e(TM)$ obstructs nowhere-vanishing sections; the Stiefel–Whitney classes obstruct orientability; the Pontryagin classes obstruct certain geometric structures via index theorems. The Lorentzian existence question is one entry point into this larger obstruction-theoretic framework.

> [!tip] Local Lorentzian Existence Always Works *(from Differential Geometry)*
> Even though Lorentzian metrics may fail to exist globally, locally they always do: every smooth manifold has Lorentzian metrics defined on each chart (just take the constant Minkowski form in the chart coordinates), and the obstruction is purely global. This is a typical pattern in differential geometry: local existence is easy, global existence is obstructed by topology, and the obstruction is characteristic-class-valued.

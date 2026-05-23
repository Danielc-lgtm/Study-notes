---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - The Tangent Space"
  - "Def - The Differential of a Smooth Map"
  - "Def - Embedded Submanifold"
  - "Def - Immersed Submanifold"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold; $S \subseteq M$ is an embedded or immersed submanifold; $\iota : S \hookrightarrow M$ is the inclusion. For $p \in S$, $T_p S$ is the tangent space of $S$ at $p$ in the intrinsic sense ([[Def - The Tangent Space]]), and $T_p M$ is the tangent space of the ambient manifold. The differential $d\iota_p : T_p S \to T_p M$ is the linear map at the tangent level. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

A **curve through $p$ in $S$** is a smooth map $\gamma : J \to M$ defined on an open interval $J \ni 0$, with $\gamma(0) = p$, whose image lies entirely in $S$ and which is smooth as a map *into $S$* (in $S$'s topology and smooth structure).

---

# Axiom Motivation

A submanifold $S \subseteq M$ is itself a smooth manifold, so by the standard machinery of [[Differential Geometry III — Tangent Vectors and the Differential|DG III]] it already has a tangent space $T_p S$ at every $p$. The question this page answers is: *how does $T_p S$ sit inside $T_p M$?* That is, what is the relationship between the intrinsic tangent space of the submanifold and the ambient tangent space?

The natural answer is via the inclusion. Since $\iota : S \hookrightarrow M$ is a smooth immersion (this is the very definition of submanifold), its differential $d\iota_p : T_p S \to T_p M$ is an injective linear map between tangent spaces. So $T_p S$ embeds canonically into $T_p M$ via $d\iota_p$, and we **identify $T_p S$ with its image $d\iota_p(T_p S) \subseteq T_p M$**.

This identification is universally adopted in differential geometry. Without it, statements like "the tangent space of the sphere at $p$ is $\{v : v \cdot p = 0\}$" would be ambiguous — is it the intrinsic tangent space of $S^n$ as a $2$-dimensional manifold, or a [[Def - Subspace|subspace]] of $T_p\mathbb{R}^3$? The convention is that it is both, identified by $d\iota_p$. The conventions matches what one would compute: a velocity vector of a curve in $S$ is naturally a vector in $T_p M$ (since the curve lies in $M$), and it is also a vector in $T_p S$ (since the curve lies in $S$); the two views are related by $d\iota_p$, which by injectivity *identifies* the tangent vector as living in both spaces.

**Why does this work in the embedded case but require care in the immersed case?** When $S$ is embedded, the subspace topology and the intrinsic topology coincide, so curves smooth "into $M$" are the same as curves smooth "into $S$" (Corollary 5.30 of Lee). The identification is automatic. When $S$ is merely immersed (figure-eight, dense torus line), one needs to demand that the curve be smooth as a map *into $S$* — not just into $M$. This is a real distinction: the map $G : \mathbb{R} \to \mathbb{R}^2$, $G(t) = (\sin 2t, \sin t)$, with domain extended to all of $\mathbb{R}$ (not just $(-\pi, \pi)$), has image in the figure-eight, but it is *not* smooth (not even continuous) as a map into the figure-eight with its immersed-submanifold topology. So "curves in $S$" must mean "smooth as maps into $S$" for the curve characterisation to work.

The three equivalent descriptions of $T_p S$ that we will give all reduce to the same subspace of $T_p M$, but each has a different computational sweet spot:
1. **Image of $d\iota_p$** — the cleanest definition, but rarely usable for computation since one rarely has an explicit description of "the intrinsic tangent space of $S$" except via this identification anyway.
2. **Velocities of curves in $S$** — the most flexible. Almost every actual tangent-space computation for matrix Lie [[Def - Group|groups]] (e.g. $T_I \mathrm{O}(n)$) uses this: write a smooth one-parameter family of group elements and differentiate.
3. **Kernel of the differential of a defining map / image of the differential of a parametrising map** — the most efficient when applicable. For a regular level set $\Phi^{-1}(c)$, $T_p S = \ker d\Phi_p$. For the image of an embedding $F : N \to M$, $T_p S = \mathrm{im}\, dF_q$ where $F(q) = p$.

All three are equivalent for embedded submanifolds; for immersed submanifolds the curve characterisation must use curves smooth into $S$.

---

# The Definition

Let $S$ be an embedded or immersed submanifold of $M$, and let $p \in S$.

**Tangent space of a submanifold (primary definition).** The **tangent space** of $S$ at $p$, written $T_p S$, is the intrinsic tangent space of $S$ as a smooth manifold ([[Def - The Tangent Space]]), identified with its image in $T_p M$ via the differential of the inclusion:
$$T_p S \;\hookrightarrow\; T_p M, \qquad v \;\mapsto\; d\iota_p(v).$$
With this identification, $T_p S$ is a $k$-dimensional linear subspace of $T_p M$, where $k = \dim S$.

**Curves characterisation.** A vector $v \in T_p M$ is in $T_p S$ if and only if there exists a smooth curve $\gamma : J \to M$ on an open interval $J \ni 0$ such that:
- $\gamma(0) = p$;
- the image of $\gamma$ lies entirely in $S$;
- $\gamma$ is smooth as a map into $S$ (with $S$'s topology and smooth structure);
- $\gamma'(0) = v$.

For embedded submanifolds, "smooth as a map into $S$" is automatic from "smooth as a map into $M$ with image in $S$" (Corollary 5.30 of Lee), so the third condition is redundant. For immersed submanifolds, it is essential.

**Kernel characterisation (level-set case).** If $\Phi : M \to N$ is a smooth submersion (or more generally has constant rank on a neighbourhood of $\Phi^{-1}(c)$) and $S = \Phi^{-1}(c)$ is a regular level set, then for every $p \in S$,
$$T_p S = \ker d\Phi_p \;\subseteq\; T_p M.$$

**Image characterisation (parametric case).** If $F : N \to M$ is a smooth embedding and $S = F(N)$, then for every $p \in S$ with $F(q) = p$,
$$T_p S = \mathrm{im}\, dF_q \;\subseteq\; T_p M.$$

**[[Def - Annihilator|Annihilator]] characterisation (embedded case).** If $S$ is embedded, then $v \in T_p S$ if and only if $v(f) = 0$ for every smooth function $f \in C^\infty(M)$ that vanishes on $S$.

---

# Categorical / Structural Definition

The tangent space of a submanifold is structurally defined by the **universal property of the inclusion functor** $\iota_* : T S \to T M$ between tangent bundles: it is the unique subspace $T_p S \subseteq T_p M$ such that the inclusion of $T_p S$ into $T_p M$ is precisely the differential of the inclusion $\iota$ on tangent vectors.

The categorical content: the inclusion $\iota : S \hookrightarrow M$ is a smooth immersion, and the tangent functor $T$ from smooth manifolds to vector bundles sends immersions to fibrewise-injective vector bundle maps. So the tangent bundle of $S$ embeds as a sub-bundle of the restricted tangent bundle of $M$ to $S$:
$$TS \;\hookrightarrow\; TM|_S = \bigsqcup_{p \in S} T_p M.$$
The fibre over $p$ of this sub-bundle is precisely $T_p S$.

---

# Relate to Other Fields / Compression

The tangent space of a submanifold is the **manifold-level upgrade of the [[Def - The Tangent Space to a Submanifold|tangent space to a submanifold of ℝⁿ]]** from [[Multivariate Analysis II — Inverse and Implicit Function Theorems|MA II]]. There, the tangent space to $S \subseteq \mathbb{R}^n$ is defined as the set of velocities $\gamma'(0)$ of $C^1$ curves $\gamma$ in $S$ through $p$, which is also a $d$-dimensional linear subspace of $T_p \mathbb{R}^n \cong \mathbb{R}^n$ (where $d = \dim S$). The manifold-level definition coincides with this when $M = \mathbb{R}^n$.

For **regular level sets**, the kernel characterisation $T_p S = \ker d\Phi_p$ generalises the Euclidean result $T_p S = \ker D\Phi_p$ from [[Thm - The Regular Value Theorem|MA II's regular value theorem]]. The reasoning is identical: any curve $\gamma$ in $S$ satisfies $\Phi(\gamma(t)) = c$ (constant), so differentiating gives $d\Phi_p(\gamma'(0)) = 0$; thus $T_p S \subseteq \ker d\Phi_p$. The reverse inclusion is by dimension count: $\dim \ker d\Phi_p = \dim M - \dim N$ (rank-nullity, since $d\Phi_p$ is surjective) $= \dim S$ (by the regular value theorem).

**True name:** the **true name** of "tangent space of a submanifold" is **"the directions in $T_p M$ along which one can move and stay in $S$ to first order"** — equivalently, the set of velocity vectors at $p$ of smooth curves that lie entirely in $S$. The "image of inclusion's differential" definition is logically primary; the curve characterisation is the operational meaning.

When $S$ is a regular level set $\Phi^{-1}(c)$, the **true name** sharpens to **"the directions in which $\Phi$ does not change to first order"** — exactly the kernel of $d\Phi_p$. This is the most computationally direct characterisation.

---

# Examples / Corollaries

**Example — tangent space of the sphere.** For $S^n = \{x \in \mathbb{R}^{n+1} : |x|^2 = 1\}$ defined by $\Phi(x) = |x|^2 - 1$, the differential at $p$ is $d\Phi_p(v) = 2 p \cdot v$. So
$$T_p S^n = \ker d\Phi_p = \{v \in \mathbb{R}^{n+1} : p \cdot v = 0\}$$
— the orthogonal complement of $p$. See [[Ex - The Sphere as a Level Set]] for the full derivation.

**Example — tangent space at the identity of $\mathrm{SL}(n, \mathbb{R})$.** For $\mathrm{SL}(n) = \det^{-1}(1)$, the differential of $\det$ at $I$ is $d\det_I(X) = \mathrm{tr}(X)$ (using Jacobi's formula). So
$$T_I \mathrm{SL}(n,\mathbb{R}) = \ker d\det_I = \{X \in \mathrm{Mat}_n(\mathbb{R}) : \mathrm{tr}\, X = 0\} = \mathfrak{sl}(n,\mathbb{R}).$$
This is the **Lie algebra** of $\mathrm{SL}(n,\mathbb{R})$, the space of trace-zero matrices. See [[Ex - The Special Linear Group is a Submanifold of GL(n)|Ex - The Special Linear Group is a Submanifold of GL(n)]].

**Example — tangent space at the identity of $\mathrm{O}(n)$.** For $\mathrm{O}(n) = \{A : A^T A = I\}$, viewed as a level set of $\Phi(A) = A^T A$ valued in symmetric matrices, the differential at $I$ is $d\Phi_I(X) = X + X^T$. So
$$T_I \mathrm{O}(n) = \ker d\Phi_I = \{X \in \mathrm{Mat}_n : X + X^T = 0\} = \mathfrak{o}(n)$$
— the antisymmetric matrices. See [[Ex - The Orthogonal Group as a Regular Level Set]].

**Example — tangent space via curves: $T_I \mathrm{O}(n)$ revisited.** A curve $A : (-\varepsilon, \varepsilon) \to \mathrm{O}(n)$ with $A(0) = I$ satisfies $A(t)^T A(t) = I$ for all $t$. Differentiating at $t = 0$: $A'(0)^T + A'(0) = 0$, so $A'(0)$ is antisymmetric. By [[Def - Dimension|dimension]] count, every antisymmetric matrix arises this way (e.g., from $A(t) = e^{tX}$ for $X$ antisymmetric). So $T_I \mathrm{O}(n) = \mathfrak{o}(n)$, matching the kernel characterisation. This curve-based derivation is the workhorse for matrix Lie groups.

**Example — tangent space of a graph.** For $g : V \to \mathbb{R}^k$ smooth and $\Gamma = \{(x, g(x)) : x \in V\}$ the graph, the tangent space at $(x, g(x))$ is the image of $dG_x = \begin{pmatrix} I \\ Dg(x) \end{pmatrix}$, namely $\{(v, Dg(x) v) : v \in \mathbb{R}^d\}$. This is the "graph of the linearisation" — the tangent space of a graph is the graph of the linear approximation.

**Example — embedded vs immersed.** For the figure-eight image set with its immersed-submanifold structure, the tangent space at the crossing point $(0,0)$ is well-defined and one-dimensional (spanned by the velocity of the parametrisation at $t = 0$, which is $(2, 1)$). But in the subspace topology of $\mathbb{R}^2$, the crossing point has *two* "tangent directions" (corresponding to $t \to -\pi$ and $t \to \pi$ approaches), and there is no consistent tangent space. The immersed-submanifold structure picks one of these — the one coming from the chosen parametrisation.

**Is NOT a tangent vector — a vector violating the constraint linearly.** If $S = \{|x|^2 = 1\} \subseteq \mathbb{R}^{n+1}$, then a vector $v \in \mathbb{R}^{n+1}$ with $p \cdot v \neq 0$ is *not* a tangent vector to $S$ at $p$: any curve $\gamma$ in $S$ with $\gamma(0) = p$ satisfies $|\gamma(t)|^2 = 1$, so $\gamma'(0) \cdot p = 0$ by differentiating.

**Corollary — the tangent space of a regular level set.** If $S = \Phi^{-1}(c)$ is a regular level set, then $T_p S = \ker d\Phi_p$ for every $p \in S$. The dimension is $\dim M - \dim N$ by rank-nullity.

**Corollary — pullback under inclusion.** For a smooth function $f \in C^\infty(M)$, its restriction $f|_S$ is smooth on $S$, and $d(f|_S)_p(v) = df_p(d\iota_p(v))$ for all $v \in T_p S$. The differential of the restriction is the restriction of the differential.

**Corollary — sub-bundle of $TM|_S$.** The collection $\{T_p S : p \in S\}$ forms a smooth sub-bundle of $TM|_S$ (the restriction of the tangent bundle of $M$ to $S$). This sub-bundle is precisely $TS$ as a vector bundle over $S$.

**Calibration check.** Verify that the tangent space at the north pole of $S^2 \subseteq \mathbb{R}^3$ is the $xy$-plane $\{(v_1, v_2, 0)\}$. Verify that the tangent space at the identity of the diagonal group $\{(a, a) : a \in \mathbb{R}\} \subseteq \mathbb{R}^2$ (a $1$-dimensional embedded submanifold) is the diagonal $\{(v, v) : v \in \mathbb{R}\} \subseteq \mathbb{R}^2$. Verify that for an embedded submanifold $S \subseteq M$, a vector $v \in T_p M$ is in $T_p S$ if and only if $v(f) = 0$ for every $f \in C^\infty(M)$ vanishing on $S$ (this is Proposition 5.37 of Lee, and it gives a fourth equivalent characterisation in the embedded case).

---

# Unlocked by This

> [!tip] The Normal Space and Normal Bundle *(from Riemannian Geometry)*
> Given a Riemannian metric on $M$, the **normal space** $N_p S$ at $p \in S$ is the orthogonal complement $(T_p S)^\perp$ in $T_p M$. The collection $\{N_p S : p \in S\}$ forms the **normal bundle** $NS$, a smooth vector bundle over $S$ of rank $\dim M - \dim S$. The decomposition $T_p M = T_p S \oplus N_p S$ is the foundation of submanifold geometry: second fundamental forms, Gauss/Codazzi equations, mean curvature.

> [!tip] Lie Algebra of a Lie Group *(from [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie Theory]])*
> For a Lie subgroup $H$ of a Lie group $G$, the tangent space $T_e H$ at the identity (where $e$ is the identity element) is the **Lie algebra** $\mathfrak{h}$ of $H$. It carries a Lie bracket inherited from $G$. The tangent-space computations $T_I \mathrm{SL}(n) = \mathfrak{sl}(n)$ and $T_I \mathrm{O}(n) = \mathfrak{o}(n)$ are the matrix instances of this principle.

> [!tip] Vector Fields Tangent to a Submanifold *(from [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|DG V]])*
> A vector field $X$ on $M$ is **tangent to** $S$ if $X_p \in T_p S$ at every $p \in S$. The flow of such a vector field preserves $S$: integral curves starting in $S$ stay in $S$. This connects directly to integrability and Frobenius's theorem in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]].

> [!tip] Differential Forms on Submanifolds *(from Differential Geometry IX)*
> A differential $k$-form on $M$ restricts (pulls back via $\iota^*$) to a differential $k$-form on $S$. The restriction "forgets the normal components" — only the components in $\Lambda^k T_p S$ survive. This is the setup for integrating forms on submanifolds.

---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Distribution on a Manifold"
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, differential-geometry, frobenius]
---

# Notation

$M$ is a smooth $n$-manifold; $D$ is a smooth distribution of rank $k$ on $M$ — see [[Def - Distribution on a Manifold]]. An **immersed submanifold** $N \hookrightarrow M$ is a smooth manifold $N$ together with a smooth injective immersion $\iota : N \to M$; we identify $N$ with its image. The tangent space $T_pN$ at $p \in N$ is identified with $d\iota_p(T_pN) \subseteq T_pM$. The full notation registry is on [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]].

---

# Axiom Motivation

The desideratum is to define the natural geometric object that "realizes" a distribution: a $k$-dimensional submanifold whose tangent spaces are exactly the planes of the distribution. The point is to make precise the question that the [[Thm - The Frobenius Theorem|Frobenius theorem]] answers.

The phrase "submanifold tangent to $D$" admits two natural strengthenings, each delivering a slightly different notion. The weaker strengthening — "tangent to $D$ at a single point" — is uninteresting; for any rank-$k$ distribution we can always find a small disc tangent to $D$ at one chosen point (just exponentiate the $k$-plane via any Riemannian metric). The stronger strengthening — "tangent to $D$ at *every* point of the submanifold" — is the interesting one. This says that not only does the submanifold *touch* the distribution at one point, but it is *carried along* by the distribution everywhere it exists. The submanifold is "integrated" with respect to the infinitesimal data of the distribution.

We also need to decide *what kind* of submanifold to allow. An *embedded* submanifold would be too restrictive: many natural integral manifolds, particularly in the global theory of [[Def - Foliation|foliations]], are only *immersed* (the line of irrational slope on the torus, for instance, is dense and hence not embedded, but is a perfectly good integral manifold). An *immersed* submanifold — locally an embedding, allowed to self-intersect or be dense globally — is the right notion. So we take immersed, which is the most permissive standard notion that still allows a tangent-space identification.

Why "immersion" rather than just "smooth map with image tangent to $D$"? Because we want the [[Def - Dimension|dimension]] to be honest. An immersion has $d\iota$ injective at every point, so $T_pN$ embeds as a *$k$-dimensional* [[Def - Subspace|subspace]] of $T_{\iota(p)}M$, which is the natural condition for "$T_pN$ equals $D_{\iota(p)}$." Without the immersion condition, $T_pN$ could be lower-dimensional and the equality "$T_pN = D_p$" would have to be replaced by inclusion.

Why "connected"? Lee does not demand connectedness, but the global Frobenius theorem talks about *connected* integral manifolds and their *maximal* extensions; the leaf of a [[Def - Foliation|foliation]] is by definition connected, and the canonical integral manifold through a point is the connected component. Connectedness is more a convention for the leaf-theoretic perspective than a fundamental requirement of the definition.

The choice to require $T_pN = D_p$ rather than $T_pN \subseteq D_p$ is deliberate. Equality means $N$ has the maximum possible [[Def - Dimension|dimension]] consistent with tangency — it is a *full* integral submanifold. Lower-dimensional sub-integrals (curves inside a $2$-dimensional integral surface) are also useful but get a different name, and we want the central definition to capture the maximum-dimension case.

---

# The Definition

Let $M$ be a smooth manifold and $D$ a smooth distribution of rank $k$ on $M$. An **integral manifold** of $D$ is a nonempty immersed submanifold $N \hookrightarrow M$ (typically of dimension $k$, though connected components of arbitrary dimension can also be considered) such that

$$T_pN = D_p \qquad \text{for every } p \in N.$$

In coordinates: an integral manifold of $D$ is a smooth map $\iota : N \to M$ from a $k$-dimensional smooth manifold $N$, injective and with $d\iota_p$ injective at every $p$, such that $d\iota_p(T_pN) = D_{\iota(p)}$ for every $p \in N$.

A distribution $D$ is **integrable** if every point of $M$ lies in some integral manifold of $D$ — see [[Def - Integrable Distribution]].

A **maximal connected integral manifold** of $D$ is a connected integral manifold that is not contained in any strictly larger connected integral manifold; by the global [[Thm - The Frobenius Theorem|Frobenius theorem]], when $D$ is involutive these exist and form a partition of $M$ (a foliation — see [[Def - Foliation]]).

---

# Relate to Other Fields / Compression

**True name:** An integral manifold is *a global realization of the infinitesimal data $D$*. The distribution gives the tangent space at every point; an integral manifold is a $k$-dimensional submanifold that *actually has* those tangent spaces — i.e. it is integrated from $D$. The word "integrated" is deliberate: an integral curve of a vector field has tangent vector equal to the field at every point, and an integral manifold is the higher-dimensional generalization.

**Compression to ODE theory.** A rank-$1$ integral manifold is precisely the image of an integral curve of a spanning vector field; rank-$1$ integral manifolds always exist by [[Thm - Existence and Uniqueness of Integral Curves|the ODE existence-uniqueness theorem]]. The question of higher-rank integral manifolds is then the question "does the analogous theorem hold for $k \geq 2$?" — and the answer is "iff involutivity," provided by [[Thm - The Frobenius Theorem|Frobenius]].

**Compression to PDE.** For an overdetermined PDE system $\partial u/\partial x^i = \alpha^i(x, u)$, the *graph* of any solution $u : \mathbb{R}^n \to \mathbb{R}$ is an integral manifold of the distribution spanned by $\partial_{x^i} + \alpha^i \partial_u$. Conversely, any integral manifold of this distribution that is the graph of a function gives a solution. So integral manifolds are *globally defined solutions* of the PDE.

**Compression to mechanics.** A holonomic constraint defines a submanifold of configuration space — the configurations satisfying the constraint. This submanifold is the integral manifold of the constraint distribution; existence of the submanifold matches existence of integral manifolds matches involutivity matches holonomicity.

---

# Examples / Corollaries

**Is an instance: a level set of a submersion.** If $F : M \to N$ is a smooth submersion and $D_p = \ker dF_p$ (the vertical distribution), then $F^{-1}(q)$ for any regular value $q$ is an integral manifold of $D$ — embedded, of dimension $\dim M - \dim N$, with tangent space exactly $D_p$ at every $p$ in the fiber. Different regular values give different (parallel) integral manifolds, and they partition $M$ into a foliation. This is the "obviously integrable" example, with the integrability built into the submersion structure.

**Is an instance: coordinate slices in $\mathbb{R}^n$.** For the distribution $D = \mathrm{span}(\partial_1, \dots, \partial_k)$ on $\mathbb{R}^n$, each affine [[Def - Subspace|subspace]] $\{x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ is an integral manifold — embedded, $k$-dimensional, with tangent space $\mathrm{span}(\partial_1, \dots, \partial_k) = D$ everywhere. This is the "model" example; Frobenius says every involutive distribution looks like this in suitable local coordinates.

**Is an instance: integral curve of a vector field.** Let $V$ be a nowhere-vanishing smooth vector field on $M$, defining a rank-$1$ distribution $D_p = \mathrm{span}(V_p)$. The image of an [[Def - Integral Curve of a Vector Field|integral curve]] $\gamma : J \to M$ of $V$ is an integral manifold of $D$: $T_{\gamma(t)} \mathrm{Im}(\gamma) = \mathrm{span}(\dot\gamma(t)) = \mathrm{span}(V_{\gamma(t)}) = D_{\gamma(t)}$. The integral manifold is the *image* of the curve as a $1$-dimensional immersed submanifold; the curve itself is the parameterization.

**Is an instance: a leaf of a foliation.** Each leaf of a foliation is a maximal connected integral manifold of the foliation's underlying involutive distribution. The connected sum of integral manifolds through a point (intersecting non-trivially) is itself an integral manifold (Lemma 19.22 in Lee), and the maximal one is the leaf.

**Is an instance: irrational slope on the torus.** On $T^2 = \mathbb{R}^2/\mathbb{Z}^2$, the rank-$1$ distribution spanned by the constant vector field $(1, \alpha)$ (for $\alpha$ irrational) has integral manifolds that are *dense lines* — immersed but not embedded, with each line winding around the torus densely. This is the standard example showing that immersed (not embedded) is the right level of generality.

**Is NOT an instance: a surface tangent to $\ker(dz - y\,dx)$ in $\mathbb{R}^3$.** No integral $2$-manifold exists for this distribution. Suppose $N$ is one; then $N$ contains the $x$-axis (integral curve of $\partial_x + y\partial_z = \partial_x$ when $y = 0$) and contains lines parallel to the $y$-axis (integral curves of $\partial_y$). So $N$ contains the $xy$-plane locally, but the $xy$-plane has tangent space $\mathrm{span}(\partial_x, \partial_y)$, while $D_{(x, y, 0)} = \mathrm{span}(\partial_y, \partial_x + y\partial_z)$. These differ when $y \neq 0$. Contradiction — see Example 19.1(d) in Lee, and [[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]].

**Is NOT an instance: a curve transverse to $D$.** A curve $\gamma$ in $M$ with $\dot\gamma_p \notin D_p$ at some $p$ is not an integral manifold of $D$, even if $\dot\gamma_q \in D_q$ at every other point. The integrality condition is *every* point, not "almost every."

**Corollary (uniqueness of integral manifolds containing a point, locally).** If $N_1$ and $N_2$ are two connected integral manifolds of $D$ both containing $p$, then $N_1$ and $N_2$ agree in a neighborhood of $p$ — they coincide on the connected component of $N_1 \cap N_2$ containing $p$, by Proposition 19.16 in Lee. So the "germ" of an integral manifold at a point is unique when it exists.

**Corollary (the union of overlapping integral manifolds is integral).** Lemma 19.22 in Lee: if $\{N_\alpha\}$ is a family of connected integral manifolds of an involutive distribution $D$ all containing a common point, then their union $\bigcup_\alpha N_\alpha$ has a unique smooth manifold structure making it a connected integral manifold of $D$. This is the key step in the global Frobenius construction of leaves.

**Corollary (weak embeddedness).** Every integral manifold of an involutive distribution is *weakly embedded* in $M$, meaning every smooth map $F : Q \to M$ whose image lies in $N$ is smooth into $N$. This is Theorem 19.17 in Lee, and it is what makes integral manifolds well-behaved despite being only immersed.

**Calibration check.** If you have understood the definition you should be able to (i) verify that the parallel coordinate planes $\{x^{k+1} = c, \dots\}$ are integral manifolds of $\mathrm{span}(\partial_1, \dots, \partial_k)$, (ii) explain why the standard contact distribution on $\mathbb{R}^3$ has *no* integral $2$-manifold, and (iii) name an example where integral manifolds exist but are only immersed (not embedded) — the irrational torus line.

---

# Unlocked by This

> [!tip] **The Frobenius theorem** *(from this same topic)*
> The central theorem of the section answers "when does a distribution admit integral manifolds?" — the answer is "iff involutive." See [[Thm - The Frobenius Theorem]] for the full statement and proof.

> [!tip] **Foliation** *(from this same topic)*
> The global, organized version of "$M$ partitions into integral manifolds." A foliation is the partition by maximal connected integral manifolds, which exists exactly when the distribution is involutive — by the global Frobenius theorem. See [[Def - Foliation]].

> [!tip] **Solution manifold of an overdetermined PDE** *(from PDE Theory)*
> For an overdetermined first-order PDE system, the solution manifold (graph of solutions) is precisely an integral manifold of the associated distribution. The classical PDE compatibility theorem of Frobenius — that solutions exist iff the mixed-partial conditions hold — is Frobenius's theorem applied to this distribution.

> [!tip] **Cauchy problem in the Cartan–Kähler theory** *(from Exterior Differential Systems)*
> The general theory of overdetermined PDE — beyond first-order, including the Einstein field equations and conservation laws — is formulated via **exterior differential systems**: ideals in the form algebra whose integral manifolds are solutions. The Cartan–Kähler theorem generalizes Frobenius to this setting, providing existence of integral manifolds under a more refined "involutivity" condition (Cartan's test).

---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
  - "Def - Rank of a Smooth Map"
  - "Def - Immersion, Submersion, and Embedding"
tags: [geometry, differential-geometry]
---

# Notation

$\Phi : M \to N$ is a smooth map between smooth manifolds with $\dim M = m$, $\dim N = n$. At each $p \in M$, the differential $d\Phi_p : T_p M \to T_{\Phi(p)} N$ is a linear map between tangent spaces. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

This is a compound page: it defines four interlocking notions — **regular point**, **critical point**, **regular value**, **critical value** — because they are introduced together and none is fully usable without the others. Regular/critical *points* are properties of points in the domain; regular/critical *values* are derived properties of points in the codomain.

---

# Axiom Motivation

The [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] says that, when the differential of $\Phi$ is surjective at every point of a level set $\Phi^{-1}(c)$, the level set is an embedded submanifold of $M$ with computable [[Def - Dimension|dimension]] and tangent space. This raises the question: at which points is the differential surjective? At which values is it surjective everywhere on the level set? These are the geometrically meaningful questions, and the definitions of "regular point" and "regular value" exist exactly to answer them.

**Why "regular" for surjectivity of $d\Phi_p$.** A point $p$ where $d\Phi_p$ is surjective is one where $\Phi$ "behaves regularly" in the sense that the [[Thm - The Implicit Function Theorem|implicit function theorem]] applies — locally $\Phi$ looks like a coordinate projection, and the level set through $p$ is locally a graph (and hence locally a submanifold). The natural opposite is "critical": a point where the linearisation drops rank, where $\Phi$ "behaves singularly" in the sense that the IFT does not apply.

Why is surjectivity the right condition (rather than, say, injectivity or non-zero)? Because the local structure we want — "the level set through $p$ is locally a submanifold of codimension $n$" — is provided by the implicit function theorem, and the IFT's hypothesis is exactly surjectivity of the differential. The mismatch is informative: for an immersion's image, the relevant local structure is "image is locally a submanifold", and the corresponding "good point" condition is *injectivity* of the differential. But for *level sets*, surjectivity is what we need.

**Why regular *values* propagate from regular *points*.** The natural way to test for "$\Phi^{-1}(c)$ is a submanifold" is to check that *every* point of $\Phi^{-1}(c)$ is regular. This is the definition of regular value. If even one point of the preimage is critical, the level set can fail to be a submanifold there — even though the rest of the level set might be perfectly fine. The classical example is the cone $\{z^2 = x^2 + y^2\}$ in $\mathbb{R}^3$: this is the level set of $\Phi(x,y,z) = z^2 - x^2 - y^2$ at $0$, and $0$ is a *critical value* because the origin is a critical point of $\Phi$ ($\nabla\Phi = 0$ there). The cone is a submanifold everywhere except at its vertex, which is exactly the critical point.

What if we only required regularity at "most" points of the level set? Then we'd admit critical sets where the manifold structure fails at isolated points, which would defeat the purpose: we want $\Phi^{-1}(c)$ to be a clean global submanifold, and one critical point on the preimage is enough to break this.

What about the **empty preimage** case? By convention, a value $c$ with $\Phi^{-1}(c) = \varnothing$ is automatically regular (vacuously: there are no points to be critical). This is the right convention because the conclusion of the regular value theorem is trivially true for an empty level set, and we should not exclude empty level sets from being "regular".

The **lower semicontinuity of rank** ([[Def - Rank of a Smooth Map]]) gives the set of regular points an additional useful property: it is *open* in $M$. So when checking that $c$ is regular, you only need to check at the points of $\Phi^{-1}(c)$; the regularity then extends to an open neighbourhood automatically (by the openness of the regular-point set). This is what makes regular values stable under small perturbations of $c$ — and indirectly what makes [[Thm - Sard's Theorem|Sard's theorem]] so powerful.

---

# The Definition

Let $\Phi : M \to N$ be a smooth map between smooth manifolds.

**Regular point.** A point $p \in M$ is a **regular point** of $\Phi$ if the differential $d\Phi_p : T_p M \to T_{\Phi(p)} N$ is **surjective** — equivalently, if $\mathrm{rank}\, d\Phi_p = \dim N$, equivalently, if $\Phi$ is a submersion at $p$.

**Critical point.** A point $p \in M$ is a **critical point** of $\Phi$ if it is not regular — that is, if $d\Phi_p$ fails to be surjective.

**Regular value.** A point $c \in N$ is a **regular value** of $\Phi$ if every point of the preimage $\Phi^{-1}(c)$ is a regular point of $\Phi$. By convention, if $\Phi^{-1}(c) = \varnothing$, then $c$ is automatically regular.

**Critical value.** A point $c \in N$ is a **critical value** of $\Phi$ if it is not regular — that is, if there is at least one critical point of $\Phi$ in $\Phi^{-1}(c)$.

**Notes:**
- Critical *points* and regular *points* live in $M$; critical *values* and regular *values* live in $N$.
- The set of regular points is open in $M$ (by lower semicontinuity of rank).
- The set of critical points may be closed but is not necessarily small; the set of *critical values*, however, is small in the sense of measure zero ([[Thm - Sard's Theorem|Sard's theorem]]).
- If $\dim M < \dim N$, then every point of $M$ is critical (the differential cannot be surjective from a lower-dimensional space). Correspondingly, the image $\Phi(M)$ has measure zero in $N$, so almost every value is regular by the empty-preimage convention.
- If $\dim M = \dim N$, then $p$ is regular iff $d\Phi_p$ is a linear isomorphism iff $\Phi$ is a local [[Def - Diffeomorphism|diffeomorphism]] at $p$.

---

# Relate to Other Fields / Compression

The notions of regular and critical points are the **manifold-level generalisations of the analogous notions from multivariable analysis**. For $\Phi : U \to \mathbb{R}^n$ on an open subset $U \subseteq \mathbb{R}^m$, the regular/critical-point distinction is described in [[Multivariate Analysis II — Inverse and Implicit Function Theorems|MA II]] and is the input to the Euclidean [[Thm - The Regular Value Theorem|regular value theorem]]. The manifold definitions coincide with the analysis definitions when $M$ and $N$ are open subsets of Euclidean space.

For a **scalar function** $f : M \to \mathbb{R}$, the regular/critical distinction reduces to: $p$ is critical iff $df_p = 0$, iff every directional derivative of $f$ at $p$ vanishes — the usual calculus notion of "critical point" of a function. This is the case of [[Def - Critical Point, Hessian, and Definiteness|critical point analysis]] for scalar functions, where the second-order classification (local minimum, local maximum, saddle, degenerate) is done via the Hessian.

**True name:** the **true name** of "regular point" is "**point where the implicit function theorem applies locally**" — that is, a point where $\Phi$'s level set through that point is locally a smooth $(m-n)$-dimensional submanifold. The "rank of differential equals $\dim N$" definition is the verification criterion; the IFT-applicability is the operational content.

The **true name** of "regular value" is "**value at which the level set is uniformly nice everywhere**" — every point of the preimage admits the local manifold structure. The empty-preimage convention is the limiting case where there is no preimage to worry about.

---

# Examples / Corollaries

**Example — a scalar function on $\mathbb{R}^n$.** For $f : \mathbb{R}^n \to \mathbb{R}$, the regular points are the points where $\nabla f \neq 0$, and the critical points are the points where $\nabla f = 0$. The critical values are the values $f$ takes at critical points. For $f(x) = |x|^2$ on $\mathbb{R}^n$, the only critical point is the origin (where $\nabla f = 0$), and the only critical value is $0$. Every positive value is regular, and the level sets $|x|^2 = c > 0$ are spheres.

**Example — the quadratic $\Phi(x,y,z) = z^2 - x^2 - y^2$ on $\mathbb{R}^3$.** $\nabla\Phi = (-2x, -2y, 2z)$ vanishes only at the origin. So the origin is the unique critical point, and $0 = \Phi(0,0,0)$ is the unique critical value. The level set $\{\Phi = 0\}$ is the cone $z^2 = x^2 + y^2$ — a submanifold everywhere except at the vertex. Level sets $\{\Phi = c\}$ for $c \neq 0$ are hyperboloids (one-sheeted for $c < 0$, two-sheeted for $c > 0$), which are smooth submanifolds.

**Example — the determinant on $\mathrm{Mat}_n(\mathbb{R})$.** For $\det : \mathrm{Mat}_n \to \mathbb{R}$, the differential at a matrix $A$ is $d\det_A(X) = \det A \cdot \mathrm{tr}(A^{-1} X)$ (when $A$ is invertible). This is non-zero whenever $A$ is invertible, so every $A \in \mathrm{GL}(n,\mathbb{R})$ is a regular point. Hence every non-zero value of $\det$ is a regular value, and the level set $\{\det = c\}$ for $c \neq 0$ is a regular level set — an embedded submanifold of $\mathrm{Mat}_n$ of dimension $n^2 - 1$. In particular $\mathrm{SL}(n,\mathbb{R}) = \{\det = 1\}$ is one of these, of dimension $n^2 - 1$; see [[Ex - The Special Linear Group is a Submanifold of GL(n)|Ex - The Special Linear Group is a Submanifold of GL(n)]]. The value $0$ is a critical value (the singular matrices form the critical set, and they get mapped to $0$).

**Example — the squaring map on $\mathbb{C}$.** $\Phi(z) = z^2$ has differential $d\Phi_z(w) = 2zw$ (in complex coordinates). This is surjective onto $\mathbb{C}$ iff $z \neq 0$. So the origin is the unique critical point of $\Phi$ in $\mathbb{C}$, and $0 = \Phi(0)$ is the unique critical value. Every $c \neq 0$ is a regular value; the level set $\{z^2 = c\}$ for $c \neq 0$ is the two points $\{\pm\sqrt{c}\}$, an embedded $0$-submanifold.

**Example — projection $\pi : \mathbb{R}^{m+n} \to \mathbb{R}^n$.** Every point of $\mathbb{R}^{m+n}$ is regular for $\pi$ (the differential is the constant projection, which is surjective). Every value of $\pi$ is regular. Every level set is a smooth submanifold (in fact a copy of $\mathbb{R}^m$).

**Example — the inclusion $S^n \hookrightarrow \mathbb{R}^{n+1}$.** Every point of $S^n$ is critical for $\iota$ — because $\dim S^n = n < n + 1 = \dim \mathbb{R}^{n+1}$, the differential cannot be surjective. There are no regular points of $\iota$. Every value of $\iota$ in $S^n$ is a critical value (it has a critical point in its preimage); every value of $\iota$ not in $S^n$ has empty preimage and is vacuously regular. By Sard, the image $S^n$ has measure zero in $\mathbb{R}^{n+1}$, confirming the principle.

**Is NOT a critical value — empty preimage.** A value $c \in N$ that is not in $\Phi(M)$ has $\Phi^{-1}(c) = \varnothing$ and is automatically regular by convention. This corner case ensures the regular value theorem is vacuously true for values outside the image.

**Corollary — the set of regular points is open.** Lower semicontinuity of rank means $\{p : \mathrm{rank}\, d\Phi_p \geq n\}$ is open in $M$; since the maximum possible rank is $n = \dim N$, this is exactly the set of regular points.

**Corollary — every point is regular when $\dim M = \dim N$ and $\Phi$ is a local diffeomorphism.** A local diffeomorphism has $d\Phi_p$ a linear isomorphism at every point, hence surjective, hence regular.

**Corollary — composition of submersions has only regular points.** If $\Phi : M \to N$ and $\Psi : N \to P$ are smooth submersions, then $\Psi \circ \Phi : M \to P$ is a smooth submersion (composition of surjective linear maps is surjective). So every point of $M$ is regular for $\Psi \circ \Phi$.

**Calibration check.** Verify that for $f(x) = x^3$ on $\mathbb{R}$, the only critical point is $0$ and the only critical value is $0$ — even though $f$ is bijective and globally invertible (the inverse is just not smooth at $0$). Verify that for $\Phi : \mathbb{R}^2 \to \mathbb{R}^2$, $\Phi(x,y) = (x^2 - y^2, 2xy)$ (the squaring on $\mathbb{C}$), the only critical point is the origin. Verify that for the height function $h : S^2 \to \mathbb{R}$, $h(x,y,z) = z$, the critical points are the north and south poles and the critical values are $\pm 1$.

---

# Unlocked by This

> [!tip] The Regular Value Theorem *(from this topic)*
> The reason these definitions exist: by the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]], $\Phi^{-1}(c)$ is an embedded submanifold of $M$ whenever $c$ is a regular value. This is the standard manufacturing device for submanifolds, and "regular value" is the genericity condition that makes it work.

> [!tip] Sard's Theorem and Genericity *(from this topic)*
> By [[Thm - Sard's Theorem|Sard's theorem]], the set of critical values has measure zero in $N$. So regular values are dense in $N$ — almost every value is regular. This is the genericity result that makes the regular value theorem ubiquitously applicable: when you can't pin down a specific regular value, the theorem guarantees one exists nearby.

> [!tip] Morse Theory *(from Differential Topology)*
> A **Morse function** is a smooth $f : M \to \mathbb{R}$ whose critical points are all *non-degenerate* (the Hessian at each critical point is non-singular). Morse functions are generic (by a Sard-style argument), and **Morse theory** reconstructs the topology of $M$ from the critical-point data of any Morse function. Critical *points* (not values) and their indices encode topological information about $M$ at the level of cells, Betti numbers, and CW-structure.

> [!tip] Transversality *(from Differential Topology)*
> A smooth map $\Phi : M \to N$ is **transverse** to a submanifold $S \subseteq N$ if at every $p \in \Phi^{-1}(S)$, the image of $d\Phi_p$ together with $T_{\Phi(p)} S$ spans all of $T_{\Phi(p)} N$. Transversality is the natural generalisation of "regular value": for $S$ a single point, transversality reduces to $p$ being a regular point. Transverse maps give submanifolds: $\Phi^{-1}(S)$ is a smooth submanifold of $M$ whenever $\Phi$ is transverse to $S$.

> [!tip] Mapping Degree *(from Algebraic Topology)*
> For a smooth map $f : M \to N$ between compact oriented manifolds of the same dimension, the **mapping degree** $\deg(f)$ is the signed count of preimages of a regular value. This is independent of the choice of regular value (by Sard, such values exist; by a connectedness/parity argument, the signed count is independent of the choice). Degree theory is the foundation of intersection numbers, the Brouwer fixed-point theorem, and the fundamental theorem of algebra.

---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold with Boundary"
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Interior Product (Contraction with a Vector Field)"
tags: [geometry, differential-geometry, orientation, boundary, manifold-with-boundary]
---

# Notation

Throughout, $M$ is a smooth $n$-manifold *with boundary* ($n \geq 1$). $\partial M$ is its boundary, an $(n-1)$-dimensional smooth manifold (without boundary, by [[Def - Smooth Manifold with Boundary|the definition]]). The boundary inclusion is $\iota : \partial M \hookrightarrow M$. The half-space model is $\mathbb{H}^n = \{x \in \mathbb{R}^n : x^n \geq 0\}$ with boundary $\partial\mathbb{H}^n = \{x^n = 0\} \cong \mathbb{R}^{n-1}$. A **vector field along $\partial M$** is a section $N : \partial M \to TM|_{\partial M}$ of the *ambient* tangent bundle restricted to $\partial M$; the value $N_p$ lies in $T_pM$, not necessarily in $T_p\partial M$. $N$ is **outward-pointing** if for every $p \in \partial M$ and every boundary chart, the last-coordinate component of $N_p$ is *negative* (recall the boundary is $\{x^n = 0\}$ with $\mathbb{H}^n = \{x^n \geq 0\}$, so "outward" is the $-\partial_n$ direction). The full notation registry is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

This is a compound page: it covers two interlocking notions — **smooth manifold with boundary** and **the induced (Stokes) orientation on its boundary** — because the integration theory of the topic uses them together and neither is fully usable without the other.

---

# Axiom Motivation

A bare smooth manifold ([[Def - Smooth Manifold]]) is locally modeled on $\mathbb{R}^n$ — every point has a chart homeomorphic to an open set in $\mathbb{R}^n$. To capture the geometry of regions with edges — a disc, a cube, a manifold-with-boundary embedded in space — we need a local model that *has* a boundary. The natural model is the upper half-space $\mathbb{H}^n = \{x^n \geq 0\}$. A point in the interior of $\mathbb{H}^n$ ($x^n > 0$) has an open neighborhood in $\mathbb{R}^n$; a point on the boundary ($x^n = 0$) has only a half-neighborhood. This dichotomy is intrinsic and forces the manifold-with-boundary structure.

A **smooth manifold with boundary** is then defined exactly as a smooth manifold, but using $\mathbb{H}^n$ instead of $\mathbb{R}^n$ as the local model. Charts are [[Def - Homeomorphism|homeomorphisms]] $\varphi : U \to \widehat U \subseteq \mathbb{H}^n$ with smooth transitions in the half-space sense (smooth on the closure of an open subset, with all derivatives extending continuously). The **boundary** $\partial M$ is the set of points sent to $\{x^n = 0\}$ by any (equivalently, every) chart — well-defined because boundary points cannot be interior in any chart, as the half-space model is local-[[Def - Diffeomorphism|diffeomorphism]]-distinct from $\mathbb{R}^n$ at boundary points.

The boundary $\partial M$ is itself an $(n-1)$-manifold without boundary: the restriction of each boundary chart $(U, \varphi)$ to $U \cap \partial M$ gives a chart $\varphi|_{U \cap \partial M} : U \cap \partial M \to \widehat U \cap \{x^n = 0\} \cong \mathbb{R}^{n-1}$ open. Transition maps restrict to smooth maps of $\mathbb{R}^{n-1}$ subsets, so $\partial M$ inherits a smooth structure.

Now suppose $M$ is *oriented*. We want $\partial M$ to also be oriented, in a way that makes [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] hold with the right sign. The boundary orientation cannot be arbitrary: it is determined by the convention that makes the identity $\int_M d\omega = \int_{\partial M}\omega$ true. We can derive the convention by examining the half-space model.

On $\mathbb{H}^n$ with the standard orientation, the boundary $\partial\mathbb{H}^n = \{x^n = 0\}$ has natural coordinates $(x^1, \ldots, x^{n-1})$. The question: should the standard ordered basis $(\partial_1, \ldots, \partial_{n-1})$ be positively or negatively oriented for $\partial\mathbb{H}^n$? The answer is forced by computing both sides of Stokes for a model form. With $\omega = b(x)\,dx^1\wedge\cdots\wedge dx^{n-1}$ supported in $\mathbb{H}^n$, the left side $\int_{\mathbb{H}^n}d\omega = \int_{\mathbb{H}^n}(-1)^{n-1}\partial_nb\,dx^1\wedge\cdots\wedge dx^n$ evaluates to $(-1)^{n-1}\int_{\mathbb{R}^{n-1}}[\partial_nb]_{x^n=0}\cdots$, which by FTC equals $(-1)^n\int_{\mathbb{R}^{n-1}}b(x',0)\,dx^1\cdots dx^{n-1}$. For this to equal $\int_{\partial\mathbb{H}^n}\omega$ with the standard $\mathbb{R}^{n-1}$ orientation, we would need the boundary orientation to be $(-1)^n$ times the standard. So the *induced orientation* on $\partial\mathbb{H}^n$ — the one that makes Stokes hold — is the standard $\mathbb{R}^{n-1}$ orientation for $n$ even, and the *opposite* for $n$ odd.

The cleanest statement of this convention is via the **outward-pointing vector**. At a boundary point $p$, the outward normal direction in $\mathbb{H}^n$ is $-\partial_n$ (which points out of $\mathbb{H}^n = \{x^n \geq 0\}$). The convention is:

$$(E_1, \ldots, E_{n-1})\text{ positive for }T_p\partial M \iff (-\partial_n, E_1, \ldots, E_{n-1})\text{ positive for }T_pM,$$

or equivalently with any outward-pointing $N$ in place of $-\partial_n$:

$$\boxed{(E_1, \ldots, E_{n-1})\text{ positive for }\partial M \iff (N, E_1, \ldots, E_{n-1})\text{ positive for }M.}$$

This is the **outward-first** or **Stokes** convention. The justification is exactly that it makes Stokes's theorem $\int_M d\omega = \int_{\partial M}\omega$ come out with the right sign. Once you adopt this convention, the half-space computation works out to an *equality* with no extra sign.

**Equivalent formulation: orientation form via interior product.** If $\omega \in \Omega^n(M)$ is a positively-oriented volume form on $M$, and $N$ is an outward-pointing vector field along $\partial M$, then $\iota^*(\iota_N\omega) \in \Omega^{n-1}(\partial M)$ is a positively-oriented volume form for $\partial M$ with the induced orientation. This is the construction: contract with the outward normal, restrict to the boundary. The formula reproduces the outward-first convention by linear algebra:
$$(\iota_N\omega)(E_1, \ldots, E_{n-1}) = \omega(N, E_1, \ldots, E_{n-1}),$$
which is positive iff $(N, E_1, \ldots, E_{n-1})$ is positive for $\omega$.

**Per-axiom failure analysis: what breaks if we adopt the *inward*-first convention?** Stokes's theorem would acquire an overall minus sign: $\int_M d\omega = -\int_{\partial M}\omega$. Many texts adopt this (or its variants) and live with the sign. The outward-first convention is the more common one because the divergence theorem $\int_M(\nabla\cdot V)\,dV = \int_{\partial M}V\cdot N\,dA$ — with the *outward* flux — is so universally adopted in physics.

**What if the convention is "$N$ inserted in a different position"?** Inserting $N$ in the $k$-th position instead of first gives a factor of $(-1)^{k-1}$. Position-$1$ (outward-*first*) makes the cleanest statement, which is why it is conventional.

**What if $M$ has no boundary?** Then $\partial M = \emptyset$, and the induced orientation is vacuous. Stokes's theorem reads $\int_M d\omega = \int_\emptyset\omega = 0$ — the boundary-less case, where exact integrands integrate to zero.

**What if $M$ has corners?** Manifolds with corners (locally modeled on $\{x_1 \geq 0, \ldots, x_k \geq 0\} \times \mathbb{R}^{n-k}$) admit a generalization in which "boundary" becomes "boundary face" and the induced orientation works face by face. Lee covers this in §16, and Stokes still holds in this setting.

---

# The Definition

**Smooth manifold with boundary.** A **smooth $n$-manifold with boundary** is a topological space $M$ that is Hausdorff, second-countable, and locally modeled on $\mathbb{H}^n$: every point $p \in M$ has a chart $\varphi : U \to \widehat U \subseteq \mathbb{H}^n$ with $\varphi$ a [[Def - Homeomorphism|homeomorphism]], and transition maps $\widetilde\varphi \circ \varphi^{-1}$ smooth in the half-space sense (smooth in the interior, with all derivatives extending continuously to the boundary). See [[Def - Smooth Manifold with Boundary]] for full details.

The **boundary** $\partial M$ is the set of points $p$ such that some (equivalently, every) chart sends $p$ to $\{x^n = 0\}$. The **interior** is $\mathring M := M \setminus \partial M$, locally modeled on $\mathbb{R}^n$. The boundary is itself a smooth $(n-1)$-manifold without boundary, and the inclusion $\iota : \partial M \hookrightarrow M$ is a smooth embedding.

**Outward-pointing vector field.** A vector field $N$ *along* $\partial M$ is a smooth map $N : \partial M \to TM|_{\partial M}$ with $N_p \in T_pM$ for $p \in \partial M$. It is **outward-pointing** at $p \in \partial M$ if in any smooth boundary chart $(U, \varphi)$ around $p$ with coordinates $(x^1, \ldots, x^n)$, the last component $N^n(p) < 0$. Outward-pointing vector fields exist (by partition of unity), and any two determine the same orientation on $\partial M$.

**Induced (Stokes) orientation on $\partial M$.** Let $M$ be an oriented smooth $n$-manifold with boundary ($n \geq 1$). The **induced orientation** on $\partial M$ is the unique orientation characterized by:

> For each $p \in \partial M$, a basis $(E_1, \ldots, E_{n-1})$ of $T_p\partial M$ is positively oriented for $\partial M$ if and only if $(N_p, E_1, \ldots, E_{n-1})$ is positively oriented for $T_pM$, where $N_p$ is any outward-pointing vector at $p$.

**Equivalent formulation via top-form contraction.** If $\omega \in \Omega^n(M)$ is a positively-oriented volume form on $M$ and $N$ is a smooth outward-pointing vector field along $\partial M$, then the $(n-1)$-form
$$\iota^*(\iota_N\omega) \in \Omega^{n-1}(\partial M)$$
is a positively-oriented volume form for $\partial M$ with the induced orientation. (Here $\iota_N$ is the [[Def - Interior Product (Contraction with a Vector Field)|interior product]] / contraction with $N$, $\iota^*$ is pullback by the boundary inclusion.)

**0-dimensional boundary.** If $n = 1$, then $\partial M$ is a 0-manifold (a discrete set of points). The induced orientation assigns to each $p \in \partial M$ the sign $+1$ if some outward-pointing $N_p$ is positively oriented for $T_pM$, and $-1$ otherwise. For $M = [a, b] \subseteq \mathbb{R}$ with the standard orientation, this gives $\partial M = \{b\}^+ \cup \{a\}^-$ — the right endpoint positive, the left endpoint negative. This is the convention behind the FTC, $\int_{[a, b]}df = f(b) - f(a)$.

**Half-space example.** On $\mathbb{H}^n = \{x^n \geq 0\}$ with the standard orientation, the boundary $\partial\mathbb{H}^n = \{x^n = 0\} \cong \mathbb{R}^{n-1}$ has induced orientation equal to the standard orientation of $\mathbb{R}^{n-1}$ when $n$ is even, and the opposite of the standard when $n$ is odd. The outward-pointing vector at the boundary is $-\partial_n$, and the convention $(-\partial_n, \partial_1, \ldots, \partial_{n-1}) = (-1)^n(\partial_1, \ldots, \partial_n)$ produces the sign factor.

---

# Categorical / Structural Definition

A smooth manifold with boundary fits into the category $\mathbf{Diff}^\partial$ of smooth manifolds with boundary and smooth maps respecting the boundary structure. The **boundary functor** $\partial : \mathbf{Diff}^\partial \to \mathbf{Diff}$ sends $M$ to $\partial M$ and a boundary-preserving smooth map $f : M \to N$ to its restriction $\partial f := f|_{\partial M} : \partial M \to \partial N$ (when $f$ takes boundary to boundary). When $M$ is oriented, the induced orientation on $\partial M$ makes $\partial$ a functor on the category of *oriented* manifolds with boundary.

In the **categorical Stokes** language: $\partial$ on the manifold side is "adjoint" to $d$ on the form side, in the sense that integration provides a pairing $\Omega^k(M) \times M^k \to \mathbb{R}$ (where $M^k$ is the space of $k$-chains) under which $d^* = \pm\partial$. The induced orientation convention is what makes this adjunction strict, with no extra sign.

The **structural backbone** of the boundary orientation is:
$$\iota^*\iota_N\,\omega = \omega_{\partial M},$$
the interior-product-then-restrict formula, which encodes "outward-first" as a linear-algebraic identity.

---

# Relate to Other Fields / Compression

The induced orientation is **the convention that makes Stokes's theorem have no extra sign factors**. Equivalently, it is the *outward flux* convention in physics — the convention under which the divergence theorem reads $\int_M\nabla\cdot V = \int_{\partial M}V\cdot N$ with $N$ outward and *no* minus sign. The connection to physics is direct: the boundary orientation is exactly the convention under which "the flux out of a region" is positive when the field points outward.

In **algebraic topology**, the boundary operator $\partial$ on singular chains satisfies $\partial^2 = 0$ — the boundary of a boundary is zero. This is the topological dual of $d^2 = 0$ on forms, and the integration pairing exhibits the duality. The induced orientation convention is what makes $\partial$ on chains have this anti-symmetric structure with respect to face inclusion (a standard combinatorial result in simplicial homology).

**True name:** The induced orientation is the unique orientation of $\partial M$ for which "outward normal first" is a positive frame extension — equivalently, the orientation for which $\iota^*(\iota_N\omega)$ is positively-oriented for any positively-oriented volume form $\omega$ on $M$ and any outward-pointing $N$. This is the operational form; concrete computations of boundary orientations always reduce to checking the sign of $(N, E_1, \ldots, E_{n-1})$.

---

# Examples / Corollaries

**Is an instance — $M = [a, b]$, $\partial M = \{a, b\}$.** With $M$ oriented by $\partial_x$ (the standard orientation), the boundary points have induced orientations: $b$ is $+1$, $a$ is $-1$. Reason: at $b$, the outward direction is $+\partial_x$, which agrees with the orientation, so the 0-dimensional sign is $+1$. At $a$, the outward direction is $-\partial_x$, opposite to the orientation, so the sign is $-1$. The FTC $\int_a^b f'\,dx = f(b) - f(a)$ is exactly Stokes with this 0-dimensional boundary orientation.

**Is an instance — $M = \overline{B^n}$ (closed unit ball in $\mathbb{R}^n$), $\partial M = S^{n-1}$.** The outward normal at $p \in S^{n-1}$ is $p$ itself (viewed as a tangent vector to $\mathbb{R}^n$ at $p$). The induced orientation on $S^{n-1}$ is the *standard* orientation of the sphere — the one in which a basis of $T_pS^{n-1}$ is positive iff prepending $p$ gives a positive basis of $T_p\mathbb{R}^n = \mathbb{R}^n$. This is the convention that makes the divergence theorem on the ball read $\int_{B^n}\nabla\cdot V\,dV = \int_{S^{n-1}}V\cdot N\,dA$ with $N$ outward (and no sign).

**Is an instance — $M = \mathbb{H}^n$.** The boundary $\partial\mathbb{H}^n = \{x^n = 0\}$ inherits the induced orientation $(-1)^n\cdot$(standard orientation of $\mathbb{R}^{n-1}$). For $n = 1$, this is "negative orientation": the boundary point $0$ of $\mathbb{H}^1 = [0, \infty)$ gets sign $-1$ (because the outward direction is $-\partial_1$). For $n = 2$ (upper half plane $\mathbb{H}^2$), the induced orientation on $\partial\mathbb{H}^2 = \mathbb{R}$ is the *opposite* of the standard (the convention is "left-to-right is negative for the boundary of the upper half plane").

**Is an instance — $M$ a solid torus, $\partial M = T^2$.** The boundary of a solid torus $M = D^2 \times S^1$ is the 2-torus $T^2 = S^1 \times S^1$. The induced orientation is the product of the standard orientation on the inner $S^1$ (from the boundary of the disc $D^2$) and the existing orientation on the outer $S^1$. This is a useful example for visualizing higher-genus surfaces as boundaries.

**Non-example — boundary of an open manifold.** An open manifold (one without boundary) has $\partial M = \emptyset$, so the induced orientation is vacuous. Stokes's theorem on an open manifold (without boundary) reads $\int_M d\omega = 0$ for compactly supported $\omega$ — the boundary contribution vanishes.

**Corollary — opposite orientation flips boundary orientation.** If $-M$ denotes $M$ with the opposite orientation, then $\partial(-M) = -\partial M$ — the boundary has its orientation flipped as well. This is the consistent way to handle orientation reversal in Stokes: $\int_{-M}d\omega = -\int_M d\omega = -\int_{\partial M}\omega = \int_{-\partial M}\omega$.

**Corollary — outward-pointing vector field exists.** By partition of unity, one can build a smooth outward-pointing vector field $N$ along $\partial M$: in each boundary chart, $-\partial_n$ is outward; glue via partition of unity to get a global outward $N$. (See Lee Problem 8-4 / 13-21.)

**Corollary — induced orientation is intrinsic.** The induced orientation does not depend on the choice of outward-pointing vector field $N$ used to define it: any two outward-pointing vectors give the same orientation, by the linear-algebra fact that they differ by a positive multiple in $T_pM/T_p\partial M$ (the quotient is one-dimensional, and both are on the same side).

**Calibration check.** Verify that on $[a, b]$ with standard orientation, $b$ is positive and $a$ is negative; that $S^2$ as the boundary of the unit ball $\overline{B^3}$ inherits the standard outward-normal orientation; that the induced orientation on $\partial\mathbb{H}^2$ is *opposite* to the standard orientation of $\mathbb{R}$; and that the divergence theorem on a region in $\mathbb{R}^3$ uses the outward-flux convention. If you can also reconstruct the sign of $(-\partial_n, \partial_1, \ldots, \partial_{n-1})$ in the standard orientation of $\mathbb{R}^n$ for $n = 1, 2, 3, 4$ (it is $(-1)^n$ times standard), you have understood the convention.

---

# Unlocked by This

> [!tip] Stokes's Theorem *(continued in this topic)*
> The induced orientation is the convention under which $\int_M d\omega = \int_{\partial M}\omega$ holds with no extra signs. See [[Thm - Stokes' Theorem on Manifolds]].

> [!tip] Divergence Theorem and the Outward-Flux Convention *(from Vector Calculus)*
> The divergence theorem $\int_M\nabla\cdot V\,dV = \int_{\partial M}V\cdot N\,dA$ with $N$ outward unit normal is the Riemannian translation of Stokes via the induced orientation. The "outward" in physics-of-flux is exactly the outward-pointing vector field used to define the induced orientation.

> [!tip] Manifolds with Corners *(from Differential Geometry / Mathematical Physics)*
> A natural generalization: manifolds locally modeled on $\{x_1 \geq 0, \ldots, x_k \geq 0\} \times \mathbb{R}^{n-k}$, with boundaries having corners. The boundary decomposes into "faces" of various codimensions, each with its own induced orientation. Stokes's theorem extends, and is the foundation of the cubical / simplicial chain complex.

> [!tip] Chain Complex of Singular Homology *(from Algebraic Topology)*
> The boundary operator $\partial$ on singular chains satisfies $\partial^2 = 0$ (boundary of a boundary is empty) — the topological dual of $d^2 = 0$. The induced orientation convention is the geometric input that makes the chain-level $\partial$ have the right signs, giving the singular chain complex its structure.

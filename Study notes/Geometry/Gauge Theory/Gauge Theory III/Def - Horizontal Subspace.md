---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Fundamental Vector Field of a Principal Bundle"
  - "Def - Vector Field on a Manifold"
tags: [geometry, gauge-theory, principal-bundles, connections]
---

# Notation

$P \to M$ is a principal $G$-bundle, $\pi : P \to M$ the projection, $V_p P = \ker(d\pi_p)$ the canonical **vertical subspace** at $p$. $\omega \in \Omega^1(P; \mathfrak{g})$ is a [[Def - Connection 1-Form on a Principal Bundle|connection 1-form]]. The horizontal subspace at $p$ depends on $\omega$ and is denoted $H_p$.

---

# Axiom Motivation

The fundamental problem solved by a connection is the *splitting of the tangent space at each point of the total space*. At any $p \in P$, there is a canonical $\dim G$-dimensional subspace — the vertical subspace $V_p P$, tangent to the fibre — but no canonical complementary subspace. Any choice of complementary subspace $H_p$ such that $T_p P = V_p P \oplus H_p$ would let one project tangent vectors onto their "horizontal" and "vertical" parts, giving a well-defined notion of parallel transport: a curve is *horizontal* if its tangent vector is everywhere in the horizontal subspaces, and parallel transport is "lift the curve horizontally".

So a connection should specify, at each point $p \in P$, a horizontal subspace $H_p \subset T_p P$. But not arbitrarily — three conditions must be satisfied for the choice to be a *connection*.

**(i) Smoothness.** The assignment $p \mapsto H_p$ should vary smoothly with $p$. Equivalently, $\{H_p\}_{p \in P}$ should be a smooth rank-$n$ subbundle of $TP$ ($n = \dim M$). Without smoothness, the horizontal lift of a smooth curve might not be smooth, and parallel transport would not have the regularity needed for ODE existence.

**(ii) Transversality to the vertical.** At every $p$, $T_p P = V_p P \oplus H_p$ — that is, $H_p$ is a complement of $V_p P$. Equivalently, $H_p \cap V_p P = 0$ and $\dim H_p = n$. Without transversality, the splitting is not a direct sum, and the horizontal projection is not uniquely defined.

**(iii) $G$-equivariance.** $(R_g)_* H_p = H_{p \cdot g}$ for every $g \in G$ — the right action carries horizontal subspaces to horizontal subspaces. Without equivariance, the horizontal distribution would not respect the principal-bundle structure, parallel transport would depend on the choice of representative in the fibre, and the formalism would not descend cleanly to the base.

These three conditions exhaust the requirements. A smooth $G$-equivariant rank-$n$ horizontal distribution is *exactly* the geometric content of a connection — see [[Thm - Principal Connection is Equivalent to a Horizontal Distribution]] for the precise bijection with the 1-form formulation.

Why is the choice of $H_p$ not canonical (i.e., why is there an entire affine space of connections)? Because the principal-bundle structure does *not* canonically give a complement to the vertical subspace. The vertical subspace is canonical (it is the kernel of the projection $d\pi$). A complement requires extra data: that data is the connection.

What if we tried to define a horizontal distribution without equivariance — just smoothness and transversality? The result would still be an "Ehresmann connection" in a weaker sense (sometimes called a "non-principal connection"). But such a distribution does *not* give a well-defined parallel transport that respects the group action: if you parallel transport $p$ along $\gamma$ to get $p'$, and then transport $p \cdot g$ along the same $\gamma$, you might *not* get $p' \cdot g$ — the two transports would not be compatible. Equivariance is precisely what makes parallel transport "the same for every representative in the fibre", which is essential for the geometry to descend to the base $M$.

The dual axiom of verticality (from the 1-form picture) is automatic in the distribution picture: given a horizontal distribution $H$, the vertical-space isomorphism $\xi \mapsto \xi^*_p$ identifies $\mathfrak{g}$ with $V_p P$ at every $p$, and the unique $\mathfrak{g}$-valued 1-form on $P$ vanishing on $H_p$ and acting as the inverse of this isomorphism on $V_p P$ is the connection 1-form $\omega$ with $H_p = \ker\omega_p$. The bijection between 1-forms and distributions is exact.

What does "horizontal" actually mean geometrically? The horizontal vectors $H_p$ are tangent to *horizontal curves* — curves whose lifts from the base to the total space do not move in the fibre direction. So a horizontal curve in $P$ above a curve $\gamma$ in $M$ is the lift "with no fibre motion", or equivalently "constant section" in the appropriate sense. Parallel transport from $p_0$ along $\gamma$ is the endpoint of the horizontal lift starting at $p_0$. This is the geometric content of the entire formalism.

---

# The Definition

Let $P \to M$ be a principal $G$-bundle and $\omega \in \Omega^1(P; \mathfrak{g})$ a [[Def - Connection 1-Form on a Principal Bundle|connection 1-form]] on $P$.

The **horizontal subspace** at $p \in P$ is
$$
H_p := \ker\omega_p \subseteq T_p P.
$$
The collection $\{H_p\}_{p \in P}$ is the **horizontal distribution** of the connection.

**Properties** (each derived from the axioms of $\omega$):

1. **Rank $n$.** $\dim H_p = n = \dim M$ for every $p$. Proof: by verticality, $\omega : T_p P \to \mathfrak{g}$ restricts to an isomorphism $V_p P \to \mathfrak{g}$, hence is surjective; so $\ker\omega_p$ has codimension $\dim\mathfrak{g} = \dim G$ in $T_p P$, giving $\dim H_p = (n + \dim G) - \dim G = n$.

2. **Transversality.** $T_p P = V_p P \oplus H_p$. Proof: $V_p P \cap H_p = V_p P \cap \ker\omega = 0$ because $\omega|_{V_p P}$ is injective (it is the inverse of an isomorphism). The dimension counts then give the direct sum.

3. **Smoothness.** $\{H_p\}$ is a smooth subbundle of $TP$. Proof: $\omega$ is smooth, so $\ker\omega$ is a smooth subbundle (the kernel of a surjective bundle map of constant rank).

4. **$G$-equivariance.** $(R_g)_* H_p = H_{p \cdot g}$ for every $g \in G$. Proof: $\omega_{p \cdot g}((R_g)_* X) = (R_g^*\omega)_p(X) = \mathrm{Ad}_{g^{-1}}\omega_p(X)$, which vanishes iff $\omega_p(X) = 0$ iff $X \in H_p$.

5. **Isomorphism with the base.** The projection $d\pi_p : H_p \to T_{\pi(p)} M$ is a linear isomorphism. Proof: $H_p$ has dimension $n$, and $d\pi_p$ kills only $V_p P$, so $d\pi_p|_{H_p}$ is injective; dimensions match, so it is surjective.

The **horizontal lift** of a tangent vector $X \in T_x M$ at a point $p$ above $x$ is the unique $\tilde X \in H_p$ with $d\pi_p(\tilde X) = X$. The **horizontal lift** of a curve $\gamma : I \to M$ starting at $p_0 \in \pi^{-1}(\gamma(0))$ is the unique curve $\tilde\gamma : I \to P$ with $\tilde\gamma(0) = p_0$, $\pi \circ \tilde\gamma = \gamma$, and $\dot{\tilde\gamma}(t) \in H_{\tilde\gamma(t)}$ for all $t$.

---

# Relate to Other Fields / Compression

In **Riemannian geometry**, the horizontal subspaces of the Levi-Civita connection on the orthonormal frame bundle $F^O(M) \to M$ are the "infinitesimal parallel transport directions" — the tangent vectors at a frame $f = (e_1, \ldots, e_n) \in F^O(M)_x$ that correspond to "moving along $M$ while keeping the frame parallel". A geodesic on $M$ corresponds to a horizontal curve in $F^O(M)$ whose projection is the geodesic and whose lift transports the initial frame parallel along it.

In **gauge theory**, horizontal subspaces are the "parallel transport directions" for the gauge field. A particle moving along a curve $\gamma$ in $M$, with internal state $p \in P$, parallel transports along $\gamma$ by lifting $\gamma$ horizontally — the lift gives the evolution of the internal state. For a charged particle in an electromagnetic field, this is the **Aharonov-Bohm transport**: the holonomy $\oint \omega = \exp(-i\oint A_\mu dx^\mu) \in U(1)$ around a closed loop is the observable phase.

In **Frobenius's theorem language**, a horizontal distribution is **integrable** if and only if the curvature vanishes: $H$ has integral submanifolds (manifolds whose tangent space at each point equals the horizontal subspace) iff the connection is *flat*. Curvature is the *obstruction* to integrability of the horizontal distribution, by the formula $\Omega(X, Y) = -\omega([\tilde X, \tilde Y])$ for horizontal lifts $\tilde X, \tilde Y$ of base vector fields — curvature measures the failure of the Lie bracket of two horizontal vectors to remain horizontal.

**True name:** the horizontal subspace is *the canonical complement to the vertical subspace selected by the connection*. The vertical subspace is determined by the bundle structure (kernel of $d\pi$); the complementary subspace requires extra data (the connection); together they give a *canonical splitting* of $T_p P$ at every point. Every parallel-transport calculation is "pick a tangent vector on $M$, lift it horizontally, integrate the resulting horizontal curve on $P$".

---

# Examples / Corollaries

**Example (canonical flat connection on $M \times G$).** For the trivial bundle $P = M \times G$ with connection $\omega = \mathrm{pr}_G^* \theta_G$, the horizontal subspace at $(x, g)$ is the kernel of $\omega = g^{-1}dg$ in matrix-group notation. Tangent vectors at $(x, g)$ split as $(X, Y)$ with $X \in T_x M, Y \in T_g G$; the connection $\omega(X, Y) = (dL_{g^{-1}})_g(Y)$ kills $(X, Y)$ iff $Y = 0$. So $H_{(x, g)} = T_x M \times \{0\}$ — the "horizontal direction is the base direction, with no fibre motion". The horizontal lift of a curve $\gamma$ on $M$ starting at $(x_0, g_0)$ is $\tilde\gamma(t) = (\gamma(t), g_0)$ — parallel transport keeps the fibre coordinate constant.

**Example (Levi-Civita connection on a Riemannian manifold).** On $F^O(M) \to M$ with the Levi-Civita connection, horizontal lifts of curves $\gamma$ on $M$ are the *parallel-transported frame curves*. A frame at $\gamma(0)$ is transported along $\gamma$ by demanding each basis vector be parallel — this gives a frame at $\gamma(t)$ for all $t$, and the resulting curve in $F^O(M)$ is the horizontal lift.

**Example (non-trivial $U(1)$-bundle with non-flat connection).** On the Hopf bundle $S^3 \to S^2$ (a non-trivial $U(1)$-bundle) with the standard $U(1)$-connection, the horizontal subspaces are *not* integrable — there are no horizontal sections globally. Equivalently, the curvature 2-form is nonzero (it is the area 2-form on $S^2$, after pullback). The Hopf fibration is the prototype of a non-flat $U(1)$-bundle and the geometric source of the Dirac monopole.

**Is NOT an instance:** the vertical subspace $V_p P$ is not a horizontal subspace — by definition, "horizontal" means $\ker\omega$, and $V_p P$ is the *complement* of horizontal, not horizontal itself.

**Is NOT an instance:** an *integrable* rank-$n$ subbundle of $TP$ transverse to $V$ is not in general the horizontal distribution of a connection — it is the horizontal distribution only if it is also $G$-equivariant. A counterexample: on $S^3 \to S^2$, one can find rank-1 transverse subbundles that are not $U(1)$-equivariant; these are not the horizontal distribution of any connection.

**Corollary.** For any tangent vector $X \in T_p P$, the decomposition into vertical and horizontal parts is
$$
X = X^V + X^H, \quad X^V = \omega(X)^*_p, \quad X^H = X - \omega(X)^*_p.
$$
The vertical part is the fundamental vector field of $\omega(X)$; the horizontal part is what is left. Verification: $\omega(X^H) = \omega(X) - \omega(\omega(X)^*_p) = \omega(X) - \omega(X) = 0$, so $X^H$ is horizontal.

**Corollary.** Horizontal lifts of base vector fields are *not* in general horizontal lifts of their Lie brackets: $[\tilde X, \tilde Y] \neq \widetilde{[X, Y]}$ in general. The difference is exactly the curvature:
$$
\omega([\tilde X, \tilde Y]) = -\Omega(\tilde X, \tilde Y)
$$
for horizontal lifts $\tilde X, \tilde Y$ — see [[Thm - Cartan Structural Equation for Principal Connections]] for the proof. So the curvature measures the failure of the horizontal distribution to be integrable.

**Corollary (Frobenius).** The horizontal distribution is integrable (has integral submanifolds) iff the curvature vanishes identically. Equivalently, locally trivial parallel transport — paths in $M$ that lift to paths in $P$ with no fibre motion in any homotopy class — exists iff $\Omega = 0$. Flat connections are precisely those with integrable horizontal distributions.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify that the horizontal subspace of the canonical flat connection on $M \times G$ at $(x, g)$ is $T_x M \times \{0\}$ (no fibre direction), and that horizontal lifts of curves keep $g$ constant; (ii) explain why $H_p \cap V_p P = \{0\}$ from the verticality axiom of $\omega$, and why $H_p + V_p P = T_p P$ from a dimension count; (iii) compute the horizontal lift of a vector field $X = \partial_\theta$ on $S^2$ (in spherical coordinates near the equator) to the Hopf bundle $S^3 \to S^2$ with the standard connection — observe that the lift is *not* periodic, because integrating around $X$ in $S^2$ accumulates a $U(1)$-phase (the holonomy of the Hopf bundle).

---

# Unlocked by This

> [!tip] Parallel Transport in Principal Bundles *(from Gauge Theory III)*
> The horizontal distribution gives **parallel transport**: for a curve $\gamma : [0, 1] \to M$ and $p_0 \in \pi^{-1}(\gamma(0))$, the horizontal lift $\tilde\gamma : [0, 1] \to P$ with $\tilde\gamma(0) = p_0$ exists and is unique. The parallel transport operator $\tau_\gamma : \pi^{-1}(\gamma(0)) \to \pi^{-1}(\gamma(1))$ sends $p_0$ to $\tilde\gamma(1)$. For loops $\gamma$, $\tau_\gamma$ acts on $\pi^{-1}(\gamma(0))$ as $p_0 \mapsto p_0 \cdot g$ for some $g \in G$; the collection of all such $g$'s as $\gamma$ ranges over loops based at $\gamma(0)$ forms the **holonomy group** of the connection.

> [!tip] Frobenius Theorem and Flat Connections *(from Differential Geometry)*
> By the **Frobenius theorem** ([[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]]), an involutive distribution has integral submanifolds. The horizontal distribution $H$ is involutive iff the curvature vanishes; flat connections ($\Omega = 0$) have integrable $H$, and their integral submanifolds are the **leaves** of a foliation of $P$, classified by holonomy along loops in $M$. For simply connected $M$, a flat connection has the trivial holonomy, and $P$ admits a global horizontal section — the connection is gauge-equivalent to the trivial one.

> [!tip] Ehresmann Connections on General Fibre Bundles *(from Differential Geometry)*
> The horizontal-distribution picture generalises directly to *any* fibre bundle (not just principal): an **Ehresmann connection** on a fibre bundle $\pi : E \to M$ is a smooth rank-$\dim M$ subbundle $H \subset TE$ transverse to the vertical (with no equivariance requirement, since there is no group action in general). For principal bundles, the equivariance axiom is added to make the distribution compatible with the right action. This is the most general notion of "connection" in differential geometry, encompassing both principal and vector-bundle connections as special cases.

> [!tip] Foliations and Bundle Reductions *(from Differential Topology)*
> A flat connection on a principal bundle defines a **foliation** of the total space $P$ by horizontal leaves, and the holonomy of the foliation gives a representation $\pi_1(M) \to G$. The space of flat connections modulo gauge transformations is then the space of conjugacy classes of representations $\pi_1(M) \to G$ — a result going back to **Galois theory in topological form** and central to **flat connections in topology and CFT** (e.g., the moduli space of flat connections on a Riemann surface is symplectic and quantises to give the Hilbert space of Chern-Simons theory).

---
type: definition
subject: geometric-mechanics
prereqs:
  - "Def - Cotangent Space and Cotangent Bundle"
  - "Def - Symplectic Manifold"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Pullback of a Covector Field"
tags: [physics, geometric-mechanics, symplectic-geometry]
---

# Notation

$Q$ is a smooth manifold (the **configuration space**) of dimension $n$; $T^*Q$ is its [[Def - Cotangent Space and Cotangent Bundle|cotangent bundle]] of dimension $2n$ (the **phase space**); $\pi : T^*Q \to Q$ is the natural projection sending a covector $\alpha \in T^*_qQ$ to the base point $q$. In a chart $(U, q^1, \dots, q^n)$ on $Q$, the **canonical (Darboux) coordinates** on $\pi^{-1}(U) \subset T^*Q$ are $(q^1, \dots, q^n, p_1, \dots, p_n)$, where $(p_1, \dots, p_n)$ are the coefficients of a covector with respect to the basis $(dq^1, \dots, dq^n)$ of $T^*_qQ$: a covector $\alpha \in T^*_qQ$ is written $\alpha = p_i\, dq^i$.

**Standing convention.** We use the **sign convention $\omega = -d\theta$** (Frankel, Marsden–Ratiu) rather than $\omega = d\theta$ (Arnold). With this convention $\omega = dp_i \wedge dq^i$ and Hamilton's equations read $\dot q^i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q^i$.

---

# Axiom Motivation

This is **the** canonical example of a symplectic manifold. We want to understand why the cotangent bundle $T^*Q$ of *any* smooth manifold $Q$ — with no extra structure on $Q$ at all, no metric, no connection, no orientation — carries a canonical symplectic form. The construction should use only the smooth structure of $Q$ and the projection $\pi : T^*Q \to Q$. What is it that distinguishes $T^*Q$ from the tangent bundle $TQ$, and why does $T^*Q$ get a canonical symplectic form while $TQ$ does not?

The answer is the **tautological 1-form** $\theta$ on $T^*Q$, a $1$-form constructed canonically out of the projection and the cotangent-space identification, with no auxiliary choice. Its definition is the cleanest piece of category theory in differential geometry: at any point $\alpha \in T^*Q$ (a covector based at $q = \pi(\alpha)$), and any tangent vector $v \in T_\alpha(T^*Q)$, we set

$$\theta_\alpha(v) := \alpha\big(d\pi_\alpha(v)\big).$$

Read this slowly: $\alpha$ is itself a covector on $Q$; $d\pi_\alpha(v) \in T_qQ$ is a tangent vector to $Q$ obtained by pushing $v$ forward along the projection; and $\alpha(d\pi_\alpha(v))$ is a real number, the pairing of a covector with a vector. This is **tautological** because it just says "$\theta$ evaluated on $v$ is the covector $\alpha$ (where we sit) evaluated on the projection of $v$". The name comes from the feeling that we're computing "the covector itself" — we are.

Why does this work only for $T^*Q$, not $TQ$? Because the point of $T^*Q$ above $q$ is *itself* a covector on $Q$, so we can use it to evaluate vectors at $q$. The point of $TQ$ above $q$ is a vector on $Q$, not a covector — it cannot eat tangent vectors. There is no analogous tautological $1$-form on $TQ$, and indeed $TQ$ does not carry a canonical symplectic structure.

In coordinates, the tautological form is $\theta = p_i\, dq^i$, the **Poincaré 1-form**. To verify this from the definition, take $\alpha = p_i(dq^i)_q$ and $v = a^i \partial_{q^i} + b_i \partial_{p_i}$. Then $d\pi_\alpha(v) = a^i\partial_{q^i}$ (the projection forgets the $p$-components), so $\theta_\alpha(v) = \alpha(a^i\partial_{q^i}) = p_i a^i = (p_i dq^i)(v)$ — confirming $\theta = p_i\, dq^i$.

Now we need the symplectic form. We take

$$\omega := -d\theta.$$

By construction $\omega$ is **exact** (it equals $-d\theta$ for the globally-defined $1$-form $\theta$), hence **closed** ($d\omega = -d^2\theta = 0$). In coordinates, $\omega = -d(p_i dq^i) = -dp_i \wedge dq^i = dp_i \wedge dq^i$ (after writing the sum out properly with the antisymmetry of wedge), which is the standard symplectic form on $\mathbb{R}^{2n}$ specialized to one chart. **Nondegeneracy** then follows: the matrix of $\omega$ in the basis $(\partial_{q^i}, \partial_{p_j})$ is the standard symplectic matrix $\begin{pmatrix}0 & I_n \\ -I_n & 0\end{pmatrix}$, which is invertible.

The **sign** in $\omega = -d\theta$ is a convention. Frankel, Marsden–Ratiu, and most modern texts use it because it makes the symplectic form on a single canonical chart come out as $\omega = dp \wedge dq$ rather than $dq \wedge dp$, which in turn makes Hamilton's equations read $\dot q = \partial H/\partial p$ (positive sign on the canonical pairing). Arnold's *Mathematical Methods of Classical Mechanics* uses $\omega = d\theta = dq^i \wedge dp_i$, which flips the sign of the Hamiltonian vector field and of the Poisson bracket. Either convention is internally consistent, but they cannot be mixed.

Why this specific symplectic form rather than some other? **Universality.** The tautological $1$-form has the universal property that for any $1$-form $\beta$ on $Q$ — viewed as a section $s_\beta : Q \to T^*Q$, $q \mapsto \beta_q$ — we have $s_\beta^*\theta = \beta$. That is, **pulling back the tautological form along a section recovers the section**. This is the precise sense in which $\theta$ is "the universal $1$-form on $Q$" living on $T^*Q$. Its exterior derivative is therefore the universal exact $2$-form, and the canonical symplectic form on $T^*Q$ is forced.

What if we did *not* require the symplectic form on $T^*Q$ to be canonical, and allowed extra data? Then any symplectic form whatsoever on $T^*Q$ would do, and the resulting Hamiltonian mechanics would still work as a formalism, but the connection to the configuration-space geometry of $Q$ would be lost. The point of the canonical construction is that the symplectic structure on phase space is **forced** by the smooth structure of configuration space, with no additional input.

---

# The Definition

Let $Q$ be a smooth manifold and let $T^*Q$ be its cotangent bundle, with projection $\pi : T^*Q \to Q$.

**The tautological (Poincaré) 1-form** $\theta \in \Omega^1(T^*Q)$ is defined pointwise by

$$\theta_\alpha(v) := \alpha\big(d\pi_\alpha(v)\big), \qquad \alpha \in T^*Q, \; v \in T_\alpha(T^*Q),$$

where $\alpha$ is regarded both as a point of $T^*Q$ and as a covector on $Q$ at $\pi(\alpha)$, and $d\pi_\alpha : T_\alpha(T^*Q) \to T_{\pi(\alpha)}Q$ is the differential of the projection.

In any chart $(U, q^1, \dots, q^n)$ on $Q$, with the induced canonical coordinates $(q^1, \dots, q^n, p_1, \dots, p_n)$ on $\pi^{-1}(U) \subset T^*Q$,

$$\theta = p_i\, dq^i.$$

**The canonical symplectic form** $\omega \in \Omega^2(T^*Q)$ is defined as

$$\omega := -d\theta.$$

In canonical coordinates,

$$\omega = -d(p_i\, dq^i) = -dp_i \wedge dq^i + p_i\, d(dq^i) = -dp_i \wedge dq^i = dp_i \wedge dq^i,$$

where the last equality flips the wedge order $-dp_i \wedge dq^i = dq^i \wedge dp_i$ — and we choose to write our final answer as $\omega = dp_i \wedge dq^i$ (i.e., $\sum_i dp_i \wedge dq^i$, with the convention of writing the higher-index variable last).

**Properties.** $\omega$ is closed (exact, in fact: $\omega = d(-\theta)$), nondegenerate (matrix is standard symplectic), and $(T^*Q, \omega)$ is therefore a [[Def - Symplectic Manifold|symplectic manifold]] of dimension $2n$. The pair $(\theta, \omega)$ is canonical: it depends only on the smooth structure of $Q$ and on the cotangent-bundle structure, with no auxiliary metric, connection, or orientation.

**Universal property of $\theta$.** For any $1$-form $\beta \in \Omega^1(Q)$, viewed as a smooth section $s_\beta : Q \to T^*Q$, $q \mapsto \beta_q$,

$$s_\beta^* \theta = \beta.$$

That is, the pullback of the tautological form along any section recovers the section. Symbolically, $\theta$ is **the universal $1$-form on $Q$**, with $s_\beta^*$ as the corresponding classifying map.

---

# Categorical / Structural Definition

The construction $Q \rightsquigarrow (T^*Q, \omega)$ is a **functor** from the category of smooth manifolds with diffeomorphisms to the category of symplectic manifolds with symplectomorphisms. A diffeomorphism $f : Q_1 \to Q_2$ induces a lift $\tilde f : T^*Q_1 \to T^*Q_2$ via $\tilde f(\alpha) = (f^{-1})^*\alpha$ (the cotangent push-forward, defined because $f$ is invertible), and this $\tilde f$ is a symplectomorphism: $\tilde f^*\omega_{Q_2} = \omega_{Q_1}$. The proof is direct from the universal property of $\theta$: $\tilde f^*\theta_{Q_2} = \theta_{Q_1}$, so $\tilde f^*\omega_{Q_2} = \tilde f^*(-d\theta_{Q_2}) = -d(\tilde f^*\theta_{Q_2}) = -d\theta_{Q_1} = \omega_{Q_1}$.

So **every diffeomorphism of the configuration space induces a symplectomorphism of phase space**. These are the **point transformations** of classical mechanics — canonical transformations that come from a coordinate change on $Q$.

In the language of universal properties: $\theta$ is the universal $1$-form on $T^*Q$ in the sense that there is a natural bijection
$$\{\text{smooth sections } s : Q \to T^*Q\} = \{1\text{-forms } \beta \in \Omega^1(Q)\}$$
realized by $\beta \mapsto s_\beta$ with inverse $s \mapsto s^*\theta$. The tautological form is the "universal way to evaluate a covector on a tangent vector while remembering the covector's basepoint".

---

# Relate to Other Fields / Compression

The canonical symplectic form on $T^*Q$ is the geometric realization of the **Legendre transform**, which is itself the bridge between Lagrangian mechanics (on $TQ$) and Hamiltonian mechanics (on $T^*Q$). On $TQ$ there is no canonical symplectic structure, but a regular Lagrangian $L : TQ \to \mathbb{R}$ produces one — the pullback of $\omega$ via the Legendre transform $\mathbb{F}L : TQ \to T^*Q$. So Hamiltonian mechanics is in a sense the "universal" formalism, with Lagrangian mechanics being symplectic mechanics on $TQ$ pulled back from $T^*Q$ via a chosen Lagrangian.

From the perspective of fiber bundles, the cotangent bundle is the **universal vector bundle over $Q$ associated to the coframe bundle**, and the canonical $1$-form on it is the **soldering form** of the coframe bundle, restricted to $T^*Q$. This is the perspective of Cartan geometry and gauge theory: many natural bundle constructions over $Q$ come with canonical $1$-forms and curvatures, and the cotangent bundle's tautological $\theta$ is the simplest and most foundational example.

**True name:** the true name of $\theta$ is **"the universal way to remember which covector you are looking at while operating on tangent vectors"** — the operational characterization that lets it produce the symplectic structure $\omega = -d\theta$ by a single application of $d$. The official definition $\theta_\alpha(v) = \alpha(d\pi(v))$ is the minimal precise statement of this.

**True name for $\omega$ on $T^*Q$:** the **exterior derivative of the universal $1$-form**, or equivalently **the unique symplectic form on $T^*Q$ that pulls back any section of $T^*Q$ to its own (extrinsic) derivative**.

---

# Examples / Corollaries

**Is an instance: $T^*\mathbb{R} = \mathbb{R}^2$ with $\omega = dp \wedge dq$.** The simplest phase space, the arena of one-degree-of-freedom mechanics (particle on a line, pendulum after linearization). Coordinates $(q, p)$, tautological form $\theta = p\, dq$, symplectic form $\omega = -d\theta = -dp \wedge dq = dq \wedge dp$ — or, by our convention with the higher-index variable last, $\omega = dp \wedge dq$. (The sign is bookkeeping; the geometry is the same.)

**Is an instance: $T^*S^1 = S^1 \times \mathbb{R}$ with $\omega = dp \wedge d\theta$.** The phase space of a particle on a circle (or a planar pendulum, ignoring the lower equilibrium). $S^1$ has the angle coordinate $\theta$, but it is only defined modulo $2\pi$; the cotangent bundle $T^*S^1$ trivializes globally as $S^1 \times \mathbb{R}$ with the momentum coordinate $p$. The symplectic form $\omega = dp \wedge d\theta$ extends globally despite $\theta$ being only locally defined, because $d\theta$ is a globally defined $1$-form on $S^1$ (it is the volume form on $S^1$, defined intrinsically without picking a starting angle).

**Is an instance: $T^*\mathbb{R}^n = \mathbb{R}^{2n}$ with $\omega = \sum_i dp_i \wedge dq^i$.** The phase space of $n$ degrees of freedom (a single particle in $\mathbb{R}^n$, or $n/3$ particles in $\mathbb{R}^3$). The standard symplectic structure on $\mathbb{R}^{2n}$ is just this canonical structure for $Q = \mathbb{R}^n$.

**Is an instance: $T^*S^2$ with the canonical symplectic form.** The phase space of a pendulum on a sphere, or a particle constrained to a sphere. $S^2$ has no global coordinates, so the symplectic form must be assembled from local coordinates (e.g., spherical $(\theta, \phi)$ with $T^*S^2$ trivializing as $S^2 \times \mathbb{R}^2$ minus the poles).

**Is NOT an instance: $TQ$ with any canonical symplectic form.** The tangent bundle does *not* carry a canonical symplectic structure — there is no analogue of the tautological $1$-form on $TQ$, because the points of $TQ$ are tangent vectors, not covectors, and cannot canonically eat tangent vectors. Symplectic structures on $TQ$ exist (e.g., pulled back from $T^*Q$ via a Riemannian musical isomorphism, or constructed from a Lagrangian via the Legendre transform), but they all require auxiliary data.

**Is NOT an instance: $T^*S^2$ with the "obvious" form on $S^2 \times \mathbb{R}^2$.** Cotangent bundles of non-trivial base manifolds are *globally* nontrivial — $T^*S^2$ is not diffeomorphic to $S^2 \times \mathbb{R}^2$. (Actually, for the rank-$2$ cotangent bundle of the $2$-sphere this is a special case that *does* trivialize as a smooth real vector bundle by the hairy-ball theorem failing in rank $2$; but the symplectic structure is not simply the product.) For higher-rank cotangent bundles (e.g., $T^*S^2$ as a $4$-manifold) the construction is intrinsic and not a product.

**Corollary (every cotangent bundle is canonically symplectic).** With no extra data on $Q$ beyond its smooth structure, $T^*Q$ is symplectic via $(\theta, \omega = -d\theta)$.

**Corollary (exactness of $\omega$).** The canonical symplectic form on $T^*Q$ is exact, $\omega = d(-\theta)$. So $[\omega] = 0 \in H^2_{dR}(T^*Q)$. This is a feature of cotangent bundles, not of general symplectic manifolds — closed symplectic manifolds have $[\omega] \neq 0$, so they are *never* cotangent bundles. The compact orientable surfaces of genus $g \geq 1$ are symplectic but not cotangent bundles.

**Corollary (lift of diffeomorphisms).** Every diffeomorphism $f : Q \to Q'$ lifts canonically to a symplectomorphism $T^*Q \to T^*Q'$ via cotangent pushforward $\tilde f(\alpha) = (f^{-1})^*\alpha$. This is the geometric realization of the **point transformations** of classical mechanics.

**Corollary (zero section is Lagrangian).** The zero section $\{(q, 0) : q \in Q\} \subset T^*Q$ is a [[Def - Lagrangian Submanifold|Lagrangian submanifold]] of dimension $n$. More generally, the graph of any closed $1$-form $\beta$ on $Q$ (i.e., $\{(q, \beta_q) : q \in Q\} \subset T^*Q$) is Lagrangian if and only if $d\beta = 0$.

**Calibration check.** If you can do these three things, you have understood the construction. First, verify the universal property $s_\beta^*\theta = \beta$ for a specific $1$-form (e.g., $\beta = dx$ on $\mathbb{R}$ with $T^*\mathbb{R} = \mathbb{R}^2$). Second, compute the tautological $1$-form on $T^*S^1$ in the angle coordinate, and check $\omega = dp \wedge d\theta$. Third, verify that the zero section of $T^*Q$ for $Q$ of dimension $n$ is Lagrangian, by checking it has the right dimension and that $\theta$ (hence $\omega$) restricts to zero on it.

---

# Unlocked by This

> [!tip] Generating Functions for Canonical Transformations *(from Hamilton–Jacobi Theory)*
> Given two cotangent bundles $T^*Q_1, T^*Q_2$ and a smooth function $S : Q_1 \times Q_2 \to \mathbb{R}$ (the **generating function**) such that the equations $p_i^{(1)} = \partial S/\partial q^i_{(1)}$, $p_i^{(2)} = -\partial S/\partial q^i_{(2)}$ implicitly define a smooth map $\varphi_S : T^*Q_1 \to T^*Q_2$, this map is automatically a symplectomorphism. In the limit $Q_1 = Q_2$ and $\varphi$ approaching the identity, $S$ becomes the generating function of the Hamiltonian flow itself, and the equation it satisfies is the **Hamilton–Jacobi equation** $\partial S/\partial t + H(q, \partial S/\partial q) = 0$. Generating functions are the practical computational tool for canonical transformations, and they connect classical mechanics to the WKB approximation of quantum mechanics: $\psi(q) \approx e^{iS(q)/\hbar}$ in the semiclassical limit.

> [!tip] Symplectic Reduction by a Lie Group Action *(from Geometric Mechanics II)*
> When a Lie group $G$ acts on $Q$, it lifts to a Hamiltonian action on $T^*Q$, with **moment map** $\mu : T^*Q \to \mathfrak{g}^*$ given by $\mu(q, p)(\xi) = p(\xi_Q(q))$, where $\xi_Q$ is the infinitesimal generator of $\xi \in \mathfrak{g}$ on $Q$. The **Marsden–Weinstein quotient** $T^*Q//_\mu G = \mu^{-1}(0)/G$ is then a smaller symplectic manifold capturing the reduced dynamics. For $Q = \mathbb{R}^3 \setminus \{0\}$ and $G = SO(3)$ acting by rotations, this reduces the Kepler problem to a $2$-dimensional symplectic problem on which the dynamics is integrable.

> [!tip] The Lagrangian Grassmannian of $T^*Q$ *(from Microlocal Analysis)*
> The set of all Lagrangian submanifolds of $(T^*Q, \omega)$ is a vast space, and important sub-classes include: graphs of closed $1$-forms (the "horizontal" Lagrangians), cotangent fibres $T^*_qQ$ (the "vertical" Lagrangians), and conormal bundles $N^*S \subset T^*Q$ of submanifolds $S \subset Q$. Lagrangians serve as the **classical analogues of quantum states**: in microlocal analysis, a quantum state can be modelled by a Lagrangian in $T^*Q$ via its wavefront set, with the WKB ansatz $\psi(q) = a(q)e^{iS(q)/\hbar}$ producing the Lagrangian $\{(q, dS(q))\}$. The wavefront set and the Maslov class are the geometric refinements of this story.

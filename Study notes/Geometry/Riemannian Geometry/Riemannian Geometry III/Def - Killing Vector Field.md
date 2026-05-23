---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Vector Field on a Manifold"
  - "Def - Isometry of Riemannian Manifolds"
  - "Def - Levi-Civita Connection"
tags: [geometry, riemannian-geometry, symmetry]
---

# Notation

$(M, g)$ is a Riemannian manifold. $\mathcal{L}_X$ is the **Lie derivative** along the vector field $X$, characterised by $(\mathcal{L}_X T)|_p = (d/dt)|_{t=0}\phi_t^* T$ where $\phi_t$ is the flow of $X$. For a $(0, 2)$-tensor $g$,

$$(\mathcal{L}_X g)(Y, Z) = X\langle Y, Z\rangle - \langle [X, Y], Z\rangle - \langle Y, [X, Z]\rangle.$$

A vector field $X$ is **Killing** if $\mathcal{L}_X g = 0$. The Killing fields form a finite-dimensional Lie algebra $\mathfrak{iso}(M, g)$ under the Lie bracket of vector fields.

---

# Axiom Motivation

We want to characterise the **infinitesimal isometries** of a Riemannian manifold: vector fields whose flow consists of isometries. The desideratum is intrinsic — we want a local condition on $X$ that is equivalent to "the flow of $X$ preserves the metric," without reference to the global flow itself.

The cleanest formulation is via the Lie derivative. The metric $g$ is a $(0, 2)$-tensor, and an isometry is a diffeomorphism with $\phi^* g = g$. If $\phi_t$ is the flow of $X$, then $\phi_t$ is an isometry for all $t$ if and only if $\phi_t^* g = g$ for all $t$, equivalently $(d/dt)\phi_t^* g = 0$. By the definition of the Lie derivative, this is exactly $\mathcal{L}_X g = 0$. So **$X$ is Killing $\iff$ the flow of $X$ is by isometries**.

The next question: how do we compute $\mathcal{L}_X g$ in terms of more familiar objects? Using the [[Def - Levi-Civita Connection|Levi-Civita connection]], one finds

$$(\mathcal{L}_X g)(Y, Z) = \langle \nabla_Y X, Z\rangle + \langle Y, \nabla_Z X\rangle = (\nabla_Y X^\flat)(Z) + (\nabla_Z X^\flat)(Y),$$

where $X^\flat = g(X, \cdot)$ is the $1$-form dual to $X$. So the Killing equation becomes

$$\nabla_a X_b + \nabla_b X_a = 0,$$

i.e., **the symmetric part of $\nabla X$ (as a $(0, 2)$-tensor) vanishes**, equivalently, $\nabla X$ is **skew-symmetric**.

This is the operationally useful form. Skew-symmetry of $\nabla X$ is a *pointwise* algebraic condition on a $(0, 2)$-tensor at each point — much easier to check than the integral condition "the flow preserves $g$." And it makes the parallels with mechanics transparent: $X$ generates a continuous symmetry, $\nabla X$ skew means "rotation-like infinitesimal motion."

Why this specific form and not, say, $\nabla X = 0$ (parallel vector fields)? Parallel vector fields are a *much* stronger condition — they would force the manifold to have a parallel direction, which restricts to very special Riemannian geometries. Killing vector fields are the weakest meaningful symmetry condition; they exist generically on symmetric spaces and on any manifold with a continuous isometry group.

How many Killing fields can there be? At any point $p$, a Killing field $X$ is determined by $X(p)$ and $\nabla X(p)$ (a skew $(0, 2)$-tensor, equivalently an element of $\mathfrak{o}(T_pM)$): the higher derivatives are determined by these data via second-order ODEs derived from the Killing equation. So the dimension of the Killing algebra is at most $n + n(n-1)/2 = n(n+1)/2$. This maximum is attained exactly by manifolds of constant sectional curvature — the **isotropic** Riemannian manifolds.

---

# The Definition

> **Definition (Killing vector field).** A smooth vector field $X$ on a Riemannian manifold $(M, g)$ is a **Killing vector field** if $\mathcal{L}_X g = 0$ — equivalently, if the flow of $X$ consists of [[Def - Isometry of Riemannian Manifolds|isometries]] of $(M, g)$.
>
> Equivalent characterisations (proved in [[Thm - Killing Equation]]):
>
> 1. $\nabla_a X_b + \nabla_b X_a = 0$ (Killing's equation).
> 2. $\nabla X$ is skew-symmetric as a $(0, 2)$-tensor: $\langle \nabla_Y X, Z\rangle = -\langle Y, \nabla_Z X\rangle$ for all $Y, Z$.
> 3. The flow $\phi_t$ of $X$ satisfies $\phi_t^* g = g$ for all $t$ in its domain.

The set of Killing fields on $(M, g)$ is a Lie algebra under the Lie bracket of vector fields, denoted $\mathfrak{iso}(M, g)$. Its dimension is at most $n(n+1)/2$, attained exactly when $(M, g)$ has constant sectional curvature.

---

# Categorical / Structural Definition

The Killing algebra $\mathfrak{iso}(M, g)$ is the Lie algebra of the **isometry group** $\mathrm{Iso}(M, g)$, a finite-dimensional Lie group acting smoothly on $M$ by the **Myers–Steenrod theorem** (every isometry of a Riemannian manifold is automatically smooth, and $\mathrm{Iso}(M, g)$ is a Lie group of dimension at most $n(n+1)/2$). So:

$$\mathfrak{iso}(M, g) = \mathrm{Lie}(\mathrm{Iso}(M, g)).$$

This makes Killing fields the **infinitesimal generators** of the isometry group, exactly as left-invariant vector fields are generators of left translations on a Lie group. Every continuous symmetry of a Riemannian manifold integrates to a $1$-parameter group of isometries, and every such $1$-parameter group is generated by a Killing field.

When $\mathrm{Iso}(M, g)$ acts transitively, $M$ is a **homogeneous Riemannian manifold** — there is essentially one Riemannian geometry "view" from every point. When the stabiliser at a point is also the full $\mathrm{O}(n)$, $M$ is **isotropic** (no preferred direction) and necessarily has constant sectional curvature.

---

# Relate to Other Fields / Compression

In **general relativity**, the timelike Killing field of a stationary spacetime defines **energy conservation** for geodesics: if $\partial_t$ is timelike Killing in Schwarzschild, then $E = -\langle \partial_t, T\rangle$ is the conserved energy of a geodesic with tangent $T$. The axial Killing field gives angular-momentum conservation. The existence of enough Killing fields is what makes Schwarzschild geodesic motion integrable in closed form. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

In **mechanics**, the Killing equation is **Noether's theorem in geometric form**: a continuous symmetry of the metric ($\mathcal{L}_X g = 0$) implies a conserved quantity along geodesics ($\langle X, T\rangle$ constant). This generalises to the **momentum map** for Hamiltonian group actions on symplectic manifolds — see [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

In **representation theory**, Killing fields on a Lie group with bi-invariant metric form a Lie algebra isomorphic to two copies of the group's Lie algebra (left- and right-invariant fields). This is the **Lie-algebraic** view of bi-invariant geometry on Lie groups.

**True name:** *A Killing field is the infinitesimal generator of a $1$-parameter group of isometries. Operationally, it is a vector field whose covariant derivative is skew-symmetric: $\nabla X \in \mathfrak{o}(TM)$ at each point.* The skew-symmetry characterisation is the most useful for verification and for theorems — it makes Killing fields the geometric analogues of harmonic forms and the natural targets for the Bochner technique.

---

# Examples / Corollaries

**Example 1 (Killing fields on Euclidean space).** On $\mathbb{R}^n$ with the flat metric, the Killing fields are linear combinations of constant vector fields $\partial_i$ (translations) and "rotation generators" $x^j \partial_i - x^i \partial_j$ (rotations in coordinate planes). Total dimension: $n + \binom{n}{2} = n(n+1)/2$ — the maximum, since $\mathbb{R}^n$ has constant curvature $0$.

**Example 2 (Killing fields on $S^n$).** The Killing fields on the round $n$-sphere come from the action of $\mathrm{SO}(n+1)$ by rotations of the ambient $\mathbb{R}^{n+1}$. For each skew-symmetric matrix $A \in \mathfrak{so}(n+1)$, the vector field $X_A(p) := Ap$ (restricted to $S^n$) is Killing. The Killing algebra is $\mathfrak{so}(n+1)$, of dimension $n(n+1)/2$ — again the maximum, since $S^n$ has constant curvature $1$. See [[Ex - Killing Fields on the Sphere from SO(n+1)]].

**Example 3 (Killing fields on Schwarzschild).** The Schwarzschild spacetime $(M, g) = (\mathbb{R} \times (2M, \infty) \times S^2, g)$ has the timelike Killing field $\partial_t$ (the spacetime is stationary) and three rotational Killing fields generating the $\mathrm{SO}(3)$ action on the $S^2$ factor. Total: $4$ Killing fields in a $4$-manifold, so the isometry group has dimension $4$. This is far from the maximum $10$, reflecting that Schwarzschild is not maximally symmetric (it is not de Sitter).

**Example 4 (Killing field that fails to be parallel).** On $S^2$, the rotation Killing field $X(\theta, \varphi) = \partial_\varphi$ is *not* parallel — its norm varies ($|X| = \sin\theta$ vanishes at the poles). Killing $\ne$ parallel; a Killing field on a non-flat manifold typically has nonconstant norm.

**Non-example.** The "radial vector field" $X(r, \theta, \varphi) = r\partial_r$ on $\mathbb{R}^3$ is **not** Killing: $\mathcal{L}_X g \ne 0$ (its flow is scaling, which dilates the metric by an overall factor). It is a **conformal Killing field** instead — it satisfies $\mathcal{L}_X g = 2g$.

**Calibration check.** If you have understood this definition correctly you should be able to: (a) verify directly that translations and rotations on $\mathbb{R}^n$ are Killing; (b) compute $\mathcal{L}_X g$ for the rotation $X = -y\partial_x + x\partial_y$ on $\mathbb{R}^2$ and confirm it vanishes; (c) state the Killing equation $\nabla_a X_b + \nabla_b X_a = 0$ in both index and covariant-derivative form; (d) explain why $\dim \mathfrak{iso}(M, g) \le n(n+1)/2$ from the determination of $X$ by $(X(p), \nabla X(p))$ at a point.

---

# Unlocked by This

> [!tip] Noether's Theorem for Geodesics *(from Riemannian Geometry / Geometric Mechanics)*
> If $X$ is a Killing field and $\gamma$ is a geodesic with tangent $T$, then $\langle X, T\rangle$ is constant along $\gamma$. Proof: $\nabla_T \langle X, T\rangle = \langle \nabla_T X, T\rangle + \langle X, \nabla_T T\rangle = \langle \nabla_T X, T\rangle$ (using $\nabla_T T = 0$ for geodesics) $= 0$ by skew-symmetry of $\nabla X$. This is the cleanest geometric form of Noether's theorem.

> [!tip] Momentum Map and Symplectic Reduction *(from Geometric Mechanics)*
> The Killing-field formalism generalises to **momentum maps** for Hamiltonian group actions on symplectic manifolds. The conserved quantity $\langle X, T\rangle$ along a geodesic generalises to a $\mathfrak{g}^*$-valued conserved quantity $\mu: M \to \mathfrak{g}^*$ along any Hamiltonian flow, and the **Marsden–Weinstein symplectic reduction** theorem reduces the system by quotienting out the symmetry. See [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

> [!tip] Bochner Vanishing for Killing Fields *(from Hodge Theory)*
> On a compact Riemannian manifold with $\mathrm{Ric} < 0$, there are no nontrivial Killing fields. Proof via the **Bochner formula**: integrating $\tfrac{1}{2}\Delta|X|^2 = |\nabla X|^2 + \mathrm{Ric}(X, X)$ over $M$ kills the left side, leaving $0 = \int |\nabla X|^2 + \int \mathrm{Ric}(X, X)$; both terms have the wrong sign under $\mathrm{Ric} < 0$, so they vanish individually, forcing $X = 0$. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

> [!tip] Isometry Group is a Lie Group (Myers–Steenrod) *(from Lie Group Theory)*
> **Myers–Steenrod theorem**: the isometry group $\mathrm{Iso}(M, g)$ of any Riemannian manifold is a finite-dimensional Lie group acting smoothly, of dimension at most $n(n+1)/2$. The Killing algebra $\mathfrak{iso}(M, g)$ is its Lie algebra. This connects Riemannian geometry to [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie group theory]] and is the foundation of **homogeneous Riemannian geometry**.

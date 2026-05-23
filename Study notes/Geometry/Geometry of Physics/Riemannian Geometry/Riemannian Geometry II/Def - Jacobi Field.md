---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Geodesic"
  - "Def - The Riemannian Exponential Map"
tags: [geometry, riemannian-geometry, jacobi-fields, curvature]
---

# Notation

$(M, g)$ a Riemannian manifold, $\gamma : I \to M$ a [[Def - Geodesic|geodesic]], $T := \dot\gamma$ its velocity field. For a vector field $J$ along $\gamma$, $J' := \nabla_T J$ is the covariant derivative along $\gamma$ and $J'' := \nabla_T \nabla_T J$. The Riemann curvature tensor is $R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$ (see [[Riemannian Geometry III — Riemann Curvature and Topology]]). $T^\perp$ denotes the orthogonal complement of $T$ in $T_{\gamma(t)}M$. The full registry lives at [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Axiom Motivation

The motivating question is: **how do nearby geodesics behave relative to a given geodesic, to first order?** We have $\gamma$, fixed. We perturb it by a one-parameter family $\gamma_s$ of nearby geodesics, with $\gamma_0 = \gamma$. The variation field
$$J(t) := \frac{\partial}{\partial s}\bigg|_{s=0} \gamma_s(t)$$
is a vector field along $\gamma$ that captures "the first-order separation of $\gamma_s$ from $\gamma$". What equation does $J$ satisfy?

To find out, we use the fact that *each $\gamma_s$ is a geodesic*: $\nabla_{\partial_t \gamma_s} \partial_t \gamma_s = 0$ for all $s$. Differentiate this with respect to $s$ at $s = 0$. After swapping $\nabla_{\partial_s}$ and $\nabla_{\partial_t}$ using the curvature tensor (the curvature is *exactly* the obstruction to commuting covariant derivatives), and using $[\partial_s, \partial_t] = 0$ (since they are coordinate vector fields on the variation surface), we get
$$\nabla_T \nabla_T J + R(J, T) T = 0.$$
This is the **Jacobi equation**, and any vector field satisfying it is a **Jacobi field**.

So the Jacobi equation is not an ad hoc definition — it is *forced* on us by the question "what is the linearisation of the geodesic equation around a fixed geodesic?". It is the geodesic equation's *equation of variations*, in exactly the sense that a linearised ODE captures first-order perturbations of solutions to the nonlinear ODE.

The role of curvature is the striking feature. The Jacobi equation is a second-order linear ODE for $J$, of the form $J'' + R(\cdot, T)T \cdot J = 0$, with the curvature tensor acting as the "potential". Where the curvature is positive (e.g., on a sphere), the curvature term is a positive-definite "spring": Jacobi fields oscillate, and nearby geodesics initially separating converge back, eventually meeting at a conjugate point. Where the curvature is negative (hyperbolic space), the curvature term acts like an inverted spring: Jacobi fields grow exponentially, and nearby geodesics separate without bound. Where the curvature is zero (Euclidean space), $J'' = 0$ and Jacobi fields are linear in $t$ — neither converging nor diverging. **The sign of curvature is the sign of the focusing/defocusing of nearby geodesics**, and the Jacobi equation is the precise mathematical statement of this.

Why $R(J, T)T$ and not, say, $R(T, J)T$ or some other index ordering? It comes out of the derivation: differentiating $\nabla_T T = 0$ with respect to $s$ gives, after the curvature identity $\nabla_T \nabla_S T - \nabla_S \nabla_T T = R(T, S) T$ (which is a special case of the general curvature definition with $[T, S] = 0$), the equation $\nabla_T \nabla_T S + R(S, T) T = 0$ where $S = \partial_s \gamma$ is just $J$. The signs and the index placement are forced. The shorthand $R(J, T)T \in T_{\gamma(t)}M$ unfolds as: take the (1,3)-curvature tensor, plug in $J$ and $T$ for the first two arguments (i.e. consider the curvature transformation $R(J, T) : T_pM \to T_pM$), then apply it to $T$.

A subtler question is **which Jacobi fields arise as variations of geodesics?** The answer is: *all of them*. Given any initial data $(J(0), J'(0)) \in T_pM \times T_pM$, there is a one-parameter family $\gamma_s$ of geodesics with $\gamma_0 = \gamma$ whose variation field $J$ has these initial values. The construction: take $\gamma_s(t) := \exp_p((1 + s\, a)(v + s b\, t))$ for appropriate $a, b$ — or more simply, fix $\gamma_s(t) := \exp_{\gamma_s(0)}(t\, \dot\gamma_s(0))$ where $\gamma_s(0), \dot\gamma_s(0)$ are chosen so that the resulting $J(0) = J_0$ and $J'(0) = J'_0$ are the prescribed data. So the space of Jacobi fields along $\gamma$ is exactly $T_pM \times T_pM$, dimension $2n$ — matching the dimension of the second-order linear ODE.

A useful split: **tangential vs normal Jacobi fields**. A Jacobi field $J$ that is parallel to $T$ (i.e. $J = f(t) T$ for some scalar function $f$) corresponds to varying the *parametrisation* of $\gamma$ or its initial speed — it does not represent a "geometric" variation of the geodesic image. Substituting $J = f T$ into the Jacobi equation gives $f'' T = 0$ (since $R(T, T) T = 0$ by antisymmetry of $R(\cdot, \cdot)$), so $f$ is linear in $t$: $J = (a + bt) T$. Tangential Jacobi fields are therefore a $2$-dimensional subspace of the $2n$-dimensional space of Jacobi fields. The remaining $2(n-1)$ dimensions are the **normal Jacobi fields**, $J \perp T$, which capture the "actual" geometric variation transverse to $\gamma$. For the index form and conjugate points, only normal Jacobi fields matter.

---

# The Definition

Let $\gamma : I \to M$ be a [[Def - Geodesic|geodesic]] on a Riemannian manifold $(M, g)$. A **Jacobi field** along $\gamma$ is a smooth vector field $J$ along $\gamma$ satisfying the **Jacobi equation**
$$\nabla_{\dot\gamma}\nabla_{\dot\gamma} J + R(J, \dot\gamma)\dot\gamma = 0,$$
where $R$ is the Riemann curvature tensor. Writing $T = \dot\gamma$ and $J' = \nabla_T J$, $J'' = \nabla_T \nabla_T J$, the equation reads
$$J'' + R(J, T) T = 0.$$

**Existence and dimension.** The Jacobi equation is a second-order linear ODE for $J$, so by Picard–Lindelöf, for any prescribed initial data $J(0) \in T_{\gamma(0)} M$ and $J'(0) \in T_{\gamma(0)} M$ there exists a unique Jacobi field along $\gamma$ with these initial values. The space of Jacobi fields along $\gamma$ is thus a vector space of dimension $2n$ (where $n = \dim M$).

**Variational characterisation.** Equivalently, $J$ is a Jacobi field iff $J(t) = \frac{\partial}{\partial s}\big|_{s=0} \gamma_s(t)$ for some smooth one-parameter family $\gamma_s$ of geodesics with $\gamma_0 = \gamma$. Both characterisations give the same vector fields.

**Tangential decomposition.** Every Jacobi field $J$ decomposes uniquely as $J = J^\parallel + J^\perp$ with $J^\parallel = (a + bt)\, T$ tangent to $\gamma$ (the *tangential* part, a $2$-dimensional space corresponding to affine reparametrisation) and $J^\perp \perp T$ everywhere (the *normal* part, a $2(n-1)$-dimensional space corresponding to genuine geometric variation).

**Relation to the exponential map.** If $\gamma = \gamma_v$ with $\gamma_v(0) = p$, then for $w \in T_pM$ the Jacobi field along $\gamma_v$ with $J(0) = 0$ and $J'(0) = w$ is
$$J(t) = d(\exp_p)_{tv}(tw).$$
So Jacobi fields with $J(0) = 0$ are exactly the *radial* derivatives of the exponential map; this is the link by which conjugate points (where $J(t) = 0$) detect failures of $\exp_p$ to be a local diffeomorphism.

---

# Relate to Other Fields / Compression

**True name:** **the linearisation of the geodesic equation around $\gamma$**. The Jacobi equation is the equation of variations of the geodesic flow — what you would call the "linearised dynamics" in dynamical-systems language. Trigger: whenever you have geodesics and want to talk about *nearby* geodesics, the Jacobi equation is the right tool.

**The Jacobi equation is the kernel of the second variation of energy.** The bilinear form $I(V, W) = \int g(V', W') - g(R(V, T)T, W)\, dt$ on variation fields along a geodesic has, as its kernel on the space of fields vanishing at the endpoints, exactly the Jacobi fields vanishing at the endpoints. This is the variational characterisation: a variation field is in the null direction of the second variation iff it satisfies the Jacobi equation. See [[Def - The Index Form]] and [[Thm - Second Variation of Arc Length]].

**Jacobi fields are the obstruction to $\exp_p$ being a local diffeomorphism.** $d(\exp_p)_v$ fails to be invertible at $v$ iff there is a nonzero $w \in T_pM$ with $d(\exp_p)_v(w) = 0$ iff there is a nonzero Jacobi field along $\gamma_v$ vanishing at $0$ and at $1$ iff $\exp_p(v)$ is conjugate to $p$ along $\gamma_v$. This identifies conjugate points (Jacobi-equation language) with singularities of $\exp_p$ (differential-map language).

**Connection to the Hamiltonian formalism.** In the [[Def - Hamiltonian Flow of the Kinetic Energy|Hamiltonian formulation]] of geodesic flow on $T^*M$, the linearisation of the Hamiltonian vector field at a geodesic gives a second-order linear system equivalent to the Jacobi equation. The eigenvalues of this linearised system govern stability of the geodesic — in symplectic-geometry language, *Krein signatures* and *Maslov indices* refine the Morse index.

---

# Examples / Corollaries

**Is an instance: Euclidean space.** With curvature $R = 0$, the Jacobi equation is $J'' = 0$, so $J(t) = J(0) + t J'(0)$. Jacobi fields are linear (affine) vector fields. Conjugate points never occur: $J(t) = 0$ only if $J(0) = 0$ and $J'(0) = 0$, i.e. $J \equiv 0$. This matches: $\exp_p$ on Euclidean space is the identity, with no singular points.

**Is an instance: the round sphere $S^n$ of radius $1$.** On a unit-speed geodesic, with normal Jacobi field $J = f(t) E$ for a parallel unit normal vector field $E$, the Jacobi equation reduces to $f'' + f = 0$ — see [[Ex - Jacobi Fields on a Sphere are Sinusoidal]]. Solutions are $f(t) = a \cos t + b \sin t$. The Jacobi field with $J(0) = 0$ and $J'(0) = w$ is $J(t) = \sin(t)\, w$ (parallel-transported), and it returns to zero at $t = \pi$ — the antipode is conjugate to $p$ along every great circle.

**Is an instance: hyperbolic space.** With sectional curvature $K = -1$, the Jacobi equation on normal fields becomes $f'' - f = 0$ with solutions $\sinh t$ and $\cosh t$. Jacobi fields grow exponentially — no conjugate points ever occur, and $\exp_p$ is a diffeomorphism $T_p\mathbb{H}^n \to \mathbb{H}^n$.

**Is an instance: tangential Jacobi fields are always linear.** Even on a curved manifold, the Jacobi field $J = (a + bt) T$ along any geodesic satisfies the equation: $J'' = 0$ (since $T' = 0$), and $R(J, T)T = (a+bt) R(T, T) T = 0$ by antisymmetry of $R$. So the tangential Jacobi fields are the "trivial" linear ones in any geometry; only normal Jacobi fields see the curvature.

**Is an instance: the Jacobi field on a Lie group with bi-invariant metric.** For a geodesic $\gamma(t) = \exp(tX)$ (a one-parameter subgroup), the normal Jacobi fields along $\gamma$ are governed by the Lie algebra structure: writing $J(t) = (\exp(tX))_* Y(t)$ for left-translated fields, the Jacobi equation becomes $Y'' + \tfrac14 [X, [X, Y]] = 0$ — the curvature $R(Y, X)X$ being equal to $\tfrac14 [X, [X, Y]]$ on a bi-invariant metric. Conjugate points along $\gamma$ are determined by the eigenvalues of $\mathrm{ad}_X^2$ on the orthogonal complement of $X$.

**Is NOT an instance: a non-Jacobi variation field.** Take a geodesic $\gamma$ and a vector field $V$ along $\gamma$ that does not satisfy the Jacobi equation — e.g., a constant non-parallel field on a curved manifold. Then $V$ is *not* a Jacobi field, even though it is a perfectly good vector field along $\gamma$. Such $V$ does not arise from a geodesic variation, only from variations through *non*-geodesic curves; it gives a nonzero second variation $I(V, V)$.

**Corollary (dimension count).** The space of Jacobi fields along a geodesic $\gamma$ is $2n$-dimensional, parametrised by $(J(0), J'(0)) \in T_{\gamma(0)}M \oplus T_{\gamma(0)}M$. *Calibration check:* this is the standard fact about second-order linear ODE systems, applied to the Jacobi equation in components after parallel-transporting an orthonormal frame.

**Corollary (normal subspace is invariant).** If $J$ is a Jacobi field with $J(t_0), J'(t_0) \perp T$ at some $t_0$, then $J(t) \perp T$ for all $t$. *Calibration check:* compute $\frac{d^2}{dt^2}g(J, T) = g(J'', T) + 0 = -g(R(J, T)T, T) = 0$ by antisymmetry of $R$ in the first two arguments — so $g(J, T)$ is linear in $t$, and if it and its derivative vanish at one point they vanish identically.

**Corollary (conjugate points are isolated).** Along a geodesic, the parameters $t_0 > 0$ at which the Jacobi field with $J(0) = 0$ has $J(t_0) = 0$ form a discrete set (no accumulation points). *Calibration check:* this follows from the ODE structure — analytic solutions of second-order linear ODEs have isolated zeros (after dividing by the highest power of $t - t_0$ that divides the solution).

**Corollary (Jacobi field formula via $\exp_p$).** If $J$ is the Jacobi field along $\gamma_v$ with $J(0) = 0$ and $J'(0) = w$, then $J(t) = d(\exp_p)_{tv}(tw)$. *Calibration check:* compute $d(\exp_p)_{tv}(tw)$ as the variation of $\gamma_{v + sw}(t)$ in $s$ at $s = 0$, which is exactly the variation through nearby geodesics, hence the Jacobi field.

**Calibration check.** If you can verify (a) that on a flat manifold Jacobi fields are linear in $t$, (b) that on a positively-curved manifold (sphere) normal Jacobi fields oscillate and conjugate points appear, and (c) that the radial differential $d(\exp_p)_{tv}(tw)$ is a Jacobi field with $J(0) = 0$ — then you have understood the definition.

---

# Unlocked by This

> [!tip] Conjugate Points and the Failure of $\exp_p$ to Be a Local Diffeo *(from Riemannian Geometry)*
> Conjugate points are exactly the values of $t$ at which the Jacobi field with $J(0) = 0$ returns to zero, and they are *precisely* the values at which $\exp_p$ ceases to be a local diffeomorphism along $\gamma_v$. See [[Def - Conjugate Point]] and [[Thm - Jacobi Equation and Conjugate Points]].

> [!tip] Rauch's Comparison Theorem *(from Riemannian Geometry)*
> Sturm-comparison applied to the Jacobi equation: if sectional curvature on $M$ satisfies $K \leq K_0$ everywhere, then Jacobi fields on $M$ grow at *least* as fast as Jacobi fields on the model space of constant curvature $K_0$. From this comes the **Rauch comparison theorem**, the foundational result of comparison geometry — and from Rauch flow all the global theorems (Bonnet–Myers, Cartan–Hadamard, Toponogov). See [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] **The Morse Index Theorem** *(from Geometric Analysis)*
> The Hessian of the energy functional at a geodesic $\gamma$ is the **index form** $I(V, V) = \int g(V', V') - g(R(V, T) T, V)$. The **index** (dimension of a maximal negative-definite subspace) equals the number of conjugate points to $p$ in the interior of $\gamma$, counted with multiplicity — this is the **Morse Index Theorem**. It is the prototype of all later Morse-theoretic counting theorems for geodesics, harmonic maps, and Yang–Mills connections.

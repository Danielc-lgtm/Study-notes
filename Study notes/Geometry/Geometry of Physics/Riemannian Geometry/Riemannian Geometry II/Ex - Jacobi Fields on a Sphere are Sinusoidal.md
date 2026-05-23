---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Jacobi Field"
  - "Ex - Great Circles are the Geodesics of the Sphere"
  - "Thm - Jacobi Equation and Conjugate Points"
tags: [geometry, riemannian-geometry, jacobi-fields, sphere]
---

# Problem Statement

Let $(S^n, g)$ be the unit $n$-sphere with the round metric, and let $\gamma : \mathbb{R} \to S^n$ be a unit-speed [[Def - Geodesic|geodesic]] (a great-circle parametrisation). Let $E$ be a parallel unit normal vector field along $\gamma$ (i.e., $E(t) \in T_{\gamma(t)} S^n$ with $|E| = 1$, $E \perp \dot\gamma$, and $\nabla_{\dot\gamma} E = 0$).

(a) Show that any [[Def - Jacobi Field|Jacobi field]] $J(t) = f(t)\, E(t)$ along $\gamma$ that is parallel to $E$ (i.e., a pure-$E$ component) satisfies the scalar ODE
$$f'' + f = 0.$$

(b) Conclude that the *normal* Jacobi fields along $\gamma$ are linear combinations of $\sin t$ and $\cos t$ (in each parallel direction $E$).

(c) Identify the Jacobi field with initial conditions $J(0) = 0, J'(0) = E(0)$.

**Recall:**

A [[Def - Jacobi Field|Jacobi field]] $J$ along a geodesic $\gamma$ satisfies $J'' + R(J, T)T = 0$, where $T = \dot\gamma$, $J' = \nabla_T J$, $J'' = \nabla_T \nabla_T J$, and $R$ is the Riemann curvature tensor.

On the unit sphere $S^n$, the sectional curvature is $1$ for every 2-plane. The Riemann curvature operator in a parallel orthonormal frame is $R(X, T)T = X$ for any $X \perp T$ — i.e., the *identity* operator on $T^\perp$.

A **parallel vector field** $E$ along $\gamma$ satisfies $\nabla_T E = 0$ — its covariant derivative vanishes.

---

# Convergent Strategy

**Problem class:** Reducing the Jacobi equation on a specific manifold (the sphere) to a scalar ODE and solving it. This is in the [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles#Problem-Solving Strategy|"find the Jacobi fields along a given geodesic"]] class — typically solvable explicitly on homogeneous spaces by parallel-transporting an orthonormal frame and reducing to a constant-coefficient ODE.

**Assumption pattern:** $S^n$ has constant sectional curvature $1$. The curvature operator $R(\cdot, T)T$ on the orthogonal complement $T^\perp$ is simply the identity (since the sectional curvature in *every* 2-plane through $T$ is $1$). So when we expand the Jacobi equation in a parallel-transported orthonormal frame, the coefficient matrix is the identity, decoupling the equation into independent scalar Sturm–Liouville equations.

**Theorem routing:** Three steps. **First**, parallel-transport the unit vector $E(0)$ along $\gamma$ to get a parallel unit field $E(t)$ (this exists by the existence theorem for parallel transport, which is an ODE for a vector field). **Second**, write $J(t) = f(t)E(t)$ and compute $J''$ using $\nabla_T E = 0$, getting $J'' = f''(t)E(t)$. **Third**, compute $R(J, T)T = R(fE, T)T = f \cdot R(E, T)T = f \cdot E$ (using sectional curvature $= 1$). The Jacobi equation becomes $f'' E + f E = 0$, so $f'' + f = 0$.

**Key decision point:** The choice of *parallel-transported* frame is crucial. Without parallel transport, the Jacobi equation would have additional terms from $\nabla_T E \neq 0$. Parallel transport eliminates these, leaving a pure scalar ODE.

---

# Legal Operations Used

1. **Operation 8 from the topic page (solve the Jacobi equation along $\gamma$).** Parallel-transport an orthonormal frame, expand $J$ in it, the equation becomes a scalar ODE in each component.

2. **Operation 5 from the topic page (use normal coordinates at one point).** Not directly used, but the parallel-frame argument is the on-curve analogue: by choosing a parallel frame, we kill the connection terms along $\gamma$.

3. **The sectional curvature is the identity on $T^\perp$ (specific to $S^n$).** Used implicitly: on a constant-curvature-$K$ manifold, $R(X, T)T = K \cdot X$ for $X \perp T$, decoupling the Jacobi equation into independent scalar equations $f_i'' + K f_i = 0$.

---

# Hints

> [!note]- Hint 1
> Parallel-transport an orthonormal basis of $(T\dot\gamma)^\perp$ along $\gamma$. In this parallel frame, what does the Jacobi equation become?

> [!note]- Hint 2
> Write $J(t) = f(t) E(t)$ with $E$ parallel, so $\nabla_T E = 0$. Compute $J' = \nabla_T J = f' E + f \nabla_T E = f' E$. Compute $J''$ similarly.

> [!note]- Hint 3
> On $S^n$, what is $R(E, T)T$ when $E \perp T$ and $E, T$ are both unit vectors? Use the formula for sectional curvature in terms of $R$: $K(\sigma) = g(R(e_1, e_2)e_2, e_1)$ for an orthonormal basis $(e_1, e_2)$ of the 2-plane $\sigma$.

> [!note]- Hint 4
> Once the scalar equation $f'' + f = 0$ is established, write down its general solution. Then determine which solution has $f(0) = 0, f'(0) = 1$.

---

# Solution

**(a) Reduction to the scalar ODE $f'' + f = 0$.**

> [!note]- Derivation
> Let $J(t) = f(t) E(t)$, where $E$ is a parallel unit field along $\gamma$ with $E \perp T$ ($T = \dot\gamma$). Compute $J' = \nabla_T J$:
> $$J' = \nabla_T (f E) = (T f) E + f \nabla_T E = f' E + 0 = f' E.$$
> Compute $J''$:
> $$J'' = \nabla_T J' = \nabla_T (f' E) = (T f') E + f' \nabla_T E = f'' E + 0 = f'' E.$$
>
> Compute the curvature term: $R(J, T)T = R(fE, T)T = f \cdot R(E, T)T$. On the unit sphere, $E$ and $T$ are orthonormal unit vectors, and the 2-plane spanned by them has sectional curvature $1$. So
> $$g(R(E, T)T, E) = K(\mathrm{span}\{E, T\}) \cdot |E|^2 |T|^2 - g(E, T)^2 = 1 \cdot 1 \cdot 1 - 0 = 1.$$
> Since $R(E, T)T$ is in $T^\perp$ (because $R(\cdot, T)T$ maps to $T^\perp$ by the symmetries of $R$ — namely, $g(R(E, T)T, T) = 0$ by antisymmetry of $R$ in the first two slots and metric-compatibility) and $E$ is a unit vector orthogonal to $T$, we get $R(E, T)T = g(R(E, T)T, E) \cdot E + (\text{components in other directions of }T^\perp)$. To handle the case $n > 2$ correctly: in general, $R(E, T)T$ has components in *every* direction of $T^\perp$, not just $E$ — but for $S^n$ with the round metric, by symmetry of the curvature tensor (constant curvature), $R(E, T)T = E$ exactly. This is the special structure of constant-curvature spaces.
>
> So $R(J, T)T = f \cdot E$. The Jacobi equation becomes
> $$J'' + R(J, T)T = 0 \implies f'' E + f E = 0 \implies (f'' + f) E = 0.$$
> Since $E$ is nonzero (unit), we get $f'' + f = 0$.

**(b) Normal Jacobi fields are sinusoidal.**

> [!note]- Derivation
> The general solution of $f'' + f = 0$ is $f(t) = a \cos t + b \sin t$ for constants $a, b \in \mathbb{R}$.
>
> So a normal Jacobi field of the form $J(t) = f(t) E(t)$ is $J(t) = (a\cos t + b\sin t) E(t)$.
>
> By choosing a parallel-transported orthonormal basis $(E_1, \ldots, E_{n-1})$ of $T^\perp$ along $\gamma$ (rather than a single $E$), the general normal Jacobi field decomposes:
> $$J(t) = \sum_{i=1}^{n-1} (a_i \cos t + b_i \sin t) E_i(t), \qquad a_i, b_i \in \mathbb{R}.$$
> This is a $2(n-1)$-dimensional family — the right count for normal Jacobi fields in [[Def - Dimension|dimension]] $n$.

**(c) The Jacobi field with $J(0) = 0, J'(0) = E(0)$.**

> [!note]- Derivation
> With $J(t) = f(t) E(t)$, $J(0) = f(0) E(0)$ and $J'(0) = f'(0) E(0)$ (since $\nabla_T E = 0$ implies $E$ has the same value as itself at $t = 0$).
>
> From $J(0) = 0$ and $E(0) \neq 0$: $f(0) = 0$.
> From $J'(0) = E(0)$ and $f'(0)E(0) = E(0)$: $f'(0) = 1$.
>
> The solution of $f'' + f = 0$ with $f(0) = 0, f'(0) = 1$ is $f(t) = \sin t$.
>
> So $J(t) = \sin(t) E(t)$ — the **sinusoidal Jacobi field**.

> [!note]- Complete formal solution
> **(a)** Let $E$ be a parallel unit normal vector field along $\gamma$. For $J = f E$, compute
> $$J' = f' E, \quad J'' = f'' E.$$
> The curvature term: on $S^n$ with constant sectional curvature $1$, $R(E, T)T = E$ for any orthonormal $E \perp T$. So $R(J, T)T = R(fE, T)T = f \cdot R(E, T)T = f E$.
>
> The Jacobi equation $J'' + R(J, T)T = 0$ becomes $f'' E + f E = 0$, i.e., $(f'' + f)E = 0$. Since $E \neq 0$, $f'' + f = 0$.
>
> **(b)** General solutions of $f'' + f = 0$ are $f(t) = a\cos t + b\sin t$. Decomposing a normal Jacobi field in a parallel-transported orthonormal basis $(E_1, \ldots, E_{n-1})$ of $T^\perp$:
> $$J(t) = \sum_{i=1}^{n-1}(a_i \cos t + b_i\sin t) E_i(t).$$
> This is the $2(n-1)$-dimensional space of normal Jacobi fields along $\gamma$.
>
> **(c)** The Jacobi field with $J(0) = 0$ and $J'(0) = E(0)$ has $f(0) = 0$ and $f'(0) = 1$, so $f(t) = \sin t$. Hence
> $$J(t) = \sin(t) \cdot E(t). \qquad\blacksquare$$

---

# Key Takeaways

**Constant sectional curvature gives constant-coefficient Jacobi equations.** On a space of constant sectional curvature $K$, the curvature operator $R(\cdot, T)T$ on $T^\perp$ is *exactly* $K \cdot \mathrm{id}$. So in a parallel-transported frame, the Jacobi equation decouples into independent scalar ODEs $f_i'' + K f_i = 0$. The solutions are:
- $K > 0$ (sphere): trigonometric, $f = a\cos(\sqrt K t) + b\sin(\sqrt K t)$, with first conjugate distance $\pi/\sqrt K$.
- $K = 0$ (Euclidean): linear, $f = a + bt$, no conjugate points.
- $K < 0$ (hyperbolic): hyperbolic, $f = a\cosh(\sqrt{|K|}t) + b\sinh(\sqrt{|K|}t)$, no conjugate points.

This is the cleanest case of the [[Thm - Jacobi Equation and Conjugate Points|eigenvalue/conjugate-point dictionary]], and it is the model against which all comparison theorems (Rauch, Toponogov, Bonnet–Myers) measure non-constant-curvature manifolds.

**Parallel transport reduces the Jacobi equation to a scalar ODE in any geometry.** The technique of writing $J = f^i E_i$ in a parallel-transported frame is *universal* — it works on any Riemannian manifold, not just constant-curvature ones. In general, the parallel frame produces a *time-dependent* matrix $A(t)$ of curvature components, and the equation $f'' + A(t)f = 0$ is a vector-valued Sturm–Liouville problem. The advantage is that the connection has been "trivialised" along the curve, leaving only the curvature as the time-dependent coefficient. **Trigger:** whenever you need to compute Jacobi fields along a specific geodesic, parallel-transport a frame first.

**The sinusoidal Jacobi field $\sin(t) E(t)$ corresponds to $d(\exp_p)$ on $S^n$.** By the [[Thm - Jacobi Equation and Conjugate Points|Jacobi-field formula]] $J_w(t) = d(\exp_p)_{tv}(tw)$, the Jacobi field $J$ with $J(0) = 0, J'(0) = w$ is $d(\exp_p)$ applied to the radial perturbation. On $S^n$, this is $J(t) = \sin(t) E(t)$ (with $E$ the parallel transport of $w$ along $\gamma_v$, assumed unit), giving the explicit formula for the radial derivative of $\exp_p$ on the sphere. The vanishing at $t = \pi$ is the [[Ex - Conjugate Points on the Round Sphere are Antipodal|antipodal conjugate point]].

**The Jacobi-field analysis bridges geometry, ODE theory, and analysis on the sphere.** The single calculation $J(t) = \sin(t)E(t)$ encodes: (i) the conjugate-point structure of $S^n$ (zeros of $\sin$ at $\pi, 2\pi, \ldots$); (ii) the failure of $\exp_p$ to be a local [[Def - Diffeomorphism|diffeomorphism]] at $|v| = \pi$ (the differential collapses); (iii) the second-variation analysis showing great-circle arcs of length $\geq \pi$ are not minimising. So one explicit Jacobi-field computation gives *all* the local geometry of the round sphere — and the same is true on hyperbolic space (with $\sinh$ instead of $\sin$).

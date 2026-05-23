---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Index Form"
  - "Ex - Jacobi Fields on a Sphere are Sinusoidal"
  - "Ex - Conjugate Points on the Round Sphere are Antipodal"
  - "Thm - Second Variation of Arc Length"
tags: [geometry, riemannian-geometry, index-form, sphere, second-variation]
---

# Problem Statement

Let $S^2$ be the unit sphere with the round metric. Let $\gamma : [0, \pi] \to S^2$ be the great-circle arc from the north pole $N$ to the south pole $S$, parametrised at unit speed (so $\gamma$ has length $\pi$). Let $e_\perp(t)$ be a parallel unit normal field along $\gamma$ (e.g., in spherical coordinates, $e_\perp = \partial_\varphi$ appropriately normalised at the equator and parallel-transported).

(a) Compute the [[Def - The Index Form|index form]] $I(V, V)$ for normal variation fields $V(t) = f(t)\, e_\perp(t)$ with $f(0) = f(\pi) = 0$. Show that
$$I(V, V) = \int_0^\pi (f'(t)^2 - f(t)^2)\, dt.$$

(b) Evaluate $I(V, V)$ on the test functions $f(t) = \sin(kt)$ for $k = 1, 2, 3, \ldots$ Identify the kernel ($I(V, V) = 0$) and the negative directions ($I(V, V) < 0$).

(c) Conclude that the geodesic $\gamma$ from $N$ to $S$ is not a *strict* local minimum of length: there exists a continuous family of curves of equal length from $N$ to $S$ to first and second order in the variation parameter.

**Recall:**

The [[Def - The Index Form|index form]] on a unit-speed geodesic $\gamma$ with tangent $T$ is
$$I(V, W) = \int_0^L \bigl(g(V', W') - g(R(V, T)T, W)\bigr)\, dt,$$
for normal variations $V, W$ vanishing at the endpoints.

On the unit sphere, the curvature operator $R(\cdot, T)T$ on $T^\perp$ is the identity (sectional curvature $1$). So $R(V, T)T = V$ for $V \in T^\perp$.

From [[Ex - Jacobi Fields on a Sphere are Sinusoidal|the sinusoidal exercise]], the Jacobi field along $\gamma$ with $J(0) = 0, J'(0) = e_\perp(0)$ is $J(t) = \sin(t) e_\perp(t)$.

By the [[Thm - Second Variation of Arc Length|second variation theorem]] and the [[Thm - Jacobi Equation and Conjugate Points|Morse index theorem]], the index of $I$ on $\mathcal V_0^\perp$ equals the number of interior conjugate points to $N$ along $\gamma$. For $\gamma|_{[0, \pi]}$, the only conjugate parameter is $t = \pi$, *at the endpoint*. So the interior conjugate-point count is $0$, hence the index of $I$ is $0$. But the *nullity* (kernel dimension) is $1$ (the sinusoidal Jacobi field $\sin t$).

---

# Convergent Strategy

**Problem class:** Direct computation of the index form on a specific geodesic. This is in the "compute the index form" sub-class — typically done by integrating the explicit formula in a parallel frame.

**Assumption pattern:** The geodesic is the half-great-circle on $S^2$, parameter $[0, \pi]$. Constant curvature, explicit Jacobi-field formula, and parallel-transported frame all available.

**Theorem routing:** Three steps. **First**, substitute $V = f e_\perp$ into the index-form formula, using $\nabla_T e_\perp = 0$ (parallel) and $R(e_\perp, T)T = e_\perp$ (curvature on $S^2$). This gives $I(V, V) = \int (f'^2 - f^2) dt$. **Second**, test on $f = \sin(kt)$. Compute $f'(t) = k\cos(kt)$, $(f')^2 = k^2 \cos^2(kt)$, $f^2 = \sin^2(kt)$. Integrate using $\int_0^\pi \cos^2(kt) dt = \pi/2$ and $\int_0^\pi \sin^2(kt) dt = \pi/2$ to get $I(V, V) = (k^2 - 1)\pi/2$. **Third**, interpret: $k = 1$ gives $I = 0$ (the kernel — the sinusoidal Jacobi field); $k \geq 2$ gives $I > 0$ (positive directions); no negative directions exist for this pole-to-pole arc.

**Key decision point:** Even though there are no negative directions, the *kernel* is non-trivial (sinusoidal Jacobi field with $f = \sin t$). This means the pole-to-pole great-circle arc is a length-minimiser, but *not a strict one* — there is a one-parameter family of variations to first and second order that don't change the length. The geometric meaning: the variation $\gamma_s(t) =$ slightly tilted great circle gives a path of equal length from $N$ to $S$ (every great circle from pole to pole has length $\pi$).

---

# Legal Operations Used

1. **Operation 7 from the topic page (apply the second variation formula to test minimisation).** Direct application: compute $I(V, V)$ on test functions to detect the kernel/index structure.

2. **Operation 8 from the topic page (solve the Jacobi equation along $\gamma$).** Used to identify the kernel of $I$ as the sinusoidal Jacobi field $\sin t \cdot e_\perp$.

3. **Operation 5 from the topic page (use a parallel frame to simplify).** The parallel-transported $e_\perp$ trivialises the index-form computation: $\nabla_T e_\perp = 0$ kills connection terms.

---

# Hints

> [!note]- Hint 1
> Substitute $V = f(t) e_\perp(t)$ into $I(V, V) = \int(g(V', V') - g(R(V,T)T, V)) dt$. Use $\nabla_T e_\perp = 0$ and the formula $R(e_\perp, T)T = e_\perp$ (sectional curvature $1$).

> [!note]- Hint 2
> $V' = f' e_\perp$ (since $e_\perp$ is parallel). So $g(V', V') = (f')^2 |e_\perp|^2 = (f')^2$. Similarly $g(R(V, T)T, V) = g(f e_\perp, f e_\perp) = f^2$. The index form becomes $\int (f'^2 - f^2) dt$.

> [!note]- Hint 3
> Test on $f = \sin(kt)$ for $k \in \mathbb{Z}^+$. These satisfy $f(0) = f(\pi) = 0$ (since $\sin(k\pi) = 0$). Compute $\int_0^\pi (k^2 \cos^2 kt - \sin^2 kt) dt$.

> [!note]- Hint 4
> $\int_0^\pi \cos^2 kt\, dt = \pi/2$ for $k \neq 0$; $\int_0^\pi \sin^2 kt\, dt = \pi/2$. So $I(V_k, V_k) = k^2 \pi/2 - \pi/2 = (k^2 - 1)\pi/2$. Identify: $k = 1$ gives $0$ (kernel); $k \geq 2$ gives positive.

---

# Solution

**Step 1: Reduce the index form to $\int(f'^2 - f^2)\, dt$.**

> [!note]- Derivation
> Set $V = f(t) e_\perp(t)$ with $e_\perp$ a parallel unit normal field along $\gamma$ (so $|e_\perp| = 1, \nabla_T e_\perp = 0$). Boundary conditions: $V(0) = f(0) e_\perp(0)$ and $V(\pi) = f(\pi) e_\perp(\pi)$, both zero iff $f(0) = f(\pi) = 0$.
>
> Compute $V' = \nabla_T V = \nabla_T (f e_\perp) = f' e_\perp + f \nabla_T e_\perp = f' e_\perp$.
>
> So $g(V', V') = (f')^2 |e_\perp|^2 = (f')^2$.
>
> Compute $R(V, T)T$. By [[Ex - Jacobi Fields on a Sphere are Sinusoidal|the sinusoidal-Jacobi exercise]] (or directly: on $S^2$, the sectional curvature is $1$), $R(e_\perp, T)T = e_\perp$. So $R(V, T)T = R(fe_\perp, T)T = f e_\perp$.
>
> $g(R(V, T)T, V) = g(f e_\perp, f e_\perp) = f^2$.
>
> Therefore
> $$I(V, V) = \int_0^\pi \bigl((f')^2 - f^2\bigr)\, dt.$$

**Step 2: Test on $f_k = \sin(kt)$.**

> [!note]- Derivation
> For $k \in \mathbb{Z}^+$, $f_k(t) = \sin(kt)$ satisfies $f_k(0) = 0$ and $f_k(\pi) = \sin(k\pi) = 0$ ✓.
>
> $f_k'(t) = k \cos(kt)$, so $(f_k')^2 = k^2 \cos^2(kt)$ and $f_k^2 = \sin^2(kt)$.
>
> $$I(V_k, V_k) = \int_0^\pi (k^2 \cos^2(kt) - \sin^2(kt))\, dt.$$
>
> Using $\int_0^\pi \cos^2(kt)\, dt = \int_0^\pi \sin^2(kt)\, dt = \pi/2$ for $k \geq 1$ (standard half-angle integrals):
> $$I(V_k, V_k) = k^2 \cdot \frac{\pi}{2} - \frac{\pi}{2} = \frac{(k^2 - 1)\pi}{2}.$$
>
> Tabulating:
> - $k = 1$: $I(V_1, V_1) = 0$. ← **Kernel direction**, $V_1 = \sin(t) e_\perp(t)$, the sinusoidal Jacobi field.
> - $k = 2$: $I(V_2, V_2) = 3\pi/2 > 0$.
> - $k = 3$: $I(V_3, V_3) = 4\pi > 0$.
> - General $k \geq 2$: $I(V_k, V_k) > 0$ — all positive directions.
>
> No negative directions among the test functions $\{\sin(kt)\}_{k \geq 1}$. In fact, $\{\sin(kt)/\sqrt{\pi/2}\}_{k \geq 1}$ is an orthonormal basis of the Hilbert space $L^2_0([0, \pi])$ of square-integrable functions on $[0, \pi]$ vanishing at endpoints, and the index form is *diagonal* in this basis with eigenvalues $(k^2 - 1)\pi/2 \geq 0$ for all $k \geq 1$. So $I \geq 0$ on $\mathcal V_0^\perp$ (in this single direction $e_\perp$), with kernel exactly spanned by $V_1 = \sin t \cdot e_\perp$.

**Step 3: Interpretation — equal-length nearby curves.**

> [!note]- Derivation
> The vanishing of $I(V_1, V_1) = 0$ means: there is a non-trivial direction in the space of variations along $\gamma$ in which the second derivative of length is zero, with the first derivative also zero (since $\gamma$ is critical). So *to second order* in the variation parameter, the length is unchanged.
>
> Geometrically, this direction corresponds to *tilting the great circle* connecting $N$ to $S$. The original $\gamma$ is the longitude $\varphi = 0$ from north pole to south pole. The variation $\gamma_s$ for small $s$ is the longitude $\varphi = s$ — also a great circle from $N$ to $S$, also of length $\pi$. So $L(\gamma_s) = \pi = L(\gamma)$ to *all* orders in $s$ — not just to second order.
>
> So we have a one-parameter family of length-minimising [[Def - Geodesic|geodesics]] from $N$ to $S$, all of equal length $\pi$. The kernel direction $V_1 = \sin(t) e_\perp(t)$ is the variation field of this family at $s = 0$, and it is *both* a Jacobi field (variation through geodesics) *and* in the kernel of $I$ (zero second variation of length).
>
> Note also that the pole-to-pole geodesic *does* minimise length — $L(\gamma) = \pi = d_g(N, S)$ — but it is not a *strict* minimum, because of the family of equal-length parallel great circles. This is the geometric meaning of "index $0$, nullity $1$ at the first conjugate pair": minimising but not strictly so.

> [!note]- Complete formal solution
> **(a)** For $V = f e_\perp$ with $e_\perp$ parallel:
> $$I(V, V) = \int_0^\pi \bigl((f')^2 - f^2\bigr)\, dt.$$
>
> **(b)** Evaluating on $f_k(t) = \sin(kt)$:
> $$I(V_k, V_k) = \int_0^\pi (k^2 \cos^2(kt) - \sin^2(kt))\, dt = \frac{(k^2 - 1)\pi}{2}.$$
> - $k = 1$: $I = 0$ (kernel direction, the Jacobi field $\sin t \cdot e_\perp$).
> - $k \geq 2$: $I > 0$ (positive directions).
>
> So on the space $\{f e_\perp : f \in L^2_0([0, \pi])\}$, the index form is positive-semidefinite with $1$-dimensional kernel spanned by $V_1 = \sin t \cdot e_\perp$. Other parallel normal directions $e_\perp'$ orthogonal to $e_\perp$ would give similar analyses, contributing $n - 1$ kernel [[Def - Dimension|dimensions]] total — but on $S^2$, $T^\perp$ is $1$-dimensional, so the total nullity is $1$.
>
> **(c)** The kernel direction corresponds to the variation by tilted parallel great circles. Each great circle from $N$ to $S$ has length $\pi$, so $L(\gamma_s) = \pi$ for all $s$ in the family — the geodesic $\gamma$ is *length-minimising but not strictly so*. There is a continuous family of equal-length minimisers between the same endpoints. This is the geometric content of the kernel of the index form at the first conjugate distance.
> $\qquad\blacksquare$

---

# Key Takeaways

**At the first conjugate distance, the index form has non-trivial kernel and the geodesic is minimising-but-not-strictly.** The pole-to-pole great circle on $S^2$ illustrates this perfectly: it is length-minimising ($L = \pi = d_g(N, S)$), but there is a one-parameter family of other minimising geodesics (all great circles through both poles) of equal length. The kernel direction $V = \sin t \cdot e_\perp$ is the variation field along this family — *both* a Jacobi field *and* a null direction of the index form. This is the borderline behaviour at the first conjugate point: minimising but degenerate.

**Past the first conjugate point, the index form develops negative directions.** Extending $\gamma$ to parameter $[0, T]$ with $T > \pi$ would change the calculation: $\int_0^T (k^2\cos^2(kt) - \sin^2(kt)) dt$ depends on $T$, and for $T > \pi$ test functions like $\sin(\pi t/T)$ give $I = (\pi/T)^2 \cdot T/2 - T/2 = T/2 \cdot ((\pi/T)^2 - 1)$, which is *negative* for $T > \pi$. So a pole-to-pole geodesic extended slightly past $S$ (parameter $[0, T]$ with $T = \pi + \varepsilon$) is *not* a local length-minimiser — there is a $V$ with $I(V, V) < 0$, and this $V$ produces a nearby curve with strictly shorter length. This is the **Morse Index Theorem in action**: the index of $I$ equals the number of interior conjugate points, and the conjugate point at $\pi$ "switches on" the negative direction for any longer geodesic.

**The eigenvalue analysis of the index form is the Sturm–Liouville theory of the Jacobi equation.** The functions $\sin(kt)/\sqrt{\pi/2}$ for $k = 1, 2, 3, \ldots$ are an orthonormal basis of $L^2_0([0, \pi])$ (the Hilbert space of zero-boundary square-integrable functions), and they are *eigenfunctions* of the operator $-d^2/dt^2$ (Dirichlet Laplacian on $[0, \pi]$) with eigenvalues $k^2$. The index form $I(V, V) = \int(f'^2 - f^2) dt$ acts on these eigenfunctions with eigenvalue $k^2 - 1$. The kernel ($k = 1$) is the *first* eigenvalue of the Jacobi equation matching the "1" in the curvature; positive eigenvalues ($k \geq 2$) correspond to higher Fourier modes. So the index form has the same spectral structure as the Jacobi operator restricted to functions with Dirichlet boundary, and the conjugate-point analysis is the Sturm oscillation theorem applied to this spectrum.

**The Morse Index Theorem connects this to the global structure of the loop space.** The fact that the index of $\gamma|_{[0, T]}$ is $0$ for $T \leq \pi$ and jumps to $1$ at $T = \pi$ (where the conjugate point appears) is the **Morse Index Theorem** in its simplest case. The index counts "how much $\gamma$ is *not* a local minimum" — the dimension of the negative-direction [[Def - Subspace|subspace]]. As $T$ grows past further conjugate points ($2\pi, 3\pi, \ldots$), the index increases, and these index jumps are the data of the Morse theory of the energy functional on the loop space of $S^2$. The Morse complex built from this gives, via Morse inequalities, lower bounds on the Betti numbers of the loop space and existence theorems for closed geodesics. This single computation on the half-great-circle of $S^2$ is the seed of an enormous theory.

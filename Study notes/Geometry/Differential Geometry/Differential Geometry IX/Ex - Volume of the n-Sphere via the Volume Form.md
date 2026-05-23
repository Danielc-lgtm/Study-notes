---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Riemannian Volume Form"
  - "Thm - Existence of the Riemannian Volume Form"
  - "Thm - Change of Variables for Integration on Manifolds"
tags: [geometry, differential-geometry, sphere, volume, integration]
---

# Problem Statement

Compute the $n$-dimensional Riemannian volume of the unit $n$-sphere $S^n \subseteq \mathbb{R}^{n+1}$ in the round metric (induced from the ambient Euclidean inner product). That is, with $\omega_g$ the Riemannian volume form of the round metric, compute
$$\mathrm{vol}(S^n) := \int_{S^n}\omega_g$$
in closed form. Specifically:

(a) Show that in higher-dimensional spherical coordinates $(\varphi_1, \ldots, \varphi_{n-1}, \theta)$ on $S^n$, the round metric has components leading to
$$\omega_g = \sin^{n-1}\varphi_1\,\sin^{n-2}\varphi_2\,\cdots\sin\varphi_{n-1}\,d\varphi_1\wedge\cdots\wedge d\varphi_{n-1}\wedge d\theta.$$

(b) Compute the iterated integral and obtain $\mathrm{vol}(S^n) = \dfrac{2\pi^{(n+1)/2}}{\Gamma\big(\tfrac{n+1}{2}\big)}$.

(c) Verify the formula for small $n$: $\mathrm{vol}(S^1) = 2\pi$, $\mathrm{vol}(S^2) = 4\pi$, $\mathrm{vol}(S^3) = 2\pi^2$, $\mathrm{vol}(S^4) = \tfrac{8\pi^2}{3}$.

**Recall:**

The Riemannian volume form on an oriented Riemannian manifold:

![[Def - Riemannian Volume Form#The Definition]]

The coordinate formula:

![[Thm - Existence of the Riemannian Volume Form#Statement]]

The Gamma function $\Gamma(s) := \int_0^\infty t^{s-1}e^{-t}\,dt$ for $s > 0$ satisfies $\Gamma(s+1) = s\Gamma(s)$, $\Gamma(1) = 1$, $\Gamma(\tfrac{1}{2}) = \sqrt{\pi}$.

---

# Convergent Strategy

**Problem class:** Direct integration of the Riemannian volume form on a specific Riemannian manifold, using an explicit chart. This is the higher-dimensional generalization of [[Ex - Computing the Integral of a 2-Form on the Sphere]].

**Assumption pattern:** $S^n$ has a well-known parametrization in higher-dimensional spherical coordinates, and the round metric in these coordinates is diagonal with a known form. The computation reduces to evaluating an iterated integral involving products of powers of sines — a classical integral known as the **Wallis integral** or **beta-function integral**.

**Theorem routing:** [[Thm - Change of Variables for Integration on Manifolds|Integration via parametrization]] converts $\int_{S^n}\omega_g$ into a Riemann integral over the parameter cube $(0, \pi)^{n-1}\times(0, 2\pi)$. [[Thm - Existence of the Riemannian Volume Form|the formula for the Riemannian volume form]] gives the integrand as a product of sines. The remaining algebra is the iterated integral, which reduces via the Wallis-Euler formula to a ratio of factorials and $\Gamma$ functions, giving the closed form.

**Key decision point:** The choice of higher-dimensional spherical coordinates (latitudes-and-longitude) over alternatives (stereographic projection, ball-of-radius-$\rho$ approach via the volume-form Jacobian relation) is the natural one because it gives a single global-up-to-measure-zero parametrization, and the integrand factorizes into a product of $\sin^k\varphi$ terms, each of which is a known Wallis integral. The factorization is crucial for getting a closed form.

---

# Legal Operations Used

1. **Operation 1 (pull back to a chart and integrate)** from the [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem#Legal Operations|topic page]]. Pull back the volume form via the spherical-coordinates parametrization, recognizing the result as a product-of-sines.

2. **Operation 4 (use the Riemannian volume formula $\sqrt{\det g}\,dx^1\wedge\cdots\wedge dx^n$)** from the topic page. The coordinate expression of $\omega_g$ in spherical coordinates is essentially $\sqrt{\det g}\,d\varphi_1\cdots d\varphi_{n-1}\,d\theta$, where the metric components in these coordinates are computed in the derivation.

3. **The Wallis integral / Beta function identity.** $\int_0^\pi\sin^k\varphi\,d\varphi = B\!\big(\tfrac{1}{2}, \tfrac{k+1}{2}\big) = \tfrac{\sqrt\pi\,\Gamma((k+1)/2)}{\Gamma((k+2)/2)}$. This is the analytical machinery that converts the iterated integral into a $\Gamma$-function expression.

---

# Hints

> [!note]- Hint 1
> Write the higher-dimensional spherical coordinates explicitly:
> $$F(\varphi_1, \ldots, \varphi_{n-1}, \theta) = (\cos\varphi_1, \sin\varphi_1\cos\varphi_2, \sin\varphi_1\sin\varphi_2\cos\varphi_3, \ldots, \sin\varphi_1\cdots\sin\varphi_{n-1}\cos\theta, \sin\varphi_1\cdots\sin\varphi_{n-1}\sin\theta).$$
> The angles $\varphi_i \in (0, \pi)$ for $i = 1, \ldots, n-1$, and $\theta \in (0, 2\pi)$.

> [!note]- Hint 2
> The round-metric components in these coordinates are diagonal:
> $$g_{\varphi_1\varphi_1} = 1, \quad g_{\varphi_2\varphi_2} = \sin^2\varphi_1, \quad g_{\varphi_3\varphi_3} = \sin^2\varphi_1\sin^2\varphi_2, \quad \ldots, \quad g_{\theta\theta} = \sin^2\varphi_1\cdots\sin^2\varphi_{n-1}.$$
> So $\det g = \sin^{2(n-1)}\varphi_1\,\sin^{2(n-2)}\varphi_2\,\cdots\sin^2\varphi_{n-1}$, and $\sqrt{\det g} = \sin^{n-1}\varphi_1\,\sin^{n-2}\varphi_2\,\cdots\sin\varphi_{n-1}$.

> [!note]- Hint 3
> The iterated integral splits as a product because the integrand is a product of functions of one variable each:
> $$\mathrm{vol}(S^n) = \Big(\int_0^{2\pi}d\theta\Big)\prod_{k=1}^{n-1}\Big(\int_0^\pi\sin^k\varphi\,d\varphi\Big).$$
> Use the Wallis identity $\int_0^\pi\sin^k\varphi\,d\varphi = \sqrt\pi\,\Gamma((k+1)/2)/\Gamma((k+2)/2)$.

> [!note]- Hint 4
> The product of Wallis integrals telescopes via $\Gamma(s+1) = s\Gamma(s)$. The result is $\mathrm{vol}(S^n) = 2\pi^{(n+1)/2}/\Gamma((n+1)/2)$. For $n = 1, 2, 3, 4$, use $\Gamma(1) = 1, \Gamma(3/2) = \sqrt\pi/2, \Gamma(2) = 1, \Gamma(5/2) = 3\sqrt\pi/4$.

---

# Solution

The proof has three steps: derive the explicit form of $\omega_g$ in spherical coordinates (step 1), set up and evaluate the iterated integral as a product of Wallis integrals (step 2), and verify the closed form against small-$n$ cases (step 3).

**Step 1: The volume form in higher-dimensional spherical coordinates.**

Define the spherical-coordinate parametrization $F : D \to S^n$ where $D = (0, \pi)^{n-1}\times(0, 2\pi)$:
$$F(\varphi_1, \ldots, \varphi_{n-1}, \theta) = \big(\cos\varphi_1, \sin\varphi_1\cos\varphi_2, \sin\varphi_1\sin\varphi_2\cos\varphi_3, \ldots, \sin\varphi_1\cdots\sin\varphi_{n-1}\cos\theta, \sin\varphi_1\cdots\sin\varphi_{n-1}\sin\theta\big).$$
Let $x^0, x^1, \ldots, x^n$ denote the components of $F$ (the first being $\cos\varphi_1$, etc.).

> [!note]- Derivation
> This is the standard recursive spherical parametrization: think of $S^n$ as built by "rotating $S^{n-1}$ by an angle $\varphi_1$". The first coordinate is $\cos\varphi_1$ (the "height"); the remaining coordinates are $\sin\varphi_1$ times a parametrization of $S^{n-1}$ in coordinates $(\varphi_2, \ldots, \varphi_{n-1}, \theta)$. Recursing gives the displayed formula.

The induced round metric in these coordinates is diagonal with components
$$g_{\varphi_k\varphi_k} = \sin^2\varphi_1\sin^2\varphi_2\cdots\sin^2\varphi_{k-1}, \qquad g_{\theta\theta} = \sin^2\varphi_1\sin^2\varphi_2\cdots\sin^2\varphi_{n-1}.$$
(For $k = 1$ the product is empty, giving $g_{\varphi_1\varphi_1} = 1$.)

> [!note]- Derivation
> Compute by differentiating $F$ with respect to each angle:
> $$\partial_{\varphi_1}F = (-\sin\varphi_1, \cos\varphi_1\cos\varphi_2, \cos\varphi_1\sin\varphi_2\cos\varphi_3, \ldots).$$
> Its squared norm is $\sin^2\varphi_1 + \cos^2\varphi_1\sum(\text{components of }F|_{\text{rest}})^2$, but the "rest" is a unit vector on $S^{n-1}$, so the sum is $1$. Hence $g_{\varphi_1\varphi_1} = \sin^2\varphi_1 + \cos^2\varphi_1 = 1$.
>
> $$\partial_{\varphi_2}F = (0, -\sin\varphi_1\sin\varphi_2, \sin\varphi_1\cos\varphi_2\cos\varphi_3, \ldots).$$
> Its squared norm has a factor $\sin^2\varphi_1$ pulled out of every term, then a sum that again equals $\sin^2\varphi_2 + \cos^2\varphi_2 = 1$. Hence $g_{\varphi_2\varphi_2} = \sin^2\varphi_1$.
>
> The pattern continues: $g_{\varphi_k\varphi_k} = \sin^2\varphi_1\cdots\sin^2\varphi_{k-1}$, and finally $g_{\theta\theta} = \sin^2\varphi_1\cdots\sin^2\varphi_{n-1}$.
>
> Cross terms vanish by orthogonality (each pair $\partial_{\varphi_i}, \partial_{\varphi_j}$ for $i \neq j$ has zero dot product, by the structure of the spherical parametrization).

The volume form is therefore
$$\omega_g = \sqrt{\det(g_{ij})}\,d\varphi_1\wedge\cdots\wedge d\varphi_{n-1}\wedge d\theta = \sqrt{\prod_{k=1}^{n}\sin^{2(k-1)}\varphi_{k}}\,\text{(...)}$$

Computing the product:
$$\det g_{ij} = g_{\varphi_1\varphi_1}\cdots g_{\varphi_{n-1}\varphi_{n-1}}g_{\theta\theta} = 1\cdot\sin^2\varphi_1\cdot\sin^4\varphi_1\sin^2\varphi_2\cdots,$$
which telescopes to give $\det g_{ij} = \sin^{2(n-1)}\varphi_1\,\sin^{2(n-2)}\varphi_2\,\cdots\sin^2\varphi_{n-1}$. Hence
$$\omega_g = \sin^{n-1}\varphi_1\,\sin^{n-2}\varphi_2\,\cdots\sin\varphi_{n-1}\,d\varphi_1\wedge\cdots\wedge d\varphi_{n-1}\wedge d\theta.$$

> [!note]- Derivation
> $\det(g_{ij})$ is the product of diagonal entries:
> $$\det g = 1\cdot\sin^2\varphi_1\cdot(\sin^2\varphi_1\sin^2\varphi_2)\cdots(\sin^2\varphi_1\cdots\sin^2\varphi_{n-1}).$$
> Each factor $\sin^2\varphi_k$ appears in the $k$-th, $(k+1)$-th, ..., $n$-th positions, so its total exponent is $n - k$. Wait — recount: $\sin^2\varphi_1$ appears in $g_{\varphi_2\varphi_2}, g_{\varphi_3\varphi_3}, \ldots, g_{\theta\theta}$, that's $n - 1$ positions. $\sin^2\varphi_2$ appears in $g_{\varphi_3\varphi_3}, \ldots, g_{\theta\theta}$, that's $n - 2$ positions. ... $\sin^2\varphi_{n-1}$ appears only in $g_{\theta\theta}$, $1$ position.
>
> So $\det g = \prod_{k=1}^{n-1}\sin^{2(n-k)}\varphi_k = \sin^{2(n-1)}\varphi_1\sin^{2(n-2)}\varphi_2\cdots\sin^2\varphi_{n-1}$, and $\sqrt{\det g} = \sin^{n-1}\varphi_1\sin^{n-2}\varphi_2\cdots\sin\varphi_{n-1}$. The exponent on $\sin\varphi_k$ is $n - k$.

**Step 2: Set up and evaluate the iterated integral.**

By the integration-over-parametrizations formula,
$$\mathrm{vol}(S^n) = \int_{S^n}\omega_g = \int_D F^*\omega_g = \int_0^{2\pi}\int_0^\pi\cdots\int_0^\pi\sin^{n-1}\varphi_1\cdots\sin\varphi_{n-1}\,d\varphi_1\cdots d\varphi_{n-1}\,d\theta.$$

The integrand factorizes, so the iterated integral factorizes:
$$\mathrm{vol}(S^n) = \Big(\int_0^{2\pi}d\theta\Big)\prod_{k=1}^{n-1}\Big(\int_0^\pi\sin^{n-k}\varphi_k\,d\varphi_k\Big) = 2\pi\prod_{k=1}^{n-1}\int_0^\pi\sin^{n-k}\varphi\,d\varphi.$$

> [!note]- Derivation
> The integrand $\sin^{n-1}\varphi_1\sin^{n-2}\varphi_2\cdots\sin\varphi_{n-1}$ has each factor depending on a *different* variable. By Fubini, the iterated integral splits as a product. The variable $\theta$ contributes $\int_0^{2\pi}d\theta = 2\pi$; the variable $\varphi_k$ contributes $\int_0^\pi\sin^{n-k}\varphi\,d\varphi$.

Substituting $j = n - k$ (so $j$ ranges from $n - 1$ down to $1$ as $k$ ranges from $1$ to $n - 1$):
$$\mathrm{vol}(S^n) = 2\pi\prod_{j=1}^{n-1}\int_0^\pi\sin^j\varphi\,d\varphi.$$

The Wallis integral / beta-function formula is
$$\int_0^\pi\sin^j\varphi\,d\varphi = B\Big(\frac{1}{2}, \frac{j+1}{2}\Big) = \frac{\Gamma(1/2)\Gamma((j+1)/2)}{\Gamma((j+2)/2)} = \frac{\sqrt\pi\,\Gamma((j+1)/2)}{\Gamma((j+2)/2)}.$$

> [!note]- Derivation
> $\int_0^\pi\sin^j\varphi\,d\varphi = 2\int_0^{\pi/2}\sin^j\varphi\,d\varphi$ by symmetry of $\sin$ about $\pi/2$. The substitution $u = \sin^2\varphi$ converts this to a beta-function integral: $\int_0^{\pi/2}\sin^j\varphi\,d\varphi = \tfrac{1}{2}B(\tfrac{j+1}{2}, \tfrac{1}{2})$. The beta-gamma identity $B(a, b) = \Gamma(a)\Gamma(b)/\Gamma(a+b)$ then gives the displayed formula.

Substituting:
$$\mathrm{vol}(S^n) = 2\pi\prod_{j=1}^{n-1}\frac{\sqrt\pi\,\Gamma((j+1)/2)}{\Gamma((j+2)/2)} = 2\pi\cdot\pi^{(n-1)/2}\prod_{j=1}^{n-1}\frac{\Gamma((j+1)/2)}{\Gamma((j+2)/2)}.$$

The product is telescoping: $\Gamma((j+2)/2)$ in the denominator of the $j$-th term cancels with $\Gamma((j+1)/2)$ in the numerator of the $(j+1)$-th term (with index shift by 1). Specifically,
$$\prod_{j=1}^{n-1}\frac{\Gamma((j+1)/2)}{\Gamma((j+2)/2)} = \frac{\Gamma(1)}{\Gamma((n+1)/2)} = \frac{1}{\Gamma((n+1)/2)}.$$

> [!note]- Derivation
> Write out the first few factors:
> - $j = 1$: $\Gamma(1)/\Gamma(3/2)$
> - $j = 2$: $\Gamma(3/2)/\Gamma(2)$
> - $j = 3$: $\Gamma(2)/\Gamma(5/2)$
> - ...
> - $j = n-1$: $\Gamma(n/2)/\Gamma((n+1)/2)$
>
> Multiplying, $\Gamma(3/2), \Gamma(2), \ldots, \Gamma(n/2)$ each appear once in numerator and once in denominator (telescope). The surviving factors are $\Gamma(1) = 1$ in the numerator and $\Gamma((n+1)/2)$ in the denominator.

Therefore,
$$\mathrm{vol}(S^n) = 2\pi\cdot\pi^{(n-1)/2}\cdot\frac{1}{\Gamma((n+1)/2)} = \frac{2\pi^{(n+1)/2}}{\Gamma((n+1)/2)}.$$

**Step 3: Verification for small $n$.**

$$n = 1: \quad \mathrm{vol}(S^1) = \frac{2\pi^1}{\Gamma(1)} = \frac{2\pi}{1} = 2\pi. \quad\checkmark$$
$$n = 2: \quad \mathrm{vol}(S^2) = \frac{2\pi^{3/2}}{\Gamma(3/2)} = \frac{2\pi^{3/2}}{\sqrt\pi/2} = \frac{4\pi^{3/2}}{\sqrt\pi} = 4\pi. \quad\checkmark$$
$$n = 3: \quad \mathrm{vol}(S^3) = \frac{2\pi^2}{\Gamma(2)} = \frac{2\pi^2}{1} = 2\pi^2. \quad\checkmark$$
$$n = 4: \quad \mathrm{vol}(S^4) = \frac{2\pi^{5/2}}{\Gamma(5/2)} = \frac{2\pi^{5/2}}{3\sqrt\pi/4} = \frac{8\pi^{5/2}}{3\sqrt\pi} = \frac{8\pi^2}{3}. \quad\checkmark$$

> [!note]- Complete formal solution
> **Step 1: Volume form in spherical coordinates.** With $F(\varphi_1, \ldots, \varphi_{n-1}, \theta)$ the standard spherical parametrization of $S^n \subseteq \mathbb{R}^{n+1}$, the induced round metric has diagonal components $g_{\varphi_k\varphi_k} = \sin^2\varphi_1\cdots\sin^2\varphi_{k-1}$, $g_{\theta\theta} = \sin^2\varphi_1\cdots\sin^2\varphi_{n-1}$. Hence
> $$\det(g_{ij}) = \sin^{2(n-1)}\varphi_1\sin^{2(n-2)}\varphi_2\cdots\sin^2\varphi_{n-1},$$
> $$\omega_g = \sin^{n-1}\varphi_1\sin^{n-2}\varphi_2\cdots\sin\varphi_{n-1}\,d\varphi_1\wedge\cdots\wedge d\varphi_{n-1}\wedge d\theta.$$
>
> **Step 2: Iterated integral.** The integrand factorizes, so
> $$\mathrm{vol}(S^n) = 2\pi\prod_{j=1}^{n-1}\int_0^\pi\sin^j\varphi\,d\varphi.$$
> Using the Wallis identity $\int_0^\pi\sin^j\varphi\,d\varphi = \sqrt\pi\,\Gamma((j+1)/2)/\Gamma((j+2)/2)$,
> $$\mathrm{vol}(S^n) = 2\pi\cdot\pi^{(n-1)/2}\prod_{j=1}^{n-1}\frac{\Gamma((j+1)/2)}{\Gamma((j+2)/2)}.$$
> The telescoping product equals $\Gamma(1)/\Gamma((n+1)/2) = 1/\Gamma((n+1)/2)$, giving
> $$\mathrm{vol}(S^n) = \frac{2\pi^{(n+1)/2}}{\Gamma((n+1)/2)}.$$
>
> **Step 3: Verification.** $\mathrm{vol}(S^1) = 2\pi$, $\mathrm{vol}(S^2) = 4\pi$, $\mathrm{vol}(S^3) = 2\pi^2$, $\mathrm{vol}(S^4) = 8\pi^2/3$, in agreement with classical computations of the surface area / volume of low-dimensional spheres. $\blacksquare$

**Sanity-check via independent route.** The formula $\mathrm{vol}(S^n) = 2\pi^{(n+1)/2}/\Gamma((n+1)/2)$ can also be derived from the ball-volume formula by differentiating. The unit ball $B^{n+1}$ in $\mathbb{R}^{n+1}$ has volume $V_{n+1} = \pi^{(n+1)/2}/\Gamma((n+1)/2 + 1) = \pi^{(n+1)/2}/((n+1)/2)\cdot\Gamma((n+1)/2)$. The relationship $\mathrm{vol}(\partial B^{n+1}) = (d/dr)\mathrm{vol}(B_r^{n+1})|_{r=1}$ — i.e., the surface area of the unit sphere is the derivative of the ball volume with respect to the radius at $r = 1$ — gives $\mathrm{vol}(S^n) = (n+1)V_{n+1} = (n+1)\pi^{(n+1)/2}/((n+1)/2)\Gamma((n+1)/2) = 2\pi^{(n+1)/2}/\Gamma((n+1)/2)$. The two routes agree.

---

# Key Takeaways

**Higher-dimensional spherical coordinates give a diagonal metric and a factorizable volume form — the key to closed-form computation.** The triumph of the spherical parametrization is that the round metric is diagonal in these coordinates, and the volume form $\sqrt{\det g}\,d\varphi_1\cdots d\theta$ factorizes into a product of single-variable powers of sines. The factorization is what makes the iterated integral evaluable in closed form via the Wallis-Beta-Gamma machinery. The takeaway: when computing integrals on a Riemannian manifold, *prefer coordinates in which the metric is diagonal* — these are the "Riemannian coordinates" of choice. For symmetric spaces (spheres, hyperbolic spaces, tori), such coordinates exist and exploit the symmetry maximally.

**The Wallis integral $\int_0^\pi\sin^k\varphi\,d\varphi$ is the universal tool for sphere-volume computations.** It appears in the volume of every sphere, in computations of moments, in spectral theory of $S^n$, in random-direction sampling. Internalize the formula $\int_0^\pi\sin^k\varphi\,d\varphi = \sqrt\pi\,\Gamma((k+1)/2)/\Gamma((k+2)/2)$ and the telescoping product structure. The Wallis integrals are also the foundation of the surface-area-of-sphere computation in physics, of the volume-of-orthogonal-group computations, and of any rotationally-symmetric integral.

**The trigger condition: the integrand factorizes after a coordinate transformation.** This is the meta-trigger for closed-form evaluation. Whenever a manifold integral can be set up so the integrand is a *product* of single-variable functions (rather than a sum or a non-separable function), Fubini converts the iterated integral into a *product* of one-variable integrals, and one-variable integrals are far more tractable than multi-variable ones. Sphere coordinates achieve this for the round metric; product manifolds achieve it for product metrics; toric manifolds achieve it for toric coordinates. The lesson: search for a parametrization that factorizes the integrand.

**Companion exercise.** [[Ex - Computing the Integral of a 2-Form on the Sphere]] is the $n = 2$ warm-up, computing the surface area $4\pi$ from a single 2-form. The $n$-dimensional case extends this to arbitrary $n$, requiring the Wallis-Beta machinery. Together they drill the three-tier approach to sphere computations: pick the spherical parametrization, write the volume form, do the iterated Wallis integral.

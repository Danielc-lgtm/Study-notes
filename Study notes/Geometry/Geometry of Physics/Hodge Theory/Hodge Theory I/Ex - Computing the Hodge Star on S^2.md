---
type: exercise
subject: hodge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Hodge Star Operator"
  - "Def - The Codifferential"
  - "Def - Hodge Laplacian"
  - "Def - Riemannian Volume Form"
tags: [geometry, hodge-theory, riemannian-geometry]
---

# Problem Statement

Consider the round $2$-sphere $S^2$ with the standard round metric in spherical coordinates $(\theta, \varphi)$, $\theta \in (0, \pi)$, $\varphi \in [0, 2\pi)$. The metric is $g = d\theta^2 + \sin^2\theta\,d\varphi^2$, and the Riemannian volume form is $\operatorname{vol}_{S^2} = \sin\theta\,d\theta\wedge d\varphi$ (with the orientation $d\theta\wedge d\varphi$ on the coordinate patch).

(a) Identify an orthonormal coframe $(\sigma^1, \sigma^2)$ at each point of the coordinate patch.

(b) Compute $\star 1$, $\star d\theta$, $\star d\varphi$, and $\star(d\theta\wedge d\varphi)$ in coordinate form (i.e., as expressions in $d\theta, d\varphi$, and functions of $\theta$).

(c) Verify the double-star formula: $\star\star f = f$ for functions, $\star\star\omega = -\omega$ for $1$-forms ($k(n-k) = 1$, so $(-1)^1 = -1$), and $\star\star\omega = +\omega$ for $2$-forms.

(d) Use $\Delta f = -\star d\star df$ for a function $f$ to derive the Laplace–Beltrami operator on $S^2$ in spherical coordinates. Verify it agrees with the classical formula $\nabla^2 f = \frac{1}{\sin\theta}\partial_\theta(\sin\theta\partial_\theta f) + \frac{1}{\sin^2\theta}\partial_\varphi^2 f$.

**Recall:**

The round metric on $S^2$ has the orthonormal coframe $(\sigma^1, \sigma^2) = (d\theta, \sin\theta\,d\varphi)$ at each interior point of the coordinate patch. The Hodge star on an orthonormal coframe satisfies $\star\sigma^I = \mathrm{sgn}(I, I^c)\sigma^{I^c}$ (signs from orientation, Riemannian signature).

![[Def - The Hodge Star Operator#The Definition]]

The codifferential on a Riemannian $2$-manifold is $\delta = -\star d\star$ on $1$-forms (sign convention $(-1)^{2\cdot 2 + 1} = -1$). On functions: $\delta f = 0$.

The Hodge Laplacian on functions is $\Delta f = \delta(df) + d(\delta f) = \delta(df) = -\star d\star df$, since $\delta f = 0$ for $f$ a function. The standard (Laplace–Beltrami) Laplacian on functions is $\nabla^2 f = -\Delta f$ in the Hodge sign convention.

---

# Convergent Strategy

**Problem class:** Concrete computation of $\star$ on a curved Riemannian $2$-manifold, with the goal of recovering the classical Laplacian on $S^2$ via $\Delta = -\star d\star$. The chapter's problem-solving strategy in §1.2 (compute $\delta$ via the explicit $\star d\star$ formula) applies directly.

**Assumption pattern:** The round metric on $S^2$ in spherical coordinates. The coordinate coframe $(d\theta, d\varphi)$ is *not* orthonormal at most points (since $|d\varphi|^2_g = 1/\sin^2\theta$, not $1$), but $(d\theta, \sin\theta\,d\varphi)$ is. The volume form $\operatorname{vol}_{S^2} = \sin\theta\,d\theta\wedge d\varphi$ has the $\sin\theta$ factor that tracks the area distortion of spherical coordinates.

**Theorem routing:** Use the orthonormal coframe to apply [[Thm - Properties of the Hodge Star]] property 5. Then translate back to the coordinate $1$-forms $d\theta, d\varphi$ by the relation $\sigma^2 = \sin\theta\,d\varphi$. For part (d), compose $\star$, $d$, $\star$, $d$ on a function $f$.

**Key decision point:** Recognize that the *correct* orthonormal coframe is $(d\theta, \sin\theta\,d\varphi)$, not $(d\theta, d\varphi)$. The factor $\sin\theta$ is essential because $|d\varphi|^2_g = 1/\sin^2\theta$ — the coordinate $1$-form $d\varphi$ is *not* of unit length in the round metric. Forgetting this factor gives incorrect Hodge stars and the wrong Laplacian.

---

# Legal Operations Used

1. **Identify the correct orthonormal coframe by Gram–Schmidt on the coordinate coframe.** The coordinate coframe $(d\theta, d\varphi)$ has $|d\theta|^2 = 1$, $|d\varphi|^2 = 1/\sin^2\theta$, $\langle d\theta, d\varphi\rangle = 0$ (orthogonal). Multiplying $d\varphi$ by $\sin\theta$ normalizes its length: $(d\theta, \sin\theta\,d\varphi)$ is orthonormal.

2. **Apply the orthonormal-coframe formula for $\star$** (operation from the topic page). On the orthonormal coframe $(\sigma^1, \sigma^2)$, $\star 1 = \sigma^1\wedge\sigma^2 = \operatorname{vol}_{S^2}$; $\star\sigma^1 = \sigma^2$; $\star\sigma^2 = -\sigma^1$; $\star(\sigma^1\wedge\sigma^2) = 1$.

3. **Translate orthonormal results back to coordinates.** Replace $\sigma^2 = \sin\theta\,d\varphi$ in the formulas, factoring the $\sin\theta$ as appropriate.

4. **Apply the chain $-\star d\star d$ to a function** to compute the Hodge Laplacian. Track signs carefully.

---

# Hints

> [!note]- Hint 1
> The orthonormal coframe is *not* $(d\theta, d\varphi)$. Compute $|d\varphi|^2_g$ to see what factor is needed. Since $|d\varphi|^2_g = g^{\varphi\varphi} = 1/\sin^2\theta$, multiplying $d\varphi$ by $\sin\theta$ normalizes it. So the orthonormal coframe is $(d\theta, \sin\theta\,d\varphi)$.

> [!note]- Hint 2
> $\star d\theta$ should be the $1$-form whose pairing with $d\theta$ via the defining identity gives $\langle d\theta, d\theta\rangle\operatorname{vol}_{S^2} = \operatorname{vol}_{S^2}$. So $d\theta\wedge\star d\theta = \operatorname{vol}_{S^2} = \sin\theta\,d\theta\wedge d\varphi$, giving $\star d\theta = \sin\theta\,d\varphi$ (the coordinate $1$-form $d\varphi$ multiplied by $\sin\theta$). Similarly for $\star d\varphi$.

> [!note]- Hint 3
> For the Laplacian, compute step by step: $df = \partial_\theta f\,d\theta + \partial_\varphi f\,d\varphi$; $\star df = \partial_\theta f\,\star d\theta + \partial_\varphi f\,\star d\varphi$; substituting and simplifying; then $d\star df$ (a $2$-form); then $\star d\star df$ (a function); then $\Delta f = -\star d\star df$ should match the classical formula.

---

# Solution

The exercise has four parts. Part (a) identifies the orthonormal coframe by normalizing $d\varphi$ with $\sin\theta$. Part (b) applies the orthonormal-coframe formula for $\star$ and translates back to coordinates. Part (c) verifies the double-star formula. Part (d) computes the Laplacian on a function via $\Delta f = -\star d\star df$ and compares with the classical Laplace–Beltrami operator.

**Step 1: Orthonormal coframe (part (a)).**

> [!note]- Derivation
> The metric $g = d\theta^2 + \sin^2\theta\,d\varphi^2$ has components $g_{\theta\theta} = 1$, $g_{\varphi\varphi} = \sin^2\theta$, $g_{\theta\varphi} = 0$. The dual metric on $1$-forms: $g^{\theta\theta} = 1$, $g^{\varphi\varphi} = 1/\sin^2\theta$, $g^{\theta\varphi} = 0$.
>
> So $|d\theta|^2_g = g^{\theta\theta} = 1$, $|d\varphi|^2_g = g^{\varphi\varphi} = 1/\sin^2\theta$. The orthonormal coframe is obtained by normalizing $d\varphi$: $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\,d\varphi$ (so $|\sigma^2|^2_g = \sin^2\theta\cdot 1/\sin^2\theta = 1$).
>
> Orientation: $\sigma^1\wedge\sigma^2 = d\theta\wedge(\sin\theta\,d\varphi) = \sin\theta\,d\theta\wedge d\varphi = \operatorname{vol}_{S^2}$. ✓ (positive orientation).

**Step 2: Compute Hodge stars (part (b)).**

> [!note]- Derivation
> Apply the orthonormal-coframe formula for $\star$ on $(\sigma^1, \sigma^2) = (d\theta, \sin\theta\,d\varphi)$ in $n = 2$ Riemannian:
> - $\star 1 = \sigma^1\wedge\sigma^2 = \sin\theta\,d\theta\wedge d\varphi$ (the volume form).
> - $\star\sigma^1 = \sigma^2$ (complementary multi-index, positive sign for cyclic order in $n = 2$): $\star d\theta = \sin\theta\,d\varphi$.
> - $\star\sigma^2 = -\sigma^1$ (sign $-1$ since $(2, 1)$ is an odd permutation of $(1, 2)$): $\star(\sin\theta\,d\varphi) = -d\theta$, hence $\star d\varphi = -d\theta/\sin\theta$.
> - $\star(\sigma^1\wedge\sigma^2) = 1$: $\star(\sin\theta\,d\theta\wedge d\varphi) = 1$, hence $\star(d\theta\wedge d\varphi) = 1/\sin\theta$.
>
> Summary:
> | Form | $\star$ |
> |---|---|
> | $1$ | $\sin\theta\,d\theta\wedge d\varphi$ |
> | $d\theta$ | $\sin\theta\,d\varphi$ |
> | $d\varphi$ | $-d\theta/\sin\theta$ |
> | $d\theta\wedge d\varphi$ | $1/\sin\theta$ |

**Step 3: Verify the double-star formula (part (c)).**

> [!note]- Derivation
> Apply $\star$ twice:
> - On functions ($k = 0$, $n - k = 2$): $\star\star f = \star(\sin\theta\,d\theta\wedge d\varphi)\cdot f = (1/\sin\theta)\cdot\sin\theta\cdot f = f$. So $\star\star = +1$ on $0$-forms, matching $(-1)^{0\cdot 2} = +1$. ✓
> - On $1$-forms ($k = 1$, $n - k = 1$): $\star\star d\theta = \star(\sin\theta\,d\varphi) = -d\theta$. So $\star\star = -1$ on $1$-forms, matching $(-1)^{1\cdot 1} = -1$. ✓ Similarly $\star\star d\varphi = \star(-d\theta/\sin\theta) = -\sin\theta\,d\varphi/\sin\theta = -d\varphi$.
> - On $2$-forms ($k = 2$, $n - k = 0$): $\star\star(d\theta\wedge d\varphi) = \star(1/\sin\theta) = (1/\sin\theta)\sin\theta\,d\theta\wedge d\varphi = d\theta\wedge d\varphi$. So $\star\star = +1$ on $2$-forms, matching $(-1)^{2\cdot 0} = +1$. ✓

**Step 4: Compute the Laplacian on a function (part (d)).**

> [!note]- Derivation
> $\Delta f = -\star d\star df$ for a function $f \in C^\infty(S^2)$. Compute step by step.
>
> **Compute $df$:**
> $df = \partial_\theta f\,d\theta + \partial_\varphi f\,d\varphi$.
>
> **Compute $\star df$:** apply $\star$ to each term using Step 2.
> $\star df = \partial_\theta f\cdot\sin\theta\,d\varphi + \partial_\varphi f\cdot(-d\theta/\sin\theta)$
> $= \sin\theta\partial_\theta f\,d\varphi - \frac{1}{\sin\theta}\partial_\varphi f\,d\theta$.
>
> Note: $\star df$ is a $1$-form on $S^2$.
>
> **Compute $d\star df$:** apply $d$ to the $1$-form.
> $d\star df = d(\sin\theta\partial_\theta f)\wedge d\varphi + d(-\partial_\varphi f/\sin\theta)\wedge d\theta$
> $= \partial_\theta(\sin\theta\partial_\theta f)d\theta\wedge d\varphi + \partial_\varphi(\sin\theta\partial_\theta f)d\varphi\wedge d\varphi + \partial_\varphi(-\partial_\varphi f/\sin\theta)d\varphi\wedge d\theta + \partial_\theta(-\partial_\varphi f/\sin\theta)d\theta\wedge d\theta$
>
> The $d\varphi\wedge d\varphi$ and $d\theta\wedge d\theta$ terms vanish. The $d\varphi\wedge d\theta = -d\theta\wedge d\varphi$:
> $d\star df = \partial_\theta(\sin\theta\partial_\theta f)d\theta\wedge d\varphi - \partial_\varphi(-\partial_\varphi f/\sin\theta)d\theta\wedge d\varphi$
> $= \left[\partial_\theta(\sin\theta\partial_\theta f) + \frac{1}{\sin\theta}\partial_\varphi^2 f\right]d\theta\wedge d\varphi$.
>
> **Compute $\star d\star df$:** apply $\star$ to the $2$-form.
> $\star d\star df = \star\left[\left(\partial_\theta(\sin\theta\partial_\theta f) + \frac{1}{\sin\theta}\partial_\varphi^2 f\right)d\theta\wedge d\varphi\right]$
> $= \left(\partial_\theta(\sin\theta\partial_\theta f) + \frac{1}{\sin\theta}\partial_\varphi^2 f\right)\cdot\frac{1}{\sin\theta}$
> $= \frac{1}{\sin\theta}\partial_\theta(\sin\theta\partial_\theta f) + \frac{1}{\sin^2\theta}\partial_\varphi^2 f$.
>
> **Compute $\Delta f$:**
> $\Delta f = -\star d\star df = -\left[\frac{1}{\sin\theta}\partial_\theta(\sin\theta\partial_\theta f) + \frac{1}{\sin^2\theta}\partial_\varphi^2 f\right]$
> $= -\nabla^2 f$,
> where $\nabla^2 f = \frac{1}{\sin\theta}\partial_\theta(\sin\theta\partial_\theta f) + \frac{1}{\sin^2\theta}\partial_\varphi^2 f$ is the classical Laplace–Beltrami operator on $S^2$.
>
> So the Hodge Laplacian $\Delta = d\delta + \delta d$ on functions agrees with $-\nabla^2$, the negative of the standard Riemannian Laplacian. ✓

> [!note]- Complete formal solution
> **Part (a):** The orthonormal coframe is $(\sigma^1, \sigma^2) = (d\theta, \sin\theta\,d\varphi)$, normalized so $|\sigma^i|^2_g = 1$. Positive orientation: $\sigma^1\wedge\sigma^2 = \sin\theta\,d\theta\wedge d\varphi = \operatorname{vol}_{S^2}$.
>
> **Part (b):** From the orthonormal-coframe formula:
> - $\star 1 = \sin\theta\,d\theta\wedge d\varphi$ (volume form).
> - $\star d\theta = \sin\theta\,d\varphi$.
> - $\star d\varphi = -d\theta/\sin\theta$.
> - $\star(d\theta\wedge d\varphi) = 1/\sin\theta$.
>
> **Part (c):** Direct verification: $\star\star = +1$ on functions and $2$-forms, $\star\star = -1$ on $1$-forms, matching the general formula $\star\star = (-1)^{k(n-k)}$ at $n = 2$, $k = 0, 1, 2$.
>
> **Part (d):** Computing $-\star d\star df$ step by step gives
> $$\Delta f = -\nabla^2 f = -\frac{1}{\sin\theta}\partial_\theta(\sin\theta\partial_\theta f) - \frac{1}{\sin^2\theta}\partial_\varphi^2 f,$$
> the negative of the classical Laplace–Beltrami operator on $S^2$. $\qquad\blacksquare$

---

# Key Takeaways

**Orthonormal coframes are essential for Hodge star computations.** The most common error in Hodge-star computations on curved manifolds is using the coordinate coframe directly without normalization. On $S^2$ in spherical coordinates, $d\varphi$ has length $1/\sin\theta$, not $1$ — so directly applying $\star d\varphi = ?$ via the wrong "orthonormal formula" gives wrong answers. The disciplined procedure: (i) find an orthonormal coframe by normalizing the coordinate coframe; (ii) compute $\star$ on the orthonormal coframe; (iii) translate back to coordinate forms. The factor $\sin\theta$ (or generally $\sqrt{|g|}$) appears in every step and must be tracked.

**The Hodge Laplacian on functions is $-\nabla^2$.** The sign convention $\Delta = d\delta + \delta d$ gives $\Delta f = -\nabla^2 f$ on functions, where $\nabla^2$ is the standard Riemannian Laplacian. The negative sign is what makes $\Delta$ nonnegative: $\langle\Delta f, f\rangle_{L^2} = \|df\|^2_{L^2} \geq 0$, with equality iff $f$ is constant. Mixing conventions silently — treating $\Delta$ and $\nabla^2$ as the same — is the most common source of sign errors in Hodge-theoretic computations, especially in physics applications where the convention $\Delta = \nabla^2$ is also common.

**On a $2$-manifold, $\star$ is a complex structure on $\Omega^1$.** The double-star formula gives $\star\star = -1$ on $1$-forms in $2$D Riemannian — exactly the relation defining a complex structure. So $\Omega^1(M^2)$ carries a natural complex structure via $\star$, with $\star\omega$ playing the role of $i\omega$. Every $1$-form decomposes into $(1, 0)$ and $(0, 1)$ parts (eigenforms of $\star$ with eigenvalues $\pm i$, in the complexified sense). This is the structural reason that *every $2$-dimensional Riemannian manifold is naturally a Riemann surface* — the Hodge star induces a complex structure on the tangent bundle. The Cauchy–Riemann equations $\partial f/\partial\bar z = 0$ for a holomorphic function $f = u + iv$ correspond to $du = \star dv$ in form language — relating real and imaginary parts via the Hodge star.

This exercise complements [[Ex - Hodge Star on R^3 Recovers Cross Product and Scalar Triple Product]] (Hodge star on flat $\mathbb{R}^3$) and previews [[Ex - Harmonic 1-Forms on the Torus]] (Hodge theory on a flat compact manifold).

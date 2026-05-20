---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Morera's Theorem"
  - "Thm - Holomorphic Dependence on a Parameter"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $\phi : [0, 1] \to \mathbb{C}$ be continuous. For $z \in \mathbb{C} \setminus [0, 1]$, define
$$g(z) := \int_0^1 \frac{\phi(t)}{t - z}\,dt.$$
Show that $g$ is holomorphic on $\mathbb{C} \setminus [0, 1]$, and compute its derivative.

**Recall:**

[[Thm - Morera's Theorem]]: continuous $f$ with $\int_\Delta f\,dz = 0$ for every triangle is holomorphic. [[Thm - Holomorphic Dependence on a Parameter]]: $g(z) = \int \varphi(z, s)\,ds$ is holomorphic when $\varphi$ continuous in $(z, s)$ and holomorphic in $z$ for each $s$.

---

# Convergent Strategy

**Problem class:** Show a function defined by an integral is holomorphic.

**Assumption pattern:** $g$ depends on a complex parameter via an integral.

**Theorem routing:** Apply [[Thm - Holomorphic Dependence on a Parameter]]: identify $\varphi(z, t) = \phi(t)/(t - z)$, verify continuity in $(z, t)$ and holomorphicity in $z$ for each $t$. Conclude holomorphicity of $g$.

**Key decision point:** The integrand $\phi(t)/(t - z)$ has a singularity at $z = t$ — so the integrand is *not* defined for $z \in [0, 1]$. For $z \notin [0, 1]$, the denominator $t - z$ stays bounded away from $0$ uniformly in $t \in [0, 1]$, so the integrand is bounded and the integral converges. The domain is exactly $\mathbb{C} \setminus [0, 1]$.

---

# Legal Operations Used

1. **Identify $\varphi(z, t) = \phi(t)/(t - z)$.**
2. **Continuity of $\varphi$ in $(z, t)$:** continuous on $\{(z, t) : z \notin [0, 1], t \in [0, 1]\}$, since the denominator $t - z$ is bounded below by $\text{dist}(z, [0, 1]) > 0$.
3. **Holomorphicity in $z$ for fixed $t$:** $1/(t - z)$ is holomorphic in $z$ away from $t$; $\phi(t)$ is a constant.
4. **Apply [[Thm - Holomorphic Dependence on a Parameter]]** to conclude $g$ holomorphic.
5. **Derivative:** $g'(z) = \int_0^1 (\partial \varphi/\partial z)(z, t)\,dt = \int_0^1 \phi(t)/(t - z)^2\,dt$.

---

# Hints

> [!note]- Hint 1
> $\varphi(z, t) = \phi(t)/(t - z)$ is continuous in $(z, t)$ on $(\mathbb{C} \setminus [0, 1]) \times [0, 1]$, and holomorphic in $z$ for each fixed $t$.

> [!note]- Hint 2
> Apply [[Thm - Holomorphic Dependence on a Parameter]]. The derivative formula is $g'(z) = \int \partial_z \varphi(z, t)\,dt = \int \phi(t)/(t - z)^2\,dt$.

---

# Solution

The proof breaks into five short steps that together verify the hypotheses of the parameter-dependent holomorphy theorem and then read off the derivative. Steps 1–3 identify the integrand $\varphi(z,t) = \phi(t)/(t-z)$ and check that it is continuous in $(z,t)$ on the relevant domain and holomorphic in $z$ for each fixed $t$; Step 4 invokes [[Thm - Holomorphic Dependence on a Parameter]] to conclude holomorphy of $g$; Step 5 differentiates under the integral sign to obtain $g'(z) = \int \phi(t)/(t-z)^2\,dt$. The non-obvious move is in Step 2 — controlling the singular denominator uniformly using $\text{dist}(z, [0,1]) > 0$, which is what fails as $z$ approaches the path.

**Step 1: Setup and identify $\varphi$.**

The integrand is $\varphi(z, t) := \phi(t)/(t - z)$, considered as a function of $(z, t)$ with $z \in \mathbb{C} \setminus [0, 1]$ and $t \in [0, 1]$.

**Step 2: $\varphi$ is continuous in $(z, t)$.**

Take $(z_0, t_0)$ with $z_0 \notin [0, 1]$ and $t_0 \in [0, 1]$. Let $d = \text{dist}(z_0, [0, 1]) > 0$. For $(z, t)$ near $(z_0, t_0)$: $|t - z| \geq d/2$ (uniformly, for $|z - z_0| < d/4$ and $t \in [0, 1]$). So $|\varphi(z, t)| \leq |\phi(t)|/(d/2)$ is bounded. Continuity in each variable + uniform bound gives continuity in both.

More precisely: $\varphi$ is a composition $(z, t) \mapsto (t - z, \phi(t)) \mapsto \phi(t)/(t - z)$ — continuous on the open set $\{(z, t) : t - z \neq 0\}$, in particular on our domain.

**Step 3: $\varphi(z, t)$ holomorphic in $z$ for fixed $t$.**

For fixed $t \in [0, 1]$: $\varphi(z, t) = \phi(t)/(t - z)$ is holomorphic in $z$ on $\mathbb{C} \setminus \{t\} \supseteq \mathbb{C} \setminus [0, 1]$.

**Step 4: Apply the parameter theorem.**

By [[Thm - Holomorphic Dependence on a Parameter]], $g(z) = \int_0^1 \varphi(z, t)\,dt$ is holomorphic on $\mathbb{C} \setminus [0, 1]$.

**Step 5: Compute the derivative.**

By the same theorem (or by direct differentiation under the integral sign, justified by uniform convergence):
$$g'(z) = \int_0^1 \frac{\partial \varphi}{\partial z}(z, t)\,dt = \int_0^1 \frac{\phi(t)}{(t - z)^2}\,dt.$$

> [!note]- Complete formal solution
> $\varphi(z, t) = \phi(t)/(t - z)$ is continuous on $(\mathbb{C} \setminus [0, 1]) \times [0, 1]$ (denominator bounded below) and holomorphic in $z$ for each $t$. By [[Thm - Holomorphic Dependence on a Parameter]], $g$ is holomorphic on $\mathbb{C} \setminus [0, 1]$ with $g'(z) = \int_0^1 \phi(t)/(t - z)^2\,dt$. $\blacksquare$

---

# Key Takeaways

**Cauchy-type integrals are holomorphic in the parameter.**

The integral $g(z) = \int_\gamma \phi(w)/(w - z)\,dw$ for $z$ off the contour is always holomorphic in $z$. This is the *defining* example of "holomorphic dependence on a parameter": the parameter $z$ appears in the denominator, holomorphic when the denominator is nonzero.

**Differentiation under the integral.**

Once holomorphicity is established, the derivative is obtained by differentiating under the integral sign:
$$g'(z) = \int \frac{\partial}{\partial z}\left[\frac{\phi(t)}{t - z}\right]\,dt = \int \frac{\phi(t)}{(t - z)^2}\,dt.$$
Iterating: $g^{(n)}(z) = n!\int \phi(t)/(t - z)^{n+1}\,dt$. This is the structure of all Cauchy-type integrals — and it underlies CIF + higher-derivative CIF.

**Domain considerations.**

The natural domain is $\mathbb{C}$ minus the trace of the integration path (the singular set of the integrand). For paths that are line segments, half-lines, or more general curves, the resulting "Cauchy-type integral" is holomorphic *off* the curve. As $z$ approaches the curve, the integral may behave singularly (in the limit, picking up "principal value" or "jump" terms).

**The Cauchy transform of $\phi$.**

The function $g(z) = (1/2\pi i)\int \phi(t)/(t - z)\,dt$ is the **Cauchy transform** of $\phi$. It is the prototype of Cauchy-type singular integrals in harmonic analysis, used in the theory of Calderón–Zygmund operators, the boundary behaviour of holomorphic functions, and the theory of analytic capacity.

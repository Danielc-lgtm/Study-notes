---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Def - Winding Number"
  - "Thm - Existence and Properties of the Winding Number"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $k$ be a nonzero integer and define $\gamma : [0, 1] \to \mathbb{C}$ by $\gamma(t) = e^{2\pi i k t}$. Compute $I(\gamma; 0)$, the winding number of $\gamma$ around the origin. Then compute $I(\gamma; w)$ for $|w| > 1$ and confirm it is zero.

**Recall:**

![[Def - Winding Number#The Definition]]

The integer-valuedness follows because $\gamma$ is closed and the lift $\tilde\gamma$ satisfies $e^{i\tilde\gamma(b)} = e^{i\tilde\gamma(a)}$, so $\tilde\gamma(b) - \tilde\gamma(a) \in 2\pi\mathbb{Z}$.

---

# Convergent Strategy

**Problem class:** Direct computation of a winding number from the integral formula. This is the prototype of "given an explicit curve, compute its winding number" — the goal is to verify that the topological definition matches the integral formula on a concrete example.

**Assumption pattern:** $\gamma$ is piecewise $C^1$ (in fact $C^\infty$) so the integral formula applies. The curve is given parametrically, making the integral straightforward.

**Theorem routing:** [[Def - Winding Number|integral formula]] $I(\gamma; w) = (2\pi i)^{-1}\int_\gamma dz/(z - w)$, then direct computation.

**Key decision point:** Recognize that $\gamma(t) = e^{2\pi i k t}$ wraps around the origin exactly $k$ times (counterclockwise if $k > 0$, clockwise if $k < 0$). Verify by parameterizing and integrating.

---

# Legal Operations Used

1. **Apply the integral formula** $I(\gamma; w) = (2\pi i)^{-1}\int_\gamma dz/(z - w)$ for piecewise $C^1$ $\gamma$.
2. **Substitute the parametrization** $\gamma(t) = e^{2\pi i k t}$, $\gamma'(t) = 2\pi i k e^{2\pi i k t}$.
3. **Simplify the integrand** in $t$ and integrate.
4. **Verify via the unbounded component fact**: for $|w| > 1$, the curve doesn't enclose $w$, so $I(\gamma; w) = 0$.

---

# Hints

> [!note]- Hint 1
> Use the integral formula and substitute $z = \gamma(t) = e^{2\pi i k t}$, $dz = 2\pi i k e^{2\pi i k t}\,dt$.

> [!note]- Hint 2
> The integrand $\gamma'(t)/\gamma(t) = (2\pi i k e^{2\pi i k t})/e^{2\pi i k t} = 2\pi i k$ is constant in $t$.

> [!note]- Hint 3
> For $|w| > 1$, the curve $\gamma$ stays in the unit disc; $w$ is in the unbounded component of $\mathbb{C}\setminus \gamma^* = \mathbb{C}\setminus S^1$. The winding number is zero by [[Thm - Existence and Properties of the Winding Number|the unbounded-component property]].

---

# Solution

**Step 1: $I(\gamma; 0) = k$**

Apply the integral formula with $w = 0$:
$$I(\gamma; 0) = \frac{1}{2\pi i}\int_\gamma \frac{dz}{z}.$$

> [!note]- Derivation
> Substitute $z = e^{2\pi i k t}$, $dz = 2\pi i k e^{2\pi i k t}\,dt$ for $t \in [0, 1]$:
> $$\int_\gamma \frac{dz}{z} = \int_0^1 \frac{2\pi i k e^{2\pi i k t}}{e^{2\pi i k t}}\,dt = \int_0^1 2\pi i k \,dt = 2\pi i k.$$
> Dividing by $2\pi i$: $I(\gamma; 0) = k$.

**Step 2: $I(\gamma; w) = 0$ for $|w| > 1$**

The curve $\gamma$ has image $\gamma^* = \{|z| = 1\}$ (the unit circle), so $\mathbb{C}\setminus \gamma^*$ has two connected components: the open unit disc $\{|z| < 1\}$ and its complement $\{|z| > 1\}$.

> [!note]- Derivation
> The component $\{|z| > 1\}$ is unbounded. By [[Thm - Existence and Properties of the Winding Number|properties of the winding number]], $I(\gamma; w) = 0$ for $w$ in the unbounded component.
>
> Alternatively, direct computation: for $|w| > 1$, the function $1/(z - w)$ is holomorphic on a neighborhood of the closed unit disc, so by [[Thm - Cauchy's Theorem for Simply Connected Domains|Cauchy's theorem]] $\int_\gamma dz/(z - w) = 0$, hence $I(\gamma; w) = 0$.

> [!note]- Complete formal solution
> Apply the integral formula. With $\gamma(t) = e^{2\pi i k t}$, $\gamma'(t) = 2\pi i k e^{2\pi i k t}$, and $\gamma(t) - 0 = e^{2\pi i k t} \neq 0$ for all $t$, the integrand is well-defined and
> $$I(\gamma; 0) = \frac{1}{2\pi i}\int_0^1 \frac{\gamma'(t)}{\gamma(t)}\,dt = \frac{1}{2\pi i}\int_0^1 2\pi i k\,dt = k.$$
>
> For $|w| > 1$: $\mathbb{C} \setminus \gamma^* = \{|z| < 1\} \cup \{|z| > 1\}$ has two components, $\{|z| > 1\}$ is unbounded, and the winding number vanishes there. Alternatively, by Cauchy: $1/(z - w)$ is holomorphic on the unit disc (which contains $\gamma^*$) for $|w| > 1$, so its integral around $\gamma$ vanishes. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "circle around origin, $n$ times" → "winding number $n$".** The simplest verification of the integral formula: a curve that visibly winds $n$ times has winding number $n$. The integral $\int_\gamma dz/z$ on a circle traversed $k$ times is $2\pi i k$, by the same calculation. This is the *generator* of the cyclic group $\pi_1(\mathbb{C}^\times) = \mathbb{Z}$: every closed curve in $\mathbb{C}^\times$ has winding number equal to its homotopy class in $\mathbb{Z}$.

**Inheritance — properties of the punctured plane.** The fact that $I(\gamma; 0) = k$ is not specific to the *unit* circle: any closed curve homotopic (in $\mathbb{C}^\times$) to $\gamma$ has the same winding number. So a wiggly closed curve that goes around the origin $k$ times has winding number $k$, regardless of the specific path. The winding number is a topological invariant, which is what makes it useful — small perturbations of the curve don't change it.

**Two definitions, one answer.** The integral formula and the topological-lift formula give the *same* winding number — this is the content of [[Thm - Existence and Properties of the Winding Number|the existence and properties theorem]]. The integral formula is what we use for computation; the topological-lift formula is what we use for proofs and conceptual arguments (homotopy invariance, integer-valuedness, additivity).

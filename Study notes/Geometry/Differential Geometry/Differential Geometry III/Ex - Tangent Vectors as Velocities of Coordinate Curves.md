---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Coordinate Tangent Vectors"
  - "Def - Velocity of a Curve"
  - "Def - The Tangent Space"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $M$ be a smooth $n$-manifold, $(U, \varphi)$ a smooth chart at $p \in M$ with coordinates $x^{1}, \dots, x^{n}$, and let $e_{i} \in \mathbb{R}^{n}$ denote the $i$-th standard basis vector. For each $i$, define the **$i$-th coordinate curve at $p$** by
$$\gamma_{i} : (-\varepsilon, \varepsilon) \to M, \qquad \gamma_{i}(t) = \varphi^{-1}(\varphi(p) + t\,e_{i})$$
for $\varepsilon$ small enough that $\varphi(p) + t\,e_{i} \in \varphi(U)$ for all $|t| < \varepsilon$.

Show that $\gamma_{i}'(0) = \partial/\partial x^{i}|_{p}$ as tangent vectors in $T_{p}M$.

**Recall:**

![[Def - Coordinate Tangent Vectors#The Definition]]

![[Def - Velocity of a Curve#The Definition]]

---

# Convergent Strategy

**Problem class:** This is a *coordinate-computation identification* problem — show that two concretely-defined tangent vectors at $p$ (the coordinate basis vector $\partial/\partial x^{i}|_{p}$ and the velocity of a specific curve $\gamma_{i}$) are equal. The general routine is: compute both quantities on an arbitrary smooth function $f$ near $p$, and check the outputs agree. Equal action on every $f$ implies equal as derivations.

**Assumption pattern:** The assumption is that $(U, \varphi)$ is a chart at $p$, with $\varphi$ a diffeomorphism onto an open subset of $\mathbb{R}^{n}$. This gives access to coordinate representatives $\hat{f} = f \circ \varphi^{-1}$ of smooth functions. The curve $\gamma_{i}$ is defined to "translate in the $i$-th coordinate direction in the chart, then transport back". By construction, in the chart $\gamma_{i}$ moves at unit speed in the $i$-th direction with all other coordinates fixed. The assumption pattern is then "chart + linear motion in the chart" — and the prediction is that the velocity of this curve will be the $i$-th coordinate-basis vector.

**Theorem routing:** Compute $\gamma_{i}'(0)(f) = (f \circ \gamma_{i})'(0)$ by the [[Def - Velocity of a Curve|definition of velocity]]. Express $f \circ \gamma_{i}$ in terms of the coordinate representative $\hat{f}$: $f \circ \gamma_{i}(t) = f(\varphi^{-1}(\varphi(p) + t\,e_{i})) = \hat{f}(\varphi(p) + t\,e_{i})$. This is a function of $t$ alone — differentiate at $t = 0$ using the one-variable chain rule applied along the $i$-th direction in $\mathbb{R}^{n}$. The result is $(\partial \hat{f}/\partial x^{i})(\varphi(p))$, which is precisely $(\partial/\partial x^{i}|_{p})(f)$ by the [[Def - Coordinate Tangent Vectors|definition of the coordinate tangent vector]].

**Key decision point:** The non-obvious step is recognizing that the velocity of $\gamma_{i}$ at $t = 0$ can be computed *entirely in the chart*: $\hat{f}(\varphi(p) + t\,e_{i})$ is a function of $t$ that we differentiate directly. The temptation is to try to compute the velocity intrinsically on $M$ — by some chart-independent route — but the cleanest path is in the chart. The choice to *work in the chart* and recognize the result as the $i$-th partial derivative is the decisive move.

---

# Legal Operations Used

1. **Express the velocity in coordinates** (operation 9 from the topic page). The velocity $\gamma_{i}'(0)$ is computed by composing $\gamma_{i}$ with an arbitrary smooth function $f$ and differentiating at $t = 0$. Working through the chart converts this to a one-variable derivative of the coordinate representative.

2. **Read off coordinate components** (operation 2). The coordinate basis vector $\partial/\partial x^{i}|_{p}$ is *defined* by its action $(\partial/\partial x^{i}|_{p})(f) = \partial \hat{f}/\partial x^{i}(\varphi(p))$. Showing $\gamma_{i}'(0)$ has this same action identifies them as tangent vectors.

---

# Hints

> [!note]- Hint 1
> Compute $\gamma_{i}'(0)(f) = (f \circ \gamma_{i})'(0)$ directly from the definition of velocity. Use the chart to express $f \circ \gamma_{i}(t)$ as a function of $t$.

> [!note]- Hint 2
> Recognize that $f \circ \gamma_{i}(t) = \hat{f}(\varphi(p) + t\,e_{i})$, where $\hat{f} = f \circ \varphi^{-1}$ is the coordinate representative of $f$. Differentiate this in $t$ using the standard one-variable chain rule applied to a function of $\mathbb{R}^{n}$ moving in a single coordinate direction.

> [!note]- Hint 3
> The derivative at $t = 0$ of $\hat{f}(\varphi(p) + t\,e_{i})$ is the $i$-th partial derivative of $\hat{f}$ at $\varphi(p)$. By the definition of $\partial/\partial x^{i}|_{p}$, this is the action $(\partial/\partial x^{i}|_{p})(f)$.

---

# Solution

The proof is a one-step calculation in the chart, identifying the velocity of the coordinate curve with the $i$-th partial derivative of the coordinate representative — which is the definition of the coordinate tangent vector. The chart converts the abstract tangent-vector identity into a familiar one-variable derivative.

**Step 1: Express the velocity action $\gamma_{i}'(0)(f)$ in the chart.**

Compute $\gamma_{i}'(0)(f) = (f \circ \gamma_{i})'(0)$ for any $f \in C^{\infty}(M)$, and convert to a function of $t$ in the chart.

> [!note]- Derivation
> By the definition of velocity (Lee equation following Proposition 3.23), $\gamma_{i}'(0) \in T_{p}M$ acts on $f \in C^{\infty}(M)$ by
> $$\gamma_{i}'(0)(f) = (f \circ \gamma_{i})'(0).$$
> Now $\gamma_{i}(t) = \varphi^{-1}(\varphi(p) + t\,e_{i})$, so
> $$f \circ \gamma_{i}(t) = f(\varphi^{-1}(\varphi(p) + t\,e_{i})) = (f \circ \varphi^{-1})(\varphi(p) + t\,e_{i}) = \hat{f}(\varphi(p) + t\,e_{i}),$$
> writing $\hat{f} = f \circ \varphi^{-1}$ for the coordinate representative. This is a smooth function of $t \in (-\varepsilon, \varepsilon)$ valued in $\mathbb{R}$.

**Step 2: Differentiate at $t = 0$ using the one-variable chain rule.**

Compute $(f \circ \gamma_{i})'(0)$ and recognize it as the $i$-th partial derivative of $\hat{f}$.

> [!note]- Derivation
> The function $t \mapsto \hat{f}(\varphi(p) + t\,e_{i})$ depends on $t$ only through the $i$-th coordinate of its argument. By the one-variable chain rule (or the multivariate chain rule applied along the $i$-th coordinate direction),
> $$\frac{d}{dt}\bigg|_{t=0} \hat{f}(\varphi(p) + t\,e_{i}) = \frac{\partial \hat{f}}{\partial x^{i}}(\varphi(p)).$$
> (Here we use that $\varphi(p) + t\,e_{i}$ has $j$-th coordinate $\varphi(p)^{j} + t\,\delta^{j}_{i}$, so the rate of change with respect to $t$ is $\delta^{j}_{i}$, and the multivariate chain rule sums $\sum_{j} \delta^{j}_{i}\,\partial_{j}\hat{f}(\varphi(p)) = \partial_{i}\hat{f}(\varphi(p))$.)
>
> Combining with Step 1: $\gamma_{i}'(0)(f) = \partial \hat{f}/\partial x^{i}(\varphi(p))$.

**Step 3: Recognize this as the action of $\partial/\partial x^{i}|_{p}$.**

By the definition of the coordinate tangent vector, this is precisely $(\partial/\partial x^{i}|_{p})(f)$.

> [!note]- Derivation
> By [[Def - Coordinate Tangent Vectors|the definition of coordinate tangent vectors]]:
> $$\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right)(f) = \frac{\partial \hat{f}}{\partial x^{i}}(\varphi(p)).$$
> Comparing with Step 2: $\gamma_{i}'(0)(f) = (\partial/\partial x^{i}|_{p})(f)$ for every smooth $f$. Since both sides are derivations at $p$ taking the same value on every function, they are equal as elements of $T_{p}M$. Hence $\gamma_{i}'(0) = \partial/\partial x^{i}|_{p}$.

> [!note]- Complete formal solution
> Let $\gamma_{i}(t) = \varphi^{-1}(\varphi(p) + t\,e_{i})$ be the $i$-th coordinate curve at $p$. By the definition of velocity, $\gamma_{i}'(0) \in T_{p}M$ acts on $f \in C^{\infty}(M)$ by
> $$\gamma_{i}'(0)(f) = (f \circ \gamma_{i})'(0).$$
> Writing $\hat{f} = f \circ \varphi^{-1}$:
> $$f \circ \gamma_{i}(t) = (f \circ \varphi^{-1})(\varphi(p) + t\,e_{i}) = \hat{f}(\varphi(p) + t\,e_{i}).$$
> By the one-variable chain rule,
> $$\frac{d}{dt}\bigg|_{t=0} \hat{f}(\varphi(p) + t\,e_{i}) = \frac{\partial \hat{f}}{\partial x^{i}}(\varphi(p)).$$
> By the definition of the coordinate tangent vector, this is $(\partial/\partial x^{i}|_{p})(f)$. Since this holds for every $f \in C^{\infty}(M)$, $\gamma_{i}'(0) = \partial/\partial x^{i}|_{p}$ as derivations at $p$. $\qquad\blacksquare$

---

# Key Takeaways

**The coordinate tangent vector $\partial/\partial x^{i}|_{p}$ is geometrically the velocity of motion along the $i$-th coordinate axis at $p$.** This is the *geometric intuition* that motivates the abstract definition of the coordinate basis. The derivation $\partial/\partial x^{i}|_{p}$ is defined algebraically (differentiate the coordinate representative in the $i$-th direction), but the operational meaning is "the velocity of the curve that moves in the $i$-th coordinate direction holding the other coordinates fixed". When you see "$\partial/\partial x^{i}|_{p}$" in differential geometry, you should picture an arrow pointing along the $i$-th coordinate axis at $p$, the way a tangent vector to a curve points in the direction of motion. This grounding is essential for transferring intuition from $\mathbb{R}^{n}$ to abstract manifolds.

**Curve-velocity arguments are the cleanest way to identify tangent vectors.** This exercise illustrates the general method: when you want to show two tangent vectors agree, find smooth functions $f$ to feed them both, and check the resulting numbers agree. Equal action on every $f$ implies equal as derivations. Curves give you a *factory* of tangent vectors — every curve through $p$ produces one — and most computational identifications of tangent vectors in differential geometry are done by picking a clever curve, computing its velocity, and recognizing the result. The pattern repeats in: identifying $T_{I}\mathrm{GL}(n) = M_{n}(\mathbb{R})$ via curves $\gamma(t) = I + tH$; identifying the Lie algebra of $\mathrm{SO}(n)$ as skew-symmetric matrices via curves $\gamma(t) = e^{tA}$; identifying the tangent space to a regular level set as the kernel of the differential via curves staying in the level set. The trigger is "I have a tangent vector specified abstractly; let me realize it as a velocity".

**Charts convert abstract tangent-vector identities to familiar one-variable derivatives.** The proof of this exercise uses a chart to transport the abstract identity $\gamma_{i}'(0) = \partial/\partial x^{i}|_{p}$ to the familiar one-variable identity that the derivative of $\hat{f}(\varphi(p) + t\,e_{i})$ at $t = 0$ is the $i$-th partial derivative of $\hat{f}$ at $\varphi(p)$. The abstract identity is *less obvious* than the chart version because tangent vectors are abstract objects; but in any chart, the identity collapses to a routine multivariate-calculus fact. This is the general pattern: *abstract differential-geometric identities are coordinate-independent packaging of familiar calculus identities*, and the role of the abstract framework is to certify that the calculus identity does not depend on which chart you compute in.

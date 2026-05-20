---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Winding Number"
  - "Thm - Existence and Properties of the Winding Number"
tags: [analysis, complex-analysis]
---

# Problem Statement

Define the figure-eight curve $\gamma : [0, 1] \to \mathbb{C}$ as the concatenation of two loops: $\gamma_1$, the circle of radius $1$ centred at $1$ traversed *counterclockwise* (i.e., $\gamma_1(t) = 1 + e^{2\pi i t}$ for $t \in [0, 1/2]$ with appropriate rescaling), and $\gamma_2$, the circle of radius $1$ centred at $-1$ traversed *clockwise*. The two loops share the common point $z = 0$.

Compute $I(\gamma; w)$ for:
(a) $w = 1$ (centre of the right loop),
(b) $w = -1$ (centre of the left loop),
(c) $w = 3$ (point outside both loops).

**Recall:**

![[Def - Winding Number#The Definition]]

Concatenation property: $I(\gamma_1 \cdot \gamma_2; w) = I(\gamma_1; w) + I(\gamma_2; w)$.

Reversal property: traversing a circle clockwise gives the negative of the counterclockwise winding number.

---

# Convergent Strategy

**Problem class:** Compute winding number for a curve that is a *concatenation* of simpler curves. The strategy is to use additivity to reduce to single-loop winding numbers.

**Assumption pattern:** $\gamma$ is closed (returns to the origin after going around both loops), piecewise $C^1$, and decomposed as $\gamma_1 \cdot \gamma_2$ where each piece is a circle.

**Theorem routing:** Concatenation property $I(\gamma; w) = I(\gamma_1; w) + I(\gamma_2; w)$, then compute each $I(\gamma_i; w)$ separately using the circle calculation (see [[Ex - Computing the winding number of a circle]]).

**Key decision point:** Identify the orientation of each loop. The right loop is counterclockwise (positive); the left loop is clockwise (negative). Track signs carefully.

---

# Legal Operations Used

1. **Apply additivity of winding number** for concatenated curves: $I(\gamma_1 \cdot \gamma_2; w) = I(\gamma_1; w) + I(\gamma_2; w)$.
2. **Compute each loop's winding number** using the circle calculation: a unit circle around its centre has winding number $\pm 1$ depending on orientation.
3. **Use the locally constant property**: the winding number depends only on which component of $\mathbb{C} \setminus \gamma^*$ the point $w$ lies in.
4. **Apply orientation reversal**: $I(\gamma^{-1}; w) = -I(\gamma; w)$.

---

# Hints

> [!note]- Hint 1
> Use the additivity property: $I(\gamma; w) = I(\gamma_1; w) + I(\gamma_2; w)$ since $\gamma$ is the concatenation.

> [!note]- Hint 2
> For (a), the right loop $\gamma_1$ winds once counterclockwise around $w = 1$ (its centre), so $I(\gamma_1; 1) = 1$. The left loop $\gamma_2$ doesn't enclose $1$, so $I(\gamma_2; 1) = 0$.

> [!note]- Hint 3
> For (b), the left loop $\gamma_2$ winds *clockwise* around $w = -1$, so $I(\gamma_2; -1) = -1$. The right loop doesn't enclose $-1$, so $I(\gamma_1; -1) = 0$.

> [!note]- Hint 4
> For (c), $w = 3$ is outside both loops; both winding numbers are zero.

---

# Solution

**Step 1: Decompose**

By additivity, $I(\gamma; w) = I(\gamma_1; w) + I(\gamma_2; w)$ for any $w$ not on either loop.

**Step 2: (a) $w = 1$**

The right loop $\gamma_1$ is a unit circle around $z = 1$, traversed counterclockwise.

> [!note]- Derivation
> Parametrize $\gamma_1(s) = 1 + e^{2\pi i s}$ for $s \in [0, 1]$. By the standard circle calculation (see [[Ex - Computing the winding number of a circle]]), $I(\gamma_1; 1) = 1$ — a unit circle around its centre, traversed counterclockwise, has winding number $1$.
>
> The left loop $\gamma_2$ has image in the disc $\overline{D(-1, 1)}$, which does not contain $w = 1$. So $w = 1$ is in the unbounded component of $\mathbb{C} \setminus \gamma_2^*$ (since the disc $D(-1, 1)$ is the bounded component, and $1 \notin \overline{D(-1, 1)}$). By the unbounded-component property, $I(\gamma_2; 1) = 0$.

So $I(\gamma; 1) = 1 + 0 = 1$.

**Step 3: (b) $w = -1$**

The left loop $\gamma_2$ is a unit circle around $z = -1$, traversed clockwise.

> [!note]- Derivation
> Parametrize $\gamma_2(s) = -1 + e^{-2\pi i s}$ for $s \in [0, 1]$ (the negative exponent encodes clockwise orientation). $I(\gamma_2; -1) = -1$ by the same calculation (a clockwise unit circle around its centre has winding number $-1$).
>
> The right loop $\gamma_1$ has image in $\overline{D(1, 1)}$, which doesn't contain $w = -1$. $I(\gamma_1; -1) = 0$.

So $I(\gamma; -1) = 0 + (-1) = -1$.

**Step 4: (c) $w = 3$**

The point $w = 3$ is in the unbounded component of $\mathbb{C} \setminus \gamma_1^* = \mathbb{C} \setminus \{|z - 1| = 1\}$ (since $|3 - 1| = 2 > 1$), so $I(\gamma_1; 3) = 0$.

> [!note]- Derivation
> Similarly, $w = 3$ is in the unbounded component of $\mathbb{C} \setminus \gamma_2^*$, so $I(\gamma_2; 3) = 0$.

So $I(\gamma; 3) = 0 + 0 = 0$.

> [!note]- Complete formal solution
> By additivity, $I(\gamma; w) = I(\gamma_1; w) + I(\gamma_2; w)$ where $\gamma_1$ is the right loop (counterclockwise) and $\gamma_2$ is the left loop (clockwise).
>
> **(a)** $\gamma_1$ winds counterclockwise around $w = 1$ once: $I(\gamma_1; 1) = 1$. $\gamma_2$ doesn't enclose $1$: $I(\gamma_2; 1) = 0$. Total: $I(\gamma; 1) = 1$.
>
> **(b)** $\gamma_1$ doesn't enclose $-1$: $I(\gamma_1; -1) = 0$. $\gamma_2$ winds clockwise around $-1$ once: $I(\gamma_2; -1) = -1$. Total: $I(\gamma; -1) = -1$.
>
> **(c)** $w = 3$ is outside both loops: $I(\gamma_1; 3) = I(\gamma_2; 3) = 0$. Total: $I(\gamma; 3) = 0$. $\blacksquare$

---

# Key Takeaways

**The winding number partitions $\mathbb{C} \setminus \gamma^*$ into components with different winding numbers.** For the figure-eight, $\mathbb{C}\setminus\gamma^*$ has *three* components — inside the right loop, inside the left loop, and outside — with winding numbers $1$, $-1$, $0$ respectively. The winding number is constant on each component, integer-valued, and vanishes on the unbounded component. This generalizes: for any closed curve, the bounded components of the complement are exactly the regions where the winding number is nonzero.

**Trigger-reaction pattern — concatenation → sum.** When a curve is naturally a concatenation of simpler pieces, *immediately* split the winding number computation. This is the standard divide-and-conquer for winding-number problems: decompose into pieces whose winding numbers are easy, then sum.

**Orientation matters.** A "clockwise" loop has winding number $-1$ around its centre, not $+1$. Standard convention is counterclockwise = positive. Always check the direction of traversal in the parametrization (or geometric picture). For physical applications (Ampère's law, flow circulation), the orientation determines the sign of the corresponding physical quantity.

**Topological character of the winding number.** The value depends only on which region $w$ is in, not on its exact position within the region. Moving $w$ around within a single component doesn't change the winding number. This is the "topological invariance" that makes the winding number useful — small perturbations are invisible to it.

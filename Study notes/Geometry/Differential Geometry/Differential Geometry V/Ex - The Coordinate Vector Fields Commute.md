---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Smooth Vector Field"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $M$ be a smooth manifold and $(U, (x^i))$ a smooth chart on $M$. Show that the coordinate vector fields $\partial/\partial x^i$ and $\partial/\partial x^j$ satisfy

$$\left[\frac{\partial}{\partial x^i}, \frac{\partial}{\partial x^j}\right] = 0 \qquad \text{for every } i, j \in \{1, \dots, n\}.$$

Give two proofs:

**(a)** Via the coordinate formula for the Lie bracket.

**(b)** Via the derivation definition $[X, Y]f = X(Yf) - Y(Xf)$, using equality of mixed partial derivatives for smooth $f$.

**Recall:**

![[Def - The Lie Bracket of Vector Fields#The Definition]]

The bracket has the coordinate formula $[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k$ in any chart.

A coordinate vector field $\partial/\partial x^i$ is defined by its action on smooth functions: $(\partial/\partial x^i) f = \partial f / \partial x^i$, the partial derivative. Equivalently, in the basis $(\partial_1, \dots, \partial_n)$ at every point of $U$, the components of $\partial/\partial x^i$ are $\delta^j_i$ (the Kronecker delta).

---

# Convergent Strategy

**Problem class:** Verify a structural identity for a fundamental family of vector fields. The class is "verify vanishing of a bracket"; the routine is either to apply the coordinate formula (which involves Kronecker-delta components) or to apply the derivation definition (which becomes the equality of mixed partials).

**Assumption pattern:** Two coordinate vector fields are given in a smooth chart. Their components are Kronecker deltas — constants — so the coordinate formula's partial derivatives of components vanish identically. Their actions on smooth functions are partial derivatives, so the derivation-commutator formula becomes the equality of mixed partials.

**Theorem routing:** Two routes, both elementary. (a) The coordinate formula $[X, Y]^k = X^i \partial_i Y^k - Y^i \partial_i X^k$ from [[Thm - Lie Bracket Properties]] reduces to $0$ when the components are constants. (b) The derivation definition reduces to $\partial_i \partial_j f - \partial_j \partial_i f$, which vanishes by Clairaut's theorem (equality of mixed partials for smooth functions).

**Key decision point:** Both proofs are essentially trivial; the *content* is what they teach about why the bracket of coordinate vector fields vanishes. (a) traces the vanishing to the constancy of Kronecker-delta components. (b) traces it to the smoothness of the manifold (which makes Clairaut applicable). Either is a one-line proof, but the underlying reason — equality of mixed partials — is the same.

---

# Legal Operations Used

1. **Operation 5 from the topic page (compute a Lie bracket coordinatewise).** Apply the coordinate formula directly. With components $X^k = \delta^k_i$ and $Y^k = \delta^k_j$, every partial derivative is zero, and the bracket vanishes.

2. **Operation 6 from the topic page (recognize a bracket via the derivation commutator).** Apply $[X, Y]f = X(Yf) - Y(Xf)$, which with $X = \partial/\partial x^i$ and $Y = \partial/\partial x^j$ becomes $\partial_i \partial_j f - \partial_j \partial_i f$. This vanishes by equality of mixed partials.

---

# Hints

> [!note]- Hint 1
> For proof (a): components of $\partial/\partial x^i$ in the basis $(\partial_1, \dots, \partial_n)$ are $(0, \dots, 0, 1, 0, \dots, 0)$ — constants. The coordinate formula involves derivatives of components, which are zero for constants.

> [!note]- Hint 2
> For proof (b): the action of $\partial/\partial x^i$ on a smooth function $f$ is $\partial f / \partial x^i$. So $(\partial/\partial x^i)(\partial/\partial x^j) f = \partial_i \partial_j f$, and the commutator $\partial_i \partial_j - \partial_j \partial_i$ vanishes on smooth functions because mixed partial derivatives commute (Clairaut / Schwarz).

> [!note]- Hint 3
> The result is therefore equivalent to the symmetry of mixed partial derivatives — a fact that requires smoothness of $f$. If $f$ were only $C^1$ with $\partial_i f$ existing but not continuous, the result could fail. The smoothness of the manifold (and of smooth functions on it) is exactly what makes this true.

---

# Solution

The proof has two independent routes, each one-line once the right framework is in place. Plan: (a) apply the coordinate formula and use that components are constants; (b) apply the derivation definition and use equality of mixed partials. Both reduce to the same underlying fact — smooth functions have commuting mixed partials.

**Step 1 (proof (a)): Apply the coordinate formula.**

The coordinate components of $\partial/\partial x^i$ in the basis $(\partial_1, \dots, \partial_n)$ are $X^k = \delta^k_i$ (Kronecker delta). Similarly $Y^k = \delta^k_j$. So in the coordinate formula

$$[\partial/\partial x^i, \partial/\partial x^j]^k = X^l \partial_l Y^k - Y^l \partial_l X^k,$$

every $\partial_l Y^k = \partial_l \delta^k_j = 0$ and $\partial_l X^k = \partial_l \delta^k_i = 0$ (the partial derivatives of constants are zero). Hence each component of the bracket vanishes, and $[\partial/\partial x^i, \partial/\partial x^j] = 0$.

> [!note]- Derivation (Step 1)
> Components: $\partial/\partial x^i$ at any point $p \in U$ is the basis vector $\partial_i|_p$, with coordinate expansion $\partial/\partial x^i = \sum_k \delta^k_i \partial_k$. The components $X^k = \delta^k_i$ are constants — they take the value $1$ if $k = i$, value $0$ otherwise, independent of position.
>
> In the coordinate formula $[X, Y]^k = X^l \partial_l Y^k - Y^l \partial_l X^k$, we have
> $$[X, Y]^k = \sum_l \delta^l_i \partial_l \delta^k_j - \sum_l \delta^l_j \partial_l \delta^k_i = \partial_i \delta^k_j - \partial_j \delta^k_i = 0 - 0 = 0,$$
> since the Kronecker delta $\delta^k_j$ is a constant in any coordinate, with zero partial derivative.
>
> Hence $[\partial/\partial x^i, \partial/\partial x^j] = \sum_k 0 \cdot \partial_k = 0$.

**Step 2 (proof (b)): Apply the derivation definition.**

For $f \in C^\infty(U)$,
$$[\partial/\partial x^i, \partial/\partial x^j] f = \frac{\partial}{\partial x^i}\left(\frac{\partial f}{\partial x^j}\right) - \frac{\partial}{\partial x^j}\left(\frac{\partial f}{\partial x^i}\right) = \frac{\partial^2 f}{\partial x^i \partial x^j} - \frac{\partial^2 f}{\partial x^j \partial x^i}.$$

By Clairaut's theorem on equality of mixed partial derivatives (applicable because $f$ is smooth, hence $C^2$), $\partial^2 f / \partial x^i \partial x^j = \partial^2 f / \partial x^j \partial x^i$. So the bracket annihilates every smooth function, hence the bracket is the zero vector field.

> [!note]- Derivation (Step 2)
> Recall: the action of $\partial/\partial x^i$ on $f \in C^\infty(U)$ is the partial derivative $\partial f / \partial x^i$.
>
> So $[\partial/\partial x^i, \partial/\partial x^j]f = (\partial/\partial x^i)((\partial/\partial x^j) f) - (\partial/\partial x^j)((\partial/\partial x^i) f) = \partial_i \partial_j f - \partial_j \partial_i f$.
>
> Since $f$ is smooth on $U \subseteq M$ (and the local coordinates make $U$ effectively a piece of $\mathbb{R}^n$), Clairaut's theorem gives $\partial_i \partial_j f = \partial_j \partial_i f$, so $[\partial/\partial x^i, \partial/\partial x^j]f = 0$.
>
> Since $f$ was arbitrary smooth on $U$, the vector field $[\partial/\partial x^i, \partial/\partial x^j]$ annihilates every smooth function, so by the derivation criterion ([[Def - Smooth Vector Field]] characterization 3), it must be the zero vector field.

> [!note]- Complete formal solution
> Let $(U, (x^i))$ be a smooth chart and $i, j \in \{1, \dots, n\}$.
>
> **Proof via the coordinate formula.** In the basis $(\partial_1, \dots, \partial_n)$, the coordinate vector field $\partial/\partial x^i$ has components $X^k = \delta^k_i$ (Kronecker delta) and $\partial/\partial x^j$ has components $Y^k = \delta^k_j$. These are constants on $U$, so $\partial_l X^k = \partial_l Y^k = 0$ for all $l, k$. The coordinate formula then gives
> $$[\partial/\partial x^i, \partial/\partial x^j]^k = \sum_l (X^l \partial_l Y^k - Y^l \partial_l X^k) = 0$$
> for every $k$. Hence $[\partial/\partial x^i, \partial/\partial x^j] = 0$ as vector fields.
>
> **Proof via the derivation definition.** For any $f \in C^\infty(U)$,
> $$[\partial/\partial x^i, \partial/\partial x^j]f = \frac{\partial}{\partial x^i}\left(\frac{\partial f}{\partial x^j}\right) - \frac{\partial}{\partial x^j}\left(\frac{\partial f}{\partial x^i}\right) = \frac{\partial^2 f}{\partial x^i \partial x^j} - \frac{\partial^2 f}{\partial x^j \partial x^i} = 0$$
> by Clairaut's theorem on equality of mixed partial derivatives, applicable since $f$ is smooth. Hence the vector field $[\partial/\partial x^i, \partial/\partial x^j]$ annihilates every smooth function on $U$, and by the derivation characterization of smooth vector fields it must be zero.
>
> Both proofs give $[\partial/\partial x^i, \partial/\partial x^j] = 0$, with the second proof making the connection to equality of mixed partials explicit. $\qquad\blacksquare$

---

# Key Takeaways

**The vanishing of $[\partial_i, \partial_j]$ is the geometric form of equality of mixed partials.** This is the central insight: the bracket vanishes because smooth functions have $\partial_i \partial_j f = \partial_j \partial_i f$. The coordinate formula reformulates this in terms of constant components, but the underlying analytic fact is Clairaut. The trigger to remember this: whenever you see a bracket of two coordinate-like vector fields, expect it to vanish, and the reason will be the symmetry of mixed partials of a smooth function. This is also the geometric reason why coordinate frames are "trivial" — they are the easiest possible frames.

**A frame is a coordinate frame if and only if it is a commuting frame (locally).** This is the converse direction (the multi-field Straightening Theorem, Lee 9.46): a smooth local frame $(E_1, \dots, E_n)$ on $U \subseteq M$ with $[E_i, E_j] = 0$ for all $i, j$ is locally the coordinate frame of some chart. So the property "$[\partial_i, \partial_j] = 0$" is both *necessary* (this exercise) and *sufficient* (Lee 9.46) for a frame to be a coordinate frame. The bracket therefore obstructs the existence of "global coordinates" — a frame whose brackets do not vanish cannot be a coordinate frame, even locally. This is the rank-$n$ version of the [[Thm - Canonical Form for a Nonvanishing Vector Field|Straightening Theorem]].

**Smoothness of the manifold is the analytical input for everything.** The proof of the bracket vanishing uses smoothness of $f$ via Clairaut; the smoothness of the manifold is what guarantees smooth $f$ exist in abundance (via partitions of unity and bump functions). So the bracket-vanishing of coordinate vector fields is a *consequence* of the smooth manifold's structure, not an additional assumption. This is the kind of innocuous-looking fact that pervades differential geometry: smoothness gives you symmetric mixed partials, and symmetric mixed partials give you commuting coordinate vector fields, and commuting coordinate vector fields give you the multi-field Straightening Theorem.

**The two proofs use different sides of $[X, Y]$ as a derivation.** Proof (a) treats the bracket as a vector field with components, focusing on the constancy of the input components. Proof (b) treats the bracket as an operator on functions, focusing on its action via mixed partials. Both proofs give the same answer, but they teach different lessons: (a) is the "structural" route (bracket as functor of components), (b) is the "operator" route (bracket as commutator of derivations). The choice of route in a more complex problem depends on which presentation of the vector fields is more natural — coordinate-explicit or derivation-explicit.

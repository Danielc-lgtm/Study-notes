---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Sectional Curvature"
  - "Def - Riemann Curvature Tensor"
  - "Def - Constant Sectional Curvature"
tags: [geometry, riemannian-geometry, curvature, sphere]
---

# Problem Statement

Let $S^n \subset \mathbb{R}^{n+1}$ be the unit $n$-sphere with the round metric $g$ induced from the standard Euclidean metric on $\mathbb{R}^{n+1}$. Show that $S^n$ has **constant sectional curvature** $K \equiv 1$ — that is, every tangent $2$-plane $\sigma \subset T_pS^n$ at every point $p \in S^n$ satisfies $K(\sigma) = 1$.

**Recall:**

A [[Def - Sectional Curvature|sectional curvature]] of a $2$-plane $\sigma = \mathrm{span}(X, Y) \subset T_pM$ is
$$K(\sigma) = \frac{\langle R(X, Y)Y, X\rangle}{|X|^2|Y|^2 - \langle X, Y\rangle^2}.$$

The [[Def - Riemann Curvature Tensor|Riemann curvature tensor]] $R$ is defined via $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$.

$S^n \subset \mathbb{R}^{n+1}$ is the level set $\{|x| = 1\}$, with tangent space $T_p S^n = p^\perp = \{v \in \mathbb{R}^{n+1} : \langle v, p\rangle = 0\}$, where $\langle\cdot, \cdot\rangle$ is the Euclidean inner product on $\mathbb{R}^{n+1}$.

The **outward unit normal** to $S^n$ at $p$ is $N(p) = p$ (since $|p| = 1$).

---

# Convergent Strategy

**Problem class:** This is a computation problem — compute the Riemann curvature tensor of a specific Riemannian manifold (the round sphere) and read off the sectional curvature. There are two standard routes: (a) the **Gauss equation** for hypersurfaces, expressing the intrinsic Riemann tensor in terms of the ambient (flat) curvature and the second fundamental form; (b) the **Cartan structural equations** in an orthonormal frame. Method (a) is the more illuminating because it makes the role of the sphere's *convexity* (encoded in the second fundamental form being $-I$) directly visible.

**Assumption pattern:** The sphere $S^n$ has a nontrivial second fundamental form because it is a curved hypersurface in $\mathbb{R}^{n+1}$. The ambient space $\mathbb{R}^{n+1}$ is flat, $R^{\mathbb{R}^{n+1}} = 0$. The Gauss equation then expresses *all* of the intrinsic Riemann tensor of $S^n$ in terms of the second fundamental form alone. The second fundamental form of $S^n$ has a particularly simple form (proportional to the metric): this is the geometric content of "the sphere is everywhere convex in the same way."

**Theorem routing:** **Gauss's equation** $R^V(X, Y, Z, W) = R^M(X, Y, Z, W) + B(Y, Z)B(X, W) - B(X, Z)B(Y, W)$ for a hypersurface $V \subset M$, where $B$ is the second fundamental form. For $M = \mathbb{R}^{n+1}$ (flat, $R^M = 0$) and $V = S^n$ with $B(X, Y) = -\langle X, Y\rangle$ (since the unit normal at $p$ is $p$ and the Weingarten map is $-\mathrm{id}$), Gauss's equation reduces to $R^{S^n}(X, Y, Z, W) = \langle Y, Z\rangle\langle X, W\rangle - \langle X, Z\rangle\langle Y, W\rangle$.

**Key decision point:** The Weingarten map / second fundamental form sign. The outward normal at $p \in S^n$ is $p$ itself; the Weingarten map (negative of the derivative of $N$ along tangent directions) is $-\mathrm{id}$ on $T_pS^n$. So the second fundamental form is $B(X, Y) = \langle X, -(-Y)\rangle = \langle X, Y\rangle$... wait, sign conventions vary; the safe choice is to compute the principal curvatures directly. All principal curvatures of $S^n$ are equal (by symmetry); their value is $\pm 1$ depending on sign convention. The cleanest is to verify directly that $\kappa_i = -1$ when using the outward normal convention (so $B = -g$), giving $K = (-1)(-1) - 0 = +1$. The whole subtlety is in this sign choice; once fixed, everything else is automatic.

---

# Legal Operations Used

1. **Operation 3 from the topic page (Cartan's structural equations).** Used as an alternative route: compute the curvature 2-form directly in an orthonormal frame on $S^n$. The route is mechanical but conceptually cleaner than the Gauss equation in some cases.

2. **Operation 4 from the topic page (trace Riemann to descend to sectional curvature).** After computing $R$, the sectional curvature is read off as $K(X \wedge Y) = \langle R(X, Y)Y, X\rangle$ for orthonormal $X, Y$.

---

# Hints

> [!note]- Hint 1
> Use the Gauss equation for a hypersurface in $\mathbb{R}^{n+1}$. The ambient curvature is $0$. What is the second fundamental form of $S^n \subset \mathbb{R}^{n+1}$?

> [!note]- Hint 2
> The unit outward normal to $S^n$ at $p$ is $N(p) = p$ itself. Compute the Weingarten map / shape operator $S(X) = -\nabla^{\mathbb{R}^{n+1}}_X N = -X$, the negative of the identity on $T_pS^n$. So the second fundamental form is $B(X, Y) = \langle S(X), Y\rangle = -\langle X, Y\rangle$ (note the sign convention!).

> [!note]- Hint 3
> Substitute $B(X, Y) = -\langle X, Y\rangle$ into Gauss's equation: $R^{S^n}(X, Y, Z, W) = 0 + (-\langle Y, Z\rangle)(-\langle X, W\rangle) - (-\langle X, Z\rangle)(-\langle Y, W\rangle) = \langle Y, Z\rangle\langle X, W\rangle - \langle X, Z\rangle\langle Y, W\rangle$. Now read off $K(X \wedge Y)$.

> [!note]- Hint 4
> $\langle R(X, Y)Y, X\rangle = R^{S^n}(X, Y, Y, X) = \langle Y, Y\rangle\langle X, X\rangle - \langle X, Y\rangle\langle Y, X\rangle = |X|^2|Y|^2 - \langle X, Y\rangle^2$. So $K(X \wedge Y) = 1$.

---

# Solution

The proof has two key steps. **Step 1** computes the second fundamental form of $S^n \subset \mathbb{R}^{n+1}$ using the outward normal $N(p) = p$ and the Weingarten map. **Step 2** applies Gauss's equation for a hypersurface in flat space, reading off the formula $R^{S^n}(X, Y, Z, W) = \langle Y, Z\rangle\langle X, W\rangle - \langle X, Z\rangle\langle Y, W\rangle$ and verifying $K \equiv 1$ from it.

**Step 1: The second fundamental form of $S^n$ is $B = -g$ (with outward normal convention).**

> [!note]- Derivation
> The outward unit normal to $S^n$ at $p \in S^n$ is $N(p) = p$ itself (since $|p| = 1$ and $p$ is perpendicular to $T_pS^n = p^\perp$). The **Weingarten map** (shape operator) is $S : T_pS^n \to T_pS^n$ defined by $S(X) = -\nabla^{\mathbb{R}^{n+1}}_X N$, where $\nabla^{\mathbb{R}^{n+1}}$ is the flat ambient connection.
>
> Compute: for $X \in T_pS^n$, $\nabla^{\mathbb{R}^{n+1}}_X N = \nabla^{\mathbb{R}^{n+1}}_X (\mathrm{id})_p = X$ (the directional derivative of the identity map in direction $X$ is $X$). So $S(X) = -X$.
>
> The second fundamental form is $B(X, Y) = \langle S(X), Y\rangle = \langle -X, Y\rangle = -\langle X, Y\rangle$.

**Step 2: Apply Gauss's equation, get $R^{S^n}(X, Y, Z, W) = \langle Y, Z\rangle\langle X, W\rangle - \langle X, Z\rangle\langle Y, W\rangle$, hence $K \equiv 1$.**

> [!note]- Derivation
> **Gauss's equation** for a hypersurface $V \subset M$:
> $$R^V(X, Y, Z, W) = R^M(X, Y, Z, W) + B(Y, Z)B(X, W) - B(X, Z)B(Y, W).$$
> For $V = S^n$, $M = \mathbb{R}^{n+1}$: $R^M = 0$ (flat), $B(X, Y) = -\langle X, Y\rangle$. Substitute:
> $$R^{S^n}(X, Y, Z, W) = (-\langle Y, Z\rangle)(-\langle X, W\rangle) - (-\langle X, Z\rangle)(-\langle Y, W\rangle) = \langle Y, Z\rangle\langle X, W\rangle - \langle X, Z\rangle\langle Y, W\rangle.$$
> Equivalently, $R^{S^n}(X, Y)Z = \langle Y, Z\rangle X - \langle X, Z\rangle Y$ — the constant-sectional-curvature form with $K_0 = 1$.
>
> Now compute the sectional curvature: $\langle R^{S^n}(X, Y)Y, X\rangle = R^{S^n}(X, Y, Y, X) = \langle Y, Y\rangle\langle X, X\rangle - \langle X, Y\rangle\langle Y, X\rangle = |X|^2|Y|^2 - \langle X, Y\rangle^2 = |X \wedge Y|^2$. So
> $$K(X \wedge Y) = \frac{|X \wedge Y|^2}{|X \wedge Y|^2} = 1.$$
> Constant, identically $1$, on every tangent $2$-plane at every point. ∎

> [!note]- Complete formal solution
> Let $p \in S^n$ and $X, Y \in T_pS^n$ a $2$-plane basis. The outward unit normal is $N(p) = p$; the Weingarten map is $S(X) = -\nabla^{\mathbb{R}^{n+1}}_X N = -X$ (since $N$ is the identity vector field restricted to $S^n$). The second fundamental form is $B(X, Y) = \langle S(X), Y\rangle = -\langle X, Y\rangle$.
>
> Gauss's equation for $V = S^n \subset M = \mathbb{R}^{n+1}$ (with $R^M = 0$):
> $$R^{S^n}(X, Y, Z, W) = B(Y, Z)B(X, W) - B(X, Z)B(Y, W) = \langle Y, Z\rangle\langle X, W\rangle - \langle X, Z\rangle\langle Y, W\rangle.$$
> Therefore $\langle R^{S^n}(X, Y)Y, X\rangle = |X|^2|Y|^2 - \langle X, Y\rangle^2 = |X \wedge Y|^2$, and
> $$K(X \wedge Y) = \frac{\langle R^{S^n}(X, Y)Y, X\rangle}{|X|^2|Y|^2 - \langle X, Y\rangle^2} = 1.$$
> Since $p$ and the $2$-plane were arbitrary, $S^n$ has constant sectional curvature $K \equiv 1$.

---

# Key Takeaways

**Convexity of a hypersurface in flat space is the source of its sectional curvature.** The sphere has constant positive sectional curvature because it is everywhere convex in the same way — its second fundamental form $B = -g$ (with the outward normal convention) is a constant scalar multiple of the metric. This is the geometric meaning of "every tangent direction is curving in the same way." More generally, for any hypersurface $V \subset \mathbb{R}^{n+1}$, the Gauss equation $R^V = B \wedge B$ (in shorthand) says the intrinsic curvature is *entirely* the convexity data — and convexity is captured by $B$. When you see a problem about hypersurfaces in Euclidean space, this Gauss-equation route is almost always the right first move.

**Constant sectional curvature is a very strong condition, characterised by the simplest possible Riemann tensor.** Once you compute $R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$, you have determined the *entire* Riemann tensor up to the single number $K_0$. There is no further computation needed; this single algebraic form encodes every component of $R$ and every comparison-geometric inequality. Recognise this trigger: if a manifold has high symmetry (homogeneous + isotropic, e.g., $S^n, \mathbb{R}^n, H^n$, or any space form), expect constant sectional curvature, and use the explicit Riemann-tensor form to bypass tedious component-by-component computations.

**The sign convention in the Weingarten map / second fundamental form is the standard pitfall.** The convention $S(X) = -\nabla N$ (so $B = -g$ for $S^n$, giving $K = +1$) is consistent with "positive sectional curvature for a convex hypersurface curving away from the normal." The opposite convention $S(X) = +\nabla N$ flips signs everywhere; you can end up with $K = -1$ on $S^n$, which is wrong. Always double-check by computing on a known example: the sphere should give $K = +1$, the hyperbolic plane $K = -1$, Euclidean space $K = 0$. These calibration checks are essential before trusting any sectional-curvature calculation.

**Comparison exercise: this is the simplest possible application of Gauss's equation; the Schwarzschild calculation (see [[Ex - Schwarzschild Sectional Curvatures (Statement)]]) is the same technique applied to a more complicated geometry.**

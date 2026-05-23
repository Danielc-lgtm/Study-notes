---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - de Rham Cohomology"
  - "Thm - The Poincaré Lemma on a Star-Shaped Region"
tags: [geometry, differential-geometry, cohomology]
---

# Problem Statement

Compute the de Rham cohomology of $\mathbb{R}^n$ for $n \geq 1$: show that $H^0_{dR}(\mathbb{R}^n) = \mathbb{R}$ and $H^k_{dR}(\mathbb{R}^n) = 0$ for $k \geq 1$.

**Recall:**

![[Def - de Rham Cohomology#The Definition]]

![[Thm - The Poincaré Lemma on a Star-Shaped Region#Statement]]

---

# Convergent Strategy

**Problem class:** This is a direct computation of de Rham cohomology for a contractible domain — the simplest non-trivial cohomology computation, and the base case for all subsequent Mayer–Vietoris arguments. The pattern: "compute $H^*$ of a manifold, identify it as a contractible space, apply the relevant cohomology vanishing theorem."

**Assumption pattern:** $\mathbb{R}^n$ is open and star-shaped about every point (in fact convex), so the Poincaré lemma applies. The cohomology computation is then a triviality theorem ("trivial in positive degrees") plus a counting argument in degree 0.

**Theorem routing:** [[Thm - The Poincaré Lemma on a Star-Shaped Region]] gives $H^k_{dR}(\mathbb{R}^n) = 0$ for $k \geq 1$ directly. For $H^0_{dR}$, use that a closed $0$-form is locally constant, and $\mathbb{R}^n$ is connected.

**Key decision point:** The only "interesting" step is recognizing that the Poincaré lemma is precisely the conclusion we want — there is no further work after identifying $\mathbb{R}^n$ as star-shaped. The result is the canonical example of "cohomology vanishes because the domain is contractible."

---

# Legal Operations Used

1. **Apply the Poincaré lemma on a contractible open set** (operation 2 from the topic page). $\mathbb{R}^n$ is star-shaped about $0$ (indeed convex), so the lemma gives $H^k_{dR}(\mathbb{R}^n) = 0$ for $k \geq 1$ directly.

2. **Read $H^0_{dR}$ as a connected-components count** (operation 9 from the topic page). $\mathbb{R}^n$ is connected, so $H^0_{dR}(\mathbb{R}^n) = \mathbb{R}^1 = \mathbb{R}$.

---

# Hints

> [!note]- Hint 1
> What is the [[Def - Homotopy|homotopy]] type of $\mathbb{R}^n$? Is it contractible? Star-shaped about a point?

> [!note]- Hint 2
> The Poincaré lemma applied to a star-shaped open set $U \subseteq \mathbb{R}^n$ says $H^k_{dR}(U) = 0$ for $k \geq 1$. Identify $\mathbb{R}^n$ with such a $U$.

> [!note]- Hint 3
> For $H^0$: $Z^0(\mathbb{R}^n)$ is the space of smooth $f$ with $df = 0$. What does this force?

---

# Solution

The proof is a direct application of the Poincaré lemma and the connectedness of $\mathbb{R}^n$. Step 1 identifies $\mathbb{R}^n$ as star-shaped, so the Poincaré lemma applies and gives the positive-degree vanishing. Step 2 handles degree 0 by direct computation: closed $0$-forms are locally constant, and $\mathbb{R}^n$ connected forces them to be constant.

**Step 1: For $k \geq 1$, $H^k_{dR}(\mathbb{R}^n) = 0$.**

> [!note]- Derivation
> $\mathbb{R}^n$ is star-shaped about any point (e.g. the origin): for any $x \in \mathbb{R}^n$, the segment $\{tx : t \in [0, 1]\}$ from $0$ to $x$ lies entirely in $\mathbb{R}^n$. By [[Thm - The Poincaré Lemma on a Star-Shaped Region]], every star-shaped open subset of $\mathbb{R}^n$ has trivial de Rham cohomology in positive degrees. Hence $H^k_{dR}(\mathbb{R}^n) = 0$ for $k \geq 1$.

**Step 2: $H^0_{dR}(\mathbb{R}^n) = \mathbb{R}$.**

> [!note]- Derivation
> A closed $0$-form on $\mathbb{R}^n$ is a smooth function $f$ with $df = 0$. The condition $df = 0$ means $\partial_i f = 0$ for every $i$, i.e. $f$ is locally constant. Since $\mathbb{R}^n$ is connected, $f$ is constant. Hence $Z^0(\mathbb{R}^n) = \{\text{constant functions}\} \cong \mathbb{R}$. There are no $(-1)$-forms, so $B^0(\mathbb{R}^n) = 0$ by convention, and $H^0_{dR}(\mathbb{R}^n) = Z^0 / B^0 = \mathbb{R} / 0 = \mathbb{R}$.

> [!note]- Complete formal solution
> $\mathbb{R}^n$ is open in $\mathbb{R}^n$ and star-shaped about the origin (for any $x \in \mathbb{R}^n$ and $t \in [0, 1]$, $tx \in \mathbb{R}^n$). By [[Thm - The Poincaré Lemma on a Star-Shaped Region]], every star-shaped open set has $H^k_{dR} = 0$ for $k \geq 1$. Hence $H^k_{dR}(\mathbb{R}^n) = 0$ for $k \geq 1$.
>
> In degree $0$: $Z^0(\mathbb{R}^n) = \{f \in C^\infty(\mathbb{R}^n) : df = 0\}$. The condition $df = 0$ means $\partial_i f \equiv 0$ for all $i$, i.e. $f$ is locally constant. Since $\mathbb{R}^n$ is connected (any two points joined by a straight segment), $f$ is constant. So $Z^0(\mathbb{R}^n) = \mathbb{R}$. The space $B^0(\mathbb{R}^n) = 0$ by convention (there are no $(-1)$-forms). Hence $H^0_{dR}(\mathbb{R}^n) = \mathbb{R}/0 = \mathbb{R}$. $\blacksquare$

---

# Key Takeaways

**The Poincaré lemma is the master local result for cohomology computations.** Every cohomology computation of a non-trivial manifold ultimately reduces, via Mayer–Vietoris or a good cover, to the case of contractible (often Euclidean) pieces — and on each such piece the Poincaré lemma gives trivial cohomology in positive degrees. So this exercise, while elementary, is the *base case* for essentially every cohomology computation that follows. Whenever you compute $H^*_{dR}$ of a complicated manifold by a cover argument, you are implicitly using this result on each piece of the cover. The trigger to recognize the pattern: any time the manifold (or open piece thereof) is contractible — Euclidean, star-shaped, convex, deformable to a point — the cohomology is zero in positive degrees and $\mathbb{R}$ in degree zero.

**$H^0_{dR}$ counts connected components.** This is a clean computational handle on the topology of $M$: $H^0_{dR}(M) = \mathbb{R}^{\#\text{components}}$. It is the *only* de Rham [[Def - Group|group]] that has such a transparent combinatorial meaning, and it is often used as a sanity check on more complex computations. If you compute $H^*$ of a manifold and the $H^0$ does not match the connected-component count, your other [[Def - Group|groups]] are also wrong. The trigger: any time you want a quick numerical handle on a manifold's connectedness, compute $H^0_{dR}$ first.

**Star-shaped is *strictly stronger* than contractible — but cohomology can't tell the difference.** The proof here uses star-shapedness, which is a metric/affine condition. The conclusion ($H^k_{dR} = 0$ for $k \geq 1$) is preserved under [[Def - Homotopy|homotopy]] equivalence, so it holds for *any* contractible space. The cohomology is insensitive to the specific contraction; only the existence of *some* contraction matters. This is a small but important instance of the general phenomenon: smooth structure (or affine structure) imposes more conditions than are needed for cohomology results, which are homotopy-invariant. *Companion exercise:* [[Ex - The de Rham Cohomology of the Torus]] uses this homotopy-invariance crucially when expressing the torus cohomology via products of the circle.

**The Poincaré lemma is also a constructive existence theorem.** Beyond the abstract vanishing $H^k = 0$, the lemma provides an *explicit* primitive: for a closed $1$-form $\omega = \sum F_j\,dx^j$ on $\mathbb{R}^n$, the primitive is $f(x) = \int_0^1 \sum F_j(tx) x_j\,dt$. For higher-degree forms there is an analogous homotopy operator formula. So whenever you need to integrate a closed form on Euclidean space — e.g. to find an electromagnetic potential from a field strength — the Poincaré lemma not only tells you a primitive exists but tells you what it is. This is the constructive content of the abstract triviality statement.

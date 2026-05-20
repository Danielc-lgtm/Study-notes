---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Primitive (Antiderivative)"
  - "Def - Domain in the Complex Plane"
  - "Def - Contour Integral"
  - "Thm - Fundamental Theorem of Contour Integration"
tags: [analysis, complex-analysis]
---

# Notation

$D \subseteq \mathbb{C}$ a [[Def - Domain in the Complex Plane|domain]] (open and path-connected); $f : D \to \mathbb{C}$ continuous. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Statement

> **Theorem (existence of a primitive iff closed integrals vanish).** Let $D \subseteq \mathbb{C}$ be a [[Def - Domain in the Complex Plane|domain]] (open and path-connected) and $f : D \to \mathbb{C}$ continuous. Then the following are equivalent:
>
> 1. $f$ has a primitive on $D$: there exists a holomorphic $F : D \to \mathbb{C}$ with $F'(z) = f(z)$ for every $z \in D$.
> 2. $\int_\gamma f(z)\,dz = 0$ for every closed piecewise $C^1$ curve $\gamma$ in $D$.
>
> When these conditions hold, a primitive is given explicitly, after choosing a base point $a_0 \in D$, by $F(w) = \int_{\gamma_w} f(z)\,dz$ along any piecewise $C^1$ curve $\gamma_w$ in $D$ from $a_0$ to $w$.

---

# Motivation

The forward direction — primitives give path-independence — is the fundamental theorem of contour integration. The converse — *path-independence forces a primitive to exist* — is the deeper and more useful result. Together they give a characterization: $f$ has a primitive on $D$ if and only if $\int_\gamma f\,dz = 0$ for every closed loop $\gamma$. This converts the analytic question "does $F$ exist with $F' = f$?" into the integral question "do all closed-loop integrals vanish?", which is checkable theorem-by-theorem (e.g., Cauchy's theorem, Goursat).

The converse construction is the integration-as-construction technique: pick a base point $a_0$, define $F(w) = \int_{a_0}^w f\,dz$ along any path (well-defined by hypothesis), and verify $F' = f$. This produces *the* primitive, up to a constant.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$\int_\gamma f\,dz = 0$ for every closed $\gamma$ in $D$".

The first disguised source is **Cauchy's theorem on simply connected domains**: provides the vanishing hypothesis automatically when $D$ is simply connected and $f$ is holomorphic.

The second disguised source is **Goursat's theorem (triangle version)**: the more refined "vanishing on triangles" — sufficient via Lemma 2.1.6 to give path-independence on star-shaped domains.

**Targets (Output Amplification)**

The conclusion is "$f$ has a primitive on $D$".

Combine with **explicit construction.** Property $D$: a base point $a_0$. The amplified result: an explicit primitive $F(w) = \int_{a_0}^w f\,dz$.

Combine with **uniqueness of primitives.** Property $D$: two primitives. The amplified result: they differ by a constant, by [[Thm - Constant on a Domain if Derivative is Zero]].

---

# Why Is It True

For the *forward* direction (primitive $\Rightarrow$ vanishing): see [[Thm - Fundamental Theorem of Contour Integration]].

For the *converse* (vanishing $\Rightarrow$ primitive): pick a base point $a_0 \in D$. For each $w \in D$, choose any piecewise $C^1$ curve $\gamma_w$ in $D$ from $a_0$ to $w$ (exists by path-connectedness), and define
$$F(w) := \int_{\gamma_w} f\,dz.$$
This is well-defined: if $\gamma_1, \gamma_2$ are two such curves, their concatenation $\gamma_1 + (-\gamma_2)$ is closed, so $\int_{\gamma_1} - \int_{\gamma_2} = \int_{\gamma_1 + (-\gamma_2)} = 0$ by hypothesis, hence the values agree.

To verify $F'(w) = f(w)$: take any $h$ small enough so the line segment $\delta_h$ from $w$ to $w + h$ lies in $D$. Then
$$F(w + h) - F(w) = \int_{\delta_h} f\,dz = \int_0^1 f(w + th) \cdot h\,dt.$$
So
$$\frac{F(w + h) - F(w)}{h} - f(w) = \int_0^1 [f(w + th) - f(w)]\,dt.$$
As $h \to 0$, by continuity of $f$ at $w$, the integrand goes to zero uniformly, so the integral goes to zero. Hence $F'(w) = f(w)$.

The technical heart is two-fold: well-definedness (uses the vanishing hypothesis) and differentiability (uses continuity of $f$). Both are elementary once the construction is set up.

---

# What Makes This Hard

The non-obvious step is recognizing that the *integration construction* $F(w) = \int_{a_0}^w f\,dz$ is the natural way to build a primitive. The hypothesis "all closed-loop integrals vanish" is what makes the construction well-defined; without it, $F$ depends on the choice of path. The most common error is to forget the path-connectedness of $D$ — needed to ensure paths from $a_0$ to any $w$ exist.

---

# Rederivation Scaffold

**High-level strategy:**
Forward: apply [[Thm - Fundamental Theorem of Contour Integration]]. Converse: build $F(w) = \int_{a_0}^w f\,dz$, show well-defined (vanishing hypothesis) and differentiable with $F' = f$ (continuity of $f$).

**Subgoal decomposition:**

1. **Forward direction.** Apply FT contour integration: if $F$ is a primitive of $f$, $\int_\gamma f = F(\gamma(b)) - F(\gamma(a)) = 0$ for closed $\gamma$.

2. **Converse: define $F$.** Pick $a_0 \in D$. For each $w$, define $F(w) = \int_{\gamma_w} f\,dz$ for any piecewise $C^1$ $\gamma_w$ from $a_0$ to $w$.

3. **Well-defined.** Two paths give the same value by the closed-loop hypothesis applied to their concatenation.

4. **$F$ is holomorphic with $F' = f$.** Difference quotient $F(w + h) - F(w))/h$ equals the average of $f$ along a small segment, which tends to $f(w)$ by continuity.

---

# Lemma Decomposition

> [!note]- Lemma 1: Well-definedness of $F$
> **Statement:** Under the closed-loop vanishing hypothesis, $F(w) := \int_\gamma f\,dz$ depends only on $w$, not on the path $\gamma$ from $a_0$ to $w$.
>
> **Hint:** Concatenate $\gamma_1$ with $-\gamma_2$; the result is closed.
>
> > [!note]- Full proof
> > Let $\gamma_1, \gamma_2$ both go from $a_0$ to $w$. Then $\gamma := \gamma_1 + (-\gamma_2)$ is closed. By hypothesis, $\int_\gamma f\,dz = 0$, i.e., $\int_{\gamma_1} f\,dz - \int_{\gamma_2} f\,dz = 0$. $\blacksquare$

> [!note]- Lemma 2: $F$ is differentiable with $F' = f$
> **Statement:** The function $F$ defined above is holomorphic on $D$ with $F'(w) = f(w)$.
>
> **Hint:** Use a line segment from $w$ to $w + h$ and continuity of $f$ at $w$.
>
> > [!note]- Full proof
> > Fix $w \in D$; choose $r > 0$ with $D(w, r) \subseteq D$. For $|h| < r$, let $\delta_h(t) = w + th$ for $t \in [0, 1]$ — the line segment, lying in $D(w, r)$. Then by well-definedness, $F(w + h) - F(w) = \int_{\delta_h} f\,dz = \int_0^1 f(w + th) \cdot h\,dt$. So
> > $$\frac{F(w + h) - F(w)}{h} - f(w) = \int_0^1 [f(w + th) - f(w)]\,dt.$$
> > Bound: $|f(w + th) - f(w)| \leq \sup_{|z - w| \leq |h|} |f(z) - f(w)| \to 0$ as $h \to 0$ (continuity of $f$ at $w$). So the integral on the right is bounded by this sup (uniformly in $t \in [0, 1]$) times $1$, which goes to zero. Hence $F'(w) = f(w)$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Forward: if $f$ has a primitive $F$, then by [[Thm - Fundamental Theorem of Contour Integration]], $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a)) = 0$ for closed $\gamma$.
>
> Converse: by Lemmas 1 and 2, $F(w) := \int_{a_0}^w f\,dz$ (any path) is well-defined and holomorphic with $F'(w) = f(w)$, so $F$ is a primitive of $f$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Building branches of $\log$.** On a simply connected $U \subseteq \mathbb{C}^\times$, $1/z$ is continuous and (by [[Thm - Cauchy's Theorem for a Star-Shaped Domain]]) has all closed integrals zero. So a primitive exists — namely, a branch of $\log$. This theorem is the deep mechanism behind the existence of branches.

**Building harmonic conjugates.** For a harmonic $u$ on a simply connected domain, $u_x - iu_y$ is holomorphic; building its primitive (a primitive $f = u + iv$) gives the harmonic conjugate $v$ via construction by line integration.

---

# Bridges

- **[[Def - Primitive (Antiderivative)]]** — the existence condition for the object.

- **[[Thm - Fundamental Theorem of Contour Integration]]** — the forward direction.

- **[[Thm - Cauchy's Theorem for a Star-Shaped Domain]]** — provides the closed-loop hypothesis automatically for holomorphic $f$ on star-shaped domains.

- **[[Thm - Existence of a Logarithm on Simply Connected Domains]]** — special case using $f = 1/z$.

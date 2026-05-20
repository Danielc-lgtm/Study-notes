---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Def - Domain in the Complex Plane"
  - "Thm - Cauchy–Riemann Equations"
tags: [analysis, complex-analysis]
---

# Notation

$D \subseteq \mathbb{C}$ — a [[Def - Domain in the Complex Plane|domain]] (non-empty path-connected open subset). $f : D \to \mathbb{C}$ holomorphic with $f'(z) = 0$ for all $z \in D$. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Statement

> **Theorem (constant on a domain if derivative is zero).** Let $D \subseteq \mathbb{C}$ be a [[Def - Domain in the Complex Plane|domain]] (non-empty connected open subset) and $f : D \to \mathbb{C}$ a holomorphic function with $f'(z) = 0$ for every $z \in D$. Then $f$ is constant on $D$.

---

# Motivation

In real analysis, a $C^1$ function on an interval whose derivative is identically zero is constant — proved by the mean value theorem. The natural complex analog: on a *connected* domain, holomorphic + zero derivative implies constant. The connectedness is essential — without it, the function can take different constant values on each connected component, in which case the conclusion holds *component-wise* but not globally.

This result is foundational: it is the "uniqueness" half of "two primitives differ by a constant", and it is the engine for several rigidity statements down the line. It is also the cleanest demonstration that path-connectedness of the [[Def - Domain in the Complex Plane|domain]] is what makes complex analysis work — without it, statements like "the value at one point determines the value everywhere" cannot even begin.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on a connected $D$, $f' \equiv 0$".

The first disguised source is **$f$ has a primitive $F$ on $D$ with $F$ constant on a subset**. If $F'(z) = f(z)$ everywhere and we know $F$ at one point, the theorem (applied to $F$) tells us $F$ is constant everywhere when $f \equiv 0$. *Example:* a function whose primitive vanishes on the boundary and has zero derivative is constant zero throughout — a uniqueness lemma for boundary value problems.

The second disguised source is **$f, g$ holomorphic on $D$ with $f' = g'$**. The difference $f - g$ has zero derivative, hence is constant. The standard way to conclude two holomorphic functions are *equal up to a constant*.

The third disguised source is **$|f|$ constant on $D$**. By a CR argument (or by taking $\log f$ locally), one shows $f$ must be constant if $|f|$ is — but the proof goes through "the derivative of an appropriate quantity is zero" and then this theorem. *Example:* a holomorphic function whose modulus is identically $1$ on a domain is a constant of modulus $1$.

**Targets (Output Amplification)**

The conclusion is "$f$ is constant on $D$".

Combine with **boundary value information.** Property $D$: $f$ is constant on some non-empty subset of $D$. The amplified result: by knowing one constant value (e.g., $f(z_0) = c$), we know $f \equiv c$ on the whole connected $D$. Used to identify the constant.

Combine with **a uniqueness statement.** Property $D$: a holomorphic function $g$ is known to have certain values on $D$. The amplified result: $f - g$ identically zero (or constant zero if a single value matches). This is the operational form: "two holomorphic functions on $D$ with the same derivative differ by a constant".

---

# Why Is It True

The intuition is that complex derivative zero means $f$ is *infinitesimally constant* at every point — moving in any direction by an infinitesimal amount changes $f$ by $0$. Path-connectedness means every two points are joined by a path; integrating zero along a path gives zero; so $f$ at one endpoint equals $f$ at the other.

More concretely: take any $C^1$ path $\gamma : [0, 1] \to D$ from $w$ to $z$. Compute $(f \circ \gamma)'(t) = f'(\gamma(t)) \gamma'(t) = 0$ for all $t$ — the composition has zero derivative. So $f \circ \gamma$ is constant on $[0, 1]$ (this is the real one-variable theorem on the interval), hence $f(z) = f(\gamma(1)) = f(\gamma(0)) = f(w)$.

The path-connectedness of $D$ — actually, we use *polygonal connectedness*, which follows from path-connectedness for open subsets of $\mathbb{C}$ — provides the chain of paths. The chain rule provides the derivative computation. The real one-variable theorem on the interval provides the constancy along each path. Combine them: $f$ is constant on $D$.

The connectedness is essential because the argument is *local*: zero derivative implies constancy on a small disc (by the chain-rule argument on radial paths), then extends to the whole component via connectivity. Without connectedness, the function can be one constant on each component.

---

# What Makes This Hard

The non-obvious step is recognizing that the *real* one-variable mean value theorem can be deployed on the *real-parameter curve* $f \circ \gamma : [0, 1] \to \mathbb{C}$, not on $f$ itself. The argument goes: $f$ has *complex* derivative zero; composing with a path gives a function of a real parameter; this function has real derivative zero (by chain rule); apply the real theorem on the interval. The error to avoid is trying to apply a "complex mean value theorem" — there is no such thing.

---

# Rederivation Scaffold

**High-level strategy:**
For any two points $w, z \in D$, find a $C^1$ path $\gamma$ joining them in $D$. Show $f \circ \gamma$ has zero real derivative on $[0, 1]$. Conclude $f(z) = f(w)$.

**Subgoal decomposition:**

1. **Reduce to a local disc.** Show that $f$ is constant on every disc $D(w, r) \subseteq D$.
   - *Hint:* Use radial paths from $w$ to $z$ inside the disc; chain rule.
   - *Why needed:* establishes local constancy.

2. **Promote local to global via connectedness.** The set of points where $f$ equals $f(w)$ is both open (by step 1) and closed (by continuity), hence is the whole connected $D$.
   - *Hint:* The set $\{z \in D : f(z) = f(w)\}$ is closed (preimage of $\{f(w)\}$ under continuous $f$) and open (by local constancy from step 1).
   - *Why needed:* delivers the global conclusion from local constancy.

---

# Lemma Decomposition

> [!note]- Lemma 1: Constancy on a disc
> **Statement:** If $f$ is holomorphic on a disc $D(w, r)$ with $f' \equiv 0$ on the disc, then $f$ is constant on $D(w, r)$.
>
> **Hint:** Take radial paths from $w$ to $z$; apply chain rule and the real one-variable theorem.
>
> **Why needed:** Establishes local constancy, the building block.
>
> > [!note]- Full proof
> > Fix $z \in D(w, r)$, $z \neq w$. Define $\gamma : [0, 1] \to D(w, r)$ by $\gamma(t) = w + t(z - w)$ — the line segment from $w$ to $z$, which lies in the convex disc. Then $\gamma$ is $C^1$ with $\gamma'(t) = z - w$. The composition $h(t) := f(\gamma(t))$ is a function $[0, 1] \to \mathbb{C}$. By the chain rule, $h'(t) = f'(\gamma(t)) \cdot \gamma'(t) = 0 \cdot (z - w) = 0$ for all $t \in [0, 1]$. So $h$ has zero (one-sided, complex) derivative; both real and imaginary parts have zero derivative as real functions of a real variable, hence are constant. Therefore $h(0) = h(1)$, i.e., $f(w) = f(z)$.

> [!note]- Lemma 2: Open + closed in a connected set is the whole set
> **Statement:** Let $D$ be a connected topological space, $S \subseteq D$ non-empty, open, and closed in $D$. Then $S = D$.
>
> **Hint:** Standard topology: $D = S \cup (D \setminus S)$ would be a disconnection if $S \neq D$.
>
> **Why needed:** Promotes local constancy to global constancy.
>
> > [!note]- Full proof
> > If $S \neq D$, then $D \setminus S$ is non-empty (assumed). $S$ is open and closed, so $D \setminus S$ is also open. Then $D = S \sqcup (D \setminus S)$ is a disjoint union of two non-empty open sets — contradicting connectedness. Hence $S = D$.

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $w \in D$ and let $S = \{z \in D : f(z) = f(w)\}$. We show $S = D$, using that $D$ is connected.
>
> $S$ is non-empty (contains $w$).
>
> $S$ is closed in $D$: $S = f^{-1}(\{f(w)\})$ is the preimage of a closed set under the continuous function $f$.
>
> $S$ is open in $D$: take $z_0 \in S$, so $f(z_0) = f(w)$. Since $D$ is open, there is $r > 0$ with $D(z_0, r) \subseteq D$. By Lemma 1 applied to the disc $D(z_0, r)$ (where $f' \equiv 0$), $f$ is constant on $D(z_0, r)$ with value $f(z_0) = f(w)$. So $D(z_0, r) \subseteq S$, and $S$ is open at $z_0$.
>
> By Lemma 2, $S = D$, i.e., $f \equiv f(w)$ on $D$. $\blacksquare$
>
> **Alternative proof using paths.** For any $z \in D$, by path-connectedness, choose a piecewise $C^1$ curve $\gamma : [0, 1] \to D$ from $w$ to $z$. The composition $f \circ \gamma$ has $(f \circ \gamma)'(t) = f'(\gamma(t)) \gamma'(t) = 0$ wherever $\gamma$ is differentiable, hence $f \circ \gamma$ is piecewise constant on $[0, 1]$. Since $f \circ \gamma$ is continuous on $[0, 1]$ (continuous composition of continuous), and piecewise constant + continuous = constant, $f(\gamma(1)) = f(\gamma(0))$, i.e., $f(z) = f(w)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Uniqueness of primitives.** Two primitives of the same continuous function $f$ on a domain differ by a constant. Application of the theorem to $F_1 - F_2$.

**Constancy of holomorphic functions with constant modulus.** If $|f|$ is constant on a domain, then $f$ is constant. The argument: locally write $f = |f| e^{i\theta}$ and show $\theta$ is constant using CR — or note that $f \bar f = c^2$ forces $\bar f = c^2/f$ holomorphic, so by CR for both $f$ and $\bar f$, $f$ must be constant.

**Two-dimensional fluid dynamics.** A 2D incompressible inviscid potential flow has velocity field $\vec v = (u, v)$ satisfying CR equations (with appropriate sign conventions). If the flow is *irrotational* and has zero velocity at every point of a connected region, then the velocity is identically zero throughout — the theorem applied to the complex velocity $u - iv$.

---

# Bridges

- **[[Thm - Cauchy–Riemann Equations]]** — the four CR partial derivatives must all be zero (from $f' = 0$ combined with the derivative formula). The real-multivariable theorem "zero gradient on path-connected open set implies constant" applies to $u, v$ separately.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — gives a more refined statement: if all derivatives of $f$ vanish at *one point* $w$, then $f$ is constant (in fact zero if $f(w) = 0$) — using the Taylor expansion plus a connectedness argument.

- **[[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]]** — the much stronger rigidity: agreement on a set with an accumulation point forces agreement on the whole domain. This theorem is a far-weaker shadow (agreement of derivatives at every point).

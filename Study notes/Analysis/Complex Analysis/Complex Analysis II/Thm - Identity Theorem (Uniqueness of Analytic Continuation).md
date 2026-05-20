---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Principle of Isolated Zeros"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

$D \subseteq \mathbb{C}$ a (connected) [[Def - Domain in the Complex Plane|domain]]; $f, g : D \to \mathbb{C}$ holomorphic. $S \subseteq D$ a set on which $f = g$. An **accumulation point** of $S$ in $D$: a point $w \in D$ such that every neighbourhood of $w$ contains points of $S$ different from $w$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

The identity theorem is the strongest rigidity statement in complex analysis: **two holomorphic functions on a connected domain that agree on a set with an accumulation point are equal everywhere**. Compare with real analysis, where $C^\infty$ functions can agree on a half-line and disagree on the other half ("bump functions"). The complex setting has no such flexibility.

Operationally, this converts "partial agreement" (on countably many points, on an arc, on the real axis, on a sub-disc) into "full agreement". This is the engine for:
- Lifting real identities to complex (e.g., $\exp(z + w) = \exp(z)\exp(w)$ from real to complex);
- Uniqueness of analytic continuation;
- Identification of functions from limited data;
- Algebraic identities verified on small sets.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f = g$ on a set $S \subseteq D$ with an accumulation point in $D$".

The first disguised source is **$f = g$ on an open subset of $D$**: every point of the open subset is an accumulation point (of the subset itself). So agreement on any open set forces global agreement.

The second disguised source is **$f = g$ on a curve in $D$**: a curve (other than a single point) has accumulation points everywhere along it. So agreement along a curve forces global agreement.

The third disguised source is **$f = g$ on a sequence $z_n \to z_\infty$ with $z_\infty \in D$**: the limit point $z_\infty$ is an accumulation point of the sequence. So agreement on a sequence with limit in $D$ forces global agreement. Useful: agreement on $\{1/n\}$ near $0 \in D$, on $\mathbb{R} \cap D$ (real axis), etc.

The fourth disguised source is **$f$ vanishes on a set with an accumulation point**: applied with $g \equiv 0$, $f \equiv 0$ on $D$.

**Targets (Output Amplification)**

The conclusion is "$f = g$ on all of $D$".

Combine with **boundary value uniqueness.** Property $D$: $f, g$ continuous on $\overline D$, agreeing on a boundary arc. Often used to show two analytic continuations of a function are the same.

Combine with **functional equations.** Property $D$: $f(z + 1) = z f(z)$ (functional equation of $\Gamma$) verified on a real interval. The amplified result: the equation holds on the full domain of holomorphicity, by identity theorem applied to both sides.

---

# Why Is It True

Set $h = f - g$, holomorphic on $D$. $h$ vanishes on $S$, which has an accumulation point $w \in D$.

If $h$ is identically zero in a neighbourhood of $w$, we say "$h$ vanishes locally at $w$". This is the strong condition. The principle of isolated zeros says: if $h$ does *not* vanish locally at $w$ but $h(w) = 0$, then $w$ is an isolated zero — there is a punctured disc around $w$ with no other zeros of $h$. But this contradicts $w$ being an accumulation point of $S \subseteq h^{-1}(0)$: any neighbourhood of $w$ has points of $S$ (i.e., zeros of $h$) other than $w$. So $h$ vanishes locally at $w$.

Now propagate: the set $D_0 = \{z \in D : h \equiv 0 \text{ on a neighbourhood of } z\}$ is open by definition. Its complement $D_1 = D \setminus D_0 = \{z \in D : \text{some derivative of } h \text{ is nonzero at } z\}$ is also open (each derivative is continuous, so "non-vanishing at a point" is open). By connectedness of $D$, $D = D_0$ or $D = D_1$. We have $w \in D_0$, so $D_0 \neq \emptyset$, hence $D_0 = D$. So $h \equiv 0$ on $D$, i.e., $f = g$. $\blacksquare$

The deep observation: the *isolation of zeros* (a strong local rigidity) combined with the *connectedness of $D$* (a global topological property) forces a strong global rigidity. The principle is: "rigidity propagates along paths".

---

# What Makes This Hard

The non-obvious step is the *partition* of $D$ into $D_0$ (where $h$ vanishes locally) and $D_1$ (where some derivative is nonzero). Both are open; the connectedness of $D$ then forces one to be empty. The clever observation is identifying $D_1$ as "*some* derivative is nonzero" — using the power series representation, this is equivalent to "$h$ does not vanish locally", and it is *open* because each derivative is continuous.

---

# Rederivation Scaffold

**High-level strategy:**
$h = f - g$ vanishes on $S$ with accumulation $w$. Use isolated zeros: $h$ must vanish locally at $w$. Set $D_0 = \{h \text{ vanishes locally}\}$ open, $D_1 = D \setminus D_0$ open. $D_0 \neq \emptyset$; connectedness gives $D_0 = D$.

**Subgoal decomposition:**

1. **Set $h = f - g$.**

2. **$h$ vanishes locally at $w$.** Use isolated zeros (contrapositive): if $h$ does not vanish locally, $w$ is isolated zero; contradicts accumulation.

3. **Partition $D = D_0 \sqcup D_1$.** $D_0 = \{z : h \equiv 0 \text{ on a neighbourhood}\}$, $D_1 = D \setminus D_0$.

4. **Both open.** $D_0$ open by definition; $D_1 = \{z : \exists n, h^{(n)}(z) \neq 0\}$ open by continuity of derivatives.

5. **Connectedness.** $D_0 \neq \emptyset$ (contains $w$); $D = D_0$.

6. **$f = g$ on $D$.**

---

# Lemma Decomposition

> [!note]- Lemma 1: Vanishing at an accumulation point forces local vanishing
> **Statement:** If $h$ is holomorphic on $D(w, R)$ and $h$ vanishes on a set with accumulation point $w$, then $h \equiv 0$ on $D(w, R)$.
>
> **Hint:** By isolated zeros, a non-locally-vanishing holomorphic function has isolated zeros; the accumulation contradicts isolation.
>
> > [!note]- Full proof
> > If $h \not\equiv 0$ on $D(w, R)$, the power series of $h$ at $w$ has at least one nonzero coefficient. By [[Thm - Principle of Isolated Zeros]] (applied to $h$ at $w$, noting $h(w) = 0$ by continuity, since $w$ is a limit of zeros), $w$ is an isolated zero — there is $r$ with $h \neq 0$ on $\{0 < |z - w| < r\}$. But by hypothesis, every neighbourhood of $w$ contains a zero $z \neq w$ — contradiction. So $h \equiv 0$ on $D(w, R)$. $\blacksquare$

> [!note]- Lemma 2: Open-and-closed argument
> **Statement:** Let $D$ be a connected domain, $h$ holomorphic on $D$. The set $D_0 = \{z \in D : h \equiv 0 \text{ on a neighbourhood of } z\}$ is both open and closed in $D$.
>
> > [!note]- Full proof
> > $D_0$ open: by definition. $D_0$ closed: equivalently $D_1 = D \setminus D_0$ open. $D_1 = \{z \in D : h \not\equiv 0 \text{ on any neighbourhood}\}$. By the contrapositive of Lemma 1 (or equivalently by the power series characterization: $z \in D_1$ iff some derivative $h^{(n)}(z)$ is nonzero), and continuity of $h^{(n)}$, $D_1$ is open. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Set $h = f - g$, holomorphic on $D$. $h$ vanishes on $S$, which has an accumulation point $w \in D$.
>
> By Lemma 1 applied on a disc $D(w, R) \subseteq D$: $h \equiv 0$ on this disc.
>
> So $w \in D_0 := \{z \in D : h \equiv 0 \text{ on some neighbourhood of } z\}$, hence $D_0 \neq \emptyset$. By Lemma 2, $D_0$ is both open and closed in $D$. By connectedness, $D_0 = D$. So $h \equiv 0$ on $D$, i.e., $f \equiv g$ on $D$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Identifying functions from real values.** A holomorphic function $f$ on a connected domain $D$ containing $\mathbb{R}$ (or a real interval) is determined by its values on $\mathbb{R}$. Used to extend identities from real to complex: if $\cos(z + w) - \cos z \cos w + \sin z \sin w = 0$ for real $z, w$, both sides are holomorphic in $z$ (for fixed real $w$), agree on $\mathbb{R}$, so agree everywhere. Then vary $w$ to get the full complex identity. See [[Ex - Uniqueness of sin from real values]].

**Uniqueness of analytic continuation.** If two analytic continuations of a function to a larger domain agree on the original domain, they agree on their common larger domain (by identity theorem). This is the *unique* analytic continuation principle.

**Power-series identification.** If two power series at $a$ agree on any open subset of their common disc of convergence, they have the same coefficients. The identity theorem promotes this to: agreement on a set with an accumulation point in the disc forces same coefficients.

---

# Bridges

- **[[Thm - Principle of Isolated Zeros]]** — the local rigidity used in the proof.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — the underlying structural theorem.

- **[[Thm - Identity Theorem for Power Series]]** — the power-series version; the full identity theorem extends to a stronger hypothesis (accumulation point, not open set).

- **[[Thm - Constant on a Domain if Derivative is Zero]]** — the weaker version (derivative zero is a strong condition; vanishing on a set with accumulation is weaker).

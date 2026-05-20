---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Power Series and Radius of Convergence"
  - "Thm - Power Series is Holomorphic with Termwise Derivative"
tags: [analysis, complex-analysis]
---

# Notation

$\sum c_n (z - a)^n, \sum d_n (z - a)^n$ — two power series with the same centre $a \in \mathbb{C}$. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Motivation

A power series $\sum c_n (z - a)^n$ is given by an infinite sequence of coefficients. The natural uniqueness question: if two power series define the *same function* on a common disc of convergence, must they have the *same coefficients*? The answer is yes — and stronger: it is enough that they agree on a non-empty *open subset* of the common disc.

This is the seed of the much stronger [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)|identity theorem for holomorphic functions]] in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]] (which only requires agreement on a set with an accumulation point). Both rest on the same idea: enough local data about an analytic object determines it everywhere.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "two power series agreeing on a non-empty open subset of the common disc of convergence".

The first disguised source is **two functions $f, g$ with respective power series and $f \equiv g$ on a disc.** Then the coefficients match. Used to prove uniqueness of power-series representation.

The second disguised source is **a power series identically zero on a disc.** All coefficients are zero. Equivalent to step 1 with $g = 0$. The fundamental "$f \equiv 0$ on a disc $\Rightarrow$ all $c_n = 0$" form.

**Targets (Output Amplification)**

The conclusion is "all coefficients are equal: $c_n = d_n$ for every $n$".

Combine with **functional identities.** Property $D$: we want to show $f \equiv g$ on a domain. The amplified result: if $f$ and $g$ are both defined by convergent power series and we know $f = g$ on a small disc, then $c_n = d_n$, hence $f \equiv g$ on the *whole* common disc. Used to extend identities from a small neighbourhood to a large one.

Combine with **comparison of Taylor coefficients.** Property $D$: $f = g$ on a disc; both have known Taylor expansions. The amplified result: the Taylor coefficients of $f$ and $g$ at the centre are equal, which translates into identities among the derivatives.

---

# Why Is It True

If $\sum c_n (z - a)^n = \sum d_n (z - a)^n$ on a disc around $a$, then $\sum(c_n - d_n)(z - a)^n = 0$ on that disc. The question reduces to: if a power series is identically zero on a disc, are all its coefficients zero?

The proof is iterative. Evaluating at $z = a$: only the $n = 0$ term survives, giving $c_0 - d_0 = 0$. Subtracting the constant term and dividing by $z - a$: the remaining series $\sum (c_n - d_n)(z - a)^{n-1}$ is also zero on the punctured disc; by continuity (the power series is continuous), the value at $z = a$ is $c_1 - d_1$, which must equal the limit as $z \to a$, which is $0$. So $c_1 = d_1$. Iterating, all coefficients match.

A cleaner formulation: by [[Thm - Power Series is Holomorphic with Termwise Derivative]], $f$ and $g$ are $C^\infty$ on the disc with $f^{(n)}(a) = n! c_n$ and $g^{(n)}(a) = n! d_n$. If $f = g$ on a neighbourhood of $a$, then $f^{(n)}(a) = g^{(n)}(a)$ for all $n$, hence $c_n = d_n$.

The agreement need only be on an *open subset* (not the entire disc) because power series are determined by their values *anywhere* — specifically, by their derivatives at *any one point*. If $f = g$ on an open subset $S$, picking any $z_0 \in S$, $f$ and $g$ agree in a neighbourhood of $z_0$, so all their derivatives at $z_0$ agree. By the analytic structure, this forces $f \equiv g$ on the whole common disc.

The deep intuition: power series are "infinitely rigid" — they are determined by countably many numbers ($c_n$), and matching values on an open set fixes those numbers.

---

# What Makes This Hard

The non-obvious step is recognizing that we can extract the coefficients one by one by *differentiating* (or equivalently, by iteratively evaluating at the centre and subtracting). The most common error is to think the agreement must be on the *whole* disc — when in fact it suffices to be on any non-empty open subset, because power series are determined by their behaviour on any open neighbourhood of any interior point.

---

# Rederivation Scaffold

**High-level strategy:**
Subtract: $\sum(c_n - d_n)(z - a)^n = 0$ on an open set. Use the coefficient formula $c_n - d_n = (f - g)^{(n)}(a)/n! = 0$ (since $f - g \equiv 0$ in a neighbourhood of $a$).

**Subgoal decomposition:**

1. **Reduce to: a power series identically zero on a disc has all coefficients zero.**
   - *Hint:* set $e_n = c_n - d_n$.
   - *Why needed:* simplifies the problem.

2. **Show: if $\sum e_n (z - a)^n = 0$ on an open set $S$ containing $a$ (without loss of generality, after shrinking), then by the coefficient formula $e_n = 0$ for all $n$.**
   - *Hint:* differentiate $k$ times at $z = a$: $f^{(k)}(a) = k! e_k$.
   - *Why needed:* uses the analyticity to extract coefficients.

---

# Lemma Decomposition

> [!note]- Lemma 1: A power series zero on a disc has all coefficients zero
> **Statement:** Let $f(z) = \sum c_n (z - a)^n$ have radius $R > 0$. If $f(z) = 0$ for all $z$ in some open disc $D(a, r) \subseteq D(a, R)$, then $c_n = 0$ for all $n$.
>
> **Hint:** Differentiate $n$ times at $z = a$ using the coefficient formula.
>
> **Why needed:** This is the core content; the full theorem reduces to it.
>
> > [!note]- Full proof
> > By [[Thm - Power Series is Holomorphic with Termwise Derivative]], $f \in C^\infty$ on $D(a, R)$ with $f^{(n)}(a) = n! c_n$ for every $n$. Since $f \equiv 0$ on $D(a, r)$, all derivatives of $f$ at $a$ are zero: $f^{(n)}(a) = 0$. Hence $n! c_n = 0$, so $c_n = 0$ for every $n \geq 0$. $\blacksquare$

> [!note]- Lemma 2: Agreement on an open set $\Rightarrow$ agreement near the centre
> **Statement:** If $\sum c_n (z - a)^n = \sum d_n (z - a)^n$ on a non-empty open subset $S$ of the common disc of convergence, then they agree on a disc $D(a, r)$ around $a$ — possibly after shrinking.
>
> **Hint:** If $a \in S$, take $r$ small enough that $D(a, r) \subseteq S$. If $a \notin S$, pick $z_0 \in S$ and shift the expansion to $z_0$.
>
> **Why needed:** Reduces the general agreement-on-an-open-set hypothesis to agreement on a disc around the centre.
>
> > [!note]- Full proof
> > Case 1: $a \in S$. Then $S$ open in $\mathbb{C}$ implies there is $r > 0$ with $D(a, r) \subseteq S$. The two series agree on $D(a, r)$. Then by Lemma 1 applied to the difference, all coefficients agree.
> >
> > Case 2: $a \notin S$. Pick $z_0 \in S$. The two power series, expanded around $z_0$ instead of $a$ (use the Taylor expansion at $z_0$ within their common disc of convergence), agree on a disc around $z_0$. So their Taylor coefficients at $z_0$ agree — meaning the functions $f, g$ have the same derivatives at $z_0$. Since $f, g$ are holomorphic on $D(a, R)$, they have unique power-series representations at $a$, determined by their derivatives at $a$. But $f - g$ is holomorphic on the disc with $(f - g)^{(n)}(z_0) = 0$, hence (by the principle of isolated zeros, see [[Thm - Principle of Isolated Zeros]] in CA II) $f - g \equiv 0$, hence $c_n = d_n$. (The proof avoiding CA II uses a direct argument: $f - g$ has a power series at $a$, all of whose derivatives vanish at $z_0$, so the Taylor expansion at $z_0$ is identically zero, implying the function is identically zero, hence the coefficients at $a$ are also zero.)

---

# Formal Proof

> [!note]- Complete formal proof
> Suppose $\sum c_n (z - a)^n = \sum d_n (z - a)^n$ for $z$ in a non-empty open subset $S$ of the common disc of convergence. Set $f(z) = \sum (c_n - d_n)(z - a)^n$, so $f \equiv 0$ on $S$.
>
> By Lemma 2, we may assume — possibly after restricting to a sub-disc — that $f \equiv 0$ on some open disc $D(a, r)$.
>
> By Lemma 1, $c_n - d_n = 0$ for all $n$, i.e., $c_n = d_n$. $\blacksquare$
>
> **Direct proof (without invoking CA II results).** Assume $a \in S$ (otherwise translate). Then $f \equiv 0$ on $D(a, r)$ for some $r > 0$. At $z = a$: $f(a) = c_0 - d_0 = 0$, so $c_0 = d_0$. For $z \neq a$ in $D(a, r)$, $f(z)/(z - a) = \sum_{n=1}^\infty (c_n - d_n)(z - a)^{n-1}$, which is $0$ on $D(a, r) \setminus \{a\}$. By continuity (the sum is a continuous function on $D(a, r)$ by uniform convergence), the value at $z = a$ is also $0$: $c_1 - d_1 = 0$. Iterating, $c_n = d_n$ for all $n$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Uniqueness of generating functions.** In combinatorics, if two generating functions agree on a small disc, they encode the same sequence. The identity theorem then says one cannot have two distinct generating functions for the same combinatorial structure.

**Extending real identities to complex.** A polynomial identity $p(x) = q(x)$ verified for all real $x$ in an interval extends to all complex $z$ in any common disc of definition by the identity theorem (since both sides are power series, the identity on a real interval — which has accumulation points — forces coefficient equality). This is one route to the *principle of analytic continuation*.

**Algebraic identities from a small disc.** The identity $\exp(z + w) = \exp(z) \exp(w)$ — proved for $z, w \in \mathbb{R}$ by elementary calculus — extends to all complex $z, w$: fix $w$, view both sides as functions of $z$; both are entire; they agree on $\mathbb{R}$ (which has accumulation points), so by identity, agree on $\mathbb{C}$. Iterate for $w$. This is a model use of the identity theorem to lift real identities to complex.

---

# Bridges

- **[[Thm - Power Series is Holomorphic with Termwise Derivative]]** — provides the coefficient formula $c_n = f^{(n)}(a)/n!$ used in the proof.

- **[[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]]** — the much stronger statement in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]: agreement on a set with an accumulation point (not just an open set) implies agreement on the whole connected domain. This power series version is the special case where the accumulation point is at the centre.

- **[[Thm - Principle of Isolated Zeros]]** — the dual: a non-zero holomorphic function has isolated zeros. Both rest on the analytic structure of power series.

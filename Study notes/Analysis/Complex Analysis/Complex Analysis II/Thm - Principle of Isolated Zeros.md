---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)"
tags: [analysis, complex-analysis]
---

# Notation

$f : D(w, R) \to \mathbb{C}$ holomorphic; $w \in \mathbb{C}$ a candidate zero; $f$ not identically zero on any disc around $w$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

A non-trivial holomorphic function has *isolated* zeros: each zero $w$ is contained in some small punctured disc on which $f$ has no other zeros. This is in stark contrast to real $C^\infty$ functions, which can have non-isolated zeros (e.g., $\sin(1/x) \cdot x$ at $0$ has the zeros $\{1/(n\pi) : n \in \mathbb{Z} \setminus \{0\}\}$ accumulating at $0$).

The factorization $f(z) = (z - w)^k g(z)$ with $g(w) \neq 0$ — where $k$ is the *order of the zero* — is the local structural form. It captures the precise rate at which $f$ vanishes near $w$.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on $D(w, R)$, $f(w) = 0$, $f$ not identically zero on any sub-disc".

The first disguised source is **$f$ holomorphic with $f(w) = 0$ and we want to know "how fast it vanishes"**: the order $k$ classifies the vanishing rate.

**Targets (Output Amplification)**

The conclusion is "$f(z) = (z - w)^k g(z)$ with $g$ holomorphic, $g(w) \neq 0$, and zeros isolated".

Combine with **the identity theorem.** Property $D$: $f$ has a zero accumulating in $D$. The amplified result: $f \equiv 0$ on a neighbourhood, hence on the whole connected $D$. See [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]].

Combine with **the residue theorem (in CA III).** Property $D$: $1/f$ has a pole of order $k$ at $w$. The amplified result: residues at the pole are computed using the factorization.

---

# Why Is It True

Expand $f$ as a power series at $w$: by [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]], $f(z) = \sum_{n \geq 0} c_n (z - w)^n$ on $D(w, R)$. Since $f$ is not identically zero, not all $c_n$ are zero. Let $k$ be the smallest index with $c_k \neq 0$.

Then $f(z) = c_k (z - w)^k + c_{k+1}(z - w)^{k+1} + \ldots = (z - w)^k [c_k + c_{k+1}(z - w) + \ldots] = (z - w)^k g(z)$, where $g(z) = c_k + c_{k+1}(z - w) + \ldots$ is a power series with $g(w) = c_k \neq 0$. Note: $g$ is the power series obtained by "dividing out $(z - w)^k$", and it converges on the same disc as $f$ (the coefficients are the original $c_n$ shifted, with the same growth rate).

By continuity of $g$ at $w$: since $g(w) \neq 0$, there is $r > 0$ with $g(z) \neq 0$ for $|z - w| < r$. Then $f(z) = (z - w)^k g(z) \neq 0$ for $0 < |z - w| < r$ (the $(z - w)^k$ factor is nonzero for $z \neq w$, and $g(z) \neq 0$). So $w$ is an isolated zero. $\blacksquare$

---

# What Makes This Hard

Nothing genuinely hard. The clean argument requires only the local power series expansion ([[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]) and basic algebra to factor out $(z - w)^k$. The conceptual content is the *order* $k$ — the precise vanishing rate — which equals the smallest index of a nonzero coefficient.

---

# Rederivation Scaffold

**High-level strategy:**
Expand $f$ in power series at $w$. Identify the smallest index $k$ with nonzero coefficient. Factor $f(z) = (z - w)^k g(z)$. $g(w) \neq 0$; continuity gives $g \neq 0$ near $w$.

**Subgoal decomposition:**

1. **Power series expansion at $w$.** $f(z) = \sum c_n (z - w)^n$.

2. **Identify $k$.** Smallest $n$ with $c_n \neq 0$ (exists since $f$ not identically zero).

3. **Factor.** $f(z) = (z - w)^k g(z)$ with $g(z) = c_k + c_{k+1}(z - w) + \ldots$.

4. **$g(w) = c_k \neq 0$.** From the definition.

5. **Isolated zero.** $g \neq 0$ near $w$ by continuity, so $f \neq 0$ for $0 < |z - w| < r$.

---

# Lemma Decomposition

(No further lemmas needed.)

---

# Formal Proof

> [!note]- Complete formal proof
> By [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]], $f(z) = \sum_{n=0}^\infty c_n (z - w)^n$ on $D(w, R)$.
>
> Since $f$ is not identically zero on any disc around $w$, not all $c_n$ are zero (otherwise $f \equiv 0$). Let $k = \min\{n : c_n \neq 0\}$. So $c_0 = \ldots = c_{k-1} = 0$ and $c_k \neq 0$.
>
> Factor: $f(z) = \sum_{n=k}^\infty c_n (z - w)^n = (z - w)^k \sum_{n=k}^\infty c_n (z - w)^{n-k} = (z - w)^k \sum_{m=0}^\infty c_{m+k}(z - w)^m =: (z - w)^k g(z)$.
>
> $g$ is a power series with $|c_{m+k}|^{1/m} = |c_{m+k}|^{(m+k)/m \cdot 1/(m+k)} \to (1/R)^{1} = 1/R$ as $m \to \infty$ (same growth rate as $f$), so radius of convergence at least $R$. Hence $g$ is holomorphic on $D(w, R)$ with $g(w) = c_k \neq 0$.
>
> By continuity of $g$ at $w$, there is $r > 0$ with $|g(z) - g(w)| < |g(w)|/2$ for $|z - w| < r$, hence $|g(z)| > |g(w)|/2 > 0$ for $|z - w| < r$. So $g(z) \neq 0$ on $D(w, r)$.
>
> For $0 < |z - w| < r$: $f(z) = (z - w)^k g(z)$ with $(z - w)^k \neq 0$ and $g(z) \neq 0$, so $f(z) \neq 0$. Hence $w$ is an isolated zero. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Factorization of polynomials.** A polynomial $p$ has a zero of order $k$ at $w$ iff $p(z) = (z - w)^k q(z)$ with $q$ polynomial and $q(w) \neq 0$. The complex factorization theorem is the holomorphic version, working for any holomorphic function on a disc.

**Multiplicity and residues.** At a zero of order $k$, $1/f$ has a pole of order $k$. The residue of $1/f$ at $w$ is computable from the factorization, providing the entry point to the [[Complex Analysis III — Winding, Laurent, Residues|residue theorem]].

---

# Bridges

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — the source.

- **[[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]]** — the global propagation: zeros accumulate forces $f \equiv 0$.

- **[[Thm - Identity Theorem for Power Series]]** — the parallel statement for series: agreement on an open set forces all coefficients to agree, equivalent in spirit to isolation of zeros.

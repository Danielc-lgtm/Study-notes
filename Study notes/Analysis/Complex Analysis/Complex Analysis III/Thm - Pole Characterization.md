---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Removable Singularity, Pole, Essential Singularity"
  - "Thm - Riemann's Removable Singularity Theorem"
  - "Def - Isolated Singularity"
tags: [analysis, complex-analysis]
---

# Notation

$a \in \mathbb{C}$ is an isolated singularity of $f$, holomorphic on $D(a, R) \setminus \{a\}$. The order of a pole is a positive integer $k$. Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Motivation

We have three types of isolated singularities — removable, pole, essential. Riemann's theorem characterized the removable case by boundedness. The corresponding characterization of poles is: $a$ is a pole of $f$ if and only if $|f(z)| \to \infty$ as $z \to a$.

This is the *qualitative* characterization of poleness, and it is the one one reaches for in practice. To check that $a$ is a pole, you usually do not expand the Laurent series — you just observe that $|f|$ blows up. Conversely, "this function blows up at $a$" immediately tells you the singularity is a pole (not essential, not removable).

The theorem also packages the equivalent characterizations of poles: factorization as $(z - a)^{-k} g(z)$ with $g$ holomorphic and $g(a) \neq 0$; equivalence with $1/f$ having a removable singularity (and a zero of order $k$). These different formulations are used interchangeably in computations: $f = (z - a)^{-k} g$ is what you write when computing a residue at a high-order pole; $1/f$ having a zero is what connects pole counting to zero counting via the argument principle.

---

# Sources and Targets

**Sources (Input Broadening)**

The sources are situations triggering "the singularity is a pole".

**$f$ blows up at $a$.** Property $B$: $|f(z)| \to \infty$ as $z \to a$. The cleanest trigger. Bridge: this is the theorem's main equivalence, so a pole is exactly when $|f|$ blows up.

**$1/f$ extends holomorphically with $1/f(a) = 0$.** Property $B$: take the reciprocal; if $1/f$ is bounded (and approaches $0$) near $a$, then by Riemann's theorem $1/f$ extends to a holomorphic function with value $0$ at $a$. Bridge: poles of $f$ are zeros of $1/f$, with the same multiplicity. This is one of the most useful reformulations.

**$f$ is a quotient of holomorphic functions $P/Q$ with $Q(a) = 0$ but $P(a) \neq 0$.** Property $B$: $f = P/Q$ where $P, Q$ are holomorphic in a neighborhood of $a$, $Q(a) = 0$, $P(a) \neq 0$, and $a$ is an isolated zero of $Q$. Bridge: writing $Q(z) = (z - a)^k h(z)$ with $h(a) \neq 0$, $f = P/Q = P/((z-a)^k h) = (z-a)^{-k}(P/h)$, with $P/h$ holomorphic and nonzero at $a$. So $f$ has a pole of order $k$ at $a$, equal to the order of the zero of $Q$ minus the order of the zero of $P$ (zero if $P(a) \neq 0$).

**$(z - a)^k f(z)$ extends to a holomorphic function with nonzero value at $a$.** Property $B$: for some integer $k \geq 1$, $(z - a)^k f(z) \to L \neq 0$ as $z \to a$. Bridge: this is the factorization characterization. Trigger when you can manipulate $f$ by multiplication.

**Targets (Output Amplification)**

The conclusion is "$a$ is a pole of order $k$".

Combine with **residue computation.** Property $D$: once you know $f$ has a pole of order $k$, you can compute the residue via $\operatorname{Res}_a f = \frac{1}{(k-1)!}\lim_{z \to a}\frac{d^{k-1}}{dz^{k-1}}[(z-a)^k f(z)]$.

Combine with **the argument principle.** Property $D$: the order of the pole appears with a minus sign in the argument principle's count of "zeros minus poles". So pole orders are needed for global counting.

Combine with **Riemann's theorem at infinity.** Property $D$: $f$ holomorphic with $|f| \to \infty$ at $\infty$ behaves like a pole at $\infty$. Bridge: viewing $\hat{\mathbb{C}}$ as the one-point compactification, the pole/zero/regular trichotomy extends to $\infty$, with $f$ at $\infty$ classified by the Laurent expansion of $f(1/w)$ at $w = 0$.

---

# Why Is It True

The intuition is that the Laurent expansion at a pole has its "biggest" term being a negative power: $f(z) \sim c_{-k}(z - a)^{-k}$ as $z \to a$, with $k \geq 1$ and $c_{-k} \neq 0$. This dominant term blows up like $(z - a)^{-k}$, so $|f(z)| \to \infty$. Conversely, if $|f| \to \infty$, then $1/f$ has limit $0$ at $a$; in particular $1/f$ is bounded near $a$, so by Riemann's removable singularity theorem $1/f$ extends holomorphically with $1/f(a) = 0$. The Taylor expansion of $1/f$ around $a$ has a leading term $(z - a)^k$ for some integer $k \geq 1$, and inverting gives $f(z) \sim 1/(z - a)^k \cdot (\text{something nonzero})$ — a pole of order $k$.

The brilliance is the *reciprocal trick*. Riemann's theorem (boundedness ⇒ removable) is hard to apply directly to a function that blows up, but $1/f$ does *not* blow up (it goes to zero), so Riemann applies cleanly to $1/f$. The pole structure of $f$ is then read off the zero structure of $1/f$, with multiplicities preserved.

The essential case is excluded because of the qualitative behaviour: at an essential singularity, $|f|$ neither tends to a finite limit nor to infinity. So pole = "$|f| \to \infty$" cleanly excludes both removable (finite limit) and essential (oscillatory) cases.

---

# What Makes This Hard

The non-obvious step is the **reciprocal trick**: study $1/f$ instead of $f$, because $1/f$ is bounded (in fact tends to $0$) when $f$ blows up, so Riemann's theorem applies. A common mistake is to try to apply Riemann directly to $f$, which fails because $f$ is unbounded near $a$. A second slip is to confuse "order of the pole" with "order of the zero of $1/f$"; they agree by definition, but one must verify this consistency. A third pitfall is forgetting that for a pole of order $k$, the *coefficient* $c_{-k}$ in the Laurent expansion is nonzero — without this nonvanishing, the function could have lower-order behaviour.

---

# Rederivation Scaffold

**High-level strategy:**
Use the reciprocal trick. If $|f| \to \infty$ at $a$, then $1/f$ is bounded and tends to $0$ at $a$; by Riemann's removable singularity theorem $1/f$ extends holomorphically with value $0$ at $a$. The order of the zero of $1/f$ at $a$ — say $k$ — is the order of the pole of $f$. Conversely, if $a$ is a pole of order $k$, the Laurent expansion of $f$ starts with $c_{-k}(z - a)^{-k}$, so $|f| \to \infty$.

**Subgoal decomposition:**

1. **Forward direction: pole ⇒ $|f| \to \infty$.** Given $a$ a pole of order $k$, Laurent expansion is $f = c_{-k}(z - a)^{-k} + \ldots$, with $c_{-k} \neq 0$. As $z \to a$, the leading term dominates, $|f(z)| \to \infty$.

2. **Reverse direction: $|f| \to \infty$ ⇒ pole.** Given $|f(z)| \to \infty$ as $z \to a$, observe $|1/f(z)| \to 0$. In a small punctured neighborhood, $f$ is nowhere zero (since $|f|$ is large), so $1/f$ is holomorphic on a punctured disc.

3. **Apply Riemann to $1/f$.** Since $1/f \to 0$ at $a$ (in particular bounded), $1/f$ extends holomorphically with $1/f(a) = 0$.

4. **Read off the pole order.** The extension has a zero at $a$; its Taylor expansion is $\sum_{n \geq k} d_n (z - a)^n$ with $d_k \neq 0$ for some $k \geq 1$. So $1/f(z) = (z - a)^k h(z)$ with $h$ holomorphic and $h(a) \neq 0$.

5. **Invert.** $f(z) = 1/((z - a)^k h(z)) = (z - a)^{-k} (1/h(z))$, with $1/h$ holomorphic and nonzero near $a$. So $f$ has a pole of order $k$ at $a$, with $c_{-k} = 1/h(a)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: If $|f| \to \infty$ at $a$, then $1/f$ is holomorphic on a punctured disc and extends to $0$ at $a$
> **Statement:** Let $f$ be holomorphic on $D(a, R) \setminus \{a\}$ with $|f(z)| \to \infty$ as $z \to a$. Then there exists $r > 0$ such that $f$ is nowhere zero on $D(a, r) \setminus \{a\}$, and $1/f$ extends holomorphically to $D(a, r)$ with $(1/f)(a) = 0$.
>
> **Hint:** $|f| \to \infty$ implies $f$ is nonzero near $a$, so $1/f$ is holomorphic there; $|1/f| \to 0$ implies $1/f$ is bounded, hence removable.
>
> > [!note]- Full proof
> > Since $|f(z)| \to \infty$ as $z \to a$, choose $r$ small enough that $|f(z)| \geq 1$ for $0 < |z - a| < r$. Then $f$ is nowhere zero on this punctured disc, so $1/f$ is holomorphic there. Moreover, $|1/f(z)| \leq 1$, so $1/f$ is bounded on the punctured disc. By [[Thm - Riemann's Removable Singularity Theorem|Riemann's theorem]], $1/f$ extends to a holomorphic function on $D(a, r)$. The extension at $a$ is $\lim_{z \to a} 1/f(z) = 0$, since $|1/f(z)| \to 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Forward direction (⇒).** Suppose $a$ is a pole of order $k$ of $f$. The Laurent expansion is $f(z) = \sum_{n \geq -k} c_n (z - a)^n$ with $c_{-k} \neq 0$. Then $(z - a)^k f(z) = c_{-k} + c_{-k+1}(z - a) + \ldots$ tends to $c_{-k} \neq 0$ as $z \to a$. So $|f(z)| = |(z - a)^k f(z)|/|z - a|^k \sim |c_{-k}|/|z - a|^k \to \infty$.
>
> **Reverse direction (⇐).** Suppose $|f(z)| \to \infty$. By Lemma 1, $1/f$ extends holomorphically to $a$ with $(1/f)(a) = 0$. Since $1/f$ is holomorphic on $D(a, r)$ and not identically zero (else $f$ would be identically $\infty$, impossible), it has a Taylor expansion $1/f(z) = \sum_{n \geq k} d_n (z - a)^n$ with $d_k \neq 0$ for some $k \geq 1$ (the order of the zero at $a$).
>
> So $1/f(z) = (z - a)^k h(z)$ with $h(z) := \sum_{m \geq 0} d_{k+m}(z - a)^m$, $h(a) = d_k \neq 0$. Then $h$ is nonzero in a neighborhood of $a$ (continuity), so $f(z) = 1/(1/f(z)) = (z - a)^{-k}/h(z) = (z - a)^{-k} \tilde h(z)$ with $\tilde h = 1/h$ holomorphic and nonzero at $a$. Expanding $\tilde h$ in Taylor series: $\tilde h(z) = \sum_{m \geq 0} e_m (z - a)^m$ with $e_0 = \tilde h(a) = 1/d_k \neq 0$. Multiplying:
> $$f(z) = (z - a)^{-k} \sum_{m \geq 0} e_m (z - a)^m = \sum_{n \geq -k} e_{n + k}(z - a)^n.$$
> The coefficient of $(z - a)^{-k}$ is $e_0 = 1/d_k \neq 0$. So $f$ has a pole of order $k$ at $a$.
>
> **Equivalence with factorization.** The argument above shows $f(z) = (z - a)^{-k} \tilde h(z)$ with $\tilde h$ holomorphic and $\tilde h(a) \neq 0$. Conversely, any such factorization gives a pole of order $k$ by the same algebra.
>
> **Equivalence with order of zero of $1/f$.** The order of the zero of $1/f$ at $a$ is $k$ — the smallest $n$ with the Taylor coefficient $d_n \neq 0$ — and this equals the order of the pole of $f$ at $a$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Rational function pole analysis.** For a rational function $f = P/Q$ with $P, Q$ polynomials and $\gcd(P, Q) = 1$, the poles are exactly the zeros of $Q$, with pole orders equal to the multiplicities of $Q$'s zeros. The reverse problem (zeros of $f$) gives the zeros of $P$. So the algebra of $\mathbb{C}[z]$ factorizations encodes the pole/zero structure of rational functions.

**Pole at infinity for entire functions.** An entire function $f$ either has $|f| \to \infty$ as $|z| \to \infty$ (in which case $f(1/w)$ has a pole at $w = 0$ — meaning $f$ has a "pole at infinity" — and $f$ is a polynomial by Liouville-like arguments), or remains bounded (Liouville: $f$ constant), or behaves wildly (entire transcendental functions have essential singularity at $\infty$).

**Transfer function pole locations.** For a transfer function $H(s)$ of a linear system, the poles' locations determine stability. A pole at $s_0$ with $\operatorname{Re} s_0 > 0$ is unstable (response grows like $e^{\operatorname{Re} s_0 \cdot t}$); $\operatorname{Re} s_0 < 0$ is stable (decays). The order of the pole determines the "polynomial-times-exponential" form of the time response: a double pole gives $t e^{s_0 t}$ behaviour.

---

# Bridges

- **[[Def - Removable Singularity, Pole, Essential Singularity]]** — the definition the theorem characterizes.

- **[[Thm - Riemann's Removable Singularity Theorem]]** — the reciprocal trick applies Riemann to $1/f$.

- **[[Thm - Computing Residues]]** — once you know the pole order, residue formulas apply.

- **[[Thm - Argument Principle]]** — uses pole orders (with negative signs) to count poles.

---

# Unlocked by This

> [!tip] Meromorphic Functions and the Riemann Sphere *(from §3.5+)*
> A function whose only singularities are poles is *meromorphic*. Pole characterization is the key technical step in showing that meromorphic functions on $\hat{\mathbb{C}}$ are exactly **rational functions** $P(z)/Q(z)$.

> [!tip] Transfer Function Stability *(from Linear Systems)*
> The pole-location ⟺ stability dictionary for [[Def - Transfer Function and Stability|transfer functions]] is a direct application: poles in the left half-plane (stable) vs right half-plane (unstable) is the classification of asymptotic behaviour.

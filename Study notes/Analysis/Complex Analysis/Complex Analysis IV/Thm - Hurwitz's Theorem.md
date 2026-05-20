---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Locally Uniform Convergence"
  - "Thm - Locally Uniform Limit of Holomorphic is Holomorphic"
  - "Thm - Argument Principle"
  - "Thm - Rouché's Theorem"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ is open, $f_n : U \to \mathbb{C}$ is a sequence of holomorphic functions converging locally uniformly to $f : U \to \mathbb{C}$. Each $f_n$ is *nonvanishing* on $U$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Motivation

A natural question about locally uniform convergence: if each $f_n$ has *no zeros* on $U$, what can we say about the zeros of the limit $f$?

Hurwitz's theorem provides a remarkable dichotomy: either $f$ has no zeros either (the "no zero" property is preserved), or $f$ is *identically zero* on a connected component. There's no middle ground — the limit cannot have isolated zeros.

The intuition: zeros of holomorphic functions are robust — they don't appear or disappear under small perturbations, by the argument principle. If each $f_n$ has zero count $0$ on a small circle, the limit has zero count $0$ (by Rouché-like reasoning). So zeros cannot suddenly emerge in the limit.

This is the analog of "limit of injective functions is either injective or constant" — another Hurwitz-style theorem (with the proof using the same argument principle approach).

Hurwitz's theorem is the key tool in the Riemann mapping theorem proof: in extracting a biholomorphism via normal families, one needs to ensure the limit is injective (not just holomorphic). The "injective or constant" dichotomy is exactly what's needed.

---

# Sources and Targets

**Sources (Input Broadening)**

**Sequence of nonvanishing holomorphic functions converging locally uniformly.** The standard hypothesis.

**Sequence of injective holomorphic functions.** Property $B$: $f_n$ injective on $U$, $f_n \to f$ locally uniformly. Bridge: apply Hurwitz to $f_n - w$ for each $w \in \mathbb{C}$ — these are nonvanishing if and only if $f_n \neq w$, which fails if $f_n^{-1}(w)$ has $\geq 2$ elements. Hurwitz then gives: $f$ is either injective or constant.

**Sequence of polynomials with no zeros in a region.** Property $B$: polynomials with all zeros outside $U$. Bridge: directly applies; limit polynomial (or limit holomorphic function) is either nonvanishing or identically zero.

**Targets (Output Amplification)**

Combine with **Riemann mapping theorem proof.** Property $D$: extracting a biholomorphism from a normal family. Amplified result $E$: the extracted limit is injective (by Hurwitz applied to $f_n - w$).

Combine with **proof that $e^z$ is nonvanishing.** Property $D$: $(1 + z/n)^n \to e^z$ locally uniformly. Amplified result $E$: $e^z$ has no zeros (by Hurwitz applied to the polynomial approximations).

---

# Why Is It True

Suppose $f$ has a zero at $a \in U$ but is not identically zero. By the identity theorem (or just because the zeros of holomorphic functions are isolated), $a$ is an isolated zero. Choose a small circle $C = \{|z - a| = r\}$ with $f$ nonvanishing on $C$.

On the compact set $C$, $|f| \geq \delta > 0$ for some $\delta$. By locally uniform convergence, $f_n \to f$ uniformly on $C$, so for large $n$, $|f_n - f| < \delta \leq |f|$ on $C$.

By [[Thm - Rouché's Theorem|Rouché's theorem]], $f_n$ and $f$ have the same number of zeros inside $C$. But $f$ has at least one zero inside $C$ (namely $a$), while $f_n$ has *zero* zeros (it's nonvanishing). Contradiction.

So $f$ has no zeros, unless $f$ is identically zero (in which case "isolated zeros" doesn't apply). The dichotomy: $f \equiv 0$ or $f$ nonvanishing.

The conceptual content: **zero count is a continuous integer-valued function under locally uniform convergence**, by Rouché. Continuous + integer-valued + nonvanishing locally ⟹ no zeros, except for the degenerate $f \equiv 0$ case.

---

# What Makes This Hard

The non-obvious step is **applying Rouché's theorem to a small circle around the would-be zero of $f$**. The trick is to recognize that zeros of $f$ would be detected by winding numbers, and these would already be detected for large $n$ by the locally uniform convergence — contradicting nonvanishing of $f_n$. The common error is to argue "$f_n$ never zero, so $f$ never zero" directly — but $f$ *can* be zero in the limit; the dichotomy is just that $f$ is *either* nonzero everywhere *or* zero everywhere (on a connected component).

---

# Rederivation Scaffold

**High-level strategy:**
Suppose $f$ has an isolated zero. Choose a circle around it where $f$ is nonvanishing on the boundary. By locally uniform convergence and Rouché, $f_n$ has the same number of zeros inside as $f$, namely $\geq 1$. Contradicts nonvanishing of $f_n$. So $f$ has no isolated zeros, i.e., $f$ is identically zero or nonvanishing.

**Subgoal decomposition:**

1. **Suppose $f \not\equiv 0$ and has a zero at $a \in U$.** By the identity theorem, $a$ is an isolated zero.

2. **Choose a circle $C = \{|z - a| = r\}$ where $f \neq 0$ on $C$.** $|f| \geq \delta > 0$ on the compact $C$.

3. **For $n$ large, $|f_n - f| < \delta$ on $C$** (by locally uniform convergence).

4. **By Rouché, $f_n$ has the same zero count as $f$ inside $C$.** Specifically, $\geq 1$ zero (since $f$ has at least one).

5. **Contradicts $f_n$ nonvanishing on $U$.** So no isolated zero of $f$ can exist; $f$ is either identically zero or nonvanishing.

---

# Formal Proof

> [!note]- Complete formal proof
> Suppose $f$ is not identically zero on a connected component $U_0$ of $U$. We show $f$ has no zeros on $U_0$.
>
> Suppose for contradiction $f(a) = 0$ for some $a \in U_0$. Since $f$ is holomorphic on $U_0$ and not identically zero, by the identity theorem the zeros of $f$ are isolated. So there exists $r > 0$ with $\overline{D(a, r)} \subset U_0$ and $f(z) \neq 0$ for $z \in \overline{D(a, r)}\setminus\{a\}$.
>
> Let $C = \{|z - a| = r\}$. By compactness of $C$ and continuity of $|f|$, $|f(z)| \geq \delta > 0$ on $C$ for some $\delta$.
>
> By locally uniform convergence, $f_n \to f$ uniformly on $C$. Choose $n$ large enough that $|f_n(z) - f(z)| < \delta$ for all $z \in C$.
>
> Then on $C$: $|f_n - f| < \delta \leq |f|$. By [[Thm - Rouché's Theorem|Rouché's theorem]], $f_n$ and $f$ have the same number of zeros in $D(a, r)$. Since $f$ has at least one zero in $D(a, r)$ (at $a$), so does $f_n$. But $f_n$ is nonvanishing on $U$ (in particular on $D(a, r) \subset U$). Contradiction.
>
> So $f$ has no zeros on $U_0$. The dichotomy: on each connected component, $f$ is either identically zero or nonvanishing. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**$e^z$ has no zeros.** Apply Hurwitz to the sequence $(1 + z/n)^n \to e^z$ (locally uniformly on $\mathbb{C}$). Each $(1 + z/n)^n$ has zero only at $z = -n$, which is outside any fixed compact set for large $n$. So on any compact $K$, for $n$ large, $(1 + z/n)^n$ is nonvanishing. By Hurwitz, $e^z$ is either identically zero on $K$ (no — it's not!) or nonvanishing on $K$. Hence $e^z$ is nonvanishing everywhere.

**Riemann mapping theorem step.** Extracting a biholomorphism via normal families: take a sequence of injective holomorphic $f_n : U \to \mathbb{D}$ maximizing $|f_n'(z_0)|$. By Montel, extract a locally uniformly convergent subsequence $f_n \to f$. By Hurwitz applied to $f_n - w$ (which is nonvanishing for $w$ outside the image of $f_n$), $f$ is injective (or constant, which is ruled out by $|f_n'(z_0)|$ bounded below). The Riemann mapping theorem then proves $f$ is surjective onto $\mathbb{D}$.

**Failure example.** $f_n(z) = z/n \to 0$ locally uniformly. Each $f_n$ has a zero only at $z = 0$. The limit $f = 0$ is identically zero — falling in the "$\equiv 0$" case of the dichotomy. This shows the dichotomy is not vacuous: in this case, the limit is $\equiv 0$, not nonvanishing.

---

# Bridges

- **[[Thm - Rouché's Theorem]]** — the engine of the proof.

- **[[Thm - Argument Principle]]** — underlies Rouché.

- **[[Def - Locally Uniform Convergence]]** — the convergence assumption.

- **[[Thm - Locally Uniform Limit of Holomorphic is Holomorphic]]** — ensures the limit $f$ is holomorphic before applying Hurwitz.

---

# Unlocked by This

> [!tip] Riemann Mapping Theorem *(from §3.5+)*
> Hurwitz applied to $f_n - w$ proves the limit of injective functions is injective (or constant). Key step in [[Thm - Riemann Mapping Theorem (Statement)|Riemann mapping]].

> [!tip] Normal Families and Compactness *(from Function Theory)*
> Hurwitz combined with Montel's theorem characterizes normal families with additional non-degeneracy properties.

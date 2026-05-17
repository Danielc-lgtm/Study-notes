---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Lp Spaces"
  - "Thm - Completeness of Lp Spaces"
  - "Def - Convergence in Measure"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $1\le p<\infty$ and $f_n\to f$ in $L^p(\mu)$.

**(a)** Show $f_n\to f$ in [[Def - Convergence in Measure|measure]].

**(b)** Show there is a subsequence $f_{n_k}\to f$ $\mu$-**a.e.**

**(c)** Show by the [[Ex - The typewriter sequence|typewriter sequence]] (scaled into $L^p$) that the *full* sequence need not converge a.e. — so "$L^p$-convergent" sits strictly between "a.e.-convergent" and "convergent in measure."

**Recall:**

[[Thm - Completeness of Lp Spaces|Completeness]] of $L^p$ is proved by extracting a *rapidly Cauchy* subsequence. [[Ex - Markov's inequality|Markov's inequality]]: $\mu(|h|\ge\lambda)\le\lambda^{-p}\int|h|^p$.

---

# Convergent Strategy

**Problem class:** locating $L^p$-convergence among the modes of convergence.

**Assumption pattern:** $\|f_n-f\|_p\to0$. Markov ($p$-th power form) converts this into a measure bound. To get an a.e.-convergent subsequence, extract one with $\|f_{n_k}-f\|_p$ summably small, so the bad sets are Borel–Cantelli-summable.

**Theorem routing:** $\|f_n-f\|_p\to0\xrightarrow{\text{Markov}}$ in measure; extract $\|f_{n_k}-f\|_p\le2^{-k}\xrightarrow{\text{Markov + Borel–Cantelli}}$ a.e.

**Key decision point:** the fast subsequence — the same device as in the proof of [[Thm - Completeness of Lp Spaces|completeness]].

---

# Legal Operations Used

1. **Markov's inequality** (power-$p$ form) to pass from $L^p$ to measure.
2. **Extract a rapidly convergent subsequence.**
3. **First Borel–Cantelli lemma** to force a.e. convergence.

---

# Hints

> [!note]- Hint 1
> (a): $\mu(|f_n-f|>\varepsilon)=\mu(|f_n-f|^p>\varepsilon^p)\le\varepsilon^{-p}\int|f_n-f|^p=\varepsilon^{-p}\|f_n-f\|_p^p\to0$.

> [!note]- Hint 2
> (b): pick $n_k$ with $\|f_{n_k}-f\|_p\le2^{-k}$. Then $\mu(|f_{n_k}-f|>2^{-k/2})\le$ ? Sum over $k$.

> [!note]- Hint 3
> (c): the typewriter functions $\mathbf{1}_{I_{m,k}}$ have $\|\mathbf{1}_{I_{m,k}}\|_p=2^{-m/p}\to0$, so they converge to $0$ in $L^p$ — but converge a.e. nowhere.

---

# Solution

**Step 1 — (a) $L^p\Rightarrow$ measure.** By [[Ex - Markov's inequality|Markov]] applied to $|f_n-f|^p$ at level $\varepsilon^p$,
$$\mu(|f_n-f|>\varepsilon)=\mu(|f_n-f|^p>\varepsilon^p)\le\frac{1}{\varepsilon^p}\int|f_n-f|^p\,d\mu=\frac{\|f_n-f\|_p^p}{\varepsilon^p}\to0.$$
So $f_n\xrightarrow{\mu}f$.

**Step 2 — (b) An a.e.-convergent subsequence.** Since $\|f_n-f\|_p\to0$, choose $n_1<n_2<\cdots$ with $\|f_{n_k}-f\|_p\le2^{-k}$. By Markov,
$$\mu\big(|f_{n_k}-f|>2^{-k/2}\big)\le\frac{\|f_{n_k}-f\|_p^p}{2^{-kp/2}}\le\frac{2^{-kp}}{2^{-kp/2}}=2^{-kp/2}.$$
The series $\sum_k2^{-kp/2}$ converges, so by the [[Ex - The first Borel-Cantelli lemma|first Borel–Cantelli lemma]], $\mu(\limsup_k\{|f_{n_k}-f|>2^{-k/2}\})=0$ — i.e. for a.e. $x$, $|f_{n_k}(x)-f(x)|\le2^{-k/2}$ for all large $k$. Hence $f_{n_k}\to f$ $\mu$-a.e.

**Step 3 — (c) The full sequence can fail.** Scale the [[Ex - The typewriter sequence|typewriter sequence]]: $f_n=\mathbf{1}_{I_{m(n),k(n)}}$ on $[0,1]$ has $\|f_n\|_p^p=\lambda(I_{m(n),k(n)})=2^{-m(n)}\to0$, so $f_n\to0$ in $L^p$. But, as shown for the typewriter, $f_n(x)\not\to0$ for *any* $x$ — the full sequence converges a.e. nowhere, only a subsequence does.

> [!note]- Derivation
> So the modes are strictly ordered (on a finite-measure space, $p<\infty$): a.e.-convergence $\Rightarrow$ in measure, and $L^p$-convergence $\Rightarrow$ in measure, but $L^p$-convergence neither implies nor is implied by a.e.-convergence. What $L^p$-convergence *does* guarantee is an a.e.-convergent *subsequence*.

> [!note]- Complete formal solution
> (a) Markov: $\mu(|f_n-f|>\varepsilon)\le\varepsilon^{-p}\|f_n-f\|_p^p\to0$. (b) Choose $\|f_{n_k}-f\|_p\le2^{-k}$; Markov gives $\mu(|f_{n_k}-f|>2^{-k/2})\le2^{-kp/2}$, summable; first Borel–Cantelli gives $f_{n_k}\to f$ a.e. (c) Typewriter $f_n=\mathbf{1}_{I_{m(n),k(n)}}$: $\|f_n\|_p^p=2^{-m(n)}\to0$ but $f_n\to0$ a.e. nowhere. $\blacksquare$

---

# Key Takeaways

**$L^p$-convergence implies convergence in measure (via Markov) and always yields an a.e.-convergent subsequence (via a fast subsequence + Borel–Cantelli) — but not full a.e. convergence.** This places $L^p$-convergence precisely in the hierarchy of [[Def - Modes of Convergence|modes of convergence]]: it is incomparable with a.e.-convergence, both being stronger than convergence in measure. The "extract a rapidly convergent subsequence, then Borel–Cantelli" technique is the same one that proves [[Thm - Completeness of Lp Spaces|completeness of Lᵖ]] — fast subsequences are the universal bridge from a norm/measure statement to a pointwise statement.

**Markov's inequality is the standard one-way valve from "norm small" to "bad set small."** Whenever a convergence is given in an integral norm ($L^1$, $L^p$) and a measure-theoretic or pointwise consequence is wanted, Markov is the first step: it trades $\|f_n-f\|_p$ for $\mu(|f_n-f|>\varepsilon)$. Pushing further to a.e. convergence then costs a subsequence and a summability check. The trigger: "I have norm convergence, I want pointwise information" → "Markov, fast subsequence, Borel–Cantelli."

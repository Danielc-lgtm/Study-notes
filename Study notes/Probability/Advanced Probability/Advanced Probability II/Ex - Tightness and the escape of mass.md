---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Weak Convergence"
  - "Thm - Prokhorov's Theorem"
  - "Ex - Markov's inequality"
tags: [probability, advanced-probability]
---

# Problem Statement

**(a)** Show the sequence $\mu_n=\delta_n$ on $\mathbb{R}$ has no weak limit, and is not [[Def - Weak Convergence|tight]].

**(b)** Show that a uniform first-moment bound, $\sup_n\mathbb{E}|X_n|<\infty$, *implies* tightness of $(\mu_{X_n})$.

**(c)** Conclude: a uniformly $L^1$-bounded sequence of random variables always has a subsequence converging in distribution.

**Recall:**

[[Def - Weak Convergence|Tight]]: $\forall\varepsilon\,\exists$ compact $K$, $\sup_n\mu_n(K^c)\le\varepsilon$. [[Thm - Prokhorov's Theorem|Prokhorov]]: tight $\Rightarrow$ relatively weakly compact.

---

# Convergent Strategy

**Problem class:** diagnosing whether weak limits exist — tightness as the no-escape criterion.

**Assumption pattern:** weak convergence can fail *only* by mass escaping to infinity; tightness forbids exactly that. A moment bound forces tightness via [[Ex - Markov's inequality|Markov]].

---

# Legal Operations Used

1. **Test against a continuous function** to detect a failed weak limit.
2. **Markov's inequality** to get tightness from a moment bound.
3. **Prokhorov** for subsequential weak limits.

---

# Hints

> [!note]- Hint 1
> If $\delta_n\Rightarrow\mu$, then $\int f\,d\delta_n=f(n)\to\int f\,d\mu$ for every bounded continuous $f$. Take $f$ with $f(n)$ not convergent, or note any limit must be the zero measure.

> [!note]- Hint 2
> (b): [[Ex - Markov's inequality|Markov]] gives $\mu_{X_n}(|x|>R)=\mathbb{P}(|X_n|>R)\le R^{-1}\mathbb{E}|X_n|\le R^{-1}\sup_n\mathbb{E}|X_n|$.

> [!note]- Hint 3
> $[-R,R]$ is compact. Choose $R$ so the bound is $<\varepsilon$.

---

# Solution

**Step 1 — (a) $\delta_n$ escapes.** Suppose $\delta_n\Rightarrow\mu$ for some probability measure $\mu$. For any *compactly supported* continuous $f$, $\int f\,d\delta_n=f(n)=0$ for $n$ beyond the support, so $\int f\,d\mu=\lim f(n)=0$ — forcing $\mu=0$, not a probability measure. Contradiction: $\delta_n$ has no weak limit.

> [!note]- Derivation
> Equivalently, $\delta_n$ is *not tight*: for any compact $K\subseteq\mathbb{R}$, $K$ is bounded, so $n\notin K$ for large $n$, giving $\delta_n(K^c)=1\not\le\varepsilon$. The mass — a unit point mass — marches off to $+\infty$ and is invisible to every compact set. Non-tightness is exactly the failure mode of weak convergence.

**Step 2 — (b) A moment bound forces tightness.** Let $M=\sup_n\mathbb{E}|X_n|<\infty$. By [[Ex - Markov's inequality|Markov's inequality]], for every $R>0$ and every $n$,
$$\mu_{X_n}(\{|x|>R\})=\mathbb{P}(|X_n|>R)\le\frac{\mathbb{E}|X_n|}{R}\le\frac{M}{R}.$$
Given $\varepsilon>0$, choose $R=M/\varepsilon$; then $\sup_n\mu_{X_n}([-R,R]^c)\le\varepsilon$, and $[-R,R]$ is compact. So $(\mu_{X_n})$ is [[Def - Weak Convergence|tight]] — a uniform bound on $\mathbb{E}|X_n|$ uniformly confines the mass.

**Step 3 — (c).** By (b) the sequence $(\mu_{X_n})$ is tight; by [[Thm - Prokhorov's Theorem|Prokhorov's theorem]], it is relatively weakly compact — every subsequence has a further subsequence converging weakly to some probability measure. So a uniformly $L^1$-bounded sequence of random variables always has a subsequence converging in distribution.

> [!note]- Complete formal solution
> (a) $\delta_n\Rightarrow\mu$ would force $\int f\,d\mu=\lim f(n)=0$ for compactly supported $f$, so $\mu=0$ — impossible; equivalently $\delta_n(K^c)=1$ for any compact $K$ and large $n$, so not tight. (b) Markov: $\mu_{X_n}(|x|>R)\le M/R$; $R=M/\varepsilon$ gives tightness. (c) Tightness $+$ [[Thm - Prokhorov's Theorem|Prokhorov]] $\Rightarrow$ a weakly convergent subsequence. $\blacksquare$

---

# Key Takeaways

**Weak convergence fails in exactly one way — mass escaping to infinity — and tightness is precisely the hypothesis ruling it out.** The sequence $\delta_n$ is the canonical failure: a perfectly good unit mass that simply walks off the real line, leaving no limit. Tightness ("uniformly, a fixed compact set holds all but $\varepsilon$ of the mass") is the no-escape condition; it is the [[Def - Weak Convergence|weak-convergence]] analogue of [[Def - Uniform Integrability|uniform integrability]] (which forbids the escape of *expected mass to the tail*).

**A uniform moment bound buys tightness for free — via [[Ex - Markov's inequality|Markov]] — and tightness plus [[Thm - Prokhorov's Theorem|Prokhorov]] buys subsequential weak limits.** This is the standard existence argument in all of weak-convergence theory: to show a limit law exists, bound a moment, deduce tightness, extract a convergent subsequence; then a *uniqueness* argument (typically via [[Def - Characteristic Function|characteristic functions]] and [[Thm - Lévy's Continuity Theorem|Lévy's theorem]]) shows all subsequential limits coincide, upgrading to full convergence. "Tight $\Rightarrow$ subsequential limit; unique limit $\Rightarrow$ convergence" is the recipe behind the [[Thm - Central Limit Theorem|CLT]] and Donsker's invariance principle alike.

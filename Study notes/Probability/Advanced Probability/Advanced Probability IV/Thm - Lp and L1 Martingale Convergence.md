---
type: theorem
subject: advanced-probability
prereqs:
  - "Thm - Almost Sure Martingale Convergence"
  - "Def - Uniform Integrability"
  - "Thm - Doob's Maximal Inequality"
tags: [probability, advanced-probability]
---

# Notation

$(X_n)$ a [[Def - Martingale|martingale]] on a [[Def - Filtration|filtered space]]; $X_\infty=\lim X_n$; $\mathcal{F}_\infty=\sigma(\bigcup_n\mathcal{F}_n)$.

---

# Motivation

The [[Thm - Almost Sure Martingale Convergence|a.s. convergence theorem]] gives a pointwise limit $X_\infty$ — but *only* almost surely, and the limit can have strictly smaller expectation (mass escapes; the [[Thm - Almost Sure Martingale Convergence|product martingale]] converges a.s. to $0$ while $\mathbb{E}X_n\equiv1$). For the limit to be *useful* one wants convergence in $L^p$, hence $\mathbb{E}[X_n]\to\mathbb{E}[X_\infty]$ and the representation $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$. This theorem says exactly when that happens: for $p>1$, *$L^p$-boundedness suffices*; for $p=1$, the precise condition is *uniform integrability*. It also identifies the **closed** martingales — those of the form $\mathbb{E}[Z\mid\mathcal{F}_n]$ — as exactly the uniformly integrable ones, a clean structural classification.

---

# Sources and Targets

**Sources.** For $L^p$ ($p>1$): $\sup_n\mathbb{E}|X_n|^p<\infty$. For $L^1$: the martingale is [[Def - Uniform Integrability|uniformly integrable]] — and a standard *bridge into* UI is "$X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ for a fixed $Z\in L^1$," since conditional expectations of a fixed variable are automatically UI.

**Targets.** $L^p$/$L^1$ convergence gives $\mathbb{E}[X_n]\to\mathbb{E}[X_\infty]$ and the **closure** $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$ — a bijection between UI martingales and $L^1(\mathcal{F}_\infty)$. This is the form needed to apply [[Thm - Optional Stopping Theorem|optional stopping at unbounded stopping times]], to prove Lévy's 0–1 law, and to run the [[Thm - Strong Law of Large Numbers|SLLN]].

---

# Formal Statement

Let $(X_n)$ be a martingale.

**($L^p$ convergence, $1<p<\infty$.)** The following are equivalent: (i) $(X_n)$ is bounded in $L^p$; (ii) $X_n$ converges a.s. **and in $L^p$** to some $X_\infty\in L^p$; (iii) $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ for some $Z\in L^p$. Then $X_\infty=\mathbb{E}[Z\mid\mathcal{F}_\infty]$.

**($L^1$ convergence.)** The following are equivalent: (i) $(X_n)$ is **uniformly integrable**; (ii) $X_n$ converges a.s. **and in $L^1$** to some $X_\infty\in L^1$; (iii) $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ for some $Z\in L^1$ (the martingale is **closed**). Then $X_\infty=\mathbb{E}[Z\mid\mathcal{F}_\infty]$, and $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$.

---

# Why Is It True

**$L^p$ case, $p>1$.** $L^p$-bounded $\Rightarrow L^1$-bounded, so by the [[Thm - Almost Sure Martingale Convergence|a.s. convergence theorem]] $X_n\to X_\infty$ a.s. To upgrade to $L^p$: [[Thm - Doob's Maximal Inequality|Doob's Lᵖ inequality]] gives $\|X^*\|_p\le\frac{p}{p-1}\sup_n\|X_n\|_p<\infty$, where $X^*=\sup_n|X_n|$. So $|X_n-X_\infty|\le2X^*$ with $X^*\in L^p$ — a *dominating function*. Since $X_n\to X_\infty$ a.s. and $|X_n-X_\infty|^p\le(2X^*)^p\in L^1$, the [[Thm - Dominated Convergence Theorem|dominated convergence theorem]] gives $\mathbb{E}|X_n-X_\infty|^p\to0$ — $L^p$-convergence. **$p>1$ is used precisely so Doob's $L^p$ inequality holds**, manufacturing the dominator.

**$L^1$ case.** Here Doob's inequality is only weak-type ($p=1$), so there is no dominator — the [[Thm - Dominated Convergence Theorem|DCT]] route fails, and one needs the sharper [[Thm - Vitali Convergence Theorem|Vitali]] criterion. (i)$\Rightarrow$(ii): UI $\Rightarrow L^1$-bounded $\Rightarrow$ ([[Thm - Almost Sure Martingale Convergence|a.s. convergence]]) $X_n\to X_\infty$ a.s.; UI plus a.s. convergence gives $L^1$-convergence by the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]]. (ii)$\Rightarrow$(iii): set $Z=X_\infty$; for $A\in\mathcal{F}_m$ and $n\ge m$, the martingale property gives $\mathbb{E}[X_n\mathbf{1}_A]=\mathbb{E}[X_m\mathbf{1}_A]$, and $L^1$-convergence lets $n\to\infty$ to yield $\mathbb{E}[X_\infty\mathbf{1}_A]=\mathbb{E}[X_m\mathbf{1}_A]$ — exactly $X_m=\mathbb{E}[X_\infty\mid\mathcal{F}_m]$. (iii)$\Rightarrow$(i): the family $\{\mathbb{E}[Z\mid\mathcal{F}_n]\}$ of conditional expectations of a *fixed* $Z\in L^1$ is uniformly integrable — a standard fact ($\mathbb{E}[|\mathbb{E}[Z\mid\mathcal{F}_n]|\mathbf{1}_{\{\cdots\}}]\le\mathbb{E}[\mathbb{E}[|Z|\mid\mathcal{F}_n]\mathbf{1}_{\{\cdots\}}]$, and $|Z|$'s tail is uniformly small).

The slogan: **a.s. convergence is free from $L^1$-boundedness; *upgrading* it to norm convergence needs a no-escape condition — for $p>1$ Doob's inequality supplies a dominator (DCT), for $p=1$ the exact condition is uniform integrability (Vitali) — and the UI martingales are precisely the closed ones $\mathbb{E}[Z\mid\mathcal{F}_n]$.**

---

# What Makes This Hard

The crux is the $p=1$ versus $p>1$ dichotomy. For $p>1$, [[Thm - Doob's Maximal Inequality|Doob's Lᵖ inequality]] gives an $L^p$ dominator $X^*$ and the upgrade is plain [[Thm - Dominated Convergence Theorem|DCT]]. For $p=1$ there is *no* dominator (Doob is only weak-type), and one must invoke the [[Thm - Vitali Convergence Theorem|Vitali theorem]] with [[Def - Uniform Integrability|uniform integrability]] — and prove the non-obvious fact that conditional expectations of a fixed $L^1$ variable are UI. The standard error is to expect $L^1$-boundedness to give $L^1$-convergence; it gives only a.s. convergence, and the [[Thm - Almost Sure Martingale Convergence|product martingale]] shows the gap is real.

---

# Rederivation Scaffold

**High-level strategy.** A.s. convergence from $L^1$-boundedness (previous theorem). Upgrade: $p>1$ — Doob's $L^p$ inequality gives a dominator, DCT. $p=1$ — UI plus a.s. convergence, Vitali; identify closed martingales as the UI ones.

**Subgoal decomposition.**

1. **A.s. limit.** $L^p$-bounded ($p\ge1$) $\Rightarrow L^1$-bounded $\Rightarrow X_n\to X_\infty$ a.s. ([[Thm - Almost Sure Martingale Convergence|a.s. convergence theorem]]).
2. **$L^p$, $p>1$.** [[Thm - Doob's Maximal Inequality|Doob]]: $X^*\in L^p$; $|X_n-X_\infty|\le2X^*$; [[Thm - Dominated Convergence Theorem|DCT]] $\Rightarrow L^p$-convergence.
3. **$L^1$.** UI $+$ a.s. $\Rightarrow$ ([[Thm - Vitali Convergence Theorem|Vitali]]) $L^1$-convergence; $L^1$-limit through the martingale identity $\Rightarrow X_m=\mathbb{E}[X_\infty\mid\mathcal{F}_m]$.
4. **Closure.** $\{\mathbb{E}[Z\mid\mathcal{F}_n]\}$ is UI; so closed $\iff$ UI.

---

# Lemma Decomposition

> [!note]- Lemma 1: $L^p$ convergence for $p>1$
> **Statement:** $L^p$-bounded martingale ($p>1$) converges a.s. and in $L^p$.
>
> > [!note]- Full proof
> > $L^p$-bounded $\Rightarrow L^1$-bounded; [[Thm - Almost Sure Martingale Convergence|a.s. convergence]] gives $X_n\to X_\infty$ a.s. [[Thm - Doob's Maximal Inequality|Doob's Lᵖ inequality]] gives $\|X^*\|_p\le\frac{p}{p-1}\sup_n\|X_n\|_p<\infty$, $X^*=\sup_n|X_n|$. Then $|X_n-X_\infty|^p\le(2X^*)^p\in L^1$ and $|X_n-X_\infty|^p\to0$ a.s.; [[Thm - Dominated Convergence Theorem|DCT]] gives $\mathbb{E}|X_n-X_\infty|^p\to0$. $\square$

> [!note]- Lemma 2: Closed martingales are exactly the UI ones
> **Statement:** $(X_n)$ is UI iff $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$ for some $Z\in L^1$; then $X_n\to X_\infty$ in $L^1$ and $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$.
>
> > [!note]- Full proof
> > UI $\Rightarrow$: $L^1$-bounded, so $X_n\to X_\infty$ a.s.; UI $+$ a.s. $\Rightarrow$ ([[Thm - Vitali Convergence Theorem|Vitali]]) $L^1$-convergence. For $A\in\mathcal{F}_m$, $n\ge m$: $\mathbb{E}[X_n\mathbf{1}_A]=\mathbb{E}[X_m\mathbf{1}_A]$ (martingale); $L^1$-convergence lets $n\to\infty$: $\mathbb{E}[X_\infty\mathbf{1}_A]=\mathbb{E}[X_m\mathbf{1}_A]$, i.e. $X_m=\mathbb{E}[X_\infty\mid\mathcal{F}_m]$, so $(X_n)$ is closed by $Z=X_\infty$. Conversely, if $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]$, the family $\{\mathbb{E}[Z\mid\mathcal{G}]:\mathcal{G}\}$ is UI: $|X_n|\le\mathbb{E}[|Z|\mid\mathcal{F}_n]$ ([[Thm - Properties of Conditional Expectation|conditional Jensen]]), and on $\{|X_n|>M\}$ — an $\mathcal{F}_n$-event — $\mathbb{E}[|X_n|\mathbf{1}_{|X_n|>M}]\le\mathbb{E}[|Z|\mathbf{1}_{|X_n|>M}]$, which is small since $\mathbb{P}(|X_n|>M)\le M^{-1}\mathbb{E}|Z|$ is small and $|Z|\in L^1$ is [[Def - Absolute Continuity and Density|uniformly absolutely continuous]]. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 establishes the $L^p$ ($p>1$) equivalences (with (iii) by Lemma 2's argument in $L^p$). Lemma 2 establishes the $L^1$ equivalences and the closure $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$. In both, $X_\infty=\mathbb{E}[Z\mid\mathcal{F}_\infty]$ because $X_n=\mathbb{E}[Z\mid\mathcal{F}_n]\to\mathbb{E}[Z\mid\mathcal{F}_\infty]$ (the increasing-$\sigma$-algebra / Lévy form of the convergence theorem). $\blacksquare$

---

# Cross-Field Exercise Suggestions

The closure $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$ is **Lévy's upward theorem** — $\mathbb{E}[Z\mid\mathcal{F}_n]\to\mathbb{E}[Z\mid\mathcal{F}_\infty]$ — which yields **Lévy's 0–1 law** ($\mathbb{E}[\mathbf{1}_A\mid\mathcal{F}_n]\to\mathbf{1}_A$ for $A\in\mathcal{F}_\infty$) and proves the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]] for a countably generated $\sigma$-algebra. The *backward* (decreasing-$\sigma$-algebra) version is the engine of the [[Thm - Strong Law of Large Numbers|strong law of large numbers]].

---

# Bridges

- **[[Thm - Almost Sure Martingale Convergence]]** — supplies the a.s. limit; this theorem upgrades it to norm convergence.
- **[[Thm - Doob's Maximal Inequality]]** — its $L^p$ form ($p>1$) is the dominator for the DCT step.
- **[[Thm - Vitali Convergence Theorem]]** / **[[Def - Uniform Integrability]]** — the exact $p=1$ criterion; UI martingales are the closed ones.
- **[[Thm - Optional Stopping Theorem]]** — uniform integrability is precisely what lets optional stopping run at *unbounded* stopping times.

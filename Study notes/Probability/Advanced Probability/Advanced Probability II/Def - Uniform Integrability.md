---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Expectation and Moments"
  - "Def - Absolute Continuity and Density"
  - "Def - Modes of Convergence"
tags: [probability, advanced-probability]
---

# Notation

$(X_i)_{i\in I}$ a family of [[Def - Random Variable|random variables]] on $(\Omega,\mathcal{F},\mathbb{P})$; "UI" — uniformly integrable.

---

# Axiom Motivation

[[Def - Modes of Convergence|Convergence in probability]] is often easy to establish, but the *useful* conclusion is usually convergence in $L^1$ — convergence of *expectations*, $\mathbb{E}[X_n]\to\mathbb{E}[X]$. Convergence in probability does *not* give this: mass can escape (the spike $n\mathbf{1}_{[0,1/n]}\to0$ in probability, $\mathbb{E}=1$). What exactly must be added? **Uniform integrability** is the precise answer.

A single integrable variable $X$ has the property that $\mathbb{E}[|X|\mathbf{1}_{\{|X|>M\}}]\to0$ as $M\to\infty$ — its tail carries negligible expected mass. **Uniform integrability** demands this *uniformly over the whole family*: one threshold $M$ works for all $X_i$ at once. Equivalently — and this is the [[Def - Absolute Continuity and Density|absolute-continuity]] face — the integrals $\int_A|X_i|$ are uniformly small over small-probability sets $A$.

UI is exactly what forbids the *escape of mass*. The [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]] makes this exact: on a probability space, $X_n\to X$ in $L^1$ **iff** $X_n\to X$ in probability *and* $(X_n)$ is uniformly integrable. So UI is not a sufficient technical hypothesis bolted on for convenience — it is the *characterising* condition, the missing half. It also subsumes domination ([[Thm - Dominated Convergence Theorem|DCT]] is "dominated $\Rightarrow$ UI") and is the criterion for $L^1$-convergence of [[Def - Martingale|martingales]].

---

# The Definition

A family $(X_i)_{i\in I}$ of random variables is **uniformly integrable** (UI) if
$$\lim_{M\to\infty}\ \sup_{i\in I}\ \mathbb{E}\big[\,|X_i|\,\mathbf{1}_{\{|X_i|>M\}}\,\big]=0.$$
Equivalently (on a finite measure space): $\sup_i\mathbb{E}|X_i|<\infty$ **and** the integrals are [[Def - Absolute Continuity and Density|uniformly absolutely continuous]] —
$$\forall\varepsilon>0\ \exists\delta>0:\quad \mathbb{P}(A)<\delta\ \Longrightarrow\ \sup_i\mathbb{E}\big[|X_i|\mathbf{1}_A\big]<\varepsilon.$$

**Sufficient conditions.** (i) A *dominated* family, $|X_i|\le Y$ for a fixed $Y\in L^1$, is UI. (ii) An *$L^p$-bounded* family for some $p>1$, $\sup_i\mathbb{E}|X_i|^p<\infty$, is UI. (iii) The family $\{\mathbb{E}[Z\mid\mathcal{G}]:\mathcal{G}\subseteq\mathcal{F}\}$ of [[Def - Conditional Expectation|conditional expectations]] of a fixed $Z\in L^1$ is UI. A single $L^1$ variable, and any finite $L^1$ family, is UI.

---

# Relate to Other Fields / Compression

Uniform integrability is the probabilistic name for [[Def - Absolute Continuity and Density|uniformly absolutely continuous integrals]] — the compactness-type condition that controls $L^1$-convergence. By the Dunford–Pettis theorem it is precisely *relative weak compactness in $L^1$* — the family $(X_i)$ has weakly convergent subsequences. It generalises domination (the [[Thm - Dominated Convergence Theorem|DCT]] hypothesis): "dominated $\Rightarrow$ UI", and [[Thm - Vitali Convergence Theorem|Vitali]] is the sharp generalisation of DCT with "dominated" relaxed to "UI."

---

# Examples / Corollaries

**UI:** any family bounded in $L^p$, $p>1$ (by [[Ex - Lp boundedness implies uniform integrability|the power-of-ℙ(A) estimate]]); any dominated family; the conditional expectations of a fixed $Z\in L^1$.

**Not UI:** the spike $X_n=n\mathbf{1}_{[0,1/n]}$ — bounded in $L^1$ ($\mathbb{E}X_n=1$) but $\mathbb{E}[X_n\mathbf{1}_{\{X_n>M\}}]=1$ for all $n>M$. *$L^1$-boundedness alone never suffices* — mass can concentrate.

Corollary ([[Thm - Vitali Convergence Theorem|Vitali]]): if $X_n\xrightarrow{\mathbb{P}}X$ and $(X_n)$ is UI, then $X_n\xrightarrow{L^1}X$, hence $\mathbb{E}X_n\to\mathbb{E}X$.

Calibration: (i) Does $\sup_n\mathbb{E}|X_n|<\infty$ imply UI? No — the spike. (ii) Does $\sup_n\mathbb{E}|X_n|^2<\infty$? Yes. (iii) Is a UI family $L^1$-bounded? Yes — UI implies a uniform bound on $\mathbb{E}|X_i|$.

---

# Unlocked by This

> [!tip] Vitali's theorem and the upgrade from probability to $L^1$
> $X_n\to X$ in $L^1$ iff in probability and UI — the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]] on a probability space.

> [!tip] $L^1$ martingale convergence *(from [[Advanced Probability IV — Martingales in Discrete Time|Advanced Probability IV]])*
> A [[Def - Martingale|martingale]] converges almost surely *and in $L^1$* iff it is uniformly integrable — the UI martingales are exactly the closed ones, $X_n=\mathbb{E}[X_\infty\mid\mathcal{F}_n]$.

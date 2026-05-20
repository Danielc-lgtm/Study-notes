---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Weak Convergence"
  - "Def - Distribution Function"
tags: [probability, advanced-probability]
---

# Notation

$(\mu_n)$ probability measures on $\mathbb{R}^d$ (or a Polish space); $\mu_n\Rightarrow\mu$ — [[Def - Weak Convergence|weak convergence]]; **tight** as defined there.

---

# Motivation

To prove a sequence of laws has a [[Def - Weak Convergence|weak]] limit, one needs a *compactness* theorem: a criterion guaranteeing convergent subsequences. Prokhorov's theorem is that criterion. It identifies the right compactness notion as **tightness** — uniformly, no probability mass escapes to infinity — and asserts: a tight family of laws is *relatively compact* in the weak topology (every subsequence has a weakly convergent sub-subsequence). It is the **Bolzano–Weierstrass / Arzelà–Ascoli of probability measures**, and the standard route to proving weak limits exist: establish tightness, extract a convergent subsequence, identify the limit.

---

# Sources and Targets

**Sources.** Hypothesis: **tightness**, $\forall\varepsilon\,\exists$ compact $K$ with $\sup_n\mu_n(K^c)\le\varepsilon$. The standard *bridge* to tightness: a uniform moment bound — $\sup_n\mathbb{E}[|X_n|]<\infty$ (or any $\sup_n\mathbb{E}[\phi(|X_n|)]<\infty$ for $\phi\to\infty$) forces tightness, by [[Ex - Markov's inequality|Markov's inequality]] ($\mu_n(|x|>R)\le R^{-1}\sup_n\mathbb{E}|X_n|$).

**Targets.** Relative compactness yields *existence* of weak limits — combined with a *uniqueness* argument (all subsequential limits coincide, e.g. via [[Thm - Lévy's Continuity Theorem|characteristic functions]]) it gives full weak convergence. This subsequence-plus-uniqueness method is how the [[Thm - Central Limit Theorem|CLT]] and many limit theorems are proved.

---

# Statement

Let $(\mu_n)$ be probability measures on $\mathbb{R}^d$ (more generally a Polish space).

**(Prokhorov, the direction used.)** If $(\mu_n)$ is **tight**, then it is **relatively compact** for [[Def - Weak Convergence|weak convergence]]: every subsequence has a further subsequence converging weakly to *some* probability measure $\mu$.

**(Converse.)** On a Polish space, conversely, every relatively (weakly) compact family is tight. So **tightness $\Leftrightarrow$ relative weak compactness**.

---

# Why Is It True

Reduce to $d=1$ for transparency; the idea is the *Helly selection principle*.

A law $\mu_n$ is encoded by its [[Def - Distribution Function|distribution function]] $F_n$ — a non-decreasing function bounded in $[0,1]$. Enumerate the rationals $q_1,q_2,\dots$. The numbers $F_n(q_1)$ lie in $[0,1]$, so [[#|Bolzano–Weierstrass]] extracts a subsequence along which $F_n(q_1)$ converges; from *that* subsequence extract a further one along which $F_n(q_2)$ converges; iterate, and **diagonalise** — the diagonal subsequence has $F_n(q)$ convergent for *every* rational $q$. Define $F(q)=\lim F_n(q)$ on $\mathbb{Q}$, extend to $\mathbb{R}$ by right limits: $F$ is non-decreasing and right-continuous.

So far $F$ is a candidate "sub-distribution function" — but is it the distribution function of a *probability* measure, or has mass leaked away ($F(+\infty)<1$ or $F(-\infty)>0$)? **This is exactly where tightness enters.** Tightness gives a compact $[-R,R]$ with $\mu_n([-R,R]^c)\le\varepsilon$ for all $n$, i.e. $F_n(R)-F_n(-R)\ge1-\varepsilon$; passing to the limit, $F(+\infty)-F(-\infty)\ge1-\varepsilon$ for every $\varepsilon$, so $F$ has the full mass $1$. Hence $F$ *is* a genuine distribution function, of a probability measure $\mu$, and $\mu_n\Rightarrow\mu$ along the diagonal subsequence (convergence of $F_n$ at continuity points is the [[Def - Weak Convergence|Portmanteau]] criterion).

The slogan: **diagonalise to extract a subsequence whose distribution functions converge everywhere; tightness is precisely what stops the limiting mass from leaking to $\pm\infty$, so the limit is a genuine probability measure.** Diagonalisation gives a *sub*-probability limit always; tightness promotes it to a probability limit.

---

# What Makes This Hard

The diagonal extraction is standard; the *crux* is recognising that diagonalisation alone yields only a *sub-distribution function* — the limit $F$ might have $F(+\infty)<1$, mass having escaped — and that **tightness is exactly the hypothesis ruling this out**. Without tightness the theorem is false: $\mu_n=\delta_n$ has $F_n\to0$ everywhere, $F\equiv0$, no probability limit. The conceptual content is "tightness $=$ no escape of mass $=$ the [[Def - Uniform Integrability|uniform-integrability]] analogue for *location* rather than *size*."

---

# Rederivation Scaffold

**High-level strategy.** Encode $\mu_n$ by $F_n$; diagonalise over the rationals to get $F_n\to F$ pointwise on $\mathbb{Q}$; extend $F$ by right limits; use tightness to show $F$ has total mass $1$, hence is a distribution function; conclude $\mu_n\Rightarrow\mu$ along the subsequence.

**Subgoal decomposition.**

1. **Diagonal subsequence.** Bolzano–Weierstrass at each rational + diagonalisation $\Rightarrow F_n(q)\to F(q)$ for all $q\in\mathbb{Q}$.
2. **$F$ is a sub-distribution function.** Non-decreasing, extend by right limits to right-continuous $F$.
3. **Tightness $\Rightarrow$ full mass.** $\mu_n([-R,R]^c)\le\varepsilon\Rightarrow F(+\infty)-F(-\infty)\ge1-\varepsilon$, all $\varepsilon$; so $F$ has mass $1$.
4. **Conclude.** $F$ is the distribution function of a probability $\mu$; $F_n\to F$ at continuity points $\Rightarrow\mu_n\Rightarrow\mu$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Helly selection
> **Statement:** Any sequence of distribution functions has a subsequence converging at every continuity point of a non-decreasing right-continuous limit $F$.
>
> **Hint:** Diagonalise over the rationals: extract a subsequence that converges $F_n(q)\to F(q)$ for every $q\in\mathbb{Q}$ (Bolzano-Weierstrass at each $q$), then right-continuise to $\mathbb{R}$ by $F(x)=\inf_{q>x}F(q)$.
>
> **Why needed:** This is the existence-of-a-limit half of Prokhorov: it produces a candidate distribution function $F$ from any sequence $(F_n)$, with no hypothesis other than the values $F_n(q)\in[0,1]$. But $F$ may sub-probability mass (escape to infinity) — Lemma 2 closes that gap.
>
> > [!note]- Full proof
> > $F_n(q)\in[0,1]$; by Bolzano–Weierstrass and a diagonal argument over an enumeration of $\mathbb{Q}$, a subsequence has $F_n(q)\to F(q)$ for all rational $q$. $F$ is non-decreasing on $\mathbb{Q}$; extend to $\mathbb{R}$ by $F(x)=\inf_{q>x}F(q)$, making it right-continuous and non-decreasing. At a continuity point $x$ of $F$, sandwiching $x$ between rationals shows $F_n(x)\to F(x)$. $\square$

> [!note]- Lemma 2: Tightness gives a probability limit
> **Statement:** If $(\mu_n)$ is tight, the Helly limit $F$ satisfies $F(-\infty)=0$, $F(+\infty)=1$.
>
> **Hint:** Tightness directly says $F_n(R)-F_n(-R)\ge 1-\varepsilon$ for $R=R(\varepsilon)$ uniform in $n$; pass to the Helly subsequence at continuity points $\pm R'$ near $\pm R$ to inherit this bound for $F$.
>
> **Why needed:** Without tightness, the Helly limit $F$ in Lemma 1 may be a sub-probability ("mass escapes to infinity"). Tightness rules out this escape mechanism, certifying that $F$ corresponds to a genuine probability measure $\mu$ — which is the conclusion of Prokhorov's relative compactness.
>
> > [!note]- Full proof
> > Given $\varepsilon$, tightness supplies $R$ with $\mu_n([-R,R]^c)\le\varepsilon$, i.e. $F_n(R)-F_n(-R)\ge1-\varepsilon$, for all $n$. Taking limits along the subsequence at continuity points $R'>R$, $-R'<-R$: $F(R')-F(-R')\ge1-\varepsilon$. Hence $F(+\infty)-F(-\infty)\ge1-\varepsilon$ for every $\varepsilon$, so $=1$; with $0\le F\le1$ this forces $F(-\infty)=0$, $F(+\infty)=1$. So $F$ is a genuine distribution function. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 extracts a subsequence with $F_n\to F$ at continuity points, $F$ non-decreasing right-continuous. Lemma 2 uses tightness to give $F(-\infty)=0$, $F(+\infty)=1$, so $F$ is the distribution function of a probability measure $\mu$ ([[Def - Distribution Function|the F↔μ correspondence]]). Convergence of $F_n$ to $F$ at all continuity points is, by [[Def - Weak Convergence|Portmanteau]], $\mu_n\Rightarrow\mu$ along the subsequence. The converse (relative compactness $\Rightarrow$ tightness on a Polish space) is the standard inner-regularity argument. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Prokhorov is the compactness behind **Donsker's invariance principle** (rescaled random walks converge to Brownian motion — tightness in path space $C[0,1]$) and the existence of [[Thm - Central Limit Theorem|weak limits]] generally. The "tight $\Rightarrow$ subsequential limit; uniqueness $\Rightarrow$ full convergence" method is the universal recipe whenever a weak limit must be *constructed* rather than guessed.

---

# Bridges

- **[[Def - Weak Convergence]]** — tightness is the hypothesis, weak convergence the conclusion; Prokhorov makes them a compactness duality.
- **[[Thm - Lévy's Continuity Theorem]]** — supplies the *uniqueness* of subsequential limits (via characteristic functions) that upgrades Prokhorov's relative compactness to genuine convergence.
- **[[Def - Uniform Integrability]]** — tightness (no escape of *location*) is the weak-convergence analogue of uniform integrability (no escape of *mass*).

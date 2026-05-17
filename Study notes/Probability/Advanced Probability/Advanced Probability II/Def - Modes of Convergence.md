---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Random Variable"
  - "Def - Convergence in Measure"
  - "Def - Lp Spaces"
tags: [probability, advanced-probability]
---

# Notation

$X_n,X$ random variables on $(\Omega,\mathcal{F},\mathbb{P})$. The four modes: a.s., $\xrightarrow{\mathbb{P}}$ (probability), $\xrightarrow{L^p}$, $\xrightarrow{d}$ (distribution).

---

# Axiom Motivation

"$X_n\to X$" is ambiguous for *random* variables — there is no single right meaning, because $X_n$ and $X$ are functions, and functions can converge in many genuinely different ways. Probability theory needs *all four* standard modes, each the right hypothesis or conclusion for different theorems.

**Almost surely** — $X_n(\omega)\to X(\omega)$ for a.e. $\omega$ — is the strongest, "pointwise off a null set." It is the mode of the [[Thm - Strong Law of Large Numbers|strong law]]. **In probability** — $\mathbb{P}(|X_n-X|>\varepsilon)\to0$ — only asks the *bad set* to shrink; it is [[Def - Convergence in Measure|convergence in measure]] on a probability space, the mode of the [[Thm - Weak Law of Large Numbers|weak law]]. **In $L^p$** — $\mathbb{E}|X_n-X|^p\to0$ — is convergence of $p$-th moments of the error. **In distribution** — the *laws* $\mu_{X_n}$ converge [[Def - Weak Convergence|weakly]] — is the weakest; it does not even require the variables to be on the same space, and it is the mode of the [[Thm - Central Limit Theorem|central limit theorem]].

The point of cataloguing them is the **hierarchy** and the *one-directional* implications: a.s. $\Rightarrow$ in probability $\Rightarrow$ in distribution, and $L^p\Rightarrow$ in probability; *none* of the converses holds, and a.s. and $L^p$ are incomparable. Knowing exactly which mode a hypothesis supplies and which a conclusion needs — and which bridge ([[Def - Uniform Integrability|uniform integrability]], a dominating function, a subsequence) closes a gap — is the organising skill of all limit theory.

---

# The Definition

Let $X_n,X$ be random variables on a common $(\Omega,\mathcal{F},\mathbb{P})$ (except (d), which needs only laws).

**(a) Almost surely:** $X_n\xrightarrow{\text{a.s.}}X$ if $\mathbb{P}(\{\omega:X_n(\omega)\to X(\omega)\})=1$.

**(b) In probability:** $X_n\xrightarrow{\mathbb{P}}X$ if $\mathbb{P}(|X_n-X|>\varepsilon)\to0$ for every $\varepsilon>0$ — i.e. [[Def - Convergence in Measure|convergence in measure]].

**(c) In $L^p$** ($1\le p<\infty$): $X_n\xrightarrow{L^p}X$ if $X_n,X\in L^p$ and $\mathbb{E}[|X_n-X|^p]\to0$.

**(d) In distribution:** $X_n\xrightarrow{d}X$ if the laws $\mu_{X_n}\to\mu_X$ [[Def - Weak Convergence|weakly]] — $\mathbb{E}[f(X_n)]\to\mathbb{E}[f(X)]$ for every bounded continuous $f$; equivalently $F_{X_n}(t)\to F_X(t)$ at every continuity point of $F_X$.

**Hierarchy.** $\text{a.s.}\Rightarrow\mathbb{P}\Rightarrow d$; $\ L^p\Rightarrow\mathbb{P}$; and ($p\ge q$) $L^p\Rightarrow L^q$. No other implication holds in general. Partial converses: $\mathbb{P}\Rightarrow$ a.s. *along a subsequence*; $\mathbb{P}\Rightarrow L^1$ *under [[Def - Uniform Integrability|uniform integrability]]* ([[Thm - Vitali Convergence Theorem|Vitali]]); $\xrightarrow{d}$ to a *constant* $\Rightarrow\xrightarrow{\mathbb{P}}$.

---

# Relate to Other Fields / Compression

The four modes are the [[Measure Theory II — §2 Integration|measure-theory modes]] read on a probability space: a.s. $=$ [[Def - Almost Everywhere|a.e.]], in probability $=$ [[Def - Convergence in Measure|in measure]], $L^p$ $=$ $L^p$-norm convergence. Only **convergence in distribution** is genuinely probabilistic — it is convergence of the *laws* in the [[Def - Weak Convergence|weak topology]], the dual-space convergence tested against $C_b$, and it discards the coupling between $X_n$ and $X$ entirely. The implication hierarchy and the [[Def - Uniform Integrability|uniform-integrability]] bridge are exactly the [[Thm - Vitali Convergence Theorem|Vitali]] / [[Thm - Egorov's Theorem|Egorov]] picture from measure theory.

---

# Examples / Corollaries

**$L^p$ without a.s.:** the [[Ex - The typewriter sequence|typewriter sequence]] $\to0$ in every $L^p$ and in probability, but a.s. nowhere. **a.s. without $L^1$:** $X_n=n\mathbf{1}_{[0,1/n]}$ (on the uniform space) $\to0$ a.s. but $\mathbb{E}X_n=1$. **In distribution without in probability:** i.i.d. non-degenerate $X_n$ all have the same law, so $X_n\xrightarrow{d}X_1$, yet $X_n$ does not converge in probability to anything.

Corollary: convergence in distribution *to a constant* is equivalent to convergence in probability to that constant — the one case where the weakest mode upgrades.

Calibration: (i) Does a.s. $\Rightarrow L^1$? No — mass can escape. (ii) Does in probability $\Rightarrow$ a.s.? No — only along a subsequence. (iii) Can $X_n\xrightarrow{d}X$ with $X_n,X$ on different spaces? Yes — distribution convergence sees only laws.

---

# Unlocked by This

> [!tip] The limit theorems, sorted by mode
> The [[Thm - Weak Law of Large Numbers|weak law]] is convergence in probability; the [[Thm - Strong Law of Large Numbers|strong law]] is almost-sure convergence; the [[Thm - Central Limit Theorem|central limit theorem]] is convergence in distribution. Each theorem is, in part, a *statement about which mode*.

> [!tip] Uniform integrability bridges $\mathbb{P}\to L^1$
> [[Def - Uniform Integrability|Uniform integrability]] is exactly the extra hypothesis upgrading convergence in probability to $L^1$ — the [[Thm - Vitali Convergence Theorem|Vitali theorem]].

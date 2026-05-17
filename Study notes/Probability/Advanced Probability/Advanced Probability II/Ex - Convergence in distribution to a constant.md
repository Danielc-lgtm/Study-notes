---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Modes of Convergence"
  - "Def - Weak Convergence"
tags: [probability, advanced-probability]
---

# Problem Statement

**(a)** Show that if $X_n\xrightarrow{d}c$ for a *constant* $c$, then $X_n\xrightarrow{\mathbb{P}}c$ — convergence in distribution to a constant upgrades to convergence in probability.

**(b)** Combine with the [[Thm - Weak Law of Large Numbers|weak law]]: deduce that $S_n/n\xrightarrow{d}\mu$ already implies $S_n/n\xrightarrow{\mathbb{P}}\mu$.

**(c)** Explain why the upgrade *fails* for a non-degenerate limit.

**Recall:**

[[Def - Modes of Convergence|Convergence in distribution]] is [[Def - Weak Convergence|weak convergence]] of laws; convergence in probability is $\mathbb{P}(|X_n-X|>\varepsilon)\to0$.

---

# Convergent Strategy

**Problem class:** identifying the *one* case where the weakest convergence mode upgrades to a stronger one.

**Assumption pattern:** the limit is a *point mass* $\delta_c$. The event $\{|X_n-c|>\varepsilon\}$ is the complement of an interval around $c$, and $\delta_c$ charges the boundary with measure $0$ — so the [[Def - Weak Convergence|Portmanteau]] criterion applies directly.

---

# Legal Operations Used

1. **Portmanteau** at a continuity set of the limit.
2. **The constant limit has interval-complements as continuity sets.**

---

# Hints

> [!note]- Hint 1
> $\{|X_n-c|>\varepsilon\}=\{X_n\notin[c-\varepsilon,c+\varepsilon]\}$. The limit $\delta_c$ gives the closed set $[c-\varepsilon,c+\varepsilon]^c$ what probability?

> [!note]- Hint 2
> Portmanteau: $\limsup\mu_{X_n}(C)\le\delta_c(C)$ for closed $C$. Take $C=[c-\varepsilon,c+\varepsilon]^c$.

---

# Solution

**Step 1 — (a).** Suppose $X_n\xrightarrow{d}c$, i.e. $\mu_{X_n}\Rightarrow\delta_c$. Fix $\varepsilon>0$ and let $C=\mathbb{R}\setminus(c-\varepsilon,c+\varepsilon)$, a closed set. By the [[Def - Weak Convergence|Portmanteau theorem]] (closed-set form),
$$\limsup_n\mathbb{P}(|X_n-c|\ge\varepsilon)=\limsup_n\mu_{X_n}(C)\le\delta_c(C)=0,$$
since $c\notin C$. Hence $\mathbb{P}(|X_n-c|>\varepsilon)\to0$ — $X_n\xrightarrow{\mathbb{P}}c$.

**Step 2 — (b).** The [[Thm - Weak Law of Large Numbers|weak law]] is usually stated as $S_n/n\xrightarrow{\mathbb{P}}\mu$. By (a), it would have been enough to prove the *a priori* weaker $S_n/n\xrightarrow{d}\mu$ — since the limit $\mu$ is a constant, convergence in distribution to it is *equivalent* to convergence in probability. The two formulations of the weak law coincide.

**Step 3 — (c).** For a *non-degenerate* limit $X$ the upgrade fails: i.i.d. non-degenerate $X_n$ satisfy $X_n\xrightarrow{d}X_1$ trivially (all laws equal), yet $\mathbb{P}(|X_n-X_1|>\varepsilon)$ is a fixed positive number. The reason: convergence in distribution constrains only the *laws*, not the *joint behaviour* of $X_n$ and $X$; with a constant limit there is no joint behaviour to constrain — "$X_n$ near $c$" is a statement about $\mu_{X_n}$ alone — but with a random limit, closeness in law says nothing about closeness as functions.

> [!note]- Complete formal solution
> (a) $\mu_{X_n}\Rightarrow\delta_c$; Portmanteau on the closed set $C=[c-\varepsilon,c+\varepsilon]^c$ gives $\limsup\mathbb{P}(|X_n-c|\ge\varepsilon)\le\delta_c(C)=0$, so $X_n\xrightarrow{\mathbb{P}}c$. (b) The weak law's limit $\mu$ is constant, so $S_n/n\xrightarrow{d}\mu\iff S_n/n\xrightarrow{\mathbb{P}}\mu$. (c) For non-degenerate $X$, i.i.d. $X_n\xrightarrow{d}X_1$ but $\mathbb{P}(|X_n-X_1|>\varepsilon)>0$ fixed — distribution convergence ignores the coupling. $\blacksquare$

---

# Key Takeaways

**Convergence in distribution to a *constant* is equivalent to convergence in probability — the unique case where the weakest mode upgrades.** A point-mass limit has no "spread," so "the law of $X_n$ concentrates near $c$" *is* "$X_n$ is near $c$ with high probability." This is why the [[Thm - Weak Law of Large Numbers|weak law]] may be proved in whichever of the two forms is convenient, and why limit theorems with constant limits ([[Thm - Strong Law of Large Numbers|laws of large numbers]]) need not distinguish the two modes.

**For a non-degenerate limit the upgrade collapses, because convergence in distribution sees only laws, never the coupling.** $X_n\xrightarrow{d}X$ permits $X_n$ and $X$ to be wildly different as *functions* — even independent — as long as their laws match. This is the fundamental nature of [[Def - Weak Convergence|weak convergence]]: it is convergence of *measures on $\mathbb{R}$*, having discarded the probability space. The [[Thm - Central Limit Theorem|CLT]]'s "$\xrightarrow{d}N(0,1)$" is a statement purely about laws, and it would be *false* as a convergence-in-probability statement — there is no single Gaussian variable the normalised sums approach pointwise.

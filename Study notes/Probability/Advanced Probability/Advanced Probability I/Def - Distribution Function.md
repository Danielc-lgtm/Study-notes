---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Random Variable"
  - "Thm - Hahn-Carathéodory Extension Theorem"
tags: [probability, advanced-probability]
---

# Notation

$X$ a real [[Def - Random Variable|random variable]], $\mu_X$ its law; $F_X$ its distribution function; $g$ the quantile (generalised inverse).

---

# Axiom Motivation

The [[Def - Random Variable|law]] $\mu_X$ is a measure on $\mathcal{B}(\mathbb{R})$ — an infinite-dimensional object. Can it be encoded by a single *function*? Yes: by the **distribution function** $F_X(t)=\mathbb{P}(X\le t)$, the accumulated probability up to $t$.

That $F_X$ *determines* $\mu_X$ is the [[Thm - Dynkin's π-λ Theorem|π–λ]] principle: the rays $(-\infty,t]$ form a $\pi$-system generating $\mathcal{B}(\mathbb{R})$, so a measure is pinned down by its values on them — and those values are exactly $F_X$. So $F_X$ and $\mu_X$ are equivalent data; the function is just the more convenient handle.

The *converse* — which functions $F$ arise — is the deep direction. A distribution function is non-decreasing (more accumulated mass to the right), right-continuous ([[Thm - Properties of Measures|continuity from above]]: $\{X\le t_n\}\downarrow\{X\le t\}$ as $t_n\downarrow t$), with limits $0$ at $-\infty$ and $1$ at $+\infty$. Conversely *any* such $F$ is the distribution function of a unique law $\mu_F$ — built by the [[Thm - Hahn-Carathéodory Extension Theorem|Hahn–Carathéodory extension]] of the pre-measure $(a,b]\mapsto F(b)-F(a)$. So distribution functions and laws on $\mathbb{R}$ are in *bijection*.

This bijection has a powerful payoff: the **quantile transform**. The generalised inverse $g(u)=\inf\{t:F(t)\ge u\}$ pushes the [[Def - Lebesgue Measure|uniform measure]] on $(0,1)$ forward to $\mu_F$ — so $g(U)$, for $U$ uniform, has law $\mu_F$. *Every* law on $\mathbb{R}$ is realised as a function of a single uniform random variable. This is the foundation of simulation and of "put all random variables on one space."

---

# The Definition

The **distribution function** (cumulative distribution function) of a real random variable $X$ is
$$F_X(t)=\mathbb{P}(X\le t)=\mu_X((-\infty,t]),\qquad t\in\mathbb{R}.$$
It is **non-decreasing**, **right-continuous**, with $\lim_{t\to-\infty}F_X(t)=0$ and $\lim_{t\to+\infty}F_X(t)=1$, and it **determines $\mu_X$** uniquely (via $\mu_X((a,b])=F_X(b)-F_X(a)$ and $\pi$–$\lambda$).

Conversely, **any** function $F:\mathbb{R}\to[0,1]$ with these three properties is the distribution function of a unique probability measure $\mu_F$ on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ — the **Lebesgue–Stieltjes measure** of $F$.

The **quantile function** (generalised inverse) is $g(u)=\inf\{t\in\mathbb{R}:F(t)\ge u\}$, $u\in(0,1)$; it is non-decreasing, left-continuous, and satisfies $g(u)\le t\iff u\le F(t)$. If $U$ is uniform on $(0,1)$, then $g(U)$ has law $\mu_F$ — the **quantile (inverse-transform) construction**.

---

# Relate to Other Fields / Compression

The distribution function is the probabilist's name for the *cumulative* of a measure — and the bijection "$F\leftrightarrow\mu_F$" is exactly the Lebesgue–Stieltjes correspondence, built by the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]] just as [[Def - Lebesgue Measure|Lebesgue measure]] is built from "length." The decomposition of $F$ into a jump part, a singular-continuous part, and an absolutely continuous part is the [[Thm - Radon-Nikodym Theorem|Lebesgue decomposition]] of $\mu_F$ in disguise. The quantile transform is the universal **inverse-transform sampling** method and the reason the [[Def - Lebesgue Measure|uniform distribution]] generates all of one-dimensional probability.

---

# Examples / Corollaries

The uniform law on $[0,1]$ has $F(t)=t$ on $[0,1]$. The exponential($\lambda$) has $F(t)=(1-e^{-\lambda t})\mathbf{1}_{t\ge0}$. A point mass $\delta_m$ has $F=\mathbf{1}_{[m,\infty)}$, a single jump. A jump of $F$ at $t$ of height $h$ means $\mathbb{P}(X=t)=h$ — **$F$ is continuous at $t$ iff $X$ has no atom there**, and $F$ has at most countably many jumps.

Corollary (the quantile transform): for $U\sim\text{Unif}(0,1)$ and any distribution function $F$, $g(U)$ has distribution function $F$ — every law on $\mathbb{R}$ is a function of one uniform variable.

Calibration: (i) Must $F$ be continuous? No — jumps encode atoms. (ii) Is $F$ left- or right-continuous? Right — because $\{X\le t_n\}\downarrow\{X\le t\}$. (iii) Does $F$ determine $\mu_X$? Yes — by $\pi$–$\lambda$ on the rays.

---

# Unlocked by This

> [!tip] Convergence in distribution
> $X_n\to X$ [[Def - Modes of Convergence|in distribution]] iff $F_{X_n}(t)\to F_X(t)$ at every continuity point of $F_X$ — the distribution-function criterion for [[Thm - Lévy's Continuity Theorem|weak convergence]].

> [!tip] Putting all variables on one space
> The quantile transform realises any law as $g(U)$; combined with an infinite [[Thm - Product Measure|product]] of uniforms it places *any* sequence of independent variables on a single probability space.

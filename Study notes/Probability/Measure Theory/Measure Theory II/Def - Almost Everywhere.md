---
type: definition
subject: measure-theory
prereqs:
  - "Def - Measure and Measure Space"
  - "Def - Null Set and Completion"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space. "$\mu$-a.e." abbreviates "$\mu$-almost everywhere"; in probability "a.s." ("almost surely").

---

# Axiom Motivation

A measure cannot see [[Def - Null Set and Completion|null sets]]. So any statement that fails only on a null set is, *to the measure*, true everywhere. Promoting this observation to a working concept — "**almost everywhere**" — is what makes measure theory flexible enough to be useful.

The need is concrete. The pointwise limit of measurable functions may fail to exist at a few points; a function may be defined only off a null set; two functions may differ on a null set yet have identical integrals. Demanding *genuine* pointwise statements everywhere would make the convergence theorems false and $L^p$ spaces impossible. Demanding them only **almost everywhere** — outside a null exceptional set — is exactly the right weakening: weak enough that the theorems hold, strong enough that the conclusions are useful.

The reason a.e.-reasoning is *coherent* (rather than a slippery abuse) is the null sets' good behaviour, all from [[Thm - Properties of Measures|$\sigma$-subadditivity]]: a *countable* union of null sets is null. So countably many a.e.-statements can be conjoined into a single a.e.-statement — the exceptional sets pool into one null set. This is the precise reason one may say "$f_n\to f$ a.e. *and* $g_n\to g$ a.e.", combine, and still have an a.e.-statement. Uncountably many would break it; countably many do not — the same "$\sigma$" discipline as everywhere else.

---

# The Definition

A property $P(x)$, $x\in X$, holds **$\mu$-almost everywhere** ($\mu$-a.e.) if
$$\mu\big(\{x\in X:P(x)\text{ fails}\}\big)=0,$$
i.e. the failure set is a [[Def - Null Set and Completion|null set]] (in a [[Def - Null Set and Completion|complete]] space, equivalently contained in a null set).

Two functions $f,g$ are **equal a.e.** ($f=g$ a.e.) if $\mu(\{f\neq g\})=0$; $g$ is then a **version** of $f$. A sequence **converges a.e.** to $f$ if $\mu(\{x:f_n(x)\not\to f(x)\})=0$. When $\mu=\mathbb{P}$ is a probability measure one says **almost surely**.

**Countable stability.** If $P_1,P_2,\dots$ each hold $\mu$-a.e., then $\bigwedge_k P_k$ holds $\mu$-a.e.: the failure set $\bigcup_k\{P_k\text{ fails}\}$ is a countable union of null sets, hence null.

---

# Relate to Other Fields / Compression

"$f=g$ a.e." is the equivalence relation one quotients by to pass from the seminormed space $\mathcal{L}^p$ to the genuine normed space [[Def - Lp Spaces|$L^p$]] — null sets are the *kernel* of the seminorm, exactly as one quotients by the kernel to make a seminorm a norm in functional analysis. In probability "almost surely" *is* "a.e." for $\mathbb{P}$; the strong law of large numbers, almost-sure martingale convergence, and the "[[Def - Filtration|usual conditions]]" all live in this register. The slogan "measure-theoretic statements are immune to null-set modification" is the operational content.

---

# Examples / Corollaries

$\mathbf{1}_\mathbb{Q}=0$ $\lambda$-a.e. on $\mathbb{R}$ (failure set $\mathbb{Q}$, null). The functions $f_n=\mathbf{1}_{\{q_1,\dots,q_n\}}$ converge to $\mathbf{1}_\mathbb{Q}$ everywhere, and $\mathbf{1}_\mathbb{Q}=0$ a.e., so $\int f_n\,d\lambda=0\to0=\int\mathbf{1}_\mathbb{Q}\,d\lambda$. A function defined on $\mathbb{R}\setminus\mathbb{Q}$ only is, for $\lambda$, "defined a.e." and may be integrated.

Corollary: if $f=g$ a.e. then $\int f\,d\mu=\int g\,d\mu$ — the integral does not see null-set changes. Corollary: a.e. limits, a.e. suprema of countably many measurable functions are measurable (in a complete space).

Calibration: (i) Does "$f_n\to f$ a.e." require $f_n(x)\to f(x)$ for every $x$? No — only off a null set. (ii) Can uncountably many a.e.-statements be combined? Not in general — only countably many. (iii) If $f=g$ a.e. and $g$ is measurable, is $f$ measurable? Yes, in a complete space — the disagreement set is null hence measurable.

---

# Unlocked by This

> [!tip] $L^p$ spaces and a.e. convergence theorems
> Quotienting by a.e.-equality turns the $L^p$ seminorm into a norm — [[Def - Lp Spaces|$L^p$ spaces]] are spaces of equivalence classes. The [[Thm - Dominated Convergence Theorem|DCT]] and [[Thm - Monotone Convergence Theorem|MCT]] hypothesise convergence (and domination) only *a.e.*

> [!tip] Almost sure convergence *(from [[Advanced Probability II — Convergence and Limit Theorems|Advanced Probability]])*
> "Almost surely" is a.e. for $\mathbb{P}$; it is the strongest of the [[Def - Modes of Convergence|modes of convergence]] of random variables and the mode in which the [[Thm - Strong Law of Large Numbers|strong law]] holds.

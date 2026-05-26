---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Measurable Function"
  - "Thm - Approximation by Simple Functions"
  - "Thm - Egorov's Theorem"
  - "Thm - Regularity of Lebesgue Measure"
tags: [analysis, measure-theory]
---

# Notation

$\Omega\subseteq\mathbb{R}^n$ measurable with $\lambda(\Omega)<\infty$; $f:\Omega\to\mathbb{R}$ measurable; $\lambda$ Lebesgue measure.

---

# Motivation

How "wild" can a measurable function be? Lusin's theorem gives the reassuring answer: **not very**. Every measurable function — even one continuous nowhere, like $\mathbf{1}_\mathbb{Q}$ — becomes *continuous* once you delete a set of arbitrarily small measure. Measurability is "continuity off a small set," the function-level twin of [[Thm - Egorov's Theorem|Egorov]]'s "uniform convergence off a small set" and of [[Thm - Regularity of Lebesgue Measure|regularity]]'s "Borel set is open off a small set." It is the precise sense in which the measurable world is only a small perturbation of the continuous world.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is "$f$ measurable on a set $\Omega$ of finite Lebesgue measure." Many situations encode this hypothesis only implicitly, and recognising the disguise is what lets one reach for Lusin in problems that do not announce themselves as Lusin problems.

The first disguised source is any measurable function on a probability space. The condition $\lambda(\Omega)<\infty$ is automatic when $(\Omega,\mathcal{A},\mathbb{P})$ is a probability space, so any real-valued random variable $X$ on a Polish space with a Borel-regular law falls inside Lusin's reach: $\mathbb{P}(\Omega)=1<\infty$ is trivial, and inner regularity holds on any Radon probability space. The concrete problem: given an almost-surely-finite random variable $X$ on $[0,1]$, find a compact $K$ with $\mathbb{P}(K)>1-\delta$ on which $X$ is continuous. This is the technical input one needs when approximating $X$ by bounded continuous functions in probability, or constructing couplings that preserve continuity off a small exceptional set — the foundational step in many weak-convergence and optimal-transport arguments.

The second disguised source is a measurable map one wishes to approximate in $L^p$ by continuous functions of compact support. The problem "show $\|f-g\|_{L^p}<\varepsilon$ for some $g\in C_c$" does not announce itself as a Lusin problem, but the bridge is direct: truncate $f$ to a bounded function $f_M=f\mathbf{1}_{|f|\le M}\mathbf{1}_{|x|\le R}$ supported in a ball of finite measure, and $f_M$ becomes a bounded measurable function on a finite-measure set — exactly Lusin's setup. A typical example: extending the Fourier transform from $C_c(\mathbb{R}^n)$ to $L^2(\mathbb{R}^n)$ requires the density of $C_c$, and the only route from "measurable" to "continuous" passes through Lusin combined with Tietze extension.

The third disguised source is a Borel function on a Polish space with a Radon measure. The bridge from general Polish-space measurability to Lusin's Euclidean setup is the abstract form of Lusin (Borel-measurable plus inner regularity on compacts), and the verification is automatic on any Radon space. A concrete example: in optimal transport on a Polish space, the cost function $c(x,y)$ is typically only Borel measurable, but for many compactness arguments one needs $c$ to be continuous off a set of small $\pi$-mass for any transport plan $\pi$. Lusin applied on the product Polish space — viewing $\pi$ itself as the finite measure — converts measurability of the cost into continuity off a thin set, enabling the standard tightness-and-continuity arguments of Villani's theory.

**Targets (Output Amplification)**

The conclusion is "$f$ is continuous on a compact set $F$ with $\lambda(\Omega\setminus F)<\delta$." This thin output, combined with other standard tools, produces some of the most-used facts in analysis.

The first amplification is Lusin combined with the Tietze extension theorem. Tietze extends a continuous function on a closed subset of $\mathbb{R}^n$ to a continuous function on all of $\mathbb{R}^n$; Lusin produces a compact $F$ on which $f$ is continuous with $\lambda(\Omega\setminus F)<\delta$; Tietze extends $f|_F$ to a globally continuous $g$ on $\mathbb{R}^n$, and a smooth truncation makes $g$ compactly supported with the same sup-norm. The amplified result: every measurable $f$ agrees, off a set of measure $<\delta$, with some $g\in C_c(\mathbb{R}^n)$. This is precisely the proof that $C_c(\mathbb{R}^n)$ is dense in [[Def - Lp Spaces|Lᵖ(ℝⁿ)]] for $p<\infty$ — the density lever underlying convolution approximation, Fourier inversion, and essentially every PDE existence proof that begins "assume smooth data, pass to the limit."

The second amplification is Lusin paired with [[Thm - Egorov's Theorem|Egorov's theorem]]. Egorov upgrades pointwise convergence to uniform convergence off a small set; Lusin upgrades measurability to continuity off a small set. Intersected, they yield: if $f_n\to f$ pointwise almost everywhere with each $f_n$ measurable, then off a set of measure $<\delta$ each $f_n$ is continuous *and* $f_n\to f$ uniformly. The amplified result is a uniform-continuous-convergence picture for any measurable convergence — the engine behind continuous-selection theorems, the construction of continuous modifications of measurable stochastic processes (Kolmogorov-Centsov style), and the proof that quasi-everywhere statements upgrade to everywhere statements on a continuous version.

The third amplification is Lusin inside regularity proofs for solutions of elliptic PDEs. Suppose $u$ is a weak solution and one knows only that $u$ is measurable on a bounded domain. Lusin produces a compact $F$ with $u|_F$ continuous and small complement; combined with a maximum principle, a local energy estimate, or a De Giorgi oscillation lemma, one bootstraps continuity from "off a small set" to "off a set of capacity zero" to full continuity. The amplified result: measurability plus an elliptic-style estimate yields Hölder regularity — the strategy underlying De Giorgi-Nash-Moser regularity for divergence-form equations, and the regularity of free boundaries in obstacle problems where the coincidence set is known only as a measurable set.

---

# Statement

Let $\Omega\subseteq\mathbb{R}^n$ be measurable with $\lambda(\Omega)<\infty$ and $f:\Omega\to\mathbb{R}$ measurable. Then for every $\delta>0$ there exists a **compact** set $F\subseteq\Omega$ with
$$\lambda(\Omega\setminus F)<\delta\qquad\text{and}\qquad f|_F:F\to\mathbb{R}\ \text{is continuous}.$$
One cannot in general take $\delta=0$.

---

# Why Is It True

Build the result in two layers, then assemble.

*Layer 1 — simple functions are continuous off a small set.* A [[Def - Simple Function|simple function]] $s=\sum\alpha_i\mathbf{1}_{A_i}$ is constant on each level set $A_i$. By [[Thm - Regularity of Lebesgue Measure|inner regularity]] pick a compact $F_i\subseteq A_i$ with $\lambda(A_i\setminus F_i)$ tiny. The $F_i$ are *disjoint compact* sets, so they are mutually positively separated, and a function constant on each of finitely many separated compacts is continuous on their union. So $s$ is continuous on $\bigcup F_i$, which misses only a small set.

*Layer 2 — general $f$ via approximation.* Write $f$ as a pointwise limit of simple functions $s_n$ ([[Thm - Approximation by Simple Functions]]). Each $s_n$ is continuous off a small set $\Omega\setminus F_n$ (Layer 1, budget $\delta2^{-n}$). By [[Thm - Egorov's Theorem|Egorov]], $s_n\to f$ *uniformly* off another small set $\Omega\setminus F_0$. Intersect: on $F=\bigcap_{n\ge0}F_n$ — still of measure $>\lambda(\Omega)-\delta$ — *every* $s_n$ is continuous **and** $s_n\to f$ uniformly. A uniform limit of continuous functions is continuous, so $f|_F$ is continuous.

The mechanism: **regularity makes each simple function continuous off a small set; Egorov makes the approximation uniform off a small set; uniformity transmits continuity to the limit.** Three "off a small set" facts, intersected, yield one.

---

# What Makes This Hard

The non-obvious idea is the *two-layer reduction*: one does not attack $f$ directly but factors the problem as "simple functions are nearly continuous" + "the approximation is nearly uniform." The subtle technical point in Layer 1: a function constant on each piece of a partition is continuous on the *union of compact representatives* precisely because disjoint compacts are *separated* — on the full (non-compact) level sets it would not be. And Layer 2 *needs uniform* convergence (hence Egorov, hence finite measure): a merely pointwise limit of continuous functions is not continuous, which is the whole reason $\mathbf{1}_\mathbb{Q}$ is discontinuous everywhere.

---

# Rederivation Scaffold

**High-level strategy.** Simple functions: continuous off a small set by inner regularity of level sets. General $f$: approximate by simple functions, make each continuous off a small set, make the approximation uniform off a small set (Egorov), intersect, use "uniform limit of continuous is continuous."

**Subgoal decomposition.**

1. **Simple case.** $s=\sum\alpha_i\mathbf{1}_{A_i}$: pick compact $F_i\subseteq A_i$, $\lambda(A_i\setminus F_i)<\delta/\ell$; $s$ is continuous on $\bigsqcup F_i$ (constant on each of finitely many separated compacts).
2. **Approximants.** $s_n\uparrow f$ simple ([[Thm - Approximation by Simple Functions]]); apply step 1 to each with budget $\delta2^{-n-1}$, get compact $F_n$.
3. **Uniformise.** [[Thm - Egorov's Theorem|Egorov]]: compact $F_0$, $\lambda(\Omega\setminus F_0)<\delta/2$, $s_n\to f$ uniformly on $F_0$.
4. **Assemble.** $F=\bigcap_{n\ge0}F_n$ compact, $\lambda(\Omega\setminus F)<\delta$; each $s_n$ continuous on $F$, $s_n\to f$ uniformly on $F$, so $f|_F$ continuous.

---

# Lemma Decomposition

> [!note]- Lemma 1: Simple functions are continuous off a small set
> **Statement:** A measurable simple $s$ on $\Omega$ is continuous on a compact $F$ with $\lambda(\Omega\setminus F)<\delta$.
>
> > [!note]- Full proof
> > Write $s=\sum_{i=1}^\ell\alpha_i\mathbf{1}_{A_i}$, $A_i$ disjoint measurable, $\bigsqcup A_i=\Omega$. By [[Thm - Regularity of Lebesgue Measure|inner regularity]] choose compact $F_i\subseteq A_i$ with $\lambda(A_i\setminus F_i)<\delta/\ell$. Then $F=\bigsqcup_i F_i$ is compact, $\lambda(\Omega\setminus F)=\sum_i\lambda(A_i\setminus F_i)<\delta$, and $s|_F$ is continuous: the $F_i$ are disjoint compact hence separated, and $s$ is constant ($=\alpha_i$) on each $F_i$. $\square$

> [!note]- Lemma 2: Uniform limit of continuous is continuous
> **Statement:** If $g_n|_F$ are continuous and $g_n\to g$ uniformly on $F$, then $g|_F$ is continuous.
>
> > [!note]- Full proof
> > Standard $\varepsilon/3$: $|g(x)-g(y)|\le|g(x)-g_n(x)|+|g_n(x)-g_n(y)|+|g_n(y)-g(y)|$; the outer terms $<\varepsilon/3$ for large $n$ by uniformity, the middle $<\varepsilon/3$ for $y$ near $x$ by continuity of $g_n$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Take $s_n\uparrow f$ simple ([[Thm - Approximation by Simple Functions]]). By Lemma 1, each $s_n$ is continuous on a compact $F_n$ with $\lambda(\Omega\setminus F_n)<\delta2^{-n-1}$. By [[Thm - Egorov's Theorem|Egorov]], there is compact $F_0$, $\lambda(\Omega\setminus F_0)<\delta/2$, with $s_n\to f$ uniformly on $F_0$. Set $F=\bigcap_{n\ge0}F_n$: compact, and $\lambda(\Omega\setminus F)\le\sum_{n\ge0}\lambda(\Omega\setminus F_n)<\delta$. On $F$ every $s_n$ is continuous and $s_n\to f$ uniformly, so by Lemma 2 $f|_F$ is continuous. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Lusin + the Tietze extension theorem yields: every measurable $f$ agrees, off a set of measure $<\delta$, with a *globally continuous* function — hence $C_c(\mathbb{R}^n)$ is dense in [[Def - Lp Spaces|Lᵖ(ℝⁿ)]] for $p<\infty$. This density is the standard reduction "prove it for continuous functions, pass to the $L^p$ limit," used throughout Fourier analysis and PDE.

---

# Bridges

- **[[Thm - Egorov's Theorem]]** — supplies the uniformity (Layer 2); both theorems are "measurable $=$ nice off a small set."
- **[[Thm - Approximation by Simple Functions]]** — supplies the simple approximants.
- **[[Thm - Regularity of Lebesgue Measure]]** — inner regularity of level sets is Layer 1.

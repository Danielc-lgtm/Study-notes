---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Measurable Function"
  - "Def - Almost Everywhere"
  - "Thm - Properties of Measures"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space, $\Omega\in\mathcal{A}$ with $\mu(\Omega)<\infty$; $f_k,f:\Omega\to\mathbb{R}$ measurable.

---

# Motivation

Pointwise (or [[Def - Almost Everywhere|a.e.]]) convergence is a *local* statement — each point converges at its own rate — and that non-uniformity is exactly why a.e. convergence is so much weaker than uniform convergence and so much harder to integrate against. Egorov's theorem says that on a *finite-measure* space the non-uniformity is confined to a *small* set: discard a set of measure $<\delta$ and on what remains the convergence is genuinely **uniform**. A.e. convergence is "uniform convergence off a small set." This is the bridge that lets one import the power of uniform convergence into the measurable world.

---

# Sources and Targets

**Sources.** Hypotheses: $f_k\to f$ a.e. and $\mu(\Omega)<\infty$. The finite-measure hypothesis is essential and is the broadening to watch — it holds automatically on any *probability* space, so Egorov is available "for free" throughout probability.

**Targets.** "Uniform off a small set" feeds [[Thm - Lusin's Theorem|Lusin's theorem]] (a measurable function is continuous off a small set — Egorov controls the simple-function approximants) and the proof of the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]] (to upgrade convergence in measure to $L^1$).

---

# Formal Statement

Let $\mu(\Omega)<\infty$ and let $f_k,f:\Omega\to\mathbb{R}$ be measurable with $f_k\to f$ $\mu$-a.e. on $\Omega$. Then for every $\delta>0$ there exists a measurable set $F\subseteq\Omega$ with
$$\mu(\Omega\setminus F)<\delta\qquad\text{and}\qquad \sup_{x\in F}|f_k(x)-f(x)|\xrightarrow[k\to\infty]{}0,$$
i.e. $f_k\to f$ **uniformly on $F$**. (For $\Omega\subseteq\mathbb{R}^n$ one may take $F$ compact.) One cannot take $\delta=0$.

---

# Why Is It True

Quantify "$x$ has not yet converged." For each resolution $2^{-i}$ and each stage $j$, let
$$C_{i,j}=\bigcup_{k\ge j}\{x:|f_k(x)-f(x)|>2^{-i}\}$$
be the set of points that, at *some* time $\ge j$, still err by more than $2^{-i}$. As $j$ grows, $C_{i,j}$ shrinks; and a point converging to $f$ eventually leaves it forever, so $\bigcap_j C_{i,j}$ is contained in the (null) non-convergence set. By [[Thm - Properties of Measures|continuity from above]] — *here is where $\mu(\Omega)<\infty$ is spent* — $\mu(C_{i,j})\to0$ as $j\to\infty$.

So for each $i$ choose a stage $J(i)$ with $\mu(C_{i,J(i)})<\delta\,2^{-i}$. Discard the union $\bigcup_i C_{i,J(i)}$ — total measure $<\delta$ by $\sigma$-subadditivity. On the surviving set $F$, for *every* $i$, all $x\in F$ satisfy $|f_k(x)-f(x)|\le2^{-i}$ once $k\ge J(i)$ — and $J(i)$ does not depend on $x$. That is the definition of uniform convergence.

The mechanism in one line: **a.e. convergence makes each "bad set" $C_{i,j}$ shrink to a null set; finite total measure lets [[Thm - Properties of Measures|continuity from above]] turn "shrinks to null" into "has small measure at a finite stage"; a $\delta2^{-i}$ budget then removes all bad sets at once.** Continuity from above is the only non-trivial input, and it is exactly the step that fails without finite measure — whence $\delta=0$ is impossible (on $[0,1]$, $f_k(x)=x^k\to\mathbf{1}_{\{1\}}$ converges nowhere-uniformly, but uniformly on each $[0,1-\delta]$).

---

# What Makes This Hard

The whole difficulty is *constructing the right bad sets and budgeting*. The double index is essential: $i$ controls the *error tolerance*, $j$ controls the *time*; one must take the bad set to be a union over all times $k\ge j$ (not a single time) so that escaping it means converging *uniformly from then on*. The $\delta2^{-i}$ budget — geometric, so the total is $<\delta$ — is the standard device, but pairing it with continuity-from-above (which silently uses $\mu(\Omega)<\infty$) is the step most often missed.

---

# Rederivation Scaffold

**High-level strategy.** Build doubly-indexed bad sets $C_{i,j}$ ("err by $>2^{-i}$ at some time $\ge j$"); continuity from above shrinks them; remove a $\delta2^{-i}$-budgeted union; uniform convergence survives.

**Subgoal decomposition.**

1. **Bad sets.** $C_{i,j}=\bigcup_{k\ge j}\{|f_k-f|>2^{-i}\}$; note $C_{i,j}\downarrow$ in $j$ and $\bigcap_j C_{i,j}\subseteq\{f_k\not\to f\}$, null.
2. **Shrink.** $\mu(\Omega)<\infty$ + continuity from above $\Rightarrow\mu(C_{i,j})\to0$; pick $J(i)$ with $\mu(C_{i,J(i)})<\delta2^{-i}$.
3. **Remove.** $F=\Omega\setminus\bigcup_i C_{i,J(i)}$; $\mu(\Omega\setminus F)\le\sum_i\delta2^{-i}=\delta$.
4. **Uniformity.** $x\in F\Rightarrow x\notin C_{i,J(i)}\Rightarrow|f_k(x)-f(x)|\le2^{-i}$ for all $k\ge J(i)$, uniformly in $x$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Bad sets shrink to null
> **Statement:** $C_{i,j}=\bigcup_{k\ge j}\{|f_k-f|>2^{-i}\}$ satisfies $\mu(C_{i,j})\to0$ as $j\to\infty$.
>
> **Hint:** Continuity from above; the finite-measure hypothesis lives here.
>
> > [!note]- Full proof
> > $C_{i,j+1}\subseteq C_{i,j}$ (fewer times in the union). If $x\in\bigcap_j C_{i,j}$ then for every $j$ some $k\ge j$ has $|f_k(x)-f(x)|>2^{-i}$, so $f_k(x)\not\to f(x)$; hence $\bigcap_j C_{i,j}\subseteq\{f_k\not\to f\}$, a null set. Since $\mu(\Omega)<\infty$, [[Thm - Properties of Measures|continuity from above]] applies: $\mu(C_{i,j})\downarrow\mu(\bigcap_j C_{i,j})=0$. $\square$

> [!note]- Lemma 2: Budgeted removal yields uniformity
> **Statement:** With $J(i)$ chosen so $\mu(C_{i,J(i)})<\delta2^{-i}$ and $F=\Omega\setminus\bigcup_i C_{i,J(i)}$: $\mu(\Omega\setminus F)<\delta$ and $f_k\to f$ uniformly on $F$.
>
> > [!note]- Full proof
> > $\mu(\Omega\setminus F)=\mu(\bigcup_i C_{i,J(i)})\le\sum_i\mu(C_{i,J(i)})<\sum_i\delta2^{-i}=\delta$. For uniformity: given $\varepsilon>0$ pick $i$ with $2^{-i}<\varepsilon$; every $x\in F$ avoids $C_{i,J(i)}$, so $|f_k(x)-f(x)|\le2^{-i}<\varepsilon$ for all $k\ge J(i)$ — and $J(i)$ is independent of $x$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemmas 1–2 give a measurable $F$ with $\mu(\Omega\setminus F)<\delta$ on which $f_k\to f$ uniformly. For $\Omega\subseteq\mathbb{R}^n$, shrink $F$ to a compact subset via [[Thm - Regularity of Lebesgue Measure|inner regularity]], losing $<\delta$ more measure. The example $f_k(x)=x^k$ on $[0,1]$ shows $\delta=0$ is impossible. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Egorov is the hidden engine of [[Thm - Lusin's Theorem|Lusin's theorem]] and appears in the proof of the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]]. In probability, applied on the (finite-measure!) probability space, it says: **a.s. convergence of random variables is uniform off an event of probability $<\delta$** — a structural fact behind many a.s.-to-$L^1$ upgrade arguments.

---

# Bridges

- **[[Thm - Lusin's Theorem]]** — Egorov controls the convergence of simple-function approximants, the first step of Lusin.
- **[[Thm - Properties of Measures]]** — continuity from above is the sole non-elementary input, and the reason finite measure is required.
- **[[Def - Convergence in Measure]]** — Egorov's "uniform off a small set" sits between a.e. convergence and convergence in measure.

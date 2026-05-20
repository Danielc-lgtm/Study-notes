---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Simple Function"
  - "Def - Measurable Function"
  - "Thm - Operations Preserve Measurability"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A})$ a measurable space; $f:X\to[0,\infty]$; $s_n\in\mathcal{S}^+$ [[Def - Simple Function|simple functions]]. $s_n\uparrow f$ means $s_n$ increasing with pointwise limit $f$.

---

# Motivation

The Lebesgue [[Def - The Integral|integral]] is *defined* on [[Def - Simple Function|simple functions]] and then extended. For the extension to reach every measurable function, simple functions must be *dense from below*: every non-negative measurable $f$ must be the increasing pointwise limit of simple functions. This theorem provides exactly that — and the approximation is *explicit and monotone*, which is what makes it interlock with the [[Thm - Monotone Convergence Theorem|monotone convergence theorem]] to define and compute integrals.

---

# Sources and Targets

**Sources.** The hypothesis "$f$ measurable, $f\ge0$" is the input. The construction also runs verbatim for $f:X\to[-\infty,\infty]$ by splitting $f=f^+-f^-$.

**Targets.** "$\exists s_n\uparrow f$ simple" is the workhorse for *every* definition and proof about integrals: define $\int f=\lim\int s_n$; prove linearity, monotonicity, [[Thm - Monotone Convergence Theorem|MCT]], [[Thm - Fubini-Tonelli Theorem|Fubini]] first for simple functions then pass to the limit. It is the "[[Def - Generated σ-Algebra|prove on generators, extend]]" principle for functions.

---

# Statement

Let $(X,\mathcal{A})$ be measurable and $f:X\to[0,\infty]$. Then **$f$ is measurable if and only if** there is a sequence $(s_n)$ of measurable simple functions $s_n:X\to[0,\infty)$ with
$$0\le s_1\le s_2\le\cdots\le f,\qquad s_n(x)\xrightarrow[n\to\infty]{}f(x)\quad\text{for every }x\in X.$$
Moreover the convergence is *uniform* on any set where $f$ is bounded.

---

# Why Is It True

The "if" direction is free: a pointwise limit of measurable functions is measurable ([[Thm - Operations Preserve Measurability]]).

The "only if" is an explicit construction — **dyadic slicing of the range**. To approximate $f$ at resolution $2^{-n}$, chop the value-axis $[0,\infty)$ into the layers $[k2^{-n},(k+1)2^{-n})$ for $k=0,1,\dots,n2^n-1$, and cap at height $n$. Define $s_n(x)=k2^{-n}$ when $f(x)$ lies in the $k$-th layer, and $s_n(x)=n$ when $f(x)\ge n$. Equivalently $s_n=\varphi_n\circ f$ where $\varphi_n(t)=2^{-n}\lfloor 2^n t\rfloor\wedge n$.

This is simple (finitely many values), measurable (its level sets are $f^{-1}$ of the layers, measurable since $f$ is), and $\le f$ (rounding *down*). Why *increasing* in $n$? Because halving the layer height refines the partition — passing from resolution $2^{-n}$ to $2^{-n-1}$ subdivides each layer, so the rounded-down value can only rise; and raising the cap from $n$ to $n+1$ can only help. Why convergent? Where $f(x)<n$, the rounding error is $f(x)-s_n(x)<2^{-n}\to0$; once $n>f(x)$ this bound kicks in, so $s_n(x)\to f(x)$ (and $s_n(x)\to\infty=f(x)$ where $f(x)=\infty$).

The decisive design choice is **slicing the range, not the domain**. Riemann slices the domain into intervals — fine for continuous $f$, useless for $\mathbf{1}_\mathbb{Q}$. Lebesgue slices the range; the layers $f^{-1}([k2^{-n},(k+1)2^{-n}))$ are arbitrary measurable sets, so the approximation works for *any* measurable $f$, however discontinuous. This is the same idea as [[Def - Simple Function|simple functions vs. step functions]], here made into an algorithm.

---

# What Makes This Hard

The construction is short; the subtle points are *why monotone* and *why this slicing*. Monotonicity is not automatic for an arbitrary approximation — it is engineered by *halving* the layer height each step (so partitions refine) and by *raising* the cap. A non-dyadic or non-refining choice loses monotonicity and breaks the link to MCT. The conceptual hurdle is appreciating that range-slicing, not domain-slicing, is what makes the result hold for all measurable $f$ — students trained on Riemann sums instinctively slice the domain.

---

# Rederivation Scaffold

**High-level strategy.** Define $s_n$ by rounding $f$ down to a multiple of $2^{-n}$, capped at $n$. Check simple, measurable, $\le f$, increasing (refinement), convergent (error $<2^{-n}$ once $n>f$).

**Subgoal decomposition.**

1. **Define the rounding map.** $\varphi_n(t)=2^{-n}\lfloor 2^n t\rfloor$ for $t<n$, $\varphi_n(t)=n$ for $t\ge n$; set $s_n=\varphi_n\circ f$.
2. **Simple and measurable.** $s_n$ takes the $n2^n+1$ values $\{k2^{-n}\}\cup\{n\}$; each level set is $f^{-1}$ of an interval, measurable.
3. **$s_n\le f$ and increasing.** Rounding down gives $\le f$; halving the mesh refines the partition, so $s_n\le s_{n+1}$.
4. **Convergence.** For $n>f(x)$ (finite case), $0\le f(x)-s_n(x)<2^{-n}\to0$; for $f(x)=\infty$, $s_n(x)=n\to\infty$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The dyadic rounding functions
> **Statement:** $\varphi_n(t)=2^{-n}\lfloor 2^n t\rfloor\wedge n$ satisfy $\varphi_n\le\varphi_{n+1}\le t$ and $\varphi_n(t)\to t$ on $[0,\infty]$, with $t-2^{-n}\le\varphi_n(t)\le t$ for $t<n$.
>
> > [!note]- Full proof
> > For $t<n$: $\lfloor 2^n t\rfloor$ is the largest integer $\le 2^n t$, so $2^n t-1<\lfloor 2^n t\rfloor\le 2^n t$, giving $t-2^{-n}<\varphi_n(t)\le t$. Refinement: $\lfloor 2^{n+1}t\rfloor 2^{-(n+1)}\ge\lfloor 2^n t\rfloor 2^{-n}$ because the finer dyadic grid contains the coarser, so a finer round-down is at least as large; and the cap rises from $n$ to $n+1$. Hence $\varphi_n\le\varphi_{n+1}\le t$. Convergence: for fixed $t<\infty$ and $n>t$, $0\le t-\varphi_n(t)<2^{-n}\to0$; for $t=\infty$, $\varphi_n(\infty)=n\to\infty$. $\square$

> [!note]- Lemma 2: $s_n=\varphi_n\circ f$ works
> **Statement:** $s_n=\varphi_n\circ f$ is measurable, simple, $0\le s_1\le s_2\le\cdots\le f$, $s_n\to f$ pointwise.
>
> > [!note]- Full proof
> > $\varphi_n$ is a Borel function (piecewise constant) with finite range, so $s_n=\varphi_n\circ f$ has finite range — simple — and is measurable as a composition of measurable maps. The pointwise inequalities and convergence transfer directly from Lemma 1 evaluated at $t=f(x)$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> "If": $f=\lim s_n$ is a pointwise limit of measurable functions, measurable by [[Thm - Operations Preserve Measurability]]. "Only if": Lemmas 1–2 construct $s_n=\varphi_n\circ f\in\mathcal{S}^+$ with $0\le s_1\le s_2\le\cdots\le f$ and $s_n(x)\to f(x)$ for all $x$. On a set where $f\le M$, for $n>M$ the bound $f-s_n<2^{-n}$ is uniform, giving uniform convergence there. $\blacksquare$

---

# Cross-Field Exercise Suggestions

This is the engine behind the *standard machine* of integration theory: to prove an identity about integrals (linearity, [[Thm - Fubini-Tonelli Theorem|Fubini]], the change-of-variables formula, properties of [[Def - Conditional Expectation|conditional expectation]]), prove it for indicators, extend to simple functions by linearity, extend to $f\ge0$ by this theorem plus [[Thm - Monotone Convergence Theorem|MCT]], extend to signed $f$ by $f=f^+-f^-$. Every theorem in Measure Theory II–III is proved by this four-step ladder.

---

# Bridges

- **[[Thm - Monotone Convergence Theorem]]** — the partner: this theorem produces $s_n\uparrow f$, MCT then gives $\int s_n\uparrow\int f$, *defining and computing* the integral.
- **[[Def - Simple Function]]** — simple functions are the "easy class"; this theorem makes them dense from below.
- **[[Thm - Lusin's Theorem]]** — uses simple-function approximation as its first step.

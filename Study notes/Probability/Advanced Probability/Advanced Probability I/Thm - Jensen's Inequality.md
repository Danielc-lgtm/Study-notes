---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Expectation and Moments"
  - "Def - Probability Space"
tags: [probability, advanced-probability]
---

# Notation

$X$ a [[Def - Random Variable|random variable]] on a [[Def - Probability Space|probability space]], $X\in L^1$; $\varphi:\mathbb{R}\to\mathbb{R}$ (or on an interval $I$) **convex**.

---

# Motivation

Expectation is linear: $\mathbb{E}[aX+b]=a\mathbb{E}[X]+b$. What happens under a *nonlinear* function $\varphi$? In general $\mathbb{E}[\varphi(X)]$ and $\varphi(\mathbb{E}X)$ differ — but if $\varphi$ is **convex** they differ in a *fixed direction*: $\mathbb{E}[\varphi(X)]\ge\varphi(\mathbb{E}X)$. Jensen's inequality is this statement. It is the single most-used inequality in probability: it produces the moment inequalities, the monotonicity of $L^p$-norms, the non-negativity of variance and of entropy/KL-divergence, and the contraction property of [[Def - Conditional Expectation|conditional expectation]] — all as one-line corollaries of choosing the right convex $\varphi$.

---

# Sources and Targets

**Sources.** Hypotheses: $\varphi$ convex, $X\in L^1$ (so $\mathbb{E}X$ is defined and lies in the domain). The crucial source-broadening: $\varphi$ need only be convex *on an interval containing the range of $X$*; and the probabilistic version requires $\mathbb{P}(\Omega)=1$ — Jensen is *false* for a general (non-probability) measure, since it needs $\mathbb{E}[1]=1$.

**Targets.** Choosing $\varphi$: $\varphi(x)=|x|^p$ gives $\|X\|_p$ non-decreasing in $p$ (moment monotonicity); $\varphi(x)=x^2$ gives $\mathrm{Var}(X)\ge0$; $\varphi(x)=e^x$ gives the bound behind [[Thm - Cramér's Theorem|Cramér's theorem]]; $\varphi(x)=-\log x$ gives the non-negativity of KL-divergence and the AM–GM inequality; $\varphi$ convex applied to [[Def - Conditional Expectation|conditional expectation]] gives the conditional Jensen inequality, the key to $L^p$-boundedness of [[Def - Martingale|martingales]].

---

# Statement

Let $I\subseteq\mathbb{R}$ be an open interval, $X$ a random variable with $X\in I$ a.s. and $X\in L^1$ (so $\mathbb{E}X\in I$), and $\varphi:I\to\mathbb{R}$ **convex**. Then $\varphi(X)^-\in L^1$ (so $\mathbb{E}[\varphi(X)]$ is well-defined in $(-\infty,\infty]$) and
$$\mathbb{E}[\varphi(X)]\ \ge\ \varphi(\mathbb{E}[X]).$$
If $\varphi$ is strictly convex, equality holds iff $X$ is a.s. constant.

---

# Why Is It True

A convex function lies *above each of its tangent (support) lines*, and *equals* one of them at any chosen point. This is the whole proof.

Fix the point $m=\mathbb{E}[X]$. Convexity guarantees a **supporting line** at $m$: a real number $c$ (a subgradient — the slope of a line through $(m,\varphi(m))$) such that
$$\varphi(x)\ \ge\ \varphi(m)+c(x-m)\qquad\text{for all }x\in I,$$
with equality at $x=m$. (For differentiable $\varphi$, $c=\varphi'(m)$; in general $c$ is any value between the left and right derivatives, which exist by convexity.) The line is a *global lower bound* for $\varphi$ that *touches* it at $m$.

Now substitute the random variable $X$ for $x$ and take expectations — a [[Thm - Properties of the Integral|monotone, linear]] operation:
$$\mathbb{E}[\varphi(X)]\ \ge\ \mathbb{E}\big[\varphi(m)+c(X-m)\big]=\varphi(m)+c\,(\mathbb{E}[X]-m)=\varphi(m)+0=\varphi(\mathbb{E}X).$$
The middle step is *linearity of expectation*; the term $\mathbb{E}[X]-m$ vanishes *by the choice $m=\mathbb{E}X$*.

The slogan: **bound the convex $\varphi$ below by its tangent at the mean; the tangent is linear, expectation passes through it exactly, and it touches $\varphi$ at the mean.** The convexity is used once (to produce the tangent line); the probability normalisation $\mathbb{E}[1]=1$ is used once (so that $\mathbb{E}[\varphi(m)]=\varphi(m)$). Strict convexity makes the tangent inequality strict off $m$, so equality forces $X=m$ a.s.

Equivalently, $\varphi=\sup$ of all its supporting lines $\ell$; expectation commutes with each line, $\mathbb{E}[\varphi(X)]\ge\sup_\ell\mathbb{E}[\ell(X)]=\sup_\ell\ell(\mathbb{E}X)=\varphi(\mathbb{E}X)$ — the same idea read as "$\varphi$ is an envelope of lines."

---

# What Makes This Hard

The proof is two lines once the *idea* is seen — and the idea is the supporting line at the mean. The non-obvious moves: (i) choose the tangent point to be *exactly* $\mathbb{E}X$, so that the linear term integrates to zero; (ii) realise that the *probability* normalisation is essential — $\mathbb{E}[\varphi(m)]=\varphi(m)$ needs $\mathbb{E}[1]=1$, which is why Jensen fails for non-probability measures. The common error is to apply Jensen with the inequality the wrong way (it goes "$\mathbb{E}\varphi\ge\varphi\mathbb{E}$" for *convex* $\varphi$; concave reverses it) or to forget that $\mathbb{E}X$ must lie in the domain.

---

# Rederivation Scaffold

**High-level strategy.** Take the supporting line of $\varphi$ at $m=\mathbb{E}X$; it lies below $\varphi$ and is linear; apply $\mathbb{E}$ and use linearity to kill the slope term.

**Subgoal decomposition.**

1. **Supporting line.** Convexity $\Rightarrow$ at $m$ there is $c$ with $\varphi(x)\ge\varphi(m)+c(x-m)$ for all $x$.
2. **Substitute $X$ and take expectations.** $\mathbb{E}[\varphi(X)]\ge\varphi(m)+c(\mathbb{E}X-m)$.
3. **Kill the slope term.** $m=\mathbb{E}X\Rightarrow\mathbb{E}X-m=0$, leaving $\mathbb{E}[\varphi(X)]\ge\varphi(\mathbb{E}X)$.
4. **Equality.** Strict convexity $\Rightarrow$ tangent inequality strict off $m$ $\Rightarrow$ equality forces $X=m$ a.s.

---

# Lemma Decomposition

> [!note]- Lemma 1: Supporting line of a convex function
> **Statement:** If $\varphi:I\to\mathbb{R}$ is convex and $m\in I$, there is $c\in\mathbb{R}$ with $\varphi(x)\ge\varphi(m)+c(x-m)$ for all $x\in I$.
>
> > [!note]- Full proof
> > Convexity gives, for $x<m<y$, $\frac{\varphi(m)-\varphi(x)}{m-x}\le\frac{\varphi(y)-\varphi(m)}{y-m}$ (the difference quotients are non-decreasing). Hence the left-derivative $\sup_{x<m}\frac{\varphi(m)-\varphi(x)}{m-x}$ and right-derivative $\inf_{y>m}\frac{\varphi(y)-\varphi(m)}{y-m}$ exist and the former is $\le$ the latter; take any $c$ between them. Then for $x>m$, $\varphi(x)-\varphi(m)\ge c(x-m)$, and for $x<m$, $\varphi(m)-\varphi(x)\le c(m-x)$ i.e. again $\varphi(x)\ge\varphi(m)+c(x-m)$. $\square$

> [!note]- Lemma 2: Jensen from the supporting line
> **Statement:** $\mathbb{E}[\varphi(X)]\ge\varphi(\mathbb{E}X)$.
>
> > [!note]- Full proof
> > By Lemma 1 with $m=\mathbb{E}X$, $\varphi(X)\ge\varphi(m)+c(X-m)$ pointwise. The right side is in $L^1$; this also shows $\varphi(X)^-\le\varphi(m)^-+|c||X-m|\in L^1$, so $\mathbb{E}[\varphi(X)]$ is well-defined. By [[Thm - Properties of the Integral|monotonicity and linearity]] of expectation, $\mathbb{E}[\varphi(X)]\ge\varphi(m)+c(\mathbb{E}X-m)=\varphi(m)=\varphi(\mathbb{E}X)$, using $\mathbb{E}[1]=1$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 supplies the supporting line at $m=\mathbb{E}X$; Lemma 2 substitutes $X$, takes expectations, and uses $\mathbb{E}X-m=0$. For strict convexity, $\varphi(x)>\varphi(m)+c(x-m)$ for $x\neq m$, so $\mathbb{E}[\varphi(X)]=\varphi(\mathbb{E}X)$ forces $\mathbb{P}(X\neq m)=0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Pick the convex $\varphi$ and reap a named inequality. $\varphi(x)=|x|^{q/p}$ ($q\ge p$) gives $\|X\|_p\le\|X\|_q$ — *moment monotonicity* on a probability space. $\varphi(x)=x\log x$ gives the non-negativity of **entropy / KL-divergence** (Gibbs' inequality) — the foundation of information theory. $\varphi$ convex applied to a [[Def - Conditional Expectation|conditional expectation]] gives **conditional Jensen** $\mathbb{E}[\varphi(X)\mid\mathcal{G}]\ge\varphi(\mathbb{E}[X\mid\mathcal{G}])$, which makes $|M_n|^p$ a [[Def - Martingale|submartingale]] when $M_n$ is a [[Def - Martingale|martingale]] — the engine of [[Thm - Doob's Maximal Inequality|Doob's Lᵖ inequality]].

---

# Bridges

- **[[Thm - Hölder and Minkowski Inequalities]]** — Young's inequality, hence Hölder, is convexity of $-\log$ run through an integral; Jensen is the general such statement.
- **[[Def - Conditional Expectation]]** — conditional Jensen ($\mathcal{G}$-conditional version) is proved by the identical supporting-line argument and is central to martingale $L^p$-theory.
- **[[Ex - Markov's inequality]]** — Markov, Chebyshev, and Jensen together are the "probabilistic inequalities" toolkit.

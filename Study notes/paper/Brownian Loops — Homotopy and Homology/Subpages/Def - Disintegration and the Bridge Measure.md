---
type: definition
subject: probability
prereqs:
  - "Def - Brownian Motion on a Riemannian Manifold"
  - "Def - Signed and Infinite Measures for Loop Measures"
tags: [probability, measure-theory, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$(X,g)$ a [[Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure|Riemannian surface]], $p(t,x,y)$ its [[Def - Heat Kernel and Heat Semigroup|heat kernel]], $\mathbb{W}^t_x$ the [[Def - Brownian Motion on a Riemannian Manifold|Wiener measure]] (law of Brownian motion from $x$) on the path space $C([0,t],X)$. For a path $\omega$, its endpoint is $\omega(t)\in X$.

---

# Axiom Motivation

A Brownian path from $x$ over time $t$ ends *somewhere*; the endpoint $\omega(t)$ is random, with density $p(t,x,\cdot)$. Often we want to fix the endpoint — to speak of "a Brownian path from $x$ that ends exactly at $y$." That is a *conditioning*: restrict attention to paths with $\omega(t)=y$. But $\{\omega:\omega(t)=y\}$ has probability zero (the endpoint is a continuous random variable), so naïve conditioning ($\mathbb{P}(\cdot\mid\omega(t)=y)$) is $0/0$. **Disintegration** is the measure-theoretic tool that makes this rigorous: it slices the Wiener measure into a family of conditional measures indexed by the endpoint, consistently, so that integrating the slices back over all endpoints reproduces the whole.

The loop measure needs exactly the diagonal slice $y=x$: Brownian paths that start *and end* at $x$, i.e. loops. Disintegration produces these as the **bridge measure** $\mathbb{W}^t_{x\to y}$, and reading off its total mass recovers the heat kernel — a small fact that turns every mass computation in the paper into a heat-kernel integral.

---

# The Definition

> **Definition (disintegration of the Wiener measure; bridge measure).** The **disintegration** of $\mathbb{W}^t_x$ with respect to the endpoint map $\omega\mapsto\omega(t)$ is a family of measures $\{\mathbb{W}^t_{x\to y}\}_{y\in X}$ on path space, each concentrated on paths with $\omega(t)=y$, such that
> $$\mathbb{W}^t_x \;=\; \int_X \mathbb{W}^t_{x\to y}\, d\operatorname{vol}_g(y).$$
> Here $\mathbb{W}^t_{x\to y}$ is the **(unnormalised) bridge measure** from $x$ to $y$ in time $t$. It is *not* a probability measure; its **total mass is the heat kernel**,
> $$\big|\mathbb{W}^t_{x\to y}\big| \;=\; p(t,x,y),$$
> and the normalised measure $\mathbb{W}^t_{x\to y}/p(t,x,y)$ is the genuine conditional law of the Brownian path given $\omega(t)=y$ (the **Brownian bridge**).

**Concrete unpacking.** The identity $\mathbb{W}^t_x=\int_X\mathbb{W}^t_{x\to y}\,d\operatorname{vol}_g(y)$ says: to sample a Brownian path from $x$, first sample its endpoint $y$ with density $p(t,x,y)$, then sample the path given that endpoint. Evaluated on the event $\{\omega(t)\in A\}$ it reads $\mathbb{P}_x(\omega(t)\in A)=\int_A p(t,x,y)\,d\operatorname{vol}_g(y)$ — the transition density again, now derived from the slicing. Taking $y=x$ gives loops; the mass $p(t,x,x)$ of the point-to-itself bridge is the diagonal heat kernel that drives the loop measure.

**Standard names.** This is the **disintegration theorem** (a.k.a. regular conditional distributions / the existence of conditional measures); $\mathbb{W}^t_{x\to y}$ is the **(unnormalised) Brownian bridge measure** or **pinned Wiener measure**.

---

# Examples and Non-Examples

**Is an instance.** On $\mathbb{R}$, the Brownian bridge from $x$ to $y$ over $[0,t]$ is the Gaussian process $\omega(s)=x+\frac{s}{t}(y-x)+(\text{a pinned Gaussian fluctuation})$; its total mass as an unnormalised measure is $p(t,x,y)=\frac{1}{\sqrt{4\pi t}}e^{-(x-y)^2/4t}$.

**Is NOT an instance.** Plain restriction of $\mathbb{W}^t_x$ to $\{\omega(t)=y\}$ is **not** the bridge measure — that set is null, so the restriction is the zero measure. Disintegration is genuinely more than restriction: it extracts a nonzero conditional slice from a null event.

**Calibration check.** (1) Integrate $|\mathbb{W}^t_{x\to y}|=p(t,x,y)$ over $y$ and recover $|\mathbb{W}^t_x|=\int_X p(t,x,y)\,d\operatorname{vol}_g(y)\ (\le1)$. (2) Explain why dividing by $p(t,x,y)$ is legitimate exactly where $p>0$ (everywhere, since the heat kernel is strictly positive). (3) State the $y=x$ specialisation and its mass.

---

# Where the paper uses this

The bridge measure $\mathbb{W}^t_{x\to y}$ and the disintegration $\mathbb{W}^t_x=\int_X\mathbb{W}^t_{x\to y}\,d\operatorname{vol}_g(y)$ are quoted verbatim in §2.1 and are the definition-level ingredient of the [[Def - Brownian Loop Measure|Brownian loop measure]] $\mu^*_X=\int_0^\infty\frac{dt}{t}\int_X \mathbb{W}^t_{x\to x}\,d\operatorname{vol}_g(x)$. The mass identity $|\mathbb{W}^t_{x\to y}|=p(t,x,y)$ converts every loop-mass into a heat-kernel integral. **[[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2]]**.

---

# Verified against

Kallenberg, *Foundations of Modern Probability*, Ch. 6 (disintegration / regular conditional distributions); Chung–Walsh or Revuz–Yor, *Continuous Martingales and Brownian Motion*, for the pinned/bridge Wiener measure and $|\mathbb{W}^t_{x\to y}|=p(t,x,y)$. Standard.

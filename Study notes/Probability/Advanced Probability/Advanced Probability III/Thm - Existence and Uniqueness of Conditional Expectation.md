---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Conditional Expectation"
  - "Thm - Radon-Nikodym Theorem"
  - "Thm - Completeness of Lp Spaces"
tags: [probability, advanced-probability]
---

# Notation

$(\Omega,\mathcal{F},\mathbb{P})$ a probability space, $\mathcal{G}\subseteq\mathcal{F}$ a sub-$\sigma$-algebra, $X\in L^1$.

---

# Motivation

[[Def - Conditional Expectation|Conditional expectation]] was *defined by a characterisation* — a $\mathcal{G}$-measurable variable with the same $\mathcal{G}$-integrals as $X$ — not by a formula. For the definition to be legitimate, such a variable must *exist*, and (so the notation $\mathbb{E}[X\mid\mathcal{G}]$ is meaningful) be *unique*. This theorem supplies both. There are two standard constructions, each illuminating: one via [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] (conditional expectation as a density), one via [[Thm - Conditional Expectation as L2 Projection|L² projection]] (conditional expectation as a best approximation).

---

# Sources and Targets

**Sources.** Hypothesis: $X\in L^1$, $\mathcal{G}$ a sub-$\sigma$-algebra. The two routes differ in what they need: the **Radon–Nikodym** route handles $X\in L^1$ directly (split $X=X^+-X^-$); the **projection** route handles $X\in L^2$ first, then extends to $L^1$ by approximation/monotone limits.

**Targets.** Existence makes $\mathbb{E}[X\mid\mathcal{G}]$ a legitimate object; uniqueness makes "$\mathbb{E}[X\mid\mathcal{G}]$" a well-defined notation. Both feed every property of conditional expectation and the entire [[Advanced Probability IV — Martingales in Discrete Time|martingale]] theory.

---

# Statement

For every $X\in L^1(\Omega,\mathcal{F},\mathbb{P})$ and every sub-$\sigma$-algebra $\mathcal{G}\subseteq\mathcal{F}$, there exists a random variable $Y$ that is **$\mathcal{G}$-measurable**, **integrable**, and satisfies $\mathbb{E}[Y\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$ for all $A\in\mathcal{G}$. Moreover $Y$ is **unique up to $\mathbb{P}$-almost-sure equality**: any two such variables agree a.s. We write $Y=\mathbb{E}[X\mid\mathcal{G}]$.

---

# Why Is It True

**Uniqueness.** Suppose $Y_1,Y_2$ both satisfy the characterisation. Then $\mathbb{E}[(Y_1-Y_2)\mathbf{1}_A]=0$ for every $A\in\mathcal{G}$. The variable $Y_1-Y_2$ is $\mathcal{G}$-measurable, so take $A=\{Y_1-Y_2>0\}\in\mathcal{G}$: $\mathbb{E}[(Y_1-Y_2)\mathbf{1}_A]=0$ with a *non-negative* integrand forces $(Y_1-Y_2)\mathbf{1}_A=0$ a.s., i.e. $\mathbb{P}(Y_1>Y_2)=0$. Symmetrically $\mathbb{P}(Y_1<Y_2)=0$. So $Y_1=Y_2$ a.s. Uniqueness is "an integral that vanishes on every $\mathcal{G}$-set, of a $\mathcal{G}$-measurable function, forces the function to be $0$."

**Existence — Radon–Nikodym route.** First $X\ge0$. The set function $\nu(A)=\int_A X\,d\mathbb{P}$, for $A\in\mathcal{G}$, is a finite measure on $(\Omega,\mathcal{G})$, and $\nu\ll\mathbb{P}|_\mathcal{G}$ (if $\mathbb{P}(A)=0$ then $X\mathbf{1}_A=0$ a.s., so $\nu(A)=0$). Both measures are finite, hence $\sigma$-finite, so the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]] *on the space $(\Omega,\mathcal{G})$* yields a $\mathcal{G}$-measurable density $Y=\mathrm{d}\nu/\mathrm{d}(\mathbb{P}|_\mathcal{G})\ge0$ with $\int_A Y\,d\mathbb{P}=\nu(A)=\int_A X\,d\mathbb{P}$ for $A\in\mathcal{G}$ — exactly the characterisation. For general $X\in L^1$, apply this to $X^+,X^-$ and subtract. **Conditional expectation is the Radon–Nikodym derivative of $X\,d\mathbb{P}$ restricted to $\mathcal{G}$** — and applying Radon–Nikodym *on $\mathcal{G}$* is what forces $Y$ to be $\mathcal{G}$-measurable.

**Existence — projection route.** First $X\in L^2$. The space $L^2(\Omega,\mathcal{G},\mathbb{P})$ is a *closed* subspace of the Hilbert space $L^2(\Omega,\mathcal{F},\mathbb{P})$ (closed because [[Thm - Completeness of Lp Spaces|L² is complete]] and $\mathcal{G}$-measurability survives $L^2$-limits). Let $Y$ be the [[Ex - The Cauchy-Schwarz inequality and L2 geometry|orthogonal projection]] of $X$ onto it: $Y$ is $\mathcal{G}$-measurable, and $X-Y\perp L^2(\mathcal{G})$, i.e. $\mathbb{E}[(X-Y)Z]=0$ for all $Z\in L^2(\mathcal{G})$ — taking $Z=\mathbf{1}_A$ gives the averaging identity. Extend to $X\in L^1$: for $X\ge0$, truncate $X_n=X\wedge n\in L^2$, project to get $Y_n$ (increasing, by a comparison argument), let $Y=\lim Y_n$ (monotone limit, $\mathcal{G}$-measurable); the averaging identity passes through by [[Thm - Monotone Convergence Theorem|MCT]].

---

# What Makes This Hard

The conceptual hurdle is that conditional expectation is *not constructed by a formula* — it is extracted from an *existence theorem* (Radon–Nikodym, or the projection theorem), which is why it works for probability-zero conditioning. The key recognition in the Radon–Nikodym route: apply the theorem *on the sub-$\sigma$-algebra $\mathcal{G}$*, not on $\mathcal{F}$ — that placement is what makes the density $\mathcal{G}$-measurable. In the projection route, the subtle point is that $L^2(\mathcal{G})$ is *closed* (needs completeness), and the extension from $L^2$ to $L^1$ needs a monotone-limit argument with its own small comparison lemma.

---

# Rederivation Scaffold

**High-level strategy.** Uniqueness: a $\mathcal{G}$-measurable function whose $\mathcal{G}$-integrals all vanish is $0$ a.s. Existence: either Radon–Nikodym on $(\Omega,\mathcal{G})$ for the measure $X\,d\mathbb{P}$, or $L^2$-projection onto $L^2(\mathcal{G})$ then a monotone extension to $L^1$.

**Subgoal decomposition.**

1. **Uniqueness.** $\mathbb{E}[(Y_1-Y_2)\mathbf{1}_A]=0\ \forall A\in\mathcal{G}$; take $A=\{Y_1>Y_2\}\in\mathcal{G}$; non-negative integrand $\Rightarrow Y_1\le Y_2$ a.s.; symmetrise.
2. **Existence, $X\ge0$.** $\nu(A)=\int_A X\,d\mathbb{P}$ on $\mathcal{G}$ is finite, $\ll\mathbb{P}|_\mathcal{G}$; [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] on $(\Omega,\mathcal{G})$ gives the $\mathcal{G}$-measurable density $Y$.
3. **General $X$.** Split $X=X^+-X^-$, subtract.

---

# Lemma Decomposition

> [!note]- Lemma 1: Uniqueness
> **Statement:** If $Y_1,Y_2$ are $\mathcal{G}$-measurable, integrable, with $\mathbb{E}[Y_i\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$ for all $A\in\mathcal{G}$, then $Y_1=Y_2$ a.s.
>
> > [!note]- Full proof
> > $D=Y_1-Y_2$ is $\mathcal{G}$-measurable with $\mathbb{E}[D\mathbf{1}_A]=0$ for all $A\in\mathcal{G}$. The set $A_+=\{D>0\}\in\mathcal{G}$, so $\mathbb{E}[D\mathbf{1}_{A_+}]=0$; the integrand $D\mathbf{1}_{A_+}\ge0$, so $D\mathbf{1}_{A_+}=0$ a.s., i.e. $\mathbb{P}(D>0)=0$. Likewise $\mathbb{P}(D<0)=0$ via $A_-=\{D<0\}$. So $D=0$ a.s. $\square$

> [!note]- Lemma 2: Existence via Radon–Nikodym
> **Statement:** For $X\ge0$ in $L^1$, a $\mathcal{G}$-measurable $Y\ge0$ with $\int_A Y\,d\mathbb{P}=\int_A X\,d\mathbb{P}$ ($A\in\mathcal{G}$) exists.
>
> > [!note]- Full proof
> > $\nu(A)=\int_A X\,d\mathbb{P}$ for $A\in\mathcal{G}$ is a measure on $(\Omega,\mathcal{G})$ ($\sigma$-additivity by [[Thm - Monotone Convergence Theorem|MCT]]), finite ($\nu(\Omega)=\mathbb{E}X<\infty$). If $A\in\mathcal{G}$, $\mathbb{P}(A)=0$, then $X\mathbf{1}_A=0$ a.s., so $\nu(A)=0$: $\nu\ll\mathbb{P}|_\mathcal{G}$. Both finite, so $\sigma$-finite; the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]] on $(\Omega,\mathcal{G})$ produces a $\mathcal{G}$-measurable density $Y\ge0$ with $\int_A Y\,d\mathbb{P}=\nu(A)$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Uniqueness is Lemma 1. Existence: Lemma 2 for $X\ge0$; for general $X\in L^1$ apply Lemma 2 to $X^+,X^-$ obtaining $\mathcal{G}$-measurable $Y^\pm$ and set $Y=Y^+-Y^-$, which is $\mathcal{G}$-measurable, integrable ($\mathbb{E}|Y|\le\mathbb{E}Y^++\mathbb{E}Y^-=\mathbb{E}|X|$), and satisfies the averaging identity by linearity. (Alternatively, the [[Thm - Conditional Expectation as L2 Projection|L²-projection construction]] followed by monotone extension to $L^1$.) $\blacksquare$

---

# Cross-Field Exercise Suggestions

The same Radon–Nikodym-on-a-sub-$\sigma$-algebra construction, iterated along a [[Def - Filtration|filtration]], builds [[Def - Martingale|martingales]]; the projection construction realises conditional expectation as the best $L^2$-predictor — the foundation of *regression* and the *Kalman filter* in statistics and control.

---

# Bridges

- **[[Thm - Radon-Nikodym Theorem]]** — conditional expectation is a Radon–Nikodym derivative on $\mathcal{G}$; this is one of the two constructions.
- **[[Thm - Conditional Expectation as L2 Projection]]** — the other construction; conditional expectation as orthogonal projection.
- **[[Thm - Properties of Conditional Expectation]]** — every property is proved from this characterisation by the uniqueness lemma.

---
type: definition
subject: measure-theory
prereqs:
  - "Def - The Integral"
  - "Def - Almost Everywhere"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space; $1\le p\le\infty$. $\|f\|_p$ — the $L^p$ norm; $L^p(\mu)$ — the $L^p$ space. Conjugate exponents: $\tfrac1p+\tfrac1q=1$.

---

# Axiom Motivation

Analysis wants to treat functions as *points in a vector space* — to add them, scale them, measure distances, take limits — and it wants that space to be **complete**, so that Cauchy sequences converge and fixed-point and approximation arguments run. The $L^p$ spaces are the measure-theoretic answer.

The size of a function is measured by $\|f\|_p=(\int|f|^p\,d\mu)^{1/p}$ — a $p$-averaged magnitude. Different $p$ weight differently: $p=1$ is total mass, $p=2$ is the energy/Hilbert-space norm, $p=\infty$ is the essential supremum (the sup ignoring null sets). One demands $\|f\|_p<\infty$ to stay in the space.

Two design problems and their resolutions. *First*, $\|\cdot\|_p$ is not quite a norm: $\|f\|_p=0$ only forces $f=0$ **[[Def - Almost Everywhere|almost everywhere]]**, not everywhere — it is a *seminorm*. The fix is to quotient: identify functions equal a.e., so $L^p(\mu)$ is a space of *equivalence classes*. This is the standard "quotient by the kernel of a seminorm" move. *Second*, is the resulting normed space complete? Yes — this is the **Riesz–Fischer theorem**, [[Thm - Completeness of Lp Spaces|completeness of Lᵖ]] — and completeness is precisely what makes $L^p$ a *Banach* space, the property that justifies the whole functional-analytic toolkit. Completeness is inherited from completeness of $\mathbb{R}$, transmitted through the [[Thm - Dominated Convergence Theorem|convergence theorems]].

The triangle inequality $\|f+g\|_p\le\|f\|_p+\|g\|_p$ ([[Thm - Hölder and Minkowski Inequalities|Minkowski]]) is not obvious for $p\neq1,\infty$ and rests on the convexity of $t\mapsto t^p$, via [[Thm - Hölder and Minkowski Inequalities|Hölder's inequality]].

---

# The Definition

Let $(X,\mathcal{A},\mu)$ be a measure space and $1\le p\le\infty$. For measurable $f:X\to[-\infty,\infty]$,
$$\|f\|_{L^p(\mu)}=\Big(\int_X|f|^p\,d\mu\Big)^{1/p}\quad(1\le p<\infty),\qquad \|f\|_{L^\infty(\mu)}=\operatorname*{ess\,sup}_X|f|=\inf\{C\ge0:|f|\le C\ \mu\text{-a.e.}\}.$$
Set $\mathcal{L}^p(\mu)=\{f:\|f\|_p<\infty\}$, a vector space. Define $f\sim g\iff f=g$ $\mu$-a.e.; this is an equivalence relation, and
$$L^p(\mu)=\mathcal{L}^p(\mu)/\!\sim$$
is the **$L^p$ space**. On $L^p(\mu)$, $\|\cdot\|_p$ is a genuine **norm** ([[Thm - Hölder and Minkowski Inequalities|Minkowski]] gives the triangle inequality), and $(L^p(\mu),\|\cdot\|_p)$ is a **complete** normed space — a **Banach space** ([[Thm - Completeness of Lp Spaces|Riesz–Fischer]]). For $p=2$ it is a **Hilbert space**, with inner product $\langle f,g\rangle=\int f\bar g\,d\mu$.

By convention one writes $f\in L^p$ for a representative, remembering $f$ is defined only up to a.e.-equality.

---

# Categorical Definition

$L^p(\mu)$ is the *completion* of the simple functions in the $\|\cdot\|_p$ seminorm, followed by the quotient that turns the seminorm into a norm — the standard "Hausdorff completion" construction. For $p=2$ it is the canonical Hilbert space: the Riesz representation theorem identifies $L^2(\mu)^*\cong L^2(\mu)$, and indeed every Hilbert space is isometric to some $L^2$.

---

# Relate to Other Fields / Compression

$L^2$ is the **Hilbert space** of square-integrable functions — the home of Fourier analysis, quantum mechanics (wavefunctions), and least-squares; its inner product makes "orthogonal projection" available, which is exactly the construction of [[Def - Conditional Expectation|conditional expectation]] for $L^2$ random variables. $L^1$ is the space of integrable functions; $L^\infty$ of essentially bounded ones. Against [[Def - Measure and Measure Space|counting measure]], $L^p$ becomes the sequence space $\ell^p$. In probability, $L^p(\Omega,\mathcal{F},\mathbb{P})$ is the space of random variables with finite $p$-th moment, and $L^p$-convergence is one of the [[Def - Modes of Convergence|modes of convergence]].

---

# Examples / Corollaries

On $([-1,1],\lambda)$, $f(x)=|x|^{-\alpha}$ lies in $L^p$ iff $\alpha p<1$ — integrability of a singularity depends on $p$. On $\mathbb{N}$ with counting measure, $L^p=\ell^p$, and $\ell^p\subseteq\ell^{p'}$ for $p\le p'$ (opposite inclusion to the finite-measure case). On a *probability* space, $\mu(X)=1$ forces $L^{p'}\subseteq L^p$ for $p\le p'$ (Jensen: higher moments control lower).

$C_c(\mathbb{R}^n)$ is dense in $L^p(\mathbb{R}^n)$ for $p<\infty$ — continuous functions approximate, the density lever for proofs.

Calibration: (i) Is $\|\cdot\|_p$ a norm on $\mathcal{L}^p$ before quotienting? No — only a seminorm ($\|f\|_p=0$ for $f=0$ a.e., $f\neq0$). (ii) Is $L^\infty$ separable? No, generally. (iii) Does $f\in L^2$ imply $f\in L^1$? Only if $\mu(X)<\infty$.

---

# Unlocked by This

> [!tip] $L^p$ convergence and uniform integrability *(from [[Advanced Probability II — Convergence and Limit Theorems|Advanced Probability]])*
> Convergence in $L^p$ norm is a [[Def - Modes of Convergence|mode of convergence]] of random variables; for $p=1$ it is governed by [[Def - Uniform Integrability|uniform integrability]] via the [[Thm - Vitali Convergence Theorem|Vitali theorem]].

> [!tip] $L^2$, orthogonal projection, conditional expectation
> The Hilbert structure of $L^2$ gives orthogonal projection onto closed subspaces; projecting onto $L^2(\mathcal{G})$ for a sub-$\sigma$-algebra $\mathcal{G}$ *is* [[Def - Conditional Expectation|conditional expectation]].

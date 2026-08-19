---
type: definition
subject: analysis
prereqs:
  - "Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure"
  - "Def - Self-Adjoint Operator"
tags: [analysis, spectral-theory, heat-kernel, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$(X,g)$ is a [[Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure|Riemannian surface]] with area measure $\operatorname{vol}_g$ and positive Laplace–Beltrami operator $\Delta_X$ (spectrum in $[0,\infty)$). $L^2(X)=L^2(X,\operatorname{vol}_g)$ is the Hilbert space of square-integrable functions $f:X\to\mathbb{C}$, with inner product $\langle f,h\rangle=\int_X f\bar h\,d\operatorname{vol}_g$. Time is $t>0$; points are $x,y\in X$.

---

# Axiom Motivation

Heat spreading out on the surface obeys the **heat equation** $\partial_t u = -\Delta_X u$ (with the paper's positive $\Delta_X$, so heat *decays*, hence the minus sign). Given an initial temperature $u(0,\cdot)=f$, we want the solution $u(t,\cdot)$ at later time. Because the equation is linear, the map $f\mapsto u(t,\cdot)$ is a linear operator; call it $P_t$. Two facts pin down its shape. First, running the flow for time $t$ then time $r$ is the same as running it for $t+r$: $P_{t+r}=P_tP_r$ — the *semigroup* law, just like $e^{a}e^{b}=e^{a+b}$. Second, since $\Delta_X$ is a positive self-adjoint operator, the spectral theorem lets us define $P_t=e^{-t\Delta_X}$ literally as a function of the operator, and this $P_t$ is self-adjoint, positivity-preserving, and contracting. So the abstract solution operator *is* the exponential of the generator.

The concrete question the paper cares about is: what is the *probability density* for heat (equivalently, for a random particle — see [[Def - Brownian Motion on a Riemannian Manifold|Brownian motion]]) starting at $x$ to be found at $y$ at time $t$? Because $P_t$ is a nice integral operator, there is a function $p(t,x,y)$ — the **heat kernel** — such that $P_t$ acts by integrating $f$ against $p(t,x,\cdot)$. That kernel is the single object the whole paper computes with: masses of loop measures are integrals of $p(t,x,y)$ over $t$ and over the surface.

---

# The Definition

> **Definition (heat semigroup).** The **heat semigroup** of $(X,g)$ is the family of operators $e^{-t\Delta_X}$ on $L^2(X)$, $t\ge 0$, defined by the [[Def - Self-Adjoint Operator|spectral]] functional calculus of the positive self-adjoint operator $\Delta_X$. It satisfies $e^{-0\cdot\Delta_X}=\mathrm{Id}$, the semigroup law $e^{-(t+r)\Delta_X}=e^{-t\Delta_X}e^{-r\Delta_X}$, is self-adjoint, and solves the heat equation: $u(t,\cdot):=e^{-t\Delta_X}f$ has $\partial_t u = -\Delta_X u$, $u(0,\cdot)=f$.

> **Definition (heat kernel).** The **heat kernel** $p_X(t,x,y)$ is the integral kernel of $e^{-t\Delta_X}$ with respect to $\operatorname{vol}_g$: the function $p_X:(0,\infty)\times X\times X\to(0,\infty)$ such that for every $f\in L^2(X)$ and $x\in X$,
> $$\big(e^{-t\Delta_X}f\big)(x) \;=\; \int_X p_X(t,x,y)\,f(y)\,d\operatorname{vol}_g(y).$$
> It is symmetric, $p_X(t,x,y)=p_X(t,y,x)$ (because $e^{-t\Delta_X}$ is self-adjoint), strictly positive, satisfies the Chapman–Kolmogorov identity $p_X(t+r,x,z)=\int_X p_X(t,x,y)p_X(r,y,z)\,d\operatorname{vol}_g(y)$ (the semigroup law written for kernels), and $\int_X p_X(t,x,y)\,d\operatorname{vol}_g(y)\le 1$ (with equality when there is no boundary/killing — it is a probability density in $y$).

**Concrete unpacking.** On flat $\mathbb{R}^2$ the heat kernel is the Gaussian $p(t,x,y)=\frac{1}{4\pi t}\,e^{-|x-y|^2/(4t)}$ (with the paper's speed-2 normalisation, generator $-\Delta$). Check the pieces: it is symmetric in $x,y$; it integrates to $1$ in $y$; as $t\downarrow0$ it concentrates at $y=x$ (an approximate identity); and on the diagonal $p(t,x,x)=\frac{1}{4\pi t}$. That last value is exactly the **short-time on-diagonal asymptotic** $p(t,x,x)\sim \frac{1}{4\pi t}$ as $t\downarrow 0$ that the paper quotes for *any* surface — locally every surface looks flat, so the leading small-$t$ behaviour is the flat one. It is why the rooted loop measure's integrand blows up like $1/t^2$ near $t=0$.

**Standard names.** $p(t,x,y)$ is the **heat kernel** (equivalently the **transition density** of Brownian motion, or the *fundamental solution* of the heat equation). $e^{-t\Delta_X}$ is the **heat semigroup**; abstractly it is a *strongly continuous contraction semigroup* whose *generator* is $-\Delta_X$.

---

# Examples and Non-Examples

**Is an instance.** On $\mathbb{R}^2$: the Gaussian above. On a compact surface with discrete spectrum $0=\lambda_0\le\lambda_1\le\cdots$ and orthonormal eigenfunctions $\varphi_k$ ($\Delta_X\varphi_k=\lambda_k\varphi_k$), the spectral theorem gives the eigenfunction expansion $p(t,x,y)=\sum_{k\ge0} e^{-t\lambda_k}\varphi_k(x)\varphi_k(y)$ — each mode decays at its own rate $e^{-t\lambda_k}$.

**Is NOT an instance.** The Gaussian $\frac{1}{4\pi t}e^{-|x-y|^2/4t}$ using the *Euclidean* distance $|x-y|$ is **not** the heat kernel on a curved surface — the correct kernel uses the geometry (e.g. on $\mathbb{H}^2$ the kernel depends on the *hyperbolic* distance and decays differently). Distance in the wrong metric gives the wrong diffusion.

**Calibration check.** (1) From $p(t,x,y)=\sum_k e^{-t\lambda_k}\varphi_k(x)\varphi_k(y)$, verify the trace identity $\int_X p(t,x,x)\,d\operatorname{vol}_g(x)=\sum_k e^{-t\lambda_k}=\operatorname{Tr}(e^{-t\Delta_X})$. (2) Check Chapman–Kolmogorov for the flat Gaussian by completing the square. (3) Confirm $p(t,x,x)\to\infty$ like $1/(4\pi t)$ as $t\downarrow0$.

---

# Where the paper uses this

$p_X(t,x,y)$ is the workhorse of the paper: the mass of every loop measure is an integral of a heat kernel over duration $t$ and position $x$. The on-diagonal asymptotic $p(t,x,x)\sim 1/(4\pi t)$ explains the divergence of the total loop mass; the trace $\int_X p(t,x,x)\,d\operatorname{vol}_g$ is what §5's zeta-regularised determinant renormalises. **[[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2]]**, and everywhere after.

---

# Verified against

Grigor'yan, *Heat Kernel and Analysis on Manifolds*, Ch. 7–9 (existence, symmetry, positivity, Chapman–Kolmogorov, short-time diagonal asymptotic $p(t,x,x)\sim(4\pi t)^{-n/2}$ for $\dim=n$, here $n=2$); flat Gaussian and eigenfunction expansion are standard. Speed-2 normalisation (generator $-\Delta$, not $-\frac12\Delta$) matches the paper's stated convention.

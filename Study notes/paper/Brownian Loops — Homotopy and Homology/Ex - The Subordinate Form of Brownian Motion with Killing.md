---
type: example
subject: probability-geometry
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Dirichlet Form and its Operator and Semigroup"
  - "Def - Hyperbolic Plane"
tags: [paper, brownian-loops, dirichlet-forms]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Example 2.6"
---

# Notation

$\mathbb{H}^2$ the upper half-plane with the hyperbolic metric $ds^2=(dx^2+dy^2)/y^2$; $\rho$ its area measure; $\Delta_{\mathbb{H}^2}$ the positive Laplace–Beltrami operator; $p_{\mathbb{H}^2}(t,z,w)$ the hyperbolic heat kernel; $\nabla$ its gradient (raised via $g^{-1}$). $\kappa>0$ the killing rate; $\phi(\lambda)=\lambda+\kappa$ the Bernstein function; $f:\mathbb{H}^2\to\mathbb{R}$ a test function in the Sobolev space $H^1(\mathbb{H}^2,\rho)$ (the domain of the Dirichlet form).

> [!recall]- The hyperbolic plane $\mathbb{H}^2$ (upper half-plane, metric $ds^2=(dx^2+dy^2)/y^2$)
> **Formally:** $\mathbb{H}^2:=\{z=x+iy\in\mathbb{C}:y>0\}$ with the Riemannian metric $ds^2=(dx^2+dy^2)/y^2$; distances shrink as $y$ grows and blow up as $y\to 0$. Area measure $\rho=dx\,dy/y^2$. Isometry group $\mathrm{PSL}(2,\mathbb{R})$, acting by Möbius $z\mapsto(az+b)/(cz+d)$, $ad-bc=1$.
> **In words:** the standard model of a 2D negatively-curved surface — the same set as the upper half-plane, but with a rescaled ruler that makes it a curved (hyperbolic) space. Geodesics are vertical lines and half-circles perpendicular to the real axis.
> **Concretely:** the distance from $z=i$ to $z=2i$ along the vertical geodesic $x=0$ equals $\int_1^2 dy/y=\log 2$; scaling $z\mapsto 2z$ is an isometry (translation length $\log 2$). See [[Def - Hyperbolic Plane]].

> [!recall]- Bernstein function $\phi(\lambda)=\lambda+\kappa$ (subordinator law $\psi^\phi_t=e^{-\kappa t}\delta_t$)
> **Formally:** the Bernstein function $\phi(\lambda)=\lambda+\kappa$ has Lévy–Khintchine data $(a,b,\nu)=(\kappa,1,0)$; the associated subordinator has law $\psi^\phi_t=e^{-\kappa t}\delta_t$ (a sub-probability measure of total mass $e^{-\kappa t}$).
> **In words:** the "killed" clock: deterministic ($S_t=t$), but with probability $e^{-\kappa t}$ of surviving to time $t$. In the survival branch the process is exactly the ambient one; in the killed branch it is dead.
> **Concretely:** at $t=1$ with $\kappa=\log 2$: the survival probability is $e^{-\log 2}=1/2$. See [[Def - Bernstein Function, Subordinator, and Subordination]] and [[Ex - The Four Bernstein Functions of the Paper]] (case 2).

> [!recall]- Dirichlet-energy form $\mathcal E(f,f)=\int|\nabla f|^2\,d\rho$ on $L^2(\mathbb{H}^2,\rho)$
> **Formally:** on the Hilbert space $L^2(\mathbb{H}^2,\rho)$, the **Dirichlet energy** is the closed symmetric non-negative bilinear form $\mathcal E(f,f):=\int_{\mathbb{H}^2}|\nabla f|^2_g\,d\rho$ on the Sobolev domain $\mathcal F=H^1(\mathbb{H}^2,\rho)$; it is a regular symmetric [[Def - Dirichlet Form and its Operator and Semigroup|Dirichlet form]] whose associated operator is $\Delta_{\mathbb{H}^2}$ and whose Markov process is [[Def - Brownian Motion on a Riemannian Manifold|hyperbolic Brownian motion]].
> **In words:** the "total steepness" of $f$, computed with the hyperbolic metric. It is the energy functional whose associated diffusion process is Brownian motion on the hyperbolic plane.
> **Concretely:** for $f(z)=y=\mathrm{Im}(z)$ on the strip $\{1\le y\le 2\}$ of unit horizontal width, $\nabla f$ has hyperbolic norm $|\nabla f|_g=y|\partial_y f|=y\cdot 1=y$; so $|\nabla f|_g^2=y^2$ and $\mathcal E(f,f)=\int_0^1\!\int_1^2 y^2\cdot y^{-2}\,dy\,dx=1$. See [[Def - Dirichlet Form and its Operator and Semigroup]].

---

# Statement

> **Example (Belyaev–Huseynli 2.6).** For $\phi(\lambda)=\lambda+\kappa$ with $\kappa>0$, the subordinate Dirichlet form on $L^2(\mathbb{H}^2,\rho)$ is
> $$\mathcal E_\kappa(f,f) \;=\; \int_{\mathbb{H}^2}|\nabla f|^2\,d\rho + \kappa\int_{\mathbb{H}^2} f^2\,d\rho,\qquad f\in H^1(\mathbb{H}^2,\rho),$$
> and its transition density is
> $$p^\kappa_{\mathbb{H}^2}(t,z,w) \;=\; e^{-\kappa t}\,p_{\mathbb{H}^2}(t,z,w).$$

---

# Computation

**Deriving the subordinate form from $\mathcal E^\phi$.** The general subordinate form is
$$\mathcal E^\phi(f,f)=a\|f\|^2+b\,\mathcal E(f,f)+\int_0^\infty\big(\|f\|^2-\langle e^{-sA}f,f\rangle\big)\,\nu(ds).$$
Substituting $(a,b,\nu)=(\kappa,1,0)$ (from $\phi(\lambda)=\lambda+\kappa$, [[Ex - The Four Bernstein Functions of the Paper|case 2]]),
$$\mathcal E_\kappa(f,f)=\kappa\|f\|^2+\mathcal E(f,f)+0=\int_{\mathbb{H}^2}|\nabla f|^2\,d\rho+\kappa\int_{\mathbb{H}^2}f^2\,d\rho.$$
The domain is unchanged: $\mathcal F^\phi=\{f\in L^2:\mathcal E^\phi(f,f)<\infty\}=H^1(\mathbb{H}^2,\rho)=\mathcal F$ (the extra $\kappa\|f\|^2$ term is finite for every $f\in L^2$, so the constraint $\mathcal E^\phi<\infty$ is the same as $\mathcal E<\infty$).

**Deriving the subordinate kernel from $p^\phi$.** The general subordinate transition density is
$$p^\phi(t,z,w)=\int_{[0,\infty)} p^E(s,z,w)\,\psi^\phi_t(ds).$$
With $\psi^\phi_t=e^{-\kappa t}\delta_t$ (case 2), the atom at $s=t$ picks out $p^E(t,z,w)=p_{\mathbb{H}^2}(t,z,w)$ (the hyperbolic heat kernel) with weight $e^{-\kappa t}$:
$$p^\kappa_{\mathbb{H}^2}(t,z,w)=e^{-\kappa t}\,p_{\mathbb{H}^2}(t,z,w).$$

**Reading the two formulas off each other.** The generator of the semigroup with kernel $p^\kappa_{\mathbb{H}^2}(t,z,w)=e^{-\kappa t}p_{\mathbb{H}^2}(t,z,w)$ is $\Delta_{\mathbb{H}^2}+\kappa$ (differentiating $e^{-t(\Delta_{\mathbb{H}^2}+\kappa)}$ at $t=0$). The Dirichlet form of $\Delta_{\mathbb{H}^2}+\kappa$ is $\langle(\Delta_{\mathbb{H}^2}+\kappa)f,f\rangle=\langle\Delta_{\mathbb{H}^2}f,f\rangle+\kappa\|f\|^2=\int|\nabla f|^2\,d\rho+\kappa\int f^2\,d\rho$ — the formula in the statement. So the two derivations are consistent.

**Sanity check: the process.** The **hyperbolic Brownian motion killed at exponential rate $\kappa$** is the process that moves as ordinary hyperbolic Brownian motion, but at each instant has an independent exponential clock $E\sim\mathrm{Exp}(\kappa)$; if $E<t$ the process is dead at time $t$, otherwise alive and located at the ordinary hyperbolic Brownian motion's position at time $t$. Its transition density is $\mathbb{P}(\text{alive at }t)\cdot p_{\mathbb{H}^2}(t,z,w)=e^{-\kappa t}p_{\mathbb{H}^2}(t,z,w)$, matching the formula. The path is continuous up until the killing time, so this is *not* a jump process — the "subordination" here is genuinely trivial in the geometric sense, changing only the survival probability, not the trajectory shape.

**Sanity check: recover the ambient case.** Setting $\kappa=0$ gives $\phi(\lambda)=\lambda$, $\mathcal E_0=\mathcal E$, and $p^0_{\mathbb{H}^2}=p_{\mathbb{H}^2}$ — as expected, the trivial-clock case (case 1) is recovered continuously.

**The loop-measure consequence.** The subordinate Brownian loop measure $\mu^\kappa_{\mathbb{H}^2}$ (see [[Def - Subordinate Brownian Loop Measure|Def. 2.8]]) has total mass
$$|\mu^\kappa_{\mathbb{H}^2}|=\int_0^\infty\frac{dt}{t}\int_{\mathbb{H}^2}p^\kappa_{\mathbb{H}^2}(t,z,z)\,d\rho(z)=\int_0^\infty\frac{e^{-\kappa t}}{t}\int_{\mathbb{H}^2}p_{\mathbb{H}^2}(t,z,z)\,d\rho(z)\,dt,$$
i.e. the ambient Brownian loop-mass integrand, exponentially damped by $e^{-\kappa t}$. The damping cures the *large-$t$* divergence (loops much longer than $1/\kappa$ are strongly suppressed) but does not touch the *small-$t$* divergence coming from the $p(t,z,z)\sim 1/(4\pi t)$ diagonal — so on the whole plane $\mathbb{H}^2$ (which has infinite area) the total is still infinite. On a compact quotient $X=\Gamma\backslash\mathbb{H}^2$, however, the small-$t$ divergence still exists, but the killing helps in the *per-homotopy-class* computations of §3 (see [[Ex - Weighted Potential Measures of the Paper's Bernstein Functions|Example 2.10(b)]]).

---

# Calibration

Setting $\kappa=0$ recovers ordinary hyperbolic Brownian motion. Sending $\kappa\to\infty$ kills the process instantly ($e^{-\kappa t}\to 0$ for every $t>0$), and $\mathcal E_\kappa(f,f)\to+\infty$ unless $f\equiv 0$ — the domain effectively collapses. The intermediate $\kappa>0$ is where the paper's shifted-Laplacian analysis of §3.1.2 and §3.1.4 lives.

**A calibration check.** Verify by direct differentiation that $u(t,z):=e^{-t(\Delta_{\mathbb{H}^2}+\kappa)}f_0(z)$ solves $\partial_t u=-(\Delta_{\mathbb{H}^2}+\kappa)u$ with $u(0)=f_0$: writing $u=e^{-\kappa t}v$ where $v:=e^{-t\Delta_{\mathbb{H}^2}}f_0$ solves the usual heat equation $\partial_t v=-\Delta_{\mathbb{H}^2}v$, we compute $\partial_t u=-\kappa e^{-\kappa t}v+e^{-\kappa t}\partial_t v=-\kappa u+e^{-\kappa t}(-\Delta_{\mathbb{H}^2}v)=-\kappa u-\Delta_{\mathbb{H}^2}u=-(\Delta_{\mathbb{H}^2}+\kappa)u$. ✓

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.3.3]] as the simplest non-trivial subordinate case. It is the "$\phi(\lambda)=\lambda+\kappa$" line in every §3 mass computation ([[Thm - Mass of a Free Homotopy Class|Theorem 3.2]]'s specialisation §3.1.2), and it is the QM digression of §3.2 (killing = mass term = Feynman–Kac potential = imaginary time Schrödinger with potential $\kappa$). It also underlies the shifted $\alpha$-stable case of §3.1.4 (see [[Ex - The Four Bernstein Functions of the Paper|Example 2.5]] case 4), where the outer $\phi=u^{\alpha/2}$ is composed *with* $u=\lambda+\kappa$ from this example.

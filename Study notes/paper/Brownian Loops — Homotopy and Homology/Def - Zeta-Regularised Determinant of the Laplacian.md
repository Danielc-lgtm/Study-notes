---
type: definition
subject: analysis
prereqs:
  - "Def - Heat Kernel and Heat Semigroup"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
tags: [analysis, spectral-geometry, zeta-functions, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$X$ a closed hyperbolic surface; $\Delta_X$ its positive [[Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure|Laplace–Beltrami operator]] with discrete spectrum $0=\lambda_0<\lambda_1\le\lambda_2\le\cdots$; $\operatorname{Tr}(e^{-t\Delta_X})=\sum_{j\ge0}e^{-t\lambda_j}$ the heat trace; $\Gamma(s)$ the Gamma function; $\zeta_R$ the Riemann zeta function; $\chi(X)=2-2g$ the Euler characteristic. $s\in\mathbb{C}$.

---

# Axiom Motivation

The "determinant of the Laplacian" $\det\Delta_X$ ought to be the product of its eigenvalues $\prod_{j\ge1}\lambda_j$ (dropping the zero mode) — a natural quantity in physics (one-loop partition functions) and geometry (analytic torsion). But that product diverges: by Weyl's law $\lambda_j\sim 4\pi j/\operatorname{Area}(X)$, so $\log\det=\sum_j\log\lambda_j$ has terms growing like $\log j$ and diverges. The eigenvalues are too many and too large. **Zeta regularisation** is the standard cure: instead of summing $\log\lambda_j$ directly, encode the eigenvalues in a **spectral zeta function** $\zeta_X(s)=\sum_j\lambda_j^{-s}$, which converges for $\operatorname{Re}s$ large, continue it analytically to $s=0$, and *define* $\log\det$ by the value of its derivative there. This is finite and canonical.

The trick that makes the continuation work — and the reason this belongs in a paper about heat/loops — is the **Mellin transform**: $\lambda^{-s}=\Gamma(s)^{-1}\int_0^\infty t^{s-1}e^{-t\lambda}\,dt$, so $\zeta_X(s)$ is a Mellin transform of the heat trace. The heat trace's *small-$t$ asymptotics* (which are local geometry — area, Euler characteristic) control the poles of $\zeta_X$, and the $1/\Gamma(s)$ factor's zero at $s=0$ makes $\zeta_X$ regular there. So $\det_\zeta\Delta$ is read off from heat-kernel data — and the heat trace $\operatorname{Tr}(e^{-t\Delta_X})=\int_X p(t,x,x)\,d\operatorname{vol}_g$ is built from Brownian loops (paths returning to their start). That is the door through which the loop measure enters: $-\log\det_\zeta\Delta$ is a regularised total loop mass.

---

# The Definition

> **Definition (spectral zeta function; zeta-regularised determinant).** For a closed hyperbolic surface $X$, the **spectral zeta function** is
> $$\zeta_X(s):=\sum_{j=1}^\infty\lambda_j^{-s}=\frac{1}{\Gamma(s)}\int_0^\infty t^{s-1}\big(\operatorname{Tr}(e^{-t\Delta_X})-1\big)\,dt,\qquad\operatorname{Re}(s)>1,$$
> where the "$-1$" removes the zero eigenvalue ($\dim\ker\Delta_X=1$, the constants). Using the short-time heat-trace asymptotic $\operatorname{Tr}(e^{-t\Delta_X})-1\sim\frac{\operatorname{Area}(X)}{4\pi t}+\big(\frac{\chi(X)}{6}-1\big)+O(t)$ as $t\downarrow0$, $\zeta_X$ continues meromorphically to $\mathbb{C}$, is **analytic at $s=0$** (the $1/\Gamma(s)$ zero cancels the potential pole), with $\zeta_X(0)=\frac{\chi(X)}{6}-1$. The **zeta-regularised determinant** is
> $$\log\det_\zeta\Delta_X:=-\zeta_X'(0),$$
> the Ray–Singer definition (formally $-\zeta_X'(0)=\sum_{j\ge1}\log\lambda_j$, since $\frac{d}{ds}\lambda^{-s}\big|_{s=0}=-\log\lambda$).

> **Definition (renormalised determinant, cusped case — sketch).** When $X$ is non-compact of finite area, $\Delta_X$ has continuous spectrum $[\frac14,\infty)$ (Eisenstein series) and $e^{-t\Delta_X}$ is **not trace-class**. One replaces the divergent $\int_X p(t,z,z)\,d\operatorname{vol}_g$ by a **renormalised ($0$-)trace** ${}^{0}\!\operatorname{Tr}(e^{-t\Delta_X})={}^{0}\!\int_X p(t,z,z)\,d\operatorname{vol}_g$ (Hadamard/Riesz finite part, cutting the cusps and dropping the divergence), forms $\zeta^0_X(s)=\Gamma(s)^{-1}\int_0^\infty t^{s-1}({}^{0}\!\operatorname{Tr}(e^{-t\Delta_X})-P)\,dt$ (with $P$ the $L^2$-null projection), and sets ${\det}_0\Delta_X:=e^{-(\zeta^0_X)'(0)}$. On a closed surface this reduces to $\det_\zeta\Delta_X$.

**Concrete unpacking (the mechanism, in one line).** For a single positive number $\lambda$, "$\zeta(s)=\lambda^{-s}$, $-\zeta'(0)=\log\lambda$" recovers $\log\lambda$; zeta regularisation just does this for all eigenvalues at once, using analytic continuation to make the infinite product sensible. The output $\det_\zeta\Delta_X$ is a single positive real number attached to the surface.

**Standard names.** **Spectral (Minakshisundaram–Pleijel) zeta function**, **zeta-regularised / Ray–Singer determinant**, **heat trace**, **Weyl's law**; the cusped-surface version is the **relative / $0$-determinant** (Müller; Borthwick–Judge–Perry). Reference: Ray–Singer, *R-torsion and the Laplacian*; for surfaces, Sarnak, *Determinants of Laplacians*.

---

# Examples and Non-Examples

**Is an instance.** On a closed hyperbolic surface, $\det_\zeta\Delta_X$ is the D'Hoker–Phong / Sarnak quantity, equal to $Z_X'(1)\,e^{(2g-2)(2\zeta_R'(-1)-1/4+\frac12\log2\pi)}$ (a Selberg-zeta derivative times a universal constant). On the round $S^2$, $\det_\zeta\Delta$ is a known constant ($\exp(\frac12-4\zeta_R'(-1))$).

**Is NOT an instance.** The naive product $\prod_{j\ge1}\lambda_j$ is **not** the zeta-regularised determinant — it diverges. Nor is $\exp(\sum_{j\le N}\log\lambda_j)$ for a hard cutoff $N$ a canonical answer; it depends on $N$ and the geometry of the truncation, whereas zeta regularisation is cutoff-independent.

**Calibration check.** (1) Verify $\lambda^{-s}=\Gamma(s)^{-1}\int_0^\infty t^{s-1}e^{-t\lambda}\,dt$ (definition of $\Gamma$ after $t\mapsto t/\lambda$). (2) From the $t\downarrow0$ heat-trace asymptotic, locate the pole of $\zeta_X$ at $s=1$ (from the $1/t$ term) and confirm analyticity at $s=0$. (3) Check $\frac{d}{ds}\lambda_j^{-s}\big|_{s=0}=-\log\lambda_j$, motivating $-\zeta_X'(0)=\sum\log\lambda_j$.

---

# Where the paper uses this

§5 renormalises the (infinite, for finite-area $X$) total Brownian loop mass by expressing $\log\det_\zeta\Delta_X$ through it: Theorem 5.1 (compact) and Theorem 5.7 (finite-area) write $-\log\det_\zeta\Delta_X$ (resp. $-\log{\det}_0(\Delta_X+\kappa)$) as a length-spectrum sum $=$ loop mass, cancelling the divergence against the Selberg zeta's zero at $s=1$ in the $\kappa\to0$ limit. This finite determinant is the normalising constant of §6's probability measure. **[[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]]**.

---

# Verified against

Ray–Singer, *R-torsion and the Laplacian on Riemannian manifolds* (Adv. Math. 1971) for $\log\det_\zeta=-\zeta'(0)$; Sarnak, *Determinants of Laplacians* (Comm. Math. Phys. 1987) and D'Hoker–Phong, *On determinants of Laplacians on Riemann surfaces* for the closed hyperbolic case $\det_\zeta\Delta=Z_X'(1)\,e^{\cdots}$; Borthwick–Judge–Perry, *Selberg zeta functions and relative determinants* for the cusped $0$-determinant. Heat-trace asymptotic $\operatorname{Tr}(e^{-t\Delta})\sim\frac{\operatorname{Area}}{4\pi t}+\frac{\chi}{6}+\cdots$ standard (Minakshisundaram–Pleijel; McKean–Singer). Matches the paper's §5.

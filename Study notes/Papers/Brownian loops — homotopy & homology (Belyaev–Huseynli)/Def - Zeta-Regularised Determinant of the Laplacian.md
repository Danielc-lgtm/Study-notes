---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Schwinger Proper-Time Representation"
  - "Def - Euler Characteristic"
tags: [paper, spectral-geometry, determinants]
---

# Notation

- $0=\lambda_0<\lambda_1\leq\lambda_2\leq\cdots$ — the eigenvalues of $\Delta_X$ on a **closed** hyperbolic surface, with multiplicity; $\lambda_0$ simple, with constant eigenfunctions
- $\zeta_X(s)=\sum_{j\geq1}\lambda_j^{-s}$ — the spectral zeta function, the zero eigenvalue excluded
- $\log\det_\zeta\Delta_X := -\zeta'_X(0)$ — the zeta-regularised determinant
- $\Gamma(s)$ — the Gamma function; $\chi(X)$ the Euler characteristic; $\mathrm{Area}(X)$ the area
- $\operatorname{Tr}(e^{-t\Delta_X})=\sum_{j\geq0}e^{-t\lambda_j}$ — the heat trace
- $\Delta^{\alpha/2}$ — the spectral fractional Laplacian, with eigenvalues $\lambda_j^{\alpha/2}$

---

# In plain language

The determinant of an operator with infinitely many eigenvalues is naively $\prod_j\lambda_j$, and on a closed hyperbolic surface that diverges: Weyl's law gives $\lambda_j\sim4\pi j/\mathrm{Area}(X)$, so $\log\det\Delta_X \stackrel{!}{=}\sum_{j\geq1}\log\lambda_j$ diverges badly.

Ray and Singer's device, from their work on analytic torsion, is to define the determinant through a **zeta function** instead. Form $\zeta_X(s)=\sum_{j\geq1}\lambda_j^{-s}$, which converges for $\operatorname{Re}(s)>1$; then formally $-\zeta'_X(0)=\sum_{j\geq1}\log\lambda_j$, since differentiating $\lambda^{-s}$ in $s$ gives $-\log\lambda\cdot\lambda^{-s}$ and setting $s=0$ leaves $-\log\lambda$. So **define** $\log\det_\zeta\Delta_X:=-\zeta'_X(0)$, provided $\zeta_X$ can be continued to be regular at $0$.

It can, and the mechanism is worth understanding because it is the same mechanism that renormalises the loop mass. Via the Mellin transform, $\lambda_j^{-s}=\Gamma(s)^{-1}\int_0^\infty t^{s-1}e^{-t\lambda_j}\,\mathrm{d}t$; summing over $j\geq1$,
$$\zeta_X(s) = \frac{1}{\Gamma(s)}\int_0^\infty t^{s-1}\big(\operatorname{Tr}(e^{-t\Delta_X})-1\big)\,\mathrm{d}t,$$
the $1$ subtracted being $\dim\ker\Delta_X$, to drop $\lambda_0=0$. **This is the [[Def - Schwinger Proper-Time Representation|Schwinger proper-time integral]] with $t^{s-1}$ in place of $t^{-1}$** — the regularisation is exactly the insertion of the extra power $t^s$, and the continuation in $s$ is what tames the divergence at $t=0$.

The pole structure then follows from the short-time heat-trace expansion. As $t\downarrow0$,
$$\operatorname{Tr}(e^{-t\Delta_X})-1 \sim \frac{\mathrm{Area}(X)}{4\pi t} + \Big(\frac{\chi(X)}{6}-1\Big) + O(t),$$
and the two visible terms do different things. The $t^{-1}$ term produces a **simple pole of $\zeta_X$ at $s=1$**. The constant term would produce a pole at $s=0$, but the simple **zero of $1/\Gamma(s)$ there cancels it** — so $\zeta_X$ is analytic at $0$, with $\zeta_X(0)=\chi(X)/6-1$, and $\zeta'_X(0)$ is well defined. That cancellation is what makes the whole definition work.

---

# The definition

> **Definition (spectral zeta function and the zeta-regularised determinant).** On a closed hyperbolic surface, where $\Delta_X$ has discrete spectrum $0=\lambda_0<\lambda_1\leq\lambda_2\leq\cdots$ with $\lambda_j\sim4\pi j/\mathrm{Area}(X)$ by Weyl's law, define
> $$\zeta_X(s):=\sum_{j=1}^\infty\frac{1}{\lambda_j^s},\qquad\operatorname{Re}(s)>1,$$
> excluding the zero eigenvalue. Using the identity $-\zeta'_X(0)=\sum_{j\geq1}\log\lambda_j$ formally, set
> $$\log\det{}_\zeta\Delta_X := -\zeta'_X(0).$$

> **Meromorphic continuation.** Via the Mellin transform, $\lambda_j^{-s}=\Gamma(s)^{-1}\int_0^\infty t^{s-1}e^{-t\lambda_j}\,\mathrm{d}t$, and summing over $j\geq1$,
> $$\zeta_X(s) = \frac{1}{\Gamma(s)}\int_0^\infty t^{s-1}\sum_{j\geq1}e^{-t\lambda_j}\,\mathrm{d}t = \frac{1}{\Gamma(s)}\int_0^\infty t^{s-1}\big(\operatorname{Tr}(e^{-t\Delta_X})-1\big)\,\mathrm{d}t.$$
> As $t\downarrow0$,
> $$\operatorname{Tr}(e^{-t\Delta_X})-1 \sim \frac{\mathrm{Area}(X)}{4\pi t}+\Big(\frac{\chi(X)}{6}-1\Big)+O(t),$$
> which determines the behaviour near $t=0$: the $t^{-1}$ term produces a simple pole of $\zeta_X$ at $s=1$, and $\zeta_X$ continues meromorphically to $\mathbb{C}$. The constant term would give a pole at $s=0$, but the simple zero of $1/\Gamma(s)$ there cancels it, so $\zeta_X$ is analytic at $s=0$ with $\zeta_X(0)=\chi(X)/6-1$, and $\zeta'_X(0)$ is well defined.

> **The fractional case.** $\det_\zeta\Delta^{\alpha/2}$ is defined as above with $\lambda_j$ replaced by $\lambda_j^{\alpha/2}$. Since $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$, the chain rule gives $\log\det_\zeta\Delta^{\alpha/2}=(\alpha/2)\log\det_\zeta\Delta$ — which is why part (iii) of [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]] is one line.

---

# Types and signatures

- $\zeta_X : \{\operatorname{Re}(s)>1\}\to\mathbb{C}$ initially, continued meromorphically to $\mathbb{C}$ with a **single** simple pole at $s=1$; analytic at $s=0$
- $\zeta_X(0)=\chi(X)/6-1$ — a rational number determined by topology alone
- $\log\det_\zeta\Delta_X=-\zeta'_X(0)$ — a real number; **not** a product of anything, despite the name
- $\det_\zeta$ excludes $\lambda_0=0$ by construction; on a surface where $0$ is not an eigenvalue the exclusion is vacuous
- the definition requires **discrete spectrum and trace-class $e^{-t\Delta_X}$** — both fail in the non-compact case, which is why [[Def - Renormalised Integral and the 0-Trace|$\det_0$]] is needed there

---

# Example

The value the paper computes. By [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1(ii)]], on a closed hyperbolic surface,
$$\log\det{}_\zeta\Delta = \mathrm{Area}(X)\,E + \log Z'_X(1),\qquad E=\frac{4\zeta'_{\mathbb{R}}(-1)-\tfrac12+\log(2\pi)}{4\pi}\approx0.0538,$$
which with $\mathrm{Area}(X)=4\pi(g-1)$ from Gauss–Bonnet is the classical D'Hoker–Phong formula
$$\det{}_\zeta\Delta = Z'_X(1)\,e^{(2g-2)\left(2\zeta'_{\mathbb{R}}(-1)-\frac14+\frac12\log2\pi\right)}.$$
Note that the answer contains $Z'_X(1)$, the *derivative* — because $\lambda_0=0$ is in the spectrum, [[Def - Selberg Zeta Function|$Z_X$]] has a simple zero at $s=1$, and excluding $\lambda_0$ from $\det_\zeta$ corresponds to dividing that zero out.

**Near-miss non-example — the naive determinant.** $\prod_{j\geq1}\lambda_j$ diverges, and so does $\int_0^\infty\frac{\mathrm{d}t}{t}(\operatorname{Tr}(e^{-t\Delta_X})-1)$, at $t=0$ like $\int_0\mathrm{Area}(X)/(4\pi t^2)\,\mathrm{d}t$. **These are the same divergence seen from the two sides of the Mellin transform**, which is exactly why inserting $t^s$ cures both at once. And it is why §5's renormalisation of the loop mass is *forced* rather than chosen: the divergent part of the total mass is the pole of $\zeta_X$, and there is only one way to subtract a pole.

**Second near-miss — the non-compact case.** On a finite-area cusped surface the spectrum is not discrete: alongside the $L^2$ eigenvalues there is continuous spectrum filling $[\tfrac14,\infty)$ with multiplicity the number of cusps, so $\sum_j\lambda_j^{-s}$ has no meaning and $e^{-t\Delta_X}$ is not trace class. The definition above simply does not parse, and §5.2 replaces it with [[Def - Renormalised Integral and the 0-Trace|the $0$-trace and $\det_0$]]. On a closed surface the $0$-trace is the ordinary trace and $\det_0$ reduces to $\det_\zeta$.

---

# Used in this paper at

- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]] — the object computed, in all three parts
- [[Thm - Polyakov's Conformal Anomaly Formula|Theorem 5.3]] and [[Thm - Polyakov's Formula via Brownian Loop Measure|Corollary 5.4]] — the transformation law under conformal rescaling
- [[Def - Renormalised Integral and the 0-Trace]] — $\det_0$ is the non-compact replacement, reducing to $\det_\zeta$ on a closed surface
- [[Def - Schwinger Proper-Time Representation]] — the formal identity that $\det_\zeta$ makes rigorous
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] — the section's central object

---

# Where this sits in my DAG

Mostly anchors, plus one quoted input. The spectral side — discrete spectrum of the Laplacian on a closed manifold, Weyl's law, trace-class heat semigroups — is *Analysis of PDEs* (🟢) and *Functional Analysis* (🟢); see [[Def - Self-Adjoint Operator]] and [[Thm - Complex Spectral Theorem]]. The Mellin transform and the pole structure of $\Gamma$ are classical analysis. The Euler characteristic is [[Def - Euler Characteristic]] and Gauss–Bonnet is [[Thm - Gauss-Bonnet Theorem for Surfaces]].

**The short-time heat-trace expansion** $\operatorname{Tr}(e^{-t\Delta_X})\sim\frac{\mathrm{Area}(X)}{4\pi t}+\frac{\chi(X)}{6}+O(t)$ is quoted. It is standard heat-kernel asymptotics — the first coefficient is the volume, the second is the integrated scalar curvature over $12\pi$, which by Gauss–Bonnet is $\chi(X)/6$ — and it is the reason $\zeta_X(0)$ is a topological invariant.

Ray and Singer's original context was analytic torsion; the definition's spread into theoretical physics was catalysed by Polyakov's work on the quantum geometry of bosonic strings, which is where the conformal anomaly of [[Thm - Polyakov's Conformal Anomaly Formula|§5.1.1]] comes from.

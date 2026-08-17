---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Renormalised Integral and the 0-Trace"
  - "Def - Selberg Zeta Function"
tags: [paper, spectral-geometry, determinants]
---

# Notation

- $X$ — a geometrically finite hyperbolic surface with $n_C$ cusps and Euler characteristic $\chi=\chi(X)$
- $R_X(s)=(\Delta_X-s(1-s))^{-1}$ — the resolvent; ${}^0\mathrm{Tr}$ the [[Def - Renormalised Integral and the 0-Trace|renormalised trace]]
- $\det_0$ — the renormalised determinant; $Z_X$ the [[Def - Selberg Zeta Function|Selberg zeta function]]
- $G(s)$ — the Barnes $G$-function; $G_\infty(s)=(2\pi)^{-s}\Gamma(s)G(s)^2$
- $M=\chi(X)\big(\tfrac12\log2\pi-2\zeta'_{\mathbb{R}}(-1)+\tfrac14\big)$, $F=-\chi(X)$ — the two constants fixed by integration
- $\zeta_{\mathbb{R}}$ — the Riemann zeta function
- $C_X=e^M(2\pi)^{-\chi(X)}\big(\sqrt{2\pi}\big)^{-n_C}$
- $D_X(s)$ — the correction term of (66)

---

# Type card

> [!abstract] Type card — Theorem 5.5 (Borthwick–Judge–Perry)
> **Given.** A geometrically finite hyperbolic surface $X$ with $n_C$ cusps and Euler characteristic $\chi$; the [[Def - Renormalised Integral and the 0-Trace|renormalised determinant]] $\det_0$; and the resolvent $R_X(s)=(\Delta_X-s(1-s))^{-1}$ with its renormalised trace.
>
> **Produces.** An explicit factorisation of $\det_0(\Delta_X-s(1-s))$ as $Z_X(s)$ times elementary factors — a Gaussian-type exponential $e^{M+Fs(1-s)}$, a power of the Barnes-$G$-built $G_\infty(s)$, and a cusp-dependent Gamma factor. And, as a consequence, $\det_0\Delta_X$ in terms of $Z'_X(1)$ or $Z_X(1)$ according as the area is finite or infinite.
>
> **Lets you.** Convert every $\det_0$ statement into a $Z_X$ statement, which [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] then converts into a loop-mass statement. This is the bridge that makes [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] a substitution rather than a computation.

---

# Statement

> **Theorem 5.5 (Borthwick–Judge–Perry).** Let $X$ be a geometrically finite hyperbolic surface with $n_C$ cusps and Euler characteristic $\chi=\chi(X)$. Then
> $$\det{}_0\big(\Delta_X-s(1-s)\big) = Z_X(s)\,e^{M+Fs(1-s)}\,G_\infty(s)^{\chi}\left(\frac{2s}{\sqrt\pi}\Big(s-\tfrac12\Big)\Gamma\Big(s-\tfrac12\Big)\right)^{-n_C},\tag{64}$$
> where $G_\infty(s)=(2\pi)^{-s}\Gamma(s)G(s)^2$ is built from the Barnes $G$-function, and
> $$M=\chi(X)\Big(\tfrac12\log2\pi-2\zeta'_{\mathbb{R}}(-1)+\tfrac14\Big),\qquad F=-\chi(X),$$
> with $\zeta_{\mathbb{R}}$ the Riemann zeta function. Consequently
> $$\det{}_0\Delta_X = \begin{cases}C_X\,Z'_X(1) & \text{if }\mathrm{Area}(X)<\infty,\\[2pt] C_X\,Z_X(1) & \text{if }\mathrm{Area}(X)=\infty,\end{cases}\qquad C_X=e^M(2\pi)^{-\chi(X)}\big(\sqrt{2\pi}\big)^{-n_C}.$$

Taking $-\log$ of (64) and separating the $\log Z_X$ term,
$$-\log\det{}_0\big(\Delta_X-s(1-s)\big) = -Fs(1-s)-M-\log Z_X(s)-D_X(s),\tag{65}$$
where
$$D_X(s) := \chi\log G_\infty(s) - \log\left(2^{s\,n_C}\Big(\pi\big(s-\tfrac12\big)\Big)^{n_C/2}\Gamma\big(s-\tfrac12\big)^{n_C}\right).\tag{66}$$

The paper quotes this theorem rather than proving it.

---

# Why it is true

The route, as the paper describes it, is a second-order differential equation in $s$ solved with two constants of integration.

Borthwick, Judge and Perry relate $\det_0\Delta_X$ to $Z_X$ through the resolvent. The identity they establish is
$$\left(\frac{1}{2s-1}\frac{\partial}{\partial s}\right)^2\log\det{}_0\big(\Delta_X-s(1-s)\big) = -\,{}^0\mathrm{Tr}\big(R_X(s)^2\big),\tag{63}$$
which says that a second-order derivative of the log-determinant, taken in the natural variable for the eigenvalue parameter $s(1-s)$, is the renormalised trace of the squared resolvent. **Integrating this in $s$ fixes the determinant up to a factor $e^{M+Fs(1-s)}$** — two constants, because the equation is second order and the operator $\frac{1}{2s-1}\partial_s$ has $1$ and $s(1-s)$ in its kernel. Comparing the resulting expression with the known analytic structure of $Z_X$ identifies the remaining factors, and matching asymptotics evaluates $M$ and $F$ in terms of $\chi(X)$.

**The mechanism in one line: a second-order identity relates $\log\det_0$ to a resolvent trace, integrating it produces $\log Z_X$ plus a two-parameter ambiguity, and the two parameters are fixed by asymptotics to be explicit functions of the Euler characteristic.**

What matters for the paper is not the derivation but the *shape* of the answer: an explicit elementary factor multiplying $Z_X(s)$. Everything that is not $Z_X$ in (64) is a function of $s$, $\chi$ and $n_C$ alone, with no further geometry — so all the surface-dependent content beyond topology sits in the Selberg zeta function, and Corollary 4.3 knows what that is in terms of loop masses.

> [!note] Remark 5.6 — why $Z'_X(1)$ in finite area and $Z_X(1)$ in infinite area
> The derivative appears in the finite-area case because **$0$ lies in the spectrum of $\Delta_X$ when $\mathrm{Area}(X)<\infty$.** There $\lambda_0=0$ gives $Z_X$ a simple zero at $s=1$, which must be divided out to form $\det_0\Delta_X$. In infinite area, $0$ is not an $L^2$ eigenvalue, $Z_X(1)\neq0$, and no derivative is needed.
>
> This is the same mechanism that makes the $\kappa\to0^+$ limit work in [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1(ii)]] and in [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]]: a $\log\kappa$ divergence cancelled against a simple zero. **Where there is no zero, there is no divergence to cancel and no limit to take** — which is why the infinite-area case of Remark 5.8 needs no renormalisation at all.

---

# Strategy

**Strategy.** Integrate the second-order resolvent identity (63) in $s$; the integration constants give a factor $e^{M+Fs(1-s)}$, and matching against the known analytic structure of $Z_X$ and the asymptotics near the ends identifies the Barnes-$G$ and Gamma factors and evaluates $M$ and $F$ in terms of $\chi(X)$.

> [!note]- Proof (skippable)
> Not reproduced in the paper. The reference given is Borthwick, Judge and Perry, and Borthwick's *Spectral theory of infinite-area hyperbolic surfaces* is the systematic account. The starting point is (63):
> $$\left(\frac{1}{2s-1}\frac{\partial}{\partial s}\right)^2\log\det{}_0\big(\Delta_X-s(1-s)\big) = -\,{}^0\mathrm{Tr}\big(R_X(s)^2\big),$$
> and integrating this in $s$ fixes the determinant up to $e^{M+Fs(1-s)}$, giving (64).

---

# What this assumes, and where to climb

**The renormalised determinant** — [[Def - Renormalised Integral and the 0-Trace]]. Without $\det_0$ there is no left-hand side; §5.2 exists to build it.

**The Selberg zeta function and its meromorphic continuation** — [[Def - Selberg Zeta Function]]. The factorisation is an identity of meromorphic functions on $\mathbb{C}$, so it lives outside the convergence region $\operatorname{Re}(s)>\delta$ and needs the continuation, which in turn rests on the Selberg trace formula.

**The Barnes $G$-function** — quoted, and the fifth of the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|recorded gaps]]. $G$ satisfies $G(s+1)=\Gamma(s)G(s)$ and is the natural "second-order Gamma function"; it turns up in every explicit determinant formula of this kind, essentially because $\log\det$ involves summing $\log\lambda$ over a spectrum whose counting function is quadratic. Nothing in the paper computes with it.

**The theorem itself is quoted wholesale.** This is the honest situation: §5.2's substance is the *substitution* of Corollary 4.3 into (65), and everything else is imported.

---

# What consumes this

- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] — the sole consumer, and the substitution is direct: replace $-\log Z_X(s)$ in (65) by the total loop mass, using $s(1-s)=-\kappa$
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.2.1
- Remark 5.8, for the infinite-area case: there the total mass is already finite by [[Thm - Finiteness of the Total Mass|Corollary 4.7]], the determinant identity holds directly at $s=1$, and the corresponding expression for $-\log\det_0\Delta_X$ via the loop mass and the resonance divisor of $Z_X$ is Lemonde–Wang's, recoverable from this theorem

---

# Reading it against the rest of the paper

The role of this theorem is exactly parallel to that of the Selberg trace formula in §5.1: it is the imported spectral input that turns the paper's probabilistic identity into a determinant statement. In §5.1 the import is the trace formula, processed through Naud's formula; in §5.2 it is this factorisation. **In both cases the paper's own contribution is the loop-mass identity of Corollary 4.3, and the imported result is what converts it into something about $\det$.**

That symmetry is worth keeping in view when reading §5, because it explains why the section feels like two disconnected halves. They are two different importations serving the same substitution.

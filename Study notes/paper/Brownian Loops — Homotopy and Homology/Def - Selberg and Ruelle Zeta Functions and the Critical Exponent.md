---
type: definition
subject: geometry
prereqs:
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
tags: [geometry, hyperbolic-geometry, spectral-geometry, zeta-functions, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$X=\Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface; $\mathcal P_X$ the set of primitive oriented closed [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length|geodesics]], $\ell_\gamma$ the length of $\gamma\in\mathcal P_X$; $s\in\mathbb{C}$ a complex variable (**not** the subordination variable of §2 — here it is the *spectral/zeta* variable). $\operatorname{Re}(s)$ its real part.

---

# Axiom Motivation

The paper sums the class-masses of §3 over *all* topological types. Each class-mass is an explicit function of a geodesic length $\ell_\gamma$, so the sum is a generating function built from the **length spectrum** $\{\ell_\gamma\}$. The **Selberg zeta function** is precisely the canonical such generating function; it plays for closed geodesics the role the Riemann zeta function plays for primes, packaging the whole length spectrum into one analytic object whose zeros encode the Laplacian's spectrum. That is why the total loop mass turns out to be a *Selberg zeta value* — the sum the paper computes is, up to a sign and log, the definition of $Z_X$.

Two companions come along. The **Ruelle zeta function** is a simpler product over lengths (one factor per geodesic, no product over $k$), related to Selberg by a shift; its *twisted* version weights each geodesic by a matrix representation, which §6 will specialise to characters to extract homology. And the **critical exponent** $\delta$ is the single number controlling convergence of all these products: it measures how fast closed geodesics proliferate (equivalently how fast the group orbit accumulates), so a zeta product converges exactly when the decay rate $s$ of its terms beats the proliferation rate $\delta$. The finiteness of the total loop mass (Corollary 4.7) is exactly the statement $s>\delta$.

---

# The Definition

> **Definition (critical exponent).** The **critical exponent** of $\Gamma$ is the exponent of convergence of the Poincaré series,
> $$\delta:=\inf\Big\{s>0:\sum_{h\in\Gamma}e^{-s\,d(z,hz)}<\infty\Big\},$$
> independent of $z\in\mathbb{H}^2$. It measures the rate at which the orbit $\Gamma z$ accumulates on the boundary. Equivalent descriptions (Patterson–Sullivan): $\delta=$ the Hausdorff dimension of the limit set $\Lambda(\Gamma)\subset\partial\mathbb{H}^2$; $\delta=$ the topological entropy of the geodesic flow; and when $\delta>\frac12$, $\lambda_0=\delta(1-\delta)$ is the smallest $L^2$-eigenvalue of $\Delta_X$. **Finite area $\Rightarrow\delta=1$** (and $\lambda_0=0$); **infinite area $\Rightarrow\delta<1$**.

> **Definition 4.1 (Selberg zeta function).** For $\operatorname{Re}(s)>\delta$,
> $$Z_X(s):=\prod_{\gamma\in\mathcal P_X}\prod_{k=0}^{\infty}\big(1-e^{-(s+k)\ell_\gamma}\big),$$
> a double (Euler) product converging absolutely for $\operatorname{Re}(s)>\delta$ and extending meromorphically to all of $\mathbb{C}$. Its logarithm expands, for $\operatorname{Re}(s)>\delta$, as
> $$-\log Z_X(s)=\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^{\infty}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},$$
> using $-\log(1-x)=\sum_m x^m/m$ and $\sum_{k\ge0}e^{-(s+k)m\ell_\gamma}=e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)$.

> **Definition 4.5 (Ruelle zeta function; twisted version).** For $\operatorname{Re}(s)>\delta$, $R_X(s):=\prod_{\gamma\in\mathcal P_X}(1-e^{-s\ell_\gamma})$, related to Selberg by $R_X(s)=Z_X(s)/Z_X(s+1)$, equivalently $Z_X(s)=\prod_{k\ge0}R_X(s+k)$. Given a finite-dimensional complex representation $\rho:\Gamma\to\mathrm{GL}(V_\rho)$ (not necessarily unitary) with $\tau$ representing the class of $\gamma$, the **twisted Ruelle zeta** is $R_X(s,\rho):=\prod_{\gamma\in\mathcal P_X}\det\big(I-\rho(\tau)e^{-s\ell_\gamma}\big)$ (well-defined since the determinant depends only on the conjugacy class), converging for $\operatorname{Re}(s)>c_\rho$ where $\|\rho(\tau)\|\le C_\rho e^{c\,\ell_\gamma}$; for unitary $\rho$, $c_\rho=\delta$.

**Concrete unpacking.** The expansion of $-\log Z_X(s)$ is *exactly* the total loop mass: comparing with §3's $\mu_X(C_X(\gamma^m))=\frac1m\frac{1}{e^{m\ell_\gamma}-1}$, one sees $\sum_{\gamma,m}\mu_X(C_X(\gamma^m))=-\log Z_X(1)$ (the case $s=1$, where $e^{(1-s)m\ell_\gamma}=1$). So the Selberg zeta at $s=1$ is $\exp(-\text{total Brownian loop mass})$. Each factor $1-e^{-(s+k)\ell_\gamma}$ is a "geodesic mode" of frequency $(s+k)\ell_\gamma$; the twisted determinant $\det(I-\rho(\tau)e^{-s\ell_\gamma})$ generalises this to a vector-valued mode, which is what lets §6 insert a character and pick out a homology class.

**Standard names.** **Selberg zeta function**, **Ruelle (dynamical) zeta function**, **twisted Ruelle zeta**, **critical exponent** (exponent of convergence of the Poincaré series; Patterson–Sullivan dimension). References: Borthwick, *Spectral Theory of Infinite-Area Hyperbolic Surfaces*, Ch. 9–10; Iwaniec, *Spectral Methods of Automorphic Forms* (finite-area Selberg theory).

---

# Examples and Non-Examples

**Is an instance.** For a closed (finite-area, cocompact) surface, $\delta=1$ and $Z_X(s)$ is the classical Selberg zeta whose non-trivial zeros sit at $s=\frac12\pm i r_n$ with $\lambda_n=\frac14+r_n^2$ the Laplace eigenvalues. For an infinite-area funnel surface, $\delta<1$ and $Z_X(1)$ is finite and positive.

**Is NOT an instance.** The Riemann zeta $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ is the *number-theoretic analogue*, not an instance: it is a single product over primes with an inverse, whereas $Z_X$ is a double product (over geodesics *and* $k\ge0$) without the inverse. The analogy "geodesics ↔ primes" is exact at the level of the prime geodesic theorem, but the zeta functions are different objects.

**Calibration check.** (1) Derive $\sum_{k\ge0}e^{-(s+k)m\ell_\gamma}=e^{-sm\ell_\gamma}/(1-e^{-m\ell_\gamma})=e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)$ (geometric series). (2) Check $R_X(s)=Z_X(s)/Z_X(s+1)$ collapses the double product to a single one (the $k=0$ factor survives, higher $k$ telescope). (3) Confirm $-\log Z_X(1)=\sum_{\gamma,m}\frac1m\frac{1}{e^{m\ell_\gamma}-1}$.

---

# Where the paper uses this

$Z_X$ is the generating function into which §4 sums all the class-masses: Lemma 4.2 (the "Selberg zeta criterion") and Corollary 4.3 give total loop mass $=-\log Z_X(\frac12+\sqrt{\frac14+\kappa})$; the twisted Ruelle $R_X(s,\rho)$ gives Corollary 4.6 and, in §6, the homology-class decomposition via characters. The critical exponent $\delta$ is the finiteness threshold (Corollary 4.7). **[[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4]]**.

---

# Verified against

Borthwick, *Spectral Theory of Infinite-Area Hyperbolic Surfaces* (2nd ed.), Ch. 9 (Selberg zeta as a double product, convergence for $\operatorname{Re}s>\delta$, meromorphic continuation) and Ch. 14 (critical exponent = Hausdorff dimension of the limit set, Patterson–Sullivan); Ruelle zeta $R_X(s)=Z_X(s)/Z_X(s+1)$ standard (Fried). Sullivan, *The density at infinity of a discrete group* (δ = dimension of limit set). Statements match the paper's §4.

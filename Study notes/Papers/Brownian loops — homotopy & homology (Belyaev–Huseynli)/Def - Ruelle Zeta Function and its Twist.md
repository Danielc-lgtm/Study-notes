---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Selberg Zeta Function"
tags: [paper, spectral-geometry, zeta-functions, dynamical-systems]
---

# Notation

- $R_X(s)$ — the Ruelle zeta function; $R_X(s,\rho)$ its twist by a representation $\rho$
- $\rho : \Gamma\to\mathrm{GL}(V_\rho)$ — a finite-dimensional complex representation, **not necessarily unitary**
- $\tau$ — a representative of the primitive hyperbolic conjugacy class corresponding to $\gamma\in\mathcal{P}_X$
- $c_\rho$ — the abscissa of convergence of the twisted product, governed by the growth $\|\rho(\tau)\|\leq C_\rho e^{c\ell_\gamma}$; one may take $c_\rho=\delta$ for unitary $\rho$
- $Z_X(s)$ — the [[Def - Selberg Zeta Function|Selberg zeta function]]; $\delta$ the critical exponent

---

# In plain language

The Ruelle zeta function is the Selberg zeta function with the $k$-product dropped:
$$R_X(s) = \prod_{\gamma\in\mathcal{P}_X}\big(1-e^{-s\ell_\gamma}\big)\qquad\text{versus}\qquad Z_X(s)=\prod_{\gamma\in\mathcal{P}_X}\prod_{k\geq0}\big(1-e^{-(s+k)\ell_\gamma}\big).$$
It is the *dynamical* zeta function: the object one writes down naturally from the closed orbits of the geodesic flow, with one factor per primitive orbit and nothing else. Selberg's extra $k$-index has a spectral origin, not a dynamical one.

The two are related by
$$R_X(s) = \frac{Z_X(s)}{Z_X(s+1)},\qquad\text{equivalently}\qquad Z_X(s)=\prod_{k=0}^\infty R_X(s+k),$$
which is just the $k$-product read backwards, and which supplies the meromorphic continuation of $R_X$ from that of $Z_X$.

**Why the paper introduces it, and what the introduction reveals.** The Selberg identity of [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] worked because $-\log Z_X$ and the loop mass have the same shape: a factor $1/m$ times $e^{(1-s)L}/(e^L-1)$. Expanding $-\log R_X$ instead gives $\sum_{\gamma,m}e^{-sm\ell_\gamma}/m$ — **no $1/(e^{m\ell_\gamma}-1)$ factor**, because that factor was exactly what the $k$-sum produced. So no single loop mass matches it, and [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]] has to reach it through a *difference* of two loop measures at two different killing rates.

The paper's verdict is worth recording: the link between total loop mass and length-spectrum zeta functions yields, in principle, an identity for any zeta function built from the length spectrum, but "for dynamical zeta functions, such as the Ruelle zeta function or its twisted versions, the corresponding identities are more difficult to use in a meaningful way". The difference structure is why — the object expressed is a signed combination, so the Poissonian interpretation of [[Thm - Poissonian Structure of Homotopy Classes|§3.3]] does not survive.

**The twist.** Weighting each geodesic by a representation $\rho$ replaces the scalar factor $1-e^{-s\ell_\gamma}$ by the determinant $\det(I-\rho(\tau)e^{-s\ell_\gamma})$. The determinant depends only on the conjugacy class of $\tau$, so the product is well defined — this is the same well-definedness that makes the free-homotopy/conjugacy correspondence usable. Twisting is the general move anticipated in Remark 3.3, and §6.2's Selberg $L$-function is the abelian one-dimensional case of it.

---

# The definition

> **Definition 4.5 (Ruelle zeta function).** The Ruelle zeta function of $X$ is
> $$R_X(s) := \prod_{\gamma\in\mathcal{P}_X}\big(1-e^{-s\ell_\gamma}\big),\qquad\operatorname{Re}(s)>\delta.\tag{36}$$
> It is related to the Selberg zeta function by
> $$R_X(s) = \frac{Z_X(s)}{Z_X(s+1)},\qquad\text{equivalently}\qquad Z_X(s)=\prod_{k=0}^\infty R_X(s+k),\tag{37}$$
> so the meromorphic continuation of $R_X$ follows from that of $Z_X$.

> **Definition (twisted Ruelle zeta function).** Let $\rho:\Gamma\to\mathrm{GL}(V_\rho)$ be a finite-dimensional complex representation, not necessarily unitary, and for $\gamma\in\mathcal{P}_X$ let $\tau$ represent the corresponding primitive hyperbolic conjugacy class. The **twisted Ruelle zeta function** is
> $$R_X(s,\rho) := \prod_{\gamma\in\mathcal{P}_X}\det\big(I-\rho(\tau)e^{-s\ell_\gamma}\big),\tag{38}$$
> which reduces to $R_X(s)$ when $\rho$ is trivial. The determinant depends only on the conjugacy class of $\tau$, so the product is well defined. It converges absolutely for $\operatorname{Re}(s)>c_\rho$, where $c_\rho$ is governed by the growth rate $\|\rho(\tau)\|\leq C_\rho e^{c\ell_\gamma}$ of the representation along geodesics; for unitary $\rho$ one may take $c_\rho=\delta$.

---

# Types and signatures

- $R_X : \{\operatorname{Re}(s)>\delta\}\to\mathbb{C}$, extended meromorphically via (37)
- $\rho : \Gamma\to\mathrm{GL}(V_\rho)$ — a group homomorphism into the invertible linear maps of a finite-dimensional complex vector space; **not** assumed unitary
- $\det(I-\rho(\tau)e^{-s\ell_\gamma})$ — a complex number, invariant under $\tau\mapsto h\tau h^{-1}$ since $\det$ is a class function
- $R_X(\cdot,\rho) : \{\operatorname{Re}(s)>c_\rho\}\to\mathbb{C}$; $c_\rho\geq\delta$, with equality for unitary $\rho$
- $-\log R_X(s,\rho) = \sum_{\gamma}\sum_{m\geq1}\frac{\operatorname{tr}\rho(\tau^m)}{m}e^{-sm\ell_\gamma}$ — via $-\log\det(I-M)=\sum_{m\geq1}\operatorname{tr}(M^m)/m$

---

# Example

The trivial representation $\rho=\mathbf{1}$ on $V_\rho=\mathbb{C}$: $\det(I-e^{-s\ell_\gamma})=1-e^{-s\ell_\gamma}$ and $R_X(s,\mathbf{1})=R_X(s)$, with $c_\rho=\delta$. The expansion is $-\log R_X(s)=\sum_{\gamma,m}e^{-sm\ell_\gamma}/m$.

Compare with the Selberg expansion $-\log Z_X(s)=\sum_{\gamma,m}\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$. Setting $L=m\ell_\gamma$, the Ruelle summand is $e^{-sL}/m$ and the Selberg summand is $\frac1m\frac{e^{(1-s)L}}{e^L-1}$. The identity that bridges them is
$$e^{(1-s)L}-e^{-sL} = e^{-sL}\big(e^L-1\big)\quad\Longrightarrow\quad \frac{e^{(1-s)L}-e^{-sL}}{e^L-1} = e^{-sL},$$
which says exactly that the Ruelle summand is the **difference** of two Selberg-type summands at spectral parameters $s$ and $s+1$. Since $s$ and $s+1$ correspond to killing rates $\kappa_-(s)=s(s-1)$ and $\kappa_+(s)=s(s+1)$, this is the computation behind [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]].

**Near-miss non-example — a non-unitary $\rho$ can shrink the convergence region.** If $\|\rho(\tau)\|$ grows like $e^{c\ell_\gamma}$ with $c>0$, the factors $\det(I-\rho(\tau)e^{-s\ell_\gamma})$ only converge for $\operatorname{Re}(s)>c_\rho>\delta$. So the twisted identity of Corollary 4.6 is stated for $\operatorname{Re}(s)>\max(c_\rho,\tfrac12)$ rather than $\operatorname{Re}(s)>\delta$: the twist can cost convergence. For unitary $\rho$, $\|\rho(\tau)\|=1$ and nothing is lost — which is why §6.2's abelian unitary twist stays in the region $\operatorname{Re}(s)>\delta$.

---

# Used in this paper at

- [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]] — the identity expressing $-\log R_X(s,\rho)$ through a difference of two loop measures
- [[§4 Zeta Identities and Finiteness of the Total Mass]] §4.1.2 — where the family of reachable zeta functions is discussed
- [[Def - Selberg L-Function]] — the abelian analogue: twisting by a **one-dimensional** unitary character of $H_1(X,\mathbb{Z})$ rather than a general representation of $\Gamma$, and twisting the *Selberg* product rather than the Ruelle one. §6.2 is the case that works cleanly, for exactly the reason this page identifies

---

# Where this sits in my DAG

Reduces to [[Def - Selberg Zeta Function]] via (37), and to elementary representation theory: finite-dimensional representations, the trace as a class function, and the expansion $-\log\det(I-M)=\sum_{m\geq1}\operatorname{tr}(M^m)/m$ (valid for $\|M\|<1$, and provable by diagonalising or by the identity $\log\det=\operatorname{tr}\log$). *Lie Groups / Representation Theory* is 🔵 in the DAG, but the content used here is at the level of [[Def - Conjugacy Class]] plus determinants of matrices, both in the vault.

The meromorphic continuation is inherited from $Z_X$ and therefore rests on the same quoted input, the Selberg trace formula — the first of the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|recorded gaps]]. The growth-rate control $\|\rho(\tau)\|\leq C_\rho e^{c\ell_\gamma}$ governing $c_\rho$ is quoted from the literature.

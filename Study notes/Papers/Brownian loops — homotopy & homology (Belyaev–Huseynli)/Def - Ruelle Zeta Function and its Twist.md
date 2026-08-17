---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Selberg Zeta Function"
tags: [paper, zeta-functions, dynamical-systems]
---

# Signature

| symbol | type |
|---|---|
| $R_X$ | $\{\mathrm{Re}(s)>\delta\}\to\mathbb{C}$ — the Ruelle zeta function |
| $\rho$ | $\Gamma\to\mathrm{GL}(V_\rho)$, a **finite-dimensional complex** representation; **not** required unitary |
| $\tau$ | $\in\Gamma$ representing the primitive hyperbolic conjugacy class of $\gamma\in\mathcal{P}_X$ |
| $R_X(\cdot,\rho)$ | $\{\mathrm{Re}(s)>c_\rho\}\to\mathbb{C}$ — the twisted Ruelle zeta |
| $c_\rho$ | abscissa of convergence, governed by $\lVert\rho(\tau)\rVert\leq C_\rho e^{c\ell_\gamma}$; $c_\rho=\delta$ for unitary $\rho$ |

---

# Definition

> **Definition 4.5 (Ruelle zeta).**
> $$R_X(s):=\prod_{\gamma\in\mathcal{P}_X}\Big(1-e^{-s\ell_\gamma}\Big),\qquad\mathrm{Re}(s)>\delta.\tag{36}$$
> A **single** Euler product — no inner $k$-product, unlike $Z_X$.

> **Definition 4.5$'$ (twisted Ruelle zeta).**
> $$R_X(s,\rho):=\prod_{\gamma\in\mathcal{P}_X}\det\Big(I-\rho(\tau)e^{-s\ell_\gamma}\Big),\qquad\mathrm{Re}(s)>c_\rho.\tag{38}$$

> **(F1) Well-definedness of (38).** $\det(I-\rho(\tau)e^{-s\ell_\gamma})$ depends only on the **conjugacy class** of $\tau$, since $\det$ is a class function. So the product is indexed by $\mathcal{P}_X$ without a choice of representative.
>
> **(F2) Relation to $Z_X$.**
> $$R_X(s)=\frac{Z_X(s)}{Z_X(s+1)},\qquad\text{equivalently}\qquad Z_X(s)=\prod_{k=0}^{\infty}R_X(s+k).\tag{37}$$
> Hence the meromorphic continuation of $R_X$ follows from that of $Z_X$ — [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions|(MC)]].
>
> **(F3) Trivial twist.** $\rho$ trivial $\Rightarrow$ $R_X(s,\rho)=R_X(s)$.
>
> **(F4) Logarithmic expansion.** $-\log\det(I-M)=\sum_{m\geq1}\mathrm{tr}(M^m)/m$ gives
> $$-\log R_X(s,\rho)=\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\frac{\mathrm{tr}\,\rho(\tau^m)\,e^{-sm\ell_\gamma}}{m}.$$
> **This is the identity §4.1.2 matches**, and the reason the twisted case is workable at all.

---

# Type card

> [!abstract] Type card — $R_X$, $R_X(\cdot,\rho)$
> **Given.** **(H1)** $X=\Gamma\backslash\mathbb{H}^2$ geometrically finite. **(H2)** for the twist: $\rho:\Gamma\to\mathrm{GL}(V_\rho)$ finite-dimensional. **(H3)** $\mathrm{Re}(s)>\delta$, resp. $>c_\rho$.
>
> **Produces.** A number in $\mathbb{C}$; via (F4), the double sum $\sum_{\gamma,m}\mathrm{tr}\,\rho(\tau^m)e^{-smL}/m$.
>
> **Lets you.** Write down a length-spectrum zeta function **weighted by a representation**, and — via [[Thm - Twisted Ruelle Zeta Identity|Cor 4.6]] — express it as a *difference* of two loop measures with different killing rates.

---

# Depends on

- [[Def - Selberg Zeta Function]] — (F2), and the continuation
- [[Def - Primitive Hyperbolic Element and Translation Length]] — the index set, and that $\tau$ is well defined up to conjugacy
- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — why a class function of $\tau$ is a function of $\gamma$
- 🟢 $\det(I-M)$, $-\log\det(I-M)=\sum\mathrm{tr}(M^m)/m$ for $\lVert M\rVert<1$ — *Linear Algebra* (7,7)
- Source for $c_\rho$: the growth bound $\lVert\rho(\tau)\rVert\leq C_\rho e^{c\ell_\gamma}$, quoted

---

# Checks

**Instance.** $\rho$ unitary: $\lVert\rho(\tau)\rVert=1$ for every $\tau$, so $c_\rho=\delta$ and (38) converges exactly where (36) does. The special case $\rho=\chi$ a **unitary character** of $H_1(X,\mathbb{Z})$ is what §6.3 uses, and there the determinant is a scalar $1-\chi(\gamma)e^{-s\ell_\gamma}$.

**Non-instance (fails H3 for non-unitary $\rho$).** $\rho$ with $\lVert\rho(\tau)\rVert$ growing like $e^{c\ell_\gamma}$ with $c>0$: then $c_\rho\geq\delta+c$ and (38) converges on a **strictly smaller** half-plane. Consequence: Corollary 4.6 must state $\mathrm{Re}(s)>\max(c_\rho,\tfrac12)$, not $\mathrm{Re}(s)>\delta$.

**Non-instance (fails the good spectral properties).** $R_X$ itself, compared with $Z_X$: the zeros of $Z_X$ sit at $s_j=\tfrac12\pm\sqrt{\tfrac14-\lambda_j}$, one per Laplace eigenvalue; by (F2) the zeros/poles of $R_X$ are differences of those, and no longer track the spectrum cleanly. **Consequence:** the paper says the Ruelle identities are "more difficult to use in a meaningful way", and it does not use them again.

---

# Used at

- [[Thm - Twisted Ruelle Zeta Identity]] — (F4) is the right-hand side matched there
- [[§4 Zeta Identities and Finiteness of the Total Mass]] §4.1.2
- [[Def - Selberg L-Function]] — the unitary-character analogue, built on $Z_X$ rather than $R_X$

---

# Commentary

> [!note]- Commentary (skippable)
> $R_X$ is the "obvious" length-spectrum zeta function — one factor per closed geodesic, precisely the Ruelle zeta of the geodesic flow — and $Z_X$ is the less obvious one with an extra product over $k$. The trade is stated by (F2): $Z_X$ is the object whose zeros are the Laplace spectrum, so it is $Z_X$ and not $R_X$ that the Selberg trace formula controls.
>
> This shows up directly in the loop-measure identities. The Selberg identity (35) matches the mass of a *single* class to a *single* term of $-\log Z_X$; the Ruelle identity of Corollary 4.6 must match a term of $-\log R_X$ to a **difference** $\mu^{\kappa_-}_X-\mu^{\kappa_+}_X$ of two loop measures, because $e^{-sL}=e^{(1-s)L}-e^{-sL}(e^L-1)\cdot0$… more precisely because $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$. The extra $k$-product of $Z_X$ is exactly what the factor $1/(e^L-1)$ supplies, and the Ruelle zeta, lacking it, needs the difference to cancel it.
>
> §4.1.2 exists to make that point and then move on: the paper says explicitly that these identities are hard to use, and does not use them.

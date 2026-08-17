---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Selberg Zeta Function"
  - "Def - Character Torus and the Pontryagin Dual"
tags: [paper, spectral-geometry, zeta-functions, homology]
---

# Notation

- $\chi : H_1(X,\mathbb{Z})\to S^1$ — a unitary character; $\chi([\gamma])$ its value on the homology class of $\gamma\in\mathcal{P}_X$
- $L_X(s,\chi)$ — the Selberg $L$-function; $Z_X(s)$ the [[Def - Selberg Zeta Function|Selberg zeta function]]
- $\mathbf{1}$ — the trivial character; $\delta$ the critical exponent
- $\mu^\kappa_X$ — the killing loop measure; $s=\tfrac12+\sqrt{\tfrac14+\kappa}$

---

# In plain language

The Selberg zeta function with each geodesic weighted by a character of the homology group.

$$Z_X(s)=\prod_{\gamma}\prod_{k\geq0}\big(1-e^{-(s+k)\ell_\gamma}\big)\qquad\longrightarrow\qquad L_X(s,\chi)=\prod_{\gamma}\prod_{k\geq0}\big(1-\chi([\gamma])e^{-(s+k)\ell_\gamma}\big).$$

Setting $\chi=\mathbf{1}$ recovers $Z_X$. So $L_X(s,\chi)$ is the **twisted Selberg zeta function associated with a one-dimensional abelian representation** — the abelian case of the twist by a representation $\rho$ of $\Gamma$ that [[Def - Ruelle Zeta Function and its Twist|§4.1.2]] considered. Like $Z_X$ it admits a meromorphic continuation to $\mathbb{C}$.

**What it is for.** Exactly what Dirichlet $L$-functions do for primes in arithmetic progressions, the paper says, and the analogy is precise. Dirichlet weights each prime by a character of $(\mathbb{Z}/q)^\times$ so that primes can be sorted by residue class, using orthogonality of characters to isolate one class at a time. Selberg $L$-functions weight each geodesic by a character of $H_1(X,\mathbb{Z})$ so that geodesics can be sorted by **homology class**, using the same orthogonality. The sorting problem is the one [[Constr - The Mass in a Homology Class|Definition 6.1]] poses: a homology class collects infinitely many homotopy classes and has no closed-form mass.

**Why it works.** The character weight in the logarithmic expansion is $\chi([\gamma])^m$, and $\chi([\gamma])^m=\chi(m[\gamma])=\chi(\beta)$ whenever $m[\gamma]=\beta$ — so the weight depends only on the **homology class of the iterate**, not on which geodesic produced it. That is exactly what lets the double sum be regrouped by homology, giving the Fourier expansion of [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]].

**Why the twist here is cleaner than §4's.** Corollary 4.6 twisted the *Ruelle* product and had to express the result as a *difference* of two loop measures, losing any interpretation as a mass. Here the twist is on the *Selberg* product, whose $k$-index supplies the factor $1/(e^{m\ell_\gamma}-1)$ that a single loop mass carries — so [[Thm - Selberg L-Function Identity|Corollary 6.4]] is a clean weighted sum of masses, with no difference required.

---

# The definition

> **Definition 6.3 (Selberg $L$-function).** The **Selberg $L$-function** associated with a unitary character $\chi:H_1(X,\mathbb{Z})\to S^1$ is
> $$L_X(s,\chi) := \prod_{\gamma\in\mathcal{P}_X}\prod_{k=0}^\infty\Big(1-\chi([\gamma])\,e^{-(s+k)\ell_\gamma}\Big),\qquad\operatorname{Re}(s)>\delta.\tag{75}$$
> When $\chi$ is trivial, $L_X(s,\chi)=Z_X(s)$. Thus $L_X(s,\chi)$ is the twisted Selberg zeta function associated with a one-dimensional abelian representation, and it admits a meromorphic continuation to $\mathbb{C}$.

**The logarithmic expansion.** For $\operatorname{Re}(s)>\delta$ the Euler product converges absolutely, so one may take logarithms term by term and expand each factor using $-\log(1-z)=\sum_{m\geq1}z^m/m$ for $|z|<1$. Here $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$, and **since $\chi$ is unitary, $|\chi([\gamma])|=1$**, so $|z|=e^{-(\operatorname{Re}(s)+k)\ell_\gamma}<1$. Summing over $k$ gives
$$\sum_{k=0}^\infty e^{-(s+k)m\ell_\gamma} = \frac{e^{-sm\ell_\gamma}}{1-e^{-m\ell_\gamma}} = \frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},$$
which is exactly the factor the killing loop mass carries — and hence [[Thm - Selberg L-Function Identity|Corollary 6.4]].

---

# Types and signatures

- $\chi : H_1(X,\mathbb{Z})\to S^1$ — a unitary character; equivalently, via $\Gamma\twoheadrightarrow H_1(X,\mathbb{Z})$, a **one-dimensional unitary representation of $\Gamma$ factoring through the abelianisation**
- $L_X(\cdot,\chi) : \{\operatorname{Re}(s)>\delta\}\to\mathbb{C}$, continued meromorphically to $\mathbb{C}$
- $L_X(s,\cdot) : \widehat{H_1(X,\mathbb{Z})}\to\mathbb{C}$ — for fixed $s$, a function on the compact character torus; **this is the direction §6.2 integrates over**
- $L_X(s,\mathbf{1})=Z_X(s)$ — the trivial character recovers the untwisted case
- $\chi([\gamma])$ — well defined on $\mathcal{P}_X$ because homology classes of oriented closed geodesics are well defined

---

# Example

The trivial character. $\chi=\mathbf{1}$ gives $L_X(s,\mathbf{1})=Z_X(s)$, and [[Thm - Selberg L-Function Identity|Corollary 6.4]] becomes [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]]. **So §6.2 is §4.1 evaluated at every point of the character torus simultaneously, then Fourier-inverted.** Keeping that in view makes the section much shorter to read: there is one identity, indexed by a torus, and one inversion.

**Near-miss non-example — a non-unitary character.** A homomorphism $H_1(X,\mathbb{Z})\to\mathbb{C}^\times$ with $|\chi(\beta)|\neq1$ breaks the definition in two ways. The absolute convergence of the Euler product for $\operatorname{Re}(s)>\delta$ fails, because the expansion needs $|z|=|\chi([\gamma])|e^{-(\operatorname{Re}(s)+k)\ell_\gamma}<1$ and unitarity is what supplies it — this is the same phenomenon as the abscissa $c_\rho>\delta$ for non-unitary $\rho$ on [[Def - Ruelle Zeta Function and its Twist]]. And there is no compact group to integrate over, so no Fourier inversion. **Unitarity is not a normalisation; it is what makes both halves of §6.2 work.**

**Second near-miss — twisting the Ruelle product instead.** $\prod_\gamma(1-\chi([\gamma])e^{-s\ell_\gamma})$ is a perfectly good object, but its logarithm expands as $\sum_{\gamma,m}\chi([\gamma])^me^{-sm\ell_\gamma}/m$ with **no** $1/(e^{m\ell_\gamma}-1)$ factor, so it does not match a single loop mass. It would need the difference construction of [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]], and the resulting signed combination would not be a mass and could not be regrouped into a Fourier expansion of masses. **The $k$-product is what makes the Selberg $L$-function, and not the twisted Ruelle zeta, the right object for §6.2.**

---

# Used in this paper at

- [[Thm - Selberg L-Function Identity|Corollary 6.4]] — the identity $-\log L_X(s,\chi)=\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$
- [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]] — $-\log L_X(s,\chi)$ is one half of the Fourier pair
- [[Thm - Distribution of the Total Homology of the Loop Soup|Proposition 6.7]] — $\mathbb{E}[\chi(\beta(\lambda))]=(Z_X(s)/L_X(s,\chi))^\lambda$, with complex powers defined via the expansion (76)
- [[Constr - The Mass in a Homology Class]] — the object the $L$-function computes

---

# Where this sits in my DAG

Two rungs: [[Def - Selberg Zeta Function]] for the untwisted product and its structure, and [[Def - Character Torus and the Pontryagin Dual]] for the characters and Haar measure. Below those, the same anchors — Euler products, $-\log(1-z)=\sum z^m/m$, geometric series, and elementary abelian-group duality.

The **meromorphic continuation** is quoted, inherited from the same source as $Z_X$'s: the Selberg trace formula, the first of the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|recorded gaps]]. As with $Z_X$, everything §6 does lives in the convergence region $\operatorname{Re}(s)>\delta$ and needs no continuation.

The analogy with Dirichlet $L$-functions is more than rhetorical and is worth keeping: it is the same construction — weight by a character of an abelian quotient, use orthogonality to isolate one class — applied to closed geodesics instead of primes, with the *Automorphic Forms / Selberg Trace Formula* (🔵) node as the common home of both stories.

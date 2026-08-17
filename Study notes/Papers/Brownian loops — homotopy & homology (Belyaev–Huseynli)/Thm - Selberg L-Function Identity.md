---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Selberg L-Function"
  - "Thm - Selberg Zeta Identity (Killing Case)"
tags: [paper, spectral-geometry, zeta-functions, homology]
---

# Notation

- $\chi : H_1(X,\mathbb{Z})\to S^1$ — a unitary character; $L_X(s,\chi)$ the [[Def - Selberg L-Function|Selberg L-function]]
- $\kappa$ — the killing rate; $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$
- $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$ — the killing loop mass
- $\mathbf{1}$ — the trivial character

---

# Type card

> [!abstract] Type card — Corollary 6.4 (Selberg $L$-function identity)
> **Given.** A unitary character $\chi:H_1(X,\mathbb{Z})\to S^1$, and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$.
>
> **Produces.** The identity $-\log L_X(s,\chi)=\sum_{\gamma,m}\chi([\gamma])^m\,\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ — an absolutely convergent $\chi$-weighted sum of loop masses, equal to a complex number.
>
> **Lets you.** Twist [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] by a character; setting $\chi=\mathbf{1}$ recovers it exactly, since $L_X(s,\mathbf{1})=Z_X(s)$. This is the one identity §6.2 runs on.

---

# Statement

> **Corollary 6.4 (Selberg $L$-function identity).** Let $\chi:H_1(X,\mathbb{Z})\to S^1$ be a unitary character, and let $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$. Then
> $$-\log L_X(s,\chi) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\chi([\gamma])^m\,\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\frac1m\cdot\frac{\chi([\gamma])^m\,e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.\tag{76}$$

---

# Why it is true

The logarithm of $L_X(s,\chi)$ has the same expansion as in the untwisted case, with the character carried along as a coefficient. Nothing else happens.

Expanding the Euler product term by term — legal because it converges absolutely for $\operatorname{Re}(s)>\delta$ — and applying $-\log(1-z)=\sum_{m\geq1}z^m/m$ with $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$, the $k$-sum is geometric and gives $e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)$, which is exactly the factor in the killing loop mass. The character contributes $\chi([\gamma])^m$ and nothing more.

**The mechanism in one line: the $k$-product of the Selberg-type Euler product produces the factor $1/(e^{m\ell_\gamma}-1)$ that a single loop mass carries, and the character rides along untouched as $\chi([\gamma])^m$.**

Two things are quietly essential and are worth separating.

**Unitarity supplies the convergence of the expansion.** The step $-\log(1-z)=\sum_m z^m/m$ needs $|z|<1$, and $|z|=|\chi([\gamma])|e^{-(\operatorname{Re}(s)+k)\ell_\gamma}$. Since $\chi$ is unitary, $|\chi([\gamma])|=1$ and $|z|=e^{-(\operatorname{Re}(s)+k)\ell_\gamma}<1$. A non-unitary character would break this — the same phenomenon as the abscissa $c_\rho>\delta$ on [[Def - Ruelle Zeta Function and its Twist]].

**The $k$-product is what makes the identity clean.** Twisting the *Ruelle* product instead would give $\sum_{\gamma,m}\chi([\gamma])^me^{-sm\ell_\gamma}/m$, with no $1/(e^{m\ell_\gamma}-1)$, so no single loop mass matches and one would need the difference construction of [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]] — producing a signed combination that is not a mass and cannot be regrouped into a Fourier expansion of masses. **The whole of §6.2 depends on the twisted object being the Selberg one.**

**What the identity is for.** Not itself — it is a stepping stone. The character weight satisfies $\chi([\gamma])^m=\chi(m[\gamma])=\chi(\beta)$ whenever $m[\gamma]=\beta$, so the weight depends only on the homology class of the iterate. That is exactly what lets [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]] regroup the double sum by homology class, turning (76) into a Fourier expansion whose coefficients are the homology masses.

---

# Strategy

**Strategy.** Take logarithms of the absolutely convergent Euler product term by term, expand $-\log(1-z)=\sum_{m\geq1}z^m/m$ with $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$ — legitimate because $|\chi([\gamma])|=1$ gives $|z|<1$ — and sum the geometric series over $k$ to get $e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)$.

> [!note]- Proof (skippable)
> For $\operatorname{Re}(s)>\delta$ the Euler product (75) converges absolutely, so one may take logarithms term by term and expand each factor using $-\log(1-z)=\sum_{m=1}^\infty z^m/m$ when $|z|<1$. Here $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$, and since $\chi$ is unitary, $|\chi([\gamma])|=1$, so $|z|=e^{-(\operatorname{Re}(s)+k)\ell_\gamma}<1$.
>
> Summing over $k$,
> $$\sum_{k=0}^\infty e^{-(s+k)m\ell_\gamma} = \frac{e^{-sm\ell_\gamma}}{1-e^{-m\ell_\gamma}} = \frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},$$
> and recognising this as $m\cdot\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ gives (76). $\;\square$

---

# What this assumes, and where to climb

**The $L$-function and its convergence region** — [[Def - Selberg L-Function]], and through it [[Def - Selberg Zeta Function]] and [[Def - Character Torus and the Pontryagin Dual]].

**Unitarity of $\chi$.** Load-bearing, as above. Everything in §6.2 is stated for unitary characters, and the character torus is by definition the unitary ones.

**The killing mass formula** — [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] and upstream [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]], §3.1.2. Note that the corollary uses the *formula* $\frac1m\frac{e^{(1-s)L}}{e^L-1}$, not the summed identity; the summation happens afterwards.

**$\operatorname{Re}(s)>\delta$** — [[Def - Critical Exponent and the Prime Geodesic Theorem]], for absolute convergence of the product and hence for the term-by-term logarithm.

---

# What consumes this

- [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]] — regroups (76) by homology class to get the Fourier expansion, then inverts
- [[Thm - Distribution of the Total Homology of the Loop Soup|Proposition 6.7]] — applied twice, to $\chi$ and to the trivial character, giving $\mathbb{E}[\chi(\beta(\lambda))]=(Z_X(s)/L_X(s,\chi))^\lambda$
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2

---

# Reading it against the rest of the paper

This is the third and cleanest instance of the twisting anticipated in [[§3.2 Euclidean Quantum Mechanics and the Path Integral|Remark 3.3]], which observed that the homotopy decomposition is the trivial-character case of the path-integral homotopy theorem, and that twisting by a unitary representation of $\pi_1(X)$ replaces the periodisation by its twisted form. The three instances:

| where | twist by | resulting object | shape of the identity |
|---|---|---|---|
| §3, §4.1.1 | trivial character | Selberg zeta $Z_X$ | a single loop mass |
| §4.1.2 | finite-dimensional $\rho$ of $\Gamma$, on the **Ruelle** product | twisted Ruelle $R_X(s,\rho)$ | a **difference** of two loop masses |
| §6.2 | one-dimensional unitary $\chi$ of $H_1$, on the **Selberg** product | Selberg $L$-function $L_X(s,\chi)$ | a $\chi$-weighted sum of loop masses |

The middle row is the awkward one, and the reason is visible in the table: it is the only one that twists the wrong product. **Reading the three rows together is the efficient way to see what §6.2 is doing and why it works when §4.1.2 does not quite.**

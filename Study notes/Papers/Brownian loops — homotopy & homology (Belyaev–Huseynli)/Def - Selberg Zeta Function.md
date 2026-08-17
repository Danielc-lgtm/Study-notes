---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Primitive Hyperbolic Element and Translation Length"
  - "Def - Critical Exponent and the Prime Geodesic Theorem"
tags: [paper, spectral-geometry, zeta-functions]
---

# Notation

- $X=\Gamma\backslash\mathbb{H}^2$ — a geometrically finite hyperbolic surface; $\mathcal{P}_X$ its primitive oriented closed geodesics
- $\ell_\gamma$ — the length of $\gamma\in\mathcal{P}_X$; $\delta$ the [[Def - Critical Exponent and the Prime Geodesic Theorem|critical exponent]] of $\Gamma$
- $Z_X(s)$ — the Selberg zeta function; $s\in\mathbb{C}$ the spectral parameter
- $Z'_X(1)$ — the derivative at $s=1$, which appears whenever $\lambda_0=0$ is in the spectrum
- $\lambda_0$ — the smallest $L^2$-eigenvalue of $\Delta_X$

---

# In plain language

The Selberg zeta function is to closed geodesics what the Riemann zeta function is to primes: an Euler product over the primitive objects, whose logarithm expands into a sum over all their powers.

The only structural difference is the **double** product. Where Riemann has $\prod_p(1-p^{-s})^{-1}$, Selberg has $\prod_\gamma\prod_{k\geq0}(1-e^{-(s+k)\ell_\gamma})$ — an extra product over $k\geq0$. That extra index looks like a complication until one takes logarithms, at which point it sums geometrically and produces exactly the factor $1/(e^{m\ell_\gamma}-1)$ that the loop mass carries:
$$-\log Z_X(s) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},\qquad\operatorname{Re}(s)>\delta.\tag{32}$$
Compare with the killing mass formula $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$: **the two expansions are term for term identical.** So the identity of [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] is not a coincidence to be explained but a matching of two expansions of the same shape, and the double product is precisely what makes the shapes match.

The zeta function is where all the spectral information of $X$ ends up. Its zeros encode the eigenvalues of $\Delta_X$; the simple zero at $s=1$ comes from $\lambda_0=0$ when $\mathrm{Area}(X)<\infty$, which is why $Z'_X(1)$ rather than $Z_X(1)$ appears in every finite-area determinant formula of §5.

---

# The definition

> **Definition 4.1 (Selberg zeta function).** The Selberg zeta function of a geometrically finite hyperbolic surface $X=\Gamma\backslash\mathbb{H}^2$ is the double Euler product
> $$Z_X(s) := \prod_{\gamma\in\mathcal{P}_X}\prod_{k=0}^\infty\Big(1-e^{-(s+k)\ell_\gamma}\Big),\qquad\operatorname{Re}(s)>\delta,\tag{31}$$
> where $\delta$ is the critical exponent of $\Gamma$. It converges absolutely for $\operatorname{Re}(s)>\delta$ and admits a meromorphic continuation to $\mathbb{C}$.

**The logarithmic expansion.** Taking the logarithm of (31) and expanding $-\log(1-x)=\sum_{m\geq1}x^m/m$ gives, for $\operatorname{Re}(s)>\delta$,
$$-\log Z_X(s) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},\tag{32}$$
where the inner sum over $k$ is geometric: $\sum_{k=0}^\infty e^{-(s+k)m\ell_\gamma} = e^{-sm\ell_\gamma}/(1-e^{-m\ell_\gamma}) = e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)$.

---

# Types and signatures

- $Z_X : \{\operatorname{Re}(s)>\delta\}\to\mathbb{C}$ initially, extended meromorphically to $\mathbb{C}$; holomorphic and non-vanishing on $\operatorname{Re}(s)>\delta$
- $-\log Z_X : (\delta,\infty)\to(0,\infty)$ on the real axis — **positive**, since (32) is a sum of positive terms, so $0<Z_X(s)<1$ for real $s>\delta$
- $Z'_X(1)$ — a number; non-zero exactly when the zero of $Z_X$ at $s=1$ is simple, which is the case when $\lambda_0=0$ is a simple eigenvalue
- the product over $\gamma$ runs over **primitive** geodesics only; the powers are supplied by the $m$-sum in (32)

---

# Example

The behaviour at the two ends of the real axis, both of which the paper uses.

**As $s\downarrow\delta$**: by (32), $-\log Z_X(s)$ increases to the divergent sum of [[Thm - Finiteness of the Total Mass|Corollary 4.7]], so by monotone convergence $Z_X(s)\to0$. The zeta function vanishes at the critical exponent, and the total loop mass blows up there.

**As $s\to\infty$**: the sum in (32) is dominated by the slowest-decaying terms, which are the primitive ($m=1$) classes realising the systole. So
$$-\log Z_X(s)\sim \frac{N_{\mathrm{sys}}}{1-e^{-\ell_{\mathrm{sys}}}}\,e^{-s\ell_{\mathrm{sys}}}\qquad(s\to\infty),$$
from which both the [[Def - Systole|systole]] and its multiplicity are recoverable — this is [[Thm - Concentration on Systolic Classes|the $s\to\infty$ analysis of §6.1]].

**At $s=1$ with $\mathrm{Area}(X)<\infty$**: $\lambda_0=0$ is in the spectrum, and $Z_X$ has a **simple zero** at $s=1$. This is why $\log Z'_X(1)$ and not $\log Z_X(1)$ appears in $\log\det_\zeta\Delta=\mathrm{Area}(X)E+\log Z'_X(1)$, and why the $\kappa\to0^+$ limit in [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1(ii)]] works: the $\log\kappa$ divergence of the exponential integral cancels against $-\log(s-1)$ coming from the simple zero, since $s-1\sim\kappa$.

**Near-miss non-example — dropping the $k$-product.** The single product $R_X(s)=\prod_\gamma(1-e^{-s\ell_\gamma})$ is the [[Def - Ruelle Zeta Function and its Twist|Ruelle zeta function]], and its logarithm expands as $-\log R_X(s)=\sum_{\gamma,m}\frac{e^{-sm\ell_\gamma}}{m}$ — **no $1/(e^{m\ell_\gamma}-1)$ factor**. So no single loop mass matches it, and [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]] has to express $-\log R_X$ as a *difference* of two loop measures at two different killing rates. The relation between the two is $R_X(s)=Z_X(s)/Z_X(s+1)$, equivalently $Z_X(s)=\prod_{k\geq0}R_X(s+k)$ — which is the $k$-product read backwards. **The extra $k$-index is exactly what makes Selberg, and not Ruelle, the zeta function the loop measure sees directly.**

---

# Used in this paper at

- [[Thm - Selberg Zeta Criterion|Lemma 4.2]] — the criterion concludes an identity with $-\log Z_X(s)$
- [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] — the central identity: total killing mass $=-\log Z_X(s)$
- [[Def - Ruelle Zeta Function and its Twist]] — $R_X(s)=Z_X(s)/Z_X(s+1)$; the meromorphic continuation of $R_X$ follows from that of $Z_X$
- [[Thm - Finiteness of the Total Mass|Corollary 4.7]] — $Z_X(s)\to0$ as $s\downarrow\delta$
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]] and [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] — $\log Z'_X(1)$ in both determinant formulas
- [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]] — $\det_0(\Delta_X-s(1-s))$ factorises through $Z_X(s)$
- [[Constr - The Probability Measure on Free Homotopy Classes]] — $-\log Z_X(s)$ is the normalising constant
- [[Thm - Moments of the Length via the Selberg Zeta Function]] — every moment is a derivative of $F(s)=-\log Z_X(s)$
- [[Def - Selberg L-Function]] — $L_X(s,\chi)$ is the character-twisted version, reducing to $Z_X$ at $\chi=\mathbf{1}$

**This is the most-consumed page in the note-set**, which is the right shape: $Z_X$ is where the paper's geometry and its analysis meet.

> [!note] Remark 4.4 — the bosonic partition function reading
> Set $Z_\gamma(s):=\prod_{k\geq0}(1-e^{-(s+k)\ell_\gamma})^{-1}$ and $Z(s):=\prod_{\gamma}Z_\gamma(s)=Z_X(s)^{-1}$. Then Corollary 4.3 reads $\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\log Z(s)$. Each $Z_\gamma(s)$ is the partition function of a family of bosonic modes indexed by $k\geq0$ with weights $(s+k)\ell_\gamma$, and $Z(s)$ is the grand canonical partition function of a free non-interacting Bose gas at zero chemical potential. **The $k$-index, which looked like a technical feature of the Euler product, is a mode number.**

---

# Where this sits in my DAG

Three ingredients, and the third is the deep one. The geometry — primitive closed geodesics and their lengths — is [[Def - Primitive Hyperbolic Element and Translation Length]]. The convergence region is [[Def - Critical Exponent and the Prime Geodesic Theorem]]. The analysis of the product and its logarithm is elementary complex analysis: Euler products, $-\log(1-x)=\sum x^m/m$, geometric series, order of a zero.

**The meromorphic continuation to $\mathbb{C}$ is quoted, not proved**, and it comes from the Selberg trace formula — the deepest input to the paper and the first of the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|recorded gaps]]. Home node: *Automorphic Forms / Selberg Trace Formula* (🔵), with Iwaniec and Bergeron as references. Everything in §4 lives in the convergence region $\operatorname{Re}(s)>\delta$ and needs no continuation; §5 needs it.

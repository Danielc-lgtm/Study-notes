---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Selberg Zeta Criterion"
  - "Def - Selberg Zeta Function"
  - "Constr - The Weighted Heat-Kernel Integral Iϕ"
tags: [paper, spectral-geometry, zeta-functions, loop-measures]
---

# Notation

- $\kappa\geq-\tfrac14$ — the killing rate; $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ the spectral parameter, equivalently $\kappa=s(s-1)$
- $\mu^\kappa_X$ — the loop measure of Brownian motion with killing at rate $\kappa$
- $Z_X(s)$ — the [[Def - Selberg Zeta Function|Selberg zeta function]]; $\delta$ the [[Def - Critical Exponent and the Prime Geodesic Theorem|critical exponent]]
- $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$ — the [[Constr - The Weighted Heat-Kernel Integral Iϕ|weighted heat-kernel integral]] in the killing case
- $L=m\ell_\gamma$

---

# Type card

> [!abstract] Type card — Corollary 4.3 (Selberg zeta identity, killing case)
> **Given.** A killing rate $\kappa\geq-\tfrac14$; set $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, and assume $s>\delta$, the [[Def - Critical Exponent and the Prime Geodesic Theorem|critical exponent]].
>
> **Produces.** The identity: total mass of the killing loop measure over all non-trivial non-peripheral classes $=-\log Z_X(s)$. A single equality of finite positive real numbers.
>
> **Lets you.** Read the total loop mass straight off the Selberg zeta function, and — at $\kappa=0$, $s=1$ — recover the Brownian total mass as $-\log Z_X(1)$. Everything in §5 and §6 runs on this identity: it is the normalising constant of $\mathbb{P}_s$, the quantity substituted into the determinant formulas, and the trivial-character case of the Selberg $L$-function identity.

---

# Statement

> **Corollary 4.3 (Selberg zeta identity, killing case).** For any $\kappa\geq-\tfrac14$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}>\delta$,
> $$\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = -\log Z_X\Big(\tfrac12+\sqrt{\tfrac14+\kappa}\Big).\tag{35}$$

Setting $\kappa=0$ gives $s=1$, hence the Brownian total mass is $\sum_{\gamma,m}\mu_X(\mathcal{C}_X(\gamma^m))=-\log Z_X(1)$. When $X$ has infinite area, $\delta<1$ and this quantity is finite; in the finite-area case $\delta=1$ and the sum diverges — see [[Thm - Finiteness of the Total Mass|Corollary 4.7]]. The killing identity was originally shown by Lemonde–Wang.

---

# Why it is true

Everything has already been done; this is the verification.

The killing mass is $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)L}}{e^L-1}$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, and the logarithm of the Selberg zeta function expands as $-\log Z_X(s)=\sum_{\gamma,m}\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$. **These are the same expression.** The [[Thm - Selberg Zeta Criterion|criterion]] is the formalisation of "these are the same expression"; the corollary is the observation that in this case they are.

What is worth pausing on is *why* the exponent works out. The substitution $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ is not a change of variable chosen for elegance. Starting from $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$,
$$\frac{L}{2\sinh(L/2)}I_\kappa(L) = \frac{e^{-L\sqrt{1/4+\kappa}}}{2\sinh(L/2)} = \frac{e^{-L\sqrt{1/4+\kappa}}\cdot e^{L/2}}{e^L-1} = \frac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1},$$
using $2\sinh(L/2)=e^{L/2}-e^{-L/2}=e^{-L/2}(e^L-1)$. So the exponent is forced to be $\tfrac12-\sqrt{\tfrac14+\kappa}=1-s$: **the $\tfrac12$ comes from the $\sinh$, and the $\sqrt{\tfrac14+\kappa}$ comes from the heat-kernel integral, and $s$ is defined so that their difference is $1-s$.** That is where the ubiquitous substitution comes from and why it recurs in every later section.

The $\tfrac14$ inside the square root traces back further still — to the $e^{-s/4}$ in [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]], which is the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$. **So the spectral parameter of §4–§6 is spectral in a literal sense: $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ solves $s(s-1)=\kappa$, and $s(1-s)$ is the eigenvalue parameter of $\Delta_{\mathbb{H}^2}$.** This is exactly the relation §5.2 uses when it writes $\Delta_X-s(1-s)=\Delta_X+\kappa$.

---

# Strategy

**Strategy.** Verify the hypothesis (33) of the criterion with $C=1$: from $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$ one gets $\frac{L}{2\sinh(L/2)}I_\kappa(L)=\frac{e^{(1-s)L}}{e^L-1}$ for $s=\tfrac12+\sqrt{\tfrac14+\kappa}$; then apply Lemma 4.2.

> [!note]- Proof (skippable)
> For $\phi(\lambda)=\lambda+\kappa$, formula (25) gives $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$ — see [[Constr - The Weighted Heat-Kernel Integral Iϕ]] for that computation, which is the integral identity with $a=\tfrac14+\kappa$, $b=L^2/4$. Hence
> $$\frac{L}{2\sinh(L/2)}I_\kappa(L) = \frac{e^{-L\sqrt{1/4+\kappa}}}{2\sinh(L/2)} = \frac{e^{(1-s)L}}{e^L-1},\qquad s=\tfrac12+\sqrt{\tfrac14+\kappa},$$
> using $2\sinh(L/2)=e^{-L/2}(e^L-1)$ and $\tfrac12-\sqrt{\tfrac14+\kappa}=1-s$.
>
> This is (33) with $C=1$, and $s>\delta$ by hypothesis. [[Thm - Selberg Zeta Criterion|Lemma 4.2]] then gives (35). $\;\square$

---

# What this assumes, and where to climb

**The criterion** — [[Thm - Selberg Zeta Criterion]] — and hence [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] and the whole §3 apparatus behind it.

**$I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$** — [[Constr - The Weighted Heat-Kernel Integral Iϕ]]. One application of the Gaussian identity $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$.

**$s>\delta$** — [[Def - Critical Exponent and the Prime Geodesic Theorem]]. Without it the Euler product does not converge and both sides are infinite. In practice this is a condition on $\kappa$: for a finite-area surface $\delta=1$ forces $\kappa>0$, and for an infinite-area surface $\delta<1$ permits $\kappa=0$ and even a range of negative $\kappa$.

**The extended range $\kappa\in[-\tfrac14,0)$**, where $\phi(\lambda)=\lambda+\kappa$ is not a Bernstein function — see Remark 3.7 on [[§3 Decomposition over Homotopy Classes]]. The formula (26) continues to make analytic sense there and the integral converges, and $\kappa=-\tfrac14$ gives $s=\tfrac12$, the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$. So the corollary's range is the whole real-$s$ range $s\geq\tfrac12$, cut off by the spectrum rather than by the Bernstein condition — and further cut to $s>\delta$ for convergence.

---

# What consumes this

- [[Constr - The Probability Measure on Free Homotopy Classes]] — $-\log Z_X(s)$ is the normalising constant of $\mathbb{P}_s$; §6 exists only because this identity gives the denominator a closed form
- [[Thm - Moments of the Length via the Selberg Zeta Function]] — every moment is a derivative of $F(s)=-\log Z_X(s)$, which is this identity differentiated
- [[Thm - Concentration on Systolic Classes]] — the $s\to\infty$ asymptotics of both sides
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1(ii)]] — substituted directly, giving $-\log\det_\zeta\Delta = -\mathrm{Area}(X)E+\log\kappa-\log Z_X(s)+O(\kappa)$
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] — substituted into the Borthwick–Judge–Perry factorisation
- [[Thm - Selberg L-Function Identity|Corollary 6.4]] — the trivial-character case: $L_X(s,\mathbf{1})=Z_X(s)$
- [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]] — uses the mass formula (26) that this corollary's proof passes through
- [[Thm - Distribution of the Total Homology of the Loop Soup|Proposition 6.7]] — the $\lambda\log Z_X(s)$ term in the exponential formula

**This is the most-consumed theorem in the paper.** Everything after §4 is an operation on it.

---

# Reading it against the rest of the paper

The identity is originally Lemonde–Wang's; the present paper reproves it as one instance of the criterion, alongside three others. That reframing is the point: the killing case is not special, it is the case with $C=1$.

The reading of the identity worth keeping is the one in Remark 4.4. Writing $Z(s)=Z_X(s)^{-1}$ as a product of $Z_\gamma(s)=\prod_{k\geq0}(1-e^{-(s+k)\ell_\gamma})^{-1}$, each factor is the partition function of a family of bosonic modes with weights $(s+k)\ell_\gamma$, and $Z(s)$ is a free Bose gas at zero chemical potential. So the total loop mass is a log-partition-function. Set that beside [[Def - Schwinger Proper-Time Representation|§3.2]], where the total mass over *all* loops was half a log-determinant, and the two readings are the two sides of a Gaussian integral — $\det^{-1/2}$ on one side, a partition function on the other.

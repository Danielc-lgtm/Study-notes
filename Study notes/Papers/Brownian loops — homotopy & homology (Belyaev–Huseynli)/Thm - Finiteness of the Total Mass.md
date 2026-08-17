---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Critical Exponent and the Prime Geodesic Theorem"
  - "Def - Systole"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
tags: [paper, spectral-geometry, loop-measures, convergence]
---

# Notation

- $s=s(\phi)$ — the spectral parameter attached to $\phi$: $s=1$ for Brownian motion and $\alpha$-stable, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ for killing at rate $\kappa\geq-\tfrac14$ and for the shifted $\alpha$-stable case
- $C>0$ — the constant of the mass formula: $1$ in the Brownian and killing cases, $\alpha/2$ in the stable cases
- $\delta$ — the [[Def - Critical Exponent and the Prime Geodesic Theorem|critical exponent]]; $N_X(R)$ the prime geodesic counting function
- $\ell_{\mathrm{sys}}$ — the [[Def - Systole|systole]]; $L=m\ell_\gamma$
- $Z_X(s)$ — the [[Def - Selberg Zeta Function|Selberg zeta function]]

---

# Type card

> [!abstract] Type card — Corollary 4.7 (finiteness)
> **Given.** Any of the Bernstein functions treated in the paper, with its spectral parameter $s=s(\phi)$ and constant $C$; the [[Def - Critical Exponent and the Prime Geodesic Theorem|prime geodesic theorem]] $N_X(R)\sim e^{\delta R}/\delta R$ for $\Gamma$; the [[Def - Systole|systole]] $\ell_{\mathrm{sys}}$.
>
> **Produces.** A dichotomy. If $s(\phi)>\delta$, the total mass $\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ is **finite**. At $s=\delta$ the sum diverges, and $Z_X(s)\to0$ as $s\downarrow\delta$ by monotone convergence.
>
> **Lets you.** Know in advance whether the normalisation of §6 is available. Infinite-area surfaces have $\delta<1$ and need nothing; finite-area surfaces have $\delta=1$ and need either a killing rate $\kappa>0$ or the renormalisation of §5.

---

# Statement

> **Corollary 4.7 (finiteness).** Let $\phi$ be any of the Bernstein functions treated in this paper, with associated spectral parameter $s=s(\phi)$ — that is, $s=1$ for Brownian motion and $\alpha$-stable, and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ for killing with rate $\kappa\geq-\tfrac14$ and for the shifted $\alpha$-stable case. If $s(\phi)>\delta$ then the total mass is finite,
> $$\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)<\infty.\tag{41}$$

---

# Why it is true

A competition between two exponential rates, and the theorem is that the exponents decide it.

**On one side, decay.** The mass of a class of geodesic length $L$ behaves like $e^{-sL}$: from the formula $\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$, the numerator grows like $e^{(1-s)L}$ and the denominator like $e^L$, so the ratio decays like $e^{-sL}$. Longer classes carry exponentially less mass, at rate $s$.

**On the other side, proliferation.** By the prime geodesic theorem there are about $e^{\delta R}/\delta R$ primitive geodesics of length up to $R$. Classes proliferate exponentially, at rate $\delta$.

**Finite total mass is exactly $s>\delta$: decay beats proliferation.** That is the entire content, and it is worth holding in that form because every convergence hypothesis in the paper is an instance of it.

The two technical steps are bookkeeping in service of that statement. Summing over the iterates $m$ first is legitimate because the $m$-sum is dominated by its first term up to a constant: the upper bound comes from $\sum_{m\geq1}x^m/m=-\log(1-x)$ with $x=e^{-s\ell_\gamma}$, and since $-\log(1-x)=x+O(x^2)$ and $x\to0$ along $\mathcal{P}_X$, the bound is asymptotically the $m=1$ term. So the $m$-sum contributes nothing to the convergence question, and everything reduces to $\sum_\gamma e^{-s\ell_\gamma}$. Then that sum is a Riemann–Stieltjes integral against the counting function, and integrating by parts converts the prime geodesic theorem into an explicit integrand $e^{-(s-\delta)R}/R$.

**The mechanism in one line: the mass decays at rate $s$ in the length, the geodesics proliferate at rate $\delta$ in the length, and integration by parts against the counting function turns the comparison into $\int^\infty e^{-(s-\delta)R}\,\mathrm{d}R/R$.**

**The borderline is as gentle as it could be and still fail.** At $s=\delta$ the integrand is $1/R$ and the integral diverges logarithmically — the slowest possible divergence. So the criterion $s>\delta$ is sharp, and the failure at equality is marginal rather than catastrophic. Correspondingly $-\log Z_X(s)$ increases to $+\infty$ as $s\downarrow\delta$, so $Z_X(s)\to0$: the zeta function vanishes exactly where the mass blows up.

---

# Strategy

**Strategy.** Sum over the iterates $m$ first, sandwiching $\sum_{m\geq1}\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ between $Ce^{-s\ell_\gamma}$ and a constant multiple of $-\log(1-e^{-s\ell_\gamma})$, so that finiteness reduces to convergence of $\sum_\gamma e^{-s\ell_\gamma}$; then write that sum as a Riemann–Stieltjes integral against $N_X$ and integrate by parts, so the prime geodesic theorem turns the integrand into $e^{-(s-\delta)R}/R$.

> [!note]- Proof (skippable)
> In each case
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{C}{m}\cdot\frac{e^{(1-s)L}}{e^L-1},\qquad L=m\ell_\gamma,\ s=s(\phi),$$
> for a constant $C>0$, equal to $1$ in the Brownian and killing cases and to $\alpha/2$ in the stable cases.
>
> **Step 1 — summing over the iterates $m$.** For $L\geq\ell_{\mathrm{sys}}$ one has $e^L-1\geq(1-e^{-\ell_{\mathrm{sys}}})e^L$, hence $\frac{e^{(1-s)L}}{e^L-1}\leq\frac{e^{-sL}}{1-e^{-\ell_{\mathrm{sys}}}}$. Using $\sum_{m\geq1}x^m/m=-\log(1-x)$ with $x=e^{-s\ell_\gamma}$,
> $$\sum_{m\geq1}\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)\;\leq\;\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}\sum_{m\geq1}\frac{e^{-sm\ell_\gamma}}{m} = -\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}\log\big(1-e^{-s\ell_\gamma}\big).$$
> Conversely, keeping only the $m=1$ term,
> $$\sum_{m\geq1}\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)\;\geq\;C\cdot\frac{e^{(1-s)\ell_\gamma}}{e^{\ell_\gamma}-1}\;\geq\;Ce^{-s\ell_\gamma}.$$
> Since $N_X(R)<\infty$ for every $R$, only finitely many geodesics have length below any bound, so $\ell_\gamma\to\infty$ along $\mathcal{P}_X$; as $e^{-s\ell_\gamma}\to0$ and $-\log(1-x)=x+O(x^2)$, the upper bound is asymptotic to $\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}e^{-s\ell_\gamma}$. **The total mass is therefore finite if and only if**
> $$\sum_{\gamma\in\mathcal{P}_X}e^{-s\ell_\gamma}<\infty.\tag{42}$$
>
> **Step 2 — the geodesic sum via the counting function.** Writing (42) as an integral against $N_X$ and integrating by parts over $[0,T]$,
> $$\sum_{\ell_\gamma\leq T}e^{-s\ell_\gamma} = \int_0^T e^{-sR}\,\mathrm{d}N_X(R) = e^{-sT}N_X(T) + s\int_0^T e^{-sR}N_X(R)\,\mathrm{d}R,$$
> since $N_X(R)=0$ for $R<\ell_{\mathrm{sys}}$ so there is no boundary term at $0$. By the prime geodesic theorem (40), $N_X(R)\asymp e^{\delta R}/R$ for large $R$, so the large-$R$ behaviour of the integrand is $e^{-(s-\delta)R}/R$, and
> $$\int^\infty\frac{e^{-(s-\delta)R}}{R}\,\mathrm{d}R\quad\begin{cases}\text{converges},& s>\delta,\\ \text{diverges (like }\int^\infty \mathrm{d}R/R),& s=\delta,\\ \text{diverges},& s<\delta.\end{cases}$$
> For $s>\delta$ the boundary term $e^{-sT}N_X(T)$ tends to $0$ as $T\to\infty$, so (42) converges; for $s\leq\delta$ the integral term alone already diverges. Thus the total mass is finite when the decay rate $s$ exceeds the proliferation rate $\delta$, which gives (41).
>
> At $s=\delta$ the sum diverges; since $-\log Z_X(s)$ increases to this divergent sum as $s\downarrow\delta$, monotone convergence gives $Z_X(s)\to0$ as $s\downarrow\delta$, and the total mass blows up. In the finite-area case $\delta=1$ and a killing rate $\kappa>0$ — equivalently $s(\kappa)>1$ — is needed to restore finiteness. $\;\square$

---

# What this assumes, and where to climb

**The mass formula in the shape $\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$** — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] via [[Thm - Selberg Zeta Criterion|Lemma 4.2]] and the four verified cases. **The corollary is stated for "any of the Bernstein functions treated in this paper" rather than for all $\phi$**, precisely because it needs this shape; a process whose mass had a different functional form in $L$ would need its own analysis.

**The prime geodesic theorem** — [[Def - Critical Exponent and the Prime Geodesic Theorem]]. Quoted, not proved; it is the second of the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|recorded gaps]], and it closes with the Selberg trace formula. Everything in the proof's Step 2 is bookkeeping around it.

**The systole** — [[Def - Systole]], only for the uniform bound $e^L-1\geq(1-e^{-\ell_{\mathrm{sys}}})e^L$. Its precise value is irrelevant; only that it is positive.

**Riemann–Stieltjes integration by parts against a counting function** — anchor material, and the reusable technique here. This is the standard device for converting a counting asymptotic into a convergence criterion for a weighted sum, and it is the same manoeuvre used to deduce convergence of Dirichlet series from the prime number theorem.

---

# What consumes this

- [[Constr - The Probability Measure on Free Homotopy Classes]] — the existence of the normalisation is exactly this corollary; §6 cannot begin without it
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] — §5 exists to handle the divergent case $\delta=1$, $\kappa=0$
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1(ii)]] — "for $\kappa>0$ the total mass is finite, so no cutoff is needed" is a direct appeal to this corollary
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] and Remark 5.8 — the infinite-area case needs no renormalisation because $\delta<1$
- [[Def - Geometrically Finite Surfaces, Cusps and Funnels]] — the area/$\delta$ dichotomy is what this corollary turns into a practical criterion

---

# Reading it against the rest of the paper

This is one of the three proofs worth reading in full, and the reason is transferability. The integration-by-parts-against-the-counting-function move is the template for **every** convergence question in this circle of ideas, and it is the same argument by which one deduces convergence of $\sum_p p^{-s}$ from the prime number theorem. Having it once means having it for any length-spectrum sum.

The borderline behaviour is worth remembering separately. At $s=\delta$ the divergence is logarithmic — the gentlest possible — which is why the paper can say that $Z_X(s)\to0$ as $s\downarrow\delta$ by monotone convergence rather than needing a rate. It also means the finite-area Brownian case ($s=\delta=1$) fails only just, and the renormalisation of §5 is correspondingly mild: a $\log\kappa$, cancelled against a simple zero.

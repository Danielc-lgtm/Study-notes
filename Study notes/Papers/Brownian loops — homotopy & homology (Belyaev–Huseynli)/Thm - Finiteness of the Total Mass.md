---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Selberg Zeta Criterion"
  - "Ext - Prime Geodesic Theorem"
  - "Def - Systole"
tags: [paper, zeta-functions, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | one of the four Bernstein functions treated; $s(\phi)$ its spectral parameter, $C(\phi)$ its constant |
| $s(\phi)$ | $=1$ for $\phi(\lambda)=\lambda$ and $\lambda^{\alpha/2}$; $=\tfrac12+\sqrt{\tfrac14+\kappa}$ for $\lambda+\kappa$ and shifted stable |
| $C(\phi)$ | $=1$ (Brownian, killing); $=\alpha/2$ (stable, shifted stable) |
| $\delta$ | the [[Def - Critical Exponent\|critical exponent]] |
| $N_X$ | the counting function of [[Ext - Prime Geodesic Theorem\|(PGT)]] |
| $\ell_{\mathrm{sys}}$ | the [[Def - Systole\|systole]] |

---

# Type card

> [!abstract] Type card — Corollary 4.7
> **Given.**
> **(H1)** $\phi$ one of the four cases, with $\mu^\phi_X(\mathcal{C}_X(\gamma^m))=\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$, $L=m\ell_\gamma$, $s=s(\phi)$, $C=C(\phi)>0$.
> **(H2)** $s(\phi)>\delta$.
>
> **Produces.**
> $$\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)<\infty.\tag{41}$$
> Moreover the converse holds: at $s=\delta$ the sum **diverges**, and $Z_X(s)\to0$ as $s\downarrow\delta$.
>
> **Lets you.** Normalise the class masses into a probability measure. Without (41) there is no $\mathbb{P}_s$, and §6 does not start.

---

# Statement

> **Corollary 4.7 (finiteness).** Assume (H1). If $s(\phi)>\delta$ then (41) holds. If $s(\phi)\leq\delta$ the sum diverges.
>
> **In the finite-area case $\delta=1$:** a killing rate $\kappa>0$, equivalently $s(\kappa)>1$, is **necessary** to restore finiteness.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - Selberg Zeta Criterion\|Lem 4.2]] table | each of the four $\phi$ | (H1): the closed form with its $(C,s)$ |
| [[Def - Systole\|(F2)]] | $L\geq\ell_{\mathrm{sys}}$ | $\frac{e^{(1-s)L}}{e^L-1}\leq\frac{e^{-sL}}{1-e^{-\ell_{\mathrm{sys}}}}$ |
| $\sum_{m\geq1}x^m/m=-\log(1-x)$ | $x=e^{-s\ell_\gamma}$ | $\sum_m\mu^\phi_X\leq\frac{-C}{1-e^{-\ell_{\mathrm{sys}}}}\log(1-e^{-s\ell_\gamma})$ |
| keeping only $m=1$ | the same sum | $\sum_m\mu^\phi_X\geq Ce^{-s\ell_\gamma}$ |
| [[Ext - Prime Geodesic Theorem\|(PGT)(F1)]] | $\mathcal{P}_X$ | $\ell_\gamma\to\infty$, so $-\log(1-x)=x+O(x^2)$ applies |
| [[Ext - Prime Geodesic Theorem\|(PGT)(40)]] | $\int_0^Te^{-sR}\,\mathrm{d}N_X(R)$ | tail integrand $e^{-(s-\delta)R}/R$; converges iff $s>\delta$ |

---

# Proof

**Strategy.** Two steps. **Step 1** reduces the double sum to the single geodesic sum $\sum_\gamma e^{-s\ell_\gamma}$, by two-sided bounds. **Step 2** decides that sum by integrating by parts against $N_X$ and applying (PGT).

> [!note]- Proof (skippable)
> **Step 1 — summing over the iterates $m$.** For $L\geq\ell_{\mathrm{sys}}$ we have $e^L-1\geq(1-e^{-\ell_{\mathrm{sys}}})e^L$, hence $\frac{e^{(1-s)L}}{e^L-1}\leq\frac{e^{-sL}}{1-e^{-\ell_{\mathrm{sys}}}}$. With $x=e^{-s\ell_\gamma}$ and $\sum_{m\geq1}x^m/m=-\log(1-x)$,
> $$\sum_{m\geq1}\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)\leq\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}\sum_{m\geq1}\frac{e^{-sm\ell_\gamma}}{m}=-\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}\log\big(1-e^{-s\ell_\gamma}\big).$$
> Conversely, keeping only $m=1$, $\sum_{m\geq1}\mu^\phi_X(\mathcal{C}_X(\gamma^m))\geq C\frac{e^{(1-s)\ell_\gamma}}{e^{\ell_\gamma}-1}\geq Ce^{-s\ell_\gamma}$.
> Since $N_X(R)<\infty$ for every $R$, $\ell_\gamma\to\infty$ along $\mathcal{P}_X$; so $e^{-s\ell_\gamma}\to0$ and $-\log(1-x)=x+O(x^2)$ makes the upper bound asymptotic to $\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}e^{-s\ell_\gamma}$. Hence
> $$\text{(41)}\iff\sum_{\gamma\in\mathcal{P}_X}e^{-s\ell_\gamma}<\infty.\tag{42}$$
>
> **Step 2 — the geodesic sum via the counting function.** Integrating by parts on $[0,T]$, and using $N_X(R)=0$ for $R<\ell_{\mathrm{sys}}$,
> $$\sum_{\ell_\gamma\leq T}e^{-s\ell_\gamma}=\int_0^Te^{-sR}\,\mathrm{d}N_X(R)=e^{-sT}N_X(T)+s\int_0^Te^{-sR}N_X(R)\,\mathrm{d}R.$$
> By (PGT), $N_X(R)\asymp e^{\delta R}/R$ for large $R$, so the large-$R$ integrand is $e^{-(s-\delta)R}/R$ and
> $$\int^\infty\frac{e^{-(s-\delta)R}}{R}\,\mathrm{d}R\quad\begin{cases}\text{converges},&s>\delta,\\ \text{diverges like }\int^\infty\mathrm{d}R/R,&s=\delta,\\ \text{diverges},&s<\delta.\end{cases}$$
> For $s>\delta$ the boundary term $e^{-sT}N_X(T)\to0$, so (42) converges. For $s\leq\delta$ the integral term alone diverges. Finally, $-\log Z_X(s)$ increases to this divergent sum as $s\downarrow\delta$, so by monotone convergence $Z_X(s)\to0$ as $s\downarrow\delta$. $\;\square$

---

# What this assumes, and where to climb

- **(PGT)** — [[Ext - Prime Geodesic Theorem]]. **The one genuine gap in §4.** It is proved from the Selberg trace formula, which this note-set imports. Nothing else in §4 is unproved.
- **$\ell_{\mathrm{sys}}>0$** — [[Def - Systole|(F1)]]. Needed for Step 1's constant; fails on infinite-type surfaces with arbitrarily short geodesics.
- **The four closed forms** — [[Thm - Selberg Zeta Criterion]]. The corollary is stated only for the $\phi$ that satisfy (33); for a general Bernstein $\phi$, (H1) fails and the argument does not start.
- **The boundary case is decided by the $1/R$**, not by the exponential. This is why the statement is $s>\delta$ strictly.

---

# The dichotomy, tabulated

| $X$ | $\delta$ | $\phi(\lambda)=\lambda$ ($s=1$) | $\phi(\lambda)=\lambda+\kappa$, $\kappa>0$ ($s>1$) |
|---|---|---|---|
| infinite area | $<1$ | **finite**, $=-\log Z_X(1)$ | finite |
| finite area (closed, or with cusps) | $=1$ | **infinite** | finite, $=-\log Z_X(s)$ |

---

# Consumed by

- [[Constr - The Probability Measure on Free Homotopy Classes]] — (41) is its existence hypothesis
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] — the divergence in the finite-area Brownian case is what §5 renormalises
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — $\#\mathcal{L}^*_\lambda$ is Poisson with finite mean
- [[Ext - Exponential Formula for Poisson Point Processes\|(F2)]] — discharges its precondition (P3)
- [[§4 Zeta Identities and Finiteness of the Total Mass]] §4.2

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: mass per class decays like $e^{-s\ell_\gamma}$, classes proliferate like $e^{\delta\ell_\gamma}$, and the sum converges exactly when decay beats proliferation.** Everything else is bookkeeping — Step 1 shows the $m$-sum contributes only a constant factor, Step 2 shows the $\gamma$-sum is a prime-number-theorem comparison.
>
> The boundary case rewards a second look. If $N_X(R)$ were exactly $e^{\delta R}$ the sum $\sum_\gamma e^{-s\ell_\gamma}$ would behave like $\int e^{-(s-\delta)R}\,\mathrm{d}R$ and would be inconclusive at $s=\delta$ only in the sense of being infinite for a trivial reason. With the true asymptotic $e^{\delta R}/\delta R$ the tail is $\int^\infty\frac{\mathrm{d}R}{R}$ — divergent, but only just. So the failure at $s=\delta$ is logarithmic, and $Z_X(s)\to0$ rather than jumping.
>
> The consequence organises the rest of the paper. On an infinite-area surface everything is finite already and §6 applies verbatim with $\kappa=0$. On a finite-area surface — which includes every closed surface, the case one most wants — the Brownian total mass is infinite, and there are exactly two repairs: add killing, or renormalise. §5 is the second repair, and the zeta-regularised determinant is what the renormalised value turns out to be.

---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Marked Length Spectrum"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
tags: [paper, hyperbolic-geometry, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\mu_X(\mathcal{C}_X(\gamma))$ | $\in(0,\infty)$; Brownian mass of the primitive class of $\gamma$ |
| $\mu^\kappa_X$ | killing loop measure, $\kappa\geq-\tfrac14$ |
| $s$ | $=\tfrac12+\sqrt{\tfrac14+\kappa}\in[\tfrac12,\infty)$ — the **spectral parameter** |
| $\ell_\gamma$ | $\in(0,\infty)$; $L=m\ell_\gamma$ |
| $\mathrm{MLS}$ | the [[Def - Marked Length Spectrum\|marked length spectrum]]; $\mathrm{MLS}(\mathcal{C}_X(\gamma^m))=m\ell_\gamma$ |

---

# Type card

> [!abstract] Type card — Proposition 3.11
> **Given.**
> **(H1)** $\kappa\geq-\tfrac14$ fixed, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$.
> **(H2)** the masses $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ for all $\gamma\in\mathcal{P}_X$, $m\geq1$.
>
> **Produces.** For $\kappa=0$: an **explicit inversion** $\ell_\gamma=\log\big(1+1/\mu_X(\mathcal{C}_X(\gamma))\big)$. For general $\kappa$: **strict monotonicity** of $\ell_\gamma\mapsto\mu^\kappa_X(\mathcal{C}_X(\gamma))$, hence injectivity. Both for every $m\geq1$; so in either case the masses determine $\mathrm{MLS}$.
>
> **Lets you.** Regard the loop masses as a **lossless** encoding of the geodesic geometry — the probabilistic data throws away nothing $\mathrm{MLS}$ retains. [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] upgrades this to rigidity.

---

# Statement

> **Proposition 3.11.** Assume (H1),(H2).
> **(a)** For every $\gamma\in\mathcal{P}_X$,
> $$\ell_\gamma=\log\!\left(1+\frac{1}{\mu_X\big(\mathcal{C}_X(\gamma)\big)}\right).\tag{30}$$
> **(b)** For $\phi(\lambda)=\lambda+\kappa$ with $\kappa\geq-\tfrac14$, the map $\ell_\gamma\mapsto\mu^\kappa_X(\mathcal{C}_X(\gamma))$ is **strictly decreasing**, hence injective, hence determines $\ell_\gamma$.
> **(c)** Both hold for every $m\geq1$; so in either case the loop masses determine $\mathrm{MLS}$.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces\|Thm 3.5]] §3.1.1 | $\phi(\lambda)=\lambda$ | $\mu_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{1}{e^L-1}$ |
| [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces\|Thm 3.5]] §3.1.2 | $\phi(\lambda)=\lambda+\kappa$ | $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)L}}{e^L-1}$, eq. (26) |
| [[Def - Free Homotopy Class and Conjugacy Class Correspondence\|(F1)]] | a class | the pair $(\gamma,m)$; so the mass is a function of $(\ell_\gamma,m)$ **and nothing else** |

---

# Proof

**Strategy.** (a) invert $x\mapsto1/(e^x-1)$ directly. (b) compute $\frac{\mathrm{d}}{\mathrm{d}\ell_\gamma}\log\mu^\kappa_X$ and bound it above by $\tfrac12-1<0$, uniformly in $\kappa\geq-\tfrac14$.

> [!note]- Proof (skippable)
> **(a)** By §3.1.1, $\mu_X(\mathcal{C}_X(\gamma))=1/(e^{\ell_\gamma}-1)$. Solving: $e^{\ell_\gamma}-1=1/\mu_X(\mathcal{C}_X(\gamma))$, so $e^{\ell_\gamma}=1+1/\mu_X(\mathcal{C}_X(\gamma))$, and (30) follows.
>
> **(b)** By (26), $\mu^\kappa_X(\mathcal{C}_X(\gamma))=e^{(\frac12-\sqrt{\frac14+\kappa})\ell_\gamma}/(e^{\ell_\gamma}-1)$. Its logarithmic derivative in $\ell_\gamma$ is
> $$\frac{\mathrm{d}}{\mathrm{d}\ell_\gamma}\log\mu^\kappa_X\big(\mathcal{C}_X(\gamma)\big)=\Big(\tfrac12-\sqrt{\tfrac14+\kappa}\Big)-\frac{e^{\ell_\gamma}}{e^{\ell_\gamma}-1}\;<\;\tfrac12-1\;<\;0,$$
> since $\sqrt{\tfrac14+\kappa}\geq0$ bounds the first bracket by $\tfrac12$ (with equality exactly at $\kappa=-\tfrac14$), and $e^{\ell}/(e^{\ell}-1)>1$ for every $\ell>0$. Strictly decreasing $\Rightarrow$ injective.
>
> **(c)** For general $m$ replace $\ell_\gamma$ by $L=m\ell_\gamma$ and multiply by the positive constant $1/m$; neither affects (a) or (b). $\;\square$

---

# What this assumes, and where to climb

- **The mass formulas** — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]], §3.1.1 and §3.1.2, hence the whole §3 stack.
- **The indexing** — [[Def - Marked Length Spectrum]], [[Def - Free Homotopy Class and Conjugacy Class Correspondence]]: the proposition is a statement about a function on classes, and needs $\mathrm{MLS}(\mathcal{C}_X(\gamma^m))=m\ell_\gamma$.
- **The extended range $\kappa\in[-\tfrac14,0)$** — where $\phi(\lambda)=\lambda+\kappa$ is **not** Bernstein (Remark 3.7). Formula (26) still converges and makes analytic sense, and **the bound $\tfrac12-1<0$ was chosen to be uniform over exactly this range**: at $\kappa=-\tfrac14$ the first bracket attains its maximum $\tfrac12$.
- **No finiteness needed.** The proposition is class-by-class and says nothing about sums.

---

# Consumed by

- [[Thm - Loop Masses Determine the Hyperbolic Surface]] — the sole consumer
- [[§3 Decomposition over Homotopy Classes]] §3.4.1

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: the mass depends on the class only through $L$, and $L\mapsto e^{(1-s)L}/(e^L-1)$ is strictly decreasing because the $1/(e^L-1)$ decay always beats the $e^{(1-s)L}$ growth — by a margin of at least $\tfrac12$ in the logarithmic derivative.**
>
> For Brownian motion the function is $\ell\mapsto1/(e^\ell-1)$, manifestly a decreasing bijection $(0,\infty)\to(0,\infty)$: short geodesics carry large mass, long ones exponentially small, and the correspondence inverts in closed form. For killing there is a competition — the numerator $e^{(1-s)\ell}$ *grows* when $s<1$, i.e. $\kappa<0$ — so monotonicity must be checked, and the margin turns out comfortable.
>
> What makes any of it work is that the mass formula depends on the class only through $(\ell_\gamma,m)$ and on **nothing else about the surface** — no genus, no other geodesic, no global geometry. That is why the inversion is class-by-class rather than a global reconstruction problem.
>
> Contrast with §6.1: there the masses are *summed* into $-\log Z_X$ and normalised, and what is recoverable drops to the systole and its multiplicity. Aggregation costs information, and these two results bracket how much.

---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Marked Length Spectrum"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
tags: [paper, hyperbolic-geometry, loop-measures]
---

# Notation

- $\mu_X(\mathcal{C}_X(\gamma))$ — the Brownian loop mass of the primitive class of $\gamma\in\mathcal{P}_X$
- $\mu^\kappa_X$ — the killing loop measure, $\kappa\geq-\tfrac14$; $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ the spectral parameter
- $\ell_\gamma>0$ — the length of the primitive closed geodesic
- $L=m\ell_\gamma$; $\mathrm{MLS}$ — the [[Def - Marked Length Spectrum|marked length spectrum]]

---

# Type card

> [!abstract] Type card — Proposition 3.11
> **Given.** The masses $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ over all free homotopy classes, for a fixed $\kappa\geq-\tfrac14$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$.
>
> **Produces.** For $\kappa=0$, an **explicit inversion**: $\ell_\gamma = \log\big(1+1/\mu_X(\mathcal{C}_X(\gamma))\big)$, a closed-form recovery of the geodesic length from the mass. For general $\kappa$, **strict monotonicity** of the mass as a function of $\ell_\gamma$, hence injectivity and recovery in principle. Both hold for every $m\geq1$, so in either case the loop masses determine $\mathrm{MLS}$.
>
> **Lets you.** Regard the loop masses as a lossless encoding of the geodesic geometry — the probabilistic data throws away nothing that $\mathrm{MLS}$ retains. This is what [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] then upgrades to a rigidity statement.

---

# Statement

> **Proposition 3.11.** For every $\gamma\in\mathcal{P}_X$,
> $$\ell_\gamma = \log\left(1+\frac{1}{\mu_X\big(\mathcal{C}_X(\gamma)\big)}\right).\tag{30}$$
> For $\phi(\lambda)=\lambda+\kappa$ with $\kappa\geq-\tfrac14$, the mass $\mu^\kappa_X(\mathcal{C}_X(\gamma))$ is a strictly decreasing function of $\ell_\gamma$ and hence again determines it. Both statements hold for every $m\geq1$, so in either case the loop masses determine $\mathrm{MLS}$.

---

# Why it is true

The mass of a class is a function of one variable — the length of its geodesic — and that function is injective. That is the whole statement; the two halves differ only in how injectivity is established.

For **Brownian motion** the function is $\ell\mapsto1/(e^\ell-1)$, which is manifestly strictly decreasing on $(0,\infty)$ from $+\infty$ to $0$, and its inverse is elementary. So not only is the length determined, it is determined by a formula one can write down: **short geodesics carry large mass, long geodesics carry exponentially small mass, and the correspondence is a bijection onto $(0,\infty)$.**

For **killing at rate $\kappa$** the function is $\ell\mapsto e^{(1-s)\ell}/(e^\ell-1)$, and now there is a competition: the numerator $e^{(1-s)\ell}$ *grows* when $s<1$, that is when $\kappa<0$. So monotonicity is no longer obvious and has to be checked. The check is a logarithmic derivative, and the margin is comfortable: the derivative of $\log\mu^\kappa_X(\mathcal{C}_X(\gamma))$ in $\ell_\gamma$ is
$$\Big(\tfrac12-\sqrt{\tfrac14+\kappa}\Big) - \frac{e^{\ell_\gamma}}{e^{\ell_\gamma}-1},$$
and the second term exceeds $1$ always, while the first is at most $\tfrac12$ (attained at the extreme $\kappa=-\tfrac14$). So the derivative is bounded above by $\tfrac12-1<0$ uniformly in $\ell_\gamma$ and in $\kappa$.

**The mechanism in one line: the mass depends on the class only through $L$, and $L\mapsto e^{(1-s)L}/(e^L-1)$ is strictly decreasing because the $1/(e^L-1)$ decay always beats the $e^{(1-s)L}$ growth — by a margin of at least $\tfrac12$ in the logarithmic derivative.**

The reason the whole thing works is worth naming separately: **the mass formula of [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] depends on the class only through $(\ell_\gamma,m)$ and on nothing else about the surface.** No genus, no other geodesic, no global geometry. That is what makes the inversion class-by-class rather than a global reconstruction problem.

---

# Strategy

**Strategy.** For $\kappa=0$, invert the Brownian formula $\mu_X(\mathcal{C}_X(\gamma))=1/(e^{\ell_\gamma}-1)$ directly. For general $\kappa$, compute the logarithmic derivative in $\ell_\gamma$ and bound it above by $\tfrac12-1<0$.

> [!note]- Proof (skippable)
> By §3.1.1, $\mu_X(\mathcal{C}_X(\gamma))=1/(e^{\ell_\gamma}-1)$. Solving, $e^{\ell_\gamma}-1 = 1/\mu_X(\mathcal{C}_X(\gamma))$, hence $e^{\ell_\gamma}=1+1/\mu_X(\mathcal{C}_X(\gamma))$ and (30) follows by taking logarithms.
>
> By (26), $\mu^\kappa_X(\mathcal{C}_X(\gamma)) = e^{(\frac12-\sqrt{\frac14+\kappa})\ell_\gamma}/(e^{\ell_\gamma}-1)$. Its logarithmic derivative in $\ell_\gamma$ is
> $$\frac{\mathrm{d}}{\mathrm{d}\ell_\gamma}\log\mu^\kappa_X\big(\mathcal{C}_X(\gamma)\big) = \Big(\tfrac12-\sqrt{\tfrac14+\kappa}\Big) - \frac{e^{\ell_\gamma}}{e^{\ell_\gamma}-1} < \tfrac12 - 1 < 0,$$
> since $\sqrt{\tfrac14+\kappa}\geq0$ gives the first bracket $\leq\tfrac12$, and $e^{\ell}/(e^{\ell}-1)>1$ for every $\ell>0$. So the mass is strictly decreasing in $\ell_\gamma$, hence injective, hence determines $\ell_\gamma$.
>
> For general $m$ the same computations apply with $\ell_\gamma$ replaced by $L=m\ell_\gamma$ and an overall factor $1/m$, which is a positive constant in $L$. $\;\square$

---

# What this assumes, and where to climb

**The mass formulas** — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]], specifically its Brownian and killing specialisations §3.1.1 and §3.1.2. Everything upstream of that theorem is inherited: the decomposition, the Wang–Xue identity, the collapse lemma.

**The identification of the class with its geodesic length** — [[Def - Marked Length Spectrum]] and [[Def - Free Homotopy Class and Conjugacy Class Correspondence]]. The proposition is a statement about a function on classes, and it needs the classes to be indexed by $(\gamma,m)$ with $\mathrm{MLS}(\mathcal{C}_X(\gamma^m))=m\ell_\gamma$.

**The extended range $\kappa\geq-\tfrac14$** — see Remark 3.7 on [[§3 Decomposition over Homotopy Classes]]. For $\kappa\in[-\tfrac14,0)$ the function $\phi(\lambda)=\lambda+\kappa$ is not Bernstein, but the mass formula (26) continues to make analytic sense and the monotonicity computation is unaffected. The bound $\tfrac12-1<0$ was chosen to be uniform over exactly this range: at $\kappa=-\tfrac14$ the first bracket attains its maximum $\tfrac12$.

**No finiteness is needed.** The proposition is class-by-class and says nothing about sums.

---

# What consumes this

- [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] — the sole consumer: equality of masses gives equality of marked length spectra with the identity marking, which Otal–Croke upgrades to an isometry
- [[§3 Decomposition over Homotopy Classes]] §3.4.1

---

# Reading it against the rest of the paper

There is a striking parallel with §6.1 worth noticing. Here the *individual* masses are inverted to recover the *individual* geodesic lengths. In [[Thm - Concentration on Systolic Classes|§6.1]] the *sum* of the masses is inverted asymptotically to recover the *systole* and its multiplicity:
$$\ell_{\mathrm{sys}} = -\lim_{s\to\infty}\frac1s\log\big(-\log Z_X(s)\big).$$
Both are recovery statements, but at opposite ends of the aggregation: one uses the full function on classes, the other uses only the total mass, and gets less back — the shortest length rather than all of them. That contrast is the cleanest illustration in the paper of what normalising to a probability measure costs and what it buys.

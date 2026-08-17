---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Dirichlet-Form Loop Measure"
  - "Def - Subordinator and Subordination of a Semigroup"
  - "Constr - Assumption 2.3 (Strictly Increasing Subordinator)"
tags: [paper, probability, subordination, loop-measures]
---

# Notation

- $\phi$ — a [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]
- $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ — the [[Def - Subordinator and Subordination of a Semigroup|subordinate Dirichlet form]] on $L^2(X,\mathrm{vol}_g)$, with semigroup $e^{-t\phi(A)}$ and transition density $p^\phi(t,x,y)$
- $W^{t,\phi}_{x\to y}$ — the associated unnormalised bridge measure, of total mass $|W^{t,\phi}_{x\to y}|=p^\phi(t,x,y)$
- $\mu^{*,\phi}_X$, $\mu^\phi_X$ — the rooted and unrooted subordinate Brownian loop measures
- $\mu^\kappa_X$, $\mu^\alpha_X$ — the shorthand for $\mu^\phi_X$ when $\phi(\lambda)=\lambda+\kappa$ and $\phi(\lambda)=\lambda^{\alpha/2}$ respectively

---

# In plain language

This is [[Constr - The Dirichlet-Form Loop Measure|Definition 2.2]] applied to the subordinate form. Nothing is new; the page exists because the object is a *hypothesis* of essentially every theorem in §3 onwards, and a hypothesis should be a link.

The value of naming it is uniformity. Brownian motion, Brownian motion with killing, the $\alpha$-stable processes and the shifted $\alpha$-stable processes become four values of one parameter $\phi$, so [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] is proved once and the four cases are substitutions. Since the choice of $\phi$ enters the final formula only through the [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] $V_\phi$, "changing the process" and "changing one measure on $(0,\infty)$" are the same act.

---

# The construction

> **Definition 2.8 (subordinate Brownian loop measure).** Fix a Bernstein function $\phi$ and let $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ be the subordinate Dirichlet form on $L^2(X,\mathrm{vol}_g)$ of §2.3, with semigroup $e^{-t\phi(A)}$ and transition density $p^\phi(t,x,y)$; the associated bridge measures have total mass $|W^{t,\phi}_{x\to y}|=p^\phi(t,x,y)$. Applying Definition 2.2 to $(\mathcal{E}^\phi,\mathcal{F}^\phi)$, the **rooted, oriented, parametrised subordinate Brownian loop measure** on $\mathcal{C}^*_X$ is
> $$\mu^{*,\phi}_X := \int_0^\infty\frac{\mathrm{d}t}{t}\int_X W^{t,\phi}_{x\to x}\,\mathrm{d}\mathrm{vol}_g(x),$$
> and its pushforward to $\mathcal{C}_X$ is the **unrooted, oriented, unparametrised subordinate Brownian loop measure** $\mu^\phi_X$.

Two hypotheses are doing quiet work. The density $p^\phi$ exists by [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]. And the subordinate object is again a *regular symmetric* Dirichlet form, with the explicit expression (5) of §2.3, which is what makes Definition 2.2 applicable at all.

**The double integral.** Because $p^\phi$ is itself an average, $p^\phi(t,x,y)=\int_{[0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s)$, the mass of $\mu^{*,\phi}_X$ carries *two* integrals — one in the loop duration $t$, one in the subordination variable $s$. Since the outer variable $t$ appears nowhere except inside $\psi^\phi_t$, it can be integrated out first, and what remains is a single measure on $s$. That observation is [[Constr - The Weighted Potential Measure Vϕ|Definition 2.9]], and it is why §2.4 exists.

---

# Type card

> [!abstract] Type card — Definition 2.8 (subordinate Brownian loop measure)
> **Given.** A Bernstein function $\phi$ satisfying Assumption 2.3, and the subordinate Dirichlet form $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ on $L^2(X,\mathrm{vol}_g)$ with transition density $p^\phi$.
>
> **Produces.** A $\sigma$-finite measure $\mu^\phi_X$ on $\mathcal{C}_X$, of infinite total mass; for a jump process, a measure on càdlàg loops on which free homotopy classes are **not** measurable sets.
>
> **Lets you.** Treat the four processes of the paper as four instances of one object, so that every theorem of §3 and §7 is proved once; and — because $\phi$ reaches the final formula only through $V_\phi$ — reduce "change the process" to "substitute a different measure on $(0,\infty)$".

---

# Properties relied on later

**Restriction — retained**, inherited from [[Constr - The Dirichlet-Form Loop Measure]]: the part form of the subordinate process on an open subset is the form of the killed subordinate process. §3.4 uses this for the killing case.

**Conformal invariance — absent** for every nonlinear $\phi$. The obstruction is exact: $\phi(e^{-2\sigma}\Delta_{X,g})\neq e^{-2\sigma}\phi(\Delta_{X,g})$ unless $\phi(\lambda)=c\lambda$. This is why $X$ is treated as a Riemannian rather than a Riemann surface from §2.3 onward, and why §3.4's length-spectrum identity degenerates.

**Homotopy classes are not measurable in the jump case.** For $\nu\neq0$ the sample loops are càdlàg, have no free homotopy class, and admit no canonical lift. Every statement of the form $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ for a jump process is therefore to be read through [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]], on the marked space carrying the pair $(B,S)$.

**Notation shorthands used without comment later.** $\mu^\kappa_X := \mu^\phi_X$ for $\phi(\lambda)=\lambda+\kappa$ and $\mu^\alpha_X := \mu^\phi_X$ for $\phi(\lambda)=\lambda^{\alpha/2}$. The unadorned $\mu_X$ is the Brownian case $\phi(\lambda)=\lambda$, agreeing with [[Constr - The Brownian Loop Measure|Definition 2.1]].

---

# Consumed by

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] — the measure whose class mass is computed
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] — the same in three dimensions
- [[Thm - Poissonian Structure of Homotopy Classes|Proposition 3.8]] — used as the intensity of the loop soup, which requires only $\sigma$-finiteness
- [[Thm - Selberg Zeta Criterion|Lemma 4.2]] and [[Thm - Finiteness of the Total Mass|Corollary 4.7]] — the object summed over all classes
- [[Constr - The Probability Measure on Free Homotopy Classes]] — the killing case is normalised to a probability measure
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]] — parts (ii) and (iii) use $\mu^\kappa_X$ and $\mu^\alpha_X$

---

# Where this sits in my DAG

Sits directly above [[Constr - The Dirichlet-Form Loop Measure]] and [[Def - Subordinator and Subordination of a Semigroup]], contributing no new dependency of its own. Both of those reduce to anchors within one further step — *Functional Analysis* (🟢) for the form and functional calculus, *Advanced Probability* (🟢) and *SDEs* (🟢) for the process, the bridge measures and the disintegration.

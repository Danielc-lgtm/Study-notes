---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Dirichlet-Form Loop Measure"
  - "Ext - Phillips Subordination of Semigroups and Dirichlet Forms"
  - "Constr - Assumption 2.3 (Strictly Increasing Subordinator)"
tags: [paper, probability, subordination, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | Bernstein function satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)\|(A2.3)]] |
| $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ | the subordinate Dirichlet form on $L^2(X,\operatorname{vol}_g)$; generator $\phi(A)$ |
| $p^\phi$ | $(0,\infty)\times X\times X\to[0,\infty)$; $p^\phi(t,x,y)=\int_{[0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s)$ |
| $W^{t,\phi}_{x\to y}$ | measure on $D([0,t],X)$; $\lvert W^{t,\phi}_{x\to y}\rvert=p^\phi(t,x,y)$ |
| $\mu^{*,\phi}_X$ | $\sigma$-finite measure on $\mathcal{C}^*_X$ |
| $\mu^\phi_X$ | $:=q_*\mu^{*,\phi}_X$; $\sigma$-finite on $\mathcal{C}_X$; $\lvert\mu^\phi_X\rvert=\infty$ |
| $\mu^\kappa_X,\ \mu^\alpha_X,\ \mu_X$ | shorthands: $\phi(\lambda)=\lambda+\kappa$; $\phi(\lambda)=\lambda^{\alpha/2}$; $\phi(\lambda)=\lambda$ |

---

# Construction

> **Definition 2.8 (subordinate Brownian loop measure).** Apply [[Constr - The Dirichlet-Form Loop Measure|Definition 2.2]] to $(\mathcal{E}^\phi,\mathcal{F}^\phi)$:
> $$\mu^{*,\phi}_X := \int_0^\infty\frac{\mathrm{d}t}{t}\int_X W^{t,\phi}_{x\to x}\,\mathrm{d}\operatorname{vol}_g(x),\qquad \mu^\phi_X:=q_*\mu^{*,\phi}_X .$$

**Well-definedness.** Three inputs, each already discharged: $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ is regular symmetric by [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms|(PH)(C4)]]; $p^\phi$ exists by (PH)(C3) given [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|(A2.3)]]; the pushforward is [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure|(LJ)]].

> **(F1) The double integral.** Since $p^\phi$ is itself an average, $\mu^{*,\phi}_X$ carries **two** integrals — one in the loop duration $t$, one in the subordination variable $s$:
> $$\lvert\mu^{*,\phi}_X\rvert=\int_0^\infty\frac{\mathrm{d}t}{t}\int_X\int_{[0,\infty)}p^{\mathcal{E}}(s,x,x)\,\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}\operatorname{vol}_g(x).$$
> The variable $t$ occurs **only** inside $\psi^\phi_t$, so it can be integrated out first. That observation is [[Constr - The Weighted Potential Measure Vϕ|Definition 2.9]] and is why §2.4 exists.

---

# Type card

> [!abstract] Type card — Definition 2.8
> **Given.**
> **(H1)** $\phi$ Bernstein satisfying (A2.3).
> **(H2)** $(\mathcal{E},\mathcal{F})$ regular symmetric on $L^2(X,\operatorname{vol}_g)$ with density $p^{\mathcal{E}}$.
> **(H3)** the subordinator independent of the base process.
>
> **Produces.** $\mu^\phi_X$: a $\sigma$-finite measure on $\mathcal{C}_X$ with $\mu^\phi_X(\mathcal{C}_X)=\infty$. For a jump process, a measure on càdlàg loops on which free homotopy classes are **not** measurable.
>
> **Lets you.** Treat the four processes of the paper as four values of one parameter, so that every theorem of §3 and §7 is proved once; and, because $\phi$ reaches the final formulas only through $V_\phi$, reduce "change the process" to "substitute a different measure on $(0,\infty)$".

---

# Depends on

- [[Constr - The Dirichlet-Form Loop Measure]] — the construction being applied
- [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms]] — (C3),(C4) supply $p^\phi$ and $(\mathcal{E}^\phi,\mathcal{F}^\phi)$
- [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]] — without it, no $p^\phi$
- [[Def - Subordinator]] — (H3)

---

# Properties

**(P1) Restriction — retained**, inherited from [[Constr - The Dirichlet-Form Loop Measure|Definition 2.2]] via the part form of the subordinate process.

**(P2) Conformal invariance — absent** for every nonlinear $\phi$: $\phi(e^{-2\sigma}\Delta_{X,g})\neq e^{-2\sigma}\phi(\Delta_{X,g})$ unless $\phi(\lambda)=c\lambda$. *Consequence:* $X$ is Riemannian, not Riemann, from §2.3 on.

**(P3) Homotopy classes not measurable in the jump case.** Every statement $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ for $\nu\neq0$ is read through [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]], on the marked space carrying $(B,S)$.

**(P4) Notation.** $\mu^\kappa_X:=\mu^\phi_X$ for $\phi(\lambda)=\lambda+\kappa$; $\mu^\alpha_X:=\mu^\phi_X$ for $\phi(\lambda)=\lambda^{\alpha/2}$; unadorned $\mu_X$ is $\phi(\lambda)=\lambda$, agreeing with [[Constr - The Brownian Loop Measure|Definition 2.1]].

---

# Consumed by

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — the measure whose class mass is computed
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — same in $\mathbb{H}^3$
- [[Thm - Poissonian Structure of Homotopy Classes]] — as a Poisson intensity; needs only $\sigma$-finiteness
- [[Thm - Selberg Zeta Criterion]], [[Thm - Finiteness of the Total Mass]] — summed over all classes
- [[Constr - The Probability Measure on Free Homotopy Classes]] — the killing case, normalised
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] — parts (ii),(iii) use $\mu^\kappa_X$, $\mu^\alpha_X$

---

# Commentary

> [!note]- Commentary (skippable)
> The page exists because the object is a *hypothesis* of essentially every theorem from §3 onward, and a hypothesis should be a link rather than a phrase.
>
> Its value is uniformity: Brownian motion, Brownian motion with killing, and the two stable families become four values of one parameter $\phi$, and since the choice of $\phi$ enters the final formula only through $V_\phi$, "changing the process" and "changing one measure on $(0,\infty)$" are literally the same act. That is the architecture of the second half of the paper, and (F1) is where it starts.

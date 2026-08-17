---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - The Space of Unrooted Unparametrised Loops"
  - "Def - Unnormalised Bridge Measure by Disintegration"
  - "Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure"
tags: [paper, probability, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $(X,g)$ | complete orientable Riemannian surface; $\partial X$ possibly non-empty |
| $\Delta_X$ | $-\operatorname{div}_g\operatorname{grad}_g$; self-adjoint on $L^2(X,\operatorname{vol}_g)$, $\operatorname{spec}\subseteq[0,\infty)$ |
| $\operatorname{vol}_g$ | Riemannian volume measure on $X$; $\sigma$-finite |
| $p_X$ | $(0,\infty)\times X\times X\to(0,\infty)$; symmetric; density w.r.t. $\operatorname{vol}_g$; kernel of $e^{-t\Delta_X}$ |
| $W^t_{x\to x}$ | measure on $C([0,t],X)$; $\lvert W^t_{x\to x}\rvert=p_X(t,x,x)$ — **unnormalised** |
| $\mathcal{C}^*_X,\ \mathcal{C}_X$ | rooted / unrooted oriented loop spaces; $q:\mathcal{C}^*_X\to\mathcal{C}_X$ |
| $\mu^*_X$ | measure on $\mathcal{C}^*_X$; $\sigma$-finite, $\lvert\mu^*_X\rvert=\infty$ |
| $\mu_X$ | $:=q_*\mu^*_X$; measure on $\mathcal{C}_X$; $\sigma$-finite, $\mu_X(\mathcal{C}_X)=\infty$ |
| $\mathrm{d}t/t$ | multiplicative Haar measure on $(0,\infty)$; the unique $\lambda$-scaling-invariant measure up to constants |

**Conventions.** $\Delta_X\geq0$. Brownian motion at speed $2$: generator $-\Delta_X$. Dirichlet conditions on $\partial X$, so the process is killed on first hitting $\partial X$.

---

# Construction

> **Definition 2.1 (Brownian loop measure).** The **rooted** Brownian loop measure on $\mathcal{C}^*_X$ is
> $$\mu^*_X \;:=\; \int_0^\infty\frac{\mathrm{d}t}{t}\int_X W^t_{x\to x}\,\mathrm{d}\operatorname{vol}_g(x),\tag{2.1}$$
> and the **Brownian loop measure** is its pushforward to unrooted unparametrised oriented loops:
> $$\mu_X := q_*\mu^*_X .$$

**Well-definedness.** The pushforward requires $\mu^*_X$ to be $\sim$-invariant, which is [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure|(LJ)]] applied to $\mathcal{E}(u,u)=\int_X\lvert\nabla u\rvert^2$. Nothing else in (2.1) requires checking: $W^t_{x\to x}$ exists by [[Def - Unnormalised Bridge Measure by Disintegration|(D1),(D2)]], and both weights are $\sigma$-finite.

> **(M) Total mass.** $\ \displaystyle\lvert\mu^*_X\rvert=\int_0^\infty\frac{1}{t}\int_X p_X(t,x,x)\,\mathrm{d}\operatorname{vol}_g(x)\,\mathrm{d}t=\infty$, divergent at $t\downarrow0$: by [[Def - Transition Density and Heat Kernel|(F3)]], $p_X(t,x,x)\sim1/4\pi t$, so the integrand is $\asymp t^{-2}$ near $0$. **$\mu_X$ is $\sigma$-finite and not normalisable.**

---

# Type card

> [!abstract] Type card — Definition 2.1
> **Given.**
> **(H1)** $(X,g)$ a complete orientable Riemannian surface, Dirichlet conditions on $\partial X$.
> **(H2)** $p_X$ exists ([[Def - Transition Density and Heat Kernel|(D1)–(D3)]]); hence $\{W^t_{x\to y}\}$ exists.
> **(H3)** [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure|(LJ)]], so $q_*$ is well defined.
>
> **Produces.** $\mu_X$: a $\sigma$-finite measure on $\mathcal{C}_X$ with $\mu_X(\mathcal{C}_X)=\infty$. **Not** a probability measure and not normalisable.
>
> **Lets you.** Assign a mass to any measurable family of loops with no normalisation; use $\mu_X$ as a Poisson intensity ($\sigma$-finiteness is all that is required); and inherit (P1),(P2) below.

---

# Depends on

- [[Def - The Space of Unrooted Unparametrised Loops]] — the target $\mathcal{C}_X$ and $q$
- [[Def - Unnormalised Bridge Measure by Disintegration]] — $W^t_{x\to x}$, and $\lvert W^t_{x\to x}\rvert=p_X(t,x,x)$
- [[Def - Transition Density and Heat Kernel]] — existence of $p_X$; (F3) for (M)
- [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure]] — well-definedness of $q_*$
- 🟢 $\sigma$-finiteness ([[Def - σ-Finite Measure]]); Riemannian volume ([[Def - Riemannian Volume Form]])

---

# Properties

Only the two consumed later. Both imported: [[Ext - Lawler–Werner Restriction and Conformal Invariance]].

**(P1) Restriction.** $X'\subseteq X$ open $\implies\ \mathrm{d}\mu_{X'}(\eta)=\mathbf{1}_{\{\eta\subseteq X'\}}\,\mathrm{d}\mu_X(\eta)$.
*Consumed by:* [[Ext - Wang–Xue Length-Spectrum Identity]]; inherited by every Dirichlet-form loop measure.

**(P2) Conformal invariance.** $\mu_{X,e^{2\sigma}g}=\mu_{X,g}$ for all $\sigma\in C^\infty(X,\mathbb{R})$; hence $\mu_X$ depends only on $[g]$.
*Consumed by:* [[Ext - Wang–Xue Length-Spectrum Identity]], [[Thm - Polyakov's Formula via Brownian Loop Measure]] — **and nowhere else in the paper.**
*Fails for:* every nonlinear $\phi$, since $\phi(e^{-2\sigma}\Delta_{X,g})\neq e^{-2\sigma}\phi(\Delta_{X,g})$ unless $\phi(\lambda)=c\lambda$.

---

# Consumed by

- [[Constr - The Dirichlet-Form Loop Measure]] — generalises (2.1); keeps (P1), drops (P2)
- [[Constr - The Subordinate Brownian Loop Measure]] — (2.1) applied to $(\mathcal{E}^\phi,\mathcal{F}^\phi)$
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — as (H1), in Dirichlet-form generality
- [[Ext - Wang–Xue Length-Spectrum Identity]] — as (H1), using (P1) **and** (P2)
- [[Thm - Polyakov's Formula via Brownian Loop Measure]] — using (P2)
- [[Thm - Poissonian Structure of Homotopy Classes]] — using $\sigma$-finiteness only

---

# Commentary

> [!note]- Commentary (skippable)
> A loop, as a stochastic process hands it to you, comes with a duration and a basepoint; neither belongs to the geometric object, so both are integrated out. The basepoint costs $\int_X\mathrm{d}\operatorname{vol}_g$. The duration forces the weight $\mathrm{d}t/t$ — the multiplicative Haar measure — because that is the unique measure (up to scale) invariant under the rescalings $t\mapsto\lambda t$ that a duration ought to be indifferent to.
>
> The price is (M): infinite total mass, diverging at the small-$t$ end. That is not a defect to be repaired but a correct statement that a surface contains overwhelmingly many very small loops. What survives — $\sigma$-finiteness — is everything the paper needs: Tonelli applies, pushforwards make sense, and $\mu_X$ can serve as a Poisson intensity. What is lost is the phrase "pick a loop at random", and §4–§6 spend their effort earning it back on a sub-family whose mass is finite.
>
> (P2) is the property most worth watching, because its scope is narrower than it looks and the entire architecture of §7 turns on that.

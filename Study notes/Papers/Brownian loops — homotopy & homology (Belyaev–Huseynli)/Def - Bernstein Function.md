---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs: []
tags: [paper, probability, subordination]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | $(0,\infty)\to[0,\infty)$; $C^\infty$ |
| $\phi^{(n)}$ | the $n$-th derivative of $\phi$ |
| $a$ | $\in[0,\infty)$ — the killing rate; $a=\phi(0^+)$ |
| $b$ | $\in[0,\infty)$ — the drift; $b=\lim_{\lambda\to\infty}\phi(\lambda)/\lambda$ |
| $\nu$ | measure on $(0,\infty)$ — the Lévy measure; $\int_0^\infty(1\wedge s)\,\nu(\mathrm{d}s)<\infty$; **not** finite in general |
| $\alpha$ | $\in(0,2)$ — stability index; $\kappa\geq0$ — constant killing rate |
| $g_{\alpha/2}$ | density of the standard $\alpha/2$-stable law on $(0,\infty)$; $\int_0^\infty g_{\alpha/2}=1$ |
| $\eta^\alpha_t$ | $(0,\infty)\to(0,\infty)$, $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(st^{-2/\alpha})$; a probability density for each $t>0$ |

---

# Definition

> **Definition (Bernstein function).** $\phi:(0,\infty)\to[0,\infty)$ is a **Bernstein function** if
> **(D1)** $\phi\in C^\infty(0,\infty)$;
> **(D2)** $(-1)^{n-1}\phi^{(n)}(\lambda)\geq0$ for all $n\geq1$ and all $\lambda>0$.

**Gloss.** (D2) says $\phi'$ is completely monotone: $\phi'\geq0$, $\phi''\leq0$, $\phi'''\geq0$, alternating.

> **(F1) Consequences of (D2).** $\phi$ is non-decreasing ($n=1$) and concave ($n=2$); $\phi(0^+)$ exists in $[0,\infty)$; $\lim_{\lambda\to\infty}\phi(\lambda)/\lambda$ exists in $[0,\infty)$.
>
> **(F2) Representation.** (D1),(D2) $\iff$ $\phi$ has the [[Ext - Lévy–Khintchine Representation for Bernstein Functions|Lévy–Khintchine form (LK)]] with a unique triple $(a,b,\nu)$.
>
> **(F3) Reading the triple.** $a$ = constant killing rate; $b$ = deterministic drift of the clock; $\nu$ = jump intensity of the clock. In particular $\nu\neq0\implies$ the subordinate process **jumps**, even if the base process is a diffusion.

---

# Type card

> [!abstract] Type card — Bernstein function
> **Given.** **(H1)** $\phi:(0,\infty)\to[0,\infty)$ with (D1),(D2).
>
> **Produces.** A unique triple $(a,b,\nu)\in[0,\infty)\times[0,\infty)\times\mathcal{M}((0,\infty))$ with $\int(1\wedge s)\,\nu(\mathrm{d}s)<\infty$; equivalently, a [[Def - Subordinator|subordinator]] with Laplace exponent $\phi$.
>
> **Lets you.** Parametrise the paper's whole family of processes by one function, so that §3–§7 are proved once and the special cases are substitutions.

---

# Depends on

- [[Ext - Lévy–Khintchine Representation for Bernstein Functions]] — for (F2)
- 🟢 completely monotone functions; Laplace transforms — *Advanced Probability*

---

# Checks

The four that carry the paper.

| $\phi(\lambda)$ | $(a,b,\nu)$ | process | $\psi^\phi_t$ |
|---|---|---|---|
| $\lambda$ | $(0,1,0)$ | Brownian motion | $\delta_t$ |
| $\lambda+\kappa$, $\kappa>0$ | $(\kappa,1,0)$ | Brownian with killing | $e^{-\kappa t}\delta_t$ |
| $\lambda^{\alpha/2}$, $\alpha\in(0,2)$ | $(0,0,\nu_\alpha)$ | $\alpha$-stable, pure jump | $\eta^\alpha_t(s)\,\mathrm{d}s$ |
| $(\lambda+\kappa)^{\alpha/2}$ | composition of the two above | shifted $\alpha$-stable | $e^{-\kappa s}\eta^\alpha_t(s)\,\mathrm{d}s$ |

with $\displaystyle\nu_\alpha(\mathrm{d}s)=\frac{\alpha/2}{\Gamma(1-\alpha/2)}\,s^{-1-\alpha/2}\,\mathrm{d}s$, so $\nu_\alpha(0,\infty)=\infty$. The framework also covers gamma, inverse Gaussian and relativistic stable subordinators; the paper computes none of them.

**Non-instance (fails D2 at $n=0$, so to speak).** $\phi(\lambda)=\lambda+\kappa$ with $\kappa<0$ is **not** Bernstein: $\phi<0$ near $\lambda=0$, so $\phi$ does not map into $[0,\infty)$, and there is no increasing Lévy process with this exponent. **The paper nevertheless uses $\kappa\in[-\tfrac14,0)$**, on the grounds that the mass *formula* (26) still converges and makes analytic sense. The cutoff is not arbitrary: $\kappa\geq-\tfrac14$ is exactly the condition for $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ to be real, and $\kappa=-\tfrac14$ gives $s=\tfrac12=\inf\operatorname{spec}\Delta_{\mathbb{H}^2}$ in $L^2$. See Remark 3.7.

**Non-instance (Bernstein but excluded).** A **compound Poisson** subordinator: $b=0$, $\nu(0,\infty)<\infty$, so $\phi(\lambda)=\int_0^\infty(1-e^{-\lambda s})\,\nu(\mathrm{d}s)$ satisfies (D1),(D2). But $\psi^\phi_t(\{0\})=e^{-\nu(0,\infty)t}>0$, so the subordinate semigroup has an atom on the diagonal and **no transition density** exists. Excluded by [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|(A2.3)]].

---

# Used at

- [[Def - Subordinator]] — $\phi$ is the Laplace exponent
- [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]] — (A2.3) is a condition on $(b,\nu)$
- [[Constr - The Weighted Potential Measure Vϕ]] — $V_\phi$ is built from $\{\psi^\phi_t\}$
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]], [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — as (H1)
- [[Thm - Finiteness of the Total Mass]] — quantified over the four rows above

---

# Commentary

> [!note]- Commentary (skippable)
> (D2) looks arbitrary until (F2): every such $\phi$ is $a+b\lambda+\int(1-e^{-\lambda s})\nu(\mathrm{d}s)$, and the three pieces have meanings — the clock stops at rate $a$, runs at speed $b$, and jumps by $s$ at rate $\nu(\mathrm{d}s)$. So reading a Bernstein function is reading a recipe for a random clock, and the sign-alternation is what "increasing process built from those three ingredients" looks like from the Laplace side.
>
> Reading the table against (F3) is the fastest way to internalise §2.3. Row 1: no killing, unit drift, no jumps — nothing happens, $\psi^\phi_t=\delta_t$. Row 2: same clock, killed, so $\lvert\psi^\phi_t\rvert=e^{-\kappa t}<1$. Row 3: **no drift**, so the clock advances *only* by jumps, and $\nu_\alpha$ infinite means infinitely many per unit time — hence a pure-jump process from a diffusion. Row 4 exists only to break the scale invariance that makes row 3 degenerate.

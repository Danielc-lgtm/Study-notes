---
type: example
subject: probability
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
tags: [paper, brownian-loops, levy-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Example 2.5"
---

# Notation

$\phi:(0,\infty)\to[0,\infty)$ a Bernstein function; $(a,b,\nu)$ its Lévy–Khintchine data ($a\ge 0$ killing rate, $b\ge 0$ drift, $\nu$ Lévy measure on $(0,\infty)$); $\psi^\phi_t$ the associated subordinator's law on $[0,\infty)$; $\alpha\in(0,2)$ a stability parameter; $\kappa\ge 0$ a killing constant. $\Gamma$ denotes the classical Gamma function ($\Gamma(z)=\int_0^\infty s^{z-1}e^{-s}\,ds$), *not* the paper's Fuchsian group.

> [!recall]- Bernstein function $\phi$, Lévy–Khintchine data $(a,b,\nu)$, subordinator law $\psi^\phi_t$
> **Formally:** $\phi\in C^\infty$ non-negative with $(-1)^{n-1}\phi^{(n)}\ge 0$; equivalently $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda s})\,\nu(ds)$ with $a,b\ge 0$, $\int(1\wedge s)\,\nu(ds)<\infty$. The associated subordinator $S_t$ has $\mathbb{E}[e^{-\lambda S_t}]=e^{-t\phi(\lambda)}$ and law $\psi^\phi_t$.
> **In words:** $\phi$ is exactly the class of Laplace exponents of increasing random clocks. $(a,b,\nu)$ decompose the clock: kill at rate $a$, drift smoothly at rate $b$, jump by $s$ at Poisson rate $\nu(ds)$.
> **Concretely:** $\phi(\lambda)=\lambda$ ↔ trivial clock $S_t=t$, $\psi^\phi_t=\delta_t$. $\phi(\lambda)=\lambda+\kappa$ ↔ $\psi^\phi_t=e^{-\kappa t}\delta_t$. See [[Def - Bernstein Function, Subordinator, and Subordination]].

> [!recall]- $\alpha/2$-stable subordinator and its density $\eta^\alpha_t(s)$
> **Formally:** the $\beta$-stable subordinator (with $\beta\in(0,1)$) has Bernstein function $\phi(\lambda)=\lambda^\beta$, Lévy measure $\nu_\beta(ds)=\frac{\beta}{\Gamma(1-\beta)}s^{-1-\beta}\,ds$ on $(0,\infty)$, and law $\psi^\phi_t(ds)=g_\beta(s;t)\,ds$ on $(0,\infty)$ where $g_\beta$ is the (Zolotarev) stable density. Writing $g_\beta(u):=g_\beta(u;1)$ for the standard $\beta$-stable density (the density of $S_1$), the scaling relation $S_t\overset{d}{=}t^{1/\beta}S_1$ gives $g_\beta(s;t)=t^{-1/\beta}g_\beta(s\,t^{-1/\beta})$. With $\beta=\alpha/2$ the paper writes $\eta^\alpha_t(s):=g_{\alpha/2}(s;t)=t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})$.
> **In words:** a heavy-tailed random clock that jumps by $s$ at Poisson intensity $\propto s^{-1-\beta}\,ds$; its density $g_\beta(u)$ is smooth and supported on $(0,\infty)$, and rescales cleanly with $t$ via $t^{1/\beta}$. Only $\beta=1/2$ has a closed-form density (the Lévy distribution $\frac{1}{2\sqrt\pi}s^{-3/2}e^{-1/(4s)}$).
> **Concretely:** the $1/2$-stable ($\alpha=1$) subordinator has density $g_{1/2}(s;t)=\frac{t}{2\sqrt\pi}s^{-3/2}e^{-t^2/(4s)}$; subordinating planar Brownian motion by it produces the Cauchy process on $\mathbb{R}^2$. The $\alpha/2=1$ (i.e. $\alpha=2$) boundary is not a stable subordinator — it degenerates to the trivial clock — recovering Brownian motion. See [BBK+09, Ch. 5] for the general $g_\beta$.

---

# Statement

> **Example (Belyaev–Huseynli 2.5 — Important Bernstein functions).** The four Bernstein functions playing a role in this paper are tabulated below with their Lévy–Khintchine data $(a,b,\nu)$ and subordinator law $\psi^\phi_t$. The framework also applies to gamma, inverse-Gaussian, and relativistic-stable subordinators, which are Bernstein.
>
> | # | Resulting process | $\phi(\lambda)$ | $(a,b,\nu)$ | Law $\psi^\phi_t$ |
> |---|---|---|---|---|
> | 1 | Brownian motion | $\lambda$ | $(0,1,0)$ | $\delta_t$ |
> | 2 | Brownian with killing ($\kappa>0$) | $\lambda+\kappa$ | $(\kappa,1,0)$ | $e^{-\kappa t}\,\delta_t$ |
> | 3 | $\alpha$-stable ($\alpha\in(0,2)$) | $\lambda^{\alpha/2}$ | $(0,0,\nu_\alpha)$ | $\eta^\alpha_t(s)\,ds$ |
> | 4 | Shifted $\alpha$-stable ($\alpha\in(0,2),\kappa\ge 0$) | $(\lambda+\kappa)^{\alpha/2}$ | (see below) | $e^{-\kappa s}\eta^\alpha_t(s)\,ds$ |
>
> Here $\nu_\alpha(ds)=\frac{\alpha/2}{\Gamma(1-\alpha/2)}s^{-1-\alpha/2}\,ds$ is the $\alpha/2$-stable Lévy measure and $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})$ is the density of the $\alpha/2$-stable subordinator at time $t$. Cases 1–3 are the paper's Example 2.5; case 4 (the shifted $\alpha$-stable) is introduced formally in §3.1.4 but sits naturally with the other three and is included here.

---

# Computation

**Case 1: Brownian, $\phi(\lambda)=\lambda$.** Read off $(a,b,\nu)=(0,1,0)$ from the Lévy–Khintchine formula: $\phi=0+1\cdot\lambda+\int(1-e^{-\lambda s})\cdot 0\,ds=\lambda$. Check: $\mathbb{E}[e^{-\lambda S_t}]=e^{-t\lambda}$, which is the Laplace transform of $\delta_t$, giving $\psi^\phi_t=\delta_t$. So the "clock" is deterministic, $S_t=t$; **subordinating any process by this clock does nothing**, $p^\phi=p^E$ and $\mu^\phi_X=\mu^E_X$.

**Case 2: Brownian with killing, $\phi(\lambda)=\lambda+\kappa$.** From Lévy–Khintchine: $\lambda+\kappa=\kappa+1\cdot\lambda+0$, so $(a,b,\nu)=(\kappa,1,0)$. Check: $\mathbb{E}[e^{-\lambda S_t}]=e^{-t(\lambda+\kappa)}=e^{-\kappa t}e^{-\lambda t}$, the Laplace transform of $e^{-\kappa t}\delta_t$, giving $\psi^\phi_t=e^{-\kappa t}\delta_t$ (a sub-probability measure of total mass $e^{-\kappa t}$). The subordinate transition density is
$$p^\phi(t,x,y)=\int_{[0,\infty)}p^E(s,x,y)\,\psi^\phi_t(ds)=e^{-\kappa t}p^E(t,x,y),$$
i.e. the ambient kernel *exponentially tilted*. The process is **Brownian motion killed at exponential rate $\kappa$**: it moves as ordinary Brownian motion, but at each instant it has probability $e^{-\kappa t}$ of surviving to time $t$. (Full unpacking of the subordinate Dirichlet form: [[Ex - The Subordinate Form of Brownian Motion with Killing]].)

**Case 3: $\alpha$-stable, $\phi(\lambda)=\lambda^{\alpha/2}$, $\alpha\in(0,2)$.** Verify $\phi$ is Bernstein by inspection: $\phi'(\lambda)=\frac{\alpha}{2}\lambda^{\alpha/2-1}>0$; $\phi''(\lambda)=\frac{\alpha}{2}(\frac{\alpha}{2}-1)\lambda^{\alpha/2-2}<0$ (since $\alpha/2<1$); each further derivative alternates in sign. Its Lévy–Khintchine representation (a classical computation via the Frullani-type integral $\lambda^\beta=\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty(1-e^{-\lambda s})s^{-1-\beta}\,ds$ for $\beta\in(0,1)$, with $\beta=\alpha/2$) gives $(a,b,\nu)=(0,0,\nu_\alpha)$ with $\nu_\alpha(ds)=\frac{\alpha/2}{\Gamma(1-\alpha/2)}s^{-1-\alpha/2}\,ds$. Its subordinator law has the scaling form $\psi^\phi_t(ds)=\eta^\alpha_t(s)\,ds=t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})\,ds$ on $(0,\infty)$. The operator is the **fractional Laplacian** $\Delta_X^{\alpha/2}$ (defined by the spectral theorem: $\Delta_X^{\alpha/2}=\phi(\Delta_X)$), and the subordinate process is **pure-jump càdlàg** — the $\alpha$-stable process on $X$ — for every $\alpha\in(0,2)$. (The boundary $\alpha=2$ recovers case 1: Brownian motion.) See [[Ex - The Subordinate Form of the alpha-Stable Process]].

**Case 4: Shifted $\alpha$-stable, $\phi(\lambda)=(\lambda+\kappa)^{\alpha/2}$, $\alpha\in(0,2),\kappa\ge 0$.** Bernstein by composition: $\lambda\mapsto\lambda+\kappa$ is Bernstein (trivially: linear plus killing), $u\mapsto u^{\alpha/2}$ is Bernstein on $(0,\infty)$ (case 3), and Bernstein functions are closed under composition ($\phi_1\circ\phi_2$ is Bernstein whenever $\phi_2$ is Bernstein and $\phi_1$ is a *complete* Bernstein function — see [SSV12, Ch. 7]; $u^{\alpha/2}$ is complete Bernstein for $\alpha/2\in(0,1)$). Its subordinator law is an **exponential tilt** of the $\alpha$-stable case:
$$e^{-t(\lambda+\kappa)^{\alpha/2}} \;=\; \int_0^\infty e^{-u(\lambda+\kappa)}\eta^\alpha_t(u)\,du \;=\; \int_0^\infty e^{-\lambda s}\,e^{-\kappa s}\eta^\alpha_t(s)\,ds,$$
so $\psi^\phi_t(ds)=e^{-\kappa s}\eta^\alpha_t(s)\,ds$. The operator is $(\Delta_X+\kappa)^{\alpha/2}$, i.e. the fractional Laplacian applied to the *shifted* Laplacian. This case breaks the pure scale-invariance of the $\alpha$-stable case (the killing $e^{-\kappa s}$ tilt is the mechanism) and is the setting in which §3.1.4 delivers a non-trivial closed-form mass computation.

**The framework's reach.** The paper notes that gamma, inverse-Gaussian, and relativistic-stable subordinators are also covered:
- **Gamma:** $\phi(\lambda)=\log(1+\lambda)$ with $\nu(ds)=s^{-1}e^{-s}\,ds$; the subordinator is the gamma process.
- **Inverse Gaussian:** $\phi(\lambda)=\sqrt{2\lambda+m^2}-m$ ($m\ge 0$), a subclass of complete Bernstein functions.
- **Relativistic stable:** $\phi(\lambda)=(\lambda+m^{2/\alpha})^{\alpha/2}-m$, a shifted-and-recentred stable.

All satisfy Assumption 2.3 (infinite Lévy activity) and so fit the paper's [[Def - Subordinate Brownian Loop Measure|subordinate loop measure]] machinery.

---

# Calibration

The four cases stack up as a small ladder of complications:

| Case | Introduces | Preserves |
|---|---|---|
| 1 (Brownian) | — | continuity, scale-invariance |
| 2 (killing) | exponential mass decay | continuity |
| 3 ($\alpha$-stable) | jumps, non-locality | scale-invariance |
| 4 (shifted $\alpha$-stable) | jumps, non-locality, mass decay | — |

Case 3 is the essential jump case; case 4 is the essential jump-plus-killing case where the killing breaks the paper's scale-invariance "trap" (see §3.1.3) and lets the homotopy-class decomposition carry non-trivial geometric information.

**A calibration check.** Verify the Lévy measure of case 3 has infinite total mass: $\nu_\alpha(0,\infty)=\frac{\alpha/2}{\Gamma(1-\alpha/2)}\int_0^\infty s^{-1-\alpha/2}\,ds=+\infty$ (the singularity at $s=0$ diverges since $-1-\alpha/2<-1$). So case 3 satisfies [[Remark - Non-Compound-Poisson Assumption on the Bernstein Function|Assumption 2.3]] via the "$\nu(0,\infty)=\infty$" branch; cases 1, 2, 4 satisfy it via $b=1>0$ or the same infinite-Lévy-activity.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.3.1]] as the paper's working list of Bernstein functions. The subordinate Dirichlet forms for cases 2 and 3 are then unpacked in [[Ex - The Subordinate Form of Brownian Motion with Killing|Example 2.6]] and [[Ex - The Subordinate Form of the alpha-Stable Process|Example 2.7]]; the weighted potential measures for all four cases are computed in [[Ex - Weighted Potential Measures of the Paper's Bernstein Functions|Example 2.10]]; the free-homotopy-class masses in §3.1 are evaluated case-by-case for each of these four Bernstein functions. The shifted-$\alpha$-stable case is the one where §3.1.4 produces the paper's most interesting closed-form loop-class mass.

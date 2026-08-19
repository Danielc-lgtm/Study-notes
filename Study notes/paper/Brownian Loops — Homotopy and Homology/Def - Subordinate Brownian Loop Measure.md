---
type: definition
subject: probability-geometry
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Dirichlet Form Loop Measure"
  - "Def - Dirichlet Form and its Operator and Semigroup"
tags: [paper, brownian-loops, levy-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 2.8"
---

# Notation

$(X,g)$ a Riemannian surface with area measure $\operatorname{vol}_g$; $(\mathcal E,\mathcal F)$ a regular symmetric Dirichlet form on $L^2(X,\operatorname{vol}_g)$ with operator $A$, semigroup $e^{-tA}$, and transition density $p^E$. $\phi:(0,\infty)\to[0,\infty)$ a Bernstein function with Lévy–Khintchine data $(a,b,\nu)$ and subordinator law $\psi^\phi_t$ (see the recall). The **subordinate Dirichlet form** $(\mathcal E^\phi,\mathcal F^\phi)$ on $L^2(X,\operatorname{vol}_g)$ has operator $\phi(A)$ and transition density
$$p^\phi(t,x,y) \;=\; \int_{[0,\infty)} p^E(s,x,y)\,\psi^\phi_t(ds).$$
Its bridge measures $\mathbb{W}^{t,\phi}_{x\to y}$ on càdlàg paths $D([0,t],X)$ have mass $|\mathbb{W}^{t,\phi}_{x\to y}|=p^\phi(t,x,y)$. Rooted càdlàg loop space $C^*_X$, unrooted quotient $C_X$, as in the previous definition. The paper's **Assumption 2.3** ($b>0$ or $\nu(0,\infty)=\infty$) is in force, ensuring $\psi^\phi_t(\{0\})=0$ and so that $p^\phi$ is genuinely a density (no atom at $s=0$ in the average). See [[Remark - Non-Compound-Poisson Assumption on the Bernstein Function]].

> [!recall]- Bernstein function $\phi$, subordinator $S_t$ (law $\psi^\phi_t$), and subordination
> **Formally:** $\phi:(0,\infty)\to[0,\infty)$ is a **Bernstein function** if $\phi\in C^\infty$ with $(-1)^{n-1}\phi^{(n)}\ge 0$ for all $n\ge 1$; equivalently, $\phi$ has the **Lévy–Khintchine representation** $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda s})\,\nu(ds)$ with $a,b\ge 0$ and $\int_0^\infty (1\wedge s)\,\nu(ds)<\infty$. A **subordinator** $(S_t)_{t\ge 0}$ is an increasing Lévy process (independent stationary increments, $S_0=0$, non-decreasing paths, possibly killed at constant rate) with Laplace transform $\mathbb{E}[e^{-\lambda S_t}]=e^{-t\phi(\lambda)}$; $\psi^\phi_t$ is its law on $[0,\infty)$. **Subordinating** a process $B_r$ by an independent $S_t$ means observing it at the random clock: $Y_t := B_{S_t}$.
> **In words:** $\phi$ is exactly the class of Laplace exponents of increasing "random clocks". A subordinator only moves forward, sometimes with jumps (skipping ahead). Observing the underlying process at those clock times gives a new process that jumps whenever the clock jumped. The three Lévy–Khintchine ingredients have direct meaning: drift $b$ says the clock advances at rate $b$ smoothly; Lévy measure $\nu(ds)$ says the clock jumps ahead by size $s$ at Poisson intensity $\nu(ds)$; killing rate $a$ says the clock dies at rate $a$.
> **Concretely:** the identity $\phi(\lambda)=\lambda$ (data $a=0,b=1,\nu=0$) gives $\mathbb{E}[e^{-\lambda S_t}]=e^{-t\lambda}$, the Laplace transform of $\delta_t$: so $S_t=t$ deterministically and subordination does nothing. $\phi(\lambda)=\lambda+\kappa$ ($a=\kappa,b=1,\nu=0$) gives $\psi^\phi_t=e^{-\kappa t}\delta_t$: the clock is still $t$ but with probability $e^{-\kappa t}$ of surviving, i.e. Brownian motion killed at rate $\kappa$. $\phi(\lambda)=\lambda^{1/2}$ (Lévy measure $\nu(ds)=\frac{1}{2\sqrt\pi}s^{-3/2}\,ds$) gives the $1/2$-stable subordinator with density $\psi^\phi_t(ds)=\frac{t}{2\sqrt\pi}s^{-3/2}e^{-t^2/(4s)}\,ds$ on $(0,\infty)$; subordinating Brownian motion by this yields the Cauchy process. See [[Def - Bernstein Function, Subordinator, and Subordination]].

> [!recall]- Subordinate Dirichlet form $(\mathcal E^\phi,\mathcal F^\phi)$, operator $\phi(A)$, kernel $p^\phi$
> **Formally:** given the regular symmetric Dirichlet form $(\mathcal E,\mathcal F)$ with operator $A$ and semigroup $e^{-sA}$, and a Bernstein $\phi$ with independent subordinator law $\psi^\phi_t$, the **subordinate semigroup** is $e^{-t\phi(A)}=\int_{[0,\infty)}e^{-sA}\,\psi^\phi_t(ds)$, its generator is $-\phi(A)$ where $\phi(A)=aI+bA+\int_0^\infty(I-e^{-sA})\,\nu(ds)$ (spectral calculus applied to $\phi$), and its transition density is $p^\phi(t,x,y)=\int_{[0,\infty)}p^E(s,x,y)\,\psi^\phi_t(ds)$. The associated **subordinate Dirichlet form** on $L^2(X,\operatorname{vol}_g)$ is $\mathcal E^\phi(u,u)=a\|u\|^2+b\,\mathcal E(u,u)+\int_0^\infty(\|u\|^2-\langle e^{-sA}u,u\rangle)\,\nu(ds)$, with domain $\mathcal F^\phi=\{u\in L^2:\mathcal E^\phi(u,u)<\infty\}$; it is regular symmetric and its associated Hunt process is again $\operatorname{vol}_g$-symmetric.
> **In words:** run the original process on the random clock; the new semigroup is the *average* of the old one against the clock's law. Its heat kernel is the same average of $p^E(s,x,y)$ against $\psi^\phi_t(ds)$. The new generator is $\phi$ applied to the old generator by the spectral theorem — literally the same function of an operator.
> **Concretely:** with $A=\Delta_X$ and $\phi(\lambda)=\lambda^{\alpha/2}$, the subordinate operator is the **fractional Laplacian** $\Delta_X^{\alpha/2}$, and $p^\phi_t(x,y)=\int_0^\infty p^E(s,x,y)\,\eta^\alpha_t(s)\,ds$ with $\eta^\alpha_t$ the $\alpha/2$-stable density — a genuine convolution of the diffusion heat kernel against the stable subordinator's density. With $\phi(\lambda)=\lambda+\kappa$ the subordinator is $\psi^\phi_t=e^{-\kappa t}\delta_t$ and $p^\phi(t,x,y)=e^{-\kappa t}p^E(t,x,y)$: the pure exponential tilt of the original kernel. See [[Def - Bernstein Function, Subordinator, and Subordination]] and [[Def - Dirichlet Form and its Operator and Semigroup]].

> [!recall]- Bridge measure $\mathbb{W}^{t,\phi}_{x\to y}$ (mass $p^\phi(t,x,y)$)
> **Formally:** disintegrating the subordinate process's law $\mathbb{W}^{t,\phi}_x$ over the endpoint yields bridge measures $\mathbb{W}^{t,\phi}_{x\to y}$ on $D([0,t],X)$ with $|\mathbb{W}^{t,\phi}_{x\to y}|=p^\phi(t,x,y)$. Assumption 2.3 ensures $\psi^\phi_t$ has no atom at $0$, so $p^\phi$ is a genuine density and this disintegration exists.
> **In words:** exactly as with Brownian motion, but for the subordinate process. The bridge weighs càdlàg (possibly-jump) paths starting at $x$ and ending at $y$, scaled so the total weight equals $p^\phi(t,x,y)$.
> **Concretely:** for killing ($\phi=\lambda+\kappa$), $\mathbb{W}^{t,\phi}_{x\to y}=e^{-\kappa t}\,\mathbb{W}^{t,E}_{x\to y}$ — literally the ambient bridge scaled by the survival probability. For $\alpha$-stable ($\phi=\lambda^{\alpha/2}$), the bridge is genuinely different from the Brownian one: its paths jump countably often. See [[Def - Disintegration and the Bridge Measure]].

> [!recall]- The multiplicative Haar measure $\frac{dt}{t}$
> **Formally:** the scale-invariant $\sigma$-finite measure on $(0,\infty)$ satisfying $\int_{\lambda a}^{\lambda b}\frac{dt}{t}=\int_a^b\frac{dt}{t}$; infinite total mass, finite on compacts of $(0,\infty)$.
> **In words:** the unique duration-blind weighting on positive reals.
> **Concretely:** $\int_1^{e^n}\frac{dt}{t}=n$; the change $u=\log t$ turns it into Lebesgue $du$. See [[Def - Signed and Infinite Measures for Loop Measures]].

---

# Statement

> **Definition (subordinate Brownian loop measure; Belyaev–Huseynli Def. 2.8).** Fix a Bernstein function $\phi$ satisfying Assumption 2.3, and let $(\mathcal E^\phi,\mathcal F^\phi)$ be the subordinate Dirichlet form on $L^2(X,\operatorname{vol}_g)$ with transition density $p^\phi$ and bridge measures $\mathbb{W}^{t,\phi}_{x\to y}$. Applying [[Def - Dirichlet Form Loop Measure|Definition 2.2]] to $(\mathcal E^\phi,\mathcal F^\phi)$, the **rooted subordinate Brownian loop measure** on $C^*_X$ is the $\sigma$-finite measure
> $$\mu^{*,\phi}_X \;:=\; \int_0^\infty\frac{dt}{t}\int_X \mathbb{W}^{t,\phi}_{x\to x}\,d\operatorname{vol}_g(x),$$
> and its pushforward to $C_X$ is the **subordinate Brownian loop measure** $\mu^\phi_X$.

---

# In One Line

The [[Def - Dirichlet Form Loop Measure|Dirichlet-form loop measure]] built from the subordinate process $\phi(A)$ — i.e. loops of the process obtained by running the original one on the random clock with Laplace exponent $\phi$ (killed Brownian motion, $\alpha$-stable, gamma, relativistic-stable, …), all packaged into one formula.

---

# Motivation and Unpacking

**Why introduce it separately.** Formally $\mu^\phi_X$ is *just* $\mu^E_X$ with $(\mathcal E,\mathcal F)$ replaced by $(\mathcal E^\phi,\mathcal F^\phi)$ — no new definition needed. The paper names it because subordination is *the* mechanism by which every process it studies is built: killed Brownian motion is subordination by $\phi(\lambda)=\lambda+\kappa$, the $\alpha$-stable process is subordination by $\phi(\lambda)=\lambda^{\alpha/2}$, the shifted $\alpha$-stable process (introduced in §3.1.4) is subordination by $\phi(\lambda)=(\lambda+\kappa)^{\alpha/2}$, and the framework covers gamma and relativistic-stable subordinators as well (see [[Ex - The Four Bernstein Functions of the Paper|Example 2.5]]). So $\mu^\phi_X$ is the paper's *working object*: every mass computation in §3–§7 is a mass in $\mu^\phi_X$ for some $\phi$.

**Unpacking the double integral.** By the mass formula, the total is
$$|\mu^{*,\phi}_X| \;=\; \int_0^\infty\frac{dt}{t}\int_X p^\phi(t,x,x)\,d\operatorname{vol}_g(x),$$
and $p^\phi$ is itself an integral of $p^E(s,x,x)$ against the subordinator law $\psi^\phi_t(ds)$. So *every* mass computation in the subordinate loop measure carries **two** integrals: one over duration $t$ (against $\frac{dt}{t}$), one over subordination time $s$ (against $\psi^\phi_t$). Collapsing these two integrals into a *single* integral in $s$ is the point of the [[Def - Weighted Potential Measure|weighted potential measure]] $V_\phi$, and this is exactly what [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] delivers.

**Concrete cases already visible.** Substituting the subordinator laws from [[Ex - The Four Bernstein Functions of the Paper|Example 2.5]]:

- **Brownian ($\phi(\lambda)=\lambda$):** $\psi^\phi_t=\delta_t$, so $p^\phi=p^E$ and $\mu^\phi_X$ is the ordinary [[Def - Brownian Loop Measure|Brownian loop measure]] of $(\mathcal E,\mathcal F)$ — subordination does nothing. (This is not merely a special case; it *is* the case when there is no killing and no jumping.)
- **Killed Brownian motion ($\phi(\lambda)=\lambda+\kappa$):** $\psi^\phi_t=e^{-\kappa t}\delta_t$, so $p^\phi(t,x,y)=e^{-\kappa t}p^E(t,x,y)$ — the ambient loop measure exponentially tilted; the tilt kills the small-$t$ divergence's rate but not the divergence itself (see [[Ex - The Subordinate Form of Brownian Motion with Killing]]).
- **$\alpha$-stable ($\phi(\lambda)=\lambda^{\alpha/2}$):** the operator is the fractional Laplacian, the paths are pure-jump càdlàg, and $\mu^\phi_X$ concentrates on càdlàg loops with countably many jumps (see [[Ex - The Subordinate Form of the alpha-Stable Process]]).

**Restriction still holds.** Because $\mu^\phi_X$ is a [[Def - Dirichlet Form Loop Measure|Dirichlet-form loop measure]] for the specific form $(\mathcal E^\phi,\mathcal F^\phi)$, the restriction property of [[Def - Dirichlet Form Loop Measure|Definition 2.2]] transfers: for open $X'\subseteq X$, $\mu^{\phi}_{X'}$ (the loop measure of $\phi(A_{X'})$, where $A_{X'}$ is the killed generator on $X'$) is $\mu^\phi_X$ restricted to loops staying in $X'$. Conformal invariance does *not* transfer: even for $\phi(\lambda)=\lambda+\kappa$ the killing rate $\kappa$ is not a conformal invariant, and for $\phi(\lambda)=\lambda^{\alpha/2}$ the fractional Laplacian depends on the metric itself, not just its conformal class.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.4]]; every free-homotopy-class mass in §3 (as in [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]]) is a mass in $\mu^\phi_X$ for a specific $\phi$; the closed-form evaluations in §3.1 (killing, $\alpha$-stable, shifted $\alpha$-stable) are computations of $\mu^\phi_X$ on individual free-homotopy classes; the total-mass, zeta-function, and renormalisation results of §4–§5 all sit on $\mu^\phi_X$; the 3-manifold extension of §7 uses the subordinate loop measure on hyperbolic 3-space. Collapsed to a single $s$-integral in [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] via [[Def - Weighted Potential Measure|$V_\phi$]].

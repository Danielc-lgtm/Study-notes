---
type: remark
subject: probability
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Subordinate Brownian Loop Measure"
tags: [paper, brownian-loops, levy-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Assumption 2.3"
---

# Notation

$\phi:(0,\infty)\to[0,\infty)$ a Bernstein function with Lévy–Khintchine data $(a,b,\nu)$: killing rate $a\ge 0$, drift $b\ge 0$, Lévy measure $\nu$ on $(0,\infty)$ with $\int_0^\infty(1\wedge s)\,\nu(ds)<\infty$. $S_t$ the associated subordinator, $\psi^\phi_t$ its law on $[0,\infty)$. $A$ a non-negative self-adjoint operator on $L^2(X,\operatorname{vol}_g)$ with semigroup $e^{-sA}$ and transition density $p^E(s,x,y)$.

> [!recall]- Bernstein function $(a,b,\nu)$ data, subordinator $S_t$, law $\psi^\phi_t$
> **Formally:** $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda s})\,\nu(ds)$; $\mathbb{E}[e^{-\lambda S_t}]=e^{-t\phi(\lambda)}$; $\psi^\phi_t$ is the law of $S_t$ on $[0,\infty)$.
> **In words:** $\phi$ is the Laplace exponent of an increasing random clock. The three data $(a,b,\nu)$ encode the clock's three mechanisms: kill at rate $a$, drift smoothly at rate $b$, jump by size $s$ at Poisson intensity $\nu(ds)$.
> **Concretely:** $(a,b,\nu)=(0,1,0)$ gives $S_t=t$ (trivial clock, $\psi^\phi_t=\delta_t$). $(\kappa,1,0)$ gives $\psi^\phi_t=e^{-\kappa t}\delta_t$ (killed). $(0,0,\nu_\alpha)$ with $\nu_\alpha(ds)=\frac{\alpha/2}{\Gamma(1-\alpha/2)}s^{-1-\alpha/2}\,ds$ gives the $\alpha/2$-stable subordinator, whose law has a smooth density on $(0,\infty)$. See [[Def - Bernstein Function, Subordinator, and Subordination]].

> [!recall]- Compound Poisson subordinator
> **Formally:** a subordinator is **compound Poisson** if $b=0$ and $\nu$ is a *finite* measure on $(0,\infty)$ (i.e. $\lambda:=\nu(0,\infty)<\infty$). Then $S_t=\sum_{k=1}^{N_t}\xi_k$, where $N_t$ is a Poisson process of rate $\lambda$ and $\xi_k\overset{\text{iid}}{\sim}\nu/\lambda$. In particular $\mathbb{P}(S_t=0)=\mathbb{P}(N_t=0)=e^{-\lambda t}>0$: a positive chance the clock has not moved at all by time $t$.
> **In words:** a subordinator that only advances by countable *jumps* — it sits still between jumps, then jumps by an amount drawn from a fixed jump-size distribution. Because there are only finitely-many jumps per unit time, with positive probability none have happened yet.
> **Concretely:** the standard Poisson process $N_t$ on the integers is a compound Poisson subordinator with $\nu=\delta_1$, $b=0$, $a=0$: it jumps by $+1$ at intensity 1 and $\mathbb{P}(N_t=0)=e^{-t}$. Its Bernstein function is $\phi(\lambda)=\int_0^\infty(1-e^{-\lambda s})\delta_1(ds)=1-e^{-\lambda}$.

---

# Statement

> **Assumption (Belyaev–Huseynli 2.3).** Throughout the paper, the Bernstein function $\phi$ satisfies
> $$b>0 \quad\text{or}\quad \nu(0,\infty)=\infty,$$
> equivalently $S_t>0$ almost surely for every $t>0$, i.e. $\psi^\phi_t(\{0\})=0$.

---

# In One Line

Rule out **compound Poisson** subordinators, whose clock has a positive chance of not having moved: their subordinate semigroup has an atom in real time and hence *no transition density*, and a density is exactly what the loop measure needs.

---

# Unpacking

**Why the equivalence.** A subordinator's law splits as $\psi^\phi_t(\{0\})+\psi^\phi_t|_{(0,\infty)}$. The atom at $0$ (the event "clock hasn't moved") is present iff there is a positive chance $S_t=0$. For a Lévy subordinator with data $(a,b,\nu)$:
- If $b>0$, the clock has a nonzero smooth drift, so it strictly advances every instant: $S_t\ge bt>0$ almost surely.
- If $b=0$ and $\nu(0,\infty)=\infty$, the clock advances by infinitely-many jumps per unit time (a *pure-jump* subordinator of infinite activity — like the $\alpha/2$-stable): with probability one it has jumped by any time $t>0$, so $S_t>0$.
- If $b=0$ and $\nu(0,\infty)=\lambda<\infty$, the clock is compound Poisson: it waits an $\mathrm{Exp}(\lambda)$-time before its first jump, and with probability $e^{-\lambda t}$ has not jumped by time $t$, giving $\psi^\phi_t(\{0\})=e^{-\lambda t}>0$.

(Adding a killing rate $a>0$ multiplies $\psi^\phi_t$ by $e^{-at}$ but does not create or remove the atom at $0$.)

The equivalence $b>0$ or $\nu(0,\infty)=\infty$ $\Longleftrightarrow$ $\psi^\phi_t(\{0\})=0$ for all $t>0$ is thus a direct consequence of the Lévy–Khintchine decomposition of a subordinator's paths.

**Why the paper needs it.** The subordinate semigroup is $e^{-t\phi(A)}=\int_{[0,\infty)}e^{-sA}\psi^\phi_t(ds)$. If $\psi^\phi_t$ has an atom $c_t:=\psi^\phi_t(\{0\})>0$, then $e^{-t\phi(A)}=c_t\,I+\int_{(0,\infty)}e^{-sA}\psi^\phi_t(ds)$: the identity operator $I$ has *no* integral kernel (it acts by the "diagonal" $\delta_x(y)$, which is a distribution, not a function), so the subordinate semigroup has no transition density $p^\phi(t,x,y)$. But every construction in §2.4 (bridge measures $\mathbb{W}^{t,\phi}_{x\to y}$, the loop measure $\mu^\phi_X$, the collapsing identity of [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]) requires a density. So compound Poisson subordinators are excluded by fiat.

**What is not excluded.** The paper's four working cases all satisfy Assumption 2.3:
- Brownian ($\phi(\lambda)=\lambda$): $b=1>0$.
- Killing ($\phi(\lambda)=\lambda+\kappa$): $b=1>0$.
- $\alpha$-stable ($\phi(\lambda)=\lambda^{\alpha/2}$, $\alpha\in(0,2)$): $\nu_\alpha(0,\infty)=+\infty$ (integral of $s^{-1-\alpha/2}$ diverges near $0$).
- Shifted $\alpha$-stable ($\phi(\lambda)=(\lambda+\kappa)^{\alpha/2}$): same Lévy measure structure, $\nu(0,\infty)=+\infty$.

Gamma, inverse Gaussian, and relativistic-stable subordinators (mentioned in [[Ex - The Four Bernstein Functions of the Paper|Example 2.5]] as also admissible) all have $\nu(0,\infty)=+\infty$.

**What is excluded.** Any Bernstein function of pure jump-type with a finite Lévy measure — e.g. $\phi(\lambda)=1-e^{-\lambda}$ (standard Poisson) — is out. This is not a serious loss: compound Poisson subordinators produce processes whose paths jump only finitely often, for which the loop-measure formalism would need reformulating (the transition "kernel" would have a singular diagonal part corresponding to the "no-jump" event).

---

# Where the paper uses this

Standing assumption for all of §2.3 onward. Used explicitly in the proof of [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] to justify dropping the atom at $s=0$ in $p^\phi(t,x,y)=\int_{[0,\infty)}p^E(s,x,y)\,\psi^\phi_t(ds)$ so the integration is genuinely over $(0,\infty)$. Also cited in §3 (all mass computations require the density) and §4 (loop-soup construction). Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.3.1]].

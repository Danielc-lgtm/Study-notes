---
type: definition
subject: probability
prereqs:
  - "Def - Dirichlet Form and its Operator and Semigroup"
  - "Def - Signed and Infinite Measures for Loop Measures"
tags: [probability, stochastic-processes, levy-processes, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$A$ a non-negative self-adjoint operator on $L^2(X,\operatorname{vol}_g)$ (for the paper, $A=\Delta_X$ or a Dirichlet-form operator), with semigroup $e^{-tA}$ and kernel $p^E(t,x,y)$. $\lambda>0$ a spectral variable; $t\ge0$ time; $s\ge0$ the subordination (proper-time) variable. $S_t$ a random time change; $\psi^\phi_t$ its law on $[0,\infty)$.

---

# Axiom Motivation

Given one Markov process (say Brownian motion) the paper wants a whole family of relatives — killed motion, $\alpha$-stable jump processes — cheaply. **Subordination** manufactures them by running the original process on a *random clock*: instead of observing the process at real time $t$, observe it at a random time $S_t$ that is itself increasing and random. If the clock $S_t$ jumps, the observed process skips ahead — so a continuous diffusion becomes a *jump* process. The question is which random clocks give again a nice Markov process with a self-adjoint generator; the answer is exactly the clocks whose "speed law" is governed by a **Bernstein function**.

The connection is through the Laplace transform. A subordinator $S_t$ is determined by $\mathbb{E}[e^{-\lambda S_t}]=e^{-t\phi(\lambda)}$; the exponent $\phi$ must be a Bernstein function, and then the new generator is simply $\phi(A)$ — you apply the *function* $\phi$ to the *operator* $A$ via its spectral calculus. Two examples make the mechanism concrete: $\phi(\lambda)=\lambda$ is the trivial clock ($S_t=t$, no change), and $\phi(\lambda)=\lambda^{\alpha/2}$ turns the Laplacian into the fractional Laplacian $\Delta^{\alpha/2}$ and Brownian motion into the $\alpha$-stable process. The **Lévy–Khintchine representation** of $\phi$ splits any such clock into three transparent pieces — a killing rate $a$, a drift $b$, and a jump intensity $\nu$ — which is why the paper can read off, for each process, how much killing, how much smooth drift, and how much jumping it carries.

---

# The Definition

> **Definition (Bernstein function).** A function $\phi:(0,\infty)\to[0,\infty)$ is a **Bernstein function** if it is $C^\infty$ and $(-1)^{n-1}\phi^{(n)}(\lambda)\ge0$ for all $n\ge1$, $\lambda>0$ (so $\phi\ge0$, $\phi'\ge0$, $\phi''\le0$, …: $\phi$ increases and is concave, with alternating derivative signs). Every Bernstein function has a unique **Lévy–Khintchine representation**
> $$\phi(\lambda) \;=\; a + b\lambda + \int_0^\infty\big(1-e^{-\lambda s}\big)\,\nu(ds),\qquad \lambda>0,$$
> where $a\ge0$ is the **killing rate**, $b\ge0$ the **drift**, and $\nu$ the **Lévy measure** on $(0,\infty)$ with $\int_0^\infty(1\wedge s)\,\nu(ds)<\infty$.

> **Definition (subordinator).** A **subordinator** $(S_t)_{t\ge0}$ is an increasing [[Def - Signed and Infinite Measures for Loop Measures|Lévy process]] on $[0,\infty)$ (independent stationary increments, $S_0=0$, non-decreasing paths), possibly killed at constant rate, whose **Laplace exponent** is a Bernstein function:
> $$\mathbb{E}\big[e^{-\lambda S_t}\big] \;=\; e^{-t\phi(\lambda)},\qquad \lambda>0,\ t\ge0.$$
> Write $\psi^\phi_t$ for the law of $S_t$ on $[0,\infty)$. When $a=0$ the subordinator is **conservative** and $\psi^\phi_t$ is a probability measure; when $a>0$ it is killed at rate $a$ and $|\psi^\phi_t|=e^{-at}$.

> **Definition (subordination of a semigroup / Dirichlet form).** Given $A$ and a Bernstein $\phi$ with independent subordinator, the **subordinate semigroup** is the average of $e^{-sA}$ against the clock law,
> $$e^{-t\phi(A)} \;=\; \int_{[0,\infty)} e^{-sA}\,\psi^\phi_t(ds),\qquad \phi(A)=aI+bA+\int_0^\infty\big(I-e^{-sA}\big)\,\nu(ds),$$
> with generator $-\phi(A)$, transition density $p^\phi(t,x,y)=\int_{[0,\infty)}p^E(s,x,y)\,\psi^\phi_t(ds)$, and associated [[Def - Dirichlet Form and its Operator and Semigroup|Dirichlet form]] $\mathcal E^\phi(u,u)=a\|u\|^2+b\,\mathcal E(u,u)+\int_0^\infty\big(\|u\|^2-\langle e^{-sA}u,u\rangle\big)\nu(ds)$.

**Concrete unpacking (the paper's Example 2.5).** Three clocks:
- **Brownian motion, $\phi(\lambda)=\lambda$:** data $(a,b,\nu)=(0,1,0)$, law $\psi^\phi_t=\delta_t$ (the clock is *deterministic*, $S_t=t$). Subordination does nothing: $p^\phi=p^E$.
- **Killing at rate $\kappa$, $\phi(\lambda)=\lambda+\kappa$:** data $(\kappa,1,0)$, law $\psi^\phi_t=e^{-\kappa t}\delta_t$. The process is Brownian motion that dies at exponential rate $\kappa$; $p^\phi(t,x,y)=e^{-\kappa t}p^E(t,x,y)$.
- **$\alpha$-stable, $\phi(\lambda)=\lambda^{\alpha/2}$, $\alpha\in(0,2)$:** data $(0,0,\nu_\alpha)$ with $\nu_\alpha(ds)=\frac{\alpha/2}{\Gamma(1-\alpha/2)}s^{-1-\alpha/2}\,ds$, law $\psi^\phi_t$ the $\alpha/2$-stable density. The operator is the **fractional Laplacian** $\Delta^{\alpha/2}$; the process is pure-jump (càdlàg), and $\alpha=2$ recovers Brownian motion.

**Standard names.** **Bernstein function**, **Lévy–Khintchine representation**, **Lévy measure**, **subordinator**, **Laplace exponent**, **subordination** (Bochner subordination). Reference: Schilling–Song–Vondraček, *Bernstein Functions*.

---

# Examples and Non-Examples

**Is an instance.** $\phi(\lambda)=\lambda^{\alpha/2}$ (stable), $\lambda+\kappa$ (killing), $\log(1+\lambda)$ (gamma subordinator), $\sqrt{\lambda+m^2}-m$ (relativistic stable) — all Bernstein.

**Is NOT an instance.** $\phi(\lambda)=\lambda^2$ is **not** Bernstein ($\phi''=2>0$ violates concavity), and indeed $-A^2$ generates no Markov process. A **compound Poisson** subordinator is Bernstein but is excluded by the paper's Assumption 2.3 ($b>0$ or $\nu(0,\infty)=\infty$): its law $\psi^\phi_t$ has an atom at $0$ (positive chance the clock hasn't moved), so the subordinate semigroup has no transition *density*.

**Calibration check.** (1) Verify $\phi(\lambda)=\lambda+\kappa$ has $(a,b,\nu)=(\kappa,1,0)$ from the Lévy–Khintchine formula. (2) Check that $\mathbb{E}[e^{-\lambda S_t}]=e^{-t\phi(\lambda)}$ with $\psi^\phi_t=e^{-\kappa t}\delta_t$ gives $\phi(\lambda)=\lambda+\kappa$. (3) Confirm $p^\phi=\int p^E(s,\cdot,\cdot)\psi^\phi_t(ds)$ reduces to $p^E$ when $\psi^\phi_t=\delta_t$.

---

# Where the paper uses this

Subordination is how the paper builds *all* its processes from one Laplacian: killed Brownian motion, $\alpha$-stable jumps, gamma and relativistic-stable processes. The transition density formula $p^\phi=\int p^E(s,\cdot,\cdot)\psi^\phi_t(ds)$ and the operator $\phi(A)$ feed directly into the [[Def - Subordinate Brownian Loop Measure|subordinate Brownian loop measure]] (§2.4) and, after collapsing the $t$-integral, into the [[Def - Weighted Potential Measure|weighted potential measure]] $V_\phi$ (§2.4.1) and [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]. Assumption 2.3 is what guarantees a transition density exists. **[[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2]]**.

---

# Verified against

Schilling, Song, Vondraček, *Bernstein Functions: Theory and Applications* (2nd ed.), Ch. 3 (Bernstein functions, complete monotonicity of derivatives, Lévy–Khintchine), Ch. 5 (subordinators, subordinate semigroups $e^{-t\phi(A)}=\int e^{-sA}\psi_t^\phi(ds)$, subordinate Dirichlet forms) — the paper cites [SSV12]. Fractional-Laplacian/$\alpha$-stable identifications standard; Assumption 2.3 ⇔ no atom at 0 ⇔ transition density exists, per [SSV12, Ch. 5].

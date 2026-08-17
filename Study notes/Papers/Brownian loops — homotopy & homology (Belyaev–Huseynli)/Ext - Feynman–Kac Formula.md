---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, probability, quantum]
---

# Signature

| symbol | type |
|---|---|
| $X$ | a complete Riemannian manifold; here a hyperbolic surface |
| $V$ | $X\to[0,\infty)$ measurable, bounded below — the **potential** / killing rate |
| $\Delta_X$ | the **positive** Laplacian; $\widehat H=\Delta_X+V$, self-adjoint, $\widehat H\geq0$ |
| $W^t_{x\to y}$ | the [[Def - Unnormalised Bridge Measure by Disintegration\|unnormalised bridge measure]] on $C([0,t];X)$; total mass $p(t,x,y)$ |
| $p_V$ | $(0,\infty)\times X\times X\to(0,\infty)$ — integral kernel of $e^{-t\widehat H}$ |

---

# Statement

> **(FK) Feynman–Kac.** *Precondition:*
> **(P1)** $p$ is the transition density of Brownian motion on $X$ (exists by [[Def - Transition Density and Heat Kernel|(F4)]] in the hyperbolic case);
> **(P2)** $V:X\to[0,\infty)$ measurable and bounded below;
> **(P3)** $\widehat H=\Delta_X+V$ self-adjoint on $L^2(X,\mathrm{vol}_g)$ with $\widehat H\geq0$.
>
> *Conclusion:* $e^{-t\widehat H}$ has an integral kernel $p_V$, and
> $$p_V(t,x,y)=\int_{C([0,t];X)}e^{-\int_0^tV(\omega(r))\,\mathrm{d}r}\,W^t_{x\to y}(\mathrm{d}\omega).\tag{FK}$$

> **(F1) Constant potential.** $V\equiv\kappa$ $\Rightarrow$ the weight is the constant $e^{-\kappa t}$, so
> $$p_\kappa(t,x,y)=e^{-\kappa t}p(t,x,y).$$
> This is exactly the kernel used by $\phi(\lambda)=\lambda+\kappa$ in [[Constr - The Subordinate Brownian Loop Measure]].
>
> **(F2) Probabilistic reading.** $e^{-\int_0^tV(\omega)}$ is the probability that a path $\omega$ survives killing at spatially varying rate $V$. So $p_V$ is the sub-probability density of Brownian motion **killed at rate $V$**.
>
> **(F3) Wick rotation.** $t\mapsto-i\tau$ carries the unitary group $e^{-it\widehat H/\hbar}$ to the contraction semigroup $e^{-\tau\widehat H/\hbar}$; well defined for $\tau\geq0$ precisely because $\widehat H\geq0$. The Euclidean time $\tau$ **is** the diffusion time $t$ of §2.

---

# Type card

> [!abstract] Type card — (FK)
> **Given.** (P1),(P2),(P3).
>
> **Produces.** The identity (FK): a kernel of an operator semigroup written as an integral against a path measure. Type: $(0,\infty)\times X\times X\to(0,\infty)$, equality of two such functions.
>
> **Lets you.** Move between the analytic object $e^{-t(\Delta_X+V)}$ and the probabilistic object "Brownian bridge weighted by survival". In this paper it is used **only** in the direction analysis $\to$ probability, and **only** for $V\equiv\kappa$, where it collapses to (F1).

---

# Status

- **Proved here:** no. Stated in §3.2 as known.
- **Source:** standard; Simon, *Functional Integration and Quantum Physics*; Sznitman, *Brownian Motion, Obstacles and Random Media*.
- **DAG node that would close this:** 🟢 *SDEs / Stochastic Analysis* (7,10) and 🟢 *Advanced Probability* (7,9) — (FK) is inside both. This import is **not** a gap.
- **What is safe to assume:** all of (FK),(F1)–(F3). Nothing downstream depends on the proof, and nothing downstream needs non-constant $V$.
- **Scope:** §3.2 only. Section 3.2 is a digression: **no** later result cites it. Deleting §3.2 costs no theorem.

> [!warning] The unnormalised bridge is what makes (FK) an identity of kernels
> If $W^t_{x\to y}$ were the *probability* bridge, the right-hand side of (FK) would be $p_V/p$, not $p_V$. The factor $p(t,x,y)=\lvert W^t_{x\to y}\rvert$ is carrying the density. See [[Def - Unnormalised Bridge Measure by Disintegration|(F1)]].

---

# Used at

- [[§3.2 Euclidean Quantum Mechanics and the Path Integral]] — the whole section
- [[Constr - The Subordinate Brownian Loop Measure]] — (F1) identifies the killing case with $\phi(\lambda)=\lambda+\kappa$

---

# Commentary

> [!note]- Commentary (skippable)
> The formal path integral $\int\mathcal{D}\omega\,e^{-S[\omega]}$ with action $S[\omega]=\int_0^t\big(\tfrac14\lvert\dot\omega\rvert^2+V(\omega)\big)\mathrm{d}r$ has no measure $\mathcal{D}\omega$ behind it: there is no Lebesgue measure on path space, and Brownian paths are nowhere differentiable so $\lvert\dot\omega\rvert^2$ is undefined pointwise. (FK) is the rigorous replacement, and the bookkeeping is worth stating once: **the kinetic part of the action is absorbed into $W^t_{x\to y}$, and only the potential part survives as an explicit weight.**
>
> That is the entire content of the physicists' formula for the purposes of this paper. The rest of §3.2 is a dictionary, not an argument.

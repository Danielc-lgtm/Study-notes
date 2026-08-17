---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs: []
tags: [paper, probability, potential-theory]
---

# Signature

| symbol | type |
|---|---|
| $M$ | a Markov process on $X$ with law $\mathbb{P}_x$ from $x$ |
| $P$ | $\subseteq X$ Borel — the candidate polar set |
| $T_P$ | $:=\inf\{t>0:M_t\in P\}$ — the hitting time, a stopping time |
| $\operatorname{cap}$ | logarithmic capacity of a compact subset of a chart; $[0,\infty)$-valued |
| $\kappa$ | $\geq0$; $\phi(\lambda)=\lambda+\kappa$ the killing case |
| $\alpha$ | $\in(0,2)$; $\phi(\lambda)=\lambda^{\alpha/2}$ the stable case |

---

# Definition

> **Definition (polar).** $P\subseteq X$ Borel is **polar for $M$** if
> $$\forall x\in X:\quad \mathbb{P}_x\big(T_P<\infty\big)=0,\qquad T_P:=\inf\{t>0:M_t\in P\}.$$
> In words: from every starting point, the process almost surely never hits $P$ at a positive time.

> **(F1) Characterisation for Brownian motion on a Riemann surface.** $P$ is polar $\iff$ $\operatorname{cap}(K)=0$ for every compact $K\subseteq P$ in every local chart (zero **logarithmic capacity**).
>
> **(F2) Singletons.** $\{p\}$ is polar for planar/surface Brownian motion, for every $p$.
>
> **(F3) $\sigma$-ideal.** The polar sets are closed under subsets and countable unions. With (F2): **every countable set is polar**, in particular every closed discrete set.
>
> **(F4) Killing does not change polarity.** A killing rate does not change the *paths*, only their weight, so for $\phi(\lambda)=\lambda+\kappa$ the polar sets are exactly the Brownian ones.
>
> **(F5) Polarity is process-dependent.** For $\phi(\lambda)=\lambda^{\alpha/2}$ the paths jump and can land anywhere; such processes hit sets a diffusion misses, so the class of polar sets **shrinks** as $\alpha$ decreases. §3.4 is therefore restricted to the diffusion cases.

---

# Type card

> [!abstract] Type card — polar set
> **Given.** **(H1)** a Markov process $M$ on $X$. **(H2)** $P\subseteq X$ Borel.
>
> **Produces.** A proposition about the pair $(M,P)$. When true: the loop measure of $M$ is supported on loops avoiding $P$, so by [[Ext - Lawler–Werner Restriction and Conformal Invariance|(LW1)]] restriction to $X\setminus P$ changes no class mass.
>
> **Lets you.** Delete a set at no cost. Used once, in §3.4, to see that puncturing at a closed discrete set is invisible to $\mu^\kappa_X$.

---

# Depends on

- 🟢 potential theory of Markov processes; hitting times ([[Def - Stopping Time]]) — *Advanced Probability*, *SDEs*
- 🟢 logarithmic capacity — classical potential theory
- Source for (F1)–(F3): Blumenthal–Getoor, *Markov processes and potential theory*

---

# Checks

**Instance.** $P$ a closed discrete subset of $X$ — e.g. a single point, or a sequence with no accumulation point in $X$. Polar for Brownian motion by (F2)+(F3), and for Brownian motion with killing by (F4). Hence invisible to $\mu^\kappa_X$: the loops that would have hit $P$ form a null set.

**Non-instance (fails F1).** A smooth curve $\Sigma\subseteq X$, e.g. a geodesic arc. $\operatorname{cap}(\Sigma)>0$, and surface Brownian motion hits curves with probability one. Consequence: restriction to $X\setminus\Sigma$ **does** change the loop measure — the loops crossing $\Sigma$ carry positive mass. Cutting along a curve is a real operation on the surface; puncturing at points is not.

**Non-instance (fails for a different process).** $\{p\}$ is polar for Brownian motion but **not** for an $\alpha$-stable process with $\alpha$ small enough: a jump process can land on a small set a diffusion steps over. By (F5) the §3.4 identity does not extend to the stable cases, and the paper restricts to "the diffusion cases (where homotopy classes make sense)".

---

# Used at

- [[Ext - Wang–Xue Length-Spectrum Identity]] — $P$ is hypothesised non-empty, closed, polar
- [[§3 Decomposition over Homotopy Classes]] §3.4 — the surviving restriction identity $\mu^\kappa_{X,g}(\mathcal{C}_X(\gamma^m))=\mu^\kappa_{X\setminus P,g}(\mathcal{C}_X(\gamma^m))$
- [[Constr - The Brownian Loop Measure]] — (P1) is what polarity is combined with

---

# Commentary

> [!note]- Commentary (skippable)
> The entire use in the paper is one implication: *$P$ polar $\Rightarrow$ $\mu^\kappa_X$ is supported on loops avoiding $P$ $\Rightarrow$ by restriction, deleting $P$ changes nothing.*
>
> (F4) is the small clause that buys the killing case for free, and (F5) is the reason §3.4 stops there. Both come from the same observation about what a killing rate does — it reweights paths without changing them — and it is the only place in the paper where that distinction is load-bearing.

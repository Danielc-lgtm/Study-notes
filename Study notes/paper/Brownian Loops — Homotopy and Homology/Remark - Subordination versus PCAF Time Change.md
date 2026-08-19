---
type: remark
subject: probability
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Dirichlet Form and its Operator and Semigroup"
tags: [paper, brownian-loops, levy-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Remark 2.4"
---

# Notation

$(X,g)$ a Riemannian surface with area measure $\operatorname{vol}_g$; $(\mathcal E,\mathcal F)$ a regular symmetric Dirichlet form with generator $-A$; $B=(B_t)_{t\ge 0}$ the associated symmetric Markov process with filtration $(\mathcal F_t)$. $S_t$ a subordinator with Bernstein function $\phi$ and law $\psi^\phi_t$. $F_t$ a **positive continuous additive functional** (PCAF) of $B$: a $(\mathcal F_t)$-adapted, continuous, non-decreasing process with $F_0=0$ and $F_{t+s}=F_t+F_s\circ\theta_t$ (an "additive" functional that only reads what $B$ has done up to time $t$).

> [!recall]- Subordinator (independent random clock)
> **Formally:** $(S_t)_{t\ge 0}$ is an increasing Lévy process on $[0,\infty)$ (independent stationary increments, $S_0=0$, non-decreasing paths, possibly killed) whose Laplace exponent is a Bernstein function $\phi$; **independent** of the underlying process $B$.
> **In words:** an increasing random clock whose future increments are independent of the past — and independent of the process $B$ it will time-change. Read the process at the random time $S_t$.
> **Concretely:** $S_t=t$ (trivial), $\psi^\phi_t=e^{-\kappa t}\delta_t$ (killed), $\alpha/2$-stable clock. Because $S_t$ is not adapted to $B$'s filtration, it can jump — and when it does, $B_{S_t}$ jumps too, so subordination can turn a continuous $B$ into a jump process $Y_t=B_{S_t}$. See [[Def - Bernstein Function, Subordinator, and Subordination]].

> [!recall]- Positive continuous additive functional (PCAF) and its Revuz measure
> **Formally:** a **PCAF** of a Markov process $B$ is a real-valued process $F=(F_t)_{t\ge 0}$ that is (i) $(\mathcal F_t)$-**adapted** (each $F_t$ is determined by $\{B_s:s\le t\}$), (ii) **continuous** in $t$, (iii) **non-decreasing**, (iv) $F_0=0$, and (v) **additive**: $F_{t+s}(\omega)=F_t(\omega)+F_s(\theta_t\omega)$, where $\theta_t$ is the time-shift on paths. The **Revuz measure** $\mu_F$ of $F$ is the (positive) measure on $X$ defined via $\int_X f\,d\mu_F=\lim_{t\downarrow 0}\frac{1}{t}\mathbb{E}_{m}[\int_0^t f(B_s)\,dF_s]$ for suitable $f$, with $m=\operatorname{vol}_g$ the reference measure of $(\mathcal E,\mathcal F)$; it records where along $B$'s trajectory $F$ accumulates its mass.
> **In words:** a PCAF is a random increasing quantity that grows *while $B$ moves*, based only on where $B$ has been so far — so it is entirely a function of $B$'s trajectory, not an outside clock. Its inverse defines a time change $t\mapsto F^{-1}(t)$: run $B$ at real time until it has accumulated $t$ units of $F$. The Revuz measure says how much $F$ typically piles up in each region.
> **Concretely:** on planar Brownian motion, $F_t=\int_0^t \mathbf 1_{\{B_s\in A\}}\,ds$ (occupation time of $A$) is a PCAF with Revuz measure $\mathbf 1_A\,d\operatorname{vol}_g$; the time-changed process $B_{F^{-1}(t)}$ is Brownian motion observed only while it is in $A$. More sophisticated: for a positive continuous $\rho:X\to(0,\infty)$, $F_t=\int_0^t\rho(B_s)\,ds$ is a PCAF with Revuz measure $\rho\,d\operatorname{vol}_g$; the time change $B_{F^{-1}(t)}$ is $B$ run on a $\rho$-weighted clock. Reference: [RY99, Ch. 10].

---

# Statement

> **Remark (Belyaev–Huseynli 2.4).** Two constructions both "run the process on a different clock", but they act differently on the data $(\mathcal E,\mathcal F,\operatorname{vol}_g)$, and it is worth keeping them apart.
> - **Subordination.** The clock $S_t$ is a subordinator, **independent** of $B$ and **not adapted** to its filtration. It replaces the generator $-A$ by $-\phi(A)$, changes the Dirichlet form to $(\mathcal E^\phi,\mathcal F^\phi)$, **keeps the reference measure $\operatorname{vol}_g$**, and (when $\nu\ne 0$) introduces **jumps** into even a diffusion $B$.
> - **PCAF time change.** The clock $F_t$ is a positive continuous additive functional, built from $B$'s **own trajectory** and **adapted** to its filtration. Its inverse reparametrises the same path, so **continuity of paths is preserved**, but the reference measure is replaced by the **Revuz measure** $\mu_F$ of the additive functional (see [RY99, Ch. 10]).
>
> The paper uses **subordination**, not PCAF time change.

---

# In One Line

Subordination = independent clock, generator becomes $\phi(A)$, keeps $\operatorname{vol}_g$, may introduce jumps; PCAF time change = process-adapted clock, preserves continuity, replaces the reference measure with $\mu_F$. The two are not the same, and the paper commits to subordination.

---

# Unpacking

**The core contrast.** Both operations start with a symmetric Markov process $B$ on $(X,\operatorname{vol}_g)$ and produce a new process $Y$ by looking at $B$ on a different clock. The difference is *whose clock*.

- In **subordination**, the clock $S_t$ is *external*: an independent Lévy process on $[0,\infty)$ with law prescribed by a Bernstein function $\phi$. $Y_t := B_{S_t}$. Because $S_t$ is not a function of $B$'s trajectory, and because $S_t$ can jump, $Y$'s paths can differ discontinuously from $B$'s: whenever $S$ jumps by $s$, $B$ moves during that clock-time by a random amount, and $Y$ jumps by that amount. So even if $B$ is a continuous diffusion (like Brownian motion), $Y$ can be a pure-jump process (like the $\alpha$-stable). The generator transforms cleanly, by the spectral calculus: $\text{gen}(Y) = -\phi(A)$; the Dirichlet form transforms into $(\mathcal E^\phi,\mathcal F^\phi)$ as in [[Def - Bernstein Function, Subordinator, and Subordination|Definition 2.9 above]]; the reference measure $\operatorname{vol}_g$ is *unchanged* (both $B$ and $Y$ live on the same measurable state space and $Y$ is $\operatorname{vol}_g$-symmetric).

- In a **PCAF time change**, the clock $F_t$ is *internal*: it is built from $B$'s own trajectory (an occupation-time-like functional), so it is $B$-adapted and *continuous* in $t$. The new process is $Z_t := B_{F^{-1}(t)}$ — run $B$ at real time until it has accumulated $t$ units of $F$, then read off. Because $F$ is continuous and non-decreasing, $F^{-1}$ is well-defined (up to constant intervals) and $Z$'s paths are just $B$'s paths *reparametrised in time*: their images in $X$ are identical, only the clock along them changes. So **continuity is preserved**: continuous $B$ gives continuous $Z$, no jumps. What changes is the reference measure: the natural reversible measure for $Z$ is the **Revuz measure** $\mu_F$ of $F$, not $\operatorname{vol}_g$. Equivalently, $Z$'s Dirichlet form is $(\mathcal E,\mathcal F)$ read against $\mu_F$ instead of $\operatorname{vol}_g$.

**The canonical PCAF example: Liouville Brownian motion.** The illustration the paper alludes to is [GRV16]. Take planar Brownian motion $B_t$, coupling constant $\gamma\in[0,2)$, and let $\varphi$ be the Gaussian free field on the plane (or on a domain); define the **quantum clock**
$$F_t \;=\; \int_0^t e^{\gamma\varphi(B_s)}\,ds$$
where $e^{\gamma\varphi}$ is the Gaussian multiplicative chaos (a random measure on the plane, since $\varphi$ is not a function pointwise; the exponential is defined via renormalisation). Then $F$ is a PCAF of $B$ with Revuz measure the Liouville measure $\mu_L=e^{\gamma\varphi}\,d\operatorname{vol}_g$. The time-changed process
$$Z_t \;=\; B_{F^{-1}(t)}$$
is called **Liouville Brownian motion**: continuous paths (same shape as ordinary Brownian motion, since it is just a reparametrisation), but the reference measure is now the Liouville measure. It arises in Liouville quantum gravity as the natural diffusion on a random metric surface.

**Why the paper flags the distinction.** All four Bernstein functions the paper uses (Brownian, killing, $\alpha$-stable, shifted $\alpha$-stable — see [[Ex - The Four Bernstein Functions of the Paper|Example 2.5]]) are subordinators, not PCAFs. For the $\alpha$-stable case this matters: the paths of the $\alpha$-stable process are discontinuous, which is why [[Def - Dirichlet Form Loop Measure|Def 2.2]] moved to càdlàg paths $D([0,t],X)$; if the paper had time-changed by a PCAF instead, the process would be continuous and the jump apparatus would be gone. The paper's homotopy-class decomposition (§3) is genuinely sensitive to which mechanism is in use — for the jump case, a càdlàg path has no honest homotopy class (there is no lift), and the paper defines the class-mass by restriction on the underlying Brownian arc (Remark 3.1). PCAF time changes would sidestep this issue but produce a different family of processes.

**A clean summary table.**

| | Subordination | PCAF time change |
|---|---|---|
| Clock $C_t$ | independent Lévy subordinator | adapted to $B$'s filtration |
| Adapted to $B$? | no | yes |
| Path continuity | may break (jumps if $\nu\ne 0$) | preserved |
| Generator | $-\phi(A)$ | $-A$ read against Revuz $\mu_F$ |
| Reference measure | unchanged ($\operatorname{vol}_g$) | replaced by $\mu_F$ |
| Example | $\alpha$-stable, Brownian with killing | Liouville Brownian motion |

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.3.1]] to head off the confusion between the two constructions before subordination is formally introduced in the next subsection. Its practical consequence: the paper's [[Def - Subordinate Brownian Loop Measure|subordinate loop measure]] carries $\operatorname{vol}_g$ (not any renormalised measure), and the paths of the subordinate process may jump — both facts that would fail under PCAF time change.

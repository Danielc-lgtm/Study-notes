---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Self-Adjoint Operator"
tags: [paper, analysis, heat-kernels]
---

# Signature

| symbol | type |
|---|---|
| $(E,m)$ | locally compact separable metric space; $m$ Radon of full support |
| $A$ | non-negative self-adjoint operator on $L^2(E,m)$; $\operatorname{spec}(A)\subseteq[0,\infty)$ |
| $e^{-tA}$ | $L^2(E,m)\to L^2(E,m)$, $t\geq0$; strongly continuous contraction semigroup |
| $p$ | $(0,\infty)\times E\times E\to[0,\infty)$; the transition density |
| $\Delta_X$ | $-\operatorname{div}_g\operatorname{grad}_g$ on a Riemannian manifold $(X,g)$; $\operatorname{vol}_g$ its volume measure |
| $p_X$ | the heat kernel: the transition density of $e^{-t\Delta_X}$ against $\operatorname{vol}_g$ |
| $\operatorname{Tr}$ | trace of a trace-class operator |

**Convention.** $\Delta_X\geq0$ — the *positive* Laplacian, opposite sign to $\partial_x^2+\partial_y^2$. Brownian motion is run at speed $2$: its generator is $-\Delta_X$, not $-\tfrac12\Delta_X$.

---

# Definition

> **Definition (transition density).** $p$ is a **transition density for $e^{-tA}$ with respect to $m$** if
> **(D1) Measurability.** $p$ is jointly measurable on $(0,\infty)\times E\times E$.
> **(D2) Symmetry.** $p(t,x,y)=p(t,y,x)$ for all $t>0$, $x,y\in E$.
> **(D3) Representation.** $\ \displaystyle (e^{-tA}f)(x)=\int_E p(t,x,y)f(y)\,m(\mathrm{d}y)$ for all $f\in L^2(E,m)$, $m$-a.e. $x$, all $t>0$.

> **Definition (heat kernel).** For $(X,g)$ a complete Riemannian manifold, $p_X$ is the transition density of $e^{-t\Delta_X}$ with respect to $\operatorname{vol}_g$. Where $\partial X\neq\emptyset$, Dirichlet conditions are imposed, so the associated process is killed on first hitting $\partial X$.

**Gloss.** (D3) is the only clause with content; (D1) and (D2) are what make the integral in (D3) and the diagonal $p(t,x,x)$ meaningful pointwise rather than $m$-a.e.

> **(F1) Chapman–Kolmogorov.** $\ \displaystyle p(t+u,x,y)=\int_E p(t,x,z)p(u,z,y)\,m(\mathrm{d}z)$, from $e^{-(t+u)A}=e^{-tA}e^{-uA}$.
>
> **(F2) Trace.** If $e^{-tA}$ is trace class then $\ \operatorname{Tr}(e^{-tA})=\int_E p(t,x,x)\,m(\mathrm{d}x)$.
>
> **(F3) Short-time diagonal, surfaces.** On a Riemannian surface, $\ p_X(t,x,x)\sim\dfrac{1}{4\pi t}$ as $t\downarrow0$.
>
> **(F4) Existence is not automatic.** A strongly continuous contraction semigroup on $L^2(E,m)$ need not admit a $p$ satisfying (D1)–(D3): if $e^{-tA}$ has an atom on the diagonal, no density exists. This is exactly what [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|(A2.3)]] rules out for subordinate semigroups.

---

# Type card

> [!abstract] Type card — transition density / heat kernel
> **Given.** **(H1)** $(E,m)$ as above. **(H2)** $A$ non-negative self-adjoint on $L^2(E,m)$.
>
> **Produces.** Either a function $p:(0,\infty)\times E\times E\to[0,\infty)$ satisfying (D1)–(D3), or nothing — existence is a hypothesis, by (F4). When it exists it is unique up to $m\otimes m$-null sets, and (F1)–(F3) hold.
>
> **Lets you.** Write every object in the paper — bridge measures, loop measures, periodisations, heat traces — as an integral of $p$, and read $p(t,x,x)$ as a pointwise number rather than an equivalence class.

---

# Depends on

- [[Def - Self-Adjoint Operator]], [[Thm - Complex Spectral Theorem]] — for $e^{-tA}$ via functional calculus
- 🟢 $L^2$ semigroup theory, Radon measures — *Functional Analysis*, *Advanced Probability*

---

# Checks

**Instance.** $E=\mathbb{H}^2$, $m=\rho$, $A=\Delta_{\mathbb{H}^2}$. (D1)–(D3) hold, and $p_{\mathbb{H}^2}(t,z,w)$ depends on $(z,w)$ only through $d(z,w)$, being $\mathrm{PSL}(2,\mathbb{R})$-invariant. On $\mathbb{H}^3$ the kernel is explicit — see [[Ext - Explicit Heat Kernel on Hyperbolic 3-Space]].

**Non-instance (fails D3, hence F4).** $A=0$, so $e^{-tA}=\mathrm{Id}$ for all $t$. There is no $p$ with $\int p(t,x,y)f(y)\,m(\mathrm{d}y)=f(x)$ for all $f\in L^2$: the required object is $\delta_x$, not a function. The same failure occurs, with weight $\psi^\phi_t(\{0\})>0$ rather than $1$, for a compound Poisson subordinator.

**Non-instance (fails F2).** On a cusped finite-area hyperbolic surface, $p_X$ exists and satisfies (D1)–(D3), but $e^{-t\Delta_X}$ is **not** trace class and $\int_Xp_X(t,z,z)\,\mathrm{d}\rho_X=\infty$ — the diagonal does not decay in the cusps. (F2) has a hypothesis and it fails here; the repair is [[Def - Renormalised Integral and the 0-Trace]].

---

# Used at

- [[Def - Unnormalised Bridge Measure by Disintegration]] — $\lvert W^t_{x\to y}\rvert=p(t,x,y)$
- [[Def - Regular Symmetric Dirichlet Form]] — existence of $p$ is a standing hypothesis
- [[Constr - The Brownian Loop Measure]], [[Constr - The Dirichlet-Form Loop Measure]] — the loop measure is built from $p$ via bridges
- [[Constr - The Periodised Kernel]] — the periodisation is a $\Gamma$-sum of values of $p$
- [[Def - Schwinger Proper-Time Representation]], [[Def - Zeta-Regularised Determinant of the Laplacian]] — via (F2)
- [[Constr - The Brownian Loop Measure]] — (F3) is why the total mass diverges at $t\downarrow0$

---

# Commentary

> [!note]- Commentary (skippable)
> The paper states (D1)–(D3) once, in §2.2, as "we assume throughout that the semigroup admits a jointly measurable symmetric transition density", and then uses $p$ everywhere without restating what it is. Isolating it makes two things visible.
>
> First, that **existence is a hypothesis, not a fact** — (F4). Half of §2.3's care, and all of Assumption 2.3, exists to preserve it under subordination.
>
> Second, that (F2) also has a hypothesis, and that the entire split between §5.1 and §5.2 is the split between (F2) holding and failing. §5.1 is what one can do when the trace is a trace; §5.2 is what one does instead.

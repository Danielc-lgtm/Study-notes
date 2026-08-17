---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Self-Adjoint Operator"
  - "Def - Transition Density and Heat Kernel"
tags: [paper, functional-analysis, dirichlet-forms]
---

# Signature

| symbol | type |
|---|---|
| $(E,m)$ | locally compact separable metric space; $m$ Radon of full support |
| $\mathcal{F}$ | dense linear subspace of $L^2(E,m)$ |
| $\mathcal{E}$ | $\mathcal{F}\times\mathcal{F}\to\mathbb{R}$; symmetric bilinear, $\mathcal{E}(u,u)\geq0$ |
| $\mathcal{E}_1$ | the form norm: $\mathcal{E}_1(u,u):=\mathcal{E}(u,u)+\lVert u\rVert^2_{L^2}$ |
| $A$ | non-negative self-adjoint on $L^2(E,m)$; $\operatorname{Dom}(A^{1/2})=\mathcal{F}$ |
| $C_c(E)$ | continuous compactly supported functions $E\to\mathbb{R}$ |
| $u^\sharp$ | the unit contraction $u^\sharp:=(0\vee u)\wedge1$ |
| $\mathcal{E}_{X'}$ | the part form on open $X'\subseteq E$: $\mathcal{F}_{X'}=\overline{\{u\in\mathcal{F}\cap C_c(E):\operatorname{supp}u\subseteq X'\}}^{\,\mathcal{E}_1}$ |

---

# Definition

> **Definition (regular symmetric Dirichlet form).** A pair $(\mathcal{E},\mathcal{F})$ on $L^2(E,m)$ with $\mathcal{E}$ symmetric bilinear and non-negative on a dense $\mathcal{F}$ is a **regular symmetric Dirichlet form** if
> **(D1) Closed.** $(\mathcal{F},\mathcal{E}_1)$ is complete.
> **(D2) Markovian.** $\ \forall u\in\mathcal{F}:\ u^\sharp\in\mathcal{F}$ and $\mathcal{E}(u^\sharp,u^\sharp)\leq\mathcal{E}(u,u)$, where $u^\sharp=(0\vee u)\wedge1$.
> **(D3) Regular.** $\mathcal{F}\cap C_c(E)$ is dense in $\mathcal{F}$ for $\mathcal{E}_1$, and dense in $C_c(E)$ for $\lVert\cdot\rVert_\infty$.

> **(F1) Generator.** (D1) alone gives a unique non-negative self-adjoint $A$ on $L^2(E,m)$ with
> $$\mathcal{F}=\operatorname{Dom}(A^{1/2}),\qquad \mathcal{E}(u,v)=\langle A^{1/2}u,A^{1/2}v\rangle,\qquad \mathcal{E}(u,v)=\langle Au,v\rangle\ \ (u\in\operatorname{Dom}A,\ v\in\mathcal{F}),$$
> hence a strongly continuous contraction semigroup $e^{-tA}$.
>
> **(F2) Standing extra hypothesis of the paper.** $e^{-tA}$ admits a [[Def - Transition Density and Heat Kernel|transition density]] $p^{\mathcal{E}}$ against $m$, i.e. satisfying (D1)–(D3) there. **This is not implied by (D1)–(D3) above** and is assumed throughout.
>
> **(F3) Part form and killing.** For $X'\subseteq E$ open, $\mathcal{E}_{X'}$ is the Dirichlet form of the process killed on leaving $X'$, and its bridge measures are the ambient ones restricted to $\{\omega:\omega([0,t])\subseteq X'\}$.

**Gloss.** (D2) is the analytic shadow of "the semigroup preserves $0\leq u\leq1$", i.e. of the process being a Markov process rather than an arbitrary $L^2$ flow.

> [!warning] Which clause does what
> (D1) $\Rightarrow$ (F1): a generator exists. (D2) $\Rightarrow$ the generator generates a *Markov process*. (D3) $\Rightarrow$ [[Ext - Fukushima Correspondence|(FK)]] applies, so that process is a Hunt process, unique q.e. **Symmetry** of $\mathcal{E}$ $\Rightarrow$ $A$ self-adjoint $\Rightarrow$ $p^{\mathcal{E}}(t,x,y)=p^{\mathcal{E}}(t,y,x)$, used silently whenever a bridge from $x$ to $y$ is exchanged for one from $y$ to $x$.

---

# Type card

> [!abstract] Type card — regular symmetric Dirichlet form
> **Given.** **(H1)** $(E,m)$ locally compact separable metric with $m$ Radon of full support. **(H2)** $\mathcal{E}$ symmetric bilinear non-negative on dense $\mathcal{F}\subseteq L^2(E,m)$ satisfying (D1),(D2),(D3).
>
> **Produces.** A non-negative self-adjoint $A$ with $\operatorname{Dom}(A^{1/2})=\mathcal{F}$; a contraction semigroup $e^{-tA}$; and, via [[Ext - Fukushima Correspondence|(FK)]], an $m$-symmetric Hunt process on $E$, unique up to quasi-everywhere equivalence.
>
> **Lets you.** State "any process for which the loop-measure construction runs" as a checkable condition on a quadratic form, and manufacture new members of the class by [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms|subordination]].

---

# Depends on

- [[Def - Self-Adjoint Operator]], [[Thm - Complex Spectral Theorem]] — for (F1)
- [[Def - Transition Density and Heat Kernel]] — for (F2)
- [[Ext - Fukushima Correspondence]] — for the process
- 🟢 closed quadratic forms, form cores, $L^2$ semigroups — *Functional Analysis*

---

# Checks

**Instance.** $E=X$ a Riemannian surface, $m=\operatorname{vol}_g$, $\mathcal{F}=H^1(X)$ (or $H^1_0(X)$ with Dirichlet conditions), $\mathcal{E}(u,u)=\int_X\lvert\nabla u\rvert^2\,\mathrm{d}\operatorname{vol}_g$. (D1): $H^1$ is complete. (D2): $\lvert\nabla u^\sharp\rvert\leq\lvert\nabla u\rvert$ pointwise. (D3): $C_c^\infty$ is a core. $A=\Delta_X$, $p^{\mathcal{E}}=p_X$. Adding a killing rate: $\mathcal{E}^\kappa(f,f)=\int_X\lvert\nabla f\rvert^2\,\mathrm{d}\operatorname{vol}_g+\kappa\int_Xf^2\,\mathrm{d}\operatorname{vol}_g$, $A=\Delta_X+\kappa$, $p^{\mathcal{E}}=e^{-\kappa t}p_X$.

**Non-instance (fails symmetry).** A non-symmetric Dirichlet form (Ma–Röckner) still satisfies analogues of (D1)–(D3) and generates a semigroup, but $A$ is not self-adjoint and $p(t,x,y)\neq p(t,y,x)$ in general. Consequence: the loop-measure construction breaks, since $\int_XW^t_{x\to x}\,\mathrm{d}m(x)$ is no longer the natural object and the shift-invariance of [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure|(LJ)]] fails.

**Non-instance (fails F2).** The form of a compound Poisson subordinate process satisfies (D1)–(D3) but has no transition density — see [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]]. Every formula from §2.4 onward then has no left-hand side.

---

# Used at

- [[Constr - The Dirichlet-Form Loop Measure]] — Definition 2.2 is stated for exactly this class
- [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms]] — the subordinate object is again of this class
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — as (H1), with $\Gamma$-invariance added
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — same on $\mathbb{H}^3$
- [[Constr - The Brownian Loop Measure]] — restriction (P1) there is (F3) here

---

# Commentary

> [!note]- Commentary (skippable)
> The reason to phrase the hypothesis as a condition on a form rather than on a process is that "which processes work?" becomes checkable. §2.1 built a loop measure from a heat kernel and its bridges, and nothing in that recipe was about Brownian motion; the class for which it runs is exactly this one, by (FK).
>
> The paper notes that the non-symmetric theory exists but "has fewer connections to Markov processes". Concretely: symmetry is what gives self-adjointness, which gives $p(t,x,y)=p(t,y,x)$, which is what makes the diagonal $p(t,x,x)$ the right thing to integrate and makes the parametrised loop measure shift-invariant.

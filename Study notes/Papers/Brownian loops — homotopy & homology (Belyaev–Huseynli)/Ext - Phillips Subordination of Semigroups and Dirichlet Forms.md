---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, probability, subordination, dirichlet-forms]
---

# Signature

| symbol | type |
|---|---|
| $A$ | non-negative self-adjoint on $L^2(X,\operatorname{vol}_g)$; generator of $(\mathcal{E},\mathcal{F})$ |
| $\phi$ | Bernstein, triple $(a,b,\nu)$; $\psi^\phi_t$ the subordinator law on $[0,\infty)$ |
| $\phi(A)$ | non-negative self-adjoint on $L^2(X,\operatorname{vol}_g)$, by functional calculus of $A$ |
| $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ | the subordinate Dirichlet form on $L^2(X,\operatorname{vol}_g)$ |
| $p^{\mathcal{E}},\ p^\phi$ | transition densities of $e^{-tA}$, $e^{-t\phi(A)}$ against $\operatorname{vol}_g$ |
| $\lVert\cdot\rVert,\ \langle\cdot,\cdot\rangle$ | norm and inner product of $L^2(X,\operatorname{vol}_g)$ |
| $\rho$ | hyperbolic area measure on $\mathbb{H}^2$ |

---

# Statement

> **(PH) Subordination of a semigroup and its form.** *Precondition:*
> **(P1)** $(\mathcal{E},\mathcal{F})$ a [[Def - Regular Symmetric Dirichlet Form|regular symmetric Dirichlet form]] on $L^2(X,\operatorname{vol}_g)$, generator $A\geq0$ self-adjoint;
> **(P2)** $\phi$ a [[Def - Bernstein Function|Bernstein function]] with triple $(a,b,\nu)$ and subordinator law $\psi^\phi_t$;
> **(P3)** the [[Def - Subordinator|subordinator]] is **independent** of the process of $(\mathcal{E},\mathcal{F})$.
>
> *Conclusion:*
> **(C1) Semigroup.** $\displaystyle e^{-t\phi(A)}=\int_{[0,\infty)}e^{-sA}\,\psi^\phi_t(\mathrm{d}s)$ for $t\geq0$, as bounded operators on $L^2$. $\ \ (3)$
> **(C2) Operator.** $\displaystyle \phi(A)=aI+bA+\int_0^\infty\big(I-e^{-sA}\big)\,\nu(\mathrm{d}s)$; the generator of the subordinate process is $-\phi(A)$.
> **(C3) Density.** If $p^{\mathcal{E}}$ exists then, whenever $\psi^\phi_t(\{0\})=0$,
> $$p^\phi(t,x,y)=\int_{[0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s).\qquad(4)$$
> **(C4) Form.** The subordinate process is again a $\operatorname{vol}_g$-symmetric Hunt process, associated with a regular symmetric Dirichlet form $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ on $L^2(X,\operatorname{vol}_g)$:
> $$\mathcal{E}^\phi(u,u)=a\lVert u\rVert^2+b\,\mathcal{E}(u,u)+\int_0^\infty\Big(\lVert u\rVert^2-\langle e^{-sA}u,u\rangle\Big)\,\nu(\mathrm{d}s),\qquad \mathcal{F}^\phi=\{u\in L^2:\mathcal{E}^\phi(u,u)<\infty\}.\qquad(5)$$
> **(C5) Invariance transfers.** If a group $G$ acts on $X$ with $p^{\mathcal{E}}(t,hz,hw)=p^{\mathcal{E}}(t,z,w)$ for all $h\in G$, then the same holds for $p^\phi$.

> [!warning] (C3) has a hypothesis
> $\psi^\phi_t(\{0\})=0$ is **not** automatic. Without it, $e^{-t\phi(A)}$ has an atom on the diagonal and no density exists. This is exactly [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|(A2.3)]].

---

# Type card

> [!abstract] Type card — (PH)
> **Given.** (P1),(P2),(P3).
>
> **Produces.** $e^{-t\phi(A)}$ as a $\psi^\phi_t$-average (C1); its generator (C2); its density (C3), conditionally; its Dirichlet form (C4), explicitly, with the three terms matching the triple $(a,b,\nu)$; and transfer of any kernel invariance (C5).
>
> **Lets you.** Apply [[Constr - The Dirichlet-Form Loop Measure|Definition 2.2]] to $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ — the whole of §2.4 — and periodise $p^\phi_{\mathbb{H}^2}$ over $\Gamma$ in §3, which needs (C5).

---

# Status

- **Proved here:** no.
- **Source:** Schilling–Song–Vondraček, *Bernstein functions*, Ch. 12–13 (semigroup side); Fukushima–Oshima–Takeda (form side, for (C4)).
- **DAG node that would close this:** *Stochastic Analysis* (⭐🔵) with *Functional Analysis* (🟢); (C1)–(C2) are the classical Phillips subordination theorem and are essentially functional calculus.
- **What is safe to assume:** (C1)–(C5) verbatim under (P1)–(P3), with (C3) additionally requiring $\psi^\phi_t(\{0\})=0$. No proof in the paper unfolds any of them; in every concrete case (4) and (5) are written out directly.

---

# Used at

- [[Def - Subordinator]] — for what $Y$'s generator and form are
- [[Constr - The Subordinate Brownian Loop Measure]] — (C4) supplies $(\mathcal{E}^\phi,\mathcal{F}^\phi)$; (C3) supplies $p^\phi$
- [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]] — (C3), i.e. (4), is the substitution the proof begins with
- [[Constr - The Periodised Kernel]] — (C5): $\Delta_{\mathbb{H}^2}$ is $\mathrm{PSL}(2,\mathbb{R})$-invariant and $\phi$ acts by functional calculus, so $p^\phi_{\mathbb{H}^2}$ is $\mathrm{PSL}(2,\mathbb{R})$-invariant
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]], [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — (4) expands the kernel in Step 1

---

# Commentary

> [!note]- Commentary (skippable)
> Read (5) against the triple: the three terms are killing, surviving diffusive part, and jump part, in the same order as in $\phi$ itself. That correspondence is the reason (F3) on [[Def - Bernstein Function]] can read qualitative behaviour off $\phi$ without touching the process.
>
> (C5) is a one-line remark in the paper — "since $\Delta_{\mathbb{H}^2}$ is $\mathrm{PSL}(2,\mathbb{R})$-invariant, so is $p^\phi_{\mathbb{H}^2}$" — but it is load-bearing: without it §3 cannot periodise, and the entire homotopy decomposition is unavailable for subordinate processes. It holds because $\phi(A)$ is defined by functional calculus, which commutes with any unitary conjugation preserving $A$.

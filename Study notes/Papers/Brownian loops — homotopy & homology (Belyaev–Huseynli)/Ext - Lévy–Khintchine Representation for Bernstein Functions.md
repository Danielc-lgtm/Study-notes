---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, probability, subordination]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | $(0,\infty)\to[0,\infty)$, $C^\infty$, with $(-1)^{n-1}\phi^{(n)}\geq0$ for $n\geq1$ |
| $a,b$ | $\in[0,\infty)$ |
| $\nu$ | measure on $(0,\infty)$ |
| $S_t$ | an increasing Lévy process on $[0,\infty)$, possibly killed at constant rate |
| $\psi^\phi_t$ | law of $S_t$; measure on $[0,\infty)$ with $\lvert\psi^\phi_t\rvert=e^{-at}$ |

---

# Statement

> **(LK) Lévy–Khintchine representation for Bernstein functions.** *Precondition:*
> **(P1)** $\phi\in C^\infty(0,\infty)$, $\phi\geq0$;
> **(P2)** $(-1)^{n-1}\phi^{(n)}(\lambda)\geq0$ for all $n\geq1$, $\lambda>0$.
>
> *Conclusion:* there is a **unique** triple $(a,b,\nu)$ with $a,b\geq0$ and $\nu$ a measure on $(0,\infty)$ satisfying $\int_0^\infty(1\wedge s)\,\nu(\mathrm{d}s)<\infty$, such that
> $$\phi(\lambda)=a+b\lambda+\int_0^\infty\big(1-e^{-\lambda s}\big)\,\nu(\mathrm{d}s),\qquad\lambda>0.\tag{1}$$
> Conversely every such triple defines a $\phi$ satisfying (P1),(P2).

> **(LK′) Subordinator correspondence.** Under (P1),(P2) there is an increasing Lévy process $S_t$ on $[0,\infty)$, possibly killed at constant rate $a$, with
> $$\mathbb{E}\big[e^{-\lambda S_t}\big]=e^{-t\phi(\lambda)},\qquad\lambda>0,\ t\geq0,\tag{2}$$
> unique in law. Its law $\psi^\phi_t$ satisfies $\lvert\psi^\phi_t\rvert=e^{-at}$: a probability measure iff $a=0$ (**conservative**), a sub-probability measure otherwise.

> [!warning] Integrability of $\nu$
> The condition $\int_0^\infty(1\wedge s)\,\nu(\mathrm{d}s)<\infty$ is what makes (1) converge, and it is two conditions: near $s=0$, $1-e^{-\lambda s}\approx\lambda s$, so small jumps must be integrable against $s$; near $s=\infty$, $1-e^{-\lambda s}\approx1$, so large jumps must be finite in number. **It does not force $\nu(0,\infty)<\infty$**, and the $\alpha$-stable case has $\nu_\alpha(0,\infty)=\infty$.

---

# Type card

> [!abstract] Type card — (LK), (LK′)
> **Given.** (P1),(P2).
>
> **Produces.** A unique triple $(a,b,\nu)$ and, up to law, a unique subordinator $S$ with Laplace exponent $\phi$; hence the family $\{\psi^\phi_t\}_{t\geq0}$ of sub-probability measures on $[0,\infty)$.
>
> **Lets you.** Read qualitative behaviour of the subordinate process directly off $\phi$: killing from $a$, surviving diffusive part from $b$, jumps from $\nu$. And write $\psi^\phi_t$, which every formula from §2.4 onward integrates against.

---

# Status

- **Proved here:** no.
- **Source:** Schilling–Song–Vondraček, *Bernstein functions*, 2nd ed., de Gruyter Studies in Mathematics 37, 2012, Ch. 3.
- **DAG node that would close this:** none needed — this is the subordinator specialisation of the Lévy–Khintchine formula, anchor material from *Advanced Probability* (🟢) and *SDEs* (🟢).
- **What is safe to assume:** the bijection $\phi\leftrightarrow(a,b,\nu)\leftrightarrow S$ and (2). No proof in the paper unfolds any of it; the four explicit cases are verified by direct computation of $\psi^\phi_t$.

---

# Used at

- [[Def - Bernstein Function]] — (F2), and the reading of the triple
- [[Def - Subordinator]] — (LK′) is the definition of the subordinator attached to $\phi$
- [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]] — (A2.3) is a condition on $(b,\nu)$, and the equivalence of its three forms is standard subordinator theory
- [[Constr - The Weighted Potential Measure Vϕ]] — the four values of $\psi^\phi_t$ come from here

---

# Commentary

> [!note]- Commentary (skippable)
> The direction that matters in the paper is (P1),(P2) $\Rightarrow$ triple: given $\phi$, know the process. The converse is used implicitly once, to see that $(\lambda+\kappa)^{\alpha/2}$ is Bernstein by exhibiting it as a composition rather than by differentiating it $n$ times — a *complete* Bernstein function, being $\lambda\mapsto\lambda+\kappa$ followed by $u\mapsto u^{\alpha/2}$.
>
> Worth noting what (LK′) does *not* deliver: a transition density for the subordinate semigroup. That requires $\psi^\phi_t(\{0\})=0$, which is a further condition on $(b,\nu)$ and is exactly Assumption 2.3.

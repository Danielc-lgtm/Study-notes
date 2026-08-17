---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, probability]
---

# Signature

| symbol | type |
|---|---|
| $(\mathcal{L},\mathcal{A},\nu)$ | a measurable space with a $\sigma$-finite measure; here $\nu=\lambda\mu^\kappa_X$ |
| $\Pi$ | a Poisson point process on $\mathcal{L}$ with intensity $\nu$ |
| $F$ | $\mathcal{L}\to\mathbb{C}$ measurable, with $\int_{\mathcal{L}}\lvert e^{F}-1\rvert\,\mathrm{d}\nu<\infty$ |

---

# Statement

> **(EF) Exponential formula (Campbell).** *Precondition:*
> **(P1)** $\Pi$ Poisson with $\sigma$-finite intensity $\nu$ on $\mathcal{L}$;
> **(P2)** $F:\mathcal{L}\to\mathbb{C}$ measurable;
> **(P3)** $\displaystyle\int_{\mathcal{L}}\big\lvert e^{F(\eta)}-1\big\rvert\,\nu(\mathrm{d}\eta)<\infty$.
>
> *Conclusion:*
> $$\mathbb{E}\Big[\prod_{\eta\in\Pi}e^{F(\eta)}\Big]=\exp\Big(\int_{\mathcal{L}}\big(e^{F(\eta)}-1\big)\,\nu(\mathrm{d}\eta)\Big).\tag{EF}$$

> **(F1) Atomic form.** If $\nu=\sum_{j}\nu_j\delta_{A_j}$ on disjoint classes and $F\equiv F_j$ on $A_j$, then (EF) reads $\prod_j\exp\big(\nu_j(e^{F_j}-1)\big)$ — the product over classes of the Poisson generating functions. This is the only form used in the paper.
>
> **(F2) Unitary case.** If $\lvert e^{F}\rvert=1$ (e.g. $F=\log\chi$ for a unitary character $\chi$), (P3) reduces to $\nu(\mathcal{L})<\infty$ — which is exactly [[Thm - Finiteness of the Total Mass|Cor 4.7]]. Then (EF) is an identity between two absolutely convergent objects and requires no further care.

> [!warning] (P3) is not automatic and is not "$\nu$ finite"
> The integrand is $e^F-1$, not $e^F$. On a soup with $\nu(\mathcal{L})=\infty$ (which is the case for the full loop measure) (EF) can still hold, because $e^F-1$ vanishes where $F$ does. In this paper the restriction to $\mathcal{L}^*_\lambda$ — non-contractible, non-peripheral loops — makes $\nu$ genuinely finite, and (P3) is discharged by (F2).

---

# Type card

> [!abstract] Type card — (EF)
> **Given.** (P1),(P2),(P3).
>
> **Produces.** The identity (EF): the expected value of a multiplicative functional over the points equals $\exp$ of an integral. Type: $\mathbb{C}$-valued equality.
>
> **Lets you.** Turn a **sum over the random points** into an **integral against the intensity** — i.e. compute $\mathbb{E}[\chi(\beta(\lambda))]$ from the class masses alone. Combined with [[Thm - Selberg L-Function Identity|Cor 6.4]] this produces $L_X(s,\chi)^{-\lambda}$.

---

# Status

- **Proved here:** no.
- **Source:** standard; Kingman, *Poisson Processes*, §3.2; Last–Penrose, *Lectures on the Poisson Process*, Thm 3.9.
- **DAG node that would close this:** 🟢 *Advanced Probability / Measure-Theoretic Probability* (7,9). **Not a gap.**
- **What is safe to assume:** (EF),(F1),(F2) as stated. The paper uses only the case $F=\log\chi([\eta])$ with $\chi$ unitary and $\nu$ finite.
- **Scope:** used once, in [[Thm - Distribution of the Total Homology of the Loop Soup|Prop 6.7]].

---

# Used at

- [[Thm - Distribution of the Total Homology of the Loop Soup]] — the sole consumer
- [[Constr - The Loop Soup]] — (P1) is its output
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.3

---

# Commentary

> [!note]- Commentary (skippable)
> (EF) is the reason the answer in §6.3 is a **zeta function to a power** rather than something messier. Write $F(\eta)=\log\chi([\eta])$; then $\prod_\eta e^{F(\eta)}=\chi(\beta(\lambda))$ where $\beta(\lambda)=\sum_\eta[\eta]$ is the total homology. By (F1) the right-hand side of (EF) is a sum over classes $(\gamma,m)$ of $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))(\chi([\gamma^m])-1)$, and that sum is precisely $\log L_X(s,\chi)-\log Z_X(s)$ by the §6.3 identities. Exponentiating gives $\big(L_X(s,\chi)/Z_X(s)\big)^{-\lambda}$.
>
> So the Euler product of the $L$-function and the independence of disjoint Poisson counts are, in this paper, the same statement written in two notations.

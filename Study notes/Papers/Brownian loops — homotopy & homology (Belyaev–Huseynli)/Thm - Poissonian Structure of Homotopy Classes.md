---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Loop Soup"
  - "Def - Free Homotopy Class and Conjugacy Class Correspondence"
tags: [paper, probability, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\mathcal{L}_c$ | the loop soup of intensity $c>0$ ([[Constr - The Loop Soup]]) |
| $N_{\gamma,m}$ | $:=\#\{\eta\in\mathcal{L}_c:\eta\in\mathcal{C}_X(\gamma^m)\}$; $\mathbb{Z}_{\geq0}$-valued |
| $\gamma$ | $\in\mathcal{P}_X$, a primitive class; $m\geq1$ |
| $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ | $\in(0,\infty)$ — computed in closed form by [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces\|Thm 3.5]] |

---

# Type card

> [!abstract] Type card — Proposition 3.8
> **Given.**
> **(H1)** $\phi$ Bernstein with [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]; $c>0$; $\mathcal{L}_c$ the loop soup.
> **(H2)** $\gamma\in\mathcal{P}_X$, $m\geq1$ — so $\mathcal{C}_X(\gamma^m)$ is a non-trivial, non-peripheral class, and $\mu^\phi_X(\mathcal{C}_X(\gamma^m))<\infty$.
> **(H3)** for jump $\phi$: $\mathcal{L}_c$ is the **marked** soup of [[Constr - The Loop Soup|(P4)]].
>
> **Produces.** $N_{\gamma,m}\sim\mathrm{Poisson}\big(c\,\mu^\phi_X(\mathcal{C}_X(\gamma^m))\big)$, and for any finite family of pairwise distinct classes, **joint independence** of the corresponding counts.
>
> **Lets you.** Replace every "mass" statement of §3–§4 by a distributional one at zero extra cost, and factor any multiplicative functional over classes into a product — the mechanism behind §6.3.

---

# Statement

> **Proposition 3.8 (Poissonian structure of homotopy classes).** Assume (H1)–(H3). Then
> $$N_{\gamma,m}\ \sim\ \mathrm{Poisson}\Big(c\,\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)\Big),$$
> and for pairwise distinct classes $\mathcal{C}_1,\dots,\mathcal{C}_k$ the variables $N_{\mathcal{C}_1},\dots,N_{\mathcal{C}_k}$ are **jointly independent**.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Def - Free Homotopy Class and Conjugacy Class Correspondence\|(F1)]] | distinct pairs $(\gamma,m)$ | distinct classes are **disjoint** subsets of $\mathcal{L}$ |
| [[Constr - The Loop Soup\|(P2)]] | $A=\mathcal{C}_X(\gamma^m)$, finite mass | the Poisson law of $N_{\gamma,m}$ |
| [[Constr - The Loop Soup\|(P3)]] | the disjoint family | joint independence |
| [[Constr - The Loop Soup\|(P4)]] | jump $\phi$ | measurability of the class, same intensity |
| [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces\|Thm 3.5]] | $(\gamma,m)$ | the mean, in closed form |

---

# Proof

**Strategy.** There is nothing to prove beyond checking the hypothesis of the Poisson point process axioms: distinct classes are disjoint measurable sets of finite mass.

> [!note]- Proof (skippable)
> Free homotopy classes partition the non-contractible non-peripheral loops, so distinct classes are **disjoint**; they are measurable by definition of the $\sigma$-algebra on $\mathcal{L}$ (for jump processes, after passing to marked loops, (H3)). Their masses are finite by Theorem 3.5. Both assertions are then the defining properties (P2),(P3) of a Poisson point process. $\;\square$

---

# What this assumes, and where to climb

- **Finiteness of each class mass** — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]]. Without it (P2) says nothing: a class of infinite mass contains infinitely many loops almost surely.
- **Disjointness, not just distinctness** — [[Def - Free Homotopy Class and Conjugacy Class Correspondence]]. Two classes are either equal or disjoint because "freely homotopic" is an equivalence relation; independence is a consequence of *disjointness*, not of any probabilistic estimate.
- **Measurability for jump processes** — Remark 3.1, [[Constr - The Loop Soup|(P4)]]. This is the only non-formal ingredient.
- **Not assumed:** any summability over classes. The proposition is finite-family; the infinite sums appear only in §4 and §6, where [[Thm - Finiteness of the Total Mass|Cor 4.7]] does the work.
- **The measure being sampled** — [[Constr - The Brownian Loop Measure]] and [[Constr - The Subordinate Brownian Loop Measure]]; the soup's intensity is one of these.
- **The marked construction for jump $\phi$** — [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] is where Remark 3.1's measurability problem and its fix are set out.

---

# Consumed by

- [[§3.3 The Loop Soup and its Poissonian Structure]]
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — independence across classes is what factors the characteristic function
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.3

---

# Commentary

> [!note]- Commentary (skippable)
> The proposition is a one-line consequence of the definition of a Poisson point process, and the paper proves it in two sentences. Its value is entirely in the interface: it is the point where the paper stops computing numbers and starts computing **laws**.
>
> The independence is worth pausing on because it is stronger than it looks. Loops in different free homotopy classes are geometrically entangled — they cross, they share the same surface — but the soup has no interaction, so counting them is independent. That is a property of the Poissonian model, not of hyperbolic geometry, and it is what allows $\mathbb{E}\big[\prod_\eta e^{F(\eta)}\big]$ to factor into $\exp\big(\lambda\sum_{\gamma,m}(\cdots)\big)$ in §6.3 — which is exactly the Euler-product shape of a Selberg $L$-function. The zeta functions of §4 and the independence here are the same fact seen twice.

---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Loop Soup"
  - "Ext - Exponential Formula for Poisson Point Processes"
  - "Thm - Selberg L-Function Identity"
tags: [paper, probability, zeta-functions]
---

# Signature

| symbol | type |
|---|---|
| $\mathcal{L}_\lambda$ | the loop soup of intensity $\lambda>0$, intensity measure $\lambda\mu^\kappa_X$ |
| $\mathcal{L}^*_\lambda$ | the loops of $\mathcal{L}_\lambda$ that are **non-contractible and not homotopic into a cusp** |
| $[\eta]$ | $\in H_1(X,\mathbb{Z})$, the homology class of a loop $\eta$ |
| $\beta(\lambda)$ | $:=\sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]\in H_1(X,\mathbb{Z})$ — the **total homology**, a random element of $\mathbb{Z}^r$ |
| $s$ | $=\tfrac12+\sqrt{\tfrac14+\kappa}$, $\mathrm{Re}(s)>\delta$ |
| $L_X(s,\chi)^{-\lambda}$ | $:=\exp\big(-\lambda\log L_X(s,\chi)\big)$, with $\log L_X(s,\chi)$ given by (76) |

---

# Type card

> [!abstract] Type card — Proposition 6.7
> **Given.**
> **(H1)** $\kappa$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, $\mathrm{Re}(s)>\delta$.
> **(H2)** $\mathcal{L}_\lambda$ the loop soup of intensity $\lambda>0$; $\mathcal{L}^*_\lambda$ its non-contractible, non-peripheral part.
> **(H3)** $\#\mathcal{L}^*_\lambda\sim\mathrm{Poisson}\big(-\lambda\log Z_X(s)\big)$, **finite** — so $\beta(\lambda)$ is a finite sum. *(From [[Thm - Finiteness of the Total Mass|Cor 4.7]] and [[Thm - Poissonian Structure of Homotopy Classes|Prop 3.8]].)*
>
> **Produces.** The characteristic function on the character torus and its inversion:
> $$\mathbb{E}\big[\chi(\beta(\lambda))\big]=\left(\frac{Z_X(s)}{L_X(s,\chi)}\right)^{\!\lambda},\tag{80}$$
> $$\mathbb{P}\big(\beta(\lambda)=\beta\big)=Z_X(s)^{\lambda}\int_{\widehat{H_1(X,\mathbb{Z})}}L_X(s,\chi)^{-\lambda}\,\overline{\chi(\beta)}\,\mathrm{d}\chi.\tag{81}$$
>
> **Lets you.** Write the **full law** of a topological random variable — the total homology of a random collection of loops — as an explicit integral of Selberg $L$-functions. This is the paper's terminal result on homology.

---

# Statement

> **Proposition 6.7 (distribution of the total homology of the loop soup).** Assume (H1)–(H3). Then (80) holds for every unitary $\chi\in\widehat{H_1(X,\mathbb{Z})}$, and (81) holds for every $\beta\in H_1(X,\mathbb{Z})$.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - Finiteness of the Total Mass\|Cor 4.7]] + [[Thm - Poissonian Structure of Homotopy Classes\|Prop 3.8]] | $\mathcal{L}^*_\lambda$ | $\#\mathcal{L}^*_\lambda\sim\mathrm{Poisson}(-\lambda\log Z_X(s))<\infty$ a.s.; $\beta(\lambda)$ well defined |
| [[Ext - Exponential Formula for Poisson Point Processes\|(EF)]] | $e^{F(\eta)}=\chi([\eta])$, intensity $\lambda\mu^\kappa_X$ | $\mathbb{E}\big[\prod_\eta e^{F(\eta)}\big]=\exp\big(\lambda\int(e^F-1)\,\mathrm{d}\mu^\kappa_X\big)$ |
| $\prod_{\eta\in\mathcal{L}^*_\lambda}\chi([\eta])=\chi\big(\sum_\eta[\eta]\big)$ | $\chi$ a homomorphism | $=\chi(\beta(\lambda))$ |
| [[Thm - Selberg L-Function Identity\|(76)]] at $\chi$ | $\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X$ | $-\log L_X(s,\chi)$ |
| [[Thm - Selberg L-Function Identity\|(76)]] at $\chi\equiv1$ | $\sum_{\gamma,m}\mu^\kappa_X$ | $-\log Z_X(s)$ |
| [[Ext - Orthogonality of Characters on a Compact Abelian Group\|(OC)]] | multiply (80) by $\overline{\chi(\beta)}$, integrate | (81) |

---

# Proof

**Strategy.** The exponential formula turns a product over the random loops into $\exp$ of an integral against the intensity; that integral is $\sum_{\gamma,m}(\chi([\gamma])^m-1)\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$, i.e. **(76) at $\chi$ minus (76) at the trivial character**. Then invert.

> [!note]- Proof (skippable)
> For a Poisson process of intensity $\lambda\mu^\kappa_X$ and measurable $F$ on loops, (EF) gives
> $$\mathbb{E}\Big[\prod_{\eta\in\mathcal{L}_\lambda}e^{F(\eta)}\Big]=\exp\Big(\lambda\int\big(e^{F(\eta)}-1\big)\,\mu^\kappa_X(\mathrm{d}\eta)\Big).$$
> Apply this with $e^{F(\eta)}=\chi([\eta])$ for $\eta\in\mathcal{L}^*_\lambda$ (and $e^F=1$ elsewhere, so those loops drop out of the integrand). Since $\chi$ is a homomorphism, $\prod_\eta e^{F(\eta)}=\chi\big(\sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]\big)=\chi(\beta(\lambda))$. The right-hand side is
> $$\exp\Big(\lambda\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\big(\chi([\gamma])^m-1\big)\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)\Big)=\exp\big(-\lambda\log L_X(s,\chi)+\lambda\log Z_X(s)\big)=\Big(\frac{Z_X(s)}{L_X(s,\chi)}\Big)^{\lambda},$$
> by the Selberg $L$-function identity applied to $\chi$ and to the trivial character. This is (80). Multiplying by $\overline{\chi(\beta)}$ and integrating over $\widehat{H_1(X,\mathbb{Z})}$, orthogonality isolates the class $\beta$ and gives (81). $\;\square$

---

# What this assumes, and where to climb

- **Finiteness of $\#\mathcal{L}^*_\lambda$** — without it $\beta(\lambda)$ is an infinite sum in $\mathbb{Z}^r$ with no meaning. It comes from [[Thm - Finiteness of the Total Mass|Cor 4.7]], hence from $s>\delta$, hence (in finite area) from $\kappa>0$.
- **(EF)'s precondition (P3)** — discharged by [[Ext - Exponential Formula for Poisson Point Processes|(F2)]]: $\lvert e^F\rvert=\lvert\chi\rvert=1$ and $\mu^\kappa_X$ restricted to $\mathcal{L}^*$ is finite.
- **$\chi$ a homomorphism** — this is what converts a **product over loops** into a **character of a sum of homology classes**. The entire proposition rests on that one line.
- **Complex powers** — $L_X(s,\chi)^{-\lambda}:=\exp(-\lambda\log L_X(s,\chi))$ with $\log L_X$ **defined by the series (76)**, not by a branch choice. Inside $\mathrm{Re}(s)>\delta$ the series converges, so no ambiguity arises.
- **Not assumed:** any continuation of $L_X$, or the Jacobian identification.

---

# Consumed by

- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.3
- Nothing further. This is the last result of §6.

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: a character turns the sum defining $\beta(\lambda)$ into a product over loops, the exponential formula turns that product into an integral against the intensity, and the Selberg $L$-function identity evaluates the integral.** Three substitutions, no estimates.
>
> The result is the sharpest form of the paper's programme. §3 computed masses; §4 summed them; §6.1 normalised them into a probability measure on classes; and here the loop soup makes a genuinely random topological object — the total homology of infinitely many Brownian loops — whose distribution is given in closed form by $\big(Z_X/L_X\big)^\lambda$. That is a *complete* answer: the characteristic function on the whole dual group, hence the law.
>
> Worth noting how the two "$-1$"s conspire. (EF) integrates $e^F-1$, and the $-1$ contributes $-\lambda\sum_{\gamma,m}\mu^\kappa_X=+\lambda\log Z_X(s)$; the $e^F=\chi$ contributes $-\lambda\log L_X(s,\chi)$. So the numerator $Z_X(s)^\lambda$ in (80) is not a normalisation added by hand — it is the compensator that the exponential formula requires, and it is precisely what makes $\mathbb{E}[\chi(\beta(\lambda))]=1$ at the trivial character, as any characteristic function must.

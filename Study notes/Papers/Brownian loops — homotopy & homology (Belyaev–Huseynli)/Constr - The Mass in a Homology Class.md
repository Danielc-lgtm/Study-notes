---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Character Torus and the Pontryagin Dual"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
tags: [paper, probability, algebraic-topology]
---

# Signature

| symbol | type |
|---|---|
| $\beta$ | $\in H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$ |
| $[\gamma]$ | image of $\gamma\in\mathcal{P}_X$ in $H_1(X,\mathbb{Z})$; $[\gamma^m]=m[\gamma]$ |
| $\mu^\kappa_X(\beta)$ | $\in[0,\infty)$ — the mass in the homology class $\beta$ |
| $s$ | $=\tfrac12+\sqrt{\tfrac14+\kappa}$, $\mathrm{Re}(s)>\delta$ |

---

# Construction

> **Definition 6.1 (mass in a homology class).** For $\beta\in H_1(X,\mathbb{Z})$,
> $$\mu^\kappa_X(\beta):=\sum_{\substack{\gamma\in\mathcal{P}_X,\ m\geq1\\ m[\gamma]=\beta}}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)=\sum_{\substack{\gamma\in\mathcal{P}_X,\ m\geq1\\ m[\gamma]=\beta}}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.\tag{74}$$

> **(P1) Finiteness and summability.** $0\leq\mu^\kappa_X(\beta)\leq\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=-\log Z_X(s)<\infty$ under $s>\delta$, and $\sum_{\beta}\mu^\kappa_X(\beta)=-\log Z_X(s)$ — the index sets $\{(\gamma,m)\}$ partition according to $m[\gamma]$. *Consumer:* [[Ext - Orthogonality of Characters on a Compact Abelian Group|(OC)(F1)]]'s absolute-summability hypothesis.
>
> **(P2) It is a pushforward.** $\mu^\kappa_X(\cdot)$ on $H_1(X,\mathbb{Z})$ is the image of the class masses under $(\gamma,m)\mapsto m[\gamma]$. Normalising by $-\log Z_X(s)$ gives the pushforward of $\mathbb{P}_s$. *Consumer:* §6.2's probabilistic reading.
>
> **(P3) Infinitely many summands.** For $g\geq2$, $\pi_1(X)$ is non-abelian and each $\beta$ receives contributions from infinitely many distinct free homotopy classes — [[Def - Character Torus and the Pontryagin Dual|(F3)]]. The sum (74) is genuinely infinite, and there is **no closed form for it directly**. *Consumer:* the reason §6.2 goes through Fourier analysis instead of summing.
>
> **(P4) $\beta=0$ is included and non-trivial.** Commutators $\gamma$ with $[\gamma]=0$ contribute; $\mu^\kappa_X(0)>0$ and is *not* the contractible-class mass, which is excluded from $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ altogether. *Consumer:* [[Thm - Distribution of the Total Homology of the Loop Soup]], where $\mathbb{P}(\beta(\lambda)=0)$ is a meaningful quantity.

> [!warning] Two different exclusions
> $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ already excludes the **contractible** and **peripheral** classes. Within what remains, the class $\beta=0\in H_1$ is a perfectly ordinary homology class containing infinitely many non-contractible loops. Do not conflate "null-homologous" with "contractible".

---

# Type card

> [!abstract] Type card — $\mu^\kappa_X(\beta)$
> **Given.** **(H1)** $X$ geometrically finite hyperbolic; $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$. **(H2)** $\kappa\geq-\tfrac14$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\mathrm{Re}(s)>\delta$.
>
> **Produces.** A summable function $\mu^\kappa_X:H_1(X,\mathbb{Z})\to[0,\infty)$ with $\sum_\beta\mu^\kappa_X(\beta)=-\log Z_X(s)$.
>
> **Lets you.** Ask homological questions — algebraic intersection numbers, winding around fixed cycles — that free homotopy classes cannot express. Its Fourier transform is $-\log L_X(s,\chi)$, which is where every computation actually happens.

---

# Depends on

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — the summands
- [[Def - Character Torus and the Pontryagin Dual]] — the index group and $[\gamma^m]=m[\gamma]$
- [[Thm - Finiteness of the Total Mass]] — (P1)
- 🟢 Hurewicz: $H_1=\pi_1^{\mathrm{ab}}$ — [[Thm - Hurewicz Theorem (Statement)]], [[Def - Hurewicz Map]]
- [[Constr - The Probability Measure on Free Homotopy Classes]] — normalising (74) gives its pushforward under $(\gamma,m)\mapsto m[\gamma]$

---

# Consumed by

- [[Thm - Fourier Expansion and Inversion by Homology Class]] — $\mu^\kappa_X(\beta)$ is exactly the Fourier coefficient
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — via the exponential formula
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2
- [[Def - Selberg L-Function]] — the twisted product whose logarithm generates these masses

---

# Commentary

> [!note]- Commentary (skippable)
> The definition is the obvious one — group the homotopy-class masses by homology — and the interesting point is what it costs and what it buys. It costs the non-abelian information: two loops that traverse the same handles in a different order are separated by $\pi_1$ and identified by $H_1$. It buys *algebraic* intersection numbers, which are defined on homology classes but not on free homotopy classes, and are the paper's stated motivation.
>
> The technical situation is that (74) is an infinite sum with no evaluable closed form. §6.2's response is the right one: don't sum, transform. The generating function $\sum_\beta\mu^\kappa_X(\beta)\chi(\beta)$ *does* have a closed form — $-\log L_X(s,\chi)$ — because the twisting weight $\chi([\gamma])^m$ multiplies the Euler product factor by factor. Fourier inversion then recovers individual $\mu^\kappa_X(\beta)$ as integrals over the character torus. Nothing is ever summed over classes.
>
> Remark 6.2 records the history: Le Jan gave the first definition of Brownian loop measure on homology classes; the authors developed theirs independently under different conventions, and the $L$-function route here recovers Le Jan's results in greater generality, notably in the non-compact case.

---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Selberg L-Function Identity"
  - "Constr - The Mass in a Homology Class"
  - "Ext - Orthogonality of Characters on a Compact Abelian Group"
tags: [paper, zeta-functions, harmonic-analysis]
---

# Signature

| symbol | type |
|---|---|
| $H_1(X,\mathbb{Z})$ | $\cong\mathbb{Z}^r$; $r=2g$ ($X$ closed), $r=2g+b-1$ ($b\geq1$ ends) |
| $\widehat{H_1(X,\mathbb{Z})}$ | $\cong(S^1)^r$ with normalised Haar measure $\mathrm{d}\chi$ |
| $\mu^\kappa_X(\beta)$ | the [[Constr - The Mass in a Homology Class\|homology-class mass]] (74) |
| $s$ | $=\tfrac12+\sqrt{\tfrac14+\kappa}$, $\kappa\geq-\tfrac14$, $\mathrm{Re}(s)>\delta$ |

---

# Type card

> [!abstract] Type card — Theorem 6.5
> **Given.**
> **(H1)** $X=\Gamma\backslash\mathbb{H}^2$ geometrically finite, $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$.
> **(H2)** $\kappa\geq-\tfrac14$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\mathrm{Re}(s)>\delta$.
>
> **Produces.** A Fourier pair on $H_1(X,\mathbb{Z})$:
> $$-\log L_X(s,\chi)=\sum_{\beta\in H_1(X,\mathbb{Z})}\chi(\beta)\,\mu^\kappa_X(\beta)\quad\text{(absolutely convergent)},\tag{77}$$
> $$\mu^\kappa_X(\beta)=\int_{\widehat{H_1(X,\mathbb{Z})}}\big(-\log L_X(s,\chi)\big)\,\overline{\chi(\beta)}\,\mathrm{d}\chi.\tag{78}$$
>
> **Lets you.** Compute the mass in a **single** homology class — an object defined by an infinite, closed-form-free sum — as an integral of an explicit $L$-function over a torus.

---

# Statement

> **Theorem 6.5 (Fourier expansion and inversion by homology class).** Assume (H1),(H2). Then (77) holds for every unitary $\chi$, and (78) holds for every $\beta\in H_1(X,\mathbb{Z})$, where $\mathrm{d}\chi$ is normalised Haar measure on $\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^r$.

> **Remark 6.6 (closed case).** Under $\widehat{H_1(X,\mathbb{Z})}\cong\mathrm{Jac}(X)$, (78) becomes
> $$\mu^\kappa_X(\beta)=\int_{\mathrm{Jac}(X)}\big(-\log L_X(s,\chi_{[\omega]})\big)\,e^{-2\pi i\int_\beta\omega}\,\mathrm{d}[\omega].\tag{79}$$

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - Selberg L-Function Identity\|(76)]] | the double sum over $(\gamma,m)$ | $-\log L_X(s,\chi)=\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ |
| [[Def - Selberg L-Function\|(F5)]] | $\chi([\gamma])^m=\chi(m[\gamma])$ | the weight depends on $(\gamma,m)$ only through $\beta=m[\gamma]$ |
| [[Constr - The Mass in a Homology Class\|(74)]] | grouping by $\beta$ | (77) |
| [[Thm - Finiteness of the Total Mass\|Cor 4.7]] | $\sum_\beta\lvert\mu^\kappa_X(\beta)\rvert=-\log Z_X(s)<\infty$ | absolute convergence, hence $\sum\leftrightarrow\int$ exchange |
| [[Ext - Orthogonality of Characters on a Compact Abelian Group\|(OC)]] | $\int\chi(\beta')\overline{\chi(\beta)}\,\mathrm{d}\chi$ | $\mathbb{1}[\beta'=\beta]$, giving (78) |
| [[Def - The Jacobian as a Principally Polarised Abelian Variety\|(D1),(D2)]] | $X$ closed | (79) |

---

# Proof

**Strategy.** Group (76) by homology class — legitimate because the twist depends only on $m[\gamma]$ — then apply orthogonality.

> [!note]- Proof (skippable)
> Starting from (76) and grouping all terms with the same $\beta=m[\gamma]$,
> $$-\log L_X(s,\chi)=\sum_{\beta\in H_1(X,\mathbb{Z})}\Bigg(\sum_{\substack{\gamma\in\mathcal{P}_X,m\geq1\\ m[\gamma]=\beta}}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)\Bigg)\chi(\beta)=\sum_\beta\mu^\kappa_X(\beta)\chi(\beta),$$
> which is (77). To extract a fixed $\beta$, multiply both sides by $\overline{\chi(\beta)}$ and integrate over the character torus. The Fourier series is absolutely convergent, so sum and integral may be exchanged:
> $$\int_{\widehat{H_1}}\big(-\log L_X(s,\chi)\big)\overline{\chi(\beta)}\,\mathrm{d}\chi=\sum_{\beta'}\mu^\kappa_X(\beta')\int_{\widehat{H_1}}\chi(\beta')\overline{\chi(\beta)}\,\mathrm{d}\chi.$$
> By orthogonality the inner integral is $1$ if $\beta'=\beta$ and $0$ otherwise, so only $\beta'=\beta$ survives, giving (78). $\;\square$

---

# What this assumes, and where to climb

- **Absolute convergence** — from [[Thm - Finiteness of the Total Mass|Cor 4.7]] via $\mathrm{Re}(s)>\delta$. It is the hypothesis of [[Ext - Orthogonality of Characters on a Compact Abelian Group|(OC)(F1)]] and the licence for the $\sum\leftrightarrow\int$ exchange. Not decorative.
- **Unitarity of $\chi$** — [[Def - Selberg L-Function|(F2)]]: keeps the abscissa at $\delta$ and makes $\widehat{H_1}$ compact so $\mathrm{d}\chi$ is a probability measure.
- **$H_1$ torsion-free** — for $\Gamma$ torsion-free Fuchsian, $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$; a torsion summand would add finite factors to the dual but not change the argument.
- **Remark 6.6 only** needs [[Ext - Hodge Theorem and the Period Lattice]], and only for **closed** $X$. Theorem 6.5 itself is stated in the general geometrically finite case.

---

# Consumed by

- [[Thm - Distribution of the Total Homology of the Loop Soup]] — the same inversion, applied to $L_X^{-\lambda}$
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2
- [[Constr - The Mass in a Homology Class]] — this is how $\mu^\kappa_X(\beta)$ is actually computed

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: the twist $\chi([\gamma])^m$ depends on $(\gamma,m)$ only through $m[\gamma]$, so the twisted Selberg product is literally the Fourier transform of the homology-class masses, and Fourier inversion does the rest.**
>
> What makes the theorem worth stating is the asymmetry between the two sides. The left-hand side of (77) is an $L$-function: an explicit Euler product, meromorphically continuable, with the analytic apparatus of §4 behind it. The right-hand side is a sum over homology classes of quantities each of which is itself an infinite sum with no closed form. Fourier inversion converts the tractable object into the intractable one, class by class — which is exactly the service Dirichlet $L$-functions perform for primes in arithmetic progressions.
>
> Remark 6.6 is a change of clothes for the closed case: the character torus becomes the Jacobian, the character becomes the holonomy $e^{2\pi i\int_\beta\omega}$ of a harmonic $1$-form, and the Haar integral becomes an integral over $\mathrm{Jac}(X)$. Nothing is gained analytically; what is gained is the recognition that the natural domain of integration is a familiar object of the surface's own geometry.

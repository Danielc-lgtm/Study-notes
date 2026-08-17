---
type: section
paper: "BH26"
subject: brownian-loops
prereqs:
  - "§4 Zeta Identities and Finiteness of the Total Mass"
  - "§3.3 The Loop Soup and its Poissonian Structure"
tags: [paper, section, probability, zeta-functions]
---

# Signature

| symbol | type |
|---|---|
| $\mathbb{P}_s$ | probability measure on non-trivial non-peripheral free homotopy classes |
| $F$ | $F(s)=-\log Z_X(s)$ — the normalising constant / free energy |
| $L$ | random variable $L(\gamma,m)=m\ell_\gamma$ under $\mathbb{P}_s$ |
| $\ell_{\mathrm{sys}},N_{\mathrm{sys}}$ | systole and its multiplicity, $N_{\mathrm{sys}}\geq2$ |
| $H_1(X,\mathbb{Z})$ | $\cong\mathbb{Z}^r$; $r=2g$ (closed), $r=2g+n_C+n_F-1$ (with $b\geq1$ ends) |
| $\widehat{H_1(X,\mathbb{Z})}$ | $\cong(S^1)^r$, normalised Haar measure $\mathrm{d}\chi$ |
| $\mu^\kappa_X(\beta)$ | the mass in homology class $\beta$ |
| $L_X(\cdot,\chi)$ | Selberg $L$-function; $L_X(\cdot,1)=Z_X$ |
| $\mathcal{L}_\lambda,\mathcal{L}^*_\lambda,\beta(\lambda)$ | loop soup, its non-contractible non-peripheral part, its total homology |

> **Convention.** $\kappa>0$ throughout §6.1, so $s>1\geq\delta$ automatically and no finite/infinite-area dichotomy is needed. §6.2–§6.3 allow $\kappa\geq-\tfrac14$ with $\mathrm{Re}(s)>\delta$.

---

# Exports

> **(E1) The measure.** $\mathbb{P}_s(\mathcal{C}_X(\gamma^m))=\dfrac{\mu^\kappa_X(\mathcal{C}_X(\gamma^m))}{-\log Z_X(s)}$, well defined by [[Thm - Finiteness of the Total Mass|Cor 4.7]] and [[Thm - Selberg Zeta Identity (Killing Case)|Cor 4.3]]. *([[Constr - The Probability Measure on Free Homotopy Classes]].)*
>
> **(E2) Moments.** $\mathbb{E}_s[e^{-rL}]=\dfrac{\log Z_X(s+r)}{\log Z_X(s)}$; $\mathbb{E}_s[L^n]=\dfrac{(-1)^nF^{(n)}(s)}{F(s)}$; $\mathbb{E}_s[L]=-(\log F)'(s)$; $\mathrm{Var}_s(L)=(\log F)''(s)$; $s\mapsto\mathbb{E}_s[L]$ strictly decreasing. *([[Thm - Moments of the Length via the Selberg Zeta Function|§6.1]], eqs. (69)–(73).)*
>
> **(E3) Concentration.** $\mathbb{P}_s\to$ uniform on the $N_{\mathrm{sys}}$ systolic classes as $s\to\infty$; $\mathbb{E}_s[L]\to\ell_{\mathrm{sys}}$; $-\log Z_X(s)\sim\frac{N_{\mathrm{sys}}}{1-e^{-\ell_{\mathrm{sys}}}}e^{-s\ell_{\mathrm{sys}}}$, and both $\ell_{\mathrm{sys}}$ and $N_{\mathrm{sys}}$ are recoverable from that asymptotic. *([[Thm - Concentration on Systolic Classes|§6.1]].)*
>
> **(E4) Homology masses.** $\mu^\kappa_X(\beta):=\sum_{m[\gamma]=\beta}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$; each $\beta$ receives **infinitely many** classes, and $\sum_\beta\mu^\kappa_X(\beta)=-\log Z_X(s)$. *([[Constr - The Mass in a Homology Class|Def 6.1]], eq. (74).)*
>
> **(E5) The $L$-function identity.** $-\log L_X(s,\chi)=\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$. *([[Thm - Selberg L-Function Identity|Cor 6.4]], eq. (76).)*
>
> **(E6) Fourier pair.** $-\log L_X(s,\chi)=\sum_\beta\chi(\beta)\mu^\kappa_X(\beta)$ and $\mu^\kappa_X(\beta)=\int_{\widehat{H_1}}(-\log L_X(s,\chi))\overline{\chi(\beta)}\,\mathrm{d}\chi$. *([[Thm - Fourier Expansion and Inversion by Homology Class|Thm 6.5]], eqs. (77),(78); Remark 6.6 restates (78) over $\mathrm{Jac}(X)$ when $X$ is closed.)*
>
> **(E7) Total homology of the soup.** $\mathbb{E}[\chi(\beta(\lambda))]=\big(Z_X(s)/L_X(s,\chi)\big)^\lambda$ and $\mathbb{P}(\beta(\lambda)=\beta)=Z_X(s)^\lambda\int_{\widehat{H_1}}L_X(s,\chi)^{-\lambda}\overline{\chi(\beta)}\,\mathrm{d}\chi$. *([[Thm - Distribution of the Total Homology of the Loop Soup|Prop 6.7]], eqs. (80),(81).)*

---

# The two partitions

| | free homotopy classes | homology classes |
|---|---|---|
| index set | $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ | $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$ |
| algebra | conjugacy classes in the **non-abelian** $\Gamma$ | the abelianisation $\Gamma^{\mathrm{ab}}$ |
| mass | closed form $\frac1m\frac{e^{(1-s)L}}{e^L-1}$ | infinite sum (74), **no closed form** |
| retains | order of handle traversal, up to conjugation | net winding only |
| supports | geometric intersection numbers | **algebraic** intersection numbers |
| computed via | direct formula | Fourier inversion of $-\log L_X(s,\chi)$ |

---

# Imported results

| import | used for | gap? |
|---|---|---|
| [[Ext - Orthogonality of Characters on a Compact Abelian Group\|(OC)]] | inversions (78),(81) | no — inside *Functional Analysis*/*Advanced Probability* |
| [[Ext - Exponential Formula for Poisson Point Processes\|(EF)]] | (80) | no — inside *Advanced Probability* |
| [[Ext - Hodge Theorem and the Period Lattice\|(HT),(PL),(HS)]] | Remark 6.6 only | **yes**, but decorative |
| [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions\|(MC)]] | naming $L_X$ outside the Euler-product region | **yes**, not load-bearing |

---

# Subpages

- [[Constr - The Probability Measure on Free Homotopy Classes]] — (E1)
- [[Thm - Moments of the Length via the Selberg Zeta Function]] — (E2)
- [[Thm - Concentration on Systolic Classes]] — (E3)
- [[Def - Character Torus and the Pontryagin Dual]] — the dual group and its Haar measure
- [[Ext - Orthogonality of Characters on a Compact Abelian Group]] — the inversion tool
- [[Ext - Hodge Theorem and the Period Lattice]] — Remark 6.6's ingredients
- [[Def - The Jacobian as a Principally Polarised Abelian Variety]] — Remark 6.6
- [[Constr - The Mass in a Homology Class]] — (E4), Definition 6.1
- [[Def - Selberg L-Function]] — Definition 6.3
- [[Thm - Selberg L-Function Identity]] — (E5), Corollary 6.4
- [[Thm - Fourier Expansion and Inversion by Homology Class]] — (E6), Theorem 6.5
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — (E7), Proposition 6.7

---

# Consumed by

- Nothing. §6 is terminal; §7 changes dimension and reruns §3, not §6.

---

# Commentary

> [!note]- Commentary (skippable)
> §6 is where the machinery pays out. §3 gave a number per free homotopy class, §4 summed those numbers and recognised the total as $-\log Z_X(s)$, and §6 divides one by the other. Because both are explicit, so is everything downstream: the moment generating function of the length is a ratio of zeta values, all moments are derivatives of $\log F$, and the zero-temperature limit returns the systole with its multiplicity.
>
> The passage to homology is the section's second half and has a different character. Homotopy classes have closed-form masses but do not support algebraic intersection numbers; homology classes do, but their masses are infinite sums with no closed form. The resolution is Fourier analysis on $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$: the transform of the homology-class masses is $-\log L_X(s,\chi)$, an object with an Euler product, and inversion recovers individual classes as integrals over the character torus. The analogy with Dirichlet $L$-functions and primes in arithmetic progressions is exact in structure; the only difference is that the dual group is a torus rather than finite.
>
> Proposition 6.7 is the natural terminus. It combines the Poissonian structure of §3.3 with the $L$-function identity to give the **full law** of the total homology of the loop soup, in closed form. Three ingredients meet — a character is a homomorphism, the exponential formula linearises products over Poisson points, and the twisted Selberg product evaluates the resulting integral — and each is one line.
>
> Two honest limitations the section states itself. The Jacobian reformulation is available only for closed surfaces; and the stated motivation — computing probabilities of geodesic intersections — is not pursued. The tools are built and left ready.

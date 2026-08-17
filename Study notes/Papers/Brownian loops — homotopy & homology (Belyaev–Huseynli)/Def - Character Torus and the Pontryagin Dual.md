---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Geometrically Finite Surfaces, Cusps and Funnels"
tags: [paper, algebraic-topology, harmonic-analysis]
---

# Signature

| symbol | type |
|---|---|
| $H_1(X,\mathbb{Z})$ | $\cong\mathbb{Z}^r$ — the abelianisation of $\pi_1(X)\cong\Gamma$ |
| $r$ | $=2g$ ($X$ closed); $=2g+b-1=2g+n_C+n_F-1$ ($X$ with $b\geq1$ ends) |
| $\chi$ | a **unitary** character: a homomorphism $H_1(X,\mathbb{Z})\to S^1$ |
| $\widehat{H_1(X,\mathbb{Z})}$ | the **character torus** / Pontryagin dual; $\cong(S^1)^r\cong(\mathbb{R}/\mathbb{Z})^r$ |
| $\mathrm{d}\chi$ | the normalised Haar measure on the torus; total mass $1$ |
| $[\gamma]$ | image of $\gamma\in\Gamma$ under $\Gamma\twoheadrightarrow H_1(X,\mathbb{Z})$; $[\gamma^m]=m[\gamma]$ |

---

# Definition

> **Definition (character torus).** A character of $H_1(X,\mathbb{Z})$ is a homomorphism $\chi:H_1(X,\mathbb{Z})\to\mathbb{C}^\times$; the **unitary** ones, $\chi:H_1(X,\mathbb{Z})\to S^1$, form the Pontryagin dual $\widehat{H_1(X,\mathbb{Z})}$.

> **(D1) Coordinates.** Choose a $\mathbb{Z}$-basis $e_1,\dots,e_r$ of $H_1(X,\mathbb{Z})$. A unitary character is determined by phases $\theta_1,\dots,\theta_r\in\mathbb{R}/\mathbb{Z}$ via $\chi(e_j)=e^{2\pi i\theta_j}$, so
> $$\widehat{H_1(X,\mathbb{Z})}\ \cong\ (S^1)^r\ \cong\ (\mathbb{R}/\mathbb{Z})^r.$$
>
> **(D2) The rank.** $H_1(X,\mathbb{Z})$ is the abelianisation of $\pi_1(X)$ by [[Def - Path-Product and the Fundamental Group|Hurewicz]]. Closed genus $g$: $r=2g$. Geometrically finite with $b=n_C+n_F\geq1$ ends: $r=2g+b-1$.
>
> **(F1) The only property used.** $[\gamma^m]=m[\gamma]$, so for a unitary character
> $$\chi([\gamma])^m=\chi\big(m[\gamma]\big)=\chi\big([\gamma^m]\big),$$
> which depends only on the **homology class** of the iterate, not on the geodesic. This is what licenses regrouping the double sum of (76) by homology class.
>
> **(F2) Compactness and Haar.** $(S^1)^r$ is a compact abelian group, so it carries a unique normalised Haar measure $\mathrm{d}\chi$, and [[Ext - Orthogonality of Characters on a Compact Abelian Group|(OC)]] applies.
>
> **(F3) Homotopy is finer than homology.** $\pi_1(X)\cong\Gamma$ is **non-abelian** for $g\geq2$; the abelianisation forgets the order in which handles are traversed. Each $\beta\in H_1(X,\mathbb{Z})$ receives contributions from **infinitely many** free homotopy classes.

---

# Type card

> [!abstract] Type card — $\widehat{H_1(X,\mathbb{Z})}$
> **Given.** **(H1)** $X$ geometrically finite hyperbolic; $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$ with $r$ as in (D2).
>
> **Produces.** A compact abelian group $\cong(S^1)^r$ with normalised Haar measure, whose elements are the unitary characters.
>
> **Lets you.** Run **Fourier analysis on $H_1(X,\mathbb{Z})$**: the map $\beta\mapsto\mu^\kappa_X(\beta)$ is a function on $\mathbb{Z}^r$, its Fourier transform is $-\log L_X(s,\chi)$, and (OC) inverts. That is the whole of §6.2–§6.3.

---

# Depends on

- [[Def - Geometrically Finite Surfaces, Cusps and Funnels]] — the count $b=n_C+n_F$ of ends
- 🟢 Hurewicz: $H_1=\pi_1^{\mathrm{ab}}$ — see [[Thm - Hurewicz Theorem (Statement)]]
- 🟢 Pontryagin duality for finitely generated abelian groups; Haar measure on a compact group — *Functional Analysis* (8,10)
- [[Ext - Orthogonality of Characters on a Compact Abelian Group]] — (F2)

---

# Checks

**Instance.** $X$ closed of genus $2$: $r=4$, $\widehat{H_1}\cong(S^1)^4$, and by [[Def - The Jacobian as a Principally Polarised Abelian Variety|§6.2]] this torus is $\mathrm{Jac}(X)$.

**Instance.** $X$ a once-punctured torus: $g=1$, $b=1$, so $r=2\cdot1+1-1=2$ and $\widehat{H_1}\cong(S^1)^2$. Note $H_1$ is **free** even though $X$ is non-compact — no torsion, so the dual is a torus with no finite factor.

**Non-instance (fails F1 for non-unitary $\chi$).** $\chi:H_1\to\mathbb{C}^\times$ with $\lvert\chi\rvert\neq1$: then $\lvert\chi([\gamma])^m\rvert$ grows or decays in $m$ and the Euler product (75)'s convergence region moves — the situation of [[Def - Ruelle Zeta Function and its Twist|$c_\rho$]]. §6 uses only unitary characters, so $\lvert z\rvert=e^{-(\mathrm{Re}(s)+k)\ell_\gamma}<1$ holds throughout.

**Non-instance (fails the abelian reduction).** Two free homotopy classes with the same homology, e.g. $aba^{-1}b^{-1}$ vs. the trivial class in homology: they are distinct in $\pi_1$ but both map to $0\in H_1$. **Consequence:** (F3) — $\mu^\kappa_X(\beta)$ is an infinite sum of class masses, and §6.2 has to say so.

---

# Used at

- [[Def - Selberg L-Function]] — $\chi$ is its twisting datum
- [[Thm - Selberg L-Function Identity]] — (F1) is what makes the weight a function of the homology class
- [[Thm - Fourier Expansion and Inversion by Homology Class]] — the Fourier pair
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — $\mathbb{E}[\chi(\beta(\lambda))]$ is a characteristic function on the torus
- [[Def - The Jacobian as a Principally Polarised Abelian Variety]] — the closed-surface identification
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2

---

# Commentary

> [!note]- Commentary (skippable)
> The whole of §6.2–§6.3 is Fourier analysis on $\mathbb{Z}^r$ dressed in geometric language. Functions on $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$ have Fourier transforms on the dual torus $(S^1)^r$; the transform of the homology-class mass is $-\log L_X(s,\chi)$; Fourier inversion recovers the mass as an integral over the torus. Once that is seen, (77),(78) and (80),(81) are all the same two-line manipulation.
>
> The analogy the paper draws is with Dirichlet $L$-functions: primes in arithmetic progressions are isolated by summing over characters of $(\mathbb{Z}/q)^\times$, and closed geodesics in a homology class are isolated by integrating over characters of $H_1(X,\mathbb{Z})$. The only structural difference is that the character group here is a **torus**, not finite, so the isolation is an integral rather than a finite sum.
>
> (F3) is worth taking seriously as a warning. Homotopy classes are a fine partition and homology classes a coarse one; the passage between them loses genuinely non-abelian information — the order in which handles are traversed. The paper's stated motivation for tolerating that loss is that *algebraic* intersection numbers are defined on homology while only *geometric* ones are defined on homotopy.

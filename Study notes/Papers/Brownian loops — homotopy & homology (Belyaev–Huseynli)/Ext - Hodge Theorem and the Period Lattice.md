---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, hodge-theory, riemann-surfaces]
---

# Signature

| symbol | type |
|---|---|
| $X$ | a **closed** oriented surface of genus $g$, with a Riemannian metric |
| $H^1_{\mathrm{dR}}(X,\mathbb{R})$ | de Rham cohomology; $\dim_{\mathbb{R}}=2g$ |
| $\mathcal{H}^1(X)$ | the space of **real harmonic** $1$-forms; $\dim_{\mathbb{R}}=2g$ |
| $\mathcal{H}^1_{\mathbb{Z}}(X)$ | the lattice of harmonic $1$-forms with **integral periods** |
| $\int_\beta\omega$ | the period of $\omega$ around the cycle $\beta\in H_1(X,\mathbb{Z})$ |
| $*$ | the Hodge star; on $1$-forms of a surface, $*^2=-1$ |

---

# Statement

> **(HT) Hodge theorem, degree $1$.** *Precondition:* **(P1)** $X$ closed oriented Riemannian surface. *Conclusion:* every class in $H^1_{\mathrm{dR}}(X,\mathbb{R})$ has a **unique** harmonic representative, so $H^1_{\mathrm{dR}}(X,\mathbb{R})\cong\mathcal{H}^1(X)$.

> **(PL) Period lattice.** Under (HT), $H_1(X,\mathbb{Z})$ — viewed inside $H^1_{\mathrm{dR}}(X,\mathbb{R})$ via de Rham — corresponds to the lattice $\mathcal{H}^1_{\mathbb{Z}}(X)$ of harmonic forms with integral periods.

> **(HS) Complex structure.** On $1$-forms of an oriented surface $*^2=-1$, so $*$ is a complex structure on the real $2g$-dimensional space $\mathcal{H}^1(X)$, making $\mathcal{H}^1(X)/\mathcal{H}^1_{\mathbb{Z}}(X)$ a complex torus of dimension $g$. Together with the intersection pairing this is a **principally polarised abelian variety**.

> **(F1) The holonomy character.** For $\omega\in\mathcal{H}^1(X)$ define
> $$\chi_\omega(\beta):=e^{2\pi i\int_\beta\omega},\qquad\beta\in H_1(X,\mathbb{Z}).$$
> $\chi_\omega$ is a unitary character; $\chi_\omega=\chi_{\omega'}\iff\omega-\omega'\in\mathcal{H}^1_{\mathbb{Z}}(X)$.
>
> **(F2) The chain of isomorphisms.** Consequently
> $$\widehat{H_1(X,\mathbb{Z})}\ \cong\ \frac{H^1_{\mathrm{dR}}(X,\mathbb{R})}{H^1(X,\mathbb{Z})}\ \cong\ \frac{\mathcal{H}^1(X)}{\mathcal{H}^1_{\mathbb{Z}}(X)}\ \cong\ \mathrm{Jac}(X),$$
> as compact real tori of dimension $2g$.
>
> **(F3) The pairing.** Under (F2), $\langle\beta,[\omega]\rangle=\int_\beta\omega\pmod{\mathbb{Z}}$, so the Haar-measure integral over $\widehat{H_1}$ becomes an integral over $\mathrm{Jac}(X)$ against $e^{-2\pi i\langle\beta,[\omega]\rangle}$.

---

# Type card

> [!abstract] Type card — (HT),(PL),(HS)
> **Given.** (P1) — $X$ **closed**.
>
> **Produces.** The identification (F2) of the character torus with the Jacobian, plus the pairing (F3).
>
> **Lets you.** Rewrite the abstract Fourier inversion over $\widehat{H_1(X,\mathbb{Z})}$ as a concrete integral over $\mathrm{Jac}(X)$ — Remark 6.6, eq. (79). **Cosmetic**: no result depends on it.

---

# Status

- **Proved here:** no.
- **Source:** standard Hodge theory; Griffiths–Harris, *Principles of Algebraic Geometry*, Ch. 0 and 2; Farkas–Kra, *Riemann Surfaces*.
- **DAG node that would close this:** 🔵 *Hodge Theory* and 🔵 *Riemann Surfaces* (both non-anchors), though [[Thm - Hodge Decomposition Theorem]] and [[Def - The Hodge Star Operator]] exist in the vault. **A gap, but a decorative one.**
- **What is safe to assume:** (HT),(PL),(HS),(F1)–(F3), for **closed** $X$ only.
- **Scope:** Remark 6.6 — the restatement (79) of the inversion formula. Nothing else. Removing this import removes one remark.

> [!warning] Closed only
> In the geometrically finite non-compact case the identification with the Jacobian is **not available**. Partial analogues exist but require substantially more Hodge-theoretic machinery, and the paper explicitly declines to invoke them. Theorem 6.5 itself is stated for the general geometrically finite case and does not use any of this.

---

# Used at

- [[Def - The Jacobian as a Principally Polarised Abelian Variety]] — this is its content
- [[Thm - Fourier Expansion and Inversion by Homology Class]] — Remark 6.6, the restatement (79)
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2

---

# Commentary

> [!note]- Commentary (skippable)
> This is the one place in the paper where a genuinely different area — complex algebraic geometry — is invoked, and it is invoked for a single reformulation. The chain (F2) is standard: cohomology has harmonic representatives; those with integral periods form a lattice; the Hodge star supplies a complex structure; the quotient is the Jacobian.
>
> The reformulation is worth having because it changes what the inversion formula *looks like*. Abstractly, $\mu^\kappa_X(\beta)$ is a Fourier coefficient of a function on a torus. Concretely, by (F3), it is an integral over $\mathrm{Jac}(X)$ of $-\log L_X(s,\chi_{[\omega]})$ against $e^{-2\pi i\int_\beta\omega}$: the mass of Brownian loops in a homology class is an integral of a twisted Selberg $L$-function over the Jacobian, weighted by the holonomy of harmonic forms around that class. That statement is more evocative than the abstract one and carries exactly the same information.

---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Character Torus and the Pontryagin Dual"
  - "Ext - Hodge Theorem and the Period Lattice"
tags: [paper, hodge-theory, riemann-surfaces]
---

# Signature

| symbol | type |
|---|---|
| $X$ | a **closed** surface of genus $g$; $r=2g$ |
| $\mathcal{H}^1(X)$ | real harmonic $1$-forms, $\dim_{\mathbb{R}}=2g$ |
| $\mathcal{H}^1_{\mathbb{Z}}(X)$ | the sublattice of forms with integral periods |
| $\mathrm{Jac}(X)$ | $:=\mathcal{H}^1(X)/\mathcal{H}^1_{\mathbb{Z}}(X)$ — a complex torus of dimension $g$ |
| $\chi_\omega$ | the character $\beta\mapsto e^{2\pi i\int_\beta\omega}$ |
| $\mathrm{d}[\omega]$ | normalised Haar measure on the real Jacobian torus |

---

# Definition

> **Definition (Jacobian).** $\mathrm{Jac}(X):=\mathcal{H}^1(X)/\mathcal{H}^1_{\mathbb{Z}}(X)$, a compact real torus of dimension $2g$, given a complex structure by the Hodge star ($*^2=-1$ on $1$-forms) and a principal polarisation by the intersection pairing.

> **(D1) Identification with the character torus.** By [[Ext - Hodge Theorem and the Period Lattice|(F2)]],
> $$\widehat{H_1(X,\mathbb{Z})}\ \cong\ \frac{H^1_{\mathrm{dR}}(X,\mathbb{R})}{H^1(X,\mathbb{Z})}\ \cong\ \frac{\mathcal{H}^1(X)}{\mathcal{H}^1_{\mathbb{Z}}(X)}\ \cong\ \mathrm{Jac}(X),$$
> the middle isomorphism by the Hodge theorem, the first by $\omega\mapsto\chi_\omega$.
>
> **(D2) The pairing.** $\langle\beta,[\omega]\rangle=\int_\beta\omega\pmod{\mathbb{Z}}$, so $\chi_\omega(\beta)=e^{2\pi i\langle\beta,[\omega]\rangle}$.
>
> **(D3) What it buys.** The inversion formula (78) may be rewritten as an integral over $\mathrm{Jac}(X)$:
> $$\mu^\kappa_X(\beta)=\int_{\mathrm{Jac}(X)}\big(-\log L_X(s,\chi_{[\omega]})\big)\,e^{-2\pi i\int_\beta\omega}\,\mathrm{d}[\omega].\tag{79}$$

> [!warning] Closed surfaces only
> For a geometrically finite non-compact $X$ the character torus is still $(S^1)^{2g+b-1}$, but **the identification with a Jacobian is not available.** Partial analogues need more Hodge theory than the paper wishes to invoke. All the *theorems* of §6 hold in the general case; only this reformulation is restricted.

---

# Type card

> [!abstract] Type card — $\mathrm{Jac}(X)$
> **Given.** **(H1)** $X$ closed of genus $g$. **(H2)** the Hodge theorem and the period lattice — [[Ext - Hodge Theorem and the Period Lattice|(HT),(PL),(HS)]].
>
> **Produces.** A principally polarised abelian variety of dimension $g$, canonically isomorphic to $\widehat{H_1(X,\mathbb{Z})}$ as a compact real torus with Haar measure.
>
> **Lets you.** Restate (78) as (79). **Nothing else** — no result of §6 depends on this page.

---

# Depends on

- [[Ext - Hodge Theorem and the Period Lattice]] — the whole content
- [[Def - Character Torus and the Pontryagin Dual]] — the object being identified
- [[Thm - Hodge Decomposition Theorem]], [[Def - The Hodge Star Operator]], [[Def - de Rham Cohomology]] — vault pages for the ingredients
- 🔵 *Riemann Surfaces*, 🔵 *Hodge Theory* — non-anchors

---

# Checks

**Instance.** $g=1$, $X$ a torus: $\mathcal{H}^1(X)$ is spanned by $\mathrm{d}x,\mathrm{d}y$, $\mathcal{H}^1_{\mathbb{Z}}$ is the integer span, and $\mathrm{Jac}(X)\cong X$ itself — the classical statement that an elliptic curve is its own Jacobian. (The paper's surfaces have $g\geq2$; this is a sanity check, not an application.)

**Non-instance (fails H1).** $X$ once-punctured of genus $g$: $r=2g$ still, but $X$ is non-compact, harmonic forms need decay conditions at the cusp, and (D1) fails. **Consequence:** Remark 6.6 is stated only in the closed case, while Theorem 6.5 is not.

**Non-instance (fails to be a *polarised* torus without the pairing).** $\mathcal{H}^1(X)/\mathcal{H}^1_{\mathbb{Z}}(X)$ with $*$ but without the intersection form is a complex torus, not an abelian variety: not every complex torus of dimension $\geq2$ is projective. The intersection pairing is what supplies the polarisation.

---

# Used at

- [[Thm - Fourier Expansion and Inversion by Homology Class]] — Remark 6.6, the restatement (79)
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2

---

# Commentary

> [!note]- Commentary (skippable)
> The page exists to record a translation, and its honest status is: pleasant, not load-bearing. The mass of Brownian loops in a fixed homology class equals an integral, over the Jacobian of the surface, of a twisted Selberg $L$-function weighted by the holonomy $e^{-2\pi i\int_\beta\omega}$ of the corresponding harmonic form. Three subjects meet in one formula — probability supplies the mass, spectral theory the $L$-function, Hodge theory the domain of integration — and none of them is doing anything difficult at the meeting point.
>
> The restriction to closed surfaces is worth respecting rather than patching. §6's theorems are proved for geometrically finite $X$ with $r=2g+b-1$, and the character torus $(S^1)^r$ is all that is ever needed. It is only the *name* Jacobian, and the complex structure that comes with it, that requires compactness.

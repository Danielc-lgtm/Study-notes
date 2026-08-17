---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Character Torus and the Pontryagin Dual"
  - "Thm - Hodge Decomposition Theorem"
  - "Def - de Rham Cohomology"
tags: [paper, geometry, hodge-theory, complex-geometry]
---

# Notation

- $X$ — a **closed** surface of genus $g$; $H^1_{\mathrm{dR}}(X,\mathbb{R})$ its first de Rham cohomology
- $\mathcal{H}^1(X)$ — the space of real harmonic $1$-forms; $\mathcal{H}^1_{\mathbb{Z}}(X)$ the lattice of those with integral periods
- $H^1(X,\mathbb{Z})$ — integral cohomology, viewed inside $H^1_{\mathrm{dR}}(X,\mathbb{R})$ via de Rham
- $\omega$ — a harmonic $1$-form; $\int_\beta\omega$ its period around a cycle $\beta$
- $\chi_\omega$ — the unitary character attached to $\omega$; $*$ the [[Def - The Hodge Star Operator|Hodge star]]
- $\mathrm{Jac}(X)$ — the Jacobian; $\mathrm{d}[\omega]$ the normalised Haar measure on the underlying real torus

---

# In plain language

For a **closed** surface the character torus of §6.2 is not merely a torus — it is the Jacobian variety, and the identification comes from Hodge theory.

The chain is short. By the [[Thm - Hodge Decomposition Theorem|Hodge theorem]], every de Rham cohomology class has a **unique harmonic representative**, so $H^1_{\mathrm{dR}}(X,\mathbb{R})\cong\mathcal{H}^1(X)$. Under that identification the integral lattice $H^1(X,\mathbb{Z})$ corresponds to $\mathcal{H}^1_{\mathbb{Z}}(X)$, the harmonic $1$-forms with integral periods. Now attach to a harmonic $1$-form $\omega$ the **unitary holonomy**
$$\chi_\omega(\beta) = e^{2\pi i\int_\beta\omega},$$
where $\int_\beta\omega$ is the period of $\omega$ around the cycle $\beta$. Two forms give the same character exactly when their difference has integral periods — because then the exponential is $1$ on every cycle. So the map $\omega\mapsto\chi_\omega$ descends to an isomorphism of compact real tori
$$\widehat{H_1(X,\mathbb{Z})}\;\cong\;\frac{H^1_{\mathrm{dR}}(X,\mathbb{R})}{H^1(X,\mathbb{Z})}\;\cong\;\frac{\mathcal{H}^1(X)}{\mathcal{H}^1_{\mathbb{Z}}(X)}\;\cong\;\mathrm{Jac}(X).$$

The extra structure comes from the **Hodge star**. On $1$-forms of a surface, $*^2=-1$, so $*$ is a complex structure on the real $2g$-dimensional space $\mathcal{H}^1(X)$ — multiplication by $i$. That makes the real $2g$-torus a **complex torus of dimension $g$**. Together with the intersection pairing, which supplies the polarisation, this gives $\mathrm{Jac}(X)$ its structure as a **principally polarised abelian variety**.

**What the paper does with it.** Nothing computational: the identification is used to restate the Fourier inversion formula of [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]] as an integral over $\mathrm{Jac}(X)$ rather than over an abstract torus, which is Remark 6.6. The value is interpretive — it says which object the analytic torus of §6.2 actually is. **In the non-compact case the identification is unavailable**, and the paper declines to pursue partial analogues, saying they would require much more Hodge-theoretic machinery than it wishes to invoke.

---

# The definition

> **The Hodge identification (closed surfaces).** For a closed surface of genus $g$ the rank of $H_1(X,\mathbb{Z})$ is $r=2g$, and the character torus has a remarkable relation to harmonic $1$-forms. By the Hodge theorem, every class in $H^1_{\mathrm{dR}}(X,\mathbb{R})$ has a unique harmonic representative, so $H^1_{\mathrm{dR}}(X,\mathbb{R})\cong\mathcal{H}^1(X)$, where $\mathcal{H}^1(X)$ denotes the space of real harmonic $1$-forms. Under this identification $H^1(X,\mathbb{Z})$ corresponds to the lattice $\mathcal{H}^1_{\mathbb{Z}}(X)$ of harmonic $1$-forms with integral periods.

> **The character attached to a harmonic form.** To a harmonic $1$-form $\omega$ one associates the unitary character
> $$\chi_\omega(\beta) = e^{2\pi i\int_\beta\omega},$$
> where $\int_\beta\omega$ is the period of $\omega$ around the cycle $\beta$ and the whole exponential is the unitary holonomy. Two harmonic $1$-forms determine the same character exactly when their difference has integral periods. It follows that there are natural isomorphisms of compact real tori
> $$\widehat{H_1(X,\mathbb{Z})}\;\cong\;\frac{H^1_{\mathrm{dR}}(X,\mathbb{R})}{H^1(X,\mathbb{Z})}\;\cong\;\frac{\mathcal{H}^1(X)}{\mathcal{H}^1_{\mathbb{Z}}(X)}\;\cong\;\mathrm{Jac}(X),$$
> where $H^1(X,\mathbb{Z})$ is viewed inside $H^1_{\mathrm{dR}}(X,\mathbb{R})$ via the de Rham isomorphism.

> **The complex and symplectic structure.** The Hodge star satisfies $*^2=-1$ on $1$-forms and therefore endows the real torus of dimension $2g$ with the structure of a **complex torus of dimension $g$**. Together with the intersection pairing, this gives the Jacobian its structure as a **principally polarised abelian variety**.

> **The pairing.** When $X$ is closed, under $\widehat{H_1(X,\mathbb{Z})}\cong\mathrm{Jac}(X)$ the natural pairing is $\langle\beta,[\omega]\rangle=\int_\beta\omega\pmod{\mathbb{Z}}$.

---

# Types and signatures

- $\mathcal{H}^1(X)$ — a real vector space of dimension $2g$; $\mathcal{H}^1_{\mathbb{Z}}(X)\subset\mathcal{H}^1(X)$ a full lattice of rank $2g$
- $\omega\mapsto\chi_\omega$ — a surjective homomorphism $\mathcal{H}^1(X)\to\widehat{H_1(X,\mathbb{Z})}$ with kernel $\mathcal{H}^1_{\mathbb{Z}}(X)$
- $* : \mathcal{H}^1(X)\to\mathcal{H}^1(X)$ — the [[Def - The Hodge Star Operator|Hodge star]], with $*^2=-\mathrm{id}$; a complex structure
- $\mathrm{Jac}(X)$ — a compact complex torus of complex dimension $g$; with the intersection pairing, a principally polarised abelian variety
- $\mathrm{d}[\omega]$ — the normalised Haar measure on the underlying real Jacobian torus, total mass $1$

---

# Example

Genus $1$, the torus $X=\mathbb{C}/\Lambda$. Then $g=1$, $\mathcal{H}^1(X)$ is spanned by $\mathrm{d}x$ and $\mathrm{d}y$ (both harmonic for the flat metric), the integral lattice is $\mathbb{Z}\mathrm{d}x\oplus\mathbb{Z}\mathrm{d}y$ in suitable coordinates, and $\mathrm{Jac}(X)\cong X$ itself — a complex torus of dimension $1$. The Hodge star sends $\mathrm{d}x\mapsto\mathrm{d}y$ and $\mathrm{d}y\mapsto-\mathrm{d}x$, so $*^2=-1$ visibly, and the complex structure it defines is the original one. The vault has the harmonic forms computed at [[Ex - Harmonic 1-Forms on the Torus]].

**Near-miss non-example — a non-compact surface.** For a geometrically finite non-compact surface the identification with a Jacobian is **not available**. Hodge theory on a non-compact manifold is more delicate: harmonic representatives need not exist or be unique without decay conditions, $L^2$ cohomology differs from de Rham cohomology, and the intersection pairing degenerates on the classes supported near the ends. The paper is explicit that partial analogues exist but "require much more Hodge-theoretic machinery than we would like to invoke". **So [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]] holds in full generality, but Remark 6.6's restatement over the Jacobian is closed-surface only.**

**Second near-miss — the character torus without the complex structure.** $\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^{2g}$ is a real torus for *any* surface with $r=2g$, and that is all §6.2 needs to do Fourier analysis. The Jacobian is that torus plus a complex structure plus a polarisation; **the extra structure is not used in any proof**, and stripping it away costs nothing computationally. It is included because it identifies the object.

---

# Used in this paper at

- [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]], Remark 6.6 — the inversion formula restated as an integral over $\mathrm{Jac}(X)$ against $e^{-2\pi i\int_\beta\omega}$
- [[Def - Character Torus and the Pontryagin Dual]] — the abstract torus that this page identifies in the closed case
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2

Nothing computational depends on it. Every proof in §6.2 runs on the abstract character torus and orthogonality of characters.

---

# Where this sits in my DAG

Three rungs, all 🔵 but all present in the vault. Hodge theory: [[Thm - Hodge Decomposition Theorem]] for the unique harmonic representative, [[Def - The Hodge Star Operator]] for $*$ and the identity $*^2=-1$ on $1$-forms of a surface (the vault has [[Def - Hodge Laplacian]] and the Geometry-of-Physics *Hodge Theory I* pages). De Rham theory: [[Def - de Rham Cohomology]] and the de Rham isomorphism placing $H^1(X,\mathbb{Z})$ inside $H^1_{\mathrm{dR}}(X,\mathbb{R})$. And [[Def - Character Torus and the Pontryagin Dual]] for the dual side.

Quoted rather than derived: that the intersection pairing supplies a **principal** polarisation, making $\mathrm{Jac}(X)$ an abelian variety rather than merely a complex torus. This is classical Riemann-surface theory — the Riemann bilinear relations — and its home node is *Riemann Surfaces* (🔵) or *Complex Geometry* (🔵). Nothing in the paper uses it.

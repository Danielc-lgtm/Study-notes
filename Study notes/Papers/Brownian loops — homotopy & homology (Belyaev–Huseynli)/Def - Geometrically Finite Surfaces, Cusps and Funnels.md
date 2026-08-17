---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
  - "Def - Euler Characteristic"
tags: [paper, hyperbolic-geometry]
---

# Notation

- $X=\Gamma\backslash\mathbb{H}^2$ — a hyperbolic surface with $\Gamma$ torsion-free Fuchsian
- $g$ — the genus; $b$ — the number of ends; $n_C$ — the number of cusps; $n_F$ — the number of funnels, so $b=n_C+n_F$
- $\chi=\chi(X)$ — the Euler characteristic
- $\delta$ — the critical exponent of $\Gamma$
- **peripheral** — a free homotopy class whose loops are freely homotopic into a cusp or onto a boundary component

---

# In plain language

Geometric finiteness is the condition that $X$ is built from a compact core plus finitely many standard ends. It is what makes $\mathcal{P}_X$ countable with a sensible counting function, what makes $H_1(X,\mathbb{Z})$ finitely generated, and what keeps every sum in the paper indexed by something one can enumerate.

There are exactly two kinds of end on a hyperbolic surface, and telling them apart is the single most useful piece of bookkeeping in §4–§6.

A **cusp** is an end of finite area, asymptotically a shrinking horocyclic tube; the surface pinches off. A **funnel** is an end of infinite area, asymptotically a flaring half-cylinder about a closed geodesic. The consequences run all the way through the paper:

- $\mathrm{Area}(X)<\infty$ if and only if there are no funnels, if and only if $\delta=1$. With a funnel, $\mathrm{Area}(X)=\infty$ and $\delta<1$.
- By [[Thm - Finiteness of the Total Mass|Corollary 4.7]] the Brownian total mass is finite exactly when $s>\delta$, so **an infinite-area surface needs no regularisation at all, and a finite-area one needs a killing rate or the machinery of §5**.
- The continuous spectrum of $\Delta_X$ in the finite-area case has multiplicity $n_C$, one [[Def - Eisenstein Series and the Continuous Spectrum|Eisenstein series]] per cusp; this is what breaks trace-class-ness in §5.2.
- $H_1(X,\mathbb{Z})\cong\mathbb{Z}^{2g+b-1}=\mathbb{Z}^{2g+n_C+n_F-1}$ when $X$ has at least one end, and $\mathbb{Z}^{2g}$ when $X$ is closed. The rank is the dimension of the character torus of §6.2.

The word **peripheral** exists to exclude the classes that live in the ends. A loop that can be pushed out into a cusp, or onto a boundary component, has no closed geodesic representative — its length infimum is not attained — so the entire mass-formula apparatus of §3, which is indexed by closed geodesics, has nothing to say about it. Excluding those classes, together with the trivial one, is what makes "the total mass" of §4 a well-defined finite object.

---

# The definition

> **Definition (geometrically finite).** A torsion-free Fuchsian group $\Gamma$ is **geometrically finite** if it admits a fundamental region in $\mathbb{H}^2$ that is a finite-sided convex polygon. The quotient $X=\Gamma\backslash\mathbb{H}^2$ is then a **geometrically finite hyperbolic surface**: a compact core with finitely many ends, each end either a cusp or a funnel.

> **Definition (cusp and funnel).** A **cusp** is an end isometric to a quotient $\{z\in\mathbb{H}^2 : \operatorname{Im}(z)>c\}/\langle z\mapsto z+1\rangle$ — the quotient by a **parabolic** element — and has finite area. A **funnel** is an end isometric to a half of the hyperbolic cylinder $\langle z\mapsto e^{\ell}z\rangle\backslash\mathbb{H}^2$ lying on one side of the core geodesic — the quotient by a **hyperbolic** element — and has infinite area.

> **Definition (non-trivial, non-peripheral).** A free homotopy class of oriented closed curves on $X$ is **non-trivial** if its loops are not null-homotopic, and **non-peripheral** if its loops are neither freely homotopic into a cusp nor freely homotopic to a boundary component. **From §3 onwards, unless otherwise stated, all free homotopy classes are assumed non-trivial and non-peripheral.** Each such class contains a unique closed geodesic representative.

---

# Types and signatures

- $g\in\mathbb{Z}_{\geq0}$, $n_C,n_F\in\mathbb{Z}_{\geq0}$, $b=n_C+n_F$ — non-negative integers
- $\chi(X)=2-2g-b$ — an integer; for a closed surface $\chi=2-2g$, and Gauss–Bonnet gives $\mathrm{Area}(X)=-2\pi\chi(X)=4\pi(g-1)$
- $\mathrm{Area}(X)\in(0,\infty]$ — finite exactly when $n_F=0$
- $\delta\in(0,1]$ — the critical exponent; $\delta=1$ exactly when $\mathrm{Area}(X)<\infty$
- $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$ with $r=2g$ (closed) or $r=2g+b-1$ (with ends)

---

# Example

A closed surface of genus $g\geq2$: no ends, $b=n_C=n_F=0$, $\chi=2-2g<0$, $\mathrm{Area}(X)=4\pi(g-1)$ by Gauss–Bonnet, $\delta=1$, $H_1(X,\mathbb{Z})\cong\mathbb{Z}^{2g}$, and $\widehat{H_1(X,\mathbb{Z})}\cong\mathrm{Jac}(X)$. This is the setting of §5.1 and of the Jacobian discussion in §6.2, and it is the case in which the Brownian total mass diverges and needs the renormalisation of Theorem 5.1.

A once-punctured torus: $g=1$, $n_C=1$, $n_F=0$, so $b=1$, $\chi=-1$, $\mathrm{Area}(X)=2\pi$, still $\delta=1$; $H_1(X,\mathbb{Z})\cong\mathbb{Z}^{2}$. This is the setting of §5.2: finite area, one cusp, continuous spectrum of multiplicity $1$ filling $[\tfrac14,\infty)$, so $e^{-t\Delta_X}$ is not trace class and $\det_0$ is needed.

A three-funnelled sphere (a hyperbolic pair of pants with geodesic boundary, flared): $g=0$, $n_C=0$, $n_F=3$, $\chi=-1$, infinite area, $\delta<1$. Here [[Thm - Finiteness of the Total Mass|Corollary 4.7]] gives finite Brownian total mass with $\kappa=0$ outright, and §6's probability measure exists with no renormalisation at all.

**Near-miss non-example.** A loop running once around a cusp is a perfectly good non-trivial free homotopy class — its element of $\Gamma$ is a non-identity parabolic, not the identity — but it is **peripheral**, and it has no closed geodesic representative: the loops in the class can be pushed further and further into the cusp, shrinking their length towards $0$ without attaining it. Its element of $\Gamma$ is parabolic rather than hyperbolic, so it has no translation length $\ell_\gamma$ and no axis, and every formula in §3 fails to parse for it. This is precisely why "non-peripheral" is in the standing hypothesis rather than being a technical afterthought.

---

# Used in this paper at

- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — where "non-trivial and non-peripheral" is imposed as the standing convention
- [[Def - Critical Exponent and the Prime Geodesic Theorem]] — the dichotomy $\delta=1$ / $\delta<1$ is the area dichotomy
- [[Thm - Finiteness of the Total Mass|Corollary 4.7]] — the practical consequence: which surfaces need regularising
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] and [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]] — $n_C$ appears explicitly in both formulas
- [[Def - Eisenstein Series and the Continuous Spectrum]] — one Eisenstein series per cusp
- [[Constr - The Mass in a Homology Class]] and [[Def - Character Torus and the Pontryagin Dual]] — the rank $r=2g+n_C+n_F-1$ is the torus dimension
- [[Thm - Distribution of the Total Homology of the Loop Soup|Proposition 6.7]] — $\mathcal{L}^*_\lambda$ is defined by excluding contractible and cusp-homotopic loops

---

# Where this sits in my DAG

The hyperbolic geometry is an anchor via the Riemannian-geometry strand, together with [[Def - Fuchsian Group and the Quotient Surface]] one rung up. The Euler characteristic and the genus classification of surfaces are *Algebraic Topology* (🔵) material covered in the vault at [[Def - Euler Characteristic]] and [[Thm - Gauss-Bonnet Theorem for Surfaces]]; the identity $\mathrm{Area}(X)=-2\pi\chi(X)$ is Gauss–Bonnet for a hyperbolic metric.

The classification of ends into cusps and funnels, and the equivalence "finite area $\Leftrightarrow$ $\delta=1$", are quoted from the standard references (Borthwick, *Spectral theory of infinite-area hyperbolic surfaces*; Buser). Nothing downstream depends on their proofs.

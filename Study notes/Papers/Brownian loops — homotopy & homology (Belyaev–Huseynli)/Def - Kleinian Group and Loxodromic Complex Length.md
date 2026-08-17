---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
  - "Def - Primitive Hyperbolic Element and Translation Length"
tags: [paper, hyperbolic-geometry, group-theory]
---

# Notation

- $\mathbb{H}^3=\{(z,y) : z\in\mathbb{C},\ y>0\}$ — hyperbolic $3$-space in the upper half-space model
- $\mathrm{PSL}(2,\mathbb{C})$ — its orientation-preserving isometry group
- $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ — a Kleinian group; torsion-free throughout; $X=\Gamma\backslash\mathbb{H}^3$
- $L_\gamma=\ell_\gamma+i\theta_\gamma$ — the complex length; $\ell_\gamma>0$ the translation length, $\theta_\gamma\in\mathbb{R}/2\pi\mathbb{Z}$ the holonomy angle
- $\tau$ — a loxodromic element; $\mathcal{P}_X$ the primitive oriented closed geodesics on $X$
- $L=mL_\gamma=m\ell_\gamma+im\theta_\gamma$ — the complex length of the $m$-fold iterate

---

# In plain language

Everything in §3's group theory transfers to three dimensions with one change: **the isometries can rotate as well as translate.**

In $\mathrm{PSL}(2,\mathbb{R})$ a non-parabolic non-elliptic element is *hyperbolic*: it translates along an axis, full stop, and its invariant is the translation length $\ell_\gamma$. In $\mathrm{PSL}(2,\mathbb{C})$ the corresponding elements are **loxodromic**: they translate along a geodesic axis *and may also rotate about it*. Two real parameters, and the natural way to package them is as one complex number, the **complex length**
$$L_\gamma = \ell_\gamma + i\theta_\gamma,$$
with $\ell_\gamma>0$ the translation length and $\theta_\gamma\in\mathbb{R}/2\pi\mathbb{Z}$ the holonomy angle. When $\theta_\gamma=0$ the element is a pure translation and the two-dimensional picture is recovered.

The rest of the dictionary is unchanged. A **Kleinian group** is a discrete subgroup of $\mathrm{PSL}(2,\mathbb{C})$; if torsion-free it acts freely and properly discontinuously, and the quotient $X=\Gamma\backslash\mathbb{H}^3$ is a complete orientable hyperbolic $3$-manifold with $\mathbb{H}^3$ as universal cover and $\Gamma$ as deck group. For a geometrically finite such manifold, free homotopy classes of oriented closed curves correspond to conjugacy classes in $\Gamma$; the non-trivial non-peripheral classes correspond to **loxodromic** conjugacy classes, and each contains a unique oriented closed geodesic representative.

**Where the extra parameter shows up.** In [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]] the mass is $\frac1m|e^{mL_\gamma}-1|^{-2}$ — the holonomy enters through a modulus. Note carefully that **the exponent $2$ is a dimensional effect, not a holonomy effect**: setting $\theta_\gamma=0$ gives $(e^{m\ell_\gamma}-1)^{-2}$, still squared, where the two-dimensional answer was $(e^{m\ell_\gamma}-1)^{-1}$. Confusing "three dimensions squares the denominator" with "holonomy squares the denominator" is the easiest mistake to make here.

---

# The definition

> **Definition (Kleinian group and the quotient manifold).** A **Kleinian group** is a discrete subgroup $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$, the orientation-preserving isometry group of hyperbolic $3$-space $\mathbb{H}^3$. When $\Gamma$ is **torsion-free** it acts freely and properly discontinuously, and $X=\Gamma\backslash\mathbb{H}^3$ is a complete orientable hyperbolic $3$-manifold.

> **Definition (loxodromic element and complex length).** Non-parabolic, non-elliptic elements of $\Gamma$ are **loxodromic**: they translate along a geodesic axis and may also rotate about that axis. An oriented closed geodesic $\gamma$ therefore carries a **complex length**
> $$L_\gamma = \ell_\gamma + i\theta_\gamma,\qquad\theta_\gamma\in\mathbb{R}/2\pi\mathbb{Z},$$
> where $\ell_\gamma$ is its translation length and $\theta_\gamma$ is its holonomy angle.

> **The correspondence.** For a geometrically finite hyperbolic $3$-manifold, free homotopy classes of oriented closed curves correspond to conjugacy classes in $\Gamma$. The non-trivial, non-peripheral classes correspond to **loxodromic** conjugacy classes, and each such class contains a unique oriented closed geodesic representative. $\mathcal{P}_X$ denotes the set of primitive oriented closed geodesics on $X$; each $\gamma\in\mathcal{P}_X$ corresponds to a primitive loxodromic conjugacy class in $\Gamma$ with complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$.

---

# Types and signatures

- $\Gamma$ — a countable discrete subgroup of $\mathrm{PSL}(2,\mathbb{C})$, acting on $\mathbb{H}^3$ by isometries, freely and properly discontinuously
- $L_\gamma\in\mathbb{C}$ with $\operatorname{Re}(L_\gamma)=\ell_\gamma>0$ and $\operatorname{Im}(L_\gamma)=\theta_\gamma\in\mathbb{R}/2\pi\mathbb{Z}$ — so $L_\gamma$ lives in a **cylinder**, not the plane; only $e^{L_\gamma}$ is unambiguous
- $L=mL_\gamma$ for $m\geq1$ — the complex length of the iterate; $\operatorname{Im}$ taken mod $2\pi$
- $|e^{L}-1|^2 = 2e^{\operatorname{Re}L}\big(\cosh(\operatorname{Re}L)-\cos(\operatorname{Im}L)\big)$ — the identity used throughout §7
- $\mathcal{P}_X$ — countable; the counting function is finite for every bound on $\ell_\gamma$

**Warning on notation.** In §3 the symbol $L$ denoted the *real* number $m\ell_\gamma$; in §7 it is the *complex* number $mL_\gamma$. Formulas transferred between sections without checking this will be wrong.

---

# Example

The standard-form loxodromic $\tau : (z,y)\mapsto(e^{L_\gamma}z,\ e^{\ell_\gamma}y)$, which is what [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]] normalises every element to. Its axis is the vertical geodesic from $0$ to $\infty$; it translates along that axis by $\ell_\gamma$ and rotates the horizontal $\mathbb{C}$-coordinate by $\theta_\gamma$. Note that the **height** $y$ is scaled by the real factor $e^{\ell_\gamma}$ only — the rotation acts within each horizontal slab and does not affect which slab a point lies in. That observation is what makes the fundamental slab work.

**Near-miss non-example — a pure translation.** $\theta_\gamma=0$ gives $\tau : (z,y)\mapsto(e^{\ell_\gamma}z,e^{\ell_\gamma}y)$, a pure hyperbolic translation, the direct analogue of §3's $z\mapsto e^{\ell_\gamma}z$. **But the resulting mass is $\frac1m(e^{m\ell_\gamma}-1)^{-2}$, not the two-dimensional $\frac1m(e^{m\ell_\gamma}-1)^{-1}$.** So "no holonomy" does not mean "the 2D answer": dimension itself changes the exponent. This is the near-miss most worth internalising.

**Second near-miss — a parabolic.** As in two dimensions, a parabolic element has no axis, no translation length and no closed geodesic; its classes are peripheral and are excluded by the standing convention. See [[Def - Geometrically Finite Surfaces, Cusps and Funnels]] for the two-dimensional version of the same exclusion.

**Third near-miss — an elliptic element.** In $\mathrm{PSL}(2,\mathbb{C})$ an elliptic element is a pure rotation about an axis, with $\ell_\gamma=0$. Torsion-freeness excludes these, exactly as in two dimensions, and for the same reason: they have fixed points, so the action would not be free and the quotient would be an orbifold. Note that a loxodromic element with $\theta_\gamma\neq0$ is *not* elliptic — it has $\ell_\gamma>0$ and no fixed point in $\mathbb{H}^3$.

---

# Used in this paper at

- [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]] — the normalisation $\tau:(z,y)\mapsto(e^{L_\gamma}z,e^{\ell_\gamma}y)$ and the slab $F_\tau$
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Theorem 7.1]] — the setting, and the source of the conjugacy-class correspondence
- [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]] — $\theta_\gamma$ enters the distance computation, hence the geometric prefactor
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] and [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]] — where $|e^{mL_\gamma}-1|^2$ appears
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]]

---

# Where this sits in my DAG

Directly parallel to [[Def - Fuchsian Group and the Quotient Surface]] and [[Def - Primitive Hyperbolic Element and Translation Length]], with $\mathrm{PSL}(2,\mathbb{C})$ in place of $\mathrm{PSL}(2,\mathbb{R})$ and one extra real parameter. The reductions are the same: group actions ([[Def - Group Action]]), covering spaces ([[Def - Covering Space]]), and conjugacy ([[Def - Conjugacy Class]]).

Anchors below: hyperbolic $3$-space and its isometry group, and the classification of elements of $\mathrm{PSL}(2,\mathbb{C})$ into elliptic, parabolic and loxodromic by trace — via the Riemannian-geometry strand and [[Def - The Hyperbolic Space H^n]], which covers $\mathbb{H}^n$ for all $n$.

Quoted, as in the two-dimensional case: that free homotopy classes correspond to conjugacy classes and that each non-trivial non-peripheral class contains a unique closed geodesic. The references the paper gives for hyperbolic manifolds are Ratcliffe and Borthwick.

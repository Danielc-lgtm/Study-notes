---
type: definition
subject: geometry
prereqs:
  - "Def - Hyperbolic Plane"
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
tags: [geometry, hyperbolic-geometry, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$\mathbb{H}^3=\{(z,y):z\in\mathbb{C},\,y>0\}$ hyperbolic 3-space (upper half-space model). $\mathrm{PSL}(2,\mathbb{C})$ the group of $2\times2$ complex matrices of determinant $1$ mod $\pm I$, acting on $\mathbb{H}^3$ by isometries. $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ a Kleinian group; $X=\Gamma\backslash\mathbb{H}^3$. $d(\cdot,\cdot)$ hyperbolic distance.

---

# Axiom Motivation

§7 repeats the entire programme one dimension up: on a hyperbolic 3-manifold instead of a surface. The construction of §2–§3 barely used that $X$ was two-dimensional — it used the heat kernel, bridge measures, the weights $dt/t$ and $\operatorname{vol}_g$, and the descent-and-unfold over a cyclic centraliser — all of which exist verbatim in any dimension. What *did* tie the paper to surfaces was conformal invariance (used for Polyakov and the length-spectrum identity); once one works with a killing rate or any non-linear subordination, conformal invariance is irrelevant and nothing obstructs going to 3D. So §7 sets $X=\Gamma\backslash\mathbb{H}^3$ for a **Kleinian group** $\Gamma$ (the 3D analogue of a Fuchsian group) and re-derives the mass formulas.

The one genuinely new feature is that a closed geodesic on a 3-manifold carries a **complex length**. In 2D a hyperbolic isometry only translates along its axis; in 3D a **loxodromic** isometry both translates (by $\ell_\gamma$) *and rotates* about the axis (by a holonomy angle $\theta_\gamma$). Packaging these as a single complex number $L_\gamma=\ell_\gamma+i\theta_\gamma$ makes every §3 formula carry over with $\ell_\gamma$ replaced by the complex length — the reason the 3-manifold mass formulas look identical to the surface ones but with $|e^{mL_\gamma/2}-e^{-mL_\gamma/2}|^2$ in place of $\sinh^2$.

---

# Recalls for the definition

> [!recall]- "Freely and properly discontinuously" (what it means for $\Gamma$ to act nicely on $\mathbb{H}^3$)
> **Formally:** an action $\Gamma\times\mathbb{H}^3\to\mathbb{H}^3$ is **free** if no non-identity $h\in\Gamma$ fixes any point ($h\cdot p=p$ forces $h=\mathrm{id}$), and **properly discontinuous** if every point has a neighbourhood $U$ with $\{h\in\Gamma:h\cdot U\cap U\ne\varnothing\}$ finite (so orbits do not accumulate). Together they mean the quotient $\Gamma\backslash\mathbb{H}^3$ inherits a smooth manifold structure with no orbifold points.
> **In words:** "free" means no wallpaper symmetry pins any point in place; "properly discontinuous" means when you take a small patch, only finitely many wallpaper symmetries can move it back onto itself.
> **Concretely:** the standard integer-lattice action of $\mathbb{Z}^3$ on $\mathbb{R}^3$ by translation is both free (no non-identity vector fixes any point) and properly discontinuous (a ball of radius $0.4$ only intersects finitely many translates); the quotient is the $3$-torus. Rotation by $\pi/3$ around the origin in $\mathbb{R}^2$ is **not** free (fixes the origin); the corresponding quotient is a cone-point orbifold, not a smooth manifold.

> [!recall]- Parabolic, elliptic, loxodromic elements of $\mathrm{PSL}(2,\mathbb{C})$
> **Formally:** for $\tau\in\mathrm{PSL}(2,\mathbb{C})$, classify by the (complex) trace-squared $|\mathrm{tr}\,\tau|^2$: **elliptic** ($0\le|\mathrm{tr}|^2<4$ and real; finite-order rotation, fixes a whole geodesic axis in $\mathbb{H}^3$), **parabolic** ($|\mathrm{tr}|^2=4$; fixes one boundary point, translation-like near infinity), **loxodromic** ($|\mathrm{tr}|^2>4$ real, or complex with nonzero imaginary part; fixes two boundary points; screw motion).
> **In words:** three families of $\mathbb{H}^3$-isometries; loxodromic is the interesting one for closed geodesics — it slides along an axis by real length $\ell_\gamma$ **and** rotates by angle $\theta_\gamma$ around the axis, packaged into $L_\gamma=\ell_\gamma+i\theta_\gamma$.
> **Concretely:** $\tau(z,y)=(2z,2y)$ has real trace with $|\mathrm{tr}|^2>4$ and is loxodromic with real complex length $\ell_\gamma=\log 2$, $\theta_\gamma=0$ (pure translation, a "hyperbolic" element). $\tau(z,y)=(2iz,2y)$ has complex trace with nonzero imaginary part and is again loxodromic, with $L_\gamma=\log 2+i\pi/2$ (a screw motion with a quarter-turn per period).

> [!recall]- Centraliser $C_\Gamma(g)$
> **Formally:** $C_\Gamma(g):=\{q\in\Gamma:qg=gq\}$, the subgroup of $\Gamma$ commuting with $g$. **Fact:** for $\tau\in\Gamma$ a primitive loxodromic element ($\Gamma$ torsion-free discrete in $\mathrm{PSL}(2,\mathbb{C})$), $C_\Gamma(\tau^m)=\langle\tau\rangle=\{\tau^k:k\in\mathbb{Z}\}$.
> **In words:** the set of wallpaper symmetries that don't change $g$ when you conjugate by them — "the symmetries preserving $g$'s action". Any $q$ commuting with $\tau$ must preserve $\tau$'s axis (the unique geodesic $\tau$ preserves) and preserve the complex length; the only elements of $\Gamma$ doing that are the powers of $\tau$.
> **Concretely:** if $\tau(z,y)=(2z,2y)$, then $C_\Gamma(\tau)$ contains all $\tau^m:(z,y)\mapsto(2^m z,2^m y)$ and nothing else — no other element of a torsion-free $\Gamma$ can commute with $\tau$ without being a proper power thereof.

---

# The Definition

> **Definition (hyperbolic 3-space; Kleinian group; complex length).** **Hyperbolic 3-space** is $\mathbb{H}^3=\{(z,y):z\in\mathbb{C},y>0\}$ with the constant-curvature-$(-1)$ metric $ds^2=(|dz|^2+dy^2)/y^2$, volume $d\!\operatorname{vol}_{\mathbb{H}^3}=y^{-3}\,dA(z)\,dy$ ($dA$ Euclidean area on $\mathbb{C}$), and isometry group $\mathrm{PSL}(2,\mathbb{C})$. A **Kleinian group** is a discrete torsion-free $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ acting freely and properly discontinuously; then $X=\Gamma\backslash\mathbb{H}^3$ is a complete orientable **hyperbolic 3-manifold**. A non-parabolic, non-elliptic $\tau\in\Gamma$ is **loxodromic**: it fixes two boundary points, preserves the geodesic between them (its axis), and acts by translating length $\ell_\gamma>0$ *and* rotating angle $\theta_\gamma\in\mathbb{R}/2\pi\mathbb{Z}$ about it. Its **complex length** is
> $$L_\gamma:=\ell_\gamma+i\theta_\gamma.$$
> Conjugating in $\mathrm{PSL}(2,\mathbb{C})$, $\tau$ takes the **standard form** $\tau:(z,y)\mapsto(e^{L_\gamma}z,\,e^{\ell_\gamma}y)$, with axis the vertical geodesic from $0$ to $\infty$. Non-trivial non-peripheral free homotopy classes correspond to loxodromic conjugacy classes, each with a unique closed geodesic representative; centralisers are cyclic ($C_\Gamma(\tau^m)=\langle\tau\rangle$) exactly as in 2D.

> **Definition (the $\mathbb{H}^3$ heat kernel).** The Brownian [[Def - Heat Kernel and Heat Semigroup|heat kernel]] on $\mathbb{H}^3$ has the closed form
> $$p_{\mathbb{H}^3}(t,z,w)=\frac{1}{(4\pi t)^{3/2}}\,\frac{u}{\sinh u}\,e^{-t-u^2/(4t)},\qquad u=d(z,w),$$
> depending only on the hyperbolic distance $u$; the factor $u/\sinh u$ is the 3D curvature correction and $e^{-t}$ the spectral shift (the bottom of the $\mathbb{H}^3$ spectrum is $1=(\frac{n-1}{2})^2$ for $n=3$).

**Concrete unpacking.** In the standard form, $\operatorname{Im}$-height $y$ scales by the *real* factor $e^{\ell_\gamma}$ while the horizontal $z$ both scales and rotates by $e^{L_\gamma}=e^{\ell_\gamma}e^{i\theta_\gamma}$. So each $\langle\tau\rangle$-orbit meets the **slab** $\{1\le y<e^{\ell_\gamma}\}$ once (the rotation stays within a slab), giving the fundamental region $\mathcal F_\tau=\{(z,y):1\le y<e^{\ell_\gamma}\}$ — the exact 3D analogue of the 2D strip, with an extra rotational coordinate. When $\theta_\gamma=0$ everything reduces to the surface case ($L_\gamma=\ell_\gamma$, $|e^{L}-1|^2=(e^{\ell}-1)^2$).

**Standard names.** **Hyperbolic 3-space** / upper half-space model; **$\mathrm{PSL}(2,\mathbb{C})$**; **Kleinian group** (discrete subgroup of $\mathrm{PSL}(2,\mathbb{C})=\operatorname{Isom}^+(\mathbb{H}^3)$); **loxodromic** element; **complex length** (translation length $+i$ holonomy angle). References: Ratcliffe, *Foundations of Hyperbolic Manifolds*; Thurston, *Three-Dimensional Geometry and Topology*.

---

# Examples and Non-Examples

**Is an instance.** Take $\Gamma=\langle(z,y)\mapsto(z+1,y),\,(z,y)\mapsto(z+i,y)\rangle$ (translations by $1$ and $i$ in the horizontal $\mathbb{C}$-plane) — this is the 3D analogue of the flat torus setup and $\Gamma\backslash\mathbb{H}^3$ is a solid rectangular chimney (a rank-2 cusp). For a genuinely hyperbolic (loxodromic) example, take $\Gamma=\langle\tau\rangle$ with $\tau(z,y)=(2iz,2y)$; $\Gamma\backslash\mathbb{H}^3$ is a solid torus with a quarter-twist per period. A famous compact example is the **figure-eight knot complement** — its fundamental group is a Kleinian $\Gamma\subset\mathrm{PSL}(2,\mathbb{Z}[\omega])$ where $\omega$ is a primitive cube root of unity (so $\mathbb{Z}[\omega]$ is the Eisenstein integers); full construction details are beyond our floor (see Thurston), but the takeaway is that infinitely many complicated $3$-manifolds arise this way. A purely-translating loxodromic ($\theta_\gamma=0$) is called *hyperbolic*; a general one rotates too.

**Is NOT an instance.** A **parabolic** element of $\mathrm{PSL}(2,\mathbb{C})$ (one fixed boundary point) has no axis and no complex length — its class is peripheral (into a cusp), excluded as in 2D. A **purely elliptic** element (rotation, finite order) is excluded by torsion-freeness.

**Calibration check.** (1) Verify $\tau:(z,y)\mapsto(e^{L_\gamma}z,e^{\ell_\gamma}y)$ is an isometry of $ds^2=(|dz|^2+dy^2)/y^2$. (2) Check each $\langle\tau\rangle$-orbit meets $\{1\le y<e^{\ell_\gamma}\}$ once (the height scales by $e^{\ell_\gamma}$). (3) Confirm $p_{\mathbb{H}^3}$ reduces near $u\to0$ to the flat 3D Gaussian $(4\pi t)^{-3/2}e^{-u^2/4t}$ (since $u/\sinh u\to1$, $e^{-t}\to1$).

---

# Where the paper uses this

§7 sets $X=\Gamma\backslash\mathbb{H}^3$ and proves Theorem 7.1 (homotopy-class decomposition, identical in structure to Theorem 3.2 with the loxodromic standard form), Theorem 7.2 (subordinate mass), and Corollary 7.3 (the closed-form Brownian mass $\frac1m\frac{1}{|e^{mL_\gamma/2}-e^{-mL_\gamma/2}|^2}$). The explicit $\mathbb{H}^3$ heat kernel is what lets §7 derive its own strip integral (rather than citing Wang–Xue as §3 did). **[[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7]]**.

---

# Verified against

Ratcliffe, *Foundations of Hyperbolic Manifolds* (2nd ed.), Ch. 4, 12 (upper half-space model, $\mathrm{PSL}(2,\mathbb{C})$ isometries, loxodromic classification, complex length); Elstrodt–Grunewald–Mennicke, *Groups Acting on Hyperbolic Space*, for the explicit $\mathbb{H}^3$ heat kernel $p(t)=(4\pi t)^{-3/2}\frac{u}{\sinh u}e^{-t-u^2/4t}$. Complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$ standard. Matches the paper's §7.

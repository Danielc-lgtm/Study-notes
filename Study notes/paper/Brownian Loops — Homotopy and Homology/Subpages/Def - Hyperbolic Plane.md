---
type: definition
subject: geometry
prereqs:
  - "Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure"
tags: [geometry, hyperbolic-geometry, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$\mathbb{H}^2$ the upper half-plane $\{z=x+iy\in\mathbb{C}:y=\operatorname{Im}z>0\}$. $\mathrm{PSL}(2,\mathbb{R})$ the group of $2\times2$ real matrices of determinant $1$, modulo $\pm\mathrm{Id}$; an element $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ acts by the Möbius map $z\mapsto\frac{az+b}{cz+d}$. $d(z,w)$ hyperbolic distance; $\rho$ the hyperbolic area measure.

---

# Axiom Motivation

The paper's surfaces are *hyperbolic* — they carry a metric of constant curvature $-1$. Every such surface is, upstairs, the same single model space, the hyperbolic plane $\mathbb{H}^2$, folded up by a group of symmetries (a [[Def - Fuchsian Group and the Hyperbolic Quotient Surface|Fuchsian group]]). So all the geometry the paper needs — distances, areas, the Laplacian, geodesics, isometries — can be computed once on $\mathbb{H}^2$ and then transported down to the surface. This is the hyperbolic analogue of doing trigonometry on the round sphere before working on a curved 2-sphere: there is one maximally symmetric model, and everything reduces to it.

Why the specific metric $|dz|^2/y^2$? Two demands force it. First, we want *constant negative curvature*; the upper half-plane with $ds^2=(dx^2+dy^2)/y^2$ is the standard realisation of curvature $-1$. Second, we want a large symmetry group so that "all points and all directions look the same" (homogeneity and isotropy) — and indeed $\mathrm{PSL}(2,\mathbb{R})$ acts on $\mathbb{H}^2$ by isometries, transitively, which is exactly what lets the paper move a geodesic into a convenient "standard position" (the imaginary axis) without loss of generality. The $1/y^2$ weight is what makes horizontal translations, dilations, and the inversion $z\mapsto-1/z$ all preserve lengths.

---

# The Definition

> **Definition (hyperbolic plane).** The **hyperbolic plane** is the [[Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure|Riemannian surface]] $\mathbb{H}^2=\{y>0\}$ with metric $g_{ij}=y^{-2}\delta_{ij}$, i.e. line element
> $$ds^2 = \frac{dx^2+dy^2}{y^2}.$$
> Its **area measure** is $\rho = \dfrac{dx\,dy}{y^2}$, its **Gaussian curvature** is constant $\equiv -1$, and its **Laplace–Beltrami operator** is $\Delta_{\mathbb{H}^2} = -y^2(\partial_x^2+\partial_y^2)$. The group $\mathrm{PSL}(2,\mathbb{R})$ acts by orientation-preserving **isometries** through Möbius maps $z\mapsto\frac{az+b}{cz+d}$; this action is transitive, and $\Delta_{\mathbb{H}^2}$ and $\rho$ are invariant under it.

> **Definition (geodesics; classification of isometries).** The **geodesics** (shortest curves) of $\mathbb{H}^2$ are the vertical half-lines $\{x=\text{const}\}$ and the half-circles centred on the real axis $\{|z-c|=r,\ y>0\}$. A non-identity isometry $\tau\in\mathrm{PSL}(2,\mathbb{R})$ is **hyperbolic** if $|\operatorname{tr}\tau|>2$: it then fixes two points of the boundary $\partial\mathbb{H}^2=\mathbb{R}\cup\{\infty\}$, preserves the geodesic joining them (its **axis**), and translates along that axis by a distance $\ell>0$, the **translation length**, with $|\operatorname{tr}\tau|=2\cosh(\ell/2)$. (The other types are **elliptic**, $|\operatorname{tr}|<2$, a rotation fixing an interior point; and **parabolic**, $|\operatorname{tr}|=2$, fixing one boundary point.)

**Concrete unpacking (the standard form used throughout §3).** Conjugating in $\mathrm{PSL}(2,\mathbb{R})$, any hyperbolic $\tau$ with translation length $\ell$ can be moved to $\tau:z\mapsto e^{\ell}z$, the map that scales by $e^\ell$. Its axis is the imaginary half-line $\{x=0,\,y>0\}$, and it acts there by $iy\mapsto e^\ell iy$: since hyperbolic arclength along the axis is $\int dy/y=\log$, the point $iy$ moves to $ie^\ell y$, a hyperbolic distance $\log(e^\ell y)-\log y=\ell$. So "$z\mapsto e^\ell z$" is literally "translate the axis by $\ell$", and $\operatorname{Im}(\tau z)=e^\ell\operatorname{Im}(z)$ rescales the imaginary part — the fact §3 uses to build the fundamental strip $1\le\operatorname{Im}z<e^\ell$.

**Standard names.** **Hyperbolic plane** / **upper half-plane model** (the other standard model is the **Poincaré disc**); **Möbius transformations**; **hyperbolic / elliptic / parabolic** classification of isometries; **translation length** (also **displacement length**). The vault already treats the hyperbolic plane as a Riemannian manifold and its geodesics — see the Riemannian-Geometry exercises — but has no standalone `Def` page, so this note serves the paper.

---

# Examples and Non-Examples

**Is an instance.** The map $z\mapsto z+1$ (parabolic, fixes $\infty$); $z\mapsto 2z$ (hyperbolic, axis the imaginary axis, translation length $\log 2$); $z\mapsto-1/z$ (elliptic, fixes $i$). Geodesic: the unit semicircle $|z|=1$, $y>0$.

**Is NOT an instance.** The Euclidean metric $dx^2+dy^2$ on the same set $\{y>0\}$ is **not** the hyperbolic plane — it is flat (curvature $0$), its geodesics are straight lines, and its isometry group is much smaller. The $1/y^2$ factor is what creates the negative curvature and the huge isometry group.

**Calibration check.** (1) Verify $\Delta_{\mathbb{H}^2}=-y^2(\partial_x^2+\partial_y^2)$ from the coordinate Laplace–Beltrami formula with $g_{ij}=y^{-2}\delta_{ij}$. (2) Check that $z\mapsto z+1$ and $z\mapsto\lambda z$ ($\lambda>0$) preserve $ds^2=|dz|^2/y^2$. (3) For $\tau:z\mapsto e^\ell z$, confirm the translation length along the imaginary axis is $\ell$ and $|\operatorname{tr}\tau|=2\cosh(\ell/2)$ (with $\tau=\begin{pmatrix}e^{\ell/2}&0\\0&e^{-\ell/2}\end{pmatrix}$).

---

# Where the paper uses this

$\mathbb{H}^2$ is the universal cover of every surface in the paper from §3 on; its $\mathrm{PSL}(2,\mathbb{R})$-invariant heat kernel and area measure descend to $X=\Gamma\backslash\mathbb{H}^2$. The standard form $\tau:z\mapsto e^{\ell_\gamma}z$ and the imaginary-axis geodesic are the coordinates in which Theorem 3.2's fundamental-strip computation is done. **[[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.3.3]]** and **[[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]]**.

---

# Verified against

Katok, *Fuchsian Groups*, Ch. 1 (upper half-plane model, $\mathrm{PSL}(2,\mathbb{R})$ isometries, geodesics, hyperbolic/parabolic/elliptic classification, $|\operatorname{tr}|=2\cosh(\ell/2)$); Beardon, *The Geometry of Discrete Groups*. Curvature $-1$, area $dx\,dy/y^2$, $\Delta=-y^2(\partial_x^2+\partial_y^2)$ standard.

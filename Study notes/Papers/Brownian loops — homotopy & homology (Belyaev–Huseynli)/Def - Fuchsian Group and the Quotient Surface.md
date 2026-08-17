---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Free and Properly Discontinuous Action"
  - "Def - Fundamental Region"
tags: [paper, hyperbolic-geometry, group-theory]
---

# Signature

| symbol | type |
|---|---|
| $\mathbb{H}^2$ | $\{z\in\mathbb{C}:\operatorname{Im}z>0\}$, metric $\lvert\mathrm{d}z\rvert^2/(\operatorname{Im}z)^2$ |
| $\rho=\rho_{\mathbb{H}^2}$ | hyperbolic area: $\mathrm{d}\rho=(\operatorname{Im}z)^{-2}\,\mathrm{d}x\,\mathrm{d}y$; $\mathrm{PSL}(2,\mathbb{R})$-invariant |
| $\mathrm{PSL}(2,\mathbb{R})$ | $\mathrm{SL}(2,\mathbb{R})/\{\pm I\}$; acts by $z\mapsto\frac{az+b}{cz+d}$; $=\operatorname{Isom}^+(\mathbb{H}^2)$ |
| $\Gamma$ | $\subseteq\mathrm{PSL}(2,\mathbb{R})$, discrete and torsion-free; countable |
| $X$ | $:=\Gamma\backslash\mathbb{H}^2$; smooth complete orientable hyperbolic surface |
| $\pi$ | $\mathbb{H}^2\to X$; covering map and local isometry |
| $\rho_X$ | induced area measure on $X$; possibly $\rho_X(X)=\infty$ |
| $F$ | $\subseteq\mathbb{H}^2$ Borel; a [[Def - Fundamental Region\|fundamental region]] for $\Gamma$ |
| $\Lambda(\Gamma)$ | $\subseteq\partial\mathbb{H}^2$; the limit set |
| $\operatorname{tr}$ | trace of a lift to $\mathrm{SL}(2,\mathbb{R})$; $\lvert\operatorname{tr}\rvert$ well defined on $\mathrm{PSL}(2,\mathbb{R})$ |

---

# Definition

> **Definition (Fuchsian group; quotient surface).**
> **(D1) Discrete.** $\Gamma\subseteq\mathrm{PSL}(2,\mathbb{R})$ is discrete in the subspace topology. Equivalently, by [[Def - Free and Properly Discontinuous Action|(D2) there]], $\Gamma$ acts properly discontinuously on $\mathbb{H}^2$: $\ \forall K\Subset\mathbb{H}^2:\ \#\{h\in\Gamma: hK\cap K\neq\emptyset\}<\infty$.
> **(D2) Torsion-free.** $\ \forall h\in\Gamma\setminus\{1\}:\ h$ has infinite order. Equivalently $\Gamma$ contains no elliptic element ($\lvert\operatorname{tr}h\rvert<2$); hence, by [[Def - Free and Properly Discontinuous Action|(D1) there]], $\Gamma$ acts **freely**: $\forall h\neq1\ \forall z:\ hz\neq z$.
>
> Under (D1),(D2): $X:=\Gamma\backslash\mathbb{H}^2$ is a smooth complete orientable hyperbolic surface, $\pi$ is a covering map, $\mathbb{H}^2$ is the universal cover, and $\Gamma$ is the deck group.

> **(F1) Descent of the area measure.** $\rho_X$ is defined by [[Def - Fundamental Region|(U)]]:
> $$\int_X f\,\mathrm{d}\rho_X=\int_F (f\circ\pi)\,\mathrm{d}\rho\qquad\text{for every fundamental region }F\text{ and every Borel }f\geq0 .$$
> **This identity is Step 2 of [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]]** and is a definition, not a trick.
>
> **(F2) Isometry classification.** For $h\in\mathrm{PSL}(2,\mathbb{R})\setminus\{1\}$: $\lvert\operatorname{tr}h\rvert<2$ **elliptic** (one fixed point in $\mathbb{H}^2$); $=2$ **parabolic** (one fixed point on $\partial\mathbb{H}^2$, none inside); $>2$ **hyperbolic** (two fixed points on $\partial\mathbb{H}^2$, none inside). Under (D2), $\Gamma$ has only parabolic and hyperbolic elements.

---

# Type card

> [!abstract] Type card — Fuchsian group and quotient
> **Given.** **(H1)** $\Gamma\subseteq\mathrm{PSL}(2,\mathbb{R})$ satisfying (D1),(D2).
>
> **Produces.** A smooth complete orientable hyperbolic surface $X=\Gamma\backslash\mathbb{H}^2$; a covering $\pi:\mathbb{H}^2\to X$ with deck group $\Gamma$; and the measure $\rho_X$ characterised by (F1).
>
> **Lets you.** Convert every topological question about loops on $X$ into a group-theoretic question about $\Gamma$, and write every analytic object on $X$ as a $\Gamma$-indexed sum upstairs. §3 is that conversion carried out.

---

# Depends on

- [[Def - Free and Properly Discontinuous Action]] — (D1),(D2) are the two clauses there; the covering consequence
- [[Def - Fundamental Region]] — for (F1)
- [[Def - Group Action]] — the action itself
- 🟢 $\mathbb{H}^2$, $\mathrm{PSL}(2,\mathbb{R})$, hyperbolic area — [[Def - The Hyperbolic Space H^n]]

---

# Checks

**Instance.** $\Gamma=\langle\tau\rangle$, $\tau:z\mapsto e^{\ell}z$, $\ell>0$. (D1): discrete, verified in [[Def - Free and Properly Discontinuous Action|the instance there]]. (D2): $\lvert\operatorname{tr}\tau\rvert=2\cosh(\ell/2)>2$, so $\tau$ is hyperbolic and of infinite order. $X$ is the **hyperbolic cylinder**: exactly one primitive closed geodesic (image of the imaginary axis, length $\ell$), plus its iterates and its orientation reversal. Fundamental region $F_\tau=\{1\leq\operatorname{Im}z<e^{\ell}\}$. **§3 reduces every general $\Gamma$ to this case, one primitive geodesic at a time.**

**Non-instance (fails D2).** $\Gamma=\langle\sigma\rangle$ with $\sigma$ elliptic of order $n$ fixing $z_0$. (D1) holds ($\Gamma$ finite, hence discrete); (D2) fails. $X$ is a hyperbolic *orbifold* with a cone point of angle $2\pi/n$: not a manifold, $\pi$ not a covering at $z_0$, and the correspondence of [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] breaks there.

**Non-instance (fails D1).** $\Gamma=\mathrm{PSL}(2,\mathbb{R})$: not discrete; the orbit space is a point.

---

# Used at

- [[Def - Geometrically Finite Surfaces, Cusps and Funnels]] — which quotients the paper works with
- [[Def - Deck Transformations and the Lift of a Rooted Loop]] — the covering dictionary on $\pi$
- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — classes on $X$ $\leftrightarrow$ conjugacy classes in $\Gamma$
- [[Constr - The Periodised Kernel]] — the $\Gamma$-indexed sum
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — (F1) is Step 2
- [[Def - Critical Exponent]] — $\delta=\dim_H\Lambda(\Gamma)$
- [[Def - Kleinian Group and Loxodromic Complex Length]] — the $\mathrm{PSL}(2,\mathbb{C})$ analogue

---

# Commentary

> [!note]- Commentary (skippable)
> The paper writes "let $\Gamma\subset\mathrm{PSL}(2,\mathbb{R})$ be a torsion-free Fuchsian group, acting freely and properly discontinuously on $\mathbb{H}^2$" — four adjectives for two conditions. *Fuchsian* $=$ discrete $=$ properly discontinuous; *torsion-free* $\Rightarrow$ no elliptics $\Rightarrow$ free. The two properties named in the sentence are consequences, not extra hypotheses.
>
> The classification (F2) is what makes torsion-freeness cheap to use: excluding elliptics excludes exactly the elements with an interior fixed point, and the remaining two types map onto the two kinds of end the quotient can have — parabolics give cusps, hyperbolics give closed geodesics and funnels. References for the general theory: Buser, Katok, Borthwick, Ratcliffe.

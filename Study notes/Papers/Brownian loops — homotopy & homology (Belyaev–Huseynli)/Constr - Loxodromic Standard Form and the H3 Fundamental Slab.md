---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Kleinian Group and Loxodromic Complex Length"
  - "Def - Fundamental Region"
tags: [paper, hyperbolic-geometry, kleinian-groups]
---

# Signature

| symbol | type |
|---|---|
| $\mathbb{H}^3$ | $\{(z,y):z\in\mathbb{C},\,y>0\}$, metric $\frac{\lvert\mathrm{d}z\rvert^2+\mathrm{d}y^2}{y^2}$ |
| $\tau$ | the standard-form loxodromic, $\tau(z,y)=(e^{L_\gamma}z,\,e^{\ell_\gamma}y)$ |
| $L_\gamma$ | $=\ell_\gamma+i\theta_\gamma$; $\tau^m(z,y)=(e^{mL_\gamma}z,\,e^{m\ell_\gamma}y)$ |
| $F_\tau$ | $:=\{(z,y)\in\mathbb{H}^3:1\leq y<e^{\ell_\gamma}\}$ — the **fundamental slab** |
| $\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}$ | $=y^{-3}\,\mathrm{d}A(z)\,\mathrm{d}y$, $\mathrm{d}A$ Euclidean area on $\mathbb{C}$ |

---

# Construction

> **(82) Standard form.** Fix a representative $\tau\in\Gamma$ of a primitive loxodromic class and conjugate in $\mathrm{PSL}(2,\mathbb{C})$ so that
> $$\tau:(z,y)\longmapsto\big(e^{L_\gamma}z,\ e^{\ell_\gamma}y\big),$$
> the isometry whose axis is the vertical geodesic from $0$ to $\infty$, translating along it by $\ell_\gamma$ and rotating about it by $\theta_\gamma$.
>
> **(84) Fundamental slab.**
> $$F_\tau:=\{(z,y)\in\mathbb{H}^3:1\leq y<e^{\ell_\gamma}\}.$$

> **(P1) $F_\tau$ is a fundamental region for $\langle\tau\rangle$.** $\tau$ scales the height by the **real** factor $e^{\ell_\gamma}$, so each $\langle\tau\rangle$-orbit meets $\{1\leq y<e^{\ell_\gamma}\}$ in exactly one point. The rotation $\theta_\gamma$ acts **within** each slab and does not change which slab a point lies in. This verifies [[Def - Fundamental Region|(D1),(D2)]]. *Consumer:* [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Thm 7.1]].
>
> **(P2) Displacement.** For $w=(z,y)$ and $u=d(w,\tau^mw)$,
> $$\cosh u=1+\frac{\lvert z-e^{mL_\gamma}z\rvert^2+(y-e^{m\ell_\gamma}y)^2}{2e^{m\ell_\gamma}y^2}=\cosh(m\ell_\gamma)+\frac{\lvert e^{mL_\gamma}-1\rvert^2\lvert z\rvert^2}{2e^{m\ell_\gamma}y^2},$$
> using $\lvert e^{mL_\gamma}-1\rvert^2=1-2e^{m\ell_\gamma}\cos(m\theta_\gamma)+e^{2m\ell_\gamma}$ and $1+\frac{(1-e^{m\ell_\gamma})^2}{2e^{m\ell_\gamma}}=\cosh(m\ell_\gamma)$. *Consumer:* [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity|(88),(89)]].
>
> **(P3) $u$ depends on $z$ only through $r=\lvert z\rvert$.** So in polar coordinates $z=re^{i\varphi}$ the angular integral contributes a factor $2\pi$. *Consumer:* the same.
>
> **(P4) The slab integrates to $\ell_\gamma$.** $\int_1^{e^{\ell_\gamma}}y^{-1}\,\mathrm{d}y=\ell_\gamma$, after the $y^2$ from (P2)'s change of variables meets the $y^{-3}$ of the volume element. *Consumer:* the factor $\ell_\gamma$ in (88).
>
> **(P5) Periodisation convergence, assumed.** The paper **assumes** that $p^E_{\mathbb{H}^3}$ decays fast enough in its spatial variables that, together with discreteness of $\Gamma$, the periodisation $\sum_{h\in\Gamma}p^E_{\mathbb{H}^3}(t,w,hw')$ converges absolutely. *Consumer:* [[Constr - The Periodised Kernel]], hence Theorem 7.1. **This is a hypothesis, not a lemma.**

> [!warning] Two different roles for $L_\gamma$ and $\ell_\gamma$
> The height scales by $e^{\ell_\gamma}$ — the **real part only**. The horizontal coordinate scales by $e^{L_\gamma}$ — the full complex number. Swapping them breaks (P1): a complex scaling of the height is not even a self-map of $\mathbb{H}^3$.

---

# Type card

> [!abstract] Type card — standard form and slab
> **Given.** **(H1)** $\tau\in\Gamma$ primitive loxodromic with complex length $L_\gamma$. **(H2)** conjugation in $\mathrm{PSL}(2,\mathbb{C})$ is available — free, since all §7 quantities are conjugation-invariant.
>
> **Produces.** An explicit normal form (82) and an explicit fundamental region (84), together with the displacement formula (P2) and the reduction (P3),(P4) of a $3$-dimensional integral to a one-dimensional one.
>
> **Lets you.** Compute $\int_{F_\tau}p_{\mathbb{H}^3}(t,w,\tau^mw)\,\mathrm{d}\mathrm{vol}$ in closed form — the $3$-dimensional replacement for the [[Ext - Wang–Xue Strip Identity|(WX)]] strip identity of §3, which §7 **derives itself** rather than importing.

---

# Depends on

- [[Def - Kleinian Group and Loxodromic Complex Length]] — the invariants $\ell_\gamma,\theta_\gamma$
- [[Def - Fundamental Region]] — (D1),(D2) are what (P1) verifies
- [[Constr - Standard-Form Representative and the Fundamental Strip]] — the $2$-dimensional analogue; compare $F_\tau=\{1\leq\lvert z\rvert<e^{\ell_\gamma}\}$ there
- 🟢 the upper half-space model, its metric and distance formula — *Riemannian Geometry*

---

# Consumed by

- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — (P1),(P5)
- [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]] — (P2),(P3),(P4)
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]]
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]]

---

# Commentary

> [!note]- Commentary (skippable)
> The construction is the $3$-dimensional twin of §3's, and the parallel is worth holding in view. In dimension $2$ one conjugates $\tau$ to $z\mapsto e^{\ell_\gamma}z$ on $\mathbb{H}^2$ and takes the annular strip $1\leq\lvert z\rvert<e^{\ell_\gamma}$; in dimension $3$ one conjugates to $(z,y)\mapsto(e^{L_\gamma}z,e^{\ell_\gamma}y)$ and takes the horizontal slab $1\leq y<e^{\ell_\gamma}$. In both cases the fundamental region is picked out by the coordinate that scales **really**, and the rotation is invisible to that choice.
>
> The computation (P2)–(P4) is where dimension $3$ pays for itself. Because the $\mathbb{H}^3$ heat kernel is elementary — $\frac{1}{(4\pi t)^{3/2}}\frac{u}{\sinh u}e^{-t-u^2/4t}$, with no integral remaining — the change of variables $r\mapsto u$ produces a Jacobian containing $\sinh u$, which **cancels the $1/\sinh u$ exactly**. The result is a clean Gaussian in $u$ integrated from $m\ell_\gamma$ to $\infty$, and the whole slab integral collapses to elementary functions. In dimension $2$ the analogous kernel has no closed form and the corresponding identity had to be imported from Wang–Xue.
>
> (P5) is the one place §7 assumes rather than proves. The decay hypothesis on $p^E_{\mathbb{H}^3}$ is stated without verification and is what makes the periodised kernel and hence Theorem 7.1 legitimate; for Brownian motion and the subordinate cases treated it is standard, but the paper does not say so explicitly.

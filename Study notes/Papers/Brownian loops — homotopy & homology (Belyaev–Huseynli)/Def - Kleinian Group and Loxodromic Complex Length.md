---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
  - "Def - Free and Properly Discontinuous Action"
tags: [paper, hyperbolic-geometry, kleinian-groups]
---

# Signature

| symbol | type |
|---|---|
| $\mathbb{H}^3$ | upper half-space model $\{(z,y):z\in\mathbb{C},\,y>0\}$ |
| $\Gamma$ | $\subset\mathrm{PSL}(2,\mathbb{C})$ discrete and **torsion-free** — a Kleinian group |
| $X$ | $=\Gamma\backslash\mathbb{H}^3$, a complete orientable hyperbolic $3$-manifold |
| $\tau$ | a **loxodromic** element: non-parabolic, non-elliptic |
| $\ell_\gamma$ | $\in(0,\infty)$ — translation length along the axis |
| $\theta_\gamma$ | $\in\mathbb{R}/2\pi\mathbb{Z}$ — holonomy rotation about the axis |
| $L_\gamma$ | $:=\ell_\gamma+i\theta_\gamma\in\mathbb{C}$ — the **complex length**; $mL_\gamma=m\ell_\gamma+im\theta_\gamma$ |
| $\mathcal{P}_X$ | primitive **oriented** closed geodesics $\leftrightarrow$ primitive loxodromic conjugacy classes |

---

# Definition

> **(D1) Kleinian group.** $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ discrete and torsion-free. By [[Def - Free and Properly Discontinuous Action|(D1),(D2)]], $\Gamma$ then acts **freely and properly discontinuously** on $\mathbb{H}^3$, so $X=\Gamma\backslash\mathbb{H}^3$ is a complete orientable hyperbolic $3$-manifold and $\mathbb{H}^3\to X$ is a regular covering with deck group $\Gamma$.
>
> **(D2) Complex length.** A loxodromic $\tau$ translates along a geodesic **axis** and may also rotate about it. Its invariants are
> $$L_\gamma=\ell_\gamma+i\theta_\gamma,\qquad\ell_\gamma>0,\ \theta_\gamma\in\mathbb{R}/2\pi\mathbb{Z}.$$
> $\theta_\gamma=0$ is the **hyperbolic** (purely translational) case; $\theta_\gamma\neq0$ is genuinely $3$-dimensional.
>
> **(D3) The dictionary, unchanged from §3.** For $X$ geometrically finite:
> free homotopy classes of oriented closed curves $\leftrightarrow$ conjugacy classes in $\Gamma$; non-trivial non-peripheral classes $\leftrightarrow$ **loxodromic** conjugacy classes; each such class contains a **unique** oriented closed geodesic representative.
>
> **(D4) Centraliser.** $\Gamma$ torsion-free and discrete $\Rightarrow$ anything commuting with $\tau^m$ preserves the axis of $\tau$, and the axis-preserving elements of $\Gamma$ form an infinite cyclic group:
> $$C_\Gamma(\tau^m)=\langle\tau\rangle=\{\tau^k:k\in\mathbb{Z}\}.$$
> Hence the coset enumeration $[\tau^m]_{\mathrm{conj}}=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^mr^{-1}\}$, **exactly as in §3**. (83)

---

# Type card

> [!abstract] Type card — Kleinian $\Gamma$, complex length
> **Given.** **(H1)** $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ discrete, torsion-free. **(H2)** $X=\Gamma\backslash\mathbb{H}^3$ geometrically finite.
>
> **Produces.** A hyperbolic $3$-manifold, a bijection classes $\leftrightarrow$ loxodromic conjugacy classes, and for each $\gamma\in\mathcal{P}_X$ a **complex** number $L_\gamma=\ell_\gamma+i\theta_\gamma$.
>
> **Lets you.** Rerun the whole of §3 with $\ell_\gamma$ replaced by $L_\gamma$ wherever it appears **as an exponent**, and $e^{L}-1$ replaced by $\lvert e^{L}-1\rvert^2$ wherever it appears **as a denominator**.

---

# Depends on

- [[Def - Fuchsian Group and the Quotient Surface]] — the $2$-dimensional template; everything here is its analogue
- [[Def - Free and Properly Discontinuous Action]] — (D1), and why torsion-freeness is the right hypothesis
- [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] — (D4) is verbatim the §3 argument
- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — (D3)
- [[Def - Primitive Hyperbolic Element and Translation Length]] — the $2$-dimensional $\ell_\gamma$

---

# Checks

**Instance.** $\Gamma=\langle\tau\rangle$ with $\tau:(z,y)\mapsto(e^{L_\gamma}z,e^{\ell_\gamma}y)$: a rank-one loxodromic cyclic group; $X$ is a solid-torus-like quotient with a single closed geodesic of complex length $L_\gamma$. This is the model computed explicitly in [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]].

**Instance ($\theta_\gamma=0$).** A Fuchsian group viewed inside $\mathrm{PSL}(2,\mathbb{C})$: the rotation vanishes, $L_\gamma=\ell_\gamma$ real, and every §7 formula reduces to a purely-hyperbolic one. **But not to the §3 surface formula** — the dimension still shows in the exponent of the denominator; see [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|(92)]].

**Non-instance (fails torsion-freeness).** $\Gamma$ containing an elliptic element $h$ of finite order: $h$ fixes a point of $\mathbb{H}^3$, so (D1) fails, the action is not free, and $\Gamma\backslash\mathbb{H}^3$ is an orbifold. **Consequence:** the covering is not regular in the required sense and the lifting dictionary of §3 breaks.

**Non-instance (parabolic).** $\tau$ parabolic: no axis, $\ell_\gamma=0$, no closed geodesic. Such classes are the **peripheral** ones (cusps), excluded throughout, exactly as in the surface case.

---

# Used at

- [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]] — (D2) is what the standard form (82) realises
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — (D3),(D4)
- [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds]] — $L=mL_\gamma$ complex is the whole point
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]]

---

# Commentary

> [!note]- Commentary (skippable)
> The single new phenomenon in dimension $3$ is that a closed geodesic carries a **rotation as well as a length**. A loxodromic isometry is a screw motion: translate along the axis by $\ell_\gamma$, rotate about it by $\theta_\gamma$. Packaging the pair as $L_\gamma=\ell_\gamma+i\theta_\gamma$ is not merely notational — it is exactly how the two enter the final formula, through $\lvert e^{mL_\gamma}-1\rvert^2$, where the real part controls exponential decay and the imaginary part contributes an oscillating $\cos(m\theta_\gamma)$.
>
> Everything else is unchanged. The centraliser argument (D4) is the §3 argument with "hyperbolic" replaced by "loxodromic": torsion-freeness forces anything commuting with $\tau^m$ to preserve the axis, and the axis stabiliser in a discrete group is infinite cyclic. That is why Theorem 7.1's proof can be, and is, one sentence long.
>
> Worth noting what the rotation costs downstream. In the surface case the mass depended on the class only through $L=m\ell_\gamma$, a positive real, and the resulting sum over classes was a Selberg zeta value. Here it depends on $mL_\gamma$, a complex number, and the resulting sum has no such closed form — see the open question in §7.

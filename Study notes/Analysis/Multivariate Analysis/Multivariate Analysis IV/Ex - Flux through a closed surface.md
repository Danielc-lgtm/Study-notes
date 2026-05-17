---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Divergence Theorem"
  - "Def - The Exterior Derivative"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

1. Compute the outward flux of the vector field $F(x,y,z) = (x,\ y,\ z)$ through the unit sphere $S^2 = \{x^2+y^2+z^2 = 1\}$, by converting the surface integral to a volume integral with the divergence theorem.
2. Compute the outward flux of $F(x,y,z) = (x^3,\ y^3,\ z^3)$ through the boundary of the unit ball $\{x^2+y^2+z^2 \le 1\}$.
3. Compute the outward flux of $G(x,y,z) = (y,\ -x,\ z)$ through the boundary of the solid unit cube $[0,1]^3$, and observe that the answer depends only on $\operatorname{div} G$.

**Recall:**

![[Thm - The Divergence Theorem#Statement]]

[[Thm - The Divergence Theorem|The divergence theorem]]: for a compact region $\Omega$ with $C^1$ boundary and a $C^1$ vector field $F$,
$$\int_\Omega\operatorname{div} F\;dV = \int_{\partial\Omega} F\cdot\nu\;dS,$$
where $\nu$ is the outward unit normal. The **divergence** is $\operatorname{div} F = \partial_x F_1 + \partial_y F_2 + \partial_z F_3$.

---

# Convergent Strategy

**Problem class.** A *direct application* problem: convert a flux integral through a closed surface into a volume integral, then evaluate. The [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] strategy records the trigger — *complicated closed surface, simple region $\Rightarrow$ integrate over the region* — and these are clean instances.

**Assumption pattern.** Each surface is *closed* — a sphere, the boundary of a ball, the boundary of a cube — hence the boundary of a solid region, exactly the divergence theorem's right-hand side. The fields are polynomial, so their divergences are easy.

**Theorem routing.** The divergence theorem replaces $\int_{\partial\Omega} F\cdot\nu\,dS$ by $\int_\Omega\operatorname{div} F\,dV$. Compute $\operatorname{div} F$ — a sum of three partials — and integrate the resulting (often simple) function over the solid region.

**Key decision point.** The decisive recognition is that "flux through a *closed* surface" means "boundary of a solid", which routes immediately to the divergence theorem rather than a direct surface integral. The direct surface integral over a sphere or a cube is laborious (six faces, or a spherical parametrization with a normal vector); the volume integral of the divergence is usually a one-liner. Part 3 makes the further point that the flux is governed *entirely* by $\operatorname{div} G$ — the rotational part of $G$ (the $(y, -x)$ piece, which is divergence-free) contributes nothing.

---

# Legal Operations Used

1. **Apply the general Stokes theorem (here the divergence theorem)** — converting each closed-surface flux to a volume integral.
2. **Compute $d$ of a form / a divergence** — computing $\operatorname{div} F$ as the sum of three partials.
3. **Choose the easier side of Stokes** — the whole point: the volume integral of $\operatorname{div} F$ beats the direct surface integral.

---

# Hints

> [!note]- Hint 1
> For part 1, the surface integral $\int_{S^2} F\cdot\nu\,dS$ would require parametrizing the sphere. Instead, the sphere bounds the unit ball. Compute $\operatorname{div} F$ for $F = (x, y, z)$ — it is a constant. Then the volume integral is that constant times the volume of the ball.

> [!note]- Hint 2
> For part 2, $\operatorname{div}(x^3, y^3, z^3) = 3x^2 + 3y^2 + 3z^2 = 3r^2$ in spherical terms. Integrate $3r^2$ over the unit ball — spherical coordinates make this clean, since $3r^2$ depends only on the radius.

> [!note]- Hint 3
> For part 3, compute $\operatorname{div} G$ for $G = (y, -x, z)$. The first two components contribute $\partial_x y = 0$ and $\partial_y(-x) = 0$; only the third survives. The flux is then the integral of a constant over the cube.

> [!note]- Hint 4
> In part 3, notice the field $(y, -x, 0)$ — the rotational part of $G$ — is divergence-free, so it contributes zero flux through *any* closed surface. The flux of $G$ is entirely due to the $z$-component, the part with nonzero divergence.

---

# Solution

Every flux here is through a *closed* surface, so the divergence theorem converts it to a volume integral of $\operatorname{div} F$ — and each divergence turns out simple.

**Step 1: flux of $F = (x, y, z)$ through the unit sphere.**

$$\int_{S^2} F\cdot\nu\,dS = \int_{\text{ball}}\operatorname{div} F\,dV = \int_{\text{ball}} 3\,dV = 3\cdot\frac{4}{3}\pi = 4\pi.$$

> [!note]- Derivation
> The unit sphere $S^2$ is closed; it bounds the unit ball $B = \{x^2+y^2+z^2 \le 1\}$. By the divergence theorem,
> $$\int_{S^2} F\cdot\nu\,dS = \int_B\operatorname{div} F\,dV.$$
> Compute the divergence of $F = (x, y, z)$:
> $$\operatorname{div} F = \partial_x x + \partial_y y + \partial_z z = 1 + 1 + 1 = 3.$$
> The divergence is the constant $3$. Hence
> $$\int_B\operatorname{div} F\,dV = 3\int_B dV = 3\cdot\operatorname{vol}(B) = 3\cdot\frac{4}{3}\pi = 4\pi.$$
> The outward flux is $4\pi$. (The direct surface integral would parametrize the sphere and compute $F\cdot\nu = (x,y,z)\cdot(x,y,z) = x^2+y^2+z^2 = 1$ on $S^2$, then $\int_{S^2} 1\,dS = \operatorname{area}(S^2) = 4\pi$ — the same answer, by a different route. The radial field $F = (x,y,z)$ has $F\cdot\nu = 1$ on the unit sphere, so its flux is the surface area; the divergence theorem says this equals $3$ times the volume.)

**Step 2: flux of $F = (x^3, y^3, z^3)$ through the unit ball's boundary.**

$$\int_{\partial B} F\cdot\nu\,dS = \int_B 3(x^2+y^2+z^2)\,dV = 3\int_0^{2\pi}\!\!\int_0^\pi\!\!\int_0^1 r^2\cdot r^2\sin\phi\,dr\,d\phi\,d\theta = \frac{12\pi}{5}.$$

> [!note]- Derivation
> The boundary $\partial B$ is the unit sphere, closed; apply the divergence theorem. The divergence of $F = (x^3, y^3, z^3)$ is
> $$\operatorname{div} F = \partial_x(x^3) + \partial_y(y^3) + \partial_z(z^3) = 3x^2 + 3y^2 + 3z^2 = 3r^2,$$
> writing $r^2 = x^2+y^2+z^2$. So
> $$\int_{\partial B} F\cdot\nu\,dS = \int_B 3r^2\,dV.$$
> Since the integrand depends only on the radius, use spherical coordinates, where $dV = r^2\sin\phi\,dr\,d\phi\,d\theta$:
> $$\int_B 3r^2\,dV = 3\int_0^{2\pi}d\theta\int_0^\pi\sin\phi\,d\phi\int_0^1 r^2\cdot r^2\,dr = 3\cdot(2\pi)\cdot(2)\cdot\int_0^1 r^4\,dr.$$
> Now $\int_0^1 r^4\,dr = \tfrac15$, so the flux is $3\cdot 2\pi\cdot 2\cdot\tfrac15 = \tfrac{12\pi}{5}$.

**Step 3: flux of $G = (y, -x, z)$ through the cube's boundary.**

$$\int_{\partial([0,1]^3)} G\cdot\nu\,dS = \int_{[0,1]^3}\operatorname{div} G\,dV = \int_{[0,1]^3} 1\,dV = 1.$$

> [!note]- Derivation
> The boundary of the cube $[0,1]^3$ is closed; apply the divergence theorem. The divergence of $G = (y, -x, z)$ is
> $$\operatorname{div} G = \partial_x(y) + \partial_y(-x) + \partial_z(z) = 0 + 0 + 1 = 1.$$
> So
> $$\int_{\partial([0,1]^3)} G\cdot\nu\,dS = \int_{[0,1]^3} 1\,dV = \operatorname{vol}([0,1]^3) = 1.$$
> The outward flux is $1$.
>
> *The observation.* The field $G$ splits as $G = (y, -x, 0) + (0, 0, z)$. The first part, $(y, -x, 0)$, is a *rotational* field — it circulates around the $z$-axis — and its divergence is $\partial_x y + \partial_y(-x) = 0$. A divergence-free field contributes *zero* flux through every closed surface (divergence theorem with $\operatorname{div} = 0$). So the entire flux of $G$ comes from the second part $(0, 0, z)$, with $\operatorname{div} = 1$. The rotational part is invisible to the closed-surface flux: whatever circulates in must circulate back out. The flux of $G$ is determined *solely* by $\operatorname{div} G$ — the divergence theorem makes this manifest, whereas a direct face-by-face surface integral would compute six nonzero face contributions that conspire to cancel down to $1$.

> [!note]- Complete formal solution
> **Part 1.** $S^2 = \partial B$ for the unit ball $B$. $\operatorname{div}(x,y,z) = 3$. By the divergence theorem, flux $= \int_B 3\,dV = 3\cdot\tfrac43\pi = 4\pi$.
>
> **Part 2.** $\operatorname{div}(x^3,y^3,z^3) = 3(x^2+y^2+z^2) = 3r^2$. By the divergence theorem, flux $= \int_B 3r^2\,dV = 3\int_0^{2\pi}\!\int_0^\pi\!\int_0^1 r^4\sin\phi\,dr\,d\phi\,d\theta = 3\cdot 2\pi\cdot 2\cdot\tfrac15 = \tfrac{12\pi}{5}$.
>
> **Part 3.** $\operatorname{div}(y,-x,z) = 0 + 0 + 1 = 1$. By the divergence theorem, flux $= \int_{[0,1]^3} 1\,dV = 1$. The rotational part $(y,-x,0)$ is divergence-free and contributes nothing. $\blacksquare$

---

# Key Takeaways

**"Flux through a closed surface" is a reflexive trigger for the divergence theorem — never integrate over the surface directly.** A closed surface — a sphere, the boundary of a ball, the boundary of any solid — is by definition the boundary of a region, which is exactly the right-hand side of the divergence theorem. The instant a problem asks for the flux of a field through a closed surface, the move is to convert it to the volume integral $\int_\Omega\operatorname{div} F\,dV$. The payoff is large and consistent: a direct surface integral requires parametrizing the surface (a spherical chart with its $\sin\phi$ Jacobian, or six separate face integrals for a cube) and computing $F\cdot\nu$, whereas the volume integral needs only $\operatorname{div} F$ — three partial derivatives — and an integral over a solid region, which is frequently a constant times a volume. The recognition "closed surface = boundary of a solid" is the entire decision; once made, the computation is routine.

**The flux of a field through a closed surface sees only its divergence — the rotational part is invisible.** Part 3 makes this vivid: the field $G = (y, -x, z)$ has a rotational part $(y, -x, 0)$ that circulates around the $z$-axis and contributes *exactly zero* to the closed-surface flux, because it is divergence-free. Whatever a divergence-free field carries into a closed region it carries back out; there is no net flux. This is a structural fact, not a coincidence: by the divergence theorem, the flux through a closed surface equals $\int_\Omega\operatorname{div} F\,dV$, which depends on $F$ only through $\operatorname{div} F$. The practical consequence for problem-solving: before computing, *split the field into its divergence-free and divergence-carrying parts* — only the latter matters for a closed-surface flux, and discarding the former can drastically simplify the computation. This is the Helmholtz-decomposition intuition (a field splits into a curl part and a gradient part) seen through the divergence theorem.

**A radially-dependent divergence calls for spherical coordinates; match the coordinate system to the symmetry of $\operatorname{div} F$.** In part 2 the divergence came out as $3r^2$ — a function of the radius alone — and the volume integral then separated cleanly in spherical coordinates, the angular integrals contributing constant factors ($2\pi$ and $2$) and the radial integral reducing to $\int_0^1 r^4\,dr$. The general lesson: after the divergence theorem hands you $\int_\Omega\operatorname{div} F\,dV$, look at the symmetry of $\operatorname{div} F$ and choose coordinates to match — spherical if it depends only on $r$, cylindrical if only on the distance to an axis, Cartesian if it is a polynomial over a box. The divergence theorem does the conceptual work of reducing flux to a volume integral; choosing the right coordinates for that volume integral is the second, separate, optimization, and it is governed by the symmetry of the divergence, not of the original field.

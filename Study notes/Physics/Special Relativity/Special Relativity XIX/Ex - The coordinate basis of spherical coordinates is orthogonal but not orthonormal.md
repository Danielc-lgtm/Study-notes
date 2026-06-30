---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Arbitrary Coordinates and the Coordinate Basis"
tags: [physics, special-relativity]
---

# Problem Statement

On flat spacetime use spherical coordinates $(x^\alpha) = (ct,r,\theta,\varphi)$, defined from inertial Cartesian coordinates $(ct',x,y,z)$ by
$$x = r\sin\theta\cos\varphi, \qquad y = r\sin\theta\sin\varphi, \qquad z = r\cos\theta.$$

1. Compute the coordinate basis vectors $\vec{e}_r$, $\vec{e}_\theta$, $\vec{e}_\varphi$ in terms of the Cartesian basis $\vec{e}_x,\vec{e}_y,\vec{e}_z$.
2. Compute the metric components $g_{\alpha\beta} = \vec{e}_\alpha\cdot\vec{e}_\beta$ and show $g_{\alpha\beta} = \mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$.
3. Show that the coordinate basis is **orthogonal** (off-diagonal $g_{\alpha\beta} = 0$) but **not orthonormal** ($g_{\theta\theta},g_{\varphi\varphi} \neq -1$), and exhibit the rescaled vectors that *are* orthonormal.
4. State why those orthonormal vectors are **not** a coordinate basis.

**Recall:**

![[Def - Arbitrary Coordinates and the Coordinate Basis#The Definition]]

The coordinate basis vector $\vec{e}_\alpha = \partial/\partial x^\alpha$ is read off the Jacobian, $\vec{e}_\alpha = (\partial x'^\beta/\partial x^\alpha)\vec{e}'_\beta$. In mostly-minus signature spatial vectors have negative norm-squared.

---

# Convergent Strategy

**Problem class.** A *compute-the-basis-and-metric* problem, the foundational drill of [[Def - Arbitrary Coordinates and the Coordinate Basis]]. The route is: Jacobian $\to$ basis vectors $\to$ dot products $\to$ metric.

**Assumption pattern.** Standard spherical coordinates; the spatial part is exactly three-dimensional Euclidean spherical geometry, and the time part is trivial since $ct' = ct$. The signpost that the basis is not orthonormal is that $\vec{e}_\theta$ and $\vec{e}_\varphi$ scale with $r$ (and $\sin\theta$).

**Theorem routing.** Part 1 differentiates the coordinate relations. Part 2 takes Euclidean dot products (with the mostly-minus sign on spatial components). Part 3 inspects the diagonal. Part 4 invokes the criterion that a coordinate basis has vanishing Lie brackets.

**Key decision point.** The interesting choice is recognising that "orthogonal but not orthonormal" is generic for curvilinear coordinate bases, and that orthonormalising destroys the coordinate-basis property — the normalised frame is a tetrad, a field of bases, but no coordinate system has it as its natural basis.

---

# Legal Operations Used

1. **Read off the metric from a coordinate change** (operation 1 from the topic page). Compute $\vec{e}_\alpha = (\partial x'^\beta/\partial x^\alpha)\vec{e}'_\beta$ and then $g_{\alpha\beta} = \vec{e}_\alpha\cdot\vec{e}_\beta$.

---

# Hints

> [!note]- Hint 1
> $\vec{e}_r = \partial x/\partial r\,\vec{e}_x + \partial y/\partial r\,\vec{e}_y + \partial z/\partial r\,\vec{e}_z$. Differentiate the three coordinate relations with respect to $r$, $\theta$, $\varphi$ in turn.

> [!note]- Hint 2
> $\vec{e}_r$ is a unit vector (in the Euclidean sense), but $\vec{e}_\theta$ has Euclidean length $r$ and $\vec{e}_\varphi$ has length $r\sin\theta$. The spatial dot products come with a minus sign in mostly-minus signature: $g_{ij} = -(\vec{e}_i)_{\text{Eucl}}\cdot(\vec{e}_j)_{\text{Eucl}}$.

> [!note]- Hint 3
> The orthonormal frame is $\vec{e}'_1 = \vec{e}_r$, $\vec{e}'_2 = r^{-1}\vec{e}_\theta$, $\vec{e}'_3 = (r\sin\theta)^{-1}\vec{e}_\varphi$, each of norm-squared $-1$. These are the "$\hat r,\hat\theta,\hat\varphi$" of ordinary vector calculus.

> [!note]- Hint 4
> A coordinate basis satisfies $[\vec{e}_\alpha,\vec{e}_\beta] = 0$ (mixed partials of coordinates commute). Compute $[\vec{e}'_1,\vec{e}'_2] = [\vec{e}_r, r^{-1}\vec{e}_\theta]$ — it is nonzero because $r^{-1}$ depends on $r$. A frame with nonzero Lie bracket cannot be any coordinate system's natural basis.

---

# Solution

The plan: differentiate the coordinate relations for the basis vectors (Step 1), dot them to get the diagonal metric (Step 2), then observe that normalising the angular vectors gives the orthonormal frame, which has a nonzero Lie bracket and so is not a coordinate basis (Step 3).

**Step 1: The coordinate basis vectors.**

> [!note]- Derivation
> Differentiating $x = r\sin\theta\cos\varphi$, $y = r\sin\theta\sin\varphi$, $z = r\cos\theta$:
> $$\vec{e}_r = \sin\theta\cos\varphi\,\vec{e}_x + \sin\theta\sin\varphi\,\vec{e}_y + \cos\theta\,\vec{e}_z,$$
> $$\vec{e}_\theta = r\cos\theta\cos\varphi\,\vec{e}_x + r\cos\theta\sin\varphi\,\vec{e}_y - r\sin\theta\,\vec{e}_z,$$
> $$\vec{e}_\varphi = -r\sin\theta\sin\varphi\,\vec{e}_x + r\sin\theta\cos\varphi\,\vec{e}_y,$$
> and $\vec{e}_{ct} = \vec{e}_{ct'}$ (the time coordinate is unchanged).

**Step 2: The metric is diagonal with $r$-dependent entries.**

> [!note]- Derivation
> Take Euclidean dot products of the spatial basis vectors and attach the mostly-minus sign $g_{ij} = -(\vec{e}_i\cdot\vec{e}_j)_{\text{Eucl}}$ for spatial indices, with $g_{(ct)(ct)} = +1$.
>
> *Radial.* $(\vec{e}_r\cdot\vec{e}_r)_{\text{Eucl}} = \sin^2\theta\cos^2\varphi + \sin^2\theta\sin^2\varphi + \cos^2\theta = \sin^2\theta + \cos^2\theta = 1$, so $g_{rr} = -1$.
>
> *Polar.* $(\vec{e}_\theta\cdot\vec{e}_\theta)_{\text{Eucl}} = r^2\cos^2\theta(\cos^2\varphi+\sin^2\varphi) + r^2\sin^2\theta = r^2(\cos^2\theta+\sin^2\theta) = r^2$, so $g_{\theta\theta} = -r^2$.
>
> *Azimuthal.* $(\vec{e}_\varphi\cdot\vec{e}_\varphi)_{\text{Eucl}} = r^2\sin^2\theta(\sin^2\varphi+\cos^2\varphi) = r^2\sin^2\theta$, so $g_{\varphi\varphi} = -r^2\sin^2\theta$.
>
> *Cross terms.* $(\vec{e}_r\cdot\vec{e}_\theta)_{\text{Eucl}} = r\sin\theta\cos\theta(\cos^2\varphi+\sin^2\varphi) - r\sin\theta\cos\theta = 0$, and similarly $\vec{e}_r\cdot\vec{e}_\varphi = \vec{e}_\theta\cdot\vec{e}_\varphi = 0$. Hence
> $$g_{\alpha\beta} = \mathrm{diag}\!\left(1,\,-1,\,-r^2,\,-r^2\sin^2\theta\right).$$

**Step 3: Orthogonal but not orthonormal; the orthonormal frame is not coordinate.**

> [!note]- Derivation
> The metric is diagonal, so the coordinate basis is **orthogonal**: distinct basis vectors are mutually perpendicular. But the diagonal entries are not all $\pm 1$ — $g_{\theta\theta} = -r^2$ and $g_{\varphi\varphi} = -r^2\sin^2\theta$ depend on position — so the basis is **not orthonormal**. The vectors that *are* orthonormal are obtained by rescaling:
> $$\vec{e}'_0 = \vec{e}_{ct}, \quad \vec{e}'_1 = \vec{e}_r, \quad \vec{e}'_2 = \frac{1}{r}\vec{e}_\theta, \quad \vec{e}'_3 = \frac{1}{r\sin\theta}\vec{e}_\varphi,$$
> each of norm-squared $\mp 1$ — these are the familiar $\hat r,\hat\theta,\hat\varphi$ of three-dimensional vector calculus.
>
> These orthonormal vectors are **not** a coordinate basis. A coordinate basis must have vanishing Lie brackets, $[\vec{e}_\alpha,\vec{e}_\beta] = 0$, because $\vec{e}_\alpha = \partial/\partial x^\alpha$ and mixed partial derivatives commute. But, acting on a scalar field $f$,
> $$[\vec{e}'_1, \vec{e}'_2]f = \Big[\vec{e}_r,\ \tfrac1r\vec{e}_\theta\Big]f = \vec{e}_r\!\Big(\tfrac1r\Big)\vec{e}_\theta f + \tfrac1r[\vec{e}_r,\vec{e}_\theta]f = -\tfrac{1}{r^2}\vec{e}_\theta f + 0 = -\tfrac{1}{r^2}\,\vec{e}_\theta f = -\tfrac1r\,\vec{e}'_2 f \neq 0,$$
> using $[\vec{e}_r,\vec{e}_\theta] = 0$ (the coordinate basis brackets vanish) and $\vec{e}_r(1/r) = \partial_r(1/r) = -1/r^2$. Since the bracket is nonzero, no coordinate system has $(\vec{e}'_\alpha)$ as its natural basis: the orthonormal spherical frame is a *field of bases* (a tetrad), not a coordinate basis. This is the standard distinction between a moving frame and a coordinate basis.

> [!note]- Complete formal solution
> Differentiating the spherical-to-Cartesian relations gives $\vec{e}_r = \sin\theta\cos\varphi\,\vec{e}_x + \sin\theta\sin\varphi\,\vec{e}_y + \cos\theta\,\vec{e}_z$, $\vec{e}_\theta = r(\cos\theta\cos\varphi\,\vec{e}_x + \cos\theta\sin\varphi\,\vec{e}_y - \sin\theta\,\vec{e}_z)$, $\vec{e}_\varphi = r\sin\theta(-\sin\varphi\,\vec{e}_x + \cos\varphi\,\vec{e}_y)$. Their Euclidean dot products give $g_{rr}=-1$, $g_{\theta\theta}=-r^2$, $g_{\varphi\varphi}=-r^2\sin^2\theta$, all cross terms zero, and $g_{(ct)(ct)}=+1$, so $g_{\alpha\beta}=\mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$ — diagonal (orthogonal) but with non-unit entries (not orthonormal). The orthonormal frame $\vec{e}'_1=\vec{e}_r$, $\vec{e}'_2=r^{-1}\vec{e}_\theta$, $\vec{e}'_3=(r\sin\theta)^{-1}\vec{e}_\varphi$ has $[\vec{e}'_1,\vec{e}'_2] = -r^{-1}\vec{e}'_2 \neq 0$, so it is not a coordinate basis. $\blacksquare$

---

# Key Takeaways

**Curvilinear coordinate bases are generically orthogonal but not orthonormal, and the non-unit diagonal entries are the metric's content.** When you compute the coordinate basis of spherical, cylindrical, or any orthogonal curvilinear system, you find that the basis vectors point in mutually perpendicular directions (so the metric is diagonal) but have lengths that vary with position (so the diagonal entries are not $\pm 1$). The entries $g_{\theta\theta} = -r^2$ and $g_{\varphi\varphi} = -r^2\sin^2\theta$ are precisely the "scale factors squared" $h_\theta^2, h_\varphi^2$ of classical vector calculus, and they are what make arc length, area, and volume elements position-dependent. The trigger for this pattern is any orthogonal curvilinear coordinate system; the diagnostic is that the basis vectors $\partial/\partial(\text{angle})$ grow with radius, because a fixed angular increment sweeps a larger arc farther out.

**The coordinate basis and the orthonormal frame are different objects, and only the former satisfies $[\vec{e}_\alpha,\vec{e}_\beta]=0$.** It is tempting to conflate the coordinate basis $\partial/\partial x^\alpha$ with the orthonormal frame $\hat r,\hat\theta,\hat\varphi$, because physics problems often use the latter. They are genuinely different: the coordinate basis has non-unit lengths but vanishing Lie brackets, while the orthonormal frame has unit lengths but nonzero Lie brackets. The vanishing-bracket property is the *definition* of a coordinate basis — it is what guarantees the existence of coordinates whose natural basis it is — and the orthonormal frame fails it, so the orthonormal frame is a tetrad with no associated coordinate system. The transferable lesson is that the Christoffel formula $\Gamma = \tfrac12 g^{-1}(\partial g + \partial g - \partial g)$ works *only* for coordinate bases; in an orthonormal frame one must use the Ricci rotation coefficients instead, which carry an extra antisymmetric piece exactly because the Lie bracket is nonzero.

**Diagonal-but-non-constant metric components are the trigger for the Christoffel symbols.** The fact that $g_{\theta\theta} = -r^2$ depends on $r$ — that $\partial_r g_{\theta\theta} \neq 0$ — is precisely what makes the coordinate basis non-constant and therefore forces the covariant derivative to differ from the partial derivative. The same computation that here produced $g_{\alpha\beta}$ feeds directly into the next section's calculation of the Christoffel symbols (for instance $\Gamma^\theta{}_{r\theta} = 1/r$ comes straight from $\partial_r g_{\theta\theta} = -2r$). Recognising that "non-constant metric components" is the upstream cause of "nonzero Christoffel symbols", which is the upstream cause of "$\boldsymbol{\nabla} \neq \partial$", is the chain of reasoning that organises the entire chapter, and it all begins with the elementary observation made here that $\vec{e}_\theta$ has length $r$.

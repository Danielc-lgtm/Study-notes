---
type: remark
subject: hyperbolic-geometry
prereqs:
  - "Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length"
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
tags: [paper, brownian-loops, hyperbolic-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §7 opening — the complex length $L_\\gamma = \\ell_\\gamma + i\\theta_\\gamma$ is the correct scalar variable to replace the surface's real translation length"
---

# Notation

- $\mathbb{H}^3 = \{(z, y) : z \in \mathbb{C},\, y > 0\}$ — hyperbolic 3-space (upper half-space model); metric $ds^2 = (|dz|^2 + dy^2)/y^2$.
- $\mathrm{PSL}(2, \mathbb{C})$ — orientation-preserving isometry group of $\mathbb{H}^3$, acting on $\partial\mathbb{H}^3 = \mathbb{C} \cup \{\infty\}$ by Möbius transformations $w \mapsto (aw + b)/(cw + d)$ with $ad - bc = 1$, extended to the interior by Poincaré's construction.
- $\tau \in \mathrm{PSL}(2, \mathbb{C})$ — a **loxodromic** isometry: two distinct boundary fixed points, no interior fixed point; equivalently the eigenvalues $\lambda, \lambda^{-1}$ of any lift to $\mathrm{SL}(2, \mathbb{C})$ satisfy $|\lambda| \ne 1$.
- **Axis of $\tau$** — the unique geodesic in $\mathbb{H}^3$ joining $\tau$'s two boundary fixed points; the set of interior points $p$ minimising $d(p, \tau p)$.
- $\ell_\gamma > 0$ — the **translation length** of $\tau$: the hyperbolic distance $\tau$ moves any point on its axis, $\ell_\gamma = \min_p d(p, \tau p)$.
- $\theta_\gamma \in \mathbb{R}/2\pi\mathbb{Z}$ — the **holonomy angle** of $\tau$: the angle by which $\tau$ rotates the plane perpendicular to its axis at any axis point.
- $L_\gamma := \ell_\gamma + i\theta_\gamma \in \mathbb{C}$ — the **complex length** of $\tau$ (of the closed geodesic $\gamma$).
- $\gamma$ — the primitive oriented closed geodesic on $X = \Gamma\backslash\mathbb{H}^3$ that is the projection of $\tau$'s axis.
- $C_X(\gamma^m)$ — the free non-peripheral homotopy class of curves winding $m$ times around $\gamma$.

> [!recall]- Loxodromic isometry of $\mathbb{H}^3$
> **Formally:** $\tau \in \mathrm{PSL}(2, \mathbb{C})$ is *loxodromic* if it has two distinct fixed points on the boundary sphere $\partial\mathbb{H}^3 = \mathbb{C} \cup \{\infty\}$ and no fixed point in the interior; equivalently the lifts to $\mathrm{SL}(2, \mathbb{C})$ have eigenvalues $\lambda, \lambda^{-1}$ with $|\lambda| \ne 1$; equivalently the trace $\mathrm{tr}\,\tau \in \mathbb{C}$ satisfies $\mathrm{tr}\,\tau \notin [-2, 2]$. It preserves the geodesic joining its two fixed points — the *axis* — along which it translates by hyperbolic distance $\ell_\gamma > 0$ while simultaneously rotating the transverse plane by an angle $\theta_\gamma$.
> **In words:** a loxodromic isometry acts like a screw motion in $\mathbb{H}^3$: pick a preferred geodesic (the axis), slide points along it by a fixed distance $\ell_\gamma$, and simultaneously spin the perpendicular plane at each axis point by a fixed angle $\theta_\gamma$. When $\theta_\gamma = 0$ it is purely translational (called "hyperbolic" in 2D language); when $\theta_\gamma \ne 0$ the extra twist is what makes it "loxodromic". Non-parabolic, non-elliptic isometries of $\mathbb{H}^3$ are all loxodromic.
> **Concretely:** the map $\tau(z, y) = (2i z, 2 y)$ on the upper half-space has axis the vertical geodesic $\{(0, y) : y > 0\}$ from $0$ to $\infty$, translation length $\ell_\gamma = \log 2$ (heights double each application) and holonomy $\theta_\gamma = \pi/2$ (the horizontal $\mathbb{C}$-coordinate is multiplied by $2i$, i.e. rotated by $\pi/2$ while its modulus doubles). See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

> [!recall]- Standard form of a loxodromic in $\mathrm{PSL}(2, \mathbb{C})$
> **Formally:** any loxodromic $\tau \in \mathrm{PSL}(2, \mathbb{C})$ is conjugate in $\mathrm{PSL}(2, \mathbb{C})$ to $\tau_0 : (z, y) \mapsto (e^{L_\gamma} z,\, e^{\ell_\gamma} y)$, whose axis is the vertical geodesic $\{(0, y) : y > 0\}$; represented by the diagonal matrix $\mathrm{diag}(e^{L_\gamma/2}, e^{-L_\gamma/2}) \in \mathrm{SL}(2, \mathbb{C})$.
> **In words:** a change of coordinates in $\mathrm{PSL}(2, \mathbb{C})$ can always put a loxodromic isometry's axis on the vertical geodesic from $0$ to $\infty$ and make the isometry act as "multiply the horizontal coordinate by $e^{L_\gamma}$, multiply the height by $e^{\ell_\gamma}$." The complex factor $e^{L_\gamma} = e^{\ell_\gamma} e^{i\theta_\gamma}$ simultaneously scales *and* rotates the horizontal plane at each height. This is the 3D analogue of putting a 2D hyperbolic isometry into the form $z \mapsto e^\ell z$. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

---

# Claim / Identity

> **Claim (complex length is the right scalar variable for 3-manifolds).** For each primitive closed geodesic $\gamma$ on a hyperbolic 3-manifold $X = \Gamma\backslash\mathbb{H}^3$, the associated loxodromic conjugacy class $[\tau]_{\mathrm{conj}} \subset \Gamma$ is parametrised up to $\mathrm{PSL}(2, \mathbb{C})$-conjugacy by a single complex number
> $$L_\gamma := \ell_\gamma + i\theta_\gamma \in \mathbb{R}_{>0} + i(\mathbb{R}/2\pi\mathbb{Z}),$$
> whose real part is the hyperbolic translation length $\ell_\gamma$ (the geometric length of $\gamma$) and whose imaginary part is the holonomy angle $\theta_\gamma$ (the transverse rotation induced by parallel transport once around $\gamma$). Under the standard form $\tau_0 : (z, y) \mapsto (e^{L_\gamma} z, e^{\ell_\gamma} y)$, the factor $e^{L_\gamma}$ is the single scalar governing $\tau$'s action on the horizontal plane at every height. In every §7 formula the surface-case scalar $\ell_\gamma$ (or $e^{\ell_\gamma}$) is replaced by its complex counterpart $L_\gamma$ (or $e^{L_\gamma}$) — and the resulting complex modulus $|e^{L_\gamma} - 1|^2$ is the 3D analogue of the surface-case $(e^{\ell_\gamma} - 1)^2$.

---

# In One Line

A closed geodesic on a hyperbolic 3-manifold has two invariants (its length and the angle its transverse frame rotates through in one loop), and the complex number $L_\gamma = \ell_\gamma + i\theta_\gamma$ packages them into one so that every 3-manifold class-mass formula reads word-for-word like the surface one with $\ell_\gamma$ replaced by $L_\gamma$.

---

# Why It's True

In 2D there is nothing perpendicular to a geodesic axis, so a hyperbolic isometry's only invariant (beyond being hyperbolic) is its translation length $\ell_\gamma$ — a single real number. In 3D there is a whole plane perpendicular to the axis at each point; an isometry preserving the axis acts on that transverse plane by an orientation-preserving rotation (an element of $\mathrm{SO}(2)$), and that rotation is characterised by a single angle $\theta_\gamma \in \mathbb{R}/2\pi\mathbb{Z}$. So a loxodromic isometry needs two real parameters: how far it slides ($\ell_\gamma$) and how far it twists ($\theta_\gamma$).

The choice to bundle them into $L_\gamma = \ell_\gamma + i\theta_\gamma$ is not arbitrary. In the standard form $\tau_0(z, y) = (e^{L_\gamma} z, e^{\ell_\gamma} y)$, the horizontal $\mathbb{C}$-coordinate is multiplied by the complex number $e^{L_\gamma}$ whose modulus is $e^{\ell_\gamma}$ (the translation factor) and whose argument is $\theta_\gamma$ (the rotation angle). Multiplication by $e^{L_\gamma}$ acts on $\mathbb{C}$ as "scale by $e^{\ell_\gamma}$ *and* rotate by $\theta_\gamma$" — a **spiral similarity**, which is exactly what a screw motion looks like when restricted to a horizontal cross-section. So $L_\gamma$ is not a formal complex assemblage of two real quantities; it is the single complex eigenvalue of $\tau$'s action on horizontal planes, chosen so that "$e^{L_\gamma}$" is the actual multiplier.

The consequence for §7 formulas is direct. Wherever a surface-case identity contains $e^{\ell_\gamma}$ (as in the strip integral $\int_{\mathcal{F}_\tau} y^{-1}\,dy = \ell_\gamma$ or the mass denominator $(e^{m\ell_\gamma} - 1)^2$), the 3D case contains $e^{L_\gamma}$ (as in the strip-integral factor $|e^{L} - 1|^2$ with $L = m L_\gamma$). The modulus-squared identity
$$|e^{a + ib} - 1|^2 = 2e^a(\cosh a - \cos b)$$
turns $(e^{m\ell_\gamma} - 1)^2$ (real, surface case at $\theta_\gamma = 0$) into $|e^{mL_\gamma} - 1|^2 = 2 e^{m\ell_\gamma}(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))$ (real, 3D case with nonzero holonomy). **Mechanism: the horizontal plane at each height is a copy of $\mathbb{C}$; $\tau$'s action on it is multiplication by a single complex number whose modulus and argument are exactly $e^{\ell_\gamma}$ and $\theta_\gamma$; so the complex length $L_\gamma = \ell_\gamma + i\theta_\gamma$ is the natural exponent, and every geometric formula that had $e^{\ell_\gamma}$ upstairs becomes an $e^{L_\gamma}$ downstairs.**

At $\theta_\gamma = 0$ everything collapses to the surface case: $e^{L_\gamma} = e^{\ell_\gamma}$ is real, $|e^{L_\gamma} - 1|^2 = (e^{\ell_\gamma} - 1)^2$, the 3D formulas become the 2D ones dimension by dimension. The extra factor $(e^{m\ell_\gamma} - 1)^2 \leadsto |e^{mL_\gamma} - 1|^2$ (as opposed to $\leadsto (e^{m\ell_\gamma} - 1)^1$, say) is not a "dimensional" factor but a "cross-sectional" one — the surface case's answer $1/(m(e^{m\ell_\gamma} - 1))$ counted loops using the one-dimensional cross-section along the axis; the 3D case's answer $1/(m|e^{mL_\gamma} - 1|^2)$ counts loops using the two-dimensional cross-section, hence the squared power.

---

# Derivation

> [!note]- Gap-free derivation
>
> **Step 1 (loxodromic classification of non-elliptic, non-parabolic isometries).** Every element of $\mathrm{PSL}(2, \mathbb{C})$ is exactly one of: identity, parabolic (one boundary fixed point, no interior), elliptic (finite order, fixes an interior geodesic pointwise), or loxodromic (two boundary fixed points, no interior). For a torsion-free discrete $\Gamma$, elliptic elements are excluded (they have finite order); parabolic elements correspond to cusps and are the "peripheral" case the paper sets aside. So a non-trivial non-peripheral element of $\Gamma$ is loxodromic.
>
> **Step 2 (axis and standard form).** Let $\tau \in \Gamma$ be loxodromic with boundary fixed points $p_-, p_+ \in \partial\mathbb{H}^3$. The unique geodesic in $\mathbb{H}^3$ joining $p_-$ to $p_+$ is $\tau$'s *axis*; $\tau$ preserves it setwise. Choose $q \in \mathrm{PSL}(2, \mathbb{C})$ carrying $p_-$ to $0$, $p_+$ to $\infty$, and (using the residual $\mathrm{Stab}(\{0, \infty\}) = \mathbb{C}^* \cdot \mathrm{SO}(2)$ freedom to rescale $q$) fixing the height of any chosen base point. Then $q\tau q^{-1}$ preserves the vertical geodesic $\{(0, y) : y > 0\}$ and sends $(0, 1)$ to some $(0, e^{\ell_\gamma})$ with $\ell_\gamma > 0$ (the sign fixed by orientation); since $q\tau q^{-1}$ is an isometry of $\mathbb{H}^3$ fixing $0$ and $\infty$ on the boundary and mapping $(0, y)$ to $(0, e^{\ell_\gamma} y)$, its most general form is
> $$q\tau q^{-1}(z, y) = (\lambda z, e^{\ell_\gamma} y)$$
> for some $\lambda \in \mathbb{C}^*$. The isometry condition on the metric $ds^2 = (|dz|^2 + dy^2)/y^2$ forces $|\lambda|^2 = e^{2\ell_\gamma}$, so $\lambda = e^{\ell_\gamma} e^{i\theta_\gamma}$ for some $\theta_\gamma \in \mathbb{R}/2\pi\mathbb{Z}$. Writing $L_\gamma := \ell_\gamma + i\theta_\gamma$, this is
> $$q\tau q^{-1}(z, y) = (e^{L_\gamma} z, e^{\ell_\gamma} y).$$
> This is the standard form. The pair $(\ell_\gamma, \theta_\gamma)$ is a conjugacy-class invariant of $\tau$: any two loxodromics with the same $(\ell_\gamma, \theta_\gamma)$ are $\mathrm{PSL}(2, \mathbb{C})$-conjugate to each other.
>
> **Step 3 (geometric interpretation of $\ell_\gamma$).** Along the axis, $\tau$ sends $(0, y)$ to $(0, e^{\ell_\gamma} y)$; the hyperbolic distance is
> $$d((0, y), (0, e^{\ell_\gamma} y)) = \int_y^{e^{\ell_\gamma} y} \frac{du}{u} = \ell_\gamma.$$
> So $\ell_\gamma$ is the hyperbolic distance $\tau$ moves any axis point — the *translation length*.
>
> **Step 4 (geometric interpretation of $\theta_\gamma$).** Fix a height $y_0 > 0$ and consider the horizontal plane $P_{y_0} = \{(z, y_0) : z \in \mathbb{C}\}$ (topologically a $\mathbb{C}$, geometrically a horosphere). $\tau$ sends $P_{y_0}$ to $P_{e^{\ell_\gamma} y_0}$ and, precomposing with the geodesic flow that carries $P_{e^{\ell_\gamma} y_0}$ back to $P_{y_0}$, one gets a map $P_{y_0} \to P_{y_0}$, $z \mapsto e^{L_\gamma} z / e^{\ell_\gamma} = e^{i\theta_\gamma} z$. This map is rotation by angle $\theta_\gamma$ about the axis point $(0, y_0)$. So $\theta_\gamma$ is the *holonomy angle*: the angle by which parallel transport once around the closed geodesic $\gamma$ rotates a transverse frame.
>
> **Step 5 (why the bundling is complex, not, say, quaternionic).** The horizontal plane at each height is a copy of $\mathbb{C}$ (not $\mathbb{R}^2$ as a bare Euclidean plane): it has a natural complex structure inherited from the identification $\mathbb{H}^3 \subset \mathbb{C} \times \mathbb{R}_{>0}$. In this complex structure, "scale by $e^{\ell_\gamma}$ and rotate by $\theta_\gamma$" is precisely multiplication by the complex number $e^{\ell_\gamma}\,e^{i\theta_\gamma} = e^{L_\gamma}$. So $L_\gamma$ is not two real parameters glued arbitrarily; it is the single complex eigenvalue of $\tau$'s action on the horizontal complex line, chosen so that "$e^{L_\gamma}$" is the actual multiplier.
>
> **Step 6 (translation into the class-mass answer).** The strip integral $\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t, w, \tau^m w)\,d\operatorname{vol}_{\mathbb{H}^3}(w)$ evaluated in [[Lemma - Hyperbolic 3-Space Strip Integral|§7.2's strip lemma]] produces the factor $|e^L - 1|^2$ in its denominator (with $L = m L_\gamma$). This factor arose from the identity $|e^L - 1|^2 = 2 e^{m\ell_\gamma}(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))$ used to simplify the distance formula $\cosh u = \cosh(m\ell_\gamma) + \frac{|e^L - 1|^2 r^2}{2 e^{m\ell_\gamma} y^2}$. So the appearance of $L$ in the final answer $\mu_X(C_X(\gamma^m)) = 1/(m |e^{mL_\gamma} - 1|^2)$ is dictated by the geometry of the axis action on horizontal planes, not by a formal analytic continuation. At $\theta_\gamma = 0$: $|e^{m\ell_\gamma} - 1|^2 = (e^{m\ell_\gamma} - 1)^2$ recovers the surface answer squared, the "square" coming from the extra transverse dimension.
>
> $\square$

---

# Where the paper uses this

The complex length is introduced at the opening of [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7]] and shows up in every downstream formula:

- [[Thm - Homotopy Decomposition for 3-Manifolds|Theorem 7.1]] states the class-mass integral over $\mathcal{F}_\tau$ using the loxodromic standard form $\tau(z, y) = (e^{L_\gamma} z, e^{\ell_\gamma} y)$.
- [[Lemma - Hyperbolic 3-Space Strip Integral|the §7.2 strip integral]] produces the factor $|e^L - 1|^2$ in the denominator.
- [[Thm - Mass of Subordinate Loops on 3-Manifolds|Theorem 7.2]] carries $|e^L - 1|^2$ through the subordinate formula.
- [[Cor - Brownian Mass on 3-Manifolds|Corollary 7.3]] states the closed-form Brownian mass as $1/(m |e^{mL_\gamma} - 1|^2)$; the paper's cross-check with the surface case at $\theta_\gamma = 0$ turns on precisely the $L_\gamma = \ell_\gamma$ reduction.
- The paper's pointer that §§4 and 6 lift to 3-manifolds is stated as "$\ell_\gamma \to L_\gamma$ and $\sinh^2 \to |e^L - 1|^2$ throughout" — again turning on $L_\gamma$ as the right variable.

---
type: definition
subject: special-relativity
prereqs:
  - "Def - Submanifolds of Spacetime"
  - "Def - The Hodge Star"
  - "Def - The Levi-Civita Tensor"
  - "Def - Metric Duality and Index Manipulation"
  - "Def - Alternate Forms and the Exterior Product"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector has positive norm-squared. Spacetime is $\mathscr{E}$ with displacement space $E$; $\mathscr{V}$ is a submanifold (see [[Def - Submanifolds of Spacetime]]). The metric dual of a vector $X$ is the 1-form $\underline{X}$, $X_\mu = \eta_{\mu\nu}X^\nu$ (see [[Def - Metric Duality and Index Manipulation]]); $\|X\|_g = \sqrt{|X\cdot X|}$ is its norm. The Levi-Civita tensor is $\epsilon$ ([[Def - The Levi-Civita Tensor]]) and the Hodge star is $\star$ ([[Def - The Hodge Star]]). A unit normal to a hypersurface is $\vec{n}$, a unit tangent to a curve is $\vec{u}$, and $(\vec{n},\vec{s})$ is an orthonormal normal pair of a 2-surface. Full registry on [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem]].

This is a compound page: it defines five interlocking notions — the **volume element** of a hypersurface, the **area element** of a surface, the **length element** of a curve, the **integral of a scalar field** over a submanifold, and the **flux** of a vector field through a hypersurface — because each lower-dimensional measure is built by the same Hodge-star recipe and the flux is the integral built from the volume element, so none is fully usable without the others.

> [!warning] Convention
> Gourgoulhon uses signature $(-,+,+,+)$, in which a future-directed unit normal to a spacelike hypersurface is *timelike with $\vec{n}\cdot\vec{n} = -1$* and a unit timelike tangent (four-velocity) has $\vec{u}\cdot\vec{u} = -1$. In our mostly-minus convention these flip: a future timelike unit normal has $\vec{n}\cdot\vec{n} = +1$, a unit timelike tangent has $\vec{u}\cdot\vec{u} = +1$, and a unit spacelike vector has norm-squared $-1$. The structural formulas $\epsilon_{\mathscr{V}} = \star\underline{n}$, $\star(\underline{n}\wedge\underline{s})$, $\pm\underline{u}$, and $\Phi = \int\star\underline{v}$ are convention-robust; only the explicit signs of normalisations change. Watch every $\vec{n}\cdot\vec{n}$, $\vec{s}\cdot\vec{s}$, $\vec{u}\cdot\vec{u}$ in a transcribed formula.

---

# Axiom Motivation

We can integrate a $p$-form over a $p$-submanifold ([[Def - Integration of Forms and the Volume Element|the previous page]]), but that is not yet enough for physics. Physics wants to integrate *scalars*: a charge density over a slice to get total charge, an energy density to get total energy, the constant function $1$ over a curve to get its length. A scalar is a $0$-form, and you cannot integrate a $0$-form over a $p$-dimensional region directly — there is a dimension mismatch. The fix is to manufacture, on each submanifold, a canonical $p$-form to multiply the scalar by: the **volume element** $\epsilon_{\mathscr{V}}$. Then $\int_{\mathscr{V}} f\,\epsilon_{\mathscr{V}}$ is a legitimate $p$-form integral, and it is the "integral of the scalar $f$ over $\mathscr{V}$". The whole content of this page is the construction of $\epsilon_{\mathscr{V}}$ for hypersurfaces, surfaces, and curves, and the recognition that it is always a Hodge dual.

What should $\epsilon_{\mathscr{V}}$ be? It should measure $p$-dimensional volume the way $\epsilon$ measures four-volume. The trick is to *complete* a $p$-box to a four-box and use $\epsilon$. Take a hypersurface ($p = 3$) with unit normal $\vec{n}$. Given an infinitesimal parallelepiped in the hypersurface spanned by $\mathrm{d}\vec{\ell}_1, \mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3$, erect on it the four-box that adds the unit normal $\vec{n}$. Its four-volume is $\epsilon(\vec{n}, \mathrm{d}\vec{\ell}_1, \mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3)$, and because $\vec{n}$ has unit length and is perpendicular to the base, this four-volume *equals* the three-volume of the base. So the natural three-volume element is $\epsilon_{\mathscr{V}} := \epsilon(\vec{n}, \cdot, \cdot, \cdot)$ — feed $\vec{n}$ into the first slot of $\epsilon$, leave three slots open, and you have a 3-form on the hypersurface. The same move with the *two* unit normals $(\vec{n}, \vec{s})$ of a 2-surface gives the area 2-form $\epsilon(\vec{n}, \vec{s}, \cdot, \cdot)$, and with the *three* normals $(\vec{n}_1,\vec{n}_2,\vec{n}_3)$ of a curve gives the length 1-form $\epsilon(\vec{n}_1, \vec{n}_2, \vec{n}_3, \cdot)$. The recipe is uniform: feed the unit normals into $\epsilon$, leave $p$ slots open.

Why is the result the Hodge dual? This is the elegant payoff. The Hodge star is *defined* to be the operation that, on a 1-form $\underline{n}$, produces the 3-form $\star\underline{n}$ with components $(\star\underline{n})_{\alpha\beta\gamma} = n^\mu\epsilon_{\mu\alpha\beta\gamma}$ — which is exactly $\epsilon(\vec{n}, \cdot, \cdot, \cdot)$. So $\epsilon_{\mathscr{V}} = \star\underline{n}$ for a hypersurface is not a coincidence but the very definition of the Hodge star applied to the normal. Likewise $\epsilon_{\mathscr{V}} = \star(\underline{n}\wedge\underline{s})$ for a 2-surface (the Hodge dual of the wedge of the two normal 1-forms) and $\epsilon_{\mathscr{V}} = \pm\underline{u}$ for a curve (the Hodge dual of the three-normal wedge collapses, by the unit-tangent normalisation, to $\pm$ the tangent's own 1-form). The volume element of a $p$-submanifold is the Hodge dual of the wedge of its unit normals — one statement covering every codimension.

What requires the normal to be a *unit* normal, and what goes wrong without it? The completion-to-a-four-box argument uses $\|\vec{n}\| = 1$ crucially: only then does the four-volume of the erected box equal the $p$-volume of the base. If $\vec{n}$ were not normalised, $\epsilon(\vec{n}, \cdot, \cdot, \cdot)$ would scale by $\|\vec{n}\|$ and overcount or undercount the base volume. This forces $\vec{n} = \vec{m}/\|\vec{m}\|_g$, where $\vec{m}$ is *any* normal (e.g. the metric dual of the gradient of the defining coordinate). And it exposes a hole: on a **null** hypersurface the normal is null, $\vec{m}\cdot\vec{m} = 0$, so $\|\vec{m}\|_g = 0$ and the normalisation $\vec{n} = \vec{m}/\|\vec{m}\|_g$ is undefined — the whole construction breaks. The unit-normal recipe is legal exactly for spacelike and timelike hypersurfaces, and null hypersurfaces need a separate (degenerate) treatment. This is not a technical nuisance to be waved away; it is the reason integrating fluxes across horizons in general relativity is genuinely harder.

Finally, the flux. The "amount of a vector field $\vec{v}$ crossing a hypersurface" is, elementarily, $\int \vec{v}\cdot\vec{n}\,\mathrm{d}V$ — the normal component of $\vec{v}$ integrated against the volume element. But the *true name* of this quantity is the integral of a Hodge dual: $\Phi_{\mathscr{V}}(\vec{v}) = \int_{\mathscr{V}}\star\underline{v}$. The reason to prefer this form is decisive: $\star\underline{v}$ is a 3-form, so its integral is exactly the kind of object Stokes' theorem acts on, and *every* conservation law in the chapter is one application of $\mathrm{d}$ away from a flux. A flux written as "$\vec{v}\cdot\vec{n}\,\mathrm{d}V$" hides this; a flux written as "$\int\star\underline{v}$" wears it on its face. The two are equal — substituting $\vec{v} = v^0\vec{n} + v^i\vec{e}_i$ into $\epsilon(\vec{n},\cdot,\cdot,\cdot)$ and using antisymmetry collapses $\vec{v}\cdot\vec{n}\,\epsilon_{\mathscr{V}}$ to $\star\underline{v}$ — but only one of them generalises and only one of them is Stokes-ready.

---

# The Definition

Throughout, $\mathscr{V}$ is an oriented submanifold of $\mathscr{E}$ and $\epsilon$ is the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]].

**Normal to a hypersurface.** Let $\mathscr{V}$ be a hypersurface ($p=3$), locally $x^0 = \mathrm{const}$ in adapted coordinates. The 1-form $\nabla x^0 = \mathrm{d}x^0$ vanishes on every tangent vector; its metric dual is a vector $\vec{m}$, and
$$
\vec{v}\ \text{tangent to}\ \mathscr{V} \;\Longleftrightarrow\; \vec{m}\cdot\vec{v} = 0 .
$$
$\vec{m}$ is **normal** to $\mathscr{V}$. The hypersurface is **spacelike** if $\vec{m}$ is timelike, **timelike** if $\vec{m}$ is spacelike, and **null** if $\vec{m}$ is null (in which case $\vec{m}$ is simultaneously normal and tangent, $\vec{m}\cdot\vec{m}=0$).

**Volume element of a hypersurface.** Assume $\mathscr{V}$ is spacelike or timelike, so $\vec{m}\cdot\vec{m}\ne 0$. The **unit normal** is
$$
\vec{n} := \frac{\vec{m}}{\|\vec{m}\|_g}, \qquad \vec{n}\cdot\vec{n} = \pm 1 \ \ (+1\ \text{if}\ \mathscr{V}\ \text{spacelike},\ -1\ \text{if timelike}),
$$
taken future-directed if $\mathscr{V}$ is spacelike. The **volume-element 3-form** of $\mathscr{V}$ is
$$
\epsilon_{\mathscr{V}} := \epsilon(\vec{n}, \cdot, \cdot, \cdot) = \star\underline{n},
$$
the Hodge dual of the normal's 1-form, with components $(\epsilon_{\mathscr{V}})_{\alpha\beta\gamma} = n^\mu\epsilon_{\mu\alpha\beta\gamma}$. In adapted coordinates the volume of the elementary parallelepiped is
$$
\mathrm{d}V = \epsilon_{\mathscr{V}}(\mathrm{d}\vec{\ell}_1, \mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3) = n^0\sqrt{|g|}\,\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3 .
$$

**Area element of a surface.** Let $\mathscr{V}$ be a spacelike 2-surface ($p=2$): at each point $E = \Pi\oplus\Pi^\perp$, with $\Pi$ the tangent plane (two spacelike directions) and $\Pi^\perp$ a timelike plane carrying an orthonormal pair $(\vec{n}, \vec{s})$, $\vec{n}\cdot\vec{n}=+1$ (timelike), $\vec{s}\cdot\vec{s}=-1$ (spacelike), $\vec{n}\cdot\vec{s}=0$. The **area-element 2-form** is
$$
\epsilon_{\mathscr{V}} := \epsilon(\vec{n}, \vec{s}, \cdot, \cdot) = \star(\underline{n}\wedge\underline{s}),
$$
the Hodge dual of the wedge of the two normal 1-forms, with components $(\epsilon_{\mathscr{V}})_{\alpha\beta} = n^\mu s^\nu\epsilon_{\mu\nu\alpha\beta}$. It is independent of the choice of orthonormal pair in $\Pi^\perp$ with the same orientation (a boost in $\Pi^\perp$ leaves $\epsilon(\vec{n},\vec{s},\cdot,\cdot)$ unchanged, since $\cosh^2\psi - \sinh^2\psi = 1$). The area of the elementary parallelogram is $\mathrm{d}S = \epsilon_{\mathscr{V}}(\mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3) = (n^0 s^1 - n^1 s^0)\sqrt{|g|}\,\mathrm{d}x^2\mathrm{d}x^3$.

**Length element of a curve.** Let $\mathscr{V}$ be a curve ($p=1$), timelike or spacelike (not null), with unit tangent $\vec{u}$ sharing its orientation, $\vec{u}\cdot\vec{u} = -1$ (timelike, then $\vec{u}$ is the four-velocity of a particle with worldline $\mathscr{V}$) or $+1$ (spacelike). Completing to an orthonormal basis $(\vec{n}_1, \vec{n}_2, \vec{n}_3, \vec{u})$, the **length-element 1-form** is
$$
\epsilon_{\mathscr{V}} := \epsilon(\vec{n}_1, \vec{n}_2, \vec{n}_3, \cdot) = \pm\underline{u},
$$
($+$ if $\vec{u}$ spacelike, $-$ if timelike), the metric dual of the unit tangent up to sign. For an infinitesimal displacement $\mathrm{d}\vec{\ell}$ along the curve, oriented with $\vec{u}$,
$$
\mathrm{d}\ell = \langle\epsilon_{\mathscr{V}}, \mathrm{d}\vec{\ell}\rangle = \|\mathrm{d}\vec{\ell}\|_g ,
$$
so the length induced by $\epsilon$ coincides with the metric length.

**Integral of a scalar field.** For a submanifold $\mathscr{V}$ of dimension $p$ with volume element $\epsilon_{\mathscr{V}}$ (and $\epsilon_{\mathscr{V}} := \epsilon$ for $p=4$), the **integral of a scalar field $f$ over $\mathscr{V}$** is
$$
\mathrm{int}_{\mathscr{V}}(f) := \int_{\mathscr{V}} f\,\epsilon_{\mathscr{V}}.
$$
Explicitly, $\mathrm{int}_{\mathscr{V}}(f) = \int f\,\sqrt{|g|}\,\mathrm{d}^4x$ ($p=4$), $\int f\,n^0\sqrt{|g|}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$ ($p=3$), $\int f\,(n^0s^1-n^1s^0)\sqrt{|g|}\,\mathrm{d}x^2\mathrm{d}x^3$ ($p=2$), $\int f\,\mathrm{d}\ell$ ($p=1$). With $f=1$ and $\mathscr{V}$ compact this gives the four-volume, volume, area, or length of $\mathscr{V}$.

**Flux of a vector field.** Let $\mathscr{V}$ be a spacelike or timelike hypersurface with unit normal $\vec{n}$, oriented so that $\epsilon_{\mathscr{V}} = \epsilon(\vec{n},\cdot,\cdot,\cdot)$ is compatible with the orientation. The **flux of a vector field $\vec{v}$ through $\mathscr{V}$** is
$$
\Phi_{\mathscr{V}}(\vec{v}) := \pm\int_{\mathscr{V}} \vec{v}\cdot\vec{n}\,\,\mathrm{d}V = \int_{\mathscr{V}} \star\underline{v},
$$
the sign being $+$ if $\vec{n}$ is spacelike and $-$ if $\vec{n}$ is timelike, and $\star\underline{v}$ the Hodge dual of the metric dual 1-form $\underline{v}$. A vector field tangent to $\mathscr{V}$ everywhere has zero flux. For a spacelike 2-surface, where the normal is not unique, the **flux of a 2-form $A$** is defined by the analogous formula $\Phi_{\mathscr{V}}(A) := \int_{\mathscr{V}}\star A$.

---

# Categorical / Structural Definition

The volume element $\epsilon_{\mathscr{V}}$ is the image of the submanifold's co-orientation under the Hodge isomorphism, and the integral of a scalar is the composite of this with the form-integration pairing. On an inner-product space $E$ with volume form $\epsilon$, the **Hodge star** $\star:\Lambda^k E^* \to \Lambda^{n-k} E^*$ is the linear isomorphism characterised by $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle\,\epsilon$. A $p$-submanifold has at each point a *co-oriented normal space* of dimension $n-p$, encoded by the decomposable $(n-p)$-form that is the wedge of its unit normal 1-forms; applying $\star$ to this $(n-p)$-form lands in $\Lambda^p E^*$, and *that* is the volume element $\epsilon_{\mathscr{V}}$. So the three constructions — $\star\underline{n}$, $\star(\underline{n}\wedge\underline{s})$, $\pm\underline{u} = \star(\underline{n}_1\wedge\underline{n}_2\wedge\underline{n}_3)$ — are one construction: Hodge-star the wedge of the unit normals.

This makes precise why the area element is independent of the chosen normal pair: the wedge $\underline{n}\wedge\underline{s}$ depends only on the *oriented plane* the pair spans, not on the pair, because any orientation-preserving basis change of the plane multiplies the wedge by a positive determinant — and for an orthonormal pair related by a boost that determinant is $\cosh^2\psi - \sinh^2\psi = 1$. The Hodge star then carries this well-defined normal-space datum to a well-defined volume element. The flux is the further composite $\vec{v}\mapsto\underline{v}\mapsto\star\underline{v}\mapsto\int_{\mathscr{V}}\star\underline{v}$: metric-dualise, Hodge-star, integrate — the metric entering at the first two steps, the integration pairing (metric-free) at the last.

---

# Relate to Other Fields / Compression

The hypersurface volume element $\star\underline{n}$ is, when $\vec{n}$ is an observer's four-velocity, exactly the **observer's volume 3-form** $\epsilon_{\vec u}$ used to define the cross product in the local rest space ([[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]]) — integration over a spatial slice is integration over an observer's "space at an instant". The length element $\|\mathrm{d}\vec{\ell}\|_g$ of a timelike curve is the **proper time** of [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]]: integrating $1$ along a worldline with $\epsilon_{\mathscr{V}} = -\underline{u}$ gives the elapsed proper time, so proper time is the length-integral of this page. The flux-as-Hodge-dual construction is the special-relativistic instance of the general fact that, on an oriented Riemannian manifold, the flux of a vector field through a hypersurface is the integral of the contraction $\iota_{\vec v}\,\mathrm{vol}$, which equals $\star\underline{v}$ — see [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]] for the Hodge-star machinery.

**True name:** the volume element of a submanifold is "the Hodge dual of the wedge of its unit normals", and a flux is "the integral of a Hodge dual". The operational content is that you never compute a lower-dimensional measure by ad hoc parametrisation — you find the unit normal(s), dualise and Hodge-star, and integrate. For a flux specifically, recasting $\int\vec{v}\cdot\vec{n}\,\mathrm{d}V$ as $\int\star\underline{v}$ is the move that makes the flux Stokes-ready, which is why it is worth doing even when the elementary form would compute the number.

---

# Examples / Corollaries

**Is an instance — the area element of a round sphere.** For the sphere $t = 0$, $r = R$ in spherical coordinates, the normal pair is $\vec{n} = \vec{e}_0 = (1,0,0,0)$ (timelike, future) and $\vec{s} = \vec{e}_r/\|\vec{e}_r\| = (0,1,0,0)$ (spacelike), so $n^0 s^1 - n^1 s^0 = 1$. With $\sqrt{|g|} = r^2\sin\theta = R^2\sin\theta$, the area element is $\mathrm{d}S = R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$, recovering the elementary sphere measure, and $\int\mathrm{d}S = 4\pi R^2$.

**Is an instance — the volume element of a spatial slice.** For the hyperplane $t = 0$ with future timelike normal $\vec{n} = \vec{e}_0$, $n^0 = 1$, in inertial Cartesian coordinates $\sqrt{|g|} = 1$, so $\mathrm{d}V = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$. Integrating a charge density $\rho$ over the slice gives the total charge $\int\rho\,\mathrm{d}V$ — the elementary expression, here derived as $\int\rho\,\star\underline{n}$.

**Is an instance — flux through a constant-time slice.** For a vector field $\vec{v}$ and the slice $\Sigma$ with future timelike unit normal $\vec{n} = \vec{e}_0$ (sign $-$ in the flux formula), the inner product is $\vec{v}\cdot\vec{n} = v^\mu n_\mu = v^0 n_0 = v^0$ (since $n_0 = \eta_{00}n^0 = 1$), so $\Phi_\Sigma(\vec{v}) = -\int_\Sigma v^0\,\mathrm{d}V$. The flux is, up to the orientation sign, the integral of the time component — the "density" $v^0$ being transported across the instant. For a current $\vec{v} = J$ this is (minus) the total charge $\int_\Sigma J^0\,\mathrm{d}V = \int_\Sigma\rho\,\mathrm{d}V$; the overall sign is a convention fixed by the choice of orientation, and is chosen so that "charge in minus charge out" comes out positive in the conservation argument.

**Is an instance — proper time as a length integral.** Along a timelike worldline with four-velocity $\vec{u}$ ($\vec{u}\cdot\vec{u}=+1$ here), $\epsilon_{\mathscr{V}} = -\underline{u}$ and $\mathrm{d}\ell = \|\mathrm{d}\vec{\ell}\|_g = \sqrt{\mathrm{d}\vec{\ell}\cdot\mathrm{d}\vec{\ell}}$, which integrated is the elapsed proper time $\tau = \int\mathrm{d}\ell$. The length element of this page *is* the proper-time element of relativistic kinematics.

**Is NOT an instance — a null hypersurface.** The future light cone $u = 0$ (in null coordinates) is a hypersurface, but its normal $\vec{m}$ is null, $\vec{m}\cdot\vec{m}=0$, so $\|\vec{m}\|_g = 0$ and the unit normal $\vec{n} = \vec{m}/\|\vec{m}\|_g$ is *undefined*. The volume-element construction $\star\underline{n}$ does not apply, and integrating over a null hypersurface requires choosing a (non-canonical) null normal and an auxiliary transverse vector — a genuinely different, degenerate construction. Any attempt to use $\star\underline{n}$ on a light cone is a category error.

**Is NOT an instance — a flux with a tangent field.** If $\vec{v}$ is everywhere tangent to the hypersurface $\mathscr{V}$, then $\vec{v}\cdot\vec{n} = 0$ pointwise, so $\Phi_{\mathscr{V}}(\vec{v}) = 0$. A field that "runs along" a surface has no flux *through* it — flux measures only the crossing (normal) component. This is the calibration that the construction measures the right thing.

**Corollary — the volume of a hypersurface is the flux of its unit normal.** Taking $\vec{v} = \vec{n}$ in the flux formula and using $\vec{n}\cdot\vec{n} = \pm 1$, $\Phi_{\mathscr{V}}(\vec{n}) = \pm\int_{\mathscr{V}}(\pm 1)\,\mathrm{d}V = \int_{\mathscr{V}}\mathrm{d}V = \mathrm{vol}(\mathscr{V})$, equivalently $\int_{\mathscr{V}}\star\underline{n} = \int_{\mathscr{V}}\epsilon_{\mathscr{V}}$. The volume of a slice is the flux of the normal through it — a clean consistency check linking the flux formula to $\epsilon_{\mathscr{V}} = \star\underline{n}$.

**Calibration check.** If you have understood these definitions you should be able to: (i) write the unit normal and $\sqrt{|g|}$ for the hyperplane $t=0$ in inertial coordinates and confirm $\mathrm{d}V = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$; (ii) state why a vector tangent to a hypersurface has zero flux through it; and (iii) explain why the unit-normal construction fails on a null hypersurface, by pointing to the step that divides by $\|\vec{m}\|_g = 0$.

---

# Unlocked by This

> [!tip] The Conserved Charge as a Slice Integral *(from Noether's Theorem and Field Theory)*
> A flux integral $Q_\Sigma = \int_\Sigma\star\underline{J}$ of a conserved current through a spacelike slice is the prototype of a **Noether charge**. Whenever a continuous symmetry of an action leaves it invariant, Noether's theorem produces a current $J$ with $\nabla\cdot J = 0$, and the corresponding conserved quantity is exactly the flux of $J$ through a spacelike hypersurface — total electric charge from the phase symmetry of a charged field, total energy and momentum from spacetime-translation symmetry, total angular momentum from Lorentz symmetry. The construction here, integrating the 3-form $\star\underline{J}$ over a slice, is what makes "the total charge at time $t$" a well-defined geometric object, and the 4D Gauss theorem ([[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)]]) is what makes it independent of the slice.

> [!tip] Surface Gravity and Horizon Integrals *(from Black-Hole Thermodynamics)*
> The breakdown of the unit-normal construction on **null hypersurfaces** flagged above is exactly the technical heart of black-hole physics. A black-hole **horizon** is a null hypersurface, and because its normal is null and simultaneously tangent, the volume element and flux integrals must be built by a degenerate procedure using a null normal $\vec{k}$ and a transverse null vector. The quantities that emerge — the **surface gravity** $\kappa$, the horizon **area** (which obeys an area-increase theorem playing the role of entropy), and the flux of energy through the horizon — are the ingredients of the laws of black-hole mechanics and of the Hawking temperature $T = \kappa/2\pi$. The fact that this page's clean apparatus fails on null surfaces is precisely why horizon thermodynamics required new geometric techniques.

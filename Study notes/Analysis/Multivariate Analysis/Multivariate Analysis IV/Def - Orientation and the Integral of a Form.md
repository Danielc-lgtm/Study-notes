---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - Differential Form"
  - "Def - The Wedge Product"
  - "Def - Pullback of a Differential Form"
  - "Def - Submanifold of Euclidean Space"
  - "Thm - The Change of Variables Formula"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $M$ is a smooth $k$-dimensional surface ([[Def - Submanifold of Euclidean Space|submanifold]]) in $\mathbb{R}^N$, and $\Omega, O$ are open subsets of $\mathbb{R}^k$ or $\mathbb{R}^n$. A chart (coordinate patch) is a parametrization $\varphi : O \to U \subseteq M$; the transition map between two charts is $F = \psi^{-1}\circ\varphi$. A nowhere-vanishing top-degree form is $\omega$; the integral of a $k$-form $\alpha$ over $M$ is $\int_M\alpha$. The full symbol registry is on [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

---

# Axiom Motivation

We have differential forms — built to be invariant integrands — and the pullback, which transports them to flat parameter domains. We now want to actually *integrate* a $k$-form over a $k$-dimensional surface. The recipe suggests itself: parametrize the surface by a chart $\varphi : O \to M$, pull the form back, and integrate the resulting form over the flat domain $O$. The motivation for this definition page is to discover the *one extra piece of data* the recipe needs to be well-posed — and that piece of data is an orientation.

Here is the difficulty. The integral $\int_M\alpha$ should not depend on which chart we used. Suppose two charts $\varphi$ and $\psi$ cover the same patch; they are related by a transition diffeomorphism $F = \psi^{-1}\circ\varphi$. The change-of-variables identity for forms (a consequence of the [[Def - Pullback of a Differential Form|pullback]]'s Jacobian property) says $\int_O\varphi^*\alpha = \int_O F^*(\psi^*\alpha)$, and pulling a top-degree form through $F$ multiplies by $\det DF$. But the *integral* of a function, in the ordinary Riemann sense, transforms by $|\det DF|$ — the absolute value. So the form's integral picks up $\det DF$ while the change-of-variables formula expects $|\det DF|$. These agree only when $\det DF > 0$. If the transition map has negative Jacobian, the two charts give answers of *opposite sign*.

This is the crux. Integration of a $k$-form is intrinsically *signed* — the wedge product carries signs, the determinant carries a sign, and there is no way to wash the sign out. So the integral of a form is well-defined only if we restrict to charts whose transition maps all have positive Jacobian. A consistent such choice of charts — equivalently, a consistent choice of "positive direction" for the top-degree forms at every point — is exactly what an **orientation** is. The definition of orientation is reverse-engineered from the single requirement: *make $\int_M\alpha$ independent of the chart, given that the pullback contributes a signed Jacobian*.

Why phrase an orientation as an equivalence class of nowhere-vanishing top-degree forms, rather than, say, a choice of "positive basis" at each point? Because the two are the same data, and the form version is cleaner. A nowhere-vanishing $k$-form $\omega$ on $M$ assigns a nonzero number to each ordered $k$-tuple of tangent vectors; calling a tuple "positively oriented" when $\omega$ gives it a positive value is exactly a consistent choice of positive basis. Two such forms define the *same* orientation when one is a positive-function multiple of the other — because then they agree on which tuples are positive. So an orientation *is* an equivalence class of nowhere-vanishing top-degree forms. This phrasing makes orientation-preservation of a map a one-line condition ($\psi^*\sigma$ is positive whenever $\sigma$ is) and connects directly to the integral.

What breaks if we ignore orientation? Two things, of different severity. First, mild: on an orientable surface, integrating with an inconsistent set of charts gives a sign-scrambled, meaningless answer — the integral is simply not defined until an orientation is fixed. Second, severe: some surfaces admit *no* orientation at all. The Möbius strip and the projective plane $\mathbb{P}^2$ have no nowhere-vanishing top-degree form — every candidate $\omega$ is forced to vanish somewhere as you transport it around a non-orientation-preserving loop. On such a surface $\int_M\alpha$ for a top-degree form $\alpha$ is *undefined*, full stop. Orientability is a genuine topological hypothesis, not a technicality, and the boundary orientation in [[Thm - The General Stokes Theorem|Stokes' theorem]] must be the *induced* one for the theorem to hold with the right sign.

---

# The Definition

Let $M$ be a smooth $k$-dimensional surface in $\mathbb{R}^N$.

**Orientation.** An **orientation** on $M$ is an equivalence class of nowhere-vanishing $k$-forms on $M$, where two such forms $\omega_1, \omega_2 \in \Lambda^k(M)$ are equivalent if $\omega_1 = a(x)\,\omega_2$ for some everywhere-positive smooth function $a$. A surface admitting such a form is called **orientable**; a surface together with a choice of orientation is **oriented**. The forms in the chosen class are called **positive**. For $M = \mathbb{R}^k$ the standard orientation is the class of $dx_1\wedge\cdots\wedge dx_k$.

A smooth map $\psi : S \to M$ between oriented $k$-surfaces **preserves orientation** if $\psi^*\sigma$ is a positive form on $S$ whenever $\sigma$ is a positive form on $M$. For two charts $\varphi : O \to U$ and $\psi : \Omega \to U$ covering the same patch, the transition map $F = \psi^{-1}\circ\varphi$ preserves orientation if and only if $\det DF > 0$ throughout.

**Integral of a top-degree form on an open subset of $\mathbb{R}^n$.** If $\alpha = A(x)\,dx_1\wedge\cdots\wedge dx_n$ is an $n$-form with compact support in an open set $\Omega \subseteq \mathbb{R}^n$ carrying the standard orientation, then
$$\int_\Omega\alpha := \int_\Omega A(x)\,dV(x),$$
the right-hand side being the ordinary [[Def - The Riemann Integral in Several Variables|Riemann integral]].

**Integral of a $k$-form over an oriented $k$-surface.** Let $M$ be an oriented $k$-surface and $\alpha$ a compactly supported $k$-form on $M$. If $\alpha$ is supported in a single patch $U$ with an orientation-preserving chart $\varphi : O \to U$ ($O \subseteq \mathbb{R}^k$ with the standard orientation), define
$$\int_M\alpha := \int_O \varphi^*\alpha.$$
For general $\alpha$, write $\alpha = \sum_i\alpha_i$ with each $\alpha_i$ supported in one patch (using a partition of unity) and set $\int_M\alpha = \sum_i\int_M\alpha_i$.

**Well-definedness.** This integral is independent of the choice of orientation-preserving charts. If $\varphi : O \to U$ and $\psi : \Omega \to U$ are two such charts and $F = \psi^{-1}\circ\varphi$, then since any form $\alpha$ satisfies $\varphi^*\alpha = F^*(\psi^*\alpha)$, and $F$ is an orientation-preserving diffeomorphism, the [[Thm - The Change of Variables Formula|change of variables formula]] gives $\int_O\varphi^*\alpha = \int_\Omega\psi^*\alpha$.

---

# Categorical Definition

An orientation can be described as a choice of generator for a rank-one object. At each point $x \in M$, the top exterior power $\Lambda^k(T_x^*M)$ of the cotangent space is a one-dimensional vector space; removing the zero element leaves two connected components ("rays"), and a pointwise orientation is a choice of one ray. The bundle of these one-dimensional spaces is the **orientation line bundle**, and an orientation of $M$ is a nowhere-vanishing global section of it — equivalently, a trivialization of that line bundle. The surface is orientable exactly when the orientation line bundle is trivial; the Möbius strip is the standard example where it is not, because transporting a ray once around the core circle returns it flipped.

The integral $\int_M : \Lambda^k_c(M) \to \mathbb{R}$ on a closed oriented $k$-surface (compactly supported $k$-forms to numbers) is, in the categorical picture, a linear functional that descends to de Rham cohomology: by [[Thm - The General Stokes Theorem|Stokes' theorem]], $\int_M$ kills exact forms, so it factors through $H^k_{\mathrm{dR}}(M)$. Integration is therefore the canonical *pairing* between de Rham cohomology and the homology class of $M$ — a pairing that is the analytic content of de Rham's theorem.

---

# Relate to Other Fields / Compression

An orientation is the global, surface-level version of the elementary linear-algebra notion "a basis is positively or negatively oriented". In $\mathbb{R}^n$, two ordered bases have the same orientation if the change-of-basis matrix has positive determinant; this partitions all ordered bases into two classes, and choosing one class is orienting $\mathbb{R}^n$. The content of this definition is that the same dichotomy can be made *consistently across a whole surface* — and that, surprisingly, this is not always possible. The obstruction is exactly a holonomy: transport a positive basis around a loop, and on a non-orientable surface it can come back negative.

The signed nature of the integral of a form is the precise reason forms, and not measures, are the objects of this theory. A measure assigns non-negative mass; its integral transforms by $|\det DF|$. A top-degree form's integral transforms by $\det DF$, with the sign. The compression achieved is that the *single* signed object — the form — simultaneously encodes the measure (its absolute value) and the orientation (its sign). This is why the change-of-variables formula for forms (with $\det DF$) is algebraically cleaner than the one for measures (with $|\det DF|$): the form carries the orientation data that the measure had to discard.

---

# Examples / Corollaries

**Is an instance — $\mathbb{R}^n$ with the standard orientation.** The form $dx_1\wedge\cdots\wedge dx_n$ is nowhere-vanishing, so $\mathbb{R}^n$ is orientable, and its standard orientation is the class of this form. Integrating an $n$-form $A\,dx_1\wedge\cdots\wedge dx_n$ over $\mathbb{R}^n$ is just integrating the function $A$ — the simplest case, and the one all others reduce to via pullback.

**Is an instance — the sphere $S^2$.** The unit sphere $S^2 \subseteq \mathbb{R}^3$ is orientable: the $2$-form $\omega = x\,dy\wedge dz + y\,dz\wedge dx + z\,dx\wedge dy$, restricted to $S^2$, is nowhere zero (it is the "area form" pointing along the outward normal). A choice of outward normal *is* a choice of orientation, and the integral of a $2$-form over $S^2$ is then well-defined. Reversing to the inward normal flips the orientation and negates every integral.

**Is an instance — orientation of the boundary.** If $M$ is an oriented $k$-surface with boundary, $\partial M$ inherits a canonical orientation, fixed by the convention: at a boundary point, an "outward-pointing vector first, followed by a positive frame of $\partial M$" must be a positive frame of $M$. This induced orientation is exactly what makes the signs in [[Thm - The General Stokes Theorem|Stokes' theorem]] come out right, and it is the reason the right-hand side of Stokes is not ambiguous.

**Is NOT an instance — the Möbius strip.** The Möbius strip admits no nowhere-vanishing $2$-form: any candidate, transported once around the central loop, returns with its sign reversed and must therefore pass through zero. The Möbius strip is *not orientable*, and the integral of a $2$-form over it is undefined. This non-example shows orientability is a real hypothesis — there is no way to repair the definition to cover it.

**Is NOT an instance — the projective plane $\mathbb{P}^2$.** Real projective space $\mathbb{P}^n$ is orientable if and only if $n$ is odd; in particular $\mathbb{P}^2$ is non-orientable. So $\int_{\mathbb{P}^2}\alpha$ for a $2$-form $\alpha$ is undefined. The pattern "$\mathbb{P}^n$ orientable iff $n$ odd" comes from whether the antipodal map of the sphere preserves or reverses orientation, which depends on the parity of $n$.

**Corollary — reversing orientation negates the integral.** If $\bar M$ denotes $M$ with the opposite orientation, then $\int_{\bar M}\alpha = -\int_M\alpha$ for every $k$-form $\alpha$. This is immediate: switching orientation switches the sign convention on charts, and the pullback then contributes $-\det DF$. It is the form-integral analogue of $\int_b^a f = -\int_a^b f$.

**Calibration check.** Verify that reversing the parametrization of a curve negates the line integral $\int_\gamma\alpha$; that the standard orientation of $\mathbb{R}^2$ is the class of $dx\wedge dy$ and that $dy\wedge dx$ defines the *opposite* orientation; that a single nowhere-vanishing top-degree form determines a unique orientation; and that the Möbius strip fails to admit one. If you can also explain why the integral needs $\det DF$ rather than $|\det DF|$, you have understood why orientation is needed at all.

---

# Unlocked by This

> [!tip] de Rham's Theorem *(from Algebraic Topology)*
> Because $\int_M$ kills exact forms (by Stokes), integration is a pairing $H^k_{\mathrm{dR}}(M) \times H_k(M) \to \mathbb{R}$ between de Rham cohomology and singular homology. **de Rham's theorem** says this pairing is perfect: the analytically-defined cohomology of forms is isomorphic to the topologically-defined cohomology, and integration is the isomorphism.

> [!tip] Orientability and Characteristic Classes *(from Differential Geometry)*
> The obstruction to orienting a surface is a single $\mathbb{Z}/2$ invariant, the **first Stiefel-Whitney class** $w_1$. A surface is orientable exactly when $w_1$ vanishes. This is the first of the characteristic classes, the cohomology classes that obstruct geometric constructions on bundles.

---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Volume Form"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Density on a Manifold"
tags: [geometry, differential-geometry, integration, orientation]
---

# Notation

This page works on a smooth $n$-manifold $M$ that may or may not be orientable. $\Lambda^k(V^*)$ denotes the alternating covariant $k$-tensors on a vector space $V$ as in [[Differential Geometry VIII — Differential Forms]]. An **orientation** of a chart is the equivalence class of its coordinate frame under "positive determinant of the Jacobian," as in [[Def - Orientation of a Vector Space]]. We write $\mathrm{Or}(V)$ for the set of two orientations of $V$ — a torsor over $\mathbb{Z}/2$. The full notation registry for this topic is on [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

> [!warning] Convention
> Frankel uses the term **pseudoform** consistently throughout his book; the synonyms **twisted form** (de Rham, Bott–Tu) and **odd form** (Schouten, older differential-geometry literature) are all in current use. The term "pseudoscalar" / "pseudovector" in classical physics refers to the same construction in degree $n$ / degree $n-1$. We adopt **pseudoform**.

---

# Axiom Motivation

A volume form on $M^n$ has a problem the moment $M$ is non-orientable: there is no nowhere-vanishing global section of $\Lambda^n T^*M$ at all, so one cannot integrate even a function on the Möbius strip in the natural way. This is awkward, because the Möbius strip is a perfectly concrete object — a $2$-dimensional surface sitting in $\mathbb{R}^3$ — and one can certainly measure its area. The failure is a notational one: the *form* notation is too rigid, not the geometry.

The diagnosis is precise. Under a change of chart with Jacobian $J = \det DF$, a top-degree form $\omega$ transforms by $\omega \mapsto J\omega$. The Riemann integral of the coefficient function transforms by $|J|$. These match when $J > 0$, that is, when transition maps preserve orientation, which is exactly the orientability hypothesis. When the manifold is non-orientable, some transition map has $J < 0$, and along the loop through that transition $\omega$ picks up a global sign change while the integral does not — the form fails to define a consistent integrand.

The fix is to *build the sign change into the object*. A **pseudoform** is the same kind of alternating multilinear object as a form, but it carries an extra slot for an orientation of the tangent space: at each point $p \in M$ a pseudo-$k$-form $\omega$ assigns to every choice of orientation $\mathfrak{o}_p \in \mathrm{Or}(T_pM)$ an alternating $k$-covector $\omega(p, \mathfrak{o}_p) \in \Lambda^k(T_p^*M)$, with the constraint that swapping the orientation negates the result: $\omega(p, -\mathfrak{o}_p) = -\omega(p, \mathfrak{o}_p)$. Under a change of chart, the chart's orientation flips when $J < 0$, and the pseudoform's value flips with it — producing the missing factor of $\mathrm{sgn}(J)$ that converts the form-transformation rule $J$ into the absolute-value rule $|J|$ demanded by the Riemann integral. The integral becomes well-defined.

The construction is the *minimal* fix: it is the smallest deformation of the form notation that restores integrability on a non-orientable manifold. The alternative — densities, which always carry $|\det J|$ in their transformation — is a different and stronger fix, but it loses the algebraic structure of forms (no exterior derivative, no Stokes theorem, no de Rham complex). Pseudoforms keep all of the algebra and add only what is needed.

The motivation for *why* pseudoforms are needed at all bottoms out in three concrete demands. First, **integration without orientation**: one wants a single object whose integral over a non-orientable manifold exists. Second, **classical-physics objects**: many quantities in physics are pseudoscalars ($\vec u \cdot (\vec v \times \vec w)$ is a pseudoscalar — it flips sign under reflections), pseudovectors (angular momentum, magnetic field), or pseudoforms in higher dimensions. The "pseudo" prefix is exactly the orientation-sign-dependence captured by this construction. Third, **the de Rham cohomology of non-orientable manifolds**: Poincaré duality on a closed manifold pairs $H^k(M)$ with $H^{n-k}(M;\mathrm{or})$, where the second factor is the cohomology of pseudoforms; the pseudoform construction is what makes Poincaré duality survive past orientability.

What would break if one tried alternatives. **Dropping the orientation-dependence** and using ordinary forms: integrals on non-orientable manifolds are undefined, full stop. **Using densities instead** ($|\det J|$ transformation law): the exterior derivative is no longer well-defined (densities are not in a graded algebra under $\wedge$), Stokes's theorem has no analogue, and the de Rham complex collapses. **Requiring the orientation to be smooth and globally defined**: that brings back the orientability hypothesis and undoes the whole point. The pseudoform construction is the one that keeps the form-side algebra ($d$, $\wedge$, $\iota_X$, $\mathcal{L}_X$) intact while restoring well-defined integration.

---

# The Definition

A **pseudo-$k$-form** on a smooth $n$-manifold $M$ is a map that assigns to each point $p \in M$ and each orientation $\mathfrak{o}_p$ of the tangent space $T_pM$ an alternating $k$-covector
$$\omega(p, \mathfrak{o}_p) \in \Lambda^k(T_p^*M),$$
satisfying the **orientation-flip rule**
$$\omega(p, -\mathfrak{o}_p) = -\omega(p, \mathfrak{o}_p)$$
and the local smoothness condition that, in any oriented chart $(U, \varphi)$ — equivalently, after fixing $\mathfrak{o}_p$ to be the orientation supplied by the chart at every $p \in U$ — the resulting ordinary $k$-form on $U$ is smooth.

Equivalently, a pseudo-$k$-form is a smooth section of the bundle $\Lambda^k T^*M \otimes \mathcal{O}_M$, where $\mathcal{O}_M$ is the **orientation line bundle**: the rank-$1$ real line bundle whose fiber at $p$ is the $\mathbb{R}$-vector space generated by the two orientations of $T_pM$ modulo the relation $\mathfrak{o}_p + (-\mathfrak{o}_p) = 0$. The orientation line bundle is trivial iff $M$ is orientable, in which case pseudo-$k$-forms reduce to ordinary $k$-forms after a global section of $\mathcal{O}_M$ is chosen.

We write $\Omega^k(M;\mathrm{or})$ or $\widetilde\Omega^k(M)$ for the space of smooth pseudo-$k$-forms on $M$.

**Transformation law in coordinates.** A pseudo-$k$-form is locally represented in a chart by $k$-form coefficients $\omega_I(x)$, $\omega = \sum'_I \omega_I(x)\,dx^I$ — with the convention that this representation is computed *in the chart's orientation*. Under change of chart $\varphi \to \widetilde\varphi$ with Jacobian $J = \det D(\widetilde\varphi\circ\varphi^{-1})$, the coefficient functions transform by
$$\widetilde\omega_I = \mathrm{sgn}(J) \cdot \big[\text{ordinary form pullback}\big],$$
i.e. by the form-pullback rule multiplied by the sign of the Jacobian. The sign factor is exactly what distinguishes pseudoforms from ordinary forms.

**The four standard operations $d$, $\wedge$, $\iota_X$, $\mathcal{L}_X$** all extend to pseudoforms in the obvious way — apply the operation orientation-by-orientation — and they satisfy the same identities as for ordinary forms. Most importantly $d$ takes pseudo-$k$-forms to pseudo-$(k+1)$-forms with $d^2 = 0$, so there is a de Rham complex of pseudoforms.

**Integration.** A compactly supported pseudo-$n$-form on a smooth $n$-manifold $M$ — *no orientability hypothesis required* — has a well-defined integral $\int_M\omega \in \mathbb{R}$: in any chart, pick an orientation of the chart, write the pseudoform as an ordinary $n$-form in that orientation, integrate the coefficient as a Riemann integral, and patch via partition of unity. The orientation-flip rule of the pseudoform exactly cancels the sign change when one chart's orientation does not extend to a neighbor's.

**Density correspondence.** A pseudo-$n$-form on $M^n$ is the same data as a [[Def - Density on a Manifold|density]] of order $1$ on $M$, via the bijection that on each fiber sends $(\omega(p, \mathfrak{o}_p), \mathfrak{o}_p) \in \Lambda^n(T_p^*M) \times \mathrm{Or}(T_pM) / \pm$ to the density $\mu_p(v_1,\dots,v_n) = |\omega(p, \mathfrak{o}_p)(v_1,\dots,v_n)|$ for $(v_1,\dots,v_n)$ positively oriented in $\mathfrak{o}_p$. So pseudo-top-forms and densities are interchangeable; for $k < n$ the pseudoform notion is strictly richer because it retains the de Rham complex structure.

---

# Relate to Other Fields / Compression

**Pseudoform as a "twisted" section.** The construction "ordinary form coefficient $\otimes$ orientation choice" is the prototype of a *twisted section* in algebraic topology: a section of a vector bundle tensored with a $\mathbb{Z}/2$ local system. Cohomology with twisted coefficients is the language in which Poincaré duality works on non-orientable manifolds, and the pseudoform construction is the de Rham model of these twisted coefficients. This is why **twisted cohomology** is sometimes called "cohomology of pseudoforms" in differential-geometry texts.

**True name.** The true name of a pseudo-$k$-form is *"a $k$-form that carries its own orientation-dependence inside it."* This is what makes the pseudoform notation invariant under change of chart even when the change reverses orientation: the form changes by $-1$, the orientation flips, and the product (which is what you actually evaluate) is unchanged. The classical-physics distinction between "polar" and "axial" vectors (or between scalars and pseudoscalars) is the same construction in a different language: a polar vector is a $1$-form, an axial vector is a pseudo-$1$-form, and the difference shows up only under reflections.

**Pseudoform vs density.** A pseudo-$n$-form and a density of order $1$ carry the same point information at each point — both can be integrated on any $n$-manifold, orientable or not. They differ only in their *algebraic* behavior: a pseudo-$n$-form belongs to a graded algebra under the wedge product, can be exterior-differentiated (vacuously, since $d$ on a top-form gives zero), can appear in Stokes's theorem, and has a place in the de Rham complex. A density has none of these — it is "just" a measure-theoretic object. So pseudoforms are the natural choice when one wants algebraic structure plus orientation-independent integration; densities are the natural choice when one only wants to integrate scalars and never differentiate.

**The orientation line bundle.** On a smooth $n$-manifold $M$, the orientation line bundle $\mathcal{O}_M$ is the rank-$1$ real vector bundle whose transition functions are the signs of the Jacobian determinants of the manifold's transition charts. It is trivial iff $M$ is orientable. Pseudoforms are smooth sections of $\Lambda^k T^*M \otimes \mathcal{O}_M$. This makes precise the slogan "pseudoform = form twisted by orientation": you literally tensor the form bundle with the orientation line bundle.

---

# Examples / Corollaries

**The volume "form" on the Möbius strip is a pseudo-$2$-form, not a $2$-form.** The Möbius strip $E$ admits no nowhere-vanishing ordinary $2$-form, so its "area" cannot be represented by an ordinary form. But it does admit a nowhere-vanishing *pseudo-*$2$-form: locally write down the area form $dx \wedge dy$ in a chart, and in any neighbor chart that disagrees on orientation, flip the sign automatically by the pseudoform rule. The result is a globally well-defined pseudo-$2$-form whose integral over $E$ is the area, computed concretely in [[Ex - Integration of a Pseudoform on the Möbius Strip]].

**Riemannian volume on a non-orientable Riemannian manifold is a pseudo-$n$-form.** On an oriented Riemannian $(M, g)$ the Riemannian volume form $\omega_g = \sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n$ in any oriented chart. On a non-orientable Riemannian manifold the *same formula* defines a pseudo-$n$-form rather than an ordinary $n$-form: the $\sqrt{\det g_{ij}}$ is always positive and depends only on the metric (not on the chart's orientation), and the $dx^1\wedge\cdots\wedge dx^n$ depends on the chart's orientation by a sign — together they give a pseudoform. Integrating this pseudo-$n$-form recovers the Riemannian volume of any (non-orientable) Riemannian manifold.

**Pseudoscalars: the triple product on $\mathbb{R}^3$.** The triple product $\vec u\cdot(\vec v\times\vec w)$ is a **pseudoscalar** — under reflection $(x,y,z) \mapsto (-x,-y,-z)$ (orientation-reversing) all three vectors flip sign so the triple product picks up $(-1)^3 = -1$. The volume $3$-form $dx\wedge dy\wedge dz$ also picks up $-1$ under this reflection. The triple product's well-defined value is $|\vec u\cdot(\vec v\times\vec w)|$ (the volume of the parallelepiped) plus a sign that depends on the orientation of $\mathbb{R}^3$. As a pseudo-$3$-form, the volume *form* on $\mathbb{R}^3$ is invariantly defined; as an ordinary $3$-form it depends on a choice of orientation.

**Magnetic field $\vec B$ is a pseudo-$1$-form (axial vector).** Under spatial inversion $\vec x \mapsto -\vec x$, the electric field $\vec E$ (a polar vector) flips: $\vec E \mapsto -\vec E$. The magnetic field $\vec B$ (an axial vector) does *not* flip: $\vec B \mapsto +\vec B$. This is exactly the form-language statement that $\vec E$ is a $1$-form (transforms by $\det J$ — picks up a sign on orientation-reversal) while $\vec B$ is a pseudo-$1$-form (transforms by $|\det J|$ — invariant under sign flip). The deeper reason in spacetime is that $\vec E$ comes from the time-space components of the Faraday $2$-form and $\vec B$ from the space-space components, and reflection acts differently on the two.

**Is NOT an instance: an ordinary form on the Möbius strip.** Any ordinary smooth $2$-form $\omega$ on the Möbius strip must *vanish somewhere*. Why: a global nowhere-vanishing $2$-form would give the strip an orientation (by [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form]]), but the strip is non-orientable. So $\omega$ is not "the area form" in any reasonable sense — its integral is zero or undefined as a positive area. The natural object is a pseudo-$2$-form, not a form.

**Corollary (pseudoforms on an orientable manifold reduce to forms).** If $M$ is orientable and one fixes a global orientation, then every pseudo-$k$-form is canonically an ordinary $k$-form (set $\omega(p) := \omega(p, \mathfrak{o}_p)$ using the fixed orientation). The two notions coincide. So pseudoforms are strictly *more* general than forms — they agree on orientable manifolds and only differ on non-orientable ones.

**Corollary (integration of $f$ on $M$ via the Riemannian pseudo-volume).** If $(M,g)$ is a non-orientable Riemannian manifold and $f \in C^\infty_c(M)$, one defines $\int_M f := \int_M f\,\omega_g$, where $\omega_g$ is the Riemannian pseudo-volume form. This recovers all the usual integration of functions — including the area of the Möbius strip and the surface area of $\mathbb{RP}^2$ in its standard round metric.

**Calibration check.** First, verify that the formula $\omega = dx \wedge dy$ in a Möbius-strip chart gives a globally well-defined pseudo-$2$-form by checking the orientation-flip rule on a transition map that reverses orientation (the standard Möbius identification $(x, y) \sim (x + 1, -y)$ has Jacobian $-1$, so the form changes sign — but the chart's orientation also flips, so the pseudoform is unchanged). Second, write down both an ordinary $1$-form and a pseudo-$1$-form on $S^1 \times \mathbb{R}$, integrate each around the circle, and confirm that the difference between "polar" and "axial" vectors in classical mechanics is exactly this distinction. Third, check that a pseudo-$0$-form on $M$ is a smooth section of the orientation line bundle, equivalently a function valued in $\{+1, -1\}$ when restricted to oriented charts — and verify that no such global function exists on a non-orientable manifold (this is one way to *prove* a manifold is non-orientable).

---

# Unlocked by This

> [!tip] Poincaré Duality on Non-Orientable Manifolds *(from Algebraic Topology)*
> Poincaré duality $H^k_{dR}(M) \cong H^{n-k}_{dR}(M)$ holds for compact oriented manifolds; on a non-orientable manifold one has instead the **twisted Poincaré duality** $H^k_{dR}(M) \cong H^{n-k}_{dR}(M;\mathrm{or})$, where the right side is the cohomology of the pseudoform complex. The pseudoform construction is exactly what makes Poincaré duality survive past orientability; without it, $\mathbb{RP}^2$ would appear to have "missing" cohomology. See **Algebraic Topology I — Singular Homology and the de Rham Theorem** for the full story.

> [!tip] First Stiefel–Whitney Class *(from Characteristic Classes)*
> The orientation line bundle $\mathcal{O}_M$ is classified by an element $w_1(M) \in H^1(M;\mathbb{Z}/2)$ — the **first Stiefel–Whitney class**. $M$ is orientable iff $w_1(M) = 0$ iff $\mathcal{O}_M$ is trivial. Pseudoforms are sections of the bundle classified by $w_1$, so the pseudoform construction is the de Rham model of $w_1$-twisted cohomology. The pattern generalizes — higher characteristic classes ($w_i$ for $i > 1$, Chern classes, Pontryagin classes) all serve as the "twists" for richer cohomology theories.

> [!tip] Axial Vectors in Physics *(from Electromagnetism / Mechanics)*
> The systematic distinction in physics between **polar** and **axial** vectors — and the fact that the magnetic field, angular momentum, and torque are all axial — is the dictionary's distinction between ordinary $1$-forms and pseudo-$1$-forms (or equivalently $2$-forms and pseudo-$2$-forms, depending on which Hodge dual one uses). The "parity" of a physical quantity under reflection is the orientation-dependence of its representation as a (pseudo)-form. Charge conservation under reflection is automatic precisely because the relevant equations balance polar with polar and axial with axial.

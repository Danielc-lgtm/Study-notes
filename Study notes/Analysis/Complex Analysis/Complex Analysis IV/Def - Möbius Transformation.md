---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ is the **Riemann sphere** (one-point compactification of $\mathbb{C}$). A Möbius transformation is $T : \hat{\mathbb{C}} \to \hat{\mathbb{C}}$ of the form $T(z) = (az + b)/(cz + d)$ with $a, b, c, d \in \mathbb{C}$ and $ad - bc \neq 0$. We write $\operatorname{Möb}(\hat{\mathbb{C}})$ for the group of Möbius transformations. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Axiom Motivation

The Möbius transformations are the conformal automorphisms of the Riemann sphere — the biholomorphic bijections $\hat{\mathbb{C}} \to \hat{\mathbb{C}}$. They are the simplest nontrivial holomorphic maps to study, and they form a finite-dimensional (3-complex-parameter) group, making them computationally tractable.

Why this specific form $(az + b)/(cz + d)$? Because we want:
(a) Bijective on $\hat{\mathbb{C}}$: the map must include $\infty$. A polynomial $az + b$ maps $\infty \to \infty$ but isn't surjective onto $\hat{\mathbb{C}}$ unless we include rational denominators.
(b) Holomorphic: rational functions are meromorphic, with poles being holomorphic in $\hat{\mathbb{C}}$.
(c) The simplest such map after the affine $z \mapsto az + b$: include one more parameter to handle inversion. The ratio of two affine functions is exactly the next level.

The condition $ad - bc \neq 0$ ensures non-degeneracy: if $ad - bc = 0$, the numerator and denominator are proportional, so $T(z)$ is constant. The matrix $\begin{pmatrix}a & b \\ c & d\end{pmatrix}$ is then non-invertible, and we lose the bijective structure.

The Möbius group is *triply transitive*: for any three distinct points $\alpha, \beta, \gamma$ and any three distinct images $\tilde\alpha, \tilde\beta, \tilde\gamma$, there is a *unique* Möbius transformation sending the first triple to the second. This is what makes Möbius transformations so useful in normalization arguments: any three points can be moved to a canonical position $\{0, 1, \infty\}$.

The group structure is $\operatorname{Möb}(\hat{\mathbb{C}}) \cong \operatorname{PGL}_2(\mathbb{C}) = \operatorname{GL}_2(\mathbb{C})/\{\lambda I\}$ — the quotient of invertible $2 \times 2$ complex matrices by scalar multiples. (Two matrices $\begin{pmatrix}a & b \\ c & d\end{pmatrix}$ and $\lambda \begin{pmatrix}a & b \\ c & d\end{pmatrix}$ give the same Möbius transformation, since multiplying numerator and denominator by $\lambda$ leaves the ratio unchanged.)

What would break with a different definition? Higher-degree rational functions: still biholomorphic but not bijective on $\hat{\mathbb{C}}$ (they take values multiply, except via a Riemann-surface lift). Polynomial maps: not surjective on $\hat{\mathbb{C}}$ unless degree-$0$ (constant) or affine. The $(az + b)/(cz + d)$ form is the unique minimum-degree way to get bijective biholomorphic self-maps of $\hat{\mathbb{C}}$.

---

# The Definition

A **Möbius transformation** (or **fractional linear transformation**, or **Möbius map**) is a map $T : \hat{\mathbb{C}} \to \hat{\mathbb{C}}$ of the form
$$T(z) = \frac{az + b}{cz + d}, \quad a, b, c, d \in \mathbb{C}, \quad ad - bc \neq 0,$$
extended to $\hat{\mathbb{C}}$ by:
- $T(\infty) = a/c$ (if $c \neq 0$), or $T(\infty) = \infty$ (if $c = 0$);
- $T(-d/c) = \infty$ (if $c \neq 0$).

The set of all Möbius transformations forms a **group** $\operatorname{Möb}(\hat{\mathbb{C}})$ under composition. Multiplication of corresponding matrices is composition of Möbius transformations: if $T_1$ corresponds to $\begin{pmatrix}a_1 & b_1 \\ c_1 & d_1\end{pmatrix}$ and $T_2$ to $\begin{pmatrix}a_2 & b_2 \\ c_2 & d_2\end{pmatrix}$, then $T_1 \circ T_2$ corresponds to the matrix product.

**Group isomorphism.** $\operatorname{Möb}(\hat{\mathbb{C}}) \cong \operatorname{PGL}_2(\mathbb{C}) = \operatorname{GL}_2(\mathbb{C})/\mathbb{C}^*\,I$, with the kernel of the natural map "matrix $\to$ Möbius" being the scalar multiples of identity.

**Triple transitivity.** For any two triples of distinct points $\{\alpha, \beta, \gamma\}$ and $\{\tilde\alpha, \tilde\beta, \tilde\gamma\}$ in $\hat{\mathbb{C}}$, there is a unique Möbius transformation sending the first triple to the second.

---

# Categorical Definition

In the category of Riemann surfaces, the Möbius transformations are the **biholomorphic automorphisms** of $\hat{\mathbb{C}}$ (the projective complex line $\mathbb{P}^1(\mathbb{C})$). The automorphism group of $\mathbb{P}^1$ is $\operatorname{PGL}_2$, the projective general linear group.

For readers unfamiliar with category theory: the Möbius group is exactly the symmetry group of the Riemann sphere, viewed as a holomorphic object. Every holomorphic bijection $\hat{\mathbb{C}} \to \hat{\mathbb{C}}$ is a Möbius transformation; conversely every Möbius transformation is a holomorphic bijection.

---

# Relate to Other Fields / Compression

In **projective geometry**, $\hat{\mathbb{C}} = \mathbb{P}^1(\mathbb{C})$ is the projective complex line, and the Möbius group is its automorphism group $\operatorname{PGL}_2(\mathbb{C})$. The action of $\operatorname{PGL}_2$ on $\mathbb{P}^1$ is the simplest nontrivial example of projective representation theory.

In **hyperbolic geometry**, the subgroup of Möbius transformations preserving the upper half-plane $\mathbb{H}$ is $\operatorname{PSL}_2(\mathbb{R})$ (real coefficients with $ad - bc = 1$), and acts as the orientation-preserving isometries of the hyperbolic plane. Similarly the subgroup preserving the unit disc $\mathbb{D}$ is $\operatorname{PSU}(1, 1)$, and acts as hyperbolic isometries of the Poincaré disc model.

In **string theory and conformal field theory**, the Möbius group is the **global conformal symmetry group of the 2-dimensional sphere**, acting on the Riemann surface that conformal field theories live on. Conformal invariance under Möbius transformations is one of the basic axioms of CFT, and the modular forms of number theory are generating functions invariant (in a specific sense) under subgroups of $\operatorname{PSL}_2(\mathbb{Z})$.

In **special relativity**, the Möbius transformations on the celestial sphere correspond to **Lorentz boosts and rotations** in $\mathbb{R}^{3,1}$. The celestial sphere $S^2 \cong \hat{\mathbb{C}}$ via stereographic projection, and the Lorentz group $\operatorname{SO}^+(3, 1) \cong \operatorname{PSL}_2(\mathbb{C})$ acts on it as the Möbius group. This is the simplest manifestation of the spinor structure of spacetime.

---

# Examples / Corollaries

**Is an instance — affine maps $z \mapsto az + b$.** With $c = 0, d = 1$: $T(z) = az + b$. These are translations and scalings (plus rotations, if $|a| = 1$). They fix $\infty$.

**Is an instance — inversion $z \mapsto 1/z$.** With $a = d = 0, b = c = 1$: $T(z) = 1/z$. This swaps $0$ and $\infty$, and is its own inverse.

**Is an instance — Cayley transform $z \mapsto (z - i)/(z + i)$.** Maps the upper half-plane $\mathbb{H}$ to the unit disc $\mathbb{D}$, with $i \mapsto 0$, $\infty \mapsto 1$, $\pm 1 \mapsto$ specific points on the unit circle.

**Is an instance — automorphism of the disc.** $T(z) = e^{i\theta}(z - a)/(1 - \bar a z)$ for $|a| < 1, \theta \in \mathbb{R}$. Maps $\mathbb{D}$ to itself with $T(a) = 0$.

**Is NOT an instance — $z \mapsto z^2$.** Not bijective on $\hat{\mathbb{C}}$ (everywhere $2$-to-$1$ except at $0, \infty$). Holomorphic but not a Möbius transformation.

**Is NOT an instance — $z \mapsto \bar z$.** Conjugation is bijective on $\hat{\mathbb{C}}$ but not *holomorphic* (it's anti-holomorphic). The Möbius transformations are *holomorphic* bijections.

**Corollary — Möbius transformations are determined by their action on three points.** Triple transitivity: a Möbius transformation is uniquely specified by where it sends three distinct points. So you can compute a Möbius transformation by specifying its action on three points and solving.

**Corollary — composition of Möbius is Möbius.** The composition of $(az + b)/(cz + d)$ and $(a'z + b')/(c'z + d')$ is another Möbius transformation, with coefficients given by matrix multiplication. So $\operatorname{Möb}(\hat{\mathbb{C}})$ is a group.

**Corollary — every Möbius transformation is a composition of standard pieces.** Every Möbius transformation factors as a composition of: translations ($z + b$), scalings ($az$), and inversion ($1/z$). Specifically: if $c \neq 0$, $T(z) = a/c + (bc - ad)/(c^2)\cdot 1/(z + d/c)$, a composition of a translation, an inversion, a scaling, and another translation.

**Calibration check.** Verify the non-degeneracy condition $ad - bc \neq 0$ is what excludes constant maps (when $ad = bc$, numerator and denominator are proportional and the ratio degenerates). Verify that the matrices $M$ and $\lambda M$ for any $\lambda \neq 0$ give the *same* Möbius transformation, which is why $\operatorname{Möb}(\hat{\mathbb{C}}) \cong \operatorname{PGL}_2(\mathbb{C})$ and not $\operatorname{GL}_2(\mathbb{C})$. And verify triple transitivity by constructing the unique Möbius transformation that sends three given distinct points to $\{0, 1, \infty\}$ — the normalisation that makes Möbius geometry tractable.

---

# Unlocked by This

> [!tip] Generalized Circles Preserved *(from §3.5+)*
> The key geometric property: Möbius transformations [[Thm - Möbius Transformations Preserve Generalized Circles|preserve generalized circles]] (circles and lines, which become circles on the Riemann sphere). This is what makes them useful in conformal mapping.

> [!tip] Conformal Automorphisms of the Disc *(from §3.5+)*
> The biholomorphic automorphisms of the unit disc are exactly the Möbius transformations of a specific form ([[Thm - Conformal Automorphisms of the Unit Disc]]).

> [!tip] Hyperbolic Geometry *(from Differential Geometry)*
> The Möbius transformations preserving the upper half-plane (or the disc) are the isometries of the hyperbolic plane. This connects complex analysis to the geometry of $\operatorname{PSL}_2(\mathbb{R})$.

> [!tip] Lorentz Group in Relativity *(from Special Relativity)*
> The Möbius group on $\hat{\mathbb{C}}$ is isomorphic to the orientation-preserving Lorentz group on $\mathbb{R}^{3,1}$, acting on the celestial sphere. This is a deep connection between 2D complex analysis and 4D spacetime symmetry.

---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - The Tangent Space"
  - "Def - The Tangent Bundle"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold of dimension $n$. $TM = \bigsqcup_{p \in M} T_p M$ is its [[Def - The Tangent Bundle|tangent bundle]], with projection $\pi : TM \to M$ sending $v \in T_p M$ to $p$. In a chart $(U, (x^i))$, every tangent vector $X_p \in T_p M$ has a unique expansion $X_p = X^i(p)\, \partial/\partial x^i\big|_p$ with components $X^i(p) \in \mathbb{R}$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Axiom Motivation

What should a "vector field on a manifold" be? The intuition is **a velocity at every point**: at each $p \in M$ you specify a tangent vector $X_p$, the direction and speed of motion at that location. On $\mathbb{R}^n$ the picture is clear — assign to each point a vector in $\mathbb{R}^n$, and you have a vector field. On an abstract manifold there is no global $\mathbb{R}^n$ in which the vectors live: the vector at $p$ lives in the tangent space $T_p M$, the vector at $q$ lives in $T_q M$, and these are formally different vector spaces. The first thing the definition must do is account for this: a "vector field" is not a single function $M \to \mathbb{R}^n$ but an assignment $p \mapsto X_p \in T_p M$.

The cleanest way to package this is to bundle all the tangent spaces together into one space, the [[Def - The Tangent Bundle|tangent bundle]] $TM$, with a projection $\pi : TM \to M$ recording which tangent space each vector belongs to. A vector field is then a map $X : M \to TM$ satisfying the one constraint that $X_p$ actually lives in $T_p M$ — equivalently, $\pi(X_p) = p$, equivalently $\pi \circ X = \mathrm{id}_M$. This is the definition of a **section** of $\pi$. So a vector field is exactly a section of the tangent bundle. The constraint $\pi \circ X = \mathrm{id}_M$ is the categorical encoding of "the vector at $p$ lives at $p$", and dropping it would allow ill-typed assignments like sending $p$ to a vector at some other point.

This raw definition has no smoothness in it — at this stage we have only a *rough* vector field (also called a *section* without further qualification). Smoothness is a separate axiom, imposed in [[Def - Smooth Vector Field]]: the map $X : M \to TM$ should be smooth as a map between smooth manifolds. The reason to separate the two definitions is that rough vector fields appear naturally in proofs even when the final object is required to be smooth — for instance, you construct a rough field by defining it pointwise (say, $X_p = $ "value at $p$ of the rough extension of a tangent vector"), and *then* check smoothness as a separate step.

Why not demand that $X_p$ depend on $p$ in some *continuous* way as part of the definition? Because continuity is automatic from the manifold-section viewpoint plus chart-by-chart smoothness, and stating it as an extra axiom would be redundant. The definition is meant to be minimal — it should encode only what is needed to fix the type of the object, leaving regularity to be the substance of the separate "smooth vector field" definition.

The reason this is the *right* abstraction is that everything that follows — integral curves, flows, the bracket — extends from $\mathbb{R}^n$ by reading the definitions chart-by-chart, and the chart-independence is automatic from the section-of-$TM$ formulation. Were we to define a vector field as "an $\mathbb{R}^n$-valued function in each chart, with compatible transformation rules between charts", we would have to verify the compatibility every time; bundling the data into a single section makes the compatibility automatic. The price is the abstraction of $TM$, but that price has already been paid by the construction of the tangent bundle in [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# The Definition

A **vector field** on a smooth manifold $M$ is a map

$$X : M \to TM$$

such that $\pi \circ X = \mathrm{id}_M$, where $\pi : TM \to M$ is the tangent bundle projection. Equivalently, $X$ assigns to each point $p \in M$ a tangent vector $X_p \in T_p M$.

In a smooth chart $(U, (x^i))$, the restriction $X|_U$ has the coordinate expression

$$X = X^i\, \frac{\partial}{\partial x^i},$$

where the **component functions** $X^i : U \to \mathbb{R}$ are determined by $X_p = X^i(p)\, \partial/\partial x^i\big|_p$ for $p \in U$.

When the additional regularity is required, the map $X : M \to TM$ is called **continuous** if it is continuous as a map between topological spaces, and **smooth** if it is smooth as a map between smooth manifolds — see [[Def - Smooth Vector Field]] for the smooth case.

---

# Categorical Definition

A vector field on $M$ is precisely a **section of the tangent bundle** $\pi : TM \to M$ in the category of smooth manifolds (or topological spaces, when no regularity is imposed). In categorical language: $\pi : TM \to M$ is a morphism in the slice category $\mathbf{Man}/M$, and a section is a right inverse — a morphism $X : M \to TM$ with $\pi \circ X = \mathrm{id}_M$.

This formulation generalizes immediately to other bundles. Sections of the cotangent bundle $T^*M$ are *covector fields* or *one-forms*; sections of tensor product bundles are *tensor fields*; sections of a general vector bundle $E \to M$ are simply called *sections of $E$*. The whole apparatus of this chapter — module structure, Lie bracket, derivations — extends in some form to all of these, with $TM$ being the prototypical and richest case because of the bracket. See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].

---

# Relate to Other Fields / Compression

A vector field on $\mathbb{R}^n$ is a map $X : \mathbb{R}^n \to \mathbb{R}^n$ — the "tangent space at every point" disappears because $T_p \mathbb{R}^n$ canonically identifies with $\mathbb{R}^n$. So on $\mathbb{R}^n$, vector field = vector-valued function, and the picture is the familiar arrow-at-each-point. The manifold version is just the price paid for allowing the underlying space to bend: tangent vectors at different points cannot be added or compared without the apparatus of $TM$ and connections.

In linear algebra terms, a vector field $X$ is a **choice of element from each fibre of a vector bundle**: at each $p$, you pick one $X_p \in T_p M$. The pointwise vector-space structure of $T_p M$ — addition and scalar multiplication of tangent vectors — promotes the set $\Gamma(TM)$ of vector fields to a vector space (and indeed a module over $C^\infty(M)$); see [[Def - Smooth Vector Field]].

**True name:** A vector field is a **smooth choice of velocity at every point**. The "smooth" is in [[Def - Smooth Vector Field]]; the bare definition fixes only the type of the object — assignment of a tangent vector at each point — leaving regularity for later.

---

# Examples / Corollaries

**Is an instance: the coordinate vector field $\partial/\partial x^i$ in a chart $(U, (x^i))$.** At each $p \in U$, $(\partial/\partial x^i)_p$ is the tangent vector to the $i$-th coordinate curve. This is well-defined as a vector field on the chart domain $U$, and is the simplest possible nontrivial vector field. Its components are constants: $X^j = \delta_i^j$.

**Is an instance: the Euler / radial vector field on $\mathbb{R}^n$.** Define $E = x^i \,\partial/\partial x^i$, the field whose value at $x \in \mathbb{R}^n$ points radially outward with magnitude $\lVert x \rVert$. It vanishes at the origin; elsewhere it points away from $0$. It appears in Euler's homogeneous-function theorem and in the proof of the [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|Poincaré lemma]].

**Is an instance: the rotation field on $\mathbb{R}^2$.** Define $W = -y\,\partial/\partial x + x\,\partial/\partial y$. Its integral curves are circles centred at the origin, traversed counterclockwise. The flow is rotation: $\phi_t(x, y) = (x\cos t - y\sin t, x\sin t + y\cos t)$.

**Is an instance: the velocity field of a flow.** Given any smooth one-parameter family of diffeomorphisms $\phi_t : M \to M$ with $\phi_0 = \mathrm{id}$, the assignment $p \mapsto \frac{d}{dt}\big|_{t=0} \phi_t(p)$ is a smooth vector field on $M$. The flow recovers the vector field by differentiation at $t = 0$ — see [[Def - Flow of a Vector Field]].

**Is an instance: the angle vector field $d/d\theta$ on $S^1$.** Choose an angle coordinate $\theta$ on any proper open subset of $S^1$; the coordinate vector field $d/d\theta$ extends to a globally defined nonvanishing smooth vector field on $S^1$ (because $d\theta$ is determined up to additive constants by any choice of angle coordinate). $S^1$ is therefore *parallelizable*: it admits a global nonvanishing vector field.

**Is NOT an instance: an arbitrary map $X : M \to TM$.** A map $X : M \to TM$ that fails the section condition $\pi \circ X = \mathrm{id}_M$ is not a vector field. The map sending every point of $M$ to a fixed vector in $T_{p_0} M$ (for some chosen $p_0$) is a constant map $M \to T_{p_0} M \subset TM$, and it fails to be a vector field everywhere except at $p_0$. The condition $\pi \circ X = \mathrm{id}_M$ rules this out by enforcing "the vector at $p$ is in $T_p M$".

**Is NOT an instance: a globally nonvanishing continuous vector field on $S^2$.** The hairy ball theorem (a consequence of the Poincaré–Hopf theorem in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]] / [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|de Rham]]) says no such field exists — every continuous vector field on $S^2$ has a zero. So while vector fields *exist* on $S^2$, *nonvanishing* ones do not, and this is the prototypical obstruction to parallelizability.

**Corollary (extension by zero).** A vector field $X$ on an open subset $U \subseteq M$ that is supported in a compact set $K \subset U$ extends by zero to a vector field on $M$. This is the basic move for localizing a vector field: take any local vector field, multiply by a bump function supported in $U$, and obtain a globally defined vector field that agrees with the original on a smaller neighbourhood. *Calibration check:* you should be able to write the extension explicitly: $\tilde X_p = \rho(p) X_p$ on $U$ and $\tilde X_p = 0$ on $M \setminus U$, where $\rho$ is a smooth bump function.

**Corollary (chart-independence of vanishing).** The set $\{p \in M : X_p = 0\}$ is independent of the choice of chart, even though the components $X^i$ are chart-dependent. The reason is that $X_p$ is the abstract tangent vector at $p$, defined intrinsically as a derivation at $p$ or an equivalence class of curves at $p$; the components depend on the chart but their simultaneous vanishing does not.

**Calibration check.** You should be able to verify the following two facts directly from the definition: (a) every linear combination $aX + bY$ of vector fields is a vector field (uses the vector-space structure of each $T_p M$); (b) the values of $X$ on any open subset $U \subseteq M$ determine $X$ on $U$ — vector fields are local objects, not just global ones. Both follow immediately from the section-of-$TM$ formulation.

---

# Unlocked by This

> [!tip] Sections of a Vector Bundle *(from Vector Bundle Theory)*
> Replacing $TM$ by any [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|vector bundle]] $E \to M$ and the section condition $\pi \circ X = \mathrm{id}_M$ verbatim, you obtain the notion of **sections of $E$**. Covector fields, tensor fields, differential forms, spinor fields, and gauge fields are all "sections of an appropriate bundle". The pattern is the same in every case: a section is a smooth choice of element from each fibre, and the space of sections is a module over $C^\infty(M)$.

> [!tip] Frame *(from Differential Geometry, intermediate)*
> An ordered $n$-tuple $(E_1, \dots, E_n)$ of vector fields on $U \subseteq M$ is a **local frame** if $(E_1|_p, \dots, E_n|_p)$ is a basis of $T_p M$ at every $p \in U$. A **global frame** exists for $U = M$ if and only if $M$ is **parallelizable** — true for $\mathbb{R}^n$, $S^1$, $S^3$, $S^7$, and every Lie group; false for $S^2$ and most spheres. Frames are the local trivializations of $TM$ and the basic tool for computations in differential geometry.

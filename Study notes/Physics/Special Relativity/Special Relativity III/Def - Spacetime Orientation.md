---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. The vector space is $E$, four-dimensional; an orthonormal basis is $(e_0,e_1,e_2,e_3)$ with $e_0\cdot e_0 = +1$, $e_i\cdot e_i = -1$. The space of antisymmetric four-linear forms on $E$ is $A_4(E)$. The chosen orientation form is $\epsilon$ (the Levi-Civita tensor), with components $\epsilon_{\alpha\beta\gamma\delta}$. The symmetric group on four letters is $S_4$, with $k(\sigma)$ the number of transpositions in a permutation $\sigma$. Full registry on [[Special Relativity III — Minkowski Spacetime and the Metric]].

> [!warning] Convention: signature and orientation
> The orientation form $\epsilon$ is singled out by taking the value $+1$ on a *right-handed* orthonormal basis. The signature convention (mostly-minus here, mostly-plus in Gourgoulhon) affects the sign relating $\epsilon$ with the components $\epsilon^{\alpha\beta\gamma\delta}$ (raising indices brings a factor of $\det\eta = -1$), but the orientation itself — a choice of one of two forms — is convention-independent.

---

# Axiom Motivation

Orienting a space means making a consistent global choice of "handedness". In a plane it is the choice of clockwise versus anticlockwise; in three-dimensional space it is the choice of right-handed versus left-handed bases, made precise by the sign of a determinant relative to a reference basis. The motivation for this page is to extend that notion to the four-dimensional Minkowski space, where it is needed for two things the chapter cannot do without: signed four-volumes (integration over spacetime) and the Hodge star (the duality that puts electromagnetism into its cleanest form).

The construction goes through *antisymmetric multilinear forms*, and the key fact is a dimension count. In three dimensions the determinant is an antisymmetric *trilinear* form — feed it three vectors, get their signed volume — and the space of such forms is one-dimensional, so all of them are proportional and the determinant is fixed once you normalise it to $+1$ on a reference basis. The same structure works in four dimensions with *four*-linear forms. The space $A_4(E)$ of antisymmetric four-linear forms on the four-dimensional $E$ is, by a classical result of linear algebra, **one-dimensional**: all such forms are proportional. So to orient $E$ it suffices to single out one of them, up to positive scale, and call the bases on which it is positive "right-handed".

But which one? Any positive multiple of a chosen form would orient the space equally well, so orientation *alone* needs only a ray in the one-dimensional $A_4(E)$. The [[Def - Minkowski Space and the Metric|metric]] does more: it singles out *two specific* forms — the opposite of each other — by demanding the value $\pm 1$ on every *orthonormal* basis. This works because any two orthonormal bases are related by a Lorentz transformation, whose determinant is $\pm 1$, so a form that is $\pm 1$ on one orthonormal basis is $\pm 1$ on all of them. Among the one-parameter family of four-forms, exactly two have this normalisation, and they differ by sign. Choosing one of them, denoted $\epsilon$ and called the **Levi-Civita tensor**, simultaneously orients the space (a basis is right-handed iff $\epsilon$ is positive on it) *and* provides a canonical **volume element** (the value of $\epsilon$ on four vectors is their signed four-volume relative to a right-handed orthonormal basis). The motivation for tying the orientation to the metric is exactly this double duty: the metric-normalised $\epsilon$ is both the orientation and the volume form, the object integrated against and the engine of the Hodge dual.

The antisymmetry of $\epsilon$ is the formal expression of "signed": swapping two arguments flips the sign, so $\epsilon(\ldots, X, \ldots, X, \ldots) = 0$ whenever two arguments coincide (a degenerate parallelepiped has zero volume). For a general permutation $\sigma$ of the four arguments, $\epsilon$ picks up $(-1)^{k(\sigma)}$, the sign of the permutation. Here Gourgoulhon flags a trap worth internalising (Remark 1.14): in four dimensions a *cyclic* permutation of the four arguments is **odd**, not even — unlike the three-dimensional case where cyclic permutations of the triple product are even. So one cannot blindly carry over three-dimensional sign intuition; the sign is governed by the parity of the permutation, and a 4-cycle is a product of three transpositions, hence odd.

---

# The Definition

The space $A_4(E)$ of **antisymmetric four-linear forms** on the four-dimensional vector space $E$ consists of the maps $A : E^4 \to \mathbb{R}$ that are linear in each argument and change sign under the exchange of any two arguments. This space is **one-dimensional**, so any two such forms are proportional.

The [[Def - Minkowski Space and the Metric|metric]] singles out two of these forms by the normalisation
$$
(e_0,e_1,e_2,e_3) \text{ orthonormal} \quad\Longrightarrow\quad A(e_0,e_1,e_2,e_3) = \pm 1,
$$
which is consistent across orthonormal bases because they are related by Lorentz transformations of determinant $\pm 1$. An **orientation** (more precisely a *spacetime orientation* together with a volume form) is a choice of one of these two forms, denoted $\epsilon$ and called the **Levi-Civita tensor**:
$$
(e_0,e_1,e_2,e_3) \text{ orthonormal} \quad\Longrightarrow\quad \epsilon(e_0,e_1,e_2,e_3) = \pm 1.
$$
A basis $(b_0,b_1,b_2,b_3)$ (not necessarily orthonormal) is **right-handed** if $\epsilon(b_0,b_1,b_2,b_3) > 0$ and **left-handed** if $\epsilon(b_0,b_1,b_2,b_3) < 0$; for a right-handed orthonormal basis one normalises $\epsilon(e_0,e_1,e_2,e_3) = +1$.

The antisymmetry gives, for any permutation $\sigma \in S_4$ and any four vectors,
$$
\epsilon(X_{\sigma(1)}, X_{\sigma(2)}, X_{\sigma(3)}, X_{\sigma(4)}) = (-1)^{k(\sigma)}\,\epsilon(X_1, X_2, X_3, X_4),
$$
where $k(\sigma)$ is the number of transpositions composing $\sigma$ ($\sigma$ is **even** or **odd** as $k(\sigma)$ is). Equivalently $\epsilon$ is an **alternating form**: it vanishes whenever two arguments are equal. Its components in an orthonormal basis are $\epsilon_{\alpha\beta\gamma\delta} = \pm 1$ for $(\alpha\beta\gamma\delta)$ an even/odd permutation of $(0123)$ and $0$ if any two indices coincide.

Applied to four vectors, $\epsilon$ returns their **determinant** with respect to any right-handed orthonormal basis — it is the four-dimensional generalisation of the scalar triple product. It is the **volume element** of spacetime: the object integrated to give four-dimensional volumes.

---

# Categorical / Structural Definition

The orientation lives in the **top exterior power** $\Lambda^4 E^*$, which is canonically isomorphic to $A_4(E)$ and is one-dimensional for a four-dimensional $E$. An orientation of a real vector space is, abstractly, a choice of connected component of $\Lambda^4 E^* \setminus \{0\}$ (equivalently, a choice of ray, since the nonzero top forms fall into two rays). The Levi-Civita tensor refines this: instead of merely a ray, the metric picks out two specific elements (a *volume form*), so $\epsilon$ carries strictly more information than a bare orientation — it fixes a *scale* as well as a *sign*, namely the value $\pm 1$ on orthonormal bases.

In the language of $G$-structures, choosing $\epsilon$ reduces the structure group from $O(1,3)$ (which contains determinant-$-1$ elements that flip the orientation) to the orientation-preserving subgroup $SO(1,3)$ (determinant $+1$); imposing additionally the time orientation reduces it to the proper orthochronous $SO^+(1,3)$. The Levi-Civita form is the invariant volume form of $SO(1,3)$, the analogue of the standard volume form on oriented Euclidean space invariant under $SO(n)$.

The volume-form aspect is the gateway to integration: $\epsilon$ is the constant, flat-space case of the Riemannian volume form $\sqrt{|g|}\,d^4x$ on a curved spacetime, which is what makes $\int_\Omega f\,\epsilon$ a well-defined coordinate-independent integral over a region $\Omega$.

---

# Relate to Other Fields / Compression

The Levi-Civita tensor is the **determinant**, promoted from a function of a matrix to an invariant four-linear form on a four-dimensional space, and tied to the metric by the orthonormal-basis normalisation. In three dimensions the same object is the scalar triple product / the $\varepsilon_{ijk}$ symbol of vector calculus; in four dimensions it is $\epsilon_{\alpha\beta\gamma\delta}$, and the cross product of vector calculus generalises to contractions of $\epsilon$ with vectors. The generalisation to alternating forms of all degrees is the **exterior algebra** of [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]]; $\epsilon$ is the top-degree (degree-four) form, the one that gives volumes and, combined with the [[Def - Metric Duality and Index Manipulation|metric]], the Hodge star.

**True name:** the orientation is *a choice of one of the two unit antisymmetric four-forms*, and the Levi-Civita tensor $\epsilon$ is *the signed four-volume relative to a right-handed orthonormal basis*. Operationally, $\epsilon$ is the determinant: $\epsilon(X_0,X_1,X_2,X_3) = \det[X_j^\alpha]$ in a right-handed orthonormal basis, with the warning that a 4-cycle of the arguments is odd.

---

# Examples / Corollaries

**Is an instance — the standard orientation in coordinates.** With the orthonormal basis $(e_0,e_1,e_2,e_3)$ ordered $(t,x,y,z)$ declared right-handed, $\epsilon(e_0,e_1,e_2,e_3) = +1$, and $\epsilon$ on four general vectors is the $4\times4$ determinant of their components. This is the usual choice in special relativity.

**Is an instance — a parity-related left-handed basis.** Reflecting one spatial axis, $(e_0,e_1,e_2,e_3) \mapsto (e_0,-e_1,e_2,e_3)$, gives a basis with $\epsilon = -1$: left-handed. A spatial reflection (parity) reverses orientation, which is why the parity transformation has $\det = -1$ and lies outside $SO(1,3)$.

**Is NOT an instance — a symmetric four-linear form.** A form that does *not* change sign under exchange of arguments — say $S(X_1,X_2,X_3,X_4) = (X_1\cdot X_2)(X_3\cdot X_4)$ — is not in $A_4(E)$ and cannot serve as an orientation: it does not vanish on degenerate arguments and is not proportional to $\epsilon$. Orientation requires *antisymmetry*.

**Corollary — a cyclic permutation is odd in four dimensions.** The 4-cycle $(0123) \mapsto (1230)$ decomposes into three transpositions, so $\epsilon(e_1,e_2,e_3,e_0) = (-1)^3\epsilon(e_0,e_1,e_2,e_3) = -\epsilon(e_0,e_1,e_2,e_3)$. The careless three-dimensional intuition ("cyclic permutations preserve the triple product") fails here (Remark 1.14).

**Corollary — $\epsilon$ vanishes on linearly dependent vectors.** If the four arguments are linearly dependent, $\epsilon$ returns $0$ (a degenerate parallelepiped has zero four-volume), since an alternating form vanishes whenever its arguments are dependent. This is the calibration that $\epsilon$ is a genuine volume.

**Calibration check.** If you have understood the definition you can: (i) compute $\epsilon(e_2,e_0,e_1,e_3)$ relative to a right-handed orthonormal basis by counting the transpositions needed to sort $(2013)$ into $(0123)$; (ii) explain why $A_4(E)$ being one-dimensional means orientation is a binary choice; (iii) state why a spatial reflection reverses the orientation while a boost does not.

---

# Unlocked by This

> [!tip] The Hodge Star *(from §3.3 and Electromagnetism)*
> Combining the orientation form $\epsilon$ with the [[Def - Metric Duality and Index Manipulation|metric]] gives the **Hodge star** $\star$, which maps a $k$-form to a $(4-k)$-form by contracting with $\epsilon$ and raising indices with $g$; see [[Def - The Hodge Star]]. The Hodge star is what turns the second pair of Maxwell's equations into $d{\star}F = J$, and it is the only place in electromagnetism where the orientation and the metric explicitly enter together.

> [!tip] Integration on Spacetime and Stokes' Theorem *(from §3.3 and Field Theory)*
> As a **volume element**, $\epsilon$ is what makes $\int_\Omega f\,\epsilon$ a coordinate-independent integral over a four-dimensional region; this is the foundation of [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem|integration in spacetime]] and the relativistic **Stokes' theorem** $\int_\Omega d\omega = \int_{\partial\Omega}\omega$, the tool behind conservation laws expressed as flux integrals over the boundary of a spacetime region.

> [!tip] Orientability and Time-Orientability *(from General Relativity)*
> On a curved spacetime, the existence of a global Levi-Civita form is the condition of **orientability**, and the analogous global choice of future null cone is **time-orientability**; together they reduce the structure group to $SO^+(1,3)$ at every point. These are the standing assumptions of **general relativity** that allow integration, the Hodge star, and a consistent arrow of time on the whole manifold — the global versions of the choices made here.

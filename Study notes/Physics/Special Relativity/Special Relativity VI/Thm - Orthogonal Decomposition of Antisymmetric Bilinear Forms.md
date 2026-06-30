---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
  - "Def - Spacetime Orientation"
  - "Def - Metric Duality and Index Manipulation"
  - "Thm - Euclidean Character of the Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$. $E$ is the four-dimensional displacement space; $A$ is an antisymmetric bilinear form on $E$; $U_0$ is a unit timelike vector ($U_0\cdot U_0 = +1$) with [[Def - Observer and Local Rest Space|rest space]] $E_{U_0} = U_0^\perp$. The lowered $U_0$ is $\underline{U_0} = g(U_0,\cdot)$, with $\langle\underline{U_0}, X\rangle = U_0\cdot X$. The [[Def - Spacetime Orientation|Levi-Civita tensor]] is $\epsilon$; $q\otimes p$ is the tensor product of linear forms, $(q\otimes p)(X,Y) = \langle q, X\rangle\langle p, Y\rangle$. The rest-space cross product is $\vec v\times_{U_0}\vec w = \epsilon(U_0, \vec v, \vec w, \cdot)^\sharp$. Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

> [!warning] Convention
> Gourgoulhon (his §3.5.2, mostly-plus $\vec u\cdot\vec u = -1$) writes the decomposition $A = \underline{u}\otimes q - q\otimes\underline{u} + \epsilon(\vec u, \vec b, \cdot, \cdot)$ with $q = A(\cdot, \vec u)$. Translating to our mostly-minus convention with $U_0\cdot U_0 = +1$, the two tensor-product terms **swap sign** (so that $A(\cdot, U_0) = q$ still holds — verified below), giving $A = q\otimes\underline{U_0} - \underline{U_0}\otimes q + \epsilon(U_0, \vec b, \cdot, \cdot)$. The orthogonality conditions $\langle q, U_0\rangle = 0$ and $U_0\cdot\vec b = 0$ are signature-independent.

---

# Statement

> **Orthogonal decomposition of an antisymmetric bilinear form.** Let $A$ be an antisymmetric bilinear form on the four-dimensional Minkowski space $E$, and let $U_0$ be a unit timelike vector. Then there exist a **unique** linear form $q\in E^*$ and a **unique** vector $\vec b\in E$, both orthogonal to $U_0$,
> $$\langle q, U_0\rangle = 0, \qquad U_0\cdot\vec b = 0,$$
> such that
> $$\boxed{\,A \;=\; q\otimes\underline{U_0} - \underline{U_0}\otimes q + \epsilon(U_0, \vec b, \cdot, \cdot)\,}.$$
> Explicitly, for all $X, Y\in E$,
> $$A(X, Y) = \langle q, X\rangle\,(U_0\cdot Y) - (U_0\cdot X)\,\langle q, Y\rangle + \epsilon(U_0, \vec b, X, Y).$$
> The form $q = A(\cdot, U_0)$ is the **electric part** and the vector $\vec b$ the **magnetic part** of $A$ relative to $U_0$. Restricted to the rest space $E_{U_0}$, $A$ acts as the mixed (scalar triple) product with $\vec b$: $A(X, Y) = \epsilon(U_0, \vec b, X, Y) = (\vec b\times_{U_0}X)\cdot Y$ for $X, Y\in E_{U_0}$.

> **Corollary (degrees of freedom).** An antisymmetric $4\times 4$ matrix has $6$ independent entries; $q$ (orthogonal to $U_0$) has $3$, and $\vec b$ (orthogonal to $U_0$) has $3$, so $3 + 3 = 6$ — the decomposition is an exact reparametrisation.

---

# Motivation

This is the one piece of genuinely new linear algebra in the chapter, and it is the engine behind two of the most important constructions in relativity: the splitting of the four-rotation into acceleration and spin, and the splitting of the electromagnetic field into electric and magnetic parts. The question it answers is structural: an antisymmetric bilinear form on spacetime has six independent components, with no preferred way to organise them — but the moment an *observer* is chosen (a timelike direction $U_0$), can those six components be organised into two physically meaningful three-component pieces? The theorem says yes, uniquely, and the two pieces are exactly what the observer measures.

The reason a six-component object should split into $3 + 3$ relative to a timelike direction is the same reason a four-vector splits into a time component and a spatial three-vector: the chosen direction $U_0$ breaks the four-dimensional symmetry, and antisymmetric forms organise themselves into "mixed time-space" components and "purely spatial" components. The mixed components — those with one index along $U_0$ — form the **electric part** $q$, a rest-space one-form with three components. The purely spatial components — both indices in the rest space — form the **magnetic part** $\vec b$, a rest-space vector with three components (because an antisymmetric form on the three-dimensional rest space is dual, via the cross product, to a vector). Six components, split $3 + 3$, by which index points along $U_0$.

The names "electric" and "magnetic" are not decorative. The electromagnetic field is an antisymmetric bilinear form $F$, and decomposing it relative to an observer's four-velocity yields exactly the electric field $\mathbf E$ (the electric part $q$, with $E_\mu = F_{\mu\nu}U_0^\nu$) and the magnetic field $\mathbf B$ (the magnetic part $\vec b$) that *that observer* measures. A different observer, with a different $U_0$, gets a different split — which is the origin of the frame-dependence of $\mathbf E$ and $\mathbf B$, and why a pure electric field in one frame carries a magnetic field in another. The theorem is the algebraic skeleton of that whole story, proved once here in full generality and reused for the four-rotation now and the electromagnetic field in [[Special Relativity XXI — The Electromagnetic Field]].

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A$ is an antisymmetric bilinear form and $U_0$ is a unit timelike vector". The disguises are worth recognising.

The first disguised source is **"$A$ is the four-rotation $\underline\Omega$ of a local frame"**. The evolution of an orthonormal [[Def - Local Frame and Four-Rotation|local frame]] is governed by an antisymmetric form $\underline\Omega$, and applying the decomposition with $U_0$ the observer's four-velocity splits the frame's motion into the four-acceleration (electric) and spatial rotation (magnetic). The bridge is that orthonormality forces $\underline\Omega$ antisymmetric. *Example problem:* split $de_\alpha/d\tau$ into Fermi–Walker and spatial-rotation parts.

The second disguised source is **"$A$ is the electromagnetic field tensor $F$"**. The field $F_{\mu\nu}$ is antisymmetric by construction (it is $dA$ for a potential one-form $A$), so relative to an observer's four-velocity it splits into the electric and magnetic fields that observer measures. The bridge is the antisymmetry of any exterior derivative of a one-form. *Example problem:* compute $\mathbf E$ and $\mathbf B$ as the electric and magnetic parts of $F$ for a given observer ([[Def - The Electromagnetic Field Tensor]]).

The third disguised source is **"$A$ is the angular-momentum two-form, or any rank-two antisymmetric tensor"**. Spin tensors, vorticity two-forms, and the like are all antisymmetric, and any of them decomposes relative to a chosen observer into a "polar" rest-space vector (electric) and an "axial" rest-space vector (magnetic). The bridge is simply antisymmetry. *Example problem:* decompose the relativistic angular-momentum tensor relative to an observer into a centre-of-mass moment and a spin.

**Targets (Output Amplification)**

The conclusion is "$A = q\otimes\underline{U_0} - \underline{U_0}\otimes q + \epsilon(U_0, \vec b, \cdot, \cdot)$ with $q, \vec b\perp U_0$".

Combine the conclusion with **the constraint $\Omega(U_0) = cA_0$**. When $A = \underline\Omega$ is the four-rotation, contracting the decomposition with $U_0$ identifies the electric part as $q = c\underline{A_0}$ — the four-acceleration. The further result is the Fermi–Walker/spatial-rotation split of the frame evolution, useful because it isolates the measurable acceleration and rotation. The combination is nonobvious because it pins one of the two free pieces to a physical, measurable quantity.

Combine the conclusion with **a change of observer $U_0\to U_0'$**. Decomposing the *same* $A$ relative to a boosted $U_0'$ gives a *different* electric–magnetic split, and the transformation law between the two splits is exactly how $\mathbf E, \mathbf B$ (or acceleration and rotation) mix under a boost. The further result is the observer-dependence of the electric and magnetic parts, useful because it explains why these "fields" are frame-relative shadows of one invariant object. The combination is nonobvious because the underlying $A$ is fixed while its decomposition is not.

Combine the conclusion with **the rest-space Hodge/cross-product structure**. The magnetic part appears through $\epsilon(U_0, \vec b, \cdot, \cdot)$, which on the rest space is the cross product with $\vec b$; this lets the spatial block of $A$ be inverted to *read off* $\vec b$ from $A$'s rest-space components, $b^i = \tfrac12\epsilon^{ijk}A_{jk}$ (rest-space indices). The further result is an explicit formula for the magnetic part, useful for computation. The combination is nonobvious because it converts an abstract "the magnetic part exists" into a concrete extraction.

---

# Why Is It True

The decomposition is a **partition of the components of $A$ by how many indices point along $U_0$**, and there are exactly two possibilities — one along $U_0$ (electric) or none (magnetic), since two-along is impossible for an antisymmetric form.

Choose an orthonormal frame with $e_0 = U_0$. The antisymmetric form $A$ has components $A_{\alpha\beta} = -A_{\beta\alpha}$, of which the independent ones are $A_{0i}$ (one index time, three of them) and $A_{ij}$ ($i < j$, both indices space, three of them); the diagonal $A_{00}, A_{ii}$ vanish by antisymmetry. The three "mixed" components $A_{0i}$ are exactly the components of the **electric** one-form $q = A(\cdot, U_0)$: indeed $\langle q, e_i\rangle = A(e_i, e_0) = A_{i0} = -A_{0i}$, so $q$ packages the time-space block. The three "spatial" components $A_{ij}$ form an antisymmetric $3\times 3$ block, which in three dimensions is dual to a vector — the **magnetic** vector $\vec b$, via $A_{ij} = \epsilon_{0ijk}b^k$ (the rest-space Levi-Civita), equivalently $b^k = \tfrac12\epsilon^{0kij}A_{ij}$. So the six components split cleanly: three time-space into $q$, three space-space into $\vec b$. **An antisymmetric form has only "one-time-index" and "no-time-index" components relative to $U_0$, and those are the electric and magnetic parts.**

Why is the split *unique*? Because the two pieces live in complementary, non-overlapping parts of the space of antisymmetric forms: the electric piece $q\otimes\underline{U_0} - \underline{U_0}\otimes q$ has only time-space components (it vanishes when both arguments are in the rest space), and the magnetic piece $\epsilon(U_0, \vec b, \cdot, \cdot)$ has only space-space components (it vanishes when either argument is $U_0$, since then $\epsilon$ has a repeated $U_0$). They cannot impersonate each other, so the decomposition is forced. Concretely, contracting with $U_0$ kills the magnetic piece and returns $q$ (this is why $q = A(\cdot, U_0)$); restricting to the rest space kills the electric piece and returns the magnetic block.

**The one-line mechanism: relative to $U_0$, an antisymmetric form's six components are three "one-time-index" (the electric form $q = A(\cdot, U_0)$) and three "no-time-index" (the magnetic vector $\vec b$, dual to the spatial block), and these two sets occupy complementary subspaces, forcing a unique split.**

---

# What Makes This Hard

The proof itself is not hard — it is a verification plus a uniqueness argument — but two points trip people up. First, getting the **sign and ordering of the tensor-product terms right in a given signature**: the combination $q\otimes\underline{U_0} - \underline{U_0}\otimes q$ must be ordered so that contracting with $U_0$ returns exactly $q$ (not $-q$ or $(U_0\cdot U_0)q$), and this ordering flips between mostly-plus and mostly-minus because it depends on the sign of $U_0\cdot U_0$. Second, recognising that the magnetic part is a *vector* dual to the spatial $3\times 3$ block, not a form — the cross-product/Levi-Civita identification $A_{ij}\leftrightarrow b^k$ is the step that uses the three-dimensionality of the rest space and is easy to skip. The most common error is to forget the orthogonality constraints $q, \vec b\perp U_0$, which are what make the decomposition unique (without them the pieces are underdetermined).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Define $q := A(\cdot, U_0)$ (forced, since contracting the target with $U_0$ must return it); subtract the electric piece to leave a form $B$ that vanishes on $U_0$; show $B$ restricted to the rest space is the cross product with a vector $\vec b$ read off from its spatial block; assemble and prove uniqueness from the orthogonality constraints.

**Subgoal decomposition:**

1. **Identify the electric part.** Set $q = A(\cdot, U_0)$ and check $\langle q, U_0\rangle = 0$.
   - *Hint:* $\langle q, U_0\rangle = A(U_0, U_0) = 0$ by antisymmetry.
   - *Why needed:* It is the unique candidate, fixed by requiring contraction with $U_0$ to return $q$.

2. **Subtract the electric piece.** Define $B := A - (q\otimes\underline{U_0} - \underline{U_0}\otimes q)$ and show $B(\cdot, U_0) = 0$.
   - *Hint:* Compute $B(X, U_0)$ using $U_0\cdot U_0 = +1$ and $\langle q, U_0\rangle = 0$; everything cancels.
   - *Why needed:* It isolates the purely spatial (magnetic) remainder.

3. **The remainder is the spatial cross product.** Show $B$ restricted to $E_{U_0}$ equals $\epsilon(U_0, \vec b, \cdot, \cdot)$ for a unique $\vec b\in E_{U_0}$.
   - *Hint:* An antisymmetric form on the three-dimensional rest space is dual to a vector via the rest-space Levi-Civita; define $b^i$ from the spatial block.
   - *Why needed:* It produces the magnetic part as a vector.

4. **Uniqueness.** Show $q$ and $\vec b$ are forced.
   - *Hint:* $q$ is determined by contracting with $U_0$; $\vec b$ by the non-degeneracy of $\epsilon$ on the rest space.
   - *Why needed:* It makes the decomposition canonical, not just possible.

---

# Lemma Decomposition

> [!note]- Lemma 1: The electric form is $q = A(\cdot, U_0)$ and is orthogonal to $U_0$
> **Statement:** Define $q\in E^*$ by $\langle q, X\rangle = A(X, U_0)$. Then $\langle q, U_0\rangle = 0$.
>
> **Hint:** Use antisymmetry of $A$ at the diagonal argument.
>
> **Why needed:** It identifies the unique electric part and verifies its orthogonality constraint.
>
> > [!note]- Full proof
> > $\langle q, U_0\rangle = A(U_0, U_0)$. An antisymmetric bilinear form vanishes on the diagonal: $A(X, X) = -A(X, X)$ forces $A(X, X) = 0$, so $A(U_0, U_0) = 0$ and $\langle q, U_0\rangle = 0$. $\blacksquare$

> [!note]- Lemma 2: After subtracting the electric piece, the remainder vanishes on $U_0$
> **Statement:** Let $B := A - (q\otimes\underline{U_0} - \underline{U_0}\otimes q)$ with $q$ as in Lemma 1. Then $B(X, U_0) = 0$ for all $X$, i.e. $B$ is supported on the rest space.
>
> **Hint:** Compute $B(X, U_0)$ term by term, using $U_0\cdot U_0 = +1$ and $\langle q, U_0\rangle = 0$.
>
> **Why needed:** It shows the leftover is purely spatial — the magnetic part lives in the rest space.
>
> > [!note]- Full proof
> > Using $\langle\underline{U_0}, Y\rangle = U_0\cdot Y$,
> > $$(q\otimes\underline{U_0})(X, U_0) = \langle q, X\rangle\,(U_0\cdot U_0) = \langle q, X\rangle\,(+1) = \langle q, X\rangle,$$
> > $$(\underline{U_0}\otimes q)(X, U_0) = (U_0\cdot X)\,\langle q, U_0\rangle = (U_0\cdot X)\cdot 0 = 0.$$
> > Hence $(q\otimes\underline{U_0} - \underline{U_0}\otimes q)(X, U_0) = \langle q, X\rangle = A(X, U_0)$, so
> > $$B(X, U_0) = A(X, U_0) - A(X, U_0) = 0.$$
> > (This is the step where the mostly-minus sign $U_0\cdot U_0 = +1$ fixes the ordering: with the opposite sign one would need $\underline{U_0}\otimes q - q\otimes\underline{U_0}$.) By antisymmetry $B(U_0, Y) = 0$ too, so $B$ is determined by its restriction to $E_{U_0}\times E_{U_0}$. $\blacksquare$

> [!note]- Lemma 3: An antisymmetric form on the rest space is the cross product with a unique vector
> **Statement:** $B|_{E_{U_0}\times E_{U_0}}$ equals $\epsilon(U_0, \vec b, \cdot, \cdot)$ for a unique $\vec b\in E_{U_0}$; equivalently $B(X, Y) = (\vec b\times_{U_0}X)\cdot Y$ for $X, Y\in E_{U_0}$.
>
> **Hint:** In an orthonormal spatial basis, an antisymmetric $3\times 3$ matrix is dual to a vector via the rest-space Levi-Civita.
>
> **Why needed:** It produces the magnetic part as a rest-space vector and gives an explicit formula for it.
>
> > [!note]- Full proof
> > On the three-dimensional [[Thm - Euclidean Character of the Local Rest Space|Euclidean rest space]] with orthonormal basis $(e_1, e_2, e_3)$ (chosen right-handed, so $\epsilon(U_0, e_1, e_2, e_3) = 1$), the restriction $B|_{E_{U_0}}$ is an antisymmetric bilinear form, with matrix $B_{ij} = B(e_i, e_j)$ antisymmetric. Define
> > $$b^1 := B(e_2, e_3), \quad b^2 := B(e_3, e_1), \quad b^3 := B(e_1, e_2), \qquad \vec b := b^i e_i.$$
> > Then for $X = X^i e_i$, $Y = Y^i e_i$ in the rest space, expanding the antisymmetric $B$ gives the $3\times 3$ determinant
> > $$B(X, Y) = \begin{vmatrix} b^1 & X^1 & Y^1 \\ b^2 & X^2 & Y^2 \\ b^3 & X^3 & Y^3 \end{vmatrix} = \epsilon(U_0, \vec b, X, Y),$$
> > using $\epsilon_u(\vec b, X, Y) := \epsilon(U_0, \vec b, X, Y)$ and $\epsilon_u(e_1, e_2, e_3) = 1$. This is exactly the mixed (scalar triple) product, $B(X, Y) = (\vec b\times_{U_0}X)\cdot Y$. Uniqueness: if $\vec b'$ also worked, then $\epsilon(U_0, \vec b' - \vec b, X, Y) = 0$ for all $X, Y\in E_{U_0}$; since $\epsilon_u$ is non-degenerate on the rest space, $\vec b' - \vec b = 0$. And $U_0\cdot\vec b = 0$ since $\vec b\in E_{U_0}$ by construction. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness.** $A$ is a bilinear form on the four-dimensional $E$ and $U_0$ is unit timelike, so the rest space $E_{U_0} = U_0^\perp$ is three-dimensional and Euclidean ([[Thm - Euclidean Character of the Local Rest Space]]), and the Levi-Civita tensor $\epsilon$ is fixed by [[Def - Spacetime Orientation|orientation]]. All constructions below are well-defined.
>
> **Existence.** Define $q := A(\cdot, U_0)$. By Lemma 1, $\langle q, U_0\rangle = 0$. Set $B := A - (q\otimes\underline{U_0} - \underline{U_0}\otimes q)$. By Lemma 2, $B(X, U_0) = B(U_0, Y) = 0$, so $B$ is supported on the rest space. By Lemma 3, $B(X, Y) = \epsilon(U_0, \vec b, X, Y)$ for a unique $\vec b\in E_{U_0}$ (so $U_0\cdot\vec b = 0$). Since $\epsilon(U_0, \vec b, \cdot, \cdot)$ also vanishes whenever either argument is $U_0$ (repeated $U_0$ in the antisymmetric $\epsilon$), it agrees with $B$ on all of $E\times E$, not just the rest space. Therefore
> $$A = q\otimes\underline{U_0} - \underline{U_0}\otimes q + \epsilon(U_0, \vec b, \cdot, \cdot),$$
> with $\langle q, U_0\rangle = 0$ and $U_0\cdot\vec b = 0$.
>
> **Uniqueness.** Suppose $A = q'\otimes\underline{U_0} - \underline{U_0}\otimes q' + \epsilon(U_0, \vec b', \cdot, \cdot)$ with $\langle q', U_0\rangle = 0$, $U_0\cdot\vec b' = 0$. Contract the second argument with $U_0$: the magnetic term vanishes (repeated $U_0$), and by the Lemma 2 computation $q'\otimes\underline{U_0} - \underline{U_0}\otimes q'$ contracts to $q'$. So $A(\cdot, U_0) = q'$, forcing $q' = q$. Subtracting the (now equal) electric pieces leaves $\epsilon(U_0, \vec b', \cdot, \cdot) = \epsilon(U_0, \vec b, \cdot, \cdot)$, and non-degeneracy of $\epsilon$ on the rest space (Lemma 3) gives $\vec b' = \vec b$.
>
> **Degrees of freedom.** $q\in U_0^\perp$ has $3$ components, $\vec b\in U_0^\perp$ has $3$; total $6 = \dim\Lambda^2 E^*$, the number of independent entries of an antisymmetric $4\times 4$ matrix. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The electromagnetic field's electric and magnetic parts (electromagnetism).** Applying the decomposition to $F_{\mu\nu}$ relative to an observer's four-velocity $U_0$ yields $E_\mu = F_{\mu\nu}U_0^\nu$ (electric part) and $B^\mu$ (magnetic part); a boost to a new $U_0'$ produces the transformation law mixing $\mathbf E$ and $\mathbf B$. This is the same theorem with $A = F$, and it is the cleanest derivation of the observer-dependence of electric and magnetic fields ([[Special Relativity XXI — The Electromagnetic Field]]). The application is nonobvious because the four-rotation and the electromagnetic field look unrelated until both are seen as antisymmetric forms.

**Self-dual and anti-self-dual decomposition (differential geometry).** Over complex scalars, the electric and magnetic parts combine into $\mathbf E\pm i\mathbf B$, the self-dual and anti-self-dual parts of a two-form in four-dimensional Lorentzian signature, on which the Hodge star squares to $-1$. The real $3+3$ split of this theorem is the real form of that complex $3+3$ split, and it underlies the spinor/twistor treatment of the field. The application is surprising because the observer-relative decomposition becomes observer-*independent* once complexified.

**Angular momentum and spin of a system (relativistic mechanics).** The antisymmetric angular-momentum tensor $J^{\mu\nu}$ decomposes relative to an observer into a "mass-moment" vector (electric part, locating the centre of inertia) and a spin vector (magnetic part). Recognising $J^{\mu\nu}$ as yet another antisymmetric form to which this theorem applies is the route to the relativistic centre of inertia and the Pauli–Lubanski spin ([[Special Relativity XIV — Angular Momentum and Spin]]). The application is out-of-distribution because angular momentum is rarely first thought of as decomposable like a field.

---

# Bridges

- **[[Def - Local Frame and Four-Rotation]]** — the immediate application: with $A = \underline\Omega$ the four-rotation and the electric part pinned to $c\underline{A_0}$ by $\Omega(U_0) = cA_0$, the decomposition is the Fermi–Walker/spatial-rotation split of the frame's evolution. This is the theorem's reason for being in this chapter.

- **[[Def - The Electromagnetic Field Tensor]]** — applied to $F_{\mu\nu}$, the decomposition *defines* the electric and magnetic fields an observer measures; the names "electric part" and "magnetic part" are Gourgoulhon's deliberate foreshadowing. The four-rotation and the electromagnetic field are both antisymmetric forms, so they decompose identically.

- **[[Def - The Lorentz Group]]** and its Lie algebra — an antisymmetric bilinear form, with one index raised, is an element of $\mathfrak{so}(1,3)$; the electric/magnetic decomposition is the boost/rotation split of the Lorentz algebra relative to $U_0$. Boost generators are the electric part, rotation generators the magnetic part — see [[Special Relativity X — The Lorentz Group as a Lie Group]].

- **[[Def - Spacetime Orientation|The Levi-Civita tensor and the cross product]]** — the magnetic part appears through $\epsilon(U_0, \vec b, \cdot, \cdot)$, the rest-space cross product; the duality "antisymmetric $3\times 3$ block $\leftrightarrow$ vector $\vec b$" is the three-dimensional Hodge duality inherited from the spacetime $\epsilon$.

---

# Unlocked by This

> [!tip] The Fermi–Walker and Spatial-Rotation Split of the Frame *(from §6.3)*
> Applied to the four-rotation, this theorem produces the split $de_\alpha/d\tau = \Omega_{\mathrm{FW}}(e_\alpha) + \vec\omega\times_{U_0}e_\alpha$ of the [[Def - Local Frame and Four-Rotation|local frame]]'s evolution into an unavoidable four-acceleration tilt and a genuine spatial rotation, and hence the [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] and the characterisation of inertial observers.

> [!tip] Electric and Magnetic Fields Relative to an Observer *(from Electromagnetism)*
> Applied to the [[Def - The Electromagnetic Field Tensor|electromagnetic field tensor]], the theorem gives $\mathbf E$ and $\mathbf B$ as the electric and magnetic parts of $F$ for a chosen observer, $E_\mu = F_{\mu\nu}U_0^\nu$; the change of split under a boost is the transformation law of electric and magnetic fields, and the field invariants $F_{\mu\nu}F^{\mu\nu}\propto B^2 - E^2$, ${\star}F\!\cdot\!F\propto\mathbf E\cdot\mathbf B$ are the observer-independent combinations.

> [!tip] Self-Dual Two-Forms and E + iB *(from Tensor Calculus and Hodge Duality)*
> Complexifying the electric and magnetic parts into $\mathbf E\pm i\mathbf B$ gives the **self-dual and anti-self-dual** decomposition of two-forms in Lorentzian four-space, where the Hodge star satisfies ${\star}^2 = -1$ — the structure behind the spinor treatment of the field in [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality]].

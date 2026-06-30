---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Boosts as Hyperbolic Rotations"
  - "Def - Classification of Restricted Lorentz Transformations"
  - "Def - Subgroups and Components of the Lorentz Group"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, timelike $\Leftrightarrow X\cdot X > 0$. $SO^+(1,3)$ is the [[Def - Subgroups and Components of the Lorentz Group|restricted Lorentz group]]. We fix a unit future-timelike vector $e_0$ ($e_0\cdot e_0 = 1$), with rest space (orthogonal complement) $E_{e_0} = e_0^\perp$, a Euclidean three-space. A [[Def - Boosts as Hyperbolic Rotations|boost]] $S$ of plane $\Pi \ni e_0$ has Lorentz factor $\Gamma = \cosh\psi$ and rapidity $\psi$. A **spatial rotation** of $E_{e_0}$ is a restricted transformation fixing $e_0$, with matrix $\mathrm{diag}(1, H)$, $H \in SO(3)$. Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

---

# Statement

> **Theorem (Polar decomposition of the Lorentz group).** Fix a unit future-timelike vector $e_0 \in E$. Every restricted Lorentz transformation $\Lambda \in SO^+(1,3)$ can be written in a unique way as the product
> $$\Lambda = S \circ R,$$
> where $S$ is a Lorentz boost whose plane contains $e_0$, and $R$ is a spatial rotation whose plane (axis) lies in the rest space $E_{e_0} = e_0^\perp$ (equivalently, $R$ fixes $e_0$). Explicitly, $S$ is the unique boost carrying $e_0$ to $\Lambda(e_0)$: its plane is $\Pi = \mathrm{Span}(e_0, \Lambda(e_0))$ and its Lorentz factor is $\Gamma = e_0\cdot\Lambda(e_0)$, and $R = S^{-1}\Lambda$.
>
> This is the special-relativistic instance of the matrix **polar decomposition theorem**: $S$ is symmetric and positive-definite, $R$ is orthogonal ($R^{\mathsf T}R = I_4$).

---

# Motivation

A restricted Lorentz transformation does two things at once: it changes the velocity of the observer (the timelike direction) and it reorients the spatial frame. The polar decomposition is the clean separation of these two effects. Relative to a chosen observer $e_0$, it splits $\Lambda$ into a *pure change of velocity* — the boost $S$ that carries $e_0$ to its image — and a *pure spatial rotation* $R$ that does the leftover reorientation without touching the velocity. This is the single most useful structural fact about the Lorentz group, because almost every physical question ("how does this transformation change what the observer sees?") wants exactly this split.

The decomposition is *relative to a choice of $e_0$* — a different observer sees a different boost-rotation split of the same $\Lambda$ — and this relativity is not a defect but the source of the Thomas rotation. When you compose two boosts and ask "is the result a boost?", you are implicitly polar-decomposing relative to the initial observer, and the leftover rotation $R$ is the Thomas rotation. So the polar decomposition is the machine that *produces* the Thomas rotation, and understanding it is the prerequisite for understanding why boosts do not form a subgroup.

One should *expect* a result like this from linear algebra. The polar decomposition theorem says any invertible real matrix factors uniquely as a positive-definite symmetric matrix times an orthogonal one — geometrically, any linear map is a stretch (along orthogonal axes) followed by a rotation. A boost *is* a stretch (it stretches one null direction, shrinks the other, fixes the rest), symmetric and positive-definite; a spatial rotation *is* a rotation, orthogonal. So the polar decomposition of a Lorentz transformation is the general theorem read inside the Lorentz group, and its uniqueness has the same source — the positive symmetric factor is forced.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\Lambda \in SO^+(1,3)$ and an $e_0$ is chosen." The disguised sources are the situations that hand you these.

The first disguised source is **"a change of observer is given."** Any transformation relating the local frames of two observers is restricted, and the natural $e_0$ is the first observer's 4-velocity; the polar decomposition then splits the frame change into the boost taking the first observer's velocity to the second's, and the residual rotation of the spatial axes. The bridge is that a frame change is automatically in $SO^+(1,3)$. *Example problem:* decompose the transformation between two observers' frames into a boost and a rotation, isolating the spatial reorientation.

The second disguised source is **"a product of transformations whose boost-rotation content is wanted."** When $\Lambda = \Lambda_2\Lambda_1$ is a product (e.g. of two boosts), polar-decomposing relative to $e_0$ extracts the net boost and the net rotation; the rotation is the Thomas rotation when the factors are non-coplanar boosts. The bridge is that the product is restricted and the decomposition applies. *Example problem:* compose two boosts and extract the Thomas rotation as the $R$ factor of the polar decomposition.

The third disguised source is **"a restricted matrix with a marked timelike direction."** Whenever a $\Lambda \in SO^+(1,3)$ is given together with a preferred rest frame $e_0$ (the lab frame, say), the polar decomposition relative to $e_0$ is the natural normal form, separating the boost the lab observer would call "the velocity change" from the rotation "the orientation change." The bridge is the choice of $e_0$ as the lab 4-velocity. *Example problem:* given a generic Lorentz matrix in lab coordinates, read off the velocity it imparts and the rotation it applies.

**Targets (Output Amplification)**

The conclusion is "$\Lambda = S\circ R$, uniquely, with $S$ a boost and $R$ a rotation fixing $e_0$."

Combine the conclusion with **the composition of boosts**. Applying the decomposition to $\Lambda = \Lambda_2\Lambda_1$ for two boosts produces a boost $S$ and a rotation $R$; when the boosts are non-coplanar, $R \ne \mathrm{Id}$ is the Thomas rotation. The further result is the existence and computation of the Thomas rotation ([[Def - Thomas Rotation]]), the engine of Thomas precession. The combination is the central application of the chapter.

Combine the conclusion with **a second rotation on the other side**. Peeling off a rotation $R'$ before the boost to standardise its plane along a coordinate axis gives the $KAK$ decomposition $\Lambda = R(H)\,B[V]\,R(H')$ — rotation, standard boost, rotation. The further result is the Cartan decomposition of $SO^+(1,3)$, expressing every restricted transformation through two rotations and one rapidity. The combination is useful for reducing any computation to a boost along a fixed axis.

Combine the conclusion with **the simplicity of $SO^+(1,3)$**. The decomposition is unique *per element* but does not split the *group*, because the boosts do not form a subgroup — and they cannot, since $SO^+(1,3)$ is simple. The further result is the conceptual statement that the Thomas rotation is the obstruction to upgrading the element-wise polar split into a group-wise factorisation. The combination is the deepest "why" of the chapter: simplicity forbids the factorisation, so the Thomas rotation must appear.

---

# Why Is It True

The proof is short and the intuition is the linear-algebra polar decomposition.

**The boost is determined by where $e_0$ goes; the rotation is whatever is left.** That single sentence is the whole theorem. Set $e_0' = \Lambda(e_0)$, the image of the chosen observer's velocity. If $e_0' = e_0$, then $\Lambda$ fixes $e_0$, hence acts only on the rest space $E_{e_0}$ (a short argument: $\Lambda$ preserves orthogonality to $e_0$, so it maps $E_{e_0}$ to itself, and $E_{e_0}$ is a Euclidean three-space, so $\Lambda|_{E_{e_0}} \in SO(3)$); thus $\Lambda$ is a pure spatial rotation, $S = \mathrm{Id}$, $R = \Lambda$. If $e_0' \ne e_0$, then $e_0$ and $e_0'$ are two distinct future unit-timelike vectors, so they span a *timelike* plane $\Pi$, and there is a unique boost $S$ of plane $\Pi$ carrying $e_0$ to $e_0'$ (a boost is determined by its plane and its rapidity, and the rapidity is fixed by $\Gamma = e_0\cdot e_0'$). Now define $R = S^{-1}\Lambda$. Then $R(e_0) = S^{-1}(\Lambda e_0) = S^{-1}(e_0') = e_0$, so $R$ fixes $e_0$ and is therefore a pure spatial rotation by the first case. Hence $\Lambda = S\circ R$.

The uniqueness is forced the same way. Suppose also $\Lambda = S'\circ R'$ with $S'$ a boost and $R'$ a rotation fixing $e_0$. Then $S'(e_0) = S'(R'(e_0)) = \Lambda(e_0) = e_0'$, so $S'$ carries $e_0$ to $e_0'$ — but the boost with that property is unique (same plane $\mathrm{Span}(e_0, e_0')$, same Lorentz factor $\Gamma = e_0\cdot e_0'$), so $S' = S$, whence $R' = R$. **The mechanism is that the image $\Lambda(e_0)$ has exactly enough information to pin down the boost, leaving no freedom; everything else is rotation.**

The connection to the matrix polar decomposition makes this unsurprising. The general theorem factors any invertible $M = SR$ with $S = (MM^{\mathsf T})^{1/2}$ symmetric positive-definite and $R = S^{-1}M$ orthogonal. A boost in a semi-adapted basis has a *symmetric* matrix ($\Lambda^\alpha{}_\beta = \Lambda^\beta{}_\alpha$), and its eigenvalues $e^\psi, e^{-\psi}, 1, 1$ are all positive, so a boost *is* a symmetric positive-definite matrix; a spatial rotation has $\mathrm{diag}(1, H)$ with $H \in SO(3)$, hence $R^{\mathsf T}R = I_4$, so it *is* an orthogonal matrix. The Lorentz polar decomposition is therefore the matrix theorem applied inside $SO^+(1,3)$, and the abstract proof (read off the symmetric part, divide it out) is exactly the concrete one (read off the boost from $\Lambda(e_0)$, divide it out).

---

# What Makes This Hard

The proof itself is not hard; the conceptual hurdle is recognising that the *boost* is the symmetric-positive-definite factor and the *rotation* the orthogonal factor — the reverse of the naive guess, since one might expect the rotation (a "nicer" transformation) to be the positive part. The technical subtlety is that "orthogonal" for the rotation means $R^{\mathsf T}R = I_4$ (literal transpose), *not* the metric condition $R^{\mathsf T}\eta R = \eta$; both hold for a spatial rotation, but it is the former that makes the analogy with the linear-algebra theorem exact, and conflating them is the common error. A third subtlety is the order: the decomposition $\Lambda = S\circ R$ (rotate, then boost) differs from $\Lambda = R'\circ S'$ (boost, then rotate), and one must fix the order to have uniqueness.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Set $e_0' = \Lambda(e_0)$. If $e_0' = e_0$, $\Lambda$ is a rotation. Otherwise build the unique boost $S$ carrying $e_0$ to $e_0'$ (plane $\mathrm{Span}(e_0, e_0')$, factor $\Gamma = e_0\cdot e_0'$), and show $R = S^{-1}\Lambda$ fixes $e_0$, hence is a rotation. Uniqueness follows because $S$ is forced by $e_0'$.

**Subgoal decomposition:**

1. **A transformation fixing $e_0$ is a spatial rotation.** Show that if $\Lambda(e_0) = e_0$ then $\Lambda$ maps $E_{e_0}$ to itself and acts there as an element of $SO(3)$.
   - *Hint:* $\Lambda$ preserves orthogonality to $e_0$ (it preserves the scalar product and fixes $e_0$); $E_{e_0}$ is Euclidean.
   - *Why needed:* It is the base case and characterises the rotation factor.

2. **Two distinct future unit-timelike vectors span a timelike plane.** Show $\mathrm{Span}(e_0, e_0')$ is timelike when $e_0' \ne e_0$.
   - *Hint:* It contains timelike vectors ($e_0, e_0'$); non-collinearity rules out a null or spacelike degeneration.
   - *Why needed:* It hosts the boost $S$.

3. **There is a unique boost carrying $e_0$ to $e_0'$.** Build $S$ of plane $\mathrm{Span}(e_0, e_0')$ and Lorentz factor $\Gamma = e_0\cdot e_0'$.
   - *Hint:* A boost is determined by its plane and rapidity; $\Gamma = \cosh\psi = e_0\cdot e_0'$ fixes $\psi$.
   - *Why needed:* It is the boost factor $S$, and its uniqueness gives uniqueness of the decomposition.

4. **Divide out the boost.** Set $R = S^{-1}\Lambda$; show $R(e_0) = e_0$, hence $R$ is a rotation by Step 1, and $\Lambda = S\circ R$.
   - *Hint:* $R(e_0) = S^{-1}(\Lambda e_0) = S^{-1}(e_0') = e_0$.
   - *Why needed:* It completes the existence; uniqueness follows from $S'(e_0) = e_0' \Rightarrow S' = S$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A restricted transformation fixing $e_0$ is a spatial rotation
> **Statement:** If $\Lambda \in SO^+(1,3)$ and $\Lambda(e_0) = e_0$, then $\Lambda$ maps the rest space $E_{e_0}$ to itself and restricts there to a rotation in $SO(3)$.
>
> **Hint:** Preservation of orthogonality to $e_0$; Euclidean character of $E_{e_0}$.
>
> **Why needed:** It identifies the rotation factor and is the base case of the construction.
>
> > [!note]- Full proof
> > Let $v \in E_{e_0}$, so $e_0\cdot v = 0$. Then $e_0\cdot\Lambda(v) = \Lambda(e_0)\cdot\Lambda(v) = e_0\cdot v = 0$ (using $\Lambda(e_0) = e_0$ and that $\Lambda$ preserves the scalar product), so $\Lambda(v) \in E_{e_0}$. Hence $\Lambda$ maps $E_{e_0}$ to itself. On $E_{e_0}$ the induced metric is negative-definite (signature $(-,-,-)$), i.e. Euclidean up to overall sign, and $\Lambda|_{E_{e_0}}$ preserves it, so $\Lambda|_{E_{e_0}}$ is an orthogonal transformation of a three-dimensional Euclidean space; being part of a *proper* $\Lambda$ (and fixing $e_0$) it has determinant $+1$, so $\Lambda|_{E_{e_0}} \in SO(3)$. Thus $\Lambda$ is a spatial rotation, $\mathrm{diag}(1, H)$ with $H \in SO(3)$. $\blacksquare$

> [!note]- Lemma 2: The unique boost carrying one 4-velocity to another
> **Statement:** Given two distinct future unit-timelike vectors $e_0, e_0'$, there is a unique boost $S$ with $S(e_0) = e_0'$; its plane is $\mathrm{Span}(e_0, e_0')$ and its Lorentz factor is $\Gamma = e_0\cdot e_0' \ge 1$.
>
> **Hint:** A boost is determined by its plane and rapidity; the plane is forced and $\Gamma$ fixes the rapidity.
>
> **Why needed:** It constructs the boost factor and its uniqueness gives the theorem's uniqueness.
>
> > [!note]- Full proof
> > Since $e_0 \ne e_0'$ are distinct future unit-timelike vectors, they are non-collinear (collinearity with both unit and future would force $e_0' = e_0$), so $\Pi = \mathrm{Span}(e_0, e_0')$ is two-dimensional and contains the timelike vector $e_0$, hence is a timelike plane (by the reversed Cauchy–Schwarz inequality, $e_0\cdot e_0' \ge 1$ with equality iff $e_0' = e_0$, so the induced metric on $\Pi$ is Lorentzian $(+,-)$). A [[Def - Boosts as Hyperbolic Rotations|boost]] of plane $\Pi$ is determined by its rapidity $\psi$, and the condition $S(e_0) = e_0'$ fixes the kinematics: writing $e_0' = \Gamma(e_0 + V e_1)$ for the unit $e_1 \in \Pi \cap E_{e_0}$ along the projection of $e_0'$, the Lorentz factor is $\Gamma = e_0\cdot e_0'$ and the velocity $V = \tanh\psi$ is determined, hence $\psi$ and $S$ are unique. Existence: the boost of plane $\Pi$ and rapidity $\psi = \mathrm{arcosh}(e_0\cdot e_0')$ carries $e_0$ to $e_0'$ by construction. $\blacksquare$

> [!note]- Lemma 3: The boost is symmetric positive-definite, the rotation orthogonal
> **Statement:** In a semi-adapted basis the boost $S$ has a symmetric matrix with positive eigenvalues; the rotation $R$ has $R^{\mathsf T}R = I_4$.
>
> **Hint:** Boost matrix $\Lambda^\alpha{}_\beta = \Lambda^\beta{}_\alpha$ (symmetry), eigenvalues $e^{\pm\psi}, 1, 1 > 0$; rotation block $\mathrm{diag}(1, H)$ with $H$ orthogonal.
>
> **Why needed:** It identifies the decomposition with the linear-algebra polar decomposition $M = (\text{pos. sym.})(\text{orth.})$.
>
> > [!note]- Full proof
> > A boost of plane $\Pi \ni e_0$, written in a basis with $e_0$ in the plane (semi-adapted), has matrix $\Lambda^\alpha{}_\beta = \delta^\alpha_\beta + (\Gamma-1)\frac{V^\alpha V_\beta}{V^2} + \cdots$ which is symmetric, $\Lambda^\alpha{}_\beta = \Lambda^\beta{}_\alpha$ (this is a general property of boosts in semi-adapted bases). By [[Thm - Eigenvalues and Eigenvectors of a Lorentz Boost|the boost-eigenvalue theorem]] its eigenvalues are $e^{\psi}, e^{-\psi}, 1, 1$, all strictly positive, so $S$ is symmetric positive-definite. A spatial rotation $R$ fixing $e_0$ has matrix $\mathrm{diag}(1, H)$ with $H \in SO(3)$, so $R^{\mathsf T}R = \mathrm{diag}(1, H^{\mathsf T}H) = \mathrm{diag}(1, I_3) = I_4$: $R$ is orthogonal in the literal sense. Hence $\Lambda = S R$ is the polar decomposition of the matrix $\Lambda$, $S$ positive-definite symmetric, $R$ orthogonal. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix a unit future-timelike $e_0$ and let $\Lambda \in SO^+(1,3)$. Set $e_0' := \Lambda(e_0)$, a future unit-timelike vector.
>
> **Step 0 (well-posedness).** $e_0'$ is future unit-timelike because $\Lambda$ is orthochronous (maps future timelike to future timelike) and preserves the norm ($e_0'\cdot e_0' = e_0\cdot e_0 = 1$).
>
> **Case $e_0' = e_0$.** By Lemma 1, $\Lambda$ is a spatial rotation; take $S = \mathrm{Id}$, $R = \Lambda$. Then $\Lambda = S\circ R$ trivially.
>
> **Case $e_0' \ne e_0$.** By Lemma 2, there is a unique boost $S$ with $S(e_0) = e_0'$, plane $\mathrm{Span}(e_0, e_0')$, Lorentz factor $\Gamma = e_0\cdot e_0'$. Define $R := S^{-1}\Lambda \in SO^+(1,3)$. Then
> $$R(e_0) = S^{-1}(\Lambda(e_0)) = S^{-1}(e_0') = e_0,$$
> so by Lemma 1, $R$ is a spatial rotation fixing $e_0$. Hence $\Lambda = S\circ R$ with $S$ a boost whose plane contains $e_0$ and $R$ a rotation of $E_{e_0}$.
>
> **Uniqueness.** Suppose $\Lambda = S'\circ R'$ with $S'$ a boost (plane $\ni e_0$) and $R'$ a rotation fixing $e_0$. Then $S'(e_0) = S'(R'(e_0)) = \Lambda(e_0) = e_0'$, so $S'$ is a boost carrying $e_0$ to $e_0'$; by the uniqueness in Lemma 2, $S' = S$, and therefore $R' = S'^{-1}\Lambda = S^{-1}\Lambda = R$.
>
> **Polar identification.** By Lemma 3, $S$ is symmetric positive-definite and $R$ is orthogonal ($R^{\mathsf T}R = I_4$), so $\Lambda = SR$ is the polar decomposition of the matrix $\Lambda$ in the linear-algebra sense. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The matrix polar decomposition and the singular value decomposition.** Every invertible real matrix factors as $M = SR$ (positive-definite symmetric times orthogonal), and the symmetric part $S = (MM^{\mathsf T})^{1/2}$ has the singular values of $M$ as eigenvalues. The application is to recognise the Lorentz polar decomposition as this theorem inside $SO^+(1,3)$, with the boost's eigenvalues $e^{\pm\psi}, 1, 1$ the singular values; it is out-of-distribution because singular value decomposition is usually met in data analysis and numerical linear algebra, not relativity.

**Deformation gradients in continuum mechanics.** The deformation of an elastic body is described by a gradient $F = RU$ (rotation times stretch, the polar decomposition), separating rigid rotation from genuine strain $U$. The application maps the boost to the *stretch* and the rotation to the *rigid rotation*: a Lorentz transformation "stretches spacetime" (the boost) and "rotates the frame" (the rotation), exactly as a deformation stretches and rotates material. It is a surprising structural identity between relativistic kinematics and elasticity theory.

**Iwasawa and Cartan decompositions of Lie groups.** The $KAK$ refinement (rotation–boost–rotation) is the Cartan decomposition of $SO^+(1,3)$, $G = KAK$ with $K = SO(3)$ the maximal compact subgroup and $A$ the one-parameter boost subgroup; the related Iwasawa decomposition $G = KAN$ adds a nilpotent factor (the null rotations). The application is to see the polar decomposition as the first step toward the general structure theory of semisimple Lie groups, where every element factors through a compact part, an abelian part, and a nilpotent part. It battle-tests the decomposition against the general machinery of harmonic analysis on Lie groups.

---

# Bridges

- **[[Def - Thomas Rotation]]** — the polar decomposition is the machine that produces the Thomas rotation: applying it to the product of two non-coplanar boosts, the boost factor $S$ is the net boost (with velocity the relativistic sum) and the rotation factor $R$ is the Thomas rotation. Without the polar decomposition there would be no canonical way to say "the leftover rotation," and the Thomas rotation would have no definition.

- **The matrix polar decomposition** — this theorem is the linear-algebra polar decomposition $M = SR$ (symmetric positive-definite times orthogonal) specialised to $SO^+(1,3)$: the boost is the symmetric positive part (symmetric in a semi-adapted basis, positive eigenvalues $e^{\pm\psi}, 1, 1$), the rotation the orthogonal part ($R^{\mathsf T}R = I_4$). The general theorem factors any invertible matrix as a stretch followed by a rotation; here the stretch is the boost and the rotation is the spatial rotation, and the abstract proof (read off $S = (MM^{\mathsf T})^{1/2}$) is the concrete proof (read off $S$ from $\Lambda(e_0)$).

- **The $KAK$ Cartan decomposition** — peeling a rotation off each side of the boost to standardise its plane gives $\Lambda = R(H)\,B[V]\,R(H')$, the Cartan decomposition $G = KAK$ of $SO^+(1,3)$ with maximal compact $K = SO(3)$ and abelian $A$ the boosts along a fixed axis. This is the structure that reduces any Lorentz computation to a boost along a single direction, and it is the relativistic instance of the decomposition underlying spherical harmonics and the representation theory of semisimple groups. The polar decomposition is its one-sided version.

---

# Unlocked by This

> [!tip] Thomas Precession and the Spin–Orbit Coupling *(from Special Relativity XVI)*
> The polar decomposition applied to a continuous sequence of infinitesimal boosts — the situation of a particle accelerating along a curved path, hence boosted in continuously changing directions — produces a continuous accumulation of Thomas rotations, integrating to the **Thomas precession** of the particle's spin. For a particle in circular motion the precession rate is $\boldsymbol{\Omega}_T = \frac{\gamma^2}{\gamma+1}\mathbf{a}\times\mathbf{v}$, a purely kinematic precession arising entirely from the non-closure of boosts that this theorem makes precise. It is the origin of the factor of $\tfrac12$ in the spin–orbit coupling of atomic fine structure: the naive coupling overpredicts by two, and the Thomas precession supplies the compensating half. See [[Special Relativity XVI — Accelerated Observers]] and [[Def - Thomas Precession]].

---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group"
  - "Def - The Spinor Map and SL(2,C)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus. $\Lambda \in SO^+(1,3)$ is a restricted Lorentz transformation; $\mathscr{S} : SL(2,\mathbb{C}) \to SO^+(1,3)$ is the [[Def - The Spinor Map and SL(2,C)|spinor map]], so $\Lambda = \mathscr{S}(A)$ for some $A \in SL(2,\mathbb{C})$ by [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|surjectivity]]. A vector $X$ is **null** if $X\cdot X = \det\underline X = 0$ ($\underline X = x^\mu\sigma_\mu$ its [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|Hermitian form]]); a **null direction** is a one-dimensional space spanned by a null vector. $\mu \in \mathbb{C}$ denotes an eigenvalue of $A$, $U \in \mathbb{C}^2$ an eigenvector. Full registry on [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

---

# Statement

> **Theorem (existence of null eigenvectors).** Every restricted Lorentz transformation $\Lambda \in SO^+(1,3)$ admits a null eigenvector — equivalently, an invariant null direction — and the corresponding eigenvalue is strictly positive:
> $$ \exists\, X \neq 0,\ X\cdot X = 0 : \quad \Lambda(X) = |\mu|^2\, X, \qquad |\mu|^2 > 0, $$
> where $\mu$ is an eigenvalue of any $A \in SL(2,\mathbb{C})$ with $\mathscr{S}(A) = \Lambda$.

---

# Motivation

This theorem looks like a statement about real $4\times 4$ matrices, and proved that way it is awkward: a real matrix need not have real eigenvalues, and one would have to argue carefully about which eigenvectors are null. The point of the theorem is that the spinor map makes it *easy* — almost a triviality — because it converts a question about a real $4\times 4$ Lorentz matrix into a question about a complex $2\times 2$ matrix, and every complex matrix has an eigenvector by the fundamental theorem of algebra.

The result is the geometric foundation of the [[Special Relativity IX — The Lorentz Group, Structure and Classification|classification of Lorentz transformations]]. Gourgoulhon uses it as the starting point: knowing that every restricted Lorentz transformation fixes at least one null direction, one classifies them by how many null directions are fixed and how the transformation acts near them — yielding the four types (rotations, boosts, null rotations, four-screws). Without the guaranteed existence of one invariant null direction, that classification has no anchor.

It is also a beautiful illustration of the *use* of a covering map. The cover $SL(2,\mathbb{C})$ is "closer to algebra" — it is a group of complex matrices, where eigenvalue theory is clean — and the spinor map transports algebraic facts from the cover down to geometric facts about the base. The whole proof is: lift to $A$, use that $A$ has an eigenvector, push the eigenvector back down to a null vector. This is the template for many arguments that are hard upstairs and easy downstairs.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "$\Lambda$ is a restricted Lorentz transformation," and the recognition skill is seeing when an invariant null direction is what a problem needs.

The first disguised source is **"a Lorentz transformation must be classified."** Any task of identifying *which* of the four types a given $\Lambda$ is begins by locating its invariant null directions, and this theorem guarantees at least one exists to begin the search. The bridge is that the classification is organised by invariant null directions. *Example problem:* determine whether a given $\Lambda$ is a boost (two invariant null directions) or a null rotation (one).

The second disguised source is **"a light ray is preserved by a symmetry."** A null direction fixed by $\Lambda$ is a light ray whose direction every observer related by $\Lambda$ agrees on; physically this is a preferred light-like axis of the transformation. The bridge is "invariant null direction = preserved light ray." *Example problem:* find the light ray unchanged in direction by a boost (the forward and backward null directions along the boost axis).

The third disguised source is **"a $2\times 2$ complex matrix is given."** Whenever a Lorentz transformation appears already in $SL(2,\mathbb{C})$ form $A$, its eigenvector immediately supplies the null direction without any further work — the eigenvector $U$ builds the null vector via $H = UU^\dagger$. The bridge is the construction in the proof. *Example problem:* given $A$, write down the null eigenvector of $\mathscr{S}(A)$ directly.

**Targets (Output Amplification)**

The conclusion is "there is an invariant null direction, with positive eigenvalue."

Combine the conclusion with **counting the eigenvectors of $A$** to determine the *number* of invariant null directions. A diagonalisable $A$ with distinct eigenvalues has two independent eigenvectors, hence two invariant null directions (a boost or rotation); a non-diagonalisable $A$ (a single Jordan block) has one, hence one invariant null direction (a null rotation). The further result is the four-fold classification. The combination is nonobvious because the Jordan structure of a $2\times 2$ complex matrix controls the geometric type of a $4\times 4$ real Lorentz transformation. *Example:* distinguishing boosts from null rotations by the diagonalisability of $A$.

Combine the conclusion with **the positivity of the eigenvalue** to fix the time-orientation. Since $|\mu|^2 > 0$, the fixed null direction is not reversed in time-orientation — a restricted (orthochronous) Lorentz transformation maps a future null ray to a future null ray. The further result is consistency with orthochronicity. The combination is useful as a check that the transformation is genuinely in the identity component. *Example:* verifying that a candidate $\Lambda$ preserves the future light cone.

Combine the conclusion with **the reality of the characteristic polynomial of $\Lambda$** to pair up the null directions. The complex eigenvalues of the real matrix $\Lambda$ come in conjugate pairs, and the invariant null directions organise accordingly, which constrains the possible Jordan forms. *Example:* showing a four-screw has its two invariant null directions with eigenvalues $|\mu|^2$ and $|\mu|^{-2}$.

---

# Why Is It True

The mechanism is the cleanest possible use of the cover. A real Lorentz matrix is hard to find eigenvectors for; a complex $2\times 2$ matrix is not — its characteristic polynomial is a quadratic over $\mathbb{C}$, which always has a root. So lift $\Lambda$ to $A \in SL(2,\mathbb{C})$, take an eigenvalue $\mu$ (nonzero, since $\det A = 1 \neq 0$) and eigenvector $U$, and then *manufacture a null four-vector from $U$*.

The manufacturing step is the elegant part. From the eigenvector $U = (u,v)$ build the rank-one Hermitian matrix $H = UU^\dagger = \begin{pmatrix} |u|^2 & u\bar v \\ \bar u v & |v|^2\end{pmatrix}$. It has $\det H = |u|^2|v|^2 - |u\bar v|^2 = 0$, so the corresponding four-vector is null. And because $U$ is an eigenvector, $AU = \mu U$, the congruence $AHA^\dagger = A(UU^\dagger)A^\dagger = (AU)(AU)^\dagger = (\mu U)(\mu U)^\dagger = |\mu|^2 UU^\dagger = |\mu|^2 H$. So the null vector built from $U$ is fixed by $\Lambda$ up to the positive scale $|\mu|^2$ — an invariant null direction with positive eigenvalue.

**The whole theorem in one sentence: a $2\times 2$ complex matrix always has an eigenvector $U$, the rank-one matrix $UU^\dagger$ is a null four-vector, and the congruence multiplies it by $|\mu|^2 > 0$ — so the eigenvector of the lift is an invariant null direction of the Lorentz transformation.**

The positivity $|\mu|^2 > 0$ is automatic because $\mu \neq 0$ (a consequence of $\det A = 1$), and the squaring $|\mu|^2$ rather than $\mu$ appears precisely because the congruence has *two* factors of $A$ — the same doubling that produces half-angles elsewhere here produces the modulus-squared.

---

# What Makes This Hard

The difficulty is entirely in *not* attempting the proof on the real $4\times 4$ matrix, where one would struggle with complex eigenvalues and have to check nullity by hand. The non-obvious step is the construction $H = UU^\dagger$ from the eigenvector — recognising that an outer product is automatically rank-one, hence null, and that the eigenvector property survives the congruence as multiplication by $|\mu|^2$. The most common error is to expect the eigenvalue of $\Lambda$ to be $\mu$ rather than $|\mu|^2$, forgetting that the congruence applies $A$ twice; the modulus-squared is forced.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Lift $\Lambda$ to $A \in SL(2,\mathbb{C})$; take an eigenvalue $\mu \neq 0$ and eigenvector $U$ of $A$; form $H = UU^\dagger$, which is rank-one hence null; check $AHA^\dagger = |\mu|^2 H$, so the null vector is fixed up to the positive scale $|\mu|^2$.

**Subgoal decomposition:**

1. **Lift and find an eigenvector.** Write $\Lambda = \mathscr{S}(A)$; $A$ has an eigenvalue $\mu \neq 0$ with eigenvector $U$.
   - *Hint:* Surjectivity of the spinor map; the characteristic polynomial of $A$ has a root over $\mathbb{C}$; $\mu \neq 0$ since $\det A = 1$.
   - *Why needed:* Supplies the complex eigenvector that the real matrix lacks cleanly.

2. **Build a null vector.** Set $H = UU^\dagger$; show $\det H = 0$, so the four-vector is null.
   - *Hint:* A rank-one outer product has zero determinant.
   - *Why needed:* Converts the eigenvector into a null direction.

3. **Show it is invariant.** Compute $AHA^\dagger = |\mu|^2 H$.
   - *Hint:* $A(UU^\dagger)A^\dagger = (AU)(AU)^\dagger = (\mu U)(\mu U)^\dagger$.
   - *Why needed:* Proves the null direction is fixed, with positive eigenvalue $|\mu|^2$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A has a nonzero eigenvalue and eigenvector
> **Statement:** Every $A \in SL(2,\mathbb{C})$ has an eigenvalue $\mu \in \mathbb{C}$ with $\mu \neq 0$ and an eigenvector $U \in \mathbb{C}^2 \setminus \{0\}$.
>
> **Hint:** The characteristic polynomial $\det(A - \mu I)$ is a degree-two polynomial over $\mathbb{C}$, which has a root; $\mu = 0$ would force $\det A = 0$.
>
> **Why needed:** The complex eigenvector is the input the construction needs, and is what the real Lorentz matrix does not cleanly provide.
>
> > [!note]- Full proof
> > The characteristic polynomial $p(\mu) = \det(A - \mu I) = \mu^2 - (\mathrm{tr}\,A)\mu + \det A = \mu^2 - (\mathrm{tr}\,A)\mu + 1$ is a degree-two polynomial with complex coefficients. By the fundamental theorem of algebra it has at least one root $\mu \in \mathbb{C}$, which is an eigenvalue of $A$, with a corresponding nonzero eigenvector $U$ (any nonzero vector in the kernel of $A - \mu I$). Since the product of the two roots is $\det A = 1 \neq 0$, neither root is zero, so $\mu \neq 0$. $\blacksquare$

> [!note]- Lemma 2: H = UU† is Hermitian with zero determinant
> **Statement:** For any $U = (u,v) \in \mathbb{C}^2$, the matrix $H = UU^\dagger = \begin{pmatrix}|u|^2 & u\bar v \\ \bar u v & |v|^2\end{pmatrix}$ is Hermitian with $\det H = 0$, so the corresponding four-vector is null.
>
> **Hint:** $\det(UU^\dagger) = |u|^2|v|^2 - |u\bar v|^2$.
>
> **Why needed:** Converts the eigenvector into a null four-vector via the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|correspondence]] $\det\underline X = X\cdot X$.
>
> > [!note]- Full proof
> > $H^\dagger = (UU^\dagger)^\dagger = U^{\dagger\dagger}U^\dagger = UU^\dagger = H$, so $H$ is Hermitian. Its determinant is $|u|^2|v|^2 - (u\bar v)(\bar u v) = |u|^2|v|^2 - |u|^2|v|^2 = 0$. By the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|Hermitian-matrix correspondence]], the four-vector $X$ with $\underline X = H$ has $X\cdot X = \det H = 0$, i.e. is null. It is nonzero whenever $U \neq 0$. $\blacksquare$

> [!note]- Lemma 3: The congruence multiplies H by |μ|²
> **Statement:** If $AU = \mu U$ then $AHA^\dagger = |\mu|^2 H$, so the null vector $X$ satisfies $\Lambda(X) = |\mu|^2 X$.
>
> **Hint:** $A(UU^\dagger)A^\dagger = (AU)(AU)^\dagger$; substitute $AU = \mu U$.
>
> **Why needed:** Proves the null direction is invariant under $\Lambda$, with the eigenvalue $|\mu|^2 > 0$.
>
> > [!note]- Full proof
> > Using $(AU)^\dagger = U^\dagger A^\dagger$,
> > $$AHA^\dagger = A(UU^\dagger)A^\dagger = (AU)(AU)^\dagger = (\mu U)(\mu U)^\dagger = \mu\bar\mu\,UU^\dagger = |\mu|^2 H.$$
> > Translating through the [[Def - The Spinor Map and SL(2,C)|spinor map]], $\Lambda(X) = \mathscr{H}^{-1}(AHA^\dagger) = \mathscr{H}^{-1}(|\mu|^2 H) = |\mu|^2 X$. Since $\mu \neq 0$ (Lemma 1), $|\mu|^2 > 0$. The line spanned by $X$ is therefore an invariant null direction, mapped to itself with positive scale factor. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\Lambda \in SO^+(1,3)$. By [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|surjectivity of the spinor map]], choose $A \in SL(2,\mathbb{C})$ with $\mathscr{S}(A) = \Lambda$. By Lemma 1, $A$ has an eigenvalue $\mu \neq 0$ and eigenvector $U \neq 0$, $AU = \mu U$.
>
> Form $H = UU^\dagger$. By Lemma 2, $H$ is Hermitian with $\det H = 0$, so the four-vector $X$ defined by $\underline X = H$ is null and nonzero.
>
> By Lemma 3, $AHA^\dagger = |\mu|^2 H$, which under the spinor map reads $\Lambda(X) = |\mu|^2 X$. Thus $X$ is a null eigenvector of $\Lambda$ with eigenvalue $|\mu|^2 > 0$, and the line $\mathbb{R}X$ is an invariant null direction of $\Lambda$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fixed points of Möbius transformations (complex dynamics).** A Möbius transformation of the Riemann sphere has either one or two fixed points, and these are exactly the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|images on the celestial sphere]] of the invariant null directions of the corresponding Lorentz transformation. This theorem's "at least one invariant null direction" is the statement "every Möbius map has at least one fixed point," and the count (one vs. two) distinguishes parabolic (null rotation) from loxodromic/elliptic/hyperbolic (the other types). The application connects the classification of Lorentz transformations to the classification of Möbius maps.

**Perron–Frobenius and invariant cones (linear algebra).** The existence of an eigenvector inside a cone preserved by a linear map is a recurring theme — the Perron–Frobenius theorem guarantees a positive eigenvector for a matrix preserving the positive orthant. Here the light cone plays the role of the invariant cone, and the theorem guarantees an eigenvector on its boundary (a null vector). The application is the recognition that "invariant cone $\Rightarrow$ boundary eigenvector" is a general pattern, of which the light-cone case is a relativistic instance.

**Principal null directions of the Weyl tensor (general relativity).** In general relativity the Weyl curvature tensor at a point has up to four *principal null directions*, and their coincidence pattern (the Petrov classification) characterises the gravitational field algebraically. These are found by exactly the spinor method of this theorem applied to the curvature spinor: an eigenvalue problem for a $2\times 2$ (here symmetric) spinor object whose eigenvectors are null directions. The application is that the existence-of-null-eigenvectors logic scales up from Lorentz transformations to curvature, underlying the Petrov–Penrose classification of spacetimes.

---

# Bridges

- **[[Special Relativity IX — The Lorentz Group, Structure and Classification]]** — this theorem is the foundation of that chapter's classification. Counting the eigenvectors of the lift $A$ (two for diagonalisable, one for a Jordan block) counts the invariant null directions, and that count — together with whether the transformation acts on the transverse plane by rotation, boost, or shear — yields the four types: rotations and boosts (two invariant null directions), null rotations (one), and four-screws (two, with a twist). The vault's [[Thm - Invariant Null Direction of a Restricted Lorentz Transformation]] is the same result stated there.

- **[[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group]]** — surjectivity is the hypothesis this proof consumes: without a guaranteed $SL(2,\mathbb{C})$ preimage for every $\Lambda$, the complex-eigenvalue argument would not apply. This theorem is a showcase of the covering map as a computational tool, transporting the algebraic fact "every complex matrix has an eigenvector" down to the geometric fact "every Lorentz transformation fixes a null direction."

- **[[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)]]** — the invariant null directions are the *fixed points* of the induced Möbius transformation on the celestial sphere. A boost fixes the two null directions along its axis (the points the stars stream away from and toward); a null rotation fixes one (a parabolic Möbius map with a single fixed point). The theorem's existence statement is the Möbius "every fractional linear map has a fixed point."

---

# Unlocked by This

> [!tip] The Petrov–Penrose Classification *(from General Relativity)*
> The same spinor-eigenvalue method classifies the **Weyl curvature tensor** of a spacetime by its principal null directions: a $2\times 2$ symmetric spinor (the Weyl spinor $\Psi_{ABCD}$) has up to four null eigendirections, and their degeneracies give the **Petrov types** I, II, D, III, N, O. Type D (two double principal null directions) is the algebraically special class containing the Schwarzschild and Kerr black holes; see [[General Relativity I — Einstein's Equations and Schwarzschild]]. This theorem's "invariant null direction from a spinor eigenvector" is the kinematic seed of that curvature classification.

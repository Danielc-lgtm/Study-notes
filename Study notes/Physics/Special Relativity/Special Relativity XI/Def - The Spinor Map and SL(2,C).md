---
type: definition
subject: special-relativity
prereqs:
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
  - "Def - The Lorentz Group"
  - "Def - Lie Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use mostly-minus, $\eta = \mathrm{diag}(1,-1,-1,-1)$. A four-vector $X$ corresponds, via the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|Hermitian-matrix correspondence]] $\mathscr{H}$, to $\underline X = x^\mu\sigma_\mu \in \mathrm{Herm}(2,\mathbb{C})$ with $\det\underline X = X\cdot X$. We write $A^\dagger = \overline A^{\mathsf T}$ for the conjugate transpose, $\det A$ for the determinant, and $I = \sigma_0$ for the $2\times 2$ identity. $SO^+(1,3)$ is the restricted (proper orthochronous) Lorentz group (Gourgoulhon's $SO_o(3,1)$), the identity component of the [[Def - The Lorentz Group|Lorentz group]]. Full registry on [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

This is a compound page: it defines two interlocking notions — the **special linear group** $SL(2,\mathbb{C})$ and the **spinor map** $\mathscr{S}$ it carries onto the restricted Lorentz group — because the spinor map is what makes $SL(2,\mathbb{C})$ relevant to relativity and neither is fully usable without the other.

---

# Axiom Motivation

By the end of [[Special Relativity X — The Lorentz Group as a Lie Group|the Lie-group chapter]] we know the restricted Lorentz group $SO^+(1,3)$ is a six-dimensional Lie group and that its complexified Lie algebra splits as $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$. That splitting is a strong hint that a group built from $2\times 2$ complex matrices is lurking, but a Lie-algebra hint is not a group, and the question this page answers is: *which* group of $2\times 2$ complex matrices is the Lorentz group, and how exactly does it act on spacetime?

The desideratum is a group $G$ of $2\times 2$ complex matrices together with a homomorphism $\mathscr{S} : G \to SO^+(1,3)$ that is explicit, surjective, and as close to an isomorphism as the topology allows. The action on spacetime should preserve the interval, since that is what "Lorentz" means.

Start from the correspondence $\underline X = x^\mu\sigma_\mu$ and ask what linear operations on $2\times 2$ Hermitian matrices preserve the interval, which is now the determinant. The most natural determinant-multiplying operation on matrices is *congruence*: $H \mapsto AHA^\dagger$ for a fixed matrix $A$. Two features recommend it above all alternatives. First, it automatically preserves Hermiticity — $(AHA^\dagger)^\dagger = AH^\dagger A^\dagger = AHA^\dagger$ — so it stays inside $\mathrm{Herm}(2,\mathbb{C})$ and hence corresponds to a genuine real four-vector transformation; a one-sided multiplication $H \mapsto AH$ would not. Second, its effect on the determinant is multiplicative and transparent: $\det(AHA^\dagger) = \det A\,\det H\,\overline{\det A} = |\det A|^2\det H$.

This last formula dictates the group. To preserve the determinant — the interval — for every $H$, we need $|\det A|^2 = 1$, i.e. $|\det A| = 1$. One could stop there, with the group $\{A : |\det A| = 1\}$, but this is larger than necessary and not connected in the right way: writing $\det A = e^{i\theta}$, the phase $\theta$ contributes nothing to the action $AHA^\dagger$ because $A$ and $e^{-i\theta/2}A$ give the same congruence. Quotienting out this phase redundancy, every congruence is implemented by an $A$ with $\det A$ a positive real, and rescaling makes $\det A = 1$. So the *efficient* group, the one with no redundancy beyond a discrete sign, is
$$SL(2,\mathbb{C}) = \{A \in \mathrm{Mat}(2,\mathbb{C}) : \det A = 1\}.$$
Why determinant exactly one, not $|\det A| = 1$? Because the residual phase freedom in $|\det A| = 1$ is a continuous redundancy (a whole circle of matrices implementing each Lorentz transformation), whereas $SL(2,\mathbb{C})$ has only the discrete redundancy $A \leftrightarrow -A$ (since $(-A)H(-A)^\dagger = AHA^\dagger$). The discrete redundancy is irreducible — it is the double cover — and it is the physically meaningful one; the continuous redundancy is pure waste.

What if we dropped the requirement that $A$ be invertible, or allowed $\det A = 0$? Then the congruence $AHA^\dagger$ could collapse the determinant to zero, mapping a timelike vector to a null one — not a Lorentz transformation, which must be invertible and interval-preserving. Invertibility ($\det A \neq 0$) is forced, and the normalisation to $\det A = 1$ is the canonical representative. What if we required $A$ unitary, $A^\dagger = A^{-1}$? That is allowed and gives a *subgroup*, $SU(2)$, but it is too small — unitary $A$ fixes the time direction and so produces only spatial rotations ([[Thm - The Spinor Map SU(2) to SO(3)]]). To reach the boosts we need the non-unitary elements of $SL(2,\mathbb{C})$, which is why the full special linear group, not its unitary subgroup, is the cover of the full restricted Lorentz group.

---

# The Definition

The **special linear group** is
$$
SL(2,\mathbb{C}) \;=\; \{\,A \in \mathrm{Mat}(2,\mathbb{C}) : \det A = 1\,\},
$$
a real Lie group of dimension $6$ (a complex $2\times 2$ matrix has $8$ real parameters; $\det A = 1$ is one complex, hence two real, constraints). It is a group under matrix multiplication, with inverse $A^{-1} = \begin{pmatrix} \delta & -\beta \\ -\gamma & \alpha\end{pmatrix}$ for $A = \begin{pmatrix}\alpha & \beta \\ \gamma & \delta\end{pmatrix}$ (using $\det A = \alpha\delta - \beta\gamma = 1$).

For $A \in SL(2,\mathbb{C})$, define the **congruence action** on Hermitian matrices
$$
\Phi_A : \mathrm{Herm}(2,\mathbb{C}) \to \mathrm{Herm}(2,\mathbb{C}), \qquad \Phi_A(\underline X) = A\,\underline X\,A^\dagger.
$$
It is well-defined (Hermitian-preserving) and linear, and $\det\big(\Phi_A(\underline X)\big) = |\det A|^2\det\underline X = \det\underline X$, so it preserves the interval. Transporting it through the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|correspondence]] $\mathscr{H}$ defines a linear map of Minkowski space,
$$
\Lambda_A \;:=\; \mathscr{H}^{-1}\circ\Phi_A\circ\mathscr{H} \;:\; \mathbb{R}^{1,3} \to \mathbb{R}^{1,3},
$$
which preserves $X\cdot X$ and is therefore a Lorentz transformation. The **spinor map** is
$$
\boxed{\;\mathscr{S} : SL(2,\mathbb{C}) \longrightarrow SO^+(1,3), \qquad \mathscr{S}(A) = \Lambda_A.\;}
$$
Its image lies in the *restricted* Lorentz group: $\Lambda_A$ is **orthochronous** because its time–time component is
$$
(\Lambda_A)^0{}_0 = \tfrac12\big(|\alpha|^2 + |\beta|^2 + |\gamma|^2 + |\delta|^2\big) > 0,
$$
and **proper** because $\det\Lambda_A = (\det A)^2\,(\overline{\det A})^2 = 1$. The map $\mathscr{S}$ is a **group homomorphism**, $\mathscr{S}(AB) = \mathscr{S}(A)\mathscr{S}(B)$, since $\Phi_A\circ\Phi_B = \Phi_{AB}$ (the computation $A(BHB^\dagger)A^\dagger = (AB)H(AB)^\dagger$ uses $(AB)^\dagger = B^\dagger A^\dagger$).

Explicitly, the matrix of $\Lambda_A$ in the standard basis is obtained by acting on each $\sigma_\nu$ and re-expanding: $A\sigma_\nu A^\dagger = (\Lambda_A)^\mu{}_\nu\,\sigma_\mu$, so column $\nu$ of $\Lambda_A$ is read off from the components of $A\sigma_\nu A^\dagger$ in the Pauli basis, $(\Lambda_A)^\mu{}_\nu = \tfrac12\mathrm{tr}\big(\sigma_\mu A\sigma_\nu A^\dagger\big)$.

---

# Categorical / Structural Definition

The cleanest framing is functorial. The [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|correspondence]] $\mathscr{H}$ is an isomorphism of quadratic spaces $(\mathbb{R}^{1,3}, X\cdot X) \cong (\mathrm{Herm}(2,\mathbb{C}), \det)$. The functor "isometry group of a quadratic space" sends this isomorphism to an isomorphism of groups $O(1,3) \cong \mathrm{Aut}(\mathrm{Herm}(2,\mathbb{C}),\det)$. The congruence action gives a homomorphism $SL(2,\mathbb{C}) \to \mathrm{Aut}(\mathrm{Herm}(2,\mathbb{C}),\det)$, $A \mapsto \Phi_A$, whose image is (after restricting to the identity component) all of $SO^+(1,3)$, and the spinor map is the composite
$$SL(2,\mathbb{C}) \xrightarrow{\;A\mapsto\Phi_A\;} \mathrm{Aut}(\mathrm{Herm}(2,\mathbb{C}),\det) \xrightarrow{\;\mathscr{H}_*\;} O(1,3).$$

There is a more abstract way to see $SL(2,\mathbb{C})$ that explains why it is the *cover* and not merely a group mapping onto $SO^+(1,3)$. A topological group $G$ together with a covering homomorphism $G \to H$ is determined, among connected covers, by a subgroup of $\pi_1(H)$. The universal cover corresponds to the trivial subgroup and is the unique simply connected cover. Here $\pi_1(SO^+(1,3)) = \mathbb{Z}/2$, so the universal cover is a two-fold cover, and $SL(2,\mathbb{C})$ — being simply connected, as shown in [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group]] — *is* that universal cover. This is the structural content of "$SL(2,\mathbb{C})$ is the spin group $\mathrm{Spin}(1,3)$": the universal cover of the restricted Lorentz group, the home of the spinor representations that do not descend to the base.

---

# Relate to Other Fields / Compression

In the language of [[Def - Pin and Spin Groups|spin groups]], $SL(2,\mathbb{C}) = \mathrm{Spin}^+(1,3)$ is the identity component of the spin group of Minkowski space, sitting inside the [[Def - Clifford Algebra|Clifford algebra]] $\mathrm{Cl}(1,3)$, and the spinor map $\mathscr{S}$ is the restriction to it of the universal *twisted adjoint* covering $\mathrm{Spin}(1,3) \to SO(1,3)$ of [[Thm - Spin(n) is the Double Cover of SO(n)]]. The congruence action $\underline X \mapsto A\underline X A^\dagger$ is the four-dimensional spacetime version of the conjugation action by which a spin group rotates vectors.

For a complex-analyst the same group is the group of holomorphic automorphisms of the Riemann sphere: $SL(2,\mathbb{C})$ acts on $\mathbb{C}\mathrm{P}^1$ by Möbius transformations, and $\mathscr{S}$ is the realisation of that action as the Lorentz group acting on the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|celestial sphere]].

**True name:** the operational characterisation is "*$A$ acts on spacetime by sandwiching the Hermitian matrix: $\underline X \mapsto A\underline X A^\dagger$*." Two factors of $A$, a dagger on the right; this single rule generates the entire homomorphism, the determinant-preservation, the orthochronous-and-proper conclusion, and the half-angle structure downstream. When computing $\Lambda_A$ you never invoke the abstract definition — you compute $A\sigma_\nu A^\dagger$ for the four $\sigma_\nu$.

---

# Examples / Corollaries

**Is an instance — the identity and its negative.** $A = I$ gives $\Phi_I(\underline X) = \underline X$, so $\mathscr{S}(I) = \mathrm{Id}$. Crucially $A = -I$ gives $\Phi_{-I}(\underline X) = (-I)\underline X(-I)^\dagger = \underline X$, so $\mathscr{S}(-I) = \mathrm{Id}$ as well — the two-to-one-ness in its simplest form.

**Is an instance — a $z$-boost.** $A = \mathrm{diag}(e^{\psi/2}, e^{-\psi/2})$ has $\det A = 1$ and is Hermitian. Acting on $\underline X = \begin{pmatrix}t+z & x-iy \\ x+iy & t-z\end{pmatrix}$ gives $A\underline X A^\dagger = \begin{pmatrix} e^{\psi}(t+z) & x-iy \\ x+iy & e^{-\psi}(t-z)\end{pmatrix}$, so $t' + z' = e^{\psi}(t+z)$ and $t' - z' = e^{-\psi}(t-z)$, i.e. $t' = \cosh\psi\,t + \sinh\psi\,z$, $z' = \sinh\psi\,t + \cosh\psi\,z$ — the boost of rapidity $\psi$ along $z$. (The sign of $\psi$ in the boost is a passive/active convention; Tong's $A = \mathrm{diag}(e^{-\psi/2},e^{+\psi/2})$ gives the inverse boost.)

**Is an instance — a $z$-rotation.** $A = \mathrm{diag}(e^{i\theta/2}, e^{-i\theta/2})$ is unitary with $\det A = 1$. Acting on $\underline X$ leaves the diagonal entries (and hence $t, z$) untouched and multiplies the off-diagonal $x - iy$ by $e^{i\theta}$, rotating $(x,y)$ by angle $\theta$ — a spatial rotation about $z$, fixing the time axis.

**Is NOT an instance — a matrix with $\det A \neq 1$.** $A = \mathrm{diag}(2, 1)$ has $\det A = 2$. Its congruence multiplies the interval by $|\det A|^2 = 4$, so it dilates spacetime rather than preserving it; it is not in $SL(2,\mathbb{C})$ and $\mathscr{S}$ is not defined on it. Rescaling to $A/\sqrt2 = \mathrm{diag}(\sqrt2, 1/\sqrt2)$ restores $\det = 1$ and gives a genuine boost.

**Corollary — the image is in the identity component.** Because $(\Lambda_A)^0{}_0 > 0$ and $\det\Lambda_A = 1$ for every $A$, no $\mathscr{S}(A)$ ever reverses time or parity; the image lies entirely in $SO^+(1,3)$. The discrete reflections (time reversal, parity) are *not* in the image, which is why $\mathscr{S}$ covers only the restricted group, not the full $O(1,3)$.

**Corollary — composition is multiplication.** Since $\mathscr{S}$ is a homomorphism, composing two Lorentz transformations corresponds to multiplying their $SL(2,\mathbb{C})$ matrices: $\Lambda_A\Lambda_B = \Lambda_{AB}$. This is what makes the matrix picture computationally efficient — a $4\times 4$ Lorentz product becomes a $2\times 2$ complex product.

**Calibration check.** If you have understood this page you should be able to: (1) verify directly that $A = \begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$ is in $SL(2,\mathbb{C})$ and compute its action on $\sigma_0 = I$, finding $A\sigma_0 A^\dagger = \begin{pmatrix}2 & 1 \\ 1 & 1\end{pmatrix}$ (a null rotation in disguise); (2) explain why $A$ and $-A$ always give the same $\Lambda$; (3) state why a unitary $A$ produces a rotation and a Hermitian $A$ a boost, in one sentence each.

---

# Unlocked by This

> [!tip] The Double Cover and Spin *(from §11.1)*
> The kernel of $\mathscr{S}$ is $\{\pm I\}$, so $SO^+(1,3) \cong SL(2,\mathbb{C})/\{\pm I\}$ ([[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group]]). The surplus sign — invisible to four-vectors, which never distinguish $A$ from $-A$ — is exactly what spinors see, and is the formal origin of half-integer spin.

> [!tip] The Lie Algebra Isomorphism *(from §11.2)*
> Differentiating $\mathscr{S}$ at the identity gives a Lie-algebra isomorphism $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(1,3)$ ([[Def - Lie Algebra sl(2,C) and the Exponential Map]]), realising concretely the complexified splitting $\mathfrak{so}(1,3)_{\mathbb C}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ of [[Special Relativity X — The Lorentz Group as a Lie Group|the previous chapter]].

> [!tip] Wigner's Classification of Particles *(from Quantum Field Theory)*
> Once Lorentz transformations are $2\times 2$ matrices, the **representations of the Poincaré group** — the quantum-mechanical notion of an elementary particle — are built from representations of $SL(2,\mathbb{C})$ labelled by a pair of spins, together with the mass and spin Casimirs of [[Def - Casimir Invariants of the Poincaré Group|the Poincaré group]]. The spinor map is the reason "spin" is a label of a group representation; see [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

---
type: definition
subject: spinors
prereqs:
  - "Def - The Pauli Matrices"
  - "Def - Vector Space"
tags: [geometry, spinors, lie-groups, quantum-mechanics]
---

# Notation

$SU(2)$ is the group of $2 \times 2$ complex unitary matrices with determinant $1$: $u \in SU(2)$ iff $u^\dagger u = I$ and $\det u = 1$. Its Lie algebra is $\mathfrak{su}(2)$, the space of traceless anti-Hermitian $2 \times 2$ complex matrices. A **(two-component) spinor** is an element $\psi \in \mathbb{C}^2$; we write its components as $\psi = (\psi^1, \psi^2)^T$ or $\psi = (\psi_\uparrow, \psi_\downarrow)^T$ (the "spin up / spin down" notation in physics). The standard inner product on $\mathbb{C}^2$ is $\langle\psi, \phi\rangle = \psi^\dagger \phi = \bar\psi^1\phi^1 + \bar\psi^2\phi^2$, which $SU(2)$ preserves (by definition of unitarity).

---

# Axiom Motivation

The phrase "$SU(2)$ acts on spinors" is a slogan for the obvious thing: every group has a *fundamental representation* on the vector space it acts on by definition. $SU(2)$ is defined as a subgroup of $GL(\mathbb{C}^2)$, so it acts on $\mathbb{C}^2$ by left multiplication. What makes the action *spinor*-shaped, as opposed to vector-shaped, is the relationship between $SU(2)$ and the rotation group $SO(3)$: $SU(2)$ is the double cover of $SO(3)$ (see [[Thm - SU(2) is the Double Cover of SO(3)]]), so the action of $SU(2)$ on $\mathbb{C}^2$ is *not* an action of $SO(3)$ — half the elements of $SU(2)$ correspond to the same rotation, but they act differently on the spinor.

The desiderata are: a vector space $V$ and a representation $\rho: SU(2) \to GL(V)$ such that (a) $V$ has the smallest possible dimension allowing a faithful representation; (b) under the cover $SU(2) \to SO(3)$, the action of $V$ "remembers" the cover — i.e., $\rho(-I) \neq \rho(I)$, so a $2\pi$ rotation in $SO(3)$ does *not* act trivially on $V$. This last condition is the spinorial signature: a representation of $SU(2)$ descends to $SO(3)$ iff $-I$ acts trivially.

The vector space satisfying these desiderata, in the smallest faithful instance, is $V = \mathbb{C}^2$ with $\rho$ the fundamental representation: $u \cdot \psi = u\psi$. To see it satisfies (b): $\rho(-I)\psi = -\psi$, which is non-trivial, so the $4\pi$-periodicity holds. To see (a): there is no nontrivial $1$-dimensional representation of $SU(2)$ (because $SU(2)$ is simple), so $\mathbb{C}^2$ is the smallest faithful one.

Why call the elements of $\mathbb{C}^2$ "spinors" rather than just "vectors"? The terminology comes from physics, where $\psi \in \mathbb{C}^2$ describes the *spin state* of an electron — the two components $\psi^\uparrow$ and $\psi^\downarrow$ are the amplitudes for finding the electron with spin up or down along a chosen axis. The mathematical content of the word is: a spinor is *not* a vector in $\mathbb{R}^3$, but it transforms covariantly when an $\mathbb{R}^3$-rotation is performed, in the way prescribed by the $SU(2) \to SO(3)$ cover. The factor of $\tfrac{1}{2}$ in the relation $u = \exp(-i\tfrac{\theta}{2}\vec\sigma\cdot\hat n) \in SU(2)$ corresponding to $R = R(\hat n, \theta) \in SO(3)$ is why electrons are said to have **spin $\tfrac{1}{2}$**: a vector picks up phase $e^{-i\theta}$ under a rotation by $\theta$, but a spinor picks up only $e^{-i\theta/2}$.

What if we strengthened the requirement and asked $\rho(-I) = +I$ (i.e., the representation descends to $SO(3)$)? Then we are looking at *integer-spin* representations: the trivial representation (spin $0$), the 3-dimensional adjoint representation (spin $1$), the 5-dimensional symmetric-traceless rank-2 tensor representation (spin $2$), and so on. These exist on $SO(3)$ already and are not spinorial. The spin-$\tfrac{1}{2}$, $\tfrac{3}{2}$, $\tfrac{5}{2}$, ... representations exist only on $SU(2)$; they are the spinor representations. The smallest is $\mathbb{C}^2$, our object of study.

---

# The Definition

The **fundamental (spinor) representation** of $SU(2)$ on $\mathbb{C}^2$ is the action by matrix multiplication:
$$SU(2) \times \mathbb{C}^2 \to \mathbb{C}^2, \quad (u, \psi) \mapsto u \cdot \psi := u\psi.$$
The elements $\psi \in \mathbb{C}^2$ transforming this way are called **(two-component) spinors** or **Pauli spinors**.

Explicitly, a rotation of $\mathbb{R}^3$ by angle $\theta$ about the unit axis $\hat n$ corresponds (under the covering map $SU(2) \to SO(3)$) to the two $SU(2)$ elements
$$u_\pm(\hat n, \theta) = \pm\exp\!\left(-\tfrac{i\theta}{2}\,\vec\sigma\cdot\hat n\right) = \pm\!\left(\cos\tfrac{\theta}{2}\,I - i\sin\tfrac{\theta}{2}\,\vec\sigma\cdot\hat n\right),$$
and acts on a spinor $\psi$ by $\psi \mapsto u_\pm \psi$. Both $u_+$ and $u_-$ project to the same rotation in $SO(3)$, but they differ by a sign on $\psi$: under a continuous rotation by $\theta \in [0, 2\pi]$, $u(\hat n, \theta)$ traces a path in $SU(2)$ from $+I$ to $-I$.

---

# Categorical / Structural Definition

The fundamental representation $\rho_{\mathrm{fund}}: SU(2) \to U(\mathbb{C}^2)$ is the inclusion of $SU(2)$ as a subgroup of $U(2)$. It is one of an infinite family of irreducible representations of $SU(2)$, indexed by *spin* $s \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$. The spin-$s$ representation has dimension $2s + 1$ and can be realized on the space of homogeneous polynomials of degree $2s$ in two complex variables $z_1, z_2$, with $SU(2)$ acting by linear change of variables. The spin-$\tfrac{1}{2}$ representation is $\mathbb{C}^2$ itself (linear polynomials), spin-$1$ is the symmetric square $\mathrm{Sym}^2(\mathbb{C}^2)$ (quadratic polynomials), and so on. **Peter–Weyl theorem** for $SU(2)$: the regular representation of $SU(2)$ on $L^2(SU(2))$ decomposes as
$$L^2(SU(2)) = \widehat{\bigoplus}_{s \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}} V_s \otimes V_s^*$$
where $V_s$ is the spin-$s$ irrep, each appearing with multiplicity $\dim V_s = 2s + 1$. The spinor representation is the *smallest* nontrivial irrep, and is the **generator of the representation ring** of $SU(2)$ in a precise sense (every other irrep arises as a subrep of a tensor power of $V_{1/2}$).

The categorical statement is: $SU(2)$ is a **simply connected compact Lie group** with $\pi_1 = 0$, so by the Lie correspondence every representation of $\mathfrak{su}(2)$ lifts to a representation of $SU(2)$. The half-integer spin representations of $\mathfrak{su}(2)$ are *legitimate* representations of $SU(2)$ but *fail* to descend to representations of $SO(3) = SU(2)/\{\pm I\}$ — they are precisely those representations where $-I \in SU(2)$ acts as $-I$ rather than $+I$. The spinor representation $\mathbb{C}^2$ is the prototypical such representation.

---

# Relate to Other Fields / Compression

**True name:** A spinor is a *vector in the fundamental representation of $SU(2)$*, equivalently the *minimal faithful representation of the double cover of the rotation group*. The word "spinor" emphasizes the contrast with "vector" (which transforms under $SO(3)$): a spinor transforms under $SU(2)$ and picks up a sign under $2\pi$ rotations. The factor of $\tfrac{1}{2}$ in $u = \exp(-i\tfrac{\theta}{2}\vec\sigma\cdot\hat n)$ corresponding to $R = R(\hat n, \theta) \in SO(3)$ is why electrons carry **spin $\tfrac{1}{2}$**: rotation phases on spinors are half of rotation phases on vectors.

The same construction works at every level of the spinor hierarchy. Replace $SU(2) \to SO(3)$ with $\mathrm{SL}(2, \mathbb{C}) \to SO^+(3, 1)$ and get **Weyl spinors** (two-component complex spinors transforming under the Lorentz group); see [[Def - Weyl Spinor]]. Replace with $\mathrm{Spin}(n) \to SO(n)$ and get **(higher-dimensional) spinors** on $\mathbb{R}^n$; see [[Def - Pin and Spin Groups]]. In each case the spinor representation is the fundamental representation of the cover group, and it fails to descend to the base group.

Compared to other fields: the $SU(2)$-action on $\mathbb{C}^2$ is the model case for *all* group actions on representation spaces. The structure of $\mathbb{C}^2$ as an $SU(2)$-module is what makes Hopf-fibration topology ($S^3 \to S^2$) work — see [[Ex - SU(2) is Diffeomorphic to S^3]]. The action also underlies the **Bloch sphere** picture of qubit states in quantum information: rotations of a qubit state on the Bloch sphere are $SU(2)$ rotations acting on $\psi \in \mathbb{C}^2$.

---

# Examples / Corollaries

**Example 1: Spin-up state and its rotation.** The "spin up along $z$" state is $\psi_\uparrow = (1, 0)^T$, the first standard basis vector. Under the $SU(2)$ rotation $u_z(\theta) = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$ corresponding to rotation by $\theta$ about the $z$-axis, $\psi_\uparrow \mapsto e^{-i\theta/2}\psi_\uparrow$: only a phase, since $\psi_\uparrow$ is an eigenvector of $\sigma_3$.

**Example 2: A $2\pi$ rotation changes the sign of $\psi$.** Under any rotation by $\theta = 2\pi$, $u(\hat n, 2\pi) = \exp(-i\pi\vec\sigma\cdot\hat n) = \cos\pi I - i\sin\pi\vec\sigma\cdot\hat n = -I$. So $\psi \mapsto -\psi$ for every spinor $\psi$. This is the famous "spinors change sign under $2\pi$ rotations" — the geometric content of $\pi_1(SO(3)) = \mathbb{Z}/2$.

**Example 3: Rotation of a generic spinor.** Take $\psi = \tfrac{1}{\sqrt 2}(1, 1)^T$ — the "spin right" state, i.e., the eigenvector of $\sigma_1$ with eigenvalue $+1$. Under a rotation about $z$ by $\theta = \pi$, $u_z(\pi) = \mathrm{diag}(e^{-i\pi/2}, e^{i\pi/2}) = -i\sigma_3$, so $\psi \mapsto -i\sigma_3\psi = -i\tfrac{1}{\sqrt 2}(1, -1)^T$. This is (up to a phase) the "spin left" state — exactly what you would expect from rotating "spin right" by $\pi$ about $z$.

**Example 4: A rotation about $\hat n = (1, 1, 1)/\sqrt 3$ by $\theta = 2\pi/3$.** We compute $u = \exp(-i\tfrac{\pi}{3}\vec\sigma\cdot\hat n)$. Since $(\vec\sigma\cdot\hat n)^2 = I$, the exponential terminates: $u = \cos(\pi/3)I - i\sin(\pi/3)\vec\sigma\cdot\hat n = \tfrac{1}{2}I - i\tfrac{\sqrt 3}{2}\vec\sigma\cdot\hat n = \tfrac{1}{2}I - \tfrac{i\sqrt 3}{2\sqrt 3}(\sigma_1 + \sigma_2 + \sigma_3) = \tfrac{1}{2}(I - i\sigma_1 - i\sigma_2 - i\sigma_3)$. This $u$ is the spinor lift of a $2\pi/3$ rotation about the body diagonal of the cube.

**Non-example: an action by a non-spinor representation.** If we ask $SU(2)$ to act on $\mathbb{R}^3$ via the *adjoint representation* $u \mapsto \mathrm{Ad}_u$, with $\mathrm{Ad}_u(\vec x) = u(\vec x \cdot \vec\sigma)u^{-1}$ decoded back as an $\mathbb{R}^3$-vector, we get the $SO(3)$-action — and *this* descends to $SO(3)$, as $\mathrm{Ad}_{-I} = \mathrm{Ad}_I$ (since $-I$ is central). So the adjoint representation is a *vector* representation, not a spinor representation. The defining feature of spinor representations is that they distinguish $u$ from $-u$.

**Calibration check.** A reader should verify: (i) under a rotation by $\theta = 4\pi$, every spinor returns to itself ($u(\hat n, 4\pi) = \exp(-2\pi i\vec\sigma\cdot\hat n) = +I$); (ii) the rotation $u_z(\pi/2)$ applied twice gives $u_z(\pi)$, demonstrating the homomorphism property; (iii) the inner product $\langle\psi, \phi\rangle = \psi^\dagger\phi$ is $SU(2)$-invariant ($\langle u\psi, u\phi\rangle = \psi^\dagger u^\dagger u \phi = \psi^\dagger\phi$).

---

# Unlocked by This

> [!tip] Spin Coherent States *(from Quantum Optics)*
> For a quantum-mechanical spin-$j$ system, the **spin coherent states** are the "most classical" states: they are the spin-$j$ analogues of the harmonic-oscillator coherent states. Each is labeled by a point on the Bloch sphere $S^2$ and obtained by rotating the highest-weight state $|j, j\rangle$ via a $SU(2)$ rotation. The construction relies on the action of $SU(2)$ on the spin-$j$ representation $V_j = \mathrm{Sym}^{2j}(\mathbb{C}^2)$ being induced from the fundamental action on $\mathbb{C}^2$; the coherent-state formalism is the geometric quantization of this orbit picture.

> [!tip] Hopf Fibration *(from Differential Topology)*
> The action of $U(1) = \{e^{i\alpha}: \alpha \in \mathbb{R}\} \subset SU(2)$ on $\mathbb{C}^2$ by multiplication (a subaction of the full $SU(2)$-action) has orbits the complex lines, and the quotient $\mathbb{C}^2 \setminus 0$ by $U(1)$ is $\mathbb{CP}^1 = S^2$. Restricted to the unit sphere $S^3 \subset \mathbb{C}^2$, this gives the **Hopf fibration** $S^3 \to S^2$ with fibre $S^1 = U(1)$. The total space $S^3 = SU(2)$ acts on itself by left multiplication, and the Hopf fibration is the quotient by the right $U(1)$-action. This makes the Hopf fibration a *principal $U(1)$-bundle over $S^2$*, with first Chern class $\pm 1$. It is the prototypical nontrivial circle bundle and the simplest topologically nontrivial example of a gauge field in physics (the **Dirac monopole**).

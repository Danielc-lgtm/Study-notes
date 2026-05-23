---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Chern Forms of a U(n) Bundle"
  - "Def - Vector Bundle"
  - "Def - de Rham Cohomology"
tags: [geometry, algebraic-topology, characteristic-classes, gauge-theory]
---

# Notation

$E \to M$ is a complex vector bundle (any rank $n \geq 1$); $L \to M$ is a complex line bundle (rank 1). $\theta$ is the curvature 2-form of a $U(n)$ connection. $\mathrm{Tr}(\theta)$ is the matrix trace, which for the rank-1 case is just $\theta$ itself. $[c_1(E)] \in H^2(M; \mathbb{Z})$ (under appropriate lift) is the cohomology class. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Axiom Motivation

The first Chern class is the *prototype* of all characteristic classes: it is the simplest, the most studied, and the model from which the others generalise. Its central feature is that for **line bundles** (rank 1), $c_1$ is a *complete* topological invariant — two line bundles on a CW complex are isomorphic if and only if their first Chern classes are equal (see [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]]). This is the simplest case of a general phenomenon, and it shows what characteristic classes *do*: they detect and classify topological obstructions.

The motivating question is: *what is the simplest topological invariant of a complex line bundle?* A complex line bundle $L$ over a manifold $M$ is locally trivial — over an open patch $U$ it is $U \times \mathbb{C}$ — but globally it can twist. The twisting is recorded in the **transition functions** $g_{UV} : U \cap V \to U(1) = S^1$. These are circle-valued functions, and their homotopy class (as elements of $H^1(M; \mathcal{O}^*)$, the sheaf cohomology of $S^1$-valued functions) classifies the bundle.

The classification is precisely $H^1(M; \underline{\mathbb{Z}}) \cong H^2(M; \mathbb{Z})$ by the exponential exact sequence $0 \to \mathbb{Z} \to \mathbb{R} \to S^1 \to 0$, giving $H^1(M; \underline{S^1}) \cong H^2(M; \mathbb{Z})$. The class of the line bundle in $H^2(M; \mathbb{Z})$ is the **first Chern class** $c_1(L)$. So $c_1$ is the *complete homotopy invariant* of a complex line bundle.

The differential-geometric expression $c_1 = (i/2\pi) \mathrm{Tr}(\theta)$ is one specific cocycle representing this cohomology class. The choice of connection picks a particular form representing the class; different connections give different forms, all in the same cohomology class. The integrality of periods $\int_z c_1 \in \mathbb{Z}$ for integer cycles $z$ is the statement that the de Rham class lifts to integer cohomology.

Why the factor $(i/2\pi)$? For a $U(1)$ bundle, the structure group elements are $e^{i\alpha}$ for $\alpha \in \mathbb{R}$, and the holonomy around a small loop $\gamma$ is $\exp(i \oint_\gamma \omega)$. Stokes's theorem gives $\oint_\gamma \omega = \int_\Sigma d\omega = \int_\Sigma F$ where $\gamma = \partial \Sigma$ and $F = d\omega$. The factor $i$ converts the anti-Hermitian connection $\omega = i\alpha$ to the real-valued $F$; the $1/(2\pi)$ normalises the period to be an integer when $\gamma$ generates $\pi_1(M)$ and the bundle has unit twist.

The integrality forces a quantisation. If we are given an arbitrary 2-form $F$ on a manifold $M$ and ask "is $F$ the curvature of a $U(1)$ bundle?", the answer is **yes** if and only if $[F/(2\pi)] \in H^2(M; \mathbb{R})$ lifts to integer cohomology — i.e., its periods are integers. This is the **Weil integrality theorem**, and it is the geometric content of charge quantisation. For the magnetic monopole, $F$ has period $4\pi g$ on the surrounding $S^2$, so $g \in \frac{1}{2}\hbar c/e \cdot \mathbb{Z}$, the **Dirac quantisation condition**.

The first Chern class generalises in three directions:

1. To **higher Chern classes** $c_2, c_3, \ldots$ for higher-rank bundles: these are higher symmetric polynomials of the eigenvalues of the curvature.
2. To **other characteristic classes** for other structure groups: Stiefel–Whitney classes for $O(n)$, Pontryagin classes for $SO(n)$, Euler class for $SO(n)$ in top degree.
3. To **K-theory invariants**: $c_1$ is the leading term of the Chern character $\mathrm{ch}(L) = e^{c_1}$ for a line bundle.

But the prototype is always $c_1$, and understanding it well is the entry point to the entire theory.

---

# The Definition

Let $E \to M$ be a complex vector bundle of any rank $n$ with $U(n)$ structure group and a chosen $U(n)$ connection with local curvature 2-form $\theta$. The **first Chern form** of $E$ is

$$c_1(E) := \frac{i}{2\pi} \mathrm{Tr}(\theta),$$

a globally defined real closed 2-form on $M$ (the matrix trace makes this independent of frame; the closedness follows from $d\mathrm{Tr}(\theta) = \mathrm{Tr}(d\theta) = 0$ via Bianchi).

The **first Chern class** of $E$ is the de Rham cohomology class

$$c_1(E) := \left[\frac{i}{2\pi} \mathrm{Tr}(\theta)\right] \in H^2_{\mathrm{dR}}(M; \mathbb{R}),$$

which lifts canonically to integer cohomology $c_1(E) \in H^2(M; \mathbb{Z})$ (via the integrality of periods on integer 2-cycles).

**For a complex line bundle** $L \to M$ (rank 1), $\mathrm{Tr}(\theta) = \theta$ since $\theta$ is a scalar 2-form, so

$$c_1(L) = \frac{i\theta}{2\pi} = \frac{F}{2\pi},$$

where $F = -i\theta$ is the real curvature 2-form when the connection is written as $\omega = -iA$ with real $U(1)$ potential $A$.

**Fundamental properties (line bundles):**

1. **Additivity under tensor product:** $c_1(L \otimes L') = c_1(L) + c_1(L')$.
2. **Conjugate:** $c_1(\bar L) = -c_1(L)$ (where $\bar L$ is the conjugate line bundle, equivalently the dual $L^*$).
3. **Naturality:** $c_1(f^* L) = f^* c_1(L)$ for any continuous map $f$.

**For higher rank:**

$$c_1(E) = c_1(\det E),$$

where $\det E = \bigwedge^n E$ is the **determinant line bundle**, the top exterior power. This identifies the first Chern class of a rank-$n$ bundle with the first Chern class of its determinant — a single line bundle.

For an **$SU(n)$ bundle**, $c_1(E) = 0$ because the determinant is trivial ($SU$ means special unitary, with $\det g = 1$ everywhere).

---

# Categorical / Structural Definition

The first Chern class is the **classifying map of a line bundle into $\mathbb{CP}^\infty$**. Specifically:

1. The classifying space of $U(1)$ is $BU(1) = \mathbb{CP}^\infty$, and the universal line bundle is the tautological line bundle $\mathcal{O}(-1) \to \mathbb{CP}^\infty$.
2. Complex line bundles on a CW complex $X$ are classified by homotopy classes of maps $X \to \mathbb{CP}^\infty$: $\mathrm{Pic}(X) \cong [X, \mathbb{CP}^\infty]$.
3. Since $\mathbb{CP}^\infty = K(\mathbb{Z}, 2)$ is the Eilenberg–MacLane space, $[X, \mathbb{CP}^\infty] = H^2(X; \mathbb{Z})$.
4. The bijection sends a line bundle $L$ to its first Chern class $c_1(L) \in H^2(X; \mathbb{Z})$.

This identifies $c_1$ as the **complete classifying invariant** of complex line bundles on CW complexes.

In sheaf-theoretic language, the first Chern class is the connecting homomorphism in the **exponential exact sequence**:

$$0 \to \mathbb{Z} \to \mathcal{O} \xrightarrow{\exp(2\pi i \cdot)} \mathcal{O}^* \to 0,$$

where $\mathcal{O}$ is the sheaf of smooth $\mathbb{C}$-valued functions and $\mathcal{O}^*$ is the sheaf of smooth $\mathbb{C}^*$-valued functions. The long exact sequence in sheaf cohomology gives

$$H^1(M; \mathcal{O}^*) \xrightarrow{c_1} H^2(M; \mathbb{Z}),$$

where $H^1(M; \mathcal{O}^*) = \mathrm{Pic}(M)$ is the Picard group of line bundles, and the map $c_1$ is the first Chern class. The differential-geometric formula $c_1 = (i/2\pi) F$ comes from the de Rham realisation: choosing a connection on $L$ and integrating over the Čech complex of the open cover gives precisely this expression.

---

# Relate to Other Fields / Compression

**True name:** the first Chern class is **the topological obstruction to the existence of a global non-vanishing section of a complex line bundle**, equivalently the **integer that classifies the line bundle up to isomorphism on a CW complex**. The operational pictures are:

- *Differential-geometric:* $c_1 = F/(2\pi)$, the curvature 2-form of a $U(1)$ connection, normalised so periods are integers.
- *Topological:* the integer counting the homotopy class of the transition function $S^1 \to U(1) = S^1$ on the equator of a sphere (winding number).
- *Algebraic:* the homotopy class of the classifying map $M \to \mathbb{CP}^\infty$.
- *Geometric:* the divisor class — number of zeros minus number of poles — of a meromorphic section (on Riemann surfaces).
- *Physical:* the monopole charge / magnetic flux quantum.

In **complex algebraic geometry**, $c_1$ is the bridge from the Picard group to integer cohomology: $\mathrm{Pic}(X) \to H^2(X; \mathbb{Z})$. The kernel of this map is the **identity component of Picard**, $\mathrm{Pic}^0(X)$, classifying topologically trivial line bundles by their analytic isomorphism class — a complex torus on a complex projective variety.

In **gauge theory**, $c_1$ is *the* charge of an Abelian gauge field. Electromagnetic field strength $F = dA$ defines a connection on a $U(1)$ bundle, and the first Chern number $\int_\Sigma c_1 = \int_\Sigma F/(2\pi) \in \mathbb{Z}$ on a closed 2-surface $\Sigma$ is the magnetic charge enclosed. The **Aharonov–Bohm effect** is the experimental detection of holonomy in a topologically nontrivial $U(1)$ bundle.

In **condensed matter**, $c_1$ is the **TKNN integer**: the Hall conductivity of a 2D electron system in a magnetic field is $\sigma_{xy} = (e^2/h) \int_{T^2} c_1$ where $T^2$ is the Brillouin torus. This explains the **integer quantum Hall effect** and is the prototype of all topological condensed-matter invariants.

In **representation theory**, $c_1$ of a line bundle on a Lie group's flag variety $G/T$ is the **weight** of the corresponding representation; the **Borel–Weil–Bott theorem** identifies cohomology of line bundles on $G/T$ with irreducible $G$-representations.

---

# Examples / Corollaries

**Example: trivial line bundle.** $c_1(M \times \mathbb{C}) = 0$, the zero class. The trivial bundle has a global non-vanishing section (the constant function 1), so no topological obstruction.

**Example: tautological line bundle on $\mathbb{CP}^1$.** The Hopf line bundle $\mathcal{O}(-1)$ on $\mathbb{CP}^1 = S^2$ has $c_1(\mathcal{O}(-1)) = -h$ where $h$ generates $H^2(\mathbb{CP}^1; \mathbb{Z})$, so $\int_{\mathbb{CP}^1} c_1 = -1$. See [[Ex - The Chern Number of the Hopf Line Bundle over CP^1]].

**Example: $\mathcal{O}(n)$ on $\mathbb{CP}^1$.** The $n$-th tensor power $\mathcal{O}(n) = \mathcal{O}(1)^{\otimes n}$ has $c_1(\mathcal{O}(n)) = n \cdot h$, so $\int_{\mathbb{CP}^1} c_1 = n$. These exhaust all line bundles on $\mathbb{CP}^1$: $\mathrm{Pic}(\mathbb{CP}^1) = \mathbb{Z}$, generated by $\mathcal{O}(1)$.

**Example: tangent bundle of a Riemann surface.** For a Riemann surface $\Sigma_g$ of genus $g$, the holomorphic tangent line bundle $T\Sigma_g$ has $\int_{\Sigma_g} c_1(T\Sigma_g) = \chi(\Sigma_g) = 2 - 2g$. This is the **Gauss–Bonnet theorem** rephrased: $\int K \, dA = 2\pi \chi$, and $c_1 = (K/2\pi) dA$ (the Gaussian curvature 2-form, normalised).

**Example: monopole bundle.** The $U(1)$ bundle on $S^2$ surrounding a magnetic monopole of charge $n$ (in appropriate units) has $\int_{S^2} c_1 = n$. The wavefunction of a charged particle is a section of this bundle, and its well-definedness requires $n \in \mathbb{Z}$ — Dirac quantisation. See [[Ex - The Magnetic Monopole and Dirac Quantization via c_1]].

**Example: $SU(n)$ bundle.** For any complex vector bundle with $SU(n)$ structure group, $c_1 = 0$. This is because $SU(n)$ matrices have determinant 1, so the determinant line bundle is trivial. Conversely, every $U(n)$ bundle with $c_1 = 0$ can be reduced to $SU(n) \times$ trivial, so $SU(n)$ bundles are exactly the "$c_1$-trivial" $U(n)$ bundles.

**Example: tensor product of line bundles.** $c_1(L \otimes L') = c_1(L) + c_1(L')$. Verification: if $L$ has connection $\omega = -iA$ and $L'$ has $\omega' = -iA'$, then $L \otimes L'$ has connection $\omega + \omega' = -i(A + A')$, with curvature $F + F'$, hence $c_1 = (F + F')/(2\pi) = c_1(L) + c_1(L')$.

**Example: determinant line bundle.** For a rank-$n$ bundle $E$, $c_1(E) = c_1(\det E)$ where $\det E = \bigwedge^n E$. In coordinates, if $E$ has connection $\omega$ (matrix-valued), $\det E$ has connection $\mathrm{Tr}(\omega)$ (scalar), and curvature $\mathrm{Tr}(\theta)$. So $c_1(\det E) = (i/2\pi) \mathrm{Tr}(\theta) = c_1(E)$.

**Is NOT an instance: a non-integer Chern number.** $c_1$ has integer periods, so $\int_z c_1$ is always an integer. A naive computation that gives a non-integer (e.g., $\int_{S^2} F / 2\pi = 1/2$) signals an error or a violation of the bundle condition (e.g., $F$ is not the curvature of a globally defined $U(1)$ connection).

**Corollary: characteristic of the determinant.** For a real oriented rank-$2$ vector bundle $E$ (a "rank-1 complex bundle" after choosing a complex structure), $c_1(E) = e(E)$ where $e$ is the Euler class. The Euler class generalises to all even-rank real oriented bundles as the top Pontryagin/Stiefel–Whitney class; for the rank-2 case, it coincides with $c_1$ via the complex structure.

**Corollary: Bertini-type theorem.** A generic section of a complex line bundle $L \to M$ (a Riemann surface) has zeros counted with sign equal to $\int_M c_1(L)$. This is the **Poincaré–Hopf theorem** for line bundles, the "obstruction-cocycle" picture for $c_1$. For $c_1 = 0$, generic sections are non-vanishing; for $c_1 \neq 0$, every section has at least $|c_1|$ zeros.

**Calibration check.** If you understand the definition you should be able to: (i) compute $c_1$ of a complex line bundle from a $U(1)$ connection in explicit coordinates; (ii) verify $c_1(L \otimes L') = c_1(L) + c_1(L')$; (iii) explain why $c_1$ of an $SU(n)$ bundle vanishes; (iv) identify the magnetic monopole charge as $\int_{S^2} c_1$.

---

# Unlocked by This

> [!tip] Dirac Quantisation *(from Quantum Mechanics)*
> The integrality $\int_{S^2} c_1 \in \mathbb{Z}$ for a $U(1)$ bundle on $S^2$ surrounding a magnetic monopole is the **Dirac quantisation condition** $eg = n\hbar c/2$, which forces the magnetic charge $g$ to be a half-integer multiple of $\hbar c / e$. Physically, this is the requirement that the wavefunction (a section of the bundle) be globally well-defined; mathematically, it is the requirement that the bundle exist as an honest complex line bundle. The quantisation of magnetic charge — strikingly, *if even one* magnetic monopole exists anywhere in the universe, then electric charge is quantised — is the prototype of all topological quantisation in physics.

> [!tip] Picard Group and the Néron–Severi Group *(from Algebraic Geometry)*
> For a complex projective variety $X$, the **Picard group** $\mathrm{Pic}(X) = H^1(X; \mathcal{O}^*)$ of holomorphic line bundles has a map $c_1 : \mathrm{Pic}(X) \to H^2(X; \mathbb{Z})$, whose image is the **Néron–Severi group** $\mathrm{NS}(X)$ — the lattice of algebraic divisor classes. The kernel is the **identity component** $\mathrm{Pic}^0(X)$, a complex torus parametrising topologically trivial line bundles (those with $c_1 = 0$). On a curve of genus $g$, $\mathrm{Pic}^0(X) =$ Jacobian variety, of complex dimension $g$. The structure $\mathrm{Pic}(X) = \mathrm{Pic}^0(X) \oplus \mathrm{NS}(X)$ (as abelian groups) is the **Picard scheme**, the fundamental object of algebraic geometry parametrising line bundles.

> [!tip] Integer Quantum Hall Effect *(from Condensed Matter)*
> A two-dimensional electron gas in a strong perpendicular magnetic field has its Hall conductivity quantised:
> $$\sigma_{xy} = \frac{e^2}{h} \cdot n, \qquad n \in \mathbb{Z}.$$
> The integer $n$ is the **TKNN invariant** (Thouless–Kohmoto–Nightingale–den Nijs), and it is precisely $\int_{T^2} c_1$ for the first Chern class of the filled-band sub-bundle of the **Bloch bundle** over the Brillouin torus $T^2$. The remarkable robustness of the quantisation (to 1 part in $10^9$) reflects the topological nature of the invariant: small perturbations cannot change an integer. This is the founding example of **topological condensed matter physics**.

---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Bundle"
  - "Def - Local Trivialization"
  - "Def - Transition Function of a Vector Bundle"
tags: [geometry, gauge-theory, complex, line-bundle]
---

# Notation

$L \to M$ denotes a complex line bundle over a smooth manifold $M$ — a complex vector bundle of rank $1$ in the sense of [[Def - Vector Bundle]]. Each fibre $L_p$ is a 1-dimensional complex vector space, isomorphic to $\mathbb{C}$. Transition functions $c_{VU} : U \cap V \to \mathrm{GL}(1, \mathbb{C}) = \mathbb{C}^\times$ are non-vanishing complex-valued functions. We reserve $J : L \to L$ for the fibrewise complex structure operator (the linear endomorphism with $J^2 = -\mathrm{id}$ realising multiplication by $i$). For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Axiom Motivation

The motivating object is the *wave function* of a charged particle. A wave function in non-relativistic quantum mechanics is a complex-valued function $\psi(x)$ on configuration space, with $|\psi|^2$ giving the probability density. The crucial feature is that $\psi$ is only defined *up to an overall phase*: $\psi$ and $e^{i\theta}\psi$ represent the same physical state. Classical quantum mechanics gets away with treating $\psi$ as a single complex-valued function, but as soon as topology becomes interesting — magnetic monopoles, Aharonov-Bohm, non-trivial configuration spaces — this becomes inadequate. The right object is a *section of a complex line bundle*: a smooth assignment of an element of a complex line $L_p$ to each point $p$, where the "lines" $L_p$ at different points need not be canonically identified, and the phase ambiguity is exactly the freedom to multiply each fibre's basis by a unit complex number.

The axioms for a complex line bundle are the minimum that captures this idea. We want: (i) at each point of $M$, *a* one-dimensional complex vector space; (ii) the fibres should vary smoothly so that "smooth section" makes sense; (iii) the bundle should be locally trivial so we can do calculations in patches.

Why complex rather than real? Two reasons. *Mathematically*, a complex 1-dimensional vector space is a real 2-dimensional space with extra structure (an operator $J$ with $J^2 = -\mathrm{id}$). The extra structure is what allows the operation "multiply by $i$" to be defined on sections — and this is exactly the operation needed for quantum mechanics' phase rotations $\psi \to e^{i\theta}\psi$. *Physically*, the wave functions of quantum mechanics are intrinsically complex; the Schrödinger equation $i\hbar\partial_t\psi = H\psi$ involves $i$ on the left side in an essential way.

Why rank 1 rather than rank $k$? Because *single*-particle wave functions take values in a *single* complex line at each configuration point. (Higher-rank bundles describe multi-component wave functions: spinors are sections of a rank-$2$ complex bundle over spacetime, isospin doublets are sections of a rank-$2$ bundle for $SU(2)$, etc.) The line bundle is the structurally simplest non-trivial complex bundle and the one electromagnetism lives on.

Why insist on the *transition functions landing in $\mathbb{C}^\times$* rather than (say) all of $\mathbb{R}^2$-linear automorphisms? Because the structure group $\mathrm{GL}(1, \mathbb{C}) = \mathbb{C}^\times$ is what makes "complex linear" the right notion of equivalence — it ensures that multiplication by complex scalars is well-defined on sections globally (not just in each patch). Dropping this would make $L$ into a real rank-2 bundle equipped with no compatible complex structure, fundamentally a different object.

Why is the *non-vanishing* of transition functions essential? Because a transition function $c_{VU}(p)$ specifies an isomorphism between two copies of $\mathbb{C}$ (the fibre coordinate in patches $U$ and $V$); an isomorphism of 1-d complex vector spaces is multiplication by a non-zero complex number. If $c_{VU}(p) = 0$ at some point, the gluing degenerates and the total space stops being a vector bundle.

The single axiom that ties everything together is the **cocycle condition** $c_{WV}c_{VU} = c_{WU}$ on triple overlaps (with $c_{UU} = 1$). Without this, the gluing data is inconsistent — going around a triple overlap $U \to V \to W \to U$ would multiply by a non-trivial scalar, contradicting "back where you started". The cocycle condition is the consistency requirement for the patching, and it is the single mathematical content that distinguishes a *line bundle* from "a collection of local copies of $U \times \mathbb{C}$".

Why is *hermitian* line bundle a useful enrichment (rather than mandatory)? Because a hermitian structure (a smoothly varying $\langle\cdot, \cdot\rangle_p : L_p \times L_p \to \mathbb{C}$) is exactly the data needed to talk about $|\psi|^2$, the probability density. Without hermitian structure, "magnitude squared" of a section is not defined intrinsically. With it, transition functions reduce from $\mathbb{C}^\times$ to $U(1) = \{z : |z| = 1\}$ — the **structure group reduction** that makes the link to physics tight. The structure-group-reduction language is the bridge to general gauge theory ([[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]]).

---

# The Definition

A **complex line bundle** over a smooth manifold $M$ is a smooth (complex) vector bundle $\pi : L \to M$ of complex rank 1. Unfolding the definition:

1. $L$ is a smooth manifold and $\pi : L \to M$ is a smooth surjection.
2. Each fibre $L_p = \pi^{-1}(p)$ has the structure of a 1-dimensional complex vector space.
3. $M$ admits an open cover $\{U_\alpha\}$ together with diffeomorphisms (**local trivializations**) $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{C}$ satisfying $\pi_1 \circ \Phi_\alpha = \pi$ (commutes with projection) and the restriction $\Phi_\alpha|_{L_p} : L_p \to \{p\} \times \mathbb{C}$ is a $\mathbb{C}$-linear isomorphism for every $p \in U_\alpha$.

On overlaps $U_\alpha \cap U_\beta$, the composition $\Phi_\beta \circ \Phi_\alpha^{-1} : (U_\alpha \cap U_\beta) \times \mathbb{C} \to (U_\alpha \cap U_\beta) \times \mathbb{C}$ has the form

$$(p, z) \mapsto (p, c_{\beta\alpha}(p)\,z)$$

for a smooth **transition function** $c_{\beta\alpha} : U_\alpha \cap U_\beta \to \mathbb{C}^\times$, satisfying the cocycle condition

$$c_{\alpha\alpha} = 1, \qquad c_{\gamma\beta}\,c_{\beta\alpha} = c_{\gamma\alpha} \quad \text{on } U_\alpha \cap U_\beta \cap U_\gamma.$$

**Equivalent real-bundle description.** A complex line bundle is equivalently a real rank-2 vector bundle $L \to M$ equipped with a smooth bundle endomorphism $J : L \to L$ satisfying $J^2 = -\mathrm{id}_L$ on each fibre. The complex structure $J$ defines multiplication by $i$: $(a + bi) \cdot v := av + bJv$ for $v \in L_p$. Conversely, any complex line bundle yields a real rank-2 bundle with such a $J$.

**Hermitian enrichment.** A **hermitian line bundle** $(L, h)$ is a complex line bundle equipped with a smoothly varying hermitian inner product $h_p : L_p \times L_p \to \mathbb{C}$ on each fibre — a sesquilinear (conjugate-linear in the first slot, complex-linear in the second), positive-definite form. The structure group reduces from $\mathbb{C}^\times$ to $U(1) = \{z \in \mathbb{C} : |z| = 1\}$: transition functions between *unit-norm* local sections are unimodular.

**Triviality.** A complex line bundle is **trivial** if and only if it admits a nowhere-vanishing global section — equivalently, if its first Chern class $c_1(L) \in H^2(M, \mathbb{Z})$ vanishes. The trivial line bundle is $L = M \times \mathbb{C}$ with $\pi$ the projection.

---

# Categorical / Structural Definition

The set $\mathrm{Pic}(M)$ of isomorphism classes of complex line bundles on $M$ forms an abelian group under tensor product, $[L_1] \cdot [L_2] := [L_1 \otimes L_2]$, with identity $[M \times \mathbb{C}]$ (the trivial bundle) and inverses $[L]^{-1} = [L^*]$ (the dual line bundle, with transition functions $c^{-1}_{\beta\alpha}$). This is the **Picard group** of $M$. The classification theorem says

$$\mathrm{Pic}(M) \cong H^2(M, \mathbb{Z}),$$

the second integer cohomology of $M$. The isomorphism sends $[L]$ to its **first Chern class** $c_1(L) \in H^2(M, \mathbb{Z})$, which can be computed from any hermitian connection on $L$ as the cohomology class $[\frac{i}{2\pi}F] \in H^2(M, \mathbb{R})$ together with the integrality from the transition-function cocycle. The classifying space of complex line bundles is $BU(1) = \mathbb{CP}^\infty$, and isomorphism classes of complex line bundles on $M$ are in bijection with homotopy classes of maps $M \to \mathbb{CP}^\infty$.

In algebraic geometry, on a complex manifold the Picard group restricts to the group of holomorphic line bundles, and there is a refined exact sequence relating it to divisor classes — the foundation of the entire theory of divisors and line bundles in algebraic geometry.

---

# Relate to Other Fields / Compression

A complex line bundle is **"a smoothly varying complex line"** — the structurally simplest non-trivial complex vector bundle and the one all of electromagnetism, abelian gauge theory, and many topological invariants live on.

**In gauge theory**, complex line bundles with hermitian structure (i.e. $U(1)$-bundles) are the bundles of $U(1)$-gauge theory, of which electromagnetism is the basic example. Connections on $U(1)$-bundles are electromagnetic potentials; curvatures are field strengths; sections are wave functions of charged particles. See [[Def - U(1) Gauge Field and Electromagnetic Connection]].

**In algebraic geometry**, *holomorphic* line bundles on a complex manifold $X$ generalize the classical notion of a divisor: a divisor (formal sum of codimension-1 subvarieties with integer multiplicities) determines a line bundle via $\mathcal{O}(D)$. Line bundles are the basic objects of *sheaf cohomology*, and the rich theory connecting them to global sections is one of the pillars of complex algebraic geometry — Serre duality, Riemann-Roch, the Kodaira vanishing theorem all live here.

**In topology**, the classifying space $BU(1) = \mathbb{CP}^\infty$ has cohomology $H^*(BU(1), \mathbb{Z}) = \mathbb{Z}[t]$ with $|t| = 2$, generated by the universal first Chern class. The classification of complex line bundles by $H^2(M, \mathbb{Z})$ is a special case of the general classifying-space machinery.

**True name:** A complex line bundle is **"a complex line that varies smoothly with the base point"**. The hermitian version adds "the line has a chosen unit circle". The bundle is **trivial** iff you can choose the lines and the unit circles globally consistently — and the obstruction to doing so is *one integer per closed 2-cycle*, the first Chern number.

---

# Examples / Corollaries

**Is an instance: Trivial line bundle $M \times \mathbb{C}$.** The simplest example, with global section $\sigma(p) = (p, 1)$ and trivial transition functions ($c \equiv 1$). All sections of $M \times \mathbb{C}$ are just complex-valued functions on $M$. First Chern class is zero.

**Is an instance: The Hopf line bundle $H \to \mathbb{CP}^n$.** Over the complex projective space $\mathbb{CP}^n$ (the space of complex lines through the origin in $\mathbb{C}^{n+1}$), the fibre $H_{[v]}$ at the line $[v] = \mathbb{C}v$ is *the line $\mathbb{C}v$ itself* (a 1-dimensional complex vector space). This is the **tautological line bundle**, denoted $\mathcal{O}(-1)$. Its first Chern class is the generator of $H^2(\mathbb{CP}^n, \mathbb{Z}) \cong \mathbb{Z}$, taken with sign $-1$. The dual bundle $\mathcal{O}(1) = H^*$ is the **hyperplane bundle**, the basic positive line bundle of algebraic geometry. Restricting to $\mathbb{CP}^1 \cong S^2$ gives a line bundle over the 2-sphere with $c_1 = -1$.

**Is an instance: The Dirac monopole bundle over $S^2$.** A non-trivial $U(1)$-bundle over $S^2$ with first Chern number $\frac{2eg}{\hbar}$, built as in [[Def - The Dirac Monopole Bundle]]. The corresponding hermitian line bundle has $c_1 = \frac{2eg}{\hbar} \in \mathbb{Z}$ (assuming the Dirac quantization condition); this is the same bundle as the $\frac{2eg}{\hbar}$-fold tensor power $H^{\otimes (2eg/\hbar)}$ of the Hopf bundle, up to sign.

**Is an instance: The tangent bundle of an oriented Riemannian surface $M^2$.** $TM$ is a real rank-2 bundle; the Riemannian metric and orientation give a canonical fibrewise rotation by $90°$, $J : TM \to TM$ with $J^2 = -\mathrm{id}$ — making $TM$ a *complex line bundle*. Transition functions between oriented orthonormal frames are rotation matrices, which under the identification $SO(2) \cong U(1)$ become unit complex numbers. The first Chern class equals the Euler class: $c_1(TM) = e(TM) \in H^2(M, \mathbb{Z}) \cong \mathbb{Z}$, with integral equal to $\chi(M) = 2 - 2g$.

**Is an instance: Determinant line bundle.** For a complex vector bundle $E$ of rank $k$, the top exterior power $\det E = \Lambda^k E$ is a complex line bundle with $c_1(\det E) = c_1(E)$. This reduces computations of the first Chern class to the rank-1 case.

**Is NOT an instance: A real line bundle that does not admit a complex structure.** The Möbius band is a real line bundle over $S^1$ — but $S^1$ is 1-dimensional, so its rank-2 real bundles are not naturally complex. The Möbius band is *not* a complex line bundle in any meaningful sense because complex line bundles have *even* real rank ($= 2$); the Möbius band has real rank $1$.

**Is NOT an instance (compatible vs incompatible $J$): An almost complex structure on $S^4$.** $S^4$ does not admit an almost complex structure — there is no fibrewise $J : TS^4 \to TS^4$ with $J^2 = -\mathrm{id}$ globally, by a theorem of Borel-Serre using characteristic classes. So $TS^4$ is *not* a complex (rank-2) bundle.

**Corollary (tensor product structure).** $\mathrm{Pic}(M) = \{$ iso classes of complex line bundles$\}$ is an abelian group under tensor product, with identity the trivial bundle and inverses the dual bundle. Chern classes are additive: $c_1(L_1 \otimes L_2) = c_1(L_1) + c_1(L_2)$.

**Corollary (line bundles classified by $H^2(M, \mathbb{Z})$).** The map $L \mapsto c_1(L)$ is an isomorphism of abelian groups $\mathrm{Pic}(M) \to H^2(M, \mathbb{Z})$. Consequence: for simply connected $M$ with $H^2 = 0$ (like $\mathbb{R}^n$, $S^n$ for $n \ne 2$), the only complex line bundle is the trivial one. For $S^2$, $H^2 = \mathbb{Z}$, so line bundles are classified by a single integer.

**Calibration check.** (1) Verify the Möbius bundle is real rank 1, hence *not* a complex line bundle. (2) Compute $c_1$ of the tangent bundle of the torus $T^2$ — answer: $\chi(T^2) = 0$, so $TT^2$ is trivial as a complex line bundle (this is why you can comb the hair on a torus). (3) Verify the cocycle condition for the Dirac monopole transition function $c_{VU} = e^{-2ieg\phi/\hbar}$ on the overlap $U \cap V$ of two hemispheres — trivially satisfied because there are only two patches.

---

# Unlocked by This

> [!tip] First Chern Class and the Classification of Line Bundles *(from Algebraic Topology)*
> The map $\mathrm{Pic}(M) \to H^2(M, \mathbb{Z})$ sending a complex line bundle to its **first Chern class** is a group isomorphism. This is the simplest case of the general classification of vector bundles by characteristic classes via classifying spaces. Computing $c_1$ from any hermitian connection's curvature, $c_1(L) = \frac{i}{2\pi}[F]$, gives a *geometric* incarnation of the topological invariant. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full Chern-Weil story.

> [!tip] Quantum Mechanics of a Charged Particle as Line-Bundle Geometry *(from Mathematical Physics)*
> Once you accept that the wave function of a charged particle is a section of a hermitian line bundle (not a complex-valued function), the entire structure of QED falls into place: covariant derivatives are coupled derivatives ($\partial_\mu - (ie/\hbar)A_\mu$), curvature is the EM field strength, Chern numbers are monopole charges, holonomies are Aharonov-Bohm phases. The classical-mechanics description (charged particle in EM field) is the trivial-bundle special case. The non-trivial bundle case (monopoles) is *forced* by the existence of magnetic charge — see [[Thm - Dirac Quantization Condition]].

> [!tip] Algebraic Geometry of Line Bundles *(from Complex Geometry and Algebraic Geometry)*
> Holomorphic line bundles on a complex algebraic variety are the foundation of much of algebraic geometry. Divisors (formal sums of codimension-1 subvarieties) determine line bundles via $\mathcal{O}(D)$. Cohomology of line bundles computes spaces of global meromorphic functions with prescribed poles. **Serre duality**, **Riemann-Roch**, and **the Kodaira vanishing theorem** all describe the interplay between line bundles, their global sections, and the geometry of the underlying variety. This is the entry point to **algebraic geometry** as a subject and to **modular forms** (which are sections of line bundles over modular curves).

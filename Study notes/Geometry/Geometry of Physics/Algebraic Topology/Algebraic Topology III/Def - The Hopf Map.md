---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Higher Homotopy Group"
  - "Def - Fibration"
tags: [geometry, algebraic-topology, fibre-bundles, gauge-theory]
---

# Notation

$S^3$ is the unit 3-sphere in $\mathbb{C}^2 = \mathbb{R}^4$: $\{(z_0, z_1) \in \mathbb{C}^2 : |z_0|^2 + |z_1|^2 = 1\}$. $S^2$ is identified with the **complex projective line** $\mathbb{CP}^1$: pairs $(z_0, z_1) \neq (0, 0)$ modulo $(z_0, z_1) \sim (\lambda z_0, \lambda z_1)$ for $\lambda \in \mathbb{C}^\times$. The homogeneous coordinate $[z_0 : z_1]$ denotes the equivalence class. The standard identification $\mathbb{CP}^1 \cong S^2$ sends $[z_0 : z_1]$ to the corresponding point on the Riemann sphere via stereographic projection — concretely $[z_0 : z_1] \mapsto (2 z_0 \bar z_1, |z_0|^2 - |z_1|^2)$ (up to normalisation) when viewed in $\mathbb{R}^3$. $SU(2)$ is the group of $2 \times 2$ complex unitary matrices of determinant 1, identified with $S^3$ via $(z_0, z_1) \leftrightarrow \begin{pmatrix} z_0 & -\bar z_1 \\ z_1 & \bar z_0 \end{pmatrix}$. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Axiom Motivation

The Hopf map answers the question Heinz Hopf posed in 1931: **does there exist a non-contractible continuous map from $S^3$ to $S^2$?** The naive answer is no, on the basis that higher-dimensional spheres are "too big" to fit non-trivially into lower-dimensional ones. Indeed, for $k < n$, we have $\pi_k(S^n) = 0$ — any map $S^k \to S^n$ misses a point and contracts. The naive intuition suggests this should also hold for $k > n$: a higher-dimensional sphere has more freedom to move around and should be deformable to a constant.

The Hopf map proves this intuition spectacularly wrong. There exists a map $\eta : S^3 \to S^2$ that is *not* null-homotopic, and this single map generates an infinite cyclic group $\pi_3(S^2) = \mathbb{Z}$ of homotopy classes. The discovery was startling enough that it led directly to the invention of higher homotopy groups by Hurewicz a few years later: the existence of non-trivial $\pi_k(S^n)$ for $k > n$ was the phenomenon that demanded a theory.

The construction itself is forced once you ask the right question. Consider $\mathbb{C}^2$. The unit 3-sphere $S^3 \subset \mathbb{C}^2$ is acted on by the unit complex numbers $S^1 = U(1)$ via scalar multiplication: $\lambda \cdot (z_0, z_1) = (\lambda z_0, \lambda z_1)$ for $|\lambda| = 1$. This action is **free** (no fixed points except at the origin, which is not on $S^3$) and the quotient is

$$S^3 / U(1) = \{(z_0, z_1) \neq (0, 0)\} / \mathbb{C}^\times = \mathbb{CP}^1.$$

The natural quotient map $\eta : S^3 \to S^3/U(1) = \mathbb{CP}^1 \cong S^2$ is the **Hopf map**. The fibre over $[z_0 : z_1] \in \mathbb{CP}^1$ is the orbit $\{(\lambda z_0, \lambda z_1) : |\lambda| = 1\}$, which is a great circle on $S^3$. So the Hopf map exhibits $S^3$ as the total space of a **circle bundle** over $S^2$:

$$S^1 \hookrightarrow S^3 \xrightarrow{\eta} S^2.$$

This is the **Hopf fibration**. Its non-triviality — the fact that $S^3 \neq S^2 \times S^1$ as a bundle — is what makes $\eta$ non-contractible. The deep content is that the long exact sequence of this fibration computes $\pi_3(S^2) = \pi_3(S^3) = \mathbb{Z}$, and the generator is precisely the Hopf map.

Why is the design forced? The construction is, up to isomorphism, the **only** non-trivial $U(1)$ bundle over $S^2$. By [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]], complex line bundles over $S^2$ (equivalently, $U(1)$ principal bundles) are classified by their first Chern number $\int_{S^2} c_1 \in H^2(S^2; \mathbb{Z}) = \mathbb{Z}$. The Hopf bundle has $c_1 = -1$ (or $+1$ in the opposite orientation), making it the *generator* of all line bundles on $S^2$ under tensor product. Every line bundle on $S^2$ is a tensor power $L^{\otimes n}$ of the Hopf line bundle, with $c_1 = n$.

There are three other ways to express the same construction, each illuminating:

1. **Quaternionic.** $S^3 =$ unit quaternions; the Hopf map sends a unit quaternion $q$ to $q i q^{-1}$, which lies on the unit 2-sphere in the imaginary quaternions $\mathbb{R}^3 = \mathrm{Im}\,\mathbb{H}$. The fibres are the conjugacy classes of unit quaternions, all isomorphic to $S^1$.

2. **Group-theoretic.** $S^3 = SU(2)$; the adjoint action of $SU(2)$ on $\mathfrak{su}(2) = \mathbb{R}^3$ gives a homomorphism $SU(2) \to SO(3)$ whose kernel is $\{\pm I\}$ — the double cover. Restricting the action to the orbit through $\sigma_3 \in \mathfrak{su}(2)$ (a sphere $S^2 \subset \mathbb{R}^3$) gives the Hopf map: $SU(2)$ acts transitively, the stabiliser of $\sigma_3$ is the diagonal subgroup $\{\mathrm{diag}(e^{i\theta}, e^{-i\theta})\} \cong U(1)$, and the map $SU(2) \to SU(2)/U(1) = S^2$ is the Hopf fibration.

3. **Topological.** $S^3 =$ join $S^1 * S^1$, the topological join of two circles. The Hopf map is the quotient that collapses each fibre $S^1$ to a point.

The viewpoint shifts but the bundle is the same.

---

# The Definition

The **Hopf map** is the continuous map $\eta : S^3 \to S^2$ defined as follows. Identify $S^3$ with the unit 3-sphere in $\mathbb{C}^2$:

$$S^3 = \{(z_0, z_1) \in \mathbb{C}^2 : |z_0|^2 + |z_1|^2 = 1\}.$$

Identify $S^2$ with the complex projective line $\mathbb{CP}^1$ via stereographic projection. Then

$$\eta(z_0, z_1) = [z_0 : z_1] \in \mathbb{CP}^1 \cong S^2,$$

the homogeneous coordinate of the point $(z_0, z_1)$ in $\mathbb{CP}^1$.

Equivalently, in real coordinates: if $z_0 = a + bi$, $z_1 = c + di$ with $a^2 + b^2 + c^2 + d^2 = 1$, then

$$\eta(a, b, c, d) = (2(ac + bd),\ 2(bc - ad),\ a^2 + b^2 - c^2 - d^2) \in S^2 \subset \mathbb{R}^3.$$

The map $\eta : S^3 \to S^2$ is the projection of a smooth principal $U(1)$-bundle (equivalently, a smooth fibre bundle with fibre $S^1$). The fibre over $[z_0 : z_1]$ is

$$\eta^{-1}([z_0 : z_1]) = \{(e^{i\theta} z_0,\ e^{i\theta} z_1) : \theta \in [0, 2\pi)\},$$

a great circle on $S^3$. The structural data is the **Hopf fibration**:

$$S^1 \hookrightarrow S^3 \xrightarrow{\eta} S^2.$$

The Hopf map represents the generator of $\pi_3(S^2) = \mathbb{Z}$ (see [[Ex - Pi_3 of S^2 is Z via the Hopf Map]]).

---

# Categorical / Structural Definition

The Hopf map is the **principal $U(1)$-bundle** classified by $c_1 = -1 \in H^2(S^2; \mathbb{Z}) = \mathbb{Z}$. In the language of [[Def - Characteristic Class|characteristic classes]], it is the generator of the group of all complex line bundles on $S^2$ under tensor product:

$$\mathrm{Pic}(S^2) \cong H^2(S^2; \mathbb{Z}) = \mathbb{Z}, \qquad [\text{Hopf}] \leftrightarrow -1.$$

The classifying map of the Hopf bundle is the inclusion $S^2 = \mathbb{CP}^1 \hookrightarrow \mathbb{CP}^\infty = BU(1)$ as the lowest-dimensional skeleton, and the universal bundle $\mathbb{CP}^\infty$ contains every complex line bundle as a pullback of the **tautological line bundle** $\mathcal{O}(-1) \to \mathbb{CP}^\infty$.

Group-theoretically, the Hopf fibration is the quotient $SU(2) \to SU(2)/U(1) = S^2$ where $U(1) \subset SU(2)$ is the diagonal subgroup $\{\mathrm{diag}(e^{i\theta}, e^{-i\theta})\}$. The space $SU(2)/U(1)$ is a **flag variety** of $SU(2)$, and the construction generalises to **complex flag varieties** $G/T$ for compact Lie groups $G$ with maximal torus $T$.

In algebraic geometry, the Hopf line bundle is the **tautological line bundle** $\mathcal{O}_{\mathbb{P}^1}(-1)$ on $\mathbb{CP}^1$, whose fibre over $[z_0 : z_1]$ is the complex line $\{(\lambda z_0, \lambda z_1) : \lambda \in \mathbb{C}\} \subset \mathbb{C}^2$. The unit-norm subset of this line is exactly the circle $\eta^{-1}([z_0 : z_1])$, so $S^3$ is the unit circle bundle inside the total space of $\mathcal{O}(-1)$.

---

# Relate to Other Fields / Compression

**True name:** the Hopf map is **the principal $U(1)$ bundle on $S^2$ of Chern number $-1$**, equivalently *the* non-trivial double cover that turns $S^3$ into a non-product bundle over $S^2$. The operational picture is "scale the unit ball in $\mathbb{C}^2$ down to its projectivisation, with the residual phase being the fibre circle". Everything else — the quaternionic, group-theoretic, and join descriptions — is a different way of saying this.

In **physics**, the Hopf map is the magnetic monopole. A monopole of charge $g$ at the origin of $\mathbb{R}^3$ produces a vector potential that cannot be globally defined on $S^2$ surrounding the monopole — it is well-defined only on patches, with transition functions $e^{i\alpha(\theta)}$ on the equator. The bundle these transition functions assemble into is a $U(1)$ bundle on $S^2$ with Chern number $= 2g/\hbar c \in \mathbb{Z}$ (by [[Ex - The Magnetic Monopole and Dirac Quantization via c_1|Dirac quantisation]]). For unit charge this is exactly the Hopf bundle.

In **quantum mechanics**, the Hopf map describes the **Bloch sphere**: a spin-1/2 state $\psi \in \mathbb{C}^2$ has $|\psi| = 1$ on its phase orbit and identifies physically equivalent states (those differing by an overall phase) — so the physical state space is $S^3/U(1) = S^2$, the Bloch sphere. The Hopf map sends the quantum-state vector to the physical Bloch-sphere point.

The Hopf map also generalises: the **quaternionic Hopf map** $S^7 \to S^4$ with fibre $S^3 = SU(2)$ generates $\pi_7(S^4) = \mathbb{Z} \oplus \mathbb{Z}/12$, and the **octonionic Hopf map** $S^{15} \to S^8$ generates a piece of $\pi_{15}(S^8)$. These are the four **division-algebra Hopf maps**: $\mathbb{R}$ (the double cover $S^1 \to S^1$), $\mathbb{C}$ (the standard Hopf $S^3 \to S^2$), $\mathbb{H}$ (quaternionic), and $\mathbb{O}$ (octonionic). They exist precisely because there are exactly four normed division algebras.

---

# Examples / Corollaries

**Example: the fibre over $[1 : 0]$.** The point $[1 : 0] \in \mathbb{CP}^1$ corresponds to the "north pole" of $S^2$ under the standard identification. Its preimage under $\eta$ is

$$\eta^{-1}([1 : 0]) = \{(e^{i\theta}, 0) : \theta \in [0, 2\pi)\}.$$

This is the unit circle in the $z_0$-plane $\mathbb{C} \times \{0\} \subset \mathbb{C}^2$, lying on $S^3$. Similarly, the fibre over $[0 : 1]$ (the south pole) is the unit circle in $\{0\} \times \mathbb{C}$. These two fibres are *linked* in $S^3$: their **linking number** is $\pm 1$. More generally, *every* two distinct fibres of the Hopf map are linked exactly once — this is the **Hopf invariant** of the map and is the geometric content of its non-triviality.

**Example: the Hopf invariant.** For a map $f : S^3 \to S^2$, the **Hopf invariant** $H(f) \in \mathbb{Z}$ is defined as the linking number of the preimages of two distinct regular values. For the Hopf map itself, $H(\eta) = 1$. The Hopf invariant gives an alternative computation of the isomorphism $\pi_3(S^2) \to \mathbb{Z}$, distinct from the long-exact-sequence approach; the two agree because both identify the class of the Hopf map with $1 \in \mathbb{Z}$.

**Example: $\eta$ as a quotient by $U(1)$ action.** The action $\lambda \cdot (z_0, z_1) = (\lambda z_0, \lambda z_1)$ for $\lambda \in U(1)$ is free on $S^3$: if $\lambda \cdot v = v$ with $v \in S^3$, then either $\lambda = 1$ or $v = 0$; the latter is impossible since $|v| = 1$. So the quotient is a smooth manifold (in fact, $\mathbb{CP}^1 \cong S^2$), and the projection is a smooth principal $U(1)$-bundle.

**Example: Hopf composition.** The composition $S^4 \xrightarrow{\Sigma\eta} S^3 \xrightarrow{\eta} S^2$, where $\Sigma\eta$ is the suspension of the Hopf map, generates $\pi_4(S^2) = \mathbb{Z}/2$ — the first higher homotopy group of $S^2$ that is not infinite cyclic. This shows that suspension takes non-trivial $\eta$ to non-trivial elements of higher homotopy, but the integer infinite-cyclic structure of $\pi_3(S^2)$ collapses to $\mathbb{Z}/2$ at one suspension.

**Is NOT an instance: the projection $S^3 = S^2 \times S^1 \to S^2$.** $S^3$ is *not* homeomorphic to $S^2 \times S^1$ — these are genuinely different 3-manifolds. The Hopf map exhibits $S^3$ as a *twisted* $S^1$-bundle over $S^2$, not a product. A product structure would force $\pi_2(S^3) = \pi_2(S^2 \times S^1) = \pi_2(S^2) \oplus \pi_2(S^1) = \mathbb{Z}$, contradicting the (correct) fact $\pi_2(S^3) = 0$.

**Corollary: $S^3$ admits two transverse $S^2$-foliations? No.** Actually no: the Hopf fibration is a foliation of $S^3$ by circles, not 2-spheres. There is no foliation of $S^3$ by codimension-1 submanifolds globally — but Reeb's theorem allows foliations with leaves of dimension 2 with finitely many exceptional leaves. The Hopf fibration is the **codimension-2 foliation** of $S^3$ that is most studied.

**Corollary: linking numbers and the Hopf invariant.** Two distinct fibres of $\eta$, say $F_1 = \eta^{-1}(p_1)$ and $F_2 = \eta^{-1}(p_2)$, are linked once in $S^3$. The proof: their projections to $S^2$ are distinct points, so the linking number can be computed by integrating $\omega \wedge d\omega$ where $\omega$ is a 1-form on $S^3$ representing the dual of $\eta^* (\text{area form on }S^2)$. This is the **Whitehead integral formula** for the Hopf invariant.

**Calibration check.** If you understand the Hopf map you should be able to: (i) verify directly that the formula $\eta(a,b,c,d) = (2(ac+bd), 2(bc-ad), a^2+b^2-c^2-d^2)$ maps $S^3$ to $S^2$ (compute the norm of the image); (ii) show that the fibres are great circles by computing the preimage of an explicit point; (iii) explain why $S^3 \neq S^2 \times S^1$ as a topological space (use $\pi_2$).

---

# Unlocked by This

> [!tip] Magnetic Monopole *(from Quantum Mechanics in EM Fields)*
> A magnetic monopole at the origin of $\mathbb{R}^3$ corresponds, on the surrounding sphere $S^2$, to a $U(1)$ bundle whose isomorphism class is determined by the first Chern number $\int_{S^2} c_1$. For unit charge, this bundle is the Hopf bundle. The wavefunction of a charged particle in the monopole field is a section of this bundle (a complex-valued function with prescribed transition rules between patches), and its global existence requires $c_1 \in \mathbb{Z}$ — the **Dirac quantisation condition**.

> [!tip] BPST Instanton *(from Yang–Mills Theory)*
> The BPST instanton is the simplest $SU(2)$ Yang–Mills field on $\mathbb{R}^4$ with $c_2 = 1$. Its structure mirrors the Hopf bundle: the gauge transformation at infinity is a map $g : S^3_\infty \to SU(2) = S^3$, and the instanton number is the degree of this map. The BPST instanton has $g(x) = (x^4 + i\vec x \cdot \vec\sigma)/|x|$, which is exactly the identity map on $S^3$ (under the standard identification $S^3 = SU(2)$), giving instanton number $1$.

> [!tip] Hopf Invariant One Problem *(from Adams's Theorem)*
> A fundamental theorem of algebraic topology (Adams, 1960) is that the **Hopf invariant one problem** has solutions only in dimensions $1, 2, 4, 8$, corresponding to the four normed division algebras $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$. This is the algebraic-topology version of **Hurwitz's theorem** on division algebras and one of the deepest results in the homotopy theory of spheres. It is proven using **Adams operations** $\psi^k$ in K-theory, the cohomology operations that act on K-theory analogously to Steenrod operations on ordinary cohomology.

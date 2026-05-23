---
type: theorem
subject: spinors
prereqs:
  - "Def - Pin and Spin Groups"
  - "Def - Clifford Algebra"
  - "Thm - SU(2) is the Double Cover of SO(3)"
tags: [geometry, spinors, lie-groups, topology]
---

# Notation

For $n \geq 3$, $\mathrm{Spin}(n) \subset \mathrm{Cl}^0(\mathbb{R}^n, |\cdot|^2)$ is the spin group (see [[Def - Pin and Spin Groups]]), and $SO(n)$ is the special orthogonal group. The covering map is $\pi: \mathrm{Spin}(n) \to SO(n)$, given by the twisted adjoint action $\pi(a)(v) = \alpha(a)va^{-1}$ where $\alpha$ is the parity automorphism. For Minkowski signature, $\mathrm{Spin}(p, q)$ is the spin group of $\mathbb{R}^{p+q}$ with signature $(p, q)$; the identity component is $\mathrm{Spin}^+(p, q)$ (or $\mathrm{Spin}^+_0(p, q)$).

---

# Statement

> **Theorem.** For every $n \geq 3$, the twisted adjoint map $\pi: \mathrm{Spin}(n) \to SO(n)$ is a surjective Lie group homomorphism with kernel $\{\pm 1\}$. Moreover:
>
> 1. $\mathrm{Spin}(n)$ is connected and simply connected.
> 2. $\pi: \mathrm{Spin}(n) \to SO(n)$ is the **universal cover** of $SO(n)$, with $\pi_1(SO(n)) = \mathbb{Z}/2$ for $n \geq 3$.
> 3. The non-trivial loop in $SO(n)$ corresponds to a $2\pi$ rotation about any axis (any 2-dimensional rotation plane in $\mathbb{R}^n$).
>
> For the Lorentzian signature $(p, q)$ with $p, q \geq 1$, $\mathrm{Spin}^+(p, q) \to SO^+(p, q)$ is again a $2:1$ covering, surjective on the identity component, with kernel $\{\pm 1\}$.

> **Corollary.** $\mathrm{Spin}(n)$ for $n \geq 3$ is the unique connected double cover of $SO(n)$; any connected Lie group $\widetilde G$ with $\widetilde G \to SO(n)$ a $2:1$ smooth covering homomorphism is isomorphic to $\mathrm{Spin}(n)$.

> **Corollary.** Every (continuous) representation of $\mathfrak{so}(n) = \mathfrak{spin}(n)$ integrates to a representation of $\mathrm{Spin}(n)$, but descends to $SO(n)$ iff $-1 \in \mathrm{Spin}(n)$ acts as the identity. The representations of $\mathrm{Spin}(n)$ not descending to $SO(n)$ are the **spinor representations**.

---

# Motivation

This theorem is the generalisation of [[Thm - SU(2) is the Double Cover of SO(3)]] from $n = 3$ to arbitrary $n \geq 3$. It is the *foundational* result of spin geometry: it asserts the existence of a "spin double cover" $\mathrm{Spin}(n)$ of $SO(n)$ in every dimension, with the same topological signature ($\pi_1 = \mathbb{Z}/2$) and the same construction principle (via the Clifford algebra). Every concrete computation in spinor physics, every spin structure on a manifold, every Dirac operator on a curved space, depends on this theorem.

The reason for restricting to $n \geq 3$: in dimensions $n = 0, 1, 2$, the topology of $SO(n)$ is different. $SO(0) = \{1\}$ is trivial; $SO(1) = \{1\}$ is trivial; $SO(2) = U(1) = S^1$ has $\pi_1 = \mathbb{Z}$, not $\mathbb{Z}/2$, and its universal cover is $\mathbb{R}$, not a double cover. So the "spin group as double cover" statement is precisely a statement for $n \geq 3$, where the fundamental group stabilises to $\mathbb{Z}/2$.

The motivation for caring about the spin cover is essentially the same as for $SU(2) \to SO(3)$: the spinor representations of $\mathrm{Spin}(n)$ — which live on the cover but cannot descend to $SO(n)$ — describe **fermionic matter** in any dimension. These representations are the irreducible $\mathrm{Cl}(n, 0)$-modules; their existence and dimension are dictated by the [[Thm - Classification of Clifford Algebras over R|classification of Clifford algebras]].

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: An orthogonal representation $\rho: G \to SO(n)$ of any Lie group $G$.* If $G$ is simply connected, by the Lie correspondence $\rho$ lifts uniquely to $\tilde\rho: G \to \mathrm{Spin}(n)$; this is "what it means for spin structures to integrate". If $G$ is not simply connected, the lift may not exist (obstruction is the pullback of $w_2$ under $\rho$). Bridge example: the orthogonal action of $SU(2)$ on $\mathbb{R}^3$ via $\mathrm{Ad}$ lifts to itself, since $SU(2) = \mathrm{Spin}(3)$.

*Source 2: An oriented Riemannian/pseudo-Riemannian manifold.* The frame bundle $P_{SO}(M)$ has a structure group $SO(n)$; by the theorem, lifting it to a $\mathrm{Spin}(n)$-bundle is a meaningful question (a *spin structure*), with obstruction $w_2(M) \in H^2(M; \mathbb{Z}/2)$. See [[Def - Spin Structure on a Manifold]].

*Source 3: A representation of $\mathfrak{so}(n)$ via matrices.* By the theorem and the Lie correspondence, this integrates uniquely to a $\mathrm{Spin}(n)$-representation, which is also a representation of $SO(n)$ iff $-1$ acts trivially. The spin representations (those that don't) are *exactly* the spinor representations.

**Targets (Output Amplification)**

*Target 1: Topological invariants of $SO(n)$.* The theorem immediately gives $\pi_1(SO(n)) = \mathbb{Z}/2$ for $n \geq 3$, with the non-trivial element realized by any $2\pi$-rotation loop. Combined with the higher topology of $\mathrm{Spin}(n)$ (e.g., $\mathrm{Spin}(n)$ is the universal cover, so $\pi_k(\mathrm{Spin}(n)) = \pi_k(SO(n))$ for $k \geq 2$), this computes a substantial portion of the homotopy groups of the classical Lie groups.

*Target 2: Classification of spin manifolds.* The spin structure existence is controlled by $w_2 \in H^2(M; \mathbb{Z}/2)$, a topological invariant; the structure (when it exists) is classified by $H^1(M; \mathbb{Z}/2)$.

*Target 3: The Lichnerowicz formula and index theorems.* On a spin manifold, the Dirac operator $\not D$ is defined using the spin double cover; its index is a topological invariant computed by the $\hat A$-genus (Atiyah–Singer). See [[Thm - Lichnerowicz Formula]].

*Target 4: Spin-statistics theorem.* Combined with $\pi_1(SO(3, 1)) = \mathbb{Z}/2$ and the spinor representation structure, the theorem implies that fermions (half-integer spin particles) must obey antisymmetric (Fermi-Dirac) statistics in any spatial dimension $\geq 3$.

---

# Why Is It True

The proof has the same structure as the $SU(2) \to SO(3)$ case but uses the Clifford algebra rather than explicit Pauli matrices. The key idea: $\mathrm{Spin}(n)$ is defined as the subgroup of $\mathrm{Cl}^0(n, 0)^\times$ generated by even-length products of unit vectors. The **twisted adjoint action** $\pi(a)(v) = \alpha(a)va^{-1}$ — using the parity automorphism $\alpha$ — sends $\mathrm{Spin}(n)$ into $SO(n)$ (surjectively, by Cartan–Dieudonné), and the kernel is $\{\pm 1\}$.

**Mechanism in one line: the spin group is the subgroup of the Clifford algebra generated by reflections-and-rotations, and the twisted-adjoint action realizes the orthogonal group as the quotient by $\{\pm 1\}$.**

The crucial new ingredient in dimension $n \geq 3$ is the **Cartan–Dieudonné theorem**: every $T \in O(n)$ is a product of at most $n$ reflections. This is what makes the spin group's twisted-adjoint action surjective onto $SO(n)$: every rotation is the product of an *even* number of reflections, so every $T \in SO(n)$ is in the image of $\mathrm{Spin}(n)$.

The kernel calculation generalises directly from the $SU(2)$ case: an element $a \in \mathrm{Spin}(n)$ in the kernel commutes with all $v \in \mathbb{R}^n$ via twisted conjugation, forcing $a$ to be a scalar. The unit-norm condition $N(a) = 1$ forces $a = \pm 1$.

The simply-connectedness of $\mathrm{Spin}(n)$ for $n \geq 3$ is the deepest ingredient. The proof: $\mathrm{Spin}(n)$ has a natural fibration structure $\mathrm{Spin}(n-1) \to \mathrm{Spin}(n) \to S^{n-1}$ (the spin analogue of $SO(n-1) \to SO(n) \to S^{n-1}$), and combining with the base cases $\mathrm{Spin}(3) = SU(2) = S^3$ (which is simply connected) and inductive use of long exact sequences in homotopy gives $\pi_1(\mathrm{Spin}(n)) = 0$ for $n \geq 3$. Equivalently, $\mathrm{Spin}(n)$ is the universal cover of $SO(n)$ by construction.

---

# What Makes This Hard

The genuinely non-trivial step is verifying that the twisted-adjoint $\pi(v_0)(v) = \alpha(v_0)v v_0^{-1} = -v_0 v v_0$ (for $v_0$ a unit vector) computes to the *reflection* $v \mapsto v - 2B(v, v_0)v_0$ in the hyperplane orthogonal to $v_0$. This requires expanding $v_0 v v_0$ using the Clifford relation $v v_0 + v_0 v = 2B(v, v_0)$ and tracking signs carefully — a calculation that is easy to bungle. The simply-connectedness in dimension $n \geq 3$ requires a topological argument (long exact sequence of homotopy for the fibration $\mathrm{Spin}(n-1) \to \mathrm{Spin}(n) \to S^{n-1}$), and the base case $\mathrm{Spin}(3) = SU(2) = S^3$ is the seed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Define $\mathrm{Spin}(n) \subset \mathrm{Cl}^0(n)$ as the even-parity subgroup generated by unit vectors. Show the twisted adjoint $\pi(a)(v) = \alpha(a)va^{-1}$ sends $\mathrm{Spin}(n) \to SO(n)$; surjectivity follows from Cartan–Dieudonné (every rotation = product of even number of reflections, hence in the image); kernel is $\{\pm 1\}$ by direct computation. Simply-connectedness of $\mathrm{Spin}(n)$ for $n \geq 3$ follows by induction from $\mathrm{Spin}(3) = SU(2) = S^3$.

**Subgoal decomposition:**

1. **Subgoal 1: For a unit vector $v_0$, the twisted adjoint $\pi(v_0)$ is the reflection through $v_0^\perp$.** That is, $\pi(v_0)(v) = v - 2B(v, v_0)v_0/Q(v_0)$ — reduces to the standard formula for $Q(v_0) = 1$.
   - *Hint:* Compute $\alpha(v_0) v v_0^{-1} = -v_0 v v_0$ using $v_0^{-1} = v_0/Q(v_0)$ and the Clifford relation $vv_0 + v_0 v = 2B(v, v_0)$.
   - *Why needed:* This is the geometric content of why spin elements correspond to rotations.

2. **Subgoal 2: $\pi$ maps $\mathrm{Spin}(n) \to SO(n)$.** Even number of reflections = orientation-preserving = element of $SO(n)$.
   - *Hint:* Cartan–Dieudonné + parity argument.
   - *Why needed:* Defines the domain of the cover.

3. **Subgoal 3: $\pi$ is surjective.** Every $T \in SO(n)$ is a product of an even number of reflections, hence lifts to $\mathrm{Spin}(n)$.
   - *Hint:* Cartan–Dieudonné.
   - *Why needed:* Surjectivity is the second main conclusion.

4. **Subgoal 4: $\ker\pi = \{\pm 1\}$.** Elements of the kernel commute (in the twisted sense) with all $v \in \mathbb{R}^n$, forcing them to be scalars.
   - *Hint:* Use the parity grading: even elements commuting with all of $V$ must be central in the even subalgebra, and the center of $\mathrm{Cl}^0(n)$ is the scalars.
   - *Why needed:* Kernel determines the cover-degree.

5. **Subgoal 5: $\mathrm{Spin}(n)$ is simply connected for $n \geq 3$.**
   - *Hint:* Long exact sequence of homotopy for $\mathrm{Spin}(n-1) \to \mathrm{Spin}(n) \to S^{n-1}$; base case $\mathrm{Spin}(3) = SU(2) = S^3$ from [[Thm - SU(2) is the Double Cover of SO(3)]]; $S^{n-1}$ is simply connected for $n \geq 3$.
   - *Why needed:* This makes $\mathrm{Spin}(n)$ the universal cover and gives $\pi_1(SO(n)) = \mathbb{Z}/2$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Twisted-adjoint of a unit vector is reflection.
> **Statement:** For $v_0 \in V$ with $Q(v_0) = 1$, the twisted-adjoint $\pi(v_0): V \to V$ given by $\pi(v_0)(v) = -v_0 v v_0$ equals the reflection $R_{v_0}(v) = v - 2B(v, v_0)v_0$ in the hyperplane $v_0^\perp$.
>
> **Hint:** Expand $v_0 v v_0$ using $vv_0 + v_0 v = 2B(v, v_0)$.
>
> **Why needed:** Establishes the geometric meaning of spin elements as reflections.
>
> > [!note]- Full proof
> > Compute $\pi(v_0)(v) = -v_0 v v_0 = -v_0(2B(v, v_0) - v_0 v) = -2B(v, v_0) v_0 + v_0^2 v = -2B(v, v_0)v_0 + Q(v_0) v = v - 2B(v, v_0)v_0$ (using $Q(v_0) = 1$). The RHS is the reflection formula.

> [!note]- Lemma 2: Cartan–Dieudonné.
> **Statement:** Every element of $O(V, Q)$ (for $\dim V = n$) is a product of at most $n$ reflections.
>
> **Hint:** Induct on $n$. If $T \in O(V, Q)$ fixes a non-zero vector $v_0$, use the inductive hypothesis on $v_0^\perp$ (an $(n-1)$-dimensional subspace). Otherwise, compose with a reflection to reduce to the previous case.
>
> **Why needed:** This is the surjectivity statement for $\mathrm{Pin}(n) \to O(n)$ (and by parity for $\mathrm{Spin}(n) \to SO(n)$).
>
> > [!note]- Full proof (sketch)
> > Induct on $n$. For $n = 0$ trivial. Assume the result for $n - 1$; let $T \in O(V, Q)$ with $\dim V = n$. If $T$ has a fixed vector $v_0 \neq 0$, then $T|_{v_0^\perp} \in O(v_0^\perp, Q|_{v_0^\perp})$ is a product of at most $n - 1$ reflections (by induction), and these extend by identity on $v_0$. If $T$ has no fixed vector, pick any $v$ and let $w = T(v) - v$; the reflection $R$ through $w^\perp$ satisfies $R \circ T(v) = v$, so $R \circ T$ fixes $v$, hence is a product of at most $n - 1$ reflections; so $T$ is a product of at most $n$.

> [!note]- Lemma 3: The kernel of $\pi$ is $\{\pm 1\}$.
> **Statement:** $\ker\pi = \{a \in \mathrm{Spin}(n) : \alpha(a) v a^{-1} = v \text{ for all } v \in V\} = \{\pm 1\}$.
>
> **Hint:** The condition $\alpha(a) v = va$ for all $v$ means $a$ commutes with all of $V$ in a parity-twisted sense. Use this to show $a$ must be a scalar.
>
> **Why needed:** The cover is exactly $2$-fold; the kernel size is $2$.
>
> > [!note]- Full proof (sketch)
> > Suppose $a \in \mathrm{Cl}^0(n)$ (even part) commutes with all $v \in V$ in the sense $\alpha(a)v = va$, equivalently (since $\alpha(a) = a$ for even $a$) $av = va$. So $a$ is in the center of $\mathrm{Cl}^0(n)$. For $n \geq 3$, the center of $\mathrm{Cl}^0(n)$ is the scalars $\mathbb{R} \cdot 1$ (a check using the basis $\{e_{i_1}\cdots e_{i_{2k}}\}$ and analyzing what commutes with $e_j$ for each $j$). So $a = \lambda \cdot 1$ for some $\lambda \in \mathbb{R}$. The norm condition $N(a) = a^t\alpha(a) = a^t a = \lambda^2 = 1$ forces $\lambda = \pm 1$.

> [!note]- Lemma 4: $\mathrm{Spin}(n)$ acts transitively on the unit sphere $S^{n-1} \subset \mathbb{R}^n$, with stabilizer $\mathrm{Spin}(n-1)$.
> **Statement:** $\mathrm{Spin}(n)/\mathrm{Spin}(n-1) \cong S^{n-1}$.
>
> **Hint:** The action of $\mathrm{Spin}(n)$ on $\mathbb{R}^n$ via $\pi$ is the same as $SO(n)$'s action; both groups act transitively on $S^{n-1}$ with stabilizer of a unit vector $\cong \mathrm{Spin}(n-1)$ (or $SO(n-1)$).
>
> **Why needed:** This gives the fibration $\mathrm{Spin}(n-1) \to \mathrm{Spin}(n) \to S^{n-1}$ used to compute homotopy.
>
> > [!note]- Full proof (sketch)
> > $\mathrm{Spin}(n)$ acts on $\mathbb{R}^n$ via $\pi$; since the $SO(n)$-action is transitive on $S^{n-1}$ and $\pi$ is surjective, the $\mathrm{Spin}(n)$-action is also transitive. The stabilizer of a unit vector $e_n$ is $\pi^{-1}(\mathrm{Stab}_{SO(n)}(e_n)) = \pi^{-1}(SO(n-1)) = \mathrm{Spin}(n-1)$ (the lift of $SO(n-1)$).

> [!note]- Lemma 5: Simply-connectedness of $\mathrm{Spin}(n)$ for $n \geq 3$.
> **Statement:** $\pi_1(\mathrm{Spin}(n)) = 0$ for $n \geq 3$.
>
> **Hint:** Long exact sequence of homotopy for $\mathrm{Spin}(n-1) \to \mathrm{Spin}(n) \to S^{n-1}$: $\pi_1(S^{n-1}) \to \pi_1(\mathrm{Spin}(n)) \to \pi_0(\mathrm{Spin}(n-1))$. For $n \geq 4$, both ends are trivial, so $\pi_1(\mathrm{Spin}(n)) = 0$. Base case $n = 3$: $\mathrm{Spin}(3) = SU(2) = S^3$ is simply connected.
>
> **Why needed:** Confirms $\mathrm{Spin}(n)$ is the universal cover and gives $\pi_1(SO(n)) = \mathbb{Z}/2$.

---

# Formal Proof

> [!note]- Complete formal proof (outline)
> **Setup.** Let $V = \mathbb{R}^n$ with standard Euclidean form. $\mathrm{Cl}(n) := \mathrm{Cl}(V, |\cdot|^2)$, with parity automorphism $\alpha$ and transpose anti-automorphism $t$. $\mathrm{Pin}(n) := \{a_1 \cdots a_k \in \mathrm{Cl}(n) : a_j \in V, Q(a_j) = \pm 1\}$, $\mathrm{Spin}(n) := \mathrm{Pin}(n) \cap \mathrm{Cl}^0(n)$. Twisted adjoint $\pi: \mathrm{Pin}(n) \to GL(V)$, $\pi(a)(v) = \alpha(a) v a^{-1}$.
>
> **Step 1.** $\pi(v_0) \in O(V, Q)$ for $v_0$ a unit vector: by Lemma 1, $\pi(v_0)$ is reflection through $v_0^\perp$, which is an orthogonal transformation. For products $a = v_1 \cdots v_k$, $\pi(a) = \pi(v_1)\cdots\pi(v_k)$, a product of reflections, hence in $O(V, Q)$.
>
> **Step 2.** $\pi(\mathrm{Spin}(n)) \subseteq SO(n)$: Spin elements are products of *even* numbers of reflections, hence have determinant $(-1)^{2k} = 1$, hence in $SO(n)$.
>
> **Step 3.** Surjectivity $\pi(\mathrm{Spin}(n)) = SO(n)$: By Cartan–Dieudonné (Lemma 2), every $T \in SO(n)$ is a product of an even number of reflections (since $\det T = +1$, the parity of the number of reflections must be even). So $T = \pi(a)$ for some $a$ that is a product of an even number of unit vectors, hence $a \in \mathrm{Spin}(n)$.
>
> **Step 4.** Kernel computation $\ker\pi = \{\pm 1\}$: By Lemma 3.
>
> **Step 5.** $\pi$ is a smooth $2:1$ covering: $\pi$ is a smooth homomorphism (Clifford multiplication and inverse are smooth); a smooth surjective Lie group homomorphism with discrete kernel is a covering map; the kernel has $2$ elements.
>
> **Step 6.** $\mathrm{Spin}(n)$ is simply connected for $n \geq 3$: By Lemma 5.
>
> **Step 7.** $\pi$ is the universal cover, and $\pi_1(SO(n)) = \ker\pi = \mathbb{Z}/2$.

---

# Cross-Field Exercise Suggestions

1. **Compute $\mathrm{Spin}(4) = SU(2) \times SU(2)$.** Verify the accidental isomorphism: $\mathrm{Cl}^0(4) = \mathbb{H} \oplus \mathbb{H}$, and the spin group inside is $(SU(2))_L \times (SU(2))_R$. The cover sends $(q_L, q_R)$ to the rotation $v \mapsto q_L v q_R^{-1}$ on $\mathbb{R}^4 \cong \mathbb{H}$. This is the source of the self-dual/anti-self-dual decomposition of 2-forms in 4 dimensions, key to gauge theory.

2. **Construct the spin structure on the round $S^n$.** Use the bundle isomorphism $TS^n \oplus \mathbb{R} \cong S^n \times \mathbb{R}^{n+1}$. Restrict the spin structure on $\mathbb{R}^{n+1}$ (which is trivially spin, being parallelizable) to $TS^n$; this is the canonical spin structure on $S^n$. See [[Ex - Spin Structure on the Sphere S^n]].

3. **Identify $\mathrm{Spin}(5) = Sp(2)$.** Show that $\mathrm{Cl}^0(5) = M_2(\mathbb{H})$, and the spin group $\mathrm{Spin}(5) \subset \mathrm{Cl}^0(5)$ is exactly the compact symplectic group $Sp(2)$ — the group of $2 \times 2$ quaternionic matrices preserving the standard quaternionic Hermitian form.

---

# Bridges

- **$\mathrm{SL}(2, \mathbb{C}) = \mathrm{Spin}^+(1, 3)$ — the Lorentzian analog.** In Minkowski signature $(1, 3)$, the spin group is $\mathrm{SL}(2, \mathbb{C})$ — a complex Lie group of complex dimension $3$, real dimension $6$, matching $SO^+(1, 3)$. The cover $\mathrm{SL}(2, \mathbb{C}) \to SO^+(1, 3)$ is constructed by acting on Hermitian $2 \times 2$ matrices via $X \to AXA^\dagger$ (rather than the Euclidean $vAv^{-1}$). Critical for relativistic quantum mechanics.

- **Accidental isomorphisms in low dimensions.** $\mathrm{Spin}(3) = SU(2)$, $\mathrm{Spin}(4) = SU(2) \times SU(2)$, $\mathrm{Spin}(5) = Sp(2)$, $\mathrm{Spin}(6) = SU(4)$ — these "coincidences" are direct consequences of the Clifford classification (low-dim entries) and have deep implications for low-dimensional geometry. The disappearance of these isomorphisms for $n \geq 7$ is why higher-dimensional spin groups are intrinsically "their own thing".

- **Higher-cover hierarchy: $\mathrm{String}(n)$ and beyond.** $\mathrm{Spin}(n)$ is the first non-trivial cover in a tower: $O(n) \supset SO(n) \supset \mathrm{Spin}(n) \supset \mathrm{String}(n) \supset \mathrm{Fivebrane}(n) \supset \cdots$, with each successive cover removing more topology. String structures (killing $\tfrac{1}{2}p_1$) arise in heterotic string theory; fivebrane structures (killing higher Pontryagin classes) are relevant for M-theory.

- **Spin manifolds and obstruction theory.** The lift of the $SO(n)$-frame bundle to $\mathrm{Spin}(n)$ on a manifold $M$ is obstructed by $w_2(M)$; the classification of spin structures (when one exists) is via $H^1(M; \mathbb{Z}/2)$. See [[Def - Spin Structure on a Manifold]].

---

# Unlocked by This

> [!tip] Topological Classification of Free Fermion Systems
> The theorem underlies the topological classification of free fermion systems in condensed-matter physics. **Topological insulators**, **topological superconductors**, and **Weyl semimetals** are all classified by the topology of the band structure modulo various symmetry constraints, and the relevant classifying spaces involve $\mathrm{Spin}(n)$. The "tenfold way" of Altland–Zirnbauer (2002) catalogues 10 symmetry classes; their classifications follow a period-8 pattern derivable from the Clifford-algebra structure of the spin group.

> [!tip] $\mathrm{Spin}^c$ Structures and Seiberg-Witten Theory
> The $\mathrm{Spin}^c$ group $\mathrm{Spin}^c(n) := \mathrm{Spin}(n) \times_{\mathbb{Z}/2} U(1)$ is a "spin-with-twist" extension that exists on a wider class of manifolds (every almost-complex manifold). The **Seiberg-Witten equations** are a coupled system involving a $\mathrm{Spin}^c$ Dirac operator and a curvature equation; they led to a revolutionary set of $4$-dimensional invariants in the mid-1990s, replacing Donaldson theory and dramatically advancing 4-manifold topology.

> [!tip] Spin Bordism and Spin Cobordism
> The set of $n$-dimensional closed spin manifolds modulo spin-bordism (existence of a spin manifold with both as boundary, with the right structure) forms the **spin cobordism group** $\Omega_n^{\mathrm{Spin}}$. The theorem $\mathrm{Spin}(n) \to SO(n)$ being a double cover is what allows the definition of spin bordism; the resulting graded ring structure is computed by Anderson-Brown-Peterson (1966) and is a basic invariant in algebraic topology.

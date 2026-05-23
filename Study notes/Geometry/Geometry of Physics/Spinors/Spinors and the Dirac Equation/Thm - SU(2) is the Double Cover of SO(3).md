---
type: theorem
subject: spinors
prereqs:
  - "Def - The Pauli Matrices"
  - "Def - SU(2) Action on Spinors"
  - "Def - Adjoint Representation"
  - "Def - Lie Group Homomorphism"
tags: [geometry, spinors, lie-groups, topology]
---

# Notation

$SU(2)$ is the group of $2 \times 2$ complex unitary matrices with determinant $1$. $SO(3)$ is the group of $3 \times 3$ real orthogonal matrices with determinant $1$. The Pauli matrices $\sigma_1, \sigma_2, \sigma_3$ are the standard $2 \times 2$ Hermitian generators. For $\vec x \in \mathbb{R}^3$, $\vec x \cdot \vec\sigma = \sum_j x^j \sigma_j$ is the corresponding traceless Hermitian matrix. The adjoint action of $u \in SU(2)$ on $A \in M_2(\mathbb{C})$ is $\mathrm{Ad}_u(A) = uAu^{-1}$. The kernel of a group homomorphism $\varphi: G \to H$ is $\ker\varphi = \{g \in G : \varphi(g) = e_H\}$.

---

# Statement

> **Theorem (Cartan / Cayley–Klein).** Define $\mathrm{Ad}: SU(2) \to GL(\mathbb{R}^3)$ by the requirement
> $$\mathrm{Ad}_u(\vec x \cdot \vec\sigma) = (\mathrm{Ad}_u\, \vec x) \cdot \vec\sigma \qquad \text{for all } \vec x \in \mathbb{R}^3,$$
> i.e., $u(\vec x \cdot \vec\sigma)u^{-1}$ is a traceless Hermitian matrix equal to $\vec y \cdot \vec\sigma$ for some $\vec y \in \mathbb{R}^3$, and $\mathrm{Ad}_u(\vec x) := \vec y$. Then:
>
> 1. $\mathrm{Ad}_u \in SO(3)$ for every $u \in SU(2)$;
> 2. $\mathrm{Ad}: SU(2) \to SO(3)$ is a surjective Lie group homomorphism;
> 3. $\ker\mathrm{Ad} = \{\pm I_2\} \subset SU(2)$;
> 4. $\mathrm{Ad}$ is a $2:1$ covering map, and $SU(2) \cong S^3$ is the universal cover of $SO(3) \cong \mathbb{RP}^3$.

In particular, $\pi_1(SO(3)) = \mathbb{Z}/2$, with the non-trivial loop corresponding to a $2\pi$ rotation about any axis.

> **Corollary (consequences for representations).** Every irreducible representation of $\mathfrak{so}(3) \cong \mathfrak{su}(2)$ integrates uniquely to a representation of $SU(2)$; it descends to $SO(3)$ iff it is of integer spin. The half-integer spin representations are intrinsically spinorial: they exist on $SU(2)$ but cannot be realized on $SO(3)$ alone.

---

# Motivation

The theorem answers the question: **what is the relationship between rotations of $\mathbb{R}^3$ and $2 \times 2$ unitary matrices?** Naively, $SO(3)$ and $SU(2)$ are very different groups — one acts on $\mathbb{R}^3$, the other on $\mathbb{C}^2$. But they have *the same Lie algebra*: $\mathfrak{so}(3) \cong \mathfrak{su}(2) \cong (\mathbb{R}^3, \times)$ as Lie algebras over $\mathbb{R}$. The theorem makes this isomorphism global: there is an *explicit* surjective map $SU(2) \to SO(3)$ that realizes the isomorphism at the group level, and the price for this is that the map is $2:1$ rather than $1:1$.

The physical importance is enormous. The wave function of an electron, when its spatial coordinates are rotated, transforms by an element of $SU(2)$ (not $SO(3)$). A rotation by $2\pi$ corresponds to $-I \in SU(2)$, which acts on a spinor by $\psi \to -\psi$ — the famous "spinors flip sign under $2\pi$ rotations". A rotation by $4\pi$ returns the spinor to itself. This is the **topological signature of $\pi_1(SO(3)) = \mathbb{Z}/2$**, and it has direct experimental consequences (the **Aharonov–Susskind experiment** demonstrates the effect with macroscopic apparatus).

The theorem is a flagship of Lie group theory because it is the simplest nontrivial example of the universal cover phenomenon, and because the cover is constructed by an *explicit formula* (conjugation in the Pauli algebra) rather than abstractly. It is also the prototype for the higher-dimensional analogues $\mathrm{Spin}(n) \to SO(n)$ and $\mathrm{SL}(2, \mathbb{C}) \to L_0$, which underpin all of spinor physics in arbitrary dimension and signature.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: A general representation of $\mathfrak{su}(2)$ on a vector space $V$.* Any Lie algebra representation $\rho: \mathfrak{su}(2) \to \mathfrak{gl}(V)$ can be integrated to a representation of $SU(2)$ (since $SU(2)$ is simply connected), but it descends to $SO(3)$ iff the central element $\exp(\pi(\tfrac{i}{2})\vec\sigma\cdot\hat n) = -I$ acts trivially on $V$. The theorem provides the criterion: $V$ is an $SO(3)$-representation iff it is *integer spin*. Bridge example: the spin-$\tfrac{1}{2}$ Pauli matrix representation does not descend; this is *why* it deserves to be called a spinor.

*Source 2: A unit quaternion $q \in \mathbb{H}^\times_1$.* Via $\mathbb{H}^\times_1 \cong SU(2)$, every unit quaternion gives a rotation of $\mathbb{R}^3$ — specifically, the rotation $\vec v \mapsto q\vec v q^{-1}$ of $\mathrm{Im}(\mathbb{H}) \cong \mathbb{R}^3$. This is the source-side bridge from quaternion-multiplication problems to rotation-composition problems. Example: composing two rotations in $\mathbb{R}^3$ is computationally easier as a quaternion product than as a $3 \times 3$ matrix product — quaternions are widely used in computer graphics for this reason.

*Source 3: A connected Lie group $\widetilde G$ with $\widetilde G \to SO(3)$ a $2:1$ covering.* By the theorem, $\widetilde G \cong SU(2)$ (unique double cover). Bridge: the **closed subgroup theorem** + connectedness of $\widetilde G$ + the kernel structure forces the isomorphism. This is the source-side argument that identifies, e.g., the spin representation of $\mathrm{Spin}(3)$ with $SU(2)$ without doing an independent construction.

*Source 4: A homotopy class of loops in $SO(3)$.* The fundamental group $\pi_1(SO(3)) = \mathbb{Z}/2$ is detected by lifting loops to $SU(2)$: a loop in $SO(3)$ is nontrivial iff it lifts to an open path in $SU(2)$ ending at $-I$. Bridge: this provides a *topological* test for whether two paths of rotations in $\mathbb{R}^3$ are homotopic, useful in robotics, computer vision, and the topology of configuration spaces.

**Targets (Output Amplification)**

*Target 1: $SO(3)$-representation theory in terms of $SU(2)$-representation theory.* Every $SO(3)$-representation is an $SU(2)$-representation in which $-I$ acts as the identity; this reduces the classification of $SO(3)$-reps to selecting the integer-spin reps from the full $SU(2)$ list. Combined with the **highest-weight theorem** for $\mathfrak{su}(2)$, this gives a complete classification.

*Target 2: Topological invariants of $SO(3)$ via $SU(2)$.* $\pi_1(SO(3)) = \mathbb{Z}/2$ from the cover; $H^*(SO(3); \mathbb{Q}) = H^*(S^3; \mathbb{Q}) = \mathbb{Q}[x]/(x^2)$ with $x$ in degree $3$; $SO(3)$ is *parallelizable* (since $S^3$ is, being a Lie group). Combined with the further fact that $SO(3) = \mathbb{RP}^3$, this gives a complete topological description.

*Target 3: Existence of spinor fields in physics.* Combined with the spin-statistics theorem (in QFT), the theorem implies that fermions exist as a distinct species of particle from bosons. The half-integer-spin representations of $SU(2)$ — which exist *only* because of the cover — are the fermion species: electron, proton, neutron, all quarks, all leptons.

*Target 4: Construction of spin structures on manifolds.* For a 3-dimensional orientable manifold $M^3$, $w_2(M) = 0$ automatically, so spin structures exist. The theorem's existence of the cover $SU(2) \to SO(3)$ is the local model for the global lift of frame bundles — see [[Def - Spin Structure on a Manifold]].

---

# Why Is It True

The theorem is true because of a single algebraic miracle: **the space of traceless Hermitian $2 \times 2$ matrices is a $3$-dimensional real vector space, isomorphic to $\mathbb{R}^3$ via the Pauli basis**, and conjugation by unitary matrices preserves both *traceless* and *Hermitian* — so $\mathrm{Ad}_u$ acts on this 3-dimensional space, and the action preserves the natural inner product (since conjugation preserves the trace, and the trace gives the inner product). So $\mathrm{Ad}_u \in O(3)$. Continuity and connectedness of $SU(2)$ (it is $S^3$, connected) then force $\mathrm{Ad}_u \in SO(3)$ (the identity component).

**The mechanism in one line: $\mathrm{Ad}_u$ is the linear action of $SU(2)$ on its own Lie algebra $\mathfrak{su}(2) \cong i\mathfrak{u}(2)_0 \cong \mathbb{R}^3$, and this 3-dimensional real action is exactly an $SO(3)$ rotation.**

Why is the map surjective? Because the Lie-algebra-level map $\mathrm{ad}: \mathfrak{su}(2) \to \mathfrak{so}(3)$ is an isomorphism (both are $3$-dimensional, the bracket structures match), the differential $d\mathrm{Ad}_I = \mathrm{ad}$ is bijective, so $\mathrm{Ad}$ is a local diffeomorphism at $I$. The image is therefore an open subgroup of $SO(3)$; since $SO(3)$ is connected, the open subgroup must be all of $SO(3)$.

Why is the kernel $\{\pm I\}$? An element $u \in \ker\mathrm{Ad}$ commutes (under conjugation) with every Pauli matrix, hence with every $\vec x \cdot \vec\sigma$, hence with every traceless Hermitian matrix. Adding back the identity (which all such $u$ commute with), $u$ commutes with all of $M_2(\mathbb{C})$ — so $u$ is a scalar, $u = \lambda I$ for some $\lambda$. Unit determinant forces $\lambda^2 = 1$, so $\lambda = \pm 1$.

Why is the cover *exactly* $2:1$? The kernel has $2$ elements, and the action is transitive on each $SO(3)$-orbit (which contains both $u$ and $-u$ above any given rotation). So the fiber has $|\ker\mathrm{Ad}| = 2$ points.

Why is $SU(2) \cong S^3$ simply connected? Any $u \in SU(2)$ has the form $u = aI + ib\sigma_1 + ic\sigma_2 + id\sigma_3$ with $a^2 + b^2 + c^2 + d^2 = 1$ — this gives an embedding $SU(2) \hookrightarrow \mathbb{R}^4$ identifying it with the unit sphere $S^3$. The sphere $S^3$ is simply connected ($n = 3 \geq 2$), so $SU(2)$ is too.

---

# What Makes This Hard

The technical step that catches most readers is showing that the kernel is *exactly* $\{\pm I\}$ rather than something larger. The argument requires noticing that "commuting with all traceless Hermitian matrices via conjugation" forces $u$ to be a scalar, which uses Schur's lemma or the explicit decomposition of $M_2(\mathbb{C})$ into commutative-with-$\vec\sigma$-vs-not. A common error is to compute $u\sigma_3 u^{-1} = \sigma_3$ and conclude $u$ is diagonal, then $u\sigma_1 u^{-1} = \sigma_1$ and conclude $u$ has equal diagonal entries — but the synthesis of these requires care. The topological step — showing the cover is $2:1$ globally, not just locally — requires connectedness of $SU(2)$ and the open-subgroup argument; this is straightforward but is the part where many quick "intuitive" derivations are incomplete.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** The map $\mathrm{Ad}: SU(2) \to GL(\mathbb{R}^3)$ via Pauli-conjugation lands in $SO(3)$ (preserves trace pairing); it is a local diffeo at $I$ (Lie algebra iso, $\dim SU(2) = 3 = \dim SO(3)$); it is surjective onto a connected open subgroup, hence all of $SO(3)$; the kernel is $\{\pm I\}$ by direct computation; the cover is universal because $SU(2) \cong S^3$ is simply connected.

**Subgoal decomposition:**

1. **Subgoal 1: The space $V = \{\vec x \cdot \vec\sigma : \vec x \in \mathbb{R}^3\}$ of traceless Hermitian matrices is preserved by $\mathrm{Ad}_u$ for $u \in SU(2)$.**
   - *Hint:* Show conjugation by a unitary preserves Hermiticity and trace.
   - *Why needed:* Without this, $\mathrm{Ad}_u$ doesn't even map $\mathbb{R}^3 \to \mathbb{R}^3$.

2. **Subgoal 2: The action of $\mathrm{Ad}_u$ on $V \cong \mathbb{R}^3$ preserves the inner product $\langle A, B\rangle = \tfrac{1}{2}\mathrm{tr}(AB)$.**
   - *Hint:* Cyclic invariance of trace: $\mathrm{tr}(uAu^{-1} \cdot uBu^{-1}) = \mathrm{tr}(uABu^{-1}) = \mathrm{tr}(AB)$.
   - *Why needed:* Establishes $\mathrm{Ad}_u \in O(3)$, then connectedness $\implies SO(3)$.

3. **Subgoal 3: $\mathrm{Ad}_u \in SO(3)$ (i.e., $\det\mathrm{Ad}_u = +1$).**
   - *Hint:* $u \mapsto \mathrm{Ad}_u$ is continuous, $\det \in \{\pm 1\}$, and $\mathrm{Ad}_I = I$.
   - *Why needed:* The map should land in $SO(3)$ — the special orthogonal group — not just $O(3)$.

4. **Subgoal 4: The Lie-algebra differential $d\mathrm{Ad}_I: \mathfrak{su}(2) \to \mathfrak{so}(3)$ is a Lie algebra isomorphism.**
   - *Hint:* Compute $d\mathrm{Ad}_I(\tfrac{i}{2}\sigma_j) = E_j$ (the standard basis of $\mathfrak{so}(3)$) directly from $\mathrm{Ad}_{\exp(\tfrac{i}{2}t\sigma_j)}(\vec x \cdot \vec\sigma)$ expanded to first order in $t$.
   - *Why needed:* Both algebras are $3$-dimensional with matching brackets; this is the Lie-algebra-level isomorphism that drives everything.

5. **Subgoal 5: $\mathrm{Ad}$ is a local diffeomorphism at $I$, hence surjective onto $SO(3)$ by connectedness.**
   - *Hint:* Inverse function theorem (from Subgoal 4); image is open; $SO(3)$ is connected; open subgroup of connected group is the whole group.
   - *Why needed:* Surjectivity is the second main conclusion.

6. **Subgoal 6: $\ker\mathrm{Ad} = \{\pm I\}$.**
   - *Hint:* $u \in \ker$ means $u\sigma_j u^{-1} = \sigma_j$ for all $j$; in particular $u\sigma_3 u^{-1} = \sigma_3$ forces $u$ diagonal; then $u\sigma_1 u^{-1} = \sigma_1$ forces equal diagonal entries; together with $\det u = 1$, get $u = \pm I$.
   - *Why needed:* The kernel computation gives the $2:1$ character of the cover.

7. **Subgoal 7: $SU(2) \cong S^3$ and is simply connected.**
   - *Hint:* The map $u = aI + ib\sigma_1 + ic\sigma_2 + id\sigma_3 \mapsto (a, b, c, d)$ gives a bijection $SU(2) \to S^3 \subset \mathbb{R}^4$; $S^3$ is simply connected.
   - *Why needed:* Together with the $2:1$ cover, this makes $SU(2)$ the universal cover of $SO(3)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Conjugation by a unitary preserves the trace pairing.
> **Statement:** For $u \in U(n)$ and $A, B \in M_n(\mathbb{C})$, $\mathrm{tr}(uAu^{-1} \cdot uBu^{-1}) = \mathrm{tr}(AB)$.
>
> **Hint:** Use the cyclic invariance of the trace.
>
> **Why needed:** Together with conjugation preserving "Hermitian" and "traceless", this shows $\mathrm{Ad}_u$ acts as an orthogonal transformation on the space of traceless Hermitian matrices.
>
> > [!note]- Full proof
> > $\mathrm{tr}(uAu^{-1} \cdot uBu^{-1}) = \mathrm{tr}(uA \cdot Bu^{-1}) = \mathrm{tr}(u^{-1}uAB) = \mathrm{tr}(AB)$ using $uu^{-1} = I$ and the cyclic property $\mathrm{tr}(XY) = \mathrm{tr}(YX)$.

> [!note]- Lemma 2: $\mathrm{Ad}_u$ preserves the space of traceless Hermitian matrices.
> **Statement:** For $u \in SU(2)$ and $A$ traceless Hermitian, $uAu^{-1}$ is also traceless Hermitian.
>
> **Hint:** Trace is conjugation-invariant; Hermiticity is preserved under conjugation by unitaries because $(uAu^{-1})^\dagger = (u^{-1})^\dagger A^\dagger u^\dagger = uA^\dagger u^{-1} = uAu^{-1}$.
>
> **Why needed:** This is what lets us *define* $\mathrm{Ad}_u: \mathbb{R}^3 \to \mathbb{R}^3$ at all — without it, $u(\vec x \cdot \vec\sigma)u^{-1}$ would not be of the form $\vec y \cdot \vec\sigma$.
>
> > [!note]- Full proof
> > Traceless: $\mathrm{tr}(uAu^{-1}) = \mathrm{tr}(A) = 0$. Hermitian: $(uAu^{-1})^\dagger = (u^{-1})^\dagger A^\dagger u^\dagger = uAu^{-1}$ using $u^\dagger = u^{-1}$ (unitarity) and $A^\dagger = A$ (Hermiticity).

> [!note]- Lemma 3: Lie-algebra differential at $I$ is an isomorphism.
> **Statement:** The map $d\mathrm{Ad}_I: \mathfrak{su}(2) \to \mathfrak{so}(3)$ defined by $d\mathrm{Ad}_I(X) = \tfrac{d}{dt}|_{t=0}\mathrm{Ad}_{\exp tX}$ is a Lie algebra isomorphism.
>
> **Hint:** Use $\mathfrak{su}(2)$ basis $\{\tfrac{i}{2}\sigma_j\}$ and $\mathfrak{so}(3)$ basis $\{E_j\}$ where $E_j$ is the infinitesimal rotation about the $j$-th axis. Compute $d\mathrm{Ad}_I(\tfrac{i}{2}\sigma_j)(\vec x \cdot \vec\sigma) = \tfrac{i}{2}[\sigma_j, \vec x \cdot \vec\sigma]$ using $[\sigma_j, \sigma_k] = 2i\epsilon_{jkl}\sigma_l$ to identify this as $-\epsilon_{jkl}x^k\sigma_l = E_j(\vec x)\cdot\vec\sigma$.
>
> **Why needed:** This is the bridge between the algebraic constructions on $\mathfrak{su}(2)$ and the geometric structure of rotations.
>
> > [!note]- Full proof
> > Take $X = \tfrac{i}{2}\sigma_j \in \mathfrak{su}(2)$. Then $\mathrm{Ad}_{\exp tX}(\vec x \cdot \vec\sigma) = \exp(t\tfrac{i}{2}\sigma_j) \cdot (\vec x \cdot \vec\sigma) \cdot \exp(-t\tfrac{i}{2}\sigma_j)$. Expanding to first order: $(\vec x \cdot \vec\sigma) + t\tfrac{i}{2}[\sigma_j, \vec x \cdot \vec\sigma] + O(t^2)$. Using $[\sigma_j, \sigma_k] = 2i\epsilon_{jkl}\sigma_l$: $\tfrac{i}{2}[\sigma_j, \vec x \cdot \vec\sigma] = \tfrac{i}{2} x^k \cdot 2i\epsilon_{jkl}\sigma_l = -\epsilon_{jkl}x^k\sigma_l$. This says $d\mathrm{Ad}_I(\tfrac{i}{2}\sigma_j)$ sends $\vec x$ to $\vec y$ with $y^l = -\epsilon_{jkl}x^k = -(\epsilon_{jkl}x^k) = (e_j \times \vec x)^l$, which is exactly the infinitesimal rotation $E_j$ about the $j$-axis. So $d\mathrm{Ad}_I$ sends the basis $\{\tfrac{i}{2}\sigma_j\}$ of $\mathfrak{su}(2)$ to the basis $\{E_j\}$ of $\mathfrak{so}(3)$ — a Lie algebra isomorphism.

> [!note]- Lemma 4: Kernel computation.
> **Statement:** $\ker\mathrm{Ad} = \{\pm I_2\}$.
>
> **Hint:** $u \in \ker\mathrm{Ad}$ iff $u\sigma_j u^{-1} = \sigma_j$ for $j = 1, 2, 3$. Conjugation with $\sigma_3$ forces $u$ diagonal; conjugation with $\sigma_1$ then forces equal diagonal entries.
>
> **Why needed:** The kernel size $2$ is what makes the cover $2:1$.
>
> > [!note]- Full proof
> > Suppose $u\sigma_3 u^{-1} = \sigma_3$. Write $u = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Then $u\sigma_3 = \begin{pmatrix} a & -b \\ c & -d \end{pmatrix}$ and $\sigma_3 u = \begin{pmatrix} a & b \\ -c & -d \end{pmatrix}$. So $u\sigma_3 = \sigma_3 u$ requires $b = -b$ and $c = -c$, i.e., $b = c = 0$. So $u = \mathrm{diag}(a, d)$. Now $u\sigma_1 u^{-1} = \sigma_1$ with $u = \mathrm{diag}(a, d)$: $u\sigma_1 = \begin{pmatrix} 0 & a \\ d & 0\end{pmatrix}$ and $\sigma_1 u = \begin{pmatrix} 0 & d \\ a & 0\end{pmatrix}$, so we need $a = d$. Combined with $\det u = ad = 1$ and $u \in SU(2)$ (so $|a|^2 = |d|^2 = 1$, $a^2 = 1$), get $a = d = \pm 1$. So $u = \pm I$.

> [!note]- Lemma 5: $SU(2) \cong S^3$.
> **Statement:** The map $\Phi: \{(a, b, c, d) \in \mathbb{R}^4 : a^2 + b^2 + c^2 + d^2 = 1\} \to SU(2)$ given by $(a, b, c, d) \mapsto aI + ib\sigma_1 + ic\sigma_2 + id\sigma_3$ is a diffeomorphism onto $SU(2)$, identifying $SU(2)$ with the unit $3$-sphere $S^3 \subset \mathbb{R}^4$.
>
> **Hint:** A general $SU(2)$ matrix has the form $\begin{pmatrix} \alpha & \beta \\ -\bar\beta & \bar\alpha\end{pmatrix}$ with $|\alpha|^2 + |\beta|^2 = 1$; writing $\alpha = a + id$ and $\beta = c + ib$ (or similar) and decomposing into the Pauli-matrix basis gives the formula.
>
> **Why needed:** $S^3$ is simply connected, so this shows $SU(2)$ is too — hence $SU(2)$ is the universal cover of $SO(3)$.
>
> > [!note]- Full proof
> > A general element of $SU(2)$ has the form $\begin{pmatrix} \alpha & \beta \\ -\bar\beta & \bar\alpha\end{pmatrix}$ with $|\alpha|^2 + |\beta|^2 = 1$. Writing $\alpha = a + id$, $\beta = -c - ib$ (with $a, b, c, d$ real), the matrix becomes $\begin{pmatrix} a + id & -c - ib \\ c - ib & a - id\end{pmatrix}$, which expands to $aI + ib\sigma_1 + ic\sigma_2 + id\sigma_3$. The constraint $|\alpha|^2 + |\beta|^2 = 1$ becomes $a^2 + b^2 + c^2 + d^2 = 1$, the equation of the unit sphere $S^3 \subset \mathbb{R}^4$. The map is a smooth bijection with smooth inverse — a diffeomorphism. Since $S^3$ is connected and simply connected, so is $SU(2)$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Setup.** For $u \in SU(2)$ and $\vec x \in \mathbb{R}^3$, the matrix $u(\vec x \cdot \vec\sigma)u^{-1}$ is traceless and Hermitian (Lemma 2), so it equals $\vec y \cdot \vec\sigma$ for a unique $\vec y \in \mathbb{R}^3$. Define $\mathrm{Ad}_u(\vec x) := \vec y$. The map $\mathrm{Ad}_u: \mathbb{R}^3 \to \mathbb{R}^3$ is linear (by linearity of conjugation on matrices). The Pauli basis gives a canonical isomorphism $\mathbb{R}^3 \xrightarrow{\sim} \{\text{traceless Hermitian } 2 \times 2 \text{ matrices}\}$, $\vec x \mapsto \vec x \cdot \vec\sigma$, with inverse $A \mapsto \tfrac{1}{2}\mathrm{tr}(A\vec\sigma)$.
>
> **Step 1 — $\mathrm{Ad}_u \in O(3)$.** Equip $\mathbb{R}^3$ with the standard Euclidean inner product; under the Pauli-basis identification, this becomes $\langle A, B\rangle = \tfrac{1}{2}\mathrm{tr}(AB)$ on traceless Hermitian matrices (since $\tfrac{1}{2}\mathrm{tr}((\vec x \cdot \vec\sigma)(\vec y \cdot \vec\sigma)) = \tfrac{1}{2}x^j y^k \mathrm{tr}(\sigma_j \sigma_k) = x^j y^k \delta_{jk} = \vec x \cdot \vec y$, using $\mathrm{tr}(\sigma_j\sigma_k) = 2\delta_{jk}$). By Lemma 1, $\mathrm{Ad}_u$ preserves this pairing, so $\mathrm{Ad}_u \in O(3)$.
>
> **Step 2 — $\mathrm{Ad}_u \in SO(3)$.** The map $u \mapsto \det\mathrm{Ad}_u$ is continuous from the connected space $SU(2) \cong S^3$ to $\{\pm 1\}$, with $\det\mathrm{Ad}_I = 1$. By connectedness, $\det\mathrm{Ad}_u \equiv 1$.
>
> **Step 3 — $\mathrm{Ad}$ is a Lie group homomorphism.** $\mathrm{Ad}_{uv}(A) = (uv)A(uv)^{-1} = u(vAv^{-1})u^{-1} = \mathrm{Ad}_u(\mathrm{Ad}_v(A))$, so $\mathrm{Ad}_{uv} = \mathrm{Ad}_u \circ \mathrm{Ad}_v$.
>
> **Step 4 — $\mathrm{Ad}$ is a local diffeomorphism at $I$.** By Lemma 3, the differential $d\mathrm{Ad}_I: \mathfrak{su}(2) \to \mathfrak{so}(3)$ is a linear isomorphism between $3$-dimensional spaces. By the inverse function theorem, $\mathrm{Ad}$ is a local diffeomorphism on a neighborhood of $I$.
>
> **Step 5 — $\mathrm{Ad}$ is surjective.** The image of $\mathrm{Ad}$ is a subgroup of $SO(3)$ (since $\mathrm{Ad}$ is a homomorphism). It contains a neighborhood of $I \in SO(3)$ (from Step 4), so it is an *open* subgroup of $SO(3)$. The complement is a union of cosets of this open subgroup, also open. So the image is closed. By connectedness of $SO(3)$, the image is all of $SO(3)$.
>
> **Step 6 — $\ker\mathrm{Ad} = \{\pm I\}$.** By Lemma 4, $u \in \ker\mathrm{Ad}$ iff $u\sigma_j u^{-1} = \sigma_j$ for $j = 1, 2, 3$, which forces $u = \pm I$.
>
> **Step 7 — $\mathrm{Ad}$ is a $2:1$ covering map.** From Steps 4 and 5, $\mathrm{Ad}$ is a smooth surjection that is a local diffeomorphism at every point (by translation, using that $\mathrm{Ad}_{uv} = \mathrm{Ad}_u\mathrm{Ad}_v$ and $\mathrm{Ad}_u$ is invertible). From Step 6, each fiber has exactly $2$ points. So $\mathrm{Ad}$ is a $2:1$ covering map of Lie groups.
>
> **Step 8 — $SU(2) \cong S^3$ is the universal cover of $SO(3)$.** By Lemma 5, $SU(2) \cong S^3$ is simply connected. A simply connected cover of a connected Lie group is automatically the *universal* cover; so $SU(2)$ is the universal cover of $SO(3)$, with $\pi_1(SO(3)) = \ker\mathrm{Ad} = \mathbb{Z}/2$. Topologically, $SO(3) = S^3/\{\pm 1\} = \mathbb{RP}^3$.

---

# Cross-Field Exercise Suggestions

1. **Computer graphics / quaternionic rotation:** Given two orientations of a rigid body in $\mathbb{R}^3$ specified as $3 \times 3$ rotation matrices $R_1, R_2$, compute the *quaternion* corresponding to each via the inverse of the $SU(2) \to SO(3)$ cover, and use SLERP (spherical linear interpolation along $S^3 = SU(2)$) to interpolate between them smoothly. This is the standard tool in animation and robotics; the theorem's $2:1$ nature manifests as the choice of "short way" vs "long way" around the rotation.

2. **Quantum mechanics: precession of spin in a magnetic field.** The Hamiltonian $H = -\gamma \vec B \cdot \vec S = -\gamma\vec B \cdot \tfrac{\hbar}{2}\vec\sigma$ generates time evolution $U(t) = e^{-iHt/\hbar} = e^{i\gamma t(\vec B \cdot \vec\sigma)/2}$, which is exactly an element of $SU(2)$. The corresponding rotation in $SO(3)$ (via the $\mathrm{Ad}$ map) is the precession of the classical angular momentum vector — but the spinor itself "rotates twice as slowly" (or equivalently, the geometric rotation rate is $|\gamma B|$ but the spinor's phase rotation is $|\gamma B|/2$). This is the **Larmor precession** in its quantum/classical correspondence.

3. **Topology: configuration space of two indistinguishable rigid bodies in $\mathbb{R}^3$.** The fundamental group $\pi_1(SO(3)) = \mathbb{Z}/2$ implies that the *configuration space* of two indistinguishable rigid bodies — bodies that can be exchanged — is *not* simply connected. The non-trivial loop corresponds to "rotating each body by $\pi$ then swapping them", which is a closed loop in configuration space but not contractible. This is the topological origin of **anyon statistics** in 2D condensed-matter systems and the **spin-statistics theorem**.

4. **Lie group representation theory: classifying $SO(3)$-modules.** Apply the theorem to deduce that the irreducible representations of $SO(3)$ are exactly the **odd-dimensional** spin-$j$ representations of $SU(2)$ (those with $j \in \mathbb{Z}_{\geq 0}$, of dimension $2j + 1$). The even-dimensional ones (half-integer spin) are intrinsically spinorial. This is the classification underlying the labeling of atomic angular momentum states by integer $\ell$ for orbital and half-integer $s$ for spin.

---

# Bridges

- **[[Thm - Spin(n) is the Double Cover of SO(n)]]** — This theorem is the $n = 3$ case of a general phenomenon: for $n \geq 3$, $\mathrm{Spin}(n) \to SO(n)$ is a $2:1$ covering, and $\mathrm{Spin}(n)$ is the unique simply-connected double cover. The construction is via the Clifford algebra of $\mathbb{R}^n$ in general, and the explicit isomorphism $\mathrm{Spin}(3) = SU(2)$ is the simplest concrete case. The higher-dimensional analogs include $\mathrm{Spin}(4) = SU(2) \times SU(2)$, $\mathrm{Spin}(5) = Sp(2)$, $\mathrm{Spin}(6) = SU(4)$ — accidental low-dimensional isomorphisms that disappear for $n \geq 7$.

- **$\mathrm{SL}(2, \mathbb{C}) \to SO^+(3, 1)$ — the Lorentz analog.** The same construction with traceless *Hermitian* (no trace requirement) matrices identifies Minkowski space $\mathbb{R}^{1,3}$ with $H(2, \mathbb{C})$ (Hermitian $2 \times 2$), and conjugation by $A \in \mathrm{SL}(2, \mathbb{C})$ via $X \mapsto AXA^\dagger$ realizes the cover of the Lorentz group. The proof structure is the same: deformation-retract $\mathrm{SL}(2, \mathbb{C})$ onto $SU(2)$ to establish simply-connectedness; show kernel is $\{\pm I\}$; identify the image with $SO^+(3, 1)$. See [[Def - Dirac Gamma Matrices]] for the consequences for relativistic spinors.

- **[[Def - Quaternions|Quaternionic cover]] of $SO(3)$.** Under the iso $\mathbb{H}^\times_1 \cong SU(2)$, the cover $SU(2) \to SO(3)$ becomes $\mathbb{H}^\times_1 \to SO(3)$ via $q \mapsto (\vec v \mapsto q\vec v q^{-1})$ on $\mathrm{Im}(\mathbb{H}) \cong \mathbb{R}^3$. This is the Hamiltonian formulation, predating the matrix formulation by 80 years; it is the basis for quaternion-based rotation computation in software.

- **Hopf fibration $S^3 \to S^2$.** The action of $U(1) \subset SU(2)$ on $\mathbb{C}^2$ has orbits the complex lines; restricting to $S^3 \subset \mathbb{C}^2$ gives the Hopf fibration with fibre $S^1$. The Hopf bundle is a $U(1)$-principal bundle over $S^2$ with first Chern class $\pm 1$ — the simplest nontrivial $U(1)$-bundle, and physically the **magnetic monopole** (Dirac monopole). The connection to $SU(2) \to SO(3)$: under the cover, the Hopf $U(1) \subset SU(2)$ maps to the rotation subgroup fixing a chosen axis in $\mathbb{R}^3$.

- **$\pi_1(SO(n)) = \mathbb{Z}/2$ for all $n \geq 3$.** The fundamental group of $SO(3)$ generalizes: for all $n \geq 3$, $\pi_1(SO(n)) = \mathbb{Z}/2$, with the spin cover $\mathrm{Spin}(n) \to SO(n)$ providing a topological resolution. This is the topological underpinning of the existence of spinors in all dimensions $\geq 3$.

---

# Unlocked by This

> [!tip] Spin-Statistics Theorem
> The **spin-statistics theorem** of QFT (Pauli, 1940) asserts that particles transforming under the spinor representations of $\mathrm{Spin}(3, 1)$ — i.e., half-integer spin — must obey *Fermi–Dirac* statistics (their wave functions are antisymmetric under exchange), while integer-spin particles (vector and tensor representations of $SO(3, 1)$ proper) obey *Bose–Einstein* statistics. The proof relies on the structure of the $\mathrm{SL}(2, \mathbb{C}) \to SO^+(3, 1)$ cover, generalising this theorem from the rotation case to the full Lorentz case. The phenomenon is purely topological: the $\pi_1(SO(3)) = \mathbb{Z}/2$ effect (the "$2\pi$ rotation gives $-1$ on spinors") combines with the Bargmann–Wightman analysis of representations to force the symmetry of multi-particle wave functions.

> [!tip] Quaternionic Cayley–Klein Parameters in Classical Mechanics
> The classical motion of a rigid body around its center of mass is described by the orientation as a function of time, $R(t) \in SO(3)$. Tracking this trajectory via Euler angles encounters **gimbal lock** singularities; tracking via the **Cayley–Klein parameters** — the components $(a, b, c, d)$ of the lifted $SU(2)$ trajectory — avoids these singularities entirely. The reason: the cover $SU(2) \to SO(3)$ provides a global parameterization of orientations modulo the $\mathbb{Z}/2$ ambiguity, and the $SU(2)$ trajectory is smooth even when the $SO(3)$ trajectory's Euler-angle representation breaks down. This is widely used in spacecraft attitude control and high-precision robotics.

> [!tip] Pauli Exclusion Principle as a Topological Consequence
> Combining the spin-statistics theorem with the $SU(2) \to SO(3)$ cover gives the **Pauli exclusion principle**: two identical fermions (spin-$\tfrac{1}{2}$ particles) cannot occupy the same quantum state. The chain of forcings: (i) the spinor representation $\mathbb{C}^2$ exists because $SU(2)$ covers $SO(3)$; (ii) under a $2\pi$ rotation $-I \in SU(2)$, the spinor changes sign; (iii) by the spin-statistics theorem, fermion wave functions are antisymmetric; (iv) antisymmetry of $\psi(x_1, x_2) = -\psi(x_2, x_1)$ implies $\psi(x, x) = 0$ — exclusion. Without the $2:1$ cover, fermions could not exist, and atoms would not have their familiar shell structure; chemistry, biology, and the existence of matter as we know it depend on this topological fact.

> [!tip] Berry Phase and the Geometric Phase of Quantum States
> The **Berry phase** is the geometric phase acquired by a quantum state under adiabatic transport around a closed loop in parameter space. For a spin-$\tfrac{1}{2}$ system, transporting through $2\pi$ in the parameter space of rotation angles produces a Berry phase of $-1$ — the same sign acquired by a spinor under a $2\pi$ rotation. This is a *gauge-invariant* observable in quantum mechanics, measured experimentally in molecular physics (Mead, 1992) and in the quantum Hall effect. The $SU(2) \to SO(3)$ cover provides the geometric framework for understanding Berry phases on the **Bloch sphere**.

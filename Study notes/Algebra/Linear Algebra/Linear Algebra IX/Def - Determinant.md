---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Alternating Multilinear Form"
  - "Def - Linear Map"
  - "Def - Matrix of a Linear Map"
  - "Def - Basis"
  - "Def - Dimension"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $\mathbb{F}$ with $n = \dim V \geq 1$. An operator on $V$ is a [[Def - Linear Map|linear map]] $T \in \mathcal{L}(V)$, and the space of alternating $n$-linear forms is $V^{(n)}_{\mathrm{alt}}$ — recall (from [[Def - Alternating Multilinear Form]]) that this space is one-dimensional. For an operator $T$ and an alternating $n$-linear form $\alpha$, define $\alpha_T \in V^{(n)}_{\mathrm{alt}}$ by

$$\alpha_T(v_1, \dots, v_n) := \alpha(T v_1, \dots, T v_n).$$

The set of permutations of $\{1, \dots, n\}$ is $\operatorname{perm}(n)$, and $\operatorname{sign}(\sigma) \in \{\pm 1\}$ is the sign of $\sigma$.

---

# Axiom Motivation

The conceptual ordering at the heart of LADR Chapter 9 is that **the determinant is defined by the action of an operator on alternating multilinear forms, and the Leibniz formula is a derived consequence**, not the other way around. This is worth dwelling on, because it inverts the standard textbook ordering and is the chapter's central pedagogical point.

The standard "first course" approach: define $\det A$ as the Leibniz sum $\sum_\sigma \operatorname{sign}(\sigma) A_{\sigma(1), 1} \cdots A_{\sigma(n), n}$, then prove its key properties (multilinearity in columns, alternation, value 1 on the identity, multiplicativity $\det(AB) = \det A \cdot \det B$). The problem with this approach is that it makes the multiplicativity $\det(AB) = \det(A) \cdot \det(B)$ a *miracle* — a non-obvious identity that has to be checked by index-pushing through $n!$-term sums. Worse, the *meaning* of the determinant — as a volume scaling factor, as a multiplicative homomorphism, as the unique alternating $n$-linear quantity — is hidden in this derivation.

The LADR approach: take the alternating-multilinear-uniqueness as foundational, define $\det$ as the scalar by which an operator acts on the one-dimensional space $V^{(n)}_{\mathrm{alt}}$, and derive everything else. The multiplicativity is then a one-line consequence: $\alpha_{ST} = (\det S) \cdot \alpha_T = (\det S)(\det T) \alpha$, so $\det(ST) = (\det S)(\det T)$. The Leibniz formula falls out by expanding $\alpha(T v_1, \dots, T v_n)$ for the standard alternating form. The conceptual content — that $\det$ is *the* alternating $n$-multilinear gadget assigned to an operator — is upfront.

**Why this is the right definition.** The defining identity $\alpha_T = (\det T) \cdot \alpha$ has several immediate consequences that the Leibniz definition has to work for.

First, *well-definedness*: the map $\alpha \mapsto \alpha_T$ from $V^{(n)}_{\mathrm{alt}}$ to itself is linear (because $T$ is linear and the assignment is linear in $\alpha$), and $V^{(n)}_{\mathrm{alt}}$ is one-dimensional (by [[Def - Alternating Multilinear Form|the alternating-uniqueness theorem]]), so every linear endomorphism of $V^{(n)}_{\mathrm{alt}}$ is multiplication by a unique scalar. That scalar is what we call $\det T$.

Second, *basis-independence*: the definition involves no choice of basis. It is intrinsic to the operator $T$. This makes it manifestly a similarity invariant: $\det(S^{-1} T S) = \det T$ comes for free, because changing basis just replaces $\alpha$ by another nonzero alternating form, leaving the scalar action the same.

Third, *multiplicativity*: from $\alpha_{ST}(v_1, \dots, v_n) = \alpha(ST v_1, \dots, ST v_n)$, replacing $T v_k$ by single vectors gives $\alpha_{ST} = (\alpha_T)_S = (\det S) \alpha_T = (\det S)(\det T)\alpha$. One line. Hence $\det(ST) = (\det S)(\det T)$.

**The Leibniz formula as a corollary.** Once the definition is in place, we want a formula. Expand: take the alternating form $\alpha$ with $\alpha(e_1, \dots, e_n) = 1$ on a basis. By definition, $\det T = \alpha(Te_1, \dots, Te_n)$ (apply $\alpha_T$ to $(e_1, \dots, e_n)$). Now $Te_k = \sum_j A_{jk} e_j$ where $A$ is the matrix of $T$ in $(e_j)$, and substituting plus the permutation-sum formula for alternating $n$-linear forms gives

$$\det T = \alpha(Te_1, \dots, Te_n) = \sum_{\sigma \in \operatorname{perm}(n)} \operatorname{sign}(\sigma)\, A_{\sigma(1), 1} \cdots A_{\sigma(n), n}.$$

The Leibniz formula is what *comes out* — it is the explicit computational form of the abstract definition. The Leibniz formula is essential for hand computation in small dimensions, but it is *useless* for $n \geq 5$ (the sum has 120 terms) and gives no conceptual content for proofs. Always start from the abstract definition; use Leibniz only when you need a specific number.

**Geometric content.** The determinant is the **factor by which the operator scales $n$-dimensional volume**. Concretely: if $P$ is the parallelepiped spanned by $(v_1, \dots, v_n)$, with signed volume $\alpha(v_1, \dots, v_n)$ for some chosen alternating $n$-linear form $\alpha$ (a "volume measurement"), then the signed volume of $T(P)$ is $\alpha(Tv_1, \dots, Tv_n) = (\det T) \alpha(v_1, \dots, v_n)$. So $\det T$ is the volume-scaling factor, with sign recording orientation: positive determinant means orientation-preserving, negative means orientation-reversing. This is why $|\det J|$ appears in the change-of-variables formula and why the Jacobian determinant is the local volume-distortion factor in multivariate calculus.

---

# The Definition

**Determinant of an operator (LADR 9.41).** Let $V$ be a finite-dimensional vector space and let $T \in \mathcal{L}(V)$ be an operator. The **determinant** of $T$, denoted $\det T$, is the unique scalar in $\mathbb{F}$ such that

$$\alpha_T = (\det T) \cdot \alpha \qquad \text{for every alternating } n\text{-linear form } \alpha \in V^{(n)}_{\mathrm{alt}},$$

where $\alpha_T(v_1, \dots, v_n) := \alpha(T v_1, \dots, T v_n)$ and $n = \dim V$.

**Why this is well-defined.** The map $\alpha \mapsto \alpha_T$ is a linear endomorphism of $V^{(n)}_{\mathrm{alt}}$ (it is linear in $\alpha$, and the alternating property is preserved because $\alpha_T(v_1, \dots, v_n)$ with $v_j = v_k$ has $Tv_j = Tv_k$ so $\alpha$ vanishes there). Since $\dim V^{(n)}_{\mathrm{alt}} = 1$ (the [[Def - Alternating Multilinear Form|alternating-uniqueness theorem]]), every linear endomorphism of a one-dimensional space is multiplication by a unique scalar.

**Determinant of a matrix (LADR 9.43).** Let $A$ be an $n \times n$ matrix with entries in $\mathbb{F}$. Let $T \in \mathcal{L}(\mathbb{F}^n)$ be the operator whose matrix in the standard basis is $A$. The **determinant** of $A$, denoted $\det A$, is defined by

$$\det A := \det T.$$

**Equivalent characterisations.**

1. **Leibniz formula (LADR 9.46).**
$$\det A = \sum_{\sigma \in \operatorname{perm}(n)} \operatorname{sign}(\sigma)\, A_{\sigma(1), 1} \cdot A_{\sigma(2), 2} \cdots A_{\sigma(n), n}.$$

2. **Multilinear-alternating-normalised characterisation.** The map $\mathbb{F}^n \times \cdots \times \mathbb{F}^n \to \mathbb{F}$, $(v_1, \dots, v_n) \mapsto \det(v_1\ v_2\ \cdots\ v_n)$ (taking $n$ columns to the determinant of the matrix they form), is the unique alternating $n$-linear form on $\mathbb{F}^n$ taking value 1 on the standard basis $(e_1, \dots, e_n)$.

3. **Product of eigenvalues (over algebraically closed fields, with multiplicity).** For $T$ on a complex vector space, $\det T = \lambda_1 \cdots \lambda_n$ where the $\lambda_i$ are eigenvalues counted with algebraic multiplicity. See [[Thm - Determinant Equals Product of Eigenvalues with Multiplicity]].

4. **Volume scaling (over $\mathbb{R}$ or $\mathbb{C}$ with the Euclidean structure).** $|\det T|$ is the factor by which $T$ scales $n$-dimensional volume, and $\operatorname{sign}(\det T)$ records whether $T$ preserves or reverses orientation.

5. **Basis-evaluation formula.** For any basis $(e_1, \dots, e_n)$ of $V$, $\det T = \alpha(T e_1, \dots, T e_n) / \alpha(e_1, \dots, e_n)$ for any nonzero $\alpha \in V^{(n)}_{\mathrm{alt}}$.

**Worked formula for small $n$.**

- $n = 1$: $\det A = A_{11}$.
- $n = 2$: $\det A = A_{11} A_{22} - A_{12} A_{21}$.
- $n = 3$: $\det A = A_{11} A_{22} A_{33} - A_{11} A_{23} A_{32} + A_{12} A_{23} A_{31} - A_{12} A_{21} A_{33} + A_{13} A_{21} A_{32} - A_{13} A_{22} A_{31}$ (six terms).
- $n = 4$: 24 terms.
- $n \geq 5$: $n!$ terms; computation by Leibniz is infeasible. Use Gaussian elimination, cofactor expansion, or eigenvalue methods.

---

# Categorical / Structural Definition

The determinant has a clean categorical formulation that unifies several perspectives.

**The determinant is the action on the top exterior power $\Lambda^n V$.** Recall (from [[Def - Alternating Multilinear Form]]) the natural isomorphism $V^{(n)}_{\mathrm{alt}} \cong (\Lambda^n V)^*$. The dual space of a one-dimensional space is one-dimensional, so $\Lambda^n V$ is one-dimensional. Any operator $T : V \to V$ induces an operator $\Lambda^n T : \Lambda^n V \to \Lambda^n V$ by

$$\Lambda^n T(v_1 \wedge \cdots \wedge v_n) := T v_1 \wedge \cdots \wedge T v_n.$$

Since $\Lambda^n V$ is one-dimensional, $\Lambda^n T$ is multiplication by a scalar — and **that scalar is $\det T$**:

$$\Lambda^n T = (\det T) \cdot \operatorname{id}_{\Lambda^n V}.$$

This is the categorical-functorial definition: $\det$ is the eigenvalue of the induced map on the top exterior power. The whole package — multilinearity, alternation, multiplicativity, similarity invariance — is built into this categorical picture: the functor $\Lambda^n$ takes operators to operators, and on a one-dimensional space "operator" is "scalar", giving $\det$ as the functorial output.

**Multiplicativity as functoriality.** $\Lambda^n(ST) = \Lambda^n S \circ \Lambda^n T$ (functoriality of $\Lambda^n$), which translates to $\det(ST) = \det S \cdot \det T$ on the one-dimensional output space.

**Determinant as a Lie group homomorphism.** The determinant is the group homomorphism

$$\det : \mathrm{GL}(V) \;\longrightarrow\; \mathbb{F}^\times = \mathrm{GL}_1(\mathbb{F}),$$

whose kernel is the special linear group $\mathrm{SL}(V)$. As Lie groups (over $\mathbb{R}$ or $\mathbb{C}$), the determinant is a smooth surjective homomorphism, and its derivative at the identity is the **trace**: $d(\det)_I(X) = \operatorname{tr}(X)$. This gives the formula $\det(I + \epsilon X) = 1 + \epsilon \operatorname{tr} X + O(\epsilon^2)$, and shows $\mathfrak{sl}(V) = \ker(\operatorname{tr})$ as the Lie algebra of $\mathrm{SL}(V)$.

---

# Relate to Other Fields / Compression

The determinant is the **volume scaling factor of a linear transformation**, with sign for orientation. This is its true name and its most useful operational interpretation. From this comes:

- **Multivariate change of variables.** For a $C^1$ diffeomorphism $\Phi$, $\int f\, dx = \int f \circ \Phi \cdot |\det D\Phi|\, dy$. The Jacobian determinant is the local volume-scaling factor.

- **Multiplicative homomorphism.** $\det : \mathrm{GL}(V) \to \mathbb{F}^\times$ is a group homomorphism — composing transformations multiplies their volume scalings, which is what multiplicativity says.

- **Determinant of similar operators is equal.** $\det(S^{-1} T S) = \det T$, because similar operators are the *same* operator viewed in different bases, and the volume-scaling factor is intrinsic.

- **Invertibility test.** $T$ is invertible iff $\det T \neq 0$. The reason: $T$ is invertible iff it sends a basis to a basis iff it sends a nonzero alternating $n$-form to a nonzero one iff its scaling factor is nonzero.

- **Eigenvalue product.** $\det T = \prod \lambda_i$ with multiplicity (over $\mathbb{C}$). The reason: in a basis where $T$ is upper-triangular (Schur theorem), the Leibniz formula collapses to the diagonal product.

**True name:** $\det T$ is the unique scalar by which $T$ scales every alternating $n$-multilinear measurement of $n$-dimensional volume.

---

# Examples / Corollaries

**Is an instance: $\det I = 1$.** The identity operator sends every basis to itself, so the alternating form is unchanged. Equivalently, $\Lambda^n I = \operatorname{id}_{\Lambda^n V}$, multiplication by 1.

**Is an instance: $\det(\lambda I) = \lambda^n$.** Multiplication by $\lambda$ sends $(v_1, \dots, v_n)$ to $(\lambda v_1, \dots, \lambda v_n)$, and multilinearity factors out $\lambda$ from each slot, giving $\lambda^n$.

**Is an instance: $\det T = \lambda_1 \cdots \lambda_n$ for a diagonal operator.** A diagonal matrix with $\lambda_i$ on the diagonal has only the identity permutation contributing in Leibniz: $\det = \lambda_1 \cdots \lambda_n$. This is the simplest non-trivial determinant computation.

**Is an instance: $\det T = \lambda_1 \cdots \lambda_n$ for an upper-triangular operator.** Same as diagonal — only the identity permutation contributes to Leibniz, because any other permutation forces some $A_{\sigma(k), k}$ with $\sigma(k) > k$, which is below-diagonal and hence zero. See [[Ex - Determinant of an upper-triangular matrix is the product of diagonal entries]].

**Is an instance: $\det J = 1$ for the symplectic matrix $J = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix}$.** A direct computation (or the eigenvalue product, since eigenvalues are $\pm i$ in pairs, giving $\prod = (i \cdot (-i))^n = 1^n = 1$).

**Is an instance: a real rotation has $\det = 1$.** Rotations preserve volume *and* orientation, so $\det = +1$. A reflection has $\det = -1$ (preserves volume, reverses orientation).

**Is NOT an instance: the determinant is *not* additive.** $\det(A + B) \neq \det A + \det B$ in general. Counterexample: $\det(I + I) = \det(2I) = 2^n$, while $\det I + \det I = 2$. The determinant is multilinear in *rows* (or columns) separately, not in the matrix as a whole.

**Corollary (sign and orientation).** Over $\mathbb{R}$, $\det T > 0$ iff $T$ preserves orientation, $\det T < 0$ iff $T$ reverses orientation. The orientation of a real vector space is an equivalence class of ordered bases under positive-determinant change of basis.

**Corollary (transpose has the same determinant).** $\det A^t = \det A$. By the Leibniz formula: $\det A^t = \sum_\sigma \operatorname{sign}(\sigma) A^t_{\sigma(1), 1} \cdots = \sum_\sigma \operatorname{sign}(\sigma) A_{1, \sigma(1)} \cdots A_{n, \sigma(n)}$, and reindexing $\tau = \sigma^{-1}$ (with $\operatorname{sign}(\tau) = \operatorname{sign}(\sigma)$) recovers the original sum. Consequence: row operations and column operations affect the determinant identically, so cofactor expansion works along rows or columns.

**Corollary (invertibility and zero determinant).** $T$ is invertible iff $\det T \neq 0$, in which case $\det T^{-1} = 1/\det T$.

**Corollary (block-triangular).** $\det \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \det A \cdot \det D$ for square blocks $A, D$. See [[Ex - Determinant of a block matrix]].

**Calibration check.** If you have understood the definition, you should be able to: (i) compute $\det\begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix} = 2 \cdot 4 - 1 \cdot 3 = 5$ from the $n = 2$ Leibniz formula; (ii) verify $\det(2I_3) = 8$ from the scaling-by-$\lambda$ formula; (iii) verify that the rotation matrix $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$ has determinant $\cos^2\theta + \sin^2\theta = 1$, consistent with rotation preserving volume and orientation; (iv) verify that the reflection matrix $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ has determinant $-1$, consistent with reflection preserving volume but reversing orientation.

---

# Unlocked by This

> [!tip] Special Linear Group SL(n) *(from Lie Theory)*
> The kernel $\mathrm{SL}(V) := \{T \in \mathrm{GL}(V) : \det T = 1\}$ is a normal subgroup of $\mathrm{GL}(V)$ — the volume-preserving (and orientation-preserving, over $\mathbb{R}$) linear transformations. Its Lie algebra $\mathfrak{sl}(V) = \{X : \operatorname{tr} X = 0\}$ is the trace-zero operators. This is one of the most studied non-compact Lie groups, central to algebraic geometry, number theory, and physics.

> [!tip] Change of Variables Formula *(from Multivariate Analysis)*
> $\int_U f \, dx = \int_{\Phi^{-1}(U)} (f \circ \Phi) \cdot |\det D\Phi|\, dy$ for a $C^1$ diffeomorphism $\Phi$. The Jacobian determinant $|\det D\Phi|$ is the infinitesimal volume-scaling factor at each point. See [[Def - Partial Derivatives and the Jacobian Matrix|the Jacobian]] and [[Def - The Total Derivative and Differentiability|the total derivative]].

> [!tip] Volume Form *(from Differential Geometry)*
> On an oriented Riemannian manifold $(M, g)$, the volume form $\omega_g = \sqrt{\det g_{ij}}\, dx^1 \wedge \cdots \wedge dx^n$ is the unique alternating top form giving unit volume to positively oriented orthonormal frames. The factor $\sqrt{\det g_{ij}}$ is the determinant of the metric tensor, converting flat $n$-volume into curved $n$-volume.

> [!tip] Liouville's Theorem in Hamiltonian Mechanics *(from Physics)*
> The Hamiltonian flow on phase space preserves the symplectic volume — equivalently, the Jacobian of the time-evolution map has determinant 1. This is what makes phase-space volume a meaningful invariant and is the foundation of statistical mechanics.

> [!tip] Reidemeister Torsion *(from Algebraic Topology)*
> A topological invariant defined via an alternating product of determinants on a chain complex. It distinguishes lens spaces with the same homotopy type — for instance $L(7, 1)$ and $L(7, 2)$ have identical fundamental groups, homology, and even cellular structure, but different Reidemeister torsions. The full theory bridges algebra (determinants), geometry (CW complexes), and topology (homotopy classification).

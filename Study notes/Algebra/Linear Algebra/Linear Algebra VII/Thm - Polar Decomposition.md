---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Isometry"
  - "Def - Unitary Operator"
  - "Def - Positive Operator"
  - "Thm - Positive Operators Have a Unique Square Root"
  - "Thm - Singular Value Decomposition"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. The [[Def - Adjoint of a Linear Map|adjoint]] of $T \in \mathcal{L}(V)$ is $T^*$; the **absolute value** of $T$ is $|T| = \sqrt{T^* T}$, the unique [[Def - Positive Operator|positive]] square root of $T^* T$ (existence by [[Thm - Positive Operators Have a Unique Square Root]]). See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Polar Decomposition).** Let $T \in \mathcal{L}(V)$ be any operator on a finite-dimensional inner product space. Then $T$ factors as
> $$T = S R,$$
> where:
> - $R = |T| = \sqrt{T^* T}$ is positive,
> - $S$ is an [[Def - Isometry|isometry]] on $\operatorname{range} R$ (extended to a [[Def - Unitary Operator|unitary]] on $V$).
>
> Furthermore:
> 1. The positive factor $R$ is uniquely determined: $R = \sqrt{T^*T}$.
> 2. When $T$ is invertible, $S$ is uniquely determined and is unitary: $S = T R^{-1}$.
> 3. When $T$ is not invertible, $S$ is determined on $\operatorname{range} R = (\operatorname{null} T)^\perp$ but can be chosen freely on its orthogonal complement.
>
> **In SVD terms.** If $T = U \Sigma V^*$ is the singular value decomposition, then $S = UV^*$ and $R = V \Sigma V^*$.

> [!warning] Both "left" and "right" polar decompositions exist.
> One can also write $T = R' S$ with $R' = \sqrt{TT^*}$ positive and $S$ an isometry — the **left polar decomposition** (with the positive factor on the left). The two decompositions agree when $T$ is normal: $R = R'$ and the isometric factors coincide. We use the right polar decomposition $T = SR$ as the standard form.

---

# Motivation

The polar decomposition is the **operator analogue of $z = e^{i\theta} \cdot r$ for complex numbers**: every operator factors uniquely (up to gauge in the singular case) as an isometric "phase" times a positive "magnitude". The positive operator $|T| = \sqrt{T^*T}$ is the operator-theoretic absolute value; the isometry $S$ is the operator-theoretic phase.

This factorisation gives a **canonical decomposition of every operator** into pieces with distinct geometric meanings:
- The positive factor $R = |T|$ encodes the **stretching information**: its eigenvalues are the singular values of $T$, the principal stretching factors.
- The isometric factor $S$ encodes the **rotation/orientation information**: it preserves lengths but rearranges directions.

Together, $T = SR$ says: "stretch first (by $R$), then rotate (by $S$)" — the stretching is along the right-singular axes (eigenvectors of $T^*T$); the rotation aligns the resulting stretched ellipsoid with the left-singular axes (eigenvectors of $TT^*$).

The polar decomposition exists for every operator, with the only subtlety being uniqueness of $S$. When $T$ is invertible, both factors are uniquely determined; when $T$ is not invertible, $|T|$ is still unique (it is always determined as $\sqrt{T^*T}$) but $S$ has gauge freedom on $\operatorname{null} T$. The analogy: when $z = 0$, the angle of $z$ is undefined; when $T$ has a non-trivial kernel, the isometric factor is undefined on that kernel.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is universally satisfied: every operator on a finite-dimensional inner product space has a polar decomposition. The challenge is recognising when polar decomposition is the right route.

The first disguised source is **an operator presented with both rotational and scaling content**. Linear deformation in continuum mechanics is the prototype: a body's deformation tensor $F$ has polar decomposition $F = RU$ with $R$ rotation and $U$ symmetric stretch tensor. The eigenvalues of $U$ are the **principal stretches**, the eigenvalues of $F$ alone do not give this information.

The second disguised source is **a problem about distance to the unitary group**. The unitary matrix closest to a given $T$ (in Frobenius norm) is the isometric factor $S$ of the polar decomposition. *Example problem:* find the closest rotation matrix to a noisy estimate of a rotation; the answer is $UV^*$ from the SVD of the estimate.

The third disguised source is **iteration toward a singular value decomposition**. The polar decomposition $T = SR$ can be iteratively refined toward an SVD by alternating polar steps; the algorithm converges quadratically and is the basis of one class of SVD algorithms in numerical linear algebra.

**Targets (Output Amplification)**

The conclusion is the factorisation $T = SR$ with $R$ positive and $S$ isometric.

Combine with **the SVD**: $T = U \Sigma V^* = (UV^*)(V \Sigma V^*)$ — polar decomposition derived from SVD. The further result $E$: an explicit recipe for computing polar decomposition from any algorithm that computes SVD.

Combine with **matrix exponential**: for skew-Hermitian $X$ (i.e., $X^* = -X$), $e^X$ is unitary; for self-adjoint $Y$, $e^Y$ is positive definite. Combining, $T = e^X e^Y$ is a polar decomposition of $T = e^{X + Y \cdot O(\|X, Y\|)}$ for small operators — the linearised polar decomposition. The further result $E$: in the tangent space at the identity, the polar decomposition is the direct sum decomposition $\mathcal{L}(V) = \mathfrak{u}(V) \oplus \mathfrak{p}(V)$ of all operators into skew-adjoint plus self-adjoint, $T = \frac{T - T^*}{2} + \frac{T + T^*}{2}$.

Combine with **manifold structure of $\operatorname{GL}(V)$**: the polar decomposition gives a **diffeomorphism** $\operatorname{GL}(V) \cong U(V) \times P(V)$, where $P(V)$ is the open cone of positive definite operators. The further result $E$: $\operatorname{GL}(V)$ retracts onto its maximal compact subgroup $U(V)$, with retraction $T \mapsto S = T |T|^{-1}$. This is the basis of homotopy-theoretic statements like "$\operatorname{GL}_n(\mathbb{C})$ deformation retracts to $U(n)$".

---

# Why Is It True

The proof is one calculation, once the SVD is in hand.

**The one-liner mechanism: the SVD $T = U\Sigma V^*$ regroups uniquely as $T = (UV^*)(V \Sigma V^*) = S \cdot |T|$, with $S = UV^*$ unitary by composition of unitaries and $R = V \Sigma V^* = (V \Sigma^{1/2} V^*)^2$ positive.**

Why is $R = V \Sigma V^*$ equal to $|T| = \sqrt{T^*T}$? Compute $T^* T = (U\Sigma V^*)^* (U\Sigma V^*) = V \Sigma^* U^* U \Sigma V^* = V \Sigma^* \Sigma V^* = V \Sigma^2 V^*$ (since $\Sigma$ has real non-negative entries, $\Sigma^* = \Sigma^t = \Sigma$). So $T^* T = V \Sigma^2 V^*$, which is positive with eigenvalues $s_j^2$. Its unique positive square root, by [[Thm - Positive Operators Have a Unique Square Root]], is $V \Sigma V^* = R$. So indeed $R = |T|$.

Why is $S = UV^*$ unitary? Both $U$ and $V$ are unitary by the SVD, so $S^* S = (UV^*)^* (UV^*) = VU^* U V^* = V V^* = I$ and similarly $SS^* = I$. So $S$ is unitary.

Verification: $SR = (UV^*)(V\Sigma V^*) = U(V^*V)\Sigma V^* = U\Sigma V^* = T$. ✓

**Uniqueness of $R$:** since $R = |T| = \sqrt{T^*T}$ depends only on $T^*T$, which is determined by $T$, and the square root is unique, $R$ is unique.

**Uniqueness of $S$ when $T$ is invertible:** if $T = SR$ with $R$ invertible, $S = TR^{-1}$ is uniquely determined.

**Non-uniqueness of $S$ when $T$ is not invertible:** $R = |T|$ has the same null space as $T$ (since $\|R v\|^2 = \langle R^2 v, v \rangle = \langle T^* T v, v \rangle = \|Tv\|^2$). On $\operatorname{null} T = \operatorname{null} R$, the equation $SRv = Tv = 0$ gives $S \cdot 0 = 0$, no constraint on $S$. So $S$ is determined on $\operatorname{range} R = (\operatorname{null} R)^\perp$ but free on $\operatorname{null} R$.

---

# What Makes This Hard

The non-obvious step is recognising that **the positive factor $|T| = \sqrt{T^*T}$, not $T$ itself, encodes the stretching information**. For self-adjoint $T$, $|T|$ is essentially $T$ (with absolute values of eigenvalues); for general $T$, $|T|$ is a derived object — the spectral data lives in $T^*T$, not $T$.

The second subtlety is that the **isometric factor's domain matters**: $S$ is an isometry on $\operatorname{range} R$, which is a subspace of $V$. To extend to a full unitary, one chooses arbitrary orthonormal extension on the orthogonal complement. For invertible $T$, the orthogonal complement is trivial and $S$ is already a full unitary; for non-invertible $T$, the choice exists and the polar decomposition is non-unique on this part.

The third subtlety is the **left vs right polar decomposition**. $T = SR$ with $R = \sqrt{T^*T}$ (right polar) and $T = R'S$ with $R' = \sqrt{TT^*}$ (left polar) are both decompositions but use different positive operators. For normal $T$ they coincide; for general $T$ they are related by $R' = SRS^{-1}$ — conjugation by the isometric factor.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Construct $R = \sqrt{T^*T}$ via the spectral theorem and uniqueness of positive square roots. Define $S$ on $\operatorname{range} R$ by $S(Rv) = Tv$ — well-defined and isometric because $\|Rv\|^2 = \langle T^*T v, v \rangle = \|Tv\|^2$.

**Subgoal decomposition:**

1. **Construct $R$.** Apply the spectral theorem to $T^*T$ to get $R = \sqrt{T^*T}$ — the unique positive square root.

2. **Show $\|R v\| = \|Tv\|$ for all $v$.** Use $\|R v\|^2 = \langle R^2 v, v \rangle = \langle T^*T v, v \rangle = \|Tv\|^2$.

3. **Define $S$ on $\operatorname{range} R$ by $S(Rv) = Tv$.** Check it is well-defined: $Rv = Rv'$ implies $Tv = Tv'$, because $R$ and $T$ have the same kernel.

4. **Show $S$ is isometric on $\operatorname{range} R$.** By construction.

5. **Extend $S$ to all of $V$.** Choose any orthonormal extension to a unitary; the choice is free.

6. **Verify $T = SR$.** Direct: $SR \cdot v = S(Rv) = Tv$.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\|Rv\| = \|Tv\|$ for $R = \sqrt{T^*T}$
> **Statement:** Let $R = \sqrt{T^*T}$. Then $\|Rv\| = \|Tv\|$ for all $v \in V$.
>
> **Hint:** Compute $\|Rv\|^2$ as $\langle R^2 v, v \rangle$ and $\|Tv\|^2$ as $\langle T^*T v, v \rangle$.
>
> **Why needed:** This is what makes $S$ — defined by $S(Rv) = Tv$ — an isometry.
>
> > [!note]- Full proof
> > $\|Rv\|^2 = \langle Rv, Rv \rangle = \langle R^* R v, v \rangle = \langle R^2 v, v \rangle$ (using $R^* = R$ since $R$ is self-adjoint). And $R^2 = T^*T$ by definition, so $\langle R^2 v, v \rangle = \langle T^*T v, v \rangle = \langle Tv, Tv \rangle = \|Tv\|^2$.

> [!note]- Lemma 2: $R$ and $T$ have the same kernel
> **Statement:** $\operatorname{null} R = \operatorname{null} T$.
>
> **Hint:** $v \in \operatorname{null} R$ iff $\|Rv\| = 0$ iff $\|Tv\| = 0$ (Lemma 1) iff $v \in \operatorname{null} T$.
>
> **Why needed:** Makes the definition $S(Rv) = Tv$ well-defined.
>
> > [!note]- Full proof
> > By Lemma 1, $\|Rv\| = 0$ iff $\|Tv\| = 0$, i.e., $Rv = 0$ iff $Tv = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> **Step 0 — well-posedness.** By [[Thm - Positive Operators Have a Unique Square Root]] applied to the positive operator $T^*T$ (positivity by [[Def - Positive Operator]]), the operator $R = \sqrt{T^*T}$ exists and is the unique positive operator with $R^2 = T^*T$. So $R = |T|$ is well-defined.
>
> **Defining $S$.** Define $S$ on $\operatorname{range} R$ by $S(Rv) = Tv$. To check well-definedness: if $Rv = Rv'$ then $R(v - v') = 0$, so $v - v' \in \operatorname{null} R = \operatorname{null} T$ (Lemma 2), so $T(v - v') = 0$, so $Tv = Tv'$. Hence $S$ is well-defined on $\operatorname{range} R$ as a function.
>
> **Linearity of $S$ on $\operatorname{range} R$.** Direct: $S(\alpha R v + \beta R v') = S(R(\alpha v + \beta v')) = T(\alpha v + \beta v') = \alpha Tv + \beta Tv' = \alpha S(Rv) + \beta S(Rv')$.
>
> **Isometry of $S$ on $\operatorname{range} R$.** For $w = Rv \in \operatorname{range} R$: $\|S w\| = \|S(Rv)\| = \|Tv\| = \|Rv\| = \|w\|$ (Lemma 1).
>
> **Extension to all of $V$.** $\operatorname{range} R = (\operatorname{null} R)^\perp$ by the [[Thm - Properties of the Adjoint|null-range duality]] (with $R = R^*$, so $\operatorname{range} R = (\operatorname{null} R)^\perp$). Extend $S$ to a unitary on $V$ by choosing any orthonormal map $\operatorname{null} R \to (\operatorname{range} R)^\perp = \operatorname{null} R$ — this can be done because $\dim \operatorname{null} R = \dim (\operatorname{range} R)^\perp$ (since $R$ is self-adjoint and finite-dimensional). Any unitary extension works; the choice is the "gauge freedom" in the non-invertible case.
>
> **Verification of $T = SR$.** For any $v$, $SR \cdot v = S(Rv) = Tv$ by definition of $S$. So $T = SR$.
>
> **Uniqueness of $R$.** $R = \sqrt{T^*T}$ is determined by $T$ via the uniqueness of the positive square root. If $T = S'R'$ with $R'$ positive and $S'$ isometric, then $T^*T = R'^* S'^* S' R' = R'^* R' = (R')^2$ (using $S'^*S' = I$ on $\operatorname{range} R'$, but we need it on all of $V$, which requires careful handling for non-invertible $T$ — the standard argument extends $S'$ unitarily to all of $V$, recovering $T^*T = (R')^2$). So $R' = R$ by uniqueness of the positive square root.
>
> **Uniqueness of $S$ when $T$ is invertible.** $T$ invertible iff $\operatorname{null} T = 0$ iff $\operatorname{null} R = 0$ iff $R$ is invertible. Then $S = T R^{-1}$ is uniquely determined and is unitary (since $T$ is invertible and $R$ is invertible positive). $\blacksquare$
>
> **Connection to SVD.** If $T = U \Sigma V^*$ is an SVD, then $T^*T = V \Sigma^2 V^*$, so $R = \sqrt{T^*T} = V \Sigma V^*$. And $S R = T$ gives $S = T R^{-1} = U \Sigma V^* (V \Sigma V^*)^{-1} = U \Sigma V^* \cdot V \Sigma^{-1} V^* = UV^*$ (when $T$ is invertible). So $S = UV^*$ and $R = V \Sigma V^*$ in SVD terms.

---

# Cross-Field Exercise Suggestions

1. **Continuum mechanics — deformation gradient.** The deformation of a continuum body is described by a deformation gradient $F$, a $3 \times 3$ invertible matrix at each point. Polar decomposition $F = RU$ separates rotation $R$ from stretch $U$ (symmetric positive definite). The eigenvalues of $U$ are the **principal stretches**, and the eigenvectors are the **principal directions of stretch**. The Cauchy–Green deformation tensor $C = F^t F = U^2$ encodes all the strain information. This is polar decomposition applied at every spacetime point of a deforming body.

2. **Computer graphics — extracting rotation from a matrix.** When animating a rigid body, the orientation is parameterised by a $3 \times 3$ rotation matrix, but numerical error during transformations can make the matrix drift away from $SO(3)$. Polar decomposition $M = RP$ extracts the closest rotation $R$, snapping the matrix back to the rotation group. This is "rotation re-orthogonalisation" in graphics pipelines.

3. **Quantum mechanics — purification of mixed states.** A density matrix $\rho$ has a unique positive square root $\sqrt{\rho}$. The "polar decomposition" perspective on purification: a pure state $|\psi\rangle = \sum \sqrt{\lambda_j} |j\rangle_A \otimes |j\rangle_B$ has reduced density matrix $\rho_A = \sum \lambda_j |j\rangle\langle j|$ on subsystem $A$, and the positive operator $\sqrt{\rho_A}$ is the "magnitude" half of $|\psi\rangle$ in the Schmidt decomposition.

4. **Optimal control — feedback gain regularisation.** The linear quadratic regulator (LQR) optimal control law involves a feedback gain matrix $K$ which can be ill-conditioned. Polar decomposition $K = U P$ separates the unitary "direction" $U$ from the positive "magnitude" $P$, allowing each to be regularised independently. This is used in robust control to ensure stability margins.

---

# Bridges

- **[[Thm - Singular Value Decomposition]]** — Polar decomposition follows from SVD by regrouping the factors. The two theorems are equivalent: SVD gives polar decomposition immediately by regrouping; polar decomposition gives SVD by diagonalising the positive factor $R$ via the spectral theorem.

- **[[Thm - Positive Operators Have a Unique Square Root]]** — Provides the positive factor $|T| = \sqrt{T^*T}$, whose existence and uniqueness make the polar decomposition canonical.

- **Iwasawa decomposition (Lie theory)** — For a real semisimple Lie group $G$, the Iwasawa decomposition $G = KAN$ generalises the polar decomposition (which for $\operatorname{GL}_n(\mathbb{C}) = U(n) \cdot P_n(\mathbb{C})$ is essentially $G = KA$, with $A$ the positive definite matrices). The decomposition $G = K \cdot P$ is the precise Lie-theoretic statement of "every group element is rotation times stretch", and is the foundation of analysis on symmetric spaces.

- **$KAK$ / Cartan decomposition (Lie theory)** — A further refinement: every element of a Lie group $G$ factors as $g = k_1 \cdot a \cdot k_2$ with $k_1, k_2 \in K$ (the maximal compact subgroup) and $a \in A$ (a maximal abelian subspace of the orthogonal complement). For $\operatorname{GL}_n(\mathbb{C})$, this is the SVD: $T = U \Sigma V^*$ with $U, V \in U(n)$ (compact) and $\Sigma$ diagonal positive (abelian).

- **Symmetric space structure of $\operatorname{GL}(V)/U(V)$** — The quotient is identifiable with the positive definite operators $P(V)$, with the action $T \cdot R = T R T^*$. Polar decomposition $T = SR$ realises this: $T$ acts on $I$ to produce $T I T^* = T T^* = R^2 = T \cdot I$, so the orbit of $I$ under $\operatorname{GL}(V)$ is $P(V)$, with stabiliser $U(V)$. This is the symmetric space geometry of positive definite matrices.

---

# Unlocked by This

> [!tip] Operator Magnitude and Phase *(from Functional Analysis)*
> The polar decomposition extends to bounded operators on infinite-dimensional Hilbert spaces, with $S$ now a **partial isometry** (an isometry from $(\operatorname{null} T)^\perp$ onto $\overline{\operatorname{range} T}$). The decomposition $T = S |T|$ is then the operator-theoretic analogue of $z = e^{i\theta} |z|$. The positive operator $|T| = \sqrt{T^* T}$ is called the **absolute value** of $T$ and plays a central role in the theory of compact operators (where the eigenvalues of $|T|$ are the singular values, and trace-class operators are those with summable singular values), in Schatten classes (where the $\ell^p$ norms of the singular values define the Schatten $p$-norms), and in the non-commutative integration theory of von Neumann algebras (where the polar decomposition is the link between the algebra and its measure-theoretic content).

> [!tip] Cartan Decomposition $\operatorname{GL}(n, \mathbb{C}) \cong U(n) \times P_n(\mathbb{C})$ *(from Lie Theory)*
> The polar decomposition gives a **diffeomorphism** $\operatorname{GL}(n, \mathbb{C}) \cong U(n) \times P_n(\mathbb{C})$, where $P_n(\mathbb{C})$ is the open cone of positive definite Hermitian matrices. This realises the **Cartan decomposition** of the real Lie algebra $\mathfrak{gl}_n(\mathbb{C}) = \mathfrak{u}(n) \oplus i\mathfrak{u}(n)$ at the group level. The decomposition is the basis of the symmetric space geometry of $P_n$ and the Iwasawa decomposition of $\operatorname{GL}_n(\mathbb{C})$. Both decompositions are starting points for harmonic analysis on Lie groups and the representation theory of $\operatorname{GL}_n$.

> [!tip] Procrustes Analysis and Distance to the Unitary Group *(from Statistics and Computer Graphics)*
> The **Procrustes problem** asks: given a matrix $A$, find the closest unitary matrix $U$ in the Frobenius norm. By an SVD argument, the answer is $U = U_A V_A^*$ — the isometric factor of the polar decomposition of $A$. The minimum distance is $\|A - U\|_F = \sqrt{\sum_j (s_j - 1)^2}$. This is used to align point clouds in computer graphics (the iterative closest-point algorithm), to align statistical configurations (generalised Procrustes analysis), to compute the rotation matrix in protein structure superposition (used in computational biology), and to extract rotational components from numerically drifting matrices in real-time graphics.

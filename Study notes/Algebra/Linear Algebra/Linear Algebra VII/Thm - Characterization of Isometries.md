---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Isometry"
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
  - "Def - Orthonormal Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ and $W$ are finite-dimensional [[Def - Inner Product Space|inner product spaces]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. An [[Def - Isometry|isometry]] is a linear map $S \in \mathcal{L}(V, W)$ with $\|Sv\| = \|v\|$ for all $v$. The [[Def - Adjoint of a Linear Map|adjoint]] $S^* \in \mathcal{L}(W, V)$ satisfies $\langle Sv, w \rangle = \langle v, S^* w \rangle$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Characterization of isometries).** Let $S \in \mathcal{L}(V, W)$ be a linear map between finite-dimensional inner product spaces. The following are equivalent:
>
> 1. $\|S v\| = \|v\|$ for all $v \in V$ (definition of isometry).
> 2. $\langle Sv, Sw \rangle = \langle v, w \rangle$ for all $v, w \in V$ ($S$ preserves the inner product).
> 3. $S^* S = I_V$.
> 4. $S$ sends *some* orthonormal basis of $V$ to an orthonormal list in $W$.
> 5. $S$ sends *every* orthonormal basis of $V$ to an orthonormal list in $W$.
> 6. The columns of the matrix of $S$ in any orthonormal bases of $V$ and $W$ are orthonormal.
>
> Furthermore, when $V = W$ (i.e., $S$ is an operator on $V$), the conditions (1)–(6) are equivalent to:
>
> 7. $S$ is a [[Def - Unitary Operator|unitary]] operator: $S^* S = S S^* = I$.

---

# Motivation

Each of the six (or seven) characterisations is the right form for a specific setting, and knowing which to reach for is what makes isometry arguments fluent.

- **(1)** for the verifier: norm preservation is the geometric content, the easiest to check from a description of $S$.
- **(2)** for the user: inner product preservation says all geometric structure transfers, useful when geometry is the question.
- **(3)** for the algebraist: $S^* S = I$ is the cleanest algebraic statement, what you write down when manipulating expressions symbolically.
- **(4) and (5)** for the constructor: the basis-mapping characterisations let you build isometries by specifying their action on a single orthonormal basis.
- **(6)** for the computer: the matrix-column condition is the form to verify when given a matrix presentation.
- **(7)** is the additional condition (surjectivity) that promotes an isometry to a [[Def - Unitary Operator|unitary operator]] when $V = W$.

The deep content is the equivalence (1) ⇔ (2): norm preservation and inner product preservation are the same condition. This is non-trivial: a priori, $\|Sv\| = \|v\|$ says one number for each $v$, while $\langle Sv, Sw \rangle = \langle v, w \rangle$ says one number for each pair $(v, w)$ — much more data. The reason they coincide is **polarisation**: the inner product is determined by the norm, so preserving the norm preserves all the inner product information.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$S$ is a linear map between inner product spaces". The theorem then triggers from any of the seven equivalent characterisations.

The first disguised source is **a map presented by its action on basis vectors**. If $S$ sends one orthonormal basis to an orthonormal list, then by (4) it is an isometry. *Example problem:* the discrete Fourier transform matrix maps the standard basis of $\mathbb{C}^n$ to a basis of orthonormal complex exponentials — hence it is a unitary operator. The signal-processing identification of "the DFT is unitary" is exactly characterisation (4).

The second disguised source is **a matrix whose columns are orthonormal**. By (6) the corresponding linear map is an isometry. *Example problem:* given the matrix of a rotation in $\mathbb{R}^3$, verify orthonormality of columns to confirm it is an isometry — much easier than computing $S^* S$ entry by entry.

The third disguised source is **a Gram matrix calculation**. If $S$ has $S^*S = I$, then $\langle S^* S v, w \rangle = \langle v, w \rangle$ — the Gram matrix of $\{S e_j\}$ equals the Gram matrix of $\{e_j\}$ for any basis. Conversely, equality of Gram matrices gives $S^* S = I$. *Example problem:* prove a Householder reflection $H_v = I - 2 \frac{v v^*}{v^* v}$ is an isometry; check $H_v^* H_v = I$ directly.

**Targets (Output Amplification)**

The conclusion is the equivalence of all seven (or six) characterisations.

Combine the conclusion with **invariance of orthonormal bases**: the image of any orthonormal basis under an isometry is orthonormal, so isometries are precisely the maps that preserve orthonormal bases. The further result $E$: the set of orthonormal bases of $V$ is acted on transitively by the unitary group $U(V)$, with stabiliser $U(V \cap \text{trivial})$. This **transitivity** is one form of the orbit-stabiliser theorem in [[Group Theory II — §1.3–1.4|group theory]].

Combine with **the matrix factorisation theorems**: every $A \in \operatorname{GL}_n(\mathbb{C})$ factors as $A = QR$ ([[Thm - QR Factorization|QR factorisation]]) with $Q$ an isometry (unitary in the square case) and $R$ upper-triangular. The further result $E$: the Gram–Schmidt algorithm, which produces the $Q$ from the columns of $A$, is the *constructive* version of characterisations (4)–(5).

Combine with **operator norm preservation**: an isometry has operator norm $1$. The further result $E$: when you precompose or postcompose with an isometry, the operator norm is preserved. This is what makes the Schatten norms and operator-norm-based metrics invariant under unitary changes of basis.

---

# Why Is It True

The equivalences flow from polarisation and the defining relation of the adjoint.

**The one-liner mechanism: $\langle Sv, Sw \rangle - \langle v, w \rangle = \langle (S^*S - I) v, w \rangle$, so all three equalities (norm-preserving, inner-product-preserving, $S^*S = I$) are equivalent by polarisation and uniqueness of the adjoint.**

For **(1) ⇔ (2)**, the polarisation identity expresses the inner product as a sum of norm-squared values: $\langle v, w \rangle = \frac{1}{4} \sum_{k=0}^{3} i^k \|v + i^k w\|^2$ over $\mathbb{C}$ (and a similar formula over $\mathbb{R}$). So if $S$ preserves the norm, it preserves the polarisation sum, hence the inner product. Conversely, inner product preservation gives norm preservation by setting $v = w$.

For **(2) ⇔ (3)**, push $S$ across the inner product: $\langle Sv, Sw \rangle = \langle v, S^* S w \rangle$, and this equals $\langle v, w \rangle$ for all $v$ iff $S^* S w = w$ for all $w$, iff $S^* S = I$. (Setting $v = (S^* S w - w)$ gives the converse.)

For **(3) ⇒ (4)**, take any orthonormal basis $e_1, \ldots, e_n$ of $V$. Then $\langle S e_i, S e_j \rangle = \langle e_i, S^* S e_j \rangle = \langle e_i, e_j \rangle = \delta_{ij}$, so the $S e_j$ are orthonormal.

For **(4) ⇒ (1)**, given orthonormal $e_1, \ldots, e_n$ with $S e_j$ also orthonormal: any $v = \sum_j \alpha_j e_j$ satisfies $\|v\|^2 = \sum |\alpha_j|^2$, and $\|S v\|^2 = \|\sum \alpha_j S e_j\|^2 = \sum |\alpha_j|^2$ (since $S e_j$ are orthonormal), so $\|Sv\| = \|v\|$.

For **(4) ⇔ (5)**, the forward direction is trivial. For the converse: characterisation (4) is preserved under change of orthonormal basis (compose with a unitary on the source, which preserves orthonormality). So "some basis" and "every basis" coincide.

For **(6)** as equivalent to **(3)**: in orthonormal bases, the column orthonormality of the matrix of $S$ is exactly the matrix relation $S^* S = I$, where $*$ is the conjugate transpose.

For **(7)**: in finite dimensions with $V = W$, $S^*S = I_V$ forces $S$ to be injective (norm-preserving), hence surjective (by dimension), hence invertible. The inverse is then $S^*$, and the relations $S^*S = SS^* = I$ both hold. So isometry on $V$ to $V$ in finite dimensions is unitary.

---

# What Makes This Hard

The most subtle step is **the equivalence (1) ⇔ (2)**: that norm preservation alone implies inner product preservation. The naive intuition is that "norm" gives one number per vector while "inner product" gives one per pair — but the polarisation identity collapses this difference. Without polarisation, the equivalence is mysterious.

The second subtle step is **(7)**: that in finite dimensions, $S^* S = I$ alone forces $S$ to be unitary (also $SS^* = I$). The argument needs that $S$ is injective (by norm preservation), hence surjective by dimension, hence invertible. In infinite dimensions both equalities must be assumed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use polarisation for (1) ⇔ (2). Use the defining relation of the adjoint for (2) ⇔ (3). Then derive (4), (5), (6) from these.

**Subgoal decomposition:**

1. **(1) ⇔ (2)**: norm preservation iff inner product preservation. Use polarisation.

2. **(2) ⇔ (3)**: inner product preservation iff $S^* S = I$. Use $\langle Sv, Sw \rangle = \langle v, S^* S w \rangle$.

3. **(3) ⇔ (4) and (5)**: $S^* S = I$ iff $S$ sends some/every orthonormal basis to orthonormal. Direct calculation in (3) ⇒ (4), and (4) ⇒ (3) by expanding $S^*S$ on basis vectors.

4. **(3) ⇔ (6)**: matrix form. Column orthonormality of $M = $ matrix of $S$ is $M^* M = I$.

5. **In finite dimensions with $V = W$ (case (7))**: (3) implies $S$ injective, hence surjective by dimension, hence $S$ invertible. Then $S^* = S^{-1}$, so $SS^* = I$ also.

---

# Lemma Decomposition

> [!note]- Lemma 1: Polarisation identity recovers the inner product from the norm
> **Statement:** Over $\mathbb{C}$, $\langle v, w \rangle = \frac{1}{4} \sum_{k=0}^{3} i^k \|v + i^k w\|^2$. Over $\mathbb{R}$, $\langle v, w \rangle = \frac{1}{4}(\|v + w\|^2 - \|v - w\|^2)$.
>
> **Hint:** Expand $\|v + i^k w\|^2 = \|v\|^2 + i^{-k} \langle v, w \rangle + i^k \langle w, v \rangle + \|w\|^2$ and sum over $k$.
>
> **Why needed:** Converts "norm preservation" into "inner product preservation" — the foundation of (1) ⇒ (2).
>
> > [!note]- Full proof
> > Over $\mathbb{C}$: $\|v + i^k w\|^2 = \langle v + i^k w, v + i^k w \rangle = \|v\|^2 + i^k \langle w, v \rangle + i^{-k} \langle v, w \rangle + \|w\|^2$. Multiply by $i^k$ and sum over $k = 0, 1, 2, 3$. The first and last terms have $\sum i^k = 0$. The $\langle w, v \rangle$ term: $\sum i^k \cdot i^k = \sum i^{2k} = (-1)^0 + (-1)^1 + \cdots = 0$. The $\langle v, w \rangle$ term: $\sum i^k \cdot i^{-k} = \sum 1 = 4$. So $\sum i^k \|v + i^k w\|^2 = 4 \langle v, w \rangle$.
> >
> > Over $\mathbb{R}$ (with $\langle \cdot, \cdot \rangle$ symmetric): $\|v + w\|^2 - \|v - w\|^2 = (\|v\|^2 + 2 \langle v, w \rangle + \|w\|^2) - (\|v\|^2 - 2 \langle v, w \rangle + \|w\|^2) = 4 \langle v, w \rangle$.

> [!note]- Lemma 2: $\langle Sv, Sw \rangle = \langle v, S^* S w \rangle$
> **Statement:** For any $S \in \mathcal{L}(V, W)$ and $v, w \in V$: $\langle Sv, Sw \rangle = \langle v, S^* S w \rangle$.
>
> **Hint:** Apply the defining relation of the adjoint once.
>
> **Why needed:** Converts "$S$ preserves inner product" to "$S^* S$ equals identity".
>
> > [!note]- Full proof
> > Direct: $\langle Sv, Sw \rangle_W = \langle v, S^* (Sw) \rangle_V = \langle v, (S^* S) w \rangle_V$, using the defining relation of $S^*$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> **(1) ⇔ (2):** If $\|Sv\| = \|v\|$ for all $v$, then $\|S(v + i^k w)\| = \|v + i^k w\|$ for all $v, w, k$. By Lemma 1 (polarisation),
> $$\langle Sv, Sw \rangle = \frac{1}{4} \sum_k i^k \|Sv + i^k Sw\|^2 = \frac{1}{4} \sum_k i^k \|S(v + i^k w)\|^2 = \frac{1}{4} \sum_k i^k \|v + i^k w\|^2 = \langle v, w \rangle.$$
> So (2) holds. Conversely, (2) with $v = w$ gives $\|Sv\|^2 = \|v\|^2$, i.e., (1).
>
> **(2) ⇔ (3):** By Lemma 2, $\langle Sv, Sw \rangle = \langle v, S^* S w \rangle$. So $\langle Sv, Sw \rangle = \langle v, w \rangle$ for all $v, w$ iff $\langle v, S^* S w \rangle = \langle v, w \rangle$ for all $v, w$ iff $\langle v, (S^*S - I) w \rangle = 0$ for all $v, w$ iff $S^* S w = w$ for all $w$ (set $v = (S^*S - I)w$) iff $S^* S = I_V$.
>
> **(3) ⇒ (4):** Let $e_1, \ldots, e_n$ be any orthonormal basis of $V$. Then $\langle S e_i, S e_j \rangle = \langle e_i, S^*S e_j \rangle = \langle e_i, e_j \rangle = \delta_{ij}$. So $\{S e_j\}$ is orthonormal in $W$.
>
> **(4) ⇒ (1):** Suppose $\{e_j\}$ is an orthonormal basis of $V$ with $\{S e_j\}$ orthonormal. Any $v \in V$ is $v = \sum_j \alpha_j e_j$ with $\|v\|^2 = \sum |\alpha_j|^2$. Then $Sv = \sum \alpha_j S e_j$, with $\|Sv\|^2 = \sum |\alpha_j|^2 = \|v\|^2$ (using orthonormality of $\{S e_j\}$). So $\|Sv\| = \|v\|$ for all $v$.
>
> **(4) ⇔ (5):** Trivially, (5) ⇒ (4). For (4) ⇒ (5): suppose $S$ sends *some* orthonormal basis $\{e_j\}$ to orthonormal. Let $\{f_k\}$ be any other orthonormal basis; the change-of-basis $U$ from $\{e_j\}$ to $\{f_k\}$ is unitary (i.e., $U^*U = I$). Then $f_k = U e_k$, so $S f_k = S U e_k$. We need $\{SU e_k\}$ orthonormal: $\langle SU e_i, SU e_j \rangle = \langle U e_i, S^* S U e_j \rangle$. From (4) ⇒ (3) (already shown), $S^*S = I$, so this is $\langle U e_i, U e_j \rangle = \langle e_i, U^* U e_j \rangle = \langle e_i, e_j \rangle = \delta_{ij}$. So $\{S f_k\}$ is orthonormal.
>
> **(3) ⇔ (6):** In orthonormal bases, the matrix $M$ of $S$ has $M^* M$ as the matrix of $S^* S$. So $S^* S = I_V$ iff $M^* M = I$, iff the columns of $M$ are orthonormal.
>
> **(7) when $V = W$ in finite dimensions:** From (3), $S^* S = I_V$. So $S$ is injective: $S v = 0$ implies $S^* S v = 0 = v$. In finite dimensions, an injective endomorphism is surjective (by rank-nullity), so $S$ is invertible. Then $S^* = S^{-1}$, hence $S S^* = S S^{-1} = I = S^{-1} S = S^* S$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

1. **Quantum computing — checking that a gate is unitary.** The Hadamard gate $H = \frac{1}{\sqrt 2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ — verify column-orthonormality by inspection (characterisation 6). Each column has norm $1$ and they are orthogonal. Hence $H$ is unitary. The same approach verifies CNOT, Toffoli, and other quantum gates in one glance.

2. **Numerical linear algebra — testing for orthogonality of computed bases.** When the Gram–Schmidt procedure is run on a list of vectors, the resulting matrix $Q$ has $Q^*Q \approx I$ — but with finite-precision arithmetic, the orthonormality is lost. The condition $\|Q^*Q - I\|$ measures this loss. Characterisation (6) — that the columns of $Q$ should be orthonormal — provides the standard diagnostic.

3. **Crystallography — symmetry operations of a lattice.** The symmetry group of a crystal is the subgroup of $O(n)$ consisting of orthogonal transformations preserving the lattice. Each symmetry is by definition an isometry of $\mathbb{R}^n$, and the orthogonality of the columns of its matrix (in the standard basis) is what makes the group structure work — composition of symmetries is composition of orthogonal matrices.

4. **Tensor networks — isometric tensors.** In the MERA (multi-scale entanglement renormalization ansatz) and similar tensor-network architectures, the basic building blocks are *isometric tensors* satisfying the matrix-level condition $V^\dagger V = I$ (characterisation 3, in the form of a contraction over indices). These isometric tensors are the essential components of the network, and their composition produces the wave functions of low-energy quantum states.

---

# Bridges

- **[[Thm - Gram-Schmidt Procedure|Gram–Schmidt]] and [[Thm - QR Factorization|QR Factorisation]]** — The Gram–Schmidt procedure takes a linearly independent list of vectors and produces an orthonormal list spanning the same subspace. The result, packaged as the matrix $Q$, is precisely an isometry by characterisation (4): the columns of $Q$ are orthonormal. QR factorisation then writes any invertible matrix as $A = QR$, with $Q$ isometric (unitary if $A$ is square invertible) and $R$ upper-triangular.

- **[[Def - Unitary Operator|Unitary Operators]]** — When $V = W$ in finite dimensions, isometries are exactly the unitary operators by characterisation (7). The unitary group $U(V)$ on a fixed inner product space is the set of all isometries; it is a compact Lie group, and the principal example of a "symmetry group" in linear algebra.

- **Polar Decomposition** — In the polar decomposition $T = U|T|$, the factor $U$ is an isometry (a partial isometry in general, a full isometry when $T$ has trivial kernel). The characterisation $S^*S = I$ on the appropriate subspace is what makes the polar decomposition's $U$ factor an honest map preserving lengths.

- **Stiefel manifold** — The set of isometries $\mathbb{F}^k \to \mathbb{F}^n$ (with $k \leq n$) forms the **Stiefel manifold** $V_k(\mathbb{F}^n)$ — equivalently the set of orthonormal $k$-frames in $\mathbb{F}^n$. By characterisation (6), $V_k(\mathbb{F}^n) = \{M \in \mathbb{F}^{n \times k} : M^*M = I_k\}$, an explicit quadratic variety. It is a homogeneous space for the unitary group $U(n)$ and a central object in algebraic topology (where its cohomology is computable from the matrix-equation description).

---

# Unlocked by This

> [!tip] Wigner Theorem and the Symmetries of Quantum Mechanics *(from Physics)*
> A theorem of Wigner says that every symmetry of a quantum system — a transformation of state space preserving probabilities — is implemented by either a unitary or an *anti-unitary* operator. The "preserving probabilities" condition $|\langle T\psi, T\phi \rangle|^2 = |\langle \psi, \phi \rangle|^2$ is weaker than full isometry — it allows complex conjugation. So Wigner's theorem extends the characterisation of isometries to the case where the inner product is preserved up to complex conjugation, with the resulting operator class being unitary $\cup$ anti-unitary. Time-reversal symmetry in quantum mechanics is anti-unitary, hinting at the deeper role of this extended class.

> [!tip] The Banach–Stone Theorem and Algebraic Isomorphisms *(from Functional Analysis)*
> The Banach–Stone theorem states that the linear isometries between two function spaces $C(X)$ and $C(Y)$ (with the sup norm) are exactly the maps of the form $f \mapsto \omega \cdot f \circ \tau$, where $\tau : Y \to X$ is a homeomorphism and $\omega$ is a continuous function with $|\omega| \equiv 1$. So isometric Banach spaces of continuous functions correspond to homeomorphic compact spaces — isometries "see" the underlying topology. This is a deep generalisation of the characterisation of isometries: in a function-space setting, the algebraic and topological structures coincide via isometries.

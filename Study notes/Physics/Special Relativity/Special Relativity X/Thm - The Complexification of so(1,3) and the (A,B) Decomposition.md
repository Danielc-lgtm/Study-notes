---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Generators and Structure Constants"
  - "Def - Lie Algebra"
tags: [physics, special-relativity, lie-groups, representation-theory]
---

# Notation

We set $c = 1$, $\eta = \mathrm{diag}(1,-1,-1,-1)$. The [[Def - Lie Algebra of the Lorentz Group|Lorentz algebra]] $\mathfrak{so}(1,3)$ has rotation generators $J_i$ and boost generators $K_i$ ($i=1,2,3$), with brackets $[J_i,J_j]=\epsilon_{ijk}J_k$, $[J_i,K_j]=\epsilon_{ijk}K_k$, $[K_i,K_j]=-\epsilon_{ijk}J_k$ (sums over $k$). The complexification of a real Lie algebra $\mathfrak{g}$ is $\mathfrak{g}_{\mathbb{C}} = \mathfrak{g}\otimes_{\mathbb{R}}\mathbb{C}$, the same brackets extended complex-bilinearly. $\mathfrak{su}(2)$ is the (real) Lie algebra of the rotation group's double cover; $\mathfrak{sl}(2,\mathbb{C})$ is the Lie algebra of $2\times 2$ complex traceless matrices. The new generators are $A_i = \tfrac12(J_i + iK_i)$ and $B_i = \tfrac12(J_i - iK_i)$. Full registry on [[Special Relativity X — The Lorentz Group as a Lie Group]].

> [!warning] Convention: the factor of $i$
> We use the **mathematics convention** $\Lambda = \exp(\omega)$ with real generators, so the structure constants carry no $i$ and the $(A,B)$ relations read $[A_i,A_j]=\epsilon_{ijk}A_k$. Physics texts use **Hermitian** generators $\Lambda = \exp(i\theta^a T_a)$, inserting an $i$ everywhere: their relations read $[A_i,A_j]=i\epsilon_{ijk}A_k$. The two are related by $A_i^{\text{phys}} = iA_i^{\text{math}}$ (and likewise for $J,K,B$). The decomposition $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ and the representation labels $(j_A,j_B)$ are identical in both conventions.

---

# Statement

> **Theorem (complexification and the (A,B) decomposition).** Over the complex numbers, define
> $$A_i = \tfrac12(J_i + iK_i), \qquad B_i = \tfrac12(J_i - iK_i), \qquad i = 1,2,3.$$
> These six elements span the complexified Lorentz algebra $\mathfrak{so}(1,3)_{\mathbb{C}}$, and they satisfy the **decoupled** commutation relations
> $$[A_i, A_j] = \sum_k\epsilon_{ijk}\,A_k, \qquad [B_i, B_j] = \sum_k\epsilon_{ijk}\,B_k, \qquad [A_i, B_j] = 0.$$
> Hence $\mathfrak{so}(1,3)_{\mathbb{C}}$ is the direct sum of two commuting copies of $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{su}(2)_{\mathbb{C}}$:
> $$\mathfrak{so}(1,3)_{\mathbb{C}} \;\cong\; \mathfrak{sl}(2,\mathbb{C}) \oplus \mathfrak{sl}(2,\mathbb{C}) \;\cong\; \mathfrak{su}(2)_{\mathbb{C}} \oplus \mathfrak{su}(2)_{\mathbb{C}}.$$

> **Corollary (classification of representations).** The finite-dimensional irreducible representations of $\mathfrak{so}(1,3)_{\mathbb{C}}$ are labelled by a pair $(j_A, j_B)$ of half-integers — one for each $\mathfrak{su}(2)$ factor — with dimension $(2j_A+1)(2j_B+1)$. The lowest cases are the scalar $(0,0)$, the left- and right-handed Weyl spinors $(\tfrac12,0)$ and $(0,\tfrac12)$, the four-vector $(\tfrac12,\tfrac12)$, the Dirac spinor $(\tfrac12,0)\oplus(0,\tfrac12)$, and the field strength $(1,0)\oplus(0,1)$.

---

# Motivation

The Lorentz algebra, as it stands, is an intertwined six-dimensional object: the boosts and rotations mix under each other's brackets, and there is no obvious way to break it into independent pieces. Over the real numbers there is none — $\mathfrak{so}(1,3)$ is *simple*. But the moment one allows complex coefficients, a miracle occurs: the algebra splits into two completely independent three-dimensional pieces, each a copy of the most familiar algebra in physics, the angular-momentum algebra $\mathfrak{su}(2)$. This theorem is that splitting, and it is the single most important structural fact about the Lorentz group, because it converts the hard problem "classify the representations of the Lorentz group" into the easy, already-solved problem "classify the representations of two independent copies of $\mathfrak{su}(2)$".

Why should one expect a split at all? The clue is the commutator $[K_i,K_j] = -\epsilon_{ijk}J_k$. Two boosts bracket to *minus* a rotation. If the sign were *plus*, the boosts and rotations would assemble into $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ — the algebra of four-dimensional Euclidean rotations, which famously splits into "self-dual" and "anti-self-dual" rotations. The Lorentz algebra has the *wrong sign* for a real split, but the wrong sign is exactly $-1 = i^2$, so introducing a factor of $i$ in the right combination repairs it. The combinations $A_i = \tfrac12(J_i + iK_i)$ and $B_i = \tfrac12(J_i - iK_i)$ are engineered so that the cross terms in their brackets cancel: $A$ closes among itself, $B$ closes among itself, and $A$ commutes with $B$. The factor of $i$ that "fixes the sign" is the precise sense in which **the Lorentz group is the Euclidean rotation group of four dimensions with one axis rotated into imaginary time**.

The payoff is the Wigner programme made elementary. The representation theory of $\mathfrak{su}(2)$ is the theory of spin: its irreducible representations are labelled by a single half-integer $j = 0, \tfrac12, 1, \tfrac32, \dots$, of dimension $2j+1$, and every physicist knows them as the spin-$j$ multiplets. Because $\mathfrak{so}(1,3)_{\mathbb{C}}$ is *two independent* copies of $\mathfrak{su}(2)$, its irreducible representations are labelled by *two* half-integers $(j_A, j_B)$ — one spin for each factor. This pair is the complete invariant of a relativistic field. A scalar is $(0,0)$; a four-vector is $(\tfrac12,\tfrac12)$; the two kinds of Weyl spinor, left and right, are $(\tfrac12,0)$ and $(0,\tfrac12)$, distinguished by *which* $\mathfrak{su}(2)$ factor they are charged under; the electromagnetic field strength is $(1,0)\oplus(0,1)$, its self-dual and anti-self-dual parts. So the entire field content of relativistic physics — every type of particle and field, organised by spin and chirality — is read directly off this one algebraic decomposition. The deepest material of the chapter is, at bottom, this theorem: it is the gateway from the geometry of the Lorentz group to the representation theory that classifies all of matter.

There is a subtlety the theorem also clarifies, and it is why the *group* topology matters. The split is of the *complexified* algebra, and a representation of $\mathfrak{so}(1,3)_{\mathbb{C}}$ need not exponentiate to a representation of the *group* $SO^+(1,3)$ — only to one of its double cover $SL(2,\mathbb{C})$, because $SO^+(1,3)$ is not simply connected ([[Thm - Topology of the Lorentz Group]]). The representations with $j_A + j_B$ a half-integer (the spinorial ones) are genuine only on the cover; this is the algebraic origin of the distinction between bosons (integer $j_A+j_B$) and fermions (half-integer), and it is why the topology of the previous theorem and the algebra of this one must be read together.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's input is "the Lorentz commutators $[J,J]=J$, $[J,K]=K$, $[K,K]=-J$". Recognising the decomposition's applicability is recognising this bracket structure in disguise.

The first disguised source is **"a six-dimensional algebra with a three-dimensional subalgebra acting on a three-dimensional complement as a vector, with the complement bracketing to minus the subalgebra"**. Any algebra of this shape complexifies to $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ by the same $A,B$ trick. The bridge is purely the sign of the complement-complement bracket: $-$ gives the Lorentz (split after complexifying), $+$ gives $\mathfrak{so}(4)$ (split already over $\mathbb{R}$). *Example problem:* given an unfamiliar algebra presented by such brackets, identify it as $\mathfrak{so}(1,3)_{\mathbb{C}}$ and read off its representations.

The second disguised source is **"a representation is built from two independent angular momenta"**. Whenever a system carries two commuting copies of angular momentum — for instance the self-dual and anti-self-dual parts of a two-form, or the left and right components of a Dirac field — it is secretly a representation of $\mathfrak{so}(1,3)_{\mathbb{C}}$, with $\mathbf{A}$ and $\mathbf{B}$ the two angular momenta. The bridge is $\mathbf{J} = \mathbf{A} + \mathbf{B}$ (the physical spin is the sum) and $\mathbf{K} = -i(\mathbf{A} - \mathbf{B})$ (the boost is the difference). *Example problem:* show that the spin content of the $(j_A,j_B)$ representation under the *rotation* subgroup is $j = |j_A - j_B|, \dots, j_A + j_B$, by adding the two angular momenta.

The third disguised source is **"a field has a definite chirality"**. A left-handed Weyl spinor is charged under the $A$ factor only ($(\tfrac12,0)$), a right-handed one under the $B$ factor only ($(0,\tfrac12)$); chirality *is* the choice of factor. The bridge is that complex conjugation exchanges $A \leftrightarrow B$ (since it sends $i \to -i$ in $A_i = \tfrac12(J_i+iK_i)$), so it exchanges left and right chirality. *Example problem:* show that the complex conjugate of a $(\tfrac12,0)$ Weyl spinor transforms as $(0,\tfrac12)$, the opposite chirality.

**Targets (Output Amplification)**

The conclusion is "$\mathfrak{so}(1,3)_{\mathbb{C}} = \mathfrak{su}(2)_A \oplus \mathfrak{su}(2)_B$, representations labelled $(j_A,j_B)$".

Combine the decomposition with **the $\mathfrak{su}(2)$ Clebsch–Gordan series**. Tensoring two Lorentz representations $(j_A,j_B)\otimes(j_A',j_B')$ decomposes by applying Clebsch–Gordan independently in each factor: $\bigoplus_{J_A}\bigoplus_{J_B}(J_A,J_B)$ with $J_A \in \{|j_A-j_A'|,\dots,j_A+j_A'\}$ and similarly $J_B$. The further result is the complete reduction of products of fields — for instance $(\tfrac12,\tfrac12)\otimes(\tfrac12,\tfrac12) = (1,1)\oplus(1,0)\oplus(0,1)\oplus(0,0)$, the decomposition of a rank-two tensor into traceless symmetric, self-dual and anti-self-dual antisymmetric, and trace parts. The combination is useful because it reduces all of Lorentz tensor algebra to $\mathfrak{su}(2)$ angular-momentum addition.

Combine the decomposition with **the requirement of a Lorentz-invariant Lagrangian**. A term in a Lagrangian is Lorentz-invariant exactly when it is in the $(0,0)$ representation, so building invariants means combining fields' $(j_A,j_B)$ labels down to $(0,0)$ via Clebsch–Gordan. The further result is the systematic construction of all possible interaction terms: a Yukawa coupling pairs $(\tfrac12,0)\otimes(0,\tfrac12)\otimes(0,0)$-type combinations to a scalar, a gauge coupling contracts a current $(\tfrac12,\tfrac12)$ with a vector field. The combination is the practical engine of model-building in particle physics.

Combine the decomposition with **the reality/chirality constraints**. Demanding that a field be real, or that it carry a definite chirality, restricts which $(j_A,j_B)$ are allowed: a real (Majorana) field needs $j_A = j_B$ or a $(j_A,j_B)\oplus(j_B,j_A)$ pairing; a parity-invariant theory needs $A \leftrightarrow B$ symmetry. The further result is the classification of *physical* fields as opposed to merely complex representations — Dirac $(\tfrac12,0)\oplus(0,\tfrac12)$ versus Weyl $(\tfrac12,0)$ versus Majorana. The combination explains why fermions come in exactly the varieties they do.

---

# Why Is It True

The proof is a short computation, but the *reason* it works is worth isolating, because it is the same reason Minkowski space is "Euclidean space with imaginary time".

Consider the Euclidean rotation algebra $\mathfrak{so}(4)$ first. It has six antisymmetric generators, which split into "self-dual" rotations $\mathbf{A} = \tfrac12(\mathbf{J} + \mathbf{K})$ and "anti-self-dual" rotations $\mathbf{B} = \tfrac12(\mathbf{J} - \mathbf{K})$ — here $\mathbf{K}$ are the rotations mixing the fourth Euclidean axis into the three spatial ones. Because $\mathfrak{so}(4)$ has $[K_i,K_j] = +\epsilon_{ijk}J_k$ (Euclidean sign), the cross terms in $[A_i,A_j]$ cancel *over the reals*, and $\mathfrak{so}(4) = \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ as a *real* direct sum. This is the well-known statement that four-dimensional rotations factor into two independent three-dimensional ones.

The Lorentz algebra is $\mathfrak{so}(4)$ with the fourth axis turned timelike, which flips the sign of the boost-boost bracket to $[K_i,K_j] = -\epsilon_{ijk}J_k$. Now watch the cancellation in $[A_i,A_j]$ with $A_i = \tfrac12(J_i + iK_i)$:
$$
[A_i, A_j] = \tfrac14\big([J_i,J_j] + i[J_i,K_j] + i[K_i,J_j] + i^2[K_i,K_j]\big).
$$
Insert the brackets. $[J_i,J_j] = \epsilon_{ijk}J_k$. The two cross terms $i[J_i,K_j] + i[K_i,J_j] = i\epsilon_{ijk}K_k + i\epsilon_{ijk}K_k = 2i\epsilon_{ijk}K_k$ (using $[K_i,J_j] = -[J_j,K_i] = -\epsilon_{jik}K_k = \epsilon_{ijk}K_k$). And the last term $i^2[K_i,K_j] = (-1)(-\epsilon_{ijk}J_k) = +\epsilon_{ijk}J_k$. So
$$
[A_i,A_j] = \tfrac14\big(\epsilon_{ijk}J_k + 2i\epsilon_{ijk}K_k + \epsilon_{ijk}J_k\big) = \tfrac14\big(2\epsilon_{ijk}J_k + 2i\epsilon_{ijk}K_k\big) = \tfrac12\epsilon_{ijk}(J_k + iK_k) = \epsilon_{ijk}A_k.
$$
**The single mechanism: the factor $i^2 = -1$ in $A_i = \tfrac12(J_i + iK_i)$ exactly cancels the minus sign in $[K_i,K_j] = -\epsilon J_k$, so that over $\mathbb{C}$ the Lorentz algebra has the same self-dual / anti-self-dual split that $\mathfrak{so}(4)$ has over $\mathbb{R}$.** The mixed bracket $[A_i,B_j]$ vanishes for the dual reason — the $A$ and $B$ combinations are conjugate, and their cross terms cancel with the *opposite* sign arrangement, leaving zero. So $A$ and $B$ live in orthogonal worlds, each a copy of $\mathfrak{su}(2)$.

The reason this single fact controls *all* Lorentz representations is that representation theory of a direct sum is the tensor product of the representation theories of the summands: an irreducible representation of $\mathfrak{su}(2)_A \oplus \mathfrak{su}(2)_B$ is an irreducible of the first tensored with an irreducible of the second, $V_{j_A}\otimes V_{j_B}$, labelled by the pair $(j_A,j_B)$. The physical rotation generator is $\mathbf{J} = \mathbf{A} + \mathbf{B}$, so the spin content under ordinary rotations is the Clebsch–Gordan sum of the two factors' spins — which is why a four-vector $(\tfrac12,\tfrac12)$ contains a spin-$1$ and a spin-$0$ part ($\tfrac12\otimes\tfrac12 = 1\oplus 0$: the three space components and the time component).

---

# What Makes This Hard

The computation has three brackets to insert and a sign to track in $[K_i,J_j] = -[J_j,K_i]$, and the place people slip is the antisymmetry there: writing $[K_i,J_j] = \epsilon_{ijk}K_k$ requires recognising it as $-[J_j,K_i] = -\epsilon_{jik}K_k = +\epsilon_{ijk}K_k$, and a dropped sign sends the cross terms to cancel instead of add (or the diagonal terms to cancel), collapsing the result. The conceptual subtlety, and the more common confusion, is that the split is of the *complexification* — the real algebra $\mathfrak{so}(1,3)$ does *not* contain two real copies of $\mathfrak{su}(2)$ (it is simple), and the two factors are exchanged by complex conjugation; mistaking the complex split for a real one leads to the wrong claim that $SO^+(1,3) = SU(2)\times SU(2)$ (the correct real statement is that $\mathfrak{so}(1,3) \cong \mathfrak{sl}(2,\mathbb{C})$ as a real algebra, and the complexification is the double).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Define $A_i, B_i$ as the $\tfrac12(J\pm iK)$ combinations; compute $[A_i,A_j]$, $[B_i,B_j]$, $[A_i,B_j]$ by expanding bilinearly and inserting the three Lorentz brackets, watching $i^2 = -1$ cancel the boost-boost sign; conclude each of $A,B$ obeys $\mathfrak{su}(2)$ relations and they commute, hence the direct-sum decomposition.

**Subgoal decomposition:**

1. **Invert the change of basis.** Express $J_i = A_i + B_i$ and $K_i = -i(A_i - B_i)$.
   - *Hint:* Add and subtract the definitions of $A_i, B_i$.
   - *Why needed:* It confirms $\{A_i,B_i\}$ is a basis of the complexification and gives the physical interpretation $\mathbf{J} = \mathbf{A}+\mathbf{B}$.

2. **Compute $[A_i, A_j]$.** Expand and insert brackets to get $\epsilon_{ijk}A_k$.
   - *Hint:* The diagonal terms $[J,J]$ and $i^2[K,K]$ both give $+\epsilon J$; the cross terms give $2i\epsilon K$; assemble to $\epsilon_{ijk}A_k$.
   - *Why needed:* It shows the $A$'s form an $\mathfrak{su}(2)$.

3. **Compute $[B_i, B_j]$.** By the same computation with $i \to -i$, get $\epsilon_{ijk}B_k$.
   - *Hint:* $B$ is the complex conjugate combination; the algebra is identical.
   - *Why needed:* It shows the $B$'s form a second $\mathfrak{su}(2)$.

4. **Compute $[A_i, B_j]$ and get $0$.** Expand; the cross terms now cancel against the diagonal.
   - *Hint:* $[A_i,B_j] = \tfrac14([J_i,J_j] - i[J_i,K_j] + i[K_i,J_j] - i^2[K_i,K_j])$; the $J$-terms cancel ($\epsilon J - \epsilon J$) and the $K$-terms cancel ($-i\epsilon K + i\epsilon K$).
   - *Why needed:* It shows the two $\mathfrak{su}(2)$'s commute, giving the direct sum.

5. **Conclude.** $\mathfrak{so}(1,3)_{\mathbb{C}} = \mathfrak{su}(2)_{\mathbb{C}}\oplus\mathfrak{su}(2)_{\mathbb{C}} = \mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$; representations labelled $(j_A,j_B)$.
   - *Hint:* A direct sum of Lie algebras has representations the tensor products of the factors' representations.
   - *Why needed:* It is the classification corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: The A, B generators form a basis of the complexification
> **Statement:** $A_i = \tfrac12(J_i+iK_i)$, $B_i = \tfrac12(J_i-iK_i)$ are six linearly independent elements of $\mathfrak{so}(1,3)_{\mathbb{C}}$ spanning it, with inverse $J_i = A_i + B_i$, $K_i = -i(A_i - B_i)$.
>
> **Hint:** Add and subtract the definitions.
>
> **Why needed:** It legitimises $\{A,B\}$ as a basis and gives $\mathbf{J} = \mathbf{A}+\mathbf{B}$, $\mathbf{K} = -i(\mathbf{A}-\mathbf{B})$.
>
> > [!note]- Full proof
> > Adding, $A_i + B_i = \tfrac12(J_i+iK_i) + \tfrac12(J_i-iK_i) = J_i$. Subtracting, $A_i - B_i = \tfrac12(J_i+iK_i) - \tfrac12(J_i-iK_i) = iK_i$, so $K_i = -i(A_i - B_i)$. Since $\{J_i, K_i\}$ is a basis of $\mathfrak{so}(1,3)$ and hence of $\mathfrak{so}(1,3)_{\mathbb{C}}$ over $\mathbb{C}$, and the change of basis to $\{A_i, B_i\}$ is invertible (the $6\times 6$ matrix with $\tfrac12$ and $\pm\tfrac{i}{2}$ entries has nonzero determinant), $\{A_i, B_i\}$ is also a basis. $\blacksquare$

> [!note]- Lemma 2: The A's close into su(2)
> **Statement:** $[A_i, A_j] = \sum_k \epsilon_{ijk}A_k$.
>
> **Hint:** Expand $[A_i,A_j] = \tfrac14([J_i,J_j] + i[J_i,K_j] + i[K_i,J_j] + i^2[K_i,K_j])$ and insert the Lorentz brackets.
>
> **Why needed:** It is the first $\mathfrak{su}(2)$ factor.
>
> > [!note]- Full proof
> > By bilinearity,
> > $$[A_i,A_j] = \tfrac14\big([J_i,J_j] + i[J_i,K_j] + i[K_i,J_j] + i^2[K_i,K_j]\big).$$
> > Insert $[J_i,J_j] = \epsilon_{ijk}J_k$, $[J_i,K_j] = \epsilon_{ijk}K_k$, $[K_i,J_j] = -[J_j,K_i] = -\epsilon_{jik}K_k = \epsilon_{ijk}K_k$, and $[K_i,K_j] = -\epsilon_{ijk}J_k$ with $i^2 = -1$, so $i^2[K_i,K_j] = (-1)(-\epsilon_{ijk}J_k) = \epsilon_{ijk}J_k$. Then
> > $$[A_i,A_j] = \tfrac14\big(\epsilon_{ijk}J_k + i\epsilon_{ijk}K_k + i\epsilon_{ijk}K_k + \epsilon_{ijk}J_k\big) = \tfrac14\big(2\epsilon_{ijk}J_k + 2i\epsilon_{ijk}K_k\big) = \tfrac12\epsilon_{ijk}(J_k + iK_k) = \epsilon_{ijk}A_k.\ \blacksquare$$

> [!note]- Lemma 3: The B's close into a second su(2)
> **Statement:** $[B_i, B_j] = \sum_k\epsilon_{ijk}B_k$.
>
> **Hint:** Identical to Lemma 2 with $i \to -i$ throughout.
>
> **Why needed:** It is the second $\mathfrak{su}(2)$ factor.
>
> > [!note]- Full proof
> > $$[B_i,B_j] = \tfrac14\big([J_i,J_j] - i[J_i,K_j] - i[K_i,J_j] + i^2[K_i,K_j]\big).$$
> > With the same substitutions, the $J$-terms give $\epsilon_{ijk}J_k + \epsilon_{ijk}J_k = 2\epsilon_{ijk}J_k$ and the $K$-terms give $-i\epsilon_{ijk}K_k - i\epsilon_{ijk}K_k = -2i\epsilon_{ijk}K_k$, so
> > $$[B_i,B_j] = \tfrac14\big(2\epsilon_{ijk}J_k - 2i\epsilon_{ijk}K_k\big) = \tfrac12\epsilon_{ijk}(J_k - iK_k) = \epsilon_{ijk}B_k.\ \blacksquare$$

> [!note]- Lemma 4: The A's and B's commute
> **Statement:** $[A_i, B_j] = 0$.
>
> **Hint:** Expand; the $J$-terms cancel each other and the $K$-terms cancel each other.
>
> **Why needed:** It is what makes the sum *direct* — two independent factors, not an intertwined algebra.
>
> > [!note]- Full proof
> > $$[A_i,B_j] = \tfrac14\big([J_i,J_j] - i[J_i,K_j] + i[K_i,J_j] - i^2[K_i,K_j]\big).$$
> > Insert: $[J_i,J_j] = \epsilon_{ijk}J_k$; $-i[J_i,K_j] = -i\epsilon_{ijk}K_k$; $+i[K_i,J_j] = +i\epsilon_{ijk}K_k$; $-i^2[K_i,K_j] = -(-1)(-\epsilon_{ijk}J_k) = -\epsilon_{ijk}J_k$. The two $J$-terms cancel ($\epsilon_{ijk}J_k - \epsilon_{ijk}J_k = 0$) and the two $K$-terms cancel ($-i\epsilon_{ijk}K_k + i\epsilon_{ijk}K_k = 0$). Hence $[A_i,B_j] = 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Define $A_i = \tfrac12(J_i + iK_i)$ and $B_i = \tfrac12(J_i - iK_i)$ in $\mathfrak{so}(1,3)_{\mathbb{C}}$. By Lemma 1 these form a basis, with $J_i = A_i + B_i$, $K_i = -i(A_i - B_i)$.
>
> By Lemmas 2, 3, 4,
> $$[A_i,A_j] = \sum_k\epsilon_{ijk}A_k, \qquad [B_i,B_j] = \sum_k\epsilon_{ijk}B_k, \qquad [A_i,B_j] = 0.$$
> The first relation says $\mathrm{span}_{\mathbb{C}}\{A_1,A_2,A_3\}$ is a complex Lie subalgebra with the $\mathfrak{su}(2)$ commutation relations, i.e. a copy of $\mathfrak{su}(2)_{\mathbb{C}} = \mathfrak{sl}(2,\mathbb{C})$; the second says the same for the $B$'s; the third says the two subalgebras commute. A Lie algebra that is the span of two commuting subalgebras with trivial intersection is their direct sum, so
> $$\mathfrak{so}(1,3)_{\mathbb{C}} = \mathrm{span}_{\mathbb{C}}\{A_i\}\oplus\mathrm{span}_{\mathbb{C}}\{B_i\} \cong \mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C}).$$
>
> **Representation corollary.** For a direct sum $\mathfrak{g}_1\oplus\mathfrak{g}_2$ of Lie algebras, every finite-dimensional irreducible representation is (uniquely) an external tensor product $V_1\boxtimes V_2$ of an irreducible of $\mathfrak{g}_1$ with one of $\mathfrak{g}_2$. The finite-dimensional irreducibles of $\mathfrak{sl}(2,\mathbb{C})$ are the spin-$j$ representations $V_j$ of dimension $2j+1$, $j \in \{0,\tfrac12,1,\dots\}$. Hence the irreducibles of $\mathfrak{so}(1,3)_{\mathbb{C}}$ are $V_{j_A}\boxtimes V_{j_B}$, labelled by the pair $(j_A,j_B)$, of dimension $(2j_A+1)(2j_B+1)$. The physical rotation subalgebra is generated by $\mathbf{J} = \mathbf{A}+\mathbf{B}$, so under ordinary rotations the representation $(j_A,j_B)$ decomposes (by Clebsch–Gordan) into spins $j = |j_A - j_B|, \dots, j_A + j_B$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Self-dual and anti-self-dual two-forms in electromagnetism.** The electromagnetic field strength $F_{\mu\nu}$ is an antisymmetric two-form, the $(1,0)\oplus(0,1)$ representation; its self-dual part $\mathbf{E} + i\mathbf{B}$ is the $(1,0)$ piece and its anti-self-dual part $\mathbf{E} - i\mathbf{B}$ is the $(0,1)$ piece, exactly the $A$- and $B$-charged halves. Maxwell's equations split correspondingly, and the Lorentz invariants $\mathbf{E}^2 - \mathbf{B}^2$ and $\mathbf{E}\cdot\mathbf{B}$ are the real and imaginary parts of $(\mathbf{E}+i\mathbf{B})^2$. The application is nonobvious because the familiar $\mathbf{E}, \mathbf{B}$ are obscuring a clean $(1,0)\oplus(0,1)$ structure that the $(A,B)$ decomposition reveals; see [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality]].

**Anti-de Sitter and the conformal group.** The conformal group of four-dimensional Minkowski space is $SO(2,4)$, whose complexification and real forms are analysed by the same $(A,B)$-style splitting; the $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ trick generalises to the identification of low-dimensional orthogonal algebras with products of $\mathfrak{sl}$'s ($\mathfrak{so}(4) = \mathfrak{su}(2)^2$, $\mathfrak{so}(6) = \mathfrak{su}(4)$, $\mathfrak{so}(2,4) = \mathfrak{su}(2,2)$). Recognising the Lorentz decomposition as the first case of this family is the bridge to the exceptional isomorphisms of low-rank Lie algebras.

**Euclidean instantons and the self-dual Yang–Mills equations.** In Euclidean signature the rotation group $\mathfrak{so}(4) = \mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R$ splits *over the reals*, and a gauge field strength can be self-dual (charged under $\mathfrak{su}(2)_L$ only) — these are the instantons. The Lorentzian $(A,B)$ decomposition is the Wick rotation of this, and the self-dual / anti-self-dual language is shared. The application connects relativistic representation theory to the topology of gauge fields; see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Bridges

- **[[Def - Lie Algebra of the Lorentz Group]]** — this theorem reorganises the algebra defined there. The intertwined generators $J_i, K_i$ with their three coupled bracket relations become, after complexifying and changing basis, two *decoupled* copies of $\mathfrak{su}(2)$. The decomposition does not change the algebra; it changes the basis to one in which the structure is transparent, and the price is admitting complex coefficients.

- **[[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]]** — the real form underlying the complexification is $\mathfrak{sl}(2,\mathbb{C})$: as a *real* six-dimensional Lie algebra, $\mathfrak{so}(1,3) \cong \mathfrak{sl}(2,\mathbb{C})$, and its complexification is the double $\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$. The group-level statement is that $SL(2,\mathbb{C})$ double-covers $SO^+(1,3)$, and the two factors $A, B$ correspond to a representation of $SL(2,\mathbb{C})$ and its complex conjugate — the undotted and dotted spinor indices.

- **[[Thm - Topology of the Lorentz Group]]** — the decomposition explains which $(j_A,j_B)$ representations are genuine representations of the *group* $SO^+(1,3)$ and which only of its cover. Integer $j_A + j_B$ (tensors) descend to the group; half-integer $j_A + j_B$ (spinors) are faithful only on $SL(2,\mathbb{C})$, because the non-contractible loop with $\pi_1 = \mathbb{Z}/2$ acts as $-1$. The algebra of this page and the topology of that one together produce the boson/fermion split.

- **Angular momentum and $\mathfrak{su}(2)$** — each factor is the algebra of angular momentum, $[A_i,A_j] = \epsilon_{ijk}A_k$, identical to $[J_i,J_j] = \epsilon_{ijk}J_k$ and to the quantum $[\hat L_i,\hat L_j] = i\hbar\epsilon_{ijk}\hat L_k$. The entire apparatus of spin — raising and lowering operators, the multiplet structure, Clebsch–Gordan coefficients — applies to each factor, which is why the representation theory is "already solved": it is two copies of the theory of spin.

---

# Unlocked by This

> [!tip] The Field Content of Relativistic Physics *(from Quantum Field Theory)*
> Every relativistic field is a $(j_A,j_B)$ representation, and this is the **complete dictionary**: the scalar $\phi$ is $(0,0)$; the left and right **Weyl spinors** $\psi_L, \psi_R$ are $(\tfrac12,0)$ and $(0,\tfrac12)$; the **Dirac spinor** is $(\tfrac12,0)\oplus(0,\tfrac12)$; the four-vector potential $A_\mu$ is $(\tfrac12,\tfrac12)$; the field strength $F_{\mu\nu}$ is $(1,0)\oplus(0,1)$; the metric perturbation (graviton) is the symmetric traceless $(1,1)$. Building a Lagrangian is combining these to $(0,0)$ via Clebsch–Gordan in each factor. This labelling *is* the organising principle of field theory.

> [!tip] Chirality and the Weak Interaction *(from Particle Physics)*
> The two factors $A, B$ are **left and right chirality**, exchanged by complex conjugation (parity). A theory that treats them asymmetrically violates parity — and the weak interaction does exactly this: it couples only to left-handed $(\tfrac12,0)$ fermions. The existence of two independent $\mathfrak{su}(2)$ factors is the precise sense in which "left-handed" and "right-handed" are distinct, Lorentz-invariant notions, and the maximal parity violation of the weak force is the statement that nature uses one factor and not the other.

> [!tip] The Wigner Classification and the Definition of a Particle *(from Quantum Field Theory)*
> Adjoining translations promotes the Lorentz algebra to the **Poincaré algebra**, whose unitary irreducible representations Wigner classified by two Casimirs — the **mass** $P^2 = m^2$ and the **spin** (Pauli–Lubanski square). For a massive particle the little group is $SO(3)$ and the spin is a single half-integer; for a massless particle it is $ISO(2)$ and the label is helicity. The finite-dimensional $(j_A,j_B)$ labels of *fields* and the unitary $(m, s)$ labels of *particles* are linked by the field equations. This is the rigorous meaning of "a particle is an irreducible representation of the Poincaré group"; see [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

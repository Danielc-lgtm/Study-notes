---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Complexification of so(1,3) and the (A,B) Decomposition"
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Generators and Structure Constants"
tags: [physics, special-relativity, lie-groups, representation-theory]
---

# Problem Statement

Starting from the Lorentz commutators $[J_i,J_j]=\epsilon_{ijk}J_k$, $[J_i,K_j]=\epsilon_{ijk}K_k$, $[K_i,K_j]=-\epsilon_{ijk}J_k$, carry out the complex change of basis that decouples the algebra.

1. Define $A_i = \tfrac12(J_i + iK_i)$ and $B_i = \tfrac12(J_i - iK_i)$. Compute $[A_i, A_j]$ and show it equals $\epsilon_{ijk}A_k$.
2. Compute $[A_i, B_j]$ and show it vanishes.
3. Conclude that $\mathfrak{so}(1,3)_{\mathbb{C}} \cong \mathfrak{su}(2)_{\mathbb{C}} \oplus \mathfrak{su}(2)_{\mathbb{C}}$, and explain why the decomposition requires *complexifying* — why the real algebra $\mathfrak{so}(1,3)$ does not split.
4. Use the labelling $(j_A, j_B)$ to identify the representations: the scalar, the four-vector, the two Weyl spinors, and the electromagnetic field strength. For the four-vector $(\tfrac12,\tfrac12)$, decompose its rotation content using $\mathbf{J} = \mathbf{A}+\mathbf{B}$.

**Recall:**

![[Thm - The Complexification of so(1,3) and the (A,B) Decomposition#Statement]]

The complexification $\mathfrak{g}_{\mathbb{C}} = \mathfrak{g}\otimes_{\mathbb{R}}\mathbb{C}$ extends the bracket complex-bilinearly. A real Lie algebra is **simple** if it has no proper nonzero ideal. The irreducible representations of $\mathfrak{su}(2)$ are the spin-$j$ representations $V_j$ of dimension $2j+1$, $j \in \{0,\tfrac12,1,\dots\}$; under a direct sum, irreducibles are tensor products $V_{j_A}\boxtimes V_{j_B}$. The physical spin under rotations is $\mathbf{J} = \mathbf{A}+\mathbf{B}$, decomposed by Clebsch–Gordan.

---

# Convergent Strategy

**Problem class.** A *change-of-basis to reveal structure* problem — the deepest in the chapter, the complex decoupling that turns Lorentz representation theory into two copies of spin. The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]] says any representation-theory question routes through the $(A,B)$ change of basis.

**Assumption pattern.** The three Lorentz commutators are given, and the combinations $A_i = \tfrac12(J_i+iK_i)$ are engineered so the cross terms cancel. The signpost is the minus sign in $[K_i,K_j]=-\epsilon J_k$: it is $i^2$, so the factor of $i$ in $A_i$ exactly repairs it, decoupling the algebra.

**Theorem routing.** Part 1: expand $[A_i,A_j]$ bilinearly, insert the three brackets (with the sign subtlety $[K_i,J_j]=\epsilon_{ijk}K_k$), watch $i^2[K,K] = +\epsilon J$ combine with $[J,J]=\epsilon J$ and the cross terms to give $\epsilon_{ijk}A_k$ ([[Thm - The Complexification of so(1,3) and the (A,B) Decomposition]]). Part 2: same expansion for $[A_i,B_j]$, where the $J$-terms and $K$-terms each cancel, giving $0$. Part 3: direct sum of two commuting $\mathfrak{su}(2)$'s; simplicity of the real algebra blocks a real split. Part 4: the $(j_A,j_B)$ dictionary and Clebsch–Gordan.

**Key decision point.** The crux is the sign tracking in $[K_i,J_j] = -[J_j,K_i] = -\epsilon_{jik}K_k = +\epsilon_{ijk}K_k$, and the combination $i^2(-\epsilon J_k) = +\epsilon J_k$. A single dropped sign collapses the result — the cross terms would cancel instead of add, or the $J$-terms would cancel. The conceptual decision is recognising the split is of the *complexification*: the two factors are complex-conjugate, not separately real, so one must say "complexified" at every step.

---

# Legal Operations Used

1. **Change basis to $(A,B)$ to decouple the algebra (operation 9 from the topic page).** The entire exercise: form $A_i, B_i$ and recompute the brackets to expose two commuting $\mathfrak{su}(2)$'s.

2. **Compute a commutator from the structure relations (operation 3 from the topic page).** Parts 1–2 expand $[A_i,A_j]$ and $[A_i,B_j]$ using the three Lorentz relations.

---

# Hints

> [!note]- Hint 1
> Expand bilinearly: $[A_i, A_j] = \tfrac14([J_i,J_j] + i[J_i,K_j] + i[K_i,J_j] + i^2[K_i,K_j])$. The four brackets are all known.

> [!note]- Hint 2
> Be careful with $[K_i, J_j]$: it is $-[J_j, K_i] = -\epsilon_{jik}K_k = +\epsilon_{ijk}K_k$ (one sign from antisymmetry of the bracket, one from antisymmetry of $\epsilon$). And $i^2[K_i,K_j] = (-1)(-\epsilon_{ijk}J_k) = +\epsilon_{ijk}J_k$.

> [!note]- Hint 3
> Collect: the two $J$-terms ($[J,J]$ and $i^2[K,K]$) both give $+\epsilon_{ijk}J_k$, summing to $2\epsilon J_k$; the two cross terms both give $i\epsilon_{ijk}K_k$, summing to $2i\epsilon K_k$. So $[A_i,A_j] = \tfrac14(2\epsilon J_k + 2i\epsilon K_k) = \tfrac12\epsilon(J_k + iK_k) = \epsilon A_k$.

> [!note]- Hint 4
> For $[A_i,B_j]$, the expansion is $\tfrac14([J_i,J_j] - i[J_i,K_j] + i[K_i,J_j] - i^2[K_i,K_j])$. Now the $J$-terms are $\epsilon J_k - \epsilon J_k = 0$ and the $K$-terms are $-i\epsilon K_k + i\epsilon K_k = 0$. Everything cancels.

> [!note]- Hint 5
> For part 3: the real algebra $\mathfrak{so}(1,3)$ is *simple* (no proper ideal), so it cannot be a direct sum over $\mathbb{R}$. The combinations $A_i, B_i$ are genuinely complex (they involve $i$), so they live in the complexification; complex conjugation sends $A_i \leftrightarrow B_i$, which is why the two factors are conjugate rather than independent.

---

# Solution

The combinations $A_i = \tfrac12(J_i+iK_i)$, $B_i = \tfrac12(J_i-iK_i)$ decouple the algebra: $[A_i,A_j]=\epsilon_{ijk}A_k$, $[B_i,B_j]=\epsilon_{ijk}B_k$, $[A_i,B_j]=0$, so $\mathfrak{so}(1,3)_{\mathbb{C}}$ is two commuting copies of $\mathfrak{su}(2)$. The factor $i^2=-1$ repairs the minus sign in $[K,K]=-\epsilon J$; the split needs complexification because the real algebra is simple. Representations are labelled $(j_A,j_B)$.

**Step 1: $[A_i, A_j] = \epsilon_{ijk}A_k$.**

> [!note]- Derivation
> By complex-bilinearity of the bracket,
> $$[A_i, A_j] = \tfrac14\big[J_i + iK_i,\ J_j + iK_j\big] = \tfrac14\big([J_i,J_j] + i[J_i,K_j] + i[K_i,J_j] + i^2[K_i,K_j]\big).$$
> Insert the Lorentz relations:
> - $[J_i,J_j] = \epsilon_{ijk}J_k$;
> - $i[J_i,K_j] = i\epsilon_{ijk}K_k$;
> - $i[K_i,J_j] = i\cdot(-[J_j,K_i]) = i\cdot(-\epsilon_{jik}K_k) = i\epsilon_{ijk}K_k$ (using $\epsilon_{jik} = -\epsilon_{ijk}$);
> - $i^2[K_i,K_j] = (-1)(-\epsilon_{ijk}J_k) = \epsilon_{ijk}J_k$.
>
> The two $J$-terms sum to $2\epsilon_{ijk}J_k$; the two $K$-terms sum to $2i\epsilon_{ijk}K_k$. So
> $$[A_i, A_j] = \tfrac14\big(2\epsilon_{ijk}J_k + 2i\epsilon_{ijk}K_k\big) = \tfrac12\epsilon_{ijk}(J_k + iK_k) = \epsilon_{ijk}A_k.$$
> The $A$'s satisfy the $\mathfrak{su}(2)$ commutation relations. The identical computation with $i \to -i$ gives $[B_i,B_j] = \epsilon_{ijk}B_k$.
>
> *The mechanism:* the factor $i^2 = -1$ in $A_i$ exactly cancels the minus sign in $[K_i,K_j] = -\epsilon J_k$, so the boost-boost term *adds* to the rotation-rotation term instead of being unavailable. This is the algebraic statement that "the Lorentz group is $\mathfrak{so}(4)$ with one axis rotated into imaginary time".

**Step 2: $[A_i, B_j] = 0$.**

> [!note]- Derivation
> $$[A_i, B_j] = \tfrac14\big[J_i + iK_i,\ J_j - iK_j\big] = \tfrac14\big([J_i,J_j] - i[J_i,K_j] + i[K_i,J_j] - i^2[K_i,K_j]\big).$$
> Insert:
> - $[J_i,J_j] = \epsilon_{ijk}J_k$;
> - $-i[J_i,K_j] = -i\epsilon_{ijk}K_k$;
> - $+i[K_i,J_j] = +i\epsilon_{ijk}K_k$;
> - $-i^2[K_i,K_j] = -(-1)(-\epsilon_{ijk}J_k) = -\epsilon_{ijk}J_k$.
>
> Now the two $J$-terms cancel ($\epsilon_{ijk}J_k - \epsilon_{ijk}J_k = 0$) and the two $K$-terms cancel ($-i\epsilon_{ijk}K_k + i\epsilon_{ijk}K_k = 0$). Hence
> $$[A_i, B_j] = 0.$$
> The $A$-world and the $B$-world commute completely: they are independent.

**Step 3: The direct-sum decomposition, and why it needs $\mathbb{C}$.**

> [!note]- Derivation
> Steps 1–2 show that $\mathrm{span}_{\mathbb{C}}\{A_i\}$ and $\mathrm{span}_{\mathbb{C}}\{B_i\}$ are each three-dimensional complex Lie algebras with $\mathfrak{su}(2)$ relations (i.e. copies of $\mathfrak{su}(2)_{\mathbb{C}} = \mathfrak{sl}(2,\mathbb{C})$), and they commute. Since together they span the six-dimensional $\mathfrak{so}(1,3)_{\mathbb{C}}$ and intersect trivially,
> $$\mathfrak{so}(1,3)_{\mathbb{C}} = \mathrm{span}_{\mathbb{C}}\{A_i\} \oplus \mathrm{span}_{\mathbb{C}}\{B_i\} \cong \mathfrak{su}(2)_{\mathbb{C}} \oplus \mathfrak{su}(2)_{\mathbb{C}} = \mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C}).$$
>
> *Why complexification is essential.* The combinations $A_i = \tfrac12(J_i + iK_i)$ are *genuinely complex* — they are not in the real span of $\{J_i, K_i\}$, because of the explicit $i$. So they live in the complexification $\mathfrak{so}(1,3)_{\mathbb{C}}$, not in the real $\mathfrak{so}(1,3)$. The real algebra does *not* split: it is **simple** (it has no proper nonzero ideal — a fact one checks from the structure relations, which let any generator be reached from any other by bracketing). A simple algebra cannot be a direct sum of two nonzero pieces. The resolution is that complex conjugation sends $A_i \mapsto \bar A_i = \tfrac12(J_i - iK_i) = B_i$, exchanging the two factors; the real algebra is the *fixed-point set* of this conjugation, which mixes the two complex factors and so is simple. The slogan: $\mathfrak{so}(1,3) \cong \mathfrak{sl}(2,\mathbb{C})$ as a *real* algebra (six real dimensions), and its complexification is the *double* $\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$.

**Step 4: The $(j_A, j_B)$ dictionary.**

> [!note]- Derivation
> Because $\mathfrak{so}(1,3)_{\mathbb{C}}$ is a direct sum of two $\mathfrak{su}(2)$'s, its irreducible representations are tensor products $V_{j_A}\boxtimes V_{j_B}$, labelled by a pair of spins $(j_A, j_B)$, of dimension $(2j_A+1)(2j_B+1)$:
> - **Scalar $(0,0)$**: dimension $1$. Invariant under the whole group — a scalar field $\phi$.
> - **Left Weyl spinor $(\tfrac12,0)$**: dimension $2$. Charged under the $A$-factor only — left-handed chirality.
> - **Right Weyl spinor $(0,\tfrac12)$**: dimension $2$. Charged under the $B$-factor only — right-handed chirality. The two Weyl spinors are exchanged by complex conjugation (which swaps $A \leftrightarrow B$), i.e. by parity.
> - **Four-vector $(\tfrac12,\tfrac12)$**: dimension $4$. The vector potential $A_\mu$, the four-velocity, any four-vector.
> - **Dirac spinor $(\tfrac12,0)\oplus(0,\tfrac12)$**: dimension $4$. A left plus a right Weyl spinor — a parity-symmetric fermion.
> - **Field strength $(1,0)\oplus(0,1)$**: dimension $3 + 3 = 6$. The antisymmetric $F_{\mu\nu}$; its self-dual part $\mathbf{E}+i\mathbf{B}$ is $(1,0)$, its anti-self-dual part $\mathbf{E}-i\mathbf{B}$ is $(0,1)$.
>
> *Rotation content of the four-vector.* Under ordinary rotations the generator is $\mathbf{J} = \mathbf{A} + \mathbf{B}$, so the spin of $(j_A,j_B)$ decomposes by adding the two angular momenta: $j = |j_A - j_B|, \dots, j_A + j_B$. For the four-vector $(\tfrac12,\tfrac12)$, this is $\tfrac12 \otimes \tfrac12 = 1 \oplus 0$ — a spin-$1$ and a spin-$0$ part. These are exactly the three *spatial* components of the four-vector (the spin-$1$ vector under rotations) and the one *time* component (the rotation-scalar). So the $(A,B)$ label $(\tfrac12,\tfrac12)$ correctly predicts that a four-vector splits, under rotations, into a $3$-vector and a scalar — which is geometrically obvious but here falls out of the representation theory.

> [!note]- Complete formal solution
> With $A_i = \tfrac12(J_i+iK_i)$, $B_i = \tfrac12(J_i-iK_i)$: expanding $[A_i,A_j] = \tfrac14([J_i,J_j] + i[J_i,K_j] + i[K_i,J_j] + i^2[K_i,K_j])$ and inserting $[J_i,J_j]=\epsilon_{ijk}J_k$, $[J_i,K_j]=\epsilon_{ijk}K_k$, $[K_i,J_j]=\epsilon_{ijk}K_k$, $i^2[K_i,K_j]=+\epsilon_{ijk}J_k$, the $J$-terms give $2\epsilon J_k$ and the $K$-terms $2i\epsilon K_k$, so $[A_i,A_j]=\tfrac12\epsilon_{ijk}(J_k+iK_k)=\epsilon_{ijk}A_k$ (and similarly $[B_i,B_j]=\epsilon_{ijk}B_k$). For $[A_i,B_j]=\tfrac14([J_i,J_j] - i[J_i,K_j] + i[K_i,J_j] - i^2[K_i,K_j])$ the $J$-terms cancel ($\epsilon J - \epsilon J$) and the $K$-terms cancel ($-i\epsilon K + i\epsilon K$), giving $0$. Hence $\mathfrak{so}(1,3)_{\mathbb{C}} = \mathfrak{su}(2)_A \oplus \mathfrak{su}(2)_B$. The split requires complexification because the real $\mathfrak{so}(1,3)$ is simple; conjugation swaps $A \leftrightarrow B$, so the real form is $\mathfrak{sl}(2,\mathbb{C})$ and its complexification is the double. Representations are labelled $(j_A,j_B)$: scalar $(0,0)$, Weyl $(\tfrac12,0)/(0,\tfrac12)$, four-vector $(\tfrac12,\tfrac12)$, Dirac $(\tfrac12,0)\oplus(0,\tfrac12)$, field strength $(1,0)\oplus(0,1)$; the four-vector's rotation content is $\mathbf{A}+\mathbf{B}$ spin $\tfrac12\otimes\tfrac12 = 1\oplus 0$ (spatial $3$-vector plus time scalar). $\blacksquare$

---

# Key Takeaways

**One factor of $i$ converts the Lorentz algebra into two copies of spin, and that is the whole of relativistic representation theory.** The change of basis $A_i = \tfrac12(J_i + iK_i)$ does something almost magical: it takes the intertwined six-generator Lorentz algebra and splits it into two completely independent copies of the angular-momentum algebra $\mathfrak{su}(2)$. The mechanism is that the factor $i^2 = -1$ cancels the minus sign in $[K,K] = -\epsilon J$, the one sign that distinguished the Lorentz algebra from the cleanly-splitting Euclidean $\mathfrak{so}(4)$. The reusable consequence is enormous: because $\mathfrak{su}(2)$ representation theory is the fully-solved theory of spin, the representations of the Lorentz group are just *pairs* of spins $(j_A, j_B)$, and the entire apparatus — multiplets, ladder operators, Clebsch–Gordan — applies twice. The trigger to reach for this decomposition: any question about how relativistic objects transform, what fields are possible, or how to build Lorentz invariants. The deepest lesson of the chapter is that the symmetry group of spacetime is, after one complex change of basis, two copies of the rotation group — which is why "spin" is the universal label of matter.

**The split is of the complexification, and forgetting that "complex" is the most common error.** The real algebra $\mathfrak{so}(1,3)$ is *simple* — it does not split at all over the reals — and the temptation to write $SO^+(1,3) = SU(2)\times SU(2)$ or $\mathfrak{so}(1,3) = \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ over $\mathbb{R}$ is wrong on a checkable point: $SU(2)\times SU(2)$ is compact while the Lorentz group is not. The combinations $A_i, B_i$ are genuinely complex (they carry an explicit $i$), so they live in the complexification, and complex conjugation *exchanges* the two factors — they are conjugate, not independent. The correct real statement is $\mathfrak{so}(1,3) \cong \mathfrak{sl}(2,\mathbb{C})$ as a real six-dimensional Lie algebra, whose complexification is the double $\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$. The reusable discipline: keep "complexified" in front of the decomposition at every step, and remember that the two factors being complex-conjugate is exactly the structure that makes left and right chirality distinct but parity-related. This conjugation is why a left-handed Weyl spinor $(\tfrac12,0)$ has a right-handed conjugate $(0,\tfrac12)$, and it is the algebraic root of why antiparticles exist.

**The $(j_A, j_B)$ label is the complete dictionary of fields, and the physical spin is the sum.** Every relativistic field is a point $(j_A, j_B)$ in a two-dimensional lattice of half-integers, and this single label determines everything about how it transforms: its dimension $(2j_A+1)(2j_B+1)$, its spin content under rotations ($\mathbf{J} = \mathbf{A}+\mathbf{B}$, decomposed by Clebsch–Gordan as $j = |j_A-j_B|,\dots,j_A+j_B$), and its chirality (which factor it is charged under). The dictionary — scalar $(0,0)$, Weyl $(\tfrac12,0)/(0,\tfrac12)$, vector $(\tfrac12,\tfrac12)$, field strength $(1,0)\oplus(0,1)$, graviton $(1,1)$ — is the organising table of all of field theory, and building a Lorentz-invariant Lagrangian is the combinatorics of reducing tensor products of these labels to the singlet $(0,0)$. The reusable insight: to understand any relativistic object, find its $(j_A, j_B)$, and then *every* transformation property follows from the two-copies-of-$\mathfrak{su}(2)$ structure. The four-vector example — $(\tfrac12,\tfrac12)$ splitting into a spatial $3$-vector (spin $1$) and a time scalar (spin $0$) under rotations — shows the representation theory correctly reproducing the obvious geometric decomposition, a check that the abstract machinery is tracking the physics. This is the gateway to the Wigner classification, where adjoining translations turns these field labels into the mass-and-spin labels of particles.

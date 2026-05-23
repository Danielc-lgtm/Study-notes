---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Space"
  - "Def - Bilinear Form"
tags: [geometry, differential-geometry, lie-groups, algebra]
---

# Notation

A Lie algebra is written $(\mathfrak{g}, [\cdot, \cdot])$: a vector space $\mathfrak{g}$ together with a bilinear bracket. Lowercase Fraktur letters $\mathfrak{g}, \mathfrak{h}, \mathfrak{k}, \mathfrak{l}, \mathfrak{n}$ are conventional for Lie algebras. Elements are usually denoted by capital Roman letters $X, Y, Z, W$. The bracket of $X$ and $Y$ is $[X, Y] \in \mathfrak{g}$. The base field is $\mathbb{R}$ unless stated otherwise.

---

# Axiom Motivation

A Lie algebra is what you get when you strip a Lie group of everything except its first-order behaviour at the identity. The motivating examples come from two sources, and the axioms are designed to capture exactly what is common to both.

**Source 1: tangent spaces of Lie groups at the identity.** For a Lie group $G$, the tangent space $T_e G$ is a vector space. The left-invariant vector fields on $G$ form a vector space canonically isomorphic to $T_e G$, and they are closed under the Lie bracket of vector fields. So $T_e G$ inherits a bracket via this identification — a bilinear map $[\cdot, \cdot] : T_e G \times T_e G \to T_e G$. The properties this bracket satisfies are: **bilinearity** (from bilinearity of the vector-field bracket in each argument), **antisymmetry** $[X, Y] = -[Y, X]$ (from antisymmetry of the vector-field bracket), and the **Jacobi identity** (from the corresponding identity for vector fields). These three properties are what we abstract into the Lie algebra axioms.

**Source 2: the matrix commutator.** For any associative algebra $A$ (say $A = M(n, \mathbb{R})$, the algebra of $n \times n$ matrices), the bracket $[a, b] = ab - ba$ — the **commutator** — gives a bilinear antisymmetric operation on $A$. The Jacobi identity for the commutator,

$$[a, [b, c]] + [b, [c, a]] + [c, [a, b]] = 0,$$

is a one-line calculation expanding both sides via the associative product. So every associative algebra has a Lie algebra structure under the commutator, and matrix algebras give the most important examples.

The remarkable fact, which is the content of the [[Thm - Left-Invariant Vector Fields Form a Lie Algebra|Lie algebra of a Lie group theorem]], is that **the Lie algebra of any matrix Lie group is the matrix commutator** restricted to the appropriate tangent space — see [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]. So the two sources are not just analogous; they are the same construction, with matrix Lie groups embedded in $\mathrm{GL}(n)$ realizing the commutator bracket.

Now, the axioms. Why **bilinearity**? The bracket should respect the vector space structure of $\mathfrak{g}$: scaling and addition in either slot should be transparent. This is a basic compatibility, and it makes the bracket a linear operator from $\mathfrak{g}$ to $\mathrm{End}(\mathfrak{g})$ in each slot (the adjoint map $\mathrm{ad}_X(Y) = [X, Y]$).

Why **antisymmetry**? Algebraically, antisymmetry is what distinguishes the Lie bracket from the symmetric Jordan bracket $\{a, b\} = ab + ba$, which gives Jordan algebras instead. Geometrically, antisymmetry comes from the fact that the commutator $ab - ba$ measures non-commutativity, and is antisymmetric in $a$ and $b$ by construction. **What breaks if we drop it?** A bilinear operation without antisymmetry could have non-trivial symmetric part — i.e., contain information not captured by commutativity failure — and there is no group-theoretic shadow of this. Antisymmetry is the algebraic shadow of the geometric fact that $C_{g_1 g_2} \circ C_{g_1 g_2}^{-1}$ is the identity.

Why **Jacobi**? The Jacobi identity is the substitute for associativity. The bracket is **not** associative: $[X, [Y, Z]]$ is not in general equal to $[[X, Y], Z]$. The "obstruction" to associativity, $[X, [Y, Z]] - [[X, Y], Z]$, is by antisymmetry equal to $[X, [Y, Z]] + [Z, [X, Y]]$, and the Jacobi identity says this equals $-[Y, [Z, X]]$, an expression that involves only nested brackets. So the Jacobi identity is the *one* non-associativity constraint that a bracket must satisfy to be a Lie bracket. **What breaks if we drop Jacobi?** The adjoint map $\mathrm{ad}_X : \mathfrak{g} \to \mathfrak{g}$, $\mathrm{ad}_X(Y) = [X, Y]$, would no longer be a derivation of the bracket: the formula $\mathrm{ad}_X[Y, Z] = [\mathrm{ad}_X Y, Z] + [Y, \mathrm{ad}_X Z]$ — which is the Jacobi identity in rewritten form — would fail. Without this, the adjoint representation is not a Lie algebra representation, the Killing form is ill-defined, and the entire structural theory collapses. So Jacobi is not a technicality; it is essential to the theory.

Why **bilinearity over $\mathbb{R}$ rather than over $\mathbb{Q}$, $\mathbb{C}$, or a general field**? A real Lie algebra is the natural object when studying real Lie groups, because the tangent space $T_e G$ is a real vector space. **Complex Lie algebras** $(\mathfrak{g}, [\cdot, \cdot])_\mathbb{C}$ arise from complex Lie groups (groups that are complex manifolds with holomorphic multiplication), and over $\mathbb{C}$ the classification is cleaner — the Cartan–Killing classification of simple complex Lie algebras gives the famous $A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2$ list. Real Lie algebras are obtained from complex ones by choosing a real form (a Galois descent), and the classification of real Lie algebras has more cases (compact, split, etc.) corresponding to different real forms of the same complex algebra. We work over $\mathbb{R}$ in this chapter, with the understanding that complexification $\mathfrak{g}_\mathbb{C} = \mathfrak{g} \otimes_\mathbb{R} \mathbb{C}$ is the standard way to access the cleaner complex classification.

What about **finite-dimensional vs infinite-dimensional**? Most of Lie group theory is developed for finite-dimensional Lie algebras, because these correspond to finite-dimensional Lie groups (Lee Thm 8.37: $\dim \mathfrak{g} = \dim G$ for a Lie group $G$). Infinite-dimensional Lie algebras — Kac–Moody algebras, the Virasoro algebra, Lie algebras of vector fields on a manifold $\mathfrak{X}(M)$, the algebra of derivations of a function algebra — exist and are very important in mathematical physics (the Virasoro algebra is central to conformal field theory and string theory), but they require additional structure (a topology, a grading, completeness conditions) to be tractable. Our default is finite-dimensional.

The summary: the three axioms — bilinearity, antisymmetry, Jacobi — capture exactly the algebraic structure of "commutator on an associative algebra" or equivalently "Lie bracket of left-invariant vector fields on a Lie group", and they are the minimum needed for the structural theory (adjoint representation, classification, Killing form) to function.

---

# The Definition

A **Lie algebra** over $\mathbb{R}$ is a pair $(\mathfrak{g}, [\cdot, \cdot])$ where $\mathfrak{g}$ is a real [[Def - Vector Space|vector space]] and $[\cdot, \cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ is a map (the **bracket** or **Lie bracket**) satisfying, for all $X, Y, Z \in \mathfrak{g}$ and $a, b \in \mathbb{R}$:

1. **Bilinearity.** $[aX + bY, Z] = a[X, Z] + b[Y, Z]$ and $[Z, aX + bY] = a[Z, X] + b[Z, Y]$.
2. **Antisymmetry.** $[X, Y] = -[Y, X]$.
3. **Jacobi identity.** $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$.

The **dimension** of $\mathfrak{g}$ is its dimension as a real vector space. Unless explicitly stated, all Lie algebras in this topic are finite-dimensional.

A Lie algebra $\mathfrak{g}$ is **abelian** if $[X, Y] = 0$ for all $X, Y \in \mathfrak{g}$ — equivalently, every bracket is zero. Examples include $\mathbb{R}^n$ with trivial bracket.

A **Lie subalgebra** $\mathfrak{h} \subseteq \mathfrak{g}$ is a vector subspace closed under the bracket: $[X, Y] \in \mathfrak{h}$ whenever $X, Y \in \mathfrak{h}$. It is itself a Lie algebra under the restricted bracket.

An **ideal** $\mathfrak{h} \subseteq \mathfrak{g}$ is a vector subspace satisfying the stronger condition $[X, Y] \in \mathfrak{h}$ whenever $X \in \mathfrak{g}$ and $Y \in \mathfrak{h}$ (one of the inputs is from $\mathfrak{h}$). Ideals are normal subgroups' algebraic shadow — see [[Thm - The Closed Subgroup Theorem]] and Lee Thm 20.28.

A **Lie algebra homomorphism** $\varphi : \mathfrak{g} \to \mathfrak{h}$ is a linear map preserving the bracket: $\varphi([X, Y]_\mathfrak{g}) = [\varphi(X), \varphi(Y)]_\mathfrak{h}$.

---

# Categorical / Structural Definition

A Lie algebra is, in structural terms, a vector space equipped with a single binary operation satisfying three identities (bilinearity, antisymmetry, Jacobi). It is *not* an associative algebra (it lacks associativity), but it is closely related to associative algebras in two ways.

**Lie algebras from associative algebras (commutator construction).** For any associative algebra $A$ over $\mathbb{R}$, the **commutator** $[a, b] = ab - ba$ defines a Lie algebra structure on $A$, which we denote $A^{\mathrm{Lie}}$. Bilinearity is from bilinearity of the associative product, antisymmetry is immediate from the definition, and the Jacobi identity is a direct calculation expanding all nested commutators. The most important example is $A = \mathrm{End}(V) = \mathfrak{gl}(V)$ for a finite-dimensional vector space $V$, whose Lie algebra under the commutator is $\mathfrak{gl}(V)$, also denoted $\mathfrak{gl}(n, \mathbb{R})$ when $V = \mathbb{R}^n$.

**Associative algebras from Lie algebras (universal enveloping algebra).** The reverse construction is the **universal enveloping algebra** $U(\mathfrak{g})$: the unique associative algebra (with unit) generated by $\mathfrak{g}$ subject to the relations $XY - YX = [X, Y]$ for $X, Y \in \mathfrak{g}$. It satisfies the universal property: every Lie algebra homomorphism $\mathfrak{g} \to A^{\mathrm{Lie}}$ (where $A$ is an associative algebra) factors uniquely through $U(\mathfrak{g})$. So $\mathfrak{g} \mapsto U(\mathfrak{g})$ is left adjoint to the forgetful functor $A \mapsto A^{\mathrm{Lie}}$ from associative algebras to Lie algebras. The Poincaré–Birkhoff–Witt theorem gives an explicit basis for $U(\mathfrak{g})$ as a vector space, and Lie algebra representations are exactly modules over $U(\mathfrak{g})$.

**The category of Lie algebras.** Lie algebras and Lie algebra homomorphisms form a category $\mathbf{LieAlg}$. It has finite products (direct sum of vector spaces with the obvious bracket), and the Lie functor $\mathrm{Lie} : \mathbf{LieGrp} \to \mathbf{LieAlg}$ from [[Def - Lie Group|Lie groups]] is — restricted to simply connected Lie groups — an equivalence of categories with the subcategory $\mathbf{LieAlg}_{\mathrm{fin}}$ of finite-dimensional Lie algebras (Lee Problem 20-18).

---

# Relate to Other Fields / Compression

A Lie algebra is **a vector space with a bilinear bracket that is antisymmetric and satisfies the Jacobi identity**. It is the linearization of a Lie group at the identity, equivalently the commutator algebra of an associative algebra, equivalently the algebra of derivations of a smooth function algebra (in the case $\mathfrak{X}(M)$), equivalently the algebra of left-invariant vector fields on a Lie group.

From the [[Def - Vector Space|vector-space side]], a Lie algebra is just a vector space with one extra piece of multilinear data — a bilinear map $\mathfrak{g} \otimes \mathfrak{g} \to \mathfrak{g}$ satisfying antisymmetry and Jacobi. From the [[Def - Lie Group|Lie-group side]], it is the tangent space at the identity, equipped with the bracket induced by left-invariant vector fields.

**True name:** A Lie algebra is **the commutator algebra of a Lie group, captured at the level of tangent vectors**. By the Baker–Campbell–Hausdorff formula, the bracket $[X, Y]$ is precisely the leading non-trivial term in $\log(\exp X \exp Y) - X - Y = \tfrac{1}{2}[X, Y] + \cdots$. So the operational meaning of the bracket is: it is the obstruction to the exponential map being a group homomorphism. In an abelian Lie group all brackets are zero and $\exp(X + Y) = \exp X \exp Y$; in a non-abelian Lie group the bracket measures the failure.

---

# Examples / Corollaries

**Is an instance: $\mathfrak{gl}(n, \mathbb{R})$.** The vector space $M(n, \mathbb{R})$ of $n \times n$ real matrices, with bracket the commutator $[A, B] = AB - BA$. Bilinearity is obvious. Antisymmetry: $[A, B] = AB - BA = -(BA - AB) = -[B, A]$. Jacobi: direct calculation, expanding $[A, [B, C]] = ABC - ACB - BCA + CBA$ and summing the three cyclic permutations gives zero. Dimension: $n^2$. This is the Lie algebra of $\mathrm{GL}(n, \mathbb{R})$.

**Is an instance: $\mathfrak{sl}(n, \mathbb{R})$.** The Lie subalgebra of $\mathfrak{gl}(n)$ consisting of traceless matrices, $\{A : \mathrm{tr} A = 0\}$. Closed under the commutator because $\mathrm{tr}[A, B] = \mathrm{tr}(AB - BA) = \mathrm{tr}(AB) - \mathrm{tr}(BA) = 0$ — the trace of a commutator is always zero. Dimension: $n^2 - 1$. Lie algebra of $\mathrm{SL}(n, \mathbb{R})$.

**Is an instance: $\mathfrak{so}(n)$.** The Lie subalgebra of $\mathfrak{gl}(n)$ consisting of antisymmetric matrices, $\{A : A^T = -A\}$. Closed under the commutator because $[A, B]^T = (AB - BA)^T = B^T A^T - A^T B^T = (-B)(-A) - (-A)(-B) = BA - AB = -[A, B]$. Dimension $\binom{n}{2}$. Lie algebra of $\mathrm{SO}(n)$ (and of $\mathrm{O}(n)$ — they have the same Lie algebra because they share the identity component).

**Is an instance: $\mathfrak{su}(2)$.** The Lie algebra of traceless skew-Hermitian $2 \times 2$ matrices, $\{A : A^* = -A, \mathrm{tr} A = 0\}$. Dimension $3$ as a real vector space; canonical basis is $\{i\sigma_1/2, i\sigma_2/2, i\sigma_3/2\}$ where $\sigma_j$ are Pauli matrices, with brackets $[i\sigma_a/2, i\sigma_b/2] = -\epsilon_{abc} (i\sigma_c/2)$ — up to sign, the angular momentum commutation relations of quantum mechanics. Isomorphic to $\mathfrak{so}(3)$ as Lie algebras.

**Is an instance: any vector space with trivial bracket.** $(V, [\cdot, \cdot]_0)$ with $[X, Y]_0 = 0$ for all $X, Y$ is an **abelian Lie algebra**. The axioms are trivially satisfied. Every abelian Lie algebra arises this way; up to isomorphism, abelian Lie algebras are classified by dimension. The Lie algebra of $\mathbb{R}^n$ and of $T^n$ are abelian.

**Is an instance: $\mathfrak{X}(M)$.** The space of smooth vector fields on a smooth manifold $M$, with the [[Def - The Lie Bracket of Vector Fields|Lie bracket of vector fields]] $[X, Y] f = X(Yf) - Y(Xf)$. This is an infinite-dimensional Lie algebra (for $\dim M \geq 1$), and on a Lie group $G$ the left-invariant vector fields form a finite-dimensional Lie subalgebra equal to $\mathrm{Lie}(G)$.

**Is an instance: the Heisenberg Lie algebra $\mathfrak{h}_3$.** The $3$-dimensional Lie algebra with basis $X, Y, Z$ and brackets $[X, Y] = Z$, $[X, Z] = 0$, $[Y, Z] = 0$. Non-abelian, nilpotent (the bracket of three elements always vanishes). Lie algebra of the [[Def - Lie Group|Heisenberg group]] $\mathrm{Heis}(3)$.

**Is NOT an instance: a vector space with a symmetric bracket.** If $[X, Y] = [Y, X]$ for all $X, Y$ — symmetric instead of antisymmetric — then setting $X = Y$ gives $[X, X] = [X, X]$ (trivially), but combined with antisymmetry (which symmetric brackets fail) we cannot conclude $[X, X] = 0$. A symmetric bilinear operation does not in general satisfy any Jacobi-like identity, and gives **Jordan algebras** rather than Lie algebras. The space $\{A \in M(n) : A^T = A\}$ of symmetric matrices with the **anticommutator** $\{A, B\} = AB + BA$ is a Jordan algebra, not a Lie algebra.

**Is NOT an instance: the cross product on $\mathbb{R}^n$ for $n \neq 3, 7$.** The cross product $\mathbb{R}^3 \times \mathbb{R}^3 \to \mathbb{R}^3$ given by $(v \times w)_i = \epsilon_{ijk} v_j w_k$ is bilinear, antisymmetric, and satisfies the Jacobi identity — it is therefore a Lie algebra, isomorphic to $\mathfrak{so}(3)$. The cross product on $\mathbb{R}^7$ (from the octonions) is bilinear and antisymmetric but **fails the Jacobi identity**, so it does *not* give $\mathbb{R}^7$ a Lie algebra structure. (It gives a "Malcev algebra".) For other $n$ there is no non-trivial bilinear antisymmetric product, by Hurwitz's theorem and friends.

**Corollary ($[X, X] = 0$).** Antisymmetry gives $[X, X] = -[X, X]$, hence $2[X, X] = 0$, hence $[X, X] = 0$ over any field of characteristic $\neq 2$. (Over characteristic $2$ this is taken as an additional axiom, since antisymmetry $[X, Y] = -[Y, X]$ does not imply $[X, X] = 0$ there.)

**Corollary ($\mathrm{ad}$ is a Lie algebra homomorphism).** The adjoint map $\mathrm{ad}_X : \mathfrak{g} \to \mathfrak{g}$, $\mathrm{ad}_X(Y) = [X, Y]$, is a derivation of the bracket: $\mathrm{ad}_X[Y, Z] = [\mathrm{ad}_X Y, Z] + [Y, \mathrm{ad}_X Z]$. The Jacobi identity is exactly this derivation property. Consequently $\mathrm{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ is a Lie algebra homomorphism, the **adjoint representation** — see [[Def - Adjoint Representation]].

**Corollary (trace of a commutator).** For matrices, $\mathrm{tr}[A, B] = \mathrm{tr}(AB - BA) = 0$. So the trace is invariant under commutators, and $\mathfrak{sl}(n) = \{A : \mathrm{tr} A = 0\}$ is an ideal in $\mathfrak{gl}(n)$ (in fact a Lie subalgebra closed under bracket with arbitrary $\mathfrak{gl}(n)$ elements, since adding a scalar matrix to either side does not change the commutator).

**Calibration check.** If you can (i) verify the Jacobi identity for the matrix commutator by direct expansion; (ii) show $\mathfrak{so}(n)$ is closed under the commutator; (iii) compute $\dim \mathfrak{su}(2) = 3$ and identify the standard basis; and (iv) explain why $[X, X] = 0$ over characteristic $\neq 2$ — you have understood the definition correctly.

---

# Unlocked by This

> [!tip] Universal Enveloping Algebra *(from Representation Theory)*
> The **universal enveloping algebra** $U(\mathfrak{g})$ is the associative algebra freely generated by $\mathfrak{g}$ subject to the relations $XY - YX = [X, Y]$. It satisfies the universal property that every Lie algebra homomorphism $\mathfrak{g} \to A^{\mathrm{Lie}}$ extends uniquely to an associative algebra homomorphism $U(\mathfrak{g}) \to A$. The **Poincaré–Birkhoff–Witt theorem** gives a vector space basis. Representations of $\mathfrak{g}$ are exactly $U(\mathfrak{g})$-modules.

> [!tip] Killing Form *(from Lie Algebra Theory)*
> Every Lie algebra has a canonical symmetric bilinear form, the **Killing form** $B(X, Y) = \mathrm{tr}(\mathrm{ad}_X \mathrm{ad}_Y)$. **Cartan's criterion** characterizes semisimple Lie algebras as those with non-degenerate Killing form, and the signature distinguishes compact from non-compact real forms. On compact semisimple Lie groups, the Killing form integrates to a bi-invariant Riemannian metric.

> [!tip] Classification of Simple Lie Algebras *(from Lie Algebra Theory, Advanced)*
> Over $\mathbb{C}$, the **simple Lie algebras** are classified by their root systems via the Cartan–Killing classification, yielding the four infinite families $A_n = \mathfrak{sl}(n+1, \mathbb{C})$, $B_n = \mathfrak{so}(2n+1, \mathbb{C})$, $C_n = \mathfrak{sp}(2n, \mathbb{C})$, $D_n = \mathfrak{so}(2n, \mathbb{C})$, and five exceptional algebras $E_6, E_7, E_8, F_4, G_2$. Over $\mathbb{R}$, each complex simple Lie algebra has several real forms (compact, split, intermediate), and the real classification is correspondingly richer.

> [!tip] Lie Algebra Cohomology *(from Algebraic Topology and Representation Theory)*
> The **Chevalley–Eilenberg complex** $\Lambda^* \mathfrak{g}^*$ with differential $d\omega(X_0, \ldots, X_k) = \sum_{i < j} (-1)^{i + j} \omega([X_i, X_j], X_0, \ldots, \widehat{X_i}, \ldots, \widehat{X_j}, \ldots, X_k)$ computes the cohomology of the Lie algebra $\mathfrak{g}$. For the Lie algebra of a compact Lie group $G$, this cohomology coincides with the de Rham cohomology of $G$: $H^*(\mathfrak{g}; \mathbb{R}) \cong H^*_{\mathrm{dR}}(G)$.

---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
tags: [algebra, linear-algebra]
---

# Notation

For subspaces $V_1, \dots, V_m$ of a vector space $V$, the **sum** is denoted $V_1 + \dots + V_m$ — read out loud as "$V_1$ plus $V_2$ plus ... plus $V_m$". When two subspaces are at stake the notation is $U + W$. The intersection is $V_1 \cap \dots \cap V_m$, with $\bigcap$ for arbitrary collections. The union is $V_1 \cup \dots \cup V_m$, but the union of subspaces is almost never itself a subspace — see [[Ex - Union of subspaces is a subspace iff one contains the other]] — which is the structural reason sums are the right object to study. See [[Linear Algebra I — §1 Vector Spaces]] for the full notation registry.

---

# Axiom Motivation

The thing we are trying to axiomatize is **the smallest subspace containing several given subspaces**. The natural set-theoretic operation here would be the union $V_1 \cup \dots \cup V_m$ — for an ordinary set, the union is the smallest set containing the pieces. But the union of subspaces fails to be a subspace in almost every interesting case. Take $V_1$ = $x$-axis and $V_2$ = $y$-axis in $\mathbb{R}^2$: each is a subspace, $V_1 \cup V_2$ is the union of the two axes, but $(1, 0) + (0, 1) = (1, 1)$ is not in either axis. So we cannot use the union as the join in the lattice of subspaces; we need something larger.

What is the smallest *subspace* containing $V_1 \cup \dots \cup V_m$? Any subspace $W$ containing all the $V_k$ must, by closure under addition, contain every expression $v_1 + \dots + v_m$ with $v_k \in V_k$. Conversely, the set of all such expressions is closed under addition and scalar multiplication, contains $0$ (take every $v_k = 0$), and contains each $V_k$ (take all but one of the $v_j$ to be zero). So this set already is a subspace, it contains the union, and it is contained in every subspace containing the union. It is the smallest, by construction. This is the **sum** $V_1 + \dots + V_m$. The motivation is therefore not arbitrary: it is the **join in the subspace lattice**, the natural counterpart to the meet (intersection).

The analogy with sets is instructive but mildly misleading. For ordinary subsets of a set $X$ the lattice operations are union (join) and intersection (meet); for subspaces the meet is still intersection but the join is *not* union — it is sum. The reason is that the union operation, when applied to two subspaces, fails to be closed under the very operation (addition) that defines a subspace. The "sum" repairs this by including all such sums explicitly. So the slogan is: **union is to sets as sum is to subspaces**.

Why define the sum as the set of *sums* $v_1 + \dots + v_m$ and not, say, the span of the union? Both definitions give the same answer — the span of $V_1 \cup \dots \cup V_m$ equals $V_1 + \dots + V_m$ — but the sum-formula is more concrete and computationally useful. Every element of the sum is realized by a particular choice of pieces $v_k \in V_k$, and many proofs involve choosing such a representation and manipulating it. The span formulation would require one to pick a generating set first, then form a generic linear combination, which is two layers of abstraction over the same construction.

Why does the sum have a special notation $+$ — why not $\vee$ or $\sqcup$ or anything else? Because the sum is, literally, the *image of the addition map* $V_1 \times \dots \times V_m \to V$, $(v_1, \dots, v_m) \mapsto v_1 + \dots + v_m$. The notation reflects the fact that the operation is built out of the vector-space addition; it is the same plus sign promoted from elements to subspaces. The product symbol $V_1 \times V_2$ already denotes the external direct product (see [[Linear Algebra IV — §3E–F Products, Quotients, Duality]] for the product of vector spaces), so the choice $V_1 + V_2$ for the internal sum is consistent: $+$ for internal sums of subspaces, $\times$ for external products.

When the sum has the extra property that every element has a **unique** representation as $v_1 + \dots + v_m$, the sum is called a **direct sum** and written $V_1 \oplus \dots \oplus V_m$ — see [[Def - Direct Sum]]. The direct sum is the strongest form of "sum"; an ordinary sum allows multiple representations of the same element, which means information about the decomposition is lost. The chapter's central goal is to characterize when a sum is direct, which is the content of [[Thm - Conditions for a Direct Sum]].

---

# The Definition

Let $V_1, \dots, V_m$ be [[Def - Subspace|subspaces]] of a vector space $V$. The **sum** of $V_1, \dots, V_m$ is the set

$$V_1 + \dots + V_m = \{v_1 + \dots + v_m : v_1 \in V_1, \dots, v_m \in V_m\}.$$

For two subspaces, $U + W = \{u + w : u \in U, w \in W\}$. The sum of zero subspaces is the trivial subspace $\{0\}$ (the empty sum is, as usual, $0$).

The sum $V_1 + \dots + V_m$ is itself a subspace of $V$ — see [[Ex - Sum of two subspaces is the smallest containing both]] — and is the smallest subspace of $V$ containing $V_1, \dots, V_m$.

---

# Categorical / Structural Definition

The sum of subspaces is the **join in the lattice of subspaces** of $V$. The collection $\operatorname{Sub}(V)$ of all subspaces of $V$, ordered by inclusion, is a complete lattice:

- **Meet** of $\{V_\alpha\}$: the intersection $\bigcap_\alpha V_\alpha$, which is a subspace.
- **Join** of $\{V_\alpha\}$: the sum $\sum_\alpha V_\alpha = \{v_{\alpha_1} + \dots + v_{\alpha_k} : k \geq 0, \alpha_i \text{ indices}, v_{\alpha_i} \in V_{\alpha_i}\}$, which is the smallest subspace containing all $V_\alpha$.

This lattice is **modular** (the *modular law*: if $V_1 \subseteq V_3$ then $(V_1 + V_2) \cap V_3 = V_1 + (V_2 \cap V_3)$), but not generally **distributive** — the operations $+$ and $\cap$ do not distribute over each other in the way $\cup$ and $\cap$ do for sets. The failure of distributivity is the reason direct-sum decompositions are not unique even when they exist (see [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]).

The sum has a **universal property** with respect to the inclusions $V_k \hookrightarrow V$: it is the *pushout* in the lattice — the smallest subspace through which every $V_k$ factors. Externally, the analogous construction is the [[Linear Algebra IV — §3E–F Products, Quotients, Duality|coproduct]] in $\mathbf{Vect}_{\mathbb{F}}$, namely the direct sum $V_1 \oplus \dots \oplus V_m$ of separate vector spaces. The internal sum of subspaces is the *image* of the natural map from the external coproduct into $V$.

---

# Relate to Other Fields / Compression

The sum of subspaces is the **subspace generated by the union**, in the same way the subgroup generated by a union of subgroups is the smallest subgroup containing all of them (see [[Def - Subgroup]]). In groups one usually writes $\langle H, K \rangle$ for this; in vector spaces the cleaner notation $H + K$ is available precisely because the algebraic structure is abelian (so every element of the join is already a single sum — no iterated multiplications needed). The same simplification applies to abelian groups: for abelian groups $H + K$ also means $\{h + k : h \in H, k \in K\}$.

In [[Def - Module|module theory]] the sum of submodules is defined identically: $M_1 + \dots + M_m = \{x_1 + \dots + x_m : x_k \in M_k\}$. The construction is one of the basic tools for building new submodules out of given ones, and it is the natural setting for the second isomorphism theorem in module form (which generalizes [[Thm - Second Isomorphism Theorem]] from group theory).

**True name:** the operational true name of the sum of subspaces is "the set of all $v$ you can write as $v_1 + \dots + v_m$ with $v_k \in V_k$". When you reach for the sum in a proof, this is what you actually use — you pick an element of the sum, decompose it into a sum, and manipulate the pieces. The "join in the lattice" framing is conceptual; the "set of all sums" framing is computational.

---

# Examples / Corollaries

**Is an instance: a sum of subspaces of $\mathbb{F}^3$ giving a plane.** Let $U = \{(x, 0, 0) : x \in \mathbb{F}\}$ and $W = \{(0, y, 0) : y \in \mathbb{F}\}$ — the first two coordinate axes in $\mathbb{F}^3$. Then $U + W = \{(x, y, 0) : x, y \in \mathbb{F}\}$, the entire $xy$-plane. Every element of the plane is realized as a sum $(x, 0, 0) + (0, y, 0)$, and conversely every such sum lies in the plane. The picture is that summing two transverse lines through the origin "fills in" the plane between them.

**Is an instance: $\mathcal{P}_m(\mathbb{F}) + \mathcal{P}_n(\mathbb{F}) = \mathcal{P}_{\max(m, n)}(\mathbb{F})$.** The sum of two finite-degree polynomial subspaces is the larger of them, because every polynomial of degree $\leq m$ is the sum of itself and the zero polynomial of degree $\leq n$. This is a degenerate but instructive example: the sum of nested subspaces is the largest one.

**Is an instance (LADR Example 1.38): sum in $\mathbb{F}^4$.** Let $U = \{(x, x, y, y) : x, y \in \mathbb{F}\}$ (vectors whose first two coordinates are equal and whose last two coordinates are equal) and $W = \{(x, x, x, y) : x, y \in \mathbb{F}\}$ (vectors whose first three coordinates are equal). Then $U + W = \{(x, x, y, z) : x, y, z \in \mathbb{F}\}$, the subspace of vectors whose first two coordinates are equal. To verify the inclusion $U + W \subseteq \{(x, x, y, z)\}$: every element of $U + W$ has the form $(a, a, b, b) + (c, c, c, d) = (a + c, a + c, b + c, b + d)$, whose first two coordinates agree. To verify the reverse: $(x, x, y, z) = (x, x, y, y) + (0, 0, 0, z - y)$ with the first term in $U$ and the second in $W$. This is a non-trivial computation that exercises both the "every element of the sum has this form" and "this form is in the sum" directions; the second direction is where the cleverness usually lies.

**Is an instance: the sum is commutative and associative.** $U + W = W + U$ for any subspaces $U, W$ (because vector addition is commutative), and $(V_1 + V_2) + V_3 = V_1 + (V_2 + V_3)$ for any three subspaces. So sums of subspaces enjoy the same arithmetic as ordinary sums. The proof is one line in each case: $\{u + w : u \in U, w \in W\} = \{w + u : w \in W, u \in U\}$ by commutativity in $V$.

**Is NOT an instance: the union of two subspaces is not generally a sum.** $V_1 \cup V_2$ is, in general, smaller than $V_1 + V_2$. For instance with $V_1$ = $x$-axis and $V_2$ = $y$-axis in $\mathbb{R}^2$: the union is the union of two axes (everything with $x = 0$ or $y = 0$), but the sum is all of $\mathbb{R}^2$. The union equals the sum if and only if one of the subspaces contains the other (see [[Ex - Union of subspaces is a subspace iff one contains the other]]), which is the precise sense in which "union is the wrong join in the subspace lattice".

**Corollary (the sum is a subspace).** $V_1 + \dots + V_m$ is a subspace of $V$. Containment of zero: $0 = 0 + 0 + \dots + 0$ with each summand in $V_k$. Closure under addition: $(v_1 + \dots + v_m) + (v_1' + \dots + v_m') = (v_1 + v_1') + \dots + (v_m + v_m')$, with each $v_k + v_k' \in V_k$. Closure under scalar multiplication: $\lambda (v_1 + \dots + v_m) = \lambda v_1 + \dots + \lambda v_m$, with each $\lambda v_k \in V_k$. So the sum is closed under linear combinations and is therefore a subspace.

**Corollary (the sum is the smallest containing subspace).** Every subspace $W$ containing $V_1 \cup \dots \cup V_m$ contains $V_1 + \dots + V_m$. Proof: if $W$ contains each $V_k$, then by closure under addition $W$ contains every sum $v_1 + \dots + v_m$ with $v_k \in V_k$. So $W \supseteq V_1 + \dots + V_m$. Combined with the fact that the sum itself is a subspace containing each $V_k$, this proves the sum is the smallest such subspace — see [[Ex - Sum of two subspaces is the smallest containing both]] for the worked argument.

**Corollary ($V_1 + V_2 + V_3 = V_1 + (V_2 + V_3)$).** Associativity holds because $(v_1 + v_2) + v_3 = v_1 + (v_2 + v_3)$ in $V$. The sum of subspaces inherits its arithmetic from $V$. Iterating, the sum $V_1 + \dots + V_m$ does not depend on a bracketing — exactly as for ordinary numerical or vector sums.

**Corollary (the sum can be much larger than the union).** If $V_1, V_2$ are subspaces with $V_1 \not\subseteq V_2$ and $V_2 \not\subseteq V_1$, then $V_1 + V_2$ contains $V_1$, $V_2$, and elements not in either. Explicitly, $V_1 \cup V_2 \subsetneq V_1 + V_2$. The strict inclusion is what makes the sum the right operation: it actively *expands* the structure to enclose the union inside a subspace.

**Calibration check.** If you have understood the definition you should be able to (i) compute $U + W$ in $\mathbb{R}^3$ when $U = \operatorname{span}((1, 0, 0))$ and $W = \operatorname{span}((1, 1, 0))$, getting the $xy$-plane; (ii) explain in one sentence why $U + U = U$ for any subspace $U$ (because every $u \in U$ is $u + 0$ with both summands in $U$, and conversely $u + u' \in U$ by closure); (iii) decide whether the sum of three lines in $\mathbb{R}^3$ is always $\mathbb{R}^3$ (no — if the three lines are coplanar, the sum is the plane they span; only if they span $\mathbb{R}^3$, equivalently are linearly independent, does the sum equal $\mathbb{R}^3$).

---

# Unlocked by This

> [!tip] Direct Sum *(from Linear Algebra I)*
> A sum $V_1 + \dots + V_m$ is called a **direct sum** $V_1 \oplus \dots \oplus V_m$ when every element of the sum has a **unique** expression as $v_1 + \dots + v_m$. The direct sum is the cleanest form of decomposition and is the setting in which dimensions add: $\dim(V_1 \oplus \dots \oplus V_m) = \dim V_1 + \dots + \dim V_m$. See [[Def - Direct Sum]] and [[Thm - Conditions for a Direct Sum]].

> [!tip] Quotient Space and Affine Subset *(from Linear Algebra IV)*
> The cosets $v + U$ of a subspace $U$ are translates of $U$ — themselves affine, not linear, subsets of $V$. The set of all cosets, $V/U$, is again a vector space, and the natural map $V \to V/U$ is a surjective linear map with kernel $U$. The quotient is the cleanest setting in which to study "the structure left over after collapsing $U$ to a point". See [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

> [!tip] Dimension Formula for Sums *(from Linear Algebra II)*
> For finite-dimensional subspaces $U, W$ of a vector space, $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$. This is the linear-algebraic analogue of the inclusion-exclusion formula for finite sets, and it specializes to $\dim(U \oplus W) = \dim U + \dim W$ precisely when $U \cap W = \{0\}$. See [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

> [!tip] Internal Sum of Submodules *(from Module Theory)*
> The sum of submodules of a module is defined identically to the sum of subspaces, with the same lattice properties. In module theory the failure of unique decomposition becomes more dramatic, and the concept of a **direct summand** — a submodule for which the inclusion has a left inverse — becomes a strict refinement of "summand in a direct sum". This is intimately related to the **projective module** condition. See [[Def - Submodule]].

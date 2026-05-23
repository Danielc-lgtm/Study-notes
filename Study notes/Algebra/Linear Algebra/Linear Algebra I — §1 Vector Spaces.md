---
type: topic
subject: linear-algebra
chapter: "1"
title: "Linear Algebra I — §1 Vector Spaces"
tags: [algebra, linear-algebra]
---

# Notation Registry

A standing-convention preamble: throughout this topic, $\mathbb{F}$ denotes either $\mathbb{R}$ or $\mathbb{C}$, following Axler's convention. Almost every result holds verbatim over any field — the inner-product chapters being the chief exceptions — and the reader who is comfortable doing so may take $\mathbb{F}$ to be an arbitrary field throughout. Vectors are abstract elements of the space $V$; their representations as coordinate tuples in $\mathbb{F}^n$ are basis-dependent and should be treated as a *viewing*, not the vector itself.

- $\mathbb{F}$ — a field; $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$ unless stated otherwise.
- $\mathbb{F}^n$ — the set $\{(x_1, \ldots, x_n) : x_i \in \mathbb{F}\}$ of $n$-tuples; the standard finite-dimensional vector space.
- $\mathbb{F}^\infty$ — the set of all sequences $(x_1, x_2, \ldots)$ with $x_i \in \mathbb{F}$.
- $\mathbb{F}^S$ — the set of functions $S \to \mathbb{F}$ for a set $S$; a vector space under pointwise operations.
- $\mathcal{P}(\mathbb{F})$ — the polynomials in one indeterminate with coefficients in $\mathbb{F}$; a subspace of $\mathbb{F}^\mathbb{F}$. The subspace $\mathcal{P}_m(\mathbb{F})$ is the polynomials of degree at most $m$.
- $V, W, U$ — vector spaces over $\mathbb{F}$; subspaces are written as $U, W, V_1, V_2, \ldots$.
- $0$ — the additive identity in $V$ (the zero vector); the same symbol $0$ denotes the scalar zero in $\mathbb{F}$, with context distinguishing.
- $-v$ — the additive inverse of $v \in V$, equal to $(-1) v$.
- $v + w$ — vector addition.
- $\lambda v$ — scalar multiplication, with the dot suppressed.
- $V_1 + V_2 + \cdots + V_m$ — the sum of subspaces, $\{v_1 + \cdots + v_m : v_k \in V_k\}$.
- $V_1 \oplus V_2 \oplus \cdots \oplus V_m$ — a direct sum: a sum in which every element has a unique decomposition.
- $\operatorname{Sub}(V)$ — the lattice of subspaces of $V$, ordered by inclusion.

---

# Motivation

A vector space is the algebraic backbone of every linear theory. Whenever you have a collection of objects you can add together, scale by numbers from a field, and ask "what does a linear combination of these look like", you have a vector space — and any theorem proved from the axioms applies to all of them at once. The plane $\mathbb{R}^2$, ordinary space $\mathbb{R}^3$, the spaces of solutions of homogeneous linear differential equations, the spaces of polynomials of bounded degree, the spaces of functions on a set, the spaces of signed measures, and the tangent spaces of a smooth manifold — these look like very different kinds of object, but the axioms in [[Def - Vector Space]] capture exactly what they share.

This first topic does three things. First, it gives the definition of a field — the scalar set $\mathbb{F}$ on which everything else is built — and the [[Def - Vector Space|definition of a vector space]] over $\mathbb{F}$. Second, it lays down the elementary corollaries that follow from the axioms — that the zero vector is unique, that additive inverses are unique, that $0 \cdot v = 0$ and $(-1) v = -v$ — packaged in [[Thm - Uniqueness of Additive Identity and Inverses]]. Third, and most substantively, it introduces the *substructures* of a vector space: [[Def - Subspace|subspaces]], sums of [[Def - Subspace|subspaces]], and direct sums. The chapter ends with the central operational fact, [[Thm - Direct Sum of Two Subspaces]]: two subspaces have a direct sum if and only if their intersection is trivial.

The unifying frame for the chapter — and indeed for all of linear algebra — is **a vector is a platonic object; its representation under a basis is one particular viewing**. The notation $\mathbb{F}^n$ encourages thinking of a vector as a tuple of numbers, but this confuses the vector with one of its coordinatizations. A genuine understanding of linear algebra requires treating the vector as an element of the abstract space $V$, independent of any basis, and treating tuples in $\mathbb{F}^n$ as the basis-dependent shadow. Different bases produce different tuples for the same vector, related by the [[Linear Algebra III — §3A–D Linear Maps|change-of-basis formula]]. Almost every conceptual difficulty in linear algebra — and most of its surprises — stem from confusing the vector with one of its representations. The structural backbone of the whole subject can be stated as:

$$\text{vector} \;\xleftrightarrow{\text{choose basis}}\; \text{coordinate tuple in } \mathbb{F}^n.$$

The arrow is **not** an equality; it is a chart, a particular way of viewing the abstract vector through a choice of basis. The "vectors first, basis later" philosophy of Axler's text (in contrast to determinant-and-matrix-first treatments) is built precisely to keep this distinction visible.

The reader is assumed to have refreshed: basic [[Def - Group|group theory]] (especially [[Def - Abelian Group|abelian groups]]; the additive structure of a vector space is one), enough [[Def - Ring|ring theory]] to know what a field is (in particular $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_p$), and elementary set theory (functions, intersections, unions, lattice of subsets). No analysis is required for this topic; the function-space examples are used algebraically, not analytically.

---

# Concept Map

## §1A The Spaces $F^n$

LADR §1A is the warm-up section: complex numbers as the field $\mathbb{C}$, the space $\mathbb{F}^n$ of $n$-tuples, and the digression on fields naming the abstract structure on $\mathbb{F}$ that the rest of the chapter rests on.

- **[[Def - Field]]**
	- A **field** is a set $\mathbb{F}$ with two operations $+$ and $\cdot$, additive and multiplicative identities $0 \neq 1$, additive inverses for every element, and multiplicative inverses for every nonzero element, satisfying commutativity, associativity, and distributivity. Equivalently, it is a commutative [[Def - Ring|ring]] with $1$ in which every nonzero element is invertible. The prototype examples are $\mathbb{Q}, \mathbb{R}, \mathbb{C}$ (all of characteristic $0$) and the finite fields $\mathbb{F}_p$ for prime $p$. The single most consequential axiom is multiplicative inverses for all nonzero elements; without it (i.e. over a [[Def - Ring|ring]]), linear algebra becomes [[Def - Module|module theory]] and loses several clean theorems (bases, dimension).

- $\mathbb{F}^n$ — the space of $n$-tuples — as the prototype vector space, with operations $(x_1, \dots, x_n) + (y_1, \dots, y_n) = (x_1 + y_1, \dots, x_n + y_n)$ and $\lambda (x_1, \dots, x_n) = (\lambda x_1, \dots, \lambda x_n)$. Every axiom of an abstract vector space is verified pointwise in $\mathbb{F}$, by the field axioms.

> [!tip] Unlocked: [[Def - Vector Space|Vector Space]] Itself *(from Linear Algebra)*
> The next section §1B abstracts the operations and properties of $\mathbb{F}^n$ into the general notion of a [[Def - Vector Space|vector space]]. The motivation for that abstraction is precisely that the operations and axioms verified for $\mathbb{F}^n$ apply to many other objects (function spaces, polynomial spaces, solution spaces of linear equations).

> [!tip] Unlocked: Algebraic Closure and the [[Thm - Fundamental Theorem of Algebra|Fundamental Theorem of Algebra]] *(from Algebra)*
> $\mathbb{C}$ is the **algebraic closure** of $\mathbb{R}$: every non-constant polynomial in $\mathbb{C}[x]$ has a root. This is the property that delivers the existence of eigenvalues for complex operators (see [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]]) and the cleanest version of the spectral theorem. Real operators do not generally have real eigenvalues; complex operators always do.

> [!tip] Unlocked: Finite Fields and Coding Theory *(from Number Theory and Computer Science)*
> The finite fields $\mathbb{F}_q$ with $q = p^n$ elements are the alphabets of error-correcting codes (Reed-Solomon, BCH), the supports of cryptographic schemes, and the algebraic ground of finite geometry. The linear-algebra theory developed in this chapter — and every chapter after — applies to vector spaces over $\mathbb{F}_q$ with only the inner-product chapters requiring an ordered or complex field.

> [!note] Exercise Index — §1A
> [[Exercise Index - §1A The Spaces Fn]]

## §1B Definition of Vector Space

LADR §1B states the abstract definition of a vector space, derives the elementary corollaries (uniqueness of zero, uniqueness of inverses, $0 \cdot v = 0$, $(-1) v = -v$), and presents the canonical infinite-dimensional examples $\mathbb{F}^\infty$ and $\mathbb{F}^S$.

- **[[Def - Vector Space]]**
	- A **vector space over $\mathbb{F}$** is a set $V$ with addition $V \times V \to V$ and scalar multiplication $\mathbb{F} \times V \to V$, satisfying eight axioms: commutativity, associativity, and existence of identity and inverses for $+$; the multiplicative-identity rule $1 \cdot v = v$ and the associativity $(ab) v = a(bv)$ of scalar multiplication; and two distributive laws $a(u + v) = au + av$ and $(a + b) v = av + bv$. The axioms naturally [[Def - Group|group]] into "$(V, +, 0)$ is an [[Def - Abelian Group|abelian group]]" and "the scalar action $\mathbb{F} \curvearrowright V$ is linear", joined by distributivity. The motivating examples are $\mathbb{F}^n$, $\mathbb{F}^\infty$, $\mathbb{F}^S$, $\mathcal{P}(\mathbb{F})$, and (over $\mathbb{R}$) the tangent space to a smooth manifold and the space of signed measures.

- **[[Thm - Uniqueness of Additive Identity and Inverses]]**
	- The zero vector is unique, and each $v$ has a unique additive inverse. Both follow from the axioms via short algebraic arguments — uniqueness of zero uses commutativity, uniqueness of inverses uses associativity (load-bearing). The corollaries $0 \cdot v = 0$, $a \cdot 0 = 0$, $(-1) v = -v$ follow from the distributive laws and the corollary $0 \cdot v = 0$. These results license the notation $-v$ and $u - v$, and underpin the [[Def - Subspace|subspace criterion]] (no separate inverse-closure axiom is needed because $(-1) v = -v$).

- The function space $\mathbb{F}^S$ — for any nonempty set $S$, the set of functions $S \to \mathbb{F}$ with pointwise operations is a vector space. Specializing $S = \{1, \dots, n\}$ gives $\mathbb{F}^n$; specializing $S = \mathbb{N}$ gives $\mathbb{F}^\infty$. Many concrete function spaces of analysis (continuous, differentiable, polynomial, $L^p$) are subspaces of $\mathbb{F}^S$.

- [[Ex - F^infinity and F^S as vector spaces]] (⭐) — verifying the function-space construction is a vector space; mechanical but worth doing once.

- [[Ex - Additive inverse axiom replaced by 0v=0]] (⭐⭐) — axiom-trading: the inverse axiom can be replaced by $0 \cdot v = 0$.

- [[Ex - F^infinity is not the union of finite-dimensional subspaces]] (⭐⭐⭐) — the diagonal argument that $\mathbb{F}^\infty$ over an infinite field resists being covered by countably many finite-dimensional subspaces.

> [!tip] Unlocked: [[Def - Module|Module]] *(from Algebra)*
> Replacing the field $\mathbb{F}$ by an arbitrary [[Def - Ring|ring]] $R$ gives a [[Def - Module|module]] over $R$, a strictly more general object whose theory loses several of linear algebra's clean theorems — bases need not exist, dimension is not always well-defined, and not every [[Def - Submodule|submodule]] is a direct summand. This is the systematic generalization developed in [[Def - Module|module theory]]. The features that distinguish vector spaces from [[Def - Module|modules]] (every space has a basis, every short exact sequence splits, every subspace is a direct summand) all come from the field axiom of multiplicative inverses for nonzero elements.

> [!tip] Unlocked: Banach Space and Hilbert Space *(from Functional Analysis)*
> Equipping a vector space with a **norm** $\|\cdot\|$ and requiring completeness produces a **Banach space**; equipping it with an **inner product** $\langle \cdot, \cdot \rangle$ (and requiring completeness) produces a **Hilbert space**. These are the right setting for infinite-dimensional vector spaces in analysis: the function spaces $L^p(\mu)$, the Sobolev spaces $H^k$, the spaces of distributions. The finite-dimensional theory developed in this chapter and the next generalizes to Banach spaces with substantial new content; Hilbert spaces are the closest infinite-dimensional analogue of $\mathbb{R}^n$ with its dot product.

> [!tip] Unlocked: Affine Space *(from Geometry)*
> Forgetting the origin of a vector space gives an **affine space**: a set on which the vector space acts freely and transitively, so that you can take *differences* of points (giving vectors) but not *sums* of points. Affine spaces model "spacetime without a preferred origin" and the configuration spaces of classical mechanics. They reappear in [[Linear Algebra IV — §3E–F Products, Quotients, Duality]] as the affine subsets that are translates of subspaces.

> [!tip] Unlocked: [[Def - The Tangent Space|Tangent Space]] *(from Differential Geometry)*
> At each point of a smooth manifold $M$, the **tangent space** $T_p M$ is a real vector space of dimension $\dim M$. Locally $T_p M \cong \mathbb{R}^n$ via any chart, but the vector space is intrinsic; the tuple of coordinates is the chart-dependent representation. Every theorem of finite-dimensional linear algebra applies pointwise on a smooth manifold, and the resulting machinery — connections, curvature, differential forms — is one of the most consequential applications of linear algebra. See [[Def - The Total Derivative and Differentiability]] for the linear-algebraic content of the multivariate derivative.

> [!note] Exercise Index — §1B
> [[Exercise Index - §1B Vector Spaces]]

## §1C Subspaces and Direct Sums

LADR §1C introduces subspaces (subsets closed under the vector-space operations), sums of subspaces (the lattice-theoretic join), and direct sums (sums with unique decomposition). The two structural results of the section are the [[Thm - Conditions for a Direct Sum|zero-uniqueness criterion]] for direct sums and the [[Thm - Direct Sum of Two Subspaces|trivial-intersection criterion]] for the two-subspace case.

- **[[Def - Subspace]]**
	- A **subspace** of $V$ is a subset $U \subseteq V$ that is itself a vector space under the inherited operations. The **subspace criterion**: $U$ is a subspace if and only if $0 \in U$, $U$ is closed under addition, and $U$ is closed under scalar multiplication. Equivalently, $U$ is non-empty and closed under linear combinations. The closure conditions imply automatically that $U$ is closed under additive inverses (via $-u = (-1) u$). Examples: lines and planes through the origin in $\mathbb{R}^n$, $C[0,1]$ inside $\mathbb{R}^{[0,1]}$, $\mathcal{P}_m(\mathbb{F})$ inside $\mathcal{P}(\mathbb{F})$. Non-examples: lines not through the origin (fail $0 \in U$), the integer lattice $\mathbb{Z}^2 \subset \mathbb{R}^2$ (fails scalar closure), and the union of two coordinate axes (fails addition closure).

- **[[Def - Sum of Subspaces]]**
	- The **sum** $V_1 + \cdots + V_m = \{v_1 + \cdots + v_m : v_k \in V_k\}$ is the smallest subspace of $V$ containing all of $V_1, \ldots, V_m$. It is the lattice-theoretic *join* of the $V_k$ in $\operatorname{Sub}(V)$, and is the structural reason "union of subspaces" is replaced by "sum of subspaces" in linear algebra: the union is rarely a subspace, the sum always is. The notation $+$ reflects that the sum is the *image of the addition map* $V_1 \times \cdots \times V_m \to V$.

- [[Ex - Sum of two subspaces is the smallest containing both]] (⭐) — universal-property characterization of the sum.

- [[Ex - Intersection of subspaces is a subspace]] (⭐) — arbitrary intersection of subspaces is a subspace; closure under intersection is what licenses the "smallest subspace containing $S$" construction (the span).

- [[Ex - Union of subspaces is a subspace iff one contains the other]] (⭐⭐) — the precise characterization of when the union is a subspace; contrapositive argument extracts witnesses.

- [[Ex - Subspaces of F^2 are classified]] (⭐⭐) — every subspace of $\mathbb{F}^2$ is $\{0\}$, a line, or all of $\mathbb{F}^2$; uses the determinant $ad - bc$ as the test for non-parallel vectors.

- **[[Def - Direct Sum]]**
	- A sum $V_1 + \cdots + V_m$ is a **direct sum** $V_1 \oplus \cdots \oplus V_m$ when every element has a **unique** decomposition $v_1 + \cdots + v_m$ with $v_k \in V_k$. Directness lets us define **projections** $\pi_k : V \to V_k$ sending $v$ to its $V_k$-component, and is the structural setting in which [[Def - Dimension|dimensions]] add: $\dim(\bigoplus V_k) = \sum \dim V_k$. Internally, $V = V_1 \oplus V_2$ asserts simultaneously $V_1 + V_2 = V$ and that the addition map $V_1 \times V_2 \to V$ is an isomorphism. The "external" direct sum $V_1 \oplus V_2$ (when $V_1, V_2$ are unrelated vector spaces) is the product $V_1 \times V_2$, made into a vector space coordinate-wise — see [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

- **[[Thm - Conditions for a Direct Sum]]**
	- A sum $V_1 + \cdots + V_m$ is direct if and only if the only way to write $0 = v_1 + \cdots + v_m$ with $v_k \in V_k$ is trivially (each $v_k = 0$). The criterion reduces verification of uniqueness at every element of the sum to verification at the single element $0$. The proof is a subtraction argument: any non-unique decomposition of an arbitrary vector subtracts off to a non-trivial decomposition of $0$. This is the general criterion; for two subspaces it simplifies to [[Thm - Direct Sum of Two Subspaces]].

- **[[Thm - Direct Sum of Two Subspaces]]**
	- For two subspaces, $U + W$ is a direct sum if and only if $U \cap W = \{0\}$. The criterion is geometric: trivial intersection certifies trivial decomposition of zero. The criterion *does not* extend to three or more subspaces — LADR's Example 1.44 displays three subspaces in $\mathbb{F}^3$ with pairwise trivial intersections whose sum is not direct. So for $m \geq 3$ one must use the zero-uniqueness criterion of [[Thm - Conditions for a Direct Sum]]; the pairwise criterion is a strictly weaker condition that suffices only for two summands.

- [[Ex - Even and odd functions form a direct sum decomposition]] (⭐⭐) — $\mathbb{R}^\mathbb{R} = V_e \oplus V_o$, the prototype of "symmetrization decomposes under an involution".

> [!tip] Unlocked: [[Def - Quotient Space|Quotient Space]] *(from Linear Algebra IV)*
> Once you have a subspace $U \subseteq V$, you can form the **quotient space** $V/U$ — the set of affine translates $v + U$, made into a vector space by $(v + U) + (w + U) = (v + w) + U$ and $\lambda (v + U) = (\lambda v) + U$. The natural projection $V \to V/U$ is a surjective linear map with kernel $U$, and the quotient is the cleanest setting for analyzing "the structure left over after collapsing $U$ to a point". The construction parallels [[Def - Quotient Group|quotient groups]] and [[Def - Quotient Ring|quotient rings]], with the same universal property.

> [!tip] Unlocked: Span and [[Def - Linear Independence|Linear Independence]] *(from Linear Algebra II)*
> The intersection of all subspaces containing a set $S$ is itself a subspace, called the **span** of $S$ (and equal to the set of all finite linear combinations of elements of $S$). The span is the smallest subspace containing $S$, and the route from "set of vectors" to "subspace they generate" goes through the lattice operation of intersection. This is the gateway to bases and dimension, the subject of [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

> [!tip] Unlocked: [[Def - Orthogonal Complement|Orthogonal Complement]] and Spectral Decomposition *(from Linear Algebra VI–VII)*
> In an inner-product space, every subspace $U$ admits an **orthogonal complement** $U^\perp$ with $U \cap U^\perp = \{0\}$, hence by [[Thm - Direct Sum of Two Subspaces]] $V = U \oplus U^\perp$. The orthogonal projection $\pi_U$ is the unique linear map that is the identity on $U$ and zero on $U^\perp$. Every self-adjoint operator decomposes $V$ as an orthogonal direct sum of its eigenspaces — the **spectral theorem** — and the entire diagonalization machinery rests on the directness criteria of this chapter.

> [!tip] Unlocked: Eigenspace Decomposition and Diagonalizability *(from Linear Algebra V)*
> An operator $T : V \to V$ is **diagonalizable** if and only if $V$ decomposes as the direct sum of $T$'s eigenspaces, $V = \bigoplus_\lambda \ker(T - \lambda I)$. Directness of this sum follows from [[Thm - Direct Sum of Two Subspaces]] applied pairwise (eigenspaces for distinct eigenvalues have trivial intersection), generalized via [[Thm - Conditions for a Direct Sum]]. So the central question of diagonalizability reduces to the directness criterion of this chapter applied to a specific natural family of subspaces. See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

> [!note] Exercise Index — §1C
> [[Exercise Index - §1C Subspaces and Direct Sums]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises of this section fall into a small number of recurring goals. The most common is **verifying a candidate is a vector space** — checking that a set with given operations satisfies all eight axioms, typically by reducing each axiom to a pointwise or coordinate-wise instance in $\mathbb{F}$. A second is **verifying a candidate is a subspace** — applying the three-condition [[Def - Subspace|subspace criterion]] to a subset of a known vector space. A third is **characterizing operations on subspaces** — showing that sum, intersection, and direct sum behave as expected, building the lattice structure of $\operatorname{Sub}(V)$. A fourth is **certifying directness of a sum** — applying [[Thm - Direct Sum of Two Subspaces]] for two summands or [[Thm - Conditions for a Direct Sum]] for more. A fifth is **classifying low-dimensional subspaces** or otherwise pinning down the structure of a particular vector space (e.g. $\mathbb{F}^2$, $\mathbb{R}^3$). These five — verify vector space, verify subspace, characterize operations, certify directness, classify — recur because each is a way of pinning down a vector space: you understand a vector space when you know its operations, its subspaces, the lattice of subspaces, the available direct-sum decompositions, and (in low dimensions) the classification of all subspaces.

**Sources — what assumptions do we usually leverage?**

The assumptions in these problems are equally stereotyped. **An explicit vector space and concrete subset** is the most common starting point: $\mathbb{F}^n$ with a particular subset defined by a linear equation, or $\mathbb{F}^S$ with a particular property of functions (even, odd, continuous, polynomial). The route is to apply the [[Def - Subspace|subspace criterion]] directly. **Two subspaces of a common ambient space** appear when sums and intersections are the question; the route runs through the lattice operations. **A candidate decomposition $V = U_1 + \cdots + U_m$** appears when directness is at issue; the route is to check the zero-uniqueness condition. **An involution or symmetry on the space** (like $f(x) \mapsto f(-x)$) yields a candidate direct-sum decomposition into $\pm 1$ eigenspaces, with directness coming from trivial intersection. **An infinite-dimensional space with a natural countable filtration** (like $\mathbb{F}^\infty \supset U_n \supset \cdots$) appears in qualifying-exam-style results about non-covering by finite-dimensional subspaces. The recurring move is to route a source to a target: a concrete subset routes through the subspace criterion; two subspaces route through the lattice operations and intersection; an involution routes through symmetrization to a direct-sum decomposition. The [[Linear Algebra I — §1 Vector Spaces#Problem-Solving Strategy|Problem-Solving Strategy]] section makes these routes explicit.

---

# Legal Operations

These are the moves that almost every problem in this topic is assembled from. When stuck, scan the list and try each one. Everything is self-contained.

**Legal operations:**

1. **Verify a candidate vector space by checking the eight axioms pointwise.** For function spaces $\mathbb{F}^S$, each axiom reduces to a pointwise instance in $\mathbb{F}$; for $\mathbb{F}^n$, each axiom reduces to a coordinate-wise instance. The check is mechanical but worth doing once for each construction (sequence space, polynomial space, signed-measure space). *Trigger:* a new operation defined on a new set; verify it produces a vector space before applying linear-algebra machinery.

2. **Apply the [[Def - Subspace|subspace criterion]] to certify a subspace.** Show $0 \in U$, $U + U \subseteq U$, $\mathbb{F} U \subseteq U$. The closure under additive inverses is then automatic via $-u = (-1) u$. *Trigger:* a subset of a known vector space whose closure under operations is in question.

3. **Reduce a candidate "smallest containing subspace" to an intersection.** The smallest subspace of $V$ containing a set $S$ is the intersection of all subspaces of $V$ containing $S$, by [[Ex - Intersection of subspaces is a subspace]]. This is the standard construction of the *span*. *Trigger:* you want to construct the "smallest" subspace with some property.

4. **Reduce directness of a sum to uniqueness of decomposition of zero.** By [[Thm - Conditions for a Direct Sum]], a sum is direct iff $0 = v_1 + \cdots + v_m$ with $v_k \in V_k$ forces each $v_k = 0$. This converts uniqueness-everywhere to uniqueness-at-one-point. *Trigger:* a direct-sum claim to verify; check zero-uniqueness.

5. **For two subspaces, reduce directness to trivial intersection.** [[Thm - Direct Sum of Two Subspaces]]: $U + W$ is direct iff $U \cap W = \{0\}$. *Trigger:* exactly two subspaces are involved; check intersection. *Pattern:* "show $U \cap W = \{0\}$" by assuming $v$ in both and deriving $v = 0$.

6. **Symmetrize and antisymmetrize under an involution.** Given an involution $\sigma : V \to V$ (so $\sigma^2 = I$), decompose $V = V^+ \oplus V^-$ where $V^\pm = \ker(\sigma \mp I)$, via $v = \tfrac{1}{2}(v + \sigma v) + \tfrac{1}{2}(v - \sigma v)$. This requires characteristic $\neq 2$ (so $2$ is invertible). *Trigger:* a domain symmetry like $f(x) \mapsto f(-x)$, $M \mapsto M^T$, or complex conjugation; decompose into $\pm 1$ eigenspaces.

7. **Solve a linear equation by subtracting and dividing.** $v + \lambda x = w$ with $\lambda \neq 0$ has the unique solution $x = (w - v)/\lambda$, via cancellation in the additive group and scalar division. *Trigger:* a single linear equation with one unknown vector and a nonzero scalar coefficient.

8. **Multiply by the conjugate to invert in $\mathbb{C}$ (or any quadratic field).** $1/(a + bi) = (a - bi)/(a^2 + b^2)$. *Trigger:* you need to compute a multiplicative inverse in $\mathbb{C}$; the standard rationalization is the conjugate trick.

9. **Extract a witness to non-containment to violate a closure condition.** If $U \not\subseteq W$, choose explicitly $u \in U \setminus W$; this is the concrete witness used in contradiction arguments (as in [[Ex - Union of subspaces is a subspace iff one contains the other]]). *Trigger:* a containment fails; extract a witness vector and manipulate it.

10. **Diagonal-style construction across a countable family.** Given $\{W_k\}_{k \in \mathbb{N}}$, construct an object inhabiting none of them by choosing, for each $k$, a feature ruling out $W_k$. *Trigger:* a claim that some countable union covers a vector space; refute by constructing a witness outside every $W_k$.

11. **Pick a basis-like family and project to one direction.** Many subspaces are best probed by what coordinates they can or cannot contain. Standard basis vectors $e_k = (0, \dots, 0, 1, 0, \dots)$ in $\mathbb{F}^n$ or $\mathbb{F}^\infty$ are the natural probes. *Trigger:* a question about a subspace of a coordinate space; project to the coordinates.

**Illegal but tempting operations:**

> [!warning] 1. Forming "$V_1 \oplus V_2 \oplus V_3$" when the three subspaces are only pairwise disjoint
> It is tempting to extend [[Thm - Direct Sum of Two Subspaces]] from two subspaces to three by replacing the single intersection condition with all pairwise intersections being trivial. The standard counterexample is LADR Example 1.44: $V_1 = \{(x, y, 0)\}$, $V_2 = \{(0, 0, z)\}$, $V_3 = \{(0, y, y)\}$ in $\mathbb{F}^3$ pairwise intersect only in $\{0\}$, but $0 = (0, 1, 0) + (0, 0, 1) + (0, -1, -1)$ is a non-trivial decomposition, so the sum is not direct. The correct condition for $m \geq 3$ is [[Thm - Conditions for a Direct Sum]] (zero has only the trivial decomposition); the pairwise-disjointness condition becomes legal only when *together with* the zero-uniqueness check.

> [!warning] 2. Treating "subspace" as "any closed subset"
> It is tempting to treat any subset that is closed under one of the operations as "essentially a subspace". The integer lattice $\mathbb{Z}^2 \subset \mathbb{R}^2$ is closed under addition (and additive inverses) and contains $0$ — but is **not** a subspace because it fails closure under scalar multiplication by non-integer reals. The set of periodic functions $\mathbb{R} \to \mathbb{R}$ is closed under scalar multiplication but not under addition. The full three-condition criterion is necessary; partial closure is not enough. The repair condition is to demand both closure properties together (under the *full* field of scalars, including non-integer ones).

> [!warning] 3. Treating the union of subspaces as their sum
> It is tempting to write the smallest subspace containing $U$ and $W$ as $U \cup W$, by analogy with sets. The union is the smallest *set* containing both, but in general fails closure under addition — see [[Ex - Union of subspaces is a subspace iff one contains the other]]. The correct join in $\operatorname{Sub}(V)$ is the **sum** $U + W$, which adds all sums of elements. The union equals the sum only in the degenerate case where one subspace contains the other.

> [!warning] 4. Assuming every linear equation has a unique solution
> The equation $v + \lambda x = w$ with $\lambda \neq 0$ has a unique solution — see [[Ex - Solving a linear equation in F^n]]. But this requires $\lambda \neq 0$ in $\mathbb{F}$, i.e. a nonzero scalar with a multiplicative inverse. Over a [[Def - Ring|ring]] (a [[Def - Module|module]] in place of a vector space) the same equation might have multiple solutions or none — e.g. $2 x = 0$ has the nontrivial solution $x = 5$ in $\mathbb{Z}/10\mathbb{Z}$. The field hypothesis is necessary; the same caution applies wherever "divide by $\lambda$" appears.

> [!warning] 5. Decomposing into even and odd parts in characteristic 2
> The decomposition $f = \tfrac{1}{2}(f + f^\vee) + \tfrac{1}{2}(f - f^\vee)$ (with $f^\vee(x) = f(-x)$) gives the direct-sum splitting $\mathbb{R}^\mathbb{R} = V_e \oplus V_o$ — see [[Ex - Even and odd functions form a direct sum decomposition]]. The argument relies on the existence of $\tfrac{1}{2}$, which fails in characteristic $2$ (where $1 + 1 = 0$). Over a field of characteristic $2$, even and odd functions coincide, and the decomposition degenerates. A recurring caution: averaging-style constructions in linear algebra often require characteristic $\neq 2$ (or characteristic not dividing some integer).

---

# Problem-Solving Strategy

The problems in this topic are won or lost at the moment you classify what kind of problem you are looking at. Almost every exercise is one of five types, and each type has a characteristic assumption pattern and a characteristic route to the answer.

If the problem **asks you to verify a candidate is a vector space**, your route is mechanical: check the eight axioms one by one. For function spaces $\mathbb{F}^S$ the axioms reduce to pointwise instances in $\mathbb{F}$, which hold by the field axioms; for $\mathbb{F}^n$ they reduce to coordinate-wise instances; for more exotic spaces (sequence spaces, formal power series, signed measures, solution spaces of differential equations) the axioms each translate into an identity to verify in the appropriate concrete arithmetic. The temptation to "skip the obvious axioms" should be resisted on first encounter — the value of verifying once is that the structural reason why each axiom holds is made explicit, and subsequent claims about the space can be made by quoting "it is a vector space, hence axiom 7 applies".

If the problem **asks you to verify a candidate is a subspace**, you reach for the three-condition [[Def - Subspace|subspace criterion]]: $0 \in U$, closure under addition, closure under scalar multiplication. The first condition is often the fastest disqualifier; many candidate subspaces fail by *not containing $0$* (a line not through the origin, the set $\{f : \int f = b\}$ for $b \neq 0$, a solution set of a non-homogeneous linear system). The second and third conditions are also disqualifiers in particular cases (the union of two subspaces fails closure under addition; the integer lattice fails closure under scalar multiplication). The criterion is not just a checklist; it is a diagnostic, with each condition revealing the failure mode of a non-subspace.

If the problem **asks you to characterize the sum, intersection, or direct sum of subspaces**, the route runs through the lattice structure. Sum is join, intersection is meet, and direct sum is the special case of sum with unique decomposition. Almost every such problem boils down to verifying the appropriate closure or universal property — see [[Ex - Sum of two subspaces is the smallest containing both]] and [[Ex - Intersection of subspaces is a subspace]] for the standard templates. The non-obvious move is recognizing when an *ad hoc* set construction is secretly a sum, intersection, or direct sum in disguise: the "everything fixed by the involution $\sigma$" subspace is the kernel of $\sigma - I$, the "kernel of a linear map" is the equalizer of the map with $0$, the "smallest subspace containing $S$" is the intersection of all subspaces containing $S$. Recognizing these in disguise makes the problem reduce to a known lattice-theoretic argument.

If the problem **asks you to certify a direct sum**, the recipe depends on the number of summands. For two summands, [[Thm - Direct Sum of Two Subspaces]] reduces the question to checking $U \cap W = \{0\}$ — usually proved by assuming $v \in U \cap W$ and deriving $v = 0$. For more than two summands, the pairwise-intersection condition is *insufficient* (LADR Example 1.44), and one must invoke [[Thm - Conditions for a Direct Sum]] directly: assume $0 = v_1 + \cdots + v_m$ with $v_k \in V_k$, and force each $v_k = 0$. The argument typically uses problem-specific structure: invariance under an operator, orthogonality, a clever choice of basis. The skill is recognizing that "verify directness" is the right question — usually because some downstream construction (a basis of the union, a projection, a block-diagonal decomposition of an operator) requires the directness.

If the problem **involves an infinite-dimensional vector space**, the structural intuition shifts. Finite-dimensional results often fail (e.g. "every subspace has a complementary subspace of the same dimension" needs care in infinite [[Def - Dimension|dimensions]]; "every operator has a matrix" depends on basis choice and converges only in special cases). The exercise [[Ex - F^infinity is not the union of finite-dimensional subspaces]] is the prototype: a structural result about $\mathbb{F}^\infty$ that has no finite-dimensional analogue. When a problem feels easy "but works in finite dimensions only", the obstruction is usually a cardinality issue (countable cannot cover uncountable) or a topological one (closure not coming for free).

Finally, a meta-strategy threads through all of the above: **when in doubt, reduce to the field $\mathbb{F}$**. Almost every vector-space axiom is a pointwise or coordinate-wise field-axiom application, and many subspace-membership problems reduce to algebraic identities in $\mathbb{F}$. The pattern "show $X$ as a statement about scalars; verify it in $\mathbb{F}$" is universal. The reason this works is the structural fact that vector spaces over $\mathbb{F}$ are built linearly from $\mathbb{F}$ — every theorem about them either follows from the field axioms or fails entirely.

The single unifying question of this chapter is: **does this subset of $V$ inherit the linear structure?** Every problem is some shade of this question — sometimes asked of a specific subset, sometimes of a sum or intersection of subsets, sometimes of the operations themselves. The vector-space and subspace axioms are the formal answer; the closures and lattice operations are the consequences; and the exercises are calibration of one's ability to verify the answer in concrete cases.

---

# Most Reusable Properties

- **[[Def - Subspace|Subspace criterion]]** (contains $0$, closed under $+$ and $\lambda \cdot$): this is the most-used single tool in the chapter, and one of the most-used in all of linear algebra. It identifies whether an arbitrary subset of a vector space carries linear structure, with three concrete checks. The closure-under-additive-inverses condition is absorbed by closure under scalar multiplication (via $-u = (-1) u$). Recognize its applicability whenever you encounter a subset of a vector space and need to apply any linear-algebra machinery — bases, kernels, ranges, eigenspaces — that requires the subset to be a subspace. **Typical use:** verify that a specific subset (the kernel of a linear map, the orthogonal complement, the solution set of a homogeneous linear system) is a subspace before applying further theorems to it.

- **[[Thm - Conditions for a Direct Sum|Direct-sum criterion (zero-uniqueness)]]**: a sum is direct iff the only decomposition of $0$ is trivial. This is the universal certifier of directness, applicable to any number of summands, and is the workhorse of every direct-sum argument in later chapters (spectral theorems, generalized eigenspace decomposition, Jordan form). The criterion converts uniqueness-everywhere into uniqueness-at-one-point. **Typical use:** verify $V = \bigoplus V_k$ for a candidate decomposition (e.g. eigenspaces of an operator) before invoking the existence of well-defined projections $\pi_k$.

- **[[Thm - Direct Sum of Two Subspaces|Two-subspace direct-sum criterion (trivial intersection)]]**: for two summands only, $U + W$ is direct iff $U \cap W = \{0\}$. The simpler criterion for the most common case. **Typical use:** verify $V = U \oplus W$ from a candidate complementary pair (orthogonal complement, range plus kernel of a projection, image of a projection and its complement); the dimension count $\dim(U + W) = \dim U + \dim W$ falls out for free.

- **The decomposition of a vector under an involution into $\pm 1$ eigenspaces**: whenever $V$ carries an involution $\sigma : V \to V$ with $\sigma^2 = I$, $V = V^+ \oplus V^-$ via $v = \tfrac{1}{2}(v + \sigma v) + \tfrac{1}{2}(v - \sigma v)$. The construction recurs throughout linear algebra: symmetric and antisymmetric matrices, even and odd functions, real and imaginary parts of a complex linear operator, Hermitian and skew-Hermitian parts. **Typical use:** decompose a structure under a known symmetry into its symmetric and antisymmetric pieces, then study them independently.

- **The lattice $(\operatorname{Sub}(V), \cap, +)$ with meet $\cap$ and join $+$**: subspaces of $V$ form a complete lattice under inclusion, with arbitrary intersection as meet and (binary or finite) sum as join. The lattice is modular but not generally distributive. **Typical use:** organize the network of subspaces of a vector space (eigenspaces, kernels, ranges, invariant subspaces of an operator) as a lattice diagram and reason about their meets and joins; questions like "what is the smallest subspace containing both $U$ and $W$" or "what is the largest subspace contained in both" become lattice operations.

---

# Bridges

1. **Group theory — the additive structure of a vector space is an abelian group.** The eight axioms of [[Def - Vector Space|a vector space]] split into "$(V, +, 0)$ is an [[Def - Abelian Group|abelian group]]" and "scalar action is linear". So every fact about abelian groups — uniqueness of identity, uniqueness of inverses, cancellation, the lattice of subgroups, the existence of quotients $G/H$ for any subgroup — applies to the additive structure of a vector space. The proofs in [[Thm - Uniqueness of Additive Identity and Inverses]] are word-for-word identical to the corresponding proofs in [[Def - Group|group theory]]. A subspace is, in particular, a subgroup of the additive group; a quotient space $V/U$ is, in particular, a quotient group. The "extra" content of a vector space is the scalar action by $\mathbb{F}$ and the corresponding distributivity.

2. **Ring theory — a field is a commutative [[Def - Ring|ring]] with multiplicative inverses for every nonzero element.** The chain of definitions is $\text{ring} \subset \text{commutative ring} \subset \text{commutative ring with } 1 \subset \text{integral domain} \subset \text{field}$, each obtained by adding one axiom. A vector space is a module over a field, so the entire theory of vector spaces sits inside [[Def - Module|module theory]] as a special case. The polynomial ring $\mathbb{F}[x]$ — see [[Def - Polynomial Ring]] — acts on any vector space $V$ once a linear operator $T : V \to V$ is chosen, by $p(x) \cdot v := p(T) v$; this construction is the gateway to the minimal polynomial in [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]]. The relationship "vector space = module over a field" is the structural reason linear algebra is cleaner than module theory: every vector space has a basis, every short exact sequence splits, every subspace is a direct summand. None of these hold in general for modules.

3. **Module theory — every vector space is a module over its scalar field; subspaces are submodules.** A [[Def - Module|module]] over a [[Def - Ring|ring]] $R$ is exactly the generalization of a vector space obtained by replacing the field by a ring. The eight axioms read identically. The substructure analogues — submodules in place of subspaces, sums of submodules, direct sums — are also identical: see [[Def - Submodule]]. The key structural differences (modules need not be free, submodules need not be direct summands, dimension may be ill-defined) all come from the absence of multiplicative inverses for nonzero elements. So learning the vector-space case prepares the reader for module theory and identifies precisely which results survive the generalization.

4. **Multivariate analysis — the total derivative is a linear map.** The [[Def - The Total Derivative and Differentiability|total derivative]] $Df_p : \mathbb{R}^n \to \mathbb{R}^m$ at a point $p$ of a differentiable map $f : \mathbb{R}^n \to \mathbb{R}^m$ is the best linear approximation to $f$ near $p$. The vector space $\mathbb{R}^n$ here is the **tangent space** at $p$, an instance of the linear-algebra construction sitting inside the multivariate calculus framework. The Jacobian matrix is the matrix of $Df_p$ in the standard bases of $\mathbb{R}^n$ and $\mathbb{R}^m$ — but the linear map $Df_p$ exists abstractly, independent of any basis. The "vectors are platonic, tuples are viewings" frame of this chapter is exactly the structural mindset that distinguishes the linear map (the derivative) from its matrix (the Jacobian).

5. **Measure theory — signed measures on a measurable space form a vector space.** Given a measurable space $(\Omega, \mathcal{F})$, the [[Def - Signed Measure|signed measures]] on $\mathcal{F}$ form a real vector space under pointwise operations: $(\mu + \nu)(A) = \mu(A) + \nu(A)$ and $(\lambda \mu)(A) = \lambda \mu(A)$. The vector-space structure is what licenses the Jordan decomposition $\mu = \mu^+ - \mu^-$ (a direct-sum decomposition into positive and negative parts) and the Radon-Nikodym derivative (an identification of the absolutely continuous measures with a function space). The construction is a substantial instance of the chapter's themes: a function space (signed measures are set functions), a direct-sum decomposition under an involution-like sign reversal, and a coordinate-free understanding of $L^p$-style geometry.

6. **Special relativity — Minkowski space is a 4-dimensional real vector space with a non-degenerate symmetric bilinear form.** [[Def - Minkowski Space and the Metric|Minkowski space]] is, as a vector space, just $\mathbb{R}^4$; the special-relativistic content is the additional structure of the **Minkowski metric** $\eta_{\mu\nu} = \operatorname{diag}(-1, 1, 1, 1)$, an indefinite bilinear form. The vector-space layer is the chapter's territory: linear combinations of 4-vectors, Lorentz transformations as linear maps, the Lorentz group as a subgroup of $\operatorname{GL}_4(\mathbb{R})$. The bilinear form is added later — see [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] and [[Linear Algebra VI — §6 Inner Product Spaces]]. The bridge runs: vector space (this chapter) → bilinear form (LADR §9 or special relativity §1) → causal structure and Lorentz invariance (relativity proper). The same construction pattern — start with a vector space, then layer on additional structure — underlies symplectic geometry, Riemannian geometry, and almost every other geometric setting in physics.

---

# Insights

**The unifying frame: a vector is a platonic object; a coordinate tuple is one viewing.** This is the most important conceptual lesson of the chapter and the philosophy of Axler's text. A vector in $V$ is an abstract element of an abstract space; the tuple $(x_1, \dots, x_n) \in \mathbb{F}^n$ representing it depends on a *choice of basis*, which is a chart for $V$ in the way local coordinates are a chart for a manifold. Different choices of basis give different tuples for the same vector, related by the [[Linear Algebra III — §3A–D Linear Maps|change-of-basis formula]]. The price of working without a chosen basis is greater abstraction; the reward is that statements and proofs become *coordinate-free*, hence apply uniformly to every vector space and every basis. Many of the surprises and traps of linear algebra come from confusing the vector with its representation — for instance the temptation to think of "diagonalizable" as a property of a *matrix* rather than of the underlying linear *map*. The same matrix can be the matrix of different operators in different bases; the underlying property is operator-theoretic. Keeping vector and representation distinct is the single most consequential conceptual move in linear algebra.

**The true name of a subspace: a subset closed under linear combinations.** The [[Def - Subspace|subspace criterion]] (contains zero, closed under addition, closed under scalar multiplication) is the right thing to *check*, but the right thing to *think* is "subset closed under linear combinations". Every meaningful construction in linear algebra — spans, linear maps, kernels, ranges, bases — is built out of linear combinations, and a subspace is exactly a subset on which all linear combinations can be formed without leaving the subset. When you reach for the subspace property in a proof, what you almost always need is closure under linear combinations, not the three pieces individually. So the operational name of "subspace" is "closed under linear combinations", and the three-condition formulation is the verification procedure.

**A trigger-reaction pattern: see "smallest subspace containing $S$" → think "span of $S$".** Almost every exercise that asks you to construct or characterize the smallest subspace containing some set $S$ has the same answer: the **span** of $S$, defined as the intersection of all subspaces containing $S$ (or equivalently, the set of all finite linear combinations of elements of $S$). The construction recurs in every direction: smallest subspace containing $v_1, \dots, v_n$ (the span); smallest subspace containing $V_1 \cup V_2$ (the sum $V_1 + V_2$); smallest subspace containing the columns of a matrix (the column space); smallest invariant subspace containing $v$ (the $T$-cyclic subspace generated by $v$). Reach for "intersect all subspaces with the property" whenever you face a "smallest containing" question, and use the alternative characterization (linear combinations of generators) for computation.

**Sums replace unions in the subspace lattice; direct sums are the cleanest case.** The lattice $\operatorname{Sub}(V)$ has intersection as meet (set-theoretic) but sum (not union) as join (algebraically built). The asymmetry — meet is set-theoretic, join is enriched — is a recurring pattern in algebra: the lattice of subgroups, the lattice of submodules, the lattice of ideals, the lattice of $\sigma$-algebras all share this structure. The cleanest case is the **direct sum**: a sum with unique decomposition, equivalent to disjoint intersection (for two summands) or trivial decomposition of zero (in general). Direct sums are the algebraic skeleton of "decomposition into pieces" throughout linear algebra: the spectral theorem, generalized eigenspace decomposition, Jordan form, polar decomposition, SVD all package direct-sum decompositions together with the projections they produce. Whenever you see "decompose $V$ into $V_1, \dots, V_m$", what you usually need is a direct sum, and certifying directness is the work.

**Universal-property proofs decompose into "exhibit" and "absorb".** Many results in this chapter are characterizations by universal property: the span is the smallest subspace containing $S$; the sum is the smallest subspace containing the union; the intersection is the largest subspace contained in the family. The proof template is universal: (1) exhibit a candidate and show it has the desired feature; (2) show every other candidate with the feature contains/is contained in it. The same template works for quotients, kernels, products, coproducts, limits, and colimits across category theory. Recognizing universal-property structure when it appears lets you generate a proof by populating the two steps. The signal is usually a word like "smallest", "largest", "free", or "universal" — and the response is to set up the exhibit-and-absorb diptych.

**Insight: linear algebra is the easy module theory.** The full generality of [[Def - Module|module theory]] is genuinely harder — modules need not have bases, dimension may be undefined, every submodule need not be a direct summand, free modules are special, torsion exists. Linear algebra is module theory with one extra axiom: the scalars form a field rather than a [[Def - Ring|ring]]. That single axiom — multiplicative inverses for nonzero scalars — buys an enormous amount: bases exist for every vector space, dimension is well-defined, every subspace is a direct summand, every short exact sequence splits, every linear map has a transpose-and-block-diagonal structure (Smith normal form is trivial). When you encounter linear algebra, you are encountering module theory in its cleanest manifestation. When you encounter module theory, you are encountering the systematic loss of these features. Knowing which features are field-specific and which are general is the most useful piece of structural awareness in algebra.

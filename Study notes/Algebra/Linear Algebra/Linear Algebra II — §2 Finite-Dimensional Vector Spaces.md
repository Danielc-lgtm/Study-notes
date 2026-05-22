---
type: topic
subject: linear-algebra
chapter: "2"
title: "Linear Algebra II — Finite-Dimensional Vector Spaces"
tags: [algebra, linear-algebra]
---

# Notation Registry

Throughout this topic we work over a fixed field $F$, which the reader may take to be $\mathbb{R}$ or $\mathbb{C}$ on first reading; nothing in this chapter uses anything more than the field axioms, so every theorem proved here is theorem in any algebraic field. $V$ denotes a vector space over $F$. The word **list** always means a *finite ordered tuple* $v_1, \ldots, v_m$ of vectors in $V$, never an infinite sequence and never a set — order does not affect the conclusions we draw, but the proofs index along lists, and the count of entries (the **length**) is the crucial invariant. The empty list, of length zero, is admitted everywhere; it is linearly independent by convention, and its span is $\{0\}$.

- $F$ — a field; in LADR, $F = \mathbb{R}$ or $\mathbb{C}$
- $V, U, W$ — vector spaces over $F$
- $v_1, \ldots, v_m$ — a list (length $m$) of vectors in $V$
- $\operatorname{span}(v_1, \ldots, v_m) = \{a_1 v_1 + \cdots + a_m v_m : a_i \in F\}$ — the **span** of the list
- $F^n$ — the vector space of $n$-tuples of elements of $F$
- $\mathcal{P}(F)$ — the vector space of polynomials with coefficients in $F$
- $\mathcal{P}_m(F)$ — the subspace of polynomials of degree at most $m$
- $F^\infty$ — the vector space of sequences in $F$
- $\dim V$ — the **dimension** of $V$ — the common length of all bases of $V$
- $V_1 + V_2$ — the sum of two subspaces, $\{v_1 + v_2 : v_i \in V_i\}$
- $V_1 \oplus V_2$ — the direct sum, used when $V_1 \cap V_2 = \{0\}$

**Standing convention.** "Finite-dimensional" means *has a finite spanning list*. Equivalently, it has a basis, and that basis has finite length; the equivalence is the content of [[Thm - Bases are Equinumerous|2.34]] together with [[Thm - Every Spanning List Contains a Basis|2.30]]. When $V$ is finite-dimensional, every list of vectors in $V$ has a well-defined length in $\mathbb{N}$, and "longer", "shorter", and "the same length" are unambiguous. The chapter's whole drama plays out at the level of these integer lengths.

---

# Motivation

Here is the entire chapter in one sentence: **every vector in a finite-dimensional space has a unique expansion in any chosen basis, and the number of basis vectors does not depend on the choice.** Both halves of that sentence are non-trivial, both are proved in this chapter, and almost every later result in linear algebra is a corollary of them.

The previous topic, [[Linear Algebra I — §1 Vector Spaces]], defined vector spaces in abstract — a set with an addition, a scalar multiplication, and a list of axioms. The trouble with the definition is that it does not, by itself, give you a way to *describe* any specific vector. If $V = \mathbb{R}^3$ and I hand you a vector $v$, you would like to say "$v$ is the vector with coordinates $(2, -1, 5)$"; but the abstract axioms do not name coordinates, they only name addition and scalar multiplication. The bridge is the notion of a **basis**: a list of vectors with two properties — a *spanning* property, that every vector of $V$ is a linear combination of them, and an *independence* property, that the combination is unique. The basis is what installs coordinates on $V$. Once you have it, a vector $v \in V$ is faithfully recorded by the tuple of scalars in its expansion, and abstract linear algebra is converted into concrete arithmetic in $F^n$.

The chapter is the story of how to build a basis and how to count its elements. Section §2A introduces the two ingredients separately: spanning lists, which are "big enough" to reach every vector, and linearly independent lists, which are "small enough" that no vector is reached twice. Either property alone is unsatisfying — a spanning list may have redundancy, an independent list may not fill the space — but a list with *both* properties is exactly a basis. The fundamental quantitative fact, stated in §2A and reused everywhere, is the **length inequality** [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List]]: in any finite-dimensional space, every linearly independent list is at most as long as every spanning list. This single inequality, proved by an exchange-and-replace argument that goes back to Ernst Steinitz, is the engine of the whole chapter.

Section §2B brings the two properties together to define a basis and proves the existence theorems that follow from the length inequality almost mechanically: [[Thm - Every Spanning List Contains a Basis]] removes redundancy from a spanning list to make it independent, and [[Thm - Every Linearly Independent List Extends to a Basis]] adjoins vectors to an independent list to make it spanning. Bases are therefore the natural meeting place of "shrink down a spanning list" and "build up an independent list", and the two operations converge on the same answer.

Section §2C is where the chapter's true theorem lives. It says all bases of a given finite-dimensional space have the same length, so we may give that length a name — **dimension** — and the integer $\dim V$ is an intrinsic invariant of the space, independent of any choice. The whole hierarchy
$$\dim V_1 \;\leq\; \dim V_2 \;\leq\; \dim(V_1 + V_2) \;\leq\; \dim V_1 + \dim V_2$$
of dimension inequalities then drops out, culminating in the precise formula [[Thm - Dimension of a Sum of Subspaces|$\dim(V_1 + V_2) = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$]] — the linear-algebra counterpart of inclusion-exclusion for the sizes of finite sets.

The reader is assumed to have absorbed [[Linear Algebra I — §1 Vector Spaces]] — in particular the definitions of [[Def - Vector Space|vector space]], [[Def - Subspace|subspace]], [[Def - Sum of Subspaces|sum]] and [[Def - Direct Sum|direct sum]] of subspaces — and to be comfortable with the polynomial space $\mathcal{P}_m(F)$ as a worked example. No previous exposure to dimension or basis is required; in fact, the whole chapter is the careful derivation of those words.

---

# Concept Map

## §2A Span and Linear Independence

- **[[Def - Linear Combination and Span]]**
	- A **linear combination** of a list $v_1, \ldots, v_m$ is any vector of the form $a_1 v_1 + \cdots + a_m v_m$ with $a_i \in F$. The **span** is the set of all such combinations: $\operatorname{span}(v_1, \ldots, v_m) = \{a_1 v_1 + \cdots + a_m v_m : a_i \in F\}$. By convention the span of the empty list is $\{0\}$. The span is always a [[Def - Subspace|subspace]] of $V$, and in fact it is the *smallest* subspace containing every $v_i$ — so span is the "subspace closure" operation. A list **spans** $V$ when $\operatorname{span}(v_1, \ldots, v_m) = V$.

- **[[Def - Finite-Dimensional Vector Space]]**
	- A vector space $V$ is **finite-dimensional** if it admits a *finite* spanning list — that is, some list $v_1, \ldots, v_m$ of vectors in $V$ satisfies $\operatorname{span}(v_1, \ldots, v_m) = V$. Equivalently (proved later in the chapter), $V$ has a basis of finite length. $F^n$ is finite-dimensional via the standard list of unit vectors; $\mathcal{P}_m(F)$ is finite-dimensional via $1, z, z^2, \ldots, z^m$; the whole polynomial space $\mathcal{P}(F)$ and the sequence space $F^\infty$ are *not* finite-dimensional, because every finite list misses polynomials or sequences of high enough index.

- **[[Def - Linear Independence]]**
	- A list $v_1, \ldots, v_m$ is **linearly independent** if the only solution of $a_1 v_1 + \cdots + a_m v_m = 0$ is $a_1 = \cdots = a_m = 0$. The empty list is independent by convention. The operational meaning is "uniqueness of expansion": $v_1, \ldots, v_m$ is independent if and only if every vector in their span has a *unique* representation as a linear combination. A list is **linearly dependent** otherwise — that is, some nontrivial combination vanishes, equivalently some $v_k$ lies in the span of the others.

- **Linear dependence lemma.** If $v_1, \ldots, v_m$ is linearly dependent, then some $v_k$ lies in $\operatorname{span}(v_1, \ldots, v_{k-1})$, and removing this $v_k$ from the list does not change the span. This is the lemma that makes the chapter's exchange-and-replace arguments work: dependence means redundancy, and the lemma identifies the redundant vector explicitly as one that can be expressed in terms of its predecessors. It is also the engine behind [[Thm - Every Spanning List Contains a Basis|2.30]] (remove the redundant vectors one by one until none remain).

- **[[Thm - Length of Linearly Independent List Bounded by Length of Spanning List]]**
	- In any finite-dimensional vector space, **every linearly independent list is at most as long as every spanning list**. The proof is the **Steinitz exchange** procedure: feed the independent list's vectors into the spanning list one at a time, removing a spanning vector at each step; since the independent vectors never become redundant, there must be enough spanning vectors to swap out. From this single inequality, equinumerosity of bases, the well-definedness of dimension, and almost every other counting fact in the chapter follow as corollaries.

- **[[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional]]**
	- Every subspace $U$ of a finite-dimensional space $V$ is itself finite-dimensional. The proof is a greedy construction: start with any nonzero vector of $U$, keep extending the list by any vector of $U$ not yet in the span, and stop when no such vector exists. The length-inequality theorem guarantees the process must stop, because the growing list is linearly independent and the spanning list of $V$ caps its length. This is the source of *inheritance* of finite-dimensionality from $V$ down to all of its subspaces — a property the analogue for spans in infinite-dimensional spaces does not have.

> [!tip] Unlocked: Affine Independence *(from Affine Geometry, Loehr Ch 11)*
> Replace "linear combination summing to zero" with "linear combination of differences" and you get **affine independence**: points $p_0, \ldots, p_m$ in $F^n$ are affinely independent if the vectors $p_1 - p_0, \ldots, p_m - p_0$ are linearly independent. The affine span of $m+1$ affinely independent points is an $m$-dimensional flat. This is the language in which simplices, barycentric coordinates, and convex combinations are formulated, and it specialises linear independence to the case where the origin is no longer privileged.

- **[[Ex - Constructing a basis from a spanning list]]** (⭐)
	- Given a spanning list $(1, 2), (3, 6), (4, 7), (5, 9)$ of $F^2$, identify and remove the redundant vectors to produce a basis. Drills the linear dependence lemma and the algorithm of [[Thm - Every Spanning List Contains a Basis|2.30]].

- **[[Ex - Removing redundancy from a linearly dependent list]]** (⭐)
	- For the list $(1, 2, 3), (6, 5, 4), (15, 16, 17), (8, 9, 7)$ in $\mathbb{R}^3$, find the smallest $k$ such that the $k$th vector lies in the span of the previous ones, and confirm by direct computation. Drills the linear dependence lemma as a diagnostic tool.

> [!note] Exercise Index — §2A
> [[Exercise Index - §2A Span and Linear Independence]]

## §2B Bases

- **[[Def - Basis]]**
	- A **basis** of $V$ is a list of vectors in $V$ that is both linearly independent *and* spans $V$. Equivalently (the criterion proved in §2B), every vector in $V$ has a *unique* expansion as a linear combination of the list — this is the operational meaning, and it is the property the rest of linear algebra rests on. The standard basis of $F^n$ is the list of unit vectors $e_k = (0, \ldots, 0, 1, 0, \ldots, 0)$; the standard basis of $\mathcal{P}_m(F)$ is $1, z, z^2, \ldots, z^m$. A vector space typically has many bases.

- **[[Thm - Every Spanning List Contains a Basis]]**
	- Every spanning list of a vector space can be reduced to a basis by deleting redundant entries — specifically, the entries that lie in the span of the previous ones. The procedure is constructive and runs from left to right through the list, identifying each redundant vector by the [[Def - Linear Combination and Span|linear dependence lemma]] and deleting it. As an immediate corollary, every finite-dimensional vector space has a basis: it has, by definition, a finite spanning list, and the spanning list contains a basis.

- **[[Thm - Every Linearly Independent List Extends to a Basis]]**
	- Every linearly independent list of vectors in a finite-dimensional space $V$ can be extended to a basis of $V$ by adjoining additional vectors. The construction is the obvious one: start with the independent list, concatenate any spanning list of $V$ to its right, and apply the reduction procedure of [[Thm - Every Spanning List Contains a Basis|2.30]]. The reduction cannot delete any of the original independent vectors (their independence forbids it), so the basis it produces contains them. Together with [[Thm - Every Spanning List Contains a Basis|2.30]], this theorem says **bases are the meeting point of two converging operations** — reducing a spanning list down and extending an independent list up.

- **Direct-sum complement.** If $U$ is a subspace of a finite-dimensional $V$, there exists a subspace $W$ of $V$ with $V = U \oplus W$. The construction: take a basis $u_1, \ldots, u_m$ of $U$; extend it to a basis $u_1, \ldots, u_m, w_1, \ldots, w_n$ of $V$; set $W = \operatorname{span}(w_1, \ldots, w_n)$. The extension theorem is what makes finite-dimensional subspaces well-behaved: every subspace has a complement, so every short exact sequence splits — a fact that fails dramatically in infinite-dimensional Banach spaces.

> [!tip] Unlocked: Free Module *(from Module Theory)*
> Replace the field $F$ by an arbitrary ring $R$ and a vector space by a [[Def - Module|module]]: a list of "vectors" (now elements of an $R$-module $M$) is called a **free generating set** if every element of $M$ has a unique expansion as an $R$-linear combination. The module is then **free**, and the size of the free generating set is its **rank** — the module-theoretic analogue of dimension. The wrinkle is that not every module is free, and even free modules over non-commutative rings can have ill-behaved rank; the property "every two free generating sets have the same cardinality" is called **invariant basis number** and is non-trivial in general. Fields are the special case where every module is free and IBN is automatic.

- **[[Ex - Polynomials of degree at most n form a basis]]** (⭐)
	- Prove that $1, z, z^2, \ldots, z^n$ is a basis of $\mathcal{P}_n(F)$, the polynomials of degree at most $n$. Drills the definition of basis and the linear independence of polynomials as functions.

- **[[Ex - Sum of dimensions in direct sum]]** (⭐⭐)
	- If $V = U \oplus W$, $u_1, \ldots, u_m$ is a basis of $U$, and $w_1, \ldots, w_n$ is a basis of $W$, prove that $u_1, \ldots, u_m, w_1, \ldots, w_n$ is a basis of $V$ (and therefore $\dim V = \dim U + \dim W$). Drills the interaction of bases with direct sum decomposition.

> [!note] Exercise Index — §2B
> [[Exercise Index - §2B Bases]]

## §2C Dimension

- **[[Thm - Bases are Equinumerous]]**
	- Any two bases of a finite-dimensional vector space have the same length. The proof is two applications of the length inequality [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]] back to back: basis $B_1$ is linearly independent and $B_2$ spans, so $|B_1| \leq |B_2|$; reversing roles gives $|B_2| \leq |B_1|$. This is the result that licenses the next definition: the common length of all bases is an invariant of $V$ alone.

- **[[Def - Dimension]]**
	- The **dimension** $\dim V$ of a finite-dimensional vector space $V$ is the common length of all bases of $V$. Examples: $\dim F^n = n$, $\dim \mathcal{P}_m(F) = m+1$, $\dim \{0\} = 0$. Dimension is the single most useful invariant of a finite-dimensional space — almost every later theorem (rank-nullity, isomorphism of equal-dimensional spaces, the existence of eigenvalues on complex spaces) is a statement about dimensions. **The true name of dimension** is "the unique integer that all bases share".

- **Length-of-basis theorems.** In a finite-dimensional space of dimension $n$: every linearly independent list of length $n$ is automatically a basis (it cannot be properly extended — see [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] — so it must already span), and every spanning list of length $n$ is automatically a basis (it cannot be properly reduced — see [[Thm - Every Spanning List Contains a Basis|2.30]] — so it must already be independent). The consequence is that in dimension $n$ you only ever need to check **one** of the two basis properties for a list of the right length, not both.

- **Subspace dimension and equality.** If $U$ is a subspace of $V$ with $V$ finite-dimensional, then $\dim U \leq \dim V$, and equality holds if and only if $U = V$. The inequality is immediate from the length inequality (a basis of $U$ is independent in $V$, so is shorter than a basis of $V$); the equality case requires that a basis of $U$ of length $\dim V$ is also a basis of $V$, by the length-of-basis theorems.

- **[[Thm - Dimension of a Sum of Subspaces]]**
	- For subspaces $V_1, V_2$ of a finite-dimensional space, $\dim(V_1 + V_2) = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$. This is the linear-algebra inclusion-exclusion: a basis of the intersection is the "doubly counted" portion. The proof: take a basis of $V_1 \cap V_2$, extend it independently to bases of $V_1$ and of $V_2$, and show the concatenated list is a basis of $V_1 + V_2$. As a corollary, a direct sum $V = V_1 \oplus V_2$ satisfies $\dim V = \dim V_1 + \dim V_2$, with no correction term — direct sum is the dimension-additive case.

> [!tip] Unlocked: Tangent Space Dimension *(from Differential Geometry)*
> A smooth $n$-manifold $M$ has, at every point $p$, a **tangent space** $T_p M$ — a vector space whose elements are equivalence classes of curves through $p$, or equivalently derivations on smooth functions at $p$. The dimension of $T_p M$ equals $n$, the dimension of the manifold, and this equality is *the* characterising property of manifold dimension. Computationally, $T_p M$ is the span of the partial-derivative operators $\partial/\partial x^1, \ldots, \partial/\partial x^n$ in a coordinate chart around $p$, a basis of length $n$. This is also the codomain of the [[Def - The Total Derivative and Differentiability|total derivative]], which at each point $p$ is a linear map $T_p M \to T_{f(p)} N$ between tangent spaces; rank-nullity for that map (next chapter) is then a statement about the manifold's local geometry.

> [!tip] Unlocked: Hamel Basis *(from Functional Analysis)*
> Every vector space — including infinite-dimensional ones — has a basis, by an application of **Zorn's lemma** to the partial order of linearly independent subsets. Such a basis is called a **Hamel basis**. It satisfies the same uniqueness-of-expansion property as in finite dimensions: every vector is a *finite* linear combination of basis elements. The catch is that Hamel bases of infinite-dimensional Banach spaces are pathological — they are uncountable (by the Baire category theorem), they cannot be exhibited explicitly, and they are useless for analysis. The right notion in infinite-dimensional analysis is the **Schauder basis**, where one allows infinite series — but Schauder bases exist only in separable spaces and the existence is subtle.

- **[[Ex - A list with the right length is a basis iff spanning iff independent]]** (⭐)
	- For a list of length $\dim V$ in a finite-dimensional space $V$, show that being a basis, being linearly independent, and spanning are all equivalent. Drills the length-of-basis theorems.

- **[[Ex - Dimension of a subspace equals dimension only if equal]]** (⭐⭐)
	- For a subspace $U$ of a finite-dimensional $V$, prove that $\dim U = \dim V$ implies $U = V$. Drills the interplay between length-of-basis theorems and the fact that a basis of a subspace is automatically a linearly independent list in the ambient space.

> [!note] Exercise Index — §2C
> [[Exercise Index - §2C Dimension]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises of §2 cluster around five recurring goals, and recognising which goal a problem points to is half the battle. The first and most common is **identifying a basis**: you are given a candidate list and asked whether it is a basis, or you are asked to construct one for a subspace defined by some condition. A second is **computing a dimension**, often as the route to a counting argument or to compare two spaces. A third is **proving that two subspaces have nontrivial intersection** or, dually, that their sum is everything — both of which are pure dimension counts. A fourth is **extending a list** — either reducing a spanning list to a basis or extending an independent list to one — typically to prepare the ground for a direct-sum decomposition or for a later argument about linear maps. A fifth is **comparing two subspaces**, deciding whether one contains the other or equals it, using dimension as a numerical witness. These five targets — identify a basis, compute a dimension, force intersection or sum, extend or contract a list, compare subspaces — recur because each is a way of pinning down a finite-dimensional space numerically: you understand such a space when you know its dimension and a basis, and you understand a subspace when you know its dimension and how it sits inside.

**Sources — what assumptions do we usually leverage?**

The assumptions in §2 problems are equally stereotyped. **A list of given length** is the most frequent — once you know a list has length $\dim V$, the [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|length inequality]] together with the length-of-basis theorems collapses the work of checking it is a basis from two conditions to one. **A subspace defined by linear equations** — for instance $\{(x_1, \ldots, x_5) : x_1 = 3 x_2 \text{ and } x_3 = 7 x_4\}$ — provides a recipe for a basis by solving the equations parametrically, with each free parameter contributing a basis vector. **Two given subspaces with known dimensions**, where the question routes through [[Thm - Dimension of a Sum of Subspaces|2.43]] to deduce information about their intersection or sum — a setup where dimension count alone suffices to force intersection to be nontrivial, when $\dim V_1 + \dim V_2 > \dim V$. **A polynomial space with degree constraints**, where the basis is some explicit list of polynomials ($z^k$, $(z-c)^k$, $(z-c_1) \cdots (z-c_k)$, ...) and the difficulty is in proving linear independence by extracting coefficients. **A direct sum $V = U \oplus W$** with bases on each side, routing through [[Ex - Sum of dimensions in direct sum]] to a basis of the whole. The recurring move is to route a source to a target: a list of the right length routes through the length-of-basis theorems to "is a basis"; two subspaces with summed dimensions exceeding the ambient route through 2.43 to a nontrivial intersection; a subspace defined by equations routes through parametric solution to an explicit basis.

---

# Legal Operations

These are the moves that almost every problem in §2 is assembled from. When stuck, scan the list and try each one. Everything here is self-contained.

**Legal operations:**

1. **Reduce a spanning list to a basis.** Given a list that spans $V$, run from left to right and delete any vector that lies in the span of the previous ones — by the [[Def - Linear Combination and Span|linear dependence lemma]] this never changes the span, and when no such vector remains the list is independent and hence a basis. *Trigger:* you have a spanning list with potential redundancy. *Pattern:* "Apply [[Thm - Every Spanning List Contains a Basis|2.30]] to extract a basis."

2. **Extend an independent list to a basis.** Given $u_1, \ldots, u_m$ linearly independent in a finite-dimensional $V$, concatenate any spanning list $w_1, \ldots, w_n$ on the right and apply the reduction of operation 1; none of the $u_i$ get deleted, and the result is a basis containing the original list. *Trigger:* you have an independent list and want to fill out to a basis (e.g. to build a direct-sum complement, or to pass to the quotient). *Pattern:* "Extend by [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] using $w_1, \ldots, w_n$."

3. **Read off the length-of-basis shortcut.** In a space of known dimension $n$, a list of length $n$ is a basis if and only if it is *either* linearly independent *or* spanning — you do not need to check both. *Trigger:* you have a list whose length matches $\dim V$. *Pattern:* "It suffices to show linear independence; spanning follows."

4. **Build a basis of a subspace by parametrising.** When $U \subseteq F^n$ is defined by a system of linear equations, solve the equations to express every element of $U$ as a parametric vector. Each free parameter contributes one basis vector — set the parameter to $1$ and the others to $0$. *Trigger:* the subspace is given as the solution set of homogeneous linear equations. *Pattern:* "Parametrise the solutions; the unit-parameter vectors form a basis."

5. **Bound a subspace's dimension by the length inequality.** A linearly independent list in $V$ is also linearly independent in any subspace it lies in, and a spanning list of a subspace gives a spanning list of itself — so the [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|length inequality]] sandwiches the dimension between known values. *Trigger:* you want to determine $\dim U$ and you can name a few independent vectors in $U$ and a known $\dim V$ that bounds it. *Pattern:* "$k$ independent vectors $\implies \dim U \geq k$; $U \subseteq V \implies \dim U \leq \dim V$."

6. **Apply the dimension formula for sums.** For subspaces $V_1, V_2$ of finite-dimensional $V$, $\dim(V_1 + V_2) + \dim(V_1 \cap V_2) = \dim V_1 + \dim V_2$. *Trigger:* the problem mentions two subspaces and asks about their intersection, their sum, or whether $V_1 + V_2 = V$. *Pattern:* "By [[Thm - Dimension of a Sum of Subspaces|2.43]], $\dim(V_1 \cap V_2) = \dim V_1 + \dim V_2 - \dim(V_1 + V_2) \geq \dim V_1 + \dim V_2 - \dim V$."

7. **Use the pigeonhole consequence: $\dim V_1 + \dim V_2 > \dim V \implies V_1 \cap V_2 \neq \{0\}$.** This is operation 6 in its most reusable form. *Trigger:* two subspaces whose dimensions sum to more than the ambient. *Pattern:* "Forced intersection."

8. **Construct a complement via basis extension.** To produce a subspace $W$ with $V = U \oplus W$, take a basis of $U$, extend to a basis of $V$ by operation 2, and let $W$ be the span of the new vectors. *Trigger:* you need a complementary subspace or a direct-sum decomposition. *Pattern:* "Extend a basis of $U$ to one of $V$; the new vectors span the complement."

9. **Test polynomial linear independence by reading off the leading coefficient.** A list of polynomials with strictly increasing degrees is linearly independent: any nontrivial linear combination has a well-defined leading term whose coefficient must vanish, forcing the next, and so on. *Trigger:* the list is of polynomials, particularly ones with distinct degrees. *Pattern:* "Sort by degree; the top degree forces the top coefficient to be zero, induct down."

**Illegal but tempting operations:**

> [!warning] 1. Treating "two bases" as "the same basis"
> It is tempting, once you have proved that any two bases have the same length, to slip into thinking they are essentially the same basis. They are not. The vectors are usually entirely different — only the *integer length* is shared. The classic counterexample is $F^2$ with the standard basis $(1, 0), (0, 1)$ and the alternative $(1, 2), (3, 5)$: same length, but a vector's coordinate tuple changes when you switch. The *change-of-basis matrix* in [[Linear Algebra III — §3A–D Linear Maps]] is the bookkeeping for this — bases are interchangeable only up to a recorded transformation.

> [!warning] 2. Assuming $\dim(V_1 + V_2) = \dim V_1 + \dim V_2$ without checking intersection
> The dimension of a sum is *not* in general the sum of dimensions. The correction term $-\dim(V_1 \cap V_2)$ is precisely what an inclusion-exclusion accounting would predict, and it can be substantial: in $\mathbb{R}^3$, two distinct 2-dimensional planes through the origin have $\dim V_1 + \dim V_2 = 4$ but $\dim(V_1 + V_2) = 3$, so $\dim(V_1 \cap V_2) = 1$ — they meet in a line. Forgetting the correction term is the most common error in §2C problems. The dimension formula is additive only on direct sums, where intersection is trivial.

> [!warning] 3. Assuming a generalisation of 2.43 to three subspaces
> The naive inclusion-exclusion analogue $\dim(V_1+V_2+V_3) = \sum \dim V_i - \sum \dim(V_i \cap V_j) + \dim(V_1 \cap V_2 \cap V_3)$ is **false** in general. The standard counterexample: take three distinct lines through the origin in $\mathbb{R}^2$. Each line has dimension 1, each pairwise intersection is $\{0\}$ (dimension 0), the triple intersection is $\{0\}$ (dimension 0), and $V_1 + V_2 + V_3 = \mathbb{R}^2$ (dimension 2). The naive formula would predict $1+1+1 - 0 - 0 - 0 + 0 = 3 \neq 2$. The reason it fails is that linear subspaces are not sets-in-general: three lines through the origin in the plane forcibly create new vector dependencies that the set-theoretic count cannot see. There exists a correct three-subspace formula (Axler exercise 2C.20) but it has a peculiar denominator-3 structure.

> [!warning] 4. Concluding "basis" from "right length, linearly independent" in a space of unknown dimension
> The length-of-basis shortcut (operation 3) is licensed only when you *already know* $\dim V$. If you do not, then a list of length $k$ might be linearly independent and still fail to span (it does not span anything beyond its own span). The standard novice error: in an exam problem of the form "prove that $v_1, \ldots, v_n$ is a basis", do not skip the spanning step unless the problem has provided $\dim V = n$ as a hypothesis. The shortcut converts spanning to a free consequence of independence, but only after $\dim V$ is on the table.

---

# Problem-Solving Strategy

Problems in §2 are won by recognising what you are being asked to do, and the recognition is mechanical once you have seen the five problem classes a few times.

If the problem **gives you a list and asks whether it is a basis**, the routine is to apply the length-of-basis shortcut — but only after you have pinned down $\dim V$. If the list's length equals $\dim V$, you only need to verify *one* of independence or spanning, whichever is easier. Spanning a known space is usually harder than independence (you would have to write every vector as a combination), so the standard route is to verify linear independence — set a generic combination to zero and show all coefficients vanish — and then invoke [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]] together with [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] to conclude. If the list's length differs from $\dim V$, then it simply *cannot* be a basis (too short to span, or too long to be independent), and the question is really asking for a counterexample.

If the problem **gives you a subspace and asks you to find a basis**, the standard recipe depends on how the subspace is described. When it is described by linear equations — for instance $U = \{(x_1, \ldots, x_5) : x_1 = 3 x_2, x_3 = 7 x_4\}$ — parametrise the solution set, with one free parameter per remaining degree of freedom, and read off a basis vector by setting each free parameter to $1$ and the rest to $0$. When the subspace is described as a span $U = \operatorname{span}(v_1, \ldots, v_m)$ but the spanning list might be redundant, run the reduction of [[Thm - Every Spanning List Contains a Basis|2.30]] from left to right. When the subspace is described abstractly (e.g. "polynomials of degree at most $n$ that vanish at $5$"), the trick is usually to *guess* the basis using a clever change of variable — $(x-5)$, $(x-5)^2$, $(x-5)^3$, ... for the example just named — and then prove linear independence by reading off coefficients of the highest power. The change of variable is the key creative step; once you have the basis it is easy to check independence and spanning.

If the problem **asks you to extend a list to a basis**, the construction is mechanical: prepend or append a known spanning list (the standard basis of $F^n$ is the all-purpose choice), and run the reduction of [[Thm - Every Spanning List Contains a Basis|2.30]]. Operation 2 is the named pattern. The construction *always* works in a finite-dimensional space; the only thing to verify is that you start with an independent list (otherwise the procedure cannot be invoked).

If the problem **gives you two subspaces and asks about their intersection or sum**, you are in [[Thm - Dimension of a Sum of Subspaces|2.43]] territory and the route is a dimension count. The crucial diagnostic is the inequality $\dim(V_1 \cap V_2) \geq \dim V_1 + \dim V_2 - \dim V$. This is operation 7, the "pigeonhole" consequence of 2.43, and it is the technique behind virtually every "show two subspaces have nontrivial intersection" problem — you simply confirm that the sum of dimensions exceeds the ambient. The same theorem, run forward, computes intersections from sums and vice versa, and it is the bridge between the abstract notion of intersection and the concrete arithmetic of dimensions.

If the problem **asks to compare two subspaces** $U \subseteq V$, the diagnostic is dimension: $\dim U \leq \dim V$ always, with equality iff $U = V$. This is the content of [[Ex - Dimension of a subspace equals dimension only if equal]]. The application is to convert a containment-and-dimension-match into an equality without computing elements directly, and it is the standard trick for showing two subspaces coincide.

The chapter's meta-strategy is: **dimension is the integer that solves linear-algebra counting problems**. Almost any question of the form "is the answer everything, or is there room to spare" reduces, in finite dimensions, to comparing two integers. This is why §2 matters out of proportion to its mathematical content: it installs an integer-valued invariant on finite-dimensional spaces that converts geometry into arithmetic.

---

# Most Reusable Properties

- **[[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|Length inequality, 2.22]]**: in any finite-dimensional space, every linearly independent list is at most as long as every spanning list. **Typical use:** this is the foundational counting fact of the chapter — every "this is too long to be independent" or "this is too short to span" argument is the length inequality applied. Reach for it the moment you need to prevent or force a list from being a basis on length grounds alone. Its compact form is the most-used single fact downstream: "in a space of dimension $n$, no list of length $> n$ is independent, no list of length $< n$ spans."

- **[[Thm - Bases are Equinumerous|2.34]] / [[Def - Dimension|Dimension]]**: the integer $\dim V$ is well-defined as the common length of all bases. **Typical use:** dimension is the numerical handle on a finite-dimensional space, and every counting argument in the rest of linear algebra reads $\dim V$ off and feeds it into an arithmetic comparison. Its most powerful use is *negative* — eliminating possibilities on dimension grounds, for instance showing two subspaces must intersect because their dimensions sum to too much.

- **[[Thm - Every Linearly Independent List Extends to a Basis|Basis extension, 2.32]]**: every linearly independent list in a finite-dimensional space extends to a basis. **Typical use:** the workhorse construction for proving "there exists a subspace $W$ such that...". Whenever you need to manufacture a complementary subspace, a coordinate system adapted to a given subspace, or a basis with a prescribed initial segment, this is the tool. It is also what makes finite-dimensional subspaces split — every short exact sequence of finite-dimensional spaces is split, a property failing in infinite dimensions.

- **[[Thm - Dimension of a Sum of Subspaces|Dimension formula, 2.43]]**: $\dim(V_1 + V_2) = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$. **Typical use:** the chapter's inclusion-exclusion. Use it both ways — forwards to compute the dimension of a sum from intersection data, backwards to deduce nontrivial intersection from dimension data. The pigeonhole consequence "$\dim V_1 + \dim V_2 > \dim V \implies V_1 \cap V_2 \neq \{0\}$" is the most-reused special case.

- **The uniqueness-of-expansion principle.** Once a basis $v_1, \ldots, v_n$ is fixed, every $v \in V$ has a *unique* tuple of coordinates $(a_1, \ldots, a_n) \in F^n$ with $v = \sum a_i v_i$. **Typical use:** this single principle is the source of the isomorphism $V \cong F^n$ (next chapter), the matrix representation of linear maps (next chapter again), and the entire computational arsenal of linear algebra. Whenever a problem talks about coordinates, components, or matrix entries, it is invoking the uniqueness-of-expansion of a chosen basis — even if the basis is not named explicitly.

---

# Bridges

1. **Module theory — a finite-dimensional vector space is a finitely generated free module over a field.** A [[Def - Module|module]] over a ring $R$ is the immediate generalisation of a vector space: replace the field $F$ in the vector-space axioms by an arbitrary (possibly non-commutative) ring $R$. The basis of a vector space becomes a **free generating set** of the module — a list whose linear combinations express every element uniquely — and a module admitting one is called **free**. The size of a free generating set, when it is well-defined, is called the **rank**. Over a field every module is free and rank is dimension; over a general ring most modules are not free, and even free modules can have ill-behaved rank (the property "every two free generating sets have the same cardinality" is **invariant basis number**, IBN, and it can fail over non-commutative rings). The chapter's main theorems specialise the module-theoretic ones: [[Thm - Bases are Equinumerous]] is the field case of IBN, and [[Thm - Every Linearly Independent List Extends to a Basis]] is the special case where projectivity of free modules degenerates to splitting of every submodule. See [[Def - Free Module]] in [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces#Bridges|the Modules subject]] for the general construction.

2. **Differential geometry — the tangent space at a point of a manifold has dimension equal to the manifold's dimension.** For a smooth $n$-manifold $M$ and a point $p \in M$, the **tangent space** $T_p M$ is a real vector space whose elements are equivalence classes of curves through $p$ (or, equivalently, derivations on the algebra of germs of smooth functions at $p$). The dimension of $T_p M$ is $n$, the dimension of $M$ — this is the *defining* property of manifold dimension, and a basis of $T_p M$ is given by the partial-derivative operators $\partial/\partial x^1, \ldots, \partial/\partial x^n$ in any coordinate chart around $p$. The bridge to our chapter is then: every theorem about dimensions of vector spaces is, at the same time, a theorem about local dimensions of manifolds. The [[Def - The Total Derivative and Differentiability|total derivative]] $Df_p : T_p M \to T_{f(p)} N$ of a smooth map between manifolds is a linear map between finite-dimensional vector spaces, and rank-nullity for it is a constraint on the local geometry of $f$.

3. **Information theory — the dimension of an empirical sample space and Shannon entropy.** A discrete random variable taking $n$ values can be encoded by its probability distribution, a vector in $\Delta_n \subseteq \mathbb{R}^n$ (the $(n-1)$-simplex). The simplex is an affine subspace of dimension $n-1$, and the entropy $H = -\sum p_i \log p_i$ is a concave function on it. When two random variables are independent the joint distribution lives in $\Delta_n \otimes \Delta_m \subseteq \mathbb{R}^{nm}$ — a tensor product (see [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]]) — and dimension multiplies. The bridge is precise: the maximum entropy of an $n$-valued variable is $\log n$, exactly the logarithm of the dimension of the support, so dimension is the *coarse* numerical handle on how complex a distribution can be. Information-theoretic results often reduce, at the coarsest level, to a dimension count.

4. **Algebraic geometry — affine varieties and Krull dimension.** An **affine variety** $V \subseteq F^n$ is the zero set of a system of polynomial equations. When the equations are linear, $V$ is a linear subspace and its dimension as a vector space is its dimension as an affine variety; when the equations are nonlinear, dimension generalises (Krull dimension of the coordinate ring) but coincides with vector-space dimension in the linear case. The bridge is that algebraic geometry's "dimension of a variety" is the right nonlinear generalisation of linear-algebra dimension, and at every smooth point $p$ of a variety the **Zariski tangent space** $T_p V$ is again a finite-dimensional vector space whose dimension equals the variety's dimension. See [[Linear Algebra IV — §3E–F Products, Quotients, Duality]] for the dual-vector-space construction that powers the cotangent space, the algebro-geometric companion of $T_p V$.

---

# Insights

**The unifying frame: a vector and its basis-expansion are two views of one object.** A vector $v \in V$ is platonic — it does not, in itself, have coordinates. Once you choose a basis $v_1, \ldots, v_n$, the *same* vector $v$ acquires a coordinate tuple $(a_1, \ldots, a_n) \in F^n$ via the unique expansion $v = \sum a_i v_i$. Change the basis and the tuple changes; the underlying vector does not. This is the platonic-vs-representation distinction made precise in linear algebra, and it is what is at stake every time you write a matrix down. The whole machinery of change-of-basis matrices in the next chapter is the bookkeeping that lets you reconcile two coordinate views of the same vector. The lesson of §2 is that the dimension $\dim V$ is intrinsic — basis-independent — while coordinate tuples are representations, basis-dependent. Confusing the two is the most persistent novice error in linear algebra.

**The true name of dimension is "the unique integer that all bases share".** The textbook definition — "$\dim V$ is the length of any basis" — is not motivating; it is a consequence of [[Thm - Bases are Equinumerous|2.34]], which is the substantive theorem. The point is that *all* bases share that integer, so it is an invariant of $V$ alone. Operationally this means: whenever you want to know $\dim V$, *any* basis will do — you do not have to find a clever one. And whenever you have a list of length $\dim V$, you are halfway to having a basis. The bidirectional move — "$\dim V$ is the length of every basis" and "any list of length $\dim V$ is half a basis" — is the chapter's engine.

**A trigger-reaction pattern catalogue.** "See a list of $n$ vectors in an $n$-dimensional space $\to$ check spanning *or* independence, not both." "Want to extend a list to a basis $\to$ concatenate the standard basis on the right, apply [[Thm - Every Spanning List Contains a Basis|2.30]]." "Want to count linear dependencies among $v_1, \ldots, v_m \to$ compute $m - \dim \operatorname{span}(v_1, \ldots, v_m)$." "Two subspaces summing to more than the ambient dimension $\to$ nontrivial intersection." "Three subspaces of dimension $> 2 \dim V / 3 \to$ nontrivial triple intersection (LADR 2C.15)." Each of these reactions takes one sentence to state and saves minutes of computation when invoked correctly.

**Inheritance: where do bases come from?** The chapter constructs bases by two converging methods — reduce a spanning list (2.30) or extend an independent list (2.32) — and the existence of bases for *every* finite-dimensional space (2.31) follows from the definition of finite-dimensionality together with 2.30. But where does the *first* spanning list come from? In every concrete example we have used in this chapter, the spanning list is *built into the definition* of the space: $F^n$ is defined as tuples and so has the standard basis by inspection; $\mathcal{P}_m(F)$ is defined as a degree-bounded polynomial space and so has $1, z, \ldots, z^m$ by inspection; a subspace defined by linear equations has its spanning list read off the parametric solution. The chapter does not give a recipe for finding a spanning list in the abstract — it only gives a recipe for refining one. The art of doing concrete linear algebra is therefore largely about choosing the *right* spanning list, and this is where most of the cleverness in §2 problems is concentrated.

**The Steinitz exchange is the engine.** Every counting theorem in this chapter rests on [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]], and 2.22 itself rests on a single exchange-and-replace procedure: feed the independent vectors $u_i$ into the spanning list one at a time, swap out a spanning vector at each step, and observe that independence prevents the procedure from running out of $w$'s prematurely. Ernst Steinitz published this argument in 1913, and it generalises far beyond vector spaces — to matroids, to dependence relations on sets, to model-theoretic pregeometries. The lesson worth carrying away from the chapter is that the abstract pattern "two notions of dependence agree on their cardinality" is robust: anywhere you have a closure operator with the exchange property, you have a notion of dimension and Steinitz works. The vector-space case is one instance of a deep structural fact, and the careful proof in §2A is the model proof in the general theory.

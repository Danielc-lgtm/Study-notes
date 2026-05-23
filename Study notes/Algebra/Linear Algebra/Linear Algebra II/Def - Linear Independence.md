---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Linear Combination and Span"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over a field $F$, and $v_1, \ldots, v_m$ is a list (finite, ordered) of vectors in $V$. The full notation registry is on the parent page [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]. The convention is that the empty list is linearly independent.

---

# Axiom Motivation

The notion is forced by a question raised the moment we have spans: when we write a vector $v$ as $a_1 v_1 + \cdots + a_m v_m$, is the choice of coefficients $a_i$ unique? If yes, then the list $v_1, \ldots, v_m$ installs *coordinates* on $\operatorname{span}(v_1, \ldots, v_m)$ — every vector in the span is faithfully recorded by its tuple of coefficients. If no, then the same vector has multiple coefficient tuples, and the list overcounts. Almost every later theorem in linear algebra — the matrix representation of linear maps, the change-of-basis formulas, the [[Def - Dimension|dimension]] formula — requires uniqueness of expansion. The question is therefore central, and **linear independence** is exactly the condition that answers it positively.

Here is the derivation. Suppose $v_1, \ldots, v_m$ is a list, and $v$ has two expansions
$$v = a_1 v_1 + \cdots + a_m v_m = c_1 v_1 + \cdots + c_m v_m.$$
Subtracting:
$$0 = (a_1 - c_1) v_1 + \cdots + (a_m - c_m) v_m.$$
So *two* expansions of one vector exist if and only if *the zero vector* has a non-trivial expansion: if and only if some nontrivial linear combination of $v_1, \ldots, v_m$ equals $0$. Conversely, uniqueness of expansion is equivalent to the trivial-combination condition: the only way to write $0 = a_1 v_1 + \cdots + a_m v_m$ is with all $a_i = 0$. This single equation — "the trivial expansion is the only expansion of $0$" — is what we are forced to require. There is no other definition we could choose if we want unique coordinates.

The definition has one axiom, so the per-axiom failure question is "what if we drop the only-trivial-expansion clause"? The answer: we get the unrestricted condition "any list of vectors", which is vacuously satisfied by every list and so carries no content. The clause is exactly the bite of the definition. A more interesting failure-mode question is: what if we weakened "only trivial expansion of $0$" to "no expansion of $0$ uses *all* coefficients nonzero"? This would be too weak — for example $(1, 0), (0, 0), (0, 1)$ in $F^2$ satisfies this weakened version (no combination with all three coefficients nonzero can equal zero, because of the middle vector) but is plainly redundant, since $(0, 0)$ is the zero vector and so any list containing it should be considered "dependent". The standard definition correctly excludes lists containing $0$, by allowing the *single-vector* combination $1 \cdot 0 = 0$ as a nontrivial combination of the list.

Equally instructive is the **operational reformulation** in terms of redundancy. A list $v_1, \ldots, v_m$ is **linearly dependent** (the negation of independent) when some non-trivial combination vanishes, which by the linear dependence lemma is equivalent to: *some $v_k$ lies in the span of the others*. This is the manipulable form: linear dependence means one vector is reachable from the others — it is *redundant*. Linear independence means none is redundant. Both formulations are useful and the reader should hold both in mind: the official definition (only trivial expansion of $0$) for verifying independence in computations, the operational form (no vector is a combination of the others) for thinking about what independence *means*.

The convention that the **empty list is linearly independent** is forced for coherence. Vacuously, the empty list has no non-trivial combinations to consider; the only combination is the empty sum, which is $0$ by convention, and the coefficient list is empty so "all coefficients zero" is vacuously satisfied. The convention is what makes statements like "every linearly independent list extends to a basis" hold without exceptions, including for the empty list which extends to a basis of $V$ from scratch.

Finally, a word on the role of the field. Linear independence depends on which field we work over. The list $(1+i), (1-i)$ in $\mathbb{C}$ is linearly *dependent* when $\mathbb{C}$ is viewed as a complex vector space (because $i \cdot (1-i) = i + 1 = (1+i)$, so they are scalar multiples) but linearly *independent* when $\mathbb{C}$ is viewed as a real vector space (no real scalar relates them). The same is true in any vector space whose scalar field is enriched — restricting scalars makes independence easier to lose. This is the cleanest reminder that "linear" in linear algebra is always relative to a field.

---

# The Definition

A list $v_1, \ldots, v_m$ of vectors in $V$ is **linearly independent** if the only solution of
$$a_1 v_1 + a_2 v_2 + \cdots + a_m v_m = 0 \qquad (a_i \in F)$$
is $a_1 = a_2 = \cdots = a_m = 0$. The empty list is linearly independent by convention.

A list that is not linearly independent is **linearly dependent**: some choice of $a_1, \ldots, a_m \in F$, not all zero, satisfies $a_1 v_1 + \cdots + a_m v_m = 0$.

**Equivalent operational form (LADR 2.15, paragraph after).** A list is linearly independent if and only if every vector in $\operatorname{span}(v_1, \ldots, v_m)$ has a *unique* representation as a linear combination of $v_1, \ldots, v_m$.

**Equivalent operational form (linear dependence lemma, LADR 2.19).** A list of length $\geq 1$ is linearly dependent if and only if some $v_k$ lies in $\operatorname{span}(v_1, \ldots, v_{k-1})$; moreover, removing this $v_k$ does not change the span.

---

# Relate to Other Fields / Compression

Linear independence is the linear-algebra incarnation of **non-redundancy** in a generating set. Whenever you have a generating set for a structure — vectors generating a subspace, group elements generating a subgroup, ring elements generating an ideal — you can ask whether any element of the set is reachable from the others; if so, the set is redundant. In linear algebra this question has a uniquely clean answer because the field operations are *invertible*: if $v_k$ is reachable, you can solve for it explicitly. In group or ring theory, generation by combinations of operations and inverses is more complicated, and a clean concept of "independent generating set" is much harder to pin down — see the theory of **free groups** and **free modules** for the analogues.

**True name:** "uniqueness of expansion of every vector in the span." The textbook definition uses the trivial-expansion-of-zero condition because it is the cleanest computational form. The operational meaning — and the reason the concept matters — is unique expansion. When you read "linearly independent" in a problem, translate it as "every vector in the span has a unique coefficient tuple", and you will know immediately what the assumption buys you.

A second compression: linear independence is the **kernel-triviality** of the linear map $F^m \to V$ defined by $(a_1, \ldots, a_m) \mapsto a_1 v_1 + \cdots + a_m v_m$. This map is always well-defined and linear; its image is $\operatorname{span}(v_1, \ldots, v_m)$, and its kernel is exactly the set of coefficient tuples giving the zero combination. Linear independence is the statement that this kernel is trivial (only the zero tuple). This connects the chapter to the next: linear independence is one half of "the standard coordinate map $F^m \to V$ is injective", and spanning is one half of "it is surjective". A basis is one giving both — an isomorphism.

---

# Examples / Corollaries

**Example (the standard list in $F^n$).** The standard basis $e_1, \ldots, e_n$ of $F^n$ is linearly independent. Any combination $a_1 e_1 + \cdots + a_n e_n$ equals $(a_1, \ldots, a_n)$, which is zero only when all $a_i = 0$.

**Example (polynomials $1, z, z^2, \ldots, z^m$).** This list in $\mathcal{P}_m(F)$ is linearly independent. Suppose $a_0 + a_1 z + \cdots + a_m z^m = 0$ as a polynomial; then it vanishes as a function at every $z \in F$, and (for $F$ infinite — true in our standing assumption $F \in \{\mathbb{R}, \mathbb{C}\}$) a nonzero polynomial of degree at most $m$ has at most $m$ roots, so the only polynomial vanishing at every $z$ is the zero polynomial. Hence all $a_i = 0$.

**Example (a list of length two).** A two-vector list $v_1, v_2$ is linearly independent if and only if neither vector is a scalar multiple of the other. (For length one: $v_1$ is independent if and only if $v_1 \neq 0$.)

**Example (the difference list).** If $v_1, \ldots, v_n$ is linearly independent in $V$, then so is $v_1 - v_2, v_2 - v_3, \ldots, v_{n-1} - v_n, v_n$. (Exercise: write a generic linear combination of the differences, expand, collect by $v_i$, use independence of the original list to force all coefficients zero.)

**Non-example (a list containing zero).** Any list containing the zero vector is linearly dependent. The combination $1 \cdot 0 = 0$ is non-trivial (its coefficient is $1 \neq 0$), so the trivial-expansion-of-zero condition fails.

**Non-example (three vectors in a plane).** In $\mathbb{R}^3$, the list $(1, 0, 0), (0, 1, 0), (1, 1, 0)$ is linearly dependent: $(1, 1, 0) = (1, 0, 0) + (0, 1, 0)$, so $(1, 0, 0) + (0, 1, 0) - (1, 1, 0) = 0$ is a nontrivial vanishing combination. The list spans the $xy$-plane (a 2-dimensional [[Def - Subspace|subspace]]), and three vectors in a 2-dimensional space cannot be independent.

**Non-example (depends on the field).** The list $1+i, 1-i$ in $\mathbb{C}$. Viewed as $\mathbb{R}$-vector space, this is independent: a real combination $a(1+i) + b(1-i) = (a+b) + (a-b)i = 0$ forces $a + b = 0$ and $a - b = 0$, so $a = b = 0$. Viewed as $\mathbb{C}$-vector space, this is dependent: the combination $i \cdot (1-i) + (-1) \cdot (1+i) = (i + 1) - 1 - i = 0$ is nontrivial. Restricting the scalar field can convert dependence into independence — never the other way around.

**Corollary (sublist independence).** If $v_1, \ldots, v_m$ is linearly independent, so is any sublist obtained by deleting some entries. (Any vanishing combination of the sublist is a vanishing combination of the full list with the missing coefficients set to zero, forcing all coefficients in the sublist to be zero.)

**Corollary (no two equal entries).** A linearly independent list has all distinct vectors. If $v_i = v_j$ for $i \neq j$, the combination $1 \cdot v_i + (-1) \cdot v_j = 0$ is non-trivial.

**Corollary (extending by an outside vector preserves independence).** If $v_1, \ldots, v_m$ is independent and $w \notin \operatorname{span}(v_1, \ldots, v_m)$, then $v_1, \ldots, v_m, w$ is independent. (Indeed, suppose $a_1 v_1 + \cdots + a_m v_m + b w = 0$; if $b \neq 0$ then $w = -b^{-1}(a_1 v_1 + \cdots + a_m v_m) \in \operatorname{span}(v_1, \ldots, v_m)$, contradiction; so $b = 0$, and then $a_i = 0$ by independence of the original list.) This is the construction used implicitly in [[Thm - Every Linearly Independent List Extends to a Basis|every-independent-extends-to-basis]] and in the greedy construction for [[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|subspace finite-dimensionality]].

**Calibration check.** If you have understood linear independence, you should be able to verify quickly: (a) any list of length $\geq 2$ containing two equal vectors is dependent; (b) any list containing the zero vector is dependent; (c) a list of length 1 is independent iff its only vector is nonzero; (d) a list whose span is properly larger than each smaller sub-span (no vector in the span of its predecessors) is independent — the iterative form of the definition.

---

# Unlocked by This

> [!tip] Affine Independence *(from Affine Geometry, Loehr Ch 11)*
> Points $p_0, p_1, \ldots, p_m$ in $F^n$ are called **affinely independent** if the vectors $p_1 - p_0, p_2 - p_0, \ldots, p_m - p_0$ are linearly independent — that is, if no point is in the affine hull of the others. The affine hull of $m+1$ affinely independent points is an $m$-dimensional **affine flat**, and the convex hull is an **$m$-simplex**. Affine independence is the right notion when the origin is not privileged: linear independence is affine independence of $0, v_1, \ldots, v_m$. This is the language of simplicial complexes, barycentric coordinates, and convex polytopes.

> [!tip] Matroid Independence *(from Combinatorics)*
> The properties of linear independence — that the empty list is independent, that sublists of independent lists are independent, and the **exchange property** (if $|A| < |B|$ are both independent, some element of $B$ extends $A$) — are abstracted in the definition of a **matroid**. Matroids generalise the notion of "independence" to settings where there are no vectors at all: graphic matroids encode acyclic edge sets of a graph, transversal matroids encode partial matchings, algebraic matroids encode algebraic independence in field extensions. The Steinitz exchange property [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|of §2A]] is precisely the matroid exchange property in disguise, and the proof of well-definedness of dimension generalises to a proof of well-definedness of matroid **rank**.

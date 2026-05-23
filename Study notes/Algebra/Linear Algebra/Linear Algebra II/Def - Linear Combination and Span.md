---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
tags: [algebra, linear-algebra]
---

# Notation

We work over a fixed field $F$ (read $\mathbb{R}$ or $\mathbb{C}$ on first pass), and $V$ denotes a vector space over $F$. A **list** is a finite ordered tuple $v_1, \ldots, v_m$ of vectors in $V$; we permit $m = 0$, the empty list. The span of a list is denoted $\operatorname{span}(v_1, \ldots, v_m)$. The full notation registry for this chapter is on the parent page [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

This is a compound page: it defines two interlocking notions — **linear combination** and **span** — because they are introduced together and neither is fully usable without the other.

---

# Axiom Motivation

A vector space lets us *add* vectors and *multiply them by scalars*. Once we have these two operations the simplest non-trivial thing to do is to repeat them: form $a_1 v_1$ and $a_2 v_2$ and add the results to get $a_1 v_1 + a_2 v_2$, and more generally form $a_1 v_1 + a_2 v_2 + \cdots + a_m v_m$ for any choice of scalars $a_i$ and any list $v_1, \ldots, v_m$ of vectors. There is no separate axiom needed to license this — the closure axioms of a vector space already guarantee that the result is in $V$. The point of defining **linear combination** as a named concept is just that this particular kind of expression — additive in the vectors, with arbitrary scalar weights — is exactly the kind we care about. Other expressions you could build, like $v_1 \cdot v_2$ (a hypothetical "product of vectors"), are not part of the vector-space structure and have no reason to make sense.

The motivation for **span** is the question "what is the smallest [[Def - Subspace|subspace]] of $V$ containing the vectors $v_1, \ldots, v_m$?" The set of vectors $\{v_1, \ldots, v_m\}$ on its own is generally *not* a subspace — it is not closed under addition or scalar multiplication. To make it into a subspace you must throw in $a_1 v_1$ for all $a_1 \in F$, then sums of those, then sums of *those* with scalar multiples of $v_2$, and so on. What you eventually end up with is exactly the set of all linear combinations. This is the span. The point of the definition is twofold: it gives the closure of $\{v_1, \ldots, v_m\}$ under the vector-space operations a name, and it does so by an explicit constructive formula rather than by abstract "intersection of all containing [[Def - Subspace|subspaces]]".

The convention $\operatorname{span}() = \{0\}$ for the empty list deserves a moment. The empty sum is the additive identity, $0$, by the standard convention; an empty linear combination has no terms but is still well-defined as $0$. The empty list's span is therefore the trivial subspace $\{0\}$, which is the smallest subspace of $V$ — exactly what "smallest subspace containing every vector in the empty list" should be. Like many empty-case conventions, this one is forced: the set of linear combinations grows monotonically as the list grows, and the only way for the convention to be coherent with that monotonicity is to put $\{0\}$ at the bottom.

There is no second axiom to fail-test here because the definition is not multi-axiomatic — it is a single positive construction. The question to ask is instead: why is this particular construction useful, and what would go wrong if we replaced it with something nearby? Suppose we restricted linear combinations to use *only positive scalars* — call those positive combinations. The set of positive combinations is *not* a subspace in general (it is a convex cone), and we would have lost the symmetry of the vector-space operations. Suppose we allowed *infinite* linear combinations: $a_1 v_1 + a_2 v_2 + \cdots$ with infinitely many $a_i \neq 0$. Then we would need a notion of convergence and a topology on $V$, which a bare vector space does not have. The finite-combination definition is the right one for purely algebraic linear algebra; the infinite-combination version belongs to functional analysis, where it requires Banach- or Hilbert-space structure to be meaningful. The wording "list", finite by definition, is the exact technical device that keeps us inside algebra.

The two definitions interlock as follows: **a list spans $V$** when $\operatorname{span}(v_1, \ldots, v_m) = V$, that is, when every vector of $V$ is some linear combination of the list. This brings us back to the chapter's animating question: which lists are "big enough" to reach every vector of $V$? When such a list exists with finite length, $V$ is called [[Def - Finite-Dimensional Vector Space|finite-dimensional]], and the whole structure theory of §2 begins.

---

# The Definition

**Linear combination.** A **linear combination** of a list $v_1, \ldots, v_m$ of vectors in $V$ is a vector of the form
$$a_1 v_1 + a_2 v_2 + \cdots + a_m v_m, \qquad a_1, \ldots, a_m \in F.$$
The scalars $a_i$ are called the **coefficients** of the combination. The empty list's only linear combination is the empty sum, $0$.

**Span.** The **span** of a list $v_1, \ldots, v_m$ in $V$ is the set of all linear combinations:
$$\operatorname{span}(v_1, \ldots, v_m) = \{a_1 v_1 + \cdots + a_m v_m : a_1, \ldots, a_m \in F\}.$$
For the empty list, $\operatorname{span}() = \{0\}$.

A list **spans** $V$ when $\operatorname{span}(v_1, \ldots, v_m) = V$.

**Key proposition** (LADR 2.6). $\operatorname{span}(v_1, \ldots, v_m)$ is the smallest [[Def - Subspace|subspace]] of $V$ containing every $v_i$. In particular, it is itself a subspace.

---

# Relate to Other Fields / Compression

The span is the **closure operator** for the vector-space structure: the smallest subspace containing a given list of vectors. The same idea, with "subspace" replaced by other closure conditions, recurs throughout algebra. In group theory the subgroup *generated by* a subset is the smallest subgroup containing it; in ring theory the ideal *generated by* a subset is the smallest ideal containing it. The span is the linear-algebra incarnation of this universal pattern. The constructive form — "all finite linear combinations" — is also universal: the subgroup generated by a set is all finite products of elements and their inverses, the ideal generated by a set is all finite sums of multiples of the elements, and so on.

**True name (of span):** "the set of vectors reachable from the list via the vector-space operations." The textbook definition gives a formula; the operational meaning is reachability. Whenever a problem asks whether some specific vector is in the span of a list, the question is exactly "can I get there from here using only additions and scalar multiplications" — and concretely this almost always reduces to solving a linear system in the coefficients.

---

# Examples / Corollaries

**Example (linear combination in $\mathbb{R}^3$).** $(17, -4, 2)$ is a linear combination of the list $(2, 1, -3), (1, -2, 4)$ because
$$6 \cdot (2, 1, -3) + 5 \cdot (1, -2, 4) = (17, -4, 2).$$
The coefficients are $a_1 = 6, a_2 = 5$.

**Non-example (not a linear combination).** $(17, -4, 5)$ is *not* a linear combination of the same list. To check, one would have to solve
$$\begin{cases} 17 = 2 a_1 + a_2 \\ -4 = a_1 - 2 a_2 \\ 5 = -3 a_1 + 4 a_2 \end{cases}$$
for $a_1, a_2 \in \mathbb{R}$. The first two equations force $a_1 = 6, a_2 = 5$, but then $-3(6) + 4(5) = 2 \neq 5$. So no solution exists.

**Example (the standard span of $F^n$).** The list
$$e_1 = (1, 0, \ldots, 0), \quad e_2 = (0, 1, 0, \ldots, 0), \quad \ldots, \quad e_n = (0, \ldots, 0, 1)$$
spans $F^n$, since any $(x_1, \ldots, x_n) = x_1 e_1 + \cdots + x_n e_n$. This is the prototypical spanning list; it is also linearly independent (next page) and so a basis.

**Example (span of polynomials).** $\operatorname{span}(1, z, z^2, \ldots, z^m) = \mathcal{P}_m(F)$, the polynomials of degree at most $m$. The full space $\mathcal{P}(F)$ is *not* the span of any finite list, by an easy degree argument (the highest degree of any polynomial in a finite list bounds the degrees of everything in its span).

**Example (span of a single nonzero vector).** $\operatorname{span}(v) = \{a v : a \in F\}$, the *line through the origin* in direction $v$. It is 1-dimensional. The span of a list of two non-parallel vectors in $\mathbb{R}^3$ is a *plane* through the origin.

**Corollary (span is a subspace).** $\operatorname{span}(v_1, \ldots, v_m)$ is closed under addition and scalar multiplication. Indeed
$$\left(\sum a_i v_i\right) + \left(\sum c_i v_i\right) = \sum (a_i + c_i) v_i, \qquad \lambda \left(\sum a_i v_i\right) = \sum (\lambda a_i) v_i,$$
both of which are again linear combinations of the same list.

**Corollary (span is the smallest containing subspace).** Any subspace $U$ of $V$ containing every $v_i$ must contain every $a_1 v_1 + \cdots + a_m v_m$ (by closure of $U$ under the vector-space operations), so $\operatorname{span}(v_1, \ldots, v_m) \subseteq U$. Combined with the previous corollary — span is *itself* a subspace containing the $v_i$ — this shows that span is the unique smallest such subspace.

**Corollary (adding a redundant vector does not change the span).** If $v \in \operatorname{span}(v_1, \ldots, v_m)$, then $\operatorname{span}(v_1, \ldots, v_m, v) = \operatorname{span}(v_1, \ldots, v_m)$. The inclusion $\supseteq$ is trivial; for $\subseteq$, write $v = \sum b_i v_i$ and substitute into any combination involving $v$.

**Corollary (linear dependence lemma, LADR 2.19).** If $v_1, \ldots, v_m$ is *linearly dependent* (see [[Def - Linear Independence]]), then some $v_k$ lies in $\operatorname{span}(v_1, \ldots, v_{k-1})$, and removing $v_k$ from the list does not change the span. This is the engine of the chapter's structural theorems: dependence equals removable redundancy.

**Calibration check.** If you have understood span, you should be able to verify in roughly a minute: (a) $\operatorname{span}((1, 1), (2, 2)) = \operatorname{span}((1, 1)) \subsetneq \mathbb{R}^2$ (the second vector is redundant, and the span is a line); (b) the span of any two non-parallel vectors in $\mathbb{R}^2$ is all of $\mathbb{R}^2$; (c) the span of $(1, 2), (3, 6)$ in $F^2$ is the line $\operatorname{span}((1, 2))$, not all of $F^2$.

---

# Unlocked by This

> [!tip] Generating Set *(from Group Theory and Ring Theory)*
> The span is the linear-algebra analogue of the **generating set** in group theory and ring theory. For a subset $S \subseteq G$ in a group, $\langle S \rangle$ is the smallest subgroup containing $S$, given constructively as the set of all finite products of elements of $S$ and their inverses; for $S \subseteq R$ in a ring, the **ideal generated by $S$** is the smallest ideal containing $S$. In each case there is an explicit constructive description (finite combinations using the field operations / group operation / ring operations) and an abstract universal-property description ("smallest substructure containing $S$"). Linear algebra is the cleanest instance because the field forces uniqueness conditions that fail in the general case — see [[Def - Linear Independence]] and [[Def - Basis]].

> [!tip] Closure Operator *(from Order Theory and Topology)*
> The map $S \mapsto \operatorname{span}(S)$ on the lattice of subsets of $V$ is a **closure operator**: it is monotone, extensive (every set is contained in its closure), and idempotent (the closure of a closure is itself). Closure operators are studied abstractly in order theory, and they govern topological closure, algebraic closure, convex closure, and many other constructions. The Steinitz exchange property of span (linear dependence allows replacement) is a *special* feature not shared by all closure operators; closure operators with this property generate the theory of **matroids**, where Steinitz's argument generalises and dimension makes sense in much greater generality than vector spaces.

---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Linear Combination and Span"
  - "Def - Linear Independence"
  - "Def - Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over $F$, with a finite spanning list $v_1, \ldots, v_n$. The full notation registry is on the parent topic page [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

---

# Statement

> **Theorem (LADR 2.30).** Every spanning list in a vector space can be reduced to a basis of that space by deleting some (possibly zero) of its entries.

> **Corollary (LADR 2.31).** Every finite-dimensional vector space has a basis.

The reduction is by an explicit greedy algorithm — for each entry, in left-to-right order, delete it if it lies in the span of the previous entries. The surviving sublist is a basis.

---

# Motivation

The theorem answers a structural question: are spanning lists "near" bases, or potentially very far from them? Concretely, given a list $v_1, \ldots, v_n$ that spans $V$ but might be highly redundant — many of the $v_i$ might be linear combinations of the others — can we always cut it down to a basis, and if so by what procedure? The answer is yes, by a simple greedy reduction, and the algorithm is explicit and constructive.

The result is the easier of the two structural building blocks of the chapter. Its dual is [[Thm - Every Linearly Independent List Extends to a Basis|every linearly independent list extends to a basis]] — which says, dually, that independent lists are "near" bases. Together these say bases are the **meeting point** of two converging operations: reduce a spanning list down, or extend an independent list up. Both procedures terminate at the same place, the basis. The chapter's main quantitative theorems then drop out: the length is the same in both procedures, and this is the well-definedness of dimension.

The proof is constructive: it gives an algorithm, not merely an existence statement. This matters because almost every problem of the form "find a basis of $V$" in §2 is solved by running this reduction on a known spanning list. The standard recipe is: spawn the largest spanning list you can — often the concatenation of the standard basis with whatever else you have — and reduce.

The corollary about existence of bases is a one-line consequence: by definition a finite-dimensional space has a finite spanning list, and the theorem reduces it to a basis.

---

# Sources and Targets

**Sources (Input Broadening).**

The hypothesis is *a spanning list*. The skill is recognising when a problem hands you one even if it does not advertise it as such.

A first source is **a list whose span includes everything needed**. Property $B$: "you have a list and have already established that every relevant vector is reachable from it." The bridge: that is exactly what spanning means. The trick is that "spanning" is often re-phrased in problems as "every $v \in V$ is a linear combination of $v_1, \ldots, v_n$", or "$V = \operatorname{span}(v_1, \ldots, v_n)$", or "the list generates $V$". Recognising these as instances of "spanning list" is the work.

A second source is **a finite-dimensional space and any old basis of an ambient space**. Property $B$: "you have a basis of $\mathbb{R}^n$ (or $F^n$) and want a basis of a subspace, or of $\mathbb{R}^n$ adapted to a subspace." The bridge: the standard basis of $\mathbb{R}^n$ is a spanning list of $\mathbb{R}^n$, which gives a spanning list of any subspace's containing space; concatenating with vectors of the subspace gives a long spanning list to reduce. This source is the engine of every "find a basis of $V$" problem.

A third source is **a list known to span a subspace, with redundancy expected**. Property $B$: "you have a list $v_1, \ldots, v_m$ describing some subspace $U$ as $U = \operatorname{span}(v_1, \ldots, v_m)$, but the $v_i$ might not be independent." The bridge: $v_1, \ldots, v_m$ is a spanning list of $U$, and the theorem reduces it to a basis of $U$. This is the standard form of "find a basis" problems where the subspace is given parametrically — first parametrise and get the spanning list, then reduce.

A fourth source is **a union of two spanning sets giving a spanning list of the sum**. Property $B$: "you have spanning lists of two subspaces $V_1$ and $V_2$." The bridge: concatenating gives a spanning list of $V_1 + V_2$ (any vector in $V_1 + V_2$ is a sum of one from each, reachable from the concatenated list). Reducing gives a basis of $V_1 + V_2$. This is the source behind [[Thm - Dimension of a Sum of Subspaces|2.43]]'s setup.

**Targets (Output Amplification).**

The theorem produces a sublist that is a basis. Combined with one further fact, this yields structural conclusions.

A first combination is **plus equality of lengths forces no reduction**. If the spanning list has length exactly $\dim V$, the basis it reduces to *also* has length $\dim V$ (by [[Thm - Bases are Equinumerous|2.34]]), so the reduction deletes zero vectors and the original list was already a basis. This is the "spanning + right length = basis" shortcut, Corollary 3 of 2.22.

A second combination is **plus the linear dependence lemma identifies the deleted vectors**. The reduction proceeds by deleting the entries that lie in the span of the previous ones. These are exactly the redundant vectors — those whose removal does not change the span. The deleted vectors are *not arbitrary*: they are the vectors that the linear dependence lemma identifies. So the theorem's algorithm is *deterministic* given a fixed order on the list. In exercises like [[Ex - Removing redundancy from a linearly dependent list]] this means we can pinpoint exactly which vectors are redundant.

A third combination is **plus the dimension formula 2.43 to compute dimensions of sums**. Apply the theorem to the concatenated spanning list of $V_1 + V_2$, deleting redundancies; the basis it produces has length $\dim(V_1 + V_2)$. Combined with knowledge of the bases of $V_1$ and $V_2$, this is one of the proofs of 2.43.

A fourth combination is **plus an existence-of-spanning hypothesis to existence of bases**. The corollary "every finite-dimensional space has a basis" follows from the theorem applied to any finite spanning list. This is what licenses the existence-of-bases claim in [[Def - Dimension]].

---

# Why Is It True

The intuition is **redundancy is removable, and the linear dependence lemma identifies which vectors are redundant**.

A spanning list is a list whose span is $V$ — but the list may carry redundant vectors, vectors that can be expressed in terms of others in the list. When such a redundancy is present, you can *throw it away*: removing the redundant vector does not change the span. So you can repeatedly delete redundancies, and the list keeps spanning $V$. When no more redundancies are present, the list is linearly independent (by the definition of independence as "no vector is a combination of the others"), and it still spans, so it is a basis.

The bolded one-liner: **deletion of redundancies preserves the span, and when no redundancies remain the list is automatically independent — so the reduction terminates exactly at a basis**.

The mechanism for identifying redundancies is the [[Def - Linear Combination and Span|linear dependence lemma]]: in any linearly dependent list, *some* vector is in the span of the previous ones, and that vector is the redundant one. The reduction algorithm scans left-to-right and deletes each entry that lies in the span of its predecessors. At termination, no entry lies in the span of its predecessors — but this is exactly the condition for linear independence (iteratively: the first vector is nonzero, the second is not a scalar multiple of the first, the third is not in the plane spanned by the first two, ...).

Two subtle points are worth flagging. First, the procedure is **constructive** — given a basis-checking procedure (decide whether $v_k \in \operatorname{span}(v_1, \ldots, v_{k-1})$ — a linear system), it actually computes the basis from the spanning list. In practice this is row-reduction. Second, the procedure depends on the order: different orderings of the input list can produce different (but equinumerous) bases. The choice of which vector to declare "redundant" is biased toward those appearing later, which is a feature of the left-to-right reduction.

---

# What Makes This Hard

The proof is a one-shot greedy argument, but two subtleties are worth noting. First, the **iterative definition of linear independence** — a list is independent iff no entry is in the span of the previous ones — is the form needed to make the reduction work cleanly. Students sometimes use the "all coefficients zero" form, which is less directly suited to the proof.

Second, the **claim that the reduction terminates with an independent list** requires unpacking. After deletion, the surviving sublist has the property that no entry is in the span of its predecessors *as ordered in the original list*. The reduction is one-pass, left-to-right, deciding each entry's fate based on what has survived so far. After the pass, the surviving sublist has the iterative independence property; using the equivalence with the standard definition, it is linearly independent. Multi-pass or backtracking versions of the algorithm exist but are unnecessary.

A third common point of confusion: the reduction *can* end up with the empty list. If the original spanning list consisted entirely of redundant vectors — for instance, all zero — then all entries are deleted, and the resulting "basis" is the empty list, which spans $\{0\}$. This is consistent only when the space being spanned is $\{0\}$.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:** Run a left-to-right pass through the spanning list, deleting each entry that lies in the span of its predecessors. The deletions do not change the span (by the linear dependence lemma's converse direction), and the surviving sublist has the iterative no-vector-in-predecessor-span property, which is equivalent to linear independence.

**Subgoal decomposition:**

1. **Define the algorithm.** Set $B = (v_1, v_2, \ldots, v_n)$ initially. For $k = 1, \ldots, n$, examine the $k$-th entry. If it is in the span of the entries preceding it *in the current list $B$*, delete it; otherwise, keep it.
   - *Hint:* The order is preserved, just some entries are deleted.
   - *Why needed:* The algorithm gives an explicit construction of the basis.

2. **Verify span is preserved at each step.** When an entry is in the span of its predecessors, the linear dependence lemma says removing it does not change the span.
   - *Hint:* This is the second part of [[Def - Linear Combination and Span|the linear dependence lemma]].
   - *Why needed:* This ensures the surviving sublist still spans $V$.

3. **Verify the surviving sublist is linearly independent.** After the pass, no entry of $B$ is in the span of the entries preceding it in $B$. By the iterative form of independence, this is exactly linear independence.
   - *Hint:* The iterative form: $v_1 \neq 0$ (if it were, it would have been deleted because $0 \in \operatorname{span}() = \{0\}$); $v_2$ not a scalar multiple of $v_1$ (else it would have been deleted); etc.
   - *Why needed:* Independence + spanning = basis.

4. **Conclude $B$ is a basis.** $B$ spans $V$ (by Step 2 repeated $n$ times) and is linearly independent (by Step 3), so it is a basis of $V$ by definition.

---

# Lemma Decomposition

> [!note]- Lemma 1: Removing a vector in the span of the others preserves the span
> **Statement:** If $v_k \in \operatorname{span}(v_1, \ldots, v_{k-1}, v_{k+1}, \ldots, v_n)$, then deleting $v_k$ from the list does not change the span: $\operatorname{span}(v_1, \ldots, v_n) = \operatorname{span}(v_1, \ldots, v_{k-1}, v_{k+1}, \ldots, v_n)$.
>
> **Hint:** The $\supseteq$ inclusion is trivial. For $\subseteq$, substitute $v_k$'s expansion into any combination using $v_k$.
>
> **Why needed:** This is what ensures each deletion in the reduction preserves the span $V$.
>
> > [!note]- Full proof
> > The inclusion $\operatorname{span}(v_1, \ldots, v_{k-1}, v_{k+1}, \ldots, v_n) \subseteq \operatorname{span}(v_1, \ldots, v_n)$ is immediate (any combination of a sublist is a combination of the full list with the missing coefficient set to zero).
> >
> > For the reverse inclusion, write $v_k = b_1 v_1 + \cdots + b_{k-1} v_{k-1} + b_{k+1} v_{k+1} + \cdots + b_n v_n$. Any element of $\operatorname{span}(v_1, \ldots, v_n)$ is of the form $a_1 v_1 + \cdots + a_n v_n$; substitute the expansion for $v_k$:
> > $$a_1 v_1 + \cdots + a_k (b_1 v_1 + \cdots + b_n v_n) + \cdots + a_n v_n.$$
> > Collecting terms, this is a combination of $v_1, \ldots, v_{k-1}, v_{k+1}, \ldots, v_n$ alone. Hence $\operatorname{span}(v_1, \ldots, v_n) \subseteq \operatorname{span}(v_1, \ldots, v_{k-1}, v_{k+1}, \ldots, v_n)$.

> [!note]- Lemma 2: A list is linearly independent iff no entry lies in the span of its predecessors
> **Statement:** A list $v_1, \ldots, v_n$ is linearly independent if and only if for every $k \in \{1, \ldots, n\}$, $v_k \notin \operatorname{span}(v_1, \ldots, v_{k-1})$ (with $\operatorname{span}() = \{0\}$).
>
> **Hint:** ($\Leftarrow$) is the contrapositive of the linear dependence lemma. ($\Rightarrow$) follows by writing $v_k = \sum b_i v_i$ as $\sum b_i v_i - v_k = 0$, a nontrivial combination.
>
> **Why needed:** This is the iterative form of independence that makes the reduction's termination produce an independent list.
>
> > [!note]- Full proof
> > ($\Leftarrow$) Suppose for contradiction the list is dependent. By the [[Def - Linear Combination and Span|linear dependence lemma]] (LADR 2.19), some $v_k$ is in $\operatorname{span}(v_1, \ldots, v_{k-1})$, contradicting the hypothesis.
> >
> > ($\Rightarrow$) Suppose for contradiction some $v_k \in \operatorname{span}(v_1, \ldots, v_{k-1})$, say $v_k = b_1 v_1 + \cdots + b_{k-1} v_{k-1}$. Then $b_1 v_1 + \cdots + b_{k-1} v_{k-1} - v_k = 0$ is a nontrivial vanishing combination (coefficient of $v_k$ is $-1 \neq 0$), contradicting independence.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Every spanning list $v_1, \ldots, v_n$ of $V$ can be reduced to a basis of $V$.
>
> *Proof.* Run the following algorithm. Start with $B = v_1, v_2, \ldots, v_n$.
>
> **Step 1.** If $v_1 = 0$ (equivalently, $v_1 \in \operatorname{span}() = \{0\}$), delete $v_1$ from $B$. Otherwise, leave $B$ unchanged.
>
> **Step $k$** (for $k = 2, \ldots, n$). Examine $v_k$. If $v_k$ is in the span of the entries of $B$ that precede $v_k$ (note: these are the surviving predecessors after earlier deletions), delete $v_k$ from $B$. Otherwise, leave $B$ unchanged.
>
> After step $n$ the algorithm terminates with a final list $B$, a sublist of $v_1, \ldots, v_n$.
>
> *Claim 1: $B$ spans $V$.* The original list $v_1, \ldots, v_n$ spans $V$. At each step, we deleted from $B$ only entries that lay in the span of the predecessor entries already in $B$. By Lemma 1, each deletion preserves the span of $B$. So at termination, $B$ still spans $V$.
>
> *Claim 2: $B$ is linearly independent.* By the construction, no entry of $B$ lies in the span of its predecessors in $B$ (if it did, it would have been deleted). By Lemma 2, $B$ is linearly independent.
>
> Hence $B$ is a basis of $V$, as required. $\qquad\blacksquare$
>
> **Corollary (LADR 2.31, existence of a basis).** Every finite-dimensional vector space $V$ has a basis. *Proof:* By definition of finite-dimensionality, $V$ has a finite spanning list, and by the theorem this list contains a basis as a sublist. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Module theory: finitely generated free modules and the structure of generating sets.** The theorem's spirit — that a generating set of a finitely generated free module reduces to a basis — fails for general modules. Over a field every finitely generated module is free, but over a general ring, generating sets need not contain a basis. For example $\mathbb{Z}/6\mathbb{Z}$ as a $\mathbb{Z}$-module is generated by $\{2, 3\}$ (since $\gcd(2, 3) = 1$ in $\mathbb{Z}$), but no sublist is a basis — the module has 2-torsion and 3-torsion and so is not free. This makes the theorem distinctively a vector-space phenomenon and a clean property of the field-special case.

**Matroid theory: the basis exchange theorem.** In matroids the analogous reduction works: every spanning set contains a *base* (the matroid analogue of basis). The proof is the same greedy argument with "is in the span of" replaced by "is in the closure of". This is the matroid axiom system in action; the chapter's algorithm specialises a general matroid construction.

**Computer science: Gaussian elimination as basis reduction.** When the spanning list consists of vectors of $F^n$, the reduction algorithm is equivalent to **Gaussian elimination** on the matrix whose columns are the vectors. The pivot columns of the reduced matrix correspond to the surviving basis vectors; the non-pivot columns are the redundant ones (the vectors in the span of the previous ones). Gaussian elimination is the computational realisation of 2.30 with explicit pivots, and it gives the algorithm $O(mn^2)$ time complexity for spanning lists of $m$ vectors in $F^n$.

**Algebraic geometry: Hilbert basis theorem.** A polynomial ideal in $k[x_1, \ldots, x_n]$ is finitely generated (Hilbert basis theorem), and given a generating set one wants to reduce it to a **Gröbner basis** — a particularly well-behaved generating set. The reduction here is more elaborate than the vector-space case (it requires *Buchberger's algorithm*), but the basic flavour is the same: identify and eliminate redundancies among the generators. Gröbner bases are the polynomial-ring analogue of the vector-space basis reduction.

---

# Bridges

- **[[Thm - Every Linearly Independent List Extends to a Basis]]** — the dual structural theorem. Together they say bases are *both* the maximal independent sublists of any spanning list, *and* the minimal spanning supersets of any independent list. The chapter's main message is that these two operations converge to the same answer, and the converging integer is $\dim V$.

- **[[Def - Linear Combination and Span|Linear dependence lemma]]** — the engine of the proof. The lemma identifies which vectors in a dependent list are redundant; the reduction algorithm just iterates that identification. So the theorem is essentially "apply the linear dependence lemma over and over until no more applications are possible".

- **Gaussian elimination** — the computational realisation. When vectors are concretely given as elements of $F^n$, the test "is $v_k \in \operatorname{span}(v_1, \ldots, v_{k-1})$" is a linear system, which Gaussian elimination solves directly. The pivot columns of the reduced echelon form are the basis vectors; the non-pivot columns are the redundancies. So 2.30 is, in matrix language, "the pivot columns of $[v_1 | v_2 | \cdots | v_n]$ form a basis of the column space".

- **Smith normal form (in [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]] and beyond)** — for modules over a PID, an analogous reduction produces a canonical form for matrices that records the rank and the torsion structure simultaneously. The vector-space reduction is the field case where there is no torsion and the canonical form simplifies to "identity in the upper-left, zeros elsewhere".

---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Linear Independence"
  - "Def - Basis"
  - "Def - Finite-Dimensional Vector Space"
  - "Thm - Every Spanning List Contains a Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional vector space over $F$, with a linearly independent list $u_1, \ldots, u_m$. The full notation registry is on the parent topic page [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

---

# Statement

> **Theorem (LADR 2.32).** Every [[Def - Linear Independence|linearly independent]] list of vectors in a [[Def - Finite-Dimensional Vector Space|finite-dimensional]] vector space can be extended to a [[Def - Basis|basis]] of the space.

> **Corollary (LADR 2.33, direct-sum complement).** If $V$ is finite-dimensional and $U$ is a [[Def - Subspace|subspace]] of $V$, then there exists a subspace $W$ of $V$ such that $V = U \oplus W$.

The extension is constructive: prepend any spanning list of $V$ to the right of the independent list, and apply the reduction of [[Thm - Every Spanning List Contains a Basis|LADR 2.30]]. None of the original independent vectors get deleted (they cannot be redundant against an independent list of which they are a sublist), and the result is a basis.

---

# Motivation

The theorem is the dual of [[Thm - Every Spanning List Contains a Basis|LADR 2.30]]. Where 2.30 says spanning lists are "near" bases — they can be cut down to one — this theorem says independent lists are near bases too, but in the opposite direction: they can be *grown* to one. The two structural theorems together say bases are the meeting point of two converging operations: shrink a spanning list, or extend an independent list. Both procedures terminate at the same place.

The theorem has two main practical roles. First, it is the engine of every "construct a basis with prescribed initial segment" problem. The standard situation is: you have a subspace $U \subseteq V$, you have a basis $u_1, \ldots, u_m$ of $U$, and you want a basis of $V$ that starts with $u_1, \ldots, u_m$. The reason you would want this: a basis of $V$ adapted to the subspace $U$ makes the geometry of $U$ inside $V$ readable, makes the dimensional accounting easy, and is the setup for [[Linear Algebra III — §3A–D Linear Maps|the matrix representation of linear maps]] in the next chapter (where one chooses bases of domain and codomain to give the linear map a particularly clean matrix). The extension theorem guarantees such a basis always exists.

Second, it is the engine of the **direct-sum complement** theorem (Corollary, LADR 2.33). Every subspace of a finite-dimensional space has a *complementary* subspace, meaning a $W$ such that $V = U \oplus W$. The complement is constructed by extending a basis of $U$ to a basis of $V$ and taking the span of the new vectors. This is dimension-additive: $\dim V = \dim U + \dim W$. The existence of complements is a feature *unique to finite-dimensional algebra*; in infinite-dimensional Banach or Hilbert spaces a subspace may have no closed complement (the **complemented subspace problem** is non-trivial), but with the Hilbert-space inner product the orthogonal complement always exists. In purely algebraic linear algebra over a field, the complement is automatic.

The theorem also makes a third structural point quietly. Together with [[Thm - Bases are Equinumerous|2.34]] and [[Thm - Every Spanning List Contains a Basis|2.30]], it gives the **length-of-basis shortcut for independent lists**: in $V$ of dimension $n$, every independent list of length $n$ is already a basis, because the extension promised by 2.32 would have to add vectors *but cannot* (every basis has length $n$). This shortcut is Corollary 2 of [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|the length inequality]].

---

# Sources and Targets

**Sources (Input Broadening).**

The hypothesis is *a linearly independent list in a finite-dimensional space*. The skill is recognising when a problem hands you one.

A first source is **a basis of a subspace**. Property $B$: "you have a basis of some subspace $U$." The bridge: a basis of $U$ is, in particular, a linearly independent list in $U$, and hence in the ambient $V$. The theorem extends it to a basis of $V$. This is the **most common source** — it is how you construct a basis of $V$ adapted to a subspace.

A second source is **a tuple of vectors known to be independent**. Property $B$: "you have specific vectors $v_1, \ldots, v_m$ shown to be independent (e.g. by a coordinate calculation), and want a basis of the ambient $V$ extending them." The bridge: directly apply 2.32. The skill is just recognising that independence has been established before extending.

A third source is **a single nonzero vector or eigenvector**. Property $B$: "you have one nonzero vector $v$, or one eigenvector of an operator." The bridge: a list of length 1 with a nonzero vector is linearly independent. Extending to a basis is then a starting point for the structural arguments in [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|invariant subspace theory]] — eigenvalues are extracted by extending a single eigenvector to a basis adapted to the operator.

A fourth source is **a list with a known number of independent vectors but no upper bound on dimension**. Property $B$: "you have produced $m$ independent vectors and want to bound $\dim V$." The bridge: 2.32 says these $m$ vectors extend to a basis of $V$, so $\dim V \geq m$. This is the standard way to lower-bound dimensions in problems.

**Targets (Output Amplification).**

A first combination is **plus equality of lengths forces no extension is needed**. If the independent list has length exactly $\dim V$, the basis it extends to has length $\dim V$ (by [[Thm - Bases are Equinumerous|2.34]]), so the extension adds zero vectors, so the original list was already a basis. This is the *independent + right length = basis* shortcut, Corollary 2 of 2.22.

A second combination is **plus a basis exhibits the direct-sum complement**. If $u_1, \ldots, u_m$ is a basis of $U \subseteq V$, extending to a basis $u_1, \ldots, u_m, w_1, \ldots, w_n$ of $V$ and setting $W = \operatorname{span}(w_1, \ldots, w_n)$ gives $V = U \oplus W$. This is the corollary 2.33. The proof: $U + W$ contains all basis vectors of $V$, so equals $V$; $U \cap W = \{0\}$ because any element common to both has expansions only in $u$'s and only in $w$'s, and uniqueness of expansion in the basis $u_1, \ldots, u_m, w_1, \ldots, w_n$ forces both to be zero.

A third combination is **plus the dimension formula 2.43 to compute dimensions**. Extending bases of $V_1 \cap V_2$ to bases of $V_1$ and of $V_2$ separately is the standard setup for proving [[Thm - Dimension of a Sum of Subspaces|2.43]]. The theorem provides the extensions; the dimension formula is then a clean count.

A fourth combination is **plus a linear map produces a basis-adapted matrix**. If $T : V \to W$ is a linear map with $\ker T$ of dimension $k$, extending a basis of $\ker T$ to a basis of $V$ produces a basis $u_1, \ldots, u_k, v_1, \ldots, v_{n-k}$ of $V$ in which $T u_i = 0$ for $i \leq k$ and $T v_j$ are independent (forming a basis of $\operatorname{range} T$). This is the **rank-nullity** structure of [[Linear Algebra III — §3A–D Linear Maps|the next chapter]] — and the matrix of $T$ in this adapted basis is block-diagonal with a zero block. So 2.32 powers the structure theorem for linear maps.

---

# Why Is It True

The intuition is **prepend the independent list to a known spanning list, then reduce; the independent vectors cannot be reduced away, so they end up in the basis**.

Concretely: take the independent list $u_1, \ldots, u_m$, and let $w_1, \ldots, w_n$ be any spanning list of $V$ (which exists by finite-dimensionality). Form the concatenated list
$$u_1, u_2, \ldots, u_m, w_1, w_2, \ldots, w_n.$$
This is a spanning list of $V$: any vector $v \in V$ is reachable from the $w$'s alone, so a fortiori from the longer list. Apply [[Thm - Every Spanning List Contains a Basis|the reduction of 2.30]] to this spanning list: the result is a sublist that is a basis.

The crucial observation is that **none of the $u_i$'s get deleted by the reduction**. The reduction deletes an entry if and only if it is in the span of its predecessors in the list. The first deletion candidate is $u_1$; but $u_1 \neq 0$ (since the list is independent, $u_1$ is in particular nonzero), so $u_1$ is not in $\operatorname{span}() = \{0\}$, and $u_1$ survives. Similarly, $u_2$ is not in $\operatorname{span}(u_1)$ (or it would be a scalar multiple of $u_1$, violating independence of the pair $u_1, u_2$), so it survives. In general, $u_k$ is not in $\operatorname{span}(u_1, \ldots, u_{k-1})$ by the iterative form of linear independence (Lemma 2 in [[Thm - Every Spanning List Contains a Basis]]), so $u_k$ survives.

By contrast, some of the $w$'s may be redundant against the $u$'s already in the surviving list, and the reduction may delete them. Those are exactly the vectors we wanted to delete: the $w$'s that don't add to the span beyond what the $u$'s and earlier $w$'s already give.

The output is a list that begins with $u_1, \ldots, u_m$ (all survived) and continues with whichever $w$'s were not deleted. It is a basis (by 2.30's conclusion). So the original independent list has been extended to a basis by adding some of the $w$'s.

The bolded one-liner: **independence of the $u$'s means no $u$ is redundant against the earlier $u$'s, so the reduction cannot delete any $u$ — it only deletes redundant $w$'s, producing a basis that starts with all the $u$'s**.

The corollary on direct-sum complements: take a basis of $U$, extend to a basis of $V$; the new basis vectors span a subspace $W$ with $V = U \oplus W$. The direct-sum decomposition is read off the basis.

---

# What Makes This Hard

The proof is short but the *order* in the concatenation matters: the $u$'s must come first, the $w$'s second. If you tried it the other way — $w$'s then $u$'s — the reduction would delete the $w$'s normally, but a $u$ following a partial sublist of $w$'s might be redundant against those $w$'s (the $u$'s are independent among themselves, but a $u$ could perfectly well lie in the span of some $w$'s). So the order is load-bearing for the conclusion "no $u$ gets deleted".

A second potential confusion is the existence of the *spanning list of $V$* used in the construction. This is where finite-dimensionality enters: $V$ has a finite spanning list by definition, and any such list works. In infinite-dimensional vector spaces the theorem still holds (every linearly independent set extends to a Hamel basis, by Zorn's lemma), but the proof is different in flavour — there is no concatenate-and-reduce algorithm, only an existence argument from the axiom of choice.

A third subtle point is that the extension is *not unique*. Different choices of the spanning list $w_1, \ldots, w_n$ produce different extensions; even with the same spanning list, the surviving subset of the $w$'s might be different if reordered. The theorem promises *existence*, not *uniqueness*. Geometrically, the complementary subspace $W$ in 2.33 is also not unique — only its *dimension* $\dim V - \dim U$ is determined.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:** Concatenate the independent list with any spanning list of $V$ (the $u$'s first, $w$'s second), apply the reduction of [[Thm - Every Spanning List Contains a Basis|2.30]] to the concatenated list, and observe that the $u$'s cannot be deleted by the reduction (because of their mutual independence).

**Subgoal decomposition:**

1. **Concatenate.** Form the list $u_1, \ldots, u_m, w_1, \ldots, w_n$, where the $w$'s are any spanning list of $V$ (exists by finite-dimensionality).
   - *Hint:* The order matters — $u$'s first, $w$'s second.
   - *Why needed:* The order ensures the independence-preserving property of the reduction.

2. **Verify concatenated list spans $V$.** Trivial: it contains a spanning list of $V$ as a sublist.
   - *Hint:* Adding vectors to a spanning list does not lose spanning.

3. **Apply [[Thm - Every Spanning List Contains a Basis|2.30]].** The reduction algorithm processes the list left-to-right, deleting any entry in the span of its predecessors.
   - *Hint:* This is the building block from the previous theorem.

4. **Show no $u_i$ is deleted.** For each $i$, $u_i \notin \operatorname{span}(u_1, \ldots, u_{i-1})$ by the iterative form of linear independence. So $u_i$'s "predecessors" in the reduction (when it reaches $u_i$) include nothing not in the original list, and $u_i$ is not in their span.
   - *Hint:* Iterative independence.
   - *Why needed:* This is the key that distinguishes 2.32 from a simple application of 2.30 — the extension is "anchored" by the $u$'s.

5. **Conclude.** The reduction produces a basis of $V$ that contains $u_1, \ldots, u_m$ as a sublist. This is the desired extension.

---

# Lemma Decomposition

> [!note]- Lemma 1: No $u_i$ is in the span of its predecessors in the concatenated list
> **Statement:** In the list $u_1, \ldots, u_m, w_1, \ldots, w_n$ with the $u$'s independent, $u_i \notin \operatorname{span}(u_1, \ldots, u_{i-1})$ for every $i$.
>
> **Hint:** Use the iterative form of linear independence (Lemma 2 of [[Thm - Every Spanning List Contains a Basis]]).
>
> **Why needed:** This is what forces the reduction to keep all $u_i$.
>
> > [!note]- Full proof
> > Suppose for contradiction $u_i \in \operatorname{span}(u_1, \ldots, u_{i-1})$ for some $i$. Then $u_i = b_1 u_1 + \cdots + b_{i-1} u_{i-1}$ for some scalars $b_j$, giving $b_1 u_1 + \cdots + b_{i-1} u_{i-1} - u_i = 0$ — a nontrivial vanishing combination of $u_1, \ldots, u_i$, contradicting linear independence of $u_1, \ldots, u_m$.

> [!note]- Lemma 2: The reduction of 2.30 deletes only entries in the span of previously surviving predecessors
> **Statement:** When [[Thm - Every Spanning List Contains a Basis|the reduction of 2.30]] is applied to a list $v_1, \ldots, v_N$, it deletes the entry $v_k$ if and only if $v_k$ is in the span of the entries in positions $1, \ldots, k-1$ that have *survived* up to step $k$.
>
> **Hint:** This is the algorithm's definition.
>
> **Why needed:** It says the test for deletion only looks at survivors, so if all of $u_1, \ldots, u_{i-1}$ have survived up to step $i$, the test for $u_i$ is against those $u$'s (plus any surviving $w$'s, but in step $i \leq m$ no $w$'s have been processed yet).
>
> > [!note]- Full proof
> > By construction, the algorithm in [[Thm - Every Spanning List Contains a Basis|2.30]] processes positions $k = 1, 2, \ldots, N$ in order, and at each step examines whether the $k$-th entry is in the span of the surviving entries at positions $1, \ldots, k-1$. Up to step $k$, the algorithm has only seen entries in positions $\leq k$; entries in positions $> k$ have not been processed and have no bearing.
> >
> > When $k \leq m$, the surviving entries at positions $1, \ldots, k-1$ are all $u$'s (no $w$'s have been processed yet), and by Lemma 1 the entry $u_k$ at position $k$ is not in their span. So $u_k$ survives. Inductively, all $u_1, \ldots, u_m$ survive, and we know which entries among the $w$'s survive after the algorithm processes them in turn.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $V$ be a finite-dimensional vector space, and let $u_1, \ldots, u_m$ be a linearly independent list in $V$. Then $u_1, \ldots, u_m$ can be extended to a basis of $V$.
>
> *Proof.* Let $w_1, \ldots, w_n$ be a finite spanning list of $V$ (exists by finite-dimensionality of $V$). Form the concatenated list
> $$L = u_1, u_2, \ldots, u_m, w_1, w_2, \ldots, w_n.$$
> The list $L$ spans $V$, since it contains the spanning list $w_1, \ldots, w_n$.
>
> Apply the reduction of [[Thm - Every Spanning List Contains a Basis|LADR 2.30]] to $L$. The reduction produces a sublist $B$ of $L$ that is a basis of $V$.
>
> *Claim: Each $u_i$ appears in $B$.*
>
> By Lemma 1, $u_i \notin \operatorname{span}(u_1, \ldots, u_{i-1})$ for every $i \in \{1, \ldots, m\}$. By Lemma 2, the reduction examines $u_i$ at step $i$ (no entries before position $i$ have been processed beyond $u_1, \ldots, u_{i-1}$, which are all surviving by induction), and the deletion test is whether $u_i \in \operatorname{span}$ of the surviving predecessors — i.e. $u_1, \ldots, u_{i-1}$. By Lemma 1 this fails, so $u_i$ survives.
>
> By induction on $i$, every $u_i$ survives. Hence $B$ contains $u_1, \ldots, u_m$ as a sublist. Since $B$ is a basis of $V$, this is an extension of the independent list to a basis.
>
> $\qquad\blacksquare$
>
> **Corollary (LADR 2.33).** If $V$ is finite-dimensional and $U$ is a subspace of $V$, then there exists a subspace $W$ of $V$ such that $V = U \oplus W$.
>
> *Proof.* By [[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|LADR 2.25]], $U$ is finite-dimensional, so has a basis $u_1, \ldots, u_m$ (where $m = \dim U$). By the theorem, this basis extends to a basis $u_1, \ldots, u_m, w_1, \ldots, w_n$ of $V$. Define $W = \operatorname{span}(w_1, \ldots, w_n)$, a subspace of $V$.
>
> *Subclaim 1: $V = U + W$.* Every $v \in V$ has an expansion $v = a_1 u_1 + \cdots + a_m u_m + b_1 w_1 + \cdots + b_n w_n$ in the basis, so $v = u + w$ with $u = \sum a_i u_i \in U$ and $w = \sum b_j w_j \in W$. Hence $V \subseteq U + W$; the reverse inclusion is immediate.
>
> *Subclaim 2: $U \cap W = \{0\}$.* Suppose $v \in U \cap W$. Then $v = \sum a_i u_i$ (as element of $U$) and $v = \sum b_j w_j$ (as element of $W$), so $\sum a_i u_i - \sum b_j w_j = 0$ in $V$. Since $u_1, \ldots, u_m, w_1, \ldots, w_n$ is a basis (in particular linearly independent), all $a_i = 0$ and all $b_j = 0$, so $v = 0$.
>
> Combining: $V = U + W$ and $U \cap W = \{0\}$, so $V = U \oplus W$ by [[Def - Direct Sum|the direct sum criterion]]. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Functional analysis: not every closed subspace of a Banach space has a closed complement.** In infinite-dimensional Banach spaces, the analogue of 2.33 fails: there exist Banach spaces $X$ and closed subspaces $U \subseteq X$ with no closed complementary subspace. The space $c_0$ inside $\ell^\infty$ is the classical example (Phillips's theorem). In Hilbert spaces, the inner product saves the day — every closed subspace has the **orthogonal complement** as its complementary subspace — but in non-Hilbert Banach spaces this fails dramatically. The complemented subspace problem (Lindenstrauss-Tzafriri 1971: a Banach space all of whose closed subspaces are complemented is isomorphic to a Hilbert space) is a deep theorem in functional analysis. So 2.32/2.33 is a *uniquely finite-dimensional* phenomenon when we restrict to closed subspaces.

**Module theory: the splitting lemma.** A short exact sequence $0 \to A \to B \to C \to 0$ of modules over a ring $R$ is **split** if it is isomorphic to the trivial direct-sum sequence $0 \to A \to A \oplus C \to C \to 0$. Over a field, every short exact sequence of vector spaces splits — this is the module-theoretic content of 2.33, with $A = U$, $C = V/U$, and $B = V$. Over a general ring, splitting fails: $0 \to \mathbb{Z} \to \mathbb{Z} \to \mathbb{Z}/2 \to 0$ (multiplication by 2) is a short exact sequence of $\mathbb{Z}$-modules that does not split (any splitting would give $\mathbb{Z} \cong \mathbb{Z} \oplus \mathbb{Z}/2$, but the right side has torsion and the left does not). So splitting of short exact sequences is the algebraic content of "complements exist", and 2.32 is the field case.

**Geometry: the existence of orthonormal bases adapted to subspaces.** In an inner product space, the Gram-Schmidt procedure ([[Linear Algebra VI — §6 Inner Product Spaces]]) refines 2.32: an *orthonormal* basis of a subspace extends to an *orthonormal* basis of the ambient space. The flat extension theorem 2.32 has an orthonormal version, where the additional basis vectors can be chosen orthogonal to the original ones. This is the foundation of the structure theory of operators on inner product spaces (spectral theorem, SVD).

---

# Bridges

- **[[Thm - Every Spanning List Contains a Basis]]** — the dual theorem. Both this theorem and that one approach bases by extremal procedures, and they converge: the basis you reach by reducing a spanning list of $V$ has the same length as the basis you reach by extending an independent list to a basis of $V$. The common length is $\dim V$, the well-defined invariant.

- **[[Thm - Bases are Equinumerous]]** — the corollary "an independent list of length $\dim V$ is automatically a basis" uses 2.32 (the extension exists) together with 2.34 (the basis has length $\dim V$, so no extension is needed). The combined shortcut is one of the most-used facts in §2C.

- **Direct-sum complements** — the corollary 2.33 is exactly the existence of complementary subspaces in finite-dimensional spaces. Every subspace has a complement; in infinite-dimensional Banach spaces this fails for closed complements, in Hilbert spaces it is restored by orthogonality.

- **[[Linear Algebra III — §3A–D Linear Maps|Rank-nullity (LADR 3.21)]]** — the structure theorem for linear maps relies on extending a basis of the kernel to a basis of the domain. The extension is the basis-adapted structure that makes the matrix of the map block-diagonal (with a zero block for the kernel). So 2.32 is essential to the proof of rank-nullity in the next chapter.

- **The splitting lemma in homological algebra** — for module categories, the analogue of 2.33 is the **splitting lemma**, which characterises when a short exact sequence is direct-sum-split. Over a field, every short exact sequence of vector spaces splits, so the homological algebra of vector spaces is comparatively trivial. This is the algebraic content of "every subspace has a complement", and it makes finite-dimensional linear algebra a uniquely clean special case of homological algebra.

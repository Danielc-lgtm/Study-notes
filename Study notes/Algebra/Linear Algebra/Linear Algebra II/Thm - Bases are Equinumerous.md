---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Basis"
  - "Thm - Length of Linearly Independent List Bounded by Length of Spanning List"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional vector space over $F$, with bases denoted $B_1, B_2, \ldots$ and lengths $|B_i|$. See the parent topic page [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]] for the full notation registry.

---

# Statement

> **Theorem (LADR 2.34).** Any two bases of a [[Def - Finite-Dimensional Vector Space|finite-dimensional]] vector space have the same length.

This theorem is what makes [[Def - Dimension|dimension]] well-defined: we may call the common length $\dim V$, and it is an invariant of $V$ alone, independent of which basis is chosen to compute it.

---

# Motivation

The theorem answers a question that is begging from the moment "basis" is defined. We have seen ([[Def - Basis]] Examples) that a finite-dimensional vector space typically has *many* bases — $F^2$ has the standard basis $(1, 0), (0, 1)$ and the alternative $(1, 2), (3, 5)$, and infinitely many others. The two bases of $F^2$ both have length 2; both standard bases of $\mathcal{P}_5(F)$ have length 6. Is this a coincidence, or is there a *forced* equality?

If different bases of the same space could have different lengths, the concept of "[[Def - Dimension|dimension]]" would be useless. We could not say $\dim \mathbb{R}^3 = 3$ — only "$\mathbb{R}^3$ has a basis of length 3, and also one of length 7". The numerical handle would be no handle at all. The theorem says no: the length is *forced* to be the same for all bases, so "dimension" becomes a basis-independent integer attached to $V$.

The theorem is also where the term **finite-dimensional** acquires its full force. Up to this point, "finite-dimensional" has meant "has a finite spanning list" or equivalently "has a finite basis", but we did not know that the *integer length* of such a basis was determined. Now we do: it is determined, and it is intrinsic.

The proof is the cleanest possible application of the [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|length inequality]]: it is *two* applications of that inequality, in opposite directions, against the *same* pair of bases. The whole proof fits in three lines, and yet without it the rest of finite-dimensional linear algebra has nothing to say.

---

# Sources and Targets

**Sources (Input Broadening).**

The theorem's hypothesis is sparse — *two bases of a finite-dimensional space*. The skill is recognising when a problem hands you two candidate "complete describing systems" and asks whether they must agree numerically.

A first source is **two parametrisations of the same subspace**. Property $B$: "you have two different lists, each of which fully describes the same subspace as a basis." The bridge: both are bases of the same space, so the theorem applies. Non-obvious examples: in $\mathcal{P}_3(\mathbb{R})$, the basis $1, x, x^2, x^3$ and the basis $1, (x-5), (x-5)^2, (x-5)^3$ are both bases — and the theorem forces them to have the same length 4, which is the dimension of the space. The skill is recognising both lists as bases (which is the work) and then automatically getting the length equality.

A second source is **two different "natural" choices in a coordinate system**. Property $B$: "a physical or geometric problem suggests two natural coordinate systems." The bridge: both correspond to bases of the same underlying vector space, and the theorem forces equal length. Example: a vector in $\mathbb{R}^3$ can be expanded in the Cartesian basis or in the spherical-coordinate basis (radial, polar, azimuthal); both give 3 components. The bridge is non-obvious because the two coordinate systems "look" so different at the level of computation, but at the level of dimension they must agree.

A third source is **two different "natural" presentations of an algebraic structure**. Property $B$: "you have an algebraic object (a polynomial ring modulo an ideal, a quotient module, a tensor product) with two different presentations as a vector space." The bridge: both presentations come with natural bases, and they must have the same length. Example: the quotient ring $\mathbb{R}[x]/(x^2 + 1)$ has $\{1, x\}$ as a basis over $\mathbb{R}$, and also $\{1, i\}$ when identified with $\mathbb{C}$ — both have length 2.

**Targets (Output Amplification).**

The theorem produces an equality of integers. Combined with one further fact, it produces structural conclusions.

A first combination is **equinumerosity plus extension by [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] forces a basis from independence at the right length**. If a linearly independent list has length equal to $\dim V$ (computable from any basis), then by 2.34 it cannot be extended further; by 2.32 extension is *always possible*; the only way to reconcile is that the list is already a basis. This is Corollary 2 of 2.22 in the [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List#Statement|length inequality]], and it is the most-used consequence of the well-definedness of dimension.

A second combination is **equinumerosity plus the dimension formula 2.43 forces a numerical identity on intersections and sums**. If two subspaces $V_1, V_2$ have bases of known length, and you know a basis of $V_1 + V_2$ or $V_1 \cap V_2$, then by 2.43 the fourth quantity is determined. Without equinumerosity none of these would be well-defined numbers. Almost every problem in §2C ultimately reduces to a 2.43 + 2.34 calculation.

A third combination is **equinumerosity plus a constructive basis exhibits a precise isomorphism**. If $V$ is finite-dimensional with $\dim V = n$, then for any basis $v_1, \ldots, v_n$ we have a vector-space isomorphism $V \cong F^n$ via $v \mapsto (\text{coordinate tuple})$ — and crucially, the *integer* $n$ is the same no matter which basis is chosen, so $V \cong F^n$ is unambiguous. This statement could not be made if dimensions were not well-defined.

---

# Why Is It True

The intuition is **two applications of the length inequality, run in opposite directions, against the same pair of bases**.

Let $B_1, B_2$ be two bases of $V$. The defining properties of a basis are: it is linearly independent, and it spans $V$. So $B_1$ is independent and $B_2$ spans. Applying [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]] gives $|B_1| \leq |B_2|$. Now reverse the roles: $B_2$ is also independent (it is a basis), and $B_1$ also spans (it is a basis). Applying 2.22 again gives $|B_2| \leq |B_1|$. Combining: $|B_1| = |B_2|$.

The bolded one-liner: **a basis is *both* independent and spanning, so the length inequality applies in both directions against any other basis, sandwiching the lengths to equality**.

The "why is it true" content lives entirely in [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]], which has its own intuition (the Steinitz exchange). Once 2.22 is granted, 2.34 follows by an entirely formal manoeuvre. This is unusual for a "main theorem of the chapter"; the usual pattern is that the main theorem has the substantive intuition and the lemmas are formal. Here it is the lemma — 2.22 — that has the substantive intuition, and the main theorem 2.34 is the formal corollary that the chapter is *named after*.

The lesson is that the well-definedness of dimension is *cheap*, once you have done the work of 2.22. You may safely study and remember 2.34 as "two applications of 2.22", and concentrate your conceptual effort on 2.22 itself.

---

# What Makes This Hard

The theorem is *not* hard in itself — it is a one-step corollary. What is hard is *recognising that this theorem is what licenses calling "dimension" a well-defined integer*. Students sometimes treat the equinumerosity as an obvious assumption rather than a substantive result, and then are confused when asked why $\dim V$ does not depend on the choice of basis. The honest answer is: it does not depend on the choice because 2.34, and 2.34 is a real theorem requiring proof. The chapter's structure should be remembered: 2.22 is the engine; 2.34 is the immediate corollary that licenses dimension; 2.43 and the rest are downstream applications.

A second source of confusion is the role of *finite-dimensionality*. The theorem's proof appeals to 2.22, which requires the space to have *a* finite spanning list — but the conclusion is then that *every* basis has the *same* finite length. The implication is one-way: finite-dimensionality is the hypothesis. Without it, bases can still exist (Hamel basis, Zorn), but they may be of different cardinalities — actually they are of the same cardinality, but the proof requires Zorn and cardinal arithmetic instead of 2.22's exchange procedure. The well-definedness of dimension in infinite [[Def - Dimension|dimensions]] is therefore a more delicate result.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:** Apply the length inequality 2.22 twice against the *same* pair of bases, in opposite directions. The first application uses one basis as independent, the other as spanning; the second swaps the roles. Both inequalities together force equality.

**Subgoal decomposition:**

1. **Use $B_1$ independent and $B_2$ spanning to get $|B_1| \leq |B_2|$.**
   - *Hint:* This is a direct application of [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]].
   - *Why needed:* This is the first half of the sandwich.

2. **Use $B_2$ independent and $B_1$ spanning to get $|B_2| \leq |B_1|$.**
   - *Hint:* Same theorem, swap roles. A basis is independent and spans, so either can play either role.
   - *Why needed:* This is the second half. Together with step 1, it forces equality.

3. **Conclude.** $|B_1| = |B_2|$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A basis is both linearly independent and spanning
> **Statement:** Every basis $B$ of $V$ is a linearly independent list in $V$ and is a spanning list of $V$.
>
> **Hint:** This is the definition of basis.
>
> **Why needed:** The proof of 2.34 uses a basis as the *independent* input in one direction and as the *spanning* input in the other. The lemma confirms that a basis can play both roles.
>
> > [!note]- Full proof
> > By [[Def - Basis|definition]] a basis is a list that is linearly independent and spans $V$. Both properties hold for the same list simultaneously.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $V$ be a finite-dimensional vector space, and let $B_1, B_2$ be two bases of $V$. Then $|B_1| = |B_2|$.
>
> *Proof.* By Lemma 1, $B_1$ is linearly independent in $V$ and $B_2$ spans $V$. By [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|LADR 2.22]] applied to these two lists,
> $$|B_1| \leq |B_2|.$$
> Similarly, $B_2$ is linearly independent and $B_1$ spans $V$. Applying LADR 2.22 again to these two lists, with roles swapped,
> $$|B_2| \leq |B_1|.$$
> Combining the two inequalities yields $|B_1| = |B_2|$, as required. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Module theory: invariant basis number (IBN).** A ring $R$ is said to have **invariant basis number** if every free $R$-module of finite rank has a well-defined rank — i.e. if $R^m \cong R^n$ as $R$-[[Def - Module|modules]] implies $m = n$. Fields, commutative [[Def - Ring|rings]], and Noetherian [[Def - Ring|rings]] have IBN; the analogue of the present theorem for free [[Def - Module|modules]] over them is 2.34 with "basis" replaced by "free generating set". For non-commutative rings IBN can fail: there exist rings $R$ with $R \cong R \oplus R$ as left $R$-modules (the **Leavitt algebras**), giving "rank" no sensible meaning. The well-definedness of dimension is therefore a feature of the *field* axioms — not a generic algebraic phenomenon. The proof for IBN-rings is the analogue of 2.22 in module theory.

**Topology: dimension of a manifold.** Classical theorems of topology (invariance of domain, Brouwer's fixed-point theorem) imply that a manifold has a well-defined dimension as a topological invariant — i.e. if $\mathbb{R}^m$ and $\mathbb{R}^n$ are homeomorphic, then $m = n$. The vector-space dimension of the tangent space at any point recovers this manifold dimension, and 2.34 is one ingredient in showing that the choice of tangent-space basis does not affect the count. The interplay is subtle: the topological dimension is the same as the linear-algebraic dimension of the tangent space, and 2.34 ensures both are well-defined.

**Algebra: transcendence degree of a field extension.** Given a field extension $K \subseteq L$, the **transcendence degree** $\operatorname{trdeg}_K(L)$ is the cardinality of any maximal algebraically independent set in $L$ over $K$ (the analogue of "basis" in the algebraic-independence matroid). The well-definedness of transcendence degree — that any two maximal algebraically independent sets have the same cardinality — is the analogue of 2.34, and its proof is the analogue of 2.22 applied to algebraic independence rather than linear independence. The transcendence degree of $\mathbb{C}$ over $\mathbb{Q}$ is uncountable.

---

# Bridges

- **[[Thm - Length of Linearly Independent List Bounded by Length of Spanning List]]** — 2.34 is one of three corollaries of 2.22, and the most fundamental one (the others — that a list of the right length is automatically a basis from either property alone — depend on 2.34 to make sense of "the right length"). So 2.34 lies between 2.22 and the rest of the chapter, as the result that converts a comparison into a *number*.

- **[[Def - Dimension]]** — the existence of $\dim V$ as a well-defined integer is exactly the content of 2.34. Every theorem in §2C and almost every theorem in later chapters uses $\dim V$ as a hypothesis or conclusion; without 2.34 those theorems would be unstatable.

- **Invariant basis number in module theory** — 2.34 is the field special case of a deeper module-theoretic fact: a ring $R$ has IBN if free $R$-modules of distinct ranks are non-isomorphic. The vector-space case is automatic because fields are commutative and the IBN proof for commutative rings runs through the determinant. Non-commutative pathologies (Leavitt algebras) are what shows the field hypothesis is essential.

- **The well-definedness of transcendence degree** — the same theorem in the matroid of algebraic independence rather than linear independence. Both rely on the exchange property, and the proof in either setting is structurally identical. The unification — that 2.34 is *one instance* of a theorem in matroid theory — is the deeper bridge.

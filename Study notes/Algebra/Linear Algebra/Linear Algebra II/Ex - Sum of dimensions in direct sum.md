---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Basis"
  - "Def - Direct Sum"
  - "Def - Dimension"
  - "Thm - Dimension of a Sum of Subspaces"
tags: [algebra, linear-algebra]
---

# Problem Statement

(LADR 2B.10). Suppose $U$ and $W$ are [[Def - Subspace|subspaces]] of $V$ such that $V = U \oplus W$. Suppose also that $u_1, \ldots, u_m$ is a basis of $U$ and $w_1, \ldots, w_n$ is a basis of $W$. Prove that
$$u_1, \ldots, u_m, w_1, \ldots, w_n$$
is a basis of $V$. In particular, $\dim V = \dim U + \dim W = m + n$.

**Recall.**

![[Def - Direct Sum#The Definition]]

A list is a [[Def - Basis|basis]] of $V$ when it is linearly independent and spans $V$. The defining property of a basis is that every $v \in V$ has a unique expansion as a linear combination of the list (see [[Def - Basis#The Definition]]).

A direct sum decomposition $V = U \oplus W$ is equivalent to: every $v \in V$ has a *unique* expression $v = u + w$ with $u \in U$ and $w \in W$. Equivalently, $V = U + W$ and $U \cap W = \{0\}$.

---

# Convergent Strategy

**Problem class:** This is a *combine-bases* problem — given bases of two [[Def - Subspace|subspaces]] and a direct-sum structure between them, combine the bases into a basis of the sum. The problem class is one of the cleanest instances of how direct sums interact with the basis machinery, and it is the *constructive* counterpart of [[Thm - Dimension of a Sum of Subspaces|the dimension formula]] in the special case where the intersection is trivial.

**Assumption pattern:** Three ingredients: (a) $V = U \oplus W$, which by the direct-sum criterion means every $v \in V$ has a unique decomposition $v = u + w$ with $u \in U, w \in W$; (b) $u_1, \ldots, u_m$ basis of $U$, so every $u \in U$ has a unique expansion $\sum a_i u_i$; (c) $w_1, \ldots, w_n$ basis of $W$, so every $w \in W$ has a unique expansion $\sum b_j w_j$. The product of these three uniqueness conditions is exactly what we need to show the concatenated list is a basis of $V$.

**Theorem routing:** We can either prove this directly (uniqueness of $v = u + w$ + uniqueness of expansions of $u$ and $w$ = uniqueness of expansion of $v$, which gives "basis" by the criterion in [[Def - Basis]]), or we can deduce it as a corollary of [[Thm - Dimension of a Sum of Subspaces|2.43]] (the case $U \cap W = \{0\}$ gives $\dim(U + W) = \dim U + \dim W = m + n$, and we have a list of length $m + n$ spanning $V$, so by [[Ex - A list with the right length is a basis iff spanning iff independent|the length-of-basis shortcut]] it is a basis). Both routes work; the direct route is more constructive and is the route I take below.

**Key decision point:** The non-obvious step is *which uniqueness to use first*. Starting from the direct-sum uniqueness ($v = u + w$ unique) and then applying the basis uniqueness in $U$ and $W$ to $u$ and $w$ is the clean path. The alternative — starting from a vanishing combination of the concatenated list and trying to identify which parts go where — works but is more tedious. The direct-sum criterion is a *structural* uniqueness; the basis criterion is a *combinatorial* uniqueness; their composition is the cleanest argument.

---

# Legal Operations Used

1. **Spanning by concatenation (implicit operation).** When the bases of $U$ and $W$ are concatenated, the result spans $V$ because every $v = u + w$ has $u$ spanned by the $u_i$'s and $w$ spanned by the $w_j$'s. This is the operation "concatenate spanning lists of summands to get a spanning list of the sum".

2. **Linear independence via direct-sum uniqueness (operation 9 generalised).** A vanishing combination of the concatenated list is interpreted via the direct-sum decomposition: the $U$-part of the combination must be in $U$ and the $W$-part in $W$, and their sum is zero in $U \oplus W$, which forces both parts to be zero.

3. **Apply [[Thm - Dimension of a Sum of Subspaces|2.43]] in the direct-sum case (operation 6).** As an alternative final step or as a corollary, the dimension formula reduces to $\dim V = \dim U + \dim W$ when the intersection is trivial.

---

# Hints

> [!note]- Hint 1
> A basis is characterised by **uniqueness of expansion** (LADR 2.28). What is the unique expansion of a vector $v \in V$ in the concatenated list?

> [!note]- Hint 2
> Direct-sum gives $v = u + w$ uniquely. Then basis of $U$ gives $u = \sum a_i u_i$ uniquely. And basis of $W$ gives $w = \sum b_j w_j$ uniquely. So $v = \sum a_i u_i + \sum b_j w_j$ — does this combination depend on choices?

> [!note]- Hint 3
> If $v$ had two expansions in the concatenated list, $v = \sum a_i u_i + \sum b_j w_j = \sum a'_i u_i + \sum b'_j w_j$, [[Def - Group|group]] the $u$-part and the $w$-part on each side. Each side is a decomposition $v = u + w$ with $u \in U$ and $w \in W$; by direct-sum uniqueness, $\sum a_i u_i = \sum a'_i u_i$ in $U$ and $\sum b_j w_j = \sum b'_j w_j$ in $W$. Now apply basis-uniqueness within $U$ and within $W$.

---

# Solution

**Plan.** I will verify that every $v \in V$ has a unique expansion $\sum a_i u_i + \sum b_j w_j$ in the concatenated list, which by the criterion-for-basis (LADR 2.28) makes the list a basis. Existence follows from compositionality of the spanning conditions; uniqueness chains three uniqueness conditions — first the direct-sum decomposition into a $u$-part and a $w$-part, then the basis expansions within $U$ and within $W$. As a corollary, $\dim V = m + n$.

**Step 1: Every $v \in V$ has an expansion in the concatenated list.**

> [!note]- Derivation
> Since $V = U + W$, there exist $u \in U$ and $w \in W$ with $v = u + w$.
>
> Since $u_1, \ldots, u_m$ spans $U$, there exist $a_1, \ldots, a_m \in F$ with $u = a_1 u_1 + \cdots + a_m u_m$.
>
> Since $w_1, \ldots, w_n$ spans $W$, there exist $b_1, \ldots, b_n \in F$ with $w = b_1 w_1 + \cdots + b_n w_n$.
>
> Combining:
> $$v = u + w = (a_1 u_1 + \cdots + a_m u_m) + (b_1 w_1 + \cdots + b_n w_n).$$
> So $v$ has an expansion in the concatenated list. Hence the list spans $V$.

**Step 2: The expansion is unique.**

> [!note]- Derivation
> Suppose $v$ has two expansions:
> $$v = a_1 u_1 + \cdots + a_m u_m + b_1 w_1 + \cdots + b_n w_n$$
> and
> $$v = a'_1 u_1 + \cdots + a'_m u_m + b'_1 w_1 + \cdots + b'_n w_n.$$
> [[Def - Group|Group]]:
> $$v = \underbrace{(a_1 u_1 + \cdots + a_m u_m)}_{\in U} + \underbrace{(b_1 w_1 + \cdots + b_n w_n)}_{\in W}$$
> and similarly with primed coefficients. So $v$ has two decompositions $v = u + w = u' + w'$ with $u, u' \in U$ and $w, w' \in W$. By uniqueness of decomposition in the direct sum $V = U \oplus W$ (the direct-sum criterion), $u = u'$ and $w = w'$.
>
> Now apply uniqueness of expansion in the bases of $U$ and $W$ separately. From $u = u'$ in $U$, with bases expansions $\sum a_i u_i = \sum a'_i u_i$, basis-uniqueness in $U$ gives $a_i = a'_i$ for all $i$. From $w = w'$ in $W$, basis-uniqueness in $W$ gives $b_j = b'_j$ for all $j$.
>
> So the two expansions agree coefficient-by-coefficient, proving uniqueness of the expansion of $v$ in the concatenated list.

**Step 3: The concatenated list is a basis. [[Def - Dimension|Dimension]] counts.**

> [!note]- Derivation
> By Step 1 (existence) and Step 2 (uniqueness), every $v \in V$ has a unique expansion as a linear combination of $u_1, \ldots, u_m, w_1, \ldots, w_n$. By [[Def - Basis|the criterion for basis]] (LADR 2.28), this list is a basis of $V$.
>
> The length of the list is $m + n$. By [[Def - Dimension|definition of dimension]] and [[Thm - Bases are Equinumerous|2.34]] (well-definedness of dimension), $\dim V$ equals the length of any basis, so $\dim V = m + n = \dim U + \dim W$.

> [!note]- Sanity check via 2.43
> The result is consistent with [[Thm - Dimension of a Sum of Subspaces|LADR 2.43]] specialised to the direct-sum case: $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$, with $U \cap W = \{0\}$, $\dim(U \cap W) = 0$, giving $\dim V = \dim U + \dim W$. The direct-sum case is dimension-additive without correction term.

> [!note]- Complete formal solution
> Let $V$ be a vector space with subspaces $U, W$ such that $V = U \oplus W$, and let $u_1, \ldots, u_m$ and $w_1, \ldots, w_n$ be bases of $U$ and $W$ respectively. We show $u_1, \ldots, u_m, w_1, \ldots, w_n$ is a basis of $V$, hence $\dim V = m + n$.
>
> By [[Def - Basis|the criterion for basis]] (LADR 2.28), it suffices to show every $v \in V$ has a unique expansion as a linear combination of the concatenated list.
>
> *Existence.* Since $V = U + W$, there exist $u \in U$ and $w \in W$ with $v = u + w$. Since $u_1, \ldots, u_m$ is a basis of $U$, $u = \sum_{i=1}^m a_i u_i$ for some $a_i \in F$. Since $w_1, \ldots, w_n$ is a basis of $W$, $w = \sum_{j=1}^n b_j w_j$ for some $b_j \in F$. Substituting,
> $$v = u + w = \sum_{i=1}^m a_i u_i + \sum_{j=1}^n b_j w_j,$$
> giving an expansion of $v$ in the concatenated list.
>
> *Uniqueness.* Suppose $v = \sum a_i u_i + \sum b_j w_j = \sum a'_i u_i + \sum b'_j w_j$ are two expansions of $v$ in the concatenated list. Group:
> $$v = \left(\sum a_i u_i\right) + \left(\sum b_j w_j\right) = \left(\sum a'_i u_i\right) + \left(\sum b'_j w_j\right),$$
> where $\sum a_i u_i, \sum a'_i u_i \in U$ and $\sum b_j w_j, \sum b'_j w_j \in W$. By [[Def - Direct Sum|uniqueness of the direct-sum decomposition]] $v = u + w$ ($u \in U, w \in W$), we have $\sum a_i u_i = \sum a'_i u_i$ in $U$ and $\sum b_j w_j = \sum b'_j w_j$ in $W$.
>
> By uniqueness of expansion in the basis $u_1, \ldots, u_m$ of $U$, $a_i = a'_i$ for all $i$. By uniqueness of expansion in the basis $w_1, \ldots, w_n$ of $W$, $b_j = b'_j$ for all $j$. So the two expansions agree.
>
> Hence every $v \in V$ has a unique expansion in the concatenated list, so the list is a basis of $V$. The length of this basis is $m + n$, so $\dim V = m + n = \dim U + \dim W$.
> $\qquad\blacksquare$

---

# Key Takeaways

**Concatenating bases of summands gives a basis of a direct sum.** This is the chapter's first concrete *construction* of bases from existing ones. The pattern is: given a direct-sum decomposition of a space, the basis of the whole is the union of the bases of the pieces. The technique generalises to direct sums of more than two subspaces, $V = V_1 \oplus V_2 \oplus \cdots \oplus V_k$, where the basis of $V$ is the concatenation of bases of each $V_i$. This is the structural reason direct sums are dimension-additive: each piece contributes its own basis vectors, with no overlap.

**Direct sums are the cleanest case of the dimension formula.** The general formula [[Thm - Dimension of a Sum of Subspaces|dim(V₁ + V_2) = dim V₁ + dim V_2 - dim(V₁ ∩ V_2)]] has a correction term subtracting the intersection's dimension. In the direct-sum case the intersection is trivial, and the formula collapses to *additive*. This is why direct sums are the "right" form of sum for dimension-counting purposes — they are the case where [[Def - Dimension|dimensions]] add cleanly. Whenever a problem has a direct-sum decomposition explicitly, the dimension count is straightforward; without one, you must work harder via 2.43.

**Three layers of uniqueness compose into one.** The proof's structure is a chain: direct-sum uniqueness of the $V = U + W$ split, then basis uniqueness within $U$, then basis uniqueness within $W$. Each layer is one of LADR's structural uniqueness statements, and they compose to give uniqueness in the concatenated list. This compositional structure is the right way to think about how basis structures interact across direct-sum decompositions: each summand contributes its own basis-coordinate uniqueness, and the direct-sum structure stitches them together.

**The construction generalises to "adapted bases" of larger spaces.** In [[Linear Algebra III — §3A–D Linear Maps|the next chapter]], one wants bases of $V$ adapted to a linear map $T : V \to W$ — typically a basis of $V$ that starts with a basis of $\ker T$. The construction here, plus [[Thm - Every Linearly Independent List Extends to a Basis|the basis extension theorem]] for the part outside $\ker T$, produces exactly such an adapted basis. The basis of $\ker T$ contributes the "kernel part", and the extension contributes the "transversal part" whose images form a basis of $\operatorname{range} T$. This is the foundation of the matrix representation of linear maps and of the rank-nullity theorem.

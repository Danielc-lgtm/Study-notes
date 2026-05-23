---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Linear Combination and Span"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over a field $F$. We use the word **list** for a finite ordered tuple of vectors. See the parent topic page [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]] for the full notation registry.

---

# Axiom Motivation

The qualifier "finite-dimensional" picks out the class of vector spaces that linear algebra is *really* about. The definition could plausibly be phrased in several ways — has a finite basis, has a finite spanning list, has bounded [[Def - Dimension|dimension]] — and they all turn out to be equivalent. The question is which formulation is the *primitive* and which are derived. Axler's choice (and ours) is **the existence of a finite spanning list**, and this is well-motivated.

Why? Because spanning is the easier of the two basis conditions to verify. To exhibit a spanning list, you only need to show that every vector of $V$ is reachable from your candidates; you do not also need to check that the candidates are non-redundant. The cost of having a redundant spanning list is small: by [[Thm - Every Spanning List Contains a Basis|LADR 2.30]] you can always reduce a finite spanning list to a basis, and the reduced list is still finite. So the existence of a finite spanning list is *equivalent* to the existence of a finite basis. We could equally well have used the latter as our definition, but the former is more economical: it does not require the reader to know what a basis is.

The per-axiom failure question for a one-axiom definition reduces to "what if we weaken or strengthen the axiom?". Strengthening to "$V$ has a spanning list of length at most $n$" picks out the spaces of [[Def - Dimension|dimension]] at most $n$, a more restrictive class. Weakening to "$V$ has a spanning list of any cardinality" (countable, or any cardinality bounded by some cardinal) gives infinite-dimensional spaces — including the case where the cardinality is $\aleph_0$ (countably infinite-dimensional), which is the setting of formal power series and many analytic objects. The intermediate case "countably-spanned" is not the same as "finite-dimensional"; for example, $F^\infty$ (the space of all sequences) is *not* spanned by any countable list (it has uncountable dimension), but its subspace of *eventually-zero* sequences is countably spanned but not finite-dimensional. The qualifier "finite" in our definition is essential and load-bearing.

The bridge to the structural theory: once $V$ has a finite spanning list, every result in this chapter is unlocked. Reduction to a basis ([[Thm - Every Spanning List Contains a Basis|2.30]]), well-defined dimension ([[Thm - Bases are Equinumerous|2.34]]), basis extension ([[Thm - Every Linearly Independent List Extends to a Basis|2.32]]), and the dimension formula for sums ([[Thm - Dimension of a Sum of Subspaces|2.43]]) all assume finite-dimensionality somewhere in their proofs. The contrast with infinite-dimensional spaces is sharp: bases still exist (Zorn's lemma), but they are uncountable and cannot be exhibited explicitly; [[Def - Subspace|subspaces]] need not have direct-sum complements; dimension is no longer well-suited to comparison arguments. The chapter is the careful unpacking of what finite-dimensionality buys you.

The opposite property, **infinite-dimensional**, is the negation: no finite list spans $V$. The polynomial space $\mathcal{P}(F)$ is the canonical example. Any finite list has a maximum degree $m$, so its span is contained in $\mathcal{P}_m(F)$, missing $z^{m+1}$.

---

# The Definition

A vector space $V$ over a field $F$ is **finite-dimensional** if there exists a finite list $v_1, \ldots, v_m$ of vectors in $V$ with $\operatorname{span}(v_1, \ldots, v_m) = V$.

A vector space is **infinite-dimensional** if it is not finite-dimensional.

**Equivalent formulation.** $V$ is finite-dimensional if and only if it has a basis of finite length. (One direction: a finite basis spans, so $V$ has a finite spanning list. Other direction: a finite spanning list contains a basis by [[Thm - Every Spanning List Contains a Basis|LADR 2.30]], and the basis it produces is a sublist, hence finite.)

**Equivalent formulation.** $V$ is finite-dimensional if and only if there exists $n \in \mathbb{N}$ such that no linearly independent list in $V$ has length $> n$. (One direction: a finite spanning list of length $n$ caps independent lists by [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]]. Other direction: if independent lists are bounded in length, take a maximal one and verify by the linear dependence lemma that it spans.)

---

# Relate to Other Fields / Compression

A finite-dimensional vector space is the **simplest free module of finite rank** in module theory. In [[Def - Module|module theory]] over a ring $R$, a module $M$ is *finitely generated* if it has a finite generating set — i.e. some finite list whose elements, under all $R$-linear combinations, give all of $M$. Finite-dimensionality is finitely-generatedness specialised to the case where $R$ is a field. In this special case finitely-generated automatically implies free (the existence of a basis), but over a general ring this implication fails — there are finitely generated modules that are not free, like $\mathbb{Z}/2\mathbb{Z}$ as a $\mathbb{Z}$-module.

**True name:** "$V$ is reachable from finitely many vectors via the vector space operations." This is the operational meaning, and it is what makes finite-dimensional spaces tractable. Every vector of $V$ is, in principle, a finite expression in finitely many fixed building blocks — exactly the setup that lets us compute by algebra.

In analysis, the contrast with infinite-dimensional spaces is dramatic. **Finite-dimensional normed vector spaces** have the following equivalent properties, none of which hold infinite-dimensionally:

- All norms are equivalent (induce the same topology).
- Closed bounded sets are compact (Heine-Borel).
- All linear maps from $V$ to any normed space are continuous.
- The unit ball is compact.
- Linear functionals are determined by their kernels.

The chapter's structural theorems are the algebraic counterpart of this analytic richness: in finite dimensions, everything is computable, every subspace has a complement, every linear map has a matrix. Infinite dimensions require topology; the algebraic theory stops working alone.

---

# Examples / Corollaries

**Example.** $F^n$ is finite-dimensional for every positive integer $n$. The standard basis $e_1, \ldots, e_n$ is a finite spanning list.

**Example.** $\mathcal{P}_m(F)$ — polynomials of degree at most $m$ — is finite-dimensional. The list $1, z, z^2, \ldots, z^m$ spans, and has length $m + 1$.

**Example.** The zero space $\{0\}$ is finite-dimensional. The empty list spans (its span is $\{0\}$).

**Example (a finite-dimensional subspace defined by equations).** $U = \{(x_1, x_2, x_3, x_4, x_5) \in \mathbb{R}^5 : x_1 = 3 x_2 \text{ and } x_3 = 7 x_4\}$ is finite-dimensional. Set the three free parameters $x_2, x_4, x_5$ each to $1$ in turn (others to $0$): we get $(3, 1, 0, 0, 0), (0, 0, 7, 1, 0), (0, 0, 0, 0, 1)$, a spanning list of length $3$. So $\dim U = 3$.

**Non-example.** $\mathcal{P}(F)$, the space of *all* polynomials with coefficients in $F$, is *not* finite-dimensional. *Proof:* Suppose $p_1, \ldots, p_m$ is any finite list of polynomials, and let $d = \max_i \deg p_i$. Every linear combination $a_1 p_1 + \cdots + a_m p_m$ has degree at most $d$. The polynomial $z^{d+1}$ has degree $d+1 > d$, so $z^{d+1} \notin \operatorname{span}(p_1, \ldots, p_m)$. Hence no finite list spans $\mathcal{P}(F)$, and the space is infinite-dimensional.

**Non-example.** $F^\infty$, the space of all sequences in $F$, is infinite-dimensional. The same argument as for $\mathcal{P}(F)$ works: any finite list of sequences has bounded "support" in some sense, and one can construct a sequence outside any finite span.

**Non-example.** The space $C[0, 1]$ of continuous real-valued functions on $[0, 1]$ is infinite-dimensional. By the Weierstrass approximation theorem polynomials are dense in $C[0, 1]$, and $\mathcal{P}(\mathbb{R})$ embeds in $C[0, 1]$ as polynomials restricted to $[0, 1]$. Since $\mathcal{P}(\mathbb{R})$ is infinite-dimensional, so is $C[0, 1]$.

**Corollary ([[Def - Subspace|subspaces]] inherit finite-dimensionality).** Every subspace of a finite-dimensional space is finite-dimensional. *Proof:* This is [[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|LADR 2.25]] — a careful greedy construction that ends because the length inequality caps independent lists in the subspace by the dimension of the ambient space.

**Corollary (sums and products of finite-dimensional spaces are finite-dimensional).** If $V_1$ and $V_2$ are finite-dimensional subspaces of $V$, then $V_1 + V_2$ is finite-dimensional. *Proof:* Concatenate spanning lists of $V_1$ and $V_2$; the concatenation spans $V_1 + V_2$.

**Calibration check.** If you have understood the definition, you should be able to answer: (a) is the subspace of $\mathcal{P}(F)$ consisting of polynomials with constant term zero finite-dimensional? (Answer: no — it contains $z, z^2, z^3, \ldots$, no bound on degree.) (b) is the subspace of $F^\infty$ of eventually-zero sequences finite-dimensional? (Answer: no — it contains $e_n = (0, \ldots, 0, 1, 0, \ldots)$ for arbitrarily large $n$, and these are linearly independent.) (c) is every space with a countably infinite generating set finite-dimensional? (Answer: no — by an extension of the polynomial-degree argument.)

---

# Unlocked by This

> [!tip] Finitely Generated Module *(from Module Theory)*
> A module $M$ over a ring $R$ is **finitely generated** if there exists a finite list of elements $m_1, \ldots, m_k \in M$ such that every element of $M$ is an $R$-linear combination of them. This is the direct generalisation of finite-dimensionality, and most of the structure theory in commutative algebra restricts to finitely generated modules (over Noetherian rings). The contrast with the vector-space case is that finitely-generated does not imply free: $\mathbb{Z}/2\mathbb{Z}$ is finitely-generated as a $\mathbb{Z}$-module (by one element) but is not free (it has 2-torsion).

> [!tip] Finite-Dimensional Banach Space *(from Functional Analysis)*
> A **Banach space** is a complete normed vector space. The category of *finite-dimensional* Banach spaces is essentially trivial: every finite-dimensional normed space is automatically complete, all norms on it are equivalent, every linear map out of it is continuous, and its closed unit ball is compact. The deep theorems of functional analysis — Hahn-Banach, open mapping, closed graph, Banach-Steinhaus — only have nontrivial content in infinite dimensions, where these comforts fail. Finite-dimensional functional analysis collapses to linear algebra; infinite-dimensional functional analysis is its own subject.

> [!tip] Compact Operator *(from Functional Analysis)*
> A linear operator $T : X \to Y$ between Banach spaces is **compact** if it maps the unit ball of $X$ to a relatively compact subset of $Y$. The basic intuition is that compact operators are "almost finite-rank": they can be approximated arbitrarily well in operator norm by linear maps whose range is finite-dimensional. So in a precise sense, compact operators in infinite-dimensional analysis play the role that *all* operators play in finite dimensions — they retain the spectral theory (eigenvalue accumulation at zero, eigenvectors forming a basis modulo a kernel) that fails for general bounded operators in infinite dimensions. Finite-dimensional linear algebra is the "compact operator" limit of infinite-dimensional analysis.

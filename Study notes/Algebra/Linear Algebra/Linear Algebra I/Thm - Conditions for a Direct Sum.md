---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
  - "Def - Sum of Subspaces"
  - "Def - Direct Sum"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over a field $\mathbb{F}$; $V_1, \dots, V_m$ are subspaces of $V$. The sum $V_1 + \dots + V_m = \{v_1 + \dots + v_m : v_k \in V_k\}$ is the set of all sums of elements drawn one from each subspace. The sum is a [[Def - Direct Sum|direct sum]] (written $V_1 \oplus \dots \oplus V_m$) when every element of the sum has a *unique* representation $v = v_1 + \dots + v_m$ with $v_k \in V_k$. See [[Linear Algebra I — §1 Vector Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Condition for a [[Def - Direct Sum|Direct Sum]]).** Let $V_1, \dots, V_m$ be [[Def - Subspace|subspaces]] of a vector space $V$. The sum $V_1 + \dots + V_m$ is a direct sum if and only if the only way to write
> $$0 = v_1 + \dots + v_m$$
> with $v_k \in V_k$ is to take $v_1 = v_2 = \dots = v_m = 0$.

In other words, uniqueness of decomposition at every element of the sum is equivalent to uniqueness of decomposition at the single element $0$. Once you have checked that the zero vector has only the trivial representation, you have certified that every vector has only one representation.

---

# Motivation

A direct sum is *defined* by demanding that every element of the sum have a unique decomposition. This is a condition that must hold for every $v$ in the sum — uncountably many vectors, in general. The theorem says you do not need to verify it for every $v$: checking it for the single vector $0$ is enough. The reason is structural: in any abelian group, the failure of uniqueness propagates to zero by subtraction, so if zero has only the trivial representation, no other element can have a non-trivial multiplicity.

This is the workhorse criterion for direct sums in practice. You almost never check directness by chasing decompositions of a generic vector; you check it by examining the equation $v_1 + \dots + v_m = 0$ and showing each summand must vanish. The condition is a *uniqueness at one point implies uniqueness everywhere* statement, of a kind familiar throughout linear algebra: the linearity of the underlying operations means a single calibration point pins down everything.

The theorem is also the structural reason the **kernel of the addition map** is the key object. The map $\sigma : V_1 \times \dots \times V_m \to V$, $(v_1, \dots, v_m) \mapsto v_1 + \dots + v_m$ is linear (a direct calculation), and $\ker \sigma = \{(v_1, \dots, v_m) : v_1 + \dots + v_m = 0\}$. Directness of the sum is equivalent to injectivity of $\sigma$, which by linearity is equivalent to $\ker \sigma = \{0\}$. So the theorem is really just the linear-algebra principle "a linear map is injective if and only if its kernel is trivial", dressed in the special clothing of the addition map.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of this theorem is bare: a sum $V_1 + \dots + V_m$ of subspaces. The skill is recognizing in a problem that the directness of a particular sum is the right thing to certify. Below are several disguised sources from which one would invoke the theorem.

A first source is **a candidate basis you want to splice together from bases of pieces**. Suppose $\beta_k$ is a basis of $V_k$ for each $k$. The union $\beta = \beta_1 \cup \dots \cup \beta_m$ is a basis of $V_1 + \dots + V_m$ if and only if the sum is direct: directness gives linear independence of the union, and spanning is automatic. The hypothesis "I want $\beta_1 \cup \dots \cup \beta_m$ to be a basis" implies "the sum should be direct", which routes through this theorem. The bridge $B \implies A$ is therefore "I have bases of each piece and want them to splice into a basis", reducible to "I want to check the sum is direct", reducible by this theorem to "I want to check $v_1 + \dots + v_m = 0$ forces each piece to vanish".

A second source is **a decomposition involving projections or idempotents**. If $V \to V$ is an operator with the property $P_1 + \dots + P_m = I$ (the identity) and $P_j P_k = 0$ for $j \neq k$, then $V = \operatorname{im}(P_1) \oplus \dots \oplus \operatorname{im}(P_m)$ — every $v$ decomposes uniquely as $v = P_1 v + \dots + P_m v$. The bridge here is "I have an idempotent decomposition" implies "I have a candidate direct sum decomposition", and to certify it one shows the only way to write $0 = v_1 + \dots + v_m$ is trivially. This is the source behind the spectral theorem (see [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]) and behind the [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces|generalized eigenspace decomposition]].

A third source is **an operator with several invariant subspaces whose union spans $V$**. If $V_1, \dots, V_m$ are $T$-invariant subspaces of $V$ with $V = V_1 + \dots + V_m$, you typically want to extract a decomposition $V = V_1 \oplus \dots \oplus V_m$ that lets you treat the restrictions $T|_{V_k}$ independently. The directness is the additional condition; the source "I have invariant subspaces summing to $V$" lacks it, and this theorem is the test you apply. The bridge to the precondition: take an arbitrary element $0 = v_1 + \dots + v_m$ and try to force each $v_k = 0$, often by exploiting invariance or eigenvalue distinction.

**Targets (Output Amplification)**

The conclusion of this theorem is that the sum is direct — every element has a unique decomposition. Combined with one more property, this turns into structural results.

A first combination is **directness plus a known basis on each piece gives a basis of the sum**. Conclusion $C$: the sum is direct, every $v$ has a unique decomposition. Property $D$: each $V_k$ has a known basis $\beta_k$. Result $E$: the union $\beta_1 \cup \dots \cup \beta_m$ is a basis of $V_1 \oplus \dots \oplus V_m$, of size $\sum |\beta_k|$. The combination is non-obvious because "directness" by itself does not look like a statement about bases, but in conjunction with bases of the pieces it forces a basis of the whole. This is the inductive engine used in proofs that $\dim(V_1 \oplus \dots \oplus V_m) = \sum \dim V_k$.

A second combination is **directness plus surjectivity onto $V$ gives a direct-sum decomposition of $V$**. Conclusion $C$: the sum $V_1 + \dots + V_m$ is direct. Property $D$: $V_1 + \dots + V_m = V$ — the sum equals all of $V$. Result $E$: $V = V_1 \oplus \dots \oplus V_m$, a direct-sum decomposition of $V$, with well-defined projections $\pi_k : V \to V_k$. The combination is non-obvious because directness is purely about the sum's internal structure, while the second condition is about the sum filling $V$ — combining them gives a complete decomposition of $V$. This is the result invoked in every diagonalization theorem.

A third combination is **directness plus a linear map gives independent restrictions**. Conclusion $C$: $V = V_1 \oplus \dots \oplus V_m$. Property $D$: $T : V \to V$ is a linear map preserving each $V_k$ ($T(V_k) \subseteq V_k$). Result $E$: $T$ is completely determined by its restrictions $T|_{V_k} : V_k \to V_k$, and questions about $T$ — its rank, trace, eigenvalues — decompose across the summands. This is the structural content of "block-diagonal matrix": a direct sum decomposition turns operator-theoretic questions into independent questions on each piece. The non-obvious step is recognizing that directness, not just sum, is what permits the decomposition of the operator.

A fourth combination is **directness plus a dimension condition forces equality with $V$**. Conclusion $C$: $V_1 + \dots + V_m$ is a direct sum. Property $D$: $\sum \dim V_k = \dim V$. Result $E$: $V_1 + \dots + V_m = V$, hence $V = V_1 \oplus \dots \oplus V_m$. The combination is non-obvious because dimension counting and uniqueness of decomposition look independent; the fact that they cooperate to certify equality with $V$ is the source of efficient proofs in finite-dimensional setting. The dimension count rules out the sum being strictly smaller than $V$.

---

# Why Is It True

The intuition is one sentence: **in a vector space, uniqueness propagates from zero by subtraction**. That is the entire content.

Suppose some vector $v$ in the sum has two different decompositions, $v = v_1 + \dots + v_m = u_1 + \dots + u_m$ with $v_k, u_k \in V_k$. Then subtracting gives

$$0 = (v_1 - u_1) + (v_2 - u_2) + \dots + (v_m - u_m),$$

with each $v_k - u_k \in V_k$ (since each $V_k$ is a subspace). If the only way to write zero as such a sum is with each summand zero, then every $v_k - u_k = 0$, hence $v_k = u_k$ for every $k$. So the two decompositions of $v$ agree. The argument goes the other way too: if $v$ always has a unique decomposition, then in particular zero has only the trivial decomposition.

**The single one-liner: the zero vector is the universal calibration point — if uniqueness holds there, it holds everywhere, because failure of uniqueness for any other vector would propagate by subtraction to a failure of uniqueness at zero.**

This is the same principle that makes "a linear map is injective if and only if its kernel is trivial". The addition map $\sigma : V_1 \times \dots \times V_m \to V$ is linear; its injectivity (uniqueness of decomposition for every $v$) is equivalent to its kernel being trivial (uniqueness only at zero). The theorem is the statement of this principle for the addition map. Nothing more than linearity is being used.

Why does this principle hold in an abelian group but not in a generic set? Because abelian [[Def - Group|groups]] have *subtraction*: from two equal expressions $v_1 + \dots + v_m = u_1 + \dots + u_m$ one obtains the difference $(v_1 - u_1) + \dots + (v_m - u_m) = 0$. In a non-additive setting there is no subtraction, and the propagation argument breaks. Linearity is the necessary algebraic structure, and the theorem leans entirely on it.

---

# What Makes This Hard

The proof itself is short and entirely mechanical — one direction is immediate, the other is a one-line subtraction argument. The genuine difficulty is conceptual: the theorem is so close to a tautology that students often overlook how much work it is doing. The non-obvious content is that uniqueness at zero implies uniqueness everywhere, which is a non-trivial statement about how linearity propagates information. The most common error is conflating this theorem with [[Thm - Direct Sum of Two Subspaces]] (which says, for two [[Def - Subspace|subspaces]], that directness is equivalent to trivial pairwise intersection); the pairwise intersection criterion fails for three or more subspaces, while the zero-uniqueness criterion is always the right test.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
One direction is obvious — if every element has unique decomposition, then so does the element $0$. The other direction is the subtraction argument: given two decompositions of an element, subtract them to get a decomposition of $0$, which by hypothesis must be trivial; this forces the two decompositions to agree.

**Subgoal decomposition:**

1. **Forward direction:** If $V_1 + \dots + V_m$ is a direct sum, then the only way to write $0 = v_1 + \dots + v_m$ with $v_k \in V_k$ is to take each $v_k = 0$.
   - *Hint:* By definition of direct sum, every element has a unique decomposition; apply this to the element $0$, which trivially decomposes as $0 + 0 + \dots + 0$.
   - *Why needed:* This is the easy direction and establishes that the zero-uniqueness condition is *necessary*.

2. **Reverse direction:** If the only way to write $0 = v_1 + \dots + v_m$ with $v_k \in V_k$ is with each $v_k = 0$, then every element of $V_1 + \dots + V_m$ has a unique decomposition.
   - *Hint:* Suppose $v \in V_1 + \dots + V_m$ has two decompositions, $v = v_1 + \dots + v_m = u_1 + \dots + u_m$. Subtract them to obtain a decomposition of $0$, and use the hypothesis.
   - *Why needed:* This is the substantive direction and establishes that zero-uniqueness is *sufficient*. The subtraction trick is the key step.

---

# Lemma Decomposition

The proof of this theorem is short enough not to require nontrivial lemma decomposition. The two implications are independent enough to be packaged as separate lemmas, however, and doing so makes the structure visible.

> [!note]- Lemma 1: Direct sum implies trivial decomposition of zero
> **Statement:** If $V_1 + \dots + V_m$ is a direct sum, then the only way to write $0 = v_1 + \dots + v_m$ with $v_k \in V_k$ is to take each $v_k = 0$.
>
> **Hint:** The element $0$ is in the sum (taking every $v_k = 0$ gives a decomposition). Uniqueness of decomposition applied to $0$ forces this to be the *only* decomposition.
>
> **Why needed:** This is the forward direction of the biconditional and is the easy half. It shows the zero-uniqueness condition is necessary for directness.
>
> > [!note]- Full proof
> > Suppose $V_1 + \dots + V_m$ is a direct sum. By definition this means every element of the sum has a unique decomposition. The zero vector $0 \in V_1 + \dots + V_m$ admits the decomposition $0 = 0 + 0 + \dots + 0$ (each $0 \in V_k$ since $V_k$ is a subspace). By directness, this must be the only decomposition of $0$. So if $0 = v_1 + \dots + v_m$ with $v_k \in V_k$, then $v_1 = \dots = v_m = 0$.

> [!note]- Lemma 2: Trivial decomposition of zero implies direct sum (by subtraction)
> **Statement:** Suppose the only way to write $0 = v_1 + \dots + v_m$ with $v_k \in V_k$ is to take each $v_k = 0$. Then every element of $V_1 + \dots + V_m$ has a unique decomposition into pieces, one in each $V_k$.
>
> **Hint:** Take an arbitrary element $v$ with two decompositions. Subtract them. The result is a decomposition of $0$, and by hypothesis it must be the trivial one; this forces the two decompositions of $v$ to agree.
>
> **Why needed:** This is the reverse direction and is the substantive content of the theorem. The subtraction argument is the key technique.
>
> > [!note]- Full proof
> > Let $v \in V_1 + \dots + V_m$, so $v = v_1 + \dots + v_m$ for some $v_k \in V_k$. To prove uniqueness, suppose also $v = u_1 + \dots + u_m$ with $u_k \in V_k$. Subtracting the two equations gives
> > $$0 = (v_1 - u_1) + (v_2 - u_2) + \dots + (v_m - u_m).$$
> > Each $v_k - u_k$ lies in $V_k$ because $V_k$ is a subspace (closed under subtraction). By the hypothesis on $0$, this forces $v_k - u_k = 0$ for every $k$, i.e. $v_k = u_k$. So the two decompositions agree, and the decomposition of $v$ is unique.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $V_1, \dots, V_m$ be subspaces of a vector space $V$. The sum $V_1 + \dots + V_m$ is a direct sum if and only if the only choice of $v_1 \in V_1, \dots, v_m \in V_m$ satisfying $v_1 + \dots + v_m = 0$ is $v_1 = \dots = v_m = 0$.
>
> *Proof.* ($\Rightarrow$) Suppose $V_1 + \dots + V_m$ is a direct sum. Then every element of the sum has a unique decomposition. The zero vector admits the decomposition $0 = 0 + 0 + \dots + 0$ with each $0 \in V_k$, so by directness this is the only such decomposition. Hence if $v_1 + \dots + v_m = 0$ with $v_k \in V_k$, then each $v_k = 0$.
>
> ($\Leftarrow$) Suppose the only way to write $0 = v_1 + \dots + v_m$ with $v_k \in V_k$ is trivially. Let $v \in V_1 + \dots + V_m$ be arbitrary, with $v = v_1 + \dots + v_m$ for some $v_k \in V_k$. To prove uniqueness of this decomposition, suppose also $v = u_1 + \dots + u_m$ with $u_k \in V_k$. Subtracting,
> $$0 = (v_1 + \dots + v_m) - (u_1 + \dots + u_m) = (v_1 - u_1) + \dots + (v_m - u_m).$$
> Because each $V_k$ is a subspace, $v_k - u_k \in V_k$. By hypothesis applied to this expression of $0$, each $v_k - u_k = 0$, i.e. $v_k = u_k$. So the decomposition of $v$ is unique, and the sum $V_1 + \dots + V_m$ is direct. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Internal direct products in abelian group theory.** A [[Def - Subgroup|subgroup]] $H \leq G$ of an [[Def - Abelian Group|abelian group]] is a direct summand if there exists $K$ with $G = H + K$ and $H \cap K = \{0\}$. The theorem here generalizes to abelian [[Def - Group|groups]] (or even to [[Def - Module|modules]] over a [[Def - Ring|ring]]) in the form: an internal sum is a direct sum if and only if the only decomposition of $0$ is trivial. So this theorem applies verbatim to abelian groups and to [[Def - Module|modules]], with the same proof. The non-obvious application: in classifying finite abelian groups, certifying the direct-sum decomposition into cyclic groups of prime-power order amounts to this criterion.

**Decomposition of representations of groups (Maschke's theorem).** A representation of a finite group $G$ on a vector space $V$ (over a field of characteristic not dividing $|G|$) decomposes as a direct sum of irreducible subrepresentations. The proof produces invariant complementary subspaces using the averaging trick, and certifies directness via this theorem applied to the candidate decomposition. The bridge from "I have a representation" to "I want a direct sum decomposition" passes through the criterion of this theorem.

**Splitting of short exact sequences in homological algebra.** A short exact sequence $0 \to U \to V \to W \to 0$ in $\mathbf{Vect}_{\mathbb{F}}$ splits if and only if $V = \iota(U) \oplus s(W)$ for some section $s : W \to V$. The directness here is verified via the present theorem: any element of $\iota(U) + s(W)$ has a unique decomposition because $\iota$ and $s$ are injective and their images intersect trivially. The application is non-obvious because exact sequences look like a chain of maps, not a sum of subspaces — but every exact sequence implicitly contains such sums.

**Fourier decomposition of $L^2$ functions.** The Hilbert space $L^2([-\pi, \pi])$ is the *closed* direct sum (Hilbert sum) of the one-dimensional eigenspaces $\operatorname{span}(e^{inx})$, $n \in \mathbb{Z}$. The directness is the orthogonality $\langle e^{inx}, e^{imx} \rangle = 0$ for $n \neq m$, which by the theorem corresponds to the unique decomposition of $0$. This is the algebraic skeleton of Fourier series: convergence of Fourier expansions is the analytical statement that the algebraic direct sum exhausts $L^2$ in the closed-span sense.

---

# Bridges

- **[[Thm - Direct Sum of Two Subspaces]]** — for the special case $m = 2$, the directness condition simplifies: $U + W$ is a direct sum if and only if $U \cap W = \{0\}$. The simplification is real and useful, but it does not generalize: three subspaces in $\mathbb{F}^3$ can pairwise intersect only at $0$ and still fail to form a direct sum (LADR Example 1.44 — see [[Def - Direct Sum]]). So the present theorem is the right criterion for $m \geq 3$, while the pairwise-intersection criterion is a strictly weaker condition that suffices only in the two-summand case.

- **Linearity of the addition map** — the addition map $\sigma : V_1 \times \dots \times V_m \to V_1 + \dots + V_m$, $(v_1, \dots, v_m) \mapsto v_1 + \dots + v_m$, is a linear map between vector spaces. Surjectivity of $\sigma$ is the definition of the sum; injectivity of $\sigma$ — equivalently, trivial kernel — is the direct-sum condition. This theorem is therefore the special case of the general principle "a linear map is injective if and only if its kernel is trivial" applied to $\sigma$. The two phrasings — "uniqueness of decomposition" and "trivial kernel of $\sigma$" — are the same fact in different clothes.

- **Linear independence of vectors** — vectors $v_1, \dots, v_n \in V$ are linearly independent precisely when the one-dimensional subspaces $\operatorname{span}(v_k)$ satisfy this theorem's hypothesis: the only way to write $0 = a_1 v_1 + \dots + a_n v_n$ is with every $a_k = 0$. So **linear independence is the special case of directness for one-dimensional subspaces**. The two concepts are not analogues; they are the same statement at different scales — see [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

- **Splitting of short exact sequences** — in any abelian category, a short exact sequence $0 \to U \to V \to W \to 0$ splits if and only if $V = \iota(U) \oplus s(W)$ for some section $s$. The directness is certified by this theorem, and the splitting is the structural reason vector spaces have well-behaved direct-sum decompositions. The theorem holds for all modules; the splitting of every short exact sequence is what distinguishes vector spaces (semisimple) from general modules.

---

# Unlocked by This

> [!tip] Block-Diagonal Matrices and Operator Decomposition *(from Linear Algebra V, VIII)*
> A direct sum decomposition $V = V_1 \oplus \dots \oplus V_m$ that is **invariant** under a linear operator $T$ (each $T(V_k) \subseteq V_k$) lets us represent $T$ as a block-diagonal matrix — the restrictions $T|_{V_k}$ are independent operators on the pieces. This is the structural content of "diagonalize", "Jordan form", and "spectral decomposition": find a direct-sum decomposition that the operator preserves. The certification of directness in any specific case routes through this theorem.

> [!tip] Module Theory: Semisimple Modules *(from Algebra)*
> A module is **semisimple** if every submodule is a direct summand — equivalently, the module is a direct sum of simple submodules. Vector spaces are always semisimple. The general module-theoretic concept of semisimplicity, and its applications to representation theory and Wedderburn's theorem, are downstream of the directness criterion in this theorem.

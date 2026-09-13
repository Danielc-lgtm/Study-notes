---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Classical Matrix Groups"
  - "Thm - The Closed Subgroup Theorem"
  - "Def - Subgroup"
  - "Def - Continuous Map"
  - "Thm - Determinant is Multiplicative"
difficulty: "⭐"
tags: [geometry, gauge-theory, lie-groups, matrix-groups]
---

# Problem Statement

Throughout the series, manifolds are smooth, Hausdorff, and second countable, and "smooth" means $C^\infty$. The letter $\mathbb{K}$ stands for one of the fields $\mathbb{R}$ and $\mathbb{C}$, $n$ is a positive integer, $\operatorname{Mat}(n \times n; \mathbb{K})$ is the $\mathbb{K}$-vector space of $n \times n$ matrices with entries in $\mathbb{K}$, identified with $\mathbb{R}^{n^2}$ (real case) or with $\mathbb{R}^{2n^2}$ (complex case, by splitting every entry $A_{jk} = x_{jk} + i y_{jk}$ into real and imaginary parts), and $GL(n; \mathbb{K}) = \{A \in \operatorname{Mat}(n \times n; \mathbb{K}) : \det A \neq 0\}$ is the general linear group, an open subset of $\operatorname{Mat}(n \times n; \mathbb{K})$ and a Lie group with the smooth structure of an open subset (this is Block A of [[Def - Classical Matrix Groups]] and DG I's [[Ex - The General Linear Group is a Smooth Manifold]]). For a matrix $A$ we write $A^t$ for the transpose, $(A^t)_{jk} = A_{kj}$, $\bar{A}$ for the entrywise complex conjugate, and $A^* := (\bar{A})^t$ for the conjugate transpose; $1_n$ is the identity matrix. This page depends on no sign or action convention.

Prove that each of the six subsets
$$O(n) = \{A \in GL(n; \mathbb{R}) : A^t A = 1_n\}, \qquad SL(n; \mathbb{R}) = \{A \in \operatorname{Mat}(n \times n; \mathbb{R}) : \det A = 1\}, \qquad SO(n) = O(n) \cap SL(n; \mathbb{R}),$$
$$U(n) = \{A \in \operatorname{Mat}(n \times n; \mathbb{C}) : A^* A = 1_n\}, \qquad SL(n; \mathbb{C}) = \{A \in \operatorname{Mat}(n \times n; \mathbb{C}) : \det A = 1\}, \qquad SU(n) = U(n) \cap SL(n; \mathbb{C})$$
is (a) a subgroup of $GL(n; \mathbb{K})$ for the appropriate field, and (b) a closed subset of $GL(n; \mathbb{K})$ in the manifold topology, and conclude (c) that each is a Lie group — indeed an embedded Lie subgroup of $GL(n; \mathbb{K})$ — by the closed subgroup theorem. For (b), exhibit each group as the preimage of a closed set under one of the three continuous maps
$$\tau : A \mapsto A^t A, \qquad \det : A \mapsto \det A, \qquad \mu : A \mapsto A^* A,$$
or as an intersection of two sets already shown to be closed.

This is Bär's Example 1.1.4 (source items E1.1.4 and E1.1.5). Bär writes out the verification for $O(n)$ and lists the other five without verification; here every one of the six is verified in full. Bär's item 5 misprints $SL(n; \mathbb{C})$ as "$SL(n; \mathbb{R}) := \{A \in \operatorname{Mat}(n \times n; \mathbb{C}) \mid \det A = 1\}$"; the corrected name $SL(n; \mathbb{C})$ is used throughout, as the definition of $SU(n) = U(n) \cap SL(n; \mathbb{C})$ in his item 6 confirms.

**Recall:**

The groups are those of the definition page; the subgroup axioms, the closed-set formulation of continuity, the multiplicativity of the determinant, and the closed subgroup theorem are the four tools.

![[Def - Classical Matrix Groups#The Definition]]

![[Def - Subgroup#The Definition]]

A subset $H$ of a group $G$ is a [[Def - Subgroup|subgroup]] when it contains the identity, is closed under the group operation, and is closed under inversion; associativity is inherited from $G$.

![[Def - Continuous Map#The Definition]]

The formulation we use is the closed-set one: a map $f : X \to Y$ between topological spaces is [[Def - Continuous Map|continuous]] if and only if $f^{-1}(F)$ is closed in $X$ for every closed $F \subseteq Y$. Two further elementary facts are used. First, if $f : X \to Y$ is continuous and $Z \subseteq X$ carries the subspace topology, then the restriction $f|_Z : Z \to Y$ is continuous, because $(f|_Z)^{-1}(F) = f^{-1}(F) \cap Z$, which is closed in the subspace topology of $Z$ whenever $f^{-1}(F)$ is closed in $X$. Second, in a metric space every singleton $\{p\}$ is closed, because every point $x \neq p$ has the open ball of radius $d(x, p) > 0$ about it disjoint from $\{p\}$, so the complement of $\{p\}$ is open.

![[Thm - Determinant is Multiplicative#Statement]]

For $A, B \in \operatorname{Mat}(n \times n; \mathbb{K})$, $\det(AB) = \det A \cdot \det B$ ([[Thm - Determinant is Multiplicative]]); consequently $A$ is invertible if and only if $\det A \neq 0$, and then $\det(A^{-1}) = 1 / \det A$ (the corollary on the same page). From the Leibniz formula on [[Def - Determinant]], $\det(A^t) = \det A$ (the transpose corollary there) and, for complex matrices, $\det(\bar{A}) = \overline{\det A}$, because complex conjugation is a field automorphism of $\mathbb{C}$ and fixes the signs $\operatorname{sign}(\sigma) = \pm 1$, so it can be pulled through the finite sums and products of the Leibniz formula.

![[Thm - The Closed Subgroup Theorem#Statement]]

The [[Thm - The Closed Subgroup Theorem|closed subgroup theorem]]: if $G$ is a Lie group and $H \subseteq G$ is a subgroup that is closed as a subset of $G$, then $H$ is an embedded Lie subgroup of $G$ — an embedded submanifold, and a Lie group with the restricted operations.

---

# Convergent Strategy

**Problem class:** This is a *verify-the-hypotheses-then-apply* problem. The conclusion "is a Lie group" is expensive to obtain by hand — one would need charts on each group and proofs that multiplication and inversion are smooth in those charts — and the closed subgroup theorem converts that expense into two cheap checks, one algebraic (subgroup) and one topological (closed). The whole exercise is the discipline of carrying out both checks, for all six groups, without skipping the ones that look routine. It is the first instance in the series of a pattern that recurs whenever a structure group is introduced: a group presented as the solution set of matrix equations inside $GL(n; \mathbb{K})$ is a Lie group as soon as the equations are respected by products and inverses and are continuous.

**Assumption pattern:** Each of the six groups is defined by an equation of the form $f(A) = c$ where $f$ is one of $\tau$, $\det$, $\mu$ and $c$ is $1_n$ or $1$, or by two such equations at once. The recognisable feature of each $f$ is that it is *polynomial in the real coordinates of $A$*, which gives continuity for free, and that it is *multiplicative in the appropriate sense* — $\tau(AB) = B^t \tau(A) B$, $\det(AB) = \det A \det B$, $\mu(AB) = B^* \mu(A) B$ — which gives closure under products for free once $\tau(A)$, respectively $\det A$, $\mu(A)$, is the identity. The intersections $SO(n)$ and $SU(n)$ need nothing new: an intersection of subgroups is a subgroup and an intersection of closed sets is closed.

**Theorem routing:** The route is: (1) establish once that $\tau$, $\det$, $\mu$ are continuous on $\operatorname{Mat}(n \times n; \mathbb{K})$, hence on the subspace $GL(n; \mathbb{K})$, and that $\{1_n\}$ and $\{1\}$ are closed; (2) for $O(n)$, $SL(n; \mathbb{K})$, $U(n)$ verify the three subgroup axioms from the algebra of transposes, determinants, and adjoints, using [[Thm - Determinant is Multiplicative]] and the transpose and conjugation corollaries of [[Def - Determinant]], and read off closedness as $f^{-1}(\{c\}) \cap GL(n; \mathbb{K})$; (3) for $SO(n)$, $SU(n)$ intersect; (4) invoke [[Thm - The Closed Subgroup Theorem]] with $G = GL(n; \mathbb{K})$, whose Lie group structure is established on [[Def - Classical Matrix Groups]].

**Key decision point:** The one place where a reader must decide rather than compute is *which ambient space the word "closed" refers to*. The closed subgroup theorem needs $H$ closed in the Lie group $G = GL(n; \mathbb{K})$, while the natural continuity argument produces a set closed in $\operatorname{Mat}(n \times n; \mathbb{K})$. The two are reconciled by restricting the continuous map to $GL(n; \mathbb{K})$ with its subspace topology, and by noting that every one of the six groups actually lies inside $GL(n; \mathbb{K})$ — for $SL(n; \mathbb{K})$ because $\det A = 1 \neq 0$, for $U(n)$ because $A^* A = 1_n$ forces $|\det A|^2 = 1$. The second decision, smaller but real, is to get the inverse axiom for $O(n)$ and $U(n)$ from the identity $A^{-1} = A^t$, respectively $A^{-1} = A^*$, which is itself a consequence of the defining equation and invertibility, rather than by any computation with entries.

---

# Legal Operations Used

The topic page's Legal Operations are not yet numbered when this page is written; each operation below is named descriptively so that the numbers can be reconciled once the topic page exists.

1. **Recognise a closed subgroup by the "polynomial equation respected by products" pattern.** Whenever a subset of $GL(n; \mathbb{K})$ is cut out by an equation $f(A) = c$ with $f$ polynomial in the entries and $f$ transforming under products by a rule that fixes the fibre over $c$, the subset is a closed subgroup. Here the pattern is applied three times, with $f = \tau$, $\det$, $\mu$.

2. **Read closedness off continuity (the preimage-of-a-closed-set operation).** A polynomial map between Euclidean spaces is continuous, a singleton in a metric space is closed, so the fibre $f^{-1}(\{c\})$ is closed; intersecting with $GL(n; \mathbb{K})$ gives a set closed in the subspace topology of $GL(n; \mathbb{K})$. This is applied in Step 0 and Steps 1–3.

3. **Derive the inverse axiom from the defining equation plus invertibility.** For $A^t A = 1_n$ with $A$ invertible, multiplying on the right by $A^{-1}$ gives $A^t = A^{-1}$; the inverse then satisfies the same equation because $(A^{-1})^t A^{-1} = A A^t = A A^{-1} = 1_n$. The same operation with $*$ in place of $t$ handles $U(n)$. Applied in Steps 1 and 3.

4. **Pass structure through intersections.** The intersection of two subgroups is a subgroup, the intersection of two closed sets is closed; therefore the intersection of two closed subgroups is a closed subgroup. Applied in Step 4 to $SO(n)$ and $SU(n)$.

5. **Upgrade a closed subgroup to a Lie group by the closed subgroup theorem.** With $G = GL(n; \mathbb{K})$ a Lie group and $H$ a closed subgroup, [[Thm - The Closed Subgroup Theorem]] yields that $H$ is an embedded submanifold and a Lie group with the restricted operations. Applied in Step 5.

---

# Hints

> [!note]- Hint 1
> Separate the two halves of the job. The algebraic half ("subgroup") needs only three checks per group: identity, products, inverses. The topological half ("closed") needs only one observation per group: the group is $f^{-1}(\{c\})$ for a continuous $f$ and a closed $\{c\}$. Do the topological half first, because it is the same for all six groups.

> [!note]- Hint 2
> For continuity, write out one entry. The $(j, k)$ entry of $A^t A$ is $\sum_{l=1}^n A_{lj} A_{lk}$, a polynomial of degree two in the entries of $A$; the determinant is a polynomial of degree $n$ by the Leibniz formula; the $(j, k)$ entry of $A^* A$ is $\sum_l \overline{A_{lj}} A_{lk}$, whose real and imaginary parts are polynomials in the real and imaginary parts of the entries. A map into $\mathbb{R}^N$ all of whose components are polynomials is continuous.

> [!note]- Hint 3
> For the product axiom, use that transposition and conjugate transposition reverse products: $(AB)^t = B^t A^t$ and $(AB)^* = B^* A^*$. Then $(AB)^t (AB) = B^t (A^t A) B$, and if $A^t A = 1_n$ this is $B^t B$. For the inverse axiom, do not compute entries of $A^{-1}$: instead show $A^t = A^{-1}$ from $A^t A = 1_n$ by multiplying on the right by $A^{-1}$.

> [!note]- Hint 4
> Bär defines $SL(n; \mathbb{K})$ and $U(n)$ inside $\operatorname{Mat}(n \times n; \mathbb{K})$, not inside $GL(n; \mathbb{K})$; before the closed subgroup theorem can be applied, you must check that these sets lie in $GL(n; \mathbb{K})$ and are closed *there*. For $U(n)$, take determinants of $A^* A = 1_n$ and use $\det(A^*) = \overline{\det A}$ to get $|\det A|^2 = 1$.

> [!note]- Hint 5
> $SO(n)$ and $SU(n)$ are intersections of two sets each of which you have already shown to be a closed subgroup. Check the three subgroup axioms for an intersection $H_1 \cap H_2$ one clause at a time, and recall that the complement of $F_1 \cap F_2$ is the union of the complements.

---

# Solution

The plan is to separate the topological input from the algebraic input. Step 0 shows once and for all that the three maps $\tau$, $\det$, $\mu$ are continuous and that the target points are closed, so that the fibre of each map over its target is closed in $GL(n; \mathbb{K})$. Steps 1 to 3 then verify, for $O(n)$, $SL(n; \mathbb{K})$, and $U(n)$ respectively, that the set lies in $GL(n; \mathbb{K})$, satisfies the three subgroup axioms, and equals the closed fibre of Step 0; Step 4 handles the two intersections $SO(n)$ and $SU(n)$; and Step 5 applies the closed subgroup theorem to each of the six closed subgroups, with $G = GL(n; \mathbb{K})$.

**Step 0: The three maps are continuous and the fibres over the identity are closed in $GL(n; \mathbb{K})$ — the topological half, done once.**

The maps $\tau : \operatorname{Mat}(n \times n; \mathbb{R}) \to \operatorname{Mat}(n \times n; \mathbb{R})$, $\det : \operatorname{Mat}(n \times n; \mathbb{K}) \to \mathbb{K}$, and $\mu : \operatorname{Mat}(n \times n; \mathbb{C}) \to \operatorname{Mat}(n \times n; \mathbb{C})$ are continuous, the singletons $\{1_n\}$ and $\{1\}$ are closed, and therefore each of $\tau^{-1}(\{1_n\}) \cap GL(n; \mathbb{R})$, $\det^{-1}(\{1\}) \cap GL(n; \mathbb{K})$, $\mu^{-1}(\{1_n\}) \cap GL(n; \mathbb{C})$ is a closed subset of $GL(n; \mathbb{K})$ in the subspace topology inherited from $\operatorname{Mat}(n \times n; \mathbb{K})$.

> [!note]- Derivation
> We need to show that each of the three maps is continuous as a map between Euclidean spaces, that the fibre targets are closed, and that the fibres are closed in $GL(n; \mathbb{K})$ rather than merely in $\operatorname{Mat}(n \times n; \mathbb{K})$.
>
> **Polynomial maps are continuous.** Let $P : \mathbb{R}^N \to \mathbb{R}^M$ be a map each of whose $M$ components $P_1, \dots, P_M : \mathbb{R}^N \to \mathbb{R}$ is a polynomial in the $N$ coordinates. Each coordinate projection $x \mapsto x_r$ is continuous (it is $1$-Lipschitz), constants are continuous, and sums and products of continuous real-valued functions are continuous; a polynomial is a finite sum of finite products of coordinate projections and constants, hence continuous. A map into $\mathbb{R}^M$ is continuous if and only if each component is continuous (the product topology on $\mathbb{R}^M$ is the topology of the Euclidean norm, and a sequence converges in the norm if and only if it converges componentwise). Therefore $P$ is continuous.
>
> **The map $\tau$.** Identify $\operatorname{Mat}(n \times n; \mathbb{R}) = \mathbb{R}^{n^2}$ with coordinates $(A_{jk})_{1 \le j, k \le n}$. The $(j, k)$ entry of $\tau(A) = A^t A$ is
> $$(A^t A)_{jk} = \sum_{l=1}^n (A^t)_{jl} A_{lk} = \sum_{l=1}^n A_{lj} A_{lk} \qquad \text{(definition of matrix product; definition of transpose } (A^t)_{jl} = A_{lj}\text{)},$$
> a polynomial of degree two in the coordinates. So $\tau$ is a polynomial map $\mathbb{R}^{n^2} \to \mathbb{R}^{n^2}$, hence continuous.
>
> **The map $\det$, real case.** By the Leibniz formula ([[Def - Determinant]]),
> $$\det A = \sum_{\sigma \in S_n} \operatorname{sign}(\sigma) \, A_{1 \sigma(1)} A_{2 \sigma(2)} \cdots A_{n \sigma(n)} \qquad \text{(Leibniz formula; } S_n \text{ the symmetric group on } n \text{ letters)},$$
> a polynomial of degree $n$ in the $n^2$ coordinates, hence continuous $\mathbb{R}^{n^2} \to \mathbb{R}$.
>
> **The maps $\det$ and $\mu$, complex case.** Identify $\operatorname{Mat}(n \times n; \mathbb{C}) = \mathbb{R}^{2n^2}$ by $A_{jk} = x_{jk} + i y_{jk}$, and $\mathbb{C} = \mathbb{R}^2$ by real and imaginary part. Each product $A_{1\sigma(1)} \cdots A_{n\sigma(n)}$ has real and imaginary parts that are polynomials in the $x_{jk}, y_{jk}$, because the real and imaginary parts of a product $(x + iy)(x' + iy') = (xx' - yy') + i(xy' + yx')$ are polynomials in $x, y, x', y'$ and this extends to $n$-fold products by induction on the number of factors; a finite signed sum of such products has the same property. So $\det : \mathbb{R}^{2n^2} \to \mathbb{R}^2$ is a polynomial map, hence continuous. For $\mu$, the $(j, k)$ entry of $\mu(A) = A^* A$ is
> $$(A^* A)_{jk} = \sum_{l=1}^n (A^*)_{jl} A_{lk} = \sum_{l=1}^n \overline{A_{lj}} \, A_{lk} \qquad \text{(definition of matrix product; } A^* = (\bar{A})^t \text{ so } (A^*)_{jl} = \overline{A_{lj}}\text{)},$$
> and for a single summand
> $$\overline{A_{lj}} \, A_{lk} = (x_{lj} - i y_{lj})(x_{lk} + i y_{lk}) = (x_{lj} x_{lk} + y_{lj} y_{lk}) + i \,(x_{lj} y_{lk} - y_{lj} x_{lk}) \qquad \text{(expand; } i^2 = -1\text{)},$$
> whose real and imaginary parts are polynomials in the real coordinates. Summing over $l$, both the real and the imaginary part of every entry of $\mu(A)$ are polynomials in the $2n^2$ real coordinates of $A$; so $\mu : \mathbb{R}^{2n^2} \to \mathbb{R}^{2n^2}$ is a polynomial map, hence continuous.
>
> **The fibre targets are closed.** $\operatorname{Mat}(n \times n; \mathbb{K})$ and $\mathbb{K}$ are metric spaces (Euclidean spaces $\mathbb{R}^N$), and in a metric space every singleton is closed: for $x \neq p$, the open ball of radius $d(x, p) > 0$ about $x$ does not contain $p$, so the complement of $\{p\}$ is a union of open balls, hence open. Thus $\{1_n\}$ is closed in $\operatorname{Mat}(n \times n; \mathbb{K})$ and $\{1\}$ is closed in $\mathbb{K}$.
>
> **The fibres are closed in $GL(n; \mathbb{K})$.** By the closed-set formulation of [[Def - Continuous Map|continuity]], $\tau^{-1}(\{1_n\})$, $\det^{-1}(\{1\})$, and $\mu^{-1}(\{1_n\})$ are closed in the respective spaces $\operatorname{Mat}(n \times n; \mathbb{K})$. The manifold topology of $GL(n; \mathbb{K})$ is the subspace topology of the open subset $GL(n; \mathbb{K}) \subseteq \operatorname{Mat}(n \times n; \mathbb{K})$ (this is the smooth structure of an open subset, [[Def - Classical Matrix Groups]] Block A). A subset of $GL(n; \mathbb{K})$ is closed in the subspace topology if and only if it is of the form $F \cap GL(n; \mathbb{K})$ with $F$ closed in $\operatorname{Mat}(n \times n; \mathbb{K})$ (by definition of the subspace topology, an open set of the subspace is $W \cap GL(n; \mathbb{K})$ with $W$ open in the ambient space, and taking complements inside $GL(n; \mathbb{K})$ turns this into the statement for closed sets). Hence
> $$\tau^{-1}(\{1_n\}) \cap GL(n; \mathbb{R}), \qquad \det^{-1}(\{1\}) \cap GL(n; \mathbb{K}), \qquad \mu^{-1}(\{1_n\}) \cap GL(n; \mathbb{C})$$
> are closed subsets of $GL(n; \mathbb{R})$, $GL(n; \mathbb{K})$, $GL(n; \mathbb{C})$ respectively. Equivalently, these are the fibres over $1_n$, $1$, $1_n$ of the restrictions $\tau|_{GL(n; \mathbb{R})}$, $\det|_{GL(n; \mathbb{K})}$, $\mu|_{GL(n; \mathbb{C})}$, which are continuous as restrictions of continuous maps to a subspace. This is the topological input for all six groups.

**Step 1: $O(n)$ is a closed subgroup of $GL(n; \mathbb{R})$ — Bär's item 1, written out.**

$O(n)$ contains $1_n$, is closed under products because transposition reverses products, and is closed under inverses because $A^t A = 1_n$ with $A$ invertible forces $A^{-1} = A^t$; and $O(n) = \tau^{-1}(\{1_n\}) \cap GL(n; \mathbb{R})$ is closed by Step 0.

> [!note]- Derivation
> We need to show three subgroup axioms and one identification of sets. Recall that $O(n)$ is defined as a subset of $GL(n; \mathbb{R})$, so invertibility of its elements is part of the hypothesis; we note in passing that the equation alone already forces it, since $A^t A = 1_n$ gives $\det(A^t) \det A = \det 1_n = 1$ by [[Thm - Determinant is Multiplicative]], that is, $(\det A)^2 = 1$ by the transpose corollary $\det A^t = \det A$, so $\det A = \pm 1 \neq 0$.
>
> **Transposition reverses products.** For $A, B \in \operatorname{Mat}(n \times n; \mathbb{R})$ and all $j, k$,
> $$((AB)^t)_{jk} = (AB)_{kj} = \sum_{l=1}^n A_{kl} B_{lj} = \sum_{l=1}^n (B^t)_{jl} (A^t)_{lk} = (B^t A^t)_{jk} \qquad \text{(definition of transpose; definition of product; transpose again; commutativity of multiplication in } \mathbb{R}\text{)},$$
> so $(AB)^t = B^t A^t$. Also $(A^t)^t = A$, since $((A^t)^t)_{jk} = (A^t)_{kj} = A_{jk}$.
>
> **Identity.** $1_n^t = 1_n$ (the identity matrix is symmetric, $(1_n)_{jk} = \delta_{jk} = \delta_{kj}$), so $1_n^t 1_n = 1_n 1_n = 1_n$; hence $1_n \in O(n)$.
>
> **Products.** Let $A, B \in O(n)$, so $A^t A = 1_n$ and $B^t B = 1_n$. Then
> $$(AB)^t (AB) = (B^t A^t)(AB) = B^t (A^t A) B = B^t \, 1_n \, B = B^t B = 1_n \qquad \text{(transposition reverses products; associativity of matrix multiplication; } A \in O(n)\text{; } 1_n \text{ is the identity; } B \in O(n)\text{)}.$$
> Also $AB \in GL(n; \mathbb{R})$ since $\det(AB) = \det A \det B \neq 0$ (multiplicativity; a product of nonzero reals is nonzero). Hence $AB \in O(n)$.
>
> **Inverses.** Let $A \in O(n)$. Since $A \in GL(n; \mathbb{R})$, the inverse $A^{-1}$ exists, and
> $$A^t = A^t (A A^{-1}) = (A^t A) A^{-1} = 1_n A^{-1} = A^{-1} \qquad \text{(} A A^{-1} = 1_n\text{; associativity; } A \in O(n)\text{; } 1_n \text{ is the identity)}.$$
> Therefore
> $$(A^{-1})^t A^{-1} = (A^t)^t A^t = A A^t = A A^{-1} = 1_n \qquad \text{(} A^{-1} = A^t \text{ twice; } (A^t)^t = A\text{; } A^t = A^{-1} \text{ again)},$$
> and $A^{-1} \in GL(n; \mathbb{R})$ because its inverse is $A$. Hence $A^{-1} \in O(n)$.
>
> **Closedness.** By definition, $A \in O(n)$ if and only if $A \in GL(n; \mathbb{R})$ and $\tau(A) = A^t A = 1_n$; that is, $O(n) = \tau^{-1}(\{1_n\}) \cap GL(n; \mathbb{R})$, which is closed in $GL(n; \mathbb{R})$ by Step 0. This is Bär's sentence "$A \mapsto A^t A$ is continuous, i.e. $A^t A = 1_n$ is a closed condition", with the continuity and the subspace-topology bookkeeping made explicit.
>
> Therefore $O(n)$ is a closed subgroup of $GL(n; \mathbb{R})$.

**Step 2: $SL(n; \mathbb{R})$ and $SL(n; \mathbb{C})$ are closed subgroups of $GL(n; \mathbb{R})$ and $GL(n; \mathbb{C})$ — Bär's items 2 and 5, with the misprint corrected.**

For either field, $SL(n; \mathbb{K}) \subseteq GL(n; \mathbb{K})$ because $\det A = 1 \neq 0$; the subgroup axioms are the three identities $\det 1_n = 1$, $\det(AB) = \det A \det B$, $\det(A^{-1}) = 1 / \det A$; and $SL(n; \mathbb{K}) = \det^{-1}(\{1\}) \cap GL(n; \mathbb{K})$ is closed by Step 0.

> [!note]- Derivation
> We treat both fields at once; every step below uses only that $\mathbb{K}$ is a field and that [[Thm - Determinant is Multiplicative]] holds over any field. Bär's item 5 prints the name $SL(n; \mathbb{R})$ for the set $\{A \in \operatorname{Mat}(n \times n; \mathbb{C}) : \det A = 1\}$; this is a misprint for $SL(n; \mathbb{C})$, and the argument is identical for the two fields.
>
> **Containment in $GL(n; \mathbb{K})$.** If $\det A = 1$ then $\det A \neq 0$, so $A \in GL(n; \mathbb{K})$ by the corollary to [[Thm - Determinant is Multiplicative]] (a square matrix is invertible if and only if its determinant is nonzero). Hence $SL(n; \mathbb{K}) \subseteq GL(n; \mathbb{K})$, and the definition inside $\operatorname{Mat}(n \times n; \mathbb{K})$ agrees with the definition inside $GL(n; \mathbb{K})$ used on [[Def - Classical Matrix Groups]].
>
> **Identity.** $\det 1_n = 1$: in the Leibniz formula only the identity permutation contributes a nonzero product (every other permutation moves some index $j$ to $\sigma(j) \neq j$ and the factor $(1_n)_{j \sigma(j)} = 0$), and that product is $1 \cdots 1 = 1$ with sign $+1$. So $1_n \in SL(n; \mathbb{K})$.
>
> **Products.** For $A, B \in SL(n; \mathbb{K})$,
> $$\det(AB) = \det A \cdot \det B = 1 \cdot 1 = 1 \qquad \text{(multiplicativity of the determinant; } A, B \in SL(n; \mathbb{K})\text{)},$$
> so $AB \in SL(n; \mathbb{K})$.
>
> **Inverses.** For $A \in SL(n; \mathbb{K})$, the inverse exists by the containment just shown, and
> $$1 = \det 1_n = \det(A A^{-1}) = \det A \cdot \det(A^{-1}) = 1 \cdot \det(A^{-1}) = \det(A^{-1}) \qquad \text{(} \det 1_n = 1\text{; } A A^{-1} = 1_n\text{; multiplicativity; } \det A = 1\text{)},$$
> so $A^{-1} \in SL(n; \mathbb{K})$.
>
> **Closedness.** By definition and the containment, $SL(n; \mathbb{K}) = \det^{-1}(\{1\}) \cap GL(n; \mathbb{K})$, which is closed in $GL(n; \mathbb{K})$ by Step 0 (real case for $\mathbb{K} = \mathbb{R}$, complex case for $\mathbb{K} = \mathbb{C}$).
>
> Therefore $SL(n; \mathbb{R})$ is a closed subgroup of $GL(n; \mathbb{R})$ and $SL(n; \mathbb{C})$ is a closed subgroup of $GL(n; \mathbb{C})$.

**Step 3: $U(n)$ is a closed subgroup of $GL(n; \mathbb{C})$ — Bär's item 4.**

The argument of Step 1 goes through with $*$ in place of $t$, once two facts are in place: conjugate transposition reverses products, $(AB)^* = B^* A^*$, and every $A$ with $A^* A = 1_n$ is invertible because $|\det A|^2 = 1$; then $U(n) = \mu^{-1}(\{1_n\}) \cap GL(n; \mathbb{C})$ is closed by Step 0.

> [!note]- Derivation
> We need to show that $U(n) \subseteq GL(n; \mathbb{C})$ (Bär defines $U(n)$ inside $\operatorname{Mat}(n \times n; \mathbb{C})$), the three subgroup axioms, and the identification with the closed fibre.
>
> **Conjugate transposition reverses products.** Entrywise complex conjugation satisfies $\overline{AB} = \bar{A} \bar{B}$, because $(\overline{AB})_{jk} = \overline{\sum_l A_{jl} B_{lk}} = \sum_l \overline{A_{jl}} \, \overline{B_{lk}} = (\bar{A} \bar{B})_{jk}$, complex conjugation being a ring homomorphism of $\mathbb{C}$ (it respects finite sums and products). Combining with the transpose rule of Step 1, which holds over $\mathbb{C}$ verbatim (the computation there used only the definitions of product and transpose and commutativity of the scalar field),
> $$(AB)^* = (\overline{AB})^t = (\bar{A} \bar{B})^t = \bar{B}^t \bar{A}^t = B^* A^* \qquad \text{(definition of } *\text{; conjugation respects products; transposition reverses products; definition of } *\text{)}.$$
> Also $(A^*)^* = A$, since $\overline{\bar{A}} = A$ and $(A^t)^t = A$, and $1_n^* = 1_n$ since the entries of $1_n$ are real and $1_n$ is symmetric.
>
> **Containment in $GL(n; \mathbb{C})$.** Let $A^* A = 1_n$. Taking determinants,
> $$1 = \det 1_n = \det(A^* A) = \det(A^*) \det A = \overline{\det A} \cdot \det A = |\det A|^2 \qquad \text{(} \det 1_n = 1\text{; hypothesis; multiplicativity; } \det(A^*) = \det(\bar{A}^t) = \det \bar{A} = \overline{\det A} \text{ by the transpose and conjugation corollaries recalled above)}.$$
> Hence $\det A \neq 0$ and $A \in GL(n; \mathbb{C})$ by the invertibility corollary of [[Thm - Determinant is Multiplicative]]. So $U(n) \subseteq GL(n; \mathbb{C})$, and the definition of $U(n)$ inside $\operatorname{Mat}(n \times n; \mathbb{C})$ agrees with the one inside $GL(n; \mathbb{C})$.
>
> **Identity.** $1_n^* 1_n = 1_n 1_n = 1_n$, so $1_n \in U(n)$.
>
> **Products.** For $A, B \in U(n)$,
> $$(AB)^* (AB) = (B^* A^*)(AB) = B^* (A^* A) B = B^* \, 1_n \, B = B^* B = 1_n \qquad \text{(conjugate transposition reverses products; associativity; } A \in U(n)\text{; identity; } B \in U(n)\text{)},$$
> so $AB \in U(n)$.
>
> **Inverses.** For $A \in U(n)$ the inverse exists by the containment, and
> $$A^* = A^* (A A^{-1}) = (A^* A) A^{-1} = 1_n A^{-1} = A^{-1} \qquad \text{(} A A^{-1} = 1_n\text{; associativity; } A \in U(n)\text{; identity)},$$
> whence
> $$(A^{-1})^* A^{-1} = (A^*)^* A^* = A A^* = A A^{-1} = 1_n \qquad \text{(} A^{-1} = A^* \text{ twice; } (A^*)^* = A\text{; } A^* = A^{-1}\text{)},$$
> so $A^{-1} \in U(n)$.
>
> **Closedness.** By definition and the containment, $U(n) = \mu^{-1}(\{1_n\}) \cap GL(n; \mathbb{C})$, which is closed in $GL(n; \mathbb{C})$ by Step 0.
>
> Therefore $U(n)$ is a closed subgroup of $GL(n; \mathbb{C})$.

**Step 4: $SO(n)$ and $SU(n)$ are closed subgroups — Bär's items 3 and 6, by intersection.**

The intersection of two subgroups of a group is a subgroup, and the intersection of two closed subsets of a topological space is closed; hence $SO(n) = O(n) \cap SL(n; \mathbb{R})$ is a closed subgroup of $GL(n; \mathbb{R})$ and $SU(n) = U(n) \cap SL(n; \mathbb{C})$ is a closed subgroup of $GL(n; \mathbb{C})$.

> [!note]- Derivation
> **Intersections of subgroups.** Let $H_1, H_2$ be subgroups of a group $G$ and $H := H_1 \cap H_2$. *Identity:* $e \in H_1$ and $e \in H_2$ (each is a subgroup), so $e \in H$. *Products:* if $a, b \in H$ then $a, b \in H_1$, so $ab \in H_1$ (closure of $H_1$), and $a, b \in H_2$, so $ab \in H_2$ (closure of $H_2$); hence $ab \in H$. *Inverses:* if $a \in H$ then $a^{-1} \in H_1$ and $a^{-1} \in H_2$ (each closed under inverses), so $a^{-1} \in H$. Thus $H$ is a subgroup of $G$.
>
> **Intersections of closed sets.** Let $F_1, F_2$ be closed subsets of a topological space $X$. Then $X \setminus (F_1 \cap F_2) = (X \setminus F_1) \cup (X \setminus F_2)$ (de Morgan), a union of two open sets, hence open; so $F_1 \cap F_2$ is closed.
>
> **$SO(n)$.** By Step 1, $O(n)$ is a closed subgroup of $GL(n; \mathbb{R})$; by Step 2, $SL(n; \mathbb{R})$ is a closed subgroup of $GL(n; \mathbb{R})$. Applying the two facts just proved with $G = X = GL(n; \mathbb{R})$, $SO(n) = O(n) \cap SL(n; \mathbb{R})$ is a closed subgroup of $GL(n; \mathbb{R})$. Concretely, $SO(n) = \{A \in GL(n; \mathbb{R}) : A^t A = 1_n \text{ and } \det A = 1\}$ is the preimage of the closed set $\{(1_n, 1)\}$ under the continuous map $A \mapsto (\tau(A), \det A)$ — the second description Bär's phrasing suggests, and equivalent to the intersection.
>
> **$SU(n)$.** By Step 3, $U(n)$ is a closed subgroup of $GL(n; \mathbb{C})$; by Step 2, $SL(n; \mathbb{C})$ is a closed subgroup of $GL(n; \mathbb{C})$. Hence $SU(n) = U(n) \cap SL(n; \mathbb{C})$ is a closed subgroup of $GL(n; \mathbb{C})$.

**Step 5: Each of the six groups is a Lie group — the closed subgroup theorem.**

$GL(n; \mathbb{K})$ is a Lie group; each of $O(n)$, $SL(n; \mathbb{R})$, $SO(n)$ is a closed subgroup of $GL(n; \mathbb{R})$ and each of $U(n)$, $SL(n; \mathbb{C})$, $SU(n)$ is a closed subgroup of $GL(n; \mathbb{C})$; therefore, by the closed subgroup theorem, each is an embedded Lie subgroup of $GL(n; \mathbb{K})$ and a Lie group in its own right.

> [!note]- Derivation
> **The ambient Lie group.** $GL(n; \mathbb{K})$ is a Lie group: it is an open subset of $\operatorname{Mat}(n \times n; \mathbb{K}) = \mathbb{R}^{n^2}$ or $\mathbb{R}^{2n^2}$ (the preimage of the open set $\mathbb{K} \setminus \{0\}$ under the continuous map $\det$), hence a smooth manifold; the entries of $AB$ are polynomials in the entries of $A$ and $B$, so multiplication is smooth; and the entries of $A^{-1}$ are rational functions of the entries of $A$ with denominator $\det A \neq 0$ (the adjugate formula), so inversion is smooth. This is Bär's Example 1.1.2 and is proved in full in Block A of [[Def - Classical Matrix Groups]] (real case also on [[Ex - The General Linear Group is a Smooth Manifold]]).
>
> **The theorem.** By [[Thm - The Closed Subgroup Theorem]] — if $G$ is a Lie group and $H \subseteq G$ is a subgroup that is a closed subset of $G$ in the manifold topology, then $H$ is an embedded submanifold of $G$ and, with the induced smooth structure and the restricted group operations, a Lie group — we may take $G = GL(n; \mathbb{R})$ and $H \in \{O(n), SL(n; \mathbb{R}), SO(n)\}$, using Steps 1, 2, 4 for the hypotheses, and $G = GL(n; \mathbb{C})$ and $H \in \{U(n), SL(n; \mathbb{C}), SU(n)\}$, using Steps 3, 2, 4. In each of the six cases the hypothesis "subgroup" was verified as the three axioms and the hypothesis "closed" was verified as the closed fibre of a continuous map or an intersection of two such.
>
> **Conclusion.** Each of $O(n)$, $SL(n; \mathbb{R})$, $SO(n)$, $U(n)$, $SL(n; \mathbb{C})$, $SU(n)$ is an embedded Lie subgroup of the corresponding general linear group, hence a Lie group. Since each is moreover closed, each is a *properly* embedded submanifold ([[Def - Embedded Submanifold]]: an embedded submanifold is properly embedded if and only if it is closed in the ambient manifold).

> [!note]- Complete formal solution
> **Claim.** Each of $O(n)$, $SL(n; \mathbb{R})$, $SO(n)$ is a closed subgroup of $GL(n; \mathbb{R})$, each of $U(n)$, $SL(n; \mathbb{C})$, $SU(n)$ is a closed subgroup of $GL(n; \mathbb{C})$, and all six are Lie groups.
>
> **Step 0 (topology).** The maps $\tau(A) = A^t A$ on $\operatorname{Mat}(n \times n; \mathbb{R}) = \mathbb{R}^{n^2}$, $\det$ on $\operatorname{Mat}(n \times n; \mathbb{K})$, and $\mu(A) = A^* A$ on $\operatorname{Mat}(n \times n; \mathbb{C}) = \mathbb{R}^{2n^2}$ have components that are polynomials in the real coordinates of $A$: $(A^t A)_{jk} = \sum_l A_{lj} A_{lk}$; $\det A = \sum_\sigma \operatorname{sign}(\sigma) \prod_j A_{j\sigma(j)}$ (Leibniz), whose real and imaginary parts are polynomials in the real and imaginary parts of the entries; $(A^* A)_{jk} = \sum_l \overline{A_{lj}} A_{lk}$, with $\overline{A_{lj}} A_{lk} = (x_{lj} x_{lk} + y_{lj} y_{lk}) + i(x_{lj} y_{lk} - y_{lj} x_{lk})$. Polynomial maps between Euclidean spaces are continuous (finite sums and products of continuous coordinate functions; a map into $\mathbb{R}^M$ is continuous if and only if its components are). Singletons in a metric space are closed. So $\tau^{-1}(\{1_n\})$, $\det^{-1}(\{1\})$, $\mu^{-1}(\{1_n\})$ are closed in the respective matrix spaces (closed-set formulation of [[Def - Continuous Map|continuity]]), and their intersections with $GL(n; \mathbb{K})$ are closed in the subspace topology of $GL(n; \mathbb{K})$, which is its manifold topology.
>
> **Step 1 ($O(n)$).** Transposition reverses products, $((AB)^t)_{jk} = (AB)_{kj} = \sum_l A_{kl} B_{lj} = \sum_l (B^t)_{jl} (A^t)_{lk} = (B^t A^t)_{jk}$. *Identity:* $1_n^t 1_n = 1_n$. *Products:* for $A, B \in O(n)$, $(AB)^t(AB) = B^t (A^t A) B = B^t B = 1_n$ (reversal, associativity, $A^t A = 1_n$, $B^t B = 1_n$), and $\det(AB) = \det A \det B \neq 0$ ([[Thm - Determinant is Multiplicative]]). *Inverses:* for $A \in O(n) \subseteq GL(n; \mathbb{R})$, $A^t = A^t (A A^{-1}) = (A^t A) A^{-1} = A^{-1}$, so $(A^{-1})^t A^{-1} = A A^t = A A^{-1} = 1_n$. *Closed:* $O(n) = \tau^{-1}(\{1_n\}) \cap GL(n; \mathbb{R})$, closed by Step 0.
>
> **Step 2 ($SL(n; \mathbb{K})$, $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$; Bär's item 5 misprints $SL(n; \mathbb{C})$ as $SL(n; \mathbb{R})$).** *Containment:* $\det A = 1 \neq 0$ gives $A \in GL(n; \mathbb{K})$ (invertibility corollary of [[Thm - Determinant is Multiplicative]]). *Identity:* $\det 1_n = 1$ (Leibniz: only $\sigma = \mathrm{id}$ contributes). *Products:* $\det(AB) = \det A \det B = 1$. *Inverses:* $1 = \det(A A^{-1}) = \det A \det(A^{-1}) = \det(A^{-1})$. *Closed:* $SL(n; \mathbb{K}) = \det^{-1}(\{1\}) \cap GL(n; \mathbb{K})$, closed by Step 0.
>
> **Step 3 ($U(n)$).** Conjugation is a ring homomorphism of $\mathbb{C}$, so $\overline{AB} = \bar{A} \bar{B}$, and with the transpose rule $(AB)^* = (\bar{A} \bar{B})^t = \bar{B}^t \bar{A}^t = B^* A^*$; also $(A^*)^* = A$ and $1_n^* = 1_n$. *Containment:* from $A^* A = 1_n$, $1 = \det(A^*) \det A = \overline{\det A} \det A = |\det A|^2$ (multiplicativity; $\det(A^*) = \det \bar{A} = \overline{\det A}$ by the transpose corollary of [[Def - Determinant]] and by pulling the field automorphism $z \mapsto \bar{z}$ through the Leibniz formula), so $\det A \neq 0$ and $A \in GL(n; \mathbb{C})$. *Identity:* $1_n^* 1_n = 1_n$. *Products:* $(AB)^*(AB) = B^*(A^* A) B = B^* B = 1_n$. *Inverses:* $A^* = A^*(A A^{-1}) = (A^* A) A^{-1} = A^{-1}$, so $(A^{-1})^* A^{-1} = A A^* = A A^{-1} = 1_n$. *Closed:* $U(n) = \mu^{-1}(\{1_n\}) \cap GL(n; \mathbb{C})$, closed by Step 0.
>
> **Step 4 ($SO(n)$, $SU(n)$).** If $H_1, H_2$ are subgroups of $G$ then $H_1 \cap H_2$ contains $e$ (both do), is closed under products (each is) and under inverses (each is), hence is a subgroup; if $F_1, F_2$ are closed then $X \setminus (F_1 \cap F_2) = (X \setminus F_1) \cup (X \setminus F_2)$ is open, so $F_1 \cap F_2$ is closed. Applying this to $O(n) \cap SL(n; \mathbb{R})$ (Steps 1, 2) and to $U(n) \cap SL(n; \mathbb{C})$ (Steps 3, 2), $SO(n)$ is a closed subgroup of $GL(n; \mathbb{R})$ and $SU(n)$ is a closed subgroup of $GL(n; \mathbb{C})$.
>
> **Step 5 (Lie groups).** $GL(n; \mathbb{K})$ is a Lie group ([[Def - Classical Matrix Groups]], Block A: open subset of $\mathbb{R}^{n^2}$ or $\mathbb{R}^{2n^2}$; polynomial multiplication; rational inversion). By [[Thm - The Closed Subgroup Theorem]] — a subgroup of a Lie group that is closed as a subset is an embedded Lie subgroup, hence a Lie group with the restricted operations — applied with $G = GL(n; \mathbb{R})$ to $O(n)$, $SL(n; \mathbb{R})$, $SO(n)$ and with $G = GL(n; \mathbb{C})$ to $U(n)$, $SL(n; \mathbb{C})$, $SU(n)$, each of the six groups is an embedded Lie subgroup of its general linear group.
>
> Therefore the orthogonal, special linear (real and complex), special orthogonal, unitary, and special unitary groups are Lie groups, each realised as a properly embedded Lie subgroup of $GL(n; \mathbb{R})$ or $GL(n; \mathbb{C})$. $\blacksquare$

> [!warning] Illegal but tempting: "closed in $\operatorname{Mat}(n \times n; \mathbb{K})$" is not what the theorem asks for, and "subgroup" alone is not enough
> Two shortcuts present themselves. The first is to say "the group is the zero set of a continuous function, hence closed" and stop, without saying *closed in what*. The closed subgroup theorem needs closedness in the Lie group $G = GL(n; \mathbb{K})$, and a set closed in $\operatorname{Mat}(n \times n; \mathbb{K})$ is closed in $GL(n; \mathbb{K})$ only after intersecting with $GL(n; \mathbb{K})$ and only if the set actually lies in $GL(n; \mathbb{K})$ — which for $U(n)$ required the separate computation $|\det A|^2 = 1$. The distinction is not decorative: the set $\{A \in \operatorname{Mat}(2 \times 2; \mathbb{R}) : \det A = 0\}$ is closed in $\operatorname{Mat}(2 \times 2; \mathbb{R})$ and is disjoint from $GL(2; \mathbb{R})$, so it says nothing about any subgroup. The second shortcut is to believe that a subgroup of a Lie group is automatically a Lie subgroup. It is not: the subgroup $H_{\mathbb{Q}} = \{A \in GL(2; \mathbb{R}) : \det A \in \mathbb{Q}\}$ (a subgroup by multiplicativity of $\det$, since $\mathbb{Q}^\times$ is a group) contains $\operatorname{diag}(q_m, 1)$ for rationals $q_m \to \sqrt{2}$, whose limit $\operatorname{diag}(\sqrt{2}, 1)$ lies in $GL(2; \mathbb{R}) \setminus H_{\mathbb{Q}}$; so $H_{\mathbb{Q}}$ is not closed, is dense in $GL(2; \mathbb{R})$ (it contains $\operatorname{diag}(q, 1) \cdot B$ for every $B \in SL(2; \mathbb{R})$ and every $q \in \mathbb{Q}^\times$, and $\mathbb{Q}^\times$ is dense in $\mathbb{R}^\times$), and cannot be an embedded submanifold of positive codimension. The extra condition that makes the shortcut legal is exactly the closedness hypothesis of the theorem.

**Independent sanity check.** For $O(n)$ and $SL(n; \mathbb{R})$ the conclusion "embedded submanifold of $GL(n; \mathbb{R})$" can be reached by a second route that does not pass through the closed subgroup theorem: the regular value theorem. On [[Ex - The Orthogonal Group as a Regular Level Set]] it is shown that $1_n$ is a regular value of $\tau : GL(n; \mathbb{R}) \to \operatorname{Sym}(n)$, $A \mapsto A^t A$, into the symmetric matrices, so $O(n) = \tau^{-1}(1_n)$ is a properly embedded submanifold of dimension $n^2 - n(n+1)/2 = n(n-1)/2$; and on [[Ex - The Special Linear Group is a Submanifold of GL(n)]] that $1$ is a regular value of $\det$, so $SL(n; \mathbb{R})$ is a properly embedded hypersurface of dimension $n^2 - 1$. Both agree with the present conclusion and, unlike it, produce the dimensions, which the closed subgroup theorem leaves to be computed from the Lie algebra; the series does that computation on [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]]. In the smallest case $n = 1$ everything can be seen whole: $O(1) = \{\pm 1\}$ and $SO(1) = \{1\}$ are finite, hence $0$-dimensional Lie groups; $SL(1; \mathbb{K}) = \{1\}$; $U(1) = \{z \in \mathbb{C} : \bar{z} z = 1\}$ is the unit circle, closed in $\mathbb{C}^\times$ as the fibre of $z \mapsto |z|^2$ over $1$; and $SU(1) = U(1) \cap \{z = 1\} = \{1\}$.

---

# Key Takeaways

**A group cut out of $GL(n; \mathbb{K})$ by polynomial equations that transform covariantly under products is a Lie group, and the proof always has the same two halves.** The reusable principle is the division of labour that organised the solution: the *topological* half (closedness) is the observation that the defining map is polynomial in the real coordinates, hence continuous, and that the target is a point, hence closed; the *algebraic* half (subgroup) is the observation that the defining map transforms under products by a rule — $\tau(AB) = B^t \tau(A) B$, $\det(AB) = \det A \det B$, $\mu(AB) = B^* \mu(A) B$ — that fixes the fibre over the identity, together with the trick $A^{-1} = A^t$ (or $A^*$) for inverses. Once both halves are in place, the closed subgroup theorem does all the differential-geometric work: charts, smoothness of multiplication and inversion, and the Lie algebra. Every structure group in this series — $U(1)$ in electrodynamics, $SU(n)$ in Yang–Mills theory, $SO(n)$ for frame bundles, $Spin(n)$ in chapter VIII, $Sp(1) \cong SU(2)$ in Seiberg–Witten theory — enters through this door, and the reader who has internalised the two halves can admit a new structure group in a few lines.

**The trigger for this pattern is a subset of $GL(n; \mathbb{K})$ described by "the matrices that preserve some structure", and the diagnostic is to ask what the defining map does to a product.** The orthogonal group preserves the Euclidean inner product, the unitary group the Hermitian one, the special linear group the determinant; in each case "preserves" is an equation $f(A) = f(1_n)$, and preservation is manifestly transitive (if $A$ and $B$ each preserve, so does $AB$) and reversible (so does $A^{-1}$). When a set is presented in this form, the subgroup axioms are not something to be computed entry by entry but something to be read off from the transformation law of $f$; and the reader should be suspicious of any argument that computes entries of $A^{-1}$, because it is almost always the sign that the transformation law has not been identified. Conversely, a subset defined by an equation without a transformation law — for instance $\{A : \operatorname{tr} A = 0\}$ inside $GL(n; \mathbb{R})$, which is closed but not a subgroup since $\operatorname{tr}(AB) \neq \operatorname{tr} A + \operatorname{tr} B$ in general and $1_n$ is not even in it — is not a candidate, and the diagnostic identifies this immediately.

**The transferable caution is to track the ambient space in which "closed" is asserted, and to remember that closedness is the hypothesis that cannot be dropped.** Bär defines some of his groups inside $\operatorname{Mat}(n \times n; \mathbb{K})$ and some inside $GL(n; \mathbb{K})$, and the closed subgroup theorem is stated for the Lie group $GL(n; \mathbb{K})$; the solution spent a whole step (Step 0) reconciling the two, and two containment checks (Steps 2 and 3) verifying that the sets in question actually lie in $GL(n; \mathbb{K})$. This is not pedantry: the subspace topology is what makes "closed in $GL(n; \mathbb{K})$" a weaker condition than "closed in $\operatorname{Mat}(n \times n; \mathbb{K})$" — the group $GL(n; \mathbb{K})$ is itself closed in $GL(n; \mathbb{K})$ but open and not closed in $\operatorname{Mat}(n \times n; \mathbb{K})$ — and the theorem is false without closedness, as the dense subgroup $H_{\mathbb{Q}}$ in the warning callout shows, or as the irrational line $\{(e^{2\pi i t}, e^{2\pi i \alpha t}) : t \in \mathbb{R}\}$ in the torus $U(1) \times U(1)$ with $\alpha \notin \mathbb{Q}$ shows (a subgroup and an immersed Lie subgroup, but dense, and not embedded). The same habit — name the space, name the topology — is the one that later prevents errors when the series passes from a Lie group to its quotient by a closed subgroup in §1.5 and to the total space of a principal bundle in chapter III.

**Companion exercises.** The dimensions of the six groups, left open here, are computed on [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]] by differentiating the same three equations at $1_n$; the regular value route to the same conclusion for $O(n)$ and $SL(n; \mathbb{R})$ is on [[Ex - The Orthogonal Group as a Regular Level Set]] and [[Ex - The Special Linear Group is a Submanifold of GL(n)]]; the group $Sp(1)$ of unit quaternions, which [[Def - Classical Matrix Groups]] adds to Bär's list, is identified with $SU(2)$ on [[Ex - SU(2) is the Group of Unit Quaternions]]; and the smallest nontrivial case of the whole story, $SO(2) \cong U(1) \cong S^1$, is worked out on [[Thm - SO(2) is Isomorphic to U(1)]].

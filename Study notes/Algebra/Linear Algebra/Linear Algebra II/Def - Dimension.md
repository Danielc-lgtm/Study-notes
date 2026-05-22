---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Basis"
  - "Thm - Bases are Equinumerous"
  - "Def - Finite-Dimensional Vector Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional vector space over $F$. The dimension is denoted $\dim V$, or $\dim_F V$ when the field needs to be made explicit. The full notation registry is on [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

---

# Axiom Motivation

The point of the definition is to attach a single integer to a finite-dimensional vector space, an integer that captures "how much room there is". The candidate definition is **the length of a basis**, because a basis installs coordinates and so the length tells you how many independent directions you need to address every vector. But the candidate definition is well-defined only if all bases of $V$ have the same length — and that is non-obvious. Two different bases could in principle differ in length, in which case $\dim V$ would depend on a choice.

The substantive theorem that licenses this definition is [[Thm - Bases are Equinumerous|LADR 2.34]]: any two bases of a finite-dimensional vector space have the same length. With that theorem in hand, the *length of any basis* is an invariant of $V$ — basis-independent — and we may call it the dimension. Without that theorem, the word "dimension" would not even be meaningful.

The dimension is the cleanest example of a **basis-independent invariant** in linear algebra. The basis itself is a choice; the coordinate tuple of a vector depends on the basis; even the matrix of a linear map depends on the bases of domain and codomain. But the *length* of the basis is rigid: it is the same integer no matter which basis you pick. This is what makes $\dim V$ a property of the space itself, and it is why dimension is the right numerical handle on the space.

The per-axiom failure question reduces here to: what would we lose if we replaced "length of a basis" by "length of *some* basis" (admitting non-uniqueness)? We would lose well-definedness — dimension would depend on the basis chosen, and the question "is $\dim V = 3$" would have no answer. The conditional structure of the definition — defining the invariant only after the equinumerosity theorem is proved — is what makes the definition meaningful.

A second motivation. Without the well-definedness of dimension, we could *not* say things like "$\mathbb{R}^3$ has more room than $\mathbb{R}^2$" with mathematical force. We could observe that the standard basis of $\mathbb{R}^3$ has more vectors than the standard basis of $\mathbb{R}^2$, but the question "is this difference an essential feature of the spaces or just an artefact of the chosen bases?" would not be answered. The equinumerosity theorem is what converts the basis-dependent observation into an essential statement about the spaces: $\dim \mathbb{R}^3 > \dim \mathbb{R}^2$, full stop, basis-independent.

The empty basis convention: the zero space $\{0\}$ has the empty list as a basis (vacuously spans, vacuously independent), and so $\dim \{0\} = 0$. This is the right normalisation — there is zero room in $\{0\}$.

Finally, dimension depends on the field. The complex numbers $\mathbb{C}$, viewed as a *complex* vector space, have dimension $1$ (the singleton list $1$ is a basis). Viewed as a *real* vector space, they have dimension $2$ (basis $1, i$). The notation $\dim_\mathbb{R} \mathbb{C} = 2$ and $\dim_\mathbb{C} \mathbb{C} = 1$ records this. Restricting the field always *multiplies* the dimension: $\dim_\mathbb{R} \mathbb{C}^n = 2n$, since each complex coordinate decomposes into real and imaginary parts.

---

# The Definition

The **dimension** of a [[Def - Finite-Dimensional Vector Space|finite-dimensional]] vector space $V$ over $F$ is the length (number of elements) of any basis of $V$:
$$\dim V := n \quad \text{where } v_1, \ldots, v_n \text{ is any basis of } V.$$
This is well-defined by [[Thm - Bases are Equinumerous|LADR 2.34]]: any two bases of $V$ have the same length, so the choice of basis does not affect $n$.

The zero vector space $\{0\}$ has dimension $0$ (its only basis is the empty list).

When the underlying field needs emphasis, write $\dim_F V$.

---

# Relate to Other Fields / Compression

Dimension is the linear-algebra incarnation of **cardinality** — the count of independent directions in $V$ — and the dimension formula $\dim(V_1 + V_2) = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$ ([[Thm - Dimension of a Sum of Subspaces|LADR 2.43]]) is the linear-algebra analogue of inclusion-exclusion $|A \cup B| = |A| + |B| - |A \cap B|$. The analogy is essentially exact in finite dimensions; the substitution table is

| sets | vector spaces |
|---|---|
| finite set $S$ | finite-dimensional space $V$ |
| $|S|$ | $\dim V$ |
| union $S_1 \cup S_2$ | sum $V_1 + V_2$ |
| intersection $S_1 \cap S_2$ | intersection $V_1 \cap V_2$ |
| disjoint union | direct sum |

This is not a coincidence — it reflects the fact that both contexts are special cases of "modular lattice" structure, in which inclusion-exclusion is a general theorem.

**True name:** "the unique integer that all bases of $V$ share." The textbook definition gives a formula; the operational meaning is that $\dim V$ is the invariant of the space, basis-independent, and *that is the reason it is a useful integer to attach*. The single most reusable use of dimension is comparative: $\dim U \leq \dim V$ when $U \subseteq V$, with equality iff $U = V$. Almost every "are these two subspaces equal" problem is answered by computing dimensions.

A second compression: $\dim V$ is the **rank** of $V$ as a free $F$-module. In [[Def - Module|module theory]], the rank of a free module is the size of its free generating set, and the same equinumerosity theorem licenses the definition. Linear algebra is the special case where every module is free and rank is dimension.

---

# Examples / Corollaries

**Example.** $\dim F^n = n$, by the standard basis.

**Example.** $\dim \mathcal{P}_m(F) = m + 1$, by the standard basis $1, z, \ldots, z^m$. (Note the off-by-one: degree at most $m$ gives $m+1$ basis vectors $1, z, \ldots, z^m$.) See [[Ex - Polynomials of degree at most n form a basis]].

**Example.** $\dim \{(x, x, y) \in F^3 : x, y \in F\} = 2$, via the basis $(1, 1, 0), (0, 0, 1)$.

**Example.** $\dim \{(x, y, z) \in F^3 : x + y + z = 0\} = 2$, via the basis $(1, -1, 0), (1, 0, -1)$.

**Example (dimension depends on the field).** $\dim_\mathbb{C} \mathbb{C} = 1$ but $\dim_\mathbb{R} \mathbb{C} = 2$ (with basis $1, i$). More generally, $\dim_\mathbb{R} \mathbb{C}^n = 2n$ and $\dim_\mathbb{C} \mathbb{C}^n = n$. Each complex coordinate decomposes into a real and an imaginary part, doubling the count.

**Non-example.** $\mathcal{P}(F)$, the space of *all* polynomials, has no finite-dimensional dimension — it is infinite-dimensional. Any finite list of polynomials has a maximum degree $m$, so its span sits inside $\mathcal{P}_m(F)$ and misses $z^{m+1}$. Similarly, $F^\infty$ (sequence space) is infinite-dimensional.

**Corollary (dimension inequality for subspaces).** If $U$ is a subspace of finite-dimensional $V$, then $\dim U \leq \dim V$. *Proof:* By [[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|LADR 2.25]], $U$ is finite-dimensional, so has a basis $u_1, \ldots, u_m$. This basis is a linearly independent list in $V$ (independence is a property of the list, not of the ambient space). By [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|LADR 2.22]] applied to the independent list $u_1, \ldots, u_m$ and any spanning list of $V$ of length $\dim V$, we get $m \leq \dim V$.

**Corollary (equality forces $U = V$).** If $U \subseteq V$ with $\dim U = \dim V$ and $V$ finite-dimensional, then $U = V$. *Proof:* A basis $u_1, \ldots, u_n$ of $U$, with $n = \dim U = \dim V$, is a linearly independent list of length $\dim V$ in $V$. By [[Thm - Every Linearly Independent List Extends to a Basis|LADR 2.32]] it extends to a basis of $V$, but every basis of $V$ has length $n$, so no extension is possible: the list is *already* a basis of $V$. Hence its span is all of $V$, and the span is $U$, so $U = V$. This is [[Ex - Dimension of a subspace equals dimension only if equal]].

**Corollary (length-of-basis shortcuts).** In a space of dimension $n$, a list of length $n$ is a basis iff it is linearly independent iff it spans. *Proof:* If independent, [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] would extend it, but all bases have length $n$ so no extension is possible — it is already a basis. Dually for spanning. The corollary halves the verification work for a list of the right length: check *one* of the two conditions, not both. This is operation 3 from the topic page.

**Corollary (direct sum).** If $V = V_1 \oplus V_2$, then $\dim V = \dim V_1 + \dim V_2$. *Proof:* By [[Thm - Dimension of a Sum of Subspaces|2.43]], $\dim(V_1 + V_2) = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$, and $V_1 \cap V_2 = \{0\}$ in a direct sum, contributing $\dim 0 = 0$. Alternatively, concatenate bases of $V_1$ and $V_2$ to get a basis of $V$ (see [[Ex - Sum of dimensions in direct sum]]). Dimension is *additive* across direct sums, but not in general across sums (the correction term subtracts the intersection).

**Calibration check.** If you have understood dimension, you should be able to answer instantly: (a) what is $\dim \mathcal{P}_5(\mathbb{R})$? (Answer: $6$.) (b) what is $\dim$ of the subspace of $\mathbb{R}^4$ defined by $x_1 = x_2$ and $x_3 = x_4$? (Answer: $2$ — two free parameters, two basis vectors.) (c) is there a basis of $\mathbb{R}^3$ of length $4$? (Answer: no — too long to be independent, by [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]] against the spanning standard basis.)

---

# Unlocked by This

> [!tip] Rank of a Linear Map *(from §3B)*
> The **rank** of a linear map $T : V \to W$ is $\dim \operatorname{range}(T)$. The dual notion is the **nullity**, $\dim \ker(T)$. The fundamental theorem of linear maps (rank-nullity, LADR 3.21) states that $\dim V = \operatorname{nullity}(T) + \operatorname{rank}(T)$ for a linear map on a finite-dimensional domain — a dimensional accounting that is one of the most-used facts in linear algebra. The proof uses [[Thm - Every Linearly Independent List Extends to a Basis|basis extension]] crucially: extend a basis of $\ker T$ to a basis of $V$, and the additional basis vectors map to a basis of $\operatorname{range} T$.

> [!tip] Krull Dimension *(from Commutative Algebra)*
> The vector-space dimension of an affine variety at a smooth point is the **Zariski tangent space dimension**, which generalises to non-linear geometry as **Krull dimension** — the supremum of the lengths of chains of prime ideals in the coordinate ring. For affine algebraic varieties Krull dimension agrees with the geometric dimension (the dimension of a generic tangent space), and the linear case is the special case where the coordinate ring is a polynomial ring in $n$ variables modulo a linear ideal. Krull dimension is also the right notion of dimension in scheme theory and is a core invariant of commutative rings.

> [!tip] Tangent Space Dimension *(from Differential Geometry)*
> An $n$-dimensional manifold $M$ has, at every point $p$, a tangent space $T_p M$ — a real vector space of dimension exactly $n$, with basis given by the partial derivatives $\partial/\partial x^1, \ldots, \partial/\partial x^n$ in any coordinate chart around $p$. The dimension of $T_p M$ equals the dimension of $M$ — this is the *defining* property of manifold dimension, and the tangent space being a vector space at every point is what makes the entire calculus-on-manifolds machinery work. The [[Def - The Total Derivative and Differentiability|total derivative]] at a point is a linear map $T_p M \to T_{f(p)} N$ between tangent spaces, and the rank-nullity theorem there is a constraint on the local behaviour of $f$.

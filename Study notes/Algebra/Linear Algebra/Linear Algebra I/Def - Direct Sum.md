---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
  - "Def - Sum of Subspaces"
tags: [algebra, linear-algebra]
---

# Notation

A direct sum is written with the special symbol $\oplus$: $V_1 \oplus V_2 \oplus \dots \oplus V_m$ for the direct sum of subspaces $V_1, \dots, V_m$. The symbol is a plus sign inside a circle, deliberately emphasizing that this is a *special* kind of sum — one in which decomposition is unique. The plain sum $V_1 + \dots + V_m$ uses the ordinary plus sign; promoting it to a direct sum $V_1 \oplus \dots \oplus V_m$ is a structural claim, not merely a notational change. When we write $V = V_1 \oplus V_2$, we are simultaneously claiming that $V = V_1 + V_2$ (every $v$ decomposes) and that the decomposition is unique. See [[Linear Algebra I — §1 Vector Spaces]] for the full notation registry.

---

# Axiom Motivation

The thing we are trying to axiomatize is **the cleanest possible decomposition of a vector space into pieces**: one in which every element has *exactly one* representation as a sum of pieces. A generic sum $V_1 + \dots + V_m$ of [[Def - Subspace|subspaces]] guarantees that every element of the sum can be written as $v_1 + \dots + v_m$ with $v_k \in V_k$, but not that this representation is unique. The same element may admit many such decompositions, and the question "what piece of $v$ lives in $V_k$" then has no answer. This ambiguity destroys the most useful applications of decomposition.

The direct sum is the demand that this ambiguity be eliminated. Why is uniqueness the right thing to demand, beyond aesthetic cleanliness? Because uniqueness lets you **define projections**: if every $v \in V = V_1 \oplus \dots \oplus V_m$ has a unique decomposition $v = v_1 + \dots + v_m$, then the map $\pi_k : V \to V_k$ sending $v$ to its $k$th piece is a well-defined linear function. With a generic sum no such map exists; with a direct sum the projections are well-defined and form a fundamental set of tools. Almost every diagonalization and decomposition result in linear algebra — the spectral theorem, the generalized-eigenspace decomposition, Jordan form, the SVD — packages a direct-sum decomposition together with the projections it produces.

Why does uniqueness boil down to "the only way to write zero is the trivial way"? Suppose every nonzero $v$ in the sum has a unique decomposition. Then in particular $0$ has only one decomposition; since $0 = 0 + \dots + 0$ is always a valid decomposition, this must be the only one. Conversely, suppose the only way to write $0 = v_1 + \dots + v_m$ with $v_k \in V_k$ is to take every $v_k = 0$. Then if some $v$ has two decompositions $v = v_1 + \dots + v_m = u_1 + \dots + u_m$, subtracting gives $0 = (v_1 - u_1) + \dots + (v_m - u_m)$ with $v_k - u_k \in V_k$, hence every $v_k - u_k = 0$, hence the decompositions agree. So uniqueness for every element follows from uniqueness at zero — this is the content of [[Thm - Conditions for a Direct Sum]]. The lesson is structural: in any vector space (more generally any abelian [[Def - Group|group]]), zero is the "test element" through which uniqueness propagates.

A pleasing simplification appears in the two-subspace case: $U + W$ is a direct sum if and only if $U \cap W = \{0\}$ — see [[Thm - Direct Sum of Two Subspaces]]. The condition is geometric: the two [[Def - Subspace|subspaces]] share only the origin. This is the linear analogue of "disjoint" for sets, with the caveat that two non-trivial subspaces always share at least the zero vector — so "disjoint up to zero" is the strongest disjointness one can demand. The two-subspace case suggests the wrong generalization for three or more subspaces: pairwise trivial intersection is *not* enough — LADR's Example 1.44 displays three subspaces in $\mathbb{F}^3$ that pairwise intersect only at $0$, yet their sum is not direct. The correct generalization is given by [[Thm - Conditions for a Direct Sum]].

Why is the direct sum often written $V = V_1 \oplus V_2$ when $V_1, V_2$ are subspaces of $V$ adding up to $V$? This is the "internal direct sum" — $V$ decomposes internally as the direct sum of its subspaces $V_1, V_2$. There is also an "external direct sum" $V_1 \oplus V_2$ where $V_1, V_2$ are arbitrary vector spaces (not subspaces of a common ambient space) and the direct sum is constructed as ordered pairs $(v_1, v_2)$ — this is the product of vector spaces, treated in [[Linear Algebra IV — §3E–F Products, Quotients, Duality]]. The two constructions are linked by the canonical map $V_1 \oplus_{\text{ext}} V_2 \to V_1 +_{\text{int}} V_2$, which is an isomorphism precisely when the internal sum is direct. The unification of the two notations under $\oplus$ is intentional: they really are the same construction, up to identification.

---

# The Definition

Let $V_1, \dots, V_m$ be subspaces of a vector space $V$.

The sum $V_1 + \dots + V_m$ is called a **direct sum** if every element of $V_1 + \dots + V_m$ has a **unique** representation as

$$v = v_1 + \dots + v_m$$

with $v_k \in V_k$. Equivalently (by [[Thm - Conditions for a Direct Sum]]):

> The sum $V_1 + \dots + V_m$ is a direct sum if and only if the only choice of $v_1 \in V_1, \dots, v_m \in V_m$ with
> $$v_1 + \dots + v_m = 0$$
> is $v_1 = \dots = v_m = 0$.

When the sum is direct, it is written

$$V_1 \oplus V_2 \oplus \dots \oplus V_m$$

with the special symbol $\oplus$ replacing the ordinary $+$. The notation $V = V_1 \oplus \dots \oplus V_m$ asserts simultaneously that $V$ equals the sum of the $V_k$ and that this sum is direct — that is, that every $v \in V$ has a unique decomposition into pieces, one in each $V_k$.

For the case of two subspaces, $U + W$ is a direct sum if and only if $U \cap W = \{0\}$ — see [[Thm - Direct Sum of Two Subspaces]].

---

# Categorical / Structural Definition

The internal direct sum $V = V_1 \oplus \dots \oplus V_m$ is precisely the assertion that the natural addition map

$$\sigma : V_1 \times V_2 \times \dots \times V_m \longrightarrow V, \qquad (v_1, \dots, v_m) \mapsto v_1 + \dots + v_m$$

is a [[Linear Algebra III — §3A–D Linear Maps|linear isomorphism]] from the product (external direct sum) onto $V$. Surjectivity is the statement that $V = V_1 + \dots + V_m$; injectivity is the statement that the kernel of $\sigma$ is $\{0\}$, which by [[Thm - Conditions for a Direct Sum]] is exactly the uniqueness condition.

This is the structural unification: a direct-sum decomposition of $V$ is the same data as an isomorphism $V \cong V_1 \oplus_{\text{ext}} \dots \oplus_{\text{ext}} V_m$ — and conversely, given any external direct sum, one obtains an internal direct sum decomposition of the result by taking the images of the inclusions. The two notions of direct sum (internal: $V_k \subseteq V$; external: $V_k$ independent) are isomorphic via $\sigma$.

A categorical perspective: in $\mathbf{Vect}_{\mathbb{F}}$, the direct sum is simultaneously the **product** $\prod V_k$ and the **coproduct** $\coprod V_k$ — these two universal objects, distinct in most categories, coincide in any **additive category**. This is one of the structural pleasantries of vector spaces and abelian [[Def - Group|groups]]: finite limits and finite colimits agree for terminal-like objects. The internal direct sum $V_1 \oplus V_2 \subseteq V$ is the assertion that $V$ realizes this biproduct of $V_1$ and $V_2$ — that the projections $\pi_k : V \to V_k$ and inclusions $\iota_k : V_k \hookrightarrow V$ together satisfy $\pi_j \circ \iota_k = \delta_{jk}$ (the identity on $V_k$ if $j = k$, the zero map otherwise) and $\iota_1 \pi_1 + \dots + \iota_m \pi_m = \operatorname{id}_V$.

In category-theoretic language, a direct-sum decomposition is a **split** structure: every direct summand $V_k$ is the image of an idempotent linear endomorphism $\iota_k \pi_k : V \to V$ with $\iota_k \pi_k \circ \iota_k \pi_k = \iota_k \pi_k$. Direct summands correspond bijectively to idempotents in $\operatorname{End}(V)$. This is the reason the spectral theorem can be packaged either as "diagonalizable" or as "writes the identity as a sum of orthogonal projections" — the two are restatements of one structural fact.

---

# Relate to Other Fields / Compression

The direct sum is the linear-algebraic analogue of a **product decomposition of an [[Def - Abelian Group|abelian group]]**. For abelian groups (or modules) one says $G = H \oplus K$ if every $g \in G$ has a unique decomposition $g = h + k$ with $h \in H, k \in K$, which is equivalent to $G = H + K$ together with $H \cap K = 0$. The group-theoretic statement "$G$ is the direct product of its subgroups $H, K$" generalizes to non-abelian groups but requires the additional condition that $H$ and $K$ each be normal — see [[Def - Normal Subgroup]] — and the direct *product* and direct *sum* terminologies start to diverge. Vector spaces (and abelian groups, and modules) sidestep this issue because every subspace is "normal" trivially: there is no non-commutativity to obstruct the decomposition.

In [[Def - Module|module theory]] the direct sum decomposition is more delicate: an arbitrary submodule need not be a direct summand. A submodule $N \subseteq M$ is a **direct summand** if there exists a submodule $N' \subseteq M$ with $M = N \oplus N'$; not every submodule has a complement. This contrasts sharply with the vector-space case, where every subspace has a complement (every subspace is a direct summand) — a consequence of the existence of bases (see [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]). The general module-theoretic property "every submodule is a direct summand" defines a **semisimple** module, and vector spaces are semisimple. This is one of the structural reasons linear algebra is cleaner than module theory.

A direct sum decomposition is also the linear analogue of a **partition** in set theory. A set is partitioned when written as a disjoint union of subsets; a vector space is decomposed when written as a direct sum of subspaces. The disjointness condition in set theory becomes $V_i \cap V_j = \{0\}$ in the two-subspace case but strengthens for multiple subspaces — see [[Thm - Conditions for a Direct Sum]]. The intuition is the same: a partition / decomposition lets every element be assigned uniquely to a piece, which is precisely what allows the construction of well-defined projections.

**True name:** the operational true name of "direct sum decomposition" is "well-defined projections onto each piece". When you reach for a direct sum in a proof, what you usually need is to take an arbitrary $v$, extract its component $v_k \in V_k$, and treat the components independently. The component $v_k = \pi_k(v)$ is well-defined because the decomposition is unique; lose uniqueness and the projections become ill-defined. So "direct sum" should be read as "decomposition with well-defined projections", and the synthetic condition "uniqueness of decomposition at $0$" is just the cleanest way to certify the projections work.

---

# Examples / Corollaries

**Is an instance: $\mathbb{F}^n = V_1 \oplus \dots \oplus V_n$, with $V_k$ the $k$th coordinate axis.** Let $V_k = \{(0, \dots, 0, x, 0, \dots, 0) : x \in \mathbb{F}\}$ with the $x$ in the $k$th slot. Then every $(x_1, \dots, x_n) \in \mathbb{F}^n$ decomposes uniquely as $(x_1, 0, \dots, 0) + (0, x_2, 0, \dots, 0) + \dots + (0, \dots, 0, x_n)$, with the $k$th term in $V_k$ and forced to be that exact vector by the coordinate constraint. So $\mathbb{F}^n = V_1 \oplus \dots \oplus V_n$, and this is the prototype of a direct-sum decomposition.

**Is an instance: $\mathbb{F}^3 = U \oplus W$ with $U$ the $xy$-plane and $W$ the $z$-axis.** Let $U = \{(x, y, 0)\}$ and $W = \{(0, 0, z)\}$. Then every $(x, y, z) \in \mathbb{F}^3$ decomposes uniquely as $(x, y, 0) + (0, 0, z)$. The intersection $U \cap W = \{(0, 0, 0)\}$, so the sum is direct by [[Thm - Direct Sum of Two Subspaces]]. Geometrically: every point in space is the unique sum of its shadow on the floor (in $U$) and a vertical displacement (in $W$).

**Is an instance: $\mathbb{R}^\mathbb{R} = V_e \oplus V_o$, even and odd functions.** The set of even functions $V_e = \{f : f(-x) = f(x)\}$ and the set of odd functions $V_o = \{f : f(-x) = -f(x)\}$ are subspaces of $\mathbb{R}^\mathbb{R}$, and every function decomposes uniquely as the sum of an even and an odd function: $f(x) = \frac{f(x) + f(-x)}{2} + \frac{f(x) - f(-x)}{2}$. This is one of the most useful direct-sum decompositions in analysis and is the worked example [[Ex - Even and odd functions form a direct sum decomposition]].

**Is an instance: in $\mathbb{F}^2$, $\mathbb{F}^2 = \operatorname{span}((1, 0)) \oplus \operatorname{span}((0, 1))$.** Two transverse lines through the origin form a direct sum decomposition of the plane. In general, any two distinct lines through the origin in $\mathbb{F}^2$ form a direct sum decomposition — see [[Ex - Subspaces of F^2 are classified]]. This is the source of "any two distinct lines through the origin span the plane" in elementary geometry.

**Is NOT an instance (LADR Example 1.44): $\mathbb{F}^3 = V_1 + V_2 + V_3$, but not direct.** Take $V_1 = \{(x, y, 0)\}$ (the $xy$-plane), $V_2 = \{(0, 0, z)\}$ (the $z$-axis), $V_3 = \{(0, y, y)\}$ (a line). The sum $V_1 + V_2 + V_3 = \mathbb{F}^3$. The pairwise intersections are all $\{0\}$. Yet the sum is *not* direct: $0 = (0, 1, 0) + (0, 0, 1) + (0, -1, -1)$ is a non-trivial decomposition of zero, with the first term in $V_1$, the second in $V_2$, the third in $V_3$. So pairwise disjoint intersections are not enough to conclude directness for three or more subspaces — see [[Thm - Conditions for a Direct Sum]] for the right condition.

**Is NOT an instance: $\mathbb{F}^2$ as the sum of the $x$-axis and itself.** $V_1 = \{(x, 0)\}$, $V_2 = \{(x, 0)\}$. Then $V_1 + V_2 = V_1 \neq \mathbb{F}^2$, and even within $V_1 + V_2 = V_1$, the element $(1, 0) = (1, 0) + (0, 0) = (0, 0) + (1, 0)$ has two decompositions. The intersection $V_1 \cap V_2 = V_1 \neq \{0\}$, so by [[Thm - Direct Sum of Two Subspaces]] the sum is not direct. This is the trivial obstruction: a subspace cannot be a direct summand with itself unless it is $\{0\}$.

**Corollary (decompositions add [[Def - Dimension|dimensions]]).** If $V = V_1 \oplus \dots \oplus V_m$ with each $V_k$ finite-dimensional, then $\dim V = \dim V_1 + \dots + \dim V_m$. The proof, which uses the basis-from-each-summand construction (see [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]), shows that a basis of $V$ is obtained by concatenating bases of the $V_k$. This is the source of "decomposing into eigenspaces makes the dimension obvious" — once you know the [[Def - Dimension|dimensions]] of all eigenspaces, the dimension of the operator's domain is forced.

**Corollary (direct sum decompositions are [[Def - Isomorphism|isomorphisms]] with the product).** If $V = V_1 \oplus V_2$, then $V \cong V_1 \times V_2$ as vector spaces, via $v_1 + v_2 \leftrightarrow (v_1, v_2)$. This is the cleanest packaging of the directness: the internal sum and the external product carry the same data, and the isomorphism is the addition map.

**Corollary (the projections are well-defined linear maps).** If $V = V_1 \oplus \dots \oplus V_m$, then the map $\pi_k : V \to V_k$ sending $v = v_1 + \dots + v_m$ to $v_k$ is a well-defined linear map (because of uniqueness), satisfies $\pi_k|_{V_k} = \operatorname{id}_{V_k}$ and $\pi_k|_{V_j} = 0$ for $j \neq k$, and $\sum_k (\iota_k \circ \pi_k) = \operatorname{id}_V$. These projections are the **idempotents** of the decomposition, and they decompose the identity operator on $V$.

**Calibration check.** If you have understood the definition you should be able to (i) verify directly that $\mathbb{F}^3 = \{(x, 0, 0)\} \oplus \{(0, y, z)\}$ by computing the unique decomposition of a generic $(x, y, z)$; (ii) decide whether $\mathbb{F}^3 = \{(x, y, 0)\} \oplus \{(x, 0, z)\}$ is direct (no: the intersection is the $x$-axis $\{(x, 0, 0)\}$, which is non-trivial); (iii) write down a non-trivial way of expressing the zero vector in $\mathbb{F}^2$ using the subspaces $V_1 = \operatorname{span}((1, 0))$, $V_2 = \operatorname{span}((0, 1))$, $V_3 = \operatorname{span}((1, 1))$, and conclude their sum is not a direct sum (for instance $0 = (1, 0) + (0, 1) + (-1, -1)$).

---

# Unlocked by This

> [!tip] Projection Operator and Idempotent *(from Linear Algebra III)*
> A direct sum decomposition $V = V_1 \oplus V_2$ defines a **projection** operator $P : V \to V$ with $P^2 = P$, $\operatorname{im}(P) = V_1$, $\ker(P) = V_2$. Conversely every idempotent linear operator splits $V$ into the direct sum of its image and kernel. The bijection between direct-sum decompositions and idempotents is one of the most useful structural facts in linear algebra and underpins the spectral theorem.

> [!tip] Eigenspace Decomposition and Diagonalizability *(from Linear Algebra V)*
> An operator $T : V \to V$ is **diagonalizable** if and only if $V$ decomposes as a direct sum of the eigenspaces $V = \bigoplus_\lambda \ker(T - \lambda I)$. This is the cleanest characterization of diagonalizability and is the structural content of the spectral theorem on inner product spaces. See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]] and [[Linear Algebra VII — §7 Operators on Inner Product Spaces]].

> [!tip] Generalized Eigenspace Decomposition and Jordan Form *(from Linear Algebra VIII)*
> When an operator on a complex vector space is not diagonalizable, the space still decomposes as a direct sum of **generalized eigenspaces** $V = \bigoplus_\lambda \ker((T - \lambda I)^{\dim V})$. The restriction of $T$ to each generalized eigenspace is upper-triangular and decomposes further into Jordan blocks. The whole machinery rests on the direct sum being available, which on a complex vector space is always.

> [!tip] Orthogonal Decomposition *(from Linear Algebra VI–VII)*
> In an inner-product space, every subspace $U$ gives rise to the orthogonal direct sum $V = U \oplus U^\perp$. This is the cleanest decomposition available — uniqueness is reinforced by orthogonality, and the projection $\pi_U$ is the unique closest-point map. The spectral theorem for self-adjoint operators decomposes $V$ as a direct sum of *mutually orthogonal* eigenspaces, refining the eigenspace decomposition by orthogonality.

> [!tip] Internal Direct Sum and Short Exact Sequence *(from Homological Algebra)*
> The internal direct sum $V = U \oplus W$ is equivalent to the splitting of the short exact sequence $0 \to U \to V \to V/U \to 0$. In $\mathbf{Vect}_{\mathbb{F}}$ every short exact sequence splits, which is why every subspace has a complement. This fails in [[Def - Module|module theory]] (a torsion abelian group, say, does not split off from $\mathbb{Z}$), giving the precise homological reason linear algebra is cleaner: $\operatorname{Ext}^1(W, U) = 0$ for vector spaces but not for general modules.

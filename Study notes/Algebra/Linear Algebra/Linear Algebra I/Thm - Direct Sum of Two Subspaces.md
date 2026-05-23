---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
  - "Def - Sum of Subspaces"
  - "Def - Direct Sum"
  - "Thm - Conditions for a Direct Sum"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over a field $\mathbb{F}$; $U$ and $W$ are subspaces of $V$. The sum $U + W = \{u + w : u \in U, w \in W\}$ is a subspace, and is a [[Def - Direct Sum|direct sum]] $U \oplus W$ exactly when every element has a unique decomposition $u + w$. The intersection $U \cap W$ is a subspace, and the zero subspace is $\{0\}$. See [[Linear Algebra I — §1 Vector Spaces]] for the full notation registry.

---

# Statement

> **Theorem ([[Def - Direct Sum|Direct Sum]] of Two [[Def - Subspace|Subspaces]]).** Let $U$ and $W$ be [[Def - Subspace|subspaces]] of a vector space $V$. Then
> $$U + W \text{ is a direct sum} \quad \Longleftrightarrow \quad U \cap W = \{0\}.$$

This is the simplest and most-used criterion for direct sums, applying only in the two-subspace case. For three or more subspaces, pairwise trivial intersection is **not** enough — see [[Thm - Conditions for a Direct Sum]] and [[Def - Direct Sum]] for the right generalization.

---

# Motivation

A direct sum is, in principle, certified by a condition involving the decomposition of *every* element of the sum. [[Thm - Conditions for a Direct Sum]] reduces this to a condition on the zero vector alone. For two subspaces, this theorem reduces the condition further to a condition on the *intersection*: just check that no nonzero vector belongs to both subspaces. This is a beautiful simplification — a structural, geometric statement (trivial overlap of subspaces) takes the place of an algebraic statement (decomposition of zero).

The geometric reading is the clearest motivation. Two lines through the origin in $\mathbb{R}^2$ that are not the same line intersect only at $0$, and they together span $\mathbb{R}^2$ uniquely (every point lies on exactly one parallelogram built from the two lines as edges). Two coincident lines intersect along themselves, and the parallelogram degenerates — every point on the line has infinitely many decompositions. The theorem packages this geometric intuition into an algebraic criterion: trivial intersection certifies trivial decomposition of zero, which certifies uniqueness throughout.

A second reason the theorem matters: it is the *operational* form one actually uses. Verifying $U \cap W = \{0\}$ usually means showing that any nonzero $v \in U \cap W$ leads to a contradiction, which is concrete and often easier than checking the abstract decomposition condition. Almost every proof that a sum is direct in practice goes through this theorem (when there are two subspaces) or its generalization (when there are more).

The theorem also encodes a useful caution: it is **not** the right test for more than two subspaces. The three subspaces $V_1 = \operatorname{span}(e_1)$, $V_2 = \operatorname{span}(e_2)$, $V_3 = \operatorname{span}(e_1 + e_2)$ in $\mathbb{F}^2$ pairwise intersect only at $\{0\}$, yet their sum is not direct: $0 = e_1 + e_2 - (e_1 + e_2)$ is a non-trivial decomposition. So the analogy "trivial intersection $\Rightarrow$ direct sum" fails for $m \geq 3$, and one must use the zero-uniqueness criterion of [[Thm - Conditions for a Direct Sum]] instead.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is: two subspaces $U, W$ of $V$ with $U \cap W = \{0\}$. The skill is recognizing this condition in disguised form.

A first source is **complementary projections**. If $P : V \to V$ is a [[Linear Algebra III — §3A–D Linear Maps|linear operator]] with $P^2 = P$ (an idempotent), then setting $U = \operatorname{im} P$ and $W = \ker P$ gives $U \cap W = \{0\}$, because any $v \in U \cap W$ has $v = Pv = 0$. The bridge "$P$ is an idempotent" implies "$U = \operatorname{im} P$ and $W = \ker P$ have trivial intersection", which routes through this theorem to "$V = U \oplus W$". The non-obvious step is recognizing the idempotent structure as a source of complementary subspaces; once recognized, the direct sum decomposition is automatic. This is the source behind the spectral decomposition of [[Linear Algebra VII — §7 Operators on Inner Product Spaces|self-adjoint operators]].

A second source is **orthogonality in an inner product space**. If $U \perp W$ — every $u \in U$ is orthogonal to every $w \in W$, so $\langle u, w \rangle = 0$ — then $U \cap W = \{0\}$: a vector $v \in U \cap W$ satisfies $\langle v, v \rangle = 0$, forcing $v = 0$. The bridge "$U$ and $W$ are orthogonal" implies trivial intersection, which by this theorem gives directness. So orthogonal sums in [[Linear Algebra VI — §6 Inner Product Spaces|inner-product spaces]] are direct sums *for free*. The non-obvious step: orthogonality is a stronger condition than the directness criterion, but provides automatic certification at no computational cost.

A third source is **eigenspaces with distinct eigenvalues**. If $T : V \to V$ is a linear operator and $\lambda_1 \neq \lambda_2$ are distinct eigenvalues, then the eigenspaces $V_{\lambda_1} = \ker(T - \lambda_1 I)$ and $V_{\lambda_2} = \ker(T - \lambda_2 I)$ satisfy $V_{\lambda_1} \cap V_{\lambda_2} = \{0\}$. Reason: a nonzero $v \in V_{\lambda_1} \cap V_{\lambda_2}$ would satisfy $\lambda_1 v = Tv = \lambda_2 v$, forcing $\lambda_1 = \lambda_2$. The bridge from "distinct eigenvalues" to "trivial intersection of eigenspaces" routes through this theorem to "the eigenspaces form a direct sum". This is the structural content of [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|eigenvectors with distinct eigenvalues are linearly independent]].

A fourth source is **a homomorphism whose kernel meets a given subspace only at zero**. If $\varphi : V \to W$ is a linear map and $U \subseteq V$ with $U \cap \ker \varphi = \{0\}$, then $U \oplus \ker \varphi$ is a direct sum and $\varphi|_U$ is injective. The non-obvious bridge: the condition "$\varphi$ restricted to $U$ is injective" is exactly the condition that $U$ meets $\ker \varphi$ only at zero. This is the source behind the splitting argument in the first isomorphism theorem and the rank-nullity theorem (see [[Linear Algebra III — §3A–D Linear Maps]]).

**Targets (Output Amplification)**

The conclusion is that $U + W$ is a direct sum, hence every element has a unique decomposition $u + w$, and (when finite-dimensional) $\dim(U + W) = \dim U + \dim W$.

A first combination is **directness plus dimensions add to $\dim V$ forces $V = U \oplus W$**. Conclusion $C$: $U + W$ is direct. Property $D$: $\dim U + \dim W = \dim V$. Result $E$: $U + W = V$, hence $V = U \oplus W$. The argument is dimension counting: $\dim(U + W) = \dim U + \dim W - \dim(U \cap W) = \dim U + \dim W$ by directness, and this equals $\dim V$, so $U + W = V$. This combination is the standard recipe for verifying a direct-sum decomposition of $V$: check $U \cap W = \{0\}$ and check the dimensions. The non-obvious bit: each ingredient is easy, but together they pin down a complete decomposition of $V$.

A second combination is **directness plus a $T$-invariant $U$ plus a complementary $W$ gives block-diagonal $T$**. Conclusion $C$: $V = U \oplus W$. Property $D$: $T(U) \subseteq U$ and $T(W) \subseteq W$. Result $E$: in any basis built from a basis of $U$ followed by a basis of $W$, the matrix of $T$ is block-diagonal. So $T$ decomposes into independent restrictions $T|_U$ and $T|_W$, and questions about $T$'s eigenvalues, rank, trace, determinant decompose. The non-obvious step: invariance plus directness, not invariance alone, gives the block structure.

A third combination is **directness plus a bilinear form gives the orthogonal-complement decomposition**. Conclusion $C$: $V = U \oplus U^\perp$. Property $D$: the inner product is non-degenerate on $U$. Result $E$: every vector decomposes uniquely into a "parallel" part in $U$ and a "perpendicular" part in $U^\perp$, giving the orthogonal projection onto $U$. This is the structural framework of best approximation, least squares, Fourier series, and is the workhorse of [[Linear Algebra VI — §6 Inner Product Spaces|inner-product geometry]].

---

# Why Is It True

The intuition is two facts knitted together: **vectors in $U \cap W$ are vectors with two different "homes"**, and **a non-trivial decomposition of zero is exactly a nonzero vector with two homes**.

Suppose first that $U + W$ is a direct sum and let $v \in U \cap W$. Consider the decomposition $0 = v + (-v)$: here $v \in U$ (the first summand) and $-v \in W$ (the second summand, since $W$ is closed under inverses). By directness applied to $0$, this must be the trivial decomposition: $v = 0$. So the only element of $U \cap W$ is $0$.

Conversely, suppose $U \cap W = \{0\}$. To verify directness, take any decomposition $0 = u + w$ with $u \in U, w \in W$. Then $u = -w$, so $u \in U$ (given) and $u = -w \in W$ (since $w \in W$ and $W$ is a subspace). So $u \in U \cap W = \{0\}$, hence $u = 0$, and then $w = -u = 0$. So the only decomposition of zero is trivial; by [[Thm - Conditions for a Direct Sum]] the sum is direct.

**The single one-liner: a nonzero vector in $U \cap W$ is the same data as a non-trivial decomposition of zero — both are a single vector with two different homes.**

The asymmetry between two and three subspaces becomes clear from this picture. In the two-subspace case, a non-trivial decomposition $0 = u + w$ produces a single shared vector. In the three-subspace case, a non-trivial decomposition $0 = v_1 + v_2 + v_3$ involves three vectors related by a single equation, and *no single pair* must coincide — the conspiracy is between three pieces, none pairwise. That is why pairwise disjointness fails to imply directness for $m \geq 3$: pairwise tests cannot catch a three-way conspiracy.

---

# What Makes This Hard

The proof is short and the result is intuitive, but the trap is generalizing it: many students see "trivial intersection $\Rightarrow$ direct sum" and assume the same holds for three or more subspaces. It does not, and the standard counterexample is LADR's Example 1.44: $V_1 = \operatorname{span}(e_1, e_2)$, $V_2 = \operatorname{span}(e_3)$, $V_3 = \operatorname{span}(e_2 + e_3)$ in $\mathbb{F}^3$ have pairwise trivial intersection yet do not form a direct sum, since $0 = e_2 + e_3 + (-e_2 - e_3)$ is a non-trivial decomposition. The genuine difficulty is therefore conceptual rather than technical: knowing exactly when this theorem applies and when one must fall back on the zero-uniqueness criterion of [[Thm - Conditions for a Direct Sum]].

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
The criterion is a biconditional. For the forward direction, use that $v \in U \cap W$ gives a non-trivial decomposition $0 = v + (-v)$ of zero, contradicting directness. For the reverse direction, suppose $0 = u + w$; then $u = -w \in U \cap W = \{0\}$, so $u = 0$ and hence $w = 0$. The two directions exchange a "vector with two homes" for a "non-trivial decomposition of zero", and vice versa.

**Subgoal decomposition:**

1. **Forward direction ($\Rightarrow$):** If $U + W$ is a direct sum, then $U \cap W = \{0\}$.
   - *Hint:* Take $v \in U \cap W$. Then $0 = v + (-v)$ with $v \in U$ and $-v \in W$. Directness of $U + W$ applied to $0$ forces $v = 0$ (and $-v = 0$).
   - *Why needed:* This is one half of the biconditional.

2. **Reverse direction ($\Leftarrow$):** If $U \cap W = \{0\}$, then $U + W$ is a direct sum.
   - *Hint:* By [[Thm - Conditions for a Direct Sum]] it suffices to show that $0 = u + w$ with $u \in U, w \in W$ forces $u = w = 0$. From $0 = u + w$ we have $u = -w$; the right-hand side lies in $W$ since $W$ is closed under inverses, so $u \in U \cap W = \{0\}$, hence $u = 0$, hence $w = 0$.
   - *Why needed:* This is the other half of the biconditional.

---

# Lemma Decomposition

> [!note]- Lemma 1: A vector in $U \cap W$ produces a non-trivial decomposition of zero
> **Statement:** If $v \in U \cap W$, then $0 = v + (-v)$ is a decomposition of zero with $v \in U$ and $-v \in W$.
>
> **Hint:** $v \in U$ by assumption; $-v \in W$ since $v \in W$ and $W$ is closed under additive inverses (as a subspace).
>
> **Why needed:** This is the bridge from "shared element" to "ambiguous decomposition". Together with directness, it forces $v = 0$ and gives the forward direction.
>
> > [!note]- Full proof
> > Let $v \in U \cap W$. Then $v \in U$, and $v \in W$. Since $W$ is a subspace it is closed under additive inverses, so $-v \in W$. Adding: $v + (-v) = 0$, so $0 = v + (-v)$ is a valid decomposition of $0$ as a sum of an element of $U$ ($v$) and an element of $W$ ($-v$). This decomposition is trivial (i.e. both summands zero) if and only if $v = 0$.

> [!note]- Lemma 2: A non-trivial decomposition of zero produces a vector in $U \cap W$
> **Statement:** If $0 = u + w$ with $u \in U, w \in W$, then $u \in U \cap W$ (and so does $w$).
>
> **Hint:** From $0 = u + w$, $u = -w$. The element $u$ is in $U$ by assumption; it is also in $W$ because $-w \in W$ (subspace closure under inverses).
>
> **Why needed:** This is the reverse bridge — from "ambiguous decomposition" to "shared element" — and is the key step of the reverse direction of the biconditional.
>
> > [!note]- Full proof
> > Suppose $u + w = 0$ with $u \in U$ and $w \in W$. Then $u = -w$. Since $w \in W$ and $W$ is a subspace, $-w \in W$. So $u = -w \in W$. Combined with $u \in U$, this gives $u \in U \cap W$. By symmetry $w = -u \in U \cap W$ as well, although we do not need this for the proof.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $U, W$ be subspaces of a vector space $V$. Then $U + W$ is a direct sum if and only if $U \cap W = \{0\}$.
>
> *Proof.* ($\Rightarrow$) Suppose $U + W$ is a direct sum. Let $v \in U \cap W$. Since $V$ is a vector space, $-v \in V$; since $W$ is a subspace, $-v \in W$. Now $0 = v + (-v)$ with $v \in U$ and $-v \in W$ is a decomposition of $0$. Trivially, $0 = 0 + 0$ is also such a decomposition. By directness applied to $0$, these two decompositions agree, so $v = 0$. Hence $U \cap W = \{0\}$.
>
> ($\Leftarrow$) Suppose $U \cap W = \{0\}$. By [[Thm - Conditions for a Direct Sum]] it suffices to show that if $0 = u + w$ with $u \in U, w \in W$, then $u = w = 0$. From $u + w = 0$ we get $u = -w$. Since $w \in W$ and $W$ is a subspace, $-w \in W$. So $u = -w \in W$. Combined with $u \in U$, this gives $u \in U \cap W = \{0\}$, hence $u = 0$, and then $w = -u = 0$. So the only decomposition of $0$ is trivial, and $U + W$ is a direct sum. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**[[Def - Subgroup|Subgroups]] of an abelian [[Def - Group|group]].** The theorem holds verbatim for two [[Def - Subgroup|subgroups]] $H, K$ of an abelian group $G$ (or two [[Def - Submodule|submodules]] of a [[Def - Module|module]]): $H + K$ is a direct sum if and only if $H \cap K = \{0\}$. This is the criterion used in classifying finite abelian [[Def - Group|groups]]: a cyclic subgroup of order $p$ and a cyclic subgroup of order $q$ with $\gcd(p, q) = 1$ have trivial intersection (by [[Thm - Lagrange's Theorem]], the intersection's order divides both $p$ and $q$, hence is $1$), so their sum is direct. The application bridges from coprime orders to direct-sum decomposition.

**Orthogonal decomposition in a Hilbert space.** For a closed subspace $U$ of a Hilbert space $H$, the orthogonal complement $U^\perp$ satisfies $U \cap U^\perp = \{0\}$ — any $v$ in both has $\langle v, v \rangle = 0$, forcing $v = 0$. Hence by this theorem $U + U^\perp$ is a direct sum, and the projection theorem of functional analysis upgrades this to $H = U \oplus U^\perp$ (the sum exhausts $H$). The theorem is the algebraic skeleton of the projection theorem.

**Idempotent operators and complementary subspaces.** For an idempotent $P : V \to V$, the kernel and image satisfy $\operatorname{im} P \cap \ker P = \{0\}$ — any $v$ in both has $v = Pv = 0$. So this theorem gives $\operatorname{im} P + \ker P$ as a direct sum, and a [[Def - Dimension|dimension]] count shows it exhausts $V$ in finite [[Def - Dimension|dimensions]]: $V = \operatorname{im} P \oplus \ker P$. The bridge from idempotency to direct-sum decomposition is the basis of the structural classification of projections.

**Decomposing solution spaces of differential equations.** The space of solutions of a linear ODE $L y = 0$ decomposes as the direct sum of solution spaces of its irreducible factors, provided the factors share no common solutions. The pairwise triviality of intersection is the criterion of this theorem, and the application gives the standard "general solution = sum of particular solutions to component equations" of ODE theory.

---

# Bridges

- **[[Thm - Conditions for a Direct Sum]]** — the present theorem is the special case $m = 2$ of the general directness criterion. For $m = 2$, "the only decomposition of zero is trivial" simplifies to "$U \cap W = \{0\}$" because a non-trivial decomposition $0 = u + w$ with $u \neq 0$ produces $u \in U \cap W$ via $u = -w \in W$. For $m \geq 3$ this two-way correspondence breaks: a non-trivial decomposition need not produce a shared element of any one *pair* of summands. So the pairwise-intersection criterion is the right test only for the two-subspace case.

- **Linear independence and the directness of one-dimensional subspaces** — for two vectors $v_1, v_2 \neq 0$, the subspaces $\operatorname{span}(v_1)$ and $\operatorname{span}(v_2)$ have trivial intersection if and only if $v_1, v_2$ are linearly independent (no scalar multiple relation), and by this theorem this is the case if and only if $\operatorname{span}(v_1) + \operatorname{span}(v_2)$ is a direct sum. The directness of subspaces is therefore the linear-independence of generating vectors, lifted from vectors to subspaces. See [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]] for the multi-vector version.

- **Dimension formula for sums of subspaces** — for finite-dimensional $U, W$, the formula $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$ specializes to $\dim(U + W) = \dim U + \dim W$ when $U \cap W = \{0\}$. The dimension formula is therefore the "with corrections" generalization; this theorem identifies the case where the correction vanishes. See [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]] for the proof.

- **Splitting in the category of vector spaces** — the inclusion $U \hookrightarrow V$ admits a complementary subspace $W$ (a *splitting*) if and only if there exists $W \subseteq V$ with $V = U + W$ and $U \cap W = \{0\}$, which by this theorem is the direct-sum decomposition $V = U \oplus W$. Every short exact sequence of vector spaces splits, which is the categorical statement that every subspace has a complement, which is in turn this theorem applied to *some* complementary subspace. The fact that vector spaces are semisimple is, structurally, this theorem in action.

---

# Unlocked by This

> [!tip] Orthogonal Decomposition and Projection *(from Linear Algebra VI–VII)*
> In an inner-product space, the orthogonal complement $U^\perp$ of a subspace $U$ satisfies $U \cap U^\perp = \{0\}$, so by this theorem $U + U^\perp$ is direct, and a dimension count gives $V = U \oplus U^\perp$ in finite dimensions. The orthogonal projection $\pi_U : V \to U$ is the well-defined map sending $v$ to its $U$-component in this decomposition, and the best-approximation theorem identifies $\pi_U(v)$ as the unique closest point in $U$ to $v$. See [[Linear Algebra VI — §6 Inner Product Spaces]].

> [!tip] Eigenspaces with Distinct Eigenvalues are Linearly Independent *(from Linear Algebra V)*
> Two eigenspaces $V_\lambda, V_\mu$ for distinct eigenvalues $\lambda \neq \mu$ of an operator $T$ have trivial intersection — any $v \in V_\lambda \cap V_\mu$ satisfies $\lambda v = T v = \mu v$, forcing $v = 0$. By this theorem $V_\lambda + V_\mu$ is direct. Iterating gives the general fact that eigenvectors with distinct eigenvalues are linearly independent, which is the structural cornerstone of diagonalization. See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

> [!tip] Direct Summand and Projective Module *(from Module Theory)*
> A submodule $N \subseteq M$ is a **direct summand** if there exists $N' \subseteq M$ with $M = N + N'$ and $N \cap N' = \{0\}$. This theorem's analogue holds for modules. The condition "every submodule is a direct summand" defines a **semisimple** module; modules that are direct summands of free modules are called **projective**. Vector spaces are both semisimple and projective for free, which is why the theory is clean; for general modules these properties become substantive.

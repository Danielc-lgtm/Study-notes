---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Basis"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V, W$ are vector spaces over a field $\mathbf{F}$, $v_1, \ldots, v_n$ is an ordered basis of $V$, and $w_1, \ldots, w_n \in W$ are *any* $n$ vectors (no linear-independence assumption). The full notation registry is on [[Linear Algebra III — §3A–D Linear Maps]].

---

# Statement

> **Theorem (Linear-Map Lemma).** Let $V, W$ be vector spaces over $\mathbf{F}$, let $v_1, \ldots, v_n$ be a basis of $V$, and let $w_1, \ldots, w_n$ be *any* vectors in $W$. Then there exists a **unique** linear map $T : V \to W$ with
>
> $$T v_k \;=\; w_k \quad \text{for each } k = 1, \ldots, n.$$
>
> Explicitly, the map is defined on the basis-expansion of $v$ by
>
> $$T(c_1 v_1 + \cdots + c_n v_n) \;=\; c_1 w_1 + \cdots + c_n w_n.$$

---

# Motivation

This is the construction tool of linear algebra. The theorem answers the question "what data specifies a linear map?", and the answer is the cleanest possible one: pick a basis of the domain, pick *anything* you like in the codomain for the basis to map to, and extend by linearity. There are no constraints on the target vectors. The map is then determined uniquely.

Two contrasts make the theorem's content sharp. **Versus functions in general**: an arbitrary function $V \to W$ is wildly more complicated to specify; you must give a value at every point in $V$, an uncountable amount of data when $V$ is infinite or even just $\mathbb{R}^n$. A linear map collapses this to a finite (when $V$ is finite-dimensional) amount of data — $n$ vectors in $W$. **Versus the requirement of linear independence in the codomain**: there is none. The vectors $w_1, \ldots, w_n$ can be all equal, all zero, a basis of $W$, a proper subset of a basis, or anything else. Whatever you pick, a unique linear map exists. The freedom is total.

The theorem is the *definitional* basis for the matrix representation of linear maps. Given the target vectors $w_1, \ldots, w_n$ and a basis of $W$, each $w_k$ has a coordinate column; arranging these columns side by side gives the matrix $\mathcal{M}(T)$ in [[Def - Matrix of a Linear Map]]. So "specifying a linear map" and "writing down a matrix" are the same operation, with the linear-map lemma certifying that the matrix is consistent (i.e., that a unique map exists with that matrix).

The theorem is also the reason **a linear map is finite data**. Once a basis of $V$ is fixed, a linear map is determined by $n$ vectors in $W$, and so the space $\mathcal{L}(V, W)$ has the same "size" as the $n$-fold product $W^n$ — which, when $W$ is finite-dimensional, has dimension $n \dim W$. This is the dimension formula $\dim \mathcal{L}(V, W) = mn$ in [[Ex - The space of linear maps has dimension mn]].

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal hypothesis is "you have a basis of $V$ and chosen vectors in $W$". The disguised forms in problems are richer.

**Source: "produce a linear map with property P".** The most common application: you need to construct a linear map satisfying some condition (specified kernel, specified range, specified values on a subspace, etc.). The reaction is: choose a basis of $V$, decide what $T$ should do to each basis vector to ensure property P, and invoke the lemma. The non-obvious step is *figuring out what property P requires on basis vectors*. Example: build $T$ with prescribed null space $X$. Choose a basis of $X$, extend to a basis of $V$ by adding $v_1, \ldots, v_m$; define $T$ by sending the $X$-basis to $0$ and the extension to chosen non-zero targets. The lemma certifies $T$ exists.

**Source: "extend a partial linear map".** A linear map is defined on a subspace $U \subseteq V$ but you need to extend it to all of $V$. Pick a basis of $U$, extend to a basis of $V$, and define the extension to send the new basis vectors anywhere you like (typically to $0$). This is the content of LADR Exercise 13 of §3A. The lemma converts "extending a function" from a daunting set-theoretic problem to a one-line construction.

**Source: "the relations of $V$ as a quotient".** A vector space $V$ can be defined by generators and relations (a presentation). To map $V$ into $W$, it suffices to specify the images of the generators *and check the relations are respected*. The lemma applies once a basis (set of independent generators) is chosen. This is also how one constructs maps out of quotient spaces — see [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

**Targets (Output Amplification)**

The bare conclusion is "a unique map exists with prescribed basis values". Combined with other facts it does much more.

**Combined with the matrix representation.** The lemma certifies that the function $\mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ sending $T$ to its matrix is well-defined and surjective: every matrix corresponds to a unique linear map. The lemma is the construction step, and combined with the fact that the matrix is a linear function of $T$, it gives the isomorphism $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$.

**Combined with knowledge of a basis of $V$.** A linear map is determined by *any* basis of $V$; one can choose the basis to make the action of $T$ as simple as possible. This is the motivation for [[Thm - Change of Basis Formula|change of basis]] and for the entire program of finding bases adapted to an operator's structure (eigenbases, [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces|Jordan bases]]).

**Combined with rank–nullity.** The linear-map lemma is used to *construct* linear maps with prescribed null space and range (Exercise 31 of LADR §3B). The construction is: pick a basis of the prescribed null space $X$, extend to a basis of $V$ via $v_1, \ldots, v_m$, pick a basis $y_1, \ldots, y_m$ of the prescribed range $Y$, and define $T$ to send the basis of $X$ to zero and $v_k \mapsto y_k$. Rank–nullity then verifies $\dim V = \dim X + \dim Y$ is the necessary condition.

---

# Why Is It True

The theorem is built on the unique-representation property of a basis. By definition of a basis, every $v \in V$ has a unique expression $v = c_1 v_1 + \cdots + c_n v_n$. This uniqueness is the foundation of everything.

For *existence*, the formula $T(c_1 v_1 + \cdots + c_n v_n) := c_1 w_1 + \cdots + c_n w_n$ is well-defined precisely because the basis expansion is unique — the coefficients $c_k$ are determined by $v$. Each side of the equation is a function of $v$, and the equation tells us what that function should be. Linearity is automatic: applying $T$ to a sum $v + v'$ and computing in the basis gives $T(v) + T(v')$, because the basis expansion is additive in $v$ and so is the formula. Similarly for scalar multiplication.

For *uniqueness*, suppose $T$ and $T'$ are two linear maps with $Tv_k = T'v_k = w_k$ for every $k$. By linearity, for any $v = \sum c_k v_k \in V$,
$$Tv = T\!\sum c_k v_k = \sum c_k Tv_k = \sum c_k w_k = \sum c_k T'v_k = T'\!\sum c_k v_k = T'v.$$
So $Tv = T'v$ for every $v$, hence $T = T'$.

> **In one sentence: a basis gives unique coefficients, and a linear map must respect linear combinations, so the values on a basis force the values everywhere — and any choice of values on a basis is consistent because the basis has no relations.**

The freedom (any $w_1, \ldots, w_n$ at all) reflects that the basis has *no* relations: there is no condition like "$v_1 + v_2 = 0$" that would force "$T v_1 = -T v_2$". A basis is, by definition, free of such relations. Were $V$ instead a vector space presented by generators and relations, the freedom would be constrained: $w_1, \ldots, w_n$ would need to respect the relations of $V$. Bases are the case where the relations are exactly "the trivial ones", and the freedom is maximal.

---

# What Makes This Hard

The lemma itself is conceptually easy — the proof is essentially one line of basis expansion. The trap is in misusing it. The most common error is to apply it when $v_1, \ldots, v_n$ is not actually a basis: if the list is linearly dependent, there are non-trivial relations $\sum a_k v_k = 0$, and choosing arbitrary $w_k$ will *not* give a well-defined linear map — the proposed value at $0 \in V$ would have to be $\sum a_k w_k$, which must equal $T(0) = 0$, forcing a relation on the $w_k$. If the list is independent but does not span, the formula does not define $T$ on all of $V$.

A subtler error is to forget that the result is *both* existence and uniqueness. Existence gives you a map; uniqueness lets you prove two maps are equal by checking equality on a basis. Both are used constantly in the chapter.

A third subtle point: the freedom of choice in the $w_k$ is exactly $n \cdot \dim W$ degrees of freedom (when $W$ is finite-dimensional), and this is the dimension of $\mathcal{L}(V, W)$. So the lemma immediately implies the dimension formula — but only after one identifies the "freedom" with a vector-space structure on the data $(w_1, \ldots, w_n) \in W^n$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Define $T$ on each $v \in V$ by linear extension from its basis expansion. Check that this is well-defined (basis expansion is unique), that it satisfies $Tv_k = w_k$, that it is linear (use the linear structure of the basis expansion), and that it is unique (any linear map agreeing with $T$ on the basis must agree on $V$ by linearity).

**Subgoal decomposition:**

1. **Define $T$.** For $v \in V$ with unique basis expansion $v = c_1 v_1 + \cdots + c_n v_n$, set $Tv := c_1 w_1 + \cdots + c_n w_n$.
   - *Hint:* The basis expansion is unique, so this is a function.
   - *Why needed:* Existence.

2. **Check $T(v_k) = w_k$.** In the basis expansion of $v_k$, the coefficient of $v_k$ is $1$ and the rest are $0$, so $Tv_k = 1 \cdot w_k = w_k$.

3. **Check linearity.** Use the additivity and homogeneity of basis expansion: $(v + v')$ has basis coefficients $c_k + c'_k$, and $\lambda v$ has coefficients $\lambda c_k$. The formula for $T$ then preserves both.

4. **Check uniqueness.** Any linear map $T'$ with $T'v_k = w_k$ for each $k$ must, by linearity, satisfy $T'(\sum c_k v_k) = \sum c_k w_k$. So $T' = T$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Basis expansion is unique
> **Statement:** If $v_1, \ldots, v_n$ is a basis of $V$, then every $v \in V$ has a *unique* expression $v = c_1 v_1 + \cdots + c_n v_n$ with $c_k \in \mathbf{F}$.
>
> **Hint:** Existence: by the spanning property of a basis. Uniqueness: by linear independence.
>
> **Why needed:** Without unique basis expansion, the proposed formula for $T$ would not be a function — the same $v$ would give different values depending on which expansion was used.
>
> > [!note]- Full proof
> > Existence: $v_1, \ldots, v_n$ spans $V$, so $v = c_1 v_1 + \cdots + c_n v_n$ for some scalars. Uniqueness: if $v = c_1 v_1 + \cdots + c_n v_n = c'_1 v_1 + \cdots + c'_n v_n$, then subtracting gives $0 = (c_1 - c'_1) v_1 + \cdots + (c_n - c'_n) v_n$. Linear independence forces $c_k - c'_k = 0$ for each $k$, so $c_k = c'_k$.

> [!note]- Lemma 2: Basis expansion is additive and homogeneous
> **Statement:** If $v$ has expansion $\sum c_k v_k$ and $v'$ has expansion $\sum c'_k v_k$, then $v + v'$ has expansion $\sum (c_k + c'_k) v_k$ and $\lambda v$ has expansion $\sum (\lambda c_k) v_k$.
>
> **Hint:** This is just $\sum c_k v_k + \sum c'_k v_k = \sum (c_k + c'_k) v_k$ — distributivity of the vector-space operations.
>
> **Why needed:** This is what lets the proposed formula for $T$ inherit linearity from the basis expansion.
>
> > [!note]- Full proof
> > For addition: $v + v' = \sum c_k v_k + \sum c'_k v_k = \sum (c_k + c'_k) v_k$ by associativity and distributivity in the vector space. By uniqueness (Lemma 1), this is *the* basis expansion of $v + v'$. For scalar multiplication: $\lambda v = \lambda \sum c_k v_k = \sum (\lambda c_k) v_k$ similarly.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $v_1, \ldots, v_n$ be a basis of $V$ and $w_1, \ldots, w_n \in W$ any vectors.
>
> **Existence.** Define $T : V \to W$ as follows. For $v \in V$, by Lemma 1 there are unique scalars $c_1, \ldots, c_n \in \mathbf{F}$ with $v = c_1 v_1 + \cdots + c_n v_n$. Set
> $$T(v) := c_1 w_1 + \cdots + c_n w_n.$$
> This is a function $V \to W$ because the coefficients $c_k$ are unique.
>
> The map $T$ takes $v_k$ to $w_k$: in the basis expansion of $v_k$, all coefficients are zero except the $k$-th, which is $1$. So $T(v_k) = 1 \cdot w_k = w_k$.
>
> The map $T$ is linear. For additivity, let $u = \sum a_k v_k$, $v = \sum c_k v_k$. By Lemma 2, $u + v = \sum (a_k + c_k) v_k$. By the definition of $T$,
> $$T(u + v) = \sum (a_k + c_k) w_k = \sum a_k w_k + \sum c_k w_k = Tu + Tv.$$
> For homogeneity, let $\lambda \in \mathbf{F}$ and $v = \sum c_k v_k$. By Lemma 2, $\lambda v = \sum (\lambda c_k) v_k$, so
> $$T(\lambda v) = \sum (\lambda c_k) w_k = \lambda \sum c_k w_k = \lambda Tv.$$
>
> **Uniqueness.** Suppose $T' : V \to W$ is any linear map with $T'(v_k) = w_k$ for each $k$. For any $v = \sum c_k v_k \in V$, linearity of $T'$ gives
> $$T'(v) = T'\!\left(\sum c_k v_k\right) = \sum c_k T'(v_k) = \sum c_k w_k = T(v).$$
> So $T' = T$ as functions on $V$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Defining maps from $\mathcal{P}_n$ to anywhere.** The space $\mathcal{P}_n(\mathbb{R})$ has the standard basis $1, x, x^2, \ldots, x^n$ of length $n + 1$. To define a linear map $\mathcal{P}_n(\mathbb{R}) \to W$, just specify where each $x^k$ goes — any $n + 1$ vectors in $W$ work. For instance, sending $x^k$ to $k(k-1)\cdots(k-j+1) x^{k-j}$ for $k \geq j$ and to $0$ otherwise defines the $j$-th derivative operator. The lemma certifies it is a well-defined linear map without verifying linearity from scratch.

**Universal property of the free vector space on a set.** Given a set $S$, the **free vector space** $\mathbf{F}^{(S)}$ is the space of formal linear combinations of elements of $S$ with finitely many nonzero coefficients. It has $S$ as a "basis" (in the sense of the lemma: $S$ is a linearly independent spanning set). The universal property: a function $S \to W$ extends uniquely to a linear map $\mathbf{F}^{(S)} \to W$. This is the linear-map lemma at the level of full generality, and it is the categorical definition of the free-vector-space functor.

**Constructing operators with prescribed eigenvalues.** Pick distinct scalars $\lambda_1, \ldots, \lambda_n \in \mathbf{F}$ and a basis $v_1, \ldots, v_n$ of $V$. The lemma gives a unique operator $T$ with $T v_k = \lambda_k v_k$ for each $k$. This $T$ has the $\lambda_k$ as eigenvalues with $v_k$ as eigenvectors, and so is **diagonalisable**. Every diagonalisable operator arises this way. See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]] for the role of diagonalisability.

**Defining group representations on basis vectors.** A representation of $G$ on $V$ is a homomorphism $\rho : G \to \operatorname{GL}(V)$. For each generator $g$ of $G$, the operator $\rho(g)$ must be specified — and the linear-map lemma lets you specify $\rho(g)$ by choosing $\rho(g) v_k$ for each basis vector $v_k$. The catch: the chosen operators must satisfy the relations of $G$, which is a non-trivial check; the lemma handles the "exists as a linear map" part, but the "is a group homomorphism" part is the real content.

---

# Bridges

- **[[Def - Matrix of a Linear Map]]** — the matrix is exactly the data of the linear-map lemma. Once a basis is chosen for $V$ and a basis for $W$, the matrix $\mathcal{M}(T)$ has the coordinate columns of $Tv_1, \ldots, Tv_n$ as its columns. The lemma certifies that *any* choice of coordinate columns gives a unique linear map, so the matrix-and-the-linear-map are in perfect bijection. The dimension formula $\dim \mathcal{L}(V, W) = mn$ follows immediately.

- **[[Thm - Fundamental Theorem of Linear Maps]]** — the linear-map lemma supplies the construction step in the converse of rank–nullity: given dimensions $\dim X + \dim Y = \dim V$ for subspaces $X \subseteq V$ and $Y \subseteq W$, build $T \in \mathcal{L}(V, W)$ with $\operatorname{null} T = X$ and $\operatorname{range} T = Y$ by specifying the values on a basis (sending an $X$-basis to $0$ and an extension to a basis of $Y$).

- **Universal property of a basis (categorical perspective).** A basis of $V$ is exactly a set $S = \{v_1, \ldots, v_n\}$ such that, for every vector space $W$, every function $S \to W$ extends uniquely to a linear map $V \to W$. So the linear-map lemma *characterises* what it means to be a basis (and is the basis of "free objects" in category theory). One could *define* a basis this way and recover the usual definition by characterising free objects in $\mathbf{Vect}_\mathbf{F}$.

- **[[Def - Module Homomorphism]]** — the linear-map lemma generalises to modules over a ring, *when the module has a basis* (i.e., when it is a free module). For non-free modules, the analogue is the *presentation* of a module: a free module mapping onto it with kernel encoding the relations, and a map out of the module is specified by a map out of the free part respecting the relations. So the linear-map lemma is a special case of "map out of a free object = function on generators".

---

# Unlocked by This

> [!tip] Matrix Representation and the Identity $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$ *(in §3C–D)*
> The lemma, combined with the choice of bases for $V$ and $W$, gives an explicit isomorphism between $\mathcal{L}(V, W)$ and $\mathbf{F}^{m, n}$. This is the source of the dimension formula $\dim \mathcal{L}(V, W) = mn$ and the entire theory of matrix representations. See [[Def - Matrix of a Linear Map]] and [[Thm - Two Vector Spaces Isomorphic iff Same Dimension]].

> [!tip] Universal Property and Free Objects *(from Category Theory)*
> The lemma says: a basis is a set whose elements can be sent anywhere to define a linear map. This is the **universal property** of a basis, and it identifies bases as the "generators" of free vector spaces. The same universal-property pattern recurs throughout algebra: free groups, free rings, free modules, free abelian groups all have analogous "map out of free object = function on generators" theorems. The categorical formalism is the **free-forgetful adjunction**.

> [!tip] Diagonalisable Operators *(from Linear Algebra V)*
> An operator $T$ on $V$ is **diagonalisable** iff $V$ has a basis of eigenvectors. The linear-map lemma constructs every diagonalisable operator: pick eigenvalues $\lambda_1, \ldots, \lambda_n$ and a basis $v_1, \ldots, v_n$, define $T v_k = \lambda_k v_k$. Operators that are *not* diagonalisable cannot be constructed this way; the structure of non-diagonalisable operators is captured by **Jordan canonical form** (see [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]]).

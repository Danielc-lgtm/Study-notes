---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Dual Space"
  - "Def - Dual Basis"
  - "Def - Dimension"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional vector space over $\mathbb{F}$. The [[Def - Dual Space|dual space]] is $V' = \mathcal{L}(V, \mathbb{F})$. The [[Def - Dual Basis|dual basis]] of a basis $v_1, \dots, v_n$ of $V$ is $\varphi_1, \dots, \varphi_n$ characterised by $\varphi_j(v_k) = \delta_{jk}$. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

---

# Statement

> **Theorem (Dimension of the Dual).** Let $V$ be a finite-dimensional vector space over $\mathbb{F}$. Then $V'$ is also finite-dimensional, and
> $$\dim V' = \dim V.$$
> Explicitly, if $v_1, \dots, v_n$ is a basis of $V$, then the dual basis $\varphi_1, \dots, \varphi_n$ is a basis of $V'$.

---

# Motivation

The dual space $V'$ is *another* vector space derived from $V$, and the first question to ask of a new vector space is its dimension. The answer is the simplest possible: the dual has *the same dimension* as the original.

This is somewhat surprising. The construction $V \mapsto V'$ has nothing obvious to do with "preserving dimension" — it produces a quite different vector space whose elements are linear functions rather than vectors. The theorem says: despite this, the dimensions match. This is what makes $V$ and $V'$ *isomorphic as vector spaces* in finite dimensions, and it is what allows the duality machinery (dual map, transpose, annihilator) to function neatly without dimension mismatches.

A point of conceptual subtlety: although $V \cong V'$ as vector spaces, the isomorphism *requires choosing a basis* (since the dual basis is defined in terms of a basis). There is no canonical isomorphism $V \to V'$. In contrast, the canonical map $V \to V''$ given by evaluation *is* canonical (basis-free); see [[Ex - Double dual is naturally isomorphic to the original]]. The theorem here is the unannotated dimensional fact — the equality of dimensions — which is necessary background to discuss naturality at all.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is finite-dimensionality of $V$. The disguised sources are:

The first disguised source is **the formula $\dim \mathcal{L}(V, W) = (\dim V)(\dim W)$**. The dual is $V' = \mathcal{L}(V, \mathbb{F})$ and $\dim \mathbb{F} = 1$, so $\dim V' = \dim V \cdot 1 = \dim V$. This is the proof of the theorem, applied at the level of formulas. *Example problem:* if asked for the dimension of "linear functionals" on a finite-dimensional space, the answer is just $\dim V$.

The second disguised source is **a basis of $V$ in hand**. Once a basis exists, the [[Def - Dual Basis|dual basis]] exists by the linear-map extension lemma, and biorthogonality $\varphi_j(v_k) = \delta_{jk}$ forces linear independence (a vanishing linear combination $\sum a_j \varphi_j = 0$ applied to $v_k$ gives $a_k = 0$). The dual basis has the same length as the basis, so dimension is preserved. *Example problem:* exhibit an explicit basis of $V'$ given a basis of $V$ — use the dual basis directly.

The third disguised source is **the universal property of $V'$ as a coordinate-extracting space**. The vector $v \in V$ has $n$ coordinates in any basis; the functional $\varphi$ has $n$ values when evaluated on a basis; both spaces have the same parameter count. This is the abstract reason the dimensions match.

**Targets (Output Amplification)**

Combine with **basis-extension**. Given a basis of a subspace $U \leq V$, extend to a basis of $V$, then dualize — the dual basis of $V'$ contains a sublist that *annihilates* $U$. This is the structural setup for the [[Def - Annihilator (Dual Space)|annihilator]] dimension formula $\dim U^0 = \dim V - \dim U$ ([[Ex - Annihilator of a subspace has complementary dimension]]).

Combine with **the dual map**. The matrix of $T'$ in dual bases has size $\dim V' \times \dim W' = \dim V \times \dim W$, but transposed: it is the *transpose* of the matrix of $T$, which has size $\dim W \times \dim V$ (entries indexed differently). The dimension match is essential for the transpose to make sense at the matrix level — see [[Thm - Matrix of Dual Map is Transpose]].

Combine with **the double dual**. Since $\dim V'' = \dim V' = \dim V$, the canonical evaluation $\Lambda : V \to V''$ between same-dimensional spaces is *automatically* an isomorphism once shown injective ([[Ex - Double dual is naturally isomorphic to the original]]). The dimension equality removes the surjectivity check.

---

# Why Is It True

The dual basis exists, it is linearly independent, and it has $n$ elements — that is the whole story.

**The dual basis exists** by the linear-map extension lemma: a linear map out of $V$ is determined freely by its values on any basis. We define each $\varphi_j$ by setting $\varphi_j(v_j) = 1$ and $\varphi_j(v_k) = 0$ for $k \neq j$, and extending linearly. The extension is unique.

**The dual basis is linearly independent**: if $\sum a_j \varphi_j = 0$ in $V'$, apply both sides to $v_k$ to get $\sum a_j \varphi_j(v_k) = a_k = 0$, for each $k$. So all coefficients vanish.

**The dual basis spans $V'$**: any $\psi \in V'$ is determined by its values $\psi(v_1), \dots, \psi(v_n)$ on the basis. The functional $\sum_j \psi(v_j) \varphi_j$ agrees with $\psi$ on each basis vector (verifying: $(\sum_j \psi(v_j) \varphi_j)(v_k) = \sum_j \psi(v_j) \delta_{jk} = \psi(v_k)$), and linear functionals agreeing on a basis are equal. So $\psi = \sum_j \psi(v_j) \varphi_j$.

So the dual basis has $n$ elements, is linearly independent, and spans $V'$ — making it a basis. The dimension is $n = \dim V$.

> **The whole intuition in one sentence: a functional is determined by its values on a basis (which is $n$ free choices), so the space of functionals has dimension $n$.**

---

# What Makes This Hard

The result feels easy, and the standard proof is mechanical, but two slips are common. The first is *not verifying that the dual basis spans* — students often check that the dual basis is linearly independent and then "argue by counting" that it must be a basis, without realising they need to know $\dim V' \geq n$ first. The cleanest proof writes any $\psi \in V'$ explicitly as $\sum_j \psi(v_j) \varphi_j$ and verifies, rather than counting.

The second slip is *thinking $V$ and $V'$ are "the same"*. They are isomorphic, with the same dimension, but they are not the same vector space — vectors live in $V$, functionals in $V'$. The lack of a *canonical* isomorphism is what distinguishes the duality theory from a trivial relabelling: an isomorphism $V \cong V'$ has to make a choice (a basis or an inner product), and the choice has consequences.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Two routes are available.
- Route 1 (slick): Use $V' = \mathcal{L}(V, \mathbb{F})$ and the formula $\dim \mathcal{L}(V, W) = (\dim V)(\dim W)$ with $W = \mathbb{F}$.
- Route 2 (explicit): Construct the dual basis $\varphi_j$, show it is a basis of $V'$, and count.

Route 1 is one line. Route 2 takes a few steps but is more informative — it produces an actual basis.

**Subgoal decomposition (Route 2):**

1. **Choose a basis of $V$.** Let $v_1, \dots, v_n$ be a basis.
   - *Hint:* Any basis works; the dual basis exists relative to *any* choice.
   - *Why needed:* The dual basis is defined in terms of a chosen basis.

2. **Define the dual basis $\varphi_1, \dots, \varphi_n$ in $V'$.** Each $\varphi_j$ is the unique linear functional with $\varphi_j(v_k) = \delta_{jk}$.
   - *Hint:* Existence is by the linear-map extension lemma.
   - *Why needed:* You need explicit candidate basis elements.

3. **Show linear independence.** A vanishing combination $\sum a_j \varphi_j = 0$, applied to each $v_k$, gives $a_k = 0$.
   - *Hint:* The biorthogonality $\varphi_j(v_k) = \delta_{jk}$ does all the work.
   - *Why needed:* Linear independence is half of being a basis.

4. **Show spanning.** Any $\psi \in V'$ equals $\sum_j \psi(v_j) \varphi_j$.
   - *Hint:* Both sides agree on each basis vector $v_k$ — check by direct computation $(\sum_j \psi(v_j) \varphi_j)(v_k) = \psi(v_k)$ using $\varphi_j(v_k) = \delta_{jk}$. Linear functionals agreeing on a basis are equal.
   - *Why needed:* Spanning is the other half.

5. **Count.** The basis has $n$ elements. Hence $\dim V' = n = \dim V$.
   - *Hint:* Length of any basis is the dimension.
   - *Why needed:* The conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Linear-map extension lemma
> **Statement:** Let $v_1, \dots, v_n$ be a basis of $V$ and let $w_1, \dots, w_n$ be any elements of $W$. There is a unique linear map $T : V \to W$ with $T(v_k) = w_k$ for each $k$.
>
> **Hint:** Define $T(\sum c_k v_k) := \sum c_k w_k$. Uniqueness follows because linearity forces this formula.
>
> **Why needed:** It guarantees that the dual basis elements $\varphi_j$ exist as linear functionals, with prescribed values $\delta_{jk}$ on basis vectors.
>
> > [!note]- Full proof
> > **Existence:** every $v \in V$ has a unique expansion $v = \sum_k c_k v_k$ in the basis. Define $T(v) := \sum_k c_k w_k$. The uniqueness of the expansion makes $T$ well-defined; linearity follows from uniqueness of expansion under addition and scalar multiplication.
> >
> > **Uniqueness:** any linear $T$ with the prescribed values satisfies $T(\sum c_k v_k) = \sum c_k T(v_k) = \sum c_k w_k$, which is the definition. So $T$ is determined.

> [!note]- Lemma 2: Linear functionals agreeing on a basis are equal
> **Statement:** Let $v_1, \dots, v_n$ be a basis of $V$. If $\varphi, \psi \in V'$ satisfy $\varphi(v_k) = \psi(v_k)$ for every $k$, then $\varphi = \psi$.
>
> **Hint:** Any $v \in V$ is $\sum c_k v_k$, and $\varphi(v) = \sum c_k \varphi(v_k) = \sum c_k \psi(v_k) = \psi(v)$ by linearity.
>
> **Why needed:** It is used to conclude that $\psi = \sum_j \psi(v_j) \varphi_j$ in the spanning step.
>
> > [!note]- Full proof
> > For $v = \sum c_k v_k$, by linearity of $\varphi$:
> > $$\varphi(v) = \sum_k c_k \varphi(v_k) = \sum_k c_k \psi(v_k) = \psi(v).$$
> > So $\varphi(v) = \psi(v)$ for every $v \in V$, hence $\varphi = \psi$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Route 1 (slick).** By definition $V' = \mathcal{L}(V, \mathbb{F})$. By the dimension formula for spaces of linear maps,
> $$\dim V' = \dim \mathcal{L}(V, \mathbb{F}) = (\dim V)(\dim \mathbb{F}) = (\dim V)(1) = \dim V.$$
> The space $\mathcal{L}(V, W)$ is finite-dimensional when both $V$ and $W$ are, so $V'$ is finite-dimensional. $\blacksquare$
>
> **Route 2 (explicit, exhibiting a basis).** Let $v_1, \dots, v_n$ be a basis of $V$, where $n = \dim V$.
>
> **Step 1 — define the dual basis.** For each $j \in \{1, \dots, n\}$, by Lemma 1, there is a unique linear functional $\varphi_j : V \to \mathbb{F}$ with $\varphi_j(v_k) = \delta_{jk}$.
>
> **Step 2 — linear independence.** Suppose $a_1 \varphi_1 + \cdots + a_n \varphi_n = 0$ in $V'$, where $a_j \in \mathbb{F}$. Applying both sides to $v_k$:
> $$(a_1 \varphi_1 + \cdots + a_n \varphi_n)(v_k) = a_1 \varphi_1(v_k) + \cdots + a_n \varphi_n(v_k) = a_k,$$
> using $\varphi_j(v_k) = \delta_{jk}$. The right-hand side is $0(v_k) = 0$, so $a_k = 0$ for every $k$. Hence $\varphi_1, \dots, \varphi_n$ is linearly independent.
>
> **Step 3 — spanning.** Take any $\psi \in V'$. Define $\tilde \psi := \sum_{j=1}^n \psi(v_j) \varphi_j$. Apply to $v_k$:
> $$\tilde \psi(v_k) = \sum_{j=1}^n \psi(v_j) \varphi_j(v_k) = \sum_{j=1}^n \psi(v_j) \delta_{jk} = \psi(v_k).$$
> So $\tilde \psi$ and $\psi$ agree on the basis $v_1, \dots, v_n$. By Lemma 2, $\tilde \psi = \psi$. Hence $\psi$ is in the span of $\varphi_1, \dots, \varphi_n$.
>
> **Step 4 — conclude.** The list $\varphi_1, \dots, \varphi_n$ is a linearly independent spanning list in $V'$, hence a basis. Therefore $\dim V' = n = \dim V$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Polynomials with point evaluations as functionals.** Show that on $\mathcal{P}_n(\mathbb{R})$ (polynomials of degree $\leq n$), the $n + 1$ functionals $p \mapsto p(a_0), p(a_1), \dots, p(a_n)$ — evaluations at $n + 1$ distinct points — form a basis of the dual space. The proof uses Lagrange interpolation: the polynomials $L_k(x) = \prod_{j \neq k} (x - a_j)/(a_k - a_j)$ form the dual basis, with $L_k(a_j) = \delta_{jk}$. This is the original setting in which dual bases were used — by Lagrange — long before linear algebra was formalised.

**Smooth functions on a manifold.** For a finite-dimensional vector space of smooth functions (such as polynomials of degree $\leq n$), the *differentiation evaluations* $p \mapsto p^{(k)}(0)/k!$ for $k = 0, 1, \dots, n$ also form the dual basis of the basis $1, x, x^2, \dots, x^n$. This is the Taylor expansion in disguise: the value $p^{(k)}(0)/k!$ is exactly the $k$-th Taylor coefficient. So *Taylor's formula is the dual-basis expansion*.

**Trace as a sum of dual-basis pairings.** On $\mathcal{L}(V)$, the trace $\operatorname{tr}(T) = \sum_k \varphi_k(T(v_k))$ is independent of the basis. This is a linear functional on $\mathcal{L}(V)$, and one can ask: what is the dual basis to the natural basis of $\mathcal{L}(V)$? The answer involves the *Killing form* and trace-pairing, and the discussion previews the inner product on $\mathcal{L}(V)$ via $\langle S, T \rangle = \operatorname{tr}(S^* T)$ — see [[Linear Algebra VII — §7 Operators on Inner Product Spaces|Chapter 7]].

---

# Bridges

- **[[Thm - Dimension of a Sum of Subspaces]]** — applies in tandem with the present theorem to count dimensions of sums of subspaces of $V'$: a sum of annihilators is the annihilator of an intersection, with the dimension formulas chaining via $\dim U^0 = \dim V - \dim U$.

- **[[Def - Dual Basis]]** — the proof of the present theorem *constructs* the dual basis. The theorem is the dimensional consequence of the existence of dual bases; the dual basis is the explicit witness.

- **[[Ex - Double dual is naturally isomorphic to the original]]** — the present theorem implies $\dim V'' = \dim V' = \dim V$, which is the dimension input that lets the canonical evaluation $\Lambda : V \to V''$ (injective by construction) become an isomorphism in finite dimensions.

- **[[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz Representation]]** (preview, [[Linear Algebra VI — §6 Inner Product Spaces|Chapter 6]]) — in an inner product space, the isomorphism $V \cong V'$ is given canonically by $w \mapsto \langle \cdot, w \rangle$. This is a "natural" version of the basis-dependent isomorphism of the present theorem, made canonical by the inner product.

- **Hahn-Banach Theorem** (Functional Analysis) — in infinite dimensions, $V'$ may be much larger or smaller than $V$, and the existence of "enough" functionals (e.g., one separating any two points) is the content of the **Hahn-Banach theorem**. This is the substantive content that replaces the easy finite-dimensional dimension equality.

---

# Unlocked by This

> [!tip] Dimension of the Annihilator *(from this topic)*
> The dimension formula $\dim U + \dim U^0 = \dim V$ for the [[Def - Annihilator (Dual Space)|annihilator]] follows from the present theorem combined with the linear-map dimension formula applied to the inclusion $i : U \hookrightarrow V$. See [[Ex - Annihilator of a subspace has complementary dimension]].

> [!tip] Matrix of Dual Map is Transpose *(from this topic)*
> Once dual bases exist for $V$ and $W$, one can write down the matrix of the dual map $T'$ in the dual bases. The matrix is the transpose of the original — see [[Thm - Matrix of Dual Map is Transpose]].

> [!tip] Double Dual is Naturally Isomorphic to $V$ *(from this topic)*
> The dimension equality $\dim V'' = \dim V$ allows the canonical evaluation map $\Lambda$ to be an isomorphism — see [[Ex - Double dual is naturally isomorphic to the original]].

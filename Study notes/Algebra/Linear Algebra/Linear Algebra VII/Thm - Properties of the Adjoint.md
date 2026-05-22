---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
  - "Def - Null Space and Range"
tags: [algebra, linear-algebra]
---

# Notation

$V$ and $W$ are finite-dimensional [[Def - Inner Product Space|inner product spaces]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. The [[Def - Adjoint of a Linear Map|adjoint]] $T^*$ of $T \in \mathcal{L}(V, W)$ is the unique map satisfying $\langle Tv, w \rangle_W = \langle v, T^* w \rangle_V$. The orthogonal complement of $U \subseteq V$ is $U^\perp = \{v \in V : \langle v, u \rangle = 0 \text{ for all } u \in U\}$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Properties of the adjoint).** Let $V$, $W$, $U$ be finite-dimensional inner product spaces over $\mathbb{F}$. The adjoint operation enjoys the following properties:
>
> 1. **(Conjugate-linearity in the operator.)** $(\alpha T + \beta S)^* = \overline{\alpha} T^* + \overline{\beta} S^*$ for $S, T \in \mathcal{L}(V, W)$ and $\alpha, \beta \in \mathbb{F}$.
> 2. **(Composition reverses.)** $(S T)^* = T^* S^*$ for $T \in \mathcal{L}(V, W)$, $S \in \mathcal{L}(W, U)$.
> 3. **(Involution.)** $T^{**} = T$ for $T \in \mathcal{L}(V, W)$.
> 4. **(Identity.)** $I_V^* = I_V$.
> 5. **(Adjoint of an isomorphism.)** If $T$ is invertible then $T^*$ is invertible and $(T^*)^{-1} = (T^{-1})^*$.
> 6. **(Null space–range duality.)** For $T \in \mathcal{L}(V, W)$:
>    - $\operatorname{null} T^* = (\operatorname{range} T)^\perp$,
>    - $\operatorname{range} T^* = (\operatorname{null} T)^\perp$,
>    - $\operatorname{null} T = (\operatorname{range} T^*)^\perp$,
>    - $\operatorname{range} T = (\operatorname{null} T^*)^\perp$.
> 7. **(Matrix description.)** In orthonormal bases of $V$ and $W$, the matrix of $T^*$ is the conjugate transpose of the matrix of $T$.

---

# Motivation

The adjoint operation is not a passive piece of bookkeeping — it has a rich algebraic structure, governed by these seven properties. Each one is necessary for the operator-theoretic calculus of inner product spaces to work, and together they make the adjoint the most useful single tool in the chapter.

The first four properties (1)–(4) say that the adjoint is a **conjugate-linear involution** on $\mathcal{L}(V, W)$ — a dagger structure, in the language of category theory. Property (5) extends this to invertibility: the adjoint of an inverse is the inverse of an adjoint, so the dagger structure descends to the group of invertible operators. Property (6) is the deepest: it says the adjoint *swaps null spaces with range complements*, a precise duality that lets you move between "what does $T$ kill?" and "what is orthogonal to $T$'s image?" — and these are the two questions about $T$ one most often asks. Property (7) is the computational realisation: in orthonormal bases, the adjoint is mechanical.

These seven properties are used throughout the chapter as routine identities. Whenever a calculation involves both $T$ and $T^*$ — most importantly in normality $T T^* = T^* T$, in self-adjointness $T = T^*$, in unitarity $T^* T = I$, in the construction of $T^* T$ for SVD — these identities are deployed without comment. The theorem is properly stated once and remembered, not rederived.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$T$ is a linear map between finite-dimensional inner product spaces." This is the universal setting; the theorem applies always.

The first disguised source is **any computation involving multiple operators in an inner product.** Property (2) — $(ST)^* = T^*S^*$ — is the engine for symbolic manipulation. *Example problem:* simplify $\langle ST v, w \rangle$ to $\langle v, ? \rangle$, where $?$ is determined by $S$ and $T$.

The second disguised source is **any question about orthogonality of images or kernels.** Property (6) — the null-space/range duality — is the bridge from "vectors orthogonal to $\operatorname{range} T$" to "vectors in $\operatorname{null} T^*$". *Example problem:* characterise $\{w : \langle Tv, w \rangle = 0 \text{ for all } v\}$. The answer is $(\operatorname{range} T)^\perp = \operatorname{null} T^*$, computed by setting up the orthogonality condition and recognising it as kernel of the adjoint.

The third disguised source is **the "transpose" of a matrix computation.** Property (7) — adjoint = conjugate transpose in orthonormal bases — converts an operator-level identity into a matrix-level identity. *Example problem:* show that the rank of a matrix equals the rank of its transpose; this is property (6) plus the rank-nullity theorem.

**Targets (Output Amplification)**

The conclusion is the seven-property list itself, treated as routine identities.

Combine property (6) with **the [[Thm - Fundamental Theorem of Linear Maps|rank-nullity theorem]]**: from $\dim \operatorname{null} T + \dim \operatorname{range} T = \dim V$ and the orthogonal complement dimension formula $\dim U + \dim U^\perp = \dim V$, you derive $\dim \operatorname{range} T = \dim \operatorname{range} T^*$. This is **row-rank-equals-column-rank** for matrices, the fundamental dimension formula. The non-obvious leverage is that property (6) translates rank statements about $T^*$ into rank statements about $T$ via orthogonal complements.

Combine properties (1)–(4) with **operator algebra**: $\mathcal{L}(V)$ together with adjoint is a **$*$-algebra**. The properties above are exactly the axioms of a $*$-algebra structure. Self-adjoint, normal, unitary operators are defined in terms of relations between $T$ and $T^*$, and the $*$-algebra structure is what gives these definitions their power. The infinite-dimensional generalisation is the theory of **$C^*$-algebras**.

Combine property (2) with **self-adjointness**: if $T$ is self-adjoint and $S$ is any operator, $(STS^*)^* = S^{**}T^* S^* = STS^*$, so **$STS^*$ is self-adjoint whenever $T$ is**. This conjugation operation preserves self-adjointness, is what makes covariance matrices (positive operators) closed under change-of-basis, and is the algebraic content of "self-adjointness is a basis-independent property".

---

# Why Is It True

These properties all flow from the **defining relation** of the adjoint, $\langle Tv, w \rangle = \langle v, T^* w \rangle$, together with the basic properties of the inner product. The systematic way to derive any of them is: write the relation involving the operator combination, move things across the comma by the defining relation, and read off the result.

**The mechanism:** to find the adjoint of an expression in $T$, $S$, $\alpha T$, $ST$, etc., write the inner product $\langle (\text{expression}) v, w \rangle$, push the operators to the other side of the comma using the defining relation, and identify the resulting operator as the adjoint.

For (1), $\langle (\alpha T + \beta S) v, w \rangle = \alpha \langle Tv, w \rangle + \beta \langle Sv, w \rangle = \alpha \langle v, T^* w \rangle + \beta \langle v, S^* w \rangle = \langle v, \overline{\alpha} T^* w + \overline{\beta} S^* w \rangle$ — the bar-flip is because conjugate-linearity in the second slot of $\langle \cdot, \cdot \rangle$ moves the $\overline{\cdot}$ in. The adjoint of a linear combination is therefore a *conjugate* linear combination, with the bars on the scalars.

For (2), $\langle (ST) v, w \rangle = \langle T v, S^* w \rangle = \langle v, T^* S^* w \rangle$. The order *reverses* because each composition step moves one operator across the comma, and the operator that was outermost (closest to $w$) becomes innermost (next to $v$ inside the adjoint).

For (3), apply (2) with the swap and the defining relation: $\langle T^* w, v \rangle = \overline{\langle v, T^* w \rangle} = \overline{\langle T v, w \rangle} = \langle w, Tv \rangle$, so $T^{**} = T$. The involution is structural — applying the adjoint twice "lands back" by conjugating both sides of the inner product.

For (4), trivial: $\langle I v, w \rangle = \langle v, w \rangle = \langle v, I w \rangle$, so $I^* = I$.

For (5), use (2): $T^{-1} T = I$, so taking adjoints, $T^* (T^{-1})^* = I^* = I$, which means $(T^{-1})^*$ is the right inverse of $T^*$. Similarly $T T^{-1} = I$ gives $(T^{-1})^* T^* = I$, the left inverse. So $(T^{-1})^* = (T^*)^{-1}$.

For (6), the null-space-range duality: $w \in \operatorname{null} T^*$ iff $T^* w = 0$ iff $\langle v, T^* w \rangle = 0$ for all $v$ iff $\langle Tv, w \rangle = 0$ for all $v$ iff $w \in (\operatorname{range} T)^\perp$. The other three relations follow by replacing $T$ with $T^*$ and applying $T^{**} = T$ and the involution of orthogonal complement $U^{\perp\perp} = U$ (for closed subspaces in finite dimensions, all subspaces are closed).

For (7), with orthonormal bases $e_1, \ldots, e_n$ of $V$ and $f_1, \ldots, f_m$ of $W$, the matrix entries are $T_{jk} = \langle Te_k, f_j \rangle$ and $(T^*)_{jk} = \langle T^* f_k, e_j \rangle$. Then $(T^*)_{jk} = \langle T^* f_k, e_j \rangle = \overline{\langle e_j, T^* f_k \rangle} = \overline{\langle T e_j, f_k \rangle} = \overline{T_{kj}}$. So the matrix of $T^*$ is the conjugate transpose, **provided the bases are orthonormal** — non-orthonormal bases introduce Gram matrix corrections.

**The unifying mechanism: every property is the defining relation, used once.** Each derivation is one application of $\langle Tv, w \rangle = \langle v, T^* w \rangle$, followed by basic inner product manipulations. The conjugate-linearity of the inner product in the second slot is responsible for every appearance of a bar.

---

# What Makes This Hard

The most common error is **forgetting the bar in property (1)**: writing $(\alpha T)^* = \alpha T^*$ instead of $\overline{\alpha} T^*$. The bar appears because conjugate-linearity in the second slot of the inner product moves the conjugation out: $\langle (\alpha T) v, w \rangle = \alpha \langle Tv, w \rangle = \alpha \langle v, T^* w \rangle = \langle v, \overline{\alpha} T^* w \rangle$. Over $\mathbb{R}$ this is invisible; over $\mathbb{C}$ it is essential.

The second common error is **forgetting to invert the order in property (2)**: writing $(ST)^* = S^* T^*$ instead of $T^* S^*$. The order reverses because each step of the derivation moves one operator past the comma, and the operator nearer the "free" slot becomes the operator nearer the result side of the new adjoint.

The third subtlety is that property (7) — adjoint equals conjugate transpose — holds *only in orthonormal bases*. In a non-orthonormal basis the matrix of $T^*$ is $G^{-1} M^* G$, where $G$ is the Gram matrix of the basis. This is why orthonormal bases are essentially the only useful basis for inner-product space calculations.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Each property is derived by writing the relevant inner product involving the operator combination, applying the defining relation $\langle Tv, w \rangle = \langle v, T^* w \rangle$ enough times to move operators across the comma, and identifying the result.

**Subgoal decomposition:**

1. **(Conjugate-linearity, property 1).** Write $\langle (\alpha T + \beta S) v, w \rangle = \langle v, (\alpha T + \beta S)^* w \rangle$ and use linearity in the first slot plus conjugate-linearity in the second to derive $(\alpha T + \beta S)^* w = \overline{\alpha} T^* w + \overline{\beta} S^* w$.
   - *Hint:* The bar comes from $\langle v, \alpha u \rangle = \overline{\alpha} \langle v, u \rangle$.
   - *Why needed:* Foundational; nothing about adjoints can be done without it.

2. **(Composition, property 2).** Compute $\langle (ST) v, w \rangle$ by applying the defining relation first to $S$, then to $T$: $\langle (ST) v, w \rangle = \langle Tv, S^* w \rangle = \langle v, T^* S^* w \rangle$.
   - *Hint:* The order reverses because each defining relation moves one operator at a time.
   - *Why needed:* Used in every algebraic manipulation of adjoints.

3. **(Involution, property 3).** From the defining relation applied symmetrically: $\langle T^* w, v \rangle = \overline{\langle v, T^* w \rangle} = \overline{\langle T v, w \rangle} = \langle w, Tv \rangle$, so $T^{**} = T$.
   - *Hint:* Use conjugation of both sides of the inner product.
   - *Why needed:* Confirms the adjoint is an involution, making "self-adjoint" a meaningful condition.

4. **(Identity, property 4) and (Invertibility, property 5).** Direct from the defining relation and property (2): $\langle Iv, w \rangle = \langle v, Iw \rangle$, so $I^* = I$; and $TT^{-1} = I$ gives $(T^{-1})^*T^* = I$, so $(T^*)^{-1} = (T^{-1})^*$.

5. **(Null space/range duality, property 6).** Prove the first identity $\operatorname{null} T^* = (\operatorname{range} T)^\perp$ and derive the others.
   - *Hint:* $w \in \operatorname{null} T^*$ iff $T^* w = 0$ iff $\langle v, T^* w \rangle = 0$ for all $v$ iff $\langle Tv, w \rangle = 0$ for all $v$ iff $w \in (\operatorname{range} T)^\perp$.
   - *Why needed:* This is the central duality theorem of inner product space operator theory; it underlies the Fredholm alternative and many existence/uniqueness arguments.

6. **(Matrix description, property 7).** Compute matrix entries $(T^*)_{jk} = \langle T^* f_k, e_j \rangle = \overline{T_{kj}}$ in orthonormal bases.
   - *Hint:* Use $\langle T^* f_k, e_j \rangle = \overline{\langle e_j, T^* f_k \rangle} = \overline{\langle T e_j, f_k \rangle}$.
   - *Why needed:* The computational realisation; orthonormal bases are essential.

---

# Lemma Decomposition

> [!note]- Lemma 1: Adjoint of a scalar multiple is conjugate
> **Statement:** $(\alpha T)^* = \overline{\alpha} T^*$.
>
> **Hint:** Push $\alpha$ across the comma using conjugate-linearity in the second slot.
>
> **Why needed:** The smallest non-trivial case of property (1), and the case where the bar is most likely to be forgotten.
>
> > [!note]- Full proof
> > For any $v, w$: $\langle (\alpha T) v, w \rangle = \alpha \langle Tv, w \rangle = \alpha \langle v, T^* w \rangle = \langle v, \overline{\alpha} T^* w \rangle$. The first equality is linearity of $T$ then linearity of the first slot; the second is the defining relation of $T^*$; the third is conjugate-linearity of $\langle \cdot, \cdot \rangle$ in the second slot. By uniqueness of the adjoint, $(\alpha T)^* = \overline{\alpha} T^*$.

> [!note]- Lemma 2: Composition reverses
> **Statement:** $(ST)^* = T^* S^*$ for composable $T : V \to W$, $S : W \to U$.
>
> **Hint:** Apply the defining relation twice in sequence, each step moving one operator.
>
> **Why needed:** The order-reversal is essential to all algebraic manipulations of adjoints; without it you cannot manipulate products.
>
> > [!note]- Full proof
> > For any $v \in V$, $u \in U$: $\langle (ST) v, u \rangle_U = \langle Tv, S^* u \rangle_W = \langle v, T^* S^* u \rangle_V$. The first equality applies the defining relation of $S^*$ (moving $S$ from one slot of the $U$-inner-product to the other); the second applies the defining relation of $T^*$ (moving $T$ similarly across the $W$-inner-product). By uniqueness, $(ST)^* = T^* S^*$.

> [!note]- Lemma 3: Null space of $T^*$ equals orthogonal complement of range of $T$
> **Statement:** $\operatorname{null} T^* = (\operatorname{range} T)^\perp$.
>
> **Hint:** Rewrite "$T^* w = 0$" as "for all $v$, $\langle v, T^* w \rangle = 0$", then push $T$ back across.
>
> **Why needed:** The first of the four null-range duality identities; the others follow from this plus $T^{**} = T$ and $U^{\perp\perp} = U$.
>
> > [!note]- Full proof
> > $w \in \operatorname{null} T^*$ iff $T^* w = 0$ iff $\langle v, T^* w \rangle = 0$ for all $v \in V$ (use that $V \neq 0$ to extract the zero vector via $v = T^* w$). By the defining relation, this is iff $\langle Tv, w \rangle = 0$ for all $v$, iff $w \perp Tv$ for all $v$, iff $w \in (\operatorname{range} T)^\perp$. So $\operatorname{null} T^* = (\operatorname{range} T)^\perp$.

> [!note]- Lemma 4: All four null-range duality identities
> **Statement:** $\operatorname{null} T^* = (\operatorname{range} T)^\perp$, $\operatorname{range} T^* = (\operatorname{null} T)^\perp$, $\operatorname{null} T = (\operatorname{range} T^*)^\perp$, $\operatorname{range} T = (\operatorname{null} T^*)^\perp$.
>
> **Hint:** Get the first from Lemma 3; get the others by replacing $T$ with $T^*$ (and using $T^{**} = T$), and by taking orthogonal complements.
>
> **Why needed:** All four are used routinely; having the symmetry between primal and dual settings allows arguments to be set up on either side.
>
> > [!note]- Full proof
> > Lemma 3 gives identity (i): $\operatorname{null} T^* = (\operatorname{range} T)^\perp$. Apply Lemma 3 with $T$ replaced by $T^*$: $\operatorname{null} T^{**} = (\operatorname{range} T^*)^\perp$, i.e., $\operatorname{null} T = (\operatorname{range} T^*)^\perp$ — identity (iii). Take the orthogonal complement of both sides of (i), using $U^{\perp\perp} = U$ for subspaces of a finite-dimensional inner product space: $(\operatorname{null} T^*)^\perp = \operatorname{range} T$ — identity (iv). Apply this with $T \leftrightarrow T^*$: $(\operatorname{null} T)^\perp = \operatorname{range} T^*$ — identity (ii). All four follow from one identity plus involution and complement double-negation.

---

# Formal Proof

> [!note]- Complete formal proof
> Use the defining relation $\langle Tv, w \rangle_W = \langle v, T^* w \rangle_V$ throughout.
>
> **(1)** For $S, T \in \mathcal{L}(V, W)$, $\alpha, \beta \in \mathbb{F}$, $v \in V$, $w \in W$:
> $$\langle (\alpha T + \beta S) v, w \rangle = \alpha \langle Tv, w \rangle + \beta \langle Sv, w \rangle = \alpha \langle v, T^* w \rangle + \beta \langle v, S^* w \rangle = \langle v, \overline{\alpha} T^* w + \overline{\beta} S^* w \rangle.$$
> By uniqueness of the adjoint, $(\alpha T + \beta S)^* = \overline{\alpha} T^* + \overline{\beta} S^*$.
>
> **(2)** For $T \in \mathcal{L}(V, W)$, $S \in \mathcal{L}(W, U)$, $v \in V$, $u \in U$:
> $$\langle (ST) v, u \rangle = \langle Tv, S^* u \rangle = \langle v, T^* S^* u \rangle.$$
> So $(ST)^* = T^* S^*$.
>
> **(3)** For $T \in \mathcal{L}(V, W)$, $w \in W$, $v \in V$:
> $$\langle T^* w, v \rangle_V = \overline{\langle v, T^* w \rangle_V} = \overline{\langle T v, w \rangle_W} = \langle w, T v \rangle_W.$$
> By the defining relation of $T^{**}$, $\langle T^* w, v \rangle = \langle w, T^{**} v \rangle$. Comparing, $\langle w, T v \rangle = \langle w, T^{**} v \rangle$ for all $w \in W$, $v \in V$. So $T^{**} = T$.
>
> **(4)** $\langle I_V v, w \rangle = \langle v, w \rangle = \langle v, I_V w \rangle$, so $I_V^* = I_V$.
>
> **(5)** If $T$ is invertible, then $TT^{-1} = I_W$ and $T^{-1}T = I_V$. Taking adjoints using (2) and (4): $(T^{-1})^* T^* = I_W$ and $T^* (T^{-1})^* = I_V$. So $T^*$ is invertible with $(T^*)^{-1} = (T^{-1})^*$.
>
> **(6)** For $w \in W$: $w \in \operatorname{null} T^*$ iff $T^* w = 0$ iff $\langle v, T^* w \rangle = 0$ for all $v \in V$ iff $\langle Tv, w \rangle = 0$ for all $v$ iff $w \in (\operatorname{range} T)^\perp$. So $\operatorname{null} T^* = (\operatorname{range} T)^\perp$. The other three identities follow by taking orthogonal complements (using $U^{\perp\perp} = U$ in finite dimensions) and by substituting $T \mapsto T^*$ (using $T^{**} = T$).
>
> **(7)** Let $e_1, \ldots, e_n$ be an orthonormal basis of $V$ and $f_1, \ldots, f_m$ an orthonormal basis of $W$. The matrix entry $T_{jk} = \langle T e_k, f_j \rangle$. Similarly, the matrix entry of $T^*$ in the bases $f_1, \ldots, f_m$ (of $W$) and $e_1, \ldots, e_n$ (of $V$) is $(T^*)_{jk} = \langle T^* f_k, e_j \rangle = \overline{\langle e_j, T^* f_k \rangle} = \overline{\langle T e_j, f_k \rangle} = \overline{T_{kj}}$. Thus the matrix of $T^*$ is the conjugate transpose of the matrix of $T$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

1. **Differential operators on function spaces.** On $L^2([0, 1])$ with functions vanishing at endpoints, compute the adjoint of the differentiation operator $D = \frac{d}{dx}$. Integration by parts gives $\langle Df, g \rangle = -\langle f, Dg \rangle$ + boundary terms; with vanishing boundary conditions, $D^* = -D$. Then the Laplacian $-D^2 = -D \cdot D$ has $(-D^2)^* = (-D)^* (-D)^* = D \cdot D = D^2$... wait, more carefully: $(D^2)^* = D^* D^* = (-D)(-D) = D^2$ so $D^2$ is self-adjoint. This is the operator-theoretic content of "the Laplacian is self-adjoint with appropriate boundary conditions". See [[Ex - Adjoint of differentiation is negative differentiation with boundary conditions]].

2. **Quantum mechanics and the canonical commutation relation.** The position operator $\hat x$ and momentum operator $\hat p = -i\hbar \partial_x$ on $L^2(\mathbb{R})$ are self-adjoint (with appropriate domains), and they satisfy $[\hat x, \hat p] = i\hbar$. From property (2): $[\hat x, \hat p]^* = (\hat x \hat p - \hat p \hat x)^* = \hat p^* \hat x^* - \hat x^* \hat p^* = \hat p \hat x - \hat x \hat p = -[\hat x, \hat p]$, so the commutator is anti-self-adjoint (skew-Hermitian). And $(i\hbar)^* = -i\hbar$, consistent. The self-consistency of the canonical commutation relation under the adjoint is property (2) at work.

3. **Graph theory and Laplacians.** The graph Laplacian $L$ of an undirected graph is $L = D - A$, where $D$ is the diagonal degree matrix and $A$ is the symmetric adjacency matrix. By property (1) and the self-adjointness of $D$ and $A$, $L$ is self-adjoint. The kernel of $L$ has dimension equal to the number of connected components — by property (6), this is also the dimension of the orthogonal complement of the range, which is the space of "harmonic" functions on the graph. The adjoint duality between kernel and range complement is at the heart of spectral graph theory.

4. **Information geometry — Fisher information matrix.** For a parametric family of probability distributions $p_\theta(x)$, the Fisher information matrix is $I(\theta) = E[(\nabla \log p)(\nabla \log p)^t]$, a positive semidefinite (self-adjoint) operator. Property (2) underlies many identities in information geometry, where the adjoint corresponds to the dual connection between primal and dual coordinate systems.

---

# Bridges

- **[[Def - Dual Map]]** — The adjoint and the dual map are the same operation in two languages. The [[Def - Dual Map|dual map]] $T' : W' \to V'$ goes between dual spaces and requires no inner product. The adjoint $T^* : W \to V$ goes between the spaces themselves and uses the inner product to identify $V \cong V'$ and $W \cong W'$ via the **Riesz map**. Under this identification, $T^*$ is $T'$ transported back to $V$ and $W$. All seven properties above have analogues for the dual map; property (1) loses its complex conjugate (the dual map is linear, not conjugate-linear), because the Riesz map is conjugate-linear and the two conjugations cancel.

- **[[Thm - Null Space and Range of Dual Map]]** — The dual-map analogue of property (6) gives null-space/range relations for the **annihilator** $U^0 = \{f \in V' : f|_U = 0\}$. Under the Riesz identification, the annihilator and the orthogonal complement coincide, and property (6) reads as: $\operatorname{null} T' = (\operatorname{range} T)^0$. The reason orthogonal complements and annihilators come out to the same thing for inner product spaces is exactly that the Riesz map is a (conjugate) linear isomorphism that sends one to the other.

- **[[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation theorem]]** — This is the *existence* theorem behind the adjoint. Without Riesz, you cannot construct $T^* w$ from the linear functional $v \mapsto \langle Tv, w \rangle$. The seven properties above are downstream consequences once $T^*$ is known to exist; Riesz is the existence input.

- **Functional calculus for self-adjoint operators** — When $T$ is self-adjoint ($T = T^*$), the spectral theorem gives functional calculus: $f(T)$ makes sense for any function $f$ on $\sigma(T)$, and $f(T)^* = \overline{f}(T)$ (computed via property (1) applied entry-wise to the spectral decomposition). The relation $f(T)^* = \overline{f}(T)$ is the operator-theoretic version of "conjugation of a complex-valued function on the spectrum", and it is the bridge from operator algebra to function-space analysis.

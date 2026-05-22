---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Jordan Basis and Jordan Form"
  - "Def - Generalized Eigenspace"
  - "Def - Nilpotent Operator"
  - "Thm - Generalized Eigenspace Decomposition"
  - "Thm - Null Spaces of Powers Stabilize"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbb{C}$ and $T \in \mathcal{L}(V)$. $J_k(\lambda)$ denotes the $k \times k$ Jordan block for eigenvalue $\lambda$ — $\lambda$s on the diagonal, $1$s on the superdiagonal, $0$s elsewhere. A **Jordan basis** is one in which $T$ has block-diagonal matrix with Jordan blocks on the diagonal; see [[Def - Jordan Basis and Jordan Form]]. Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

The nilpotent case of the theorem holds over any field (not just $\mathbb{C}$); the full statement requires every eigenvalue to lie in the field, which on a complex space is automatic by the Fundamental Theorem of Algebra.

---

# Statement

> **Theorem (Existence of Jordan form for nilpotent operators).** Suppose $T \in \mathcal{L}(V)$ is nilpotent. Then there is a basis of $V$ that is a Jordan basis for $T$.

> **Theorem (Existence of Jordan form, general).** Suppose $\mathbf{F} = \mathbb{C}$ and $T \in \mathcal{L}(V)$. Then there is a basis of $V$ that is a Jordan basis for $T$. With respect to such a basis, the matrix of $T$ is block diagonal with each block a Jordan block $J_k(\lambda)$ for some eigenvalue $\lambda$ of $T$. The multiset of (eigenvalue, block size) pairs is uniquely determined by $T$.

In particular, every $n \times n$ complex matrix is similar to a block-diagonal matrix whose blocks are Jordan blocks.

---

# Motivation

This is the *canonical form theorem* for operators on a complex vector space. The point is that every operator $T$ — no matter how complicated it appears in a given basis — can be brought, by a change of basis, to a particularly sparse and structured form: block diagonal, with each block a Jordan block (eigenvalue on the diagonal, $1$s on the superdiagonal, zeros elsewhere). The Jordan form is the simplest matrix that $T$ admits, and it is the *complete* similarity invariant: two operators are similar iff their Jordan forms agree up to the order of the blocks.

The theorem is the answer to the natural follow-up question of the previous one — the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]]. That theorem told us $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$ with $T$ acting as $\lambda_k I + N_k$ on each piece, where $N_k$ is nilpotent. The structural picture is in place, but we still do not have a *canonical matrix* for $T$ — only a block-diagonal form with arbitrary upper-triangular blocks on each generalized eigenspace. The Jordan form refines this further: on each $G(\lambda_k, T)$, the nilpotent $N_k$ itself has a canonical form (the standard "shift" matrices arranged as Jordan blocks at $0$), and adding $\lambda_k I$ to a standard nilpotent gives the Jordan blocks $J_{m}(\lambda_k)$ at $\lambda_k$.

So the heart of the proof is the **nilpotent case**: every nilpotent operator has a Jordan basis. This is the hard step, and the rest of the proof is the assembly via the generalized eigenspace decomposition. The nilpotent case is in fact more general than the complex case — it holds over any field, including $\mathbb{R}$ — because nilpotence is field-independent. So the *real* theorem of §8C is the nilpotent Jordan form; the complex Jordan form is its assembly via the generalized eigenspace decomposition.

Why is the Jordan form *the* answer? Because the partition of block sizes for each eigenvalue is a complete similarity invariant. Two operators on $\mathbb{C}^n$ are similar iff they have the same Jordan form (up to block ordering). Equivalently, two complex matrices are similar iff their multiset of (eigenvalue, block size) pairs agree. Equivalently, two complex matrices are similar iff $\dim \operatorname{null}(A - \lambda I)^k = \dim \operatorname{null}(B - \lambda I)^k$ for every $\lambda$ and every $k$. The Jordan form is the matrix that exhibits these invariants explicitly.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is "complex vector space, any operator". Source-broadening is about recognising when the *Jordan form* (rather than weaker forms like upper triangular) is the right tool.

The first disguised source is **a problem about similarity of operators**. Two operators are similar iff their Jordan forms agree. *Example problem:* are the $4 \times 4$ matrices $\begin{pmatrix} 5 & 1 & 0 & 0 \\ 0 & 5 & 1 & 0 \\ 0 & 0 & 5 & 0 \\ 0 & 0 & 0 & 5 \end{pmatrix}$ and $\begin{pmatrix} 5 & 1 & 0 & 0 \\ 0 & 5 & 0 & 0 \\ 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 5 \end{pmatrix}$ similar? Both have the same characteristic polynomial $(z - 5)^4$ and the same trace $20$. But the first has Jordan form $J_3(5) \oplus J_1(5)$ (block partition $(3, 1)$), the second has Jordan form $J_2(5) \oplus J_2(5)$ (block partition $(2, 2)$). Different block partitions, so not similar. The Jordan form was the right tool because the characteristic polynomial alone could not distinguish them.

The second disguised source is **a problem about powers, polynomials, or functions of $T$**. The Jordan form makes computing $T^k$, $p(T)$, $f(T)$ straightforward: each Jordan block can be raised to a power explicitly using the binomial expansion $J_k(\lambda)^m = (\lambda I + N)^m = \sum_j \binom{m}{j} \lambda^{m-j} N^j$, which is a finite sum because $N^k = 0$. *Example problem:* compute $J_3(\lambda)^{10}$. Direct expansion: $J_3(\lambda)^{10} = (\lambda I + N)^{10} = \sum_{j=0}^{2} \binom{10}{j} \lambda^{10-j} N^j$ — only three terms because $N^3 = 0$ for a $3 \times 3$ Jordan block.

The third disguised source is **a problem requiring an explicit basis that makes $T$ "nice"**. The Jordan basis is the sparsest such basis. *Example problem:* find an explicit basis of $\mathbb{C}^3$ that diagonalises the operator $T(z_1, z_2, z_3) = (2 z_1 + z_2, 2 z_2, 2 z_3 + z_1)$ — except it cannot be diagonalised. The Jordan basis is the next-best thing, and computing it produces an explicit, useful basis where $T$ has at most one off-diagonal entry per row.

**Targets (Output Amplification)**

The bare conclusion is "a Jordan basis exists". Combined with other facts it does much more.

Combine with **dimensional invariants of $T$**. The Jordan block sizes for $\lambda$ form a partition of $\dim G(\lambda, T)$, and this partition is recovered from the dimensions $\dim \operatorname{null}(T - \lambda I)^k$: the number of blocks of size $\geq j$ is $\dim \operatorname{null}(T - \lambda I)^j - \dim \operatorname{null}(T - \lambda I)^{j-1}$. The further result $E$ is that the entire Jordan structure is computable from kernel dimensions, *without* hunting for an explicit Jordan basis — a major operational simplification for the similarity-question. *See* the prototypical exercise [[Ex - Operators with the same characteristic polynomial need not have the same Jordan form]].

Combine with **the minimal and characteristic polynomials**. The minimal polynomial is $m_T(z) = \prod_\lambda (z - \lambda)^{k_{\max}(\lambda)}$ where $k_{\max}(\lambda)$ is the size of the *largest* Jordan block at $\lambda$; the characteristic polynomial is $p_T(z) = \prod_\lambda (z - \lambda)^{d_\lambda}$ where $d_\lambda$ is the algebraic multiplicity (= sum of block sizes at $\lambda$). The further result $E$ is that the pair (characteristic polynomial, minimal polynomial) determines the Jordan form when every algebraic multiplicity is at most $3$ (because partitions of $1, 2, 3$ are determined by their maximum), but fails for higher multiplicities — the partitions $(2, 2)$ and $(3, 1)$ of $4$ are indistinguishable by characteristic polynomial alone. *See* exercise 11–14 of §8B in LADR.

Combine with **functions of $T$ holomorphic on the spectrum**. Once a Jordan form is in hand, $f(T)$ is computed block-by-block: $f(J_k(\lambda)) = \sum_{j=0}^{k-1} \frac{f^{(j)}(\lambda)}{j!} N^j$, a $k \times k$ upper triangular matrix with $f(\lambda)$ on the diagonal, $f'(\lambda)$ on the superdiagonal, and so on. The further result is the **holomorphic functional calculus** in finite dimensions, with explicit matrix formulas. This is how one computes $e^{tA}$, $\sqrt A$, $\log A$ in practice — bring $A$ to Jordan form, apply the function to each block.

---

# Why Is It True

The picture is two-step. **Step 1: reduce to the nilpotent case.** By the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]], $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$, and on each piece $T = \lambda_k I + N_k$ with $N_k = (T - \lambda_k I)|_{G(\lambda_k, T)}$ nilpotent. A Jordan basis of $G(\lambda_k, T)$ for the operator $N_k$ is automatically a Jordan basis of $G(\lambda_k, T)$ for $T$: adding $\lambda_k I$ to a Jordan-block-at-$0$ matrix gives a Jordan-block-at-$\lambda_k$ matrix. So the global Jordan basis is obtained by assembling Jordan bases of each piece for the corresponding nilpotent restriction.

**Step 2: prove the nilpotent case.** This is the heart of the proof and uses induction on $\dim V$. The key construction is to find a vector $u$ with $T^{m-1} u \neq 0$ (where $m$ is the smallest power killing $T$), then the chain $u, Tu, \dots, T^{m-1} u$ is linearly independent (by exercise 2 of §8A in LADR, which is the standard linear-independence-of-chains argument) and the subspace $U = \operatorname{span}(u, Tu, \dots, T^{m-1} u)$ is $T$-invariant — so $U$ is itself a Jordan block (when read in reverse order, the matrix of $T|_U$ in the basis $T^{m-1} u, T^{m-2} u, \dots, u$ is exactly $J_m(0)$).

If $U = V$, we are done. Otherwise we need to find a $T$-invariant complement $W$ with $V = U \oplus W$, so we can induct on $W$.

The construction of $W$ is the clever step. Pick a linear functional $\varphi \in V'$ with $\varphi(T^{m-1} u) \neq 0$ — such $\varphi$ exists by the dual-space construction. Define
$$W = \{ v \in V : \varphi(v) = \varphi(T v) = \cdots = \varphi(T^{m-1} v) = 0 \}.$$
Then $W$ is a subspace, and it is $T$-invariant: if $v \in W$ then $\varphi(T^k (T v)) = \varphi(T^{k+1} v)$, which equals $0$ for $k \leq m - 2$ (by the defining conditions for $v$) and equals $\varphi(T^m v) = \varphi(0) = 0$ for $k = m - 1$ (since $T^m = 0$).

Why is $V = U \oplus W$? The argument has two parts:
- $U \cap W = \{0\}$: if $v = c_0 u + c_1 Tu + \cdots + c_{m-1} T^{m-1} u \in W \cap U$ is nonzero, let $j$ be the smallest index with $c_j \neq 0$. Then $T^{m-1-j} v = c_j T^{m-1} u$ (the other terms vanish by $T^m = 0$), so $\varphi(T^{m-1-j} v) = c_j \varphi(T^{m-1} u) \neq 0$, contradicting $v \in W$.
- $\dim U + \dim W \geq \dim V$: define $S : V \to \mathbf{F}^m$ by $S v = (\varphi(v), \varphi(T v), \dots, \varphi(T^{m-1} v))$. Then $\ker S = W$, and by rank-nullity $\dim W = \dim V - \dim \operatorname{range} S \geq \dim V - m = \dim V - \dim U$. So $\dim(U + W) = \dim U + \dim W \geq \dim V$, hence $U + W = V$, and the previous bullet gives directness.

By induction on $\dim V$ (applied to $W$, of smaller dimension), $W$ has a Jordan basis for $T|_W$. Combining with the Jordan-block-basis of $U$ gives a Jordan basis of $V$.

**Mechanism summary: the longest chain $u, Tu, \dots, T^{m-1} u$ generates a Jordan block, and a linear functional $\varphi$ detecting the top of the chain defines a $T$-invariant complement via the conditions $\varphi(T^k v) = 0$ for $k < m$.**

---

# What Makes This Hard

The reduction to the nilpotent case via the generalized eigenspace decomposition is easy. The nilpotent case itself is the genuine difficulty, and the subtle step is the construction of the $T$-invariant complement $W$. Students try to construct $W$ as a "complement of $U$ in $V$" without the $T$-invariance constraint, but an arbitrary complement is not $T$-invariant in general — finding a $T$-invariant complement requires the linear-functional construction above.

The second common difficulty is proving the directness $U \cap W = \{0\}$: the argument requires picking the smallest index $j$ with $c_j \neq 0$ and applying $T^{m-1-j}$ to extract the leading term — a maneuver that resembles the linear-independence proof of [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]] but with a different power-application twist.

Uniqueness of the Jordan form is a separate (and easier) statement we omit from the formal proof here; it follows from the fact that the number of blocks of size $\geq j$ for $\lambda$ equals $\dim \operatorname{null}(T - \lambda I)^j - \dim \operatorname{null}(T - \lambda I)^{j-1}$, a basis-invariant quantity, so any two Jordan forms have the same block partition.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Two-step. First reduce to the nilpotent case using the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]]. Then prove the nilpotent case by induction on $\dim V$: find the longest chain $u, Tu, \dots, T^{m-1} u$, observe it spans a $T$-invariant Jordan-block subspace $U$, find a $T$-invariant complement $W$ via a linear functional, and induct.

**Subgoal decomposition:**

1. **Reduction to nilpotent case.** Show that if every nilpotent operator on a vector space admits a Jordan basis, then every operator on a complex space does.
   - *Hint:* Apply the generalized eigenspace decomposition. On each $G(\lambda_k, T)$, the operator $(T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent. A Jordan basis of this nilpotent (for $T - \lambda_k I$) is also a Jordan basis of $T|_{G(\lambda_k, T)}$ (the Jordan blocks just have $\lambda_k$ on the diagonal instead of $0$). Assemble across $k$.
   - *Why needed:* This is the "easy" direction. It localises the proof to the nilpotent case.

2. **Longest chain generates a Jordan block.** For $T$ nilpotent of nilpotency index $m$, find $u$ with $T^{m-1} u \neq 0$ and show $u, Tu, \dots, T^{m-1} u$ is linearly independent.
   - *Hint:* $T^m = 0$ but $T^{m-1} \neq 0$; pick $u$ such that $T^{m-1} u \neq 0$. For linear independence, a relation $\sum c_j T^j u = 0$ — apply $T^{m-1}$ to extract the leading term.
   - *Why needed:* The span $U = \operatorname{span}(u, Tu, \dots, T^{m-1} u)$ is the first Jordan block.

3. **$T$-invariant complement via a linear functional.** Find $W$ with $V = U \oplus W$ and $T(W) \subseteq W$.
   - *Hint:* Pick $\varphi \in V'$ with $\varphi(T^{m-1} u) \neq 0$. Set $W = \{ v : \varphi(v) = \varphi(T v) = \cdots = \varphi(T^{m-1} v) = 0 \}$. Show (a) $W$ is $T$-invariant; (b) $U \cap W = \{0\}$ by extracting leading coefficients; (c) $\dim W \geq \dim V - m$ by rank-nullity applied to $S : V \to \mathbf{F}^m, v \mapsto (\varphi(v), \dots, \varphi(T^{m-1} v))$.
   - *Why needed:* The induction step needs a $T$-invariant complement, not just any complement.

4. **Induction.** Apply the nilpotent Jordan form to $T|_W$ (smaller dimension) and assemble.
   - *Hint:* Base case $\dim V = 1$ trivial. Induction step: $\dim W < \dim V$, so $W$ has a Jordan basis for $T|_W$ by induction. Combine with the chain basis of $U$ (read in reverse: $T^{m-1} u, T^{m-2} u, \dots, u$ for the $J_m(0)$ matrix to come out right).
   - *Why needed:* This is the formal inductive step.

5. **Assembly into full Jordan form.** Combine (1) and (4) to give the complex Jordan form.
   - *Hint:* For each eigenvalue $\lambda_k$, get a Jordan basis of $G(\lambda_k, T)$ for the nilpotent $N_k = (T - \lambda_k I)|_{G(\lambda_k, T)}$ from the nilpotent Jordan form (steps 2–4). Translate by $\lambda_k$. Combine across $k$.
   - *Why needed:* This is the final statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: A chain of length $m$ is linearly independent
> **Statement:** Suppose $T \in \mathcal{L}(V)$, $m$ is a positive integer, $v \in V$, and $T^{m-1} v \neq 0$ but $T^m v = 0$. Then $v, T v, T^2 v, \dots, T^{m-1} v$ is linearly independent.
>
> **Hint:** Suppose $\sum_{j=0}^{m-1} c_j T^j v = 0$. Apply $T^{m-1-k}$ where $k$ is the smallest index with $c_k \neq 0$, to extract $c_k T^{m-1} v$.
>
> **Why needed:** It guarantees the chain generates an $m$-dimensional subspace, which becomes the Jordan block.
>
> > [!note]- Full proof
> > Suppose $c_0 v + c_1 T v + \cdots + c_{m-1} T^{m-1} v = 0$ for some scalars $c_0, \dots, c_{m-1}$. Let $k$ be the smallest index with $c_k \neq 0$ (if all are zero we are done). Apply $T^{m-1-k}$ to both sides:
> > $$\sum_{j=k}^{m-1} c_j T^{m-1-k+j} v = 0.$$
> > For $j \geq k+1$, the exponent $m - 1 - k + j \geq m$, so $T^{m-1-k+j} v = 0$. The only surviving term is the $j = k$ one: $c_k T^{m-1} v = 0$. But $T^{m-1} v \neq 0$ by hypothesis, so $c_k = 0$ — contradiction. Hence all $c_j = 0$, and the chain is linearly independent.

> [!note]- Lemma 2: The chain's span is $T$-invariant
> **Statement:** With $u, T, m$ as in Lemma 1, $U = \operatorname{span}(u, Tu, \dots, T^{m-1} u)$ is $T$-invariant.
>
> **Hint:** $T$ shifts the basis $u \to Tu \to \cdots \to T^{m-1} u \to T^m u = 0$.
>
> **Why needed:** The chain's span must be invariant under $T$ for it to be a "block" in the block-diagonal Jordan form.
>
> > [!note]- Full proof
> > Take any $v = \sum_{j=0}^{m-1} c_j T^j u \in U$. Then $T v = \sum_{j=0}^{m-1} c_j T^{j+1} u$. For $j \leq m - 2$, $T^{j+1} u \in U$ directly (it's one of the basis vectors). For $j = m - 1$, $T^m u = 0 \in U$. So $T v \in U$ — $U$ is $T$-invariant.

> [!note]- Lemma 3: A $T$-invariant complement exists
> **Statement:** Let $T \in \mathcal{L}(V)$ be nilpotent of index $m$, $u \in V$ with $T^{m-1} u \neq 0$, and $U = \operatorname{span}(u, Tu, \dots, T^{m-1} u)$. Then there exists a $T$-invariant subspace $W$ of $V$ with $V = U \oplus W$.
>
> **Hint:** Pick $\varphi \in V'$ with $\varphi(T^{m-1} u) \neq 0$. Define $W = \{v : \varphi(T^k v) = 0 \text{ for } k = 0, 1, \dots, m-1\}$. Verify: $W$ is $T$-invariant (since $\varphi(T^k (Tv)) = \varphi(T^{k+1} v) = 0$ for $k \leq m - 2$, and $\varphi(T^{m-1}(T v)) = \varphi(T^m v) = 0$); $U \cap W = \{0\}$ (extract leading coefficient with $T^{m-1-k}$ and apply $\varphi$); $\dim U + \dim W = \dim V$ (rank-nullity on $S : V \to \mathbf{F}^m, v \mapsto (\varphi(v), \dots, \varphi(T^{m-1} v))$, with $\ker S = W$ and $\operatorname{range} S$ at least $m$-dimensional because $S u = (\varphi(u), \dots, \varphi(T^{m-1} u))$ has last coordinate nonzero — and shifted versions of $u$ give the other coordinates).
>
> **Why needed:** The induction needs an invariant complement, not just any complement.
>
> > [!note]- Full proof
> > Let $\varphi \in V'$ satisfy $\varphi(T^{m-1} u) \neq 0$ — such $\varphi$ exists because $T^{m-1} u \neq 0$, so any linear functional extending "$T^{m-1} u \mapsto 1$" on the $1$-dimensional subspace $\operatorname{span}(T^{m-1} u)$ works.
> >
> > Define $W = \{ v \in V : \varphi(T^k v) = 0 \text{ for } k = 0, 1, \dots, m-1 \}$.
> >
> > **$W$ is $T$-invariant:** If $v \in W$, then for $k = 0, \dots, m-2$, $\varphi(T^k (T v)) = \varphi(T^{k+1} v) = 0$ (by the defining condition for $v$ at index $k+1 \leq m - 1$). For $k = m - 1$, $\varphi(T^{m-1}(T v)) = \varphi(T^m v) = \varphi(0) = 0$ (using $T^m = 0$). So $T v \in W$.
> >
> > **$U \cap W = \{0\}$:** Suppose $v = c_0 u + c_1 T u + \cdots + c_{m-1} T^{m-1} u$ is in $U \cap W$ and $v \neq 0$. Let $k$ be the smallest index with $c_k \neq 0$. Apply $T^{m-1-k}$:
> > $$T^{m-1-k} v = c_k T^{m-1} u + \sum_{j > k} c_j T^{m-1-k+j} u = c_k T^{m-1} u,$$
> > the higher terms vanishing because their $T$-exponents exceed $m - 1$. Hence
> > $$\varphi(T^{m-1-k} v) = c_k \varphi(T^{m-1} u) \neq 0.$$
> > But $v \in W$ requires $\varphi(T^{m-1-k} v) = 0$ (since $m - 1 - k \leq m - 1$). Contradiction.
> >
> > **$\dim U + \dim W = \dim V$:** Define $S : V \to \mathbf{F}^m$ by $S v = (\varphi(v), \varphi(T v), \dots, \varphi(T^{m-1} v))$. Then $\ker S = W$ exactly. By rank-nullity,
> > $$\dim W = \dim V - \dim \operatorname{range} S.$$
> > We claim $\dim \operatorname{range} S = m$, that is, $S$ is surjective. Compute $S(T^{m-1-j} u) = (\varphi(T^{m-1-j} u), \varphi(T^{m-j} u), \dots, \varphi(T^{2m-2-j} u))$. For $j = 0$ this is $(\varphi(T^{m-1} u), 0, 0, \dots, 0)$ (the higher terms are zero since their $T$-exponents are $\geq m$). For $j = 1$, $S(T^{m-2} u) = (\varphi(T^{m-2} u), \varphi(T^{m-1} u), 0, \dots, 0)$. In general $S(T^{m-1-j} u)$ has nonzero entry $\varphi(T^{m-1} u)$ in position $j$ and zero entries in positions $> j$, so the images $S(u), S(Tu), \dots, S(T^{m-1} u)$ are upper triangular with nonzero diagonal — linearly independent — so $S$ has rank $m$.
> >
> > Hence $\dim W = \dim V - m = \dim V - \dim U$, so $\dim U + \dim W = \dim V$. Combined with $U \cap W = \{0\}$, $V = U \oplus W$.

> [!note]- Lemma 4: Nilpotent Jordan form (induction)
> **Statement:** Every nilpotent operator $T \in \mathcal{L}(V)$ has a Jordan basis.
>
> **Hint:** Induct on $\dim V$. Base case $\dim V = 1$: $T = 0$ (only nilpotent in dimension $1$). Step: get $u, Tu, \dots, T^{m-1} u$ generating a Jordan block $U$ (Lemmas 1, 2); get $T$-invariant complement $W$ (Lemma 3); apply induction to $T|_W$.
>
> **Why needed:** This is the hardest case of the theorem; the general case reduces to it.
>
> > [!note]- Full proof
> > Induct on $\dim V$.
> >
> > **Base case $\dim V = 1$:** the only nilpotent operator is $T = 0$. The basis is any nonzero vector; the matrix is the $1 \times 1$ zero matrix, which is the Jordan block $J_1(0)$. Trivially a Jordan basis.
> >
> > **Induction step $\dim V > 1$:** Suppose the result holds for all vector spaces of smaller dimension. Let $m$ be the nilpotency index of $T$ (the smallest $m$ with $T^m = 0$). Then $T^{m-1} \neq 0$, so there is some $u \in V$ with $T^{m-1} u \neq 0$.
> >
> > By Lemma 1, $u, Tu, \dots, T^{m-1} u$ is linearly independent. By Lemma 2, $U = \operatorname{span}(u, Tu, \dots, T^{m-1} u)$ is $T$-invariant. The matrix of $T|_U$ in the (reversed) basis $T^{m-1} u, T^{m-2} u, \dots, T u, u$ is the $m \times m$ Jordan block $J_m(0)$: $T(T^{m-2} u) = T^{m-1} u$ (the previous basis vector), $T(T^{m-3} u) = T^{m-2} u$, ..., $T u = T u$ (one step backward), and $T(T^{m-1} u) = T^m u = 0$. The matrix is exactly the $m \times m$ shift matrix.
> >
> > **Case A: $U = V$.** The reversed basis $T^{m-1} u, \dots, u$ is a Jordan basis for $T$ on $V$ with matrix $J_m(0)$. Done.
> >
> > **Case B: $U \neq V$.** By Lemma 3, there is a $T$-invariant subspace $W$ with $V = U \oplus W$ and $\dim W = \dim V - m < \dim V$. The restriction $T|_W$ is nilpotent (any restriction of a nilpotent to an invariant subspace is nilpotent, with nilpotency index at most that of $T$). By the induction hypothesis, $T|_W$ has a Jordan basis $w_1, \dots, w_{\dim W}$.
> >
> > Combining: the basis of $V$ given by $T^{m-1} u, T^{m-2} u, \dots, u, w_1, w_2, \dots, w_{\dim W}$ is a Jordan basis for $T$. The matrix is block diagonal: the first $m \times m$ block is $J_m(0)$ from $U$; the remaining blocks come from the Jordan basis of $W$.

> [!note]- Lemma 5: Reduction from general to nilpotent case
> **Statement:** Suppose every nilpotent operator has a Jordan basis. Then every operator on a complex space has a Jordan basis.
>
> **Hint:** By [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]], $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$. On each $G(\lambda_k, T)$, the operator $N_k = (T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent. A Jordan basis of $G(\lambda_k, T)$ for $N_k$ is also a Jordan basis for $T|_{G(\lambda_k, T)}$ — the blocks just have $\lambda_k$ on the diagonal instead of $0$.
>
> **Why needed:** This is the assembly step.
>
> > [!note]- Full proof
> > By [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]], $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$ where the $\lambda_k$ are the distinct eigenvalues of $T$. For each $k$, the operator $N_k := (T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent. By hypothesis (or by Lemma 4), $N_k$ has a Jordan basis $v_1^{(k)}, \dots, v_{d_k}^{(k)}$ of $G(\lambda_k, T)$, where $d_k = \dim G(\lambda_k, T)$. In this basis the matrix of $N_k$ is block diagonal with Jordan blocks $J_{s_{k,i}}(0)$ for some sizes $s_{k,i}$.
> >
> > The matrix of $T|_{G(\lambda_k, T)} = N_k + \lambda_k I$ in the same basis is block diagonal with blocks $J_{s_{k,i}}(0) + \lambda_k I = J_{s_{k,i}}(\lambda_k)$ — the same blocks but with $\lambda_k$ on the diagonal instead of $0$.
> >
> > Concatenating the bases of all the $G(\lambda_k, T)$ in the order $k = 1, 2, \dots, m$ gives a basis of $V$ in which the matrix of $T$ is block diagonal with Jordan blocks $J_{s_{k,i}}(\lambda_k)$. This is a Jordan basis for $T$ on $V$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathbf{F} = \mathbb{C}$ and $T \in \mathcal{L}(V)$.
>
> **Step 0 — eigenvalues exist.** Since $\mathbf{F} = \mathbb{C}$ and $V$ is finite-dimensional nonzero, the Fundamental Theorem of Algebra applied to the characteristic polynomial (or minimal polynomial — see [[Thm - Existence of Eigenvalues on Complex Vector Spaces]]) guarantees at least one eigenvalue.
>
> **Step 1 — generalized eigenspace decomposition.** By [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]], $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$ where $\lambda_1, \dots, \lambda_m$ are the distinct eigenvalues of $T$. On each $G(\lambda_k, T)$, the operator $N_k := (T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent.
>
> **Step 2 — nilpotent Jordan form on each piece.** By Lemma 4, each nilpotent $N_k$ has a Jordan basis $v_1^{(k)}, \dots, v_{d_k}^{(k)}$ of $G(\lambda_k, T)$, in which the matrix of $N_k$ is block diagonal with Jordan blocks $J_{s_{k,i}}(0)$.
>
> **Step 3 — translate by $\lambda_k$.** The matrix of $T|_{G(\lambda_k, T)} = N_k + \lambda_k I$ in this basis is block diagonal with Jordan blocks $J_{s_{k,i}}(\lambda_k)$ (i.e., adding $\lambda_k$ to each diagonal entry).
>
> **Step 4 — assemble.** Concatenate the bases across $k$: the basis $v_1^{(1)}, \dots, v_{d_1}^{(1)}, v_1^{(2)}, \dots, v_{d_2}^{(2)}, \dots, v_1^{(m)}, \dots, v_{d_m}^{(m)}$ is a basis of $V$, and the matrix of $T$ in this basis is block diagonal with all the Jordan blocks $J_{s_{k,i}}(\lambda_k)$ on the diagonal. This is a Jordan basis for $T$, and the matrix is the Jordan form of $T$.
>
> **Uniqueness (up to block ordering).** For each eigenvalue $\lambda$, the number of Jordan blocks of size $\geq j$ in any Jordan form of $T$ equals $\dim \operatorname{null}(T - \lambda I)^j - \dim \operatorname{null}(T - \lambda I)^{j-1}$, a basis-independent quantity. Hence the multiset of (eigenvalue, block size) pairs is uniquely determined by $T$.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Linear ODEs with explicit polynomial-times-exponential solutions.** Solve $\dot x = A x$ on $\mathbb{R}^n$ where $A$ is a real matrix with complex Jordan blocks. The Jordan form of (the complexification of) $A$ gives the explicit fundamental matrix $e^{tA}$, and the solution corresponding to a Jordan block of size $k$ at eigenvalue $\lambda$ has the form $e^{\lambda t}(p_0 + p_1 t + \cdots + p_{k-1} t^{k-1} / (k-1)!)$. The Jordan form is what *makes the explicit formula explicit*. *See* an exercise like "find the general solution of $\dot x = Ax$ for $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$" — the Jordan block at $2$ of size $2$ gives solutions $e^{2t}(a + b t)$ instead of just $e^{2t}$.

**The Cayley–Hamilton theorem via Jordan form.** The Cayley–Hamilton theorem $p_T(T) = 0$ has a direct proof via Jordan form: for each Jordan block $J_k(\lambda)$, the characteristic polynomial of the full operator includes $(z - \lambda)^{d_\lambda}$ with $d_\lambda \geq k$, so $(J_k(\lambda) - \lambda I)^{d_\lambda} = 0$ (the nilpotent on a $k$-dim space raised to power $\geq k$ is zero), hence the characteristic polynomial applied to the block is zero. Assembling, $p_T(T) = 0$ on each block, hence on all of $V$. The Jordan form makes the theorem a one-line computation.

**Stability of fixed points of dynamical systems.** For a smooth dynamical system $\dot x = f(x)$ with fixed point $x_0$, the Jacobian $A = (Df)_{x_0}$ controls the linearised dynamics. The Jordan form of $A$ determines the qualitative behaviour near $x_0$: eigenvalues with $\operatorname{Re} \lambda < 0$ give exponentially attracting directions, $\operatorname{Re} \lambda > 0$ exponentially repelling, $\operatorname{Re} \lambda = 0$ neutral (with subtleties depending on Jordan block structure). A Jordan block of size $\geq 2$ at $\lambda = 0$ produces a *linear growth* secular term $t \cdot \xi$ in the linearised solution, distinguishing "neutrally stable" (eigenvalues on imaginary axis, all blocks of size $1$) from "neutral with secular instability" (eigenvalues on imaginary axis, some block of size $\geq 2$). The latter is unstable even though all eigenvalues have zero real part.

---

# Bridges

- **[[Thm - Generalized Eigenspace Decomposition|Generalized Eigenspace Decomposition]]** — the input to this theorem. The reduction to the nilpotent case relies entirely on the decomposition.

- **[[Thm - Jordan Normal Form|Jordan Normal Form]] in [[Modules II — §3.3–3.4]]** — the same theorem in module-theoretic guise. Regard $V$ as a $\mathbb{C}[x]$-module via $T$ (see `[[Def - The Module of a Linear Operator]]`). The [[Thm - Primary Decomposition Theorem|primary decomposition]] gives the generalized eigenspace decomposition; the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem for modules over a Euclidean domain]] then decomposes each primary component into cyclic modules $\mathbb{C}[x]/(x - \lambda_k)^{n_{k,i}}$ — these are the Jordan blocks. The module-theoretic proof of the Jordan form does not use the Fitting decomposition or the linear-functional construction explicitly; it just specialises the general module structure theorem. The linear-algebra proof here is more elementary (no module language) but ultimately the same content.

- **[[Thm - Rational Canonical Form|Rational Canonical Form]]** — the analogue of the Jordan form over arbitrary fields. Over a field $k$ that is not algebraically closed, the irreducible factors of the minimal polynomial may not be linear, and the analogue of the Jordan block is the **companion matrix** of an irreducible polynomial. The rational canonical form is the basis-of-cyclic-vectors form valid over any field; over $\mathbb{C}$, it specialises to the Jordan form. The two are different *normal forms* for the same data; one chooses depending on whether the field is algebraically closed.

- **Real Jordan form** — the modification of the Jordan form over $\mathbb{R}$. For a real operator $T$ on $\mathbb{R}^n$, complex-conjugate eigenvalue pairs $a \pm bi$ contribute $2 \times 2$ blocks $\begin{pmatrix} a & b \\ -b & a \end{pmatrix}$ to the real Jordan form, while real eigenvalues contribute ordinary $1 \times 1$ or larger Jordan blocks. The proof goes by complexifying, applying the complex Jordan form, and projecting back to $\mathbb{R}$ in a way that respects the conjugate pairing.

- **Smith normal form** — the row-column reduction algorithm for matrices over a Euclidean domain — see [[Thm - Smith Normal Form]] in [[Modules II — §3.3–3.4]]. Applied to the matrix $xI - T$ over the Euclidean domain $\mathbb{C}[x]$, the Smith normal form yields the invariant factors of the $\mathbb{C}[x]$-module structure on $V$ — equivalently, the Jordan block partition. So Smith normal form is the *algorithmic* route to the Jordan form: it gives an explicit procedure for computing the Jordan blocks from any matrix of $T$. See [[Ex - Computing the Jordan normal form]] for a worked example.

---

# Unlocked by This

> [!tip] Matrix Exponential Closed Form *(from ODE Theory)*
> The matrix exponential $e^{tA}$ has a closed form: bring $A$ to Jordan form $A = C \Lambda C^{-1}$, then $e^{tA} = C e^{t \Lambda} C^{-1}$ where $e^{t \Lambda}$ is block-diagonal with $e^{t J_k(\lambda)}$ on each block. Each $e^{t J_k(\lambda)} = e^{\lambda t} e^{t N_k}$ where $N_k$ is the nilpotent part, a $k \times k$ upper triangular matrix with entries $\frac{t^j}{j!}$ on the $j$-th superdiagonal. So $e^{tA}$ is computable in closed form for any $A$.

> [!tip] Holomorphic Functional Calculus on Matrices *(from Functional Analysis)*
> For any function $f$ holomorphic on a neighbourhood of the spectrum of $A$, $f(A) = C f(\Lambda) C^{-1}$ where $f(\Lambda)$ is block diagonal with $f(J_k(\lambda))$ on each block — a $k \times k$ upper triangular matrix with $f(\lambda), f'(\lambda), \frac{f''(\lambda)}{2!}, \dots$ on the diagonal and successive superdiagonals. This is the matrix incarnation of Cauchy's integral formula.

> [!tip] Similarity Invariants and Conjugacy Classes *(from Lie Theory / Geometric Representation Theory)*
> Two matrices are similar iff their Jordan forms agree, so the **conjugacy classes** in $\mathrm{GL}(V)$ (under the conjugation action $g \cdot x = g x g^{-1}$) are parametrised by Jordan forms. The set of conjugacy classes is a finite union of irreducible algebraic varieties (the **Jordan stratification**), and the closure relations between strata form the geometric foundation of representation theory and the theory of nilpotent orbits in Lie algebras.

> [!tip] Exceptional Points in Non-Hermitian Systems *(from Physics)*
> In a parametrised family of operators $T(\theta)$, points where the Jordan structure degenerates (two distinct eigenvalues coalesce, or two distinct Jordan blocks merge into a larger one) are called **exceptional points**. They are mathematical singularities of the Jordan form viewed as a function of the parameter, and physically they correspond to qualitative changes in the dynamics — for instance, the transition from underdamped to overdamped oscillation, or the formation of resonances in scattering theory.

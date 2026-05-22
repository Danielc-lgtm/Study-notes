---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Subspace"
  - "Def - Sum of Subspaces"
  - "Def - Direct Sum"
  - "Def - Basis"
  - "Def - Dimension"
  - "Thm - Every Linearly Independent List Extends to a Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional vector space over $F$, with subspaces $V_1, V_2 \subseteq V$. Recall $V_1 + V_2 = \{v_1 + v_2 : v_i \in V_i\}$ is the **sum** ([[Def - Sum of Subspaces]]) and $V_1 \cap V_2$ is the intersection. The full notation registry is on [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

---

# Statement

> **Theorem (LADR 2.43, dimension formula).** If $V_1$ and $V_2$ are [[Def - Subspace|subspaces]] of a [[Def - Finite-Dimensional Vector Space|finite-dimensional]] vector space, then
> $$\dim(V_1 + V_2) = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2).$$

> **Corollary (direct sum case, LADR 3.94 / Ex 2C.18).** If $V_1 \cap V_2 = \{0\}$, equivalently if $V_1 + V_2 = V_1 \oplus V_2$, then $\dim(V_1 \oplus V_2) = \dim V_1 + \dim V_2$.

> **Corollary (pigeonhole, Ex 2C.13–15).** If $V_1, V_2$ are subspaces of an $n$-dimensional space with $\dim V_1 + \dim V_2 > n$, then $V_1 \cap V_2 \neq \{0\}$.

---

# Motivation

The formula is the linear-algebra **inclusion-exclusion principle**. For finite sets, $|A \cup B| = |A| + |B| - |A \cap B|$ — the double-counted overlap is subtracted once. For finite-dimensional subspaces, the same accounting holds with **union → sum** and **size → dimension** and **disjoint → trivially intersecting**. The analogy is essentially exact, and the table in LADR pages 47–48 makes it explicit.

The formula matters for two reasons. First, it is the principal computational tool for **dimensions of sums**. Given two subspaces with known dimensions and a known intersection, the dimension of their sum is determined; given the sum and intersection, the dimensions of $V_1$ and $V_2$ are constrained; given dimensions of $V_1, V_2$, and the sum, the dimension of the intersection is determined. In any "two-subspace" problem there are four numbers and one equation: knowing any three forces the fourth.

Second, the formula's **pigeonhole corollary** is the standard route to forcing nontrivial intersection. If $\dim V_1 + \dim V_2 > \dim V$, the formula gives $\dim(V_1 \cap V_2) \geq \dim V_1 + \dim V_2 - \dim V > 0$, so $V_1 \cap V_2$ is nontrivial. This converts a dimension inequality into an existence statement about vectors. It is one of the cleanest applications of the formula and appears repeatedly in exam problems (LADR 2C.11, 13, 14, 15 all use this).

The proof is the constructive one: take a basis of $V_1 \cap V_2$, extend independently to bases of $V_1$ and of $V_2$, and show the concatenated list is a basis of $V_1 + V_2$. The dimension count is then immediate from the lengths.

---

# Sources and Targets

**Sources (Input Broadening).**

The hypothesis is *two subspaces of a finite-dimensional space*. The skill is recognising that any "two-things-meeting" problem in linear algebra is a 2.43 problem in disguise.

A first source is **two given subspaces with known dimensions**. Property $B$: "you have $V_1, V_2$ with $\dim V_1, \dim V_2$ given." The bridge: 2.43 applies directly, and gives $\dim(V_1 + V_2) + \dim(V_1 \cap V_2)$ as a fixed sum. So two of the three quantities ($\dim$ of $V_1 + V_2$, $\dim$ of $V_1 \cap V_2$, $\dim V_1 + \dim V_2$) determine the third.

A second source is **a sum decomposition $V = V_1 + V_2$ given but not promised to be direct**. Property $B$: "$V_1 + V_2 = V$ is hypothesised." The bridge: $\dim(V_1 + V_2) = \dim V$, and 2.43 then determines $\dim(V_1 \cap V_2) = \dim V_1 + \dim V_2 - \dim V$. This is the route by which problems like LADR 2C.12 ("if $\dim U = 3$, $\dim W = 5$, $U + W = \mathbb{R}^8$, then $\mathbb{R}^8 = U \oplus W$") are solved — compute $\dim(U \cap W) = 3 + 5 - 8 = 0$, so the intersection is trivial, so the sum is direct.

A third source is **two subspaces of a space with insufficient total dimension**. Property $B$: "$\dim V_1 + \dim V_2 > \dim V$." The bridge: 2.43 gives $\dim(V_1 \cap V_2) = \dim V_1 + \dim V_2 - \dim(V_1 + V_2) \geq \dim V_1 + \dim V_2 - \dim V > 0$, so the intersection is nontrivial. This is the pigeonhole corollary, and it is the standard route to existence-of-vector results.

A fourth source is **a basis of $V_1 \cap V_2$ and extensions**. Property $B$: "you have an explicit basis of the intersection." The bridge: extend to bases of $V_1$ and of $V_2$ separately; the concatenation is a basis of $V_1 + V_2$. This source is more constructive — it produces an explicit basis of $V_1 + V_2$ rather than just a dimension — and it is the technique behind problems that ask for bases of sums.

**Targets (Output Amplification).**

A first combination is **plus iteration to three subspaces (and a failure)**. Naively iterating 2.43 would suggest $\dim(V_1 + V_2 + V_3) = \sum \dim V_i - \sum \dim(V_i \cap V_j) + \dim(V_1 \cap V_2 \cap V_3)$. This formula is **false** in general — see "Illegal but tempting" #3 on the topic page for the three-lines-in-a-plane counterexample. The correct three-subspace formula has a denominator of 3 (LADR 2C.20) and is comparatively obscure. The non-iterability of inclusion-exclusion for subspaces is a key cautionary tale.

A second combination is **plus the inequality $\dim(V_1 + V_2) \leq \dim V$ for ambient finite-dimensional $V$** gives the pigeonhole result. This is the standard route to "forced intersection" problems. Whenever the *sum* of dimensions exceeds the ambient dimension, the intersection is *forced* to be nontrivial.

A third combination is **plus the direct-sum criterion $V = V_1 \oplus V_2 \iff V = V_1 + V_2$ and $V_1 \cap V_2 = \{0\}$**. The intersection-triviality and sum-totality of the criterion are exactly the two conditions appearing in 2.43, so the formula doubles as a *test for directness* of a sum. Many problems take the form "show the sum is direct" — equivalent to "show the intersection is trivial" — and 2.43 computes the intersection dimension by subtraction.

A fourth combination is **plus 2.32 (basis extension) to assemble bases of $V$ adapted to two subspaces**. Take a basis of $V_1 \cap V_2$, extend to bases of $V_1$ and of $V_2$; the resulting "concatenated" basis of $V_1 + V_2$ can be further extended to a basis of $V$. The result is a basis of $V$ with explicit blocks for $V_1 \cap V_2$, $V_1$, $V_2$, and the rest — useful for arguments about linear maps respecting these subspaces (e.g. the structure of operators on inner product spaces in [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]).

---

# Why Is It True

The intuition is **the formula is an inclusion-exclusion accounting at the level of basis vectors**.

Take a basis of $V_1 \cap V_2$, say $v_1, \ldots, v_m$ where $m = \dim(V_1 \cap V_2)$. This is a linearly independent list in $V_1$ (since $V_1 \cap V_2 \subseteq V_1$), so by [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] it extends to a basis $v_1, \ldots, v_m, u_1, \ldots, u_j$ of $V_1$ — so $\dim V_1 = m + j$. Similarly, the same list $v_1, \ldots, v_m$ is linearly independent in $V_2$, and extends to a basis $v_1, \ldots, v_m, w_1, \ldots, w_k$ of $V_2$ — so $\dim V_2 = m + k$.

Now consider the concatenated list
$$v_1, \ldots, v_m, u_1, \ldots, u_j, w_1, \ldots, w_k.$$
It is contained in $V_1 \cup V_2 \subseteq V_1 + V_2$, and its span contains $V_1$ (which is the span of the first two blocks) and $V_2$ (which is the span of the first and third blocks), so the span equals $V_1 + V_2$. **It spans $V_1 + V_2$.**

The bolded one-liner: **a basis of $V_1 \cap V_2$ extended independently to bases of $V_1$ and $V_2$ glues into a basis of $V_1 + V_2$, with the intersection's basis appearing exactly once on the "joint" side, not twice as in a naive concatenation**.

If the concatenated list of length $m + j + k$ is also linearly independent, then it is a basis of $V_1 + V_2$, and $\dim(V_1 + V_2) = m + j + k$. Substituting $\dim V_1 = m + j$ and $\dim V_2 = m + k$:
$$\dim(V_1 + V_2) = m + j + k = (m + j) + (m + k) - m = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2).$$
The formula falls out.

So the proof's content is **the concatenated list is linearly independent**. This is what the lemma decomposition addresses below. The intuition for *why* it is independent: a vanishing combination $\sum a_i v_i + \sum b_j u_j + \sum c_l w_l = 0$ must, after rearranging, equate a $V_2$-vector with a $V_1$-vector, putting it in $V_1 \cap V_2$, where it has a unique expansion in the $v$'s alone. The $w$'s have coefficients in this expansion, but they are not in the $V_1 \cap V_2$-basis $v_1, \ldots, v_m$, so their coefficients $c_l$ must vanish. Then the remaining combination is just $\sum a_i v_i + \sum b_j u_j = 0$ in $V_1$, which is the basis of $V_1$ — so $a_i = b_j = 0$.

The result is a beautiful exact accounting: the intersection $V_1 \cap V_2$ is "shared" by the bases of $V_1$ and $V_2$, and the dimension of the sum corrects for the double-count.

---

# What Makes This Hard

The hardest step in the proof is **showing the concatenated list is linearly independent**. The argument goes through the linear dependence and uses uniqueness of expansion in the basis of $V_1$ — a slightly tricky manipulation. Students sometimes try to prove independence by direct manipulation of the coefficients and get tangled; the cleaner argument is the *bilateral* one: a vanishing combination is decomposed into $V_1$ and $V_2$ parts, both of which must individually vanish.

A second common error is to **forget that the same basis $v_1, \ldots, v_m$ of the intersection is used in both extensions**. If you extend the basis of $V_1 \cap V_2$ to $V_1$ using one ordering and to $V_2$ using a different basis of $V_1 \cap V_2$, the concatenation argument breaks. The basis of $V_1 \cap V_2$ must be *fixed* and reused.

A third error is to **misremember the formula's sign**. It is $\dim(V_1 + V_2) = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$, with the intersection **subtracted**. The mnemonic: in inclusion-exclusion for sets, $|A \cup B| < |A| + |B|$ when there is overlap, so the overlap is subtracted; same for subspaces.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:** Build a basis of $V_1 + V_2$ explicitly: start with a basis of $V_1 \cap V_2$, extend to a basis of $V_1$ and (using the same intersection basis) extend to a basis of $V_2$. The concatenated list — the intersection basis, then the $V_1$-extension, then the $V_2$-extension — is a basis of $V_1 + V_2$. Its length is $m + j + k = \dim V_1 + \dim V_2 - m = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$.

**Subgoal decomposition:**

1. **Fix a basis of $V_1 \cap V_2$, say $v_1, \ldots, v_m$ of length $m = \dim(V_1 \cap V_2)$.**
   - *Hint:* The intersection is a subspace of the finite-dimensional ambient, hence finite-dimensional by [[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|2.25]], hence has a basis.
   - *Why needed:* This basis is the "shared" portion of the two extensions.

2. **Extend $v_1, \ldots, v_m$ to a basis $v_1, \ldots, v_m, u_1, \ldots, u_j$ of $V_1$.**
   - *Hint:* The original list is independent in $V_1$ (it is a basis of a subspace of $V_1$), so [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] applies.
   - *Why needed:* This gives $\dim V_1 = m + j$.

3. **Extend $v_1, \ldots, v_m$ to a basis $v_1, \ldots, v_m, w_1, \ldots, w_k$ of $V_2$.**
   - *Hint:* Same argument as step 2, applied to $V_2$.
   - *Why needed:* This gives $\dim V_2 = m + k$.

4. **Show the concatenated list $v_1, \ldots, v_m, u_1, \ldots, u_j, w_1, \ldots, w_k$ spans $V_1 + V_2$.**
   - *Hint:* The span contains both $V_1$ (first two blocks) and $V_2$ (first and third), so contains their sum.
   - *Why needed:* Part of "basis = spans + independent".

5. **Show the concatenated list is linearly independent.** A vanishing combination $\sum a_i v_i + \sum b_j u_j + \sum c_l w_l = 0$ reorganises as $\sum c_l w_l = -\sum a_i v_i - \sum b_j u_j \in V_1$ (because the right side is in $V_1$'s basis). The left side is in $V_2$, so this common element is in $V_1 \cap V_2$. But $\sum c_l w_l$, viewed as a vector in $V_1 \cap V_2$, must also be expressible in the basis $v_1, \ldots, v_m$ of $V_1 \cap V_2$. Using uniqueness of expansion in the basis $v_1, \ldots, v_m, w_1, \ldots, w_k$ of $V_2$, all $c_l = 0$. Then $\sum a_i v_i + \sum b_j u_j = 0$ in $V_1$, and since $v_1, \ldots, v_m, u_1, \ldots, u_j$ is a basis of $V_1$, all $a_i = 0$ and $b_j = 0$.
   - *Hint:* Decompose the vanishing combination across $V_1$ and $V_2$.
   - *Why needed:* The other half of "basis = spans + independent".

6. **Count.** The basis has length $m + j + k$, so $\dim(V_1 + V_2) = m + j + k = (m + j) + (m + k) - m = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The intersection $V_1 \cap V_2$ is a finite-dimensional subspace
> **Statement:** If $V$ is finite-dimensional and $V_1, V_2$ are subspaces of $V$, then $V_1 \cap V_2$ is also a subspace of $V$ (in particular of $V_1$ and of $V_2$), and is finite-dimensional.
>
> **Hint:** Intersection of subspaces is a subspace. Subspaces of a finite-dimensional space are finite-dimensional ([[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|2.25]]).
>
> **Why needed:** The proof of the dimension formula starts by fixing a basis of $V_1 \cap V_2$, which requires this lemma to know such a basis exists.
>
> > [!note]- Full proof
> > *Subspace.* $0 \in V_1$ and $0 \in V_2$, so $0 \in V_1 \cap V_2$. If $u, v \in V_1 \cap V_2$, then $u, v \in V_1$ so $u + v \in V_1$ (closure of $V_1$); similarly $u + v \in V_2$; so $u + v \in V_1 \cap V_2$. For scalar multiplication: if $v \in V_1 \cap V_2$ and $\lambda \in F$, then $\lambda v \in V_1$ and $\lambda v \in V_2$, hence $\lambda v \in V_1 \cap V_2$. So $V_1 \cap V_2$ is a subspace.
> >
> > *Finite-dimensional.* By [[Thm - Subspace of Finite-Dimensional Space is Finite-Dimensional|LADR 2.25]], every subspace of a finite-dimensional space is finite-dimensional.

> [!note]- Lemma 2: A linearly independent list in a sub-subspace remains linearly independent in the ambient
> **Statement:** If $W \subseteq U \subseteq V$ are nested subspaces and $v_1, \ldots, v_m$ is a linearly independent list in $W$, then it is also linearly independent in $U$ and in $V$.
>
> **Hint:** Linear independence is a property of the list, not of the ambient space.
>
> **Why needed:** This is what lets us extend a basis of $V_1 \cap V_2$ to a basis of $V_1$ (via 2.32 applied within $V_1$): the basis of $V_1 \cap V_2$ remains independent when viewed as a list in $V_1$.
>
> > [!note]- Full proof
> > Linear independence is defined by the condition "only the trivial vanishing combination". This condition is on the combination — $a_1 v_1 + \cdots + a_m v_m = 0_W$ — but $0_W = 0_U = 0_V$ (subspaces share the zero vector), and the combination's result lies in the smaller subspace if and only if it lies in the larger one. So a non-trivial vanishing combination in any one of $W, U, V$ is a non-trivial vanishing combination in all three. Hence independence is preserved.

> [!note]- Lemma 3: A vanishing combination decomposes across $V_1$ and $V_2$
> **Statement:** Suppose $v_1, \ldots, v_m$ is a basis of $V_1 \cap V_2$, $v_1, \ldots, v_m, u_1, \ldots, u_j$ is a basis of $V_1$, and $v_1, \ldots, v_m, w_1, \ldots, w_k$ is a basis of $V_2$. If $\sum a_i v_i + \sum b_j u_j + \sum c_l w_l = 0$ in $V$, then all $a_i = b_j = c_l = 0$.
>
> **Hint:** Move the $w$-terms to the right side: $\sum c_l w_l = -\sum a_i v_i - \sum b_j u_j$. The right side lies in $V_1$ (since $v_i \in V_1, u_j \in V_1$), and the left side lies in $V_2$. So the common element is in $V_1 \cap V_2$.
>
> **Why needed:** This is the linear-independence half of "concatenated list is a basis of $V_1 + V_2$".
>
> > [!note]- Full proof
> > Let $z = \sum c_l w_l = -\sum a_i v_i - \sum b_j u_j$.
> >
> > The right form shows $z \in V_1$ (since it is a combination of basis vectors of $V_1$). The left form shows $z \in V_2$ (since it is a combination of basis vectors of $V_2$). So $z \in V_1 \cap V_2$.
> >
> > Since $v_1, \ldots, v_m$ is a basis of $V_1 \cap V_2$, $z = \sum d_l v_l$ for some scalars $d_l$. But $z$ is also expressed in the basis $v_1, \ldots, v_m, w_1, \ldots, w_k$ of $V_2$ as $\sum c_l w_l$ (no $v$-coefficients in this expansion). Two expansions of the same vector in the basis of $V_2$ — one with $w$-coefficients $c_l$ and zero $v$-coefficients, the other with $v$-coefficients $d_l$ and zero $w$-coefficients — must agree, so by uniqueness of expansion, all $c_l = 0$ (and all $d_l = 0$).
> >
> > Hence $\sum c_l w_l = 0$, and the original equation reduces to $\sum a_i v_i + \sum b_j u_j = 0$ in $V_1$. Since $v_1, \ldots, v_m, u_1, \ldots, u_j$ is a basis of $V_1$, all $a_i = 0$ and all $b_j = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $V$ be finite-dimensional and $V_1, V_2 \subseteq V$ subspaces. Then $\dim(V_1 + V_2) = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$.
>
> *Proof.* By Lemma 1, $V_1 \cap V_2$ is a finite-dimensional subspace; let $v_1, \ldots, v_m$ be a basis of it, where $m = \dim(V_1 \cap V_2)$.
>
> By Lemma 2, $v_1, \ldots, v_m$ is linearly independent in $V_1$. By [[Thm - Every Linearly Independent List Extends to a Basis|LADR 2.32]] applied within $V_1$, it extends to a basis $v_1, \ldots, v_m, u_1, \ldots, u_j$ of $V_1$, where $\dim V_1 = m + j$.
>
> Similarly, $v_1, \ldots, v_m$ extends to a basis $v_1, \ldots, v_m, w_1, \ldots, w_k$ of $V_2$, where $\dim V_2 = m + k$.
>
> Consider the concatenated list $L = v_1, \ldots, v_m, u_1, \ldots, u_j, w_1, \ldots, w_k$ of length $m + j + k$.
>
> *$L$ spans $V_1 + V_2$.* Every vector $z \in V_1 + V_2$ has the form $z = z_1 + z_2$ with $z_i \in V_i$. Writing $z_1 = \sum a_i v_i + \sum b_j u_j$ in the basis of $V_1$ and $z_2 = \sum a'_i v_i + \sum c_l w_l$ in the basis of $V_2$, we have
> $$z = \sum (a_i + a'_i) v_i + \sum b_j u_j + \sum c_l w_l,$$
> which is a linear combination of $L$. So $\operatorname{span}(L) \supseteq V_1 + V_2$. The reverse inclusion is immediate (each vector of $L$ is in $V_1$ or $V_2$).
>
> *$L$ is linearly independent.* By Lemma 3, the only vanishing combination of $L$ is the trivial one.
>
> Hence $L$ is a basis of $V_1 + V_2$, and
> $$\dim(V_1 + V_2) = |L| = m + j + k = (m + j) + (m + k) - m = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2). \qquad\blacksquare$$
>
> **Corollary (direct sum case).** If $V_1 \cap V_2 = \{0\}$, then $\dim(V_1 \oplus V_2) = \dim V_1 + \dim V_2$. *Proof:* $\dim(V_1 \cap V_2) = \dim \{0\} = 0$, so the correction term vanishes. $\qquad\blacksquare$
>
> **Corollary (pigeonhole).** If $V_1, V_2 \subseteq V$ with $\dim V$ finite and $\dim V_1 + \dim V_2 > \dim V$, then $V_1 \cap V_2 \neq \{0\}$. *Proof:* $\dim(V_1 + V_2) \leq \dim V$ since $V_1 + V_2 \subseteq V$ (apply [[Def - Dimension|the subspace-dimension corollary]]). So $\dim(V_1 \cap V_2) = \dim V_1 + \dim V_2 - \dim(V_1 + V_2) \geq \dim V_1 + \dim V_2 - \dim V > 0$, hence $V_1 \cap V_2$ is nonzero. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Finite set theory: classical inclusion-exclusion.** The formula $|A \cup B| = |A| + |B| - |A \cap B|$ for finite sets is the set-theoretic analogue of 2.43. Both are special cases of inclusion-exclusion for modular lattices (subspace lattices and subset lattices), and both have the same proof structure: count the "shared" part once instead of twice. The deeper unification is that modular lattices admit a Möbius function, and inclusion-exclusion is its first-order use.

**Combinatorics: Hall's theorem and bipartite matching.** The pigeonhole corollary of 2.43 (dimensions summing to too much force intersection) has a combinatorial analogue: in a bipartite graph, if the total "degree" on one side exceeds the size of the other side, some vertex is overloaded — and this drives the proof of Hall's marriage theorem. The structural similarity is exact when one passes to matroid theory: 2.43 is the rank function of the union/intersection lattice for vector matroids.

**Topology: Mayer-Vietoris exact sequence.** In algebraic topology, the Mayer-Vietoris sequence relates the homology of a union $X = U \cup V$ to the homology of $U$, $V$, and $U \cap V$. The long exact sequence implies, in particular, the inclusion-exclusion equality $\dim H_n(X) = \dim H_n(U) + \dim H_n(V) - \dim H_n(U \cap V)$ when the relevant maps are surjective. Linear algebra inclusion-exclusion 2.43 is the *abelian-category* model on which the topological version is built.

**Probability: covariance and the law of total variance.** For two random variables $X, Y$ on a finite probability space, viewed as elements of the function space $\mathcal{F}(\Omega)$, the inner product is the covariance, and orthogonal decomposition gives a variance-decomposition law: $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2 \operatorname{Cov}(X, Y)$. This is a quadratic analogue of 2.43: the dimension of the joint variation decomposes into the parts attributable to each variable plus the overlap.

---

# Bridges

- **[[Thm - Every Linearly Independent List Extends to a Basis]]** — the proof of 2.43 uses 2.32 essentially: extending a basis of $V_1 \cap V_2$ to bases of $V_1$ and $V_2$ separately. Without 2.32 the proof would have to choose bases independently and reconcile them.

- **[[Def - Direct Sum|Direct sum]]** — 2.43 specialises to the direct-sum case $\dim(V_1 \oplus V_2) = \dim V_1 + \dim V_2$ when the intersection is trivial. The direct-sum decomposition is *dimension-additive*; the general sum carries a correction term equal to the dimension of the intersection. So 2.43 doubles as a test for directness — a sum is direct iff dimensions add cleanly without correction.

- **Inclusion-exclusion principle** — for finite sets, $|A \cup B| = |A| + |B| - |A \cap B|$, the cardinality counterpart of 2.43. The deeper unification — both being instances of inclusion-exclusion on a modular lattice — is what justifies calling 2.43 "the linear algebra inclusion-exclusion".

- **Rank-nullity (LADR 3.21, [[Linear Algebra III — §3A–D Linear Maps]])** — for a linear map $T : V \to W$, $\dim V = \dim \ker T + \dim \operatorname{range} T$. This is *not* an instance of 2.43, but it is a related dimension-accounting result. The relationship: rank-nullity is for kernels and ranges (which need not be in the same space), while 2.43 is for two subspaces of one ambient space. Both are key counting tools in linear algebra.

- **Mayer-Vietoris / spectral sequences** — in homological algebra, the long exact sequence relating homology of a union to homology of the pieces is the linearisation of 2.43 to the world of chain complexes. When the connecting maps are surjective, the long exact sequence implies inclusion-exclusion at the level of dimensions of homology groups. So 2.43 is the abelian-category model for a vast machinery of long exact sequences in topology and algebra.

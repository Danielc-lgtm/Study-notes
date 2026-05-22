---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Dual Space"
  - "Def - Dual Basis"
  - "Def - Basis"
  - "Def - Dimension"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional vector space over $\mathbb{F}$ with basis $v_1, \dots, v_n$. Let $\varphi_1, \dots, \varphi_n \in V'$ be the [[Def - Dual Basis|dual basis]], defined by $\varphi_j(v_k) = \delta_{jk}$.

Prove that $\varphi_1, \dots, \varphi_n$ is a basis of $V'$, and conclude that
$$\dim V' = \dim V.$$

**Recall:**

A [[Def - Linear Map|linear functional]] on $V$ is a linear map $V \to \mathbb{F}$, where $\mathbb{F}$ is the field of scalars viewed as a one-dimensional vector space. The [[Def - Dual Space|dual space]] is $V' = \mathcal{L}(V, \mathbb{F})$, the vector space of all linear functionals.

![[Def - Dual Basis#The Definition]]

A [[Def - Basis|basis]] of a vector space is a linearly independent spanning list.

The **Kronecker delta** is $\delta_{jk} = 1$ if $j = k$ and $\delta_{jk} = 0$ if $j \neq k$.

---

# Convergent Strategy

**Problem class.** This is the *foundational dimension theorem* for the dual space, and it provides an explicit basis along with the proof of dimensionality. As mentioned in the [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Problem-Solving Strategy|topic page]], dimension computation is one of the recurring targets, and the dual-dimension equality is the input to almost every other theorem in §3F.

**Assumption pattern.** The recognisable signal is "a basis of $V$ is given, find a basis of $V'$". The dual basis is the natural candidate by virtue of its construction — biorthogonal to the basis of $V$. The verification has two parts: linear independence (which uses biorthogonality directly) and spanning (which uses biorthogonality to identify coefficients in a general expansion).

**Theorem routing.** The route has three steps:
- *Existence of dual basis* via the [[Def - Linear Map|linear-map extension lemma]]: a linear map is determined by its values on a basis.
- *Linear independence*: apply a vanishing linear combination to each basis vector $v_k$, use biorthogonality to extract one coefficient.
- *Spanning*: for any $\psi \in V'$, observe that $\sum_j \psi(v_j) \varphi_j$ agrees with $\psi$ on each basis vector $v_k$, and linear functionals agreeing on a basis are equal.

The conclusion $\dim V' = \dim V$ then follows by counting: the basis has $n$ elements.

**Key decision point.** The non-obvious move is the *expansion formula* $\psi = \sum_j \psi(v_j) \varphi_j$. Many students try to prove spanning by some basis-extension or dimension-counting argument; the right move is to write down the expansion directly. The formula is forced by biorthogonality and works because two linear functionals equal on a basis are equal everywhere.

---

# Legal Operations Used

From [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Legal Operations|the topic page]]:

1. **Use the dual basis to read off coordinates** (operation 5). The proof uses the dual basis structurally; the spanning step writes $\psi$ as a linear combination of dual-basis elements, using the values $\psi(v_k)$ as coordinates.

2. **Build a linear functional** (operation 4), instance: define each $\varphi_j$ via its prescribed values on the basis $v_1, \dots, v_n$.

---

# Hints

> [!note]- Hint 1
> The dual basis $\varphi_j$ is defined by $\varphi_j(v_k) = \delta_{jk}$. To check linear independence of $\varphi_1, \dots, \varphi_n$: suppose $\sum_j a_j \varphi_j = 0$ in $V'$. Apply both sides to the basis vector $v_k$ — what does biorthogonality give you?

> [!note]- Hint 2
> For spanning: given an arbitrary functional $\psi \in V'$, consider the functional $\sum_j \psi(v_j) \varphi_j$. What does this functional take to $v_k$? Compare with $\psi(v_k)$.

> [!note]- Hint 3
> Two linear functionals that agree on a basis are equal. Why? Any vector $v \in V$ is a linear combination $v = \sum c_k v_k$, and by linearity $\varphi(v) = \sum c_k \varphi(v_k) = \sum c_k \psi(v_k) = \psi(v)$ if $\varphi(v_k) = \psi(v_k)$ for all $k$.

---

# Solution

The proof has three steps. Step 1 invokes the linear-map extension lemma to show the dual basis exists. Step 2 verifies linear independence using biorthogonality. Step 3 verifies spanning by writing an explicit linear combination. The non-obvious move is in Step 3, where the formula $\psi = \sum_j \psi(v_j) \varphi_j$ is the natural expansion that biorthogonality forces.

**Step 1: The dual basis exists.**

By the [[Def - Linear Map|linear-map extension lemma]], for each $j$ there is a unique linear functional $\varphi_j \in V'$ with $\varphi_j(v_k) = \delta_{jk}$.

> [!note]- Derivation
> The linear-map extension lemma says: given a basis $v_1, \dots, v_n$ of $V$ and any list of values $a_1, \dots, a_n \in W$, there is a unique linear map $T : V \to W$ with $T(v_k) = a_k$ for each $k$. Apply this to $W = \mathbb{F}$ and the values $(0, \dots, 0, 1, 0, \dots, 0)$ with $1$ in position $j$: there is a unique linear map $\varphi_j : V \to \mathbb{F}$ with $\varphi_j(v_k) = \delta_{jk}$. The list $\varphi_1, \dots, \varphi_n$ is well-defined.

**Step 2: $\varphi_1, \dots, \varphi_n$ is linearly independent in $V'$.**

A vanishing linear combination $\sum_j a_j \varphi_j = 0$ forces all $a_j = 0$.

> [!note]- Derivation
> Suppose $a_1 \varphi_1 + \cdots + a_n \varphi_n = 0$ in $V'$, where $a_1, \dots, a_n \in \mathbb{F}$. The zero of $V'$ is the zero functional, which sends every vector to $0$.
>
> Apply both sides to the basis vector $v_k$ (for any fixed $k$):
> $$(a_1 \varphi_1 + \cdots + a_n \varphi_n)(v_k) = a_1 \varphi_1(v_k) + a_2 \varphi_2(v_k) + \cdots + a_n \varphi_n(v_k) = a_k,$$
> using $\varphi_j(v_k) = \delta_{jk}$ (the sum collapses to the single nonzero term, $j = k$).
>
> The right-hand side is $0(v_k) = 0$. So $a_k = 0$ for every $k \in \{1, \dots, n\}$. Hence all coefficients vanish, and $\varphi_1, \dots, \varphi_n$ is linearly independent.

**Step 3: $\varphi_1, \dots, \varphi_n$ spans $V'$.**

Every $\psi \in V'$ has the expansion $\psi = \sum_{j=1}^n \psi(v_j) \varphi_j$.

> [!note]- Derivation
> Let $\psi \in V'$ be an arbitrary linear functional on $V$. Define the candidate expansion
> $$\tilde \psi := \psi(v_1) \varphi_1 + \psi(v_2) \varphi_2 + \cdots + \psi(v_n) \varphi_n \in V',$$
> a linear combination of $\varphi_1, \dots, \varphi_n$ with the scalars $\psi(v_j)$ as coefficients.
>
> *Claim: $\tilde \psi = \psi$.* To prove this, it suffices to show $\tilde \psi$ and $\psi$ agree on each basis vector $v_k$ (since two linear functionals agreeing on a basis are equal — applied to a generic vector $\sum c_k v_k$, both give the same answer by linearity). Compute:
> $$\tilde \psi(v_k) = \sum_{j=1}^n \psi(v_j) \varphi_j(v_k) = \sum_{j=1}^n \psi(v_j) \delta_{jk} = \psi(v_k),$$
> using biorthogonality (the only nonzero term is $j = k$). So $\tilde \psi(v_k) = \psi(v_k)$ for every $k$.
>
> Therefore $\tilde \psi = \psi$ as linear functionals, i.e. $\psi$ is a linear combination of $\varphi_1, \dots, \varphi_n$ with coefficients $\psi(v_1), \dots, \psi(v_n)$. Since $\psi$ was arbitrary, $\varphi_1, \dots, \varphi_n$ spans $V'$.

**Step 4: $\dim V' = \dim V$.**

The list $\varphi_1, \dots, \varphi_n$ is linearly independent (Step 2) and spans (Step 3), so it is a basis of $V'$. It has $n$ elements, hence $\dim V' = n = \dim V$. $\blacksquare$

> [!note]- Complete formal solution
> Let $V$ be a finite-dimensional vector space with basis $v_1, \dots, v_n$, and let $\varphi_1, \dots, \varphi_n$ be defined by $\varphi_j(v_k) = \delta_{jk}$ via the linear-map extension lemma.
>
> *Linear independence.* Suppose $a_1 \varphi_1 + \cdots + a_n \varphi_n = 0$. Applying both sides to $v_k$:
> $$0 = a_1 \varphi_1(v_k) + \cdots + a_n \varphi_n(v_k) = a_k.$$
> So $a_k = 0$ for all $k$.
>
> *Spanning.* For arbitrary $\psi \in V'$, set $\tilde \psi := \sum_{j=1}^n \psi(v_j) \varphi_j$. For each $k$:
> $$\tilde \psi(v_k) = \sum_{j=1}^n \psi(v_j) \varphi_j(v_k) = \sum_j \psi(v_j) \delta_{jk} = \psi(v_k).$$
> Since $\tilde \psi$ and $\psi$ agree on the basis $v_1, \dots, v_n$, they are equal as linear functionals. So $\psi = \tilde \psi$ is in the span of $\varphi_1, \dots, \varphi_n$.
>
> *Conclusion.* $\varphi_1, \dots, \varphi_n$ is a basis of $V'$ of length $n$, so $\dim V' = n = \dim V$. $\blacksquare$

> [!note]- Sanity check via the formula $\dim \mathcal{L}(V, W) = (\dim V)(\dim W)$
> An alternative one-line proof: $\dim V' = \dim \mathcal{L}(V, \mathbb{F}) = (\dim V)(\dim \mathbb{F}) = (\dim V)(1) = \dim V$. This is faster but does not produce an explicit basis, so the constructive proof above is preferable when a basis is needed (which is the typical use case).

---

# Key Takeaways

**Biorthogonality is the engine of the dual basis.** The defining property $\varphi_j(v_k) = \delta_{jk}$ does *all* the work in the proof: it collapses sums in both directions (in linear independence and in spanning), it is the source of the coordinate-extraction formula, and it is the structural identity used in every subsequent dual-basis computation. Whenever you need to compute a dual-basis quantity, look for the move that lets biorthogonality collapse a sum. This is the same move that appears in:
- *Inner products* with orthonormal bases: $\langle v_j, v_k \rangle = \delta_{jk}$ collapses sums similarly.
- *Dirac delta functions* in functional analysis: $\delta(x - y) \cdot f(y)$ integrated over $y$ gives $f(x)$ — the continuous version of biorthogonality.
- *Cofactor expansions* of determinants: the cofactor matrix is essentially the dual basis to the column vectors of a matrix.

In each setting, the recognition trigger is *"this would collapse if I had a biorthogonal pair"* — and you should reach for the appropriate pair.

**Linear functionals agreeing on a basis are equal — the basis spans, so the functional is determined.** This is the dual face of the statement that *vectors with the same coordinates are equal*. The proof uses linearity: any $v$ is $\sum c_k v_k$, and $\varphi(v) = \sum c_k \varphi(v_k) = \sum c_k \psi(v_k) = \psi(v)$ when $\varphi$ and $\psi$ agree on the basis. The same template proves uniqueness of any linear quantity defined on a basis: the trace, the determinant (as the unique alternating multilinear form $\det(I) = 1$), the characteristic polynomial. *A linear quantity is determined by its values on a basis*, and "agreeing on a basis $\Rightarrow$ equal" is the formal statement.

**The dimension formula $\dim V' = \dim V$ is what makes finite-dimensional duality work.** Many of the theorems in §3F — the annihilator dimension formula, the rank equality of $T$ and $T'$, the natural isomorphism $V \cong V''$ — depend on the dimension equality holding. In infinite dimensions, where the equality fails (the algebraic dual of an infinite-dimensional space is generally *strictly larger* than the original), the theory of dual spaces becomes much subtler and requires topological hypotheses (continuity of functionals, Hahn-Banach). The Hahn-Banach theorem is essentially the analytic replacement for the existence of dual bases in finite dimensions. Recognising this structural role of the dimension equality helps you understand why finite-dimensional dual spaces are *easy* and infinite-dimensional ones are *hard*.

**The coordinate-extraction formula $v = \sum \varphi_j(v) v_j$ is the universal "expand in this basis" identity.** Once $\varphi_j$ is defined, the formula $v = \sum_j \varphi_j(v) v_j$ holds for every $v$ — and the proof is one line: both sides agree when paired with each $\varphi_k$ via biorthogonality. This formula will be reused constantly throughout the chapter (and beyond) whenever you need to expand a vector in coordinates. The dual identity $\psi = \sum_j \psi(v_j) \varphi_j$, proved in Step 3, is the same formula on the dual side: a linear functional is expanded in the dual basis with the values $\psi(v_j)$ as coefficients.

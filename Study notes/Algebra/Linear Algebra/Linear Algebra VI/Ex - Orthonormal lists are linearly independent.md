---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Orthogonal and Orthonormal Vectors"
  - "Def - Linear Independence"
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be an inner product space over $\mathbf{F}$. Show that every **orthonormal list** $e_1, \dots, e_m$ in $V$ is **linearly independent**.

**Recall:**

A list $v_1, \dots, v_m$ is **linearly independent** if the only solution to $a_1 v_1 + \cdots + a_m v_m = 0$ is $a_1 = \cdots = a_m = 0$.

![[Def - Orthogonal and Orthonormal Vectors#The Definition]]

The key feature of orthonormality: $\langle e_j, e_k\rangle = \delta_{jk}$ (the Kronecker delta), equal to $1$ when $j = k$ and $0$ when $j \neq k$.

---

# Convergent Strategy

**Problem class.** This is a *prove linear independence* problem — the simplest pattern in the chapter. The strategy is to assume a vanishing linear combination and extract each coefficient using the orthonormal structure.

**Assumption pattern.** The hypothesis is that the list is orthonormal: pairwise orthogonal, each of unit norm. Two distinct vectors have inner product $0$; each vector has inner product $1$ with itself. This is precisely the structure that lets us *extract* a coefficient by taking the inner product with a fixed vector.

**Theorem routing.** The route is direct: assume $\sum_k a_k e_k = 0$, take the inner product of both sides with $e_j$ for each $j$, and use orthonormality to read off $a_j = 0$. No named theorem is invoked beyond the definition of orthonormality and the linearity of the inner product.

**Key decision point.** Which auxiliary vector to take the inner product with. The answer is forced by the orthonormal structure: taking the inner product with $e_j$ exploits orthogonality (other terms vanish) and unit-norm (the $j$-th term gives $a_j \cdot 1 = a_j$). Any other choice loses the cleanness.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VI — §6 Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Take the inner product with a basis vector to extract a coefficient** (operation 6). The proof is essentially this operation: assume $\sum_k a_k e_k = 0$, take $\langle\cdot, e_j\rangle$ of both sides, and read off $a_j = 0$ thanks to orthonormality.

2. **Expand $\|\alpha u + \beta v\|^2$ using sesquilinearity** (operation 1), in the alternative proof via the squared-norm formula $\|\sum a_k e_k\|^2 = \sum |a_k|^2$.

---

# Hints

> [!note]- Hint 1
> Suppose $a_1 e_1 + \cdots + a_m e_m = 0$. To extract a single coefficient, take the inner product of both sides with one specific $e_j$ and see what happens to the other terms.

> [!note]- Hint 2
> $\langle a_1 e_1 + \cdots + a_m e_m, e_j\rangle = \sum_k a_k \langle e_k, e_j\rangle$. By orthonormality, $\langle e_k, e_j\rangle = \delta_{kj}$, so only the $k = j$ term survives, giving $a_j$.

> [!note]- Hint 3
> The right-hand side is $\langle 0, e_j\rangle = 0$. So $a_j = 0$ for each $j$. Since $j$ was arbitrary, all coefficients are zero.

---

# Solution

The strategy is to take the inner product with each $e_j$ in turn and use orthonormality to extract the corresponding coefficient.

**Plan:** Assume a vanishing linear combination $\sum_k a_k e_k = 0$. Take the inner product of both sides with $e_j$ for arbitrary $j$. The left-hand side simplifies to $a_j$ (only the $k = j$ term survives, with $\langle e_j, e_j\rangle = 1$); the right-hand side is $0$. Hence $a_j = 0$ for all $j$.

**Step 1: Take the inner product with $e_j$.**

Fix $j \in \{1, \dots, m\}$. Apply $\langle\cdot, e_j\rangle$ to both sides of $a_1 e_1 + \cdots + a_m e_m = 0$.

> [!note]- Derivation
> By linearity of the inner product in the first slot,
> $$\langle a_1 e_1 + \cdots + a_m e_m, e_j\rangle = \sum_{k=1}^m a_k \langle e_k, e_j\rangle.$$
> By orthonormality, $\langle e_k, e_j\rangle = \delta_{kj}$, which is $1$ if $k = j$ and $0$ otherwise. So all terms with $k \neq j$ vanish, and only the $k = j$ term contributes:
> $$\sum_{k=1}^m a_k \langle e_k, e_j\rangle = a_j \cdot 1 = a_j.$$
>
> The right-hand side is $\langle 0, e_j\rangle = 0$ (the inner product with the zero vector is always zero).

**Step 2: Conclude $a_j = 0$ for each $j$, hence all coefficients are zero.**

From Step 1, $a_j = 0$ for the arbitrary $j$. Since $j$ ranges over $\{1, \dots, m\}$, all coefficients are zero.

> [!note]- Derivation
> Step 1 gave $a_j = 0$. Since $j$ was arbitrary, this holds for each $j \in \{1, \dots, m\}$. Hence $a_1 = a_2 = \cdots = a_m = 0$, which is the defining condition of linear independence.

> [!note]- Complete formal solution
> Suppose $a_1 e_1 + \cdots + a_m e_m = 0$ for some $a_1, \dots, a_m \in \mathbf{F}$.
>
> Fix $j \in \{1, \dots, m\}$. Taking the inner product with $e_j$:
> $$\left\langle \sum_{k=1}^m a_k e_k, e_j\right\rangle = \sum_{k=1}^m a_k \langle e_k, e_j\rangle = \sum_{k=1}^m a_k \delta_{kj} = a_j,$$
> using orthonormality $\langle e_k, e_j\rangle = \delta_{kj}$ at the second equality. On the other side, $\langle 0, e_j\rangle = 0$.
>
> Hence $a_j = 0$. Since $j$ was arbitrary, $a_1 = \cdots = a_m = 0$. This shows $e_1, \dots, e_m$ is linearly independent. $\blacksquare$

> [!note]- Alternative proof via the norm formula
> *Proof.* If $\sum_k a_k e_k = 0$, then $\|\sum_k a_k e_k\|^2 = 0$. By the orthonormal-list norm formula (corollary of the [[Thm - Pythagorean Theorem|Pythagorean theorem]]: see [[Def - Orthogonal and Orthonormal Vectors]]),
> $$\left\|\sum_{k=1}^m a_k e_k\right\|^2 = \sum_{k=1}^m |a_k|^2.$$
> Hence $\sum_k |a_k|^2 = 0$. A sum of non-negative reals equals zero iff each is zero, so $|a_k|^2 = 0$ for each $k$, hence $a_k = 0$. $\blacksquare$

---

# Key Takeaways

**Orthonormality is "linear independence with extras".** Every orthonormal list is linearly independent (this exercise), but the converse is false: linearly independent lists need not be orthogonal, let alone orthonormal. The relationship is: orthonormal ⟹ orthogonal ⟹ linearly independent (for nonzero vectors). Orthonormality is the strongest property, capturing not only "no redundancy" (linear independence) but also "pairwise perpendicular with unit length" (orthonormality). This is why orthonormal bases are the gold-standard computational tool: every nice property of bases (existence, expansion coefficients, spanning) holds, and the orthonormality adds clean inner-product structure on top. The transferable lesson: when you have an orthonormal list, you automatically have linear independence — no separate check needed.

**Taking the inner product with a basis vector is the orthonormal-extraction technique.** The proof above is the cleanest illustration of a recurring pattern: in an orthonormal basis, expansion coefficients are inner products. To extract $a_j$ from $v = \sum_k a_k e_k$, compute $\langle v, e_j\rangle = a_j$. The same pattern gives the Fourier-coefficient formula $c_n = \langle f, e^{inx}/\sqrt{2\pi}\rangle$ in $L^2[-\pi, \pi]$, the expansion-coefficient formula for any orthonormal basis, and the explicit form of the [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation]] $v = \sum_k \overline{\varphi(e_k)} e_k$. The triggers are: "I have an orthonormal list" + "I want a specific coefficient" → "take the inner product with the appropriate basis vector".

**The alternative proof via the norm formula is the "global" version of the same idea.** Rather than extracting coefficients one at a time, the norm formula $\|\sum a_k e_k\|^2 = \sum |a_k|^2$ extracts all coefficients simultaneously: a sum of non-negative reals is zero iff each is zero. Both proofs are correct and instructive. The coefficient-extraction proof is more directly applicable in other contexts (Fourier coefficients, Riesz vectors, dual-basis computations). The norm-formula proof is more conceptually clean — it relies on the squared-norm identity that the Pythagorean theorem gives. Knowing both proofs is useful because different problems naturally lead to one or the other.

**The result holds in infinite dimensions verbatim.** The proof above is completely finite-character: a vanishing finite linear combination, finitely many coefficient extractions, finitely many equality checks. The same argument shows that any **finite** orthonormal subset of a Hilbert space (countable or otherwise) is linearly independent. The infinite version — that any orthonormal sequence is linearly independent — follows from the fact that linear combinations involve only finitely many nonzero coefficients. So in any inner product space (finite- or infinite-dimensional), orthonormal lists are linearly independent, and the proof technique generalizes verbatim.

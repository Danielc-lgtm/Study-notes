---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Trace"
  - "Def - Change of Basis Matrix"
  - "Def - Matrix of a Linear Map"
tags: [algebra, linear-algebra]
---

# Problem Statement

(a) Prove that for any square matrices $A$ ($m \times n$) and $B$ ($n \times m$), $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ — the **cyclic property** of the trace.

(b) Deduce that for any invertible matrix $C$ of the same size as a square matrix $A$, $\operatorname{tr}(C^{-1} A C) = \operatorname{tr}(A)$.

(c) Conclude that the trace of an operator $T \in \mathcal{L}(V)$ — defined as the trace of any matrix of $T$ in any basis — is well-defined (does not depend on the basis).

(d) Verify that the trace is a *linear functional* on $\mathcal{L}(V)$: $\operatorname{tr}(\lambda S + \mu T) = \lambda \operatorname{tr} S + \mu \operatorname{tr} T$ for all $\lambda, \mu \in \mathbf{F}$ and $S, T \in \mathcal{L}(V)$. Also verify $\operatorname{tr}(I) = \dim V$.

**Recall:**

The objects are square matrices, their products, and operators on a finite-dimensional space.

![[Def - Trace#The Definition]]

The matrix of an operator depends on the choice of basis; the change-of-basis formula (see [[Def - Change of Basis Matrix]]) says that if $A$ is the matrix of $T$ in basis $\beta$ and $B$ is the matrix of $T$ in basis $\gamma$, then $B = C^{-1} A C$ where $C$ is the change-of-basis matrix from $\gamma$ to $\beta$.

---

# Convergent Strategy

**Problem class.** This is a *foundational algebraic identity* problem — establishing the trace's basic properties from its definition. The class is the kind of "verify the definition has the expected properties" that appears at the start of any treatment of a new invariant.

**Assumption pattern.** The matrices are arbitrary; the only hypothesis is the index-matching ($A$ is $m \times n$, $B$ is $n \times m$, so $AB$ and $BA$ are both defined). For (b) we add invertibility of $C$. For (c) we add finite-dimensionality of $V$. For (d) we add nothing — linearity is immediate from the definition.

**Theorem routing.** Single chain of identities: cyclic property of matrix multiplication via index manipulation ($\sum_{i,j} A_{i,j} B_{j,i} = \sum_{j,i} B_{j,i} A_{i,j}$) gives (a). Substituting $A = (C^{-1}) X$ and $B = (X C) = (XC)$ for $X = (C A)$... wait, let me re-think. We have $\operatorname{tr}(C^{-1} (AC))$ and want to apply (a). Setting $A' = C^{-1}$, $B' = AC$, we have $A' B' = C^{-1} A C$ (the target) and $B' A' = A C C^{-1} = A$. So (a) gives $\operatorname{tr}(C^{-1} A C) = \operatorname{tr}(A)$, which is (b). For (c), use (b) plus the change-of-basis formula. For (d), unfold the definition.

**Key decision point.** The non-obvious move is to *carefully match the indices in the cyclic property proof*. The identity $\operatorname{tr}(AB) = \sum_{i, j} A_{i,j} B_{j,i} = \sum_{j, i} B_{j,i} A_{i, j} = \operatorname{tr}(BA)$ uses two facts: (i) the diagonal entries of $AB$ are sums $\sum_j A_{i,j} B_{j,i}$ — this is matrix multiplication; (ii) summation is commutative, so swapping the order of the two sums is fine. The diagonal entries of $BA$ are then $\sum_i B_{j,i} A_{i,j}$, which is the same expression with $i$ and $j$ exchanged in the role of "row" and "column". The key is to keep track of which sum is over what index.

---

# Legal Operations Used

This solution does not deploy operations from the topic page's Legal Operations directly — it is a foundational identity that *underlies* those operations rather than using them. In particular, operation 7 ("Read the trace and determinant off any matrix") *relies on this exercise* for its validity.

The cyclic property of the trace is one of those structural identities, like the symmetry of mixed partial derivatives in calculus or the unitarity of the Fourier transform in analysis, that is foundational rather than derivative.

---

# Hints

> [!note]- Hint 1 (for part (a))
> Compute the diagonal entries of $AB$ directly: $(AB)_{i,i} = \sum_j A_{i,j} B_{j,i}$. Compute the diagonal entries of $BA$: $(BA)_{j,j} = \sum_i B_{j,i} A_{i,j}$. Now sum the diagonal entries over $i$ for $AB$ and over $j$ for $BA$, and observe the resulting double sums are the same.

> [!note]- Hint 2 (for part (b))
> Use part (a) twice. First with $A' = C^{-1}$ and $B' = A C$ to get $\operatorname{tr}((C^{-1})(AC)) = \operatorname{tr}((AC)(C^{-1}))$. Simplify the right side using $CC^{-1} = I$.

> [!note]- Hint 3 (for part (c))
> The matrices of $T$ in two bases are related by the change-of-basis formula: $B = C^{-1} A C$. Apply (b).

> [!note]- Hint 4 (for part (d))
> Each property follows from the corresponding property of matrices, applied entry-by-entry on the diagonal.

---

# Solution

The strategy is to compute the cyclic property directly from the definition of matrix multiplication, then apply it twice to get basis-independence, then unfold linearity.

**Step 1 (Part (a)): The cyclic property $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.**

Compute both sides as double sums over the indices, and observe they are the same expression.

> [!note]- Derivation
> Suppose $A$ is $m \times n$ with entries $A_{i,j}$ ($1 \leq i \leq m$, $1 \leq j \leq n$) and $B$ is $n \times m$ with entries $B_{k,l}$ ($1 \leq k \leq n$, $1 \leq l \leq m$). Then $AB$ is $m \times m$ with entries
> $$(AB)_{i,l} = \sum_{j=1}^n A_{i, j} B_{j, l}.$$
> The diagonal of $AB$ is $(AB)_{i, i} = \sum_j A_{i,j} B_{j,i}$. Summing over $i$:
> $$\operatorname{tr}(AB) = \sum_{i=1}^m (AB)_{i, i} = \sum_{i=1}^m \sum_{j=1}^n A_{i, j} B_{j, i}.$$
>
> Similarly, $BA$ is $n \times n$ with $(BA)_{j, k} = \sum_i B_{j, i} A_{i, k}$, and the diagonal is $(BA)_{j, j} = \sum_i B_{j, i} A_{i, j}$. Summing over $j$:
> $$\operatorname{tr}(BA) = \sum_{j=1}^n (BA)_{j, j} = \sum_{j=1}^n \sum_{i=1}^m B_{j, i} A_{i, j} = \sum_{i=1}^m \sum_{j=1}^n B_{j, i} A_{i, j}.$$
>
> Since multiplication of scalars is commutative, $A_{i, j} B_{j, i} = B_{j, i} A_{i, j}$, and the two double sums are equal. Hence $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.

**Step 2 (Part (b)): Conjugation-invariance $\operatorname{tr}(C^{-1} A C) = \operatorname{tr}(A)$ for invertible $C$.**

Apply the cyclic property of (a) with the factors $(C^{-1})$ and $(AC)$.

> [!note]- Derivation
> Take $A' = C^{-1}$ (a square matrix) and $B' = A C$. Then $A' B' = C^{-1} (A C) = C^{-1} A C$, and $B' A' = (A C) C^{-1} = A (C C^{-1}) = A I = A$.
>
> By the cyclic property (a),
> $$\operatorname{tr}(C^{-1} A C) = \operatorname{tr}(A' B') = \operatorname{tr}(B' A') = \operatorname{tr}(A).$$

**Step 3 (Part (c)): The trace of an operator is well-defined.**

Use the change-of-basis formula and (b).

> [!note]- Derivation
> Let $T \in \mathcal{L}(V)$ and let $\beta = (v_1, \dots, v_n)$ and $\gamma = (w_1, \dots, w_n)$ be two ordered bases of $V$. Let $A = \mathcal{M}(T, \beta)$ and $B = \mathcal{M}(T, \gamma)$ be the matrices of $T$ in these bases.
>
> By the change-of-basis formula (see [[Def - Change of Basis Matrix]]), there is an invertible matrix $C$ such that
> $$B = C^{-1} A C.$$
> (Specifically $C$ is the matrix whose $k$-th column is the coordinates of $w_k$ in the basis $\beta$, but we do not need this explicit form.)
>
> By (b), $\operatorname{tr}(B) = \operatorname{tr}(C^{-1} A C) = \operatorname{tr}(A)$. So the trace of the matrix of $T$ does not depend on the choice of basis, and the definition $\operatorname{tr}(T) := \operatorname{tr}(\mathcal{M}(T, \beta))$ is independent of $\beta$.

**Step 4 (Part (d)): Linearity and $\operatorname{tr}(I) = \dim V$.**

Each property follows from the analogous property of matrix entries on the diagonal.

> [!note]- Derivation
> Fix a basis $\beta = (v_1, \dots, v_n)$ of $V$ and let $\mathcal{M}(\cdot, \beta)$ denote the matrix in this basis.
>
> **Linearity.** For $\lambda, \mu \in \mathbf{F}$ and $S, T \in \mathcal{L}(V)$:
> $$\mathcal{M}(\lambda S + \mu T, \beta) = \lambda \mathcal{M}(S, \beta) + \mu \mathcal{M}(T, \beta)$$
> (because the map $T \mapsto \mathcal{M}(T, \beta)$ is linear — see [[Def - Matrix of a Linear Map]]). Hence the $(i, i)$-entry of $\mathcal{M}(\lambda S + \mu T, \beta)$ is $\lambda \mathcal{M}(S, \beta)_{i,i} + \mu \mathcal{M}(T, \beta)_{i,i}$. Summing over $i$:
> $$\operatorname{tr}(\lambda S + \mu T) = \sum_i \lambda \mathcal{M}(S, \beta)_{i, i} + \sum_i \mu \mathcal{M}(T, \beta)_{i, i} = \lambda \operatorname{tr}(S) + \mu \operatorname{tr}(T).$$
>
> **Value at identity.** $\mathcal{M}(I, \beta)$ is the $n \times n$ identity matrix, with $1$s on the diagonal and $0$s elsewhere. The trace is $\sum_i 1 = n = \dim V$.

> [!note]- Complete formal solution
> **(a)** Let $A$ be $m \times n$ and $B$ be $n \times m$. By definition of matrix multiplication, $(AB)_{i,l} = \sum_{j} A_{i,j} B_{j,l}$. Hence
> $$\operatorname{tr}(AB) = \sum_i (AB)_{i, i} = \sum_{i, j} A_{i, j} B_{j, i}.$$
> Similarly $\operatorname{tr}(BA) = \sum_{j, i} B_{j, i} A_{i, j}$. By commutativity of scalar multiplication, $A_{i, j} B_{j, i} = B_{j, i} A_{i, j}$, so both double sums are the same: $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
>
> **(b)** Apply (a) with $A' = C^{-1}$ and $B' = AC$:
> $$\operatorname{tr}(C^{-1} A C) = \operatorname{tr}((C^{-1})(AC)) = \operatorname{tr}((AC)(C^{-1})) = \operatorname{tr}(A \cdot I) = \operatorname{tr}(A).$$
>
> **(c)** Let $A$ and $B$ be matrices of $T$ in bases $\beta$ and $\gamma$ respectively. The change-of-basis formula gives $B = C^{-1} A C$ for the change-of-basis matrix $C$. By (b), $\operatorname{tr}(B) = \operatorname{tr}(A)$. So the trace of a matrix of $T$ does not depend on the basis, and $\operatorname{tr}(T)$ is well-defined.
>
> **(d)** Fix a basis $\beta$. The map $T \mapsto \mathcal{M}(T, \beta)$ is linear ([[Def - Matrix of a Linear Map]]), so $\mathcal{M}(\lambda S + \mu T, \beta) = \lambda \mathcal{M}(S, \beta) + \mu \mathcal{M}(T, \beta)$. Taking traces (which is a linear functional on matrices) gives $\operatorname{tr}(\lambda S + \mu T) = \lambda \operatorname{tr}(S) + \mu \operatorname{tr}(T)$. Also, $\mathcal{M}(I, \beta)$ is the $n \times n$ identity matrix, whose trace is $n = \dim V$. $\blacksquare$

---

# Key Takeaways

**The cyclic property of the trace is the master identity for basis-invariance.** The cyclic property $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ has dramatic consequences. It immediately gives conjugation-invariance ($\operatorname{tr}(C^{-1} A C) = \operatorname{tr}(A)$), which gives basis-independence of the operator trace; it gives that $\operatorname{tr}([X, Y]) = \operatorname{tr}(XY) - \operatorname{tr}(YX) = 0$ for all $X, Y$, the **Lie-algebraic identity** that drops the trace functional to the Lie algebra $\mathfrak{sl}$; it gives the **invariance** of the trace under all inner automorphisms of $\mathrm{GL}(V)$; it gives the analogous identity for the Hilbert–Schmidt inner product on $\mathcal{L}(V)$. Every property of the trace that is not direct from the definition uses cyclicity. The reusable diagnostic: when you see a basis-invariance or class-function claim about the trace, the proof is almost always one application of cyclicity.

**The basis-independence reduces operator-level statements to matrix-level computations.** The trace of an operator $T$ can be computed in *any* basis — there is no privileged choice. This is the operator-theoretic version of "the determinant of $T$ is well-defined" (also an exercise in basis-independence). The transferable lesson is that whenever you want to compute an invariant of $T$, *choose the basis that makes the computation easiest*. For the trace, this is often the standard basis (if a matrix is given) or the upper-triangular basis (if you have access to one — see [[Thm - Trace Equals Sum of Eigenvalues]] for the spectral version). For the determinant, an upper-triangular basis is also good. For more refined invariants like the Jordan form, a Jordan basis is the privileged one. *Basis-choosing-strategy* is a meta-skill.

**The trace is a linear functional, not a multiplicative one.** In the universe of operations on operators, addition behaves well ($\operatorname{tr}(S + T) = \operatorname{tr}(S) + \operatorname{tr}(T)$) but multiplication does not ($\operatorname{tr}(ST) \neq \operatorname{tr}(S) \operatorname{tr}(T)$ in general — see Step 4's non-example $\operatorname{diag}(1, 0) \cdot \operatorname{diag}(0, 1) = 0$). The right "multiplicative" identity is the cyclic one: $\operatorname{tr}(ST) = \operatorname{tr}(TS)$. This is exactly the statement that the trace vanishes on commutators, and it is the algebraic foundation for many results: the LADR theorem 8.57 ("the identity is not a commutator", $\operatorname{tr}(ST - TS) = 0 \neq \dim V = \operatorname{tr} I$), the uniqueness of the trace as a Lie-algebra functional ($\operatorname{tr}$ is unique up to scalar among linear functionals vanishing on commutators), the canonical commutation relation $[Q, P] = i \hbar$ requiring infinite [[Def - Dimension|dimensions]], and others. The reusable insight is to think of the trace as a linear functional with a specific cyclic property — not as a quantity that "behaves like a number" in every way.

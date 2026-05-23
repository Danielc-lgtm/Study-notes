---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Embedded Submanifold"
  - "Def - Regular and Critical Points"
  - "Def - Tangent Space of a Submanifold"
  - "Thm - Regular Value Theorem on Manifolds"
tags: [geometry, differential-geometry]
---

# Problem Statement

Show that the orthogonal group
$$\mathrm{O}(n) = \{A \in \mathrm{GL}(n,\mathbb{R}) : A^T A = I\}$$
is an embedded smooth submanifold of $\mathrm{GL}(n,\mathbb{R})$ of dimension $n(n-1)/2$. The non-obvious step is to choose the codomain of the defining map correctly: the naive choice "$\Phi(A) = A^T A - I$ valued in $\mathrm{Mat}_n$" makes the differential fail to be surjective. Identify the correct codomain (symmetric matrices) and verify the regular value condition. Then compute the tangent space at the identity
$$T_I \mathrm{O}(n) = \mathfrak{o}(n) = \{X \in \mathrm{Mat}_n : X + X^T = 0\}$$
— the antisymmetric matrices, which form the **Lie algebra** of $\mathrm{O}(n)$.

**Recall:**

The space $\mathrm{Sym}_n = \{S \in \mathrm{Mat}_n : S = S^T\}$ of symmetric $n \times n$ matrices is a linear subspace of $\mathrm{Mat}_n$ of dimension $n(n+1)/2$ (entries on and above the diagonal are free, entries below are determined by the symmetry condition).

The space $\mathrm{AntiSym}_n = \mathfrak{o}(n) = \{X \in \mathrm{Mat}_n : X = -X^T\}$ of antisymmetric (or skew-symmetric) matrices has dimension $n(n-1)/2$ (entries strictly above the diagonal are free; the diagonal must be zero; the entries below the diagonal are determined).

$\mathrm{Mat}_n = \mathrm{Sym}_n \oplus \mathrm{AntiSym}_n$ as vector spaces, since any matrix $X$ decomposes uniquely as $X = \frac{1}{2}(X + X^T) + \frac{1}{2}(X - X^T)$ (symmetric + antisymmetric).

By [[Thm - Regular Value Theorem on Manifolds]], a regular level set is properly embedded with tangent space the kernel of the defining map's differential.

---

# Convergent Strategy

**Problem class:** This is a regular value theorem application to identify a matrix Lie group, with the technical twist that the naive defining map fails the surjectivity check, and one must choose the codomain to match the actual image.

**Assumption pattern:** $\mathrm{O}(n)$ is the preimage of $I$ under $\Phi(A) = A^T A$. Crucially, $A^T A$ is *always* symmetric (transpose of $A^T A$ is $A^T A$ again), so the image of $\Phi$ lies in $\mathrm{Sym}_n$, *not* in all of $\mathrm{Mat}_n$. Viewing $\Phi$ as $\mathrm{Mat}_n \to \mathrm{Mat}_n$, the differential cannot be surjective onto $\mathrm{Mat}_n$ — but viewed as $\Phi : \mathrm{Mat}_n \to \mathrm{Sym}_n$, the differential *can* be surjective onto $\mathrm{Sym}_n$, and we'll verify it is at every point of $\mathrm{O}(n)$.

**Theorem routing:** The route is:
1. Define $\Phi : \mathrm{Mat}_n \to \mathrm{Sym}_n$ by $\Phi(A) = A^T A$, noting the codomain.
2. Compute $d\Phi_A(X) = A^T X + X^T A$ (product rule for matrix multiplication and transpose).
3. Restricted to $A \in \mathrm{O}(n)$ (where $A^T = A^{-1}$), show $d\Phi_A$ is surjective onto $\mathrm{Sym}_n$.
4. Conclude $I \in \mathrm{Sym}_n$ is a regular value, so $\mathrm{O}(n) = \Phi^{-1}(I)$ is an embedded submanifold of dimension $\dim \mathrm{Mat}_n - \dim \mathrm{Sym}_n = n^2 - n(n+1)/2 = n(n-1)/2$.
5. Read off $T_I \mathrm{O}(n) = \ker d\Phi_I = \{X : X + X^T = 0\} = \mathfrak{o}(n)$.

**Key decision point:** The crucial non-obvious step is the *choice of codomain*. The naive map $\Phi : \mathrm{Mat}_n \to \mathrm{Mat}_n$, $\Phi(A) = A^T A - I$, has the issue that its image is contained in symmetric matrices, so the rank of the differential is at most $n(n+1)/2$, not $n^2$ — making $0$ a critical value of this map. The correct map is $\Phi : \mathrm{Mat}_n \to \mathrm{Sym}_n$, $\Phi(A) = A^T A$; with the smaller codomain, the differential *can* achieve maximal rank, and $I$ becomes a regular value. This codomain-choice trick recurs for $\mathrm{U}(n)$ (codomain Hermitian matrices), $\mathrm{Sp}(2n)$ (codomain antisymmetric matrices), and other matrix Lie groups where the defining equation has a hidden symmetry.

---

# Legal Operations Used

1. **Operation 3 from the topic page (choose the codomain to match the actual image):** the central technique. The defining map's image is automatically in the symmetric matrices, so the right codomain is $\mathrm{Sym}_n$, not $\mathrm{Mat}_n$.

2. **Operation 2 (apply the regular value theorem):** after choosing the codomain, the standard application gives the submanifold structure.

3. **Operation 1 (compute the differential in coordinates):** computing $d\Phi_A(X) = A^T X + X^T A$ is a direct computation via the product rule for matrix multiplication: $\Phi(A + tX) = (A + tX)^T(A + tX) = A^T A + t(A^T X + X^T A) + t^2 X^T X$, giving $d\Phi_A(X) = A^T X + X^T A$.

4. **Operation 8 (identify tangent vectors as velocities of curves):** an alternative for the tangent space at $I$. A smooth curve $A(t)$ in $\mathrm{O}(n)$ with $A(0) = I$ satisfies $A(t)^T A(t) = I$. Differentiating at $t = 0$: $A'(0)^T + A'(0) = 0$, so $A'(0)$ is antisymmetric.

---

# Hints

> [!note]- Hint 1
> What is the most natural defining function for $\mathrm{O}(n)$? Think of $\mathrm{O}(n)$ as the matrices preserving a quadratic form, namely the standard inner product on $\mathbb{R}^n$.

> [!note]- Hint 2
> Try $\Phi(A) = A^T A$. What is the natural codomain — what space does $A^T A$ live in? (Compute its transpose.)

> [!note]- Hint 3
> Once you have the right codomain $\mathrm{Sym}_n$, compute $d\Phi_A(X)$. Use the product rule: $\Phi(A + tX) = (A + tX)^T(A + tX)$. Expand to first order in $t$.

> [!note]- Hint 4
> Show $d\Phi_A : \mathrm{Mat}_n \to \mathrm{Sym}_n$ is surjective at every $A \in \mathrm{O}(n)$. Given a target $S \in \mathrm{Sym}_n$, exhibit an $X \in \mathrm{Mat}_n$ with $d\Phi_A(X) = S$. (Hint: use $A^T = A^{-1}$ for $A \in \mathrm{O}(n)$.)

> [!note]- Hint 5
> The dimension count: $\dim \mathrm{Mat}_n - \dim \mathrm{Sym}_n = n^2 - n(n+1)/2 = n(n-1)/2$.

> [!note]- Hint 6
> For the tangent space at $I$: $d\Phi_I(X) = X + X^T$, so $\ker d\Phi_I = \{X : X + X^T = 0\}$.

---

# Solution

The proof breaks into four steps. Step 1 identifies the correct codomain. Step 2 computes the differential. Step 3 verifies surjectivity of the differential at every point of $\mathrm{O}(n)$ — the crucial regularity check, using the fact that $A^{-1} = A^T$ for $A \in \mathrm{O}(n)$. Step 4 applies the regular value theorem and reads off the tangent space at the identity.

**Step 1: The defining function is $\Phi(A) = A^T A$ valued in $\mathrm{Sym}_n$.**

> [!note]- Derivation
> Define $\Phi : \mathrm{Mat}_n(\mathbb{R}) \to \mathrm{Mat}_n(\mathbb{R})$ by $\Phi(A) = A^T A$. This is smooth (polynomial in the matrix entries).
>
> **Crucial observation:** $\Phi(A)$ is always *symmetric*. Indeed, $(\Phi(A))^T = (A^T A)^T = A^T (A^T)^T = A^T A = \Phi(A)$. So the image of $\Phi$ lies entirely in the linear subspace $\mathrm{Sym}_n = \{S \in \mathrm{Mat}_n : S = S^T\} \subseteq \mathrm{Mat}_n$. We therefore view $\Phi$ as a smooth map
> $$\Phi : \mathrm{Mat}_n(\mathbb{R}) \to \mathrm{Sym}_n.$$
> With this codomain, $\dim \mathrm{Mat}_n = n^2$ and $\dim \mathrm{Sym}_n = n(n+1)/2$.
>
> The orthogonal group is $\mathrm{O}(n) = \{A : A^T A = I\} = \Phi^{-1}(I) \subseteq \mathrm{Mat}_n$, with $I$ regarded as an element of $\mathrm{Sym}_n$ (which it is, since $I^T = I$).

**Step 2: $d\Phi_A(X) = A^T X + X^T A$.**

> [!note]- Derivation
> Expand $\Phi(A + tX)$ to first order in $t$:
> $$\Phi(A + tX) = (A + tX)^T(A + tX) = A^T A + t(A^T X + X^T A) + t^2 X^T X.$$
> The first-order coefficient is $A^T X + X^T A$. Hence
> $$d\Phi_A(X) = A^T X + X^T A.$$
> Sanity check: this is a symmetric matrix, as expected — $(A^T X + X^T A)^T = X^T A + A^T X = A^T X + X^T A$ (using $(BC)^T = C^T B^T$). So $d\Phi_A$ maps $\mathrm{Mat}_n$ into $\mathrm{Sym}_n$, confirming the codomain choice.

**Step 3: $d\Phi_A$ is surjective onto $\mathrm{Sym}_n$ for every $A \in \mathrm{O}(n)$.**

> [!note]- Derivation
> Given $S \in \mathrm{Sym}_n$, we must exhibit some $X \in \mathrm{Mat}_n$ with $d\Phi_A(X) = A^T X + X^T A = S$.
>
> Try $X = \frac{1}{2} A S$. Then
> $$A^T X = A^T \cdot \frac{1}{2} A S = \frac{1}{2}(A^T A) S = \frac{1}{2} S \quad \text{(using $A^T A = I$ for $A \in \mathrm{O}(n)$).}$$
> Also $X^T = \frac{1}{2} S^T A^T = \frac{1}{2} S A^T$ (using $S^T = S$), so
> $$X^T A = \frac{1}{2} S A^T A = \frac{1}{2} S \quad \text{(using $A^T A = I$).}$$
> Hence $d\Phi_A(X) = A^T X + X^T A = \frac{1}{2}S + \frac{1}{2}S = S$. So $d\Phi_A$ is surjective onto $\mathrm{Sym}_n$ at every $A \in \mathrm{O}(n)$.
>
> Hence $I$ is a regular value of $\Phi : \mathrm{Mat}_n \to \mathrm{Sym}_n$ (every point of $\mathrm{O}(n) = \Phi^{-1}(I)$ is a regular point).

**Step 4: Apply the regular value theorem and read off $T_I \mathrm{O}(n)$.**

> [!note]- Derivation
> By [[Thm - Regular Value Theorem on Manifolds]] (with $M = \mathrm{Mat}_n$ of dimension $n^2$, $N = \mathrm{Sym}_n$ of dimension $n(n+1)/2$, $\Phi$ as defined, $c = I$), $\mathrm{O}(n) = \Phi^{-1}(I)$ is a properly embedded smooth submanifold of $\mathrm{Mat}_n$ of codimension $\dim \mathrm{Sym}_n = n(n+1)/2$. The dimension is
> $$\dim \mathrm{O}(n) = n^2 - \frac{n(n+1)}{2} = \frac{2n^2 - n^2 - n}{2} = \frac{n^2 - n}{2} = \frac{n(n-1)}{2}.$$
> The tangent space at $A \in \mathrm{O}(n)$ is
> $$T_A \mathrm{O}(n) = \ker d\Phi_A = \{X \in \mathrm{Mat}_n : A^T X + X^T A = 0\}.$$
> At $A = I$ (where $A^T = I$):
> $$T_I \mathrm{O}(n) = \{X \in \mathrm{Mat}_n : X + X^T = 0\} = \mathfrak{o}(n),$$
> the antisymmetric matrices, of dimension $n(n-1)/2$ as expected.
>
> $\mathrm{O}(n)$ is also closed in $\mathrm{GL}(n,\mathbb{R})$ (the equation $A^T A = I$ is closed), hence properly embedded; in fact it is closed and bounded in $\mathrm{Mat}_n$ (each entry of an orthogonal matrix has absolute value at most $1$), so $\mathrm{O}(n)$ is *compact*.

> [!note]- Complete formal solution
> Define $\Phi : \mathrm{Mat}_n(\mathbb{R}) \to \mathrm{Sym}_n$ by $\Phi(A) = A^T A$. Since $(A^T A)^T = A^T A$, the image of $\Phi$ is contained in $\mathrm{Sym}_n$, so this is a well-defined smooth map. $\mathrm{O}(n) = \Phi^{-1}(I) \subseteq \mathrm{Mat}_n$, with $I \in \mathrm{Sym}_n$.
>
> By the product-rule expansion $(A + tX)^T(A + tX) = A^T A + t(A^T X + X^T A) + O(t^2)$, the differential of $\Phi$ at $A$ is $d\Phi_A(X) = A^T X + X^T A$.
>
> For $A \in \mathrm{O}(n)$ (where $A^T A = I$) and any $S \in \mathrm{Sym}_n$, take $X = \frac{1}{2} A S$. Then $A^T X = \frac{1}{2} S$ and $X^T A = \frac{1}{2} S^T A^T A = \frac{1}{2} S$, giving $d\Phi_A(X) = S$. So $d\Phi_A$ surjects onto $\mathrm{Sym}_n$, i.e., every $A \in \mathrm{O}(n)$ is a regular point and $I$ is a regular value.
>
> By [[Thm - Regular Value Theorem on Manifolds]], $\mathrm{O}(n)$ is a properly embedded submanifold of $\mathrm{Mat}_n$ of codimension $\dim \mathrm{Sym}_n = n(n+1)/2$, hence of dimension $n^2 - n(n+1)/2 = n(n-1)/2$. The tangent space at $I$ is
> $$T_I \mathrm{O}(n) = \ker d\Phi_I = \{X \in \mathrm{Mat}_n : X + X^T = 0\} = \mathfrak{o}(n). \qquad\blacksquare$$
>
> **Sanity check via curves.** A smooth curve $A : (-\varepsilon, \varepsilon) \to \mathrm{O}(n)$ with $A(0) = I$ satisfies $A(t)^T A(t) = I$ for all $t$. Differentiating at $t = 0$: $A'(0)^T \cdot I + I \cdot A'(0) = 0$, i.e., $A'(0)^T + A'(0) = 0$. So $A'(0)$ is antisymmetric. Conversely, for any antisymmetric $X$, the curve $A(t) = e^{tX}$ satisfies $A(t)^T = e^{tX^T} = e^{-tX} = A(t)^{-1}$, so $A(t)^T A(t) = I$, and $A(t) \in \mathrm{O}(n)$ with $A(0) = I$ and $A'(0) = X$. So $T_I \mathrm{O}(n) = \mathfrak{o}(n)$, confirming the kernel computation.

> [!warning] Illegal but tempting alternative route — using $\Phi : \mathrm{Mat}_n \to \mathrm{Mat}_n$ as the defining map
> A naive attempt is to use the same formula $\Phi(A) = A^T A - I$ but view it as $\mathrm{Mat}_n \to \mathrm{Mat}_n$, hoping $0$ is a regular value. This *fails* because the image of $\Phi$ is automatically in $\mathrm{Sym}_n - I \subseteq \mathrm{Sym}_n$ (since both $A^T A$ and $I$ are symmetric), so the differential $d\Phi_A$ also lands in $\mathrm{Sym}_n - $ (the constant translate). Specifically, $d\Phi_A(X) = A^T X + X^T A$, which is symmetric, so the image of $d\Phi_A$ is contained in $\mathrm{Sym}_n$ — a $n(n+1)/2$-dimensional subspace of the $n^2$-dimensional target. The rank of $d\Phi_A$ as a map into $\mathrm{Mat}_n$ is at most $n(n+1)/2 < n^2$, so $d\Phi_A$ is not surjective onto $\mathrm{Mat}_n$. The trap: $0$ is not a regular value of $\Phi$ viewed as $\mathrm{Mat}_n \to \mathrm{Mat}_n$, and the regular value theorem does not apply with this codomain choice. The repair is to shrink the codomain to $\mathrm{Sym}_n$, which is what we did above.

---

# Key Takeaways

**Choosing the codomain to match the actual image.** This is the most important technical lesson of the exercise, and it generalises to a recurring trap in matrix-Lie-group problems. Whenever a defining map has a *hidden symmetry* — its values automatically satisfy some equation, like being symmetric, antisymmetric, Hermitian, etc. — the codomain should be the smaller subspace where the values actually live, not the full ambient space. Examples beyond $\mathrm{O}(n)$:
- $\mathrm{U}(n) = \{A \in \mathrm{GL}(n,\mathbb{C}) : A^* A = I\}$: $A^* A$ is automatically Hermitian, so the codomain is the Hermitian matrices, not all complex matrices.
- $\mathrm{Sp}(2n,\mathbb{R}) = \{A : A^T J A = J\}$ for $J$ the standard symplectic form: $A^T J A$ is automatically antisymmetric (since $J^T = -J$), so the codomain is antisymmetric matrices.

The general principle: the defining map's *image* sits in a smaller subspace by structural reasons; checking regular value with the right codomain is the *only* way to make the theorem apply.

**The trace-zero / antisymmetric Lie algebras are the canonical examples.** $\mathfrak{sl}(n) = \{X : \mathrm{tr}\, X = 0\}$ and $\mathfrak{o}(n) = \{X : X + X^T = 0\}$ are the simplest and most-used matrix Lie algebras. Each is the tangent space at the identity of its matrix Lie group, computed as the kernel of the differential of the defining map at $I$. The pattern repeats throughout Lie theory: every classical Lie group has its Lie algebra as the kernel of the differential of its defining map at the identity. The dimension counts ($n^2 - 1$ for $\mathfrak{sl}(n)$, $n(n-1)/2$ for $\mathfrak{o}(n)$) are computed as $\dim \mathrm{Mat}_n - \dim(\text{codomain})$.

**Compactness comes for free.** $\mathrm{O}(n)$ is compact: it is closed (preimage of the closed point $I$ under a continuous map) and bounded (each row of an orthogonal matrix has length $1$, so each entry is at most $1$ in absolute value). Compactness is the additional property that distinguishes $\mathrm{O}(n)$ from $\mathrm{SL}(n)$ (which is non-compact: $\mathrm{SL}(n)$ contains arbitrarily large matrices). Compact matrix Lie groups have many additional properties — finite-dimensional representations are unitarisable, averaging over the group via the Haar measure works, etc. — that make them especially tractable.

**Curve-based tangent space computation as a sanity check.** The two-direction verification — kernel of differential matches velocities of curves through the identity — is the standard sanity check for tangent space computations on matrix Lie groups. The "kernel direction" uses the regular value theorem; the "curve direction" uses the exponential map $e^{tX}$ for $X$ in the candidate tangent space. The two agreeing is the confirmation that the candidate Lie algebra is correct.

**Cross-link to companion exercises.** This is the canonical "hard" matrix-Lie-group example in the topic. The companion [[Ex - The Special Linear Group is a Submanifold of GL(n)|Ex - The Special Linear Group is a Submanifold of GL(n)]] illustrates the simpler scalar-codomain case where the codomain choice is automatic. Future exercises in [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]] develop the general theory of Lie groups and Lie algebras, of which $\mathrm{O}(n)$ and $\mathfrak{o}(n)$ are foundational examples.

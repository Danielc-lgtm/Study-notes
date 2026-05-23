---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Left and Right Inverse of a Matrix"
  - "Def - Norm and Distance"
tags: [algebra, linear-algebra, applied, least-squares]
---

# Problem Statement

Let $A \in \mathbb R^{m \times n}$ with $m \geq n$ and linearly independent columns. Define the **[[Def - Pseudoinverse|pseudoinverse]]**
$$A^\dagger = (A^T A)^{-1} A^T.$$

(a) Show that $A^T A$ is invertible (so $(A^T A)^{-1}$ exists).

(b) Show that $A^\dagger$ is a left inverse of $A$, i.e., $A^\dagger A = I_n$.

(c) Given any $b \in \mathbb R^m$, define $\hat x = A^\dagger b$. Show that $\hat x$ minimises the **least-squares objective** $\|Ax - b\|^2$ over $x \in \mathbb R^n$, by showing that the residual $b - A\hat x$ is orthogonal to the columns of $A$.

**Recall:**

A **left inverse** $C$ of $A$ satisfies $CA = I$; see [[Def - Left and Right Inverse of a Matrix]]. The **Euclidean norm** is $\|v\| = \sqrt{v^T v}$; see [[Def - Norm and Distance]]. The **Gram matrix** of the columns of $A$ is $A^T A$, an $n \times n$ symmetric matrix.

A vector $v \in \mathbb R^m$ is **orthogonal** to the columns of $A$ if $A^T v = 0$.

---

# Convergent Strategy

**Problem class.** This is a *core theorem of least-squares*, decomposed into a sequence of standard moves: invertibility of the Gram matrix, the [[Def - Pseudoinverse|pseudoinverse]] as a left inverse, and the orthogonality characterisation of the least-squares solution.

**Assumption pattern.** $A$ is tall ($m \geq n$) with linearly independent columns. The first hypothesis ensures $A^T A$ is $n \times n$ and the second ensures it is invertible.

**Theorem routing.** (a) Invertibility of $A^T A$ via linear independence of columns of $A$. (b) Direct computation: $A^\dagger A = (A^T A)^{-1}(A^T A) = I$. (c) The least-squares solution is characterised by the **normal equations** $A^T(b - Ax) = 0$, equivalently $A^T A x = A^T b$, equivalently $x = (A^T A)^{-1} A^T b = A^\dagger b$.

**Key decision point.** The non-obvious step is recognising that *the least-squares problem $\min_x \|Ax - b\|^2$ is solved by demanding $A^T(b - Ax) = 0$* — the orthogonality of the residual to the column space. This is the **geometric** characterisation of least-squares: the residual must be perpendicular to the search space.

---

# Legal Operations Used

1. **Operation 10 (invoke linear independence).** Linear independence of columns of $A$ $\Rightarrow$ $A^T A$ is invertible.

2. **Operation 2 (reduce a question to an inner product).** The least-squares objective $\|Ax - b\|^2$ is an inner product; its derivative or expansion reveals the orthogonality condition.

3. **Operation 4 (expand a squared norm).** Apply to $\|Ax - b\|^2$ to obtain the explicit quadratic in $x$.

---

# Hints

> [!note]- Hint 1
> For (a): show $A^T A x = 0 \Rightarrow x = 0$. Use the fact that $x^T A^T A x = \|Ax\|^2$ and that the columns of $A$ are linearly independent.

> [!note]- Hint 2
> For (b): compute $A^\dagger A$ directly using the definition $A^\dagger = (A^T A)^{-1} A^T$.

> [!note]- Hint 3
> For (c): expand $\|Ax - b\|^2 = (Ax - b)^T(Ax - b)$. Take the derivative with respect to $x$ (or complete the square), set to zero, get $A^T A x = A^T b$.

> [!note]- Hint 4
> Equivalently, write the residual condition: $\hat x$ minimises iff $b - A\hat x$ is orthogonal to every column of $A$, i.e., $A^T(b - A\hat x) = 0$.

---

# Solution

The proof has three steps. Step 1 establishes that $A^T A$ is invertible. Step 2 verifies that $A^\dagger$ is a left inverse. Step 3 shows that $\hat x = A^\dagger b$ satisfies the normal equations and hence minimises the least-squares objective.

**Step 1: $A^T A$ is invertible.**

By [[Thm - Conditions for a Square Matrix to be Invertible|invertibility theorem]], it suffices to show that the columns of $A^T A$ are linearly independent, i.e., $A^T A x = 0 \Rightarrow x = 0$.

> [!note]- Derivation
> Suppose $A^T A x = 0$. Multiply on the left by $x^T$:
> $$x^T A^T A x = x^T \cdot 0 = 0.$$
> But $x^T A^T A x = (Ax)^T(Ax) = \|Ax\|^2$. So $\|Ax\|^2 = 0$, hence $Ax = 0$ (since the norm is zero iff the vector is zero).
>
> By hypothesis, the columns of $A$ are linearly independent, so $Ax = 0 \Rightarrow x = 0$. Hence $A^T A x = 0 \Rightarrow x = 0$, which means $A^T A$ has linearly independent columns and so is invertible.

**Step 2: $A^\dagger$ is a left inverse of $A$.**

Direct computation.

> [!note]- Derivation
> $$A^\dagger A = \big[(A^T A)^{-1} A^T\big] A = (A^T A)^{-1} (A^T A) = I_n,$$
> using associativity to bracket $A^T A$, then the definition of the matrix inverse.

**Step 3: $\hat x = A^\dagger b$ minimises $\|Ax - b\|^2$.**

The least-squares objective is a convex quadratic; the unique minimiser is found by setting the gradient to zero.

> [!note]- Derivation
> Define $f(x) = \|Ax - b\|^2 = (Ax - b)^T (Ax - b)$. Expanding:
> $$f(x) = x^T A^T A x - 2 b^T A x + b^T b.$$
> This is a convex quadratic in $x$ (since $A^T A$ is positive semidefinite — in fact, positive definite by Step 1), so it has a unique global minimum. The gradient is
> $$\nabla f(x) = 2 A^T A x - 2 A^T b.$$
> Setting $\nabla f = 0$:
> $$A^T A x = A^T b. \quad (\star)$$
> These are the **normal equations**. Solving (using $A^T A$ invertible from Step 1):
> $$\hat x = (A^T A)^{-1} A^T b = A^\dagger b. \quad \checkmark$$
>
> *Orthogonality interpretation.* Equation $(\star)$ can be rewritten as $A^T(b - A\hat x) = 0$, which says the **residual** $r = b - A\hat x$ is orthogonal to every column of $A$. Geometrically, the residual is in the orthogonal complement of the column space, and $A\hat x$ is the orthogonal projection of $b$ onto the column space.
>
> *Verification of minimality.* Direct substitution: for any $x \in \mathbb R^n$, write $x = \hat x + d$ where $d = x - \hat x$. Then
> $$\|Ax - b\|^2 = \|A(\hat x + d) - b\|^2 = \|(A\hat x - b) + Ad\|^2 = \|A\hat x - b\|^2 + 2(A\hat x - b)^T(Ad) + \|Ad\|^2.$$
> The cross term is $2 d^T A^T(A\hat x - b) = -2 d^T A^T(b - A\hat x) = 0$ by the orthogonality condition. So
> $$\|Ax - b\|^2 = \|A\hat x - b\|^2 + \|Ad\|^2 \geq \|A\hat x - b\|^2,$$
> with equality iff $Ad = 0$, iff $d = 0$ (by linear independence of columns), iff $x = \hat x$. So $\hat x$ is the unique global minimiser.

> [!note]- Complete formal solution
> Let $A \in \mathbb R^{m \times n}$ with $m \geq n$ and linearly independent columns.
>
> *Step 1: $A^T A$ is invertible.* Suppose $A^T A x = 0$. Then $x^T A^T A x = \|A x\|^2 = 0$, so $A x = 0$. By linear independence of columns, $x = 0$. Hence $A^T A x = 0 \Rightarrow x = 0$, so $A^T A$ has linearly independent columns and (by [[Thm - Conditions for a Square Matrix to be Invertible|the invertibility theorem]]) is invertible. The pseudoinverse $A^\dagger = (A^T A)^{-1} A^T$ is well-defined.
>
> *Step 2: $A^\dagger$ is a left inverse.* $A^\dagger A = (A^T A)^{-1} A^T A = (A^T A)^{-1}(A^T A) = I_n$.
>
> *Step 3: $\hat x = A^\dagger b$ minimises $\|Ax - b\|^2$.* Expand:
> $$\|A x - b\|^2 = x^T A^T A x - 2 b^T A x + \|b\|^2.$$
> Set the gradient to zero: $\nabla = 2 A^T A x - 2 A^T b = 0$, giving $A^T A x = A^T b$. Since $A^T A$ is invertible, $\hat x = (A^T A)^{-1} A^T b = A^\dagger b$ is the unique solution.
>
> *Orthogonality.* The normal equations $A^T A \hat x = A^T b$ rewrite as $A^T(b - A\hat x) = 0$. So $b - A\hat x$ is orthogonal to every column of $A$, i.e., to the entire column space. Geometrically, $A\hat x$ is the orthogonal projection of $b$ onto the column space.
>
> *Minimality verification.* For any $x = \hat x + d$,
> $$\|Ax - b\|^2 = \|A\hat x - b\|^2 + 2 d^T A^T(A\hat x - b) + \|Ad\|^2 = \|A\hat x - b\|^2 + \|Ad\|^2,$$
> using $A^T(b - A\hat x) = 0$. Since $\|Ad\|^2 \geq 0$ with equality only when $d = 0$ (by linear independence), $\hat x$ is the unique global minimiser. $\quad\blacksquare$

---

# Key Takeaways

**The pseudoinverse $A^\dagger = (A^T A)^{-1} A^T$ is the canonical left inverse of a tall full-rank matrix, and it solves least-squares automatically.** The exercise reveals the structural reason: $A^\dagger$ is constructed precisely to solve the normal equations $A^T A x = A^T b$, which are the first-order conditions for minimising $\|Ax - b\|^2$. The trigger-reaction pattern: when you encounter an over-determined system $Ax = b$ (more equations than unknowns, no exact solution), the standard move is to compute $\hat x = A^\dagger b$, which gives the *least-squares* solution — the one minimising the residual norm. This is the foundation of regression, statistical estimation, and engineering parameter-fitting.

**Orthogonality of the residual to the column space is the geometric characterisation of least-squares.** The residual $r = b - A\hat x$ must be orthogonal to the column space of $A$: $A^T r = 0$. Geometrically, $A\hat x$ is the **orthogonal projection** of $b$ onto $\operatorname{col}(A)$ — the closest point in the column space to $b$, in the Euclidean distance. This geometric picture is the most compressing way to remember least-squares: the answer is the projection, period. The pseudoinverse formula $A^\dagger = (A^T A)^{-1} A^T$ is the *computation* of this projection in coordinates. Algorithms in practice use [[Thm - QR Factorization via Gram-Schmidt (Boyd)|QR factorization]] $A = QR$ and compute $\hat x = R^{-1} Q^T b$, which is numerically more stable than forming $A^T A$ (whose condition number is the *square* of $A$'s).

**The pseudoinverse trick converts "no exact solution" into "the best approximate solution".** Over-determined systems generically have no exact solution: the equations are inconsistent. Rather than concluding "this problem is unsolvable", the least-squares approach reframes the question as "what is the $x$ that comes closest to satisfying all the equations simultaneously?" The answer — the pseudoinverse — is *always* well-defined as long as the columns of $A$ are linearly independent. This conversion from exact-solvability to approximate-solvability is one of the most important conceptual moves in applied mathematics. It turns ill-posed problems (over-determined systems) into well-posed ones (minimisation problems), and it does so in a principled way (orthogonality of the residual). The same idea generalises to ridge regression, total least squares, regularised problems, and the entire field of optimisation under uncertainty.

---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Polynomial over a Field"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $D : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$ be the differentiation operator $Dp = p'$. Find all eigenvalues and eigenvectors of $D$.

(Optional refinement: consider also $D$ acting on the finite-dimensional [[Def - Subspace|subspace]] $\mathcal{P}_n(\mathbb{R})$ of polynomials of degree at most $n$.)

**Recall:**

A polynomial over $\mathbb{R}$ is a finite formal expression $p(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_m x^m$ with real coefficients. The **degree** of $p$ is the largest $k$ with $a_k \neq 0$. See [[Def - Polynomial over a Field]].

An **eigenvalue** of an operator $T$ on $V$ is a scalar $\lambda$ such that there exists a nonzero $v \in V$ with $Tv = \lambda v$; the vector $v$ is the corresponding **eigenvector**. See [[Def - Eigenvalue and Eigenvector]].

![[Def - Eigenvalue and Eigenvector#The Definition]]

The differentiation operator is defined by $D(\sum_k a_k x^k) = \sum_k k a_k x^{k-1}$ — linear and decreases the degree by $1$ (for nonzero polynomials of positive degree). On constants, $D$ acts as zero.

---

# Convergent Strategy

**Problem class.** This is the chapter's prototype "find the eigenvalues of a concrete operator" problem — the simplest instance of the [[Linear Algebra V — §4–5 Polynomials and Eigenvalues#Problem-Solving Strategy|problem-solving strategy]] for finding eigenvalues of an explicit operator. The operator $D$ has a clean degree-decreasing structure, so the eigenvalue equation $Dp = \lambda p$ produces a sharp degree constraint that nearly solves the problem.

**Assumption pattern.** The recognisable signal is that $D$ acts on polynomials by *strictly lowering* the degree (for non-constant polynomials). This is the structural feature that drives the analysis: if $p$ has degree $\geq 1$, then $\deg(Dp) = \deg p - 1 < \deg p$, so $Dp$ cannot be a scalar multiple of $p$ (which would have the same degree). The only escape is $\deg p = 0$ (constants), where $Dp = 0$, putting the equation $\lambda p = 0$.

**Theorem routing.** Direct application of the definition of eigenvalue/eigenvector. No big theorem needed — the structural fact "degree decreases under $D$" is enough. Equivalently, one could compute the minimal polynomial of $D$ on $\mathcal{P}_n(\mathbb{R})$ (the finite-dimensional case): $D^{n+1} = 0$ on $\mathcal{P}_n$ (each application lowers degree by $1$, and after $n+1$ applications all polynomials of degree $\leq n$ are killed) and $D^n \neq 0$ (since $D^n(x^n) = n!$), so $m_D = z^{n+1}$ — root $0$ with multiplicity $n+1$. By [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]], $0$ is the only eigenvalue. This is the canonical demonstration that an operator can have *one* eigenvalue with *one-dimensional* eigenspace but high algebraic multiplicity — the textbook example of non-diagonalisable.

**Key decision point.** The non-obvious move (and there is barely one) is to recognise that the equation $Dp = \lambda p$ comparing *degrees* gives all the constraints needed: for $\lambda \neq 0$, both sides should have the same degree, but $\deg(Dp) = \deg p - 1$ while $\deg(\lambda p) = \deg p$ — impossible unless $p = 0$. The case $\lambda = 0$ has $Dp = 0$, which says $p$ is a constant, and any nonzero constant works.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra V — §4–5 Polynomials and Eigenvalues#Legal Operations|the topic page's Legal Operations]]:

1. **Compute the minimal polynomial by the iterate algorithm** (operation 3 from the topic page). For the finite-dimensional case $\mathcal{P}_n(\mathbb{R})$, observe that $D^{n+1}$ annihilates everything (degree-decrease principle), and $D^k$ does not for $k \leq n$. So $m_D = z^{n+1}$.

2. **Translate operator equations to divisibility of $m_T$** (operation 4). $D^{n+1} = 0$ tells us $m_D \mid z^{n+1}$, hence $m_D = z^k$ for some $k$; lower powers fail, forcing $k = n+1$.

---

# Hints

> [!note]- Hint 1
> Compare degrees of $Dp$ and $\lambda p$. What constraint does the equation $Dp = \lambda p$ put on the degree of $p$?

> [!note]- Hint 2
> If $p$ has degree $\geq 1$, the equation $Dp = \lambda p$ forces $\deg Dp = \deg(\lambda p)$, i.e. $\deg p - 1 = \deg p$ — impossible. So $p$ must have degree $0$ (be a constant).

> [!note]- Hint 3
> A nonzero constant $c$ satisfies $Dc = 0 = 0 \cdot c$. So $0$ is an eigenvalue with the nonzero constants as eigenvectors. Are there any others?

---

# Solution

The plan is to compare degrees in the equation $Dp = \lambda p$, eliminating all $\lambda \neq 0$ by a degree-count argument, then identify the $\lambda = 0$ eigenspace as the constants.

**Step 1: For $\lambda \neq 0$, the eigenvalue equation has no solution.**

The only $\lambda \in \mathbb{R}$ that can be an eigenvalue is $\lambda = 0$.

> [!note]- Derivation
> Suppose $\lambda \in \mathbb{R}$ is a (potential) eigenvalue of $D$ with eigenvector $p$, so $p \neq 0$ and $Dp = \lambda p$.
>
> **Case 1: $\lambda \neq 0$.** Then $\lambda p \neq 0$, so $Dp \neq 0$, so $p$ is not constant. Hence $\deg p \geq 1$. The differentiation operator satisfies $\deg(Dp) = \deg p - 1$ for any nonzero polynomial of positive degree (the leading term $a_m x^m$ becomes $m a_m x^{m-1}$, with $m a_m \neq 0$ in characteristic $0$). So
> $$\deg(Dp) = \deg p - 1.$$
> Meanwhile $\deg(\lambda p) = \deg p$ (multiplication by a nonzero scalar preserves degree). So the equation $Dp = \lambda p$ becomes $\deg p - 1 = \deg p$, i.e. $-1 = 0$ — contradiction. So no $\lambda \neq 0$ can be an eigenvalue.
>
> **Case 2: $\lambda = 0$.** The equation $Dp = 0 \cdot p = 0$ says $p$ is a polynomial with zero derivative, i.e. $p$ is constant. Conversely, any nonzero constant $c$ satisfies $Dc = 0 = 0 \cdot c$, so $c$ is an eigenvector for $\lambda = 0$.

**Step 2: The eigenspace $E(0, D)$ is the one-dimensional space of nonzero constants.**

$E(0, D) = \ker D = \mathbb{R} \cdot 1 = \{c : c \in \mathbb{R}\}$, the constant polynomials.

> [!note]- Derivation
> $\ker D = \{p \in \mathcal{P}(\mathbb{R}) : p' = 0\}$. A polynomial $p(x) = a_0 + a_1 x + \cdots + a_m x^m$ has derivative $p'(x) = a_1 + 2 a_2 x + \cdots + m a_m x^{m-1}$. For $p' = 0$, all coefficients $a_1, 2 a_2, \ldots, m a_m$ must vanish, hence $a_k = 0$ for $k \geq 1$. So $p = a_0$ is constant.
>
> Conversely, every constant satisfies $p' = 0$, hence $\ker D =$ the space of constants, which is one-dimensional as a real vector space.

> [!note]- Complete formal solution
> Let $D : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$ be defined by $Dp = p'$.
>
> *Claim 1: $0$ is an eigenvalue of $D$ with eigenspace the nonzero constants.* The constant polynomial $1 \in \mathcal{P}(\mathbb{R})$ is nonzero and satisfies $D(1) = 0 = 0 \cdot 1$, so $0$ is an eigenvalue with eigenvector $1$. The eigenspace $E(0, D) = \ker D = \{p : p' = 0\} = \{c \in \mathbb{R} : c \text{ a constant polynomial}\} = \mathbb{R}$.
>
> *Claim 2: No $\lambda \neq 0$ is an eigenvalue of $D$.* Suppose $\lambda \in \mathbb{R}$ with $\lambda \neq 0$ and $p \in \mathcal{P}(\mathbb{R})$ with $p \neq 0$ satisfies $Dp = \lambda p$. Since $\lambda p \neq 0$, $Dp \neq 0$, so $p$ is not constant, hence $\deg p \geq 1$. The differentiation operator strictly decreases degree: $\deg(Dp) = \deg p - 1$ for any non-constant polynomial. On the other hand $\deg(\lambda p) = \deg p$. So $\deg p - 1 = \deg p$, contradiction. So no such $\lambda$ exists.
>
> Therefore the eigenvalues of $D$ are exactly $\{0\}$, with eigenspace $E(0, D) = \mathbb{R}$ (the constant polynomials). $\blacksquare$

> [!note]- Alternative via the minimal polynomial on $\mathcal{P}_n(\mathbb{R})$
> Restrict $D$ to the finite-dimensional space $\mathcal{P}_n(\mathbb{R})$. Compute the minimal polynomial. Since $D$ lowers degree by $1$, $D^{n+1}(p) = 0$ for any $p \in \mathcal{P}_n(\mathbb{R})$ (after $n+1$ applications, every polynomial of degree $\leq n$ is killed). So $m_D \mid z^{n+1}$, meaning $m_D = z^k$ for some $k \leq n+1$.
>
> The smallest such $k$ is the smallest exponent for which $D^k = 0$. But $D^n(x^n) = n!$ (the constant polynomial), which is nonzero. So $D^n \neq 0$ and $m_D \neq z^k$ for $k \leq n$. Hence $m_D = z^{n+1}$.
>
> By [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]], the eigenvalues of $D$ are the roots of $m_D = z^{n+1}$, which is just $\{0\}$. So $0$ is the only eigenvalue, with $E(0, D) = \ker D =$ constants — a one-dimensional eigenspace, despite the algebraic multiplicity being $n+1$.

---

# Key Takeaways

**Trigger: "find eigenvalues of a degree-decreasing operator" → eigenvalue must be zero.** The differentiation operator on polynomials illustrates a general pattern: any linear operator $T$ on an infinite-dimensional polynomial-like space that *strictly lowers* a graded structure — degree, total degree, weight, level — can only have $0$ as an eigenvalue. The reason is the degree-count argument: $Tp = \lambda p$ with $\lambda \neq 0$ forces $T$ to preserve the grading on $p$, but $T$ strictly lowers it. The kernel — where $T$ acts as $0$ — gives the eigenspace for the eigenvalue $0$. This pattern recurs in many graded-operator settings: differentiation, boundary operators in algebraic topology (where $\partial^2 = 0$), step-down operators in representation theory. In each case the eigenvalues collapse to zero, and the eigenspace is the "grade-zero" part.

**Eigenspace [[Def - Dimension|dimension]] can be much smaller than the [[Def - Dimension|dimension]] of the space — the prototype of non-diagonalisable operator.** The differentiation operator on $\mathcal{P}_n(\mathbb{R})$ has dimension $n+1$ but eigenspace of dimension $1$. So we have many "modes" being killed by $D^{n+1}$ but only one of them is an honest eigenvector. The other $n$ are *generalised eigenvectors* — vectors killed by some power $D^k$ for $k > 1$ but not by $D^1$. This is the prototypical example of a non-diagonalisable operator: the algebraic multiplicity of $0$ (in the minimal polynomial $z^{n+1}$) is $n+1$, but the geometric multiplicity (the dimension of the eigenspace) is just $1$. The full structural description requires generalised eigenspaces (Linear Algebra VIII) and the [[Thm - Jordan Normal Form|Jordan form]] ([[Def - Module|Modules]] II): $D$ is a *single* Jordan block of size $n+1$ at the eigenvalue $0$.

**The degree-decrease argument is more general than it looks.** The same argument works for the **right-shift operator** on $\mathbb{F}^\infty$ ($S(z_1, z_2, \ldots) = (0, z_1, z_2, \ldots)$), which has no eigenvalues at all (Exercise 19 of LADR §5A) — because "right-shift" strictly increases the position of the first nonzero entry. The same argument works for various **nilpotent operators** in graded settings — these operators have only $0$ as an eigenvalue, and (over $\mathbb{C}$) decompose as direct sums of nilpotent Jordan blocks. The pattern is: a "graded shift" operator either has no eigenvalues (if it never hits a stationary direction) or has $0$ as its only eigenvalue (if a graded zero [[Def - Subspace|subspace]] is preserved).

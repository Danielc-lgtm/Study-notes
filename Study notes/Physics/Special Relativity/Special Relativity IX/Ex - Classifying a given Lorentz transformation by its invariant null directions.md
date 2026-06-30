---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Classification of Restricted Lorentz Transformations"
  - "Thm - Invariant Null Direction of a Restricted Lorentz Transformation"
  - "Thm - Eigenvalues and Eigenvectors of a Lorentz Boost"
tags: [physics, special-relativity]
---

# Problem Statement

Classify each of the following restricted Lorentz transformations (matrices in the orthonormal basis $(e_0,e_1,e_2,e_3)$) by finding its invariant null directions, computing its trace, and naming its type (boost, spatial rotation, four-screw, or null rotation):

$$
\Lambda_A = \begin{pmatrix} \cosh\psi & \sinh\psi & 0 & 0 \\ \sinh\psi & \cosh\psi & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \quad
\Lambda_B = \begin{pmatrix} \cosh\psi & \sinh\psi & 0 & 0 \\ \sinh\psi & \cosh\psi & 0 & 0 \\ 0 & 0 & \cos\theta & -\sin\theta \\ 0 & 0 & \sin\theta & \cos\theta \end{pmatrix}, \quad
\Lambda_C = \begin{pmatrix} 1 + 2\alpha^2 & -2\alpha^2 & 2\alpha & 0 \\ 2\alpha^2 & 1 - 2\alpha^2 & 2\alpha & 0 \\ 2\alpha & -2\alpha & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix},
$$
with $\psi, \theta \ne 0$ and $\alpha > 0$. For each, state the number of invariant null directions and extract the rapidity and/or rotation angle from the trace.

**Recall:**

![[Def - Classification of Restricted Lorentz Transformations#The Definition]]

A restricted transformation has two distinct invariant null directions iff it is a four-screw (boost and rotation in orthogonal planes; boosts and rotations are the degenerate cases), one iff it is a null rotation, three or more iff it is the identity. The trace gives $\cosh\psi = \tfrac12\mathrm{tr}\,\Lambda - 1$ for a boost, $\cos\theta = \tfrac12\mathrm{tr}\,\Lambda - 1$ for a rotation; a four-screw has $\mathrm{tr}\,\Lambda = 2\cosh\psi + 2\cos\theta$; a null rotation has $\mathrm{tr}\,\Lambda = 4$.

---

# Convergent Strategy

**Problem class.** A *classification* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: given an explicit restricted matrix, find its invariant null directions, count them, and read off the type. The trace provides a cross-check on the parameters.

**Assumption pattern.** Each matrix is given explicitly, so the invariant null directions are found by solving $\Lambda(\ell) = \lambda\ell$ with $\ell\cdot\ell = 0$. The number of solutions — one or two — distinguishes the null rotation from the four-screw, and the degenerate four-screws (boost, rotation) are identified by which of $\psi, \theta$ is zero.

**Theorem routing.** The count routes through the [[Def - Classification of Restricted Lorentz Transformations|classification]]: two null directions $\Rightarrow$ four-screw (here $\Lambda_B$); a single one $\Rightarrow$ null rotation ($\Lambda_C$); the degenerate four-screw with $\theta = 0$ is a boost ($\Lambda_A$), whose null eigenvectors are the Doppler-factor eigenvectors of [[Thm - Eigenvalues and Eigenvectors of a Lorentz Boost|the boost-eigenvalue theorem]]. The trace cross-checks: $\mathrm{tr}\,\Lambda_A = 2\cosh\psi + 2$, $\mathrm{tr}\,\Lambda_B = 2\cosh\psi + 2\cos\theta$, $\mathrm{tr}\,\Lambda_C = 4$.

**Key decision point.** The non-obvious choice is to look for *null* eigenvectors specifically, not all real eigenvectors. A four-screw has two real null eigenvectors (in its boost plane) but also two complex ones (in its rotation plane); a null rotation has a single null eigenvector despite the eigenvalue $1$ having high algebraic multiplicity. The count that classifies is the number of *real null directions* fixed, which is one or two, never the total eigenvalue multiplicity.

---

# Legal Operations Used

1. **Find an invariant null direction** (operation 3 from the topic page): solve $\Lambda(\ell) = \lambda\ell$ with $\ell\cdot\ell = 0$ for each matrix.

2. **Count invariant null directions to name the type** (operation 5 from the topic page): one $\Rightarrow$ null rotation, two $\Rightarrow$ four-screw.

3. **Use the trace to extract the parameter** (operation 6 from the topic page): $\tfrac12\mathrm{tr}\,\Lambda - 1$ gives $\cosh\psi$ or $\cos\theta$.

---

# Hints

> [!note]- Hint 1
> For each matrix, try the candidate null vectors $\ell_\pm = e_0 \pm e_1$ first — they are the light-cone generators of the $(e_0,e_1)$-plane and the natural eigenvector candidates for a transformation acting there.

> [!note]- Hint 2
> $\Lambda_A$: a boost, $\theta = 0$. $\Lambda_B$: boost-block times rotation-block — count null directions in each. $\Lambda_C$: this is the null-rotation matrix from the classification; find which single null direction it fixes.

> [!note]- Hint 3
> Compute the trace of each and apply $\cosh\psi = \tfrac12\mathrm{tr} - 1$ (boost), $\cos\theta = \tfrac12\mathrm{tr} - 1$ (rotation). For $\Lambda_C$, the trace is $4$, the signature of a null rotation (or the identity).

---

# Solution

We classify each matrix in turn by solving for null eigenvectors and computing the trace.

**Step 1: $\Lambda_A$ is a boost (two null directions, $\theta = 0$).**

> [!note]- Derivation
> Apply $\Lambda_A$ to $\ell_\pm = e_0 \pm e_1$: $\Lambda_A(e_0 + e_1) = (\cosh\psi + \sinh\psi)(e_0 + e_1) = e^\psi(e_0+e_1)$ and $\Lambda_A(e_0 - e_1) = e^{-\psi}(e_0 - e_1)$. Both $\ell_\pm$ are null ($\ell_\pm\cdot\ell_\pm = 0$), so there are (at least) **two** invariant null directions $\mathrm{Span}(e_0\pm e_1)$. Any other null direction $\ell = (1, \mathbf{n})$ with $\mathbf{n}$ not along $e_1$ is not fixed (the boost moves it), so exactly two. Two invariant null directions $\Rightarrow$ four-screw, and since the lower block is the identity ($\theta = 0$), $\Lambda_A$ is a **boost** of rapidity $\psi$. Trace: $\mathrm{tr}\,\Lambda_A = 2\cosh\psi + 2$, so $\cosh\psi = \tfrac12\mathrm{tr}\,\Lambda_A - 1$. ✓

**Step 2: $\Lambda_B$ is a four-screw (two null directions, $\psi, \theta \ne 0$).**

> [!note]- Derivation
> $\Lambda_B$ is block-diagonal: a boost on $\mathrm{Span}(e_0,e_1)$ and a rotation on $\mathrm{Span}(e_2,e_3)$. The boost block fixes the two null directions $\mathrm{Span}(e_0\pm e_1)$ exactly as in Step 1 ($\Lambda_B(e_0\pm e_1) = e^{\pm\psi}(e_0\pm e_1)$, with the rotation block leaving these untouched since they have no $e_2, e_3$ components). The rotation block (with $\theta \ne 0, \pi$) has *complex* eigenvalues $e^{\pm i\theta}$, so it contributes no real null directions. Hence exactly **two** invariant null directions. Two distinct null directions with $\psi, \theta \ne 0$ $\Rightarrow$ **four-screw**. Trace: $\mathrm{tr}\,\Lambda_B = 2\cosh\psi + 2\cos\theta$. The boost rapidity is recovered as $\cosh\psi$ from the $(e_0,e_1)$ block and the rotation angle as $\cos\theta$ from the $(e_2,e_3)$ block; the trace alone does not separate them, but the block structure does. ✓

**Step 3: $\Lambda_C$ is a null rotation (one null direction).**

> [!note]- Derivation
> This is the null-rotation matrix from the classification (parameters $\psi = \theta = 0$, $\alpha > 0$). Apply it to $\ell_+ = e_0 + e_1$:
> $$\Lambda_C(e_0 + e_1) = \begin{pmatrix} (1+2\alpha^2) + (-2\alpha^2) \\ 2\alpha^2 + (1 - 2\alpha^2) \\ 2\alpha + (-2\alpha) \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix} = e_0 + e_1,$$
> so $\mathrm{Span}(e_0 + e_1)$ is fixed with eigenvalue $1$. Is there another? Try $\ell_- = e_0 - e_1$: $\Lambda_C(e_0 - e_1) = \big((1+2\alpha^2)-(-2\alpha^2),\ 2\alpha^2 - (1-2\alpha^2),\ 2\alpha - (-2\alpha),\ 0\big) = (1 + 4\alpha^2,\ -1 + 4\alpha^2,\ 4\alpha,\ 0)$, which is *not* proportional to $\ell_-$ (it has a nonzero $e_2$-component). A systematic search for null eigenvectors of $\Lambda_C$ finds only $\mathrm{Span}(e_0 + e_1)$. Hence exactly **one** invariant null direction $\Rightarrow$ **null rotation**. Trace: $\mathrm{tr}\,\Lambda_C = (1+2\alpha^2) + (1-2\alpha^2) + 1 + 1 = 4$, the null-rotation signature (and $\ne$ identity since $\alpha > 0$, confirmed by $\Lambda_C \ne \mathrm{Id}$). Confirm the Jordan structure: $N = \Lambda_C - \mathrm{Id}$ has $N(e_0+e_1) = 0$, $N(e_2) = 2\alpha(e_0+e_1)$, $N(k) = N(e_0 - e_1) = (4\alpha^2, 4\alpha^2, 4\alpha, 0) = 4\alpha^2(e_0+e_1) + 4\alpha e_2$ (wait: $N(e_0-e_1) = \Lambda_C(e_0-e_1) - (e_0-e_1) = (4\alpha^2, 4\alpha^2, 4\alpha, 0)$), so $N^2(e_0 - e_1) = N(4\alpha^2(e_0+e_1) + 4\alpha e_2) = 4\alpha\cdot 2\alpha(e_0+e_1) = 8\alpha^2(e_0+e_1) \ne 0$ and $N^3(e_0-e_1) = 0$: a single Jordan block of size three. ✓

> [!note]- Complete formal solution
> $\Lambda_A$: $\Lambda_A(e_0\pm e_1) = e^{\pm\psi}(e_0\pm e_1)$, two invariant null directions, lower block identity ($\theta = 0$) — a **boost** of rapidity $\psi$, $\mathrm{tr} = 2\cosh\psi + 2$.
>
> $\Lambda_B$: boost block fixes $\mathrm{Span}(e_0\pm e_1)$ (two null directions), rotation block has complex eigenvalues $e^{\pm i\theta}$ (no real null directions) — a **four-screw** of rapidity $\psi$ and angle $\theta$, $\mathrm{tr} = 2\cosh\psi + 2\cos\theta$.
>
> $\Lambda_C$: fixes only $\mathrm{Span}(e_0+e_1)$ among null directions, $N = \Lambda_C - \mathrm{Id}$ nilpotent of index three — a **null rotation** of parameter $\alpha$, $\mathrm{tr} = 4$. $\blacksquare$

---

# Key Takeaways

**Classification is a count of real null directions, not a count of eigenvalues.** The decisive datum is how many *real null* directions a transformation fixes — one (null rotation) or two (four-screw) — and this is found by solving $\Lambda(\ell) = \lambda\ell$ with the null constraint $\ell\cdot\ell = 0$, not by tallying eigenvalue multiplicities. A four-screw has eigenvalues $e^{\pm\psi}, e^{\pm i\theta}$ (four distinct, two real on null directions, two complex), while a null rotation has the single eigenvalue $1$ of algebraic multiplicity four but only one null eigenvector. The trigger "classify a restricted transformation" should fire the move "find the real null eigenvectors and count them," because the count is the classification. The light-cone generators $\ell_\pm = e_0\pm e_1$ of any boost plane are the natural first candidates to test.

**The trace is a fast type-detector, and the value $4$ flags the null-rotation/identity boundary.** Computing $\mathrm{tr}\,\Lambda$ immediately narrows the type: a value greater than $4$ forces a boost or four-screw with a real hyperbolic part ($\cosh\psi > 1$); a value less than $4$ forces a rotation-dominated type; and exactly $4$ flags either the identity or a null rotation (since a null rotation has $\mathrm{tr} = 4$). The trace formulas $\cosh\psi = \tfrac12\mathrm{tr} - 1$ and $\cos\theta = \tfrac12\mathrm{tr} - 1$ then extract the parameter once the type is known. The reusable diagnostic: compute the trace first, and if it is $4$, check whether the matrix is the identity to distinguish the null rotation. This is the cheapest possible classification step, requiring no eigenvector computation.

**A null rotation is detected by the nilpotency of $\Lambda - \mathrm{Id}$.** When a transformation has a single invariant null direction and trace $4$, the confirming computation is that $N = \Lambda - \mathrm{Id}$ is nilpotent of index three: $N^3 = 0$ but $N^2 \ne 0$. This is the algebraic fingerprint that distinguishes a null rotation from every other restricted transformation — no boost, rotation, or four-screw has a nontrivial nilpotent part, because they are all diagonalisable (semisimple). The trigger "trace $4$, one null direction, not the identity" should fire the check "$N^2 \ne 0$, $N^3 = 0$," confirming the size-three Jordan block. This nilpotency is what makes the null rotation the parabolic, non-diagonalisable element of the classification, and it generalises to the recognition of any parabolic transformation by the nilpotency of (matrix minus identity).

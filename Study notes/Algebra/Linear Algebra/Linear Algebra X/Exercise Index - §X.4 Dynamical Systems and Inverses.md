---
type: exercise-index
subject: linear-algebra
section: "X.4"
tags: [algebra, linear-algebra, applied]
---

## §X.4 Dynamical Systems and Inverses — Exercises

The exercises of §X.4 bring together the topic's biggest themes: time evolution via linear dynamical systems, the composition of linear functions as matrix multiplication, the QR factorization for orthogonalisation and solving linear systems, and the various notions of matrix inverse (left, right, two-sided, pseudo-). The targets are: (a) set up linear dynamical systems for applied phenomena and simulate forward in time; (b) verify the conditions for a square matrix to be invertible and compute inverses for small examples; (c) use the [[Def - Pseudoinverse|pseudoinverse]] to solve over- and under-determined systems; (d) apply QR factorization to solve linear systems numerically.

- [[Ex - Population dynamics matrix as a linear dynamical system]] (⭐⭐) — set up the Boyd population dynamics model as $x_{t+1} = A x_t$ from given birth and death rates, and verify by computing one step forward from a given initial age distribution ([[Def - Linear Dynamical System]])
- [[Ex - Existence of a left inverse forces linear independence of columns]] (⭐) — one-line proof that if $A$ has a left inverse $C$, then $Ax = 0 \Rightarrow x = 0$, using associativity and the cancellation $CA = I$ ([[Def - Left and Right Inverse of a Matrix]])
- [[Ex - Pseudoinverse for least squares (Boyd)]] (⭐⭐) — show that for a tall full-rank $A$, the [[Def - Pseudoinverse|pseudoinverse]] $A^\dagger = (A^T A)^{-1} A^T$ is a left inverse and that $\hat x = A^\dagger b$ minimises $\|Ax - b\|^2$, via the orthogonality condition $A^T(b - A\hat x) = 0$ ([[Def - Left and Right Inverse of a Matrix]], [[Def - Norm and Distance]])
- **(Boyd Ex 9.1)** Compartmental system: write the $3 \times 3$ dynamics matrix for a compartmental model with three compartments and the given inter-compartment transfer rates ($10\%$ flow between certain pairs, $5\%$ for others), and verify that each row sum equals $1$ minus the elimination rate (so that "stuff is conserved minus elimination"). (⭐⭐, [[Def - Linear Dynamical System]])
- **(Boyd Ex 9.3)** Equilibrium point: for the time-invariant linear dynamical system $x_{t+1} = A x_t + c$, find the linear system $Fz = g$ that characterises equilibrium points. The answer is $F = I - A$, $g = c$: equilibria solve $(I - A)z = c$. The equation has a unique solution iff $I - A$ is invertible, iff $A$ has no eigenvalue equal to $1$. (⭐, [[Def - Linear Dynamical System]], [[Thm - Conditions for a Square Matrix to be Invertible]])
- **(Boyd Ex 9.4)** Reduce a $2$-Markov model to a standard linear dynamical system: given $x_{t+1} = A_1 x_t + A_2 x_{t-1}$, define $z_t = (x_t, x_{t-1})$ and write the augmented dynamics $z_{t+1} = B z_t$ for an explicit $2n \times 2n$ matrix $B$. (⭐⭐, [[Def - Linear Dynamical System]])
- **(Boyd Ex 9.5)** Fibonacci sequence as a linear dynamical system: the Fibonacci recurrence $y_{t+1} = y_t + y_{t-1}$ is a $2$-Markov system; reduce to a standard LDS with state $(y_t, y_{t-1})$ and dynamics matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$. Simulate by hand up to $y_{10}$. The eigenvalues are the golden ratio $\phi$ and $1 - \phi$. (⭐⭐, [[Def - Linear Dynamical System]])
- **(Boyd Ex 10.6)** Product of rotation matrices in $\mathbb R^2$: let $A, B$ be rotations by $\theta$ and $\omega$. Compute $AB$ and verify it is the rotation by $\theta + \omega$. Show $AB = BA$, contrasting with the general non-commutativity of matrix multiplication. (⭐, [[Thm - Block Matrix Multiplication]])

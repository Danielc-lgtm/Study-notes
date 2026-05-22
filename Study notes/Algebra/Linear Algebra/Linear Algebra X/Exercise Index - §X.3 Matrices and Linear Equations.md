---
type: exercise-index
subject: linear-algebra
section: "X.3"
tags: [algebra, linear-algebra, applied]
---

## §X.3 Matrices and Linear Equations — Exercises

The exercises of §X.3 introduce matrices as the structural language for vector-valued linear and affine functions, and exhibit them in the recurring applied examples: geometric transformations, selectors and permutations, incidence matrices for networks, and convolution. Linear equations $Ax = b$ enter as the central problem, with the classification into over-, exactly-, and under-determined systems setting up the algorithmic regimes of the next section. The targets are: (a) recognise and construct matrices for given linear or affine functions; (b) verify properties of structured matrices (transpose, symmetry, sparsity); (c) translate graph problems into incidence-matrix questions; (d) set up linear-equation models for real-world phenomena (polynomial interpolation, chemical balancing, flow conservation).

- **(Boyd Ex 7.1)** Projection onto a line: given a line through the origin in $\mathbb R^2$ at angle $\theta$ from horizontal, find the $2 \times 2$ matrix $A$ such that $P(x) = Ax$ is the projection of $x$ onto the line. Use the formula $P(x) = (x^T \hat u)\hat u$ where $\hat u$ is a unit vector along the line; verify $A$ is symmetric and satisfies $A^2 = A$. (⭐⭐, [[Def - Affine and Linear Functions on Rn]])
- **(Boyd Ex 7.2)** Rotation in 3-D: find the $3 \times 3$ matrix $A$ for rotation about the $z$-axis (the vertical axis $e_3$) by $45°$ counterclockwise. The columns of $A$ are $f(e_1), f(e_2), f(e_3)$ where $f$ is the rotation. Verify $A$ is orthogonal. (⭐, [[Def - Affine and Linear Functions on Rn]])
- **(Boyd Ex 7.6)** Rows of incidence matrix: show that for any directed graph, the rows of the incidence matrix are linearly dependent. The proof is one line: their sum is the zero row, since every edge has exactly one $+1$ and one $-1$, summing to zero in each column. (⭐, [[Def - Incidence Matrix]])
- **(Boyd Ex 7.10)** Circle graph: for the cycle graph with $n$ vertices in a single closed loop, give the incidence matrix, describe all circulations $f$ (i.e., $f$ with $Af = 0$), and compute the Dirichlet energy $\|A^T v\|^2$ for a given potential $v$. (⭐⭐, [[Def - Incidence Matrix]])
- **(Boyd Ex 7.14)** Rainfall and river height: interpret the convolution relation $h = g \ast r$ between rainfall $r$ and river height $h$ in English, naming the delay structure encoded by the kernel $g = (0.1, 0.4, 0.5, 0.2)$. The river height peaks $2$–$3$ days after the rainfall, and the response decays over $4$ days. (⭐, [[Def - Convolution]])
- **(Boyd Ex 8.11)** Location from range measurements: given the distances from an unknown point $x \in \mathbb R^3$ to four known points $a_1, a_2, a_3, a_4$ (each a $3$-vector), set up a system of linear equations for $x$ by squaring the distance equations and subtracting one from the others to eliminate the $\|x\|^2$ term. This converts the non-linear trilateration problem into a linear $3 \times 3$ system. (⭐⭐, [[Def - Norm and Distance]])

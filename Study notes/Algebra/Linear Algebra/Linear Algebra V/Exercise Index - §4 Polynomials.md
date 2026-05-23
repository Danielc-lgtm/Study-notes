---
type: exercise-index
subject: linear-algebra
section: "4"
tags: [algebra, linear-algebra]
---

## §4 Polynomials — Exercises

The §4 polynomials section is the algebraic foundation of the eigenvalue theory to follow. The exercises here drill the **division algorithm** (the engine that makes $F[x]$ a Euclidean domain, hence a PID), **factorisation over $\mathbb{R}$ and $\mathbb{C}$** (the structural theorem distinguishing the two fields), and the **factor theorem** (zero of a polynomial ↔ linear factor). The recurring strategic move is to leverage the polynomial-[[Def - Ring|ring]] structure to extract structural information, exactly the move that will power §5's eigenvalue arguments through the minimal polynomial. The fundamental theorem of algebra over $\mathbb{C}$ is the key analytic fact whose algebraic consequences drive the chapter.

- [[Ex - The differentiation operator on polynomials has eigenvalue zero only]] (⭐) — degree-decrease argument for eigenvalues of a graded operator; previews §5A by showing eigenvalue-zero-only is the prototypical non-trivial spectrum on an infinite-dimensional polynomial space ([[Def - Polynomial over a Field]], [[Def - Eigenvalue and Eigenvector]]).
- **(Web exercise — polynomial division)** (⭐) — verify the division algorithm directly: compute $q$ and $r$ for $p(x) = x^4 + 2x^3 - x + 5$ divided by $s(x) = x^2 - 1$. Standard polynomial long division gives $q$ and $r$ with $\deg r < 2$. The drill is to make sure you can produce both $q$ and $r$ algorithmically without error ([[Thm - Division Algorithm for Polynomials (LA)]]).
- **(Web exercise — factor theorem)** (⭐) — given $p(x) = x^3 - 6x^2 + 11x - 6$, find all real zeros by checking small integer values for roots, peeling off linear factors via the division algorithm, and factoring the remaining quadratic. Answer: zeros are $1, 2, 3$, and $p(x) = (x - 1)(x - 2)(x - 3)$ ([[Def - Division Algorithm and Factorization]]).

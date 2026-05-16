---
type: exercise-index
subject: module-theory
section: "3.3"
tags: [algebra, module-theory]
---

## §3.3 Matrices over Euclidean Domains — Exercises

- [[Ex - Computing the Smith normal form]] — run the Smith normal form algorithm by hand on concrete integer matrices ($\begin{pmatrix}2&-1\\1&2\end{pmatrix}$ with invariant factors $1,5$, and a $3\times 3$ example), using elementary row and column operations and the Euclidean function as termination certificate, then cross-check the result against the invariant factors extracted from the Fitting ideals via $\operatorname{Fit}_k=(d_1\cdots d_k)$ ([[Def - Euclidean Domain]], [[Def - Elementary Operations and Equivalent Matrices]], [[Def - Minor and Fitting Ideal]], [[Thm - Smith Normal Form]], [[Thm - Fitting Ideals are Invariants]]).

- [[Ex - Identifying an abelian group from generators and relations]] — turn an opaque finite presentation $\langle a,b,c\mid 2a+3b+c=0,\ a+2b=0,\ 5a+6b+7c=0\rangle$ of an abelian group into an explicit product of cyclic groups: encode the relations as the columns of a relation matrix, read its invariant factors $1,1,3$ off the Fitting ideals (a unit entry and a unit $2\times 2$ minor collapse the chain, leaving $\det X$), and conclude $A\cong C_3$ ([[Def - Euclidean Domain]], [[Def - Elementary Operations and Equivalent Matrices]], [[Def - Minor and Fitting Ideal]], [[Thm - Smith Normal Form]], [[Thm - Fitting Ideals are Invariants]], [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain]], [[Thm - Classification of Finitely Generated Abelian Groups]]).

- [[Ex - Invariant factors and elementary divisors]] — translate a finite abelian group between its two canonical forms — the invariant-factor chain $C_{d_1}\times\cdots$ with $d_1\mid d_2\mid\cdots$ and the elementary-divisor product of prime-power cyclic groups — by building the grid of prime-power exponents and reading it cell-by-cell (elementary divisors) or by right-aligned columns (invariant factors), with the Chinese remainder theorem splitting and merging cyclic groups along coprime factorisations ([[Thm - Classification of Finitely Generated Abelian Groups]], [[Thm - Chinese Remainder Theorem for Modules]], [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain]]).

- [[Ex - Classifying abelian groups of a given order]] — count the abelian groups of order $600=2^3\cdot 3\cdot 5^2$ up to isomorphism: the Chinese remainder theorem decouples the classification across primes, each $p$-primary part of order $p^a$ corresponds bijectively to a partition of $a$, so the total is $p(3)\cdot p(1)\cdot p(2)=3\cdot 1\cdot 2=6$, listed explicitly in both elementary-divisor and invariant-factor form ([[Thm - Classification of Finitely Generated Abelian Groups]], [[Thm - Chinese Remainder Theorem for Modules]], [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain]]).

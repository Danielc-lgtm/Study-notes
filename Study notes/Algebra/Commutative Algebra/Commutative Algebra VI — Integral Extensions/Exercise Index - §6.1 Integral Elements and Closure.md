---
type: exercise-index
subject: commutative-algebra
section: "6.1"
tags: [algebra, commutative-algebra]
---

## §6.1 Integral Elements and Closure — Exercises

The exercises of §6.1 drill the foundational distinction of the chapter — *integral* versus merely *algebraic* — and the master technique that flows from it: re-characterising integrality as module-finiteness so that closure properties become module bookkeeping. Across these problems you practise the two reflexes that solve most element-level questions: *exhibit a monic equation* to prove integrality, and *place elements in a finite module* to prove combinations are integral without producing their equations. The base case — that $\mathbb{Z}$ is integrally closed — and the flagship application — that algebraic integers form a ring — are both here, with the algorithm for combining minimal polynomials as a constructive coda.

- [[Ex - The integral closure of Z in Q is Z]] (⭐) — prove $\mathbb{Z}$ is normal: a rational integral over $\mathbb{Z}$ is an integer, via the lowest-terms argument (clear denominators, isolate the numerator power, track a single prime to a contradiction), the prototype for "disprove integrality with a UFD" ([[Def - Integral Element and Integral Extension]], [[Def - Integral Closure and Normal Domain]], [[Thm - A UFD is Integrally Closed]], [[Thm - Rational Algebraic Integers are Integers]], [[Def - Unique Factorization Domain]]).

- [[Ex - Sums and products of algebraic integers are algebraic integers]] (⭐⭐) — show the algebraic integers form a ring by the module-finite criterion (put $a, b$ in the finite module $\mathbb{Z}[a, b]$ and integralise everything in it at once), then make it constructive via companion matrices and the Kronecker sum/product (Example Sheet 1 Q15(b)) ([[Def - Integral Element and Integral Extension]], [[Def - Algebraic Integer and Minimal Polynomial]], [[Thm - The Integral Closure is a Subring]], [[Thm - Characterizations of Integrality (Module-Finite Criterion)]], [[Thm - Transitivity of Integrality and Finiteness]]).

- [[Ex - Z[sqrt 5] is not integrally closed]] (⭐⭐) — exhibit the missing algebraic integer $\tfrac{1+\sqrt5}2$ (integral via $T^2 - T - 1$, outside $\mathbb{Z}[\sqrt5]$ by its half-integer coordinate) to disprove normality, then compute $\overline A = \mathbb{Z}[\tfrac{1+\sqrt5}2]$ by the sandwich, capping with a Euclidean-hence-UFD candidate ([[Def - Integral Element and Integral Extension]], [[Def - Integral Closure and Normal Domain]], [[Def - Field of Fractions]], [[Thm - The Integral Closure is a Subring]], [[Thm - A UFD is Integrally Closed]]).

- [[Ex - The integral closure of k[t^2,t^3] resolves the cusp]] (⭐⭐) — compute the normalization of the cuspidal cubic: $t = t^3/t^2$ is integral via $T^2 - t^2$ but missing from $k[t^2, t^3]$, and the closure is the smooth line $k[t]$ (sandwich, capped by $k[t]$ a PID), interpreted geometrically as resolution of the cusp singularity ([[Def - Integral Element and Integral Extension]], [[Def - Integral Closure and Normal Domain]], [[Def - Field of Fractions]], [[Thm - The Integral Closure is a Subring]], [[Thm - A UFD is Integrally Closed]]).

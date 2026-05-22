---
type: exercise-index
subject: linear-algebra
section: "X.2"
tags: [algebra, linear-algebra, applied]
---

## §X.2 Distance, Clustering, and Independence — Exercises

The exercises of §X.2 build geometric fluency in $\mathbb R^n$: norms and distances, angles and orthogonality, standard deviation and correlation, and the $k$-means clustering algorithm. The Cauchy–Schwarz inequality is the workhorse, appearing in nearly every proof. Linear independence emerges as the abstract counterpart to "no redundancy" in data, with the Gram–Schmidt algorithm as the constructive tool for converting a list of independent vectors into an orthonormal basis. The targets are: (a) verify inequalities and identities involving norms (triangle, parallelogram, Pythagorean); (b) compute correlations and standardised quantities for given vectors; (c) execute the $k$-means algorithm on small datasets and reason about its convergence; (d) determine whether a list of vectors is linearly independent and find a basis or orthonormal basis.

- [[Ex - Correlation coefficient via Cauchy-Schwarz]] (⭐) — apply Cauchy–Schwarz to de-meaned vectors to show $-1 \leq \rho \leq 1$, and characterise the equality cases as perfect affine dependence ([[Def - Standard Deviation and Correlation Coefficient]], [[Thm - Cauchy-Schwarz and the Angle in Rn]])
- [[Ex - k-Means with two clusters on a one-dimensional dataset]] (⭐⭐) — run $k$-means by hand on a small one-dimensional dataset, identify the threshold structure of the optimal partition, and verify global optimality by enumerating alternative partitions ([[Def - Clustering and k-Means]], [[Thm - Convergence of k-Means]])
- [[Ex - Triangle inequality for the Euclidean norm]] (⭐) — *cross-listed with §X.1* — prove the triangle inequality using Cauchy–Schwarz, with the equality case being alignment ([[Def - Norm and Distance]], [[Thm - Cauchy-Schwarz and the Angle in Rn]])
- **(Boyd Ex 3.4)** Prove the parallelogram law $\|a + b\|^2 + \|a - b\|^2 = 2\|a\|^2 + 2\|b\|^2$ by expanding both squared norms and simplifying. This identity characterises inner-product norms among all norms — only the Euclidean norm satisfies it. (⭐, [[Def - Norm and Distance]])
- **(Boyd Ex 3.18)** Triangle inequality with equality: characterise when $\|a + b\| = \|a\| + \|b\|$ holds. The equality case is exactly when $a$ and $b$ are non-negative scalar multiples of each other (the aligned case). (⭐, [[Def - Norm and Distance]], [[Thm - Cauchy-Schwarz and the Angle in Rn]])
- **(Boyd Ex 5.6)** Run the Gram–Schmidt algorithm on the list $a_i \in \mathbb R^n$ where $a_i = (1, 1, \dots, 1, 0, \dots, 0)$ has $i$ ones followed by $n - i$ zeros. Show that $q_i = e_i$ (the $i$-th standard unit vector), and that $a_1, \dots, a_n$ is a basis of $\mathbb R^n$. (⭐⭐, [[Thm - QR Factorization via Gram-Schmidt (Boyd)]])

---
type: exercise-index
subject: group-theory
section: "1.1"
tags: [algebra, group-theory]
---

## §1.1 Basic Concepts — Exercises

The exercises of §1.1 drill the foundational toolkit of finite [[Def - Group|group]] theory: [[Def - Coset|cosets]], the order of elements, the cyclic [[Def - Subgroup|subgroup]] attached to an element, and above all [[Thm - Lagrange's Theorem|Lagrange's theorem]] and its corollary on element orders. Each entry below names the exercise, summarizes the technique it practices in one line, and lists in parentheses every definition and theorem invoked in that exercise's solution — these are the per-exercise prerequisites, the precise set of concepts that exercise rehearses.

- [[Ex - Groups of prime order are cyclic]] (⭐) — turn the order of a [[Def - Group|group]] into structure: a prime order collapses the possible element orders to two values, forcing a generator to exist ([[Def - Group]], [[Def - Subgroup]], [[Def - Order of a Group and of an Element]], [[Thm - Lagrange's Theorem]], [[Def - Isomorphism]])
- [[Ex - Order of an element divides the group order]] (⭐) — apply Lagrange to the cyclic [[Def - Subgroup|subgroup]] an element generates, obtaining $\operatorname{ord}(g) \mid |G|$ and $g^{|G|} = e$, then specialize to the units mod $p$ to read off Fermat's little theorem ([[Def - Group]], [[Def - Subgroup]], [[Def - Order of a Group and of an Element]], [[Thm - Lagrange's Theorem]])
- [[Ex - A finite group with a unique element of order two]] (⭐⭐) — exploit a uniqueness hypothesis with an order-preserving operation: conjugation sends the unique order-$2$ element to an order-$2$ element, hence fixes it, so it is central ([[Def - Group]], [[Def - Order of a Group and of an Element]], [[Thm - Lagrange's Theorem]])
- [[Ex - No group is the union of two proper subgroups]] (⭐⭐⭐) — refute a covering by contradiction: harvest a witness from each proper subgroup and combine them into a product that closure forbids from both ([[Def - Group]], [[Def - Subgroup]])
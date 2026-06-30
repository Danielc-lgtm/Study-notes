---
type: exercise-index
subject: special-relativity
section: "18.2"
tags: [physics, special-relativity]
---

## §18.2 Alternate Forms and the Exterior Product — Exercises

The exercises of §18.2 drill the [[Def - Alternate Forms and the Exterior Product|exterior algebra]]: the [[Def - Alternate Forms and the Exterior Product|wedge product]], its graded-commutativity $B\wedge A = (-1)^{pq}A\wedge B$, the dimension count $\dim\mathscr{A}_p = \binom{4}{p}$, and the expansion of a $2$-form in the wedge basis. The unifying theme is that a $p$-form is the algebraic measurer of oriented $p$-volume — a determinant in disguise — so that the wedge of one-forms is a determinant of pairings, an independent component is a choice of distinct indices, and the binomial symmetry $\binom{4}{p} = \binom{4}{4-p}$ is the precondition for Hodge duality. The culminating drill writes the electromagnetic field strength $F = E_i\,e^0\wedge e^i + \tfrac12\epsilon_{ijk}B^k\,e^i\wedge e^j$, making the six numbers $(\mathbf E, \mathbf B)$ the six components of a single $2$-form.

- [[Ex - The wedge of two one-forms]] (⭐) — compute $a\wedge b = a\otimes b - b\otimes a$ with components $(a\wedge b)_{\mu\nu} = a_\mu b_\nu - a_\nu b_\mu$, recognise the action as a $2\times2$ determinant of pairings, show $a\wedge b = 0$ iff $a, b$ are dependent, and interpret the wedge as the oriented plane (bivector) they span ([[Def - Alternate Forms and the Exterior Product]], [[Def - Tensor Operations]]).
- [[Ex - Counting the dimension of the space of p-forms]] (⭐) — prove $\dim\mathscr{A}_p(E) = \binom{4}{p}$ by counting strictly-increasing index tuples ($1, 4, 6, 4, 1$, summing to $2^4$), show $\mathscr{A}_p(E) = \{0\}$ for $p > 4$, and explain why $\binom{4}{p} = \binom{4}{4-p}$ is the dimension match that permits the Hodge star ([[Def - Alternate Forms and the Exterior Product]], [[Def - Tensors on Minkowski Space]]).
- [[Ex - Anticommutation and associativity of the wedge product]] (⭐⭐) — prove $B\wedge A = (-1)^{pq}A\wedge B$ (one-forms anticommute, a one-form and two-form commute), deduce that odd-degree forms square to zero while even need not ($F\wedge F \neq 0$), and verify associativity via the determinant of pairings ([[Def - Alternate Forms and the Exterior Product]], [[Def - Tensor Operations]]).
- [[Ex - Expanding a 2-form in the wedge basis]] (⭐⭐) — reconcile $\tfrac12 A_{\alpha\beta}e^\alpha\wedge e^\beta = \sum_{\alpha<\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta$ (the factor-of-two symmetry), list the six basis $2$-forms split into electric-type and magnetic-type, and write the field strength to read off its six components as $(\mathbf E, \mathbf B)$ ([[Def - Alternate Forms and the Exterior Product]], [[Def - Tensor Operations]]).

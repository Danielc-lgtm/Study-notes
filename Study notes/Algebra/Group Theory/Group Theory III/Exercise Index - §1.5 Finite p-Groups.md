---
type: exercise-index
subject: group-theory
section: "1.5"
tags: [algebra, group-theory]
---

## §1.5 Finite p-Groups — Exercises

The exercises of §1.5 drill the single technique on which all [[Def - p-group|p-group]] theory rests: the [[Thm - The Class Equation|class equation]] read modulo $p$, which forces a [[Thm - p-Groups Have Non-Trivial Centre|non-trivial centre]], and the inductive structure built on top of it. In every problem below the input is nothing but a prime-power order, and the recurring move is to convert that arithmetic — via [[Thm - Lagrange's Theorem|Lagrange]] and a conjugation action — into a statement about the centre. Each entry names the exercise, summarises in one line the technique it practices, and lists in parentheses every definition and theorem invoked in that exercise's solution — the per-exercise prerequisites, the precise set of concepts that exercise rehearses.

- [[Ex - p-groups are never simple for order at least p squared]] (⭐) — produce a proper non-trivial normal subgroup from a prime-power order: the centre is normal and non-trivial, and if it is all of $G$ then $G$ is abelian and a subgroup of order $p$ serves instead ([[Def - p-group]], [[Def - Simple Group]], [[Def - Normal Subgroup]], [[Def - Centraliser and Centre]], [[Def - Abelian Group]], [[Thm - p-Groups Have Non-Trivial Centre]], [[Thm - Subgroups of a p-Group]], [[Thm - Lagrange's Theorem]])
- [[Ex - Groups of order p squared are abelian]] (⭐⭐) — squeeze the order of the centre: Lagrange leaves $|Z(G)| \in \{1, p, p^2\}$, non-triviality deletes $1$, and a cyclic $G/Z(G)$ is self-contradictory, so $Z(G) = G$ ([[Def - p-group]], [[Def - Abelian Group]], [[Def - Centraliser and Centre]], [[Thm - p-Groups Have Non-Trivial Centre]], [[Thm - Quotient by the Centre and Commutativity]], [[Thm - Lagrange's Theorem]])
- [[Ex - A non-trivial normal subgroup meets the centre of a p-group]] (⭐⭐⭐) — run the fixed-point congruence on the right set: act $G$ on the normal subgroup $N$ by conjugation, identify the fixed points as $N \cap Z(G)$, and count modulo $p$ ([[Def - p-group]], [[Def - Normal Subgroup]], [[Def - Centraliser and Centre]], [[Def - Group Action]], [[Def - Conjugacy Class]], [[Thm - Orbit-Stabiliser Theorem]], [[Thm - Lagrange's Theorem]])
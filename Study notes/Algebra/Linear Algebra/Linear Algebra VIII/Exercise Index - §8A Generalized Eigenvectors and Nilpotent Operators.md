---
type: exercise-index
subject: linear-algebra
section: "8A"
tags: [algebra, linear-algebra]
---

## §8A Generalized Eigenvectors and Nilpotent Operators — Exercises

Section 8A is the introduction to generalized eigenvectors and nilpotent operators. The defining theme is the null-space chain $\operatorname{null} T^k$ and its stabilisation by dimension — the source of the "universal power $\dim V$" form of all subsequent definitions. The exercises drill two foundational skills: (i) using stabilisation to convert existential power statements into universal ones; (ii) computing the Jordan structure of small explicit nilpotent matrices by chasing the null-space chain. The techniques here are the precursor to the chapter's headline construction (generalized eigenspace decomposition + Jordan form): every later result reduces a question about a general operator to a question about nilpotent restrictions, and that reduction in turn rests on the null-space-stabilisation results of this section.

- [[Ex - A nilpotent operator on V satisfies T^dim V = 0]] (⭐) — converts the existential "$T^k = 0$ for some $k$" into the universal "$T^{\dim V} = 0$" via the null-space-stabilisation chain ([[Def - Nilpotent Operator]], [[Thm - Null Spaces of Powers Stabilize]]).

- [[Ex - Jordan form of a 3x3 nilpotent matrix]] (⭐⭐) — computes the Jordan form and an explicit Jordan basis of a $3 \times 3$ nilpotent matrix by verifying $A^3 = 0$, $A^2 \neq 0$, and constructing the chain $A^2 v, A v, v$ ([[Def - Nilpotent Operator]], [[Def - Jordan Basis and Jordan Form]], [[Thm - Existence of Jordan Form]]).

- [[Ex - Sum of algebraic multiplicities equals dimension]] (⭐) — extracts the dimension identity from the generalized eigenspace decomposition; verifies the formula $\dim V = \sum_\lambda \dim G(\lambda, T)$ ([[Def - Generalized Eigenspace]], [[Def - Algebraic and Geometric Multiplicity]], [[Thm - Generalized Eigenspace Decomposition]]).

The section's recurring move is "use null-space stabilisation"; the recurring template is the chain $\operatorname{null}(T - \lambda I)^k$ and how its dimensions encode the Jordan structure at $\lambda$. Students returning to the section after months should re-derive the null-space stabilisation result and the conversion of existential into universal power statements.

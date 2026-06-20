---
type: exercise-index
subject: higher-categories
section: "3"
tags: [category-theory, higher-categories, foundations]
---

## §3 Algebras and the Unifying Picture — Exercises

The closing section's exercises turn the framework into a working tool by drilling *algebras* — what a generalized operad acts on — and by assembling the chapter's payoff, the unifying table. The master technique is the operad-to-monad translation: a $T$-operad $P$ induces a monad $T_P X = P \times_{T1} TX$ whose Eilenberg–Moore algebras are the $P$-algebras, so the entire theory of monad-algebras becomes available. Concretely, this is how algebras for the associative operad are recognized as monoids (one operation per arity, all forced to be iterates of the binary one, with the unique ternary operation *being* the associativity law). The capstone exercise builds the full table across the three monads $\mathrm{id}, (-)^{*}, \mathbb{T}$, and articulates its two reading directions — a row is one coherent theory, a column is one uniform construction — guarding against the characteristic error of expecting "operad" to mean a fixed object regardless of $T$. The recurring insight is that the framework's thinness is its strength: a generic theorem about $T$-multicategories is automatically a theorem about every row.

- [[Ex - Algebras for the associative operad are monoids]] (⭐⭐) — "one operation per arity" is the signature of an associative structure; the unique ternary operation forces associativity ([[Def - Algebra for a Generalized Operad]], [[Def - Generalized Operad]], [[Def - Monoid in a Monoidal Category]])
- [[Ex - The induced monad of a generalized operad]] (⭐⭐) — the operad-to-monad construction $T_P X = P \times_{T1} TX$; operations compose and shapes flatten in parallel, kept aligned by cartesianness ([[Def - Algebra for a Generalized Operad]], [[Def - Generalized Operad]], [[Def - Algebra for a Monad]], [[Def - Cartesian Monad]])
- [[Ex - Reading the unifying table across three monads]] (⭐⭐⭐) — assembling the four-column table for $\mathrm{id}, (-)^{*}, \mathbb{T}$; rows are theories, columns are constructions, and conflating them is the trap ([[Def - Generalized Multicategory]], [[Def - Generalized Operad]], [[Def - Algebra for a Generalized Operad]], [[Def - Cartesian Monad]])

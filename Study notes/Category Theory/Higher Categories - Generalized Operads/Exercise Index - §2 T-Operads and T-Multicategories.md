---
type: exercise-index
subject: higher-categories
section: "2"
tags: [category-theory, higher-categories, foundations]
---

## §2 T-Operads and T-Multicategories — Exercises

These exercises drill the central skill of the chapter: *unwinding* a generalized definition into a classical one by computing the two controlling objects, $T C_0$ (what an arrow's domain may be) and $T1$ (the arity object). The procedure is mechanical once those objects are known — substitute the concrete monad, watch each structure map turn into a classical axiom, and check the comparison functors are mutually inverse on objects *and* morphisms. The set covers the two foundational rows of the unifying table: the identity monad (recovering small categories, where $T C_0 = C_0$) and the list monad (recovering classical multicategories and operads, where $T C_0 = C_0^{*}$ and $T1 = \mathbb{N}$). A dedicated drill on computing $T1$ for four monads installs the reflex "new cartesian monad $\rightsquigarrow$ compute $T1$ first", which classifies an operad before any other work. The recurring trap, guarded against throughout, is assuming the one-object case ($C_0 = 1$) is always a monoid: it is only when $T1$ is trivial.

- [[Ex - A category is an identity-multicategory]] (⭐⭐) — unwinding by computing $T C_0 = C_0$; an equivalence of categories requires matching morphisms (functors), not just objects ([[Def - Generalized Multicategory]], [[Def - Cartesian Monad]], [[Def - Category]], [[Def - Functor]])
- [[Ex - A classical operad is a free-monoid-operad]] (⭐⭐) — the one-object case with $T1 = \mathbb{N}$; collapsing colours does not collapse arities, so the result is an operad, not a monoid ([[Def - Generalized Operad]], [[Def - Generalized Multicategory]], [[Def - Cartesian Monad]])
- [[Ex - Computing the arity object T1]] (⭐) — computing $T1$ for the identity, list, free-category, and globular monads; reading off monoids / operads / linear-graph-operads / globular operads ([[Def - Generalized Operad]], [[Def - Cartesian Monad]], [[Def - Initial and Terminal Object]], [[Def - Monoid in a Monoidal Category]])

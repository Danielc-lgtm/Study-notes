---
type: exercise-index
subject: higher-categories
section: "HC7.1"
tags: [category-theory, higher-categories, foundations]
---

## §1 The Free Strict ω-Category Monad — Exercises

This section makes the substrate of the whole chapter concrete. The free strict $\omega$-category monad $T$ is the object every later construction perturbs, and the exercises here build the three skills you will reuse constantly: *computing* the pasting diagrams $T1 = \mathrm{pd}$ via the recursion $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$, *verifying cartesianness* (the single load-bearing property of $T$) on a manageable truncation, and *reading* a general $TX$ as labelled pasting diagrams (the prototype every globular operad imitates). Do the computation exercise first — it demystifies the abstraction — then the cartesianness and labelling exercises, which together justify the operad framework of §2.

- [[Ex - Computing the low-dimensional pasting diagrams]] (⭐) — evaluate the pasting-diagram recursion in low dimensions and compute the boundary; the habit of dropping to small dimensions to demystify globular machinery ([[Def - The Free Strict ω-Category Monad]])
- [[Ex - The free strict omega-category monad is cartesian on a slice]] (⭐⭐) — prove the free-category monad is cartesian via the path description, showing "freeness made into a pullback", and lift dimension by dimension ([[Def - The Free Strict ω-Category Monad]], [[Def - Pullback and Pushout]])
- [[Ex - Pasting diagrams as labelled composites]] (⭐⭐) — read an element of $TX$ as a pasting diagram with an $X$-labelling, and use cartesianness to compute the fibre over a fixed shape as the labellings ([[Def - The Free Strict ω-Category Monad]], [[Def - Pullback and Pushout]])

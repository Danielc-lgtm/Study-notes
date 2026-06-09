---
type: exercise-index
subject: commutative-algebra
section: "11.1"
tags: [algebra, commutative-algebra]
---

## §11.1 Limits and Directed Systems — Exercises

The exercises of §11.1 drill the two dual constructions of the chapter — the [[Def - Direct and Inverse Limits|direct and inverse limits]] — and the discipline of reading a system off its *arrows* rather than its objects. The unifying technique is the [[Def - Direct and Inverse Limits|universal property]]: to identify a limit, build a compatible family of maps into (for $\varprojlim$) or out of (for $\varinjlim$) the stages and exhibit the candidate as universal. The headline contrast — the Prüfer group and the $p$-adic integers built from the *same* objects $\mathbb{Z}/p^n\mathbb{Z}$ with opposite arrows — is the reference example for "direct limits enlarge, inverse limits refine", and recurs throughout the chapter. Each exercise trains the level-by-level (for threads) or push-to-one-stage (for unions) computation that the two limits demand.

- [[Ex - The p-adic integers as an inverse limit]] (⭐⭐) — construct $\mathbb{Z}_p=\varprojlim\mathbb{Z}/p^n\mathbb{Z}$, extract the unique left-infinite base-$p$ digit expansion from a compatible thread (compatibility freezes low digits), compute $-1=\dots4444_5$, and prove $\mathbb{Z}_p$ is a local domain whose units are the threads with non-zero first digit, by digit-by-digit inversion ([[Def - Direct and Inverse Limits]], [[Def - The I-adic Completion]], [[Def - Integral Domain]], [[Def - Local Ring and Residue Field]], [[Thm - The Inverse Limit and Completeness]]).

- [[Ex - A direct limit of cyclic groups (Prufer group)]] (⭐⭐) — identify $\varinjlim\mathbb{Z}/p^n\mathbb{Z}\cong\mathbb{Z}[1/p]/\mathbb{Z}$ (Prüfer $p$-group) along the multiplication-by-$p$ inclusions by re-coordinatising the stages as nested subgroups $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$ of $\mathbb{Q}/\mathbb{Z}$, deduce divisibility and the totally-ordered finite cyclic subgroup structure, and contrast with the dual $\mathbb{Z}_p=\varprojlim$ of the same objects ([[Def - Direct and Inverse Limits]], [[Def - Directed Set and Direct System]], [[Def - Group]], [[Def - The I-adic Completion]]).

- [[Ex - The formal power series ring as a completion]] (⭐⭐) — prove $\varprojlim k[T]/(T^n)\cong k[[T]]$ by the coefficient-extraction bijection, verify multiplication survives the limit because each Cauchy-product coefficient is a finite sum, and read off locality (units $=\{f(0)\neq0\}$, inverse of $1-T$ is $\sum T^m$); this is the §11.1 universal-property technique applied to the degree-truncation tower, bridging into §11.2 ([[Def - Direct and Inverse Limits]], [[Def - The I-adic Completion]], [[Def - Polynomial Ring]], [[Def - Local Ring and Residue Field]]).

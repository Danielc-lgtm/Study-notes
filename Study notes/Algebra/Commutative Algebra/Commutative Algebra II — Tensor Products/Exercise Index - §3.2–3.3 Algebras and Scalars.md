---
type: exercise-index
subject: commutative-algebra
section: "3.2-3.3"
tags: [algebra, commutative-algebra]
---

## §3.2–3.3 Algebras and Scalars — Exercises

The exercises of §3.2–3.3 drill the two upgrades of the module tensor product: to *algebras*, where $A\otimes_R B$ is the [[Thm - Universal Property of the Tensor Product of Algebras|coproduct]] (the fibre product of spaces), and to *base change*, where extension of scalars $S\otimes_R(-)$ rebases a module along a ring map $f : R\to S$. Each exercise practises the coproduct universal property and the upgrading lemma (checking algebra-maps on generators), the quotient rule $A\otimes_R B\cong B[X]/(\bar f)$ that makes the factorisation of $\bar f$ control the structure, and the reduction-versus-enlargement faces of extension of scalars. The unifying lesson is that tensoring algebras *glues* (variables, relations, spaces) while tensoring with a residue ring *reduces* — both governed by how the relevant ideal $I+J$ or $I^e+J^e$ behaves, and both incarnations of the same universal construction.

- [[Ex - Tensoring with R over I gives M over IM]] (⭐⭐) — prove $(R/I)\otimes_R M\cong M/IM$ ($\bar r\otimes m\mapsto\overline{rm}$), the workhorse special case of extension of scalars, by building mutually inverse maps whose two well-definedness checks are the single mirror-image identity $\bar a\otimes m = \bar1\otimes am$; deduce $(\mathbb{Z}/n)\otimes\mathbb{Z}^k\cong(\mathbb{Z}/n)^k$ and the enlargement $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{R}^n\cong\mathbb{C}^n$ ([[Def - Tensor Product of Modules]], [[Def - Quotient Module]], [[Thm - Standard Isomorphisms of Tensor Products]], [[Thm - Universal Property of the Tensor Product of Modules]], [[Def - Ideal]], [[Def - Restriction and Extension of Scalars]]).

- [[Ex - Extension of scalars of a free module]] (⭐) — show $S\otimes_R R^{(I)}\cong S^{(I)}$ with basis $\{1\otimes e_i\}$, by distributivity over direct sums and the identity law, and that $\operatorname{id}_S\otimes T$ keeps the matrix $[T]$ of $T$ over the new ring — base change of a free module is "rebase the scalars, same basis, same matrix" ([[Def - Tensor Product of Modules]], [[Def - Restriction and Extension of Scalars]], [[Thm - Standard Isomorphisms of Tensor Products]], [[Thm - Extension of Scalars and the Adjunction]], [[Def - Free Module]]).

- [[Ex - Tensor product of polynomial algebras]] (⭐⭐) — prove $R[X_*]\otimes_R R[T_*]\cong R[X_*,T_*]$ two ways (monomial-basis isomorphism upgraded via the upgrading lemma; recognition of the joint polynomial ring as the coproduct), and the quotient version $R[X_*]/I\otimes R[T_*]/J\cong R[X_*,T_*]/(I^e+J^e)$ — gluing variable sets and relation ideals, the product of affine spaces ([[Def - Tensor Product of Algebras]], [[Thm - Universal Property of the Tensor Product of Algebras]], [[Thm - Standard Isomorphisms of Tensor Products]], [[Def - Polynomial Ring]], [[Def - Free Module]], [[Def - Ideal]]).

- [[Ex - C tensor R C is not a field]] (⭐⭐) — show $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ via $A\otimes_R B\cong B[X]/(\bar f)$ and the splitting $X^2+1=(X-i)(X+i)$, exhibiting zero divisors and idempotents, and reading the geometry as a single $\mathbb{R}$-point splitting into two $\mathbb{C}$-points — the failure of geometric irreducibility under base change ([[Def - Tensor Product of Algebras]], [[Thm - Universal Property of the Tensor Product of Algebras]], [[Thm - Standard Isomorphisms of Tensor Products]], [[Def - Ideal]]).

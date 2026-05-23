---
type: exercise-index
subject: module-theory
section: "3.2"
tags: [algebra, module-theory]
---

## §3.2 Direct Sums and Free Modules — Exercises

The exercises of §3.2 drill the free-[[Def - Module|module]] concept and its limitations. Each exercise calibrates a structural intuition: torsion obstructs freeness ($\mathbb{Z}/2$ as a $\mathbb{Z}$-module), generating sets need not contain bases over non-fields (Bézout coefficients yield redundant generators of $\mathbb{Z}$), $\mathbb{Q}$ is not finitely generated as a $\mathbb{Z}$-module (denominator-bound obstruction), and [[Def - Ideal|ideals]] can be free [[Def - Submodule|submodules]] of free [[Def - Ring|rings]] only when the ring is a PID (counterexample $(X, Y) \subseteq k[X, Y]$). The unifying observation: "free" is a strong condition that fails precisely where the scalar ring is not nice enough.

- [[Ex - The integers mod two is not a free module]] (⭐) — show the abelian [[Def - Group|group]] $\mathbb{Z}/2$ is not a free $\mathbb{Z}$-module, by two routes: directly, the only candidate basis element $\overline{1}$ is torsion ($2\cdot\overline{1}=\overline{0}$) so it fails linear independence; structurally, a non-zero free $\mathbb{Z}$-module embeds the infinite group $\mathbb{Z}$ (build a homomorphism to $\mathbb{Z}$ from a basis element and apply it to $2b=0$), which a two-element module cannot house ([[Def - Module]], [[Def - Free Module]], [[Def - Module Homomorphism]], [[Thm - Characterisations of Free Generation]]).

- [[Ex - Generating sets that are not bases]] (⭐⭐) — show $\{2,3\}$ generates the $\mathbb{Z}$-module $\mathbb{Z}$ (Bézout assembles the unit $1$) but not freely (the relation $3\cdot 2-2\cdot 3=0$), and that neither $\{2\}$ nor $\{3\}$ generates $\mathbb{Z}$ — so a redundant generating set need not contain a basis, because the exchange lemma's hidden hypothesis, invertibility of the scalar being eliminated, fails over a non-field ([[Def - Module]], [[Def - Submodule]], [[Def - Finitely Generated Module]], [[Def - Free Module]], [[Thm - Characterisations of Free Generation]], [[Thm - Invariance of Rank]]).

- [[Ex - The rationals are not a finitely generated module over the integers]] (⭐⭐) — show $\mathbb{Q}$ is not a finitely generated $\mathbb{Z}$-module by a denominator bound: a hypothetical finite generating set has a common denominator $d$, so the submodule it generates lies inside the fractions $\tfrac{1}{d}\mathbb{Z}$, which misses $\tfrac{1}{2d}$ since $2d\nmid d$ ([[Def - Module]], [[Def - Submodule]], [[Def - Finitely Generated Module]]).

- [[Ex - A submodule of a free module that is not free]] (⭐⭐) — show the ideal $(X,Y)$ of $R=k[X,Y]$, a submodule of the free module $R$, is not free: it is not principal (a single generator would divide both $X$ and $Y$, forcing a unit), so any generating set has $\ge 2$ elements, and commutativity makes any two generators relate via $Y\cdot X-X\cdot Y=0$ — ruling out every basis size, and pinpointing that $k[X,Y]$ is not a PID ([[Def - Module]], [[Def - Submodule]], [[Def - Free Module]], [[Def - Finitely Generated Module]], [[Thm - Characterisations of Free Generation]], [[Def - Ideal]], [[Def - Polynomial Ring]]).

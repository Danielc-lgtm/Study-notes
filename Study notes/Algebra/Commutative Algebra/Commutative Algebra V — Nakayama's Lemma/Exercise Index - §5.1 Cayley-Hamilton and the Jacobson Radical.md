---
type: exercise-index
subject: commutative-algebra
section: "5.1"
tags: [algebra, commutative-algebra]
---

## §5.1 Cayley–Hamilton and the Jacobson Radical — Exercises

The exercises of §5.1 drill the engine of the chapter — the [[Thm - Cayley-Hamilton for Modules (Determinant Trick)|determinant trick]] — in the settings where it produces conclusions that look like they should require a field but do not. The unifying technique is the same in every case: turn a structural hypothesis (a surjection, an embedding, a self-map) into a matrix over an ideal, then let the adjugate identity $\operatorname{adj}(Q)Q = (\det Q)I$ extract a polynomial relation. Two recurring moves recur: *make the module an $R[T]$-module by letting $T$ act as the relevant endomorphism*, which manufactures the ideal $(T)$ out of thin air, and *pad a cross-rank map into a self-map* so the determinant is defined. These exercises also isolate the necessity of finite generation, the hypothesis without which the trick has no finite matrix to grip. The Jacobson-radical material is exercised here through its unit characterisation, the bridge that lets the trick's output $1 - a$ be inverted.

- [[Ex - A surjective endomorphism of a finitely generated module is injective]] (⭐⭐) — promote surjectivity to injectivity by letting $T$ act as the endomorphism and reading the determinant-trick relation as an explicit inverse; isolates that finite generation is necessary (left shift on an infinite-rank module) and that the converse fails (multiplication by $2$ on ℤ) ([[Thm - Cayley-Hamilton for Modules (Determinant Trick)]], [[Def - Finitely Generated Module]], [[Def - Module Homomorphism]], [[Def - Polynomial Ring]]).

- [[Ex - Every generating set of size n for R^n is a basis]] (⭐⭐⭐) — read a size-$n$ generating set of $Rⁿ$ as a surjective endomorphism (hence a basis, by the previous exercise), then pad an embedding $Rⁿ ↪ Rᵐ$ into a self-map and use McCoy's theorem (injective $\iff \det$ a non-zero-divisor) to force $n \le m$; the determinant trick controls rank with no notion of dimension ([[Thm - Cayley-Hamilton for Modules (Determinant Trick)]], [[Def - Free Module]], [[Def - Finitely Generated Module]], [[Thm - Invariance of Rank]]).

- [[Ex - A module with mM equal to M that is nonzero]] (⭐⭐) — construct a nonzero module $M = ℚ$ over $ℤ_{(p)}$ with $𝔪M = M$, isolating the finite-generation hypothesis of the determinant trick / Nakayama by exhibiting a divisible (infinitely generated) module where the trick has no finite matrix ([[Thm - Nakayama's Lemma]], [[Def - Finitely Generated Module]], [[Def - Local Ring and Residue Field]]).

---
type: exercise-index
subject: commutative-algebra
section: "3.5"
tags: [algebra, commutative-algebra]
---

## §3.5 Projectivity and Hom — Exercises

The exercises of §3.5 drill projectivity and the splitting of short exact sequences, the Hom-side counterparts to §3.4's flatness. The recurring technique is the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]]: projectivity becomes "direct summand of a free module," which is how projectives are recognised (idempotents, free covers that split) and how projective $\Rightarrow$ flat is read off. Two further skills are practiced: deciding whether a short exact sequence splits — by producing a section or retraction via [[Ex - The splitting lemma|the splitting lemma]], with a projective quotient as the clean sufficient condition — and separating the rungs of the tower with witnesses (flat-not-projective, projective-not-free), each refuted by an invariant a stronger class would have to share. The standing caution, drilled directly, is that "splits" is a property of the maps and not of the abstract isomorphism type of the middle term.

- [[Ex - The splitting lemma]] (⭐⭐) — prove the equivalence of "splits," "$g$ has a section," and "$f$ has a retraction" by a cycle of constructions, the key move being the complementary projection $\operatorname{id}_B - sg$ that converts a section into a retraction, and the explicit splitting isomorphism $(r, g) : B\to A\oplus C$ ([[Def - Exact Sequence and Short Exact Sequence]], [[Def - Module Homomorphism]], [[Def - Direct Sum of Modules]], [[Def - Projective Module]]).

- [[Ex - Q is a flat but not projective Z-module]] (⭐⭐) — separate flat from projective: $\mathbb{Q}$ is flat as a localization of $\mathbb{Z}$, but not projective because the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]] would embed it in a free abelian group, contradicting divisibility — the technique of refuting a structural property with a preserved invariant ([[Def - Flat Module]], [[Def - Projective Module]], [[Def - Field of Fractions]], [[Thm - Projective iff Direct Summand of a Free Module]], [[Thm - Extension of Scalars Preserves Flatness]]).

- [[Ex - A projective module that is not free]] (⭐⭐) — separate projective from free using an idempotent: in $\mathbb{Z}/6\cong\mathbb{Z}/2\times\mathbb{Z}/3$ the summand $\mathbb{Z}/2 = Re$ ($e = (1,0)$) is projective by the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]] but not free, refuted by counting ($2\neq 6^n$), with the Dedekind-domain ideal $(2, 1+\sqrt{-5})$ as the number-theoretic face ([[Def - Projective Module]], [[Def - Free Module]], [[Thm - Projective iff Direct Summand of a Free Module]], [[Def - Ideal]]).

- [[Ex - A short exact sequence that does not split though B is the direct sum]] (⭐⭐) — isolate the distinction between "splits" (a property of the maps) and "$B\cong A\oplus C$" (a property of the abstract module), using a torsion obstruction over $\mathbb{Z}/4$ and self-similarity $M\oplus M\cong M$ to build the witness, the deeper invariant being the extension class in $\operatorname{Ext}^1$ ([[Def - Exact Sequence and Short Exact Sequence]], [[Def - Module Homomorphism]], [[Def - Direct Sum of Modules]]).

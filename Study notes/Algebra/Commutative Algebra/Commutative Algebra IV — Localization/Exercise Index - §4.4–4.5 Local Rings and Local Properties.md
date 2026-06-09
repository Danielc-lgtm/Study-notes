---
type: exercise-index
subject: commutative-algebra
section: "4.4-4.5"
tags: [algebra, commutative-algebra]
---

## §4.4–4.5 Local Rings and Local Properties — Exercises

These exercises drill the chapter's payoff: the local–global principle, the properties it does and does not cover, and the local-ring techniques it unlocks. The unifying technique is **"check it one prime at a time"**, justified by the principle that being zero, injective, surjective, exact, and flat are all local properties — and the engine under all of them is the base lemma "a nonzero module is detected by some maximal localization", proved by the annihilator argument. The exercises practice three things: proving a property is local by recasting it as the vanishing of a canonical module (reducedness as $\operatorname{nil} R = 0$), using locality to establish a global equality by checking surjectivity at each maximal ideal (a domain as the intersection of its localizations), and — crucially — confronting the *boundary* of the principle, where freeness fails to be local and nontrivial vector bundles are born. Knowing which properties are local and which are not is as important as the principle itself.

- [[Ex - Being reduced is a local property]] (⭐⭐) — prove $R$ reduced $\iff R_{\mathfrak{p}}$ reduced for all $\mathfrak{p}$ by recasting "reduced" as the vanishing of the module $\operatorname{nil} R$ and running the local–global principle (using that localization commutes with the nilradical), then exhibit $\mathbb{C}\times\mathbb{C}$ to show "integral domain" is *not* local ([[Def - Radical of an Ideal and the Nilradical]], [[Def - Local Property (Localizable and Local-to-Global)]], [[Thm - The Local-Global Principle]], [[Def - Multiplicative Set and Localization]]).

- [[Ex - A domain is the intersection of its localizations at maximal ideals]] (⭐⭐) — prove $A = \bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$ inside $\operatorname{Frac}(A)$, via the ideal of denominators $(A:x)$ (an element lying in every $A_{\mathfrak{m}}$ has denominator-ideal escaping every maximal ideal, hence equal to $A$), equivalently by surjectivity of the inclusion being a local property ([[Def - Integral Domain]], [[Def - Field of Fractions]], [[Thm - The Local-Global Principle]], [[Def - Local Ring and Residue Field]], [[Def - Prime and Maximal Ideal]]).

- [[Ex - Freeness is not a local property]] (⭐⭐⭐) — construct a locally free but non-free module: over $R = \mathbb{C}\times\mathbb{C}$ every localization is a field so every module is locally free, yet the ideal $\mathbb{C}\times\{0\}$ has no basis (annihilated by an idempotent); then the integral-domain version $(2, 1+\sqrt{-5})\trianglelefteq\mathbb{Z}[\sqrt{-5}]$, a non-trivial line bundle, projective hence locally free but non-principal hence non-free ([[Def - Free Module]], [[Def - Local Property (Localizable and Local-to-Global)]], [[Thm - Prime Ideals of a Localization]], [[Def - Multiplicative Set and Localization]], [[Def - Prime and Maximal Ideal]]).

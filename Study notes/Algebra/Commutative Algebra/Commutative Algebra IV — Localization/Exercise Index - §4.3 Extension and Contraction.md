---
type: exercise-index
subject: commutative-algebra
section: "4.3"
tags: [algebra, commutative-algebra]
---

## §4.3 Extension and Contraction of Ideals — Exercises

These exercises drill how ideals move under a ring map, and especially under the localization map, where the abstract machinery becomes the geometric prime correspondence. The unifying technique is the **Galois-connection adjunction** $\mathfrak{a}^e\subseteq\mathfrak{b}\iff\mathfrak{a}\subseteq\mathfrak{b}^c$, from which every round-trip inequality, fixed-point characterisation, and bijection follows formally — recognising the adjunction is what turns multi-part computations into one identity plus deductions. The exercises practice three things: the general extension–contraction bijection between contracted and extended ideals (the abstract engine), its geometric upgrade for the localization map to the bijection $\{\mathfrak{p} : \mathfrak{p}\cap S = \varnothing\}\leftrightarrow\operatorname{Spec}(S^{-1}R)$, and the commutation of the radical with extension. The recurring trigger is "every ideal of $S^{-1}R$ is extended", the fact that makes localization a transparent operation on the spectrum.

- [[Ex - Extension and contraction bijection of ideals]] (⭐⭐) — establish the full Galois-connection machinery for any ring map: $\mathfrak{b}^c$ is always an ideal but $\varphi(\mathfrak{a})$ need not be, the round-trip inequalities $\mathfrak{a}\subseteq\mathfrak{a}^{ec}$ and $\mathfrak{b}^{ce}\subseteq\mathfrak{b}$, and the bijection between contracted and extended ideals — all derived from the single adjunction identity ([[Def - Extension and Contraction of Ideals]], [[Def - Ring Homomorphism]], [[Def - Ideal]]).

- [[Ex - The prime spectrum of a localization]] (⭐⭐) — compute $\operatorname{Spec}(S^{-1}R)$ via the disjointness criterion $\mathfrak{p}\cap S = \varnothing$, upgrade the bijection to a homeomorphism onto the basic open $D(f)$ (checking that closed sets correspond via the adjunction), and list $\operatorname{Spec}(\mathbb{Z}_{(p)})$ versus $\operatorname{Spec}(\mathbb{Z}[\tfrac1p])$ as complementary pieces of $\operatorname{Spec}\mathbb{Z}$ ([[Thm - Prime Ideals of a Localization]], [[Def - The Prime Spectrum (Spec)]], [[Def - Extension and Contraction of Ideals]], [[Def - Multiplicative Set and Localization]]).

- [[Ex - The radical of an extended ideal]] (⭐⭐) — prove $\sqrt{I}^{\,e} = \sqrt{I^e}$ (radical commutes with localization), by a clear-denominators-then-absorb computation, and deduce $(\operatorname{nil} R)^e = \operatorname{nil}(S^{-1}R)$; a conceptual second proof routes through $\sqrt I = \bigcap\mathfrak{p}$ and the prime correspondence ([[Def - Radical of an Ideal and the Nilradical]], [[Def - Extension and Contraction of Ideals]], [[Thm - Prime Ideals of a Localization]], [[Thm - The Radical is the Intersection of the Primes Above It]]).

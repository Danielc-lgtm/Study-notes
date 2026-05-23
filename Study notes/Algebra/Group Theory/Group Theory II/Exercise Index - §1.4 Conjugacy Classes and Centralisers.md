---
type: exercise-index
subject: group-theory
section: "1.4"
tags: [algebra, group-theory]
---

## §1.4 Conjugacy Classes and Centralisers — Exercises

The exercises of §1.4 drill the conjugacy-class / centraliser pair: the orbit-stabiliser identity $|G| = |\text{class}| \cdot |\text{centraliser}|$ lets one quantity determine the other, and the cycle-type classification of conjugacy classes in $S_n$ makes the symmetric [[Def - Group|group]]'s structure totally explicit. The unifying technique: every conjugacy-counting argument runs on orbit-stabiliser applied to the conjugation action, with normal-[[Def - Subgroup|subgroups]] recognised as conjugation-saturated unions of classes.

- [[Ex - Centraliser of a permutation in the symmetric group]] (⭐) — compute a centraliser by counting its conjugacy class via cycle type and dividing $|G|$ by it with orbit-stabiliser; identifies the centraliser of an $n$-cycle as $\langle\sigma\rangle$ and $C_{S_4}((1\,2)(3\,4))$ as $D_8$ ([[Def - Symmetric Group]], [[Def - Conjugacy Class]], [[Def - Centraliser and Centre]], [[Def - Subgroup]], [[Thm - Conjugacy Classes of the Symmetric Group]], [[Thm - Orbit-Stabiliser Theorem]])
- [[Ex - A normal subgroup is a union of conjugacy classes]] (⭐⭐) — prove a [[Def - Subgroup|subgroup]] is normal if and only if it is conjugation-saturated, by reading the definition $gNg^{-1}=N$ as a fixed-set condition for the conjugation action; the principle behind every conjugacy-counting (non-)simplicity proof ([[Def - Normal Subgroup]], [[Def - Subgroup]], [[Def - Conjugacy Class]], [[Def - Simple Group]], [[Thm - Lagrange's Theorem]])
- [[Ex - Conjugacy class sizes in the symmetric group]] (⭐⭐) — derive the class-size formula $n!/\prod_k k^{a_k}a_k!$ by counting the centraliser as the wreath-product bookkeeping of shuffling equal-length cycles and rotating within each, then applying orbit-stabiliser ([[Def - Symmetric Group]], [[Def - Conjugacy Class]], [[Def - Centraliser and Centre]], [[Thm - Conjugacy Classes of the Symmetric Group]], [[Thm - Orbit-Stabiliser Theorem]])
- [[Ex - Inner automorphisms and the centre]] (⭐⭐) — show conjugation gives a homomorphism $\gamma:G\to\operatorname{Aut}(G)$ with kernel $Z(G)$ and image $\operatorname{Inn}(G)$, deduce $G/Z(G)\cong\operatorname{Inn}(G)$ and $\operatorname{Inn}(G)\trianglelefteq\operatorname{Aut}(G)$ via the first isomorphism theorem ([[Def - Automorphism Group]], [[Def - Centraliser and Centre]], [[Def - Homomorphism]], [[Def - Kernel and Image]], [[Def - Normal Subgroup]], [[Def - Subgroup]], [[Thm - First Isomorphism Theorem]])
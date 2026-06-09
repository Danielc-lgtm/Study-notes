---
type: exercise-index
subject: commutative-algebra
section: "14.1"
tags: [algebra, commutative-algebra]
---

## §14.1 Discrete Valuation Rings — Exercises

The exercises of §14.1 drill the local theory: recognizing a discrete valuation ring through each of its equivalent faces and understanding how the valuation, the ring, and the field constrain one another. The unifying skill is to treat a DVR as "the integers near one prime" — a local ring where every element is a unit times a power of the uniformizer, and where the valuation is just the exponent. The first exercise builds the prototype $\mathbb{Z}_{(p)}$ from scratch; the second proves the implications that turn "principal maximal ideal" into the full DVR structure (the operational identity "DVR = local PID, not a field"); the third explores what the valuation ring remembers about the valuation and the field. Across all three, the recurring techniques are valuation arithmetic ("read off the power of the uniformizer"), the "factor out the minimum" proof of the ultrametric inequality, and the recovery of the valuation from the ideal lattice.

- [[Ex - Z localized at p is a DVR]] (⭐) — build the prototype DVR by verifying the $p$-adic valuation $v_p$ directly: well-definedness and multiplicativity from unique factorization in ℤ, the ultrametric inequality by factoring out the minimal power of $p$, and identification of the valuation ring as $\mathbb{Z}_{(p)}$ with uniformizer $p$ and residue field $\mathbb{F}_p$ ([[Def - Discrete Valuation and Valuation Ring]], [[Def - Multiplicative Set and Localization]], [[Def - Local Ring and Residue Field]], [[Def - Prime and Maximal Ideal]]).

- [[Ex - A DVR is a PID with one maximal ideal]] (⭐⭐) — prove the implications (principal $\mathfrak{m}$) ⇒ (every ideal a power of $\mathfrak{m}$) ⇒ (every ideal is $(\pi^n)$) ⇒ (DVR), via the "element of exact order $t$" argument and Nakayama's $\mathfrak{m} \neq \mathfrak{m}^2$, concluding the operational identity "DVR = local PID that is not a field" ([[Def - Discrete Valuation and Valuation Ring]], [[Def - Principal Ideal Domain]], [[Def - Local Ring and Residue Field]], [[Thm - Characterization of Discrete Valuation Rings]], [[Commutative Algebra V — Nakayama's Lemma]]).

- [[Ex - The valuation ring of the p-adic valuation]] (⭐⭐) — determine how much the valuation ring remembers: prove the valuation ring *determines* the valuation (reading $v(x)$ off the equation $(x) = \mathfrak{m}^n$), and prove that isomorphic valuation rings force isomorphic fields (the fraction field is functorial) — resisting the framing's invitation to find a nonexistent counterexample ([[Def - Discrete Valuation and Valuation Ring]], [[Def - Local Ring and Residue Field]], [[Def - Prime and Maximal Ideal]]).

---
type: exercise-index
subject: ring-theory
section: "2.8"
tags: [algebra, ring-theory]
---

## §2.8 Hilbert's Basis Theorem — Exercises

The exercises of §2.8 drill the Noetherian condition and Hilbert's basis theorem. The non-Noetherian counterexample $\mathbb{Z}[X_1, X_2, \ldots]$ shows that infinitely many variables genuinely break the ascending chain condition; Hilbert's basis theorem (adjoining one variable preserves Noetherianity) extends inductively to all polynomial [[Def - Ring|rings]] in finitely many variables; and quotients preserve Noetherianity via the [[Def - Ideal|ideal]] correspondence. The unifying observation: "finitely generated" propagates through every finite construction (polynomial extension, quotient), but not through countable adjunctions.

- [[Ex - A ring that is not Noetherian]] (⭐⭐) — disprove the Noetherian property by exhibiting a counterexample: in $\mathbb{Z}[X_1,X_2,\dots]$ the ideal $(X_1,X_2,\dots)$ has no finite generating set, since finitely many polynomials mention finitely many variables, and an evaluation homomorphism certifies that an unmentioned variable escapes — equivalently the chain $(X_1)\subsetneq(X_1,X_2)\subsetneq\cdots$ never stabilises, breaking the ascending chain condition ([[Def - Noetherian Ring]], [[Thm - Noetherian Rings and Finitely Generated Ideals]], [[Def - Ideal]], [[Def - Polynomial Ring]], [[Def - Ring]]).

- [[Ex - Noetherianity passes to quotients and polynomial extensions]] (⭐⭐) — prove $\mathbb{Z}[X,Y]/(X^2-Y^3)$ is Noetherian by reading it as a tower over $\mathbb{Z}$: the base $\mathbb{Z}$ is a PID hence Noetherian, Hilbert's basis theorem applied twice makes $\mathbb{Z}[X,Y]$ Noetherian, and a quotient by any ideal — the generator $X^2-Y^3$ being irrelevant — descends the property via the ideal correspondence ([[Def - Noetherian Ring]], [[Thm - Hilbert's Basis Theorem]], [[Thm - Noetherian Rings and Finitely Generated Ideals]], [[Thm - Ideal Correspondence]], [[Def - Ideal]], [[Def - Polynomial Ring]], [[Def - Quotient Ring]], [[Def - Principal Ideal Domain]], [[Def - Ring]]).

- [[Ex - Hilbert's basis theorem and polynomial rings in several variables]] (⭐) — deduce the multivariate corollary by induction on the number of variables: the base rings $F$ and $\mathbb{Z}$ are Noetherian, and Hilbert's basis theorem is the inductive step "adjoin one variable, stay Noetherian," so $F[X_1,\dots,X_n]$ and $\mathbb{Z}[X_1,\dots,X_n]$ are Noetherian — hence every ideal is finitely generated, so every system of polynomial equations is equivalent to a finite subsystem ([[Def - Noetherian Ring]], [[Thm - Hilbert's Basis Theorem]], [[Thm - Noetherian Rings and Finitely Generated Ideals]], [[Def - Ideal]], [[Def - Polynomial Ring]], [[Def - Principal Ideal Domain]], [[Def - Ring]]).

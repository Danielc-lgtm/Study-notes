---
type: exercise-index
subject: ring-theory
section: "2.4"
tags: [algebra, ring-theory]
---

## §2.4 Factorization in Integral Domains — Exercises

The exercises of §2.4 drill the hierarchy $\text{ED} \subseteq \text{PID} \subseteq \text{UFD} \subseteq \text{ID}$ and the structural facts that connect the layers. Each exercise uses the *norm* as the workhorse: norms transport unit and irreducibility questions to the integers, expose the failure of unique factorisation in $\mathbb{Z}[\sqrt{-5}]$ by mismatched norm-lists, and turn the Euclidean axiom for $\mathbb{Z}[i]$ into a geometric "round to nearest lattice point" claim.

- [[Ex - Failure of unique factorization]] (⭐⭐) — push every multiplicative question in $\mathbb{Z}[\sqrt{-5}]$ through the norm $N(a+b\sqrt{-5})=a^2+5b^2$: norm-$1$ pins the units to $\pm1$, the missing norms $2,3$ make $2,3,1\pm\sqrt{-5}$ irreducible, and the mismatched norm-lists $\{4,9\}\neq\{6,6\}$ separate the two factorisations of $6$, exhibiting an irreducible ($2$) that is not prime and a non-UFD ([[Def - Integral Domain]], [[Def - Irreducible and Prime Elements]], [[Def - Unique Factorization Domain]], [[Def - Unit and Field]]).

- [[Ex - The Gaussian integers form a Euclidean domain]] (⭐⭐) — verify the Euclidean axioms for $\mathbb{Z}[i]$ with $\varphi(z)=|z|^2$: multiplicativity settles $\varphi(ab)\geq\varphi(b)$, and division-with-remainder is the geometric move of dividing in $\mathbb{C}$ and rounding to the nearest lattice point, where the unit-square covering radius gives error norm $\leq\tfrac12<1$; then chain ED $\Rightarrow$ PID $\Rightarrow$ UFD ([[Def - Integral Domain]], [[Def - Euclidean Domain]], [[Def - Principal Ideal Domain]], [[Def - Unique Factorization Domain]], [[Thm - Euclidean Domains are Principal Ideal Domains]], [[Thm - Principal Ideal Domains are Unique Factorization Domains]]).

- [[Ex - In a principal ideal domain irreducibles are prime]] (⭐⭐) — prove the key lemma making PIDs into UFDs by manufacturing a Bézout identity: form the probe [[Def - Ideal|ideal]] $(p,a)$, collapse it to $(d)$ using the PID hypothesis, force $d$ to be a unit via irreducibility of $p$ and the hypothesis $p\nmid a$, extract $1=rp+sa$, and multiply by $b$ ([[Def - Integral Domain]], [[Def - Principal Ideal Domain]], [[Def - Irreducible and Prime Elements]], [[Def - Ideal]], [[Def - Unit and Field]]).

- [[Ex - Computing a greatest common divisor in the Gaussian integers]] (⭐) — run the Euclidean algorithm in $\mathbb{Z}[i]$ on $11+7i$ and $18-i$, dividing at each step by rationalising the complex ratio with the conjugate and rounding to the nearest Gaussian integer so the norm strictly decreases; the last non-zero remainder is the gcd, defined only up to a unit, and here it is a unit so the inputs are coprime ([[Def - Euclidean Domain]], [[Def - Greatest Common Divisor and Least Common Multiple]], [[Def - Irreducible and Prime Elements]], [[Def - Unit and Field]]).

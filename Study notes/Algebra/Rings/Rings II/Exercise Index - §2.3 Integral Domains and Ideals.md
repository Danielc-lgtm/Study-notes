---
type: exercise-index
subject: ring-theory
section: "2.3"
tags: [algebra, ring-theory]
---

## §2.3 Integral Domains and Ideals — Exercises

The exercises of §2.3 drill the dictionary between ideals and their quotients: prime $\leftrightarrow$ quotient is a domain, maximal $\leftrightarrow$ quotient is a field. Each exercise practices building evaluation surjections to identify quotients explicitly, distinguishing prime from maximal in $\mathbb{Z}[X]$, and tracking the field of fractions construction. The structural fact "the characteristic of a domain is $0$ or prime" is the simplest manifestation of "subring of a domain is a domain."

- [[Ex - Prime versus maximal ideals in a polynomial ring]] (⭐⭐) — classify the ideals $(X)$ and $(2,X)$ of $\mathbb{Z}[X]$ by identifying their quotient rings: build evaluation surjections, run the first isomorphism theorem to get $\mathbb{Z}[X]/(X)\cong\mathbb{Z}$ and $\mathbb{Z}[X]/(2,X)\cong\mathbb{F}_2$, then read off primality and maximality from "domain" versus "field", exhibiting a prime ideal that is not maximal ([[Def - Prime and Maximal Ideal]], [[Def - Integral Domain]], [[Thm - Maximal and Prime Ideals via Quotients]], [[Thm - First Isomorphism Theorem for Rings]], [[Def - Polynomial Ring]], [[Def - Ideal]], [[Def - Quotient Ring]]).

- [[Ex - The field of fractions of an integral domain]] (⭐) — identify $\operatorname{Frac}(\mathbb{Z}[i])=\mathbb{Q}(i)$ and $\operatorname{Frac}(F[X])=F(X)$ by guessing a candidate field and verifying it against the universal property — smallest field containing the domain — with the substantive step being to clear denominators so every element is a ratio of elements of the domain ([[Def - Field of Fractions]], [[Thm - Existence of the Field of Fractions]], [[Def - Integral Domain]], [[Def - Polynomial Ring]], [[Def - Unit and Field]]).

- [[Ex - The characteristic of an integral domain is zero or prime]] (⭐⭐) — show $\operatorname{char}(R)$ is $0$ or prime for an integral domain $R$, by two routes: directly, a composite characteristic $mn$ gives the zero divisors $(m\cdot 1_R)(n\cdot 1_R)=0$ via the distributive law and minimality; structurally, the first isomorphism theorem embeds $\mathbb{Z}/\operatorname{char}(R)\mathbb{Z}$ as a subring of the domain, forcing it to be a domain ([[Def - Characteristic of a Ring]], [[Def - Integral Domain]], [[Thm - First Isomorphism Theorem for Rings]], [[Thm - Maximal and Prime Ideals via Quotients]], [[Def - Prime and Maximal Ideal]]).

- [[Ex - An ideal is prime exactly when its complement is multiplicatively closed]] (⭐⭐) — prove a proper ideal $P$ is prime if and only if $R\setminus P$ contains $1$ and is closed under multiplication, by recognising the two conditions as contrapositives — De Morgan turns "a product inside has a factor inside" into "a product of outsiders is an outsider" — and matching the properness side-condition to "$1$ lies outside $P$" ([[Def - Prime and Maximal Ideal]], [[Def - Ideal]], [[Def - Integral Domain]], [[Thm - Maximal and Prime Ideals via Quotients]]).

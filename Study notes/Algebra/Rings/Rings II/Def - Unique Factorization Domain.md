---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Unit and Field"
  - "Def - Integral Domain"
  - "Def - Irreducible and Prime Elements"
  - "Def - Principal Ideal Domain"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is an [[Def - Integral Domain|integral domain]] — a non-zero commutative [[Def - Ring|ring]] with $1$ and no zero divisors. A [[Def - Unit and Field|unit]] is an invertible element; an [[Def - Irreducible and Prime Elements|irreducible]] is a non-zero non-unit with no non-trivial factorisation; two elements are **associates** if they differ by a unit factor. We abbreviate "unique factorization domain" as UFD only where spelling it out would clog the prose. The symbol $\mathbb{Z}[\sqrt{-5}]$ is the subring $\{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$ of $\mathbb{C}$. The chapter symbol registry is on [[Rings II — §2.3–2.4]].

---

# Axiom Motivation

The fundamental theorem of arithmetic says every integer greater than $1$ factors into primes in *exactly one way*. This is so familiar it is easy to miss that it is two separate assertions — **existence** (a factorisation exists) and **uniqueness** (there is only one) — and that *neither is automatic* in a general [[Def - Integral Domain|integral domain]]. A unique factorization domain is the abstraction of an integral domain where both assertions hold, and the definition must be engineered carefully, because each clause is repairing a specific way the naive statement can fail.

Start with **existence**. We want every element to break down into atoms. The atoms are the [[Def - Irreducible and Prime Elements|irreducible elements]]; so clause (i) asks that every non-zero non-unit be a product of irreducibles. Why "non-zero non-unit" and not "every element"? Zero is not a product of anything sensible, and a unit is *already* as factored as it gets — a unit has no irreducible factors, and demanding it be a product of irreducibles would be false. So the domain of the existence claim is exactly the elements that *should* factor: the non-zero non-units. Even restricted thus, existence is not free. There are integral domains in which an element admits an infinite descending chain of proper factorisations and never bottoms out at irreducibles. Existence is the assertion that this pathology does not occur — that the factoring process terminates.

Now **uniqueness**, clause (ii), and this is where the design is delicate. The naive statement "the factorisation is unique" is *false even in $\mathbb{Z}$* if read literally: $6 = 2 \cdot 3 = 3 \cdot 2 = (-2)(-3)$. Two harmless ambiguities must be quotiented out. First, **order**: $2 \cdot 3$ and $3 \cdot 2$ are the same factorisation written differently, so uniqueness can only be "up to reordering the factors". Second, **associates**: $2$ and $-2$ differ by the unit $-1$, which carries no arithmetic content, so $(-2)(-3)$ is not a genuinely new factorisation of $6$. Uniqueness can only be "up to replacing factors by [[Def - Irreducible and Prime Elements|associates]]". Hence clause (ii): if $p_1 \cdots p_n = q_1 \cdots q_m$ with all $p_i, q_j$ irreducible, then $n = m$ and, after reordering, $p_i$ is an associate of $q_i$. Drop "up to order" and the definition is vacuously unsatisfiable; drop "up to associates" and even $\mathbb{Z}$ fails to qualify. Both hedges are forced — they are the *minimal* hedges that make the prototype $\mathbb{Z}$ an example.

Now the question that the whole section circles: *why is uniqueness ever a problem?* What concretely breaks? The answer is the gap between irreducible and prime. Recall [[Def - Irreducible and Prime Elements|two distinct notions]]: an element is *irreducible* if it does not factor, and *prime* if it satisfies Euclid's lemma, $p \mid xy \Rightarrow p \mid x$ or $p \mid y$. In $\mathbb{Z}[\sqrt{-5}]$ the element $2$ is irreducible but not prime, and the *symptom* of that failure is precisely a non-unique factorisation:
$$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5}),$$
two factorisations of $6$ into irreducibles whose factors are pairwise non-associate. Uniqueness fails *because* an irreducible failed to be prime. This is not a coincidence; it is the structural heart of the matter. The uniqueness argument is a cancellation-and-rematching induction — given $p_1 \cdots p_n = q_1 \cdots q_m$, you observe $p_1$ divides the product of the $q_j$, you need $p_1$ to divide *some single* $q_j$ so you can match and cancel, and *only primality delivers that*. Irreducibility alone does not. So uniqueness holds if and only if every irreducible is prime — and indeed one can prove:

> In an integral domain where every non-zero non-unit factors into irreducibles, the factorisation is unique (clause (ii) holds) **if and only if** every irreducible element is prime.

This equivalence is why "in a UFD, irreducible $=$ prime" is not an extra axiom but a *theorem* — it is logically the same as the uniqueness clause. It also explains the role of the [[Def - Principal Ideal Domain|principal ideal domain]] in the chapter: a PID is where one *proves* irreducible $\Rightarrow$ prime (via Bézout on the [[Def - Ideal|ideal]] $(p, a)$) and where the ascending chain condition delivers existence, so [[Thm - Principal Ideal Domains are Unique Factorization Domains|every PID is a UFD]].

To see the definition is exactly right, weigh the alternatives. If you defined a UFD by "every element factors into *primes* uniquely" you would have a correct but circular-feeling definition, since you would then need primes to exist in abundance. The chosen definition factors into *irreducibles* — the notion that is *easy to verify* (you just check the element does not split) — and then *derives* that irreducibles are prime as a consequence of uniqueness. That is the right division of labour: assume the cheap-to-check thing, conclude the powerful thing.

---

# The Definition

An [[Def - Integral Domain|integral domain]] $R$ is a **unique factorization domain** if both of the following hold:

**(i) Existence of factorisation.** Every non-zero element of $R$ that is not a unit can be written as a finite product of [[Def - Irreducible and Prime Elements|irreducible]] elements:
$$r = p_1 p_2 \cdots p_n, \qquad \text{each } p_i \text{ irreducible.}$$

**(ii) Uniqueness of factorisation.** If
$$p_1 p_2 \cdots p_n = q_1 q_2 \cdots q_m$$
with every $p_i$ and every $q_j$ irreducible, then $n = m$, and after reordering the $q_j$ we have that $p_i$ and $q_i$ are [[Def - Irreducible and Prime Elements|associates]] for every $i$.

Uniqueness is therefore asserted **only up to the order of the factors and up to associates** — both qualifications are essential, and without them even $\mathbb{Z}$ would fail the definition.

A theorem rather than part of the definition, but inseparable from it: **in a unique factorization domain, an element is irreducible if and only if it is prime.** (One direction holds in every integral domain. The other — irreducible $\Rightarrow$ prime — is logically equivalent to clause (ii) given clause (i).)

---

# Relate to Other Fields / Compression

A unique factorization domain is the abstraction of the **fundamental theorem of arithmetic**: it is precisely an integral domain in which that theorem holds. Number theory — gcds, lcms, coprimality, the structure of the multiplicative monoid — is exactly the mathematics that survives the move from $\mathbb{Z}$ to a general UFD, and the definition is calibrated to be the weakest hypothesis under which that mathematics still runs.

The cleanest compression is monoid-theoretic. Throw away addition and look at $R \setminus \{0\}$ under multiplication alone: it is a commutative monoid. Quotient by the units (identify associates) and you get a commutative monoid with no invertible elements but the identity. The UFD axiom says this monoid is **free commutative** — it is the free commutative monoid on the set of associate-classes of irreducibles. "Free commutative monoid on a set $S$" means $\bigoplus_{S} \mathbb{Z}_{\geq 0}$, the finite multisets of elements of $S$, with addition of multisets; an element is a product of generators in exactly one way. So a UFD is precisely an integral domain whose multiplicative structure, modulo units, is as simple as it could possibly be: a polynomial-style monoid where "factor into irreducibles" is "read off the exponent vector". This is the true name of the concept — *unique factorisation is freeness of the multiplicative monoid*.

The concept's place in the hierarchy is the other essential compression:
$$\text{Euclidean} \ \subsetneq \ \text{PID} \ \subsetneq \ \text{UFD} \ \subsetneq \ \text{integral domain},$$
with every inclusion strict. A UFD is more general than a [[Def - Principal Ideal Domain|principal ideal domain]] — every PID is a UFD by [[Thm - Principal Ideal Domains are Unique Factorization Domains]], but $\mathbb{Z}[X]$ is a UFD that is not a PID. And a UFD is strictly less general than an integral domain, with $\mathbb{Z}[\sqrt{-5}]$ the standard separating example. Crucially, "UFD" is *not* an ideal-theoretic condition the way "PID" is: it constrains the multiplicative monoid, not the ideal lattice, and that is why it is preserved by polynomial extension ($R$ a UFD $\Rightarrow R[X]$ a UFD — Gauss's theorem) while "PID" is not.

Compared with linear algebra, factoring into irreducibles is the analogue of expressing a vector in a basis: the irreducibles (up to associates) are a "multiplicative basis", and the exponents are the "coordinates". Uniqueness of factorisation is uniqueness of coordinates. The analogy is not perfect — there is no analogue of dimension, and the "coordinates" are non-negative integers, not field elements — but it correctly conveys why a UFD is a place where you can *compute*.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}$.** The integers form a unique factorization domain: this is the fundamental theorem of arithmetic, the historical source of the entire concept. Existence is repeated factoring, uniqueness is Euclid's lemma. Here irreducible, prime, and "prime number" all name the same elements.

**Is an instance — $F[X]$ for a field $F$.** Polynomials over a field factor uniquely into irreducible polynomials, because $F[X]$ is a [[Def - Euclidean Domain|Euclidean domain]], hence a [[Def - Principal Ideal Domain|principal ideal domain]], hence a UFD. The associate ambiguity is visible here: $X^2 - 1 = (X-1)(X+1) = (2X - 2)\bigl(\tfrac{1}{2}X + \tfrac{1}{2}\bigr)$ over $\mathbb{Q}$, two factorisations differing only by the unit $2$ — the same factorisation up to associates, exactly as clause (ii) permits.

**Is an instance — every principal ideal domain.** By [[Thm - Principal Ideal Domains are Unique Factorization Domains]], every PID is a UFD. So $\mathbb{Z}$, $F[X]$, and the Gaussian integers $\mathbb{Z}[i]$ are all unique factorization domains, each via the route Euclidean $\Rightarrow$ PID $\Rightarrow$ UFD.

**Is an instance — $\mathbb{Z}[X]$, a UFD that is not a PID.** The polynomial [[Def - Ring|ring]] over the integers is a unique factorization domain (Gauss's theorem: if $R$ is a UFD then so is $R[X]$). But it is *not* a principal ideal domain — the ideal $(2, X)$ is not principal. So $\mathbb{Z}[X]$ separates the two classes: it witnesses that the inclusion (PID) $\subsetneq$ (UFD) is strict, and that unique factorisation is genuinely weaker than "every ideal principal".

**Is NOT an instance — $\mathbb{Z}[\sqrt{-5}]$.** The central non-example of the chapter. In $R = \mathbb{Z}[\sqrt{-5}]$,
$$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5}).$$

> [!note]- Why this violates unique factorisation
> Using the multiplicative norm $N(a + b\sqrt{-5}) = a^2 + 5b^2$: the units are $\pm 1$ (only $N = 1$ is solvable), and $2$, $3$, $1 + \sqrt{-5}$, $1 - \sqrt{-5}$ are all *irreducible*, because $N(2) = 4$, $N(3) = 9$, $N(1 \pm \sqrt{-5}) = 6$ and there is no element of norm $2$ or $3$, so none of these can split into two non-units. Thus $6 = 2 \cdot 3$ and $6 = (1+\sqrt{-5})(1-\sqrt{-5})$ are *both* factorisations of $6$ into irreducibles. They are genuinely different: $2$ has norm $4$ while $1 \pm \sqrt{-5}$ has norm $6$, so $2$ is not an associate of either (associates have equal norm). Clause (ii) fails — $n = m = 2$ but the factors cannot be matched up to associates. Hence $\mathbb{Z}[\sqrt{-5}]$ is **not** a unique factorization domain.
>
> Existence (clause (i)) actually *does* hold here — $\mathbb{Z}[\sqrt{-5}]$ is Noetherian, so factorisations terminate. It is *uniqueness* that fails. This is the cleaner diagnosis: a UFD can fail by lacking existence or by lacking uniqueness, and $\mathbb{Z}[\sqrt{-5}]$ fails specifically on uniqueness — equivalently, it has irreducibles ($2$) that are not prime.

**Corollary — in a UFD, irreducible $\iff$ prime.** This is the operative consequence; verifying it is the best calibration check on the definition.

> [!note]- Proof that in a UFD every irreducible is prime
> Every integral domain has the direction prime $\Rightarrow$ irreducible (see [[Def - Irreducible and Prime Elements]]). For the converse, let $p$ be irreducible in a UFD $R$, and suppose $p \mid ab$, say $ab = pc$ for some $c \in R$. We show $p \mid a$ or $p \mid b$. If $a$ or $b$ is zero the claim is trivial; if $a$ or $b$ is a unit, then $p$ divides the other directly. Otherwise factor $a = \prod a_i$, $b = \prod b_j$, $c = \prod c_k$ into irreducibles by clause (i). Then
> $$\Bigl(\prod a_i\Bigr)\Bigl(\prod b_j\Bigr) \;=\; ab \;=\; pc \;=\; p \prod c_k$$
> are two factorisations of the same element into irreducibles. By uniqueness, clause (ii), the irreducible $p$ on the right must be an associate of one of the irreducibles on the left — some $a_i$ or some $b_j$. If $p$ is an associate of some $a_i$, then $p \mid a_i \mid a$; if of some $b_j$, then $p \mid b$. Either way $p \mid a$ or $p \mid b$, so $p$ is prime. $\blacksquare$

**Corollary — gcds and lcms exist in any UFD.** Because factorisation is unique, the [[Def - Greatest Common Divisor and Least Common Multiple|greatest common divisor]] of $a_1, \dots, a_n$ can be *constructed*: take each irreducible to the minimum exponent appearing across the $a_i$; the least common multiple takes the maximum. In a general integral domain gcds need not exist; the UFD axiom guarantees them.

**Calibration check.** Verify that a field is (vacuously) a unique factorization domain — it has no non-zero non-units, so clauses (i) and (ii) are empty. Verify that in $\mathbb{Z}$ the two factorisations $12 = 2 \cdot 2 \cdot 3 = 3 \cdot 2 \cdot 2$ are "the same" under clause (ii), and so are $-12 = 2 \cdot 2 \cdot (-3) = (-2) \cdot 2 \cdot 3$. Confirm you can state, in one sentence, why uniqueness fails in $\mathbb{Z}[\sqrt{-5}]$ (an irreducible is not prime) and not in $\mathbb{Z}$. If you can also explain why the definition factors into *irreducibles* rather than *primes* — irreducibility is the cheap-to-check property — the definition has fully landed.

---

# Unlocked by This

> [!tip] Greatest Common Divisor and Least Common Multiple *(from this topic)*
> The UFD axiom is exactly what makes the [[Def - Greatest Common Divisor and Least Common Multiple|greatest common divisor and least common multiple]] *exist* (and be unique up to associates): with unique factorisation in hand, gcd is "minimum exponent on each irreducible" and lcm is "maximum exponent". In a general integral domain neither need exist.

> [!tip] Gauss's Lemma and $R[X]$ *(from later ring theory)*
> If $R$ is a unique factorization domain then so is the polynomial ring $R[X]$ — this is Gauss's theorem, proved via Gauss's lemma on primitive polynomials. Iterating, $R[X_1, \dots, X_n]$ is a UFD. This is how unique factorisation reaches multivariate polynomial rings, which are *not* principal ideal domains, so the result is genuinely beyond the PID world.

> [!tip] Algebraic number theory and ideal factorisation *(from number theory)*
> The failure of unique factorisation in rings like $\mathbb{Z}[\sqrt{-5}]$ is the founding problem of algebraic number theory. The repair — due to Kummer and Dedekind — is to factor *ideals* instead of elements: in a Dedekind domain, every non-zero ideal factors uniquely into prime ideals even when elements do not factor uniquely. Unique factorisation is recovered one level up, in the ideal lattice.

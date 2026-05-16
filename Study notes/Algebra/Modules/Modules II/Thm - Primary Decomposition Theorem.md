---
type: theorem
subject: module-theory
prereqs:
  - "Def - Euclidean Domain"
  - "Def - Module"
  - "Def - Finitely Generated Module"
  - "Def - Free Module"
  - "Def - Direct Sum of Modules"
  - "Def - Irreducible and Prime Elements"
  - "Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain"
  - "Thm - Chinese Remainder Theorem for Modules"
tags: [algebra, module-theory]
---

# Notation

Throughout, $R$ is a [[Def - Euclidean Domain|Euclidean domain]] — an integral domain carrying a function $\varphi : R \setminus \{0\} \to \mathbb{Z}_{\geq 0}$ supporting division with remainder — and modules are [[Def - Module|$R$-modules]]. A non-zero, non-unit element $p \in R$ is **[[Def - Irreducible and Prime Elements|prime]]** (equivalently, in a Euclidean domain, **irreducible**) if whenever $p \mid xy$ then $p \mid x$ or $p \mid y$; **distinct primes** $p, q$ are primes that are not associates (do not differ by a unit). For $d \in R$, the ideal $(d) = \{rd : r \in R\}$ is principal and $R/(d)$ the cyclic quotient module; $R/(p^n)$, with $p$ prime and $n \geq 1$, is a **primary cyclic module** (a **$p$-primary** one). The [[Def - Free Module|free module]] $R^s$ is the [[Def - Direct Sum of Modules|direct sum]] of $s$ copies of $R$. Two elements are **coprime** if their only common divisors are units. Every non-zero non-unit of a Euclidean domain has a factorisation into primes, unique up to order and units (Euclidean domains are unique factorisation domains). The symbol $\cong$ denotes module isomorphism. The full symbol registry is on the parent page [[Modules II — §3.3–3.4]].

---

# Statement

> **Primary Decomposition Theorem.** Let $R$ be a [[Def - Euclidean Domain|Euclidean domain]] and let $M$ be a [[Def - Finitely Generated Module|finitely generated]] $R$-module. Then
> $$M \;\cong\; N_1 \oplus N_2 \oplus \dots \oplus N_t,$$
> where each summand $N_i$ is either a free copy of $R$ or a **primary cyclic module** $R/(p^n)$ for some prime $p \in R$ and some integer $n \geq 1$.

Equivalently: every finitely generated module over a Euclidean domain is a direct sum of a [[Def - Free Module|free module]] $R^s$ and finitely many modules of the single shape $R/(p^n)$, with $p$ prime. This is the **elementary-divisor form** of the classification — the finest of the canonical forms, in which every cyclic piece is governed by a *prime power*. It carries exactly the same information as the invariant-factor form of the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]]; the two are interchangeable, and the [[Thm - Chinese Remainder Theorem for Modules|Chinese remainder theorem]] is the dictionary. This page proves the existence half, exactly as the lecture notes do.

---

# Motivation

The [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] already classifies finitely generated modules over a Euclidean domain: every such module is $R/(d_1) \oplus \dots \oplus R/(d_r) \oplus R^s$ with $d_1 \mid \dots \mid d_r$. This is a complete and canonical normal form — so why is another theorem needed?

Because the moduli $d_i$ are still *composite*. A summand $R/(d)$ with $d = 12$, say, is a single cyclic module, but it is built from primes $2$ and $3$ tangled together inside the one modulus $12$. Many questions about a module are most naturally answered "one prime at a time": the part of the module governed by the prime $2$ behaves independently of the part governed by $3$, and lumping them into $R/(12)$ hides that independence. The invariant-factor form is the *coarsest* canonical form — it uses the fewest summands — but coarseness is exactly what obscures the prime-by-prime structure.

The primary decomposition is the opposite extreme: the *finest* canonical form. It breaks every cyclic summand all the way down until each is governed by a single prime power $p^n$ and cannot be broken further. The module is then displayed as a direct sum of pieces, each of which is "purely about one prime". This is the form in which the module's structure is most transparent — you can see, at a glance, how much of the module lives at each prime.

One should expect this refinement to be possible, and to be easy, because of a fact already in hand: distinct prime powers are *coprime*. If $d = p_1^{n_1} \cdots p_k^{n_k}$ is the prime factorisation of an invariant factor, then $p_1^{n_1}, \dots, p_k^{n_k}$ are pairwise coprime, and the [[Thm - Chinese Remainder Theorem for Modules|Chinese remainder theorem]] says a cyclic module splits along a coprime factorisation of its modulus:
$$\frac{R}{(d)} \;\cong\; \frac{R}{(p_1^{n_1})} \oplus \dots \oplus \frac{R}{(p_k^{n_k})}.$$
So the primary decomposition is the structure theorem followed by a coprime split of each summand. There is no new heavy machinery: the structure theorem provides the cyclic pieces, the Chinese remainder theorem grinds each one into prime-power pieces, and unique factorisation in the Euclidean domain $R$ guarantees a prime factorisation exists to grind along.

Why care about this finest form specifically? Because it is the version that yields the **Jordan normal form**. Taking $R = F[X]$, a finite-dimensional vector space with a linear operator is a finitely generated $F[X]$-module; the invariant-factor form gives the [[Thm - Rational Canonical Form|rational canonical form]], but the *primary* form — splitting each invariant factor into powers of irreducible polynomials — gives the [[Thm - Jordan Normal Form|Jordan normal form]], the decomposition into generalised eigenspaces with a single eigenvalue apiece. The Jordan blocks are exactly the primary cyclic summands $F[X]/((X - \lambda)^n)$. Primary decomposition is the abstract theorem behind the most-used canonical form in linear algebra.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is a finitely generated module over a Euclidean domain — the same precondition as the structure theorem. The skill is the same: recognising when an object is such a module.

The first disguised source is **any module already in invariant-factor form**. If a module is presented as $\bigoplus R/(d_i) \oplus R^s$ — the output of the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] — then primary decomposition applies immediately as a *post-processing step*: factor each $d_i$ and split. The non-obvious recognition is that the invariant-factor form is not the end of the road; it can always be refined further, and the refinement requires only factorising the $d_i$. *Example problem:* given $\mathbb{Z}/(12) \oplus \mathbb{Z}/(60)$, produce the primary form $\mathbb{Z}/(4) \oplus \mathbb{Z}/(3) \oplus \mathbb{Z}/(4) \oplus \mathbb{Z}/(3) \oplus \mathbb{Z}/(5)$.

The second disguised source is **a module presented by generators and relations**, or as a quotient $R^m/K$. Such a module is finitely generated, so the structure theorem applies and yields an invariant-factor form, after which primary decomposition refines it. The non-obvious step is the two-stage route: first Smith normal form of the presentation matrix to get the $d_i$, then Chinese-remainder splitting to get the prime powers. *Example problem:* an abelian group given by an integer presentation matrix — compute its Smith normal form, then split each invariant factor into prime-power cyclic groups.

The third disguised source is **a finitely generated torsion module**, in particular **a finite module over a Euclidean domain** — every element killed by some non-zero ring element. Here the free rank is $0$, so primary decomposition writes the module purely as $\bigoplus R/(p^n)$, with no free part. The non-obvious recognition is that finiteness alone forces the cleanest possible outcome: a finite module is a direct sum of primary cyclic modules, period. *Example problem:* a finite abelian group is a product of cyclic groups of prime-power order — the elementary-divisor form of the classification of finite abelian groups.

The fourth disguised source is **a vector space carrying a linear operator**. With $R = F[X]$ and $X$ acting as the operator, the vector space is a finitely generated torsion $F[X]$-module; primary decomposition splits it into primary cyclic $F[X]$-modules. The non-obvious recognition is that "operator on a vector space" is a primary-decomposition input, and the primary summands are the generalised eigenspace pieces — the Jordan blocks.

**Targets (Output Amplification)**

The bare conclusion is the decomposition into primary cyclic modules and a free part. Combined with other facts it does more.

Combine the conclusion with **specialisation to $R = F[X]$ over an algebraically closed field**. When $F$ is algebraically closed, every irreducible polynomial is linear, $p = X - \lambda$, so every primary summand is $F[X]/((X - \lambda)^n)$ — a single Jordan block. The further result is the [[Thm - Jordan Normal Form|Jordan normal form]]: every operator on a finite-dimensional vector space over an algebraically closed field is, in a suitable basis, a direct sum of Jordan blocks. This combination is non-obvious because an abstract module decomposition becomes the most concrete and most-used normal form in linear algebra.

Combine the conclusion with **grouping the summands by prime**. Collecting all the $p$-primary summands $R/(p^n)$ for a fixed prime $p$ gives the **$p$-primary component** $M_p$ of $M$, and $M$ is the direct sum of its primary components plus the free part: $M = \bigoplus_p M_p \oplus R^s$. The further result is that questions about $M$ localise — each prime can be studied in isolation, since the $p$-primary component is annihilated by a power of $p$ and untouched by other primes. This is non-obvious because it organises a single module into independent prime-by-prime strata, the algebraic analogue of localisation in geometry.

Combine the conclusion with **the structure theorem's invariant-factor form, run in reverse**. The primary form and the invariant-factor form carry the same information; from a primary decomposition one *reassembles* invariant factors by collecting, for each "rank", the largest prime power at each prime and multiplying across primes (the Chinese remainder theorem in the fusing direction). The further result is that the two canonical forms are fully interchangeable, and one converts freely between them. This is non-obvious because the two forms look unrelated — one uses composite moduli with a divisibility chain, the other uses prime-power moduli with no chain — until coprime fusion is seen as the dictionary.

Combine the conclusion with **a counting argument over a finite module**. For a finite module, the order is the product of the orders of the primary summands, and the orders of $p$-primary summands are powers of $|R/(p)|$. The further result is that the primary decomposition reduces the enumeration of finite modules of a given order to a prime-by-prime, partition-counting problem. This is non-obvious because it turns "how many modules of order $n$?" into independent combinatorial counts, one per prime dividing $n$.

---

# Why Is It True

The intuition is a single sentence: **the structure theorem gives you cyclic pieces with composite moduli, and the Chinese remainder theorem grinds each composite modulus into prime powers — coprimality is what lets the grinding lose no information.**

Start from where the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] leaves you. It has already done the hard work: it tells you a finitely generated module over a Euclidean domain is
$$M \;\cong\; \frac{R}{(d_1)} \oplus \dots \oplus \frac{R}{(d_r)} \oplus R^s.$$
The free part $R^s$ is already as simple as can be — leave it alone; it contributes its $s$ summands $R$ to the final answer untouched. The torsion summands $R/(d_i)$ are the only thing standing between this form and the primary form, and the obstruction is precisely that the moduli $d_i$ are *composite*. The whole remaining task is to break each $R/(d_i)$ into primary pieces.

Now the key fact, and it is a fact about the *ring*, not the module. $R$ is a Euclidean domain, and Euclidean domains are unique factorisation domains. So every non-zero non-unit $d_i$ has a prime factorisation
$$d_i \;=\; p_1^{n_1}\, p_2^{n_2} \cdots p_k^{n_k}$$
with $p_1, \dots, p_k$ *distinct* primes (gather repeated primes into a single power). This factorisation is the raw material; it exists for free, supplied by the arithmetic of $R$.

Here is the move that does the splitting. Distinct primes $p_j$ and $p_l$ share no irreducible factor, so the prime powers $p_j^{n_j}$ and $p_l^{n_l}$ are **pairwise coprime** — and a power of one prime is coprime to the *product* of powers of all the others. So the modulus $d_i$ factors, repeatedly, into coprime pairs: $d_i = p_1^{n_1} \cdot (p_2^{n_2} \cdots p_k^{n_k})$, with the two factors coprime; then the second factor splits again, $p_2^{n_2} \cdot (p_3^{n_3} \cdots p_k^{n_k})$, again coprime; and so on. Each coprime split is exactly the hypothesis of the [[Thm - Chinese Remainder Theorem for Modules|Chinese remainder theorem]], which says a cyclic module breaks along a coprime factorisation of its modulus:
$$\frac{R}{(ab)} \;\cong\; \frac{R}{(a)} \oplus \frac{R}{(b)} \qquad (\gcd(a, b) = 1).$$
Apply it once: $R/(d_i) \cong R/(p_1^{n_1}) \oplus R/(p_2^{n_2} \cdots p_k^{n_k})$. Apply it to the second summand: $R/(p_2^{n_2} \cdots p_k^{n_k}) \cong R/(p_2^{n_2}) \oplus R/(p_3^{n_3} \cdots p_k^{n_k})$. Iterate down the list. After $k - 1$ applications,
$$\frac{R}{(d_i)} \;\cong\; \frac{R}{(p_1^{n_1})} \oplus \frac{R}{(p_2^{n_2})} \oplus \dots \oplus \frac{R}{(p_k^{n_k})},$$
a direct sum of primary cyclic modules. The composite cyclic summand has been ground completely into prime-power dust.

Do this to *every* torsion summand $R/(d_1), \dots, R/(d_r)$, leave the free part as it is, and collect everything:
$$M \;\cong\; \underbrace{\bigoplus_{i=1}^r \bigoplus_{j} \frac{R}{(p_{i,j}^{\,n_{i,j}})}}_{\text{primary cyclic pieces}} \;\oplus\; \underbrace{R^s}_{\text{free part}}.$$
Every summand is now either $R$ or $R/(p^n)$ — which is exactly the claim.

So the theorem is true for the reason the slogan says, and the division of labour is clean. The *structure theorem* did the genuinely hard part: it turned an arbitrary finitely generated module into a direct sum of cyclic pieces, by diagonalising relations via Smith normal form. The *Chinese remainder theorem* does the refinement: it splits each cyclic piece along the prime factorisation of its modulus. And *unique factorisation in $R$* — automatic in a Euclidean domain — guarantees that prime factorisation exists, so there is always a coprime factorisation to feed the Chinese remainder theorem. Primary decomposition is not a new deep theorem; it is the structure theorem with a coprime-splitting rinse applied to each summand.

---

# What Makes This Hard

The genuine difficulty is *not* in this theorem at all — it is in its two inputs, the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] (which diagonalises relations via Smith normal form) and the [[Thm - Chinese Remainder Theorem for Modules|Chinese remainder theorem]] (which consumes coprimality through a Bézout relation); once those are granted, primary decomposition is a short assembly, and the main conceptual hazard is not noticing how little is left to do. The one technical point that must be got right is *why distinct prime powers are coprime* — a power $p^n$ and the product $p_2^{n_2} \cdots p_k^{n_k}$ of powers of other primes share no irreducible factor, which is exactly what licenses each application of the Chinese remainder theorem — and the common error is to apply the Chinese remainder theorem to factors that are *not* coprime (for instance splitting $R/(p^2)$ as $R/(p) \oplus R/(p)$, which is false: $p$ and $p$ are not coprime, and $R/(p^2)$ is *indecomposable*). When returning to this theorem after months, the rederivation effort belongs on the iterated coprime split, not on any hard new idea.

---

# Rederivation Scaffold

**High-level strategy:**
Take the structure theorem as a known input: $M \cong \bigoplus R/(d_i) \oplus R^s$. Leave the free part alone. For each torsion summand $R/(d_i)$, factor $d_i$ into prime powers using unique factorisation in $R$, then apply the Chinese remainder theorem iteratively to split $R/(d_i)$ into a direct sum of primary cyclic modules $R/(p^n)$. Collect everything.

**Subgoal decomposition:**

1. **Reduce to splitting one cyclic summand.** Invoke the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] to write $M \cong \bigoplus_{i} R/(d_i) \oplus R^s$; observe the free part is already in the required form, so it suffices to put each $R/(d_i)$ into primary form.
   - *Hint:* The theorem's claim allows summands $R$ and $R/(p^n)$; $R^s$ supplies the $R$'s, the $R/(d_i)$ must supply the $R/(p^n)$'s.
   - *Why needed:* It isolates the only remaining work — refining a single composite cyclic module.

2. **Factor the modulus into prime powers.** For each $i$, use that $R$ is a unique factorisation domain (every Euclidean domain is) to write $d_i = p_1^{n_1} \cdots p_k^{n_k}$ with the $p_j$ distinct primes.
   - *Hint:* Gather repeated prime factors into a single power; "distinct" means pairwise non-associate.
   - *Why needed:* It produces the coprime factorisation that the Chinese remainder theorem requires.

3. **Verify the prime powers are pairwise coprime.** Show that for distinct primes $p_j, p_l$ the powers $p_j^{n_j}, p_l^{n_l}$ are coprime, and that $p_1^{n_1}$ is coprime to the product $p_2^{n_2} \cdots p_k^{n_k}$.
   - *Hint:* Distinct primes share no irreducible factor; a common divisor of $p_j^{n_j}$ and $p_l^{n_l}$ would be a unit.
   - *Why needed:* Coprimality is the exact hypothesis of the Chinese remainder theorem.

4. **Split each cyclic summand by the iterated Chinese remainder theorem.** Apply $R/(ab) \cong R/(a) \oplus R/(b)$ for coprime $a, b$ repeatedly, peeling off one prime power at a time, to obtain $R/(d_i) \cong \bigoplus_j R/(p_j^{n_j})$.
   - *Hint:* First split off $p_1^{n_1}$ from the rest; then recurse on $R/(p_2^{n_2} \cdots p_k^{n_k})$.
   - *Why needed:* It performs the refinement, turning each composite cyclic module into primary cyclic modules.

---

# Lemma Decomposition

> [!note]- Lemma 1: Distinct prime powers are pairwise coprime
> **Statement:** Let $p_1, \dots, p_k$ be distinct primes in a Euclidean domain $R$ and $n_1, \dots, n_k \geq 1$. Then for $j \neq l$ the elements $p_j^{n_j}$ and $p_l^{n_l}$ are coprime; more generally, $p_j^{n_j}$ is coprime to the product $\prod_{l \neq j} p_l^{n_l}$.
>
> **Hint:** A common divisor would contain an irreducible factor shared by two distinct primes — impossible.
>
> **Why needed:** Coprimality is the precise hypothesis of the Chinese remainder theorem; without it the splitting step is illegal.
>
> > [!note]- Full proof
> > Suppose $c$ is a common divisor of $p_j^{n_j}$ and $p_l^{n_l}$ with $j \neq l$. If $c$ were a non-unit, it would have an [[Def - Irreducible and Prime Elements|irreducible]] factor $q$. Then $q \mid p_j^{n_j}$, and since $q$ is prime, $q \mid p_j$; as $p_j$ is itself irreducible, $q$ is an associate of $p_j$. Symmetrically $q \mid p_l^{n_l}$ forces $q$ to be an associate of $p_l$. Hence $p_j$ and $p_l$ would be associates — contradicting that they are *distinct* primes. So every common divisor $c$ is a unit, i.e. $\gcd(p_j^{n_j}, p_l^{n_l}) = 1$.
> >
> > For the general claim, let $c$ be a common divisor of $p_j^{n_j}$ and $\prod_{l \neq j} p_l^{n_l}$. Any irreducible factor $q$ of $c$ divides $p_j^{n_j}$, hence is an associate of $p_j$; but $q$ also divides $\prod_{l \neq j} p_l^{n_l}$, so by primality $q$ divides some $p_l^{n_l}$ with $l \neq j$, hence is an associate of $p_l$ — again forcing $p_j, p_l$ associate, a contradiction. So $c$ is a unit and $p_j^{n_j}$ is coprime to $\prod_{l \neq j} p_l^{n_l}$. $\blacksquare$

> [!note]- Lemma 2: A composite cyclic module splits into primary cyclic modules
> **Statement:** Let $d \in R$ be a non-zero non-unit with prime factorisation $d = p_1^{n_1} \cdots p_k^{n_k}$, the $p_j$ distinct primes. Then
> $$\frac{R}{(d)} \;\cong\; \frac{R}{(p_1^{n_1})} \oplus \frac{R}{(p_2^{n_2})} \oplus \dots \oplus \frac{R}{(p_k^{n_k})}.$$
>
> **Hint:** Peel off one prime power at a time with the Chinese remainder theorem; at each step the peeled factor is coprime to the rest by Lemma 1.
>
> **Why needed:** It is the refinement step — it converts each torsion summand of the structure theorem into primary form.
>
> > [!note]- Full proof
> > Argue by induction on the number $k$ of distinct primes. If $k = 1$ then $d = p_1^{n_1}$ and $R/(d) = R/(p_1^{n_1})$ is already primary; there is nothing to do.
> >
> > Suppose $k \geq 2$ and the result holds for fewer than $k$ primes. Write $d = a \cdot b$ with $a = p_1^{n_1}$ and $b = p_2^{n_2} \cdots p_k^{n_k}$. By Lemma 1, $a$ and $b$ are coprime. By the [[Thm - Chinese Remainder Theorem for Modules|Chinese remainder theorem]] for modules over a Euclidean domain,
> > $$\frac{R}{(d)} \;=\; \frac{R}{(ab)} \;\cong\; \frac{R}{(a)} \oplus \frac{R}{(b)} \;=\; \frac{R}{(p_1^{n_1})} \oplus \frac{R}{(p_2^{n_2} \cdots p_k^{n_k})}.$$
> > The second summand $R/(p_2^{n_2} \cdots p_k^{n_k})$ is a cyclic module whose modulus is a product of $k - 1$ distinct prime powers, so by the inductive hypothesis
> > $$\frac{R}{(p_2^{n_2} \cdots p_k^{n_k})} \;\cong\; \frac{R}{(p_2^{n_2})} \oplus \dots \oplus \frac{R}{(p_k^{n_k})}.$$
> > Combining the two displays,
> > $$\frac{R}{(d)} \;\cong\; \frac{R}{(p_1^{n_1})} \oplus \frac{R}{(p_2^{n_2})} \oplus \dots \oplus \frac{R}{(p_k^{n_k})},$$
> > a direct sum of primary cyclic modules. By induction the result holds for all $k$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be a [[Def - Euclidean Domain|Euclidean domain]] and $M$ a [[Def - Finitely Generated Module|finitely generated]] $R$-module.
>
> **Step 1 — apply the structure theorem.** By the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem for finitely generated modules over a Euclidean domain]], there are non-zero non-unit elements $d_1, \dots, d_r \in R$ and an integer $s \geq 0$ with
> $$M \;\cong\; \frac{R}{(d_1)} \oplus \frac{R}{(d_2)} \oplus \dots \oplus \frac{R}{(d_r)} \oplus \underbrace{R \oplus \dots \oplus R}_{s}.$$
> The $s$ free summands $R$ are already of the form permitted in the conclusion. It therefore suffices to put each torsion summand $R/(d_i)$ into a direct sum of primary cyclic modules.
>
> **Step 2 — factor each modulus into prime powers.** Fix $i$. Since $R$ is a Euclidean domain, it is a unique factorisation domain, so the non-zero non-unit $d_i$ has a prime factorisation
> $$d_i \;=\; p_1^{n_1}\, p_2^{n_2} \cdots p_k^{n_k},$$
> where $p_1, \dots, p_k$ are distinct primes (repeated prime factors gathered into a single power) and each $n_j \geq 1$. (Here $k$, the $p_j$, and the $n_j$ depend on $i$; the notation is kept light.)
>
> **Step 3 — the prime powers are pairwise coprime.** By Lemma 1, distinct primes share no irreducible factor, so for $j \neq l$ the prime powers $p_j^{n_j}$ and $p_l^{n_l}$ are coprime, and $p_1^{n_1}$ is coprime to the product $p_2^{n_2} \cdots p_k^{n_k}$.
>
> **Step 4 — split each cyclic summand by the iterated Chinese remainder theorem.** By Lemma 2 — which applies the [[Thm - Chinese Remainder Theorem for Modules|Chinese remainder theorem]] $R/(ab) \cong R/(a) \oplus R/(b)$ (for coprime $a, b$) repeatedly, peeling off one prime power at a time —
> $$\frac{R}{(d_i)} \;\cong\; \frac{R}{(p_1^{n_1})} \oplus \frac{R}{(p_2^{n_2})} \oplus \dots \oplus \frac{R}{(p_k^{n_k})}.$$
> Each summand on the right is a primary cyclic module $R/(p^n)$.
>
> **Step 5 — assemble.** Performing Steps 2–4 for every index $i = 1, \dots, r$ and substituting into the decomposition of Step 1,
> $$M \;\cong\; \left( \bigoplus_{i=1}^{r} \bigoplus_{j} \frac{R}{(p_{i,j}^{\,n_{i,j}})} \right) \oplus \underbrace{R \oplus \dots \oplus R}_{s},$$
> where $p_{i,j}$ denotes the $j$-th prime in the factorisation of $d_i$. Every summand is either a free copy of $R$ or a primary cyclic module $R/(p^n)$. Relabelling the summands $N_1, \dots, N_t$,
> $$M \;\cong\; N_1 \oplus N_2 \oplus \dots \oplus N_t,$$
> with each $N_i$ equal to $R$ or to $R/(p^n)$ for a prime $p$ and an integer $n \geq 1$. This is the required decomposition. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Jordan normal form of a matrix.** Let $\alpha$ be a linear operator on a finite-dimensional vector space $V$ over an algebraically closed field $F$; make $V$ an $F[X]$-module via $X \cdot v = \alpha(v)$. The polynomial ring $F[X]$ is a Euclidean domain and $V$ is a finitely generated torsion $F[X]$-module, so primary decomposition writes $V$ as a direct sum of primary cyclic modules $F[X]/(p^n)$. Because $F$ is algebraically closed, every irreducible $p$ is linear, $p = X - \lambda$, so each summand is $F[X]/((X - \lambda)^n)$ — and that is precisely a single **Jordan block** of eigenvalue $\lambda$ and size $n$. The non-obvious recognition is that the [[Thm - Jordan Normal Form|Jordan normal form]] *is* the primary decomposition theorem applied with $R = F[X]$.

**The elementary-divisor form of a finite abelian group.** A finite abelian group is a finite $\mathbb{Z}$-module; primary decomposition writes it as a direct sum of primary cyclic groups $\mathbb{Z}/(p^n) = C_{p^n}$, with no free part since the group is finite. This is the elementary-divisor form of the [[Thm - Classification of Finitely Generated Abelian Groups|classification of abelian groups]] — for example $C_{12} \times C_{60}$ decomposes as $C_4 \times C_3 \times C_4 \times C_3 \times C_5$. The non-obvious application is that the prime-power form of the classification of finite abelian groups, often proved separately, is this single theorem with $R = \mathbb{Z}$.

**Primary decomposition of an ideal in a Dedekind-like setting.** In the ring of Gaussian integers $\mathbb{Z}[i]$ — a Euclidean domain — a quotient $\mathbb{Z}[i]/(z)$ regarded as a $\mathbb{Z}[i]$-module decomposes, via primary decomposition, along the factorisation of $z$ into Gaussian primes. The non-obvious recognition is that the way a rational prime splits in $\mathbb{Z}[i]$ (for instance $5 = (2+i)(2-i)$) is read off the primary decomposition of $\mathbb{Z}[i]/(5)$, connecting the abstract theorem to the splitting of primes in number theory.

**Generalised eigenspace decomposition over a non-closed field.** Let $\alpha$ act on a vector space over a field $F$ that is *not* algebraically closed. Primary decomposition with $R = F[X]$ still applies, but the irreducible polynomials $p$ need not be linear, so the primary summands are $F[X]/(p^n)$ with $\deg p > 1$ possible. The non-obvious application is that the decomposition into generalised eigenspaces survives over any field — it is the primary decomposition — but the pieces are governed by irreducible polynomials rather than by single eigenvalues, which is exactly why the rational canonical form, not the Jordan form, is the field-agnostic normal form.

---

# Bridges

- **[[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|Structure Theorem]]** — the supplier of the cyclic pieces. Primary decomposition takes the structure theorem's invariant-factor form $\bigoplus R/(d_i) \oplus R^s$ as its starting point and refines it; the structure theorem does the genuinely hard work (diagonalising relations via Smith normal form), and primary decomposition only splits each resulting summand.

- **[[Thm - Chinese Remainder Theorem for Modules|Chinese Remainder Theorem for Modules]]** — the engine of the refinement. Each step of the splitting $R/(d_i) \cong \bigoplus R/(p_j^{n_j})$ is one application of the Chinese remainder theorem to a coprime factorisation; the theorem is invoked, iterated, once per prime in each modulus.

- **[[Thm - Classification of Finitely Generated Abelian Groups|Classification of Finitely Generated Abelian Groups]]** — the case $R = \mathbb{Z}$. Primary decomposition over $\mathbb{Z}$ produces the elementary-divisor form of a finitely generated abelian group: a product of prime-power cyclic groups $C_{p^n}$ and copies of $\mathbb{Z}$, the finest canonical form of the classification.

- **[[Thm - Jordan Normal Form|Jordan Normal Form]]** — the case $R = F[X]$ over an algebraically closed field. A finite-dimensional vector space with a linear operator is a finitely generated torsion $F[X]$-module; primary decomposition splits it into primary cyclic modules $F[X]/((X-\lambda)^n)$, and these are exactly the Jordan blocks. Over a non-closed field the same theorem yields the [[Thm - Rational Canonical Form|rational canonical form]] instead.

- **Invariant-Factor versus Elementary-Divisor Forms** — the two canonical forms are interchangeable, and primary decomposition is the *passage from invariant factors to elementary divisors*. The reverse passage — fusing prime-power summands across distinct primes back into invariant factors — is the Chinese remainder theorem run in the opposite direction; the two forms carry identical information.

---

# Unlocked by This

> [!tip] Jordan Normal Form *(from Linear Algebra)*
> Taking $R = F[X]$ with $F$ algebraically closed, primary decomposition of the $F[X]$-module attached to a linear operator splits the space into pieces $F[X]/((X-\lambda)^n)$ — the Jordan blocks. The [[Thm - Jordan Normal Form|Jordan normal form]] is precisely the primary decomposition theorem in disguise, and the multiplicities of the blocks are the elementary divisors of the operator.

> [!tip] Primary Decomposition of Ideals and Modules *(from Commutative Algebra)*
> Over a general Noetherian ring, every ideal (and every module) has a primary decomposition — a representation as an intersection of primary ideals, the Lasker–Noether theorem. The theorem on this page is the cleanest, fully-explicit case: over a Euclidean domain, the decomposition is a *direct sum* of primary cyclic modules, with the primary components indexed by the primes of $R$.

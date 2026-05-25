---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Quotient Ring"
  - "Def - Unit and Field"
  - "Def - Integral Domain"
  - "Def - Prime and Maximal Ideal"
  - "Thm - Ideal Correspondence"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is a nonzero commutative [[Def - Ring|ring]] with $1_R \neq 0_R$, and $I \trianglelefteq R$ is an [[Def - Ideal|ideal]]. The [[Def - Quotient Ring|quotient ring]] $R/I$ has elements the cosets $r + I$, zero $0_{R/I} = 0_R + I = I$, and identity $1_{R/I} = 1_R + I$; the canonical quotient map is $\pi : R \to R/I$, $\pi(r) = r + I$. An ideal $I$ is **[[Def - Prime and Maximal Ideal|maximal]]** if $I \neq R$ and no ideal lies strictly between $I$ and $R$; it is **[[Def - Prime and Maximal Ideal|prime]]** if $I \neq R$ and $ab \in I$ implies $a \in I$ or $b \in I$. A **[[Def - Unit and Field|field]]** is a nonzero ring in which every nonzero element is a unit; an **[[Def - Integral Domain|integral domain]]** is a nonzero ring with no zero divisors. We write $\trianglelefteq$ for "is an ideal of", $\leq$ for "is a subring of", $\cong$ for ring isomorphism. The full symbol registry is on the parent page [[Rings II — §2.3–2.4]].

---

# Statement

> **Maximal and prime ideals via quotients.** Let $R$ be a nonzero commutative ring. Then:
>
> 1. **(Field criterion.)** $R$ is a [[Def - Unit and Field|field]] if and only if its only [[Def - Ideal|ideals]] are $\{0\}$ and $R$.
> 2. **(Maximal $\iff$ field quotient.)** An ideal $I \trianglelefteq R$ is [[Def - Prime and Maximal Ideal|maximal]] if and only if the [[Def - Quotient Ring|quotient]] $R/I$ is a field.
> 3. **(Prime $\iff$ domain quotient.)** An ideal $I \trianglelefteq R$ is [[Def - Prime and Maximal Ideal|prime]] if and only if $R/I$ is an [[Def - Integral Domain|integral domain]].
> 4. **(Maximal $\implies$ prime.)** Every maximal ideal of $R$ is prime.
>
> Statements 2 and 3 translate a property of the ideal $I$ into a property of the *quotient ring* $R/I$; statement 4 follows because every field is an integral domain.

---

# Motivation

You have two kinds of object and want a dictionary between them. On one side are *ideals* $I \trianglelefteq R$ — subsets of $R$ closed under addition and under multiplication by anything in $R$. On the other side are *quotient [[Def - Ring|rings]]* $R/I$ — whole new rings built by collapsing $I$ to zero. The two are joined at the hip: every ideal produces a quotient, every quotient comes from an ideal. The natural question is whether *properties* travel across this bridge. If I impose a condition on the ideal $I$, what does it say about the ring $R/I$, and conversely?

This package answers the question for the two most important ideal conditions, "maximal" and "prime", and the answer is as clean as one could hope. Maximality of $I$ — an *external*, lattice-theoretic statement that there is no room between $I$ and $R$ — translates into the *internal* statement that $R/I$ is a field. Primality of $I$ — an *external* divisibility-flavoured statement, $ab \in I \Rightarrow a \in I$ or $b \in I$ — translates into the internal statement that $R/I$ is an integral domain. The two definitions of ideals that looked unrelated and slightly arbitrary are revealed to be exactly the ideals whose quotients are the two best kinds of ring.

Why does this matter? Because it converts a hard question into an easy one, in both directions. Suppose you want to prove an ideal is maximal — directly, you would have to survey every ideal above it and rule out an intermediate one, a search over a potentially huge lattice. The theorem replaces that search with a single computation: identify the ring $R/I$, and check whether it is a field. That is how one knows $(X^2+1)$ is maximal in $\mathbb{R}[X]$ — because $\mathbb{R}[X]/(X^2+1) \cong \mathbb{C}$ is a field — and $(7)$ is maximal in $\mathbb{Z}$ because $\mathbb{Z}/7\mathbb{Z}$ is. Conversely, the package lets you certify a ring as a field or a domain by exhibiting it as a quotient by an ideal of the right type. And statement 4 — every maximal ideal is prime — which would be awkward to see directly from the definitions, becomes a one-line corollary: maximal gives a field quotient, a field is a domain, a domain quotient gives prime.

The whole package is *one coherent result*, and the glue holding it together is the [[Thm - Ideal Correspondence|ideal correspondence]]: the bijection between ideals of $R/I$ and ideals of $R$ lying above $I$. The field criterion (statement 1) describes rings with the simplest possible ideal lattice; the ideal correspondence transports that description across the quotient; and statements 2 and 4 fall out. Statement 3 is proved directly but belongs in the same package because it has the identical shape — a property of $I$ read off from the quotient.

---

# Sources and Targets

**Sources (Input Broadening)**

The package has several entry points, and the skill is recognising which statement a problem is secretly asking for.

The first disguised source is **a request to prove an ideal is maximal**. The property $B$ is "I must show $I$ is maximal". The bridge is statement 2: rather than ruling out intermediate ideals, *compute the quotient ring $R/I$ and check it is a field*. The non-obvious part is that an assertion about the *lattice of ideals above $I$* is equivalent to an assertion about a *single ring*, which is usually far easier to inspect. *Example problem:* show $(X^2+1) \trianglelefteq \mathbb{R}[X]$ is maximal — identify $\mathbb{R}[X]/(X^2+1) \cong \mathbb{C}$, a field.

The second disguised source is **a request to prove an ideal is prime**, where the property $B$ is "$ab\in I\Rightarrow a\in I$ or $b\in I$ is wanted". The bridge is statement 3: exhibit $R/I$ as an integral domain. The non-obvious step is that a divisibility condition on $I$ becomes a no-zero-divisors condition on the quotient. *Example problem:* show $(X) \trianglelefteq \mathbb{Z}[X,Y]$ is prime by noting $\mathbb{Z}[X,Y]/(X) \cong \mathbb{Z}[Y]$ is a domain.

The third disguised source is **a surjective ring homomorphism $\varphi : R \twoheadrightarrow T$**. The property $B$ is "there is a surjection onto $T$, and $T$ is a field (resp. a domain)". By the first isomorphism theorem $R/\ker\varphi \cong T$, so $\ker\varphi$ is maximal (resp. prime) by statement 2 (resp. 3). The non-obviousness: primality and maximality of an ideal — internal multiplicative conditions — are *read off an external map* into a recognisable ring. *Example problem:* the evaluation map $k[X_1,\dots,X_n]\to k$, $f\mapsto f(a)$, is onto a field, so its kernel $(X_1-a_1,\dots,X_n-a_n)$ is a maximal ideal.

The fourth disguised source is **a maximal ideal where primality is needed**. The property $B$ is simply "$I$ is maximal", and statement 4 hands you primality for free. The non-obvious value is that one need not re-examine the divisibility condition at all. *Example problem:* in any argument that needs a prime ideal, a maximal ideal already qualifies.

**Targets (Output Amplification)**

The conclusions are "$R/I$ is a field", "$R/I$ is a domain", or "$I$ is prime/maximal".

Combine "$R/I$ is a field" with **the ideal correspondence**. A field has only the ideals $\{0\}$ and itself, and via [[Thm - Ideal Correspondence|the correspondence]] those pull back to "$I$ and $R$ are the only ideals above $I$" — which is maximality. The further result $E$ is that maximality and field-quotient are *not just related but equivalent*, each computable from the other; this is the engine that lets statement 4 be a one-liner.

Combine "$R/I$ is a domain" with **finiteness of $R/I$**. If $R/I$ is a finite domain, then by [[Thm - Finite Integral Domains are Fields|finite integral domains are fields]] it is in fact a field, so $I$ is in fact maximal. The further result $E$: **a prime ideal of finite index is maximal**. This is non-obvious because primality looks strictly weaker than maximality, yet finiteness collapses the gap.

Combine "$R/I$ is a domain" with **the field-of-fractions construction**. A domain $R/I$ embeds in its field of fractions ([[Thm - Existence of the Field of Fractions|existence of the field of fractions]]), so a prime quotient always sits inside a field. The further result $E$ is the *residue field at a prime* — the fraction field of $R/P$ — a central object in commutative algebra and geometry, available the instant $P$ is prime.

Combine statement 4 with **the contrapositive**. Statement 4 says maximal $\Rightarrow$ prime; contrapositively, *not prime* $\Rightarrow$ *not maximal*. The further result $E$ is a quick disqualification: to show an ideal is not maximal, it suffices to show it is not prime, e.g. by exhibiting a product landing in $I$ with neither factor in $I$. The strictness of the implication (prime does not imply maximal) is witnessed by $\{0\}\subseteq\mathbb{Z}$ — prime, since $\mathbb{Z}$ is a domain, but not maximal.

---

# Why Is It True

The package looks like four facts; it is really one idea applied in different costumes. The idea: *a property of the ideal $I$ should be visible as a property of the ring $R/I$, because $R/I$ is what $R$ becomes once you declare the elements of $I$ to be zero.* Run that slogan through each statement.

**Statement 1, the field criterion.** Why should "field" be the same as "only ideals $\{0\}$ and $R$"? An ideal is a subset closed under multiplication by everything in the ring. The instant an ideal $I$ contains a *unit* $u$, it must contain $u^{-1}u = 1$, and then it contains $r\cdot 1 = r$ for every $r$ — so $I$ is all of $R$. Now, in a field every nonzero element is a unit. So any ideal that contains *anything* nonzero contains a unit, hence is the whole ring; the only escape is to contain nothing nonzero, i.e. to be $\{0\}$. That is the forward direction. Backwards: if the only ideals are $\{0\}$ and $R$, take any nonzero $x$ and form the *principal ideal* $(x)$ — the set of all multiples of $x$. It contains $x \neq 0$, so it is not $\{0\}$, so it must be $R$; in particular $1 \in (x)$, meaning $1 = xu$ for some $u$, so $x$ has an inverse. Every nonzero element is a unit: $R$ is a field. The deep content: **fields are precisely the rings with the simplest possible ideal lattice** — a two-element lattice. Having few ideals and having lots of inverses are the same phenomenon, because an inverse is exactly what blows a principal ideal up to the whole ring.

**Statement 2, maximal $\iff$ field quotient.** Here is where the [[Thm - Ideal Correspondence|ideal correspondence]] does the work. The correspondence is a perfect, inclusion-preserving dictionary: ideals of $R/I$ $\longleftrightarrow$ ideals of $R$ that contain $I$. Apply statement 1 *inside the ring $R/I$*: "$R/I$ is a field" means "$R/I$ has only the ideals $\{0\}$ and $R/I$". Translate each side of that through the dictionary. The zero ideal of $R/I$ corresponds to $I$ itself; the whole ring $R/I$ corresponds to $R$. So "$R/I$ has only those two ideals" becomes "$R$ has only $I$ and $R$ among ideals containing $I$" — and that is *verbatim the definition of $I$ being maximal*: nothing strictly between $I$ and $R$. Maximality of $I$ and field-ness of $R/I$ are the same statement, viewed on the two sides of the correspondence.

**Statement 3, prime $\iff$ domain quotient.** This one is even more transparent — it is almost a tautology once you write down what the quotient multiplication is. Multiplication in $R/I$ is defined by $(a+I)(b+I) = ab + I$. Now, "$R/I$ is a domain" means: a product of [[Def - Coset|cosets]] is zero only if a factor is zero, i.e. $ab + I = 0_{R/I}$ forces $a + I = 0_{R/I}$ or $b + I = 0_{R/I}$. Unwind each coset equation: "$ab+I = 0_{R/I}$" means $ab \in I$; "$a+I = 0_{R/I}$" means $a \in I$. So "$R/I$ a domain" reads, letter for letter, as "$ab \in I \Rightarrow a \in I$ or $b \in I$" — which is *exactly the definition of $I$ prime*. The notion of a prime ideal was, in effect, reverse-engineered from the demand "make the quotient a domain". It only looks like a separate concept because the definition is usually stated before the quotient.

**Statement 4, maximal $\implies$ prime.** Now the package pays off. You have a chain of equivalences:
$$I \text{ maximal} \overset{(2)}{\iff} R/I \text{ is a field} \implies R/I \text{ is a domain} \overset{(3)}{\iff} I \text{ prime}.$$
The only non-equivalence in the chain is the middle implication "field $\Rightarrow$ domain", and that holds because an invertible element can never be a zero divisor: if $ab = 0$ and $b$ is a unit, then $a = a(bb^{-1}) = (ab)b^{-1} = 0$. So maximal forces prime. The converse fails exactly because "field $\Rightarrow$ domain" does not reverse — there are domains that are not fields, $\mathbb{Z}$ being the standard one, and correspondingly the prime ideal $\{0\}\subseteq\mathbb{Z}$ is not maximal.

The unifying picture: there is a ladder of niceness for rings — *field* is strictly better than *integral domain* — and a parallel ladder for ideals — *maximal* is strictly better than *prime*. The two ladders are not analogous by coincidence; they are the *same ladder*, related rung-for-rung by the quotient construction. The theorem is the statement that the dictionary "$I \leftrightarrow R/I$" carries one ladder onto the other.

---

# What Makes This Hard

The proof is not technically hard — each statement is short — so the difficulty is *seeing it as one structure rather than four scattered facts*, and remembering that the [[Thm - Ideal Correspondence|ideal correspondence]] is the load-bearing tool for statement 2 (not a direct lattice argument). The single non-obvious move is, in the field criterion, to form the *principal ideal $(x)$ generated by a nonzero element* and observe that $1 \in (x)$ exactly when $x$ is a unit — turning "$(x) = R$" into "$x$ invertible". The most common error is to prove statement 4 (maximal $\Rightarrow$ prime) directly from the definitions, fighting with intermediate ideals and divisibility, instead of routing through the quotients where it is the trivial implication "field $\Rightarrow$ domain".

---

# Rederivation Scaffold

**High-level strategy:**
Prove the field criterion first — it is the bedrock. Then get maximality from it by transporting through the [[Thm - Ideal Correspondence|ideal correspondence]] applied to $R/I$. Prove the prime characterisation directly by unwinding the definition of quotient multiplication. Finally, chain the equivalences through "every field is a domain" to get maximal $\Rightarrow$ prime.

**Subgoal decomposition:**

1. **Field criterion.** Show: $R$ is a field $\iff$ its only ideals are $\{0\}$ and $R$.
   - *Hint:* Forward — an ideal containing a unit contains $1$, hence everything; in a field every nonzero element is a unit. Backward — for nonzero $x$, the principal ideal $(x)$ is not $\{0\}$, so equals $R$, so $1\in(x)$ and $x$ is a unit.
   - *Why needed:* It is the prototype; statement 2 is this statement transported across the quotient.

2. **Maximal $\iff$ field quotient.** Show $I$ maximal $\iff R/I$ a field.
   - *Hint:* By statement 1, $R/I$ is a field if and only if its only ideals are $\{0\}$ and $R/I$. By the [[Thm - Ideal Correspondence|ideal correspondence]], the ideals of $R/I$ correspond to the ideals of $R$ containing $I$; $\{0\}\leftrightarrow I$ and $R/I\leftrightarrow R$. "Only those two" is exactly "$I$ maximal".
   - *Why needed:* It establishes the maximal-side of the dictionary; statement 4 needs it.

3. **Prime $\iff$ domain quotient.** Show $I$ prime $\iff R/I$ an integral domain.
   - *Hint:* Quotient multiplication is $(a+I)(b+I)=ab+I$. Unwind "$ab+I=0_{R/I}$" as "$ab\in I$" and "$a+I=0_{R/I}$" as "$a\in I$"; the domain condition and the prime condition then read identically.
   - *Why needed:* It establishes the prime-side of the dictionary; statement 4 needs it.

4. **Maximal $\implies$ prime.** Chain the equivalences.
   - *Hint:* $I$ maximal $\overset{(2)}{\Rightarrow}$ $R/I$ field $\Rightarrow$ $R/I$ domain (a unit is never a zero divisor) $\overset{(3)}{\Rightarrow}$ $I$ prime.
   - *Why needed:* It is the headline corollary; the converse fails because domain $\not\Rightarrow$ field (witness $\{0\}\subseteq\mathbb{Z}$).

---

# Lemma Decomposition

> [!note]- Lemma 1: An ideal containing a unit is the whole ring
> **Statement:** If $I \trianglelefteq R$ and $I$ contains a unit $u$, then $I = R$.
>
> **Hint:** [[Def - Ideal|Ideals]] absorb multiplication by arbitrary ring elements; multiply $u$ by $u^{-1}$, then by everything.
>
> **Why needed:** It is the mechanism behind the field criterion: in a field every nonzero element is a unit, so any nonzero ideal swallows the whole ring.
>
> > [!note]- Full proof
> > Let $u \in I$ be a unit, with inverse $u^{-1} \in R$. Since $I$ is an ideal, it absorbs multiplication by ring elements, so $u^{-1} \cdot u \in I$, i.e. $1_R \in I$. Then for any $r \in R$, again by absorption $r = r \cdot 1_R \in I$. Hence $I = R$.

> [!note]- Lemma 2: The field criterion
> **Statement:** A nonzero commutative ring $R$ is a field if and only if its only ideals are $\{0\}$ and $R$.
>
> **Hint:** Forward, use Lemma 1. Backward, generate a principal ideal from a nonzero element.
>
> **Why needed:** It is the prototype for statement 2: maximality is this criterion transported across the quotient by the ideal correspondence.
>
> > [!note]- Full proof
> > **($\Rightarrow$)** Let $R$ be a field and $I \trianglelefteq R$. If $I \neq \{0\}$, pick $x \in I$ with $x \neq 0_R$. Since $R$ is a field, $x$ is a unit, so by Lemma 1, $I = R$. Hence the only ideals are $\{0\}$ and $R$.
> >
> > **($\Leftarrow$)** Suppose the only ideals of $R$ are $\{0\}$ and $R$. Let $x \in R$ be nonzero. The principal ideal $(x) = \{rx : r \in R\}$ is an ideal of $R$, and it contains $x = 1_R\cdot x \neq 0_R$, so $(x) \neq \{0\}$. By hypothesis $(x) = R$, so $1_R \in (x)$, meaning $1_R = u x$ for some $u \in R$. Thus $x$ has a multiplicative inverse $u$. Since $x \neq 0_R$ was arbitrary, every nonzero element of $R$ is a unit, and (as $R$ is nonzero) $R$ is a field.

> [!note]- Lemma 3: Maximality of $I$ equals the field criterion for $R/I$ via the ideal correspondence
> **Statement:** $I \trianglelefteq R$ is maximal if and only if $R/I$ has exactly two ideals, $\{0_{R/I}\}$ and $R/I$.
>
> **Hint:** Apply the [[Thm - Ideal Correspondence|ideal correspondence]]; track which ideals of $R$ correspond to $\{0_{R/I}\}$ and to $R/I$.
>
> **Why needed:** It is the precise translation step that turns the field criterion on $R/I$ into a statement about $I$, yielding statement 2.
>
> > [!note]- Full proof
> > The [[Thm - Ideal Correspondence|ideal correspondence theorem]] gives an inclusion-preserving bijection
> > $$\{\text{ideals of } R/I\} \;\longleftrightarrow\; \{\text{ideals } J \text{ of } R \text{ with } I \subseteq J\},$$
> > under which an ideal $L$ of $R/I$ corresponds to its preimage $\pi^{-1}(L) \trianglelefteq R$. Under this bijection the zero ideal $\{0_{R/I}\}$ corresponds to $\pi^{-1}(\{0_{R/I}\}) = I$, and the whole ring $R/I$ corresponds to $\pi^{-1}(R/I) = R$. Therefore "$R/I$ has exactly the two ideals $\{0_{R/I}\}$ and $R/I$" is equivalent, term by term, to "the only ideals $J$ of $R$ with $I \subseteq J$ are $I$ and $R$". The latter is precisely the definition of $I$ being a maximal ideal ($I \neq R$, and no ideal strictly between). Hence $I$ is maximal if and only if $R/I$ has exactly two ideals.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be a nonzero commutative ring.
>
> ---
> **Statement 1 — the field criterion.** This is Lemma 2: $R$ is a field if and only if its only ideals are $\{0\}$ and $R$. (Forward: in a field, any nonzero ideal contains a unit, hence is all of $R$ by Lemma 1. Backward: for nonzero $x$, the principal ideal $(x)$ is nonzero, hence equals $R$, so $1_R \in (x)$ and $x$ is a unit.)
>
> ---
> **Statement 2 — maximal $\iff$ field quotient.** Let $I \trianglelefteq R$. By Statement 1 applied to the ring $R/I$, the quotient $R/I$ is a field if and only if its only ideals are $\{0_{R/I}\}$ and $R/I$. By Lemma 3 — the [[Thm - Ideal Correspondence|ideal correspondence]] — this holds if and only if the only ideals of $R$ containing $I$ are $I$ and $R$, which is exactly the statement that $I$ is maximal. Hence
> $$I \text{ maximal} \iff R/I \text{ is a field}.$$
>
> ---
> **Statement 3 — prime $\iff$ domain quotient.** Let $I \trianglelefteq R$. Recall that multiplication in $R/I$ is $(a+I)(b+I) = ab + I$, and that a coset $c + I$ equals the zero element $0_{R/I}$ if and only if $c \in I$.
>
> *($\Rightarrow$)* Suppose $I$ is prime. Take cosets $a + I,\, b + I \in R/I$ with $(a+I)(b+I) = 0_{R/I}$. Then $ab + I = 0_{R/I}$, so $ab \in I$. As $I$ is prime, $a \in I$ or $b \in I$, i.e. $a + I = 0_{R/I}$ or $b + I = 0_{R/I}$. So $R/I$ has no zero divisors; and $R/I$ is nonzero because $I \neq R$ (a prime ideal is proper). Hence $R/I$ is an integral domain.
>
> *($\Leftarrow$)* Suppose $R/I$ is an integral domain. First $I \neq R$, since $R/I$ is nonzero. Let $a, b \in R$ with $ab \in I$. Then $(a+I)(b+I) = ab + I = 0_{R/I}$. Since $R/I$ is a domain, $a + I = 0_{R/I}$ or $b + I = 0_{R/I}$, i.e. $a \in I$ or $b \in I$. Hence $I$ is prime. Therefore
> $$I \text{ prime} \iff R/I \text{ is an integral domain}.$$
>
> ---
> **Statement 4 — maximal $\implies$ prime.** Suppose $I$ is maximal. By Statement 2, $R/I$ is a field. Every field is an integral domain: if $a,b$ lie in a field and $ab = 0$ with $b \neq 0$, then $a = a(b\,b^{-1}) = (ab)b^{-1} = 0\cdot b^{-1} = 0$, so a field has no zero divisors. Hence $R/I$ is an integral domain. By Statement 3, $I$ is prime.
>
> So every maximal ideal is prime. (The converse fails: $\{0\}\trianglelefteq\mathbb{Z}$ is prime, since $\mathbb{Z}/\{0\}\cong\mathbb{Z}$ is a domain, but not maximal, since $\mathbb{Z}$ is not a field; equivalently $\{0\}\subsetneq(2)\subsetneq\mathbb{Z}$.) $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Points of affine space are maximal ideals.** For a field $k$ and a point $a = (a_1,\dots,a_n)\in k^n$, the evaluation map $\operatorname{ev}_a : k[X_1,\dots,X_n]\to k$, $f\mapsto f(a)$, is a surjective ring homomorphism onto the field $k$, with kernel $\mathfrak{m}_a = (X_1-a_1,\dots,X_n-a_n)$. By the first isomorphism theorem $k[X_1,\dots,X_n]/\mathfrak{m}_a\cong k$, a field, so statement 2 makes $\mathfrak{m}_a$ a maximal ideal. The nonobvious recognition: a *geometric point* corresponds to a *maximal ideal*, the seed of the algebra–geometry dictionary, and the certification of maximality is a quotient computation, not a lattice search.

**Prime numbers as prime ideals, and primality as a quotient property.** The ideal $(n)\trianglelefteq\mathbb{Z}$ is prime if and only if $\mathbb{Z}/n\mathbb{Z}$ is a domain. For $n=p$ prime, $\mathbb{Z}/p\mathbb{Z}$ is a domain (indeed a field); for $n$ composite, $\mathbb{Z}/n\mathbb{Z}$ has zero divisors. So the ring-theoretic notion of "prime ideal" recovers the number-theoretic notion of "prime number" exactly. The application is nonobvious because it reframes elementary number theory — "$p$ is prime" — as the structural statement "the quotient ring is a domain".

**Irreducible polynomials cut out maximal ideals in $F[X]$.** For a field $F$ and an irreducible $p \in F[X]$, the quotient $F[X]/(p)$ is a field (every nonzero coset is invertible, by the Euclidean algorithm). Statement 2 then says $(p)$ is a maximal ideal of $F[X]$. The application is nonobvious because it links a *factorisation* property of a polynomial to a *lattice* property of an ideal, and it is the algebraic engine of field extension theory: $F[X]/(p)$ is the field obtained by adjoining a root of $p$.

**Distinguishing prime from maximal in a two-variable polynomial ring.** The ideal $(X)\trianglelefteq\mathbb{Z}[X,Y]$ has quotient $\mathbb{Z}[X,Y]/(X)\cong\mathbb{Z}[Y]$, which is an integral domain but *not* a field. By statements 3 and 2 respectively, $(X)$ is prime but not maximal — a concrete witness that statement 4 does not reverse. The application is nonobvious because it uses the package as a *diagnostic*: the single quotient computation $\mathbb{Z}[X,Y]/(X)\cong\mathbb{Z}[Y]$ simultaneously certifies primality and refutes maximality.

---

# Bridges

- **[[Thm - Ideal Correspondence|Ideal Correspondence]]** — the structural backbone of statement 2. The correspondence is the inclusion-preserving bijection between ideals of $R/I$ and ideals of $R$ above $I$; statement 2 is obtained by feeding the field criterion (statement 1) through this bijection. Without the correspondence, "maximal $\iff$ field quotient" would have to be proved by a direct and clumsier lattice argument.

- **[[Def - Prime and Maximal Ideal|Prime and Maximal Ideal]]** — this theorem is the *raison d'être* of those two definitions. The definitions, stated abstractly, look arbitrary; the theorem reveals them as exactly the ideals whose quotients are domains and fields respectively.

- **[[Thm - Finite Integral Domains are Fields|Finite Integral Domains are Fields]]** — combine with statement 3 to get a partial converse to statement 4: if $R/I$ is a *finite* domain, it is a field, so a **prime ideal of finite index is maximal**. This is why, in $\mathbb{Z}$, every nonzero prime ideal is maximal.

- **[[Thm - Existence of the Field of Fractions|Existence of the Field of Fractions]]** — combine with statement 3: a prime quotient $R/P$ is a domain, hence embeds in its field of fractions, the *residue field at $P$*. This is how prime ideals acquire fields attached to them.

- **[[Thm - First Isomorphism Theorem for Rings|First Isomorphism Theorem for Rings]]** — the companion tool for *applying* statements 2 and 3. To certify $I$ as maximal or prime, exhibit a surjection $R\twoheadrightarrow T$ with kernel $I$ and $T$ a field or domain; the first isomorphism theorem gives $R/I\cong T$, and the package finishes the job.

- **Krull dimension and the spectrum of a ring** — the downstream generalisation. The set of all prime ideals, $\operatorname{Spec}(R)$, organised by inclusion, is the foundational object of scheme theory; maximal ideals are its "closed points". Statement 4 — maximal ideals are prime — is what places the closed points inside the spectrum.

---

# Unlocked by This

> [!tip] The Spectrum of a Ring and Schemes *(from Algebraic Geometry)*
> Because prime ideals are exactly the ideals with domain quotients, and maximal ideals exactly those with field quotients, the set of prime ideals $\operatorname{Spec}(R)$ becomes a geometric space whose points are primes and whose closed points are maximal ideals. This is the starting point of scheme theory, where every commutative ring becomes a geometric object.

> [!tip] Residue Fields and Local Rings *(from Commutative Algebra)*
> A prime ideal $P$ has a domain quotient $R/P$, whose field of fractions is the *residue field* $\kappa(P)$. Localising $R$ at $P$ produces a local ring whose unique maximal ideal has residue field $\kappa(P)$ — the basic apparatus for studying a ring "one prime at a time".

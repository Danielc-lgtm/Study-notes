---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Integral Domain"
  - "Def - Unit and Field"
  - "Def - Field of Fractions"
  - "Def - Ring Homomorphism"
  - "Thm - First Isomorphism Theorem for Rings"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is an [[Def - Integral Domain|integral domain]] — a nonzero commutative [[Def - Ring|ring]] with $1_R \neq 0_R$ and no zero divisors. A [[Def - Field of Fractions|field of fractions]] of $R$ is a [[Def - Unit and Field|field]] $F$ such that (i) $R$ is (isomorphic to) a subring of $F$, $R \leq F$, and (ii) every element of $F$ has the form $a \cdot b^{-1}$ with $a, b \in R$ and $b \neq 0_R$, where $b^{-1}$ is the inverse of $b$ taken in $F$. We write $S = \{(a,b) \in R \times R : b \neq 0_R\}$ for the set of formal pairs, and use the fraction notation $\tfrac{a}{b}$ for the class $[(a,b)]$ under the equivalence relation $\sim$ defined below. The symbol $\leq$ means "is a subring of", $\cong$ denotes ring isomorphism, and $\hookrightarrow$ an injective homomorphism. The full symbol registry is on the parent page [[Rings II — §2.3–2.4]].

---

# Statement

> **Existence of the field of fractions.** Every [[Def - Integral Domain|integral domain]] $R$ has a [[Def - Field of Fractions|field of fractions]]. Concretely, on the set $S = \{(a,b) \in R \times R : b \neq 0_R\}$ the relation
> $$(a,b) \sim (c,d) \iff ad = bc$$
> is an equivalence relation; the quotient set $F = S/\!\sim$, with elements written $\tfrac{a}{b} = [(a,b)]$ and operations
> $$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}, \qquad \frac{a}{b}\cdot\frac{c}{d} = \frac{ac}{bd},$$
> zero $\tfrac{0_R}{1_R}$ and one $\tfrac{1_R}{1_R}$, is a field; and the map $\varphi : R \to F$, $r \mapsto \tfrac{r}{1_R}$, is an injective ring homomorphism. Hence $R \cong \varphi(R) \leq F$ and every integral domain embeds in a field. In particular, $\mathbb{Q}$ is the field of fractions of $\mathbb{Z}$.

---

# Motivation

We already know one direction of an equivalence: *a subring of a field is an integral domain*. If $R \leq F$ with $F$ a field, then $R$ inherits the absence of zero divisors, because an equation $ab = 0$ inside $R$ is also an equation inside $F$, and a field has no zero divisors (an invertible element cannot kill a nonzero element). So "is a subring of a field" implies "is an integral domain". This theorem proves the *converse*: every integral domain *is* a subring of a field. The two statements together say the class of integral domains is exactly the class of subrings of fields — a clean structural characterisation.

The question is therefore: given an abstract domain $R$ with no division, how do you *manufacture* a field around it? The model to imitate is the most familiar construction in all of mathematics — building $\mathbb{Q}$ from $\mathbb{Z}$. You cannot divide inside $\mathbb{Z}$, so you invent new symbols, the fractions $\tfrac{a}{b}$, declare two of them equal when they cross-multiply to the same thing, and check that arithmetic on these symbols obeys the field axioms. The theorem says this recipe is not special to $\mathbb{Z}$: it works verbatim for *any* integral domain. Run it on $\mathbb{Z}$ and you get $\mathbb{Q}$; run it on a polynomial ring $F[X]$ and you get the field of rational functions $F(X)$; run it on the Gaussian integers $\mathbb{Z}[i]$ and you get $\mathbb{Q}(i)$.

There are two reasons this matters beyond tidiness. First, it is a tool for *importing field techniques into the study of domains*: many statements about a domain $R$ are easiest to prove by passing to its fraction field, working there where everything is invertible, and pulling the conclusion back. Second, it is a *source of new fields*: number fields like $\mathbb{Q}(\sqrt{2})$ and function fields are most naturally born as fields of fractions. The construction is the precise sense in which "division" can always be adjoined to a domain — and the integral-domain hypothesis is not decoration: it is exactly what makes the construction work, and the proof will pin down the one line where it is used.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$R$ is an integral domain". The skill is recognising domains in disguise, since the theorem then hands you a field for free.

The first disguised source is **a polynomial ring over a domain**. The property $B$ is "$R = D[X_1, \dots, X_n]$ with $D$ a domain". The bridge is the lemma that $D$ a domain implies $D[X]$ a domain (the top coefficient of a product of nonzero polynomials is the product of the top coefficients, hence nonzero), iterated over the variables. So $D[X_1,\dots,X_n]$ is a domain, and the theorem produces its field of fractions — the field of **rational functions** $D(X_1,\dots,X_n)$. The non-obvious part is that polynomial rings, which have no division at all, are nonetheless domains and therefore admit fraction fields. *Example problem:* construct the rational function field $\mathbb{C}(X)$ as the field of fractions of $\mathbb{C}[X]$.

The second disguised source is **a subring of a known domain or field**. The property $B$ is "$R \leq T$ with $T$ a domain". Any subring of a domain is a domain, since a zero divisor in $R$ would be a zero divisor in $T$. The theorem then gives $R$ a fraction field, which moreover embeds in any field containing $T$. The non-obviousness: you need not check the domain axiom for $R$ from scratch — it is inherited downward. *Example problem:* $\mathbb{Z}[\sqrt{2}] \leq \mathbb{R}$ is a domain, with field of fractions $\mathbb{Q}(\sqrt{2})$.

The third disguised source is **a quotient $R/P$ by a [[Def - Prime and Maximal Ideal|prime ideal]]**. The property $B$ is "$P$ is a prime ideal of $R$". By [[Thm - Maximal and Prime Ideals via Quotients|the prime-ideal characterisation]], $R/P$ is then an integral domain, so the theorem furnishes *its* field of fractions. The non-obvious step is that primality of an ideal is exactly the input the theorem needs, routed through the quotient. *Example problem:* for an irreducible polynomial the quotient $\mathbb{Z}[X,Y]/(X)$ is a domain, with a fraction field.

**Targets (Output Amplification)**

The bare conclusion is "$R$ embeds in a field $F$, every element of $F$ a quotient of elements of $R$".

Combine the conclusion with **the universal property of $F$**. The fraction field comes with more than its existence: *any* injective homomorphism from $R$ into a field $K$ extends uniquely to a homomorphism $F \to K$. The further result $E$ is that $F$ is the *smallest* field containing $R$ — initial among all fields receiving $R$ — so the fraction field is canonical, not just one field among many. This is non-obvious because the construction looks like an arbitrary choice of formal symbols, yet it is forced by a universal property.

Combine the conclusion with **a degree or transcendence count**. If $R$ is finitely generated over a base field $k$, the fraction field $F$ has a well-defined *transcendence degree* over $k$, which is the **dimension** of the associated geometric object. The further result $E$: the fraction field of the coordinate ring of an algebraic variety is its *function field*, and its transcendence degree is the dimension of the variety. The theorem is what makes the function field exist in the first place.

Combine the conclusion with **localisation at a prime**. The same equivalence-class construction, but inverting only the elements *outside* a prime ideal $P$ rather than all nonzero elements, produces the local ring $R_P$. The further result $E$ is the entire technique of localisation in commutative algebra; the field of fractions is the special case $P = \{0\}$, where everything nonzero is inverted. Recognising the fraction field as "localise at the zero ideal" is the non-obvious unification.

---

# Why Is It True

The theorem feels inevitable once you see what problem the equivalence relation is solving. You want division, so you want symbols $\tfrac{a}{b}$ that behave like quotients. The obstruction is that the *same* quotient has many names: $\tfrac{1}{2}$ and $\tfrac{2}{4}$ ought to be the same number. So the raw set of pairs $(a,b)$ is too big — it distinguishes things that should be equal. The fix is the only fix available: glue together pairs that *should* name the same fraction. Two fractions $\tfrac{a}{b}$ and $\tfrac{c}{d}$ name the same value precisely when $ad = bc$ — this is what "cross-multiplying" means, and crucially it is an equation *inside $R$*, using no division, so it makes sense before the field exists. The set of equivalence classes is then exactly the set of *genuine* fractions, each counted once.

Why should the arithmetic work? The formulas $\tfrac{a}{b} + \tfrac{c}{d} = \tfrac{ad+bc}{bd}$ and $\tfrac{a}{b}\cdot\tfrac{c}{d} = \tfrac{ac}{bd}$ are not invented — they are *forced*. If $\tfrac{a}{b}$ is to behave like $a$ divided by $b$, then a common denominator and the distributive law leave no other possible answer for the sum, and likewise for the product. The only real worry is whether these formulas *respect the gluing*: if you replace $\tfrac{a}{b}$ by an equal fraction $\tfrac{a'}{b'}$, you must get an equal answer. This is the well-definedness check, and it goes through by direct computation.

Now, the field axioms. Every nonzero $\tfrac{a}{b}$ has the obvious inverse $\tfrac{b}{a}$ — and "$\tfrac{a}{b} \neq 0$" unwinds, via the equivalence relation, to "$a \neq 0$", which is exactly the condition under which $\tfrac{b}{a}$ is a legal symbol. So inverses are visibly present; that is the whole point of the construction. The element $r$ of $R$ sits inside $F$ as $\tfrac{r}{1}$, and $\tfrac{a}{b} = \tfrac{a}{1}\cdot(\tfrac{b}{1})^{-1}$ shows every element of $F$ is a quotient of things from $R$, so condition (ii) of "field of fractions" holds by design. The embedding $r \mapsto \tfrac{r}{1}$ is injective because $\tfrac{r}{1} = \tfrac{0}{1}$ means $r \cdot 1 = 1 \cdot 0$, i.e. $r = 0$.

The single place the construction can fail — and the reason the integral-domain hypothesis is non-negotiable — is **transitivity of $\sim$**. Suppose $(a,b)\sim(c,d)$ and $(c,d)\sim(e,f)$, so $ad = bc$ and $cf = de$. You want $(a,b)\sim(e,f)$, i.e. $af = be$. Multiply the first equation by $f$ and the second by $b$: $adf = bcf$ and $bcf = bde$, so $adf = bde$, which rearranges to $d(af - be) = 0$. You would *love* to cancel $d$ and conclude $af = be$ — but cancelling $d$ requires that $d$, which is nonzero (it is a denominator), is not a *zero divisor*. That is precisely the integral-domain hypothesis. Drop it, and the relation is not transitive, the equivalence classes do not exist, and the construction collapses at the first step. The intuition: a domain is exactly a ring in which "$\tfrac{a}{b}$" can be unambiguously simplified, because nonzero denominators can always be cancelled.

---

# What Makes This Hard

The construction has many small parts (an equivalence relation, two binary operations, well-definedness of each, all the field axioms, an embedding) and the honest difficulty is bookkeeping stamina — the lecture notes themselves skip the routine verifications. The single conceptually load-bearing step, and the one to recall under spaced practice, is **transitivity of $\sim$**: it is the *only* place the integral-domain hypothesis is used, surfacing as the need to cancel a nonzero denominator $d$ from $d(af-be)=0$. The most common error is to treat well-definedness as automatic — forgetting that the sum and product formulas are defined on *representatives* and must be checked to descend to equivalence classes — and, relatedly, to overlook that every denominator appearing ($b$, $d$, $bd$, $bf$) is nonzero exactly because $R$ is a domain.

---

# Rederivation Scaffold

**High-level strategy:**
Imitate the construction of $\mathbb{Q}$ from $\mathbb{Z}$ verbatim. Form pairs $(a,b)$ with $b \neq 0$, glue them by cross-multiplication, define addition and multiplication by the common-denominator formulas, check the gluing is an equivalence relation and the operations descend, verify the field axioms (the inverse of $\tfrac{a}{b}$ is $\tfrac{b}{a}$), and embed $R$ via $r \mapsto \tfrac{r}{1}$.

**Subgoal decomposition:**

1. **$\sim$ is an equivalence relation.** Show $(a,b)\sim(c,d) \iff ad = bc$ is reflexive, symmetric, transitive on $S$.
   - *Hint:* Reflexivity and symmetry are immediate. For transitivity, from $ad=bc$, $cf=de$ derive $d(af-be)=0$ and cancel the nonzero $d$ — this is the *only* use of "integral domain".
   - *Why needed:* Without it the quotient set $F = S/\!\sim$ does not exist.

2. **The operations are well-defined.** Show $+$ and $\cdot$ on $\tfrac{a}{b}$ do not depend on the chosen representatives.
   - *Hint:* Replace $(a,b)$ by an equivalent $(a',b')$ and verify the formula's output is equivalent to the original; all denominators are nonzero since $R$ is a domain.
   - *Why needed:* Operations on classes must be computed on representatives; descent is not automatic.

3. **$(F,+,\cdot)$ is a commutative ring.** Verify the ring axioms with zero $\tfrac{0}{1}$ and one $\tfrac{1}{1}$.
   - *Hint:* Each axiom reduces, after clearing denominators, to a ring axiom of $R$. Routine.
   - *Why needed:* A field is first of all a ring.

4. **Every nonzero element is invertible.** Show $\tfrac{a}{b} \neq 0_F \implies \tfrac{a}{b}$ has inverse $\tfrac{b}{a}$.
   - *Hint:* $\tfrac{a}{b} = \tfrac{0}{1}$ means $a\cdot 1 = b\cdot 0$, i.e. $a = 0$. So $\tfrac{a}{b}\neq 0_F$ if and only if $a\neq 0$, exactly when $\tfrac{b}{a}$ is a legal symbol; then $\tfrac{a}{b}\cdot\tfrac{b}{a}=\tfrac{ab}{ab}=\tfrac{1}{1}$.
   - *Why needed:* This is what upgrades the ring $F$ to a field.

5. **Embed $R$ in $F$.** Show $\varphi : R \to F$, $r \mapsto \tfrac{r}{1}$, is an injective ring homomorphism, and every element of $F$ is a quotient of elements of $R$.
   - *Hint:* Check $\varphi$ respects $+,\cdot,0,1$; its kernel is $\{r : \tfrac{r}{1}=\tfrac{0}{1}\} = \{0\}$, so by the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]] $R\cong\varphi(R)\leq F$. Finally $\tfrac{a}{b}=\varphi(a)\varphi(b)^{-1}$.
   - *Why needed:* This verifies conditions (i) and (ii) of "field of fractions".

---

# Lemma Decomposition

> [!note]- Lemma 1: $\sim$ is an equivalence relation (the integral-domain step)
> **Statement:** On $S = \{(a,b)\in R\times R : b\neq 0_R\}$, the relation $(a,b)\sim(c,d)\iff ad=bc$ is reflexive, symmetric and transitive.
>
> **Hint:** Reflexivity and symmetry use only commutativity. Transitivity is where you cancel a nonzero denominator — the sole appearance of the no-zero-divisors hypothesis.
>
> **Why needed:** It is the foundation: the quotient set $F = S/\!\sim$ exists only if $\sim$ is genuinely an equivalence relation.
>
> > [!note]- Full proof
> > **Reflexive:** $(a,b)\sim(a,b)$ since $ab = ba$ by commutativity of $R$.
> >
> > **Symmetric:** if $(a,b)\sim(c,d)$ then $ad = bc$; commutativity gives $cb = da$, i.e. $(c,d)\sim(a,b)$.
> >
> > **Transitive:** suppose $(a,b)\sim(c,d)$ and $(c,d)\sim(e,f)$, so
> > $$ad = bc \qquad\text{and}\qquad cf = de.$$
> > Multiply the first equation by $f$ and the second by $b$:
> > $$adf = bcf, \qquad bcf = bde.$$
> > Hence $adf = bde$, and rearranging (using commutativity to collect the factor $d$),
> > $$d(af - be) = 0_R.$$
> > Now $d$ is a denominator, so $d \neq 0_R$. **Because $R$ is an integral domain**, $d \cdot (af - be) = 0_R$ with $d \neq 0_R$ forces $af - be = 0_R$, i.e. $af = be$. Therefore $(a,b)\sim(e,f)$. This is the one and only place the integral-domain hypothesis is used; without it $\sim$ need not be transitive.

> [!note]- Lemma 2: Addition and multiplication descend to equivalence classes
> **Statement:** The formulas $\tfrac{a}{b}+\tfrac{c}{d}=\tfrac{ad+bc}{bd}$ and $\tfrac{a}{b}\cdot\tfrac{c}{d}=\tfrac{ac}{bd}$ define operations on $F = S/\!\sim$ that are independent of the chosen representatives. (The outputs are legal: $bd\neq 0_R$ since $b,d\neq 0_R$ and $R$ is a domain.)
>
> **Hint:** Fix the second fraction and replace $(a,b)$ by an equivalent $(a',b')$; show the results are $\sim$-equivalent. By symmetry of the argument, varying the second fraction too gives full well-definedness.
>
> **Why needed:** $+$ and $\cdot$ are written using representatives; the theorem's operations on $F$ exist only if the answer does not depend on which representative is chosen.
>
> > [!note]- Full proof
> > First, the outputs lie in $S$: if $b\neq 0_R$ and $d\neq 0_R$ then $bd\neq 0_R$, because $R$ is an integral domain (a product of nonzero elements is nonzero).
> >
> > **Multiplication.** Suppose $(a,b)\sim(a',b')$, so $ab' = a'b$. We compare $\tfrac{ac}{bd}$ and $\tfrac{a'c}{b'd}$; we need $(ac)(b'd) = (bd)(a'c)$. Indeed
> > $$(ac)(b'd) = (ab')(cd) = (a'b)(cd) = (bd)(a'c),$$
> > using commutativity and $ab' = a'b$. So replacing the first fraction by an equivalent one leaves the product unchanged; the identical computation handles the second fraction. Hence $\cdot$ is well-defined.
> >
> > **Addition.** Suppose again $(a,b)\sim(a',b')$, so $ab' = a'b$. We compare $\tfrac{ad+bc}{bd}$ and $\tfrac{a'd+b'c}{b'd}$; we need $(ad+bc)(b'd) = (bd)(a'd+b'c)$. Expanding the left side,
> > $$(ad+bc)(b'd) = ab'd^2 + bb'cd,$$
> > and the right side,
> > $$(bd)(a'd+b'c) = a'bd^2 + bb'cd.$$
> > These are equal precisely when $ab'd^2 = a'bd^2$, which follows by multiplying $ab' = a'b$ by $d^2$. So replacing the first fraction by an equivalent one leaves the sum unchanged; the same computation handles the second fraction. Hence $+$ is well-defined.

> [!note]- Lemma 3: $F$ is a field, with inverse $\tfrac{a}{b}\mapsto\tfrac{b}{a}$
> **Statement:** With the operations of Lemma 2, $(F, +, \cdot, \tfrac{0_R}{1_R}, \tfrac{1_R}{1_R})$ is a commutative ring, and every element $\tfrac{a}{b}\neq 0_F$ has multiplicative inverse $\tfrac{b}{a}$. Hence $F$ is a field.
>
> **Hint:** The ring axioms reduce to ring axioms of $R$ after clearing denominators. For the field property, note $\tfrac{a}{b}=0_F\iff a=0_R$.
>
> **Why needed:** This is the conclusion that $F$ is a *field*, not merely a set with operations.
>
> > [!note]- Full proof
> > That $(F,+,\cdot)$ is a commutative ring is a routine verification: associativity and commutativity of $+$ and $\cdot$, the distributive law, the additive identity $\tfrac{0_R}{1_R}$, additive inverses $-\tfrac{a}{b}=\tfrac{-a}{b}$, and the multiplicative identity $\tfrac{1_R}{1_R}$ each reduce, after clearing denominators, to the corresponding axiom of $R$. (For instance, $\tfrac{0_R}{1_R}$ is the zero: $\tfrac{a}{b}+\tfrac{0}{1}=\tfrac{a\cdot 1+b\cdot 0}{b\cdot 1}=\tfrac{a}{b}$.) These are the verifications the lecture notes describe as "straightforward" and omit.
> >
> > **Field property.** First identify the zero: $\tfrac{a}{b}=\tfrac{0_R}{1_R}$ in $F$ means $(a,b)\sim(0_R,1_R)$, i.e. $a\cdot 1_R = b\cdot 0_R$, i.e. $a = 0_R$. So $\tfrac{a}{b}\neq 0_F$ if and only if $a\neq 0_R$. Now take $\tfrac{a}{b}\neq 0_F$, so $a\neq 0_R$; then $(b,a)\in S$ is a legal pair, and $\tfrac{b}{a}\in F$ is defined. We compute
> > $$\frac{a}{b}\cdot\frac{b}{a} = \frac{ab}{ba} = \frac{ab}{ab} = \frac{1_R}{1_R},$$
> > the last step because $(ab)\cdot 1_R = (ab)\cdot 1_R$ gives $(ab,ab)\sim(1_R,1_R)$. So $\tfrac{b}{a}$ is the inverse of $\tfrac{a}{b}$. Every nonzero element of $F$ is therefore a unit, and since $\tfrac{1_R}{1_R}\neq\tfrac{0_R}{1_R}$ (as $1_R\neq 0_R$ in the domain $R$), $F$ is a field.

> [!note]- Lemma 4: $r\mapsto\tfrac{r}{1_R}$ is an injective ring homomorphism with quotient image
> **Statement:** The map $\varphi:R\to F$, $r\mapsto\tfrac{r}{1_R}$, is a ring homomorphism with trivial kernel, hence injective; and every element of $F$ equals $\varphi(a)\varphi(b)^{-1}$ for some $a,b\in R$, $b\neq 0_R$.
>
> **Hint:** Check $\varphi$ respects $+,\cdot,0,1$; compute $\ker\varphi$; then write $\tfrac{a}{b}$ as a product.
>
> **Why needed:** This delivers conditions (i) and (ii) of the definition of a field of fractions — it places a copy of $R$ inside $F$ and shows $F$ is built from quotients of that copy.
>
> > [!note]- Full proof
> > **Homomorphism.** $\varphi(r+s)=\tfrac{r+s}{1}=\tfrac{r\cdot 1+1\cdot s}{1\cdot 1}=\tfrac{r}{1}+\tfrac{s}{1}=\varphi(r)+\varphi(s)$; $\varphi(rs)=\tfrac{rs}{1}=\tfrac{rs}{1\cdot 1}=\tfrac{r}{1}\cdot\tfrac{s}{1}=\varphi(r)\varphi(s)$; $\varphi(0_R)=\tfrac{0_R}{1_R}=0_F$; $\varphi(1_R)=\tfrac{1_R}{1_R}=1_F$. So $\varphi$ is a ring homomorphism.
> >
> > **Injectivity.** $\ker\varphi = \{r\in R : \tfrac{r}{1}=\tfrac{0}{1}\}$. By the identification of the zero in Lemma 3, $\tfrac{r}{1}=\tfrac{0}{1}$ forces $r=0_R$. So $\ker\varphi=\{0_R\}$, and a ring homomorphism with trivial kernel is injective. By the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]], $R\cong\operatorname{im}\varphi=\varphi(R)\leq F$.
> >
> > **Quotient image.** For any $\tfrac{a}{b}\in F$ (so $b\neq 0_R$), $\varphi(b)=\tfrac{b}{1}\neq 0_F$, so it is invertible in $F$ with inverse $\tfrac{1}{b}$ (by Lemma 3, since $b\neq 0_R$). Then
> > $$\varphi(a)\,\varphi(b)^{-1} = \frac{a}{1}\cdot\frac{1}{b} = \frac{a\cdot 1}{1\cdot b} = \frac{a}{b}.$$
> > So every element of $F$ is $\varphi(a)\varphi(b)^{-1}$, i.e. (identifying $R$ with $\varphi(R)$) of the form $a\cdot b^{-1}$ with $a,b\in R$, $b\neq 0_R$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be an integral domain. Set $S = \{(a,b)\in R\times R : b\neq 0_R\}$, thought of as formal fractions $\tfrac{a}{b}$.
>
> **Step 1 — the equivalence relation.** Define $(a,b)\sim(c,d)\iff ad=bc$. By Lemma 1, $\sim$ is reflexive, symmetric, and transitive — transitivity being the unique point at which the integral-domain hypothesis enters, via cancellation of a nonzero denominator $d$ from $d(af-be)=0_R$. Hence $\sim$ is an equivalence relation and the quotient set
> $$F = S/\!\sim$$
> is defined. Write $\tfrac{a}{b}=[(a,b)]$ for equivalence classes.
>
> **Step 2 — the operations.** Define
> $$\frac{a}{b}+\frac{c}{d}=\frac{ad+bc}{bd}, \qquad \frac{a}{b}\cdot\frac{c}{d}=\frac{ac}{bd}.$$
> The outputs are legal pairs: $b,d\neq 0_R$ and $R$ a domain give $bd\neq 0_R$. By Lemma 2, both operations are independent of the choice of representatives, so they are well-defined binary operations on $F$.
>
> **Step 3 — $F$ is a field.** By Lemma 3, $(F,+,\cdot,\tfrac{0_R}{1_R},\tfrac{1_R}{1_R})$ is a commutative ring (each axiom reducing to a ring axiom of $R$ after clearing denominators), and every nonzero element $\tfrac{a}{b}$ — equivalently every $\tfrac{a}{b}$ with $a\neq 0_R$ — has inverse $\tfrac{b}{a}$, since $\tfrac{a}{b}\cdot\tfrac{b}{a}=\tfrac{ab}{ab}=\tfrac{1_R}{1_R}$. As $1_F\neq 0_F$, $F$ is a field.
>
> **Step 4 — the embedding.** Define $\varphi:R\to F$ by $\varphi(r)=\tfrac{r}{1_R}$. By Lemma 4, $\varphi$ is a ring homomorphism with $\ker\varphi=\{0_R\}$, hence injective; by the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]], $R\cong\varphi(R)\leq F$. So condition (i) of "field of fractions" holds: $R$ is (a copy of) a subring of the field $F$.
>
> **Step 5 — every element is a quotient.** Again by Lemma 4, for any $\tfrac{a}{b}\in F$,
> $$\frac{a}{b} = \frac{a}{1_R}\cdot\frac{1_R}{b} = \varphi(a)\,\varphi(b)^{-1},$$
> so, identifying $R$ with $\varphi(R)$, every element of $F$ has the form $a\cdot b^{-1}$ with $a,b\in R$ and $b\neq 0_R$. This is condition (ii).
>
> **Conclusion.** $F$ is a field satisfying (i) and (ii), hence a field of fractions of $R$. Every integral domain therefore embeds in a field. Applying the construction to $R=\mathbb{Z}$ recovers $F=\mathbb{Q}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Rational function fields and the dimension of a variety.** Apply the theorem to $R = k[X_1,\dots,X_n]$, a domain because polynomial rings over a domain are domains. Its field of fractions is the field $k(X_1,\dots,X_n)$ of rational functions, and the transcendence degree of this field over $k$ is $n$ — the dimension of affine $n$-space. The application is nonobvious because "field of fractions" sounds like a number-theoretic gadget, yet here it produces the *function field* of algebraic geometry, the object whose transcendence degree measures geometric dimension.

**Quotient fields of coordinate rings.** For an irreducible affine variety $V$, its coordinate ring $k[V]$ is an integral domain (irreducibility is exactly the statement that the defining ideal is prime, so the quotient is a domain by [[Thm - Maximal and Prime Ideals via Quotients|the prime-ideal criterion]]). The theorem produces the *function field* $k(V)$, whose elements are rational functions on $V$. The nonobvious recognition is the chain "irreducible variety $\Rightarrow$ prime ideal $\Rightarrow$ domain quotient $\Rightarrow$ apply field-of-fractions".

**Formal Laurent series from formal power series.** The ring $k[[X]]$ of formal power series over a field is an integral domain. Its field of fractions is the field $k((X))$ of formal Laurent series — series with finitely many negative-power terms. This is out-of-distribution because $k[[X]]$ is an infinite-dimensional, completed object, yet the purely algebraic equivalence-class construction still applies: the disguised source is simply that $k[[X]]$ has no zero divisors (the lowest-degree term of a product is the product of lowest-degree terms).

**The field $\mathbb{Q}$ inside any characteristic-zero field.** Any field $K$ of characteristic $0$ contains a copy of $\mathbb{Z}$ (the image of the unique homomorphism $\mathbb{Z}\to K$, injective since the characteristic is $0$). The universal property accompanying the theorem then extends this to a unique embedding $\mathbb{Q}\hookrightarrow K$ — every characteristic-zero field contains $\mathbb{Q}$ as its prime subfield. The application is nonobvious because it uses the field of fractions *backwards*: not to build a new field, but to certify that an existing field must contain $\mathbb{Q}$.

---

# Bridges

- **[[Def - Field of Fractions|Field of Fractions]]** — this theorem is the existence half of that definition: the definition says *what* a field of fractions is, and the theorem proves one always exists for a domain, by explicit construction. Uniqueness (up to canonical isomorphism) is the companion statement, secured by the universal property.

- **[[Thm - Finite Integral Domains are Fields|Finite Integral Domains are Fields]]** — a complementary "domain becomes field" result. There, finiteness alone upgrades a domain to a field internally, with the *same* underlying set; here, the domain is enlarged by adjoining formal inverses. Both witness that domains are "nearly" fields, differing only in invertibility.

- **[[Thm - First Isomorphism Theorem for Rings|First Isomorphism Theorem for Rings]]** — used inside the proof: the embedding $\varphi:R\to F$ has trivial kernel, and the first isomorphism theorem turns "trivial kernel" into the clean statement $R\cong\varphi(R)\leq F$.

- **Localisation of a ring** — the direct generalisation. Instead of inverting *all* nonzero elements, invert only a chosen multiplicatively closed set $T$; the same equivalence-class construction yields the localisation $T^{-1}R$. The field of fractions is the case $T = R\setminus\{0\}$; localising at the complement of a prime ideal gives a local ring. The construction here is the prototype of all of localisation.

- **The construction of $\mathbb{Q}$ from $\mathbb{Z}$** — the historical and motivating special case, reproduced verbatim. The theorem's content is precisely that this construction was never special to the integers.

---

# Unlocked by This

> [!tip] Function Fields and Birational Geometry *(from Algebraic Geometry)*
> The field of fractions of the coordinate ring of an irreducible variety is its *function field*. Two varieties with isomorphic function fields are birationally equivalent, so the field of fractions is the algebraic carrier of birational geometry, and its transcendence degree is the dimension of the variety.

> [!tip] Localisation and Local Rings *(from Commutative Algebra)*
> Generalising "invert everything nonzero" to "invert everything outside a prime ideal $P$" yields the local ring $R_P$, whose study is the foundation of local commutative algebra and scheme theory. The field of fractions is the localisation at the zero ideal — the first and simplest instance.

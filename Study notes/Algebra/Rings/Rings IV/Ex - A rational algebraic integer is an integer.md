---
type: exercise
subject: ring-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Algebraic Integer and Minimal Polynomial"
  - "Thm - Rational Algebraic Integers are Integers"
  - "Thm - Gauss's Lemma"
  - "Def - Polynomial Ring"
  - "Def - Greatest Common Divisor and Least Common Multiple"
tags: [algebra, ring-theory]
---

# Problem Statement

Prove the following: if $\alpha \in \mathbb{Q}$ is a root of some monic polynomial $f \in \mathbb{Z}[X]$, then $\alpha \in \mathbb{Z}$.

In the language of [[Rings IV — §2.7–2.8]]: *a rational number that is an algebraic integer is an honest integer*. Equivalently, $\mathbb{Z}[X] \cap \mathbb{Q} = \mathbb{Z}$ as far as roots of monic polynomials are concerned — there are no "fractional algebraic integers".

Prove it via the **rational root theorem**: write $\alpha = p/q$ in lowest terms, substitute into $f(\alpha) = 0$, clear denominators, and read off a divisibility forcing $q \mid 1$.

**Recall:**

The setting is the field $\mathbb{Q}$ of rationals sitting inside $\mathbb{C}$, the [[Def - Polynomial Ring|polynomial ring]] $\mathbb{Z}[X]$, and the notion of an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]].

A complex number $\alpha$ is an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]] when it is a root of a **monic** polynomial $f \in \mathbb{Z}[X]$, i.e. $f = X^n + a_{n-1}X^{n-1} + \cdots + a_1 X + a_0$ with $a_0, \dots, a_{n-1} \in \mathbb{Z}$ and leading coefficient $1$. The statement to prove is the content of:

![[Thm - Rational Algebraic Integers are Integers#Statement]]

Two pieces of elementary arithmetic are used. First, **lowest terms**: every non-zero rational $\alpha$ can be written $\alpha = p/q$ with $p \in \mathbb{Z}$, $q \in \mathbb{Z}_{>0}$, and $\gcd(p, q) = 1$ — the [[Def - Greatest Common Divisor and Least Common Multiple|gcd]] of numerator and denominator equal to $1$. Second, **coprime cancellation (Euclid's lemma)**: if $\gcd(p, q) = 1$ and $q \mid p \cdot m$, then $q \mid m$; in particular if $\gcd(p, q) = 1$ then $\gcd(p^k, q) = 1$ for every $k \geq 1$, so $q$ shares no prime factor with any power of $p$.

The textbook proves this lemma differently — via [[Thm - Gauss's Lemma|Gauss's lemma]]: the minimal polynomial $f_\alpha$ of $\alpha$ is monic irreducible in $\mathbb{Z}[X]$; over $\mathbb{Q}[X]$ the linear factor $X - \alpha$ divides $f_\alpha$; Gauss's lemma says $f_\alpha$ remains irreducible over $\mathbb{Q}$, forcing $f_\alpha = X - \alpha \in \mathbb{Z}[X]$, hence $\alpha \in \mathbb{Z}$. We give the rational-root-theorem proof as the main argument and record the Gauss's-lemma proof as an alternative.

---

# Convergent Strategy

**Problem class.** This is a *rigidity / integrality* statement: an a priori "loose" object (a rational number) is forced to be "tight" (an integer) by an algebraic constraint (satisfying a monic integer polynomial). The [[Rings IV — §2.7–2.8]] strategy notes that integrality theorems of this kind are proved by *writing the rational in lowest terms and extracting a divisibility from the defining equation* — the coprimality of numerator and denominator is the lever.

**Assumption pattern.** Two hypotheses, both indispensable. (i) $\alpha \in \mathbb{Q}$: this is what lets us write $\alpha = p/q$ with integer $p, q$ at all. (ii) $f$ is **monic**: the leading coefficient is $1$. Monicity is the load-bearing assumption — drop it and the theorem is false ($2X - 1$ is a non-monic integer polynomial with root $\tfrac12 \notin \mathbb{Z}$). The general rational root theorem says a rational root $p/q$ of $\sum a_i X^i$ has $q \mid a_n$; when $a_n = 1$ this collapses to $q \mid 1$, which is the entire point.

**Theorem routing.** Substitute $\alpha = p/q$ into $f(\alpha) = 0$ and multiply through by $q^n$ to clear all denominators. The resulting integer equation, rearranged, exhibits $q$ dividing a single term $p^n$. Coprimality of $p$ and $q$ (Euclid's lemma, [[Def - Greatest Common Divisor and Least Common Multiple|gcd]] $= 1$) then upgrades "$q \mid p^n$" to "$q \mid 1$", so $q = 1$ and $\alpha = p \in \mathbb{Z}$. The independent route, recorded in the alternative derivation, goes through [[Thm - Gauss's Lemma|Gauss's lemma]] and the minimal polynomial.

**Key decision point.** The non-obvious move is writing $\alpha$ in **lowest terms** *before* substituting — and then, after clearing denominators, *isolating the one term not visibly divisible by $q$*. Every term of the cleared equation except $p^n$ carries an explicit factor of $q$; moving $p^n$ alone to one side reveals it equal to $q \times (\text{integer})$, so $q \mid p^n$. The coprimality hypothesis then does the decisive work: a number coprime to $p$ that divides a power of $p$ must be a unit. If one substitutes a *non-reduced* fraction, coprimality is unavailable and the argument stalls.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings IV — §2.7–2.8#Legal Operations|the topic page's Legal Operations]]:

1. **Write a rational in lowest terms.** Express $\alpha = p/q$ with $\gcd(p,q) = 1$ and $q > 0$. This installs the coprimality that the whole proof exploits.

2. **Substitute into the defining relation.** Replace $\alpha$ by $p/q$ in $f(\alpha) = 0$, turning a statement about $\alpha$ into a statement about the integers $p, q$.

3. **Clear denominators by the leading power.** Multiply the equation $f(p/q) = 0$ by $q^n$ (where $n = \deg f$) so that every term becomes an integer — the monicity of $f$ ensures $q^n$ is exactly the right multiplier.

4. **Isolate a single term to expose a divisibility.** Rearrange so that the term $p^n$ stands alone on one side, with every other term sharing a visible factor of $q$; this reads off $q \mid p^n$.

5. **Apply coprime cancellation (Euclid's lemma).** From $\gcd(p, q) = 1$ deduce $\gcd(p^n, q) = 1$, so $q \mid p^n$ forces $q \mid 1$.

6. **Conclude a unit / integrality.** $q \in \mathbb{Z}_{>0}$ with $q \mid 1$ gives $q = 1$, hence $\alpha = p \in \mathbb{Z}$.

---

# Hints

> [!note]- Hint 1
> Since $\alpha$ is rational, write it as a fraction. But not just any fraction — write it in *lowest terms*: $\alpha = p/q$ with $p, q$ integers, $q > 0$, and $p, q$ sharing no common factor. The coprimality of $p$ and $q$ is the hypothesis that will do all the work, so install it from the start.

> [!note]- Hint 2
> Substitute $\alpha = p/q$ into $f(\alpha) = 0$, where $f = X^n + a_{n-1}X^{n-1} + \cdots + a_0$. You get an equation full of fractions. Multiply the whole equation by $q^n$ to clear every denominator. Because $f$ is *monic*, the leading term $\alpha^n = p^n/q^n$ becomes exactly $p^n$ — no leftover $q$.

> [!note]- Hint 3
> After clearing denominators you have an integer equation in which one term is $p^n$ and *every other term* visibly contains a factor of $q$. Move $p^n$ to one side by itself. The other side is $q$ times an integer. So $q$ divides $p^n$.

> [!note]- Hint 4
> You now know $q \mid p^n$ and $\gcd(p, q) = 1$. A number coprime to $p$ cannot share any prime factor with $p$, hence cannot share one with $p^n$ either — so $\gcd(p^n, q) = 1$. The only positive integer dividing $p^n$ and coprime to it is $1$. Conclude $q = 1$, so $\alpha = p$ is an integer.

---

# Solution

The proof is the rational root theorem at its sharpest. Writing $\alpha$ in lowest terms and clearing denominators converts the constraint "$\alpha$ satisfies a monic integer polynomial" into the divisibility $q \mid p^n$; coprimality of $p$ and $q$ then forces $q = 1$. Monicity is what makes the leading term clear to exactly $p^n$ rather than $a_n p^n$.

**Step 1: Write $\alpha$ in lowest terms.**

Since $\alpha \in \mathbb{Q}$, write $\alpha = p/q$ with $p \in \mathbb{Z}$, $q \in \mathbb{Z}_{>0}$, and $\gcd(p, q) = 1$.

> [!note]- Derivation
> If $\alpha = 0$ then $\alpha = 0 \in \mathbb{Z}$ and there is nothing to prove, so assume $\alpha \neq 0$. Any rational number is a quotient of two integers; among all such representations choose one whose denominator is least positive — equivalently, divide numerator and denominator by their [[Def - Greatest Common Divisor and Least Common Multiple|greatest common divisor]]. The result is $\alpha = p/q$ with $q \in \mathbb{Z}_{>0}$, $p \in \mathbb{Z}$, and
> $$\gcd(p, q) = 1.$$
> This coprimality is not a cosmetic normalisation: it is the single hypothesis the rest of the proof consumes. Recording it now is the whole strategic decision of the problem.

**Step 2: Substitute and clear denominators.**

Let $f = X^n + a_{n-1}X^{n-1} + \cdots + a_1 X + a_0$ with each $a_i \in \mathbb{Z}$. Substituting $\alpha = p/q$ into $f(\alpha) = 0$ and multiplying by $q^n$ gives the integer equation
$$p^n + a_{n-1}\,p^{n-1}q + a_{n-2}\,p^{n-2}q^2 + \cdots + a_1\,p\,q^{n-1} + a_0\,q^n = 0.$$

> [!note]- Derivation
> Because $\alpha$ is an algebraic integer, by definition it is a root of a *monic* $f \in \mathbb{Z}[X]$; write $f = X^n + a_{n-1}X^{n-1} + \cdots + a_0$ with $n = \deg f \geq 1$ and $a_0, \dots, a_{n-1} \in \mathbb{Z}$. The leading coefficient is $1$ — this is the monicity, and it is used in a moment.
>
> Evaluate at $\alpha = p/q$:
> $$f\!\left(\tfrac{p}{q}\right) = \left(\tfrac{p}{q}\right)^n + a_{n-1}\left(\tfrac{p}{q}\right)^{n-1} + \cdots + a_1\left(\tfrac{p}{q}\right) + a_0 = 0.$$
> Every term has denominator a power of $q$, the largest being $q^n$ (from the leading term). Multiply the entire equation by $q^n$. The $i$-th term $a_i (p/q)^i$ becomes $a_i\, p^i\, q^{n-i}$, an integer since $n - i \geq 0$. In particular the leading term $(p/q)^n$, with $a_n = 1$ by monicity, becomes exactly
> $$1 \cdot p^n \cdot q^{0} = p^n,$$
> carrying *no* factor of $q$. (Had $f$ been non-monic with leading coefficient $a_n \neq 1$, this term would be $a_n p^n$ — and the proof below would yield $q \mid a_n$ instead of $q \mid 1$. Monicity is exactly what sharpens the conclusion.) The cleared equation is
> $$p^n + a_{n-1}\,p^{n-1}q + a_{n-2}\,p^{n-2}q^2 + \cdots + a_1\,p\,q^{n-1} + a_0\,q^n = 0,$$
> an identity in $\mathbb{Z}$.

**Step 3: Isolate $p^n$ to extract the divisibility $q \mid p^n$.**

Every term except $p^n$ contains a factor $q$. Moving $p^n$ to one side exhibits $p^n = q \cdot (\text{integer})$, so
$$q \;\bigm|\; p^n.$$

> [!note]- Derivation
> In the cleared equation
> $$p^n + \underbrace{a_{n-1}\,p^{n-1}q + a_{n-2}\,p^{n-2}q^2 + \cdots + a_1\,p\,q^{n-1} + a_0\,q^n}_{\text{every term has a factor } q} = 0,$$
> inspect the bracketed sum. The $i$-th term (for $i = 0, \dots, n-1$) is $a_i\,p^i\,q^{n-i}$ with $n - i \geq 1$, so it contains at least one factor of $q$. Factor $q$ out of the whole bracket:
> $$a_{n-1}\,p^{n-1}q + \cdots + a_0\,q^n = q\bigl(a_{n-1}\,p^{n-1} + a_{n-2}\,p^{n-2}q + \cdots + a_0\,q^{n-1}\bigr).$$
> Call the integer in parentheses $N := a_{n-1}\,p^{n-1} + a_{n-2}\,p^{n-2}q + \cdots + a_0\,q^{n-1} \in \mathbb{Z}$. The equation becomes $p^n + qN = 0$, that is
> $$p^n = -\,q\,N.$$
> The right-hand side is $q$ times the integer $-N$. Therefore $q$ divides $p^n$:
> $$q \mid p^n.$$
> This is the crux. The defining equation $f(\alpha) = 0$ has been converted, by clearing denominators and isolating the leading power, into a divisibility relation between the numerator and denominator of $\alpha$.

**Step 4: Coprimality forces $q = 1$, hence $\alpha \in \mathbb{Z}$.**

Since $\gcd(p, q) = 1$, also $\gcd(p^n, q) = 1$; combined with $q \mid p^n$ this gives $q = 1$. Therefore $\alpha = p/1 = p \in \mathbb{Z}$.

> [!note]- Derivation
> From Step 1, $\gcd(p, q) = 1$: $p$ and $q$ share no prime factor. Raising $p$ to a power introduces no new prime factors — the prime factors of $p^n$ are exactly the prime factors of $p$. Hence $p^n$ and $q$ also share no prime factor:
> $$\gcd(p^n, q) = 1.$$
> (This is Euclid's lemma in the form "coprime to $p$ implies coprime to every power of $p$": if a prime $\ell$ divided both $q$ and $p^n$, then $\ell \mid p^n$ forces $\ell \mid p$, so $\ell$ would divide both $p$ and $q$, contradicting $\gcd(p,q) = 1$.)
>
> Now combine with Step 3's $q \mid p^n$. A positive integer $q$ that divides $p^n$ and is coprime to $p^n$ must divide $\gcd(p^n, q) = 1$:
> $$q \mid 1.$$
> The only positive integer dividing $1$ is $1$ itself, so $q = 1$. Therefore
> $$\alpha = \frac{p}{q} = \frac{p}{1} = p \in \mathbb{Z}.$$
> A rational number that is an algebraic integer is an integer. $\blacksquare$

> [!note]- Alternative derivation via Gauss's lemma (the textbook proof)
> A second, more structural proof routes through the minimal polynomial and [[Thm - Gauss's Lemma|Gauss's lemma]] — this is the argument in the source text.
>
> Let $\alpha \in \mathbb{Q}$ be an algebraic integer and let $f_\alpha \in \mathbb{Z}[X]$ be its [[Def - Algebraic Integer and Minimal Polynomial|minimal polynomial]]: by [[Thm - The Minimal Polynomial Generates the Kernel Ideal|the kernel-ideal theorem]], $f_\alpha$ is monic and *irreducible* in $\mathbb{Z}[X]$, and it generates the [[Def - Ideal|ideal]] of all integer polynomials vanishing at $\alpha$.
>
> Work in $\mathbb{Q}[X]$, which *is* a principal ideal domain (indeed a Euclidean domain). Since $\alpha \in \mathbb{Q}$ is a root of $f_\alpha$, the linear polynomial $X - \alpha \in \mathbb{Q}[X]$ divides $f_\alpha$ in $\mathbb{Q}[X]$:
> $$f_\alpha = (X - \alpha)\,g, \qquad g \in \mathbb{Q}[X].$$
> By [[Thm - Gauss's Lemma|Gauss's lemma]], a primitive polynomial of $\mathbb{Z}[X]$ that is irreducible over $\mathbb{Z}$ is also irreducible over $\mathbb{Q}$. The minimal polynomial $f_\alpha$ is monic, hence primitive, and irreducible over $\mathbb{Z}$ — so $f_\alpha$ is **irreducible over $\mathbb{Q}$**.
>
> An irreducible polynomial admits no factorisation into two factors of positive degree. In $f_\alpha = (X - \alpha)g$ the factor $X - \alpha$ has degree $1 > 0$; irreducibility forces the other factor $g$ to have degree $0$, i.e. $g$ is a non-zero constant. Comparing leading coefficients — $f_\alpha$ monic, $X - \alpha$ monic — gives $g = 1$. Hence
> $$f_\alpha = X - \alpha.$$
> But $f_\alpha \in \mathbb{Z}[X]$, so its constant term $-\alpha$ is an integer, i.e. $\alpha \in \mathbb{Z}$. $\blacksquare$
>
> The two proofs illuminate each other: the rational-root-theorem proof is the *explicit* arithmetic shadow of the Gauss's-lemma proof. "Clearing denominators and tracking content" is precisely the mechanism inside Gauss's lemma, and "the linear factor $X - \alpha$ must already have integer coefficients" is the structural restatement of "$q = 1$".

> [!note]- Complete formal solution
> **Claim.** If $\alpha \in \mathbb{Q}$ is a root of a monic $f \in \mathbb{Z}[X]$, then $\alpha \in \mathbb{Z}$.
>
> If $\alpha = 0$ the claim is immediate, so assume $\alpha \neq 0$ and write $\alpha = p/q$ in lowest terms: $p \in \mathbb{Z}$, $q \in \mathbb{Z}_{>0}$, $\gcd(p,q) = 1$.
>
> Write $f = X^n + a_{n-1}X^{n-1} + \cdots + a_1 X + a_0$ with $a_i \in \mathbb{Z}$ and $n \geq 1$. From $f(\alpha) = 0$,
> $$\left(\tfrac{p}{q}\right)^n + a_{n-1}\left(\tfrac{p}{q}\right)^{n-1} + \cdots + a_1\left(\tfrac{p}{q}\right) + a_0 = 0.$$
> Multiply by $q^n$; since $f$ is monic the leading term yields $p^n$ exactly:
> $$p^n + a_{n-1}\,p^{n-1}q + a_{n-2}\,p^{n-2}q^2 + \cdots + a_1\,p\,q^{n-1} + a_0\,q^n = 0.$$
> Each term other than $p^n$ has a factor $q$; setting $N := a_{n-1}p^{n-1} + a_{n-2}p^{n-2}q + \cdots + a_0 q^{n-1} \in \mathbb{Z}$, the equation reads $p^n = -qN$, so $q \mid p^n$.
>
> Since $\gcd(p,q) = 1$, no prime divides both $p$ and $q$; as the primes of $p^n$ are those of $p$, no prime divides both $p^n$ and $q$, i.e. $\gcd(p^n, q) = 1$. A positive $q$ with $q \mid p^n$ and $\gcd(p^n, q) = 1$ satisfies $q \mid 1$, so $q = 1$.
>
> Therefore $\alpha = p/q = p \in \mathbb{Z}$. $\blacksquare$

---

# Key Takeaways

**To prove a rational number is forced to be an integer, write it in lowest terms and mine the defining equation for a divisibility on the denominator.** This is the master template for *integrality* results, and it recurs far beyond this exercise. The pattern: you have a rational $\alpha$ subject to some algebraic constraint, and you want $\alpha \in \mathbb{Z}$; write $\alpha = p/q$ with $\gcd(p,q) = 1$, push $\alpha = p/q$ through the constraint, clear denominators, and rearrange until the equation says "$q$ divides something coprime to $q$" — whence $q = 1$. The same skeleton proves the *rational root theorem* in full (a rational root $p/q$ of $\sum a_i X^i$ has $p \mid a_0$ and $q \mid a_n$ — isolate the constant term for the first, the leading term for the second), proves that a rational number whose square is an integer is an integer (so $\sqrt2$ is irrational: it satisfies $X^2 - 2$, monic, so a rational root would be an integer, and no integer squares to $2$), and proves that the only rational eigenvalues of an integer matrix are integers (they are roots of the monic characteristic polynomial). The trigger is always the same: a rational constrained by a *monic* integer polynomial relation.

**Monicity is the hypothesis that sharpens "$q$ divides the leading coefficient" into "$q$ divides $1$".** The general rational root theorem says only that the denominator $q$ of a rational root divides the *leading coefficient* $a_n$. The algebraic-integer hypothesis sets $a_n = 1$, and "$q \mid 1$" is a vastly stronger conclusion than "$q \mid a_n$" — it pins $q$ exactly. This is *why* the definition of algebraic integer demands a *monic* polynomial and not merely an integer polynomial: monic is precisely the condition under which rational solutions are forced all the way down to $\mathbb{Z}$. Drop monicity and the statement collapses — $2X - 1$ has the non-integer rational root $\tfrac12$. Whenever you see "monic integer polynomial" in a hypothesis, the reflex should be: *the leading term will clear to a pure power with no leftover coefficient, and that is what makes the denominator a unit.* Conversely, when a desired integrality conclusion fails, suspect a missing monicity hypothesis.

**Coprimality converts a divisibility into an equality — "$q \mid p^n$ with $\gcd(p,q)=1$" is the engine, not a side remark.** The decisive inference is not "$q \mid p^n$" by itself (true but weak) but its combination with $\gcd(p, q) = 1$. Euclid's lemma — coprime to $p$ implies coprime to every power of $p$ — promotes $q \mid p^n$ to $q \mid \gcd(p^n, q) = 1$. This "$a \mid bc$, $\gcd(a,b) = 1 \Rightarrow a \mid c$" cancellation is the workhorse of elementary number theory, and recognising when it applies is a transferable skill: any time a divisibility $q \mid (\text{product})$ appears and you know $q$ is coprime to one of the factors, you may *delete* that factor. The reason to write the fraction in lowest terms at the very start is to *manufacture* this coprimality so it is on hand when the divisibility surfaces. A proof that substitutes a non-reduced fraction has thrown away the only tool that finishes the argument.

**The same theorem has an arithmetic proof and a structural proof, and seeing both is worth more than seeing either.** The rational-root-theorem proof is hands-on: lowest terms, clear denominators, isolate, cancel. The Gauss's-lemma proof is structural: the minimal polynomial is monic irreducible, the linear factor $X - \alpha$ divides it over $\mathbb{Q}$, irreducibility forces $f_\alpha = X - \alpha$, so $\alpha$ is the integer constant term. These are not unrelated tricks — the structural proof is the *conceptual compression* of the arithmetic one. "Clearing denominators and watching them cancel against content" is literally the mechanism inside the proof of Gauss's lemma; "the linear factor must have integer coefficients" is the structural shadow of "$q = 1$". The lesson for spaced practice: when you meet a number-theoretic fact with a grubby computational proof, ask whether it is a special case of a clean [[Def - Ring|ring]]-theoretic theorem — here, integrality of rational algebraic integers is the degree-$1$ case of "the minimal polynomial of an algebraic integer is the monic generator and stays irreducible over $\mathbb{Q}$". Holding both pictures lets you *rederive* the result from whichever end you remember, and tells you which generalisations are available (the Gauss's-lemma proof immediately generalises from $\mathbb{Z} \subset \mathbb{Q}$ to any UFD inside its field of fractions, and indeed to the integral closure of any integrally closed domain — a generalisation the arithmetic proof does not obviously suggest).

**This is the base case of "the algebraic integers form a ring", and the foundation under every quadratic-field integrality computation.** The result looks modest — "no fractional algebraic integers among the rationals" — but it is the indispensable starting point for the structure theory. It is what makes "ring of integers" a well-defined notion: when one computes the ring of integers of a number field $K$, this lemma is the $K = \mathbb{Q}$ base case, asserting that the ring of integers of $\mathbb{Q}$ is exactly $\mathbb{Z}$, no larger. It is also the silent justification behind [[Ex - Deciding whether a number is an algebraic integer]]: there, the verdict that $\tfrac12(1+\sqrt3)$ is *not* an algebraic integer ultimately rests on knowing that its rational coefficients, were they forced by an integer relation, would have to be genuine integers — i.e. on this very theorem. More broadly, "$\mathbb{Z}$ is integrally closed in $\mathbb{Q}$" is the prototype of an *integrally closed domain*, and recognising the present exercise as that prototype tells you exactly which abstract theorem to invoke when the same rigidity is needed one field up.

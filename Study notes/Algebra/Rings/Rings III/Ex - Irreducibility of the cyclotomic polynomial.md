---
type: exercise
subject: ring-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Eisenstein's Criterion"
  - "Thm - Gauss's Lemma"
  - "Def - Content and Primitive Polynomial"
  - "Def - Irreducible and Prime Elements"
  - "Def - Polynomial Ring"
tags: [algebra, ring-theory]
---

# Problem Statement

Let $p$ be a prime number. The **$p$-th cyclotomic polynomial** is
$$\Phi_p(X) = X^{p-1} + X^{p-2} + \cdots + X^2 + X + 1 \in \mathbb{Z}[X].$$

Prove that $\Phi_p(X)$ is **irreducible over $\mathbb{Q}$**.

Notice first that Eisenstein's criterion cannot be applied to $\Phi_p$ as it stands — every coefficient equals $1$, so no prime divides any coefficient. The task is to find a manoeuvre that exposes a hidden Eisenstein pattern.

**Recall:**

The objects are the [[Def - Polynomial Ring|polynomial ring]] $\mathbb{Z}[X]$, the notion of [[Def - Content and Primitive Polynomial|primitivity]], [[Def - Irreducible and Prime Elements|irreducibility]], and Eisenstein's criterion.

The polynomial $\Phi_p$ is the quotient that appears in the **finite geometric series**: since $X^p - 1 = (X - 1)(X^{p-1} + \cdots + X + 1)$, we have the identity
$$\Phi_p(X) = \frac{X^p - 1}{X - 1}.$$
This is an identity of polynomials in $\mathbb{Z}[X]$ — the division is exact, with no remainder.

**[[Thm - Eisenstein's Criterion|Eisenstein's criterion]].** Let $R$ be a unique factorization domain and $f = a_0 + a_1 X + \cdots + a_n X^n \in R[X]$ a primitive polynomial with $a_n \neq 0$. If there is a prime $p \in R$ with (i) $p \nmid a_n$, (ii) $p \mid a_i$ for all $0 \leq i < n$, and (iii) $p^2 \nmid a_0$, then $f$ is irreducible in $R[X]$, hence in $F[X]$ for $F$ the field of fractions of $R$.

The criterion needs a prime dividing every coefficient except the leading one, with the square of the prime not dividing the constant term. $\Phi_p$ obviously fails this: all its coefficients are $1$. The strategy will be to *substitute a shifted variable* and apply the criterion to the result.

![[Thm - Gauss's Lemma#Statement]]

Gauss's lemma converts irreducibility in $\mathbb{Z}[X]$ into irreducibility in $\mathbb{Q}[X]$ for primitive polynomials. As always, Eisenstein's criterion is fundamentally a $\mathbb{Z}[X]$ statement and Gauss is the bridge to $\mathbb{Q}$.

A standing fact used at the end: the **binomial coefficients** satisfy $p \mid \binom{p}{k}$ for $1 \leq k \leq p - 1$ whenever $p$ is prime. This is because $\binom{p}{k} = \frac{p!}{k!\,(p-k)!}$ is an integer, the numerator $p!$ carries exactly one factor of $p$, and the denominator $k!\,(p-k)!$ carries none (every factor in it is strictly between $1$ and $p$, so coprime to $p$); the single factor of $p$ survives.

---

# Convergent Strategy

**Problem class.** This is *irreducibility certification when the criterion does not directly apply* — the hardest tier of the [[Rings III — §2.5–2.6]] strategy. The polynomial is genuinely irreducible, but Eisenstein's criterion is blind to it in its given form. The technique is a **change of variable**: find an invertible substitution $X \mapsto X + c$ that transforms $\Phi_p$ into a polynomial Eisenstein *can* see, prove the transformed polynomial irreducible, and transport the conclusion back.

**Assumption pattern.** The signal that a substitution will help is twofold. First, $\Phi_p$ has a clean closed form, $\Phi_p(X) = (X^p - 1)/(X - 1)$, which is the kind of expression a substitution can simplify. Second, the *root structure* hints at the right shift: the roots of $\Phi_p$ are the primitive $p$-th roots of unity, clustered near $X = 1$ on the unit circle, so the shift $X \mapsto X + 1$ moves the interesting behaviour to the origin, where Eisenstein "looks". The substitution $Y = X - 1$, equivalently $X = Y + 1$, is the canonical choice.

**Theorem routing.** Three results chain. The substitution turns $\Phi_p(X)$ into $\Phi_p(X+1) = \frac{(X+1)^p - 1}{X}$; the **binomial theorem** expands $(X+1)^p$ and the divisibility $p \mid \binom{p}{k}$ supplies the Eisenstein pattern. Then [[Thm - Eisenstein's Criterion]] certifies $\Phi_p(X+1)$ irreducible in $\mathbb{Z}[X]$, and [[Thm - Gauss's Lemma]] lifts this to $\mathbb{Q}[X]$. A fourth, structural, fact closes the loop: the substitution $X \mapsto X + 1$ is a **[[Def - Ring|ring]] automorphism** of $\mathbb{Q}[X]$, so it preserves the property of being irreducible — a factorisation of $\Phi_p(X)$ would push forward to a factorisation of $\Phi_p(X+1)$, and conversely.

**Key decision point.** Two non-obvious moves. The first is *to substitute at all* — recognising that a polynomial with no Eisenstein prime might acquire one after an invertible change of variable. The second is *justifying that the substitution preserves irreducibility*: it is not enough to prove $\Phi_p(X+1)$ irreducible; one must argue that irreducibility is invariant under $X \mapsto X+1$. The cleanest justification is that $X \mapsto X+1$ is an automorphism, so it carries genuine factorisations to genuine factorisations in both directions, and a unit to a unit. Skipping this step is the most common gap in the argument.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings III — §2.5–2.6#Legal Operations|the topic page's Legal Operations]]:

1. **Substitute a shifted variable to expose an Eisenstein prime.** Replace $X$ by $X + 1$; a polynomial with no usable prime can become one whose coefficients all share a prime factor.

2. **Use a closed form to compute the substituted polynomial.** Apply the substitution to the identity $\Phi_p(X) = (X^p-1)/(X-1)$ rather than to the expanded sum, turning the computation into $\frac{(X+1)^p - 1}{X}$.

3. **Expand by the binomial theorem and read off divisibility.** Use $p \mid \binom{p}{k}$ for $1 \leq k \leq p-1$ to see that every non-leading coefficient of $\Phi_p(X+1)$ is divisible by $p$.

4. **Scan the coefficient list for the Eisenstein pattern** and apply [[Thm - Eisenstein's Criterion|Eisenstein's criterion]] to $\Phi_p(X+1)$.

5. **Invoke automorphism-invariance of irreducibility.** Since $X \mapsto X+1$ is a ring automorphism of $\mathbb{Q}[X]$, irreducibility of $\Phi_p(X+1)$ transfers back to irreducibility of $\Phi_p(X)$.

6. **Transport irreducibility from $\mathbb{Z}[X]$ to $\mathbb{Q}[X]$ via Gauss.**

---

# Hints

> [!note]- Hint 1
> Eisenstein's criterion fails on $\Phi_p$ because every coefficient is $1$. But irreducibility is not changed by an *invertible* change of variable. Try substituting $X \mapsto X + 1$ and see whether the new polynomial is more cooperative. To compute the substitution, do not expand the sum — use the closed form $\Phi_p(X) = \dfrac{X^p - 1}{X - 1}$.

> [!note]- Hint 2
> Substituting $X \mapsto X + 1$ into $\dfrac{X^p - 1}{X - 1}$ gives $\dfrac{(X+1)^p - 1}{(X+1) - 1} = \dfrac{(X+1)^p - 1}{X}$. Now expand $(X+1)^p$ by the binomial theorem. The $-1$ cancels the constant term $\binom{p}{0} = 1$, and dividing by $X$ lowers every exponent by one.

> [!note]- Hint 3
> After the expansion you should find
> $$\Phi_p(X+1) = X^{p-1} + \binom{p}{1}X^{p-2} + \binom{p}{2}X^{p-3} + \cdots + \binom{p}{p-1}.$$
> Recall the arithmetic fact $p \mid \binom{p}{k}$ for every $1 \leq k \leq p - 1$. What does this say about the non-leading coefficients? And what is the constant term — is it divisible by $p$? By $p^2$?

> [!note]- Hint 4
> The leading coefficient is $1$ (not divisible by $p$); every other coefficient is some $\binom{p}{k}$ with $1 \leq k \leq p-1$ (all divisible by $p$); the constant term is $\binom{p}{p-1} = p$ (divisible by $p$ but not by $p^2$). That is exactly the Eisenstein pattern at the prime $p$. Conclude $\Phi_p(X+1)$ is irreducible — then argue that $X \mapsto X+1$ being an automorphism forces $\Phi_p(X)$ irreducible too.

---

# Solution

Eisenstein's criterion cannot see $\Phi_p$ directly, but the substitution $X \mapsto X + 1$ transforms it into a polynomial whose every non-leading coefficient is a binomial coefficient $\binom{p}{k}$ divisible by $p$, with constant term exactly $p$. Eisenstein then applies, and because $X \mapsto X+1$ is an automorphism, irreducibility transfers back.

**Step 1: Compute $\Phi_p(X+1)$ using the closed form.**

Substituting $X \mapsto X+1$ into $\Phi_p(X) = \dfrac{X^p - 1}{X - 1}$ gives
$$\Phi_p(X+1) = \frac{(X+1)^p - 1}{X}.$$

> [!note]- Derivation
> Over $\mathbb{Z}[X]$ the factorisation of the geometric series gives the exact identity
> $$X^p - 1 = (X - 1)\big(X^{p-1} + X^{p-2} + \cdots + X + 1\big) = (X - 1)\,\Phi_p(X),$$
> so $\Phi_p(X) = (X^p - 1)/(X - 1)$ as an identity in $\mathbb{Z}[X]$ (the quotient is exact).
>
> Substitution $X \mapsto X + 1$ is the ring homomorphism $\mathbb{Z}[X] \to \mathbb{Z}[X]$ that evaluates a polynomial at $X + 1$; it respects sums, products and the exact quotient above. Applying it,
> $$\Phi_p(X + 1) = \frac{(X+1)^p - 1}{(X+1) - 1} = \frac{(X+1)^p - 1}{X}.$$
> The denominator collapsed from $X + 1 - 1$ to $X$ — this is the entire point of shifting by $1$ rather than by some other constant: it sends the awkward root of $X - 1$ (the point $X = 1$) to the origin.

**Step 2: Expand and identify the coefficients.**

Expanding the numerator by the binomial theorem and dividing by $X$,
$$\Phi_p(X+1) = X^{p-1} + \binom{p}{1}X^{p-2} + \binom{p}{2}X^{p-3} + \cdots + \binom{p}{p-2}X + \binom{p}{p-1}.$$
The leading coefficient is $1$; every other coefficient is a binomial coefficient $\binom{p}{k}$ with $1 \leq k \leq p - 1$; the constant term is $\binom{p}{p-1} = p$.

> [!note]- Derivation
> The **binomial theorem** gives
> $$(X+1)^p = \sum_{k=0}^{p} \binom{p}{k} X^{p-k} = X^p + \binom{p}{1}X^{p-1} + \binom{p}{2}X^{p-2} + \cdots + \binom{p}{p-1}X + \binom{p}{p}.$$
> The bottom term is $\binom{p}{p} = 1$. Subtracting $1$ cancels it exactly:
> $$(X+1)^p - 1 = X^p + \binom{p}{1}X^{p-1} + \binom{p}{2}X^{p-2} + \cdots + \binom{p}{p-1}X.$$
> Every surviving term contains at least one factor of $X$, so dividing by $X$ is exact and lowers each exponent by $1$:
> $$\Phi_p(X+1) = \frac{(X+1)^p - 1}{X} = X^{p-1} + \binom{p}{1}X^{p-2} + \binom{p}{2}X^{p-3} + \cdots + \binom{p}{p-2}X + \binom{p}{p-1}.$$
> Reading off the coefficient list (constant term first):
> $$a_0 = \binom{p}{p-1},\quad a_1 = \binom{p}{p-2},\quad \dots,\quad a_{p-2} = \binom{p}{1},\quad a_{p-1} = \binom{p}{0} = 1.$$
> So the leading coefficient $a_{p-1} = 1$, the constant term $a_0 = \binom{p}{p-1} = p$, and each interior coefficient is $\binom{p}{k}$ for some $1 \leq k \leq p-1$.

**Step 3: Apply Eisenstein's criterion at the prime $p$.**

The three Eisenstein conditions hold for $\Phi_p(X+1)$ at the prime $p$, so $\Phi_p(X+1)$ is irreducible in $\mathbb{Z}[X]$, and by Gauss's lemma in $\mathbb{Q}[X]$.

> [!note]- Derivation
> $\Phi_p(X+1)$ is monic (leading coefficient $1$), hence primitive — the hypothesis of [[Thm - Eisenstein's Criterion|Eisenstein's criterion]] is met. Check the three conditions at $p$:
> - **$p \nmid a_{p-1}$:** the leading coefficient is $1$, and $p \nmid 1$. ✓
> - **$p \mid a_i$ for all $0 \leq i < p-1$:** every interior coefficient is $\binom{p}{k}$ with $1 \leq k \leq p-1$, and the standing fact $p \mid \binom{p}{k}$ holds for exactly that range of $k$. ✓
> - **$p^2 \nmid a_0$:** the constant term is $a_0 = \binom{p}{p-1} = \dfrac{p!}{(p-1)!\,1!} = p$. Now $p^2 \mid p$ is false (it would force $p \mid 1$). So $p^2 \nmid a_0$. ✓
>
> By Eisenstein's criterion, $\Phi_p(X+1)$ is irreducible in $\mathbb{Z}[X]$. Being monic it is primitive, so [[Thm - Gauss's Lemma|Gauss's lemma]] gives that $\Phi_p(X+1)$ is irreducible in $\mathbb{Q}[X]$ as well.
>
> The constant term being *exactly* $p$ — not merely divisible by $p$ — is the delicate point. Eisenstein needs $p^2 \nmid a_0$, and $a_0 = \binom{p}{p-1} = p$ satisfies this on the nose. Had the constant term been $p^2$ or $0$, the criterion would have failed.

**Step 4: Transfer irreducibility back to $\Phi_p(X)$.**

The substitution $X \mapsto X + 1$ is a ring automorphism of $\mathbb{Q}[X]$, so it preserves irreducibility. Since $\Phi_p(X+1)$ is irreducible, so is $\Phi_p(X)$. Hence $\Phi_p$ is irreducible over $\mathbb{Q}$.

> [!note]- Derivation
> Let $\sigma : \mathbb{Q}[X] \to \mathbb{Q}[X]$ be the substitution $\sigma(f)(X) = f(X + 1)$. This is a ring homomorphism (evaluation maps always are). It has a two-sided inverse, namely the substitution $\tau(f)(X) = f(X - 1)$: indeed $\tau\sigma(f)(X) = \sigma(f)(X-1) = f((X-1)+1) = f(X)$, and likewise $\sigma\tau = \mathrm{id}$. So $\sigma$ is a **ring automorphism** of $\mathbb{Q}[X]$.
>
> An automorphism preserves every ring-theoretic property. In particular it carries units to units — the units of $\mathbb{Q}[X]$ are the non-zero constants, and $\sigma$ fixes constants — and it carries genuine factorisations to genuine factorisations. Concretely, suppose $\Phi_p(X)$ were *reducible*, say $\Phi_p(X) = g(X)\,h(X)$ with $g, h$ non-units (positive degree) in $\mathbb{Q}[X]$. Apply $\sigma$:
> $$\Phi_p(X+1) = \sigma(\Phi_p) = \sigma(g)\,\sigma(h) = g(X+1)\,h(X+1).$$
> Since $\sigma$ preserves degree (substituting $X+1$ does not change the degree of a polynomial), $g(X+1)$ and $h(X+1)$ again have positive degree, hence are non-units. So $\Phi_p(X+1)$ would be reducible — contradicting Step 3.
>
> Therefore $\Phi_p(X)$ is irreducible in $\mathbb{Q}[X]$: the $p$-th cyclotomic polynomial is irreducible over $\mathbb{Q}$. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** For every prime $p$, $\Phi_p(X) = X^{p-1} + \cdots + X + 1$ is irreducible over $\mathbb{Q}$.
>
> From the geometric-series factorisation $X^p - 1 = (X-1)\Phi_p(X)$ in $\mathbb{Z}[X]$ we have $\Phi_p(X) = (X^p - 1)/(X - 1)$. Substituting $X \mapsto X + 1$,
> $$\Phi_p(X+1) = \frac{(X+1)^p - 1}{X}.$$
> By the binomial theorem $(X+1)^p - 1 = \sum_{k=0}^{p-1}\binom{p}{k}X^{p-k}$ (the $k = p$ term $\binom{p}{p} = 1$ is cancelled by $-1$); dividing by $X$,
> $$\Phi_p(X+1) = X^{p-1} + \binom{p}{1}X^{p-2} + \cdots + \binom{p}{p-2}X + \binom{p}{p-1}.$$
> This is monic, hence primitive. Apply [[Thm - Eisenstein's Criterion|Eisenstein's criterion]] at $p$: the leading coefficient is $1$, so $p \nmid$ it; each interior coefficient is $\binom{p}{k}$ with $1 \leq k \leq p-1$, and $p \mid \binom{p}{k}$ for all such $k$ (since $\binom pk = p!/(k!(p-k)!)$ has exactly one factor of $p$ in the numerator and none in the denominator); the constant term is $\binom{p}{p-1} = p$, and $p^2 \nmid p$. All conditions hold, so $\Phi_p(X+1)$ is irreducible in $\mathbb{Z}[X]$, and by [[Thm - Gauss's Lemma|Gauss's lemma]] in $\mathbb{Q}[X]$.
>
> The map $\sigma : f(X) \mapsto f(X+1)$ is a ring automorphism of $\mathbb{Q}[X]$ (inverse $f(X) \mapsto f(X-1)$), preserving degree and units. If $\Phi_p(X) = gh$ were a non-trivial factorisation, then $\Phi_p(X+1) = g(X+1)h(X+1)$ would be one too, contradicting the previous paragraph. Hence $\Phi_p(X)$ is irreducible over $\mathbb{Q}$. $\blacksquare$

---

# Key Takeaways

**A change of variable can manufacture an Eisenstein prime where none was visible — irreducibility is invariant under invertible substitutions.** This is the central, transferable lesson. Eisenstein's criterion is a *sufficient* test; its silence on a polynomial means only that the criterion in that form does not apply, not that the polynomial is reducible. The repair, when you suspect irreducibility, is to act on the polynomial by an automorphism of $\mathbb{Q}[X]$ — most usefully a shift $X \mapsto X + c$ — and re-test. The shifts $X \mapsto X + c$ are the simplest automorphisms, and one of them often drags the coefficient list into Eisenstein range. The trigger to try this: a polynomial that "should" be irreducible (it has no rational roots, it is a minimal polynomial of some algebraic number) but displays no prime in its coefficient list. The cyclotomic polynomial is the paradigm — all-ones coefficients are maximally hostile to Eisenstein, yet one shift fixes everything. The same trick proves, for instance, that $X^4 + 1$ is irreducible over $\mathbb{Q}$ via $X \mapsto X + 1$ (giving $X^4 + 4X^3 + 6X^2 + 4X + 2$, Eisenstein at $2$), even though $X^4 + 1$ has no Eisenstein prime and — as [[Ex - Reduction modulo a prime as an irreducibility test]] shows — is reducible modulo *every* prime.

**The right substitution is dictated by where the polynomial's roots or its defining quotient misbehave.** The choice $X \mapsto X + 1$ is not arbitrary. The closed form $\Phi_p(X) = (X^p - 1)/(X - 1)$ has its denominator vanish at $X = 1$, and the roots of $\Phi_p$ — the primitive $p$-th roots of unity — cluster around $X = 1$. Shifting by $+1$ moves that point to the origin, which is exactly where Eisenstein's criterion concentrates its attention (the constant term and the low-degree coefficients). The general heuristic for choosing a substitution: identify the special point — a root, a pole of a defining rational expression, a point of high multiplicity — and translate it to $0$. This converts "interesting behaviour near $X = c$" into "small coefficients divisible by a prime", which is the Eisenstein signature. Using the closed form rather than the expanded sum is the computational counterpart: $\frac{(X+1)^p - 1}{X}$ is far easier to expand than $\sum (X+1)^k$ term by term.

**Proving the substituted polynomial irreducible is only half the job — invariance of irreducibility under the substitution must be argued explicitly.** The most common error in this proof is to compute $\Phi_p(X+1)$, apply Eisenstein, and *stop*, as though irreducibility of $\Phi_p(X+1)$ were literally irreducibility of $\Phi_p(X)$. It is not — they are different polynomials. The bridge is the structural fact that $X \mapsto X + 1$ is a ring *automorphism* of $\mathbb{Q}[X]$: it is bijective, with inverse $X \mapsto X - 1$, it preserves degree, and it sends units to units. An automorphism carries non-trivial factorisations to non-trivial factorisations in *both* directions, so reducibility of $\Phi_p(X)$ would force reducibility of $\Phi_p(X+1)$ and vice versa. Whenever a proof transforms an object to make a theorem applicable, the transformation must be shown to *preserve the property in question* — here, irreducibility — and the cleanest way to guarantee that is for the transformation to be an isomorphism. This same discipline appears whenever one "changes coordinates" to simplify a problem: the change must be invertible, and one must check the conclusion is coordinate-independent.

**The constant term landing exactly on $p$ — divisible by $p$ but not $p^2$ — is the delicate hinge, and it is no accident.** Eisenstein's third condition, $p^2 \nmid a_0$, is the one that most often fails and the one easiest to overlook. Here the constant term of $\Phi_p(X+1)$ is $\binom{p}{p-1}$, which equals $p$ *exactly*. Divisible by $p$: yes, so the second condition is satisfied. Divisible by $p^2$: no, so the third is satisfied. Both conditions on $a_0$ are met precisely because $a_0$ is $p$ to the first power and no higher. This razor's-edge fit is a recurring feature of well-posed Eisenstein arguments — the constant term must be a *unit times a single copy of the prime*. When constructing or recognising Eisenstein-amenable polynomials, the constant term deserves separate scrutiny from the interior coefficients: the interior needs only divisibility by $p$, but the constant needs divisibility by $p$ *and* non-divisibility by $p^2$, a two-sided constraint. The same care is needed in [[Ex - Irreducibility by Eisenstein's criterion]], where choosing a wrong prime fails exactly this constant-term test.

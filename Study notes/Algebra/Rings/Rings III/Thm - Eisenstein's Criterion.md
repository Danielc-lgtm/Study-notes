---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Polynomial Ring"
  - "Def - Integral Domain"
  - "Def - Unique Factorization Domain"
  - "Def - Field of Fractions"
  - "Def - Irreducible and Prime Elements"
  - "Def - Content and Primitive Polynomial"
  - "Thm - Gauss's Lemma"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is a [[Def - Unique Factorization Domain|unique factorization domain]] (UFD) and $F = \operatorname{Frac}(R)$ is its [[Def - Field of Fractions|field of fractions]]. A polynomial $f \in R[X]$ in the [[Def - Polynomial Ring|polynomial ring]] over $R$ is written $f = a_0 + a_1 X + \cdots + a_n X^n$ with $a_n \neq 0$, so $\deg f = n$; $a_n$ is the **leading coefficient** and $a_0$ the **constant term**. The polynomial $f$ is [[Def - Content and Primitive Polynomial|**primitive**]] when its [[Def - Content and Primitive Polynomial|content]] $c(f) = \gcd(a_0, \dots, a_n)$ is a [[Def - Unit and Field|unit]]; every monic polynomial is primitive. An element $p \in R$ is [[Def - Irreducible and Prime Elements|**irreducible**]] if it is a non-zero non-unit not splitting into two non-units; in the UFD $R$ every irreducible is also [[Def - Irreducible and Prime Elements|**prime**]] ($p \mid xy \Rightarrow p \mid x$ or $p \mid y$). We write $p \mid a$ for "$p$ divides $a$" and $p \nmid a$ for its negation, and $\binom{p}{i}$ for a binomial coefficient. The full symbol registry is on [[Rings III — §2.5–2.6]].

---

# Statement

> **Eisenstein's Criterion.** Let $R$ be a [[Def - Unique Factorization Domain|unique factorization domain]] and let
> $$f = a_0 + a_1 X + a_2 X^2 + \cdots + a_n X^n \in R[X]$$
> be [[Def - Content and Primitive Polynomial|primitive]] with $a_n \neq 0$. Suppose there is an [[Def - Irreducible and Prime Elements|irreducible]] element $p \in R$ such that:
>
> 1. $p \nmid a_n$ — $p$ does **not** divide the leading coefficient;
> 2. $p \mid a_i$ for all $0 \leq i < n$ — $p$ divides **every** lower coefficient;
> 3. $p^2 \nmid a_0$ — $p^2$ does **not** divide the constant term.
>
> Then $f$ is **irreducible in $R[X]$**, and hence — by [[Thm - Gauss's Lemma|Gauss's lemma]] — **irreducible in $F[X]$**, where $F$ is the field of fractions of $R$.

The three conditions are a checklist run on the coefficients: miss the top, hit all the rest, and do not hit the bottom too hard.

---

# Motivation

We have just learned, from [[Thm - [[Thm - Polynomial Rings over a UFD|Polynomial Rings over a UFD]]|the theorem that $R[X]$ is a UFD]], that polynomials over a UFD factor uniquely into irreducible polynomials. That is a fine existence-and-uniqueness statement, but it leaves the *practical* question wide open: given a specific polynomial, **how do I tell whether it is irreducible?** This is genuinely hard. To prove a degree-$n$ polynomial irreducible directly, one must rule out *every* way it could factor — every pairing of a degree-$k$ factor with a degree-$(n-k)$ factor — and the space of candidate factors is large. We need a *test*: a condition that can be checked at a glance and that, when it holds, certifies irreducibility outright.

Eisenstein's criterion is exactly such a test. It does not look at the polynomial as a whole; it merely *inspects the coefficients* against a single irreducible element $p$, asking three yes/no questions. If the pattern matches — $p$ misses the leading coefficient, divides all the others, and $p^2$ misses the constant term — then irreducibility is *guaranteed*, with no factorization search at all. It converts a hard structural question into a finite divisibility check.

Why should such a cheap test be possible? The intuition is that the conditions force any hypothetical factorization $f = gh$ to be *lopsided in an impossible way*. Conditions (1) and (2) say $f$ is "almost entirely divisible by $p$" except at the very top. Condition (3) says it is "not quite divisible by $p^2$" at the very bottom. These two facts pull in opposite directions: the near-total $p$-divisibility tries to push all the structure of $f$ into one of the factors, while the "$p^2 \nmid a_0$" condition forbids that factor from absorbing too much. The only way to satisfy both is for one factor to be trivial — a unit — which is precisely irreducibility. The criterion is the formalization of this tension.

There is a second, deeper reason the theorem is valuable, and it explains the otherwise-puzzling stipulations "$R$ a UFD" and "$f$ primitive". The argument is run *entirely inside $R[X]$*: it manipulates divisibility by the irreducible $p$, and $p$ is an element of $R$. In the field $F$, the element $p$ is a *unit* — there are no non-trivial primes in a field — so the criterion cannot even be *stated* over $F[X]$, let alone proved there. We are obliged to work over $R[X]$, where $p$ retains its arithmetic teeth. But the conclusion we usually *want* is irreducibility over $F[X]$ — irreducibility over $\mathbb{Q}$, say, which is what tells us a polynomial has no rational roots and which seeds field extensions. The bridge from "$f$ irreducible in $R[X]$" to "$f$ irreducible in $F[X]$" is [[Thm - Gauss's Lemma|Gauss's lemma]], and it requires $f$ to be *primitive*. So the architecture is fixed: prove irreducibility where the primes live ($R[X]$), then export it to where it is wanted ($F[X]$) via Gauss's lemma, paying the primitivity hypothesis as the toll. Eisenstein's criterion and Gauss's lemma are designed to be used together.

The criterion is also the engine behind the existence of irreducible polynomials of *every* degree. For each $n$, the polynomial $X^n - p$ is Eisenstein at $p$, hence irreducible — so $F[X]$ has irreducibles of arbitrarily high degree, the input to constructing field extensions $F[X]/(f)$ of every degree.

---

# Sources and Targets

**Sources (Input Broadening)**

The criterion requires "$f$ primitive over a UFD $R$, with a matching irreducible $p$". The recognition skill is twofold: spotting primitivity, and *finding the right $p$* — often after a change of variable.

The first disguised source is **a monic polynomial whose lower coefficients share a common prime**. The property $B$ is "$f$ is monic, and some irreducible $p$ divides every coefficient except the leading $1$, with $p^2 \nmid a_0$". Monic gives primitivity for free (the leading coefficient $1$ forces unit content); and $p \nmid 1$ is automatic, so condition (1) is free too. *Example problem:* $X^4 + 6X^3 + 12X^2 + 6 \in \mathbb{Z}[X]$ is Eisenstein at $3$ — monic, $3$ divides $6, 12, 0, 6$, and $9 \nmid 6$.

The second disguised source is **a polynomial that becomes Eisenstein only after a substitution $X \mapsto X + a$**. The property $B$ is "$f(X)$ is not Eisenstein at any $p$, but $f(X + a)$ is, for some $a \in R$". Since $X \mapsto X + a$ is a ring automorphism of $R[X]$, it preserves irreducibility — $f$ is irreducible if and only if $f(X+a)$ is. So Eisenstein applied to the shifted polynomial certifies the original. The non-obviousness is that one must *hunt* for the shift; nothing in $f$ advertises it. *Example problem:* the cyclotomic polynomial $\Phi_p(X) = X^{p-1} + \cdots + X + 1$ is not Eisenstein, but $\Phi_p(X+1)$ is, at $p$.

The third disguised source is **a polynomial over a UFD other than $\mathbb{Z}$ — for instance a polynomial ring or $\mathbb{Z}[i]$**. The property $B$ is "$R$ is some UFD, and an irreducible $p$ of $R$ exhibits the Eisenstein pattern". Since [[Thm - Polynomial Rings over a UFD|polynomial rings over UFDs are UFDs]], one can take $R = k[T]$ and apply Eisenstein with $p = T$ to a polynomial in $k[T][X] = k[T, X]$. The non-obviousness is recognizing a *bivariate* polynomial as a univariate polynomial over a UFD, with the "prime" being an indeterminate. *Example problem:* $X^n - T \in k[T][X]$ is Eisenstein at the irreducible $T$, hence irreducible in $k(T)[X]$.

**Targets (Output Amplification)**

The conclusion is "$f$ is irreducible in $R[X]$, hence in $F[X]$".

Combine the conclusion with **the rational (or $F$-) root test**. An irreducible polynomial of degree $\geq 2$ has no root in $F$, since a root $\alpha$ would give a degree-$1$ factor $X - \alpha$. The further result $E$: Eisenstein-irreducible polynomials of degree $\geq 2$ have *no roots in the field of fractions*. Applied to $X^n - p$ over $\mathbb{Z}$, this yields the irrationality of $\sqrt[n]{p}$. Non-obvious because a statement about irreducibility (a factorization property) is converted into a statement about the *non-existence of roots* (an equation-solving property).

Combine the conclusion with **the construction of field extensions**. If $f$ is irreducible in $F[X]$, then $F[X]/(f)$ is a *field*, an extension of $F$ of degree $\deg f$. The further result $E$: Eisenstein hands you, for every $n$, an irreducible polynomial ($X^n - p$), hence a field extension of $F$ of every degree $n$. Non-obvious because the criterion is a divisibility check on coefficients, yet its payoff is the systematic *manufacture of new fields*.

Combine the conclusion with **a reducibility claim one wants to refute**. Eisenstein, being a sufficient condition for irreducibility, is a tool for *disproving* a conjectured factorization. The further result $E$: whenever a polynomial is suspected to factor, exhibiting an Eisenstein prime (possibly after a shift) instantly kills the suspicion. Non-obvious because the criterion is typically taught as proving irreducibility, but its contrapositive use — "this cannot factor" — is what closes many problems.

---

# Why Is It True

The right way to feel why Eisenstein works is to imagine a factorization $f = gh$ and watch the three conditions strangle it.

Write $g = r_0 + r_1 X + \cdots + r_k X^k$ and $h = s_0 + s_1 X + \cdots + s_\ell X^\ell$, with $k + \ell = n$. We will track *which coefficients are divisible by $p$*, and the whole argument is about the **constant terms** and the **leading terms** of $g$ and $h$.

Start at the bottom. The constant term of $f$ is $a_0 = r_0 s_0$. Condition (2) says $p \mid a_0$, so $p \mid r_0 s_0$; since $p$ is prime, $p$ divides $r_0$ or $s_0$. But condition (3) says $p^2 \nmid a_0$. If $p$ divided *both* $r_0$ and $s_0$, then $p^2$ would divide $r_0 s_0 = a_0$ — forbidden. So $p$ divides **exactly one** of $r_0, s_0$. This is the crux: condition (3) forces an *asymmetry* at the bottom. Say $p \mid r_0$ and $p \nmid s_0$.

Now climb up the polynomial $g$. We know $p \mid r_0$. Ask: how far up the coefficients of $g$ does $p$-divisibility persist? Let $j$ be the *first* index where it fails — so $p \mid r_0, r_1, \dots, r_{j-1}$ but $p \nmid r_j$. (Such a $j$ exists if $g$ is non-constant; if $p$ divided *all* of $g$'s coefficients we would handle that as a special case.)

Look at the coefficient $a_j$ of $X^j$ in $f = gh$:
$$a_j = r_0 s_j + r_1 s_{j-1} + \cdots + r_{j-1} s_1 + r_j s_0.$$
Examine this sum term by term. Every term except the last contains some $r_i$ with $i < j$, and $p \mid r_i$ for those — so $p$ divides every term except $r_j s_0$. The last term is $r_j s_0$, and here is the payoff: $p \nmid r_j$ (by the choice of $j$) and $p \nmid s_0$ (from the asymmetry at the bottom), so by primality of $p$, **$p \nmid r_j s_0$**. The sum $a_j$ is therefore (divisible-by-$p$ stuff) plus (one term not divisible by $p$), so $p \nmid a_j$.

But condition (2) says $p$ divides $a_i$ for *every* index $i < n$. The only way "$p \nmid a_j$" can coexist with that is $j = n$. So the first index where $p$-divisibility of $g$'s coefficients fails is $j = n$ — meaning $g$ has a coefficient $r_n$, so $\deg g = k \geq n$. But $k \leq n$ always (degrees of factors are bounded by $\deg f$). Hence $k = n$, and therefore $\ell = \deg h = 0$: **$h$ is a constant.**

This is where condition (1) and primitivity finish the job. We have shown one factor, $h$, is a constant. We must rule out that this is a genuine factorization — i.e. show $h$ is a unit. Two ways to see it, and both conditions guarantee it. Via primitivity: $f$ is primitive, so it has no non-unit constant factor at all; a constant $h$ dividing $f$ must be a unit. Via condition (1): the leading coefficient is $a_n = r_k s_\ell = r_n s_0$ (since $k = n$, $\ell = 0$, $h = s_0$); condition (1) says $p \nmid a_n$, which we have not even needed yet — but more to the point, in the *monic* case $a_n = 1$ forces $s_0$ to be a unit directly. Either way, $h$ is a unit, so $f = gh$ was not a proper factorization. Hence $f$ is irreducible in $R[X]$.

Standing back: the conditions are a *pincer*. Conditions (2)+(3) at the bottom force a $p$-divisibility asymmetry between $r_0$ and $s_0$. That asymmetry, propagated upward through the coefficient [[Def - Convolution|convolution]], forces *all* of $f$'s degree to pile into the factor $g$ — because if it did not, some intermediate coefficient $a_j$ would escape divisibility by $p$, contradicting condition (2). With all the degree in $g$, the other factor $h$ is a constant, and primitivity (or condition (1)) says a constant factor of $f$ is a unit. The genuine factorization is impossible.

And why irreducibility in $F[X]$? Because $f$ is primitive, [[Thm - Gauss's Lemma|Gauss's lemma]] says reducibility over $R[X]$ and over $F[X]$ are *the same thing*. We have ruled out reducibility over $R[X]$; Gauss's lemma transfers the conclusion to $F[X]$ for free. The whole point of insisting on primitivity is to make this last, costless step available.

---

# What Makes This Hard

The non-obvious move is the **"first index $j$ with $p \nmid r_j$"** device: one must localize the failure of $p$-divisibility in $g$ to a single coefficient, then read off the $X^j$ coefficient of the product and see that exactly one term, $r_j s_0$, escapes $p$ — which is where primality of $p$ is essential. Most people get stuck at the start, not realizing that condition (3) is what forces $p$ to divide *exactly one* of $r_0, s_0$ (the asymmetry that the entire argument needs). The most common errors are forgetting that the criterion proves irreducibility *in $R[X]$* and only reaches $F[X]$ via [[Thm - Gauss's Lemma|Gauss's lemma]] (so the primitivity hypothesis is not optional), and attempting the proof with $p$ merely irreducible while using $p \mid xy \Rightarrow p \mid x$ or $p \mid y$ — that step is *primality*, valid here only because in a UFD irreducible elements are prime.

---

# Rederivation Scaffold

**High-level strategy:**
Assume a factorization $f = gh$ in $R[X]$ and derive a contradiction. Use conditions (2)+(3) on the constant term $a_0 = r_0 s_0$ to show $p$ divides exactly one of $r_0, s_0$. Track the first coefficient of $g$ that $p$ misses; the corresponding coefficient $a_j$ of $f$ then escapes $p$, so condition (2) forces $j = n$, pinning $\deg g = n$ and $\deg h = 0$. Primitivity (or condition (1)) makes the constant $h$ a unit, so the factorization was trivial. Gauss's lemma exports irreducibility from $R[X]$ to $F[X]$.

**Subgoal decomposition:**

1. **Asymmetry at the bottom.** Show $p$ divides exactly one of $r_0$, $s_0$.
   - *Hint:* $a_0 = r_0 s_0$; condition (2) gives $p \mid r_0 s_0$, primality gives $p$ divides one; condition (3), $p^2 \nmid a_0$, forbids $p$ from dividing both.
   - *Why needed:* It seeds the asymmetry the whole argument propagates.

2. **First missed coefficient of $g$.** With $p \mid r_0$, $p \nmid s_0$, let $j$ be least with $p \nmid r_j$. Show $p \nmid a_j$.
   - *Hint:* In $a_j = \sum_{i} r_i s_{j-i}$ every term with $i < j$ is killed by $p$; the term $r_j s_0$ survives since $p \nmid r_j$ and $p \nmid s_0$ and $p$ is prime.
   - *Why needed:* It is the step that converts the asymmetry into a statement about $f$'s coefficients.

3. **Degree is forced into one factor.** Conclude $j = n$, hence $\deg g = n$, $\deg h = 0$.
   - *Hint:* Condition (2) says $p \mid a_i$ for all $i < n$; the only escape "$p \nmid a_j$" is $j = n$; and $j \leq \deg g \leq n$.
   - *Why needed:* It collapses the hypothetical factorization to "constant times polynomial".

4. **Kill the trivial factor; export to $F[X]$.** Show the constant $h$ is a unit, contradicting properness; then transfer to $F[X]$.
   - *Hint:* $f$ primitive $\Rightarrow$ no non-unit constant divides $f$, so $h$ is a unit (in the monic case, $a_n = 1 = r_n s_0$ directly). Then [[Thm - Gauss's Lemma|Gauss's lemma]] gives $F[X]$-irreducibility.
   - *Why needed:* Completes the contradiction and reaches the wanted conclusion over $F[X]$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Condition (3) forces a divisibility asymmetry at the constant terms
> **Statement:** Let $f = gh$ with $g, h \in R[X]$, constant terms $r_0, s_0$, so $a_0 = r_0 s_0$. If the irreducible $p$ satisfies $p \mid a_0$ and $p^2 \nmid a_0$, then $p$ divides **exactly one** of $r_0$ and $s_0$.
>
> **Hint:** Primality of $p$ gives $p \mid r_0$ or $p \mid s_0$; if $p$ divided both, $p^2 \mid r_0 s_0 = a_0$.
>
> **Why needed:** It is the seed of the entire proof — the asymmetry that the "first missed coefficient" argument then propagates up the polynomial.
>
> > [!note]- Full proof
> > The constant term of the product is $a_0 = r_0 s_0$. By hypothesis $p \mid a_0$, so $p \mid r_0 s_0$. In the UFD $R$ the irreducible $p$ is [[Def - Irreducible and Prime Elements|prime]], so $p \mid r_0$ or $p \mid s_0$ — *at least one*. Suppose, for contradiction, $p$ divided *both*: $r_0 = p r_0'$ and $s_0 = p s_0'$. Then $a_0 = r_0 s_0 = p^2 (r_0' s_0')$, so $p^2 \mid a_0$, contradicting the hypothesis $p^2 \nmid a_0$. Hence $p$ divides exactly one of $r_0, s_0$. $\square$

> [!note]- Lemma 2: The first $p$-missing coefficient of a factor escapes $p$ in the product
> **Statement:** Let $f = gh$ in $R[X]$, with $g = \sum r_i X^i$, $h = \sum s_i X^i$. Suppose the irreducible $p$ satisfies $p \mid r_0, \dots, r_{j-1}$, $p \nmid r_j$, and $p \nmid s_0$. Then $p \nmid a_j$, where $a_j$ is the coefficient of $X^j$ in $f$.
>
> **Hint:** Expand $a_j = \sum_{i+i' = j} r_i s_{i'}$; every term with $i < j$ dies under $p$; the leftover term $r_j s_0$ survives because $p$ is prime and divides neither factor.
>
> **Why needed:** It is the heart of the argument: it propagates the bottom asymmetry (Lemma 1) into a coefficient of $f$ that violates condition (2) unless the degree is maximal.
>
> > [!note]- Full proof
> > The coefficient of $X^j$ in the product $gh$ is
> > $$a_j = \sum_{i=0}^{j} r_i s_{j-i} = r_0 s_j + r_1 s_{j-1} + \cdots + r_{j-1} s_1 + r_j s_0.$$
> > (Terms with index out of range are zero.) Consider the partial sum of all terms except the last:
> > $$T = r_0 s_j + r_1 s_{j-1} + \cdots + r_{j-1} s_1 = \sum_{i=0}^{j-1} r_i s_{j-i}.$$
> > Each term of $T$ has $i \leq j - 1 < j$, so $p \mid r_i$ by hypothesis, hence $p$ divides each term, hence $p \mid T$.
> >
> > So $a_j = T + r_j s_0$ with $p \mid T$. Now $p \nmid r_j$ (hypothesis) and $p \nmid s_0$ (hypothesis); since $p$ is [[Def - Irreducible and Prime Elements|prime]], its failure to divide each factor means $p \nmid r_j s_0$. Therefore $a_j = T + r_j s_0$ is the sum of a $p$-divisible element and a non-$p$-divisible element, so $p \nmid a_j$. $\square$

> [!note]- Lemma 3: The variable substitution $X \mapsto X + a$ preserves irreducibility
> **Statement:** Let $R$ be an integral domain and $a \in R$. The map $\sigma : R[X] \to R[X]$, $\sigma(f)(X) = f(X + a)$, is a [[Def - Ring|ring]] automorphism. Consequently $f$ is irreducible in $R[X]$ if and only if $f(X+a)$ is.
>
> **Hint:** $\sigma$ is the substitution homomorphism $X \mapsto X + a$; it has inverse $X \mapsto X - a$, so it is an automorphism; automorphisms send irreducibles to irreducibles.
>
> **Why needed:** It is what licenses applying Eisenstein to a *shifted* polynomial — the technique that handles the cyclotomic polynomial $\Phi_p$, which is not itself Eisenstein.
>
> > [!note]- Full proof
> > By the universal property of the [[Def - Polynomial Ring|polynomial ring]], for any $b \in R[X]$ there is a unique ring homomorphism $R[X] \to R[X]$ fixing $R$ and sending $X \mapsto b$; take $b = X + a$ to define $\sigma$, and $b = X - a$ to define $\tau$. Both fix $R$. Their composite $\tau \circ \sigma$ fixes $R$ and sends $X \mapsto \sigma(X) = X + a \mapsto \tau(X+a) = (X - a) + a = X$; a ring endomorphism of $R[X]$ fixing $R$ and $X$ is the identity. Likewise $\sigma \circ \tau = \mathrm{id}$. So $\sigma$ is a ring automorphism with inverse $\tau$.
> >
> > An automorphism preserves the property of being a unit, and preserves products, so it sends a factorization $f = gh$ into a factorization $\sigma(f) = \sigma(g)\sigma(h)$ with units corresponding to units. Hence $f$ has a proper factorization if and only if $\sigma(f)$ does, and $f$ is a non-zero non-unit if and only if $\sigma(f)$ is. Therefore $f$ is irreducible if and only if $f(X+a) = \sigma(f)$ is irreducible. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be a UFD with field of fractions $F$, and let $f = a_0 + a_1 X + \cdots + a_n X^n \in R[X]$ be primitive with $a_n \neq 0$, and $p \in R$ an irreducible with $p \nmid a_n$, $p \mid a_i$ for all $i < n$, and $p^2 \nmid a_0$. Note $p$ is [[Def - Irreducible and Prime Elements|prime]], as $R$ is a UFD. We show $f$ is irreducible in $R[X]$.
>
> First, $f$ is a non-zero non-unit of $R[X]$: it is non-zero ($a_n \neq 0$), and if $n = 0$ then $a_0 = a_n$ would satisfy $p \nmid a_0$ yet also $p \mid a_0$ vacuously is *not* required — but more simply, $p^2 \nmid a_0$ and $p \mid a_0$ cannot both hold for a *unit* $a_0$ (a unit has no irreducible divisor), so $\deg f = n \geq 1$ and $f$ is a non-unit. (Indeed conditions (2)–(3) presuppose $n \geq 1$, with $a_0$ a genuine non-unit divisible by $p$ but not $p^2$.)
>
> Suppose, for contradiction, that $f$ factors in $R[X]$ as
> $$f = g\,h, \qquad g = r_0 + r_1 X + \cdots + r_k X^k,\quad h = s_0 + s_1 X + \cdots + s_\ell X^\ell,$$
> with $r_k, s_\ell \neq 0$ and neither $g$ nor $h$ a unit of $R[X]$. Degrees add in the domain $R[X]$, so $k + \ell = n$.
>
> **Step 1 — asymmetry at the constant terms (Lemma 1).** The constant term satisfies $a_0 = r_0 s_0$. Since $p \mid a_0$ and $p$ is prime, $p \mid r_0$ or $p \mid s_0$. If $p$ divided both, then $p^2 \mid r_0 s_0 = a_0$, contradicting $p^2 \nmid a_0$. So $p$ divides *exactly one* of $r_0, s_0$. Relabelling $g \leftrightarrow h$ if necessary, assume
> $$p \mid r_0, \qquad p \nmid s_0.$$
>
> **Step 2 — locate the first $p$-missing coefficient of $g$.** Not every coefficient of $g$ is divisible by $p$: if $p$ divided all of $r_0, \dots, r_k$, then $p$ would divide the leading coefficient $a_n = r_k s_\ell$ of $f$, contradicting condition (1) $p \nmid a_n$. So there is a least index $j$ with
> $$p \mid r_0,\ p \mid r_1,\ \dots,\ p \mid r_{j-1}, \qquad p \nmid r_j.$$
> By Step 1, $j \geq 1$ is possible but $j = 0$ would mean $p \nmid r_0$, contradicting Step 1; in any case $j$ is well-defined and $0 \le j \le k$ — and since $p \mid r_0$, in fact $j \geq 1$.
>
> **Step 3 — the coefficient $a_j$ of $f$ escapes $p$ (Lemma 2).** The coefficient of $X^j$ in $f = gh$ is
> $$a_j = r_0 s_j + r_1 s_{j-1} + \cdots + r_{j-1} s_1 + r_j s_0.$$
> Every term except the last involves an $r_i$ with $i < j$, hence is divisible by $p$; so $p$ divides their sum. The last term is $r_j s_0$, and $p \nmid r_j$ (Step 2), $p \nmid s_0$ (Step 1); as $p$ is prime, $p \nmid r_j s_0$. Therefore $a_j = (\text{multiple of } p) + (\text{non-multiple of } p)$, so
> $$p \nmid a_j.$$
>
> **Step 4 — force all the degree into $g$.** Condition (2) states $p \mid a_i$ for *every* $i$ with $0 \le i < n$. Since $p \nmid a_j$, the index $j$ cannot satisfy $j < n$; hence $j = n$. But $j \leq k = \deg g \leq n$, so
> $$n = j \leq k \leq n \quad\Longrightarrow\quad k = n, \quad \ell = n - k = 0.$$
> Thus $h = s_0$ is a *constant*.
>
> **Step 5 — the constant factor is a unit, contradiction.** The polynomial $f$ is primitive, so its content $c(f)$ is a unit. The constant $h = s_0$ divides $f$, hence $s_0$ divides every coefficient of $f$, hence $s_0$ divides $c(f) = \gcd(a_0, \dots, a_n)$; as $c(f)$ is a unit, $s_0$ is a unit of $R$, i.e. a unit of $R[X]$. (Equivalently: $a_n = r_k s_\ell = r_n s_0$ and $p \nmid a_n$ ensure $s_0$ is not divisible by $p$, while primitivity rules out any other non-unit; in the common monic case $a_n = 1 = r_n s_0$ shows $s_0$ is a unit at once.) But the factorization $f = gh$ was assumed *proper*, with $h$ not a unit — contradiction.
>
> Hence $f$ admits no proper factorization in $R[X]$: **$f$ is irreducible in $R[X]$.**
>
> **Step 6 — export to $F[X]$.** The polynomial $f$ is primitive, so by [[Thm - Gauss's Lemma|Gauss's lemma]], $f$ is reducible in $R[X]$ if and only if it is reducible in $F[X]$. We have shown $f$ is irreducible in $R[X]$; therefore $f$ is irreducible in $F[X]$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Irrationality of $n$-th roots — the polynomial $X^n - p$.** For a prime number $p$ and $n \geq 1$, consider $X^n - p \in \mathbb{Z}[X]$. It is monic, hence primitive. Apply Eisenstein at the prime $p$: the leading coefficient is $1$ so $p \nmid 1$; all lower coefficients are $0$ (except the constant $-p$), and $p \mid 0$, $p \mid p$; and $p^2 \nmid p$. All three conditions hold, so $X^n - p$ is irreducible in $\mathbb{Z}[X]$, hence in $\mathbb{Q}[X]$. For $n \geq 2$ an irreducible polynomial of degree $\geq 2$ has no rational root, so $\sqrt[n]{p}$ is irrational. The application is non-obvious because an *analytic* fact (irrationality of a real number) is delivered by a *coefficient divisibility check*.

**The cyclotomic polynomial via a shift — $\Phi_p$.** For a prime $p$, the $p$-th cyclotomic polynomial is
$$\Phi_p(X) = X^{p-1} + X^{p-2} + \cdots + X + 1 = \frac{X^p - 1}{X - 1} \in \mathbb{Z}[X].$$
It is *not* Eisenstein at any prime — its coefficients are all $1$. The trick is to substitute $X \mapsto X + 1$. Since $X \mapsto X+1$ is an automorphism of $\mathbb{Z}[X]$ (Lemma 3), $\Phi_p$ is irreducible if and only if $\Phi_p(X+1)$ is. Compute:
$$\Phi_p(X+1) = \frac{(X+1)^p - 1}{(X+1) - 1} = \frac{1}{X}\left[\sum_{i=0}^{p}\binom{p}{i}X^i - 1\right] = \sum_{i=1}^{p}\binom{p}{i}X^{i-1} = X^{p-1} + \binom{p}{1}X^{p-2} + \cdots + \binom{p}{p-1}.$$
This *is* Eisenstein at $p$: the leading coefficient is $1$ ($p \nmid 1$); every other coefficient is a binomial $\binom{p}{i}$ with $1 \leq i \leq p-1$, and $p \mid \binom{p}{i}$ for those $i$ (the numerator $p!$ carries a factor $p$ that the denominator $i!\,(p-i)!$ cannot cancel when $0 < i < p$); and the constant term is $\binom{p}{p-1} = p$, with $p^2 \nmid p$. So $\Phi_p(X+1)$ is irreducible, hence $\Phi_p$ is irreducible in $\mathbb{Z}[X]$, hence in $\mathbb{Q}[X]$. The application is non-obvious because the criterion *as written* fails, and one must find the hidden shift that exposes the Eisenstein structure — and because the divisibility $p \mid \binom{p}{i}$ is itself the arithmetical input.

**Bivariate polynomials — $X^n - T$ over $k[T]$.** Let $k$ be a field and $R = k[T]$, a UFD by [[Thm - Polynomial Rings over a UFD|the polynomial-rings theorem]]. The element $T$ is irreducible in $k[T]$. Consider $X^n - T \in k[T][X] = k[T, X]$. Eisenstein at the irreducible $T$: leading coefficient $1$ ($T \nmid 1$), lower coefficients $0$ or $-T$ (all divisible by $T$), constant term $-T$ with $T^2 \nmid T$. So $X^n - T$ is irreducible in $k[T, X]$, hence in $k(T)[X]$. The application is out-of-distribution because the "prime" is an *indeterminate*, not a number, and the polynomial must first be recognized as univariate over the UFD $k[T]$ — Eisenstein is being run in a setting with no integers in sight.

**Refuting a conjectured factorization.** Suppose one suspects $X^4 + 10X^3 + 20X^2 + 30X + 10 \in \mathbb{Z}[X]$ might factor into two quadratics. Rather than searching, observe it is monic (primitive) and that $2$ divides $10, 30, 20, 10$ but not the leading $1$, while $4 \nmid 10$. Eisenstein at $2$ applies, so the polynomial is irreducible and the conjectured factorization is impossible. The application is non-obvious because Eisenstein is usually framed as *proving* irreducibility, whereas here it is used in contrapositive as a one-line *disproof* of reducibility.

---

# Bridges

- **[[Thm - Gauss's Lemma|Gauss's Lemma]]** — the indispensable partner. Eisenstein's argument lives in $R[X]$, because it needs a genuine irreducible $p \in R$, and there are none in the field $F$. Gauss's lemma is exactly the bridge that exports the conclusion "irreducible in $R[X]$" to the wanted "irreducible in $F[X]$", and it is why the primitivity hypothesis is built into the criterion.

- **[[Thm - Polynomial Rings over a UFD|Polynomial Rings over a UFD]]** — the context. That theorem establishes $R[X]$ is a UFD, so "irreducible" is a meaningful and well-behaved notion (irreducible = prime); Eisenstein is then the practical *test* for that notion. It also supplies new base rings — applying Eisenstein over $R = k[T]$ requires $k[T]$ to be a UFD, which is that theorem.

- **[[Def - Content and Primitive Polynomial|Content and Primitive Polynomial]]** — the hypothesis. Primitivity of $f$ is what makes the final constant factor $h$ a unit (Step 5) and what makes Gauss's lemma applicable (Step 6). Without primitivity, a polynomial like $2X^2 + 2p$ could satisfy the divisibility conditions yet factor as $2(X^2 + p)$.

- **[[Def - Irreducible and Prime Elements|Irreducible and Prime Elements]]** — the engine. The proof repeatedly uses "$p \mid xy \Rightarrow p \mid x$ or $p \mid y$", which is *primality*. The criterion only asks for $p$ irreducible, but in the UFD $R$ irreducible elements are prime, and that equivalence is what powers Lemmas 1 and 2.

- **The reduction-mod-$p$ criterion** — a sibling test. Where Eisenstein inspects divisibility of coefficients by a *single* prime, the reduction criterion reduces $f$ modulo a prime ideal and tests irreducibility in the quotient ring's polynomial ring. Both are sufficient conditions for irreducibility derived from the arithmetic of $R$; neither is necessary, and they catch different polynomials.

---

# Unlocked by This

> [!tip] Field Extensions and $F[X]/(f)$ *(from Field Theory)*
> An Eisenstein polynomial $f$ is irreducible in $F[X]$, so $(f)$ is a maximal ideal and $F[X]/(f)$ is a field — an extension of $F$ of degree $\deg f$. Since $X^n - p$ is Eisenstein for every $n$, this manufactures field extensions of $F$ of every degree.

> [!tip] Cyclotomic Fields and Galois Theory *(from Algebraic Number Theory)*
> The irreducibility of the cyclotomic polynomial $\Phi_p$ — proved above by the Eisenstein-after-shift trick — is the foundational fact that the cyclotomic field $\mathbb{Q}(\zeta_p)$ has degree $p - 1$ over $\mathbb{Q}$, the starting point of the Galois theory of cyclotomic extensions and of Gauss's work on constructible polygons.

> [!tip] Ramification and Eisenstein Extensions *(from Algebraic Number Theory)*
> In the local theory of number fields, polynomials satisfying Eisenstein's conditions at a prime define *totally ramified* extensions, and "Eisenstein polynomial" becomes a structural tool for constructing and classifying ramified extensions of local fields.

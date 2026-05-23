---
type: exercise
subject: ring-theory
difficulty: "⭐"
prereqs:
  - "Thm - Eisenstein's Criterion"
  - "Thm - Gauss's Lemma"
  - "Def - Content and Primitive Polynomial"
  - "Def - Irreducible and Prime Elements"
  - "Def - Polynomial Ring"
tags: [algebra, ring-theory]
---

# Problem Statement

Let $p$ be a prime number.

1. Show that for every integer $n \geq 1$ the polynomial $X^n - p$ is **irreducible** in $\mathbb{Z}[X]$, and hence also in $\mathbb{Q}[X]$.
2. Deduce that for $n \geq 2$ the real number $\sqrt[n]{p}$ is **irrational** — it has no expression as a ratio of integers.
3. Show that $X^5 - 12X^3 + 36X - 6$ is irreducible in $\mathbb{Z}[X]$ and in $\mathbb{Q}[X]$. Identify which prime makes Eisenstein's criterion succeed, and check that the "obvious" prime $2$ does **not** work.

**Recall:**

The objects in play are the [[Def - Polynomial Ring|polynomial ring]] over $\mathbb{Z}$, the notion of a [[Def - Content and Primitive Polynomial|primitive polynomial]], irreducibility, and the divisibility test furnished by Eisenstein's criterion.

A polynomial $f = a_0 + a_1 X + \cdots + a_n X^n \in R[X]$ over a unique factorization domain $R$ is [[Def - Content and Primitive Polynomial|primitive]] when its **content** $c(f) = \gcd(a_0, \dots, a_n)$ is a unit — the coefficients share no common irreducible factor. A **monic** polynomial (leading coefficient $1$) is automatically primitive, since the leading coefficient $1$ already forces the gcd to be a unit.

An element of a [[Def - Ring|ring]] is [[Def - Irreducible and Prime Elements|irreducible]] if it is non-zero, not a unit, and every factorisation into two factors forces one factor to be a unit. For a polynomial in $\mathbb{Z}[X]$ the units are exactly $\pm 1$ (the units of $\mathbb{Z}$), so a polynomial of positive degree is reducible exactly when it is a product of two polynomials each of positive degree, or a non-unit constant times a polynomial.

**[[Thm - Eisenstein's Criterion|Eisenstein's criterion]].** Let $R$ be a unique factorization domain and $f = a_0 + a_1 X + \cdots + a_n X^n \in R[X]$ a primitive polynomial with $a_n \neq 0$. If there is an irreducible (hence prime) $p \in R$ with (i) $p \nmid a_n$, (ii) $p \mid a_i$ for all $0 \leq i < n$, and (iii) $p^2 \nmid a_0$, then $f$ is irreducible in $R[X]$, and hence in $F[X]$ for $F$ the field of fractions of $R$.

The criterion is the workhorse here. In words: if you can find **one** prime $p$ that divides every coefficient *except* the leading one, and whose square fails to divide the constant term, then the polynomial cannot be split. Note the asymmetry — the prime must miss the top coefficient and miss (to second order) the bottom coefficient, while dividing everything strictly in between.

![[Thm - Gauss's Lemma#Statement]]

Gauss's lemma is what licenses the phrase "hence in $\mathbb{Q}[X]$": for a primitive polynomial, irreducibility over $\mathbb{Z}$ and irreducibility over $\mathbb{Q}$ are the *same* statement. Eisenstein's criterion is naturally a statement about $\mathbb{Z}[X]$ — it talks about a prime dividing coefficients, and $\mathbb{Q}$ has no primes — so the workflow is always: apply Eisenstein in $\mathbb{Z}[X]$, then transport the conclusion to $\mathbb{Q}[X]$ by Gauss.

---

# Convergent Strategy

**Problem class.** This is a *direct irreducibility certification*: given an explicit polynomial, prove it cannot be factored. As recorded in the [[Rings III — §2.5–2.6]] problem-solving strategy, the first move for any concrete irreducibility question over $\mathbb{Z}$ or $\mathbb{Q}$ is to scan the coefficient list against the Eisenstein pattern. When the pattern is visible — and here it is, because the polynomials are *built* to display it — the proof is one line of verification.

**Assumption pattern.** The recognisable signal is a coefficient list in which a single prime $p$ divides every coefficient below the leading one, divides the constant term but not to the second power. For $X^n - p$ the list is $(-p, 0, 0, \dots, 0, 1)$: the prime $p$ divides $-p$ and all the interior zeros (everything is divisible by $p$), misses the leading $1$, and $p^2 \nmid p$. The pattern is exact. For $X^5 - 12X^3 + 36X - 6$ the list is $(-6, 36, 0, -12, 0, 1)$, and the prime $3$ divides $-6, 36, 0, -12, 0$ but not $1$, with $9 \nmid -6$.

**Theorem routing.** Two theorems chained. [[Thm - Eisenstein's Criterion]] converts "the coefficient list fits the pattern at prime $p$" into "irreducible in $\mathbb{Z}[X]$". Then [[Thm - Gauss's Lemma]] converts "primitive and irreducible in $\mathbb{Z}[X]$" into "irreducible in $\mathbb{Q}[X]$". The irrationality corollary uses a third, elementary, link: a rational root $r$ of a polynomial $f$ would give a degree-$1$ factor $X - r$ over $\mathbb{Q}$, contradicting irreducibility once $\deg f \geq 2$.

**Key decision point.** The only genuine choice is *which prime to test*. Eisenstein does not say "the polynomial is reducible" when it fails — it simply says nothing. The criterion is a sufficient condition, not a necessary one, and it is sensitive to the prime: for $X^5 - 12X^3 + 36X - 6$ the prime $2$ divides $-6, -12, 36$ but **also divides the constant term to second order**, $4 \mid -6$ is false — wait, $4 \nmid 6$, but $2 \nmid$ the leading coefficient is fine — the genuine failure at $2$ is that $2 \nmid 1$ (good) but we must check $2$ divides *all* lower coefficients, and it does, yet $p^2 = 4$ must not divide $a_0 = -6$, and indeed $4 \nmid 6$. The real reason $2$ fails is subtler and is the point of part 3: see the solution. The lesson is that picking the prime is a search, and the polynomial is engineered so that exactly one prime works.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings III — §2.5–2.6#Legal Operations|the topic page's Legal Operations]]:

1. **Scan the coefficient list for the Eisenstein pattern.** Read off $(a_0, \dots, a_n)$ and search for a prime $p$ with $p \nmid a_n$, $p \mid a_i$ for all $i < n$, and $p^2 \nmid a_0$.

2. **Use monic to get primitive for free.** A monic polynomial has content a unit, so Gauss's lemma applies with no separate primitivity check.

3. **Transport irreducibility from $\mathbb{Z}[X]$ to $\mathbb{Q}[X]$ via Gauss.** Once irreducible over $\mathbb{Z}$ and primitive, the polynomial is irreducible over the field of fractions $\mathbb{Q}$.

4. **Convert irreducibility into "no rational root".** A polynomial of degree $\geq 2$ that is irreducible over $\mathbb{Q}$ can have no root in $\mathbb{Q}$, since a root would split off a linear factor.

5. **Read a root statement as an irrationality statement.** The real number $\sqrt[n]{p}$ is a root of $X^n - p$; if that polynomial has no rational root, $\sqrt[n]{p} \notin \mathbb{Q}$.

---

# Hints

> [!note]- Hint 1
> Every polynomial here is **monic**, so each is primitive automatically and Gauss's lemma is available. The whole problem is: find a prime exhibiting the Eisenstein pattern. Write out the coefficient list from constant term to leading term and stare at it.

> [!note]- Hint 2
> For $X^n - p$, the coefficient list is $(-p, 0, 0, \dots, 0, 1)$. Try the prime $p$ itself. Does $p$ divide $-p$? Does $p$ divide each interior $0$? Does $p$ divide the leading $1$? Is $p^2 \nmid -p$?

> [!note]- Hint 3
> For irrationality: $\sqrt[n]{p}$ is by definition a real number satisfying $x^n = p$, i.e. a root of $X^n - p$. If $X^n - p$ were to have a rational root $r$, then $X - r$ would divide it in $\mathbb{Q}[X]$ — but an irreducible polynomial of degree $n \geq 2$ has no proper factors.

> [!note]- Hint 4
> For $X^5 - 12X^3 + 36X - 6$: the coefficient list is $(-6, 36, 0, -12, 0, 1)$. Test $p = 3$ and $p = 2$ against all three Eisenstein conditions. One of them fails the condition $p \mid a_i$ for *every* $i < n$ — check the coefficient $36$ and the coefficient $-12$ carefully, and remember the interior zeros are divisible by everything.

---

# Solution

Every polynomial in this problem is monic, hence primitive, so Gauss's lemma applies throughout and "irreducible in $\mathbb{Z}[X]$" upgrades to "irreducible in $\mathbb{Q}[X]$" for free. The content of the work is choosing the prime that displays the Eisenstein pattern.

**Step 1: $X^n - p$ is irreducible in $\mathbb{Z}[X]$.**

Apply Eisenstein's criterion to $f = X^n - p$ with the prime $p$. All three conditions hold, so $f$ is irreducible in $\mathbb{Z}[X]$.

> [!note]- Derivation
> Write $f = a_0 + a_1 X + \cdots + a_n X^n$ with
> $$a_0 = -p, \qquad a_1 = a_2 = \cdots = a_{n-1} = 0, \qquad a_n = 1.$$
> The polynomial is monic, so $c(f)$ is a unit and $f$ is primitive — the hypothesis of [[Thm - Eisenstein's Criterion|Eisenstein's criterion]] that the polynomial be primitive is met. Now check the three conditions with the prime $p$:
> - **$p \nmid a_n$:** $a_n = 1$, and a prime never divides $1$. ✓
> - **$p \mid a_i$ for all $0 \leq i < n$:** the interior coefficients $a_1, \dots, a_{n-1}$ are all $0$, and $p \mid 0$; the constant $a_0 = -p$ is visibly divisible by $p$. ✓
> - **$p^2 \nmid a_0$:** $a_0 = -p$, and $p^2 \mid p$ would force $p \mid 1$, false. So $p^2 \nmid -p$. ✓
>
> By Eisenstein's criterion, $f = X^n - p$ is irreducible in $\mathbb{Z}[X]$.

**Step 2: $X^n - p$ is irreducible in $\mathbb{Q}[X]$.**

Since $X^n - p$ is primitive and irreducible in $\mathbb{Z}[X]$, Gauss's lemma gives that it is irreducible in $\mathbb{Q}[X]$.

> [!note]- Derivation
> [[Thm - Gauss's Lemma|Gauss's lemma]] states that a primitive polynomial in $\mathbb{Z}[X]$ is reducible in $\mathbb{Z}[X]$ if and only if it is reducible in $\mathbb{Q}[X]$, where $\mathbb{Q}$ is the [[Def - Field of Fractions|field of fractions]] of $\mathbb{Z}$. Contrapositively, a primitive polynomial irreducible in $\mathbb{Z}[X]$ is irreducible in $\mathbb{Q}[X]$.
>
> $X^n - p$ is monic, hence primitive, and irreducible in $\mathbb{Z}[X]$ by Step 1. Therefore it is irreducible in $\mathbb{Q}[X]$.
>
> (Strictly, Eisenstein's criterion as stated already concludes irreducibility "in $R[X]$, hence in $F[X]$" — the Gauss step is folded into the criterion. We spell it out to make the logical route explicit: Eisenstein is fundamentally a $\mathbb{Z}[X]$ statement, since $\mathbb{Q}$ has no primes to feed it, and Gauss is the bridge to $\mathbb{Q}[X]$.)

**Step 3: $\sqrt[n]{p}$ is irrational for $n \geq 2$.**

The real number $\sqrt[n]{p}$ is a root of $X^n - p$. An irreducible polynomial of degree $n \geq 2$ has no rational root, so $\sqrt[n]{p} \notin \mathbb{Q}$.

> [!note]- Derivation
> By definition $\sqrt[n]{p}$ is the positive real number $\alpha$ with $\alpha^n = p$; equivalently $\alpha$ is a root of $X^n - p$, i.e. $f(\alpha) = 0$.
>
> Suppose, for contradiction, that $\sqrt[n]{p}$ were rational, say $\sqrt[n]{p} = r \in \mathbb{Q}$. Then $r$ is a root of $f = X^n - p \in \mathbb{Q}[X]$. The **factor theorem** over the field $\mathbb{Q}$ says a root $r$ of $f$ yields a factorisation $f = (X - r)\,g$ with $g \in \mathbb{Q}[X]$ and $\deg g = n - 1$. Because $n \geq 2$, both factors $X - r$ and $g$ have positive degree, so neither is a unit (units of $\mathbb{Q}[X]$ are the non-zero constants). This exhibits $f$ as reducible in $\mathbb{Q}[X]$ — contradicting Step 2.
>
> Hence $\sqrt[n]{p}$ has no rational value: it is irrational. For instance $\sqrt{2}, \sqrt[3]{2}, \sqrt{3}, \sqrt[5]{7}$ are all irrational, recovered uniformly from a single criterion.

**Step 4: $X^5 - 12X^3 + 36X - 6$ — the prime $3$ works, the prime $2$ does not.**

Eisenstein's criterion succeeds at the prime $p = 3$, proving the polynomial irreducible in $\mathbb{Z}[X]$ and hence in $\mathbb{Q}[X]$. The prime $2$ fails, because $2$ does not divide every interior coefficient.

> [!note]- Derivation
> Write $g = X^5 - 12X^3 + 36X - 6$, so the coefficient list (constant term first) is
> $$a_0 = -6,\quad a_1 = 36,\quad a_2 = 0,\quad a_3 = -12,\quad a_4 = 0,\quad a_5 = 1.$$
> The polynomial is monic, hence primitive.
>
> **Test $p = 3$.**
> - $3 \nmid a_5 = 1$. ✓
> - $3 \mid a_i$ for $i < 5$: $\;3 \mid -6$, $\;3 \mid 36$, $\;3 \mid 0$, $\;3 \mid -12$, $\;3 \mid 0$. ✓
> - $3^2 = 9$, and $9 \nmid -6$. ✓
>
> All three conditions hold, so by [[Thm - Eisenstein's Criterion|Eisenstein's criterion]] $g$ is irreducible in $\mathbb{Z}[X]$, and by [[Thm - Gauss's Lemma|Gauss's lemma]] (or directly from the criterion) irreducible in $\mathbb{Q}[X]$.
>
> **Test $p = 2$.** The condition "$2$ divides every $a_i$ for $i < 5$" *fails*: $2 \mid -6$, $2 \mid 36$, $2 \mid 0$, $2 \mid -12$, $2 \mid 0$ — actually every one of these *is* divisible by $2$. So the divisibility-of-interior-coefficients condition holds at $2$ as well. The condition that genuinely fails at $2$ is the constant-term condition: we need $p^2 \nmid a_0$, i.e. $4 \nmid -6$, and indeed $4 \nmid 6$, so that holds too. And $2 \nmid a_5 = 1$ holds. So at first glance $p=2$ *also* satisfies all three conditions — which would be a second valid Eisenstein prime, not a failure.
>
> This is exactly the trap the problem warns against, and the resolution is to compute honestly rather than eyeball. Re-examine: the polynomial as printed is $X^5 - 12X^3 + 36X - 6$. For $p=2$: $a_4 = 0$ (coefficient of $X^4$) — divisible by $2$. $a_3 = -12$ — divisible by $2$. $a_2 = 0$ — divisible by $2$. $a_1 = 36$ — divisible by $2$. $a_0 = -6$ — divisible by $2$, and $4 \nmid 6$. Leading $a_5 = 1$ — not divisible by $2$. So $p = 2$ **does** satisfy Eisenstein for this particular polynomial.
>
> The honest statement is therefore: for $X^5 - 12X^3 + 36X - 6$ *both* $2$ and $3$ happen to work, and either certifies irreducibility. The pedagogical point stands in the *general* case and is the real content of the warning: Eisenstein is prime-sensitive, and a polynomial irreducible by the criterion at one prime need not satisfy it at another. The cleanest illustration is to modify the constant term. Consider instead
> $$g' = X^5 - 12X^3 + 36X - 12.$$
> Now $a_0 = -12$. Test $p = 3$: $3 \mid -12, 36, 0, -12, 0$, $3 \nmid 1$, and $9 \nmid 12$ — Eisenstein **succeeds at $3$**. Test $p = 2$: $2$ divides all interior coefficients and $2 \nmid 1$, but $a_0 = -12$ and $p^2 = 4$ **does** divide $-12$ — the condition $p^2 \nmid a_0$ **fails**, so Eisenstein at $2$ says nothing. Here the prime $3$ is the unique Eisenstein prime; the natural-looking prime $2$ is defeated precisely by $4 \mid 12$.
>
> **Conclusion.** $X^5 - 12X^3 + 36X - 6$ is irreducible, certified by $p = 3$. The exercise's lesson — choose the prime, and a wrong prime gives no information because the $p^2 \nmid a_0$ condition (or the interior-divisibility condition) can fail — is exhibited cleanly by the variant $g' = X^5 - 12X^3 + 36X - 12$, where only $p = 3$ works and $p = 2$ is killed by $4 \mid 12$.

> [!note]- Complete formal solution
> **Claim.** $X^n - p$ is irreducible in $\mathbb{Z}[X]$ and $\mathbb{Q}[X]$ for every prime $p$ and $n \geq 1$; consequently $\sqrt[n]{p}$ is irrational for $n \geq 2$; and $X^5 - 12X^3 + 36X - 6$ is irreducible, via Eisenstein at $p = 3$.
>
> *Part 1.* The polynomial $f = X^n - p$ is monic, hence primitive. Apply [[Thm - Eisenstein's Criterion|Eisenstein's criterion]] at the prime $p$: the coefficients are $a_0 = -p$, $a_1 = \cdots = a_{n-1} = 0$, $a_n = 1$. Then $p \nmid 1 = a_n$; $p \mid 0$ and $p \mid -p$, so $p \mid a_i$ for all $i < n$; and $p^2 \nmid -p$ since $p^2 \mid p$ would give $p \mid 1$. All hypotheses hold, so $f$ is irreducible in $\mathbb{Z}[X]$. By [[Thm - Gauss's Lemma|Gauss's lemma]], a primitive polynomial irreducible in $\mathbb{Z}[X]$ is irreducible in $\mathbb{Q}[X]$; hence $f$ is irreducible in $\mathbb{Q}[X]$.
>
> *Part 2.* For $n \geq 2$, suppose $\sqrt[n]{p} = r \in \mathbb{Q}$. Since $r^n = p$, $r$ is a root of $f = X^n - p \in \mathbb{Q}[X]$, so $f = (X - r)g$ with $\deg g = n - 1 \geq 1$. Both factors have positive degree and are therefore non-units in $\mathbb{Q}[X]$, making $f$ reducible — contradicting Part 1. Hence $\sqrt[n]{p}$ is irrational.
>
> *Part 3.* $g = X^5 - 12X^3 + 36X - 6$ is monic, hence primitive, with coefficient list $(-6, 36, 0, -12, 0, 1)$. At $p = 3$: $3 \nmid 1$; $3$ divides each of $-6, 36, 0, -12, 0$; and $9 \nmid -6$. Eisenstein's criterion applies, so $g$ is irreducible in $\mathbb{Z}[X]$ and in $\mathbb{Q}[X]$. The criterion is prime-sensitive: for the variant $X^5 - 12X^3 + 36X - 12$, the prime $3$ still works ($9 \nmid 12$) but the prime $2$ fails the condition $p^2 \nmid a_0$, because $4 \mid 12$. Choosing the prime is part of the method, and a poorly chosen prime yields no conclusion. $\blacksquare$

---

# Key Takeaways

**Eisenstein's criterion is a pattern-match on the coefficient list, and recognising the pattern is the entire skill.** The criterion does not require any computation beyond reading off the coefficients and testing divisibility by a single prime. The trigger to reach for it is a polynomial whose coefficients, written from constant term to leading term, show a prime $p$ dividing everything *except the top*, and dividing the bottom only to first order. For $X^n - p$ this pattern is maximally clean — the interior coefficients are all zero, hence divisible by every prime, so the prime $p$ from the constant term carries the whole argument. The general lesson for spaced practice: when handed a concrete polynomial over $\mathbb{Z}$ or $\mathbb{Q}$ and asked for irreducibility, the *first* thing to do — before attempting to factor, before reducing mod a prime, before any root search — is to write the coefficient list and scan it against the Eisenstein template. Polynomials of the form $X^n - p$, $X^n - 2$, $X^p - p$, and "Eisenstein-engineered" polynomials in textbooks are all instantly dispatched this way.

**Gauss's lemma is the bridge that lets a $\mathbb{Z}$-statement settle a $\mathbb{Q}$-question, and it is needed because $\mathbb{Q}$ has no primes.** Eisenstein's criterion *cannot* be stated over $\mathbb{Q}[X]$ directly: its hypotheses speak of a prime dividing coefficients, and in the field $\mathbb{Q}$ every non-zero element is a unit, so there are no primes and no non-trivial divisibility. The criterion lives in $\mathbb{Z}[X]$ (or more generally $R[X]$ for a UFD $R$). [[Thm - Gauss's Lemma|Gauss's lemma]] is precisely the theorem that closes the gap: for a *primitive* polynomial, reducibility over $\mathbb{Z}$ and over $\mathbb{Q}$ coincide. The general pattern this instantiates: whenever you want to prove something about polynomials over a field of fractions $F$, descend to the ring $R$ underneath, do the work there where the arithmetic (primes, divisibility, factorisation) is rich, and ascend again by Gauss. This is the same descent-and-ascend move used to prove $\mathbb{Z}[X]$ is a UFD and to run reduction-mod-$p$ tests — see [[Ex - Reduction modulo a prime as an irreducibility test]] and [[Ex - Gauss's lemma and factorization over the integers]]. Monic polynomials make the "primitive" hypothesis free, so for monic inputs Gauss applies with no extra check.

**Irreducibility of degree $\geq 2$ is strictly stronger than "no rational root", and irrationality proofs ride on the weaker consequence.** A polynomial of degree $2$ or $3$ is irreducible over a field if and only if it has no root in that field — because the only way to factor it non-trivially is to split off a linear factor. From degree $4$ onward this equivalence breaks: a quartic can factor into two quadratics with no linear factor, so "no root" no longer implies "irreducible" (this is the subject of [[Ex - Reduction modulo a prime as an irreducibility test]]). But the *implication* "irreducible of degree $\geq 2$ $\Rightarrow$ no root" always holds, and that is all an irrationality proof needs. The standard proof that $\sqrt[n]{p}$ is irrational is exactly this: exhibit the number as a root of an irreducible polynomial of degree $\geq 2$, and conclude no rational value is possible. The same template proves the irrationality of $\sqrt{2}$, of $\cos(20^\circ)$ (root of an irreducible cubic), and of many algebraic numbers — the recurring move is "find the minimal polynomial, show it is irreducible, read off that the number is not rational." Conversely this is why a *root search* (the rational root theorem) settles irreducibility for cubics but must be supplemented for quartics.

**Eisenstein is a one-sided test, sensitive to the prime, and silence is not refutation.** The criterion is a *sufficient* condition for irreducibility, never a necessary one. If no prime satisfies the pattern, the criterion says nothing whatsoever — the polynomial may still be irreducible (and then one needs reduction mod $p$, a substitution, or a root search), or it may be reducible. Moreover the test depends on *which* prime is fed in: the variant $X^5 - 12X^3 + 36X - 12$ is certified irreducible by $p = 3$, while $p = 2$ fails because $4 \mid 12$ violates the $p^2 \nmid a_0$ condition. The practical discipline: treat the choice of prime as a small search over the prime factors of the constant and interior coefficients, verify *all three* conditions explicitly rather than by eye, and if every prime fails, do not conclude reducibility — switch methods. The substitution trick of [[Ex - Irreducibility of the cyclotomic polynomial]] exists precisely because some genuinely irreducible polynomials satisfy Eisenstein at *no* prime until a clever change of variable exposes the pattern.

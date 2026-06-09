---
type: exercise
subject: commutative-algebra
difficulty: "⭐"
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - Integral Closure and Normal Domain"
  - "Def - Unique Factorization Domain"
  - "Thm - A UFD is Integrally Closed"
  - "Thm - Rational Algebraic Integers are Integers"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Prove that $\mathbb{Z}$ is **integrally closed** in $\mathbb{Q}$: the only rational numbers integral over $\mathbb{Z}$ are the integers. Equivalently, the integral closure of $\mathbb{Z}$ in $\operatorname{Frac}(\mathbb{Z}) = \mathbb{Q}$ is $\mathbb{Z}$ itself, so $\mathbb{Z}$ is a normal domain.

Concretely: if $x \in \mathbb{Q}$ satisfies a monic equation $x^n + c_{n-1}x^{n-1} + \cdots + c_0 = 0$ with $c_i \in \mathbb{Z}$, show $x \in \mathbb{Z}$.

**Recall:**

The objects in play are integral elements, the integral closure, normal domains, and unique factorization in $\mathbb{Z}$.

![[Def - Integral Element and Integral Extension#The Definition]]

![[Def - Integral Closure and Normal Domain#The Definition]]

An element $x$ of $\operatorname{Frac}(A)$ is [[Def - Integral Element and Integral Extension|integral]] over $A$ if it satisfies a *monic* polynomial with coefficients in $A$. The [[Def - Integral Closure and Normal Domain|integral closure]] of $A$ in $\operatorname{Frac}(A)$ is the set of such $x$; $A$ is **normal** (integrally closed) if this set is just $A$.

![[Thm - A UFD is Integrally Closed#Statement]]

$\mathbb{Z}$ is a [[Def - Unique Factorization Domain|unique factorization domain]]: every nonzero integer factors uniquely into primes, and a rational $x = a/b$ can be put in **lowest terms** with $\gcd(a, b) = 1$.

---

# Convergent Strategy

**Problem class.** This is the *base case of the entire normalization theory* — establishing that the most familiar ring, $\mathbb{Z}$, is already integrally closed. It is the prototype for "disprove integrality using normality of a UFD" (operation 4 on the [[Commutative Algebra VI — Integral Extensions#Legal Operations|topic page]]). The result is also exactly [[Thm - Rational Algebraic Integers are Integers|"a rational algebraic integer is an integer"]] restated in the integral-closure language.

**Assumption pattern.** The single leverable fact is that $\mathbb{Z}$ is a *UFD*. This unlocks the lowest-terms representation $x = a/b$ with $a, b$ coprime, which is the entire engine: coprimality means no prime divides both numerator and denominator, and that is what the contradiction will exploit. The hypothesis "monic equation" is what lets the numerator power $a^n$ stand alone after clearing denominators.

**Theorem routing.** Two routes, both valid. The *general* route is to invoke [[Thm - A UFD is Integrally Closed|"a UFD is integrally closed"]] with $A = \mathbb{Z}$: $\mathbb{Z}$ is a UFD, so it is normal, done in one line. The *hands-on* route — which is the proof of that theorem specialised — is to run the lowest-terms argument directly: write $x = a/b$ coprime, clear denominators, and show any prime in $b$ divides $a$, contradicting coprimality. We present the hands-on route as the substance and note the general route as the one-liner.

**Key decision point.** The only non-obvious move is to write $x$ in *lowest terms* before substituting. If you substitute a non-reduced fraction, the divisibility bookkeeping fails — you need coprimality of $a, b$ to derive the contradiction. The second subtlety is *where monic-ness is used*: it is precisely the step that isolates $a^n$ with coefficient $1$, so that a prime dividing $b$ is forced to divide $a^n$ (hence $a$), rather than possibly dividing the leading coefficient.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VI — Integral Extensions#Legal Operations|the topic page's Legal Operations]]:

1. **Disprove integrality with a normal ring (operation 4).** Recognise $\mathbb{Z}$ as a UFD, hence normal, so its integral closure in $\mathbb{Q}$ is $\mathbb{Z}$ — a genuine fraction cannot be integral.

2. **Write in lowest terms using unique factorization.** The UFD structure of $\mathbb{Z}$ supplies a coprime representation $x = a/b$, the lever for the contradiction.

3. **Clear denominators to isolate the numerator power.** Multiply the monic equation by $b^n$ so that $a^n$ stands alone, with every other term divisible by $b$.

4. **Track a single prime to a contradiction.** A prime $p \mid b$ must then divide $a^n$, hence $a$ (primality), contradicting coprimality.

---

# Hints

> [!note]- Hint 1
> $\mathbb{Z}$ is a unique factorization domain. There is a one-line theorem in this chapter that finishes the problem immediately — which one? If you want to do it by hand instead, what is the most useful way to write a rational number $x$ before plugging it into a polynomial equation?

> [!note]- Hint 2
> Write $x = a/b$ in *lowest terms*: $a, b \in \mathbb{Z}$, $b > 0$, $\gcd(a, b) = 1$. Suppose for contradiction $x \notin \mathbb{Z}$, so $b > 1$, and pick a prime $p$ dividing $b$. Substitute into the monic equation and clear denominators by multiplying by $b^n$.

> [!note]- Hint 3
> After multiplying by $b^n$ you get $a^n + c_{n-1}a^{n-1}b + \cdots + c_0 b^n = 0$. Isolate $a^n$ on one side: every other term has a factor of $b$. So $b \mid a^n$, hence $p \mid a^n$. Now use that $p$ is prime: $p \mid a$. But $p \mid b$ and $\gcd(a, b) = 1$ — contradiction.

---

# Solution

The cleanest proof is one line: $\mathbb{Z}$ is a UFD, and [[Thm - A UFD is Integrally Closed|every UFD is integrally closed]]. We give the hands-on argument that *is* that theorem specialised to $\mathbb{Z}$, because it exposes exactly where unique factorization and monic-ness do their work. The plan: write $x$ in lowest terms, assume it is not an integer so a prime divides the denominator, clear denominators to isolate $a^n$, and derive that the prime divides the numerator — contradicting coprimality.

**Step 1: Reduce to lowest terms.**

Write $x = a/b$ with $a, b \in \mathbb{Z}$, $b \geq 1$, and $\gcd(a, b) = 1$.

> [!note]- Derivation
> Any rational is a ratio of integers; dividing numerator and denominator by their greatest common divisor (which exists and is unique up to sign because $\mathbb{Z}$ is a [[Def - Unique Factorization Domain|UFD]]) gives a representation $x = a/b$ with $\gcd(a, b) = 1$ and $b \geq 1$. "Coprime" means: no prime $p$ divides both $a$ and $b$. We aim to show $b = 1$, i.e. $x = a \in \mathbb{Z}$.

**Step 2: Suppose $x \notin \mathbb{Z}$ and clear denominators.**

If $b > 1$, pick a prime $p \mid b$. Substituting $x = a/b$ into $x^n + c_{n-1}x^{n-1} + \cdots + c_0 = 0$ and multiplying by $b^n$ gives $a^n + c_{n-1}a^{n-1}b + \cdots + c_0 b^n = 0$.

> [!note]- Derivation
> Assume for contradiction $x \notin \mathbb{Z}$. Then $b \neq 1$, so $b > 1$ has a prime factor $p$ (existence of prime factors is unique factorization in $\mathbb{Z}$). Substitute $x = a/b$ into the [[Def - Integral Element and Integral Extension|monic equation]]:
> $$\Big(\frac{a}{b}\Big)^n + c_{n-1}\Big(\frac{a}{b}\Big)^{n-1} + \cdots + c_1 \frac{a}{b} + c_0 = 0.$$
> Multiply through by $b^n$:
> $$a^n + c_{n-1}a^{n-1}b + c_{n-2}a^{n-2}b^2 + \cdots + c_1 a\, b^{n-1} + c_0 b^n = 0.$$
> The leading term is $a^n$ with coefficient $1$ — this is exactly where *monic-ness* is used; a non-monic equation would leave a coefficient $c_n a^n$ and break the next step.

**Step 3: Derive the contradiction.**

$b \mid a^n$, so $p \mid a^n$, so $p \mid a$ — contradicting $\gcd(a, b) = 1$. Hence $b = 1$ and $x \in \mathbb{Z}$.

> [!note]- Derivation
> Rearrange the cleared equation to isolate $a^n$:
> $$a^n = -\big(c_{n-1}a^{n-1}b + c_{n-2}a^{n-2}b^2 + \cdots + c_0 b^n\big) = -b\big(c_{n-1}a^{n-1} + c_{n-2}a^{n-2}b + \cdots + c_0 b^{n-1}\big).$$
> The right-hand side is divisible by $b$, hence by the prime $p \mid b$. So $p \mid a^n$. Since $p$ is prime, $p \mid a$. But then $p$ divides both $a$ and $b$, contradicting $\gcd(a, b) = 1$. The contradiction came solely from assuming $b > 1$; therefore $b = 1$ and $x = a \in \mathbb{Z}$.

> [!note]- Complete formal solution
> **Claim.** $\mathbb{Z}$ is integrally closed in $\mathbb{Q}$.
>
> *One-line proof.* $\mathbb{Z}$ is a UFD, and [[Thm - A UFD is Integrally Closed|every UFD is integrally closed in its field of fractions]]. Hence the only elements of $\mathbb{Q} = \operatorname{Frac}(\mathbb{Z})$ integral over $\mathbb{Z}$ are those of $\mathbb{Z}$. $\blacksquare$
>
> *Direct proof.* Let $x \in \mathbb{Q}$ satisfy $x^n + c_{n-1}x^{n-1} + \cdots + c_0 = 0$ with $c_i \in \mathbb{Z}$. Write $x = a/b$ in lowest terms ($\gcd(a, b) = 1$, $b \geq 1$). Suppose $b > 1$ and let $p$ be a prime dividing $b$. Multiplying the equation by $b^n$,
> $$a^n + c_{n-1}a^{n-1}b + \cdots + c_0 b^n = 0,$$
> so $a^n = -b(c_{n-1}a^{n-1} + \cdots + c_0 b^{n-1})$, whence $b \mid a^n$ and $p \mid a^n$. As $p$ is prime, $p \mid a$, contradicting $\gcd(a, b) = 1$. Hence $b = 1$ and $x \in \mathbb{Z}$. $\blacksquare$

---

# Key Takeaways

**Normality of a UFD is the one-line reason a "genuine fraction" can never be an algebraic integer.** The single most useful reflex this exercise installs is: when asked whether some $x \in \operatorname{Frac}(A)$ is integral over $A$, *first ask whether $A$ is a UFD*. If it is — and $\mathbb{Z}$, every PID, every polynomial ring over a field, every DVR are — then the answer is immediate: $x$ is integral iff $x \in A$, with no equation to check. This collapses an entire genre of problems ("is $\tfrac{17}{5}$ an algebraic integer?", "is $t^{-1}$ integral over $k[t]$?", "is this element in the ring of integers?") into a membership test. The trigger is "$A$ is a UFD and $x$ is a non-trivial fraction"; the reaction is "not integral, by [[Thm - A UFD is Integrally Closed|normality of a UFD]]".

**Lowest terms is not a convenience but the engine, and it needs unique factorization to exist.** The proof turns entirely on writing $x = a/b$ with $\gcd(a, b) = 1$. Coprimality is what makes "$p \mid a$ and $p \mid b$" a contradiction; without it there is nothing to contradict. And the existence of a coprime representation is *exactly* unique factorization — in a non-UFD you cannot always reduce to lowest terms, and indeed the conclusion can fail. This is why the theorem is "a *UFD* is integrally closed" and not "every domain is": the hypothesis is precisely what guarantees lowest terms. When you see a divisibility argument hinging on coprimality, recognise that a UFD hypothesis is silently doing the work.

**Monic-ness is the hinge that isolates the numerator power.** Track where "$f$ is monic" is used: it is the single step where $a^n$ emerges with coefficient $1$ after clearing denominators, so that *every other term* carries a factor of $b$. With a non-monic equation $c_n x^n + \cdots = 0$, clearing denominators leaves $c_n a^n + (\text{multiples of } b) = 0$, and now a prime $p \mid b$ only forces $p \mid c_n a^n$ — which it could satisfy by dividing $c_n$ rather than $a$. That is exactly the loophole through which $\tfrac12$ escapes (its equation $2T - 1$ has leading coefficient $2$, and $p = 2$ divides the leading coefficient). The distinction integral-versus-algebraic *lives* in this one step; understanding it is understanding the whole chapter's defining boundary. See the companion [[Ex - Z[sqrt 5] is not integrally closed]] for what happens when the base is *not* a UFD and a genuine fraction *does* turn out integral.

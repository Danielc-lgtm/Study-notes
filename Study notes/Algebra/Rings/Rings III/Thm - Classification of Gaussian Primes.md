---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Gaussian Integers"
  - "Def - Irreducible and Prime Elements"
  - "Def - Unique Factorization Domain"
  - "Thm - The Unit Group of a Finite Field is Cyclic"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ is the ring of [[Def - Gaussian Integers|Gaussian integers]] and $N(a+bi) = a^2 + b^2 = (a+bi)(a-bi)$ is its **norm**, which is multiplicative, $N(zw) = N(z)N(w)$. We write $\bar z = a - bi$ for the complex conjugate of $z = a + bi$; conjugation is a ring automorphism of $\mathbb{Z}[i]$. The units of $\mathbb{Z}[i]$ are $\pm 1, \pm i$, the elements of norm $1$. A **rational prime** is an ordinary prime $p \in \mathbb{Z}$ (the word distinguishes it from a prime *of $\mathbb{Z}[i]$*). Two Gaussian integers are **associates**, $u \sim v$, if $v = uw$ for a unit $w$; "up to associates" means we count an element and its three unit multiples as one. The notation $p \equiv 3 \pmod 4$ means $p$ leaves remainder $3$ on division by $4$. Since $\mathbb{Z}[i]$ is a [[Def - Unique Factorization Domain|UFD]], **[[Def - Irreducible and Prime Elements|irreducible and prime coincide]]** in it, and we use the words interchangeably. The full registry is on [[Rings III — §2.5–2.6]].

---

# Statement

> **Proposition (which rational primes stay prime).** A rational prime $p$ is prime in $\mathbb{Z}[i]$ if and only if $p$ is *not* a sum of two non-zero squares — that is, $p \neq a^2 + b^2$ for any $a, b \in \mathbb{Z} \setminus \{0\}$.

> **Classification of Gaussian primes.** Up to associates and ordering, every prime of $\mathbb{Z}[i]$ is of exactly one of the following two types:
>
> **(i)** a rational prime $p \in \mathbb{Z} \leq \mathbb{Z}[i]$ with $p \equiv 3 \pmod 4$ (these are the **inert** primes);
>
> **(ii)** a Gaussian integer $z$ with $N(z) = z\bar z = p$ for a rational prime $p$ equal to $2$ or congruent to $1 \pmod 4$ (these are the **split** primes — together with the **ramified** prime $1+i$ over $p = 2$).
>
> Equivalently, the rational primes behave as follows under passage to $\mathbb{Z}[i]$:
> $$p \equiv 3 \!\!\pmod 4 \ \Rightarrow\ p \text{ stays prime}; \qquad p \equiv 1 \!\!\pmod 4 \ \Rightarrow\ p = z\bar z \text{ splits}; \qquad 2 = -i(1+i)^2 \text{ ramifies}.$$

---

# Motivation

You have just learned that $\mathbb{Z}[i]$ is a [[Def - Unique Factorization Domain|unique factorization domain]]: every Gaussian integer factors into primes, uniquely up to order and units. That is a powerful guarantee — but it is *empty* until you know what the primes actually are. Unique factorization into an unknown set of primes is like a dictionary in a language you cannot read. This theorem reads the language: it lists every prime of $\mathbb{Z}[i]$ explicitly.

The first concrete observation, met in §2.6, is that rational primes do **not** stay prime when you enlarge $\mathbb{Z}$ to $\mathbb{Z}[i]$. We saw $2 = (1+i)(1-i)$ and $5 = (2+i)(2-i)$ — both *split* — while $3$ and $7$ remained prime. So the rational primes get sorted into two boxes by passage to the Gaussian integers, and the natural question is: *which prime goes in which box, and is there a pattern?* The answer is strikingly clean. The pattern is the residue of $p$ modulo $4$: primes $\equiv 3$ stay prime, primes $\equiv 1$ split, and the single even prime $2$ is a special "ramified" case. The whole of the rich behaviour of primes in $\mathbb{Z}[i]$ is governed by one bit of arithmetic information about $p$.

Why should one expect such a result? Because of the **norm**. A prime of $\mathbb{Z}[i]$ has a norm, and that norm is a positive integer; a Gaussian integer of *prime* norm is automatically irreducible (its norm cannot factor non-trivially). So Gaussian primes come in two flavours from the start: those whose norm is a rational prime $p$ (these "lie over $p$" and there are two of them, $z$ and $\bar z$), and those whose norm is $p^2$ (a rational prime that did not split). The norm of $z = a+bi$ is $a^2 + b^2$ — a **sum of two squares** — and the elementary fact that a square is $0$ or $1$ mod $4$ means a sum of two squares is *never* $\equiv 3 \pmod 4$. That single congruence obstruction is the seed of the whole classification: it instantly explains why $p \equiv 3$ cannot be a norm, hence cannot split. The harder direction — that $p \equiv 1$ *always* splits — is where the [[Thm - The Unit Group of a Finite Field is Cyclic|cyclicity of mathbbFptimes]] enters, to manufacture a square root of $-1$ modulo $p$.

The theorem is also the gateway to [[Thm - Sum of Two Squares|Fermat's two-squares theorem]]: once you know which primes are norms, the multiplicativity of the norm tells you which *integers* are norms, i.e. which are sums of two squares.

---

# Sources and Targets

**Sources (Input Broadening)**

The proposition and the classification consume two kinds of input, and recognising each in disguise is the skill.

The first source is **a rational prime $p$ together with its residue mod $4$**. Whenever a problem hands you an ordinary prime and asks about its behaviour in $\mathbb{Z}[i]$ — does it stay prime? does $p \mid z$ for a given $z$? — the residue $p \bmod 4$ is the input that routes the answer. The bridge is the classification itself: $p \bmod 4 \in \{1, 2, 3\}$ (every odd prime is $1$ or $3$; $p = 2$ is the exception) and each value forces a definite splitting type. The non-obvious part is that a question about *factorization in a quadratic ring* is answered by a *congruence*, with no factorization attempted. *Example problem:* decide whether $13$ is prime in $\mathbb{Z}[i]$ — it is not, since $13 \equiv 1 \pmod 4$.

The second source is **a Gaussian integer of known norm**. If you are handed $z \in \mathbb{Z}[i]$ and can compute $N(z)$, the factorization of the *integer* $N(z)$ controls the factorization of $z$. The cleanest case: $N(z)$ is a rational prime $\Rightarrow z$ is irreducible. More generally, the rational primes dividing $N(z)$ are exactly the rational primes lying under the Gaussian primes dividing $z$. The bridge is multiplicativity of the norm. The non-obviousness is that an *integer* factorization (easy, classical) is leveraged to deduce a *Gaussian* factorization. *Example problem:* show $4 + i$ is irreducible — its norm is $17$, a rational prime.

The third, subtler source is **a sum-of-two-squares representation, or the lack of one**. By the proposition, "$p$ is a sum of two non-zero squares" is *equivalent* to "$p$ splits in $\mathbb{Z}[i]$". So any time a problem gives you, or denies you, a representation $p = a^2 + b^2$, it is secretly telling you the splitting type. The non-obvious bridge is the identity $a^2 + b^2 = (a+bi)(a-bi)$ — an arithmetic statement about $\mathbb{Z}$ reinterpreted as a factorization in $\mathbb{Z}[i]$.

**Targets (Output Amplification)**

The bare conclusion is a list of the Gaussian primes. Combined with other facts it does much more.

Combine the classification with **the multiplicativity of the norm** to factor *arbitrary* Gaussian integers. Once you know the primes, factoring $z$ reduces to: factor the integer $N(z)$ into rational primes, sort those by residue mod $4$, and for each split prime $p = \pi\bar\pi$ decide how many copies of $\pi$ versus $\bar\pi$ divide $z$. This is the non-obvious target: the classification plus the norm turns Gaussian factorization into ordinary integer factorization. It is the engine of the [[Thm - Sum of Two Squares|sum-of-two-squares theorem]].

Combine the classification with **counting** to count representations as sums of two squares. The number of ways to write $n = x^2 + y^2$ is the number of factorizations of $n$ as $z\bar z$ in $\mathbb{Z}[i]$, which the classification makes computable: each split prime $p^k$ in $n$ contributes a free choice of how to distribute the $k$ factors between $\pi$ and $\bar\pi$. This yields the classical formula $r_2(n) = 4\sum_{d \mid n}\chi(d)$ — a non-obvious bridge from a factorization list to an exact counting function.

Combine the proposition with **its contrapositive** to prove *non*-representability. "$p \equiv 3 \pmod 4 \Rightarrow p$ is not a sum of two non-zero squares" is the contrapositive direction, and it is the standard way to certify that a specific number cannot be written as $x^2 + y^2$. Useful far beyond $\mathbb{Z}[i]$: it underlies which integers are *not* sums of two squares.

---

# Why Is It True

There are two halves, and they have completely different characters. One half is a one-line congruence; the other half is the real content and needs a square root of $-1$ conjured out of [[Def - Group|group]] theory. Seeing why each half is what it is makes the proof unsurprising.

**The easy half: $p \equiv 3 \pmod 4$ stays prime.** A Gaussian integer that splits a rational prime would have to have norm $p$ — because if $p = uv$ with $u, v$ non-units then $p^2 = N(u)N(v)$ forces $N(u) = N(v) = p$. So $p$ splits *only if* $p$ is a norm, i.e. $p = a^2 + b^2$ for some integers. But now look mod $4$: an integer square is $0^2, 1^2, 2^2, 3^2 \equiv 0, 1, 0, 1$, so every square is $0$ or $1$ mod $4$, and a sum of two squares is $0 + 0, 0 + 1, 1 + 1 \equiv 0, 1, 2$ mod $4$ — **never $3$**. A prime $\equiv 3 \pmod 4$ is therefore not a sum of two squares, cannot be a norm, cannot split, and stays prime. The whole obstruction is the arithmetic of squares modulo $4$; nothing deep is happening, the congruence simply forbids $p$ from being a norm.

**The hard half: $p \equiv 1 \pmod 4$ (and $p = 2$) splits.** Now you must *exhibit* a factorization, and the question becomes: how do you break $p$? The idea is to find a non-unit Gaussian integer that *shares a factor* with $p$. Suppose you could find an ordinary integer $a$ with
$$p \mid a^2 + 1.$$
Then in $\mathbb{Z}[i]$ the right-hand side factors: $a^2 + 1 = (a + i)(a - i)$. So $p$ divides the product $(a+i)(a-i)$. If $p$ were *prime* in $\mathbb{Z}[i]$, it would have to divide one of the factors — but $p \mid a + i$ would mean $\tfrac{a}{p} + \tfrac{1}{p}i \in \mathbb{Z}[i]$, impossible since $\tfrac{1}{p} \notin \mathbb{Z}$, and likewise for $a - i$. So $p$ divides a product without dividing either factor: $p$ is **not prime** in $\mathbb{Z}[i]$. Since $\mathbb{Z}[i]$ is a UFD, not prime means not irreducible, so $p$ genuinely factors, $p = z_1 z_2$ with non-units, and (taking norms) $N(z_1) = N(z_2) = p$. The prime splits.

Everything now rests on producing that integer $a$ with $p \mid a^2 + 1$ — equivalently, a **square root of $-1$ modulo $p$**. Why should one exist when $p \equiv 1 \pmod 4$? This is exactly where the [[Thm - The Unit Group of a Finite Field is Cyclic|cyclicity of mathbbFptimes]] is decisive. The group $\mathbb{F}_p^\times$ is cyclic of order $p - 1$. When $p \equiv 1 \pmod 4$, the order $p - 1$ is divisible by $4$, and a cyclic group whose order is a multiple of $4$ contains an element $a$ of order exactly $4$. Square it: $a^2$ has order $2$. But a cyclic group of even order has a *unique* element of order $2$, and in $\mathbb{F}_p^\times$ that element is plainly $[-1]$ (it satisfies $x^2 = 1$, $x \neq 1$). Hence $a^2 = [-1]$ in $\mathbb{F}_p$ — that is, $p \mid a^2 + 1$. The square root of $-1$ exists *because* the residue $p \equiv 1 \pmod 4$ makes $4$ divide the order of the cyclic group $\mathbb{F}_p^\times$. (For $p = 2$ no group theory is needed — one simply checks $2 = (1+i)(1-i)$ by hand.) This is the moment the congruence mod $4$ does its work: it is precisely the condition for the cyclic group $\mathbb{F}_p^\times$ to have room for an order-$4$ element.

**Why the list is complete.** Finally, why are these *all* the Gaussian primes? Because every Gaussian prime $z$ has a norm $N(z) = z\bar z > 1$, so some rational prime $p$ divides $N(z)$, hence (as $z$ is prime and divides... ) $z$ lies over $p$: $z$ divides $p$ in $\mathbb{Z}[i]$. So every Gaussian prime divides *some* rational prime, and we have just analysed how each rational prime factors — into one prime (if $p \equiv 3$) or two (if $p \equiv 1$ or $p = 2$). The Gaussian primes are therefore exhausted by running over all rational primes and collecting the prime factors that appear. There is nowhere else for a Gaussian prime to come from.

---

# What Makes This Hard

The genuinely hard step is producing an integer $a$ with $p \mid a^2 + 1$ when $p \equiv 1 \pmod 4$; most people get stuck here because the natural instinct is to search for $a$ directly, when the right move is to extract it *non-constructively* from the [[Thm - The Unit Group of a Finite Field is Cyclic|cyclicity of mathbbFptimes]] — an order-$4$ element whose square is the unique order-$2$ element $[-1]$. The most common error is to forget that "$p$ is not prime" must be upgraded to "$p$ factors": this needs $\mathbb{Z}[i]$ to be a UFD, where irreducible and prime coincide; without it, "$p$ divides a product without dividing a factor" alone does not hand you a factorization. A secondary subtlety is the completeness argument — one must remember that every Gaussian prime lies over a rational prime, otherwise the list is only shown to *contain* primes, not to be *all* of them.

---

# Rederivation Scaffold

**High-level strategy:**
Two directions for the proposition, then a completeness sweep. For "$p$ splits $\Rightarrow$ $p$ is a sum of squares": take norms. For "$p \equiv 1 \pmod 4 \Rightarrow p$ splits": find $a$ with $p \mid a^2+1$ via cyclicity of $\mathbb{F}_p^\times$, factor $a^2+1 = (a+i)(a-i)$, observe $p$ divides the product but neither factor. For completeness: every Gaussian prime divides some rational prime.

**Subgoal decomposition:**

1. **A split rational prime has prime norm.** Show that if $p = uv$ in $\mathbb{Z}[i]$ with $u, v$ non-units, then $N(u) = N(v) = p$.
   - *Hint:* Apply the multiplicative norm: $N(p) = p^2 = N(u)N(v)$, and non-units have norm $> 1$.
   - *Why needed:* It identifies "splits" with "has a divisor of norm $p$", i.e. "$p$ is a sum of two squares".

2. **Squares mod $4$ block $p \equiv 3$.** Show no sum of two squares is $\equiv 3 \pmod 4$.
   - *Hint:* A square is $0$ or $1$ mod $4$; sum two of them.
   - *Why needed:* Combined with Subgoal 1, it proves $p \equiv 3 \Rightarrow p$ stays prime.

3. **Produce a square root of $-1$ mod $p$ for $p \equiv 1 \pmod 4$.** Show there is $a \in \mathbb{Z}$ with $p \mid a^2 + 1$.
   - *Hint:* $\mathbb{F}_p^\times$ is cyclic of order $p - 1$, divisible by $4$; take an order-$4$ element $a$, so $a^2$ has order $2$ and equals the unique order-$2$ element $[-1]$.
   - *Why needed:* It gives the factorable element $a^2 + 1$ that breaks $p$.

4. **Break $p$ using $(a+i)(a-i)$.** Show $p$ is not prime in $\mathbb{Z}[i]$, hence factors, hence splits.
   - *Hint:* $p \mid a^2 + 1 = (a+i)(a-i)$ but $p \nmid a \pm i$ (the imaginary part $\tfrac{1}{p} \notin \mathbb{Z}$); not prime $\Rightarrow$ not irreducible in a UFD; then take norms. For $p = 2$, use $2 = (1+i)(1-i)$ directly.
   - *Why needed:* Completes the proposition's hard direction and supplies type-(ii) primes.

5. **Completeness.** Show every Gaussian prime $z$ divides some rational prime, and is therefore an associate of a prime found in Subgoals 1–4.
   - *Hint:* $N(z) > 1$ has a rational prime factor $p$; then $p \mid z\bar z$, and analysing $p$'s factorization places $z$.
   - *Why needed:* Confirms the list (i)–(ii) is exhaustive, not merely a list of examples.

---

# Lemma Decomposition

> [!note]- Lemma 1: A rational prime that factors in $\mathbb{Z}[i]$ has a factor of norm $p$
> **Statement:** If a rational prime $p$ can be written $p = uv$ with $u, v \in \mathbb{Z}[i]$ both non-units, then $N(u) = N(v) = p$; equivalently, writing $u = a + bi$, one has $a^2 + b^2 = p$.
>
> **Hint:** Take the norm of $p = uv$ and use that the norm of a non-unit is at least $2$.
>
> **Why needed:** It is the bridge between "$p$ splits in $\mathbb{Z}[i]$" and "$p$ is a sum of two squares" — used in both directions of the proposition.
>
> > [!note]- Full proof
> > Apply the multiplicative norm to $p = uv$:
> > $$p^2 = N(p) = N(uv) = N(u)\,N(v).$$
> > Both $N(u)$ and $N(v)$ are positive integers. Since $u$ is not a unit, $N(u) \neq 1$, so $N(u) \geq 2$; likewise $N(v) \geq 2$. The only factorization of $p^2$ into two integer factors each $\geq 2$ is $p \cdot p$. Hence $N(u) = N(v) = p$. Writing $u = a + bi$ gives $a^2 + b^2 = N(u) = p$. $\blacksquare$

> [!note]- Lemma 2: A prime $p \equiv 3 \pmod 4$ is not a sum of two squares
> **Statement:** If $p \equiv 3 \pmod 4$, then there are no integers $a, b$ with $a^2 + b^2 = p$.
>
> **Hint:** Compute the possible values of a square, and of a sum of two squares, modulo $4$.
>
> **Why needed:** With Lemma 1, it proves the easy direction of the classification — primes $\equiv 3 \pmod 4$ cannot split, so they stay prime.
>
> > [!note]- Full proof
> > For any integer $n$, $n$ is even or odd, so $n \equiv 0, 1, 2, 3 \pmod 4$ and $n^2 \equiv 0, 1, 0, 1 \pmod 4$ respectively. Hence **every square is $\equiv 0$ or $1 \pmod 4$.** Adding two squares, the possible [[Def - Residue|residues]] are
> > $$0 + 0 = 0, \quad 0 + 1 = 1, \quad 1 + 1 = 2 \pmod 4.$$
> > So a sum of two squares is $\equiv 0, 1$, or $2 \pmod 4$, and **never $\equiv 3$**. A prime $p \equiv 3 \pmod 4$ therefore cannot equal $a^2 + b^2$. $\blacksquare$

> [!note]- Lemma 3: For $p \equiv 1 \pmod 4$ there is an integer $a$ with $p \mid a^2 + 1$
> **Statement:** If $p$ is a prime with $p \equiv 1 \pmod 4$, then there exists $a \in \mathbb{Z}$ such that $p \mid a^2 + 1$ — equivalently, $-1$ is a square modulo $p$.
>
> **Hint:** Use that $\mathbb{F}_p^\times$ is cyclic of order $p - 1$; since $4 \mid p - 1$, pick an element of order $4$ and square it.
>
> **Why needed:** It manufactures the element $a^2 + 1 = (a+i)(a-i)$ that exhibits $p$ as non-prime in $\mathbb{Z}[i]$ — the hard direction of the classification.
>
> > [!note]- Full proof
> > Since $p \equiv 1 \pmod 4$, write $p - 1 = 4k$ for some integer $k \geq 1$. By [[Thm - The Unit Group of a Finite Field is Cyclic|the theorem that mathbbFptimes is cyclic]], the group $\mathbb{F}_p^\times = (\mathbb{Z}/p\mathbb{Z}) \setminus \{0\}$ is cyclic of order $p - 1 = 4k$. A cyclic group of order $n$ has an element of order $d$ for every divisor $d$ of $n$; since $4 \mid 4k$, there is an element $[a] \in \mathbb{F}_p^\times$ of order exactly $4$.
> >
> > Then $[a]^2 = [a^2]$ has order $4/\gcd(2,4) = 2$. Now $\mathbb{F}_p^\times$ is cyclic of *even* order $4k$, and a cyclic group of even order has exactly **one** element of order $2$. The residue $[-1]$ satisfies $[-1]^2 = [1]$ and $[-1] \neq [1]$ (as $p > 2$), so $[-1]$ is an element of order $2$ — hence *the* element of order $2$. Therefore
> > $$[a^2] = [-1] \quad\text{in } \mathbb{F}_p, \qquad\text{i.e.}\qquad a^2 \equiv -1 \pmod p,$$
> > which says $p \mid a^2 + 1$. $\blacksquare$
> >
> > *Remark.* This is non-constructive: it produces $a$ from the existence of a generator of $\mathbb{F}_p^\times$, without exhibiting one.

> [!note]- Lemma 4: A rational prime dividing $(a+i)(a-i)$ but neither factor is not prime in $\mathbb{Z}[i]$
> **Statement:** Let $p$ be a rational prime and $a \in \mathbb{Z}$ with $p \mid a^2 + 1$. Then $p$ divides the product $(a+i)(a-i)$ but divides neither factor; consequently $p$ is not prime in $\mathbb{Z}[i]$, and since $\mathbb{Z}[i]$ is a UFD, $p$ is reducible — it factors as $p = z_1 z_2$ with $z_1, z_2$ non-units of norm $p$.
>
> **Hint:** $p \mid a \pm i$ would force $\tfrac{1}{p}$ to be an integer. Then use "not prime $\Rightarrow$ not irreducible" in a UFD, and take norms.
>
> **Why needed:** It is the step that actually *splits* $p$, producing the type-(ii) Gaussian primes.
>
> > [!note]- Full proof
> > Since $p \mid a^2 + 1$ and $a^2 + 1 = (a+i)(a-i)$ in $\mathbb{Z}[i]$, we have $p \mid (a+i)(a-i)$.
> >
> > But $p \nmid a + i$: if $a + i = p\,(c + di)$ for some $c, d \in \mathbb{Z}$, comparing imaginary parts gives $1 = pd$, impossible for $d \in \mathbb{Z}$ and $p \geq 2$. Identically $p \nmid a - i$ (imaginary parts give $-1 = pd$).
> >
> > So $p$ divides a product of two Gaussian integers without dividing either: $p$ is **not prime** in $\mathbb{Z}[i]$. Because $\mathbb{Z}[i]$ is a [[Def - Unique Factorization Domain|UFD]], an element is prime if and only if it is [[Def - Irreducible and Prime Elements|irreducible]]; hence $p$ is not irreducible. As $p$ is a non-zero non-unit ($N(p) = p^2 > 1$), being reducible means $p = z_1 z_2$ with $z_1, z_2$ non-units. By Lemma 1, $N(z_1) = N(z_2) = p$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
>
> **Part A — the proposition.** *Claim: a rational prime $p$ is prime in $\mathbb{Z}[i]$ if and only if $p$ is not a sum of two non-zero squares.*
>
> ($\Leftarrow$, contrapositive) Suppose $p = a^2 + b^2$ with $a, b \in \mathbb{Z} \setminus \{0\}$. Then $p = (a + bi)(a - bi)$, and $N(a \pm bi) = a^2 + b^2 = p \neq 1$, so neither factor is a unit. Hence $p$ is reducible, so (in the UFD $\mathbb{Z}[i]$) not prime.
>
> ($\Rightarrow$, contrapositive) Suppose $p$ is not prime, hence reducible: $p = uv$ with $u, v$ non-units. By Lemma 1, $N(u) = p$, so writing $u = a + bi$ gives $p = a^2 + b^2$. Neither $a$ nor $b$ is zero: if $b = 0$ then $p = a^2$ is not prime, and if $a = 0$ then $p = b^2$ is not prime. So $p$ is a sum of two non-zero squares. This proves Part A.
>
> **Part B — the two types are primes.**
>
> *Type (i).* Let $p \equiv 3 \pmod 4$. By Lemma 2, $p$ is not a sum of two squares; by Part A, $p$ is prime in $\mathbb{Z}[i]$.
>
> *Type (ii).* Let $z \in \mathbb{Z}[i]$ with $N(z) = p$ a rational prime. If $z = uv$, then $p = N(z) = N(u)N(v)$, so one of $N(u), N(v)$ equals $1$, i.e. $u$ or $v$ is a unit. Hence $z$ is irreducible, so prime. (No condition on $p \bmod 4$ is needed here: $N(z) = a^2+b^2$ is automatically a sum of two squares, so by Lemma 2 it cannot itself be $\equiv 3 \pmod 4$.)
>
> **Part C — every rational prime factors as claimed.**
>
> If $p \equiv 3 \pmod 4$: by Type (i), $p$ is itself a Gaussian prime — a prime of type (i).
>
> If $p = 2$: directly $2 = (1+i)(1-i)$, and $1 - i = -i(1+i)$, so $2 = -i(1+i)^2$. The element $1+i$ has $N(1+i) = 2$, prime, so $1+i$ is a Gaussian prime of type (ii). ($2$ ramifies.)
>
> If $p \equiv 1 \pmod 4$: by Lemma 3 there is $a$ with $p \mid a^2 + 1$; by Lemma 4, $p$ is reducible, $p = z_1 z_2$ with $N(z_1) = N(z_2) = p$. By Type (ii) each $z_j$ is a Gaussian prime. Moreover $p = N(z_1) = z_1 \bar z_1$ and $p = z_1 z_2$, so $z_2 = \bar z_1$: the prime $p$ splits as $p = z_1 \bar z_1$ into a conjugate pair of type-(ii) primes.
>
> **Part D — completeness: these are all the Gaussian primes.**
>
> Let $z \in \mathbb{Z}[i]$ be any prime (equivalently irreducible). Its conjugate $\bar z$ is also irreducible (conjugation is a [[Def - Ring|ring]] automorphism, and it carries units to units, hence irreducibles to irreducibles). Now $N(z) = z\bar z$ is a factorization of the integer $N(z)$, and $N(z) \neq 1$ since $z$ is not a unit, so $N(z)$ has a rational prime factor $p$. Then
> $$p \;\mid\; N(z) \;=\; z\bar z \quad\text{in } \mathbb{Z}[i].$$
> Consider the two cases for $p$.
>
> *If $p \equiv 3 \pmod 4$:* by Type (i), $p$ is prime in $\mathbb{Z}[i]$, so from $p \mid z\bar z$ we get $p \mid z$ or $p \mid \bar z$. If $p \mid \bar z$, conjugating gives $p \mid z$ (as $\bar p = p$). So $p \mid z$. Both $p$ and $z$ are irreducible and $p \mid z$, so $z$ and $p$ are associates: $z$ is a type-(i) prime.
>
> *If $p = 2$ or $p \equiv 1 \pmod 4$:* by Part C, $p = z_1\bar z_1$ (for $p=2$ take $z_1 = 1+i$) with $z_1$ a type-(ii) prime of norm $p$. Then $z_1\bar z_1 = p \mid z\bar z$. Since $z_1$ is prime and $z_1 \mid z\bar z$, either $z_1 \mid z$ or $z_1 \mid \bar z$ (and conjugating turns the second into $\bar z_1 \mid z$). In either case $z$ is divisible by an irreducible of norm $p$ ($z_1$ or $\bar z_1$); as $z$ is itself irreducible, $z$ is an associate of that irreducible, so $N(z) = p$ — a type-(ii) prime.
>
> In every case $z$ is, up to associates, a prime of type (i) or (ii). The list is exhaustive. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fermat's two-squares theorem.** The classification is the precise input to [[Thm - Sum of Two Squares|Fermat's theorem]] that a positive integer $n$ is a sum of two squares if and only if every prime $\equiv 3 \pmod 4$ in its factorization occurs to an even power. The non-obvious recognition is that "is a sum of two squares" means "is a norm from $\mathbb{Z}[i]$", and the classification tells you exactly which primes are norms; multiplicativity of the norm extends this to all $n$.

**Quadratic reciprocity, the supplementary law.** Lemma 3 — that $-1$ is a square mod $p$ exactly when $p \equiv 1 \pmod 4$ — is the *first supplement to quadratic reciprocity*, $\left(\tfrac{-1}{p}\right) = (-1)^{(p-1)/2}$. The non-obvious link: a statement usually proved by Euler's criterion drops out here as a corollary of the cyclicity of $\mathbb{F}_p^\times$, and it is the engine of the splitting of primes in $\mathbb{Z}[i]$.

**Counting lattice points on circles.** The number $r_2(n)$ of integer points $(x,y)$ on the circle $x^2 + y^2 = n$ equals the number of $z \in \mathbb{Z}[i]$ with $N(z) = n$. The classification makes $r_2(n)$ computable prime-by-prime: split primes contribute, inert primes constrain, and one obtains $r_2(n) = 4(d_1(n) - d_3(n))$ with $d_j$ counting divisors $\equiv j \pmod 4$. This is a non-obvious bridge from prime classification to a problem in the geometry of numbers.

**Splitting of primes in number fields.** The trichotomy *inert / split / ramified* for primes in $\mathbb{Z}[i]$ is the first instance of the general theory of how rational primes factor in the ring of integers of a number field. Recognising $\mathbb{Z}[i]$'s behaviour as the prototype — with $p \bmod 4$ playing the role of a *splitting condition* governed by a quadratic character — is the non-obvious step that connects §2.6 to algebraic number theory and class field theory.

---

# Bridges

- **[[Thm - The Unit Group of a Finite Field is Cyclic|Cyclicity of mathbbFptimes]]** — the essential lemma for the hard direction. Without it there is no guarantee that $-1$ has a square root modulo $p$ when $p \equiv 1 \pmod 4$, and the proof that such $p$ split would collapse. The classification is, in a precise sense, the cyclicity theorem cashed out in $\mathbb{Z}[i]$.

- **[[Thm - Sum of Two Squares|Sum of Two Squares (Fermat)]]** — the direct corollary. The classification identifies which *primes* are norms; multiplicativity of the norm then identifies which *integers* are norms, which is exactly Fermat's two-squares theorem. The two theorems are best read as a pair: classify the primes, then multiply up.

- **[[Def - Irreducible and Prime Elements|Irreducible equals prime in a UFD]]** — the bookkeeping that makes the proof legal. The argument repeatedly slides between "irreducible" and "prime"; this is licensed only because $\mathbb{Z}[i]$ is a [[Def - Unique Factorization Domain|UFD]], where the two notions coincide. Lemma 4 in particular needs "not prime $\Rightarrow$ not irreducible".

- **Quadratic residues and the Legendre symbol** — the number-theoretic shadow. The condition "$p \equiv 1 \pmod 4$" is "$-1$ is a quadratic residue mod $p$", i.e. $\left(\tfrac{-1}{p}\right) = 1$. The splitting type of $p$ in $\mathbb{Z}[i]$ is governed by this single quadratic character — the model case of the general principle that prime splitting in a quadratic field is governed by a Legendre symbol.

- **Splitting of primes in rings of integers** — the generalisation. The inert/split/ramified trichotomy for $\mathbb{Z}[i]$ is the first instance of how primes decompose in the ring of integers of a number field; the residue $p \bmod 4$ generalises to a Frobenius/splitting condition, the content of class field theory.

---

# Unlocked by This

> [!tip] Sum of Two Squares *(from this topic)*
> Knowing exactly which rational primes are norms from $\mathbb{Z}[i]$ — those equal to $2$ or $\equiv 1 \pmod 4$ — and that the norm is multiplicative, lets you characterise *every* integer that is a sum of two squares. See [[Thm - Sum of Two Squares]].

> [!tip] Decomposition of Primes in Number Fields *(from Algebraic Number Theory)*
> The trichotomy inert / split / ramified, here decided by $p \bmod 4$, is the prototype for how a rational prime factors in the ring of integers of any number field — the subject of decomposition groups, the Frobenius element, and ultimately class field theory.

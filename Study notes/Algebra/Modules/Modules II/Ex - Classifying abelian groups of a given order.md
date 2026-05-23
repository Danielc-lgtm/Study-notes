---
type: exercise
subject: module-theory
difficulty: "⭐"
prereqs:
  - "Thm - Classification of Finitely Generated Abelian Groups"
  - "Thm - Chinese Remainder Theorem for Modules"
  - "Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain"
tags: [algebra, module-theory]
---

# Problem Statement

How many abelian [[Def - Group|groups]] of order $600$ are there, up to isomorphism?

1. Determine the count, and **list every one of them explicitly** — in elementary-divisor form, and also in invariant-factor form.
2. Justify the counting formula: explain why the number of abelian [[Def - Group|groups]] of order $n=p_1^{a_1}\cdots p_k^{a_k}$ is $p(a_1)\cdot p(a_2)\cdots p(a_k)$, where $p(\,\cdot\,)$ is the integer **partition function** ($p(m)$ = number of ways to write $m$ as a sum of positive integers, order disregarded).

For $600=2^3\cdot 3\cdot 5^2$ the answer is $p(3)\cdot p(1)\cdot p(2)=3\cdot 1\cdot 2=6$.

This is the standard "count the abelian groups of order $n$" problem: a direct payoff of the classification theorem, reducing a group-theoretic census to elementary combinatorics — counting partitions of prime exponents.

**Recall:**

The classification of finite abelian groups is what makes the count finite and computable.

![[Thm - Classification of Finitely Generated Abelian Groups#Statement]]

So every finite abelian group has a *unique* invariant-factor form $C_{d_1}\times\cdots\times C_{d_s}$ with $d_1\mid\cdots\mid d_s$. Equivalently — splitting each $d_i$ into prime powers by the Chinese remainder theorem — it has a unique **elementary-divisor form**, a product of cyclic groups of prime-power order.

![[Thm - Chinese Remainder Theorem for Modules#Statement]]

Because $C_n\cong\prod_i C_{p_i^{a_i}}$ when $n=\prod p_i^{a_i}$, a group of order $n=p_1^{a_1}\cdots p_k^{a_k}$ splits canonically as a product of its **$p$-primary parts** $A=A_{p_1}\times\cdots\times A_{p_k}$, where $A_{p_i}$ is the abelian group whose order is the prime power $p_i^{a_i}$. Choosing $A$ is therefore the same as independently choosing each $A_{p_i}$.

The **partition function** $p(m)$ counts the partitions of the positive integer $m$: the ways to write $m=m_1+m_2+\cdots+m_r$ with $m_1\ge m_2\ge\cdots\ge m_r\ge 1$. The first values are $p(1)=1$, $p(2)=2$, $p(3)=3$, $p(4)=5$, $p(5)=7$.

---

# Convergent Strategy

**Problem class.** This is a *classification census* — count, up to isomorphism, the structures of a given size. The classification theorem turns it from an open-ended search into a finite, mechanical enumeration.

**Assumption pattern.** The hypothesis is a single integer $n$ and the word "abelian". The decisive feature is the *prime factorisation* of $n$: the exponents $a_1,\dots,a_k$ are the only data that matter; the primes themselves are irrelevant to the *count* (though they appear in the explicit list).

**Theorem routing.** [[Thm - Classification of Finitely Generated Abelian Groups]] says each group is uniquely a product of cyclic factors. [[Thm - Chinese Remainder Theorem for Modules]] decouples the primes: a group of order $n$ is uniquely $A_{p_1}\times\cdots\times A_{p_k}$ with $|A_{p_i}|=p_i^{a_i}$. So the total count is the *product* over primes of the count of abelian groups of order $p^a$ — and that per-prime count is exactly the number of partitions of the exponent $a$.

**Key decision point.** The one insight that makes the problem trivial is: *abelian groups of order $p^a$ correspond bijectively to partitions of $a$.* A group of order $p^a$ is a product $C_{p^{a_1}}\times\cdots\times C_{p^{a_r}}$ of cyclic $p$-power groups, and uniqueness means the only freedom is the multiset of exponents $\{a_1,\dots,a_r\}$ with $\sum a_i=a$ — i.e. a partition of $a$. Recognising this converts "count groups" into "count partitions", and the prime-by-prime independence (Chinese remainder theorem) turns the global count into a product. Everything else is reading off $p(a)$ for small $a$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Modules II — §3.3–3.4#Legal Operations|the topic page's Legal Operations]]:

1. **Factor the order and split into $p$-primary parts.** Write $n=\prod p_i^{a_i}$; by the Chinese remainder theorem a group of order $n$ is uniquely $\prod_i A_{p_i}$ with $|A_{p_i}|=p_i^{a_i}$. This decouples the classification across primes.

2. **Identify $p$-groups with partitions.** An abelian group of order $p^a$ is $\prod_j C_{p^{a_j}}$ with $\sum_j a_j=a$ and $a_1\ge a_2\ge\cdots$; the data is exactly a partition of $a$.

3. **Multiply per-prime counts.** Since the choices of $A_{p_i}$ are independent, the number of abelian groups of order $n$ is $\prod_i p(a_i)$.

4. **Enumerate partitions of small integers.** List the partitions of each exponent $a_i$ explicitly to produce, not merely count, every group.

5. **Convert elementary-divisor form to invariant-factor form** via the right-aligned exponent grid, so each group is also displayed as a divisibility chain $C_{d_1}\times\cdots\times C_{d_s}$.

---

# Hints

> [!note]- Hint 1
> First factor $600$ into primes. Then use the Chinese remainder theorem: a finite abelian group splits uniquely as a product of its $p$-primary parts, one for each prime dividing the order. So choosing an abelian group of order $600$ is the same as *independently* choosing an abelian group of order $2^3$, one of order $3^1$, and one of order $5^2$.

> [!note]- Hint 2
> How many abelian groups have order $p^a$ (a prime power)? Such a group is a product $C_{p^{a_1}}\times\cdots\times C_{p^{a_r}}$ of cyclic $p$-power factors, and by uniqueness in the classification theorem the only freedom is the multiset of exponents $a_1\ge\cdots\ge a_r\ge 1$ with $a_1+\cdots+a_r=a$. That is precisely a *partition* of $a$.

> [!note]- Hint 3
> So the number of abelian groups of order $p^a$ is $p(a)$, the partition function, and by independence across primes the total for $n=\prod p_i^{a_i}$ is $\prod_i p(a_i)$. You need $p(3)$, $p(1)$, $p(2)$. List the partitions: of $1$ there is $1$; of $2$ there are $2$ ($2$ and $1{+}1$); of $3$ there are $3$ ($3$, $2{+}1$, $1{+}1{+}1$).

> [!note]- Hint 4
> The total is $p(3)\cdot p(1)\cdot p(2)=3\cdot 1\cdot 2=6$. To *list* the six groups, take each of the $3$ choices for the order-$8$ part — $C_8$, $C_4\times C_2$, $C_2\times C_2\times C_2$ — and pair it with the forced $C_3$ and one of the $2$ choices for the order-$25$ part, $C_{25}$ or $C_5\times C_5$.

---

# Solution

The strategy is: factor the order, decouple the primes by the Chinese remainder theorem, identify each $p$-primary part with a partition, multiply the counts, and enumerate.

**Step 1: Factor the order and decouple the primes.**

$600=2^3\cdot 3\cdot 5^2$. By the Chinese remainder theorem a finite abelian group of order $600$ is *uniquely* a product $A_2\times A_3\times A_5$ of its $p$-primary parts, with $|A_2|=8$, $|A_3|=3$, $|A_5|=25$.

> [!note]- Derivation
> First, $600=8\cdot 75=8\cdot 3\cdot 25=2^3\cdot 3^1\cdot 5^2$.
>
> Let $A$ be any abelian group with $|A|=600$. By [[Thm - Classification of Finitely Generated Abelian Groups|the classification]], $A$ is a product of cyclic groups; grouping the cyclic factors by the prime dividing their order and using [[Thm - Chinese Remainder Theorem for Modules|the Chinese remainder theorem]] (which merges and splits cyclic groups along coprime factorisations), $A$ decomposes uniquely as
> $$A\cong A_2\times A_3\times A_5,$$
> where $A_p$, the **$p$-primary part**, is the product of those cyclic factors of $p$-power order. By Lagrange-type counting of orders, $|A_2|\cdot|A_3|\cdot|A_5|=|A|=600$, and since $A_p$ is a $p$-group its order is the full power of $p$ in $600$:
> $$|A_2|=2^3=8,\qquad |A_3|=3^1=3,\qquad |A_5|=5^2=25.$$
> Crucially, this decomposition is *unique*, and conversely *any* choice of $A_2,A_3,A_5$ with these orders assembles into a group of order $600$. So
> $$\#\{\text{abelian groups of order }600\}=\#\{A_2\}\cdot\#\{A_3\}\cdot\#\{A_5\},$$
> a product of three independent counts.

**Step 2: Count abelian groups of prime-power order — the partition correspondence.**

The abelian groups of order $p^a$ are in bijection with the partitions of $a$: a group of order $p^a$ is $C_{p^{a_1}}\times\cdots\times C_{p^{a_r}}$ with $a_1\ge\cdots\ge a_r\ge 1$ and $\sum a_i=a$. Hence there are $p(a)$ of them.

> [!note]- Derivation
> Fix a prime $p$ and exponent $a$. An abelian group $A_p$ of order $p^a$ is, by [[Thm - Classification of Finitely Generated Abelian Groups|the classification]] in elementary-divisor form, a product of cyclic groups of prime-power order; since $|A_p|=p^a$ has only the prime $p$, *every* factor is a $p$-power cyclic group:
> $$A_p\cong C_{p^{a_1}}\times C_{p^{a_2}}\times\cdots\times C_{p^{a_r}}.$$
> Taking orders, $p^{a_1}\cdot p^{a_2}\cdots p^{a_r}=p^a$, so $a_1+a_2+\cdots+a_r=a$. Order the exponents $a_1\ge a_2\ge\cdots\ge a_r\ge 1$ (each $\ge 1$ since a factor $C_{p^0}=C_1$ is trivial and dropped).
>
> The data of $A_p$ is therefore exactly the multiset $\{a_1,\dots,a_r\}$ of positive integers summing to $a$ — a **partition of $a$**. The classification theorem supplies *uniqueness*: two such products are isomorphic if and only if their exponent multisets coincide. Hence the map
> $$\{\text{abelian groups of order }p^a\}\ \longleftrightarrow\ \{\text{partitions of }a\}$$
> is a bijection, and
> $$\#\{\text{abelian groups of order }p^a\}=p(a).$$
> Notice the prime $p$ has dropped out entirely — the count depends only on the exponent $a$.

**Step 3: Assemble the count for $600$.**

The total is $p(3)\cdot p(1)\cdot p(2)=3\cdot 1\cdot 2=\boxed{6}$.

> [!note]- Derivation
> Combine Steps 1 and 2. The number of abelian groups of order $600=2^3\cdot 3^1\cdot 5^2$ is the product of the per-prime counts, each given by the partition function evaluated at the exponent:
> $$\#\{\text{order }600\}=p(3)\cdot p(1)\cdot p(2).$$
> Enumerate the partitions explicitly:
> - **$p(3)=3$:** the partitions of $3$ are $3$, $\ 2+1$, $\ 1+1+1$.
> - **$p(1)=1$:** the only partition of $1$ is $1$.
> - **$p(2)=2$:** the partitions of $2$ are $2$, $\ 1+1$.
>
> Hence
> $$\#\{\text{order }600\}=3\cdot 1\cdot 2=6.$$
> This is the special case $n=p_1^{a_1}\cdots p_k^{a_k}\Rightarrow\#=\prod_i p(a_i)$ of the general formula, valid because the $p$-primary parts are chosen independently (Step 1) and each $p$-primary part is a partition (Step 2).

**Step 4: List all six groups explicitly.**

Pair each of the $3$ groups of order $8$ with the forced $C_3$ and each of the $2$ groups of order $25$.

> [!note]- Derivation
> The order-$3$ part is forced: $p(1)=1$ means $A_3\cong C_3$ always. The choices are:
> - **Order $8=2^3$** ($p(3)=3$ options, from partitions $3,\ 2{+}1,\ 1{+}1{+}1$ of $3$):
>   $$A_2\in\{\,C_8,\quad C_4\times C_2,\quad C_2\times C_2\times C_2\,\}.$$
> - **Order $25=5^2$** ($p(2)=2$ options, from partitions $2,\ 1{+}1$ of $2$):
>   $$A_5\in\{\,C_{25},\quad C_5\times C_5\,\}.$$
>
> The six groups, in **elementary-divisor form** $A_2\times C_3\times A_5$:
>
> | # | order-$8$ part | order-$25$ part | group (elementary-divisor form) |
> |---|---|---|---|
> | 1 | $C_8$ | $C_{25}$ | $C_8\times C_3\times C_{25}$ |
> | 2 | $C_8$ | $C_5\times C_5$ | $C_8\times C_3\times C_5\times C_5$ |
> | 3 | $C_4\times C_2$ | $C_{25}$ | $C_4\times C_2\times C_3\times C_{25}$ |
> | 4 | $C_4\times C_2$ | $C_5\times C_5$ | $C_4\times C_2\times C_3\times C_5\times C_5$ |
> | 5 | $C_2\times C_2\times C_2$ | $C_{25}$ | $C_2\times C_2\times C_2\times C_3\times C_{25}$ |
> | 6 | $C_2\times C_2\times C_2$ | $C_5\times C_5$ | $C_2\times C_2\times C_2\times C_3\times C_5\times C_5$ |
>
> The same six in **invariant-factor form** $C_{d_1}\times\cdots\times C_{d_s}$ with $d_1\mid\cdots\mid d_s$, obtained by the right-aligned exponent grid (the largest invariant factor collects the top prime power of each prime):
>
> | # | invariant-factor form | check: $\prod d_i$ |
> |---|---|---|
> | 1 | $C_{600}$ | $600$ |
> | 2 | $C_5\times C_{120}$ | $5\cdot 120=600$ |
> | 3 | $C_2\times C_{300}$ | $2\cdot 300=600$ |
> | 4 | $C_{10}\times C_{60}$ | $10\cdot 60=600$ |
> | 5 | $C_2\times C_2\times C_{150}$ | $2\cdot 2\cdot 150=600$ |
> | 6 | $C_2\times C_{10}\times C_{30}$ | $2\cdot 10\cdot 30=600$ |
>
> A worked grid for group #4: prime $2$ row $(2^1,2^2)$, prime $3$ row $(3^1)$, prime $5$ row $(5^1,5^1)$; right-aligned, $d_2=2^2\cdot 3^1\cdot 5^1=60$ and $d_1=2^1\cdot 1\cdot 5^1=10$, with $10\mid 60$. A worked grid for group #6: prime $2$ row $(2^1,2^1,2^1)$, prime $3$ row $(3^1)$, prime $5$ row $(5^1,5^1)$; right-aligned to three columns, $d_3=2^1\cdot 3^1\cdot 5^1=30$, $d_2=2^1\cdot 1\cdot 5^1=10$, $d_1=2^1\cdot 1\cdot 1=2$, with $2\mid 10\mid 30$. Every group is finite (no $C_\infty$ factor) since the order is finite, and all six are pairwise non-isomorphic by the uniqueness clause of [[Thm - Classification of Finitely Generated Abelian Groups|the classification]].

> [!note]- Complete formal solution
> Factor $600=2^3\cdot 3^1\cdot 5^2$. By [[Thm - Classification of Finitely Generated Abelian Groups]] and [[Thm - Chinese Remainder Theorem for Modules]], every abelian group of order $600$ is uniquely $A_2\times A_3\times A_5$ with $|A_2|=8$, $|A_3|=3$, $|A_5|=25$, and the three factors may be chosen independently. An abelian group of order $p^a$ is a product $\prod_j C_{p^{a_j}}$ with $\sum a_j=a$, $a_1\ge\cdots\ge a_r\ge 1$; uniqueness makes such groups correspond bijectively to partitions of $a$, so there are $p(a)$ of them. Hence
> $$\#\{\text{abelian groups of order }600\}=p(3)\cdot p(1)\cdot p(2)=3\cdot 1\cdot 2=6,$$
> using $p(3)=3$ (partitions $3,\,2{+}1,\,1{+}1{+}1$), $p(1)=1$, $p(2)=2$ (partitions $2,\,1{+}1$). The six groups, in invariant-factor form: $C_{600}$, $\ C_5\times C_{120}$, $\ C_2\times C_{300}$, $\ C_{10}\times C_{60}$, $\ C_2\times C_2\times C_{150}$, $\ C_2\times C_{10}\times C_{30}$. They are pairwise non-isomorphic by uniqueness of the invariant-factor decomposition. $\blacksquare$

---

# Key Takeaways

**Counting abelian groups of order $n$ is counting partitions — the primes only contribute their exponents.** The classification theorem turns the seemingly hard question "how many groups of order $n$?" into pure combinatorics: factor $n=\prod p_i^{a_i}$, and the answer is $\prod_i p(a_i)$. The primes $p_i$ themselves are *irrelevant to the count*; only the exponents $a_i$ enter. So abelian groups of order $2^3\cdot 3\cdot 5^2$, of order $7^3\cdot 11\cdot 13^2$, and of order $p^3 q r^2$ for any distinct primes $p,q,r$ all number $p(3)p(1)p(2)=6$. The trigger "count the abelian groups of order $n$" should fire the reaction "factorise, then multiply partition numbers of the exponents". This is the cleanest illustration of a classification theorem doing real work — converting a structural census into arithmetic.

**The Chinese remainder theorem decouples a classification problem across primes.** The reason the count is a *product* $\prod_i p(a_i)$ rather than something entangled is that [[Thm - Chinese Remainder Theorem for Modules|CRT]] guarantees a finite abelian group is uniquely the product of its $p$-primary parts, and those parts can be chosen *independently*. Each prime's contribution is sealed off in its own primary component, of order the full prime power $p_i^{a_i}$, and what happens at $p_i$ has no bearing on $p_j$. This "decouple across primes, then multiply" pattern is ubiquitous: it is the same logic behind multiplicativity of the Euler totient $\varphi$, of the number-of-divisors function, and of counting solutions to congruences. Whenever a structure splits as a product over primes, count each prime's piece separately and multiply.

**Abelian $p$-groups are partitions; the two canonical forms read the partition two ways.** A group of order $p^a$ *is* a partition of $a$: the partition $a=a_1+\cdots+a_r$ (parts descending) is the elementary-divisor form $C_{p^{a_1}}\times\cdots\times C_{p^{a_r}}$. The same partition, read through the right-aligned exponent grid, yields the invariant-factor form. So "list the abelian groups of order $p^a$" and "list the partitions of $a$" are the *same task*. This is why the partition function $p(m)$ — with its values $1,2,3,5,7,11,\dots$ — is exactly the growth rate of the number of abelian $p$-groups, and why the conversion machinery of [[Ex - Invariant factors and elementary divisors]] is just relabelling a partition. When you must enumerate (not merely count) the groups, enumerate the partitions of each exponent and take all combinations.

**Every group on the list is genuinely distinct — uniqueness is doing the heavy lifting.** The count $6$ is correct only because the invariant-factor (equivalently elementary-divisor) decomposition is *unique*: two finite abelian groups are isomorphic if and only if their invariant-factor lists are identical. Without uniqueness, the enumeration might overcount — perhaps $C_4\times C_2$ secretly equals $C_8$. It does not: $C_8$ has an element of order $8$, $C_4\times C_2$ has maximal element order $4$, $C_2\times C_2\times C_2$ has maximal element order $2$. The uniqueness clause of [[Thm - Classification of Finitely Generated Abelian Groups]] certifies that distinct partitions give non-isomorphic groups, so listing partitions neither overcounts nor undercounts. The general principle: a classification theorem is only a counting tool if it includes a *uniqueness* statement — existence alone tells you the forms exist, uniqueness tells you they are distinct, and a census needs both.

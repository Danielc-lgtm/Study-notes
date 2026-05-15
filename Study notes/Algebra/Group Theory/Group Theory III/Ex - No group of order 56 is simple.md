---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Sylow p-Subgroup"
  - "Def - Simple Group"
  - "Thm - Sylow's Theorems"
  - "Thm - A Unique Sylow Subgroup is Normal"
tags: [algebra, group-theory]
---

# Problem Statement

Prove that no group of order $56$ is [[Def - Simple Group|simple]].

**Recall:**

The objects in play are Sylow subgroups, simplicity, the Sylow count, and the element-counting consequence of prime-order Sylow subgroups.

![[Def - Sylow p-Subgroup#The Definition]]

Here $|G| = 56 = 2^3 \cdot 7$. The prime $2$ appears to the *third* power, so a Sylow $2$-subgroup has order $2^3 = 8$. The prime $7$ appears to the *first* power, so a Sylow $7$-subgroup has order $7$ — it is cyclic, with all $6$ non-identity elements of order $7$.

![[Def - Simple Group#The Definition]]

The two clauses of [[Thm - Sylow's Theorems|Sylow's theorems]] used are the count and its consequence. Sylow III says the number $n_p$ of Sylow $p$-subgroups satisfies $n_p \equiv 1 \pmod p$ and $n_p \mid m$, where $|G| = p^a m$. And:

![[Thm - A Unique Sylow Subgroup is Normal#Statement]]

The element-counting step uses the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]]: when a prime $p$ divides $|G|$ but $p^2$ does not, distinct Sylow $p$-subgroups intersect only in the identity, so $G$ has exactly $n_p(p-1)$ elements of order $p$. Note this applies to the prime $7$ here, but **not** to $2$, since $2^3 \mid 56$.

---

# Convergent Strategy

**Problem class.** This is a *non-simplicity* problem, the dominant target of [[Group Theory III — §1.5–1.7#Sources and Targets|the topic]]. As with order $30$, the first step of the playbook — force some $n_p = 1$ from the arithmetic alone — does not finish: the constraints permit $n_7 > 1$ and $n_2 > 1$. The exercise drills the **element-counting** tactic again, but in its sharper *leftover-room* form: instead of overflowing $G$ with too many elements, we count the order-$7$ elements and observe that the *complement* is exactly the right size to be a single Sylow $2$-subgroup.

**Assumption pattern.** The factorization $56 = 2^3 \cdot 7$ is *not* square-free — $2$ appears cubed. So element-counting is available **only for the prime $7$**, the one appearing to the first power. The Sylow $2$-subgroups, of order $8$, can overlap and cannot be counted by the prime-order formula. The asymmetry between the two primes — one countable, one not — is what shapes the argument: count $7$, and corner $2$.

**Theorem routing.** The route runs by cases on $n_7$. By [[Thm - Sylow's Theorems|Sylow III]], $n_7 \equiv 1 \pmod 7$ and $n_7 \mid 8$, which leaves only $n_7 \in \{1, 8\}$. If $n_7 = 1$, the unique Sylow $7$-subgroup is [[Thm - A Unique Sylow Subgroup is Normal|normal]] and we are done immediately. If $n_7 = 8$, the [[Ex - Counting elements of prime order with Sylow subgroups|counting fact]] gives $8 \cdot 6 = 48$ elements of order $7$. That leaves $56 - 48 = 8$ elements of $G$ not of order $7$. A Sylow $2$-subgroup has order $8$ and contains *no* elements of order $7$ (their orders divide $8$), so it must consist entirely of those $8$ leftover elements — there is room for *only one* Sylow $2$-subgroup, forcing $n_2 = 1$, and the unique Sylow $2$-subgroup is normal.

**Key decision point.** The non-obvious move is the *leftover-room* count rather than an *overflow* count. With only one first-power prime, $7$, there is no second population of elements to add and overflow $|G|$ with — the order-$30$ trick is unavailable. Instead one counts a single population, the $48$ elements of order $7$, and reasons about the *complement*: the $8$ remaining elements. The decisive observation is that a Sylow $2$-subgroup, having order $8$ and being a $2$-group, contains *no element of order $7$*, so it is forced to live entirely inside the $8$-element complement — and an $8$-element subgroup inside an $8$-element set is *unique*. Recognising that "complement has exactly $|P|$ elements" forces $n_2 = 1$ is the heart of the exercise.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory III — §1.5–1.7#Legal Operations|the topic page's Legal Operations]]:

1. **Factor the order and write down the Sylow constraints** (operation 1). The order $56 = 2^3 \cdot 7$ is factored, and for the prime $7$ the constraints $n_7 \equiv 1 \pmod 7$, $n_7 \mid 8$ are written down, leaving $n_7 \in \{1, 8\}$.

2. **Conclude normality from a unique Sylow subgroup** (operation 2). Used twice — once in the case $n_7 = 1$ directly, and once at the end of the case $n_7 = 8$ when the count forces $n_2 = 1$. Either way [[Thm - A Unique Sylow Subgroup is Normal]] supplies the proper non-trivial normal subgroup.

3. **Count elements of prime order** (operation 3). Since $7$ appears to the first power, the [[Ex - Counting elements of prime order with Sylow subgroups|counting fact]] gives $n_7(7-1) = 48$ elements of order $7$ in the case $n_7 = 8$. The complement is then sized against a Sylow $2$-subgroup. The operation is *not* applied to the prime $2$, whose Sylow subgroups have order $8 > 2$.

---

# Hints

> [!note]- Hint 1
> Factor $56$ and write the Sylow constraints for $7$. They leave exactly two candidates for $n_7$. One of them finishes the problem at once — which? Treat the other as a case to be handled separately.

> [!note]- Hint 2
> Suppose $n_7 = 8$. The prime $7$ appears to the first power, so the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]] applies: how many elements of order $7$ does $G$ have? Subtract from $56$. How many elements are left over?

> [!note]- Hint 3
> A Sylow $2$-subgroup has order $8$, and every element in it has order a power of $2$ — so it contains *no* element of order $7$. There are exactly $56 - 48 = 8$ elements of $G$ that are not of order $7$. A Sylow $2$-subgroup, with its $8$ elements, must be *precisely* this set of $8$. So there is room for only one — $n_2 = 1$ — and the Sylow $2$-subgroup is [[Thm - A Unique Sylow Subgroup is Normal|normal]].

---

# Solution

The plan is a case split on $n_7$. The Sylow constraints leave $n_7 \in \{1, 8\}$. The case $n_7 = 1$ finishes immediately; the case $n_7 = 8$ is settled by counting the order-$7$ elements and showing the $8$-element complement is forced to be the unique Sylow $2$-subgroup.

**Step 1: The Sylow constraints leave $n_7 \in \{1, 8\}$.**

For the prime $7$, write $|G| = 7^1 \cdot 8$. Sylow III gives $n_7 \mid 8$ and $n_7 \equiv 1 \pmod 7$; the only divisors of $8$ congruent to $1$ modulo $7$ are $1$ and $8$.

> [!note]- Derivation
> Factor $|G| = 56 = 2^3 \cdot 7$. With respect to the prime $7$, the largest power of $7$ dividing $56$ is $7^1$, so $|G| = 7^a m$ with $a = 1$ and $m = 8$.
>
> By [[Thm - Sylow's Theorems|Sylow's third theorem]], $n_7 \mid m = 8$ and $n_7 \equiv 1 \pmod 7$. The divisors of $8$ are $1, 2, 4, 8$. Reducing modulo $7$: $1 \equiv 1$, $2 \equiv 2$, $4 \equiv 4$, $8 \equiv 1$. So the divisors congruent to $1 \pmod 7$ are exactly $1$ and $8$. Hence
> $$n_7 \in \{1, 8\}.$$

**Step 2: If $n_7 = 1$, the unique Sylow $7$-subgroup is normal — done.**

A unique Sylow $7$-subgroup is [[Thm - A Unique Sylow Subgroup is Normal|normal]]; it has order $7$, so it is proper and non-trivial, and $G$ is not simple.

> [!note]- Derivation
> Suppose $n_7 = 1$. Let $P$ be the unique Sylow $7$-subgroup. By [[Thm - A Unique Sylow Subgroup is Normal]], $P$ is [[Def - Normal Subgroup|normal]] in $G$: every conjugate $gPg^{-1}$ is a Sylow $7$-subgroup, and uniqueness forces $gPg^{-1} = P$.
>
> Now $|P| = 7$, so $P \neq \{e\}$ (as $7 > 1$) and $P \neq G$ (as $7 < 56$). Thus $P$ is a proper non-trivial normal subgroup, and by the definition of a [[Def - Simple Group|simple group]], $G$ is not simple. This case is complete.

**Step 3: If $n_7 = 8$, there are $48$ elements of order $7$, leaving an $8$-element complement.**

By the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]], $n_7 = 8$ gives $8 \cdot 6 = 48$ elements of order $7$. The remaining $56 - 48 = 8$ elements of $G$ have order *not* equal to $7$.

> [!note]- Derivation
> Suppose instead $n_7 = 8$. The prime $7$ divides $|G| = 56$ but $7^2 = 49$ does not, so the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]] applies: every Sylow $7$-subgroup has order $7$, distinct ones intersect only in the identity, and the number of elements of order $7$ is exactly
> $$n_7 (7 - 1) = 8 \cdot 6 = 48.$$
>
> (For self-containedness: each Sylow $7$-subgroup is cyclic of order $7$ with $6$ non-identity elements, all of order $7$; two distinct ones $P \neq Q$ have $P \cap Q$ a subgroup of $P$ of order dividing $7$, hence $\{e\}$, so the $8$ subgroups contribute disjoint sets of $6$.)
>
> Let $E$ be the set of these $48$ elements of order $7$. Its complement in $G$,
> $$L := G \setminus E,$$
> has $|L| = 56 - 48 = 8$. Every element of $L$ has order $\neq 7$. (Note $L$ contains the identity, which has order $1$.)

**Step 4: The $8$-element complement is forced to be the unique Sylow $2$-subgroup, so $n_2 = 1$ — done.**

A Sylow $2$-subgroup has order $8$ and contains no element of order $7$, so it lies inside the $8$-element set $L$; being of size $8$ it *equals* $L$. Hence there is exactly one Sylow $2$-subgroup, $n_2 = 1$, and it is normal.

> [!note]- Derivation
> Let $Q$ be any Sylow $2$-subgroup of $G$. With respect to the prime $2$, $|G| = 2^3 \cdot 7$, so $|Q| = 2^3 = 8$.
>
> Every element $x \in Q$ has order dividing $|Q| = 8$ by [[Thm - Lagrange's Theorem|Lagrange]], so $\operatorname{ord}(x) \in \{1, 2, 4, 8\}$. In particular *no* element of $Q$ has order $7$. Therefore $Q \cap E = \emptyset$, which means $Q \subseteq G \setminus E = L$.
>
> But $|Q| = 8 = |L|$, and $Q \subseteq L$. A subset of an $8$-element set that itself has $8$ elements is the whole set, so
> $$Q = L.$$
>
> This identity holds for *every* Sylow $2$-subgroup $Q$ — each of them equals the one fixed set $L$. So there is exactly one Sylow $2$-subgroup, i.e. $n_2 = 1$.
>
> By [[Thm - A Unique Sylow Subgroup is Normal]], this unique Sylow $2$-subgroup is [[Def - Normal Subgroup|normal]]. It has order $8$, so it is proper ($8 < 56$) and non-trivial ($8 > 1$). Hence $G$ has a proper non-trivial normal subgroup and is not [[Def - Simple Group|simple]].
>
> In *both* cases — $n_7 = 1$ and $n_7 = 8$ — the group $G$ has been shown to have a normal Sylow subgroup. Therefore no group of order $56$ is simple. $\blacksquare$

> [!note]- Complete formal solution
> Let $|G| = 56 = 2^3 \cdot 7$.
>
> With respect to $7$, $|G| = 7^1 \cdot 8$. By [[Thm - Sylow's Theorems|Sylow III]], $n_7 \mid 8$ and $n_7 \equiv 1 \pmod 7$; the divisors of $8$ congruent to $1$ modulo $7$ are $1$ and $8$, so $n_7 \in \{1, 8\}$.
>
> *Case $n_7 = 1$.* The unique [[Def - Sylow p-Subgroup|Sylow $7$-subgroup]] is [[Thm - A Unique Sylow Subgroup is Normal|normal]]; it has order $7$, so it is a proper non-trivial normal subgroup, and $G$ is not [[Def - Simple Group|simple]].
>
> *Case $n_7 = 8$.* Since $7$ divides $56$ to the first power, distinct Sylow $7$-subgroups (each of order $7$, hence cyclic) intersect only in $\{e\}$, so the number of elements of order $7$ is exactly $n_7(7-1) = 8 \cdot 6 = 48$. Call this set $E$; then $L := G \setminus E$ has $|L| = 56 - 48 = 8$, and every element of $L$ has order $\neq 7$.
>
> Let $Q$ be any Sylow $2$-subgroup; $|Q| = 2^3 = 8$. By [[Thm - Lagrange's Theorem|Lagrange]] every element of $Q$ has order dividing $8$, so $Q$ contains no element of order $7$, giving $Q \subseteq L$. As $|Q| = 8 = |L|$, we get $Q = L$. This holds for every Sylow $2$-subgroup, so $n_2 = 1$. By [[Thm - A Unique Sylow Subgroup is Normal]] the unique Sylow $2$-subgroup is normal; it has order $8$, so it is proper and non-trivial, and $G$ is not simple.
>
> In either case $G$ is not simple. $\blacksquare$

---

# Key Takeaways

**When only one prime appears to the first power, count it and reason about the complement — the leftover-room argument.** The order-$30$ proof had three first-power primes and worked by *overflow*: two element-populations summed to more than $|G|$. Order $56$ has only *one* first-power prime, $7$, so there is no second population to overflow with. The adaptation is to count the single population — the $48$ elements of order $7$ — and study the *complement*, the $56 - 48 = 8$ remaining elements. The decisive fact is that a Sylow $2$-subgroup, being a $2$-group, contains no element of order $7$, so it is trapped inside the complement; and when the complement has *exactly* $|Q|$ elements, the Sylow $2$-subgroup must *be* the complement, which forces $n_2 = 1$. The reusable trigger: an order with exactly one first-power prime $p$, where the count $n_p(p-1)$ leaves a complement whose size matches $|Q|$ for the Sylow subgroup $Q$ of another prime. Then the complement *is* that Sylow subgroup, uniquely.

**Element-counting applies only to first-power primes — the formula $n_p(p-1)$ is silent about the prime $2$ here.** The factorization $56 = 2^3 \cdot 7$ is not square-free, and this restricts which primes can be counted. For $7$, which appears to the first power, distinct Sylow subgroups intersect trivially and the count $n_7(7-1)$ is exact. For $2$, which appears *cubed*, two Sylow $2$-subgroups of order $8$ can share a subgroup of order $2$ or $4$, so there is no clean formula for the number of elements of order $2$ — the [[Group Theory III — §1.5–1.7#Legal Operations|topic-page warning]] against assuming trivial intersection for higher-power primes applies in full. The discipline: before invoking $n_p(p-1)$, check that $p$ appears to the *first* power in $|G|$. Here that check licenses counting $7$ and forbids counting $2$ — and the proof respects this exactly, deriving $n_2 = 1$ not by counting Sylow $2$-subgroups but by *cornering* them inside a set that has no room for two.

**A proof by cases is complete only when every case ends in a normal subgroup — and "$n_p = 1$" is a perfectly good case to *land on*, not just to start from.** The argument splits on $n_7 \in \{1, 8\}$, and the two branches close differently: the first by an immediate appeal to [[Thm - A Unique Sylow Subgroup is Normal]], the second by a counting argument that *concludes* with $n_2 = 1$ and *then* the same appeal. The lesson is that the goal of a non-simplicity proof — exhibit a normal subgroup — can be reached at different primes in different cases, and the proof is finished only when *every* branch has produced one. It is a common error to handle the easy case ($n_7 = 1$), find a normal subgroup, and stop, forgetting that the hard case ($n_7 = 8$) is still open. Both cases must terminate in a normal Sylow subgroup. Note also that, unlike the order-$30$ proof, this argument never *assumes* simplicity for contradiction — it directly produces a normal subgroup in each case, which is the cleaner style when a case split is available.

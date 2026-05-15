---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Sylow p-Subgroup"
  - "Def - Simple Group"
  - "Def - Normal Subgroup"
  - "Thm - Sylow's Theorems"
  - "Thm - A Unique Sylow Subgroup is Normal"
tags: [algebra, group-theory]
---

# Problem Statement

Let $p < q$ be prime numbers and let $G$ be a group of order $|G| = pq$. Prove that $G$ has a normal [[Def - Sylow p-Subgroup|Sylow $q$-subgroup]]. Conclude that $G$ is not [[Def - Simple Group|simple]].

**Recall:**

The objects in play are Sylow subgroups, simplicity, and the consequence of a Sylow count of $1$.

![[Def - Sylow p-Subgroup#The Definition]]

Here $|G| = pq$ with $p < q$ both prime. For the prime $q$ the factorization $|G| = q^a m$ has $a = 1$ and $m = p$ (since $q \nmid p$, as $p < q$), so a Sylow $q$-subgroup has order $q$.

![[Def - Simple Group#The Definition]]

The two clauses of [[Thm - Sylow's Theorems|Sylow's theorems]] this problem uses are the *count* and what it implies. Sylow III says the number $n_q$ of Sylow $q$-subgroups satisfies $n_q \equiv 1 \pmod q$ and $n_q \mid m$, where $|G| = q^a m$. And:

![[Thm - A Unique Sylow Subgroup is Normal#Statement]]

So if the arithmetic forces $n_q = 1$, the unique Sylow $q$-subgroup is normal, and being a proper (it has order $q < pq$) non-trivial (order $q > 1$) normal subgroup, it witnesses that $G$ is not simple.

---

# Convergent Strategy

**Problem class.** This is the prototype *non-simplicity* problem, the dominant target of the topic as set out in the [[Group Theory III — §1.5–1.7#Sources and Targets|Sources and Targets]] section. It is the cleanest possible instance: the order is a product of two distinct primes, and the non-simplicity is settled at the very first step of the playbook, with no element-counting and no group actions required. It is the calibration case — if any non-simplicity argument is going to be a one-liner, this is it.

**Assumption pattern.** The hypothesis is entirely numerical: $|G| = pq$ with $p < q$ prime. The *ordering* $p < q$ is not decorative — it is the load-bearing assumption. The Sylow constraints on $n_q$ are $n_q \equiv 1 \pmod q$ and $n_q \mid p$. The divisor condition leaves only $n_q \in \{1, p\}$, and the congruence then asks which of $1$ and $p$ is $\equiv 1 \pmod q$. Because $p < q$, the value $p$ lies strictly between $1$ and $q$, so $p \not\equiv 1 \pmod q$ — there is no room for $p - 1$ to be a positive multiple of $q$. The ordering is exactly what kills the candidate $n_q = p$.

**Theorem routing.** The route is the standard two-step composition: [[Thm - Sylow's Theorems|Sylow III]] to force $n_q = 1$, then [[Thm - A Unique Sylow Subgroup is Normal|a unique Sylow subgroup is normal]] to convert that count into a normal subgroup. A normal subgroup of order $q$ in a group of order $pq$ is proper and non-trivial, so by the definition of [[Def - Simple Group|simplicity]], $G$ is not simple.

**Key decision point.** The one choice that makes the proof work is *to test the larger prime $q$, not the smaller prime $p$*. The asymmetry is genuine. For $q$, the divisor condition $n_q \mid p$ leaves only $\{1, p\}$ and the congruence eliminates $p$. For $p$, the divisor condition is $n_p \mid q$, leaving $\{1, q\}$, and the congruence $n_p \equiv 1 \pmod p$ may well *permit* $n_p = q$ (it does whenever $p \mid q - 1$, as for $|G| = 6$ where $n_3 = 1$ but $n_2$ can be $3$). The Sylow $p$-subgroup need not be normal. Picking the right prime — always the largest — is the heart of the technique, and it generalises far beyond this problem.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory III — §1.5–1.7#Legal Operations|the topic page's Legal Operations]]:

1. **Factor the order and write down the Sylow constraints** (operation 1). The order $pq$ is factored, and for the prime $q$ the constraints $n_q \equiv 1 \pmod q$ and $n_q \mid p$ are written down. Their common solutions are enumerated.

2. **Conclude normality from a unique Sylow subgroup** (operation 2). Once the constraints force $n_q = 1$, the unique Sylow $q$-subgroup is declared normal by [[Thm - A Unique Sylow Subgroup is Normal]], producing the proper non-trivial normal subgroup that defeats simplicity.

---

# Hints

<details>
<summary>Hint 1</summary>

Do not test both primes. Non-simplicity needs only *one* prime with a unique Sylow subgroup. Which of $p$ and $q$ is more constrained? Write out the Sylow constraints for each and compare how many candidate values survive.

</details>

<details>
<summary>Hint 2</summary>

For the prime $q$: the count $n_q$ must divide $m = p$, so $n_q \in \{1, p\}$. It must also satisfy $n_q \equiv 1 \pmod q$. Use the hypothesis $p < q$ to decide whether $p$ can be $\equiv 1 \pmod q$.

</details>

<details>
<summary>Hint 3</summary>

Since $1 < p < q$, the integer $p$ is strictly between $1$ and $q$, so $p \not\equiv 1 \pmod q$ — there is no positive multiple of $q$ equal to $p - 1$. Hence $n_q = 1$. A unique Sylow $q$-subgroup is [[Thm - A Unique Sylow Subgroup is Normal|normal]]; it has order $q$, so it is proper and non-trivial, and $G$ is not simple.

</details>

---

# Solution

The plan is the first step of the non-simplicity playbook: factor $|G| = pq$, apply the Sylow constraints to the *larger* prime $q$, find that only $n_q = 1$ survives, and conclude normality.

**Step 1: The Sylow constraints leave $n_q \in \{1, p\}$.**

For the prime $q$, write $|G| = q^1 \cdot p$. Sylow III says $n_q \mid p$, so $n_q$ is $1$ or $p$.

<details>
<summary>Derivation</summary>

Factor $|G| = pq$ with respect to the prime $q$: since $q$ is prime and $q \nmid p$ (because $0 < p < q$ means $p$ cannot be a multiple of $q$), the largest power of $q$ dividing $|G|$ is $q^1$, and we have $|G| = q^a m$ with $a = 1$ and $m = p$.

By [[Thm - Sylow's Theorems|Sylow's third theorem]], the number $n_q = |\operatorname{Syl}_q(G)|$ of Sylow $q$-subgroups satisfies
$$n_q \mid m = p.$$
Since $p$ is prime, its only positive divisors are $1$ and $p$. Hence $n_q \in \{1, p\}$.

</details>

**Step 2: The congruence eliminates $n_q = p$, so $n_q = 1$.**

Sylow III also says $n_q \equiv 1 \pmod q$. Since $1 < p < q$, the value $p$ is not congruent to $1$ modulo $q$. So $n_q \neq p$, and the only surviving candidate is $n_q = 1$.

<details>
<summary>Derivation</summary>

[[Thm - Sylow's Theorems|Sylow III]] also imposes the congruence
$$n_q \equiv 1 \pmod q.$$
We test the two candidates from Step 1.

The candidate $n_q = 1$ satisfies the congruence trivially: $1 \equiv 1 \pmod q$.

The candidate $n_q = p$ would require $p \equiv 1 \pmod q$, that is, $q \mid (p - 1)$. But $p$ is a prime with $p < q$, so $1 \leq p - 1 < q - 1 < q$. A positive multiple of $q$ is at least $q$, and $p - 1$ is strictly smaller than $q$; the only way out would be $p - 1 = 0$, i.e. $p = 1$, which is not prime. So $q \nmid (p - 1)$, and $p \not\equiv 1 \pmod q$.

Thus $n_q = p$ violates the congruence and is rejected. The only value satisfying *both* Sylow constraints is
$$n_q = 1.$$

</details>

**Step 3: The unique Sylow $q$-subgroup is normal, so $G$ is not simple.**

With $n_q = 1$ there is exactly one Sylow $q$-subgroup; by [[Thm - A Unique Sylow Subgroup is Normal]] it is normal. It has order $q$, so it is a proper non-trivial normal subgroup, and $G$ is not simple.

<details>
<summary>Derivation</summary>

Let $P$ be the unique Sylow $q$-subgroup of $G$ (it exists by [[Thm - Sylow's Theorems|Sylow I]], and there is exactly one by Step 2). By [[Thm - A Unique Sylow Subgroup is Normal]], a Sylow subgroup that is the only one of its kind is [[Def - Normal Subgroup|normal]]: any conjugate $gPg^{-1}$ is again a Sylow $q$-subgroup (conjugation preserves order), and uniqueness forces $gPg^{-1} = P$ for all $g$, which is exactly normality. So $P \trianglelefteq G$.

Now $|P| = q$. Since $q > 1$, the subgroup $P$ is non-trivial: $P \neq \{e\}$. Since $q < pq = |G|$ (because $p > 1$), the subgroup $P$ is proper: $P \neq G$.

A group is [[Def - Simple Group|simple]] precisely when its only normal subgroups are $\{e\}$ and itself. We have exhibited a normal subgroup $P$ that is neither. Therefore $G$ is **not simple**. $\blacksquare$

</details>

<details>
<summary><strong>Complete formal solution</strong></summary>

Let $p < q$ be primes and $|G| = pq$.

With respect to the prime $q$, write $|G| = q^a m$. Since $q \nmid p$ (as $0 < p < q$), we have $a = 1$ and $m = p$. By [[Thm - Sylow's Theorems|Sylow's third theorem]], the number $n_q$ of [[Def - Sylow p-Subgroup|Sylow $q$-subgroups]] satisfies $n_q \mid p$ and $n_q \equiv 1 \pmod q$.

From $n_q \mid p$ and $p$ prime, $n_q \in \{1, p\}$. The candidate $n_q = p$ would require $q \mid (p - 1)$; but $0 < p - 1 < q$, so no positive multiple of $q$ equals $p - 1$, and this is impossible. Hence $n_q = 1$.

By [[Thm - A Unique Sylow Subgroup is Normal]], the unique Sylow $q$-subgroup $P$ is [[Def - Normal Subgroup|normal]] in $G$. It has order $q$, so $\{e\} \neq P \neq G$ (using $q > 1$ and $q < pq$). Thus $P$ is a proper non-trivial normal subgroup, and by the definition of a [[Def - Simple Group|simple group]], $G$ is not simple. $\blacksquare$

</details>

---

# Key Takeaways

**Always test the largest prime first — the divisibility constraint is tightest there.** The whole proof turns on a single judicious choice: examine the prime $q$, not $p$. The reason is structural and worth carrying to every non-simplicity problem. The Sylow count $n_p$ for a prime $p$ in $|G| = p^a m$ must divide $m$, which is $|G|$ with the $p$-part stripped out. When $p$ is the *largest* prime divisor, $m$ is built from *smaller* primes, so its divisors are small, and the congruence $n_p \equiv 1 \pmod p$ — which forces $n_p$ to be $1$ or at least $1 + p$ — then has very little room to admit anything but $1$. For the largest prime, $1 + p$ already exceeds many of the available divisors of $m$. So the heuristic is: in any non-simplicity problem, factor $|G|$ and attack the *largest* prime divisor first; it is the most likely to yield $n_p = 1$ outright. Only if it does not should you move down the list of primes or switch tactics.

**A Sylow count of $1$ is the cheapest possible certificate of non-simplicity.** This problem is the template for the two-step move that ends a large fraction of non-simplicity arguments: get some $n_p = 1$ from the arithmetic, then cite [[Thm - A Unique Sylow Subgroup is Normal]] to upgrade the count into a normal subgroup. A unique Sylow $p$-subgroup is automatically normal — its conjugates are Sylow $p$-subgroups, and uniqueness leaves nowhere for them to go but back to itself. Crucially the resulting subgroup is *automatically* proper and non-trivial: it has order $p^a$ with $1 \leq a < $ (the exponent making it all of $G$), so it never accidentally equals $\{e\}$ or $G$. This means the only real work in such a problem is the arithmetic of forcing $n_p = 1$; once that is done, non-simplicity follows mechanically. Recognising that "$n_p = 1$" and "not simple" are essentially synonymous, given a single normal-subgroup-producing prime, is the single most reusable insight of the topic.

**The ordering of the primes is a hypothesis, not a labelling convention.** It is tempting to read "$p < q$" as a harmless way of naming the two primes, but it is doing essential work: it is precisely the inequality $p < q$ that makes $p \not\equiv 1 \pmod q$ and so kills the candidate $n_q = p$. Drop the ordering and the argument collapses — for the *smaller* prime there genuinely can be more than one Sylow subgroup, as $S_3$ (order $6 = 2 \cdot 3$) shows with its three Sylow $2$-subgroups. The transferable lesson is to treat every numerical inequality in a hypothesis as potentially load-bearing and to locate, explicitly, the step where it is consumed. Here it is consumed in the single line "$0 < p - 1 < q$, so $q \nmid (p-1)$" — and identifying that line is identifying the spine of the proof. More broadly: groups of order $pq$ with $p < q$ are never simple, and in fact always have a normal Sylow $q$-subgroup, so they are semidirect products $C_q \rtimes C_p$ — the smallest interesting family of non-abelian groups after the prime-order and $p^2$ cases.

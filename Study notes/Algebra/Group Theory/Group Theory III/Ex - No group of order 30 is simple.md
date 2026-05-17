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

Prove that no group of order $30$ is [[Def - Simple Group|simple]].

**Recall:**

The objects in play are Sylow subgroups, simplicity, the Sylow count, and the element-counting consequence of prime-order Sylow subgroups.

![[Def - Sylow p-Subgroup#The Definition]]

Here $|G| = 30 = 2 \cdot 3 \cdot 5$. Each prime $2, 3, 5$ divides $30$ to the *first power only*, so every Sylow subgroup — $2$-, $3$-, or $5$- — has prime order, and is therefore cyclic with all non-identity elements of that prime order.

![[Def - Simple Group#The Definition]]

The two clauses of [[Thm - Sylow's Theorems|Sylow's theorems]] used are the count and its consequence. Sylow III says the number $n_p$ of Sylow $p$-subgroups satisfies $n_p \equiv 1 \pmod p$ and $n_p \mid m$, where $|G| = p^a m$. And:

![[Thm - A Unique Sylow Subgroup is Normal#Statement]]

The element-counting step uses the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]]: when a prime $p$ divides $|G|$ but $p^2$ does not, distinct Sylow $p$-subgroups intersect only in the identity, so $G$ has exactly $n_p(p-1)$ elements of order $p$.

---

# Convergent Strategy

**Problem class.** This is a *non-simplicity* problem, the dominant target of [[Group Theory III — §1.5–1.7#Sources and Targets|the topic]]. But unlike the groups of order $pq$, the first step of the playbook — find a prime with $n_p = 1$ forced — does *not* finish the job: assuming simplicity, the constraints permit $n_p > 1$ for every one of the three primes. This is the canonical case for the *second* tactic, **element-counting**, and the exercise exists to drill exactly that tactic.

**Assumption pattern.** The factorization $30 = 2 \cdot 3 \cdot 5$ has the special feature that *every* prime appears to the first power. By the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]], every Sylow subgroup is then of prime order, so distinct Sylow $p$-subgroups (for each fixed $p$) intersect trivially and the population of order-$p$ elements is exactly $n_p(p-1)$. A square-free order is the signature that element-counting is available — and $30$ is square-free.

**Theorem routing.** The route is a proof by contradiction. *Assume $G$ is simple.* Then no $n_p$ can be $1$, for [[Thm - A Unique Sylow Subgroup is Normal|a unique Sylow subgroup is normal]] and would contradict simplicity. Apply [[Thm - Sylow's Theorems|Sylow III]] to the primes $5$ and $3$: the constraints, *together with $n_p \neq 1$*, pin $n_5 = 6$ and $n_3 = 10$ exactly. Then the [[Ex - Counting elements of prime order with Sylow subgroups|counting fact]] converts these into $6 \cdot 4 = 24$ elements of order $5$ and $10 \cdot 2 = 20$ elements of order $3$. These two sets are disjoint, so $G$ would contain at least $24 + 20 = 44$ elements — but $|G| = 30$. The contradiction refutes the assumption.

**Key decision point.** The non-obvious move is to *use the assumption of simplicity as an active hypothesis* — to feed "$n_p \neq 1$" back into the Sylow constraints. The bare congruence-and-divisibility constraints leave $n_5 \in \{1, 6\}$ and $n_3 \in \{1, 10\}$; only the simplicity assumption, by deleting the value $1$, pins them down to the *single* values $6$ and $10$. Without that deletion the counting argument has no fixed numbers to work with. The second decision is which primes to count: $5$ and $3$ alone produce $44 > 30$, so the prime $2$ never needs to be examined — counting the two largest primes suffices.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory III — §1.5–1.7#Legal Operations|the topic page's Legal Operations]]:

1. **Factor the order and write down the Sylow constraints** (operation 1). The order $30 = 2 \cdot 3 \cdot 5$ is factored, and for the primes $5$ and $3$ the constraints $n_p \equiv 1 \pmod p$, $n_p \mid m$ are written down.

2. **Conclude normality from a unique Sylow subgroup** (operation 2), used *in contrapositive*. The assumption that $G$ is simple, combined with [[Thm - A Unique Sylow Subgroup is Normal]], forbids $n_p = 1$ for every prime — this is what deletes the value $1$ from each candidate list.

3. **Count elements of prime order** (operation 3). Since $5$ and $3$ appear to the first power, the [[Ex - Counting elements of prime order with Sylow subgroups|counting fact]] gives $n_5(5-1)$ elements of order $5$ and $n_3(3-1)$ elements of order $3$; these counts are summed and compared with $|G| = 30$.

---

# Hints

> [!note]- Hint 1
> Factor $30$ and write the Sylow constraints for each prime. You will find that for every prime the value $n_p > 1$ is *permitted* — so the first tactic, forcing some $n_p = 1$ from the arithmetic alone, does not finish. A second tactic is needed; notice that $30$ is square-free.

> [!note]- Hint 2
> Argue by contradiction: *suppose $G$ is simple*. Then no Sylow subgroup can be unique, since a unique Sylow subgroup is [[Thm - A Unique Sylow Subgroup is Normal|normal]]. Feed "$n_p \neq 1$" back into the Sylow constraints for $p = 5$ and $p = 3$. What single value does each $n_p$ collapse to?

> [!note]- Hint 3
> With $n_5 = 6$ and $n_3 = 10$: every Sylow $5$-subgroup has order $5$, and distinct ones meet only in $e$, so there are $6 \cdot (5 - 1) = 24$ elements of order $5$. Likewise $10 \cdot (3 - 1) = 20$ elements of order $3$. An element of order $5$ cannot also have order $3$, so these sets are disjoint. Add: $24 + 20 = 44$. Compare with $|G| = 30$.

---

# Solution

The plan is a proof by contradiction. Assume $G$ is simple; then no Sylow subgroup is unique. The Sylow constraints then pin $n_5$ and $n_3$ to single values, and counting the elements of orders $5$ and $3$ produces more elements than $G$ has.

**Step 1: If $G$ is simple, then $n_5 = 6$ and $n_3 = 10$.**

Assume $G$ is simple, so no $n_p$ equals $1$. For $p = 5$ the constraints $n_5 \equiv 1 \pmod 5$, $n_5 \mid 6$ leave $\{1, 6\}$; deleting $1$ gives $n_5 = 6$. For $p = 3$ the constraints $n_3 \equiv 1 \pmod 3$, $n_3 \mid 10$ leave $\{1, 10\}$; deleting $1$ gives $n_3 = 10$.

> [!note]- Derivation
> Factor $|G| = 30 = 2 \cdot 3 \cdot 5$. Suppose, for contradiction, that $G$ is [[Def - Simple Group|simple]]. If some prime $p$ had $n_p = 1$, the unique Sylow $p$-subgroup would be [[Thm - A Unique Sylow Subgroup is Normal|normal]]; it has order $p \in \{2, 3, 5\}$, so it is a proper non-trivial normal subgroup, contradicting simplicity. Hence
> $$n_p \neq 1 \quad \text{for every prime } p \in \{2, 3, 5\}.$$
>
> *The prime $5$.* With respect to $5$, $|G| = 5^1 \cdot 6$, so $m = 6$. [[Thm - Sylow's Theorems|Sylow III]] gives $n_5 \mid 6$ and $n_5 \equiv 1 \pmod 5$. The divisors of $6$ are $1, 2, 3, 6$; of these, $1 \equiv 1$ and $6 \equiv 1 \pmod 5$, while $2, 3 \not\equiv 1$. So the constraints alone leave $n_5 \in \{1, 6\}$. Simplicity deletes $1$, so $n_5 = 6$.
>
> *The prime $3$.* With respect to $3$, $|G| = 3^1 \cdot 10$, so $m = 10$. Sylow III gives $n_3 \mid 10$ and $n_3 \equiv 1 \pmod 3$. The divisors of $10$ are $1, 2, 5, 10$; of these, $1 \equiv 1$ and $10 \equiv 1 \pmod 3$, while $2 \equiv 2$ and $5 \equiv 2$. So the constraints leave $n_3 \in \{1, 10\}$. Simplicity deletes $1$, so $n_3 = 10$.

**Step 2: There are exactly $24$ elements of order $5$ and exactly $20$ of order $3$.**

Every prime $5, 3$ appears to the first power, so by the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]] there are $n_5(5-1) = 24$ elements of order $5$ and $n_3(3-1) = 20$ elements of order $3$.

> [!note]- Derivation
> The prime $5$ divides $|G| = 30$ but $5^2 = 25$ does not. By the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]], every Sylow $5$-subgroup has order $5$, distinct Sylow $5$-subgroups intersect only in the identity, and the number of elements of order $5$ is exactly
> $$n_5 \,(5 - 1) = 6 \cdot 4 = 24.$$
>
> (For self-containedness: a Sylow $5$-subgroup has order $5$, hence is cyclic with $5 - 1 = 4$ elements of order $5$. Two distinct ones $P \neq Q$ have $P \cap Q$ a subgroup of $P$, so $|P \cap Q| \mid 5$; it cannot be $5$ or $P = Q$, so $P \cap Q = \{e\}$. Thus the $6$ Sylow $5$-subgroups contribute disjoint sets of $4$ order-$5$ elements each.)
>
> Identically, $3$ divides $30$ but $3^2 = 9$ does not, so the number of elements of order $3$ is exactly
> $$n_3 \,(3 - 1) = 10 \cdot 2 = 20.$$

**Step 3: $24 + 20 = 44 > 30$ — contradiction; $G$ is not simple.**

An element of order $5$ cannot have order $3$, so the two sets are disjoint and $G$ would contain at least $24 + 20 = 44$ elements. But $|G| = 30 < 44$. The assumption of simplicity is therefore false.

> [!note]- Derivation
> The set $A$ of elements of order $5$ and the set $B$ of elements of order $3$ are *disjoint*: an element has a single well-defined order, and $5 \neq 3$, so no element lies in both. (Neither set contains the identity, which has order $1$.) Hence
> $$|A \cup B| = |A| + |B| = 24 + 20 = 44.$$
> But $A \cup B$ is a subset of $G$, so $|A \cup B| \leq |G| = 30$. This gives $44 \leq 30$, a contradiction.
>
> The contradiction arose solely from the assumption that $G$ is [[Def - Simple Group|simple]]. Therefore $G$ is **not simple**: no group of order $30$ is simple. $\blacksquare$

> [!note]- Complete formal solution
> Let $|G| = 30 = 2 \cdot 3 \cdot 5$ and suppose, for contradiction, that $G$ is [[Def - Simple Group|simple]].
>
> If any $n_p = 1$, the unique [[Def - Sylow p-Subgroup|Sylow p-subgroup]] would be a proper non-trivial [[Thm - A Unique Sylow Subgroup is Normal|normal subgroup]], contradicting simplicity. So $n_p \neq 1$ for $p \in \{2, 3, 5\}$.
>
> By [[Thm - Sylow's Theorems|Sylow III]]: for $p = 5$, $n_5 \mid 6$ and $n_5 \equiv 1 \pmod 5$, leaving $n_5 \in \{1, 6\}$, hence $n_5 = 6$. For $p = 3$, $n_3 \mid 10$ and $n_3 \equiv 1 \pmod 3$, leaving $n_3 \in \{1, 10\}$, hence $n_3 = 10$.
>
> Since $5$ and $3$ each divide $30$ to the first power, every Sylow $5$- and Sylow $3$-subgroup has prime order; distinct ones intersect only in $\{e\}$ (an intersection is a subgroup of prime order, so trivial unless the subgroups coincide). Hence $G$ has exactly $n_5(5-1) = 6 \cdot 4 = 24$ elements of order $5$, and exactly $n_3(3-1) = 10 \cdot 2 = 20$ elements of order $3$.
>
> The order-$5$ elements and the order-$3$ elements form disjoint sets (an element has one order, $5 \neq 3$), so $G$ contains at least $24 + 20 = 44$ elements. But $|G| = 30 < 44$ — a contradiction.
>
> Therefore $G$ is not simple. $\blacksquare$

---

# Key Takeaways

**Square-free order is the signal to switch from the uniqueness tactic to element-counting.** When the first step of the playbook fails — when the Sylow constraints permit $n_p > 1$ for every prime — the next thing to check is whether the order is *square-free*, that is, a product of distinct primes each to the first power. If so, every Sylow subgroup has prime order, and the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]] becomes available: each prime $p$ contributes a known number $n_p(p-1)$ of elements of order $p$, and these populations are disjoint across primes. The whole non-simplicity argument then reduces to arithmetic — add the forced counts and check whether they exceed $|G|$. The trigger is precise: see a square-free order that survives the uniqueness step, and reach immediately for element-counting. Orders like $30$, $42$, and $66$ all yield to this exact move.

**Assume simplicity, then mine the assumption — "$n_p \neq 1$" is the tool that pins the counts.** The Sylow constraints by themselves are too loose: they leave $n_5 \in \{1, 6\}$ and $n_3 \in \{1, 10\}$, and a counting argument needs *exact* numbers, not two-element sets. The proof by contradiction is what supplies the exactness. Assuming $G$ is simple forbids any $n_p = 1$ — because a unique Sylow subgroup is [[Thm - A Unique Sylow Subgroup is Normal|normal]] — and *deleting the value $1$* from each candidate list collapses it to a singleton. This is the structural role of the contradiction hypothesis in nearly every element-counting non-simplicity proof: it is not a passive "suppose not" but an active hypothesis that, by removing the value $1$, makes the Sylow counts computable. The reusable pattern is: assume simple, immediately conclude $n_p \neq 1$ for all $p$, and use that to evaluate every $n_p$ exactly before counting anything.

**Count only the primes you need, largest first, and stop when the total overshoots.** The order $30$ has three primes, but the proof never touches the prime $2$: the elements of orders $5$ and $3$ already number $44 > 30$. The efficient habit is to count the elements of the *largest* primes first, because large primes produce large element-populations ($p - 1$ per subgroup) and the most non-trivial Sylow counts. As soon as the running tally exceeds $|G|$, the contradiction is complete and the remaining primes are irrelevant. Counting the Sylow $2$-subgroups here would be wasted effort. More generally, the element-counting tactic does not require a full census of $G$ — it requires only *enough* of a census to overflow the group, and overflowing it with the two or three largest primes is almost always quickest. (The leftover-room version of the same idea — too few elements remain for some Sylow subgroup — is what finishes orders like $56$.)

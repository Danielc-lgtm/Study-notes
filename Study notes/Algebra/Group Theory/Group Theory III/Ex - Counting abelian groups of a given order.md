---
type: exercise
subject: group-theory
difficulty: "⭐"
prereqs:
  - "Def - Abelian Group"
  - "Def - Direct Product"
  - "Thm - Classification of Finite Abelian Groups"
  - "Thm - Chinese Remainder Theorem for Cyclic Groups"
tags: [algebra, group-theory]
---

# Problem Statement

How many [[Def - Abelian Group|abelian]] groups of order $720$ are there, up to [[Def - Isomorphism|isomorphism]]?

After answering this, extract the general rule: for an integer $n$ with prime factorization $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, the number of abelian groups of order $n$ up to isomorphism is $p(a_1)\, p(a_2) \cdots p(a_k)$, where $p(a)$ denotes the number of integer partitions of $a$.

**Recall:**

The whole problem rests on a single theorem, which it is worth having in front of you in both of its forms.

![[Thm - Classification of Finite Abelian Groups#Statement]]

The two forms named there are the lever for this count. The **elementary divisor** form writes a finite abelian group as a [[Def - Direct Product|direct product]] $C_{q_1} \times C_{q_2} \times \cdots \times C_{q_s}$ in which every $q_j$ is a prime power. The **invariant factor** form instead writes it as $C_{d_1} \times \cdots \times C_{d_r}$ with the divisibility chain $d_{i+1} \mid d_i$. The [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] — if $\gcd(m,n) = 1$ then $C_{mn} \cong C_m \times C_n$ — is what translates between them, and in particular it lets us treat the different primes dividing the order completely independently of one another.

An **integer partition** of a non-negative integer $a$ is a way of writing $a$ as an unordered sum of positive integers; the number of such partitions is written $p(a)$. For instance $4 = 4 = 3+1 = 2+2 = 2+1+1 = 1+1+1+1$, so $p(4) = 5$. By convention $p(1) = 1$ and $p(2) = 2$.

A [[Def - Abelian Group|finite abelian group]] is a finite group in which every pair of elements commutes, $gh = hg$. We count such groups *up to isomorphism*: two groups are counted as the same exactly when there is a bijective homomorphism between them, so the question asks for the number of genuinely distinct isomorphism types of abelian group with $720$ elements.

---

# Convergent Strategy

**Problem class.** This is a *counting* problem of the kind catalogued in the [[Group Theory III — §1.5–1.7#Sources and Targets|Sources and Targets]] of the topic page — specifically, counting isomorphism types of group of a fixed order. It belongs to the §1.6 family, where the conceptual work is all front-loaded into the [[Thm - Classification of Finite Abelian Groups|classification theorem]] and what remains afterwards is combinatorics.

**Assumption pattern.** The only datum is the integer $720$, and the only hypothesis on the group is that it is *abelian*. That word "abelian" is the trigger: the instant a problem fixes a finite abelian group, the [[Group Theory III — §1.5–1.7#Problem-Solving Strategy|topic strategy]] says to reach for the classification, because the classification converts every question about the group into a question about partitions and divisibility, with no group theory left to do.

**Theorem routing.** The route is short. Factor $720$ into prime powers. The [[Thm - Classification of Finite Abelian Groups|classification]] in elementary-divisor form says an abelian group of order $720$ is a product of cyclic groups of prime-power order, and the multiset of those prime powers — restricted to a single prime $p$ — is exactly a partition of the exponent of $p$ in $720$. The [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] guarantees the choices for different primes do not interact, so the total count is the product, over primes, of the number of partitions of each exponent.

**Key decision point.** The one idea that makes the problem trivial rather than intractable is the recognition that *choosing an abelian group of order $p^a$ is the same act as choosing a partition of $a$*. A group of order $p^a$ in elementary-divisor form is $C_{p^{b_1}} \times \cdots \times C_{p^{b_t}}$ where the exponents satisfy $b_1 + \cdots + b_t = a$; since direct product does not care about the order of its factors, what has been chosen is an unordered collection of positive integers summing to $a$ — a partition. Counting groups becomes counting partitions, and the only remaining labour is to evaluate $p(\cdot)$ on small inputs.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory III — §1.5–1.7#Legal Operations|the topic page's Legal Operations]]:

1. **Decompose an abelian group via the classification** (operation 7). This is the operation the entire exercise is built on. The trigger — the word "abelian" attached to a finite group — is present, and the move is to write the group as a product of cyclic groups of prime-power order and read off the combinatorial data that determines it.

2. **Combine factors across coprime orders via the Chinese remainder theorem** (the partner half of operation 7). Here it is used in reverse, as an *independence* statement rather than a fusing one: because $C_{mn} \cong C_m \times C_n$ for coprime $m, n$, the prime-power pieces belonging to distinct primes can be chosen separately, so the count factorizes as a product over primes.

---

# Hints

> [!note]- Hint 1
> You are counting *abelian* groups, so the [[Thm - Classification of Finite Abelian Groups|classification of finite abelian groups]] applies. Use the form that writes the group as a product of cyclic groups of *prime-power* order. Begin by factorizing $720$ into prime powers — what primes appear, and to what powers?

> [!note]- Hint 2
> The primes can be handled one at a time. The [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] says that the part of the group belonging to one prime does not interact with the part belonging to another, so the total count is a *product* of separate counts, one per prime. Fix a single prime $p$ appearing with exponent $a$: how many abelian groups of order exactly $p^a$ are there?

> [!note]- Hint 3
> An abelian group of order $p^a$ is $C_{p^{b_1}} \times \cdots \times C_{p^{b_t}}$ with $b_1 + \cdots + b_t = a$ and every $b_j \geq 1$. Because direct product ignores the ordering of its factors, this is exactly an unordered way of writing $a$ as a sum of positive integers — a *partition* of $a$. So the number of abelian groups of order $p^a$ is $p(a)$, the partition function. Now evaluate $p(4)$, $p(2)$, $p(1)$ and multiply.

---

# Solution

The strategy is to factor $720$, use the [[Thm - Classification of Finite Abelian Groups|classification]] to reduce each prime's contribution to a partition count, and multiply.

**Step 1: Factorize the order.**

The order factorizes as $720 = 2^4 \cdot 3^2 \cdot 5^1$. The three primes are $2, 3, 5$, with exponents $4, 2, 1$.

> [!note]- Derivation
> Divide out powers of small primes: $720 = 2 \cdot 360 = 2^2 \cdot 180 = 2^3 \cdot 90 = 2^4 \cdot 45$, and $45 = 9 \cdot 5 = 3^2 \cdot 5$. Hence
> $$720 = 2^4 \cdot 3^2 \cdot 5^1,$$
> with $2 \nmid 45$ confirming the power of $2$ is exactly $4$. The relevant data is the list of exponents $(a_2, a_3, a_5) = (4, 2, 1)$.

**Step 2: Reduce to one prime at a time.**

By the [[Thm - Classification of Finite Abelian Groups|classification]] together with the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]], an abelian group of order $720$ is determined, independently for each prime $p \in \{2,3,5\}$, by an abelian group of order $p^{a_p}$ — its **Sylow $p$-subgroup**. The total count is the product of the per-prime counts.

> [!note]- Derivation
> The classification, in elementary-divisor form, says any abelian group $G$ of order $720$ is a [[Def - Direct Product|direct product]] of cyclic groups of prime-power order:
> $$G \cong C_{q_1} \times C_{q_2} \times \cdots \times C_{q_s}, \qquad \text{each } q_j \text{ a prime power.}$$
> Group the factors $q_j$ by which prime they are a power of. Collecting the $2$-power factors into a product $G_2$, the $3$-power factors into $G_3$, and the $5$-power factor into $G_5$, we get $G \cong G_2 \times G_3 \times G_5$. Counting orders, $|G_2|$ is a power of $2$, $|G_3|$ a power of $3$, $|G_5|$ a power of $5$, and their product is $720 = 2^4 \cdot 3^2 \cdot 5$; by uniqueness of prime factorization, $|G_2| = 2^4$, $|G_3| = 3^2$, $|G_5| = 5$.
>
> This is independence in two directions. First, *every* abelian $G$ of order $720$ arises this way. Second, the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] guarantees there is no double-counting and no interference between primes: because $2^4$, $3^2$, $5$ are pairwise coprime, a choice of $G_2$, a choice of $G_3$, and a choice of $G_5$ assemble into one and only one isomorphism type $G_2 \times G_3 \times G_5$, and distinct triples of choices give non-isomorphic groups (their Sylow subgroups, which the triple records, differ). So the abelian groups of order $720$ are in bijection with triples
> $$(\text{abelian group of order } 2^4,\ \text{abelian group of order } 3^2,\ \text{abelian group of order } 5),$$
> and the count is the *product* of the three separate counts.

**Step 3: Count abelian groups of order $p^a$ as partitions of $a$.**

The number of abelian groups of order $p^a$, up to isomorphism, is exactly $p(a)$ — the number of integer partitions of the exponent $a$. This holds for every prime $p$ and is independent of which prime $p$ is.

> [!note]- Derivation
> Fix a prime $p$ and exponent $a$. By the [[Thm - Classification of Finite Abelian Groups|classification]], an abelian group of order $p^a$ is a direct product of cyclic groups of prime-power order, and since the order is $p^a$ every factor must be a power *of $p$*:
> $$C_{p^{b_1}} \times C_{p^{b_2}} \times \cdots \times C_{p^{b_t}}, \qquad b_1, b_2, \dots, b_t \geq 1.$$
> The order of this product is $p^{b_1 + b_2 + \cdots + b_t}$, and for it to equal $p^a$ we need
> $$b_1 + b_2 + \cdots + b_t = a.$$
> So the data of the group is a finite list of positive integers summing to $a$. But the [[Def - Direct Product|direct product]] does not depend on the order in which its factors are listed — $C_{p^{b_1}} \times C_{p^{b_2}} \cong C_{p^{b_2}} \times C_{p^{b_1}}$ — so what has actually been specified is the *unordered* multiset $\{b_1, \dots, b_t\}$. An unordered multiset of positive integers summing to $a$ is precisely an **integer partition** of $a$.
>
> The correspondence is a genuine bijection. Each partition of $a$ produces one group, by raising $p$ to each part and taking the product. Conversely each abelian group of order $p^a$, by the *uniqueness* clause of the classification, has a single well-defined multiset of elementary divisors, hence determines a single partition; and two groups with the same partition have the same elementary divisors, so by uniqueness are isomorphic. Therefore the number of abelian groups of order $p^a$ up to isomorphism equals $p(a)$, the partition function evaluated at $a$. The prime $p$ played no role beyond labelling — only the exponent $a$ matters.

**Step 4: Evaluate and multiply.**

The exponents are $4, 2, 1$. Counting partitions, $p(4) = 5$, $p(2) = 2$, $p(1) = 1$, so the number of abelian groups of order $720$ is
$$p(4) \cdot p(2) \cdot p(1) = 5 \cdot 2 \cdot 1 = 10.$$

> [!note]- Derivation
> The partitions of $4$ are
> $$4, \quad 3+1, \quad 2+2, \quad 2+1+1, \quad 1+1+1+1,$$
> so $p(4) = 5$. These correspond to the five abelian groups of order $2^4 = 16$:
> $$C_{16}, \quad C_8 \times C_2, \quad C_4 \times C_4, \quad C_4 \times C_2 \times C_2, \quad C_2 \times C_2 \times C_2 \times C_2.$$
> The partitions of $2$ are $2$ and $1+1$, so $p(2) = 2$, corresponding to the two abelian groups of order $3^2 = 9$:
> $$C_9, \quad C_3 \times C_3.$$
> The only partition of $1$ is $1$ itself, so $p(1) = 1$: the single abelian group of order $5$ is $C_5$.
>
> By Step 2 the total count is the product of these:
> $$p(4) \cdot p(2) \cdot p(1) = 5 \cdot 2 \cdot 1 = 10.$$
> There are exactly $\mathbf{10}$ abelian groups of order $720$ up to isomorphism.

> [!note]- Complete formal solution
> Factor the order: $720 = 2^4 \cdot 3^2 \cdot 5^1$.
>
> By the [[Thm - Classification of Finite Abelian Groups|classification of finite abelian groups]] in elementary-divisor form, every abelian group $G$ of order $720$ is a [[Def - Direct Product|direct product]] of cyclic groups of prime-power order. Grouping these factors by their underlying prime gives $G \cong G_2 \times G_3 \times G_5$ where $|G_2| = 2^4$, $|G_3| = 3^2$, $|G_5| = 5$. Because $2^4, 3^2, 5$ are pairwise coprime, the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] makes this decomposition a bijection: isomorphism types of $G$ correspond bijectively to triples $(G_2, G_3, G_5)$ of abelian groups of orders $2^4, 3^2, 5$ respectively. Hence
> $$\#\{\text{abelian groups of order } 720\} = \#\{\text{order } 2^4\} \cdot \#\{\text{order } 3^2\} \cdot \#\{\text{order } 5\}.$$
>
> For a single prime $p$, an abelian group of order $p^a$ is $C_{p^{b_1}} \times \cdots \times C_{p^{b_t}}$ with each $b_j \geq 1$ and $\sum b_j = a$. Since the direct product is insensitive to the ordering of its factors, the group is determined by the unordered multiset $\{b_1, \dots, b_t\}$, i.e. by an integer partition of $a$. By the uniqueness clause of the classification this correspondence is a bijection, so the number of abelian groups of order $p^a$ is $p(a)$, the partition function.
>
> The exponents here are $4, 2, 1$, with $p(4) = 5$ (partitions $4,\ 3{+}1,\ 2{+}2,\ 2{+}1{+}1,\ 1{+}1{+}1{+}1$), $p(2) = 2$ (partitions $2,\ 1{+}1$), and $p(1) = 1$. Therefore
> $$\#\{\text{abelian groups of order } 720\} = p(4) \cdot p(2) \cdot p(1) = 5 \cdot 2 \cdot 1 = 10.$$
>
> In general, for $n = p_1^{a_1} \cdots p_k^{a_k}$ the same argument gives the number of abelian groups of order $n$ as $\prod_{i=1}^{k} p(a_i)$. $\blacksquare$

---

# Key Takeaways

**"Abelian" plus "finite" is a trigger that converts a group problem into a partition problem.** The moment a problem fixes a finite abelian group, the [[Thm - Classification of Finite Abelian Groups|classification]] is available, and its effect is total: it does not merely *help* with the problem, it *removes the group theory entirely*. After invoking it, no group remains to be reasoned about — there is only an integer, its prime factorization, and the combinatorics of partitions and divisibility. This is the defining feature of the §1.6 problem family and the reason those exercises feel mechanical once the classification is internalised. The reusable instinct is to treat "finite abelian group" as a coded instruction meaning "translate to partitions now"; the conceptual difficulty of any such problem lives in the classification theorem itself, and everything downstream is bookkeeping. The same translation underlies counting elements of a given order, deciding isomorphism of two abelian groups, and converting between the two normal forms — all of §1.6 is this one move.

**Coprimality lets a global count factorize into independent local counts.** The reason the answer is a *product* $p(4) \cdot p(2) \cdot p(1)$ and not something entangled is the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]]: because the prime-power parts $2^4, 3^2, 5$ of the order are pairwise coprime, choosing the $2$-part of the group, the $3$-part, and the $5$-part are three independent decisions, and independent decisions multiply. This "decompose along coprime factors, count each piece, multiply" pattern is pervasive far beyond group theory — it is exactly why arithmetic functions like Euler's totient $\varphi$ and the divisor-count function are *multiplicative*, and it is the same logic by which the structure of a module over a principal ideal domain splits along its primary components. Whenever an object canonically decomposes into pieces indexed by distinct primes, expect the count, the invariant, or the classification to factorize as a product over those primes; the work then reduces to understanding a single prime in isolation.

**Unordered data signals a partition; the partition function is the universal counter for it.** The crux of the count is recognising that an abelian group of order $p^a$ records nothing more than an *unordered* collection of positive integers — the exponents $b_j$ — summing to $a$, because the [[Def - Direct Product|direct product]] forgets the order of its factors. An unordered multiset of positive integers with a fixed sum is the definition of an integer partition, so the count is $p(a)$ by definition, with no further computation of structure required. This is worth installing as a general recognition: whenever the objects you are counting are determined by an unordered tuple of positive integers with a prescribed total, you are counting partitions, and $p(a)$ is the answer. The same partition function counts the conjugacy classes of the symmetric group $S_a$ (each is a cycle type, an unordered list of cycle lengths summing to $a$) and the number of ways a $p$-group can sit as an abelian group — the recurrence of $p(a)$ across these settings is a sign that "unordered positive integers with fixed sum" is a single combinatorial primitive appearing in many disguises.

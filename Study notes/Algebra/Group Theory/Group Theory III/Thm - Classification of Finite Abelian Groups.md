---
type: theorem
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Abelian Group"
  - "Def - Direct Product"
  - "Def - Order of a Group and of an Element"
  - "Def - Isomorphism"
  - "Thm - Chinese Remainder Theorem for Cyclic Groups"
tags: [algebra, group-theory]
---

# Notation

$G$ denotes a finite [[Def - Abelian Group|abelian group]]. $C_n$ is the cyclic group of order $n$, written multiplicatively or — since everything here is abelian — additively as $\mathbb{Z}/n\mathbb{Z}$ without change of meaning. The symbol $\times$ is the [[Def - Direct Product|direct product]]: $C_{d_1} \times \cdots \times C_{d_r}$ is the group of tuples with componentwise operation and order $\prod_i d_i$. The relation $d \mid d'$ means $d$ divides $d'$. The integers $d_1, \dots, d_r$ produced in the invariant-factor form satisfy the divisibility chain $d_{i+1} \mid d_i$ and are called the **invariant factors** of $G$; the prime-power orders produced in the alternative form are the **elementary divisors**. A prime is $p$; a prime power is $p^k$. The symbol $\cong$ is group [[Def - Isomorphism|isomorphism]]. The full notation registry lives on the parent page [[Group Theory III — §1.5–1.7]].

---

# Statement

> **Classification of Finite [[Def - Abelian Group|Abelian Groups]].** Let $G$ be a finite [[Def - Abelian Group|abelian]] group. Then there exist integers $d_1, d_2, \dots, d_r \geq 2$ such that
> $$G \;\cong\; C_{d_1} \times C_{d_2} \times \cdots \times C_{d_r}.$$
> Moreover, the $d_i$ may be chosen so that
> $$d_{i+1} \mid d_i \qquad \text{for each } i = 1, \dots, r-1,$$
> and with this divisibility condition imposed **the list $(d_1, \dots, d_r)$ is unique**. These $d_i$ are the **invariant factors** of $G$.

> **Equivalent form (elementary divisors).** Every finite abelian group $G$ is also isomorphic to a [[Def - Direct Product|direct product]]
> $$G \;\cong\; C_{q_1} \times C_{q_2} \times \cdots \times C_{q_s}$$
> in which **every** $q_j$ is a prime power $p^k$. The multiset $\{q_1, \dots, q_s\}$ of prime powers — the **elementary divisors** of $G$ — is unique.

The two forms describe the same [[Def - Group|groups]], and the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] is the explicit dictionary between them. Taken together, the theorem is a **complete and irredundant classification**: it produces, for each isomorphism type of finite abelian group, exactly one normal form, so two finite abelian [[Def - Group|groups]] are isomorphic if and only if their invariant-factor lists (equivalently, their elementary-divisor multisets) coincide. The isomorphism problem for finite abelian groups is thereby solved outright.

> **Worked example (order $8$).** The abelian groups of order $8$ are exactly three, up to isomorphism:
> $$C_8, \qquad C_4 \times C_2, \qquad C_2 \times C_2 \times C_2.$$
> In invariant-factor form the lists are $(8)$, $(4, 2)$, $(2, 2, 2)$ — each a decreasing divisibility chain. In elementary-divisor form they are $\{2^3\}$, $\{2^2, 2\}$, $\{2, 2, 2\}$. The count, three, is the number of partitions of the exponent $3$ in $8 = 2^3$.

The theorem is **stated and used here, not proved from scratch**: its proof is deferred to the structure theorem for finitely generated [[Def - Module|modules]] over a principal [[Def - Ideal|ideal]] domain (later in the course), of which it is the case $R = \mathbb{Z}$. The "Formal Proof" section below explains why the deferral is the honest choice, and instead proves the part that genuinely belongs to this topic — the equivalence of the two forms.

---

# Motivation

The defining ambition of finite group theory is classification: to list, without omission and without repetition, every finite group of a given kind, so that "which group is this?" has a finite, checkable answer. For arbitrary finite groups this ambition is monstrously hard — its non-abelian endpoint is the classification of finite simple groups, thousands of pages of work culminating in twenty-six sporadic exceptions. The natural first question is whether *some* class of finite groups is tame enough to be classified completely and cleanly. The answer is yes, and the [[Def - Abelian Group|abelian]] groups are that class.

Before this theorem, even a finite abelian group is opaque. You might know $|G| = 360$ and that $G$ is abelian, and still not know which group $G$ is — there are several, and nothing tells you how many or how to tell them apart. A multiplication table of $360$ entries is not an answer; it does not let you decide, given a *second* abelian group of order $360$, whether the two are the same group in disguise. What is missing is a **normal form**: a canonical, smallest-possible description of each isomorphism type, computed in a fixed way, such that two groups are isomorphic exactly when their normal forms are literally equal.

The classification supplies precisely this. It says every finite abelian group is built, by [[Def - Direct Product|direct product]], out of the simplest abelian groups there are — the cyclic groups — and it pins down the building in two complementary canonical ways. The invariant-factor form gives the shortest such description, a decreasing divisibility chain. The elementary-divisor form gives the most refined, a multiset of prime powers. Either way the description is *unique*, so the isomorphism problem collapses to comparing two lists of integers. The opaque "abelian group of order $360$" becomes the transparent "$C_{60} \times C_6$" or equivalently "$C_4 \times C_3 \times C_3 \times C_5$", and counting how many abelian groups of order $360$ there are becomes counting partitions of the exponents $3, 2, 1$ in $360 = 2^3 \cdot 3^2 \cdot 5$.

One should expect a result like this to exist precisely because abelian groups lack the feature that makes general groups wild: non-commuting elements. In an abelian group every subgroup is automatically [[Def - Normal Subgroup|normal]], every quotient is again abelian, and conjugation is trivial — so the obstructions that let non-abelian groups twist their pieces together (the semidirect-product twists) are all absent. With no room for twisting, the only way to assemble cyclic pieces is the untwisted way, the direct product, and the surprise is not that a classification exists but that it is this short.

---

# Sources and Targets

This section records the non-obvious ways a problem arrives at the hypothesis of the classification (sources) and the non-obvious results that follow from combining its conclusion with one more fact (targets).

**Sources (Input Broadening)**

The hypothesis is minimal: *a finite abelian group*. The skill is recognizing, in a problem that does not announce "abelian", that the group in front of you is abelian and finite — at which point the entire classification becomes available and the problem is reduced to combinatorics.

The most frequent source is **a group of order $p^2$, or more generally a group all of whose elements have small order**. Property $B$ here is "$|G| = p^2$ for a prime $p$". The bridge is [[Thm - Quotient by the Centre and Commutativity|the order-p² theorem]]: every group of order $p^2$ is abelian, because its [[Def - Centraliser and Centre|centre]] cannot have index a prime without forcing $G/Z(G)$ cyclic. The implication is non-obvious because the hypothesis "$|G| = p^2$" mentions only a number, not commutativity; yet it secretly delivers abelianness, and so the classification applies and tells you $G$ is either $C_{p^2}$ or $C_p \times C_p$ — there are exactly two groups of order $p^2$, and the source argument is what licenses naming them.

A second source is **$G$ is a quotient or subgroup of a known abelian group**. Property $B$ is "$G = A/N$ or $G \leq A$ with $A$ abelian". The bridge is that subgroups and quotients of abelian groups are abelian — commutativity is inherited downward and passes to quotients — so the classification applies to $G$ even though $G$ was handed to you only as a piece of something else. The non-obvious payoff is that you can read off the invariant factors of a quotient $\mathbb{Z}^n / L$ from the lattice $L$, which is how the classification connects to lattices and to the cokernel of an integer matrix.

A third source is **$G$ is the group of units, or the additive group, of a finite ring or field**. Property $B$ is "$G = (R, +)$ for a commutative ring $R$", or "$G = R^\times$ for a finite *commutative* ring". The additive group of any ring is abelian by the ring axioms; the unit group of a commutative ring is abelian because multiplication commutes. The bridge is non-obvious because the object is presented as a ring, with its multiplicative structure foregrounded, and the abelian group hiding inside it is easy to miss. This is the route by which the classification determines the additive structure of $\mathbb{Z}/n\mathbb{Z}$ and underlies the proof that $(\mathbb{Z}/p\mathbb{Z})^\times$ is cyclic.

A fourth source is **$G$ is finitely generated and abelian, with a torsion hypothesis**. Property $B$ is "$G$ is a finitely generated abelian group in which every element has finite order". Finite generation plus all-elements-finite-order forces $G$ finite, so the classification applies. The non-obvious step is the implication "finitely generated $+$ torsion $\implies$ finite": it fails without commutativity (finitely generated infinite torsion groups exist among non-abelian groups) and is exactly the abelian miracle that makes the *finitely generated* abelian groups — not merely the finite ones — completely classified.

**Targets (Output Amplification)**

The conclusion delivered is a normal form $C_{d_1} \times \cdots \times C_{d_r}$ with $d_{i+1} \mid d_i$, or equivalently a multiset of elementary divisors. On its own this is a description; combined with one further property it yields counts, structural identifications, and decision procedures.

The most useful combination is **the normal form plus partition-counting yields the number of abelian groups of a given order**. The conclusion $C$ is "every finite abelian group has a unique elementary-divisor multiset". Add property $D$: the elementary divisors at the prime $p$ are a multiset of powers of $p$ whose exponents sum to the exponent of $p$ in $|G|$. Then the abelian groups of order $p^a$ are in bijection with the **partitions of the integer $a$**, and the abelian groups of order $n = \prod p_i^{a_i}$ are in bijection with tuples of partitions, one per prime, so their number is $\prod_i \mathfrak{p}(a_i)$ where $\mathfrak{p}$ is the partition function. The result $E$ — an exact formula for the number of abelian groups of order $n$ — is non-obvious because "number of groups" sounds like a question requiring group theory, yet it has become pure combinatorics of integer partitions.

A second combination is **the normal form plus the structure of cyclic groups yields the exact count of elements of each order**. The conclusion $C$ is the decomposition $G \cong \prod C_{d_i}$. Add property $D$: in $C_n$ there are exactly $\varphi(d)$ elements of order $d$ for each $d \mid n$, and the order of a tuple in a direct product is the [[Def - Direct Product|lcm of the coordinate orders]]. Combining these lets you compute, for any finite abelian group, precisely how many elements have any prescribed order. The result $E$ — a complete element-order census — is non-obvious because it requires fusing the classification with the arithmetic of the totient function across all factors at once, and it is the tool that distinguishes $C_4 \times C_2$ from $C_2^3$ by counting elements of order $4$.

A third combination is **the normal form plus a hypothesized isomorphism yields a decision procedure**. The conclusion $C$ is uniqueness of invariant factors. Add property $D$: you are asked whether two finite abelian groups $G$ and $G'$, possibly presented very differently, are isomorphic. Then $E$ is the algorithm — compute the invariant factors of each, compare the two integer lists, and they are isomorphic exactly when the lists match. The combination is non-obvious because two abelian groups can be presented so as to look entirely unalike (one as a product of prime-power cyclics, another as a quotient of $\mathbb{Z}^n$), and the classification is what guarantees the comparison is both *decidable* and *complete*.

A fourth combination is **the normal form plus the largest invariant factor identifies the exponent and detects cyclicity**. The conclusion $C$ gives the chain $d_1, \dots, d_r$ with $d_{i+1} \mid d_i$. Add property $D$: the largest invariant factor $d_1$ is the **exponent** of $G$, the least common multiple of all element orders, since every $d_i$ divides $d_1$. Then $G$ is cyclic exactly when $r = 1$, i.e. exactly when $d_1 = |G|$ — equivalently, when $G$ contains an element of order $|G|$. The result $E$ — a clean criterion for a finite abelian group to be cyclic, and a formula for its exponent — is non-obvious because the exponent looks like a quantity you would have to compute element by element, whereas the classification hands it to you as the first invariant factor.

---

# Why Is It True

The intuition splits into two independent pieces — *that the group decomposes at all*, and *that the decomposition is essentially unique* — and it is worth seeing each separately, because they are convincing for entirely different reasons.

**Why a decomposition exists.** Picture a finite abelian group as a finite-dimensional object that you are trying to find a "basis" for. In a vector space, you pick a vector, throw in its span, pick a vector outside that span, throw in *its* span, and continue; the space falls apart into a direct sum of one-dimensional pieces, the lines through basis vectors. A finite abelian group wants to do the same thing — peel off a cyclic subgroup, split it off as a direct factor, and recurse on what remains. The reason this *almost* works, and the reason it needs care, is that the group $\mathbb{Z}/n\mathbb{Z}$-module structure is not quite as free as a vector space: integers are not invertible, so a cyclic subgroup $\langle g \rangle$ need not have a *complement*. The fix, which the full proof carries out, is to choose $g$ greedily — to take an element of *maximal order* first. An element of maximal order generates a cyclic subgroup that, it turns out, *can* be split off as a direct factor, and then the quotient is a smaller abelian group to recurse on. So the decomposition exists for the same reason a vector space has a basis: you can repeatedly peel off a cyclic piece. The single subtlety, absent for vector spaces, is that the piece must be chosen of maximal order for the peeling to leave a clean complement, and that subtlety is exactly why the invariant factors come out in *decreasing* order $d_1 \geq d_2 \geq \cdots$ with $d_{i+1} \mid d_i$ — each is the maximal order surviving after the previous ones are removed.

**Why the prime-power refinement exists.** Once you have *any* decomposition into cyclic groups, the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] grinds each cyclic factor into prime-power cyclic factors: $C_n$ with $n = p_1^{a_1} \cdots p_k^{a_k}$ splits as $C_{p_1^{a_1}} \times \cdots \times C_{p_k^{a_k}}$ because the prime powers are pairwise coprime. So a decomposition into *arbitrary* cyclic groups and a decomposition into *prime-power* cyclic groups carry the same information; you can always pass from the coarser to the finer. This is why the elementary-divisor form is available the moment the invariant-factor form is.

**Why the decomposition is unique.** Uniqueness is the part that feels like it could fail, and the intuition that it does not comes from realising that the decomposition's data is *forced by intrinsic, isomorphism-invariant features of $G$* — features you can compute without ever choosing a decomposition. Take the prime-power picture. For a fixed prime $p$, the number of elementary divisors equal to $p$, the number equal to $p^2$, and so on, can be *recovered* from $G$ by counting solutions to equations: the subgroup $\{x \in G : px = 0\}$ of elements killed by $p$ is itself a vector space over the field $\mathbb{Z}/p\mathbb{Z}$, and its [[Def - Dimension|dimension]] counts the *total number* of $p$-power factors; refining the count by looking at $\{x : p^k x = 0\}$ for each $k$ pins down how many factors are $C_p$, how many are $C_{p^2}$, and so on. None of these counts depends on a choice — they are determined by $G$ alone. Two different-looking decompositions of the same $G$ must therefore yield the same prime-power multiset, because both must match these intrinsic counts. Uniqueness is not a coincidence to be checked; it is the statement that the decomposition merely *displays* invariants that were already inside $G$, computable by counting how many elements each prime power annihilates.

Putting the three pieces together: a finite abelian group decomposes because it can be peeled like a vector space (with the maximal-order subtlety), it refines to prime powers because the Chinese remainder theorem permits it, and the decomposition is unique because the multiplicities of the pieces are intrinsic [[Def - Annihilator|annihilator]]-counts of $G$. None of this should be surprising once the vector-space analogy and the [[Def - Annihilator|annihilator]]-counting idea are in hand — which is exactly why the genuine proof is deferred: it is the same argument, run cleanly, in the language of [[Def - Module|modules]] over a PID.

---

# What Makes This Hard

The conceptual trap is believing the *existence* of the decomposition is the easy half and uniqueness the hard half — in fact existence is where the real work sits, because a cyclic subgroup of an abelian group need not have a complement, so you cannot naively "peel off a factor" and must instead choose an element of *maximal* order to guarantee the split. The most common error is to assume the elementary-divisor multiset can be reshuffled freely into invariant factors; the conversion is rigid — at each prime you must take the *largest* surviving prime power into the *current* invariant factor — and getting the divisibility chain $d_{i+1} \mid d_i$ wrong is the standard mistake. When returning to this theorem after months, focus rederivation effort on the maximal-order choice in existence and on the column-by-column rule for assembling invariant factors from elementary divisors.

---

# Rederivation Scaffold

This section is self-sufficient. Because the *existence-and-uniqueness* proof is the module structure theorem (deferred), this scaffold reconstructs what genuinely belongs here: the **statement, the two normal forms, and the explicit equivalence between them**, together with the example counts. Mastering this is the practical content of §1.6.

**High-level strategy:**
Take the existence-and-uniqueness of the invariant-factor decomposition as a known input (it is the $R = \mathbb{Z}$ case of the PID module structure theorem). From it, derive the elementary-divisor form by splitting each cyclic factor with the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]]; conversely, reassemble invariant factors from elementary divisors by a "largest-first, column-by-column" rule. The two forms then visibly classify the same groups, and counting reduces to partitions.

**Subgoal decomposition:**

1. **State the invariant-factor form and what uniqueness means.** Write $G \cong C_{d_1} \times \cdots \times C_{d_r}$ with $d_{i+1} \mid d_i$, and state that this list is unique; conclude $G \cong G'$ if and only if their lists agree.
   - *Hint:* The divisibility chain is what makes the list canonical — without it, $C_2 \times C_6$ and $C_6 \times C_2$ and $C_{12} \times C_1$ would be distinct "answers" for the same group.
   - *Why needed:* It is the normal form; everything else is derived from or converted into it.

2. **Existence $\Rightarrow$ elementary-divisor form, via the Chinese remainder theorem.** Given the invariant-factor decomposition, factor each $d_i = \prod_p p^{a_{i,p}}$ and apply [[Thm - Chinese Remainder Theorem for Cyclic Groups|Cₘₙ cong Cₘ times Cₙ for coprime m, n]] repeatedly to split $C_{d_i}$ into prime-power cyclic factors.
   - *Hint:* Distinct prime powers $p^a$ and $q^b$ are coprime, so the theorem applies; iterate over the primes dividing $d_i$.
   - *Why needed:* It produces the second normal form from the first, showing both describe the same group.

3. **Elementary divisors $\Rightarrow$ invariant factors, the column rule.** Group the elementary divisors by prime. For each prime $p$, list its prime-power elementary divisors in decreasing order. The largest invariant factor $d_1$ is the product, over all primes, of the *largest* prime-power for that prime; $d_2$ is the product of the *second-largest* for each prime; and so on. Pad shorter prime-lists with $1$s.
   - *Hint:* Lay the prime-power factors in a table, one row per prime, entries decreasing left to right; $d_j$ is the product of column $j$. Coprimality of the column entries plus the Chinese remainder theorem makes the product cyclic.
   - *Why needed:* It is the inverse conversion; together with subgoal 2 it proves the two forms are interchangeable, and it produces the canonical divisibility chain.

4. **Reduce counting to partitions.** Conclude that abelian groups of order $p^a$ correspond to partitions of $a$ (each partition $a = a_1 + a_2 + \cdots$ giving elementary divisors $p^{a_1}, p^{a_2}, \dots$), and abelian groups of order $\prod p_i^{a_i}$ correspond to tuples of partitions.
   - *Hint:* Verify on order $8 = 2^3$: partitions of $3$ are $3$, $2{+}1$, $1{+}1{+}1$, giving $C_8$, $C_4 \times C_2$, $C_2^3$.
   - *Why needed:* It is the form in which the classification is actually used to count.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes. They are the genuinely-local content of §1.6 — the existence-and-uniqueness lemma is flagged as the deferred input.

> [!note]- Lemma 1: Coprime cyclic factors fuse — the Chinese remainder step
> **Statement:** If $\gcd(m, n) = 1$ then $C_m \times C_n \cong C_{mn}$.
>
> **Hint:** Exhibit an element of order $mn$ in $C_m \times C_n$: a pair $(g, h)$ of generators has order $\operatorname{lcm}(m, n)$, and coprimality makes that $mn$. A group of order $mn$ with an element of order $mn$ is cyclic.
>
> **Why needed:** It is the engine of subgoal 2 — splitting each invariant-factor cyclic group $C_{d_i}$ into prime-power cyclic pieces — and the reassembly engine of subgoal 3.
>
> > [!note]- Full proof
> > This is exactly [[Thm - Chinese Remainder Theorem for Cyclic Groups]]; see that page for the complete proof. In brief: let $g$ generate $C_m$ and $h$ generate $C_n$. The element $(g, h) \in C_m \times C_n$ satisfies $(g, h)^k = (g^k, h^k) = (e, e)$ if and only if $m \mid k$ and $n \mid k$, i.e. if and only if $\operatorname{lcm}(m, n) \mid k$. Since $\gcd(m, n) = 1$, $\operatorname{lcm}(m, n) = mn$, so $\operatorname{ord}(g, h) = mn$. As $|C_m \times C_n| = mn$, the cyclic subgroup generated by $(g, h)$ is the whole group, so $C_m \times C_n \cong C_{mn}$.

> [!note]- Lemma 2: Every finite abelian group splits into prime-power cyclic factors, given any cyclic decomposition
> **Statement:** If a finite abelian group $G$ is a direct product of cyclic groups, then $G$ is a direct product of cyclic groups of *prime-power* order.
>
> **Hint:** Apply Lemma 1 in reverse to each cyclic factor: factor its order into prime powers and split.
>
> **Why needed:** It is subgoal 2 — the passage from the invariant-factor form to the elementary-divisor form — isolated as a standalone fact.
>
> > [!note]- Full proof
> > Suppose $G \cong C_{n_1} \times \cdots \times C_{n_r}$. Fix one factor $C_{n}$ and write $n = p_1^{a_1} \cdots p_k^{a_k}$ with the $p_j$ distinct primes. The prime powers $p_1^{a_1}, \dots, p_k^{a_k}$ are pairwise coprime, so by repeated application of Lemma 1,
> > $$C_n \cong C_{p_1^{a_1}} \times C_{p_2^{a_2}} \times \cdots \times C_{p_k^{a_k}}.$$
> > Doing this to every factor $C_{n_i}$ and collecting the prime-power cyclic groups produced gives $G$ as a direct product of prime-power cyclic groups. The multiset of prime powers obtained is the multiset of elementary divisors.

> [!note]- Lemma 3: Elementary divisors reassemble into invariant factors — the column rule
> **Statement:** Given the elementary divisors of $G$, define $d_1$ as the product over all primes $p$ of the largest $p$-power among the $p$-elementary-divisors, $d_2$ as the product of the second-largest, and so on (treating absent entries as $1$). Then each $d_{j+1} \mid d_j$, the $C_{d_j}$ are cyclic, and $\prod_j C_{d_j} \cong G$.
>
> **Hint:** Arrange the prime powers in a table — one row per prime, entries decreasing along each row. The $j$-th column has pairwise coprime entries, so its product is a cyclic group by Lemma 1; and the $(j{+}1)$-th column entries each divide the $j$-th, prime by prime, giving $d_{j+1} \mid d_j$.
>
> **Why needed:** It is subgoal 3 — the inverse conversion — and it is what produces the canonical decreasing divisibility chain.
>
> > [!note]- Full proof
> > For each prime $p$ dividing $|G|$, let the $p$-power elementary divisors be $p^{e_{p,1}} \geq p^{e_{p,2}} \geq \cdots$, listed in decreasing order and padded with $p^0 = 1$ so that every prime contributes the same number $r$ of entries (where $r$ is the maximum, over primes, of the count of $p$-elementary-divisors). Set
> > $$d_j = \prod_{p} p^{e_{p,j}}.$$
> > The factors $p^{e_{p,j}}$ for distinct $p$ are coprime, so by Lemma 1 the group $\prod_p C_{p^{e_{p,j}}}$ is cyclic of order $d_j$, i.e. $C_{d_j}$. Reassembling, $\prod_j C_{d_j} \cong \prod_j \prod_p C_{p^{e_{p,j}}} \cong \prod_p \prod_j C_{p^{e_{p,j}}} \cong G$, the last step because the right-hand double product is exactly the elementary-divisor decomposition. Finally, for each prime $p$ the exponents satisfy $e_{p,j+1} \leq e_{p,j}$ by the decreasing arrangement, so $p^{e_{p,j+1}} \mid p^{e_{p,j}}$; multiplying over all primes gives $d_{j+1} \mid d_j$. Discarding any $d_j = 1$ leaves the invariant-factor list with $d_r \geq 2$.

> [!note]- Lemma 4 (the deferred input): existence and uniqueness of the invariant-factor decomposition
> **Statement:** Every finite abelian group $G$ admits a decomposition $G \cong C_{d_1} \times \cdots \times C_{d_r}$ with $d_{i+1} \mid d_i$ and $d_r \geq 2$, and the list $(d_1, \dots, d_r)$ is uniquely determined by $G$.
>
> **Hint:** Existence: peel off a cyclic subgroup generated by an element of *maximal* order and show it is a direct factor; recurse on the quotient. Uniqueness: the multiplicities of the prime-power pieces are recovered as [[Def - Dimension|dimensions]] of the $\mathbb{Z}/p\mathbb{Z}$-vector spaces $\{x : p^k x = 0\}/\{x : p^{k-1}x = 0\}$, which are intrinsic to $G$.
>
> **Why needed:** It is the foundation on which Lemmas 2 and 3 build. **This lemma is not proved in §1.6** — it is the case $R = \mathbb{Z}$ of the structure theorem for finitely generated modules over a principal [[Def - Ideal|ideal]] domain, proved later in the course (Chapter 3). It is recorded here as the precise statement being imported, so the dependency is explicit.
>
> > [!note]- Why the proof is deferred, not omitted
> > The honest scope of §1.6 is to *state and apply* the classification, not to prove it, and the lecture notes say so explicitly: the classification "will be proved in Chapter 3 as a special case of the classification of modules over certain [[Def - Ring|rings]]". The reason for the deferral is structural rather than expository. The natural proof does not stay inside group theory: it treats a finite abelian group as a module over the principal ideal domain $\mathbb{Z}$ and runs a general argument — Smith normal form of a presentation matrix, or a maximal-order peeling argument — that works verbatim for finitely generated modules over *any* PID. Proving the abelian-group case in isolation would mean proving a special case of a theorem one is about to prove in full anyway, in less natural language (one would be re-deriving, by hand, the integer Smith normal form). The "Why Is It True" section above gives the genuine intuition — peel like a vector space, refine by the Chinese remainder theorem, uniqueness from intrinsic annihilator counts — and that intuition *is* the deferred proof in outline. What §1.6 owns, and what the other lemmas on this page prove in full, is the equivalence of the two normal forms.

---

# Formal Proof

> [!note]- Complete formal proof
> **What is proved here, and what is imported.** The classification has two halves. The half that is *deferred* — proved later in the course — is the existence and uniqueness of the invariant-factor decomposition (Lemma 4): that every finite abelian group $G$ is isomorphic to some $C_{d_1} \times \cdots \times C_{d_r}$ with $d_{i+1} \mid d_i$, with the list unique. This is the case $R = \mathbb{Z}$ of the structure theorem for finitely generated modules over a principal ideal domain, and the lecture notes defer it deliberately; it is not reproved here, because doing so means re-deriving the integer Smith normal form by hand. The half that *belongs to this topic*, and is proved in full below, is the **equivalence of the invariant-factor form and the elementary-divisor form** — the content that makes the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] the dictionary between the two faces of the classification.
>
> **Imported (deferred).** Existence and uniqueness of the invariant-factor decomposition, Lemma 4. We take as given: $G \cong C_{d_1} \times \cdots \times C_{d_r}$ with $d_{i+1} \mid d_i$, $d_r \geq 2$, and this list determined by $G$.
>
> **Claim (equivalence of forms).** $G$ also decomposes as a direct product of cyclic groups of prime-power order, and this multiset of prime powers — the elementary divisors — is unique; moreover the elementary-divisor data and the invariant-factor data determine each other.
>
> *Proof of the claim.*
>
> *From invariant factors to elementary divisors.* Take the imported decomposition $G \cong C_{d_1} \times \cdots \times C_{d_r}$. Fix an index $i$ and write the prime factorisation $d_i = p_1^{a_{i,1}} p_2^{a_{i,2}} \cdots p_k^{a_{i,k}}$ with distinct primes $p_j$. The prime powers $p_1^{a_{i,1}}, \dots, p_k^{a_{i,k}}$ are pairwise coprime, so applying [[Thm - Chinese Remainder Theorem for Cyclic Groups|the Chinese remainder theorem]] $C_{mn} \cong C_m \times C_n$ (for $\gcd(m,n) = 1$) repeatedly,
> $$C_{d_i} \;\cong\; C_{p_1^{a_{i,1}}} \times C_{p_2^{a_{i,2}}} \times \cdots \times C_{p_k^{a_{i,k}}}.$$
> Performing this for every $i$ and collecting all the prime-power cyclic factors,
> $$G \;\cong\; \prod_{i=1}^{r} C_{d_i} \;\cong\; \prod_{i=1}^{r} \prod_{j} C_{p_j^{a_{i,j}}},$$
> a direct product of cyclic groups of prime-power order. The multiset of prime powers $\{p_j^{a_{i,j}} : a_{i,j} > 0\}$ is the multiset of **elementary divisors**.
>
> *From elementary divisors to invariant factors.* Conversely, suppose $G \cong \prod_j C_{q_j}$ with each $q_j$ a prime power. Group the $q_j$ by their prime: for each prime $p$ dividing $|G|$, let the $p$-power factors be $p^{e_{p,1}} \geq p^{e_{p,2}} \geq \cdots$, written in decreasing order of exponent and padded by $p^0 = 1$ so that, with $r := \max_p (\text{number of } p\text{-power factors})$, every prime contributes exactly $r$ entries. Define
> $$d_j \;=\; \prod_{p \,\mid\, |G|} p^{\,e_{p,j}}, \qquad j = 1, \dots, r.$$
> For fixed $j$, the factors $p^{e_{p,j}}$ over distinct primes $p$ are pairwise coprime, so by the Chinese remainder theorem $\prod_p C_{p^{e_{p,j}}} \cong C_{d_j}$. Therefore
> $$\prod_{j=1}^{r} C_{d_j} \;\cong\; \prod_{j=1}^{r} \prod_{p} C_{p^{e_{p,j}}} \;\cong\; \prod_{p} \prod_{j=1}^{r} C_{p^{e_{p,j}}} \;\cong\; G,$$
> the reordering of factors being legal because the direct product is commutative and associative up to isomorphism, and the last isomorphism holding because $\prod_p \prod_j C_{p^{e_{p,j}}}$ is precisely the elementary-divisor decomposition. Finally the divisibility chain: for each prime $p$, the decreasing arrangement gives $e_{p,j+1} \leq e_{p,j}$, hence $p^{e_{p,j+1}} \mid p^{e_{p,j}}$; multiplying these divisibilities over all primes $p$ yields $d_{j+1} \mid d_j$. Discarding any $d_j$ equal to $1$ leaves a list with $d_r \geq 2$, which is the invariant-factor list.
>
> *Uniqueness of the elementary divisors.* The two conversions are mutually inverse: starting from invariant factors, splitting into prime powers, and reassembling by the column rule returns the original $d_i$ (at each prime, splitting then re-collecting the same decreasing exponent sequence is the identity). Hence the elementary-divisor multiset and the invariant-factor list carry the same information. Since the invariant-factor list is unique by the imported Lemma 4, the elementary-divisor multiset is unique as well. $\qquad\blacksquare$
>
> **Consequence — the count.** The elementary divisors at a prime $p$ are a multiset of powers $p^{a_1}, p^{a_2}, \dots$ whose exponents $a_1 + a_2 + \cdots$ sum to the exponent of $p$ in $|G|$. Choosing them is therefore choosing a **partition** of that exponent. Hence the number of isomorphism types of abelian groups of order $p^a$ is the number of partitions $\mathfrak{p}(a)$, and for $|G| = \prod_i p_i^{a_i}$ the number of types is $\prod_i \mathfrak{p}(a_i)$.
>
> **Worked example, order $8$.** Here $8 = 2^3$, so abelian groups of order $8$ correspond to partitions of $3$: the partition $3$ gives elementary divisor $2^3$, hence $C_8$; the partition $2 + 1$ gives $\{2^2, 2\}$, hence $C_4 \times C_2$; the partition $1 + 1 + 1$ gives $\{2, 2, 2\}$, hence $C_2 \times C_2 \times C_2$. There are $\mathfrak{p}(3) = 3$ of them, and the corresponding invariant-factor lists, by the column rule applied to a single prime, are $(8)$, $(4, 2)$, $(2, 2, 2)$.

---

# Cross-Field Exercise Suggestions

The aim is to find settings where the classification applies but is not advertised — to battle-test recognition of the *sources*.

**Number theory: the multiplicative group of a finite field is cyclic.** The nonzero elements of a finite field $\mathbb{F}_q$ form a finite abelian group $\mathbb{F}_q^\times$ of order $q - 1$ under multiplication. By the classification it has invariant factors $d_1 \geq d_2 \geq \cdots$ with $d_{i+1} \mid d_i$; one shows $r = 1$ by observing that every element of $\mathbb{F}_q^\times$ satisfies $x^{d_1} = 1$, so the polynomial $X^{d_1} - 1$ has all $q - 1$ elements as roots — but a polynomial of degree $d_1$ over a field has at most $d_1$ roots, forcing $d_1 \geq q - 1$, hence $d_1 = q-1$ and the group is cyclic. The application is non-obvious because the statement "$\mathbb{F}_q^\times$ is cyclic" is usually proved by hand with totient sums; the property $B$ "$\mathbb{F}_q^\times$ is a finite abelian group" routes it instead through the classification's *largest-invariant-factor-is-the-exponent* target.

**Linear algebra: Jordan and rational canonical forms.** A single linear operator $T$ on a finite-dimensional vector space $V$ over a field $k$ makes $V$ into a module over the polynomial [[Def - Ring|ring]] $k[X]$, with $X$ acting as $T$. The ring $k[X]$ is a principal ideal domain, so the *same* structure theorem that gives the classification of finite abelian groups (the $R = \mathbb{Z}$ case) gives, at $R = k[X]$, a decomposition of $V$ into cyclic $k[X]$-modules — and that decomposition is exactly the rational canonical form, or, after splitting by the Chinese remainder theorem into prime-power pieces, the Jordan canonical form. The non-obvious step is recognising that "classifying $T$ up to similarity" is "classifying a finitely generated module over a PID", the very problem the classification of finite abelian groups is the baby case of.

**Combinatorics: counting [[Def - Subgroup|subgroups]] via partitions.** Ask how many [[Def - Subgroup|subgroups]] of order $p^2$ a group of order $p^4$ has. If the group is abelian, the classification reduces it entirely to the partition of $4$ describing the group (the partition $4$, $3{+}1$, $2{+}2$, $2{+}1{+}1$, or $1{+}1{+}1{+}1$), after which subgroup-counting becomes a combinatorial enumeration over the lattice of sub-partitions. The application is non-obvious because the problem is posed as subgroup enumeration with no mention of decomposition; the property $B$ "$G$ is a finite abelian $p$-group" turns the entire question into combinatorics of Young diagrams.

**Topology: the homology of a finite simplicial complex.** The homology groups $H_n(X; \mathbb{Z})$ of a finite simplicial complex are finitely generated abelian groups, and their *torsion* subgroups are finite abelian groups. The classification supplies the canonical form of each torsion subgroup — its invariant factors are the **torsion coefficients** of the space, genuine topological invariants distinguishing, for instance, the Klein bottle from the torus. The non-obvious recognition is that a torsion homology group, presented as the quotient of a cycle group by a boundary group, is a finite abelian group to which the classification applies, turning algebraic topology's invariants into integer lists.

---

# Bridges

- **[[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese Remainder Theorem for Cyclic Groups]]** — this is not merely related to the classification, it is the *dictionary* internal to it. The invariant-factor form and the elementary-divisor form describe the same groups, and the Chinese remainder theorem $C_{mn} \cong C_m \times C_n$ (for coprime $m, n$) is the explicit isomorphism that converts one form into the other: splitting invariant factors into prime powers in one direction, fusing prime powers across distinct primes back into invariant factors in the other. Without it the two faces of the classification would be two separate theorems.

- **[[Def - Direct Product|Direct Product]]** — the classification is a statement *about* direct products: it says the direct product of cyclic groups is the *only* way a finite abelian group is ever built. Every finite abelian group is an internal direct product of cyclic subgroups, and the recognition criterion for internal direct products is what lets one verify a proposed decomposition. The classification is, in a sense, the theorem that the direct product of cyclic groups exhausts the abelian world.

- **Structure Theorem for Finitely Generated Modules over a PID** *(from Rings and Modules)* — this is the genuine home of the proof. A finite abelian group is exactly a finite $\mathbb{Z}$-module; the structure theorem says every finitely generated module over a principal ideal domain $R$ is a direct sum of cyclic modules $R/(d_i)$ with $d_i \mid d_{i+1}$, and the classification of finite abelian groups is the case $R = \mathbb{Z}$ restricted to finite (equivalently, torsion) modules. The invariant factors are the same $d_i$. This is why the proof is deferred — it is most naturally a corollary of the more general theorem.

- **[[Thm - Quotient by the Centre and Commutativity|Order-p² groups are abelian]]** — this small theorem is one of the standard *sources* feeding the classification: it certifies that a group of order $p^2$, presented with no commutativity hypothesis, is in fact abelian, after which the classification applies and forces $G$ to be $C_{p^2}$ or $C_p \times C_p$. The two theorems compose to give the complete list of groups of order $p^2$.

- **Classification of Finite Simple Groups** — the abelian classification is the easy, fully-elementary end of the classification programme; the simple-group classification is the impossibly hard non-abelian end. They bracket the subject: abelian groups are completely understood by a one-page theorem, while the non-abelian simple groups required a multi-thousand-page collective effort, and most finite groups sit between, assembled from simple [[Thm - Composition Series|composition factors]] by extensions.

# Unlocked by This

> [!tip] Smith Normal Form *(from Rings and Modules / Computational Algebra)*
> The classification's invariant factors are computed, for a concretely presented abelian group $\mathbb{Z}^n / L$, as the diagonal entries of the **Smith normal form** of an integer matrix whose columns generate the relation lattice $L$. Smith normal form is the algorithm that makes the classification *effective* — it turns "find the invariant factors" from an existence statement into a finite computation, and the same algorithm over $k[X]$ produces canonical forms of matrices.

> [!tip] Pontryagin Duality *(from Harmonic Analysis on Groups)*
> A finite abelian group $G$ is canonically isomorphic to its **dual** $\hat G = \operatorname{Hom}(G, \mathbb{C}^\times)$, the group of characters; the classification is what makes this concrete, since the dual of $C_n$ is again $C_n$ and duality respects direct products. This is the finite, baby case of Pontryagin duality, the foundation of the Fourier transform on locally compact abelian groups.

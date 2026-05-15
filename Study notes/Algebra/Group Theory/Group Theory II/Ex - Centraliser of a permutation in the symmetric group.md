---
type: exercise
subject: group-theory
difficulty: "⭐"
prereqs:
  - "Def - Symmetric Group"
  - "Def - Conjugacy Class"
  - "Def - Centraliser and Centre"
  - "Thm - Orbit-Stabiliser Theorem"
  - "Thm - Conjugacy Classes of the Symmetric Group"
tags: [algebra, group-theory]
---

# Problem Statement

Let $S_n$ be the symmetric group on $\{1, \dots, n\}$.

1. Let $\sigma \in S_n$ be a single $n$-cycle, for instance $\sigma = (1\,2\,\cdots\,n)$. Compute the centraliser $C_{S_n}(\sigma)$ — both its order and, explicitly, which permutations belong to it.
2. Compute the centraliser $C_{S_4}\big((1\,2)(3\,4)\big)$ inside $S_4$: find its order and identify the group up to isomorphism.

**Recall:**

The objects in play are a symmetric group, the conjugacy class of one of its elements, and the centraliser of that element.

![[Def - Symmetric Group#The Definition]]

The [[Def - Conjugacy Class|conjugacy class]] of $g$ in a group $G$ is $\operatorname{ccl}_G(g) = \{hgh^{-1} : h \in G\}$ — the set of all conjugates of $g$, equivalently the orbit of $g$ under the action of $G$ on itself by conjugation.

![[Def - Centraliser and Centre#The Definition]]

So the [[Def - Centraliser and Centre|centraliser]] $C_G(g) = \{h \in G : hg = gh\}$ is the set of elements that commute with $g$; it is a [[Def - Subgroup|subgroup]] of $G$, and it is exactly the stabiliser of $g$ under the conjugation action.

Two further facts are needed. The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]], applied to conjugation, says that for a finite group the conjugacy class size and the centraliser order multiply to $|G|$:
$$|\operatorname{ccl}_G(g)| \cdot |C_G(g)| = |G|, \qquad \text{so} \qquad |\operatorname{ccl}_G(g)| = |G : C_G(g)|.$$
And the classification of conjugacy in symmetric groups ([[Thm - Conjugacy Classes of the Symmetric Group]]) says two permutations of $S_n$ are conjugate **if and only if they have the same cycle type** — the same multiset of disjoint-cycle lengths. The class of an $n$-cycle is therefore all $n$-cycles; the class of $(1\,2)(3\,4)$ in $S_4$ is all permutations of cycle type "two $2$-cycles".

---

# Convergent Strategy

**Problem class.** This is a *compute a centraliser* problem, and the [[Group Theory II — §1.3–1.4#Problem-Solving Strategy|problem-solving strategy]] of the topic page is explicit about the route: a centraliser is a stabiliser for the conjugation action, so its order is governed by the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]]. The deliberate move is to refuse to hunt for commuting elements one by one and instead count the conjugacy class, because the class size and the centraliser order are two faces of the same equation.

**Assumption pattern.** The group is a [[Def - Symmetric Group|symmetric group]] and the element is given by its cycle type — a single $n$-cycle in part 1, cycle type $(2,2)$ in part 2. Cycle type is exactly the data that controls conjugacy in $S_n$, so the assumption is tailored to make the conjugacy class *visible*: we can see what the whole class is without computing a single conjugate.

**Theorem routing.** The route has two links. First [[Thm - Conjugacy Classes of the Symmetric Group|conjugacy = cycle type]] turns "the class of $\sigma$" into "all permutations of $\sigma$'s cycle type", a set we can count by elementary combinatorics. Then the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] in the form $|C_{S_n}(\sigma)| = |S_n| / |\operatorname{ccl}(\sigma)|$ converts that count into the centraliser's order. The class size is the *input*; the centraliser order is the *output*.

**Key decision point.** Orbit-stabiliser delivers the *order* of the centraliser but not its *elements*. The genuinely interesting step is to close that gap. For the $n$-cycle one exhibits $n$ obvious commuting elements — the powers $\sigma^0, \sigma^1, \dots, \sigma^{n-1}$ — and observes that there are exactly $n$ slots to fill, so these powers *are* the entire centraliser: $C_{S_n}(\sigma) = \langle \sigma \rangle$. For $(1\,2)(3\,4)$ the order comes out as $8$, and the decision is to recognise the group of order $8$ that actually sits inside $S_4$ stabilising this element — it is a copy of the dihedral group $D_8$, the symmetries of a square. The skill is using a counting bound to pin down an algebraic object exactly.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory II — §1.3–1.4#Legal Operations|the topic page's Legal Operations]]:

1. **Act on the group itself by conjugation** (operation 5). The centraliser only *means* anything as the stabiliser of $\sigma$ for the conjugation action of $S_n$ on itself; setting up that action is what makes orbit-stabiliser applicable.

2. **Read conjugacy in $S_n$ off cycle type** (operation 8). Used to identify the conjugacy class of $\sigma$ with the set of all permutations of its cycle type, so that the class can be counted by hand.

3. **Count conjugates by the index of a centraliser** (operation 7). The conjugacy class size equals $|S_n : C_{S_n}(\sigma)|$; running this equation backwards turns a known class size into the centraliser's order.

4. **Apply the orbit-stabiliser theorem** (operation 2). The arithmetic identity $|\operatorname{ccl}(\sigma)| \cdot |C_{S_n}(\sigma)| = |S_n|$ is precisely orbit-stabiliser for the conjugation action, and it is the single equation that does the computation.

---

# Hints

> [!note]- Hint 1
> Do not try to list every permutation that commutes with $\sigma$ by trial. The centraliser is the *stabiliser* of $\sigma$ under conjugation, so its order is tied to the size of $\sigma$'s orbit — its conjugacy class — by the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]]. Count the conjugacy class first.

> [!note]- Hint 2
> In $S_n$, the conjugacy class of an element is exactly the set of all permutations with the **same cycle type** ([[Thm - Conjugacy Classes of the Symmetric Group]]). How many $n$-cycles are there in $S_n$? How many permutations of $S_4$ have cycle type "two disjoint $2$-cycles"? Count those sets directly.

> [!note]- Hint 3
> For the $n$-cycle: once orbit-stabiliser gives $|C_{S_n}(\sigma)| = n$, notice that $\sigma$ certainly commutes with each of its own powers $e, \sigma, \sigma^2, \dots, \sigma^{n-1}$ — and there are exactly $n$ of them. A subgroup of order $n$ containing $n$ known elements *is* those elements. For $(1\,2)(3\,4) \in S_4$: the count gives a centraliser of order $8$; think about which order-$8$ subgroup of $S_4$ fixes this element under conjugation.

---

# Solution

The strategy is uniform: identify the conjugacy class via cycle type, count it, divide $|S_n|$ by that count to get the centraliser's order, then identify the centraliser as a concrete subgroup.

**Step 1: The conjugacy class of an $n$-cycle has size $(n-1)!$.**

By [[Thm - Conjugacy Classes of the Symmetric Group|conjugacy = cycle type]], the class of $\sigma$ is the set of *all* $n$-cycles in $S_n$, and there are exactly $(n-1)!$ of them.

> [!note]- Derivation
> Conjugate permutations in $S_n$ have the same cycle type, and conversely any two permutations of the same cycle type are conjugate — this is the content of [[Thm - Conjugacy Classes of the Symmetric Group]]. The cycle type of $\sigma = (1\,2\,\cdots\,n)$ is a single cycle of length $n$, so
> $$\operatorname{ccl}_{S_n}(\sigma) = \{\text{all } n\text{-cycles in } S_n\}.$$
>
> Now count the $n$-cycles. An $n$-cycle moves all $n$ points in a single loop. Write it as $(a_1\,a_2\,\cdots\,a_n)$ where $a_1, \dots, a_n$ is some ordering of $\{1, \dots, n\}$; there are $n!$ such orderings. But each $n$-cycle is counted $n$ times, once for each choice of starting point: the cycle $(a_1\,a_2\,\cdots\,a_n)$ is literally the same permutation as $(a_2\,a_3\,\cdots\,a_n\,a_1)$, and so on through all $n$ cyclic rotations of the list. Hence the number of distinct $n$-cycles is
> $$\frac{n!}{n} = (n-1)!.$$
> So $|\operatorname{ccl}_{S_n}(\sigma)| = (n-1)!$.

**Step 2: Therefore $|C_{S_n}(\sigma)| = n$.**

The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] turns the class size into the centraliser order: $|C_{S_n}(\sigma)| = |S_n| / |\operatorname{ccl}(\sigma)| = n! / (n-1)! = n$.

> [!note]- Derivation
> The centraliser $C_{S_n}(\sigma)$ is the stabiliser of $\sigma$ under the conjugation action of $S_n$ on itself, and the conjugacy class $\operatorname{ccl}_{S_n}(\sigma)$ is the orbit. The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] states that orbit size times stabiliser size equals the order of the acting group:
> $$|\operatorname{ccl}_{S_n}(\sigma)| \cdot |C_{S_n}(\sigma)| = |S_n| = n!.$$
> Substituting $|\operatorname{ccl}_{S_n}(\sigma)| = (n-1)!$ from Step 1,
> $$|C_{S_n}(\sigma)| = \frac{n!}{(n-1)!} = n.$$

**Step 3: The centraliser of an $n$-cycle is exactly the cyclic subgroup $\langle \sigma \rangle$.**

The $n$ powers $e, \sigma, \sigma^2, \dots, \sigma^{n-1}$ all commute with $\sigma$ and are distinct; since the centraliser has order exactly $n$, these powers fill it completely: $C_{S_n}(\sigma) = \langle \sigma \rangle$.

> [!note]- Derivation
> Any element commutes with any power of itself: $\sigma \cdot \sigma^k = \sigma^{k+1} = \sigma^k \cdot \sigma$. So every power $\sigma^k$ lies in $C_{S_n}(\sigma)$, and hence the cyclic subgroup $\langle \sigma \rangle$ is contained in $C_{S_n}(\sigma)$:
> $$\langle \sigma \rangle \leq C_{S_n}(\sigma).$$
> An $n$-cycle has order exactly $n$ — applying $\sigma$ repeatedly cycles each point through all $n$ positions, returning home only after $n$ steps — so $|\langle \sigma \rangle| = n$. By Step 2 the centraliser also has order $n$. A subgroup of order $n$ contained in a group of order $n$ must be the whole group, so
> $$C_{S_n}(\sigma) = \langle \sigma \rangle = \{e, \sigma, \sigma^2, \dots, \sigma^{n-1}\}.$$
> The permutations commuting with an $n$-cycle are precisely its own powers — nothing else.

**Step 4: The conjugacy class of $(1\,2)(3\,4)$ in $S_4$ has size $3$.**

The class of $(1\,2)(3\,4)$ is all permutations of $S_4$ of cycle type $(2,2)$, and there are exactly three of them.

> [!note]- Derivation
> Again by [[Thm - Conjugacy Classes of the Symmetric Group|conjugacy = cycle type]], the conjugacy class of $(1\,2)(3\,4)$ in $S_4$ is the set of all permutations whose disjoint-cycle decomposition consists of two $2$-cycles (and no fixed points, since $2 + 2 = 4$).
>
> Count them directly. A permutation of cycle type $(2,2)$ on $\{1,2,3,4\}$ is determined by how $\{1,2,3,4\}$ is partitioned into two unordered pairs — once the pairs are chosen, each pair becomes a transposition and there is no further freedom. The number of ways to split four points into two unordered pairs is $3$:
> $$\{1,2\}\,|\,\{3,4\}, \qquad \{1,3\}\,|\,\{2,4\}, \qquad \{1,4\}\,|\,\{2,3\}.$$
> So the three permutations of this cycle type are
> $$(1\,2)(3\,4), \qquad (1\,3)(2\,4), \qquad (1\,4)(2\,3),$$
> and $|\operatorname{ccl}_{S_4}((1\,2)(3\,4))| = 3$.

**Step 5: Therefore $|C_{S_4}((1\,2)(3\,4))| = 8$, and the centraliser is a copy of $D_8$.**

Orbit-stabiliser gives $|C_{S_4}((1\,2)(3\,4))| = 24/3 = 8$. The order-$8$ subgroup of $S_4$ fixing $(1\,2)(3\,4)$ under conjugation is a dihedral group $D_8$ — the symmetry group of a square.

> [!note]- Derivation
> By the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] applied to conjugation in $S_4$, with $|S_4| = 4! = 24$,
> $$|C_{S_4}\big((1\,2)(3\,4)\big)| = \frac{|S_4|}{|\operatorname{ccl}_{S_4}((1\,2)(3\,4))|} = \frac{24}{3} = 8.$$
>
> To identify this subgroup of order $8$, write $\sigma = (1\,2)(3\,4)$ and list elements that commute with it. An element $h$ centralises $\sigma$ exactly when $h\sigma h^{-1} = \sigma$, i.e. when conjugation by $h$ — which relabels the points by $h$ — leaves the pair-partition $\{\{1,2\},\{3,4\}\}$ unchanged. So $h$ must permute $\{1,2,3,4\}$ in a way that maps the set $\{1,2\}$ to one of the two blocks and $\{3,4\}$ to the other. The permutations doing this are:
>
> - the identity $e$;
> - $\sigma = (1\,2)(3\,4)$ itself, $(1\,2)$, and $(3\,4)$ — these fix each block setwise;
> - $(1\,3)(2\,4)$ and $(1\,4)(2\,3)$ — these swap the two blocks;
> - $(1\,3\,2\,4)$ and $(1\,4\,2\,3)$ — the two $4$-cycles that swap the blocks.
>
> That is exactly eight permutations, matching the count. This group is generated by the two elements $a = (1\,3\,2\,4)$ and $b = (1\,2)$: a direct check gives $a^4 = e$, $b^2 = e$, and $bab^{-1} = a^{-1}$. These are the defining relations of the **dihedral group** $D_8$ of order $8$, the group of symmetries of a square. The geometric picture is exact: place $1,2,3,4$ at the corners of a square so that $1,2$ are one diagonal pair and $3,4$ the other; then "permutations preserving the partition into diagonal pairs" are precisely the eight rigid symmetries of the square. So
> $$C_{S_4}\big((1\,2)(3\,4)\big) \cong D_8.$$

> [!note]- Complete formal solution
> **Part 1.** Let $\sigma = (1\,2\,\cdots\,n) \in S_n$ be an $n$-cycle.
>
> By [[Thm - Conjugacy Classes of the Symmetric Group]], two permutations of $S_n$ are conjugate if and only if they have the same cycle type, so $\operatorname{ccl}_{S_n}(\sigma)$ is the set of all $n$-cycles in $S_n$. An $n$-cycle written as an ordered list $(a_1\,\cdots\,a_n)$ corresponds to an ordering of $\{1,\dots,n\}$, of which there are $n!$, and each $n$-cycle arises from exactly $n$ orderings (its $n$ cyclic rotations). Hence
> $$|\operatorname{ccl}_{S_n}(\sigma)| = \frac{n!}{n} = (n-1)!.$$
>
> The centraliser $C_{S_n}(\sigma)$ is the stabiliser of $\sigma$ for the conjugation action of $S_n$ on itself, with orbit $\operatorname{ccl}_{S_n}(\sigma)$. By the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]],
> $$|C_{S_n}(\sigma)| = \frac{|S_n|}{|\operatorname{ccl}_{S_n}(\sigma)|} = \frac{n!}{(n-1)!} = n.$$
>
> Every power $\sigma^k$ commutes with $\sigma$, so $\langle\sigma\rangle \leq C_{S_n}(\sigma)$. Since $\sigma$ is an $n$-cycle it has order $n$, so $|\langle\sigma\rangle| = n = |C_{S_n}(\sigma)|$. A subgroup of order $n$ inside a group of order $n$ is the whole group, hence
> $$C_{S_n}(\sigma) = \langle\sigma\rangle = \{e, \sigma, \sigma^2, \dots, \sigma^{n-1}\}.$$
>
> **Part 2.** Let $\sigma = (1\,2)(3\,4) \in S_4$, of cycle type $(2,2)$.
>
> By [[Thm - Conjugacy Classes of the Symmetric Group]], $\operatorname{ccl}_{S_4}(\sigma)$ is the set of permutations of cycle type $(2,2)$. Such a permutation is determined by a partition of $\{1,2,3,4\}$ into two unordered pairs, of which there are $3$: $\{1,2\}|\{3,4\}$, $\{1,3\}|\{2,4\}$, $\{1,4\}|\{2,3\}$. So
> $$|\operatorname{ccl}_{S_4}(\sigma)| = 3.$$
>
> By the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] with $|S_4| = 24$,
> $$|C_{S_4}(\sigma)| = \frac{24}{3} = 8.$$
>
> The eight elements are the permutations of $\{1,2,3,4\}$ that preserve the partition $\{\{1,2\},\{3,4\}\}$:
> $$e,\ (1\,2),\ (3\,4),\ (1\,2)(3\,4),\ (1\,3)(2\,4),\ (1\,4)(2\,3),\ (1\,3\,2\,4),\ (1\,4\,2\,3).$$
> Setting $a = (1\,3\,2\,4)$ and $b = (1\,2)$, one checks $a^4 = e$, $b^2 = e$, $bab^{-1} = a^{-1}$ — the defining relations of the dihedral group of order $8$. Therefore
> $$C_{S_4}\big((1\,2)(3\,4)\big) \cong D_8. \qquad \blacksquare$$

---

# Key Takeaways

**Compute a centraliser by counting its conjugacy class, never by hunting for commuting elements.** The reflex this exercise installs is the recognition that a centraliser is a *stabiliser in disguise* — the stabiliser of $g$ for the conjugation action — and that stabilisers are reached through the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] rather than by direct search. The conjugacy class is the orbit, so once you know $|G|$ and the class size you know the centraliser order by a single division, $|C_G(g)| = |G|/|\operatorname{ccl}_G(g)|$. This inverts the difficulty in your favour: counting a conjugacy class is often elementary combinatorics, whereas testing the commuting condition $hg = gh$ element by element is hopeless even in $S_4$. The trigger is any phrase of the form "find the centraliser of $g$" or "how many elements commute with $g$" — and the first move is always to ask what the orbit of $g$ under conjugation is and how big it is. The same logic, run the other way, computes a conjugacy class size when the centraliser is the visible object.

**In a symmetric group the conjugacy class is free, because cycle type is the complete invariant.** Symmetric groups are the one infinite family of groups whose conjugacy structure is completely transparent: by [[Thm - Conjugacy Classes of the Symmetric Group|conjugacy = cycle type]], the class of a permutation is *every* permutation with the same multiset of disjoint-cycle lengths, and that set can be counted by pure combinatorics. The two counts in this exercise — $n$-cycles via "$n!$ orderings, each cycle counted $n$ times", and cycle type $(2,2)$ via "partition four points into two pairs" — are templates. Whenever a problem about $S_n$ asks for a conjugacy class, a centraliser, or whether two permutations are conjugate, you should reach immediately for cycle type. It converts a group-theoretic question into a question about partitions of $n$, where everything is finite, concrete, and checkable by hand. This is what makes $S_n$ the natural laboratory for the conjugation action.

**An order from orbit-stabiliser plus a few obvious elements can pin a subgroup down exactly.** Orbit-stabiliser is generous with *cardinality* but silent about *which* elements form the subgroup — and that gap is closed by a counting squeeze. For the $n$-cycle the move is canonical: the powers of $\sigma$ visibly commute with $\sigma$ and there are exactly $n$ of them, so once the order is known to be $n$, the inclusion $\langle\sigma\rangle \leq C_{S_n}(\sigma)$ between two groups of equal order is forced to be an equality, and the centraliser is identified as $\langle\sigma\rangle$ with no further work. The general pattern — exhibit an obvious subgroup, compute the ambient order, and conclude equality when the orders match — is one of the most reliable identification techniques in finite group theory. It also rewards knowing the small groups: a centraliser of order $8$ sitting inside $S_4$ and stabilising a $(2,2)$-element could in principle be cyclic, $C_2 \times C_2 \times C_2$, $C_4 \times C_2$, the quaternion group, or dihedral — and recognising it as $D_8$, the square's symmetry group acting on the diagonal-pair partition, comes from carrying a working catalogue of the order-$8$ groups and matching the relations $a^4 = b^2 = e$, $bab^{-1} = a^{-1}$.

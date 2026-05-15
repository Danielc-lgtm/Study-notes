---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Symmetric Group"
  - "Def - Conjugacy Class"
  - "Def - Centraliser and Centre"
  - "Thm - Orbit-Stabiliser Theorem"
  - "Thm - Conjugacy Classes of the Symmetric Group"
tags: [algebra, group-theory]
---

# Problem Statement

Let $\sigma \in S_n$ be a permutation whose disjoint-cycle decomposition has exactly $a_k$ cycles of length $k$, for each $k = 1, 2, \dots, n$ (cycles of length $1$ being fixed points). The data $(a_1, a_2, \dots, a_n)$ is the **cycle type** of $\sigma$, and it satisfies the constraint
$$\sum_{k=1}^{n} k\, a_k = n.$$
Prove that the conjugacy class of $\sigma$ in $S_n$ has size
$$\big|\operatorname{ccl}_{S_n}(\sigma)\big| = \frac{n!}{\displaystyle\prod_{k=1}^{n} k^{a_k}\, a_k!}.$$
Equivalently, prove that the centraliser of $\sigma$ has order $|C_{S_n}(\sigma)| = \prod_{k} k^{a_k}\, a_k!$.

**Recall:**

The objects in play are a symmetric group, the conjugacy class of one of its elements, and the centraliser of that element.

![[Def - Symmetric Group#The Definition]]

The [[Def - Conjugacy Class|conjugacy class]] of $\sigma$ is $\operatorname{ccl}_{S_n}(\sigma) = \{\tau\sigma\tau^{-1} : \tau \in S_n\}$ — the orbit of $\sigma$ under conjugation. The [[Def - Centraliser and Centre|centraliser]] $C_{S_n}(\sigma) = \{\tau \in S_n : \tau\sigma = \sigma\tau\}$ is the subgroup of permutations commuting with $\sigma$; it is the stabiliser of $\sigma$ for the conjugation action.

The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] applied to conjugation gives $|\operatorname{ccl}_{S_n}(\sigma)| \cdot |C_{S_n}(\sigma)| = |S_n| = n!$.

The mechanism of conjugation in $S_n$ ([[Thm - Conjugacy Classes of the Symmetric Group]]) is the key computational fact: conjugating a permutation **relabels the points it moves**. Concretely, if $\sigma$ contains the cycle $(x_1\, x_2\, \cdots\, x_k)$, then for any $\tau \in S_n$,
$$\tau\sigma\tau^{-1} \text{ contains the cycle } \big(\tau(x_1)\ \tau(x_2)\ \cdots\ \tau(x_k)\big).$$
In words: to compute $\tau\sigma\tau^{-1}$, take the cycle notation of $\sigma$ and replace every entry $x$ by $\tau(x)$. The cycle *lengths* are untouched, so $\tau\sigma\tau^{-1}$ has the same cycle type as $\sigma$ — which is why conjugate permutations have equal cycle type.

---

# Convergent Strategy

**Problem class.** This is a *count a conjugacy class* problem, the recurring computational task of §1.4. The [[Group Theory II — §1.3–1.4#Problem-Solving Strategy|topic page's strategy]] prescribes the route directly: a conjugacy class is an orbit of the conjugation action, so its size is the index of a [[Def - Centraliser and Centre|centraliser]] by the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]]. The class size is hard to count head-on but the centraliser order is structured and countable, so the productive direction is to compute the centraliser and divide $n!$ by it.

**Assumption pattern.** The group is a [[Def - Symmetric Group|symmetric group]] and the element is specified by its cycle type $(a_1, \dots, a_n)$. Cycle type is precisely the invariant that determines conjugacy in $S_n$, so the assumption hands us, for free, a complete description of the centraliser's *job*: a permutation $\tau$ centralises $\sigma$ exactly when relabelling $\sigma$'s cycles by $\tau$ reproduces $\sigma$. The assumption converts an abstract count into a concrete combinatorial bookkeeping of "ways to relabel without changing the picture".

**Theorem routing.** Two theorems do the work. [[Thm - Conjugacy Classes of the Symmetric Group|Conjugation relabels cycle entries]] turns "$\tau$ commutes with $\sigma$" into "$\tau$ permutes $\sigma$'s disjoint cycles among themselves and rotates within them" — a condition we can enumerate. Counting those $\tau$ gives $|C_{S_n}(\sigma)| = \prod_k k^{a_k} a_k!$. Then the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]], $|\operatorname{ccl}(\sigma)| = |S_n|/|C_{S_n}(\sigma)|$, delivers the class-size formula. The centraliser is the *computed* object; the class size is *read off* by division.

**Key decision point.** The whole problem turns on correctly enumerating the centraliser, and there are exactly two independent freedoms a centralising $\tau$ has — both must be found, and neither double-counted. First, $\tau$ may **permute the $a_k$ cycles of each fixed length $k$ among one another** ($a_k!$ ways, since cycles of the same length are interchangeable); these choices are independent across different lengths $k$, contributing $\prod_k a_k!$. Second, $\tau$ may **cyclically rotate the labelling within each individual cycle** ($k$ ways for a $k$-cycle, because a $k$-cycle has $k$ equivalent starting points); over all cycles this contributes $\prod_k k^{a_k}$. The non-obvious part is seeing that these are the *only* freedoms and that they multiply independently — that a centralising permutation is nothing more than (a shuffle of equal-length cycles) composed with (an internal rotation of each). Missing the within-cycle rotations, or the cross-cycle shuffles, or double-counting their overlap, are the three ways the count goes wrong.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory II — §1.3–1.4#Legal Operations|the topic page's Legal Operations]]:

1. **Act on the group itself by conjugation** (operation 5). The conjugacy class is the orbit and the centraliser is the stabiliser of $\sigma$ under conjugation; this action is the setting in which orbit-stabiliser applies.

2. **Read conjugacy in $S_n$ off cycle type** (operation 8). The relabelling description of conjugation — $\tau\sigma\tau^{-1}$ is $\sigma$ with each entry $x$ replaced by $\tau(x)$ — is the tool that translates "$\tau$ commutes with $\sigma$" into a combinatorial condition on how $\tau$ moves $\sigma$'s cycles.

3. **Count conjugates by the index of a centraliser** (operation 7). The class size equals $|S_n : C_{S_n}(\sigma)|$; the strategy is to compute the centraliser order and then take the index.

4. **Apply the orbit-stabiliser theorem** (operation 2). The identity $|\operatorname{ccl}(\sigma)| \cdot |C_{S_n}(\sigma)| = n!$ is orbit-stabiliser for conjugation; it converts the computed centraliser order into the desired class size.

---

# Hints

<details>
<summary>Hint 1</summary>

Counting the conjugacy class directly is awkward. By the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]], the class size is $|S_n|/|C_{S_n}(\sigma)|$, so it suffices to count the centraliser — the permutations $\tau$ with $\tau\sigma\tau^{-1} = \sigma$. The centraliser is the more structured object; compute it instead.

</details>

<details>
<summary>Hint 2</summary>

Use the relabelling rule: $\tau\sigma\tau^{-1}$ is the permutation obtained from $\sigma$'s cycle notation by replacing each entry $x$ with $\tau(x)$. So $\tau$ centralises $\sigma$ exactly when this relabelling reproduces the *same* permutation $\sigma$. Ask: in how many ways can you relabel the cycle notation of $\sigma$ and end up writing down the same permutation?

</details>

<details>
<summary>Hint 3</summary>

A relabelling reproduces $\sigma$ in two independent ways. (i) It may send each cycle of $\sigma$ to a cycle of $\sigma$ *of the same length* — the $a_k$ cycles of length $k$ may be permuted among themselves in $a_k!$ ways. (ii) Within a single $k$-cycle, the relabelling may start at any of the $k$ entries — a $k$-cycle has $k$ equivalent rotations. Multiply: $a_k!$ for shuffling the length-$k$ cycles, and $k$ for each of the $a_k$ such cycles. Over all $k$ this gives $|C_{S_n}(\sigma)| = \prod_k k^{a_k} a_k!$.

</details>

---

# Solution

The strategy is to count the centraliser $C_{S_n}(\sigma)$ — the permutations that "relabel $\sigma$ back to itself" — and then divide $n!$ by it using orbit-stabiliser.

**Step 1: A permutation $\tau$ centralises $\sigma$ if and only if relabelling $\sigma$'s cycle notation by $\tau$ reproduces $\sigma$.**

By the relabelling rule for conjugation, $\tau\sigma\tau^{-1} = \sigma$ holds exactly when applying $\tau$ to every entry of $\sigma$'s disjoint-cycle notation yields a cycle notation for the same $\sigma$.

<details>
<summary>Derivation</summary>

By [[Thm - Conjugacy Classes of the Symmetric Group|the conjugation rule]], if $\sigma$ has the disjoint cycles $C_1, C_2, \dots$ with $C_i = (x_1^{(i)}\, x_2^{(i)}\, \cdots)$, then
$$\tau\sigma\tau^{-1} \text{ has disjoint cycles } \tau(C_1), \tau(C_2), \dots, \quad \text{where } \tau(C_i) = \big(\tau(x_1^{(i)})\ \tau(x_2^{(i)})\ \cdots\big).$$
That is, $\tau\sigma\tau^{-1}$ is read off by replacing each entry $x$ in $\sigma$'s cycle notation by $\tau(x)$.

Therefore $\tau \in C_{S_n}(\sigma)$, meaning $\tau\sigma\tau^{-1} = \sigma$, holds precisely when the relabelled collection of cycles $\{\tau(C_1), \tau(C_2), \dots\}$ is, as a set of disjoint cycles, the *same permutation* as $\sigma$. Counting the centraliser is thus counting the bijections $\tau$ of $\{1,\dots,n\}$ for which this relabelling regenerates $\sigma$.

</details>

**Step 2: Such a $\tau$ has exactly two independent freedoms — permuting equal-length cycles, and rotating within each cycle.**

For the relabelling to reproduce $\sigma$, $\tau$ must carry each cycle of $\sigma$ onto a cycle of $\sigma$ of the *same length*; cycles of the same length may be interchanged freely, and within a cycle the relabelling may begin at any entry.

<details>
<summary>Derivation</summary>

Suppose $\tau$ centralises $\sigma$, so $\{\tau(C_1), \tau(C_2), \dots\} = \{C_1, C_2, \dots\}$ as sets of cycles. Each $\tau(C_i)$ is itself a cycle, of the *same length* as $C_i$ (relabelling does not change a cycle's length). So $\tau$ permutes the cycles of $\sigma$ among themselves, and this permutation can only mix cycles of equal length — a $k$-cycle must go to a $k$-cycle.

This gives the **first freedom**. For each length $k$, the $a_k$ cycles of length $k$ are sent by $\tau$ to the $a_k$ cycles of length $k$ in some order: there are $a_k!$ such orderings, and the choices for different lengths $k$ are independent of each other.

Now fix which cycle goes to which. If $\tau$ must send the cycle $C = (x_1\, x_2\, \cdots\, x_k)$ onto the cycle $C' = (y_1\, y_2\, \cdots\, y_k)$, what can $\tau$ do on the points of $C$? The relabelling $\tau(C) = (\tau(x_1)\, \tau(x_2)\, \cdots\, \tau(x_k))$ must equal $C'$ *as a cyclic sequence*. But a $k$-cycle written $(y_1\, y_2\, \cdots\, y_k)$ has $k$ equally valid starting points — it is the same cycle as $(y_2\, \cdots\, y_k\, y_1)$, and so on. So $\tau(x_1)$ may be any one of $y_1, \dots, y_k$, and once $\tau(x_1)$ is chosen the rest is forced: $\tau(x_2)$ is the next entry, $\tau(x_3)$ the one after, since $\tau$ must respect the cyclic order. This gives exactly $k$ choices for how $\tau$ acts on the $k$ points of $C$.

This is the **second freedom**: for each individual cycle of length $k$, there are $k$ ways to fix the internal alignment of the relabelling, and the choices for different cycles are independent.

Crucially these two freedoms are *independent* and *exhaust all of $\tau$*. The first decides the cycle-to-cycle assignment; the second decides, for each assigned pair, the rotational alignment; and together they determine $\tau$ on every one of the $n$ points (every point lies in exactly one cycle of $\sigma$, since the cycles are disjoint and cover $\{1,\dots,n\}$). Conversely, *any* choice of a cycle-permutation respecting lengths together with a rotation for each cycle defines a bona fide $\tau \in S_n$ that centralises $\sigma$. So the centraliser is in bijection with (cycle-shuffles) $\times$ (per-cycle rotations).

</details>

**Step 3: Counting the two freedoms gives $|C_{S_n}(\sigma)| = \prod_k k^{a_k} a_k!$.**

Multiplying the $a_k!$ ways to shuffle the length-$k$ cycles by the $k$ rotations available to each of those $a_k$ cycles, and taking the product over all lengths $k$, gives $|C_{S_n}(\sigma)| = \prod_{k=1}^n k^{a_k}\, a_k!$.

<details>
<summary>Derivation</summary>

By Step 2 a centralising $\tau$ is determined by two independent collections of choices, so $|C_{S_n}(\sigma)|$ is the product of the number of choices.

*Shuffling cycles of equal length.* For each length $k$ there are $a_k!$ ways to permute the $a_k$ cycles of length $k$ among themselves; over all lengths this contributes
$$\prod_{k=1}^{n} a_k!.$$

*Rotating within each cycle.* Each cycle of length $k$ admits $k$ internal rotational alignments. There are $a_k$ cycles of length $k$, each contributing a factor $k$ independently, so the length-$k$ cycles together contribute $k^{a_k}$; over all lengths this contributes
$$\prod_{k=1}^{n} k^{a_k}.$$

Since the two collections of choices are independent, the centraliser order is their product:
$$|C_{S_n}(\sigma)| = \Big(\prod_{k=1}^{n} a_k!\Big)\Big(\prod_{k=1}^{n} k^{a_k}\Big) = \prod_{k=1}^{n} k^{a_k}\, a_k!.$$

(As a sanity check, the factors for $k$ with $a_k = 0$ are $k^0\,0! = 1$ and contribute nothing, so the product effectively runs only over the cycle lengths actually present. Fixed points, $k = 1$, contribute $1^{a_1} a_1! = a_1!$ — the freedom to permute the $a_1$ fixed points among themselves, and no rotation since a $1$-cycle has only one alignment.)

</details>

**Step 4: Orbit-stabiliser converts this into the class size.**

The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] gives $|\operatorname{ccl}_{S_n}(\sigma)| = |S_n|/|C_{S_n}(\sigma)| = n!/\prod_k k^{a_k} a_k!$.

<details>
<summary>Derivation</summary>

The conjugacy class $\operatorname{ccl}_{S_n}(\sigma)$ is the orbit of $\sigma$ under the conjugation action of $S_n$ on itself, and the centraliser $C_{S_n}(\sigma)$ is the stabiliser of $\sigma$. The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] gives
$$|\operatorname{ccl}_{S_n}(\sigma)| \cdot |C_{S_n}(\sigma)| = |S_n| = n!.$$
Substituting $|C_{S_n}(\sigma)| = \prod_{k} k^{a_k} a_k!$ from Step 3,
$$|\operatorname{ccl}_{S_n}(\sigma)| = \frac{n!}{\displaystyle\prod_{k=1}^{n} k^{a_k}\, a_k!}. \qquad \blacksquare$$

</details>

<details>
<summary><strong>Complete formal solution</strong></summary>

Let $\sigma \in S_n$ have cycle type $(a_1, \dots, a_n)$, so $\sigma$ has $a_k$ disjoint cycles of length $k$ and $\sum_k k a_k = n$.

By [[Thm - Conjugacy Classes of the Symmetric Group|the conjugation rule]], for any $\tau \in S_n$ the permutation $\tau\sigma\tau^{-1}$ is obtained from the disjoint-cycle notation of $\sigma$ by replacing each entry $x$ with $\tau(x)$; in particular each cycle $(x_1\,\cdots\,x_k)$ of $\sigma$ becomes the cycle $(\tau(x_1)\,\cdots\,\tau(x_k))$. Hence $\tau \in C_{S_n}(\sigma)$ — that is, $\tau\sigma\tau^{-1} = \sigma$ — if and only if relabelling the cycles of $\sigma$ by $\tau$ regenerates $\sigma$.

Such a $\tau$ must send each cycle of $\sigma$ to a cycle of $\sigma$ of the same length, and is determined by two independent collections of choices:

1. *A length-preserving permutation of the cycles.* For each $k$, the $a_k$ cycles of length $k$ are permuted among themselves: $a_k!$ choices, independent across $k$, contributing $\prod_k a_k!$.

2. *A rotational alignment within each cycle.* Once $\tau$ is required to map a particular $k$-cycle onto a particular $k$-cycle, the image of the first entry may be any of the $k$ entries of the target (a $k$-cycle has $k$ equivalent starting points), after which $\tau$ is forced on the remaining $k-1$ points by cyclic order: $k$ choices per cycle. Over the $a_k$ cycles of length $k$ this contributes $k^{a_k}$, hence $\prod_k k^{a_k}$ overall.

These choices are independent and jointly determine $\tau$ on all $n$ points, and every such choice yields a valid centralising $\tau$. Therefore
$$|C_{S_n}(\sigma)| = \prod_{k=1}^{n} k^{a_k}\, a_k!.$$

The conjugacy class is the orbit and the centraliser the stabiliser of $\sigma$ under conjugation, so by the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]],
$$|\operatorname{ccl}_{S_n}(\sigma)| = \frac{|S_n|}{|C_{S_n}(\sigma)|} = \frac{n!}{\displaystyle\prod_{k=1}^{n} k^{a_k}\, a_k!}. \qquad \blacksquare$$

</details>

---

# Key Takeaways

**Count a conjugacy class by counting its centraliser — the harder-looking object is the structured one.** The class-size formula is genuinely hard to derive by trying to enumerate conjugates directly, but the centraliser yields to a clean combinatorial description. This inversion — count the stabiliser, then divide $|G|$ by it via the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] — is the standard strategy for *any* orbit-counting problem, not just conjugacy. The general principle: when an orbit is hard to count, count its stabiliser; when a stabiliser is hard to count, count its orbit; orbit-stabiliser lets you always work with whichever of the two is more structured. Here the centraliser is more structured because "permutations that relabel $\sigma$ back to itself" is a concrete description with visible degrees of freedom, whereas "all permutations of a given cycle type" resists a direct count. Recognising in advance which side of $|\operatorname{orbit}| \cdot |\operatorname{stab}| = |G|$ is the tractable one is the strategic skill.

**A centraliser in $S_n$ is a wreath-product bookkeeping: shuffle equal cycles, rotate within each.** The structural lesson behind the formula $\prod_k k^{a_k} a_k!$ is that a permutation commuting with $\sigma$ does exactly two things, and they multiply independently: it permutes the $\sigma$-cycles of each length among themselves (the $a_k!$ factors), and it rotates the labelling inside each individual cycle (the $k^{a_k}$ factors). This decomposition is the defining anatomy of a *wreath product* — the centraliser of an element of cycle type $1^{a_1}2^{a_2}\cdots$ is precisely $\prod_k (C_k \wr S_{a_k})$, the cyclic group $C_k$ supplying the within-cycle rotations and the symmetric group $S_{a_k}$ supplying the cross-cycle shuffles. Even without naming the wreath product, the takeaway is the habit of decomposing a symmetry count into independent "internal" and "external" freedoms and multiplying — the same pattern counts automorphisms of graphs built from repeated identical pieces, symmetries of molecules with equivalent substituents, and orbits in Pólya enumeration. The trigger is any object made of interchangeable repeated parts: count the rearrangements of the parts and the symmetries within each part separately.

**The single-cycle and $(2,2)$ cases are this formula collapsed — and worth checking to calibrate it.** Special cases are the fastest way to confirm a general formula is right and to remember it. For a single $n$-cycle the cycle type is $a_n = 1$ with all other $a_k = 0$, so $\prod_k k^{a_k} a_k! = n^1 \cdot 1! = n$, recovering $|C_{S_n}(\sigma)| = n$ and class size $n!/n = (n-1)!$ — the centraliser of an $n$-cycle is just its own $n$ powers. For cycle type $(2,2)$ in $S_4$, $a_2 = 2$ and the rest vanish, so $\prod_k k^{a_k} a_k! = 2^2 \cdot 2! = 8$, giving class size $24/8 = 3$ — the three ways to split four points into two pairs. The discipline of substituting a small or extreme cycle type into a general formula and watching it reproduce a count you can verify by hand is the cheapest available error-check, and it is exactly how to re-derive the formula from memory under spaced practice: reconstruct the two freedoms, test them on the $n$-cycle, and the general product writes itself.

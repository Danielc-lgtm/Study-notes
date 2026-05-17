---
type: theorem
subject: group-theory
prereqs:
  - "Def - Symmetric Group"
  - "Def - Conjugacy Class"
  - "Def - Centraliser and Centre"
  - "Def - Group Action"
  - "Thm - The Class Equation"
tags: [algebra, group-theory]
---

# Notation

$S_n$ is the [[Def - Symmetric Group|symmetric group]] on $\{1, 2, \dots, n\}$, the group of all bijections of that set under composition; it has order $n!$. A permutation $\sigma \in S_n$ is written in **disjoint cycle notation**: $(a_1\,a_2\,\cdots\,a_r)$ denotes the cycle sending $a_1 \mapsto a_2 \mapsto \cdots \mapsto a_r \mapsto a_1$, and a permutation factors uniquely (up to order) into disjoint cycles. The **cycle type** of $\sigma$ is the list of lengths of those disjoint cycles, fixed points counted as $1$-cycles; it is a [[Def - Conjugacy Class|partition]] of $n$. We write a cycle type as $1^{a_1} 2^{a_2} \cdots n^{a_n}$, meaning $a_k$ cycles of length $k$, so $\sum_k k\, a_k = n$. The [[Def - Conjugacy Class|conjugacy class]] of $\sigma$ is $\operatorname{ccl}_{S_n}(\sigma) = \{\tau \sigma \tau^{-1} : \tau \in S_n\}$, and $C_{S_n}(\sigma)$ is its [[Def - Centraliser and Centre|centraliser]]. The full notation registry lives on the parent page [[Group Theory II — §1.3–1.4]].

---

# Statement

> **Conjugacy classes of $S_n$.** Two permutations $\sigma, \sigma' \in S_n$ are conjugate in $S_n$ if and only if they have the same **cycle type**. Consequently the conjugacy classes of $S_n$ are in bijection with the partitions of $n$: one class for each partition.

The proof rests on an explicit formula for how conjugation acts.

> **Relabelling formula.** If $\sigma$ has disjoint cycle decomposition $\sigma = (a_1\,a_2\,\cdots)(b_1\,b_2\,\cdots)\cdots$ and $\tau \in S_n$, then
> $$\tau \sigma \tau^{-1} = \bigl(\tau(a_1)\ \tau(a_2)\ \cdots\bigr)\bigl(\tau(b_1)\ \tau(b_2)\ \cdots\bigr)\cdots,$$
> the same cycle structure with every entry relabelled by $\tau$.

> **Class size.** The conjugacy class of cycle type $1^{a_1} 2^{a_2} \cdots n^{a_n}$ has size
> $$\bigl|\operatorname{ccl}_{S_n}(\sigma)\bigr| = \frac{n!}{\prod_{k=1}^{n} k^{a_k}\, a_k!}.$$

---

# Motivation

[[Def - Conjugacy Class|Conjugacy]] is the right notion of "two elements are structurally the same", but for a general group it is invisible: deciding whether $x$ and $y$ are conjugate means searching all of $G$ for some $g$ with $gxg^{-1} = y$, an existence question with no shortcut. Conjugacy classes are defined, not computed. The [[Thm - The Class Equation|class equation]] can be written down only once you already know the classes, and for most groups that knowledge is hard-won.

The symmetric group is the great exception, and this theorem says exactly why. In $S_n$ conjugacy stops being an existence problem and becomes a *visible combinatorial invariant*: two permutations are conjugate if and only if they look the same when you ignore the names of the points — same number of $2$-cycles, same number of $3$-cycles, and so on. The cycle type, a partition of $n$, is a complete invariant of conjugacy. Nothing else about a permutation matters; conjugate or not is decided by counting.

This is worth pausing on because it is unusual. For a generic finite group there is no easily computed complete invariant of conjugacy at all — finding the classes is part of understanding the group. For $S_n$ the classes are *handed to you* by elementary combinatorics: they are the partitions of $n$, a list anyone can write down. The symmetric group is therefore the one infinite family whose entire conjugacy structure — the classes, their number, their sizes — is completely transparent and computable by hand.

The payoff is concrete and immediate. Because we can list the classes and compute their sizes from the formula $n!/\prod_k k^{a_k}a_k!$, the class equation of $S_n$ becomes a genuine numerical object. This is the combinatorial input to the hardest result of the topic: the [[Thm - Simplicity of the Alternating Group|simplicity of Aₙ]] is proved by tracking which cycle types lie in a putative normal subgroup, and the brute-force verification that $A_5$ is simple is nothing but reading the $S_5$ class sizes, restricting to $A_5$, and checking that no sub-collection forms a normal subgroup. Cycle type is what makes that argument possible.

---

# Sources and Targets

This section is not an input/output summary. It records the non-obvious circumstances in which a problem reduces to cycle-type bookkeeping (sources), and the non-obvious conclusions that follow once you know the conjugacy classes of $S_n$ (targets).

**Sources (Input Broadening)**

The theorem applies whenever the ambient group is a symmetric group, so the question is recognising that a problem *lives* in $S_n$ even when it does not say so.

The basic source is **a concrete permutation problem** — anything about shuffles, rearrangements, or orderings. Property $B$ is "the objects are bijections of a finite set", and the bridge is that such bijections *are* the elements of a symmetric group; conjugating one by another is relabelling. This is non-obvious only because permutations are often presented as functions or as one-line arrays, not as elements of $S_n$. Once the symmetric-group framing is in place, "are these two shuffles the same up to renaming the cards" becomes "do they have the same cycle type".

A second source is **a group given as a permutation group**, i.e. realised inside some $S_n$ by a [[Def - Group Action|group action]] — by [[Thm - Cayley's Theorem|Cayley's theorem]] every finite group can be so realised. Property $B$ is "$G$ acts faithfully on a set $X$ of size $n$". The bridge is that $G$ embeds in $S_n$ and conjugacy *within $G$* refines conjugacy within $S_n$: elements conjugate in $G$ certainly have the same cycle type as permutations of $X$. So cycle type is a necessary condition for conjugacy in *any* permutation group, computable from the action alone. This is non-obvious because the abstract group $G$ may give no hint of cycle structure until you fix the action.

A third source is **a structural question about $A_n$**, the [[Def - Symmetric Group|alternating group]]. Property $B$ is "the problem concerns even permutations". The bridge is that $A_n \leq S_n$, so every element of $A_n$ has an $S_n$-cycle type — and the cycle type determines parity, since a $k$-cycle is even exactly when $k$ is odd. Whether an element lies in $A_n$, and how its $S_n$-class meets $A_n$, is read off the cycle type. This is the source feeding the [[Thm - Simplicity of the Alternating Group|simplicity proof for Aₙ]].

A fourth source is **a problem supplying an order, or a count of elements of a given order**. Property $B$ is information about $\operatorname{ord}(\sigma)$ for permutations $\sigma$. The bridge is that the order of a permutation is the *least common multiple of its cycle lengths*, a function of cycle type alone. So "how many elements of $S_n$ have order $6$" becomes "which partitions of $n$ have lcm of parts equal to $6$", and the count of each is the class-size formula. This is non-obvious because element order is an algebraic quantity, yet here it is fully combinatorial.

**Targets (Output Amplification)**

The theorem delivers: the classes of $S_n$ are the partitions of $n$, with explicit sizes. Combined with one further property $D$, this becomes a sharper conclusion.

The most useful combination is **cycle type plus the class-size formula gives centraliser orders for free**. The theorem says $|\operatorname{ccl}_{S_n}(\sigma)| = n!/\prod_k k^{a_k}a_k!$. Add property $D$ — the [[Thm - The Class Equation|proposition]] $|\operatorname{ccl}_{S_n}(\sigma)| = |S_n : C_{S_n}(\sigma)|$. Dividing $n!$ by the class size, the result $E$ is $|C_{S_n}(\sigma)| = \prod_k k^{a_k}a_k!$: the centraliser of a permutation has order exactly the product over cycle lengths. This is non-obvious because the centraliser — elements commuting with $\sigma$ — looks like an algebraic object requiring you to solve $\tau\sigma = \sigma\tau$, yet its *order* is pure cycle-type combinatorics. (One even sees the structure: $C_{S_n}(\sigma)$ is generated by cyclically rotating each cycle and permuting equal-length cycles among themselves, a wreath product $\prod_k (C_k \wr S_{a_k})$.)

A second combination is **cycle type plus restriction to $A_n$ tells you when an $S_n$-class splits**. Property $D$ is "$\sigma$ is even, so $\operatorname{ccl}_{S_n}(\sigma) \subseteq A_n$". The $S_n$-class of $\sigma$ either stays one class in $A_n$ or breaks into two equal halves. The result $E$: it splits exactly when no *odd* permutation commutes with $\sigma$, i.e. when the cycle type has only odd parts, all distinct. This is the non-obvious mechanism behind the five conjugacy classes of $A_5$ — the $5$-cycles, all of cycle type $5$ (odd, distinct), split into two classes of size $12$. The split is invisible from $S_n$ alone and is decisive in the simplicity argument.

A third combination is **the partition correspondence plus a generating-function viewpoint counts permutations by structure**. Property $D$ is any weighting of partitions — by number of parts, by largest part, by parity. Because classes are partitions, summing the class-size formula against such a weight, the result $E$ is an exact count of permutations with a prescribed structural feature; the relevant generating function is $\prod_k \exp(x^k/k)$, the exponential formula. This is non-obvious because it turns an enumeration over the group $S_n$ into an enumeration over the combinatorial set of partitions of $n$.

---

# Why Is It True

The whole theorem follows from a single picture: **conjugation in $S_n$ is renaming the points.**

Think of a permutation $\sigma$ as a piece of machinery — a set of wheels. Each disjoint cycle is one wheel: a cycle $(a_1\,a_2\,\cdots\,a_r)$ is an $r$-toothed wheel whose teeth are labelled $a_1, \dots, a_r$ and which, when turned, advances each tooth to the next. The permutation $\sigma$ *is* this collection of wheels, and its cycle type is the unlabelled blueprint: how many wheels of each size.

Now ask what $\tau\sigma\tau^{-1}$ does to a point. Conjugation is a three-step sandwich. To compute $\tau\sigma\tau^{-1}$ on the point $\tau(a)$: first $\tau^{-1}$ sends $\tau(a)$ back to $a$; then $\sigma$ advances $a$ along its wheel to $\sigma(a)$; then $\tau$ sends $\sigma(a)$ forward to $\tau(\sigma(a))$. The net effect is $\tau(a) \mapsto \tau(\sigma(a))$. In words: $\tau\sigma\tau^{-1}$ does to the *renamed* point $\tau(a)$ exactly what $\sigma$ did to $a$. Conjugating by $\tau$ has not changed the machinery at all — it has only relabelled every tooth, $a \rightsquigarrow \tau(a)$. The wheels are identical; only the names painted on them differ.

This makes both directions of the theorem transparent.

If $\sigma$ and $\sigma'$ are conjugate, $\sigma' = \tau\sigma\tau^{-1}$, then $\sigma'$ is $\sigma$ with relabelled teeth — same wheels, same blueprint, *same cycle type*. Relabelling cannot turn a $3$-wheel into a $2$-wheel.

Conversely, if $\sigma$ and $\sigma'$ have the same cycle type, they have the same blueprint: the same number of wheels of each size. Then you can match up their wheels, and matching wheels means writing down a dictionary $\tau$ that renames the teeth of $\sigma$ into the teeth of $\sigma'$. Because $\sigma$ and $\sigma'$ each touch all $n$ points (counting fixed points as $1$-wheels), this dictionary is a bijection of $\{1, \dots, n\}$, hence an element of $S_n$ — and by the relabelling picture $\tau\sigma\tau^{-1} = \sigma'$. Same blueprint, therefore conjugate.

So conjugacy in $S_n$ is sameness of blueprint, and blueprints are exactly partitions of $n$ — one wheel-count for each way of writing $n$ as a sum. That is the bijection between classes and partitions.

The size formula is the same picture, counted. Fix a cycle type. Lay out an empty template of wheels — slots for the teeth — and pour the numbers $1, \dots, n$ into the $n$ slots: $n!$ ways. Two pourings give the *same* permutation when they differ by a symmetry of the template, and the template has exactly two kinds of symmetry. First, each wheel of length $k$ can be rotated to any of $k$ starting positions without changing the cycle — that is a factor $k$ for each of the $a_k$ wheels of length $k$, so $k^{a_k}$ in all. Second, the $a_k$ wheels that have the *same* length $k$ are interchangeable — relabelling which wheel is "first" does not change the permutation — contributing $a_k!$. Dividing the $n!$ pourings by the total symmetry $\prod_k k^{a_k}a_k!$ counts each permutation of that cycle type exactly once, giving $|\operatorname{ccl}_{S_n}(\sigma)| = n!/\prod_k k^{a_k}a_k!$.

---

# What Makes This Hard

The forward direction (conjugate $\implies$ same cycle type) is the easy half — it is just the relabelling formula. The genuine step is the *converse*: given two permutations of the same cycle type, one must explicitly *construct* the conjugating $\tau$ by lining up the cycles, and the subtle point is that $\tau$ must be a well-defined bijection of *all* of $\{1, \dots, n\}$ — which is why fixed points must be included as $1$-cycles, so that the two permutations cover the same point set and the matching is total. In the size formula the common error is to divide by only one of the two symmetries: people remember to divide by $\prod_k k^{a_k}$ for cyclic rotation within each cycle but forget the $\prod_k a_k!$ for permuting equal-length cycles among themselves (or vice versa).

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire result.

**High-level strategy:**
Establish the relabelling formula $\tau\sigma\tau^{-1} = (\tau(a_1)\,\tau(a_2)\,\cdots)\cdots$ by a direct three-step computation. This instantly gives "conjugate $\implies$ same cycle type". For the converse, line up the cycles of two equal-type permutations and read off a $\tau$ from the line-up. The class size then comes from counting labelled fillings of a fixed cycle-type template and dividing by the template's symmetries.

**Subgoal decomposition:**

1. **Relabelling formula.** Show that if $\sigma$ contains the cycle $(a_1\,\cdots\,a_r)$ then $\tau\sigma\tau^{-1}$ contains the cycle $(\tau(a_1)\,\cdots\,\tau(a_r))$.
   - *Hint:* Compute $(\tau\sigma\tau^{-1})(\tau(a)) = \tau(\sigma(a))$ — apply $\tau^{-1}$, then $\sigma$, then $\tau$.
   - *Why needed:* It is the engine of the whole theorem; it shows conjugation only renames points.

2. **Conjugate $\implies$ same cycle type.** Conclude that $\tau\sigma\tau^{-1}$ has the identical list of cycle lengths as $\sigma$.
   - *Hint:* Relabelling sends each $r$-cycle to an $r$-cycle bijectively; lengths are untouched.
   - *Why needed:* The forward direction of the biconditional.

3. **Same cycle type $\implies$ conjugate.** Given $\sigma, \sigma'$ of the same cycle type, write both in disjoint cycle notation including $1$-cycles, align cycles of equal length, and define $\tau$ to map each entry of $\sigma$ to the entry in the corresponding position of $\sigma'$.
   - *Hint:* Because all $n$ points appear (fixed points as $1$-cycles), $\tau$ is a bijection of $\{1,\dots,n\}$; by step 1, $\tau\sigma\tau^{-1} = \sigma'$.
   - *Why needed:* The converse direction; it completes the biconditional and the bijection with partitions.

4. **Class size.** Count permutations of a fixed cycle type $1^{a_1}\cdots n^{a_n}$: fill the cycle template with $1, \dots, n$ in $n!$ ways, then divide by the over-counting.
   - *Hint:* Each $k$-cycle is counted $k$ times (rotations); the $a_k$ equal-length $k$-cycles are counted $a_k!$ times (reorderings). Divide by $\prod_k k^{a_k}a_k!$.
   - *Why needed:* It yields the size formula and, via the class-equation proposition, the centraliser order.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

> [!note]- Lemma 1: The relabelling formula for conjugation
> **Statement:** For $\sigma, \tau \in S_n$ and any cycle $(a_1\,a_2\,\cdots\,a_r)$ appearing in the disjoint cycle decomposition of $\sigma$, the conjugate $\tau\sigma\tau^{-1}$ contains the cycle $(\tau(a_1)\,\tau(a_2)\,\cdots\,\tau(a_r))$. Hence $\tau\sigma\tau^{-1}$ is obtained from $\sigma$ by applying $\tau$ to every entry.
>
> **Hint:** Evaluate $\tau\sigma\tau^{-1}$ on the point $\tau(a)$ by composing right to left.
>
> **Why needed:** It is the single computation from which both directions of the theorem and the geometric picture follow.
>
> > [!note]- Full proof
> > Take any point of the form $\tau(a)$ with $a \in \{1, \dots, n\}$ — every point is of this form, since $\tau$ is a bijection. Compute, applying maps right to left:
> > $$(\tau \sigma \tau^{-1})\bigl(\tau(a)\bigr) = \tau\Bigl(\sigma\bigl(\tau^{-1}(\tau(a))\bigr)\Bigr) = \tau\bigl(\sigma(a)\bigr).$$
> > So $\tau\sigma\tau^{-1}$ sends $\tau(a)$ to $\tau(\sigma(a))$. If $\sigma$ has the cycle $(a_1\,a_2\,\cdots\,a_r)$, meaning $\sigma(a_i) = a_{i+1}$ (indices mod $r$), then $\tau\sigma\tau^{-1}$ sends $\tau(a_i) \mapsto \tau(a_{i+1})$, which is precisely the cycle $(\tau(a_1)\,\tau(a_2)\,\cdots\,\tau(a_r))$. Applying this to every cycle of $\sigma$ shows $\tau\sigma\tau^{-1}$ is $\sigma$ with each entry relabelled by $\tau$.

> [!note]- Lemma 2: Conjugate permutations have equal cycle type
> **Statement:** If $\sigma' = \tau\sigma\tau^{-1}$ in $S_n$, then $\sigma$ and $\sigma'$ have the same cycle type.
>
> **Hint:** Use Lemma 1: relabelling sends each $r$-cycle to an $r$-cycle.
>
> **Why needed:** It is the forward implication of the biconditional.
>
> > [!note]- Full proof
> > By Lemma 1, $\sigma' = \tau\sigma\tau^{-1}$ is obtained by replacing each cycle $(a_1\,\cdots\,a_r)$ of $\sigma$ with $(\tau(a_1)\,\cdots\,\tau(a_r))$. Since $\tau$ is a bijection, distinct cycles of $\sigma$ (which are supported on disjoint point sets) map to cycles of $\sigma'$ supported on disjoint point sets, and an $r$-cycle becomes an $r$-cycle. So $\sigma$ and $\sigma'$ have exactly the same multiset of cycle lengths — the same cycle type.

> [!note]- Lemma 3: Equal cycle type implies conjugacy
> **Statement:** If $\sigma, \sigma' \in S_n$ have the same cycle type, there exists $\tau \in S_n$ with $\tau\sigma\tau^{-1} = \sigma'$.
>
> **Hint:** Write both permutations in full disjoint cycle notation, *including $1$-cycles for fixed points*, with cycles of each length aligned; define $\tau$ position by position.
>
> **Why needed:** It is the converse implication, completing the biconditional and the bijection between classes and partitions.
>
> > [!note]- Full proof
> > Write $\sigma$ and $\sigma'$ in disjoint cycle notation, including a $1$-cycle for every fixed point, so that each notation uses all $n$ symbols exactly once. Because $\sigma$ and $\sigma'$ have the same cycle type, their cycles can be paired off: each $k$-cycle of $\sigma$ with a $k$-cycle of $\sigma'$, every cycle paired. Write the paired cycles one above the other, aligning their entries position by position; this is possible because paired cycles have equal length.
> >
> > Define $\tau : \{1,\dots,n\} \to \{1,\dots,n\}$ by sending each entry of $\sigma$ to the entry directly below it in $\sigma'$. Since every symbol appears exactly once in the layout of $\sigma$ and exactly once in that of $\sigma'$, $\tau$ is a well-defined bijection, hence $\tau \in S_n$.
> >
> > By construction $\tau$ carries each cycle $(a_1\,\cdots\,a_r)$ of $\sigma$ entry-wise to the paired cycle of $\sigma'$. By Lemma 1, $\tau\sigma\tau^{-1}$ is $\sigma$ with each entry relabelled by $\tau$ — which is exactly $\sigma'$. Hence $\tau\sigma\tau^{-1} = \sigma'$.

> [!note]- Lemma 4: The class-size formula
> **Statement:** The conjugacy class of cycle type $1^{a_1} 2^{a_2} \cdots n^{a_n}$ (where $\sum_k k\,a_k = n$) has size $\dfrac{n!}{\prod_{k=1}^n k^{a_k}\, a_k!}$.
>
> **Hint:** Count ordered fillings of a fixed cycle template, then quotient by rotations within cycles and by permutations of equal-length cycles.
>
> **Why needed:** It makes the class equation of $S_n$ explicit and, by the proposition $|\operatorname{ccl}| = |S_n : C_{S_n}(\sigma)|$, yields $|C_{S_n}(\sigma)| = \prod_k k^{a_k}a_k!$.
>
> > [!note]- Full proof
> > Fix the cycle type: a template consisting of $a_k$ empty cycles of length $k$, for each $k$, with $\sum_k k\,a_k = n$ slots in total. Filling the $n$ slots with the symbols $1, 2, \dots, n$ in some order can be done in $n!$ ways, and every permutation of the given cycle type arises from at least one filling.
> >
> > Two fillings produce the *same* permutation precisely when they differ by a symmetry of the template:
> >
> > - **Rotation within a cycle.** A cycle $(a_1\,a_2\,\cdots\,a_k)$ is unchanged by cyclic rotation of its entries, so each $k$-cycle is written in $k$ equivalent ways. With $a_k$ cycles of length $k$, this contributes a factor $k^{a_k}$ of redundancy, and over all $k$ a factor $\prod_k k^{a_k}$.
> >
> > - **Permuting equal-length cycles.** The $a_k$ disjoint cycles of the same length $k$ may be listed in any order without changing the permutation, contributing a factor $a_k!$, and over all $k$ a factor $\prod_k a_k!$.
> >
> > These are all the redundancies: two fillings give the same permutation if and only if they are related by rotations and reorderings of this kind. Hence each permutation of the cycle type corresponds to exactly $\prod_k k^{a_k}a_k!$ fillings, and the number of distinct permutations is
> > $$\frac{n!}{\prod_{k=1}^n k^{a_k}\,a_k!}.$$

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Two permutations $\sigma, \sigma' \in S_n$ are conjugate if and only if they have the same cycle type; hence the conjugacy classes of $S_n$ correspond bijectively to the partitions of $n$.
>
> *Proof.*
>
> *Relabelling formula.* Let $\sigma, \tau \in S_n$. For any $a \in \{1, \dots, n\}$,
> $$(\tau\sigma\tau^{-1})\bigl(\tau(a)\bigr) = \tau\bigl(\sigma(\tau^{-1}\tau(a))\bigr) = \tau\bigl(\sigma(a)\bigr).$$
> Thus if $\sigma$ contains the cycle $(a_1\,a_2\,\cdots\,a_r)$ — that is, $\sigma(a_i) = a_{i+1}$ with indices modulo $r$ — then $\tau\sigma\tau^{-1}$ sends $\tau(a_i) \mapsto \tau(a_{i+1})$, so it contains the cycle $(\tau(a_1)\,\tau(a_2)\,\cdots\,\tau(a_r))$. Applying this to each disjoint cycle, $\tau\sigma\tau^{-1}$ is $\sigma$ with every entry relabelled by $\tau$.
>
> *($\Rightarrow$) Conjugate implies equal cycle type.* If $\sigma' = \tau\sigma\tau^{-1}$, the relabelling formula expresses $\sigma'$ as $\sigma$ with entries permuted by the bijection $\tau$. Disjoint cycles map to disjoint cycles and an $r$-cycle maps to an $r$-cycle, so $\sigma$ and $\sigma'$ have identical multisets of cycle lengths — the same cycle type.
>
> *($\Leftarrow$) Equal cycle type implies conjugate.* Suppose $\sigma$ and $\sigma'$ have the same cycle type. Write each in disjoint cycle notation, including a $1$-cycle for every fixed point, so that all $n$ symbols are used exactly once in each. Pair the cycles of $\sigma$ with the cycles of $\sigma'$ so that paired cycles have equal length — possible since the cycle types agree. Place each pair of cycles one above the other with entries aligned by position. Define $\tau$ to send each entry of $\sigma$ to the entry directly below it in $\sigma'$. Each of the $n$ symbols appears once in the layout of $\sigma$ and once in that of $\sigma'$, so $\tau$ is a bijection of $\{1, \dots, n\}$, hence $\tau \in S_n$. By construction $\tau$ carries each cycle of $\sigma$ entry-wise onto the paired cycle of $\sigma'$, so by the relabelling formula $\tau\sigma\tau^{-1} = \sigma'$.
>
> *Bijection with partitions.* By the two implications, the conjugacy class of $\sigma$ is determined by, and determines, its cycle type. A cycle type is a multiset of positive integers summing to $n$, i.e. a partition of $n$. Hence $\sigma \mapsto (\text{cycle type of } \sigma)$ induces a bijection between the conjugacy classes of $S_n$ and the partitions of $n$. $\qquad\blacksquare$
>
> **Class size.** The conjugacy class of cycle type $1^{a_1}\cdots n^{a_n}$ has size $n!/\prod_k k^{a_k}a_k!$.
>
> *Proof.* Fix a template of $a_k$ empty $k$-cycles for each $k$, with $\sum_k k\,a_k = n$ slots. Filling the slots with $1, \dots, n$ in order gives $n!$ fillings, and every permutation of the cycle type arises. Two fillings yield the same permutation if and only if they differ by (i) a cyclic rotation of the entries within some cycles — a $k$-cycle has $k$ rotations, giving redundancy $\prod_k k^{a_k}$ — or (ii) a reordering of the $a_k$ equal-length $k$-cycles among themselves — giving redundancy $\prod_k a_k!$. These exhaust the ways two fillings produce the same permutation, so each permutation corresponds to exactly $\prod_k k^{a_k}a_k!$ fillings, and the class has size $n!/\prod_k k^{a_k}a_k!$. $\qquad\blacksquare$
>
> **Worked example: the conjugacy classes of $S_5$.** The partitions of $5$ give seven classes. Applying the size formula:
>
> | Cycle type | Partition of $5$ | Representative | Class size $\dfrac{5!}{\prod_k k^{a_k}a_k!}$ |
> |---|---|---|---|
> | $1^5$ | $1+1+1+1+1$ | $e$ | $\dfrac{120}{1^5\cdot 5!} = 1$ |
> | $2 \cdot 1^3$ | $2+1+1+1$ | $(1\,2)$ | $\dfrac{120}{2^1\,1!\cdot 1^3\,3!} = 10$ |
> | $2^2 \cdot 1$ | $2+2+1$ | $(1\,2)(3\,4)$ | $\dfrac{120}{2^2\,2!\cdot 1^1\,1!} = 15$ |
> | $3 \cdot 1^2$ | $3+1+1$ | $(1\,2\,3)$ | $\dfrac{120}{3^1\,1!\cdot 1^2\,2!} = 20$ |
> | $3 \cdot 2$ | $3+2$ | $(1\,2\,3)(4\,5)$ | $\dfrac{120}{3^1\,1!\cdot 2^1\,1!} = 20$ |
> | $4 \cdot 1$ | $4+1$ | $(1\,2\,3\,4)$ | $\dfrac{120}{4^1\,1!\cdot 1^1\,1!} = 30$ |
> | $5$ | $5$ | $(1\,2\,3\,4\,5)$ | $\dfrac{120}{5^1\,1!} = 24$ |
>
> The seven class sizes are $1, 10, 15, 20, 20, 30, 24$, and they sum to $120 = |S_5| = 5!$, confirming the [[Thm - The Class Equation|class equation]] for $S_5$. The single size-$1$ class is the identity, so $Z(S_5) = \{e\}$.

---

# Cross-Field Exercise Suggestions

The aim is to find settings where cycle-type combinatorics is the right tool although the problem does not mention conjugacy.

**Combinatorics: counting permutations by order, and the lcm structure.** The order of a permutation is the least common multiple of its cycle lengths. A problem asking "how many elements of $S_7$ have order $12$" is, after this translation, "which partitions of $7$ have parts with $\operatorname{lcm} = 12$" — here $12 = 4 \cdot 3$, so the parts must include a $4$ and a $3$ — followed by the class-size formula for each such partition. The application is non-obvious because element order looks algebraic; cycle type makes it a partition-counting exercise. This also explains structural facts like "$S_n$ has an element of order $m$ if and only if $m$ is a sum-of-its-own-lcm-factors realisable within $n$".

**Linear algebra: the determinant and the sign homomorphism.** The Leibniz formula for the determinant sums $\operatorname{sgn}(\sigma)$ over all $\sigma \in S_n$. Since conjugate permutations have the same cycle type and the sign is a function of cycle type — a $k$-cycle has sign $(-1)^{k-1}$ — the sign is a *class function*, constant on conjugacy classes. Grouping the determinant's $n!$ terms by cycle type, and using the class-size formula, reorganises the sum by partition. The application is non-obvious because the determinant is presented analytically, with the symmetric group hidden inside the index set.

**Probability: random permutations and the Chinese restaurant process.** A uniformly random permutation of $\{1, \dots, n\}$ has a random cycle type, and the class-size formula is exactly the probability weight: $\Pr[\text{cycle type } 1^{a_1}\cdots n^{a_n}] = 1/\prod_k k^{a_k}a_k!$. This is the Ewens sampling formula at parameter $1$, and the expected number of $k$-cycles is $1/k$, so the expected total number of cycles is the harmonic number $H_n \approx \ln n$. The application is non-obvious because the question is phrased probabilistically; the bridge is that uniform-on-$S_n$ pushed forward to cycle type *is* the class-size distribution.

**Representation theory: the character table of $S_n$ is indexed by partitions on both sides.** The irreducible representations of $S_n$ are indexed by partitions of $n$ (via Young diagrams), and — by the general principle that the number of irreducibles equals the number of [[Def - Conjugacy Class|conjugacy classes]] — the conjugacy classes are *also* indexed by partitions of $n$, which is this theorem. So the character table of $S_n$ is a square matrix with rows and columns both labelled by partitions of $n$. The application is non-obvious because the two partition labellings have completely different origins (Young symmetrisers versus cycle type), yet this theorem is what guarantees the table is square.

---

# Bridges

- **[[Thm - The Class Equation|The Class Equation]]** — this theorem makes the class equation of $S_n$ fully explicit: the classes are the partitions of $n$, and the size formula gives every summand. The class equation $|S_n| = \sum |\operatorname{ccl}|$ becomes the identity that the cycle-type class sizes sum to $n!$. Conversely, the proposition $|\operatorname{ccl}_{S_n}(\sigma)| = |S_n : C_{S_n}(\sigma)|$ converts the size formula into the centraliser order $|C_{S_n}(\sigma)| = \prod_k k^{a_k}a_k!$.

- **[[Thm - Simplicity of the Alternating Group|Simplicity of the Alternating Group]]** — cycle type is the combinatorial backbone of the simplicity proof. The argument that a normal subgroup of $A_n$ containing one $3$-cycle contains them all uses that all $3$-cycles share the cycle type $3 \cdot 1^{n-3}$; the case analysis showing every non-trivial normal subgroup contains a $3$-cycle is organised entirely by the cycle type of a chosen element. And the brute-force check that $A_5$ is simple reads off the $S_5$ table above, restricted to even permutations.

- **[[Thm - Cayley's Theorem|Cayley's Theorem]]** — Cayley embeds an arbitrary finite group $G$ into a symmetric group $S_n$. This theorem then says the conjugacy classes of $G$, viewed inside $S_n$, are constrained by cycle type: conjugate elements of $G$ have equal cycle type as permutations. Cycle type is thus a computable invariant available for *any* finite group once an action is fixed, though it is generally coarser than $G$-conjugacy.

- **Partitions and the theory of $\lambda$-rings / symmetric functions** — the appearance of partitions of $n$ as the conjugacy classes of $S_n$ is the entry point to symmetric function theory: the irreducible characters of $S_n$ are the transition coefficients between the power-sum and Schur bases of the ring of symmetric functions, both indexed by partitions. The relabelling formula is, in that language, the statement that power sums are the natural basis adapted to cycle type.

---

# Unlocked by This

> [!tip] Young diagrams and the representation theory of $S_n$ *(from [[Group Theory III — §1.5–1.7|Representation Theory]])*
> Because the conjugacy classes of $S_n$ are the partitions of $n$, and the number of irreducible representations equals the number of conjugacy classes, the irreducible representations of $S_n$ are also indexed by partitions of $n$ — realised concretely by Young diagrams and Specht modules. This theorem is the conjugacy-side half of that double indexing.

> [!tip] The cycle index and Pólya enumeration *(from Enumerative Combinatorics)*
> Recording each conjugacy class of $S_n$ together with its size and cycle type assembles into the cycle index polynomial $Z(S_n) = \frac{1}{n!}\sum_\sigma \prod_k x_k^{a_k(\sigma)}$. Substituting into the cycle index counts colourings up to symmetry — the Pólya enumeration theorem — and the class-size formula is exactly what makes the cycle index computable.

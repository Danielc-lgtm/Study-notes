---
type: exercise
subject: group-theory
difficulty: "⭐"
prereqs:
  - "Def - Subgroup"
  - "Def - Coset"
  - "Def - Normal Subgroup"
  - "Def - Order of a Group and of an Element"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be a group and let $H \leq G$ be a subgroup of **index two**, that is, $|G : H| = 2$. Prove that $H$ is a normal subgroup of $G$, written $H \trianglelefteq G$.

**Recall:**

The objects in play are a subgroup, its cosets, and the notion of normality.

A [[Def - Subgroup|subgroup]] $H \leq G$ is a subset of $G$ that contains the identity $e$ and is itself a group under the operation of $G$ — closed under products and under inverses.

![[Def - Coset#The Definition]]

The **index** $|G : H|$ is the number of left cosets of $H$ in $G$. Saying $|G : H| = 2$ means there are exactly two left cosets. Since $H$ itself is always one of them (it is the coset $eH$), the other left coset is everything else: the set-theoretic complement $G \setminus H$. The same statement holds for right cosets $Hg = \{hg : h \in H\}$ — there are also exactly two of them, and one of them is $H$.

![[Def - Normal Subgroup#The Definition]]

The face of normality this problem uses is the **coset characterisation**: $H$ is normal in $G$ if and only if its left and right cosets coincide, that is, $gH = Hg$ for every $g \in G$. This is equivalent to the conjugation definition $g^{-1}Hg = H$, since multiplying $gH = Hg$ on the left by $g^{-1}$ gives $H = g^{-1}Hg$.

---

# Convergent Strategy

**Problem class.** This is a *prove a subgroup is normal* problem — the gateway task that decides whether the quotient $G/H$ can be formed at all. As the [[Group Theory I — §1.1–1.2#Problem-Solving Strategy|problem-solving strategy]] of the topic page urges, the first move on any normality question is to scan for a cheap structural reason rather than reaching immediately for a conjugation calculation. Index two is the cheapest reason there is.

**Assumption pattern.** The single hypothesis is numerical: $|G : H| = 2$. A hypothesis about the *index* is a hypothesis about *how many cosets there are*, and when that number is as small as two the cosets are pinned down completely. Two cosets, one of which is forced to be $H$, leaves the other with no freedom: it must be the complement $G \setminus H$. The assumption does its work by making the coset partition rigid.

**Theorem routing.** No named theorem is needed — the route runs directly through the coset characterisation of normality in [[Def - Normal Subgroup]]. The plan is to compute the two left cosets explicitly, compute the two right cosets explicitly, observe that both partitions are the identical pair of sets $\{H,\ G \setminus H\}$, and conclude $gH = Hg$ for every $g$.

**Key decision point.** The one idea that makes the proof work is to *split into the two cases $g \in H$ and $g \notin H$ and use complementation*. For $g \in H$ both cosets equal $H$ and there is nothing to prove. For $g \notin H$, the genuine step is the realisation that a coset is determined by being one of only two blocks of a partition: once you know $gH \neq H$, the coset $gH$ is forced to be the *whole rest of the group*, and the identical argument forces $Hg$ to be that same rest. Two sets that are each "everything except $H$" are equal. Recognising that "the complement of $H$" is a description with exactly one referent is the whole exercise.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory I — §1.1–1.2#Legal Operations|the topic page's Legal Operations]]:

1. **Use index $2$ to force normality** (operation 7). This is the operation the entire exercise is an instance of — indeed this exercise is the *justification* for that operation being legal. The trigger is the literal appearance of a subgroup of index two, and the move is to argue via the two-block coset partition rather than by conjugation.

2. **Partition a group into cosets of a subgroup** (operation 1). Applied twice: once with left cosets and once with right cosets. The content used is that the cosets are *disjoint and exhaustive* — they tile $G$ with no overlaps and no gaps — so that knowing one block lets you name the other by complementation.

3. **Conjugate to test or exploit normality** (operation 6), in its packaged form. The conjugation definition $g^{-1}Hg = H$ is what "normal" ultimately means, but here we reach it through the equivalent coset identity $gH = Hg$ rather than by conjugating a general element directly.

---

# Hints

> [!note]- Hint 1
> Do not start conjugating elements. The hypothesis is about the *index*, so it is about *how many cosets exist*. Write down what the complete list of left cosets of $H$ looks like when there are exactly two of them, and remember that $H$ is always one coset on the list.

> [!note]- Hint 2
> The two left cosets partition $G$ — they are disjoint and together cover everything. One of them is $H$. What set must the other one be? Now run the identical argument for *right* cosets. Compare the two lists.

> [!note]- Hint 3
> For $g \in H$ you have $gH = H = Hg$ directly. For $g \notin H$, the left coset $gH$ is not $H$, so it is the other left coset; the right coset $Hg$ is not $H$, so it is the other right coset. Both "other" cosets equal $G \setminus H$. Hence $gH = Hg$ for every $g$, which is exactly the coset characterisation of normality.

---

# Solution

The strategy is to show the left-coset partition and the right-coset partition of $G$ are the *same* pair of sets, so that $gH = Hg$ for every $g$ — the coset characterisation of normality.

**Step 1: The two left cosets are $H$ and $G \setminus H$.**

Because $|G : H| = 2$ there are exactly two left cosets, and one of them is $H$ itself. The cosets partition $G$, so the second left coset is exactly $G \setminus H$.

> [!note]- Derivation
> By definition the index $|G : H|$ is the number of distinct left cosets $gH$, so the hypothesis $|G : H| = 2$ says there are precisely two of them. One left coset is always $H$: taking the representative $g = e$ gives the coset $eH = \{e \cdot h : h \in H\} = H$.
>
> The left cosets of $H$ **partition** $G$ — this is a standard fact from [[Def - Coset]]: any two cosets are either identical or disjoint, and every element $g$ lies in *some* coset, namely $gH$ (since $g = ge \in gH$ as $e \in H$). So the two cosets are disjoint and their union is all of $G$. Calling the second coset $C$, disjointness gives $C \cap H = \emptyset$ and exhaustiveness gives $C \cup H = G$. Together these say $C$ consists of exactly those elements of $G$ not in $H$:
> $$C = G \setminus H.$$
> Hence the complete list of left cosets is $\{\,H,\ G \setminus H\,\}$.

**Step 2: The two right cosets are also $H$ and $G \setminus H$.**

The identical argument with right cosets in place of left cosets shows the two right cosets are $H$ and $G \setminus H$ — literally the same pair of subsets of $G$.

> [!note]- Derivation
> Lagrange's counting works identically for right cosets: the number of right cosets of $H$ equals the number of left cosets, so there are exactly two right cosets as well. (Even without quoting that fact, the map $gH \mapsto Hg^{-1}$ is a bijection between left and right cosets, so the two counts agree.)
>
> One right coset is $H$, via the representative $e$: the coset $He = \{h \cdot e : h \in H\} = H$. The right cosets also partition $G$ — the same disjoint-or-equal and exhaustive argument applies, with $g \in Hg$ because $g = eg$ and $e \in H$. So the second right coset is the complement of $H$, exactly as in Step 1:
> $$G \setminus H.$$
> Hence the complete list of right cosets is $\{\,H,\ G \setminus H\,\}$ — the same two sets that appeared as the left cosets.

**Step 3: Conclude $gH = Hg$ for every $g \in G$, hence $H \trianglelefteq G$.**

Every $g$ falls into one of two cases, and in each case its left coset and right coset are the same set. Therefore $gH = Hg$ for all $g$, which is the coset characterisation of normality.

> [!note]- Derivation
> Fix $g \in G$ and split on whether $g$ lies in $H$.
>
> *Case $g \in H$.* A coset equals $H$ exactly when its representative lies in $H$: if $g \in H$ then $gH = H$ (and $Hg = H$), because $gH \subseteq H$ by closure of the subgroup $H$ under products, and $H = g(g^{-1}H) \subseteq gH$ shows the reverse inclusion. So $gH = H = Hg$.
>
> *Case $g \notin H$.* Then the left coset $gH$ is not equal to $H$ — if it were, $g = ge$ would lie in $H$. By Step 1 there are only two left cosets, $H$ and $G \setminus H$, so $gH$ must be the other one:
> $$gH = G \setminus H.$$
> Identically, the right coset $Hg$ is not $H$, and by Step 2 the only other right coset is $G \setminus H$, so
> $$Hg = G \setminus H.$$
> Therefore $gH = G \setminus H = Hg$.
>
> In both cases $gH = Hg$. Since $g$ was arbitrary, $gH = Hg$ for **every** $g \in G$. The coset characterisation in [[Def - Normal Subgroup]] states that a subgroup is normal precisely when its left and right cosets coincide; equivalently, multiplying $gH = Hg$ on the left by $g^{-1}$ gives $g^{-1}Hg = H$ for all $g$, the conjugation definition of normality. Either way, $H \trianglelefteq G$. $\blacksquare$

> [!note]- Complete formal solution
> Let $H \leq G$ with $|G : H| = 2$.
>
> Since $|G : H| = 2$, there are exactly two left cosets of $H$. One of them is $H$ itself (the coset $eH = H$). The left cosets partition $G$: they are pairwise disjoint and their union is $G$, because every $g$ lies in $gH$ (as $g = ge$, $e \in H$) and two cosets that share an element are equal. Hence the second left coset is the complement $G \setminus H$, and the list of left cosets is $\{H,\ G \setminus H\}$.
>
> The same reasoning applies to right cosets. There are exactly two of them (the map $gH \mapsto Hg^{-1}$ is a bijection from left cosets to right cosets), one is $H$ (the coset $He = H$), and they partition $G$. So the list of right cosets is also $\{H,\ G \setminus H\}$.
>
> Now fix $g \in G$.
>
> - If $g \in H$, then $gH = H$ and $Hg = H$, so $gH = Hg$.
> - If $g \notin H$, then $gH \neq H$, so $gH$ is the other left coset $G \setminus H$; likewise $Hg \neq H$, so $Hg$ is the other right coset $G \setminus H$. Hence $gH = G \setminus H = Hg$.
>
> In either case $gH = Hg$. As $g \in G$ was arbitrary, $gH = Hg$ for all $g \in G$. This is the coset characterisation of a [[Def - Normal Subgroup|normal subgroup]] — equivalently $g^{-1}Hg = H$ for all $g$ — so $H \trianglelefteq G$. $\blacksquare$

---

# Key Takeaways

**A hypothesis on the index is a hypothesis on the number of cosets — exploit smallness directly.** The phrase "$|G : H| = 2$" is not really a numerical curiosity; it is the statement that the coset partition of $G$ has only two blocks. The reusable move is to recognise that whenever a problem hands you a subgroup of small index, you should immediately write out the entire coset partition, because a short list of cosets is a rigid object. With index two the rigidity is total: one block is forced to be $H$, the other is forced to be its complement, and there is simply no room for the left and right partitions to differ. The same instinct pays off for index three, four, or any small number — in those cases $G$ acts on the small set of cosets and you get a homomorphism into a small symmetric group $S_n$ — so "few cosets means strong structure" is the general principle, and index two is its sharpest and cheapest instance. Whenever you see a low index, do not compute; *enumerate*.

**Complementation turns one known coset into the other for free.** The engine of this proof is that the cosets of $H$ are *disjoint and exhaustive* — they tile the group with no overlaps and no gaps. When a partition has exactly two blocks and you know one of them, the other is determined with zero further work: it is the set-theoretic complement. This is why the left cosets and the right cosets cannot help but agree — both partitions consist of $H$ together with "the set of everything not in $H$", and that complementary set has only one possible identity. The transferable lesson is to look for situations where a structure is split into a known piece and exactly one unknown piece: the unknown piece is then no longer unknown. The technique generalises past cosets — it is the same reasoning that shows a subgroup of index two of any structure (a sublattice, a subspace over the two-element field, a subgroup inside a larger group) is forced to be a "halving" with no freedom — and it is the reason index-two phenomena are so abundant: the alternating group $A_n$ inside $S_n$, the rotation subgroup inside a dihedral group, the kernel of any homomorphism onto a two-element group.

**Prefer the cheap structural argument over a conjugation calculation.** Normality can always be checked by the definition — conjugate a general element $g h g^{-1}$ and verify it lands back in $H$ — but that calculation is laborious and, worse, teaches nothing reusable: it is bespoke to the particular group. The discipline this exercise installs is to *scan for a structural shortcut first*. Index two is one such shortcut; being a kernel is another; being the centre, or an intersection of normal subgroups, or the whole group, or the trivial subgroup, are others. Each of these certifies normality for a reason that generalises across all groups at once. The trigger is simply the appearance of the word "normal" as a goal: before touching the conjugation definition, ask whether the subgroup is visibly one of the standard always-normal types. Only when every structural route is exhausted should you fall back on conjugating a general element. This habit — cheap and general before expensive and specific — is the meta-skill the problem is really drilling.

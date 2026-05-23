---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
tags: [algebra, group-theory]
---

# Notation

For a [[Def - Subgroup|subgroup]] $H \leq G$ and an element $g \in G$, the **left coset** is $gH = \{gh : h \in H\}$ and the **right coset** is $Hg = \{hg : h \in H\}$. The set of all left cosets is written $G/H$, the set of all right cosets $H \backslash G$. The number of left cosets is the **index**, written $|G : H|$ (or $[G : H]$). The identity is $e$; note $eH = H$, so $H$ is itself one of its own cosets. See [[Group Theory I — §1.1–1.2]] for the full registry.

---

# Axiom Motivation

We have a [[Def - Group|group]] $G$ and a [[Def - Subgroup|subgroup]] $H$, and we want to **count $G$ in terms of $H$** and, ultimately, to build the [[Def - Quotient Group|quotient]] $G/H$. To do either we need to chop $G$ into pieces, each piece a faithful copy of $H$, with no overlaps and nothing left over. The coset is the definition of that piece. So the desideratum is precise: we want, for each subgroup $H$, a way of partitioning the set $G$ into blocks, all of the same size as $H$. If we can do that, then $|G|$ is just the number of blocks times $|H|$, which is [[Thm - Lagrange's Theorem|Lagrange's theorem]], and the blocks become the elements of the quotient.

How should the blocks be defined? The instinct is to translate $H$ around. The subgroup $H$ contains the identity and sits "at" $e$; sliding it by an element $g$ — multiplying every element of $H$ on the left by $g$ — produces the set $gH = \{gh : h \in H\}$, a translated copy of $H$. The claim is that these translates are exactly the blocks we wanted. Let us check the three desiderata, and in doing so see why the definition must be exactly $gH$ and not a variant.

**Same size as $H$.** Every block $gH$ should be a perfect copy of $H$, in the sense of having the same number of elements. This is true, and the reason is sharp: the map $h \mapsto gh$ is a **bijection** $H \to gH$. It is surjective by the definition of $gH$ (every element of $gH$ is $gh$ for some $h$), and it is injective because $gh_1 = gh_2$ forces $h_1 = h_2$ by left-cancellation in the group ([[Def - Group]]). So $|gH| = |H|$ for every $g$. This is where the *group* structure is essential — cancellation is what makes translation a bijection — and it is what lets the count "number of blocks times $|H|$" work.

**The blocks partition $G$.** Every element of $G$ should lie in exactly one block. Every $g$ lies in *some* block, namely its own: since $e \in H$, we have $g = ge \in gH$. The subtle part is "exactly one" — that two cosets are either identical or disjoint, never partially overlapping. This is true, but it depends on $H$ being a *subgroup*, not just any subset. Here is the mechanism: if $gH$ and $g'H$ share an element $x$, then $x = gh_1 = g'h_2$ for some $h_1, h_2 \in H$; rearranging, $g' = g h_1 h_2^{-1}$, and $h_1 h_2^{-1} \in H$ precisely because $H$ is closed under products and inverses. So $g'$ differs from $g$ by an element of $H$, and one checks this forces $gH = g'H$ entirely. **What breaks if $H$ is not a subgroup:** if $H$ failed to be closed under inverses or products, then $h_1 h_2^{-1}$ could escape $H$, two "cosets" could overlap in some elements but not all, and we would not have a partition at all. The subgroup axioms are *exactly* what is needed for the translates to partition. Take a subset of $\mathbb{Z}$ that is not a subgroup, say $S = \{0, 1\}$; the translates $0 + S = \{0,1\}$ and $1 + S = \{1,2\}$ overlap in $1$ without being equal — not a partition.

This gives the **equality criterion**, which is the single most useful fact about cosets and deserves to be stated as the heart of the motivation: $gH = g'H$ **if and only if** $g^{-1}g' \in H$. The forward direction is the computation above; the reverse: if $g^{-1}g' = h \in H$ then $g' = gh$, so $g'H = ghH = gH$ (using $hH = H$, since multiplying a subgroup by one of its own elements permutes it). The criterion is what lets you decide, mechanically, whether two labels $g$ and $g'$ name the same block — you just test whether $g^{-1}g'$ falls inside $H$.

There is one design decision still to justify: **left** cosets $gH$ versus **right** cosets $Hg = \{hg : h \in H\}$. Both work — both give partitions of $G$ into blocks of size $|H|$, and both prove Lagrange. The reason we cannot simply ignore the distinction is that for a *non-abelian* group the left coset $gH$ and the right coset $Hg$ are generally **different sets**: in $S_3$ with $H = \langle(1\,2)\rangle$, the left and right cosets of a $3$-cycle do not coincide. The [[Def - Subgroup|subgroups]] for which $gH = Hg$ for all $g$ are exactly the [[Def - Normal Subgroup|normal subgroups]], and that coincidence is precisely what makes the quotient construction possible — so the left/right distinction is not pedantry, it is the seed of normality. We standardize on left cosets; everything has a mirror-image right-coset version.

Finally, the **equivalence-relation viewpoint**, which explains *why* cosets partition without any computation. Define a relation on $G$ by $a \sim b \iff a^{-1}b \in H$. This is an equivalence relation: it is reflexive since $a^{-1}a = e \in H$; symmetric since $a^{-1}b \in H$ implies its inverse $b^{-1}a \in H$; and transitive since $a^{-1}b \in H$ and $b^{-1}c \in H$ multiply to $a^{-1}c \in H$. Each of the three properties uses exactly one subgroup axiom — identity, inverses, closure — which is the cleanest way to see that the subgroup axioms are *engineered* to make $\sim$ an equivalence relation. And any equivalence relation partitions its set into equivalence classes. The equivalence class of $a$ is $\{b : a^{-1}b \in H\} = \{b : b = ah \text{ for some } h\} = aH$. So **the cosets are the equivalence classes of $\sim$**, and they partition $G$ for the structural reason that equivalence classes always do. This is the conceptually correct way to hold the definition: a coset is "the set of elements indistinguishable from $g$, where two elements are deemed the same when they differ by an element of $H$".

---

# The Definition

Let $G$ be a [[Def - Group|group]] and $H \leq G$ a [[Def - Subgroup|subgroup]]. For $g \in G$, the **left coset of $H$ containing $g$** is the set

$$gH := \{x \in G : x = gh \text{ for some } h \in H\} = \{gh : h \in H\}.$$

Symmetrically, the **right coset** is $Hg := \{hg : h \in H\}$. The set of all left cosets is denoted $G/H = \{gH : g \in G\}$.

The **index** of $H$ in $G$, written $|G : H|$, is the number of left cosets — the cardinality of $G/H$. (Counting right cosets instead gives the same number.)

Three facts hold for every subgroup $H$:

- **Partition.** The left cosets partition $G$: every $g$ lies in exactly one coset, namely $gH$, and any two cosets are either equal or disjoint.
- **Equinumerosity.** For every $g$, the map $h \mapsto gh$ is a bijection $H \to gH$; hence $|gH| = |H|$.
- **Equality criterion.** $gH = g'H \iff g^{-1}g' \in H$. Equivalently, the cosets are the equivalence classes of the relation $a \sim b \iff a^{-1}b \in H$.

A subgroup for which $gH = Hg$ for all $g \in G$ is a [[Def - Normal Subgroup|normal subgroup]]; only for such [[Def - Subgroup|subgroups]] does $G/H$ carry a [[Def - Quotient Group|group structure]].

---

# Categorical Definition

Cosets are best seen categorically as the **orbits of a group action**, equivalently as a **quotient set / coequalizer**. The subgroup $H$ acts on the set $G$ by right multiplication: each $h \in H$ sends $g \mapsto gh$. This is a genuine action — the identity acts trivially and $(gh)h' = g(hh')$ — and the *orbit* of $g$ under this $H$-action is exactly the set $\{gh : h \in H\} = gH$. So the left cosets are precisely the orbits of $H$ acting on $G$ by right translation, and the orbit space is $G/H$. Since orbits of any group action always partition the set acted on, the partition property of cosets is a free consequence of this description — no computation needed. Dually, $G/H$ is the **coequalizer** in $\mathbf{Set}$ of the two maps $H \times G \rightrightarrows G$ given by $(h, g) \mapsto gh$ and $(h, g) \mapsto g$: the coequalizer is the universal set in which "$g$" and "$gh$" become equal, which is exactly the set of cosets together with the quotient map $G \to G/H$. When $H$ is moreover [[Def - Normal Subgroup|normal]], this coequalizer is computed in the category of [[Def - Group|groups]] rather than sets, and $G/H$ becomes the [[Def - Quotient Group|quotient group]].

---

# Relate to Other Fields / Compression

A coset is **the same construction as a parallel translate of a linear subspace, specialized to groups**. In a vector space $V$ with a subspace $W$, the sets $v + W = \{v + w : w \in W\}$ — the affine subspaces parallel to $W$ — partition $V$ into parallel copies of $W$, and the quotient $V/W$ is the set of these translates; this is exactly the coset construction with the group operation written additively. The solution set of an inhomogeneous linear system $Ax = b$ is precisely a coset $x_0 + \ker A$ of the subspace $\ker A$: "particular solution plus homogeneous solutions" is "pick a coset representative, add the subgroup". More broadly, a coset is **the fibre of a quotient map**: whenever you have a structure-preserving surjection, the preimages of points are cosets of the kernel. In number theory the residue class $a + n\mathbb{Z}$ — all integers congruent to $a$ modulo $n$ — is literally a coset of the subgroup $n\mathbb{Z}$ in $(\mathbb{Z}, +)$, so "congruence mod $n$" is the coset equivalence relation $a \sim b \iff a - b \in n\mathbb{Z}$.

---

# Examples / Corollaries

**Is an instance: cosets of $3\mathbb{Z}$ in $\mathbb{Z}$.** With $G = (\mathbb{Z}, +)$ and $H = 3\mathbb{Z}$, the operation is addition so a coset is $g + 3\mathbb{Z}$. There are exactly three: $0 + 3\mathbb{Z} = \{\ldots, -3, 0, 3, \ldots\}$, $1 + 3\mathbb{Z} = \{\ldots, -2, 1, 4, \ldots\}$, $2 + 3\mathbb{Z} = \{\ldots, -1, 2, 5, \ldots\}$. They partition $\mathbb{Z}$, each is infinite (a copy of the infinite group $3\mathbb{Z}$), and the equality criterion reads $a + 3\mathbb{Z} = b + 3\mathbb{Z} \iff a - b \in 3\mathbb{Z}$, i.e. $a \equiv b \pmod 3$. The index is $|\mathbb{Z} : 3\mathbb{Z}| = 3$. This is the cleanest example: cosets *are* [[Def - Residue|residue]] classes.

**Is an instance: cosets in a finite group.** Take $G = S_3$ (order $6$) and $H = \langle(1\,2\,3)\rangle = \{e, (1\,2\,3), (1\,3\,2)\}$, the rotation subgroup, of order $3$. There are $|S_3 : H| = 6/3 = 2$ left cosets: $H$ itself, and the coset $(1\,2)H = \{(1\,2), (2\,3), (1\,3)\}$ of all three transpositions. They partition the six elements into two blocks of three. This example also probes Lagrange directly: $6 = 3 \times 2$.

**Is an instance: a coset equal to the subgroup.** For *any* $h \in H$, the coset $hH$ equals $H$ itself, because multiplying $H$ by one of its own elements just permutes $H$. So $H$ is its own coset, and it is the *only* coset that is a subgroup. This probes the equality criterion: $hH = eH \iff e^{-1}h = h \in H$, which holds exactly when $h \in H$.

**Is NOT an instance of a subgroup: a non-trivial coset.** A coset $gH$ with $g \notin H$ is **not** a [[Def - Subgroup|subgroup]] of $G$: it does not contain the identity, since $e \in gH$ would force $g \in H$. So cosets partition $G$ into blocks, but only one block (namely $H$) is a group. This is the crucial conceptual point — cosets are *cells of a partition*, not subgroups, and the [[Def - Quotient Group|quotient]] makes them into the *elements* of a new group rather than subgroups of the old one.

**Is NOT an instance of left = right: cosets in a non-abelian group.** In $S_3$ with $H = \langle(1\,2)\rangle = \{e, (1\,2)\}$, the left coset $(1\,2\,3)H = \{(1\,2\,3), (1\,2\,3)(1\,2)\} = \{(1\,2\,3), (1\,3)\}$ while the right coset $H(1\,2\,3) = \{(1\,2\,3), (1\,2)(1\,2\,3)\} = \{(1\,2\,3), (2\,3)\}$. These are different sets. This non-example is the whole reason [[Def - Normal Subgroup|normality]] exists: normal subgroups are exactly those for which this never happens.

**Corollary (Lagrange's theorem).** If $G$ is finite, the cosets of $H$ partition $G$ into $|G : H|$ blocks each of size $|H|$, so $|G| = |H| \cdot |G : H|$; in particular $|H|$ divides $|G|$. This is [[Thm - Lagrange's Theorem]], and it is an *immediate* corollary of the partition and equinumerosity facts. *Calibration check:* if you can derive Lagrange from "cosets partition into equal-sized blocks", you have understood cosets.

**Corollary (the index can be infinite-group-finite).** A subgroup of an infinite group can have finite index — $|\mathbb{Z} : 3\mathbb{Z}| = 3$ even though both [[Def - Group|groups]] are infinite. The index counts *blocks*, not elements, so it is meaningful and often finite even when $|G|$ and $|H|$ are not. *Calibration check:* this is why $|G : H|$ is given its own notation rather than being defined as $|G|/|H|$ — the quotient of cardinalities may be undefined, but the count of cosets is not.

**Corollary ($\sim$ is an equivalence relation).** The relation $a \sim b \iff a^{-1}b \in H$ is reflexive, symmetric, and transitive, with one subgroup axiom underwriting each property; its equivalence classes are the left cosets. This recasts the partition property as the general fact that equivalence classes partition. *Calibration check:* matching each of reflexivity, symmetry, transitivity to the identity, inverse, closure axiom confirms you see why $H$ must be a subgroup.

---

# Unlocked by This

> [!tip] Quotient Group *(this topic, §1.2)*
> Once the cosets of $H$ are in hand, the natural next move is to make the *set* of cosets $G/H$ into a *group* by the rule $(gH)(g'H) = gg'H$. This works exactly when $H$ is a [[Def - Normal Subgroup|normal subgroup]]; the result is the [[Def - Quotient Group|quotient group]], the central construction of this topic.

> [!tip] Homogeneous Space *(from Differential Geometry)*
> When $G$ is a Lie group and $H$ a closed subgroup, the coset space $G/H$ is a smooth manifold called a homogeneous space — the sphere, projective space, and Grassmannians all arise this way. The set-level coset partition you have just defined is the skeleton of that geometry.

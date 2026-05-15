---
type: theorem
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Group Action"
  - "Def - Orbit and Stabiliser"
  - "Def - Subgroup"
  - "Def - Coset"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Notation

$G$ is a group acting on a set $X$ via $(g, x) \mapsto g\cdot x$ (see [[Def - Group Action]]). For a point $x \in X$, the **orbit** is $G\cdot x = \{g\cdot x : g \in G\} \subseteq X$ — all the points $x$ can be moved to — and the **stabiliser** is $G_x = \{g \in G : g\cdot x = x\} \leq G$ — all the elements of $G$ that fix $x$ (see [[Def - Orbit and Stabiliser]]). The stabiliser is always a [[Def - Subgroup|subgroup]]. The set of left [[Def - Coset|cosets]] of $G_x$ in $G$ is written $G/G_x$, and the **index** $|G : G_x|$ is the number of such cosets. An action is **transitive** when $X$ is a single orbit. The full notation registry lives on the parent page [[Group Theory II — §1.3–1.4]].

---

# Statement

> **Theorem (Orbit-Stabiliser).** Let a group $G$ act on a set $X$, and fix $x \in X$. The map
> $$\Phi : G/G_x \longrightarrow G\cdot x, \qquad g\,G_x \longmapsto g\cdot x$$
> is a well-defined [[Def - Isomorphism|bijection]] between the set of left [[Def - Coset|cosets]] of the [[Def - Orbit and Stabiliser|stabiliser]] $G_x$ and the [[Def - Orbit and Stabiliser|orbit]] $G\cdot x$.

> **Counting form.** If $G$ is finite, then for every $x \in X$
> $$|G| \;=\; |G_x|\cdot|G\cdot x|,$$
> equivalently $|G\cdot x| = |G : G_x|$. In particular, **every orbit size divides $|G|$**.

The bijective form holds for arbitrary (possibly infinite) groups; the counting form is its finite specialisation, obtained by [[Thm - Lagrange's Theorem|Lagrange's theorem]] applied to the subgroup $G_x$. This is the master counting theorem of finite group theory: the [[Thm - The Class Equation|class equation]], the conjugate-counting formula, and [[Thm - Lagrange's Theorem|Lagrange's theorem]] itself are all instances of it.

---

# Motivation

A group action presents two numbers attached to each point $x$, and at first sight they measure unrelated things. The [[Def - Orbit and Stabiliser|orbit]] $G\cdot x$ records *how far $x$ can travel* — how many distinct points it can be sent to. The [[Def - Orbit and Stabiliser|stabiliser]] $G_x$ records *how much of $G$ ignores $x$* — how many group elements leave it fixed. One is a subset of $X$, the other a subgroup of $G$; one is about motion, the other about rest.

The orbit-stabiliser theorem says these two numbers are not independent: they are *complementary*, and their product is the whole of $|G|$. Largeness of the orbit is exactly smallness of the stabiliser, in lockstep, with $|G|$ as the fixed budget. If $x$ moves to many places, few elements can fix it; if $x$ is fixed by much of $G$, it cannot move far. This is the conservation law of group actions, and it is the reason actions are the central tool of finite group theory.

The reason it matters so much in practice is that it converts *structure into arithmetic*. Many questions about a finite group are secretly questions of the form "how big is this set the group acts on" — how many symmetries a polyhedron has, how many elements are conjugate to a given one, how many subgroups have a given order. The orbit-stabiliser theorem turns each such question into the integer equation $|G| = |G_x|\cdot|G\cdot x|$: know any two of $|G|$, $|G_x|$, $|G\cdot x|$ and the third is forced. And even when you know only $|G|$, the theorem still bites — it says every orbit size *divides* $|G|$, an immediate and often decisive constraint. Counting symmetries, counting conjugates, proving an orbit must be small or large: all of it routes through this one equation. The entire skill the topic trains — *choose the right set for $G$ to act on* — exists because, once the set is chosen, this theorem does the rest.

---

# Sources and Targets

This section is not an input/output summary. Sources record the non-obvious circumstances under which you hold the hypothesis — *a group acting on a set*. Targets record what becomes provable once the conclusion $|G| = |G_x|\cdot|G\cdot x|$ is combined with one further fact. Both are distilled from the exercises that actually use the theorem.

**Sources (Input Broadening)**

The hypothesis is "$G$ acts on a set $X$". The art of the whole topic is recognizing — or *constructing* — an action where the problem advertises none.

The first source is **a geometric object with symmetries**. Property $B$ is "$G$ is the symmetry group of a shape, and $X$ is a set of features of that shape — its faces, edges, vertices, diagonals". The bridge is that symmetries permute features, which is an action. The implication is non-obvious because the question usually asks for $|G|$, an unknown, while the features are concrete and countable. Example: to find the order of the rotation group of a cube, let it act on the $6$ faces; the orbit is all $6$ faces (one orbit), the stabiliser of a face is the $4$ rotations about the axis through it, so $|G| = 4\cdot 6 = 24$.

The second source is **a subgroup, accessed through its cosets**. Property $B$ is "$H \leq G$ is a subgroup" and $X = G/H$ the coset space. The bridge is the [[Thm - Coset Action and the Normal Core|coset action]] $g\cdot(xH) = gxH$. The implication is non-obvious because a subgroup is a static algebraic object with no action attached, yet it generates one on its own coset space. Example: any divisibility question about the index $|G:H|$ becomes an orbit-size question for this action.

The third source is **an element or subgroup whose conjugates matter**. Property $B$ is "you are interested in the conjugates $gxg^{-1}$ of an element $x$, or $gHg^{-1}$ of a subgroup $H$". The bridge is the *conjugation action* of $G$ on itself, or on its set of subgroups. The implication is non-obvious because "the set of things conjugate to $x$" does not look like an orbit until you name the action. Then the orbit of $x$ is its [[Def - Conjugacy Class|conjugacy class]], the stabiliser is the [[Def - Centraliser and Centre|centraliser]] $C_G(x)$, and orbit-stabiliser gives $|\operatorname{ccl}(x)| = |G : C_G(x)|$ — this is exactly the [[Thm - The Class Equation|class equation]]'s input. For a subgroup, the stabiliser is the [[Def - Normaliser|normaliser]] and the orbit count is $|G : N_G(H)|$.

The fourth source is **a set of subsets or sub-configurations of a fixed size**. Property $B$ is "$X$ is the collection of all $k$-element subsets of something $G$ permutes, or all subgroups of a given order, or all colourings of an object". The bridge is that $G$ permutes these derived objects whenever it permutes the underlying one. The implication is non-obvious because one must first *manufacture* the set $X$ from the data of the problem. Example: this is how a $p$-group is made to act on its $p^a$-element subsets in the proof of Sylow's first theorem — orbit sizes dividing $|G|$ force an orbit of the right size to exist.

**Targets (Output Amplification)**

The conclusion is $|G| = |G_x|\cdot|G\cdot x|$, and the standalone fact $|G\cdot x| \mid |G|$.

The first combination is **orbit-stabiliser plus the regular action recovers Lagrange**. The conclusion gives $|G| = |G_x|\cdot|G\cdot x|$. Add property $D$: take $G$ acting on the cosets $G/H$ of a subgroup $H$ by left multiplication, and look at the point $x = H$. Its stabiliser is $H$ itself and its orbit is all of $G/H$. Substituting, $|G| = |H|\cdot|G/H| = |H|\cdot|G:H|$. The further result $E$ is [[Thm - Lagrange's Theorem|Lagrange's theorem]]. The combination is non-obvious because Lagrange looks logically prior to actions, yet it is the special case of orbit-stabiliser for the coset action — so this theorem *contains* Lagrange.

The second combination is **orbit-stabiliser plus the conjugation action, summed, gives the class equation**. The conclusion gives $|\operatorname{ccl}(x)| = |G:C_G(x)|$ for the conjugation action. Add property $D$: the conjugacy classes partition $G$, and the singleton classes are exactly the central elements. Summing the orbit sizes over a set of class representatives yields $|G| = |Z(G)| + \sum_i |G:C_G(x_i)|$. The result $E$ is the [[Thm - The Class Equation|class equation]]. The combination is non-obvious because it requires seeing conjugacy classes *as orbits* and then partitioning; it is the single most consequential use of the theorem in §1.4 and beyond.

The third combination is **orbit-stabiliser plus a transitive action pins down a stabiliser's index**. The conclusion gives $|G\cdot x| = |G:G_x|$. Add property $D$: the action is transitive, so $G\cdot x = X$ and $|X| = |G:G_x|$. The result $E$ is that the stabiliser of any point of a transitive action has index exactly $|X|$ — so a transitive action on a set of size $n$ is "the same as" the action on cosets of an index-$n$ subgroup. The combination is non-obvious because it reverses the usual direction: instead of computing an orbit from a stabiliser, it reads the index of a mysterious stabiliser off the visible size of $X$.

The fourth combination is **orbit-stabiliser plus "$|G|$ has restricted divisibility" forces orbit sizes**. The conclusion gives $|G\cdot x| \mid |G|$ for every $x$. Add property $D$: $|G| = p^a$ is a prime power. Then every orbit size is a power of $p$, so an orbit is either a *single point* (size $p^0$) or has size divisible by $p$. The result $E$: in a $p$-group action, the number of fixed points is congruent to $|X|$ modulo $p$ — the fixed-point-congruence lemma, the workhorse behind Cauchy's theorem and the Sylow congruences. The combination is non-obvious because it extracts a *modular* statement from a *divisibility* statement by sorting orbits into "trivial" and "$p$-divisible".

---

# Why Is It True

The theorem should feel inevitable once you see what the orbit and the stabiliser are *measuring*, and why they measure complementary halves of $G$.

Fix the point $x$, and think of every element $g \in G$ as a "delivery instruction": $g$ delivers $x$ to the destination $g\cdot x$. The orbit $G\cdot x$ is precisely the set of *destinations actually reached*. Now ask: how many different delivery instructions land at the *same* destination? Suppose $g$ and $h$ both deliver $x$ to the same place, $g\cdot x = h\cdot x$. Then $h^{-1}g\cdot x = x$, which says $h^{-1}g \in G_x$ — the discrepancy between two instructions reaching the same place is an element of the stabiliser. And this is reversible: $g$ and $gk$ deliver $x$ to the same place for every $k \in G_x$. So the instructions landing at a given destination form *exactly a coset* $g\,G_x$ of the stabiliser.

That is the whole theorem in one sentence: **the instructions are sorted by destination, and the sorting bins are the cosets of the stabiliser**. Each destination in the orbit corresponds to one bin; each bin is one coset. So the orbit and the set of cosets are in bijection — there are as many destinations as there are bins. This is the bijective statement, and it holds for any group, finite or not, because it is purely the observation "same destination $\iff$ same coset".

Now make it quantitative for finite $G$. The cosets of $G_x$ all have the same size — every coset is a translate of $G_x$, and translation is reversible — so each delivery-bin contains exactly $|G_x|$ instructions. The bins do not overlap and together exhaust all of $G$ (every element is *some* instruction, landing *somewhere*). So $G$ is partitioned into $|G\cdot x|$ bins, each of size $|G_x|$. Counting elements bin by bin:
$$|G| = (\text{number of bins})\times(\text{bin size}) = |G\cdot x|\times|G_x|.$$
There is no slack, because there is none in the picture: $G$ is genuinely chopped into equal-sized bins indexed by orbit points.

This is why orbit size and stabiliser size are complementary. The number $|G|$ is a fixed budget. It is spent in two ways at once: a little on the orbit (how many places to go) and a little on the stabiliser (how many ways to stay), and the two factors multiply to the budget. A point with a huge orbit has spent the budget on travel, leaving a small stabiliser; a point with a huge stabiliser has spent it on rest, leaving a small orbit. The trade-off is forced — it is just the multiplication $|G_x|\cdot|G\cdot x| = |G|$. And the divisibility corollary, that $|G\cdot x|$ divides $|G|$, is immediate: an orbit size is a factor in a product equal to $|G|$, so it divides $|G|$.

The theorem is, in the end, [[Thm - Lagrange's Theorem|Lagrange's theorem]] wearing a different costume. Lagrange says a subgroup tiles the group into equal cosets; orbit-stabiliser says the stabiliser subgroup tiles the group into equal bins, *and identifies the tiles with the points of the orbit*. The new content beyond Lagrange is only that last identification — the bijection $g\,G_x \leftrightarrow g\cdot x$ — and that identification is what makes the theorem a *counting tool for the orbit* rather than a counting tool for an abstract index.

---

# What Makes This Hard

The proof has exactly one delicate step, and it is **well-definedness** of the map $\Phi(g\,G_x) = g\cdot x$: the input is a coset, named by a representative $g$, and one must check the *output does not depend on the choice of representative* — if $g\,G_x = h\,G_x$ then $g\cdot x = h\cdot x$. People routinely skip this and verify only the bijection, but a map on cosets that is not well-defined is not a map at all. The non-obvious idea is that the same equivalence — $g\,G_x = h\,G_x \iff h^{-1}g \in G_x \iff g\cdot x = h\cdot x$ — proves well-definedness *and* injectivity simultaneously, read in the two directions. The common error is to conflate the stabilisers of different points of the orbit; they are only *conjugate* ($G_{g\cdot x} = g\,G_x\,g^{-1}$), equal in size but generally distinct subgroups.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Define $\Phi : G/G_x \to G\cdot x$ by $g\,G_x \mapsto g\cdot x$. The single identity $g\cdot x = h\cdot x \iff h^{-1}g \in G_x \iff g\,G_x = h\,G_x$ does almost everything: read left-to-right it gives well-definedness, read right-to-left it gives injectivity. Surjectivity is the definition of the orbit. Then $\Phi$ is a bijection; for finite $G$, count cosets with [[Thm - Lagrange's Theorem|Lagrange]] to get $|G| = |G_x|\cdot|G\cdot x|$.

**Subgoal decomposition:**

1. **The key equivalence.** Show that for $g, h \in G$, the conditions $g\cdot x = h\cdot x$, $\ h^{-1}g \in G_x$, and $\ g\,G_x = h\,G_x$ are all equivalent.
   - *Hint:* $g\cdot x = h\cdot x \iff (h^{-1}g)\cdot x = x$ (act by $h^{-1}$, use the action axioms), which is the definition of $h^{-1}g \in G_x$; and $h^{-1}g \in G_x \iff g\,G_x = h\,G_x$ is the standard criterion for two cosets to coincide.
   - *Why needed:* It is the engine of the entire proof — it supplies both well-definedness and injectivity in one stroke.

2. **$\Phi$ is well-defined.** Show $g\,G_x = h\,G_x$ implies $g\cdot x = h\cdot x$, so the rule $g\,G_x \mapsto g\cdot x$ does not depend on the coset representative.
   - *Hint:* This is the equivalence of Subgoal 1 read from "$g\,G_x = h\,G_x$" to "$g\cdot x = h\cdot x$".
   - *Why needed:* Without it, $\Phi$ is not a function on cosets.

3. **$\Phi$ is injective.** Show $g\cdot x = h\cdot x$ implies $g\,G_x = h\,G_x$.
   - *Hint:* The same equivalence, read the other direction.
   - *Why needed:* Distinct cosets must map to distinct orbit points for $\Phi$ to be a bijection.

4. **$\Phi$ is surjective.** Show every point of $G\cdot x$ is $\Phi(g\,G_x)$ for some $g$.
   - *Hint:* By definition $G\cdot x = \{g\cdot x : g \in G\}$, and $g\cdot x = \Phi(g\,G_x)$.
   - *Why needed:* Completes the bijection $G/G_x \leftrightarrow G\cdot x$.

5. **Counting form.** For finite $G$, conclude $|G\cdot x| = |G:G_x|$ and hence $|G| = |G_x|\cdot|G\cdot x|$.
   - *Hint:* A bijection equates cardinalities, so $|G\cdot x| = |G/G_x| = |G:G_x|$; then [[Thm - Lagrange's Theorem|Lagrange]] gives $|G| = |G_x|\cdot|G:G_x|$.
   - *Why needed:* It is the arithmetic form in which the theorem is used.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

<details>
<summary><strong>Lemma 1: The stabiliser is a subgroup</strong></summary>

**Statement:** For an action of $G$ on $X$ and any $x \in X$, the stabiliser $G_x = \{g \in G : g\cdot x = x\}$ is a [[Def - Subgroup|subgroup]] of $G$.

**Hint:** Check non-emptiness, closure under products, and closure under inverses, using only the two action axioms.

**Why needed:** $G_x$ must be a subgroup for "cosets of $G_x$" and Lagrange's theorem to make sense.

<details>
<summary>Full proof</summary>

*Identity:* $e\cdot x = x$ by the identity axiom, so $e \in G_x$ and $G_x$ is non-empty.

*Products:* if $g, h \in G_x$, then $(gh)\cdot x = g\cdot(h\cdot x) = g\cdot x = x$, using the associativity axiom and $h\cdot x = x$, then $g\cdot x = x$. So $gh \in G_x$.

*Inverses:* if $g \in G_x$, then $g\cdot x = x$; acting by $g^{-1}$ gives $g^{-1}\cdot(g\cdot x) = g^{-1}\cdot x$, and the left side is $(g^{-1}g)\cdot x = e\cdot x = x$. So $g^{-1}\cdot x = x$, i.e. $g^{-1} \in G_x$.

Hence $G_x \leq G$.

</details>
</details>

<details>
<summary><strong>Lemma 2: Same orbit point iff same coset of the stabiliser</strong></summary>

**Statement:** For $g, h \in G$ and a fixed $x \in X$: $\ g\cdot x = h\cdot x \iff h^{-1}g \in G_x \iff g\,G_x = h\,G_x$.

**Hint:** Move everything to one side by acting with $h^{-1}$; then use the standard coset-equality criterion.

**Why needed:** This is the heart of the theorem — it gives well-definedness and injectivity of $\Phi$ together.

<details>
<summary>Full proof</summary>

*First equivalence.* Suppose $g\cdot x = h\cdot x$. Act by $h^{-1}$ on both sides:
$$h^{-1}\cdot(g\cdot x) = h^{-1}\cdot(h\cdot x) \;\Longrightarrow\; (h^{-1}g)\cdot x = (h^{-1}h)\cdot x = e\cdot x = x,$$
using the associativity and identity axioms. So $(h^{-1}g)\cdot x = x$, i.e. $h^{-1}g \in G_x$. Conversely, if $h^{-1}g \in G_x$ then $(h^{-1}g)\cdot x = x$; acting by $h$ gives $g\cdot x = h\cdot x$ by the same axioms.

*Second equivalence.* By the standard criterion for left cosets, $g\,G_x = h\,G_x$ holds if and only if $h^{-1}g \in G_x$.

Chaining the two gives the stated triple equivalence.

</details>
</details>

<details>
<summary><strong>Lemma 3: The orbit-coset map is a bijection</strong></summary>

**Statement:** The map $\Phi : G/G_x \to G\cdot x$, $\ \Phi(g\,G_x) = g\cdot x$, is well-defined, injective, and surjective.

**Hint:** Well-definedness and injectivity are the two directions of Lemma 2; surjectivity is the definition of the orbit.

**Why needed:** This is the bijective form of the theorem, valid for all groups.

<details>
<summary>Full proof</summary>

*Well-defined.* If $g\,G_x = h\,G_x$, then by Lemma 2, $g\cdot x = h\cdot x$, so $\Phi$ assigns the same value to a coset regardless of the chosen representative.

*Injective.* If $\Phi(g\,G_x) = \Phi(h\,G_x)$, then $g\cdot x = h\cdot x$, so by Lemma 2, $g\,G_x = h\,G_x$.

*Surjective.* By definition $G\cdot x = \{g\cdot x : g \in G\}$. Any $g\cdot x$ in the orbit equals $\Phi(g\,G_x)$, so $\Phi$ hits every element of $G\cdot x$.

Hence $\Phi$ is a bijection.

</details>
</details>

<details>
<summary><strong>Lemma 4: Stabilisers along an orbit are conjugate</strong></summary>

**Statement:** For points $x$ and $g\cdot x$ in the same orbit, $G_{g\cdot x} = g\,G_x\,g^{-1}$. In particular $|G_{g\cdot x}| = |G_x|$.

**Hint:** Translate the condition "$h$ fixes $g\cdot x$" into a condition on $g^{-1}hg$.

**Why needed:** It explains why the counting form $|G| = |G_x|\cdot|G\cdot x|$ is independent of the chosen point $x$ — and corrects the tempting error of treating "the stabiliser" as a single subgroup.

<details>
<summary>Full proof</summary>

An element $h$ fixes $g\cdot x$ iff $h\cdot(g\cdot x) = g\cdot x$. Acting by $g^{-1}$: this holds iff $(g^{-1}hg)\cdot x = x$, i.e. iff $g^{-1}hg \in G_x$, i.e. iff $h \in g\,G_x\,g^{-1}$. So $G_{g\cdot x} = g\,G_x\,g^{-1}$.

Conjugation by $g$ is a bijection $G_x \to g\,G_x\,g^{-1}$, so the two subgroups have equal order. Hence every point of the orbit has a stabiliser of the same size, and $|G| = |G_x|\cdot|G\cdot x|$ does not depend on which $x$ in the orbit is used.

</details>
</details>

---

# Formal Proof

<details>
<summary><strong>Complete formal proof</strong></summary>

**Theorem.** Let $G$ act on $X$ and fix $x \in X$. The map $\Phi : G/G_x \to G\cdot x$, $\ g\,G_x \mapsto g\cdot x$, is a bijection. If $G$ is finite, $|G| = |G_x|\cdot|G\cdot x|$.

*Proof.* First, $G_x$ is a [[Def - Subgroup|subgroup]] of $G$: it contains $e$ since $e\cdot x = x$; it is closed under products since $g, h \in G_x$ give $(gh)\cdot x = g\cdot(h\cdot x) = g\cdot x = x$; and it is closed under inverses since $g\cdot x = x$ gives $g^{-1}\cdot x = (g^{-1}g)\cdot x = e\cdot x = x$. So the left cosets $G/G_x$ are defined.

We claim that for all $g, h \in G$,
$$g\cdot x = h\cdot x \iff h^{-1}g \in G_x \iff g\,G_x = h\,G_x. \tag{$\ast$}$$
For the first equivalence: $g\cdot x = h\cdot x$ holds iff, acting by $h^{-1}$, $(h^{-1}g)\cdot x = (h^{-1}h)\cdot x = e\cdot x = x$ — that is, iff $h^{-1}g \in G_x$. The second equivalence is the standard criterion for equality of left cosets.

*$\Phi$ is well-defined.* If $g\,G_x = h\,G_x$, then by $(\ast)$ read right-to-left into the middle and then to the left, $g\cdot x = h\cdot x$; so $\Phi(g\,G_x)$ is independent of the representative.

*$\Phi$ is injective.* If $\Phi(g\,G_x) = \Phi(h\,G_x)$, then $g\cdot x = h\cdot x$, so by $(\ast)$, $g\,G_x = h\,G_x$.

*$\Phi$ is surjective.* Every element of $G\cdot x = \{g\cdot x : g \in G\}$ is of the form $g\cdot x = \Phi(g\,G_x)$.

Hence $\Phi : G/G_x \to G\cdot x$ is a bijection.

*Counting form.* Suppose $G$ is finite. The bijection $\Phi$ gives $|G\cdot x| = |G/G_x| = |G : G_x|$, the number of left cosets of $G_x$. By [[Thm - Lagrange's Theorem|Lagrange's theorem]], $|G| = |G_x|\cdot|G : G_x|$. Substituting,
$$|G| = |G_x|\cdot|G\cdot x|.$$
In particular $|G\cdot x|$ divides $|G|$. $\qquad\blacksquare$

This is the orbit-stabiliser theorem as stated in §1.3 of the source lecture notes; the notes record the bijective form $G\cdot x \leftrightarrow G/G_x$, valid for arbitrary groups, with the counting form as the finite specialisation.

</details>

---

# Cross-Field Exercise Suggestions

The aim is to find settings where orbit-stabiliser applies but is not advertised, battle-testing recognition of the *sources*.

**Enumerative combinatorics: counting colourings up to symmetry.** Burnside's lemma — the number of orbits equals the average fixed-point count $\frac{1}{|G|}\sum_g|X^g|$ — is proved by counting the incidence set $\{(g,x) : g\cdot x = x\}$ two ways, and the orbit-stabiliser theorem is the step that rewrites the count over $x$ as a sum of $|G|/|G\cdot x|$ terms. So every necklace-counting, cube-colouring, or chemical-isomer enumeration secretly invokes orbit-stabiliser. The application is non-obvious because the problem is phrased as raw enumeration with no group equation in sight; the property $B$ "a symmetry group acts on the set of colourings" is the bridge.

**Geometry: the sphere, hyperbolic plane, and homogeneous spaces.** A homogeneous space is a set on which a group acts transitively; orbit-stabiliser then identifies it with a coset space $G/G_x$. The $2$-sphere is $\mathrm{SO}(3)/\mathrm{SO}(2)$ because $\mathrm{SO}(3)$ acts transitively on it with the stabiliser of a point a circle of rotations. The application is non-obvious because the sphere is a geometric object, not visibly a set of cosets; recognizing it as $G/G_x$ via the transitive-action source is the foundation of the theory of symmetric spaces and, in physics, of the orbit method for classifying particle states.

**Number theory: counting solutions and class numbers.** When a group acts on the set of solutions to a Diophantine equation, or on the set of representations of an integer by a quadratic form, orbit-stabiliser turns "count solutions up to equivalence" into orbit counting, and the stabiliser indices control multiplicities. The application is non-obvious because the arithmetic problem mentions no group; the symmetry group of the equation must be supplied. This underlies the mass formulas in the theory of quadratic forms, where each orbit is weighted by $1/|G_x|$.

**Linear algebra and physics: the dimension of an orbit.** For a Lie group acting smoothly on a manifold, the orbit-stabiliser bijection $G/G_x \cong G\cdot x$ upgrades to a diffeomorphism, so $\dim(G\cdot x) = \dim G - \dim G_x$ — the *continuous* analogue of the counting form, with dimension replacing cardinality. The application is non-obvious because the theorem was stated for finite groups and sizes, yet the same bijection, now in the smooth category, computes the dimension of a coadjoint orbit (the phase spaces of geometric mechanics) as $\dim G$ minus the dimension of an isotropy subgroup.

---

# Bridges

- **[[Thm - Lagrange's Theorem|Lagrange's Theorem]]** — orbit-stabiliser *is* Lagrange, generalised. Lagrange counts a subgroup against the group via cosets; orbit-stabiliser does the same with the stabiliser subgroup, and additionally identifies the cosets with the points of an orbit. Conversely, Lagrange is the special case of orbit-stabiliser for $G$ acting on $G/H$ by left multiplication, at the point $x = H$. The two theorems are the same conservation law, one stated for abstract indices and one for orbits.

- **[[Thm - The Class Equation|The Class Equation]]** — the class equation is orbit-stabiliser applied to the conjugation action and then summed. Each [[Def - Conjugacy Class|conjugacy class]] is an orbit, with size $|G:C_G(x)|$ by orbit-stabiliser; partitioning $G$ into classes and separating the singletons gives $|G| = |Z(G)| + \sum|G:C_G(x_i)|$. The class equation is this theorem's most consequential single application.

- **[[Thm - Cayley's Theorem|Cayley's Theorem]]** — Cayley uses the *regular* action, which is transitive and free, so orbit-stabiliser there is the tautology $|G| = 1\cdot|G|$. Cayley extracts content from that action through its kernel rather than through orbit counting — it is the action on which orbit-stabiliser says nothing and the homomorphism viewpoint says everything. The two theorems exploit complementary features of group actions.

- **[[Def - Normaliser|Normaliser]] and conjugate subgroups** — applying orbit-stabiliser to the action of $G$ by conjugation on its set of subgroups gives: the number of conjugates of a subgroup $H$ is $|G : N_G(H)|$, with the [[Def - Normaliser|normaliser]] as the stabiliser. This is the standard tool for counting subgroups of a given type, and it is the orbit-stabiliser theorem specialised one more time.

- **Burnside's Lemma and Pólya Counting** *(from Enumerative Combinatorics)* — averaging fixed-point counts over the group counts orbits: $\#\{\text{orbits}\} = \frac{1}{|G|}\sum_g|X^g|$. The proof double-counts the incidence set $\{(g,x):g\cdot x = x\}$, and orbit-stabiliser is the lemma that converts the per-point count into $|G|/|G\cdot x|$. Burnside's lemma turns this theorem from a structural identity into a counting engine for configurations up to symmetry.

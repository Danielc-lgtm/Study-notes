---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Normal Subgroup"
  - "Def - Subgroup"
  - "Def - Conjugacy Class"
  - "Def - Simple Group"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be a group and let $N \leq G$ be a subgroup. Prove that
$$N \trianglelefteq G \qquad \Longleftrightarrow \qquad N \text{ is a union of conjugacy classes of } G.$$
That is: $N$ is normal in $G$ if and only if, whenever $n \in N$, the entire conjugacy class $\operatorname{ccl}_G(n)$ is contained in $N$.

**Recall:**

The objects in play are a subgroup, normality, and conjugacy classes.

A [[Def - Subgroup|subgroup]] $N \leq G$ is a subset of $G$ containing the identity $e$ and closed under products and inverses.

![[Def - Normal Subgroup#The Definition]]

So a [[Def - Normal Subgroup|normal subgroup]] $N \trianglelefteq G$ is a subgroup satisfying $gNg^{-1} = N$ for all $g \in G$, where $gNg^{-1} = \{gng^{-1} : n \in N\}$.

![[Def - Conjugacy Class#The Definition]]

So the [[Def - Conjugacy Class|conjugacy class]] of $n$ is $\operatorname{ccl}_G(n) = \{gng^{-1} : g \in G\}$ — the orbit of $n$ under the action of $G$ on itself by conjugation. A central fact about orbits, used here, is that they **partition** $G$: every element of $G$ lies in exactly one conjugacy class. To say a subset $S \subseteq G$ is a *union of conjugacy classes* therefore means that $S$ contains, with any element $s$, the whole class of $s$ — equivalently, $S$ is "saturated" for conjugation: conjugating any element of $S$ never leaves $S$.

---

# Convergent Strategy

**Problem class.** This is a *prove an equivalence* problem — a biconditional connecting a structural property (normality) to a set-theoretic shape (being a union of classes). It belongs to the family the [[Group Theory II — §1.3–1.4#Problem-Solving Strategy|topic page's strategy]] groups under "questions about the centre, commutativity, or the existence of a normal subgroup", all of which are handled by the conjugation action.

**Assumption pattern.** The hypothesis is minimal — $N$ is merely *a subgroup* of $G$. What makes the problem tractable is not an extra assumption but a *change of viewpoint*: read the defining condition of normality, $gNg^{-1} = N$, as a statement about the conjugation action. The set $gNg^{-1}$ is the image of $N$ under conjugation by $g$, and demanding it equal $N$ for every $g$ is demanding that $N$ be a *fixed set* of the conjugation action — which is exactly what "union of orbits" means.

**Theorem routing.** No named theorem is required; the route is a chain of definitional equivalences. Normality $gNg^{-1} = N$ is first reduced to the one-sided containment $gNg^{-1} \subseteq N$ for all $g$ (an inverse-symmetry argument upgrades containment to equality). That containment, read pointwise, says every conjugate $gng^{-1}$ of every $n \in N$ stays in $N$ — i.e. each [[Def - Conjugacy Class|conjugacy class]] $\operatorname{ccl}_G(n)$ lies inside $N$. Because the classes partition $G$, "every class meeting $N$ lies inside $N$" is identical to "$N$ is a union of classes". Each arrow is forced; the work is making each translation airtight.

**Key decision point.** Two small but genuine subtleties carry the proof. The first is the upgrade from containment to equality: knowing $gNg^{-1} \subseteq N$ for *all* $g$ — including $g^{-1}$ — lets you sandwich $N$ between $gNg^{-1}$ and itself, giving equality without ever proving the reverse inclusion directly. The second is the realisation that "$N$ is a union of conjugacy classes" is not an extra structural demand but *literally a rephrasing* of "$N$ is closed under conjugation": orbits partition, so a subset is a union of orbits exactly when it is orbit-saturated. Seeing that these two descriptions have the same meaning is the whole insight.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory II — §1.3–1.4#Legal Operations|the topic page's Legal Operations]]:

1. **Act on the group itself by conjugation** (operation 5). The conjugation action of $G$ on itself is the frame for the entire argument: its orbits are the conjugacy classes, and "fixed set of the action" is the bridge concept.

2. **Conjugate to test or exploit normality.** The defining condition of normality, $gNg^{-1} = N$, is restated and then weakened to $gNg^{-1} \subseteq N$ for all $g$; conjugating elements of $N$ and tracking where they land is the mechanical core.

3. **Use that orbits partition the set.** Conjugacy classes partition $G$ — every element lies in exactly one. This is what makes "closed under conjugation" and "union of classes" the same statement, and it is invoked when assembling $N$ from the classes it contains.

---

# Hints

<details>
<summary>Hint 1</summary>

Stare at the definition of normality, $gNg^{-1} = N$ for all $g \in G$, and ask what action this is talking about. The set $gNg^{-1}$ is what you get by conjugating every element of $N$ by $g$. Normality is the statement that $N$ is *unchanged* by every conjugation — a fixed set of the conjugation action.

</details>

<details>
<summary>Hint 2</summary>

You do not need both inclusions $gNg^{-1} \subseteq N$ and $N \subseteq gNg^{-1}$ separately. Prove the single containment "$gng^{-1} \in N$ for all $g \in G$ and all $n \in N$", but prove it *for every $g$* — then apply it to $g^{-1}$ in place of $g$ to recover the reverse inclusion for free.

</details>

<details>
<summary>Hint 3</summary>

The conjugacy classes [[Def - Conjugacy Class|partition]] $G$. So a subset $N$ is a *union of conjugacy classes* if and only if it contains, with each of its elements $n$, the whole class $\operatorname{ccl}_G(n)$. And $\operatorname{ccl}_G(n) \subseteq N$ says exactly that every conjugate $gng^{-1}$ of $n$ lies in $N$ — which is the containment from Hint 2. The two sides of the biconditional are the same condition stated twice.

</details>

---

# Solution

The proof runs both directions through one pivot condition:
$$(\star) \qquad gng^{-1} \in N \quad \text{for every } g \in G \text{ and every } n \in N.$$
We show $N \trianglelefteq G \iff (\star) \iff N$ is a union of conjugacy classes.

**Step 1: Normality is equivalent to the one-sided condition $(\star)$.**

$N \trianglelefteq G$ means $gNg^{-1} = N$ for all $g$. This is equivalent to the weaker-looking containment $gNg^{-1} \subseteq N$ for all $g$ — i.e. to $(\star)$ — because applying the containment to $g^{-1}$ supplies the reverse inclusion.

<details>
<summary>Derivation</summary>

By the [[Def - Normal Subgroup|definition of normality]], $N \trianglelefteq G$ means $gNg^{-1} = N$ for every $g \in G$. Equality certainly implies the containment $gNg^{-1} \subseteq N$ for every $g$, and unwinding the set $gNg^{-1} = \{gng^{-1} : n \in N\}$, that containment is precisely the pointwise statement $(\star)$: every conjugate $gng^{-1}$ lands in $N$.

For the converse, suppose $(\star)$ holds, i.e. $gNg^{-1} \subseteq N$ for all $g \in G$. We must recover $gNg^{-1} = N$. Fix $g$. We already have $gNg^{-1} \subseteq N$. For the reverse inclusion, apply $(\star)$ to the element $g^{-1}$ (it too is an element of $G$, so $(\star)$ applies):
$$g^{-1} N g \subseteq N.$$
Conjugate both sides by $g$ — that is, apply the bijection $x \mapsto gxg^{-1}$, which preserves containments:
$$g(g^{-1} N g)g^{-1} \subseteq gNg^{-1}, \qquad \text{i.e.} \qquad N \subseteq gNg^{-1}.$$
Combining $gNg^{-1} \subseteq N$ and $N \subseteq gNg^{-1}$ gives $gNg^{-1} = N$. Since $g$ was arbitrary, $N \trianglelefteq G$.

So $N \trianglelefteq G$ if and only if $(\star)$ holds.

</details>

**Step 2: $(\star)$ is equivalent to "$N$ contains the conjugacy class of each of its elements".**

The condition $(\star)$ — every conjugate of every $n \in N$ lies in $N$ — says exactly that $\operatorname{ccl}_G(n) \subseteq N$ for every $n \in N$.

<details>
<summary>Derivation</summary>

The [[Def - Conjugacy Class|conjugacy class]] of $n$ is by definition the set of all its conjugates,
$$\operatorname{ccl}_G(n) = \{gng^{-1} : g \in G\}.$$
The statement "$\operatorname{ccl}_G(n) \subseteq N$" therefore means: for every $g \in G$, the conjugate $gng^{-1}$ lies in $N$. Quantifying this over all $n \in N$ gives exactly the condition $(\star)$: for all $g \in G$ and all $n \in N$, $gng^{-1} \in N$.

So $(\star)$ holds $\iff$ for every $n \in N$, $\operatorname{ccl}_G(n) \subseteq N$.

</details>

**Step 3: "$N$ contains the class of each of its elements" is equivalent to "$N$ is a union of conjugacy classes".**

Because the conjugacy classes partition $G$, a subset $N$ is a union of classes precisely when it is conjugation-saturated — when it contains the full class of every element it contains.

<details>
<summary>Derivation</summary>

Conjugacy classes are the orbits of the conjugation action, and orbits **partition** $G$: every element of $G$ lies in exactly one conjugacy class, and distinct classes are disjoint.

($\Rightarrow$) Suppose $N$ contains the conjugacy class of each of its elements. Then
$$N = \bigcup_{n \in N} \{n\} \subseteq \bigcup_{n \in N} \operatorname{ccl}_G(n) \subseteq N,$$
where the first inclusion holds because $n \in \operatorname{ccl}_G(n)$ (take $g = e$), and the second is the hypothesis. Hence $N = \bigcup_{n \in N} \operatorname{ccl}_G(n)$, exhibiting $N$ as a union of conjugacy classes.

($\Leftarrow$) Suppose $N = \bigcup_{i} C_i$ is a union of conjugacy classes $C_i$. Take any $n \in N$. Then $n$ lies in some $C_i$. But $n$ lies in exactly one conjugacy class — namely $\operatorname{ccl}_G(n)$ — so $C_i = \operatorname{ccl}_G(n)$. Hence $\operatorname{ccl}_G(n) = C_i \subseteq N$. So $N$ contains the class of each of its elements.

The two conditions are therefore equivalent. (The role of the partition property is the disjointness used in $(\Leftarrow)$: it is what forces the class $C_i$ containing $n$ to be *the* class $\operatorname{ccl}_G(n)$.)

</details>

**Step 4: Assemble the chain.**

Chaining Steps 1–3: $N \trianglelefteq G \iff (\star) \iff \operatorname{ccl}_G(n) \subseteq N$ for all $n \in N \iff N$ is a union of conjugacy classes. $\blacksquare$

<details>
<summary><strong>Complete formal solution</strong></summary>

Let $N \leq G$ be a subgroup. We prove the biconditional via the intermediate condition
$$(\star) \qquad gng^{-1} \in N \quad \text{for all } g \in G,\ n \in N.$$

**$N \trianglelefteq G \iff (\star)$.** By [[Def - Normal Subgroup|definition]], $N \trianglelefteq G$ means $gNg^{-1} = N$ for all $g \in G$, which gives $gNg^{-1} \subseteq N$ — exactly $(\star)$. Conversely, assume $(\star)$, i.e. $gNg^{-1} \subseteq N$ for all $g \in G$. Fix $g$; applying the hypothesis to $g^{-1}$ gives $g^{-1}Ng \subseteq N$, and conjugating by $g$ (an inclusion-preserving bijection) yields $N \subseteq gNg^{-1}$. With $gNg^{-1} \subseteq N$ this gives $gNg^{-1} = N$ for all $g$, so $N \trianglelefteq G$.

**$(\star) \iff \operatorname{ccl}_G(n) \subseteq N$ for all $n \in N$.** The [[Def - Conjugacy Class|conjugacy class]] is $\operatorname{ccl}_G(n) = \{gng^{-1} : g \in G\}$, so $\operatorname{ccl}_G(n) \subseteq N$ means $gng^{-1} \in N$ for all $g \in G$. Quantifying over $n \in N$ gives exactly $(\star)$.

**$\operatorname{ccl}_G(n) \subseteq N$ for all $n \in N \iff N$ is a union of conjugacy classes.** Conjugacy classes partition $G$. If $N$ contains the class of each of its elements, then $N = \bigcup_{n \in N}\{n\} \subseteq \bigcup_{n \in N}\operatorname{ccl}_G(n) \subseteq N$, so $N = \bigcup_{n\in N}\operatorname{ccl}_G(n)$ is a union of classes. Conversely, if $N = \bigcup_i C_i$ with each $C_i$ a conjugacy class, then any $n \in N$ lies in some $C_i$; since $n$ lies in a unique class, $C_i = \operatorname{ccl}_G(n)$, so $\operatorname{ccl}_G(n) \subseteq N$.

Chaining the three equivalences: $N \trianglelefteq G$ if and only if $N$ is a union of conjugacy classes of $G$. $\blacksquare$

</details>

---

# Key Takeaways

**Normality means "fixed by conjugation" — read the definition as a statement about an action.** The definitional condition $gNg^{-1} = N$ looks like a piece of algebraic bookkeeping, but the productive way to hear it is dynamic: $G$ acts on its own subsets by conjugation, and $N$ being normal says $N$ is a *fixed point of that action* — every conjugation maps $N$ onto itself. This reframing is the single most useful move in §1.4. It is why conjugacy classes, the orbits of conjugation, are the natural currency for normality: a fixed *set* of an action is always a union of *orbits*. Whenever a problem involves a normal subgroup, you should immediately translate "normal" into "conjugation-invariant" and bring the conjugation action and its orbits into play. The same translation turns the [[Def - Centraliser and Centre|centre]] into the fixed points of the action on *elements*, and the [[Def - Normaliser|normaliser]] into the stabiliser of a subgroup — the whole vocabulary of §1.4 is the conjugation action seen from different angles.

**To upgrade a one-sided containment to equality, feed the hypothesis its own inverse.** A recurring micro-technique in group theory: you want $gNg^{-1} = N$ but it is cleaner to prove only $gNg^{-1} \subseteq N$. The trick is to prove that containment *for every $g$ in the group at once*, and then instantiate it at $g^{-1}$ to obtain the reverse inclusion at no extra cost — $g^{-1}Ng \subseteq N$ conjugates up to $N \subseteq gNg^{-1}$. The pattern works because the group is closed under inverses, so a universally quantified one-sided statement secretly contains its own mirror image. This is exactly why the standard normality test is often stated as the *containment* $gNg^{-1} \subseteq N$ rather than equality: the two are the same for subgroups, and the containment is less to verify. Recognise the pattern "prove $\subseteq$ for all $g$, then apply at $g^{-1}$" — it recurs in the definition of the normaliser, in showing stabilisers of points in one orbit are conjugate, and throughout subgroup theory.

**This equivalence is the engine of every conjugacy-counting (non-)simplicity proof — internalise it as a reduction.** The real payoff of the theorem is that it converts the structural question "does $G$ have a proper non-trivial normal subgroup?" into the purely *arithmetic* question "can the conjugacy class sizes, one of which is the $1$ from $\{e\}$, be added up to a proper divisor of $|G|$?" Since a normal subgroup is a subgroup, its order divides $|G|$ ([[Thm - Lagrange's Theorem|Lagrange]]); and since it is a union of classes containing $\{e\}$, its order is a sum of class sizes including the term $1$. So checking [[Def - Simple Group|simplicity]] becomes: list the class sizes and test whether any sub-collection containing the $1$ sums to a proper divisor of the group order. For $A_5$ the class sizes are $1, 12, 12, 15, 20$, and no sub-sum containing the $1$ — other than $1 + 12 + 12 + 15 + 20 = 60$ itself — divides $60$, so $A_5$ is simple. Run the same arithmetic and *find* such a sub-collection, and you have proved a group is *not* simple, which is how groups of many specific orders are handled in [[Group Theory III — §1.5–1.7]]. The trigger is any simplicity question: this exercise is the licence to stop thinking about subgroups and start thinking about partitions of the integer $|G|$ into class sizes.

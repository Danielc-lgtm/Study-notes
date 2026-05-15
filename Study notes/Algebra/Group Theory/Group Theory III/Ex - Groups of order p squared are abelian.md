---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - p-group"
  - "Def - Abelian Group"
  - "Def - Centraliser and Centre"
  - "Thm - p-Groups Have Non-Trivial Centre"
  - "Thm - Quotient by the Centre and Commutativity"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $p$ be a prime number and let $G$ be a group of order $p^2$. Prove that $G$ is **abelian**.

**Recall:**

Three objects are in play: the order of a group, the centre, and the quotient by the centre.

A [[Def - p-group|$p$-group]] is a finite group whose order is a power $p^n$ of a prime, with $n \geq 1$. A group of order $p^2$ is the case $n = 2$, the smallest $p$-group order that is not prime.

A group $G$ is [[Def - Abelian Group|abelian]] when $xy = yx$ for every pair of elements $x, y \in G$ — the multiplication does not depend on the order of the factors.

![[Def - Centraliser and Centre#The Definition]]

The centre $Z(G)$ is itself a subgroup, and it is always normal, so the quotient group $G/Z(G)$ is defined. We will need two facts about it. First, by [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]], a non-trivial finite [[Def - p-group|$p$-group]] has $Z(G) \neq \{e\}$ — its centre contains more than just the identity. Second:

![[Thm - Quotient by the Centre and Commutativity#Statement]]

Finally, [[Thm - Lagrange's Theorem|Lagrange's theorem]] states that the order of any subgroup of a finite group $G$ divides $|G|$; in particular $|Z(G)|$ must divide $p^2$.

---

# Convergent Strategy

**Problem class.** This is a *prove a group is abelian from its order alone* problem, the §1.5 archetype. As the [[Group Theory III — §1.5–1.7#Problem-Solving Strategy|problem-solving strategy]] of the topic page records, every structural fact about [[Def - p-group|$p$-groups]] is extracted from one source — the centre is non-trivial — and the input here is nothing but the integer $p^2$. The whole content of the problem is the conversion of that arithmetic into commutativity.

**Assumption pattern.** The single hypothesis is $|G| = p^2$: an order that is a prime *squared*. Two features of this number do the work. It is a prime power, which triggers [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]] and forces $Z(G) \neq \{e\}$. And it has exactly three divisors — $1$, $p$, $p^2$ — which means [[Thm - Lagrange's Theorem|Lagrange]] confines $|Z(G)|$ to a list of only three values, one of which is immediately excluded. A short list of candidate orders is a rigid object, and rigidity is what makes the argument go through.

**Theorem routing.** The route is a two-theorem pincer. [[Thm - p-Groups Have Non-Trivial Centre|The non-trivial centre theorem]] supplies $|Z(G)| \in \{p, p^2\}$ (Lagrange gives the three divisors; non-triviality deletes $1$). [[Thm - Quotient by the Centre and Commutativity|The quotient-by-the-centre theorem]] then closes the door on $|Z(G)| = p$: that value would make $G/Z(G)$ a group of order $p$, hence cyclic, hence — by the theorem — would force $G$ abelian and $Z(G) = G$, contradicting $|Z(G)| = p < p^2$. Only $|Z(G)| = p^2$ survives, and $|Z(G)| = |G|$ says $Z(G) = G$, which *is* the statement that $G$ is abelian.

**Key decision point.** The non-obvious move is to attack the *middle* candidate by contradiction rather than to attack abelian-ness directly. One does not produce a commuting pair of elements by hand; instead one observes that the centre cannot have order $p$, because an index-$p$ centre would make the quotient cyclic, and a cyclic quotient by the centre is self-defeating — it forces the centre to have been everything all along. The cleverness is recognising that "$G/Z(G)$ is cyclic" is not a neutral fact but a *trap*: any group that lands in it collapses to abelian, and an abelian group's centre is the whole group. The candidate $|Z(G)| = p$ asserts a proper centre while simultaneously implying a total one, so it destroys itself.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory III — §1.5–1.7#Legal Operations|the topic page's Legal Operations]]:

1. **Apply the class equation** (operation 5), in packaged form. The work of reading the [[Thm - The Class Equation|class equation]] modulo $p$ is already done and bottled as [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]]. We invoke that theorem directly to obtain $Z(G) \neq \{e\}$ — the one fact from which everything else in the problem follows.

2. **Constrain a subgroup order by Lagrange.** Since $Z(G) \leq G$, [[Thm - Lagrange's Theorem|Lagrange's theorem]] forces $|Z(G)| \mid p^2$, so $|Z(G)| \in \{1, p, p^2\}$. This is the analogue, for the centre, of operation 1 ("factor the order and write down the constraints"): we factor $p^2$ and list every order the centre is permitted to have.

3. **Pass to the quotient by a central subgroup** (operation 6, the structural half). Rather than quotient by a single central element and induct, we quotient by the whole centre $Z(G)$ and read off the order $|G/Z(G)| = |G|/|Z(G)|$, then feed that quotient into [[Thm - Quotient by the Centre and Commutativity|the quotient-by-the-centre theorem]]. The trigger is the appearance of $Z(G)$ together with a need to convert information about its index into information about $G$ itself.

---

# Hints

> [!note]- Hint 1
> The hypothesis is a prime power, so the first thing to write down is what every [[Def - p-group|$p$-group]] problem starts with: the centre is non-trivial. Then ask what [[Thm - Lagrange's Theorem|Lagrange's theorem]] permits the *order* of that centre to be.

> [!note]- Hint 2
> Lagrange and non-triviality together leave only two possibilities, $|Z(G)| = p$ or $|Z(G)| = p^2$. The case $|Z(G)| = p^2$ is the conclusion you want, so it needs no work. Spend all your effort ruling out $|Z(G)| = p$.

> [!note]- Hint 3
> If $|Z(G)| = p$ then $G/Z(G)$ has order $p^2/p = p$, so it is cyclic — every group of prime order is. Now apply [[Thm - Quotient by the Centre and Commutativity|the quotient-by-the-centre theorem]]: a cyclic $G/Z(G)$ makes $G$ abelian, and an abelian group is its own centre. That says $Z(G) = G$, so $|Z(G)| = p^2$ — flatly contradicting the assumption $|Z(G)| = p$.

---

# Solution

The strategy is to pin the order of the centre. [[Thm - Lagrange's Theorem|Lagrange]] allows three values and [[Thm - p-Groups Have Non-Trivial Centre|non-triviality]] deletes one; the third is excluded because it would make $G/Z(G)$ cyclic, which is self-contradictory. What remains is $Z(G) = G$.

**Step 1: The centre is non-trivial, so $|Z(G)| \in \{p, p^2\}$.**

$G$ is a $p$-group, so $Z(G) \neq \{e\}$. By [[Thm - Lagrange's Theorem|Lagrange]] the order $|Z(G)|$ divides $p^2$, hence lies in $\{1, p, p^2\}$; non-triviality removes $1$.

> [!note]- Derivation
> By definition $G$ has order $p^2 = p^2$, a prime power with exponent $2 \geq 1$, so $G$ is a [[Def - p-group|$p$-group]]. [[Thm - p-Groups Have Non-Trivial Centre|The non-trivial centre theorem]] states that every non-trivial finite $p$-group has a non-trivial [[Def - Centraliser and Centre|centre]]; since $|G| = p^2 > 1$, the group $G$ is non-trivial, and therefore
> $$Z(G) \neq \{e\}.$$
>
> The centre $Z(G)$ is a subgroup of $G$. [[Thm - Lagrange's Theorem|Lagrange's theorem]] says the order of any subgroup of a finite group divides the order of the group, so $|Z(G)|$ divides $|G| = p^2$. The positive divisors of $p^2$ are exactly $1$, $p$, and $p^2$ — these and no others, because $p$ is prime. Hence
> $$|Z(G)| \in \{1,\ p,\ p^2\}.$$
> The value $1$ corresponds to $Z(G) = \{e\}$, which Step 1's first sentence has excluded. Therefore $|Z(G)| \in \{p,\ p^2\}$.

**Step 2: The case $|Z(G)| = p$ is impossible.**

If the centre had order $p$, the quotient $G/Z(G)$ would have order $p$, hence be cyclic; but a cyclic $G/Z(G)$ forces $G$ abelian and thus $Z(G) = G$ — contradicting $|Z(G)| = p < p^2$.

> [!note]- Derivation
> Suppose, for contradiction, that $|Z(G)| = p$. The centre is a normal subgroup, so the [[Def - Quotient Group|quotient group]] $G/Z(G)$ exists, and by the counting form of [[Thm - Lagrange's Theorem|Lagrange's theorem]] its order is
> $$|G/Z(G)| = \frac{|G|}{|Z(G)|} = \frac{p^2}{p} = p.$$
>
> A group of prime order $p$ is cyclic: pick any non-identity element $g$; its order divides $p$ by Lagrange and is not $1$, so it is $p$, and the $p$ powers $e, g, g^2, \dots, g^{p-1}$ already exhaust the group. Hence $G/Z(G)$ is **cyclic**.
>
> Now invoke [[Thm - Quotient by the Centre and Commutativity|the quotient-by-the-centre theorem]]: *if $G/Z(G)$ is cyclic then $G$ is abelian*. So $G$ is abelian. But the [[Def - Centraliser and Centre|centre]] of an abelian group is the whole group — every element commutes with every other, so every element is central — giving
> $$Z(G) = G, \qquad \text{hence} \qquad |Z(G)| = |G| = p^2.$$
> This contradicts the assumption $|Z(G)| = p$, because $p \neq p^2$ (indeed $p < p^2$ as $p \geq 2$). The assumption is therefore untenable: $|Z(G)| \neq p$.

**Step 3: Conclude $Z(G) = G$, so $G$ is abelian.**

Steps 1 and 2 leave only $|Z(G)| = p^2$. Then $|Z(G)| = |G|$ with $Z(G) \leq G$ forces $Z(G) = G$, and $G$ equal to its own centre is precisely the statement that $G$ is abelian.

> [!note]- Derivation
> By Step 1, $|Z(G)| \in \{p, p^2\}$; by Step 2, $|Z(G)| \neq p$. The only remaining possibility is
> $$|Z(G)| = p^2 = |G|.$$
> A subgroup of a finite group whose order equals the order of the whole group must be the whole group — it is a subset of the same finite cardinality. Hence $Z(G) = G$.
>
> Unwinding the definition of the [[Def - Centraliser and Centre|centre]], $Z(G) = G$ says that *every* element of $G$ commutes with *every* element of $G$: for all $x, y \in G$, $xy = yx$. That is the definition of an [[Def - Abelian Group|abelian]] group. Therefore $G$ is abelian. $\blacksquare$

> [!note]- Complete formal solution
> Let $p$ be prime and $|G| = p^2$.
>
> Since $|G| = p^2$ is a prime power, $G$ is a [[Def - p-group|$p$-group]], and as $|G| > 1$ it is non-trivial. By [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]], $Z(G) \neq \{e\}$.
>
> The centre $Z(G)$ is a subgroup of $G$, so by [[Thm - Lagrange's Theorem|Lagrange's theorem]] its order divides $|G| = p^2$. The divisors of $p^2$ are $1, p, p^2$, and $Z(G) \neq \{e\}$ rules out $1$. Hence
> $$|Z(G)| \in \{p,\ p^2\}.$$
>
> Suppose $|Z(G)| = p$. The centre is normal, so $G/Z(G)$ is a group, of order
> $$|G/Z(G)| = |G|/|Z(G)| = p^2/p = p.$$
> Every group of prime order is cyclic, so $G/Z(G)$ is cyclic. By [[Thm - Quotient by the Centre and Commutativity|the quotient-by-the-centre theorem]], a cyclic $G/Z(G)$ implies $G$ is abelian. But then every element of $G$ is central, so $Z(G) = G$ and $|Z(G)| = p^2$, contradicting $|Z(G)| = p$. Hence $|Z(G)| \neq p$.
>
> Therefore $|Z(G)| = p^2 = |G|$. Since $Z(G) \leq G$ and the two have equal finite order, $Z(G) = G$. By definition of the [[Def - Centraliser and Centre|centre]], $Z(G) = G$ means every pair of elements of $G$ commutes, i.e. $G$ is [[Def - Abelian Group|abelian]]. $\blacksquare$

---

# Key Takeaways

**To prove a $p$-group is abelian, do not exhibit commuting elements — squeeze the order of the centre.** Commutativity looks like a statement about *pairs* of elements, and the naive instinct is to take an arbitrary $x, y$ and show $xy = yx$. That instinct is almost never the right one for [[Def - p-group|$p$-groups]], because there is no handle on a general pair. The reusable move is to recast "abelian" as the single equation $Z(G) = G$, and then prove that equation by *trapping the integer $|Z(G)|$*: [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]] supplies a lower bound (the centre is not trivial), [[Thm - Lagrange's Theorem|Lagrange]] supplies a short candidate list (the centre's order divides $|G|$), and a structural obstruction deletes the middle candidates until only $|Z(G)| = |G|$ survives. The trigger for this whole manoeuvre is the phrase "prime power order" — whenever you must prove a $p$-group has some property, ask first whether the property is equivalent to a statement about $Z(G)$, because the centre is the only part of a $p$-group you get information about for free.

**A cyclic $G/Z(G)$ is a contradiction waiting to happen — never an admissible end state.** The decisive lever in this problem is [[Thm - Quotient by the Centre and Commutativity|the quotient-by-the-centre theorem]], and the right way to hold it in memory is not as a neutral implication but as a *self-destruct rule*: the moment $G/Z(G)$ is cyclic, $G$ becomes abelian, which makes $Z(G)$ the whole group, which makes $G/Z(G)$ *trivial*. So a non-trivial cyclic $G/Z(G)$ cannot exist. This converts the theorem into a powerful proof-by-contradiction engine. Any time an argument produces a quotient $G/Z(G)$ of prime order — or, more generally, any cyclic $G/Z(G)$ — you have reached a contradiction, because prime-order groups are automatically cyclic and a cyclic quotient by the centre is impossible unless it was trivial to begin with. The pattern recurs throughout $p$-group theory: it is why a group of order $p^2$ cannot have a centre of order exactly $p$, and the same reasoning shows a group of order $p^3$ cannot have a centre of index $p^2$.

**A prime power has very few divisors, and that scarcity is the engine.** The reason the order $p^2$ is so tractable is purely arithmetical: it has exactly three divisors, $1, p, p^2$. [[Thm - Lagrange's Theorem|Lagrange]] turns "the centre is a subgroup" into "the centre's order is one of these three numbers", a list short enough that knocking out two entries finishes the problem. This is a general lesson about why prime-power orders are the docile case of finite group theory: every subgroup order is forced into a tiny totally-ordered ladder $1 \mid p \mid p^2 \mid \cdots \mid p^n$, with no branching and no surprises. Whenever the order in front of you is $p^n$, count the divisors first — there are only $n+1$ of them — and expect the proof to proceed by eliminating candidates from that short ladder one at a time. The same divisor-counting opens the proof that a $p$-group has a [[Thm - Subgroups of a p-Group|subgroup of every order]] $p^b$ and underlies the entire inductive structure of §1.5.

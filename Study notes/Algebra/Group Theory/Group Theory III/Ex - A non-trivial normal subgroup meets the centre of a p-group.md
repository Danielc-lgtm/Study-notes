---
type: exercise
subject: group-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - p-group"
  - "Def - Normal Subgroup"
  - "Def - Centraliser and Centre"
  - "Def - Group Action"
  - "Def - Conjugacy Class"
  - "Thm - Orbit-Stabiliser Theorem"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be a finite [[Def - p-group|$p$-group]] and let $N \trianglelefteq G$ be a normal subgroup with $N \neq \{e\}$. Prove that
$$N \cap Z(G) \neq \{e\},$$
that is, $N$ contains a non-identity element of the centre of $G$.

**Recall:**

The objects in play are a $p$-group, a normal subgroup, the centre, and the action of a group on a set by conjugation.

A [[Def - p-group|$p$-group]] is a finite group of order $p^n$ for a prime $p$ and $n \geq 1$. By [[Thm - Lagrange's Theorem|Lagrange's theorem]] every subgroup of $G$ has order a power of $p$, so in particular $|N|$ is a power of $p$; since $N \neq \{e\}$ this power is at least $p^1$, and therefore $p \mid |N|$.

![[Def - Normal Subgroup#The Definition]]

The point of normality here is closure under conjugation: $gng^{-1} \in N$ for every $g \in G$ and every $n \in N$. This is what lets $G$ act on the *set* $N$.

![[Def - Centraliser and Centre#The Definition]]

A group [[Def - Group Action|acts]] on a set $X$ when each $g \in G$ permutes $X$ compatibly with multiplication; the **orbit** of $x \in X$ is $\{g \ast x : g \in G\}$ and the **stabiliser** is $\{g \in G : g \ast x = x\}$. Orbits partition $X$. The [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] states that for a finite group, $|\text{orbit of } x| = |G|/|\text{stabiliser of } x|$; in particular every orbit size divides $|G|$.

---

# Convergent Strategy

**Problem class.** This is a *fixed-point counting* problem dressed as a statement about subgroups. The [[Group Theory III — §1.5–1.7#Insights|topic page]] isolates the principle that powers it — the **fixed-point congruence**: a [[Def - p-group|$p$-group]] acting on a finite set $X$ has $|X^G| \equiv |X| \pmod p$, where $X^G$ is the set of fixed points. This exercise is exactly that congruence, applied to a cleverly chosen $X$. It is the same engine that drives [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]] — indeed this exercise *generalises* that theorem, which is the case $N = G$.

**Assumption pattern.** Two hypotheses combine. First, $G$ is a $p$-group, so every orbit of any $G$-action has size a power of $p$ — hence size $1$ or a multiple of $p$, with no middle ground. Second, $N$ is *normal*, which is precisely the condition that makes conjugation by $G$ map $N$ into itself: without normality there would be no action of $G$ on the set $N$ to speak of. The hypothesis $N \neq \{e\}$ contributes the arithmetic fact $p \mid |N|$, the seed of the counting argument.

**Theorem routing.** The route is: let $G$ act on the set $N$ by conjugation (well-defined by normality); apply the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] to learn that every orbit has size $1$ or a multiple of $p$; identify the size-$1$ orbits as exactly the points of $N \cap Z(G)$; then use that the orbits *partition* $N$ to write $|N|$ as (number of fixed points) plus (a sum of multiples of $p$). Since [[Thm - Lagrange's Theorem|Lagrange]] gives $p \mid |N|$, the number of fixed points is $\equiv 0 \pmod p$. As $e$ is one fixed point, there must be at least $p$ of them.

**Key decision point.** The non-obvious choice is *what set to act on*. The temptation is to act $G$ on itself — that proves only the non-trivial centre theorem. The insight is to act $G$ on the subset $N$ instead: this is legitimate only because $N$ is normal, and it is exactly this restriction of the conjugation action that makes the fixed points land inside $N$. A second subtlety, easy to get wrong, is the precise identification of the fixed points. The orbit of $x \in N$ has size $1$ when $gxg^{-1} = x$ for *every* $g \in G$ — note: for every $g$ in the whole group $G$, not merely every $g \in N$ — which says $x$ commutes with all of $G$, i.e. $x \in Z(G)$; and $x$ was already in $N$. So the fixed-point set is $N \cap Z(G)$, not $Z(N)$. Confusing $Z(N)$ with $N \cap Z(G)$ collapses the whole argument.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory III — §1.5–1.7#Legal Operations|the topic page's Legal Operations]]:

1. **Apply the class equation** (operation 5), in its underlying form. We do not quote the [[Thm - The Class Equation|class equation]] for $G$ verbatim; instead we run the argument *behind* it — orbits of a conjugation action, sizes divisible by $p$, fixed points counted modulo $p$ — but on the set $N$ rather than on $G$. The class equation is the special case $N = G$; this is the same lever, repositioned.

2. **Choose a set and act on it, then apply orbit–stabiliser.** This is the master operation of the whole topic (the [[Group Theory III — §1.5–1.7#Insights|topic page]] notes that all of Sylow theory is this move applied three times). Here the chosen set is $N$ and the action is conjugation by $G$; the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] then forces every orbit size to divide $|G| = p^n$, hence to be $1$ or a multiple of $p$.

3. **Constrain an order by Lagrange.** Since $N \leq G$ is a non-trivial subgroup of a $p$-group, [[Thm - Lagrange's Theorem|Lagrange's theorem]] gives $|N| = p^k$ with $k \geq 1$, so $p \mid |N|$. This single divisibility fact is what turns "the fixed-point count is $\equiv |N| \pmod p$" into "the fixed-point count is $\equiv 0 \pmod p$".

4. **Partition the set into orbits and count modulo $p$.** The orbits of any group action are disjoint and exhaustive, so $|N|$ is the sum of the orbit sizes. Splitting that sum into size-$1$ orbits and larger orbits, and reading it modulo $p$, isolates the number of fixed points — exactly as the [[Thm - The Class Equation|class equation]] isolates $|Z(G)|$.

---

# Hints

<details>
<summary>Hint 1</summary>

You want to find a central element inside $N$. Central elements are the ones fixed by conjugation, so think about the conjugation action — but act on the *right set*. Acting $G$ on all of $G$ only reproves [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]]. What does the normality of $N$ allow $G$ to act on instead?

</details>

<details>
<summary>Hint 2</summary>

Because $N$ is normal, conjugation $n \mapsto gng^{-1}$ sends $N$ into $N$, so $G$ acts on the *set* $N$ by conjugation. Apply the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]]: since $|G|$ is a power of $p$, every orbit has size $1$ or a size divisible by $p$. Now ask: which elements $x \in N$ have an orbit of size exactly $1$?

</details>

<details>
<summary>Hint 3</summary>

An element $x \in N$ has a size-$1$ orbit precisely when $gxg^{-1} = x$ for **every** $g \in G$ — that is, when $x$ commutes with all of $G$, so $x \in Z(G)$. Hence the fixed-point set of the action is exactly $N \cap Z(G)$. The orbits partition $N$, so
$$|N| = |N \cap Z(G)| + (\text{sum of orbit sizes} > 1).$$

</details>

<details>
<summary>Hint 4</summary>

Every orbit of size greater than $1$ has size divisible by $p$, so the parenthesised sum is $\equiv 0 \pmod p$. And $p \mid |N|$, since $N$ is a non-trivial subgroup of a $p$-group ([[Thm - Lagrange's Theorem|Lagrange]]). Reading the displayed equation modulo $p$ gives $|N \cap Z(G)| \equiv 0 \pmod p$. The identity $e$ lies in $N \cap Z(G)$, so this set is non-empty and its size is a multiple of $p \geq 2$ — hence at least $p$, so it contains something other than $e$.

</details>

---

# Solution

The strategy is to let $G$ act on the *set* $N$ by conjugation — legitimate because $N$ is normal — and count fixed points modulo $p$. The fixed points are exactly $N \cap Z(G)$, and a $p$-group action makes their number $\equiv |N| \equiv 0 \pmod p$.

**Step 1: $G$ acts on the set $N$ by conjugation.**

Because $N$ is normal, the rule $g \ast n = gng^{-1}$ sends elements of $N$ to elements of $N$, and it satisfies the group-action axioms. So $G$ acts on the set $N$.

<details>
<summary>Derivation</summary>

Define $\ast : G \times N \to N$ by $g \ast n = gng^{-1}$. The first thing to check is that the output really lands in $N$: this is exactly the content of $N \trianglelefteq G$. By the definition of a [[Def - Normal Subgroup|normal subgroup]], $gng^{-1} \in N$ for every $g \in G$ and every $n \in N$, so $\ast$ is a well-defined function into $N$. (Normality is not optional here — for a non-normal subgroup, conjugation would push elements *out* of the subset, and there would be no action on $N$ at all.)

The [[Def - Group Action|group action]] axioms hold because conjugation is an action of $G$ on the whole of $G$ and we have merely restricted its domain to the invariant subset $N$:
$$e \ast n = ene^{-1} = n, \qquad g \ast (h \ast n) = g(hnh^{-1})g^{-1} = (gh)n(gh)^{-1} = (gh) \ast n.$$
So $\ast$ is a genuine action of $G$ on the set $N$. The orbits of this action are the **$G$-conjugacy classes that lie inside $N$**, and they partition $N$.

</details>

**Step 2: Every orbit has size $1$ or a multiple of $p$.**

By the orbit–stabiliser theorem each orbit size divides $|G| = p^n$, so it is a power of $p$ — hence either $1$ or divisible by $p$.

<details>
<summary>Derivation</summary>

Fix $x \in N$ and let $\mathcal{O}_x$ be its orbit under the action of Step 1. The [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] states that, for a finite group $G$,
$$|\mathcal{O}_x| = \frac{|G|}{|G_x|},$$
where $G_x = \{g \in G : g \ast x = x\}$ is the stabiliser. In particular $|\mathcal{O}_x|$ divides $|G|$.

Since $G$ is a [[Def - p-group|$p$-group]], $|G| = p^n$. The divisors of $p^n$ are exactly $1, p, p^2, \dots, p^n$. So every orbit size is one of these. An orbit size therefore falls into exactly one of two cases: it equals $1$ (the divisor $p^0$), or it is one of $p, p^2, \dots, p^n$, every one of which is divisible by $p$. There is no third possibility — this dichotomy is the whole reason a $p$-group hypothesis is so powerful in counting arguments.

</details>

**Step 3: The size-$1$ orbits are exactly the elements of $N \cap Z(G)$.**

An element $x \in N$ has an orbit of size $1$ if and only if $gxg^{-1} = x$ for all $g \in G$, i.e. $x \in Z(G)$. So the fixed-point set is $N \cap Z(G)$.

<details>
<summary>Derivation</summary>

The orbit $\mathcal{O}_x$ has size $1$ exactly when $x$ is its only member, that is, when $g \ast x = x$ for every $g \in G$. Spelling out the action,
$$\mathcal{O}_x = \{x\} \iff gxg^{-1} = x \text{ for all } g \in G \iff gx = xg \text{ for all } g \in G.$$
The right-hand condition says $x$ commutes with every element of $G$, which is the defining property of the [[Def - Centraliser and Centre|centre]]: $x \in Z(G)$.

Crucially, the quantifier ranges over *all* $g \in G$, not merely $g \in N$. So a fixed point is an element that is central in the **whole group $G$** — not merely central in $N$. An element $x$ with a size-$1$ orbit is therefore an element of $N$ (it was chosen there) that also lies in $Z(G)$. Hence the set of fixed points of the action is exactly
$$N^{G} = \{x \in N : \mathcal{O}_x = \{x\}\} = N \cap Z(G).$$
This is the step where the choice of $N$ as the acted-on set pays off: the fixed points are forced *into* $N$, because the set being acted on was $N$ in the first place. (Were one to confuse this with $Z(N)$, the elements central in $N$ alone, the argument would break — $Z(N)$ need not meet $Z(G)$ non-trivially, and is not what the count below produces.)

</details>

**Step 4: Count modulo $p$ — there are at least $p$ fixed points.**

The orbits partition $N$, so $|N| = |N \cap Z(G)| + (\text{multiples of } p)$. Since $p \mid |N|$, this forces $p \mid |N \cap Z(G)|$. As $e$ is a fixed point, $|N \cap Z(G)| \geq p > 1$.

<details>
<summary>Derivation</summary>

The orbits of a [[Def - Group Action|group action]] are pairwise disjoint and their union is the whole set, so they partition $N$. Summing their sizes recovers $|N|$. Separate the orbits into those of size $1$ and those of size greater than $1$. By Step 3 there are exactly $|N \cap Z(G)|$ orbits of size $1$, each contributing $1$ to the total. By Step 2 every orbit of size greater than $1$ has size divisible by $p$, so their sizes sum to some multiple of $p$, say $pK$. Therefore
$$|N| = |N \cap Z(G)| + pK.$$
Now read this modulo $p$. The term $pK$ vanishes, leaving
$$|N \cap Z(G)| \equiv |N| \pmod p.$$
Next, $N$ is a subgroup of the $p$-group $G$, so by [[Thm - Lagrange's Theorem|Lagrange's theorem]] $|N|$ divides $|G| = p^n$, making $|N|$ a power of $p$. The hypothesis $N \neq \{e\}$ rules out $|N| = p^0 = 1$, so $|N| = p^k$ with $k \geq 1$, and in particular $p \mid |N|$, i.e. $|N| \equiv 0 \pmod p$. Combining,
$$|N \cap Z(G)| \equiv 0 \pmod p.$$
Finally, $N \cap Z(G)$ is not empty: the identity $e$ lies in $N$ (it is a subgroup) and in $Z(G)$ (it commutes with everything), so $e \in N \cap Z(G)$ and $|N \cap Z(G)| \geq 1$. A positive integer that is divisible by $p$ is at least $p$. Since $p \geq 2$, we conclude
$$|N \cap Z(G)| \geq p > 1,$$
so $N \cap Z(G)$ contains an element other than $e$. Hence $N \cap Z(G) \neq \{e\}$. $\blacksquare$

</details>

<details>
<summary><strong>Complete formal solution</strong></summary>

Let $G$ be a finite $p$-group, $|G| = p^n$, and let $N \trianglelefteq G$ with $N \neq \{e\}$.

**The action.** Define $\ast : G \times N \to N$ by $g \ast n = gng^{-1}$. Since $N \trianglelefteq G$, the [[Def - Normal Subgroup|normality]] condition $gng^{-1} \in N$ makes this a well-defined function into $N$, and the identities $e \ast n = n$ and $g \ast (h \ast n) = (gh) \ast n$ hold because conjugation is an action of $G$ on $G$ restricted to the invariant subset $N$. So $G$ acts on the set $N$.

**Orbit sizes.** For $x \in N$ with orbit $\mathcal{O}_x$, the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] gives $|\mathcal{O}_x| = |G|/|G_x|$, so $|\mathcal{O}_x|$ divides $|G| = p^n$ and is thus a power of $p$. Every orbit therefore has size $1$ or a size divisible by $p$.

**Fixed points.** The orbit $\mathcal{O}_x$ has size $1$ iff $gxg^{-1} = x$ for all $g \in G$, i.e. iff $x$ commutes with every element of $G$, i.e. iff $x \in Z(G)$. Since $x \in N$, the set of size-$1$ orbits corresponds exactly to $N \cap Z(G)$.

**Counting modulo $p$.** The orbits partition $N$, so summing orbit sizes,
$$|N| = |N \cap Z(G)| + pK$$
for some integer $K \geq 0$ (the size-$1$ orbits contribute $|N \cap Z(G)|$; the larger orbits contribute a sum of multiples of $p$). Hence $|N \cap Z(G)| \equiv |N| \pmod p$.

By [[Thm - Lagrange's Theorem|Lagrange's theorem]], $|N|$ divides $|G| = p^n$, so $|N|$ is a power of $p$; as $N \neq \{e\}$, $|N| \neq 1$, so $p \mid |N|$. Therefore $|N \cap Z(G)| \equiv 0 \pmod p$.

Finally $e \in N \cap Z(G)$, so $|N \cap Z(G)| \geq 1$; being a positive multiple of $p \geq 2$, it is at least $p > 1$. Hence $N \cap Z(G)$ contains a non-identity element, and $N \cap Z(G) \neq \{e\}$. $\blacksquare$

</details>

---

# Key Takeaways

**When you must place a special element inside a given subset, act on that subset — not on the whole group.** The reflexive version of the centre argument acts $G$ on $G$ by conjugation and concludes $Z(G) \neq \{e\}$. But the target here is sharper: the central element must lie inside the prescribed $N$. The reusable insight is that *the conclusion of a fixed-point count is confined to whatever set you acted on* — the fixed points are a subset of $X$, so if you want them inside $N$, make $X = N$. The price of choosing $X = N$ is that the action must be well-defined on $N$, and this is exactly what the normality hypothesis buys you: conjugation preserves a subset precisely when that subset is normal. So the pattern is: identify the set the conclusion must live in, check that the natural action stabilises it (this is where a "normal" or "invariant" hypothesis gets consumed), and run the count there. This is the same logic by which Sylow's theorems act on cleverly restricted sets — subsets of a given size, cosets of a fixed subgroup — rather than on the group at large.

**The fixed-point congruence is one tool: a $p$-group acting on a finite set has $|X^G| \equiv |X| \pmod p$.** Strip away the specifics and every §1.5 counting argument is this single statement. A [[Def - p-group|$p$-group]] $G$ acting on a finite set $X$ has all orbit sizes equal to powers of $p$, so the non-singleton orbits contribute a multiple of $p$, and the partition identity gives $|X^G| \equiv |X| \pmod p$ where $X^G$ is the fixed-point set. [[Thm - p-Groups Have Non-Trivial Centre|The non-trivial centre theorem]] is this with $X = G$ under conjugation ($X^G = Z(G)$). This exercise is this with $X = N$ under conjugation ($X^G = N \cap Z(G)$). Sylow III is this with $X = \operatorname{Syl}_p(G)$. Once you recognise a problem as "a $p$-group acting on a finite set, and I care about the fixed points", the conclusion is automatic: count $|X| \bmod p$, and the number of fixed points matches it. The skill being drilled is *seeing the action* — naming the set $X$, the $p$-group, and the fixed-point set you actually want — after which the arithmetic writes itself.

**Distinguish "central in the subgroup" from "central in the ambient group" — the quantifier is everything.** The single most dangerous error in this problem is to identify the fixed points with $Z(N)$, the centre of $N$ as a group in its own right. They are not: a fixed point satisfies $gxg^{-1} = x$ for all $g \in \mathbf{G}$, the entire ambient group, whereas membership in $Z(N)$ would only require commuting with elements of $N$. The fixed-point set is $N \cap Z(G)$, the elements of $N$ that are central in *all* of $G$ — a much stronger and much smaller condition. Whenever an argument involves a conjugation action restricted to a subset, pause and read off precisely which elements the action's group ranges over: that quantifier determines whether you land in $Z(N)$, in $N \cap Z(G)$, or somewhere else, and getting it wrong silently invalidates the count. This vigilance about the scope of a "for all $g$" is a transferable discipline — the same care separates the normaliser $N_G(H)$ from the centraliser $C_G(H)$, and the stabiliser of a point from the stabiliser of a set.

**This result is the inductive workhorse behind $p$-group structure theory.** The statement "every non-trivial normal subgroup of a $p$-group meets the centre" is not a curiosity; it is the lemma that makes induction on $p$-groups actually run. When you quotient a $p$-group $G$ by a central $C_p$ and want to lift a normal subgroup back, or when you build a chain of normal subgroups $\{e\} = N_0 \trianglelefteq N_1 \trianglelefteq \cdots \trianglelefteq N_k = G$ with each quotient central in the next — the **upper central series**, which proves every $p$-group is *nilpotent* — this is the fact guaranteeing each step is non-trivial. The trigger to remember it is: any time you have a normal subgroup of a $p$-group and need a *central* element of it to seed an induction or a series, this exercise hands you one for free. It is the natural strengthening of [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]] from $G$ to every normal subgroup of $G$, and that strengthening is exactly what an inductive argument needs.

---
type: exercise
subject: ring-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Prime and Maximal Ideal"
  - "Def - Ideal"
  - "Def - Integral Domain"
  - "Thm - Maximal and Prime Ideals via Quotients"
tags: [algebra, ring-theory]
---

# Problem Statement

Let $R$ be a commutative ring and $P\trianglelefteq R$ an ideal with $P\neq R$. A subset $S\subseteq R$ is called **multiplicatively closed** if $1\in S$ and $S$ is closed under multiplication: $s,t\in S\Rightarrow st\in S$.

Prove that the following are equivalent:

1. $P$ is a **prime ideal** of $R$.
2. The complement $R\setminus P$ is **multiplicatively closed**.

In words: an ideal is prime precisely when its *complement* — the set of elements *outside* the ideal — is closed under multiplication and contains $1$.

**Recall:**

An [[Def - Ideal|ideal]] $P\trianglelefteq R$ of a commutative ring is an additive subgroup closed under multiplication by every element of $R$. The defining property of an ideal is a statement about the *inside*: an element of $P$ times anything stays in $P$.

A [[Def - Prime and Maximal Ideal|prime ideal]] is defined by the converse-flavoured condition:

![[Def - Prime and Maximal Ideal#The Definition]]

What matters for this exercise is the prime condition stated as a slogan: **a product lands in $P$ only if a factor already lies in $P$.** Symbolically, $ab\in P\Rightarrow(a\in P\ \text{or}\ b\in P)$, together with $P\neq R$.

A subset $S\subseteq R$ is **multiplicatively closed** (or a *multiplicative set*) if $1\in S$ and $st\in S$ whenever $s,t\in S$. Standard examples: the set of non-zero elements of an [[Def - Integral Domain|integral domain]]; the powers $\{1,f,f^2,\dots\}$ of a fixed element $f$; and — as this exercise shows — the complement of any prime ideal.

For orientation, the equivalent characterisation through the quotient: $P$ is prime iff $R/P$ is an [[Def - Integral Domain|integral domain]] (see [[Thm - Maximal and Prime Ideals via Quotients]]). This exercise gives a *third* face of the same notion, phrased entirely on the complement.

---

# Convergent Strategy

**Problem class.** This is a *prove an equivalence of two characterisations* problem: two conditions on the same object $P$ are claimed to be the same, and the task is to show each implies the other. As the [[Rings II — §2.3–2.4#Problem-Solving Strategy|topic page's strategy]] records, an "if and only if" between two definitions is attacked by *translating both into a common symbolic core and observing they are contrapositives of one another* — often the two directions are a single logical identity read forwards and backwards.

**Assumption pattern.** The defining condition of "prime" is an implication $ab\in P\Rightarrow a\in P\ \text{or}\ b\in P$. The condition "$R\setminus P$ multiplicatively closed" is also an implication: $a\notin P\ \text{and}\ b\notin P\Rightarrow ab\notin P$. The recognisable pattern is *two implications that look different but are negations of each other's pieces*. Whenever you see "property of being inside a set" versus "property of being outside it", suspect a **contrapositive**: $A\Rightarrow B$ is logically identical to $\neg B\Rightarrow\neg A$.

**Theorem routing.** No theorem is needed — the route is pure propositional logic. The prime condition is $P\neq R$ together with "$ab\in P\Rightarrow(a\in P\lor b\in P)$". The contrapositive of that implication is "$(a\notin P\land b\notin P)\Rightarrow ab\notin P$", which is *exactly* the multiplicative-closure condition on $R\setminus P$. The two named conditions are therefore the same statement; the only genuine content beyond the contrapositive is matching up the side-conditions: "$P\neq R$" must correspond to "$1\in R\setminus P$".

**Key decision point.** Two things require care, both about the *side-conditions* rather than the main implication. First, "$P\neq R$" and "$1\in R\setminus P$" must be seen to be equivalent — this uses the fact that an [[Ex - An ideal contains a unit exactly when it is the whole ring|ideal equals $R$ iff it contains $1$]]. Second, one must be careful that "$R\setminus P$ multiplicatively closed" *bundles* the requirement $1\in R\setminus P$ into the definition of multiplicative set, so the side-condition is not lost. The interesting conceptual payoff — flagged in the takeaways — is that this reformulation moves attention from the ideal to its complement, which is the doorway to **localisation**.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings II — §2.3–2.4#Legal Operations|the topic page's Legal Operations]]:

1. **Translate a membership condition into its contrapositive** (operation: *replace $A\Rightarrow B$ by the logically identical $\neg B\Rightarrow\neg A$*). The prime implication "$ab\in P\Rightarrow a\in P\lor b\in P$" is rewritten as "$a\notin P\land b\notin P\Rightarrow ab\notin P$".

2. **Convert "outside the ideal" into set-complement language** (operation: *$a\notin P\iff a\in R\setminus P$*). This is what turns the contrapositive into a closure statement about the set $R\setminus P$.

3. **Match the properness side-condition to a statement about the complement** (operation: *$P\neq R\iff 1\notin P\iff 1\in R\setminus P$*; uses [[Ex - An ideal contains a unit exactly when it is the whole ring|"$I=R\iff 1\in I$"]]). This handles the $1\in S$ clause of multiplicative closure.

4. **Read an equivalence as a single biconditional, both directions at once** (operation: *when two statements reduce to the same symbolic core, the two implications are one identity*). Rather than proving (1)$\Rightarrow$(2) and (2)$\Rightarrow$(1) separately by different arguments, we observe the two conditions are *literally* contrapositive, so each direction is the other read backwards.

---

# Hints

> [!note]- Hint 1
> Write both conditions out as logical implications quantified over $a,b\in R$. "Prime" says: *if* $ab\in P$ *then* $a\in P$ or $b\in P$. "$R\setminus P$ multiplicatively closed" says: *if* $a\notin P$ and $b\notin P$ *then* $ab\notin P$ (plus $1\notin P$). Stare at these two implications. How are they related?

> [!note]- Hint 2
> They are **contrapositives**. The contrapositive of "$ab\in P\Rightarrow(a\in P\ \text{or}\ b\in P)$" is "$\neg(a\in P\ \text{or}\ b\in P)\Rightarrow\neg(ab\in P)$". Push the negation inside: $\neg(a\in P\ \text{or}\ b\in P)$ is "$a\notin P$ and $b\notin P$", and $\neg(ab\in P)$ is "$ab\notin P$". That is exactly multiplicative closure of the complement.

> [!note]- Hint 3
> So the *multiplication* halves of the two conditions are logically identical — no work, just a contrapositive. What remains is the *side-condition*. "Prime" requires $P\neq R$. "Multiplicatively closed" requires $1\in R\setminus P$. Show these match: an ideal $P$ is proper ($P\neq R$) if and only if $1\notin P$, i.e. $1\in R\setminus P$.

> [!note]- Hint 4
> Recall that an ideal $I$ equals the whole ring $R$ exactly when $1\in I$ (an ideal containing a unit is everything). Contrapositive: $I\neq R\iff 1\notin I$. So "$P$ is a proper ideal" is the same as "$1\in R\setminus P$" — precisely the $1\in S$ clause in the definition of a multiplicative set. Assemble: main implication (contrapositive) plus side-condition (properness $=$ $1$ outside) gives the full equivalence in both directions simultaneously.

---

# Solution

The two conditions are not merely equivalent — once written symbolically they are the *same statement*, related by a contrapositive. The solution is therefore short: rewrite each condition in logical notation, observe that the multiplication clauses are contrapositive and the side-conditions match, and conclude both directions at once.

**Step 1: Write the prime condition symbolically.**

$P$ is prime if and only if, for all $a,b\in R$,
$$ab\in P\ \Longrightarrow\ (a\in P\ \text{or}\ b\in P),\qquad\text{and}\qquad P\neq R.$$

> [!note]- Derivation
> This is the [[Def - Prime and Maximal Ideal|definition of a prime ideal]] transcribed. The defining clause is the implication "a product in $P$ has a factor in $P$"; the standing requirement $P\neq R$ (a prime ideal is *proper*) is part of the definition — without it the whole ring $R$ would vacuously satisfy the implication and count as prime, which is excluded by convention, exactly as $1$ is excluded from the prime numbers.

**Step 2: Write the multiplicative-closure condition symbolically.**

$R\setminus P$ is multiplicatively closed if and only if
$$1\in R\setminus P,\qquad\text{and}\qquad \big(a\in R\setminus P\ \text{and}\ b\in R\setminus P\big)\ \Longrightarrow\ ab\in R\setminus P.$$

> [!note]- Derivation
> This is the definition of a **multiplicative set** applied to $S=R\setminus P$: such a set must contain $1$ and be closed under products. Rewriting membership in the complement as non-membership in $P$ — "$x\in R\setminus P$" is by definition "$x\in R$ and $x\notin P$", and since everything in sight is in $R$ this is just "$x\notin P$" — the two clauses become
> $$1\notin P,\qquad\text{and}\qquad \big(a\notin P\ \text{and}\ b\notin P\big)\ \Longrightarrow\ ab\notin P.$$

**Step 3: The multiplication clauses are contrapositives — hence identical.**

The implication "$ab\in P\Rightarrow(a\in P\ \text{or}\ b\in P)$" and the implication "$(a\notin P\ \text{and}\ b\notin P)\Rightarrow ab\notin P$" are contrapositive to each other, so each holds if and only if the other does.

> [!note]- Derivation
> Recall the **contrapositive law** of propositional logic: an implication $A\Rightarrow B$ is logically equivalent to $\neg B\Rightarrow\neg A$. Take $A$ to be "$ab\in P$" and $B$ to be "$a\in P\ \text{or}\ b\in P$". Then:
> - $\neg B$ is $\neg(a\in P\ \text{or}\ b\in P)$, which by **De Morgan's law** is "$a\notin P\ \text{and}\ b\notin P$";
> - $\neg A$ is "$ab\notin P$".
>
> So $\neg B\Rightarrow\neg A$ reads
> $$\big(a\notin P\ \text{and}\ b\notin P\big)\ \Longrightarrow\ ab\notin P,$$
> which is *verbatim* the multiplication clause of Step 2. Since $A\Rightarrow B$ and $\neg B\Rightarrow\neg A$ are equivalent for every choice of $a,b$, quantifying over all $a,b\in R$:
> $$\Big[\forall a,b:\ ab\in P\Rightarrow(a\in P\lor b\in P)\Big]\quad\Longleftrightarrow\quad\Big[\forall a,b:\ (a\notin P\land b\notin P)\Rightarrow ab\notin P\Big].$$
> The prime implication and the closure implication are the same statement.

**Step 4: The side-conditions match — properness equals "$1$ is outside".**

The condition $P\neq R$ holds if and only if $1\notin P$, i.e. if and only if $1\in R\setminus P$.

> [!note]- Derivation
> An [[Def - Ideal|ideal]] $I$ of a ring equals the whole ring exactly when it contains $1$: if $1\in I$ then for any $r\in R$, $r=r\cdot 1\in I$ by the ideal's closure under multiplication by ring elements, so $I=R$; conversely if $I=R$ then certainly $1\in I$. (This is the content of [[Ex - An ideal contains a unit exactly when it is the whole ring]].) Taking the contrapositive,
> $$P\neq R\quad\Longleftrightarrow\quad 1\notin P\quad\Longleftrightarrow\quad 1\in R\setminus P.$$
> So the prime side-condition "$P\neq R$" and the multiplicative-set side-condition "$1\in R\setminus P$" are the *same* requirement.

**Step 5: Assemble — both directions at once.**

Combining Steps 3 and 4, the prime condition (Step 1) and the multiplicative-closure condition (Step 2) are equivalent. This proves (1)$\iff$(2).

> [!note]- Derivation
> Condition (1), $P$ prime, is the conjunction of two clauses: the implication of Step 1 and the side-condition $P\neq R$. Condition (2), $R\setminus P$ multiplicatively closed, is the conjunction of: the implication of Step 2 and the side-condition $1\in R\setminus P$.
>
> - By Step 3, the two *implications* are equivalent.
> - By Step 4, the two *side-conditions* are equivalent.
>
> A conjunction $A_1\land A_2$ is equivalent to $B_1\land B_2$ when $A_1\iff B_1$ and $A_2\iff B_2$. Hence condition (1) is equivalent to condition (2). Because the argument is a chain of *equivalences* throughout, both directions (1)$\Rightarrow$(2) and (2)$\Rightarrow$(1) are established simultaneously — there is no need to argue them separately. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** For an ideal $P\trianglelefteq R$ (commutative $R$), $P$ is prime $\iff$ $R\setminus P$ is multiplicatively closed.
>
> By [[Def - Prime and Maximal Ideal|definition]], $P$ is prime iff $P\neq R$ and $\forall a,b\in R:\ ab\in P\Rightarrow(a\in P\lor b\in P)$.
>
> By definition, $R\setminus P$ is multiplicatively closed iff $1\in R\setminus P$ and $\forall a,b\in R:\ (a\in R\setminus P\land b\in R\setminus P)\Rightarrow ab\in R\setminus P$; equivalently, $1\notin P$ and $\forall a,b:\ (a\notin P\land b\notin P)\Rightarrow ab\notin P$.
>
> *Implications coincide.* For fixed $a,b$, the implication $ab\in P\Rightarrow(a\in P\lor b\in P)$ is the contrapositive of $\neg(a\in P\lor b\in P)\Rightarrow\neg(ab\in P)$, i.e. of $(a\notin P\land b\notin P)\Rightarrow ab\notin P$ (using De Morgan). Contrapositives are logically equivalent, so the quantified prime implication and the quantified closure implication are equivalent.
>
> *Side-conditions coincide.* An ideal equals $R$ iff it contains $1$ (if $1\in P$ then $r=r\cdot 1\in P$ for all $r$). So $P\neq R\iff 1\notin P\iff 1\in R\setminus P$.
>
> Both clauses of "prime" are equivalent to the corresponding clauses of "$R\setminus P$ multiplicatively closed", so the two conditions are equivalent. $\blacksquare$

---

# Key Takeaways

**An equivalence between an "inside" condition and an "outside" condition is almost always a contrapositive in disguise.** The cleanest way to recognise this problem's structure is the slogan: a property of *belonging to a set* and the corresponding property of *belonging to its complement* are linked by negation. The prime condition is phrased on $P$ ("a product inside has a factor inside"); the multiplicative-closure condition is phrased on $R\setminus P$ ("a product of outsiders is an outsider"); and these are contrapositive because $\neg(x\in P)$ is exactly $x\in R\setminus P$. The reusable move: whenever a problem asks you to relate a condition on a set to a condition on its complement, write both as quantified implications and check whether one is $\neg B\Rightarrow\neg A$ for the other's $A\Rightarrow B$. If so, the equivalence is *free* — no construction, no theorem, just the contrapositive law. This same pattern recognises why "closed" and "open" are complementary in topology, why "$f$ is injective" dualises cleanly, and why subgroup/coset arguments often have a mirror form.

**Prove a biconditional by reducing both sides to one symbolic core, rather than arguing two separate directions.** The instinctive approach to "$A\iff B$" is to prove $A\Rightarrow B$ and then $B\Rightarrow A$ with two distinct arguments. Often that is necessary — but when both $A$ and $B$ can be *rewritten* until they become the identical statement, the biconditional collapses to a single observation and both directions come for free. Here $A$ ("$P$ prime") and $B$ ("$R\setminus P$ multiplicative") each unfold into "an implication $+$ a side-condition", and after applying the contrapositive law the two unfoldings are character-for-character the same. The general technique: before splitting a biconditional into two implications, spend effort *normalising* each side — expand definitions, apply logical identities, clear notation — and check whether they have already met in the middle. A chain of equivalences ($A\iff A'\iff B'\iff B$) is shorter, less error-prone, and more illuminating than two one-directional proofs.

**Reframing primality on the complement is the entry point to localisation — the multiplicative set is the object you build fractions over.** This exercise looks like a logic puzzle, but its real significance is constructional. The reason "multiplicatively closed" is the right notion is that a multiplicative set $S\subseteq R$ is *exactly* the data needed to form a ring of fractions $S^{-1}R$ — you invert the elements of $S$, just as forming $\operatorname{Frac}(R)$ inverts all non-zero elements (see [[Ex - The field of fractions of an integral domain]]). Forming $\operatorname{Frac}$ requires $R\setminus\{0\}$ to be multiplicatively closed, which is precisely the integral-domain condition; forming the **localisation at a prime** $R_P:=(R\setminus P)^{-1}R$ requires $R\setminus P$ to be multiplicatively closed, which is precisely this exercise. So the content of "primality $=$ complement multiplicatively closed" is: *prime ideals are exactly the ideals you can localise at.* The result reframes a prime not as a special subset of $R$ but as a chosen multiplicative set of "allowed denominators", and localisation at a prime is the central tool of commutative algebra and algebraic geometry — it is how one zooms in on a single point of a variety.

**The properness clause "$P\neq R$" is real content and corresponds to "$1$ lies outside" — never let a side-condition silently vanish.** It is tempting to focus entirely on the multiplication implication and treat "$P\neq R$" as a triviality. But the definition of a multiplicative set *also* carries a clause, "$1\in S$", and the equivalence only holds because these two side-conditions match: $P\neq R\iff 1\notin P\iff 1\in R\setminus P$, via the fact that [[Ex - An ideal contains a unit exactly when it is the whole ring|an ideal is the whole ring iff it contains $1$]]. Had one omitted properness from the definition of prime, or omitted $1\in S$ from the definition of multiplicative set, the equivalence would fail at the edge case $P=R$. The general lesson for equivalence proofs: definitions frequently bundle a *main condition* with a *non-degeneracy side-condition* (prime ideals are proper, multiplicative sets contain $1$, fields are non-zero, bases are linearly independent *and* spanning). When proving two definitions equivalent, account for *every* clause on each side and pair them off explicitly — the side-conditions are where a "nearly correct" proof quietly goes wrong.

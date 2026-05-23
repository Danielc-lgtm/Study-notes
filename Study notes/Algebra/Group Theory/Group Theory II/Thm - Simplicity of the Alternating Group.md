---
type: theorem
subject: group-theory
prereqs:
  - "Def - Symmetric Group"
  - "Def - Simple Group"
  - "Def - Normal Subgroup"
  - "Def - Conjugacy Class"
  - "Thm - Conjugacy Classes of the Symmetric Group"
  - "Thm - The Class Equation"
tags: [algebra, group-theory]
---

# Notation

$S_n$ is the [[Def - Symmetric Group|symmetric group]] on $\{1, \dots, n\}$, and $A_n \leq S_n$ is the **alternating group**, the [[Def - Subgroup|subgroup]] of *even* permutations — those expressible as a product of an even number of transpositions; it has order $n!/2$ for $n \geq 2$. A **transposition** is a $2$-cycle $(a\,b)$; it is odd. A **$3$-cycle** is $(a\,b\,c)$, which equals $(a\,b)(b\,c)$ — a product of two transpositions, hence even, so every $3$-cycle lies in $A_n$. Permutations are written in disjoint cycle notation; the **cycle type** is the list of cycle lengths (see [[Thm - Conjugacy Classes of the Symmetric Group]]). A group $G$ is [[Def - Simple Group|simple]] if $G \neq \{e\}$ and its only [[Def - Normal Subgroup|normal subgroups]] $N \trianglelefteq G$ are $\{e\}$ and $G$. We write $H \trianglelefteq G$ for "$H$ is normal in $G$", $\operatorname{ccl}_G$ for a [[Def - Conjugacy Class|conjugacy class]]. The full notation registry lives on the parent page [[Group Theory II — §1.3–1.4]].

---

# Statement

> **Simplicity of the alternating group.** The alternating group $A_n$ is [[Def - Simple Group|simple]] for every $n \geq 5$. It is also simple for $n = 2$ and $n = 3$. It is **not** simple for $n = 4$.

The cases $n = 2, 3$ are degenerate: $A_2 = \{e\}$ is excluded as not simple by convention's "$G \neq \{e\}$" — more precisely $A_2$ is trivial — while $A_3 \cong C_3$ is cyclic of prime order, hence simple. The case $n = 4$ is a genuine exception: $A_4$, of order $12$, contains the normal subgroup $V = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$, the **Klein four-group**, so it is not simple. The substance of the theorem is the assertion for $n \geq 5$.

---

# Motivation

[[Def - Simple Group|Simple groups]] are the prime numbers of group theory. The Jordan–Hölder theorem says every finite group can be broken down, by repeatedly passing to quotients by normal [[Def - Subgroup|subgroups]], into a uniquely determined list of simple "factors" — so the simple [[Def - Group|groups]] are the indivisible atoms from which all finite [[Def - Group|groups]] are assembled. Understanding finite groups means understanding the simple ones and the ways they can be glued together.

Up to this point the only simple groups in evidence have been the *cyclic groups of prime order* $C_p$. These are simple for a trivial reason: by [[Thm - Lagrange's Theorem|Lagrange's theorem]] a group of prime order has no [[Def - Subgroup|subgroups]] at all except $\{e\}$ and itself, so it has no room for a non-trivial proper normal subgroup. They are also abelian. A natural and pressing question is whether that is the whole story — whether every finite simple group is one of these prime cyclic groups. If so, the atoms of group theory would all be abelian, and finite group theory would be, in a sense, commutative at its core.

This theorem destroys that hope, and decisively. The alternating group $A_5$ has order $60$, which is not prime, and it is non-abelian — yet it is simple. It is, in fact, the *smallest* non-abelian simple group: no non-abelian simple group has order less than $60$. With $A_5$ the subject acquires its first genuinely non-commutative atom, and the infinite family $A_n$, $n \geq 5$, shows there are infinitely many. The classification of finite simple groups — one of the monumental achievements of twentieth-century mathematics — has the alternating groups as one of its main infinite families precisely because of this theorem.

There is a second motivation, historically the original one. A group is called *solvable* if it can be broken down into abelian pieces. A simple non-abelian group cannot be — it has no pieces to break into — so $A_n$ for $n \geq 5$ is **not solvable**, and neither is $S_n$, which contains it. Galois theory attaches to each polynomial a group, and proves that the polynomial is solvable by radicals exactly when that group is solvable. The general polynomial of degree $n$ has Galois group $S_n$. For $n \leq 4$ the group $S_n$ is solvable, and indeed there are formulas — the quadratic, the cubic of Cardano, the quartic of Ferrari. For $n \geq 5$, the simplicity of $A_n$ makes $S_n$ non-solvable, and so **the general quintic, and every higher-degree general polynomial, cannot be solved by radicals**. The Abel–Ruffini theorem is, at its core, this theorem about $A_n$.

---

# Sources and Targets

This section is not an input/output summary. It records the non-obvious circumstances in which the simplicity of $A_n$ is the operative fact (sources), and the non-obvious conclusions that follow from it (targets).

**Sources (Input Broadening)**

Unlike a tool theorem, "$A_n$ is simple" is a fact one *uses*, so its sources are the disguises under which $A_n$, or simplicity, appears.

The first source is **a problem about a group that turns out to contain or surject onto $A_n$**. Property $B$ is "$G$ has a [[Def - Normal Subgroup|normal subgroup]] $N$ with $G/N$ or $N$ isomorphic to $A_n$, $n \geq 5$". The bridge is that simplicity of $A_n$ blocks all further normal structure inside that factor: a normal subgroup of $G$ contained in $N \cong A_n$ must be $\{e\}$ or all of $N$. This is non-obvious because the appearance of $A_n$ may be the *output* of an earlier argument — for instance the [[Thm - Coset Action and the Normal Core|coset action]] embeds a simple group into $A_n$ — and recognising the embedded $A_n$ is what unlocks the rigidity.

A second source is **a polynomial or field extension whose Galois group is $S_n$ or $A_n$**. Property $B$ is "the Galois group of an extension is $S_n$ for some $n \geq 5$" — which happens for the *generic* polynomial of degree $n$, and for many explicit ones. The bridge is that simplicity of $A_n$ forces $S_n$ to be non-solvable, and the Galois correspondence then says the extension is not built by a tower of radicals. This is non-obvious because the problem is about roots and radicals, with the alternating group nowhere mentioned; the simplicity of $A_n$ is the hidden obstruction.

A third source is **the need to certify that a specific group of order $60$ is $A_5$**. Property $B$ is "a simple group of order $60$ is given". A classical theorem says *every* simple group of order $60$ is isomorphic to $A_5$. So whenever a counting argument produces a simple group of order $60$, simplicity of $A_5$ — together with its uniqueness — pins down the group exactly. This is non-obvious because order $60$ alone permits many groups; simplicity collapses them to one.

A fourth source is **a transitive group action of large degree with no obvious normal subgroup**. Property $B$ is "a group acts transitively and primitively on a set, generated by elements of small support such as $3$-cycles". The bridge is a Jordan-type theorem: a primitive permutation group containing a $3$-cycle must contain the whole alternating group, and the simplicity argument's lemma — *a normal subgroup containing one $3$-cycle contains all $3$-cycles* — is the engine. This is non-obvious because the problem looks like combinatorics of an action, not a question about $A_n$.

**Targets (Output Amplification)**

The theorem delivers: $A_n$ has no normal subgroup but $\{e\}$ and itself, for $n \geq 5$. Combined with one further property $D$, this becomes a sharper conclusion.

The headline combination is **simplicity of $A_n$ plus the Galois correspondence yields the unsolvability of the quintic**. Property $D$ is "the general degree-$n$ polynomial has Galois group $S_n$, and a polynomial is solvable by radicals if and only if its Galois group is solvable". A simple non-abelian group is not solvable; $A_n \trianglelefteq S_n$ with simple non-abelian $A_n$ makes $S_n$ non-solvable. The result $E$ — *no radical formula for the general quintic* — is non-obvious because solvability by radicals is an analytic-looking property of explicit formulas, while the obstruction is the internal normal-subgroup structure of a finite group.

A second combination is **simplicity plus the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] forces every homomorphism out of $A_n$ to be trivial or injective**. Property $D$ is "$\varphi : A_n \to K$ is any homomorphism". Its [[Def - Kernel and Image|kernel]] is normal in $A_n$, hence $\{e\}$ or $A_n$; so $\varphi$ is either injective or constant. The result $E$ is that $A_n$ ($n \geq 5$) admits no non-trivial proper quotient at all — it cannot be "simplified". This is non-obvious because most groups have many quotients; simplicity is exactly the statement that this one has none.

A third combination is **simplicity plus normality of $A_n$ in $S_n$ identifies $A_n$ as the unique proper non-trivial normal subgroup of $S_n$ for $n \geq 5$**. Property $D$ is "$N \trianglelefteq S_n$ is non-trivial and proper". Then $N \cap A_n \trianglelefteq A_n$, so by simplicity $N \cap A_n$ is $\{e\}$ or $A_n$; a short argument rules out $\{e\}$ for $n \geq 5$, forcing $A_n \leq N$, and then index considerations give $N = A_n$. The result $E$ — *$A_n$ is the only normal subgroup of $S_n$ besides $\{e\}$ and $S_n$* — is non-obvious because $S_n$ is large and one might expect a richer lattice of normal subgroups.

A fourth combination is **simplicity plus a transitive action gives a primitivity/multiple-transitivity conclusion**. Property $D$ is "$A_n$ acts on a set". Because $A_n$ is simple, the kernel of any non-trivial action is trivial, so the action is faithful; and a simple group acting non-trivially acts with no system of blocks coming from a normal subgroup. The result $E$ — strong transitivity properties, e.g. $A_n$ acts $(n-2)$-transitively on $\{1, \dots, n\}$ — is non-obvious because transitivity is a statement about an action while simplicity is a statement about subgroup structure; the bridge is the kernel.

---

# Why Is It True

The result feels surprising — a non-abelian group of composite order $60$ with no normal subgroups at all — so the goal here is to make it *expected*. Three ideas do that.

**First idea: $3$-cycles are the atoms of $A_n$, and they are all interchangeable.** A normal subgroup is a substance closed under conjugation. To show $A_n$ has no proper non-trivial normal subgroup, it would be enough to know two things: that $A_n$ is *built out of* $3$-cycles (generated by them), and that the $3$-cycles form a *single* conjugacy class — all the same, none distinguished. If both hold, then any non-trivial normal subgroup that manages to capture even one $3$-cycle must, by closure under conjugation, capture *every* $3$-cycle, and therefore — since $3$-cycles generate — be the whole group. The $3$-cycles are like a single indivisible element of the group's chemistry: a normal subgroup either has none of them or has all of them.

Why are all $3$-cycles conjugate *inside $A_n$*? In $S_n$ they certainly are, because [[Thm - Conjugacy Classes of the Symmetric Group|conjugacy is sameness of cycle type]] and all $3$-cycles have the same type. But conjugacy in $S_n$ might use an *odd* permutation, which is not allowed inside $A_n$. The repair is the room afforded by $n \geq 5$: if the conjugating permutation is odd, multiply it by a transposition of two points *not involved in the $3$-cycle* — there are at least two such points when $n \geq 5$ — which fixes up the parity without disturbing the $3$-cycle. This is the precise place the hypothesis $n \geq 5$ enters, and it is why $A_3$ and $A_4$ are exceptional: they are too cramped to perform this parity correction.

**Second idea: every non-trivial normal subgroup is forced to contain a $3$-cycle.** This is the hard part, and the intuition is a kind of *erosion*. Suppose $N \trianglelefteq A_n$ is non-trivial; pick any non-identity $\sigma \in N$. Normality means $N$ contains not only $\sigma$ but also $\sigma^{-1}\delta^{-1}\sigma\delta$ — the **commutator** of $\sigma$ with any $\delta \in A_n$ — because $\delta^{-1}\sigma\delta \in N$ and $N$ is a subgroup. The point of a commutator is that it measures the failure of $\sigma$ and $\delta$ to commute, and if $\delta$ is chosen to overlap $\sigma$ only *slightly*, the commutator is a permutation of *small support* — it moves very few points. So from any element of $N$, by commutating against a well-chosen short cycle $\delta$, you can manufacture a new, *simpler* element of $N$. Iterating this erosion drives the complexity down until what is left is a $3$-cycle (or a $5$-cycle, which the first idea then converts). The case analysis in the formal proof is just the bookkeeping of "however $\sigma$ looks, here is the $\delta$ that erodes it".

**Third idea: $A_4$ shows the argument is sharp.** It is reassuring, not troubling, that the proof fails for $n = 4$. With only four points there is no spare pair to fix parity, the $3$-cycles split into two $A_4$-conjugacy classes rather than one, and the erosion has nowhere to go but the double transpositions, which assemble into the Klein four-group $V \trianglelefteq A_4$. The exception is not a flaw in the theorem; it is the visible boundary of the two mechanisms — parity correction and erosion — both of which need elbow room, and both of which first have it at $n = 5$.

Putting the three together: in $A_n$ for $n \geq 5$, a normal subgroup that contains anything non-trivial is eroded down to a $3$-cycle, and one $3$-cycle spreads by conjugacy to all of them, and all of them generate everything. There is simply nowhere for a proper non-trivial normal subgroup to hide.

---

# What Makes This Hard

The genuinely hard step is the last claim — *every non-trivial normal subgroup contains a $3$-cycle* — which is not a single argument but a case analysis over the possible cycle structures of an element of $N$, where in each case one must *invent* the right short permutation $\delta$ so that the commutator $\sigma^{-1}\delta^{-1}\sigma\delta$ is simpler than $\sigma$; people get stuck because there is no formula for $\delta$, only a pattern. Two subtleties trip up most attempts: forgetting that the hypothesis $n \geq 5$ is used *twice* (once to correct parity when spreading $3$-cycles, once to supply a spare point $5$ in the double-transposition case), and forgetting that the commutator $\sigma^{-1}\delta^{-1}\sigma\delta$ lies in $N$ only because *both* $\delta^{-1}\sigma\delta \in N$ (normality) *and* $\sigma^{-1} \in N$ (subgroup) — a common error is to assume only normality and write down something that need not be in $N$.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Reduce simplicity to two lemmas about $3$-cycles. (a) $A_n$ is generated by $3$-cycles, so a normal subgroup containing all $3$-cycles is everything. (b) For $n \geq 5$, all $3$-cycles are conjugate *within $A_n$*, so a normal subgroup containing *one* $3$-cycle contains all of them. (c) The crux: every non-trivial normal subgroup contains *some* $3$-cycle — proved by taking an element $\sigma \in N$, forming the commutator $\sigma^{-1}\delta^{-1}\sigma\delta \in N$ with a cleverly chosen short $\delta$, and checking, case by case on the cycle type of $\sigma$, that this produces a $3$-cycle (or a $5$-cycle reducible to one). Combining (a)–(c): any non-trivial normal subgroup contains a $3$-cycle by (c), hence all $3$-cycles by (b), hence equals $A_n$ by (a).

**Subgoal decomposition:**

1. **$A_n$ is generated by $3$-cycles.** Show every even permutation is a product of $3$-cycles.
   - *Hint:* An even permutation is a product of an even number of transpositions; group them in pairs and rewrite each pair $(a\,b)(c\,d)$, $(a\,b)(b\,c)$, $(a\,b)(a\,b)$ using $3$-cycles: $(a\,b)(b\,c) = (a\,b\,c)$ and $(a\,b)(c\,d) = (a\,c\,b)(a\,c\,d)$.
   - *Why needed:* A normal subgroup containing every $3$-cycle then contains every product of $3$-cycles, i.e. all of $A_n$.

2. **A normal subgroup containing one $3$-cycle contains all $3$-cycles (for $n \geq 5$).** Show that if $H \trianglelefteq A_n$ and $(a\,b\,c) \in H$, then every $3$-cycle, e.g. $(1\,2\,3)$, lies in $H$.
   - *Hint:* In $S_n$ pick $\sigma$ with $(a\,b\,c) = \sigma(1\,2\,3)\sigma^{-1}$. If $\sigma$ is even, done by normality. If $\sigma$ is odd, replace it by $\bar\sigma = \sigma \cdot (4\,5)$; since $(4\,5)$ commutes with $(1\,2\,3)$, still $\bar\sigma(1\,2\,3)\bar\sigma^{-1} = (a\,b\,c)$, and $\bar\sigma$ is even. (First use of $n \geq 5$.)
   - *Why needed:* It upgrades "contains one $3$-cycle" to "contains all $3$-cycles", which step 1 turns into "$= A_n$".

3. **Every non-trivial normal subgroup contains a $3$-cycle.** Let $H \trianglelefteq A_n$ be non-trivial; take $e \neq \sigma \in H$. By cases on the disjoint cycle structure of $\sigma$, produce a $3$-cycle in $H$.
   - *Hint:* In each case form the commutator $\sigma^{-1}\delta^{-1}\sigma\delta \in H$ for a short $\delta$. Case (i) $\sigma$ has a cycle of length $r \geq 4$: take $\delta = (1\,2\,3)$, get a $3$-cycle. Case (ii) $\sigma$ has $\geq 2$ disjoint $3$-cycles: take $\delta = (1\,2\,4)$, get a $5$-cycle, reduce by case (i). Case (iii) $\sigma$ is one $3$-cycle times $2$-cycles: $\sigma^2$ is a $3$-cycle. Case (iv) $\sigma$ is a product of $2$-cycles: two commutators (using a spare point $5$) produce a $5$-cycle, reduce by case (i).
   - *Why needed:* It supplies the *one* $3$-cycle that steps 2 and 1 then amplify to all of $A_n$.

4. **Assemble.** A non-trivial $H \trianglelefteq A_n$ contains a $3$-cycle (step 3), hence all $3$-cycles (step 2), hence equals $A_n$ (step 1). So the only normal subgroups are $\{e\}$ and $A_n$: $A_n$ is simple for $n \geq 5$.
   - *Hint:* Just chain the three lemmas.
   - *Why needed:* It is the statement.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes (the case analysis of Lemma 3 is longer; treat each case as its own exercise).

> [!note]- Lemma 1: $A_n$ is generated by $3$-cycles
> **Statement:** Every element of $A_n$ is a product of $3$-cycles.
>
> **Hint:** An even permutation is a product of an even number of transpositions; pair them up and convert each pair into $3$-cycles.
>
> **Why needed:** It means a subgroup containing all $3$-cycles is all of $A_n$, turning "contains every $3$-cycle" into "$= A_n$".
>
> > [!note]- Full proof
> > Any element of $A_n$ is, by definition of *even*, a product of an even number of transpositions. Group the transpositions into consecutive pairs; it suffices to show each pair $(a\,b)(c\,d)$ — a product of two transpositions — is a product of $3$-cycles. Let $a, b, c, d$ be points; there are three cases according to how much the two transpositions overlap.
> >
> > - The transpositions are equal: $(a\,b)(a\,b) = e$, a (empty) product of $3$-cycles.
> > - They share one point: $(a\,b)(b\,c) = (a\,b\,c)$, a single $3$-cycle.
> > - They are disjoint, $a, b, c, d$ distinct: $(a\,b)(c\,d) = (a\,c\,b)(a\,c\,d)$ — check by tracking each point.
> >
> > So every product of two transpositions is a product of $3$-cycles, hence so is every product of an even number of transpositions, i.e. every element of $A_n$.

> [!note]- Lemma 2: All $3$-cycles are conjugate in $A_n$ (for $n \geq 5$)
> **Statement:** Let $n \geq 5$ and $H \trianglelefteq A_n$. If $H$ contains one $3$-cycle, it contains every $3$-cycle.
>
> **Hint:** Conjugate $(1\,2\,3)$ to the given $3$-cycle in $S_n$; if the conjugator is odd, fix its parity with a transposition disjoint from $\{1,2,3\}$.
>
> **Why needed:** It upgrades a single $3$-cycle in $H$ to all $3$-cycles, which by Lemma 1 makes $H = A_n$.
>
> > [!note]- Full proof
> > Suppose $(a\,b\,c) \in H$; we show an arbitrary $3$-cycle, say $(1\,2\,3)$, also lies in $H$. Since $(a\,b\,c)$ and $(1\,2\,3)$ have the same cycle type, by [[Thm - Conjugacy Classes of the Symmetric Group|conjugacy in Sₙ]] there is $\sigma \in S_n$ with $(a\,b\,c) = \sigma(1\,2\,3)\sigma^{-1}$.
> >
> > If $\sigma$ is even, $\sigma \in A_n$, and by normality of $H$,
> > $$(1\,2\,3) = \sigma^{-1}(a\,b\,c)\,\sigma \in \sigma^{-1} H \sigma = H.$$
> >
> > If $\sigma$ is odd, replace it by $\bar\sigma = \sigma \cdot (4\,5)$ — here we use $n \geq 5$, so that the points $4, 5$ exist. Then $\bar\sigma$ is even (odd times odd). Since the transposition $(4\,5)$ moves only $4, 5$ and the $3$-cycle $(1\,2\,3)$ moves only $1, 2, 3$, they are disjoint and hence commute, so
> > $$\bar\sigma(1\,2\,3)\bar\sigma^{-1} = \sigma(4\,5)(1\,2\,3)(4\,5)\sigma^{-1} = \sigma(1\,2\,3)\sigma^{-1} = (a\,b\,c).$$
> > Now $\bar\sigma \in A_n$, so by normality $(1\,2\,3) = \bar\sigma^{-1}(a\,b\,c)\,\bar\sigma \in H$.
> >
> > Either way $(1\,2\,3) \in H$, and as $(1\,2\,3)$ was an arbitrary $3$-cycle, $H$ contains all $3$-cycles.

> [!note]- Lemma 3: Every non-trivial normal subgroup of $A_n$ contains a $3$-cycle ($n \geq 5$)
> **Statement:** Let $n \geq 5$ and let $H \trianglelefteq A_n$ be non-trivial. Then $H$ contains a $3$-cycle.
>
> **Hint:** Pick $e \neq \sigma \in H$ and split into four cases by the disjoint cycle structure of $\sigma$. In each case, conjugate $\sigma$ by a short permutation $\delta$ and form the commutator $\sigma^{-1}(\delta^{-1}\sigma\delta) \in H$; choose $\delta$ so the commutator is a $3$-cycle, or a $5$-cycle reducible by Case (i).
>
> **Why needed:** It produces the single $3$-cycle that Lemmas 2 and 1 amplify into all of $A_n$.
>
> > [!note]- Full proof
> > Let $e \neq \sigma \in H$, written in disjoint cycle notation. Throughout, for $\delta \in A_n$ the element $\delta^{-1}\sigma\delta$ lies in $H$ by normality, and $\sigma^{-1} \in H$ since $H$ is a subgroup, so the **commutator** $\sigma^{-1}\delta^{-1}\sigma\delta$ lies in $H$. The four cases below exhaust the possible cycle structures.
> >
> > **Case (i): $\sigma$ contains a cycle of length $r \geq 4$.** Write $\sigma = (a_1\,a_2\,\cdots\,a_r)\,\tau$ with $\tau$ disjoint from $a_1, \dots, a_r$. Relabelling, take the long cycle to be $(1\,2\,3\,\cdots\,r)$, so $\sigma = (1\,2\,3\,\cdots\,r)\,\tau$. Let $\delta = (1\,2\,3) \in A_n$. By normality $\delta^{-1}\sigma\delta \in H$, hence $\sigma^{-1}\delta^{-1}\sigma\delta \in H$. Since $\tau$ does not involve $1, 2, 3$ it commutes with $\delta$, and (being disjoint from the long cycle) with $(1\,2\,3\,\cdots\,r)$; the $\tau$ factors cancel, leaving
> > $$\sigma^{-1}\delta^{-1}\sigma\delta = (r\,\cdots\,2\,1)(1\,3\,2)(1\,2\,3\,\cdots\,r)(1\,2\,3) = (2\,3\,r),$$
> > a $3$-cycle, which lies in $H$. (The same computation works for a long cycle on any points $a_1, \dots, a_r$.)
> >
> > **Case (ii): $\sigma$ is a product of at least two disjoint $3$-cycles** (and no longer cycle, else Case (i)). Relabelling, $\sigma = (1\,2\,3)(4\,5\,6)\,\tau$ with $\tau$ disjoint from $1, \dots, 6$. Let $\delta = (1\,2\,4) \in A_n$. Then $\sigma^{-1}\delta^{-1}\sigma\delta \in H$, and the computation gives
> > $$\sigma^{-1}\delta^{-1}\sigma\delta = (1\,3\,2)(4\,6\,5)(1\,4\,2)(1\,2\,3)(4\,5\,6)(1\,2\,4) = (1\,2\,4\,3\,6),$$
> > a $5$-cycle, which lies in $H$. A $5$-cycle is a cycle of length $\geq 4$, so applying Case (i) to this element of $H$ produces a $3$-cycle in $H$.
> >
> > **Case (iii): $\sigma = (1\,2\,3)\,\tau$ with $\tau$ a product of $2$-cycles** (relabelling; $\tau$ cannot contain a cycle of length $\geq 3$ or there would be two $3$-cycles, Case (ii), or a longer cycle, Case (i)). Then, since $(1\,2\,3)$ and $\tau$ are disjoint and $\tau^2 = e$,
> > $$\sigma^2 = (1\,2\,3)^2\,\tau^2 = (1\,3\,2),$$
> > a $3$-cycle, which lies in $H$ because $H$ is a subgroup.
> >
> > **Case (iv): $\sigma$ is a product of disjoint $2$-cycles** (the only remaining structure; $\sigma$ even forces an even number of them). Relabelling, $\sigma = (1\,2)(3\,4)\,\tau$ with $\tau$ a product of $2$-cycles disjoint from $1,2,3,4$. Let $\delta = (1\,2\,3) \in A_n$ and form
> > $$u = \sigma^{-1}\delta^{-1}\sigma\delta = (1\,2)(3\,4)(1\,3\,2)(1\,2)(3\,4)(1\,2\,3) = (1\,4)(2\,3) \in H.$$
> > We are still in Case (iv), but $u$ is *cleaner* — just two transpositions, with no trailing $\tau$. Now use the spare point $5$ (here $n \geq 5$ is used): conjugate $u$ by $(1\,5\,2) \in A_n$,
> > $$v = (1\,5\,2)\,u\,(1\,5\,2)^{-1} = (1\,5\,2)(1\,4)(2\,3)(1\,2\,5) = (1\,3)(4\,5) \in H.$$
> > Again two transpositions — but $u$ and $v$ are *different* double transpositions. Their product is
> > $$uv = (1\,4)(2\,3)\,(1\,3)(4\,5) = (1\,2\,3\,4\,5) \in H,$$
> > a $5$-cycle. By Case (i) applied to this $5$-cycle in $H$, $H$ contains a $3$-cycle.
> >
> > In every case $H$ contains a $3$-cycle, as claimed.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** $A_n$ is simple for all $n \geq 5$ (and for $n = 2, 3$); $A_4$ is not simple.
>
> *The cases $n = 2, 3$.* $A_2 = \{e\}$ is trivial, and $A_3 \cong C_3$ is cyclic of prime order $3$, which is simple by [[Thm - Lagrange's Theorem|Lagrange's theorem]] (a group of prime order has no proper non-trivial subgroup, normal or otherwise).
>
> *The case $n = 4$.* $A_4$ has order $12$. The set $V = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ is closed under multiplication and inverses, hence a subgroup of order $4$; and it is a union of conjugacy classes of $A_4$ (the identity, and the three double transpositions, which form a single $A_4$-class), so $V \trianglelefteq A_4$. As $V$ is neither $\{e\}$ nor $A_4$, the group $A_4$ is not simple.
>
> *The case $n \geq 5$.* Let $H \trianglelefteq A_n$ with $H \neq \{e\}$; we show $H = A_n$. This is achieved by three claims.
>
> **Claim 1: $A_n$ is generated by $3$-cycles.** Every element of $A_n$ is a product of an even number of transpositions. Grouping them in pairs, it suffices to write a product of two transpositions as a product of $3$-cycles. For points $a, b, c, d$:
> $$(a\,b)(a\,b) = e, \qquad (a\,b)(b\,c) = (a\,b\,c), \qquad (a\,b)(c\,d) = (a\,c\,b)(a\,c\,d).$$
> These three identities cover all overlap patterns of two transpositions, so every element of $A_n$ is a product of $3$-cycles.
>
> **Claim 2: if $H$ contains one $3$-cycle, it contains every $3$-cycle.** Suppose $(a\,b\,c) \in H$; let $(1\,2\,3)$ be an arbitrary $3$-cycle. Since the two have equal cycle type, [[Thm - Conjugacy Classes of the Symmetric Group|conjugacy in Sₙ]] gives $\sigma \in S_n$ with $(a\,b\,c) = \sigma(1\,2\,3)\sigma^{-1}$. If $\sigma \in A_n$, normality of $H$ gives $(1\,2\,3) = \sigma^{-1}(a\,b\,c)\sigma \in H$. If $\sigma$ is odd, set $\bar\sigma = \sigma\cdot(4\,5)$ (this needs $n \geq 5$); then $\bar\sigma$ is even, and since $(4\,5)$ commutes with $(1\,2\,3)$,
> $$\bar\sigma(1\,2\,3)\bar\sigma^{-1} = \sigma(4\,5)(1\,2\,3)(4\,5)\sigma^{-1} = \sigma(1\,2\,3)\sigma^{-1} = (a\,b\,c),$$
> so by normality $(1\,2\,3) = \bar\sigma^{-1}(a\,b\,c)\bar\sigma \in H$. Hence $H$ contains all $3$-cycles, and by Claim 1, $H = A_n$.
>
> **Claim 3: every non-trivial $H \trianglelefteq A_n$ contains a $3$-cycle.** Pick $e \neq \sigma \in H$ and write it in disjoint cycle notation. For any $\delta \in A_n$, normality gives $\delta^{-1}\sigma\delta \in H$, and as $H$ is a subgroup the commutator $\sigma^{-1}\delta^{-1}\sigma\delta \in H$. Cases by the cycle structure of $\sigma$:
>
> *(i) $\sigma$ contains a cycle of length $r \geq 4$.* Relabel so $\sigma = (1\,2\,3\,\cdots\,r)\,\tau$, $\tau$ disjoint from $1, \dots, r$. With $\delta = (1\,2\,3)$, the disjoint $\tau$ commutes with both $\delta$ and the long cycle, so
> $$\sigma^{-1}\delta^{-1}\sigma\delta = (r\,\cdots\,2\,1)(1\,3\,2)(1\,2\,3\,\cdots\,r)(1\,2\,3) = (2\,3\,r) \in H,$$
> a $3$-cycle. (The argument is unchanged for a long cycle on arbitrary points $a_1, \dots, a_r$.)
>
> *(ii) $\sigma$ is a product of at least two disjoint $3$-cycles.* Relabel so $\sigma = (1\,2\,3)(4\,5\,6)\,\tau$. With $\delta = (1\,2\,4)$,
> $$\sigma^{-1}\delta^{-1}\sigma\delta = (1\,3\,2)(4\,6\,5)(1\,4\,2)(1\,2\,3)(4\,5\,6)(1\,2\,4) = (1\,2\,4\,3\,6) \in H,$$
> a $5$-cycle. Applying Case (i) to this element yields a $3$-cycle in $H$.
>
> *(iii) $\sigma = (1\,2\,3)\,\tau$ with $\tau$ a product of $2$-cycles.* Then $\sigma^2 = (1\,2\,3)^2\,\tau^2 = (1\,3\,2) \in H$, a $3$-cycle.
>
> *(iv) $\sigma$ is a product of (an even number of) disjoint $2$-cycles.* Relabel so $\sigma = (1\,2)(3\,4)\,\tau$. With $\delta = (1\,2\,3)$,
> $$u = \sigma^{-1}\delta^{-1}\sigma\delta = (1\,2)(3\,4)(1\,3\,2)(1\,2)(3\,4)(1\,2\,3) = (1\,4)(2\,3) \in H.$$
> Conjugating $u$ by $(1\,5\,2)$ (using $n \geq 5$),
> $$v = (1\,5\,2)\,u\,(1\,2\,5) = (1\,3)(4\,5) \in H.$$
> Then
> $$uv = (1\,4)(2\,3)(1\,3)(4\,5) = (1\,2\,3\,4\,5) \in H,$$
> a $5$-cycle; Case (i) applied to it yields a $3$-cycle in $H$.
>
> The four cases exhaust the cycle structures of an even permutation, so $H$ contains a $3$-cycle.
>
> *Conclusion.* A non-trivial $H \trianglelefteq A_n$ contains a $3$-cycle by Claim 3, hence all $3$-cycles by Claim 2, hence $H = A_n$ by Claim 1. So the only normal subgroups of $A_n$ are $\{e\}$ and $A_n$: for $n \geq 5$, $A_n$ is simple. $\qquad\blacksquare$
>
> **Remark (the brute-force check for $A_5$).** For $n = 5$ simplicity can also be seen directly from the [[Thm - The Class Equation|class equation]]. The conjugacy classes of $A_5$ have sizes $1$ (identity), $15$ (double transpositions, type $2^2\cdot 1$), $20$ ($3$-cycles, type $3\cdot 1^2$), and $12 + 12$ (the $5$-cycles, type $5$, which split into two $A_5$-classes since the cycle type has only odd, distinct parts). Thus $|A_5| = 60 = 1 + 15 + 20 + 12 + 12$. A normal subgroup is a union of conjugacy classes including the class $\{e\}$, and its order divides $60$ by Lagrange. No sub-collection of $\{1, 15, 20, 12, 12\}$ that includes the $1$ sums to a proper divisor of $60$ — the only sub-sums giving $1, 60$ are the empty extension and the whole set. Hence $A_5$ has no proper non-trivial normal subgroup. This brute-force method does not generalise to larger $n$, which is why the case analysis above is needed.

---

# Cross-Field Exercise Suggestions

The aim is to find settings where simplicity of $A_n$ is the decisive fact although nothing in the problem mentions alternating groups.

**Galois theory: the unsolvability of the general quintic.** The splitting field of the generic degree-$n$ polynomial over the field of its coefficients has Galois group $S_n$. A polynomial is solvable by radicals exactly when its Galois group is *solvable* — admits a chain of normal subgroups with abelian quotients ending at $\{e\}$. Because $A_n$ is simple and non-abelian for $n \geq 5$, the chain $S_n \trianglerighteq A_n \trianglerighteq \{e\}$ cannot be refined into abelian pieces, so $S_n$ is not solvable. The result — no radical formula for the general quintic — is the Abel–Ruffini theorem, and its entire group-theoretic content is this theorem. The application is non-obvious because solvability by radicals is a statement about explicit formulas for roots, with the alternating group nowhere in sight.

**Combinatorics: primitive permutation groups containing a $3$-cycle.** Jordan's theorem states that a primitive permutation group on $n$ points that contains a $3$-cycle must contain all of $A_n$. The proof reuses, almost verbatim, the lemma "a normal subgroup containing one $3$-cycle contains all $3$-cycles". A puzzle that asks whether a given set of shuffles, known to act primitively, can generate only a small group is answered by checking for a $3$-cycle among them. The application is non-obvious because the problem is combinatorial — about which arrangements a set of moves can reach — and the alternating group emerges only through the $3$-cycle criterion.

**Geometry: the rotation group of the regular icosahedron.** The orientation-preserving symmetry group of the icosahedron (equivalently the dodecahedron) has order $60$ and acts on certain natural sets of five inscribed objects, giving a homomorphism into $S_5$. One shows this group is simple — it has no normal subgroups — and a simple group of order $60$ must be $A_5$. So the icosahedral rotation group *is* $A_5$. The application is non-obvious because the starting point is a three-dimensional solid and its rotations; that the answer is an alternating group is revealed only by simplicity plus the order-$60$ uniqueness.

**Topology: covering spaces with simple deck group.** A connected covering of a space $X$ corresponds to a subgroup of $\pi_1(X)$, and a *normal* (regular) covering corresponds to a normal subgroup, with deck transformation group the quotient. If a covering has deck group $A_5$, then because $A_5$ is simple there are no intermediate regular coverings strictly between $X$ and the cover — the simplicity of the deck group forbids them. The application is non-obvious because the question is about the lattice of covering spaces, a topological object, and the constraint comes from the normal-subgroup structure of a finite group.

---

# Bridges

- **[[Thm - Conjugacy Classes of the Symmetric Group|Conjugacy Classes of the Symmetric Group]]** — this theorem is the combinatorial backbone of the simplicity proof. "All $3$-cycles are conjugate in $S_n$" is the special case of "conjugacy = cycle type" for the cycle type $3 \cdot 1^{n-3}$; the parity correction by a disjoint transposition is what promotes $S_n$-conjugacy to $A_n$-conjugacy. The case analysis of Claim 3 is organised throughout by the cycle type of the chosen element.

- **[[Thm - The Class Equation|The Class Equation]]** — for $A_5$ the class equation $60 = 1 + 15 + 20 + 12 + 12$ gives the alternative brute-force proof of simplicity: a normal subgroup is a union of classes including $\{e\}$ with order dividing $60$, and no such union is proper and non-trivial. The general proof exists precisely because this class-counting method does not scale to larger $n$.

- **[[Thm - Lagrange's Theorem|Lagrange's Theorem]]** — Lagrange disposes of the small cases ($A_3$ of prime order is automatically simple) and is the reason a normal subgroup's order must divide $|A_n|$, which constrains the brute-force check for $A_5$. The interplay between "divides" and "is realised" is also why $A_4$, of order $12$, has no subgroup of order $6$ — the standard companion fact to its non-simplicity.

- **[[Def - Simple Group|Simple Groups]] and the Jordan–Hölder programme** — $A_5$ is the first non-abelian entry in the catalogue of finite simple groups, and the family $\{A_n : n \geq 5\}$ is one of the major infinite families in the classification of finite simple groups. This theorem is the proof that the atoms of finite group theory are not all abelian.

- **Solvability and Galois theory** — a simple non-abelian group is not solvable, so $A_n$ ($n \geq 5$) and hence $S_n$ are non-solvable. Via the Galois correspondence — solvable Galois group if and only if solvable by radicals — this is the exact group-theoretic reason the general polynomial of degree $\geq 5$ has no solution formula in radicals (Abel–Ruffini).

---

# Unlocked by This

> [!tip] The Abel–Ruffini theorem and Galois' solvability criterion *(from [[Group Theory III — §1.5–1.7|Galois Theory]])*
> Since $A_n$ is simple and non-abelian for $n \geq 5$, the group $S_n$ is not solvable. Galois' theorem — a polynomial is solvable by radicals if and only if its Galois group is solvable — then yields the Abel–Ruffini theorem: the general quintic, and every higher-degree general polynomial, cannot be solved by radicals.

> [!tip] The classification of finite simple groups *(from Advanced Group Theory)*
> $A_5$ is the smallest non-abelian simple group, and $\{A_n : n \geq 5\}$ is one of the principal infinite families in the classification of all finite simple groups — alongside the cyclic groups of prime order, the groups of Lie type, and the $26$ sporadic groups.

---
type: theorem
subject: group-theory
prereqs:
  - "Def - Sylow p-Subgroup"
  - "Def - p-group"
  - "Def - Group Action"
  - "Def - Orbit and Stabiliser"
  - "Def - Coset"
  - "Def - Normaliser"
  - "Def - Conjugacy Class"
  - "Thm - Orbit-Stabiliser Theorem"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a finite group and $p$ a prime. The order is written in its **standard $p$-factorization** $|G| = p^a m$ with $p \nmid m$, so $p^a$ is the exact power of $p$ dividing $|G|$. A [[Def - Sylow p-Subgroup|Sylow p-subgroup]] is a subgroup of order exactly $p^a$; the set of all of them is $\operatorname{Syl}_p(G)$, with $n_p = |\operatorname{Syl}_p(G)|$. A [[Def - p-group|p-subgroup]] is a subgroup of $p$-power order $p^b$ ($b$ not necessarily equal to $a$). For a group $G$ [[Def - Group Action|acting]] on a set $X$, the **orbit** of $x$ is $G \cdot x = \{g \cdot x : g \in G\}$ and the **stabiliser** is $G_x = \{g : g \cdot x = x\}$ (see [[Def - Orbit and Stabiliser]]). For $H \leq G$, the **normaliser** is $N_G(H) = \{g \in G : g^{-1}Hg = H\}$, the largest subgroup in which $H$ is [[Def - Normal Subgroup|normal]] (see [[Def - Normaliser]]). The left coset of $H$ by $g$ is $gH$, and $G/H$ is the set of left cosets. The full notation registry lives on the parent page [[Group Theory III — §1.5–1.7]].

---

# Statement

> **Sylow's Theorems.** Let $G$ be a finite group with $|G| = p^a m$, where $p$ is prime and $p \nmid m$. Then:
>
> **(I) — Existence.** The set $\operatorname{Syl}_p(G) = \{P \leq G : |P| = p^a\}$ is non-empty: $G$ has a [[Def - Sylow p-Subgroup|Sylow p-subgroup]].
>
> **(II) — Conjugacy and containment.** Any two Sylow $p$-[[Def - Subgroup|subgroups]] of $G$ are [[Def - Conjugacy Class|conjugate]] in $G$. More strongly, every [[Def - p-group|p-subgroup]] of $G$ is contained in some Sylow $p$-subgroup.
>
> **(III) — Count.** The number $n_p = |\operatorname{Syl}_p(G)|$ of Sylow $p$-[[Def - Subgroup|subgroups]] satisfies
> $$n_p \equiv 1 \pmod p \qquad \text{and} \qquad n_p \mid |G|.$$
> Since $p \nmid n_p$ by the congruence, in fact $n_p \mid m$.

These are commonly called Sylow's first, second, and third theorems. They are the central result of finite group theory at this level: Sylow I is an existence theorem, the strongest possible converse to [[Thm - Lagrange's Theorem|Lagrange]] at a prime-power divisor; Sylow II is a uniqueness theorem, asserting all Sylow $p$-subgroups look alike; Sylow III is a counting theorem, pinning $n_p$ between a congruence and a divisibility so tightly that often only one value survives.

---

# Motivation

[[Thm - Lagrange's Theorem|Lagrange's theorem]] is a magnificent restriction and a complete non-construction. It tells you the order of any subgroup divides $|G|$, and so it forbids enormously — but it builds nothing. Knowing $|G| = 12$, you know no subgroup has order $5$; you do not know whether a subgroup of order $4$ *exists*. And the converse of Lagrange is genuinely false: $A_4$ has order $12$ and contains no subgroup of order $6$. So the question that organises this entire section is sharp and unavoidable: **for which divisors $d$ of $|G|$ is a subgroup of order $d$ guaranteed to exist?**

The answer comes in layers. Cauchy's theorem handles prime divisors: if a prime $p$ divides $|G|$, there is an element, hence a cyclic subgroup, of order $p$. The $p$-group results of §1.5 handle the case where $|G|$ is *itself* a prime power, where the converse of Lagrange holds in full. Sylow's theorems are the summit because they handle the largest prime-power divisor of an *arbitrary* $|G|$ all at once. Where Cauchy rescues the bottom of each $p$-tower and the $p$-group theorems climb a tower in isolation, Sylow I plants a subgroup at the *top* of the tower — order $p^a$, the exact power — inside any group whatever. And then [[Thm - Subgroups of a p-Group|the subgroup theorem for p-groups]] climbs down from there, delivering a subgroup of every intermediate $p$-power. The converse of Lagrange is thus *true at every prime-power divisor of any finite group*, and Sylow I is the keystone of that statement.

But existence alone would be a curiosity. What makes Sylow's theorems the workhorse of the subject is parts II and III, which say the Sylow $p$-subgroups are *rigidly organised*. They are all conjugate — so as abstract [[Def - Group|groups]] they are indistinguishable, and there is essentially "one" Sylow $p$-subgroup up to the symmetry of $G$. And their number $n_p$ is not free: it is squeezed between $n_p \equiv 1 \pmod p$ and $n_p \mid m$. These two constraints are so tight that for a long list of orders they force $n_p = 1$ outright. A unique Sylow $p$-subgroup is [[Thm - A Unique Sylow Subgroup is Normal|normal]], so this is, in disguise, a theorem about the existence of normal subgroups — and hence about non-[[Def - Simple Group|simplicity]]. The motivating payoff is that the question "is there a simple group of order $n$?" — a question about the existence of an abstract structure — becomes, for small $n$, a finite arithmetic computation. That reduction is the reason Sylow's theorems are taught the way they are.

---

# Sources and Targets

This section records the non-obvious ways a problem arrives at the hypothesis of Sylow's theorems, and the non-obvious results obtained by combining the conclusion with one more fact. Both are distilled from the exercises that actually use the theorem.

**Sources (Input Broadening)**

The hypothesis of Sylow's theorems is almost nothing — *a finite group* — so the theorem applies whenever a finite group is in sight. The genuine recognition skill is spotting which *property of the problem* sets up a productive application; the precondition is bare, so the art is in the targets, but a few sources are worth isolating.

The dominant source is **the order $|G|$ is given as an explicit integer**. Property $B$ is simply "$|G| = n$ for a known $n$", and the bridge is that factoring $n = p^a m$ for each prime $p$ feeds the standard $p$-factorization that Sylow needs. The implication is non-obvious only in that beginners do not realise the *factorization itself is the entire input* — every constraint on the group flows from the exponents $a$ and the cofactors $m$. This is the source behind essentially every non-simplicity exercise: you are handed $n$, and the prime factorization is all you are given to work with.

A second source is **a subgroup of $p$-power order is present**, perhaps constructed earlier in a proof or arising as a kernel or stabiliser. Property $B$ is "$Q \leq G$ with $|Q| = p^b$", and the bridge to the theorem is the strong form of Sylow II: such a $Q$, being a $p$-subgroup, is contained in some Sylow $p$-subgroup, so any $p$-power-order subgroup can be *enlarged* to a maximal one. The implication is non-obvious because one tends to think of Sylow II as a statement about Sylow subgroups only, when in fact it controls *all* $p$-subgroups. This is the source whenever a problem produces a small $p$-group and you need to know it sits inside a Sylow subgroup — for instance, to show two $p$-elements lie in a common Sylow subgroup.

A third source is **$G$ has a normal subgroup $N$, or a quotient $G/N$, of interest**. Property $B$ is "$N \trianglelefteq G$", and the bridge is that Sylow subgroups behave well under intersection with $N$ and projection to $G/N$: a Sylow $p$-subgroup of $G$ meets $N$ in a Sylow $p$-subgroup of $N$ and projects onto a Sylow $p$-subgroup of $G/N$. The implication is non-obvious because the interaction of "maximal $p$-power order" with quotients requires the multiplicativity $|G| = |N| \cdot |G/N|$ to be unwound carefully. This source lets inductive arguments on $|G|$ pass Sylow data between $G$, $N$, and $G/N$.

**Targets (Output Amplification)**

The conclusions Sylow delivers — existence, conjugacy, and the constrained count — become decisive when combined with one further property.

The most powerful combination is **the count plus the arithmetic of $m$ forces $n_p = 1$**. Sylow III gives $n_p \equiv 1 \pmod p$ and $n_p \mid m$ (property $C$). Add the property $D$ that the integer $m$ has *no divisor congruent to $1$ modulo $p$ other than $1$ itself* — a condition you check by listing the divisors of $m$. Then $n_p = 1$, the Sylow $p$-subgroup is unique, hence [[Thm - A Unique Sylow Subgroup is Normal|normal]], and the result $E$ is that $G$ is not [[Def - Simple Group|simple]]. The combination is non-obvious because it converts a structural question ("is there a normal subgroup?") into a divisibility check on a single integer. Orders like $15$, $20$, $1000$ die instantly this way: for $|G| = 1000 = 2^3 \cdot 5^3$, taking $p = 5$ gives $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 8$, and the only common solution is $n_5 = 1$.

A second combination is **conjugacy plus the orbit being a single $G$-set gives an action $G \to S_{n_p}$**. Sylow II says $G$ acts *transitively* by conjugation on $\operatorname{Syl}_p(G)$ (property $C$). Add the property $D$ that $n_p$ is small relative to $|G|$ — specifically $|G| \nmid n_p!$. Then the [[Def - Homomorphism|homomorphism]] $G \to S_{n_p}$ encoding the action has non-trivial kernel (it cannot embed $G$ into the too-small $S_{n_p}$) and non-total kernel (the action is transitive, hence non-trivial), so the kernel is a proper non-trivial normal subgroup; result $E$ is again non-simplicity. The combination is non-obvious because the *number* $n_p$ is being used as the size of a permutation domain, not as a count. This is the tactic for orders like $36$ and $24$.

A third combination is **existence plus the subgroup theorem gives subgroups of every $p$-power order**. Sylow I produces a subgroup $P$ of order $p^a$ (property $C$). Add the property $D$, supplied by [[Thm - Subgroups of a p-Group]], that a $p$-group of order $p^a$ has a normal subgroup of order $p^b$ for every $0 \leq b \leq a$. The result $E$ is that $G$ — *any* finite group — has a subgroup of order $p^b$ for every prime power $p^b$ dividing $|G|$. The combination is non-obvious because it stitches a theorem about arbitrary groups (Sylow I) to a theorem about $p$-groups (the subgroup theorem) to obtain a converse-to-Lagrange statement valid for all finite groups at all prime-power divisors.

A fourth combination is **uniqueness for every prime gives a direct product decomposition**. If Sylow III forces $n_p = 1$ for *every* prime $p$ dividing $|G|$ (property $C$, applied prime by prime), add the property $D$ that distinct Sylow subgroups for distinct primes have coprime orders, hence trivial intersection, and pairwise commute (each being normal). The result $E$ is $G \cong P_1 \times P_2 \times \cdots \times P_k$, the [[Def - Direct Product|direct product]] of its Sylow subgroups — a complete structural description, not merely non-simplicity. The combination is non-obvious because it upgrades several separate normality facts into a single global splitting; it is also the elementary characterisation of nilpotent finite groups.

---

# Why Is It True

The single idea behind all three theorems is worth stating before any of the details: **a finite group understands a prime $p$ by acting on a set and counting fixed points modulo $p$.** Every Sylow theorem is this idea, with a different set chosen each time. So the right intuition is not three separate stories but one mechanism deployed three ways, and the mechanism rests on a fact about $p$-[[Def - Group|groups]] acting on sets that is so useful it deserves to be named the **fixed-point congruence**.

Here is the fixed-point congruence. Suppose a $p$-group $Q$, of order $p^b$, acts on a finite set $X$. Decompose $X$ into orbits. By [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser]], each orbit has size dividing $|Q| = p^b$, so each orbit size is a power of $p$ — either $1$ or a multiple of $p$. The orbits of size $1$ are exactly the fixed points of the action. Summing orbit sizes recovers $|X|$, and modulo $p$ every orbit of size divisible by $p$ contributes nothing, so $|X| \equiv |X^Q| \pmod p$, where $X^Q$ is the set of fixed points. In words: *when a $p$-group acts on a finite set, the number of fixed points is congruent to the size of the set modulo $p$.* The immediate corollary is the one that does the heavy lifting: **if a $p$-group acts on a set whose size is coprime to $p$, there must be at least one fixed point** — because $|X^Q| \equiv |X| \not\equiv 0$, so $|X^Q|$ cannot be zero. Hold onto this; it is the lever for Sylow II.

Now the three theorems, each as an instance.

**Why Sylow I (existence) is plausible.** We want a subgroup of order $p^a$. The clever and counterintuitive move is *not* to look for an element of the set $\Omega$ of all $p^a$-element subsets of $G$ that happens to be a subgroup — there is no reason such a subset is a subgroup. Instead let $G$ act on $\Omega$ by left translation, $g \cdot X = gX$, and look at the *stabilisers*. If some orbit has size exactly $m$, then orbit–stabiliser says the stabiliser of a point in it has index $m$, hence order $p^a$ — and a stabiliser is always a subgroup. So existence of a Sylow $p$-subgroup follows the moment we find an orbit of size $m$. Why should such an orbit exist? Two observations. First, every orbit has size *at least* $m$: an orbit containing the subset $X$ must, by translating, contain a subset through *every* element of $G$, and since each subset has only $p^a$ elements you need at least $|G|/p^a = m$ of them to cover $G$. Second, the total $|\Omega| = \binom{p^a m}{p^a}$ turns out *not* to be divisible by $p$ — a clean and slightly surprising binomial-coefficient computation. Since $\Omega$ is the disjoint union of its orbits and $p \nmid |\Omega|$, not every orbit can have size divisible by $p$; but any orbit of size strictly greater than $m$ would have size a multiple of $p$ (its size divides $p^a m$ and exceeds $m$). So some orbit has size exactly $m$, and its stabiliser is the subgroup we wanted. The intuition: $p$-divisibility of orbit sizes is forced *except* for the orbits of the minimal size $m$, and the count $|\Omega|$ being $p$-coprime guarantees a minimal orbit is actually there.

**Why Sylow II (conjugacy and containment) is plausible.** Take a $p$-subgroup $Q$ and a Sylow $p$-subgroup $P$; we want a conjugate of $Q$ inside $P$. Let $Q$ act on the set $G/P$ of left [[Def - Coset|cosets]] of $P$, by $q \cdot (gP) = qgP$. This set has size $|G|/p^a = m$, *coprime to $p$*. So the fixed-point congruence's corollary applies: $Q$ is a $p$-group acting on a $p$-coprime set, hence there is a fixed coset $gP$. A coset $gP$ being fixed by every $q \in Q$ means $qgP = gP$, i.e. $g^{-1}qg \in P$ for all $q$, i.e. $g^{-1}Qg \subseteq P$. So a conjugate of $Q$ lands inside $P$ — that is the containment statement. When $Q$ is itself a Sylow $p$-subgroup, $g^{-1}Qg$ has the same order $p^a$ as $P$, so the containment is equality and the two are conjugate. The intuition: [[Def - Coset|cosets]] of a Sylow subgroup are a $p$-coprime arena, and any $p$-group poked into that arena cannot avoid a fixed point — and a fixed point is precisely a conjugating element.

**Why Sylow III (the count) is plausible.** Two halves. The divisibility $n_p \mid |G|$ is immediate: by Sylow II, $G$ acts transitively by conjugation on $\operatorname{Syl}_p(G)$, so $\operatorname{Syl}_p(G)$ is a *single orbit*, and by orbit–stabiliser its size $n_p$ divides $|G|$. The congruence $n_p \equiv 1 \pmod p$ is the fixed-point congruence again, with a carefully chosen actor: let a *single* Sylow $p$-subgroup $P$ act by conjugation on the whole set $\operatorname{Syl}_p(G)$. Since $P$ is a $p$-group, every orbit has size $1$ or a multiple of $p$, so $n_p$ is congruent modulo $p$ to the number of fixed points. Now $P$ fixes *itself* — conjugating $P$ by elements of $P$ does nothing — so $\{P\}$ is a fixed point. The whole content is that it is the *only* one. If some other $Q$ were fixed by $P$, then $P$ would normalise $Q$, so $P$ lies in $N_G(Q)$; but inside the group $N_G(Q)$ both $P$ and $Q$ are Sylow $p$-subgroups (both have the maximal $p$-power order $p^a$, since $p^a \mid |N_G(Q)| \mid p^a m$), so by Sylow II *applied within $N_G(Q)$* they are conjugate there — and conjugation inside the normaliser of $Q$ fixes $Q$, forcing $P = Q$. So $P$ is the unique fixed point, $n_p \equiv 1 \pmod p$. The intuition: a Sylow subgroup, conjugating its peers, is too rigid to fix anyone but itself, and "exactly one fixed point" is exactly "$\equiv 1 \pmod p$".

Step back. Each theorem chose a set — the $p^a$-subsets, the cosets $G/P$, the set $\operatorname{Syl}_p(G)$ — let a group act, and read off orbit sizes modulo $p$. That repetition is not a coincidence of exposition; it is the actual unity of the subject. Sylow theory *is* the fixed-point congruence, aimed three times.

---

# What Makes This Hard

The hard part of Sylow I is psychological: the natural instinct is to hunt for an element of $\Omega$ that *is* a subgroup, and the proof refuses to do that — it finds an *orbit* whose *stabiliser* is the subgroup, an indirection most people do not invent unaided. The hard part of Sylow II is recognising that the relevant set is $G/P$ (size $m$, coprime to $p$) and that the fixed-point corollary is what is being used; the common error is to try to conjugate $Q$ into $P$ "by hand" rather than letting $Q$ act. The hard step of Sylow III's congruence is the uniqueness of the fixed point — the argument "$P$ fixes $Q$ $\implies$ $P, Q$ are conjugate *inside $N_G(Q)$* $\implies$ $P = Q$" is genuinely subtle, and the most common mistake is to forget that $Q$ is a Sylow $p$-subgroup *of $N_G(Q)$*, not of $G$, so that Sylow II is being invoked one level down.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct all three proofs.

**High-level strategy:**
All three theorems are one technique — choose a set for a group to act on, then apply [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser]] (so every orbit size divides the group order) and the fixed-point congruence (a $p$-group's orbits have size $1$ or a multiple of $p$, so fixed points are counted modulo $p$). The only creativity is the choice of set: the $p^a$-element subsets of $G$ for existence, the cosets $G/P$ for conjugacy, the set $\operatorname{Syl}_p(G)$ for the count.

**Subgoal decomposition:**

1. **Fixed-point congruence (the shared tool).** Show: if a $p$-group $Q$ acts on a finite set $X$, then $|X^Q| \equiv |X| \pmod p$; consequently if $p \nmid |X|$ there is a fixed point.
   - *Hint:* Orbit sizes divide $|Q| = p^b$, so each is $1$ or divisible by $p$; sum orbit sizes modulo $p$.
   - *Why needed:* It is the engine of Sylow II's conjugacy and Sylow III's congruence.

2. **Sylow I — set up the action.** Let $\Omega = \{X \subseteq G : |X| = p^a\}$ and let $G$ act by left translation $g \cdot X = gX$. Show every orbit has size $\geq m$.
   - *Hint:* An orbit of $X$ contains a translate through every element of $G$; covering $G$ with $p^a$-element sets needs $\geq |G|/p^a = m$ of them.
   - *Why needed:* It pins the minimal possible orbit size, the size that yields a Sylow subgroup.

3. **Sylow I — the binomial count.** Show $p \nmid |\Omega| = \binom{p^a m}{p^a}$.
   - *Hint:* Write $\binom{p^a m}{p^a} = \prod_{j=0}^{p^a - 1} \frac{p^a m - j}{p^a - j}$; for each $j$ the power of $p$ in numerator and denominator is the same (both equal the power of $p$ dividing $j$, since $j < p^a$), so they cancel.
   - *Why needed:* If every orbit had size divisible by $p$, so would $|\Omega|$; $p$-coprimality forces an orbit of size exactly $m$.

4. **Sylow I — extract the subgroup.** Conclude some orbit has size $m$; its stabiliser has index $m$, hence order $p^a$, hence is a Sylow $p$-subgroup.
   - *Hint:* Orbit size divides $|G| = p^a m$ and exceeds $m$ only if divisible by $p$; combine with step 3.
   - *Why needed:* This is Sylow I.

5. **Sylow II — set up and apply the congruence.** Given a $p$-subgroup $Q$ and a Sylow $p$-subgroup $P$, let $Q$ act on $G/P$ by $q \cdot gP = qgP$. Since $|G/P| = m$ is coprime to $p$, step 1 gives a fixed coset $gP$.
   - *Hint:* $|G/P| = |G|/|P| = p^a m / p^a = m$.
   - *Why needed:* A fixed coset is the conjugating element.

6. **Sylow II — read off conjugacy.** From $qgP = gP$ for all $q \in Q$ deduce $g^{-1}Qg \subseteq P$. If $Q$ is itself Sylow, orders are equal so $g^{-1}Qg = P$.
   - *Hint:* $qgP = gP \iff g^{-1}qg \in P$.
   - *Why needed:* This is the containment statement; the equal-order case is conjugacy.

7. **Sylow III — divisibility.** By Sylow II, $G$ acts transitively on $\operatorname{Syl}_p(G)$ by conjugation; orbit–stabiliser gives $n_p \mid |G|$.
   - *Hint:* Transitive action means a single orbit of size $n_p$.
   - *Why needed:* Half of Sylow III.

8. **Sylow III — congruence.** Let one Sylow $p$-subgroup $P$ act by conjugation on $\operatorname{Syl}_p(G)$. By step 1, $n_p \equiv \#\{\text{fixed points}\} \pmod p$. Show $\{P\}$ is the unique fixed point.
   - *Hint:* If $P$ fixes $Q$ then $P \leq N_G(Q)$; both $P$ and $Q$ are Sylow $p$-subgroups of $N_G(Q)$, so by Sylow II *inside $N_G(Q)$* they are conjugate there, hence equal.
   - *Why needed:* Exactly one fixed point gives $n_p \equiv 1 \pmod p$; with $p \nmid n_p$ and step 7, $n_p \mid m$.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

> [!note]- Lemma 1: The fixed-point congruence for a $p$-group action
> **Statement:** Let $Q$ be a [[Def - p-group|p-group]] of order $p^b$ acting on a finite set $X$, and let $X^Q = \{x \in X : q \cdot x = x \text{ for all } q \in Q\}$ be the set of fixed points. Then $|X^Q| \equiv |X| \pmod p$. In particular, if $p \nmid |X|$, then $X^Q \neq \emptyset$.
>
> **Hint:** Partition $X$ into [[Def - Orbit and Stabiliser|orbits]]; by [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser]] each orbit size divides $p^b$, so is $1$ or a multiple of $p$; sum modulo $p$.
>
> **Why needed:** It is the shared engine: Sylow II uses it on $G/P$, Sylow III's congruence uses it on $\operatorname{Syl}_p(G)$.
>
> > [!note]- Full proof
> > The set $X$ is the disjoint union of the orbits of the $Q$-action. For an orbit $O$, the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]] gives $|O| = |Q : Q_x| = |Q|/|Q_x|$ for any $x \in O$, so $|O|$ divides $|Q| = p^b$. Hence each orbit has size a power of $p$: either $1$ or divisible by $p$. An orbit of size $1$ is a single point fixed by all of $Q$, i.e. a point of $X^Q$. Writing $|X| = \sum_{\text{orbits } O} |O|$ and reducing modulo $p$, every orbit with $|O|$ divisible by $p$ contributes $0$, and every orbit of size $1$ contributes $1$, so $|X| \equiv |X^Q| \pmod p$. If $p \nmid |X|$ then $|X^Q| \equiv |X| \not\equiv 0 \pmod p$, so $|X^Q| \neq 0$.

> [!note]- Lemma 2: Every translation orbit of $p^a$-subsets has size at least $m$
> **Statement:** Let $|G| = p^a m$ and let $G$ act on $\Omega = \{X \subseteq G : |X| = p^a\}$ by left translation $g \cdot X = gX$. Then every orbit $\Sigma$ has $|\Sigma| \geq m$.
>
> **Hint:** Show $\Sigma$ contains, for every $g \in G$, a subset *containing* $g$; since each subset has only $p^a$ elements, you need at least $|G|/p^a$ of them to reach every $g$.
>
> **Why needed:** It establishes the minimal orbit size in the Sylow I proof — the size that yields a Sylow subgroup.
>
> > [!note]- Full proof
> > Fix an orbit $\Sigma$ and a subset $X = \{g_1, \dots, g_{p^a}\} \in \Sigma$. For any $g \in G$, the element $g g_1^{-1}$ lies in $G$, so $\Sigma$ — being closed under the action — contains
> > $$g g_1^{-1} \cdot X = \{g g_1^{-1} g_1, \; g g_1^{-1} g_2, \dots\} = \{g, \; g g_1^{-1} g_2, \dots\},$$
> > a $p^a$-element subset that *contains $g$*. Thus for every $g \in G$ there is a member of $\Sigma$ containing $g$. The union of all members of $\Sigma$ is therefore all of $G$. Since each member has exactly $p^a$ elements, covering the $|G| = p^a m$ elements of $G$ requires at least $p^a m / p^a = m$ members. Hence $|\Sigma| \geq m$.

> [!note]- Lemma 3: The count $\binom{p^a m}{p^a}$ is not divisible by $p$
> **Statement:** For $p$ prime and any positive integer $m$ with $p \nmid m$ (indeed any $m$), $p \nmid \dbinom{p^a m}{p^a}$.
>
> **Hint:** Write the binomial coefficient as $\prod_{j=0}^{p^a-1} \frac{p^a m - j}{p^a - j}$ and compare, for each $j$, the power of $p$ in the numerator $p^a m - j$ with that in the denominator $p^a - j$.
>
> **Why needed:** It forces a translation orbit of size exactly $m$ in the Sylow I proof: if every orbit had size divisible by $p$, then $|\Omega|$ would be too.
>
> > [!note]- Full proof
> > Write
> > $$\binom{p^a m}{p^a} = \prod_{j=0}^{p^a - 1} \frac{p^a m - j}{p^a - j}.$$
> > Fix $j$ with $0 \leq j < p^a$ and let $p^c$ be the exact power of $p$ dividing $j$ (for $j = 0$ the factor is $\frac{p^a m}{p^a} = m$, contributing no $p$ either way). Since $j < p^a$ we have $c < a$. Now $p^a m - j$: writing $j = p^c j'$ with $p \nmid j'$, we get $p^a m - j = p^c(p^{a-c} m - j')$, and $p^{a-c} m - j' \equiv -j' \not\equiv 0 \pmod p$ because $a - c \geq 1$; so the exact power of $p$ dividing $p^a m - j$ is $p^c$. Identically, $p^a - j = p^c(p^{a-c} - j')$ with $p^{a-c} - j' \equiv -j' \not\equiv 0 \pmod p$, so the exact power of $p$ dividing $p^a - j$ is also $p^c$. Numerator and denominator carry the *same* power of $p$ in every factor, so all powers of $p$ cancel and the product $\binom{p^a m}{p^a}$ is coprime to $p$.

> [!note]- Lemma 4: A Sylow $p$-subgroup of $G$ contained in a subgroup $K$ is a Sylow $p$-subgroup of $K$
> **Statement:** Let $P$ be a [[Def - Sylow p-Subgroup|Sylow p-subgroup]] of $G$ and let $K$ be any subgroup of $G$ with $P \leq K \leq G$. Then $P$ is a Sylow $p$-subgroup of $K$.
>
> **Hint:** $|P| = p^a$ is a $p$-power dividing $|K|$, and $|K|$ divides $|G| = p^a m$, so $p^a$ is already the largest power of $p$ that *can* divide $|K|$.
>
> **Why needed:** In Sylow III's congruence, this is what makes both $P$ and $Q$ Sylow $p$-subgroups of $N_G(Q)$, so that Sylow II can be applied inside the normaliser.
>
> > [!note]- Full proof
> > By [[Thm - Lagrange's Theorem|Lagrange]], $|P| \mid |K|$ and $|K| \mid |G|$, so $p^a = |P| \mid |K| \mid p^a m$. Thus the order of $K$ is $p^a m'$ where $m' \mid m$, and since $p \nmid m$ also $p \nmid m'$ — so $p^a$ is the exact power of $p$ dividing $|K|$. The subgroup $P \leq K$ has order $p^a$, which is precisely the maximal $p$-power dividing $|K|$. Hence $P$ is a Sylow $p$-subgroup of $K$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a finite group with $|G| = p^a m$, $p$ prime, $p \nmid m$. The arguments below are the proofs from the source lecture notes.
>
> ---
>
> **Proof of Sylow I (existence).**
>
> We must produce a subgroup of order $p^a$. We find a clever set for $G$ to act on. Let
> $$\Omega = \{X \subseteq G : |X| = p^a\}$$
> be the set of all $p^a$-*element subsets* of $G$ (subsets, not subgroups), and let $G$ act on $\Omega$ by left translation,
> $$g * \{g_1, g_2, \dots, g_{p^a}\} = \{g g_1, g g_2, \dots, g g_{p^a}\}.$$
> Let $\Sigma$ be an orbit of this action.
>
> *Every orbit has size at least $m$.* If $\{g_1, \dots, g_{p^a}\} \in \Sigma$, then for every $g \in G$, by the definition of an orbit,
> $$g g_1^{-1} * \{g_1, \dots, g_{p^a}\} = \{g, \; g g_1^{-1} g_2, \dots, g g_1^{-1} g_{p^a}\} \in \Sigma,$$
> so $\Sigma$ contains a set which contains $g$. Since each member of $\Sigma$ has $p^a$ elements and their union is all of $G$, we need at least $|G|/p^a = m$ members:
> $$|\Sigma| \geq \frac{|G|}{p^a} = m.$$
>
> *If some orbit has size exactly $m$, we are done.* Suppose $|\Sigma| = m$. By the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]], the stabiliser of any $X \in \Sigma$ has index $|\Sigma| = m$ in $G$, hence order $|G|/m = p^a$. A stabiliser is a subgroup, so this stabiliser is a subgroup of order $p^a$ — a Sylow $p$-subgroup.
>
> *Some orbit does have size $m$.* By orbit–stabiliser, every orbit size divides $|G| = p^a m$. So if an orbit has size $> m$, that size is divisible by $p$. We show not every orbit can have size $> m$ by showing $p \nmid |\Omega|$ — for $\Omega$ is the disjoint union of its orbits, so if all orbits had $p$-divisible size, $|\Omega|$ would be $p$-divisible too. We compute:
> $$|\Omega| = \binom{|G|}{p^a} = \binom{p^a m}{p^a} = \prod_{j=0}^{p^a - 1} \frac{p^a m - j}{p^a - j}.$$
> Fix $j$ with $0 \leq j < p^a$. Since $j < p^a$, the largest power of $p$ dividing $p^a m - j$ equals the largest power of $p$ dividing $j$ (write $j = p^c j'$ with $c < a$, $p \nmid j'$; then $p^a m - j = p^c(p^{a-c}m - j')$ and $p \nmid p^{a-c}m - j'$). Identically, the largest power of $p$ dividing $p^a - j$ equals the largest power of $p$ dividing $j$. So numerator and denominator carry the same power of $p$ in every factor; they cancel, and $p \nmid |\Omega|$.
>
> Therefore not every orbit has size $> m$; some orbit has size exactly $m$, and its stabiliser is a Sylow $p$-subgroup. $\quad\blacksquare$
>
> *(Remark, after the lecture notes: the proof is not straightforward. The clever idea is to act on $\Omega$ at all; and even given $\Omega$, the obvious move would be to find a member of $\Omega$ that happens to be a subgroup — that is **not** what is done. Instead one finds an orbit whose stabiliser is a Sylow $p$-subgroup.)*
>
> ---
>
> **Proof of Sylow II (conjugacy and containment).**
>
> We prove the stronger statement: *if $Q \leq G$ is any $p$-subgroup (so $|Q| = p^b$, $b$ not necessarily $a$) and $P \leq G$ is a Sylow $p$-subgroup, then there exists $g \in G$ with $g^{-1}Qg \leq P$.* Applying this with $Q$ a Sylow $p$-subgroup gives $g^{-1}Qg \leq P$ with $|g^{-1}Qg| = |Q| = p^a = |P|$, forcing $g^{-1}Qg = P$ — so any two Sylow $p$-subgroups are conjugate.
>
> Let $Q$ act on the set of left cosets $G/P$ by
> $$q * gP = qgP.$$
> By the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]], every orbit of this action has size dividing $|Q| = p^b$, hence size $1$ or divisible by $p$. They cannot *all* be divisible by $p$, because
> $$|G/P| = \frac{|G|}{|P|} = \frac{p^a m}{p^a} = m$$
> is coprime to $p$, and the orbit sizes sum to $|G/P| = m$. So at least one orbit has size $1$, say $\{gP\}$.
>
> An orbit $\{gP\}$ of size $1$ means $q * gP = gP$ for every $q \in Q$, i.e. $qgP = gP$, i.e. $g^{-1}qg \in P$ for every $q \in Q$. Hence $g^{-1}Qg \subseteq P$, and being a subgroup, $g^{-1}Qg \leq P$. This proves the strong form, and with it conjugacy. $\quad\blacksquare$
>
> ---
>
> **Proof of Sylow III (the count).**
>
> We must show $n_p \equiv 1 \pmod p$ and $n_p \mid |G|$, where $n_p = |\operatorname{Syl}_p(G)|$.
>
> *The divisibility $n_p \mid |G|$.* The group $G$ acts on $\operatorname{Syl}_p(G)$ by conjugation, $g * P = gPg^{-1}$ (this is well-defined: a conjugate of a subgroup of order $p^a$ again has order $p^a$). By Sylow II, all Sylow $p$-subgroups are conjugate, so this action is **transitive** — it has a single orbit, all of $\operatorname{Syl}_p(G)$. By the [[Thm - Orbit-Stabiliser Theorem|orbit–stabiliser theorem]], the size of this orbit, namely $|\operatorname{Syl}_p(G)| = n_p$, divides $|G|$.
>
> *The congruence $n_p \equiv 1 \pmod p$.* Fix one Sylow $p$-subgroup $P \in \operatorname{Syl}_p(G)$ and let $P$ act on $\operatorname{Syl}_p(G)$ by conjugation. By orbit–stabiliser, every orbit of this action has size dividing $|P| = p^a$, hence $1$ or divisible by $p$. So $n_p$ is congruent modulo $p$ to the number of orbits of size $1$. There is one orbit of size $1$, namely $\{P\}$ itself, since conjugating $P$ by elements of $P$ returns $P$. It remains to show this is the *only* orbit of size $1$.
>
> Suppose $\{Q\}$ is an orbit of size $1$. Then $p^{-1}Qp = Q$ for every $p \in P$, which says $P \leq N_G(Q)$, the [[Def - Normaliser|normaliser]] of $Q$. Now $N_G(Q)$ is itself a group, and we examine its Sylow $p$-subgroups. We have $Q \leq N_G(Q) \leq G$, so by [[Thm - Lagrange's Theorem|Lagrange]] $p^a = |Q| \mid |N_G(Q)| \mid |G| = p^a m$; hence $p^a$ is the exact power of $p$ dividing $|N_G(Q)|$. Therefore $Q$, of order $p^a$, is a Sylow $p$-subgroup *of $N_G(Q)$*. Likewise $P \leq N_G(Q)$ has order $p^a$, so $P$ is also a Sylow $p$-subgroup of $N_G(Q)$.
>
> By Sylow II applied **within the group $N_G(Q)$**, the two Sylow $p$-subgroups $P$ and $Q$ of $N_G(Q)$ are conjugate in $N_G(Q)$ — there is $g \in N_G(Q)$ with $g^{-1}Qg = P$. But conjugating $Q$ by an element of $N_G(Q)$ does nothing, by the definition of the normaliser: $g^{-1}Qg = Q$. Hence $P = Q$.
>
> So $\{P\}$ is the only orbit of size $1$, and $n_p \equiv 1 \pmod p$.
>
> *Finally $n_p \mid m$.* We have $n_p \mid |G| = p^a m$ and, from the congruence, $p \nmid n_p$. A divisor of $p^a m$ coprime to $p$ must divide $m$. Hence $n_p \mid m$. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

The aim is to find settings where Sylow's theorems apply but are not advertised — to battle-test recognition of the *sources*.

**Linear algebra: Sylow $p$-subgroups of $\mathrm{GL}_n$ over a finite field.** The group $G = \mathrm{GL}_n(\mathbb{Z}/p)$ of invertible $n \times n$ matrices over the $p$-element field has order $(p^n - 1)(p^n - p)\cdots(p^n - p^{n-1})$, and the exact power of $p$ in it is $p^{\binom{n}{2}}$. Sylow I guarantees a subgroup of that order, and one can *exhibit* it: the unipotent upper-triangular matrices (ones on the diagonal, free entries above) form a Sylow $p$-subgroup. The application is non-obvious because the problem is phrased about matrices and linear independence, with no abstract group order in sight until you count $|\mathrm{GL}_n(\mathbb{Z}/p)|$ — property $B$, "the invertible matrices form a finite group", is the bridge to the precondition. The same idea finds a Sylow $\ell$-subgroup for a prime $\ell \mid p - 1$: since $(\mathbb{Z}/p)^\times \cong C_{p-1}$ contains $C_\ell$, the diagonal matrices give $C_\ell \times C_\ell \leq \mathrm{GL}_2(\mathbb{Z}/p)$, a Sylow $\ell$-subgroup when $\ell^3 \nmid |G|$.

**Number theory: a clean proof of Cauchy's theorem and Wilson-type counts.** Sylow I subsumes Cauchy's theorem — a Sylow $p$-subgroup for $p \mid |G|$ is a non-trivial [[Def - p-group|p-group]], and any non-trivial $p$-group has an element of order $p$ — so a problem asking "show $G$ has an element of order $p$" can be routed through Sylow I even though it mentions no subgroup of order $p^a$. The application is non-obvious because Sylow I produces *more* than asked (a whole subgroup of order $p^a$), and one must see that the bigger object answers the smaller question. More subtly, the fixed-point congruence (Lemma 1) applied to cyclic group actions on tuples gives congruence identities — for instance, letting $C_p$ rotate the $p$-tuples of $G$ with product $e$ recovers Cauchy directly and yields the number of such tuples modulo $p$.

**Combinatorics and design theory: counting via the Sylow-set action.** When $G$ acts by conjugation on $\operatorname{Syl}_p(G)$, the orbit is a single transitive $G$-set of size $n_p$, so $n_p = |G : N_G(P)|$ — a *combinatorial* count of subgroups is realised as an index. A problem that asks for the number of subgroups of a certain order in a specific group becomes a normaliser-index computation. The application is non-obvious because "how many subgroups of order $p^a$?" sounds like a search problem, whereas Sylow III turns it into the evaluation of a single index $|G : N_G(P)|$, constrained further to lie in $\{1, 1+p, 1+2p, \dots\} \cap \{\text{divisors of } m\}$.

**Geometry and the symmetries of polytopes.** The rotation group of a Platonic solid is a finite group — the icosahedral rotation group has order $60$, the same as $A_5$. Asking whether such a symmetry group can be [[Def - Simple Group|simple]], or locating its subgroups of prime-power order, is a Sylow problem: factor $60 = 2^2 \cdot 3 \cdot 5$, list the admissible $n_p$, and the Sylow subgroups correspond to stabilisers of geometric features (axes through faces, edges, vertices). The application is non-obvious because the input is a geometric object; property $B$, "the rotational symmetries form a finite group", is the bridge, and the Sylow $5$-subgroups turn out to be the rotation groups about the six five-fold axes.

---

# Bridges

- **[[Thm - A Unique Sylow Subgroup is Normal|A unique Sylow subgroup is normal]]** — the immediate and most-used corollary: if Sylow III forces $n_p = 1$, the lone Sylow $p$-subgroup is [[Def - Normal Subgroup|normal]], because Sylow II says every conjugate of it is again a Sylow $p$-subgroup and there is only one. This is the bridge from the Sylow count to the existence of normal subgroups, hence to non-[[Def - Simple Group|simplicity]].

- **[[Thm - Lagrange's Theorem|Lagrange's theorem]]** — Sylow I is the sharp *partial converse* to Lagrange. Lagrange says a subgroup of order $d$ exists only if $d \mid |G|$; the converse is false for general $d$ ($A_4$, no subgroup of order $6$), true for prime $d$ (Cauchy), and true for the top prime power $p^a$ (Sylow I). Together with [[Thm - Subgroups of a p-Group]], which climbs down from $p^a$, the converse of Lagrange holds at *every* prime-power divisor of any finite group.

- **[[Thm - Orbit-Stabiliser Theorem|Orbit–stabiliser theorem]]** — the single tool every Sylow proof rests on. Sylow I uses it to convert an orbit of size $m$ into a stabiliser of order $p^a$; Sylow II and III use it in the form "a $p$-group's orbit sizes are powers of $p$", which is the fixed-point congruence. Sylow theory is orbit–stabiliser applied to three well-chosen actions.

- **[[Thm - The Class Equation|The class equation]]** — the special case of the fixed-point congruence when a group acts on *itself* by conjugation; the size-$1$ orbits are the [[Def - Centraliser and Centre|centre]]. Applied to a $p$-group it forces a non-trivial centre ([[Thm - p-Groups Have Non-Trivial Centre]]), and the same modulo-$p$ orbit-counting underlies Sylow III's congruence — the two are the one fixed-point principle, aimed at different sets.

- **[[Thm - Subgroups of a p-Group|Subgroups of a p-group]]** — the downstream partner of Sylow I. Sylow I plants a subgroup at order $p^a$; the subgroup theorem then supplies, *inside that $p$-group*, a normal subgroup of order $p^b$ for every $0 \leq b \leq a$. The composite gives subgroups of every prime-power order in any finite group.

---

# Unlocked by This

> [!tip] The Non-Simplicity Playbook *(from §1.7 exercises)*
> Sylow's theorems make the question "is there a [[Def - Simple Group|simple group]] of order $n$?" a finite computation for small $n$: factor $n$, list the $n_p$ permitted by $n_p \equiv 1 \pmod p$ and $n_p \mid m$, and run the tactics — force some $n_p = 1$ (uniqueness), count elements of prime order, or act on the Sylow set $G \to S_{n_p}$.

> [!tip] Nilpotent and Solvable Groups *(from Galois Theory)*
> A finite group is **nilpotent** precisely when it is the [[Def - Direct Product|direct product]] of its Sylow $p$-subgroups — a structural characterisation built directly on Sylow theory. Every $p$-group is nilpotent, hence solvable; solvability of a polynomial's Galois group decides solubility by radicals.

> [!tip] Borel Subgroups and Algebraic Groups *(from the Theory of Algebraic Groups)*
> Sylow II — all Sylow $p$-subgroups are conjugate — is the finite-group prototype of **Borel's conjugacy theorem**: all maximal connected solvable subgroups (Borel subgroups) of an algebraic group are conjugate. The unipotent upper-triangular Sylow $p$-subgroup of $\mathrm{GL}_n(\mathbb{Z}/p)$ is the finite shadow of the Borel subgroup of $\mathrm{GL}_n$.

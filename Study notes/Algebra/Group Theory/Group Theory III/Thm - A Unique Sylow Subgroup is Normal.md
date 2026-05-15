---
type: theorem
subject: group-theory
prereqs:
  - "Def - Sylow p-Subgroup"
  - "Def - Normal Subgroup"
  - "Def - Conjugacy Class"
  - "Def - Simple Group"
  - "Thm - Sylow's Theorems"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a finite group and $p$ a prime, with order in the **standard $p$-factorization** $|G| = p^a m$, $p \nmid m$. A [[Def - Sylow p-Subgroup|Sylow $p$-subgroup]] is a subgroup of order exactly $p^a$; the set of all of them is $\operatorname{Syl}_p(G)$, and $n_p = |\operatorname{Syl}_p(G)|$ is their number. A subgroup $N \leq G$ is [[Def - Normal Subgroup|normal]], written $N \trianglelefteq G$, if $gNg^{-1} = N$ for every $g \in G$ — equivalently, $N$ is invariant under conjugation. Two subgroups $H, K$ are **conjugate** if $K = gHg^{-1}$ for some $g \in G$ (see [[Def - Conjugacy Class]]). A group with no [[Def - Normal Subgroup|normal subgroup]] other than $\{e\}$ and itself is [[Def - Simple Group|simple]]. The full notation registry lives on the parent page [[Group Theory III — §1.5–1.7]].

---

# Statement

> **Theorem (a unique Sylow $p$-subgroup is normal).** Let $G$ be a finite group and $p$ a prime. If $G$ has exactly one [[Def - Sylow p-Subgroup|Sylow $p$-subgroup]] — that is, if $n_p = 1$ — then that subgroup is [[Def - Normal Subgroup|normal]] in $G$.
>
> Conversely, if a Sylow $p$-subgroup $P$ is normal in $G$, then it is the *only* Sylow $p$-subgroup, so $n_p = 1$. Thus $n_p = 1$ if and only if some (equivalently, every) Sylow $p$-subgroup is normal.

The theorem is short, and its proof is shorter still — a single line off the back of [[Thm - Sylow's Theorems|Sylow II]]. Its importance is entirely disproportionate to its difficulty: it is the hinge that converts the arithmetic of [[Thm - Sylow's Theorems|Sylow III]] into the existence of a normal subgroup, and hence the standard route to every non-[[Def - Simple Group|simplicity]] proof in the subject.

---

# Motivation

The recurring goal of finite group theory at this level is to find a [[Def - Normal Subgroup|normal subgroup]] — most often because one wants to prove a group of a given order is not [[Def - Simple Group|simple]]. But "normal subgroup" is a structural, almost geometric condition: $N$ must be invariant under conjugation by *every* element of $G$, and conjugation is hard to control directly. One would much rather have a goal that is *arithmetic*, something checkable by counting and divisibility, because [[Thm - Sylow's Theorems|Sylow's theorems]] hand us arithmetic in abundance — Sylow III pins the number $n_p$ between $n_p \equiv 1 \pmod p$ and $n_p \mid m$.

This theorem is the bridge between the two. It says: to produce a normal subgroup, it is enough to produce a *number* — namely, to force $n_p = 1$ for some prime $p$. The abstract task "find a conjugation-invariant subgroup" becomes the concrete, mechanical task "show the Sylow count is $1$", and the latter is pure arithmetic on the divisors of $|G|$. Without this theorem, Sylow III would be a curious fact about how many Sylow subgroups there are; *with* it, Sylow III becomes a normal-subgroup detector. That is why, despite a one-line proof, it is the single most-invoked consequence of Sylow's theorems in practice.

The reason the theorem is *true* is equally worth front-loading. Normality of $P$ means every conjugate $gPg^{-1}$ equals $P$. But [[Thm - Sylow's Theorems|Sylow II]] tells us a conjugate of a Sylow $p$-subgroup is *always itself a Sylow $p$-subgroup* — conjugation permutes the set $\operatorname{Syl}_p(G)$ within itself. If that set has only one element, a permutation of it has nowhere to send that element but back to itself. Uniqueness leaves conjugation no room to move $P$, and "cannot be moved by conjugation" is the definition of normal.

---

# Sources and Targets

This section records the non-obvious ways a problem arrives at the hypothesis $n_p = 1$, and the non-obvious results that follow once a normal Sylow subgroup is in hand. Both are distilled from the non-simplicity exercises that use this theorem.

**Sources (Input Broadening)**

The hypothesis is $n_p = 1$. One almost never *checks* this directly; the skill is recognising the properties $B$ of a problem that *force* it.

The dominant source is **the divisors of $m$ admit no value $\equiv 1 \pmod p$ except $1$**. Property $B$ is an arithmetic fact about the factorization $|G| = p^a m$: when you list the divisors of $m$ and intersect with the residue class $1 \pmod p$, only $1$ survives. The bridge is [[Thm - Sylow's Theorems|Sylow III]] — $n_p$ must lie in exactly that intersection — so $n_p = 1$ is forced. The implication is non-obvious only because it requires *both* Sylow constraints at once: the congruence alone permits $1 + p, 1 + 2p, \dots$, the divisibility alone permits every divisor of $m$, and it is their *common* solutions that count. This is the source behind orders like $15, 20, 33, 1000$: for $|G| = 1000 = 2^3 \cdot 5^3$ and $p = 5$, the divisors of $m = 8$ are $1, 2, 4, 8$, of which only $1$ is $\equiv 1 \pmod 5$, so $n_5 = 1$ and the Sylow $5$-subgroup is normal.

A second source is **a counting or embedding argument has eliminated every other value of $n_p$**. Property $B$ is the conclusion of a prior contradiction — perhaps element-counting showed too few elements remain for a non-unique Sylow subgroup, or an action $G \to S_{n_p}$ ruled out the larger admissible values. The bridge is that once all values $n_p > 1$ are excluded, only $n_p = 1$ is left, and this theorem converts that into normality. The implication is non-obvious because the source is not a single clean divisibility but the *residue* of a longer argument; the theorem is then the final step that turns "$n_p$ cannot be anything else" into "there is a normal subgroup".

A third source is **$G$ is known to be the [[Def - Direct Product|direct product]] of, or to contain as a direct factor, a group of $p$-power order**. Property $B$ is a decomposition $G \cong P \times H$ with $|P| = p^a$. The bridge is that the factor $P$ is then a normal subgroup of $p$-power maximal order, hence *the* Sylow $p$-subgroup, so $n_p = 1$. The implication is non-obvious because the direct-product structure is usually used to read off other features, and one must notice that a $p$-power direct factor is automatically a normal Sylow subgroup.

**Targets (Output Amplification)**

The conclusion is "$G$ has a normal Sylow $p$-subgroup $P$". Combined with one further property it yields more.

The headline combination is **a normal Sylow subgroup plus the search for a proper non-trivial normal subgroup gives non-simplicity**. The conclusion provides a normal subgroup $P$ (property $C$). Add the property $D$ that $1 < p^a < |G|$ — true whenever $p \mid |G|$ and $|G|$ is not itself a prime power. Then $P$ is a *proper, non-trivial* normal subgroup, and the result $E$ is that $G$ is not [[Def - Simple Group|simple]]. The combination is the entire point of the theorem; it is non-obvious only in that one must confirm $P$ is neither trivial (it is not, since $p \mid |G|$ gives $p^a > 1$) nor everything (it is not, since $|G| = p^a m$ with $m > 1$).

A second combination is **a normal Sylow subgroup for *every* prime gives a direct product**. If this theorem yields $n_p = 1$ for every prime $p$ dividing $|G|$ (property $C$, applied prime by prime), add the property $D$ that distinct Sylow subgroups for distinct primes have coprime orders, hence trivial intersection, and — being normal — pairwise commute. The result $E$ is $G \cong P_1 \times \cdots \times P_k$, the [[Def - Direct Product|direct product]] of its Sylow subgroups. The combination is non-obvious because it upgrades a list of separate normality facts into one global splitting; it is the elementary characterisation of nilpotent finite groups, and it shows the theorem proves not just non-simplicity but, when the arithmetic fully cooperates, complete structure.

A third combination is **a normal Sylow $p$-subgroup plus a complement gives a semidirect product**. The conclusion gives $P \trianglelefteq G$ (property $C$). Add the property $D$ that there is a subgroup $H \leq G$ with $|H| = m$ and $H \cap P = \{e\}$ — for instance a Sylow subgroup for the *other* prime factors, when $|G| = p^a q^b$. Then $G = P \rtimes H$ is a semidirect product, and the result $E$ is that classifying the groups of order $|G|$ with normal Sylow $p$-subgroup reduces to classifying the homomorphisms $H \to \operatorname{Aut}(P)$. The combination is non-obvious because normality of one Sylow subgroup does *not* give a direct product — only a semidirect one — and recognising which is in play is the difference between $C_6$ and $S_3$.

---

# Why Is It True

The theorem is true for a reason that can be seen in a single mental picture, and the picture is worth holding onto because it makes the result feel inevitable rather than clever.

Picture the set $\operatorname{Syl}_p(G)$ of all Sylow $p$-subgroups as a collection of dots. The group $G$ acts on this collection by conjugation: an element $g$ sends the dot $P$ to the dot $gPg^{-1}$. The crucial fact — and it is *all* of [[Thm - Sylow's Theorems|Sylow II]] one needs here — is that this action *stays inside the collection*: conjugating a Sylow $p$-subgroup yields a subgroup of the same order $p^a$, which is again a Sylow $p$-subgroup. Conjugation never produces a dot outside $\operatorname{Syl}_p(G)$; it only shuffles the dots among themselves.

Now suppose there is only *one* dot. A shuffle of a one-element collection is forced: the lone dot can only be sent to itself. So conjugation by *every* $g \in G$ fixes $P$, meaning $gPg^{-1} = P$ for all $g$ — and that equation, holding for all $g$, is exactly the definition of $P$ being [[Def - Normal Subgroup|normal]]. There is simply no other dot for $g$ to send $P$ to. Uniqueness removes all the freedom conjugation might have had.

This is why the theorem needs nothing beyond Sylow II. The substantive input — that a conjugate of a Sylow $p$-subgroup is again a Sylow $p$-subgroup — is what confines the conjugation action to the set $\operatorname{Syl}_p(G)$. Once you grant that confinement, the rest is the trivial observation that a set with one element has only the identity permutation. The theorem is the meeting of one genuine fact (Sylow II) and one triviality (a singleton has no non-trivial self-maps), and the genuine fact is doing all the work.

It is worth noticing the converse is just as transparent. If $P$ is normal, $gPg^{-1} = P$ for all $g$, so the conjugation action fixes $P$; but by Sylow II every Sylow $p$-subgroup is a conjugate of $P$, and every conjugate of $P$ is $P$ itself — so $P$ is the *only* Sylow $p$-subgroup, $n_p = 1$. Normality and uniqueness are two descriptions of the same situation: the conjugation action on $\operatorname{Syl}_p(G)$ has a fixed point that is also the whole set.

---

# What Makes This Hard

There is almost nothing hard in the proof itself — the difficulty is entirely in *remembering to use it* and in not over-claiming. The one genuine subtlety is that the result rests silently on [[Thm - Sylow's Theorems|Sylow II]]: the reason a conjugate $gPg^{-1}$ is again a Sylow $p$-subgroup is that conjugation preserves order, and one must not skip the remark that $|gPg^{-1}| = |P| = p^a$. The most common error is the *converse over-claim* — concluding that a normal Sylow $p$-subgroup makes $G$ a [[Def - Direct Product|direct product]]; it does not, unless *every* Sylow subgroup is normal, and $S_3$ (normal $C_3$, non-normal $C_2$) is the standing counterexample.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Conjugation by any $g \in G$ sends a Sylow $p$-subgroup to a subgroup of the same order, which by [[Thm - Sylow's Theorems|Sylow II]] is again a Sylow $p$-subgroup. If there is only one Sylow $p$-subgroup, conjugation must send it to itself — and being fixed by all conjugations is the definition of normal.

**Subgoal decomposition:**

1. **A conjugate of a Sylow $p$-subgroup is a Sylow $p$-subgroup.** For $P$ with $|P| = p^a$ and any $g \in G$, show $gPg^{-1}$ is a subgroup of order $p^a$.
   - *Hint:* Conjugation $x \mapsto gxg^{-1}$ is an isomorphism of $G$ onto itself, so it sends subgroups to subgroups and preserves order; $|gPg^{-1}| = |P| = p^a$.
   - *Why needed:* It places $gPg^{-1}$ back in $\operatorname{Syl}_p(G)$, so uniqueness can be applied to it.

2. **Uniqueness forces $gPg^{-1} = P$.** Assume $n_p = 1$, so $P$ is the only Sylow $p$-subgroup; conclude $gPg^{-1} = P$ for every $g$.
   - *Hint:* By step 1, $gPg^{-1} \in \operatorname{Syl}_p(G)$; since $\operatorname{Syl}_p(G) = \{P\}$ has one element, $gPg^{-1}$ must equal $P$.
   - *Why needed:* This is the equation defining normality.

3. **Conclude normality.** Note $gPg^{-1} = P$ for all $g \in G$ is exactly $P \trianglelefteq G$.
   - *Hint:* This is the definition of a [[Def - Normal Subgroup|normal subgroup]].
   - *Why needed:* This is the statement.

4. **(Converse.)** If $P \trianglelefteq G$, show $n_p = 1$.
   - *Hint:* By [[Thm - Sylow's Theorems|Sylow II]] every Sylow $p$-subgroup is a conjugate $gPg^{-1}$; normality gives $gPg^{-1} = P$, so $P$ is the only one.
   - *Why needed:* It establishes the "if and only if".

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

> [!note]- Lemma 1: Conjugation preserves the property of being a Sylow $p$-subgroup
> **Statement:** Let $P$ be a [[Def - Sylow p-Subgroup|Sylow $p$-subgroup]] of $G$ and let $g \in G$. Then the conjugate $gPg^{-1}$ is also a Sylow $p$-subgroup of $G$.
>
> **Hint:** The map $c_g : x \mapsto gxg^{-1}$ is an automorphism of $G$; automorphisms carry subgroups to subgroups of equal order.
>
> **Why needed:** It is the one substantive input — it confines the conjugation action of $G$ to the set $\operatorname{Syl}_p(G)$, which is what makes uniqueness bite.
>
> > [!note]- Full proof
> > The map $c_g : G \to G$, $c_g(x) = gxg^{-1}$, is a homomorphism — $c_g(xy) = gxyg^{-1} = (gxg^{-1})(gyg^{-1}) = c_g(x)c_g(y)$ — and it is a bijection with inverse $c_{g^{-1}}$, so it is an automorphism of $G$. An automorphism sends subgroups to subgroups, so $c_g(P) = gPg^{-1}$ is a subgroup of $G$; and being a bijection it preserves cardinality, so $|gPg^{-1}| = |P| = p^a$. A subgroup of order $p^a$ in a group of order $p^a m$ is by definition a Sylow $p$-subgroup. Hence $gPg^{-1} \in \operatorname{Syl}_p(G)$.

> [!note]- Lemma 2: A normal subgroup equals its conjugacy class of subgroups
> **Statement:** A subgroup $N \leq G$ is [[Def - Normal Subgroup|normal]] if and only if $gNg^{-1} = N$ for every $g \in G$ — equivalently, $N$ is the only member of its conjugacy class $\{gNg^{-1} : g \in G\}$ of subgroups.
>
> **Hint:** This is the definition of normal, restated as a statement about the orbit of $N$ under the conjugation action of $G$ on its set of subgroups.
>
> **Why needed:** It is the dictionary entry translating "the conjugation orbit of $P$ is a single point" into "$P$ is normal", used in both directions of the theorem.
>
> > [!note]- Full proof
> > By definition $N \trianglelefteq G$ means $gNg^{-1} = N$ for all $g \in G$. The conjugates $gNg^{-1}$ as $g$ ranges over $G$ form the orbit of $N$ under the action of $G$ on the set of its subgroups by conjugation. To say every $gNg^{-1}$ equals $N$ is exactly to say this orbit is the single point $\{N\}$ — i.e. $N$ is the only member of its conjugacy class of subgroups. Conversely, if the orbit is $\{N\}$ then $gNg^{-1} = N$ for all $g$, which is normality.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $G$ be a finite group, $p$ a prime, $|G| = p^a m$ with $p \nmid m$. If $n_p = 1$ — that is, if $G$ has a unique [[Def - Sylow p-Subgroup|Sylow $p$-subgroup]] $P$ — then $P \trianglelefteq G$. Conversely, if a Sylow $p$-subgroup is normal then $n_p = 1$.
>
> *Proof (of the main statement).* Let $P$ be the unique Sylow $p$-subgroup of $G$, so $|P| = p^a$, and let $g \in G$ be arbitrary. Consider the conjugate subgroup $g^{-1}Pg$.
>
> Conjugation by $g$ is an automorphism of $G$ — it is a bijective homomorphism — so $g^{-1}Pg$ is a subgroup of $G$, and it has the same order as $P$:
> $$|g^{-1}Pg| = |P| = p^a.$$
> A subgroup of order $p^a$ is a Sylow $p$-subgroup. Hence $g^{-1}Pg \in \operatorname{Syl}_p(G)$.
>
> But $G$ has only one Sylow $p$-subgroup, namely $P$; that is, $\operatorname{Syl}_p(G) = \{P\}$. Since $g^{-1}Pg$ is a member of this one-element set, we must have
> $$g^{-1}Pg = P.$$
> This holds for every $g \in G$. By the definition of a [[Def - Normal Subgroup|normal subgroup]], $P \trianglelefteq G$. $\quad\blacksquare$
>
> *Proof (of the converse).* Suppose a Sylow $p$-subgroup $P$ satisfies $P \trianglelefteq G$, so $g^{-1}Pg = P$ for all $g \in G$. Let $P'$ be any Sylow $p$-subgroup of $G$. By [[Thm - Sylow's Theorems|Sylow's second theorem]], all Sylow $p$-subgroups are conjugate, so $P' = g^{-1}Pg$ for some $g \in G$. By normality $g^{-1}Pg = P$, hence $P' = P$. So $P$ is the only Sylow $p$-subgroup, and $n_p = 1$. $\quad\blacksquare$
>
> This is the lemma proved in §1.7 of the source lecture notes, immediately after the statement of Sylow's theorems.

---

# Cross-Field Exercise Suggestions

The aim is to find settings where the theorem applies but is not advertised — to battle-test recognition of the *sources*. Almost every application is an instance of the **non-simplicity playbook**: force some $n_p = 1$ using $n_p \equiv 1 \pmod p$ and $n_p \mid m$, then this theorem hands you a normal subgroup.

**The non-simplicity playbook itself: orders that die at the first step.** Given an integer $n$, the most common exercise is "show every group of order $n$ is not [[Def - Simple Group|simple]]". The first move is always the same: factor $n = p^a m$ and, for each prime, intersect the divisors of $m$ with the residue class $1 \pmod p$. For a startling range of $n$ — $15, 20, 33, 35, 100, 200, 1000$ — some prime is left with $n_p = 1$ as the *only* admissible value, and this theorem instantly produces a normal Sylow subgroup. The application is non-obvious in that the problem mentions no subgroup at all; property $B$, "$|G| = n$ with a divisor structure forcing $n_p = 1$", is the bridge to the hypothesis. Worked example: $|G| = 1000 = 2^3 \cdot 5^3$, take $p = 5$, the divisors of $8$ that are $\equiv 1 \pmod 5$ are just $\{1\}$, so $n_5 = 1$ and the Sylow $5$-subgroup is normal.

**Orders that need a second tactic before this theorem applies.** Sometimes the first arithmetic pass leaves several admissible $n_p$, and a secondary argument — element-counting, or an action $G \to S_{n_p}$ — eliminates all but $n_p = 1$. For $|G| = 132 = 2^2 \cdot 3 \cdot 11$, assuming $G$ simple forces $n_{11} = 12$ and $n_3 = 22$; but $12$ Sylow $11$-subgroups contribute $12 \cdot 10 = 120$ elements of order $11$ and $22$ Sylow $3$-subgroups contribute $22 \cdot 2 = 44$ elements of order $3$, totalling $164 > 132$ — a contradiction, so some $n_p = 1$ after all, and this theorem closes the argument. The application is non-obvious because the theorem is the *last* step of a multi-stage proof; one reaches it only after the counting contradiction has done its work.

**Geometry: symmetry groups of polytopes and tilings.** The rotation group of a polytope or the symmetry group of a periodic tiling is a finite group; asking whether it is simple, or extracting a normal subgroup of symmetries, routes through this theorem once the order is factored. For a symmetry group of order $2^a m$ with $m$ small, a forced $n_2 = 1$ yields a normal Sylow $2$-subgroup — a distinguished family of symmetries invariant under the whole group. The application is non-obvious because the input is a geometric object and the normal subgroup emerges as a by-product of pure arithmetic on the order.

**Number theory and Galois theory: solvability via normal Sylow towers.** A finite group with a normal Sylow $p$-subgroup for *every* prime is the [[Def - Direct Product|direct product]] of those subgroups, hence nilpotent, hence solvable. When this theorem can be applied at every prime dividing $|G|$, the group is solvable, and via the Galois correspondence a polynomial with such a Galois group is soluble by radicals. The application is non-obvious because "solvable by radicals" is a statement about field extensions and root formulas, while the route to it is a sequence of Sylow counts each forced to equal $1$.

---

# Bridges

- **[[Thm - Sylow's Theorems|Sylow's theorems]]** — this theorem is the immediate corollary of Sylow II (conjugacy): a conjugate of a Sylow $p$-subgroup is again one, so a unique Sylow $p$-subgroup is conjugation-invariant. It is also the consumer of Sylow III (the count): Sylow III supplies the arithmetic that forces $n_p = 1$, and this theorem converts that into normality. The three Sylow theorems plus this corollary are the complete toolkit for non-[[Def - Simple Group|simplicity]].

- **[[Def - Simple Group|Simple groups]]** — the theorem is the primary engine for proving a group of given order is *not* simple. A simple group has no proper non-trivial [[Def - Normal Subgroup|normal subgroup]]; this theorem produces exactly such a subgroup whenever some $n_p$ is forced to $1$ and $|G|$ is not a prime power. Every "no simple group of order $n$" exercise that is settled by arithmetic alone is settled by this theorem.

- **[[Thm - p-Groups Have Non-Trivial Centre|$p$-groups have non-trivial centre]]** — a complementary non-simplicity tool for the *other* case. When $|G|$ is itself a prime power, there are no Sylow subgroup constraints to exploit (the group is its own Sylow $p$-subgroup); instead the non-trivial centre supplies the normal subgroup. Between them, the two results cover non-simplicity for prime-power orders and for orders with several prime factors.

- **[[Thm - First Isomorphism Theorem|First isomorphism theorem]]** — when this theorem yields a normal Sylow $p$-subgroup $P$, the quotient $G/P$ becomes available, and the first isomorphism theorem and the [[Def - Direct Product|direct product]] / semidirect product machinery turn $P \trianglelefteq G$ into a structural decomposition of $G$. Normality is the gateway to quotients, and quotients are where classification proceeds.

- **The semidirect product, and the contrast with direct products** — a single normal Sylow subgroup gives only a *semidirect* product $G = P \rtimes H$, not a direct product; $G$ is a direct product of its Sylow subgroups precisely when *every* Sylow subgroup is normal. The smallest cautionary example is $S_3$: its Sylow $3$-subgroup $C_3$ is normal but its Sylow $2$-subgroups are not, so $S_3$ is $C_3 \rtimes C_2$ and not $C_3 \times C_2 = C_6$.

---

# Unlocked by This

> [!tip] The Non-Simplicity Playbook *(from §1.7 exercises)*
> This theorem is the final move of the standard playbook: factor $|G| = p^a m$, list the $n_p$ permitted by [[Thm - Sylow's Theorems|Sylow III]]'s constraints $n_p \equiv 1 \pmod p$ and $n_p \mid m$, force some $n_p = 1$ — directly, by element-counting, or via an action $G \to S_{n_p}$ — and this theorem converts that $1$ into a proper normal subgroup, proving $G$ is not [[Def - Simple Group|simple]].

> [!tip] Nilpotent Groups and Sylow Towers *(from Galois Theory)*
> When this theorem applies at *every* prime dividing $|G|$, the group is the [[Def - Direct Product|direct product]] of its Sylow subgroups — the elementary characterisation of a **nilpotent** finite group. Nilpotent groups are solvable, and solvability of a Galois group is what decides solubility of a polynomial by radicals.

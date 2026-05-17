---
type: theorem
subject: group-theory
prereqs:
  - "Def - p-group"
  - "Def - Subgroup"
  - "Def - Normal Subgroup"
  - "Def - Quotient Group"
  - "Thm - p-Groups Have Non-Trivial Centre"
  - "Thm - Correspondence Theorem"
  - "Thm - Lagrange's Theorem"
  - "Def - Centraliser and Centre"
tags: [algebra, group-theory]
---

# Notation

$G$ is a finite group with identity $e$, and $p$ is a prime; $G$ is a [[Def - p-group|p-group]] when $|G| = p^a$ for some $a \geq 1$. We write $H \leq G$ for "$H$ is a [[Def - Subgroup|subgroup]]" and $N \trianglelefteq G$ for "$N$ is a [[Def - Normal Subgroup|normal subgroup]]". The **centre** $Z(G) = \{z : zg = gz \text{ for all } g\}$ is a normal subgroup (see [[Def - Centraliser and Centre]]). For $x \in G$, $\langle x \rangle$ is the cyclic subgroup it generates and $\operatorname{ord}(x)$ its order. The [[Def - Quotient Group|quotient]] $G/N$ is the group of cosets of a normal subgroup $N$. The [[Thm - Correspondence Theorem|correspondence theorem]] (also called the lattice or fourth isomorphism theorem) puts the subgroups of $G/N$ in inclusion-preserving bijection with the subgroups of $G$ containing $N$. The full registry is on [[Group Theory III — §1.5–1.7]].

---

# Statement

> **Theorem (subgroups of a $p$-group, of every order).** Let $G$ be a group of order $p^a$, where $p$ is prime and $a \geq 1$. Then for *every* exponent $b$ with $0 \leq b \leq a$, the group $G$ has a [[Def - Subgroup|subgroup]] of order $p^b$. Moreover such a subgroup can be chosen [[Def - Normal Subgroup|normal]] in $G$.

In words: a $p$-group has a (normal) subgroup of *every* order permitted by [[Thm - Lagrange's Theorem|Lagrange's theorem]] — the divisors of $|G| = p^a$ are exactly $p^0, p^1, \dots, p^a$, and every one of them is realised. This is the **converse of Lagrange's theorem, holding in full** for $p$-groups.

> **Warning (the converse of Lagrange fails for general groups).** For an arbitrary finite group, a divisor of $|G|$ need not be the order of any subgroup. The standard counterexample is the alternating group $A_5$, of order $60$: it has no subgroup of order $30$. (A subgroup of order $30$ would have index $2$, hence be normal, but $A_5$ is [[Def - Simple Group|simple]] and has no proper non-trivial normal subgroup.) Likewise $A_4$, of order $12$, has no subgroup of order $6$.

---

# Motivation

[[Thm - Lagrange's Theorem|Lagrange's theorem]] is a one-way street: it says the order of any subgroup *divides* $|G|$, but it never promises that a given divisor is *achieved*. The natural question — the converse — is "given a divisor $d$ of $|G|$, is there a subgroup of order $d$?" — and for general groups the honest answer is no. The alternating group $A_4$ has order $12$ and no subgroup of order $6$; $A_5$ has order $60$ and no subgroup of order $30$. So the converse of Lagrange is false, and one of the recurring themes of this chapter is *how much* of it can be rescued, and for which groups.

This theorem is the most satisfying rescue. It says: for $p$-groups, the converse of Lagrange holds **completely**. Not for some divisors, not for prime divisors only (that would be Cauchy's theorem), but for *every* divisor — and $p$-groups have a particularly simple divisor set, since the divisors of $p^a$ are exactly the chain $p^0 \mid p^1 \mid \cdots \mid p^a$. So a $p$-group has a subgroup of every order from $1$ up to $|G|$, with nothing skipped. And not merely a subgroup — a *normal* subgroup. The result is a complete answer to the existence question for an entire class of groups.

Why should one expect prime-power order to be the boundary at which the converse becomes true? Because the obstruction to the converse is the existence of [[Def - Simple Group|simple]] groups: a subgroup of index $2$ is automatically normal, and a simple group has no proper non-trivial normal subgroup, which is exactly why $A_5$ (simple) has no index-$2$ — i.e. order-$30$ — subgroup. But [[Thm - p-Groups Have Non-Trivial Centre|the previous theorem]] tells us $p$-groups are *never* simple (for $a \geq 2$): they always have a non-trivial centre, hence a normal subgroup. So $p$-groups are precisely the groups in which the simplicity obstruction is absent at every stage, and one should expect the converse of Lagrange to go through by induction — peel off a normal subgroup, descend to a smaller $p$-group, repeat. The non-trivial-centre theorem is what guarantees there is always a normal subgroup to peel off. This theorem is the cleanest demonstration that the rigidity of $p$-groups, sourced entirely from the class equation, has real constructive force: it builds subgroups, not just constrains them.

---

# Sources and Targets

This records the non-obvious ways a problem arrives at the hypothesis (a $p$-group) and the non-obvious uses of the conclusion (a normal subgroup of every order).

**Sources (Input Broadening)**

The hypothesis is "$G$ is a finite $p$-group". The skill is recognising it without the words.

The first source is **a group of explicitly prime-power order**. Property $B$ is "$|G| = p^a$", read off a factorisation: orders like $8, 16, 27, 81, 125$ are prime powers and trigger the theorem. The bridge is the definition itself. In practice a problem says "$|G| = 16$" and you must notice $16 = 2^4$.

The second source is **a Sylow $p$-subgroup of an arbitrary finite group**. Property $B$ is "$P$ is a [[Def - Sylow p-Subgroup|Sylow p-subgroup]] of a group $G$ of order $p^a m$". The bridge is $|P| = p^a$, so $P$ is a $p$-group and this theorem applies to $P$ even though $G$ is not a $p$-group. The non-obvious consequence: $G$ has a $p$-subgroup of *every* order $p^b$ for $0 \leq b \leq a$ — combine Sylow I (a Sylow subgroup $P$ exists) with this theorem (inside $P$, subgroups of every smaller prime-power order exist). This is precisely the part of the converse of Lagrange that *does* survive for general groups: subgroups of prime-power order, of every prime-power order dividing $|G|$, always exist. The implication is non-obvious because $G$ itself is not a prime-power group.

The third source is **a quotient of a $p$-group**. Property $B$ is "$G = K/N$ where $K$ is a $p$-group". The bridge is that $|K/N| = |K|/|N|$ is again a power of $p$, so the quotient is a $p$-group and the theorem applies to it. The non-obviousness is that the theorem is being applied inside an inductive argument — the smaller object $G/\langle x\rangle$ is the quotient to which one recurses.

**Targets (Output Amplification)**

The conclusion is "$G$ has a normal subgroup of every order $p^b$, $0 \leq b \leq a$". Combined with one further fact this becomes a stronger structural statement.

The first combination is **a full subgroup of every order plus an index-$p$ subgroup is normal gives a maximal subgroup that is normal**. The conclusion $C$ provides a subgroup $M$ of order $p^{a-1}$, of index $p$. Add property $D$: in a $p$-group every subgroup of index $p$ is in fact normal (a maximal subgroup of a $p$-group is always normal — this is itself a $p$-group fact). The result $E$ is that $G$ has a normal subgroup of index $p$, hence the quotient $G/M$ is cyclic of order $p$. Iterating, the result $E'$ is a **chief series** $\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_a = G$ with each $|G_{i+1}/G_i| = p$. The combination is non-obvious because it upgrades "subgroups of every order exist" to "they can be threaded into a single normal chain", which is what exhibits the $p$-group as solvable, indeed nilpotent.

The second combination is **subgroups of every order plus the contrast with $A_5$ delimits exactly where the converse of Lagrange holds**. The conclusion $C$ "$p$-groups realise every divisor" together with property $D$ "$A_5$ and $A_4$ fail to realise the divisors $30$ and $6$" gives the result $E$: the converse of Lagrange holds *precisely* for prime-power divisors — for a prime-power divisor of any $|G|$ a subgroup exists (via Sylow plus this theorem), for a non-prime-power divisor it may fail. The combination is non-obvious because it is a *sharp boundary* statement: knowing both the positive theorem and the negative counterexample tells you exactly which existence questions have guaranteed answers.

The third combination is **a normal subgroup of order $p^{a-1}$ plus the correspondence theorem catalogues all maximal subgroups**. The conclusion $C$ gives normal subgroups; via the [[Thm - Correspondence Theorem|correspondence theorem]] the subgroups of $G$ of order $p^{a-1}$ correspond to subgroups of order $p$ in $G/[\text{something}]$, organising the maximal-subgroup structure. The result $E$ is structural bookkeeping: the lattice of subgroups of a $p$-group is "graded" by order, with each level non-empty. This is non-obvious because Lagrange alone would leave open whether intermediate levels are populated.

---

# Why Is It True

The intuition is *peeling*. A $p$-group is rigid enough that you can always shave one prime $p$ off its order in a controlled way — pass to a quotient that is a smaller $p$-group — and intermediate-order subgroups are built by peeling down and then climbing back up.

Here is the picture. Suppose you want a subgroup of order $p^b$ inside a group $G$ of order $p^a$. The previous theorem, [[Thm - p-Groups Have Non-Trivial Centre|p-groups have non-trivial centre]], guarantees there is a non-identity *central* element, and from it you can extract a central element $x$ of order exactly $p$ (take a suitable power). Because $x$ is central, the cyclic subgroup $\langle x \rangle \cong C_p$ it generates is automatically **normal** — conjugation fixes central elements, so it fixes the subgroup they generate. So you have, for free, a normal subgroup of order $p$.

Now quotient. The group $G/\langle x \rangle$ has order $p^a / p = p^{a-1}$ — it is a *smaller* $p$-group. This is the peeling step: you have shaved exactly one factor of $p$ off, in a way that produced a genuine smaller group of the same kind. Genuinely smaller and genuinely the same kind — that is exactly the setup for **induction**. By the inductive hypothesis, the smaller $p$-group $G/\langle x \rangle$ already has a subgroup of every order it should, in particular one of order $p^{b-1}$.

The last move is climbing back up. A subgroup of $G/\langle x \rangle$ is not literally a subgroup of $G$ — it lives in the quotient — but the [[Thm - Correspondence Theorem|correspondence theorem]] says subgroups of $G/\langle x\rangle$ correspond *exactly* to subgroups of $G$ that contain $\langle x \rangle$, and the correspondence multiplies orders by $|\langle x \rangle| = p$. So a subgroup of order $p^{b-1}$ in the quotient *lifts* to a subgroup of order $p^{b-1} \cdot p = p^b$ in $G$. You wanted $p^b$; you got $p^b$.

So the whole theorem is: *peel off a central $C_p$, recurse on the smaller $p$-group, lift the answer back up the correspondence*. The reason to expect this to work is that each ingredient is exactly what a $p$-group guarantees and a general group does not. A general group might have no normal subgroup to quotient by — it could be simple — and then the peeling step is impossible; that is exactly what goes wrong for $A_5$. A $p$-group always has a normal subgroup, and not just any normal subgroup but a *central* $C_p$, which is the cleanest possible thing to quotient by because its order is the single prime $p$ — peeling one prime at a time matches the divisor chain $p^0 \mid p^1 \mid \cdots \mid p^a$ perfectly. The rigidity of $p$-groups, traced all the way back to the class equation, is precisely the property that makes the peel-recurse-lift loop never get stuck. That is why the converse of Lagrange holds for $p$-groups and fails in general: $p$-groups can always be peeled, simple groups cannot.

---

# What Makes This Hard

The proof is an induction and the step people get wrong is the *lift*: a subgroup $L$ of order $p^{b-1}$ in the quotient $G/\langle x\rangle$ is not a subgroup of $G$, and you must invoke the [[Thm - Correspondence Theorem|correspondence theorem]] to pull it back to a subgroup $K \leq G$ with $K/\langle x\rangle = L$, whence $|K| = |L| \cdot |\langle x\rangle| = p^{b-1} \cdot p = p^b$. The most common error is forgetting to ensure the chosen element $x$ is *central* — if $x$ is merely some element of order $p$ (as Cauchy would give), $\langle x \rangle$ need not be normal, the quotient $G/\langle x\rangle$ is not even defined, and the whole induction collapses. A secondary slip is mishandling the base case $b = 0$ (the trivial subgroup, order $p^0 = 1$) or $a = 1$, where the only subgroups are $\{e\}$ and $G$ themselves.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Induct on $a$, the exponent in $|G| = p^a$. To build a subgroup of order $p^b$: use the non-trivial centre to extract a central element of order $p$, generating a *normal* $C_p$; quotient by it to get a strictly smaller $p$-group of order $p^{a-1}$; apply the inductive hypothesis to get a subgroup of order $p^{b-1}$ there; lift it through the correspondence theorem to a subgroup of order $p^b$ in $G$.

**Subgoal decomposition:**

1. **Base case.** Verify the claim for $a = 1$ (and the trivial case $b = 0$ for all $a$).
   - *Hint:* For $a = 1$ the only orders to realise are $p^0$ and $p^1$, given by $\{e\}$ and $G$. For any $a$, the order $p^0 = 1$ is given by $\{e\}$.
   - *Why needed:* It anchors the induction and handles the degenerate exponents the inductive step does not cover.

2. **Produce a central element of order $p$.** For $a > 1$ and $b \geq 1$, find $x \in Z(G)$ with $\operatorname{ord}(x) = p$.
   - *Hint:* By [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial-centre theorem]] there is a non-identity $z \in Z(G)$; its order is a power of $p$, say $p^c$, and then $x = z^{p^{c-1}}$ has order exactly $p$ and is still central.
   - *Why needed:* $x$ central makes $\langle x \rangle$ normal — the only kind of subgroup you may quotient by.

3. **Form the normal $C_p$ and the smaller quotient.** Show $\langle x \rangle \trianglelefteq G$ and $|G/\langle x \rangle| = p^{a-1}$.
   - *Hint:* A subgroup generated by a central element is normal because conjugation fixes $x$, hence fixes every power of $x$; the order of the quotient is $|G|/|\langle x\rangle| = p^a/p$.
   - *Why needed:* It manufactures the strictly smaller $p$-group on which to recurse.

4. **Apply the inductive hypothesis and lift.** Get a subgroup $L \leq G/\langle x\rangle$ of order $p^{b-1}$, then lift to $K \leq G$ of order $p^b$.
   - *Hint:* The inductive hypothesis applies since $G/\langle x\rangle$ has order $p^{a-1} < p^a$. The [[Thm - Correspondence Theorem|correspondence theorem]] gives a unique $K$ with $\langle x\rangle \leq K \leq G$ and $K/\langle x\rangle = L$, so $|K| = |L|\cdot|\langle x\rangle| = p^{b-1}\cdot p = p^b$.
   - *Why needed:* This is the construction of the desired subgroup; the order arithmetic is the payoff.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

> [!note]- Lemma 1: A central element of order $p$ exists in any non-trivial $p$-group
> **Statement:** If $G$ is a $p$-group of order $p^a$ with $a \geq 1$, there is an element $x \in Z(G)$ with $\operatorname{ord}(x) = p$.
>
> **Hint:** Take a non-identity central element from the previous theorem; its order is a $p$-power $p^c$; raise it to the power $p^{c-1}$.
>
> **Why needed:** It supplies the central — hence normality-guaranteeing — element of order exactly $p$ that the induction quotients by.
>
> > [!note]- Full proof
> > By [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial-centre theorem]], $Z(G) \neq \{e\}$, so choose $z \in Z(G)$ with $z \neq e$. By [[Thm - Lagrange's Theorem|Lagrange]], $\operatorname{ord}(z)$ divides $|G| = p^a$, so $\operatorname{ord}(z) = p^c$ for some $c \geq 1$ (as $z \neq e$). Set $x = z^{p^{c-1}}$. Then $x^p = z^{p^c} = e$, and $x \neq e$ since $p^{c-1} < p^c = \operatorname{ord}(z)$; so $\operatorname{ord}(x) = p$. Finally $x$ is a power of the central element $z$, and powers of central elements are central, so $x \in Z(G)$.

> [!note]- Lemma 2: A subgroup generated by a central element is normal
> **Statement:** If $x \in Z(G)$, then $\langle x \rangle \trianglelefteq G$.
>
> **Hint:** Conjugation fixes $x$, so it fixes every power of $x$.
>
> **Why needed:** Normality of $\langle x\rangle$ is what makes the quotient $G/\langle x\rangle$ a group — without it the inductive step has nothing to descend to.
>
> > [!note]- Full proof
> > For any $g \in G$ and any power $x^k$, since $x$ is central $gx^k g^{-1} = x^k g g^{-1} = x^k \in \langle x\rangle$. So $g\langle x\rangle g^{-1} \subseteq \langle x\rangle$ for every $g$, which is the definition of $\langle x\rangle$ being [[Def - Normal Subgroup|normal]] in $G$. (In fact every subgroup of $Z(G)$ is normal in $G$, by the identical argument.)

> [!note]- Lemma 3: Lifting a subgroup through the correspondence theorem multiplies its order by $|N|$
> **Statement:** Let $N \trianglelefteq G$ and let $L \leq G/N$. Then there is a unique subgroup $K$ with $N \leq K \leq G$ and $K/N = L$, and $|K| = |L| \cdot |N|$.
>
> **Hint:** $K$ is the union of the cosets of $N$ that constitute $L$; count.
>
> **Why needed:** It converts the inductive hypothesis's subgroup-in-the-quotient into an honest subgroup of $G$ of the desired order.
>
> > [!note]- Full proof
> > By the [[Thm - Correspondence Theorem|correspondence theorem]], the subgroups of $G/N$ are exactly the sets $K/N$ for subgroups $K$ with $N \leq K \leq G$, and this correspondence $K \leftrightarrow K/N$ is a bijection. So there is a unique $K$ with $N \leq K \leq G$ and $K/N = L$. For the order: $K$ is partitioned into the cosets of $N$ it contains, and the cosets of $N$ lying inside $K$ are precisely the elements of $K/N = L$. So $K$ is a disjoint union of $|L|$ cosets, each of size $|N|$, giving $|K| = |L| \cdot |N|$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $G$ be a group of order $p^a$, $p$ prime, $a \geq 1$. Then for every $0 \leq b \leq a$, $G$ has a normal subgroup of order $p^b$.
>
> *Proof.* We induct on $a$.
>
> **Base case $a = 1$.** Here $|G| = p$. The orders to realise are $p^0 = 1$ and $p^1 = p$. The trivial subgroup $\{e\}$ has order $p^0$ and is normal; $G$ itself has order $p^1$ and is normal in itself. So the claim holds for $a = 1$.
>
> **Inductive step.** Let $a > 1$, and assume the theorem holds for all $p$-groups of order $p^{a'}$ with $a' < a$. Let $|G| = p^a$, and fix $b$ with $0 \leq b \leq a$.
>
> If $b = 0$, the trivial subgroup $\{e\}$ has order $p^0 = 1$ and is normal; done. So assume $b \geq 1$.
>
> By [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial-centre theorem]], $Z(G) \neq \{e\}$. Pick $z \in Z(G)$ with $z \neq e$. By [[Thm - Lagrange's Theorem|Lagrange's theorem]], $\operatorname{ord}(z)$ divides $p^a$, so $\operatorname{ord}(z) = p^c$ for some $c \geq 1$. Put $x = z^{p^{c-1}}$; then $x^p = z^{p^c} = e$ and $x \neq e$, so $\operatorname{ord}(x) = p$, and $x$ is a power of the central element $z$, hence central.
>
> Since $x$ is central, $\langle x \rangle \trianglelefteq G$: for any $g \in G$ and any power $x^k$, $gx^kg^{-1} = x^k \in \langle x\rangle$. The subgroup $\langle x \rangle$ has order $p$ (it is cyclic of order $\operatorname{ord}(x) = p$). Therefore the [[Def - Quotient Group|quotient]] $G/\langle x\rangle$ is a group of order
> $$|G/\langle x\rangle| = \frac{|G|}{|\langle x\rangle|} = \frac{p^a}{p} = p^{a-1}.$$
>
> This is a $p$-group of order $p^{a-1}$ with $a - 1 < a$, so the inductive hypothesis applies to it. Since $1 \leq b \leq a$, we have $0 \leq b - 1 \leq a - 1$, so the inductive hypothesis gives a subgroup $L \leq G/\langle x\rangle$ of order $p^{b-1}$.
>
> By the [[Thm - Correspondence Theorem|correspondence theorem]], there is a (unique) subgroup $K$ with $\langle x\rangle \leq K \leq G$ and $K/\langle x\rangle = L$. The subgroup $K$ is the disjoint union of the cosets of $\langle x\rangle$ comprising $L$, so
> $$|K| = |L| \cdot |\langle x\rangle| = p^{b-1} \cdot p = p^b.$$
>
> Thus $K$ is a subgroup of $G$ of order $p^b$, completing the induction.
>
> (For normality of $K$: the inductive hypothesis can be taken to deliver $L$ *normal* in $G/\langle x\rangle$; the correspondence theorem then makes the corresponding $K$ normal in $G$, since the correspondence carries normal subgroups to normal subgroups. Hence the subgroup of order $p^b$ may be chosen normal in $G$.) $\qquad\blacksquare$
>
> **Contrast.** The converse of Lagrange fails for general groups: $A_5$ has order $60$ but no subgroup of order $30$. Such a subgroup would have index $2$ and so be normal; but $A_5$ is [[Def - Simple Group|simple]], with no proper non-trivial normal subgroup, a contradiction. Similarly $A_4$, order $12$, has no subgroup of order $6$. The theorem above is special to $p$-groups precisely because $p$-groups, by the non-trivial-centre theorem, always supply the normal subgroup the induction needs — a simple group supplies none.

---

# Cross-Field Exercise Suggestions

The aim is to find settings where the theorem applies but is not advertised — testing recognition of the *sources*.

**General finite groups: subgroups of every prime-power order always exist.** Take any finite group $G$, of order $n = p_1^{a_1} \cdots p_k^{a_k}$, with no prime-power structure assumed. For each prime $p_i$, [[Thm - Sylow's Theorems|Sylow I]] gives a [[Def - Sylow p-Subgroup|Sylow pᵢ-subgroup]] $P_i$ of order $p_i^{a_i}$, and this theorem, applied *inside* the $p_i$-group $P_i$, produces subgroups of $P_i$ — hence of $G$ — of every order $p_i^{b}$, $0 \leq b \leq a_i$. So although the full converse of Lagrange fails, the *prime-power part* of it always holds: a group of order $n$ has a subgroup of order $p^b$ for every prime power $p^b \mid n$. The application is non-obvious because $G$ is not a $p$-group; the source is "restrict to a Sylow subgroup, where this theorem lives".

**Solvability: every $p$-group has a chief series with cyclic factors.** Iterating this theorem (in its normal-subgroup form) threads $G$ into a chain $\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_a = G$ with $|G_i| = p^i$, so each factor $G_{i+1}/G_i$ has order $p$ and is cyclic. This exhibits every finite $p$-group as **solvable** — indeed nilpotent — which is the input to the Galois-theoretic statement that a polynomial with $p$-group Galois group is soluble by radicals. The application is non-obvious because "solvable" is a Galois-theory word; the bridge is that this theorem builds the very normal chain solvability requires.

**Linear algebra: flags inside the unitriangular group.** The unitriangular group $U_n(\mathbb{Z}/p)$ — upper-triangular matrices over $\mathbb{Z}/p$ with $1$s on the diagonal — is a $p$-group of order $p^{\binom n2}$, so it has subgroups of every intermediate prime-power order. These subgroups can be realised concretely as stabilisers of partial flags of subspaces, and the theorem guarantees the chain of orders is unbroken. The application is non-obvious because the natural language is geometric (flags, subspaces) while the theorem is a counting statement about abstract subgroups; the source is the order count $p^{\binom n 2}$.

---

# Bridges

- **[[Thm - Lagrange's Theorem|Lagrange's Theorem]]** — this theorem is the *converse* of Lagrange, valid for $p$-groups. Lagrange says subgroup order divides $|G|$; this says, for $p$-groups, every divisor is achieved. Together they make the subgroup-order question for $p$-groups completely transparent: the orders of subgroups of a group of order $p^a$ are *exactly* $p^0, p^1, \dots, p^a$, no more (Lagrange) and no fewer (this theorem).

- **[[Thm - p-Groups Have Non-Trivial Centre|p-Groups Have Non-Trivial Centre]]** — the engine of the inductive step. The non-trivial centre is what guarantees, at every stage of the induction, a *central* element of order $p$ and hence a *normal* $C_p$ to quotient by. Without it the peeling step is impossible. This theorem is essentially "the non-trivial-centre theorem, iterated".

- **[[Thm - Correspondence Theorem|Correspondence Theorem]]** — the lifting tool. The induction produces a subgroup in the quotient $G/\langle x\rangle$; the correspondence theorem is what turns it back into a subgroup of $G$, multiplying the order by $|\langle x\rangle| = p$. The whole proof is "descend by quotienting, ascend by the correspondence theorem".

- **Cauchy's theorem** *(from [[Group Theory II — §1.3–1.4]])* — Cauchy is the special case $b = 1$, but *only* for a prime divisor and *only* asserting an element (hence a subgroup) of that prime order. This theorem is far stronger for $p$-groups: it gives subgroups of every prime-power order, not just order $p$, and they can be taken normal. Conversely Cauchy is more general in that it applies to *any* finite group, not only $p$-groups — it is the fragment of the converse of Lagrange that survives universally.

- **The converse of Lagrange, and its failure** — the theorem is the positive half of a sharp dichotomy. The negative half is that the converse of Lagrange is *false* in general: $A_5$ (order $60$) has no subgroup of order $30$, $A_4$ (order $12$) has none of order $6$. The obstruction is [[Def - Simple Group|simplicity]] — and $p$-groups are exactly the groups whose non-trivial centre rules simplicity out at every stage. The precise statement of where the converse holds: for a prime-power divisor of any $|G|$, always (via Sylow plus this theorem); for an arbitrary divisor, not necessarily.

# Unlocked by This

> [!tip] Nilpotent Groups and Chief Series *(from Group Theory)*
> The iterated form of this theorem produces a **central series** of normal subgroups $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_a = G$ with each quotient $G_{i+1}/G_i$ cyclic of order $p$. This is exactly the data exhibiting a finite $p$-group as **nilpotent**. Nilpotence is the structural notion under which a finite group is the [[Def - Direct Product|direct product]] of its Sylow $p$-subgroups, and it is the property that makes $p$-groups the tractable "layered" subclass of all finite groups.

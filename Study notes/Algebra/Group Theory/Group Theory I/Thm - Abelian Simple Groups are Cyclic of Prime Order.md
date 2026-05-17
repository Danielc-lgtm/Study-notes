---
type: theorem
subject: group-theory
prereqs:
  - "Def - Abelian Group"
  - "Def - Subgroup"
  - "Def - Normal Subgroup"
  - "Def - Simple Group"
  - "Def - Order of a Group and of an Element"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a group, written multiplicatively, with identity $e$. It is [[Def - Abelian Group|abelian]] if $ab = ba$ for all $a, b \in G$. A [[Def - Simple Group|simple group]] is a non-trivial group whose only [[Def - Normal Subgroup|normal subgroups]] are $\{e\}$ and itself. The cyclic group of order $n$ is $C_n$; for a prime $p$, $C_p$ is the cyclic group of order $p$. For $g \in G$, $\langle g \rangle = \{g^n : n \in \mathbb{Z}\}$ is the cyclic subgroup it generates, and $\operatorname{ord}(g)$ is its [[Def - Order of a Group and of an Element|order]]. The symbol $\cong$ denotes [[Def - Isomorphism|isomorphism]]. The full registry is on the parent page [[Group Theory I — §1.1–1.2]].

---

# Statement

> **Classification of Abelian Simple Groups.** An abelian group $G$ is simple if and only if $G \cong C_p$ for some prime number $p$.

---

# Motivation

A [[Def - Simple Group|simple group]] is a group that cannot be broken apart — it has no normal subgroup to quotient by, hence no non-trivial quotient. Simple groups are the *atoms* of finite group theory: every finite group is assembled from them, as the [[Thm - Composition Series|composition series]] makes precise. So a basic question is: what *are* the simple groups?

In full generality this question is monstrous — its answer is the Classification of Finite Simple Groups, a theorem running to thousands of pages, listing the cyclic groups of prime order, the alternating groups $A_n$ for $n \geq 5$, sixteen infinite families of groups of Lie type, and twenty-six sporadic groups. But restrict attention to *abelian* groups and the question becomes elementary, and this theorem settles it completely: the abelian simple groups are exactly the cyclic groups $C_p$ of prime order, and nothing else.

This matters for two reasons. First, it is the one corner of the classification you can prove in a paragraph, and it tells you the abelian composition factors of any group are cyclic of prime order — so when a finite group is solvable, its composition factors are *precisely* the groups $C_p$. Second, it pins down what "simple" means in the friendliest setting and shows the answer is the most familiar groups imaginable. The cyclic groups of prime order are the abelian atoms; the substance and difficulty of the classification lies entirely in the *non-abelian* simple groups.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem characterises abelian simple groups. The disguised-source question is: what hypotheses force a group to be both abelian and simple, so that the theorem applies and pins it down as $C_p$?

The first source is **a group of prime order $p$**. By [[Thm - Lagrange's Theorem|Lagrange's theorem]] such a group has no proper non-trivial subgroup, hence none normal, so it is simple; and a group of prime order is automatically cyclic, hence abelian. The non-obvious step is that "$|G| = p$" alone — a single arithmetic fact — forces both abelianness and simplicity, so the theorem's hypotheses are met for free. *Example problem:* show every group of order $7$ is simple and abelian, hence $\cong C_7$.

The second source is **a minimal normal subgroup of a solvable group**. In a finite solvable group $G$, a minimal non-trivial normal subgroup $N$ turns out to be abelian (because the derived subgroup of $N$ is characteristic in $N$, hence normal in $G$, hence trivial by minimality). If $N$ is moreover *characteristically simple* it is a product of copies of a simple group; in the abelian case the theorem forces those factors to be $C_p$. The non-obviousness is that minimality plus solvability secretly delivers abelianness. *Example problem:* show a minimal normal subgroup of a finite solvable group is elementary abelian.

The third source is **the quotient $G/M$ by a maximal normal subgroup, when $G$ is abelian**. If $G$ is abelian and $M$ is a maximal proper normal subgroup, then $G/M$ is abelian (a quotient of an abelian group) and simple (by maximality, via the [[Thm - Correspondence Theorem|correspondence theorem]]). The theorem then forces $G/M \cong C_p$. The non-obvious payoff is that the abelian composition factors arising in any composition series are *always* of this form. *Example problem:* identify the composition factors of a finite abelian group.

**Targets (Output Amplification)**

The conclusion is the strong identification $G \cong C_p$.

Combine the conclusion with **the structure of $C_p$**. Once $G \cong C_p$, you know everything: $G$ has exactly $p$ elements, every non-identity element has order $p$ and generates $G$, $G$ has no proper non-trivial subgroup, and $\operatorname{Aut}(C_p) \cong C_{p-1}$. The further result $E$ is total structural knowledge from a one-word hypothesis ("simple") plus "abelian" — non-obvious because "simple" is a statement purely about normal subgroups, yet here it determines the entire group.

Combine the conclusion with **a composition series**. If $G$ is a finite *solvable* group, every composition factor is abelian simple, hence by this theorem is some $C_p$. The further result is that the composition factors of a finite solvable group are exactly a list of primes (with multiplicity), and their product is $|G|$ — so the composition series of a solvable group is a refinement of the prime factorisation of its order. This is the precise sense in which solvable groups are "built from primes".

Combine the conclusion with **Cauchy's theorem in reverse**. The theorem says the only way an abelian group can be simple is to have prime order. Contrapositively, any abelian group whose order is *composite* has a proper non-trivial subgroup (indeed a normal one). The further result is a clean criterion: an abelian group is simple precisely when its order is prime — useful as an instant non-simplicity test for abelian groups of composite order.

---

# Why Is It True

The whole theorem turns on one observation, and once you have it the result is almost obvious.

**In an abelian group, every subgroup is normal.** Normality of $H$ means $gHg^{-1} = H$ for all $g$; but if the group is abelian, $gHg^{-1} = gg^{-1}H = H$ automatically. Conjugation does nothing. So in the abelian world there is no distinction between "subgroup" and "normal subgroup" — the two notions coincide.

Now feed this into the definition of simple. Simple means *no normal subgroups except $\{e\}$ and $G$*. For an abelian group, since every subgroup is normal, this collapses to:

> An abelian group is simple $\iff$ it has **no proper non-trivial subgroups at all.**

That is a far more elementary condition, and it is easy to see which groups satisfy it. Suppose $G$ is abelian with no proper non-trivial subgroup. Pick any element $g \neq e$. It generates a cyclic subgroup $\langle g \rangle$, which is non-trivial (it contains $g$). The only subgroup that is both non-trivial and not proper is $G$ itself — so $\langle g \rangle = G$, and $G$ is cyclic. So $G$ is forced to be cyclic, generated by *any* of its non-identity elements.

A cyclic group is either infinite, hence $\cong \mathbb{Z}$, or finite of order $m$, hence $\cong C_m$. The infinite case is killed instantly: $\mathbb{Z}$ has the proper non-trivial subgroup $2\mathbb{Z}$, so $\mathbb{Z}$ is *not* simple. Thus $G \cong C_m$ for some finite $m$. Finally, if $m$ had a divisor $d$ with $1 < d < m$, then $C_m$ would contain a subgroup of order $d$ (generated by $g^{m/d}$) — proper and non-trivial. For $G$ to have no such subgroup, $m$ must have *no* divisors strictly between $1$ and itself: $m$ must be prime.

So the chain of reasoning is: abelian $\Rightarrow$ subgroups are normal $\Rightarrow$ simple means *no* proper subgroups $\Rightarrow$ cyclic $\Rightarrow$ finite cyclic $\Rightarrow$ prime order. The intuition is that simplicity is a constraint on *normal* subgroups, and abelianness erases the gap between normal and arbitrary subgroups — so for abelian groups, "simple" is the maximally strong condition "no subgroups at all", which only the prime-order cyclic groups can meet. The converse — that $C_p$ really is simple — is the same subgroup count run forwards: [[Thm - Lagrange's Theorem|Lagrange]] says a subgroup of $C_p$ has order dividing $p$, so order $1$ or $p$, so $\{e\}$ or $C_p$.

---

# What Makes This Hard

The theorem is not hard once you see the key reduction — *abelian forces every subgroup to be normal, so "simple" downgrades to "no proper non-trivial subgroups"* — and the usual stumbling point is failing to make that reduction and instead trying to reason about normal subgroups directly. After the reduction, the common errors are two boundary oversights: forgetting to rule out the *infinite* cyclic case ($\mathbb{Z}$ is cyclic with no normality obstruction, yet not simple because $2\mathbb{Z} \trianglelefteq \mathbb{Z}$), and forgetting that a *composite* order $m$ produces an explicit subgroup of order $d$ for each divisor $d \mid m$ via the element $g^{m/d}$ — which is exactly what forces $m$ prime.

---

# Rederivation Scaffold

**High-level strategy:**
Reduce "simple" to "no proper non-trivial subgroups" using that an abelian group's subgroups are all normal. Then: a non-identity element must generate the whole group (so $G$ is cyclic); rule out $\mathbb{Z}$; rule out composite order. For the converse, use Lagrange.

**Subgoal decomposition:**

1. **Reduction.** Show that for an abelian $G$, simplicity is equivalent to having no subgroup other than $\{e\}$ and $G$.
   - *Hint:* In an abelian group $gHg^{-1} = H$ for every subgroup $H$, so "normal subgroup" means "subgroup".
   - *Why needed:* It converts a statement about normal subgroups into one about all subgroups, which is far easier to control.

2. **$G$ is cyclic.** Assuming $G$ abelian simple, show $G = \langle g \rangle$ for any $g \neq e$.
   - *Hint:* $\langle g \rangle$ is a non-trivial subgroup; by step 1 the only such is $G$ itself.
   - *Why needed:* It restricts $G$ to the classified family of cyclic groups.

3. **$G$ is finite.** Rule out $G \cong \mathbb{Z}$.
   - *Hint:* $\mathbb{Z}$ has the proper non-trivial subgroup $2\mathbb{Z}$, so $\mathbb{Z}$ is not simple.
   - *Why needed:* It leaves only the finite cyclic groups $C_m$.

4. **$|G|$ is prime.** Show that if $G \cong C_m$ is simple then $m$ is prime.
   - *Hint:* A divisor $d$ of $m$ with $1 < d < m$ gives the proper non-trivial subgroup $\langle g^{m/d}\rangle$ of order $d$.
   - *Why needed:* It completes the forward direction with the exact identification $G \cong C_p$.

5. **Converse.** Show $C_p$ is simple for $p$ prime.
   - *Hint:* By [[Thm - Lagrange's Theorem|Lagrange]] any subgroup has order dividing $p$, hence $1$ or $p$; all subgroups are normal as $C_p$ is abelian.
   - *Why needed:* It gives the "if" direction, making the characterisation an equivalence.

---

# Lemma Decomposition

> [!note]- Lemma 1: In an abelian group, every subgroup is normal
> **Statement:** If $G$ is abelian and $H \leq G$, then $H \trianglelefteq G$.
>
> **Hint:** Compute $gHg^{-1}$ using commutativity.
>
> **Why needed:** It is the reduction that makes the whole theorem elementary — it equates "normal subgroup" with "subgroup" in the abelian setting.
>
> > [!note]- Full proof
> > Let $H \leq G$ and $g \in G$. For any $h \in H$, commutativity gives
> > $$ghg^{-1} = g g^{-1} h = e h = h \in H.$$
> > So $gHg^{-1} \subseteq H$ for every $g$; applying this with $g^{-1}$ gives $g^{-1}Hg \subseteq H$, i.e. $H \subseteq gHg^{-1}$. Hence $gHg^{-1} = H$ for all $g$, and $H \trianglelefteq G$.

> [!note]- Lemma 2: A group with no proper non-trivial subgroup is cyclic
> **Statement:** If $G$ is a non-trivial group whose only subgroups are $\{e\}$ and $G$, then $G = \langle g \rangle$ for every $g \neq e$; in particular $G$ is cyclic.
>
> **Hint:** For $g \neq e$, the cyclic subgroup $\langle g \rangle$ is non-trivial.
>
> **Why needed:** It moves the argument into the cyclic groups, where the classification ($\mathbb{Z}$ or $C_m$) is known.
>
> > [!note]- Full proof
> > Since $G$ is non-trivial, choose $g \in G$ with $g \neq e$. The set $\langle g \rangle = \{g^n : n \in \mathbb{Z}\}$ is a subgroup of $G$, and it is non-trivial because it contains $g \neq e$. By hypothesis the only subgroups are $\{e\}$ and $G$; as $\langle g \rangle \neq \{e\}$, we must have $\langle g \rangle = G$. Hence $G$ is cyclic, generated by $g$. Since $g$ was an arbitrary non-identity element, every non-identity element generates $G$.

> [!note]- Lemma 3: A finite cyclic group $C_m$ has a subgroup of order $d$ for every divisor $d$ of $m$
> **Statement:** If $G = \langle g \rangle$ has order $m$ and $d \mid m$, then $\langle g^{m/d}\rangle$ is a subgroup of $G$ of order exactly $d$.
>
> **Hint:** The order of the element $g^{m/d}$ is $m / \gcd(m, m/d) = d$.
>
> **Why needed:** It produces, from any non-trivial proper divisor of $m$, a proper non-trivial subgroup — forcing $m$ prime in a simple cyclic group.
>
> > [!note]- Full proof
> > Let $g$ have order $m$ and let $d \mid m$, say $m = d e$. Consider $x = g^{m/d} = g^{e}$. The order of $x$ is the least positive $k$ with $g^{ek} = e$, i.e. with $m \mid ek$, i.e. with $de \mid ek$, i.e. with $d \mid k$. The least such $k$ is $d$. So $\operatorname{ord}(x) = d$, and $\langle x \rangle$ is a subgroup of order $d$. If $1 < d < m$ this subgroup is proper ($d < m$) and non-trivial ($d > 1$).

> [!note]- Lemma 4: $C_p$ is simple for $p$ prime (the converse)
> **Statement:** For a prime $p$, the cyclic group $C_p$ is simple.
>
> **Hint:** Combine [[Thm - Lagrange's Theorem|Lagrange's theorem]] with Lemma 1.
>
> **Why needed:** It is the "if" direction of the theorem, certifying that prime-order cyclic groups really are simple.
>
> > [!note]- Full proof
> > Let $H \leq C_p$. By [[Thm - Lagrange's Theorem|Lagrange's theorem]], $|H|$ divides $|C_p| = p$. Since $p$ is prime, $|H| \in \{1, p\}$, so $H = \{e\}$ or $H = C_p$. Thus $C_p$ has no proper non-trivial subgroup. As $C_p$ is abelian, every subgroup is normal (Lemma 1), so in particular the only normal subgroups are $\{e\}$ and $C_p$. Since $C_p$ is non-trivial, it is simple.

---

# Formal Proof

> [!note]- Complete formal proof
> **($\Leftarrow$) If $G \cong C_p$ for a prime $p$, then $G$ is abelian and simple.**
>
> A cyclic group is abelian. By [[Thm - Lagrange's Theorem|Lagrange's theorem]], any subgroup of $C_p$ has order dividing $p$, hence order $1$ or $p$, hence equals $\{e\}$ or $C_p$. Since $C_p$ is abelian, every subgroup is normal (Lemma 1), so the only normal subgroups are $\{e\}$ and $C_p$. As $C_p$ is non-trivial, it is simple. (See Lemma 4.)
>
> **($\Rightarrow$) If $G$ is abelian and simple, then $G \cong C_p$ for some prime $p$.**
>
> Since $G$ is abelian, every subgroup of $G$ is normal (Lemma 1). Simplicity says the only normal subgroups are $\{e\}$ and $G$; combined with the previous sentence, *the only subgroups of $G$ whatsoever are $\{e\}$ and $G$*.
>
> By the definition of simple, $G$ is non-trivial, so pick $g \in G$ with $g \neq e$. The cyclic subgroup $\langle g \rangle$ is non-trivial (it contains $g$), so it cannot be $\{e\}$; hence $\langle g \rangle = G$. Therefore $G$ is cyclic (Lemma 2).
>
> A cyclic group is isomorphic either to the infinite cyclic group $\mathbb{Z}$ or to a finite cyclic group $C_m$. The case $G \cong \mathbb{Z}$ is impossible: $2\mathbb{Z}$ is a proper non-trivial subgroup of $\mathbb{Z}$, contradicting that $G$ has only the subgroups $\{e\}$ and $G$. Hence $G \cong C_m$ for some finite $m \geq 2$ (note $m \neq 1$ since $G$ is non-trivial).
>
> Finally, suppose for contradiction $m$ is not prime, so $m$ has a divisor $d$ with $1 < d < m$. By Lemma 3, $G \cong C_m$ has a subgroup of order $d$; since $1 < d < m$ this subgroup is proper and non-trivial — again contradicting that the only subgroups of $G$ are $\{e\}$ and $G$. Therefore $m$ has no divisor strictly between $1$ and $m$, i.e. $m$ is prime.
>
> Hence $G \cong C_p$ for the prime $p = m$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Composition factors of a finite abelian group.** Let $G$ be a finite abelian group. Any composition series of $G$ has factors that are simple, and — being quotients/subquotients of an abelian group — abelian. By this theorem each factor is $\cong C_p$ for some prime $p$. So the composition factors of a finite abelian group of order $n = p_1^{a_1}\cdots p_r^{a_r}$ are exactly the primes $p_i$, each appearing $a_i$ times. The application is non-obvious because it reduces the [[Thm - Composition Series|Jordan–Hölder]] data of an abelian group to the prime factorisation of its order.

**The only simple abelian group acted on faithfully and irreducibly.** In representation theory, a minimal normal subgroup $N$ of a finite group, when abelian, is *elementary abelian* — a product of copies of $C_p$ for a single prime $p$. The single-factor case is governed by this theorem: the only abelian simple group is $C_p$. Recognising that "abelian + simple" leaves *only* $C_p$ is the non-obvious step that pins down the building blocks of elementary abelian groups.

**Fields with no proper subfield.** The prime fields $\mathbb{F}_p$ and $\mathbb{Q}$ are the fields with no proper subfield. The additive group of $\mathbb{F}_p$ is $C_p$, an abelian simple group — and the theorem explains *why $p$ must be prime* for $\mathbb{F}_p$ to exist as a field: the additive group of a finite field of prime order is forced, by simplicity considerations, to have prime order. The non-obvious link is that the characteristic of a field being prime is shadowed by the abelian-simple classification.

**Quotient groups that cannot be subdivided.** Suppose $G$ is abelian and $N \trianglelefteq G$ is chosen so that $G/N$ is as small as possible while non-trivial — a *maximal* normal subgroup. Then $G/N$ is abelian and simple, so $G/N \cong C_p$. This gives a clean recipe: the smallest non-trivial quotient of an abelian group is always cyclic of prime order. The application is non-obvious because "smallest non-trivial quotient" sounds like it could be any small group, yet the theorem forces it to be $C_p$.

---

# Bridges

- **[[Thm - Lagrange's Theorem|Lagrange's Theorem]]** — supplies both directions of the order count. Forwards: a composite order produces a subgroup of each divisor's size. Backwards: a prime order forbids any proper non-trivial subgroup, which is what makes $C_p$ simple.

- **[[Def - Simple Group|Simple Group]]** — this theorem is the complete classification of the *abelian* simple groups. The non-abelian simple groups — $A_n$ for $n \geq 5$, the groups of Lie type, the sporadic groups — are the content of the Classification of Finite Simple Groups and lie far beyond this result.

- **[[Thm - Composition Series|Composition Series]]** — this theorem identifies the abelian composition factors. In a finite *solvable* group every composition factor is abelian simple, hence by this theorem cyclic of prime order; so this result is what makes the composition factors of a solvable group a multiset of primes.

- **Cauchy's theorem** — a partial converse to Lagrange. Cauchy guarantees an element (hence a subgroup) of order $p$ whenever a prime $p$ divides $|G|$. For abelian groups of composite order this exhibits the proper subgroup that this theorem says must exist, the reason such groups fail to be simple.

- **[[Thm - Correspondence Theorem|Correspondence Theorem]]** — used to see that the quotient of an abelian group by a *maximal* normal subgroup is simple; combined with this theorem, that quotient is $\cong C_p$.

---

# Unlocked by This

> [!tip] Elementary Abelian Groups *(from Group Theory / Sylow Theory)*
> A minimal normal subgroup of a finite solvable group is *elementary abelian* — a direct product $C_p \times \cdots \times C_p$ — and this theorem is the single-factor base case identifying the only abelian simple group as $C_p$.

> [!tip] The Prime Field $\mathbb{F}_p$ *(from Field Theory)*
> The additive group of the prime field $\mathbb{F}_p$ is the abelian simple group $C_p$; this theorem underlies why a field of prime order has its characteristic forced to be prime.

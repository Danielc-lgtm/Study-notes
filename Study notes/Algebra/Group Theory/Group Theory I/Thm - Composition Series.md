---
type: theorem
subject: group-theory
prereqs:
  - "Def - Normal Subgroup"
  - "Def - Quotient Group"
  - "Def - Simple Group"
  - "Def - Order of a Group and of an Element"
  - "Thm - Correspondence Theorem"
  - "Thm - Abelian Simple Groups are Cyclic of Prime Order"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a finite group with identity $e$, and $\{e\}$ denotes the trivial group. The relation $H \trianglelefteq G$ means $H$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$; $H \trianglerighteq H'$ means $H' \trianglelefteq H$. A [[Def - Simple Group|simple group]] is a non-trivial group whose only normal subgroups are $\{e\}$ and itself. A chain of subgroups
$$G = H_1 \trianglerighteq H_2 \trianglerighteq \cdots \trianglerighteq H_n = \{e\}$$
is a **composition series** if each $H_{i+1} \trianglelefteq H_i$ and each successive quotient $H_i / H_{i+1}$ is simple; these quotients are the **composition factors**. Note $H_{i+1}$ is required normal only in $H_i$, not in $G$. The full registry is on the parent page [[Group Theory I — §1.1–1.2]].

---

# Statement

> **Existence of a Composition Series.** Every finite group $G$ admits a composition series: a chain of subgroups
> $$G = H_1 \;\trianglerighteq\; H_2 \;\trianglerighteq\; \cdots \;\trianglerighteq\; H_n = \{e\}$$
> in which each $H_{i+1}$ is normal in $H_i$ and each quotient $H_i / H_{i+1}$ is simple.

---

# Motivation

The recurring strategy of this whole topic is: to understand a complicated group $G$, find a [[Def - Normal Subgroup|normal subgroup]] $N$ and break $G$ into the two simpler pieces $N$ and the [[Def - Quotient Group|quotient]] $G/N$. But this raises an obvious question — *can you always keep going?* You break $G$ into $N$ and $G/N$; can you break those, and their pieces, and so on, until nothing breaks any further? And what do the indivisible pieces at the end look like?

A composition series is the answer. It is a maximal record of the breaking-apart process: a chain descending from $G$ to the trivial group, in which each step quotients out a normal subgroup, and — crucially — each successive quotient $H_i/H_{i+1}$ is *simple*, meaning it cannot be broken any further. The composition factors are the indivisible residue, the pieces at which the process halts.

This is the **prime factorisation analogy** made exact. To understand an integer $n$ you write it as a product of primes — numbers that cannot be factored further. To understand a finite group you write a composition series, whose factors are simple groups — groups that cannot be quotiented further. The simple groups are the "primes" of finite group theory, and this theorem is the assertion that the factorisation always *exists*: every finite group, no matter how intricate, is assembled from simple pieces.

The theorem has a famous companion, the **Jordan–Hölder theorem**, which says the factorisation is moreover *unique*: although a group may have many different composition series, the multiset of composition factors — counted with multiplicity, ignoring order — is an invariant of $G$. Existence (this theorem) plus uniqueness (Jordan–Hölder) together say that the composition factors are a genuine, well-defined invariant, the true analogue of the prime factorisation. That is why classifying the simple groups — the Classification of Finite Simple Groups — is so fundamental: it is the project of writing down the periodic table from which every finite group is built.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is mild — *any* finite group has a composition series. The disguised-source question is: when does having a composition series, or controlling its factors, become the useful hypothesis?

The first source is **a finite solvable group**. A finite group $G$ is solvable if it has a normal series with abelian factors; refining such a series produces a composition series whose factors are abelian *and* simple. By [[Thm - Abelian Simple Groups are Cyclic of Prime Order|the classification of abelian simple groups]], those factors are cyclic of prime order. The non-obvious step is that solvability secretly pins down the composition factors completely — they are exactly cyclic groups $C_p$. *Example problem:* show a finite group is solvable if and only if all its composition factors are cyclic of prime order.

The second source is **a finite $p$-group** (order a power of a prime $p$). Every finite $p$-group has a non-trivial centre, and from this one builds a composition series all of whose factors are $C_p$. The non-obviousness is that "$|G| = p^n$" alone forces every composition factor to be the *same* group $C_p$, so a $p$-group is, in composition-factor terms, maximally homogeneous. *Example problem:* show every group of order $p^n$ has a normal subgroup of every order $p^k$, $0 \le k \le n$.

The third source is **a group given only by its order $|G| = n$**. The factors of a composition series have orders multiplying to $n$, so the prime factorisation of $n$ constrains the possible factors before any structure is known. The non-obvious payoff is that arithmetic of $n$ alone — via [[Thm - Lagrange's Theorem|Lagrange]] applied along the chain — limits which simple groups can appear. *Example problem:* show a group of order $pq$ ($p < q$ primes) has composition factors $C_p$ and $C_q$.

**Targets (Output Amplification)**

The conclusion produces a chain whose successive quotients are simple.

Combine the conclusion with **the Jordan–Hölder theorem**. Jordan–Hölder upgrades the existence of *a* composition series to the uniqueness of the *multiset of factors*. The further result $E$ is that the composition factors are an **invariant** of $G$ — two groups with different composition-factor multisets are non-isomorphic. This is non-obvious because a single group has many composition series, yet they all yield the same factors; the combination gives a powerful invariant for distinguishing groups.

Combine the conclusion with **a property closed under extensions**. Many properties — solvability, nilpotency, being a $p$-group — are inherited by subgroups and quotients and built up along normal series. If every composition factor of $G$ has such a property in its strongest "simple" form (e.g. every factor is cyclic of prime order), then $G$ itself has the corresponding global property (e.g. $G$ is solvable). The further result is a *factor-by-factor* criterion: a global structural property of $G$ is decided by examining its simple composition factors one at a time.

Combine the conclusion with **induction on $|G|$**. A composition series exhibits $G$ as a tower over the strictly smaller group $H_2$ with simple top factor $G/H_2$. The further result is a clean inductive scaffold: prove a statement for simple groups and for extensions, then the composition series propagates it to all finite groups. This is non-obvious as a *proof technique* — the composition series is not just a description of $G$ but a recursion skeleton for theorems about all finite groups.

---

# Why Is It True

The existence of a composition series should not be surprising at all, and the reason is a simple **finiteness** argument: you keep chopping, and because the group is finite you cannot chop forever.

Here is the picture. Start with $G$. If $G$ is already simple, the chain $G \trianglerighteq \{e\}$ is a composition series and you are done. If $G$ is *not* simple, it has *some* proper non-trivial normal subgroup. The clever move is not to pick any such subgroup, but to pick a **maximal** one — a proper normal subgroup $H_2 \trianglelefteq G$ of largest possible order. (Such a maximal one exists because there are only finitely many subgroups to compare.)

Why maximal? Because maximality is *exactly* the condition that makes the quotient $G/H_2$ simple. Suppose $G/H_2$ were not simple. Then $G/H_2$ would have a proper non-trivial normal subgroup. By the [[Thm - Correspondence Theorem|correspondence theorem]], normal subgroups of $G/H_2$ correspond to normal subgroups of $G$ lying *between* $H_2$ and $G$ — and a proper non-trivial one of $G/H_2$ would correspond to a normal subgroup $K$ of $G$ with $H_2 \subsetneq K \subsetneq G$. But that $K$ is a proper normal subgroup of $G$ *strictly larger than* $H_2$, contradicting the choice of $H_2$ as maximal. So $G/H_2$ has no proper non-trivial normal subgroup: it is simple.

So one step of the process gives you a normal subgroup $H_2$ with $G/H_2$ simple. Now just repeat the whole argument on $H_2$: find a maximal proper normal subgroup $H_3$ of $H_2$, with $H_2/H_3$ simple; then on $H_3$; and so on. This generates a strictly decreasing chain $G = H_1 \supsetneq H_2 \supsetneq H_3 \supsetneq \cdots$ — strictly decreasing because each $H_{i+1}$ is a *proper* subgroup of $H_i$, so $|H_{i+1}| < |H_i|$.

And here is the finiteness: the orders $|H_1| > |H_2| > |H_3| > \cdots$ form a strictly decreasing sequence of positive integers. Such a sequence cannot go on forever — it must terminate, and it can only terminate when some $H_n$ has no proper non-trivial normal subgroup to descend through, i.e. when $H_n = \{e\}$. (If $H_n$ were non-trivial and simple, we append $\{e\}$; if non-trivial and non-simple, the process continues.) The chain therefore reaches $\{e\}$ in finitely many steps, and by construction every successive quotient is simple. That is a composition series.

The intuition in one sentence: **breaking a finite group apart is a process that cannot run forever, because each break strictly shrinks the order, and the only place it can stop is the trivial group — so the process always succeeds.** The single non-trivial ingredient is the use of the correspondence theorem to see that quotienting by a *maximal* normal subgroup yields a *simple* quotient; everything else is "a decreasing sequence of positive integers terminates".

---

# What Makes This Hard

The conceptual leap is realising you should descend by a *maximal* proper normal subgroup, not an arbitrary one: maximality is precisely what forces the quotient to be simple, and the [[Thm - Correspondence Theorem|correspondence theorem]] is the tool that converts "no normal subgroup strictly above $H_2$" into "$G/H_2$ has no proper non-trivial normal subgroup". The most common error is the slogan "normal is transitive" — assuming each $H_i$ is normal in $G$; it is not, and the theorem only claims $H_{i+1} \trianglelefteq H_i$, normality in the *immediate predecessor*. A second subtlety is justifying termination: one must invoke that a strictly decreasing sequence of positive integers (the orders $|H_i|$) is finite — skipping this leaves the induction without a base.

---

# Rederivation Scaffold

**High-level strategy:**
Induct on $|G|$. If $G$ is simple, done. Otherwise pick a *maximal* proper normal subgroup $H_2$; the correspondence theorem makes $G/H_2$ simple. Apply the inductive hypothesis to the strictly smaller $H_2$ and prepend $G$.

**Subgoal decomposition:**

1. **Base case.** Handle $G$ trivial or simple.
   - *Hint:* If $G = \{e\}$ the chain is trivial; if $G$ is simple, $G \trianglerighteq \{e\}$ works since $G/\{e\} \cong G$ is simple.
   - *Why needed:* It anchors the induction and covers the indivisible groups.

2. **Choose a maximal proper normal subgroup.** For non-simple $G$, select $H_2 \trianglelefteq G$ proper, non-trivial, of maximal order.
   - *Hint:* The set of proper normal subgroups is finite and non-empty (as $G$ is not simple), so a maximal-order element exists.
   - *Why needed:* Maximality is the hypothesis that forces the next step.

3. **The quotient $G/H_2$ is simple.** Show $G/H_2$ has no proper non-trivial normal subgroup.
   - *Hint:* By the [[Thm - Correspondence Theorem|correspondence theorem]], such a subgroup would correspond to a normal subgroup of $G$ strictly between $H_2$ and $G$, contradicting maximality of $H_2$.
   - *Why needed:* It makes the top factor $G/H_2$ simple, the defining requirement of a composition series.

4. **Recurse on $H_2$.** Apply the inductive hypothesis to $H_2$, which has $|H_2| < |G|$.
   - *Hint:* $H_2$ is a smaller finite group, so by induction it has a composition series $H_2 \trianglerighteq H_3 \trianglerighteq \cdots \trianglerighteq \{e\}$.
   - *Why needed:* It produces the rest of the chain below $H_2$.

5. **Assemble and confirm termination.** Prepend $G$ to the series for $H_2$; confirm the process terminates.
   - *Hint:* $|H_1| > |H_2| > \cdots$ is a strictly decreasing sequence of positive integers, hence finite; the chain ends at $\{e\}$.
   - *Why needed:* It yields the full composition series $G = H_1 \trianglerighteq \cdots \trianglerighteq \{e\}$ and proves it has finite length.

---

# Lemma Decomposition

> [!note]- Lemma 1: A non-simple finite group has a maximal proper normal subgroup
> **Statement:** If $G$ is a finite group that is not simple (and non-trivial), then among the proper non-trivial normal subgroups of $G$ there is one of maximal order.
>
> **Hint:** There are only finitely many subgroups of a finite group; a finite non-empty set of integers has a maximum.
>
> **Why needed:** The whole construction descends through this maximal subgroup; without its existence there is nothing to quotient by.
>
> > [!note]- Full proof
> > Since $G$ is not simple and is non-trivial, it has at least one normal subgroup other than $\{e\}$ and $G$ — that is, the set $\mathcal{N}$ of proper non-trivial normal subgroups is non-empty. A finite group has only finitely many subsets, hence finitely many subgroups, so $\mathcal{N}$ is finite. The orders $\{|N| : N \in \mathcal{N}\}$ form a finite non-empty set of positive integers, which therefore has a maximum; any $N \in \mathcal{N}$ achieving it is a proper non-trivial normal subgroup of maximal order.

> [!note]- Lemma 2: Quotienting by a maximal proper normal subgroup yields a simple group
> **Statement:** Let $G$ be a group and $M \trianglelefteq G$ a proper normal subgroup that is maximal among proper normal subgroups of $G$. Then $G/M$ is simple.
>
> **Hint:** Use the [[Thm - Correspondence Theorem|correspondence theorem]]: normal subgroups of $G/M$ match normal subgroups of $G$ containing $M$.
>
> **Why needed:** It is the step that produces a *simple* composition factor at the top of the chain — the defining property of a composition series.
>
> > [!note]- Full proof
> > First, $G/M$ is non-trivial because $M$ is a *proper* subgroup of $G$. Suppose, for contradiction, $G/M$ is not simple: then it has a normal subgroup $X$ with $X \neq \{e_{G/M}\}$ and $X \neq G/M$.
> >
> > By the [[Thm - Correspondence Theorem|correspondence theorem]] applied to $M \trianglelefteq G$, normal subgroups of $G/M$ correspond bijectively (preserving inclusion and normality) to normal subgroups of $G$ containing $M$. Let $K \trianglelefteq G$ be the normal subgroup of $G$ corresponding to $X$, so $M \leq K$. Because the correspondence preserves inclusion and is a bijection:
> > - $X \neq \{e_{G/M}\}$ corresponds to $K \neq M$, so $M \subsetneq K$;
> > - $X \neq G/M$ corresponds to $K \neq G$, so $K \subsetneq G$.
> >
> > Thus $K$ is a normal subgroup of $G$ with $M \subsetneq K \subsetneq G$ — a proper non-trivial normal subgroup of $G$ strictly larger than $M$. This contradicts the maximality of $M$. Hence $G/M$ is simple.

> [!note]- Lemma 3: A strictly decreasing chain of subgroups of a finite group has finite length
> **Statement:** If $G$ is finite and $G = H_1 \supsetneq H_2 \supsetneq H_3 \supsetneq \cdots$ is a strictly decreasing chain of subgroups, the chain has finitely many terms.
>
> **Hint:** Track the orders.
>
> **Why needed:** It guarantees the descending construction terminates — the induction on $|G|$ is well-founded only because the chain cannot be infinite.
>
> > [!note]- Full proof
> > For each $i$, $H_{i+1} \subsetneq H_i$, and both are subgroups of the finite group $G$, so $|H_{i+1}| < |H_i|$ (a proper subset has strictly smaller cardinality). Hence $|H_1| > |H_2| > |H_3| > \cdots$ is a strictly decreasing sequence of positive integers bounded below by $1$. Such a sequence has at most $|H_1| = |G|$ terms, so the chain is finite.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove by strong induction on $|G|$ that every finite group $G$ has a composition series.
>
> **Base case.** If $|G| = 1$, then $G = \{e\}$ and the one-term chain $G = \{e\}$ is a (degenerate) composition series. If $G$ is simple, the chain $G \trianglerighteq \{e\}$ is a composition series: the single quotient $G/\{e\} \cong G$ is simple.
>
> **Inductive step.** Let $|G| > 1$ and suppose every finite group of order less than $|G|$ has a composition series. If $G$ is simple, the base case applies. Otherwise $G$ is not simple.
>
> By Lemma 1, $G$ has a proper non-trivial normal subgroup of maximal order; call it $H_2$, so $H_2 \trianglelefteq G$ and $\{e\} \neq H_2 \subsetneq G$. By Lemma 2, since $H_2$ is maximal among proper normal subgroups of $G$, the quotient $G/H_2$ is simple.
>
> Now $H_2$ is a finite group with $|H_2| < |G|$ (it is a proper subgroup). By the inductive hypothesis, $H_2$ has a composition series
> $$H_2 = H_2 \;\trianglerighteq\; H_3 \;\trianglerighteq\; \cdots \;\trianglerighteq\; H_n = \{e\},$$
> with each $H_{i+1} \trianglelefteq H_i$ and each $H_i/H_{i+1}$ simple, for $i = 2, \dots, n-1$.
>
> Prepend $G$ to obtain
> $$G = H_1 \;\trianglerighteq\; H_2 \;\trianglerighteq\; H_3 \;\trianglerighteq\; \cdots \;\trianglerighteq\; H_n = \{e\}.$$
> We check this is a composition series. Each $H_{i+1} \trianglelefteq H_i$: for $i \geq 2$ this holds by the series for $H_2$, and for $i = 1$ it is the statement $H_2 \trianglelefteq G$, established above. Each quotient $H_i/H_{i+1}$ is simple: for $i \geq 2$ by the series for $H_2$, and for $i = 1$ the quotient $H_1/H_2 = G/H_2$ is simple by Lemma 2.
>
> Hence $G$ has a composition series. By induction, every finite group does.
>
> **Termination remark.** The construction terminates because, reading it as a repeated descent, it produces a strictly decreasing chain $G = H_1 \supsetneq H_2 \supsetneq \cdots$, which by Lemma 3 has finitely many terms; it can only stop at $\{e\}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Composition factors of a cyclic group recover prime factorisation.** Take $G = C_n$ with $n = p_1 p_2 \cdots p_r$ (primes, with repetition). A composition series of $C_n$ has factors that are abelian simple, hence each $\cong C_{p}$ for some prime by [[Thm - Abelian Simple Groups are Cyclic of Prime Order|the abelian classification]], and their orders multiply to $n$. So the composition factors of $C_n$ are exactly the prime factors of $n$. The application is non-obvious because it exhibits the prime factorisation of an integer as a *special case* of the composition series of a group — the analogy made literal.

**Solvability as a composition-factor condition.** A finite group $G$ is solvable if and only if every composition factor of $G$ is cyclic of prime order. To use this: given a finite group, compute (or constrain) its composition factors; if any factor is a non-abelian simple group, $G$ is not solvable. This is the standard route to proving, for instance, that $S_n$ is not solvable for $n \geq 5$ — its composition factors include the non-abelian simple group $A_n$. The non-obvious step is converting the global property "solvable" into a local check on each simple factor.

**Distinguishing groups of the same order.** Two finite groups with different multisets of composition factors are non-isomorphic (by Jordan–Hölder, the factors are an invariant). For example, $C_6$ and $S_3$ both have order $6$ — but $C_6$ has composition factors $\{C_2, C_3\}$ with abelian-only factors (so it is solvable, indeed abelian), while $S_3$ has the same factor multiset $\{C_2, C_3\}$ yet is non-abelian; a sharper invariant (the series itself, or the extension data) is needed here, illustrating that composition factors *constrain* but the extension problem carries the remaining information. The non-obvious lesson: composition factors are necessary but not sufficient to identify a group.

**Chief series and minimal normal subgroups.** A variant of the construction descends by normal subgroups of $G$ that are normal *in $G$* throughout (a chief series), with factors that are *characteristically* simple. The same maximality-plus-correspondence argument works, replacing "maximal proper normal subgroup" by "minimal normal subgroup", and the [[Thm - Correspondence Theorem|correspondence theorem]] again controls the factors. Recognising that the composition-series argument adapts to chief series by swapping which extreme you optimise is the non-obvious transfer.

---

# Bridges

- **[[Thm - Correspondence Theorem|Correspondence Theorem]]** — the engine of the proof. It is what converts "maximal proper normal subgroup $H_2$" into "$G/H_2$ is simple": a proper non-trivial normal subgroup of $G/H_2$ would correspond to a normal subgroup of $G$ strictly between $H_2$ and $G$, which maximality forbids.

- **[[Thm - Abelian Simple Groups are Cyclic of Prime Order|Abelian Simple Groups are Cyclic of Prime Order]]** — identifies the *abelian* composition factors. When $G$ is solvable, every composition factor is abelian simple, hence cyclic of prime order; this is what makes the composition series of a solvable group a refinement of the prime factorisation of $|G|$.

- **[[Def - Simple Group|Simple Group]]** — supplies the indivisible pieces. The composition factors are simple groups; the existence theorem says the simple groups are exactly the building blocks, and the Classification of Finite Simple Groups is the project of listing them.

- **The prime factorisation of integers** — the structural analogue. A composition series is to a finite group what a prime factorisation is to an integer: simple groups are the "primes", existence here corresponds to "every integer is a product of primes", and Jordan–Hölder corresponds to the uniqueness of prime factorisation.

---

# Unlocked by This

> [!tip] Jordan–Hölder Theorem *(from Group Theory)*
> Existence of a composition series is only half the story. The **Jordan–Hölder theorem** asserts uniqueness: any two composition series of a finite group $G$ have the same length and the same multiset of composition factors (up to isomorphism and reordering). Together with this existence theorem, it makes the composition factors a genuine invariant of $G$ — the true analogue of the prime factorisation. See [[Thm - Jordan-Hölder Theorem]].

> [!tip] Solvable Groups and Galois' Criterion *(from Galois Theory)*
> A finite group is **solvable** exactly when all its composition factors are cyclic of prime order. Galois' theorem says a polynomial is solvable by radicals if and only if its Galois group is solvable — so the composition series, with its factors classified by [[Thm - Abelian Simple Groups are Cyclic of Prime Order]], is the algebraic heart of why the general quintic has no radical formula. See [[Def - Solvable Group]].

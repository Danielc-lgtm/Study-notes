---
type: exercise
subject: group-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Sylow p-Subgroup"
  - "Def - Simple Group"
  - "Def - Normaliser"
  - "Thm - Sylow's Theorems"
  - "Thm - A Unique Sylow Subgroup is Normal"
  - "Thm - Coset Action and the Normal Core"
  - "Thm - First Isomorphism Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Prove that no [[Def - Group|group]] of order $132$ is [[Def - Simple Group|simple]].

**Recall:**

The objects in play are Sylow [[Def - Subgroup|subgroups]], simplicity, the Sylow count, the element-counting consequence of prime-order Sylow [[Def - Subgroup|subgroups]], and the conjugation action on the set of Sylow subgroups.

![[Def - Sylow p-Subgroup#The Definition]]

Here $|G| = 132 = 2^2 \cdot 3 \cdot 11$. The primes $3$ and $11$ appear to the *first* power, so a Sylow $3$-subgroup has order $3$ and a Sylow $11$-subgroup has order $11$ — both cyclic, with all non-identity elements of that prime order. The prime $2$ appears squared, so a Sylow $2$-subgroup has order $4$.

![[Def - Simple Group#The Definition]]

The clauses of [[Thm - Sylow's Theorems|Sylow's theorems]] used are the *count* (Sylow III: $n_p \equiv 1 \pmod p$ and $n_p \mid m$, where $|G| = p^a m$) and the *conjugacy* clause (Sylow II: $G$ acts transitively by conjugation on the set $\operatorname{Syl}_p(G)$ of Sylow $p$-subgroups). And:

![[Thm - A Unique Sylow Subgroup is Normal#Statement]]

The element-counting step uses the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]]: when a prime $p$ divides $|G|$ but $p^2$ does not, $G$ has exactly $n_p(p-1)$ elements of order $p$. This applies to $3$ and $11$, not to $2$.

The action step uses the **conjugation action on Sylow subgroups**: $G$ acts on $\operatorname{Syl}_p(G)$ by $g \cdot P = gPg^{-1}$, giving a [[Def - Homomorphism|homomorphism]] $\varphi : G \to \operatorname{Sym}(\operatorname{Syl}_p(G)) \cong S_{n_p}$. By the [[Thm - Coset Action and the Normal Core|normal-core principle]], $\ker\varphi$ is a normal subgroup of $G$; if $G$ is simple, $\ker\varphi$ is $\{e\}$ or $G$. When the action is non-trivial (it is, by Sylow II, whenever $n_p > 1$), $\ker\varphi \neq G$, so simplicity forces $\ker\varphi = \{e\}$ and then the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] embeds $G \hookrightarrow S_{n_p}$ — which is impossible if $|G| \nmid n_p!$.

---

# Convergent Strategy

**Problem class.** This is a *non-simplicity* problem, the dominant target of [[Group Theory III — §1.5–1.7#Sources and Targets|the topic]] — and it is the worked summit case of the chapter, the one in the source lecture notes. It is harder than orders $30$ and $56$ because *no single tactic settles it*: the uniqueness step fails, raw element-counting is inconclusive on its own, and the Sylow-set action is needed to *eliminate a candidate value* before element-counting can finish. It drills the combination of all three playbook tactics in sequence.

**Assumption pattern.** The factorization $132 = 2^2 \cdot 3 \cdot 11$ has two first-power primes, $3$ and $11$, so element-counting is available for both — but the Sylow $3$-count has *two* admissible values, $\{4, 22\}$, and only one of them ($22$) makes the element-count overflow. The smaller value $4$ must be killed by other means. The signature here is a small Sylow count ($n_3 = 4$) sitting next to a [[Def - Group|group]] too large to embed in the corresponding symmetric group ($132 \nmid 4! = 24$) — exactly the trigger for the *embedding-obstruction* tactic.

**Theorem routing.** The route is a proof by contradiction with three stages. *Assume $G$ is simple*, so no $n_p = 1$. **(a)** [[Thm - Sylow's Theorems|Sylow III]] on $p = 11$: $n_{11} \equiv 1 \pmod{11}$, $n_{11} \mid 12$, leaving $\{1, 12\}$; simplicity deletes $1$, so $n_{11} = 12$, giving (by the [[Ex - Counting elements of prime order with Sylow subgroups|counting fact]]) $12 \cdot 10 = 120$ elements of order $11$. **(b)** Sylow III on $p = 3$: $n_3 \equiv 1 \pmod 3$, $n_3 \mid 44$, leaving $\{1, 4, 22\}$; simplicity deletes $1$, leaving $\{4, 22\}$. The value $n_3 = 4$ is eliminated by the **Sylow-set action**: $G$ would act on its $4$ Sylow $3$-subgroups, and since $G$ is simple this action is faithful, embedding $G \hookrightarrow S_4$ via the [[Thm - Coset Action and the Normal Core|normal core]] and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] — but $|G| = 132 \nmid 24 = |S_4|$, a contradiction. So $n_3 = 22$, giving $22 \cdot 2 = 44$ elements of order $3$. **(c)** Element-count: $120 + 44 = 164 > 132 = |G|$ — contradiction.

**Key decision point.** The crux — and what lifts this to ⭐⭐⭐ — is recognising that *element-counting alone is not enough* and must be *preceded* by an embedding-obstruction step. If one naively counts with $n_3 = 4$, the order-$3$ elements number only $4 \cdot 2 = 8$, and $120 + 8 = 128 < 132$: no contradiction. The counting argument only bites for $n_3 = 22$. So the value $n_3 = 4$ has to be excised *first*, and the only tool for that is the action of $G$ on the $4$ Sylow $3$-subgroups: $4! = 24$ is too small to contain a faithful image of a group of order $132$. The non-obvious decision is to *not* count immediately, but to first run the Sylow-set action against the small candidate $n_3 = 4$, and only then count with the survivor $n_3 = 22$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory III — §1.5–1.7#Legal Operations|the topic page's Legal Operations]]:

1. **Factor the order and write down the Sylow constraints** (operation 1). The order $132 = 2^2 \cdot 3 \cdot 11$ is factored, and the Sylow constraints are written for $11$ (giving $\{1,12\}$) and for $3$ (giving $\{1, 4, 22\}$).

2. **Conclude normality from a unique Sylow subgroup** (operation 2), used *in contrapositive*. Assuming $G$ simple, [[Thm - A Unique Sylow Subgroup is Normal]] forbids every $n_p = 1$, deleting that value from each candidate list.

3. **Act on the set of Sylow $p$-subgroups** (operation 4). To eliminate $n_3 = 4$: $G$ acts on its $4$ Sylow $3$-subgroups, the [[Thm - Coset Action and the Normal Core|normal core]] gives a normal kernel, simplicity makes the action faithful, and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] yields $G \hookrightarrow S_4$ — impossible since $132 \nmid 24$.

4. **Count elements of prime order** (operation 3). With $n_{11} = 12$ and $n_3 = 22$, the [[Ex - Counting elements of prime order with Sylow subgroups|counting fact]] gives $120$ elements of order $11$ and $44$ of order $3$; the sum $164$ exceeds $|G| = 132$.

---

# Hints

> [!note]- Hint 1
> Factor $132$ and write the Sylow constraints, assuming $G$ is simple (so no $n_p = 1$). For $p = 11$ you get a single value; for $p = 3$ you get *two* admissible values. The two-valued case is where the difficulty lies.

> [!note]- Hint 2
> Try element-counting straight away with $n_{11} = 12$ and *each* candidate for $n_3$. With the larger candidate the counts overflow $|G|$ — good. With the smaller candidate $n_3 = 4$ they do not. So $n_3 = 4$ must be eliminated by a *different* tactic before counting can finish.

> [!note]- Hint 3
> To kill $n_3 = 4$: $G$ acts by conjugation on its $4$ Sylow $3$-subgroups, giving $\varphi : G \to S_4$. The kernel is normal ([[Thm - Coset Action and the Normal Core|normal core]]); the action is non-trivial ([[Thm - Sylow's Theorems|Sylow II]] makes it transitive on $4 > 1$ points), so by simplicity the kernel is trivial, and $G$ embeds in $S_4$ by the [[Thm - First Isomorphism Theorem|first isomorphism theorem]]. But $|S_4| = 24$ and $|G| = 132$. Can a group of order $132$ embed in a group of order $24$?

> [!note]- Hint 4
> So $n_3 = 22$. Now element-count: $n_{11} = 12$ gives $12 \cdot (11-1) = 120$ elements of order $11$; $n_3 = 22$ gives $22 \cdot (3-1) = 44$ elements of order $3$. These sets are disjoint. Add them and compare with $|G| = 132$.

---

# Solution

The plan is a proof by contradiction in three stages: pin $n_{11} = 12$; pin $n_3 = 22$ by eliminating the rival value $n_3 = 4$ with the Sylow-set action; then overflow $G$ by counting.

**Step 1: If $G$ is simple, then $n_{11} = 12$, contributing $120$ elements of order $11$.**

Assume $G$ is simple, so no $n_p = 1$. For $p = 11$ the constraints $n_{11} \equiv 1 \pmod{11}$, $n_{11} \mid 12$ leave $\{1, 12\}$; deleting $1$ gives $n_{11} = 12$. Since $11$ appears to the first power, this gives $12 \cdot 10 = 120$ elements of order $11$.

> [!note]- Derivation
> Factor $|G| = 132 = 2^2 \cdot 3 \cdot 11$. Suppose for contradiction that $G$ is [[Def - Simple Group|simple]]. If any $n_p = 1$, the unique [[Def - Sylow p-Subgroup|Sylow p-subgroup]] would be [[Thm - A Unique Sylow Subgroup is Normal|normal]] and proper non-trivial (its order is $p^a$ with $1 < p^a < 132$), contradicting simplicity. So
> $$n_p \neq 1 \quad \text{for all } p \in \{2, 3, 11\}.$$
>
> *The prime $11$.* With respect to $11$, $|G| = 11^1 \cdot 12$, so $m = 12$. [[Thm - Sylow's Theorems|Sylow III]] gives $n_{11} \mid 12$ and $n_{11} \equiv 1 \pmod{11}$. The divisors of $12$ are $1, 2, 3, 4, 6, 12$; modulo $11$ these are $1, 2, 3, 4, 6, 1$, so only $1$ and $12$ are $\equiv 1$. The constraints leave $n_{11} \in \{1, 12\}$, and simplicity deletes $1$, so
> $$n_{11} = 12.$$
>
> Since $11$ divides $132$ but $11^2 = 121$ does not, the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]] applies: each Sylow $11$-subgroup has order $11$, distinct ones meet only in $\{e\}$, and the number of elements of order $11$ is exactly
> $$n_{11}(11 - 1) = 12 \cdot 10 = 120.$$

**Step 2: The Sylow constraints leave $n_3 \in \{4, 22\}$.**

For $p = 3$ the constraints $n_3 \equiv 1 \pmod 3$, $n_3 \mid 44$ leave $\{1, 4, 22\}$; simplicity deletes $1$, leaving the two candidates $n_3 \in \{4, 22\}$.

> [!note]- Derivation
> With respect to the prime $3$, $|G| = 3^1 \cdot 44$, so $m = 44$. [[Thm - Sylow's Theorems|Sylow III]] gives $n_3 \mid 44$ and $n_3 \equiv 1 \pmod 3$.
>
> The divisors of $44 = 2^2 \cdot 11$ are $1, 2, 4, 11, 22, 44$. Reducing modulo $3$:
> $$1 \equiv 1,\quad 2 \equiv 2,\quad 4 \equiv 1,\quad 11 \equiv 2,\quad 22 \equiv 1,\quad 44 \equiv 2.$$
> The divisors congruent to $1 \pmod 3$ are $1, 4, 22$. So the bare constraints give $n_3 \in \{1, 4, 22\}$, and simplicity deletes $1$:
> $$n_3 \in \{4, 22\}.$$
>
> Two candidates remain, and they must be separated before the argument can proceed.

**Step 3: The value $n_3 = 4$ is impossible — it would embed $G$ into $S_4$.**

If $n_3 = 4$, the conjugation action of $G$ on its $4$ Sylow $3$-subgroups is faithful (its kernel is normal, hence trivial by simplicity, since the action is non-trivial). The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] then embeds $G$ into $S_4$. But $|S_4| = 24$ and $132 \nmid 24$ — impossible. So $n_3 = 22$.

> [!note]- Derivation
> Suppose, towards eliminating it, that $n_3 = 4$. Let $G$ act on the set $\operatorname{Syl}_3(G)$ of its $4$ Sylow $3$-subgroups by conjugation, $g \cdot P = gPg^{-1}$. This action is a [[Def - Homomorphism|homomorphism]]
> $$\varphi : G \longrightarrow \operatorname{Sym}(\operatorname{Syl}_3(G)) \cong S_4.$$
>
> By the [[Thm - Coset Action and the Normal Core|normal-core principle]], the kernel $\ker\varphi$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$. Since $G$ is [[Def - Simple Group|simple]], $\ker\varphi$ is either $\{e\}$ or $G$.
>
> It is not $G$: that would mean $\varphi$ is trivial, i.e. $gPg^{-1} = P$ for every $g$ and every Sylow $3$-subgroup $P$. But by [[Thm - Sylow's Theorems|Sylow II]] the conjugation action on $\operatorname{Syl}_3(G)$ is *transitive*, and with $n_3 = 4 > 1$ Sylow subgroups a transitive action cannot fix every point. So $\varphi$ is non-trivial and $\ker\varphi \neq G$.
>
> Therefore $\ker\varphi = \{e\}$: the homomorphism $\varphi$ is injective. By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], $G \cong \varphi(G) = \operatorname{im}\varphi$, which is a subgroup of $S_4$. By [[Thm - Lagrange's Theorem|Lagrange's theorem]], the order of a subgroup divides the order of the group, so
> $$|G| \;\Big|\; |S_4| = 4! = 24.$$
> But $|G| = 132$, and $132 \nmid 24$ (indeed $132 > 24$). This is a contradiction.
>
> Hence $n_3 = 4$ is impossible, and by Step 2 the only surviving value is
> $$n_3 = 22.$$

**Step 4: With $n_3 = 22$ there are $44$ elements of order $3$; the count overflows $G$.**

By the [[Ex - Counting elements of prime order with Sylow subgroups|counting fact]], $n_3 = 22$ gives $22 \cdot 2 = 44$ elements of order $3$. Together with the $120$ elements of order $11$, and these sets being disjoint, $G$ would contain at least $120 + 44 = 164$ elements — but $|G| = 132$.

> [!note]- Derivation
> The prime $3$ divides $|G| = 132$ but $3^2 = 9$ does not, so the [[Ex - Counting elements of prime order with Sylow subgroups|prime-order counting fact]] applies: each Sylow $3$-subgroup has order $3$, distinct ones meet only in $\{e\}$, and the number of elements of order $3$ is exactly
> $$n_3(3 - 1) = 22 \cdot 2 = 44.$$
>
> Let $A$ be the set of elements of order $11$ (size $120$, by Step 1) and $B$ the set of elements of order $3$ (size $44$). An element has a single order and $11 \neq 3$, so $A \cap B = \emptyset$, and neither set contains the identity. Hence
> $$|A \cup B| = |A| + |B| = 120 + 44 = 164.$$
> But $A \cup B \subseteq G$, so $164 = |A \cup B| \leq |G| = 132$ — that is, $164 \leq 132$, a contradiction.
>
> Every line since Step 1 used the standing assumption that $G$ is [[Def - Simple Group|simple]]; the contradiction refutes it. Therefore $G$ is **not simple**: no group of order $132$ is simple. $\blacksquare$

> [!note]- Complete formal solution
> Let $|G| = 132 = 2^2 \cdot 3 \cdot 11$ and suppose, for contradiction, that $G$ is [[Def - Simple Group|simple]]. Then no $n_p = 1$, since a unique [[Def - Sylow p-Subgroup|Sylow p-subgroup]] would be a proper non-trivial [[Thm - A Unique Sylow Subgroup is Normal|normal subgroup]].
>
> *The prime $11$.* Here $|G| = 11^1 \cdot 12$. By [[Thm - Sylow's Theorems|Sylow III]], $n_{11} \mid 12$ and $n_{11} \equiv 1 \pmod{11}$, leaving $n_{11} \in \{1, 12\}$; since $n_{11} \neq 1$, $n_{11} = 12$. As $11^2 \nmid 132$, distinct Sylow $11$-subgroups (cyclic of order $11$) meet only in $\{e\}$, so $G$ has exactly $n_{11}(11-1) = 12 \cdot 10 = 120$ elements of order $11$.
>
> *The prime $3$.* Here $|G| = 3^1 \cdot 44$. By Sylow III, $n_3 \mid 44$ and $n_3 \equiv 1 \pmod 3$; the divisors of $44$ congruent to $1$ modulo $3$ are $1, 4, 22$, so $n_3 \in \{4, 22\}$ after deleting $1$.
>
> *Eliminate $n_3 = 4$.* Suppose $n_3 = 4$. The conjugation action of $G$ on its $4$ Sylow $3$-subgroups gives $\varphi : G \to S_4$. By the [[Thm - Coset Action and the Normal Core|normal-core principle]], $\ker\varphi \trianglelefteq G$; simplicity forces $\ker\varphi \in \{\{e\}, G\}$. By [[Thm - Sylow's Theorems|Sylow II]] the action is transitive on $4 > 1$ points, so $\varphi$ is non-trivial and $\ker\varphi \neq G$; hence $\ker\varphi = \{e\}$. By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], $G$ embeds in $S_4$, so $|G| = 132$ divides $|S_4| = 24$ by [[Thm - Lagrange's Theorem|Lagrange]] — impossible. So $n_3 = 22$.
>
> *Count.* As $3^2 \nmid 132$, $G$ has exactly $n_3(3-1) = 22 \cdot 2 = 44$ elements of order $3$. The order-$11$ and order-$3$ elements form disjoint sets, so $G$ has at least $120 + 44 = 164$ elements. But $|G| = 132 < 164$ — a contradiction.
>
> Therefore $G$ is not simple. $\blacksquare$

---

# Key Takeaways

**When a Sylow count has more than one admissible value, eliminate the small ones with the embedding obstruction before counting.** This is the structural lesson that separates order $132$ from the easier orders $30$ and $56$. The Sylow $3$-count is two-valued, $\{4, 22\}$, and only the *large* value makes the element-count overflow $|G|$; the small value $n_3 = 4$ gives a harmless $4 \cdot 2 = 8$ extra elements. Element-counting therefore cannot run until $n_3 = 4$ is excised. The tool for excising a *small* Sylow count is the **action on the Sylow set**: $G$ acts on its $n_p$ Sylow $p$-subgroups, the action is faithful when $G$ is simple, so $G$ embeds in $S_{n_p}$ — and if $|G| \nmid n_p!$ this is impossible. The trigger is exact: a candidate value $n_p$ small enough that $|G| > n_p!$ (or more precisely $|G| \nmid n_p!$). Whenever you face a multi-valued Sylow count in a non-simplicity proof, scan the candidates for ones small enough to be killed by the embedding obstruction, kill them, and only then count with the survivors.

**The three Sylow tactics are designed to be chained, not chosen between.** The introductory framing of the playbook — uniqueness, then element-counting, then the Sylow-set action — can read as a menu from which one picks the applicable tactic. Order $132$ shows the truer picture: a single problem can need *all three at once, in sequence*. Uniqueness (via [[Thm - A Unique Sylow Subgroup is Normal]] in contrapositive) deletes the value $1$ from every count. The Sylow-set action then deletes the value $4$ from the Sylow $3$-count. Only with both deletions done is the count $n_3$ pinned to $22$, and only then does element-counting deliver the final overflow. Each tactic does a *different* job — one narrows $n_{11}$, one narrows $n_3$, one produces the contradiction — and they compose. The reusable discipline for a hard non-simplicity problem is to run the tactics as a pipeline: list every $n_p$, narrow each count as far as uniqueness allows, narrow further with embedding obstructions wherever a count stays multi-valued, and reserve element-counting for the final blow once every count is a single number.

**The embedding obstruction is the first isomorphism theorem turning a faithful action into a divisibility constraint.** The step that kills $n_3 = 4$ deserves to be understood as a self-contained reusable device. Any action of $G$ on a set of size $k$ is a homomorphism $\varphi : G \to S_k$; its kernel is the [[Thm - Coset Action and the Normal Core|normal core]] of the point stabilisers, hence *normal*. If $G$ is simple and the action is non-trivial, the kernel is forced to be $\{e\}$ — the action is *faithful* — and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] then realises $G$ as a subgroup of $S_k$, so [[Thm - Lagrange's Theorem|Lagrange]] demands $|G| \mid k!$. Contrapositively: *a simple group of order $|G|$ admits no non-trivial action on fewer than the smallest $k$ with $|G| \mid k!$ points.* For the Sylow-set action $k = n_p$, so a simple group cannot have a Sylow count $n_p$ with $|G| \nmid n_p!$. This obstruction is what handles non-simplicity for orders like $24$, $36$, and $48$, where element-counting alone stalls — and recognising "small action $\Rightarrow$ small symmetric group $\Rightarrow$ Lagrange violation" as a single move is one of the most transferable techniques in finite group theory.

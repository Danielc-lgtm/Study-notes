---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Linear Combination and Span"
  - "Def - Linear Independence"
  - "Def - Finite-Dimensional Vector Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional vector space over $F$. The full notation registry is on the parent topic page [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

---

# Statement

> **Theorem (Length inequality, LADR 2.22 — Steinitz exchange).** In a finite-dimensional vector space, the length of every [[Def - Linear Independence|linearly independent list]] is less than or equal to the length of every [[Def - Linear Combination and Span|spanning list]].

> **Corollary 1 (Length of basis is invariant, LADR 2.34).** Any two bases of a finite-dimensional vector space have the same length.

> **Corollary 2 (Linearly independent list of right length is a basis, LADR 2.38).** In a finite-dimensional vector space $V$ with $\dim V = n$, every linearly independent list of length $n$ is a basis.

> **Corollary 3 (Spanning list of right length is a basis, LADR 2.42).** In a finite-dimensional vector space $V$ with $\dim V = n$, every spanning list of length $n$ is a basis.

The corollaries follow rapidly from the theorem and the structure theorems of §2B; their proofs are sketched in **Why Is It True** below.

---

# Motivation

The theorem is the chapter's central computational fact. Its plain statement — *any independent list is at most as long as any spanning list* — is unassuming, but the consequences are enormous. Most immediately it gives well-definedness of [[Def - Dimension|dimension]]: applying the inequality twice in opposite directions to two bases of $V$ forces them to have the same length. The integer "[[Def - Dimension|dimension]]" then drops out as a basis-independent invariant, and almost every result of finite-dimensional linear algebra is a corollary.

The theorem also provides the chapter's main *bound*. Whenever you produce a linearly independent list in a space whose spanning list of length $n$ is known, you have at most $n$ vectors in your list — no matter how cleverly you chose them. This converts the abstract question "can I find a list of $n+1$ independent vectors here?" into the concrete impossibility "no, the spanning list caps it at $n$". The corollaries inherit this rigidity: a list of length exactly $n$ in an $n$-dimensional space cannot be properly extended to an independent list, so an independent list of length $n$ is *already* a basis without further work. The length-of-basis shortcut is the most-used computational consequence of the theorem.

Historically, the result was proved by Ernst Steinitz in 1913 in the form of an **exchange procedure** — feed the independent vectors into the spanning list one at a time, swap out a spanning vector at each step. The exchange procedure is the proof, and it generalises far beyond vector spaces to *matroids* and *dependence relations*, where the same length inequality drives the same well-definedness of rank. So although the result is stated for vector spaces, the argument is genuinely structural: anywhere you have a closure operator with the exchange property, you have a notion of dimension.

---

# Sources and Targets

**Sources (Input Broadening).**

The theorem's hypothesis is very plain — *any* linearly independent list and *any* spanning list in a finite-dimensional space. The skill is recognising that a problem provides one of each, even when neither is named explicitly.

A first source is **two given lists with comparison-of-length sought**. Property $B$: "you are given two lists in $V$ and asked which is longer, or whether one fits inside the other." The bridge: if one list is shown independent and the other shown spanning, the theorem applies directly. The non-obvious step is recognising that a comparison question is a length-inequality question — the student tries to compare element by element and gets nowhere, whereas the theorem compares lengths directly. Example problem: "show no list of $4$ polynomials spans $\mathcal{P}_4(F)$" — the source is the independent list $1, z, z^2, z^3, z^4$ of length $5$, and the theorem forbids a shorter spanning list.

A second source is **a subspace $U \subseteq V$ of unknown dimension**. Property $B$: "you have a subspace and want to bound its dimension." The bridge: any basis of $U$ is a linearly independent list in $V$, while any spanning list of $V$ is also a spanning list of $\operatorname{span}(...) = V \supseteq U$. The theorem gives $\dim U \leq \dim V$ — exactly the inequality used in [[Ex - Dimension of a subspace equals dimension only if equal]]. This is a key source in §2C, where bounding subspace dimensions is most of the work.

A third source is **a list whose dimensions sum to too much**. Property $B$: "you have lists from two subspaces whose lengths sum to more than $\dim V$." The bridge: concatenating gives a long list in $V$. Independence of the concatenation would contradict 2.22, so dependence forces a relation across the two pieces — typically yielding a nonzero element of the intersection of the two subspaces. This is exactly how [[Thm - Dimension of a Sum of Subspaces|2.43]] feeds back into existence-of-intersection arguments, and it is the engine behind LADR exercises 2C.13, 2C.14, 2C.15.

A fourth source is **a homomorphism between vector spaces of different dimensions**. Property $B$: "you have a linear map $T : V \to W$ with $\dim V > \dim W$, or vice versa." The bridge: the image of a basis of $V$ is a list of length $\dim V$ in $W$; if $T$ is injective, that list is independent (since $T$ injective preserves independence — see [[Linear Algebra III — §3A–D Linear Maps]]); by 2.22 this is impossible if $\dim V > \dim W$. So an injective linear map $V \to W$ forces $\dim V \leq \dim W$, and dually a surjective one forces $\dim V \geq \dim W$. This source pre-figures the rank-nullity theorem of [[Linear Algebra III — §3A–D Linear Maps]].

**Targets (Output Amplification).**

The conclusion of 2.22 is a numerical inequality. Combining it with one further fact produces structural results.

A first combination is **inequality plus equality of one direction forces a basis**. The theorem says any independent list has length $\leq$ any spanning list. If the lengths are *equal*, then the independent list is *itself* a basis, by an extension-and-no-room argument: extend to a basis by [[Thm - Every Linearly Independent List Extends to a Basis|2.32]], but the basis has length $\dim V$, so no extension is possible — the independent list was already a basis. The dual combination (spanning + right length = basis) gives [[Thm - Every Spanning List Contains a Basis|2.30]]'s extremal case. These are the length-of-basis shortcuts, **the single most-used consequence of 2.22 in problems**.

A second combination is **inequality plus a count of free parameters forces an isomorphism**. The theorem caps the dimension of a subspace; combined with the property "$\dim U \geq k$" derived from $k$ explicit independent vectors of $U$, it sandwiches $\dim U$ to exactly $k$. The non-obvious result is that knowing $k$ vectors in $U$ are independent, plus $U \subseteq F^n$, plus $k = n$ minus a count of free parameters, forces $U = F^n$ or any other complete characterisation. This is the technique used in essentially every "find a basis of $U$ where $U$ is defined by linear equations" problem.

A third combination is **the dimension formula 2.43 plus pigeonhole**. Combining 2.43 ($\dim(V_1 + V_2) = \dim V_1 + \dim V_2 - \dim(V_1 \cap V_2)$) with the inequality $\dim(V_1 + V_2) \leq \dim V$ (which is 2.22 applied to the subspace $V_1 + V_2 \subseteq V$) gives the pigeonhole consequence $\dim(V_1 \cap V_2) \geq \dim V_1 + \dim V_2 - \dim V$. This is the technique behind problems like "two $5$-dimensional subspaces of $\mathbb{R}^9$ must meet nontrivially" — applied directly, the calculation is $5 + 5 - 9 = 1 > 0$.

A fourth combination is **the inequality plus a known basis of one side forces equality of dimensions on the other**. If $V_1 \subseteq V_2$ and you have a basis of $V_1$ of length $n$, and you can find a list of length $n$ in $V_2$ that is independent, then by 2.22 you have $\dim V_2 \geq n = \dim V_1$. Combined with $V_1 \subseteq V_2 \implies \dim V_1 \leq \dim V_2$, you get $\dim V_1 = \dim V_2$, hence $V_1 = V_2$ by [[Ex - Dimension of a subspace equals dimension only if equal]]. This routing — count, count, conclude equality of spaces — is the standard "show two subspaces are equal" pattern.

---

# Why Is It True

The intuition is **the Steinitz exchange**: an independent list, fed into a spanning list one vector at a time, displaces a spanning vector at each step, and *never runs out* of spanning vectors to displace.

Imagine the spanning list $w_1, \ldots, w_n$ as a stack of $n$ tickets that get traded in for the independent list's vectors $u_1, \ldots, u_m$. At step 1, you toss $u_1$ into the stack to make a list of length $n+1$. This list is linearly dependent because $u_1$ is in the span of the $w$'s (the $w$'s span everything). By the linear dependence lemma, *one of the vectors in the new list is a linear combination of its predecessors*. The first vector is $u_1$, which is nonzero (independence of $u_1$ alone, since the $u$'s are independent), so the redundant vector cannot be $u_1$. Hence it must be some $w_j$. Remove $w_j$. The remaining list — $u_1$ plus $n - 1$ of the $w$'s — still spans, and has length $n$.

At step $k$, the current list is $u_1, \ldots, u_k$ plus $n - k + 1$ of the surviving $w$'s, and it still spans. Toss $u_{k+1}$ in (placed after $u_k$, before the surviving $w$'s) to get a list of length $n + 1$ that is dependent ($u_{k+1}$ is in its predecessors' span). By the linear dependence lemma, some vector is a combination of its predecessors. It cannot be any of the $u$'s — independence of $u_1, \ldots, u_{k+1}$ forbids any $u_i$ being in the span of the earlier ones — so it is a $w$. Remove that $w$, and the list has length $n$ again, now containing $u_1, \ldots, u_{k+1}$ and $n - k - 1$ of the $w$'s.

Repeating $m$ times feeds in all the $u$'s and removes $m$ of the $w$'s. The process **never gets stuck** — at every step there is a $w$ available to remove, because the redundant vector at that step *must* be a $w$. The only way the process can run out of $w$'s is if $m > n$, which would mean we tried to remove an $n+1$st $w$ when there are only $n$. But the lemma guarantees we *can* remove one at each step up to and including step $m$, so $m \leq n$.

The single bolded one-liner: **independence of the $u$'s ensures that the redundancy lemma displaces a $w$ at every step, so there are at least as many $w$'s as $u$'s**.

The corollaries follow rapidly. Two bases of $V$: one is independent and the other spans, so the lengths are bidirectionally bounded — they are equal. An independent list of length $n = \dim V$ extends to a basis ([[Thm - Every Linearly Independent List Extends to a Basis|2.32]]) of length $n$, so the extension adds zero vectors, so the original list is a basis. A spanning list of length $n$ reduces to a basis ([[Thm - Every Spanning List Contains a Basis|2.30]]) of length $n$, so the reduction removes zero vectors, so the original list is a basis.

---

# What Makes This Hard

The non-obvious step is the **claim that the redundant vector is a $w$, not a $u$, at every step**. Students often mis-state the linear dependence lemma as "some vector is in the span of the others", which would allow the redundancy to land on a $u$ and break the argument. The correct statement is "some vector is in the span of the *previous ones* in the list", and to make this work the $u$'s must be placed *first* in the list (in the order $u_1, \ldots, u_k$, then the surviving $w$'s) so that the independence of the $u_i$'s prevents the redundancy from landing on any $u_i$. The order of the list is load-bearing; reorder it and the proof breaks.

A second common error is to claim that the procedure stops only when all $u$'s have been inserted — but the procedure could equally well "fail" by running out of $w$'s. The argument that this *cannot happen* is the bite of the proof: at step $k+1$ there is at least one $w$ remaining (because there are $n - k$ $w$'s currently in the list, and the new vector $u_{k+1}$ enters making length $n + 1$, with the redundancy being one of the existing list members; that redundancy can only be one of the $w$'s, so $n - k \geq 1$, i.e. $k \leq n - 1$, i.e. the procedure can run for at least $n$ steps). The careful inequality bookkeeping is what makes the proof go.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:** Run an exchange procedure that, at each of $m$ steps, inserts one independent vector $u_k$ into a copy of the spanning list and immediately removes a redundant spanning vector $w$. The list maintained throughout is a spanning list of length $n$. The argument that the procedure does not get stuck is: at each step, the inserted $u_k$ creates a linearly dependent list, by the linear dependence lemma some vector is a combination of its predecessors, and independence of the $u$'s forces it to be a $w$.

**Subgoal decomposition:**

1. **Setup.** Place $u_1, \ldots, u_m$ first, then $w_1, \ldots, w_n$. The combined list has length $m + n$. It spans (because the $w$'s do). Argue we will remove $m$ of the $w$'s in a particular order.
   - *Hint:* The trick is the order — independent list first, then spanning list.
   - *Why needed:* The linear dependence lemma identifies a redundant vector as a combination of its *predecessors*; placing the $u$'s first ensures that the redundant vector at each step is a $w$, not a $u$.

2. **Single-step exchange.** Given a current list of the form $u_1, \ldots, u_k, w_{i_1}, \ldots, w_{i_{n-k}}$ that spans $V$, insert $u_{k+1}$ after $u_k$ to get a list of length $n + 1$. Show that this longer list is linearly dependent, so by the linear dependence lemma some vector is a combination of its predecessors. Show that vector cannot be $u_{k+1}$ (since $u_{k+1}$ is not in the span of $u_1, \ldots, u_k$, by linear independence of $u_1, \ldots, u_{k+1}$) — so it is one of the $w$'s. Remove that $w$; the new list of length $n$ still spans (linear dependence lemma's "removing the redundant vector preserves the span") and now contains $u_1, \ldots, u_{k+1}$.
   - *Hint:* The redundant vector being one of the predecessors, and not a $u$, is the crucial bookkeeping.
   - *Why needed:* This is the engine of the entire argument — the exchange step that gets repeated.

3. **Termination.** After $m$ steps, all of $u_1, \ldots, u_m$ have been inserted and $m$ of the $w$'s removed. For the process to have run for all $m$ steps, the supply of $w$'s must not have been exhausted earlier — but the procedure ensures the list is always length $n$ after each step, so as long as we have not removed *more* than $n$ $w$'s, we are fine. Hence $m \leq n$.
   - *Hint:* Bookkeeping. Each step removes one $w$; the procedure runs for $m$ steps; the initial $w$-list has length $n$.
   - *Why needed:* This is the conclusion.

4. **Derive corollaries.** Two bases: bidirectional inequality gives equality. Independent list of length $\dim V$: extension preserves length, so no extension is needed, list is already a basis. Spanning list of length $\dim V$: reduction preserves length, so no reduction is needed, list is already a basis.
   - *Hint:* Each corollary is a one-line application of 2.22 to a special case.

---

# Lemma Decomposition

> [!note]- Lemma 1: Insertion of a dependent vector produces a dependent list
> **Statement:** Let $w_1, \ldots, w_n$ span $V$, and let $u \in V$. Then the list $u, w_1, \ldots, w_n$ is linearly dependent.
>
> **Hint:** $u$ is in the span of the $w$'s.
>
> **Why needed:** This is the starting observation for each exchange step. It is what gives us a redundant vector to remove.
>
> > [!note]- Full proof
> > Since $w_1, \ldots, w_n$ spans $V$, we have $u \in V = \operatorname{span}(w_1, \ldots, w_n)$, so $u = a_1 w_1 + \cdots + a_n w_n$ for some $a_i \in F$. Then $u - a_1 w_1 - \cdots - a_n w_n = 0$ is a non-trivial vanishing combination (the coefficient of $u$ is $1 \neq 0$). Hence the list $u, w_1, \ldots, w_n$ is linearly dependent.

> [!note]- Lemma 2: The redundant vector is a $w$, not a $u$
> **Statement:** In the list $u_1, \ldots, u_k, u_{k+1}, w_{i_1}, \ldots, w_{i_{n-k}}$ (with the $u$'s independent and the list spanning $V$), if the list is linearly dependent and the linear dependence lemma identifies a vector as a combination of its predecessors, that vector is one of the $w_{i_j}$.
>
> **Hint:** Independence of $u_1, \ldots, u_{k+1}$ rules out the $u$'s.
>
> **Why needed:** This is the crux of the argument. Without it, the exchange procedure could "stall" by removing a $u$ and undoing its own work.
>
> > [!note]- Full proof
> > Suppose for contradiction the redundant vector is $u_j$ for some $j \in \{1, \ldots, k+1\}$. By the linear dependence lemma, $u_j$ is in the span of its predecessors. If $j = 1$, the predecessors are empty, so $u_1 \in \{0\}$, meaning $u_1 = 0$ — but a list containing zero is dependent, contradicting independence of $u_1, \ldots, u_{k+1}$. If $j \geq 2$, the predecessors are $u_1, \ldots, u_{j-1}$, so $u_j \in \operatorname{span}(u_1, \ldots, u_{j-1})$. But this would express $u_j$ as a combination of preceding $u$'s, giving a nontrivial vanishing combination of $u_1, \ldots, u_j$ — contradicting independence of $u_1, \ldots, u_{k+1}$. So the redundant vector is not a $u_j$; it must be a $w_{i_j}$.

> [!note]- Lemma 3: Each exchange preserves spanning
> **Statement:** If $u_1, \ldots, u_k, w_{i_1}, \ldots, w_{i_{n-k}}$ spans $V$, and we insert $u_{k+1}$ after $u_k$ and remove a $w_{i_j}$ identified as a combination of the previous vectors, then the new list of length $n$ still spans $V$.
>
> **Hint:** This is the second part of the linear dependence lemma — removing the redundant vector preserves the span.
>
> **Why needed:** It maintains the invariant of the procedure (always spanning) so that the next exchange step can be performed.
>
> > [!note]- Full proof
> > By the linear dependence lemma, removing a vector that is a linear combination of the previous ones from a list does not change the span. So removing $w_{i_j}$ from the list of length $n + 1$ produces a list of length $n$ with the same span, namely $V$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** In a finite-dimensional vector space $V$, if $u_1, \ldots, u_m$ is linearly independent in $V$ and $w_1, \ldots, w_n$ spans $V$, then $m \leq n$.
>
> *Proof.* We describe an $m$-step procedure that maintains a current list $B$ of length $n$ that spans $V$.
>
> **Step 0** (initialisation). Set $B = w_1, \ldots, w_n$. By hypothesis, $B$ spans $V$ and has length $n$.
>
> **Step $k$** for $k = 1, 2, \ldots, m$. Insert $u_k$ into the current list $B$ immediately after $u_{k-1}$ (or at the beginning if $k = 1$); call the new list $B'$. By construction, $B'$ has the form
> $$u_1, u_2, \ldots, u_k, w_{i_1}, \ldots, w_{i_{n-k+1}}$$
> for some $n - k + 1$ surviving $w$'s. The list $B'$ has length $n + 1$ and spans $V$ (since adding a vector to a spanning list does not lose any spanning, and the previous $B$ already spanned $V$).
>
> Because $B'$ spans $V$ and $u_k \in V$, applying Lemma 1 (with $u_k$ playing the role of $u$ and the rest of $B'$ playing the role of $w_1, \ldots, w_n$) the list $B'$ is linearly dependent. By the linear dependence lemma (LADR 2.19), some vector in $B'$ is in the span of its predecessors, and removing that vector preserves the span $V$.
>
> By Lemma 2, the redundant vector must be one of the $w_{i_j}$ (not a $u$, because the $u$'s are independent). Remove that $w_{i_j}$ from $B'$; the result is a list $B$ of length $n$ that still spans $V$ (by Lemma 3) and contains $u_1, \ldots, u_k$ as its first $k$ entries.
>
> **Termination.** After step $m$, the current list $B$ has length $n$, spans $V$, and contains $u_1, \ldots, u_m$. The original $n$ spanning vectors $w_1, \ldots, w_n$ have been reduced to $n - m$ surviving $w$'s. For this to be possible, we must have removed at most $n$ $w$'s in total — i.e. $m \leq n$. $\qquad\blacksquare$
>
> **Corollary 1 (LADR 2.34).** Any two bases $B_1, B_2$ of $V$ have the same length. Apply the theorem with $B_1$ independent and $B_2$ spanning to get $|B_1| \leq |B_2|$; reverse roles to get $|B_2| \leq |B_1|$. Hence $|B_1| = |B_2|$. $\qquad\blacksquare$
>
> **Corollary 2 (LADR 2.38).** Every linearly independent list of length $n = \dim V$ in $V$ is a basis. *Proof:* By [[Thm - Every Linearly Independent List Extends to a Basis|LADR 2.32]] the list extends to a basis of $V$; but the basis has length $n$ by Corollary 1, so the extension is trivial (no new vectors added), and the original list was already a basis. $\qquad\blacksquare$
>
> **Corollary 3 (LADR 2.42).** Every spanning list of length $n = \dim V$ in $V$ is a basis. *Proof:* By [[Thm - Every Spanning List Contains a Basis|LADR 2.30]] the list reduces to a basis of $V$; but the basis has length $n$, so the reduction is trivial. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Matroid theory: rank is well-defined.** The Steinitz exchange property is one of the equivalent axiomatisations of a **matroid**, and the length inequality 2.22 generalises to matroids almost verbatim: the rank — the size of any maximal independent set — is well-defined. The proof is the same exchange procedure with "independent set" and "spanning set" replaced by the matroid versions. Applications: in a graphic matroid, the rank of an edge set equals the number of edges minus the number of components of the spanning subgraph; in a transversal matroid, the rank equals the maximum size of a partial matching in a bipartite graph.

**Algebraic independence in fields: transcendence degree.** Given a field extension $K \subseteq L$, a subset $S \subseteq L$ is **algebraically independent over $K$** if no polynomial in $K[x_1, \ldots, x_n]$ in finitely many elements of $S$ evaluates to zero. The **transcendence degree** $\operatorname{trdeg}_K(L)$ is the cardinality of any maximal algebraically independent set, and the analogue of 2.22 holds: any algebraically independent set is at most as large as any algebraically spanning set (in the sense of generating an algebraic extension). The transcendence degree of $\mathbb{C}$ over $\mathbb{Q}$ is uncountable, and the Steinitz argument is essential to making the cardinality comparison work.

**Combinatorics: the bipartite matching problem.** In a bipartite graph with parts $A, B$ and edge set $E$, the matching matroid on $A$ has independent sets being the subsets of $A$ that can be saturated by some matching. The rank of the full matroid is the maximum matching size. The Steinitz-like exchange in this setting is Hall's theorem (a subset $S \subseteq A$ has a saturating matching iff for every $T \subseteq S$, the neighborhood of $T$ in $B$ is at least as large as $T$). The whole edifice of matching theory is, conceptually, a Steinitz argument in disguise.

**Functional analysis: countable dimension forbids infinite linear independence.** In a Banach space $X$, an infinite linearly independent list cannot have its span equal to a countable-dimensional space. This is a quick application of 2.22's spirit: if the span were countable-dimensional, with countable basis $b_1, b_2, \ldots$, then the truncated sub-spans $\operatorname{span}(b_1, \ldots, b_n)$ would be finite-dimensional and 2.22 would cap the size of independent sets in each — but the union of these finite-dimensional [[Def - Subspace|subspaces]] is the full countable-dimensional span, while an infinite independent list extends through all of them.

---

# Bridges

- **[[Thm - Bases are Equinumerous]]** — Corollary 1 of 2.22 *is* this theorem. The reason we get this corollary is that one basis is independent, the other spans, and the inequality is bidirectional. Without 2.22 the notion of dimension would not even be well-defined; without dimension, almost no later theorem of linear algebra would be statable. So 2.22 is the *enabling* result for the entire chapter.

- **[[Thm - Every Linearly Independent List Extends to a Basis]]** and **[[Thm - Every Spanning List Contains a Basis]]** — these structural theorems combine with 2.22 to give Corollaries 2 and 3 above, the length-of-basis shortcuts. The structural theorems supply the *extension* and *reduction*, while 2.22 supplies the *no-room-to-extend* and *no-room-to-reduce* observations. Together they install the integer $\dim V$ as the precise measure of a basis's length.

- **The Steinitz exchange property in matroid theory** — the proof of 2.22 used only two facts: that spanning lists generate everything, and that the linear dependence lemma identifies a redundant vector among the predecessors. Abstract these to a general **closure operator** with the exchange property (if $x \in \operatorname{cl}(S \cup \{y\})$ and $x \notin \operatorname{cl}(S)$ then $y \in \operatorname{cl}(S \cup \{x\})$) and you get the theory of **matroids**, in which rank is well-defined by the same argument. So 2.22 is one instance of a general structural theorem. The Algebra of Linear Independence (Whitney 1935, Mac Lane 1936) is the locus classicus.

- **Rank-nullity (LADR 3.21, [[Linear Algebra III — §3A–D Linear Maps]])** — for a linear map $T : V \to W$ on a finite-dimensional domain, $\dim V = \dim \ker T + \dim \operatorname{range} T$. This is a dimension equation, and its proof uses [[Thm - Every Linearly Independent List Extends to a Basis|2.32]] (which uses 2.22) to extend a basis of $\ker T$ to a basis of $V$. So 2.22 propagates: it underlies the very next chapter's central result.

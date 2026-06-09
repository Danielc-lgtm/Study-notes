---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Noetherian and Artinian Module"
  - "Def - Composition Series and Length"
  - "Thm - Length is Additive and Finite iff Noetherian and Artinian"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be a field and $V$ a $k$-vector space (a $k$-module). Prove that the following four conditions are equivalent:

1. $\dim_k V < \infty$;
2. $\ell(V) < \infty$ (finite [[Def - Composition Series and Length|length]]);
3. $V$ is [[Def - Noetherian and Artinian Module|Noetherian]];
4. $V$ is [[Def - Noetherian and Artinian Module|Artinian]].

Moreover, when these hold, $\ell(V) = \dim_k V$.

(This is Example Sheet 2, Question 1(d). The content is that over a field, the entire chain-condition apparatus of the chapter collapses to a single number — the dimension — so the phenomena that make Noetherian and Artinian *independent* cannot occur over a field.)

**Recall:**

![[Def - Noetherian and Artinian Module#Noetherian module]]

![[Def - Noetherian and Artinian Module#Artinian module]]

For a $k$-vector space the [[Def - Submodule|submodules]] are exactly the $k$-subspaces. A [[Def - Composition Series and Length|composition series]] of $V$ is a maximal chain of subspaces $V = V_0 \supsetneq \cdots \supsetneq V_n = 0$ with each quotient $V_i/V_{i+1}$ **simple**; over a field, a simple module is a one-dimensional space, so a composition series is a maximal flag with one-dimensional successive quotients, and $\ell(V) = \dim_k V$ when finite. The finiteness criterion [[Thm - Length is Additive and Finite iff Noetherian and Artinian|finite length ⟺ Noetherian and Artinian]] does most of the work.

---

# Convergent Strategy

**Problem class.** This is an *equivalence-of-finiteness-conditions* problem, the place in [[Commutative Algebra I — Chain Conditions#Problem-Solving Strategy|the chapter]] where the general theory is shown to *collapse* over a field. The target is a four-way equivalence; the strategy is to route everything through the dimension, using that subspaces of a vector space are controlled by dimension alone.

**Assumption pattern.** The crucial feature of a *field* base is that every subspace has a well-defined dimension and every strict inclusion of subspaces strictly changes dimension by at least $1$. The recognisable trigger is "submodules over a field $=$ subspaces $=$ controlled by an integer dimension". This is exactly what makes both chain conditions equivalent to finite dimension: a strict chain of subspaces strictly changes dimension at each step, so it can have at most $\dim V + 1$ terms.

**Theorem routing.** The route is a cycle. (1) $\dim_k V < \infty \Rightarrow$ both Noetherian and Artinian: a strict chain of subspaces changes dimension by $\geq 1$ per step, so has $\leq \dim V + 1$ terms and stabilises (both ascending and descending). (2) Noetherian $\Rightarrow \dim_k V < \infty$, and Artinian $\Rightarrow \dim_k V < \infty$: if $\dim V = \infty$, pick a countable independent set $v_1, v_2, \dots$ and form the ascending chain $\langle v_1\rangle \subsetneq \langle v_1, v_2\rangle \subsetneq \cdots$ (kills Noetherian) and the descending chain $\langle v_1, v_2, \dots\rangle \supsetneq \langle v_2, v_3, \dots\rangle \supsetneq \cdots$ (kills Artinian). (3) The finiteness criterion [[Thm - Length is Additive and Finite iff Noetherian and Artinian|finite length ⟺ Noetherian and Artinian]] ties $\ell$ to (3) and (4), and $\ell = \dim$ comes from a one-dimensional-quotient flag. The key tool is "dimension changes strictly across strict inclusions".

**Key decision point.** The non-obvious construction is, for the infinite-dimensional case, building *both* a non-stabilising ascending chain *and* a non-stabilising descending chain from a single infinite independent set. The ascending one is the obvious "$\langle v_1, \dots, v_n\rangle$"; the descending one — "$\langle v_n, v_{n+1}, \dots\rangle$" — is less obvious and is what shows Artinian *also* fails in infinite dimension. The genuine insight is that over a field neither chain condition can hold without finite dimension, because the two failures are symmetric (build up from a finite set, or pare down from an infinite set). The natural error is to prove only Noetherian fails and forget that the *descending* chain must also be exhibited to handle Artinian.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra I — Chain Conditions#Legal Operations|the topic page's Legal Operations]]:

1. **Operation 4 (refute a chain condition with one explicit chain), used twice.** In the infinite-dimensional case, exhibit a strictly ascending chain $\langle v_1, \dots, v_n\rangle$ (to refute Noetherian) and a strictly descending chain $\langle v_n, v_{n+1}, \dots\rangle$ (to refute Artinian).

2. **Bound chain length by dimension.** In the finite-dimensional case, use that a strictly monotone chain of subspaces changes dimension by $\geq 1$ at each step, so has at most $\dim_k V + 1$ terms — giving both chain conditions.

3. **Operation 8 / refine to a composition series, and the finiteness criterion.** Use [[Thm - Length is Additive and Finite iff Noetherian and Artinian|finite length ⟺ Noetherian and Artinian]] and a one-dimensional-quotient flag to get $\ell(V) = \dim_k V$.

---

# Hints

> [!note]- Hint 1
> Over a field, submodules are subspaces, and subspaces are controlled by a single number: dimension. A strict inclusion of subspaces $U \subsetneq W$ forces $\dim U < \dim W$. What does this say about the length of a chain of subspaces in a finite-dimensional $V$?

> [!note]- Hint 2
> If $\dim_k V = d < \infty$: any strictly monotone chain of subspaces has dimensions changing by $\geq 1$ each step, so at most $d+1$ terms — it stabilises. This gives both Noetherian and Artinian from finite dimension.

> [!note]- Hint 3
> Conversely, if $\dim_k V = \infty$, pick an infinite linearly independent set $v_1, v_2, v_3, \dots$. Build $\langle v_1\rangle \subsetneq \langle v_1, v_2\rangle \subsetneq \cdots$ — this is strictly ascending, so Noetherian fails. Now build a strictly *descending* chain from the same set to show Artinian fails too.

> [!note]- Hint 4
> For Artinian: the chain $\langle v_1, v_2, v_3, \dots\rangle \supsetneq \langle v_2, v_3, \dots\rangle \supsetneq \langle v_3, v_4, \dots\rangle \supsetneq \cdots$ is strictly descending (each omits one more basis vector). So infinite dimension kills Artinian as well. Finally, for $\ell(V) = \dim V$: a composition series of a finite-dimensional $V$ is a flag with one-dimensional quotients, so the number of steps is $\dim V$; combine with the criterion $\ell < \infty \iff$ Noetherian and Artinian.

---

# Solution

The proof routes all four conditions through the dimension. Finite dimension bounds every chain (giving both chain conditions); infinite dimension supplies an explicit ascending *and* descending non-stabilising chain (killing both); and the length equals the dimension because a composition series of a vector space is a flag with one-dimensional quotients. The non-obvious step is the descending chain $\langle v_n, v_{n+1}, \dots\rangle$ in the infinite-dimensional case.

**Step 1: $\dim_k V < \infty \Rightarrow V$ is both Noetherian and Artinian.**

> [!note]- Derivation
> Suppose $\dim_k V = d < \infty$. Let $W_1 \subsetneq W_2 \subsetneq \cdots$ be any strictly ascending chain of subspaces. For each strict inclusion $W_i \subsetneq W_{i+1}$ we have $\dim_k W_i < \dim_k W_{i+1}$, so the dimensions $\dim_k W_1 < \dim_k W_2 < \cdots$ form a strictly increasing sequence of integers bounded above by $d$. Such a sequence has at most $d+1$ terms, so the chain has at most $d+1$ members and therefore stabilises — $V$ is Noetherian. The identical argument with $\supsetneq$ (dimensions strictly *decreasing*, bounded below by $0$) shows every strictly descending chain has at most $d+1$ terms, so $V$ is Artinian.

**Step 2: $V$ Noetherian $\Rightarrow \dim_k V < \infty$, and $V$ Artinian $\Rightarrow \dim_k V < \infty$ (contrapositives).**

> [!note]- Derivation
> Suppose $\dim_k V = \infty$. Choose an infinite linearly independent set $\{v_1, v_2, v_3, \dots\} \subseteq V$ (possible since $V$ is infinite-dimensional).
>
> *Noetherian fails.* The subspaces $W_n = \langle v_1, \dots, v_n\rangle$ satisfy $W_n \subsetneq W_{n+1}$ (strict because $v_{n+1} \notin W_n$ by linear independence), so $W_1 \subsetneq W_2 \subsetneq \cdots$ is a strictly ascending chain that never stabilises. Hence $V$ is not Noetherian.
>
> *Artinian fails.* Let $U_n = \langle v_n, v_{n+1}, v_{n+2}, \dots\rangle$, the span of the tail. Then $U_n \supsetneq U_{n+1}$: clearly $U_{n+1} \subseteq U_n$, and the inclusion is strict because $v_n \in U_n \setminus U_{n+1}$ (by linear independence, $v_n$ is not in the span of $v_{n+1}, v_{n+2}, \dots$). So $U_1 \supsetneq U_2 \supsetneq U_3 \supsetneq \cdots$ is a strictly descending chain that never stabilises. Hence $V$ is not Artinian.
>
> Contrapositively: Noetherian $\Rightarrow \dim_k V < \infty$, and Artinian $\Rightarrow \dim_k V < \infty$.

**Step 3: Assemble the equivalence and prove $\ell(V) = \dim_k V$.**

> [!note]- Derivation
> Combining Steps 1 and 2: $\dim_k V < \infty \iff V$ Noetherian $\iff V$ Artinian. (Finite dimension gives both by Step 1; either chain condition gives finite dimension by Step 2.) This is conditions (1), (3), (4) all equivalent.
>
> For (2): by [[Thm - Length is Additive and Finite iff Noetherian and Artinian|the finiteness criterion]], $\ell(V) < \infty \iff V$ is both Noetherian and Artinian. By the above, "both Noetherian and Artinian" is equivalent to $\dim_k V < \infty$. So $\ell(V) < \infty \iff \dim_k V < \infty$, adding (2) to the equivalence.
>
> *The numerical equality.* Suppose $\dim_k V = d < \infty$. Choose a basis $e_1, \dots, e_d$ and form the flag
> $$V = \langle e_1, \dots, e_d\rangle \supsetneq \langle e_1, \dots, e_{d-1}\rangle \supsetneq \cdots \supsetneq \langle e_1 \rangle \supsetneq 0.$$
> Each successive quotient $\langle e_1, \dots, e_i\rangle / \langle e_1, \dots, e_{i-1}\rangle$ is one-dimensional over $k$, hence simple (a one-dimensional space has no proper non-zero subspace). So this flag is a composition series of length $d$, and $\ell(V) = d = \dim_k V$.

> [!note]- Complete formal solution
> **Claim.** For a $k$-vector space $V$: $\dim_k V < \infty \iff \ell(V) < \infty \iff V$ Noetherian $\iff V$ Artinian, and then $\ell(V) = \dim_k V$.
>
> *Finite dimension $\Rightarrow$ both chain conditions.* A strict chain of subspaces has strictly monotone dimensions bounded between $0$ and $\dim_k V$, so has $\leq \dim_k V + 1$ terms and stabilises. Hence $V$ is Noetherian and Artinian.
>
> *Infinite dimension $\Rightarrow$ neither.* With $\{v_i\}$ infinite independent, $\langle v_1, \dots, v_n\rangle$ strictly ascends (no Noetherian) and $\langle v_n, v_{n+1}, \dots\rangle$ strictly descends (no Artinian).
>
> So (1), (3), (4) are equivalent. By [[Thm - Length is Additive and Finite iff Noetherian and Artinian|finite length ⟺ Noetherian and Artinian]], (2) joins them. Finally a basis flag with one-dimensional quotients is a composition series of length $\dim_k V$, so $\ell(V) = \dim_k V$. $\blacksquare$

---

# Key Takeaways

**Over a field, the entire chain-condition apparatus collapses to dimension — Noetherian, Artinian, finite length, and finite-dimensional are one condition.** This is the calibrating fact of the chapter: all the machinery of chain conditions and length, which over a general ring distinguishes genuinely different finiteness phenomena, reduces over a field to the single familiar invariant $\dim_k V$, with $\ell = \dim$. The reusable lesson is that the *interest* of the general theory lies precisely in the phenomena that this exercise rules out — that Noetherian and Artinian are independent (witnessed by $\mathbb{Z}$ and $\mathbb{Z}[\tfrac12]/\mathbb{Z}$), that finitely generated need not be Noetherian, that length can be infinite. None of these can happen over a field. When you study the general theory, anchor yourself by asking "what does this say over a field?" — usually it reduces to a dimension statement you already know, and the deviation from that statement is the new content the ring introduces.

**Dimension changing strictly across strict inclusions is what forces both chain conditions in finite dimension.** The engine of Step 1 is the elementary fact that $U \subsetneq W$ (subspaces) implies $\dim U < \dim W$ — a strict inclusion changes dimension by at least one. This bounds the length of *any* strict chain by $\dim V + 1$, giving Noetherian and Artinian simultaneously. The transferable principle: whenever submodules carry a $\mathbb{Z}$-valued invariant that strictly changes across strict inclusions and is bounded, both chain conditions follow automatically. For modules over a field that invariant is dimension; for finite-length modules over any ring it is length; this is exactly why finite length implies both chain conditions in general. Recognising a "strictly monotone bounded invariant" is a fast route to proving a chain condition.

**Infinite dimension kills *both* chain conditions, by symmetric ascending and descending constructions — do not forget the descending one.** The subtlety students miss is that infinite dimension fails Artinian as well as Noetherian, and the descending chain $\langle v_n, v_{n+1}, \dots\rangle$ (pare down from the tail) is the witness, dual to the ascending $\langle v_1, \dots, v_n\rangle$ (build up from the front). The general diagnostic for "neither chain condition" is an infinite linearly independent (or, over a ring, suitably independent) family supporting both directions of strict chain. This symmetric pair is why an infinite-dimensional space is the cleanest example of a module that is *neither* Noetherian nor Artinian, and contrasting it with the one-sided failures ($\mathbb{Z}$ fails only Artinian, $\mathbb{Z}[\tfrac12]/\mathbb{Z}$ fails only Noetherian) sharpens the understanding that the two conditions are logically independent.

---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
  - "Def - Sum of Subspaces"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V_1, \dots, V_m$ be subspaces of a vector space $V$. Show that the sum $V_1 + \dots + V_m$ is itself a subspace of $V$, and that it is the **smallest** subspace of $V$ containing all of $V_1, \dots, V_m$.

In other words: $V_1 + \dots + V_m$ is a subspace, it contains each $V_k$, and any subspace of $V$ containing each $V_k$ must contain $V_1 + \dots + V_m$.

(LADR Result 1.40.)

**Recall:**

A [[Def - Subspace|subspace]] of $V$ is a non-empty subset $U \subseteq V$ closed under addition and scalar multiplication, equivalently a subset satisfying:

![[Def - Subspace#The Definition]]

The [[Def - Sum of Subspaces|sum of subspaces]] $V_1, \dots, V_m$ is

$$V_1 + \dots + V_m = \{v_1 + \dots + v_m : v_k \in V_k\}.$$

A subspace $W \subseteq V$ is "smaller" than another subspace $W'$ if $W \subseteq W'$. So "smallest subspace with property $P$" means the unique subspace with property $P$ that is contained in every other subspace with property $P$.

---

# Convergent Strategy

**Problem class:** This is a **characterization-by-universal-property** problem of the form: "show this object $X$ has property $P$ and is universal among objects with that property". The pattern is standard throughout algebra. For sums-of-subspaces, the property is "subspace containing each $V_k$". For spans-of-vectors (and intersections, and quotients) the same kind of pattern recurs.

**Assumption pattern:** Each $V_k$ is a subspace, so contains $0$ and is closed under addition and scalar multiplication. We are not told anything else, so the proof must be entirely structural — manipulating the definitions of subspace and sum.

**Theorem routing:** The route is the [[Def - Subspace|subspace criterion]] for proving the sum is a subspace (verify the three closure conditions), and then a containment chain for proving the universal property. There are no nontrivial theorems invoked; the entire argument is a direct application of the definitions.

**Key decision point:** The non-obvious choice is how to formulate the proof of the universal property. One could try to invoke completeness of the subspace lattice, but the cleanest argument is concrete: take any subspace $W$ containing each $V_k$, take an arbitrary element of $V_1 + \dots + V_m$, and verify directly that it lies in $W$. The choice of "concrete inclusion argument over abstract lattice argument" is what makes the proof clean.

---

# Legal Operations Used

1. **Verify a subset is a subspace by checking the three subspace conditions.** From the topic page's legal operations, the standard subspace check: contains $0$, closed under addition, closed under scalar multiplication. Applied here to certify $V_1 + \dots + V_m$ is a subspace.

2. **Show one set is contained in another by element-chasing.** Take an arbitrary element of the left-hand set and show it lies in the right-hand set. Used here to show $V_k \subseteq V_1 + \dots + V_m$ for each $k$, and to show $V_1 + \dots + V_m \subseteq W$ for any $W$ containing the $V_k$.

3. **Exploit closure of a subspace under finite sums.** A subspace is closed under finite sums (iterated application of closure under addition). Used in the universal-property argument: if $W$ contains each $V_k$ and $v_k \in V_k \subseteq W$, then $v_1 + \dots + v_m \in W$.

---

# Hints

> [!note]- Hint 1
> Break the problem into two parts: (a) prove that $V_1 + \dots + V_m$ is a subspace using the subspace criterion; (b) prove the universal property by an inclusion argument.

> [!note]- Hint 2
> For part (a), verify the three conditions one at a time. The zero vector is in the sum because each $V_k$ contains $0$ and $0 + \dots + 0 = 0$. For closure under addition, take two elements and add them coordinatewise. For closure under scalar multiplication, take an element and scale it.

> [!note]- Hint 3
> For containment of $V_k$ in the sum: write $v_k = 0 + \dots + 0 + v_k + 0 + \dots + 0$ with $v_k$ in slot $k$.

> [!note]- Hint 4
> For the universal property, take any subspace $W \supseteq V_1 \cup \dots \cup V_m$ and any element $v = v_1 + \dots + v_m$ of the sum. Each $v_k \in V_k \subseteq W$, so by closure of $W$ under addition, $v_1 + \dots + v_m \in W$.

---

# Solution

The proof breaks into three steps. Step 1 verifies that $V_1 + \dots + V_m$ is itself a subspace using the three subspace conditions. Step 2 shows each $V_k$ is contained in the sum, by exhibiting elements of $V_k$ as trivial sums. Step 3 shows the universal property: every subspace containing all the $V_k$ contains the sum, by closure under addition. The proof uses only the definitions, not any prior theorem.

**Step 1: The sum $V_1 + \dots + V_m$ is a subspace of $V$.**

We verify the three subspace conditions: contains $0$, closed under addition, closed under scalar multiplication.

> [!note]- Derivation
> *Contains $0$.* Each $V_k$ is a subspace, so $0 \in V_k$. Then $0 = 0 + 0 + \dots + 0$ (with each summand zero, one per $V_k$) lies in $V_1 + \dots + V_m$.
>
> *Closed under addition.* Let $v, v' \in V_1 + \dots + V_m$, so $v = v_1 + \dots + v_m$ with each $v_k \in V_k$, and $v' = v_1' + \dots + v_m'$ with each $v_k' \in V_k$. Then
> $$v + v' = (v_1 + v_1') + (v_2 + v_2') + \dots + (v_m + v_m'),$$
> where the rearrangement uses commutativity and associativity of vector addition. Each $v_k + v_k' \in V_k$ by closure of $V_k$ under addition, so $v + v' \in V_1 + \dots + V_m$.
>
> *Closed under scalar multiplication.* Let $\lambda \in \mathbb{F}$ and $v = v_1 + \dots + v_m \in V_1 + \dots + V_m$. Then
> $$\lambda v = \lambda (v_1 + \dots + v_m) = \lambda v_1 + \lambda v_2 + \dots + \lambda v_m$$
> by repeated application of axiom 7 (distributivity over vector addition). Each $\lambda v_k \in V_k$ by closure under scalar multiplication, so $\lambda v \in V_1 + \dots + V_m$.

**Step 2: Each $V_k$ is contained in $V_1 + \dots + V_m$.**

Every element of $V_k$ is realized as a sum with all-but-one summand zero.

> [!note]- Derivation
> Let $v_k \in V_k$. We need to exhibit $v_k$ as a sum $u_1 + \dots + u_m$ with $u_j \in V_j$ for each $j$. Take $u_k = v_k$ and $u_j = 0$ for $j \neq k$. Each $V_j$ contains $0$ (subspace condition), so $u_j \in V_j$ for every $j$. The sum is $u_1 + \dots + u_m = 0 + \dots + 0 + v_k + 0 + \dots + 0 = v_k$. Hence $v_k \in V_1 + \dots + V_m$.

**Step 3: Every subspace $W \subseteq V$ containing all $V_k$ contains $V_1 + \dots + V_m$.**

A subspace is closed under finite sums, so containment of the pieces forces containment of all their finite sums.

> [!note]- Derivation
> Let $W$ be a subspace of $V$ with $V_k \subseteq W$ for every $k$. Let $v = v_1 + \dots + v_m \in V_1 + \dots + V_m$, with each $v_k \in V_k$. Since $V_k \subseteq W$, each $v_k \in W$. By repeated application of closure of $W$ under addition (a subspace is closed under finite sums), $v_1 + \dots + v_m \in W$. Hence $v \in W$, and so $V_1 + \dots + V_m \subseteq W$.

> [!note]- Complete formal solution
> **Claim.** $V_1 + \dots + V_m$ is a subspace of $V$ and is the smallest subspace of $V$ containing $V_1, \dots, V_m$.
>
> *Step 1 — Subspace.* We verify the three conditions of the subspace criterion.
> - *Zero:* Each $V_k$ contains $0$, so $0 + 0 + \dots + 0 = 0$ is a valid expression of $0$ as an element of the sum.
> - *Addition:* For $v = v_1 + \dots + v_m$ and $v' = v_1' + \dots + v_m'$ with $v_k, v_k' \in V_k$, the sum $v + v' = (v_1 + v_1') + \dots + (v_m + v_m')$ lies in $V_1 + \dots + V_m$, since $V_k$ is closed under addition.
> - *Scalar multiplication:* For $\lambda \in \mathbb{F}$ and $v$ as above, $\lambda v = \lambda v_1 + \dots + \lambda v_m$ by distributivity, and $\lambda v_k \in V_k$ by closure of $V_k$ under scalar multiplication.
>
> *Step 2 — Containment.* For each $k$ and each $v_k \in V_k$, write $v_k = 0 + \dots + 0 + v_k + 0 + \dots + 0$ with $v_k$ in slot $k$ and $0$ elsewhere (each $0 \in V_j$ since $V_j$ is a subspace). This exhibits $v_k$ as an element of $V_1 + \dots + V_m$, so $V_k \subseteq V_1 + \dots + V_m$.
>
> *Step 3 — Universal property.* Let $W$ be any subspace of $V$ with $V_k \subseteq W$ for all $k$. For $v = v_1 + \dots + v_m \in V_1 + \dots + V_m$, each $v_k \in V_k \subseteq W$, so by closure of $W$ under finite sums (iterating closure under addition), $v_1 + \dots + v_m \in W$. Hence $V_1 + \dots + V_m \subseteq W$.
>
> Together: $V_1 + \dots + V_m$ is a subspace containing each $V_k$, and is contained in every such subspace, so it is the smallest. $\blacksquare$

---

# Key Takeaways

**The sum is the lattice-theoretic join of subspaces.** The result says, in lattice language, that the sum $V_1 + \dots + V_m$ is the join $V_1 \vee \dots \vee V_m$ in the lattice of subspaces of $V$ — the smallest subspace containing each piece. This puts sums of subspaces into the same conceptual frame as joins in any lattice (the union of subsets, the join of partitions, the supremum of real numbers): a universal upper bound. Recognizing the pattern lets you transfer intuition: in any lattice, when you want "the smallest thing above this collection", you reach for a join, and the universal property is "contained in every upper bound". The same proof template — verify the candidate has property $P$, verify it is contained in every $X$ with property $P$ — works whenever you have a join to characterize.

**Sums replace unions in the subspace lattice.** The naive analogue of "smallest subspace containing the $V_k$" would be the union, $V_1 \cup \dots \cup V_m$. The union is the smallest *set* containing them, but it is rarely a subspace — see [[Def - Sum of Subspaces]] and the standard example of the union of two coordinate axes in $\mathbb{R}^2$ failing closure under addition. The sum is what *repairs* the union by adding all finite sums of pieces. The slogan "union is to sets as sum is to subspaces" is the transferable takeaway, and it generalizes: in [[Def - Module|module theory]] one sums submodules, in [[Def - Group|group theory]] (for abelian groups) one sums subgroups, in topology one takes the topology generated by a union of sub-bases. Whenever a substructure needs to be "joined" while preserving its closure, the join is built by including all the algebraic combinations of pieces.

**Universal-property proofs split into "exhibit" and "absorb".** The pattern this proof follows is general for universal-property characterizations: (1) exhibit a candidate, and (2) show every other candidate absorbs it. Step 2 (subspace) shows that the candidate has the desired feature; step 3 (universal) shows any other object with the feature is at least as large. The same two-part structure works for spans (smallest subspace containing a set), intersections (largest subspace contained in a set), kernels (universal in the "vanishes on these elements" sense), and quotients. Recognizing the template lets you generate a proof of *any* universal-property statement by populating the two steps. The skill is in noticing that you are facing a universal-property problem in the first place — a signal is the appearance of words like "smallest", "largest", "free", or "universal" in the problem.

**The closure under finite sums of a subspace is what makes Step 3 work.** A subspace is closed under addition (axiomatically) but in fact closed under *finite* sums by iteration — at each addition step, the running sum remains in the subspace. This iterated closure is the engine of the universal-property argument: a subspace $W$ containing the pieces $V_k$ contains every $v_k \in V_k$, hence (by iterated closure) contains every finite sum of such, hence contains the sum subspace. The same iteration appears throughout linear algebra: "closure under finite linear combinations" is the operative form of the subspace condition, and is the form invoked when proving spans are subspaces or that linear maps are determined by their action on bases.

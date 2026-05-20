---
type: exercise
subject: topology
difficulty: "⭐"
prereqs:
  - "Def - Separation Axioms"
  - "Def - Subspace Topology"
tags: [analysis, topology, separation-axioms]
---

# Problem Statement

Let $X$ be a Hausdorff topological space and $A \subseteq X$ a subset, equipped with the subspace topology. Show that $A$ is Hausdorff.

**Recall:**

![[Def - Separation Axioms#The Definition]]

The [[Def - Subspace Topology|subspace topology]] on $A \subseteq X$ has as its open sets all sets of the form $A \cap U$ where $U$ is open in $X$. So an open set in $A$ is the restriction (intersection) of an open set in $X$.

A space $X$ is **Hausdorff** ($T_2$) if for any two distinct points $p \neq q$ in $X$ there exist disjoint open sets $U \ni p$, $V \ni q$.

---

# Convergent Strategy

**Problem class.** A *hereditary property* check: Hausdorff passes from $X$ to any subspace. Routine application of definitions.

**Assumption pattern.** $X$ Hausdorff is given. $A \subseteq X$ is arbitrary. Distinct points $p \neq q$ in $A$ are also distinct points in $X$.

**Theorem routing.** Use the Hausdorff condition in $X$ to obtain disjoint opens $U, V$ in $X$ separating $p, q$. Restrict to $A$ by intersection: $U' = U \cap A$, $V' = V \cap A$. These are open in $A$ (by definition of subspace topology), contain $p$ and $q$ respectively, and are disjoint (their intersection $U \cap V \cap A \subseteq U \cap V = \emptyset$).

**Key decision point.** None — this is the routine warm-up exercise for the separation hierarchy, and the same "intersect-with-$A$" recipe shows that $T_0, T_1, T_2, T_3$ all pass to subspaces (whereas $T_4$, normality, does *not*).

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **Restrict an ambient open set to a subspace.** The basic move for transferring properties from a space to a subspace is to intersect ambient open sets with the subspace.

2. **Preserve disjointness under intersection.** If $U \cap V = \emptyset$ in $X$, then certainly $(U \cap A) \cap (V \cap A) = \emptyset$ — disjointness only gets stronger under restriction.

---

# Hints

> [!note]- Hint 1
> Take any two distinct points $p, q \in A$. Since $p, q \in X$ and $p \neq q$, use Hausdorff in $X$ to get disjoint opens $U, V$ in $X$.

> [!note]- Hint 2
> The intersections $U \cap A$ and $V \cap A$ are open in $A$ by definition of the subspace topology. They contain $p$ and $q$ respectively (since $p \in U \cap A$ and $q \in V \cap A$). And they are disjoint since $U \cap V = \emptyset$.

---

# Solution

This is the prototype proof that separation properties transfer to subspaces via intersection.

**Step 1: Apply Hausdorff in $X$.**

Let $p, q \in A$ with $p \neq q$. Since $A \subseteq X$, both points are in $X$. By the Hausdorff condition in $X$, there exist disjoint open sets $U, V \subseteq X$ with $p \in U$ and $q \in V$.

> [!note]- Derivation
> $p \neq q$ in $A$ implies $p \neq q$ in $X$ (since both are elements of $X$). $X$ is Hausdorff, so by definition there exist open $U, V \subseteq X$ with $p \in U$, $q \in V$, $U \cap V = \emptyset$.

**Step 2: Restrict to $A$.**

Define $U' = U \cap A$ and $V' = V \cap A$. By the definition of the subspace topology on $A$, $U'$ and $V'$ are open in $A$. We have $p \in U'$ (since $p \in U$ and $p \in A$) and $q \in V'$ (similarly). Their intersection $U' \cap V' = U \cap V \cap A \subseteq U \cap V = \emptyset$, hence is empty.

> [!note]- Derivation
> The [[Def - Subspace Topology|subspace topology]] on $A$ is defined so that open subsets of $A$ are exactly the intersections $A \cap W$ for $W$ open in $X$. So $U' = A \cap U$ and $V' = A \cap V$ are both open in $A$.
>
> $p \in U'$: $p \in A$ (given) and $p \in U$ (from Step 1), so $p \in A \cap U = U'$. Similarly $q \in V'$.
>
> $U' \cap V' = (A \cap U) \cap (A \cap V) = A \cap (U \cap V) = A \cap \emptyset = \emptyset$.
>
> So $U', V'$ are disjoint open neighbourhoods of $p, q$ in $A$, showing that $A$ is Hausdorff.

> [!note]- Complete formal solution
> Let $X$ be Hausdorff and $A \subseteq X$. For $p \neq q$ in $A$, Hausdorff in $X$ gives disjoint opens $U \ni p$ and $V \ni q$ in $X$. Define $U' = U \cap A$, $V' = V \cap A$. By the [[Def - Subspace Topology|subspace topology]] definition, $U', V'$ are open in $A$. They contain $p, q$ respectively, and $U' \cap V' = U \cap V \cap A = \emptyset$. Hence $A$ is Hausdorff. $\blacksquare$

---

# Key Takeaways

**The "intersect with the subspace" recipe transfers $T_0, T_1, T_2, T_3$ but *not* $T_4$ to subspaces.** The pattern: take separating ambient opens, intersect with the subspace, the result remains open in the subspace and disjoint. This works as long as the separating condition is *pointwise* or *point-and-closed-set*: $T_0, T_1$ (point vs. point), $T_2$ (point vs. point), $T_3$ (point vs. closed set — and closed sets in a subspace are restrictions of closed sets in $X$, intersected with the subspace, so the recipe still works). $T_4$ (normal — two closed sets) fails because a closed set in a subspace may not extend to a closed set in $X$ that maintains the disjointness pattern, and the classical counterexample is the Tychonoff plank, where a normal $X$ has a non-normal subspace.

**Hausdorff is one of a small family of "monotone" properties: hereditary downward (subspaces), preserved by products, preserved by inverse images of continuous maps.** Recognizing which axiom in the separation hierarchy is monotone in which direction is one of the most important book-keeping disciplines in topology. Hausdorff is hereditary (this exercise), $T_1$ is hereditary, regularity is hereditary, normality is *not* hereditary. Hausdorff is preserved by arbitrary products (an arbitrary product of Hausdorff spaces is Hausdorff), as is regularity, but not normality. A continuous map's image being Hausdorff does *not* imply the source is Hausdorff (consider any space mapping to a one-point space, which is trivially Hausdorff). Knowing these direction-by-direction inheritance facts converts most separation questions into immediate look-up.

**Subspace topology is exactly the topology that makes "Hausdorff in $X$ $\Rightarrow$ Hausdorff in $A$" true with the cleanest proof — and this is structural: the subspace topology is the initial topology of the inclusion $A \hookrightarrow X$.** This means every continuous map $f : Y \to X$ that factors through $A$ is automatically continuous as a map $Y \to A$. The hereditary nature of separation axioms reflects this universal property: the inclusion preserves the topology in the strongest possible sense, so it preserves any property that is defined in terms of the open sets locally near each point. Hausdorff, $T_1$, and regularity are all such "local" properties. Normality, defined globally on disjoint closed sets, is not.

**The simplicity of this proof is a feature: every theorem about topological spaces should have a "subspace" version, and they usually do, with the same proof.** When studying a new topological property $P$, the first question is always "is $P$ hereditary?" — and the answer almost always follows from the same intersect-with-$A$ recipe. This is the *first move* in topology, and the discipline of asking it is what reveals which properties are local-ish ($T_2$, $T_3$, connectedness in a sense — though connectedness is *not* hereditary, see $\mathbb{Q} \subseteq \mathbb{R}$) versus which are genuinely global ($T_4$, compactness when target-side, completeness).

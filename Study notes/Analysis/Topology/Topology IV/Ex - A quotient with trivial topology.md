---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Quotient Topology and Identification Map"
  - "Def - Topological Space"
tags: [analysis, topology, quotient, pathological]
---

# Problem Statement

Consider $\mathbb{R}$ with the standard topology, and the equivalence relation $x \sim y \iff x - y \in \mathbb{Q}$. Let $X = \mathbb{R}/\mathbb{Q}$ be the quotient (the set of $\mathbb{Q}$-cosets in $\mathbb{R}$).

Show:

1. $X$ has uncountably many points.
2. The quotient topology on $X$ is the **trivial (indiscrete) topology**: the only open sets are $\emptyset$ and $X$.

**Recall:**

The [[Def - Quotient Topology and Identification Map|quotient topology]] declares $V \subseteq X$ open iff $\pi^{-1}(V) \subseteq \mathbb{R}$ is open, where $\pi : \mathbb{R} \to X$ is the canonical projection.

A subset $A \subseteq \mathbb{R}$ is **$\mathbb{Q}$-saturated** if $a \in A$ and $a' \sim a$ together imply $a' \in A$ — i.e., $A$ is a union of $\mathbb{Q}$-cosets.

---

# Convergent Strategy

**Problem class:** Verify a quotient has trivial topology by analyzing the structure of $\mathbb{Q}$-saturated open sets.

**Assumption pattern:** $\mathbb{R}$ is a topological space; $\sim$ is a translation-by-rationals equivalence; the cosets are dense in $\mathbb{R}$ (each coset is a translate of $\mathbb{Q}$).

**Theorem routing:** Direct computation. Show $V \subseteq X$ open $\Leftrightarrow$ $\pi^{-1}(V) \subseteq \mathbb{R}$ open and $\mathbb{Q}$-saturated. Then show every $\mathbb{Q}$-saturated open in $\mathbb{R}$ is either $\emptyset$ or $\mathbb{R}$.

**Key decision point:** Recognizing that a $\mathbb{Q}$-saturated open set in $\mathbb{R}$ is either empty or all of $\mathbb{R}$. This is because $\mathbb{Q}$ is dense: a $\mathbb{Q}$-saturated set contains $a + \mathbb{Q}$ for any $a$ in it, and $a + \mathbb{Q}$ is dense in $\mathbb{R}$.

---

# Legal Operations Used

1. **Translate the quotient topology to saturated opens.** The opens in $X$ correspond exactly to the $\mathbb{Q}$-saturated opens in $\mathbb{R}$.

2. **Use density of $\mathbb{Q}$.** Any $\mathbb{Q}$-saturated subset of $\mathbb{R}$ contains a translate of $\mathbb{Q}$, which is dense in $\mathbb{R}$.

3. **Cardinality argument.** The number of cosets equals $\mathbb{R}/\mathbb{Q}$, which has the cardinality of $\mathbb{R}$ (in fact, exactly the same, since $\mathbb{Q}$ is countable).

---

# Hints

> [!note]- Hint 1
> A set $V \subseteq X$ is open iff $\pi^{-1}(V) \subseteq \mathbb{R}$ is open. $\pi^{-1}(V)$ is always a union of $\mathbb{Q}$-cosets. So $V$ open in $X$ iff $\pi^{-1}(V)$ is open in $\mathbb{R}$ *and* is a union of $\mathbb{Q}$-cosets.

> [!note]- Hint 2
> A $\mathbb{Q}$-coset $a + \mathbb{Q}$ is dense in $\mathbb{R}$: for any $r \in \mathbb{R}$ and any $\epsilon > 0$, choose a rational $q$ within $\epsilon$ of $r - a$; then $a + q$ is within $\epsilon$ of $r$ and is in the coset.

> [!note]- Hint 3
> If $U \subseteq \mathbb{R}$ is open and contains a single $\mathbb{Q}$-coset $a + \mathbb{Q}$, then $U$ contains a dense subset, so $U$ is dense. But a dense open set isn't necessarily all of $\mathbb{R}$ — extra work needed. Combine with: $U$ saturated means $U = a + \mathbb{Q} \cup b + \mathbb{Q} \cup \dots$ — but each coset is dense, so $U$ contains many translates.

> [!note]- Hint 4
> Crucial step: a nonempty $\mathbb{Q}$-saturated open set in $\mathbb{R}$ has dense complement that is also $\mathbb{Q}$-saturated and open. Both can't be nonempty and disjoint: any nonempty open set in $\mathbb{R}$ intersects every dense set. So one of them must be empty.

---

# Solution

**Step 1: $X$ has uncountably many points.**

The cosets $a + \mathbb{Q}$ for $a \in \mathbb{R}$ partition $\mathbb{R}$. The number of cosets is $|\mathbb{R}|/|\mathbb{Q}| = |\mathbb{R}|/\aleph_0 = |\mathbb{R}|$ (since $\mathbb{R}$ has cardinality $2^{\aleph_0}$ and $\mathbb{Q}$ is countable, removing countably many points from $\mathbb{R}$ doesn't reduce its cardinality). So $|X| = |\mathbb{R}| = 2^{\aleph_0}$, uncountable.

**Step 2: Every $\mathbb{Q}$-coset is dense in $\mathbb{R}$.**

> [!note]- Derivation
> For $a \in \mathbb{R}$, the coset is $a + \mathbb{Q} = \{a + q : q \in \mathbb{Q}\}$. Given any $r \in \mathbb{R}$ and $\epsilon > 0$, by density of $\mathbb{Q}$ in $\mathbb{R}$, there exists $q \in \mathbb{Q}$ with $|q - (r - a)| < \epsilon$. Then $|(a + q) - r| < \epsilon$, so the coset intersects $(r - \epsilon, r + \epsilon)$. Hence the coset is dense.

**Step 3: Every nonempty $\mathbb{Q}$-saturated open set in $\mathbb{R}$ is all of $\mathbb{R}$.**

> [!note]- Derivation
> Let $U \subseteq \mathbb{R}$ be nonempty, open, and $\mathbb{Q}$-saturated. Pick any $a \in U$. By saturation, $U$ contains the entire coset $a + \mathbb{Q}$. By Step 2, $a + \mathbb{Q}$ is dense in $\mathbb{R}$.
>
> Now consider the complement $V := \mathbb{R} \setminus U$. $V$ is closed. Is $V$ saturated? Yes: if $b \in V$ and $b' \sim b$ (so $b' - b \in \mathbb{Q}$), then $b' \notin U$ (else by saturation $b \in U$). So $V$ is saturated, hence a union of cosets.
>
> Suppose $V \neq \emptyset$. Pick $b \in V$. Then $V$ contains the coset $b + \mathbb{Q}$, which is dense in $\mathbb{R}$. So $V$ is dense in $\mathbb{R}$. But $V = \mathbb{R} \setminus U$ where $U$ is open and nonempty. A dense set and a nonempty open set must intersect — every nonempty open set in $\mathbb{R}$ meets every dense set, by definition of density. So $V \cap U \neq \emptyset$ — contradiction.
>
> Hence $V = \emptyset$, i.e., $U = \mathbb{R}$.

**Step 4: The quotient topology on $X$ is the trivial topology.**

> [!note]- Derivation
> By the quotient topology definition, $W \subseteq X$ is open iff $\pi^{-1}(W) \subseteq \mathbb{R}$ is open. $\pi^{-1}(W)$ is always $\mathbb{Q}$-saturated (preimages of sets under a quotient map are saturated). So $W$ open in $X$ iff $\pi^{-1}(W)$ is open and saturated.
>
> By Step 3, $\pi^{-1}(W)$ is either $\emptyset$ or $\mathbb{R}$. So $W = \pi(\pi^{-1}(W))$ is either $\emptyset$ or $X$.
>
> Hence the only open sets in $X$ are $\emptyset$ and $X$ — the trivial topology.

> [!note]- Complete formal solution
> *Cardinality:* Each $\mathbb{Q}$-coset is countable (translate of countable $\mathbb{Q}$), so the partition of $\mathbb{R}$ into cosets has $|\mathbb{R}|/\aleph_0 = |\mathbb{R}|$ classes.
>
> *Trivial topology:* Let $W \subseteq X$ be open. Then $\pi^{-1}(W) \subseteq \mathbb{R}$ is open (quotient topology) and $\mathbb{Q}$-saturated (preimage under projection). If $\pi^{-1}(W) \neq \emptyset$, pick $a \in \pi^{-1}(W)$. By saturation, $a + \mathbb{Q} \subseteq \pi^{-1}(W)$. By density of $a + \mathbb{Q}$, $\pi^{-1}(W)$ is dense. Its complement $\mathbb{R} \setminus \pi^{-1}(W)$ is also $\mathbb{Q}$-saturated (closed under same argument) and closed, hence either empty or dense. If nonempty, both $\pi^{-1}(W)$ and its complement would be dense and disjoint, contradicting nonempty intersection of dense sets with open sets. So the complement is empty, meaning $\pi^{-1}(W) = \mathbb{R}$, so $W = X$. Hence the only opens are $\emptyset$ and $X$. $\blacksquare$

---

# Key Takeaways

**Quotients can destroy Hausdorffness wildly.** $\mathbb{R}$ is the prototype Hausdorff space (metrizable, second-countable, locally compact, etc.). Yet the quotient $\mathbb{R}/\mathbb{Q}$ has the *trivial* topology — no separation whatsoever. The lesson: quotients are gentle on the side of openness (every open in the quotient comes from an open in the source) but brutal on the side of separation. A dense equivalence relation can collapse a Hausdorff space to indiscrete.

**Saturated opens are the natural objects.** The quotient topology lives "downstairs" but is most cleanly described by its preimages "upstairs". A set in the quotient is open iff its preimage is a $\mathbb{Q}$-saturated open set in $\mathbb{R}$. So understanding the quotient topology amounts to understanding the saturated-open lattice of $\mathbb{R}$ (under $\mathbb{Q}$-translation).

**Density of the equivalence classes is what kills the topology.** The argument hinges on each $\mathbb{Q}$-coset being dense in $\mathbb{R}$. If we replaced $\mathbb{Q}$ by $\mathbb{Z}$ (whose cosets are $\mathbb{Z}$-translates, *not* dense), the quotient $\mathbb{R}/\mathbb{Z} \cong S^1$ would be a perfectly nice Hausdorff space. The difference: $\mathbb{Z}$ is discrete, so a saturated open can have small support; $\mathbb{Q}$ is dense, so saturation forces the support to be everywhere.

**Trigger-reaction pattern.** When checking a quotient space for separation, ask: "are the equivalence classes closed? are they discrete? are they bounded?" Dense, non-closed equivalence classes are the warning sign for pathology. Closed equivalence classes (especially finite or discrete ones) give Hausdorff quotients. This is the dichotomy that distinguishes good quotients (like $\mathbb{R}/\mathbb{Z}$) from bad ones (like $\mathbb{R}/\mathbb{Q}$).

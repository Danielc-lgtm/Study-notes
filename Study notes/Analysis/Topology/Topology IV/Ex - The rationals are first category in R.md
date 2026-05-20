---
type: exercise
subject: topology
difficulty: "⭐"
prereqs:
  - "Def - Nowhere Dense and Meager"
  - "Thm - Baire Category Theorem"
  - "Def - Cauchy Sequence and Complete Metric Space"
tags: [analysis, topology, baire, meager]
---

# Problem Statement

Show that $\mathbb{Q} \subseteq \mathbb{R}$ is **first category** (meager): it is a countable union of nowhere dense sets.

Conclude (using the Baire category theorem) that $\mathbb{R} \setminus \mathbb{Q}$ — the irrationals — is **non-meager** in $\mathbb{R}$, and in particular nonempty.

**Recall:**

A subset $A \subseteq X$ is [[Def - Nowhere Dense and Meager|nowhere dense]] if $\overline{A}$ has empty interior. It is **meager** (first category) if it is a countable union of nowhere dense sets. **Second category** = not meager.

The [[Thm - Baire Category Theorem|Baire category theorem]] says: a complete metric space (or LCH space) is not meager in itself.

---

# Convergent Strategy

**Problem class:** Verify a specific set is meager and apply Baire to conclude the complement is non-meager.

**Assumption pattern:** $\mathbb{Q}$ is countable. Each singleton $\{q\}$ for $q \in \mathbb{Q}$ is a closed set with empty interior in $\mathbb{R}$. The union of countably many such singletons is $\mathbb{Q}$ itself.

**Theorem routing:** $\mathbb{Q} = \bigcup_{q \in \mathbb{Q}} \{q\}$, a countable union of nowhere dense singletons. So $\mathbb{Q}$ is meager. By Baire, $\mathbb{R}$ is non-meager, so the complement $\mathbb{R} \setminus \mathbb{Q}$ is non-meager.

**Key decision point:** Recognize that singletons in $\mathbb{R}$ are nowhere dense (since $\mathbb{R}$ has no isolated points, every singleton's closure is itself, with empty interior).

---

# Legal Operations Used

1. **Singletons are nowhere dense in $\mathbb{R}$.** A singleton's closure is the singleton itself (closed); its interior is empty (no interior point in $\mathbb{R}$ has a neighborhood within a singleton).

2. **Countable union of nowhere dense sets is meager.** Definition.

3. **Apply Baire.** $\mathbb{R}$ is a complete metric space, so it is not meager in itself.

---

# Hints

> [!note]- Hint 1
> $\mathbb{Q}$ is countable, so write $\mathbb{Q} = \{q_1, q_2, q_3, \dots\}$. Then $\mathbb{Q} = \bigcup_n \{q_n\}$ — a countable union.

> [!note]- Hint 2
> Each singleton $\{q\} \subseteq \mathbb{R}$ is closed (since $\mathbb{R}$ is Hausdorff) with empty interior (every open subset of $\mathbb{R}$ has uncountably many points). So $\{q\}$ is nowhere dense.

> [!note]- Hint 3
> $\mathbb{Q}$ is a countable union of nowhere dense sets, hence meager.

> [!note]- Hint 4
> Apply Baire to $\mathbb{R}$ (complete metric): $\mathbb{R}$ is not meager. If $\mathbb{R} \setminus \mathbb{Q}$ were meager, then $\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q})$ would be a union of two meager sets, hence meager. Contradiction. So $\mathbb{R} \setminus \mathbb{Q}$ is non-meager.

---

# Solution

The proof breaks into four short steps. Step 1 observes each singleton $\{q\} \subseteq \mathbb{R}$ is nowhere dense (closed with empty interior, since open subsets of $\mathbb{R}$ are uncountable); Step 2 writes $\mathbb{Q} = \bigcup_n \{q_n\}$ as a countable union of nowhere dense singletons, concluding $\mathbb{Q}$ is meager; Step 3 applies Baire to the complete metric space $\mathbb{R}$ to conclude $\mathbb{R}$ is not meager in itself; Step 4 deduces that $\mathbb{R} \setminus \mathbb{Q}$ is non-meager by complementation. The non-obvious move is in Step 4 — the irrationals' non-emptiness comes from Baire, not from a cardinality count, giving a *structural* reason that generalises to Banach spaces.

**Step 1: Each singleton $\{q\}$ is nowhere dense in $\mathbb{R}$.**

> [!note]- Derivation
> $\overline{\{q\}} = \{q\}$ (the singleton is closed in $\mathbb{R}$, since $\mathbb{R}$ is Hausdorff $T_1$). $\operatorname{int}(\{q\}) = \emptyset$ (any nonempty open in $\mathbb{R}$ is an interval, containing uncountably many points, not equal to a single point). So $\operatorname{int}(\overline{\{q\}}) = \emptyset$: $\{q\}$ is nowhere dense.

**Step 2: $\mathbb{Q}$ is meager.**

> [!note]- Derivation
> $\mathbb{Q}$ is countable, say $\mathbb{Q} = \{q_1, q_2, q_3, \dots\}$. Then
> $$\mathbb{Q} = \bigcup_{n=1}^{\infty} \{q_n\}.$$
> Each $\{q_n\}$ is nowhere dense (Step 1). The union is countable. So $\mathbb{Q}$ is a countable union of nowhere dense sets, hence meager (first category) in $\mathbb{R}$.

**Step 3: $\mathbb{R}$ is not meager in itself.**

> [!note]- Derivation
> $\mathbb{R}$ is a complete metric space (Cauchy sequences converge, by the standard construction of $\mathbb{R}$). By [[Thm - Baire Category Theorem]], $\mathbb{R}$ is not meager in itself.

**Step 4: $\mathbb{R} \setminus \mathbb{Q}$ is non-meager.**

> [!note]- Derivation
> Suppose, for contradiction, that $\mathbb{R} \setminus \mathbb{Q}$ is meager. Then $\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q})$ is a union of two meager sets. The union of finitely (or countably) many meager sets is meager (a countable union of countable unions of nowhere dense sets is itself a countable union of nowhere dense sets). So $\mathbb{R}$ would be meager. Contradiction with Step 3.
>
> Hence $\mathbb{R} \setminus \mathbb{Q}$ is non-meager.

> [!note]- Complete formal solution
> *Meagerness of $\mathbb{Q}$:* $\mathbb{Q} = \bigcup_{q \in \mathbb{Q}} \{q\}$ is a countable union of singletons. Each singleton $\{q\} \subseteq \mathbb{R}$ is closed (Hausdorff) with empty interior (every nonempty open in $\mathbb{R}$ is uncountable). So $\{q\}$ is nowhere dense, and the union is meager.
>
> *Non-meagerness of irrationals:* By [[Thm - Baire Category Theorem]], $\mathbb{R}$ (complete metric) is not meager in itself. If $\mathbb{R} \setminus \mathbb{Q}$ were meager, $\mathbb{R}$ would be a union of two meager sets, hence meager. So $\mathbb{R} \setminus \mathbb{Q}$ is non-meager; in particular nonempty. $\blacksquare$

---

# Key Takeaways

**Meager and dense are *not* opposite.** $\mathbb{Q}$ is meager (small in the Baire sense) but *dense* in $\mathbb{R}$ (every open contains a rational). The two notions — "small" by meagerness and "dense" by closure — measure different things. A set can be dense and meager (rationals); dense and non-meager (irrationals are *both* dense and non-meager); meager and not dense (a finite set); or non-meager and not dense (an open ball misses dense complement, but is itself non-meager).

**Countable subsets of $\mathbb{R}$ are always meager.** The argument generalizes: any countable subset $S = \{s_1, s_2, \dots\} \subseteq \mathbb{R}$ is meager, by writing it as a countable union of nowhere dense singletons. In particular: $\mathbb{Z}$ is meager, $\mathbb{Q}$ is meager, the algebraic numbers are meager (countable), the integers raised to rational powers are meager.

**Cardinality vs. meagerness.** $\mathbb{R} \setminus \mathbb{Q}$ has the cardinality of the continuum ($|\mathbb{R}| = 2^{\aleph_0}$); $\mathbb{Q}$ is countable. This is one way to see that the irrationals are "much more numerous" than the rationals. But Baire gives a *structural* reason for non-emptiness that doesn't reference cardinality: the irrationals are non-meager.

**The lesson generalizes to Banach spaces.** Replace $\mathbb{R}$ by a Banach space $V$ and $\mathbb{Q}$ by some "small" subset (e.g., a finite-dimensional subspace, or a countable subset). The same argument: the subset is meager, its complement is non-meager and dense. *Example:* in a Banach space, the union of all finite-dimensional subspaces is meager (each finite-dim subspace is closed with empty interior — the proof for $\mathbb{Q}$ in $\mathbb{R}$ generalizes). So most elements of an infinite-dimensional Banach space are "not in any finite-dimensional subspace" — a topological version of "infinite-dimensionality is dense".

**The shrinking-ball intuition.** Baire's proof technique — construct shrinking balls avoiding each $A_n$, take the limit — produces a specific witness. For the irrationals: choose a shrinking sequence of intervals avoiding $q_1, q_2, \dots$ successively. The limit is an irrational (by completeness of $\mathbb{R}$). This is the constructive content of Baire.

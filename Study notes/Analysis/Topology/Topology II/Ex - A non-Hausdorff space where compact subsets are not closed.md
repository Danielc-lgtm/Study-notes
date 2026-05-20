---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Compact Space"
  - "Def - Separation Axioms"
  - "Thm - Compact Subset of Hausdorff is Closed"
tags: [analysis, topology, compactness, counterexample]
---

# Problem Statement

In any Hausdorff space, compact subsets are closed (see [[Thm - Compact Subset of Hausdorff is Closed]]). The Hausdorff hypothesis cannot be dropped: in a non-Hausdorff space, there can be compact subsets that are not closed. Show this concretely.

Equip $\mathbb{R}$ with the **cofinite topology**: open sets are $\emptyset$ together with all subsets of $\mathbb{R}$ with finite complement.

**(a)** Show that *every* subset of $\mathbb{R}$ is compact in the cofinite topology.

**(b)** Determine all closed subsets of $\mathbb{R}$ in the cofinite topology. (Answer: $\mathbb{R}$ and all finite sets.)

**(c)** Conclude that there exist compact subsets of $\mathbb{R}$ that are not closed — for instance, the open interval $(0, 1)$ in the cofinite topology is compact (by (a)) but not closed (by (b)), since it is infinite but not all of $\mathbb{R}$.

**Recall:**

![[Def - Compact Space#The Definition]]

![[Def - Separation Axioms#The Definition]]

The **cofinite topology** on a set $X$ has as its open sets $\emptyset$ together with all subsets $U \subseteq X$ such that $X \setminus U$ is finite. The closed sets are $X$ itself and all finite subsets.

A subset $A \subseteq X$ is **compact** in $X$ if it is compact as a topological space in the subspace topology, equivalently, if every cover of $A$ by open sets of $X$ admits a finite subcover.

---

# Convergent Strategy

**Problem class.** Construct a *named counterexample* showing the necessity of Hausdorff in the "compact $\Rightarrow$ closed" theorem. The cofinite topology is the canonical such example because its compactness behaviour is degenerate (everything is compact) while its closed sets are highly restricted (only finite sets plus the whole space).

**Assumption pattern.** The cofinite topology has the property that every nonempty open set is cofinite, hence "very large", hence a *single* open set can cover almost everything.

**Theorem routing.** No prior theorems beyond the cofinite topology being not Hausdorff (proved in [[Ex - A T1 space that is not Hausdorff]]). Direct construction.

**Key decision point.** Part (a) — every subset is compact — has a clean counting argument: a single open set covers the subset modulo a finite set of exceptional points, which can be covered by finitely many opens individually.

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **A single cofinite open covers all but finitely many points.** This is the structural feature of cofinite topology: opens are very large, and a finite subcover is automatically available once we cover the finite exceptional set.

2. **Use the closedness criterion "finite or whole space" in the cofinite topology.** This makes the failure of "compact $\Rightarrow$ closed" immediate: any infinite proper subset is compact (by (a)) but not closed (by criterion).

3. **Test theorems by removing hypotheses.** To verify that a hypothesis is essential, exhibit an example where the conclusion fails when only the rest of the hypotheses hold. Here, (compact, but not Hausdorff) violates "compact $\Rightarrow$ closed".

---

# Hints

> [!note]- Hint 1
> For (a): let $A \subseteq \mathbb{R}$ be any subset. Take any open cover $\mathcal{U} = \{U_\alpha\}$ of $A$ by open sets of $\mathbb{R}$ (in the cofinite topology). Pick any nonempty $U_{\alpha_0} \in \mathcal{U}$. Then $\mathbb{R} \setminus U_{\alpha_0}$ is a finite set; call its elements $x_1, \ldots, x_n$. For each $x_i \in A \setminus U_{\alpha_0}$, pick $U_{\alpha_i} \ni x_i$. Then $A \subseteq U_{\alpha_0} \cup U_{\alpha_1} \cup \cdots \cup U_{\alpha_n}$.

> [!note]- Hint 2
> For (b): the closed sets are by definition the complements of open sets. Complements of cofinite sets are *finite*. Plus the complement of $\emptyset$ is $\mathbb{R}$. So the closed sets are: $\mathbb{R}$ and all finite subsets.

> [!note]- Hint 3
> For (c): $(0, 1)$ is an infinite proper subset of $\mathbb{R}$, hence not closed in the cofinite topology (by (b)). But it is compact (by (a)). So this is an example of compact but not closed.

---

# Solution

The cofinite topology is the canonical example showing that almost no separation conclusion holds without Hausdorff. Here we use it to break the "compact subsets are closed" theorem.

**Step 1: Part (a) — every subset is compact.**

Let $A \subseteq \mathbb{R}$ be any subset (the empty set is vacuously compact, so assume $A \neq \emptyset$). Let $\mathcal{U} = \{U_\alpha\}$ be a cover of $A$ by sets open in the cofinite topology on $\mathbb{R}$. We extract a finite subcover.

> [!note]- Derivation
> Pick any nonempty $U_{\alpha_0} \in \mathcal{U}$ (it exists since $\mathcal{U}$ covers nonempty $A$). By definition of the cofinite topology, $\mathbb{R} \setminus U_{\alpha_0}$ is a finite set; list its elements $x_1, \ldots, x_n$ (with $n \geq 0$; if $n = 0$, $U_{\alpha_0} = \mathbb{R}$).
>
> For each $i = 1, \ldots, n$: if $x_i \in A$, then $\mathcal{U}$ covers $A$, so some $U_{\alpha_i} \in \mathcal{U}$ contains $x_i$. If $x_i \notin A$, we don't need to cover it; skip.
>
> Now claim $A \subseteq U_{\alpha_0} \cup \bigcup_{x_i \in A} U_{\alpha_i}$. Indeed, for any $a \in A$:
> - If $a \in U_{\alpha_0}$, done.
> - If $a \notin U_{\alpha_0}$, then $a \in \mathbb{R} \setminus U_{\alpha_0} = \{x_1, \ldots, x_n\}$, so $a = x_i$ for some $i$. Since $a = x_i \in A$, we picked some $U_{\alpha_i} \ni x_i = a$. So $a \in U_{\alpha_i}$.
>
> Hence $\{U_{\alpha_0}, U_{\alpha_{i_1}}, \ldots, U_{\alpha_{i_k}}\}$ (where $i_1, \ldots, i_k$ are the indices with $x_i \in A$) is a finite subcover of $A$. So $A$ is compact.

**Step 2: Part (b) — closed sets are $\mathbb{R}$ and the finite subsets.**

A subset $F \subseteq \mathbb{R}$ is closed iff $\mathbb{R} \setminus F$ is open. In the cofinite topology, open means $\emptyset$ or cofinite. So $\mathbb{R} \setminus F$ is open iff $\mathbb{R} \setminus F = \emptyset$ (i.e., $F = \mathbb{R}$) or $\mathbb{R} \setminus F$ is cofinite (i.e., $F$ is finite).

> [!note]- Derivation
> By definition of the cofinite topology: $U \subseteq \mathbb{R}$ is open iff $U = \emptyset$ or $\mathbb{R} \setminus U$ is finite. So $F$ is closed (= $\mathbb{R} \setminus F$ open) iff $\mathbb{R} \setminus F = \emptyset$ or $\mathbb{R} \setminus (\mathbb{R} \setminus F) = F$ is finite. The first case is $F = \mathbb{R}$; the second case is $F$ finite. So the closed sets are exactly $\{F : F \text{ is finite}\} \cup \{\mathbb{R}\}$.

**Step 3: Part (c) — an explicit compact non-closed subset.**

Take $A = (0, 1) \subseteq \mathbb{R}$. By Part (a), $A$ is compact. By Part (b), $A$ is closed iff $A$ is finite or $A = \mathbb{R}$; but $A$ is infinite (uncountable, in fact) and $A \neq \mathbb{R}$. So $A$ is compact and not closed.

> [!note]- Derivation
> $(0, 1) \subseteq \mathbb{R}$ has uncountably many elements, so $(0, 1)$ is not finite. Also $(0, 1) \neq \mathbb{R}$ (for instance $2 \in \mathbb{R} \setminus (0, 1)$). By Part (b), $(0, 1)$ is not closed in the cofinite topology.
>
> By Part (a), $(0, 1)$ is compact.
>
> So $(0, 1)$ is a compact subset of $(\mathbb{R}, \text{cofinite})$ that is not closed. The Hausdorff hypothesis is essential for "compact $\Rightarrow$ closed" in [[Thm - Compact Subset of Hausdorff is Closed]].

> [!note]- Complete formal solution
> Equip $\mathbb{R}$ with the cofinite topology.
>
> **(a) Every subset is compact.** Let $A \subseteq \mathbb{R}$ and let $\{U_\alpha\}$ cover $A$. Pick any nonempty $U_{\alpha_0}$; its complement $\mathbb{R} \setminus U_{\alpha_0}$ is finite. For each of the finitely many points $x \in (A \setminus U_{\alpha_0})$, pick a $U_{\alpha_x} \ni x$. Then $\{U_{\alpha_0}\} \cup \{U_{\alpha_x}\}_x$ is a finite subcover of $A$.
>
> **(b) Closed sets are $\mathbb{R}$ and finite subsets.** By definition of the cofinite topology, $F$ closed iff $\mathbb{R} \setminus F$ open iff $\mathbb{R} \setminus F = \emptyset$ or $\mathbb{R} \setminus F$ cofinite, iff $F = \mathbb{R}$ or $F$ finite.
>
> **(c) Compact $\neq$ closed.** $(0, 1)$ is compact by (a) but is infinite and proper, hence not closed by (b). $\blacksquare$

---

# Key Takeaways

**The cofinite topology produces "too many" compacts and "too few" closed sets — the two coincide only for finite subsets, so the theorem "compact $\Rightarrow$ closed" trivially fails.** This is the structural diagnosis: compactness in the cofinite topology is degenerate (any subset works), and closedness is highly restricted (only finite sets). The intersection of these two classes — compact-and-closed = finite — is a tiny fragment of $\mathcal{P}(\mathbb{R})$. The general lesson: when Hausdorff fails, "compact" loses its bite and ceases to be a useful invariant for cataloguing subsets. Recognize the pattern: degenerate compactness is a feature of weak topologies on infinite sets.

**The "Hausdorff is essential" lesson generalizes: Hausdorff is needed for almost every interesting *uniqueness*-type theorem in topology.** Uniqueness of limits (failure: cofinite — see [[Ex - A T1 space that is not Hausdorff]]), uniqueness of compact-implying-closed (failure: this exercise), uniqueness in the closed-graph theorem, uniqueness in Stone-Weierstrass. The structural reason: Hausdorff forces the topology to "see" the difference between distinct points, which is what makes any property of an individual point well-defined and unambiguous. Without it, "the point in this neighbourhood" or "the limit of this net" is ambiguous, and the consequences of those ambiguities cascade through the rest of the theory.

**For verifying that a hypothesis is essential, the universal recipe is: identify a topological property of the same flavor as your hypothesis (here: $T_2$ vs. cofinite which is $T_1$ but not $T_2$), and exhibit a space where the property holds but the hypothesis fails.** Then test the conclusion. The cofinite topology is one of the best testing-grounds for this because it satisfies many natural axioms in a degenerate way: every set is compact, every set is connected (the only clopens are $\emptyset, \mathbb{R}$), every set is dense (every nonempty open contains all but finitely many points), but Hausdorff fails. So any theorem of the form "compact $\Rightarrow$ X" or "connected $\Rightarrow$ X" that requires Hausdorff can be tested by checking whether $X$ holds in the cofinite topology. If it doesn't, Hausdorff is essential.

**The trigger "compact subset" should immediately summon the question "ambient Hausdorff?" — and if not, the subset need not be closed.** This is the most common operational error in non-Hausdorff settings (Zariski topology, weak topologies, quotient spaces with non-Hausdorff quotients). The default intuition from metric spaces — "compact = closed and bounded" — is precisely the trigger that fails. Trigger-reaction pattern: see "compact" → check Hausdorff before concluding closed. In Zariski topology on $\mathbb{A}^1_k$, the whole space is compact (= the only open cover is the trivial one when the field is infinite), but most subsets are *not* closed.

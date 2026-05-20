---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Compact Space"
  - "Def - Separation Axioms"
  - "Thm - Closed Subset of Compact is Compact"
tags: [analysis, topology, compactness, separation-axioms]
---

# Problem Statement

Show that every compact Hausdorff topological space is normal.

That is: if $X$ is compact and Hausdorff, and $F, G \subseteq X$ are disjoint closed subsets, then there exist disjoint open subsets $U, V \subseteq X$ with $F \subseteq U$ and $G \subseteq V$.

(Since $X$ is Hausdorff in particular $T_1$, this gives the $T_4$ axiom in full, including the $T_1$ clause that singletons are closed.)

**Recall:**

![[Def - Compact Space#The Definition]]

![[Def - Separation Axioms#The Definition]]

![[Thm - Closed Subset of Compact is Compact#Formal Statement]]

A space is **Hausdorff** ($T_2$) if any two distinct points have disjoint open neighbourhoods. **Regular** ($T_3$) adds: a point and a disjoint closed set have disjoint open neighbourhoods. **Normal** ($T_4$) adds: two disjoint closed sets have disjoint open neighbourhoods.

A useful intermediate fact: **closed subsets of compact spaces are compact** ([[Thm - Closed Subset of Compact is Compact]]).

---

# Convergent Strategy

**Problem class.** A *separation-axiom upgrade*: from Hausdorff (point-vs-point separation) to normal (closed-set-vs-closed-set separation), via two stages. The route passes through regularity as an intermediate.

**Assumption pattern.** $X$ is compact and Hausdorff. $F, G \subseteq X$ are disjoint closed subsets. We have the closed-subset-of-compact-is-compact theorem, so both $F$ and $G$ are compact.

**Theorem routing.** The argument has the following structure:
1. *Lemma 1 (compact Hausdorff $\Rightarrow$ regular):* Given a point $x$ and a closed set $C$ with $x \notin C$, separate by disjoint opens. The proof uses Hausdorff to separate $x$ from each $c \in C$, then uses compactness of $C$ to extract a finite subcover.
2. *Main step (regular $+$ compactness $\Rightarrow$ normal):* Given disjoint closed $F, G$, for each $x \in F$ apply Lemma 1 to separate $x$ from $G$. Cover $F$ by the $x$-side opens, use compactness of $F$ to extract a finite subcover, assemble.

**Key decision point.** The double-iteration "for each point, find separating opens, then extract finite cover" is the canonical compactness-extraction move. The non-obvious step is that *applying this twice* — once for each closed set in the pair — gives a full normal-axiom separation.

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **Use Hausdorff to separate points pairwise.** Each pair (point of $F$, point of $G$) has disjoint open neighbourhoods. This is the raw material.

2. **Apply closed-subset-of-compact-is-compact to get compactness of $F$ and $G$.** The compactness of the ambient $X$ propagates to the closed subsets, providing the finite-subcover extraction needed.

3. **Extract a finite subcover from a compactness assumption.** For each $x \in F$ we have an open cover of $G$; by compactness of $G$, extract a finite subcover. Intersect the corresponding $x$-side opens. This converts pointwise separation into uniform separation against the whole of $G$.

4. **Iterate the procedure.** Doing this once converts (point vs. closed set) into uniform separation; doing it twice converts (closed set vs. closed set).

---

# Hints

> [!note]- Hint 1
> First prove: compact Hausdorff $\Rightarrow$ regular. Take a point $x \notin C$ closed. For each $y \in C$, by Hausdorff there are disjoint opens $U_y \ni x$, $V_y \ni y$. The $V_y$'s cover $C$, and $C$ is compact (closed in compact $X$). Extract a finite subcover $V_{y_1}, \ldots, V_{y_n}$. Let $V = V_{y_1} \cup \cdots \cup V_{y_n}$ (still covers $C$) and $U = U_{y_1} \cap \cdots \cap U_{y_n}$ (still contains $x$). Show $U \cap V = \emptyset$: any point in $V$ is in some $V_{y_i}$, and $U \subseteq U_{y_i}$, but $U_{y_i} \cap V_{y_i} = \emptyset$.

> [!note]- Hint 2
> Now prove: regular + compact $\Rightarrow$ normal. Take $F, G$ disjoint closed in $X$. $F$ is closed in compact $X$, hence compact. For each $x \in F$, $x \notin G$ closed, so by regularity (Lemma 1) there are disjoint opens $U_x \ni x$, $V_x \supseteq G$. The $U_x$'s cover $F$; by compactness of $F$, finite subcover $U_{x_1}, \ldots, U_{x_n}$. Let $U = U_{x_1} \cup \cdots \cup U_{x_n} \supseteq F$ and $V = V_{x_1} \cap \cdots \cap V_{x_n} \supseteq G$. Show $U \cap V = \emptyset$ similarly.

> [!note]- Hint 3
> The same finite-subcover-then-assemble pattern is used twice: in Lemma 1 to upgrade (point vs. point) to (point vs. closed), and in the main step to upgrade (point vs. closed) to (closed vs. closed). Each upgrade requires compactness of the relevant set.

---

# Solution

The proof is the "compactness as topological finiteness" theorem in action: compactness turns each piece of pointwise structure into a finite, uniform statement, allowing the assembly to occur.

**Step 1: Lemma 1 — Compact Hausdorff is regular.**

Let $X$ be compact Hausdorff. Let $C \subseteq X$ be closed and $x \in X \setminus C$. We construct disjoint opens $U \ni x$ and $V \supseteq C$.

> [!note]- Derivation
> *Step 1a: Pointwise separation.* For each $y \in C$, $x \neq y$, so by Hausdorff there exist disjoint opens $U_y, V_y \subseteq X$ with $x \in U_y$, $y \in V_y$, $U_y \cap V_y = \emptyset$.
>
> *Step 1b: Cover $C$.* The collection $\{V_y\}_{y \in C}$ is an open cover of $C$ (each $y \in C$ is in $V_y$).
>
> *Step 1c: $C$ is compact.* By [[Thm - Closed Subset of Compact is Compact]], $C$ closed in compact $X$ implies $C$ compact. So $\{V_y\}$ has a finite subcover $V_{y_1}, \ldots, V_{y_n}$ of $C$.
>
> *Step 1d: Assemble.* Set
> $$V = V_{y_1} \cup \cdots \cup V_{y_n}, \quad U = U_{y_1} \cap \cdots \cap U_{y_n}.$$
> Both are open: $V$ is a finite union, $U$ is a finite intersection.
> - $C \subseteq V$ by construction.
> - $x \in U$ since $x \in U_{y_i}$ for each $i$.
> - $U \cap V = \emptyset$: any point $p \in V$ lies in some $V_{y_i}$, but $U \subseteq U_{y_i}$ which is disjoint from $V_{y_i}$, so $p \notin U$. Hence $U \cap V = \emptyset$.

**Step 2: Main step — compact Hausdorff is normal.**

Let $X$ be compact Hausdorff, and let $F, G \subseteq X$ be disjoint closed subsets. We construct disjoint opens $U \supseteq F$ and $V \supseteq G$.

> [!note]- Derivation
> *Step 2a: Pointwise application of regularity.* For each $x \in F$, $x \notin G$ (since $F \cap G = \emptyset$) and $G$ is closed. By Lemma 1 (just proved), there exist disjoint opens $U_x, V_x \subseteq X$ with $x \in U_x$, $G \subseteq V_x$, $U_x \cap V_x = \emptyset$.
>
> *Step 2b: Cover $F$.* The collection $\{U_x\}_{x \in F}$ is an open cover of $F$.
>
> *Step 2c: $F$ is compact.* By [[Thm - Closed Subset of Compact is Compact]], $F$ closed in compact $X$ implies $F$ compact. So $\{U_x\}$ has a finite subcover $U_{x_1}, \ldots, U_{x_n}$ of $F$.
>
> *Step 2d: Assemble.* Set
> $$U = U_{x_1} \cup \cdots \cup U_{x_n}, \quad V = V_{x_1} \cap \cdots \cap V_{x_n}.$$
> Both are open. $F \subseteq U$ (by construction), $G \subseteq V$ (since $G \subseteq V_{x_i}$ for each $i$).
>
> $U \cap V = \emptyset$: any $p \in U$ lies in some $U_{x_i}$, but $V \subseteq V_{x_i}$ which is disjoint from $U_{x_i}$, so $p \notin V$. Hence $U \cap V = \emptyset$.
>
> So $U$ and $V$ are disjoint open neighbourhoods of $F$ and $G$ respectively. Since $F, G$ were arbitrary disjoint closed sets, $X$ is normal.

> [!note]- Complete formal solution
> Let $X$ be compact Hausdorff.
>
> **Lemma (regular).** For closed $C \subseteq X$ and $x \notin C$:
> - For each $y \in C$, Hausdorff gives disjoint opens $U_y \ni x$, $V_y \ni y$.
> - $C$ is closed in compact $X$, hence compact. The cover $\{V_y\}_{y \in C}$ has a finite subcover $V_{y_1}, \ldots, V_{y_n}$.
> - Set $V = \bigcup_i V_{y_i} \supseteq C$ (open) and $U = \bigcap_i U_{y_i} \ni x$ (open). Disjoint: $p \in V \cap U$ would give $p \in V_{y_i}$ and $p \in U_{y_i}$ for some $i$, contradiction.
>
> **Main.** For disjoint closed $F, G \subseteq X$:
> - For each $x \in F$, the lemma gives disjoint opens $U_x \ni x$, $V_x \supseteq G$.
> - $F$ is closed in compact $X$, hence compact. The cover $\{U_x\}_{x \in F}$ has a finite subcover $U_{x_1}, \ldots, U_{x_n}$.
> - Set $U = \bigcup_i U_{x_i} \supseteq F$ (open) and $V = \bigcap_i V_{x_i} \supseteq G$ (open). Disjoint: $p \in U \cap V$ would give $p \in U_{x_i}$ and $p \in V_{x_i}$ for some $i$, contradiction.
>
> So $X$ is normal. $\blacksquare$

---

# Key Takeaways

**The "iterate the finite-subcover assembly" is the universal recipe for upgrading separation axioms in the presence of compactness.** The proof has a precise modular structure: a single move — for each point in one set, separate by disjoint opens from the *other* set, cover with the resulting opens, extract a finite subcover, assemble — is applied *twice*. The first application upgrades (point vs. point) to (point vs. closed set), giving regularity. The second application upgrades (point vs. closed set) to (closed set vs. closed set), giving normality. In principle the iteration could go further (closed set vs. closed set vs. closed set — but normality already covers all such cases). Recognize the pattern: any time you have a pointwise separation property and want to upgrade to a uniform one across a *compact* set, this is the move.

**Compact + Hausdorff is exceptionally well-behaved: regular and normal come for free, continuous bijections are homeomorphisms, compact subsets are closed.** This pair of hypotheses unlocks an enormous amount of structure with minimal effort, and it is the standard setting for: most general topology theorems, classification of compact surfaces, the spectrum of a commutative $C^*$-algebra (compact Hausdorff via Gelfand duality), profinite group theory (compact Hausdorff totally disconnected). The discipline: when you see "compact Hausdorff" in a hypothesis, expect to be able to deploy normality, the continuous-bijection-is-homeomorphism upgrade, and the closed-graph theorem essentially for free.

**Closed subsets of compact spaces are compact — this little fact ([[Thm - Closed Subset of Compact is Compact]]) is the workhorse of every "extract a finite subcover from a closed subset" move in topology.** Without it, we could not extract a finite subcover of $C$ or $F$ in the proof. The compactness of these closed subsets is what allows the pointwise data to be reduced to finite data, which is what allows the final assembly. The cheapness of this lemma (its proof: add the complement of the closed subset to the cover, get a finite subcover of the ambient space, remove the complement) belies its importance. Trigger: "I need a finite subcover of a closed subset of a compact space" → use this lemma.

**The structural reason normality follows from compactness + Hausdorff is that compactness *uniformizes* pointwise data, and Hausdorff is enough to start the pointwise separation.** This is the deepest version of the take-home. The Hausdorff axiom is pointwise: it says individual pairs of points can be separated. Compactness is a uniform-finite axiom: it says any cover can be refined to a finite one, hence pointwise data parametrized by all points collapses to finite data. Composing these two operations gives uniform separation between closed sets. The same compositional structure underlies many other compactness-based theorems: extreme value theorem (pointwise local maximum + compact $\Rightarrow$ global maximum), uniform continuity (pointwise continuity + compact $\Rightarrow$ uniform continuity), and the existence of partitions of unity in differential topology.

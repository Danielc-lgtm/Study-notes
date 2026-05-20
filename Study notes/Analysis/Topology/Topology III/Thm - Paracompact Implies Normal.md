---
type: theorem
subject: topology
prereqs:
  - "Def - Paracompact Space"
  - "Def - Separation Axioms"
  - "Def - Locally Finite Family and Refinement"
tags: [analysis, topology]
---

# Notation

$X$ is a paracompact (Hausdorff) topological space. $F, G \subseteq X$ are disjoint closed sets; we want disjoint open sets separating them. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Paracompact Implies Normal.** Let $X$ be a paracompact Hausdorff space. Then $X$ is **normal**: for every pair of disjoint closed sets $F, G \subseteq X$, there exist disjoint open sets $U, V \subseteq X$ with $F \subseteq U$ and $G \subseteq V$.
>
> The intermediate step in the proof: paracompact Hausdorff is **regular** (point–closed separation).

---

# Motivation

Paracompactness is the most flexible covering condition for non-compact spaces. The theorem says that this covering condition, combined with Hausdorff, *automatically* gives normality — the strongest standard separation axiom in the Hausdorff hierarchy. So paracompact Hausdorff spaces inherit, for free, all the function-rich consequences of normality: Urysohn's lemma, Tietze extension, complete regularity, embedding in products of intervals.

Why is this the right structural fact? Because it justifies treating paracompact Hausdorff as the *default setting* for analysis on non-compact spaces. The classic spaces of analysis — manifolds, locally compact $\sigma$-compact Hausdorff spaces, metric spaces — are all paracompact Hausdorff, and they all have Urysohn and Tietze automatically.

The proof has a beautiful structure: combine the *pointwise* separation hypothesis (Hausdorff: distinct points separated by disjoint opens) with the *combinatorial* hypothesis (paracompact: locally finite refinements of covers) to produce *global* separation (normality: disjoint closeds separated by disjoint opens). The mechanism: separate locally (pointwise via Hausdorff), then assemble the local separations using local finiteness.

The first step, regularity, is the warm-up. Take a point $x$ and closed set $C$ not containing $x$. For each $y \in C$, Hausdorff gives disjoint opens $U_y \ni x$ and $V_y \ni y$. The collection $\{V_y\}_{y \in C} \cup \{X \setminus C\}$ is an open cover of $X$. By paracompactness, take a locally finite open refinement; the elements that refine into some $V_y$ together with the elements refining $X \setminus C$ form a locally finite open cover. The union of the $V_y$-refinements is open and contains $C$; its closure (by locally-finite-union = union-of-closures) does not contain $x$. So $x$ is separated from $C$ by disjoint opens — regularity.

The second step, normality, is the same argument with $C$ replaced by another closed set $F$. The structure is identical to the regularity step but applied at the level of closed-versus-closed separation.

The proof crucially uses the property that **locally finite unions of closed sets are closed** (or equivalently, $\overline{\bigcup_\alpha A_\alpha} = \bigcup_\alpha \overline{A_\alpha}$ for locally finite families). This is what allows the assembly: locally we have separations, locally we can combine them, and the locally-finite structure ensures the global assembly remains closed.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "paracompact + Hausdorff". The skill is to recognize this combination in problems where normality is needed.

The first source is **any smooth manifold**. Property $B$: a smooth manifold (Hausdorff + second countable + locally Euclidean). The bridge: manifolds are LCH + $\sigma$-compact, hence paracompact by [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]]; with Hausdorffness, paracompact Hausdorff, hence normal. So Urysohn and Tietze are available on every manifold. *Example:* the existence of smooth bump functions on a manifold, used to construct smooth partitions of unity, relies on normality from paracompactness.

The second source is **any metric space**. Property $B$: a metric space. The bridge: Stone's theorem says every metric space is paracompact; metric spaces are Hausdorff; so paracompact Hausdorff, so normal. *Example:* normality of metric spaces is a standard direct result ([[Thm - Metric Spaces are Normal]]); the paracompact route is an alternative proof.

The third source is **any locally compact $\sigma$-compact Hausdorff space**. Property $B$: e.g., an open subset of $\mathbb{R}^n$, a locally finite CW complex. The bridge: LCH + $\sigma$-compact ⇒ paracompact (Bredon 12.11); with Hausdorffness, normal. So Urysohn and Tietze are available on every such space.

**Targets (Output Amplification)**

The conclusion is "paracompact Hausdorff implies normal".

Combine the conclusion with **Urysohn's lemma**. Property $D$: two disjoint closed sets $F, G$. The amplified result $E$: a continuous Urysohn function separating them. The combination is: paracompact Hausdorff ⇒ normal ⇒ Urysohn applies. This gives access to all of [[Thm - Urysohn's Lemma]] in paracompact Hausdorff spaces.

Combine the conclusion with **Tietze extension**. Property $D$: a continuous bounded function on a closed subspace. The amplified result $E$: continuous extension to the whole space. The combination: paracompact Hausdorff ⇒ normal ⇒ Tietze applies. Used for extending sections of bundles, prescribed boundary data, etc.

Combine the conclusion with **partition of unity construction**. Property $D$: an open cover of a paracompact Hausdorff space. The amplified result $E$: a subordinate partition of unity. The combination: paracompactness gives the locally finite refinement; normality (from this theorem) gives the Urysohn functions; together they assemble into a partition. See [[Thm - Paracompact Has Partitions of Unity]].

---

# Why Is It True

The intuition: paracompactness says you can refine open covers to locally finite ones; Hausdorff says points can be separated pairwise; together they let you "average" the pairwise separations to global ones using the locally-finite structure.

The argument runs in two stages:

**Stage 1: Regularity (point ↔ closed set).**
Take $x \notin C$ closed. Use Hausdorff at each $y \in C$ to find disjoint opens $U_y \ni x$ and $V_y \ni y$. The collection $\{V_y\}_{y \in C} \cup \{X \setminus C\}$ is an open cover of $X$. Take a locally finite open refinement; the refinement contains finitely many sets near $x$, so finitely many $V_y$-refinements (each is contained in some $V_y$ and disjoint from the corresponding $U_y \ni x$). Take the union of these $V_y$-refinements as the open neighborhood of $C$; its closure is the union of closures (locally finite!), which is contained in $X \setminus \{x\}$ (each closure is in some $X \setminus U_y \subseteq X \setminus \{x\}$ — wait, $X \setminus U_y$ does not contain $x$ since $x \in U_y$, but it does contain $V_y$). The complement of this closure is an open neighborhood of $x$ disjoint from the open neighborhood of $C$.

**Stage 2: Normality (closed ↔ closed).**
Take disjoint closeds $F, G$. By Stage 1 (regularity), for each $x \in F$, find an open $U_x \ni x$ with $\overline{U_x} \cap G = \emptyset$ — separate $x$ from $G$ by disjoint opens, then take the open one around $x$. The collection $\{U_x\}_{x \in F} \cup \{X \setminus F\}$ is an open cover of $X$. Take a locally finite refinement; the refinement elements that refine into some $U_x$ together form a locally finite family whose union is open and contains $F$. The closure of this union (using locally finite ⇒ union of closures = closure of union) avoids $G$ (each $\overline{U_x}$ avoids $G$). The complement of this closure is an open neighborhood of $G$ disjoint from the open neighborhood of $F$.

The key technique is the **locally-finite closure trick**: if $\{V_\alpha\}$ is locally finite, then $\overline{\bigcup V_\alpha} = \bigcup \overline{V_\alpha}$, so the closure of the union is itself a controlled assembly of the individual closures. Without local finiteness, the closure could "spill" to include limit points not in any individual closure.

Why does paracompactness suffice (rather than mere refinability)? Because we need *both* locally finite (for the closure trick) and open (for the union to be open). Paracompact provides exactly this combination.

---

# What Makes This Hard

The non-obvious step is the **locally-finite closure manipulation**: recognizing that $\overline{\bigcup V_\alpha} = \bigcup \overline{V_\alpha}$ for locally finite $\{V_\alpha\}$, and using this to control the closure of the assembled open neighborhood. Most people, attempting the proof, focus on the pointwise Hausdorff separations and miss the assembly step — they produce locally separating opens but cannot combine them into a global separation. The most common error is to take the union of pointwise opens without checking local finiteness, leading to a closure that spreads too far and meets the other closed set. A second common slip is to forget that regularity is the warm-up: the normality argument is the same structure applied at one level higher (closed-closed instead of point-closed).

---

# Rederivation Scaffold

**High-level strategy:**
Prove regularity first (point-closed separation), then bootstrap to normality using the same argument structure with one closed set in place of a point. Both steps use Hausdorff for pointwise separations, paracompactness for locally finite refinements, and the locally-finite closure trick to assemble.

**Subgoal decomposition:**

1. **Regularity step.** For $x \notin C$ closed, find disjoint open $U \ni x$ and open $V \supseteq C$.
   - *Hint:* At each $y \in C$, Hausdorff gives disjoint opens around $x$ and $y$; cover $X$ by these (plus $X \setminus C$); take a locally finite refinement; assemble.
   - *Why needed:* Half of normality, and the structural pattern.

2. **Strengthen: closed neighborhood of $x$.** For $x \notin C$, find an open $W \ni x$ with $\overline W \cap C = \emptyset$.
   - *Hint:* Apply step 1 to get separating $U, V$; then $\overline U \subseteq X \setminus V$ closed, disjoint from $C \subseteq V$.
   - *Why needed:* The form needed for the normality argument.

3. **Normality step.** For disjoint closed $F, G$, find disjoint open $U \supseteq F$ and $V \supseteq G$.
   - *Hint:* By step 2 applied at each $x \in F$, find $W_x$ open with $x \in W_x$ and $\overline{W_x} \cap G = \emptyset$. Cover $X$ by $\{W_x\}_{x \in F} \cup \{X \setminus F\}$; take locally finite refinement; assemble.
   - *Why needed:* The conclusion.

4. **Apply the locally-finite closure trick.** $\overline{\bigcup_\alpha V_\alpha} = \bigcup_\alpha \overline{V_\alpha}$ for locally finite $\{V_\alpha\}$ — used to control the closure in steps 1 and 3.
   - *Hint:* See [[Def - Locally Finite Family and Refinement]] for the proof.
   - *Why needed:* The key combinatorial step.

---

# Lemma Decomposition

> [!note]- Lemma 1: Locally finite union closure equals union of closures
> **Statement:** Let $\{V_\alpha\}_{\alpha \in A}$ be a locally finite family of subsets of a topological space. Then $\overline{\bigcup_\alpha V_\alpha} = \bigcup_\alpha \overline{V_\alpha}$.
>
> **Hint:** $\supseteq$ is trivial (each $\overline{V_\alpha}$ is in the closure of the union). For $\subseteq$: a limit point of $\bigcup V_\alpha$ has a neighborhood meeting only finitely many $V_\alpha$ (local finiteness), so it is a limit point of a finite union, which equals its own closure (union of closures).
>
> **Why needed:** The key step for assembling local separations.
>
> > [!note]- Full proof
> > $\supseteq$: $V_\alpha \subseteq \bigcup_\beta V_\beta$, so $\overline{V_\alpha} \subseteq \overline{\bigcup_\beta V_\beta}$. Hence $\bigcup_\alpha \overline{V_\alpha} \subseteq \overline{\bigcup_\beta V_\beta}$.
> >
> > $\subseteq$: Let $x \in \overline{\bigcup_\alpha V_\alpha}$. By local finiteness, there is a neighborhood $N$ of $x$ meeting only finitely many $V_{\alpha_1}, \dots, V_{\alpha_k}$.
> >
> > Then $\bigcup_\alpha V_\alpha \cap N = (V_{\alpha_1} \cup \cdots \cup V_{\alpha_k}) \cap N$, so $x \in \overline{(V_{\alpha_1} \cup \cdots \cup V_{\alpha_k}) \cap N} \subseteq \overline{V_{\alpha_1} \cup \cdots \cup V_{\alpha_k}} = \overline{V_{\alpha_1}} \cup \cdots \cup \overline{V_{\alpha_k}}$ (finite union of closed is closed; finite union of closures equals closure of finite union). So $x \in \bigcup_\alpha \overline{V_\alpha}$.

> [!note]- Lemma 2: Regular Hausdorff property derived from paracompact Hausdorff
> **Statement:** Every paracompact Hausdorff space is regular: for $x \in X$ and closed $C \subseteq X$ with $x \notin C$, there exist disjoint open sets $U \ni x$ and $V \supseteq C$.
>
> **Hint:** At each $y \in C$, Hausdorff gives disjoint opens; cover $X$, refine to locally finite; the union of refining elements is the desired $V$, and a neighborhood of $x$ missing all the locally-finitely-many refining elements is $U$.
>
> **Why needed:** The intermediate step en route to normality.
>
> > [!note]- Full proof
> > For each $y \in C$, $y \neq x$ (since $x \notin C$). By Hausdorff, there exist disjoint open sets $U_y \ni x$ and $V_y \ni y$. The collection $\{V_y\}_{y \in C} \cup \{X \setminus C\}$ is an open cover of $X$ ($x \in X \setminus C$ since $C$ closed; points of $C$ in their $V_y$; other points either in $X \setminus C$ or in some $V_y$).
> >
> > By paracompactness, take a locally finite open refinement $\{W_\beta\}_{\beta \in B}$. Partition $B$ into $B_C = \{\beta : W_\beta \subseteq V_y \text{ for some } y\}$ and $B_0 = B \setminus B_C$ (those refining $X \setminus C$).
> >
> > Set $V = \bigcup_{\beta \in B_C} W_\beta$ — open, and $V \supseteq C$ (every $y \in C$ is in some $V_y$, hence in some $W_\beta$ with $\beta \in B_C$).
> >
> > We need an open $U \ni x$ disjoint from $V$. By local finiteness at $x$, there is a neighborhood $N_x$ of $x$ meeting only finitely many $W_\beta$, say $W_{\beta_1}, \dots, W_{\beta_k}$. The $W_{\beta_i}$ that have $\beta_i \in B_C$ are each in some $V_{y_i}$, hence disjoint from $U_{y_i} \ni x$. Set $U = N_x \cap \bigcap_i U_{y_i}$ — a finite intersection of opens containing $x$, hence open and containing $x$. For each $\beta \in B_C$ with $W_\beta$ meeting $N_x$, $W_\beta \subseteq V_{y_i}$ for some $i$ with $\beta = \beta_i$, so $W_\beta \cap U_{y_i} = \emptyset$, so $W_\beta \cap U = \emptyset$.
> >
> > For $\beta \in B_C$ with $W_\beta$ NOT meeting $N_x$: $W_\beta \cap U \subseteq W_\beta \cap N_x = \emptyset$.
> >
> > Hence $U \cap V = U \cap \bigcup_{\beta \in B_C} W_\beta = \emptyset$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be paracompact Hausdorff.
>
> **Step 1: Regularity.** By Lemma 2, $X$ is regular: for any point $x$ and closed $C \not\ni x$, there are disjoint open $U \ni x$ and $V \supseteq C$.
>
> **Step 2: Closed neighborhood of a point.** Given $x$ and closed $C \not\ni x$, by Step 1 find disjoint open $U_0 \ni x$ and $V_0 \supseteq C$. Then $\overline{U_0} \subseteq X \setminus V_0$ (the complement of $V_0$ is closed and contains $U_0$, hence contains $\overline{U_0}$). So $\overline{U_0} \cap C \subseteq (X \setminus V_0) \cap V_0 = \emptyset$. So $U_0$ is an open neighborhood of $x$ whose closure is disjoint from $C$.
>
> **Step 3: Normality.** Let $F, G \subseteq X$ be disjoint closed sets.
>
> For each $x \in F$, $x \notin G$ (since $F \cap G = \emptyset$). By Step 2, find $W_x$ open with $x \in W_x$ and $\overline{W_x} \cap G = \emptyset$.
>
> The collection $\{W_x\}_{x \in F} \cup \{X \setminus F\}$ is an open cover of $X$. By paracompactness, take a locally finite open refinement $\{T_\gamma\}_{\gamma \in C}$. Partition $C$ into $C_F = \{\gamma : T_\gamma \subseteq W_x \text{ for some } x \in F\}$ and $C_0 = C \setminus C_F$.
>
> Set $U = \bigcup_{\gamma \in C_F} T_\gamma$ — open, and $U \supseteq F$ (every $x \in F$ is in some $W_x$, hence in some $T_\gamma$ that refines into $W_x$).
>
> Now: $\overline U = \overline{\bigcup_{\gamma \in C_F} T_\gamma} = \bigcup_{\gamma \in C_F} \overline{T_\gamma}$ by Lemma 1 (locally finite, hence locally finite when restricted to $C_F$). Each $\overline{T_\gamma} \subseteq \overline{W_{x_\gamma}}$ for some $x_\gamma$ (since $T_\gamma \subseteq W_{x_\gamma}$ and taking closures preserves containment), and $\overline{W_{x_\gamma}} \cap G = \emptyset$, so $\overline{T_\gamma} \cap G = \emptyset$. So $\overline U \cap G = \emptyset$.
>
> Set $V = X \setminus \overline U$ — open (complement of closed) and contains $G$ (since $\overline U \cap G = \emptyset$ means $G \subseteq X \setminus \overline U$).
>
> $U \cap V = U \cap (X \setminus \overline U) \subseteq \overline U \cap (X \setminus \overline U) = \emptyset$.
>
> So $U \supseteq F$, $V \supseteq G$, $U \cap V = \emptyset$, $U, V$ open. $X$ is normal. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Normality of smooth manifolds.** Every smooth manifold is paracompact Hausdorff (by definition or by being LCH + second countable), hence normal. This is what gives rise to **smooth Urysohn functions** and **smooth Tietze extensions** on manifolds, the workhorses of differential geometry. The application illustrates how this theorem makes the smoothness machinery work.

**Smooth partitions of unity.** Given a paracompact Hausdorff manifold and an open cover, by paracompactness take a locally finite refinement; by normality (from this theorem) apply Urysohn to each pair (closed shrinkage, complement of original cover element) to get bumps; normalize. The two-step "refine then bump" uses paracompactness for the refinement and normality (from paracompactness via this theorem) for the bumps.

**Construction of $\beta X$ via the Tychonoff embedding.** For a paracompact Hausdorff space, normality (from this theorem) implies completely regular, hence Stone–Čech compactification exists. The connection: paracompact Hausdorff is a sufficient condition for completely regular, the precondition of [[Thm - Stone–Čech Compactification]].

---

# Bridges

- **[[Def - Paracompact Space]]** — the precondition.

- **[[Def - Separation Axioms]]** — normality is one of the separation axioms; the theorem upgrades paracompact Hausdorff to fully normal.

- **[[Def - Locally Finite Family and Refinement]]** — the technical tool: locally finite families allow assembly of pointwise separations.

- **[[Thm - Urysohn's Lemma]]** — a downstream consequence: with normality in hand, Urysohn applies.

- **[[Thm - Tietze Extension Theorem]]** — another downstream consequence: with normality, Tietze applies.

- **[[Thm - Paracompact Has Partitions of Unity]]** — uses both paracompactness (for the locally finite refinement) and normality from this theorem (for the Urysohn bumps).

- **[[Thm - Metric Spaces are Normal]]** — an alternative proof of normality for metric spaces, which are paracompact (Stone).

---

# Unlocked by This

> [!tip] Urysohn Lemma on Paracompact Hausdorff *(from this topic)*
> Urysohn's lemma is automatically available on every paracompact Hausdorff space: paracompact Hausdorff ⇒ normal ⇒ Urysohn. This is what powers Urysohn functions on manifolds, in metric spaces, and in CW complexes.

> [!tip] Tietze Extension on Paracompact Hausdorff *(from this topic)*
> Tietze extension is automatically available on every paracompact Hausdorff space, by the same chain: paracompact Hausdorff ⇒ normal ⇒ Tietze. This is the underpinning of section extensions for vector bundles and continuous extensions of functions on manifolds.

> [!tip] Smooth Partitions of Unity on Manifolds *(from Differential Geometry)*
> Smooth manifolds are paracompact Hausdorff. By this theorem they are normal. Normality plus paracompactness yields the existence of partitions of unity, which yields the existence of Riemannian metrics, connections, and integration of smooth forms.

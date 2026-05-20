---
type: theorem
subject: topology
prereqs:
  - "Def - Locally Compact Space"
  - "Def - Paracompact Space"
  - "Def - Compact Space"
  - "Def - Locally Finite Family and Refinement"
tags: [analysis, topology]
---

# Notation

$X$ is a locally compact, $\sigma$-compact, Hausdorff space. $\sigma$-compact: $X = \bigcup_{n=1}^\infty C_n$ for some sequence of compact sets $C_n$. We write $\operatorname{int}(K)$ for the interior of $K$, $\overline U$ for the closure of $U$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Locally Compact σ-Compact Hausdorff is Paracompact.** Let $X$ be a topological space that is **locally compact**, **σ-compact**, and **Hausdorff**. Then $X$ is **paracompact**.
>
> Equivalently: $X$ has an **exhaustion by compact sets** with controlled interiors: $X = \bigcup_{n=1}^\infty K_n$ where each $K_n$ is compact and $K_n \subseteq \operatorname{int}(K_{n+1})$. Given an open cover, refine within each "shell" $K_{n+1} \setminus \operatorname{int}(K_n)$ to get a locally finite global refinement.

---

# Motivation

The question: when is a non-compact space paracompact? Paracompactness is the topological condition that unlocks partitions of unity, and we want sufficient conditions that are easy to verify.

The standard combination is: **locally compact + Hausdorff + σ-compact**. These three are independent: $\mathbb{Q}$ is Hausdorff and σ-compact (it is countable, even discrete-σ-compact) but not locally compact; the long line is locally compact and Hausdorff but not σ-compact; an uncountable discrete space is locally compact, Hausdorff, but not σ-compact. The combination, however, gives paracompact.

The proof uses a beautiful technique: **exhaustion by compact sets**. From σ-compactness, $X = \bigcup C_n$ with $C_n$ compact. From local compactness, each compact set is contained in a "fatter" compact with non-empty interior structure. Combining, one constructs an exhaustion $X = \bigcup K_n$ where:
- $K_n$ compact,
- $K_n \subseteq \operatorname{int}(K_{n+1})$ (strict inner containment),
- $\bigcup_n \operatorname{int}(K_n) = X$.

The "concentric rings" $A_n = K_n \setminus \operatorname{int}(K_{n-1})$ are compact (closed in $K_n$, compact). The technique: given an open cover of $X$, restrict to a slightly thickened ring $K_{n+1} \setminus \operatorname{int}(K_{n-1})$ which is compact; take a finite subcover within the ring (compactness); union over $n$ gives a global cover; the rings overlap only with neighbors (each piece intersects only its $\pm 1$ neighbor), so the global cover is *locally finite*. This is the paracompact refinement.

The key insight is that **the exhaustion structures the space into compact rings**, each of which gives a finite cover, and **each ring only interacts with its immediate neighbors**. This bounded interaction is what gives local finiteness.

This theorem is the standard route by which **smooth manifolds**, **CW complexes with countably many cells**, **open subsets of $\mathbb{R}^n$**, and other natural spaces acquire paracompactness. The chain: LCH + second countable ⇒ σ-compact (a standard implication), so LCH + second countable ⇒ paracompact via this theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "LCH + σ-compact". The skill is to recognize when σ-compactness is available.

The first source is **a topological manifold (Hausdorff + locally Euclidean + second countable)**. Property $B$: a topological manifold $M$. The bridge: locally Euclidean implies locally compact (each point has a compact neighborhood — closed ball in a chart); second countable plus locally compact implies σ-compact (a standard implication: cover by countably many compact closures of basic opens); Hausdorff is given. So manifolds are LCH + σ-compact, hence paracompact by this theorem. *Example:* every smooth manifold automatically supports partitions of unity, because this theorem gives paracompactness, hence the existence theorem.

The second source is **a locally compact Hausdorff space that is also second countable**. Property $B$: an LCH space with countable basis. The bridge: from a countable basis, take basic opens with compact closures (possible by local compactness — every point has a compact neighborhood, find a basis element inside); countably many such cover, giving σ-compactness. So LCH + second countable ⇒ paracompact.

The third source is **a finite-dimensional CW complex**. Property $B$: a CW complex with finitely many cells in each dimension, but possibly infinitely many in total. The bridge: each compact subset meets only finitely many cells; the union of $n$-skeleta is σ-compact (finite skeleton at each level); combined with local compactness (CW complexes are locally finite if each vertex is in finitely many cells), paracompact by this theorem. Note: not every CW complex is locally compact; the locally finite ones are.

**Targets (Output Amplification)**

The conclusion is "$X$ is paracompact".

Combine the conclusion with **the partition of unity existence theorem**. Property $D$: an open cover of $X$. The amplified result $E$: a subordinate partition of unity exists. The combination: this theorem gives paracompactness, which by [[Thm - Paracompact Has Partitions of Unity]] gives partitions of unity.

Combine the conclusion with **the normality of paracompact Hausdorff spaces**. Property $D$: disjoint closed sets in $X$. The amplified result $E$: separated by Urysohn-style continuous functions, extendable by Tietze. The combination: paracompact Hausdorff ⇒ normal ⇒ Urysohn + Tietze.

Combine the conclusion with **the exhaustion structure**. Property $D$: a continuous function or section to be constructed globally on $X$. The amplified result $E$: construct on each shell $A_n$ (compact), combine using the locally finite partition. The combination is the "build globally from concentric rings" technique, used in dimensional theory, sheaf theory, and the construction of Borel–Moore homology.

---

# Why Is It True

The intuition: from σ-compactness we have a countable union of compacts; from local compactness we can "fatten" each compact to have a compact closure with strict containment; this gives an exhaustion by compacts where each one's interior contains the previous. The exhaustion partitions $X$ into "concentric rings" (compact pieces) that interact only with neighbors. Locally finite covers of each ring assemble into a global locally finite cover.

**Step 1: Construct the exhaustion.** Set $K_1 = C_1$ (or any compact). Inductively, given $K_n$ compact, by local compactness each $x \in K_n$ has a compact neighborhood $L_x$; the finite cover $\{L_{x_i}\}$ of $K_n$ gives a compact $K_n^+ = \bigcup_i L_{x_i}$ with $K_n \subseteq \operatorname{int}(K_n^+)$ (since each $x_i \in \operatorname{int}(L_{x_i})$, and finite unions of opens are open, $\operatorname{int}(K_n^+) \supseteq \bigcup_i \operatorname{int}(L_{x_i}) \supseteq K_n$). Set $K_{n+1} = K_n^+ \cup C_{n+1}$ — compact (union of two compacts), and $K_n \subseteq \operatorname{int}(K_n^+) \subseteq \operatorname{int}(K_{n+1})$.

By induction, $K_n$ compact, $K_n \subseteq \operatorname{int}(K_{n+1})$, and $\bigcup_n K_n \supseteq \bigcup_n C_n = X$, so $\bigcup_n K_n = X$ and indeed $\bigcup_n \operatorname{int}(K_n) = X$ (each $x \in K_n$ for some $n$, hence $\operatorname{int}(K_{n+1})$).

**Step 2: Define the shells.** Let $A_n = K_n \setminus \operatorname{int}(K_{n-1})$ (with $K_0 = \emptyset$). Each $A_n$ is closed (complement of open in closed) inside $K_n$ (compact), hence compact. The $A_n$ form a (closed) cover of $X$: every $x \in X$ is in some $K_m$ but not in $K_0 = \emptyset$, so for the smallest $n$ with $x \in K_n$, $x \in K_n \setminus K_{n-1} \subseteq A_n$.

The crucial property: $A_n$ meets only $A_{n-1}$, $A_n$, $A_{n+1}$ (and the shells themselves are pairwise disjoint or only border-overlapping, since the inner-containment $K_{n-1} \subseteq \operatorname{int}(K_n)$ means $A_n$ does not extend below $K_{n-1}$'s interior).

**Step 3: Refine the cover within each shell.** Given an open cover $\{U_\alpha\}$ of $X$, restrict to a slightly thickened shell $B_n = K_{n+1} \setminus \operatorname{int}(K_{n-2})$ (so $B_n$ is open and compact-thickened). The cover $\{U_\alpha \cap B_n\}_\alpha$ covers the compact $K_{n+1} \setminus \operatorname{int}(K_{n-1}) \supseteq A_n$, and by compactness of $K_{n+1} \setminus \operatorname{int}(K_{n-1})$ (a closed subset of compact $K_{n+1}$), there is a finite subcover. Take these finitely many opens (intersected with the open $B_n$ to keep them open) — each is open, each is in some $U_\alpha$, each lies inside the larger thickened shell.

**Step 4: Union the refinements.** The collection $\{\text{finite refinement at shell } n\}_n$ is a global refinement of $\{U_\alpha\}$ (covering $A_n \subseteq$ refinements within shell $n$, and these cover $X$). Local finiteness: every point lies in some $A_n$, with a neighborhood inside the open $\operatorname{int}(K_{n+1}) \setminus K_{n-2}$, which only meets the finite refinements from shells $n-1, n, n+1$. So only finitely many refinement elements meet any point's neighborhood — local finiteness.

The result is a locally finite open refinement, so $X$ is paracompact.

---

# What Makes This Hard

The non-obvious step is the **construction of the exhaustion** $K_n \subseteq \operatorname{int}(K_{n+1})$ with strict inner containment. Local compactness alone gives compact neighborhoods, but the strict inner containment requires the "fatten and union" step: cover the previous compact by finite compact neighborhoods, take their union, and add the next σ-compact piece. The most common error is to skip the inner-containment step (which is essential for the shells to have positive "width" and the locally finite assembly to work), producing an exhaustion where shells degenerate to single points. Another non-obvious aspect is using a *thickened* shell $B_n$ in step 3 (rather than just $A_n$) so that the refinement elements are *open* and cover the shell *plus* a neighborhood.

---

# Rederivation Scaffold

**High-level strategy:**
Build a compact exhaustion $K_1 \subseteq \operatorname{int}(K_2) \subseteq K_2 \subseteq \operatorname{int}(K_3) \subseteq \cdots$ with $\bigcup K_n = X$. Cover each "shell" $A_n = K_n \setminus \operatorname{int}(K_{n-1})$ (compact) by finitely many cover-elements, restricted to a slightly thickened open neighborhood of the shell. The union of these finite per-shell refinements is locally finite globally.

**Subgoal decomposition:**

1. **Construct the exhaustion.** Build $K_n$ compact with $K_n \subseteq \operatorname{int}(K_{n+1})$ and $\bigcup K_n = X$.
   - *Hint:* Inductively cover $K_n$ by finitely many compact neighborhoods, union them, add the next σ-compact piece.
   - *Why needed:* Provides the concentric structure.

2. **Identify shells $A_n$.** $A_n = K_n \setminus \operatorname{int}(K_{n-1})$, compact (closed in $K_n$).
   - *Hint:* Shells form a closed cover; each $A_n$ is compact.
   - *Why needed:* Partitions $X$ into compact "rings" for finite refinement.

3. **Finite refinement on each shell.** Given an open cover $\{U_\alpha\}$, restrict to the slightly larger open $\operatorname{int}(K_{n+1}) \setminus K_{n-2}$ (containing $A_n$); use compactness of $A_n$ to extract a finite subcover.
   - *Hint:* The thickened neighborhood is open, the shell-plus-thickening is contained in $\operatorname{int}(K_{n+1}) \setminus K_{n-2}$, which only meets adjacent shells.
   - *Why needed:* Produces finite open refinements interacting only with neighbors.

4. **Assemble globally.** The union of per-shell refinements is a global cover, locally finite because each point's neighborhood meets only finitely many shells.
   - *Hint:* Local finiteness: at $x \in A_n$, a neighborhood inside $\operatorname{int}(K_{n+1}) \setminus K_{n-2}$ only meets refinements from shells $n-1, n, n+1$.
   - *Why needed:* Completes the proof of paracompactness.

---

# Lemma Decomposition

> [!note]- Lemma 1: Compact set in LCH has compact neighborhood with strictly larger interior
> **Statement:** Let $X$ be locally compact Hausdorff and $K \subseteq X$ compact. There exists a compact set $K'$ with $K \subseteq \operatorname{int}(K')$.
>
> **Hint:** Each $x \in K$ has a compact neighborhood $L_x$ with $x \in \operatorname{int}(L_x)$. Finite cover of $K$ by such $L_{x_i}$; take $K' = \bigcup L_{x_i}$.
>
> **Why needed:** The inductive step in constructing the exhaustion.
>
> > [!note]- Full proof
> > For each $x \in K$, by local compactness $x$ has a compact neighborhood $L_x$; in LCH, we can choose $L_x$ to be the closure of a relatively compact open ball $V_x$ (i.e., $V_x \subseteq L_x = \overline{V_x}$ compact). So $x \in V_x \subseteq L_x$ with $V_x$ open.
> >
> > The $\{V_x\}$ form an open cover of $K$; by compactness of $K$, take a finite subcover $V_{x_1}, \dots, V_{x_n}$. Set $K' = \bigcup_i L_{x_i}$ — compact (finite union of compacts) and contains $K \subseteq \bigcup_i V_{x_i} \subseteq \operatorname{int}(K')$ (since $\bigcup_i V_{x_i}$ is open and $\subseteq K'$).

> [!note]- Lemma 2: Exhaustion of σ-compact LCH by compact sets with inner containment
> **Statement:** Let $X$ be locally compact Hausdorff and σ-compact, with $X = \bigcup_n C_n$ for $C_n$ compact. There exists a sequence $\{K_n\}_n$ of compact sets with $K_n \subseteq \operatorname{int}(K_{n+1})$ and $\bigcup_n K_n = X$.
>
> **Hint:** Inductively, starting from $K_1 = C_1$, apply Lemma 1 and union with the next $C_n$.
>
> **Why needed:** Provides the exhaustion structure for the main proof.
>
> > [!note]- Full proof
> > Set $K_1 = C_1$ (compact). Given $K_n$ compact, by Lemma 1 find a compact $K_n^+$ with $K_n \subseteq \operatorname{int}(K_n^+)$. Set $K_{n+1} = K_n^+ \cup C_{n+1}$ — compact (union of two compacts), with $K_n \subseteq \operatorname{int}(K_n^+) \subseteq \operatorname{int}(K_{n+1})$ (the interior of a containing set contains the interior).
> >
> > $\bigcup_n K_n \supseteq \bigcup_n C_n = X$ (since $C_n \subseteq K_n$ for $n \geq 2$, and $C_1 = K_1$). So $\bigcup_n K_n = X$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be locally compact Hausdorff and σ-compact.
>
> **Step 1: Exhaustion.** By Lemma 2, find compact $K_1 \subseteq K_2 \subseteq \cdots$ with $K_n \subseteq \operatorname{int}(K_{n+1})$ and $\bigcup_n K_n = X$. Set $K_0 = K_{-1} = \emptyset$ for index convention.
>
> **Step 2: Shells.** Define $A_n = K_n \setminus \operatorname{int}(K_{n-1})$. $A_n$ is closed (complement of open) inside $K_n$ (compact), so $A_n$ is compact. Also, $X = \bigcup_n A_n$ (each $x \in K_m$ for some smallest $m$, hence $x \in A_m$).
>
> **Step 3: Thickened shells.** Define $B_n = \operatorname{int}(K_{n+1}) \setminus K_{n-2}$ for $n \geq 1$ (with $K_{-1} = \emptyset$). $B_n$ is open (intersection of open $\operatorname{int}(K_{n+1})$ with open $X \setminus K_{n-2}$). And $B_n \supseteq A_n$: if $x \in A_n = K_n \setminus \operatorname{int}(K_{n-1})$, then $x \in K_n \subseteq \operatorname{int}(K_{n+1})$, and $x \notin \operatorname{int}(K_{n-1}) \supseteq K_{n-2}$ (since $K_{n-2} \subseteq \operatorname{int}(K_{n-1})$), so $x \in B_n$.
>
> The crucial geometric fact: $B_n \cap B_m = \emptyset$ for $|n - m| \geq 3$. (If $x \in B_n$, then $x \in K_{n+1}$ and $x \notin K_{n-2}$, so $x$'s "level" is between $n-2$ and $n+1$. If $x \in B_m$ similarly, $x$'s level is between $m-2$ and $m+1$. The intersection condition forces $|n - m| \leq 3$, with strict bound $|n-m| \leq 2$ after a careful look; certainly $|n-m| \geq 3$ gives empty intersection.)
>
> **Step 4: Refinement.** Let $\{U_\alpha\}$ be an open cover of $X$. For each $n$, consider the compact set $A_n$ (or, more conveniently, $K_n \setminus \operatorname{int}(K_{n-1})$ which is $A_n$). The collection $\{U_\alpha \cap B_n : \alpha \in A\}$ is an open cover of $A_n \subseteq B_n$ — each set is open in $X$ (intersection of open with open), and the family covers $A_n$. By compactness of $A_n$, take a finite subcover $\{V_{n,1}, \dots, V_{n,k(n)}\}$ where each $V_{n,j} = U_{\alpha(n,j)} \cap B_n$ for some $\alpha(n, j)$.
>
> **Step 5: Global refinement.** Let $\mathcal{V} = \{V_{n,j} : n \geq 1, 1 \leq j \leq k(n)\}$. We show $\mathcal{V}$ is a locally finite open refinement of $\{U_\alpha\}$ covering $X$.
>
> *Open:* Each $V_{n,j}$ is an intersection of two opens. ✓
>
> *Refines $\{U_\alpha\}$:* $V_{n,j} \subseteq U_{\alpha(n,j)}$. ✓
>
> *Covers $X$:* Every $x \in X$ is in some $A_n$, hence in some $V_{n,j}$ (the finite cover of $A_n$). ✓
>
> *Locally finite:* Let $x \in X$, $x \in A_n$ for the smallest such $n$. The open neighborhood $B_n$ of $x$ contains only the finite refinement elements from levels $m$ with $B_m \cap B_n \neq \emptyset$, which are at most $|m - n| \leq 2$, i.e., 5 levels ($n-2, n-1, n, n+1, n+2$). Each level contributes finitely many refinement elements ($k(m)$ of them). So $B_n$ meets at most $\sum_{|m - n| \leq 2} k(m) < \infty$ refinement elements. So $\mathcal V$ is locally finite at $x$, for every $x$.
>
> $X$ is paracompact. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**$\mathbb{R}^n$ is paracompact.** $\mathbb{R}^n$ is locally compact (closed balls are compact), Hausdorff, and σ-compact ($\mathbb{R}^n = \bigcup_n \overline{B(0, n)}$, each closed ball compact). By this theorem, paracompact. Hence Urysohn, Tietze, partitions of unity all available on $\mathbb{R}^n$. The application is foundational.

**Smooth manifolds are paracompact.** A smooth manifold $M$ is locally Euclidean (locally homeomorphic to $\mathbb{R}^n$, hence locally compact); Hausdorff (by definition); second countable (by definition). Second countable + locally compact ⇒ σ-compact (standard implication: take a countable basis of compact-closed opens). By this theorem, $M$ is paracompact, hence has partitions of unity, hence has Riemannian metrics, connections, etc.

**Open subsets of $\mathbb{R}^n$ are paracompact.** An open $U \subseteq \mathbb{R}^n$ is locally compact (closed balls inside $U$ are compact), Hausdorff, σ-compact (countable union of compact closures of basis elements). By this theorem, paracompact. The application is to PDE and harmonic analysis on open domains.

**The product of two LCH σ-compact spaces is LCH σ-compact, hence paracompact.** Product of locally compact is locally compact (finite products); Hausdorff is preserved; σ-compact ($X \times Y = \bigcup_{n,m} C_n^X \times C_m^Y$, a countable union of compacts). Hence paracompact by this theorem.

---

# Bridges

- **[[Def - Locally Compact Space]]** — one of the preconditions; provides compact neighborhoods used in the exhaustion.

- **[[Def - Paracompact Space]]** — the conclusion.

- **[[Thm - Paracompact Has Partitions of Unity]]** — the downstream consequence; partitions of unity exist via paracompactness from this theorem.

- **[[Thm - Paracompact Implies Normal]]** — another downstream consequence; normality from paracompactness via this theorem.

- **Stone's theorem (metric ⇒ paracompact)** — an alternative route to paracompactness for metric spaces, not requiring σ-compactness.

---

# Unlocked by This

> [!tip] Paracompactness of Smooth Manifolds *(from Differential Geometry)*
> Every smooth manifold (Hausdorff + locally Euclidean + second countable) is paracompact by this theorem. Hence smooth manifolds support partitions of unity, Riemannian metrics, and integration.

> [!tip] Paracompactness of Open Subsets of $\mathbb{R}^n$ *(from PDE / Real Analysis)*
> Every open subset of $\mathbb{R}^n$ is LCH σ-compact, hence paracompact. PDE on such domains can use partition-of-unity techniques.

> [!tip] One-Point Compactification of σ-Compact LCH is Second Countable *(from Topology)*
> If $X$ is LCH and σ-compact, $X^+$ is second countable and metrizable. Combined with the metrization theorem (Urysohn metrization, applied to $X^+$), this gives a metric on $X^+$ and hence on $X$.

> [!tip] Soft Sheaf Acyclicity *(from Sheaf Theory)*
> Soft sheaves on paracompact Hausdorff spaces are acyclic for sheaf cohomology. Combined with this theorem, σ-compact LCH spaces support the full sheaf-theoretic machinery.

---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Group"
  - "Def - Separation Axioms"
  - "Thm - Symmetric Neighborhoods Form a Basis at the Identity"
  - "Thm - Translations are Homeomorphisms"
tags: [analysis, topology, topological-group, separation-axioms]
---

# Notation

$G$ a topological group; $e$ the identity. Recall: $G$ is **regular** if for any closed $C \subseteq G$ and any point $x \notin C$, there exist disjoint open sets $U \ni x$ and $V \supseteq C$. By Bredon's convention, "regular" is the $T_3$ axiom (sometimes called $T_{3.5}$ for *completely* regular). The full registry is on the topic page.

---

# Motivation

In point-set topology, one of the standard "separation axioms" is **regularity**: any point can be separated from any closed set not containing it, by disjoint open sets. Regular spaces are well-behaved: they have nice extension properties, continuous functions to $[0, 1]$ exist in abundance (when combined with second countability), and metrizability theorems (Urysohn) apply.

For general topological spaces, regularity is an *extra hypothesis*. For topological groups, it is *automatic*: every topological group is regular, with no additional assumption beyond the Hausdorff axiom in Bredon's definition. The reason is that the group structure provides a translation mechanism that, combined with symmetric neighborhoods of $e$, produces the separating open sets explicitly.

The proof is in two stages. First, reduce to the case of separating $e$ from a closed set $C$ not containing $e$ (using homogeneity / left translation). Second, use that the topology around $e$ has symmetric neighborhoods $V$ with $V^2 \subseteq U$ for any given $U$: choose $U = G \setminus C$ (open), pick a symmetric $V$ with $V^2 \subseteq U$; then $V$ and $CV$ (which is open as a union of translates) are disjoint, and $V$ separates $e$ from $C$.

This is the prototype "rigid topology from group structure" result.

---

# Statement

Every topological group is **regular**: for any closed set $C \subseteq G$ and any point $x \notin C$, there are disjoint open sets $U \ni x$ and $V \supseteq C$.

In fact, every topological group is **completely regular** (also called Tychonoff): for any closed $C$ and $x \notin C$, there is a continuous function $f : G \to [0, 1]$ with $f(x) = 0$ and $f|_C = 1$. (This stronger statement uses the existence of left-invariant pseudometrics from continuity of multiplication, but the regularity is sufficient for many applications.)

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is just "topological group" — joint continuity of multiplication, inversion, Hausdorff.

A disguised source: **a Hausdorff topological space with a continuous group action by homeomorphisms transitive on some "scaling" basis.** Property $B$: a homogeneous space with enough internal symmetry. The bridge: the same argument works for homogeneous spaces of topological groups (i.e., $G/H$ for $H$ closed in $G$). *Example:* spheres $S^{n-1} = \operatorname{O}(n)/\operatorname{O}(n-1)$, projective spaces, Grassmannians — all are regular Hausdorff spaces.

**Targets (Output Amplification)**

The conclusion "$G$ is regular" amplifies:

Combine with **second countability.** Property $D$: $G$ has a countable base. The amplified result $E$: $G$ is **normal** (Urysohn-style separation of any two disjoint closed sets), and by Urysohn's metrization theorem, $G$ is metrizable. *Example:* every second-countable topological group is metrizable. The Kakutani-Birkhoff theorem strengthens: any first-countable Hausdorff topological group is metrizable, by a left-invariant metric.

Combine with **local compactness.** Property $D$: $G$ is locally compact. The amplified result $E$: $G$ is **completely regular** by a direct argument (every closed set has a continuous Urysohn function separating it from a point), and admits a Haar measure (left-invariant Radon measure). Local compactness + regularity is the standard setting for Haar measure theory.

Combine with **path-connectedness and simple connectivity.** Property $D$: $G$ is connected and has trivial $\pi_1$. The amplified result $E$: covers and lifts of continuous functions exist; the simply-connected case is the universal cover.

---

# Why Is It True

The key insight is the existence of *symmetric neighborhoods with squared inclusion*. By continuity of multiplication at $(e, e)$ and [[Thm - Symmetric Neighborhoods Form a Basis at the Identity]], for any open neighborhood $U$ of $e$, there is a symmetric neighborhood $V$ of $e$ with $V \cdot V \subseteq U$, equivalently $V V^{-1} \subseteq U$ (since $V = V^{-1}$).

Now suppose we want to separate $e$ from a closed set $C$ not containing $e$. The set $U := G \setminus C$ is open and contains $e$. Choose symmetric $V$ with $V V \subseteq U$. We claim:

- $V$ is an open neighborhood of $e$.
- $C V$ is an open set containing $C$.
- $V \cap CV = \emptyset$.

The first two are clear ($V$ open by hypothesis; $CV = \bigcup_{c \in C} cV$, a union of opens, hence open; $C \subseteq CV$ since $e \in V$).

For disjointness: if $v \in V \cap CV$, then $v = cw$ for some $c \in C, w \in V$. So $c = vw^{-1} \in V \cdot V^{-1} = V \cdot V \subseteq U = G \setminus C$. Contradiction: $c \in C$ and $c \notin C$.

So $V$ and $CV$ are disjoint opens separating $e$ from $C$. By homogeneity ([[Thm - Translations are Homeomorphisms]]), translating $V$ to any other point gives the same result there.

The reason to expect this: the group structure gives an explicit "spread" mechanism. Any neighborhood of $e$ can be "thickened" into a neighborhood of any closed set $C$ via $CV$ — and this thickening is precisely controlled by the squaring estimate. The closed set $C$ has a "fattened" open thickening $CV$ that is small enough to avoid $V$ itself.

The proof generalizes: by using a sequence of nested symmetric neighborhoods $V_n$ with $V_{n+1}^2 \subseteq V_n$, one can build a continuous Urysohn function separating $\{e\}$ from $C$, giving complete regularity.

---

# What Makes This Hard

The non-obvious step is *recognizing the right squared estimate*: $V V^{-1} \subseteq U$ where $U = G \setminus C$. This is the squaring-and-shrinking trick combined with symmetry. The common error is to choose $V$ as a "naive" small neighborhood and try to separate directly; the squaring is what gives the *disjoint* open sets, not just any separating ones.

---

# Rederivation Scaffold

**High-level strategy:**
Reduce to separating $e$ from a closed set $C$ not containing $e$ (via translation). Use continuity of multiplication to find a symmetric neighborhood $V$ of $e$ with $V^2 \subseteq G \setminus C$. Then $V$ and $CV$ are disjoint opens separating $e$ from $C$.

**Subgoal decomposition:**

1. **Reduce to separating $e$ from a closed set.** Translate so $x = e$. By homogeneity, regularity at $e$ implies regularity everywhere.
   - *Hint:* Use $L_{x^{-1}}$.

2. **Choose squared-inclusion neighborhood.** Let $U = G \setminus C$ (open, contains $e$). By continuity of $\mu$ and symmetric basis, choose symmetric $V$ with $V V \subseteq U$.

3. **Show $V \cap CV = \emptyset$.** If $v \in V \cap CV$, then $v = cw$, $c = vw^{-1} \in V \cdot V^{-1} = V^2 \subseteq U = G \setminus C$, contradicting $c \in C$.

4. **Conclude.** $V$ open containing $e$, $CV$ open containing $C$, disjoint.

---

# Lemma Decomposition

> [!note]- Lemma 1: Continuity of $\mu$ gives squared-shrinking
> **Statement:** For any neighborhood $U$ of $e$, there is a neighborhood $W$ of $e$ with $W W \subseteq U$.
>
> **Hint:** Continuity of $\mu$ at $(e, e)$.
>
> **Why needed:** The basic shrinking lemma.
>
> > [!note]- Full proof
> > $\mu : G \times G \to G$ is continuous and $\mu(e, e) = e \in U$. So $\mu^{-1}(U)$ is an open neighborhood of $(e, e)$ in $G \times G$. By the product topology, this contains a basic open $W_1 \times W_2$. Set $W = W_1 \cap W_2$, an open neighborhood of $e$. Then $W \times W \subseteq W_1 \times W_2 \subseteq \mu^{-1}(U)$, i.e., $WW \subseteq U$.

> [!note]- Lemma 2: Symmetric variant of Lemma 1
> **Statement:** For any neighborhood $U$ of $e$, there is a *symmetric* neighborhood $V$ of $e$ with $V V \subseteq U$.
>
> **Hint:** Combine Lemma 1 with [[Thm - Symmetric Neighborhoods Form a Basis at the Identity]].
>
> **Why needed:** This is the actual neighborhood we use.
>
> > [!note]- Full proof
> > By Lemma 1, find $W$ with $W W \subseteq U$. By [[Thm - Symmetric Neighborhoods Form a Basis at the Identity]], there is a symmetric $V \subseteq W$. Then $V V \subseteq W W \subseteq U$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $C \subseteq G$ be closed and $x \notin C$. We want disjoint open sets separating $x$ from $C$.
>
> *Reduce to $x = e$.* Apply the homeomorphism $L_{x^{-1}}$ (left translation by $x^{-1}$). It sends $x$ to $e$ and $C$ to the closed set $x^{-1}C$, which does not contain $e$. If we can separate $e$ from $x^{-1}C$ by disjoint opens $V'$ and $W'$, then $L_x(V')$ and $L_x(W')$ separate $x$ from $C$. So we may assume $x = e$.
>
> *Construct the symmetric neighborhood.* $U := G \setminus C$ is open (since $C$ is closed) and contains $e$ (since $e \notin C$). By Lemma 2, choose a symmetric open neighborhood $V$ of $e$ with $V V \subseteq U$.
>
> *Construct the open thickening of $C$.* Set $W := CV = \bigcup_{c \in C} cV$. Each $cV = L_c(V)$ is open (translation is a homeomorphism — [[Thm - Translations are Homeomorphisms]]); $W$ is a union of opens, hence open. Also $C \subseteq W$ because $e \in V$, so $c = ce \in cV \subseteq W$.
>
> *Verify disjointness.* Suppose, for contradiction, that $V \cap W \neq \emptyset$. Then there is $v \in V$ and $c \in C$, $w \in V$ with $v = cw$. So $c = vw^{-1}$. Since $V$ is symmetric, $w^{-1} \in V$, so $c \in V \cdot V \subseteq U = G \setminus C$. So $c \notin C$. Contradiction.
>
> Hence $V$ and $W$ are disjoint opens with $e \in V$ and $C \subseteq W$. This is regularity at $e$. By homogeneity, regularity holds at every point. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Topological vector spaces are completely regular.** A topological vector space is a topological group $(V, +)$, hence regular by this theorem. With additional structure (locally convex topology), it is completely regular and admits a separation by continuous linear functionals (Hahn-Banach). The TVS proof closely parallels the topological group one.

**Lie groups are metrizable.** A Lie group is a topological group that is also a manifold. Manifolds are second-countable Hausdorff and locally Euclidean, hence first-countable. By the Kakutani-Birkhoff theorem, a first-countable Hausdorff topological group is metrizable by a left-invariant metric. This theorem (regularity) is the foundational separation result behind this.

**Quotient $G/H$ for $H$ closed is Hausdorff.** If $H \leq G$ is a closed subgroup, the quotient $G/H$ is Hausdorff (Proposition 15.11 in Bredon). The proof uses the symmetric neighborhood + closed subset technique here — separate two cosets by symmetric neighborhoods.

---

# Bridges

- **[[Def - Separation Axioms]]** — defines regularity and the other $T_i$ axioms.

- **[[Thm - Symmetric Neighborhoods Form a Basis at the Identity]]** — the essential tool for constructing the separating neighborhood.

- **[[Thm - Translations are Homeomorphisms]]** — homogeneity used to reduce to the case $x = e$.

---

# Unlocked by This

> [!tip] Complete Regularity / Tychonoff *(from Topology)*
> A space is **completely regular** (Tychonoff) if points can be separated from closed sets by continuous functions $G \to [0, 1]$. Every topological group is completely regular — a stronger statement than mere regularity, but provable by iterating the squared-symmetric construction.

> [!tip] Metrizability of Topological Groups *(from Topological Groups)*
> The **Kakutani-Birkhoff theorem**: every Hausdorff first-countable topological group is metrizable, by a left-invariant metric. The construction uses iterated symmetric neighborhoods to define the metric. Regularity is the foundational separation result.

> [!tip] Haar Measure Existence *(from Measure Theory)*
> The existence of a left-invariant Radon measure on a locally compact topological group depends on regularity: the measure of a closed set is defined via approximation by open sets, and the regularity ensures this approximation is well-defined.

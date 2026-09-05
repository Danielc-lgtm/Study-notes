---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Bump Function and Smooth Cutoff"
  - "Def - Support of a Function"
  - "Def - Partition of Unity on a Manifold"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold. $A \subseteq M$ is a closed subset; $U \subseteq M$ is an open set with $A \subseteq U$. A **smooth bump function for $A$ supported in $U$** is a smooth $\psi : M \to [0, 1]$ with $\psi \equiv 1$ on $A$ and $\operatorname{supp}(\psi) \subseteq U$. The standard one-sided germ is $\psi_0(t) = e^{-1/t}$ for $t > 0$ and $0$ otherwise. The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Statement

> **Theorem (Existence of Smooth Bump Functions).** Let $M$ be a smooth manifold. For any closed subset $A \subseteq M$ and any open set $U \supseteq A$, there exists a smooth function $\psi : M \to [0, 1]$ such that $\psi \equiv 1$ on $A$ and $\operatorname{supp}(\psi) \subseteq U$.

This is Lee Proposition 2.25.

---

# Motivation

The motivating question: how rigid is the structure of $C^\infty(M)$? Real-analytic functions are extremely rigid — a real-analytic function on a connected manifold that vanishes on a nonempty open set must vanish identically. Could the same hold for smooth functions? The answer is dramatically *no*: smooth functions can be tailored to vanish exactly where we want and equal $1$ exactly where we want, with smooth interpolation in between.

This is the *softness* property of $C^\infty(M)$, and the theorem makes it precise. Given any two regions of $M$ — a "fully on" region $A$ and a "fully off" region $M \setminus U$ — there is a smooth function realizing this pattern. The interpolation between the two regions happens smoothly, with values in $(0, 1)$, in the buffer zone $U \setminus A$.

The theorem is the **smooth-category upgrade of Urysohn's lemma**. Urysohn says: in a normal topological space, any two disjoint closed sets can be separated by a continuous function. Smooth manifolds are paracompact Hausdorff, hence normal, so Urysohn applies and produces continuous separators. The bump-function theorem upgrades the continuity to smoothness — replacing the "rational interpolation" of Urysohn's bare-handed construction with a $\psi_0$-based smooth interpolation.

The proof uses (a baby version of) partitions of unity: cover $M$ by $U$ and $M \setminus A$, take a smooth partition of unity $\{\psi_0, \psi_1\}$ subordinate to this cover, and take $\psi_0$ — the one supported in $U$. By the partition-of-unity axiom $\psi_0 + \psi_1 = 1$, and the fact that $\psi_1 = 0$ on $A$ (since $\operatorname{supp}(\psi_1) \subseteq M \setminus A$, which is disjoint from $A$), we get $\psi_0 \equiv 1$ on $A$. The conditions on a bump function are satisfied.

This is therefore a *corollary* of [[Thm - Existence of Smooth Partitions of Unity]] — but it is so frequently used that it gets its own theorem statement, and in fact the partition-of-unity theorem can be proved with bump functions as a separate input (the order of theorems is up to taste). We follow Lee's order: partitions of unity first, bump functions as a corollary.

The bump-function theorem has many applications, often more direct than appealing to the full partition-of-unity machinery. Bump functions are used to *localize* global problems, to *extend* functions defined on closed subsets ([[Thm - Smooth Extension Lemma]]), and to *truncate* unbounded functions to compactly-supported ones. The theorem licenses the constant phrase "let $\psi$ be a smooth bump function equal to $1$ on $K$ and supported in a neighbourhood of $K$" — used in every chapter of every textbook on smooth manifolds.

The smooth-vs-analytic gap is essential here. The theorem fails in the analytic category — there are no nonzero compactly supported analytic functions on a connected noncompact analytic manifold, so analytic analogues of these arbitrary-support constructions fail. This is why smooth manifold theory is so much "softer" and more flexible than complex analytic or algebraic geometry, and why so many constructions that work for smooth manifolds (gluing local data, deforming, perturbing) fail in the analytic / algebraic settings.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem requires only that $A$ be closed and $U$ open. The skill is recognizing when this hypothesis is met.

The first source is **a compact set $K \subseteq M$**. Property $B$: $K$ is compact. The bridge: compact subsets of Hausdorff spaces are closed, so $K$ is closed. *Example:* a coordinate ball $\overline{B(0, 1)}$ pulled back through a chart is compact (image of compact under homeomorphism), hence closed, hence eligible for a bump.

The second source is **the closure of any subset**. Property $B$: $A = \overline S$ for some $S \subseteq M$. The bridge: closures are closed by definition. *Example:* the support of a function is the closure of the non-vanishing set, hence eligible.

The third source is **a level set of a continuous function**. Property $B$: $A = f^{-1}(\{0\})$ for some continuous $f : M \to \mathbb{R}$. The bridge: $\{0\}$ is closed in $\mathbb{R}$, preimages of closed sets under continuous maps are closed. *Example:* the unit sphere $S^n = \{|x| = 1\} \subseteq \mathbb{R}^{n+1}$ is the level set of the continuous function $|x| - 1$, hence closed, hence eligible for bumps.

The fourth source is **the boundary of a manifold-with-boundary**. Property $B$: $A = \partial M$ where $M$ is a manifold-with-boundary. The bridge: the boundary is a closed submanifold. *Example:* useful in constructing bump functions vanishing on the boundary, for integration / Stokes' theorem arguments.

**Targets (Output Amplification)**

The conclusion produces a smooth function $\psi$ with $\psi = 1$ on $A$ and $\operatorname{supp}(\psi) \subseteq U$.

Combine the conclusion with **a globally defined smooth function $g$ on $M$**. Property $D$: $g \in C^\infty(M)$. The amplified result $E$: the product $\psi g$ is a smooth function on $M$ that agrees with $g$ on $A$ and is supported in $U$. The combination is useful because it converts a globally-defined smooth function into a "localized" version of itself, with prescribed support. *Example:* to test a global hypothesis on small sets, multiply by a bump for the small set — the resulting product has the global smoothness and the local prescribed-support behaviour.

Combine the conclusion with **a smooth function $f$ defined on a neighbourhood of $A$**. Property $D$: $f$ is smooth on some open $W$ containing $A$. The amplified result $E$: the function $\widetilde f = \psi f$ (extended by zero outside $W$) is a smooth function on all of $M$, agreeing with $f$ on $A$, supported in $U$ (provided $U \subseteq W$). The combination is the seed of the [[Thm - Smooth Extension Lemma|smooth extension lemma]]. *Example:* extend a smooth function from a coordinate chart to all of $M$ via multiplication by a chart-bump.

Combine the conclusion with **a $C^\infty(M)$-module structure**. Property $D$: a smooth vector field $X$ or a smooth section $\sigma$ of a vector bundle. The amplified result $E$: $\psi X$ or $\psi \sigma$ is a smooth section, agreeing with $X$ / $\sigma$ on $A$, supported in $U$. The combination produces *compactly supported* sections, the standard tool in approximating global sections and in defining inner products on section spaces. *Example:* every smooth vector field on a non-compact manifold can be modified to a compactly supported vector field with the same restriction to any given compact set, by multiplying with a bump function for that compact set.

Combine the conclusion with **a smooth partition of unity** subordinate to a cover. Property $D$: a smooth partition of unity $\{\psi_\alpha\}$ for some cover $\{U_\alpha\}$. The amplified result $E$: any function defined globally can be written as $f = \sum_\alpha \psi_\alpha f$, with each $\psi_\alpha f$ supported in $U_\alpha$. The bump functions are the atomic case ($\{U_\alpha, M \setminus A\}$), and partition-of-unity decompositions are systematic versions of this. *Example:* the decomposition of a smooth function into "chart-local pieces" used in integration theory.

---

# Why Is It True

The intuition: cover $M$ by $U$ and $M \setminus A$, take a partition of unity, retain the function supported in $U$.

**The mechanism in one line: a bump function for $A$ supported in $U$ is just the $U$-component of a partition of unity subordinate to $\{U, M \setminus A\}$.**

The cover $\{U, M \setminus A\}$ is an open cover of $M$: their union is $U \cup (M \setminus A) = M$ since $A \subseteq U$. The partition-of-unity theorem produces smooth $\{\psi, \widetilde \psi\}$ with $\operatorname{supp}(\psi) \subseteq U$, $\operatorname{supp}(\widetilde\psi) \subseteq M \setminus A$, and $\psi + \widetilde \psi = 1$ on $M$.

Now on $A$, $\widetilde \psi(p) = 0$ for every $p \in A$ — because $\operatorname{supp}(\widetilde \psi) \subseteq M \setminus A$, which is disjoint from $A$. So $\psi(p) = 1 - \widetilde \psi(p) = 1$ for every $p \in A$.

The required properties of a bump function are met: smooth (by the partition), takes values in $[0, 1]$ (by the partition), equals $1$ on $A$ (just shown), supported in $U$ (by the partition's subordination).

Conceptually, the bump function is the *indicator* of $A$ smoothed out within $U$. The smoothing is what the partition-of-unity refinement provides, and the partition's $\psi_0$-based bump construction is what produces the smooth interpolation in the buffer zone $U \setminus A$.

---

# What Makes This Hard

The proof, given the existence of smooth partitions of unity, is one paragraph. The depth is in the *partition-of-unity theorem itself* — the construction of smooth bumps on $\mathbb{R}^n$ from the $\psi_0$-trick, the patching of cover elements via paracompactness, the normalization. Once those are in place, the bump-function theorem is essentially trivial. The most common error in proving the bump-function theorem from scratch (without invoking partitions of unity) is to forget the chart-by-chart construction of the smooth bumps; absent the $\psi_0$-trick, the smoothness is unachievable.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Cover $M$ by $U$ and $M \setminus A$, apply the smooth partition of unity theorem, and take the function supported in $U$.

**Subgoal decomposition:**

1. **The pair $\{U, M \setminus A\}$ is an open cover of $M$.** Since $A \subseteq U$, $M \setminus A \supseteq M \setminus U$, so $U \cup (M \setminus A) = M$. Both are open ($U$ open by hypothesis, $M \setminus A$ open since $A$ closed).
   - *Hint:* Direct verification.
   - *Why needed:* Establishes that the partition-of-unity theorem is applicable.

2. **Apply the smooth partition of unity theorem.** [[Thm - Existence of Smooth Partitions of Unity]] gives smooth $\{\psi, \widetilde \psi\}$ with $\operatorname{supp}(\psi) \subseteq U$, $\operatorname{supp}(\widetilde \psi) \subseteq M \setminus A$, $\psi + \widetilde \psi = 1$, both in $[0, 1]$.
   - *Hint:* The standard application — partition of unity for the cover $\{U, M \setminus A\}$.
   - *Why needed:* Produces the candidate bump function $\psi$.

3. **Verify $\psi \equiv 1$ on $A$.** On $A$, $\widetilde \psi = 0$ (since $A \cap \operatorname{supp}(\widetilde \psi) \subseteq A \cap (M \setminus A) = \emptyset$), so $\psi = 1 - \widetilde \psi = 1$.
   - *Hint:* Use the support condition on $\widetilde \psi$.
   - *Why needed:* This is the bump-function condition that the partition doesn't directly guarantee.

4. **Verify $\operatorname{supp}(\psi) \subseteq U$.** This is exactly the partition-of-unity subordination.
   - *Why needed:* Bump-function condition.

---

# Lemma Decomposition

> [!note]- Lemma 1: The pair $\{U, M \setminus A\}$ is an open cover of $M$
> **Statement:** Let $A \subseteq U \subseteq M$ with $A$ closed and $U$ open in $M$. Then $\{U, M \setminus A\}$ is an open cover of $M$.
>
> **Hint:** Both sets are open by hypothesis. Their union covers $M$ because $A \subseteq U$ means any point of $M$ is either in $A$ (hence in $U$) or in $M \setminus A$.
>
> **Why needed:** The partition-of-unity theorem operates on open covers, so we need to express our setup as such a cover.
>
> > [!note]- Full proof
> > *Open:* $U$ is open by hypothesis. $M \setminus A$ is open because $A$ is closed.
> >
> > *Covering:* let $p \in M$. Either $p \in A$, in which case $p \in U$ (since $A \subseteq U$); or $p \notin A$, in which case $p \in M \setminus A$. Either way, $p$ is in the union $U \cup (M \setminus A)$, so the pair covers $M$.

> [!note]- Lemma 2: A function whose support is disjoint from $A$ vanishes on $A$
> **Statement:** Let $f : M \to \mathbb{R}$ be a function with $\operatorname{supp}(f) \subseteq M \setminus A$. Then $f(p) = 0$ for every $p \in A$.
>
> **Hint:** If $p \in A$, then $p \notin \operatorname{supp}(f)$, so $p$ has a neighbourhood disjoint from $\operatorname{supp}(f)$, hence disjoint from $\{f \neq 0\}$ (a subset of the support). On this neighbourhood, $f$ is identically zero, hence $f(p) = 0$.
>
> **Why needed:** Applied to $f = \widetilde \psi$ to conclude $\widetilde \psi \equiv 0$ on $A$, hence $\psi \equiv 1$ on $A$.
>
> > [!note]- Full proof
> > Suppose $p \in A$, so $p \notin M \setminus A$. Since $\operatorname{supp}(f) \subseteq M \setminus A$ and supports are closed, $p$ has an open neighbourhood $W$ disjoint from $\operatorname{supp}(f)$.
> >
> > By the definition of support, $\operatorname{supp}(f) = \overline{\{f \neq 0\}}$. The disjointness $W \cap \operatorname{supp}(f) = \emptyset$ means $W \cap \{f \neq 0\} = \emptyset$ (since $\{f \neq 0\} \subseteq \operatorname{supp}(f)$), so $f \equiv 0$ on $W$. In particular $f(p) = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a smooth manifold, $A \subseteq M$ closed, $U \subseteq M$ open with $A \subseteq U$.
>
> *Step 1: open cover.* By Lemma 1, $\{U, M \setminus A\}$ is an open cover of $M$.
>
> *Step 2: partition of unity.* By [[Thm - Existence of Smooth Partitions of Unity]], there exists a smooth partition of unity $\{\psi, \widetilde \psi\}$ subordinate to this cover: $\psi, \widetilde \psi : M \to [0, 1]$ are smooth, $\operatorname{supp}(\psi) \subseteq U$, $\operatorname{supp}(\widetilde \psi) \subseteq M \setminus A$, the supports are locally finite (here automatic, since there are only two), and $\psi(p) + \widetilde \psi(p) = 1$ for every $p \in M$.
>
> *Step 3: $\psi \equiv 1$ on $A$.* For any $p \in A$, by Lemma 2 applied to $\widetilde \psi$, $\widetilde \psi(p) = 0$. Therefore $\psi(p) = 1 - \widetilde \psi(p) = 1$.
>
> *Step 4: $\operatorname{supp}(\psi) \subseteq U$.* This is the partition-of-unity subordination.
>
> *Step 5: $0 \leq \psi(p) \leq 1$.* This is the partition-of-unity range condition.
>
> Therefore $\psi$ is a smooth bump function for $A$ supported in $U$. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Distribution theory: existence of test functions with prescribed properties.** In distribution theory on $\mathbb{R}^n$, test functions are compactly supported smooth functions, and the existence theorem gives test functions equal to $1$ on a prescribed compact set and supported in a slightly larger one. This is the source for the standard technique of *cutoff arguments* in PDE: to localize an estimate to a compact set $K$, multiply by a bump function for $K$ and argue on the supports. The bump-function theorem is the foundation.

**Differential topology: any closed set is the zero set of a smooth function.** Lee Theorem 2.29 states that for any closed $K \subseteq M$, there is a smooth $f : M \to [0, \infty)$ with $f^{-1}(0) = K$. The proof builds bumps $\rho_i$ on a countable open cover of $M \setminus K$ (using the bump-function theorem at each step), then sums them with shrinking weights. This is a remarkable rigidity-vs-flexibility statement: closed sets in smooth manifolds are *exactly* the zero sets of smooth nonnegative functions. The analytic analogue is dramatically false (zero sets of real-analytic functions are *highly* restricted).

**Symplectic geometry: cutting off symplectic forms.** A symplectic form is a closed, non-degenerate $2$-form on a manifold. To construct a global symplectic form, one often takes local symplectic forms in Darboux charts and weights them by bump functions — but the non-degeneracy is *not* preserved under convex combinations, so the construction is delicate. Bump functions are the seed of the construction but the gluing requires more careful symplectic linear algebra. See **Symplectic Geometry** (downstream).

---

# Bridges

- **[[Def - Bump Function and Smooth Cutoff]]** — the object being constructed. The theorem says these objects exist on every smooth manifold for every (closed, open) pair.

- **[[Thm - Existence of Smooth Partitions of Unity]]** — the main input. The bump-function theorem follows by applying the partition-of-unity theorem to the cover $\{U, M \setminus A\}$.

- **[[Thm - Smooth Extension Lemma]]** — the main application. The extension lemma uses bump functions to extend a smooth function from a closed set to the whole manifold.

- **[[Thm - Urysohn's Lemma]]** — the topological analogue. Urysohn's lemma produces continuous separators on normal spaces; the bump-function theorem produces smooth ones on smooth manifolds. The two theorems have isomorphic structure, with the topological "continuous Urysohn-style bump" replaced by the smooth "$\psi_0$-based bump".

- **The smooth-vs-analytic distinction** — on a connected real-analytic or complex manifold, there are no nonzero compactly supported analytic functions unless the relevant connected component is compact: vanishing on a nonempty open set forces vanishing on that component. This is the defining flexibility-vs-rigidity distinction between smooth and analytic categories, and the bump-function theorem is the existence statement that licenses the flexibility.

---

# Unlocked by This

> [!tip] Smooth Extension Lemma *(within Differential Geometry II)*
> Any smooth function on a closed subset $A \subseteq M$ extends smoothly to all of $M$, with support inside any prescribed open $U \supseteq A$. The construction uses one bump function per neighbourhood-extension of $f$, summed via a partition of unity. See [[Thm - Smooth Extension Lemma]].

> [!tip] Existence of Compactly Supported Smooth Sections *(from Differential Geometry)*
> Any smooth section of a vector bundle on a non-compact manifold can be modified to a compactly supported section with the same restriction to any prescribed compact set, by multiplication with a bump function. This is the technical mechanism by which the global space of smooth sections is dense (in a suitable topology) in the larger spaces relevant for analysis on manifolds. See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|DG VI]].

> [!tip] Localized Operators in PDE *(from Microlocal Analysis)*
> Pseudo-differential operators and Fourier integral operators on a manifold are defined via partitions of unity: each chart hosts a local symbol, the global operator is $\sum_\alpha \psi_\alpha P_\alpha \psi_\alpha$ for chart-localized operators $P_\alpha$ and a partition of unity $\{\psi_\alpha\}$. The bump-function theorem is what gives access to the $\psi_\alpha$'s.

> [!tip] Closed Sets are Zero Sets of Smooth Functions *(from Differential Topology)*
> Every closed $K \subseteq M$ is the zero set of some smooth $f : M \to [0, \infty)$, with $f^{-1}(0) = K$ exactly. The construction sums bumps over the countably many balls in a refinement of $M \setminus K$. This is Lee Theorem 2.29.

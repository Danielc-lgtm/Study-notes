---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Function on a Manifold"
  - "Def - Support of a Function"
  - "Def - Partition of Unity on a Manifold"
  - "Def - Bump Function and Smooth Cutoff"
  - "Thm - Existence of Smooth Partitions of Unity"
  - "Thm - Existence of Smooth Bump Functions"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold, $A \subseteq M$ a closed subset, $U \subseteq M$ an open set containing $A$. A function $f : A \to \mathbb{R}^k$ is **smooth on $A$** (in the sense relevant here) if every point $p \in A$ has an open neighbourhood $W_p \subseteq M$ and a smooth function $\widetilde f_p : W_p \to \mathbb{R}^k$ such that $\widetilde f_p|_{W_p \cap A} = f|_{W_p \cap A}$. That is, $f$ extends locally to a smooth function. The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Statement

> **Theorem (Smooth Extension Lemma).** Let $M$ be a smooth manifold (with or without boundary), $A \subseteq M$ a closed subset, and $f : A \to \mathbb{R}^k$ a smooth function (in the sense of admitting a smooth extension in a neighbourhood of each point of $A$). For any open set $U \supseteq A$, there exists a smooth function $\widetilde f : M \to \mathbb{R}^k$ such that
>
> 1. $\widetilde f|_A = f$;
> 2. $\operatorname{supp}(\widetilde f) \subseteq U$.

This is Lee Lemma 2.26. The codomain $\mathbb{R}^k$ is essential — see the remark in the Sources section about why extension fails for general codomains.

---

# Motivation

The motivating question: when does a function defined on a closed subset extend to the whole manifold? The Tietze extension theorem in topology says yes for continuous real-valued functions on normal spaces. The smooth-category upgrade is the natural next question. The Tietze proof produces a continuous extension via sup-of-approximations — but the construction is not smooth, so we need a different approach.

The answer is exactly what one expects: cover $A$ by neighbourhoods on which $f$ extends, add the complement $M \setminus A$ as a "buffer", take a smooth partition of unity, weight each local extension by the partition function, sum. The result is global, smooth, agrees with $f$ on $A$, and has support inside the prescribed open set $U$. The construction is the canonical partition-of-unity argument applied to extension data.

The theorem is *the* smooth-category extension theorem. It is used constantly throughout differential geometry whenever a smooth construction defined on a closed subset (a coordinate ball, a compact submanifold, a single chart) needs to be treated as a global object. *Pattern: every "extend this from a local situation to a global one" argument in smooth manifold theory routes through this lemma or an equivalent.*

The smooth extension lemma is the smooth-category analogue of two topological theorems: the **Tietze extension theorem** (continuous extension from closed subsets) and (via the bridge to topological partition of unity) of the gluing of continuous local sections on closed covers. Both topological theorems hold on normal spaces; the smooth lemma holds on smooth manifolds. The proof is parallel: instead of using Urysohn's lemma to build continuous bumps, use the $\psi_0$-trick to build smooth bumps; instead of summing continuous separators, sum smooth ones via a smooth partition of unity.

A subtle but important point: the theorem applies to *vector-valued* functions $f : A \to \mathbb{R}^k$, not to functions $f : A \to N$ for a general target manifold $N$. The reason is that the proof sums local extensions weighted by partition-of-unity weights, and *sums in $\mathbb{R}^k$* are well-defined while *sums in a general manifold* are not. For target manifolds that are not vector spaces, extension can fail purely topologically: the identity map $S^1 \to S^1$ is smooth but does not extend continuously to $\mathbb{R}^2 \to S^1$ (no continuous extension exists, by topological obstruction). The smooth extension is more delicate, and Lee handles it separately in later chapters (Corollary 6.27: smooth extension exists iff continuous extension exists, for target a smooth manifold).

A reader is assumed to be comfortable with the partition-of-unity construction and to have a grasp of the support condition (closure of non-vanishing set).

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem requires only that $A$ be closed and $f$ smooth-on-$A$ in the local-extension sense. The skill is recognizing when extension data is available.

The first source is **a smooth function defined on a compact set $K \subseteq M$**. Property $B$: $K$ is compact and $f : K \to \mathbb{R}^k$ is smooth (extends smoothly to a neighbourhood of each point). The bridge: compact sets in Hausdorff spaces are closed; the theorem applies, yielding a smooth extension supported in any prescribed open neighbourhood. *Example:* a smooth function on a compact submanifold (e.g., a smooth function on $S^2 \subseteq \mathbb{R}^3$) extends to a smooth function on $\mathbb{R}^3$.

The second source is **a smooth function defined in a chart**. Property $B$: $f$ is smooth on a chart $(U, \varphi)$, given by smooth coordinate representation $\widehat f : \varphi(U) \to \mathbb{R}^k$. The bridge: $f$ defines a smooth function on $U$ (open, but its closure $\overline U$ is closed); extension applies to $A = \overline U$ if we want to keep the values on $\overline U$, or simply multiply by a bump function for $U$. *Example:* the typical "extend a chart-local construction to a global construction" — done by multiplying by a chart bump, but the extension lemma can also be invoked when the bump-multiplication does not directly produce the global object.

The third source is **a smooth function defined on a sub-cover of $A$**. Property $B$: $A$ is covered by open sets $W_p$ for $p \in A$, with smooth functions $\widetilde f_p$ on each $W_p$ that agree on $A \cap W_p \cap W_q$ (the part of $A$ in the overlaps). The bridge: this is the local-extension hypothesis of the theorem, in the form most amenable to verification. *Example:* a smooth function defined chart-by-chart on a closed subset, consistent on overlaps within $A$, extends globally.

**Targets (Output Amplification)**

The conclusion provides a global smooth $\widetilde f$ extending $f$ with prescribed support.

Combine the conclusion with **multiplication by an arbitrary smooth function $g \in C^\infty(M)$**. Property $D$: a smooth $g$ on $M$. The amplified result $E$: $g \widetilde f$ is a smooth function on $M$ with support inside $\operatorname{supp}(g) \cap \operatorname{supp}(\widetilde f) \subseteq \operatorname{supp}(g) \cap U$, agreeing with $gf$ on $A$. This combination is useful when we want to extend $f$ from $A$ but modulate the extension to vanish in some region. *Example:* extend $f$ from a compact $K$, then multiply by a bump to localize.

Combine the conclusion with **integration on a manifold with boundary**. Property $D$: $M$ has a boundary, and a smooth function on the boundary $\partial M$ needs to be extended to a global function for integration. The amplified result $E$: the global extension allows integration of the boundary's data against test forms, giving a meaningful boundary-data formulation. *Example:* in the proof of Stokes' theorem, smooth functions on the boundary are extended to compactly-supported functions on the manifold for the divergence-theorem calculation.

Combine the conclusion with **a smooth-vector-bundle structure**. Property $D$: $f$ is a smooth section of a vector bundle $E \to M$ defined on a closed subset $A$. The amplified result $E$: $f$ extends to a global smooth section of $E$, supported in any prescribed open $U \supseteq A$. *Example:* the extension lemma for vector-valued maps generalizes to bundle sections by applying it in local trivializations and using partition of unity to glue. This is the foundational result for the existence of global sections "extending" local ones.

---

# Why Is It True

The intuition: cover $A$ by open sets on which $f$ extends smoothly, add the open $M \setminus A$ to make a cover of $M$, take a smooth partition of unity, sum the local extensions weighted by the partition.

**The mechanism in one line: a global smooth extension is the partition-of-unity-weighted sum of local smooth extensions.**

The key observation is that each local extension $\widetilde f_p$ on $W_p$ is "right" on the part of $A$ inside $W_p$ — it equals $f$ there. Different local extensions $\widetilde f_p$ and $\widetilde f_q$ may *disagree* on $W_p \cap W_q \setminus A$ (where $f$ does not constrain them), but they *agree* on $W_p \cap W_q \cap A$. So the issue is only the "off-$A$" disagreement, and the partition of unity blends this away — at points off $A$, the weighting still produces a smooth function (smoothness is preserved by convex combinations of smooth functions), but the resulting values are some weighted average of the off-$A$ extensions, which is fine since $f$ is not defined off $A$ anyway.

On $A$ itself, all local extensions $\widetilde f_p$ agree with $f$, so the weighted sum at any $p \in A$ is:
$$\widetilde f(p) = \sum_q \psi_q(p) \widetilde f_q(p) = \sum_q \psi_q(p) f(p) = \left(\sum_q \psi_q(p)\right) f(p) = 1 \cdot f(p) = f(p).$$
The extension property is automatic from the partition-of-unity normalization. (Here we use $\psi_0$ for the partition's component supported in $M \setminus A$ — which vanishes on $A$ — and $\psi_q$ for the components supported in the $W_q$'s.)

So the construction is "natural in the partition-of-unity sense": the weights take care of the disagreement off $A$, the partition-sum-to-$1$ property takes care of the agreement on $A$. The clean fact is that the partition of unity is set up *specifically* to make this work.

---

# What Makes This Hard

The proof is conceptually simple once partitions of unity are available. The non-obvious step is realizing that *the off-$A$ disagreement is not a problem* — different local extensions disagree there, but the partition-of-unity weighting blends them into a smooth global function, and the values are not constrained off $A$. Most students try to construct *one* extension that is "right" everywhere, which is unnecessary: the construction only needs $\widetilde f|_A = f$, and that is automatic from the partition normalization regardless of how local extensions disagree off $A$.

The most common technical error is to forget the buffer set $M \setminus A$ in the cover. Without it, the partition of unity is only subordinate to the open sets $W_p$ that *cover $A$*, not all of $M$. Adding $M \setminus A$ extends the cover to all of $M$ and assigns the points off $A$ a weight (via $\psi_0$ supported in $M \setminus A$), and the sum-to-$1$ becomes valid. The buffer is essential.

Another common error is to confuse "support of the extension is in $U$" with "support of the extension is in $\overline U$". The closure can in principle escape $U$ if $\overline U \not\subseteq U$ (which happens when $U$ is not regular), but with our standard topology assumptions (manifolds are normal) and the buffer-set construction, the support is in the union of the bumped-up neighbourhoods of $A$ which is inside $U$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Cover $A$ by sets on which $f$ extends smoothly. Add $M \setminus A$ to make a cover of $M$. Take a smooth partition of unity. Weight each local extension by its partition function and sum.

**Subgoal decomposition:**

1. **Construct local extensions.** For each $p \in A$, the hypothesis gives an open $W_p \subseteq M$ and a smooth $\widetilde f_p : W_p \to \mathbb{R}^k$ with $\widetilde f_p|_{W_p \cap A} = f|_{W_p \cap A}$. By replacing $W_p$ with $W_p \cap U$ if needed, we may assume $W_p \subseteq U$.
   - *Hint:* Direct use of the local-extension hypothesis.
   - *Why needed:* Provides the local data to be glued.

2. **Form an open cover of $M$.** The collection $\{W_p : p \in A\} \cup \{M \setminus A\}$ is an open cover.
   - *Hint:* The union covers $M$: points in $A$ are in some $W_p$, points not in $A$ are in $M \setminus A$.
   - *Why needed:* The partition-of-unity theorem operates on open covers of $M$.

3. **Take a partition of unity.** By [[Thm - Existence of Smooth Partitions of Unity]], there exists a smooth partition of unity $\{\psi_p\}_{p \in A} \cup \{\psi_0\}$ subordinate to this cover, with $\operatorname{supp}(\psi_p) \subseteq W_p$ and $\operatorname{supp}(\psi_0) \subseteq M \setminus A$, and $\psi_0 + \sum_p \psi_p = 1$ on $M$.
   - *Hint:* Standard application.
   - *Why needed:* Provides the smooth weights.

4. **Form the weighted sum.** Define $\widetilde f : M \to \mathbb{R}^k$ by $\widetilde f(q) = \sum_{p \in A} \psi_p(q) \widetilde f_p(q)$, where each summand $\psi_p \widetilde f_p$ is extended by zero outside $W_p$ (since $\psi_p \to 0$ at the boundary of its support inside $W_p$). By local finiteness, this is a finite sum at each point, hence smooth.
   - *Hint:* Each $\psi_p \widetilde f_p$ is well-defined globally because $\psi_p = 0$ outside $\operatorname{supp}(\psi_p) \subseteq W_p$.
   - *Why needed:* Produces the candidate extension.

5. **Verify $\widetilde f|_A = f$.** For $q \in A$, $\psi_0(q) = 0$ (since $A \cap \operatorname{supp}(\psi_0) \subseteq A \cap (M \setminus A) = \emptyset$), so $\sum_p \psi_p(q) = 1$. Each $\widetilde f_p(q)$ equals $f(q)$ when $q \in W_p \cap A$ (the only $p$ with $\psi_p(q) \neq 0$ are those with $q \in W_p$, and on $W_p \cap A$, $\widetilde f_p = f$). So $\widetilde f(q) = \sum_p \psi_p(q) f(q) = f(q) \sum_p \psi_p(q) = f(q) \cdot 1 = f(q)$.
   - *Hint:* Use the agreement of $\widetilde f_p$ with $f$ on $W_p \cap A$ and the sum-to-$1$ property.
   - *Why needed:* This is the extension condition.

6. **Verify $\operatorname{supp}(\widetilde f) \subseteq U$.** $\widetilde f$ is the sum of $\psi_p \widetilde f_p$, each supported in $W_p \subseteq U$. So $\operatorname{supp}(\widetilde f) \subseteq \bigcup_p \overline{W_p} \subseteq \overline U$ (or actually $\subseteq U$ when $U$ is suitably chosen; in standard cases with $W_p \subseteq U$, the support is in $\overline{\bigcup W_p}$, which is closed and contained in $\overline U$).
   - *Hint:* Use the partition of unity's subordination.
   - *Why needed:* Support condition of the lemma.

---

# Lemma Decomposition

> [!note]- Lemma 1: Local extensions of a smooth function on a closed set
> **Statement:** Let $f : A \to \mathbb{R}^k$ be smooth on $A$ (in the local-extension sense). Then there exists an open cover $\{W_p\}_{p \in A}$ of $A$ in $M$ and smooth functions $\widetilde f_p : W_p \to \mathbb{R}^k$ with $\widetilde f_p|_{W_p \cap A} = f|_{W_p \cap A}$.
>
> **Hint:** This is just the local-extension hypothesis written out. For each $p \in A$, the smoothness of $f$ at $p$ gives an open neighbourhood $W_p$ and a smooth extension $\widetilde f_p$ on it.
>
> **Why needed:** The local data to be assembled.
>
> > [!note]- Full proof
> > By the hypothesis "$f$ is smooth on $A$" (in the local-extension sense), each $p \in A$ has an open neighbourhood $W_p$ and a smooth $\widetilde f_p : W_p \to \mathbb{R}^k$ with $\widetilde f_p|_{W_p \cap A} = f|_{W_p \cap A}$. The collection $\{W_p\}_{p \in A}$ is an open cover of $A$ in $M$.

> [!note]- Lemma 2: $\psi_p \widetilde f_p$ extends smoothly by zero outside $\operatorname{supp}(\psi_p)$
> **Statement:** Let $\psi_p \in C^\infty(M)$ with $\operatorname{supp}(\psi_p) \subseteq W_p$, and let $\widetilde f_p \in C^\infty(W_p)$. Define $h_p : M \to \mathbb{R}^k$ by $h_p = \psi_p \widetilde f_p$ on $W_p$ and $h_p = 0$ on $M \setminus \operatorname{supp}(\psi_p)$. Then $h_p \in C^\infty(M)$.
>
> **Hint:** The two definitions agree on the overlap $W_p \setminus \operatorname{supp}(\psi_p)$ (where $\psi_p = 0$, so $\psi_p \widetilde f_p = 0$ on both sides). Smoothness on each definition's domain is clear; smoothness at the seam follows from agreement of the two definitions on a neighbourhood of each seam point.
>
> **Why needed:** Lets us globally define $\psi_p \widetilde f_p$ on $M$, even though $\widetilde f_p$ is only defined on $W_p$.
>
> > [!note]- Full proof
> > On $W_p$: $h_p = \psi_p \widetilde f_p$, a product of smooth functions, hence smooth.
> >
> > On $M \setminus \operatorname{supp}(\psi_p)$: $h_p \equiv 0$, hence smooth.
> >
> > On the overlap $W_p \setminus \operatorname{supp}(\psi_p)$: $\psi_p = 0$ (since $\operatorname{supp}(\psi_p)$ is the closure of $\{\psi_p \neq 0\}$, so outside the support, $\psi_p = 0$), so $\psi_p \widetilde f_p = 0 = h_p$ from the other definition. Hence the two definitions agree, and $h_p$ is well-defined.
> >
> > Smoothness at any point $q$ in the overlap: $q$ has a neighbourhood inside $W_p \setminus \operatorname{supp}(\psi_p)$ (open) on which both definitions are zero — smooth. $q$ also has a neighbourhood inside $W_p$ on which $h_p = \psi_p \widetilde f_p$ — smooth. The two agree, so $h_p$ is smooth at $q$.
> >
> > Globally: smoothness at every point implies smoothness on $M$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a smooth manifold, $A \subseteq M$ closed, $f : A \to \mathbb{R}^k$ smooth on $A$ (in the local-extension sense), $U \subseteq M$ open with $A \subseteq U$.
>
> *Step 1: local extensions.* By Lemma 1, for each $p \in A$ there is an open $W_p \subseteq M$ with $p \in W_p$ and a smooth $\widetilde f_p : W_p \to \mathbb{R}^k$ with $\widetilde f_p|_{W_p \cap A} = f|_{W_p \cap A}$. Replace $W_p$ by $W_p \cap U$ to ensure $W_p \subseteq U$; the local extension still holds on the smaller set.
>
> *Step 2: open cover of $M$.* The collection $\mathcal{W} = \{W_p\}_{p \in A} \cup \{M \setminus A\}$ is an open cover of $M$: each $W_p$ is open in $M$, $M \setminus A$ is open ($A$ closed), and the union covers $M$ since every $q \in M$ either lies in $A$ (then $q \in W_q$) or in $M \setminus A$.
>
> *Step 3: smooth partition of unity.* By [[Thm - Existence of Smooth Partitions of Unity]], there is a smooth partition of unity $\{\psi_p\}_{p \in A} \cup \{\psi_0\}$ subordinate to $\mathcal{W}$: $\operatorname{supp}(\psi_p) \subseteq W_p$, $\operatorname{supp}(\psi_0) \subseteq M \setminus A$, supports locally finite, and $\psi_0 + \sum_p \psi_p = 1$ on $M$.
>
> *Step 4: define $\widetilde f$.* For each $p \in A$, define $h_p : M \to \mathbb{R}^k$ by $h_p = \psi_p \widetilde f_p$ on $W_p$ and $h_p = 0$ outside $\operatorname{supp}(\psi_p)$. By Lemma 2, $h_p \in C^\infty(M)$.
>
> Define
> $$\widetilde f(q) = \sum_{p \in A} h_p(q) = \sum_{p \in A} \psi_p(q) \widetilde f_p(q).$$
> By local finiteness of $\{\operatorname{supp}(\psi_p)\}$, the sum is a finite sum at each point, hence $\widetilde f \in C^\infty(M)$ (sum of smooth functions, finite at each point).
>
> *Step 5: $\widetilde f|_A = f$.* Let $q \in A$. Then $\psi_0(q) = 0$ (since $A \cap \operatorname{supp}(\psi_0) = \emptyset$, as $\operatorname{supp}(\psi_0) \subseteq M \setminus A$). So $\sum_{p \in A} \psi_p(q) = 1$.
>
> Moreover, if $\psi_p(q) \neq 0$ for some $p \in A$, then $q \in \operatorname{supp}(\psi_p) \subseteq W_p$. On $W_p \cap A$, $\widetilde f_p = f$, so $\widetilde f_p(q) = f(q)$.
>
> Therefore
> $$\widetilde f(q) = \sum_{p \in A} \psi_p(q) \widetilde f_p(q) = \sum_{p \in A : \psi_p(q) \neq 0} \psi_p(q) f(q) = f(q) \sum_{p \in A} \psi_p(q) = f(q) \cdot 1 = f(q).$$
>
> *Step 6: $\operatorname{supp}(\widetilde f) \subseteq U$.* $\widetilde f$ is a sum of $h_p$, each supported in $\operatorname{supp}(\psi_p) \subseteq W_p \subseteq U$. So $\widetilde f \equiv 0$ outside $\bigcup_p \operatorname{supp}(\psi_p) \subseteq U$, hence $\operatorname{supp}(\widetilde f) \subseteq \overline{\bigcup_p \operatorname{supp}(\psi_p)}$. By local finiteness of the supports, this union of closed sets is itself closed (a locally finite union of closed sets is closed). So $\operatorname{supp}(\widetilde f) \subseteq \bigcup_p \operatorname{supp}(\psi_p) \subseteq U$.
>
> Therefore $\widetilde f$ is the required smooth extension. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**PDE on bounded domains: extending boundary data.** In boundary value problems for elliptic PDEs (Dirichlet, Neumann, Robin), one often has prescribed boundary data $g$ on $\partial \Omega$ (a closed subset of $\Omega$) and wants to extend $g$ to a smooth function $\widetilde g$ on $\Omega$ for use in the weak formulation. The extension lemma provides this: $\widetilde g \in C^\infty(\overline\Omega)$ with $\widetilde g|_{\partial \Omega} = g$. The PDE is then solved for $u = \widetilde g + v$ with $v$ in the test space (zero boundary).

**Topology: Tietze-type theorems.** The extension lemma is the smooth-category analogue of the Tietze extension theorem. The topological Tietze (continuous extension from closed subsets of normal spaces) extends to the smooth-Tietze (smooth extension from closed subsets of smooth manifolds). The proofs are parallel (sum of local separators), but the smooth-category needs smooth bumps. In normal Hausdorff spaces that lack smooth structure, only the continuous version holds — and indeed, on a topological manifold without a smooth structure, there is no notion of smooth extension.

**Geometric measure theory: smoothing characteristic functions of closed sets.** Given a closed set $K \subseteq M$, the indicator $\chi_K$ is discontinuous. By the extension lemma, the function $\chi_K|_K = 1$ extends to a smooth $\widetilde \chi : M \to \mathbb{R}$ with $\widetilde \chi \equiv 1$ on $K$ and $\widetilde \chi$ supported in any prescribed open neighbourhood of $K$. This is the *smooth indicator* — a smooth approximation of $\chi_K$, useful for integration arguments where the indicator's discontinuity is problematic. The values of $\widetilde \chi$ outside $K$ depend on the extension chosen; this non-uniqueness is exploited in **geometric measure theory** for limiting arguments.

**Differential topology: smooth extension to a closed manifold from a submanifold.** Given a smooth function on a closed submanifold $N \subseteq M$ (where $N$ is a *closed subset* of $M$ in the topological sense — e.g., a compact submanifold), the extension lemma yields a global smooth function on $M$ extending it. This is the standard mechanism for "extending data from a submanifold to the ambient manifold", used in cobordism theory, Morse theory, and the construction of smooth structures by gluing.

---

# Bridges

- **[[Thm - Existence of Smooth Partitions of Unity]]** — the main input. The extension is built as a partition-of-unity-weighted sum of local extensions.

- **[[Thm - Existence of Smooth Bump Functions]]** — the special case where $f \equiv 1$ on $A$. The extension lemma applied to the constant function $1$ on $A$ produces a smooth function equal to $1$ on $A$ and supported in $U$ — exactly a bump function. So the bump-function theorem is the constant case of the extension lemma. (The bump-function theorem is also derivable directly from partitions of unity, of course; the two are nearly the same theorem.)

- **[[Thm - Urysohn's Lemma]]** and **Tietze Extension Theorem** — the topological analogues. Urysohn produces continuous separators on normal spaces; Tietze extends continuous functions from closed subsets. The smooth extension lemma is the smooth-category version of Tietze.

- **The codomain issue (Lee Corollary 6.27)** — for codomain a general smooth manifold $N$ instead of $\mathbb{R}^k$, the extension lemma must be modified: smooth extension from a closed subset exists iff continuous extension exists. The proof uses tubular neighbourhood theorems (from [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]) and partition-of-unity arguments. The reason the simple-sum-of-extensions argument fails for non-vector codomains is that there is no global notion of "sum" — convex combinations of points in $N$ are not well-defined without additional structure.

- **Cousin problems and analytic obstruction** — in the holomorphic / real-analytic category, smooth extension is much more delicate. The Cousin I and Cousin II problems ask, respectively, for additive and multiplicative extensions of meromorphic/holomorphic data; these are governed by sheaf cohomology obstructions (vanishing of $H^1$ for the relevant sheaf). The smooth category trivializes these obstructions because the smooth-function sheaf is acyclic. The contrast is sharp: the extension lemma in the smooth category is a single page of partition-of-unity argument; in the holomorphic category it requires sheaf cohomology and is generally obstructed.

---

# Unlocked by This

> [!tip] Extending Smooth Sections of Vector Bundles *(from Differential Geometry)*
> The extension lemma extends to smooth sections of vector bundles: a smooth section defined on a closed subset extends to a global smooth section, supported in any prescribed open neighbourhood. The proof uses local trivializations to reduce to the $\mathbb{R}^k$-valued case. See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|DG VI]].

> [!tip] Approximating Continuous Functions by Smooth Ones *(from Approximation Theory)*
> Any continuous function on a smooth manifold can be uniformly approximated by smooth functions. The approximation uses the extension lemma to build smooth approximations of indicator functions of small open sets, then combines them via partition of unity. This is the **smooth Stone–Weierstrass theorem** for manifolds.

> [!tip] Smooth Lifting from Closed Subsets *(from Algebraic Topology and Differential Geometry)*
> When a continuous map $f : A \to N$ from a closed subset $A \subseteq M$ to a smooth manifold $N$ lifts to a smooth map (in the local-extension sense), the lift extends globally to a smooth $\widetilde f : M \to N$ — provided $N$ is a vector space, or, in the general case, provided the continuous version of $f$ extends globally (Lee Corollary 6.27).

> [!tip] Closed Sets are Zero Sets of Smooth Functions *(from Differential Topology)*
> Lee Theorem 2.29 (a direct corollary): every closed $K \subseteq M$ is exactly the zero set of some smooth nonnegative function $M \to [0, \infty)$. The construction extends the constant-$0$ function on $K$ to a non-negative function on $M$ that is positive away from $K$.

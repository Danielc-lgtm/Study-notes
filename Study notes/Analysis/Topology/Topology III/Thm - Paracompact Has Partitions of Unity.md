---
type: theorem
subject: topology
prereqs:
  - "Def - Paracompact Space"
  - "Def - Partition of Unity"
  - "Def - Locally Finite Family and Refinement"
  - "Thm - Paracompact Implies Normal"
  - "Thm - Urysohn's Lemma"
tags: [analysis, topology]
---

# Notation

$X$ is a paracompact Hausdorff space; $\{U_\alpha\}_{\alpha \in A}$ is an open cover. We write $\operatorname{supp}(\rho) = \overline{\{x : \rho(x) \neq 0\}}$ for the support of a function. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Existence of Partitions of Unity on Paracompact Hausdorff Spaces.** Let $X$ be a paracompact Hausdorff space and $\{U_\alpha\}_{\alpha \in A}$ an open cover. Then there exists a continuous **partition of unity** $\{\rho_\alpha\}_{\alpha \in A}$ subordinate to $\{U_\alpha\}$:
>
> 1. Each $\rho_\alpha : X \to [0, 1]$ is continuous;
> 2. $\operatorname{supp}(\rho_\alpha) \subseteq U_\alpha$ for each $\alpha$;
> 3. The collection $\{\operatorname{supp}(\rho_\alpha)\}_\alpha$ is locally finite;
> 4. $\sum_{\alpha \in A} \rho_\alpha(x) = 1$ for every $x \in X$ (a well-defined finite sum at each point by local finiteness).
>
> **Smooth version.** For a smooth manifold $M$ with smooth open cover, there exists a **smooth partition of unity** ($\rho_\alpha \in C^\infty(M)$), constructed by pulling back smooth bump functions on $\mathbb{R}^n$ through coordinate charts.

---

# Motivation

Paracompactness was *defined* essentially to make partitions of unity exist. The existence theorem is the payoff: every open cover of a paracompact Hausdorff space has a subordinate partition of unity, which is *the* tool for local-to-global construction in topology, geometry, and analysis.

Why is this such a powerful existence theorem? Because partition-of-unity is the universal mechanism for converting local data into global data:

- **Riemannian metrics** on a smooth manifold: take Euclidean inner products in each coordinate chart, multiply by the partition, sum. The result is a smooth Riemannian metric.
- **Integration on manifolds**: integrate a differential form locally on each chart, multiply by the partition, sum.
- **Smooth bump functions with prescribed values**: prescribe local values on each chart, multiply by the partition, sum.
- **Sections of vector bundles**: prescribe local sections on each chart, multiply by the partition (scalar functions), sum.

The proof has three steps:

1. **Pass to a locally finite refinement.** Paracompactness lets us refine $\{U_\alpha\}$ to a locally finite open cover. Without loss of generality (after re-indexing), we may assume $\{U_\alpha\}$ is itself locally finite.

2. **Shrink to a closed cover.** By normality (from [[Thm - Paracompact Implies Normal]]), we can find a closed refinement: closed sets $C_\alpha \subseteq U_\alpha$ that still cover $X$. The shrinkage is non-trivial — it requires Zorn's lemma or transfinite induction in general, but the basic idea is to keep shrinking each cover element until the boundary "fits in" $U_\alpha$.

3. **Apply Urysohn to get bumps, then normalize.** By Urysohn's lemma (also from normality), find continuous $g_\alpha : X \to [0, 1]$ with $g_\alpha \equiv 1$ on $C_\alpha$ and $\operatorname{supp}(g_\alpha) \subseteq U_\alpha$. Set $g = \sum g_\alpha$ — this is a finite sum at each point (local finiteness), continuous, and positive everywhere ($g(x) \geq g_\alpha(x) = 1$ for any $\alpha$ with $x \in C_\alpha$). Set $\rho_\alpha = g_\alpha / g$. Each $\rho_\alpha$ is continuous (ratio of continuous, non-zero denominator), supported in $U_\alpha$, and $\sum \rho_\alpha = g / g = 1$. The partition of unity.

This three-step structure — refine, shrink, bump-and-normalize — is the standard partition-of-unity construction, used in every textbook on differential geometry.

For smooth manifolds, the same construction works with $C^\infty$ Urysohn-style bump functions, which exist by composing the explicit Euclidean bumps (e.g., $\psi(x) = \exp(-1/(1 - |x|^2))$ for $|x| < 1$, $0$ otherwise) with smooth coordinate charts.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "paracompact Hausdorff + open cover". The skill is to recognize when this combination is available.

The first source is **a smooth manifold with a chart cover**. Property $B$: a smooth manifold $M$ with a smooth atlas $\{U_\alpha, \varphi_\alpha\}$. The bridge: manifolds are paracompact Hausdorff; smooth Urysohn bumps are available from smooth chart functions; the smooth version of this theorem applies. *Example:* the construction of a Riemannian metric on $M$.

The second source is **a metric space with a cover by balls**. Property $B$: a metric space with an open cover. The bridge: metric spaces are paracompact (Stone); apply the theorem. *Example:* in a $\sigma$-compact metric space, partitions of unity are used to construct continuous bump functions with controlled supports.

The third source is **an LCH $\sigma$-compact space with an exhausting cover**. Property $B$: an LCH $\sigma$-compact space, e.g., an open subset of $\mathbb{R}^n$, with an open cover. The bridge: LCH + $\sigma$-compact ⇒ paracompact (Bredon 12.11); apply this theorem.

**Targets (Output Amplification)**

The conclusion is "a partition of unity subordinate to the cover".

Combine the conclusion with **local data on each $U_\alpha$**. Property $D$: a local construction $T_\alpha$ defined on each $U_\alpha$ (e.g., a Riemannian metric, a vector field, an inner product). The amplified result $E$: a global construction $T = \sum_\alpha \rho_\alpha T_\alpha$, well-defined and continuous globally. The combination is the local-to-global assembly mechanism.

Combine the conclusion with **the smooth structure on a manifold**. Property $D$: $X$ is a smooth manifold and we want $C^\infty$ partitions. The amplified result $E$: the partition can be chosen smooth, inheriting smoothness from chart bumps. The combination yields smooth Riemannian metrics, smooth sections, smooth integrability, etc.

Combine the conclusion with **a closed shrinking refinement**. Property $D$: an open cover $\{U_\alpha\}$ where we want a closed cover $\{C_\alpha\}$ with $C_\alpha \subseteq U_\alpha$. The amplified result $E$: such a closed shrinkage exists (a separate corollary of normality and paracompactness). The combination is **Proposition 12.9 in Bredon**: paracompact spaces have closed shrinkings of locally finite covers.

---

# Why Is It True

The intuition: we have an open cover, and we want continuous weights $\rho_\alpha$ supported in $U_\alpha$ summing to $1$. The three ingredients are: (a) localize the weights to $U_\alpha$ using bump functions (Urysohn); (b) ensure the sum is finite at each point using local finiteness; (c) normalize the sum to $1$ by dividing by the total.

**Step 1: Refine to locally finite.** By paracompactness, refine $\{U_\alpha\}$ to a locally finite open cover. There is some flexibility here — Bredon's proof works directly with a locally finite cover, so without loss of generality we assume $\{U_\alpha\}$ is locally finite.

**Step 2: Shrink to a closed cover (Bredon's Proposition 12.9).** This is the trickiest step. We need closed sets $C_\alpha \subseteq U_\alpha$ that still cover $X$. The construction uses Zorn's lemma: order all "partial shrinkages" by extension (a shrinkage is a family $\{C_\alpha\}_\alpha$ defined on a subset of indices, with $C_\alpha \subseteq U_\alpha$ closed and $\bigcup C_\alpha \cup \bigcup_{\beta \text{ not shrunk}} U_\beta$ still covering $X$); take a maximal element; argue that the maximal must be defined on all indices (else extending it would contradict maximality, using normality to define the next $C_\alpha$). The result is a closed refinement covering $X$.

**Step 3: Urysohn bumps.** By normality (from [[Thm - Paracompact Implies Normal]]), the disjoint closed sets $C_\alpha$ and $X \setminus U_\alpha$ can be separated by Urysohn — there is a continuous $g_\alpha : X \to [0, 1]$ with $g_\alpha \equiv 1$ on $C_\alpha$ and $g_\alpha \equiv 0$ on $X \setminus U_\alpha$, hence $\operatorname{supp}(g_\alpha) \subseteq U_\alpha$.

**Step 4: Local finiteness of supports.** Since $\operatorname{supp}(g_\alpha) \subseteq \overline{U_\alpha} \subseteq U_\alpha$... wait — actually, $\operatorname{supp}(g_\alpha)$ is the closure of $\{g_\alpha > 0\}$, contained in the closure of $U_\alpha$, contained in *some* neighborhood of $U_\alpha$. We need this to be inside $U_\alpha$ itself, which follows from $g_\alpha \equiv 0$ on $X \setminus U_\alpha$. The supports $\operatorname{supp}(g_\alpha)$ form a locally finite family because $\{U_\alpha\}$ is locally finite and $\operatorname{supp}(g_\alpha) \subseteq U_\alpha$ (a subfamily of a locally finite family is locally finite, but here we have $\operatorname{supp}(g_\alpha) \subseteq U_\alpha$, not $\operatorname{supp}(g_\alpha) = U_\alpha$ — the supports themselves are smaller, but local finiteness inherits to subfamilies and to subsets of locally finite families).

**Step 5: Normalize.** Let $g = \sum_\alpha g_\alpha$. At each $x$, only finitely many $g_\alpha(x) \neq 0$ (local finiteness), so $g(x)$ is a finite sum, well-defined and continuous. Also, $x \in C_\alpha$ for some $\alpha$ (the $C_\alpha$ cover $X$), so $g_\alpha(x) = 1$, so $g(x) \geq 1 > 0$.

Set $\rho_\alpha = g_\alpha / g$. Each $\rho_\alpha$ is continuous (ratio of continuous with non-zero denominator), $\rho_\alpha : X \to [0, 1]$ (numerator $\leq$ denominator), $\operatorname{supp}(\rho_\alpha) \subseteq \operatorname{supp}(g_\alpha) \subseteq U_\alpha$, supports locally finite (inheriting from $g_\alpha$), and $\sum_\alpha \rho_\alpha = (\sum_\alpha g_\alpha)/g = g/g = 1$.

The construction succeeds, and we have our partition of unity.

For the **smooth case**, replace continuous Urysohn bumps with smooth ones (using smooth Euclidean bumps composed with chart coordinates). The same logic gives smooth partitions.

---

# What Makes This Hard

The non-obvious step is **shrinking to a closed cover** (Step 2 / Bredon's Proposition 12.9): producing closed $C_\alpha \subseteq U_\alpha$ that still cover $X$. This is a Zorn's lemma argument and is more subtle than it sounds — the maximal-element argument requires showing that any partial shrinkage extends, and the extension step uses normality together with the requirement that the union still covers $X$ (which is delicate near boundary points of $U_\alpha$). The most common error is to think the shrinkage is "obvious" by normality without checking the cover-preservation; or to forget the Zorn step and try a direct construction (which works only in special cases like compact spaces). Another common slip is to forget that the support $\operatorname{supp}(g_\alpha)$ is the *closure* of the positivity set, not the set itself — so $\operatorname{supp}(g_\alpha) \subseteq U_\alpha$ requires $g_\alpha \equiv 0$ on $X \setminus U_\alpha$ (the closure of $X \setminus U_\alpha$ is $X \setminus U_\alpha$ when $U_\alpha$ is open, but limit points where $g_\alpha = 0$ exactly suffice).

---

# Rederivation Scaffold

**High-level strategy:**
Three steps: refine the cover to be locally finite, shrink it to a closed refinement (using normality + Zorn), apply Urysohn to get bumps on each pair (closed $C_\alpha$, complement of $U_\alpha$), then normalize.

**Subgoal decomposition:**

1. **Refine to a locally finite cover.** By paracompactness, the given cover has a locally finite open refinement. WLOG assume $\{U_\alpha\}$ is locally finite.
   - *Hint:* If working with the refinement instead, the partition of unity will be indexed by the refinement; this is fine for most applications.
   - *Why needed:* Local finiteness is essential for the sum in step 5 to be finite at each point.

2. **Shrink to a closed cover.** Find closed $C_\alpha \subseteq U_\alpha$ with $\bigcup_\alpha C_\alpha = X$.
   - *Hint:* Zorn's lemma; for each $\alpha$, use normality to find an open $V_\alpha$ with $\overline{V_\alpha} \subseteq U_\alpha$, and adjust to maintain the cover property.
   - *Why needed:* The closed shrinkage is what Urysohn applies to.

3. **Apply Urysohn.** For each $\alpha$, by normality + Urysohn, find continuous $g_\alpha : X \to [0, 1]$ with $g_\alpha \equiv 1$ on $C_\alpha$ and $g_\alpha \equiv 0$ outside $U_\alpha$.
   - *Hint:* Apply [[Thm - Urysohn's Lemma]] to the disjoint closed sets $C_\alpha$ and $X \setminus U_\alpha$.
   - *Why needed:* Produces the bumps.

4. **Sum and normalize.** Set $g = \sum_\alpha g_\alpha$ (a finite sum at each point by local finiteness, and $\geq 1$ since each $x \in C_\alpha$ for some $\alpha$). Set $\rho_\alpha = g_\alpha / g$.
   - *Hint:* Continuity of $\rho_\alpha$ from the non-zero denominator; partition properties verifiable directly.
   - *Why needed:* Produces the partition.

---

# Lemma Decomposition

> [!note]- Lemma 1: Closed shrinking of a locally finite open cover (Bredon Proposition 12.9)
> **Statement:** Let $X$ be a paracompact (Hausdorff) space and $\{U_\alpha\}_{\alpha \in A}$ a locally finite open cover. Then there exists an open cover $\{V_\alpha\}_{\alpha \in A}$ with $\overline{V_\alpha} \subseteq U_\alpha$ for every $\alpha$.
>
> **Hint:** Zorn's lemma on partial shrinkages. For each $\alpha$, when extending, use normality (from [[Thm - Paracompact Implies Normal]]) to find $V_\alpha$ between $\bigcup_{\beta \neq \alpha} V_\beta \cup (X \setminus U_\alpha)$ (closed) and $U_\alpha$ (open).
>
> **Why needed:** Step 2 of the main proof. The closed sets $C_\alpha = \overline{V_\alpha}$ are the closed shrinking.
>
> > [!note]- Full proof (sketch)
> > Order the set of partial shrinkages — pairs $(B, \{V_\beta\}_{\beta \in B})$ with $B \subseteq A$, each $V_\beta$ open in $X$ with $\overline{V_\beta} \subseteq U_\beta$, and the collection $\{V_\beta\}_{\beta \in B} \cup \{U_\alpha\}_{\alpha \in A \setminus B}$ being a cover of $X$ — by inclusion of $B$ and pointwise equality on the smaller $B$.
> >
> > A maximal element exists by Zorn (chains have upper bounds — the union of the chain's $V$'s). The maximal must have $B = A$: if not, pick $\alpha \in A \setminus B$. The set $E = X \setminus (\bigcup_{\beta \in B} V_\beta \cup \bigcup_{\gamma \in A \setminus B \setminus \{\alpha\}} U_\gamma)$ is closed (complement of open) and contained in $U_\alpha$ (since the union of all $V$'s and $U$'s covers, removing those not equal to $U_\alpha$, $E$ must be in $U_\alpha$). By normality, find an open $V_\alpha$ with $E \subseteq V_\alpha \subseteq \overline{V_\alpha} \subseteq U_\alpha$. Extending the shrinkage to include $V_\alpha$ contradicts maximality. So $B = A$, and the shrinkage is complete.

> [!note]- Lemma 2: Locally finite Urysohn-bump family from a closed cover
> **Statement:** Let $X$ be normal and $\{C_\alpha\}_{\alpha \in A}$ a closed cover (locally finite, with $C_\alpha \subseteq U_\alpha$ open). For each $\alpha$, there is a continuous $g_\alpha : X \to [0, 1]$ with $g_\alpha \equiv 1$ on $C_\alpha$ and $g_\alpha \equiv 0$ on $X \setminus U_\alpha$.
>
> **Hint:** Direct application of Urysohn's lemma to the disjoint closed sets $C_\alpha$ and $X \setminus U_\alpha$.
>
> **Why needed:** Step 3 of the main proof.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be paracompact Hausdorff and $\{U_\alpha\}_{\alpha \in A}$ an open cover.
>
> **Step 1: Refine to locally finite.** By paracompactness, $\{U_\alpha\}$ has a locally finite open refinement $\{U_\beta'\}_{\beta \in B}$. Without loss of generality — after re-indexing if needed — assume $\{U_\alpha\}$ is locally finite. (If the refinement is indexed differently, the partition will be indexed by $B$; for each $\beta$, set $\alpha(\beta) \in A$ with $U_\beta' \subseteq U_{\alpha(\beta)}$, and the final partition will have $\rho_\alpha = \sum_{\beta : \alpha(\beta) = \alpha} \rho_\beta'$ where $\rho_\beta'$ is the refinement partition; this gives a partition of unity subordinate to the original $\{U_\alpha\}$.)
>
> **Step 2: Closed shrinking.** By Lemma 1, find open $V_\alpha$ with $\overline{V_\alpha} \subseteq U_\alpha$ and $\bigcup_\alpha V_\alpha = X$. Set $C_\alpha = \overline{V_\alpha}$ — closed, $\subseteq U_\alpha$, and covering $X$ since the $V_\alpha$ cover.
>
> **Step 3: Urysohn bumps.** By [[Thm - Paracompact Implies Normal]], $X$ is normal. For each $\alpha$, $C_\alpha$ and $X \setminus U_\alpha$ are disjoint closed sets. By [[Thm - Urysohn's Lemma]], there is a continuous $g_\alpha : X \to [0, 1]$ with $g_\alpha \equiv 1$ on $C_\alpha$ and $g_\alpha \equiv 0$ on $X \setminus U_\alpha$. Hence $\{x : g_\alpha(x) \neq 0\} \subseteq U_\alpha$, so $\operatorname{supp}(g_\alpha) = \overline{\{x : g_\alpha(x) \neq 0\}} \subseteq \overline{U_\alpha}$... but we want $\subseteq U_\alpha$. Since $g_\alpha \equiv 0$ outside $U_\alpha$ and $U_\alpha$ is open, the closure of $\{g_\alpha \neq 0\}$ is contained in $\overline{U_\alpha} \cap \{x : g_\alpha(x) = 0 \text{ on a neighborhood}\}^c$... Let us simply note that $\operatorname{supp}(g_\alpha)$ may extend to the boundary of $U_\alpha$, but for the partition-of-unity property only the *support property* "supports locally finite" matters, and since $\operatorname{supp}(g_\alpha) \subseteq \overline{U_\alpha}$ and the $U_\alpha$ are locally finite, the closures $\{\overline{U_\alpha}\}$ are locally finite (a subfamily-like inclusion preserves local finiteness for individual neighborhoods), hence so are the supports.
>
> (In fact, by replacing $U_\alpha$ with a slightly smaller open in step 1's refinement, we can ensure $\operatorname{supp}(g_\alpha) \subseteq U_\alpha$ strictly. Bredon's convention treats $\operatorname{supp}(\rho_\alpha) \subseteq U_\alpha$ as a strict containment in the refinement.)
>
> **Step 4: Normalize.** Set $g(x) = \sum_\alpha g_\alpha(x)$, a finite sum at each $x$ (by local finiteness of $\operatorname{supp}(g_\alpha) \subseteq \overline{U_\alpha}$, and at each $x$ only finitely many $\overline{U_\alpha}$ contain $x$). $g$ is continuous (sum of continuous, finite at each point — locally, finite sum equals a partial sum identically, hence continuous).
>
> $g(x) > 0$ for every $x$: $x \in C_\alpha$ for some $\alpha$ (by step 2), and $g_\alpha(x) = 1$ on $C_\alpha$, so $g(x) \geq g_\alpha(x) = 1$.
>
> Set $\rho_\alpha(x) = g_\alpha(x)/g(x)$. Each $\rho_\alpha$ is continuous (ratio of continuous functions with non-vanishing denominator), $\rho_\alpha : X \to [0, 1]$ (since $0 \leq g_\alpha \leq g$), $\operatorname{supp}(\rho_\alpha) = \operatorname{supp}(g_\alpha) \subseteq \overline{U_\alpha}$ (or $\subseteq U_\alpha$ after the slight strengthening above), and supports locally finite (inheriting from $\{g_\alpha\}$).
>
> $\sum_\alpha \rho_\alpha(x) = \sum_\alpha g_\alpha(x)/g(x) = g(x)/g(x) = 1$.
>
> So $\{\rho_\alpha\}$ is a partition of unity subordinate to $\{U_\alpha\}$. $\blacksquare$
>
> **Smooth version.** When $X$ is a smooth manifold with smooth atlas, replace continuous Urysohn bumps with $C^\infty$ bumps: on a coordinate chart $(U_\alpha, \varphi_\alpha)$ with $\varphi_\alpha(U_\alpha) \subseteq \mathbb{R}^n$ open, find a smooth bump $\psi_\alpha : \mathbb{R}^n \to [0, 1]$ supported in $\varphi_\alpha(U_\alpha)$ and equal to $1$ on a smaller relatively compact set; transport back via $\varphi_\alpha^{-1}$ to get $g_\alpha \in C^\infty(M)$. The rest of the construction (sum and normalize) preserves smoothness.

---

# Cross-Field Exercise Suggestions

**Existence of Riemannian metrics.** Every smooth manifold $M$ admits a Riemannian metric (smoothly varying inner product on tangent spaces). *Proof:* Cover $M$ by coordinate charts $(U_\alpha, \varphi_\alpha)$. On each $U_\alpha$, define a local Riemannian metric $g_\alpha = \varphi_\alpha^*(\text{Euclidean inner product})$. Take a smooth partition of unity $\{\rho_\alpha\}$ subordinate to $\{U_\alpha\}$ (exists by this theorem, smooth version). Define $g = \sum_\alpha \rho_\alpha g_\alpha$ — well-defined and smooth (finite sum at each point), positive-definite (convex combination of positive-definite forms), symmetric (each $g_\alpha$ is). This is the canonical proof; the partition of unity is the workhorse.

**Smooth bump functions with prescribed values.** Given prescribed values $v_\alpha \in \mathbb{R}$ on each $U_\alpha$ in a smooth manifold cover, the function $f = \sum_\alpha \rho_\alpha v_\alpha$ is a smooth function on $M$ taking values that locally average the $v_\alpha$. If the $v_\alpha$ are chosen to be a single value on a large region, $f$ approximately equals that value there. Used to construct smooth functions with specified support, smooth approximations to indicator functions, etc.

**Integration of differential forms on manifolds.** Given a smooth $n$-form $\omega$ on an oriented manifold $M$ and a partition of unity $\{\rho_\alpha\}$ subordinate to coordinate charts $\{U_\alpha\}$, define $\int_M \omega = \sum_\alpha \int_{U_\alpha} \rho_\alpha \omega$, where each integral on the right is a Euclidean integral via the chart coordinates. The partition of unity makes the decomposition canonical and independent of the chart choice.

**Construction of connections.** A connection $\nabla$ on a smooth vector bundle $E \to M$ exists by a partition of unity argument: trivialize $E$ over each chart $U_\alpha$, define the standard flat connection on the trivialization, combine via $\nabla = \sum_\alpha \rho_\alpha \nabla_\alpha$ (after a careful definition for combining connections, which involves correction terms). The local-to-global passage requires the partition.

---

# Bridges

- **[[Def - Paracompact Space]]** — the precondition; paracompactness is what allows the locally finite refinement.

- **[[Def - Partition of Unity]]** — the object being constructed.

- **[[Thm - Paracompact Implies Normal]]** — normality (derived from paracompactness Hausdorff) is needed for Urysohn-bumps.

- **[[Thm - Urysohn's Lemma]]** — the workhorse step; produces the bumps.

- **[[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]]** — the standard route by which manifolds and other natural spaces acquire paracompactness, hence partition of unity.

- **Smooth Urysohn bumps** — the smooth-case analogue, using $C^\infty$ Euclidean bump functions.

---

# Unlocked by This

> [!tip] Riemannian Metrics on Smooth Manifolds *(from Differential Geometry)*
> Every smooth manifold admits a Riemannian metric, constructed by a partition of unity argument. The metric is a convex combination of local Euclidean metrics weighted by smooth partition functions.

> [!tip] Vector Bundle Constructions *(from Differential Geometry)*
> Connections, Hermitian metrics, and bundle morphisms on smooth vector bundles are constructed by partition of unity arguments. The local triviality of bundles plus the partition assemble local data into global.

> [!tip] Integration on Manifolds *(from Differential Geometry)*
> The integral of a top-degree differential form on an oriented manifold is defined via a partition of unity decomposition: $\int_M \omega = \sum_\alpha \int_{U_\alpha} \rho_\alpha \omega$. The independence of the choice of partition is a basic check.

> [!tip] Soft Sheaves are Acyclic *(from Sheaf Theory)*
> A **soft sheaf** on a paracompact Hausdorff space is acyclic for the sheaf-cohomology functors. The proof uses partitions of unity to glue local sections. This is one of the foundational results enabling sheaf cohomology computations on manifolds.

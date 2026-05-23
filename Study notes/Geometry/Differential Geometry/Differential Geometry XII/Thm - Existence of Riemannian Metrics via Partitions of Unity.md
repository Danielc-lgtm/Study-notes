---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Partition of Unity on a Manifold"
  - "Thm - Existence of Smooth Partitions of Unity"
  - "Def - Smooth Manifold"
tags: [geometry, differential-geometry, riemannian-geometry, existence]
---

# Notation

$(M, g)$ — a smooth manifold $M$ with a Riemannian metric $g$ (the conclusion). $(U_\alpha, \varphi_\alpha)$ — a smooth chart, with $\varphi_\alpha : U_\alpha \to \mathbb{R}^n$ the coordinate map. $\bar g$ — the standard Euclidean metric on $\mathbb{R}^n$. $\{\psi_\alpha\}$ — a smooth partition of unity subordinate to the cover $\{U_\alpha\}$. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

---

# Statement

> **Theorem (Existence of Riemannian Metrics).** Every smooth manifold $M$, with or without boundary, admits a Riemannian metric.

This is Proposition 13.3 in Lee. The proof is a partition-of-unity gluing of local Euclidean pullback metrics.

---

# Motivation

A Riemannian metric is the *additional data* that converts a smooth manifold from a calculus object into a geometric one — once installed, lengths, angles, distances, gradients, volumes, and curvature become defined ([[Def - Riemannian Metric]]). The natural question is whether such data exists on a given manifold: is the geometric layer always available, or only under topological hypotheses?

This theorem answers: yes, always. Every smooth manifold (Hausdorff, second-countable, with or without boundary) admits at least one Riemannian metric. The proof is constructive and is the prototype of the **partition-of-unity gluing argument** that appears throughout differential geometry: cover by charts, use a local construction on each chart, and combine using a partition of unity. The local construction here is the pullback of the Euclidean metric; the gluing exploits the *convexity* of positive-definite forms, which makes positive combinations of positive-definite forms automatically positive-definite.

The contrast with the [[Thm - A Lorentzian Manifold Need Not Exist on Every Smooth Manifold|Lorentzian existence question]] is essential: not every smooth manifold admits a Lorentzian metric (the 2-sphere is the standard counterexample). The reason the partition-of-unity argument fails there is that *indefinite* non-degenerate symmetric forms do not form a convex set in the space of symmetric forms — a convex combination of two indefinite forms can be degenerate or change signature. The Riemannian case works because positive-definiteness *is* convex.

So this theorem is the statement that the most universal additional geometric structure on a smooth manifold — a positive-definite inner product field — is always available, and that the partition-of-unity construction is the universal method for producing it.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: Any smooth manifold.* The hypothesis is just that $M$ be a smooth manifold (Hausdorff, second-countable). No topological obstruction is in play; the result applies universally. This is what makes the theorem so reusable: every time one needs to assume "let $g$ be a Riemannian metric on $M$", the theorem makes the assumption free. The bridge from "smooth manifold" to "Riemannian metric is available" is the partition-of-unity argument, which uses second-countability (to get the partition of unity) and Hausdorffness (so that charts are actually open subsets).

*Source 2: Any smooth vector bundle.* The same construction works for any smooth real vector bundle $E \to M$ — every such bundle admits a **fibre metric** (a smooth choice of inner product on each fibre). The proof is identical: cover, pull back the Euclidean metric on each local trivialisation, glue with a partition of unity. The case $E = TM$ is the Riemannian metric, but the same theorem covers Hermitian metrics on complex bundles, sub-Riemannian metrics on a distribution, etc. Recognising this generalisation is the key to reusing the construction in new contexts.

*Source 3: Convex pointwise data.* The proof generalises to any "smooth choice of pointwise data" where the pointwise data lies in a convex set at each point. Examples: orientation forms (volume forms) on an oriented manifold (the cone of positive multiples of a fixed volume form is convex); connections on a bundle (the space of connections is an affine space and hence convex); Riemannian metrics with specified scale (the cone of positive-definite forms with given determinant). Whenever a problem reduces to "smoothly choose pointwise data in a convex set", the partition-of-unity gluing produces a global solution. *Trigger:* you need a smoothly varying structure, and pointwise the structure lies in a convex set.

**Targets (Output Amplification)**

*Target combination 1: Riemannian metric + a Riemannian property.* Once we have $g$, we have all the consequences of being a Riemannian manifold: a metric-space structure ([[Thm - The Riemannian Distance Makes M a Metric Space]]), musical isomorphisms ([[Thm - Musical Isomorphism Identifies Tangent and Cotangent Bundles]]), Levi-Civita connection ([[Thm - Fundamental Theorem of Riemannian Geometry (Statement)]]), and all of Riemannian geometry. The existence theorem is the gateway, and combining its conclusion ("there is a metric") with any standard result of Riemannian geometry yields the corresponding property on the manifold.

*Target combination 2: Combined with the [[Thm - The Riemannian Distance Makes M a Metric Space|metric-space theorem]], every smooth manifold is metrisable.* This is Corollary 13.30 of Lee. The existence theorem gives a metric $g$; the metric-space theorem turns it into a distance $d_g$ generating the manifold topology; hence the manifold topology is metrisable. This is the standard route to proving manifolds are metrisable, and it goes through Riemannian geometry rather than direct point-set topology.

*Target combination 3: Combined with paracompactness, every smooth manifold has reasonable analytic structure.* Riemannian metrics in conjunction with the underlying paracompactness of smooth manifolds (the hypothesis behind partitions of unity) give Sobolev spaces, $L^p$-spaces, Hodge theory, harmonic analysis, geometric PDE — all the analytic machinery one might want to bring to bear. Without the metric, none of these is well-defined; with the metric (existence guaranteed by this theorem), all of it is available.

---

# Why Is It True

**Mechanism summary:** **the cone of positive-definite forms is convex, so a positive convex combination of local Euclidean metrics is positive-definite — and a partition of unity is the manifold's machinery for taking smooth positive convex combinations of locally-defined objects.**

The argument is as natural as it is mechanical. At each point $p \in M$, one needs an inner product $g_p$ on $T_pM$ — equivalently, a positive-definite symmetric bilinear form on the $n$-dimensional vector space $T_pM$. The space of all symmetric bilinear forms on $T_pM$ is a vector space (of dimension $n(n+1)/2$), and the subset of positive-definite ones is a *convex open cone* in this vector space. So if I have *several* positive-definite forms — for instance, one local pullback from each chart covering $p$ — and I take a positive convex combination of them (positive coefficients summing to $1$), the result is again positive-definite.

Now, in a chart $(U, \varphi)$, the pullback $\varphi^* \bar g$ of the Euclidean metric is a Riemannian metric on $U$ (smooth, symmetric, positive-definite — these properties pull back). So on each chart we have a local Riemannian metric. To combine them globally, we need a way of "averaging" the local metrics with weights that vary smoothly across the manifold. That is exactly what a smooth partition of unity does: the functions $\psi_\alpha$ are non-negative, sum to $1$, and vary smoothly. Define $g = \sum_\alpha \psi_\alpha (\varphi_\alpha^* \bar g)$. Pointwise, this is a positive convex combination of positive-definite forms (only those $\alpha$ with $\psi_\alpha(p) > 0$ contribute, and they all give positive-definite forms at $p$), so $g_p$ is positive-definite. The sum is smooth by local finiteness of the partition of unity. So $g$ is a Riemannian metric on $M$.

The decisive insight, and the reason the argument can be remembered as a single move, is the **convexity of positive-definiteness**: positive linear combinations of positive-definite forms are positive-definite. This single algebraic fact does the entire work of the gluing. The same fact, *false* for indefinite forms, is why the analogous argument fails for Lorentzian metrics.

A different way to see why the result holds: a Riemannian metric is a section of a bundle whose fibres are positive-definite symmetric forms — a smooth subbundle of the symmetric $(0, 2)$-tensor bundle. The fibres are convex, non-empty (the Euclidean inner product on $\mathbb{R}^n$, pulled back via any chart, gives a positive-definite form in the fibre at every point), and *contractible* (in fact, convex cones). For a smooth bundle with convex, contractible fibres over a paracompact base, smooth sections always exist — this is a general principle. The partition-of-unity construction is the explicit method.

---

# What Makes This Hard

The theorem itself is not hard; the proof is short and follows the canonical pattern. The non-obvious part is **recognising the role of convexity** — that the existence theorem hinges on positive-definite forms being a convex set, and that this is what allows the partition-of-unity gluing to succeed. Students often go through the proof mechanically without noticing this, and then are surprised when the analogous Lorentzian existence question turns out to be obstructed. The trap is treating "existence by partition of unity" as a routine technique with no preconditions; the precondition is convexity of the relevant pointwise data, and recognising when it holds (Riemannian, Hermitian, volume forms) and when it fails (Lorentzian, almost complex structure, integer-valued data) is the conceptual content of the theorem.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Cover $M$ by smooth charts, use the Euclidean pullback metric on each chart, take a positive convex combination weighted by a partition of unity. The convexity of "positive-definite" makes the combination positive-definite.

**Subgoal decomposition:**

1. **Choose a cover of $M$ by smooth charts.** Use second-countability and Hausdorffness implicit in the definition of a smooth manifold.
   - *Hint:* The atlas of smooth charts on $M$ is a cover; refine if needed to make it locally finite (paracompactness of $M$).
   - *Why needed:* The local construction (pullback of Euclidean metric) requires charts.

2. **On each chart, define a local Riemannian metric.** Pull back the Euclidean metric.
   - *Hint:* $g_\alpha = \varphi_\alpha^* \bar g$, where $\varphi_\alpha : U_\alpha \to \mathbb{R}^n$ is the chart map.
   - *Why needed:* This is the local building block; positive-definiteness is inherited from $\bar g$.

3. **Take a smooth partition of unity subordinate to the cover.** Use [[Thm - Existence of Smooth Partitions of Unity]].
   - *Hint:* $\{\psi_\alpha\}$ with $\psi_\alpha \geq 0$, $\mathrm{supp}\,\psi_\alpha \subseteq U_\alpha$, $\sum_\alpha \psi_\alpha = 1$, locally finite.
   - *Why needed:* This gives the smooth weights for combining the local metrics.

4. **Define $g = \sum_\alpha \psi_\alpha g_\alpha$.** The sum is locally finite by paracompactness.
   - *Hint:* Extend each $\psi_\alpha g_\alpha$ by zero outside $U_\alpha$ to make global sense.
   - *Why needed:* This is the candidate global Riemannian metric.

5. **Verify $g$ is smooth, symmetric, positive-definite.** Smoothness and symmetry are routine; positive-definiteness uses the partition-of-unity property $\sum \psi_\alpha = 1$ together with convexity of positive-definite forms.
   - *Hint:* For any nonzero $v \in T_pM$, $g_p(v, v) = \sum_\alpha \psi_\alpha(p) g_{\alpha,p}(v, v)$. Each term is $\geq 0$ (since $g_\alpha$ is positive-definite where defined and $\psi_\alpha \geq 0$). At least one $\psi_\alpha(p) > 0$ (since they sum to $1$), and the corresponding $g_{\alpha,p}(v, v) > 0$ for $v \neq 0$. So the sum is positive.
   - *Why needed:* This completes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: Pullback of Euclidean metric on a chart is a Riemannian metric on $U$
> **Statement:** Let $(U, \varphi)$ be a smooth chart on $M$ with $\varphi : U \to \varphi(U) \subseteq \mathbb{R}^n$ a diffeomorphism. The pullback $\varphi^* \bar g$ is a Riemannian metric on $U$ (where $\bar g$ is the Euclidean metric on $\varphi(U) \subseteq \mathbb{R}^n$).
>
> **Hint:** Pullback preserves smoothness, symmetry, and positive-definiteness (since the differential of $\varphi$ is an isomorphism at each point of $U$).
>
> **Why needed:** Provides the local Riemannian metrics that the partition-of-unity gluing combines.
>
> > [!note]- Full proof
> > $\varphi^* \bar g$ is smooth because $\bar g$ is smooth and $\varphi$ is smooth, and pullback of smooth tensor fields is smooth. It is symmetric because $\bar g$ is symmetric and pullback preserves symmetry: $(\varphi^*\bar g)_p(v, w) = \bar g_{\varphi(p)}(d\varphi_p v, d\varphi_p w) = \bar g_{\varphi(p)}(d\varphi_p w, d\varphi_p v) = (\varphi^*\bar g)_p(w, v)$. It is positive-definite because $d\varphi_p : T_pU \to T_{\varphi(p)}\mathbb{R}^n$ is an isomorphism (the differential of a diffeomorphism), so for $v \neq 0$ we have $d\varphi_p v \neq 0$, hence $(\varphi^*\bar g)_p(v, v) = \bar g_{\varphi(p)}(d\varphi_p v, d\varphi_p v) > 0$.

> [!note]- Lemma 2: A positive convex combination of positive-definite forms is positive-definite
> **Statement:** Let $b_1, \ldots, b_k$ be positive-definite symmetric bilinear forms on a finite-dimensional vector space $V$, and let $\lambda_1, \ldots, \lambda_k \geq 0$ with at least one $\lambda_i > 0$. Then $b = \sum_i \lambda_i b_i$ is positive-definite.
>
> **Hint:** For $v \neq 0$, expand $b(v, v) = \sum_i \lambda_i b_i(v, v)$ — every term is non-negative, and a term with $\lambda_i > 0$ contributes a strictly positive amount.
>
> **Why needed:** This is the algebraic fact that makes the partition-of-unity gluing produce a positive-definite global metric.
>
> > [!note]- Full proof
> > Let $v \in V$ with $v \neq 0$. Each $b_i$ is positive-definite, so $b_i(v, v) > 0$ for every $i$. The combination $b(v, v) = \sum_i \lambda_i b_i(v, v)$ is a non-negative sum (since $\lambda_i \geq 0$ and $b_i(v, v) > 0$) of positive numbers, with at least one term strictly positive (the index $i$ with $\lambda_i > 0$). Hence $b(v, v) > 0$, proving positive-definiteness of $b$.
> >
> > Symmetry of $b$ is immediate from symmetry of the $b_i$.

> [!note]- Lemma 3: Partition of unity argument produces a global Riemannian metric
> **Statement:** Let $\{U_\alpha, \varphi_\alpha\}$ be a smooth atlas for $M$, $\{\psi_\alpha\}$ a smooth partition of unity subordinate to $\{U_\alpha\}$, and $g_\alpha = \varphi_\alpha^* \bar g$ the pullback metric on $U_\alpha$. Then $g = \sum_\alpha \psi_\alpha g_\alpha$ (where each $\psi_\alpha g_\alpha$ is extended by zero outside $U_\alpha$) is a Riemannian metric on $M$.
>
> **Hint:** Local finiteness of $\{\psi_\alpha\}$ gives smoothness; symmetry is immediate from each term; positive-definiteness uses Lemma 2.
>
> **Why needed:** This is the heart of the proof — the explicit construction of the global metric.
>
> > [!note]- Full proof
> > **Smoothness.** Each $\psi_\alpha g_\alpha$ is smooth on $U_\alpha$ (product of smooth function and smooth tensor field). Extending by zero outside $\mathrm{supp}\,\psi_\alpha \subseteq U_\alpha$ gives a smooth tensor field on $M$ (the extension is smooth because $\psi_\alpha$ and its derivatives vanish outside $\mathrm{supp}\,\psi_\alpha$, which is closed). By local finiteness of $\{\psi_\alpha\}$, only finitely many terms are nonzero in any neighbourhood of any point, so the sum $\sum_\alpha \psi_\alpha g_\alpha$ is a finite sum of smooth tensor fields locally, hence smooth globally.
> >
> > **Symmetry.** Each $g_\alpha$ is symmetric (Lemma 1), and each $\psi_\alpha g_\alpha$ is symmetric (scalar multiple of symmetric tensor). Sums of symmetric tensors are symmetric, so $g$ is symmetric.
> >
> > **Positive-definiteness.** Let $p \in M$ and $v \in T_pM$ with $v \neq 0$. Then
> > $$
> > g_p(v, v) = \sum_\alpha \psi_\alpha(p) g_{\alpha, p}(v, v),
> > $$
> > where only finitely many terms are nonzero. Each contributing term has $\psi_\alpha(p) \geq 0$ and (by Lemma 1) $g_{\alpha, p}(v, v) > 0$, so each term is $\geq 0$, and the contributing terms with $\psi_\alpha(p) > 0$ contribute strictly positive amounts. At least one $\psi_\alpha(p)$ is strictly positive (since $\sum_\alpha \psi_\alpha(p) = 1$), so the sum is strictly positive: $g_p(v, v) > 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a smooth manifold (Hausdorff, second-countable, with or without boundary).
>
> **Step 0 — well-posedness preconditions.** Smooth atlases exist on $M$ by definition. By second countability and Hausdorffness, $M$ is paracompact (Lee, Proposition 1.12), so smooth partitions of unity subordinate to any open cover exist by [[Thm - Existence of Smooth Partitions of Unity]].
>
> **Step 1 — Local metrics.** Choose a smooth atlas $\{(U_\alpha, \varphi_\alpha)\}_{\alpha \in A}$ for $M$, where $\varphi_\alpha : U_\alpha \to \varphi_\alpha(U_\alpha) \subseteq \mathbb{R}^n$ is a smooth diffeomorphism onto an open subset. On each $U_\alpha$, set $g_\alpha := \varphi_\alpha^* \bar g$, the pullback of the standard Euclidean metric $\bar g$ on $\mathbb{R}^n$. By Lemma 1, $g_\alpha$ is a Riemannian metric on $U_\alpha$.
>
> **Step 2 — Partition of unity.** Let $\{\psi_\alpha\}_{\alpha \in A}$ be a smooth partition of unity subordinate to the cover $\{U_\alpha\}$: each $\psi_\alpha : M \to [0, 1]$ is smooth with $\mathrm{supp}\,\psi_\alpha \subseteq U_\alpha$, the family is locally finite, and $\sum_\alpha \psi_\alpha(p) = 1$ for every $p \in M$.
>
> **Step 3 — Global metric.** Define
> $$
> g := \sum_\alpha \psi_\alpha\, g_\alpha,
> $$
> where each $\psi_\alpha g_\alpha$ is extended by zero outside $U_\alpha$ (the extension is smooth because $\psi_\alpha$ has support in $U_\alpha$).
>
> **Step 4 — Verification.** By Lemma 3, $g$ is a smooth, symmetric, positive-definite $(0, 2)$-tensor field on $M$, hence a Riemannian metric. $\blacksquare$

---

# Cross-Field Exercise Suggestions

*1. Existence of Hermitian metrics on complex vector bundles.* The same partition-of-unity argument shows that every smooth complex vector bundle $E \to M$ over a smooth manifold admits a smoothly varying Hermitian inner product on each fibre. The positive-definite Hermitian forms on a complex vector space form a convex cone, exactly as the positive-definite symmetric bilinear forms do, and the gluing works identically.

*2. Existence of Riemannian volume forms.* On an oriented smooth manifold, every Riemannian metric induces a [[Def - Riemannian Volume Form|volume form]] $dV_g$. The existence of orientations is itself a topological condition (not every manifold is orientable), but once an orientation is fixed, the choice of metric gives a volume form. The partition-of-unity argument can be applied directly to "positive top forms compatible with the orientation" — these form a convex cone, and the gluing gives a global volume form even without going through the metric.

*3. Existence of sub-Riemannian structures.* A **sub-Riemannian** structure on $M$ is a smooth distribution $\mathcal{D} \subseteq TM$ together with a fibre metric on $\mathcal{D}$ — a Riemannian metric on a *subbundle* of $TM$. By the same partition-of-unity argument applied to the subbundle, every smooth distribution admits a sub-Riemannian metric. This is the geometric setting of, e.g., the Carnot–Carathéodory metric on the Heisenberg group, the metric of optimal control problems, and sub-Riemannian geodesics.

*4. Failure for almost complex structures.* An **almost complex structure** on $M$ is a smooth bundle endomorphism $J : TM \to TM$ with $J^2 = -\mathrm{id}$. Pointwise this requires $T_pM$ to be even-dimensional and gives a complex structure on the tangent space. *Unlike* Riemannian metrics, almost complex structures are obstructed: the manifold must be even-dimensional, and even then there are further topological obstructions (the existence of $J$ on the $2k$-sphere $S^{2k}$ fails for most $k$ — only $k = 1$ ($S^2$) and $k = 3$ ($S^6$) admit one, and even on $S^6$ no integrable $J$ has been found). The reason the partition-of-unity argument fails is that the set of complex structures on $\mathbb{R}^{2k}$ is *not* convex — averaging two complex structures gives an endomorphism with $J^2 \neq -\mathrm{id}$ in general.

---

# Bridges

- **[[Thm - Existence of Smooth Partitions of Unity]]** — the topological-analytic foundation of the proof. Smooth partitions of unity exist because smooth manifolds are paracompact; this is the input that converts local data (one metric per chart) into global data (one metric on all of $M$). The same theorem is used in the existence proofs of orientations, connections, smooth extensions, and many other "patching" constructions in differential geometry, each of which is one specific application of the partition-of-unity construction to a different convex pointwise structure.

- **[[Thm - A Lorentzian Manifold Need Not Exist on Every Smooth Manifold]]** — the counterpoint. The Lorentzian analogue *fails* because Lorentzian metrics are not pointwise convex: a convex combination of two Lorentzian metrics can change signature or become degenerate. Comparing the two theorems clarifies exactly what convexity does in the Riemannian proof.

- **[[Thm - The Riemannian Distance Makes M a Metric Space]]** — the immediate downstream consequence. Once a metric exists, the [[Def - Length of a Curve and Riemannian Distance|Riemannian distance]] makes $M$ a metric space, and combined with this existence theorem yields the corollary that every smooth manifold is metrisable as a topological space (Lee Corollary 13.30).

- **[[Thm - Fundamental Theorem of Riemannian Geometry (Statement)]]** — the deepest downstream consequence. The existence theorem provides a metric; the fundamental theorem turns the metric into a unique torsion-free metric-compatible connection (Levi-Civita), which then generates all of Riemannian geometry. Existence of metrics is the gateway, and the Levi-Civita connection is the immediate gate's destination.

---

# Unlocked by This

> [!tip] Every Smooth Manifold is Metrisable *(from Point-Set Topology of Manifolds)*
> Combining this existence theorem with [[Thm - The Riemannian Distance Makes M a Metric Space|the metric-space theorem]] gives: every smooth (Hausdorff, second-countable) manifold is metrisable. This is Corollary 13.30 of Lee, and it is the standard route to manifold metrisability — through Riemannian geometry rather than direct point-set arguments.

> [!tip] Existence of Complete Riemannian Metrics *(from Riemannian Geometry)*
> Once a Riemannian metric exists, one can ask whether a *complete* one exists. The answer (Lee Problem 13-17): every connected smooth manifold admits a complete Riemannian metric, constructed by rescaling a given Riemannian metric $g$ to $\tilde g = h\, g$ for a suitably chosen positive function $h$. The proof uses an exhaustion function and is more subtle than the basic existence theorem, but the conclusion is that "complete Riemannian manifold" is also a universally available structure.

> [!tip] Universal Properties of Smooth Vector Bundles *(from Vector Bundle Theory)*
> The same partition-of-unity argument shows that every smooth real (resp. complex) vector bundle over a paracompact base admits a fibre metric (resp. Hermitian fibre metric). This is the structural input that turns vector bundle theory into a geometric subject — once a fibre metric is available, the bundle has an orthogonal complement decomposition, a notion of orthonormal frame, and (after choice of connection) a notion of parallel transport preserving the inner product.

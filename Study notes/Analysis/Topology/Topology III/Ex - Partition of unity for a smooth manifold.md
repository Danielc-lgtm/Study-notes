---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Partition of Unity"
  - "Def - Paracompact Space"
  - "Thm - Locally Compact σ-Compact Hausdorff is Paracompact"
  - "Thm - Paracompact Has Partitions of Unity"
tags: [analysis, topology]
---

# Problem Statement

Let $M$ be a smooth manifold — Hausdorff, second countable, locally diffeomorphic to $\mathbb{R}^n$ via smooth charts $\{(U_\alpha, \phi_\alpha)\}$ with $\phi_\alpha : U_\alpha \to V_\alpha \subseteq \mathbb{R}^n$ a diffeomorphism onto an open subset of $\mathbb{R}^n$.

(a) Show that $M$ is locally compact (every point has a compact neighborhood) and $\sigma$-compact (a countable union of compact subsets). Hence by [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]], $M$ is paracompact.

(b) Conclude from [[Thm - Paracompact Has Partitions of Unity]] that every open cover of $M$ admits a continuous partition of unity. Strengthen this: every open cover of $M$ admits a *smooth* ($C^\infty$) partition of unity.

(c) As an application, sketch the construction of a **Riemannian metric** on $M$: a smoothly varying inner product on each tangent space. Combine local inner products in each chart (the Euclidean one, pulled back via $\phi_\alpha$) with a smooth partition of unity subordinate to $\{U_\alpha\}$.

(d) Sketch the construction of **integration of a top-form** on an oriented $M$: define locally in charts using the Lebesgue integral on $\mathbb{R}^n$, weight by partition of unity, sum.

**Recall:**

A **[[Def - Partition of Unity|partition of unity]]** subordinate to an open cover $\{U_\alpha\}$ of $X$ is a family of continuous (or smooth) functions $\{\rho_\alpha : X \to [0, 1]\}$ with $\operatorname{supp}(\rho_\alpha) \subseteq U_\alpha$, locally finite supports, and $\sum_\alpha \rho_\alpha \equiv 1$.

[[Thm - Locally Compact σ-Compact Hausdorff is Paracompact|LC + σ-compact + Hausdorff ⇒ paracompact]]. The standard manifold definition makes $M$ Hausdorff, locally compact (since $\mathbb{R}^n$ is locally compact and charts are diffeomorphisms onto open subsets), and second countable, hence $\sigma$-compact.

![[Thm - Locally Compact σ-Compact Hausdorff is Paracompact#Statement]]

**[[Thm - Paracompact Has Partitions of Unity|Paracompact Hausdorff ⇒ has partitions of unity]]** subordinate to any open cover.

---

# Convergent Strategy

**Problem class.** *Application synthesis*: combine several theorems of [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III §11–12]] to produce the standard machinery used in differential geometry. The structural narrative: (i) topology of $M$ gives paracompactness; (ii) paracompactness gives continuous partitions of unity; (iii) smooth structure upgrades to smooth partitions of unity; (iv) smooth partitions of unity are the engine of geometric constructions.

**Assumption pattern.** Smooth manifold (with the standard definition) ⇒ paracompact, hence partition of unity. The smooth upgrade requires *smooth* bump functions, which exist on $\mathbb{R}^n$ ([[Ex - Partitions of unity on Rn]]) and pull back smoothly to chart neighborhoods of $M$.

**Theorem routing.**
- LC + $\sigma$-compact + Hausdorff ⇒ paracompact ([[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]]).
- Paracompact + Hausdorff ⇒ continuous partition of unity exists ([[Thm - Paracompact Has Partitions of Unity]]).
- *Smooth upgrade:* use smooth bumps in $\mathbb{R}^n$, pulled back via charts. Sum, normalize.
- *Riemannian metric:* in each chart use pulled-back Euclidean metric; glue with smooth partition of unity; sum of positive-definite forms is positive-definite.
- *Integration:* in each chart use $\int_{V_\alpha} (\phi_\alpha^{-1})^* \omega \cdot \rho_\alpha$; sum over $\alpha$ via partition of unity.

**Key decision point.** The smoothness of the partition of unity requires both (a) smooth bumps in $\mathbb{R}^n$, (b) careful pullback through charts, and (c) normalization preserving smoothness (which works because the denominator is locally a finite sum of smooth bumps, hence smooth, and bounded below by a positive constant on any compact set).

---

# Legal Operations Used

1. **Combine local compactness and $\sigma$-compactness to get paracompactness** ([[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]]).

2. **Pull smooth bumps from $\mathbb{R}^n$ to chart neighborhoods of $M$** via the diffeomorphisms $\phi_\alpha$. A smooth function on $V_\alpha$ pulls back to a smooth function on $U_\alpha$; extending by zero gives a smooth function on $M$ supported in $U_\alpha$.

3. **Use a smooth partition of unity to glue local constructions into global** — multiply local pieces by $\rho_\alpha$ and sum.

4. **Combine positive-definite local forms with a partition of unity** — positive linear combinations of positive-definite forms are positive-definite. This is the standard "convex combination" trick for building positive structures.

---

# Hints

> [!note]- Hint 1
> *$M$ locally compact.* For $p \in M$, take chart $(U, \phi)$ with $p \in U$. The image $\phi(p) \in V = \phi(U) \subseteq \mathbb{R}^n$ has a compact neighborhood (a closed ball $\overline B$), and $\phi^{-1}(\overline B) \subseteq U$ is a compact neighborhood of $p$ in $M$.

> [!note]- Hint 2
> *$M$ $\sigma$-compact.* Second countability + Hausdorff + local compactness ⇒ $\sigma$-compact. Take a countable basis of opens with compact closure (such a basis exists for second-countable LCH spaces); the closures of the basis elements are countably many compacts whose union is $M$.

> [!note]- Hint 3
> *Smooth partition of unity construction.* Cover $M$ by precompact charts $\{U_\alpha\}$. By paracompactness, refine to a locally finite open cover $\{W_\beta\}$ each contained in some $U_{\alpha(\beta)}$. In each $V_\beta = \phi_{\alpha(\beta)}(W_\beta) \subseteq \mathbb{R}^n$, build a smooth bump function with compact support in $V_\beta$ via the $\exp(-1/t)$ trick. Pull back to $M$, extend by zero. Sum, normalize.

> [!note]- Hint 4
> *Riemannian metric.* In each chart $(U_\alpha, \phi_\alpha)$, pull back the standard Euclidean inner product: $g_\alpha(p)(v, w) = \langle d\phi_\alpha(v), d\phi_\alpha(w) \rangle_{\mathbb{R}^n}$ for $p \in U_\alpha$ and $v, w \in T_pM$. Then set $g = \sum_\alpha \rho_\alpha g_\alpha$ — a smooth section of $T^*M \otimes T^*M$, positive definite at each $p$ (positive combination of positive forms).

---

# Solution

The smooth-manifold infrastructure of differential geometry rests on smooth partitions of unity, which exist precisely because of the topological structure of $M$ (LC + $\sigma$-compact + Hausdorff) combined with the smoothness inherited from $\mathbb{R}^n$.

**Step 1: $M$ is locally compact.**

> [!note]- Derivation
> Let $p \in M$. By definition of "smooth manifold", there is a chart $(U, \phi)$ with $p \in U$, $\phi : U \to V$ a diffeomorphism, $V \subseteq \mathbb{R}^n$ open. Choose a closed ball $\overline B_r(\phi(p)) \subseteq V$ — possible because $V$ is open. The closed ball is compact in $\mathbb{R}^n$ (Heine–Borel). Its preimage $K = \phi^{-1}(\overline B_r(\phi(p)))$ is a compact subset of $U \subseteq M$ (homeomorphism preserves compactness), containing $p$, and $K \supseteq \phi^{-1}(B_r(\phi(p)))$, an open neighborhood of $p$. So $K$ is a compact neighborhood of $p$.

**Step 2: $M$ is $\sigma$-compact.**

> [!note]- Derivation
> Second countability gives a countable basis $\{B_n\}_{n \in \mathbb{N}}$ for the topology of $M$. By local compactness + Hausdorff, refine to a countable basis $\{B_n\}_{n \in \mathbb{N}}$ where each $B_n$ has *compact closure* (in any LCH space with a countable basis, the precompact open sets form a basis — take the original basis and intersect each element with a precompact open neighborhood of each of its points, exploiting second countability to keep countability). Then $M = \bigcup_n \overline{B_n}$, a countable union of compacts.

**Step 3: $M$ is paracompact.**

> [!note]- Derivation
> By [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]], locally compact + $\sigma$-compact + Hausdorff ⇒ paracompact. All three hypotheses hold (Steps 1, 2, and "$M$ is Hausdorff by definition"). Hence $M$ is paracompact.

**Step 4: $M$ has continuous partitions of unity for every open cover.**

> [!note]- Derivation
> By [[Thm - Paracompact Has Partitions of Unity]], every paracompact Hausdorff space admits continuous partitions of unity subordinate to any open cover. Since $M$ is paracompact Hausdorff (Step 3), continuous partitions of unity exist.

**Step 5: The smooth upgrade — smooth partitions of unity exist.**

> [!note]- Derivation
> The general construction (paracompactness) gives only *continuous* partitions of unity. To get *smooth*, use the smoothness of $\mathbb{R}^n$ to construct smooth bumps.
>
> *Construction.* Given an open cover $\{U_\alpha\}$ of $M$, first refine to an open cover $\{W_\beta\}$ that is locally finite (by paracompactness) and where each $W_\beta$ is contained in some chart domain $U_{\alpha(\beta)}$. (One can further refine so that each $\overline{W_\beta}$ is compact in $M$, contained in a slightly larger chart domain $U'_{\alpha(\beta)}$.)
>
> *Construct a smooth bump $\sigma_\beta$ on $M$ with $\sigma_\beta > 0$ on $W_\beta$ and $\operatorname{supp}(\sigma_\beta) \subseteq U_{\alpha(\beta)}$.* In the chart $(U_{\alpha(\beta)}, \phi_{\alpha(\beta)})$, $\phi_{\alpha(\beta)}(W_\beta)$ is a relatively compact open subset of $\phi_{\alpha(\beta)}(U_{\alpha(\beta)}) \subseteq \mathbb{R}^n$. Build a smooth bump $\eta_\beta$ on $\mathbb{R}^n$ with $\eta_\beta > 0$ on $\phi_{\alpha(\beta)}(W_\beta)$ and $\operatorname{supp}(\eta_\beta) \subseteq \phi_{\alpha(\beta)}(U_{\alpha(\beta)})$, using the standard $\exp(-1/t)$ construction (see [[Ex - Partitions of unity on Rn]]). Pull back: $\sigma_\beta(p) = \eta_\beta(\phi_{\alpha(\beta)}(p))$ for $p \in U_{\alpha(\beta)}$, $\sigma_\beta(p) = 0$ for $p \notin U_{\alpha(\beta)}$. The pullback is smooth on $U_{\alpha(\beta)}$ (composition of smooth) and smoothly extends by zero (the support of $\eta_\beta$ is compactly contained in $\phi_{\alpha(\beta)}(U_{\alpha(\beta)})$, so the extension is smooth at the boundary of $U_{\alpha(\beta)}$).
>
> *Normalize.* The sum $S = \sum_\beta \sigma_\beta$ is locally a finite sum (locally finite $\{W_\beta\}$ ⇒ locally finite $\{\operatorname{supp}\sigma_\beta\}$ ⇒ at each $p$, only finitely many $\sigma_\beta(p) \neq 0$). Hence $S$ is smooth. $S > 0$ everywhere: at $p \in M$, $p$ lies in some $W_\beta$ where $\sigma_\beta(p) > 0$, so $S(p) > 0$. Set $\rho_\beta = \sigma_\beta / S$. Then $\{\rho_\beta\}$ is a smooth partition of unity subordinate to $\{U_{\alpha(\beta)}\}$, hence subordinate to $\{U_\alpha\}$ (relabeling).

**Step 6: Application — Riemannian metric.**

> [!note]- Derivation
> A *Riemannian metric* on $M$ is a smooth section $g$ of the bundle $T^*M \otimes T^*M$ — equivalently, a smoothly varying symmetric positive-definite bilinear form $g_p : T_pM \times T_pM \to \mathbb{R}$.
>
> *Construction.* Take any chart cover $\{U_\alpha, \phi_\alpha\}$ and a subordinate smooth partition of unity $\{\rho_\alpha\}$. In each chart, define a local Riemannian metric $g_\alpha$ on $U_\alpha$ by pulling back the standard Euclidean inner product:
> $$g_\alpha(p)(v, w) = \langle d\phi_\alpha|_p(v), d\phi_\alpha|_p(w) \rangle_{\mathbb{R}^n}, \quad p \in U_\alpha, v, w \in T_pM.$$
> Then $g_\alpha$ is a smooth Riemannian metric on $U_\alpha$ (smooth and positive definite by construction).
>
> *Glue.* Define $g = \sum_\alpha \rho_\alpha g_\alpha$ — interpreted pointwise: at $p$, $g(p) = \sum_\alpha \rho_\alpha(p) g_\alpha(p)$, where the sum is taken only over $\alpha$ with $p \in U_\alpha$ (so $g_\alpha(p)$ is defined) and $\rho_\alpha(p) > 0$. The sum is locally finite (finite at each $p$), hence well-defined and smooth.
>
> *Positive definiteness.* At $p$, $g(p)(v, v) = \sum_\alpha \rho_\alpha(p) g_\alpha(p)(v, v)$. Each $g_\alpha(p)(v, v) \geq 0$, with equality iff $v = 0$ (positive definiteness of pulled-back Euclidean). The sum is $\geq 0$, with equality iff every term is zero — but $\sum_\alpha \rho_\alpha(p) = 1$, so some $\rho_\alpha(p) > 0$, hence $g_\alpha(p)(v, v) = 0$ for that $\alpha$, forcing $v = 0$. So $g(p)(v, v) > 0$ for $v \neq 0$ — positive definite.
>
> *Smoothness.* Smooth at each $p$ (locally finite sum of smooth forms).
>
> Hence $g$ is a smooth Riemannian metric on $M$.

**Step 7: Application — integration of a top-form.**

> [!note]- Derivation
> Let $\omega$ be a compactly supported top-degree differential form on an oriented smooth manifold $M$ of dimension $n$. Define
> $$\int_M \omega = \sum_\alpha \int_M \rho_\alpha \omega,$$
> where $\{\rho_\alpha\}$ is a smooth partition of unity subordinate to an oriented chart cover $\{(U_\alpha, \phi_\alpha)\}$.
>
> *Each piece $\int_M \rho_\alpha \omega$ is defined.* $\rho_\alpha \omega$ has support in $U_\alpha$, so we can transport via the chart: $\int_M \rho_\alpha \omega = \int_{V_\alpha} (\phi_\alpha)_* (\rho_\alpha \omega) = \int_{\mathbb{R}^n} f_\alpha \, dx^1 \wedge \dots \wedge dx^n$, with $f_\alpha = (\rho_\alpha \omega)(p) / (dx^1 \wedge \dots \wedge dx^n)$ in the chart — a compactly supported smooth function on $\mathbb{R}^n$. The Lebesgue integral of a compactly supported smooth function is finite.
>
> *Finiteness of the sum.* The support of $\omega$ is compact, hence meets only finitely many $U_\alpha$ (local finiteness of $\{\operatorname{supp}\rho_\alpha\}$). So only finitely many terms $\int_M \rho_\alpha \omega$ are nonzero — finite sum.
>
> *Invariance under change of partition or chart.* By the change-of-variables formula for the Lebesgue integral and the orientation-preserving nature of the charts, $\int_M \omega$ does not depend on the choice of partition of unity or chart cover. This is the standard verification omitted here.
>
> Hence integration of compactly supported top-forms is well-defined on oriented smooth manifolds, via the partition-of-unity recipe.

> [!note]- Complete formal solution
> *(a) Paracompactness.* $M$ is LC (compact preimages of closed Euclidean balls under charts), $\sigma$-compact (countable basis ⇒ countably many precompact basics covering $M$), Hausdorff (by definition). [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]] gives paracompact.
>
> *(b) Smooth partitions of unity.* Continuous exist by [[Thm - Paracompact Has Partitions of Unity]]. Smooth upgrade: refine cover to locally finite + each refinement element in a chart; in each chart pull back a smooth bump from $\mathbb{R}^n$ (standard $\exp(-1/t)$ construction); normalize.
>
> *(c) Riemannian metric.* In each chart pull back Euclidean inner product; glue with $g = \sum_\alpha \rho_\alpha g_\alpha$. Positive definite (positive combination of positive-definite forms, $\sum \rho_\alpha = 1$ ensures nontrivial), smooth (locally finite sum of smooth).
>
> *(d) Integration of top-forms.* $\int_M \omega = \sum_\alpha \int_M \rho_\alpha \omega$, each piece a Lebesgue integral over $\mathbb{R}^n$ via chart. Finite sum (compact support of $\omega$). Invariance under partition/chart choice by change-of-variables formula. $\blacksquare$

---

# Key Takeaways

**Every smooth manifold has smooth partitions of unity subordinate to every open cover — this is the *single* most-used tool of differential geometry.** Almost every existence theorem on smooth manifolds proceeds by: (i) construct the desired object locally in each chart, where the question reduces to a problem in $\mathbb{R}^n$; (ii) glue with a smooth partition of unity. This is how Riemannian metrics, connections, smooth Cartan-style frame bundles, distributions, foliations, and orientations are built. The structural prerequisites are exactly what the standard manifold definition provides: paracompactness via LC + $\sigma$-compact + Hausdorff, smooth structure for the smooth upgrade. Without paracompactness (the long line — see [[Ex - A non-paracompact space]]), all these constructions fail.

**Trigger-reaction: "I have a local construction on a smooth manifold and need it globally" ⇒ "use a smooth partition of unity".** This is *the* defining move of differential geometry. The pattern: cover $M$ by charts; in each chart do the local construction (which reduces to $\mathbb{R}^n$, where everything is easy); multiply by $\rho_\alpha$ and sum. The sum is well-defined because partitions of unity are locally finite (only finitely many terms at each point), and smoothness is preserved because all pieces are smooth. The result is global, smooth, and inherits the desired property from the local pieces — provided the property is preserved under positive linear combinations (which holds for Riemannian metrics, smooth functions, positive measures, etc.).

**Positive-definiteness is preserved under positive combinations, which is why Riemannian metrics exist.** $g = \sum_\alpha \rho_\alpha g_\alpha$ is positive-definite at $p$ if each $g_\alpha(p)$ is positive-definite *and* the coefficients $\rho_\alpha(p)$ are non-negative with $\sum \rho_\alpha(p) = 1$. The partition-of-unity condition $\sum_\alpha \rho_\alpha = 1$ is *essential* for this — without it, the sum could be zero, breaking positive-definiteness. The general principle: positive-definite forms (in any setting — Riemannian metrics, Hermitian metrics, positive measures) form a *convex cone*, and partition of unity arguments combine local witnesses via convex combinations.

**The smoothness of the partition of unity requires *smooth* bumps in $\mathbb{R}^n$.** The $\exp(-1/t)$ construction is the source of smoothness in differential geometry. Without smooth bumps, only *continuous* partitions of unity exist (e.g. via [[Thm - Paracompact Has Partitions of Unity]]), which give continuous Riemannian metrics — not enough for the smooth invariants of differential geometry. The continuity-vs-smoothness distinction is exactly the distinction between general manifold topology and smooth manifold geometry; smoothness adds the analytic content.

**Trigger-reaction: "I have an open cover of a manifold and need a globally defined object that is locally one thing per chart" ⇒ "find a partition of unity and weight".** Standard examples beyond Riemannian metrics: (i) a smooth function with prescribed Taylor coefficients at a point — use Borel's theorem in one chart, extend smoothly via partition of unity; (ii) integrating a compactly supported top-form — sum the chart-by-chart integrals weighted by $\rho_\alpha$ (Step 7); (iii) defining a connection on a vector bundle — use trivializations in each chart, glue with partition of unity; (iv) constructing a Whitney embedding $M \hookrightarrow \mathbb{R}^{2n + 1}$ — use local charts and partition of unity to assemble local coordinate functions into a global embedding.

**The full chain LC + $\sigma$-compact + Hausdorff ⇒ paracompact ⇒ partition of unity is the *engine* of every differential geometric construction.** This is one of the cleanest "topology → geometry" pipelines in mathematics: the abstract topological hypotheses of "manifoldness" (locally Euclidean + Hausdorff + second countable) suffice to produce the analytical tools needed for everything else. Compare with: in algebraic geometry, schemes are *not* paracompact in this sense (the Zariski topology is too coarse), and partitions of unity *do not exist* — which is why algebraic geometry uses sheaves and Čech cohomology instead of partition-of-unity arguments. The structural choice "what topological category to work in" determines what tools are available.

**Bridges: this exercise is the topological foundation for everything in [[Multivariate Analysis II — Inverse and Implicit Function Theorems]], differential topology, Riemannian geometry, and integration on manifolds.** The single fact "smooth manifolds have smooth partitions of unity" supports an enormous downstream edifice: the Whitney embedding theorem, Hodge theory, the de Rham theorem, the existence of geodesic structure, the existence of foliations, the construction of characteristic classes, the construction of moduli spaces. Each of these stories begins with "by partition of unity, we may assume..." and then proceeds with a local argument in $\mathbb{R}^n$.

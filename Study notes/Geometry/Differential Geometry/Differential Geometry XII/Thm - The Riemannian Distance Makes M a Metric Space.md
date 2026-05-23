---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Length of a Curve and Riemannian Distance"
  - "Def - Riemannian Metric"
  - "Def - Metric Space"
tags: [geometry, differential-geometry, riemannian-geometry, topology]
---

# Notation

$(M, g)$ — a connected Riemannian manifold. $d_g$ — the [[Def - Length of a Curve and Riemannian Distance|Riemannian distance]] function, $d_g(p, q) = \inf L_g(\gamma)$ over piecewise smooth curves from $p$ to $q$. $\bar g$ — the standard Euclidean metric on $\mathbb{R}^n$ used inside coordinate charts; $L_{\bar g}$ and $d_{\bar g}$ are the corresponding Euclidean length and distance functions. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

---

# Statement

> **Theorem ([[Def - Riemannian Manifold|Riemannian Manifolds]] as [[Def - Metric Space|Metric Spaces]]).** Let $(M, g)$ be a connected Riemannian manifold. With the Riemannian distance function $d_g$, $M$ is a [[Def - Metric Space|metric space]]. Moreover, the metric topology induced by $d_g$ coincides with the original manifold topology on $M$.

This is Theorem 13.29 in Lee. The non-trivial content is the *positivity* of $d_g$ (that $p \neq q$ implies $d_g(p, q) > 0$) and the *topology coincidence* — the rest is routine.

---

# Motivation

A Riemannian metric assigns lengths to tangent vectors and, via integration, lengths to curves. By taking infimum over curves connecting two points, we get a distance function $d_g(p, q)$ — a candidate metric in the point-set-topology sense. The question is whether this candidate is actually a metric, and whether the topology it induces on $M$ is the right one.

The theorem affirms both. The Riemannian distance is a genuine metric (satisfying non-negativity, symmetry, triangle inequality, and *positivity*), and the metric topology agrees with the manifold topology. So a Riemannian manifold is automatically a metric space, and there is no conflict between the two topological pictures.

The conceptual significance is that this is the bridge between differential geometry and point-set topology. Once installed, every notion of metric topology — open balls, Cauchy sequences, completeness, total boundedness, Heine–Borel — becomes available on a Riemannian manifold, with the metric being the Riemannian distance. Conversely, the manifold's local structure makes the metric have a particularly nice form: locally, it is comparable to the Euclidean metric.

Combined with the [[Thm - Existence of Riemannian Metrics via Partitions of Unity|existence theorem]], the result has the corollary that every smooth manifold is *metrisable* — admits a distance function generating its topology. This is the standard route to manifold metrisability.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: A connected Riemannian manifold.* Connectedness is needed so that any two points can be joined by a piecewise smooth curve, hence $d_g$ is finite. For disconnected manifolds, distances between different components are conventionally $+\infty$ (or undefined), and one works component by component. The bridge from "Riemannian manifold" to the precondition "$d_g$ is defined" is the connectedness assumption together with the path-connectedness of any connected smooth manifold.

*Source 2: Any continuous Riemannian-like structure.* The argument generalises to any structure that has a well-defined "length of curves" and is locally comparable to Euclidean: Finsler manifolds (with smooth norms varying smoothly on tangent spaces), sub-Riemannian manifolds (where lengths are defined only along horizontal curves), even some non-smooth situations. The key input is the **local-comparability lemma** (Lee Lemma 13.28): on a compact set in a coordinate chart, the Riemannian metric is bilipschitz-equivalent to the Euclidean metric.

*Source 3: Any smooth manifold (via the existence theorem).* Combined with [[Thm - Existence of Riemannian Metrics via Partitions of Unity]], this theorem says: every smooth manifold has a metric (in the point-set-topology sense) generating its topology — every smooth manifold is metrisable.

**Sources (Input Broadening) — what makes the precondition recognisable in disguise:**

A common starting point for invoking this theorem is *not* "I have a Riemannian metric" — that source is too obvious — but *"I have a smooth manifold and want to do analysis"*. Once we recognise that any Riemannian metric induces a distance, and any smooth manifold has a Riemannian metric, the chain is: smooth manifold $\rightarrow$ Riemannian metric (existence theorem) $\rightarrow$ Riemannian distance $\rightarrow$ metric-space structure. So the disguised source is "smooth manifold", routing through this theorem to "metric space".

**Targets (Output Amplification)**

*Target combination 1: Distance + completeness gives Hopf–Rinow.* The Riemannian distance plus a completeness assumption (every Cauchy sequence converges) gives the **Hopf–Rinow theorem**: a connected Riemannian manifold is metrically complete iff geodesically complete iff every closed bounded set is compact, and any two points are then joined by a length-minimising geodesic. This is the central completeness theorem of Riemannian geometry; the distance function provided by this theorem is the input.

*Target combination 2: Distance + continuity gives uniform continuity.* On a compact subset of a Riemannian manifold, every continuous function is uniformly continuous with respect to $d_g$. Combined with this theorem, continuous-function theory on manifolds runs through the Riemannian distance, with the same Heine–Borel theorem and uniform-continuity statements as in $\mathbb{R}^n$.

*Target combination 3: Distance + sequence convergence agrees with manifold convergence.* The topology-coincidence half of the theorem implies that a sequence $p_n \to p$ in $M$ (manifold topology) iff $d_g(p_n, p) \to 0$. So convergence in the Riemannian distance is the same as convergence in the manifold topology — the two pictures of "limit" agree. This is essential for analysis on manifolds: it lets one use metric-space techniques (Cauchy sequences, completeness) interchangeably with manifold techniques (charts, smooth functions).

---

# Why Is It True

**Mechanism summary:** **on any compact set inside a coordinate chart, the Riemannian metric $g$ is uniformly bilipschitz-equivalent to the Euclidean metric in that chart — so $d_g$-distances are pinched between scaled $d_{\bar g}$-distances, and the topology generated by $d_g$ has to coincide with the Euclidean (hence manifold) topology.**

The result is intuitively clear once stated correctly: in a small enough neighborhood of any point, the manifold "looks like" $\mathbb{R}^n$, the Riemannian metric "looks like" the Euclidean metric, and the Riemannian distance "looks like" the Euclidean distance. The work is in making this intuition precise.

The decisive observation is **Lemma 13.28** of Lee: on a compact subset $K$ of a coordinate chart, viewed as an open subset of $\mathbb{R}^n$, the Riemannian norm $|v|_g$ and the Euclidean norm $|v|_{\bar g}$ are uniformly comparable. There exist constants $c, C > 0$ depending on $K$ and $g$ such that
$$
c\, |v|_{\bar g} \;\leq\; |v|_g \;\leq\; C\, |v|_{\bar g} \qquad \text{for all } x \in K,\ v \in T_x\mathbb{R}^n.
$$
The proof is a compactness argument: the function $(x, v) \mapsto |v|_g$ is continuous and strictly positive on the compact set $\{(x, v) : x \in K,\ |v|_{\bar g} = 1\}$ (a "unit sphere bundle" over $K$), so it is bounded above and below by positive constants. The general case follows by homogeneity.

Once this lemma is in hand:

**Positivity** ($p \neq q$ implies $d_g(p, q) > 0$): Pick a small chart $U$ around $p$ but not containing $q$, a regular coordinate ball $V$ of Euclidean radius $\varepsilon$ around $p$ with $\bar V \subseteq U$, and constants $c, C$ from the local comparability lemma on $\bar V$. Any piecewise smooth curve from $p$ to $q$ must exit $\bar V$ (since $q \notin V$); the portion inside $\bar V$ has $g$-length at least $c \cdot \varepsilon$ (since its Euclidean length is at least $\varepsilon$, the radius). So $d_g(p, q) \geq c\varepsilon > 0$.

**Topology coincidence** ($M$-open iff $d_g$-open): Any manifold-open set $U$ around $p$ contains a regular coordinate ball $V$ of small Euclidean radius $\varepsilon$, hence (by local comparability) a $d_g$-ball of radius $c\varepsilon$ around $p$. So manifold-open implies $d_g$-open. Conversely, a $d_g$-ball of radius $\rho$ around $p$ — restricted to a coordinate chart $V$ around $p$ — contains a small Euclidean ball $V_{\rho/C}$, hence is a neighbourhood in the manifold topology.

So the entire structure of the theorem rests on **the local comparability of $g$ and $\bar g$ on compact sets**, which is itself a consequence of compactness and continuity of the metric tensor.

---

# What Makes This Hard

The conceptual obstruction is recognising that **positivity of $d_g$ is the only non-trivial axiom**. Non-negativity, symmetry, and the triangle inequality all follow trivially from the definition $d_g(p, q) = \inf L_g(\gamma)$. Positivity — the statement $d_g(p, q) > 0$ for $p \neq q$ — requires the local-comparability argument, which is where all the content lives. Without it one could, *a priori*, imagine a degenerate metric where points have distance zero from each other but are not the same point (a "pseudometric"). The positivity proof rules this out, and it is the heart of the theorem.

The topology-coincidence half is then a relatively quick consequence, also resting on local comparability: every neighbourhood in one topology contains a neighbourhood in the other.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Routine properties (non-negativity, symmetry, triangle inequality) follow from the definition. Positivity and topology-coincidence both reduce to a single local-comparability lemma: on any compact $K$ inside a chart, $g$ and $\bar g$ are bilipschitz equivalent.

**Subgoal decomposition:**

1. **Non-negativity and $d_g(p, p) = 0$.** Constant curves have length zero.
   - *Hint:* $L_g(\text{constant curve}) = 0$.
   - *Why needed:* Half of the metric-space axioms come for free.

2. **Symmetry $d_g(p, q) = d_g(q, p)$.** Reverse any curve to swap endpoints.
   - *Hint:* If $\gamma : [a, b] \to M$ goes from $p$ to $q$, then $\tilde\gamma(t) = \gamma(a + b - t)$ goes from $q$ to $p$ and $L_g(\tilde\gamma) = L_g(\gamma)$.
   - *Why needed:* Trivial axiom.

3. **Triangle inequality.** Concatenate curves.
   - *Hint:* For any curve $\gamma_1$ from $p$ to $q$ and any $\gamma_2$ from $q$ to $r$, the concatenation is a piecewise smooth curve from $p$ to $r$ with length $L(\gamma_1) + L(\gamma_2)$; take infimum.
   - *Why needed:* The metric-space triangle inequality.

4. **Local comparability lemma (Lee Lemma 13.28).** On any compact $K \subseteq U$ in a chart, there exist $c, C > 0$ with $c|v|_{\bar g} \leq |v|_g \leq C|v|_{\bar g}$ for all $x \in K$, $v \in T_x M$.
   - *Hint:* Compactness of $\{(x, v) \in TK : |v|_{\bar g} = 1\}$ plus continuity of $(x, v) \mapsto |v|_g$.
   - *Why needed:* The key technical input for everything below.

5. **Positivity $d_g(p, q) > 0$ for $p \neq q$.** Apply the comparability lemma to a small ball around $p$ not containing $q$.
   - *Hint:* Any curve from $p$ to $q$ must cross out of any small chart-ball around $p$, and the portion inside that ball has length bounded below by a positive constant.
   - *Why needed:* The decisive positivity axiom.

6. **Topology coincidence.** Use comparability to pinch $d_g$-balls between Euclidean balls.
   - *Hint:* Manifold-open and $d_g$-open both reduce to coordinate-ball open via local comparability.
   - *Why needed:* The topology-coincidence half of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Local comparability of $g$ and $\bar g$ on compact sets (Lee 13.28)
> **Statement:** Let $g$ be a Riemannian metric on an open subset $U \subseteq \mathbb{R}^n$, and let $K \subseteq U$ be compact. Then there exist constants $c, C > 0$ such that for all $x \in K$ and all $v \in T_x \mathbb{R}^n$,
> $$
> c\, |v|_{\bar g} \;\leq\; |v|_g \;\leq\; C\, |v|_{\bar g}.
> $$
>
> **Hint:** Consider the function $(x, v) \mapsto |v|_g$ on the compact set $L = \{(x, v) : x \in K,\ |v|_{\bar g} = 1\}$. It is continuous and strictly positive, hence bounded above and below by positive constants. The general case follows by homogeneity ($|v|_g$ is homogeneous of degree $1$ in $v$).
>
> **Why needed:** This is the key technical input for both positivity of $d_g$ and topology coincidence.
>
> > [!note]- Full proof
> > Under the canonical identification $T\mathbb{R}^n \cong \mathbb{R}^n \times \mathbb{R}^n$, the set
> > $$
> > L = \{(x, v) \in TU : x \in K,\ |v|_{\bar g} = 1\}
> > $$
> > is the product $K \times S^{n-1}$ and is therefore compact (product of compact sets). The function $(x, v) \mapsto |v|_g$ is continuous on $TU$ (since $g$ is smooth, hence the components $g_{ij}(x)$ are continuous, and $|v|_g = \sqrt{g_{ij}(x)v^i v^j}$ is a continuous function of $(x, v)$). It is strictly positive on $L$: at any $(x, v) \in L$, $v \neq 0$ so $|v|_g > 0$.
> >
> > A continuous strictly positive function on a compact set attains its extrema, both positive. So there exist constants $c, C > 0$ with $c \leq |v|_g \leq C$ for every $(x, v) \in L$.
> >
> > For general $(x, v) \in TK$ with $v \neq 0$, set $\lambda = |v|_{\bar g} > 0$; then $(x, \lambda^{-1}v) \in L$, so by homogeneity ($|v|_g$ is linear in $v$ in the sense $|tv|_g = |t| |v|_g$):
> > $$
> > |v|_g = \lambda\, |\lambda^{-1} v|_g \leq \lambda C = C |v|_{\bar g},
> > $$
> > and similarly $|v|_g \geq c |v|_{\bar g}$. For $v = 0$, both sides are zero, so the inequality is trivial.

> [!note]- Lemma 2: Positivity of $d_g$ for distinct points
> **Statement:** For a connected Riemannian manifold $(M, g)$ and distinct points $p, q \in M$, $d_g(p, q) > 0$.
>
> **Hint:** Pick a chart around $p$ not containing $q$ and a small regular coordinate ball $V$ around $p$. Any curve from $p$ to $q$ exits $V$, and the segment inside $V$ has length bounded below by Lemma 1.
>
> **Why needed:** This is the non-trivial metric-space axiom — without it, $d_g$ would only be a pseudometric.
>
> > [!note]- Full proof
> > Let $p \neq q$. Choose a smooth coordinate chart $(U, \varphi)$ with $p \in U$ and $q \notin U$. Choose a regular coordinate ball $V$ of Euclidean radius $\varepsilon > 0$ centred at $p$ with $\bar V \subseteq U$. Apply Lemma 1 on the compact $\bar V$ (viewed via the chart as a subset of $\mathbb{R}^n$): there exist constants $c, C > 0$ with $c|v|_{\bar g} \leq |v|_g \leq C|v|_{\bar g}$ for every $x \in \bar V$, $v \in T_x M$.
> >
> > Let $\gamma : [a, b] \to M$ be any piecewise smooth curve from $p$ to $q$. Since $q \notin V$, the image of $\gamma$ exits $V$, so $\gamma(t_1) \in \partial V$ for some $t_1 \in (a, b)$ (continuity, intermediate value). Restrict to $[a, t_0]$ where $t_0$ is the *infimum* of $\{t : \gamma(t) \notin V\}$, so $\gamma|_{[a, t_0]}$ lies in $\bar V$ and $\gamma(t_0) \in \partial V$. By Lemma 1,
> > $$
> > L_g(\gamma) \geq L_g(\gamma|_{[a, t_0]}) \geq c\, L_{\bar g}(\gamma|_{[a, t_0]}) \geq c\, d_{\bar g}(p, \gamma(t_0)) = c \varepsilon,
> > $$
> > where the last equality uses that $\gamma(t_0) \in \partial V$ is at Euclidean distance exactly $\varepsilon$ from $p$, and the Euclidean straight-line distance bounds any curve length from above (so $L_{\bar g}(\gamma|_{[a, t_0]}) \geq d_{\bar g}(p, \gamma(t_0)) = \varepsilon$).
> >
> > Taking infimum over all such $\gamma$: $d_g(p, q) \geq c\varepsilon > 0$.

> [!note]- Lemma 3: Topology coincidence
> **Statement:** On a connected Riemannian manifold $(M, g)$, the metric topology induced by $d_g$ equals the original manifold topology.
>
> **Hint:** Every manifold-neighbourhood of $p$ contains a $d_g$-ball, and every $d_g$-ball contains a manifold-neighbourhood — both by Lemma 1 applied to a small chart-ball.
>
> **Why needed:** This is the topology-coincidence half of the theorem.
>
> > [!note]- Full proof
> > **Manifold-open $\Rightarrow$ $d_g$-open.** Let $U$ be a manifold-open neighbourhood of $p$. Pick a regular coordinate ball $V \subseteq U$ of Euclidean radius $\varepsilon$ around $p$. By Lemma 2's argument: for any $q \notin V$, $d_g(p, q) \geq c\varepsilon$ where $c$ is from Lemma 1 on $\bar V$. So the $d_g$-ball $\{q : d_g(p, q) < c\varepsilon\}$ is contained in $V \subseteq U$, showing $U$ is $d_g$-open.
> >
> > **$d_g$-open $\Rightarrow$ manifold-open.** Let $W$ be $d_g$-open with $p \in W$, so there exists $\rho > 0$ with $\{q : d_g(p, q) < \rho\} \subseteq W$. Pick a regular coordinate ball $V$ of Euclidean radius $r > 0$ around $p$ with $\bar V \subseteq M$, and constants $c, C$ from Lemma 1 on $\bar V$. Choose $\varepsilon < r$ small enough that $C\varepsilon < \rho$, and let $V_\varepsilon \subseteq V$ be the Euclidean ball of radius $\varepsilon$ around $p$ in the chart. For $q \in V_\varepsilon$, the straight-line curve in coordinates from $p$ to $q$ has Euclidean length $|p - q|_{\bar g} < \varepsilon$ and lies in $\bar V$, so by Lemma 1 its $g$-length is at most $C\varepsilon < \rho$. Hence $d_g(p, q) < \rho$, and $V_\varepsilon \subseteq W$. Since $V_\varepsilon$ is a manifold-open neighbourhood of $p$, $W$ is manifold-open.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(M, g)$ be a connected Riemannian manifold and $d_g$ the Riemannian distance function.
>
> **Step 0 — well-posedness.** Since $M$ is connected (and smooth manifolds are locally path-connected, hence path-connected if connected), any two points of $M$ can be joined by a piecewise smooth curve (Proposition 11.33 of Lee), so $d_g(p, q)$ is a well-defined real number (the infimum of a nonempty set bounded below by zero).
>
> **Step 1 — $d_g \geq 0$, $d_g(p, p) = 0$, $d_g$ symmetric, triangle inequality.**
>
> - Non-negativity: $L_g(\gamma) \geq 0$ for every curve $\gamma$, since the integrand $|\dot\gamma|_g$ is non-negative.
> - $d_g(p, p) = 0$: the constant curve at $p$ has length zero.
> - Symmetry: any curve $\gamma$ from $p$ to $q$ has a reverse $\tilde\gamma$ from $q$ to $p$ of the same length, so the infima are equal.
> - Triangle inequality: for any curves $\gamma_1$ from $p$ to $q$ and $\gamma_2$ from $q$ to $r$, the concatenation $\gamma_1 \cdot \gamma_2$ is a piecewise smooth curve from $p$ to $r$ of length $L(\gamma_1) + L(\gamma_2)$, so $d_g(p, r) \leq L(\gamma_1) + L(\gamma_2)$. Taking infimum over each: $d_g(p, r) \leq d_g(p, q) + d_g(q, r)$.
>
> **Step 2 — Positivity for $p \neq q$.** This is Lemma 2 above, proved via the local-comparability Lemma 1.
>
> By Steps 1 and 2, $(M, d_g)$ is a metric space.
>
> **Step 3 — Topology coincidence.** This is Lemma 3 above, again via Lemma 1.
>
> Combining, $(M, d_g)$ is a metric space whose induced topology equals the original manifold topology. $\blacksquare$

---

# Cross-Field Exercise Suggestions

*1. Metrisability of arbitrary smooth manifolds.* Combining this theorem with [[Thm - Existence of Riemannian Metrics via Partitions of Unity]], one obtains: every smooth manifold (with or without boundary) is metrisable. This is the standard proof of manifold metrisability — much cleaner than direct point-set arguments using partition-of-unity-based Urysohn-type constructions.

*2. Hopf–Rinow theorem application.* On a connected Riemannian manifold, the following are equivalent: (i) $(M, d_g)$ is metrically complete; (ii) every [[Def - Geodesic|geodesic]] extends to all parameter values ([[Def - Geodesic|geodesic]] completeness); (iii) every closed bounded subset of $M$ is compact; (iv) for some $p \in M$, the exponential map $\exp_p$ is defined on all of $T_pM$. The implications use this theorem as a starting point, then layer in the Levi-Civita connection from [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)]].

*3. Distance function on Lie [[Def - Group|groups]].* For a Lie group $G$ with a left-invariant Riemannian metric, the Riemannian distance is also left-invariant: $d_g(hp, hq) = d_g(p, q)$ for every $h \in G$. So $G$ acts on itself by [[Def - Isometry|isometries]] via left translation. This connects the topology of Lie [[Def - Group|groups]] to the geometry of their invariant metrics.

*4. Riemannian distance vs. graph-theoretic distance on a triangulated manifold.* On a smoothly triangulated manifold, one can compare the Riemannian distance to the path-distance on the 1-skeleton with edge lengths given by Riemannian lengths. The two are mutually quasi-isometric (with constants depending on the triangulation), illustrating how Riemannian geometry interfaces with combinatorial/PL geometry.

---

# Bridges

- **[[Def - Metric Space]]** — the target structure. The theorem produces a metric space from a Riemannian manifold; the metric-space machinery (open balls, Cauchy sequences, completeness, total boundedness, Heine–Borel) then applies. The bridge is operational: any time a metric-space concept is invoked on a Riemannian manifold, this theorem is implicitly being used.

- **[[Thm - Existence of Riemannian Metrics via Partitions of Unity]]** — the existence input. The existence theorem says a Riemannian metric is always available; this theorem says, once available, it generates a metric space structure. Combined, they give: every smooth manifold is metrisable.

- **[[Thm - Heine–Borel Theorem]]** — the classical theorem this generalises. In $\mathbb{R}^n$, closed and bounded equals compact. On a complete Riemannian manifold, by Hopf–Rinow, closed and bounded equals compact also. The local-comparability argument used to prove this theorem is, in a sense, "Heine–Borel in coordinates": the local comparison between $g$ and $\bar g$ uses compactness of the unit sphere in $\mathbb{R}^n$, which is Heine–Borel content.

- **[[Def - Cauchy Sequence and Complete Metric Space]]** — the next concept to define. A Cauchy sequence in $(M, d_g)$ is one for which $d_g(p_n, p_m) \to 0$ as $n, m \to \infty$. The manifold is **complete** iff every Cauchy sequence converges. By Hopf–Rinow this is equivalent to geodesic completeness, but the equivalence requires the Levi-Civita connection and is the content of Riemannian geometry rather than this chapter.

---

# Unlocked by This

> [!tip] Every Smooth Manifold is Metrisable *(from Point-Set Topology of Manifolds)*
> Combined with [[Thm - Existence of Riemannian Metrics via Partitions of Unity]], this gives the corollary: every smooth manifold is metrisable as a topological space. This is the standard route to metrisability of manifolds — through Riemannian geometry rather than direct point-set arguments. (Lee Corollary 13.30.)

> [!tip] The Hopf–Rinow Theorem *(from Riemannian Geometry)*
> Combined with the Levi-Civita connection of [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)]], the metric-space picture of this theorem unfolds into the **Hopf–Rinow theorem**: a connected Riemannian manifold is metrically complete iff geodesically complete iff closed-and-bounded equals compact iff $\exp_p$ is defined on $T_pM$ for some $p$. Under any of these equivalent conditions, every pair of points is joined by a length-minimising geodesic. This is the central completeness/connectedness theorem of Riemannian geometry, and the metric-space structure provided here is its foundation.

> [!tip] Distance Comparison Theorems *(from Comparison Geometry)*
> Once a distance function exists, one can compare it to distances on model spaces (constant-curvature spaces). The **Toponogov triangle comparison theorem**, the **Rauch comparison theorem**, and the entire programme of **comparison geometry** depend on having a distance function to compare, and this theorem is the foundation. Comparison geometry connects sectional curvature bounds to global metric properties (diameter, volume growth, fundamental group).

> [!tip] Sobolev Spaces and Analysis on Manifolds *(from Geometric Analysis)*
> Once a Riemannian metric and its distance are available, $L^p$-spaces, Sobolev spaces $W^{k, p}$, and elliptic PDE theory can be set up on Riemannian manifolds. The Riemannian distance is the input that lets one define $L^p$-norms (using the Riemannian volume form), Hölder continuity (using $d_g$), and uniform-continuity arguments on compact subsets. The entire geometric-analysis programme — harmonic maps, mean curvature flow, Ricci flow, Yamabe problem — runs on these foundations.

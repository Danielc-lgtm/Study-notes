---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Length of a Curve and Riemannian Distance"
  - "Thm - The Riemannian Distance Makes M a Metric Space"
  - "Def - Metric Space"
tags: [geometry, differential-geometry, riemannian-geometry, topology]
---

# Problem Statement

Let $(M, g)$ be a connected Riemannian manifold with Riemannian distance function $d_g$. Prove that the metric topology on $M$ induced by $d_g$ coincides with the original (manifold) topology on $M$.

That is, prove: a subset $U \subseteq M$ is open in the manifold topology if and only if it is open in the metric topology induced by $d_g$.

**Recall:**

![[Def - Length of a Curve and Riemannian Distance#The Definition]]

A subset $U \subseteq M$ is **open in the metric topology** induced by $d_g$ if for every $p \in U$ there exists $r > 0$ such that the metric ball $B_{d_g}(p, r) = \{q \in M : d_g(p, q) < r\}$ is contained in $U$.

A subset $U \subseteq M$ is **open in the manifold topology** if for every $p \in U$ there is a smooth chart $(V, \varphi)$ on $M$ with $p \in V \subseteq U$ (or equivalently, by definition of the manifold topology).

The key technical tool — the **local-comparability lemma** — is Lemma 13.28 of Lee: on any compact subset $K$ of a coordinate chart, viewed via the chart as an open subset of $\mathbb{R}^n$, there exist constants $c, C > 0$ with
$$
c|v|_{\bar g} \;\leq\; |v|_g \;\leq\; C|v|_{\bar g} \qquad \text{for all } x \in K,\ v \in T_xM,
$$
where $|\cdot|_{\bar g}$ is the Euclidean norm in the chart and $|\cdot|_g$ is the Riemannian norm.

---

# Convergent Strategy

**Problem class.** This is a *prove two topologies agree* problem — a classical point-set topology task with a twist. The [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Problem-Solving Strategy|problem-solving strategy]] of the topic page identifies the route: when comparing manifold-derived distances or topologies to chart-derived (Euclidean) ones, the technical input is the local comparability of $g$ with the Euclidean metric on compact pieces. Once you have $c |v|_{\bar g} \leq |v|_g \leq C |v|_{\bar g}$ uniformly, distances and balls in the two metrics pinch each other, and the two topologies have to coincide.

**Assumption pattern.** The hypothesis is a connected Riemannian manifold. *Connectedness* is needed so that $d_g$ is finite-valued (any two points can be joined by a piecewise smooth curve). The Riemannian metric provides the local-comparability lemma via continuity and compactness of the unit sphere in $\mathbb{R}^n$. So the assumption breaks into "local comparability available" plus "all pairs of points connectable", and both follow from the manifold being a connected smooth manifold with a Riemannian metric.

**Theorem routing.** Two implications need to be proved. *Manifold-open implies $d_g$-open*: given a manifold-open $U$ and $p \in U$, find a $d_g$-ball around $p$ inside $U$ — done by taking a small chart ball around $p$ inside $U$ and using local comparability to find a $d_g$-ball inside it. *$d_g$-open implies manifold-open*: given a $d_g$-open $W$ and $p \in W$, find a manifold-open neighborhood inside $W$ — done by taking a small chart ball that, by local comparability, has small $d_g$-diameter. Both run on the local-comparability lemma.

**Key decision point.** The non-obvious choice is *how small* to pick the chart ball at each step. For "manifold-open $\Rightarrow$ $d_g$-open", one wants a chart ball *contained in* $U$ (so its radius is bounded by the distance to the boundary of $U$); the local comparability lemma then converts this to a $d_g$-ball of radius $c \cdot \mathrm{rad}$. For the converse, one wants a chart ball *whose $d_g$-diameter is at most the prescribed $d_g$-radius*; this requires choosing the Euclidean radius small enough that $C \cdot \mathrm{rad} < d_g\text{-radius}$. The interplay between $c$ and $C$ in the comparability constants is the heart of the proof; both directions are needed.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Legal Operations|the topic page's Legal Operations]]:

7. **Bound a metric locally by the Euclidean one** (operation 7). The local-comparability lemma is the workhorse: on any compact set in a chart, $c |v|_{\bar g} \leq |v|_g \leq C |v|_{\bar g}$ with constants depending on the chart and the compact subset. This converts distance/length statements in $g$ to distance/length statements in the Euclidean metric, and vice versa, with universal constants.

3. **Construct a global Riemannian metric via partition of unity** (operation 3) — implicit, since we are assuming the metric exists. The same partition-of-unity infrastructure (paracompactness, smooth atlases) underlies the smooth structure on which the lemma rests.

5. **Verify positive-definiteness or non-degeneracy in coordinates** (operation 5) — implicit in the use of $|v|_g > 0$ for $v \neq 0$, which is what gives the lower bound $c > 0$.

---

# Hints

> [!note]- Hint 1
> Both implications reduce to the local-comparability lemma. The setup is: given $p \in M$, pick a chart $(V, \varphi)$ with $p \in V$, restrict to a small compact ball $\bar V_\varepsilon \subseteq V$ around $p$, and apply the lemma on $\bar V_\varepsilon$ to get constants $c, C > 0$. Then translate radii between $d_g$-balls and Euclidean balls using these constants.

> [!note]- Hint 2
> For "manifold-open $\Rightarrow$ $d_g$-open": given $U$ manifold-open and $p \in U$, find a Euclidean ball $V_\varepsilon$ centred at $p$ in a chart with $\bar V_\varepsilon \subseteq U$. Use the *lower* bound $c |v|_{\bar g} \leq |v|_g$ to argue that any curve leaving $V_\varepsilon$ has $g$-length at least $c\varepsilon$; hence the $d_g$-ball of radius $c\varepsilon$ is contained in $V_\varepsilon \subseteq U$.

> [!note]- Hint 3
> For "$d_g$-open $\Rightarrow$ manifold-open": given $W$ $d_g$-open with $p \in W$ and $\rho > 0$ with $B_{d_g}(p, \rho) \subseteq W$, find a Euclidean ball $V_\varepsilon$ centred at $p$ with the property that every $q \in V_\varepsilon$ satisfies $d_g(p, q) < \rho$. Use the *upper* bound $|v|_g \leq C |v|_{\bar g}$ to argue: the straight-line curve in the chart from $p$ to $q$ has Euclidean length less than $\varepsilon$, hence $g$-length less than $C\varepsilon$. Choose $\varepsilon < \rho/C$ to ensure $d_g(p, q) < \rho$.

---

# Solution

The proof breaks into two main steps, both running on the local-comparability lemma. Step 1 proves manifold-open implies $d_g$-open by lower-bounding $d_g$-distances using the lower bound $c$. Step 2 proves the converse by upper-bounding $d_g$-distances using the upper bound $C$. The decisive trick is recognising that the lemma's two-sided estimate pinches Euclidean and Riemannian distances together, so every neighborhood in one topology contains a neighborhood in the other.

**Step 1: Manifold-open implies $d_g$-open.**

Let $U \subseteq M$ be manifold-open and let $p \in U$. We must find $r > 0$ with $B_{d_g}(p, r) \subseteq U$.

> [!note]- Derivation
> Since $U$ is manifold-open and $p \in U$, there is a smooth chart $(V, \varphi)$ around $p$ with $V \subseteq U$. Choose a Euclidean ball $V_\varepsilon \subseteq V$ centred at $p$ — that is, a coordinate ball $\{x \in V : |x - \varphi(p)|_{\bar g} < \varepsilon\}$ — with the closure $\bar V_\varepsilon \subseteq V$. Such an $\varepsilon > 0$ exists because $V$ is open and $\varphi(p)$ is an interior point.
>
> Apply the local-comparability lemma on the compact set $\bar V_\varepsilon$: there exists $c > 0$ such that $c|v|_{\bar g} \leq |v|_g$ for every $x \in \bar V_\varepsilon$, $v \in T_x M$.
>
> We claim $B_{d_g}(p, c\varepsilon) \subseteq V_\varepsilon \subseteq U$. Suppose $q \notin V_\varepsilon$. Any piecewise smooth curve $\gamma : [a, b] \to M$ from $p$ to $q$ must exit $V_\varepsilon$ at some parameter (since $q \notin V_\varepsilon$). Let $t_0 = \inf\{t : \gamma(t) \notin V_\varepsilon\}$; by continuity, $\gamma(t_0) \in \partial V_\varepsilon$ (the Euclidean sphere of radius $\varepsilon$), and $\gamma|_{[a, t_0]}$ lies in $\bar V_\varepsilon$. Now
> $$
> L_g(\gamma) \;\geq\; L_g(\gamma|_{[a, t_0]}) \;=\; \int_a^{t_0} |\dot\gamma(t)|_g\, dt \;\geq\; c \int_a^{t_0} |\dot\gamma(t)|_{\bar g}\, dt \;\geq\; c \cdot d_{\bar g}(p, \gamma(t_0)) \;=\; c\varepsilon,
> $$
> where the last inequality uses that the Euclidean length of any curve from $p$ to $\gamma(t_0)$ is at least the Euclidean straight-line distance, which is $\varepsilon$ since $\gamma(t_0) \in \partial V_\varepsilon$.
>
> Taking infimum over all curves from $p$ to $q$: $d_g(p, q) \geq c\varepsilon$. So if $d_g(p, q) < c\varepsilon$, we have $q \in V_\varepsilon \subseteq U$. This is exactly the statement $B_{d_g}(p, c\varepsilon) \subseteq U$, so $U$ is $d_g$-open with witness $r = c\varepsilon > 0$.

**Step 2: $d_g$-open implies manifold-open.**

Let $W \subseteq M$ be $d_g$-open and let $p \in W$. We must find a manifold-open neighborhood $V_\varepsilon \subseteq W$ around $p$.

> [!note]- Derivation
> Since $W$ is $d_g$-open and $p \in W$, there exists $\rho > 0$ with $B_{d_g}(p, \rho) \subseteq W$. Choose a smooth chart $(V, \varphi)$ around $p$ and a Euclidean ball $V_r \subseteq V$ centred at $p$ with $\bar V_r \subseteq V$. Apply the local-comparability lemma on $\bar V_r$: there exists $C > 0$ such that $|v|_g \leq C|v|_{\bar g}$ for every $x \in \bar V_r$, $v \in T_x M$.
>
> Choose $\varepsilon < \min(r, \rho/C)$. We claim $V_\varepsilon \subseteq B_{d_g}(p, \rho) \subseteq W$.
>
> For any $q \in V_\varepsilon$, consider the straight-line curve $\gamma$ in the chart from $\varphi(p)$ to $\varphi(q)$. This curve has Euclidean length $L_{\bar g}(\gamma) = |\varphi(q) - \varphi(p)|_{\bar g} < \varepsilon$, and it stays inside $\bar V_\varepsilon \subseteq \bar V_r$ (a Euclidean ball is convex). By the comparability lemma,
> $$
> L_g(\gamma) \;=\; \int_a^b |\dot\gamma(t)|_g\, dt \;\leq\; C \int_a^b |\dot\gamma(t)|_{\bar g}\, dt \;=\; C \cdot L_{\bar g}(\gamma) \;<\; C\varepsilon \;\leq\; \rho.
> $$
> So $\gamma$ is a curve from $p$ to $q$ of $g$-length less than $\rho$, hence $d_g(p, q) \leq L_g(\gamma) < \rho$. Therefore $q \in B_{d_g}(p, \rho) \subseteq W$.
>
> Since $V_\varepsilon$ is manifold-open and contains $p$ and is contained in $W$, this shows $W$ is manifold-open at $p$. Repeating for every $p \in W$, $W$ is manifold-open.

> [!note]- Complete formal solution
> Let $(M, g)$ be a connected Riemannian manifold with Riemannian distance function $d_g$.
>
> We show: $U \subseteq M$ is manifold-open iff $d_g$-open.
>
> ($\Rightarrow$) Suppose $U$ is manifold-open and $p \in U$. Choose a smooth chart $(V, \varphi)$ with $p \in V \subseteq U$. Choose $\varepsilon > 0$ so that the Euclidean ball $V_\varepsilon \subseteq V$ around $\varphi(p)$ has closure $\bar V_\varepsilon \subseteq V$. By the local-comparability lemma, there exists $c > 0$ with $c|v|_{\bar g} \leq |v|_g$ for every $x \in \bar V_\varepsilon$, $v \in T_x M$.
>
> Any piecewise smooth curve from $p$ exiting $V_\varepsilon$ must cross the boundary $\partial V_\varepsilon$. Let $\gamma : [a, b] \to M$ be such a curve, with $\gamma(a) = p$ and $\gamma$ exiting $V_\varepsilon$ at parameter $t_0$ with $\gamma(t_0) \in \partial V_\varepsilon$. Then
> $$
> L_g(\gamma) \geq L_g(\gamma|_{[a, t_0]}) \geq c L_{\bar g}(\gamma|_{[a, t_0]}) \geq c |\varphi(\gamma(t_0)) - \varphi(p)|_{\bar g} = c\varepsilon.
> $$
> So $d_g(p, q) \geq c\varepsilon$ for $q \notin V_\varepsilon$. Hence $B_{d_g}(p, c\varepsilon) \subseteq V_\varepsilon \subseteq U$, showing $U$ is $d_g$-open at $p$.
>
> ($\Leftarrow$) Suppose $W$ is $d_g$-open and $p \in W$. There is $\rho > 0$ with $B_{d_g}(p, \rho) \subseteq W$. Choose a chart $(V, \varphi)$ around $p$, a Euclidean ball $V_r$ with $\bar V_r \subseteq V$, and constants $c, C > 0$ from the comparability lemma on $\bar V_r$. Choose $\varepsilon < \min(r, \rho/C)$.
>
> For $q \in V_\varepsilon$, the chart-straight-line curve from $p$ to $q$ has Euclidean length $|\varphi(q) - \varphi(p)|_{\bar g} < \varepsilon$ and lies in $\bar V_\varepsilon \subseteq \bar V_r$. By the upper bound, $L_g \leq C \cdot L_{\bar g} < C\varepsilon \leq \rho$. So $d_g(p, q) < \rho$, hence $q \in B_{d_g}(p, \rho) \subseteq W$. Thus $V_\varepsilon \subseteq W$, and $V_\varepsilon$ is a manifold-open neighborhood of $p$. Repeating for every $p \in W$ shows $W$ is manifold-open.
>
> Combining both directions: manifold-open and $d_g$-open subsets of $M$ are the same family, so the two topologies coincide. $\blacksquare$

---

# Key Takeaways

**Local comparability of metrics is the engine of topology coincidence.** The technical heart of this exercise is the local-comparability lemma: on any compact set in a chart, $c |v|_{\bar g} \leq |v|_g \leq C |v|_{\bar g}$ uniformly. This pinches the Riemannian metric between scaled Euclidean metrics, and the same pinch applies to distances (by integration) and to topology (by taking balls in the two distances). The reusable lesson: whenever a "manifold-intrinsic" quantity must be compared to a "chart-extrinsic" one (Euclidean), the right tool is uniform comparability on compact pieces; the rest is bookkeeping with the constants $c$ and $C$. The same pattern shows up in Lipschitz comparison of metrics, equivalence of norms on finite-dimensional vector spaces (any two norms on $\mathbb{R}^n$ are equivalent), and the comparison theorems in Riemannian geometry (sectional curvature bounds give comparability with model spaces). Recognise comparable-on-compact-sets as a setup that licences the entire metric-topological machinery.

**Topology coincidence is what makes Riemannian-analytic methods rigorous.** Once we know the metric topology generated by $d_g$ equals the original manifold topology, every concept of metric-space topology — Cauchy sequences, completeness, total boundedness, open balls, Heine–Borel — is now available on the manifold with the same meaning it has in $\mathbb{R}^n$. We can talk about a sequence "converging in $d_g$" or "converging in the manifold sense", and the two are the same. This is what makes geometric analysis on manifolds — Sobolev spaces, $L^p$ spaces, harmonic maps, geometric PDE — well-defined. The reusable point: when the metric (in the metric-space sense) and the original topology agree, you can use both languages interchangeably; when they would disagree, one would have to commit to one or the other.

**The argument is a model for proofs in geometric topology.** The structure of this proof — pick a chart, restrict to a compact piece, apply a comparability lemma, conclude pointwise — recurs throughout differential geometry. The argument is local (works in a chart neighborhood), uses smoothness through the metric tensor, and exploits compactness for uniform bounds. The same template applies to: proving that two Riemannian metrics with the same smooth structure define the same topology; proving that smooth maps are continuous; proving that integral curves of a vector field are unique (the comparability lemma is used to bound the divergence of two purported solutions). The takeaway is the architecture: local + compactness + comparability + uniform constants gives global topological conclusions.

**Cross-link to companion exercises:** This is the topology-foundations exercise of the chapter. The downstream consequences (Hopf–Rinow, completeness, metrisability of manifolds) build on this single result, and the technical lemma it relies on is reused throughout Riemannian geometry.

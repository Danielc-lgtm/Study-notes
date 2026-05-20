---
type: exercise
subject: topology
difficulty: "⭐"
prereqs:
  - "Def - Metric Space"
tags: [analysis, topology]
---

# Problem Statement

Let $(X, d)$ be a metric space. Define two new candidate metrics on $X$:
$$d'(x, y) = \min(d(x, y), 1), \qquad d''(x, y) = \frac{d(x, y)}{1 + d(x, y)}.$$

(a) Show that $d'$ and $d''$ are metrics on $X$.

(b) Show that both $d'$ and $d''$ are **bounded** (every distance is at most $1$).

(c) Show that $d'$ and $d''$ are **topologically equivalent** to $d$: each induces the same topology on $X$ as $d$.

**Recall:**

A **metric** on a set $X$ is a function $d : X \times X \to [0, \infty)$ with (i) $d(x, y) = 0 \iff x = y$, (ii) $d(x, y) = d(y, x)$, (iii) $d(x, z) \leq d(x, y) + d(y, z)$ (triangle inequality). A metric is **bounded** if $\sup_{x, y} d(x, y) < \infty$.

Two metrics $d, d'$ on the same set $X$ are **topologically equivalent** if they induce the same topology — equivalently, if every open ball of $d$ contains an open ball of $d'$ around the same center and vice versa. The two metrics need not be uniformly equivalent (Lipschitz comparable globally); topological equivalence is a strictly weaker condition.

---

# Convergent Strategy

**Problem class.** A *boundedness-of-metrics* problem: given an unbounded metric, produce a bounded one with the same topology. The standard application is enabling countable infinite products (the metric $\sum_n 2^{-n} d_n(x_n, y_n)$ on $\prod_n X_n$ requires the $d_n$ to be uniformly bounded to converge). The same trick is used in the [[Thm - Urysohn Metrization Theorem|Urysohn metrization theorem]] to embed a second countable Hausdorff regular space into $[0, 1]^\mathbb{N}$.

**Assumption pattern.** Two natural choices: $d' = \min(d, 1)$ truncates large distances and is geometrically immediate; $d'' = d/(1+d)$ smoothly squashes large distances into $[0, 1)$ via the diffeomorphism $t \mapsto t/(1+t)$ from $[0, \infty)$ to $[0, 1)$. The triangle inequality is automatic for $d'$ (a case-split on which terms are clipped) but requires a small computation for $d''$ (concavity of $t \mapsto t/(1+t)$).

**Theorem routing.** For topological equivalence, the cleanest argument is *ball comparison for small radius*: for $\varepsilon < 1$, $d'(x, y) < \varepsilon \iff d(x, y) < \varepsilon$ (the truncation is invisible at small scales), so the small-radius balls coincide. The same idea works for $d''$: for $\varepsilon < 1$, $d''(x, y) < \varepsilon \iff d(x, y) < \varepsilon/(1-\varepsilon)$, so each small $d''$-ball is a small $d$-ball of a (different but equivalent) radius. Since the small-radius balls form a neighborhood basis, equality of small-radius balls implies equality of topologies.

**Key decision point.** The argument simplifies enormously by noting that *small balls only* need to be compared — the topology is determined by any neighborhood basis at each point. There is no need to compare arbitrary radii.

---

# Legal Operations Used

1. **Bound a metric by truncation or by squashing through a bounded diffeomorphism.** $\min(d, c)$ caps the metric at $c$; $d/(1 + d)$ smoothly compresses into $[0, 1)$. Both preserve the topology and reduce uniformity issues.

2. **Compare topologies via small-ball comparison.** Two metrics induce the same topology iff every small ball of one contains a small ball of the other around each point — and "small" can be made as small as desired.

3. **Compose the metric with a monotonic concave function preserving $0$.** The triangle inequality for $d'$ and $d''$ comes from $\min$ being concave and $t/(1+t)$ being concave; in general, $f \circ d$ is a metric for any concave $f : [0, \infty) \to [0, \infty)$ with $f(0) = 0$, $f$ strictly increasing.

---

# Hints

> [!note]- Hint 1
> *Triangle inequality for $d'$.* Case-split on whether each pairwise distance is $< 1$ or $\geq 1$. If $d(x, z) \geq 1$ then $d'(x, z) = 1 \leq d'(x, y) + d'(y, z)$ since either $d'(x, y) + d'(y, z) \geq 1$ or both are $< 1$ and $\geq d(x, y) + d(y, z) \geq d(x, z) \geq 1$, contradiction.

> [!note]- Hint 2
> *Triangle inequality for $d''$.* The function $\phi(t) = t/(1+t)$ is concave and increasing on $[0, \infty)$. Then $d''(x, z) = \phi(d(x, z)) \leq \phi(d(x, y) + d(y, z))$. Use $\phi(a + b) \leq \phi(a) + \phi(b)$ — true because $\phi(a + b) = (a+b)/(1+a+b) \leq a/(1+a) + b/(1+b) = \phi(a) + \phi(b)$ after clearing denominators.

> [!note]- Hint 3
> *Topological equivalence.* For $\varepsilon < 1$, the $d'$-ball of radius $\varepsilon$ around $x$ equals the $d$-ball of radius $\varepsilon$ around $x$. Both metrics have the same small-radius balls at every point, hence the same topology.

---

# Solution

The trick is the same in both cases: take the unbounded $d$ and compose it with a monotonic concave function $\phi : [0, \infty) \to [0, 1]$ with $\phi(0) = 0$. Concavity gives the triangle inequality; monotonicity and the small-scale behavior $\phi(t) \approx t$ give topological equivalence.

**Step 1: $d'$ is a metric, bounded by $1$.**

The non-negativity, identity-of-indiscernibles, and symmetry axioms are immediate from those of $d$. The triangle inequality follows from a short case analysis.

> [!note]- Derivation
> *Non-negativity, symmetry, identity.* $d' = \min(d, 1) \geq 0$; $d'(x, y) = 0 \iff \min(d(x, y), 1) = 0 \iff d(x, y) = 0 \iff x = y$; $d'(x, y) = \min(d(x, y), 1) = \min(d(y, x), 1) = d'(y, x)$.
>
> *Triangle inequality.* For $x, y, z \in X$, we need $d'(x, z) \leq d'(x, y) + d'(y, z)$.
>
> Case (i): $d'(x, y) + d'(y, z) \geq 1$. Then $d'(x, z) \leq 1 \leq d'(x, y) + d'(y, z)$, done.
>
> Case (ii): $d'(x, y) + d'(y, z) < 1$. Then both $d'(x, y), d'(y, z) < 1$, so $d'(x, y) = d(x, y)$ and $d'(y, z) = d(y, z)$. Triangle for $d$ gives $d(x, z) \leq d(x, y) + d(y, z) < 1$, so $d'(x, z) = d(x, z) \leq d(x, y) + d(y, z) = d'(x, y) + d'(y, z)$.
>
> *Bounded.* $d'(x, y) = \min(d(x, y), 1) \leq 1$ for all $x, y$.

**Step 2: $d''$ is a metric, bounded by $1$.**

The map $\phi(t) = t/(1+t)$ is a concave, strictly increasing diffeomorphism of $[0, \infty)$ onto $[0, 1)$. The metric axioms for $d'' = \phi \circ d$ follow from properties of $\phi$.

> [!note]- Derivation
> *Properties of $\phi$.* $\phi(0) = 0$. $\phi'(t) = 1/(1+t)^2 > 0$, so $\phi$ is strictly increasing. $\phi''(t) = -2/(1+t)^3 < 0$, so $\phi$ is strictly concave. As $t \to \infty$, $\phi(t) \to 1$.
>
> *Non-negativity, symmetry, identity.* Immediate from those of $d$ and the fact that $\phi(0) = 0$, $\phi > 0$ on $(0, \infty)$.
>
> *Triangle inequality.* We need $\phi(d(x, z)) \leq \phi(d(x, y)) + \phi(d(y, z))$. Since $\phi$ is increasing and $d(x, z) \leq d(x, y) + d(y, z)$, $\phi(d(x, z)) \leq \phi(d(x, y) + d(y, z))$. So it suffices to show *subadditivity*: $\phi(a + b) \leq \phi(a) + \phi(b)$ for $a, b \geq 0$.
>
> Compute:
> $$\phi(a) + \phi(b) - \phi(a + b) = \frac{a}{1+a} + \frac{b}{1+b} - \frac{a + b}{1 + a + b}.$$
> Bring to common denominator $(1+a)(1+b)(1+a+b)$. Some patient algebra (or noting that $\phi$ concave with $\phi(0) = 0$ implies $\phi$ subadditive: $\phi(a + b) = \phi(\frac{a+b}{1+\varepsilon}(1+\varepsilon)) \leq \dots$, but the direct algebraic route is cleaner):
> $$\phi(a) + \phi(b) - \phi(a+b) = \frac{a(1+b)(1+a+b) + b(1+a)(1+a+b) - (a+b)(1+a)(1+b)}{(1+a)(1+b)(1+a+b)}.$$
> Numerator: expand and simplify to $2ab + a^2b + ab^2 = ab(2 + a + b) \geq 0$. Hence $\phi(a) + \phi(b) \geq \phi(a+b)$ for $a, b \geq 0$.
>
> *Bounded.* $\phi(t) < 1$ for all $t \geq 0$, so $d'' < 1$.

**Step 3: $d'$ and $d$ induce the same topology.**

For every $\varepsilon < 1$ and every $x$, the ball $B^{d'}_\varepsilon(x)$ equals the ball $B^d_\varepsilon(x)$. So the two metrics have a common neighborhood basis at every point — they induce the same topology.

> [!note]- Derivation
> Fix $x \in X$ and $\varepsilon < 1$. We claim
> $$B^{d'}_\varepsilon(x) = \{y : d'(x, y) < \varepsilon\} = \{y : \min(d(x, y), 1) < \varepsilon\}.$$
> Since $\varepsilon < 1$, $\min(d(x, y), 1) < \varepsilon$ iff $d(x, y) < \varepsilon$. So $B^{d'}_\varepsilon(x) = B^d_\varepsilon(x)$.
>
> Now, the topology induced by $d$ has basis $\{B^d_\varepsilon(x) : x \in X, \varepsilon > 0\}$, equivalently $\{B^d_\varepsilon(x) : x \in X, 0 < \varepsilon < 1\}$ (the small-radius balls form a basis already). The same with $d'$. Since the small-radius balls coincide, the bases coincide, so the topologies coincide.

**Step 4: $d''$ and $d$ induce the same topology.**

The function $\phi$ is a homeomorphism $[0, \infty) \to [0, 1)$, so it carries small-radius $d$-balls to small-radius $d''$-balls and vice versa.

> [!note]- Derivation
> *Small $d''$-ball contains a small $d$-ball.* Fix $\varepsilon > 0$. Choose $\delta > 0$ with $\phi(\delta) < \varepsilon$; concretely $\delta = \varepsilon/(1-\varepsilon)$ for $\varepsilon < 1$, so $\phi(\delta) = (\varepsilon/(1-\varepsilon))/(1 + \varepsilon/(1-\varepsilon)) = \varepsilon$. Then $d(x, y) < \delta$ implies $d''(x, y) = \phi(d(x, y)) < \phi(\delta) = \varepsilon$, so $B^d_\delta(x) \subseteq B^{d''}_\varepsilon(x)$.
>
> *Small $d$-ball contains a small $d''$-ball.* Fix $\delta > 0$. Choose $\varepsilon > 0$ with $\phi^{-1}(\varepsilon) = \varepsilon/(1 - \varepsilon) < \delta$ (well-defined for $\varepsilon < 1$). Then $d''(x, y) < \varepsilon$ implies $\phi(d(x, y)) < \varepsilon$, so $d(x, y) < \phi^{-1}(\varepsilon) < \delta$, giving $B^{d''}_\varepsilon(x) \subseteq B^d_\delta(x)$.
>
> So every $d$-ball contains a $d''$-ball, and every $d''$-ball contains a $d$-ball — same topology.

> [!note]- Complete formal solution
> *(a, b) Metrics, bounded.* $d' = \min(d, 1)$, $d'' = d/(1+d)$: non-negativity, symmetry, identity-of-indiscernibles immediate from $d$. Triangle for $d'$: case split on whether $d'(x, y) + d'(y, z) \geq 1$. Triangle for $d''$: $\phi(t) = t/(1+t)$ is increasing with $\phi(a + b) \leq \phi(a) + \phi(b)$ (algebraic). Both are bounded by $1$.
>
> *(c) Topological equivalence.* For $\varepsilon < 1$, $B^{d'}_\varepsilon(x) = B^d_\varepsilon(x)$, so $d'$ and $d$ have a common neighborhood basis at every point. For $d''$, $\phi$ being a homeomorphism $[0, \infty) \to [0, 1)$ converts small $d$-balls to small $d''$-balls; every $d$-ball contains a $d''$-ball and vice versa. Same topology. $\blacksquare$

---

# Key Takeaways

**Boundedness of a metric is *not* a topological property — it is a property of the metric.** The same topological space can carry both bounded and unbounded metrics. This is why "completeness" (which is metric-dependent) and "boundedness" (metric-dependent) are different from "complete metrizability" and "bounded metrizability" — the latter are topological. This is part of the broader theme of being careful about which properties depend on the metric vs. on the topology: completeness, total boundedness, uniform continuity, and Lipschitz-ness are all metric-dependent; compactness, connectedness, Hausdorffness, and continuity are all topological.

**The reduction to a bounded equivalent metric is the standard preparation for forming infinite products.** The countable product metric $D(x, y) = \sum_n 2^{-n} d_n(x_n, y_n)$ converges precisely when the individual $d_n$ are bounded (say by $1$). Without this step, one cannot define a metric on $\prod_n X_n$ at all from the factor metrics; with it, every countable product of metric spaces becomes a metric space. This is the metric structure assumed implicitly in the [[Thm - Urysohn Metrization Theorem|Urysohn metrization theorem]] and in much of analysis on infinite-dimensional Polish spaces. The trigger to recognize: any time you want to form an infinite metric product, first reduce each factor to a bounded equivalent metric.

**$\min(d, 1)$ and $d/(1+d)$ are two natural choices, and the right one depends on the situation.** $\min(d, 1)$ has a *sharp* threshold at $1$ and is identically $1$ for far-apart points — convenient for proofs by cases but discontinuous in its derivative if one is differentiating. $d/(1+d)$ is *smooth* (analytic, in fact) and never quite reaches $1$ — convenient when you want the metric to behave nicely under analysis, but the explicit constants are slightly awkward. In analysis, the smooth squashing $d/(1+d)$ is generally preferred; in pure topology, the truncation $\min(d, 1)$ is simpler.

**The general principle: $\phi \circ d$ is a metric whenever $\phi : [0, \infty) \to [0, \infty)$ is concave, strictly increasing, and $\phi(0) = 0$.** Concavity gives subadditivity ($\phi(a + b) \leq \phi(a) + \phi(b)$), which combined with monotonicity gives the triangle inequality. Strict increase plus $\phi(0) = 0$ preserves the identity-of-indiscernibles axiom. This is the abstract version of what is happening with $\min(d, 1)$ (concave at the corner) and $d/(1+d)$ (strictly concave). Other examples: $\sqrt{d}$ is a metric (the "square root metric"); $\log(1 + d)$ is a metric; $d^p$ for $0 < p < 1$ is a metric (but $d^p$ for $p > 1$ is *not*, because then $\phi(t) = t^p$ is convex, not concave). The standard exception to remember: $d^2$ is not a metric on $\mathbb{R}$ — the triangle inequality fails for $0, 1, 2$ (squared distances $1, 4, 1$ violate $4 \leq 1 + 1$).

**Topological equivalence is much weaker than uniform/Lipschitz equivalence.** $d$ and $d'$ here induce the same topology but $d$ is unbounded while $d'$ is bounded by $1$ — no Lipschitz constant $L$ can satisfy $d(x, y) \leq L \cdot d'(x, y)$ globally. Topological equivalence asks only that the *neighborhood bases* agree at each point, which is a strictly weaker condition than uniform comparability of the metrics. The trigger-reaction: when you read "topologically equivalent metrics", do *not* assume uniform comparability; whenever uniform continuity or uniform convergence enters the picture, the difference matters. Conversely, when topological properties (continuity of a function, compactness of a subset) are what is being claimed, topological equivalence is enough.

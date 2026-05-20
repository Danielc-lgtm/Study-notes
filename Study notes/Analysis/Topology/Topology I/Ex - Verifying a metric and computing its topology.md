---
type: exercise
subject: topology
difficulty: "⭐"
prereqs:
  - "Def - Metric Space"
  - "Def - Open and Closed Sets in a Metric Space"
  - "Def - Neighbourhood and Neighbourhood Basis"
tags: [analysis, topology]
---

# Problem Statement

Let $C[0,1]$ denote the set of continuous real-valued functions on $[0,1]$. Define
$$d(f, g) = \int_0^1 |f(t) - g(t)|\, dt.$$

1. Show that $d$ is a [[Def - Metric Space|metric]] on $C[0,1]$.
2. Identify a [[Def - Neighbourhood and Neighbourhood Basis|neighbourhood basis]] at the zero function $f = 0$, expressed as a family of explicit open balls.
3. Exhibit a sequence $f_n \in C[0,1]$ with $d(f_n, 0) \to 0$ but $f_n(0) \not\to 0$, showing that convergence in this metric does *not* imply pointwise convergence.

**Recall:**

The objects in play are the metric axioms, the open-ball construction, and the notion of a neighbourhood basis at a point.

![[Def - Metric Space#The Definition]]

In short, a [[Def - Metric Space|metric]] on a set $X$ is a function $d : X \times X \to \mathbb{R}_{\geq 0}$ satisfying positivity ($d(x,y) = 0 \iff x = y$), symmetry ($d(x,y) = d(y,x)$), and the triangle inequality ($d(x,z) \leq d(x,y) + d(y,z)$). An [[Def - Open and Closed Sets in a Metric Space|open ball]] is $B_\varepsilon(x) = \{y : d(x,y) < \varepsilon\}$, and a [[Def - Neighbourhood and Neighbourhood Basis|neighbourhood basis at a point]] is a collection of neighbourhoods such that every neighbourhood of the point contains some element of the collection.

For continuous functions on a compact interval, all integrals are finite — $|f - g|$ is continuous on $[0,1]$, hence bounded, hence Riemann-integrable. The only subtlety in showing $d$ is a metric is **positivity**: $\int_0^1 |f - g| = 0$ does not in general force $f = g$ pointwise — but for *continuous* functions it does.

---

# Convergent Strategy

**Problem class.** Verifying that a specific function is a metric, then describing the induced topology near a point. This is the prototypical first encounter with non-Euclidean metric spaces and is calibrated to expose the difference between metric convergence and pointwise convergence.

**Assumption pattern.** The candidate metric is given by an *integral* of a difference. The two non-trivial axioms — positivity and the triangle inequality — each route through a single standard observation: positivity uses continuity (to upgrade "zero integral" to "zero function"), and the triangle inequality is the pointwise triangle inequality integrated.

**Theorem routing.** Positivity: continuity of $|f - g|$ plus the standard analysis lemma that a nonnegative continuous function with zero integral is identically zero. Symmetry: trivial from $|a - b| = |b - a|$. Triangle inequality: pointwise $|f - h| \leq |f - g| + |g - h|$ followed by monotonicity of the integral. The neighbourhood basis is then just the open balls $B_\varepsilon(0)$ for $\varepsilon > 0$ — a standard fact in any metric space — and the counterexample to pointwise convergence is a *tent function* whose mass shrinks to zero but whose value at one specific point stays large.

**Key decision point.** The positivity step is the only one where the structure of $C[0,1]$ matters. If we had instead taken $L^1[0,1]$ (the space of integrable functions modulo a.e. equality), the integral would be a *seminorm* rather than a norm on functions — two functions agreeing almost everywhere have integral distance zero. The metric only works on $C[0,1]$ because continuity rules out a.e. equality without genuine equality.

---

# Legal Operations Used

This solution deploys the following operations from [[Topology I — §1–3 Metric and Topological Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Verify metric axioms directly from the definition.** Check positivity (with the continuity argument), symmetry (one line), and the triangle inequality (pointwise plus integral monotonicity).

2. **Identify a neighbourhood basis via open balls.** In any metric space, the open balls $\{B_\varepsilon(x) : \varepsilon > 0\}$ — or equivalently $\{B_{1/n}(x) : n \in \mathbb{N}\}$ — form a neighbourhood basis at $x$. This is built into the construction of the metric topology.

3. **Construct an escaping-mass counterexample.** When proving that two notions of convergence diverge, look for a sequence whose *mass escapes* in a way that one mode of convergence sees and the other does not. Here, the mass of $f_n$ concentrates into a thinner and thinner spike at the origin: the integral sees the shrinking width, the pointwise evaluation at $0$ sees only the height.

---

# Hints

> [!note]- Hint 1
> The only non-trivial axiom is positivity. If $f, g \in C[0,1]$ and $\int_0^1 |f - g| = 0$, why must $f = g$ everywhere? Use continuity of $|f-g|$ at a point where it would be nonzero.

> [!note]- Hint 2
> In any [[Def - Metric Space|metric space]], the collection $\{B_\varepsilon(x) : \varepsilon > 0\}$ is automatically a neighbourhood basis at $x$, by the definition of the metric topology. A countable subfamily $\{B_{1/n}(x) : n \in \mathbb{N}\}$ also works.

> [!note]- Hint 3
> For the counterexample, draw a triangle of height $1$ and base $[0, 2/n]$ with peak at $t = 1/n$. The integral is $\frac{1}{2} \cdot \frac{2}{n} \cdot 1 = \frac{1}{n}$. But what is $f_n(0)$? And what is $f_n(0)$ in the limit if we modify the construction so the peak sits at $t = 0$?

---

# Solution

The problem splits cleanly into three independent verifications, each illustrating a different aspect of how a metric structures a function space.

**Step 1: $d$ is a metric on $C[0,1]$.**

Positivity, symmetry, and the triangle inequality each reduce to a one-line standard argument. The only point requiring care is upgrading "$\int |f - g| = 0$" to "$f = g$"; this uses continuity.

> [!note]- Derivation
> *Nonnegativity.* The integrand $|f - g|$ is nonnegative, so $d(f, g) \geq 0$.
>
> *Positivity.* If $f = g$ then $|f - g| \equiv 0$ and $d(f, g) = 0$. Conversely, suppose $d(f, g) = 0$ but $f \neq g$; we derive a contradiction. Pick $t_0 \in [0, 1]$ with $f(t_0) \neq g(t_0)$, and let $c = |f(t_0) - g(t_0)| > 0$. Since $|f - g|$ is continuous at $t_0$ (composition and difference of continuous functions), there exists $\delta > 0$ such that $|f(t) - g(t)| > c/2$ for every $t$ in $[0,1] \cap (t_0 - \delta, t_0 + \delta)$. The intersection has length at least $\delta$ (take the smaller of $\delta$ and the distance to the nearest endpoint of $[0,1]$, and shrink $\delta$ if necessary). Hence
> $$\int_0^1 |f - g|\, dt \geq \int_{t_0 - \delta}^{t_0 + \delta} \frac{c}{2}\, dt \geq \delta \cdot \frac{c}{2} > 0,$$
> contradicting $d(f, g) = 0$. So $f = g$.
>
> *Symmetry.* $|f(t) - g(t)| = |g(t) - f(t)|$ pointwise, so the integrals agree.
>
> *Triangle inequality.* For each $t \in [0, 1]$, $|f(t) - h(t)| \leq |f(t) - g(t)| + |g(t) - h(t)|$ by the triangle inequality on $\mathbb{R}$. Integrating both sides over $[0, 1]$ (monotonicity of the integral) gives $d(f, h) \leq d(f, g) + d(g, h)$.

**Step 2: A neighbourhood basis at $f = 0$.**

The open balls $B_\varepsilon(0) = \{f \in C[0,1] : \int_0^1 |f| < \varepsilon\}$ for $\varepsilon > 0$ form a neighbourhood basis at $0$. The countable subfamily $\{B_{1/n}(0)\}_{n \geq 1}$ also works, so $C[0,1]$ with this metric is [[Def - First and Second Countable|first countable]].

> [!note]- Derivation
> By the [[Def - Open and Closed Sets in a Metric Space|definition of the open-ball metric topology]], a set $U$ is open in $C[0,1]$ if and only if for every $f \in U$ there exists $\varepsilon > 0$ such that $B_\varepsilon(f) \subseteq U$. In particular, every open set containing $0$ contains some ball $B_\varepsilon(0)$. Conversely, every $B_\varepsilon(0)$ is open (open balls are open in any metric space, by the triangle inequality). So the collection $\{B_\varepsilon(0) : \varepsilon > 0\}$ is a [[Def - Neighbourhood and Neighbourhood Basis|neighbourhood basis at 0]].
>
> Concretely:
> $$B_\varepsilon(0) = \left\{f \in C[0,1] : \int_0^1 |f(t)|\, dt < \varepsilon\right\}.$$
> Each such ball is exactly the set of continuous functions whose $L^1$-norm is less than $\varepsilon$.
>
> Since $\varepsilon$ ranges over the positive reals and any neighbourhood basis can be subsampled along a sequence $\varepsilon_n \to 0$, the countable family $\{B_{1/n}(0) : n \geq 1\}$ is also a neighbourhood basis — every neighbourhood of $0$ contains some $B_\varepsilon(0)$, hence some $B_{1/n}(0)$ once $1/n < \varepsilon$.

**Step 3: Convergence in $d$ does not imply pointwise convergence.**

Define the tent functions
$$f_n(t) = \begin{cases} 1 - nt & \text{if } 0 \leq t \leq 1/n, \\ 0 & \text{if } 1/n \leq t \leq 1.\end{cases}$$
Then $f_n \in C[0,1]$ (the two pieces agree at $t = 1/n$), $d(f_n, 0) = \frac{1}{2n} \to 0$, but $f_n(0) = 1$ for every $n$. So $d(f_n, 0) \to 0$ while $f_n(0) \not\to 0$.

> [!note]- Derivation
> Each $f_n$ is piecewise linear and continuous: the linear piece on $[0, 1/n]$ has value $1$ at $t = 0$ and value $0$ at $t = 1/n$; the constant piece on $[1/n, 1]$ has value $0$; the two pieces agree at $t = 1/n$. So $f_n \in C[0,1]$.
>
> The integral $\int_0^1 |f_n|\, dt$ is the area under the triangle with vertices $(0, 1)$, $(1/n, 0)$, and $(0, 0)$ — base $1/n$, height $1$, area $\frac{1}{2n}$. So $d(f_n, 0) = \frac{1}{2n} \to 0$.
>
> But $f_n(0) = 1 - n \cdot 0 = 1$ for every $n$, so the sequence of values at $0$ is the constant sequence $1$, which does not converge to $0$.

> [!note]- Complete formal solution
> **(1) Metric axioms.** Nonnegativity is automatic. For positivity, if $\int |f - g| = 0$ with $f, g$ continuous and $f(t_0) \neq g(t_0)$ for some $t_0$, then $|f - g| > c/2 > 0$ on an interval about $t_0$ (continuity), forcing the integral to be positive — contradiction. Symmetry is from $|a - b| = |b - a|$. Triangle inequality: $|f(t) - h(t)| \leq |f(t) - g(t)| + |g(t) - h(t)|$ integrates to $d(f, h) \leq d(f, g) + d(g, h)$.
>
> **(2) Neighbourhood basis at $0$.** $\{B_\varepsilon(0) : \varepsilon > 0\} = \{f : \int |f| < \varepsilon\}$ is a neighbourhood basis at $0$ by the definition of the metric topology; the countable subfamily $\{B_{1/n}(0)\}$ also is one.
>
> **(3) Non-pointwise convergence.** Set $f_n(t) = \max(1 - nt, 0)$, a tent function with $f_n(0) = 1$ and $\int |f_n| = \frac{1}{2n} \to 0$. Then $f_n \to 0$ in $d$ but $f_n(0) = 1 \not\to 0$. $\blacksquare$

---

# Key Takeaways

**The positivity axiom is the only one where the *space* matters: it is where "almost-equality" must be upgraded to "equality".** On $C[0,1]$ the upgrade works because of continuity — if a continuous function is nonzero at one point it is nonzero on a neighbourhood, and a neighbourhood has positive measure. The same definition $d(f, g) = \int |f - g|$ on the *larger* space of integrable functions $L^1[0,1]$ is only a *semi*metric: distinct functions can have zero distance (they differ only on a measure-zero set). To upgrade the semimetric to a genuine metric on $L^1[0,1]$, one quotients by the equivalence relation $f \sim g \iff f = g$ almost everywhere — and this is exactly the construction of the $L^1$ space. The general lesson: an integral always gives at most a semimetric on a space of functions; the question of whether it is a genuine metric is the question of whether the space is small enough to rule out distinct functions agreeing a.e.

**The neighbourhood basis at a point of a metric space is *always* the collection of open balls, and a *countable* subfamily $\{B_{1/n}(x)\}$ always works.** This is why every metric space is automatically [[Def - First and Second Countable|first countable]] — a property that, in general topological spaces, has to be assumed. The countable neighbourhood basis is what lets sequence-based arguments work: in a metric space, $x \in \overline{A}$ if and only if some sequence in $A$ converges to $x$, and a function is continuous at $x$ if and only if it preserves sequential convergence. None of this requires the metric *axioms* per se; it requires only the countable neighbourhood basis. In a general topological space, the analogous statements require nets or filters because there may be no countable neighbourhood basis at all.

**The tent-function counterexample is the canonical witness that "$L^1$-norm convergence does not imply pointwise convergence" — and the mechanism is escaping mass.** Read off the construction: the area shrinks because the *width* of the tent goes to zero, but the *height* stays $1$. The integral metric sees only the product of width and height, so it goes to zero; the evaluation at the peak sees only the height, so it does not. This is the same mechanism that makes a.s. convergence and $L^p$ convergence incomparable in [[Ex - The hierarchy of convergence modes|probability theory]] — the spike $n \mathbf{1}_{[0, 1/n]}$ converges a.s. to zero but not in $L^1$, mass escaping into a thin tall spike. Whenever you face two notions of convergence and want to show one does not imply the other, the first thing to try is an "escaping-mass" sequence: a feature (mass, height, derivative) that stays bounded away from zero while another feature (integral, width, value) goes to zero.

**Different metrics on the *same* set encode different "closeness", and the integral metric is genuinely weaker than the sup metric on $C[0,1]$.** The pointwise value at a specific point is a *continuous* functional under the sup metric — $|f(0) - g(0)| \leq \sup_t |f - g| = d_\infty(f, g)$ — but is *not* continuous under the integral metric, as the tent example shows. This means the space of continuous functions has a finer topology under the sup metric than under the integral metric. The companion exercise [[Ex - Sup metric versus L1 metric on C[0,1]]] makes this comparison rigorous and shows the two metrics are not topologically equivalent. The lesson is that on a single set there can be a *hierarchy* of metrics, each producing a different topology, and the choice of metric controls which functionals are continuous — a theme that becomes structural in functional analysis, where the choice of topology on a Banach space (norm topology versus weak topology versus weak-$*$ topology) determines which operators are continuous and which limits exist.

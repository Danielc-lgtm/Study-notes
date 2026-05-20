---
type: definition
subject: topology
prereqs:
  - "Def - Metric Space"
tags: [analysis, topology]
---

# Notation

Throughout, $(X, d)$ is a metric space. For $x \in X$ and $\varepsilon > 0$, the **open ball** of radius $\varepsilon$ about $x$ is $B_\varepsilon(x) = \{y \in X : d(x, y) < \varepsilon\}$, with strict inequality. The **closed ball** is $\overline{B_\varepsilon(x)} = \{y \in X : d(x, y) \leq \varepsilon\}$, with non-strict inequality. We will be careful below: the notation $\overline{B_\varepsilon(x)}$ here means the closed *ball* (the set defined by $\leq$), not the topological *closure* of $B_\varepsilon(x)$ — these two coincide in $\mathbb{R}^n$ but, as we will see, not always. We denote the collection of open sets by $\tau$ and the complement of $A \subseteq X$ by $X \setminus A$. For the full registry of symbols see [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Axiom Motivation

We have a metric and we have the $\varepsilon$–$\delta$ definition of continuity. The question is: what is the *minimum* data that lets us state and verify continuity? The $\varepsilon$–$\delta$ definition mentions specific balls, but a moment's thought shows that the *content* of the definition is "$f$ stays close to $f(x_0)$ when $x$ stays close to $x_0$", and "close" is just shorthand for "inside some ball". So we are really asking: what is the structural feature of $(X, d)$ that captures *closeness*?

The right answer turns out to be: a *family* of subsets, the **open sets**, with the property that every point in such a set has "wiggle room" — a neighbourhood of nonzero radius inside the set. The intuition is that an open set is one in which every point can move a little bit in any direction and stay in the set. The points on the boundary of a closed disc, say, can move in some directions and stay in the disc, but in other directions they leave it. So the closed disc is *not* open. The open disc, on the other hand, is open: every interior point has a small ball of wiggle room. The defining property of an open set is therefore: *every point of $U$ is the centre of some open ball contained in $U$*.

The most basic open sets are the open balls themselves, and the first thing to check is that they really are open in our sense — every point of $B_\varepsilon(x)$ has its own ball in $B_\varepsilon(x)$. This is where the triangle inequality earns its keep: if $y \in B_\varepsilon(x)$, set $\delta = \varepsilon - d(x, y) > 0$, and then any $z \in B_\delta(y)$ satisfies $d(z, x) \leq d(z, y) + d(y, x) < \delta + d(y, x) = \varepsilon$. The ball $B_\delta(y)$ lies inside $B_\varepsilon(x)$. So open balls are open; this is the engine that makes the whole open-set theory work, and it uses *exactly* the triangle inequality. Without that axiom the balls would not be open in their own sense, and the entire theory would have to be rebuilt.

Now ask: what closure operations should the collection of open sets be closed under? Two natural ones, and a third that fails. First, *arbitrary unions*: a union of open sets is open. Reason: if $x \in \bigcup_\alpha U_\alpha$, then $x \in U_{\alpha_0}$ for some $\alpha_0$, and the ball around $x$ in $U_{\alpha_0}$ lies in the union. So no matter how many open sets you union — even uncountably many — the result is still open. This is the cleanest closure property we have. Second, *finite intersections*: a finite intersection of open sets is open. Reason: if $x \in U_1 \cap U_2$, then there is a ball $B_{\varepsilon_1}(x) \subseteq U_1$ and a ball $B_{\varepsilon_2}(x) \subseteq U_2$; take $\varepsilon = \min(\varepsilon_1, \varepsilon_2)$ and $B_\varepsilon(x)$ lies in both. This extends to any finite intersection by induction, with $\varepsilon = \min_i \varepsilon_i > 0$.

The third — *arbitrary intersections* — is where things break, and it is instructive to see *why*. Consider the intervals $U_n = (-1/n, 1/n)$ in $\mathbb{R}$. Each is open. Their intersection is $\bigcap_{n=1}^\infty U_n = \{0\}$, the single point at the origin. Is $\{0\}$ open? It is *not*: no ball of any radius about $0$ lies in $\{0\}$, because every ball contains points other than $0$. The intersection has shrunk away the wiggle room. The mechanism is: each $U_n$ has wiggle room of size $1/n$, but as $n \to \infty$ that wiggle room shrinks to zero. A finite intersection is safe because the minimum of finitely many positive numbers is positive; an infinite intersection is not. This explains the asymmetry between unions and intersections in the open-set axioms — *unions never shrink wiggle room, but intersections can*. To make the theory work, we keep arbitrary unions and restrict to finite intersections.

The empty set and the whole space $X$ are open: the empty set vacuously (no points to check), and $X$ because every ball lies in $X$ by definition. These are the trivial edge cases, included to make the axioms close cleanly under arbitrary union and finite intersection (the union of no sets is empty; the intersection of no sets is everything).

Now define a **closed** set as the complement of an open one. This is the dual notion: a closed set is one whose complement has wiggle room everywhere. The standard examples — closed intervals $[a, b]$, the unit ball $\overline{B_1(0)}$, the set $\mathbb{Z} \subseteq \mathbb{R}$ — are closed because their complements are open. By De Morgan, closed sets are closed under arbitrary intersections and finite unions: dual to the open-set axioms.

A subtlety worth flagging early: "closed" is not the opposite of "open". A set may be both open and closed (the empty set, the whole space, every set in the discrete metric), or neither (an open interval together with one endpoint, like $[0, 1)$). The English word "closed" suggests a finished boundary, but it really only means "has an open complement". The distinction is purely set-theoretic; the geometric picture of "containing its boundary" is a *consequence* of the definition (a closed set in $\mathbb{R}^n$ contains all its limit points), not the definition itself.

One last subtlety: the closed *ball* $\{y : d(x, y) \leq \varepsilon\}$ is a closed set, but it need not equal the *closure* of the open ball $B_\varepsilon(x)$. In $\mathbb{R}^n$ they coincide — the closure of the open disc is the closed disc — but in the discrete metric the open ball $B_1(x) = \{x\}$ (since the only point within distance $< 1$ of $x$ is $x$ itself), while the closed ball $\{y : d(x, y) \leq 1\} = X$ (every point has distance at most $1$ from $x$). The closure of $\{x\}$ in the discrete metric is $\{x\}$ (singletons are closed). So we have $\overline{B_1(x)} = \{x\} \neq X$. The two notations look the same but mean different things: be aware of the source of the bar.

---

# The Definition

Let $(X, d)$ be a metric space.

**Open ball.** For $x \in X$ and $\varepsilon > 0$, the **open ball** of radius $\varepsilon$ centred at $x$ is
$$B_\varepsilon(x) = \{y \in X : d(x, y) < \varepsilon\}.$$
The **closed ball** of radius $\varepsilon$ centred at $x$ is
$$\{y \in X : d(x, y) \leq \varepsilon\}.$$

**Open set.** A subset $U \subseteq X$ is **open** if for every $x \in U$ there exists $\varepsilon > 0$ with $B_\varepsilon(x) \subseteq U$.

**Closed set.** A subset $F \subseteq X$ is **closed** if its complement $X \setminus F$ is open.

The collection $\tau = \tau_d \subseteq \mathcal{P}(X)$ of open sets is called the **topology induced by $d$**.

**Properties of the collection $\tau$:**

1. $\emptyset \in \tau$ and $X \in \tau$.

2. (Open balls are open.) For every $x \in X$ and $\varepsilon > 0$, $B_\varepsilon(x) \in \tau$.

3. (Arbitrary unions of opens are open.) If $\{U_\alpha\}_{\alpha \in I}$ is any family of open sets, then $\bigcup_\alpha U_\alpha \in \tau$.

4. (Finite intersections of opens are open.) If $U_1, \dots, U_n \in \tau$, then $U_1 \cap \dots \cap U_n \in \tau$.

The dual statements for closed sets follow by complementation: $X$ and $\emptyset$ are closed, arbitrary intersections of closed sets are closed, finite unions of closed sets are closed.

---

# Relate to Other Fields / Compression

The four properties above — empty and full set open, open balls open, arbitrary unions open, finite intersections open — are *exactly* the data needed to define a **topology** in the abstract sense (see [[Def - Topological Space]]). So a metric space is a special kind of topological space: one whose topology is *induced* by a metric. The compression is dramatic — we forget the actual distances $d(x, y)$ and remember only the collection of open sets — but enough information remains to define continuity and to do much of analysis. Topologies that arise from metrics are called **metrizable**; not every topology is metrizable, and the question of which topologies are metrizable is the subject of the *Urysohn metrization theorem* in [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

In **measure theory**, the analogous structure is the **σ-algebra**. A σ-algebra is closed under arbitrary *countable* unions and under *complementation* — and the asymmetry between topology (finite intersections, arbitrary unions, no complementation) and σ-algebra (countable unions, complementation) is exactly the asymmetry between the two kinds of "regularity" mathematics studies. The bridge is the **Borel σ-algebra**: given a topological space $(X, \tau)$, the smallest σ-algebra containing $\tau$ is $\mathcal{B}(X)$. Topological data feeds into measurable data through this construction.

In **functional analysis**, the *weak topology* on a normed space is generated by demanding that every continuous linear functional be continuous in the new topology — concretely, this means the open sets are unions of finite intersections of preimages $\varphi^{-1}(U)$ for $\varphi \in V^*$ and $U \subseteq \mathbb{R}$ open. The finite-intersection-then-arbitrary-union recipe is the engine. The weak topology is rarely metrizable on infinite-dimensional spaces, which is precisely why one must work in the more general topological setting.

In **algebraic geometry**, the *Zariski topology* on $\mathbb{R}^n$ (or any variety) has as closed sets the zero sets of polynomials. There are very few open sets — the topology is far coarser than the Euclidean one — but the same four axioms hold. This shows that the four axioms are agnostic to whether the topology comes from a metric: they work equally well for the Euclidean topology and the Zariski one, and the abstract framework treats them on equal footing.

---

# Examples / Corollaries

**Is an instance — the open interval $(a, b) \subseteq \mathbb{R}$ with the Euclidean metric.** For any $x \in (a, b)$, take $\varepsilon = \min(x - a, b - x) > 0$. Then $B_\varepsilon(x) = (x - \varepsilon, x + \varepsilon) \subseteq (a, b)$. So $(a, b)$ is open.

**Is an instance — the closed interval $[a, b] \subseteq \mathbb{R}$.** The complement is $(-\infty, a) \cup (b, \infty)$, which is a union of two open sets, hence open. So $[a, b]$ is closed.

**Is NOT an instance of either — the half-open interval $[a, b)$.** The complement is $(-\infty, a) \cup [b, \infty)$. The set $[b, \infty)$ is *not* open (no ball around $b$ stays in it; any ball $(b - \varepsilon, b + \varepsilon)$ contains points $< b$). So $[a, b)$ is not closed. And $[a, b)$ is not open either: at $x = a$, every ball $(a - \varepsilon, a + \varepsilon)$ contains points $< a$ which are not in $[a, b)$. So $[a, b)$ is neither open nor closed in $\mathbb{R}$.

**Is an instance — both the empty set $\emptyset$ and the whole space $X$ are open and closed** in every metric space. They are the only two "clopen" sets in $\mathbb{R}$, but in general there can be more — see the discrete metric below. A space in which the only clopen sets are $\emptyset$ and $X$ is **connected** (this will become the definition in [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]]).

**Is an instance — the discrete metric $d(x, y) = 1$ for $x \neq y$.** Every singleton $\{x\}$ is open: $B_{1/2}(x) = \{x\} \subseteq \{x\}$. Therefore every subset is a union of singletons, hence open. By complementation every subset is closed. The induced topology is the **discrete topology** — every set is both open and closed.

**Is an instance — counterexample to "arbitrary intersections of opens are open".** On $\mathbb{R}$, consider $U_n = (-1/n, 1/n)$. Each is open. Their intersection is $\bigcap_{n=1}^\infty (-1/n, 1/n) = \{0\}$. The set $\{0\}$ is *not* open in $\mathbb{R}$: any ball $(-\varepsilon, \varepsilon)$ contains points other than $0$. This shows we cannot weaken "finite intersections" to "arbitrary intersections" — the open-set axioms have *exactly* the right strength.

**Is an instance — the closed ball and the closure of the open ball coinciding in $\mathbb{R}^n$.** In $\mathbb{R}^2$, the closure of $B_1(0) = \{x : |x| < 1\}$ is $\{x : |x| \leq 1\}$, which equals the closed ball. The argument: any point with $|x| = 1$ is the limit of the sequence $(1 - 1/n)x$, which lies in $B_1(0)$. So in $\mathbb{R}^n$ the notations $\overline{B_\varepsilon(x)}$ for "closed ball" and for "closure of open ball" are interchangeable.

**Is NOT an instance — closed ball $\neq$ closure of open ball, in the discrete metric.** Take $X = \{0, 1\}$ with the discrete metric. Then $B_1(0) = \{0\}$ (since $d(0, 1) = 1$, not strictly less than 1). The closure of $\{0\}$ is $\{0\}$ (singletons are closed in the discrete metric). But the closed ball $\{y : d(0, y) \leq 1\} = \{0, 1\} = X$. So the closed ball is *strictly larger* than the closure of the open ball. This counterexample is canonical: it shows the two notations must be read carefully.

**Corollary — open balls are open.** This is one of the defining properties listed in The Definition above. The proof uses the triangle inequality: if $y \in B_\varepsilon(x)$ and $\delta = \varepsilon - d(x, y) > 0$, then $B_\delta(y) \subseteq B_\varepsilon(x)$.

**Corollary — a set is open if and only if it is a union of open balls.** If $U$ is open, then for each $x \in U$ pick $\varepsilon_x > 0$ with $B_{\varepsilon_x}(x) \subseteq U$; then $U = \bigcup_{x \in U} B_{\varepsilon_x}(x)$. Conversely, a union of open balls is open by the "arbitrary unions" axiom. So the open balls form a *basis* for the topology — see [[Def - Basis and Subbasis for a Topology]].

**Corollary — a set is closed if and only if it contains all its limit points.** A point $x$ is a *limit point* of $F$ if every ball $B_\varepsilon(x)$ contains a point of $F$ other than $x$. The "if": suppose $F$ contains its limit points. Take $x \notin F$. If every ball about $x$ met $F$, then $x$ would be a limit point, contradicting $x \notin F$; so some ball $B_\varepsilon(x)$ is disjoint from $F$, i.e. lies in $X \setminus F$, so $X \setminus F$ is open. The "only if" runs the same argument in reverse. This is the geometric reason "closed" is named what it is — the set is closed under taking limits of its sequences.

**Calibration check.** Verify that $\mathbb{Q} \subseteq \mathbb{R}$ is *neither* open nor closed: every ball about a rational contains irrationals (so $\mathbb{Q}$ is not open), and every ball about an irrational contains rationals (so $\mathbb{R} \setminus \mathbb{Q}$ is not open, i.e. $\mathbb{Q}$ is not closed). Verify that $\mathbb{Z} \subseteq \mathbb{R}$ *is* closed (the complement is a union of open intervals) but not open. Verify that in the discrete metric the closed ball of radius 1 about any point is the whole space, while the open ball is the singleton. If you can also explain why "intersection of countably many open intervals shrinking to a point" produces a non-open set, you have understood the asymmetry between unions and intersections that drives the entire axiom system.

---

# Unlocked by This

> [!tip] **Continuity via Open Sets** *(from this topic)*
> The map $f : (X, d_X) \to (Y, d_Y)$ is continuous if and only if $f^{-1}(U)$ is open in $X$ for every open $U \subseteq Y$. This is the bridge from metric continuity ($\varepsilon$–$\delta$) to *topological* continuity, and it shows that continuity depends only on the open sets — not on the actual distances. See [[Thm - Continuity via Open Sets (Metric Spaces)]].

> [!tip] **Equivalent Metrics** *(from this topic)*
> Two metrics on the same set may give *the same open sets* even though their numerical values differ. The Euclidean, taxicab, and sup metrics on $\mathbb{R}^n$ are pairwise equivalent in this sense. See [[Def - Equivalent Metrics]].

> [!tip] **Closure, Interior, Boundary** *(from this topic)*
> The closure $\overline{A}$ is the smallest closed set containing $A$; the interior $A^\circ$ is the largest open set contained in $A$; the boundary $\partial A = \overline{A} \setminus A^\circ$ is what is in the closure but not the interior. These are defined in terms of open and closed sets alone, with no further metric data needed.

> [!tip] **Borel σ-Algebra** *(from Measure Theory)*
> The smallest σ-algebra containing the open sets is the **Borel σ-algebra** $\mathcal{B}(X)$. This is the standard σ-algebra on a metric (or topological) space, the one used in probability and Lebesgue integration. The topology of open sets is what feeds into the measure-theoretic world.

> [!tip] **Topological Space** *(from this topic)*
> The four properties of $\tau_d$ — closed under arbitrary unions, finite intersections, containing $\emptyset$ and $X$ — are exactly the axioms of an abstract **topological space**, where one forgets the metric entirely and works with the open-set collection directly. See [[Def - Topological Space]].

---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Metric Space"
  - "Def - Equivalent Metrics"
  - "Def - Open and Closed Sets in a Metric Space"
  - "Def - Continuous Map"
tags: [analysis, topology]
---

# Problem Statement

On the set $C[0,1]$ of continuous real-valued functions on $[0,1]$, consider two metrics:
$$d_\infty(f, g) = \sup_{t \in [0,1]} |f(t) - g(t)|, \qquad d_1(f, g) = \int_0^1 |f(t) - g(t)|\, dt.$$

1. Show that $d_1(f, g) \leq d_\infty(f, g)$ for all $f, g \in C[0,1]$.
2. Deduce that the identity map $\operatorname{id} : (C[0,1], d_\infty) \to (C[0,1], d_1)$ is [[Def - Continuous Map|continuous]].
3. Show that the identity map in the *reverse* direction, $(C[0,1], d_1) \to (C[0,1], d_\infty)$, is *not* continuous, by exhibiting a sequence $f_n \in C[0,1]$ with $d_1(f_n, 0) \to 0$ but $d_\infty(f_n, 0) \not\to 0$.
4. Conclude that $d_1$ and $d_\infty$ are *not* [[Def - Equivalent Metrics|topologically equivalent]].

**Recall:**

![[Def - Equivalent Metrics#The Definition]]

Two metrics $d, \rho$ on $X$ are [[Def - Equivalent Metrics|topologically equivalent]] iff they generate the same open sets, equivalently iff the identity $(X, d) \to (X, \rho)$ is a [[Def - Homeomorphism|homeomorphism]] — *both* directions continuous. To show they are *not* equivalent it is enough to refute continuity of the identity in one direction; the other inclusion of open balls fails.

A function $f : (X, d) \to (Y, \rho)$ between metric spaces is [[Def - Continuous Map|continuous]] iff it pulls back open balls to opens, equivalently iff for every $x \in X$ and $\varepsilon > 0$ there is $\delta > 0$ with $d(x, x') < \delta \Rightarrow \rho(f(x), f(x')) < \varepsilon$ (by [[Thm - Continuity via Open Sets (Metric Spaces)|continuity-via-open-sets]]). For the identity map between two metrics, this $\varepsilon$–$\delta$ statement becomes: $d_\infty(f, g) < \delta \Rightarrow d_1(f, g) < \varepsilon$ in one direction, and the reverse implication in the other.

---

# Convergent Strategy

**Problem class.** Compare two metrics on the same set and decide whether they generate the same topology. The standard route is to test whether the *identity map* is a homeomorphism: it is automatically a bijection, so the question reduces to continuity in each direction.

**Assumption pattern.** Each direction is an $\varepsilon$–$\delta$ statement about the identity map. Continuity in one direction is the inequality $d_1 \leq d_\infty$ (so $d_\infty < \varepsilon \Rightarrow d_1 < \varepsilon$). The reverse direction would need $d_1 < \delta \Rightarrow d_\infty < \varepsilon$ — equivalently, $d_\infty \leq C \cdot d_1$ for some constant $C$, which would force the two metrics to be *Lipschitz equivalent* and hence give the same topology.

**Theorem routing.** Step 1 is a one-line pointwise bound integrated over $[0,1]$ — the sup is an upper bound for the integrand. Step 2 follows because the identity map is its own thing (no derivative computation, no decomposition); continuity reduces to the $\varepsilon$–$\delta$ statement $d_\infty(f, g) < \varepsilon \Rightarrow d_1(f, g) < \varepsilon$, which is Step 1. Step 3 needs an *escaping-mass* counterexample: a sequence that converges in the integral metric but not in the sup metric. The same tent functions that work in [[Ex - Verifying a metric and computing its topology]] are the natural candidates — area going to zero but height staying $1$.

**Key decision point.** The non-obvious move is recognizing that the reverse continuity, $d_1 \to d_\infty$, would require a bound $d_\infty(f, g) \leq C \cdot d_1(f, g)$ — equivalently the sup norm bounded by the integral norm up to a constant. This is false because the sup sees a *single point* while the integral averages over the whole interval, and a function can be enormous at one point and tiny on average. Once this is recognized, finding a counterexample is straightforward.

---

# Legal Operations Used

This solution deploys the following operations from [[Topology I — §1–3 Metric and Topological Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Bound the integral pointwise by the sup.** $|f(t) - g(t)| \leq \sup_s |f(s) - g(s)|$ for every $t$, so integrating both sides gives $d_1 \leq d_\infty$. This is the prototype of the universal trigger "an integral is bounded by the sup times the measure".

2. **Reduce identity-map continuity to a one-line metric inequality.** Between two metrics on the same set, the identity is continuous iff $d_{\text{source}}(f, g) < \delta \Rightarrow d_{\text{target}}(f, g) < \varepsilon$. The shortest possible verification is a global inequality $d_{\text{target}} \leq d_{\text{source}}$.

3. **Construct an escaping-mass counterexample.** Tent functions with shrinking base and unit height — area $\to 0$ but sup stays $1$ — separate the two metrics.

4. **Use the identity-is-homeomorphism criterion for equivalent metrics.** Two metrics on the same set are [[Def - Equivalent Metrics|topologically equivalent]] iff the identity is a homeomorphism in both directions, equivalently iff every $d_1$-ball about a point contains a $d_2$-ball about the same point and vice versa.

---

# Hints

> [!note]- Hint 1
> For the inequality, observe $|f(t) - g(t)| \leq d_\infty(f, g)$ for every $t \in [0,1]$ — this is the definition of sup. Now integrate.

> [!note]- Hint 2
> For Step 2, the inequality $d_1 \leq d_\infty$ means that the identity map $(C, d_\infty) \to (C, d_1)$ is *Lipschitz with constant $1$*. Lipschitz maps are continuous.

> [!note]- Hint 3
> For Step 3, take tent functions: $f_n(t) = \max(1 - nt, 0)$ for $t \in [0,1]$. What is $d_\infty(f_n, 0)$? What is $d_1(f_n, 0)$?

> [!note]- Hint 4
> The deeper reason no Lipschitz bound $d_\infty \leq C \cdot d_1$ can hold: the sup depends on the function's value at a *single point*, but the integral averages over the whole interval. A function can be huge at a point and small on average.

---

# Solution

Two metrics on the same set generate the same topology iff the identity map is a homeomorphism. Continuity in one direction is a one-line inequality; the failure in the other direction is the canonical counterexample of analysis — a spike whose area is small but whose height is not.

**Step 1: The pointwise bound and the inequality.**

For every $t \in [0,1]$, $|f(t) - g(t)| \leq \sup_{s \in [0,1]} |f(s) - g(s)| = d_\infty(f, g)$. Integrating this over $[0,1]$:
$$d_1(f, g) = \int_0^1 |f - g|\, dt \leq \int_0^1 d_\infty(f, g)\, dt = d_\infty(f, g) \cdot 1 = d_\infty(f, g).$$

> [!note]- Derivation
> The supremum of a function is, by definition, an upper bound for every value the function takes: $|f(t) - g(t)| \leq \sup_s |f(s) - g(s)|$ for each $t$. (The sup is finite because $f - g$ is continuous on the compact interval $[0,1]$, hence bounded — this is the **extreme value theorem**.)
>
> Integrating the inequality preserves the relation (**monotonicity of the Riemann integral**): nonnegative pointwise inequalities integrate to nonnegative integral inequalities. The right-hand side is a constant, so $\int_0^1 d_\infty(f, g)\, dt = d_\infty(f, g)$. Hence $d_1(f, g) \leq d_\infty(f, g)$.

**Step 2: The identity $(C, d_\infty) \to (C, d_1)$ is continuous.**

Continuity of the identity map between two metrics is exactly the $\varepsilon$–$\delta$ statement "$d_\infty(f, g)$ small $\Rightarrow d_1(f, g)$ small". By Step 1, we can take $\delta = \varepsilon$: if $d_\infty(f, g) < \varepsilon$, then $d_1(f, g) \leq d_\infty(f, g) < \varepsilon$. The identity is in fact **Lipschitz with constant $1$** between these metrics.

> [!note]- Derivation
> Fix $f \in C[0,1]$ and $\varepsilon > 0$. We need $\delta > 0$ such that whenever $d_\infty(f, g) < \delta$, then $d_1(\operatorname{id}(f), \operatorname{id}(g)) = d_1(f, g) < \varepsilon$. Choose $\delta = \varepsilon$. Then $d_\infty(f, g) < \delta = \varepsilon$ implies $d_1(f, g) \leq d_\infty(f, g) < \varepsilon$ by Step 1.
>
> By [[Thm - Continuity via Open Sets (Metric Spaces)|continuity-via-open-sets]], $\varepsilon$–$\delta$ continuity at every point is equivalent to the open-preimage criterion, so the identity is continuous as a map of topological spaces.
>
> Equivalently, every $d_1$-open ball pulls back to a $d_\infty$-open set: $\operatorname{id}^{-1}(B^{d_1}_\varepsilon(f)) \supseteq B^{d_\infty}_\varepsilon(f)$. So every $d_1$-open set is $d_\infty$-open — the $d_\infty$ topology is *finer* than the $d_1$ topology.

**Step 3: The identity in reverse is not continuous.**

Define the tent functions $f_n(t) = \max(1 - nt, 0)$. Then $d_1(f_n, 0) = \frac{1}{2n} \to 0$ but $d_\infty(f_n, 0) = 1$ for every $n$. Hence the identity $(C, d_1) \to (C, d_\infty)$ takes a sequence converging to $0$ in the source to a sequence not converging to $0$ in the target — so it is not continuous.

> [!note]- Derivation
> Each $f_n$ is piecewise linear with $f_n(0) = 1$, $f_n(1/n) = 0$, and $f_n(t) = 0$ on $[1/n, 1]$; the two pieces agree at $t = 1/n$, so $f_n \in C[0,1]$.
>
> *Integral metric.* $\int_0^1 |f_n(t)|\, dt$ is the area of the triangle with vertices $(0, 1)$, $(1/n, 0)$, $(0, 0)$ — base $1/n$, height $1$, area $\frac{1}{2n}$. So $d_1(f_n, 0) = \frac{1}{2n} \to 0$.
>
> *Sup metric.* $\sup_{t \in [0,1]} |f_n(t)| = f_n(0) = 1$ for every $n$. So $d_\infty(f_n, 0) = 1$ for every $n$, and $d_\infty(f_n, 0) \not\to 0$.
>
> If $\operatorname{id} : (C, d_1) \to (C, d_\infty)$ were continuous at $0$, then $d_1(f_n, 0) \to 0$ would force $d_\infty(\operatorname{id}(f_n), \operatorname{id}(0)) = d_\infty(f_n, 0) \to 0$ (continuous maps preserve sequence limits in metric spaces, since they are [[Def - First and Second Countable|first countable]]). It does not, so the identity is *not* continuous.

**Step 4: The two metrics are not equivalent.**

By definition, $d_1$ and $d_\infty$ are [[Def - Equivalent Metrics|topologically equivalent]] iff the identity map is a homeomorphism, i.e. continuous in both directions. Step 3 shows one direction fails, so they are not equivalent.

> [!note]- Derivation
> If $d_1$ and $d_\infty$ generated the same topology $\tau$, then the identity map $(C, d_1) = (C, \tau) \to (C, \tau) = (C, d_\infty)$ would be the identity on the topological space $(C, \tau)$, which is continuous. Step 3 contradicts this.
>
> Equivalently, the $d_\infty$ topology is *strictly finer* than the $d_1$ topology: the $d_\infty$-ball $B^{d_\infty}_1(0) = \{f : \sup |f| < 1\}$ is $d_\infty$-open but is *not* $d_1$-open at $0$ (it does not contain any $d_1$-ball $B^{d_1}_\varepsilon(0)$, since $f_n \in B^{d_1}_\varepsilon(0)$ for $n > 1/(2\varepsilon)$ but $f_n \notin B^{d_\infty}_1(0)$).

> [!note]- Complete formal solution
> **(1)** Pointwise $|f(t) - g(t)| \leq d_\infty(f,g)$, integrate: $d_1(f,g) \leq d_\infty(f,g)$. **(2)** The identity is Lipschitz-1 from $d_\infty$ to $d_1$: $d_\infty(f, g) < \varepsilon \Rightarrow d_1(f, g) < \varepsilon$, so continuous. **(3)** $f_n(t) = \max(1 - nt, 0)$: $d_1(f_n, 0) = 1/(2n) \to 0$ but $d_\infty(f_n, 0) = 1$, so the reverse identity is not continuous. **(4)** Continuity of the identity in both directions is the definition of [[Def - Equivalent Metrics|topological equivalence]] — Step 3 refutes it. $\blacksquare$

---

# Key Takeaways

**Continuity of the identity map between two metrics is equivalent to a "smaller open balls contain smaller open balls" containment — and the easiest way to verify it is a pointwise metric inequality.** The implication chain is: $d_\infty(f, g) \leq C \cdot d_1(f, g)$ everywhere $\Rightarrow$ $B^{d_1}_{\varepsilon/C}(f) \subseteq B^{d_\infty}_\varepsilon(f)$ for all $f, \varepsilon$ $\Rightarrow$ every $d_\infty$-open set is $d_1$-open $\Rightarrow$ identity $(C, d_1) \to (C, d_\infty)$ is continuous. So a global metric inequality $d_{\text{tgt}} \leq C \cdot d_{\text{src}}$ proves continuity of the identity in the corresponding direction. In our problem, $d_1 \leq d_\infty$ proves $(C, d_\infty) \to (C, d_1)$ continuous; the *absence* of any such bound in reverse is what fails. Whenever comparing two metrics on the same set, the first computation to do is: is there a constant $C$ with each metric bounded by $C$ times the other? If both directions work, the metrics are *Lipschitz equivalent* (a strong form of topological equivalence); if neither works, the topologies are incomparable.

**The sup metric is "stronger" (finer topology) than the $L^1$ metric on $C[0,1]$, and the gap is the difference between *uniform convergence* and *mean convergence*.** Convergence in $d_\infty$ is uniform convergence, which preserves continuity, suprema, and pointwise values. Convergence in $d_1$ is mean convergence, which preserves integrals against bounded test functions but not pointwise values. This means there are vastly more $d_1$-Cauchy sequences than $d_\infty$-Cauchy sequences, and the *completion* of $C[0,1]$ in $d_1$ is the much larger space $L^1[0,1]$ — a fundamentally different object containing discontinuous functions. The completion of $C[0,1]$ in $d_\infty$ is just $C[0,1]$ itself (already complete). The general lesson: weaker topologies have more Cauchy sequences and hence richer completions; the choice of metric on a function space controls which limits exist.

**Escaping-mass counterexamples are the universal mechanism separating "integrated" notions of convergence from "pointwise" or "sup" notions.** The same tent functions work in three different settings: separating $L^1$ from pointwise convergence on $C[0,1]$ (this exercise), separating a.s. from $L^1$ convergence in probability (see [[Ex - The hierarchy of convergence modes]]), and separating weak from strong convergence in Hilbert spaces (the orthonormal basis $e_n$). In each case the mechanism is the same: a feature of the function (height, value at a point, $L^\infty$ norm, inner product with a fixed vector) is preserved while another feature (integral, $L^1$ norm, distance from the limit on average) shrinks. The "spike" or "tent" is the geometric realization of "mass escaping into a single point". Once recognized, this construction is reusable across analysis, probability, and functional analysis.

**Two metrics give the same topology iff every "small" $d$-ball contains some "smaller" $\rho$-ball about the same point, in both directions — but they need not give the same *uniform structure* (Cauchy sequences) or *Lipschitz structure* (distances up to constants).** Topological equivalence is the weakest of three increasingly strong relations: topologically equivalent ($\subseteq$ same opens) $\Leftarrow$ uniformly equivalent (same Cauchy sequences) $\Leftarrow$ Lipschitz equivalent ($C_1 d \leq \rho \leq C_2 d$). Each layer adds rigidity to the comparison. In $\mathbb{R}^n$ the three Euclidean-style metrics ($\ell^1$, $\ell^2$, $\ell^\infty$) are *all three* (Lipschitz equivalent, hence the others) — see [[Ex - Three equivalent metrics on Rn]]. On infinite-dimensional spaces the layers genuinely separate: $d_1$ and $d_\infty$ on $C[0,1]$ are not even topologically equivalent. This stratification is the entry point into Banach space theory, where "equivalent norms" is the Lipschitz layer and the *non*-equivalent-norm world is what makes functional analysis nontrivial.

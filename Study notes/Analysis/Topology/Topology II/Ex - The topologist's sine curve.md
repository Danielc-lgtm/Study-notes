---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Connected Space"
  - "Def - Path-Connected Space"
  - "Def - Closure, Interior, and Boundary"
  - "Def - Continuous Map"
  - "Thm - Continuous Image of a Connected Space"
tags: [analysis, topology, connectedness, counterexample]
---

# Problem Statement

Let
$$X = A \cup S, \qquad A = \{(x, \sin(1/x)) : x > 0\}, \qquad S = \{0\} \times [-1, 1],$$
both equipped with the subspace topology from $\mathbb{R}^2$. The space $X$ is called the **topologist's sine curve**. Show:

**(a)** $X$ is the closure $\overline{A}$ of the graph piece $A$ in $\mathbb{R}^2$.

**(b)** $X$ is connected.

**(c)** $X$ is *not* path-connected: there is no continuous $\gamma : [0, 1] \to X$ with $\gamma(0) \in S$ and $\gamma(1) \in A$.

**Recall:**

The relevant objects are connectedness, path-connectedness, closure, and the propagation theorems for both.

![[Def - Connected Space#The Definition]]

![[Def - Path-Connected Space#The Definition]]

A point $p \in \mathbb{R}^2$ lies in the [[Def - Closure, Interior, and Boundary|closure]] $\overline{A}$ if every open neighbourhood of $p$ in $\mathbb{R}^2$ meets $A$, equivalently if there is a sequence in $A$ converging to $p$ (since $\mathbb{R}^2$ is metric, hence first countable).

A [[Def - Continuous Map|continuous map]] $\gamma : [0,1] \to X \subseteq \mathbb{R}^2$ is a pair of continuous coordinate maps $\gamma(t) = (\gamma_1(t), \gamma_2(t))$.

Closures of connected sets are connected: if $A$ is connected and $A \subseteq B \subseteq \overline{A}$, then $B$ is connected. This is a corollary of [[Def - Connected Space|the connectedness definition]] — see also the [[Def - Connected Space#Examples / Corollaries|closure is connected corollary]] on the definition page.

---

# Convergent Strategy

**Problem class.** A *separation argument*. The graph $A$ is the continuous image of $(0, \infty)$ under $x \mapsto (x, \sin(1/x))$, hence path-connected and so connected. The hard work is (c): showing no path crosses from $S$ to $A$, which is a *nonexistence* result requiring control over what continuous functions can do near $x = 0$ where $\sin(1/x)$ oscillates without bound.

**Assumption pattern.** The graph piece $A$ has the metric structure of a smooth curve; the segment $S$ is a closed interval embedded vertically; the join happens at $x = 0$ where the graph cannot be extended continuously because $\sin(1/x)$ has no limit. The closure argument in (a) is the standard "small disc around any point of $S$ contains points of $A$" computation, and (b) is the closure-is-connected corollary.

**Theorem routing.** Part (a) is direct from the closure characterization. Part (b) follows from (a) via the [[Def - Connected Space#Examples / Corollaries|closure-is-connected corollary]] applied to $A$ (connected because path-connected via the continuous parametrization $x \mapsto (x, \sin(1/x))$ of the connected set $(0, \infty)$). Part (c) is the deepest: the standard argument considers the set $T = \gamma^{-1}(S) = \{t : \gamma_1(t) = 0\}$, shows it is closed, takes $t_0 = \sup T$, and derives a contradiction from the oscillation of $\sin(1/x)$.

**Key decision point.** Where exactly does oscillation give the contradiction? At $t_0 = \sup T$, the path's $x$-coordinate $\gamma_1$ is positive on $(t_0, 1]$ but $\gamma_1(t_0) = 0$. By continuity of $\gamma$, $\gamma_2(t) \to \gamma_2(t_0)$ as $t \to t_0^+$. But $\gamma_2(t) = \sin(1/\gamma_1(t))$ on $(t_0, 1]$, and as $\gamma_1(t) \to 0^+$, the value $\sin(1/\gamma_1(t))$ takes every value in $[-1, 1]$ in every right-neighbourhood of $t_0$. So $\gamma_2$ cannot have a limit — contradicting continuity.

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **Closure-of-connected-is-connected.** Apply this to $A$ to immediately deduce (b) from (a). The closure of any connected set is connected — a corollary of the definition.

2. **Express a path-connectedness obstruction as continuity of a coordinate function.** Reduce the question "is there a path?" to "is there a continuous extension across the oscillation?", which uses [[Thm - Continuous Image of a Connected Space|continuity propagation]] on $\gamma^{-1}(S)$ (which is closed).

3. **Use oscillation of $\sin(1/x)$ as a discontinuity engine.** The key fact about $\sin(1/x)$ near $0$ is that it takes every value of $[-1, 1]$ in every neighbourhood of $0$ — concretely, $\sin(1/x_n) = 1$ for $x_n = 2/(\pi(4n+1))$ and $\sin(1/y_n) = -1$ for $y_n = 2/(\pi(4n+3))$, both with $x_n, y_n \to 0^+$.

---

# Hints

> [!note]- Hint 1
> For (a): a point $(0, y) \in S$ is in $\overline{A}$ if and only if every disc around $(0, y)$ meets $A$. For any $y \in [-1, 1]$, pick a sequence $x_n \to 0^+$ with $\sin(1/x_n) = y$ — such sequences exist by the intermediate value theorem applied to $\sin(1/x)$ on the intervals between its consecutive maxima and minima.

> [!note]- Hint 2
> For (b): use (a) and the fact that closures of connected sets are connected. $A$ is connected because it is the continuous image of $(0, \infty)$ under the parametrization $x \mapsto (x, \sin(1/x))$.

> [!note]- Hint 3
> For (c): suppose for contradiction $\gamma : [0, 1] \to X$ is a path with $\gamma(0) \in S$ and $\gamma(1) \in A$. Let $T = \gamma^{-1}(S) = \{t : \gamma_1(t) = 0\}$. Show $T$ is closed in $[0, 1]$ and $0 \in T$ and $1 \notin T$. Take $t_0 = \sup T$, so $t_0 \in T$ (it is closed), and $\gamma_1(t) > 0$ for $t > t_0$ (else $t > t_0$ would be in $T$).

> [!note]- Hint 4
> Now examine $\gamma_2$ as $t \to t_0^+$. For each $n$, you want to find $t_n \in (t_0, t_0 + 1/n]$ with $\gamma_2(t_n) = 1$ and $s_n \in (t_0, t_0 + 1/n]$ with $\gamma_2(s_n) = -1$. This is the intermediate value theorem applied to the continuous function $\gamma_1$ on a small interval after $t_0$: $\gamma_1(t_0) = 0$ and $\gamma_1(t)$ takes positive values, so $\gamma_1$ passes through every small positive value, and in particular through the values $x$ where $\sin(1/x) = 1$ and $\sin(1/x) = -1$.

---

# Solution

The topologist's sine curve is the *canonical* example of a connected space that is not path-connected. The proof of (c) hinges on a single fact: $\sin(1/x)$ has no limit as $x \to 0^+$, so any continuous path that approaches $x = 0$ along the graph from the right cannot have a continuous $y$-coordinate.

**Step 1: Part (a) — $X = \overline{A}$.**

The graph $A$ is contained in $X$, so $\overline{A} \subseteq \overline{X}$. We show the more substantive inclusion $S \subseteq \overline{A}$, which combined with $A \subseteq \overline{A}$ gives $X = A \cup S \subseteq \overline{A}$. Conversely, any closure point of $A$ either lies in $A$ or has $x$-coordinate $0$, hence lies in $S$.

> [!note]- Derivation
> Take any $(0, y) \in S$, so $y \in [-1, 1]$. We exhibit a sequence in $A$ converging to $(0, y)$. By the intermediate value theorem applied to $\sin$ on each interval $[2\pi n + 0, 2\pi n + 2\pi]$, there is $\theta_n \in [2\pi n, 2\pi n + 2\pi]$ with $\sin(\theta_n) = y$. Set $x_n = 1/\theta_n \to 0^+$ as $n \to \infty$. Then $\sin(1/x_n) = \sin(\theta_n) = y$, so $(x_n, y) \in A$ and $(x_n, y) \to (0, y)$. Thus $(0, y) \in \overline{A}$.
>
> For the reverse inclusion, suppose $p \in \overline{A} \setminus A$. Then there is a sequence $(x_n, \sin(1/x_n)) \in A$ converging to $p$. The first coordinate $x_n$ converges to the first coordinate $p_1$ of $p$. If $p_1 > 0$ then by continuity of $\sin(1/x)$ on $(0, \infty)$, the second coordinate $\sin(1/x_n) \to \sin(1/p_1)$, so $p = (p_1, \sin(1/p_1)) \in A$ — contradicting $p \notin A$. So $p_1 = 0$. The second coordinate $\sin(1/x_n)$ lies in $[-1, 1]$, hence so does its limit $p_2$, so $p = (0, p_2) \in S$. Hence $\overline{A} \subseteq A \cup S = X$.
>
> Combined with $X \subseteq \overline{A}$, we get $X = \overline{A}$.

**Step 2: Part (b) — $X$ is connected.**

The graph $A$ is the continuous image of $(0, \infty)$ under $x \mapsto (x, \sin(1/x))$, and $(0, \infty)$ is connected (it is an interval), so $A$ is connected by [[Thm - Continuous Image of a Connected Space]]. Since $A \subseteq X = \overline{A}$, and the closure of a connected set is connected (see [[Def - Connected Space#Examples / Corollaries|the closure-is-connected corollary]]), $X$ is connected.

> [!note]- Derivation
> The map $\varphi : (0, \infty) \to \mathbb{R}^2$ given by $\varphi(x) = (x, \sin(1/x))$ is continuous (both coordinates are continuous on $(0, \infty)$), and its image is exactly $A$. The interval $(0, \infty)$ is connected — it is path-connected via $t \mapsto x_0 + t(x_1 - x_0)$, hence connected. By [[Thm - Continuous Image of a Connected Space]], the image $A = \varphi((0, \infty))$ is connected.
>
> Now $A \subseteq X = \overline{A}$ by (a). We invoke: if $A$ is connected and $A \subseteq B \subseteq \overline{A}$, then $B$ is connected. (Proof sketch: any clopen subset $C$ of $B$ has $C \cap A$ clopen in $A$, hence equal to $\emptyset$ or $A$. If $C \cap A = A$, then $C \supseteq A$, and since $C$ is closed in $B$ and contains $A$, $C \supseteq B \cap \overline{A}^B = B$, so $C = B$. If $C \cap A = \emptyset$, then $A \subseteq B \setminus C$, and the same argument gives $C = \emptyset$.) Apply with $B = X = \overline{A}$.

**Step 3: Part (c) — set-up of the no-path proof.**

Suppose for contradiction $\gamma : [0, 1] \to X$ is continuous with $\gamma(0) \in S$ and $\gamma(1) \in A$. The set $T = \gamma_1^{-1}(\{0\}) = \{t \in [0, 1] : \gamma_1(t) = 0\}$ is the preimage of $\{0\}$ under the continuous coordinate $\gamma_1$, hence closed. It contains $0$ (since $\gamma(0) \in S$) and excludes $1$ (since $\gamma(1) \in A$). Let $t_0 = \sup T \in T$ (closed). Then $t_0 < 1$ and $\gamma_1(t) > 0$ for all $t \in (t_0, 1]$.

> [!note]- Derivation
> $T$ is closed because $\gamma_1$ is continuous (as a coordinate of $\gamma$) and $\{0\}$ is closed in $\mathbb{R}$. The set $T \subseteq [0, 1]$ is nonempty (contains $0$) and bounded above by $1$, so $t_0 = \sup T$ exists. Closure of $T$ implies $t_0 \in T$, so $\gamma_1(t_0) = 0$, so $\gamma(t_0) \in S$.
>
> $t_0 \neq 1$: $\gamma(1) \in A$, so $\gamma_1(1) > 0$, so $1 \notin T$. Since $t_0 \in T$, $t_0 < 1$. By the supremum property, for $t > t_0$ we have $t \notin T$, i.e., $\gamma_1(t) \neq 0$. Since $\gamma_1$ is continuous and $\gamma_1(t_0) = 0$, and the image $\gamma([0,1]) \subseteq X$ has $x$-coordinates in $\{0\} \cup (0, \infty)$, we conclude $\gamma_1(t) > 0$ for $t \in (t_0, 1]$.

**Step 4: Part (c) — extract the oscillation contradiction.**

By continuity of $\gamma$ at $t_0$ from the right, $\gamma_2(t) \to \gamma_2(t_0)$ as $t \to t_0^+$. But on $(t_0, 1]$, $\gamma_2(t) = \sin(1/\gamma_1(t))$ because $\gamma(t) \in A$ when $\gamma_1(t) > 0$. We show $\sin(1/\gamma_1(t))$ has no limit as $t \to t_0^+$: by the intermediate value theorem applied to $\gamma_1$ on small right-intervals of $t_0$, $\gamma_1$ takes every small positive value, and in particular hits sequences $x_n \to 0$ with $\sin(1/x_n) = 1$ and $\sin(1/y_n) = -1$. Hence $\gamma_2$ takes both values $1$ and $-1$ in every right-neighbourhood of $t_0$, contradicting that $\gamma_2(t) \to \gamma_2(t_0)$.

> [!note]- Derivation
> Since $\gamma_1(t_0) = 0$ and $\gamma_1(t) > 0$ for $t \in (t_0, 1]$, $\gamma_1$ is continuous at $t_0$ and $\gamma_1(t_0 + h) \to 0$ as $h \to 0^+$. So for every $\delta > 0$ there is $h_0 > 0$ with $0 < \gamma_1(t) < \delta$ for $t \in (t_0, t_0 + h_0)$.
>
> Pick sequences in $(0, \delta)$:
> - $x_n = \dfrac{2}{\pi(4n + 1)}$, so $1/x_n = \pi(4n+1)/2$ and $\sin(1/x_n) = \sin(\pi/2 + 2\pi n) = 1$.
> - $y_n = \dfrac{2}{\pi(4n + 3)}$, so $1/y_n = \pi(4n+3)/2$ and $\sin(1/y_n) = \sin(3\pi/2 + 2\pi n) = -1$.
>
> Both $x_n, y_n \to 0^+$. So given any $h > 0$, take $\delta$ small enough that $x_n, y_n < \delta$ for $n$ large, then find $h_0$ as above; then the continuous function $\gamma_1 : [t_0, t_0 + h_0] \to [0, \delta]$ satisfies $\gamma_1(t_0) = 0$ and takes positive values, so by the intermediate value theorem it hits every value in $(0, \gamma_1(t_0 + h_0))$, hence in particular hits $x_n$ and $y_n$ for any $n$ large enough.
>
> Concretely: pick any $n$ with $x_n < \gamma_1(t_0 + h_0)$. Then there is $t_n \in (t_0, t_0 + h_0)$ with $\gamma_1(t_n) = x_n$. Then $\gamma_2(t_n) = \sin(1/\gamma_1(t_n)) = \sin(1/x_n) = 1$. By taking $n$ larger and $h_0$ smaller, we can produce a sequence $t_n \to t_0^+$ with $\gamma_2(t_n) = 1$ for all $n$. Hence $\gamma_2(t_n) \to 1$.
>
> By the symmetric argument with $y_n$, we get a sequence $s_n \to t_0^+$ with $\gamma_2(s_n) = -1$, hence $\gamma_2(s_n) \to -1$.
>
> Both $t_n, s_n \to t_0$ from the right, but $\gamma_2(t_n) \to 1 \neq -1 \leftarrow \gamma_2(s_n)$. So $\gamma_2$ has no right limit at $t_0$, contradicting continuity of $\gamma_2$ at $t_0$.

> [!note]- Complete formal solution
> **(a)** *Step a1: $S \subseteq \overline{A}$.* For $(0, y) \in S$ with $y \in [-1, 1]$, choose $\theta_n \in [2\pi n, 2\pi n + 2\pi]$ with $\sin\theta_n = y$ (intermediate value theorem on $\sin$). Set $x_n = 1/\theta_n \to 0^+$. Then $(x_n, \sin(1/x_n)) = (x_n, y) \to (0, y)$ in $\mathbb{R}^2$.
>
> *Step a2: $\overline{A} \subseteq X$.* For $p \in \overline{A} \setminus A$, a sequence $(x_n, \sin(1/x_n)) \to p$ in $\mathbb{R}^2$. If $p = (p_1, p_2)$ with $p_1 > 0$, continuity of $\sin(1/x)$ on $(0, \infty)$ gives $p_2 = \sin(1/p_1)$, so $p \in A$ — contradiction. So $p_1 = 0$ and $p_2 \in [-1, 1]$, hence $p \in S \subseteq X$.
>
> **(b)** $A$ is the continuous image of $(0, \infty)$ under $x \mapsto (x, \sin(1/x))$. Since $(0, \infty)$ is connected and continuous images of connected sets are connected ([[Thm - Continuous Image of a Connected Space]]), $A$ is connected. By (a), $A \subseteq X = \overline{A}$. The closure of a connected set is connected (proved: a clopen subset $C \subseteq X$ has $C \cap A$ clopen in $A$, hence $\emptyset$ or $A$; in either case $C$ must be $\emptyset$ or $X$ by closure-density). So $X$ is connected.
>
> **(c)** Suppose $\gamma : [0, 1] \to X$ is continuous with $\gamma(0) \in S$ and $\gamma(1) \in A$. Let $T = \{t : \gamma_1(t) = 0\}$, closed (preimage of closed under continuous $\gamma_1$), containing $0$, missing $1$. Let $t_0 = \sup T \in T$. Then $\gamma_1(t_0) = 0$, and $\gamma_1(t) > 0$ for $t \in (t_0, 1]$.
>
> Continuity of $\gamma_1$ at $t_0$ gives: for every $\delta > 0$ there is $h > 0$ with $\gamma_1(t) \in [0, \delta)$ for $t \in [t_0, t_0 + h]$. By the intermediate value theorem applied to $\gamma_1$ on $[t_0, t_0 + h]$, $\gamma_1$ takes every value in $[0, \gamma_1(t_0 + h)]$. For any $n$ large enough that $x_n = 2/(\pi(4n+1)) \in (0, \gamma_1(t_0 + h))$, choose $t_n \in (t_0, t_0 + h]$ with $\gamma_1(t_n) = x_n$, giving $\gamma_2(t_n) = \sin(1/x_n) = 1$. Similarly find $s_n \in (t_0, t_0 + h]$ with $\gamma_2(s_n) = -1$ (using $y_n = 2/(\pi(4n+3))$).
>
> Taking $h \to 0^+$, both $t_n \to t_0^+$ and $s_n \to t_0^+$, but $\gamma_2(t_n) = 1$ and $\gamma_2(s_n) = -1$ for all $n$. So $\lim_{t \to t_0^+} \gamma_2(t)$ does not exist, contradicting continuity of $\gamma_2$ at $t_0$. $\blacksquare$

---

# Key Takeaways

**Connectedness is closed under closure; path-connectedness is not.** This is the deepest structural fact in the example. The graph $A$ is path-connected (and hence connected); its closure $X = \overline{A}$ is connected (closure preserves it) but no longer path-connected — the act of taking closure has glued on a piece ($S$) to which there is no continuous path from $A$. The trigger to remember: any time you have a path-connected set whose closure adds new "boundary" points reachable only by oscillation or by traversing infinitely many obstacles, suspect that path-connectedness has been lost. The cure, when it exists, is to also assume *local path-connectedness*: under local path-connectedness, components and path-components coincide, and the topologist's-sine-curve pathology cannot happen.

**Oscillation is the canonical mechanism of discontinuity: a function whose values densely cycle in every neighbourhood of a point cannot have a limit there.** This is the *single insight* that makes the no-path proof work. $\sin(1/x)$ as $x \to 0^+$ visits the entire range $[-1, 1]$ in every interval $(0, \varepsilon)$, and that is incompatible with having a limit. The same mechanism shows up in the dyadic rationals, in characteristic functions of dense sets, in the Dirichlet function, and in countless quantum-mechanical wave-packet examples — anywhere a function refuses to settle. The trigger: when asked whether a function extends continuously to a boundary point, ask whether its values oscillate densely, and if so, the answer is no.

**The "sup of the preimage of the bad set" is the canonical contradiction-point in continuity arguments on $[0, 1]$.** This same shape — let $T = \gamma^{-1}(\text{closed set})$, take $t_0 = \sup T$, derive a contradiction from continuity at $t_0$ — appears in many proofs in topology: the connectedness of $[0, 1]$ above, the topologist's sine curve here, lifting theorems for covering spaces ("the set of times at which a lift exists is open and closed in $[0, 1]$"), the proof that $\pi_1(S^1) = \mathbb{Z}$. The supremum is always the place where the contradictory transition between "good" and "bad" is forced to happen, and continuity is always the thing that fails there. Recognize the pattern: any time you have a continuous function on $[0, 1]$ and a closed set whose preimage is closed, look at the supremum of the preimage.

**Closed graph plus oscillation defeats sequential continuity, but never net continuity — this is what nets are for.** Even in the topologist's sine curve, *nets* could distinguish the limit behaviour at $(0, y)$ for any $y$ (different nets approaching $(0, y)$ from different angles, with different limits), and indeed the failure of path-connectedness *is* a failure of having a directed convergence path. The deeper unifying view: path-connectedness is a *parametric* connectedness statement (the parameter is $t \in [0, 1]$), and it fails when the connectedness in the closure is too "irregular" to be parametrised by an interval. Connectedness alone does not enforce regularity of parametrisation, which is why the gap exists. This makes the topologist's sine curve the prototype for path-connectedness *failures*, and motivates the introduction of local path-connectedness as the cleanest sufficient condition for path = connected.

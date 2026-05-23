---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Atlas and Smooth Structure"
  - "Def - Transition Function"
  - "Thm - Product of Smooth Manifolds is a Smooth Manifold"
tags: [geometry, differential-geometry]
---

# Problem Statement

Realize the $n$-torus as the quotient $T^n = \mathbb{R}^n / \mathbb{Z}^n$ — the quotient of $\mathbb{R}^n$ by the action of $\mathbb{Z}^n$ via translation $(x, k) \mapsto x + k$. Equip $T^n$ with the quotient topology.

(a) Verify the natural projection $\pi : \mathbb{R}^n \to T^n$ is an open map and that the $\mathbb{Z}^n$-action on $\mathbb{R}^n$ is free and properly discontinuous.

(b) Construct a smooth atlas on $T^n$ by restricting $\pi$ to small open subsets where it becomes a homeomorphism onto its image.

(c) Compute a sample transition function and verify smoothness.

(d) Show that this smooth structure coincides with the product smooth structure on $T^n = S^1 \times \cdots \times S^1$ (where $S^1 = \mathbb{R}/\mathbb{Z}$ is the circle).

**Recall:**

The smooth atlas / smooth structure framework:

![[Def - Smooth Atlas and Smooth Structure#The Definition]]

The product manifold theorem:

![[Thm - Product of Smooth Manifolds is a Smooth Manifold#Statement]]

The $\mathbb{Z}^n$-action on $\mathbb{R}^n$ by translation: $k \cdot x = x + k$ for $k \in \mathbb{Z}^n$, $x \in \mathbb{R}^n$. Two points $x, y \in \mathbb{R}^n$ are equivalent iff $y - x \in \mathbb{Z}^n$.

---

# Convergent Strategy

**Problem class:** Constructing a smooth structure on a quotient of a smooth manifold by a discrete group action — type 2 of the problem-solving routine in [[Differential Geometry I — Smooth Manifolds and Atlases#Problem-Solving Strategy]]. The key sub-problem is to verify the group action is *free* and *properly discontinuous*, which guarantees the quotient is a topological manifold; then lift charts from $\mathbb{R}^n$ to make it a smooth manifold.

**Assumption pattern:** The action of $\mathbb{Z}^n$ on $\mathbb{R}^n$ has two properties that make the quotient construction work: (i) *free*: no nontrivial group element fixes any point (translation by $k \neq 0$ moves every point); (ii) *properly discontinuous*: for any compact $K \subseteq \mathbb{R}^n$, only finitely many elements $k \in \mathbb{Z}^n$ satisfy $K \cap (K + k) \neq \emptyset$. Together these make $\pi : \mathbb{R}^n \to T^n$ a *covering map*, and standard covering-space theory makes $T^n$ a topological manifold; the smooth structure descends because the action is by *smooth* maps (translations).

**Theorem routing:** Either of two routes:
- **Direct route:** lift charts on $\mathbb{R}^n$ to $T^n$ by restricting $\pi$ to open sets of diameter less than $1$ (where $\pi$ is a homeomorphism onto its image), verify smoothness of transitions.
- **Product route:** Identify $T^n = S^1 \times \cdots \times S^1$ as a product of $n$ circles, invoke [[Thm - Product of Smooth Manifolds is a Smooth Manifold]] and the smooth structure on $S^1 = \mathbb{R}/\mathbb{Z}$ (the case $n = 1$ of the direct route).

We perform the direct route in (a)–(c) and verify equivalence with the product route in (d).

**Key decision point:** The non-obvious choice is the *size* of the lifting open sets. Charts on $T^n$ are obtained by restricting $\pi$ to small enough open sets in $\mathbb{R}^n$ — specifically, open balls of diameter less than $1/2$ (to ensure no two points of the ball are $\mathbb{Z}^n$-equivalent). A larger open set would fail injectivity of $\pi$; a smaller one is fine but unnecessary. Once the right size is chosen, the chart is the inverse of $\pi$ restricted to that ball.

---

# Legal Operations Used

1. **Operation 1 from the topic page (cover with charts).** We choose a cover of $T^n$ by images of small open balls in $\mathbb{R}^n$ under $\pi$, and let the chart maps be the inverses of $\pi|_{\text{ball}}$.

2. **Operation 2 from the topic page (compute transition functions).** On overlaps, the transition functions are *integer translations* (a fixed $k \in \mathbb{Z}^n$), which are smooth maps of $\mathbb{R}^n$.

3. **Operation 5 from the topic page (take a product).** Alternative construction via $T^n = S^1 \times \cdots \times S^1$.

4. **Operation 7 from the topic page (quotient by a properly discontinuous group action).** $T^n = \mathbb{R}^n / \mathbb{Z}^n$ is the prototype of this construction.

5. **Operation 8 from the topic page (verify Hausdorff and second countability).** Both follow from the properly discontinuous action of $\mathbb{Z}^n$ on Hausdorff second-countable $\mathbb{R}^n$.

---

# Hints

> [!note]- Hint 1
> Picture $T^2$ as the unit square $[0, 1]^2$ with opposite sides identified — the $\mathbb{Z}^2$ action on $\mathbb{R}^2$ is by integer translations, and the *fundamental domain* (a region containing exactly one representative of each orbit) is the unit square. The quotient is the square with $(0, y) \sim (1, y)$ and $(x, 0) \sim (x, 1)$ — topologically a torus.

> [!note]- Hint 2
> A chart on $T^n$ from $\mathbb{R}^n$: pick an open ball $B = B_r(x_0) \subseteq \mathbb{R}^n$ with $r < 1/2$. Then no two points of $B$ are $\mathbb{Z}^n$-equivalent (their difference would be in $\mathbb{Z}^n \setminus \{0\}$, hence have norm $\geq 1 > 2r$). So $\pi|_B : B \to \pi(B)$ is a homeomorphism; its inverse is a chart map for $T^n$ defined on the open set $\pi(B)$.

> [!note]- Hint 3
> The transition function between two charts (lifts of overlapping open balls $B_1, B_2$ in $\mathbb{R}^n$) is the *deck transformation* — translation by the unique $k \in \mathbb{Z}^n$ that takes a chosen representative of an overlapping point in one chart to the corresponding representative in the other.

> [!note]- Hint 4
> To verify the quotient is Hausdorff: take two non-equivalent points $x, y \in \mathbb{R}^n$; the difference $x - y \notin \mathbb{Z}^n$ implies $\inf_{k \in \mathbb{Z}^n} |x - y - k| > 0$ (because $\mathbb{Z}^n$ is discrete and closed in $\mathbb{R}^n$). Pick $\varepsilon$ less than half this infimum; then $B_\varepsilon(x)$ and $B_\varepsilon(y)$, after $\pi$-saturation, become disjoint open neighbourhoods in $T^n$.

---

# Solution

The proof breaks into four steps. Step 1 verifies the $\mathbb{Z}^n$-action is free and properly discontinuous, and that $\pi$ is an open map. Step 2 constructs the lifting atlas. Step 3 computes transitions and verifies smoothness. Step 4 identifies the resulting smooth structure with the product structure $S^1 \times \cdots \times S^1$. The non-obvious move is in Step 1: the *properly discontinuous* hypothesis, which is what allows the quotient to be Hausdorff and second-countable.

**Step 1: The $\mathbb{Z}^n$-action on $\mathbb{R}^n$ is free and properly discontinuous; $\pi$ is open.**

The $\mathbb{Z}^n$-action $(k, x) \mapsto x + k$ is:
- *Free*: $x + k = x$ implies $k = 0$.
- *Properly discontinuous*: for any compact $K \subseteq \mathbb{R}^n$, the set $\{k \in \mathbb{Z}^n : K \cap (K + k) \neq \emptyset\}$ is finite.
The projection $\pi$ is an open map: for $W \subseteq \mathbb{R}^n$ open, $\pi^{-1}(\pi(W)) = \bigcup_{k \in \mathbb{Z}^n} (W + k)$, a union of open sets.

> [!note]- Derivation
> *Free.* $x + k = x \Leftrightarrow k = 0$, trivially.
>
> *Properly discontinuous.* Let $K$ be compact in $\mathbb{R}^n$. There is $R > 0$ with $K \subseteq B_R(0)$. If $K \cap (K + k) \neq \emptyset$, there exist $x \in K, y \in K$ with $y = x + k$, so $|k| = |y - x| \leq |y| + |x| \leq 2R$. Hence $k$ is in the finite set $\mathbb{Z}^n \cap B_{2R}(0)$.
>
> *Open map.* For $W \subseteq \mathbb{R}^n$ open, the saturation $\pi^{-1}(\pi(W)) = \{x + k : x \in W, k \in \mathbb{Z}^n\} = \bigcup_{k \in \mathbb{Z}^n} (W + k)$. Each $W + k$ is open (translation is a homeomorphism), so the union is open. Therefore $\pi(W)$ is open in $T^n$ (by the definition of the quotient topology).

**Step 2: Construct the lifting smooth atlas.**

For each $x_0 \in \mathbb{R}^n$, pick the open ball $B_r(x_0)$ of radius $r < 1/2$. Then $\pi|_{B_r(x_0)} : B_r(x_0) \to \pi(B_r(x_0))$ is a homeomorphism onto an open subset of $T^n$. Define the chart $(U_{x_0}, \varphi_{x_0})$ where $U_{x_0} = \pi(B_r(x_0))$ and $\varphi_{x_0} = (\pi|_{B_r(x_0)})^{-1}$, so $\varphi_{x_0} : U_{x_0} \to B_r(x_0) \subseteq \mathbb{R}^n$ is a homeomorphism. The collection $\{(U_{x_0}, \varphi_{x_0})\}_{x_0 \in \mathbb{R}^n}$ is an atlas on $T^n$ (the domains cover, since $\{\pi(B_r(x_0)) : x_0 \in \mathbb{R}^n\}$ covers $T^n$).

> [!note]- Derivation
> *$\pi|_{B_r(x_0)}$ is injective.* Take $x, y \in B_r(x_0)$ with $\pi(x) = \pi(y)$, i.e. $y - x \in \mathbb{Z}^n$. Since $|y - x| \leq |y - x_0| + |x_0 - x| < 2r < 1$ and the smallest nonzero element of $\mathbb{Z}^n$ has norm $\geq 1$, we conclude $y - x = 0$, so $x = y$.
>
> *Homeomorphism.* $\pi$ is continuous (definition of quotient topology) and an open map (Step 1), so its restriction to an open set on which it is injective is a homeomorphism onto its image.
>
> *Charts cover.* Every $[x] \in T^n$ has a representative $x \in \mathbb{R}^n$, and $[x] \in \pi(B_r(x)) = U_x$. So the union of all $U_{x_0}$ as $x_0$ ranges over $\mathbb{R}^n$ is $T^n$. (One can extract a countable subcover by taking $x_0$ with rational coordinates.)

**Step 3: Compute transition functions; verify smoothness.**

Take two charts $(U_{x_1}, \varphi_{x_1})$ and $(U_{x_2}, \varphi_{x_2})$ with $U_{x_1} \cap U_{x_2} \neq \emptyset$. The transition function $\varphi_{x_2} \circ \varphi_{x_1}^{-1}$ on a connected component of $\varphi_{x_1}(U_{x_1} \cap U_{x_2}) \subseteq B_r(x_1)$ is a *translation by an integer vector* $k_0 \in \mathbb{Z}^n$ (depending on the connected component). Translations are smooth on all of $\mathbb{R}^n$, in particular on each connected component of the domain. Therefore the charts are smoothly compatible.

> [!note]- Derivation
> A connected component of $\varphi_{x_1}(U_{x_1} \cap U_{x_2})$ in $B_r(x_1)$ corresponds to a single $\mathbb{Z}^n$-translation taking some neighbourhood in $B_r(x_1)$ to $B_r(x_2)$.
>
> Take $x \in \varphi_{x_1}(U_{x_1} \cap U_{x_2})$. By definition $\varphi_{x_1}^{-1}(x) = \pi(x) \in U_{x_1} \cap U_{x_2}$, so $\pi(x) \in U_{x_2} = \pi(B_r(x_2))$, meaning $\pi(x) = \pi(y)$ for some $y \in B_r(x_2)$. So $y - x \in \mathbb{Z}^n$ — call this difference $k_0$. Then $\varphi_{x_2}(\pi(x)) = y = x + k_0$.
>
> By continuity of $\varphi_{x_2} \circ \varphi_{x_1}^{-1}$ on a connected component, and since $\mathbb{Z}^n$ is discrete, the integer $k_0$ is *locally constant*, hence constant on each connected component of the domain. So $\varphi_{x_2} \circ \varphi_{x_1}^{-1}(x) = x + k_0$ for all $x$ in that component. Translation by a constant vector $k_0$ is a smooth map. The inverse $\varphi_{x_1} \circ \varphi_{x_2}^{-1}(y) = y - k_0$ is also smooth.
>
> So the atlas $\{(U_{x_0}, \varphi_{x_0})\}$ is smooth. By [[Thm - Smooth Structure from Maximal Atlas]], it determines a unique smooth structure on $T^n$.

**Step 4: Identify with the product smooth structure $S^1 \times \cdots \times S^1$.**

The $n = 1$ case ($S^1 = \mathbb{R}/\mathbb{Z}$) gives the standard smooth structure on the circle. The product $S^1 \times \cdots \times S^1$ has the product smooth structure ([[Thm - Product of Smooth Manifolds is a Smooth Manifold]]). The map $T^n \to S^1 \times \cdots \times S^1$ given by $[x^1, \dots, x^n] \mapsto ([x^1], \dots, [x^n])$ — projection onto each coordinate's $\mathbb{Z}$-quotient — is a smooth bijection with smooth inverse; the two smooth structures coincide.

> [!note]- Derivation
> The map $\Phi : T^n \to S^1 \times \cdots \times S^1$, $[x] = [x^1, \dots, x^n] \mapsto ([x^1], \dots, [x^n])$, is well-defined (depends only on the equivalence class). It is continuous (lifts to the identity on $\mathbb{R}^n$ followed by componentwise projection, which is continuous).
>
> *$\Phi$ is bijective.* Two equivalence classes $[x], [y] \in T^n$ are equal iff $y - x \in \mathbb{Z}^n$ iff $y^i - x^i \in \mathbb{Z}$ for each $i$ iff $[x^i] = [y^i]$ in $S^1$ for each $i$ iff $\Phi([x]) = \Phi([y])$. ✓
>
> *Smoothness in both directions.* In local coordinates: an open subset $U_{x_0}$ of $T^n$ as defined in Step 2 maps to a product of open subsets of $S^1$ via the chart $\varphi_{x_0}$ followed by componentwise lift. The lift is the identity in coordinates, so $\Phi$ in coordinates is the identity (modulo unwrapping each circle's quotient). It is smooth, with smooth inverse.
>
> *Conclusion.* The smooth structure on $T^n = \mathbb{R}^n/\mathbb{Z}^n$ from the lifting atlas equals the product smooth structure on $T^n = S^1 \times \cdots \times S^1$.

> [!note]- Complete formal solution
> **Claim.** The quotient $T^n = \mathbb{R}^n / \mathbb{Z}^n$ is a smooth $n$-manifold, with smooth structure determined by the lifting atlas described below. This smooth structure agrees with the product smooth structure on $T^n = S^1 \times \cdots \times S^1$.
>
> *Proof.*
>
> **Step 0 — Topological setup.** $\mathbb{R}^n$ is Hausdorff and second-countable. The $\mathbb{Z}^n$-action by translation is free (trivially) and properly discontinuous (for any compact $K \subseteq B_R(0)$, the set $\{k : K \cap (K + k) \neq \emptyset\} \subseteq \mathbb{Z}^n \cap B_{2R}(0)$ is finite). The projection $\pi : \mathbb{R}^n \to T^n$ is an open map (since $\pi^{-1}(\pi(W)) = \bigcup_k (W + k)$ is a union of opens for any open $W$). By standard covering-space theory, $T^n$ is Hausdorff and second-countable.
>
> **Step 1 — Construct the lifting atlas.** For $x_0 \in \mathbb{R}^n$, the restriction $\pi|_{B_{1/4}(x_0)}$ is injective: if $\pi(y) = \pi(z)$ for $y, z \in B_{1/4}(x_0)$, then $z - y \in \mathbb{Z}^n$ and $|z - y| < 1/2 < 1$, forcing $z - y = 0$. So $\pi|_{B_{1/4}(x_0)}$ is a continuous bijection from the open set $B_{1/4}(x_0)$ onto $\pi(B_{1/4}(x_0))$ (open in $T^n$ by the open-map property). The inverse $\varphi_{x_0} = (\pi|_{B_{1/4}(x_0)})^{-1}$ is continuous (since $\pi$ is open), so $\pi|_{B_{1/4}(x_0)}$ is a homeomorphism. The chart $(U_{x_0}, \varphi_{x_0})$ with $U_{x_0} = \pi(B_{1/4}(x_0))$ is a chart of $T^n$.
>
> The charts $\{(U_{x_0}, \varphi_{x_0})\}_{x_0 \in \mathbb{Q}^n}$ (with $x_0$ ranging over a countable dense subset) cover $T^n$: every $[x] \in T^n$ is $[x_0]$ for some $x_0 \in \mathbb{Q}^n$ within distance $1/4$ of $x$, hence $[x] \in U_{x_0}$.
>
> **Step 2 — Smooth compatibility.** Two charts $(U_{x_1}, \varphi_{x_1}), (U_{x_2}, \varphi_{x_2})$ have transition function $\varphi_{x_2} \circ \varphi_{x_1}^{-1}$. On each connected component $C$ of $\varphi_{x_1}(U_{x_1} \cap U_{x_2})$, this transition is the translation by a unique $k_0 \in \mathbb{Z}^n$ (the difference between corresponding points in the two preimages, locally constant by discreteness of $\mathbb{Z}^n$). Translation by $k_0$ is $C^\infty$ on $\mathbb{R}^n$, in particular on the connected component. By symmetry, the inverse transition is smooth. So the lifting atlas is smooth.
>
> **Step 3 — Smooth structure.** By [[Thm - Smooth Structure from Maximal Atlas]], the lifting atlas determines a unique smooth manifold structure on $T^n$.
>
> **Step 4 — Equivalence with the product structure.** The map $\Phi : T^n = \mathbb{R}^n/\mathbb{Z}^n \to (S^1)^n$, $[x] \mapsto ([x^1], \dots, [x^n])$, is a well-defined bijection (verified by coordinate-by-coordinate equivalence). In local coordinates: a chart $\varphi_{x_0}$ of $T^n$ maps to a product of $n$ charts on $S^1$ (one for each coordinate, lifting on $B_{1/4}(x_0^i)$), and $\Phi$ becomes the identity in coordinates. So $\Phi$ is a smooth diffeomorphism, and the lifting atlas on $T^n$ and the product atlas on $(S^1)^n$ are smoothly compatible — they determine the same smooth structure. $\blacksquare$

> [!warning] Illegal but tempting alternative route: use the quotient theorem for Lie groups
> One might try to invoke "the quotient of a Lie group by a closed subgroup is a smooth manifold" (a theorem from [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]]) — $\mathbb{R}^n$ is a Lie group under addition, $\mathbb{Z}^n$ is a closed (discrete) subgroup, so $T^n = \mathbb{R}^n/\mathbb{Z}^n$ is a smooth manifold of dimension $n - 0 = n$. This is correct, but invokes a substantial theorem (the *closed subgroup theorem*) that is more advanced than needed. The direct lifting-atlas construction is more elementary and gives explicit coordinates.

> [!warning] Sanity-check via the product structure
> Computing the smooth structure on $T^n$ two different ways — by direct quotient and by product — and verifying they agree (Step 4) is a sanity check: both constructions should give the same smooth manifold, and indeed they do.

---

# Key Takeaways

**Charts on a quotient manifold are "lifted from a fundamental domain."** When a manifold $M$ is a quotient $\widetilde{M}/\Gamma$ by a discrete group $\Gamma$ acting freely and properly discontinuously, the strategy is to choose a *fundamental domain* — a subset of $\widetilde{M}$ meeting each $\Gamma$-orbit exactly once — and use small open subsets of the fundamental domain as chart domains on $M$. For $T^n = \mathbb{R}^n / \mathbb{Z}^n$, the unit cube $[0,1)^n$ is a fundamental domain, and any open ball of radius $< 1/2$ inside it gives a valid chart on $T^n$.

**Transition functions of a covering quotient are *deck transformations*.** The transition functions of the lifting atlas on $T^n$ are *integer translations* — elements of the deck transformation group $\mathbb{Z}^n$ acting on $\mathbb{R}^n$. This is the *universal property* of covering spaces: the transition functions of any covering map are the deck transformations of the covering action, and they are smooth iff the covering action is by smooth maps. For $T^n$, the deck transformations are smooth (translations by integer vectors), so $T^n$ is a smooth manifold.

**The product structure and the quotient structure on $T^n$ coincide.** Two natural constructions — $T^n = (S^1)^n$ as a product, $T^n = \mathbb{R}^n / \mathbb{Z}^n$ as a quotient — give the same smooth manifold. This is not automatic; it requires verifying that the coordinate-by-coordinate map between the two constructions is a smooth bijection with smooth inverse. The equivalence is a special case of the general fact that *covering spaces commute with finite products*: $\widetilde{X_1 \times \cdots \times X_n} = \widetilde{X_1} \times \cdots \times \widetilde{X_n}$ (universal covers of products are products of universal covers), and for $T^n$ both sides equal $\mathbb{R}^n$.

**Freedom + proper discontinuity of an action = Hausdorff quotient + smoothness propagation.** The two hypotheses on the $\mathbb{Z}^n$-action are exactly what is needed: *free* prevents fixed points (which would make the quotient locally non-Euclidean); *properly discontinuous* ensures the quotient is Hausdorff (so points with different orbits have disjoint open neighbourhoods after $\pi$-saturation). Without proper discontinuity, the quotient by a free action can be non-Hausdorff — e.g., the "irrational rotation" of $\mathbb{R}$ by an irrational $\alpha$ gives a free action of $\mathbb{Z}$ on $\mathbb{R}$, but the quotient is a non-Hausdorff space (the orbits are dense). The lesson: for quotient manifolds, both freedom and proper discontinuity are essential.

**$T^n$ is the configuration space of an $n$-armed planar pendulum.** Each angle $\theta_i \in S^1$ measures the orientation of one arm, and the joint configuration is $(\theta_1, \dots, \theta_n) \in T^n$. The flow of an integrable Hamiltonian system on $T^n$ (in *action-angle* coordinates) consists of independent periodic orbits in each $S^1$ factor — the prototype of *integrable dynamics*. The torus is also the universal cover of countless other manifolds (it covers any flat compact connected manifold), making it the simplest non-trivial example of a compact, parallelizable manifold (and the only compact orientable surface of genus 1).

---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Continuous Map"
  - "Def - Path-Connected Space"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$I = [0,1] \subset \mathbb{R}$ is the unit interval. A **path** in a topological space $X$ is a continuous map $\gamma : I \to X$. The image $\gamma(0)$ is the **start** and $\gamma(1)$ the **end**. A **loop based at $x_0$** is a path with $\gamma(0) = \gamma(1) = x_0$. The constant path at $x_0$ is $c_{x_0}(t) = x_0$. We write $\gamma_0 \simeq \gamma_1$ (rel endpoints) for "path-homotopic rel endpoints", and $[\gamma]$ for the equivalence class. The square $I \times I$ has coordinates $(s, t)$ throughout; $s$ is the **path parameter**, $t$ the **homotopy parameter**. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full notation registry.

---

# Axiom Motivation

The goal is to make precise the intuitive statement "two paths are essentially the same if you can continuously slide one into the other while keeping the endpoints fixed." The word "continuously" is doing serious work — the slide must be continuous *in both* the path parameter and the time parameter — and that joint continuity is what a homotopy formalises. The endpoint-fixing requirement is the subtle part: without it, *every* path in a path-connected space would be "homotopic" to every other (just slide both endpoints over), and the notion would carry no information at all.

The natural object that records a continuous deformation of one path into another is a map from a *square* $I \times I$ into $X$. The first coordinate is the position along the path; the second is the time of deformation. At time $0$ we read off the first path; at time $1$ we read off the second; in between, we read off intermediate paths that interpolate continuously. Why a square and not, say, a line or a triangle? Because we have two independent parameters — where you are along the path, and how far along the deformation you are — and they vary independently. The Cartesian product $I \times I$ is exactly the parameter space of "path indexed by time".

For the endpoints to stay fixed during the deformation, the **left and right edges of the square** must map to the fixed endpoints. The left edge $\{0\} \times I$ traces out the start of every intermediate path — it must all map to $\gamma_0(0) = \gamma_1(0)$. Similarly the right edge $\{1\} \times I$ all maps to the common end. These two edges being constant is exactly the rel-endpoints condition, and it is what guarantees that during the homotopy you are deforming a *family of paths between the same two points* rather than a more general continuous wiggle.

What if we *dropped* the endpoint-fixing condition? Then we get the weaker notion of **homotopy of maps** (without "rel endpoints"), and any path in a path-connected space could be deformed to any other by first sliding the start and end. The result is that every path becomes "homotopic" to a constant, and there is no information to extract. So the endpoint-fixing condition is not a technical decoration; it is what makes the equivalence relation non-trivial. The trade-off is precise: the more you allow the homotopy to move things, the coarser the equivalence relation; the more you constrain it, the finer.

What if we *strengthened* by demanding the homotopy be smooth (when $X$ is a manifold)? Mostly nothing changes — every continuous homotopy of smooth paths can be smoothed by mollification — but you would exclude pathological spaces where the relevant equivalence relation is genuinely topological. Continuous is the right level.

What if we *strengthened* by also requiring the intermediate paths to be reparameterisations of each other? You get a much coarser equivalence — "same image up to traversal speed" — and you lose the ability to distinguish $S^1$ from $D^2$, since both have the same image-up-to-reparameterisation relation on closed paths. The freedom for the intermediate paths to wander away from the image of $\gamma_0$ is essential.

The test of this motivation: with the four-edge boundary condition (constant top? no — top is $\gamma_1$. Constant left and right? yes. Bottom $\gamma_0$, top $\gamma_1$), a reader unfamiliar with the definition should now be able to write it down. The four edges of the square are pre-specified; the only freedom is the interior, and the only requirement on the interior is continuity.

---

# The Definition

Let $X$ be a topological space and let $\gamma_0, \gamma_1 : I \to X$ be paths with the same start and the same end: $\gamma_0(0) = \gamma_1(0)$ and $\gamma_0(1) = \gamma_1(1)$. A **homotopy of $\gamma_0$ to $\gamma_1$ rel endpoints** is a continuous map
$$
H : I \times I \to X
$$
satisfying:

1. **Bottom = $\gamma_0$:** $H(s, 0) = \gamma_0(s)$ for all $s \in I$;
2. **Top = $\gamma_1$:** $H(s, 1) = \gamma_1(s)$ for all $s \in I$;
3. **Left edge constant at the start:** $H(0, t) = \gamma_0(0)$ for all $t \in I$;
4. **Right edge constant at the end:** $H(1, t) = \gamma_0(1)$ for all $t \in I$.

The paths $\gamma_0$ and $\gamma_1$ are **path-homotopic (rel endpoints)** if such an $H$ exists, and we write $\gamma_0 \simeq \gamma_1$. The relation is an equivalence relation on the set of paths from a fixed start $x_0$ to a fixed end $x_1$; the equivalence class of $\gamma$ is denoted $[\gamma]$.

For loops based at a single point $x_0$ (i.e., $\gamma(0) = \gamma(1) = x_0$), the conditions reduce to: $H(s, 0) = \gamma_0(s)$, $H(s, 1) = \gamma_1(s)$, and $H(0, t) = H(1, t) = x_0$ for all $t$ — both vertical edges of the square map to the single point $x_0$.

---

# Categorical / Structural Definition

In the category $\mathbf{Top}$ of topological spaces, a homotopy of paths rel endpoints is the same data as a continuous map $I \to X^I$ (with $X^I$ given the compact-open topology) starting at $\gamma_0$ and ending at $\gamma_1$, factoring through the subspace $X^I_{x_0, x_1}$ of paths from $x_0$ to $x_1$. So path-homotopy rel endpoints is the path-connectedness relation on the space of paths $X^I_{x_0, x_1}$ between fixed endpoints. The set of path-homotopy classes $\pi_0(X^I_{x_0, x_1})$ is exactly the set of equivalence classes; for loops at $x_0$, this is $\pi_1(X, x_0)$ as a set (the group structure comes from path-product).

This viewpoint compresses the definition: "path-homotopic" simply means "in the same path-component of the path-space." Many later constructions become transparent here — the action of $\pi_1$ on higher homotopy groups, the long exact sequence of a fibration, the Eckmann-Hilton dual of suspension — all follow from manipulating function spaces in $\mathbf{Top}$.

---

# Relate to Other Fields / Compression

A homotopy of paths is the **1-dimensional analogue of a homotopy of maps**: a homotopy of maps $f, g : X \to Y$ is a map $X \times I \to Y$ interpolating between them, and a homotopy of paths is the special case where the domain is $I$ and we additionally pin the endpoints. So this is one face of a much more general construction — for higher-dimensional spheres mapped into $X$, one gets the higher homotopy groups $\pi_k(X)$.

It is also the **continuous analogue of a chain homotopy** in homological algebra: two chain maps $f, g$ are chain-homotopic if there is an operator $h$ with $f - g = \partial h + h\partial$, mirroring the relation $H(\cdot, 0) - H(\cdot, 1) = \partial_t H$. The Hurewicz theorem, which compares $\pi_1$ with $H_1$, is one fruit of taking this analogy seriously.

**True name:** the path-homotopy relation is *connectedness of the path-space*. Saying "$\gamma_0$ and $\gamma_1$ are path-homotopic" is *literally* saying "there is a continuous deformation, i.e., a path in the space of paths, joining $\gamma_0$ to $\gamma_1$." This reframing makes $\pi_1(X) = \pi_0(\Omega X)$ where $\Omega X$ is the loop space, which is the conceptual starting point for higher algebraic topology.

---

# Examples / Corollaries

**Is an instance: any two paths in a convex subset of $\mathbb{R}^n$ with the same endpoints are homotopic.** If $\gamma_0, \gamma_1 : I \to U \subseteq \mathbb{R}^n$ with $U$ convex, the **straight-line homotopy** $H(s,t) = (1-t)\gamma_0(s) + t\gamma_1(s)$ does it. The straight line at each $s$ lies in $U$ by convexity, $H$ is continuous because addition and scaling are, and the endpoint conditions are automatic since $\gamma_0$ and $\gamma_1$ agree there. So in $\mathbb{R}^n$, in a convex open set, or in any star-shaped region, path-homotopy collapses to "same endpoints."

**Is an instance: any reparameterisation is path-homotopic to the original.** If $\varphi : I \to I$ is continuous, with $\varphi(0) = 0$ and $\varphi(1) = 1$, then $\gamma \simeq \gamma \circ \varphi$: the homotopy is $H(s,t) = \gamma((1-t)s + t\varphi(s))$, the straight-line interpolation between the parameter $s$ and the new parameter $\varphi(s)$. This is the precise statement that "we don't care how fast you traverse the path", and it is the technical lemma behind associativity of the path-product on homotopy classes.

**Is an instance: the "fold" homotopy from $\gamma \cdot \gamma^{-1}$ to the constant.** For any path $\gamma : I \to X$, the loop $\gamma \cdot \gamma^{-1}$ (go out, come back) is path-homotopic to the constant loop at $\gamma(0)$. The homotopy: $H(s,t)$ traces out the first $t$ of the way out along $\gamma$, sits there, then comes back. Explicitly,
$$H(s,t) = \begin{cases} \gamma(2s(1-t)) & 0 \leq s \leq \tfrac12 \\ \gamma(2(1-s)(1-t)) & \tfrac12 \leq s \leq 1 \end{cases}$$
At $t=0$ this is the full out-and-back loop; at $t=1$ it is the constant.

**Is NOT an instance: the constant loop and the once-traversed circle are not path-homotopic in $S^1$.** Take $X = S^1$, $x_0 = 1$, $\gamma_0 \equiv 1$ the constant loop, $\gamma_1(\theta) = e^{2\pi i \theta}$ the standard loop. They have the same start and end (both at $1$), but no path-homotopy exists — this is the content of $\pi_1(S^1) = \mathbb{Z}$, with $[\gamma_1]$ generating. The obstruction is the **winding number**: $\gamma_0$ winds $0$ times, $\gamma_1$ winds once, and any path-homotopy would have to continuously change the winding number, which is integer-valued and hence locally constant. See [[Thm - Pi_1 of S^1 is Z]].

**Is NOT an instance: two paths with *different* endpoints.** If $\gamma_0(0) \neq \gamma_1(0)$ or $\gamma_0(1) \neq \gamma_1(1)$, the relation simply does not apply — path-homotopy rel endpoints is only defined between paths sharing both endpoints. Without rel-endpoints, you can always slide the endpoints over (in a path-connected space), and the notion becomes trivial.

**Corollary (equivalence relation):** $\simeq$ is reflexive (constant homotopy $H(s,t) = \gamma(s)$), symmetric (reverse the time parameter, $H'(s,t) = H(s, 1-t)$), and transitive (concatenate two homotopies, possibly with a reparameterisation in time). So it makes sense to take homotopy classes $[\gamma]$.

**Corollary (compatibility with reverse):** if $\gamma_0 \simeq \gamma_1$ then $\gamma_0^{-1} \simeq \gamma_1^{-1}$. Just reverse the path parameter, $H'(s,t) = H(1-s, t)$.

**Calibration check.** If you can (a) write down the straight-line homotopy explicitly, (b) state the four boundary conditions of the homotopy square without looking, and (c) explain why a homotopy *without* rel endpoints would make every path trivial in a path-connected space, you have understood the definition. Bonus: sketch the "fold" homotopy and verify the four boundary conditions for it.

---

# Unlocked by This

> [!tip] The Loop Space and Iterated Loop Spaces *(from Higher Algebraic Topology)*
> The set of homotopy classes of loops at $x_0$ is the same as the set of path-components of the **loop space** $\Omega_{x_0} X = \{$continuous $\gamma : I \to X : \gamma(0) = \gamma(1) = x_0\}$ with the compact-open topology. Then $\pi_1(X, x_0) = \pi_0(\Omega X, c_{x_0})$, and iterating, $\pi_n(X) = \pi_{n-1}(\Omega X) = \cdots = \pi_0(\Omega^n X)$. The higher homotopy groups are just $\pi_0$ of iterated loop spaces. This unlocks the entire machinery of **infinite loop spaces** and **spectra** in stable homotopy theory.

> [!tip] Homotopy Equivalence and Weak Equivalence *(from Algebraic Topology I)*
> Two spaces $X, Y$ are **homotopy equivalent** if there are maps $f : X \to Y$ and $g : Y \to X$ with $g \circ f$ homotopic to $\mathrm{id}_X$ and $f \circ g$ homotopic to $\mathrm{id}_Y$ (now using homotopy of maps, not paths). All homotopy invariants — $\pi_1$, $H_*$, cohomology — agree on homotopy-equivalent spaces. So when you want to compute $\pi_1(X)$, you may freely replace $X$ by anything homotopy-equivalent: $\mathbb{R}^n$ is replaced by a point, the annulus by $S^1$, the wedge of two discs by a point. See [[Algebraic Topology I — Singular Homology and the de Rham Theorem]].

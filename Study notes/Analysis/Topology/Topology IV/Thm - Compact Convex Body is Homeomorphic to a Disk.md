---
type: theorem
subject: topology
prereqs:
  - "Def - Convex Body"
  - "Def - Compact Space"
  - "Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism"
tags: [analysis, topology, convexity, classification]
---

# Notation

$C \subseteq \mathbb{R}^n$ a compact convex body with nonempty interior. $D^n = \{x \in \mathbb{R}^n : \|x\| \leq 1\}$ the closed unit ball; $S^{n-1} = \partial D^n$. $\partial C = C \setminus \operatorname{int}(C)$ the topological boundary of $C$. The radial projection $f_C : \partial C \to S^{n-1}$, $x \mapsto x/\|x\|$ (assuming $0 \in \operatorname{int}(C)$). The full registry is on the topic page.

---

# Motivation

A compact convex body $C \subseteq \mathbb{R}^n$ with nonempty interior is the most rigid possible convex object: closed (no missing boundary), bounded (no escaping to infinity), full-dimensional (interior nonempty), and convex (closed under line segments). What is its topology? The answer is the prototype "topological classification" result: it is homeomorphic to the standard closed unit disk $D^n$.

This result is at first surprising. A cube, a tetrahedron, a regular pentagon, a smooth ellipsoid — all wildly different geometrically — are all homeomorphic to $D^n$. The shape, the corners, the smoothness of the boundary — none of these survive at the topological level. Only the *gross structure* matters: a convex closed bounded full-dimensional set is, topologically, "a $D^n$ with a possibly-funny coordinate system on the boundary".

The proof is constructive and explicit. Choose any interior point as the origin. From this origin, every ray exits $C$ at exactly one boundary point (this is what convexity guarantees — Proposition 16.2 in Bredon). The map "boundary point $\to$ direction (unit vector)" is a continuous bijection $\partial C \to S^{n-1}$. It is a homeomorphism by the compact-to-Hausdorff continuous bijection upgrade. Extending radially gives a homeomorphism $C \to D^n$.

The geometric content: convexity is what makes the radial parametrization well-defined (one ray exit point per direction). Closedness ensures the exit point is in $C$. Boundedness ensures the exit point exists. Full-dimensionality ensures we can choose a true interior origin. Each axiom plays a precise role.

---

# Statement

Let $C \subseteq \mathbb{R}^n$ be a compact convex body with nonempty interior. Then $C$ is homeomorphic to the closed unit ball $D^n$, and the boundary $\partial C$ is homeomorphic to $S^{n-1}$:
$$C \cong D^n, \qquad \partial C \cong S^{n-1}.$$

The homeomorphism is constructive: choosing any interior point as origin, the **radial projection** $f : \partial C \to S^{n-1}$, $x \mapsto x/\|x\|$, is a homeomorphism, and it extends to a homeomorphism $k : D^n \to C$, $y \mapsto \|y\| \cdot f^{-1}(y/\|y\|)$ (with $k(0) := 0$).

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "compact convex body with nonempty interior" is the strict version. The theorem applies more broadly:

**Strictly convex bodies.** Property $B$: $C$ is closed convex with $\partial C$ a "smooth" boundary (e.g., the unit ball of a strictly convex norm). The bridge: strict convexity is a special case of convexity; the theorem applies. The boundary is a $C^0$ hypersurface (not necessarily smooth).

**Polytopes.** Property $B$: $C$ is the convex hull of finitely many points in general position. The bridge: a polytope is a compact convex body. *Example:* the $n$-simplex, the $n$-cube, regular polytopes — all are homeomorphic to $D^n$.

**Unit balls of finite-dimensional Banach spaces.** Property $B$: $C$ is the unit ball of a norm on $\mathbb{R}^n$. The bridge: every norm's unit ball is convex (triangle inequality), closed, bounded, and contains $0$ in its interior. *Example:* the unit balls of $\ell^p$ norms for $1 \leq p \leq \infty$ are all homeomorphic to $D^n$, even though their shapes vary continuously with $p$.

**Sublevel sets of convex functions.** Property $B$: $C = \{x : f(x) \leq c\}$ for a continuous convex function $f$ and $c$ above the minimum. The bridge: closed sublevel sets of convex functions are convex bodies (when the function is coercive).

**Targets (Output Amplification)**

The conclusion "$C \cong D^n$" amplifies in topological / geometric settings:

Combine with **a continuous function on $C$.** Property $D$: $g : C \to C$ is continuous. The amplified result $E$: $g$ has a fixed point, by the Brouwer fixed-point theorem (which holds on $D^n$, hence on any homeomorphic space). *Example:* every continuous self-map of a convex body has a fixed point — see [[Ex - The Brouwer fixed-point theorem]].

Combine with **a CW structure.** Property $D$: $C$ has a triangulation (as a polytope, or via simplicial approximation). The amplified result $E$: $C$ is a CW complex with one cell of each dimension up to $n$, equivalent to the standard CW structure on $D^n$.

Combine with **a measure on $C$.** Property $D$: Lebesgue measure restricted to $C$ has finite total mass. The amplified result $E$: $C$ is a probability space (after normalization), and the homeomorphism with $D^n$ transports Lebesgue-like properties.

---

# Why Is It True

The key geometric fact is Proposition 16.2 (Bredon): if $C$ is a compact convex body with $0 \in \operatorname{int}(C)$, then any ray from $0$ meets $\partial C$ in *exactly one* point. The proof: if a ray hits $C$ at $p$ and $q$ with $\|q\| > \|p\|$, then $q$ is in $C$ (by hypothesis), and so is the cone from a small ball around $0$ to $q$ (by convexity, since the ball is in $C$). The point $p$ lies in the interior of this cone, hence in the interior of $C$ — contradicting $p \in \partial C$.

Given this, the radial projection $f : \partial C \to S^{n-1}$ defined by $f(x) = x/\|x\|$ is:

- *Continuous*: composition of the inclusion $\partial C \hookrightarrow \mathbb{R}^n \setminus \{0\}$ with the radial map $r : \mathbb{R}^n \setminus \{0\} \to S^{n-1}$.
- *Injective*: if $f(x) = f(y)$, then $x$ and $y$ lie on the same ray from $0$. By the proposition, $x = y$.
- *Surjective*: for any unit vector $u \in S^{n-1}$, the ray $\{tu : t \geq 0\}$ exits $C$ at some point (since $C$ is bounded), and that point is in $\partial C$.

So $f$ is a continuous bijection. $\partial C$ is compact (closed subset of compact $C$); $S^{n-1}$ is Hausdorff. By [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $f$ is a homeomorphism.

For the extension to $C \cong D^n$: define $k : D^n \to C$ by $k(y) = \|y\| \cdot f^{-1}(y/\|y\|)$ for $y \neq 0$, and $k(0) = 0$. This is continuous (away from $0$ by composition; at $0$ by the bound $\|k(y)\| \leq M \|y\|$ where $M = \max_{x \in C} \|x\|$). Bijective by direct check. Continuous bijection from compact $D^n$ to Hausdorff $C$, hence homeomorphism by the same upgrade.

The reason to expect this: convexity gives a unique radial parametrization, so the convex body is essentially "a ball with a rescaled boundary". The rescaling can be arbitrarily wild geometrically (a cube, a tetrahedron) but topologically it is just a homeomorphism of $S^{n-1}$ to itself, which doesn't change the topology of the body.

The locality of the result: the theorem is *local* in the sense that we choose an interior point as origin; *global* in the sense that the radial map covers all of $\partial C$. The choice of interior point doesn't matter — different choices give homeomorphic radial parametrizations, and the resulting homeomorphism is the composition.

---

# What Makes This Hard

The non-obvious step is Proposition 16.2: showing that any ray exits $C$ at exactly one boundary point. The proof uses convexity and the cone-from-interior-ball trick — given two points on the same ray with one in the interior, the further one's cone with the interior ball contains the closer point in its interior. This requires careful geometric reasoning about cones in $\mathbb{R}^n$. The common error is to assume convexity gives uniqueness by a simpler argument (e.g., from strict convexity, which is *not* assumed).

---

# Rederivation Scaffold

**High-level strategy:**
Translate to put $0$ in the interior of $C$. The radial projection $f : \partial C \to S^{n-1}$ is a continuous bijection by convexity (Proposition 16.2). Use compact-to-Hausdorff upgrade. Extend radially to get $C \cong D^n$.

**Subgoal decomposition:**

1. **Translate $0$ to an interior point.** Choose $p \in \operatorname{int}(C)$; replace $C$ by $C - p$.
   - *Hint:* Translation is a homeomorphism.

2. **Show any ray exits $\partial C$ at one point (Proposition 16.2).** If two points on the same ray are in $C$, the further one's cone with the interior ball contains the closer.
   - *Hint:* Convexity + open ball at origin.

3. **Define radial projection $f : \partial C \to S^{n-1}$.** $f(x) = x/\|x\|$, continuous as a restriction of the radial retraction $\mathbb{R}^n \setminus \{0\} \to S^{n-1}$.

4. **Show $f$ is a continuous bijection.** Injective: by step 2. Surjective: by boundedness of $C$.

5. **Upgrade to homeomorphism.** $\partial C$ compact, $S^{n-1}$ Hausdorff; apply [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]].

6. **Extend to $C \cong D^n$.** Define $k : D^n \to C$ by $k(y) = \|y\| \cdot f^{-1}(y/\|y\|)$, $k(0) = 0$. Continuous bijection, compact-Hausdorff upgrade.

---

# Lemma Decomposition

> [!note]- Lemma 1: A ray from an interior point exits $C$ at exactly one boundary point
> **Statement:** (Bredon Proposition 16.2.) If $C$ is a convex body and $0 \in \operatorname{int}(C)$, then any ray $R = \{tu : t \geq 0\}$ from $0$ meets $\partial C$ at exactly one point.
>
> **Hint:** Suppose two points $p, q$ on $R$ are in $C$ with $\|q\| > \|p\|$. Use the open ball at $0$ and convexity to put $p$ in the interior.
>
> **Why needed:** The radial map's injectivity.
>
> > [!note]- Full proof
> > $C$ is bounded, so $R \cap C$ is bounded and the supremum of $t$ with $tu \in C$ is finite. Call the supremum point $q$. Then $q \in \overline{C} = C$ (since $C$ is closed). Is $q \in \partial C$? If $q \in \operatorname{int}(C)$, then a small ball around $q$ is in $C$, contradicting the supremality of $t$.
> >
> > For uniqueness: suppose $p \in R \cap \partial C$ with $\|p\| < \|q\|$. There is an open ball $B \subseteq C$ around $0$ (since $0$ is interior). Consider the union of segments from points of $B$ to $q$: this is the cone $\operatorname{Cone}(B, q) = \{(1-s)b + sq : b \in B, s \in [0, 1]\}$. By convexity (each segment is in $C$), the cone is in $C$. The point $p = (\|p\|/\|q\|)q \in R$ has "scaling factor" $s_0 = \|p\|/\|q\| \in (0, 1)$, and $p = s_0 q = s_0 q + (1 - s_0) \cdot 0$. So $p$ is on the segment from $0$ to $q$, hence in the cone. Now, for $s$ close to $s_0$ and $b$ near $0$ (in $B$), the point $(1-s)b + sq$ is near $p$ — varying over an open neighborhood of $p$. So $p \in \operatorname{int}(\operatorname{Cone}(B, q)) \subseteq \operatorname{int}(C)$, contradicting $p \in \partial C$.
> >
> > So the exit point is unique, namely $q$.

> [!note]- Lemma 2: The radial map $\partial C \to S^{n-1}$ is a continuous bijection
> **Statement:** $f : \partial C \to S^{n-1}$, $f(x) = x/\|x\|$, is a continuous bijection.
>
> **Hint:** Composition of inclusion with normalization.
>
> **Why needed:** The first homeomorphism.
>
> > [!note]- Full proof
> > *Continuous:* $f$ is the composition $\partial C \hookrightarrow \mathbb{R}^n \setminus \{0\} \xrightarrow{r} S^{n-1}$, where the inclusion is continuous and $r(x) = x/\|x\|$ is continuous (away from $0$, which is in the interior of $C$, hence not in $\partial C$). So $f$ is continuous.
> >
> > *Bijective:* By Lemma 1, each ray $\{tu : t \geq 0\}$ meets $\partial C$ at exactly one point, so $f^{-1}(u)$ is a singleton for each $u \in S^{n-1}$. Surjective and injective.

---

# Formal Proof

> [!note]- Complete formal proof
> By translation, assume $0 \in \operatorname{int}(C)$.
>
> **Radial map on the boundary is a homeomorphism.** By Lemma 2, $f : \partial C \to S^{n-1}$, $f(x) = x/\|x\|$, is a continuous bijection. $\partial C$ is closed in the compact $C$, hence compact. $S^{n-1}$ is Hausdorff (subspace of $\mathbb{R}^n$). By [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $f$ is a homeomorphism.
>
> **Extend to the full body.** Define $k : D^n \to C$ by
> $$k(y) = \begin{cases} \|y\| \cdot f^{-1}(y/\|y\|) & y \neq 0 \\ 0 & y = 0 \end{cases}$$
>
> *Continuity away from $0$:* composition of continuous maps $y \mapsto y/\|y\|$ (continuous on $\mathbb{R}^n \setminus \{0\}$), $f^{-1}$, $u \mapsto \|y\| u$ (scalar multiplication is continuous).
>
> *Continuity at $0$:* Since $C$ is compact, $M := \max_{x \in C} \|x\|$ is finite. For $y \neq 0$, $\|k(y)\| = \|y\| \cdot \|f^{-1}(y/\|y\|)\| \leq M \|y\|$. So as $y \to 0$, $k(y) \to 0 = k(0)$. Continuous at $0$.
>
> *Bijective:* injective because both the scaling $\|y\|$ and the direction $f^{-1}(y/\|y\|)$ are determined by $y$. Surjective: for $x \in C$ with $x \neq 0$, the ray through $x$ exits $\partial C$ at some $p$; set $y = \|x\|/\|p\| \cdot (x/\|x\|) \cdot 1 = (\|x\|/\|p\|) \cdot (x/\|x\|)$. Then $\|y\| = \|x\|/\|p\| \leq 1$ (since $x$ on the ray from $0$ through $p$, with $\|x\| \leq \|p\|$). And $k(y) = (\|x\|/\|p\|) \cdot p = (\|x\|/\|p\|) \cdot \|p\| \cdot (x/\|x\|) = x$. So $k$ is surjective.
>
> *Homeomorphism:* $k$ is a continuous bijection from compact $D^n$ to Hausdorff $C$, so $k$ is a homeomorphism. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Brouwer fixed-point theorem extends from $D^n$ to convex bodies.** Every continuous self-map of a compact convex set in $\mathbb{R}^n$ has a fixed point. The proof: homeomorphism $D^n \cong C$ transports the fixed point of $f$ (which exists on $D^n$ by Brouwer) to $C$. This is the Schauder fixed-point theorem in finite dimensions; it extends to infinite-dimensional convex sets in TVSs (Schauder-Tychonoff).

**The Krein-Milman theorem.** Every compact convex set in a (locally convex) topological vector space is the closed convex hull of its extreme points. The finite-dimensional case is geometric ($D^n$'s extreme points are $S^{n-1}$); the topological identification is what makes the higher-dimensional case tractable.

**Approximation of convex bodies by polytopes.** Every compact convex body in $\mathbb{R}^n$ can be approximated arbitrarily well (in the Hausdorff metric) by polytopes. The homeomorphism $C \cong D^n$ is the topological backbone; the polytope approximation refines this to a continuous family of homeomorphisms with controlled error.

---

# Bridges

- **[[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]** — the upgrade theorem applied twice (boundary and full body).

- **[[Def - Convex Body]]** — the object of classification.

- **[[Def - Compact Space]]** — compactness is essential for the upgrade.

---

# Unlocked by This

> [!tip] Brouwer Fixed-Point Theorem *(from Algebraic Topology)*
> Every continuous self-map of a compact convex body in $\mathbb{R}^n$ has a fixed point. This generalizes the disk version to all convex bodies via the homeomorphism here. See [[Ex - The Brouwer fixed-point theorem]].

> [!tip] Schauder Fixed-Point Theorem *(from Functional Analysis)*
> Every continuous self-map of a compact convex subset of a Banach space has a fixed point. The finite-dimensional version is Brouwer; the infinite-dimensional version is Schauder's, used for proving existence of solutions to nonlinear PDEs.

> [!tip] Convex Polytope Classification *(from Discrete Geometry)*
> Every $n$-dimensional convex polytope is homeomorphic to $D^n$. The boundary is homeomorphic to $S^{n-1}$ and is a topological sphere even though the combinatorial structure (face lattice, $f$-vectors) can be very different. The homeomorphism is the basis of the Euler-Poincaré formula and the upper bound theorem.

---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Compact Space"
  - "Def - Closure, Interior, and Boundary"
tags: [analysis, topology, convexity]
---

# Notation

$C \subseteq \mathbb{R}^n$ is a subset; $\operatorname{int}(C)$ its topological interior; $\partial C = C \setminus \operatorname{int}(C) = \overline{C} \setminus \operatorname{int}(C)$ its boundary (assuming $C$ closed). $D^n = \{x \in \mathbb{R}^n : \|x\| \leq 1\}$ the closed unit ball. $S^{n-1} = \partial D^n$ the unit sphere. For $p, q \in \mathbb{R}^n$, $[p, q]$ denotes the closed line segment $\{(1-t)p + tq : t \in [0, 1]\}$. The full registry is on the topic page.

---

# Axiom Motivation

A convex set in $\mathbb{R}^n$ is one closed under taking line segments between its points. The geometric content is *no concavities, no holes, no twists*: between any two points of the set, the straight line lies entirely inside. This is the simplest non-trivial geometric property a subset of Euclidean space can have, and it has remarkable topological consequences.

A **convex body** is a convex set that is additionally **closed** and has **nonempty interior**. The closedness ensures we are working with a "completed" set — no missing boundary points — and the nonempty interior ensures the set is "full-dimensional" (not flattened into a lower-dimensional subspace). The combination — closed + convex + interior — defines the class of objects that the §16 classification handles.

Why these three conditions specifically? Each rules out a degenerate case:

- **Drop closedness:** open convex sets (the open ball, an open half-space) are convex but not "bodies" — they lack a boundary. The classification theorem says $C \cong D^n$, the *closed* ball; for open convex sets, the result would say $C \cong \operatorname{int}(D^n) =$ open ball, which is true but is a special case of the closed version.

- **Drop convexity:** a closed set with interior need not be homeomorphic to a disk — think of an annulus or a figure-eight neighborhood. Convexity is the essential geometric input.

- **Drop nonempty interior:** a closed convex set of strictly lower dimension (a single point, a segment in $\mathbb{R}^2$, a triangle in $\mathbb{R}^3$) is convex but not "full-dimensional" — it does not contain an open ball of $\mathbb{R}^n$. The classification then yields a homeomorphism not with $D^n$ but with the disk in the appropriate dimension (a point, $D^1$, $D^2$ respectively). The "nonempty interior" assumption pins us to the dimension we want.

The convexity axiom can be **strengthened** to **strict convexity** (the line segment between two boundary points lies in the interior, except for the endpoints) — this excludes "flat faces" and ensures the boundary $\partial C$ is in some sense "smooth". The classification theorem of §16 does not need strict convexity, so it applies even to polytopes like the cube. But strict convexity becomes essential for differentiability arguments (the boundary is a $C^1$ hypersurface for strictly convex bodies with smooth boundaries).

The **radial parametrization** is the key technical tool: from any interior point $p \in \operatorname{int}(C)$, every ray from $p$ exits $C$ at exactly one boundary point. This is Proposition 16.2 in Bredon, and it is the convexity-driven analogue of "star-shaped from $p$". The proof: if a ray exits at $q$ and the point $p + tq'$ is interior for some $t' > t$ and $q' \in C$, then convexity of $C$ together with the open-ball neighborhood of $p$ inside $C$ forces $q$ to be interior, contradicting $q \in \partial C$. So the ray meets $\partial C$ in exactly one point, parametrizable by direction.

This gives a continuous bijection $\partial C \to S^{n-1}$ (radial projection from $p$), which extends radially to a homeomorphism $C \cong D^n$ — the content of [[Thm - Compact Convex Body is Homeomorphic to a Disk]].

---

# The Definition

**Convex set.** A subset $C \subseteq \mathbb{R}^n$ is **convex** if for every $p, q \in C$, the line segment $[p, q] = \{(1-t)p + tq : t \in [0, 1]\}$ is contained in $C$.

**Convex body.** A **convex body** $C \subseteq \mathbb{R}^n$ is a closed convex subset of $\mathbb{R}^n$ with nonempty interior. The **boundary** of $C$ is $\partial C = C \setminus \operatorname{int}(C)$.

**Compact convex body.** A **compact convex body** is a convex body that is additionally compact — equivalently (by Heine-Borel), closed and bounded.

**Strictly convex.** A convex body $C$ is **strictly convex** if for every $p \neq q$ in $C$ and $t \in (0, 1)$, the point $(1-t)p + tq$ lies in $\operatorname{int}(C)$.

---

# Relate to Other Fields / Compression

A convex body is the topological-geometric primitive underlying **convex analysis** and **convex optimization**. Every closed convex function $f : \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ has as its sublevel sets $\{x : f(x) \leq c\}$ convex bodies (when $c$ is large enough). Conversely, every convex body $C$ defines its **support function** $h_C(\xi) = \sup_{x \in C} \langle \xi, x \rangle$, which is convex and positively homogeneous; this gives a duality between convex bodies and convex functions.

In **functional analysis**, the analogue is a **convex body in a Banach space**: a closed bounded convex subset with nonempty interior. The Banach-Alaoglu theorem says the unit ball of the dual space is weak-* compact (a "weak-* convex body"); the Krein-Milman theorem says every compact convex set in a topological vector space is the closed convex hull of its extreme points.

In **integral geometry**, convex bodies are the natural objects for measuring "intrinsic volumes" (volume, surface area, Euler characteristic, etc.). The Steiner formula and Hadwiger's theorem give a clean axiomatic description.

---

# Examples and Corollaries

**Is an instance — the closed unit ball $D^n$.** $D^n = \{x \in \mathbb{R}^n : \|x\| \leq 1\}$ is convex (the line segment between two unit-ball points is itself in the ball, by the triangle inequality for the norm), closed, and has nonempty interior (the open unit ball). The prototype convex body and the target of the classification theorem.

**Is an instance — the cube $[-1, 1]^n$.** Convex (line segments in a box stay in the box), closed (intersection of closed half-spaces), with nonempty interior. By [[Thm - Compact Convex Body is Homeomorphic to a Disk]], $[-1, 1]^n \cong D^n$. See [[Ex - The cube and the ball]].

**Is an instance — the standard $n$-simplex.** $\Delta^n = \{(x_0, \dots, x_n) \in \mathbb{R}^{n+1} : x_i \geq 0, \sum x_i = 1\}$ is convex (convex combinations preserve the affine constraints), closed (intersection of half-spaces and a hyperplane), and has nonempty interior *as a subset of the hyperplane $\sum x_i = 1$* (relative interior). The simplex is a convex body in this hyperplane, of dimension $n$, hence $\Delta^n \cong D^n$. See [[Ex - Every n-simplex is homeomorphic to the disk]].

**Is an instance — an ellipsoid.** $E = \{x \in \mathbb{R}^n : \sum (x_i/a_i)^2 \leq 1\}$ for positive $a_i$ is convex, closed, with interior. Homeomorphic to $D^n$ via the linear map $(x_i) \mapsto (x_i/a_i)$.

**Is NOT an instance — an annulus.** The set $\{x \in \mathbb{R}^2 : 1 \leq \|x\| \leq 2\}$ is closed and has interior, but it is *not* convex: the line segment between $(1, 0)$ and $(-1, 0)$ passes through $(0, 0)$, which is not in the annulus. So an annulus is not a convex body, and it is *not* homeomorphic to $D^2$ — it has a hole.

**Is NOT an instance — a single point.** $\{p\}$ is convex and closed, but its interior in $\mathbb{R}^n$ is empty. It is a 0-dimensional convex set, but not a convex body. Similarly, a closed segment $[0, 1] \subseteq \mathbb{R}^2$ has empty interior in $\mathbb{R}^2$.

**Is NOT an instance — the open ball.** $\{x : \|x\| < 1\}$ is convex with nonempty interior, but is not *closed*. It is not a convex body by Bredon's definition. (However, $D^n$ is the closure, which *is*.)

**Corollary — convex bodies are connected and path-connected.** Convexity directly implies path-connectedness: any two points are connected by a line segment. So a convex body is path-connected, hence connected.

**Corollary — convex bodies are simply connected.** Any loop in $C$ can be contracted to a point via straight-line homotopies (linearly interpolate to any chosen base point $p$, using convexity to keep the homotopy inside $C$). So $\pi_1(C) = 0$, and inductively $\pi_n(C) = 0$ for all $n$ — convex bodies are *contractible*.

**Corollary — every interior point is a star-center.** For $p \in \operatorname{int}(C)$ and any $q \in C$, the segment $[p, q] \subseteq C$ (convexity), and an open neighborhood of $p$ lies in $C$ (interior). One can show that the segment lies in $\operatorname{int}(C)$ for $t < 1$ — the set is "star-shaped from $p$" in a strong sense. This is the key input to the radial parametrization.

**Calibration check.** Verify: a regular polygon is a convex body in $\mathbb{R}^2$; a circle (the set $S^1$, just the boundary) is *not* a convex body (empty interior); the convex hull of finitely many points in general position is a convex body (a **polytope**); the intersection of a convex body with a hyperplane through its interior is a convex body in the hyperplane.

---

# Unlocked by This

> [!tip] Support Function and Convex Duality *(from Convex Analysis)*
> Every compact convex body $C$ in $\mathbb{R}^n$ has a **support function** $h_C(\xi) = \sup_{x \in C} \langle \xi, x \rangle$ which is convex and positively homogeneous. The map $C \mapsto h_C$ is a bijection between compact convex bodies (containing $0$) and such functions — the Legendre-Fenchel duality.

> [!tip] Polytope and Combinatorics *(from Discrete Geometry)*
> A **polytope** is a convex body that is the convex hull of finitely many points. Polytopes are the simplest convex bodies and the source of combinatorial topology — their face lattices encode rich structural information (Euler-Poincaré formula, $f$-vectors, Hadwiger's theorem).

> [!tip] Banach Space Geometry *(from Functional Analysis)*
> The unit ball of every Banach space is a convex body. Banach space geometry studies how the shape of the unit ball (smoothness, strict convexity, uniform convexity) relates to analytic properties of the space. Hilbert spaces have the "roundest" unit balls; $L^1$ has corners.

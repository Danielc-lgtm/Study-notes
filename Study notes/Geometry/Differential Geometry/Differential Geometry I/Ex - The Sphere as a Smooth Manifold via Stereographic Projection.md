---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Atlas and Smooth Structure"
  - "Def - Transition Function"
  - "Def - Topological Manifold"
  - "Thm - Smooth Structure from Maximal Atlas"
tags: [geometry, differential-geometry]
---

# Problem Statement

Show that the $n$-sphere $S^n = \{x \in \mathbb{R}^{n+1} : |x| = 1\}$ admits a smooth manifold structure of dimension $n$ via the **stereographic atlas**. Specifically:

(a) Define the stereographic projection $\sigma_N : S^n \setminus \{N\} \to \mathbb{R}^n$ from the north pole $N = (0, \dots, 0, 1)$ and verify it is a homeomorphism onto $\mathbb{R}^n$. Define analogously $\sigma_S : S^n \setminus \{S\} \to \mathbb{R}^n$ from the south pole $S = (0, \dots, 0, -1)$.

(b) Compute the transition function $\sigma_S \circ \sigma_N^{-1} : \mathbb{R}^n \setminus \{0\} \to \mathbb{R}^n \setminus \{0\}$ explicitly.

(c) Verify the transition function is smooth (in fact a diffeomorphism), so $\{(S^n \setminus \{N\}, \sigma_N), (S^n \setminus \{S\}, \sigma_S)\}$ is a smooth atlas on $S^n$.

(d) Conclude that this smooth atlas determines a smooth manifold structure on $S^n$, called the **standard smooth structure**.

**Recall:**

A **smooth atlas** on a topological manifold is a covering family of charts whose transition functions are diffeomorphisms:

![[Def - Smooth Atlas and Smooth Structure#The Definition]]

The transition function:

![[Def - Transition Function#The Definition]]

A topological manifold needs Hausdorff, second-countable, locally Euclidean — $S^n$ as a subspace of $\mathbb{R}^{n+1}$ is Hausdorff and second-countable automatically. Locally Euclidean is established by exhibiting any atlas; this exercise constructs the two-chart stereographic atlas.

---

# Convergent Strategy

**Problem class:** This is a "construct a smooth atlas explicitly" problem — type 1 of the problem-solving routine in [[Differential Geometry I — Smooth Manifolds and Atlases#Problem-Solving Strategy]]. The space is presented as a subset of $\mathbb{R}^{n+1}$, and the goal is to produce an atlas with smooth transition functions, then verify smoothness by direct computation.

**Assumption pattern:** The sphere $S^n$ has a *symmetry* — the antipodal map $x \mapsto -x$ — which makes the north and south poles geometrically interchangeable. We exploit this by constructing two charts that omit each pole respectively. Each chart covers all but one point, and together they cover everything. The Euclidean structure of $\mathbb{R}^{n+1}$ gives us explicit projection formulae.

**Theorem routing:** Once we have a smooth atlas, [[Thm - Smooth Structure from Maximal Atlas]] gives us a unique maximal smooth atlas, hence a smooth manifold structure. The work is in (a)–(c): produce the atlas and verify smoothness.

**Key decision point:** The non-obvious choice is the **inversion map** $u \mapsto u/|u|^2$ as the transition function. To compute it, one inverts $\sigma_N$ to land back on $S^n$, then applies $\sigma_S$, and the result is the inversion. This involves a nontrivial Euclidean-geometry computation: lines from the poles through a point of the sphere intersect the equator-plane at the stereographic images, and computing where these intersect on different hyperplanes requires identifying the right algebraic relationship. The choice of pole position (top/bottom of the sphere) is conventional but standard.

---

# Legal Operations Used

1. **Operation 1 from the topic page (cover with charts).** We name the charts $(S^n \setminus \{N\}, \sigma_N)$ and $(S^n \setminus \{S\}, \sigma_S)$, with the two charts covering $S^n$.

2. **Operation 2 from the topic page (compute transition functions explicitly).** We compute $\sigma_S \circ \sigma_N^{-1}$ on $\mathbb{R}^n \setminus \{0\}$ by directly applying the formula for $\sigma_N^{-1}$ followed by $\sigma_S$. The result is the inversion $u \mapsto u/|u|^2$.

3. **Operation 8 from the topic page (verify Hausdorff and second countability by inheritance).** $S^n$ inherits Hausdorff and second countability from $\mathbb{R}^{n+1}$ via the subspace topology.

---

# Hints

> [!note]- Hint 1
> Think of $\sigma_N(x)$ geometrically: project from $N$ through $x$ to the equator plane $\{x^{n+1} = 0\} \cong \mathbb{R}^n$. The intersection point with this hyperplane is $\sigma_N(x)$. Use similar triangles to derive the formula.

> [!note]- Hint 2
> The inverse $\sigma_N^{-1} : \mathbb{R}^n \to S^n \setminus \{N\}$ sends $u \in \mathbb{R}^n$ to the unique point of $S^n$ on the line through $N$ and $(u, 0)$. Solve $|tN + (1-t)(u, 0)|^2 = 1$ for $t$ and substitute.

> [!note]- Hint 3
> For the transition: starting from $u \in \mathbb{R}^n \setminus \{0\}$ in the domain of $\sigma_N^{-1}$, get a point $\sigma_N^{-1}(u) \in S^n$, then project via $\sigma_S$. The result should be a function of $u$ alone; simplify using $|u|^2 + 1 = (u, 1)$'s relation to the sphere.

> [!note]- Hint 4
> The smoothness of $u \mapsto u/|u|^2$ on $\mathbb{R}^n \setminus \{0\}$ is immediate: each component is a rational function with denominator $|u|^2$, nonzero on the domain.

---

# Solution

The proof breaks into four steps. Step 1 derives $\sigma_N$ explicitly and computes its inverse. Step 2 derives $\sigma_S$ similarly. Step 3 computes the transition function $\sigma_S \circ \sigma_N^{-1}$ and shows it is the inversion $u \mapsto u/|u|^2$ on $\mathbb{R}^n \setminus \{0\}$. Step 4 verifies smoothness and concludes via [[Thm - Smooth Structure from Maximal Atlas]]. The non-obvious move is in Step 3, where the algebraic simplification reveals that the transition is geometric inversion — a fact that would not be apparent from the projection formulae alone.

**Step 1: Define $\sigma_N$ and compute its inverse $\sigma_N^{-1}$.**

The stereographic projection from the north pole is
$$\sigma_N : S^n \setminus \{N\} \to \mathbb{R}^n, \quad \sigma_N(x^1, \dots, x^{n+1}) = \frac{1}{1 - x^{n+1}}(x^1, \dots, x^n).$$
Its inverse is
$$\sigma_N^{-1}(u) = \frac{1}{|u|^2 + 1}\left(2u^1, \dots, 2u^n, |u|^2 - 1\right) \in S^n \setminus \{N\}.$$

> [!note]- Derivation
> *Geometric definition:* The line from $N = (0, \dots, 0, 1)$ through $x \in S^n \setminus \{N\}$ has parametrization $t \mapsto tN + (1-t) x$, and it crosses the equator plane $\{x^{n+1} = 0\}$ at $t = x^{n+1}/(x^{n+1} - 1)$. At that $t$, the first $n$ coordinates of the parametrization are $(1-t) x^i = \frac{-1}{x^{n+1} - 1} x^i = \frac{x^i}{1 - x^{n+1}}$ for $i = 1, \dots, n$. So $\sigma_N(x) = (1 - x^{n+1})^{-1} (x^1, \dots, x^n)$. This is well-defined on $S^n \setminus \{N\}$ since $x^{n+1} \neq 1$ there.
>
> *Continuity:* Each component is continuous (denominator nonzero).
>
> *Inverse:* Given $u \in \mathbb{R}^n$, we seek $x = (x^1, \dots, x^{n+1}) \in S^n \setminus \{N\}$ with $\sigma_N(x) = u$. So $x^i = (1 - x^{n+1}) u^i$ for $i = 1, \dots, n$, and the sphere condition $\sum_{i=1}^{n+1} (x^i)^2 = 1$ gives
> $$(1 - x^{n+1})^2 |u|^2 + (x^{n+1})^2 = 1.$$
> Expand: $|u|^2 - 2 |u|^2 x^{n+1} + (|u|^2 + 1)(x^{n+1})^2 = 1$, equivalently $(|u|^2 + 1)(x^{n+1})^2 - 2|u|^2 x^{n+1} + (|u|^2 - 1) = 0$. Solving via the quadratic formula (and noting that the root $x^{n+1} = 1$ corresponds to $N$, which we exclude),
> $$x^{n+1} = \frac{|u|^2 - 1}{|u|^2 + 1}, \quad x^i = (1 - x^{n+1}) u^i = \frac{2 u^i}{|u|^2 + 1} \text{ for } i = 1, \dots, n.$$
> *Verification:* $(x^{n+1})^2 + \sum_{i=1}^n (x^i)^2 = \frac{(|u|^2 - 1)^2 + 4|u|^2}{(|u|^2 + 1)^2} = \frac{(|u|^2 + 1)^2}{(|u|^2 + 1)^2} = 1$. ✓
>
> *Continuity of $\sigma_N^{-1}$:* Each component is a continuous function of $u$ (rational, no division by zero). So $\sigma_N$ is a homeomorphism onto $\mathbb{R}^n$.

**Step 2: Define $\sigma_S$ analogously.**

The stereographic projection from the south pole is
$$\sigma_S : S^n \setminus \{S\} \to \mathbb{R}^n, \quad \sigma_S(x^1, \dots, x^{n+1}) = \frac{1}{1 + x^{n+1}}(x^1, \dots, x^n),$$
with inverse
$$\sigma_S^{-1}(v) = \frac{1}{|v|^2 + 1}\left(2v^1, \dots, 2v^n, -(|v|^2 - 1)\right) = \frac{1}{|v|^2 + 1}\left(2v^1, \dots, 2v^n, 1 - |v|^2\right).$$

> [!note]- Derivation
> Replace $N$ by $S = (0, \dots, 0, -1)$ in the Step 1 derivation. The line from $S$ through $x$ is $t \mapsto tS + (1-t) x$, crossing the equator plane at $t = -x^{n+1}/(x^{n+1} + 1)$, giving $(1-t) x^i = \frac{x^i}{1 + x^{n+1}}$. Inversion is analogous; the only sign change is in the last coordinate of the inverse (the $-(|v|^2-1) = 1 - |v|^2$).

**Step 3: Compute the transition function $\sigma_S \circ \sigma_N^{-1}$ on $\mathbb{R}^n \setminus \{0\}$.**

For $u \in \mathbb{R}^n \setminus \{0\}$,
$$\sigma_S \circ \sigma_N^{-1}(u) = \frac{u}{|u|^2}.$$

> [!note]- Derivation
> Start with $u \in \mathbb{R}^n \setminus \{0\}$ (the value $u = 0$ is excluded because $\sigma_N^{-1}(0) = S$, which is not in the domain of $\sigma_S$). Compute $\sigma_N^{-1}(u)$ from Step 1:
> $$\sigma_N^{-1}(u) = \left(\frac{2u^1}{|u|^2 + 1}, \dots, \frac{2u^n}{|u|^2 + 1}, \frac{|u|^2 - 1}{|u|^2 + 1}\right) \in S^n.$$
> Apply $\sigma_S$:
> $$\sigma_S\left(\sigma_N^{-1}(u)\right) = \frac{1}{1 + \frac{|u|^2 - 1}{|u|^2 + 1}}\left(\frac{2u^1}{|u|^2 + 1}, \dots, \frac{2u^n}{|u|^2 + 1}\right).$$
> Simplify the leading factor: $1 + \frac{|u|^2 - 1}{|u|^2 + 1} = \frac{(|u|^2 + 1) + (|u|^2 - 1)}{|u|^2 + 1} = \frac{2|u|^2}{|u|^2 + 1}$. Thus
> $$\sigma_S(\sigma_N^{-1}(u)) = \frac{|u|^2 + 1}{2|u|^2}\cdot\frac{2u}{|u|^2 + 1} = \frac{u}{|u|^2}.$$

This is the **inversion in the unit sphere** of $\mathbb{R}^n$ — the geometric inversion map well known from classical Euclidean geometry. It is defined and a diffeomorphism on $\mathbb{R}^n \setminus \{0\}$.

**Step 4: Verify smoothness, conclude smooth manifold structure.**

The map $u \mapsto u/|u|^2$ on $\mathbb{R}^n \setminus \{0\}$ has $i$-th component $u^i / \sum_j (u^j)^2$, a rational function in the coordinates $u^j$ with nonvanishing denominator on the domain. Hence it is smooth. By symmetry (computing $\sigma_N \circ \sigma_S^{-1}$ produces the same inversion), the inverse transition function is also smooth. So the two charts are smoothly compatible.

> [!note]- Derivation
> Smoothness of $u/|u|^2$: each component $\frac{u^i}{|u|^2}$ is a quotient of polynomials with denominator $|u|^2 > 0$ on $\mathbb{R}^n \setminus \{0\}$, hence smooth (the quotient rule, iterated, gives all partial derivatives as polynomials in the $u^j$ divided by powers of $|u|^2$). Computing $\sigma_N \circ \sigma_S^{-1}$ by the same method yields $v \mapsto v/|v|^2$, the same inversion. Both maps are smooth.
>
> The two charts $\{(S^n \setminus \{N\}, \sigma_N), (S^n \setminus \{S\}, \sigma_S)\}$ have domains covering $S^n$ (every point is in at least one of $S^n \setminus \{N\}$ or $S^n \setminus \{S\}$). Their pairwise transition functions are smooth. So they form a smooth atlas. By [[Thm - Smooth Structure from Maximal Atlas]], this atlas determines a unique smooth structure on $S^n$ — the **standard smooth structure**.
>
> $S^n$ is Hausdorff and second-countable (subspace of $\mathbb{R}^{n+1}$, which is). Combined with the locally Euclidean property (witnessed by the stereographic charts), $S^n$ is a smooth $n$-manifold.

> [!note]- Complete formal solution
> **Claim.** $S^n = \{x \in \mathbb{R}^{n+1} : |x| = 1\}$ is a smooth $n$-manifold under the smooth structure determined by the stereographic atlas $\{(S^n \setminus \{N\}, \sigma_N), (S^n \setminus \{S\}, \sigma_S)\}$ described below.
>
> *Proof.* $S^n$ inherits the Hausdorff and second-countable properties from $\mathbb{R}^{n+1}$ via the subspace topology, so it suffices to exhibit a smooth atlas of dimension $n$.
>
> **Stereographic projection from $N$.** Define $\sigma_N : S^n \setminus \{N\} \to \mathbb{R}^n$ by
> $$\sigma_N(x^1, \dots, x^{n+1}) = \frac{1}{1 - x^{n+1}}\left(x^1, \dots, x^n\right).$$
> This is continuous (denominator nonzero on the domain) and surjective onto $\mathbb{R}^n$. Its inverse is
> $$\sigma_N^{-1}(u) = \frac{1}{|u|^2 + 1}\left(2u^1, \dots, 2u^n, |u|^2 - 1\right),$$
> verified by direct substitution into the sphere equation $\sum_{i=1}^{n+1} (x^i)^2 = 1$ — the computation $(|u|^2 - 1)^2 + 4|u|^2 = (|u|^2 + 1)^2$ confirms the image lies on $S^n$, and the last coordinate is $\frac{|u|^2 - 1}{|u|^2 + 1} < 1$, so the image avoids $N$.
>
> **Stereographic projection from $S$.** Analogously, $\sigma_S : S^n \setminus \{S\} \to \mathbb{R}^n$, $\sigma_S(x^1, \dots, x^{n+1}) = \frac{1}{1 + x^{n+1}}(x^1, \dots, x^n)$, with inverse $\sigma_S^{-1}(v) = \frac{1}{|v|^2 + 1}(2v^1, \dots, 2v^n, 1 - |v|^2)$.
>
> **Both maps are homeomorphisms.** Each $\sigma_N, \sigma_S$ is continuous with continuous inverse, hence a homeomorphism between an open subset of $S^n$ and $\mathbb{R}^n$. They cover $S^n$: every $x \in S^n$ has $x^{n+1} \neq \pm 1$ unless $x = N$ or $x = S$, and these two cases are handled by $\sigma_S$ and $\sigma_N$ respectively.
>
> **Smooth compatibility.** The domains overlap on $S^n \setminus \{N, S\}$, mapped to $\mathbb{R}^n \setminus \{0\}$ under each chart (the omitted points $S, N$ map to $0$ under $\sigma_N, \sigma_S$ respectively, and these are the only points missing from the image). The transition function $\sigma_S \circ \sigma_N^{-1}$ on $\mathbb{R}^n \setminus \{0\}$ is computed:
> $$\sigma_S(\sigma_N^{-1}(u)) = \frac{1}{1 + \frac{|u|^2 - 1}{|u|^2 + 1}}\left(\frac{2u^1}{|u|^2 + 1}, \dots, \frac{2u^n}{|u|^2 + 1}\right) = \frac{u}{|u|^2}.$$
> By the symmetry of the construction, $\sigma_N \circ \sigma_S^{-1}(v) = v/|v|^2$ on $\mathbb{R}^n \setminus \{0\}$. Both maps are quotients of polynomials with nonvanishing denominator $|u|^2$ on the domain, hence smooth. Thus the two charts are smoothly compatible, and the atlas $\{(S^n \setminus \{N\}, \sigma_N), (S^n \setminus \{S\}, \sigma_S)\}$ is a smooth atlas.
>
> By [[Thm - Smooth Structure from Maximal Atlas]], this smooth atlas determines a unique maximal smooth atlas — the **standard smooth structure** on $S^n$. With this structure, $S^n$ is a smooth $n$-manifold. $\blacksquare$

> [!warning] Illegal but tempting alternative route: a global chart
> One might hope to cover $S^n$ with a *single* chart, but this is impossible. $S^n$ is compact (a closed bounded subset of $\mathbb{R}^{n+1}$), while every open subset of $\mathbb{R}^n$ is non-compact (Heine–Borel). A chart $\varphi : S^n \to \widehat{S^n} \subseteq \mathbb{R}^n$ would be a homeomorphism, hence would map a compact space to a non-compact space — impossible. So at least two charts are required, and stereographic projection gives the simplest two-chart atlas.

> [!warning] Sanity check via independent route — the graph atlas
> A different two-chart atlas would be unnatural, but the $2(n+1)$-chart graph atlas (Lee Example 1.4) provides an alternative construction. The two atlases are compatible — [[Ex - Compatibility of Two Atlases on the Sphere]] proves this — so they determine the same standard smooth structure.

---

# Key Takeaways

**The trigger pattern: "compact manifold needs at least two charts."** Whenever you encounter a *compact* topological manifold, you cannot cover it with a single chart, because no compact space is homeomorphic to any open subset of $\mathbb{R}^n$ (an open subset of $\mathbb{R}^n$ is non-compact unless empty). The minimum is two charts for the simplest compact manifolds — and stereographic projection is the cheapest way to get two charts on a sphere. This pattern recurs constantly: covering $S^n$ takes 2 charts (stereographic) or $2(n+1)$ (graph); covering $T^n$ takes $2^n$ (one per orthant of the fundamental domain) or more; covering $\mathbb{CP}^n$ takes $n+1$. The total number depends on the geometry but is always finite for compact manifolds.

**The geometric meaning of stereographic projection: lines from a pole to the equator plane.** Stereographic projection has a classical interpretation: project from the north pole $N$ through the point $x$ to where the line crosses the equator plane $\{x^{n+1} = 0\}$. This is the same map used in cartography (the Mercator projection is a 2D variant), in complex analysis (the Riemann sphere uses $\mathbb{CP}^1 = S^2$ and stereographic charts give the holomorphic structure), and in physics (the celestial sphere). Once you internalize the picture, every property — conformal, mapping circles to circles or lines, etc. — becomes geometrically obvious.

**The transition function is the inversion $u \mapsto u/|u|^2$ — a classical geometric transformation.** The transition between the two stereographic charts is the *inversion in the unit sphere*, a transformation classical Euclidean geometry has studied for two centuries (the Apollonius construction, Möbius transformations on $\mathbb{R}^n$). This is not a coincidence: stereographic projection conjugates the "rotations of $S^n$" with the "Möbius transformations of $\mathbb{R}^n \cup \{\infty\}$" (or "conformal transformations of $S^n$"), and the change of pole reflects this conjugation. In dimension $n = 2$, the result is the Möbius group $\mathrm{PSL}(2, \mathbb{C})$, the symmetry group of complex projective line and the Riemann sphere. The exercise is thus the gateway to a rich classical geometry.

**The standard smooth structure on $S^n$ is *not* obvious without the verification.** A priori, the atlas $\{(S^n \setminus \{N\}, \sigma_N), (S^n \setminus \{S\}, \sigma_S)\}$ could fail smooth compatibility, in which case it would describe a non-standard smooth structure. The fact that the transition is the inversion (a smooth diffeomorphism) is what justifies calling it the *standard* smooth structure. Milnor's exotic 7-spheres ($S^7$ with 28 distinct smooth structures, all topologically equivalent) shows that on higher-dimensional spheres, alternative smooth structures genuinely exist — but the standard one is always defined via stereographic projection or graph coordinates.

**This exercise is the prototype for "build a manifold from charts" arguments.** The four-step routine — (1) name charts, (2) verify homeomorphism, (3) compute transitions, (4) check smoothness — appears in essentially every exercise where one constructs a smooth manifold from scratch. See [[Ex - Real Projective Space is a Smooth Manifold]] and [[Ex - The Grassmannian is a Smooth Manifold]] for the next two instances. Once the routine is fluent, constructing smooth manifolds is mechanical.

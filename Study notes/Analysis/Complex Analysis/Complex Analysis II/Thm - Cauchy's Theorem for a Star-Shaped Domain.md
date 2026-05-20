---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Def - Domain in the Complex Plane"
  - "Thm - Goursat's Theorem (Cauchy for a Triangle)"
  - "Thm - Existence of a Primitive iff Closed Integrals Vanish"
tags: [analysis, complex-analysis]
---

# Notation

$D \subseteq \mathbb{C}$ open, **star-shaped** with respect to $a_0$ (every line segment from $a_0$ to any $w \in D$ lies in $D$). $f : D \to \mathbb{C}$ holomorphic. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Statement

> **Theorem (Cauchy's theorem for a star-shaped domain).** Let $D \subseteq \mathbb{C}$ be a star-shaped open set (there exists $a_0 \in D$ such that for every $w \in D$, the line segment $[a_0, w]$ lies in $D$) and $f : D \to \mathbb{C}$ holomorphic. Then $f$ has a primitive on $D$ — explicitly, $F(w) = \int_{[a_0, w]} f(z)\,dz$ — and for every closed piecewise $C^1$ curve $\gamma$ in $D$:
> $$\int_\gamma f(z)\,dz = 0.$$

---

# Motivation

The leap from Goursat (vanishing of integrals around *triangles*) to vanishing of integrals around *all closed curves* requires a topological hypothesis on the domain. The simplest such hypothesis is *star-shaped*: there is a "center" $a_0$ such that every point of $D$ can be reached from $a_0$ by a line segment. This allows a clean construction of primitives, via integration along line segments from $a_0$.

Star-shaped is stronger than simply connected (the disc, convex, star-shaped all contain each other in order) but it covers most "nice" domains arising in computation — discs, half-planes, slit planes, convex sets — and the proof is clean and elementary, using only Goursat. The full simply-connected version (every closed curve in $D$ is contractible) requires more topology and is treated in [[Complex Analysis III — Winding, Laurent, Residues|CA III]].

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$D$ star-shaped, $f$ holomorphic".

The first disguised source is **$D$ is a disc, half-plane, convex set, or slit plane**: all star-shaped. The disc is star-shaped with respect to any point; convex sets are star-shaped with respect to every point.

The second disguised source is **$f$ continuous on $D$, holomorphic on $D \setminus S$ for finite $S$**: the theorem extends to this case (as in Cambridge IB 2.2.3), via the extended Goursat.

**Targets (Output Amplification)**

The conclusion is "$f$ has a primitive on $D$, and $\int_\gamma f\,dz = 0$ for every closed piecewise $C^1$ curve $\gamma$ in $D$".

Combine with **explicit contour integral computations.** Property $D$: a specific contour in $D$. The amplified result: $\int_\gamma f\,dz = 0$, regardless of the shape of $\gamma$.

Combine with **the residue theorem.** Property $D$: a domain with one isolated singularity removed. The amplified result: the integral around an encircling curve equals $2\pi i$ times the residue (in [[Complex Analysis III — Winding, Laurent, Residues|CA III]]). The star-shaped Cauchy is the building block.

---

# Why Is It True

Construct a primitive by integrating along line segments from the star-point $a_0$. For each $w \in D$, define
$$F(w) := \int_{[a_0, w]} f\,dz$$
where $[a_0, w]$ is the line segment from $a_0$ to $w$ (lies in $D$ by star-shapedness).

We must check that $F$ is holomorphic with $F'(w) = f(w)$. For $w \in D$ and small $h$, both $w$ and $w + h$ are in $D$, and so is the triangle $T$ with vertices $a_0, w, w + h$ (by star-shapedness: each vertex lies in $D$ via a segment from $a_0$, and the triangle, being a 2D figure, is contained in $D$... actually this needs care — star-shapedness ensures the segments lie in $D$, but the interior of the triangle needs to be checked. The standard treatment is: $D$ star-shaped means each *segment* from $a_0$ is in $D$, so the triangle $[a_0, w, w + h]$ is in $D$ provided the segment from $a_0$ to $w + h$ is in $D$, which holds. The interior of the triangle is filled by segments from $a_0$ to points on $[w, w + h]$, all of which are in $D$.)

By [[Thm - Goursat's Theorem (Cauchy for a Triangle)|Goursat]] on this triangle: $\int_{\partial T} f\,dz = 0$. So
$$\int_{[a_0, w + h]} f\,dz - \int_{[a_0, w]} f\,dz - \int_{[w, w + h]} f\,dz = 0,$$
hence $F(w + h) - F(w) = \int_{[w, w + h]} f\,dz$. Parametrize this segment by $\delta(t) = w + th$, $t \in [0, 1]$: $\int_{[w, w + h]} f\,dz = \int_0^1 f(w + th)\,h\,dt$. So
$$\frac{F(w + h) - F(w)}{h} - f(w) = \int_0^1 [f(w + th) - f(w)]\,dt \to 0$$
as $h \to 0$ by continuity of $f$ at $w$. Hence $F'(w) = f(w)$.

Once $F$ is constructed, [[Thm - Fundamental Theorem of Contour Integration]] gives $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a)) = 0$ for any closed $\gamma$.

---

# What Makes This Hard

The technical care is in verifying that the triangle $[a_0, w, w + h]$ lies in $D$ — uses star-shapedness, but the *interior* of the triangle is parametrized as segments from $a_0$. Once this is granted, Goursat does the work. The most common error is to apply this theorem on non-star-shaped domains (e.g., $\mathbb{C}^\times$) where it is *false* in general.

---

# Rederivation Scaffold

**High-level strategy:**
Define $F(w) = \int_{[a_0, w]} f\,dz$. Use Goursat on triangles $[a_0, w, w + h]$ to show $F$ is differentiable with $F' = f$. Apply [[Thm - Fundamental Theorem of Contour Integration]] to conclude.

**Subgoal decomposition:**

1. **Define $F$ via line integration from $a_0$.**
2. **Apply Goursat to the triangle $[a_0, w, w + h]$.** Concludes $F(w + h) - F(w) = \int_{[w, w + h]} f\,dz$.
3. **Differentiability of $F$.** Difference quotient tends to $f(w)$ by continuity.
4. **Apply FT contour integration.** $\int_\gamma f\,dz = 0$ for closed $\gamma$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Triangle from $a_0$ lies in $D$
> **Statement:** If $D$ is star-shaped about $a_0$ and $w, w + h \in D$ with the segment $[w, w + h] \subseteq D$, then the closed triangle with vertices $a_0, w, w + h$ lies in $D$.
>
> **Hint:** Points of the triangle are convex combinations $\alpha a_0 + \beta w + \gamma(w + h)$ with $\alpha + \beta + \gamma = 1$, expressed as segments from $a_0$ to points on $[w, w + h]$.
>
> > [!note]- Full proof
> > Any point $p$ of the triangle can be written as $p = (1 - t) a_0 + t q$ with $t \in [0, 1]$ and $q \in [w, w + h]$. Since $D$ is star-shaped about $a_0$ and $q \in D$, the segment from $a_0$ to $q$ lies in $D$. So $p \in D$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $a_0 \in D$ with respect to which $D$ is star-shaped. Define $F(w) := \int_{[a_0, w]} f\,dz$ for $w \in D$; the line segment lies in $D$ by star-shapedness.
>
> For $w \in D$, choose $r > 0$ with $D(w, r) \subseteq D$. For $|h| < r$ small enough that the segment $[w, w + h] \subseteq D$ (always for small $h$ since $D$ open), Lemma 1 gives that the closed triangle $T$ with vertices $a_0, w, w + h$ lies in $D$. By [[Thm - Goursat's Theorem (Cauchy for a Triangle)|Goursat's theorem]]:
> $$0 = \int_{\partial T} f\,dz = \int_{[a_0, w]} f\,dz + \int_{[w, w + h]} f\,dz + \int_{[w + h, a_0]} f\,dz$$
> $$= F(w) + \int_{[w, w + h]} f\,dz - F(w + h).$$
> So $F(w + h) - F(w) = \int_{[w, w + h]} f\,dz = \int_0^1 f(w + th) \cdot h\,dt$.
>
> Hence
> $$\frac{F(w + h) - F(w)}{h} - f(w) = \int_0^1 [f(w + th) - f(w)]\,dt.$$
> The right side is bounded by $\sup_{|z - w| \leq |h|} |f(z) - f(w)|$, which $\to 0$ as $h \to 0$ by continuity. So $F'(w) = f(w)$.
>
> $F$ is holomorphic on $D$ with $F'(w) = f(w)$, i.e., $F$ is a primitive. By [[Thm - Fundamental Theorem of Contour Integration]], $\int_\gamma f\,dz = 0$ for every closed piecewise $C^1$ curve in $D$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Cauchy on the disc.** A disc is star-shaped, so this theorem specializes to **Cauchy's theorem for a disc** ([[Thm - Cauchy's Theorem for a Disc]]) — the workhorse for local computations.

**Slit plane and logarithm.** The slit plane $\mathbb{C} \setminus (-\infty, 0]$ is star-shaped with respect to any point on the positive real axis. So the principal branch of $\log$ exists there, as the primitive of $1/z$. This connects to [[Thm - Existence of a Logarithm on Simply Connected Domains]].

**Half-plane domains.** The upper half-plane $\{\operatorname{Im} z > 0\}$ is convex (hence star-shaped), so Cauchy applies. Useful for evaluating real integrals via contours in the upper half-plane.

---

# Bridges

- **[[Thm - Goursat's Theorem (Cauchy for a Triangle)]]** — the building block.

- **[[Thm - Cauchy's Theorem for a Disc]]** — direct specialization.

- **[[Thm - Existence of a Primitive iff Closed Integrals Vanish]]** — the conceptual framework; this theorem constructs the primitive directly.

- **[[Thm - Cauchy Integral Formula]]** — built on top of star-shaped Cauchy.

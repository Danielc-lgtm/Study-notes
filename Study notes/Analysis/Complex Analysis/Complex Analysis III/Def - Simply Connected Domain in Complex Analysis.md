---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Winding Number"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis, topology]
---

# Notation

Throughout, $U$ is an open subset of $\mathbb{C}$ (often a domain — open and path-connected). The symbol $\gamma : [a, b] \to U$ denotes a closed piecewise $C^1$ curve in $U$, and $I(\gamma; w)$ is the winding number of $\gamma$ around a point $w \in \mathbb{C} \setminus U$. We sometimes call a curve homologous to zero in $U$ if its winding number around every point of the complement is zero. The full registry lives on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Axiom Motivation

We want a class of domains on which Cauchy's theorem holds in its strongest form: every closed integral of a holomorphic function vanishes, every holomorphic function has a primitive, and every nowhere-vanishing holomorphic function has a logarithm. What is the right condition on the domain?

In the disc, Cauchy's theorem holds because any closed curve bounds a region inside the disc, and one can fill in the inside to apply Goursat-style triangulation. In an annulus, this fails: a closed curve going once around the central hole does not bound a region inside the annulus — its "inside" includes the hole. The annulus shows that *closed curves can have a topologically essential winding around a "missing" piece*, and on such a domain Cauchy's theorem fails (for instance, $\int_{|z|=1} dz/z = 2\pi i \neq 0$ on the punctured plane).

So the right condition is: no closed curve has essential winding around anything missing from $U$. Formally, for every closed curve $\gamma$ in $U$ and every point $w \notin U$, the winding number $I(\gamma; w) = 0$. This is the *homological* simple connectedness: every closed curve bounds a region inside $U$, in the sense that its winding number around the complement is zero. This is exactly what Cauchy's theorem needs — the curve's integral picks up no contribution from any missing piece because the curve does not wind around any missing piece.

The topologically-inclined reader will recognize the topological definition of simply connected: every closed loop is null-homotopic (can be continuously contracted to a point) within $U$. For open subsets of $\mathbb{C}$, the two definitions coincide — null-homotopy implies zero winding number (by homotopy invariance of the winding number), and zero winding number for open planar sets implies null-homotopy (a slightly deeper result). The complex-analytic version (winding number zero around the complement) is what Cauchy's theorem actually uses, so we adopt it as the definition.

What would break with a stronger definition? Asking every closed curve to be null-homotopic in $U$ would be the topologist's definition; it agrees with ours for open subsets of $\mathbb{C}$ but disagrees in general topological spaces (the Polish circle is a classical example where the two come apart). Since we work in $\mathbb{C}$, both definitions give the same class. What would break with a weaker definition? Asking only that $U$ be connected, or path-connected, would include the annulus, on which Cauchy's theorem fails. The simple-connectedness condition is the minimum strengthening of connectedness that makes the global theorems of complex analysis go through.

---

# The Definition

Let $U \subseteq \mathbb{C}$ be open.

**Complex-analytic definition.** $U$ is **simply connected** if for every closed piecewise $C^1$ curve $\gamma$ in $U$ and every point $w \in \mathbb{C} \setminus U$,
$$I(\gamma; w) = 0.$$
Equivalently: every closed curve in $U$ is *homologous to zero* in $U$.

**Topological definition (equivalent for open $U \subseteq \mathbb{C}$).** $U$ is path-connected and every closed continuous curve $\gamma : [0, 1] \to U$ is null-homotopic in $U$ — there is a continuous $H : [0, 1] \times [0, 1] \to U$ with $H(s, 0) = \gamma(s)$ and $H(s, 1) = $ constant. Equivalently, $\pi_1(U) = 0$.

**Equivalent characterizations on open subsets of $\mathbb{C}$.** For an open $U \subseteq \mathbb{C}$, the following are equivalent:
1. $U$ is simply connected.
2. The complement $\hat{\mathbb{C}} \setminus U$ is connected (as a subset of the Riemann sphere).
3. Every nowhere-vanishing holomorphic function on $U$ has a holomorphic logarithm.
4. Every nowhere-vanishing holomorphic function on $U$ has a holomorphic square root.
5. The Cauchy integral $\int_\gamma f\,dz$ vanishes for every closed curve $\gamma$ in $U$ and every holomorphic $f$ on $U$.

---

# Relate to Other Fields / Compression

In **algebraic topology**, simply connected means $\pi_1(U) = 0$ — the fundamental group is trivial. This is the first cohomology vanishing condition in the chain of higher connectivity ($n$-connected = $\pi_k(U) = 0$ for $k \leq n$). For open subsets of $\mathbb{C}$, simply-connected is equivalent to many other "no holes" conditions; in higher dimensions these conditions split apart (a domain in $\mathbb{R}^3$ can be simply connected but have nontrivial $H_2$ — a hollow ball-shell has $\pi_1 = 0$ but encloses a cavity).

In **algebraic geometry / Riemann surfaces**, simply connected Riemann surfaces are classified by the **uniformization theorem**: every simply connected Riemann surface is biholomorphic to the Riemann sphere $\hat{\mathbb{C}}$, the complex plane $\mathbb{C}$, or the open unit disc $\mathbb{D}$. The simply-connected condition is what makes covers and uniformization tractable; multiply-connected surfaces are quotients of these three by group actions.

In **physics — gauge theory**, simply-connectedness controls whether one can globally define gauge potentials and phases. On a non-simply-connected domain, gauge potentials can have nontrivial holonomy (the Aharonov–Bohm effect: a magnetic flux confined to a region inaccessible to electrons still affects their phase, via the winding number of their trajectory around the flux). The simply-connected condition makes the Aharonov–Bohm phase trivial.

---

# Examples / Corollaries

**Is an instance — the open disc $\mathbb{D}$.** Any disc is simply connected: it is convex, so any closed curve can be contracted to a point by linear homotopy $H(s, t) = (1 - t)\gamma(s) + t z_0$. The winding number around any external point is zero because the disc lies in a half-plane through any external point and any closed curve in a half-plane has winding number zero around points outside the half-plane.

**Is an instance — the slit plane $\mathbb{C} \setminus (-\infty, 0]$.** Remove a ray from $\mathbb{C}$. The remaining domain is simply connected because any closed curve in it cannot wind around any point of the removed ray (the ray "blocks" the winding). This is the canonical domain on which the principal branch of $\log$ is defined.

**Is an instance — the upper half-plane $\mathbb{H} = \{z : \operatorname{Im} z > 0\}$.** Convex, hence simply connected. Biholomorphic to $\mathbb{D}$ via $z \mapsto (z - i)/(z + i)$.

**Is NOT an instance — the punctured plane $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$.** The unit circle $\gamma(t) = e^{2\pi i t}$ has $I(\gamma; 0) = 1 \neq 0$, so $\mathbb{C}^\times$ is not simply connected. Equivalently, the unit circle is not null-homotopic in $\mathbb{C}^\times$, and $\pi_1(\mathbb{C}^\times) = \mathbb{Z}$. There is no global branch of $\log$ on $\mathbb{C}^\times$.

**Is NOT an instance — an annulus $A = \{z : 1 < |z| < 2\}$.** The circle $\gamma(t) = (3/2)e^{2\pi i t}$ has $I(\gamma; 0) = 1$ and $0 \notin A$, so $A$ is not simply connected. Its fundamental group is $\mathbb{Z}$, generated by a loop around the inner boundary.

**Is NOT an instance — $\mathbb{C} \setminus \{0, 1\}$.** Removing two points gives a doubly-punctured plane with $\pi_1 = $ free group on two generators (much wilder than $\mathbb{Z}$). Closed curves can wind around either puncture independently.

**Corollary — log existence on simply connected domains avoiding zero.** If $U$ is simply connected and $0 \notin U$, then $1/z$ has a primitive on $U$ (since $\int_\gamma dz/z = 2\pi i \cdot I(\gamma; 0) = 0$ for every closed $\gamma$ in $U$), and that primitive is a branch of $\log z$. This is one of the most-used facts about simply-connected domains.

**Corollary — every closed curve bounds.** If $U$ is simply connected and $\gamma$ is a closed curve in $U$, then $\gamma$ bounds a region inside $U$ in the homological sense — the integer-valued function $w \mapsto I(\gamma; w)$ extends to all of $\mathbb{C}$, vanishes outside $U$, and equals the "filled in" interior of $\gamma$.

**Calibration check.** Verify that the punctured plane $\mathbb{C}^\times$ is *not* simply connected by exhibiting the unit circle as a closed curve with winding number $1$ around the missing point $0$ — and that this is exactly why there is no global branch of $\log$ on $\mathbb{C}^\times$. Verify that the slit plane $\mathbb{C} \setminus (-\infty, 0]$ *is* simply connected, since the removed ray "blocks" any closed curve from winding around its points. And verify that $\mathbb{C} \setminus \{0, 1\}$ has fundamental group the *free* group on two generators (not $\mathbb{Z} \times \mathbb{Z}$), because the two punctures are independent obstructions and the free product structure tracks the order in which they are encircled.

> [!tip] Cauchy's Theorem in Full Generality *(from §3.2)*
> The full form of [[Thm - Cauchy's Theorem for Simply Connected Domains|Cauchy's theorem]]: on a simply connected open $U$, every holomorphic function has a primitive and every closed integral vanishes. This is what we needed to motivate the definition.

> [!tip] Riemann Mapping Theorem *(from §3.5+)*
> The [[Thm - Riemann Mapping Theorem (Statement)|Riemann mapping theorem]]: every simply connected proper open subset of $\mathbb{C}$ is biholomorphic to the unit disc $\mathbb{D}$. Simple-connectedness is the *complete* invariant of planar domains up to biholomorphism (modulo the exceptional case of $\mathbb{C}$ itself).

> [!tip] Existence of Harmonic Conjugates *(from Harmonic theory)*
> Every harmonic function on a simply connected domain is the real part of a holomorphic function. This is the [[Thm - Harmonic ↔ Real Part of Holomorphic (on Simply Connected)|harmonic conjugate theorem]] — it fails on $\mathbb{C}^\times$, where $\log|z|$ is harmonic but $\arg z$ (its would-be conjugate) is multi-valued.

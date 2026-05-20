---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Curve and C1 Curve"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis, topology]
---

# Notation

Throughout, $\gamma : [a, b] \to \mathbb{C}$ is a closed continuous curve, meaning $\gamma(a) = \gamma(b)$, and $w \in \mathbb{C}$ is a point not lying on the image $\gamma^* := \gamma([a, b])$. We write $I(\gamma; w)$ for the winding number of $\gamma$ about $w$, sometimes also denoted $n(\gamma, w)$ in older sources. A curve is piecewise $C^1$ if there is a finite partition of $[a, b]$ on each piece of which $\gamma$ is continuously differentiable. The full notation registry lives on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Axiom Motivation

We want a single integer to record "how many times does the curve $\gamma$ wind around $w$?" — clockwise winds count negatively, counterclockwise positively, and a curve that never goes around at all gets $0$. Why must this be an integer, and why is it a sensible quantity to define at all?

Start with the picture. The curve $\gamma$ moves around the punctured plane $\mathbb{C} \setminus \{w\}$ and returns to where it started. At each time $t$, the vector $\gamma(t) - w$ points in some direction, and we can ask for its angle $\theta(t)$ measured from a fixed reference axis. The angle changes continuously as the curve moves — but only modulo $2\pi$, because angle is only defined up to that ambiguity. The integer we want is the net change in $\theta$ divided by $2\pi$: if the curve goes around once counterclockwise, $\theta$ increases by $2\pi$; once clockwise, $\theta$ decreases by $2\pi$; not at all, no net change. The definition is forced on us: the only integer that captures "net rotation" with the right signs is this one.

The technical content is that $\theta$ must be chosen *continuously*. There are infinitely many functions $\theta(t)$ satisfying $e^{i\theta(t)} = (\gamma(t) - w)/|\gamma(t) - w|$ — they differ from each other by integer multiples of $2\pi$, pointwise. But once we choose a continuous lift, the difference $\theta(b) - \theta(a)$ is well-defined independently of which lift we chose (different lifts differ by a constant $2\pi k$, which cancels in the difference). So the winding number is well-defined once we know a continuous lift exists, and the existence is a small topological fact: the path $\gamma$ can be partitioned into pieces, each lying in a half-plane on which the principal branch of $\arg$ is continuous, and the lifts on the pieces can be glued by adjusting integer multiples of $2\pi$.

The *integral formula* $\frac{1}{2\pi i}\int_\gamma \frac{dz}{z - w}$ is the same quantity computed differently. The point is that $\log(z - w)$ has $\arg(z - w)$ as its imaginary part, and integrating $1/(z - w)$ along $\gamma$ recovers the change in $\log(z - w)$, hence the change in $\arg(z - w)$. This formula has the great advantage of being *computable* — you parametrize $\gamma$ and evaluate an ordinary integral. The price is that the topological content (integer-valued, homotopy-invariant) is no longer manifest from the formula and must be re-proved.

What would break with a different definition? If we asked only for "the total change in angle (un-normalized)", we would get a multiple of $2\pi$, but the division by $2\pi$ is what makes the answer an integer with a clean interpretation. If we asked for "the number of times $\gamma$ crosses a particular ray from $w$", we would get a count that depends on the choice of ray and is not invariant under deformation. Continuous lift of the angle, divided by $2\pi$, is the unique definition that captures net topological rotation invariantly.

---

# The Definition

Let $\gamma : [a, b] \to \mathbb{C}$ be a closed continuous curve and $w \in \mathbb{C} \setminus \gamma^*$.

**Topological definition.** Write $\gamma(t) = w + r(t) e^{i\theta(t)}$ where $r(t) = |\gamma(t) - w| > 0$ and $\theta : [a, b] \to \mathbb{R}$ is a continuous function (a *continuous lift* of the argument). Such a $\theta$ exists by a partition argument (split $[a, b]$ into small intervals on each of which $\gamma$ stays inside a half-plane through $w$). The **winding number** of $\gamma$ about $w$ is
$$I(\gamma; w) = \frac{\theta(b) - \theta(a)}{2\pi}.$$
Since $\gamma$ is closed, $e^{i\theta(b)} = e^{i\theta(a)}$, so $\theta(b) - \theta(a) \in 2\pi\mathbb{Z}$, hence $I(\gamma; w) \in \mathbb{Z}$. The value is independent of the choice of lift $\theta$.

**Integral formula.** If $\gamma$ is piecewise $C^1$,
$$I(\gamma; w) = \frac{1}{2\pi i} \int_\gamma \frac{dz}{z - w}.$$
This agrees with the topological definition: parametrizing $\gamma(t) = w + r(t) e^{i\theta(t)}$ gives $dz/(z - w) = d\log(\gamma - w) = d\log r + i\,d\theta$; the $d\log r$ part is exact and integrates to zero over a closed loop, and the $i\,d\theta$ part integrates to $i(\theta(b) - \theta(a))$.

---

# Relate to Other Fields / Compression

The winding number is the fundamental example of a **degree** in algebraic topology. The map $\gamma : S^1 \to \mathbb{C} \setminus \{w\} \simeq S^1$ (after retracting the punctured plane onto a circle around $w$) is a continuous map between circles, and its **degree** is exactly $I(\gamma; w)$. The fundamental group $\pi_1(\mathbb{C} \setminus \{w\})$ is isomorphic to $\mathbb{Z}$, and the winding number realizes this isomorphism: $[\gamma] \mapsto I(\gamma; w)$. See [[Topology IV — §13–17 Quotients, Homotopy, Topological Groups, Baire|Topology IV]] for the homotopy-theoretic framework.

In **algebraic topology**, the winding number is the prototype of a **homology class pairing with a cohomology class**. The closed curve $\gamma$ represents a class in $H_1(\mathbb{C} \setminus \{w\}; \mathbb{Z}) \cong \mathbb{Z}$; the holomorphic 1-form $\frac{1}{2\pi i}\frac{dz}{z - w}$ represents a class in $H^1_{\mathrm{dR}}(\mathbb{C} \setminus \{w\}; \mathbb{C}) \cong \mathbb{C}$ (its integral around any small loop about $w$ gives $1$, so it generates the cohomology); the integral pairing is the winding number. The residue theorem of the next sections is the generalization to forms with multiple singularities.

In **fluid dynamics**, the winding number of a flow around an obstacle equals the *circulation* divided by $2\pi$ (more precisely, the circulation $\Gamma = \oint v \cdot d\ell$ around a closed curve enclosing a vortex of strength $\Gamma$ is $2\pi$ times the winding number times the vortex strength). In **electromagnetism**, the winding number of a closed loop around a current-carrying wire enters Ampère's law: the line integral of the magnetic field equals $\mu_0$ times the enclosed current, where "enclosed" is measured by winding number.

---

# Examples / Corollaries

**Is an instance — the circle traversed $k$ times.** Let $\gamma(t) = e^{2\pi i k t}$ for $t \in [0, 1]$, with $w = 0$. The integral formula gives
$$I(\gamma; 0) = \frac{1}{2\pi i}\int_0^1 \frac{2\pi i k\, e^{2\pi i k t}}{e^{2\pi i k t}}\,dt = \frac{1}{2\pi i}\cdot 2\pi i k = k.$$
For $k > 0$ this is counterclockwise winding; $k < 0$ is clockwise; $k = 0$ is a constant loop. This is the prototypical example: the unit circle gives the generator of $\pi_1(\mathbb{C}^\times) = \mathbb{Z}$.

**Is an instance — a circle not enclosing the point.** Let $\gamma(t) = 2 + e^{2\pi i t}$ for $t \in [0, 1]$, with $w = 0$. The curve traces a unit circle around $z = 2$ and never reaches the origin. By the integral formula one can compute $I(\gamma; 0) = 0$, but geometrically it is immediate: the curve stays in the half-plane $\operatorname{Re} z > 1$, so the argument $\arg(\gamma(t))$ never wraps around and the net change is zero.

**Is NOT an instance of "winding number is defined" — a curve passing through $w$.** If $\gamma$ passes through $w$, then $z - w$ vanishes somewhere along the curve and the angle becomes undefined there. The integral formula has an integrand with a singularity on the contour, and the integral diverges. This is why the definition requires $w \notin \gamma^*$.

**Calibration check — locally constant.** As $w$ varies in $\mathbb{C} \setminus \gamma^*$, the winding number $I(\gamma; w)$ is locally constant: for $w'$ close to $w$, the curve $\gamma$ winds the same number of times around $w'$ as around $w$. This is because the integral $\int_\gamma dz/(z - w)$ depends continuously on $w$ as long as $w$ stays off the curve, and being integer-valued plus continuous implies locally constant. Specifically, $I(\gamma; \cdot)$ is constant on each connected component of $\mathbb{C} \setminus \gamma^*$, and zero on the unbounded component (since for $|w|$ large the integrand decays and the integral tends to zero).

**Calibration check — concatenation.** If $\gamma = \gamma_1 \cdot \gamma_2$ is the concatenation of two closed curves at a common point, $I(\gamma; w) = I(\gamma_1; w) + I(\gamma_2; w)$. This follows immediately from additivity of integration. Reversal: $I(\gamma^{-1}; w) = -I(\gamma; w)$ where $\gamma^{-1}(t) = \gamma(b + a - t)$ is the curve traversed backwards.

**Corollary — figure-eight.** The figure-eight curve (two circles touching at a point, traversed as a single closed loop) has winding number $+1$ around a point in one loop, $-1$ in the other (if the two loops go opposite directions), and $0$ outside both. This is the simplest example where the bounded complement has multiple components with different winding numbers.

---

# Unlocked by This

> [!tip] Homotopy Invariance and the Argument Principle *(from §3.5)*
> Two homotopic closed curves in $\mathbb{C} \setminus \{w\}$ have the same winding number, because both the topological and integral definitions are preserved under continuous deformation in the punctured plane. This invariance is the topological skeleton on which Cauchy's theorem and the [[Thm - Argument Principle|argument principle]] rest.

> [!tip] Brouwer Fixed Point Theorem *(from Topology)*
> The winding-number argument extends to give the **Brouwer fixed point theorem** in dimension 2: every continuous map $\overline{\mathbb{D}} \to \overline{\mathbb{D}}$ has a fixed point. The proof: if not, the map $z \mapsto (z - f(z))/|z - f(z)|$ would give a retraction of the disc onto its boundary, contradicting a winding-number count on the boundary.

> [!tip] Topological Charge in Physics *(from Field Theory)*
> In condensed matter and field theory, defects in an order parameter (vortices in superfluids, dislocations in crystals, monopoles in gauge fields) are classified by integers that are higher-dimensional analogs of the winding number. The whole subject of **topological invariants of field configurations** rests on the same construction.

---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Cauchy's Theorem for a Star-Shaped Domain"
  - "Thm - Goursat's Theorem (Cauchy for a Triangle)"
  - "Def - Branch of the Logarithm"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $T$ be a closed triangle in $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$ that does *not* enclose the origin. Show that
$$\int_{\partial T}\frac{dz}{z} = 0.$$

**Recall:**

[[Thm - Goursat's Theorem (Cauchy for a Triangle)|Goursat]]: for $f$ holomorphic on an open set containing a triangle $T$, $\int_{\partial T} f\,dz = 0$. [[Thm - Cauchy's Theorem for a Star-Shaped Domain|Star-shaped Cauchy]]: if $f$ is holomorphic on a star-shaped domain $D$, then $f$ has a primitive on $D$ and integrals around closed curves in $D$ are zero. The function $f(z) = 1/z$ has a primitive on any simply connected open subset of $\mathbb{C}^\times$ (a [[Def - Branch of the Logarithm|branch]] of $\log z$).

---

# Convergent Strategy

**Problem class:** Verifying that Cauchy's theorem applies on a non-simply-connected domain ($\mathbb{C}^\times$) for a specific curve.

**Assumption pattern:** A triangle not enclosing the obstruction point $0$.

**Theorem routing:** Find a star-shaped neighbourhood of the triangle that excludes $0$. Apply Cauchy on that star-shaped subdomain.

**Key decision point:** Recognizing that the triangle is *bounded away from $0$*, and so lies in a neighbourhood that is itself star-shaped (e.g., the complement of a ray from $0$ through a fixed point in the triangle's exterior).

---

# Legal Operations Used

1. **Identify that the triangle does not enclose $0$.** So $0$ is on the "outside" of $T$.
2. **Find a star-shaped open set** $D \subseteq \mathbb{C}^\times$ containing $T$.
3. **Apply Cauchy on $D$.** Conclude integral is $0$.

Alternative: directly construct a branch of $\log z$ on a neighbourhood of $T$ and apply [[Thm - Fundamental Theorem of Contour Integration]].

---

# Hints

> [!note]- Hint 1
> Geometrically, $T$ is bounded away from $0$. So there is a ray from $0$ that does not intersect $T$. The slit plane $\mathbb{C}$ minus that ray is star-shaped and contains $T$.

> [!note]- Hint 2
> On the slit plane, a branch of $\log$ exists (primitive of $1/z$). Then FT applied around the closed triangle gives $0$.

---

# Solution

The proof breaks into two steps. Step 1 finds a star-shaped open neighbourhood of the triangle that excludes $0$, by picking a ray from $0$ in a direction not subtended by $T$ and removing it from the plane; Step 2 applies Cauchy's theorem (or Goursat) on this star-shaped slit plane, where $1/z$ has a primitive (a branch of $\log$). The non-obvious move is in Step 1 — the geometric argument that "does not enclose $0$" forces the angular set $\{\arg z : z \in T\}$ to be a proper closed subset of $S^1$, which is exactly what guarantees a clean ray.

**Step 1: Find a star-shaped neighbourhood.**

The triangle $T$ is a compact set in $\mathbb{C}^\times$ that does not enclose $0$. "Does not enclose" means $0$ is in the unbounded component of $\mathbb{C} \setminus T$ (or, equivalently, in the complement of the closed convex hull of $T$... actually we need care: "enclose" means $0$ is in the interior of $T$. Since $T$ is the closed triangle including its interior, "does not enclose $0$" means $0 \notin T$). Plus, since the interior of $T$ is bounded, "does not enclose $0$" means $0$ is in the exterior of the simple closed curve $\partial T$.

In any case: $0 \notin T$ and we can find a ray from $0$ (in the exterior of $T$) that does not intersect $T$. Let $L$ be such a ray. Then $D := \mathbb{C} \setminus L$ is a slit plane, star-shaped with respect to any point in the half-plane opposite to $L$, and $T \subseteq D$.

> [!note]- Why we can pick such a ray
> The triangle $T$ subtends an angle from $0$ — the set of angles $\{\arg z : z \in T\}$ is a closed subset of $S^1$ (the unit circle of directions). Since $T$ does not enclose $0$, this set of angles does *not* equal all of $S^1$ — there is some direction $\theta_0$ not in the set. The ray from $0$ in direction $\theta_0$ does not meet $T$ (since no point of $T$ has that argument).

**Step 2: Apply Cauchy on the slit plane.**

$D$ is star-shaped (with respect to a suitable point, e.g., the point at angle $\theta_0 + \pi$ on the unit circle). $1/z$ is holomorphic on $\mathbb{C}^\times \supseteq D$. By [[Thm - Cauchy's Theorem for a Star-Shaped Domain]], $1/z$ has a primitive on $D$ (a branch of $\log z$), and integrals of $1/z$ around closed curves in $D$ are zero.

The triangle $T$ is contained in $D$, and $\partial T$ is a closed curve in $D$. So $\int_{\partial T} dz/z = 0$.

> [!note]- Alternative via Goursat directly
> On the slit plane $D$, $1/z$ is holomorphic. By Goursat (which is just "holomorphic on a domain containing the triangle"), $\int_{\partial T} dz/z = 0$. No need to invoke the full star-shaped theorem.

> [!note]- Complete formal solution
> $T$ does not enclose $0$, so there is a ray $L$ from $0$ disjoint from $T$. Set $D = \mathbb{C} \setminus L$, the slit plane: open, star-shaped (with respect to any point in the half-plane opposite to $L$), and avoiding $0$, and $T \subseteq D$.
>
> $f(z) = 1/z$ is holomorphic on $D$. By [[Thm - Goursat's Theorem (Cauchy for a Triangle)|Goursat]] (which gives the conclusion directly for a holomorphic function on an open set containing the triangle), $\int_{\partial T} dz/z = 0$. $\blacksquare$

---

# Key Takeaways

**Topological obstruction is local to "enclosing".**

The contour integral $\int_\gamma dz/z$ is nonzero when $\gamma$ encloses $0$ (winding number $\neq 0$), zero otherwise. The unit circle encloses $0$ (winding $1$): integral $2\pi i$. A triangle in $\mathbb{C}^\times$ not enclosing $0$: integral $0$. The general winding-number theorem ([[Complex Analysis III — Winding, Laurent, Residues|CA III]]) formalizes this.

**Cauchy on non-simply-connected domains via star-shaped subdomains.**

Cauchy's theorem requires *some* topological condition (star-shaped, simply connected, etc.). For a general curve in a non-simply-connected domain, one finds a star-shaped subdomain containing the curve. The verification of the theorem reduces to identifying the right subdomain.

**Triangle as a star-shaped surrogate.**

For any closed curve in a non-simply-connected domain, one can often approximate by a polygonal curve and decompose into triangles. Each triangle lies in a star-shaped subdomain (provided the triangle doesn't enclose an obstruction). Sum the triangle integrals to get the full polygon integral. This is one strategy for extending Cauchy beyond star-shaped to general simply-connected, in CA III.

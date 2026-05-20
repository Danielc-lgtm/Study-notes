---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Thm - Cauchy–Riemann Equations"
tags: [analysis, complex-analysis]
---

# Notation

$U, V \subseteq \mathbb{C}$ are open sets. A map $f : U \to V$ is conformal at $z_0$ if $f$ is holomorphic at $z_0$ with $f'(z_0) \neq 0$. We write $f : U \to V$ is a **conformal equivalence** (or **biholomorphism**) if $f$ is a holomorphic bijection with holomorphic inverse. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Axiom Motivation

A *conformal* map is one that preserves angles. Geometrically, conformality is the property that "infinitesimal squares are mapped to infinitesimal squares" (not, say, infinitesimal parallelograms). The map can distort lengths and orientations differently in different directions, but at each point, the angle between any two intersecting curves is preserved.

Why is this property worth a name? Because it is exactly the geometric content of "holomorphic with nonvanishing derivative". A holomorphic function $f$ at $z_0$ with $f'(z_0) \neq 0$ acts locally as $f(z) \approx f(z_0) + f'(z_0)(z - z_0)$ — multiplication by the complex number $f'(z_0)$, which rotates by $\arg f'(z_0)$ and scales by $|f'(z_0)|$. *Multiplication by a complex number is a similarity transformation*: it preserves angles, scales lengths uniformly (in every direction), and preserves orientation. So a holomorphic function with nonvanishing derivative is exactly an *angle-preserving, orientation-preserving similarity at every point*.

The converse holds too: a $C^1$ map of $\mathbb{R}^2 \to \mathbb{R}^2$ (viewed as a map of $\mathbb{C}$) that is angle-preserving and orientation-preserving must satisfy the Cauchy-Riemann equations, hence is holomorphic. So **holomorphic + nonzero derivative ⟺ conformal**.

This is one of the deepest "true names" in complex analysis: the *holomorphic* condition (a calculus condition) is *equivalent* to the *conformal* condition (a geometric condition). The two definitions are different but describe the same class of functions, and the equivalence is the source of many applications: solving Laplace's equation on complicated domains by conformal mapping, classifying conformally equivalent surfaces, designing aerofoils.

The condition $f'(z_0) \neq 0$ is crucial. If $f'(z_0) = 0$, the linear approximation $f(z) - f(z_0) \approx 0$ is degenerate, and the local behaviour is dominated by higher-order terms. For instance, $f(z) = z^2$ has $f'(0) = 0$, and locally near $0$ behaves like $z \mapsto z^2$, which is *not* angle-preserving — angles at $0$ are *doubled*. The local mapping degree is $k$ in this case, meaning $f$ wraps a small neighborhood of $0$ $k$ times around $f(0) = 0$.

A *conformal map* (not just conformal at a point) is one that is conformal at every point of its domain — holomorphic with nowhere-zero derivative.

What would break with a different definition? Asking only for "holomorphic, possibly with zero derivatives": includes maps like $z^2$ at the origin, which fail angle preservation. Asking for "differentiable and angle-preserving" (in the real-variable sense): turns out to give exactly the holomorphic functions, so no difference. Asking for "orientation-preserving and conformal": the orientation condition is automatic from the determinant of the Jacobian being $|f'(z)|^2 > 0$.

---

# The Definition

Let $U \subseteq \mathbb{C}$ be open and $f : U \to \mathbb{C}$.

**Conformal at a point.** $f$ is **conformal at $z_0 \in U$** if $f$ is holomorphic at $z_0$ with $f'(z_0) \neq 0$. Equivalently, $f$ is real-differentiable at $z_0$, the differential is non-degenerate, and the differential preserves angles and orientation.

**Conformal map.** $f : U \to V$ is a **conformal map** (or **conformal mapping**) if $f$ is conformal at every point of $U$ — i.e., $f$ is holomorphic on $U$ with $f'(z) \neq 0$ for all $z \in U$.

**Conformal equivalence (biholomorphism).** $f : U \to V$ is a **conformal equivalence** if $f$ is a *bijective* conformal map, in which case the inverse $f^{-1} : V \to U$ is also a conformal map. We say $U$ and $V$ are **conformally equivalent** (or **biholomorphic**) if there exists such an $f$.

**Local conformal equivalence.** $f$ is **locally conformal** at $z_0$ if $f$ is conformal at $z_0$ — by the [[Thm - Holomorphic Inverse Function Theorem|holomorphic inverse function theorem]], $f$ is then a biholomorphism between a neighborhood of $z_0$ and a neighborhood of $f(z_0)$.

---

# Relate to Other Fields / Compression

In **Riemannian geometry**, a conformal map between Riemannian manifolds is a diffeomorphism preserving angles. For $\mathbb{R}^2 = \mathbb{C}$ with the standard metric, the conformal maps are exactly the holomorphic functions with nonzero derivative (plus anti-holomorphic with nonzero "anti-derivative", which we exclude by requiring orientation preservation). In higher dimensions, **Liouville's theorem** (different from the complex one) says conformal maps on $\mathbb{R}^n$ for $n \geq 3$ are rigid: they are compositions of Möbius transformations on $\mathbb{R}^n$, with no infinite-dimensional family. The "infinite richness" of conformal maps in 2D is what makes complex analysis applicable to PDE.

In **physics**, conformal field theories are quantum field theories invariant under conformal transformations. In 2D, the conformal group is infinite-dimensional (generated by holomorphic and anti-holomorphic local conformal maps), and this infinite symmetry is what makes 2D CFT a uniquely tractable subject. In higher dimensions, the conformal group is finite-dimensional (Möbius-like).

In **fluid dynamics**, conformal maps are the technique for solving Laplace's equation on complicated domains: map conformally to a simple domain (disc or half-plane), solve there, pull back. This works because *conformal maps preserve Laplace's equation* (composing a harmonic function with a conformal map gives another harmonic function).

---

# Examples / Corollaries

**Is an instance — affine maps.** $z \mapsto az + b$ for $a \neq 0$. Holomorphic with $f' = a \neq 0$ everywhere, hence conformal.

**Is an instance — exponential.** $z \mapsto e^z$ has $f' = e^z \neq 0$ everywhere, hence conformal at every $z \in \mathbb{C}$. Maps horizontal strips $\{a < \operatorname{Im} z < b\}$ to sectors of the plane.

**Is an instance — Cayley transform.** $z \mapsto (z - i)/(z + i)$ has $f' = 2i/(z + i)^2 \neq 0$ for $z \neq -i$, hence conformal. Maps the upper half-plane $\mathbb{H}$ to the unit disc $\mathbb{D}$.

**Is NOT an instance globally — $z \mapsto z^2$.** Has $f'(z) = 2z = 0$ at $z = 0$. So $f$ is not conformal *at* $z = 0$, although it is conformal elsewhere. On $\mathbb{C}\setminus\{0\}$ it is conformal but not bijective.

**Is NOT an instance — $z \mapsto \bar z$ (complex conjugation).** Real-differentiable and angle-preserving in magnitude, but *reverses orientation*. Not holomorphic (fails Cauchy-Riemann). Excluded from "conformal" by the orientation-preserving requirement.

**Corollary — invariance of harmonicity under conformal maps.** If $u$ is harmonic on $V$ and $f : U \to V$ is conformal, then $u \circ f$ is harmonic on $U$. This is the key property used in solving Dirichlet problems via conformal mapping: map a hard domain to an easy one, solve, pull back the solution.

**Corollary — conformal map preserves the cross-ratio.** A Möbius transformation (a conformal automorphism of $\hat{\mathbb{C}}$) preserves the *cross-ratio* of four points: $(z_1, z_2; z_3, z_4) := \frac{(z_1 - z_3)(z_2 - z_4)}{(z_1 - z_4)(z_2 - z_3)}$. This is the unique Möbius invariant.

**Calibration check — angles at a corner.** If $f$ is conformal at $z_0$ and two curves $\gamma_1, \gamma_2$ meet at $z_0$ at angle $\theta$, then $f \circ \gamma_1$ and $f \circ \gamma_2$ meet at $f(z_0)$ at the same angle $\theta$, in the same rotational sense. The conformality preserves both the magnitude and the direction of the angle.

---

# Unlocked by This

> [!tip] Riemann Mapping Theorem *(from §3.5+)*
> The [[Thm - Riemann Mapping Theorem (Statement)|Riemann mapping theorem]] says every simply connected proper open $U \subset \mathbb{C}$ is conformally equivalent to $\mathbb{D}$. So the conformal equivalence class of a simply connected proper domain is *trivial* — there's only one such class.

> [!tip] Conformal Pullback of Laplace's Equation *(from Harmonic theory)*
> Solving Laplace's equation on a domain $U$ reduces to solving it on a simpler conformally-equivalent domain $V$ — see [[Ex - Solving Dirichlet on a half-plane via conformal mapping]].

> [!tip] Hyperbolic Geometry on the Disc *(from Differential Geometry)*
> The conformal automorphisms of the unit disc are the isometries of the **Poincaré disc model** of hyperbolic geometry. Conformality is what makes the hyperbolic angle equal to the Euclidean angle in this model.

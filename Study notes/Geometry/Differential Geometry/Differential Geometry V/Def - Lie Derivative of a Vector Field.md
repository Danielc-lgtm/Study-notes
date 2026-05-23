---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Flow of a Vector Field"
  - "Def - The Differential of a Smooth Map"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold. $X, Y \in \mathfrak{X}(M)$ are smooth [[Def - Smooth Vector Field|vector fields]]. $\phi^X : \mathcal{D} \to M$ is the [[Def - Flow of a Vector Field|flow]] of $X$, with $\phi^X_t : M_t \to M_{-t}$ the time-$t$ diffeomorphism wherever defined. $d(\phi^X_{-t})_{\phi^X_t(p)} : T_{\phi^X_t(p)} M \to T_p M$ is the [[Def - The Differential of a Smooth Map|differential]] of $\phi^X_{-t}$ at the point $\phi^X_t(p)$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Axiom Motivation

We want to make sense of "the rate of change of a vector field $Y$ in the direction of $X$". On $\mathbb{R}^n$ this is unproblematic: $Y$ is a function $\mathbb{R}^n \to \mathbb{R}^n$, and the directional derivative is

$$D_v Y(p) = \frac{d}{dt}\bigg|_{t=0} Y(p + tv) = \lim_{t \to 0} \frac{Y(p + tv) - Y(p)}{t},$$

evaluable because $Y(p + tv)$ and $Y(p)$ are both elements of $\mathbb{R}^n$, so their difference makes sense.

On a manifold the difficulty is severe: $Y_{\phi_t(p)} \in T_{\phi_t(p)} M$ and $Y_p \in T_p M$, and these are different vector spaces. There is no canonical way to subtract $Y_p$ from $Y_{\phi_t(p)}$. We need to *transport* one to live in the other's tangent space before we can compare them.

The "transport" available without any extra structure (no metric, no connection) is the **flow of $X$**: $\phi^X_t$ is a diffeomorphism (locally), so its differential $d(\phi^X_t)_p : T_p M \to T_{\phi^X_t(p)} M$ identifies the tangent spaces. The transport of $Y_{\phi^X_t(p)}$ back to $T_p M$ is therefore

$$\big(d(\phi^X_{-t})_{\phi^X_t(p)}\big) \big(Y_{\phi^X_t(p)}\big) \;\in\; T_p M,$$

— pull back $Y$ along the flow of $X$. Now both this and $Y_p$ live in $T_p M$, and we can take their difference and differentiate at $t = 0$:

$$(\mathcal{L}_X Y)_p := \frac{d}{dt}\bigg|_{t=0} \big(d(\phi^X_{-t})_{\phi^X_t(p)}\big) \big(Y_{\phi^X_t(p)}\big).$$

This is the **Lie derivative**, the natural rate of change of $Y$ "in the moving frame of $\phi^X$".

The conceptual content of this construction: the Lie derivative measures the discrepancy between "$Y$ at the next moment" and "the flow's expected version of $Y$ at the next moment". If $Y$ is *invariant* under the flow of $X$ — meaning $\phi^X_t$ maps $Y_p$ exactly to $Y_{\phi^X_t(p)}$, equivalently $d(\phi^X_t)_p(Y_p) = Y_{\phi^X_t(p)}$ — then the pulled-back vector field equals $Y$ at every $t$, and the Lie derivative vanishes. So **$\mathcal{L}_X Y = 0$ if and only if $Y$ is invariant under the flow of $X$.**

Why is this the *right* construction, given that other natural-looking candidates exist? The cleanest evidence is the identification

$$\mathcal{L}_X Y = [X, Y],$$

— the Lie derivative *equals* the Lie bracket (Lee Theorem 9.38, restated in [[Thm - Lie Bracket Properties]]). This is not a coincidence; it is the fundamental theorem that makes the bracket geometric. So the algebraic Lie bracket and the geometric Lie derivative are two faces of one object: the bracket is the operational tool for computing, the Lie derivative is the operational tool for understanding what the bracket *means*.

A reader who has never seen this construction might invent it by asking: "What is the only natural way to differentiate a vector field along another vector field, given only the smooth structure of $M$?" The answer is "transport via the flow and take the difference at $t = 0$" — there is no other natural transport without additional structure.

Could one differentiate $Y$ in a different direction without using flows — say, in the direction of a tangent vector $v \in T_p M$ alone? No, because differentiating requires comparing $Y$ at two nearby points, which requires identifying their tangent spaces, which requires transport. To use just $v$, one would need a connection — see [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]] for the preview, and Riemannian Geometry for the full development. Without a connection, the Lie derivative along $X$ is the only natural notion of "directional derivative of a vector field", and it requires a *vector field* $X$, not just a tangent vector $v$.

What changes if we replace $\phi^X_{-t}$ by $\phi^X_t$ in the formula? The sign flips: we would get $-\mathcal{L}_X Y$ rather than $\mathcal{L}_X Y$. The choice of $\phi^X_{-t}$ (pulling back) rather than $\phi^X_t$ (pushing forward) is a convention; the formula above is the standard one.

---

# The Definition

Let $X, Y \in \mathfrak{X}(M)$ be smooth vector fields, and let $\phi^X$ denote the flow of $X$. The **Lie derivative** of $Y$ along $X$ is the smooth vector field $\mathcal{L}_X Y \in \mathfrak{X}(M)$ defined pointwise by

$$(\mathcal{L}_X Y)_p \;:=\; \frac{d}{dt}\bigg|_{t=0} \big(d(\phi^X_{-t})_{\phi^X_t(p)}\big)\big(Y_{\phi^X_t(p)}\big) \;=\; \lim_{t \to 0} \frac{d(\phi^X_{-t})_{\phi^X_t(p)}(Y_{\phi^X_t(p)}) - Y_p}{t}.$$

The derivative exists for every $p \in M$ and the resulting assignment $p \mapsto (\mathcal{L}_X Y)_p$ is smooth (Lee Lemma 9.36).

The fundamental identification (Lee Theorem 9.38; proved in [[Thm - Lie Bracket Properties]]) is:

$$\mathcal{L}_X Y \;=\; [X, Y].$$

Thus the Lie derivative of $Y$ along $X$ is computed in practice by the bracket formula

$$(\mathcal{L}_X Y)^j = X^i \frac{\partial Y^j}{\partial x^i} - Y^i \frac{\partial X^j}{\partial x^i}$$

in any chart, even though the *meaning* is the flow-derivative formula above.

The Lie derivative extends, with the same defining formula (pull back along the flow and differentiate), to smooth functions, covector fields, tensor fields, and differential forms. On a smooth function $f \in C^\infty(M)$, $\mathcal{L}_X f = Xf$. On a differential form $\omega$, Cartan's magic formula reads $\mathcal{L}_X \omega = d\iota_X \omega + \iota_X d\omega$ (see [[Differential Geometry VIII — Differential Forms]]).

---

# Relate to Other Fields / Compression

In Riemannian geometry, the Lie derivative is one of two natural derivatives on a manifold; the other is the **covariant derivative** $\nabla_X Y$ (the Levi-Civita derivative), which requires a metric. The two derivatives differ:

$$\mathcal{L}_X Y - \nabla_X Y = -\nabla_Y X + T(X, Y),$$

where $T$ is the torsion. For the Levi-Civita connection ($T = 0$), the relation simplifies to $[X, Y] = \nabla_X Y - \nabla_Y X$, expressing the bracket as the antisymmetric part of the covariant derivative. So the Lie derivative is the **antisymmetric, metric-free** part of differentiation; the covariant derivative is the **metric-dependent** part. Without a metric, only the Lie derivative is available — see [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]] forward.

In physics, the Lie derivative measures how a tensor field changes under a "drag" by a vector field. **Killing's equation** $\mathcal{L}_X g = 0$ asks that a metric be invariant under the flow of $X$, characterizing the **Killing vector fields** — the infinitesimal isometries. The Killing fields of Minkowski space are the generators of the Poincaré group; the Killing fields of a Schwarzschild black hole are the time-translation and the spherical rotations.

**True name:** The Lie derivative $\mathcal{L}_X Y$ is **the rate of change of $Y$ as seen by an observer riding the flow of $X$**. Computationally it equals the Lie bracket $[X, Y]$; geometrically it is the flow-pulled-back $Y$, differentiated.

---

# Examples / Corollaries

**Is an instance: $\mathcal{L}_X f = Xf$ for $f \in C^\infty(M)$.** The Lie derivative of a function along $X$ is just the directional derivative — the action of $X$ on $f$ as a derivation. This is the function-level case, where the pull-back is just $f \circ \phi^X_t$ and the derivative at $t = 0$ is $\frac{d}{dt}\big|_{t=0} f(\phi^X_t(p)) = X_p f$.

**Is an instance: $\mathcal{L}_X Y$ for $X = \partial_x$ and $Y = x^2 \partial_y$ on $\mathbb{R}^2$.** Bracket formula: $[X, Y]^x = (1)(0) - (x^2)(0) = 0$, $[X, Y]^y = (1)(2x) - (x^2)(0) = 2x$, so $\mathcal{L}_X Y = 2x \partial_y$. Geometric check: the flow of $X$ is $\phi_t(x, y) = (x + t, y)$, so $\phi_{-t*}(Y_{\phi_t(p)}) = \phi_{-t*}((x+t)^2 \partial_y) = (x+t)^2 \partial_y$ at $p$; differentiating in $t$ at $0$ gives $2x \partial_y$ — same answer.

**Is an instance: $\mathcal{L}_X X = 0$.** Every vector field is invariant under its own flow ($X$ is "carried by itself"), so the Lie derivative vanishes. This is also immediate from the bracket: $[X, X] = 0$ by antisymmetry. See [[Ex - Lie Derivative Annihilates Constant Functions]] for the function-level version.

**Is an instance: $\mathcal{L}_X Y = -\mathcal{L}_Y X$.** From $\mathcal{L}_X Y = [X, Y]$ and antisymmetry of the bracket. Even though the geometric definitions of $\mathcal{L}_X Y$ and $\mathcal{L}_Y X$ are not visibly antisymmetric (one uses the flow of $X$, the other the flow of $Y$), their values match via the bracket identification.

**Is an instance: $\mathcal{L}_X (fY) = (Xf) Y + f \mathcal{L}_X Y$ — Leibniz rule.** The Lie derivative is a derivation of the $C^\infty(M)$-module $\mathfrak{X}(M)$. Proof: from the bracket, $[X, fY] = X(f)Y + f[X, Y] = (Xf)Y + f \mathcal{L}_X Y$. The Leibniz rule holds in any module-with-derivation structure on tensor fields.

**Is NOT an instance: the Lie derivative as a "directional derivative of $Y$ along a fixed tangent vector $v$".** The Lie derivative requires a **vector field** $X$, not just a tangent vector $v$ at $p$, because we use the flow of $X$ (which exists in a neighbourhood). One cannot define "$\mathcal{L}_v Y$" for a single tangent vector $v$; the closest available analogue would require a connection, giving $\nabla_v Y$.

**Is NOT an instance: a $C^\infty(M)$-linear operation in $X$.** The map $X \mapsto \mathcal{L}_X Y$ is *not* $C^\infty(M)$-linear in $X$: $\mathcal{L}_{fX} Y = f \mathcal{L}_X Y - (Yf) X \neq f \mathcal{L}_X Y$ in general. The obstruction $(Yf)X$ matches the obstruction to $C^\infty(M)$-bilinearity in the bracket.

**Corollary (flow invariance).** $\mathcal{L}_X Y = 0$ if and only if $Y$ is invariant under the flow of $X$, equivalently $d(\phi^X_t)_p(Y_p) = Y_{\phi^X_t(p)}$ for all $(t, p)$ in the flow domain. By the bracket identification, $\mathcal{L}_X Y = 0 \iff [X, Y] = 0 \iff$ flows of $X$ and $Y$ commute (see [[Thm - Commuting Flows Theorem]]).

**Corollary (Lie derivative computes the rate of flow-pullback).** More generally than at $t = 0$: for any $t_0$ in the flow domain,
$$\frac{d}{dt}\bigg|_{t = t_0} \big(d(\phi^X_{-t})_{\phi^X_t(p)}\big)(Y_{\phi^X_t(p)}) = d(\phi^X_{-t_0})_{\phi^X_{t_0}(p)}\big((\mathcal{L}_X Y)_{\phi^X_{t_0}(p)}\big).$$
(Lee Proposition 9.41.) So the Lie derivative gives the derivative of the flow-pullback at *every* time, not just at $t = 0$.

**Corollary ($\mathcal{L}_X$ is a derivation of the Lie algebra).** $\mathcal{L}_X[Y, Z] = [\mathcal{L}_X Y, Z] + [Y, \mathcal{L}_X Z]$. This is the Jacobi identity reinterpreted: writing each side in bracket notation gives the Jacobi identity for $X, Y, Z$. So $\mathrm{ad}_X = [X, \cdot\,]$ is a derivation of the Lie bracket, and the Lie derivative is the geometric expression of this fact.

**Calibration check.** You should be able to: (a) compute $\mathcal{L}_X f$ for $X = \partial_x$ and $f(x, y) = x^2 y$ (answer: $\mathcal{L}_X f = 2xy$, equal to $Xf$); (b) verify that a function $f$ is constant along the integral curves of $X$ if and only if $\mathcal{L}_X f = 0$ (the standard test for conservation laws); (c) explain why $\mathcal{L}_X Y$ can be nonzero even when $X_p = 0$ at a particular point $p$ (the Lie derivative depends on the derivatives of $X$, not just its value).

---

# Unlocked by This

> [!tip] Killing Vector Field *(from Riemannian / Lorentzian Geometry)*
> A **Killing vector field** $X$ on a Riemannian (or Lorentzian) manifold $(M, g)$ is one satisfying $\mathcal{L}_X g = 0$ — the metric is invariant under the flow of $X$. Killing fields are infinitesimal isometries; they form a finite-dimensional Lie subalgebra of $\mathfrak{X}(M)$, and on compact Riemannian manifolds they integrate to a Lie group action (the isometry group). The number of Killing fields measures the symmetry of the metric: $\mathbb{R}^n$ and $S^n$ have $\binom{n+1}{2}$ Killing fields each (maximal symmetry); a generic metric has none. In general relativity, Killing vector fields correspond to **conservation laws** by Noether's theorem.

> [!tip] Lie Derivative on Forms and Cartan's Magic Formula *(from Differential Forms)*
> The Lie derivative extends to differential forms in [[Differential Geometry VIII — Differential Forms]], and on forms it satisfies **Cartan's magic formula** $\mathcal{L}_X = d \iota_X + \iota_X d$, where $\iota_X$ is interior product and $d$ is the exterior derivative. This formula reduces every Lie-derivative computation on forms to two simpler operations, and it is the bridge between the Lie derivative and de Rham cohomology — flow-invariance of a closed form is automatic when the form is exact.

> [!tip] Adjoint Representation of a Lie Algebra *(from Lie Theory)*
> The map $X \mapsto \mathrm{ad}_X = [X, \cdot\,] = \mathcal{L}_X$ is the **adjoint representation** of the Lie algebra $\mathfrak{X}(M)$ on itself. It is a Lie algebra homomorphism $\mathfrak{X}(M) \to \mathrm{End}(\mathfrak{X}(M))$; the Jacobi identity is precisely the statement that $\mathrm{ad}$ is a Lie algebra homomorphism. For a finite-dimensional Lie algebra, the adjoint representation is the central tool for the structure theory (Killing form, semi-simplicity, root systems) — see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

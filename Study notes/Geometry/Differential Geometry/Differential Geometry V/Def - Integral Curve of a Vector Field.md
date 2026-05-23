---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Field on a Manifold"
  - "Def - Smooth Vector Field"
  - "Def - The Tangent Space"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold. $X \in \mathfrak{X}(M)$ is a smooth [[Def - Smooth Vector Field|vector field]]. A **smooth curve** in $M$ is a smooth map $\gamma : J \to M$ with $J \subseteq \mathbb{R}$ an open interval. The **velocity** of $\gamma$ at $t \in J$ is the tangent vector $\gamma'(t) := d\gamma_t(d/dt|_t) \in T_{\gamma(t)} M$, where $d\gamma_t$ is the differential of $\gamma$ at $t$. In a chart $(U, (x^i))$ with $X = X^i \partial_i$, write $\gamma$ in coordinates as $(\gamma^1(t), \dots, \gamma^n(t))$; then $\gamma'(t) = \dot\gamma^i(t)\, \partial_i|_{\gamma(t)}$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Axiom Motivation

Once a vector field is in place, it is impossible *not* to ask: "If I stand at $p$ and follow the arrow, where do I go?" An integral curve is the formalization of this question. Concretely, we want a smooth curve $\gamma : J \to M$ that *is* the trajectory of the velocity field $X$ — its tangent at every moment equals $X$ evaluated at the point it has reached. The single defining equation is

$$\gamma'(t) = X_{\gamma(t)}.$$

Why this exact equation and not some variant? The first variant to consider is $\gamma'(t) = X_p$, with $X$ evaluated at the starting point $p$ rather than at the current location. This would give straight lines tangent to $X_p$ at $p$ — *not* curves following the changing vector field. We want the curve to respond to the field at every point of its passage, not just at the start, so the right side must be $X_{\gamma(t)}$, not $X_{\gamma(0)}$.

A second variant: $\gamma'(t) = c(t) X_{\gamma(t)}$ for some function $c$, allowing reparametrization. This is *not* the standard definition because the chapter wants to capture the unique "natural" speed at which the integral curve traverses the orbits — and that speed is precisely $|X|$ (where $|X|$ would require a metric, which we do not have, but conceptually the parametrization is fixed by the equality, not by a more general proportionality). With reparametrization allowed, the integral *curve* would become an integral *orbit* (the image of $\gamma$, forgetting the parametrization), and we would lose the connection to flows. So we hard-code $c(t) = 1$ into the definition.

A third question: why require $\gamma$ to be smooth? We need to differentiate $\gamma$ to even *state* the integral-curve condition, so we need at least $C^1$ regularity. Once we have $C^1$ and an autonomous smooth ODE on the right side, the standard ODE smoothness theorem ([[Thm - The Contraction Mapping Principle|Picard–Lindelöf]]'s smoothness conclusion) upgrades $C^1$ to $C^\infty$ automatically. So demanding smoothness is no cost — every $C^1$ integral curve of a smooth vector field is automatically smooth — and it lets us use the smooth manifold machinery without bookkeeping the regularity at every step.

The constraint $0 \in J$ (for the "starting point" terminology) is a convention — by translation we can always shift so the parameter starts at $0$. Once $\gamma(0) = p$ is the starting point, the curve is determined uniquely by the ODE; see the existence-and-uniqueness theorem ([[Thm - Existence and Uniqueness of Integral Curves]]).

What this definition *captures*: the trajectory of a particle whose velocity field is given by $X$. What it *excludes*: curves that share the trajectory but not the parametrization (those are "orbits", not integral curves), and any notion of "average velocity" or "secant" (these are global, but integral curves are infinitesimal — they integrate an instantaneous condition).

Could we have replaced $\gamma'(t) = X_{\gamma(t)}$ by a condition only on $\gamma(t) - \gamma(s)$ for $s$ near $t$? In principle yes — we could ask that the curve be tangent to $X$ at every point — but the standard formulation, which we use here, packages this into the cleaner ODE statement.

---

# The Definition

Let $M$ be a smooth manifold and $X \in \mathfrak{X}(M)$ a smooth vector field. An **integral curve** of $X$ is a smooth curve $\gamma : J \to M$ on an open interval $J \subseteq \mathbb{R}$ satisfying

$$\gamma'(t) = X_{\gamma(t)} \quad \text{for all } t \in J.$$

If $0 \in J$, the point $\gamma(0) \in M$ is called the **starting point** of $\gamma$. We say $\gamma$ is the integral curve starting at $p$ if $\gamma(0) = p$.

In a chart $(U, (x^i))$ with $X = X^i \partial/\partial x^i$, writing $\gamma$ in coordinates as $(\gamma^1, \dots, \gamma^n)$, the integral curve condition becomes the system of ordinary differential equations

$$\dot\gamma^i(t) = X^i(\gamma^1(t), \dots, \gamma^n(t)), \qquad i = 1, \dots, n,$$

an **autonomous first-order ODE system**. ("Autonomous" means the right side does not depend explicitly on $t$.) An integral curve is **maximal** if its domain $J$ cannot be enlarged to a strictly larger interval on which it remains an integral curve.

---

# Relate to Other Fields / Compression

In ordinary differential equations, an integral curve is exactly a **solution to a first-order autonomous ODE system**. The translation between the languages is clean: a vector field on $M$ becomes, in any chart, a smooth $\mathbb{R}^n$-valued function $X^i$, and the integral curve condition is the corresponding ODE $\dot\gamma^i = X^i \circ \gamma$. So the chapter is, in part, "qualitative ODE theory on manifolds".

In physics, an integral curve is the **trajectory of a particle in a velocity field**: given a velocity field on configuration space (or phase space), the particle follows an integral curve. This is the connection to [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Hamiltonian mechanics]]: the trajectories of a mechanical system are integral curves of the Hamiltonian vector field on phase space.

**True name:** An integral curve is **a parametrized trajectory of $X$, with parametrization fixed by the equation $\gamma' = X \circ \gamma$**. The word "trajectory" captures the orbit; the word "parametrized" captures the choice of speed; the equation captures both at once.

---

# Examples / Corollaries

**Is an instance: the integral curve of $\partial/\partial x$ on $\mathbb{R}^2$.** Take $X = \partial/\partial x$. The ODE $\dot\gamma^1 = 1$, $\dot\gamma^2 = 0$ has solutions $\gamma(t) = (a + t, b)$ — horizontal lines, traversed at unit speed. Through every point $(a, b)$ there is exactly one integral curve, and they fill $\mathbb{R}^2$ disjointly.

**Is an instance: the integral curve of the rotation field $W = -y \partial_x + x \partial_y$ on $\mathbb{R}^2$.** The ODE is $\dot x = -y$, $\dot y = x$ — the harmonic oscillator. Its solutions are $\gamma(t) = (a \cos t - b \sin t,\, a \sin t + b \cos t)$, circles centred at the origin traversed counterclockwise, with the constant solution $(0, 0)$ as a fixed point. Through every point there is exactly one integral curve.

**Is an instance: the blowing-up integral curve of $W = x^2 \partial_x$ on $\mathbb{R}$.** The ODE $\dot\gamma = \gamma^2$ has solution $\gamma(t) = a / (1 - at)$ starting at $\gamma(0) = a$. For $a > 0$ the curve escapes to $+\infty$ at finite time $t = 1/a$ and cannot be extended past it. So integral curves need not be defined for all $t \in \mathbb{R}$ — this is the failure of [[Def - Complete Vector Field|completeness]].

**Is an instance: a constant integral curve at a singular point.** If $X_p = 0$, then the constant curve $\gamma(t) \equiv p$ satisfies $\gamma'(t) = 0 = X_{\gamma(t)}$, so it is an integral curve. By uniqueness, this is the unique integral curve starting at $p$. Singular points of $X$ are exactly the equilibrium points of the flow.

**Is NOT an instance: a curve tangent to $X$ only at $\gamma(0)$.** Suppose $X = \partial_x$ on $\mathbb{R}^2$ and let $\gamma(t) = (t, t)$. Then $\gamma'(0) = (1, 1) \neq X_{\gamma(0)} = (1, 0)$, so $\gamma$ is not an integral curve. Even matching the velocity at $\gamma(0)$ would not suffice; the condition must hold at *every* point.

**Is NOT an instance: a curve traversing the same orbit but at a different speed.** Take $X = \partial_x$ on $\mathbb{R}$ and consider $\gamma(t) = (2t, 0)$. The orbit is correct (the $x$-axis), but $\gamma'(t) = (2, 0) \neq X_{\gamma(t)} = (1, 0)$. This is an integral curve of the *rescaled* field $2X = 2\partial_x$, not of $X$ itself. The parametrization is fixed by the vector field, not chosen freely.

**Corollary (translation lemma).** If $\gamma : J \to M$ is an integral curve of $X$ and $b \in \mathbb{R}$, then $\tilde\gamma(t) = \gamma(t + b)$, defined on $\tilde J = \{t : t + b \in J\}$, is also an integral curve of $X$. This is because the ODE is autonomous — time-translation is a symmetry. The reparametrization shifts the starting point: $\tilde\gamma(0) = \gamma(b)$.

**Corollary (rescaling lemma).** If $\gamma : J \to M$ is an integral curve of $X$ and $a \in \mathbb{R}$, then $\tilde\gamma(t) = \gamma(at)$ is an integral curve of $aX$, defined on $\tilde J = \{t : at \in J\}$. The proof is the chain rule. So scaling the vector field by a constant scales the speed of the integral curves — and reverses direction if $a < 0$.

**Corollary (smoothness from $C^1$).** If $\gamma$ is a $C^1$ curve satisfying the integral-curve equation for a smooth $X$, then $\gamma$ is automatically smooth. The reason is bootstrap: $\gamma'(t) = X(\gamma(t))$ is the composition of $\gamma$ and $X$, smooth in any argument that $\gamma$ is regular enough; differentiating gives $\gamma'' = dX(\gamma) \cdot \gamma'$, which is one degree smoother, and induction gives all derivatives smooth.

**Calibration check.** You should be able to: (a) compute the integral curve of $X = x \partial_x$ on $\mathbb{R}$ starting at $x_0$ (answer: $\gamma(t) = x_0 e^t$ — exponential growth, defined for all $t$, so $X$ is complete); (b) verify that the orbit-image $\gamma(J) \subset M$ depends only on the unparametrized vector field (the orbit is the same for $X$ and for $cX$, but the parametrization changes by rescaling); (c) explain why the integral curve through a regular point $p$ ($X_p \neq 0$) is an immersion (its velocity is nonzero everywhere) — see [[Thm - Canonical Form for a Nonvanishing Vector Field]].

---

# Unlocked by This

> [!tip] Flow of a Vector Field *(within this chapter)*
> Assembling the integral curves through every point into a single map $\phi : \mathcal{D} \to M$ — the [[Def - Flow of a Vector Field|flow]] — packages the chapter's central construction. The flow is the *aggregate* of all integral curves; an integral curve is a *single slice* of the flow.

> [!tip] Phase Portrait *(from Dynamical Systems)*
> The collection of all integral curves of a vector field is its **phase portrait**, the central visual tool of dynamical systems. Equilibrium points (singularities of $X$), limit cycles (periodic integral curves), and basin boundaries are the qualitative features one extracts from the phase portrait. The Hartman–Grobman theorem says the local phase portrait near a hyperbolic equilibrium is topologically the same as the phase portrait of the linearized vector field.

> [!tip] Variational Principles *(from Geometric Mechanics)*
> In Hamiltonian mechanics, integral curves of the Hamiltonian vector field $X_H$ are the trajectories of the mechanical system, and they extremize the action functional. The differential-geometric content of "least action" is that the trajectories satisfy a first-order ODE on phase space — they are integral curves of $X_H$ — and the variational structure is a property of $X_H$ that distinguishes Hamiltonian flows from arbitrary flows.

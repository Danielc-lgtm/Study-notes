---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Field on a Manifold"
  - "Def - Smooth Vector Field"
  - "Def - Integral Curve of a Vector Field"
  - "Def - Diffeomorphism"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold, $X \in \mathfrak{X}(M)$ a smooth [[Def - Smooth Vector Field|vector field]]. A **flow domain** is an open subset $\mathcal{D} \subseteq \mathbb{R} \times M$ such that for each $p \in M$ the slice $\mathcal{D}^{(p)} = \{t \in \mathbb{R} : (t, p) \in \mathcal{D}\}$ is an open interval containing $0$. We write $\phi_t(p) = \phi(t, p)$ when $(t, p) \in \mathcal{D}$, and $\phi^{(p)}(t) = \phi(t, p)$ for fixed $p$; in this notation, $\phi^{(p)} : \mathcal{D}^{(p)} \to M$ is a curve and $\phi_t : M_t \to M_{-t}$ is a map between open subsets of $M$, where $M_t = \{p : (t, p) \in \mathcal{D}\}$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Axiom Motivation

The integral curves of a vector field $X$ partition $M$ into one-dimensional orbits, and for each $p$ there is a unique maximal integral curve $\phi^{(p)}$ starting at $p$. The **flow** is the natural way to package all these curves into a single object: a map $\phi : \mathbb{R} \times M \to M$ such that for each fixed $p$ the curve $t \mapsto \phi(t, p)$ is the integral curve starting at $p$. Equivalently, for each fixed $t$ the map $p \mapsto \phi(t, p)$ is "advance every point by time $t$ along the integral curve through it". The two viewpoints are the curve-perspective (vary $t$, fix $p$) and the map-perspective (vary $p$, fix $t$), and the flow combines them into one smooth map.

Why must we allow a *flow domain* $\mathcal{D} \subsetneq \mathbb{R} \times M$ rather than insist on a global flow $\mathbb{R} \times M \to M$? Because integral curves can escape — see [[Def - Complete Vector Field|complete vector field]] for the contrast — and they have maximal domains $\mathcal{D}^{(p)}$ that may be strictly smaller than $\mathbb{R}$. The flow $\phi(t, p) = \phi^{(p)}(t)$ is defined only where $\phi^{(p)}(t)$ is defined, which is the slice $\{t\} \times \{p\}$-version of "$t$ is in the maximal interval $\mathcal{D}^{(p)}$ of the integral curve starting at $p$". The domain $\mathcal{D}$ is the disjoint union of these slices, and the slice-conditions (open, contains $0$) force it to be open and to have the structure of a "horizontal-fibration" — the right side of the projection $\mathcal{D} \to M$ is an open interval at every point.

The **group laws** $\phi(0, p) = p$ and $\phi(t, \phi(s, p)) = \phi(t+s, p)$ deserve a moment's attention. The first is automatic: $\phi^{(p)}(0) = p$ is the starting condition. The second is the substantive content: it says that "follow $X$ for time $s$, then for time $t$" is the same as "follow $X$ for time $t + s$" — which is exactly the autonomous nature of the ODE $\dot\gamma = X(\gamma)$. The proof is the translation lemma for integral curves: the curve $s \mapsto \phi^{(p)}(s + t)$ is the integral curve starting at $\phi^{(p)}(t)$, hence equals $\phi^{(\phi_t(p))}$. So the group law is the geometric statement of "time-translation symmetry of an autonomous ODE".

A subtlety in the group law: even where the right-hand side $\phi(t+s, p)$ is defined, the left-hand side $\phi(t, \phi(s, p))$ requires $\phi(s, p)$ to be defined *and* $\phi(t, \phi(s, p))$ to be defined, which is a stronger condition. The group law as stated in the definition therefore reads "for all $s \in \mathcal{D}^{(p)}$ and $t \in \mathcal{D}^{(\phi_s(p))}$ such that $s + t \in \mathcal{D}^{(p)}$"; the equality holds wherever both sides make sense. For global flows ($\mathcal{D} = \mathbb{R} \times M$) the subtlety disappears.

Why insist on smoothness? Because we want the diffeomorphisms $\phi_t$ for varying $t$ to form a smooth family, and because in applications we need to differentiate the flow with respect to both arguments (the $\partial_t$ derivative recovers the vector field; the $\partial_p$ derivative gives the linearization of the flow). The smoothness is not for free — it comes from the smooth-dependence-on-initial-data conclusion of [[Thm - The Contraction Mapping Principle|Picard–Lindelöf]], applied via the Fundamental Theorem on Flows.

Could the flow be defined with $\mathcal{D}$ closed instead of open? No: openness is exactly the chart-version of "if a flow exists at $(t_0, p_0)$ it exists at a neighbourhood" — the local existence of integral curves is what makes $\mathcal{D}$ open. The flow domain being open is the geometric expression of "ODE solutions exist for a positive time interval".

---

# The Definition

Let $M$ be a smooth manifold. A **flow domain** is an open subset $\mathcal{D} \subseteq \mathbb{R} \times M$ such that for every $p \in M$ the set

$$\mathcal{D}^{(p)} := \{t \in \mathbb{R} : (t, p) \in \mathcal{D}\}$$

is an open interval containing $0$.

A **flow** on $M$ is a smooth map $\phi : \mathcal{D} \to M$, where $\mathcal{D}$ is a flow domain, satisfying:

1. **Identity at zero.** $\phi(0, p) = p$ for every $p \in M$.

2. **Group law.** For every $p \in M$, $s \in \mathcal{D}^{(p)}$, and $t \in \mathcal{D}^{(\phi(s, p))}$ such that $s + t \in \mathcal{D}^{(p)}$,
$$\phi(t, \phi(s, p)) = \phi(t + s, p).$$

We write $\phi_t(p) := \phi(t, p)$ and $\phi^{(p)}(t) := \phi(t, p)$. The flow is **global** if $\mathcal{D} = \mathbb{R} \times M$.

The **flow of a smooth vector field** $X \in \mathfrak{X}(M)$ is the unique smooth maximal flow $\phi^X : \mathcal{D} \to M$ such that for every $p \in M$ the curve $\phi^{(p)}$ is the maximal integral curve of $X$ starting at $p$; equivalently, $\frac{d}{dt}\big|_{t=0} \phi_t(p) = X_p$ and the chain rule gives $\frac{d}{dt} \phi_t(p) = X_{\phi_t(p)}$ for all $(t, p) \in \mathcal{D}$. Existence and uniqueness are the content of [[Thm - Fundamental Theorem on Flows]].

The vector field $X$ is called the **infinitesimal generator** of $\phi$, and conversely $\phi$ is the **flow generated by** $X$.

---

# Categorical / Structural Definition

A *global* flow on $M$ is a smooth left action of the additive group $(\mathbb{R}, +)$ on $M$: a smooth map $\phi : \mathbb{R} \times M \to M$ with $\phi_0 = \mathrm{id}_M$ and $\phi_{s+t} = \phi_s \circ \phi_t$. Equivalently, a global flow is a smooth group homomorphism $\mathbb{R} \to \mathrm{Diff}(M)$, where $\mathrm{Diff}(M)$ is the diffeomorphism group of $M$ (treated as an infinite-dimensional Lie group). Each $\phi_t$ is then a diffeomorphism of $M$, with inverse $\phi_{-t}$.

A *local* flow weakens this to a partial $\mathbb{R}$-action: $\phi_t$ is defined on an open subset $M_t \subseteq M$, the group law holds on appropriate domains, and one cannot demand $\phi_t$ be defined on all of $M$ when the vector field is incomplete. The "category" of flows is the category of partial group actions of $\mathbb{R}$ on smooth manifolds, with morphisms being equivariant smooth maps — but this framework is rarely used; the language of flow domains is enough.

The fundamental categorical fact is **Lie's third theorem in the simplest setting**: there is a bijection

$$\{\text{smooth vector fields on } M\} \;\longleftrightarrow\; \{\text{maximal smooth local flows on } M\}.$$

Going $\to$: assemble integral curves into the flow ([[Thm - Fundamental Theorem on Flows]]). Going $\leftarrow$: differentiate at $t = 0$ to recover the generator. This bijection is the differential-geometric heart of Lie theory.

---

# Relate to Other Fields / Compression

A flow on $\mathbb{R}^n$ is exactly a smooth solution to an autonomous ODE system, with all initial conditions assembled. The chapter generalizes from $\mathbb{R}^n$ to $M$ by reading the definitions chart-by-chart and gluing.

In dynamical systems, a flow is the central object of study. The **discrete-time** analogue is a *map* $f : M \to M$ and the dynamics is $p, f(p), f^2(p), \ldots$; the **continuous-time** analogue is a flow $\phi_t$, with $\phi_t \circ \phi_s = \phi_{t+s}$. Continuous-time flows are the smooth dynamics derived from a vector field, while discrete-time maps are studied for their own sake.

In physics, a flow describes time evolution. For a Hamiltonian $H : T^*M \to \mathbb{R}$, the Hamiltonian flow is the flow of the Hamiltonian vector field $X_H$ on phase space, and it preserves the symplectic form — see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] forward. For a Riemannian gradient field $\nabla f$, the gradient flow performs gradient descent on $f$.

**True name:** A flow is **a smooth one-parameter family of diffeomorphisms generated by a vector field**. The "one-parameter" is the $t$; the "diffeomorphisms" are the $\phi_t$; the "generated by a vector field" is the differential equation $\frac{d}{dt} \phi_t = X \circ \phi_t$.

---

# Examples / Corollaries

**Is an instance: the flow of $\partial/\partial x$ on $\mathbb{R}^2$.** $\phi_t(x, y) = (x + t, y)$, global flow ($\mathcal{D} = \mathbb{R} \times \mathbb{R}^2$). Each $\phi_t$ is translation by $t$ in the $x$-direction, a diffeomorphism. Group law: $\phi_t \circ \phi_s = \phi_{t+s}$.

**Is an instance: the rotation flow of $W = -y \partial_x + x \partial_y$ on $\mathbb{R}^2$.** $\phi_t(x, y) = (x \cos t - y \sin t,\, x \sin t + y \cos t)$, global flow. Each $\phi_t$ is rotation by angle $t$ about the origin. Group law: $\phi_t \circ \phi_s = \phi_{t+s}$ — composition of rotations adds angles.

**Is an instance: the local flow of $X = x^2 \partial_x$ on $\mathbb{R}$.** $\phi_t(x) = x/(1 - tx)$, with $\mathcal{D}^{(x)} = (-\infty, 1/x)$ for $x > 0$, $\mathcal{D}^{(x)} = (1/x, +\infty)$ for $x < 0$, and $\mathcal{D}^{(0)} = \mathbb{R}$ (the origin is a fixed point). Not global — escapes in finite time. Verify the group law: $\phi_t(\phi_s(x)) = \frac{x/(1-sx)}{1 - tx/(1-sx)} = \frac{x}{1 - (t+s)x} = \phi_{t+s}(x)$, on appropriate domain.

**Is an instance: the matrix exponential flow on $\mathbb{R}^n$.** For a constant matrix $A \in \mathbb{R}^{n \times n}$ and the linear vector field $X(x) = Ax$, the flow is $\phi_t(x) = e^{tA} x$, global. Group law: $e^{tA} e^{sA} = e^{(t+s)A}$ — the exponential map is a group homomorphism. This is the prototype of the exponential map in Lie theory.

**Is NOT an instance: a smooth map $\phi : \mathbb{R} \times M \to M$ failing the group law.** For instance, on $\mathbb{R}$ define $\phi(t, x) = x + t^2$. Then $\phi(0, x) = x$ (identity), but $\phi(t, \phi(s, x)) = x + s^2 + t^2 \neq x + (t + s)^2 = \phi(t + s, x)$. This is not a flow — there is no autonomous vector field generating it. The infinitesimal generator at $t = 0$ would be $\partial_t|_0 (x + t^2) = 0$, but this would give the trivial flow $\phi_t = \mathrm{id}$, not $\phi$ itself.

**Is NOT an instance: $\phi$ defined on a domain that fails the "openness" requirement.** If we tried to define a flow on $\mathcal{D} = [0, 1] \times M$, the slice $\mathcal{D}^{(p)} = [0, 1]$ is not an open interval, so this is not a flow domain. The right side of an ODE has no preference for forward vs backward time — we need *both* directions of the integral curve at each point, hence an open interval around $0$.

**Corollary (the flow recovers the vector field).** Given a smooth flow $\phi$, the infinitesimal generator $X_p = \frac{d}{dt}\big|_{t=0} \phi_t(p)$ is automatically a smooth vector field (smoothness of $\phi$ in $(t, p)$ gives smoothness of $X$ in $p$), and $\phi$ is the flow generated by $X$. The bijection between vector fields and maximal flows is the central content of [[Thm - Fundamental Theorem on Flows]].

**Corollary (each $\phi_t$ is a diffeomorphism).** For $(t, p) \in \mathcal{D}$, the map $\phi_t : M_t \to M_{-t}$ is a diffeomorphism with inverse $\phi_{-t}$. The proof is the group law: $\phi_{-t} \circ \phi_t = \phi_0 = \mathrm{id}$ on $M_t$, and similarly $\phi_t \circ \phi_{-t} = \mathrm{id}$ on $M_{-t}$. Smoothness of both directions comes from the smoothness of $\phi$.

**Corollary (orbits partition $M$).** The image of each maximal integral curve — the *orbit* of $p$ under the flow — is either a single point (when $p$ is an equilibrium, $X_p = 0$) or an injectively immersed 1-manifold (when $p$ is regular). Different orbits are disjoint, so $M$ is partitioned into the orbits. This partition is the **foliation by orbits** of the flow, and it is a foliation by 1-dimensional leaves except at the equilibrium set.

**Calibration check.** You should be able to: (a) verify that $\phi_t(x) = x e^t$ on $\mathbb{R}$ is the global flow of $X = x \partial_x$, and check the group law explicitly; (b) explain why a smooth one-parameter family of diffeomorphisms $\phi_t$ with $\phi_0 = \mathrm{id}$ is *not* automatically a flow — the group law is the substantive extra condition; (c) compute the infinitesimal generator of $\phi_t(x) = x + t$ on $\mathbb{R}$ (answer: $X = \partial_x$) and verify it generates $\phi$ via the integral-curve equation.

---

# Unlocked by This

> [!tip] One-Parameter Subgroup of a Lie Group *(from Lie Theory)*
> The flow of a left-invariant vector field on a [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie group]] is right-translation by a one-parameter subgroup. The infinitesimal generator of this flow is the tangent vector at the identity; the assignment $v \mapsto \phi^{v^L}_1(e)$ is the **exponential map** $\exp : \mathfrak{g} \to G$. Left-invariant vector fields are always complete (their flows are defined globally), so this picture is clean.

> [!tip] Hamiltonian Flow *(from Symplectic and Hamiltonian Geometry)*
> On a [[Differential Geometry VIII — Differential Forms|symplectic]] manifold $(M, \omega)$, a smooth function $H : M \to \mathbb{R}$ determines its **Hamiltonian vector field** $X_H$ by $\iota_{X_H} \omega = dH$, and the flow of $X_H$ is the **Hamiltonian flow** — the time-evolution of the mechanical system with Hamiltonian $H$. Hamiltonian flows preserve $\omega$ and preserve $H$ (energy conservation).

> [!tip] Reeb Flow *(from Contact Geometry)*
> On a contact manifold, the **Reeb vector field** is canonically determined by the contact structure, and its flow — the Reeb flow — is the basic object of contact dynamics. The closed orbits of Reeb flows are a central topic, with the Weinstein conjecture being one of the deepest unresolved questions in symplectic topology.

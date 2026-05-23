---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Geodesic"
  - "Def - Riemannian Metric"
  - "Thm - The Contraction Mapping Principle"
tags: [geometry, riemannian-geometry, geodesics, ODE]
---

# Notation

$(M, g)$ a smooth Riemannian (or semi-Riemannian) manifold, $\nabla$ the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|Levi-Civita connection]] of $g$, and $\Gamma^k_{ij}$ its Christoffel symbols in a chart. For $(p, v) \in TM$, $\gamma_{(p, v)}$ denotes the unique maximal geodesic with $\gamma(0) = p, \dot\gamma(0) = v$. The full registry: [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Statement

> **Theorem (Existence and Uniqueness of Geodesics).** Let $(M, g)$ be a smooth Riemannian (or semi-Riemannian) manifold. For every $(p, v) \in TM$, there exists a unique maximal [[Def - Geodesic|geodesic]] $\gamma_{(p, v)} : I_{(p, v)} \to M$ defined on a maximal open interval $I_{(p, v)} \subseteq \mathbb{R}$ containing $0$, with $\gamma_{(p, v)}(0) = p$ and $\dot\gamma_{(p, v)}(0) = v$.
>
> Furthermore, the map $(t, p, v) \mapsto \gamma_{(p, v)}(t)$ is smooth on the open set $\{(t, p, v) \in \mathbb{R} \times TM : t \in I_{(p, v)}\}$, and satisfies the homogeneity property $\gamma_{(p, cv)}(t) = \gamma_{(p, v)}(ct)$ for $c \neq 0$.

> **Corollary (smooth dependence on initial data).** The geodesic flow $\phi : \Omega \subseteq TM \times \mathbb{R} \to TM$, $\phi_t(p, v) = (\gamma_{(p, v)}(t), \dot\gamma_{(p, v)}(t))$, is a smooth flow defined on an open neighbourhood $\Omega$ of $TM \times \{0\}$ in $TM \times \mathbb{R}$.

---

# Motivation

This is the foundational existence theorem of Riemannian geometry. Without it, the notion of "geodesic" would be a definition without content — we would have a second-order ODE on $M$ but no guarantee that it has solutions, let alone smooth solutions depending well on initial data. With it, every Riemannian manifold has, for each point and each initial direction, a unique geodesic — and this unique geodesic is the input to *every* subsequent construction: the [[Def - The Riemannian Exponential Map|exponential map]] (which is just the time-$1$ value of the geodesic), the geodesic flow on $TM$, the variational characterisation via [[Thm - First Variation of Arc Length|length minimisation]], and the global structure theorems via [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]].

The theorem is striking for what it does *not* require. No global hypothesis on $M$ — not compactness, not completeness, not even orientability. No regularity of the metric beyond smoothness (and in fact $C^2$ would suffice). The reason is that the existence theorem is a *local* ODE theorem, and ODE theory is generous: smoothness of the coefficients gives smoothness of the solutions.

The theorem is also striking for what it *gives* beyond mere existence. The homogeneity property $\gamma_{(p, cv)}(t) = \gamma_{(p, v)}(ct)$ — rescaling the initial velocity rescales the parameter — is what makes the exponential map well-defined as a function of $v$ alone (rather than of speed and time separately), and what makes the differential $d(\exp_p)_0 = \mathrm{id}$ come out cleanly. The smoothness in initial data is what makes the exponential map smooth, which is what enables normal coordinates, the Gauss lemma, and the entire local Riemannian theory.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of the theorem is *just* a smooth Riemannian manifold $(M, g)$ — there is no precondition to broaden, beyond the smooth-manifold structure. So "sources" here means: ways in which the *application* of the theorem can be unexpected, recognising hidden geodesic flow in problems that don't openly mention geodesics.

A common source is **a problem about smooth curves on $M$**. Any smooth curve $\gamma$ has a velocity $\dot\gamma$ and a covariant acceleration $\nabla_{\dot\gamma}\dot\gamma$. So any constraint of the form "find a curve with given initial position, initial velocity, and prescribed covariant acceleration zero" is *automatically* a geodesic problem, and existence-and-uniqueness applies. The bridge: a problem mentions "the curve that does not accelerate" or "the curve along which a vector is parallel-transported back to itself" — this is the geodesic ODE in disguise.

A subtler source is **a problem about the orbits of a Killing vector field**. If $X$ is a Killing field on $(M, g)$, its integral curves are *not* in general geodesics — but if $X$ is parallel ($\nabla X = 0$), then the integral curves of $X$ are geodesics, because $\nabla_X X = 0$ trivially. The bridge: any vector field $X$ with $\nabla_X X = 0$ has, as its integral curves, geodesics, and the theorem then gives the existence-and-uniqueness directly. Parallel vector fields are rare (they exist only on flat manifolds, locally), but the principle is useful in symmetric spaces and Lie groups, where one-parameter subgroups of the isometry group can be identified with geodesics.

A third source is **the lifted second-order ODE on $TM$**. A geodesic on $M$ corresponds to an integral curve of the **geodesic vector field** $G$ on $TM$, defined in coordinates by $G_{(q, v)} = v^i \partial_{q^i} - \Gamma^k_{ij}(q) v^i v^j\, \partial_{v^k}$. So the existence-and-uniqueness theorem is *literally* the existence-and-uniqueness theorem for integral curves of $G$ — i.e., for a smooth vector field on the manifold $TM$. The bridge: any problem about integral curves of smooth vector fields can be brought into the geodesic framework, with the inverse direction (constructing $g$ from a given second-order ODE) being the inverse problem of the calculus of variations.

A fourth source is **bridging from Riemannian to Lorentzian**. The same theorem holds in semi-Riemannian signature, including the Lorentzian signature of general relativity. So *every* timelike, null, and spacelike geodesic in a Lorentzian spacetime exists locally and uniquely, given the initial data. This is the source behind GR test-particle analyses: existence-and-uniqueness is the precondition for "the worldline of a free-falling particle is determined by its initial position and velocity", which is the kinematic content of general relativity.

**Targets (Output Amplification)**

The conclusion of the theorem is "unique maximal geodesic exists, smoothly in initial data". The targets are the constructions and theorems that *use* this conclusion.

The most important target combination is **existence and uniqueness + the homogeneity property gives the exponential map**. The conclusion produces $\gamma_{(p, v)}$ for each $(p, v)$. The additional property (homogeneity) lets us evaluate at $t = 1$ and get a function of $v$ alone: $\exp_p(v) := \gamma_{(p, v)}(1)$. This is the definition of the [[Def - The Riemannian Exponential Map|exponential map]], the central object of the entire chapter. Without the existence-and-uniqueness theorem, the exponential map would not exist; without the homogeneity, it would not be well-defined.

A second combination is **existence + smoothness in initial data ⟹ smoothness of $\exp_p$**. The differential $d(\exp_p)_0 = \mathrm{id}$ then follows from the homogeneity, the [[Thm - The Inverse Function Theorem|inverse function theorem]] kicks in to give local diffeomorphism, and the entire [[Def - Normal Coordinates and Geodesic Coordinates|normal-coordinate]] construction unfolds. So the existence theorem, combined with smooth dependence on parameters, is the source of all local Riemannian analytic constructions.

A third combination is **existence + completeness ⟹ Hopf–Rinow**. If we additionally know the manifold is complete (every maximal geodesic exists for all time, $I_{(p,v)} = \mathbb{R}$), then the theorem combines with completeness to produce the [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]] equivalences: metric completeness, Heine–Borel, and existence of minimising geodesics between any two points. So the existence theorem is the local input to the central global theorem.

A fourth combination is **existence + a Killing vector $X$ ⟹ a conservation law for geodesic flow**. The conserved quantity is $g(\dot\gamma, X)$, constant along every geodesic $\gamma$. The theorem produces $\gamma$; the Killing property of $X$ gives the conservation. Together, these reduce the geodesic equation by one order, which is how every explicit geodesic computation on symmetric spaces (sphere, hyperbolic, Schwarzschild, Kerr) is performed.

---

# Why Is It True

**Mechanism summary:** **the geodesic equation $\ddot x^k + \Gamma^k_{ij}\dot x^i \dot x^j = 0$ is a smooth second-order ODE; lifting to first-order on $TM$ via the geodesic vector field, Picard–Lindelöf gives local existence, uniqueness, and smooth dependence on initial data. The homogeneity property comes for free from the structure of the equation (homogeneity of degree two in velocities).**

The proof is, at root, just the existence theorem for ODEs: the [[Thm - The Contraction Mapping Principle|contraction mapping principle]] applied to the Volterra integral form of the geodesic equation. The geodesic equation in a chart is
$$\ddot x^k = -\Gamma^k_{ij}(x)\, \dot x^i\, \dot x^j,$$
a second-order ODE with smooth right-hand side. Lift to a first-order ODE on $TM$ by setting $y = (x, v)$ with $v = \dot x$:
$$\dot y = (\dot x, \dot v) = (v, -\Gamma^k_{ij}(x)\, v^i\, v^j\, \partial_k) =: G(y).$$
This $G$ is the **geodesic vector field** on $TM$, a smooth vector field (since the Christoffel symbols are smooth functions of $x$). The standard ODE existence theorem — local existence, uniqueness, smooth dependence on initial data — applied to this vector field gives all the conclusions of our theorem at once. Maximality of $I_{(p,v)}$ comes from the standard "patch together local solutions" argument, and the open-ness of the domain of the flow is a standard fact about ODEs.

The **homogeneity property** $\gamma_{(p, cv)}(t) = \gamma_{(p, v)}(ct)$ comes from the structure of the equation, not from the ODE existence theorem. The geodesic equation is invariant under the rescaling $t \mapsto t/c$: if $\gamma$ is a geodesic, so is $\tilde\gamma(t) := \gamma(ct)$, because $\dot{\tilde\gamma} = c\dot\gamma$ and $\ddot{\tilde\gamma} = c^2 \ddot\gamma$, while $\Gamma^k_{ij}\dot{\tilde\gamma}^i \dot{\tilde\gamma}^j = c^2 \Gamma^k_{ij}\dot\gamma^i \dot\gamma^j$, so the equation $\ddot{\tilde\gamma}^k + \Gamma^k_{ij}\dot{\tilde\gamma}^i \dot{\tilde\gamma}^j = c^2(\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i \dot\gamma^j) = 0$ is preserved. The reparametrised $\tilde\gamma$ has initial velocity $c\dot\gamma(0) = cv$, so by uniqueness, $\tilde\gamma = \gamma_{(p, cv)}$. Hence $\gamma_{(p, cv)}(t) = \gamma(ct) = \gamma_{(p, v)}(ct)$.

The two pieces — ODE existence and the algebraic homogeneity — together give the full statement.

The reason the existence theorem applies *uniformly* on any Riemannian manifold is that the geodesic equation is *intrinsic*: the Christoffel symbols transform between charts in such a way that the equation $\nabla_{\dot\gamma}\dot\gamma = 0$ has the same meaning everywhere. So we can patch the local existence statements together coherently, producing a maximal solution defined on an open interval. This is the smooth-manifold-machinery analogue of patching local ODE solutions on $\mathbb{R}^n$.

---

# What Makes This Hard

The conceptual difficulty is **recognising the geodesic equation as a smooth ODE on $TM$ rather than a constraint on curves on $M$**. The second-order ODE $\nabla_{\dot\gamma}\dot\gamma = 0$ does not lend itself directly to Picard–Lindelöf, which wants first-order equations. The lifting trick — phase-space variables $(x, v)$ on $TM$ — converts it to a first-order ODE on the higher-dimensional manifold $TM$. Without this trick the theorem is not visibly accessible from ODE theory.

The technical difficulty, once the lifting is done, is **uniformity across charts**: the Christoffel symbols look completely different in different coordinate systems, but the geodesic equation describes the same geometric object. So the local existence in one chart must be coherently extended across coordinate changes, using the chain rule for second derivatives (which is exactly what makes Christoffel symbols transform the way they do). This is more of a bookkeeping issue than a conceptual one, and it is invisible if one works coordinate-freely from the start.

The most common error is to forget the **smoothness in initial data** statement and to think only about pointwise existence. The smooth dependence is essential for downstream applications: it is what makes $\exp_p$ smooth in $v$, and the geodesic flow $\phi_t$ smooth on $TM$, and the comparison theorems applicable.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Write the geodesic equation in coordinates as a second-order ODE for the curve $x(t)$ in $\mathbb{R}^n$ (via a chart). Lift to a first-order ODE on $TM \cong \mathbb{R}^{2n}$ in coordinates. Apply Picard–Lindelöf: smooth vector field on a smooth manifold gives local existence, uniqueness, and smooth dependence on initial data. Extend across coordinate changes; patch maximal local solutions to get global maximal existence on an open interval.

**Subgoal decomposition:**

1. **Write the geodesic equation in chart-coordinate form.** In a chart $(U, x^1, \ldots, x^n)$, $\nabla_{\dot\gamma}\dot\gamma = 0$ becomes $\ddot x^k + \Gamma^k_{ij}(x) \dot x^i \dot x^j = 0$.
   - *Hint:* compute $\nabla_{\dot\gamma} \dot\gamma = \nabla_{\dot x^i \partial_i}(\dot x^j \partial_j) = \dot x^i \nabla_{\partial_i}(\dot x^j \partial_j)$. Apply the connection definition.
   - *Why needed:* This converts the abstract geodesic equation into a concrete ODE we can apply Picard–Lindelöf to.

2. **Lift to a first-order ODE on $TM$.** Set $y = (x, v) \in \mathbb{R}^n \times \mathbb{R}^n$; the equation becomes $\dot y = (v, -\Gamma^k_{ij}(x)v^i v^j)$, with right-hand side a smooth function of $y$.
   - *Hint:* this is just "introduce velocity as a new variable", the standard ODE trick.
   - *Why needed:* Picard–Lindelöf wants first-order ODEs; the lift is the standard conversion.

3. **Apply Picard–Lindelöf in the chart.** Smooth right-hand side ⟹ for any $y_0 \in TM$, a unique smooth solution exists on a maximal open interval, and the solution depends smoothly on $y_0$.
   - *Hint:* this is the standard theorem; see [[Thm - The Contraction Mapping Principle]] for the proof via the Volterra integral form.
   - *Why needed:* Local existence and smoothness in initial data.

4. **Check coordinate-invariance.** Verify that the geodesic equation transforms correctly between charts via the transformation rule for Christoffel symbols, so the solutions agree on overlaps.
   - *Hint:* the Christoffel symbols transform with an inhomogeneous term that exactly cancels the second-derivative chain-rule term when applied to $\dot x^k$.
   - *Why needed:* To patch local solutions into a global one.

5. **Patch local solutions to a global maximal solution.** Use the uniqueness statement (any two local solutions with the same initial data agree on the overlap) and Zorn or a direct construction to get a unique maximal interval.
   - *Hint:* the union of all open intervals containing $0$ on which a solution is defined is open and gives the maximal interval.
   - *Why needed:* Establishes $I_{(p, v)}$ as a well-defined maximal interval.

6. **Verify homogeneity.** Show $\tilde\gamma(t) := \gamma_{(p, v)}(ct)$ satisfies the geodesic equation with initial velocity $cv$, by direct substitution and the homogeneity of degree two of the equation in velocity.
   - *Hint:* $\dot{\tilde\gamma} = c\dot\gamma$, $\ddot{\tilde\gamma} = c^2 \ddot\gamma$, and $\Gamma^k_{ij}\dot{\tilde\gamma}^i \dot{\tilde\gamma}^j = c^2 \Gamma^k_{ij}\dot\gamma^i \dot\gamma^j$, so the equation rescales uniformly by $c^2$.
   - *Why needed:* This is the additional property beyond pure ODE existence, used to define the exponential map.

---

# Lemma Decomposition

> [!note]- Lemma 1: The geodesic equation in a chart is $\ddot x^k + \Gamma^k_{ij}\dot x^i \dot x^j = 0$
> **Statement:** In any chart $(U, x^1, \ldots, x^n)$ on $M$, the equation $\nabla_{\dot\gamma}\dot\gamma = 0$ is equivalent to the system $\ddot x^k + \Gamma^k_{ij}(x(t)) \dot x^i \dot x^j = 0$ for $k = 1, \ldots, n$, where $\Gamma^k_{ij}$ are the Christoffel symbols of $\nabla$ in this chart.
>
> **Hint:** Expand $\dot\gamma = \dot x^i \partial_i$, apply the connection's Leibniz rule and the definition $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$.
>
> **Why needed:** Converts the abstract equation to a concrete system of ODEs.
>
> > [!note]- Full proof
> > In coordinates, $\dot\gamma = \dot x^i(t) \partial_i$. The covariant derivative along $\gamma$ of any vector field along $\gamma$ of the form $W = w^k \partial_k$ is, by the chain rule on coefficients and the definition of the connection on basis vectors,
> > $$\nabla_{\dot\gamma} W = \dot w^k \partial_k + w^k \nabla_{\dot\gamma}\partial_k = \dot w^k \partial_k + w^k \dot x^i \nabla_{\partial_i}\partial_k = \dot w^k \partial_k + w^k \dot x^i \Gamma^l_{ik}\partial_l.$$
> > Setting $W = \dot\gamma$ (so $w^k = \dot x^k$) and renaming dummy indices:
> > $$\nabla_{\dot\gamma}\dot\gamma = \ddot x^k \partial_k + \dot x^k \dot x^i \Gamma^l_{ik}\partial_l = (\ddot x^l + \Gamma^l_{ik}\dot x^i \dot x^k)\partial_l.$$
> > Setting this to zero gives $\ddot x^l + \Gamma^l_{ik}\dot x^i \dot x^k = 0$ for each $l$, as claimed.

> [!note]- Lemma 2: The geodesic vector field on $TM$ is smooth
> **Statement:** In coordinates $(x, v)$ on $TM$ induced by a chart on $M$, the vector field $G_{(x, v)} = v^i \partial_{x^i} - \Gamma^k_{ij}(x) v^i v^j \partial_{v^k}$ is smooth, and the projections of its integral curves to $M$ are exactly the [[Def - Geodesic|geodesics]].
>
> **Hint:** Smoothness is just smoothness of the Christoffel symbols. The integral curves satisfy $\dot x = v, \dot v = -\Gamma^k_{ij}(x)v^i v^j$, which is the geodesic equation written as a first-order system.
>
> **Why needed:** Reduces the second-order geodesic equation to a first-order vector field on $TM$, to which standard ODE existence applies directly.
>
> > [!note]- Full proof
> > Smoothness: the Christoffel symbols $\Gamma^k_{ij}$ are smooth functions of $x$ (since $g$ is smooth), so $G$ has smooth components. (Globally, $G$ is well-defined as a vector field on $TM$ because the Christoffel transformation rule, combined with the transformation of the velocity $v$, makes the right-hand side of $\dot v = -\Gamma^k_{ij}v^i v^j$ transform correctly between charts on $M$.)
> >
> > Integral curves: solving $\dot{(x, v)} = G_{(x, v)}$ means $\dot x = v$ and $\dot v^k = -\Gamma^k_{ij}(x) v^i v^j$. Eliminating $v$ via $v = \dot x$ gives $\ddot x^k = -\Gamma^k_{ij}\dot x^i \dot x^j$ — the geodesic equation. So the projection $x(t) = \pi(\phi_t(x_0, v_0))$ is a geodesic in $M$.

> [!note]- Lemma 3: Picard–Lindelöf applied to the geodesic vector field
> **Statement:** For any $(p, v) \in TM$, there exists a unique maximal integral curve of $G$ through $(p, v)$, defined on a maximal open interval $I \subseteq \mathbb{R}$ containing $0$. The integral curve depends smoothly on $(p, v)$, and the map $(t, p, v) \mapsto \phi_t(p, v)$ is smooth on its domain.
>
> **Hint:** This is just the standard ODE theorem (Picard–Lindelöf with smooth dependence on parameters) applied to a smooth vector field on the manifold $TM$.
>
> **Why needed:** Existence, uniqueness, maximality, and smooth dependence on initial data — the four conclusions of our theorem — are all packaged here.
>
> > [!note]- Full proof
> > Locally in a chart, $G$ is a smooth vector field on an open subset of $\mathbb{R}^{2n}$. Picard–Lindelöf (e.g., via the [[Thm - The Contraction Mapping Principle|contraction mapping principle]] on the Volterra integral $\phi(t) = \phi_0 + \int_0^t G(\phi(s))\, ds$ in a small ball) gives a unique local solution on some $(-\varepsilon, \varepsilon)$, smoothly depending on $\phi_0$.
> >
> > Smoothness of $\phi(t)$ in $(t, \phi_0)$ follows from the standard "smooth dependence on parameters" extension of Picard–Lindelöf, using the contraction's smoothness in parameters.
> >
> > Maximality: define $I_{(p, v)} := \bigcup\{(-\delta_1, \delta_2) : $ unique solution exists on this interval with initial condition $(p, v)\}$. This is open, contains $0$, and by uniqueness the solutions on overlapping intervals coincide, so we get a single solution defined on $I_{(p, v)}$.

> [!note]- Lemma 4: Homogeneity $\gamma_{(p, cv)}(t) = \gamma_{(p, v)}(ct)$
> **Statement:** For any $(p, v) \in TM$ and $c \neq 0$, $\gamma_{(p, cv)}(t) = \gamma_{(p, v)}(ct)$, with corresponding maximal intervals related by $I_{(p, cv)} = c^{-1} I_{(p, v)}$.
>
> **Hint:** Define $\tilde\gamma(t) := \gamma_{(p, v)}(ct)$, verify it satisfies the geodesic equation with initial velocity $cv$, then invoke uniqueness.
>
> **Why needed:** This is the property that makes $\exp_p(v) := \gamma_{(p,v)}(1)$ a well-defined function of $v$ alone, equivalently that the geodesic flow has the appropriate scaling.
>
> > [!note]- Full proof
> > Define $\tilde\gamma(t) := \gamma_{(p, v)}(ct)$. Then $\tilde\gamma(0) = \gamma_{(p, v)}(0) = p$ and $\dot{\tilde\gamma}(0) = c \dot\gamma_{(p, v)}(0) = cv$. Compute the covariant acceleration:
> > $$\nabla_{\dot{\tilde\gamma}}\dot{\tilde\gamma} = \nabla_{c\dot\gamma}(c\dot\gamma) = c^2 \nabla_{\dot\gamma}\dot\gamma = 0.$$
> > So $\tilde\gamma$ is a geodesic with initial data $(p, cv)$. By uniqueness, $\tilde\gamma = \gamma_{(p, cv)}$, i.e. $\gamma_{(p, cv)}(t) = \gamma_{(p, v)}(ct)$. The interval relation follows by tracing where each curve is defined.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For every $(p, v) \in TM$, there exists a unique maximal geodesic $\gamma_{(p, v)} : I_{(p, v)} \to M$ with $\gamma(0) = p, \dot\gamma(0) = v$, defined on a maximal open interval $I_{(p, v)} \subseteq \mathbb{R}$ containing $0$. The geodesic depends smoothly on initial data and satisfies the homogeneity property $\gamma_{(p, cv)}(t) = \gamma_{(p, v)}(ct)$ for $c \neq 0$.
>
> *Proof.* By Lemma 1, in any chart the geodesic equation $\nabla_{\dot\gamma}\dot\gamma = 0$ is the system $\ddot x^k + \Gamma^k_{ij}\dot x^i \dot x^j = 0$. By Lemma 2, this lifts to the first-order ODE $\dot y = G(y)$ on $TM$, where $G$ is the smooth geodesic vector field.
>
> By Lemma 3 (Picard–Lindelöf applied to the smooth vector field $G$ on the smooth manifold $TM$), through each $(p, v) \in TM$ there is a unique maximal integral curve $\phi(t) = (\gamma(t), \dot\gamma(t))$ defined on a maximal open interval $I \ni 0$, smoothly depending on $(p, v)$. The projection $\gamma(t) = \pi(\phi(t))$ is the desired geodesic, smooth in $(t, p, v)$ on the open set $\{(t, p, v) : t \in I_{(p, v)}\}$.
>
> By Lemma 4, the homogeneity property holds.
>
> The smoothness of the flow $\phi : \Omega \subseteq TM \times \mathbb{R} \to TM$ on its open domain $\Omega$ is the standard openness-and-smoothness conclusion of ODE theory. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Number theory: continued fractions and geodesics on the modular surface.** The modular surface $\mathbb{H}^2 / \mathrm{PSL}(2, \mathbb{Z})$ is a Riemannian orbifold, and geodesic flow on it has a remarkable coding by continued-fraction expansions of real numbers — the **Artin coding**. The closed geodesics correspond to periodic continued fractions (i.e., quadratic irrationals), and the geodesic length spectrum is related to the regulators of orders in real quadratic fields. The existence theorem produces all these geodesics; the dynamical and number-theoretic content comes from the specific geometry.

**Classical mechanics: Liouville integrability of the Euler top.** The Euler top is the geodesic flow of a left-invariant Riemannian metric on $\mathrm{SO}(3) \cong \mathbb{RP}^3$. The metric is generally not bi-invariant (it depends on the moments of inertia $I_1, I_2, I_3$), so geodesics are *not* one-parameter [[Def - Subgroup|subgroups]]. But the system is integrable — the conserved quantities are the components of angular momentum in the body frame, which Poisson-commute with the energy. Geodesic flow on $\mathrm{SO}(3)$ with a left-invariant metric is the classical case in symplectic mechanics.

**General relativity: Schwarzschild geodesics.** The existence theorem in Lorentzian signature gives unique timelike, null, and spacelike geodesics in the Schwarzschild spacetime starting from any initial event with any initial 4-velocity. The classical tests of GR — perihelion precession, light bending, the Shapiro delay — are all calculations of specific Schwarzschild geodesics. The theorem guarantees these exist and depend smoothly on the initial conditions, which is the precondition for "linearise around the Schwarzschild orbits".

**Quantum mechanics: semiclassical asymptotics.** In the semiclassical limit, solutions to the Schrödinger equation on a Riemannian manifold are concentrated near geodesic flow on the cotangent bundle (Egorov's theorem). The existence theorem for geodesics produces the "skeleton" along which quantum wave packets propagate; the entire machinery of WKB approximation, semiclassical limits, and quantum chaos depends on the smoothness of this skeleton, which is the smooth-dependence conclusion of our theorem.

---

# Bridges

- **[[Thm - The Contraction Mapping Principle|The Contraction Mapping Principle]]** — the proof's engine. The Volterra integral form of the geodesic equation, $\phi(t) = \phi_0 + \int_0^t G(\phi(s))\, ds$, becomes a fixed-point equation $\phi = T(\phi)$ where $T$ is a contraction on a small ball in the Banach space of continuous curves. The contraction's unique fixed point is the unique geodesic. So the existence theorem is, at its mathematical core, the contraction principle — a striking compression of differential geometry into functional analysis.

- **[[Def - The Riemannian Exponential Map|The Riemannian Exponential Map]]** — the direct downstream consumer. $\exp_p(v) := \gamma_{(p, v)}(1)$ is well-defined precisely because the existence theorem guarantees $\gamma_{(p, v)}$ exists at least to time $1$ when $v$ is in the appropriate star-shaped neighbourhood. The smooth-dependence statement makes $\exp_p$ smooth, the homogeneity makes $d(\exp_p)_0 = \mathrm{id}$, and from there the [[Thm - The Inverse Function Theorem|inverse function theorem]] gives the local-diffeomorphism property.

- **[[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]]** — the global upgrade. The existence theorem gives geodesics on a maximal interval $I_{(p, v)}$, which may be bounded. The Hopf–Rinow theorem characterises when $I_{(p, v)} = \mathbb{R}$ for all $(p, v)$ — when the manifold is *geodesically complete* — in terms of metric-space completeness and the Heine–Borel property. So existence (local) plus completeness (global hypothesis) gives the full strength of "geodesics through every initial data exist for all time".

- **The geodesic flow as a Hamiltonian flow** — the symplectic upgrade. The geodesic vector field $G$ on $TM$ is, after Legendre transform to $T^*M$, the Hamiltonian vector field of the kinetic-energy Hamiltonian $H = \tfrac12 g^{ij}p_i p_j$. So the existence theorem for geodesics is *exactly* the existence theorem for the flow of this specific Hamiltonian; see [[Def - Hamiltonian Flow of the Kinetic Energy]] and [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

---

# Unlocked by This

> [!tip] The Exponential Map and Normal Coordinates *(from Riemannian Geometry)*
> The existence theorem is what lets us define $\exp_p(v) = \gamma_{(p, v)}(1)$ at all — without it, the exponential map has no content. Once it exists, the local diffeomorphism property gives [[Def - Normal Coordinates and Geodesic Coordinates|normal coordinates]], and from there the entire local Riemannian-geometry theory unfolds.

> [!tip] **The Geodesic Flow on Unit Cotangent Bundle as an Ergodic Dynamical System** *(from Dynamical Systems)*
> The geodesic flow $\phi_t$ on the unit tangent bundle $SM$ of a compact Riemannian manifold is a measure-preserving flow (Liouville measure). When sectional curvature is negative, it is **Anosov** (uniformly hyperbolic), hence ergodic, mixing, and admits the entire arsenal of hyperbolic dynamics: stable/unstable foliations, exponential decay of correlations, SRB measures, the Margulis lattice-point counting. The existence theorem is the input that produces this flow in the first place.

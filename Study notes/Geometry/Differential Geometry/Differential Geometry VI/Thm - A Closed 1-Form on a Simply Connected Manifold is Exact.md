---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Covector Field and Differential 1-Form"
  - "Def - The Differential of a Function as a 1-Form"
  - "Def - Line Integral of a 1-Form"
  - "Def - Connected Space"
  - "Def - Path-Connected Space"
tags: [geometry, differential-geometry, closed-exact, cohomology]
---

# Notation

$M$ is a smooth manifold, **connected** and **simply connected** (every continuous loop is contractible to a point). $\omega \in \Omega^1(M)$ is a smooth 1-form on $M$. The 1-form is **closed** if $d\omega = 0$ in $\Omega^2(M)$, and **exact** if $\omega = df$ for some $f \in C^\infty(M)$. For a curve $\gamma : [a, b] \to M$, the line integral is $\int_\gamma \omega$ ([[Def - Line Integral of a 1-Form]]).

---

# Statement

> **Theorem (Closed implies exact on simply connected manifolds).** Let $M$ be a connected, simply connected smooth manifold. If $\omega \in \Omega^1(M)$ is a **closed** 1-form ($d\omega = 0$), then $\omega$ is **exact**: there exists $f \in C^\infty(M)$ with $\omega = df$. The function $f$ is unique up to an additive constant.
>
> **Equivalent formulation.** On a connected, simply connected smooth manifold, every smooth 1-form satisfying $d\omega = 0$ has a globally defined "potential function" $f$ such that $df = \omega$.

In the language of de Rham cohomology, this says $H^1_{dR}(M) = 0$ for any simply connected smooth manifold.

---

# Motivation

This theorem is the **first-degree de Rham vanishing theorem**: it gives a complete answer to "when is a closed 1-form exact?" — namely, when the manifold's fundamental [[Def - Group|group]] $\pi_1(M)$ is trivial. The theorem makes the obstruction to exactness explicit and topological, providing the first concrete instance of the bridge between differential geometry (the closed-exact distinction for 1-forms) and topology (the simple-connectivity of $M$).

The motivation is direct. Exact 1-forms automatically satisfy $d\omega = d^2 f = 0$ (since $d^2 = 0$, which is the well-defined cancellation $d \circ d = 0$). So "exact implies closed". The converse — "closed implies exact" — is the substantive content, and the theorem says it holds when the topology of $M$ is trivial.

The mechanism: an exact 1-form $\omega = df$ has the property that $\int_\gamma \omega = f(\gamma(b)) - f(\gamma(a))$ depends only on endpoints. So $\int_\gamma \omega$ around any closed loop is zero, by the fundamental theorem. Conversely, if every closed-loop integral of $\omega$ vanishes, one can define a potential function $f(p) := \int_{p_0}^{p} \omega$ along any path from a basepoint $p_0$ to $p$, and the loop-integral hypothesis makes this well-defined.

The hypothesis "closed" plus "simply connected" combine to give the loop-integral vanishing: $\omega$ closed plus $\gamma$ a loop in a simply connected manifold means $\gamma$ is the boundary of a smooth surface $S$, and Stokes's theorem gives $\int_\gamma \omega = \int_S d\omega = \int_S 0 = 0$. So closed forms on simply connected manifolds are conservative (path-independent integrals), hence exact.

The deeper content is that the theorem is **sharp**: on non-simply-connected manifolds, closed 1-forms that are not exact exist, and they detect the failure of simple connectivity. The angle form $d\theta$ on $S^1$ and the winding form $(x dy - y dx)/(x^2 + y^2)$ on $\mathbb{R}^2 \setminus \{0\}$ are the canonical examples. The cohomology $H^1_{dR}(M)$ measures exactly this gap, and it is a topological invariant of $M$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypotheses are "$M$ smooth, connected, simply connected; $\omega$ smooth and closed". Each hypothesis comes from a different context.

The most common source of **closedness** is **$\omega = df$ for some explicit function $f$** — automatically closed, so the converse problem of "find $f$" is trivial. The harder source is **$\omega$ given by an abstract construction with $d\omega = 0$ verifiable by computation** — for instance, $\omega = \omega_i(x) dx^i$ with $\partial_j \omega_i = \partial_i \omega_j$ (symmetry of partial derivatives, which is equivalent to $d\omega = 0$ in coordinates). This is the case in physics where conservative force fields are characterized by vanishing curl.

The most common source of **simple connectivity** is **a star-shaped (or contractible) domain**. Convex open subsets of $\mathbb{R}^n$, balls in $\mathbb{R}^n$, half-spaces, products of contractible spaces — all are contractible, hence simply connected. The Poincaré lemma (which is the theorem on star-shaped domains, special case of contractible manifolds) is the textbook foundation.

A second source of simple connectivity is **a sphere $S^n$ for $n \geq 2$**. Spheres of dimension $\geq 2$ are simply connected (every loop on $S^n$ contracts), so closed 1-forms on $S^n$ are exact for $n \geq 2$. (Note: $S^1$ is *not* simply connected, and indeed $d\theta$ is closed but not exact.)

A third source is **a universal cover**. Every connected manifold has a universal covering manifold, which is simply connected; pulling back a closed 1-form on $M$ to its universal cover $\tilde M$ gives a closed 1-form on $\tilde M$, which is exact by the theorem. So the structure of closed 1-forms on $M$ is encoded in functions on $\tilde M$ with appropriate transformation properties under deck transformations.

**Targets (Output Amplification)**

The conclusion is "exists $f$ with $\omega = df$". This translates into structural and computational results.

The first combination is **theorem plus a curve from $p_0$ to $p$ gives the explicit potential**. Once existence of $f$ is known, one computes $f$ as $f(p) = \int_{p_0}^p \omega$ for any choice of path; the path-independence (by closedness plus simply connectedness) makes this well-defined. This gives an explicit formula for $f$.

A second combination is **theorem plus the de Rham complex gives $H^1_{dR}(M) = 0$ on simply connected manifolds**. The first de Rham cohomology is closed-modulo-exact, and the theorem says closed = exact, so $H^1_{dR} = 0$. Combined with the de Rham theorem, this gives $H^1(M; \mathbb{R}) = 0$ for any simply connected smooth manifold — a topological statement proved via differential forms.

A third combination is **theorem plus the Stokes's theorem gives "loop integrals vanish on simply connected manifolds"**. The proof of the theorem uses Stokes's theorem, but the conclusion in the form "loops have zero integral" is itself a useful statement: for closed $\omega$ and any loop $\gamma$ in a simply connected $M$, $\int_\gamma \omega = 0$. This is the manifold-native version of "every closed contour integral vanishes for a holomorphic function on a simply connected domain" (which is Cauchy's theorem in complex analysis).

A fourth combination is **theorem plus failure of simple connectivity gives nontrivial $H^1_{dR}$**. When $M$ is not simply connected, the theorem fails: $H^1_{dR}(M) \neq 0$ in general. The cohomology classes are detected by integrating closed forms around generators of $\pi_1(M)$; this is the *period* of the form, and the period map $H^1_{dR}(M) \to \mathrm{Hom}(\pi_1(M), \mathbb{R})$ is the bridge between de Rham theory and the fundamental group.

---

# Why Is It True

The intuition is direct: **on a simply connected manifold, every loop contracts, so by Stokes's theorem the loop integral of a closed 1-form vanishes; the vanishing of loop integrals means the path integral $\int_{p_0}^p \omega$ is path-independent, defining the potential $f$**.

**The one-line mechanism summary: closedness ensures $\int_\gamma \omega = 0$ on contractible loops via Stokes, simple connectivity ensures every loop is contractible, and path-independence of the integral defines the potential $f$.**

The construction has three stages.

**Stage 1: define the potential.** Fix a basepoint $p_0 \in M$ (use connectedness of $M$). For each $p \in M$, choose a smooth path $\gamma_p : [0, 1] \to M$ from $p_0$ to $p$, and define $f(p) := \int_{\gamma_p} \omega$. This requires the path-integral to be path-independent — the next stage handles this.

**Stage 2: path-independence.** Given two paths $\gamma_1, \gamma_2$ from $p_0$ to $p$, the concatenation $\gamma_1 * \gamma_2^{-1}$ is a loop at $p_0$. By simple connectivity, this loop is contractible — i.e., it bounds a smooth surface $S$ (technically: the loop is homotopic to a constant, which gives a continuous map $D^2 \to M$ extending the loop; smoothness can be arranged by approximation). By closedness, $d\omega = 0$, so Stokes's theorem gives $\int_{\gamma_1 * \gamma_2^{-1}} \omega = \int_S d\omega = 0$. By additivity of the line integral, $\int_{\gamma_1} \omega = \int_{\gamma_2} \omega$. So $f(p)$ is well-defined.

**Stage 3: $df = \omega$.** Verify that the constructed $f$ has differential $\omega$. At any point $p \in M$, choose a coordinate chart and a "small" path from $p$ to $p + \epsilon v$ (in the chart). The line integral along this path is approximately $\omega_p(v) \epsilon$ to first order in $\epsilon$, by the fundamental computation of the line integral. So $f(p + \epsilon v) - f(p) \approx \omega_p(v) \epsilon$, which means $df_p(v) = \omega_p(v)$. Since this holds for every $v$, $df_p = \omega_p$, and the equality of 1-forms follows pointwise.

The smoothness of $f$ follows from the smoothness of $\omega$ and the locally-line-integral computation.

So the theorem's logic is: closed $\omega$ + simply connected $M$ + Stokes ⟹ path-independent line integral ⟹ well-defined potential $f$ ⟹ $df = \omega$.

---

# What Makes This Hard

The substantive technical step is the **smoothness of the [[Def - Homotopy|homotopy]] connecting any loop to a constant**, used in the application of Stokes's theorem. Simple connectivity is by definition a *topological* condition (continuous homotopy), but Stokes's theorem requires *smooth* surfaces. The bridge is the smooth-approximation theorem: every continuous map from a manifold-with-boundary to a smooth manifold is homotopic to a smooth one, with the boundary behavior preserved. This is a non-trivial result in differential topology.

A second source of difficulty is the **proof that $df = \omega$ pointwise**. The natural argument is to compute $f(p + \epsilon v) - f(p)$ to first order in $\epsilon$, but the careful version requires a coordinate chart, a smooth path, and Taylor expansion of the integrand — bookkeeping that beginners often skip.

A common error is to **forget the simple-connectivity hypothesis**. Without it, the path-independence fails: on $\mathbb{R}^2 \setminus \{0\}$, two paths from $p_0$ to $p$ that wind differently around the origin give different line integrals of a typical closed-but-not-exact 1-form. The hypothesis is essential.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use connectedness of $M$ to fix a basepoint $p_0$ and define $f(p) := \int_{p_0}^p \omega$ along any path. Use simple connectivity plus Stokes's theorem to show the integral is path-independent (so $f$ is well-defined). Use a local-chart Taylor argument to show $df = \omega$.

**Subgoal decomposition:**

1. **Fix a basepoint and define candidate $f$.** Choose $p_0 \in M$ (by connectedness, any point works). For each $p \in M$, choose a smooth path $\gamma_p : [0, 1] \to M$ with $\gamma_p(0) = p_0, \gamma_p(1) = p$, and define $f(p) := \int_{\gamma_p} \omega$. (Existence of smooth paths uses smooth path-connectedness, which follows from connectedness of a smooth manifold.)
   - *Hint:* Connected smooth manifolds are smoothly path-connected.
   - *Why needed:* Provides a candidate for the potential function.

2. **Show $f$ is independent of the path choice.** For two paths $\gamma_1, \gamma_2$ from $p_0$ to $p$, the concatenation $\gamma = \gamma_1 * \gamma_2^{-1}$ is a loop at $p_0$. By simple connectivity, $\gamma$ bounds a smooth surface $S$ (smooth homotopy of the loop to a point). By closedness $d\omega = 0$ and Stokes: $\int_\gamma \omega = \int_S d\omega = 0$, so $\int_{\gamma_1} \omega = \int_{\gamma_2} \omega$.
   - *Hint:* Simple connectivity gives a smooth disk; Stokes gives the integral identity.
   - *Why needed:* This makes $f(p)$ well-defined.

3. **Show $f$ is smooth.** In any chart $(U, x^i)$ around $p$, use the line-integral formula $f(q) = f(p) + \int_p^q \omega = f(p) + \int_0^1 \omega_i(\gamma(t)) \dot\gamma^i(t) dt$ for a smooth path from $p$ to $q$. As $q$ varies smoothly in $p$, this integral is smooth in $q$.
   - *Hint:* Smoothness of $\omega$ and smoothness of the path.
   - *Why needed:* Required to conclude $f \in C^\infty(M)$.

4. **Show $df = \omega$.** At any $p$ and any $v \in T_pM$, the derivative of $f$ in direction $v$ at $p$ is $\omega_p(v)$ — directly from the integral construction and the fundamental theorem of calculus.
   - *Hint:* Pick a curve $\gamma(t)$ with $\gamma(0) = p, \gamma'(0) = v$; then $f(\gamma(t)) - f(p) = \int_0^t \omega(\gamma'(s)) ds$ by additivity, and differentiating at $t = 0$ gives $df_p(v) = \omega(\gamma'(0)) = \omega_p(v)$.
   - *Why needed:* This is the conclusion.

5. **Uniqueness up to constant.** If $df_1 = df_2 = \omega$, then $d(f_1 - f_2) = 0$; on a connected $M$, this forces $f_1 - f_2$ to be constant.
   - *Hint:* $d = 0$ means locally constant; connectedness extends to global.
   - *Why needed:* Completes the existence-and-uniqueness statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: Smooth path-connectedness of connected smooth manifolds
> **Statement:** Every connected smooth manifold $M$ is *smoothly* path-connected — i.e., any two points are joined by a piecewise smooth curve.
>
> **Hint:** Topological path-connectedness follows from connectedness (manifolds are locally path-connected); smooth approximation upgrades to piecewise smooth.
>
> **Why needed:** Required to choose smooth paths in the construction of $f$.
>
> > [!note]- Full proof
> > A connected manifold is path-connected (manifolds are locally path-connected, and connected + locally path-connected implies path-connected). Every continuous path can be approximated by a smooth path agreeing at the endpoints, using a partition of unity and smooth bumps to "smooth out" any non-smooth points. So smooth path-connectedness holds.

> [!note]- Lemma 2: Simple-connectivity implies loops bound smooth disks
> **Statement:** In a simply connected smooth manifold $M$, every smooth loop $\gamma$ at $p_0$ is the boundary of a smooth map $S : D^2 \to M$, where $D^2$ is the closed unit disk.
>
> **Hint:** Simple connectivity gives a continuous nullhomotopy of $\gamma$; smooth approximation upgrades to smooth.
>
> **Why needed:** Required for the Stokes argument in path-independence.
>
> > [!note]- Full proof
> > Simple connectivity by definition: every continuous loop $\gamma : S^1 \to M$ extends to a continuous $\tilde S : D^2 \to M$ with $\tilde S|_{S^1} = \gamma$. The Whitney approximation theorem says: every continuous map between smooth manifolds is homotopic to a smooth one, and the homotopy can be made constant on any subset where the map is already smooth. Applying with $\gamma$ smooth gives a smooth $S : D^2 \to M$ with $S|_{S^1} = \gamma$ (relative homotopy fixing the boundary).

> [!note]- Lemma 3: Stokes's theorem for 1-forms on smooth disks
> **Statement:** For a smooth map $S : D^2 \to M$ and a smooth 1-form $\omega$ on $M$, $\int_{\partial S} S^*\omega = \int_{D^2} S^*(d\omega)$.
>
> **Hint:** This is Stokes's theorem for the 2-manifold $D^2$ with boundary $S^1$.
>
> **Why needed:** Converts the loop integral to a disk integral, showing the loop integral of a closed form is zero.
>
> > [!note]- Full proof
> > Stokes's theorem on a smooth manifold-with-boundary states $\int_S d\omega = \int_{\partial S} \omega$ for $\omega$ a compactly-supported $(k-1)$-form and $S$ a smooth $k$-manifold-with-boundary. Applying with $k = 2$ and $S = D^2$ (with its standard orientation), and using $\omega$ restricted to the image of $S$ (which is compact for a closed $D^2$): the line integral around $\partial D^2 = S^1$ pulled back via $S$ equals the surface integral of $d\omega$ pulled back via $S$. Pull-back commutes with the line integral and exterior derivative, so the identity in the form $\int_{\partial S}^{} S^*\omega = \int_{D^2} S^*(d\omega)$ holds.

> [!note]- Lemma 4: Loop integral of closed form vanishes on simply connected $M$
> **Statement:** For $M$ simply connected, $\omega \in \Omega^1(M)$ closed, and $\gamma$ a smooth loop in $M$, $\int_\gamma \omega = 0$.
>
> **Hint:** Apply Lemma 2 to get a smooth disk bounded by $\gamma$, then Lemma 3 to convert to a disk integral, which vanishes by closedness.
>
> **Why needed:** Reduces path-independence to a property of $\omega$ and $M$.
>
> > [!note]- Full proof
> > By Lemma 2, $\gamma = \partial S$ for some smooth $S : D^2 \to M$. By Lemma 3, $\int_{\gamma} \omega = \int_{\partial S} \omega = \int_{D^2} S^*(d\omega) = 0$ (using $d\omega = 0$ and pullback commutativity, so $S^*(d\omega) = d(S^*\omega)$, but more directly, $S^*$ of zero is zero).

> [!note]- Lemma 5: Path-independence of the integral
> **Statement:** For $M$ simply connected, $\omega$ closed, and two smooth paths $\gamma_1, \gamma_2$ from $p_0$ to $p$, $\int_{\gamma_1} \omega = \int_{\gamma_2} \omega$.
>
> **Hint:** Concatenate $\gamma_1$ and $\gamma_2^{-1}$ to form a loop; apply Lemma 4.
>
> **Why needed:** Makes the candidate $f(p)$ well-defined.
>
> > [!note]- Full proof
> > Consider the concatenation $\gamma := \gamma_1 * \gamma_2^{-1}$, a loop at $p_0$. By Lemma 4, $\int_\gamma \omega = 0$. By additivity of the line integral, $\int_\gamma \omega = \int_{\gamma_1} \omega + \int_{\gamma_2^{-1}} \omega = \int_{\gamma_1} \omega - \int_{\gamma_2} \omega$. So $\int_{\gamma_1} \omega = \int_{\gamma_2} \omega$.

> [!note]- Lemma 6: $df = \omega$
> **Statement:** For the function $f$ defined by $f(p) := \int_{p_0}^p \omega$, $df = \omega$.
>
> **Hint:** Pick a smooth curve $\gamma$ with $\gamma(0) = p, \gamma'(0) = v$; compute $df_p(v) = (d/dt)|_{t=0} f(\gamma(t)) = \omega(\gamma'(0)) = \omega_p(v)$.
>
> **Why needed:** This is the conclusion of the theorem.
>
> > [!note]- Full proof
> > For $v \in T_pM$ and a smooth curve $\gamma : (-\epsilon, \epsilon) \to M$ with $\gamma(0) = p$ and $\gamma'(0) = v$, by additivity, $f(\gamma(t)) = f(p) + \int_p^{\gamma(t)} \omega = f(p) + \int_0^t \omega_{\gamma(s)}(\gamma'(s)) ds$. Differentiating at $t = 0$: $(d/dt)|_{t=0} f(\gamma(t)) = \omega_p(\gamma'(0)) = \omega_p(v)$. The left-hand side is $df_p(v)$ by definition of the differential. So $df_p(v) = \omega_p(v)$ for every $v$, hence $df_p = \omega_p$ for every $p$, and $df = \omega$ as 1-forms.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Setup.** $M$ connected, simply connected, smooth manifold. $\omega \in \Omega^1(M)$ smooth with $d\omega = 0$. We construct $f \in C^\infty(M)$ with $df = \omega$.
>
> **Step 1 — Choose a basepoint.** Fix $p_0 \in M$. By Lemma 1, $M$ is smoothly path-connected, so for every $p \in M$ there exists a smooth path $\gamma_p : [0, 1] \to M$ with $\gamma_p(0) = p_0, \gamma_p(1) = p$.
>
> **Step 2 — Define the candidate $f$.** Set $f(p) := \int_{\gamma_p} \omega$.
>
> **Step 3 — $f$ is path-independent.** By Lemma 5, the integral depends only on the endpoints, not on the path. So $f(p)$ is well-defined (does not depend on the choice of $\gamma_p$).
>
> **Step 4 — $f$ is smooth.** In a chart $(U, x^i)$ around any $p$, for $q \in U$ near $p$, choose a path from $p_0$ to $q$ that goes through $p$ and then along a smooth path from $p$ to $q$ in the chart. By additivity of line integrals, $f(q) = f(p) + \int_p^q \omega$, with the second integral computed in coordinates as a smooth function of $q$ (since $\omega_i$ are smooth and the path in the chart is smooth). So $f$ is smooth on $U$, hence smooth on $M$.
>
> **Step 5 — $df = \omega$.** By Lemma 6, $df_p(v) = \omega_p(v)$ for every $p \in M$ and $v \in T_pM$. So $df = \omega$ as smooth 1-forms.
>
> **Step 6 — Uniqueness.** Suppose $df_1 = df_2 = \omega$. Then $d(f_1 - f_2) = 0$, so $f_1 - f_2$ is locally constant. By connectedness of $M$, $f_1 - f_2$ is globally constant.
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Complex analysis: Cauchy's theorem on simply connected domains.** For a holomorphic function $f : U \to \mathbb{C}$ on a simply connected open $U \subseteq \mathbb{C}$, the contour integral $\oint_\gamma f(z) dz = 0$ for every closed contour $\gamma \subseteq U$. This is Cauchy's theorem, and it has the same logical structure as the present theorem: the 1-form $f(z) dz$ is closed (because $f$ is holomorphic implies $\partial f/\partial \bar z = 0$, which translates to $d(f dz) = 0$), simple connectivity gives bounding disks, Stokes (or its complex-analytic equivalent) gives loop-integral vanishing.

**Classical electromagnetism: existence of potentials.** A static magnetic field $\mathbf{B}$ on simply connected $\mathbb{R}^3$ has $\nabla \cdot \mathbf{B} = 0$ (Maxwell), which in form language is $dF = 0$ for the magnetic 2-form $F$. Wait, this is a 2-form theorem (Poincaré lemma for higher degrees). The 1-form version: a conservative force field on simply connected $\mathbb{R}^3$ has $\nabla \times \mathbf{F} = 0$, which is $d\omega = 0$ for the force 1-form $\omega$. The theorem says $\omega = -dU$ for a potential energy $U$ — this is the existence of energy potentials for conservative forces.

**Algebraic topology: vanishing of $H^1_{dR}$ for simply connected spaces.** The theorem gives $H^1_{dR}(M) = 0$ for any simply connected smooth manifold. Combined with the de Rham theorem, this proves $H^1(M; \mathbb{R}) = 0$ for any simply connected manifold — a topological statement proved via differential forms. The same logic applied to higher degrees gives the Poincaré lemma and the general vanishing $H^k_{dR}(M) = 0$ for $k > 0$ when $M$ is contractible.

**Thermodynamics: existence of state functions.** In thermodynamics, an exact 1-form $\omega = dF$ for some function $F$ represents a *state function* — the integral of $\omega$ from state $A$ to state $B$ depends only on the endpoints, not on the path through state space. The theorem applied to thermodynamic state space (assumed simply connected) characterizes when "the integral of an infinitesimal change is path-independent" — equivalently, when there exists a state function whose differential is the given 1-form. Closed 1-forms that are not exact would correspond to "non-state-function" quantities like heat $Q$ and work $W$ separately, with $Q + W = U$ a state function.

---

# Bridges

- **Stokes's theorem** *(from Differential Geometry IX)* — The proof of this theorem uses Stokes in the form $\int_S d\omega = \int_{\partial S} \omega$ for 2-disks $S$ bounded by smooth loops. The bridge is direct: closed forms ($d\omega = 0$) have vanishing $\int_S d\omega$ for every disk, hence vanishing loop integrals.

- **[[Def - Path-Connected Space]] and the fundamental group** *(from topology)* — Simple connectivity is the vanishing of the fundamental group: $\pi_1(M) = 0$. The theorem says $\pi_1(M) = 0$ implies $H^1_{dR}(M) = 0$. More generally, there is a map $H^1_{dR}(M) \to \mathrm{Hom}(\pi_1(M), \mathbb{R})$ given by integrating closed forms around loops, and the kernel of this map is the exact forms. So $H^1_{dR}$ measures the abelianized real-valued fundamental group.

- **de Rham cohomology** *(from Differential Geometry X)* — The theorem says $H^1_{dR}(M) = 0$ for simply connected $M$. The general de Rham theorem then identifies $H^1_{dR}(M)$ with the singular cohomology $H^1(M; \mathbb{R})$, which by the universal coefficient theorem equals $\mathrm{Hom}(\pi_1(M), \mathbb{R})$ for connected $M$. So the theorem and the de Rham theorem together give a differential-geometric proof that $H^1(M; \mathbb{R}) = 0$ for simply connected $M$.

- **The Poincaré lemma** *(generalization)* — The Poincaré lemma is the higher-degree version: on a contractible smooth manifold $M$ (e.g., a star-shaped open subset of $\mathbb{R}^n$), every closed $k$-form is exact for $k \geq 1$. The case $k = 1$ on contractible $M$ is a special case of the present theorem (contractible $\implies$ simply connected $\implies$ closed 1-form is exact). The full Poincaré lemma extends this to all degrees and is proved by an explicit cochain-homotopy construction.

---

# Unlocked by This

> [!tip] de Rham Cohomology *(from Differential Geometry X)*
> The first de Rham cohomology $H^1_{dR}(M) = \{d\omega = 0\}/\{exact\}$ measures the gap between closed and exact 1-forms. The theorem says $H^1_{dR}(M) = 0$ for simply connected $M$; for general $M$, $H^1_{dR}(M)$ detects the "1-dimensional holes" — topologically, it is dual to $\pi_1(M)^{ab}$ tensored with $\mathbb{R}$. The full de Rham complex $\Omega^0 \to \Omega^1 \to \Omega^2 \to \cdots$ generalizes this, and de Rham cohomology is a contravariant functor from smooth manifolds to graded vector spaces.

> [!tip] The de Rham Theorem *(from Algebraic Topology)*
> The **de Rham theorem** identifies $H^k_{dR}(M)$ with the singular cohomology $H^k(M; \mathbb{R})$ — a purely topological invariant. So differential forms on $M$ "know" the topology of $M$. The case $k = 1$ is essentially the present theorem combined with the universal coefficient theorem in topology.

> [!tip] Periods and the Period Map *(from Hodge Theory)*
> When $H^1_{dR}(M) \neq 0$, the cohomology classes are detected by **periods**: integrating a closed 1-form around a generator of $\pi_1(M)$ gives a number, and the collection of these numbers (the periods) characterizes the cohomology class. The **period map** $H^1_{dR}(M) \to \mathrm{Hom}(\pi_1(M), \mathbb{R})$ is essentially the integration pairing. For Kähler manifolds, the period map is the gateway to Hodge theory and the Hodge decomposition $H^k(M; \mathbb{C}) = \bigoplus H^{p,q}$.

> [!tip] Aharonov–Bohm Effect *(from Gauge Theory and Quantum Mechanics)*
> In quantum mechanics, a charged particle moving in an electromagnetic field has wavefunction $\psi$ whose phase is determined by the line integral $\int_\gamma A$ of the electromagnetic potential 1-form $A$. The Aharonov–Bohm effect is the observation that for a magnetic field localized in a "tube" with topology of $S^1 \times \mathbb{R}^2$, the potential $A$ outside the tube is closed but *not* exact (the tube's interior is excluded from the region of definition). Different paths around the tube give different phases, observable as interference. This is a physical manifestation of $H^1_{dR}(M) \neq 0$ for the non-simply-connected exterior region — the present theorem's failure mode made into a measurable phenomenon.

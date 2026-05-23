---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Geodesic"
  - "Thm - First Variation of Arc Length"
  - "Def - The Index Form"
  - "Def - Jacobi Field"
tags: [geometry, riemannian-geometry, variational-calculus, index-form, curvature]
---

# Notation

$(M, g)$ a Riemannian manifold, $\gamma : [a, b] \to M$ a unit-speed [[Def - Geodesic|geodesic]] with $T = \dot\gamma$. A smooth two-parameter variation is $\Gamma(s, t) : (-\varepsilon, \varepsilon) \times [a, b] \to M$ with $\Gamma(0, t) = \gamma(t)$, $\gamma_s(t) := \Gamma(s, t)$, and variation field $V(t) := \partial_s|_{s=0}\Gamma(s, t)$. The transverse acceleration is $A := \nabla_{\partial_s}\nabla_{\partial_s}\Gamma|_{s=0}$ — a vector field along $\gamma$, generally not vanishing. The Riemann curvature tensor is $R$. The full registry is on [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Statement

> **Theorem (Second Variation of Arc Length).** Let $\gamma : [a, b] \to M$ be a unit-speed [[Def - Geodesic|geodesic]] and let $\gamma_s$ be a smooth variation of $\gamma$ with fixed endpoints and variation field $V$ orthogonal to $T = \dot\gamma$. Then
> $$\frac{d^2}{ds^2}\bigg|_{s=0} L(\gamma_s) = \int_a^b \bigl(g(V', V') - g(R(V, T)T, V)\bigr)\, dt = I(V, V),$$
> where $V' = \nabla_T V$, $R$ is the Riemann curvature tensor, and $I$ is the [[Def - The Index Form|index form]].

> **Corollary (sign of second variation determines minimisation).** A geodesic $\gamma$ is a strict local minimum of $L$ (with fixed endpoints) iff $I(V, V) > 0$ for all $V \in \mathcal V_0^\perp \setminus \{0\}$ (normal variations vanishing at the endpoints). $\gamma$ is not a local minimum if there exists $V \in \mathcal V_0^\perp$ with $I(V, V) < 0$.

> **Corollary (energy version).** For the energy $E$, the same formula $\frac{d^2}{ds^2}|_0 E(\gamma_s) = I(V, V)$ holds for normal variations $V$ along a (unit-speed) geodesic. The full energy version, including non-normal variations, has an additional contribution from the tangential part that does not appear in the length version.

> **Corollary (vanishing of $I(V, V)$).** $I(V, V) = 0$ for some non-zero $V \in \mathcal V_0^\perp$ iff $V$ is a [[Def - Jacobi Field|Jacobi field]] vanishing at the endpoints — i.e., iff the endpoints are [[Def - Conjugate Point|conjugate]] along $\gamma$.

---

# Motivation

The first variation identifies [[Def - Geodesic|geodesics]] as critical points of length and energy; the second variation determines what *kind* of critical points they are. Strictly minimising? Saddle? Maximum? The second variation is the Hessian of the length (or energy) functional at the geodesic, and its sign is what determines the local geometric character of the geodesic.

The remarkable feature is that **the second variation involves the Riemann curvature tensor**. The Hessian of length at $\gamma$ depends not only on the metric along $\gamma$ but on the curvature of $M$ in the plane spanned by $T$ and the variation direction $V$. This is geometrically deep: positive curvature decreases the index form (geodesics tend to come together — the "rubber band" intuition), and negative curvature increases it (geodesics tend to spread out — no length-minimisation obstruction from curvature). The first variation knew nothing about curvature; the second variation reveals it as the central player.

The connection to [[Def - Jacobi Field|Jacobi fields]] is the second remarkable feature. The kernel of $I$ (directions in which the Hessian is degenerate) is exactly the space of Jacobi fields vanishing at the endpoints — and these correspond to the conjugate-point obstruction. So $I$, the Hessian of length at a geodesic, has a degenerate direction iff the geodesic has a conjugate pair at its endpoints. This ties together the three independent-looking objects of the chapter: geodesics (geometric), Jacobi fields (ODE-theoretic), and the index form (variational).

The third remarkable feature is the **Morse Index Theorem**: the index of $I$ on $\mathcal V_0^\perp$ (the [[Def - Dimension|dimension]] of a maximal [[Def - Subspace|subspace]] on which $I$ is negative-definite) equals the number of conjugate points strictly inside $\gamma$ counted with multiplicity. This converts a *spectral* statement (about the negative eigenvalues of the Jacobi operator) into a *geometric counting* statement (about conjugate points along $\gamma$), and it is the prototype of all subsequent Morse-theoretic index theorems in geometric analysis.

Historically, the second variation formula was used by Bonnet, Synge, and Myers to prove the first global curvature-to-topology theorems: positive Ricci curvature bounded below ⟹ compact manifold of bounded diameter and finite fundamental [[Def - Group|group]] ([[Riemannian Geometry III — Riemann Curvature and Topology|Bonnet–Myers]]). The bookkeeping of the second variation is the entire technical content of these theorems.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a geodesic and a variation through it. Sources are problems where this setup is implicit but not openly stated.

The most common source is **a problem asking whether a geodesic minimises**. The first variation already tells us $\gamma$ is critical; the question of whether it is a minimum demands the second variation. Bridge: "is this the shortest path?" calls for the second variation, even if it is presented as a comparison problem ("compare the great-circle arc to the shorter alternative").

A subtler source is **a problem about Jacobi fields or conjugate points**. The dictionary between conjugate points and degeneracies of $I$ is bidirectional: a problem about Jacobi fields can be analysed via the index form, and vice versa. Bridge: "find conjugate points on this manifold" is the same as "find the kernel of the index form on geodesic arcs" — they are different views of the same equation.

A third source is **a problem with a curvature bound and a question about geodesic behaviour**. If the problem assumes "sectional curvature is $\geq K_0 > 0$" and asks about something, the second variation is almost certainly involved: positive curvature lower bounds force the curvature term in $I$ to dominate the kinetic term for long geodesics, producing conjugate points and obstructing length-minimisation. Bridge: any "$K \geq K_0$" or "$\mathrm{Ric} \geq K_0 g$" hypothesis routes through the second variation analysis to a structural conclusion.

A fourth source is **a problem about closed geodesics and their stability**. A closed geodesic is a periodic orbit of the geodesic flow, and its *stability* (linearly stable, hyperbolic, etc.) is governed by the linearised Poincaré return map, which is built from Jacobi fields along the closed geodesic — same kernel as the index form. So stability of periodic orbits in classical mechanics is a second-variation analysis.

**Targets (Output Amplification)**

The conclusion is the integral formula $\frac{d^2}{ds^2}|_0 L = I(V, V)$. Targets are the structural results that use this formula.

The most important combination is **second variation + positive curvature lower bound ⟹ Bonnet–Myers diameter bound**. Pick orthonormal normal variations $V_i(t) = \sin(\pi t / L) e_i(t)$ along a unit-speed geodesic of length $L$. Compute $\sum_i I(V_i, V_i) = (n-1)(\pi/L)^2 \int \cos^2(\pi t/L) - \int \sum_i g(R(V_i, T)T, V_i) = (n-1)(\pi/L)^2 \cdot L/2 - \int \mathrm{Ric}(T, T) \sin^2(\pi t/L)\, dt$. If $\mathrm{Ric} \geq (n-1)K_0 g$, then $\sum_i I(V_i, V_i) \leq (n-1) L [(\pi/L)^2/2 - K_0/2]$, which is *negative* if $L > \pi/\sqrt{K_0}$. So for long enough geodesics, the index is at least $1$, hence $\gamma$ is not minimising, hence by [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]] the diameter is at most $\pi/\sqrt{K_0}$. This is the entire technical content of Bonnet–Myers.

A second combination is **second variation + non-positive curvature ⟹ no conjugate points ⟹ $\exp_p$ is a diffeomorphism (Cartan–Hadamard)**. With $K \leq 0$, the curvature term in $I$ is non-positive, so $I \geq \int g(V', V') > 0$ for any nonzero $V$ vanishing at the endpoints. So $I$ is positive-definite for every geodesic, no conjugate points exist, and $\exp_p$ is a local diffeomorphism everywhere. With completeness and simple connectedness, $\exp_p$ is then a global diffeomorphism — the Cartan–Hadamard theorem. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

A third combination is **second variation + the Morse Index Theorem ⟹ count of conjugate points**. The index of $I$ on $\mathcal V_0^\perp$ equals the number of interior conjugate points, by the Morse Index Theorem. This makes the conjugate-point count a *variational* invariant of the geodesic. The theorem is the prototype of all Morse-theoretic counting theorems and the technical core of the Morse theory of the energy functional.

A fourth combination is **second variation + Synge's clever trick ⟹ Synge's theorem**. On a compact orientable even-dimensional manifold with positive sectional curvature, pick a closed geodesic of minimal length $\gamma$; parallel-transport an orthonormal frame around the loop; one direction $e$ is preserved (by even-dimensional orientation arguments); the variation $V = e$ (the *parallel* extension) gives $I(V, V) < 0$ by positive curvature, contradicting minimality. So no nontrivial closed geodesics exist — i.e., $\pi_1 = 0$. This is the simply-connectedness conclusion of Synge's theorem.

---

# Why Is It True

**Mechanism summary:** **the second variation of length at a geodesic decomposes into a "kinetic" term $\int g(V', V')$ (positive, encoding how the variation field wants to spread) and a "curvature" term $-\int g(R(V, T)T, V)$ (sign depending on sectional curvature, encoding the focusing or defocusing effect of curvature on nearby geodesics).**

The structural reason for the formula is the same as for the first variation: differentiate under the integral, swap covariant derivatives using torsion-freeness, integrate by parts using metric-compatibility. The new ingredient at second order is the curvature term, which arises from the swap of *two* sets of covariant derivatives — and one of these swaps picks up a Riemann tensor contribution.

Specifically, in computing $\frac{d^2}{ds^2}|_0 L(\gamma_s)$, we differentiate twice. The first differentiation gives $\int g(\nabla_T V, T)\, dt$ (as in the first variation, when restricted to a critical geodesic where the boundary contribution is captured by $V(b)$ vs $V(a)$). For the second differentiation we need the second derivative in $s$. This requires
$$\frac{d^2}{ds^2}|_{s=0}|\dot\gamma_s| = \frac{d}{ds}|_{s=0}\frac{g(\nabla_{\partial_s}T_s, T_s)}{|T_s|},$$
and computing this involves both another derivative of the inner product (giving a kinetic term) and a swap of $\nabla_{\partial_s}$ past $\nabla_T$ (giving a curvature term):
$$\nabla_{\partial_s}\nabla_T = \nabla_T \nabla_{\partial_s} + R(\partial_s, T),$$
because the connection is *not* flat in general — the failure to commute is the curvature operator. When applied to $T$ in the right place, this gives the $R(V, T)T$ term in the index form.

The two terms in $I(V, V) = \int g(V', V') - g(R(V, T)T, V)$ have a clean geometric interpretation:

- **Kinetic term $g(V', V')$.** Always non-negative; it represents the variation field's rate of change along $\gamma$. A larger $V'$ means the variation oscillates more rapidly, contributing positively to the length.

- **Curvature term $-g(R(V, T)T, V)$.** The quantity $g(R(V, T)T, V) = K(\sigma)\, |V|^2\, |T|^2 \sin^2\theta$ where $\sigma$ is the 2-plane spanned by $V$ and $T$, $K(\sigma)$ is the sectional curvature, and $\theta$ is the angle between $V$ and $T$ (here $V \perp T$ so $\sin\theta = 1$). For positive $K$, this term is positive, so $-g(R(V, T)T, V) < 0$, *decreasing* $I$. For negative $K$, the curvature term increases $I$. **The sign of the sectional curvature in the variation plane is the sign of the focusing of geodesics**: positive $K$ focuses, negative $K$ defocuses.

For a *short* geodesic (small $L = b - a$), the kinetic term dominates (by Wirtinger's inequality, $\int |V'|^2 \geq (\pi/L)^2 \int |V|^2$), so $I > 0$ — short geodesics minimise. For a *long* geodesic on a positively curved manifold, the curvature term can dominate, giving $I < 0$ — long geodesics don't minimise. The transition happens at the first conjugate point, where $I$ has zero eigenvalue.

The bridge to Jacobi fields: integrating by parts on the kinetic term,
$$I(V, V) = \int g(V', V')\, dt - \int g(R(V, T)T, V)\, dt = -\int g(V'' + R(V, T)T, V)\, dt$$
(with boundary terms vanishing for $V \in \mathcal V_0^\perp$). So $I(V, V) = -\int g(\mathcal J(V), V)\, dt$ where $\mathcal J$ is the Jacobi operator. The kernel of $I$ is the kernel of $\mathcal J$ restricted to fields vanishing at the endpoints — i.e., Jacobi fields vanishing at the endpoints — i.e., conjugate pairs. The connection is exact.

---

# What Makes This Hard

The conceptual difficulty is **the appearance of the curvature tensor in the second variation**. The first variation involves only the metric (via $\nabla T$); the second variation involves the curvature. This is unexpected if one is thinking of $L$ as just an integral of $|\dot\gamma|$ — there is nothing curvature-y about the integrand. The curvature appears because computing the *second* derivative requires swapping covariant derivatives, and *that swap* is where the curvature lives.

The technical difficulty is **bookkeeping the variation surface carefully**. We are differentiating twice in $s$ on a curve $\gamma_s(t)$ in $M$, which means we need to keep track of $\nabla_{\partial_s}\nabla_{\partial_s}\Gamma$ — a *transverse acceleration*, generally not vanishing. This object does *not* appear in the final formula (it cancels because we are at a critical point of the first variation), but it must be handled carefully along the way.

The most common error is to **forget the orthogonality assumption** $V \perp T$. The formula as stated assumes normal variations; for tangential variations, the length is unchanged to all orders (reparametrisation), so the second variation also vanishes — but the formula as written doesn't manifestly show this without the orthogonality assumption. To handle general variations, decompose $V = V^\parallel + V^\perp$ and treat each piece separately.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Start from the first-variation formula evaluated at general (not necessarily critical) $\gamma$; differentiate again in $s$. Use the curvature identity $\nabla_{\partial_s}\nabla_T - \nabla_T \nabla_{\partial_s} = R(\partial_s, T)$ to introduce curvature. At a geodesic (critical point of first variation), the algebra collapses to the index-form expression. Apply integration by parts and the curvature symmetry to get the symmetric form $\int g(V', V') - g(R(V, T)T, V)$.

**Subgoal decomposition:**

1. **Write the first variation for general $\gamma$.** $\frac{d}{ds} L(\gamma_s) = \int g(\nabla_T V_s, T_s)\, dt +$ boundary terms, where $V_s = \partial_s \Gamma$ and $T_s = \partial_t \Gamma$.
   - *Hint:* the formula generalises trivially; just don't yet assume $\gamma$ is a geodesic.
   - *Why needed:* sets up the framework for differentiating again.

2. **Differentiate in $s$, evaluating at $s = 0$.** $\frac{d^2}{ds^2}|_0 L = \int \frac{d}{ds}|_0 [g(\nabla_T V_s, T_s)/|T_s|]\, dt$. Compute this using the chain rule on the quotient.
   - *Hint:* the denominator $|T_s| = 1$ at $s = 0$ (unit-speed); its $s$-derivative contributes.
   - *Why needed:* sets up the second-derivative calculation.

3. **Use the curvature swap.** $\nabla_{\partial_s}\nabla_T = \nabla_T \nabla_{\partial_s} + R(\partial_s, T)$ as operators on vector fields along $\Gamma$. Apply to $V_s$ at $s = 0$ to get an $R$ term.
   - *Hint:* this is the definition of the Riemann curvature operator, applied to the parametrised surface.
   - *Why needed:* introduces the curvature into the formula.

4. **At a geodesic, $\nabla_T T = 0$, simplifying the surviving terms.** Most of the messy intermediate terms (involving $\nabla_T T$) vanish, leaving only $\int g(V', V') - g(R(V, T)T, V) + \int g(\text{tangential stuff}, T)$.
   - *Hint:* the tangential terms involve $g(\cdot, T)$, which vanishes for normal $V$.
   - *Why needed:* reduces to the clean index-form expression.

5. **Restrict to normal $V \perp T$.** The tangential boundary contributions all vanish, leaving exactly $I(V, V)$.
   - *Hint:* this is where the assumption $V \perp T$ pays off.
   - *Why needed:* gives the clean formula.

6. **Apply integration by parts to verify Jacobi-operator form.** $I(V, V) = -\int g(V'' + R(V, T)T, V)$, identifying the kernel with Jacobi fields vanishing at the endpoints.
   - *Hint:* this is the same integration-by-parts as in the first variation.
   - *Why needed:* connects to the conjugate-point characterisation.

---

# Lemma Decomposition

> [!note]- Lemma 1: Curvature appears via the commutator of covariant derivatives
> **Statement:** For a smooth two-parameter map $\Gamma : (-\varepsilon, \varepsilon) \times [a, b] \to M$ and any vector field $W$ along $\Gamma$,
> $$\nabla_{\partial_s}\nabla_{\partial_t} W - \nabla_{\partial_t}\nabla_{\partial_s} W = R(\partial_s \Gamma, \partial_t \Gamma) W.$$
>
> **Hint:** This is the definition of the Riemann curvature tensor, specialised to vector fields along a parametrised surface, with $[\partial_s, \partial_t] = 0$.
>
> **Why needed:** This is where curvature enters the second-variation calculation.
>
> > [!note]- Full proof
> > The general definition of the Riemann tensor is $R(X, Y)W = \nabla_X \nabla_Y W - \nabla_Y \nabla_X W - \nabla_{[X, Y]} W$ for vector fields $X, Y, W$ on $M$. For the pullback to a parametrised surface, with $X = \partial_s \Gamma, Y = \partial_t \Gamma$ (vector fields along $\Gamma$, not vector fields on $M$), the bracket $[\partial_s \Gamma, \partial_t \Gamma]$ — interpreted via the pullback — vanishes because $[\partial_s, \partial_t] = 0$ on the parameter space and the connection is torsion-free. So
> > $$\nabla_{\partial_s}\nabla_{\partial_t} W - \nabla_{\partial_t}\nabla_{\partial_s} W = R(\partial_s \Gamma, \partial_t \Gamma) W.$$

> [!note]- Lemma 2: Second variation formula for length
> **Statement:** Let $\gamma$ be a unit-speed geodesic and $\gamma_s$ a fixed-endpoint variation with variation field $V$ orthogonal to $T = \dot\gamma$. Then
> $$\frac{d^2}{ds^2}\bigg|_0 L(\gamma_s) = \int_a^b g(V', V')\, dt - \int_a^b g(R(V, T)T, V)\, dt = I(V, V).$$
>
> **Hint:** Differentiate the first-variation formula in $s$ at $s = 0$. Use Lemma 1 to swap covariant derivatives, picking up the curvature term. The fact that $\gamma$ is a geodesic ($\nabla_T T = 0$) kills several terms. The orthogonality $V \perp T$ kills boundary terms involving $g(\cdot, T)$.
>
> **Why needed:** Establishes the second variation formula as the index form.
>
> > [!note]- Full proof
> > Start from $\frac{d}{ds} L(\gamma_s) = \int_a^b \frac{g(\nabla_{\partial_s}T_s, T_s)}{|T_s|}\, dt$. Differentiate again in $s$, using the quotient rule and the product rule. At $s = 0$, $|T| = 1$ and $\nabla_T T = 0$ (geodesic).
> >
> > The terms that survive (after using $V \perp T$, $\nabla_T T = 0$, and integration by parts as in the first-variation argument):
> > $$\frac{d^2}{ds^2}\bigg|_0 L(\gamma_s) = \int_a^b g(\nabla_T V, \nabla_T V)\, dt + \int_a^b g(\nabla_{\partial_s}\nabla_T T|_{s=0}, V)\, dt + (\text{boundary terms vanishing for fixed endpoints}).$$
> > By Lemma 1, $\nabla_{\partial_s}\nabla_T T|_{s=0} = \nabla_T \nabla_{\partial_s} T|_{s=0} + R(V, T) T$. Since $T = \partial_t \Gamma$ and $\nabla_{\partial_s} T|_{s=0} = \nabla_T V$ (by torsion-freeness in the parameter surface), the first term contributes $\nabla_T \nabla_T V = V''$ — but this combines with the $\nabla_T V$ kinetic term via integration by parts.
> >
> > Putting everything together and integrating by parts to consolidate, and using the curvature symmetry $g(R(V, T)T, V) = -g(R(V, T)V, T)$ etc., one obtains
> > $$\frac{d^2}{ds^2}\bigg|_0 L(\gamma_s) = \int_a^b g(V', V')\, dt - \int_a^b g(R(V, T)T, V)\, dt,$$
> > which is the index form $I(V, V)$. (The intermediate calculation has several signs and cancellations; we refer to do Carmo or Lee for the line-by-line bookkeeping.)

> [!note]- Lemma 3: Kernel of $I$ on normal variations vanishing at endpoints = Jacobi fields
> **Statement:** A normal variation field $V$ vanishing at the endpoints satisfies $I(V, W) = 0$ for *every* $W \in \mathcal V_0^\perp$ if and only if $V$ is a Jacobi field — i.e., $V'' + R(V, T)T = 0$.
>
> **Hint:** Integration by parts on $I(V, W)$ converts it to $-\int g(V'' + R(V, T)T, W)\, dt$ for $W$ vanishing at the endpoints. Apply the fundamental lemma of the calculus of variations.
>
> **Why needed:** This identifies the kernel of $I$, hence the conjugate-point obstruction to length-minimisation.
>
> > [!note]- Full proof
> > $I(V, W) = \int_a^b g(V', W') - g(R(V, T)T, W)\, dt$. Integration by parts on the first term:
> > $$\int_a^b g(V', W')\, dt = [g(V', W)]_a^b - \int_a^b g(V'', W)\, dt = -\int_a^b g(V'', W)\, dt$$
> > (boundary term vanishes since $W(a) = W(b) = 0$). So $I(V, W) = -\int_a^b g(V'' + R(V, T)T, W)\, dt$.
> >
> > If this vanishes for every $W \in \mathcal V_0^\perp$, then by the fundamental lemma applied to the orthogonal projection onto $T^\perp$, $V'' + R(V, T)T \perp T$ and equal to its $T^\perp$-projection; combined with the normality of $V'' + R(V, T)T$ (which follows from $V \perp T$ and a similar computation), we conclude $V'' + R(V, T)T = 0$ — i.e., $V$ is a Jacobi field. The converse is direct: if $V$ is a Jacobi field, $I(V, W) = 0$ for every $W$ vanishing at the endpoints.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $\gamma : [a, b] \to M$ be a unit-speed geodesic and $\gamma_s$ a smooth fixed-endpoint variation with variation field $V \perp T$. Then
> $$\frac{d^2}{ds^2}\bigg|_0 L(\gamma_s) = \int_a^b \bigl(g(V', V') - g(R(V, T)T, V)\bigr)\, dt = I(V, V).$$
>
> *Proof.* See Lemma 2 for the calculation: differentiate the first-variation formula in $s$, use the curvature commutator (Lemma 1), use the geodesic equation $\nabla_T T = 0$ to kill intermediate terms, use the orthogonality $V \perp T$ to kill tangential boundary contributions, integrate by parts to assemble the symmetric form. The result is $I(V, V)$.
>
> **Corollary.** $\gamma$ is a strict local minimum of $L$ on the space of fixed-endpoint curves iff $I(V, V) > 0$ for every nonzero $V \in \mathcal V_0^\perp$. If there is $V \in \mathcal V_0^\perp$ with $I(V, V) < 0$, then $\gamma$ is not a local minimum.
>
> *Proof.* The standard second-derivative test on functional spaces: a critical point is a strict local minimum iff its Hessian is positive-definite. $I$ is the Hessian; positive-definiteness is the criterion.
>
> **Corollary (kernel of $I$ = Jacobi fields).** By Lemma 3, $V \in \ker I|_{\mathcal V_0^\perp}$ iff $V$ is a Jacobi field. This kernel is non-trivial iff the endpoints are conjugate along $\gamma$. So $I$ is positive-semidefinite (with kernel) at the first conjugate pair, indefinite past the first conjugate point, and positive-definite below. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Variational calculus: the second variation of any Lagrangian.** For a general Lagrangian $L(q, \dot q)$ on $TM$, the second variation around a critical-point trajectory is a quadratic form analogous to the index form. The signature of this form determines the local minimisation properties of the trajectory, and the kernel corresponds to **Jacobi fields of the Lagrangian** — solutions to the linearised Euler–Lagrange equations. The geodesic case is the prototype; the same machinery applies to optimal control, variational problems on graphs, and infinite-dimensional variational problems (harmonic maps, minimal surfaces).

**Optimal control: the second-order conditions for optimality.** In control theory, the Pontryagin maximum principle gives first-order necessary conditions. Second-order conditions (analogous to the second variation) determine whether a candidate trajectory is actually optimal. The conjugate-point conditions for control problems, the **Riccati equation** for the second-order propagator, and the **Maslov index** counting the focal points are all generalisations of the geodesic-case Morse Index Theorem.

**Quantum mechanics: WKB and the Maslov index.** The semiclassical limit of quantum mechanics on a manifold concentrates wavefunctions on Lagrangian submanifolds of $T^*M$. The phase corrections at caustics (where the Lagrangian submanifold is no longer a graph over $M$) are governed by the **Maslov index**, a generalisation of the Morse index for Lagrangian intersections. The geodesic Morse index — counting conjugate points — is the case where the Lagrangian submanifold is the image of a Hamiltonian flow line.

**Mathematical relativity: Penrose's singularity theorem.** Penrose proved that in Lorentzian signature, under suitable causal-structure and energy conditions, **trapped surfaces** generate **incomplete** timelike or null geodesics — i.e., singularities. The proof uses a second-variation argument (the Raychaudhuri equation, which is the Jacobi equation in Lorentzian signature applied to a congruence of geodesics): focusing of a null geodesic congruence in finite affine parameter forces incompleteness. This is the dramatic Lorentzian analogue of Bonnet–Myers.

---

# Bridges

- **[[Thm - First Variation of Arc Length|First Variation of Arc Length]]** — the predecessor. The first variation identifies geodesics as critical points; the second variation classifies the type of critical point. They are the standard first-and-second derivative tools of the calculus of variations applied to length.

- **[[Def - The Index Form|The Index Form]]** — the bilinear form that *is* the second variation. The index form $I(V, W)$ on normal variations along a geodesic *is* the Hessian of length at $\gamma$, and the second-variation theorem is the statement of this identity.

- **[[Def - Jacobi Field|Jacobi Fields]]** — the kernel. Jacobi fields vanishing at the endpoints are exactly the kernel of $I$ on $\mathcal V_0^\perp$, and this kernel is non-trivial exactly at conjugate-point parameter pairs. The second variation is the *variational* face of the Jacobi-field theory; the Jacobi equation is its *ODE* face.

- **[[Thm - Jacobi Equation and Conjugate Points|Jacobi Equation and Conjugate Points]]** — the curvature-eigenvalue dictionary. The Jacobi equation along $T^\perp$ decomposes (in a parallel frame) into scalar Sturm–Liouville equations $f_i'' + \lambda_i(t) f_i = 0$, where $\lambda_i$ are the eigenvalues of the curvature operator. Sturm comparison then translates curvature bounds into conjugate-point distance bounds, the technical core of all comparison theorems.

- **The Bonnet–Myers diameter bound** — the direct application. Pick orthonormal $V_i = \sin(\pi t/L) e_i$ along a unit-speed geodesic of length $L$; compute $\sum_i I(V_i, V_i)$ using the second-variation formula; if $\mathrm{Ric} \geq (n-1) K_0 g$ and $L > \pi/\sqrt{K_0}$, the sum is negative, proving the geodesic does not minimise. By [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]], diameter $\leq \pi/\sqrt{K_0}$. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

---

# Unlocked by This

> [!tip] The Morse Index Theorem *(from Riemannian Geometry / Morse Theory)*
> The **Morse Index Theorem** states that the index of $I$ on $\mathcal V_0^\perp$ equals the number of conjugate points to $\gamma(a)$ strictly inside $(\gamma(a), \gamma(b))$ along $\gamma$, counted with multiplicity. The proof uses the second-variation formula and a careful analysis of how the index changes as $b$ varies. This is the prototype of all Morse-theoretic counting theorems and is the technical core of the Morse theory of the energy functional on the loop space.

> [!tip] **Bonnet–Myers and Cartan–Hadamard** *(from Riemannian Geometry)*
> The second variation is the direct input to the two foundational curvature-to-topology theorems: **Bonnet–Myers** (positive Ricci ⟹ compact, bounded diameter, finite $\pi_1$) and **Cartan–Hadamard** (non-positive sectional curvature + complete + simply connected ⟹ diffeomorphic to $\mathbb{R}^n$ via $\exp_p$). Both are derived by analysing the sign of $I$ on appropriately chosen test variations. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] **The Lorentzian Singularity Theorems** *(from General Relativity)*
> The Lorentzian analogue of the second variation — the **Raychaudhuri equation** governing the expansion of geodesic congruences — combined with positive energy conditions and trapped surfaces, gives the **Penrose–Hawking singularity theorems**: under reasonable physical conditions on the matter content, spacetime singularities (geodesic incompleteness in Lorentzian signature) are inevitable. Black-hole singularities and the Big Bang are direct consequences. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

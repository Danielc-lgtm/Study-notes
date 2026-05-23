---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Geodesic"
  - "Def - Length and Energy Functionals"
tags: [geometry, riemannian-geometry, variational-calculus]
---

# Notation

$(M, g)$ a Riemannian manifold, $\gamma : [a, b] \to M$ a smooth curve with velocity $T := \dot\gamma$, often taken unit-speed so $|T| = 1$. A **smooth variation** of $\gamma$ is a smooth map $\Gamma : (-\varepsilon, \varepsilon) \times [a, b] \to M$ with $\Gamma(0, t) = \gamma(t)$; we write $\gamma_s(t) := \Gamma(s, t)$, and the **variation field** is $V(t) := \partial_s|_{s=0}\Gamma(s, t)$, a vector field along $\gamma$. A variation has **fixed endpoints** if $\gamma_s(a) = \gamma(a)$ and $\gamma_s(b) = \gamma(b)$ for all $s$, i.e. $V(a) = V(b) = 0$. The full registry: [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Statement

> **Theorem (First Variation of Arc Length).** Let $\gamma : [a, b] \to M$ be a smooth unit-speed curve on a Riemannian manifold $(M, g)$, with tangent $T = \dot\gamma$. For any smooth variation $\gamma_s$ of $\gamma$ with variation field $V$,
> $$\frac{d}{ds}\bigg|_{s=0} L(\gamma_s) = -\int_a^b g(V, \nabla_T T)\, dt + g(V(b), T(b)) - g(V(a), T(a)).$$
> Consequently, a smooth unit-speed curve $\gamma$ is a critical point of $L$ with respect to *all fixed-endpoint smooth variations* (i.e., $V(a) = V(b) = 0$) if and only if $\nabla_T T = 0$ — i.e., $\gamma$ is a [[Def - Geodesic|geodesic]].

> **Corollary (energy version).** The same conclusion holds for the energy functional $E$: a constant-speed curve $\gamma$ is a critical point of $E$ with respect to all fixed-endpoint smooth variations iff $\nabla_T T = 0$. The first variation of $E$ on a unit-speed curve is
> $$\frac{d}{ds}\bigg|_{s=0} E(\gamma_s) = -\int_a^b g(V, \nabla_T T)\, dt + g(V(b), T(b)) - g(V(a), T(a)).$$

> **Corollary (no-need-to-be-unit-speed).** For a general smooth curve $\gamma$, the same conclusion holds: critical points of $L$ (modulo reparametrisation) are unparametrised [[Def - Geodesic|geodesics]]; critical points of $E$ are parametrised geodesics (which are automatically constant-speed).

---

# Motivation

The variational principle is the second great characterisation of geodesics, complementing the ODE characterisation in [[Def - Geodesic|the geodesic equation]]. The ODE characterisation is local and operational; the variational characterisation is global and conceptual. The first variation formula is the bridge: it shows that the *Euler–Lagrange equation* of the length functional (or, more cleanly, the energy functional) is exactly the geodesic equation.

Why does this matter? Two reasons.

First, it explains *why* the geodesic equation is the right definition of "straight". Calling a curve straight if its covariant acceleration vanishes is mathematically convenient but does not immediately convey that this is the curve "of least length". The first variation formula shows that critical points of length are exactly geodesics — so geodesics are precisely the locally length-extremising curves. (Whether they are minima vs saddles is the content of the second variation; the first variation just identifies criticality.) This makes the choice of geodesic equation as definition not arbitrary but forced by the variational principle.

Second, it unlocks the entire machinery of the calculus of variations. Once we know geodesics are critical points of $L$ (or $E$), we can use Morse theory of the energy functional to prove existence theorems (e.g., **the existence of closed geodesics on any closed Riemannian manifold** — a theorem proved by Ljusternik–Fet using minimax over the loop space), and we can use the second variation to study local-minimisation properties, conjugate points, and the index form. The first variation formula is the entry point to all of this.

The formula itself is, structurally, the standard integration-by-parts that appears in any first-variation calculation in physics or mathematics. The new content is that the result is an integral whose integrand is $-g(V, \nabla_T T)$ — i.e., the variational equation is $\nabla_T T = 0$. The proof is a direct calculation using metric-compatibility of the connection and the swap of covariant derivatives in the parametrisation surface.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a smooth curve and a smooth variation. The sources are problems where this setup is implicit.

The most common source is **any minimum-finding problem on a Riemannian manifold**. If you are trying to find the curve of minimum length between two given points, you are setting up a calculus-of-variations problem whose Euler–Lagrange equation is the geodesic equation — by the first variation. The bridge: any "shortest path on a manifold" problem can be re-cast as "find the geodesics between the endpoints", and the first variation formula is the tool that converts the global minimisation problem into the local ODE.

A subtler source is **a Lagrangian mechanics problem with kinetic energy alone**. The Lagrangian $L(q, \dot q) = \tfrac12 g_{ij}\dot q^i \dot q^j$ is the kinetic energy of a unit-mass particle moving on $(M, g)$, and the Euler–Lagrange equation $\frac{d}{dt}\frac{\partial L}{\partial \dot q^k} = \frac{\partial L}{\partial q^k}$ produces the geodesic equation $\ddot q^k + \Gamma^k_{ij}\dot q^i \dot q^j = 0$. The first variation formula for $E$ is exactly the abstract version of this concrete physics calculation. The bridge: any "minimise the action of a free particle" problem on a curved configuration space is a geodesic problem.

A third source is **a geodesic-flow conservation law**. If $X$ is a [[Def - Vector Field on a Manifold|Killing field]] on $M$ (so its flow is by isometries), then $g(T, X)$ is conserved along any geodesic. This is a Noether-style conservation law derived from the first variation: a one-parameter family of isometries gives a one-parameter family of curves all of the same length, hence a critical-point family, hence a conservation law. The bridge: every continuous isometry of $(M, g)$ gives a conserved quantity for geodesic flow.

**Targets (Output Amplification)**

The conclusion of the theorem is "$\gamma$ critical for $L$ ⟺ $\gamma$ is a geodesic". The targets are the constructions that build on this.

The most important combination is **first variation + second variation ⟹ index form**. Once the first variation identifies geodesics as critical points, the natural next question is "what kind of critical point — minimum, saddle, maximum?" The second variation (Hessian) of $L$ at a geodesic is the [[Def - The Index Form|index form]] $I$, and its signature determines the geometric nature of the critical point. The first variation is therefore the gateway to the entire local Morse theory of geodesics, conjugate points, and the Bonnet–Myers diameter bound.

A second combination is **first variation + Hopf–Rinow ⟹ existence of minimising geodesics between any two points (on complete manifolds)**. On a complete Riemannian manifold, [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]] gives that the infimum of lengths over curves from $p$ to $q$ is realised by some curve. The first variation then shows this minimising curve is a geodesic — without the first variation formula, we could only conclude the existence of a minimiser, not its dynamical character.

A third combination is **first variation + reparametrisation gives the energy version of the theorem**. The energy functional $E$ is *not* reparametrisation-invariant; its critical points are parametrised geodesics (constant-speed, with the specific parametrisation determined by the equation). Combining the first variation of $L$ with Cauchy–Schwarz gives the first variation of $E$, and the two together explain why we prefer to vary $E$: its critical points are exactly the parametrised geodesics, no reparametrisation freedom left over.

A fourth combination is **first variation + a one-parameter family of isometries gives Noether's theorem**. If $\varphi_s$ is a one-parameter family of isometries of $(M, g)$ with $\varphi_0 = \mathrm{id}$ and generating Killing field $X$, then for any geodesic $\gamma$, the variation $\gamma_s := \varphi_s \circ \gamma$ preserves length: $L(\gamma_s) = L(\gamma)$. So $\frac{d}{ds}|_0 L(\gamma_s) = 0$. By the first variation formula (with $V = X|_\gamma$), this gives the boundary terms cancel to zero in a coordinate-invariant way, and in fact the function $g(T, X)$ is conserved along $\gamma$. This is Noether's theorem for geodesics: every Killing field gives a conserved momentum.

---

# Why Is It True

**Mechanism summary:** **the variation of length is computed by differentiating $\sqrt{g(\dot\gamma, \dot\gamma)}$ under the integral, swapping covariant derivatives $\nabla_{\partial_s}\partial_t = \nabla_{\partial_t}\partial_s$ (torsion-free), and integrating by parts to isolate $\langle V, \nabla_T T\rangle$ as the integrand — the boundary terms give the endpoint contribution, and fixed-endpoint variations kill them.**

The calculation is a direct unrolling of the chain rule and integration by parts. Start with
$$L(\gamma_s) = \int_a^b \sqrt{g(\dot\gamma_s, \dot\gamma_s)}\, dt.$$
Differentiate in $s$ at $s = 0$:
$$\frac{d}{ds}\bigg|_0 L(\gamma_s) = \int_a^b \frac{g(\nabla_{\partial_s}\dot\gamma_s, \dot\gamma_s)}{\sqrt{g(\dot\gamma_s, \dot\gamma_s)}}\bigg|_{s=0}\, dt = \int_a^b \frac{g(\nabla_{\partial_s}T, T)}{|T|}\, dt.$$
For unit-speed $\gamma$, $|T| = 1$, simplifying.

Now use the symmetry $\nabla_{\partial_s}T = \nabla_{\partial_s}\partial_t \Gamma = \nabla_{\partial_t}\partial_s \Gamma = \nabla_{\partial_t} V = \nabla_T V$, valid because the connection is torsion-free and $[\partial_s, \partial_t] = 0$ (these are coordinate vector fields on the parameter rectangle). So
$$\frac{d}{ds}\bigg|_0 L = \int_a^b g(\nabla_T V, T)\, dt.$$

Integrate by parts using metric compatibility ($T g(V, T) = g(\nabla_T V, T) + g(V, \nabla_T T)$):
$$\int_a^b g(\nabla_T V, T)\, dt = \int_a^b T g(V, T)\, dt - \int_a^b g(V, \nabla_T T)\, dt = [g(V, T)]_a^b - \int_a^b g(V, \nabla_T T)\, dt.$$
This is the first variation formula.

If $V(a) = V(b) = 0$ (fixed endpoints), the boundary term vanishes:
$$\frac{d}{ds}\bigg|_0 L = -\int_a^b g(V, \nabla_T T)\, dt.$$
For $\gamma$ to be a critical point, this must vanish for *every* $V$ vanishing at the endpoints. The fundamental lemma of the calculus of variations then forces $\nabla_T T = 0$ — the geodesic equation.

The reason the formula is so clean is that the connection's two crucial properties — torsion-freeness (so $\nabla_{\partial_s}\partial_t = \nabla_{\partial_t}\partial_s$) and metric compatibility (so we can integrate by parts) — *both* enter, in different roles. Without torsion-freeness, the swap of covariant derivatives would pick up a torsion term; without metric compatibility, the integration by parts would not yield the clean inner product $g(V, \nabla_T T)$ with a definite sign. The first variation formula is therefore one place where the full structure of the Levi-Civita connection is being used.

---

# What Makes This Hard

The conceptual difficulty is **understanding why the variation surface $\Gamma : (-\varepsilon, \varepsilon) \times [a, b] \to M$ has two distinguished directions** and why the covariant derivatives $\nabla_{\partial_s}$ and $\nabla_{\partial_t}$ can be swapped. The swap requires both torsion-freeness of the connection and the fact that $[\partial_s, \partial_t] = 0$ on the parameter space — and the latter is a property of coordinate fields, not a tautology.

The technical difficulty is **handling the square-root in the length integrand**. The energy functional avoids this by using the squared norm, which is what makes $E$ technically cleaner. For arc length, the differentiation produces a $1/|T|$ factor that one usually handles by assuming unit-speed parametrisation at the start.

The most common error is to **drop the boundary terms** without checking the variation is fixed-endpoint. The boundary terms encode genuine geometric information — they are what gives the first variation formula its "open endpoint" meaning, used in computing the length of nearby geodesics from a fixed point to a moving point.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute $\frac{d}{ds}|_{s=0} L(\gamma_s)$ by differentiating under the integral. Swap covariant derivatives $\nabla_{\partial_s}\partial_t = \nabla_{\partial_t}\partial_s$ using torsion-freeness. Integrate by parts using metric compatibility to isolate $-\int g(V, \nabla_T T)\, dt + \text{boundary}$. Apply the fundamental lemma to conclude criticality ⟺ geodesic equation.

**Subgoal decomposition:**

1. **Differentiate under the integral.** $\frac{d}{ds}\big|_0 L(\gamma_s) = \int_a^b \frac{g(\nabla_{\partial_s}\dot\gamma_s, \dot\gamma_s)}{|\dot\gamma_s|}|_{s=0}\, dt$.
   - *Hint:* this is the chain rule for $\sqrt{g(\dot\gamma_s, \dot\gamma_s)}$ in $s$, using metric compatibility.
   - *Why needed:* converts variation of length to variation of a vector quantity.

2. **Swap covariant derivatives.** $\nabla_{\partial_s}\dot\gamma_s = \nabla_{\partial_t}V$, using torsion-freeness and $[\partial_s, \partial_t] = 0$.
   - *Hint:* in coordinates, $\nabla_{\partial_s}\partial_t \Gamma - \nabla_{\partial_t}\partial_s \Gamma = $ torsion $T(\partial_s, \partial_t) + [\partial_s, \partial_t]$ — both vanish.
   - *Why needed:* converts the awkward $\nabla_{\partial_s}T$ to the natural $T V'$ where $V' = \nabla_T V$.

3. **Specialise to unit speed.** For $|T| = 1$, the integrand becomes $g(V', T)$.
   - *Hint:* divides cleanly when $|T| = 1$.
   - *Why needed:* simplifies the formula.

4. **Integrate by parts.** $\int g(V', T) = [g(V, T)]_a^b - \int g(V, \nabla_T T)$, using metric compatibility.
   - *Hint:* $T g(V, T) = g(V', T) + g(V, \nabla_T T)$, integrate.
   - *Why needed:* isolates $\nabla_T T$ as the variational quantity.

5. **Apply the fundamental lemma.** If $\int_a^b g(V, \nabla_T T) dt = 0$ for *every* smooth $V$ vanishing at endpoints, then $\nabla_T T \equiv 0$.
   - *Hint:* take $V = f \cdot \nabla_T T$ for a bump function $f \geq 0$, then $\int f |\nabla_T T|^2 = 0$ forces $\nabla_T T = 0$ on the support of $f$, which can be arbitrary.
   - *Why needed:* converts the integral identity to a pointwise equation.

6. **Conclude criticality ⟺ geodesic.** Critical point with fixed endpoints ⟺ $\nabla_T T = 0$ ⟺ $\gamma$ is a geodesic.

---

# Lemma Decomposition

> [!note]- Lemma 1: Differentiating arc length under the integral
> **Statement:** For a smooth variation $\gamma_s$ with $|\dot\gamma_s| \neq 0$, $\frac{d}{ds}|_{s=0} L(\gamma_s) = \int_a^b \frac{g(\nabla_{\partial_s}\dot\gamma_s, \dot\gamma_s)}{|\dot\gamma_s|}\bigg|_{s=0}\, dt$.
>
> **Hint:** Apply the chain rule to $\sqrt{g(\dot\gamma_s, \dot\gamma_s)}$ in $s$.
>
> **Why needed:** Converts the length variation into a metric-derived expression.
>
> > [!note]- Full proof
> > $L(\gamma_s) = \int_a^b \sqrt{g(\dot\gamma_s, \dot\gamma_s)}\, dt$. Differentiate in $s$, using metric compatibility $\partial_s g(\dot\gamma_s, \dot\gamma_s) = 2 g(\nabla_{\partial_s}\dot\gamma_s, \dot\gamma_s)$:
> > $$\frac{d}{ds} L(\gamma_s) = \int_a^b \frac{1}{2\sqrt{g(\dot\gamma_s, \dot\gamma_s)}} \cdot 2 g(\nabla_{\partial_s}\dot\gamma_s, \dot\gamma_s)\, dt = \int_a^b \frac{g(\nabla_{\partial_s}\dot\gamma_s, \dot\gamma_s)}{|\dot\gamma_s|}\, dt.$$
> > Evaluating at $s = 0$ gives the claim.

> [!note]- Lemma 2: $\nabla_{\partial_s}\dot\gamma_s = \nabla_{\partial_t}V$ (commutation of covariant derivatives in the variation surface)
> **Statement:** For a smooth variation $\Gamma(s, t)$ with $\dot\gamma_s = \partial_t \Gamma$ and $V = \partial_s\Gamma|_{s=0}$, $\nabla_{\partial_s}(\partial_t \Gamma) = \nabla_{\partial_t}(\partial_s \Gamma)$.
>
> **Hint:** This is a consequence of torsion-freeness combined with $[\partial_s, \partial_t] = 0$.
>
> **Why needed:** Converts $\nabla_{\partial_s}T$ (awkward) to $\nabla_T V$ (natural along $\gamma$).
>
> > [!note]- Full proof
> > The torsion-free condition for the connection on a parametrised surface is
> > $$\nabla_{\partial_s}\partial_t \Gamma - \nabla_{\partial_t}\partial_s \Gamma = [\partial_s \Gamma, \partial_t \Gamma].$$
> > Wait — that's not quite right. The torsion condition is $\nabla_X Y - \nabla_Y X = [X, Y]$ for actual vector fields $X, Y$ on $M$. For a parametrised surface $\Gamma$, the vector fields $\partial_s \Gamma$ and $\partial_t \Gamma$ are only defined *along* $\Gamma$, not globally on $M$, so the formula needs reinterpretation. The correct identity is: for $\Gamma : U \to M$ smooth and the connection $\nabla$ pulled back along $\Gamma$, $\nabla_{\partial_s}\partial_t \Gamma = \nabla_{\partial_t}\partial_s \Gamma$ whenever the connection on $M$ is torsion-free and $[\partial_s, \partial_t] = 0$ on the parameter space $U$.
> >
> > Explicitly: in coordinates, $\partial_t \Gamma = \partial_t \Gamma^k \cdot \partial_k$ and $\partial_s \Gamma = \partial_s \Gamma^k \cdot \partial_k$. Compute:
> > $$\nabla_{\partial_s}(\partial_t \Gamma) = \partial_s \partial_t \Gamma^k \cdot \partial_k + \partial_t \Gamma^k \cdot \nabla_{\partial_s \Gamma}\partial_k = \partial_s \partial_t \Gamma^k \cdot \partial_k + \partial_t \Gamma^k \partial_s \Gamma^j \Gamma^l_{jk}\partial_l.$$
> > And similarly $\nabla_{\partial_t}(\partial_s \Gamma) = \partial_t \partial_s \Gamma^k \cdot \partial_k + \partial_s \Gamma^k \partial_t \Gamma^j \Gamma^l_{jk}\partial_l$. The mixed second partial derivatives $\partial_s \partial_t = \partial_t \partial_s$ agree (equality of mixed partials in smooth $\Gamma$), and the bilinear Christoffel terms are symmetric in $(j, k)$ (because the Levi-Civita connection is torsion-free, $\Gamma^l_{jk} = \Gamma^l_{kj}$). So the two expressions agree.

> [!note]- Lemma 3: Integration by parts using metric compatibility
> **Statement:** For a vector field $V$ along $\gamma$, $\int_a^b g(\nabla_T V, T)\, dt = [g(V, T)]_a^b - \int_a^b g(V, \nabla_T T)\, dt$.
>
> **Hint:** Differentiate $g(V, T)$ along $\gamma$ using metric compatibility and integrate.
>
> **Why needed:** Isolates $\nabla_T T$, which is the variational unknown we want to determine.
>
> > [!note]- Full proof
> > By metric compatibility,
> > $$T g(V, T) = g(\nabla_T V, T) + g(V, \nabla_T T).$$
> > Integrating from $a$ to $b$:
> > $$[g(V, T)]_a^b = \int_a^b T g(V, T)\, dt = \int_a^b g(\nabla_T V, T)\, dt + \int_a^b g(V, \nabla_T T)\, dt.$$
> > Rearranging:
> > $$\int_a^b g(\nabla_T V, T)\, dt = [g(V, T)]_a^b - \int_a^b g(V, \nabla_T T)\, dt.$$

> [!note]- Lemma 4: Fundamental lemma of the calculus of variations
> **Statement:** If $W$ is a smooth vector field along $\gamma$ such that $\int_a^b g(V, W)\, dt = 0$ for every smooth $V$ along $\gamma$ vanishing at $a$ and $b$, then $W \equiv 0$.
>
> **Hint:** Take $V = f W$ where $f$ is a smooth bump function compactly supported in $(a, b)$.
>
> **Why needed:** Converts the variational integral identity into a pointwise equation.
>
> > [!note]- Full proof
> > Suppose for contradiction that $W(t_0) \neq 0$ at some $t_0 \in (a, b)$. By continuity, $W$ is bounded away from zero on a neighbourhood $(t_0 - \delta, t_0 + \delta)$. Choose a smooth $f \geq 0$ supported in this neighbourhood with $f(t_0) > 0$, and set $V := f \cdot W$. Then $V$ vanishes at $a$ and $b$, and
> > $$\int_a^b g(V, W)\, dt = \int_a^b f \cdot g(W, W)\, dt > 0,$$
> > contradicting the hypothesis.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $\gamma : [a, b] \to M$ be a smooth unit-speed curve. For any smooth variation $\gamma_s$ with variation field $V$,
> $$\frac{d}{ds}\bigg|_0 L(\gamma_s) = -\int_a^b g(V, \nabla_T T)\, dt + [g(V, T)]_a^b.$$
> If $V(a) = V(b) = 0$ (fixed endpoints), then $\frac{d}{ds}|_0 L(\gamma_s) = -\int_a^b g(V, \nabla_T T)\, dt$, and $\gamma$ is a critical point of $L$ for every such $V$ iff $\nabla_T T \equiv 0$.
>
> *Proof.* By Lemma 1, $\frac{d}{ds}|_0 L(\gamma_s) = \int_a^b \frac{g(\nabla_{\partial_s}\partial_t \Gamma, \partial_t \Gamma)}{|\partial_t \Gamma|}|_{s=0}\, dt$. For unit-speed $\gamma$, $|\partial_t \Gamma||_{s=0} = 1$, so this is $\int_a^b g(\nabla_{\partial_s}T, T)\, dt$.
>
> By Lemma 2, $\nabla_{\partial_s}\partial_t \Gamma = \nabla_{\partial_t}\partial_s \Gamma$, so $\nabla_{\partial_s}T|_{s=0} = \nabla_T V$. The integrand becomes $g(\nabla_T V, T)$.
>
> By Lemma 3, integration by parts gives
> $$\int_a^b g(\nabla_T V, T)\, dt = [g(V, T)]_a^b - \int_a^b g(V, \nabla_T T)\, dt.$$
> So $\frac{d}{ds}|_0 L(\gamma_s) = -\int_a^b g(V, \nabla_T T)\, dt + [g(V, T)]_a^b$, as claimed.
>
> For fixed-endpoint variations, the boundary term vanishes. Criticality (the derivative is zero for *every* $V$ with $V(a) = V(b) = 0$) then becomes $\int_a^b g(V, \nabla_T T)\, dt = 0$ for every such $V$. By Lemma 4 applied with $W := \nabla_T T$, this forces $\nabla_T T \equiv 0$ — i.e., $\gamma$ is a geodesic. The converse is immediate. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Classical mechanics: Lagrange's equations from Hamilton's principle.** Given a Lagrangian $L(q, \dot q, t)$ on $TM \times \mathbb{R}$, Hamilton's principle says that physical trajectories extremise $\int L\, dt$ with fixed endpoints. The first-variation calculation (formally identical to the first variation of arc length) produces the **Euler–Lagrange equations** $\frac{d}{dt}\frac{\partial L}{\partial \dot q^k} = \frac{\partial L}{\partial q^k}$, the equations of motion of classical mechanics. The geodesic case is $L = T = \tfrac12 g_{ij}\dot q^i \dot q^j$, and the Euler–Lagrange equations specialise to the geodesic equation. See [[Thm - Hamilton's Principle Gives the Geodesic Equation]].

**Optics: Fermat's principle.** Light rays in an inhomogeneous optical medium follow paths that extremise the *optical length* $\int n(\mathbf x)\, ds$, where $n$ is the index of refraction. Treating this as a length functional with metric $g = n^2 \delta$, the geodesic equation gives Snell's law and the equations of geometric optics. So Fermat's principle is the first-variation formula applied to the optical metric — geometric optics is a special case of Riemannian geometry.

**General relativity: timelike geodesics of free fall.** In a Lorentzian spacetime, free-falling massive particles follow timelike geodesics extremising the proper time $\tau = \int \sqrt{-g(\dot\gamma, \dot\gamma)}\, dt$. The first variation gives the geodesic equation $\nabla_{\dot\gamma}\dot\gamma = 0$, the equation of motion of free fall. The variational characterisation in GR is *maximisation* of proper time (for timelike geodesics in Lorentzian signature — the sign of the metric flips the extremum direction).

**Calculus of variations: Euler's brachistochrone problem.** The brachistochrone problem (find the curve of fastest descent) is a variational problem of finding the extremiser of a functional $\int f(x, y, y')\, dx$. The Euler–Lagrange equation derived from the first variation is the standard tool of the calculus of variations, and the answer (the cycloid) is the geodesic of a particular conformally rescaled metric on the upper half-plane. The first variation formula in Riemannian geometry generalises the historic first variation calculations of Euler and Lagrange.

---

# Bridges

- **[[Def - Length and Energy Functionals|Length and Energy]]** — the functionals being varied. The first variation formula tells us that critical points of $L$ are unparametrised geodesics, and of $E$ are parametrised (constant-speed) geodesics. The two functionals are linked by Cauchy–Schwarz, and the first variation analysis is one of the cleanest cases of "the variation of an action functional gives the equation of motion".

- **[[Thm - Second Variation of Arc Length|Second Variation of Arc Length]]** — the direct sequel. Once we know geodesics are critical points, the second variation classifies the type of critical point: positive-definite Hessian ⟹ local minimum, indefinite Hessian ⟹ saddle, etc. The Hessian is the [[Def - The Index Form|index form]] $I$, and conjugate points are the places where it becomes degenerate. The first variation identifies *what* is critical; the second variation classifies *how* it is critical.

- **[[Thm - Hamilton's Principle Gives the Geodesic Equation|Hamilton's Principle]]** — the mechanics version. The Euler–Lagrange equations of the Lagrangian $L(q, \dot q) = \tfrac12 g_{ij}\dot q^i \dot q^j$ are the geodesic equation; this is the first variation of $E$ written in coordinates. The first variation formula in Riemannian geometry and Hamilton's principle in classical mechanics are the *same* calculation, applied in different settings.

- **The Euler–Lagrange equations for higher-dimensional variational problems** — the generalisation. For maps $\varphi : (N, h) \to (M, g)$ instead of curves, the energy functional $E(\varphi) = \tfrac12 \int_N |d\varphi|^2\, \mathrm{vol}_h$ has Euler–Lagrange equation $\tau(\varphi) = 0$ where $\tau$ is the **tension field** — the higher-dimensional analogue of $\nabla_T T$. Critical points are **harmonic maps**, generalising geodesics ($N = \mathbb{R}$). The first variation formula in the curve case is the prototype.

---

# Unlocked by This

> [!tip] The Second Variation and the Index Form *(from Riemannian Geometry)*
> Once we know geodesics are critical points of $L$, the next step is the second variation — the Hessian of $L$ at a geodesic. This produces the **index form** $I(V, W) = \int g(V', W') - g(R(V, T)T, W)$ on normal variations, whose signature determines the local-minimisation properties of $\gamma$. See [[Thm - Second Variation of Arc Length]] and [[Def - The Index Form]].

> [!tip] **Noether's Theorem for Geodesic Flow** *(from Geometric Mechanics)*
> Every continuous symmetry of the metric (i.e., every Killing field $X$) gives a conserved quantity along geodesics: the function $g(\dot\gamma, X)$ is constant along $\gamma$. The proof is a direct application of the first variation formula. This is the geometric origin of conservation of energy, momentum, and angular momentum in classical mechanics.

> [!tip] **Existence of Closed Geodesics via Minimax** *(from Morse Theory)*
> The energy functional on the loop space of $M$ has, by the first variation formula, critical points that are exactly the closed geodesics. **Ljusternik–Fet's theorem** (1951) says that every compact Riemannian manifold has at least one closed geodesic, proved by minimax over the loop space using the Morse theory of the energy functional. The first variation is the input to this existence theorem.

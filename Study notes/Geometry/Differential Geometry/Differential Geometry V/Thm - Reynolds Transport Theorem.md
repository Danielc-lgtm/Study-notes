---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Flow of a Vector Field"
  - "Def - Vector Field on a Manifold"
  - "Def - Lie Derivative of a Vector Field"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Lie Derivative of a Differential Form"
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Thm - Cartan's Magic Formula"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, differential-geometry, fluid-mechanics, transport]
---

# Notation

$M$ is a smooth manifold and $X \in \mathfrak{X}(M)$ is a smooth vector field on $M$. The [[Def - Flow of a Vector Field|flow]] of $X$ is denoted $\phi_t : M \to M$, defined where the flow exists (an open subset of $\mathbb{R} \times M$; complete if $X$ has compact support, see [[Def - Complete Vector Field]]). For a compact oriented $p$-dimensional submanifold $D \subseteq M$ with boundary $\partial D$ (possibly empty), $\phi_t(D)$ denotes the image of $D$ under the time-$t$ flow — a moving submanifold, the same shape as $D$ at $t = 0$ but displaced and possibly distorted by the flow.

For a smooth $p$-form $\omega \in \Omega^p(M)$, $\mathcal{L}_X\omega \in \Omega^p(M)$ is the [[Def - Lie Derivative of a Differential Form|Lie derivative]], and $\iota_X\omega \in \Omega^{p-1}(M)$ is the [[Def - Interior Product (Contraction with a Vector Field)|interior product]]; they are related by [[Thm - Cartan's Magic Formula|Cartan's magic formula]] $\mathcal{L}_X = d\iota_X + \iota_X d$.

In the time-dependent case, $X(t, \cdot) \in \mathfrak{X}(M)$ is a smooth time-dependent vector field, and $\phi_t$ is the corresponding (in general not group-like) family of diffeomorphisms determined by $d\phi_t(p)/dt = X(t, \phi_t(p))$, $\phi_0 = \mathrm{id}$. Forms are also allowed to depend on time: $\omega_t \in \Omega^p(M)$.

In the fluid-mechanics specialization on $\mathbb{R}^3$, $\vec u(t, \vec x)$ is the (time-dependent) velocity field, $f(t, \vec x)$ is a scalar density (mass per unit volume, energy density, etc.), $V(t) \subseteq \mathbb{R}^3$ is a "material volume" — the time-$t$ image of an initial volume $V(0)$ under the fluid flow — and $\partial V(t)$ is its boundary. $dV = dx \wedge dy \wedge dz$ is the Euclidean volume $3$-form, $d\vec A$ is the outward-oriented area $2$-form on $\partial V(t)$, and $\nabla\cdot(\,\cdot\,)$ is the [[Ex - The Exterior Derivative on R^3 Recovers Grad-Curl-Div|divergence]] (the form-language counterpart of $d$ acting on a $2$-form).

The full notation registry for this topic is on [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]].

---

# Statement

> **Theorem (Reynolds Transport — Autonomous Form).** Let $M$ be a smooth manifold, $X$ a smooth vector field on $M$ with flow $\phi_t$, and $D \subseteq M$ a compact oriented $p$-dimensional submanifold (possibly with boundary). Let $\omega \in \Omega^p(M)$ be a smooth $p$-form. Then for $t$ small enough that the flow exists on a neighborhood of $D$,
> $$\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_{\phi_t(D)}\mathcal{L}_X\omega.$$
> Equivalently, using Cartan's magic formula,
> $$\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_{\phi_t(D)}(\iota_X\,d\omega + d\,\iota_X\omega) = \int_{\phi_t(D)}\iota_X\,d\omega + \int_{\partial\phi_t(D)}\iota_X\omega.$$

> **Theorem (Reynolds Transport — Time-Dependent Form).** Let $\phi_t$ be a smooth isotopy with $\phi_0=\mathrm{id}$, defined on a neighbourhood of compact $D$, and let its Eulerian velocity be $X_t=\dot\phi_t\circ\phi_t^{-1}$. For a smooth family $\omega_t\in\Omega^p(M)$,
> $$\frac{d}{dt}\int_{\phi_t(D)}\omega_t = \int_{\phi_t(D)}\left(\frac{\partial \omega_t}{\partial t} + \mathcal{L}_{X(t,\cdot)}\omega_t\right).$$

> **Corollary (Classical Reynolds Transport on $\mathbb{R}^3$).** Let $\vec u(t, \vec x)$ be a smooth time-dependent velocity field on $\mathbb{R}^3$, $V(t)$ a material volume transported by $\vec u$, and $f(t, \vec x)$ a smooth scalar density. Then
> $$\frac{d}{dt}\int_{V(t)}f\,dV = \int_{V(t)}\frac{\partial f}{\partial t}\,dV + \int_{\partial V(t)}f\,\vec u\cdot d\vec A = \int_{V(t)}\left(\frac{\partial f}{\partial t} + \nabla\cdot(f\vec u)\right)dV.$$
> The two equivalent forms are the **convective** and **divergence** forms of the classical transport theorem, used in fluid mechanics, continuum mechanics, and conservation laws.

---

# Motivation

This theorem solves a problem that lies at the intersection of fluid mechanics, kinetic theory, and the differential geometry of integration: *how does an integral change when both the integrand and the region of integration depend on time?* In the static case — a fixed region, fixed integrand — the integral is a number, and there is nothing to compute. In one of the two time-dependent cases (the region moves but the integrand is fixed, or the region is fixed but the integrand moves), there is a single source of $t$-dependence, and the answer can be obtained by ordinary differentiation. But when *both* the region and the integrand depend on time, neither of the obvious answers ($\int \partial_t\omega$ or "boundary flux") is correct individually — the right answer is a combination of the two, and getting the combination right is exactly what Reynolds's theorem provides.

The reason this theorem matters far beyond fluid mechanics is that the question "rate of change of an integral over a moving region" is the *fundamental* question of conservation laws. Almost every conservation law in physics is a statement of the form "the rate of change of (some quantity) inside a material volume equals (some source or boundary flux)" — conservation of mass, momentum, energy, charge, entropy. The Reynolds Transport Theorem is the geometric identity that lets you derive the *local* (differential) form of the conservation law from the *global* (integral) form. Continuity equation, Navier–Stokes, the energy equation in continuum mechanics, the Vlasov equation in kinetic theory, Faraday's law in electromagnetism — every one of them comes from Reynolds's theorem applied to a specific form on a specific moving region.

The form-language version of the theorem, $\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_{\phi_t(D)}\mathcal{L}_X\omega$, is striking in its compactness. It says: the Lie derivative $\mathcal{L}_X\omega$ is *literally* the rate at which an integral of $\omega$ over a flowing region changes, normalized per unit volume. So $\mathcal{L}_X\omega = 0$ is the geometric definition of "$\omega$ is invariant under the flow generated by $X$" — and the theorem makes precise what invariance means for an integrated quantity rather than a pointwise one. This is the conceptual upgrade over the pointwise definition of $\mathcal{L}_X$ as a limit of differences: from "infinitesimal change of $\omega$ at a point" to "rate of change of integrated $\omega$ over a moving region."

The proof technique itself — pull back to the time-$0$ region, differentiate inside the integral, recognize the time derivative as the Lie derivative — is a template that applies far beyond this specific identity. Whenever one needs to differentiate something "along a flow" (a variational formula in geometric mechanics, the conservation of a Hamiltonian, the variation of the Einstein–Hilbert action), the same three-step pattern (pull back, differentiate, recognize) works. So this theorem is also a methodological centerpiece.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypotheses Reynolds's theorem demands are mild — a smooth vector field, a compact submanifold, a smooth form — and almost any setup in continuum mechanics or geometric integration delivers them. The skill is recognizing the disguised hypotheses in problems that mention no submanifold or flow.

The most common source is **a velocity field plus an initial region**. Property $B$ is "you are given a smooth velocity field $\vec u(t, \vec x)$ on a region and an initial region $V_0$." The bridge: the time-$t$ image $V(t) = \phi_t(V_0)$ is automatically a compact submanifold transported by the flow of $\vec u$. The implication "velocity field $\implies$ flow $\implies$ moving region" is unconscious for anyone who knows ODE theory, but it is the bridge that lets the theorem apply. Concrete example: in fluid mechanics, you are given $\vec u$ and asked about the rate of change of mass / momentum / energy inside a moving "material" parcel. Reynolds's theorem applies directly.

A second source is **a one-parameter family of diffeomorphisms**. Property $B$ is "you have a smooth one-parameter family $\phi_t : M \to M$ with $\phi_0 = \mathrm{id}$." The bridge: differentiate to get $X(t, \cdot) := d\phi_t/dt \circ \phi_t^{-1}$ (or in the autonomous case $X = d\phi_t/dt|_{t=0}$). Once you have $X$, you have the hypothesis of Reynolds's theorem. The implication is non-obvious because the family $\phi_t$ might not look like a flow at first — it might be a parametric family of deformations of a region in mechanics, or a homotopy of embeddings in geometry. Concrete example: the **second variation of arc length** in Riemannian geometry differentiates the length integral twice along a variational family of curves, and the first variation is exactly Reynolds's theorem applied to the arc-length form. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket#Most Reusable Properties|Most Reusable Properties]] for the variational pattern.

A third source is **conservation in integral form**. Property $B$ is "a physical conservation law in integral form, $\frac{d}{dt}\int_{V(t)} q = -\int_{\partial V(t)} \vec F \cdot d\vec A$ (or with a source term)." The bridge: by Reynolds's theorem applied to $q\,dV$, the left side equals $\int_{V(t)}(\partial_t q + \nabla\cdot(q\vec u))\,dV$; by the divergence theorem, the right side equals $-\int_{V(t)} \nabla\cdot\vec F\,dV$. Setting the integrands equal — using that $V(t)$ is arbitrary — gives the local form $\partial_t q + \nabla\cdot(q\vec u + \vec F) = 0$. So the source-target route "integral conservation law $\to$ Reynolds $\to$ local PDE" is the standard derivation of the **continuity equation**, **conservation of momentum** (Cauchy's first law), and **conservation of energy**.

A fourth source is **a closed form on a closed manifold**. Property $B$ is "$\omega$ is closed ($d\omega = 0$) and $D$ is a closed manifold ($\partial D = \emptyset$)." The bridge: applying Cartan's magic formula, $\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_{\phi_t(D)}(\iota_X d\omega + d\iota_X\omega) = 0 + \int_{\partial D}\iota_X\omega = 0$. So the integral is *constant* in time — *for every* vector field $X$ and every region $D$. This is how one proves that periods of closed forms are flow-invariant, which is the key to **Liouville's theorem** in classical mechanics and to the homotopy invariance of de Rham cohomology.

**Targets (Output Amplification)**

The conclusion Reynolds's theorem delivers is the identity $\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_{\phi_t(D)}\mathcal{L}_X\omega$. By itself this is just a chain rule. Combined with one further fact it becomes a powerful tool.

The most powerful combination is **Reynolds plus arbitrariness of $V$ gives a local PDE**. Take the conclusion in the form $\frac{d}{dt}\int_{V(t)} q\,dV = \int_{V(t)}(\partial_t q + \nabla\cdot(q\vec u))\,dV$ (property $C$). Combine with property $D$: an integral conservation law $\frac{d}{dt}\int_{V(t)} q\,dV = 0$ (no source). Then $\int_{V(t)}(\partial_t q + \nabla\cdot(q\vec u))\,dV = 0$ for *every* $V(t)$, and since the integrand is continuous, it must vanish pointwise: $\partial_t q + \nabla\cdot(q\vec u) = 0$. The result $E$ is the **continuity equation**, and the localization step — "since the integral vanishes for all $V$, the integrand vanishes" — is one of the most important moves in continuum mechanics. The combination is nonobvious because a global integral identity does not look like it should give a local PDE, but the arbitrariness of $V$ is exactly what unlocks the localization.

A second combination is **Reynolds plus incompressibility gives the convective derivative**. Take Reynolds applied to a scalar density $f$ in the form $\frac{d}{dt}\int_{V(t)} f\,dV = \int_{V(t)}(\partial_t f + \nabla\cdot(f\vec u))\,dV$. Combine with property $D$: incompressibility $\nabla\cdot\vec u = 0$. Then $\nabla\cdot(f\vec u) = f\nabla\cdot\vec u + \vec u\cdot\nabla f = \vec u\cdot\nabla f$, so the right side is $\int_{V(t)}(\partial_t f + \vec u\cdot\nabla f)\,dV = \int_{V(t)} Df/Dt\,dV$, where $Df/Dt := \partial_t f + \vec u\cdot\nabla f$ is the **material** or **convective derivative**. The result $E$ is that for incompressible flow, the integrated rate-of-change is the integral of the convective derivative — the "rate of change following the fluid parcel." This is the clean way to write the energy equation, the heat equation in a moving frame, and the kinetic theory's Vlasov equation.

A third combination is **Reynolds plus closedness gives flow-invariance of periods**. Take Reynolds for a closed form $\omega$ on a closed manifold $D$ (property $C$: $d\omega = 0$, $\partial D = \emptyset$). Combine with property $D$: any homotopy of $D$ given by a flow $\phi_t$. Then $\int_{\phi_t(D)}\omega = \int_D\omega$ for all $t$: the period is constant. The result $E$ is the **homotopy invariance of integrals of closed forms**, which is the geometric basis of de Rham cohomology. The combination is nonobvious because "homotopy invariance" is a topological statement and Reynolds's theorem is differential — but they are the same statement, with Reynolds providing the infinitesimal version that integrates to homotopy invariance.

A fourth combination is **Reynolds plus a Hamiltonian gives Liouville's theorem**. Take Reynolds for the symplectic volume $\omega^n/n!$ on a $2n$-dimensional phase space, with $X = X_H$ the Hamiltonian vector field generated by $H$. Then $\mathcal{L}_{X_H}(\omega^n/n!) = n\,\omega^{n-1}\wedge\mathcal{L}_{X_H}\omega / n!$, and Cartan's formula plus $\mathcal{L}_{X_H}\omega = d\iota_{X_H}\omega = ddH = 0$ gives $\mathcal{L}_{X_H}(\omega^n) = 0$. Reynolds then says $\frac{d}{dt}\int_{\phi_t(V)}\omega^n/n! = 0$ for every region $V$ — **phase-space volume is conserved**, which is Liouville's theorem in symplectic geometry. The combination is nonobvious because "Hamiltonian" and "volume" don't seem related, but symplectic-form invariance under the Hamiltonian flow is exactly Reynolds-plus-Hamilton.

---

# Why Is It True

The intuition is a single picture. **A flowing region "carries" the form along with it; the integral changes only because the form itself changes along the flow — and the rate of change along the flow is, by definition, the Lie derivative.**

Concretely: pretend, just for one paragraph, that the form $\omega$ is constant along the flow ($\mathcal{L}_X\omega = 0$). Then as the region $D$ moves to $\phi_t(D)$, every infinitesimal piece of $D$ carries its piece of $\omega$ with it — the form is "carried along by the flow" — and the integral $\int_{\phi_t(D)}\omega$ does not change at all. The integral is just a sum, and we are merely relabelling which infinitesimal piece is contributing at time $t$. Constant under flow means constant integral. This is the case where Reynolds's theorem gives $0 = 0$.

Now consider the general case where $\omega$ is not flow-invariant. The integral $\int_{\phi_t(D)}\omega$ changes for exactly *one* reason: as the region moves, it encounters values of $\omega$ at points it could not have reached without flowing. The "amount by which $\omega$ has changed in the time $t$" at a point $\phi_t(p)$, as seen from the perspective of an observer riding along the flow from $p$, is precisely the Lie derivative $\mathcal{L}_X\omega$ evaluated along the orbit. The integral's rate of change is just the integral of this rate-of-change.

**The mechanism in one line: pullback brings the moving integral back to a fixed region, the chain rule passes the time derivative inside, and what comes out is the Lie derivative by its definition.**

This is also the *cleanest* way to see why the Lie derivative was defined the way it was. The original definition of $\mathcal{L}_X\omega$ is the pointwise limit $\mathcal{L}_X\omega = \lim_{t\to 0}\frac{\phi_t^*\omega - \omega}{t}$. Reynolds's theorem says: integrate both sides over $D$ and you get the rate of change of the integral. So the Lie derivative is not just a pointwise gadget; it is *literally the rate of change of integrated quantities along the flow*. The pointwise definition was just the pointwise content of the integrated identity.

The time-dependent version is the same picture with one extra term: the form itself changes in time (not just under the flow), so the integrand changes for an additional reason. The two contributions add: $\partial\omega/\partial t$ (explicit time dependence) plus $\mathcal{L}_{X(t,\cdot)}\omega$ (change-along-the-flow). This is the same chain-rule decomposition as the classical "total derivative = partial derivative + convective derivative" of fluid mechanics, just lifted to forms on a manifold.

The classical specialization on $\mathbb{R}^3$ uses Cartan's formula: $\mathcal{L}_X(f\,dV) = d(\iota_X(f\,dV)) + \iota_X d(f\,dV)$. The second term is zero because $d(f\,dV) = 0$ (the volume form is the top form on $\mathbb{R}^3$). The first term unpacks via the divergence formula: $\iota_X(f\,dV)$ is the "flux" $2$-form $f\vec u\cdot d\vec A$, and $d$ applied to it gives $\nabla\cdot(f\vec u)\,dV$. Together with $\partial f/\partial t\,dV$ this is the classical Reynolds Transport identity. The geometric content of the divergence is exactly "rate at which volume changes under the flow," which is the same Lie-derivative content as the general theorem.

---

# What Makes This Hard

The single hardest step is realizing that the time derivative of $\int_{\phi_t(D)}\omega$ is *not* the integral of $\partial\omega/\partial t$ — the region's motion contributes a separate term that one must not forget. The most common error in fluid mechanics is to apply $\partial/\partial t$ inside the integral without accounting for the moving boundary, missing the convective term $\nabla\cdot(f\vec u)$ or the boundary-flux term $f\vec u\cdot d\vec A$. The second common error is to mix up the two equivalent forms (convective vs divergence) and write $\partial f/\partial t + f\nabla\cdot\vec u$ instead of $\partial f/\partial t + \nabla\cdot(f\vec u)$, missing the cross-term $\vec u\cdot\nabla f$. Both errors disappear once one writes the theorem in the form-language version: Lie derivatives carry all the necessary corrections automatically.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Pull the moving integral back to the fixed initial region using $\phi_t^*$, pass the time derivative inside the (now-fixed) integral, recognize the result as the Lie derivative by its definition, then push forward by $\phi_t$ to write the answer as an integral over the current region. Three steps, each a single line.

**Subgoal decomposition:**

1. **Pull back to the initial region.** Show $\int_{\phi_t(D)}\omega = \int_D \phi_t^*\omega$ for every $t$.
   - *Hint:* This is the change-of-variables formula for forms ([[Thm - Change of Variables for Integration on Manifolds]]) applied to the diffeomorphism $\phi_t : D \to \phi_t(D)$.
   - *Why needed:* The right side has a *fixed* domain of integration, so the $t$-derivative passes inside the integral.

2. **Differentiate inside.** Show $\frac{d}{dt}\int_D\phi_t^*\omega = \int_D\frac{d}{dt}\phi_t^*\omega$.
   - *Hint:* Standard differentiation-under-the-integral, valid because $\phi_t^*\omega$ is smooth jointly in $(t, p)$ and $D$ is compact.
   - *Why needed:* Brings the time derivative onto the form, where it becomes a Lie derivative.

3. **Recognize the Lie derivative.** Show $\frac{d}{dt}\phi_t^*\omega = \phi_t^*(\mathcal{L}_X\omega)$.
   - *Hint:* This is one of the equivalent definitions of $\mathcal{L}_X\omega$: $\mathcal{L}_X\omega = \frac{d}{dt}\phi_t^*\omega|_{t=0}$, extended to general $t$ by the group property of the flow ($\phi_{t+s} = \phi_t \circ \phi_s$).
   - *Why needed:* This is what converts the time derivative into the geometric object $\mathcal{L}_X$.

4. **Push forward.** Conclude $\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_D\phi_t^*\mathcal{L}_X\omega = \int_{\phi_t(D)}\mathcal{L}_X\omega$.
   - *Hint:* Change of variables in reverse — the same identity as Step 1, now with $\mathcal{L}_X\omega$ in place of $\omega$.
   - *Why needed:* Gives the statement in the natural form, integrating over the *current* region.

5. **(Time-dependent extension.)** If $\omega = \omega_t$ depends on time, repeat with $\phi_t^*\omega_t$, expand $\frac{d}{dt}\phi_t^*\omega_t = \phi_t^*(\partial\omega_t/\partial t) + \phi_t^*\mathcal{L}_{X(t,\cdot)}\omega_t$, push forward.
   - *Hint:* The chain rule for the time derivative of the composition.
   - *Why needed:* Gives the form with the extra $\partial\omega/\partial t$ term.

6. **(Classical specialization.)** Apply to $\omega = f\,dV$ on $\mathbb{R}^3$, use $\mathcal{L}_{\vec u}(f\,dV) = (\partial_t f + \nabla\cdot(f\vec u))\,dV$ (a Cartan-magic-formula computation), and apply the divergence theorem to get the boundary-flux form.
   - *Hint:* $\mathcal{L}_{\vec u}(f\,dV) = d\iota_{\vec u}(f\,dV) + \iota_{\vec u}d(f\,dV)$; the second term vanishes (top form), and $d\iota_{\vec u}(f\,dV) = d(f\vec u^\flat\cdot d\vec A)$ is $\nabla\cdot(f\vec u)\,dV$.
   - *Why needed:* Translates the geometric statement into the standard fluid-mechanics formula.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

> [!note]- Lemma 1: Change-of-variables for the moving integral
> **Statement:** For a diffeomorphism $\phi_t : D \to \phi_t(D)$ (orientation-preserving, which is automatic for a flow continuous in $t$ with $\phi_0 = \mathrm{id}$), $\int_{\phi_t(D)}\omega = \int_D \phi_t^*\omega$.
>
> **Hint:** This is [[Thm - Change of Variables for Integration on Manifolds]]: the integral is invariant under pullback by an orientation-preserving diffeomorphism.
>
> **Why needed:** Converts the moving region $\phi_t(D)$ to the fixed region $D$, with the time-dependence now sitting on the form $\phi_t^*\omega$. Once the domain is fixed, the $t$-derivative passes inside.
>
> > [!note]- Full proof
> > Since $\phi_t : M \to M$ is a smooth flow (the time-$t$ stage), it is in particular a diffeomorphism on its domain of definition. Restricted to $D$, it is an orientation-preserving diffeomorphism $D \to \phi_t(D)$ — orientation-preserving because $\phi_0 = \mathrm{id}$ preserves orientation, and by continuity $\det D\phi_t > 0$ for all sufficiently small $t$ (the determinant of $D\phi_t$ is a continuous function of $t$ and is $+1$ at $t = 0$, so it stays positive).
> >
> > By the change-of-variables formula for integration of forms on manifolds (applied to $\phi_t$),
> > $$\int_{\phi_t(D)}\omega = \int_D\phi_t^*\omega.$$
> > This holds for every smooth $p$-form $\omega$ and every compact oriented $p$-dimensional submanifold $D$.

> [!note]- Lemma 2: Pullback derivative is the Lie derivative
> **Statement:** $\frac{d}{dt}\phi_t^*\omega = \phi_t^*(\mathcal{L}_X\omega)$ for all $t$ in the flow domain.
>
> **Hint:** Use the group property $\phi_{t+s} = \phi_t \circ \phi_s$ to reduce to $s = 0$, then use the definition $\mathcal{L}_X\omega = \frac{d}{ds}\phi_s^*\omega|_{s=0}$.
>
> **Why needed:** This is the central identity converting the time derivative of a pulled-back form into the geometric Lie derivative. Without it, the proof has no way to express its conclusion in the natural form.
>
> > [!note]- Full proof
> > The flow satisfies $\phi_{t+s} = \phi_t \circ \phi_s$ wherever both sides are defined. Pulling back gives $\phi_{t+s}^*\omega = \phi_s^*\phi_t^*\omega$, so
> > $$\frac{d}{dt}\phi_t^*\omega = \lim_{s\to 0}\frac{\phi_{t+s}^*\omega - \phi_t^*\omega}{s} = \lim_{s\to 0}\frac{\phi_s^*(\phi_t^*\omega) - \phi_t^*\omega}{s} = \mathcal{L}_X(\phi_t^*\omega),$$
> > by the definition $\mathcal{L}_X\eta := \lim_{s\to 0}(\phi_s^*\eta - \eta)/s$.
> >
> > Finally, because the Lie derivative is natural under diffeomorphisms — $\mathcal{L}_X(\phi_t^*\omega) = \phi_t^*(\mathcal{L}_X\omega)$ — we get $\frac{d}{dt}\phi_t^*\omega = \phi_t^*(\mathcal{L}_X\omega)$. (The naturality holds because the flow of $X$ commutes with $\phi_t^*$: pulling back by $\phi_t$ takes the flow of $X$ to itself.)

> [!note]- Lemma 3: Cartan's formula on a top-form
> **Statement:** For a smooth scalar $f \in C^\infty(\mathbb{R}^3)$ and the Euclidean volume $dV = dx\wedge dy\wedge dz$, $\mathcal{L}_{\vec u}(f\,dV) = (\vec u\cdot\nabla f + f\nabla\cdot\vec u)\,dV = \nabla\cdot(f\vec u)\,dV$.
>
> **Hint:** Apply Cartan's magic formula $\mathcal{L}_X = d\iota_X + \iota_X d$. The second term vanishes because $d(f\,dV) = 0$ (top-degree). The first term: $\iota_{\vec u}(f\,dV) = f(\iota_{\vec u}dV) = f\vec u^\flat$ in the flux-$2$-form sense, and $d(f\iota_{\vec u}dV) = (\nabla\cdot(f\vec u))\,dV$ by the divergence-as-$d$-of-$2$-form identity from the [[Def - Frankel Dictionary (Forms vs Vector Calculus)|Frankel dictionary]].
>
> **Why needed:** Specializes the abstract $\mathcal{L}_X$ on a $3$-manifold to the classical divergence formula in $\mathbb{R}^3$, which is what produces the classical Reynolds Transport Theorem.
>
> > [!note]- Full proof
> > By Cartan's magic formula, $\mathcal{L}_{\vec u}(f\,dV) = d(\iota_{\vec u}(f\,dV)) + \iota_{\vec u}(d(f\,dV))$.
> >
> > The form $f\,dV$ is a $3$-form on the $3$-manifold $\mathbb{R}^3$, so $d(f\,dV) \in \Omega^4(\mathbb{R}^3) = 0$. The second term vanishes.
> >
> > For the first term, $\iota_{\vec u}(f\,dV) = f(\iota_{\vec u}\,dV)$ by $C^\infty$-linearity of $\iota_{\vec u}$ in its form-argument. The contraction $\iota_{\vec u}\,dV$ in coordinates: writing $\vec u = u^i\partial_i$, $\iota_{\vec u}(dx\wedge dy\wedge dz) = u^1\,dy\wedge dz + u^2\,dz\wedge dx + u^3\,dx\wedge dy$. This is the flux $2$-form $\vec u^\flat\cdot d\vec A$ in the [[Def - Frankel Dictionary (Forms vs Vector Calculus)|Frankel dictionary]].
> >
> > Then $d(f\iota_{\vec u}\,dV) = \sum_i d(fu^i\,\widehat{dx^i})$ where $\widehat{dx^i}$ denotes the standard $2$-form missing the $i$-th coordinate. Each summand is $\partial_j(fu^i)\,dx^j\wedge \widehat{dx^i}$, which for $j = i$ gives $\partial_i(fu^i)\,dV$ (and vanishes for $j \neq i$ by antisymmetry of $\wedge$). Summing, $d(f\iota_{\vec u}\,dV) = (\sum_i\partial_i(fu^i))\,dV = \nabla\cdot(f\vec u)\,dV$.
> >
> > Equivalently, $\nabla\cdot(f\vec u) = \vec u\cdot\nabla f + f\nabla\cdot\vec u$ by the product rule.

---

# Formal Proof

> [!note]- Complete formal proof
> *Proof of the autonomous form.* By the change-of-variables formula for integration on manifolds (Lemma 1), $\int_{\phi_t(D)}\omega = \int_D\phi_t^*\omega$. The right side has $D$ as a fixed compact domain, and $\phi_t^*\omega$ depends smoothly on $t$, so by differentiation under the integral,
> $$\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_D\frac{d}{dt}\phi_t^*\omega.$$
> By Lemma 2, $\frac{d}{dt}\phi_t^*\omega = \phi_t^*(\mathcal{L}_X\omega)$. Substituting,
> $$\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_D\phi_t^*(\mathcal{L}_X\omega) = \int_{\phi_t(D)}\mathcal{L}_X\omega,$$
> by the change-of-variables formula applied in reverse to the form $\mathcal{L}_X\omega$.
>
> The equivalent form $\int_{\phi_t(D)}\iota_X d\omega + \int_{\partial\phi_t(D)}\iota_X\omega$ follows from Cartan's magic formula $\mathcal{L}_X = d\iota_X + \iota_X d$ and Stokes's theorem applied to the term $\int_{\phi_t(D)}d\iota_X\omega = \int_{\partial\phi_t(D)}\iota_X\omega$.
>
> *Proof of the time-dependent form.* Replace $\omega$ by $\omega_t$ throughout. Lemma 1 still gives $\int_{\phi_t(D)}\omega_t = \int_D\phi_t^*\omega_t$. Differentiation now uses the chain rule:
> $$\frac{d}{dt}\phi_t^*\omega_t = \phi_t^*\left(\frac{\partial\omega_t}{\partial t}\right) + \phi_t^*(\mathcal{L}_{X(t,\cdot)}\omega_t).$$
> The first term comes from the explicit $t$-dependence of $\omega_t$; the second comes from the $t$-dependence of $\phi_t$ via Lemma 2 (extended to the time-dependent flow). Pushing forward and using change-of-variables in reverse,
> $$\frac{d}{dt}\int_{\phi_t(D)}\omega_t = \int_{\phi_t(D)}\left(\frac{\partial\omega_t}{\partial t} + \mathcal{L}_{X(t,\cdot)}\omega_t\right). \qquad\blacksquare$$
>
> *Proof of the classical $\mathbb{R}^3$ corollary.* Apply the time-dependent form to $\omega_t = f(t, \vec x)\,dV$ on $\mathbb{R}^3$. Then $\partial\omega_t/\partial t = \partial f/\partial t\,dV$ (the volume form itself is time-independent). By Lemma 3, $\mathcal{L}_{\vec u}(f\,dV) = \nabla\cdot(f\vec u)\,dV$. So
> $$\frac{d}{dt}\int_{V(t)}f\,dV = \int_{V(t)}\left(\frac{\partial f}{\partial t}\,dV + \nabla\cdot(f\vec u)\,dV\right) = \int_{V(t)}\left(\frac{\partial f}{\partial t} + \nabla\cdot(f\vec u)\right)dV.$$
> Applying the divergence theorem to the second term gives the boundary-flux form,
> $$\frac{d}{dt}\int_{V(t)}f\,dV = \int_{V(t)}\frac{\partial f}{\partial t}\,dV + \int_{\partial V(t)}f\vec u\cdot d\vec A. \qquad\blacksquare$$

---

# Cross-Field Exercise Suggestions

**Fluid mechanics: derive the continuity equation.** Apply Reynolds's theorem to $f = \rho$, the mass density of a fluid. The conservation of mass says $\frac{d}{dt}\int_{V(t)}\rho\,dV = 0$ (no mass is created or destroyed inside a material volume). By Reynolds, $\int_{V(t)}(\partial_t\rho + \nabla\cdot(\rho\vec u))\,dV = 0$. Since $V(t)$ is arbitrary, $\partial_t\rho + \nabla\cdot(\rho\vec u) = 0$, the **continuity equation** for compressible flow. For incompressible flow ($\nabla\cdot\vec u = 0$), this becomes $D\rho/Dt = 0$ — density is constant along streamlines. This derivation is the standard route into **continuum mechanics** and the **Navier–Stokes equations**.

**Electromagnetism: Faraday's law.** Apply Reynolds to the magnetic flux $2$-form $B$ through a moving surface $S(t) \subseteq \mathbb{R}^3$ in a moving conductor. Reynolds gives $\frac{d}{dt}\int_{S(t)}B = \int_{S(t)}(\partial_t B + \mathcal{L}_{\vec u}B)$, and using Cartan's formula plus $dB = 0$ (no magnetic monopoles), $\mathcal{L}_{\vec u}B = d(\iota_{\vec u}B)$. By Stokes, $\int_{S(t)}d(\iota_{\vec u}B) = \int_{\partial S(t)}\iota_{\vec u}B = -\oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell$ (the $\iota_{\vec u}B$ at a tangent vector unpacks as $-(\vec u\times\vec B)$ via the cross-product/Hodge dictionary). Combining with the differential Faraday law $\partial_t\vec B + \nabla\times\vec E = 0$ recovers the integral Faraday law $\oint_{\partial S(t)}\vec E\cdot d\vec\ell = -\frac{d}{dt}\int_{S(t)}\vec B\cdot d\vec A$ — including the motional EMF term $\vec u\times\vec B$ in moving conductors. See [[Ex - Faraday's Law via Reynolds Transport]].

**Riemannian geometry: first variation of arc length.** For a one-parameter family of curves $\gamma_s : [0, 1] \to (M, g)$ with variation vector field $V$, the arc length $L(s) = \int_0^1|\gamma_s'(t)|\,dt$ has the first variation $\frac{dL}{ds}|_{s=0} = \int_0^1\frac{d}{ds}|\gamma_s'(t)|\,dt$. This is Reynolds's theorem applied to the arc-length $1$-form along curves transported by the variation. The first variation formula in geodesic geometry — that $\gamma$ is a critical point of $L$ iff it satisfies the geodesic equation $\nabla_{\gamma'}\gamma' = 0$ — comes directly from this Reynolds computation. The same pattern produces the **second variation** by applying Reynolds twice. See **Riemannian Geometry II — [[Def - Geodesic|Geodesics]], the Exponential Map, and Variational Principles**.

**Kinetic theory: Vlasov equation.** Apply Reynolds in $6$-dimensional phase space $\mathbb{R}^3_x \times \mathbb{R}^3_v$ to the probability density $f(t, \vec x, \vec v)$ of particles. The phase-space flow is generated by $\vec X = (\vec v, \vec F/m)$ where $\vec F$ is the force. Reynolds plus the conservation of probability gives $\partial_t f + \vec v\cdot\nabla_x f + (\vec F/m)\cdot\nabla_v f = 0$ — the **Vlasov equation**, foundational to plasma physics and stellar dynamics.

---

# Bridges

- **[[Thm - Cartan's Magic Formula]]** — Cartan's formula $\mathcal{L}_X = d\iota_X + \iota_X d$ is exactly what converts the Reynolds Transport identity into its boundary-flux form. The two together give $\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_{\phi_t(D)}\iota_X d\omega + \int_{\partial\phi_t(D)}\iota_X\omega$, separating the "interior change" from the "boundary flux" cleanly. When $\omega$ is closed, the interior term vanishes and Reynolds reduces to Stokes's theorem in disguise — the rate of change of an integrated closed form is purely a boundary phenomenon. This is the geometric origin of the unification of "rate of change" with "flux through a moving boundary" in continuum mechanics.

- **[[Thm - Stokes' Theorem on Manifolds]]** — Reynolds's theorem and Stokes's theorem are dual statements about the boundary operator $\partial$ and the exterior derivative $d$. Stokes's theorem says $\int_M d\omega = \int_{\partial M}\omega$ for a fixed domain; Reynolds's theorem says $\frac{d}{dt}\int_{\phi_t(D)}\omega = \int_{\phi_t(D)}\mathcal{L}_X\omega$ for a flowing domain. Using Cartan's formula, the right-hand side of Reynolds becomes the right-hand side of Stokes plus an "interior production" term, so Reynolds is *Stokes-with-flow* — the moving-boundary generalization of the fundamental theorem of calculus.

- **Liouville's theorem on phase-space volume** — Reynolds's theorem applied to the symplectic volume form $\omega^n/n!$ with $X = X_H$ a Hamiltonian vector field, plus the algebraic fact $\mathcal{L}_{X_H}\omega = 0$, gives $\frac{d}{dt}\int_{\phi_t(V)}\omega^n/n! = 0$ — phase-space volume is conserved by Hamiltonian flow. This is **Liouville's theorem**, the geometric core of statistical mechanics and the foundation of ergodic theory. The proof is one line of Reynolds plus one line of Hamiltonian-flow geometry. See **Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics** and the bridge from there to ergodic theory.

- **The de Rham homotopy formula** — The proof of homotopy invariance of de Rham cohomology constructs a chain homotopy operator $h : \Omega^k(M) \to \Omega^{k-1}(M)$ satisfying $dh + hd = i_1^* - i_0^*$ on a cylinder $M \times [0, 1]$. The construction of $h$ uses Reynolds's theorem on $M \times [0, 1]$ with the trivial flow along the $[0, 1]$ direction, integrating the Lie derivative $\mathcal{L}_{\partial_t}$ from $0$ to $1$. This is the Reynolds-driven proof of [[Thm - Homotopy Invariance of de Rham Cohomology]], and it makes precise that de Rham cohomology is the cohomology of the de Rham complex modulo the equivalence "integrals over homotopic submanifolds agree."

- **Maxwell's equations and forms-treatment of electromagnetism** — Faraday's law in moving conductors uses Reynolds's theorem applied to the magnetic flux $2$-form. This bridges to the full forms-treatment of electromagnetism in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]] (see [[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]]), where the equations $dF = 0$ and $d\star F = J$ are the closed/exact-form statements that Reynolds's theorem integrates against moving surfaces. The motional EMF term — the $\vec u\times\vec B$ contribution — emerges from Reynolds's Lie-derivative term, while the $\partial_t\vec B$ contribution emerges from the explicit time-dependence term. See [[Ex - Faraday's Law via Reynolds Transport]] for the worked example.

---

# Unlocked by This

> [!tip] Continuity Equation and Conservation Laws *(from Continuum Mechanics)*
> Reynolds's theorem is the engine for deriving every local conservation law in continuum mechanics from its integral statement. The **continuity equation** $\partial_t\rho + \nabla\cdot(\rho\vec u) = 0$ (conservation of mass), **Cauchy's first law of motion** $\rho D\vec u/Dt = \nabla\cdot\sigma + \rho\vec f$ (conservation of momentum, with $\sigma$ the stress tensor and $\vec f$ the body force), and the **energy equation** $\rho De/Dt = \sigma:\nabla\vec u - \nabla\cdot\vec q + \rho r$ all come from Reynolds applied to mass density, momentum density, and energy density respectively. The pattern is universal: integral conservation $\to$ Reynolds $\to$ local PDE. This unlocks the entirety of **continuum mechanics** and (in the special case of incompressible viscous flow) the **Navier–Stokes equations**.

> [!tip] Liouville's Theorem in Statistical Mechanics *(from Statistical Mechanics)*
> Reynolds's theorem applied to the Hamiltonian flow on phase space, combined with $\mathcal{L}_{X_H}\omega^n = 0$, gives **Liouville's theorem**: the phase-space volume is conserved under any Hamiltonian flow. This is the foundational geometric input of statistical mechanics — it is why the microcanonical ensemble (uniform measure on the energy surface) is preserved by the dynamics, and why entropy of an isolated Hamiltonian system is constant (the apparent entropy increase in real systems requires coarse-graining or interaction with the environment). The Reynolds-theorem proof is the cleanest derivation and generalizes immediately to Liouville's theorem on the cotangent bundle of any configuration manifold; see **Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics**.

> [!tip] Variational Principles and the Euler–Lagrange Equations *(from Classical Mechanics / Calculus of Variations)*
> The first variation of an action functional $S[\gamma] = \int L\,dt$ along a family of curves is exactly Reynolds's theorem applied to the Lagrangian $1$-form. The vanishing of the first variation gives the **Euler–Lagrange equations**, and this is the geometric reason variational principles produce ODEs of the right form. The same applies to field theories — the variation of $\int\mathcal{L}\,d^4x$ over a moving spacetime region gives the field equations via Reynolds. This is the universal pattern behind classical mechanics, electromagnetism (Maxwell's equations from the Maxwell Lagrangian $-\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu}$), and general relativity (Einstein's equations from the Hilbert action).

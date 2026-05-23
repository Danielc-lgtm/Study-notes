---
type: theorem
subject: general-relativity
prereqs:
  - "Def - The Einstein Field Equations"
  - "Def - The Metric Tensor as Gravitational Potential"
  - "Def - Equivalence Principle"
  - "Def - Stress-Energy Tensor"
tags: [physics, general-relativity, weak-field-limit, classical-mechanics]
---

# Notation

Spacetime $(M, g)$, signature $(+,-,-,-)$. The **weak-field, slow-motion** limit means: write $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h_{\mu\nu}| \ll 1$ (weak field), and matter velocities $|v| \ll c = 1$ (slow motion). The Newtonian gravitational potential is $\phi$ (so that the Newtonian gravitational acceleration is $-\nabla\phi$). Full registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Statement

> **Theorem (Newtonian limit of GR).** In the weak-field, slow-motion limit of general relativity:
>
> (i) **Identification of the Newtonian potential.** With $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ and $|h_{\mu\nu}| \ll 1$, the $(0,0)$ metric component is $g_{00} = -(1 + 2\phi) + O(h^2)$, where $\phi$ is the Newtonian gravitational potential. So $h_{00} = -2\phi$.
>
> (ii) **Geodesic equation reduces to Newton's law of motion.** For a slowly-moving particle ($|v| \ll 1$) in this metric, the timelike geodesic equation $\ddot x^\mu + \Gamma^\mu{}_{\nu\rho} \dot x^\nu \dot x^\rho = 0$ reduces to
> $$\ddot x^\alpha = -\partial^\alpha \phi$$
> (where $\alpha = 1, 2, 3$ is a spatial index and the dot is the time derivative) — Newton's equation of motion in a gravitational field with potential $\phi$.
>
> (iii) **$(0,0)$ Einstein equation reduces to Poisson's equation.** The $G_{00} = 8\pi G T_{00}$ component of the Einstein equations, evaluated in the linearised theory for slow non-relativistic matter ($T_{00} \approx \rho$ the rest-mass density), reduces to
> $$\nabla^2 \phi = 4\pi G \rho.$$
> This is Poisson's equation for the Newtonian potential of a mass density $\rho$ — exactly the Newtonian field equation, with the correct coupling constant.

The factor of $8\pi G$ in the Einstein equations is fixed by demanding this correct Newtonian limit. The theorem establishes that GR contains Newton's gravity exactly as a low-velocity weak-field limit.

---

# Motivation

This theorem is the consistency check that anchors GR to its predecessor. Newton's theory of gravity is extraordinarily successful in the regime of weak fields ($GM/(rc^2) \ll 1$) and slow motion ($v \ll c$) — which covers everyday gravity, planetary motion, satellite orbits, and most astrophysical situations short of compact objects. Any successful relativistic theory of gravity *must* reproduce Newton in this regime; if it didn't, it would conflict with centuries of experimental success of Newtonian gravity.

GR does reproduce Newton, and this theorem makes the reduction explicit. The geodesic equation in the weak-field limit becomes Newton's $\ddot x = -\nabla \phi$, with the identification $g_{00} = -(1 + 2\phi)$. The $(0,0)$ component of the Einstein equation becomes Poisson's $\nabla^2 \phi = 4\pi G \rho$. So Newton's gravitational potential $\phi$ is half the deviation of $g_{00}$ from its Minkowski value, and Newton's Poisson equation is the leading-order GR field equation for $g_{00}$.

The deeper significance is that the Newtonian limit *fixes the coupling constant* in the Einstein equations. If we had written $G_{\mu\nu} = \kappa T_{\mu\nu}$ for some unknown $\kappa$, then the Newtonian limit would give $\nabla^2 \phi = (\kappa/2) \rho$, which matches Newton's $4\pi G \rho$ only if $\kappa = 8\pi G$. So the factor "$8\pi$" in the Einstein equations is forced by the requirement that GR have the correct Newtonian limit — it is not a free choice.

The theorem also identifies $g_{00}$ — one of the ten metric potentials — as the GR generalisation of the single Newtonian potential. The other nine components are "new" in GR (frame dragging, gravitational waves, spatial curvature), but $g_{00}$ has a direct Newtonian counterpart: it is the gravitational potential.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source B₁: Weak-field, slow-motion conditions.* Whenever $|h_{\mu\nu}| \ll 1$ and $|v| \ll c$, the Newtonian limit applies. *Example problem*: in the solar system, $h_{\mu\nu} \sim GM_\odot/r \cdot 10^{-8}$ (very weak field, $r \sim 1$ AU), and planetary velocities $v \sim 30$ km/s $\sim 10^{-4} c$ (slow motion). So Newtonian gravity is the leading-order description, with GR corrections appearing at order $(v/c)^2$ or $h$.

*Source B₂: Linearised GR around any background.* The general framework: $g_{\mu\nu} = \bar g_{\mu\nu} + h_{\mu\nu}$ with $|h| \ll 1$, where $\bar g$ is some background metric. The linearised field equations for $h$ are: the Einstein equations expanded to first order in $h$ around the background. For Minkowski background, the linearised equations give the Newtonian limit (for slow matter) or **linearised gravitational waves** (for vacuum, propagating modes). *Bridge argument*: the Newtonian limit is the slow-motion limit of linearised GR around Minkowski. *Example problem*: gravitational waves propagating through the solar system can be analysed in linearised GR around the solar-system-modified Minkowski background.

*Source B₃: Post-Newtonian expansion (Eddington 1924, Will 1981).* The systematic expansion of GR in powers of $v/c$ and $GM/(rc^2)$ — the **post-Newtonian (PN) expansion** — has Newton's gravity as the $0$th-order term, with 1PN corrections at $(v/c)^2$, 2PN at $(v/c)^4$, etc. Each higher order brings in additional GR effects (perihelion precession at 1PN, gravitational radiation at 2.5PN). *Bridge argument*: the Newtonian limit is the leading order of the PN expansion. *Example problem*: the orbital dynamics of binary pulsars and binary inspirals are computed in the post-Newtonian framework, with the Newtonian-limit theorem being the starting point.

**Targets (Output Amplification).**

*Target T₁: Confirms GR's coupling constant.* The factor $8\pi G$ in $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ is *fixed* by the requirement that GR reduce to Newton. The Newtonian limit thus determines a non-trivial input parameter of the theory.

*Target T₂: Identification of $g_{00}$ with Newtonian potential.* This is the GR meaning of "the gravitational potential": $\phi = -\frac{1}{2}(g_{00} + 1)$. So in any GR computation, the leading-order Newtonian potential is just half the deviation of $g_{00}$ from $-1$.

*Target T₃: Foundation for post-Newtonian expansion.* All higher-order GR effects (perihelion precession, light bending, gravitational waves) are computed as corrections to the Newtonian limit. The Newtonian limit is the $0$th-order term; everything else is a post-Newtonian correction.

---

# Why Is It True

**The mechanism in one sentence: the Christoffel symbol $\Gamma^\alpha{}_{00}$ at low velocity is approximately $\partial^\alpha h_{00}/2$, so the spatial geodesic equation $\ddot x^\alpha \approx -\Gamma^\alpha{}_{00}$ gives $\ddot x^\alpha = -\partial^\alpha(h_{00}/2)$ — which matches Newton's $\ddot x^\alpha = -\partial^\alpha \phi$ with the identification $h_{00} = -2\phi$, fixing the connection between metric and potential.**

To unpack:

**Piece 1: geodesic equation in the slow-motion limit.** The geodesic equation is $\ddot x^\mu + \Gamma^\mu{}_{\nu\rho} \dot x^\nu \dot x^\rho = 0$, where $\dot{}$ is differentiation with respect to proper time $\tau$. In the slow-motion limit ($v \ll 1$), the four-velocity is $\dot x^\mu \approx (1, \vec v) + O(v^2)$, and $d\tau \approx dt$ (the proper time approximately equals coordinate time). For the spatial part:
$$\ddot x^\alpha + \Gamma^\alpha{}_{\nu\rho} \dot x^\nu \dot x^\rho \approx \ddot x^\alpha + \Gamma^\alpha{}_{00} \cdot 1 \cdot 1 + 2\Gamma^\alpha{}_{0i} v^i + \Gamma^\alpha{}_{ij} v^i v^j.$$
The leading term (slowest-motion) is $\Gamma^\alpha{}_{00}$, with the others being $O(v)$ or $O(v^2)$ relative.

So $\ddot x^\alpha \approx -\Gamma^\alpha{}_{00}$.

**Piece 2: $\Gamma^\alpha{}_{00}$ for static, weak metric.** For a static metric ($\partial_t g_{\mu\nu} = 0$) and weak field ($g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h| \ll 1$):
$$\Gamma^\alpha{}_{00} = \frac{1}{2} g^{\alpha\beta}(\partial_0 g_{\beta 0} + \partial_0 g_{\beta 0} - \partial_\beta g_{00}) = -\frac{1}{2} g^{\alpha\beta} \partial_\beta g_{00} \approx -\frac{1}{2}\eta^{\alpha\beta}\partial_\beta h_{00} = -\frac{1}{2} \partial^\alpha h_{00}.$$
Wait — let me redo: signature $(+,-,-,-)$, so $\eta^{\alpha\beta}$ for $\alpha \neq 0$ is $-\delta^{\alpha\beta}$. So $\Gamma^\alpha{}_{00} = -\frac{1}{2}(-\delta^{\alpha\beta})\partial_\beta h_{00} = \frac{1}{2}\partial^\alpha h_{00}$, where $\partial^\alpha$ uses the spatial Euclidean metric.

So $\ddot x^\alpha \approx -\Gamma^\alpha{}_{00} = -\frac{1}{2}\partial^\alpha h_{00}$.

**Piece 3: matching with Newton.** Compare with Newton's $\ddot x^\alpha = -\partial^\alpha \phi$. Match: $-\partial^\alpha \phi = -\frac{1}{2}\partial^\alpha h_{00}$, so $\phi = \frac{1}{2} h_{00}$, equivalently $h_{00} = 2\phi$.

Now: $g_{00} = \eta_{00} + h_{00} = 1 + h_{00}$ in signature $+---$... wait, $\eta_{00} = +1$ in this signature. So $g_{00} = 1 + 2\phi$, giving $g_{00} = +(1 + 2\phi)$.

Hmm — but standard form should be $g_{00} = -(1 + 2\phi)$ in the $-+++$ signature. Let me redo carefully.

In signature $(+,-,-,-)$, $\eta_{00} = +1$. For an asymptotically flat metric where $g_{00} \to +1$ at infinity and the gravitational potential is *negative* near a mass, we need $g_{00}$ to *decrease* as we approach the mass. Specifically: $g_{00} = 1 + h_{00}$ with $h_{00} < 0$ near a mass. Identifying $h_{00} = 2\phi$ with $\phi < 0$ (Newtonian potential is negative for an attractive source), we get $g_{00} = 1 + 2\phi$ near a mass, less than $1$ near a source — correct.

In the alternative signature $(-,+,+,+)$, $\eta_{00} = -1$ and $g_{00} \to -1$ at infinity, $g_{00} = -1 + h_{00}$ with $h_{00} < 0$ near a mass (further negative). Identification $h_{00} = -2\phi$ gives $g_{00} = -1 - 2\phi = -(1 + 2\phi)$, with $\phi < 0$ near mass so $g_{00}$ more negative. Correct.

So in both signatures, the identification is $\phi =$ half the deviation of $g_{00}$ from its asymptotic value, with sign convention adjusted. In our convention $(+,-,-,-)$: $g_{00} = 1 + 2\phi$, so $h_{00} = 2\phi$, and Newton's gravity has $\phi < 0$ near mass (attractive potential).

**Piece 4: Poisson equation from Einstein.** Now compute the $(0,0)$ component of the linearised Einstein equations. The linearised Ricci tensor for a static weak metric is $R_{00} \approx -\frac{1}{2}\nabla^2 h_{00}$ (where $\nabla^2$ is the spatial Laplacian). The linearised Ricci scalar is $R = g^{\mu\nu} R_{\mu\nu} \approx \eta^{\mu\nu} R_{\mu\nu} = R_{00} - R^i{}_i = -\frac{1}{2}\nabla^2 h_{00} - R^i{}_i$. To leading order in the static limit (with appropriate gauge choice), $R^i{}_i \approx -\frac{1}{2}\nabla^2 h_{00}$ as well (using the trace), so $R \approx -\nabla^2 h_{00}$ ... let me just use the simpler argument:

In the slow-motion limit, $T_{00} \approx \rho c^2 = \rho$ (in $c = 1$ units). The trace-reversed Einstein equation $R_{\mu\nu} = 8\pi G(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$ has trace $T = T^\mu{}_\mu \approx T^0{}_0 = \eta^{00} T_{00} = \rho$. So the $(0, 0)$ component is $R_{00} = 8\pi G(T_{00} - \frac{1}{2} g_{00} T) = 8\pi G(\rho - \frac{1}{2}(1) \rho) = 4\pi G \rho$.

From the geometric side, $R_{00} \approx -\frac{1}{2}\nabla^2 h_{00} = -\frac{1}{2}\nabla^2 (2\phi) = -\nabla^2 \phi$. So $-\nabla^2 \phi = 4\pi G \rho$, i.e., $\nabla^2 \phi = -4\pi G \rho$.

Hmm — that's the wrong sign. Let me re-examine the linearised Ricci. In the **mostly-plus** signature, $R_{00} \approx +\frac{1}{2}\nabla^2 h_{00}$ for a static metric, leading to $\nabla^2 \phi = 4\pi G \rho$. In the **mostly-minus** signature, the linearised Ricci is $R_{00} \approx -\frac{1}{2}\nabla^2 h_{00}$. The sign comes from the signature.

OK — to be safe, let me state the result for the standard Wald/Carroll mostly-plus convention, then translate:

In signature $(-,+,+,+)$:
- $g_{00} \to -1$ at infinity, $h_{00} = -2\phi$, $g_{00} = -(1 + 2\phi)$.
- Linearised $R_{00} = +\frac{1}{2}\nabla^2 h_{00} = -\nabla^2 \phi$.
- Trace-reversed Einstein gives $R_{00} = 8\pi G(T_{00} - \frac{1}{2} g_{00} T) = 8\pi G(\rho - \frac{1}{2}(-1)\rho) = 8\pi G \cdot \frac{3}{2}\rho$. Hmm this gives $-\nabla^2 \phi = 12\pi G \rho$, wrong factor.

I'm getting confused. The standard derivation:

Trace-reversed Einstein equation: $R_{\mu\nu} = 8\pi G(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$. For dust at rest, $T^{\mu\nu} = \rho u^\mu u^\nu$ with $u^\mu = (1, 0, 0, 0)$. So $T_{\mu\nu} = \rho u_\mu u_\nu$. In mostly-minus signature, $u_0 = g_{00} u^0 = 1$, so $T_{00} = \rho$. The trace $T = g^{\mu\nu} T_{\mu\nu} = g^{00} T_{00} = 1 \cdot \rho = \rho$ (since $g^{00} = 1$ in mostly-minus to leading order). So $T_{00} - \frac{1}{2} g_{00} T = \rho - \frac{1}{2}(1)\rho = \frac{1}{2}\rho$. Hence $R_{00} = 4\pi G \rho$.

Linearised $R_{00}$ in mostly-minus signature: a standard calculation gives $R_{00} = -\frac{1}{2}\Box h_{00}$, where $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu = \partial_t^2 - \nabla^2$ in mostly-plus, or $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu = \partial_t^2 - \nabla^2$ in mostly-minus also (the sign of $\eta$ flips but the d'Alembertian operator is well-defined). For static, $\Box h_{00} = -\nabla^2 h_{00}$. So $R_{00} = -\frac{1}{2}(-\nabla^2 h_{00}) = \frac{1}{2}\nabla^2 h_{00}$.

Wait — that's mostly-plus convention for $\Box$. In mostly-minus, $\eta^{\mu\nu}\partial_\mu\partial_\nu = \partial_t^2 - \nabla^2$ as before but with $\eta^{00} = 1$, $\eta^{ii} = -1$. So $\Box = \partial_t^2 - \nabla^2$. For static, $\Box h = -\nabla^2 h$.

So $R_{00} = -\frac{1}{2}\Box h_{00} = -\frac{1}{2}(-\nabla^2 h_{00}) = +\frac{1}{2}\nabla^2 h_{00}$.

Now $h_{00} = 2\phi$ (in mostly-minus, $g_{00} = 1 + h_{00} \approx 1 + 2\phi$, so $h_{00} = 2\phi$).

$R_{00} = +\frac{1}{2}\nabla^2(2\phi) = +\nabla^2 \phi$.

Setting equal to $4\pi G \rho$: $\nabla^2 \phi = 4\pi G \rho$. **Correct Poisson!**

OK so the sign works out. Let me clean up.

**The final clean version: $R_{00} = +\frac{1}{2}\nabla^2 h_{00}$ in the static weak-field limit (mostly-minus signature); $h_{00} = 2\phi$; trace-reversed Einstein gives $R_{00} = 4\pi G \rho$; hence $\nabla^2 \phi = 4\pi G \rho$, Newton's Poisson equation.**

The factor of $8\pi$ in the original Einstein equation produces the factor of $4\pi$ in Poisson's equation after the trace-reversal — specifically, $R_{00} = 8\pi G(T_{00} - \frac{1}{2} g_{00} T) = 8\pi G \cdot \frac{1}{2}\rho = 4\pi G \rho$ for the dust source.

---

# What Makes This Hard

The technical difficulty is in carefully tracking signs and signature conventions. The Newtonian limit derivation appears in nearly every GR textbook, and they use different conventions: Wald uses mostly-plus signature, Carroll uses mostly-plus, Frankel uses mostly-minus, MTW uses mostly-plus, Misner-Thorne-Wheeler uses some mixed signature... Getting from one source's convention to another requires careful translation, and a sign error makes the Newtonian potential come out with the wrong sign.

A common error is to compute the wrong linearised Ricci tensor: the formula $R_{\mu\nu} = \frac{1}{2}(\partial^\rho\partial_\mu h_{\nu\rho} + \partial^\rho\partial_\nu h_{\mu\rho} - \Box h_{\mu\nu} - \partial_\mu\partial_\nu h)$ has many terms, and in different gauges (Lorenz gauge $\partial^\mu h_{\mu\nu} = \frac{1}{2}\partial_\nu h$, transverse-traceless gauge, etc.) the form simplifies differently. Choosing the right gauge to make the Newtonian limit transparent requires practice.

Another conceptual subtlety: the slow-motion limit requires $|v| \ll c$, but the metric perturbation $h_{\mu\nu}$ can be large in some directions ($g_{rr} \sim 1$ for the spatial part of Schwarzschild has $h_{rr}$ small even at horizons, but the spatial geometry is still genuinely curved). What matters is $|h_{00}| \ll 1$ for the timelike geodesic equation, and $|h_{ij}|$ separately for the spatial corrections.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Three steps: (1) Geodesic equation in slow-motion gives $\ddot x^\alpha \approx -\Gamma^\alpha{}_{00}$. (2) Linearised $\Gamma^\alpha{}_{00}$ for static metric gives $\Gamma^\alpha{}_{00} \approx \frac{1}{2}\partial^\alpha h_{00}$. (3) Match with Newton's $\ddot x^\alpha = -\partial^\alpha\phi$ to identify $h_{00} = 2\phi$. Then: $R_{00}$ in linearised theory equals $\frac{1}{2}\nabla^2 h_{00} = \nabla^2 \phi$; trace-reversed Einstein gives $R_{00} = 4\pi G \rho$ for dust; equating gives Poisson's $\nabla^2 \phi = 4\pi G \rho$.

**Subgoal decomposition:**

1. **Slow-motion geodesic:** $\ddot x^\alpha \approx -\Gamma^\alpha{}_{00}$ for $|v| \ll 1$.

2. **Christoffel for static weak metric:** $\Gamma^\alpha{}_{00} \approx \frac{1}{2}\partial^\alpha h_{00}$.

3. **Identification:** $\phi = h_{00}/2$, i.e., $h_{00} = 2\phi$ (in signature $+---$, so $g_{00} \to 1$ at infinity).

4. **Linearised Ricci:** $R_{00} \approx \frac{1}{2}\nabla^2 h_{00}$ for static weak metric.

5. **Trace-reversed Einstein:** $R_{00} = 8\pi G(T_{00} - \frac{1}{2} g_{00} T) = 4\pi G \rho$ for dust at rest.

6. **Combine:** $\nabla^2 \phi = 4\pi G \rho$ — Poisson's equation. Coupling constant matches.

---

# Lemma Decomposition

> [!note]- Lemma 1: Geodesic in slow-motion limit
> **Statement:** For a timelike geodesic in coordinates with $|v^i| \ll 1$ and $d\tau \approx dt$, the spatial geodesic equation reduces to $\ddot x^\alpha \approx -\Gamma^\alpha{}_{00}$.
>
> **Hint:** Expand $\dot x^\mu \approx (1, v^i)$ in the geodesic equation; keep only the leading-order term in $v$.
>
> **Why needed:** Provides the dynamical reduction to a "Newton-like" form.
>
> > [!note]- Full proof
> > Geodesic equation: $\ddot x^\mu + \Gamma^\mu{}_{\nu\rho}\dot x^\nu \dot x^\rho = 0$. Spatial component ($\mu = \alpha$): $\ddot x^\alpha + \Gamma^\alpha{}_{00}(\dot x^0)^2 + 2\Gamma^\alpha{}_{0i}\dot x^0 \dot x^i + \Gamma^\alpha{}_{ij}\dot x^i \dot x^j = 0$. With $\dot x^0 \approx 1$ and $\dot x^i \approx v^i$ with $|v| \ll 1$: $\ddot x^\alpha \approx -\Gamma^\alpha{}_{00} - 2\Gamma^\alpha{}_{0i} v^i - \Gamma^\alpha{}_{ij} v^i v^j$. The leading term (lowest power of $v$) is $-\Gamma^\alpha{}_{00}$; the others are $O(v)$ or $O(v^2)$ and are next-to-leading post-Newtonian corrections.

> [!note]- Lemma 2: Christoffel symbol for static weak metric
> **Statement:** For $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $\partial_t h_{\mu\nu} = 0$ and $|h| \ll 1$, $\Gamma^\alpha{}_{00} \approx \frac{1}{2}\partial^\alpha h_{00}$ (signature $+---$, so $\partial^\alpha = -\delta^{\alpha\beta}\partial_\beta = -\partial_\alpha$ spatially).
>
> **Hint:** $\Gamma^\rho{}_{\mu\nu} = \frac{1}{2} g^{\rho\sigma}(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu})$. Substitute $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$, use $\partial_t h = 0$ for static, keep only leading order in $h$.
>
> **Why needed:** Computes the gravitational "force" $-\Gamma^\alpha{}_{00}$.
>
> > [!note]- Full proof
> > $\Gamma^\alpha{}_{00} = \frac{1}{2} g^{\alpha\beta}(\partial_0 g_{\beta 0} + \partial_0 g_{\beta 0} - \partial_\beta g_{00})$. For static metric, $\partial_0 g = 0$, so the first two terms vanish: $\Gamma^\alpha{}_{00} = -\frac{1}{2} g^{\alpha\beta}\partial_\beta g_{00}$. To leading order in $h$, $g^{\alpha\beta} \approx \eta^{\alpha\beta}$ (with signature $+---$, $\eta^{00} = +1, \eta^{ii} = -1$, off-diagonal zero), and $g_{00} = 1 + h_{00}$, so $\partial_\beta g_{00} = \partial_\beta h_{00}$. For spatial $\alpha = i$: $\Gamma^i{}_{00} = -\frac{1}{2}\eta^{ij}\partial_j h_{00} = -\frac{1}{2}(-\delta^{ij})\partial_j h_{00} = \frac{1}{2}\partial^i h_{00}$, where $\partial^i = \delta^{ij}\partial_j$ uses the Euclidean spatial metric.

> [!note]- Lemma 3: Identification $h_{00} = 2\phi$
> **Statement:** Matching the spatial geodesic equation $\ddot x^\alpha \approx -\Gamma^\alpha{}_{00} = -\frac{1}{2}\partial^\alpha h_{00}$ with Newton's $\ddot x^\alpha = -\partial^\alpha \phi$ gives $h_{00} = 2\phi$, equivalently $g_{00} = 1 + 2\phi$ (in signature $+---$).
>
> **Hint:** Direct comparison.
>
> **Why needed:** Identifies the Newtonian potential with the metric.
>
> > [!note]- Full proof
> > From Lemmas 1, 2: $\ddot x^\alpha \approx -\frac{1}{2}\partial^\alpha h_{00}$. Newton's gravitational acceleration: $\ddot x^\alpha = -\partial^\alpha \phi$. Equating: $\partial^\alpha \phi = \frac{1}{2}\partial^\alpha h_{00}$, so $\phi = \frac{1}{2} h_{00}$ (up to an additive constant, fixed by demanding $\phi, h_{00} \to 0$ at infinity). Hence $h_{00} = 2\phi$.

> [!note]- Lemma 4: Linearised Ricci tensor $R_{00}$
> **Statement:** In the static weak-field limit, $R_{00} \approx \frac{1}{2}\nabla^2 h_{00}$ (with $\nabla^2$ the spatial Laplacian).
>
> **Hint:** Compute $R_{\mu\nu}$ to first order in $h$. For static, terms with $\partial_t h$ vanish. The result is a specific combination of derivatives of $h$ that, for $R_{00}$, reduces to $\frac{1}{2}\nabla^2 h_{00}$.
>
> **Why needed:** Provides the geometric LHS of the field equation.
>
> > [!note]- Full proof
> > The linearised Ricci tensor in any signature is $R_{\mu\nu}^{(1)} = \frac{1}{2}(\partial^\rho\partial_\mu h_{\nu\rho} + \partial^\rho\partial_\nu h_{\mu\rho} - \Box h_{\mu\nu} - \partial_\mu\partial_\nu h)$, where $h = \eta^{\mu\nu} h_{\mu\nu}$. For static metric, $\partial_t h = 0$, and the d'Alembertian $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu$ becomes $-\nabla^2$ for static fields (signature $+---$: $\Box = \partial_t^2 - \nabla^2 \to -\nabla^2$). For the $(0,0)$ component: $R_{00}^{(1)} = \frac{1}{2}(\partial^\rho\partial_0 h_{0\rho} + \partial^\rho\partial_0 h_{0\rho} - \Box h_{00} - \partial_0\partial_0 h)$. For static, the time derivatives vanish: $R_{00}^{(1)} = \frac{1}{2}(0 + 0 - (-\nabla^2) h_{00} - 0) = \frac{1}{2}\nabla^2 h_{00}$.

> [!note]- Lemma 5: Trace-reversed Einstein equation for dust
> **Statement:** The trace-reversed equation $R_{\mu\nu} = 8\pi G(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$ for dust at rest, with $T^{\mu\nu} = \rho u^\mu u^\nu$ and $u^\mu = (1, 0, 0, 0)$, gives $R_{00} = 4\pi G \rho$.
>
> **Hint:** Compute $T_{00}$ and the trace $T$; substitute.
>
> **Why needed:** Provides the source side of the field equation.
>
> > [!note]- Full proof
> > For dust at rest, $T^{00} = \rho$ and $T^{0i} = T^{ij} = 0$. Lowering: $T_{00} = g_{0\mu} g_{0\nu} T^{\mu\nu} = (g_{00})^2 T^{00} \approx (1)^2 \rho = \rho$ to leading order. Trace: $T = g_{\mu\nu} T^{\mu\nu} = g_{00} T^{00} \approx 1 \cdot \rho = \rho$. Substituting in trace-reversed Einstein: $R_{00} = 8\pi G(T_{00} - \frac{1}{2} g_{00} T) = 8\pi G(\rho - \frac{1}{2}(1)\rho) = 8\pi G \cdot \frac{1}{2}\rho = 4\pi G \rho$.

> [!note]- Lemma 6: Poisson equation
> **Statement:** Combining Lemmas 3, 4, 5: $\nabla^2 \phi = 4\pi G \rho$.
>
> **Hint:** Substitute $h_{00} = 2\phi$ from Lemma 3 into $R_{00} = \frac{1}{2}\nabla^2 h_{00}$ from Lemma 4; equate with $R_{00} = 4\pi G \rho$ from Lemma 5.
>
> **Why needed:** Final form: Newton's gravity equation.
>
> > [!note]- Full proof
> > From Lemma 4: $R_{00} = \frac{1}{2}\nabla^2 h_{00}$. From Lemma 3: $h_{00} = 2\phi$, so $R_{00} = \frac{1}{2}\nabla^2(2\phi) = \nabla^2 \phi$. From Lemma 5: $R_{00} = 4\pi G \rho$. Equating: $\nabla^2 \phi = 4\pi G \rho$ — Poisson's equation for the Newtonian potential with the correct coupling constant $4\pi G$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0** (setup): Consider a spacetime $(M, g)$ with $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ where $|h_{\mu\nu}| \ll 1$ (weak field), $\partial_t h_{\mu\nu} = 0$ (static), and matter velocities $|v| \ll 1$ (slow motion). Signature $(+,-,-,-)$.
>
> **Step 1** (geodesic reduction): By Lemma 1, the slow-motion geodesic equation reduces to $\ddot x^\alpha = -\Gamma^\alpha{}_{00}$.
>
> **Step 2** (Christoffel for weak static): By Lemma 2, $\Gamma^\alpha{}_{00} = \frac{1}{2}\partial^\alpha h_{00}$.
>
> **Step 3** (identification of $\phi$): By Lemma 3, matching $\ddot x^\alpha = -\partial^\alpha \phi$ (Newton) with $\ddot x^\alpha = -\frac{1}{2}\partial^\alpha h_{00}$ (GR) gives $\phi = h_{00}/2$, equivalently $g_{00} = 1 + 2\phi$.
>
> **Step 4** (linearised Ricci): By Lemma 4, in the static weak-field limit, $R_{00} = \frac{1}{2}\nabla^2 h_{00} = \nabla^2 \phi$.
>
> **Step 5** (trace-reversed Einstein for dust): By Lemma 5, $R_{00} = 4\pi G \rho$ for dust at rest.
>
> **Step 6** (Poisson's equation): Combining Steps 4 and 5: $\nabla^2 \phi = 4\pi G \rho$ — Newton's Poisson equation with the correct coupling constant.
>
> The factor $8\pi G$ in the original Einstein equations is therefore precisely what reproduces the Newtonian $4\pi G$ in Poisson's equation, after the trace-reversal yields the $4\pi G$ from $8\pi G \cdot \frac{1}{2}$. So the coupling constant in GR is fixed by the requirement of the correct Newtonian limit.
>
> $\square$

---

# Cross-Field Exercise Suggestions

**Application 1: Geodesic motion in a weak field beyond Newton.** Compute the *next* post-Newtonian correction to the geodesic equation, going beyond the slow-motion limit to include terms at $O(v^2/c^2)$. This gives **gravitational time dilation** beyond the Newtonian potential, and the leading-order correction to planetary orbits — in particular the perihelion precession.

**Application 2: Post-Newtonian deflection of light.** The naive Newtonian deflection of a light "particle" moving at speed $c$ in the gravitational field of the Sun gives $\Delta\phi_\text{Newton} = 2GM/(bc^2)$. The full GR calculation (using null [[Def - Geodesic|geodesics]] in the full Schwarzschild metric, not just the Newtonian limit) gives $\Delta\phi_\text{GR} = 4GM/(bc^2)$ — twice the Newtonian value. The factor of 2 arises from the spatial $g_{rr}$ component of the Schwarzschild metric, beyond just the temporal $g_{00}$. So the light-bending discrepancy is direct evidence of the spatial curvature in GR, beyond just the equivalence-principle "gravitational redshift" effect.

**Application 3: Newtonian limit with cosmological constant.** Include the $\Lambda g_{\mu\nu}$ term in the Einstein equations: the modified Poisson equation becomes $\nabla^2 \phi = 4\pi G \rho - \Lambda$. The cosmological constant acts as a *repulsive* contribution to gravity at large scales — the basis for accelerated cosmic expansion and the de Sitter solution.

**Application 4: Stellar structure in the Newtonian limit.** Apply the Newtonian limit to the TOV equation for spherical relativistic stars. The result is the **Lane–Emden equation** $dp/dr = -\rho M(r)/r^2$ — the Newtonian equation of stellar structure. This is the limit of the TOV equation valid for non-compact stars (Sun, planets). Compact objects (white dwarfs, neutron stars) require the full TOV.

---

# Bridges

- **[[Def - Equivalence Principle]]** — The Newtonian limit is the operational content of the equivalence principle plus the dynamical Einstein equations. The equivalence principle says that locally, in a freely-falling frame, the laws of physics are special-relativistic; the Newtonian limit takes this further to the *globally weak field* where the metric is approximately Minkowski and slow particles move approximately Newtonianly. So the Newtonian limit is the weak-field, slow-motion realisation of the equivalence principle.

- **[[Def - The Metric Tensor as Gravitational Potential]]** — The Newtonian limit makes precise the slogan "the metric is the gravitational potential". Specifically, the temporal component $g_{00}$ encodes the Newtonian potential via $g_{00} = 1 + 2\phi$ (or $-(1 + 2\phi)$ in mostly-plus). The other nine components of $g_{\mu\nu}$ are "new" in GR and capture frame-dragging, gravitational waves, and spatial curvature — phenomena absent from Newton.

- **Post-Newtonian expansion** — The Newtonian limit is the $0$th-order term in the **post-Newtonian (PN) expansion** of GR — a systematic expansion in powers of $v/c$ and $GM/(rc^2)$. Each higher order brings in additional GR effects: 1PN gives perihelion precession; 1.5PN gives gravitomagnetic effects (frame dragging); 2.5PN gives gravitational radiation reaction. Modern post-Newtonian theory routinely computes corrections up to 4PN, used in waveform modelling for LIGO data analysis.

- **Geometric flow theory — Yamabe flow, Ricci flow.** The leading-order field equations for a metric (essentially the Newtonian limit) are second-order PDEs (Poisson, Laplace). The full GR equations are nonlinear PDEs, but viewing them as a flow on metric space (Ricci flow $\partial_t g = -2 R_{\mu\nu}$) puts them in the framework of **geometric analysis**. The Newtonian limit is the linearised version of this flow on Minkowski background. Perelman's proof of the **Poincaré conjecture** via Ricci flow with surgery is the analytic culmination of this perspective.

---

# Unlocked by This

> [!tip] Post-Newtonian Expansion *(from Relativistic Astrophysics)*
> The **post-Newtonian (PN) expansion** systematically extends the Newtonian limit by higher-order terms in $v/c$ and $GM/(rc^2)$. The 1PN corrections give the **classical tests of GR**: perihelion precession of Mercury ($43''$/century, exactly the GR prediction), Shapiro time delay, gyroscopic precession. The 2.5PN corrections give **gravitational radiation reaction** — the orbital energy loss that drives binary inspirals. Modern PN theory at 4PN and higher is used to model LIGO waveforms.

> [!tip] Gravitomagnetism and Lense-Thirring Effect *(from Frame Dragging)*
> Beyond Newton, the off-diagonal $g_{0i}$ components of the metric encode **gravitomagnetic** effects — gravitational analogues of magnetism. A rotating mass (the Earth, the Sun, a black hole) drags inertial frames around with it, in analogy to a moving charge creating a magnetic field. The **Lense-Thirring effect** is the precession of a gyroscope orbiting a rotating body — measured by **Gravity Probe B** (2011) around the Earth to precision $\sim 37$ milliarcseconds per year.

> [!tip] Gravitational Lensing in the Weak-Field Limit *(from Astrophysical Observations)*
> Light passing through a weak-field gravitational region (around a galaxy or cluster) is deflected by $\Delta\phi = 4GM/(bc^2)$ — twice the Newtonian-particle value. This is the basis of **gravitational lensing**: distorted images of distant galaxies behind foreground masses. Used to map dark matter distributions in galaxy clusters and to study cosmic structure on the largest scales.

> [!tip] Newtonian Limit of Modified Gravity *(from Beyond-Einstein Theories)*
> Modified gravity theories (scalar-tensor, $f(R)$, etc.) must reproduce Newton's gravity in the weak-field limit to be observationally viable. The Newtonian limit of each modified theory provides a fitness test: any deviation from $\nabla^2 \phi = 4\pi G \rho$ in the appropriate regime would be detected by solar-system tests. This is the strongest experimental constraint on modified gravity at solar-system scales.

> [!tip] Effective Field Theory of Gravity *(from Quantum Gravity)*
> Quantising gravity in the weak-field limit (linearised gravity around Minkowski) gives the **graviton** — a massless spin-2 particle. The Newtonian limit is the static, large-distance limit of graviton exchange between matter sources. The full effective field theory of gravity has the Hilbert action as its leading term, with higher-curvature corrections from quantum effects suppressed by powers of the Planck mass. This gives a well-defined, finite, renormalisable theory of *quantum corrections to Newton's law* — though the theory becomes strongly coupled (non-renormalisable) at the Planck scale.

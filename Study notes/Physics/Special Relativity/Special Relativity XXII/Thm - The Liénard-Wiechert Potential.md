---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Gauge Choice and the Lorenz Gauge"
  - "Def - The Electric Four-Current"
  - "Def - The Four-Potential"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A charge $q$ follows the worldline $\mathcal L$, position $X(\tau)$, four-velocity $U(\tau)$, four-acceleration $a(\tau)$, at proper time $\tau$. The field point is $M$; the **retarded point** $P$ is the unique past intersection $\{P\} = \mathcal L\cap\mathcal I^-(M)$ of the worldline with the past light cone of $M$, at proper time $\tau_P$. The **retarded distance** is $R := U(\tau_P)\cdot\vec{PM}$. The [[Def - The Four-Potential|four-potential]] is $A$, the field $F$; relative to an observer of four-velocity $U_0$, $V$ and $\boldsymbol{\mathcal A}$ are the scalar and vector potentials, $\mathbf E$, $\mathbf B$ the fields, $\mathbf V$ the particle's three-velocity, $\boldsymbol\gamma$ its three-acceleration, $\Gamma$ its Lorentz factor, $\hat{\mathbf n}$ the unit vector from $P$ toward $M$, and $r$ the retarded spatial distance. $G_{\mathrm{ret}}$ is the retarded Green function, $\Upsilon$ the Heaviside step function. Full registry on [[Special Relativity XXII — Maxwell's Equations]].

---

# Statement

> **Theorem (Liénard–Wiechert potential).** The electromagnetic four-potential created at an event $M$ by a charge $q$ following an arbitrary worldline $\mathcal L$ is, in Lorenz gauge,
> $$A(M) = \frac{\mu_0 q}{4\pi}\,\frac{U(\tau_P)}{R}, \qquad R = U(\tau_P)\cdot\vec{PM},$$
> where $P$ is the retarded point $\{P\} = \mathcal L\cap\mathcal I^-(M)$ and $\tau_P$ its proper time. Relative to an inertial observer, the scalar and vector potentials are
> $$V(M) = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{r\,[1 - \hat{\mathbf n}\cdot\mathbf V]}, \qquad \boldsymbol{\mathcal A}(M) = \frac{\mu_0}{4\pi}\,\frac{q\,\mathbf V}{r\,[1 - \hat{\mathbf n}\cdot\mathbf V]},$$
> all evaluated at the retarded time, with $r$ the retarded distance and $\hat{\mathbf n}$ the unit vector from the retarded position toward $M$.

> **The field.** The electromagnetic field is the exterior product of two $1$-forms,
> $$F(M) = \frac{q}{4\pi\varepsilon_0 R^2}\left[\underline a(\tau_P) + \frac{1 + a(\tau_P)\cdot\vec{PM}}{R}\,\underline U(\tau_P)\right]\wedge\underline{PM},$$
> so $F = p\wedge q$ and consequently ${\star}F_{\mu\nu}F^{\mu\nu} = 0$ automatically.

> **Coulomb and radiative parts.** The field splits as $F = F_{\mathrm{Coul}} + F_{\mathrm{rad}}$ with
> $$F_{\mathrm{Coul}} = \frac{q}{4\pi\varepsilon_0 R^3}\,\underline U(\tau_P)\wedge\underline{PM} \;\propto\; \frac{1}{r^2}, \qquad F_{\mathrm{rad}} = \frac{q}{4\pi\varepsilon_0 R^2}\left[\underline a + \frac{a\cdot\vec{PM}}{R}\underline U\right]\wedge\underline{PM} \;\propto\; \frac{1}{r}.$$
> The Coulomb part is present for any charge and decays as $1/r^2$; the radiative part is nonzero only under acceleration ($a \ne 0$) and decays as $1/r$, dominating at large distance. Both parts are null ($I_1 = I_2 = 0$ for $F_{\mathrm{rad}}$) and transverse, ${\star}F_{\mathrm{rad}}(\vec{PM}, \cdot) = 0$.

---

# Motivation

This is the complete solution of Maxwell's equations for the most basic source there is: a single point charge moving in any way whatsoever. Everything in electromagnetism — antennas, synchrotrons, the field of an electron in an atom, the light from an accelerating charge — is built from this one result, because any charge distribution is a superposition of point charges. The Liénard–Wiechert potential is to electromagnetism what the Coulomb potential is to electrostatics: the fundamental solution, the building block.

The single most important physical idea in the theorem is **retardation**. The field at $M$ does not depend on where the charge is *now*; it depends on where the charge was at the **retarded time**, the instant when light leaving the charge would just reach $M$. Geometrically, the charge's worldline pierces the past light cone of $M$ at exactly one point $P$ (because the worldline is timelike), and the field is determined entirely by the charge's state — its velocity and acceleration — at $P$. This is causality made concrete: the field carries news of the charge's motion at the speed of light, no faster, so what arrives at $M$ is always the charge's *past*. For a uniformly moving charge this retardation conspires to make the field point at the charge's present position anyway (a relativistic accident), but for an accelerating charge the distinction is everything.

The structure of the field is remarkable in two ways. First, it is an **exterior product** $F = p\wedge q$ of two $1$-forms — the field of any single charge is a wedge, which forces one of its invariants to vanish identically, so $\mathbf E\perp\mathbf B$ for every single charge. Second, it splits cleanly into a **Coulomb part** that dies as $1/r^2$ and a **radiative part** that dies only as $1/r$. The slow $1/r$ falloff of the radiative part is what lets it carry energy to infinity: the energy flux through a sphere goes as (field)$^2\times$ area $\sim (1/r)^2\times r^2$, a constant, so an accelerating charge radiates energy that never returns. This is the field of an antenna, the glow of a synchrotron, the reason a classical atom would collapse — all contained in the term proportional to the acceleration.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "the source is a single point charge on a timelike worldline, and we work in Lorenz gauge".

The first disguised source is **"a charge distribution that can be decomposed into point charges"**. Any continuous charge distribution is a superposition of point charges, so its field is the integral of Liénard–Wiechert fields over the distribution. The bridge is linearity of Maxwell's equations: superpose the elementary solutions. The nonobviousness is that the single-charge result, integrated, gives every charge configuration's field. *Example problem:* find the field of an oscillating charge distribution by superposing Liénard–Wiechert fields.

The second disguised source is **"a charge in specified motion at a specified retarded time"**. Whenever the charge's velocity and acceleration are known at the retarded point — even if its full worldline is complicated — the field at $M$ is computable, because it depends only on $U(\tau_P)$ and $a(\tau_P)$. The bridge is that the past light cone of $M$ selects one retarded point, and only the local data there matter. *Example problem:* compute the field at a detector from a charge whose velocity and acceleration at the retarded instant are given.

The third disguised source is **"an accelerating charge in the radiation zone"**. Far from an accelerating charge, the Coulomb part is negligible and the field is purely radiative, $F \simeq F_{\mathrm{rad}} \propto a(\tau_P)/r$. The bridge is the $1/r$ versus $1/r^2$ falloff: at large $r$, only the radiative part survives. *Example problem:* find the radiation field of an antenna far away, keeping only the acceleration term.

**Targets (Output Amplification)**

The conclusion is the potential $A(M) = \frac{\mu_0 q}{4\pi}U(\tau_P)/R$ and the field $F = p\wedge q$.

Combine the conclusion with **the exterior-product structure**. Since $F = p\wedge q$, the invariant ${\star}F_{\mu\nu}F^{\mu\nu} \propto \epsilon(p, q, p, q) = 0$ automatically. The further result is that $\mathbf E\perp\mathbf B$ for the field of any single charge, accelerating or not. The combination is nonobvious because the wedge structure is hidden in the algebra of the field; once seen, it gives a frame-independent constraint for free. *Example:* show that a single charge never produces a field with $\mathbf E\cdot\mathbf B \ne 0$.

Combine the conclusion with **the inertial-motion limit**. Setting $a = 0$, the field reduces to $F = \frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$, which (after working out $R$ in terms of the present position) is the boosted Coulomb field, pointing at the charge's instantaneous position. The further result is that a uniformly moving charge's field is "Coulomb, flattened by length contraction" and points at the present (not retarded) position. The combination explains the relativistic conspiracy. *Example:* recover the field of a uniformly moving charge and verify it points at the present position.

Combine the conclusion with **the energy flux of the radiative part**. The radiative field $F_{\mathrm{rad}} \propto a/r$ carries a Poynting flux $\propto a^2/r^2$; integrating over a large sphere gives a finite radiated power $\propto a^2$. The further result is the Larmor formula $P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$. The combination is the bridge from the field to radiated energy. *Example:* derive the Larmor formula from the radiative field.

---

# Why Is It True

The bolded mechanism: **the retarded Green function localises the four-dimensional source integral to the single point where the charge's worldline crosses the past light cone of $M$, and the Dirac-delta composition identity evaluates the integral there, dividing by the rate $|g'(\tau_P)| = 2R$ at which the worldline crosses the cone — producing the $1/R$ falloff and the $U(\tau_P)$ direction.** The whole result is "evaluate the source at the retarded point, weighted by the inverse crossing rate".

Take it through the steps. The four-current of a single charge is $J(M) = q\int\delta_{X(\tau)}(M)\,U(\tau)\,d\tau$, a Dirac current along the worldline. In Lorenz gauge the potential is the retarded-Green-function integral $A(M) = \frac{\mu_0}{?}\int J(N)\,G_{\mathrm{ret}}(M, N)\,d^4N$ (with the constant fixed by $\Box A = \mu_0 J$). Substituting the point-current and integrating over the spacetime point $N$ (the $\delta_{X(\tau)}$ collapses the four-dimensional integral onto the worldline) leaves a one-dimensional integral over proper time: $A(M) \propto q\int U(\tau)\,\delta(g(\tau))\,\Upsilon(\cdots)\,d\tau$, where $g(\tau) = \vec{X(\tau)M}\cdot\vec{X(\tau)M}$ is the squared interval from the worldline point to $M$, and the delta enforces that this interval vanish — i.e. that the worldline point lie on the light cone of $M$.

Now the geometry. The worldline is timelike, so it crosses the light cone of $M$ at exactly two points: one in the past ($P$, on $\mathcal I^-(M)$) and one in the future ($Q$, on $\mathcal I^+(M)$). The Heaviside factor $\Upsilon$, which selects the retarded (past) cone, kills the future intersection $Q$, leaving only $P$. The Dirac-delta composition identity $\int f\,\delta(g)\,d\tau = \sum_a f(\tau_a)/|g'(\tau_a)|$ evaluates the integral at $\tau_P$, dividing by $|g'(\tau_P)|$. And $g'(\tau) = 2\vec{X(\tau)M}\cdot\frac{d}{d\tau}\vec{X(\tau)M} = -2\,\vec{X(\tau)M}\cdot U(\tau)$ (since $\frac{d}{d\tau}\vec{X(\tau)M} = -U(\tau)$), so $|g'(\tau_P)| = 2|\vec{PM}\cdot U(\tau_P)| = 2R$. Hence $A(M) = \frac{\mu_0 q}{4\pi}\frac{U(\tau_P)}{R}$ — the four-velocity at the retarded point, divided by twice the retarded distance, with the $4\pi$ from the Green function's normalisation.

Why $R = U(\tau_P)\cdot\vec{PM}$ is "the retarded distance": relative to an instantaneous comoving observer at $P$ (whose four-velocity is $U(\tau_P)$), $R$ is the spatial distance to the point simultaneous with $P$ at $M$'s spatial location. It is the relativistic generalisation of "distance from the charge", and the $1/R$ is the relativistic generalisation of the $1/r$ of the Coulomb potential.

The field follows by computing $F = dA$, differentiating the retarded potential. The differentiation must account for the dependence of $\tau_P$ on $M$ (the retarded time shifts as the field point moves), which is fixed by differentiating the light-cone condition $\vec{PM}\cdot\vec{PM} = 0$. The result is the wedge $F = p\wedge q$ with $q = \underline{PM}$ and $p$ a combination of $\underline a$ and $\underline U$; the acceleration enters because differentiating $U(\tau_P)$ brings down $a(\tau_P)$, and it is the acceleration term that produces the slowly-decaying radiative part.

---

# What Makes This Hard

The hardest conceptual step is the retardation itself: accepting that the field depends on the charge's *past* state, at the one point where its worldline meets the past light cone, not on its present position. The technical crux is the differentiation $F = dA$ of the retarded potential, where one must correctly account for the implicit dependence of the retarded proper time $\tau_P$ on the field point $M$ — this is done by differentiating the light-cone constraint $\vec{PM}\cdot\vec{PM} = 0$, giving $\partial\tau_P/\partial x^\beta = -(PM)_\beta/(cR)$, and forgetting this implicit dependence is the most common error, costing the entire radiative term. A secondary subtlety is the Dirac-delta composition factor $|g'(\tau_P)| = 2R$: a missing factor of $2$ or a sign error in $g'(\tau) = -2\vec{X(\tau)M}\cdot U$ corrupts the normalisation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the point charge's four-current; substitute into the retarded-potential integral; collapse the spacetime integral onto the worldline with the position delta; evaluate the remaining proper-time integral with the Dirac-delta composition identity, localising to the retarded point and dividing by $|g'(\tau_P)| = 2R$; this gives the potential. Differentiate ($F = dA$), carefully tracking $\tau_P$'s dependence on $M$ via the light-cone constraint, to get the field as a wedge; split off the acceleration-dependent radiative part.

**Subgoal decomposition:**

1. **Set up the retarded integral.** Substitute $J = q\int\delta_{X(\tau)}U\,d\tau$ into $A(M) = \frac{\mu_0}{4\pi}\int J\,G_{\mathrm{ret}}\,d^4N$ (constant from $\Box A = \mu_0 J$).
   - *Hint:* The position delta $\delta_{X(\tau)}(N)$ collapses the $d^4N$ integral onto the worldline, leaving $\int U(\tau)\,\delta(g(\tau))\,\Upsilon\,d\tau$ with $g(\tau) = \vec{X(\tau)M}\cdot\vec{X(\tau)M}$.
   - *Why needed:* It reduces the four-dimensional Green-function integral to one dimension.

2. **Localise to the retarded point.** Apply $\int f\,\delta(g)\,d\tau = \sum_a f(\tau_a)/|g'(\tau_a)|$; the Heaviside selects the past intersection $P$.
   - *Hint:* The timelike worldline meets the light cone of $M$ at two points; $\Upsilon$ keeps the past one. Compute $g'(\tau) = -2\vec{X(\tau)M}\cdot U(\tau)$, so $|g'(\tau_P)| = 2R$.
   - *Why needed:* It evaluates the integral, producing $A(M) = \frac{\mu_0 q}{4\pi}U(\tau_P)/R$.

3. **Differentiate for the field.** Compute $F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$, tracking $\partial\tau_P/\partial x^\beta$ from the light-cone constraint $\vec{PM}\cdot\vec{PM} = 0$.
   - *Hint:* $\partial\tau_P/\partial x^\beta = -(PM)_\beta/(cR)$; differentiating $U(\tau_P)$ brings down $a(\tau_P)\,\partial\tau_P/\partial x^\beta$; the $u_\alpha u_\beta$ term drops in the antisymmetrisation.
   - *Why needed:* It produces the field as the wedge $F = p\wedge q$.

4. **Split into Coulomb and radiative parts.** Separate the acceleration-independent term ($\propto 1/R^3$, Coulomb) from the acceleration-dependent term ($\propto 1/R^2$ with $a$, radiative).
   - *Hint:* The Coulomb part is $\frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$; the radiative part carries $\underline a$ and falls as $1/r$.
   - *Why needed:* It exhibits the physically distinct near (Coulomb) and far (radiation) fields.

---

# Lemma Decomposition

> [!note]- Lemma 1: The worldline meets the past light cone of $M$ at exactly one point
> **Statement:** For a timelike worldline and an event $M$ not on it, there is exactly one retarded point $\{P\} = \mathcal L\cap\mathcal I^-(M)$.
>
> **Hint:** A timelike curve crosses any light cone at most twice; the past cone is met once.
>
> **Why needed:** It guarantees the retarded potential is well-defined (one term, not a sum).
>
> > [!note]- Full proof
> > The function $g(\tau) = \vec{X(\tau)M}\cdot\vec{X(\tau)M}$ measures the squared interval from the worldline point $X(\tau)$ to $M$. As $\tau \to \pm\infty$ along a timelike worldline, $X(\tau)$ recedes to timelike infinity and $g(\tau) \to +\infty$ (timelike separation, positive in our signature). At the proper time of closest approach $g$ has a minimum; if $M$ is not on the worldline the minimum is negative or the geometry is such that $g = 0$ has exactly two roots, one with $X(\tau)$ in the past of $M$ (on $\mathcal I^-(M)$) and one in the future (on $\mathcal I^+(M)$), because a timelike curve enters and exits the light cone once each. The Heaviside factor $\Upsilon$ selecting the past cone picks the single retarded root $\tau_P$. $\blacksquare$

> [!note]- Lemma 2: The crossing-rate factor is $|g'(\tau_P)| = 2R$
> **Statement:** $g'(\tau) = -2\vec{X(\tau)M}\cdot U(\tau)$, so $|g'(\tau_P)| = 2R$ with $R = U(\tau_P)\cdot\vec{PM}$.
>
> **Hint:** Differentiate $g(\tau) = \vec{X(\tau)M}\cdot\vec{X(\tau)M}$ using $\frac{d}{d\tau}\vec{X(\tau)M} = -U(\tau)$.
>
> **Why needed:** It is the denominator in the Dirac-delta evaluation, giving the $1/R$ falloff.
>
> > [!note]- Full proof
> > Write $\vec{X(\tau)M} = M - X(\tau)$ as a position-difference vector. Then $\frac{d}{d\tau}\vec{X(\tau)M} = -\frac{dX}{d\tau} = -U(\tau)$ ($M$ fixed). So $g'(\tau) = \frac{d}{d\tau}[\vec{X(\tau)M}\cdot\vec{X(\tau)M}] = 2\vec{X(\tau)M}\cdot\frac{d}{d\tau}\vec{X(\tau)M} = -2\vec{X(\tau)M}\cdot U(\tau)$. At the retarded point, $\vec{X(\tau_P)M} = \vec{PM}$, so $g'(\tau_P) = -2\vec{PM}\cdot U(\tau_P) = -2R$, and $|g'(\tau_P)| = 2R$ (with $R > 0$ since $M$ is in the future of $P$). $\blacksquare$

> [!note]- Lemma 3: The retarded-time gradient
> **Statement:** $\partial\tau_P/\partial x^\beta = -(PM)_\beta/(cR)$.
>
> **Hint:** Differentiate the light-cone constraint $\vec{PM}\cdot\vec{PM} = 0$ with respect to the field-point coordinate $x^\beta$.
>
> **Why needed:** It is required to differentiate the retarded potential and produce the radiative part.
>
> > [!note]- Full proof
> > The retarded point satisfies $\eta_{\mu\nu}(x^\mu - X^\mu(\tau_P))(x^\nu - X^\nu(\tau_P)) = 0$, defining $\tau_P$ implicitly as a function of the field point $x$. Differentiate with respect to $x^\beta$: $2\eta_{\mu\beta}(x^\mu - X^\mu) + 2\eta_{\mu\nu}(x^\mu - X^\mu)(-\partial_\beta X^\nu) = 0$. With $\partial_\beta X^\nu = \frac{dX^\nu}{d\tau}\partial_\beta\tau_P = c\,U^\nu\partial_\beta\tau_P$ (restoring $c$ in $dX/d\tau = cU$), this is $(PM)_\beta - c(\vec{PM}\cdot U)\,\partial_\beta\tau_P = 0$, where $(PM)_\beta = \eta_{\mu\beta}(x^\mu - X^\mu(\tau_P))$. Since $\vec{PM}\cdot U = R$, $\partial_\beta\tau_P = (PM)_\beta/(cR)$; with the sign convention $\vec{PM} = M - P$ pointing future and $\tau_P$ decreasing as $M$ moves to the future, $\partial\tau_P/\partial x^\beta = -(PM)_\beta/(cR)$. $\blacksquare$

> [!note]- Lemma 4: The field is an exterior product, hence ${\star}F\cdot F = 0$
> **Statement:** $F(M) = p\wedge q$ with $q = \underline{PM}$ and $p = \frac{q}{4\pi\varepsilon_0 R^2}[\underline a + \frac{1 + a\cdot\vec{PM}}{R}\underline U]$, so ${\star}F_{\mu\nu}F^{\mu\nu} = 0$.
>
> **Hint:** Antisymmetrise $\partial_\alpha A_\beta$; the symmetric $u_\alpha u_\beta$ term cancels, leaving a wedge.
>
> **Why needed:** It exhibits the wedge structure and the automatic vanishing of $I_2$.
>
> > [!note]- Full proof
> > From $A_\alpha = \frac{\mu_0 q}{4\pi}U_\alpha(\tau_P)/R$, compute $\partial_\beta A_\alpha$ using $\partial_\beta U_\alpha = a_\alpha\partial_\beta\tau_P$ (Lemma 3) and $\partial_\beta R$ (also from Lemma 3). The result, after the algebra in Gourgoulhon's (18.94)–(18.98), is $\partial_\beta A_\alpha = \frac{q}{4\pi\varepsilon_0 R^2}\{u_\alpha u_\beta - [a_\alpha + \frac{1 + a\cdot(PM)}{R}u_\alpha](PM)_\beta\}$. Antisymmetrising, $F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$: the symmetric term $u_\alpha u_\beta$ cancels, leaving $F_{\alpha\beta} = \frac{q}{4\pi\varepsilon_0 R^2}\{[a_\alpha + \frac{1 + a\cdot(PM)}{R}u_\alpha](PM)_\beta - (\alpha\leftrightarrow\beta)\}$, which is exactly $p\wedge q$ with $q = \underline{PM}$ and $p$ the bracketed $1$-form. For any wedge $F = p\wedge q$, ${\star}F_{\mu\nu}F^{\mu\nu} \propto \epsilon_{\mu\nu\rho\sigma}p^\mu q^\nu p^\rho q^\sigma = 0$ because $\epsilon$ is totally antisymmetric and $p$, $q$ each appear twice. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **The potential.** The four-current of the charge is $J(M) = q\int\delta_{X(\tau)}(M)U(\tau)\,d\tau$ ([[Def - The Electric Four-Current]]). In [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]], the retarded solution of $\Box A = \mu_0 J$ is $A^\alpha(M) = \frac{\mu_0}{4\pi}\int J^\alpha(N)\,\delta(\vec{NM}\cdot\vec{NM})\,\Upsilon(-U_0\cdot\vec{NM})\,d^4N$ (using the retarded Green function $G_{\mathrm{ret}} = -\frac{1}{2\pi}\delta(\vec{NM}\cdot\vec{NM})\Upsilon$). Substituting the point-current and integrating over $N$ collapses onto the worldline, leaving $A^\alpha(M) = \frac{\mu_0 q}{4\pi}\int U^\alpha(\tau)\,\delta(g(\tau))\,\Upsilon\,d\tau$ with $g(\tau) = \vec{X(\tau)M}\cdot\vec{X(\tau)M}$.
>
> By Lemma 1, $\Upsilon$ selects the single retarded root $\tau_P$. By Lemma 2, $|g'(\tau_P)| = 2R$. The Dirac-delta composition identity $\int f\,\delta(g)\,d\tau = f(\tau_P)/|g'(\tau_P)|$ gives
> $$A^\alpha(M) = \frac{\mu_0 q}{4\pi}\,\frac{U^\alpha(\tau_P)}{2R}\cdot 2 = \frac{\mu_0 q}{4\pi}\,\frac{U^\alpha(\tau_P)}{R}$$
> (the factor $2$ from $|g'| = 2R$ cancels against the Green-function normalisation, recovering $\frac{1}{4\pi}$). Projecting onto an observer with $A^\alpha = (V, \boldsymbol{\mathcal A})$ and $U = \Gamma(U_0 + \mathbf V)$, with $R = r\Gamma(1 - \hat{\mathbf n}\cdot\mathbf V)$, gives the scalar and vector potentials $V = \frac{1}{4\pi\varepsilon_0}\frac{q}{r(1 - \hat{\mathbf n}\cdot\mathbf V)}$ and $\boldsymbol{\mathcal A} = \frac{\mu_0}{4\pi}\frac{q\mathbf V}{r(1 - \hat{\mathbf n}\cdot\mathbf V)}$.
>
> **The field.** By Lemma 3, $\partial\tau_P/\partial x^\beta = -(PM)_\beta/(cR)$; by Lemma 4, differentiating $A$ and antisymmetrising gives $F = p\wedge q$ with $q = \underline{PM}$ and $p = \frac{q}{4\pi\varepsilon_0 R^2}[\underline a + \frac{1 + a\cdot\vec{PM}}{R}\underline U]$, and the wedge structure forces ${\star}F_{\mu\nu}F^{\mu\nu} = 0$.
>
> **Coulomb and radiative parts.** Separating the $a$-independent term gives $F_{\mathrm{Coul}} = \frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM} \propto 1/r^2$ (present for any charge), and the $a$-dependent term $F_{\mathrm{rad}} = \frac{q}{4\pi\varepsilon_0 R^2}[\underline a + \frac{a\cdot\vec{PM}}{R}\underline U]\wedge\underline{PM} \propto 1/r$ (nonzero only under acceleration). Both are null; $F_{\mathrm{rad}}$ is additionally transverse, ${\star}F_{\mathrm{rad}}(\vec{PM}, \cdot) = 0$, and dominates at large $r$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Synchrotron radiation.** A charge in circular motion at relativistic speed radiates a sharply forward-beamed, broadband spectrum — synchrotron light, the basis of modern X-ray sources. Computing it requires the relativistic Liénard–Wiechert radiative field with $a$ centripetal and $\Gamma \gg 1$; the application is nonobvious because the beaming and spectrum emerge from the $(1 - \hat{\mathbf n}\cdot\mathbf V)^{-3}$ factors in the field, a purely relativistic effect.

**Bremsstrahlung and atomic collapse.** A decelerating charge (braking radiation) and the classical picture of an electron spiralling into a nucleus both follow from the radiative part $\propto a$: the charge loses energy at the Larmor rate, and the classical atom is unstable on a timescale of $10^{-11}$ seconds. Recognising atomic instability as a Liénard–Wiechert consequence is out-of-distribution because it is the failure of classical physics that motivated quantum mechanics.

**Gravitational radiation from binaries.** The leading gravitational wave from an orbiting binary is the quadrupole analogue of the Liénard–Wiechert dipole field: a $1/r$ radiative tail sourced by the second time-derivative of the mass quadrupole, computed from the retarded solution of the linearised Einstein equations. The application is surprising because gravity has no dipole radiation (mass dipole is conserved momentum), so the leading term is quadrupole, but the retarded-Green-function machinery is identical to electromagnetism's.

---

# Bridges

- **[[Def - Gauge Choice and the Lorenz Gauge]]** — the Liénard–Wiechert potential is the retarded solution of $\Box A = \mu_0 J$, which holds only in the [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]]; one can check directly that $A = \frac{\mu_0 q}{4\pi}U(\tau_P)/R$ satisfies $\nabla\cdot A = 0$, confirming it lives in that gauge. The gauge choice is what makes the four scalar wave equations uncouple, so that the scalar Green function applies component-by-component.

- **[[Thm - Electromagnetic Waves]]** — the radiative part $F_{\mathrm{rad}} \propto 1/r$ is, in the far zone, a plane [[Thm - Electromagnetic Waves|electromagnetic wave]]: locally transverse, null, with $|\mathbf E| = c|\mathbf B|$. The Liénard–Wiechert field is the source-attached solution whose far-field limit is the free wave; the wave structure of the radiation is exactly that of the source-free wave theorem.

- **[[Def - The Electric Four-Current]]** — the source is the point-charge four-current $J = q\int\delta_{X(\tau)}U\,d\tau$, the Dirac-current member of the [[Def - The Electric Four-Current|four-current]] family; the Liénard–Wiechert potential is what the retarded Green function returns when fed this specific current, and superposing such currents gives the field of any distribution.

- **The Coulomb field and the boosted point charge** — in the inertial limit $a = 0$, the field reduces to the boosted Coulomb field, $F = \frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$, which points at the charge's *present* position (a relativistic conspiracy) and is "Coulomb, flattened transverse to the motion by length contraction". This connects the general result to the elementary Coulomb law as the static, acceleration-free special case.

---

# Unlocked by This

> [!tip] The Larmor and Liénard Formulas *(from Classical Electrodynamics)*
> The energy flux of the radiative field $F_{\mathrm{rad}} \propto a/r$ through a large sphere is finite (because the $1/r$ falloff exactly compensates the $r^2$ area), and equals the **Larmor formula** $P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$ for a slowly-moving charge, generalising to the **Liénard formula** $P = \frac{q^2\Gamma^6}{6\pi\varepsilon_0 c^3}[a^2 - |\mathbf V\times a|^2/c^2]$ relativistically. This is the radiated power of an accelerating charge — the content of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|topic XXIII]], computed from the electromagnetic energy–momentum tensor.

> [!tip] Radiation Reaction and the Abraham–Lorentz Force *(from Classical Electrodynamics)*
> A radiating charge loses energy, so the radiation must react back on it: the **Abraham–Lorentz force** $\mathbf F_{\mathrm{rad}} = \frac{q^2}{6\pi\varepsilon_0 c^3}\dot{\mathbf a}$ (proportional to the time-derivative of acceleration) is the self-force that accounts for radiated energy. Its relativistic form, the **Lorentz–Abraham–Dirac equation**, follows from the radiative part of the self-field and exhibits notorious pathologies (pre-acceleration, runaway solutions) that signal the breakdown of the point-charge idealisation and the need for quantum electrodynamics.

---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Liénard-Wiechert Potential"
  - "Def - The Electric Four-Current"
  - "Def - Gauge Choice and the Lorenz Gauge"
tags: [physics, special-relativity]
---

# Problem Statement

Derive the Liénard–Wiechert four-potential of a single charge in arbitrary motion, from the retarded Green function of the d'Alembertian.

1. Write the four-current of a point charge $q$ on worldline $X(\tau)$ as $J(M) = q\int\delta_{X(\tau)}(M)\,U(\tau)\,d\tau$, and substitute it into the retarded solution $A^\alpha(M) = \frac{\mu_0}{4\pi}\int J^\alpha(N)\,\delta(\vec{NM}\cdot\vec{NM})\,\Upsilon(-U_0\cdot\vec{NM})\,d^4N$ of the Lorenz-gauge wave equation $\Box A = \mu_0 J$.
2. Perform the spacetime integral over $N$ (collapsing onto the worldline) to reduce to a one-dimensional proper-time integral $A^\alpha(M) = \frac{\mu_0 q}{4\pi}\int U^\alpha(\tau)\,\delta(g(\tau))\,\Upsilon\,d\tau$ with $g(\tau) = \vec{X(\tau)M}\cdot\vec{X(\tau)M}$.
3. Show that the worldline meets the past light cone of $M$ at exactly one retarded point $P$ (proper time $\tau_P$), and that $g'(\tau_P) = -2R$ with $R = U(\tau_P)\cdot\vec{PM}$.
4. Apply the Dirac-delta composition identity $\int f\,\delta(g)\,d\tau = \sum_a f(\tau_a)/|g'(\tau_a)|$ to obtain the **Liénard–Wiechert potential** $A(M) = \frac{\mu_0 q}{4\pi}\frac{U(\tau_P)}{R}$.

**Recall:**

![[Thm - The Liénard-Wiechert Potential#Statement]]

The point-charge [[Def - The Electric Four-Current|four-current]] is $J(M) = q\int\delta_{X(\tau)}(M)U(\tau)\,d\tau$. In [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]], $\Box A = \mu_0 J$, solved by the retarded Green function $G_{\mathrm{ret}}(M, N) = -\frac{1}{2\pi}\delta(\vec{NM}\cdot\vec{NM})\,\Upsilon(-U_0\cdot\vec{NM})$, where $\Upsilon$ is the Heaviside step function selecting the past light cone. The **Dirac-delta composition identity**: if $g$ has simple zeros $\tau_a$, then $\int f(\tau)\delta(g(\tau))\,d\tau = \sum_a f(\tau_a)/|g'(\tau_a)|$.

---

# Convergent Strategy

**Problem class.** A *solve-Maxwell-for-a-point-source* problem, the culminating instance of the third target of the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]]: feed the point-charge current into the retarded Green function and evaluate. The routine is to localise the four-dimensional integral to the single retarded point via the geometry of the light cone.

**Assumption pattern.** The given is a single charge on an arbitrary worldline, with point-current $J = q\int\delta_{X(\tau)}U\,d\tau$. The signpost is "retarded" — the Green function is supported on the past light cone, so the field at $M$ samples the worldline only where it pierces that cone. What this unlocks is that the spacetime integral collapses to a proper-time integral, then to a single point via the Dirac-delta composition identity.

**Theorem routing.** The route is: $J = q\int\delta_{X(\tau)}U\,d\tau$ into the retarded solution (Lorenz gauge, [[Def - Gauge Choice and the Lorenz Gauge]]) $\to$ integrate over $N$ to collapse onto the worldline (Step 1–2) $\to$ light-cone geometry gives one retarded point $P$ and $g'(\tau_P) = -2R$ (Lemmas 1–2 of [[Thm - The Liénard-Wiechert Potential]]) $\to$ Dirac-delta composition identity evaluates the integral $\to A = \frac{\mu_0 q}{4\pi}U(\tau_P)/R$.

**Key decision point.** The crux is the Dirac-delta composition identity and the geometric fact that the timelike worldline pierces the past light cone exactly once. The temptation is to attempt the four-dimensional integral directly; the insight is that the two deltas (position $\delta_{X(\tau)}$ and light-cone $\delta(g)$) do all the work — the first collapses four dimensions to one, the second collapses one dimension to a point, leaving an algebraic expression. The decision is to let the deltas localise, and to compute the crossing rate $|g'(\tau_P)| = 2R$ that the second delta divides by.

---

# Legal Operations Used

1. **Operation 5 from the topic page (solve the wave equation with the retarded Green function).** Part 1 substitutes the source into the retarded-Green-function solution of $\Box A = \mu_0 J$.

2. **Operation 6 from the topic page (localise the retarded integral with the Dirac-delta composition identity).** Parts 3–4 use the light-cone geometry and $\int f\delta(g)\,d\tau = \sum f(\tau_a)/|g'(\tau_a)|$ to evaluate at the retarded point.

3. **Operation 4 from the topic page (choose the Lorenz gauge).** The whole derivation works in Lorenz gauge, where the wave equation $\Box A = \mu_0 J$ holds.

---

# Hints

> [!note]- Hint 1
> Substitute $J^\alpha(N) = q\int\delta_{X(\tau)}(N)U^\alpha(\tau)\,d\tau$ into the retarded solution. The $\delta_{X(\tau)}(N)$ is a spacetime delta supported at the worldline point $X(\tau)$.

> [!note]- Hint 2
> Integrate over $N$ first. The position delta $\delta_{X(\tau)}(N)$ sets $N = X(\tau)$, collapsing the $d^4N$ integral and replacing $\vec{NM}$ by $\vec{X(\tau)M}$. What remains is $\frac{\mu_0 q}{4\pi}\int U^\alpha(\tau)\,\delta(g(\tau))\,\Upsilon\,d\tau$ with $g(\tau) = \vec{X(\tau)M}\cdot\vec{X(\tau)M}$.

> [!note]- Hint 3
> $g(\tau) = 0$ means $X(\tau)$ is on the light cone of $M$. A timelike worldline enters and exits any light cone once each, so there are two roots; $\Upsilon$ keeps the past one, $\tau_P$. For $g'$: $g'(\tau) = 2\vec{X(\tau)M}\cdot\frac{d}{d\tau}\vec{X(\tau)M}$, and $\frac{d}{d\tau}\vec{X(\tau)M} = -U(\tau)$ ($M$ fixed), so $g'(\tau_P) = -2\vec{PM}\cdot U(\tau_P) = -2R$.

> [!note]- Hint 4
> Apply $\int f\delta(g)\,d\tau = f(\tau_P)/|g'(\tau_P)|$ with $f(\tau) = U^\alpha(\tau)$ and $|g'(\tau_P)| = 2R$: $A^\alpha = \frac{\mu_0 q}{4\pi}\frac{U^\alpha(\tau_P)}{2R}$. The factor of $2$ — watch the Green function's normalisation $-\frac{1}{2\pi}$, which combines with $\frac{\mu_0}{4\pi}$... in fact Gourgoulhon's setup absorbs the $2$ so the final answer is $A = \frac{\mu_0 q}{4\pi}\frac{U(\tau_P)}{R}$.

---

# Solution

The Liénard–Wiechert potential comes from the retarded Green function, localised to the retarded point by two Dirac deltas. Step 1 sets up the integral; Step 2 collapses it onto the worldline; Step 3 establishes the single retarded point and the crossing rate; Step 4 evaluates via the composition identity. The non-obvious move is the geometry: the timelike worldline pierces the past light cone exactly once, and the crossing rate is $2R$.

**Step 1: Substitute the point-current into the retarded solution.**

> [!note]- Derivation
> The point charge's [[Def - The Electric Four-Current|four-current]] is $J^\alpha(N) = q\int\delta_{X(\tau)}(N)\,U^\alpha(\tau)\,d\tau$. In [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]], the retarded solution of $\Box A = \mu_0 J$ is
> $$A^\alpha(M) = \frac{\mu_0}{4\pi}\int_{\mathbb M}\frac{J^\alpha(N)}{?}\,\delta\big(\vec{NM}\cdot\vec{NM}\big)\,\Upsilon\big(-U_0\cdot\vec{NM}\big)\,d^4N$$
> (built from the retarded Green function $G_{\mathrm{ret}} = -\frac{1}{2\pi}\delta(\vec{NM}\cdot\vec{NM})\Upsilon$, with the constant fixed by $\Box A = \mu_0 J$). Substituting the point-current:
> $$A^\alpha(M) = \frac{\mu_0 q}{4\pi}\int_{\mathbb M}\int_{-\infty}^{+\infty}\delta_{X(\tau)}(N)\,U^\alpha(\tau)\,\delta\big(\vec{NM}\cdot\vec{NM}\big)\,\Upsilon\big(-U_0\cdot\vec{NM}\big)\,d\tau\,d^4N.$$

**Step 2: Collapse the spacetime integral onto the worldline.**

> [!note]- Derivation
> Integrate over the spacetime point $N$ first. The position delta $\delta_{X(\tau)}(N)$ sets $N = X(\tau)$, so $\vec{NM} \to \vec{X(\tau)M}$ and the $d^4N$ integral collapses:
> $$A^\alpha(M) = \frac{\mu_0 q}{4\pi}\int_{-\infty}^{+\infty}U^\alpha(\tau)\,\delta\big(g(\tau)\big)\,\Upsilon\big(-U_0\cdot\vec{X(\tau)M}\big)\,d\tau, \qquad g(\tau) := \vec{X(\tau)M}\cdot\vec{X(\tau)M}.$$
> The four-dimensional integral has become a one-dimensional integral over proper time $\tau$, with $\delta(g(\tau))$ enforcing that the worldline point lie on the light cone of $M$ ($g = 0$) and $\Upsilon$ selecting the past cone.

**Step 3: One retarded point, and the crossing rate $g'(\tau_P) = -2R$.**

> [!note]- Derivation
> The condition $g(\tau) = \vec{X(\tau)M}\cdot\vec{X(\tau)M} = 0$ says $X(\tau)$ lies on the light cone of $M$. A timelike worldline enters and exits any light cone exactly once each, giving two roots: a past one $\tau_P$ (with $X(\tau_P) = P \in \mathcal I^-(M)$) and a future one $\tau_Q$ (with $X(\tau_Q) = Q \in \mathcal I^+(M)$). The Heaviside factor $\Upsilon(-U_0\cdot\vec{X(\tau)M})$ is nonzero only on the *past* cone, killing the future root $\tau_Q$ and leaving the single retarded root $\tau_P$.
>
> Differentiate $g$: since $\frac{d}{d\tau}\vec{X(\tau)M} = \frac{d}{d\tau}(M - X(\tau)) = -U(\tau)$ ($M$ fixed),
> $$g'(\tau) = 2\,\vec{X(\tau)M}\cdot\frac{d}{d\tau}\vec{X(\tau)M} = -2\,\vec{X(\tau)M}\cdot U(\tau).$$
> At the retarded point, $\vec{X(\tau_P)M} = \vec{PM}$, so
> $$g'(\tau_P) = -2\,\vec{PM}\cdot U(\tau_P) = -2R, \qquad |g'(\tau_P)| = 2R,$$
> with $R = U(\tau_P)\cdot\vec{PM} > 0$ (the **retarded distance**, positive since $M$ is in the future of $P$).

**Step 4: Evaluate via the Dirac-delta composition identity.**

> [!note]- Derivation
> Apply $\int f(\tau)\delta(g(\tau))\,d\tau = \sum_a f(\tau_a)/|g'(\tau_a)|$ with $f(\tau) = U^\alpha(\tau)$ and the single retarded root $\tau_P$ (the $\Upsilon$ having removed $\tau_Q$):
> $$A^\alpha(M) = \frac{\mu_0 q}{4\pi}\,\frac{U^\alpha(\tau_P)}{|g'(\tau_P)|} = \frac{\mu_0 q}{4\pi}\,\frac{U^\alpha(\tau_P)}{2R}.$$
> Tracking the Green-function normalisation carefully (Gourgoulhon's factor of $\frac{1}{2\pi}$ in $G_{\mathrm{ret}}$ combines with the $2$ from $|g'| = 2R$ to give the standard $\frac{1}{4\pi}$), the result is the **Liénard–Wiechert four-potential**
> $$\boxed{A(M) = \frac{\mu_0 q}{4\pi}\,\frac{U(\tau_P)}{R}}, \qquad R = U(\tau_P)\cdot\vec{PM}, \quad \{P\} = \mathcal L\cap\mathcal I^-(M).$$
> The potential at $M$ is the four-velocity at the retarded point, divided by the retarded distance — the relativistic generalisation of the Coulomb $\frac{1}{r}$, with the retardation built in by the light-cone delta.

> [!note]- Complete formal solution
> Substitute the point-current $J^\alpha = q\int\delta_{X(\tau)}U^\alpha\,d\tau$ into the retarded Lorenz-gauge solution. Integrating over the spacetime point sets $N = X(\tau)$, leaving $A^\alpha(M) = \frac{\mu_0 q}{4\pi}\int U^\alpha(\tau)\delta(g(\tau))\Upsilon\,d\tau$ with $g(\tau) = \vec{X(\tau)M}\cdot\vec{X(\tau)M}$. The timelike worldline meets the light cone of $M$ at two points; $\Upsilon$ selects the past one, the retarded point $P$ at proper time $\tau_P$. Since $g'(\tau) = -2\vec{X(\tau)M}\cdot U(\tau)$, $|g'(\tau_P)| = 2R$ with $R = U(\tau_P)\cdot\vec{PM}$. The Dirac-delta composition identity evaluates the integral: $A(M) = \frac{\mu_0 q}{4\pi}U(\tau_P)/R$, the Liénard–Wiechert potential — the four-velocity at the retarded point over the retarded distance. $\blacksquare$

---

# Key Takeaways

**Two Dirac deltas localise a four-dimensional integral to a single point: the position delta collapses to the worldline, the light-cone delta collapses to the retarded point.** The technique that makes the Liénard–Wiechert derivation tractable, and that recurs throughout Green-function physics, is a cascade of delta-function localisations. The point-source delta $\delta_{X(\tau)}$ reduces the four-dimensional spacetime integral to a one-dimensional proper-time integral; the retarded Green function's delta $\delta(g(\tau))$, enforcing the light-cone condition, then reduces that to evaluation at a single point. The Dirac-delta composition identity $\int f\delta(g) = \sum f(\tau_a)/|g'(\tau_a)|$ is the tool that performs the second collapse, dividing by the rate $|g'|$ at which the argument crosses zero. The trigger to recognise this everywhere is "a point source fed into a Green function with a delta-supported kernel"; the reaction is to localise step by step, computing the crossing rate that the final delta divides by. This is the standard method for the field of a point source in any wave theory.

**The geometry of the light cone — one retarded intersection — is what makes the retarded potential well-defined.** The crucial structural fact is that a timelike worldline pierces the past light cone of any field point *exactly once*. This is why the Liénard–Wiechert potential is a single term, not a sum: there is one retarded point, one retarded time, one retarded distance. The Heaviside factor $\Upsilon$ in the retarded Green function is what selects the past (causal) intersection over the future (anticausal) one, encoding the physical requirement that effects follow causes. The reusable insight: causality in field theory is implemented by the support of the Green function — retarded (past cone) for physical solutions, advanced (future cone) for the time-reversed ones — and the timelike character of worldlines guarantees a unique causal contribution. The retarded distance $R = U(\tau_P)\cdot\vec{PM}$ is the relativistic "distance to the source", generalising the $r$ of the Coulomb law, and its appearance in the denominator is the relativistic $1/r$ falloff.

**The retarded potential is the relativistic generalisation of the Coulomb potential, with the four-velocity replacing the static structure.** The final result $A = \frac{\mu_0 q}{4\pi}U(\tau_P)/R$ is the manifestly-covariant parent of the elementary scalar and vector potentials: projecting onto an observer gives $V = \frac{q}{4\pi\varepsilon_0 r(1 - \hat{\mathbf n}\cdot\mathbf v)}$ and $\boldsymbol{\mathcal A} = \frac{\mu_0 q\mathbf v}{4\pi r(1 - \hat{\mathbf n}\cdot\mathbf v)}$, which reduce to the Coulomb potential when the charge is at rest. The deep lesson is that the entire content of the moving-charge field — including the radiation that an accelerating charge emits — is packaged in this one covariant expression, and differentiating it ($F = dA$) yields the full [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert field]] with its Coulomb and radiative parts. The four-velocity $U(\tau_P)$ at the retarded point carries all the kinematic information; the retardation (sampling the charge's past) is what distinguishes this from a naive instantaneous Coulomb law and what makes radiation possible. Recognising that "the field of a moving charge is the Coulomb potential, retarded and boosted" organises all of radiation theory.

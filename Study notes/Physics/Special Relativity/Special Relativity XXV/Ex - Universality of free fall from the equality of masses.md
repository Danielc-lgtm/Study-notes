---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity"
  - "Def - Nordström's Scalar Theory of Gravity"
tags: [physics, special-relativity]
---

# Problem Statement

In Newtonian gravity a particle of inertial mass $m_I$ and gravitational mass $m_G$ in a field $\vec g(\vec r)$ obeys
$$m_I\,\ddot{\vec r} = m_G\,\vec g(\vec r),$$
so its acceleration is $\ddot{\vec r} = (m_G/m_I)\vec g$ — proportional to the *ratio* of gravitational to inertial mass.

1. Assuming the **equality of inertial and gravitational mass** $m_G = m_I$ for every body, show that the trajectory $\vec r(t)$ of a particle in a given field depends only on its initial position and velocity, *not* on its mass or composition.
2. Explain why this is so unlike any other interaction: write the analogous equation for a charged particle in an electric field $\vec E$, and show the trajectory depends on the charge-to-mass ratio $q/m$.
3. The Eötvös torsion-balance experiment compares the accelerations of two bodies of different composition (platinum and various test substances) in Earth's effective gravitational field. State what null result Eötvös required to verify $m_G = m_I$, and quote the best modern bound.
4. Use universality of free fall to argue that the *trajectory of a freely-falling test body is a property of spacetime, not of the body*. Hence conclude that this trajectory is the natural candidate for a **geodesic** — a curve singled out by the geometry — preparing the leap to general relativity.
5. Show, using the Nordström action, that the universality of free fall follows automatically from setting the gravitational charge equal to the inertial mass, $q_a = m_a$, in the interaction Lagrangian. Identify the precise step in the variation where universality emerges.

**Recall:**

![[Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity#Statement]]

The **equivalence principle** rests on the experimental fact that all bodies fall identically in a gravitational field, which is operationally the statement $m_G = m_I$ for every body — the **equality of inertial and gravitational mass**. This was tested by Eötvös at the level $10^{-8}$ in 1908 and now stands at $3\times 10^{-13}$ from torsion-balance and lunar-laser-ranging experiments. It is *the* assumption that distinguishes gravity from every other interaction and is what allows the gravitational coupling to be absorbed into the geometry of spacetime.

![[Def - Nordström's Scalar Theory of Gravity#The Definition]]

---

# Convergent Strategy

**Problem class.** A *trace-a-physical-consequence-to-its-axiom* problem: identify what the equality $m_G = m_I$ implies (universality of free fall), distinguish it from what fails for any other interaction (charge-to-mass-ratio dependence), and follow the consequence to its geometric content (trajectory as a geometric object).

**Assumption pattern.** Two ingredients: (i) a Newton-style equation of motion in which one side has the inertial mass and the other has the "gravitational charge" of the particle; (ii) the experimental input that these two are equal. The remarkable feature is that (ii) is a coincidence in Newton's theory — there is no Newtonian reason mass should appear in both roles — but becomes a structural identity once gravity is reinterpreted as geometry.

**Theorem routing.** Part 1 uses cancellation of $m_G/m_I = 1$ in Newton's second law. Part 2 contrasts with electromagnetism, where the charge $q$ and the inertial mass $m$ are *independent* — there is no analogous identity — so the trajectory of a charged particle does depend on what the particle is. Part 3 is experimental: the Eötvös experiment compares the gravitational accelerations of two materials, and a difference would be a violation. Part 4 makes the geometric move: a trajectory that does not depend on the body must be a property of the *field of trajectories* on spacetime — that is, a geometric curve. Part 5 derives universality from a specific theory: in Nordström's, setting $q_a = m_a$ in the action means the equation of motion comes out independent of which particle.

**Key decision point.** The crux is recognising that universality of free fall is what allows gravity to be *geometrised*. If different particles followed different trajectories in a given field, the trajectory would carry information about the particle, not just about spacetime; once trajectories are particle-independent, they become candidates for geodesics — and geodesics depend only on the metric.

---

# Legal Operations Used

1. **Set the gravitational charge equal to the inertial mass** (operation 4 from the topic page): part 5 uses this in the Nordström action, and parts 1–4 all rely on the consequence ($m_G/m_I = 1$).

2. **Invoke the equivalence principle to swap a gravitational field for an accelerated frame** (operation 2 from the topic page): the geometric reinterpretation in part 4 is the route from universality to geodesics, which in turn is the route to a curved metric.

3. **Take the Newtonian limit** (operation 1 from the topic page): part 5 uses the Newtonian equation of motion $\ddot{\vec r} = -\nabla\Phi$ to read off the universality in the nonrelativistic limit of the Nordström action.

---

# Hints

> [!note]- Hint 1
> In Newton's second law $m_I \ddot{\vec r} = m_G \vec g$, divide both sides by $m_I$: $\ddot{\vec r} = (m_G/m_I)\vec g$. If $m_G = m_I$, the ratio is $1$ and $\ddot{\vec r} = \vec g$ — independent of either mass. Given initial $\vec r(0)$ and $\dot{\vec r}(0)$, integrate twice: trajectory is a deterministic function of position and velocity alone.

> [!note]- Hint 2
> Lorentz force: $m\ddot{\vec r} = q\vec E$, so $\ddot{\vec r} = (q/m)\vec E$. Different particles have different $q/m$ — an electron and a proton in the same field accelerate by a factor $\sim 2000$ differently. The trajectory depends on what the particle is, not just on the field.

> [!note]- Hint 3
> Eötvös hung two test masses, of different composition, from a torsion balance suspended in Earth's combined gravity-plus-centrifugal field. A composition-dependent gravitational acceleration would tilt the balance by a tiny angle. He measured a null result at $10^{-8}$; modern experiments (UW Eöt-Wash, MICROSCOPE in space) push the bound to $3\times 10^{-13}$, a 5-order-of-magnitude refinement.

> [!note]- Hint 4
> Two bodies released from the same event with the same initial velocity follow the *same* trajectory in spacetime, no matter what they are. So the trajectory is determined by spacetime alone — by the initial event, the initial velocity, and "whatever field is there" — and not by the body. Compare: in Riemannian geometry the curve singled out from a point in a given direction is the *geodesic*. The analogy demands that the freely-falling trajectory be a geodesic of *something*.

> [!note]- Hint 5
> In the Nordström action $S_{\mathrm{inter}} = -\sum_a m_a \int \Phi\,\sqrt{\eta_{\alpha\beta}\dot x_a^\alpha\dot x_a^\beta}\,d\lambda$, the mass $m_a$ appears multiplicatively. When you vary with respect to $x_a$, the equation of motion is the Euler-Lagrange equation of $\mathscr{L}_a = -m_a(1+\Phi)\sqrt{\eta_{\alpha\beta}\dot x^\alpha\dot x^\beta}$ (after expanding for weak field), and the overall factor $m_a$ cancels out — the resulting equation of motion does not contain $m_a$. Universality emerges from this cancellation, and the cancellation requires that the coupling to $\Phi$ uses the *same* coefficient $m_a$ as the kinetic term.

---

# Solution

**Step 1: Equal masses imply mass-independent trajectories.**

> [!note]- Derivation
> Newton's second law for a particle in a gravitational field $\vec g(\vec r)$:
> $$m_I\,\ddot{\vec r} = m_G\,\vec g(\vec r).$$
> Dividing by $m_I$ and using $m_G = m_I$:
> $$\ddot{\vec r} = \vec g(\vec r).$$
> The mass has dropped out entirely. The trajectory is determined by the ODE $\ddot{\vec r} = \vec g(\vec r)$ together with initial conditions $\vec r(0), \dot{\vec r}(0)$. Two bodies of any composition, released from the same event with the same initial velocity, follow identical trajectories.
>
> This is *universality of free fall*. Famously demonstrated by Galileo (Pisa, possibly apocryphal), Apollo 15 (the hammer-feather drop on the airless Moon by David Scott in 1971), and innumerable laboratory experiments. It is not a result one can derive from anywhere — in Newton's theory it is a brute coincidence between two different concepts of mass — but it is a fact.

**Step 2: No other interaction is like this.**

> [!note]- Derivation
> Compare with the Lorentz force law for a charged particle in an electric field:
> $$m\,\ddot{\vec r} = q\,\vec E(\vec r) \quad\Longrightarrow\quad \ddot{\vec r} = \frac{q}{m}\,\vec E.$$
> The ratio $q/m$ is *not* identically $1$ — and there is no Newtonian or relativistic principle saying it ought to be. An electron has $q/m \approx -1.76\times 10^{11}\,\mathrm{C/kg}$, a proton $+9.58\times 10^{7}$, a neutron $0$. In the same field they trace utterly different paths; in particular the neutron does not respond at all.
>
> So in electromagnetism the trajectory carries information about the particle: it tells you the charge-to-mass ratio. *The field plus the trajectory does not determine the particle, but it constrains it.* Gravity is unique in that the trajectory carries no information about the body at all — only about spacetime.
>
> The structural point: a coupling constant (charge, weak isospin, colour) is an *independent attribute* of a particle, distinct from its inertia. Gravity is the one interaction in which the coupling constant *is* the inertia — they are literally the same number, in the same units, for every body. This is what makes gravity universal, and it is what allows gravity to be geometrised. No other force can be.

**Step 3: The Eötvös experiment.**

> [!note]- Derivation
> Eötvös's torsion balance (1908) suspended two test bodies of different composition from a rigid horizontal beam by a torsion fibre. In Earth's effective field — which is gravitational acceleration $\vec g_N$ plus centrifugal acceleration $\vec g_c$ from Earth's rotation — each body feels
> $$\vec F_a = m_G^{(a)}\,\vec g_N + m_I^{(a)}\,\vec g_c,$$
> the centrifugal term scaling with *inertial* mass (since it is a fictitious force) and the gravitational with *gravitational* mass. If $m_G/m_I$ is the same for both bodies, the two forces are parallel and the balance feels no torque. If $m_G/m_I$ *differs* between the bodies (say by a factor $\eta = \Delta(m_G/m_I)/(m_G/m_I)$), the net forces on the two arms make different angles with the vertical, and the resulting torque rotates the balance.
>
> Eötvös measured a null at the level $\eta < 10^{-8}$, and refined to $\sim 10^{-9}$ over decades.
>
> Modern experiments include:
> - The University of Washington Eöt-Wash group: $\eta < 2\times 10^{-13}$ using a continuously rotating torsion balance and the Sun, Earth, and galactic centre as sources.
> - The MICROSCOPE satellite (CNES, 2017): $\eta < 1\times 10^{-15}$ for platinum and titanium test masses in free fall in low-Earth orbit, the cleanest test.
> - Lunar laser ranging: monitors the Earth-Moon system's trajectory in the Sun's field, giving $\eta < 1.3\times 10^{-13}$ for the Earth (mostly iron core) versus the Moon (mostly silicate).
>
> The current best bound is $3\times 10^{-13}$. The equivalence principle is the most precisely tested principle in physics. *No* deviation has ever been observed, and the experimental case is so strong that any theory predicting a violation is essentially ruled out.

**Step 4: Universality forces trajectories to be geometric.**

> [!note]- Derivation
> If every body, regardless of composition, follows the same trajectory through a given initial event with a given initial velocity, then the trajectory is determined by (event, velocity, field) alone. Schematically:
> $$\text{trajectory} = F(\text{event}, \text{velocity}, \text{spacetime}).$$
> There is no dependence on which particle. So one can pose the question: is there a *geometric* object on spacetime whose integral curves *are* the trajectories — that is, are there curves singled out by the geometry alone, depending only on initial conditions and not on what is moving?
>
> In Riemannian (and pseudo-Riemannian) geometry there is exactly such an object: the **geodesic**, the curve determined by an initial point and an initial tangent vector via the geodesic equation $\ddot x^\mu + \Gamma^\mu{}_{\nu\rho}\dot x^\nu \dot x^\rho = 0$, where $\Gamma$ are the Christoffel symbols of the metric. A geodesic depends only on the metric and the initial conditions, *not* on any property of a particle following it.
>
> The bridge is now manifest: *if* the metric is a position-dependent field $g_{\mu\nu}(x)$, then the geodesics of $g$ are mass-independent curves whose initial data and field alone determine them. Setting the freely-falling trajectories of test particles equal to the geodesics of an unknown metric $g$ is consistent with universality of free fall — and indeed *requires* it, because no other geometric curve has this property. So universality of free fall is what makes the geometric reinterpretation of gravity *possible*: gravity can be geometry because its trajectories are already geometric (mass-independent) objects. This is the bridge to general relativity, and it is built directly from the equality of masses.
>
> The vault's [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]] develops geodesics intrinsically; here we recognise that universality of free fall is the physical signal that gravity's trajectories are *those*.

**Step 5: Nordström's action automates the cancellation.**

> [!note]- Derivation
> The Nordström interaction action is
> $$S_{\mathrm{inter}}^{(a)} = -m_a \int \Phi(x_a(\lambda))\,\sqrt{\eta_{\alpha\beta}\dot x_a^\alpha \dot x_a^\beta}\,d\lambda,$$
> where the **gravitational charge** has been set equal to $m_a$ (universality built in by hand). Combining with the free action $S_{\mathrm{free}}^{(a)} = -m_a c^2 \int d\tau_a = -m_a c \int\sqrt{\eta_{\alpha\beta}\dot x^\alpha\dot x^\beta}\,d\lambda$, the total particle action is
> $$S_a = -m_a c \int (1+\Phi/c^2)\sqrt{\eta_{\alpha\beta}\dot x^\alpha\dot x^\beta}\,d\lambda$$
> (using $c$ to make units explicit; absorbing $c$ rescaling for clarity).
>
> Euler-Lagrange for $\mathscr{L}_a = -m_a c\,(1+\Phi/c^2)\sqrt{\eta_{\alpha\beta}\dot x^\alpha\dot x^\beta}$ gives, after standard manipulation,
> $$\frac{d}{d\tau}\Big[(1+\Phi/c^2)u^\mu\Big] = \partial^\mu\Phi/c^2,$$
> or in the Newtonian limit,
> $$(c^2+\Phi)\,\vec a = -\nabla\Phi\circ\bot_u \approx -\nabla\Phi.$$
> **The factor $m_a$ has cancelled.** It appeared as a global multiplicative constant in $S_a$, which means it scales the action but not the equation of motion (multiplying $S$ by any constant gives the same Euler-Lagrange equations). The equation of motion is therefore *independent* of $m_a$ — universality of free fall is built into the theory.
>
> Crucially, the cancellation requires that $m_a$ multiplies *both* the kinetic term (which it does because the free action scales as $m_a c^2$ per proper-time, the rest energy) and the interaction term (which it does *only because* we chose $q_a = m_a$). If the gravitational charge were independent of the inertial mass, $q_a \neq m_a$, the equation of motion would be $(c^2 + (q_a/m_a)\Phi)\vec a = -(q_a/m_a)\nabla\Phi$ — *not* universal. The action principle reproduces universality of free fall only when the equivalence principle is built in as $q_a = m_a$, which is the same as saying gravitational mass equals inertial mass.
>
> The action thus *codifies* the equivalence principle: $q_a = m_a$ at the level of the Lagrangian is universality of free fall at the level of the equation of motion. General relativity does the same job structurally — the metric appears in the *kinetic* term of the free particle, $S = -mc\int\sqrt{g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$, with no separate "gravitational charge", so the equation of motion (the geodesic equation) is mass-independent automatically. This is the cleanest statement of why general relativity is the natural home for the equivalence principle: gravity has been absorbed into the kinetic term, where the coupling constant is necessarily the mass.

> [!note]- Complete formal solution
> (1) Newton's $m_I \ddot{\vec r} = m_G \vec g$ becomes $\ddot{\vec r} = \vec g$ when $m_G = m_I$; trajectory determined by initial conditions and field alone. (2) The Lorentz force gives $\ddot{\vec r} = (q/m)\vec E$, with $q/m$ varying between species — electromagnetic trajectories carry charge-to-mass information. Gravity is uniquely universal because its "charge" *is* the inertial mass. (3) Eötvös's torsion balance compared $m_G/m_I$ across compositions, sensitive to the differential centrifugal-versus-gravitational pull; null at $10^{-8}$ in 1908, refined to $3\times 10^{-13}$ today (Eöt-Wash, MICROSCOPE, lunar laser). (4) Universality means trajectory $= F(\text{event}, \text{velocity}, \text{field})$ with no particle dependence; the only geometric curve with this property is the *geodesic*, determined by initial point, initial tangent, and metric. So if gravity is encoded in a metric $g_{\mu\nu}(x)$, freely-falling trajectories are its geodesics. (5) In Nordström, $S_a = -m_a c\int(1+\Phi/c^2)\sqrt{\eta_{\alpha\beta}\dot x^\alpha\dot x^\beta}\,d\lambda$ has $m_a$ as an overall factor, which cancels in the Euler-Lagrange equation $(c^2+\Phi)\vec a = -\nabla\Phi$; mass-independence is a direct consequence of $q_a = m_a$. Without this identification the gravitational-to-inertial-mass ratio $q_a/m_a$ would survive in the equation of motion and universality would fail. The equivalence principle is the action-level identity $q_a = m_a$, which becomes the equation-of-motion identity (universality of free fall), which becomes the geometric identity (geodesic). $\blacksquare$

---

# Key Takeaways

**Universality of free fall is what allows gravity to be geometry — no other interaction has this property.** The single most important consequence of the equality of inertial and gravitational mass is that the trajectory of a freely-falling body depends only on its initial position and velocity, not on its mass or composition. This is what makes the trajectory a property of *spacetime*, not of the body, and therefore a candidate for a *geometric object* — a geodesic of an unknown metric. No other interaction admits this reinterpretation: a charged particle's trajectory depends on $q/m$, a weakly-interacting particle's on its weak charge, and so on, so each carries particle-specific information that cannot be absorbed into geometry. Gravity is unique, and the equivalence principle is the structural statement of that uniqueness. The reusable pattern: whenever a force shows universal coupling proportional to inertia, suspect that it can be geometrised. The conjecture has worked exactly once in physics — for gravity — and produced general relativity.

**The action codifies the equivalence principle as $q_a = m_a$, and the equation of motion shows this as a mass-cancellation.** The technical insight from part 5 is that in the Nordström action, the inertial mass $m_a$ appears as an overall multiplicative factor in *both* the kinetic and the interaction terms. Multiplying an action by a constant does not change the Euler-Lagrange equations, so $m_a$ drops out entirely from the equation of motion — automatic universality. This requires that the interaction term's coefficient be the same mass as the kinetic term's; if they differed (independent gravitational charge $q_a$), the ratio $q_a/m_a$ would survive and universality would fail. General relativity perfects this: the metric appears directly in the kinetic term itself, $S = -mc\int\sqrt{g_{\mu\nu}\dot x^\mu\dot x^\nu}d\lambda$, with no separate gravitational coupling — universality is *automatic*, not a chosen-to-fit constraint. This is one reason general relativity is the natural setting for the equivalence principle: in general relativity universality is *built into the kinematics*, not imposed on the dynamics.

**Eötvös and his descendants are the most precisely tested principle in physics; any theory violating $m_G = m_I$ is essentially ruled out.** The experimental case for the equivalence principle is overwhelming. From Eötvös's $10^{-8}$ in 1908 to MICROSCOPE's $10^{-15}$ in 2017, the equality has been tested across compositions, scales, and accelerations spanning many orders of magnitude, always with null result. This means any modification of gravity that predicts composition-dependent free fall — many variants of string theory, modified-inertia theories, certain dark-matter models — is constrained at the parts-per-trillion level. The lesson is twofold: first, the equivalence principle is not a convenient axiom one might drop, but a hard empirical fact; second, it strongly constrains theoretical alternatives to general relativity, which inherit (or must engineer) the universality automatically. Any new theory of gravity must reproduce universality of free fall at least to $10^{-13}$, and structurally the cleanest way to do this is — like general relativity — to absorb gravity into the geometry of spacetime, so that universality is kinematic rather than dynamical.

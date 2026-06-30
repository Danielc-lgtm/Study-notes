---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Energy-Momentum Tensor"
  - "Def - The Covariant Derivative"
  - "Thm - Stokes Theorem on Spacetime"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ except where $c$ is restored for recognisability, and use the mostly-minus signature $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$. $T$ is the [[Def - The Energy-Momentum Tensor|energy-momentum tensor]], a symmetric $(0,2)$-tensor field; $T_{\mu\nu}$ are its components and $T^{\mu\nu}$ the raised ones. The **divergence** of $T$ is the $1$-form $\vec{\nabla}\cdot T$ with components $(\vec{\nabla}\cdot T)_\alpha = \nabla^\mu T_{\alpha\mu} = \eta^{\mu\nu}\nabla_\nu T_{\alpha\mu}$, formed with the flat-spacetime [[Def - The Covariant Derivative|covariant derivative]] $\nabla$ (which reduces to $\partial_\mu$ in inertial coordinates). An observer has four-velocity $U_0$, rest space $\mathcal{E}_{U_0}$, energy density $\varepsilon = T(U_0,U_0)$, momentum density $\varpi$, energy flux $\varphi = c^2\varpi$, and stress $S$. The symbol $\mathcal{F}$ denotes the four-force density. Full registry on [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

---

# Statement

> **Theorem (Local conservation of energy-momentum).** Let $\mathscr{S}$ be a physical system described by an [[Def - The Energy-Momentum Tensor|energy-momentum tensor]] $T$. If $\mathscr{S}$ is isolated, then the divergence of $T$ vanishes everywhere:
> $$\boxed{\;\vec{\nabla}\cdot T = 0\;}\qquad\text{i.e.}\qquad \nabla^\mu T_{\mu\nu} = 0 \;\;\text{ for each } \nu = 0,1,2,3.$$
> This single tensor equation encodes both the conservation of energy and the conservation of momentum: in the local frame of any inertial observer it splits into
> $$\frac{\partial \varepsilon}{\partial t} + c^2\,\vec{\nabla}\cdot\varpi = 0 \qquad(\nu = 0,\ \text{energy}),$$
> $$\frac{\partial \varpi}{\partial t} + \vec{\nabla}\cdot S = 0 \qquad(\nu = i,\ \text{momentum}).$$

> **Theorem (Four-force density, non-isolated system).** If $\mathscr{S}$ is not isolated, its divergence equals the **four-force density** $\mathcal{F}$ exerted on it:
> $$\vec{\nabla}\cdot T = \mathcal{F},$$
> and the splitting becomes $\partial\varepsilon/\partial t + c^2\vec{\nabla}\cdot\varpi = -c\,\langle\mathcal{F}, U_0\rangle$ (power supplied per unit volume) and $\partial\varpi/\partial t + \vec{\nabla}\cdot S = \mathcal{F}\circ\,\perp_{U_0}$ (force per unit volume). For two interacting systems the *total* energy-momentum is conserved: $\vec{\nabla}\cdot(T_1 + T_2) = 0$, with $\mathcal{F}_1 = -\mathcal{F}_2$.

---

# Motivation

For a finite collection of particles, four-momentum conservation is the statement that the total $P$ before a collision equals the total $P$ after — an equation between two numbers (well, two four-vectors) evaluated at two instants. But a continuous medium has no "before" and "after": energy and momentum are spread through space and flow continuously from one region to the next. The conservation law for a continuum cannot be an equation between totals at two times; it must be a *local* statement, holding at every event, that says momentum is neither created nor destroyed but only transported. This theorem is that local statement, and the question it answers is: *what is the differential form of "four-momentum is conserved" when the four-momentum is carried by a field?*

The answer is the vanishing of a divergence, and that is exactly the right shape. In ordinary vector calculus, a conserved scalar quantity with density $\rho$ and current $\mathbf{j}$ obeys the continuity equation $\partial_t\rho + \vec\nabla\cdot\mathbf{j} = 0$: the rate of change of the density in a region equals minus the flux out through its boundary. Energy-momentum conservation is *four* continuity equations bundled together — one for energy, three for momentum — and the four densities-and-currents assemble into the single object $T^{\mu\nu}$, whose four-divergence vanishing is the four continuity equations at once. The miracle the theorem records is that this bundling is consistent: the same tensor that gives the energy current also gives the momentum density, because of the symmetry of $T$, so the four conservation laws are not independent statements but four components of one geometric identity.

The deeper reason a conservation law appears at all is Noether's theorem: to every continuous symmetry of the action corresponds a conserved current. Spacetime is invariant under translations — there is no preferred origin in time or space — and $T^{\mu\nu}$ is the conserved current of that translation symmetry. Time-translation invariance gives energy conservation; space-translation invariance gives momentum conservation. So this theorem is the field-theoretic face of the most basic symmetry of physics, the homogeneity of spacetime, and its failure ($\vec\nabla\cdot T = \mathcal{F} \ne 0$) signals that an external agent is breaking that homogeneity by pushing on the system.

Why this matters beyond bookkeeping: the conservation law is the consistency condition that lets the energy-momentum tensor *source gravity*. In general relativity the field equation sets the Einstein curvature tensor proportional to $T_{\mu\nu}$, and the curvature side has an identically vanishing divergence (the contracted Bianchi identity). For the equation to be solvable at all, $T$ must have vanishing divergence too — exactly this theorem. So $\vec\nabla\cdot T = 0$ is not an afterthought; it is the property without which $T$ could not be coupled to geometry.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$\mathscr{S}$ is isolated", i.e. no external force acts. The art is recognising this hypothesis in disguise.

The first disguised source is **"the system fills all of spacetime, or is bounded by vacuum"**. A field configuration that decays at infinity, or a fluid surrounded by empty space with nothing pushing on its boundary, is isolated. The bridge is that "isolated" means the four-momentum flux through any closed hypersurface vanishes, which holds whenever there is no flux of energy or momentum across the system's outer boundary. *Example problem:* show that the total electromagnetic field energy of a localised radiating system plus the kinetic energy of its charges is conserved, even as energy sloshes between field and matter — the combined $T_{\text{em}} + T_{\text{mat}}$ is divergence-free because the *pair* is isolated, while neither piece is.

The second disguised source is **"two subsystems interact only with each other"**. Charged particles in their own electromagnetic field are *not* isolated individually — the field does work on them, $\vec\nabla\cdot T_{\text{mat}} = \mathcal{F} \ne 0$ — but the matter-plus-field system *is* isolated, so $\vec\nabla\cdot(T_{\text{mat}} + T_{\text{em}}) = 0$. The bridge is Newton's third law in field form: the force density the field exerts on the matter is exactly minus the divergence of the field's own energy-momentum, so the two divergences cancel. This is the single most important application of the theorem and the entire logic of [[Def - Energy-Momentum Tensor of the Electromagnetic Field|attributing energy-momentum to the field]]. *Example:* a charge radiating energy loses kinetic energy at exactly the rate the radiation field gains it (the Larmor formula, [[Thm - Radiation by an Accelerated Charge (Larmor Formula)]]).

The third disguised source is **"the action has no explicit dependence on the spacetime coordinates"**. A Lagrangian built only from fields and their derivatives, with no explicit $x^\mu$, is translation-invariant, and Noether's theorem then *manufactures* a divergence-free $T^{\mu\nu}$. The bridge is Noether's first theorem. The nonobviousness is that you do not need to know the dynamics in detail — translation invariance alone guarantees conservation. *Example:* deriving the conserved energy-momentum of a scalar field directly from $\mathcal{L} = \tfrac12(\partial\phi)^2 - V(\phi)$ without solving the equation of motion.

**Targets (Output Amplification)**

The conclusion is "$\nabla^\mu T_{\mu\nu} = 0$".

Combine the conclusion with **integration over a four-dimensional region and [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]]**. Integrating the divergence over a four-volume $\mathcal{U}$ and applying Gauss–Ostrogradsky converts the local law into the global statement that the four-momentum flux through the closed boundary $\partial\mathcal{U}$ vanishes — i.e. the four-momentum entering equals the four-momentum leaving. The further result is that the total four-momentum on a spacelike slice is *constant in time*: $\mathbf{p}(t_2) = \mathbf{p}(t_1)$. The combination is the bridge from differential to integral conservation, and it is how one recovers the familiar particle statement from the field statement. *Example:* the total energy of an isolated star is time-independent.

Combine the conclusion with **a Killing vector** $\xi$ (a generator of a symmetry of the metric). The current $J^\mu = T^{\mu\nu}\xi_\nu$ is then *also* divergence-free, $\nabla_\mu(T^{\mu\nu}\xi_\nu) = (\nabla_\mu T^{\mu\nu})\xi_\nu + T^{\mu\nu}\nabla_\mu\xi_\nu = 0$ — the first term vanishes by the theorem, the second because $T$ is symmetric and $\nabla_\mu\xi_\nu$ is antisymmetric (Killing's equation). The further result is a conserved scalar for *every* symmetry of spacetime: time-translation Killing vector gives conserved energy, rotational Killing vector gives conserved angular momentum, boost Killing vector gives the centre-of-energy theorem. The combination is nonobvious because it shows the symmetric, divergence-free $T$ secretly contains *all* the conserved quantities of the system, each unlocked by a different symmetry. *Example:* conserved angular momentum of an axisymmetric fluid.

Combine the conclusion with the **observer decomposition of $T$**. Substituting $T = \varepsilon\, U_0^\flat\otimes U_0^\flat + c(\varpi\otimes U_0^\flat + U_0^\flat\otimes\varpi) + S$ into $\vec\nabla\cdot T = 0$ and projecting along and orthogonal to $U_0$ produces the *separate* energy and momentum continuity equations $\partial_t\varepsilon + c^2\vec\nabla\cdot\varpi = 0$ and $\partial_t\varpi + \vec\nabla\cdot S = 0$. The further result is that the abstract tensor law becomes two recognisable physical balance laws — the first the Poynting theorem (energy density changes as energy flows in), the second Newton's second law per unit volume (momentum density changes as stress pushes). The combination is what makes the theorem usable in a laboratory frame. *Example:* the Poynting theorem $\partial_t u_{\text{em}} + \vec\nabla\cdot\mathbf{S} = -\mathbf{j}\cdot\mathbf{E}$ for the electromagnetic field.

---

# Why Is It True

The theorem is true for two reasons that meet in the middle: a *physical* reason (four-momentum is locally conserved because spacetime is homogeneous) and a *geometric* reason (the flux of $T$ through any closed hypersurface vanishes, and a vanishing flux through every closed surface forces a vanishing divergence). The proof runs through the geometric reason, but the physical reason is what makes the result inevitable.

**The bold one-liner: $\vec\nabla\cdot T = 0$ is the continuity equation $\partial_t(\text{density}) + \vec\nabla\cdot(\text{current}) = 0$ written four times over — once for energy and three times for momentum — and bundled into a single tensor equation by the fact that the energy current and the momentum density are the same object.**

Take the physical reason first. Conservation of four-momentum for particles says the total $P$ is unchanged by any interaction. For a continuum, "the total is unchanged" must be promoted to "none is created or destroyed locally": whatever four-momentum leaves a small region must show up in a neighbouring region, having flowed across the shared boundary. That is exactly what a continuity equation says. The density of the $\nu$-component of four-momentum is $T^{0\nu}$ (in a given frame), and its current — the flux of $\nu$-momentum in the spatial direction $i$ — is $T^{i\nu}$. Conservation of each component is $\partial_0 T^{0\nu} + \partial_i T^{i\nu} = 0$, which is $\partial_\mu T^{\mu\nu} = 0$. The four conservation laws (one per $\nu$) are four continuity equations, and they package into the vanishing four-divergence of the single tensor $T^{\mu\nu}$.

Now the geometric reason, which is how the source proves it without choosing a frame. The defining property of $T$ is that its flux through a hypersurface *is* the four-momentum on that hypersurface. For an isolated system, the four-momentum on any *closed* hypersurface vanishes — there is no net four-momentum threading a surface that bounds a region, because what flows in one part flows out another (this is the precise meaning of "isolated", and it generalises the particle statement that total $P$ is the same on every spacelike slice). So: the flux of $T$ through every closed hypersurface is zero. Take the closed hypersurface to be the boundary $\partial\mathcal{U}$ of a compact four-dimensional region $\mathcal{U}$. The flux of $T$ through $\partial\mathcal{U}$ equals, by the [[Thm - Stokes Theorem on Spacetime|Gauss–Ostrogradsky theorem]], the integral of $\vec\nabla\cdot T$ over the interior $\mathcal{U}$. So $\int_{\mathcal{U}}\vec\nabla\cdot T\,\mathrm{d}U = 0$ for *every* region $\mathcal{U}$. A continuous integrand whose integral over every region vanishes must itself vanish identically — if it were nonzero at a point, it would have a definite sign in a small ball around that point and the integral over that ball would be nonzero. Hence $\vec\nabla\cdot T = 0$ everywhere.

The whole argument is the field analogue of the particle proof "total $P$ on every slice is equal $\Rightarrow$ nothing changes". Replace "every slice" by "every closed surface", use the flux interpretation of $T$ to turn four-momentum into a surface integral, use Gauss to turn the surface integral into a volume integral of the divergence, and use the arbitrariness of the volume to localise. The non-isolated case is the same argument with a source: if the system can exchange four-momentum with the outside at a rate given by a density $\mathcal{F}$, the flux through a closed surface equals the enclosed source integral, and localisation gives $\vec\nabla\cdot T = \mathcal{F}$.

There is a beautiful consistency check buried here: the *symmetry* of $T$ and its *conservation* are independently true, and one can be used to prove the other. The conservation of angular momentum, applied to the angular-momentum tensor built from $T$, forces $T$ to be symmetric — and that derivation uses *only* $\vec\nabla\cdot T = 0$, never the symmetry itself, so there is no circularity. Symmetry and conservation are the two pillars, and they hold each other up.

---

# What Makes This Hard

The conceptual hurdle is believing that one tensor equation contains four conservation laws and that the off-diagonal symmetry of $T$ is what glues the energy current to the momentum density — most people first see $\partial_\mu T^{\mu\nu} = 0$ as four unrelated continuity equations and miss that $T^{0i} = T^{i0}$ is doing essential work. The non-obvious technical step is the localisation argument: passing from "$\int_{\mathcal U}\vec\nabla\cdot T = 0$ for all $\mathcal U$" to "$\vec\nabla\cdot T = 0$ pointwise" requires invoking continuity and the arbitrariness of $\mathcal U$, and a common error is to stop at the integral (global) statement and forget that the local statement is strictly stronger. The other frequent slip is sign confusion in the splitting: the energy equation carries the factor $c^2$ relating flux to momentum density, and dropping it (or mismatching the mostly-minus signs when raising the index $\nu$) corrupts the Poynting theorem.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use the flux definition of $T$ to write the four-momentum on a closed hypersurface as a surface integral; apply Gauss–Ostrogradsky to convert it to the volume integral of the divergence; invoke "isolated $\Rightarrow$ four-momentum on a closed surface vanishes" to set the volume integral to zero for every region; conclude pointwise vanishing by arbitrariness of the region. Then substitute the observer decomposition and project to extract the energy and momentum balance laws.

**Subgoal decomposition:**

1. **Express the four-momentum on $\partial\mathcal{U}$ as a flux of $T$.** Show $\mathbf{p}|_{\partial\mathcal{U}} = \tfrac1c\int_{\partial\mathcal{U}} T(\,\cdot\,,\vec n)\,\mathrm{d}V$.
   - *Hint:* This is the defining property of $T$; the closed boundary $\partial\mathcal{U}$ has consistent outward orientation.
   - *Why needed:* It converts a statement about four-momentum into a surface integral amenable to Stokes.

2. **Apply Gauss–Ostrogradsky.** Contract $T$ with an arbitrary constant test vector $\vec v$ to get a $1$-form, take its metric-dual vector field $\vec w$, and apply the divergence theorem to turn $\int_{\partial\mathcal U}\vec w\cdot\vec n\,\mathrm{d}V$ into $\int_{\mathcal U}\vec\nabla\cdot\vec w\,\mathrm{d}U$.
   - *Hint:* $\vec\nabla\cdot\vec w = (\vec\nabla\cdot T)\cdot\vec v$ because $\vec v$ is constant, so its derivative drops.
   - *Why needed:* It localises the surface integral to a volume integral of the divergence of $T$.

3. **Use "isolated".** For an isolated system the four-momentum on the closed $\partial\mathcal U$ is zero, so the volume integral $\int_{\mathcal U}(\vec\nabla\cdot T)\cdot\vec v\,\mathrm{d}U = 0$ for every $\mathcal U$ and every constant $\vec v$.
   - *Hint:* "Isolated" is *defined* by vanishing four-momentum on every closed hypersurface.
   - *Why needed:* It sets the integral to zero, the input to the localisation step.

4. **Localise.** Arbitrariness of $\mathcal U$ and continuity of the integrand give $(\vec\nabla\cdot T)\cdot\vec v = 0$ pointwise; arbitrariness of $\vec v$ gives $\vec\nabla\cdot T = 0$.
   - *Hint:* A continuous function with vanishing integral over every region vanishes identically.
   - *Why needed:* It delivers the pointwise (local) conservation law, the theorem's conclusion.

5. **Split into energy and momentum.** Substitute $T = \varepsilon U_0^\flat\otimes U_0^\flat + c(\varpi\otimes U_0^\flat + U_0^\flat\otimes\varpi) + S$ into $\vec\nabla\cdot T = 0$, project along $U_0$ for the energy equation and orthogonally for the momentum equation.
   - *Hint:* For inertial $U_0$, $\nabla_{U_0}U_0 = 0$; use $\nabla_{U_0}\varepsilon = c^{-1}\partial_t\varepsilon$.
   - *Why needed:* It produces the two recognisable balance laws.

---

# Lemma Decomposition

> [!note]- Lemma 1: The divergence of $T$ is the localised four-momentum source
> **Statement:** For a compact region $\mathcal{U}$ with boundary $\mathscr{V} = \partial\mathcal{U}$, the four-momentum on $\mathscr{V}$ is $\mathbf{p}|_{\mathscr{V}} = \tfrac1c\int_{\mathcal U}\vec\nabla\cdot T\,\mathrm{d}U$.
>
> **Hint:** Apply $\mathbf{p}|_{\mathscr V}$ to an arbitrary constant vector $\vec v$, identify the resulting $1$-form's metric-dual vector $\vec w$ with $w^\alpha = g^{\alpha\nu}T_{\mu\nu}v^\mu$, and use Gauss–Ostrogradsky.
>
> **Why needed:** It is the bridge from the flux definition of $T$ to a volume integral of its divergence, and it holds whether or not the system is isolated — so it also delivers the four-force-density statement.
>
> > [!note]- Full proof
> > By the defining flux property of the [[Def - The Energy-Momentum Tensor|energy-momentum tensor]], $\langle\mathbf{p}|_{\mathscr V}, \vec v\rangle = \pm\tfrac1c\int_{\mathscr V} T(\vec v, \vec n)\,\mathrm{d}V = \tfrac1c\Phi_{\mathscr V}(\vec w)$, where $\vec w$ is the vector field metric-dual to the $1$-form $T(\vec v, \cdot)$, with components $w^\alpha = g^{\alpha\nu}T_{\mu\nu}v^\mu$, and $\Phi_{\mathscr V}$ denotes the flux through $\mathscr V$. Taking $\mathscr V = \partial\mathcal U$ the boundary of a compact four-domain and applying the Gauss–Ostrogradsky theorem ([[Thm - Stokes Theorem on Spacetime#Statement]], divergence form),
> > $$\langle\mathbf{p}|_{\mathscr V}, \vec v\rangle = \frac1c\int_{\mathcal U}\vec\nabla\cdot\vec w\;\mathrm{d}U.$$
> > Now compute the divergence, using that $\vec v$ is a *constant* vector so $\nabla_\rho v^\mu = 0$:
> > $$\vec\nabla\cdot\vec w = \nabla_\nu w^\nu = \nabla^\nu(T_{\mu\nu}v^\mu) = (\nabla^\nu T_{\mu\nu})\,v^\mu + T_{\mu\nu}\underbrace{\nabla^\nu v^\mu}_{0} = (\vec\nabla\cdot T)_\mu\, v^\mu = \langle\vec\nabla\cdot T, \vec v\rangle.$$
> > Hence $\langle\mathbf{p}|_{\mathscr V}, \vec v\rangle = \tfrac1c\int_{\mathcal U}\langle\vec\nabla\cdot T, \vec v\rangle\,\mathrm{d}U$ for every constant $\vec v$, which is the asserted identity $\mathbf{p}|_{\mathscr V} = \tfrac1c\int_{\mathcal U}\vec\nabla\cdot T\,\mathrm{d}U$. $\blacksquare$

> [!note]- Lemma 2: Vanishing flux on every region forces vanishing divergence
> **Statement:** If $\int_{\mathcal U}(\vec\nabla\cdot T)\,\mathrm{d}U = 0$ for every compact region $\mathcal U$, then $\vec\nabla\cdot T = 0$ everywhere.
>
> **Hint:** Suppose not; take a small ball around a point where some component is nonzero.
>
> **Why needed:** It is the localisation step that upgrades the global (integral) conservation law to the local (pointwise) one, which is the strictly stronger conclusion of the theorem.
>
> > [!note]- Full proof
> > Fix a component $(\vec\nabla\cdot T)_\alpha$ and suppose it is nonzero at some event $M$, say positive. By continuity it is positive on an open ball $B$ around $M$. Then $\int_B (\vec\nabla\cdot T)_\alpha\,\mathrm{d}U > 0$, contradicting the hypothesis that the integral over every region — in particular $B$ — vanishes. Hence $(\vec\nabla\cdot T)_\alpha = 0$ at every event, for each $\alpha$, i.e. $\vec\nabla\cdot T = 0$. $\blacksquare$

> [!note]- Lemma 3: The splitting into energy and momentum balance
> **Statement:** For an inertial observer $U_0$, the equation $\vec\nabla\cdot T = \mathcal{F}$ projects to $\partial_t\varepsilon + c^2\vec\nabla\cdot\varpi = -c\langle\mathcal F, U_0\rangle$ (along $U_0$) and $\partial_t\varpi + \vec\nabla\cdot S = \mathcal F\circ\perp_{U_0}$ (orthogonal to $U_0$).
>
> **Hint:** Substitute the orthogonal decomposition of $T$, use $\nabla_{U_0}U_0 = 0$ (inertial), and project the resulting $1$-form equation onto $U_0$ and onto the rest space.
>
> **Why needed:** It shows that the single abstract tensor law is exactly the pair of physical balance laws — energy continuity (Poynting) and momentum continuity (Newton per unit volume).
>
> > [!note]- Full proof
> > Substitute $T = \varepsilon\,U_0^\flat\otimes U_0^\flat + c\,\varpi\otimes U_0^\flat + c\,U_0^\flat\otimes\varpi + S$ into $\vec\nabla\cdot T = \mathcal F$. Since $U_0$ is constant ($\mathcal O$ inertial, $\nabla U_0 = 0$),
> > $$(\nabla_{U_0}\varepsilon)\,U_0^\flat + c\,\nabla_{U_0}\varpi + c(\vec\nabla\cdot\varpi)\,U_0^\flat + \vec\nabla\cdot S = \mathcal F,$$
> > where terms with a derivative falling on $U_0^\flat$ vanish. Project onto $U_0$ (apply the $1$-form equation to the vector $U_0$): using $\langle U_0^\flat, U_0\rangle = 1$, $\langle\varpi, U_0\rangle = 0$ (the momentum density lies in the rest space), and $\nabla_{U_0}\varepsilon = c^{-1}\partial_t\varepsilon$,
> > $$\frac1c\frac{\partial\varepsilon}{\partial t} + c\,\vec\nabla\cdot\varpi = \langle\mathcal F, U_0\rangle \;\Longrightarrow\; \frac{\partial\varepsilon}{\partial t} + c^2\vec\nabla\cdot\varpi = c\,\langle\mathcal F, U_0\rangle.$$
> > (For an isolated system $\mathcal F = 0$, recovering the boxed energy equation; the power *supplied* to the system is $-c\langle\mathcal F, U_0\rangle$ in the sign convention where $\mathcal F$ is the force the system exerts.) Projecting orthogonally (compose with $\perp_{U_0}$): using $\perp_{U_0}U_0 = 0$, $\varpi\circ\perp_{U_0} = \varpi$, $S\circ\perp_{U_0} = S$, and $\nabla_{U_0}\varpi = c^{-1}\partial_t\varpi$,
> > $$\frac{\partial\varpi}{\partial t} + \vec\nabla\cdot S = \mathcal F\circ\perp_{U_0}. \qquad\blacksquare$$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness of the divergence.** On flat spacetime the [[Def - The Covariant Derivative|covariant derivative]] $\nabla$ exists and reduces to $\partial_\mu$ in inertial coordinates, so $(\vec\nabla\cdot T)_\alpha = \nabla^\mu T_{\alpha\mu}$ is a well-defined $1$-form (the metric-dual of the divergence of $T^\sharp$, which is the relativistic analogue of the divergence of a vector field). The flux property of $T$ presupposes that the hypersurfaces are non-null and consistently oriented, which we assume throughout.
>
> Let $\mathscr S$ be isolated and let $\mathcal U \subset \mathbb{M}$ be an arbitrary compact four-dimensional region with boundary $\mathscr V = \partial\mathcal U$, a closed hypersurface.
>
> By **Lemma 1**, for any constant test vector $\vec v$,
> $$\langle\mathbf{p}|_{\mathscr V}, \vec v\rangle = \frac1c\int_{\mathcal U}\langle\vec\nabla\cdot T, \vec v\rangle\,\mathrm{d}U.$$
> Because $\mathscr S$ is isolated and $\mathscr V$ is a *closed* hypersurface, its total four-momentum vanishes: $\mathbf{p}|_{\mathscr V} = 0$ (this is the definition of "isolated" in flux form, the continuum generalisation of "the total four-momentum is the same on every spacelike slice"). Hence
> $$\int_{\mathcal U}\langle\vec\nabla\cdot T, \vec v\rangle\,\mathrm{d}U = 0 \quad\text{for every compact } \mathcal U \text{ and every constant } \vec v.$$
> By **Lemma 2**, the vanishing of this integral over every region forces the integrand to vanish pointwise: $\langle\vec\nabla\cdot T, \vec v\rangle = 0$ at every event. Since $\vec v$ is arbitrary,
> $$\vec\nabla\cdot T = 0, \qquad\text{i.e.}\qquad \nabla^\mu T_{\mu\nu} = 0,$$
> which is the local conservation law.
>
> **Non-isolated case.** If $\mathscr S$ exchanges four-momentum with its surroundings, the four-momentum on the closed boundary equals the enclosed source rate, and the identical argument with $\mathbf p|_{\mathscr V} = \tfrac1c\int_{\mathcal U}\mathcal F\,\mathrm dU$ yields $\vec\nabla\cdot T = \mathcal F$, defining the four-force density. For two interacting subsystems, the union is isolated, so $\vec\nabla\cdot(T_1 + T_2) = 0$ and therefore $\mathcal F_1 = \vec\nabla\cdot T_1 = -\vec\nabla\cdot T_2 = -\mathcal F_2$.
>
> **Splitting.** By **Lemma 3**, projecting $\vec\nabla\cdot T = \mathcal F$ along and orthogonal to an inertial $U_0$ gives the energy balance $\partial_t\varepsilon + c^2\vec\nabla\cdot\varpi = c\langle\mathcal F, U_0\rangle$ and the momentum balance $\partial_t\varpi + \vec\nabla\cdot S = \mathcal F\circ\perp_{U_0}$; for $\mathcal F = 0$ these are the boxed energy and momentum conservation laws. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Poynting theorem of electromagnetism.** Applying the splitting to the [[Def - Energy-Momentum Tensor of the Electromagnetic Field|electromagnetic energy-momentum tensor]] gives $\partial_t u_{\text{em}} + \vec\nabla\cdot\mathbf{S} = -\mathbf{j}\cdot\mathbf{E}$, the statement that the field energy density $u_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$ changes as the Poynting vector $\mathbf{S}$ carries energy away and as the field does work $\mathbf{j}\cdot\mathbf{E}$ on charges. The source term is exactly the four-force-density form of the theorem: the field is not isolated when charges are present. This is the most familiar incarnation of energy-momentum conservation and the one most students meet first, usually without realising it is $\partial_\mu T^{\mu 0} = -\mathcal F^0$.

**Hydrodynamics — Euler's equation as a projection.** For a [[Def - Perfect Fluid|perfect fluid]] $T^{\mu\nu} = (\rho+p)U^\mu U^\nu - p\,\eta^{\mu\nu}$, the orthogonal projection of $\nabla_\mu T^{\mu\nu} = 0$ is the relativistic Euler equation $(\rho+p)\,U^\nu\nabla_\nu U^\mu = -(\eta^{\mu\nu} - U^\mu U^\nu)\nabla_\nu p$, and the parallel projection is the energy (entropy advection) equation. The same theorem thus produces both equations of motion of a fluid, with the choice of projection selecting which one. This is the foundation of relativistic astrophysics and the application that most directly battle-tests the "project along and orthogonal to $U$" technique.

**Cosmology — the dilution of energy in an expanding universe.** Applied in a Friedmann–Lemaître spacetime (curved, so $\nabla$ carries Christoffel symbols), the energy equation $\dot\rho + 3H(\rho + p) = 0$ — where $H$ is the Hubble rate — follows directly from $\nabla_\mu T^{\mu 0} = 0$ for the cosmological perfect fluid, and predicts that matter dilutes as $a^{-3}$, radiation as $a^{-4}$, and a cosmological constant ($p = -\rho$) not at all. The application is out-of-distribution because the conservation law here governs the global energy budget of the universe, yet it is the same $\nabla_\mu T^{\mu\nu} = 0$, now with the connection of an expanding geometry.

---

# Bridges

- **[[Thm - Conservation of Four-Momentum]]** — the particle version of this theorem. For a finite system of particles, four-momentum conservation is the statement that the total $P$ on every spacelike slice is equal; here that statement is localised into the differential law $\nabla_\mu T^{\mu\nu} = 0$. The bridge is the flux interpretation: the particle "total four-momentum" is the flux of the particle energy-momentum tensor $T = \sum_a\int\delta\,P_a\otimes U_a\,\mathrm d\tau$ through a spacelike slice, and the conservation of that flux across slices is exactly the vanishing of the divergence. Discrete conservation and continuum conservation are the same law at two resolutions.

- **[[Thm - Stokes Theorem on Spacetime]]** — the engine of the proof. Gauss–Ostrogradsky (the divergence-theorem corollary of Stokes) is what converts "four-momentum on a closed hypersurface" into "integral of the divergence over the enclosed region", and it is the arbitrariness of that region, combined with continuity, that localises the law. Without Stokes there is no passage from the global flux statement to the local differential statement.

- **[[Def - Energy-Momentum Tensor of the Electromagnetic Field]]** — the first concrete non-trivial application. The matter system of charged particles is *not* isolated, $\vec\nabla\cdot T_{\text{mat}} = \mathcal F = F(\,\cdot\,, J)$, but the matter-plus-field system *is*, so $\vec\nabla\cdot(T_{\text{mat}} + T_{\text{em}}) = 0$ and the field's energy-momentum tensor is *defined* as the object that makes this hold. The theorem is thus not just a property of $T_{\text{em}}$ — it is the construction principle that produces $T_{\text{em}}$ in the first place.

- **The contracted Bianchi identity (general relativity)** — the geometric mirror of this theorem. In general relativity the Einstein tensor satisfies $\nabla^\mu G_{\mu\nu} = 0$ *identically*, as a consequence of the second Bianchi identity for the Riemann curvature. The field equation $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ is consistent only if $\nabla^\mu T_{\mu\nu} = 0$ — exactly this theorem. So conservation of energy-momentum is, in the curved theory, *forced* by the geometry: it is the integrability condition of the Einstein equation, and it is no longer an independent postulate but a corollary of the field equation itself.

---

# Unlocked by This

> [!tip] Conserved Charges from Killing Vectors *(from General Relativity)*
> Once $\nabla_\mu T^{\mu\nu} = 0$ holds, every symmetry of the spacetime — every **Killing vector** $\xi$ — yields a conserved current $J^\mu = T^{\mu\nu}\xi_\nu$ with $\nabla_\mu J^\mu = 0$, because the symmetric, divergence-free $T$ contracted against the antisymmetric $\nabla_\mu\xi_\nu$ kills the extra term. Time-translation symmetry gives conserved energy, rotational symmetry conserved angular momentum, boost symmetry the centre-of-energy theorem. This is the general mechanism by which conserved quantities arise in gravitational physics, and it is why stationary and axisymmetric spacetimes (Schwarzschild, Kerr) admit conserved energy and angular momentum for orbiting test bodies.

> [!tip] The ADM Energy and the Positive Energy Theorem *(from Mathematical General Relativity)*
> Integrating the conservation law over an asymptotically flat spacelike slice defines the total **ADM energy-momentum** of an isolated gravitating system — a four-vector living at spatial infinity. The deep **positive energy theorem** of Schoen–Yau and Witten states that, provided the matter $T_{\mu\nu}$ satisfies the dominant energy condition, this total energy is non-negative and vanishes only for Minkowski space. The flux-of-$T$ definition of four-momentum used in this chapter is the special-relativistic shadow of that construction.

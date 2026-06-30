---
type: definition
subject: special-relativity
prereqs:
  - "Def - Perfect Fluid"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Thm - Stokes Theorem on Spacetime"
  - "Def - The Hodge Star"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, $u\cdot u = 1$. The proper baryon density (baryon number per unit volume in the fluid rest frame) is $n$; the fluid four-velocity is $u$ (see [[Def - Perfect Fluid]]). An observer $\mathcal{O}$ has four-velocity $u_0$, and $\Gamma = u\cdot u_0$ is the fluid Lorentz factor relative to $\mathcal{O}$. The [[Def - The Hodge Star|Hodge star]] is $\star$, the [[Def - The Exterior Derivative|exterior derivative]] is $d$, and the [[Def - The Covariant Derivative|covariant derivative]] is $\nabla$. This is a compound page: it defines two interlocking notions — the **baryon four-current** and its **conservation law** — because the current is introduced precisely in order to state its conservation, and neither is fully usable without the other. Full registry on [[Special Relativity XXIV — Relativistic Hydrodynamics]].

> [!warning] Convention
> Gourgoulhon uses the mostly-plus signature, in which the flux of the current through a spatial domain with future-pointing unit normal $u_0$ carries a minus sign, $N = -j_{\mathrm b}\cdot u_0$, and $\Gamma = -u\cdot u_0$. In our mostly-minus convention these become $N = j_{\mathrm b}\cdot u_0$ and $\Gamma = u\cdot u_0$.

---

# Axiom Motivation

We have a fluid described by an energy–momentum tensor, but the matter is also made of particles, and the count of those particles is a conserved quantity that the energy–momentum tensor does not by itself track. The desideratum is a relativistic object whose conservation expresses "the number of baryons is fixed", in exactly the way the electric four-current's conservation expresses charge conservation. The construction is forced once you ask what data such an object needs.

To count baryons you need two things: a density and a flow. In the fluid rest frame there is a proper baryon density $n$ — baryons per unit rest-frame volume. But density is frame-dependent (a moving observer sees the rest-frame volume length-contracted, hence a higher density), so $n$ alone is not a relativistic object. The fix is the same one that turns charge density into the electric four-current: combine the density with the four-velocity. Define the **baryon four-current** $j_{\mathrm b}^\mu = n\,u^\mu$. In the rest frame this is $(n, 0, 0, 0)$ — pure density, no spatial flux — and in any other frame its time component is the observed density (boosted by $\Gamma$, the length-contraction factor) and its spatial components are the baryon flux. The single ingredient is: multiply the proper density by the four-velocity, exactly as for charge.

Why is this the right object and not, say, $n$ times some other vector? Because the flux of $j_{\mathrm b}^\mu$ through a spatial domain must count the baryons inside, and only $n\,u^\mu$ does this correctly. The flux through a piece of an observer's rest space, with future-pointing unit normal $u_0$, is $\int j_{\mathrm b}\cdot u_0\,dV = \int n(u\cdot u_0)\,dV = \int \Gamma n\,dV$. The combination $\Gamma n$ is precisely the baryon density *as measured by* $\mathcal{O}$ — the proper density $n$ enhanced by the length-contraction factor $\Gamma$ — so the integral is the baryon number $\mathcal{O}$ counts. Had we used anything but $u^\mu$, the $\Gamma$ would not appear and the flux would not be a baryon count. The structure is dictated by the requirement that the flux equals the count.

Now the conservation law. The physical postulate is that baryon number is conserved: in the Standard Model, baryon number is preserved by the electromagnetic, strong, and (perturbatively) weak interactions, violated only by non-perturbative anomalies that are negligible outside the primordial universe, and proton decay has never been observed (the experimental lower bound on the proton lifetime is above $10^{33}$ years). So we postulate, exactly as for charge, that the flux of the baryon four-current through any *closed* hypersurface vanishes. This integral statement is the primary axiom; its local form follows. By [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]], the vanishing of $\oint_\Sigma \star j_{\mathrm b}$ over every closed $\Sigma$ forces the four-form $d\star j_{\mathrm b}$ to vanish identically, and by Hodge duality this is the vanishing of the divergence: $\nabla_\mu j_{\mathrm b}^\mu = 0$, i.e. $\nabla_\mu(n u^\mu) = 0$.

What would go wrong with a weaker or different law? If the divergence were merely *bounded* rather than zero, baryons could be created or destroyed in the interior — there would be sources — and the count would not be conserved; this is what happens in the early universe with baryogenesis, where the anomaly provides a source. If we used a non-unit four-velocity, the relation between proper and observed density would be wrong and $\Gamma$ would not be the correct enhancement factor. The conservation law in the form $\nabla_\mu(nu^\mu) = 0$ is the minimal statement that the baryon count is fixed, written so that it holds in every frame.

---

# The Definition

The **baryon four-current** of a fluid with proper baryon density $n$ and four-velocity $u$ is the vector field
$$j_{\mathrm b}^\mu \;=\; n\,u^\mu.$$
The baryon number contained in a three-dimensional domain $\mathcal{V}$ lying in the rest space of an observer $\mathcal{O}$ (four-velocity $u_0$, the unit normal to $\mathcal{V}$) is the flux
$$\mathcal{N} \;=\; \int_\mathcal{V} j_{\mathrm b}\cdot u_0\,dV \;=\; \int_\mathcal{V} \star j_{\mathrm b},$$
where $\star j_{\mathrm b}$ is the three-form Hodge-dual to the one-form associated with $j_{\mathrm b}$ by metric duality. The integrand $N := j_{\mathrm b}\cdot u_0 = \Gamma n$ (with $\Gamma = u\cdot u_0$) is the baryon density measured by $\mathcal{O}$.

The **principle of baryon-number conservation** states that for an isolated fluid, the flux of $j_{\mathrm b}$ through any closed hypersurface $\Sigma$ vanishes:
$$\oint_\Sigma \star j_{\mathrm b} \;=\; 0.$$
By [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] and Hodge duality, this is equivalent to the **local conservation law**
$$\boxed{\nabla_\mu(n\,u^\mu) \;=\; 0.}$$
Relative to an inertial observer $\mathcal{O}$, with $\mathbf{V}$ the fluid three-velocity, this becomes the **continuity equation**
$$\frac{\partial N}{\partial t} + \nabla\cdot(N\mathbf{V}) = 0, \qquad N = \Gamma n,$$
which has the same form as the nonrelativistic continuity equation, with no extra relativistic factor.

A companion identity, derived by transporting a comoving volume element along the flow, expresses the four-divergence of the four-velocity as the fractional expansion rate of a comoving volume $V$ (proper time $\tau$):
$$\nabla_\mu u^\mu \;=\; \frac{1}{V}\frac{dV}{d\tau}.$$

---

# Categorical / Structural Definition

The baryon four-current is a **conserved current** in the precise sense of the theory of currents on a Lorentzian manifold: a vector field $J$ (equivalently, via metric duality and the Hodge star, a closed three-form $\star J$) whose flux through homologous hypersurfaces is invariant. Structurally it is the exact analogue of the electric four-current of [[Special Relativity XXII — Maxwell's Equations|electromagnetism]], and the parallel is complete: both are of the form (proper density)$\times$(four-velocity), both have conservation laws $\nabla_\mu J^\mu = 0$, and in both cases the conservation law is the statement $d\star J = 0$ that the dual three-form is closed. The difference is only in which scalar charge is being counted — baryon number here, electric charge there.

The conservation law sits inside the general framework of **Noether currents and continuity equations**. A conserved current is the object whose existence is guaranteed, by Noether's theorem, by a symmetry — here the $U(1)$ phase symmetry associated with baryon number. The integral form $\oint_\Sigma \star J = 0$ and the local form $\nabla_\mu J^\mu = 0$ are related by [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] exactly as the global and local statements of any conservation law are related: closing a hypersurface and applying Stokes converts "no net flux out of a region" into "no sources inside". This is the same logic that turns Gauss's law into charge conservation, and it is worth seeing the baryon current as one instance of the universal pattern "symmetry $\Rightarrow$ conserved current $\Rightarrow$ continuity equation".

---

# Relate to Other Fields / Compression

The baryon four-current is the relativistic completion of the **mass-flux density** $\rho_{\mathrm m}\mathbf{v}$ of nonrelativistic fluid dynamics, whose conservation is the continuity equation $\partial_t\rho_{\mathrm m} + \nabla\cdot(\rho_{\mathrm m}\mathbf{v}) = 0$. In the nonrelativistic limit $\Gamma \to 1$, the observed baryon density $N = \Gamma n$ becomes the proper density $n$, and the relativistic continuity equation becomes the classical one. The fact that the relativistic continuity equation has *no* extra factor of $\Gamma$ or $c^{-1}$ — that it is identical in form to the Newtonian one — is a genuine feature: number conservation is "kinematically Newtonian" because the relativistic enhancement of the density ($\Gamma n$) and the relativistic transformation of the flux conspire to leave the conservation law in classical form.

The companion identity $\nabla_\mu u^\mu = \dot V/V$ relates the four-divergence of the flow to **volume expansion**, the relativistic version of $\nabla\cdot\mathbf{v} = \dot V/V$ for the rate of change of a fluid-element volume. This is the quantity that, in cosmology, becomes the Hubble expansion $3\dot a/a$.

**True name:** the operational content of baryon-number conservation is *"the four-divergence of (density times four-velocity) vanishes"*, equivalently *"the number of fluid lines threading a comoving region is fixed"*. This is the form to reach for: whenever a scalar charge is carried by the fluid and conserved, build the current (proper density)$\times u^\mu$ and write $\nabla_\mu(\text{density}\cdot u^\mu) = 0$. Combined with the identity $\nabla_\mu u^\mu = \dot V/V$, it immediately gives that the density times the comoving volume — the actual count — is constant along the flow.

---

# Examples / Corollaries

**Is an instance — the baryon current of a star or cosmological fluid.** In a neutron star or in cosmology, $n$ is the rest-frame number density of baryons and $j_{\mathrm b}^\mu = nu^\mu$ counts them; its conservation $\nabla_\mu(nu^\mu) = 0$ is imposed alongside the [[Thm - Relativistic Euler Equation|Euler equation]] to close the system. In an expanding universe it gives $n \propto a^{-3}$: the number density dilutes as the inverse cube of the scale factor, simply because the same baryons fill an expanding comoving volume.

**Is an instance — any conserved-particle current.** The construction is not special to baryons. For any conserved particle species with proper number density $n_a$, the current $n_a u^\mu$ is conserved if that species is neither created nor destroyed: $\nabla_\mu(n_a u^\mu) = 0$. Lepton number, electric charge (via charge density), and a frozen chemical species all give conserved currents of this form.

**Is NOT an instance — the entropy current when there are sources.** The entropy current $s u^\mu$ is *not* conserved in general: $\nabla_\mu(su^\mu)$ equals the entropy production rate, which is positive for dissipative processes and zero only for a reversible (isentropic) flow. For an isolated *perfect* fluid the entropy current happens to be conserved (the flow is adiabatic), but this is a consequence of the perfect-fluid dynamics, not a postulate, and it fails the moment viscosity or conduction is added. The baryon current, by contrast, is conserved by postulate regardless of dissipation.

**Is NOT an instance — a current with creation.** In the early universe, baryogenesis creates a net baryon number, so $\nabla_\mu(nu^\mu) \ne 0$ there: the anomaly provides a source term. This is exactly the regime the conservation postulate excludes, and it is why the postulate is stated for an "isolated" fluid away from such non-perturbative processes.

**Corollary — the count is constant along the flow.** Combining $\nabla_\mu(nu^\mu) = 0$ with $\nabla_\mu u^\mu = \dot V/V$ gives $\dot n/n + \dot V/V = 0$, i.e. $d(nV)/d\tau = 0$: the baryon number $\mathcal{N} = nV$ in a comoving volume is constant. This is the cleanest statement of conservation — the actual count carried by a fluid element does not change.

**Corollary — the observed density is the boosted proper density.** Contracting with an observer's four-velocity, $N = j_{\mathrm b}\cdot u_0 = n(u\cdot u_0) = \Gamma n$. A moving fluid is seen to have a higher number density than its rest-frame value, by the length-contraction factor $\Gamma$ — the same effect that makes a moving box of gas denser to a passing observer.

**Calibration check.** If you have understood the page you should be able to: (i) write the baryon current in the rest frame and confirm it is $(n,0,0,0)$; (ii) derive the continuity equation $\partial_t(\Gamma n) + \nabla\cdot(\Gamma n\mathbf{V}) = 0$ from $\nabla_\mu(nu^\mu) = 0$; (iii) combine conservation with $\nabla_\mu u^\mu = \dot V/V$ to show the comoving baryon count $nV$ is constant.

---

# Unlocked by This

> [!tip] Adiabaticity of Perfect-Fluid Flow *(from §24.2)*
> Baryon-number conservation $\nabla_\mu(nu^\mu) = 0$, combined with entropy conservation $\nabla_\mu(su^\mu) = 0$ (which follows from the energy equation for an isolated simple fluid), gives $\nabla_u(s/n) = 0$: the entropy per baryon $S = s/n$ is constant along each fluid line, so the flow is **adiabatic**. This is the input that simplifies the canonical equation $\Omega(u,\cdot) = T\,dS$ and underlies [[Thm - Kelvin's Circulation Theorem (exterior-calculus formulation)|Kelvin's circulation theorem]].

> [!tip] Dilution of Cosmic Species *(from Cosmology)*
> In an expanding universe the conservation $\nabla_\mu(nu^\mu) = 0$ becomes $n \propto a^{-3}$: number densities dilute as the inverse cube of the scale factor. This, together with the energy equation, fixes how every cosmic component scales and is the bookkeeping behind the relative abundances of matter, radiation, and dark energy in the **Friedmann** cosmology.

---
type: definition
subject: special-relativity
prereqs:
  - "Def - Perfect Fluid"
  - "Thm - Relativistic Euler Equation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ (restored where the structure is clearer) and use the mostly-minus signature, $u\cdot u = 1$. The proper energy density is $\rho$ and the pressure is $p$ (see [[Def - Perfect Fluid]]); the proper entropy density is $s$, the proper baryon density is $n$, and the proper number densities of particle species are $n_a$. The entropy per baryon is $S = s/n$. The temperature is $T$, the chemical potential of species $a$ is $\mu_a$, the chemical potential per baryon is $\mu$, and the enthalpy per baryon is $h = (\rho+p)/n$. The speed of sound is $c_s$. This is a compound page: it defines two interlocking notions — the **equation of state** and the **speed of sound** — because the sound speed is a derivative of the equation of state and has no meaning without it. Full registry on [[Special Relativity XXIV — Relativistic Hydrodynamics]].

> [!warning] Convention
> Gourgoulhon writes $\varepsilon$ for the proper energy density that we call $\rho$, and his rest-mass density is also denoted $\rho$. We reserve $\rho$ for the **proper energy density** and write the rest-mass density as $\rho_{\mathrm m}$ when it is needed. The speed of sound is $c_s^2 = (\partial p/\partial\rho)_S$ with $\rho$ the energy density (Gourgoulhon's $(\partial p/\partial\varepsilon)_S$); in the nonrelativistic limit $\rho \to \rho_{\mathrm m}c^2$ and it becomes $(\partial p/\partial\rho_{\mathrm m})_S$.

---

# Axiom Motivation

The perfect-fluid tensor $(\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$ has two independent scalar fields, $\rho$ and $p$, but the conservation law $\nabla_\mu T^{\mu\nu} = 0$ supplies only four equations for the five unknowns $\rho$, $p$, and the three independent components of $u$. The system is *underdetermined*: one more relation is needed, and it cannot come from the dynamics — it must come from the *matter*. The equation of state is that relation, and the question is what form it should take.

The honest answer comes from thermodynamics. A fluid element is, microscopically, a large number of particles in **local thermodynamic equilibrium**: the mean free path is short compared to the size of the element, so the element has a well-defined temperature, entropy, and pressure. Equilibrium thermodynamics then says that the energy density is a function of the extensive densities — the entropy density and the particle number densities:
$$\rho = \rho(s, n_1, \dots, n_N).$$
This is the equation of state, and its precise form encodes the microphysics (an ideal gas, a degenerate Fermi gas, a photon gas all have different $\rho(s, \{n_a\})$). Given it, *everything thermodynamic is a derivative*: temperature is how energy changes with entropy, $T = (\partial\rho/\partial s)$, and the chemical potential of a species is how energy changes with its number, $\mu_a = (\partial\rho/\partial n_a)$. These are not separate postulates — they are the *definitions* of $T$ and $\mu_a$, forced by the first law $d\rho = T\,ds + \sum_a\mu_a\,dn_a$, which is just the differential of the equation of state.

Why these variables and not others? Because the conserved quantities a fluid element carries along its worldline are its entropy and its particle numbers (for an adiabatic, non-reacting flow), and energy is naturally a function of what is conserved. One could Legendre-transform to other variables — pressure as a function of temperature and chemical potentials, say — and indeed the **Gibbs–Duhem relation** $dp = s\,dT + \sum_a n_a\,d\mu_a$ does exactly this, but the energy-as-function-of-densities form is the one that closes the dynamical system, because $\rho$ and $p$ are what appear in the tensor.

Now the speed of sound. A sound wave is a small compression that propagates through the fluid, and its speed is determined by how stiff the fluid is — how much the pressure rises when you compress it. Compress an element adiabatically (sound is fast, so no heat is exchanged, and the entropy per baryon $S$ is held fixed), and the pressure responds by $\delta p = (\partial p/\partial\rho)_S\,\delta\rho$. The wave equation that the perfect-fluid equations produce for a small perturbation has propagation speed squared equal to exactly this derivative:
$$c_s^2 = \left(\frac{\partial p}{\partial\rho}\right)_S.$$
The subscript $S$ is the whole subtlety, and it is forced by the physics: sound is an *adiabatic* compression, not an isothermal one, so the entropy per baryon is constant and the derivative is taken at fixed $S$. Using an isothermal derivative $(\partial p/\partial\rho)_T$ instead would give the wrong speed (this was Newton's famous error for the speed of sound in air, corrected by Laplace). And it must be a *derivative*, a slope, not a ratio $p/\rho$: only for a linear equation of state $p \propto \rho$ do the slope and the ratio coincide.

What constrains the equation of state? Causality. No signal, including sound, may travel faster than light, so $c_s \le 1$. This is a constraint on the *slope* of $p(\rho)$: the equation of state may not stiffen faster than $p = \rho$, which is the limiting "hardest" causal matter, with $c_s = c$ exactly. A fluid violating $c_s \le 1$ would transmit information superluminally, which is forbidden.

---

# The Definition

The **equation of state** of a fluid in local thermodynamic equilibrium is the relation expressing the proper energy density as a function of the proper entropy density and the proper particle number densities:
$$\rho \;=\; \rho(s, n_1, \dots, n_N).$$
Its first derivatives define the **temperature** and the **chemical potentials**:
$$T := \left(\frac{\partial\rho}{\partial s}\right)_{n_a}, \qquad \mu_a := \left(\frac{\partial\rho}{\partial n_a}\right)_{s,\,n_{b\ne a}},$$
and the **fundamental thermodynamic relation** (first law) is
$$d\rho = T\,ds + \sum_{a=1}^N \mu_a\,dn_a.$$
Two further identities follow: the **Euler relation** $\rho + p = Ts + \sum_a\mu_a n_a$ (so $\rho + p$ is the proper enthalpy density), and the **Gibbs–Duhem relation** $dp = s\,dT + \sum_a n_a\,d\mu_a$.

A **simple fluid** is a perfect fluid whose equation of state depends on only two variables, the entropy density and the baryon density:
$$\rho = \rho(s, n).$$
A **barotropic fluid** is one whose equation of state depends on the baryon density alone, $\rho = \rho(n)$; for a barotropic fluid $T = 0$, and the Euler relation gives $\rho + p = \mu n$, so the chemical potential equals the enthalpy per baryon, $\mu = (\rho+p)/n = h$.

The **speed of sound** is
$$\boxed{c_s := c\sqrt{\left(\frac{\partial p}{\partial\rho}\right)_S},}$$
the derivative of pressure with respect to energy density at fixed entropy per baryon $S = s/n$. It is the propagation speed of small adiabatic perturbations: linearising the perfect-fluid equations about a homogeneous state gives the wave equation $-c_s^{-2}\,\partial_t^2\delta\rho + \nabla^2\delta\rho = 0$. Causality requires $c_s \le c$. In the nonrelativistic limit $\rho \simeq \rho_{\mathrm m}c^2$, and
$$c_s = \sqrt{\left(\frac{\partial p}{\partial\rho_{\mathrm m}}\right)_S} \quad\text{(nonrelativistic)},$$
the classical Laplace expression with the mass density.

---

# Categorical / Structural Definition

The equation of state is, structurally, a **thermodynamic potential** — specifically the energy density as a function of its natural (extensive) variables $(s, n_a)$ — and the whole apparatus of equilibrium thermodynamics is the geometry of this potential and its Legendre transforms. The energy density $\rho(s, \{n_a\})$ is the fundamental potential; its gradient is the vector of intensive variables $(T, \{\mu_a\})$; its Legendre transforms in various directions give the other potentials (pressure in the grand-canonical direction, free energy in the canonical direction). The relations $T = \partial\rho/\partial s$, $\mu_a = \partial\rho/\partial n_a$ are the statement that the intensive variables are the components of the gradient, and the Euler relation $\rho + p = Ts + \sum\mu_a n_a$ is the statement that $\rho$ is a degree-one homogeneous function of the extensive densities (Euler's theorem on homogeneous functions). The Gibbs–Duhem relation $dp = s\,dT + \sum n_a\,d\mu_a$ is the integrability condition tying the intensive variables together. This places the chapter's thermodynamics inside the standard convex-geometry framework of equilibrium thermodynamics, where stability is the convexity of $\rho$ and the speed of sound is a curvature.

The speed of sound, in this language, is a **characteristic speed of the hydrodynamic system viewed as a system of conservation laws**. Writing the conservation of baryon number, energy, and momentum as a first-order system $\partial_t U_A + \partial_j F_A^j = 0$ for a state vector $U$, the system is hyperbolic precisely when the Jacobian flux matrices have real eigenvalues, and those eigenvalues are the characteristic speeds, built from $c_s$. The condition $c_s < c$ for a causal equation of state is exactly the condition that the system is hyperbolic with subluminal characteristics, which is what makes the initial-value problem well-posed and admits shock solutions. So $c_s$ wears two hats — a thermodynamic curvature of the equation of state, and a characteristic speed of the partial differential equations — and they are the same number.

---

# Relate to Other Fields / Compression

The speed of sound is the relativistic completion of the classical **Laplace speed of sound** $c_s = \sqrt{(\partial p/\partial\rho_{\mathrm m})_S}$, with the mass density replaced by the energy density. Laplace's correction to Newton — using the adiabatic rather than the isothermal derivative — is built into the definition through the fixed-$S$ subscript, and it survives unchanged into relativity. The equation of state itself is the same object that closes the nonrelativistic Euler system; relativity only changes which density ($\rho$ versus $\rho_{\mathrm m}$) appears.

In **statistical mechanics**, the equation of state is computed from the microphysics: the partition function gives $p$, $\rho$, and $s$ as functions of temperature and chemical potential, and eliminating those gives $\rho(s, n)$. A photon gas gives $p = \rho/3$; a degenerate Fermi gas gives a polytrope $p \propto n^\gamma$.

In **general relativity and astrophysics**, the equation of state is the crucial unknown input to the Tolman–Oppenheimer–Volkoff equation: the mass–radius relation and maximum mass of a neutron star depend sensitively on how stiff the equation of state is at high density, and the speed of sound's approach to $c$ is the central question in determining the densest stable matter.

**True name:** the operational content is *"the equation of state is the one extra relation $\rho = \rho(s,n)$ that closes the fluid equations, and everything thermodynamic — $T$, $\mu$, $h$, $c_s$ — is a derivative of it"*; and the sound speed's true name is *"the adiabatic slope $(\partial p/\partial\rho)_S$, a stiffness, not a ratio"*. The discipline these enforce is: to get any thermodynamic quantity, differentiate the equation of state; and to get the sound speed, take the slope at fixed entropy per baryon, never the ratio $p/\rho$ unless the law is linear.

---

# Examples / Corollaries

**Is an instance — the photon gas (radiation), $p = \rho/3$.** Electromagnetic radiation in equilibrium has $\rho = a T^4$ and $p = \tfrac13 a T^4$, so $p = \rho/3$. This is a linear equation of state, so the sound speed is $c_s^2 = dp/d\rho = 1/3$, i.e. $c_s = 1/\sqrt3 \approx 0.577\,c$. This is the equation of state of the radiation-dominated early universe.

**Is an instance — the polytrope, $p = \kappa n^\gamma$.** Cold degenerate matter has $\rho = m_{\mathrm b}n + \kappa n^\gamma/(\gamma-1)$ and $p = \kappa n^\gamma$, with $\gamma = 5/3$ for a non-relativistic and $\gamma = 4/3$ for an ultra-relativistic degenerate electron gas. This is barotropic ($T = 0$), and the chemical potential equals the enthalpy per baryon $\mu = h = (\rho+p)/n$.

**Is an instance — the stiff fluid, $p = \rho$.** The limiting causal equation of state has $c_s^2 = dp/d\rho = 1$, so sound travels at the speed of light. It arises, for instance, for a fluid with $h = \alpha n$ (then $\rho = \tfrac\alpha2 n^2 = p$), and it is the "hardest" matter compatible with causality. No physical fluid can be stiffer.

**Is NOT an instance — pressureless dust as a closure.** Dust ($p = 0$) is a perfect fluid, but $p = 0$ is not a genuine equation of state relating $p$ to $\rho$ in a way that supports sound: the sound speed is $c_s = 0$, so dust transmits no pressure waves. It is the trivial, infinitely soft limit, and it is closed by mass conservation alone rather than by a $p(\rho)$ relation.

**Is NOT an instance — an isothermal closure for sound.** Using $p = p(\rho)$ at fixed *temperature* rather than fixed entropy gives the wrong sound speed. For an ideal gas the isothermal speed $\sqrt{(\partial p/\partial\rho)_T}$ is smaller than the adiabatic one by $\sqrt\gamma$; this is Newton's error, and it illustrates that the equation of state used for sound must be the adiabatic one, with $S$ fixed.

**Corollary — causality bounds the stiffness.** $c_s \le 1$ is equivalent to $(\partial p/\partial\rho)_S \le 1$, i.e. the pressure may not rise faster than the energy density. The bound is saturated only by $p = \rho$.

**Corollary — for radiation the trace vanishes.** Since $T^\mu{}_\mu = \rho - 3p$ for a perfect fluid (see [[Def - Perfect Fluid]]), the equation of state $p = \rho/3$ is exactly the traceless case. The conformal (scale) invariance of the electromagnetic field forces its trace to vanish, hence forces $p = \rho/3$ for a photon gas.

**Calibration check.** If you have understood the page you should be able to: (i) compute the sound speed of a photon gas, $c_s = 1/\sqrt3$, from $p = \rho/3$; (ii) explain why the derivative is taken at fixed $S$ and what goes wrong with the isothermal derivative; (iii) state the causality bound $c_s \le 1$ as a constraint on the slope of $p(\rho)$ and identify $p = \rho$ as the stiffest causal law.

---

# Unlocked by This

> [!tip] Hyperbolicity and Relativistic Shocks *(from Computational Astrophysics)*
> The speed of sound is the characteristic speed of the conservation-law system $\partial_t U_A + \partial_j F_A^j = 0$. When $c_s < c$ the system is **hyperbolic** with subluminal characteristics, the initial-value problem is well-posed, and discontinuous **shock** solutions exist, satisfying Rankine–Hugoniot jump conditions. This is the structure exploited by **high-resolution shock-capturing schemes** in every numerical simulation of relativistic jets, accretion, and stellar collapse.

> [!tip] The Neutron-Star Maximum Mass *(from General Relativity)*
> Fed into the **Tolman–Oppenheimer–Volkoff equation**, the equation of state determines the mass–radius relation of a neutron star and the maximum mass beyond which no equilibrium exists. How close $c_s$ comes to $c$ at high density — how stiff matter can be while staying causal — is the central uncertainty, and it is what gravitational-wave observations of merging neutron stars probe. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

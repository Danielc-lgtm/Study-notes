---
type: definition
subject: special-relativity
prereqs:
  - "Def - Perfect Fluid"
  - "Def - The Exterior Derivative"
  - "Def - Equation of State and Speed of Sound"
  - "Thm - Energy-Momentum Conservation projected (Euler + energy equation)"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature, $u\cdot u = 1$. The fluid is a [[Def - Perfect Fluid|simple perfect fluid]], four-velocity $u$, proper energy density $\rho$, pressure $p$, proper baryon density $n$; the enthalpy per baryon is $h = (\rho+p)/n = \mu + TS$ (see [[Def - Equation of State and Speed of Sound]]), with $\mu$ the chemical potential per baryon, $T$ the temperature, $S = s/n$ the entropy per baryon. We write $u_\mu = \eta_{\mu\nu}u^\nu$ for the one-form (lowered four-velocity); $d$ is the [[Def - The Exterior Derivative|exterior derivative]], $\star$ the [[Def - The Hodge Star|Hodge star]]. The kinematic vorticity vector $\boldsymbol\omega$ is the curl of $u$ in the fluid rest space. This is a compound page: it defines two interlocking notions — the **fluid momentum one-form** $\pi$ and the **vorticity two-form** $\Omega = d\pi$ — together with the canonical equation they satisfy, because the vorticity is the exterior derivative of the momentum and neither is usable without the other. Full registry on [[Special Relativity XXIV — Relativistic Hydrodynamics]].

> [!warning] Convention
> Gourgoulhon uses the mostly-plus signature. The fluid momentum one-form $\pi = (\mu + TS)\underline{u}$ and the canonical equation $\Omega(u,\cdot) = T\,dS$ are signature-robust in form (they are built from the exterior derivative and the contraction $\Omega(u,\cdot)$), but the explicit components $\pi_\mu = h u_\mu$ use the lowered four-velocity, whose sign convention follows the signature. We use mostly-minus throughout.

---

# Axiom Motivation

The relativistic [[Thm - Relativistic Euler Equation|Euler equation]] is a perfectly good equation of motion, but it is written with the covariant derivative and projectors, and from it the classical conservation laws of fluid mechanics — Bernoulli, irrotational flow, Kelvin's circulation theorem — are awkward to extract. The desideratum is a reformulation in which those conservation laws become almost automatic. The classical theory points the way: there, the conserved object is the circulation $\oint\mathbf{v}\cdot d\boldsymbol\ell$, vorticity is $\nabla\times\mathbf{v}$, and the cleanest statements are about line and surface integrals. In the language of differential forms, line integrals are integrals of one-forms, surface integrals of two-forms, and the relation between them is [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]]. So the natural relativistic object is a *one-form* whose circulation is conserved, and a *two-form* — its exterior derivative — that is the vorticity.

What one-form? The naive guess is the velocity one-form $u_\mu$, mimicking $\mathbf{v}$. But that is wrong, and seeing why pins down the correct object. The equation of motion, when you try to write it as a statement about $d(u_\mu)$, does not close cleanly: an enthalpy factor keeps appearing. Trace it back to the four-dimensional Euler equation $(\rho+p)a = -\nabla p - (\nabla_u p)u$. Divide by $n$ to bring in per-baryon quantities, use the thermodynamic relations $\rho + p = (\mu + TS)n$ and the Gibbs–Duhem relation $dp = s\,dT + n\,d\mu$, and the equation reorganises into a statement about $d[(\mu + TS)u_\mu]$. The combination $\mu + TS$ is exactly the enthalpy per baryon $h = (\rho+p)/n$, and it is *this* — the enthalpy-weighted velocity, not the bare velocity — that the dynamics wants. So define the **fluid momentum one-form**
$$\pi = h\,u, \qquad \pi_\mu = h\,u_\mu,$$
and the **vorticity two-form** as its exterior derivative, $\Omega = d\pi$.

Why is the enthalpy weighting the right one? Three reasons converge. First, dimensionally and physically, $h u$ is the *momentum per baryon*: $h = (\rho+p)/n$ is the enthalpy per baryon, and $\pi = hu$ is the relativistic four-momentum carried by each baryon's worth of fluid, including the work done by pressure. The natural conserved circulation is of momentum, not velocity, and $\pi$ is the momentum. Second, the analogy with a charged particle is exact: a particle in a potential has canonical momentum $mcu + qA$, and the fluid's $\pi = hu$ plays the identical role, which is why Bernoulli mirrors the conservation of a particle's energy. Third — and decisively — only with the enthalpy weighting does the equation of motion collapse to the clean *canonical equation*
$$\Omega(u, \cdot) = T\,dS,$$
which says: the one-form obtained by feeding the four-velocity into the first slot of the vorticity two-form equals the temperature times the gradient of the entropy per baryon. This is the entire equation of motion of a simple fluid, written in the exterior derivative alone — no covariant derivative, no Christoffel symbol. The enthalpy factor is what makes the left-hand side a pure $d$ of something.

What would the bare velocity cost? If we defined "vorticity" as $d(u_\mu)$, the equation of motion would carry extra enthalpy-gradient terms and would not be $d(u_\mu)(u,\cdot) = (\text{thermodynamic source})$; the conservation laws would not follow cleanly. In particular, irrotational flow would be mis-defined: the correct condition $\Omega = 0$ gives $hu = d\Psi$, the enthalpy-weighted velocity is a gradient, whereas $d(u) = 0$ would wrongly demand the bare velocity be a gradient. The enthalpy weighting is not cosmetic — it is forced by the requirement that the dynamics be a statement about a closed two-form.

Finally, why call $\Omega$ a *vorticity*? Because its rest-space part is exactly the classical vorticity. Decomposing $\Omega$ with respect to $u$ via the [[Def - The Hodge Star|Hodge star]] shows its "magnetic" part is $h$ times the curl of $u$ in the rest space — the kinematic vorticity vector $\boldsymbol\omega$ — so $\Omega = 0$ implies $\boldsymbol\omega = 0$, the flow has no local rotation, exactly as in the classical theory. The two-form $\Omega$ is the relativistic, enthalpy-weighted, four-dimensional generalisation of $\nabla\times\mathbf{v}$.

---

# The Definition

For a simple perfect fluid, the **fluid momentum one-form** is
$$\pi := h\,u, \qquad \pi_\mu = h\,u_\mu, \qquad h = \frac{\rho+p}{n} = \mu + TS,$$
the enthalpy per baryon times the lowered four-velocity; it is the four-momentum per baryon of the fluid. The **vorticity two-form** is its exterior derivative,
$$\boxed{\Omega := d\pi = d(h\,u),}$$
with components
$$\Omega_{\mu\nu} = \partial_\mu(h u_\nu) - \partial_\nu(h u_\mu) = \nabla_\mu(h u_\nu) - \nabla_\nu(h u_\mu).$$
The equation of motion of an isolated simple fluid is the **canonical equation of relativistic fluid dynamics**,
$$\Omega(u, \cdot) = T\,dS, \qquad u^\mu\big[\partial_\mu(h u_\alpha) - \partial_\alpha(h u_\mu)\big] = T\,\partial_\alpha S,$$
equivalent (together with baryon conservation $\nabla_\mu(nu^\mu) = 0$) to the conservation law $\nabla_\mu T^{\mu\nu} = 0$. In words: *the one-form obtained by setting the first argument of the vorticity two-form to the fluid four-velocity equals the temperature times the gradient of the entropy per baryon.*

For a **barotropic** fluid ($T = 0$) or an **isentropic** flow ($dS = 0$), the right-hand side vanishes and the canonical equation reduces to
$$\Omega(u, \cdot) = 0.$$

The two-form is linked to the **kinematic vorticity vector** $\boldsymbol\omega = \nabla\times_u u$ (the curl of $u$ in the fluid rest space) by Hodge duality: the orthogonal decomposition of $\Omega$ with respect to $u$ is
$$\Omega = T\,dS\wedge u + h\,\boldsymbol\epsilon(u, \boldsymbol\omega, \cdot, \cdot),$$
where $\boldsymbol\epsilon$ is the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]]; the second term is the rotational ("magnetic") part of the vorticity, carrying the local rotation of the flow.

---

# Categorical / Structural Definition

The vorticity two-form is the **field strength of the fluid momentum one-form**, and the entire structure is an exact replica of the gauge-theoretic / electromagnetic pattern. In [[Special Relativity XXII — Maxwell's Equations|electromagnetism]] one has a potential one-form $A$ and a field-strength two-form $F = dA$; here one has the momentum one-form $\pi$ and the vorticity two-form $\Omega = d\pi$. The structural facts are identical and follow purely from $\Omega$ being an *exact* two-form. Because $\Omega = d\pi$, it is automatically **closed**, $d\Omega = d^2\pi = 0$ — the Bianchi identity of the fluid. Because it is closed, its flux through a boundaryless surface depends only on the homology class of the surface ([[Thm - Stokes Theorem on Spacetime|Stokes' theorem]]), which is the geometric content of Kelvin's circulation theorem. And because $\pi$ is the primitive, the vanishing of $\Omega$ means $\pi$ is closed hence locally exact (Poincaré lemma), which is irrotational flow with a velocity potential.

In the Hamiltonian framework of [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|geometric mechanics]], $\pi$ is a section of the cotangent bundle — the canonical momentum of the fluid — and $\Omega$ is the pullback to the flow of the canonical symplectic two-form. Brandon Carter showed that the canonical equation $\Omega(u,\cdot) = T\,dS$ is then a Hamilton equation $\dot\pi = -\nabla H$ for a quadratic Hamiltonian on the cotangent bundle, so the closedness $d\Omega = 0$ is the relativistic-fluid analogue of the conservation of the symplectic structure under Hamiltonian flow. In this reading the fluid is a continuum of Hamiltonian systems sharing one symplectic geometry, the conserved circulation $\oint\pi$ is a Poincaré–Cartan relative integral invariant, and Bernoulli's theorem is the momentum map of the time-translation symmetry. The vorticity two-form is thus simultaneously a "field strength" (electromagnetic analogy) and a "symplectic form" (Hamiltonian analogy) — two faces of the same closed two-form.

---

# Relate to Other Fields / Compression

The vorticity two-form is the relativistic completion of the classical **vorticity** $\boldsymbol\omega = \nabla\times\mathbf{v}$, with two refinements: it is four-dimensional (a two-form on spacetime, not a vector in space), and it is *enthalpy-weighted* (built from $hu$, not $u$). In the nonrelativistic limit the enthalpy per baryon becomes the constant $m_{\mathrm b}c^2$, which can be divided out, and $\Omega$ reduces to the spacetime two-form whose rest-space part is the classical vorticity. The fluid momentum one-form $\pi = hu$ reduces to (a constant times) the velocity one-form, and the circulation $\oint\pi$ to the classical circulation.

The structure is **identical to electromagnetism**: $\pi$ is to $\Omega$ as the electromagnetic potential $A$ is to the field strength $F = dA$ (see [[Special Relativity XXI — The Electromagnetic Field]]). Both are exact two-forms; both have a "Bianchi identity" $d\Omega = 0$, $dF = 0$ automatic from exactness; and the conserved-flux theorems (Kelvin for the fluid, magnetic-flux conservation for a perfect conductor) are the same statement about a closed two-form transported by the flow. This is the deepest single analogy of the chapter.

**True name:** the operational content is *"package the flow into the momentum-per-baryon one-form $\pi = hu$; its exterior derivative $\Omega = d\pi$ is the vorticity, and the entire equation of motion is $\Omega(u,\cdot) = T\,dS$"*. The reusable discipline: to get a conservation law (Bernoulli, irrotational, Kelvin), do not grind the covariant Euler equation — form $\pi = hu$, apply $d$, and read the canonical equation, which is metric-free and makes closedness and exactness do all the work.

---

# Examples / Corollaries

**Is an instance — a barotropic flow has $\Omega(u,\cdot) = 0$.** For a barotropic fluid $T = 0$, so the canonical equation reduces to $\Omega(u,\cdot) = 0$: feeding the four-velocity into the vorticity two-form gives zero. This is the case of cold dense matter (white dwarfs, neutron-star interiors) and is the setting in which Bernoulli and Kelvin take their simplest form.

**Is an instance — an isentropic flow has $\Omega(u,\cdot) = 0$.** If the entropy per baryon $S$ is uniform over the whole fluid (not merely constant along each line), then $dS = 0$ and again $\Omega(u,\cdot) = 0$. This is the common idealisation for a fluid that started uniform and flows adiabatically.

**Is an instance — irrotational flow has $\Omega = 0$.** A flow with vanishing vorticity two-form, $\Omega = d\pi = 0$, has $\pi = hu$ closed, hence locally $hu = d\Psi$ for a velocity potential $\Psi$; see [[Ex - Irrotational flow and the velocity potential]]. Irrotational flow requires $\boldsymbol\omega = 0$ *and* $T\,dS = 0$ (barotropic or isentropic).

**Is NOT an instance — the bare velocity one-form $u$.** The exterior derivative $d(u_\mu)$ is *not* the vorticity two-form: it lacks the enthalpy weighting, and the equation of motion is not a clean statement about $d(u)$. Using $du$ in place of $\Omega = d(hu)$ would mis-define irrotationality (demanding $u$ rather than $hu$ be a gradient) and would not yield the canonical equation. The enthalpy factor is essential.

**Is NOT an instance — a baroclinic flow as "irrotational".** A flow in which pressure and entropy gradients cross has $T\,dS \ne 0$ along the flow, so $\Omega(u,\cdot) \ne 0$ even if the kinematic vorticity $\boldsymbol\omega$ momentarily vanishes: vorticity is *generated* by the baroclinic term. Such a flow is not irrotational and its circulation is not conserved — the obstruction is exactly the right-hand side $T\,dS$ of the canonical equation.

**Corollary — the canonical equation is metric-free.** The left side $\Omega(u,\cdot)$ uses only the exterior derivative (in $\Omega = d\pi$) and the contraction with $u$; the right side $T\,dS$ uses only the gradient $d$. No covariant derivative or Christoffel symbol appears. This is the practical advantage over the covariant Euler equation: $\Omega = d\pi$ is the same in any coordinates.

**Corollary — vorticity is closed.** $d\Omega = d(d\pi) = 0$ identically, the fluid Bianchi identity. This is what makes the flux $\int_\mathcal{S}\Omega$ depend only on the boundary $\partial\mathcal{S}$ and underlies Kelvin's theorem.

**Calibration check.** If you have understood the page you should be able to: (i) write $\pi = hu$ and explain why the enthalpy per baryon $h = (\rho+p)/n$ rather than $1$ is the right weight; (ii) state the canonical equation $\Omega(u,\cdot) = T\,dS$ in words; (iii) explain why $\Omega = 0$ gives $hu = d\Psi$ (not $u = d\Psi$) and identify the obstruction to circulation conservation as the term $T\,dS$.

---

# Unlocked by This

> [!tip] Bernoulli's Theorem *(from §24.3)*
> In a stationary flow, contracting the canonical equation with a time-translation symmetry shows the scalar $\langle\pi, u_0\rangle = h\Gamma$ is constant along each fluid line — [[Thm - Relativistic Bernoulli Theorem|relativistic Bernoulli's theorem]]. It is the momentum-one-form formulation: $\pi$ plays the role of a particle's four-momentum, and Bernoulli is the conservation of its time-component along the flow.

> [!tip] Kelvin's Circulation Theorem *(from §24.3)*
> The circulation $\oint_\mathcal{C}\pi$ equals $\int_\mathcal{S}\Omega$ by [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]], and the closedness $d\Omega = 0$ together with the canonical equation gives [[Thm - Kelvin's Circulation Theorem (exterior-calculus formulation)|Kelvin's theorem]]: circulation is conserved by transport along the flow for barotropic or isentropic fluids. The vorticity two-form is the object whose flux is the transported invariant.

> [!tip] Relativistic Magnetohydrodynamics and Frozen-In Flux *(from Plasma Astrophysics)*
> Coupling the fluid to the electromagnetic field, the vorticity two-form $\Omega$ and the field-strength two-form $F$ play structurally identical roles. For a perfectly conducting fluid, the analogue of Kelvin's theorem is **Alfvén's frozen-in theorem**: magnetic flux through any loop carried by the fluid is conserved, so field lines are frozen into the matter. This is the mechanism of **jet collimation** and **dynamo field amplification** in accretion disks and stars.

> [!tip] Carter's Hamiltonian Formulation *(from Geometric Mechanics)*
> The canonical equation $\Omega(u,\cdot) = T\,dS$ is a **Hamilton equation** $\dot\pi = -\nabla H$ for the fluid momentum one-form $\pi$, with a quadratic Hamiltonian on the cotangent bundle (Carter). The vorticity two-form is the pullback of the canonical symplectic form, circulation is a Poincaré–Cartan relative integral invariant, and the conservation laws are momentum maps — placing relativistic fluid dynamics inside [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|symplectic geometry]].

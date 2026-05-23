---
type: exercise
subject: general-relativity
difficulty: "⭐"
prereqs:
  - "Def - Stress-Energy Tensor"
  - "Def - Four-Vector"
  - "Def - Spacetime Manifold"
tags: [physics, general-relativity, fluids]
---

# Problem Statement

**Verify that the stress-energy tensor of dust is $T^{\mu\nu} = \rho u^\mu u^\nu$, where $\rho$ is the rest-frame energy density and $u^\mu$ is the unit timelike four-velocity field of the dust. Specifically:**

(a) Show that this $T^{\mu\nu}$ has the correct rest-frame components ($T^{00} = \rho$, all others zero).

(b) Show that conservation $\nabla_\mu T^{\mu\nu} = 0$ implies both the **continuity equation** $\nabla_\mu(\rho u^\mu) = 0$ (number of dust particles conserved) and the **geodesic equation** $u^\mu \nabla_\mu u^\nu = 0$ (each dust particle follows a geodesic).

**Recall:**

![[Def - Stress-Energy Tensor#The Definition]]

A four-velocity $u^\mu$ is a timelike unit vector field, normalised $g_{\mu\nu} u^\mu u^\nu = 1$ (signature $+---$), future-directed. **Dust** is the simplest matter model: a continuum of non-interacting point particles, characterised only by rest-frame energy density $\rho$ (a scalar) and four-velocity $u^\mu$. The geodesic equation is $u^\mu \nabla_\mu u^\nu = 0$, expressing that each particle follows a geodesic of the metric.

---

# Convergent Strategy

**Problem class:** This is a verification exercise — given a candidate stress-energy tensor, check its properties (rest-frame components, conservation). The class is "tensor identity verification" within continuous-matter GR. Such problems are direct applications of the variational definition of $T^{\mu\nu}$ and the Bianchi identity.

**Assumption pattern:** The given data are (i) the candidate form $T^{\mu\nu} = \rho u^\mu u^\nu$, (ii) the normalisation $g_{\mu\nu} u^\mu u^\nu = 1$, (iii) the requirement of conservation $\nabla_\mu T^{\mu\nu} = 0$. The normalisation will be used in the calculation of conservation (via $u_\nu \nabla_\mu u^\nu = 0$, a consequence of $u^\nu u_\nu = 1$ being constant). Part (a) is checked by evaluation in the rest frame; part (b) by direct computation of $\nabla_\mu T^{\mu\nu}$ and projection.

**Theorem routing:** The route is from the definition $T^{\mu\nu} = \rho u^\mu u^\nu$ to: (i) rest-frame evaluation (direct substitution); (ii) covariant derivative computation, decomposed via projections along and orthogonal to $u^\mu$, yielding two equations — the continuity equation and the geodesic equation. The key intermediate identity is $u_\nu \nabla_\mu u^\nu = 0$ (since $u^\nu u_\nu = 1$ is constant, $\nabla_\mu(u^\nu u_\nu) = 2 u_\nu \nabla_\mu u^\nu = 0$).

**Key decision point:** The non-obvious choice is *how to decompose* the conservation equation $\nabla_\mu T^{\mu\nu} = 0$ into two independent equations. Direct expansion gives one tensor equation in $\nu$, but it bundles together two physical statements (energy conservation and geodesic motion). The decomposition into "parallel to $u$" (giving continuity) and "orthogonal to $u$" (giving geodesic equation) is the natural physical split. Without this split, one has a single complicated tensor equation; with it, one gets the two recognisable physical equations.

---

# Legal Operations Used

1. **Operation 1 from the topic page** (Lift Newtonian intuitions to GR): The classical equation for dust is the continuity equation $\partial_t \rho + \nabla\cdot(\rho \vec v) = 0$, which is the Newtonian limit of the relativistic $\nabla_\mu(\rho u^\mu) = 0$. Knowing this Newtonian analogue tells us what to expect from the projection along $u$.

2. **Operation 5 from the topic page** (Use contracted Bianchi to deduce conservation): The conservation $\nabla_\mu T^{\mu\nu} = 0$ is enforced by the Einstein equations via the contracted Bianchi identity. So we *expect* the dust $T^{\mu\nu}$ to be conserved when the dust follows the natural equations of motion — and we verify this gives the geodesic equation.

---

# Hints

> [!note]- Hint 1
> The dust stress-energy in the rest frame: $u^\mu = (1, 0, 0, 0)$. Compute $T^{00}$ from the formula and check it equals $\rho$. Then check the other components vanish.

> [!note]- Hint 2
> For conservation: compute $\nabla_\mu T^{\mu\nu}$ directly using the product rule. You'll get two terms, $u^\nu \nabla_\mu(\rho u^\mu) + \rho u^\mu \nabla_\mu u^\nu$. These can't be set independently to zero from a single equation $\nabla_\mu T^{\mu\nu} = 0$.

> [!note]- Hint 3
> To separate the two physical statements, project onto $u^\nu$ (parallel projection) and onto the orthogonal direction (using $h^{\nu\sigma} = g^{\nu\sigma} - u^\nu u^\sigma$). The parallel projection uses $u_\nu u^\nu = 1$, $u_\nu \nabla_\mu u^\nu = 0$. The orthogonal projection isolates the $\rho u^\mu \nabla_\mu u^\nu$ term.

> [!note]- Hint 4
> The "parallel" projection should give an equation involving $\nabla_\mu(\rho u^\mu)$ — the **continuity equation** (the dust analogue of mass conservation). The "orthogonal" projection should give $u^\mu \nabla_\mu u^\nu = 0$ — the **geodesic equation** for the dust four-velocity.

---

# Solution

The proof breaks into three steps. Step 1 verifies the rest-frame components by direct substitution. Step 2 computes the divergence $\nabla_\mu T^{\mu\nu}$ using the product rule. Step 3 projects this onto two orthogonal pieces — parallel to $u^\mu$ (giving continuity) and orthogonal to $u^\mu$ (giving geodesic equation). The non-obvious move is in Step 3, where we recognise that the single equation $\nabla_\mu T^{\mu\nu} = 0$ bundles two physical equations that must be separated by projection.

**Step 1: Rest-frame components are $T^{00} = \rho$, others zero.**

In the local rest frame of the dust, $u^\mu = (1, 0, 0, 0)$. Substituting into $T^{\mu\nu} = \rho u^\mu u^\nu$: $T^{00} = \rho \cdot 1 \cdot 1 = \rho$; $T^{0i} = \rho \cdot 1 \cdot 0 = 0$; $T^{ij} = \rho \cdot 0 \cdot 0 = 0$.

> [!note]- Derivation
> Direct substitution: $T^{\mu\nu} = \rho u^\mu u^\nu$, with $u^\mu = (1, 0, 0, 0)$ giving $u^\mu u^\nu = \mathrm{diag}(1, 0, 0, 0)$. So $T^{\mu\nu} = \rho \cdot \mathrm{diag}(1, 0, 0, 0) = \mathrm{diag}(\rho, 0, 0, 0)$. Only $T^{00} = \rho$, all other components zero — as expected: dust has energy density $\rho$ in its rest frame, but no momentum density, no spatial stress.

**Step 2: Compute $\nabla_\mu T^{\mu\nu}$ using the product rule.**

By the product rule:
$$\nabla_\mu T^{\mu\nu} = \nabla_\mu(\rho u^\mu u^\nu) = (\nabla_\mu \rho) u^\mu u^\nu + \rho (\nabla_\mu u^\mu) u^\nu + \rho u^\mu \nabla_\mu u^\nu.$$

Combining the first two: $[\nabla_\mu(\rho u^\mu)] u^\nu + \rho u^\mu \nabla_\mu u^\nu$.

> [!note]- Derivation
> $\nabla_\mu(\rho u^\mu u^\nu) = \rho \nabla_\mu(u^\mu u^\nu) + u^\mu u^\nu \nabla_\mu \rho = \rho [u^\nu \nabla_\mu u^\mu + u^\mu \nabla_\mu u^\nu] + u^\mu u^\nu \nabla_\mu \rho$. Grouping: $\nabla_\mu T^{\mu\nu} = [u^\mu \nabla_\mu \rho + \rho \nabla_\mu u^\mu] u^\nu + \rho u^\mu \nabla_\mu u^\nu = [\nabla_\mu(\rho u^\mu)] u^\nu + \rho u^\mu \nabla_\mu u^\nu$. The first bracket is a scalar; the whole expression is a four-vector.

**Step 3: Project to separate the two equations.**

(i) **Parallel projection** (contract with $u_\nu$):
$$u_\nu \nabla_\mu T^{\mu\nu} = u_\nu u^\nu \nabla_\mu(\rho u^\mu) + \rho u^\mu \cdot u_\nu \nabla_\mu u^\nu = \nabla_\mu(\rho u^\mu) + 0 = \nabla_\mu(\rho u^\mu),$$
using $u^\nu u_\nu = 1$ and $u_\nu \nabla_\mu u^\nu = \frac{1}{2}\nabla_\mu(u^\nu u_\nu) = 0$ (since $u^\nu u_\nu = 1$ is constant).

Setting $u_\nu \nabla_\mu T^{\mu\nu} = 0$ gives the **continuity equation** $\nabla_\mu(\rho u^\mu) = 0$ — the relativistic conservation of the number of dust particles.

(ii) **Orthogonal projection** (contract with $h^{\sigma}{}_\nu = \delta^\sigma{}_\nu - u^\sigma u_\nu$):
$$h^{\sigma}{}_\nu \nabla_\mu T^{\mu\nu} = h^{\sigma}{}_\nu [u^\nu \nabla_\mu(\rho u^\mu) + \rho u^\mu \nabla_\mu u^\nu] = 0 + \rho u^\mu \nabla_\mu u^\sigma,$$
using $h^{\sigma}{}_\nu u^\nu = 0$.

Setting this to zero (with $\rho \neq 0$) gives the **geodesic equation** $u^\mu \nabla_\mu u^\nu = 0$ — each dust particle follows a geodesic of the spacetime metric.

> [!note]- Derivation
> Parallel projection: $u_\nu T^{\mu\nu}_{,\mu} = u_\nu[u^\nu \nabla_\mu(\rho u^\mu) + \rho u^\mu \nabla_\mu u^\nu]$. The first piece: $u_\nu u^\nu \nabla_\mu(\rho u^\mu) = 1 \cdot \nabla_\mu(\rho u^\mu)$. The second: $\rho u^\mu \cdot u_\nu \nabla_\mu u^\nu$, and $u_\nu \nabla_\mu u^\nu = \frac{1}{2}\nabla_\mu(u^\nu u_\nu) = \frac{1}{2}\nabla_\mu 1 = 0$. So the parallel projection gives $\nabla_\mu(\rho u^\mu) = 0$.
>
> Orthogonal projection: $h^\sigma{}_\nu T^{\mu\nu}_{,\mu} = (\delta^\sigma{}_\nu - u^\sigma u_\nu)[u^\nu \nabla_\mu(\rho u^\mu) + \rho u^\mu \nabla_\mu u^\nu]$. The terms with $u^\nu$ get killed by $(\delta^\sigma{}_\nu - u^\sigma u_\nu) u^\nu = u^\sigma - u^\sigma \cdot 1 = 0$. Left over: $h^\sigma{}_\nu \rho u^\mu \nabla_\mu u^\nu = \rho u^\mu \nabla_\mu u^\sigma - \rho u^\sigma u_\nu u^\mu \nabla_\mu u^\nu = \rho u^\mu \nabla_\mu u^\sigma - 0$ (second term vanishes for the same reason). So the orthogonal projection gives $\rho u^\mu \nabla_\mu u^\sigma = 0$. With $\rho \neq 0$, this is $u^\mu \nabla_\mu u^\sigma = 0$ — the geodesic equation.

> [!note]- Complete formal solution
> Let $T^{\mu\nu} = \rho u^\mu u^\nu$ be the dust stress-energy tensor, where $\rho$ is the rest-frame energy density and $u^\mu$ is the unit timelike four-velocity field ($g_{\mu\nu} u^\mu u^\nu = 1$).
>
> **Part (a) — rest-frame components.** In the rest frame, $u^\mu = (1, 0, 0, 0)$. Then $u^\mu u^\nu = \mathrm{diag}(1, 0, 0, 0)$, so $T^{\mu\nu} = \rho u^\mu u^\nu = \rho \cdot \mathrm{diag}(1, 0, 0, 0)$. Hence $T^{00} = \rho$ and all other components are zero — confirming that dust has rest-frame energy density $\rho$ with no momentum density and no spatial stress.
>
> **Part (b) — conservation gives continuity and geodesic equations.** Compute the divergence:
> $$\nabla_\mu T^{\mu\nu} = \nabla_\mu(\rho u^\mu u^\nu) = u^\nu \nabla_\mu(\rho u^\mu) + \rho u^\mu \nabla_\mu u^\nu.$$
>
> *Parallel projection* (contract with $u_\nu$):
> $$u_\nu \nabla_\mu T^{\mu\nu} = u_\nu u^\nu \nabla_\mu(\rho u^\mu) + \rho u^\mu u_\nu \nabla_\mu u^\nu = \nabla_\mu(\rho u^\mu)$$
> using $u_\nu u^\nu = 1$ and $u_\nu \nabla_\mu u^\nu = \frac{1}{2}\nabla_\mu(u^\nu u_\nu) = 0$. Setting $u_\nu \nabla_\mu T^{\mu\nu} = 0$ (from $\nabla_\mu T^{\mu\nu} = 0$) gives the **continuity equation**:
> $$\boxed{\nabla_\mu(\rho u^\mu) = 0}.$$
>
> *Orthogonal projection* (contract with $h^\sigma{}_\nu = \delta^\sigma{}_\nu - u^\sigma u_\nu$):
> $$h^\sigma{}_\nu \nabla_\mu T^{\mu\nu} = (\delta^\sigma{}_\nu - u^\sigma u_\nu)[u^\nu \nabla_\mu(\rho u^\mu) + \rho u^\mu \nabla_\mu u^\nu].$$
> The $u^\nu$ pieces cancel ($h^\sigma{}_\nu u^\nu = u^\sigma - u^\sigma = 0$), and the remaining piece is $\rho u^\mu \nabla_\mu u^\sigma$ (using $u_\nu \nabla_\mu u^\nu = 0$ as before for the second term). Setting equal to zero (with $\rho \neq 0$) gives the **geodesic equation**:
> $$\boxed{u^\mu \nabla_\mu u^\nu = 0}.$$
>
> So conservation of dust stress-energy yields both: (i) conservation of dust energy/number (continuity), and (ii) each dust particle following a geodesic (geodesic equation). $\square$

---

# Key Takeaways

**The decomposition of a tensor conservation law into projections.** When a divergence-free tensor equation $\nabla_\mu T^{\mu\nu} = 0$ is given, the right physical analysis is often to *project* onto a preferred direction (like the four-velocity $u^\mu$ for a fluid) and orthogonal to it. The parallel projection gives a "scalar" conservation law (energy or particle number); the orthogonal projection gives a "force" equation (the equation of motion for the fluid elements). This is the universal pattern for fluid mechanics in relativity, applied to dust here and to perfect fluids more generally in [[Thm - Stress-Energy of a Perfect Fluid]]. The trigger for this technique: any time you have a conservation law for a tensor that's built from a velocity field, project onto the velocity and orthogonal.

**The geodesic equation comes from conservation of stress-energy.** A remarkable structural fact: the geodesic equation — Einstein's prescription that freely-falling test bodies follow geodesics — is *not* an independent postulate but a *consequence* of the Einstein equations (which force $\nabla_\mu T^{\mu\nu} = 0$ via the contracted Bianchi identity) applied to dust. So Einstein's two great equations (the field equations and the equation of motion) are not independent; the second follows from the first. This was proved rigorously by **Einstein–Infeld–Hoffmann** (1938) and is one of the most beautiful self-consistency results in physics. The trigger for recognising this pattern: in any field theory where matter equations of motion follow from a conserved tensor coupling to gravity, the equation of motion is a consequence rather than a postulate.

**Pressure $p = 0$ is the structural simplicity of dust.** The dust formula $T^{\mu\nu} = \rho u^\mu u^\nu$ is the $p \to 0$ limit of the perfect fluid $T^{\mu\nu} = (\rho + p) u^\mu u^\nu - p g^{\mu\nu}$. The simplicity is what makes dust a natural first model: no equation of state to specify, no pressure gradients, no thermodynamic complications. In cosmology, "matter" (cold dark matter, galaxies treated as test particles on large scales) is well-modelled as dust. In particular, the cosmic matter-dominated era is governed by dust + gravity, and the cosmological scaling $\rho \propto a^{-3}$ (with $a$ the scale factor) is the continuity equation for cosmological dust expanding with the universe. The trigger for recognising dust: any problem involving non-interacting massive particles, with negligible thermal pressure, is well-modelled as dust — collapse of a spherical dust cloud (Oppenheimer-Snyder model of black hole formation), large-scale structure formation in cosmology, etc.

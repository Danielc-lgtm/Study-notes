---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Perfect Fluid"
  - "Def - The Energy-Momentum Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

1. Write out the components of the perfect-fluid tensor $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$ in the local rest frame of the fluid ($u = (1,0,0,0)$) and confirm they equal $\mathrm{diag}(\rho, p, p, p)$ — energy density $\rho$ and isotropic pressure $p$.
2. Verify by direct contraction that $\rho = T_{\mu\nu}u^\mu u^\nu$ (energy density measured by a comoving observer) and that the rest-frame momentum density $T^{0i}$ vanishes.
3. Compute the trace $T^\mu{}_\mu$ and deduce that a traceless perfect fluid is exactly radiation, $p = \rho/3$.

**Recall:**

![[Def - Perfect Fluid#The Definition]]

The metric is $\eta = \mathrm{diag}(1,-1,-1,-1)$, and the [[Def - The Energy-Momentum Tensor|energy–momentum tensor]] $T^{\mu\nu}$ has the interpretation: $T^{00}$ is energy density, $T^{0i}$ momentum density, $T^{ij}$ the stress (momentum flux). A perfect fluid has isotropic rest-frame stress $S_{ij} = p\,\delta_{ij}$.

---

# Convergent Strategy

**Problem class.** A *verify-the-definition-in-a-convenient-frame* problem — the most basic check that the tensor means what it is supposed to. Per the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]], evaluating a tensor in the rest frame, where most components are simple, is the standard first move.

**Assumption pattern.** Work in the rest frame, where $u = (1,0,0,0)$, so $u^\mu u^\nu$ is $\mathrm{diag}(1,0,0,0)$ and $\eta^{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$. The signpost is "rest frame" — the frame in which the fluid is at rest and the physics is simplest.

**Theorem routing.** Direct substitution into $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\,\eta^{\mu\nu}$ (see [[Def - Perfect Fluid]]); contractions for the energy density and trace.

**Key decision point.** The only subtlety is sign-bookkeeping with the mostly-minus metric: $T^{ij} = -p\,\eta^{ij} = -p(-\delta^{ij}) = +p\,\delta^{ij}$, so the spatial stress comes out $+p$, the physically correct positive pressure. The natural slip is to drop the minus sign on $\eta^{ij}$ and get the wrong sign for the pressure.

---

# Legal Operations Used

1. **Compute an invariant in the most convenient frame** (the rest-frame technique from [[Special Relativity I — Postulates and Lorentz Transformations|SR I]]): evaluate the tensor where $u = (1,0,0,0)$.

2. **Compute thermodynamic derivatives / trace relations** (operation 10 from the topic page): the trace $T^\mu{}_\mu = \rho - 3p$ links the tensor to the equation of state.

---

# Hints

> [!note]- Hint 1
> In the rest frame $u^\mu = (1,0,0,0)$, so $u^\mu u^\nu$ has only the $00$ component equal to $1$. Then $T^{00} = (\rho+p)\cdot 1 - p\cdot\eta^{00} = (\rho+p) - p = \rho$.

> [!note]- Hint 2
> $T^{ij} = (\rho+p)\cdot 0 - p\,\eta^{ij}$. With $\eta^{ij} = -\delta^{ij}$ (mostly-minus), $T^{ij} = +p\,\delta^{ij}$. And $T^{0i} = (\rho+p)u^0 u^i - p\,\eta^{0i} = 0$.

> [!note]- Hint 3
> The trace is $T^\mu{}_\mu = \eta_{\mu\nu}T^{\mu\nu} = (\rho+p)(u\cdot u) - p\,\eta_{\mu\nu}\eta^{\mu\nu} = (\rho+p) - 4p = \rho - 3p$. Traceless means $\rho = 3p$, i.e. $p = \rho/3$.

---

# Solution

In the rest frame the perfect-fluid tensor is diagonal, with energy density $\rho$ on the time–time slot and isotropic pressure $p$ on the space–space slots; its trace is $\rho - 3p$, vanishing exactly for radiation.

**Step 1: Rest-frame components.**

> [!note]- Derivation
> In the local rest frame, $u^\mu = (1,0,0,0)$, so $u^\mu u^\nu$ has the single nonzero entry $(u^0)^2 = 1$ at $\mu=\nu=0$. Then:
> - $T^{00} = (\rho+p)(1) - p\,\eta^{00} = (\rho+p) - p(1) = \rho$.
> - $T^{0i} = (\rho+p)u^0 u^i - p\,\eta^{0i} = 0 - 0 = 0$.
> - $T^{ij} = (\rho+p)u^i u^j - p\,\eta^{ij} = 0 - p(-\delta^{ij}) = p\,\delta^{ij}$.
>
> So
> $$T^{\mu\nu}_{\text{rest}} = \begin{pmatrix} \rho & 0 & 0 & 0 \\ 0 & p & 0 & 0 \\ 0 & 0 & p & 0 \\ 0 & 0 & 0 & p \end{pmatrix} = \mathrm{diag}(\rho, p, p, p).$$
> The time–time component is the energy density $\rho$; the space–space part is the **isotropic** stress $p\,\delta^{ij}$ — a single pressure, equal in all directions, no shear. This isotropy is the defining feature of a [[Def - Perfect Fluid|perfect fluid]].

**Step 2: Energy density and vanishing momentum density.**

> [!note]- Derivation
> Contract twice with the four-velocity (in any frame, by tensor invariance):
> $$T_{\mu\nu}u^\mu u^\nu = (\rho+p)(u\cdot u)^2 - p(u\cdot u) = (\rho+p)(1)^2 - p(1) = \rho,$$
> using $u\cdot u = 1$. So $\rho$ is indeed the energy density a comoving observer measures. The rest-frame momentum density $T^{0i} = 0$ (Step 1) confirms there is no energy flux relative to the fluid — no heat conduction, as required for a perfect fluid.

**Step 3: The trace and radiation.**

> [!note]- Derivation
> The trace is
> $$T^\mu{}_\mu = \eta_{\mu\nu}T^{\mu\nu} = (\rho+p)(u_\mu u^\mu) - p\,\eta_{\mu\nu}\eta^{\mu\nu} = (\rho+p)(1) - p(4) = \rho - 3p,$$
> using $u\cdot u = 1$ and $\eta_{\mu\nu}\eta^{\mu\nu} = \delta^\mu_\mu = 4$. A **traceless** perfect fluid has $\rho - 3p = 0$, i.e.
> $$p = \frac{\rho}{3},$$
> which is the equation of state of **radiation** (a photon gas). The electromagnetic energy–momentum tensor is traceless (from the conformal invariance of the free electromagnetic field), so a photon gas *must* have $p = \rho/3$ — confirmed here from the trace alone.

> [!note]- Complete formal solution
> In the rest frame $u = (1,0,0,0)$, so $T^{\mu\nu} = (\rho+p)u^\mu u^\nu - p\eta^{\mu\nu}$ gives $T^{00} = (\rho+p) - p = \rho$, $T^{0i} = 0$, and $T^{ij} = -p\eta^{ij} = p\delta^{ij}$, i.e. $\mathrm{diag}(\rho,p,p,p)$ — energy density and isotropic pressure. Contracting, $T_{\mu\nu}u^\mu u^\nu = (\rho+p) - p = \rho$ (energy density) and $T^{0i} = 0$ (no rest-frame momentum density). The trace is $T^\mu{}_\mu = (\rho+p) - 4p = \rho - 3p$, vanishing iff $p = \rho/3$ — radiation. $\blacksquare$

---

# Key Takeaways

**The rest frame is where a tensor reveals its meaning.** The basic lesson is that evaluating $T^{\mu\nu}$ in the fluid rest frame, where $u = (1,0,0,0)$, immediately exposes its physical content: energy density on the time–time slot, isotropic pressure on the space–space slots, zero momentum density. The mostly-minus signature flips the sign of $\eta^{ij}$, which is exactly what turns $-p\,\eta^{ij}$ into the physically correct $+p\,\delta^{ij}$ — a positive, isotropic pressure. The transferable diagnostic is that whenever you meet a covariant tensor expression and want its physical interpretation, go to the rest frame (or whatever frame makes $u$ simple): the components there are the measured quantities, and the covariant expression is just their frame-independent packaging. This is the single most-used labour-saving move in relativistic physics.

**Isotropy of the rest-frame stress is the definition of "perfect".** The space–space part coming out as $p\,\delta^{ij}$ — diagonal, equal in all directions, no off-diagonal shear — is not incidental; it *is* what makes the fluid perfect. A general medium would have a full symmetric stress matrix with shear (viscosity) and possibly off-diagonal heat flux; the perfect fluid is precisely the case where the rest-frame stress is a single number times the identity. The trigger to recall: "perfect fluid" means "isotropic rest-frame stress, no shear, no conduction", and the tensor $\mathrm{diag}(\rho, p, p, p)$ is the visual signature of that. Any departure from this diagonal isotropic form signals dissipation and takes the fluid outside the perfect class.

**The trace is the equation-of-state diagnostic, and tracelessness means radiation.** The trace $T^\mu{}_\mu = \rho - 3p$ is a quick, frame-independent probe of the equation of state: it vanishes exactly for $p = \rho/3$, radiation. This connects to a deep fact — the electromagnetic field's energy–momentum tensor is traceless because the free electromagnetic field is conformally (scale) invariant, and that tracelessness *forces* a photon gas to have $p = \rho/3$. The reusable insight is that the trace of the energy–momentum tensor measures conformal symmetry: a traceless $T^{\mu\nu}$ corresponds to scale-invariant matter (massless, like radiation), while a nonzero trace signals a scale (a mass, a condensate). Whenever you want a quick check on a fluid's stiffness or its conformal character, compute $\rho - 3p$.

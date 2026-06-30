---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Energy-Momentum Tensor of the Electromagnetic Field"
  - "Def - The Energy-Momentum Tensor"
  - "Def - Perfect Fluid"
tags: [physics, special-relativity]
---

# Problem Statement

The vanishing trace of the electromagnetic energy-momentum tensor is one of its deepest properties — it expresses the masslessness of the photon, the conformal invariance of Maxwell theory in four dimensions, and, when applied to a thermal bath of photons, fixes the **equation of state of radiation** $p = \rho/3$. Working with $c = 1$ unless restored, mostly-minus signature:

1. **Direct trace computation.** Start from $T^{\text{em}}_{\alpha\beta} = \varepsilon_0(F_{\mu\alpha}F^\mu{}_\beta - \tfrac14\eta_{\alpha\beta}F_{\mu\nu}F^{\mu\nu})$ and compute $\eta^{\alpha\beta}T^{\text{em}}_{\alpha\beta}$ directly, using $\eta^{\alpha\beta}\eta_{\alpha\beta} = 4$ in four spacetime dimensions, to verify $T^\mu{}_\mu = 0$.

2. **Dimension dependence.** Repeat the trace computation in general spacetime dimension $d$. Show that the coefficient of the trace term that gives a traceless tensor is $1/d$, and conclude that the electromagnetic tensor is traceless precisely *in four dimensions*. Explain what this has to do with the dimensional-analysis fact that Maxwell theory has no length scale in $d = 4$ (conformal invariance).

3. **Thermal radiation: the equation of state $p = \rho/3$.** A bath of thermal blackbody radiation has, by isotropy in the rest frame, a [[Def - Perfect Fluid|perfect-fluid]] energy-momentum tensor $T^{\mu\nu} = (\rho + p)U^\mu U^\nu - p\,\eta^{\mu\nu}$. Use tracelessness $T^\mu{}_\mu = 0$ together with the perfect-fluid form to derive the equation of state $\rho = 3p$, i.e. **$p = \rho/3$**, the relation that governs the radiation-dominated early universe and underlies the Stefan–Boltzmann law's pressure component.

4. **Casimir-effect anomaly preview.** Note that the *classical* trace vanishes but in the quantum theory $\langle T^\mu{}_\mu\rangle$ acquires a nonzero **trace anomaly** in the presence of boundaries or curvature — the renormalisation-induced breaking of conformal symmetry — and briefly describe in plain prose what this would imply for the classical equation of state derived in Part 3 (correction terms in cosmological perturbation theory, finite-temperature corrections to the Stefan–Boltzmann law).

**Recall:**

The exercise rests on the trace structure of the electromagnetic energy-momentum tensor and the perfect-fluid form.

![[Def - Energy-Momentum Tensor of the Electromagnetic Field#The Definition]]

A [[Def - Perfect Fluid|perfect fluid]] has energy-momentum tensor $T^{\mu\nu} = (\rho + p)U^\mu U^\nu - p\,\eta^{\mu\nu}$, with $\rho$ the proper energy density and $p$ the isotropic pressure. In the fluid's rest frame the tensor is $\mathrm{diag}(\rho, p, p, p)$, and its trace is $T^\mu{}_\mu = \rho - 3p$ (in mostly-minus, using $U\cdot U = 1$ and $\eta^\mu{}_\mu = 4$).

---

# Convergent Strategy

**Problem class.** A *prove-and-apply-a-structural-property* problem. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] for tracelessness: compute the trace directly, identify the dimension-dependent coefficient, and use it as a constraint when the field is in a continuous form.

**Assumption pattern.** Two ingredients: the *form* of $T^{\text{em}}$ (quadratic in $F$ with the $-\tfrac14\eta F^2$ trace term) and the *form* of the perfect-fluid tensor (with energy density $\rho$ and pressure $p$ playing symmetric roles in the matrix). Tracelessness is the bridge between them: it forces $p = \rho/3$.

**Theorem routing.** Part 1: direct trace, using $\eta^{\alpha\beta}\eta_{\alpha\beta} = 4$. Part 2: replace $4$ by $d$ and find the coefficient. Part 3: equate the photon-gas tensor (isotropic, perfect-fluid form) to a traceless tensor, get $\rho - 3p = 0$. Part 4: briefly describe the quantum anomaly.

**Key decision point.** The crux of Part 3 is recognising that a thermal photon gas is *macroscopically* a perfect fluid (isotropic stress, no preferred direction in the rest frame), so its $T^{\mu\nu}$ takes the perfect-fluid form *with no $F$-dependence anywhere* — yet it inherits tracelessness from being radiation. The mismatch between "looks like a fluid" and "has zero trace" is precisely what forces $\rho = 3p$.

---

# Legal Operations Used

1. **Exploit tracelessness of the electromagnetic tensor** (operation 6 from the topic page): $T^\mu{}_\mu = 0$ is the key constraint, used both as an internal consistency check and as a forcing condition on the equation of state.

2. **Build the fluid tensor from the four-velocity field** (operation 2): the photon gas has $T^{\mu\nu} = (\rho+p)U^\mu U^\nu - p\,\eta^{\mu\nu}$, with $\rho, p$ scalars characterising the gas.

3. **Take the trace and use it as a check or constraint**: in Part 1 a check (must vanish if the formula is right); in Part 3 a constraint (must vanish, forces $p = \rho/3$).

---

# Hints

> [!note]- Hint 1
> Trace: $\eta^{\alpha\beta}T^{\text{em}}_{\alpha\beta} = \varepsilon_0\eta^{\alpha\beta}F_{\mu\alpha}F^\mu{}_\beta - \tfrac{\varepsilon_0}{4}\eta^{\alpha\beta}\eta_{\alpha\beta}F^2$. First term: $\eta^{\alpha\beta}F_{\mu\alpha}F^\mu{}_\beta = F_\mu{}^\beta F^\mu{}_\beta = F^{\mu\beta}F_{\mu\beta} = F^2$. Second term: $\eta^{\alpha\beta}\eta_{\alpha\beta} = \delta^\alpha_\alpha = 4$. So $\eta^{\alpha\beta}T^{\text{em}}_{\alpha\beta} = \varepsilon_0 F^2 - \varepsilon_0 F^2 = 0$. Zero.

> [!note]- Hint 2
> In $d$ dimensions, $\eta^{\alpha\beta}\eta_{\alpha\beta} = d$. So if the trace term has coefficient $c$, the trace is $\varepsilon_0(1 - c\cdot d)F^2$, which vanishes when $c = 1/d$. For $d=4$, $c=\tfrac14$. The tensor with the wrong coefficient is *not traceless*, and the conformal-invariance reasoning fails. Maxwell theory in $d \ne 4$ does have a length scale (the coupling carries dimension) and is *not* conformally invariant; the photon there is "effectively massive" in scaling arguments.

> [!note]- Hint 3
> Perfect-fluid tensor in mostly-minus: $T^{\mu\nu} = (\rho + p)U^\mu U^\nu - p\,\eta^{\mu\nu}$. Trace: $T^\mu{}_\mu = (\rho + p)U\cdot U - p\cdot 4 = (\rho + p)\cdot 1 - 4p = \rho - 3p$. Setting this to zero (radiation is traceless): $\rho = 3p$, i.e. $\boxed{p = \rho/3}$. This is the equation of state of the early universe's photon bath, and equivalently $w := p/\rho = 1/3$.

> [!note]- Hint 4
> The classical $T^\mu{}_\mu = 0$ becomes $\langle T^\mu{}_\mu\rangle = \text{(curvature, boundary terms)}$ in the quantum theory — the **trace anomaly**. For free electromagnetism in flat space with no boundaries it remains zero; in the presence of Casimir-plate boundaries or in curved spacetime it acquires a calculable nonzero value proportional to dimensional combinations of the Riemann tensor (and ultimately the beta function in interacting theories). Physically: a corrective pressure term shifts the radiation equation of state slightly away from $p = \rho/3$, with measurable consequences in fine cosmological observables and in laboratory Casimir effects.

---

# Solution

Tracelessness $T^\mu{}_\mu = 0$ is verified directly by the $\tfrac14$ coefficient that makes $\varepsilon_0 F^2 - \tfrac{\varepsilon_0}{4}\cdot 4\cdot F^2 = 0$ in four dimensions. The coefficient generalises to $1/d$, traceless only in $d = 4$ — the dimension where Maxwell theory is conformally invariant. Combined with the perfect-fluid form of a thermal photon gas, tracelessness *forces* the equation of state $p = \rho/3$ — the relation governing radiation-dominated cosmology and the Stefan–Boltzmann pressure.

**Step 1: Direct trace computation.**

> [!note]- Derivation
> Contract $T^{\text{em}}_{\alpha\beta}$ with $\eta^{\alpha\beta}$:
> $$\eta^{\alpha\beta}T^{\text{em}}_{\alpha\beta} = \varepsilon_0\,\eta^{\alpha\beta}F_{\mu\alpha}F^\mu{}_\beta - \tfrac{\varepsilon_0}{4}\,\eta^{\alpha\beta}\eta_{\alpha\beta}\,F_{\mu\nu}F^{\mu\nu}.$$
> *First term.* $\eta^{\alpha\beta}F_{\mu\alpha}F^\mu{}_\beta = F_\mu{}^\beta F^\mu{}_\beta = F^{\mu\beta}F_{\mu\beta} =: F^2$ (the field invariant — the same scalar twice).
> *Second term.* $\eta^{\alpha\beta}\eta_{\alpha\beta} = \mathrm{tr}(\delta^\alpha_\beta) = 4$ in four spacetime dimensions, since $\delta^\alpha_\beta$ is the identity on a four-dimensional vector space and its trace is the dimension.
>
> Putting it together,
> $$T^\mu{}_\mu = \varepsilon_0 F^2 - \tfrac{\varepsilon_0}{4}\cdot 4\cdot F^2 = \varepsilon_0 F^2 - \varepsilon_0 F^2 = 0.$$
> The factor $4$ from $\eta^{\alpha\beta}\eta_{\alpha\beta}$ kills the $\tfrac14$ exactly. **The electromagnetic energy-momentum tensor is traceless.**

**Step 2: Dimension dependence.**

> [!note]- Derivation
> In $d$-dimensional spacetime, repeat the calculation with $\eta^{\alpha\beta}\eta_{\alpha\beta} = d$. If the trace term in $T^{\text{em}}$ has *general* coefficient $c$, $T^{\text{em}}_{\alpha\beta} = \varepsilon_0(F_{\mu\alpha}F^\mu{}_\beta - c\,\eta_{\alpha\beta}F^2)$, then
> $$T^\mu{}_\mu = \varepsilon_0 F^2 - c\,\varepsilon_0\cdot d\cdot F^2 = \varepsilon_0(1 - cd)F^2.$$
> This vanishes if and only if $c = 1/d$. In $d = 4$, $c = \tfrac14$ — the famous coefficient. In $d = 3$, $c = \tfrac13$; in $d = 2$, $c = \tfrac12$; and so on. The Maxwell action $-\tfrac{1}{4\mu_0}\int F^2\sqrt{-g}\,\mathrm d^dx$ continues to have this coefficient by convention, but the variational derivative produces $T^{\text{em}}$ with the trace term's coefficient becoming $1/d$ — so tracelessness *only* holds in $d = 4$.
>
> The dimensional-analysis reason: in $d = 4$, the Maxwell coupling $\mu_0$ (or $1/(\mu_0 c)$) is dimensionless in natural units, so the theory has *no intrinsic length scale*. A theory without a length scale is invariant under conformal rescalings $g_{\mu\nu}\to\Omega^2 g_{\mu\nu}$, and the Noether current of conformal transformations is the trace of $T$ — which must vanish for the symmetry to hold. In $d \ne 4$, dimensional analysis forces the coupling to carry dimension, breaking conformal invariance, and the trace acquires a nonzero classical value proportional to that dimensional coupling. Tracelessness of $T^{\text{em}}$ is thus *the special property of Maxwell theory in $d = 4$* — a structural fact about our universe.

**Step 3: The equation of state of radiation.**

> [!note]- Derivation
> A bath of thermal blackbody radiation (e.g. the cosmic microwave background, or the photon gas in the early universe) is macroscopically isotropic in its rest frame: no preferred direction, equal stress in all spatial directions. So its energy-momentum tensor takes the [[Def - Perfect Fluid|perfect-fluid]] form
> $$T^{\mu\nu}_{\text{rad}} = (\rho + p)\,U^\mu U^\nu - p\,\eta^{\mu\nu},$$
> with $\rho$ the proper energy density (energy per rest-frame volume) and $p$ the isotropic radiation pressure. In the rest frame $U = (1, \mathbf 0)$, and this is $\mathrm{diag}(\rho, p, p, p)$ — energy density on the time-time slot, equal pressure on each spatial diagonal.
>
> Compute the trace. Using $U\cdot U = 1$ (mostly-minus) and $\eta^\mu{}_\mu = 4$:
> $$T^\mu{}_\mu = \eta_{\mu\nu}T^{\mu\nu}_{\text{rad}} = (\rho + p)\,U_\mu U^\mu - p\,\eta_\mu{}^\mu = (\rho + p)\cdot 1 - 4p = \rho - 3p.$$
> Now, *radiation is traceless*: the photon gas, as a sum over individual photon contributions, inherits from each photon (via $T^{\mu\nu}_{\text{em}}$ for a single mode) the vanishing trace. So
> $$T^\mu{}_\mu = \rho - 3p = 0 \quad\Longrightarrow\quad \boxed{\;p = \tfrac{1}{3}\rho\;.}$$
> This is the **equation of state of radiation**. The "pressure" of a photon gas is one-third of its energy density — a stiffer equation of state than dust ($p = 0$) but softer than a "stiff fluid" ($p = \rho$). In FLRW cosmology this fixes radiation's dilution with the scale factor: combined with energy conservation, $\rho_{\text{rad}}\propto a^{-4}$ (one $a^{-3}$ from volume expansion, one $a^{-1}$ from redshift), versus matter $\rho_{\text{mat}}\propto a^{-3}$ and a cosmological constant $\rho_\Lambda = \text{const}$. The radiation-dominated era of the early universe is governed by exactly this $p = \rho/3$, and the Stefan–Boltzmann law's pressure component $p = aT^4/3$ (with $a$ the radiation constant) is a thermodynamic restatement of the same identity.

**Step 4: Trace anomaly preview.**

> [!note]- Derivation
> The classical $T^\mu{}_\mu = 0$ is broken by *quantum corrections* in the presence of either curvature or boundaries. Promoting the field to a quantum operator, the vacuum expectation value $\langle 0|T^\mu{}_\mu|0\rangle$ no longer vanishes:
> - In *curved spacetime*, $\langle T^\mu{}_\mu\rangle \propto \alpha\,(\text{Riemann tensor invariants})$ — the trace anomaly, computable by heat-kernel methods, equals a specific dimensional combination of $R^2$, $R_{\mu\nu}R^{\mu\nu}$, $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ with renormalisation-scheme coefficients.
> - In *Casimir geometries* (parallel conducting plates), $\langle T^\mu{}_\mu\rangle = 0$ in the bulk but the vacuum stress between the plates is nonzero and finite, giving the measurable **Casimir effect** — an attractive force between uncharged conductors due to the modified vacuum stress of confined photons.
>
> For Part 3's equation of state, the anomaly implies small corrections to $p = \rho/3$ at finite temperature and in curved geometries — the **finite-temperature trace anomaly** shifts the relation by terms $\sim\alpha T^4 R$ in cosmology, generally tiny but in principle observable in fine cosmological perturbation theory. The classical relation remains the dominant truth; the anomaly is a calculable correction. For the special-relativity course, the takeaway is that *exact* tracelessness is a *classical* statement specific to free Maxwell theory in four-dimensional Minkowski space, and quantum/gravitational corrections respect its spirit by being small and calculable, never overwhelming.

> [!note]- Complete formal solution
> The trace of $T^{\text{em}}_{\alpha\beta} = \varepsilon_0(F_{\mu\alpha}F^\mu{}_\beta - \tfrac14\eta_{\alpha\beta}F_{\mu\nu}F^{\mu\nu})$ is, in $d = 4$, $T^\mu{}_\mu = \varepsilon_0(F^2 - \tfrac14\cdot 4\cdot F^2) = 0$ — exactly traceless. In general dimension $d$, the trace-term coefficient that makes $T$ traceless is $1/d$, so tracelessness of Maxwell theory is the special-to-four-dimensions statement of conformal invariance (the theory has no intrinsic length scale only in $d=4$). For a thermal photon gas, isotropy forces the perfect-fluid form $T^{\mu\nu} = (\rho + p)U^\mu U^\nu - p\,\eta^{\mu\nu}$ with trace $T^\mu{}_\mu = \rho - 3p$; combining with tracelessness of radiation yields the **equation of state $p = \rho/3$**, governing FLRW radiation-dominated cosmology and the Stefan–Boltzmann pressure. Quantum corrections produce a calculable trace anomaly in curved or bounded geometries (the Casimir effect being the laboratory paradigm), introducing small corrections to the classical relation that respect its spirit. $\blacksquare$

---

# Key Takeaways

**Tracelessness of $T^{\text{em}}$ is the masslessness of the photon, the conformal invariance of Maxwell theory, and the equation of state of radiation — all the same fact.** The single algebraic identity $T^\mu{}_\mu = 0$ controls a remarkable diversity of physical phenomena because it expresses a single deep symmetry: the absence of any intrinsic length scale in four-dimensional Maxwell theory. *Masslessness* of the photon: a massive field would have a rest energy and hence a scale, breaking tracelessness. *Conformal invariance*: rescaling $g \to \Omega^2 g$ leaves the Maxwell action unchanged in $d = 4$, and the Noether current of dilatations is precisely the trace, which must vanish for the symmetry to hold. *Equation of state $p = \rho/3$*: when this same traceless tensor is averaged over a thermal bath of photons, the perfect-fluid form's trace $\rho - 3p$ must vanish, forcing the relation. Whenever you see one of these three statements, the other two are present implicitly, and recognising the unity collapses what looked like three separate facts into one structural feature.

**Dimensional dependence: tracelessness lives only in $d = 4$, and that is the dimension we inhabit.** The coefficient $\tfrac14$ of the trace term is not a numerical accident — it is $1/d$ with $d = 4$, the spacetime dimension. In $d = 3$ or $d = 5$ Maxwell theory the coefficient that makes $T$ traceless would be $\tfrac13$ or $\tfrac15$, and the dimensional analysis of the coupling tells us that the theory in those dimensions has an intrinsic length scale (the Maxwell coupling carries dimension), so it is not conformally invariant and acquires a nonzero classical trace. The fact that *we* live in $d = 4$ is what permits the photon to be massless, the radiation equation of state to be exactly $p = \rho/3$, and the conformal-symmetry methods of high-energy physics to apply. This is one of those subtle "the dimension of our spacetime is special" observations — like the fact that planetary orbits in $d = 3$ are conic sections (no other dimension supports stable bounded orbits in a $1/r$ potential), or that the Riemann tensor has nontrivial structure only when dimension exceeds 2. The trigger is any computation involving the trace of an electromagnetic stress tensor: assert tracelessness, use it as a hard constraint, but remember the constraint is *dimension-specific*.

**A traceless symmetric tensor *and* a perfect-fluid form together overdetermine the system, forcing the equation of state.** The general logic is the most reusable lesson of this exercise. When a system's energy-momentum tensor is constrained simultaneously by (i) a symmetry (here, conformal invariance giving $T^\mu{}_\mu = 0$) and (ii) a phenomenological form (here, perfect-fluid isotropy giving the $(\rho + p)U^\mu U^\nu - p\eta^{\mu\nu}$ structure), the two constraints together typically fix a relation that neither alone would impose — here the equation of state. The same pattern derives the equation of state of *any* conformal matter (relativistic gas of massless particles, ultrarelativistic limits of degenerate Fermi gases) as $p = \rho/3$, and analogous constraints from other symmetries (scale invariance with anomalous dimensions, supersymmetry) impose other equations of state. The reusable workflow: identify the symmetry constraint on $T$ (trace condition, conservation law, divergence-free condition), identify the phenomenological form ($(0,2)$ symmetric, perfect fluid, anisotropic with one axis…), impose both, and solve for the relations among the free parameters $\rho, p, \ldots$. This pattern is how one writes down cosmological equations of state from symmetry principles alone, before having any microscopic model.

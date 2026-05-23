---
type: definition
subject: general-relativity
prereqs:
  - "Def - Spacetime Manifold"
  - "Def - The Metric Tensor as Gravitational Potential"
  - "Def - Riemannian Volume Form"
tags: [physics, general-relativity, variational-principle, action]
---

# Notation

Spacetime $(M, g)$, signature $(+,-,-,-)$, geometrised units. The Lorentzian volume element is $\sqrt{-g}\, d^4x$ (note $g < 0$). The scalar curvature is $R = g^{\mu\nu} R_{\mu\nu}$. A variation of the metric is denoted $\delta g_{\mu\nu}$ or, equivalently in the inverse, $\delta g^{\mu\nu}$ (related by $\delta g_{\mu\nu} = -g_{\mu\rho} g_{\nu\sigma} \delta g^{\rho\sigma}$). Full notation registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Axiom Motivation

The desideratum is to identify the action functional whose Euler–Lagrange equations are the [[Def - The Einstein Field Equations|Einstein field equations]]. There are deep reasons to want such a formulation: (i) Lagrangian field theories have automatic conservation laws via Noether's theorem; (ii) symmetries of the action (diffeomorphism invariance) directly imply the structural identities (contracted Bianchi); (iii) the action provides a starting point for **canonical quantisation** (Wheeler–DeWitt equation) and **path-integral quantisation** ($Z = \int \mathcal{D}g\, e^{iS}$); (iv) modifications of gravity (with cosmological constant, with extra fields, with higher-curvature terms) are most cleanly formulated as modifications of the action.

David Hilbert, working in Göttingen in 1915 in parallel with Einstein in Berlin, found the answer essentially simultaneously: the **Hilbert action** is
$$S_\text{grav}[g] = \frac{1}{16\pi G} \int_M R\, \sqrt{-g}\, d^4x.$$
The integrand $R\sqrt{-g}$ is the simplest scalar density (a scalar times the volume element) built from the metric and its derivatives. The variation with respect to $g^{\mu\nu}$ yields the Einstein tensor times $\sqrt{-g}$, and demanding $\delta S/\delta g^{\mu\nu} = 0$ gives the vacuum Einstein equations $G_{\mu\nu} = 0$. Adding a matter action $S_\text{matter}$ — with the convention that $T_{\mu\nu} = -(2/\sqrt{-g}) \delta S_\text{matter}/\delta g^{\mu\nu}$ — gives the full Einstein equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$.

**Why is $R\sqrt{-g}$ the right Lagrangian?** Several structural reasons:

1. *Scalar density*: $R$ is a scalar (a coordinate-invariant function on $M$), and $\sqrt{-g}\, d^4x$ is the unique coordinate-invariant volume measure (transforming with a Jacobian factor that exactly cancels the inverse Jacobian from $d^4x$). So $\int R\sqrt{-g}\, d^4x$ is a coordinate-invariant number, a well-defined action.

2. *Simplest non-trivial choice*: The only simpler scalar is a constant (giving just $\int \Lambda \sqrt{-g}\, d^4x$, the cosmological-constant term with $\Lambda = $ const). The next-simplest is $R$ itself. Higher-curvature scalars ($R^2$, $R_{\mu\nu} R^{\mu\nu}$, $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$) give higher-order field equations with generic instabilities (Ostrogradsky's theorem).

3. *Second-order field equations*: Variation of $R$ gives $R_{\mu\nu}\delta g^{\mu\nu} + g^{\mu\nu}\delta R_{\mu\nu}$; the second piece is a total divergence (Palatini identity), which would normally be discarded. After dropping the boundary term, the variation gives terms involving up to second derivatives of $g$ — and *only* second derivatives, despite $R$ containing second derivatives in its definition. The miraculous cancellation that achieves this is what makes $R$ special.

4. *Diffeomorphism invariance*: $\int R\sqrt{-g}\, d^4x$ is manifestly invariant under coordinate changes (both $R$ and $\sqrt{-g}\, d^4x$ are scalars/scalar densities). This forces the field equations to be covariant tensor equations, and via Noether's theorem implies the contracted Bianchi identity automatically.

**Why $\sqrt{-g}$ (not $\sqrt{|g|}$ or $\sqrt{g}$)?** Because in Lorentzian signature, $\det g < 0$ (one positive eigenvalue, three negative), so $\sqrt{-g}$ is real and positive. The volume element $\sqrt{-g}\, d^4x$ is positive and is what integrates Lorentz-invariant tensor densities. The factor $\sqrt{-g}$ is essential: without it, the integral would change under coordinate changes by the Jacobian factor.

**The factor $1/(16\pi G)$.** This is fixed by demanding that the resulting Einstein equations have the right coupling $8\pi G$ to the stress-energy tensor (see Newtonian limit). The "16" comes from the convention that the stress-energy tensor be defined as $T_{\mu\nu} = -(2/\sqrt{-g}) \delta S_\text{matter}/\delta g^{\mu\nu}$, with the factor of 2 yielding the symmetric tensor and the minus sign agreeing with energy density being positive.

**The matter action.** The total action is $S = S_\text{grav} + S_\text{matter}$, where $S_\text{matter}[g, \psi] = \int \mathcal{L}_\text{matter}(\psi, \nabla\psi, g)\sqrt{-g}\, d^4x$ is the action of all non-gravitational fields (denoted collectively $\psi$). The matter Lagrangian is constructed by the **minimal coupling prescription** (forced by the strong equivalence principle): take the special-relativistic matter Lagrangian, replace $\eta_{\mu\nu}$ by $g_{\mu\nu}$, and replace $\partial_\mu$ by $\nabla_\mu$ (covariant derivative). This is what makes the matter action diffeomorphism-invariant, which in turn (by Noether) gives $\nabla^\mu T_{\mu\nu} = 0$ — local energy-momentum conservation.

**Per-component motivation:**

(a) *Why include the matter action?* Otherwise, the variational principle yields only vacuum equations ($G_{\mu\nu} = 0$). The matter sources gravity, so its presence on the RHS of the field equation requires it to be in the action.

(b) *Why minimal coupling?* The **strong equivalence principle** (universal coupling of matter to gravity) forbids additional couplings of matter to curvature (like a direct $R\phi^2$ term). Such couplings would violate the SEP and are ruled out experimentally.

(c) *Why not non-minimal couplings?* They exist in **scalar-tensor theories** (Brans–Dicke, $f(R)$ gravity) — the action then contains terms like $f(R)$ instead of $R$, or scalar fields coupled directly to $R$. These are testable alternatives to GR but are constrained by observations to be small perturbations from minimal coupling.

(d) *Why not higher-derivative gravity?* Adding $R^2$, $R_{\mu\nu} R^{\mu\nu}$, etc. to the action gives fourth-order field equations, which have Ostrogradsky ghosts (unstable degrees of freedom). Such terms appear as higher-loop corrections in effective field theory but cannot be the leading-order theory.

---

# The Definition

> **Definition (Hilbert action, Einstein–Hilbert action).** For a four-dimensional spacetime $(M, g)$ (possibly with boundary $\partial M$), the **Hilbert action** for the gravitational field is
> $$S_\text{grav}[g] = \frac{1}{16\pi G} \int_M R\, \sqrt{-g}\, d^4x.$$
> Here $G$ is Newton's constant, $R$ is the scalar curvature of the Levi-Civita connection of $g$, and $\sqrt{-g}\, d^4x$ is the Lorentzian volume element. In geometrised units ($G = 1$), the prefactor is $1/(16\pi)$.
>
> The total action of GR coupled to matter (denoted collectively $\psi$) is
> $$S[g, \psi] = S_\text{grav}[g] + S_\text{matter}[g, \psi],$$
> where the **matter stress-energy tensor** is defined via the variational formula
> $$T_{\mu\nu} = -\frac{2}{\sqrt{-g}} \frac{\delta S_\text{matter}}{\delta g^{\mu\nu}}.$$
>
> **With cosmological constant** $\Lambda$:
> $$S_\text{grav}^\Lambda[g] = \frac{1}{16\pi G} \int_M (R - 2\Lambda)\, \sqrt{-g}\, d^4x.$$
>
> **Boundary term (Gibbons–Hawking–York):** For a spacetime with boundary $\partial M$, the action $S_\text{grav}$ as defined above is not stationary under variations $\delta g$ with $\delta g|_{\partial M} = 0$ (the boundary variations of derivatives of $g$ do not vanish even when the boundary values do). The full action is
> $$S_\text{grav}^\text{full}[g] = \frac{1}{16\pi G}\int_M R\, \sqrt{-g}\, d^4x + \frac{1}{8\pi G}\int_{\partial M} K\, \sqrt{|h|}\, d^3y,$$
> where $K$ is the trace of the extrinsic curvature of $\partial M$ and $h$ is the induced metric on $\partial M$. The boundary term is the **Gibbons–Hawking–York term**, essential for treating spacetimes with boundary or for evaluating the action numerically.

The action is a functional on the space of Lorentzian metrics on $M$; varying it with respect to $g$ yields the Einstein field equations as Euler–Lagrange equations (see [[Thm - Hilbert's Variational Principle Yields Einstein Equations]]).

---

# Categorical / Structural Definition

The Hilbert action is the **simplest diffeomorphism-invariant action functional** on the configuration space of Lorentzian metrics on $M$, in the sense of effective field theory: it is the leading term in an expansion in powers of curvature,
$$S_\text{grav} = \frac{1}{16\pi G}\int (R - 2\Lambda + c_1 R^2 + c_2 R_{\mu\nu}R^{\mu\nu} + c_3 R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} + \ldots)\sqrt{-g}\, d^4x,$$
with the cosmological constant term being dimension 0, the $R$ term being dimension 2, and higher-curvature terms being dimension 4 and above (in mass dimension). The $1/(16\pi G)$ in front of $R$ is the Newton-constant-determined coupling, and the higher-curvature coefficients $c_i$ are dimensionless coupling constants suppressed by powers of the Planck scale.

In **fibre bundle** language: the metric $g$ is a section of the bundle of Lorentzian quadratic forms over $M$; the Hilbert action is a smooth functional on this section space, gauge-invariant under the action of the diffeomorphism group $\mathrm{Diff}(M)$. The Einstein field equations are the gauge-fixed Euler–Lagrange equations, and the **constraints** of canonical GR (Hamiltonian and momentum constraints) are the generators of the gauge group.

In the **path-integral approach** to quantum gravity, the partition function is formally
$$Z = \int \mathcal{D}g\, e^{iS_\text{grav}[g]/\hbar},$$
with the integral over Lorentzian metrics modulo diffeomorphisms. This integral is ill-defined in 4D (the theory is non-renormalisable), motivating the search for a more fundamental theory (**string theory**, **loop quantum gravity**, **asymptotic safety**).

---

# Relate to Other Fields / Compression

**True name:** The Hilbert action is *the simplest non-trivial scalar density built from a Lorentzian metric and its derivatives — namely $R\sqrt{-g}$, the scalar curvature times the volume element*. The Euler–Lagrange equations of $\int R\sqrt{-g}\, d^4x$ are exactly the vacuum Einstein equations $R_{\mu\nu} = 0$. Adding matter and demanding diffeomorphism invariance gives the full Einstein equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$, with $T_{\mu\nu}$ defined variationally from the matter action.

The Hilbert action is to general relativity what the **Yang-Mills action** $S_{YM} = -\frac{1}{4}\int F_{\mu\nu}^a F^{a\mu\nu} \sqrt{-g}\, d^4x$ is to gauge theory: the universal Lagrangian whose Euler–Lagrange equations are the field equations of the theory. The structural similarity is deep: both are integrals of curvature invariants of a connection, both have automatic gauge invariance (diffeomorphism for gravity, structure-group gauge for Yang–Mills), and both produce conserved currents via Noether (stress-energy for gravity, color current for Yang–Mills).

The key *difference* is order: Yang–Mills is *quadratic* in the field strength, while Hilbert is *linear* in the scalar curvature. This makes gravity inherently different from gauge theory — the linearity allows tools (variational principles, conformal techniques) not directly available in Yang–Mills, but also makes the theory non-renormalisable (the absence of a quadratic-curvature kinetic term is unusual). The deep reason for the linearity is that gravity has an extra structure (the tetrad / soldering form), which Yang–Mills lacks.

---

# Examples / Corollaries

**Is an instance — Einstein–Hilbert action of GR.** $S = \frac{1}{16\pi G}\int R\sqrt{-g}\, d^4x + S_\text{matter}$. Varying with respect to $g^{\mu\nu}$ yields the Einstein equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$. The canonical example.

**Is an instance — Einstein–Hilbert with cosmological constant.** $S = \frac{1}{16\pi G}\int(R - 2\Lambda)\sqrt{-g}\, d^4x + S_\text{matter}$. Yields $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$.

**Is an instance — Einstein–Maxwell action.** $S = \frac{1}{16\pi G}\int R\sqrt{-g}\, d^4x - \frac{1}{16\pi}\int F_{\mu\nu} F^{\mu\nu}\sqrt{-g}\, d^4x$. Varying with respect to $g$ gives Einstein's equations with the EM stress-energy tensor as source; varying with respect to $A_\mu$ gives Maxwell's equations $\nabla_\mu F^{\mu\nu} = 0$. The joint solution (spherically symmetric, with charge) is the Reissner–Nordström metric.

**Is an instance — minimally coupled scalar field action.** $S = \frac{1}{16\pi G}\int R\sqrt{-g}\, d^4x + \int [\frac{1}{2} g^{\mu\nu} \partial_\mu\phi \partial_\nu \phi - V(\phi)]\sqrt{-g}\, d^4x$. Varying with respect to $g$ gives the Einstein equations with scalar-field stress-energy; varying with respect to $\phi$ gives the Klein–Gordon equation $\Box\phi + V'(\phi) = 0$.

**Is NOT an instance — non-covariant action.** $\int R\, d^4x$ (without the $\sqrt{-g}$ factor) is not coordinate-invariant; varying it gives non-tensorial equations. The factor $\sqrt{-g}$ is essential.

**Is NOT an instance — $\int R^2\sqrt{-g}\, d^4x$ alone.** Pure $R^2$ gravity gives fourth-order field equations (instead of second-order), with Ostrogradsky ghosts. Not viable as a leading-order gravity theory, though it appears in **Starobinsky inflation** as a special $f(R) = R + R^2/(6m^2)$ model that is equivalent to GR plus a massive scalar (the **scalaron**).

**Is NOT a viable action — pure higher-curvature term.** $\int R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}\sqrt{-g}\, d^4x$ alone — wrong propagator structure, ghosts. Such terms appear as small corrections in effective field theory but cannot be the leading dynamics.

**Corollary — vacuum Einstein equations.** Setting $S_\text{matter} = 0$ in the variational principle, $\delta S_\text{grav}/\delta g^{\mu\nu} = 0$ gives $G_{\mu\nu} = 0$, equivalent to $R_{\mu\nu} = 0$ (vacuum Einstein equations).

**Corollary — Noether's theorem for diffeomorphisms.** The diffeomorphism invariance of $S_\text{matter}$ implies $\nabla^\mu T_{\mu\nu} = 0$ — local stress-energy conservation, derived as a Noether identity rather than postulated.

**Corollary — Lovelock's theorem.** Among all diffeomorphism-invariant actions on a 4-dimensional Lorentzian manifold yielding second-order field equations, the unique combination is $\int(R - 2\Lambda)\sqrt{-g}\, d^4x$ — Einstein–Hilbert plus cosmological constant. Any other choice gives either higher-order equations or non-second-order ones.

**Corollary — boundary term necessity.** For a spacetime with boundary, the variation of $\int R \sqrt{-g}\, d^4x$ produces non-vanishing boundary terms (from the derivative of the metric variation in the boundary direction) even when $\delta g|_{\partial M} = 0$. The Gibbons–Hawking–York term cancels these, making the variational principle well-posed for boundary-value problems.

**Calibration check.** (i) Dimensional analysis: $[R] = \text{length}^{-2}$, $[\sqrt{-g}\, d^4x] = \text{length}^4$, so $[R\sqrt{-g}\, d^4x] = \text{length}^2$; $[1/G] = \text{length}^{-1} \cdot \text{mass}$ (in natural units), so $[S/G] = \text{length}^2 \cdot \text{mass} \cdot \text{length}^{-1} = \text{mass} \cdot \text{length} = \text{action}$ — dimensions of $\hbar$, consistent. (ii) Verify that the integrand is a scalar density: $R$ is a scalar, $\sqrt{-g}$ is a density of weight 1, so $R\sqrt{-g}$ is a density of weight 1, and integrating it over $d^4x$ gives a coordinate-invariant number. (iii) Check that varying the action with respect to $g^{\mu\nu}$ gives the right combination $R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$ (this is the content of [[Thm - Hilbert's Variational Principle Yields Einstein Equations]]).

---

# Unlocked by This

> [!tip] Modified Gravity Theories *(from Beyond-Einstein Gravity)*
> Replacing $R$ in the Hilbert action by an arbitrary function $f(R)$ gives **$f(R)$ gravity**, equivalent (after a field redefinition) to GR plus a scalar field with potential determined by $f$. Examples: **Starobinsky inflation** with $f = R + R^2/(6m^2)$; **$1/R$ gravity** as an attempted dark-energy model (ruled out by solar-system tests). More general modifications: scalar-tensor theories (Brans–Dicke), tensor-vector-scalar (TeVeS), Horndeski theories — all are formulated as modifications of the Hilbert action.

> [!tip] Path Integral Quantum Gravity *(from Quantum Gravity)*
> The path integral $Z = \int \mathcal{D}g\, e^{iS_\text{grav}[g]/\hbar}$ is the formal definition of quantum gravity in the Lagrangian framework. In 4D it is non-renormalisable, but **Euclidean quantum gravity** (Wick-rotated, $iS \to -S_E$ with Euclidean action $S_E$) gives well-defined results for some quantities — most famously the **Bekenstein–Hawking entropy** of black holes via on-shell evaluation of the Euclidean action.

> [!tip] Canonical Quantisation and the Wheeler–DeWitt Equation *(from Quantum Gravity)*
> The Hamiltonian decomposition of the Hilbert action (ADM) gives the **Hamiltonian** as a sum of constraints — the **Hamiltonian constraint** $\mathcal{H} = 0$ and the **momentum constraints** $\mathcal{H}_i = 0$. Quantising as $\hat{\mathcal{H}}\Psi = 0$ on a wavefunctional $\Psi[h_{ij}]$ over the configuration space of spatial metrics gives the **Wheeler–DeWitt equation** — the central equation of canonical quantum gravity. The interpretation (where does time come from?) is the **problem of time** in quantum gravity.

> [!tip] Gauge-Gravity Duality / AdS/CFT *(from String Theory)*
> The on-shell value of the Hilbert action (with cosmological constant) for asymptotically AdS spacetimes computes correlation functions of the boundary conformal field theory, via the **AdS/CFT dictionary**. Specifically, the boundary metric is dual to the stress-energy tensor of the CFT, and the gravity action evaluated on bulk solutions computes generating functionals on the CFT side. This is the bridge between gravity and quantum field theory in the holographic framework.

> [!tip] Asymptotic Safety in Quantum Gravity *(from Quantum Gravity Approaches)*
> **Weinberg's asymptotic safety** programme conjectures that quantum gravity, viewed as a non-perturbative quantum field theory on the space of metrics, has a non-trivial UV fixed point making the theory finite at all energies. The Hilbert action is the IR (large-distance) starting point, and the renormalisation-group flow generates higher-curvature corrections. Active research using **functional renormalisation group** methods provides evidence for the existence of such a fixed point, though full quantitative control is elusive.

> [!tip] Gibbons–Hawking–York Boundary Term and Black Hole Thermodynamics *(from Black Hole Physics)*
> Evaluating the Hilbert action (with GHY boundary term) on Euclidean Schwarzschild gives a finite result: $S_E = \beta M/2$ where $\beta = 1/T_H$ is the inverse Hawking temperature. This is identified with the free energy of the black hole, giving the **Bekenstein–Hawking entropy** $S_\text{BH} = A/(4 G\hbar)$ — a direct calculation via the action principle. The boundary term is *essential* for this result; without it, the action is divergent.

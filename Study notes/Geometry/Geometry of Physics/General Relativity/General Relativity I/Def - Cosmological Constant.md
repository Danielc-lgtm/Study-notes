---
type: definition
subject: general-relativity
prereqs:
  - "Def - The Einstein Field Equations"
  - "Def - Einstein Tensor"
  - "Def - Spacetime Manifold"
tags: [physics, general-relativity, cosmology, dark-energy]
---

# Notation

Spacetime $(M, g)$, signature $(+,-,-,-)$, geometrised units. The cosmological constant is $\Lambda$, with units of inverse length-squared (or, equivalently, energy per unit volume divided by Planck energy). The modified Einstein equations are $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$. Full notation registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Axiom Motivation

The desideratum is to identify the most general consistent modification of the [[Def - The Einstein Field Equations|Einstein field equations]] that preserves all the structural requirements (covariant, symmetric, divergence-free, built from $g$ and at most second derivatives). The answer, by **Lovelock's theorem**, is: add a multiple of the metric, $\Lambda g_{\mu\nu}$. This is the **cosmological constant** term, and it is the unique additional freedom in the gravitational sector.

**Why $\Lambda g_{\mu\nu}$ specifically?** The covariant divergence of the metric vanishes identically ($\nabla_\mu g_{\nu\rho} = 0$, **metric compatibility** of the Levi-Civita connection), so $\nabla^\mu(\Lambda g_{\mu\nu}) = 0$ automatically — the addition does not spoil the divergence-freeness of the LHS of the field equations. So $G_{\mu\nu} + \Lambda g_{\mu\nu}$ remains symmetric and divergence-free, exactly as $G_{\mu\nu}$ alone is. By Lovelock's theorem this is the *only* such addition in 4D (modulo higher-derivative terms, which introduce ghosts).

**Why call it a "constant"?** $\Lambda$ must be a scalar field, but the requirement that the LHS be built from $g$ and derivatives at most to second order, with no additional fields, forces $\Lambda$ to be a *constant* (since a non-constant scalar field would have to be sourced by something, requiring an additional equation of motion). So in pure gravity + $\Lambda$, $\Lambda$ is a fixed parameter, like Newton's $G$ — a fundamental constant of nature.

**The physical content of $\Lambda$.** Moving $\Lambda g_{\mu\nu}$ to the RHS gives
$$G_{\mu\nu} = 8\pi G\, T_{\mu\nu}^\text{total}, \quad T_{\mu\nu}^\text{total} = T_{\mu\nu} - \frac{\Lambda}{8\pi G} g_{\mu\nu}.$$
So the cosmological constant is equivalent to a contribution to the stress-energy tensor of the form $T^\Lambda_{\mu\nu} = -\rho_\Lambda g_{\mu\nu}$ with constant energy density $\rho_\Lambda = \Lambda/(8\pi G)$. This is a **perfect fluid with equation of state** $p = -\rho$ (using $T^\Lambda_{\mu\nu} = -\rho_\Lambda g_{\mu\nu}$ in signature $+---$ gives $T^{00} = \rho_\Lambda$ and $T^{ii} = -\rho_\Lambda$ for $i = 1, 2, 3$, hence $p = -\rho$). This is a peculiar fluid: positive energy density, negative pressure. In the Einstein equations it acts as a *repulsive* gravitating source, causing accelerated expansion of the universe — exactly the **dark energy** observed since the late 1990s.

**Why introduce $\Lambda$ at all?** Three historical motivations:

(i) *Einstein's 1917 motivation*: He wanted a static universe (Hubble's expansion was not yet known), and the matter-only Einstein equations admit no static cosmological solution (gravity would cause everything to collapse). Adding $\Lambda > 0$ provides a repulsive term that can balance the attraction, giving a static (though unstable) universe — the **Einstein static universe**. After Hubble (1929) discovered the universe is expanding, Einstein famously called $\Lambda$ his "biggest blunder" and removed it.

(ii) *Observational re-introduction (1998–1999)*: Type Ia supernova observations by the **Supernova Cosmology Project** (Perlmutter et al.) and the **High-Z Supernova Search Team** (Riess et al.) showed that the expansion of the universe is *accelerating*. This requires a repulsive contribution to gravity at cosmological scales — exactly what a positive $\Lambda$ provides. The value $\Lambda \approx 10^{-52}\,\mathrm{m}^{-2}$ fits all cosmological observations (CMB, BAO, supernovae, large-scale structure) — collectively the **standard model of cosmology** ($\Lambda$CDM).

(iii) *Quantum field theory*: vacuum fluctuations of quantum fields contribute an effective $\Lambda$ to the field equations. Naively, this contribution is of order the cutoff scale to the fourth power (Planck scale, giving $\rho_\Lambda \sim 10^{72}\,\mathrm{GeV}^4$); observed is $\rho_\Lambda \sim 10^{-47}\,\mathrm{GeV}^4$ — a discrepancy of $\sim 120$ orders of magnitude, the **cosmological constant problem**.

**Failure analysis (what if $\Lambda$ is wrong sign, wrong size, or absent?):**

(a) *$\Lambda = 0$*: the prediction is decelerating expansion (from gravitating matter). Observations rule this out — the universe is accelerating. Either $\Lambda > 0$ or some other dynamical "dark energy" component is required.

(b) *$\Lambda < 0$*: predicts a universe that eventually re-collapses (the negative $\Lambda$ adds to gravitational attraction at large scales). Also predicts **anti-de Sitter spacetime** as the vacuum, which has closed timelike curves and other pathologies. Not observed.

(c) *$\Lambda$ much larger than observed*: would cause faster acceleration than observed, with the universe expanding so fast that no structures could form. Observed value is anthropically just-right, leading to **anthropic arguments** (only universes with small $\Lambda$ permit life; we observe small $\Lambda$ because we are in such a universe).

(d) *$\Lambda$ as a dynamical scalar* (**quintessence**): models where $\Lambda$ is replaced by a slowly-evolving scalar field with potential $V(\phi)$, allowing the equation of state to vary slightly from $-1$. Observationally distinguishable in principle from a constant $\Lambda$ via the equation-of-state parameter $w(z)$; current data is consistent with $w = -1$ (constant $\Lambda$) to within a few percent.

---

# The Definition

> **Definition (Cosmological constant).** The **cosmological constant** $\Lambda$ is a constant parameter in the Einstein field equations:
> $$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\, T_{\mu\nu}.$$
> Equivalently, the Hilbert action with cosmological constant is
> $$S_\text{grav} = \frac{1}{16\pi G}\int_M (R - 2\Lambda)\, \sqrt{-g}\, d^4x.$$
> Varying with respect to $g^{\mu\nu}$ yields $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\, T_{\mu\nu}$ (the factor $-2\Lambda$ in the action gives $+\Lambda g_{\mu\nu}$ in the equations because of the metric variation rules).

**Equivalent reinterpretations:**

- **As an effective vacuum stress-energy:** moving $\Lambda g_{\mu\nu}$ to the RHS,
  $$G_{\mu\nu} = 8\pi G(T_{\mu\nu} + T_{\mu\nu}^\Lambda), \quad T_{\mu\nu}^\Lambda = -\frac{\Lambda}{8\pi G} g_{\mu\nu},$$
  with constant vacuum energy density $\rho_\Lambda = \Lambda/(8\pi G)$ and pressure $p_\Lambda = -\rho_\Lambda$ (equation of state $w = -1$).
- **As a curvature scale:** $\Lambda$ has units of inverse length-squared; $|\Lambda|^{-1/2}$ defines a length scale (the **de Sitter radius** $L = \sqrt{3/\Lambda}$ for $\Lambda > 0$). Beyond this scale, the cosmological constant dominates gravity.

**Sign conventions:** $\Lambda > 0$ gives **de Sitter spacetime** (the maximally symmetric vacuum), with accelerated expansion. $\Lambda < 0$ gives **anti-de Sitter spacetime**, with closed timelike curves in its maximal form. $\Lambda = 0$ gives **Minkowski spacetime** as the maximally symmetric vacuum.

---

# Categorical / Structural Definition

The cosmological constant is the unique zeroth-order term in an expansion of the gravitational action in powers of curvature: $S_\text{grav} = \frac{1}{16\pi G}\int(R - 2\Lambda + \alpha R^2 + \beta R_{\mu\nu}R^{\mu\nu} + \ldots) \sqrt{-g}\, d^4x$. The first term ($-2\Lambda$) is [[Def - Dimension|dimension]]-zero in curvature, the $R$ term is dimension-2, and higher-curvature terms are dimension-4 and above. From the effective-field-theory standpoint, $\Lambda$ is the leading-order term, $R$ the next-to-leading, and higher curvatures are corrections.

By **Lovelock's theorem**, the variations of all these terms with respect to $g^{\mu\nu}$ give symmetric divergence-free tensors built from $g$ and its derivatives. In 4D, the linearly-second-order terms reduce to $G_{\mu\nu}$ and $g_{\mu\nu}$ — yielding the Einstein equations with cosmological constant.

In the **Hamiltonian formulation** of GR, $\Lambda$ enters as a constant contribution to the Hamiltonian constraint, shifting the constraint surface by a constant amount. In the **path-integral quantisation**, it enters as an exponent $\exp(i\Lambda V/(8\pi G))$ where $V$ is the spacetime volume — a factor highly sensitive to the total volume of the universe.

---

# Relate to Other Fields / Compression

**True name:** The cosmological constant is *a constant vacuum energy density that gravitates with negative pressure ($w = -1$)*. Equivalently, it is the unique consistent modification of GR by a constant in the action, and the unique constant divergence-free contribution to the field equations. Operationally, it is what makes the universe accelerate.

The cosmological constant connects three otherwise-separate areas of physics:
- **General relativity / classical**: the cosmological term in Einstein's equations.
- **Cosmology / observational**: dark energy, accelerated expansion, supernova surveys.
- **Quantum field theory / theoretical**: vacuum energy density, zero-point fluctuations of quantum fields.

The structural identification of these three is correct (the same $\Lambda$ appears in all), but the quantitative disagreement (120 orders of magnitude between QFT and observation) is the **cosmological constant problem** — one of the deepest unsolved problems in physics.

In **de Sitter cosmology**, the cosmological constant is the only nontrivial parameter. The de Sitter spacetime is the maximally symmetric solution of $G_{\mu\nu} + \Lambda g_{\mu\nu} = 0$, has 10 Killing vectors (the de Sitter group $SO(1, 4)$), and has the same symmetry algebra as the Poincaré group of Minkowski space, except with a positive curvature scale.

---

# Examples / Corollaries

**Is an instance — Einstein's static universe.** Einstein's 1917 model: a 3-sphere $S^3$ of radius $R_E$ filled with dust, with $\Lambda$ tuned to exactly balance gravitational attraction. Solving $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi T_{\mu\nu}$ for static dust gives $\Lambda = 4\pi G \rho$, $R_E = (4\pi G \rho)^{-1/2}$. Unstable — any perturbation causes either collapse or expansion. Abandoned after Hubble's discovery of expansion (1929).

**Is an instance — de Sitter spacetime.** Vacuum solution of $G_{\mu\nu} + \Lambda g_{\mu\nu} = 0$ with $\Lambda > 0$. Topology $\mathbb{R} \times S^3$; in flat slicing $ds^2 = dt^2 - e^{2Ht} d\vec x^2$ with Hubble rate $H = \sqrt{\Lambda/3}$. Models the inflationary epoch of the early universe and (with very different $H$) the late-time accelerated expansion.

**Is an instance — anti-de Sitter spacetime.** Vacuum solution with $\Lambda < 0$. Has a timelike boundary at conformal infinity, used as the gravitational dual in the **AdS/CFT correspondence**. Negative spatial curvature, closed timelike curves in the maximal covering.

**Is an instance — $\Lambda$CDM cosmology.** The current best-fit cosmological model: flat spatial geometry, $\Omega_\Lambda \approx 0.69$ (dark energy fraction), $\Omega_m \approx 0.31$ (matter, including dark matter), Hubble constant $H_0 \approx 67$–$73\,\mathrm{km/s/Mpc}$ (discrepancy between local and CMB measurements is the **Hubble tension**). Cosmological constant value: $\Lambda \approx 1.1 \times 10^{-52}\,\mathrm{m}^{-2}$.

**Is NOT a cosmological constant — a non-constant scalar field.** A dynamical scalar field $\phi(x)$ with potential $V(\phi)$ can mimic a cosmological constant (as long as the kinetic energy is small compared to $V$) but is not strictly a cosmological constant. Such **quintessence** fields are alternative explanations of dark energy, distinguishable in principle from a true $\Lambda$ via time-variation of the equation-of-state parameter $w(z)$.

**Is NOT consistent with current data — $\Lambda$ much different from observed.** The observed value is robust (multiple independent cosmological probes agree). Theoretical "natural" values from QFT are $10^{120}$ times larger — the cosmological constant problem. The "correct" value seems to require either a cancellation mechanism (supersymmetric?) or anthropic explanation.

**Corollary — vacuum energy.** A positive $\Lambda$ corresponds to a positive vacuum energy density $\rho_\Lambda = \Lambda/(8\pi G) > 0$. The vacuum has weight — it gravitates. This is a remarkable physical implication of GR: even the empty vacuum, in the absence of matter, is gravitationally active if $\Lambda \neq 0$.

**Corollary — accelerated expansion.** The Friedmann equation with $\Lambda$ is $H^2 = (8\pi G/3) \rho - K/a^2 + \Lambda/3$, and the acceleration equation is $\ddot a/a = -(4\pi G/3)(\rho + 3p) + \Lambda/3$. A positive $\Lambda$ drives acceleration; with no matter, $a \propto e^{Ht}$ exponential expansion (de Sitter).

**Corollary — modifies black hole solutions.** Schwarzschild–de Sitter (with $\Lambda > 0$): $ds^2 = (1 - 2M/r - \Lambda r^2/3) dt^2 - (\ldots)^{-1} dr^2 - r^2 d\Omega^2$. Has both an event horizon (black hole) and a **cosmological horizon** at large $r$. The horizons coincide at the **Nariai limit** $\Lambda M^2 = 1/9$ — the largest black hole in a de Sitter universe.

**Calibration check.** (i) Compute the de Sitter Hubble rate $H = \sqrt{\Lambda/3}$ for the observed value $\Lambda \approx 10^{-52}\,\mathrm{m}^{-2}$: $H \approx 5.8 \times 10^{-27}\,\mathrm{m}^{-1} \sim 67\,\mathrm{km/s/Mpc}$ — matches observed Hubble rate (since we are dark-energy dominated). (ii) Verify dimensional consistency: $[\Lambda] = \text{length}^{-2}$, $[G_{\mu\nu}] = \text{length}^{-2}$, $[g_{\mu\nu}] = $ dimensionless, $[\Lambda g_{\mu\nu}] = \text{length}^{-2}$. (iii) Compute $\rho_\Lambda$ for the observed $\Lambda$: $\rho_\Lambda = \Lambda/(8\pi G) \approx 6 \times 10^{-27}\,\mathrm{kg/m}^3$ — about 6 hydrogen atoms per cubic metre, the "dark energy" density.

---

# Unlocked by This

> [!tip] Dark Energy and the Accelerating Universe *(from Observational Cosmology)*
> Type Ia supernova observations (Perlmutter, Schmidt, Riess — Nobel Prize 2011) and CMB observations (WMAP, Planck) jointly establish that the universe is accelerating in its expansion, requiring a positive vacuum energy density — the **dark energy**. The standard model assumes a constant $\Lambda$; observational programs (DESI, Euclid, LSST) probe whether the dark energy might be dynamical (varying $w(z)$). The equation of state is currently consistent with $w = -1$ to within a few percent.

> [!tip] de Sitter Spacetime and Inflation *(from Early-Universe Cosmology)*
> The very early universe ($t \sim 10^{-36}$ s after the Big Bang) is believed to have undergone a brief period of **cosmic inflation** — exponential expansion driven by a large (then-decaying) effective cosmological constant. This solves the **horizon problem**, **flatness problem**, and **monopole problem** of standard Big Bang cosmology, and seeds **primordial density perturbations** observed in the cosmic microwave background. Inflation is described by **de Sitter spacetime** at zeroth order, with the inflaton field providing small departures.

> [!tip] AdS/CFT Correspondence *(from String Theory)*
> The anti-de Sitter spacetime (negative $\Lambda$) is dual to a conformal field theory on its boundary, via **Maldacena's conjecture**. Quantum gravity in AdS is equivalent to a non-gravitational gauge theory in one less dimension — a precise realisation of the **holographic principle**. Used to compute properties of strongly-coupled QFTs (quark-gluon plasmas, condensed matter at quantum critical points) by translating to weakly-coupled gravity. The AdS/CFT side is exactly solvable in many cases; the field-theory side often is not.

> [!tip] The Cosmological Constant Problem and the Landscape *(from String Theory and Multiverse Cosmology)*
> Quantum field theory predicts $\rho_\Lambda$ of order the cutoff scale (Planck) to the fourth power: $\sim 10^{120}$ times the observed value. **String theory** has a "landscape" of $\sim 10^{500}$ metastable vacua with different values of $\Lambda$, and the **anthropic principle** selects vacua with small $\Lambda$ (where galaxies can form). This converts the "fine-tuning problem" into a statistical selection question — but the answer remains controversial.

> [!tip] Nariai Black Holes and the Hottest Hawking Radiation *(from Black Hole Thermodynamics)*
> In Schwarzschild-de Sitter spacetimes, when the black-hole horizon and cosmological horizon coincide (Nariai limit $\Lambda M^2 = 1/9$), the geometry is $\text{dS}_2 \times S^2$ and the black hole is in thermal equilibrium with the cosmological horizon. Studied as a simple model of black hole thermodynamics in de Sitter, with implications for understanding the late-time decay of black holes in our accelerating universe.

> [!tip] Vacuum Decay and the Fate of the Universe *(from Quantum Field Theory in Curved Spacetime)*
> If the Higgs vacuum is metastable (a possibility supported by current measurements of the Higgs and top quark masses), our universe could tunnel to a lower-energy vacuum with a different effective $\Lambda$. **Coleman–de Luccia** bubble nucleation describes this process; the bubble interior would be a different cosmological constant universe expanding into ours. The current best-fit suggests our vacuum is metastable on cosmological time scales but stable enough for our current physics — a remarkable coincidence of Standard Model parameters.

---
type: definition
subject: general-relativity
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Lorentzian Manifold"
tags: [physics, general-relativity, curvature]
---

# Notation

Spacetime $(M, g)$, signature $(+,-,-,-)$. The Levi-Civita connection (see [[Riemannian Geometry I — Connections and Covariant Differentiation]]) has Christoffel symbols $\Gamma^\rho{}_{\mu\nu}$. The **Riemann curvature tensor** has components $R^\rho{}_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho{}_{\nu\sigma} - \partial_\nu \Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$ (see [[Riemannian Geometry III — Riemann Curvature and Topology]]). The **Ricci tensor** is the contraction $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$; the **scalar curvature** is $R = g^{\mu\nu} R_{\mu\nu}$. Full notation registry on [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Axiom Motivation

The desideratum is to construct, from the [[Riemannian Geometry III — Riemann Curvature and Topology|Riemann curvature tensor]] of a Lorentzian manifold, a symmetric $(0,2)$-tensor that (i) is built from the metric and its first two derivatives, (ii) is automatically divergence-free (so its equation to $T_{\mu\nu}$ is consistent with energy-momentum conservation), and (iii) reduces to the correct Newtonian limit. The unique such tensor (modulo $g_{\mu\nu}$ itself, giving the cosmological constant) is the **Einstein tensor** $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$. This is a remarkable structural fact: the *form* of the field equations is essentially forced by these three requirements.

**Why not just the Ricci tensor?** Einstein's first guess (October 1915) was $R_{\mu\nu} = 8\pi T_{\mu\nu}$. This is wrong, for a structural reason: the Ricci tensor is *not* divergence-free in general. From the contracted Bianchi identity (a consequence of the second Bianchi identity for the Riemann tensor),

$$\nabla^\mu R_{\mu\nu} = \frac{1}{2} \nabla_\nu R.$$

If we set $R_{\mu\nu} = 8\pi T_{\mu\nu}$ and demand $\nabla^\mu T_{\mu\nu} = 0$ (local energy-momentum conservation), then we need $\nabla_\nu R = 0$ — the scalar curvature must be constant throughout spacetime. This is far too restrictive (it would forbid most physically interesting solutions). So Einstein's first guess is over-determined: either conservation fails, or the geometry is unnaturally restricted.

**The fix: subtract $\frac{1}{2} g_{\mu\nu} R$.** Compute:
$$\nabla^\mu G_{\mu\nu} = \nabla^\mu(R_{\mu\nu} - \tfrac{1}{2} g_{\mu\nu} R) = \nabla^\mu R_{\mu\nu} - \tfrac{1}{2} \nabla_\nu R = \tfrac{1}{2} \nabla_\nu R - \tfrac{1}{2} \nabla_\nu R = 0.$$

Identically. The Einstein tensor is divergence-free as a geometric identity — no equations of motion needed, no constraint on the geometry. This is the structural payoff of the $-\frac{1}{2} g_{\mu\nu} R$ subtraction, and it is the unique correction (at the level of symmetric $(0,2)$-tensors built linearly from Ricci and the metric) that makes Einstein's field equations automatically consistent with conservation. Einstein arrived at this in November 1915, after weeks of struggle, and it is the formula that closed the search for the field equations.

**Why is this the unique answer?** **Lovelock's theorem** (1971) makes the uniqueness precise: in four spacetime [[Def - Dimension|dimensions]], the only symmetric, divergence-free $(0,2)$-tensor built from $g_{\mu\nu}$ and its derivatives, linear in the second derivatives (i.e., yielding second-order field equations), is
$$\alpha G_{\mu\nu} + \beta g_{\mu\nu},$$
with $\alpha, \beta$ constants — the Einstein tensor plus a possible cosmological constant. Higher-dimensional generalisations (the **Lovelock gravities**) admit richer choices (the **Gauss–Bonnet** term in 5D and higher), but in 4D the form is forced by these structural requirements.

**Per-condition failure analysis:**

(a) *If we drop "symmetric"*: the most general $(0,2)$-tensor built from $g$ and derivatives could have an antisymmetric part, but the matter source $T_{\mu\nu}$ is symmetric, so an antisymmetric LHS would have to vanish, eliminating the asymmetric degrees of freedom anyway.

(b) *If we drop "divergence-free"*: as discussed, the field equations would be inconsistent with conservation unless special restrictions hold. This is exactly Einstein's first-attempt mistake.

(c) *If we drop "built from $g$ and first two derivatives"*: higher-derivative theories (involving $\nabla\nabla\nabla\nabla g$ or quadratic curvature invariants like $R^2$, $R_{\mu\nu} R^{\mu\nu}$) are allowed, but they generically introduce **ghost modes** (unstable degrees of freedom, see Ostrogradsky's theorem) and are non-renormalisable. They appear in **effective field theory** as small corrections at high energy, but not as the leading-order theory of gravity at accessible scales.

(d) *If we drop "linear in second derivatives"*: nonlinear-in-second-derivative theories (like $R^2$ gravity or $f(R)$ gravity) generically violate the second-order field equation requirement and introduce extra propagating degrees of freedom (additional scalar fields in disguise).

(e) *If we drop the 4D assumption*: in higher dimensions, the **Gauss–Bonnet** term $\mathcal{G} = R^2 - 4R_{\mu\nu}R^{\mu\nu} + R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ contributes nontrivially to the field equations (in 4D, it is a topological term and contributes nothing to the equations of motion); this is the basis of **Lovelock gravity** and **Einstein–Gauss–Bonnet** theory.

---

# The Definition

> **Definition (Einstein tensor).** Let $(M, g)$ be a (semi-)Riemannian manifold, with the Levi-Civita connection $\nabla$, Riemann tensor $R^\rho{}_{\sigma\mu\nu}$, Ricci tensor $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$, and scalar curvature $R = g^{\mu\nu} R_{\mu\nu}$. The **Einstein tensor** is the symmetric $(0,2)$-tensor field
> $$G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R.$$
>
> The contracted form is $G^\mu{}_\nu = R^\mu{}_\nu - \frac{1}{2} \delta^\mu{}_\nu R$. The trace is $G = g^{\mu\nu} G_{\mu\nu} = R - 2R = -R$.

**Key properties:**

1. **Symmetry:** $G_{\mu\nu} = G_{\nu\mu}$ (inherited from symmetry of the Ricci tensor).

2. **Divergence-free:** $\nabla^\mu G_{\mu\nu} = 0$, identically — this is the **contracted Bianchi identity**, a consequence of the second Bianchi identity for the Riemann tensor.

3. **Trace:** $G^\mu{}_\mu = -R$.

4. **Trace-reversed form:** Solving $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$ for $R_{\mu\nu}$ gives
$$R_{\mu\nu} = G_{\mu\nu} - \frac{1}{2} g_{\mu\nu} G = G_{\mu\nu} + \frac{1}{2} g_{\mu\nu} R.$$
Combined with the Einstein equation $G_{\mu\nu} = 8\pi T_{\mu\nu}$, this gives the **trace-reversed Einstein equation** $R_{\mu\nu} = 8\pi(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$, where $T = T^\mu{}_\mu$ is the trace of the stress-energy. In vacuum ($T_{\mu\nu} = 0$), this reduces to **$R_{\mu\nu} = 0$** — the **vacuum Einstein equations**.

5. **With cosmological constant:** The most general divergence-free symmetric tensor built from the metric and first two derivatives is $G_{\mu\nu} + \Lambda g_{\mu\nu}$, where $\Lambda$ is the cosmological constant (a divergence-free addition since $\nabla_\mu g_{\nu\rho} = 0$). The **modified Einstein tensor** $G_{\mu\nu} + \Lambda g_{\mu\nu}$ is the LHS of the Einstein equations with cosmological constant.

---

# Categorical / Structural Definition

Structurally, the Einstein tensor is the **conserved current** of diffeomorphism invariance of the **Hilbert action**
$$S_\text{grav}[g] = \frac{1}{16\pi G}\int_M R\, \sqrt{-g}\, d^4x.$$

The variation of this action with respect to the inverse metric $g^{\mu\nu}$ is
$$\frac{\delta S_\text{grav}}{\delta g^{\mu\nu}} = \frac{1}{16\pi G} \sqrt{-g}\, G_{\mu\nu}$$
(see [[Thm - Hilbert's Variational Principle Yields Einstein Equations]]). The Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$ is then the **Noether identity** associated with diffeomorphism invariance of the gravitational action — exactly analogous to the gauge identity $\nabla_\mu F^{\mu\nu} \cdot J_\nu \propto \nabla^\nu \partial_\nu (\nabla_\mu A^\mu)$ in electromagnetism, where the antisymmetry of $F$ forces the identity.

From the **fibre bundle** perspective: the Einstein tensor is the moment map for diffeomorphism transformations on the configuration space of Lorentzian metrics, with respect to the symplectic structure induced by the Hilbert action. Its vanishing is the condition that the gauge transformations ([[Def - Diffeomorphism|diffeomorphisms]]) be a symmetry of the dynamics — the source of Einstein equation constraint structure.

---

# Relate to Other Fields / Compression

**True name:** The Einstein tensor is *the unique divergence-free symmetric $(0,2)$-tensor built from the metric and its first two derivatives in 4D, modulo the cosmological term*. Its uniqueness is **Lovelock's theorem** (1971), and its divergence-freeness is the **contracted Bianchi identity**. The combination $R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$ is forced by these structural requirements, not chosen.

In Newton's theory of gravity, the analogue of $G_{\mu\nu}$ is the Laplacian $\nabla^2 \phi$ — the differential operator that, applied to the gravitational potential, equals (a constant times) the mass density. In GR, the Laplacian is upgraded to the Einstein tensor — a nonlinear differential operator on the metric, returning a tensor of the same rank as the stress-energy tensor on the right.

The structural pattern recurs in other field theories:
- In **electromagnetism**, $\partial^\mu F_{\mu\nu} = 4\pi J_\nu$ is the field equation; the LHS is divergence-free automatically (by antisymmetry of $F$ and partial-derivative commutation), forcing $\partial^\nu J_\nu = 0$ — charge conservation.
- In **Yang–Mills**, $D^\mu F_{\mu\nu} = J_\nu$ has covariant divergence-free LHS, forcing covariant conservation of the color current.

In each case, the *form* of the LHS is structurally rigid (forced by gauge symmetry or geometry), and the conservation of the source is a consequence.

---

# Examples / Corollaries

**Is an instance — vacuum (Minkowski space).** For flat Minkowski space, $R^\rho{}_{\sigma\mu\nu} = 0$, hence $R_{\mu\nu} = 0$, $R = 0$, and $G_{\mu\nu} = 0$. The vacuum Einstein equations $G_{\mu\nu} = 0$ are trivially satisfied.

**Is an instance — Schwarzschild metric.** In the exterior region $r > 2M$, $T_{\mu\nu} = 0$ (vacuum), so $G_{\mu\nu} = 0$, which is equivalent to $R_{\mu\nu} = 0$. The Schwarzschild metric satisfies these vacuum equations (this is the *content* of Schwarzschild being a solution; see [[Thm - Schwarzschild Solution]]).

**Is an instance — de Sitter spacetime.** $G_{\mu\nu} = -\Lambda g_{\mu\nu}$ with $\Lambda > 0$; equivalent to vacuum Einstein with cosmological constant. The maximally symmetric vacuum solution.

**Is an instance — FLRW spacetime.** For a homogeneous isotropic universe filled with perfect fluid, $G_{\mu\nu}$ is diagonal in comoving coordinates with $G^{00}$ giving the Friedmann equation $H^2 = (8\pi/3) \rho$ and $G^{ii}$ giving the acceleration equation. The form of $G_{\mu\nu}$ in cosmological symmetry is fixed by the symmetry.

**Is NOT an instance — the Ricci tensor alone.** $R_{\mu\nu}$ is symmetric but not divergence-free in general; using it as the LHS of the field equations (Einstein's October 1915 attempt) is inconsistent with conservation.

**Is NOT an instance — the Riemann tensor.** $R^\rho{}_{\sigma\mu\nu}$ has wrong rank (it is a $(1,3)$-tensor, while $T_{\mu\nu}$ is $(0,2)$). The Einstein equations cannot directly involve the full Riemann tensor; they involve its trace (the Ricci tensor) packaged into the Einstein tensor.

**Corollary — vacuum Einstein equations.** In vacuum, $T_{\mu\nu} = 0$, so $G_{\mu\nu} = 0$. Taking the trace: $G = -R = 0$, so $R = 0$. Substituting back: $G_{\mu\nu} = R_{\mu\nu} = 0$. The vacuum equations are simply $R_{\mu\nu} = 0$ — the Ricci tensor vanishes, but the full Riemann tensor need not (it has 20 independent components in 4D, of which 10 are in the Ricci tensor and 10 in the **Weyl tensor** that vanishes only for conformally flat spacetimes).

**Corollary — trace of the field equations.** Taking the trace of $G_{\mu\nu} = 8\pi T_{\mu\nu}$ gives $-R = 8\pi T$, where $T = T^\mu{}_\mu$. Combined with the original, this gives the trace-reversed form $R_{\mu\nu} = 8\pi(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$.

**Corollary — Einstein tensor in terms of sectional curvatures.** For an orthonormal frame $\{e_0, e_1, e_2, e_3\}$ with $e_0$ timelike, the $(0,0)$ component is
$$G(e_0, e_0) = K(e_1 \wedge e_2) + K(e_1 \wedge e_3) + K(e_2 \wedge e_3),$$
the sum of the three spatial sectional curvatures (see Frankel §11.5a). This is Wheeler's geometric formula and gives the physical content of $G_{00}$ as "intrinsic + extrinsic spatial curvature".

**Calibration check.** (i) Verify by direct computation that $\nabla^\mu G_{\mu\nu} = 0$ given the second Bianchi identity $\nabla_{[\rho} R_{\sigma\tau]\mu\nu} = 0$. (ii) Compute the trace $g^{\mu\nu} G_{\mu\nu}$ and verify it equals $-R$. (iii) In a Riemannian (Euclidean) 2-manifold, show that $G_{\mu\nu} = 0$ identically — in 2D, the Einstein tensor vanishes, which is why 2D gravity is topological. The full Riemann tensor in 2D is $R_{\mu\nu\rho\sigma} = K(g_{\mu\rho} g_{\nu\sigma} - g_{\mu\sigma} g_{\nu\rho})$ with $K$ the Gauss curvature; computing $R_{\mu\nu}$ and $R$ from this verifies $G_{\mu\nu} \equiv 0$.

---

# Unlocked by This

> [!tip] Vacuum Einstein Equations and Black Holes *(from Black Hole Physics)*
> The vacuum equations $R_{\mu\nu} = 0$ admit the **Schwarzschild**, **Kerr**, and **Reissner–Nordström** (with EM) solutions — the black hole spacetimes. These are not just mathematical curiosities: they describe the gravity outside ordinary stars (where Schwarzschild applies), the gravity outside rotating astrophysical bodies (Kerr), and the gravity of charged objects (Reissner–Nordström). The **no-hair theorem** asserts that the most general stationary vacuum black hole solution is Kerr, parametrised by mass and angular momentum only.

> [!tip] Lovelock's Theorem and Modified Gravity *(from Beyond-Einstein Theories)*
> **Lovelock's theorem** (1971) states that in 4D, the only divergence-free symmetric $(0,2)$-tensor built from the metric and at most its second derivatives, linear in second derivatives, is $\alpha G_{\mu\nu} + \beta g_{\mu\nu}$. Modifications to gravity in 4D therefore must either introduce new fields ($f(R)$ gravity is equivalent to a scalar-tensor theory), drop locality, or go to higher derivatives (introducing instability via Ostrogradsky's theorem). In higher dimensions, the **Lovelock gravities** include the Gauss–Bonnet term and richer structures, studied in **brane-world cosmology** and **string theory** corrections.

> [!tip] The Initial-Value Problem of GR *(from Mathematical General Relativity)*
> The four equations $G_{0\mu} = 8\pi T_{0\mu}$ (where $0$ is the time-normal direction) are **constraint equations** on a spacelike slice: they involve only the spatial metric and second fundamental form, not their time derivatives, and are obstructions to free choice of initial data. The other six equations $G_{\alpha\beta} = 8\pi T_{\alpha\beta}$ ($\alpha, \beta$ spatial) are **evolution equations**. The structure $\nabla^\mu G_{\mu\nu} = 0$ ensures the constraints propagate: if they hold on the initial slice, they hold on every later slice, making the Cauchy problem consistent. This is the **3+1 decomposition** and the basis of numerical relativity.

> [!tip] Einstein–Cartan Theory *(from Spin and Torsion in Gravity)*
> Relaxing the assumption of torsion-free connection (allowing the connection to have torsion, which would source spin densities) gives **Einstein–Cartan theory**. The field equations split: the symmetric part gives a modified Einstein equation, the antisymmetric part gives the **Cartan equation** relating torsion to spin density. For ordinary matter (which has no spin density at the macroscopic level), Einstein–Cartan reduces to GR. For Dirac fermions in curved spacetime, the spin density is nonzero and modifies the gravitational dynamics at the level of $\hbar G \sim (\text{Planck length})^2$ — usually negligible.

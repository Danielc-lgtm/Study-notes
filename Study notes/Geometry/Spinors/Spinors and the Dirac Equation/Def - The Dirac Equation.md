---
type: definition
subject: spinors
prereqs:
  - "Def - Dirac Gamma Matrices"
  - "Def - Minkowski Space and the Metric"
  - "Def - The Lorentz Group"
tags: [geometry, spinors, quantum-mechanics, relativity]
---

# Notation

A **Dirac spinor** is a function $\psi : \mathbb{R}^{1,3} \to \mathbb{C}^4$ assigning to each spacetime point a 4-component complex vector. The components are usually written $\psi^a$ for $a = 1, 2, 3, 4$, with the natural decomposition $\psi = (\psi_L, \psi_R)^T$ into two-component left- and right-handed Weyl spinors in the chiral basis. The **Dirac conjugate** is $\bar\psi = \psi^\dagger \gamma^0$, a row vector. The Minkowski metric is $\eta = \mathrm{diag}(-1, +1, +1, +1)$ (Frankel's "mostly plus" convention), and $\partial_\mu = \partial/\partial x^\mu$. Mass is denoted $m$, with $\hbar = c = 1$. We use the **Feynman slash** $\not\partial = \gamma^\mu \partial_\mu$.

> [!warning] Convention: sign of mass term
> In the Frankel convention $(- + + +)$, the Dirac equation reads $\gamma^\mu \partial_\mu \psi = m\psi$ — no explicit factor of $i$. In the alternative physics convention $(+ - - -)$, the d'Alembertian flips sign, and to keep $m^2$ positive in the squared equation one writes $i\gamma^\mu \partial_\mu \psi = m\psi$ instead. The two equations describe the *same physics*; only conventions differ.

---

# Axiom Motivation

The Dirac equation was forced on physics in 1928 by the following chain of desiderata:

**Desideratum 1: relativistic.** A wave equation describing relativistic particles must be Lorentz-covariant. The first guess — the **Klein–Gordon equation** $\Box\psi = m^2\psi$ — is relativistic but second-order in time; its conserved current $j^\mu = i(\psi^*\partial^\mu\psi - \psi\partial^\mu\psi^*)$ is not positive-definite, so $j^0$ can be negative and cannot be interpreted as a probability density.

**Desideratum 2: first-order in time.** The Schrödinger-style probabilistic interpretation requires $\psi$ to evolve via an equation of the form $i\partial_t\psi = H\psi$ with $H$ a self-adjoint Hamiltonian (so probability is conserved). This forces the equation to be first-order in $\partial_t$, and by Lorentz covariance also first-order in the spatial derivatives.

**Desideratum 3: still implies Klein–Gordon for free particles.** A relativistic particle of mass $m$ has $E^2 = p^2 + m^2$, so $\psi$ must satisfy $\Box\psi = m^2\psi$ (componentwise). If $\not D\psi = m\psi$ is the first-order equation, then $\not D^2\psi = m^2\psi$ must equal $\Box\psi$, so $\not D^2 = \Box$. As computed in [[Def - Dirac Gamma Matrices|the gamma matrices' axiom motivation]], $\not D = \gamma^\mu\partial_\mu$ satisfies $\not D^2 = \tfrac{1}{2}\{\gamma^\mu, \gamma^\nu\}\partial_\mu\partial_\nu$, which equals $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu$ iff $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$. This is the Clifford relation, and forces $\gamma^\mu$ to be $4 \times 4$ matrices.

**Desideratum 4: $\psi$ transforms correctly under Lorentz transformations.** Under a Lorentz transformation $\Lambda \in L_0$ corresponding to $A \in \mathrm{SL}(2, \mathbb{C})$ via the cover $\mathrm{SL}(2, \mathbb{C}) \to L_0$, the spinor $\psi$ transforms as $\psi(x) \mapsto \rho(A)\psi(\Lambda^{-1}x)$ with $\rho$ the Dirac spinor representation $\rho(A) = \mathrm{diag}(A, (A^\dagger)^{-1})$. The Dirac equation should be invariant: $\not D \psi(x) = m\psi(x)$ should imply $\not D \tilde\psi(\tilde x) = m\tilde\psi(\tilde x)$ where $\tilde\psi(\tilde x) = \rho(A)\psi(\Lambda^{-1}\tilde x)$. The non-trivial verification: $\gamma^\mu$ is the *same matrix* in every Lorentz frame, but $\partial_\mu$ is frame-dependent — Lorentz covariance requires the intertwining $\rho(A)^{-1}\gamma^\mu \rho(A) = \Lambda^\mu_{\;\nu}\gamma^\nu$, which is exactly the homomorphism property of $\mathrm{SL}(2, \mathbb{C}) \to L_0$ at the Lie-algebra level.

**Desideratum 5: positive-definite conserved current.** Under the Dirac equation, the four-current $j^\mu = \bar\psi\gamma^\mu\psi$ satisfies $\partial_\mu j^\mu = 0$ (conservation), and $j^0 = \bar\psi\gamma^0\psi = \psi^\dagger\psi \geq 0$ — a positive-definite probability density. This resolves the negative-probability problem of Klein–Gordon. See [[Ex - The Square of a Dirac Spinor Gives a 4-Current]].

What if we *dropped desideratum 3* (the implication of Klein–Gordon)? We could write a first-order linear equation with non-Clifford gamma matrices, but the resulting equation would not have the correct relativistic dispersion relation $E^2 = p^2 + m^2$. The Klein–Gordon implication is what *fixes* the gamma matrices' algebra; the Dirac equation is the *minimal* relativistic first-order wave equation.

What if we dropped *covariance* (desideratum 4)? Then we could pick a preferred frame, but the equation would not respect special relativity — physically unacceptable.

What if we *strengthened* the equation to be invariant under all of $\mathrm{SL}(2, \mathbb{C})$ rather than just its image $L_0$? This is automatic: the Dirac equation's covariance is encoded as $\rho$-equivariance, and the *two* possible $A \in \mathrm{SL}(2, \mathbb{C})$ above a given $\Lambda \in L_0$ give the same equation (the equation involves only the Lorentz transformation $\Lambda$ on coordinates and the matrix $\rho(A)$ on spinor indices, and $\rho(-A) = -\rho(A)$ just multiplies $\psi$ by $-1$ everywhere — a global phase that drops out of the equation).

The equation that emerges is the **Dirac equation**, and the resulting theory describes spin-$\tfrac{1}{2}$ particles (electrons, protons, neutrons, neutrinos, quarks) with their antiparticles, automatically displaying the correct gyromagnetic ratio ($g = 2$), the Pauli exclusion principle (via spin-statistics), and the negative-energy solutions that led to the prediction of antimatter.

---

# The Definition

The **Dirac equation** for a free spin-$\tfrac{1}{2}$ particle of mass $m$ on Minkowski space $\mathbb{R}^{1,3}$ is
$$(\gamma^\mu \partial_\mu - m)\psi = 0,$$
equivalently
$$\not\partial \psi = m\psi,$$
where $\not\partial = \gamma^\mu\partial_\mu$ is the **Dirac operator** (Feynman slash), $\gamma^\mu$ are the [[Def - Dirac Gamma Matrices|Dirac gamma matrices]] satisfying $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$, and the wave function $\psi: \mathbb{R}^{1,3} \to \mathbb{C}^4$ is a **Dirac spinor**.

Equivalent form: writing $\not\partial - m$ explicitly,
$$\sum_{\mu = 0}^3 \gamma^\mu \frac{\partial\psi}{\partial x^\mu} = m\psi.$$

**Lorentz covariance.** For each Lorentz transformation $\Lambda \in L_0 = SO^+(3,1)$ with $A \in \mathrm{SL}(2, \mathbb{C})$ a lift via the cover $\mathrm{SL}(2, \mathbb{C}) \to L_0$, the transformation
$$\psi(x) \mapsto \tilde\psi(\tilde x) = \rho(A)\psi(\Lambda^{-1}\tilde x)$$
maps solutions of the Dirac equation to solutions, with $\rho: \mathrm{SL}(2, \mathbb{C}) \to GL(4, \mathbb{C})$ the **Dirac spinor representation**:
$$\rho(A) = \begin{pmatrix} A & 0 \\ 0 & (A^\dagger)^{-1}\end{pmatrix}$$
(in the Weyl basis). The two lifts $\pm A$ give the same physics — a $2\pi$ Lorentz rotation flips the sign of $\psi$, but observable quantities (bilinears in $\psi$) are unchanged.

**Conserved current.** $j^\mu = \bar\psi \gamma^\mu \psi$ (where $\bar\psi = \psi^\dagger\gamma^0$) is a Lorentz $4$-vector, and the Dirac equation implies $\partial_\mu j^\mu = 0$. The $0$-component $j^0 = \bar\psi\gamma^0\psi = -\psi^\dagger(\gamma^0)^2\psi/(-1) = \psi^\dagger\psi \geq 0$ is the **probability density**. See [[Ex - The Square of a Dirac Spinor Gives a 4-Current]].

**Decoupled form.** In the Weyl (chiral) basis, with $\psi = (\psi_L, \psi_R)^T$ and the gamma matrices block-decomposed, the Dirac equation reads as a coupled system for the two Weyl spinors:
$$(-\partial_t + \vec\sigma \cdot \vec\nabla)\psi_R = m\psi_L,$$
$$(\partial_t + \vec\sigma \cdot \vec\nabla)\psi_L = m\psi_R.$$
For $m = 0$, the system **decouples** into independent **Weyl equations** $(\pm\partial_t + \vec\sigma\cdot\vec\nabla)\psi = 0$, describing massless chiral fermions (neutrinos in the early Standard Model).

**EM coupling.** In the presence of an electromagnetic field with $4$-potential $A_\mu$, the Dirac equation becomes
$$(\gamma^\mu(\partial_\mu - ieA_\mu) - m)\psi = 0,$$
the standard **minimal coupling** prescription. See [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Categorical / Structural Definition

The Dirac equation is the equation of motion for the **Dirac Lagrangian**
$$\mathcal{L}_D = \bar\psi(\gamma^\mu\partial_\mu - m)\psi$$
(up to total derivatives and conventions). Variation with respect to $\bar\psi$ yields the Dirac equation $(\gamma^\mu\partial_\mu - m)\psi = 0$; variation with respect to $\psi$ yields the conjugate equation $\partial_\mu\bar\psi\gamma^\mu + m\bar\psi = 0$. The Lagrangian is Lorentz-invariant: under $\psi \to \rho(A)\psi$, $\bar\psi \to \bar\psi\rho(A)^{-1}$ (using $\rho(A)^\dagger\gamma^0 = \gamma^0\rho(A)^{-1}$), and $\gamma^\mu\partial_\mu$ transforms covariantly.

Categorically, the Dirac operator $\not\partial: \Gamma(SM) \to \Gamma(SM)$ is a **first-order linear differential operator** on sections of the Dirac spinor bundle $SM$ over spacetime. In the flat-space case $M = \mathbb{R}^{1,3}$, $SM = \mathbb{R}^{1,3} \times \mathbb{C}^4$ is trivial; in curved spacetime, $SM$ is the spinor bundle associated to a [[Def - Spin Structure on a Manifold|spin structure]], and the Dirac operator generalizes to $\not D = \gamma^a e_a^\mu \nabla^S_\mu$ (see [[Def - Spin Connection and the Dirac Operator]]).

The Dirac equation is **elliptic in Euclidean signature** (where $\not D^2 = \Delta$, a positive-definite Laplacian) and **hyperbolic in Lorentzian signature** (where $\not D^2 = \Box$). Elliptic operators have finite-dimensional kernels on compact manifolds (the index theorem); hyperbolic operators have rich evolution-equation structure (existence and uniqueness for the Cauchy problem).

---

# Relate to Other Fields / Compression

**True name:** The Dirac equation is *the unique Lorentz-covariant first-order linear wave equation on Minkowski space whose square is the Klein–Gordon operator*. The "uniqueness" is up to representation choice (Weyl, Dirac, Majorana basis) and the trivial freedom to replace $\psi$ by $\rho(A)\psi$ for any fixed $A$ — physically the equation is unique. The non-trivial content is the *existence* of such an equation, which requires the Clifford algebra to be representable as $4 \times 4$ complex matrices.

The Dirac equation generalizes in three natural directions:

1. **Higher dimensions:** in spacetime dimension $D = 2k$, the gamma matrices are $2^k \times 2^k$ complex matrices, and $\psi$ is a $2^k$-component spinor. The Dirac equation $\not D\psi = m\psi$ continues to make sense. In $D = 10$ (superstring theory), $\psi$ has 32 complex components.

2. **Curved spacetime:** on a [[Def - Spin Structure on a Manifold|spin manifold]] $M$ with metric $g$, the Dirac operator becomes $\not D = \gamma^a e_a^\mu \nabla^S_\mu$ where $e_a^\mu$ is an orthonormal frame and $\nabla^S$ is the [[Def - Spin Connection and the Dirac Operator|spin connection]]. Its square satisfies the **Lichnerowicz formula** $\not D^2 = -\nabla^*\nabla + R/4$ with $R$ the scalar curvature — see [[Thm - Lichnerowicz Formula]].

3. **Coupled to gauge fields:** $\not D \to \not D_A = \gamma^\mu(\partial_\mu - igA_\mu)$ for a gauge connection $A_\mu$. This is **minimal coupling**, and it is the standard recipe for adding interactions in the Standard Model.

Connections to other physics:

- **QED Lagrangian** $\mathcal{L} = -\tfrac{1}{4}F^{\mu\nu}F_{\mu\nu} + \bar\psi(i\gamma^\mu D_\mu - m)\psi$ combines the Maxwell Lagrangian with the (electromagnetic-coupled) Dirac Lagrangian; varying gives Maxwell's equations and the Dirac equation as Euler–Lagrange equations.
- **Standard Model fermions:** every fundamental fermion (quark, lepton) is described by a Dirac equation, with mass terms forbidden by the chiral $SU(2)_L$ gauge symmetry until the Higgs mechanism generates them via the Yukawa couplings.
- **Heisenberg's matrix mechanics**: Dirac's original derivation aimed to make Heisenberg's noncommutative observables compatible with relativity — the Clifford-relation structure of the gamma matrices is a direct consequence.

---

# Examples / Corollaries

**Example 1: Massless case.** For $m = 0$, the Dirac equation decouples in the Weyl basis into two Weyl equations: $(\partial_t + \vec\sigma\cdot\vec\nabla)\psi_L = 0$ and $(-\partial_t + \vec\sigma\cdot\vec\nabla)\psi_R = 0$. Each is the wave equation for a chiral massless fermion (the neutrino in the Standard Model before neutrino masses).

**Example 2: Plane wave solutions.** Look for $\psi(x) = u(p) e^{-ip\cdot x}$ with $p \cdot x = p_0 x^0 + \vec p \cdot \vec x = -E t + \vec p \cdot \vec x$ (since $p_0 = -E$ for a future-pointing momentum). Substituting: $\gamma^\mu\partial_\mu\psi = -ip_\mu\gamma^\mu u e^{-ip\cdot x} = -i\not p \,u\,e^{-ip\cdot x}$. So the equation $\not\partial\psi = m\psi$ becomes $-i\not p\, u = m u$, i.e. $(\not p + im)u = 0$. Since $\not p^2 = p^2 = -m^2$ (using $E^2 - \vec p^2 = m^2$), the operator $\not p + im$ has rank 2, so there are two linearly independent solutions for $u$. See [[Ex - Plane-Wave Solutions of the Free Dirac Equation]].

**Example 3: Verifying Lorentz covariance for a boost.** Take a boost in the $x$-direction with rapidity $\xi$: $\Lambda = \begin{pmatrix} \cosh\xi & \sinh\xi & 0 & 0 \\ \sinh\xi & \cosh\xi & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$. The corresponding $A \in \mathrm{SL}(2, \mathbb{C})$ is $A = \exp(\tfrac{1}{2}\xi\sigma_1)$. The Dirac spinor representation is $\rho(A) = \mathrm{diag}(A, (A^\dagger)^{-1}) = \mathrm{diag}(\exp(\tfrac{1}{2}\xi\sigma_1), \exp(-\tfrac{1}{2}\xi\sigma_1))$. Verify that $\rho(A)^{-1}\gamma^1\rho(A) = \cosh\xi\gamma^1 + \sinh\xi\gamma^0 = \Lambda^1_{\;\nu}\gamma^\nu$ as required.

**Example 4: Conservation of the probability current.** For any solution $\psi$ of the Dirac equation, $\partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu\partial_\mu\psi = -m\bar\psi\psi + m\bar\psi\psi = 0$ (using the Dirac equation and its conjugate). So the current is conserved automatically.

**Non-example: a "Dirac equation" with scalar coefficients.** The equation $\sum_\mu c_\mu \partial_\mu\psi = m\psi$ for $c_\mu \in \mathbb{R}$ and $\psi: \mathbb{R}^{1,3} \to \mathbb{C}$ is not the Dirac equation — squaring gives $(\sum c_\mu\partial_\mu)^2 = \sum c_\mu^2 \partial_\mu^2 + 2\sum_{\mu < \nu} c_\mu c_\nu \partial_\mu\partial_\nu = m^2$, which is the Klein-Gordon equation only if $c_\mu c_\nu = 0$ for $\mu \neq \nu$ — i.e., only one $c_\mu$ nonzero. Scalar coefficients cannot give the cross-derivative cancellation; non-commutativity is essential.

**Non-example: the Klein–Gordon equation with positive-energy projection.** Some texts attempt to "extract" the Dirac equation from Klein–Gordon by projecting onto positive-energy solutions. This works for free particles but fails in the presence of interactions (the projection becomes time-dependent), so the Dirac equation is the genuinely fundamental object.

**Calibration check.** A reader should verify: (i) plug $\psi = u(p)e^{-ip\cdot x}$ into the Dirac equation and recover $(\not p + im)u = 0$ (with our sign convention); (ii) verify the conserved current $j^\mu = \bar\psi\gamma^\mu\psi$ is real (i.e., $j^\mu = \overline{j^\mu}$) using $(\gamma^\mu)^\dagger \gamma^0 = \gamma^0\gamma^\mu$; (iii) check that under $\psi \mapsto -\psi$ (the $2\pi$-rotation effect), the Dirac equation is invariant — confirming the equation depends only on the *projective* spinor up to phase.

---

# Unlocked by This

> [!tip] Prediction of the Positron *(from Quantum Field Theory)*
> The Dirac equation has *negative-energy solutions* $\psi(x) = v(p)e^{+ip\cdot x}$ corresponding to $(\not p - im)v = 0$, which classically would represent particles with negative energy. Dirac initially interpreted these as a "Dirac sea" filled with negative-energy particles, with "holes" appearing as positive-energy *positrons* — the antimatter predicted in 1928 and discovered by Anderson in 1932. In modern quantum field theory, these solutions are reinterpreted as antiparticle creation operators in the second-quantized Dirac field. The existence of antimatter is thus a direct consequence of taking the *square root* of the relativistic energy operator — it is forced by the algebra of gamma matrices.

> [!tip] Dirac Operator on Curved Spacetime *(from Differential Geometry)*
> The flat-space Dirac equation $\gamma^\mu\partial_\mu\psi = m\psi$ generalizes to a curved Riemannian or Lorentzian spin manifold $M$ as $\not D\psi = \gamma^a e_a^\mu \nabla^S_\mu\psi = m\psi$, where $\nabla^S$ is the [[Def - Spin Connection and the Dirac Operator|spin connection]] lifted from the Levi-Civita connection. The Dirac operator $\not D$ is the **square root** of the Hodge–Laplacian-like operator $\not D^2 = -\nabla^{S*}\nabla^S + R/4$ (the [[Thm - Lichnerowicz Formula|Lichnerowicz formula]]). This makes the Dirac operator the fundamental elliptic operator of spin geometry, the central object in the Atiyah–Singer index theorem and the source of all major index formulas.

> [!tip] Gyromagnetic Ratio $g = 2$ as a Prediction
> In the nonrelativistic limit of the Dirac equation coupled to electromagnetism (the **Pauli equation**), one finds that the electron's spin contributes to its magnetic moment with **gyromagnetic ratio $g = 2$** — an order of magnitude larger than the orbital contribution would suggest. This was a triumph of Dirac's theory: pre-Dirac, $g = 2$ was a phenomenological fit to experiment; post-Dirac, it is a *prediction* of relativity plus spin. The small deviation $g - 2 \approx 2 \times \alpha/(2\pi) \approx 0.00232$ (Schwinger's 1948 calculation) is one of the most precisely tested predictions in all of physics.

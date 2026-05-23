---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Complex Line Bundle"
  - "Def - Hermitian Vector Bundle"
  - "Def - Connection on a Vector Bundle"
  - "Def - Curvature of a Vector-Bundle Connection"
tags: [geometry, gauge-theory, electromagnetism, U(1)]
---

# Notation

$M$ is spacetime (typically $\mathbb{R}^4$ with signature $(+, -, -, -)$ or in non-relativistic settings $\mathbb{R}^3 \times \mathbb{R}$). $L \to M$ is a hermitian complex line bundle (see [[Def - Hermitian Vector Bundle]] and [[Def - Complex Line Bundle]]) with structure group $U(1)$. We use the **standing convention** $c = 1$ (speed of light) throughout. $A = A_\mu\,dx^\mu$ denotes the classical electromagnetic 4-potential; the **connection 1-form** of the $U(1)$-bundle is $\omega = -(ie/\hbar)A$, with $e$ the particle charge and $\hbar$ the reduced Planck constant. The curvature is $\theta = -(ie/\hbar)F$ where $F = dA$ is the electromagnetic field strength 2-form. $\mathfrak{u}(1) = i\mathbb{R}$ is the Lie algebra of $U(1)$; a $\mathfrak{u}(1)$-valued 1-form is $i$ times a real 1-form. For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Axiom Motivation

The question this definition resolves is **what kind of geometric object is the electromagnetic potential, really?** Classically, the EM 4-potential $A_\mu$ is a covector field on spacetime defined up to the addition of a gradient $A \to A + df$ — the "gauge freedom" of electromagnetism. Two potentials differing by a gradient produce the same physical field strength $F = dA$, hence the same Lorentz force, hence the same classical physics. Before quantum mechanics, this gauge freedom looked like a *mathematical redundancy* — a choice of $A$ is convenient for computation but no physically meaningful aspect of $A$ beyond $F$.

Quantum mechanics changes this dramatically. The wave function $\psi$ of a charged particle obeys Schrödinger's equation $i\hbar\partial_t\psi = \frac{1}{2m}(-i\hbar\nabla - eA)^2\psi + V\psi$, and this equation explicitly contains $A$, not just $F$. Under the gauge transformation $A \to A + df$, the equation becomes a different-looking equation — but it has the same solutions provided $\psi$ is *also* transformed by a phase: $\psi \to e^{(ie/\hbar)f}\psi$. The physics (in particular $|\psi|^2$, the probability density) is invariant, but the wave function "twists" under gauge transformations. This combined transformation rule is **Weyl's principle of gauge invariance** (Weyl 1929), and it points to a structural fact: $A$ and $\psi$ are not separate objects with their own gauge freedoms but two facets of a single geometric structure.

That structure is a **hermitian line bundle with a $U(1)$-connection**. The "wave function" $\psi$ is a section of $L$, the "vector potential" $A$ is (up to a constant) the connection 1-form, and the gauge transformation $\psi \to e^{(ie/\hbar)f}\psi$, $A \to A + df$ is simply a **change of local frame** in the bundle, with $g = e^{(ie/\hbar)f}$ a $U(1)$-valued change-of-frame matrix. Under such a change, the connection 1-form transforms as $\omega \to g^{-1}\omega g + g^{-1}dg = \omega + g^{-1}dg$ (since $U(1)$ is abelian), and we compute $g^{-1}dg = e^{-(ie/\hbar)f} \cdot e^{(ie/\hbar)f}(ie/\hbar)df = (ie/\hbar)df$, giving $\omega \to \omega + (ie/\hbar)df$. With the dictionary $\omega = -(ie/\hbar)A$, this is precisely $A \to A - df$ (the sign convention varies — Frankel uses $\omega = -ie A/\hbar$ giving $A \to A + df$).

Why does the factor $-ie/\hbar$ appear? Three constraints fix it. (i) The connection must be **hermitian** (preserve the inner product $h(\psi, \psi) = |\psi|^2$, so total probability is conserved), forcing $\omega$ to take values in $\mathfrak{u}(1) = i\mathbb{R}$ — hence the factor of $i$. (ii) Real $A_\mu$ from electromagnetism translates to imaginary $\omega$ — hence the imaginary unit. (iii) Schrödinger's equation has *Planck's constant* $\hbar$ in the canonical commutation relation $[\hat x, \hat p] = i\hbar$, and the *charge* $e$ in the Lorentz coupling. The combination $e/\hbar$ is the natural scale at which "phase per unit gauge potential" enters quantum mechanics, and the dictionary $\omega = -(ie/\hbar)A$ is forced by the requirement that $\nabla_\mu = \partial_\mu + \omega_\mu = \partial_\mu - (ie/\hbar)A_\mu$ recovers the minimally coupled momentum operator $\hat p_\mu = -i\hbar\partial_\mu - eA_\mu$. (In SI units one has $A/c$ instead of $A$, restoring a factor of $c$; in Gaussian units with $c = 1$ as here, the factor is gone.)

Why is **$U(1)$** the right gauge group? Because the symmetry of the wave function — multiplication by a unit complex number $e^{i\theta}$ at each point — is exactly the action of the group $U(1) = \{z \in \mathbb{C} : |z| = 1\}$ on the fibre $\mathbb{C}$. The local "phase ambiguity" of QM is a $U(1)$-action, and the *spatially varying* phase ambiguity (different phase at each point) is a *section* of $\mathrm{Aut}(L)$, equivalently a smooth function $f : M \to U(1)$.

Why does the **field strength $F = dA$** play the role of curvature? Because the structure equation $\theta = d\omega + \omega \wedge \omega$ for an abelian connection reduces to $\theta = d\omega$ (since $\omega \wedge \omega = 0$ for scalar-valued forms wedged with themselves). With $\omega = -(ie/\hbar)A$ we get $\theta = -(ie/\hbar)dA = -(ie/\hbar)F$. The physical field strength $F$ *is* (up to the dictionary) the curvature of the EM connection.

What does this exclude? An interpretation of $A$ as a "field" in the classical sense — a function on spacetime carrying physical information at every point — is misleading: only the *equivalence class* of $A$ under gauge transformations has physical content (and that equivalence class is exactly "the connection on $L$"). A naïve identification of $A$ with $F$ — taking $F$ to be the fundamental object — misses the Aharonov-Bohm effect and the monopole quantization, both of which require the bundle structure (the *patching* of local potentials).

---

# The Definition

A **$U(1)$ gauge field** on a smooth manifold $M$ is a connection on a hermitian complex line bundle $L \to M$ with structure group $U(1)$. Equivalently — by the abelian special case of [[Def - Connection on a Vector Bundle|connection]] theory — a $U(1)$ gauge field on $M$ is specified by:

1. A hermitian complex line bundle $L \to M$ with a chosen cover $\{U_\alpha\}$ trivializing $L$, transition functions $c_{\beta\alpha} : U_\alpha \cap U_\beta \to U(1)$, and the cocycle condition $c_{\gamma\beta}\,c_{\beta\alpha} = c_{\gamma\alpha}$.
2. In each patch $U_\alpha$, a **connection 1-form** $\omega_\alpha \in \Omega^1(U_\alpha, i\mathbb{R})$ — a real-valued 1-form times $i$ — satisfying on overlaps the abelian change-of-frame law

$$\omega_\beta = \omega_\alpha + c_{\beta\alpha}^{-1}dc_{\beta\alpha}.$$

**Electromagnetic dictionary.** The **electromagnetic connection** on $L$ associated with the electromagnetic 4-potential $A = A_\mu dx^\mu$ (a real 1-form) and a particle of charge $e$ is the $U(1)$-connection with local 1-form

$$\boxed{\omega = -\frac{ie}{\hbar}A.}$$

**Covariant derivative.** For a section $\psi$ of $L$ (the wave function), the covariant derivative is

$$\nabla_\mu\psi = (\partial_\mu - \tfrac{ie}{\hbar}A_\mu)\psi.$$

**Curvature.** The curvature 2-form of the EM connection is (using $\omega \wedge \omega = 0$ for abelian)

$$\theta = d\omega = -\frac{ie}{\hbar}dA = -\frac{ie}{\hbar}F,$$

where $F = dA$ is the **electromagnetic field-strength 2-form**. In components, $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ — in 4-d spacetime these are the entries of the antisymmetric tensor whose components are the electric field $E_i$ and the magnetic field $B^i$ via $F_{0i} = E_i$, $F_{ij} = -\epsilon_{ijk}B^k$.

**Gauge transformations.** A change of local frame $\psi \to g\psi$ with $g(x) = e^{(ie/\hbar)f(x)}$ for real $f \in C^\infty(M)$ transforms:

$$\psi \to e^{(ie/\hbar)f}\psi, \qquad A \to A + df, \qquad \omega \to \omega - \tfrac{ie}{\hbar}df.$$

The covariant derivative transforms covariantly: $\nabla_\mu(g\psi) = g(\nabla_\mu\psi)$. The curvature is gauge-invariant: $\theta_\beta = \theta_\alpha$.

**Hermiticity.** The connection 1-form $\omega = -(ie/\hbar)A$ is anti-hermitian as a $1 \times 1$ complex matrix (since $A$ is real): $\omega^* = (-(ie/\hbar)A)^* = (ie/\hbar)A = -\omega$. This is the $\mathfrak{u}(1) = i\mathbb{R}$-valuedness, and it is the technical face of "hermitian connection" — i.e., parallel transport is by $U(1)$ transformations (phase rotations), preserving $|\psi|^2$.

---

# Categorical / Structural Definition

A $U(1)$ gauge field is a **connection on a principal $U(1)$-bundle $P \to M$**, equivalently the data $(\{U_\alpha\}, \{c_{\beta\alpha}\}, \{A_\alpha\})$ modulo simultaneous gauge transformations. From the principal-bundle viewpoint (developed in [[Gauge Theory III — Connections in Principal and Associated Bundles]]):
- The principal $U(1)$-bundle $P$ is the "frame bundle" of the wave-function line bundle, with each fibre $P_p$ the $U(1)$-torsor of choices of unit-length basis vector in $L_p$.
- The connection on $P$ is a $\mathfrak{u}(1)$-valued 1-form $\tilde A$ on $P$, equivariant under right-$U(1)$ action and reproducing the Maurer-Cartan form $g^{-1}dg$ on vertical vectors.
- Pulling $\tilde A$ back to $M$ via a local section gives the local 1-form $A_\alpha = -(\hbar/ie)\omega_\alpha$ in the chosen "gauge".

The **moduli space** of $U(1)$ gauge fields on $M$ — connections modulo gauge equivalence — is an *affine* space modelled on closed 1-forms modulo exact ones, which is $H^1(M, \mathbb{R})$ for trivial bundles, and a torsor for $H^1(M, \mathbb{R})$ over each topological class of bundle. The classification of $U(1)$-bundles by $H^2(M, \mathbb{Z})$ (the first Chern class) plus this $H^1(M, \mathbb{R})$ modulus gives the full gauge-theoretic phase space.

The category of $U(1)$-bundles with connection on $M$ is a *2-category* — objects are bundles, 1-morphisms are connection-preserving bundle morphisms, 2-morphisms are gauge transformations between such morphisms — and is equivalent to the 2-category of "$U(1)$-gerbes" with connection at one level higher. This higher-categorical structure becomes essential in modern formulations of quantum field theory.

---

# Relate to Other Fields / Compression

The electromagnetic connection is **"the unique $\mathfrak{u}(1)$-valued 1-form on a complex line bundle whose curvature is the electromagnetic field strength"**.

**In classical electromagnetism (pre-quantum)**, the vector potential $A_\mu$ is a "mathematical convenience" without independent physical meaning — only $F_{\mu\nu}$ matters. Going from classical to quantum mechanics promotes $A$ to a *geometric* object (the connection), with physical consequences (Aharonov-Bohm) that distinguish $A$ from $A + df$ globally but not locally.

**In Yang-Mills theory** ([[Gauge Theory IV — Yang–Mills Fields and Instantons]]), the $U(1)$ gauge field is the abelian special case of a $G$-gauge field for general compact Lie group $G$. The structure equation $F = dA + A \wedge A$ has the non-linear $A \wedge A$ term for non-abelian $G$; for $U(1)$ it vanishes. Everything about EM generalizes — minimal coupling, covariant derivatives, gauge invariance — but with the new feature that the gauge field interacts with itself non-linearly.

**In condensed matter physics**, the $U(1)$ phase symmetry of wave functions and the corresponding gauge connections appear in: (a) superconductivity (the Cooper-pair condensate is a $U(1)$-charged field, gauge-coupled to electromagnetism, with the Higgs mechanism breaking the gauge symmetry); (b) the quantum Hall effect (the Berry connection on the Bloch bundle over the Brillouin zone is a $U(1)$-connection whose first Chern number is the quantized Hall conductance); (c) superfluidity (the order parameter is a $U(1)$-charged field and vortices are quantized magnetic flux tubes).

**True name:** The EM connection is **"the geometrically correct object whose minimal-coupling prescription replaces $\partial_\mu$ by $\nabla_\mu$ in any equation"**. To take any free-particle equation and couple it to electromagnetism, replace $\partial_\mu \to \nabla_\mu = \partial_\mu - (ie/\hbar)A_\mu$. The result is automatically gauge-invariant, automatically reproduces the Lorentz force at the classical limit, and correctly captures all the topological subtleties (Aharonov-Bohm, monopoles).

---

# Examples / Corollaries

**Is an instance: Free particle ($A = 0$).** The trivial $U(1)$-connection has $\omega = 0$, hence covariant derivative $\nabla_\mu = \partial_\mu$. The wave function is just a complex-valued function and Schrödinger's equation is the standard free-particle equation $i\hbar\partial_t\psi = -\frac{\hbar^2}{2m}\nabla^2\psi$. Curvature: zero — no electromagnetic field.

**Is an instance: Constant magnetic field $B$ in the $z$-direction.** Choose the symmetric gauge $A = \frac{1}{2}B(-y\,dx + x\,dy)$. Curvature $F = dA = B\,dx \wedge dy$. The minimally coupled Schrödinger equation produces **Landau levels** $E_n = \hbar\omega_c(n + \frac{1}{2})$ with cyclotron frequency $\omega_c = eB/m$, the fundamental result for charged particles in magnetic fields.

**Is an instance: Aharonov-Bohm solenoid.** $A = \frac{\Phi}{2\pi}d\phi$ on $\mathbb{R}^3 \setminus \{z\text{-axis}\}$, with $\Phi$ the flux through the solenoid. $F = dA = 0$ on the domain (the flux is hidden inside the excluded $z$-axis), but $\oint A = \Phi$ around any loop encircling the axis. See [[Ex - The Aharonov-Bohm Phase from the Magnetic Solenoid]].

**Is an instance: Dirac monopole.** Two-patch description with $A_U = g(1 - \cos\theta)d\phi$ on $S^2 \setminus \{\mathrm{south}\}$ and $A_V = -g(1 + \cos\theta)d\phi$ on $S^2 \setminus \{\mathrm{north}\}$. Transition function $c_{VU} = e^{-2ieg\phi/\hbar}$, well-defined iff $2eg/\hbar \in \mathbb{Z}$. See [[Def - The Dirac Monopole Bundle]] and [[Thm - Dirac Quantization Condition]].

**Is NOT an instance: Non-Hermitian "$U(1)$" connection.** A complex-valued 1-form $\omega \in \Omega^1(M, \mathbb{C})$ that is *not* purely imaginary corresponds to a connection on a complex line bundle that is *not* hermitian — parallel transport would not preserve $|\psi|^2$, breaking probability conservation. Physically meaningless for quantum mechanics.

**Corollary (gauge-invariance of $|\psi|^2$).** Under a gauge transformation $\psi \to e^{(ie/\hbar)f}\psi$, the probability density $|\psi|^2 = \bar\psi\psi$ is invariant: $|e^{(ie/\hbar)f}\psi|^2 = |\psi|^2$. So observable probability densities, and hence all measurement outcomes, are gauge-invariant — as physics demands.

**Corollary (Bianchi identity gives homogeneous Maxwell equations).** $dF = d(dA) = 0$ is the Bianchi identity $d_\nabla\theta = 0$ for the EM curvature. In components, $\partial_{[\lambda}F_{\mu\nu]} = 0$, equivalently the homogeneous Maxwell equations $\nabla \cdot B = 0$ (no magnetic monopoles) and $\nabla \times E = -\partial_t B$ (Faraday's law). These are *automatic* for any field strength derived as $F = dA$ — they are not equations of motion but identities.

**Corollary (covariant derivative satisfies Leibniz).** For $f \in C^\infty(M)$ and section $\psi$: $\nabla_\mu(f\psi) = (\partial_\mu f)\psi + f\nabla_\mu\psi$. This means functions on $M$ (uncharged) differentiate normally; the covariant piece only appears for sections of $L$ (charged objects).

**Corollary (holonomy around a closed loop).** The holonomy of the EM connection around a closed loop $\gamma$ is $\exp(-\oint_\gamma\omega) = \exp((ie/\hbar)\oint_\gamma A) = \exp((ie/\hbar)\int_\Sigma F)$ where $\Sigma$ is any surface with $\partial\Sigma = \gamma$ (when such a surface exists). This is the **Wilson loop**, the gauge-invariant phase a charged particle picks up traversing $\gamma$.

**Calibration check.** (1) Verify directly that $\omega = -(ie/\hbar)A$ is anti-hermitian: $\omega^* = (-ie/\hbar A)^* = (ie/\hbar)A = -\omega$, using that $A$ is real. (2) Compute the covariant Laplacian $\nabla_\mu\nabla^\mu\psi$ in flat spacetime — answer: $(\partial_\mu - (ie/\hbar)A_\mu)(\partial^\mu - (ie/\hbar)A^\mu)\psi$, which expands to $\Box\psi - (ie/\hbar)(\partial_\mu A^\mu + A^\mu\partial_\mu)\psi - 2(ie/\hbar)A^\mu\partial_\mu\psi - (e^2/\hbar^2)A_\mu A^\mu\psi$. (3) Check that the change-of-frame law $A \to A + df$ leaves $F = dA$ invariant: $F \to d(A + df) = dA + d^2f = dA + 0 = F$.

---

# Unlocked by This

> [!tip] Minimal Coupling as Geometry *(from Quantum Field Theory)*
> The prescription "replace $\partial_\mu$ by $D_\mu = \partial_\mu - (ie/\hbar)A_\mu$" to couple any field theory to electromagnetism, called **minimal coupling**, is the universal recipe of QED, QCD, and the Standard Model. Geometrically it is just "replace ordinary differentiation by covariant differentiation in the relevant bundle". Generalizing to non-abelian $G$, the prescription becomes $D_\mu = \partial_\mu + A_\mu^a T^a$ with $T^a$ generators of $\mathfrak{g}$ — exactly the structure of the Standard Model. The gauge principle "matter fields have a local symmetry $G$, and the gauge field is the connection on the principal $G$-bundle" is the organizing principle of all of fundamental physics.

> [!tip] Lattice Gauge Theory and Wilson Loops *(from Mathematical Physics)*
> Discretizing a $U(1)$ gauge theory on a spacetime lattice, the connection 1-form becomes a $U(1)$ "link variable" $U_{xy} = e^{ia A_\mu(\hat x)}$ on each edge of the lattice (parallel transport from $x$ to neighbouring $y$, lattice spacing $a$). The curvature becomes the **plaquette variable** $U_{\square} = \prod_{\text{edges in plaquette}} U_{xy}$ around each elementary square. The Wilson loop around any closed lattice path is gauge-invariant and gives the lattice version of $\exp((ie/\hbar)\oint A)$. This is the foundation of **lattice gauge theory**, the only known non-perturbative approach to QCD and the basis of modern computational particle physics.

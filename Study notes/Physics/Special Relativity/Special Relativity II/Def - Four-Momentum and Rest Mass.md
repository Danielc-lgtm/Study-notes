---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Four-Vector"
  - "Def - Classification of Four-Vectors"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

Natural units, $c = 1$ (factors of $c$ restored where the Newtonian comparison is the point). The Minkowski metric is $\eta_{\mu\nu} = \operatorname{diag}(+1,-1,-1,-1)$, inner product $A\cdot B = A^0B^0 - \mathbf{A}\cdot\mathbf{B}$. A particle has [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu = \gamma(c,\mathbf{u})$, with $\mathbf{u}$ its three-velocity, $u$ its speed, $\gamma = (1-u^2/c^2)^{-1/2}$. The four-momentum is $P^\mu$, rest mass $m$, total energy $E$, relativistic three-momentum $\mathbf{p}$. The full registry is on [[Special Relativity II — Relativistic Kinematics and Dynamics]].

---

# Axiom Motivation

Newtonian mechanics has two pillars in its analysis of interacting particles: conservation of momentum $\mathbf{p} = m\mathbf{u}$ and conservation of mass $\sum m$. These are *not* arbitrary — they are what make collisions, decays, and the whole study of particle dynamics tractable. We want their relativistic replacements, and the desideratum is sharp: we need a quantity that is (i) **conserved** in interactions with no external force, (ii) a genuine **four-vector**, so that the conservation law is the same in every inertial frame, and (iii) reduces to the Newtonian momentum $m\mathbf{u}$ at low speed, so we have not thrown away nineteenth-century physics.

Start from what we already have. [[Def - Four-Velocity and Four-Acceleration|The four-velocity]] $U^\mu = \gamma(c,\mathbf{u})$ is a four-vector, and at low speed its spatial part $\gamma\mathbf{u}\approx\mathbf{u}$ is the Newtonian velocity. To build a momentum we want to multiply by mass. But which mass, and is it allowed? Here is the constraint: the result must still be a four-vector, so we may only multiply $U^\mu$ by a **Lorentz scalar**. A frame-dependent quantity would spoil the transformation law. So we need a notion of mass that is an invariant.

There is exactly one natural candidate. Take the Newtonian definition of mass — the ratio of applied force to acceleration — but apply it only in the one frame where the particle is *at rest*. Every observer can agree to perform this measurement in the particle's own rest frame, so the number obtained is the same for all: it is frame-independent by construction. Call it the **rest mass** $m$. It is a Lorentz scalar, intrinsic to the particle. (The older literature also defined a "relativistic mass" $\gamma m$, frame-dependent, but as we will see this is just the energy in disguise and carries no new information; modern usage reserves "mass" for the invariant $m$.)

Now the definition is forced: $P^\mu = mU^\mu$, the rest mass times the four-velocity. It is a four-vector because $m$ is a scalar and $U^\mu$ a four-vector. Its spatial part is $\mathbf{p} = \gamma m\mathbf{u}$, which reduces to $m\mathbf{u}$ as $u\to 0$, satisfying desideratum (iii). And — this is the deep payoff, established in [[Thm - Conservation of Four-Momentum|the conservation theorem]] — *this* is the quantity that experiment shows to be conserved. Note what desideratum (i) costs us: relativistic momentum is $\gamma m\mathbf{u}$, not $m\mathbf{u}$. The extra $\gamma$ is not optional decoration; without it the quantity is not conserved and is not a four-vector component.

One more thing comes for free, and it is the most important consequence. The four-velocity is normalised, $U\cdot U = c^2$. Multiplying by $m^2$, the four-momentum satisfies
$$P\cdot P = m^2 c^2.$$
This single invariant constraint ties together all four components of $P^\mu$. Writing $P^\mu = (E/c,\mathbf{p})$ — anticipating that the time component will turn out to be the energy — it reads $E^2/c^2 - \mathbf{p}^2 = m^2c^2$, the energy–momentum relation. The constraint is why a four-momentum, despite having four components, still describes only three independent degrees of freedom, and it is the workhorse identity of every collision calculation: whenever a four-momentum can be isolated, squaring it yields the known number $m^2c^2$.

Why insist the rest mass be the *invariant* one rather than working with $\gamma m$? Because a conservation law must be frame-independent to be a law at all. If "mass" meant $\gamma m$, the conserved object would have a frame-dependent definition, and "conservation of mass" would hold in one frame and fail in another — useless. The rest mass is the invariant, the four-momentum built from it is a four-vector, and only then is its conservation a genuine law.

---

# The Definition

Let a particle move on a timelike worldline through Minkowski space with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu$.

**Rest mass.** The **rest mass** (or **invariant mass**) $m$ of the particle is its mass as measured in the inertial frame in which it is instantaneously at rest — operationally, the ratio of an applied force to the resulting acceleration in that frame. Because the defining measurement is always carried out in the particle's own rest frame, $m$ is a **Lorentz scalar**: every inertial observer assigns the particle the same rest mass. In modern usage, "mass" without qualification means rest mass.

**Four-momentum.** The **four-momentum** (or **energy–momentum four-vector**) of the particle is the rest mass times the four-velocity:
$$P^\mu \;=\; m\,U^\mu.$$
Since $m$ is a scalar and $U^\mu$ a [[Def - Four-Vector|four-vector]], $P^\mu$ is a four-vector: under a [[Def - The Lorentz Transformation|Lorentz transformation]] $\Lambda$, $P^\mu\to\Lambda^\mu{}_\nu P^\nu$. In an inertial frame where the particle has speed $u$ and $\gamma = (1-u^2/c^2)^{-1/2}$, its components are
$$P^\mu \;=\; m\gamma\,(c,\ \mathbf{u}) \;=\; \big(m\gamma c,\ m\gamma\mathbf{u}\big).$$

**Energy and three-momentum.** The components of the four-momentum are named:
$$P^\mu \;=\; \Big(\frac{E}{c},\ \mathbf{p}\Big),\qquad E \;=\; \gamma m c^2 \quad\text{(total energy)},\qquad \mathbf{p} \;=\; \gamma m\,\mathbf{u}\quad\text{(relativistic three-momentum)}.$$
The identification of the time component with the energy is justified by [[Thm - Mass-Energy Equivalence|mass–energy equivalence]] and by the fact that it is the conserved quantity associated with time-translation invariance.

---

# The Mass-Shell Relation

The normalisation $U\cdot U = c^2$ of the four-velocity becomes a constraint on the four-momentum:
$$P\cdot P \;=\; \eta_{\mu\nu}P^\mu P^\nu \;=\; m^2 c^2,$$
equivalently, in components,
$$E^2 \;=\; \mathbf{p}^2 c^2 + m^2 c^4.$$
The four-momentum of a massive particle is therefore a future-pointing **timelike** four-vector whose Minkowski length is fixed by the rest mass — every particle's four-momentum lies on the **mass shell**, the hyperboloid $P\cdot P = m^2c^2$. (For a massless particle, $m = 0$ and $P^\mu$ is **null**: see [[Def - The Four-Momentum of a Photon]].)

---

# Relate to Other Fields / Compression

In [[Multivariate Analysis I — Differentiation in Several Variables|geometric mechanics]], the four-momentum is the **canonical momentum conjugate to the four-position**. A free relativistic particle has the action $S = -mc^2\int d\tau = -mc\int\sqrt{\eta_{\mu\nu}\dot X^\mu\dot X^\nu}\,d\lambda$, and the momentum conjugate to $X^\mu$, namely $P_\mu = \partial L/\partial\dot X^\mu$, evaluates to exactly $mU_\mu$ — the four-momentum with a lowered index. A reader who knows Hamiltonian mechanics will recognise the mass-shell relation $P\cdot P = m^2c^2$ as a **primary constraint**: the relativistic free particle is a constrained Hamiltonian system, the constraint surface is the mass shell, and the constraint itself generates reparametrisations of the worldline. The same constraint, promoted to an operator equation $\hat P\cdot\hat P\,\psi = m^2c^2\,\psi$, is the Klein–Gordon equation of relativistic quantum mechanics.

The phrase "rest mass" rather than just "mass" is a deliberate break with an older convention. Early relativity texts wrote $E = mc^2$ with $m = \gamma m_0$ the "relativistic mass" and $m_0$ the "rest mass", so that momentum stayed $\mathbf{p} = m\mathbf{u}$ and the Newtonian formulae looked preserved. This is internally consistent but obscures the structure: "relativistic mass" is nothing but $E/c^2$, so it is energy under another name and contributes no independent concept, while the genuinely invariant, frame-independent, particle-intrinsic quantity is the rest mass. The modern convention — *mass means rest mass, full stop; energy is a separate, frame-dependent quantity* — is the one that makes the four-vector structure transparent and is used throughout these notes.

---

# Examples / Corollaries

**Is an instance — a particle at rest.** With $\mathbf{u}=0$, $\gamma=1$: $P^\mu = (mc,\mathbf{0})$, so $E = mc^2$ and $\mathbf{p}=\mathbf{0}$. The mass-shell relation gives $P\cdot P = m^2c^2$, trivially. A particle at rest still has energy — its rest energy $mc^2$.

**Is an instance — a fast electron.** An electron ($m c^2\approx 0.511$ MeV) moving at $u$ with $\gamma = 10$ has $E = 10\,mc^2\approx 5.11$ MeV and $|\mathbf{p}| = \gamma m u \approx \gamma m c = 10\,mc$ (since $u\approx c$). Check: $E^2 - \mathbf{p}^2c^2 = 100\,m^2c^4 - (\gamma^2 m^2 u^2)c^2 = m^2c^4(100 - \gamma^2u^2/c^2) = m^2c^4\,\gamma^2(1-u^2/c^2)\cdot\ldots$ — works out to $m^2c^4$, the invariant.

**Is NOT an instance — the Newtonian momentum $m\mathbf{u}$.** The triple $m\mathbf{u}$ is not the spatial part of any four-vector: it is missing the factor $\gamma$. It is the $u\to 0$ limit of the true momentum $\gamma m\mathbf{u}$, and using it relativistically violates conservation and the transformation law. As $u\to c$ it stays finite at $mc$, whereas the true $|\mathbf{p}| = \gamma mu$ diverges — and the divergence is what enforces the speed limit.

**Is NOT an instance — a photon's four-momentum via $P = mU$.** A photon has $m = 0$ and no four-velocity, so $P^\mu = mU^\mu$ is the indeterminate $0\cdot\infty$. The photon's [[Def - The Four-Momentum of a Photon|four-momentum]] exists but must be defined another way; it is null, $P\cdot P = 0$, not timelike.

**Corollary — energy and momentum diverge as $u\to c$.** Both $E = \gamma mc^2$ and $|\mathbf{p}| = \gamma mu$ contain $\gamma\to\infty$ as $u\to c$. So accelerating a massive particle to light speed would require infinite energy and impart infinite momentum: **no massive particle can reach $c$.** The speed limit is a consequence of the four-momentum's structure, not a separate postulate.

**Corollary — the kinetic energy is $(\gamma-1)mc^2$.** The total energy minus the rest energy is $T = E - mc^2 = (\gamma-1)mc^2$. Taylor-expanding, $T = \tfrac12 mu^2 + \tfrac38 mu^4/c^2 + \cdots$, so the leading term is the Newtonian kinetic energy and the rest are relativistic corrections — see [[Thm - Mass-Energy Equivalence]].

**Calibration check.** Verify $P\cdot P = m^2c^2$ from the components $(m\gamma c, m\gamma\mathbf{u})$; verify that $E^2 = \mathbf{p}^2c^2 + m^2c^4$ is the same statement; check that $\mathbf{p}/E = \mathbf{u}/c^2$, so the velocity is recovered as $\mathbf{u} = \mathbf{p}c^2/E$; and confirm that as $m\to 0$ at fixed $E$, the relation collapses to $E = |\mathbf{p}|c$. If you can explain why $P^\mu$ has four components but only three are independent, you have understood the definition.

---

# Unlocked by This

> [!tip] Mass–Energy Equivalence *(from this topic)*
> Expanding the time component $E = \gamma mc^2$ in powers of $u/c$ reveals the rest energy $mc^2$, the Newtonian kinetic energy, and relativistic corrections. The invariant $P\cdot P = m^2c^2$ is the energy–momentum relation $E^2 = \mathbf{p}^2c^2 + m^2c^4$ — see [[Thm - Mass-Energy Equivalence]].

> [!tip] Conservation of Four-Momentum *(from this topic)*
> The four-momentum is the quantity conserved in interactions with no external force; [[Thm - Conservation of Four-Momentum|its conservation]] replaces and unifies the Newtonian conservation of mass and of energy.

> [!tip] The Energy–Momentum Tensor *(from General Relativity and Continuum Mechanics)*
> For a continuous medium the single four-momentum $P^\mu$ is replaced by the **energy–momentum tensor** $T^{\mu\nu}$, the flux of four-momentum across surfaces. Its conservation $\partial_\mu T^{\mu\nu} = 0$ is the local form of four-momentum conservation, and it is the source of gravity in Einstein's equations.

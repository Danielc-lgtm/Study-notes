---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Lie Group"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - Differential k-Form on a Manifold"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

Throughout, $M$ is a (pseudo-)Riemannian 4-manifold and $E \to M$ is a vector bundle whose fibre $\mathbb{R}^N$ (or $\mathbb{C}^N$) carries a representation of a Lie group $G$. The "field" $\phi$ is a smooth section of $E$, locally an $N$-tuple of functions $\phi^a(x)$, $a = 1, \dots, N$. A Lagrangian density $\mathcal{L}$ is a scalar function of $\phi$, $\partial_\mu\phi$ (or covariant derivative $\nabla_\mu\phi$), and the spacetime point $x$.

An **internal symmetry** is one that acts only on the fibre coordinates $\phi^a$ — leaving the spacetime point $x$ fixed — as opposed to an *external* symmetry, which moves spacetime points (translations, rotations, Lorentz transformations). The contrast is the same as that between a "passive" change of field variables and an "active" diffeomorphism of $M$.

For a 1-parameter subgroup $g(\alpha) = e^{\alpha E}$ of $G$ with generator $E \in \mathfrak{g}$, the symmetry transformation is $\phi \to g(\alpha)\phi$, and the infinitesimal variation is $\delta\phi^a = E^a{}_b\,\phi^b$, where $E^a{}_b$ are the matrix entries of $E$ in the representation.

The Lie algebra index conventions match [[Gauge Theory III — Connections in Principal and Associated Bundles]].

---

# Axiom Motivation

Conservation laws and continuous symmetries are tied together by one of the deepest facts of physics: **every continuous symmetry of a Lagrangian produces a conserved current**, and the conservation law is computable explicitly in terms of the generator of the symmetry. This is **Noether's first theorem** (1918), and the object the theorem produces is the *Noether current*. The job of the definition is to extract, from a generator $E$ of an internal symmetry, the specific vector field $J^\mu$ whose divergence vanishes on shell.

Two motivating questions clarify what the definition must accomplish. *First*, why should there be any such current at all? The answer is the variational identity. The first variation of the action $\delta S = \int_M (\delta\mathcal{L}/\delta\phi^a)\,\delta\phi^a\, d^4x + \text{boundary terms}$ always splits into a "bulk" piece proportional to the Euler–Lagrange equations and a "boundary" piece coming from the partial integration. For *any* variation $\delta\phi$, the boundary piece is $\int_{\partial U} N_\mu (\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\,\delta\phi^a\, dS$. Now suppose $\delta\phi$ is a *symmetry variation* — one that leaves $\mathcal{L}$ pointwise invariant (so $\delta\mathcal{L} = 0$). Then for a solution $\phi$ (on which the bulk piece vanishes), the boundary piece must equal $\int_{\partial U}\delta\mathcal{L}\,d^4x = 0$ for *every* region $U$. Since this holds for arbitrary $U$, the integrand $\partial_\mu[(\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\,\delta\phi^a]$ must vanish pointwise. That bracketed expression is precisely the Noether current $J^\mu$.

*Second*, why is the current built from $(\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\,\delta\phi^a$ specifically? The factor $\partial\mathcal{L}/\partial(\partial_\mu\phi^a)$ is the *canonical momentum conjugate to $\phi^a$* (in the $\mu$-th direction). The Noether current contracts the canonical momentum with the direction of the symmetry variation: $J^\mu = p^{\mu a}\,\delta\phi_a$. Geometrically, $J$ is the pullback of the symplectic potential under the symmetry-vector-field on the space of fields. This is why the *form* of the Noether current — not just its existence — is fixed.

The choice to focus on *internal* rather than external symmetries is one of relative simplicity. External symmetries (translations, rotations) also yield conserved currents (energy-momentum tensor, angular momentum), but the derivation involves the Lie derivative of the field with respect to a spacetime vector field, picking up additional boundary terms from the deformation of the integration region. Internal symmetries — phase rotations of $\psi$, isospin rotations of the nucleon doublet, colour rotations of the quark triplet — produce currents directly from the variation of the field, with no spacetime gymnastics. The fundamental forces (electromagnetic, weak, strong) are all sourced by *internal*-symmetry currents, so this case alone covers most of physics.

Why not define the current without reference to a particular generator $E$? Because the conservation law is one equation per independent generator: a $k$-dimensional Lie algebra of internal symmetries produces $k$ independent conserved currents, one for each basis element. The choice to package the current as $J^\mu_E$, indexed by the generator $E$, is the cleanest way to handle non-abelian internal-symmetry groups, where the full current is naturally Lie-algebra-valued: $J^\mu = J^\mu_a\, T^a$ with $T^a$ a basis of $\mathfrak{g}$. For $G = U(1)$ the algebra is one-dimensional and the index $a$ disappears, recovering the electromagnetic current $J^\mu = -e\bar\psi\gamma^\mu\psi$ as a single 4-vector.

---

# The Definition

Let $\mathcal{L}(\phi, \partial\phi)$ be a Lagrangian density for a field $\phi^a$ (section of a vector bundle $E \to M$), and let $E \in \mathfrak{g}$ be a generator of a 1-parameter subgroup $g(\alpha) = e^{\alpha E}$ of an internal-symmetry group $G$, acting on $\phi$ by $\phi \to g(\alpha)\phi$. The **Noether current** associated to $E$ is the vector field $J = J^\mu \partial_\mu$ on $M$ with components

$$J^\mu = \frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi^a)}\,\delta\phi^a = \frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi^a)}\,E^a{}_b\,\phi^b.$$

Equivalently, $J^\mu$ is the canonical momentum conjugate to $\phi^a$ in the $\mu$-th direction, contracted with the infinitesimal symmetry variation $\delta\phi^a = E^a{}_b\,\phi^b$.

If $g_{\mu\nu}$ is a metric on $M$ and one wishes to write the current as a $(d-1)$-form rather than a vector field, one defines $\star J = \iota_J\,\operatorname{vol}_g$; this is the form whose integral over a 3-dimensional spatial slice computes the conserved charge $Q = \int_{V^3}\star J$.

For a non-abelian internal-symmetry group $G$ with basis $\{T^a\}$ of $\mathfrak{g}$, one defines a current for each generator: $J^\mu_a = (\partial\mathcal{L}/\partial(\partial_\mu\phi^b))(T^a)^b{}_c\,\phi^c$. The collection $\{J^\mu_a\}$ assembles into a single $\mathfrak{g}^*$-valued (or, using the trace pairing, $\mathfrak{g}$-valued) current.

---

# Relate to Other Fields / Compression

This is the *internal-symmetry* version of the broader **Noether construction**, which associates a conserved current to any continuous symmetry of an action — internal or external, global or local. The Lie-algebra perspective unifies both cases: the symmetry generators form a Lie algebra $\mathfrak{g}$, and each generator $E \in \mathfrak{g}$ produces a current $J_E$. The map $E \mapsto J_E$ is linear, and the Poisson brackets of the currents (in the Hamiltonian framework) reproduce the Lie bracket of $\mathfrak{g}$ — the "current algebra" structure that underlies non-abelian gauge theory and chiral models.

The construction has direct analogues in classical mechanics, where it becomes the **momentum map** of symplectic geometry. For a Lie group $G$ acting on a symplectic manifold $(P, \omega)$ in a Hamiltonian way (preserving $\omega$), the **momentum map** $\mu : P \to \mathfrak{g}^*$ sends each phase-space point to a linear functional on $\mathfrak{g}$ whose value on a generator $E$ is the Hamiltonian function generating that symmetry. Conservation of $J_E$ in field theory is the field-theoretic version of conservation of $\langle \mu, E\rangle$ in classical mechanics — both reduce to the statement that the Hamiltonian flow of an invariant function preserves the level sets of the momentum map. See [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]] for the finite-dimensional picture.

**True name:** the Noether current is the *canonical momentum contracted with the symmetry variation*. The operational form is $J^\mu = p^\mu_a\,\delta\phi^a$, where $p^\mu_a = \partial\mathcal{L}/\partial(\partial_\mu\phi^a)$ is the canonical momentum and $\delta\phi^a$ is the infinitesimal symmetry transformation. This is what you actually reach for when computing a current — you do not start from the divergence-free property; you start from the canonical momentum, contract with the symmetry direction, and verify divergence-freeness at the end. This form also makes manifest why the current depends linearly on the symmetry generator: the symmetry variation does.

---

# Examples / Corollaries

**Example 1 — The electromagnetic current as the $U(1)$ Noether current.** Take $\mathcal{L} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$, the free Dirac Lagrangian. The global symmetry $\psi \to e^{i\alpha}\psi$, $\bar\psi \to e^{-i\alpha}\bar\psi$ has generator $E = i$ on $\psi$ and $E = -i$ on $\bar\psi$. The canonical momentum is $\partial\mathcal{L}/\partial(\partial_\mu\psi) = i\bar\psi\gamma^\mu$, and $\delta\psi = i\psi$, so $J^\mu = (i\bar\psi\gamma^\mu)(i\psi) = -\bar\psi\gamma^\mu\psi$. Including the electron charge factor $-e$, one obtains $J^\mu = -e\bar\psi\gamma^\mu\psi$, the **electric four-current**. The conserved charge $Q = \int_{V^3}J^0\, d^3x = -e\int\psi^\dagger\psi\, d^3x$ is the total electric charge in the volume $V^3$, and its constancy in time is *electric charge conservation*.

**Example 2 — The isospin current for the Heisenberg nucleon.** Take $\mathcal{L} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ for $\psi = (p, n)^T$ a doublet of Dirac spinors, with $SU(2)$ acting on the doublet structure. For the generator $\sigma_a/2$ (with $\sigma_a$ a Pauli matrix), $\delta\psi = (i\sigma_a/2)\psi$, and $J^\mu_a = -\bar\psi\gamma^\mu(\sigma_a/2)\psi$ — the **isospin current**. There are three of these, one per Pauli matrix, and their Poisson-bracket algebra reproduces the $\mathfrak{su}(2)$ Lie algebra: $\{Q_a, Q_b\} = \epsilon_{abc}Q_c$. The conserved charges $Q_a$ are the isospin quantum numbers.

**Example 3 — Translation as an "external" symmetry: the energy–momentum tensor (NOT a pure-internal example).** Translation $x^\mu \to x^\mu + a^\mu$ is an external symmetry. Although the *form* of the Noether construction works the same way, the variation $\delta\phi = -a^\nu\partial_\nu\phi$ involves a spacetime derivative, producing the **energy–momentum tensor** $T^{\mu\nu} = (\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\partial^\nu\phi^a - \eta^{\mu\nu}\mathcal{L}$. This is *not* an instance of "internal Noether current" — it is its external cousin. The distinction matters because internal-symmetry currents do not pick up the $-\eta^{\mu\nu}\mathcal{L}$ term, while external ones do.

**Non-example — A *non-symmetry* generates no conserved current.** Take the same Dirac Lagrangian and consider the *non-symmetric* transformation $\psi \to e^{i\alpha\sigma_3}\psi$, where $\sigma_3$ is the third Pauli matrix acting on a hypothetical doublet structure that the Lagrangian does *not* respect. The would-be current $J^\mu = -\bar\psi\gamma^\mu\sigma_3\psi$ exists as a vector field but is *not divergence-free* — applying the equations of motion shows $\partial_\mu J^\mu \neq 0$ generically. This is the reason the symmetry hypothesis on $\mathcal{L}$ is essential: divergence-freeness is precisely the on-shell consequence of invariance of $\mathcal{L}$ under $\delta\phi$.

**Calibration check.** A reader who has internalised the definition should be able to: (a) compute the electromagnetic current for the *complex scalar* Lagrangian $\mathcal{L} = |\partial\phi|^2 - m^2|\phi|^2$, obtaining $J^\mu = i(\phi^*\partial^\mu\phi - \phi\partial^\mu\phi^*)$ from the $U(1)$ symmetry $\phi \to e^{i\alpha}\phi$; (b) explain why the current associated to the *constant* shift $\phi \to \phi + c$ of a *massive* scalar Lagrangian fails to be conserved — the mass term $m^2|\phi|^2$ is not invariant, so the hypothesis fails; (c) name two currents for the non-abelian $SU(2)$ isospin symmetry of the nucleon doublet (one per Pauli matrix), and state that their commutator-algebra reproduces $\mathfrak{su}(2)$.

---

# Unlocked by This

> [!tip] Symplectic Reduction *(from Geometric Mechanics)*
> The Noether-current construction is the field-theoretic version of the **momentum map** $\mu : P \to \mathfrak{g}^*$ in symplectic geometry. Given a Hamiltonian $G$-action on $(P, \omega)$, the level sets $\mu^{-1}(c)$ for $c \in \mathfrak{g}^*$ are preserved by the dynamics, and the **Marsden–Weinstein quotient** $\mu^{-1}(c)/G_c$ is a smaller symplectic manifold encoding the reduced dynamics. In gauge theory, the analogous reduction quotients the space of connections by gauge transformations, giving the gauge-orbit moduli space $\mathcal{A}/\mathcal{G}$ — the natural arena for instanton moduli spaces and Donaldson theory. See [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

> [!tip] Current Algebra and Chiral Symmetry Breaking *(from Quantum Field Theory)*
> When the Noether construction is applied to non-abelian global symmetries in field theory, the conserved currents $J^\mu_a$ satisfy an algebra of equal-time commutators reproducing the Lie algebra of the symmetry group: $[J^0_a(x), J^0_b(y)]|_{x^0=y^0} = i f_{ab}{}^c\,J^0_c(x)\,\delta^3(x-y)$. This is the **current algebra** of Gell-Mann (1962), which in QCD provides one of the few rigorous handles on non-perturbative dynamics — sum rules (Adler–Weisberger), the **Goldberger–Treiman relation**, **partially conserved axial current** (PCAC). The phenomenon of **spontaneous chiral symmetry breaking** — where the QCD vacuum spontaneously breaks the chiral $SU(N_f) \times SU(N_f)$ symmetry of massless quarks down to vector $SU(N_f)$, producing massless **Goldstone bosons** (the pions) — is one of the most important non-perturbative facts about the strong interaction, and is detected via the Noether currents.

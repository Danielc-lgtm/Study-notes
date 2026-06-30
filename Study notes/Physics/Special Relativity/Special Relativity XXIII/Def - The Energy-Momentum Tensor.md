---
type: definition
subject: special-relativity
prereqs:
  - "Def - Tensors on Minkowski Space"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ except where a formula is more recognisable with $c$ restored, in which case both forms are given. The signature is **mostly minus**, $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector has $X \cdot X > 0$ and a four-velocity satisfies $U \cdot U = 1$ (with $c$: $U \cdot U = c^2$). Greek indices $\mu,\nu,\alpha,\beta$ run over $0,1,2,3$; Latin indices $i,j$ over the spatial $1,2,3$. An observer is a future-pointing timelike unit worldline; $U_0$ is its [[Def - Four-Velocity and Four-Acceleration|four-velocity]], $\mathcal{E}_{U_0} = U_0^\perp$ its [[Def - Observer and Local Rest Space|local rest space]], and $(U_0, \mathbf{e}_i)$ an orthonormal local frame with dual basis $(e^\mu)$. The orthogonal projector onto the rest space is $\perp_{U_0}(X) = X - (X \cdot U_0)\,U_0$. The symbol $T$ denotes the energy-momentum tensor; $T_{\mu\nu}$ its components; $T^{\mu\nu} = \eta^{\mu\alpha}\eta^{\nu\beta}T_{\alpha\beta}$ the fully raised components. Full registry on [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!warning] Convention
> Gourgoulhon, the source for this chapter, uses the opposite signature $\mathrm{diag}(-1,+1,+1,+1)$ ("mostly plus"), in which a four-velocity has $\mathbf{u}\cdot\mathbf{u} = -1$. Every formula transcribed here has had its overall metric sign flipped to our mostly-minus convention. The component matrix $T_{\mu\nu}$ of energy density / momentum density / stress is **unchanged** by the signature flip — it is a table of physically measured quantities relative to an observer — but the *trace* term $\eta^{\mu\nu}$ in any tensor built from the metric (such as the electromagnetic $T^{\mu\nu}$ on [[Def - Energy-Momentum Tensor of the Electromagnetic Field]]) flips sign with the metric, so be vigilant.

---

# Axiom Motivation

By the end of relativistic particle dynamics we know how to track a handful of particles: each carries a [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = mU$, and the total four-momentum of an isolated collection is conserved. But a litre of gas contains of order Avogadro's number of particles, a magnetic field fills a region with no particles at all, and a star is a continuous ball of fluid. We need an object that describes the energy and momentum of *continuous* matter and of *fields* — something that, region by region, tells us how much energy is there, how much momentum, and how that momentum is flowing. The energy-momentum tensor is that object, and the way to invent it is to ask what a single number — the energy in a region — must generalise to.

Start from what we want to measure. Pick an observer with four-velocity $U_0$ and a small chunk of their rest space of volume $\mathrm{d}V$. Three quantities are physically meaningful. First, the **energy** $\mathrm{d}E$ contained in the chunk, hence an energy density $\varepsilon = \mathrm{d}E/\mathrm{d}V$. Second, the **momentum** $\mathrm{d}\mathbf{P}$ contained in it, hence a momentum density. Third — and this is the part that has no Newtonian-particle analogue — the **stress**: the rate at which momentum flows across each face of the chunk, which is exactly the force per unit area, the pressure and shear that one part of a medium exerts on the adjacent part. A gas has pressure even when its bulk momentum is zero; that pressure is momentum crossing surfaces, and it must be in the bookkeeping.

Now count what kind of mathematical object carries all of this. Energy density is one number. Momentum density is three numbers (a spatial vector). Stress is a $3\times 3$ matrix $S_{ij}$ — the $i$-th component of force per unit area on a surface whose normal is the $j$-th direction. That is $1 + 3 + 3 + 9$ pieces of data, and they are not independent objects floating side by side: they must assemble into something that transforms correctly under a change of observer, because what one observer calls "energy density" another calls a mix of energy density, momentum, and stress (just as one observer's electric field is another's mix of electric and magnetic). The only structure with exactly $4\times 4 = 16$ components that transforms with two factors of the Lorentz matrix is a rank-two [[Def - Tensors on Minkowski Space|tensor]]. So the desideratum "package energy density, momentum density, and stress into one frame-covariant object" forces a rank-two tensor on us. We write its components, in the observer's local frame, as the matrix
$$
T_{\mu\nu} = \begin{pmatrix} \varepsilon & -\,\varphi_1/c & -\,\varphi_2/c & -\,\varphi_3/c \\ -\,c\,\varpi_1 & S_{11} & S_{12} & S_{13} \\ -\,c\,\varpi_2 & S_{21} & S_{22} & S_{23} \\ -\,c\,\varpi_3 & S_{31} & S_{32} & S_{33} \end{pmatrix},
$$
where $\varepsilon$ is the energy density, $\varpi_i$ the momentum density, $\varphi_i$ the energy-flux density, and $S_{ij}$ the stress. The entire content of the definition is: *each of these measured quantities is obtained by feeding the observer's four-velocity and frame vectors into one bilinear form $T$.*

Why a *bilinear form* — a tensor with two slots — and not, say, a vector? Because the data we want is intrinsically two-index. The energy density is "the energy seen by $U_0$, flowing in the $U_0$ direction": two appearances of $U_0$. The stress $S_{ij}$ is "the $i$-momentum crossing the surface with normal $j$": two spatial directions. A vector (one slot) could carry energy and momentum — that is the four-momentum of a single particle — but it cannot carry stress, because stress is a relation between two directions (which momentum, across which surface). The jump from particle to medium is precisely the jump from a one-slot object ($P^\mu$) to a two-slot object ($T^{\mu\nu}$).

The cleanest frame-independent way to pin the definition down is through a flux. Recall that the electric charge in a region is the flux of the [[Def - The Electric Four-Current|electric four-current]] $J$ through a hypersurface: charge is a *scalar*, so it is the flux of a *vector*. Here the conserved quantity is the total four-momentum $\mathbf{p}$ on a hypersurface, which is a *vector* (four numbers, not one). A flux that produces a vector cannot be the flux of a vector field — it must be the flux of a *field of bilinear forms*. This is the deepest reason $T$ has the rank it has: it is the object whose flux through a hypersurface is the four-momentum crossing that hypersurface, exactly as $J$'s flux is the charge. We will see this is not optional — it is forced by demanding that the four-momentum, a vector, be conserved.

One axiom we have not yet justified is **symmetry**, $T_{\mu\nu} = T_{\nu\mu}$. It is not obvious: nothing in "energy density, momentum density, stress" demands the off-diagonal blocks match. What symmetry asserts is that the energy-flux density and the momentum density are the same vector up to a factor of $c^2$, $\boldsymbol{\varphi} = c^2\boldsymbol{\varpi}$, and that the stress matrix $S_{ij}$ is itself symmetric. Both are theorems, not assumptions: the first is the relativistic equivalence of mass and energy (energy flowing carries momentum; if energy density $\varepsilon$ moves with velocity $\mathbf{V}$ then it carries momentum density $\varepsilon\mathbf{V}/c^2$, which is exactly $\boldsymbol{\varphi}/c^2$), and the second follows from the conservation of angular momentum, as shown on [[Thm - Energy-Momentum Conservation]] and in the source. So symmetry is a derived property of *any* physical energy-momentum tensor — we record it as part of the definition because every $T$ we will meet has it, but it earns its place by proof, not by fiat.

What the definition must *exclude* is the temptation to treat $T$ like the metric. Both are symmetric bilinear forms, but the metric $g$ is non-degenerate (it defines lengths and angles), whereas $T$ can be degenerate — in particular, in a vacuum region with no matter and no field, $T = 0$ identically. A zero metric is meaningless; a zero energy-momentum tensor is just empty space. So $T$ is a symmetric bilinear form that is *allowed to vanish or to be degenerate*, and it does not define any geometry. It is a field — a different symmetric bilinear form at each event — sourced by whatever matter and radiation are present.

---

# The Definition

Let $\mathscr{S}$ be a physical system (continuous matter, a field, or a particle distribution). Its **energy-momentum tensor** $T$ is the field of symmetric bilinear forms on [[Def - Minkowski Space and the Metric|Minkowski space]] — a tensor field of type $(0,2)$ — characterised by the property that the total four-momentum of $\mathscr{S}$ on any oriented, non-null hypersurface $\mathscr{V}$ is the flux
$$
\mathbf{p}\big|_{\mathscr{V}} \;=\; \pm\,\frac{1}{c}\int_{\mathscr{V}} T(\,\cdot\,, \vec{n})\,\mathrm{d}V,
$$
where $\vec{n}$ is the unit normal compatible with the orientation of $\mathscr{V}$, the sign being $+$ where $\vec{n}$ is spacelike and $-$ where it is timelike. Equivalently, $T$ is the unique symmetric tensor whose contractions reproduce the quantities measured by an arbitrary observer $\mathcal{O}$ of four-velocity $U_0$ with orthonormal local frame $(U_0, \mathbf{e}_i)$:

- **Energy density:** $\displaystyle \varepsilon = T(U_0, U_0)$.
- **Momentum density** (a $1$-form in the rest space): $\displaystyle \varpi = -\frac{1}{c}\,T(\perp_{U_0}, U_0)$, i.e. $\varpi_i = -\tfrac{1}{c}T(\mathbf{e}_i, U_0)$.
- **Energy-flux density** (a $1$-form): $\displaystyle \varphi = -\,c\,T(U_0, \mathbf{e}_j)\,e^j$, giving the power $\mathrm{d}E/\mathrm{d}t = \langle \varphi, \vec n\rangle\,\mathrm{d}S$ crossing a surface of normal $\vec n$.
- **Stress tensor** (a bilinear form on the rest space): $\displaystyle S = T(\perp_{U_0}, \perp_{U_0})$, i.e. $S_{ij} = T(\mathbf{e}_i, \mathbf{e}_j)$, giving the force $\mathrm{d}\mathbf{F} = S(\,\cdot\,, \vec n)\,\mathrm{d}S$ on a surface of normal $\vec n$.

In the observer's frame these are the entries of the component matrix
$$
T_{\mu\nu} = \begin{pmatrix} \varepsilon & -c\,\varpi_1 & -c\,\varpi_2 & -c\,\varpi_3 \\ -c\,\varpi_1 & S_{11} & S_{12} & S_{13} \\ -c\,\varpi_2 & S_{12} & S_{22} & S_{23} \\ -c\,\varpi_3 & S_{13} & S_{23} & S_{33} \end{pmatrix},
$$
written here in its symmetric form, which uses the identity $\varphi = c^2\varpi$ (so the first row and first column agree up to the $1/c$ and $c$ factors). The frame-independent decomposition of $T$ with respect to the observer is
$$
T \;=\; \varepsilon\,U_0^\flat \otimes U_0^\flat \;+\; c\,\varpi \otimes U_0^\flat \;+\; c\,U_0^\flat \otimes \varpi \;+\; S,
$$
where $U_0^\flat = \eta(U_0, \cdot)$ is the $1$-form metric-dual to $U_0$; this is the **orthogonal decomposition** of the symmetric form $T$ relative to $\mathcal{O}$, valid for any symmetric tensor.

The **symmetry** $T(X,Y) = T(Y,X)$ holds for the energy-momentum tensor of every physical system; it is established in general from the conservation of angular momentum (see [[Thm - Energy-Momentum Conservation]]).

For a system of simple particles $(\mathscr{P}_a)$ with masses $m_a$, four-velocities $U_a$ and proper times $\tau_a$, the explicit form is
$$
T(M) \;=\; \sum_a m_a c^2 \int_{-\infty}^{+\infty} \delta_{A_a(\tau)}(M)\; U_a^\flat(\tau) \otimes U_a^\flat(\tau)\; c\,\mathrm{d}\tau,
$$
the sum of the world-tube contributions of the individual particles, $\delta_{A_a(\tau)}$ being the Dirac distribution on spacetime supported on the worldline of $\mathscr{P}_a$. In the continuum limit this becomes a smooth field, e.g. $T = \varepsilon_0\, U^\flat \otimes U^\flat$ for **pressureless dust** of proper energy density $\varepsilon_0$ and four-velocity field $U$.

---

# Categorical / Structural Definition

Structurally, the energy-momentum tensor lives in the same space as the metric: both are sections of the bundle $S^2 T^*\mathbb{M}$ of symmetric $(0,2)$-tensors over Minkowski space. The metric $\eta$ is a *distinguished, constant, non-degenerate* section — it is fixed background geometry. The energy-momentum tensor is a *variable, possibly degenerate* section — it is a dynamical field determined by the matter content. The map "matter configuration $\mapsto$ its $T$" is the fundamental coupling of physics to geometry: in special relativity $T$ is merely a convenient bookkeeping device, but in general relativity it becomes the *source* in the Einstein equation $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$, where the same symmetric $(0,2)$ slot that holds the geometry's curvature on the left holds the matter's energy-momentum on the right. The fact that both sides are symmetric $(0,2)$-tensors with vanishing divergence — $\nabla^\mu G_{\mu\nu} = 0$ identically (the contracted Bianchi identity), $\nabla^\mu T_{\mu\nu} = 0$ by [[Thm - Energy-Momentum Conservation|conservation]] — is not a coincidence: it is what makes the equation consistent.

There is a second structural reading, through the action principle. For a field theory with action $S[\phi, g]$ depending on the field $\phi$ and the metric $g$, the energy-momentum tensor is the **variational derivative of the action with respect to the metric**,
$$
T_{\mu\nu} \;=\; \frac{-2}{\sqrt{-g}}\,\frac{\delta S}{\delta g^{\mu\nu}},
$$
the *Hilbert* (or *metric*) energy-momentum tensor. This definition is manifestly symmetric (because $g^{\mu\nu}$ is) and manifestly the right object to couple to gravity. It also explains, via Noether's theorem applied to spacetime-translation symmetry, why $T$ is the *conserved current of translations*: energy conservation is invariance under time translation, momentum conservation is invariance under space translation, and the four-index object packaging both currents is exactly $T^{\mu\nu}$. The canonical Noether tensor obtained this way is not automatically symmetric and must be improved (Belinfante–Rosenfeld) to match the Hilbert tensor; the improvement terms are precisely those forced by angular-momentum conservation.

---

# Relate to Other Fields / Compression

The energy-momentum tensor is the relativistic completion of three separate Newtonian quantities that turn out to be facets of one object. In Newtonian continuum mechanics one carries a mass density $\rho$, a momentum density $\rho\mathbf{v}$, and a Cauchy stress tensor $\sigma_{ij}$ as logically distinct fields obeying distinct balance laws (mass continuity, momentum balance). Special relativity fuses them: $\rho$ (times $c^2$) is the $00$ component, $\rho\mathbf{v}$ is the $0i$ block, and $\sigma_{ij}$ is the $ij$ block of a single $T^{\mu\nu}$, and the separate Newtonian balance laws are the time and space components of the single equation $\nabla_\mu T^{\mu\nu} = 0$.

**True name:** the energy-momentum tensor is *the conserved Noether current of spacetime translations, packaged as the object whose flux through a hypersurface is the four-momentum crossing it.* This is more operational than the component matrix, because it tells you immediately (a) why it is conserved (translations are a symmetry), (b) why it has two indices (one for "which component of four-momentum", one for "across which surface"), and (c) how to compute it from a Lagrangian. When you meet a new field and need its $T$, do not try to read off energy density and stress by hand — vary the action with respect to the metric, or apply Noether to translations, and the symmetric conserved tensor falls out.

To a probabilist or kinetic theorist, $T^{\mu\nu}$ is the second moment of the one-particle distribution function $f(x,p)$ over momentum: $T^{\mu\nu}(x) = \int f(x,p)\,p^\mu p^\nu\, \tfrac{\mathrm{d}^3 p}{p^0}$. The number current $N^\mu = \int f\,p^\mu\,\mathrm{d}^3p/p^0$ is the first moment; $T^{\mu\nu}$ is the next. This is why the dust tensor is $\varepsilon_0 U^\mu U^\nu$ — a single delta-function in momentum at $p = mU$ gives $p^\mu p^\nu \propto U^\mu U^\nu$ — and why a thermal gas, with momenta spread isotropically in the rest frame, acquires an isotropic pressure: the spread in $p^i p^j$ off-diagonal directions averages to $p\,\delta^{ij}$.

---

# Examples / Corollaries

**Is an instance — pressureless dust.** A cloud of non-interacting particles all sharing, locally, the four-velocity field $U$ and with proper energy density $\varepsilon_0$ (energy per unit rest-frame volume) has
$$
T = \varepsilon_0\, U^\flat \otimes U^\flat, \qquad T^{\mu\nu} = \varepsilon_0\, U^\mu U^\nu.
$$
In the rest frame $U = (1,0,0,0)$ (with $c=1$), so $T^{00} = \varepsilon_0$ and all other components vanish: pure energy density, no momentum, no stress. This is the simplest non-vacuum $T$ and the $p \to 0$ limit of a [[Def - Perfect Fluid|perfect fluid]].

**Is an instance — a perfect fluid.** A fluid with proper energy density $\rho$ and isotropic pressure $p$ has $T^{\mu\nu} = (\rho + p)U^\mu U^\nu - p\,\eta^{\mu\nu}$ (in mostly-minus). In the rest frame this is $\mathrm{diag}(\rho, p, p, p)$: energy density on the diagonal time slot, equal pressure on the three spatial diagonal slots, no shear and no energy flux. The pressure terms are the isotropic stress — momentum streaming equally in all directions. This is the subject of relativistic hydrodynamics.

**Is an instance — the electromagnetic field.** With no matter present, a pure electromagnetic field still carries energy and momentum, with $T^{\mu\nu}_{\text{em}} = \varepsilon_0(F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta})$; its $00$ component is the familiar field energy density $\tfrac{\varepsilon_0}{2}(E^2 + c^2 B^2)$ and its $0i$ block is the Poynting momentum density. See [[Def - Energy-Momentum Tensor of the Electromagnetic Field]].

**Is NOT an instance — the metric tensor.** The metric $\eta_{\mu\nu}$ is a symmetric $(0,2)$-tensor, but it is *not* an energy-momentum tensor: it is constant, non-degenerate, and describes geometry, not matter. The decisive difference is degeneracy — $\eta$ is never zero or degenerate, whereas a physical $T$ vanishes in vacuum and may be degenerate even where matter is present (the dust tensor $\varepsilon_0 U^\mu U^\nu$ has rank one, hence is highly degenerate). Confusing the two is the error of thinking $T$ defines lengths; it does not.

**Is NOT an instance — an antisymmetric tensor.** The electromagnetic field strength $F_{\mu\nu}$ is a rank-two tensor, but it is *antisymmetric*, $F_{\mu\nu} = -F_{\nu\mu}$, and is not an energy-momentum tensor: it is a field, not the energy of a field. The energy-momentum tensor built *from* $F$ is the symmetric quadratic combination above. An antisymmetric tensor has zero diagonal, so it could never carry a non-zero energy density $T_{00}$.

**Corollary — energy density is observer-dependent but always a single contraction.** Two observers with four-velocities $U_0$ and $U_0'$ generally disagree on the energy density, $T(U_0,U_0) \ne T(U_0',U_0')$, because energy is frame-dependent. But each obtains *their* energy density by the identical recipe: set both slots of $T$ to their own four-velocity. The frame-dependence lives entirely in the choice of $U_0$, not in the tensor.

**Corollary — the trace is a Lorentz scalar.** The trace $T = \eta^{\mu\nu}T_{\mu\nu} = T^\mu{}_\mu$ is a frame-independent number. For dust it is $\varepsilon_0\,U\cdot U = \varepsilon_0$ (with $c=1$); for a perfect fluid it is $\rho - 3p$; for the electromagnetic field it is *zero*, the statement that the photon is massless and the electromagnetic field is conformally invariant. A vanishing trace is a strong structural fact, and you should reach for it whenever electromagnetism or massless fields appear.

**Calibration check.** If you have understood the definition you should be able to: (i) write down the dust tensor in a frame where the dust moves at speed $v$ along $x$, and check that its $00$ component is $\gamma^2\varepsilon_0$ — the energy density is boosted by $\gamma^2$, one $\gamma$ for the energy per particle and one for the Lorentz contraction of the volume; (ii) confirm that the perfect-fluid tensor reduces to the dust tensor when $p = 0$; and (iii) verify from the component matrix that the symmetry $T_{0i} = T_{i0}$ is exactly the statement $c\varpi_i = \varphi_i/c$, i.e. $\varphi = c^2\varpi$.

---

# Unlocked by This

> [!tip] The Source of Gravity *(from General Relativity)*
> The single most consequential role of the energy-momentum tensor lies one chapter downstream, in **general relativity**. Einstein's field equation reads $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}/c^4$, where the left-hand **Einstein tensor** $G_{\mu\nu}$ is built from the curvature of spacetime and the right-hand side is exactly the symmetric $T_{\mu\nu}$ defined here. In words: *energy and momentum tell spacetime how to curve.* This is why the rank, symmetry, and conservation of $T$ are not incidental — they are forced by what the right-hand side of the field equation must be. The Einstein tensor is symmetric, so $T$ must be symmetric; the contracted Bianchi identity gives $\nabla^\mu G_{\mu\nu} = 0$ identically, so consistency demands $\nabla^\mu T_{\mu\nu} = 0$ — which is precisely the [[Thm - Energy-Momentum Conservation|conservation law]] established in this chapter. The flat-spacetime $T$ of special relativity is the seed: it is what the source term reduces to in the local inertial frame at each event, and the whole apparatus of [[Special Relativity XXV — Toward Relativistic Gravitation|relativistic gravitation]] is the story of letting $T$ curve the very metric it is measured against. The bridge to the curved theory is the existing vault treatment **[[General Relativity I — Einstein's Equations and Schwarzschild]]**, where this same tensor appears as the matter source of the Schwarzschild geometry.

> [!tip] The Stress-Energy of Quantum Fields and the Casimir Effect *(from Quantum Field Theory)*
> Promoting the classical fields in $T_{\mu\nu}$ to operators gives the **stress-energy operator** of quantum field theory, whose vacuum expectation value $\langle 0 | T_{\mu\nu} | 0\rangle$ need not vanish. The difference of vacuum energies between two configurations — for instance, between the region inside a pair of conducting plates and free space — is finite and measurable: the **Casimir effect**. The conservation law $\nabla^\mu T_{\mu\nu} = 0$ survives quantisation as a Ward identity, and the trace $T^\mu{}_\mu$, classically zero for the electromagnetic field, acquires a quantum **trace anomaly** — one of the deepest fingerprints of the breaking of classical conformal symmetry by renormalisation.

> [!tip] Relativistic Hydrodynamics and the Perfect Fluid *(from Continuum Mechanics)*
> Specialising $T_{\mu\nu}$ to a continuous medium with isotropic pressure gives the **perfect-fluid** tensor and, through the conservation law, the **relativistic Euler equation**. Projecting $\nabla_\mu T^{\mu\nu} = 0$ along the flow yields the energy (entropy) equation; projecting orthogonally yields the momentum equation. This is the engine of relativistic astrophysics — accretion flows, neutron-star structure, the cosmological fluid — and is developed in [[Special Relativity XXIV — Relativistic Hydrodynamics]].

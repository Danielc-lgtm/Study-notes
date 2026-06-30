---
type: definition
subject: special-relativity
prereqs:
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - The Hodge Star"
  - "Def - Observer and Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity, electromagnetism]
---

# Notation

We use SI units and keep the speed of light $c$ explicit, restoring it wherever a formula is more recognisable that way. The signature is **mostly minus**, $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector $X$ has $X\cdot X > 0$. Four-vectors are capital Latin letters with no arrows ($U$, $V$, $P$); spatial three-vectors in an observer's rest space are bold ($\mathbf{E}$, $\mathbf{B}$, $\mathbf{V}$). Greek indices $\mu,\nu,\alpha,\beta$ run $0\ldots3$; Latin indices $i,j,k$ run $1\ldots3$. The Einstein summation convention is in force. The metric dual (index lowering) of a vector $V$ is the one-form $\underline{V}$ with components $V_\mu = \eta_{\mu\nu}V^\nu$. An **observer** $\mathcal{O}$ has unit future-directed four-velocity $U_0$ ($U_0\cdot U_0 = 1$) and a [[Def - Observer and Local Rest Space|local rest space]] $\mathcal{E}_{U_0} = U_0^\perp$. The fully antisymmetric **Levi-Civita tensor** is $\epsilon$, and $\star$ is the [[Def - The Hodge Star|Hodge star]]. Full registry on [[Special Relativity XXI — The Electromagnetic Field]].

> [!warning] Convention
> Gourgoulhon, the rigour source for this chapter, works in the opposite signature $\mathrm{diag}(-1,+1,+1,+1)$, where a timelike four-velocity has $(U_0)_\alpha = (-1,0,0,0)$. We have flipped to $\mathrm{diag}(+1,-1,-1,-1)$, so $(U_0)_\alpha = (+1,0,0,0)$ and the time rows and columns of the component matrices below carry the opposite overall sign from his Eq. (17.12). The 2-form $F$ itself and the physical fields $\mathbf{E}$, $\mathbf{B}$ are convention-independent; only the bookkeeping of raised/lowered components changes. Both invariants and every physical force are sign-robust.

---

# Axiom Motivation

The problem is to say what the electromagnetic field *is*, as a single geometric object on spacetime, rather than as the pair of three-vectors $\mathbf{E}$ and $\mathbf{B}$ that an introductory course hands you. The motivation is to start not from the field but from its *effect* — the force it exerts on a charged particle — and let the structure of that force dictate the structure of the field. This is the cleanest possible route, and it is forced at almost every step.

Begin with the demand that the electromagnetic interaction be a **vector interaction**, not a scalar one. A scalar interaction (like the coupling of a particle to a scalar field) exerts a force that depends only on a number characterising the particle — its mass, say. Experiment shows the electromagnetic force depends on a *direction* intrinsic to the particle: a charge at rest in a magnetic field feels nothing, a charge moving through it is deflected, and the deflection depends on the direction of motion. The only direction intrinsic to a particle $\mathcal{P}$ is its [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$, the unit tangent to its [[Def - Worldline of a Particle|worldline]]. So the four-force must be built from $U$. The simplest assumption — and, it turns out, the correct one — is that the four-force is **linear** in $U$. A linear map sending the vector $U$ to the four-force one-form $f$ is exactly a **bilinear form** $F$, and we are forced to write
$$
f \;=\; q\,F(\,\cdot\,,U), \qquad f_\alpha = q\,F_{\alpha\beta}\,U^\beta,
$$
with $q$ a constant — the **electric charge** — characterising the particle. This single equation *defines* the field $F$: it is the object that, contracted with any particle's four-velocity, returns the four-force per unit charge. There is no other object in the theory; $F$ is the electromagnetic field.

Now the second axiom, **antisymmetry**, is not an aesthetic choice but a consequence of a physical law: the electromagnetic four-force is a **pure** four-force, meaning it is orthogonal to the four-velocity, $f\cdot U = 0$. This is the statement that the Lorentz force does no work in the particle's instantaneous rest frame — equivalently, that it conserves the particle's rest mass (recall from [[Def - Four-Force|the four-force page]] that $f\cdot U = dm/d\tau$, so a pure force keeps $m$ fixed). Imposing $f\cdot U = 0$ on $f = qF(\cdot,U)$ gives $q\,F(U,U) = 0$ for every four-velocity $U$, hence $F(V,V) = 0$ for all $V$ in a neighbourhood of any unit timelike vector, and by linearity for all $V$ whatsoever. A bilinear form that vanishes on the diagonal is **antisymmetric**, $F(U,V) = -F(V,U)$, i.e. $F_{\alpha\beta} = -F_{\beta\alpha}$. So the field is a **2-form**, an antisymmetric $(0,2)$ tensor — a degree-two [[Def - Alternate Forms and the Exterior Product|alternating form]]. Drop the purity axiom and you would permit a symmetric part to $F$; that symmetric part would describe a force that changes the rest mass of the particle as it accelerates, which is not what electromagnetism does and not what is observed.

Why a 2-form and not, say, a vector or a scalar? Because the data we must encode are exactly the right size. A 2-form in four dimensions has $\binom{4}{2} = 6$ independent components, and the electromagnetic field has precisely six numbers at each event: the three components of $\mathbf{E}$ and the three of $\mathbf{B}$. This is not a coincidence to be admired but a constraint that the 2-form structure *enforces*. A vector would give four components, a symmetric tensor ten — neither matches. The 2-form is the unique antisymmetric object whose component count is six, and it organises $\mathbf{E}$ and $\mathbf{B}$ into one Lorentz tensor whose transformation law mixes them. The whole of the next section's "transformation of $\mathbf{E}$ and $\mathbf{B}$" is just the tensor transformation law $F'_{\alpha\beta} = \Lambda_\alpha{}^\mu\Lambda_\beta{}^\nu F_{\mu\nu}$ read out in components.

The final design decision is to make the split into $\mathbf{E}$ and $\mathbf{B}$ **observer-relative**. There is no frame-free way to say which part of $F$ is "electric" and which is "magnetic"; that division requires a choice of time direction, that is, an observer's four-velocity $U_0$. Given $U_0$, the contraction $F(\cdot,U_0)$ picks out a one-form living in the rest space — the electric field — and the Hodge-dual contraction $\star F(U_0,\cdot)$ picks out the magnetic field. Change the observer and you change the split, but not the underlying $F$. This is the precise content of the slogan that $\mathbf{E}$ and $\mathbf{B}$ are *shadows* of a single object: they are the projections of $F$ adapted to one observer's rest space, and a different observer casts different shadows.

---

# The Definition

Let $\mathcal{P}$ be a particle of electric charge $q$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$, on its worldline in Minkowski spacetime. The **electromagnetic field tensor** (also **Faraday tensor**, **field-strength tensor**, **Maxwell tensor**) is the antisymmetric $(0,2)$ tensor field $F$ — a **2-form** — defined by the requirement that the [[Def - Four-Force|four-force]] it exerts on $\mathcal{P}$ is
$$
f \;=\; q\,F(\,\cdot\,,U), \qquad\text{equivalently}\qquad f_\alpha \;=\; q\,F_{\alpha\beta}\,U^\beta, \quad f^\mu = q\,F^\mu{}_\nu\,U^\nu.
$$
This four-force is the **Lorentz four-force** (see [[Def - The Lorentz Four-Force]]). Antisymmetry,
$$
F(V,W) = -F(W,V), \qquad F_{\alpha\beta} = -F_{\beta\alpha},
$$
follows from the postulate that the Lorentz force is a pure four-force, $f\cdot U = 0$.

**Decomposition relative to an observer.** Let $\mathcal{O}$ be an observer of four-velocity $U_0$, with [[Def - Observer and Local Rest Space|local rest space]] $\mathcal{E}_{U_0} = U_0^\perp$. There exist a unique one-form $\mathbf{E}$ (the **electric field relative to $\mathcal{O}$**) and a unique vector $\mathbf{B}$ (the **magnetic field relative to $\mathcal{O}$**), both lying in the rest space, such that
$$
F \;=\; \underline{U_0}\wedge \mathbf{E} \;+\; \star\!\left(\underline{U_0}\wedge c\,\underline{\mathbf{B}}\right),
\qquad \langle\mathbf{E},U_0\rangle = 0,\quad U_0\cdot\mathbf{B} = 0.
$$
Equivalently, $\mathbf{E}$ and $\mathbf{B}$ are recovered from $F$ by the contractions
$$
\mathbf{E} \;=\; F(\,\cdot\,,U_0), \qquad c\,\mathbf{B} \;=\; \star F(U_0,\,\cdot\,),
\qquad B^\alpha = -\frac{1}{2c}\,\epsilon^{\alpha\mu\nu}{}_\rho\,F_{\mu\nu}\,U_0^\rho .
$$
The fields depend on $\mathcal{O}$; the tensor $F$ does not. The electric field has the dimension of $F$ (volt per metre in SI); the magnetic field has the dimension of an electric field divided by a velocity (the SI unit is the tesla, $1\,\mathrm{T} = 1\,\mathrm{V\,m^{-2}\,s}$).

**Components in an observer's local frame.** Choose the orthonormal frame $(e_0,e_1,e_2,e_3)$ with $e_0 = U_0$, so $\mathbf{E} = (E_1,E_2,E_3)$ and $\mathbf{B} = (B^1,B^2,B^3)$ are purely spatial. In the mostly-minus convention the components of $F$ are
$$
F_{\alpha\beta} \;=\; \begin{pmatrix} 0 & E_1 & E_2 & E_3 \\ -E_1 & 0 & -cB^3 & cB^2 \\ -E_2 & cB^3 & 0 & -cB^1 \\ -E_3 & -cB^2 & cB^1 & 0 \end{pmatrix},
\qquad
F^{\alpha\beta} \;=\; \begin{pmatrix} 0 & -E_1 & -E_2 & -E_3 \\ E_1 & 0 & -cB^3 & cB^2 \\ E_2 & cB^3 & 0 & -cB^1 \\ E_3 & -cB^2 & cB^1 & 0 \end{pmatrix},
$$
related by $F^{\alpha\beta} = \eta^{\alpha\mu}\eta^{\beta\nu}F_{\mu\nu}$. The time-space block holds $\pm\mathbf{E}$, the space-space block holds $c\mathbf{B}$ through $F_{ij} = -c\,\epsilon_{ijk}B^k$.

The **preview that organises everything downstream**: $F$ is *closed and exact*, $F = dA$ for a [[Def - The Four-Potential|four-potential]] one-form $A$, with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. This is established in [[Special Relativity XXII — Maxwell's Equations]]; antisymmetry of $F$ is then automatic from $d^2 = 0$, and the homogeneous Maxwell equations $dF = 0$ are an identity.

---

# Categorical / Structural Definition

Structurally, $F$ is a section of the bundle $\Lambda^2 T^*\mathbb{M}$ of 2-forms over Minkowski space — a degree-two element of the [[Def - Alternate Forms and the Exterior Product|exterior algebra]] of the cotangent space at each event. The space $\Lambda^2(\mathbb{R}^{1,3})^*$ is six-dimensional, and it carries a natural action of the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$: this is the antisymmetric-rank-two **tensor representation**, which decomposes, over the complex numbers, into two three-dimensional irreducible pieces — the self-dual and anti-self-dual 2-forms, the eigenspaces of the [[Def - The Hodge Star|Hodge star]] $\star$ (which squares to $-\mathrm{Id}$ on 2-forms in Lorentzian signature). The combination $\mathbf{E} + i c\mathbf{B}$ transforms under one of these $(1,0)$ or $(0,1)$ pieces; this is the precise representation-theoretic sense in which the electromagnetic field "is" a $(1,0)\oplus(0,1)$ object of the Lorentz group, the same statement that, quantised, says the photon has helicity $\pm1$.

A second structural reading: the assignment "particle four-velocity $\mapsto$ four-force per unit charge" is a fibrewise linear map $T\mathbb{M}\to T^*\mathbb{M}$, i.e. a bundle morphism, and $F$ is its representing bilinear form. The purity condition $f\cdot U = 0$ says this morphism is *skew* with respect to the metric pairing — exactly the condition that places $F$ in the Lie algebra $\mathfrak{so}(1,3)$ when an index is raised, $F^\mu{}_\nu \in \mathfrak{so}(1,3)$. That $F^\mu{}_\nu$ is (pointwise) an element of the Lorentz Lie algebra is why the field acts on four-velocities as an infinitesimal Lorentz transformation: a charged particle in a uniform field is being continuously, infinitesimally Lorentz-boosted-and-rotated, which is why its motion integrates to a hyperbolic-or-circular trajectory (see [[Thm - Motion of a Charge in a Uniform Field]]).

---

# Relate to Other Fields / Compression

The deepest cross-field identification is with **gauge theory**: $F$ is the **curvature** of a connection on a $U(1)$ principal bundle, and $A$ is the connection (the gauge potential). In the vault, [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]] develops exactly this — the electromagnetic field strength $F = dA$ is the curvature 2-form of the electromagnetic connection, and the statement $dF = 0$ is the Bianchi identity. The flat-spacetime Faraday tensor of this page is that curvature read in an inertial frame; gauge invariance $A\to A + d\chi$ leaves $F$ unchanged because $d^2\chi = 0$, the curvature being independent of the gauge representative.

**True name:** the operational characterisation of $F$, the one you reach for in computation, is *the antisymmetric matrix that turns a four-velocity into a four-force per unit charge*, $f^\mu = qF^\mu{}_\nu U^\nu$ — or, even more compactly, *the matrix whose time-space block is $\mathbf{E}$ and whose space-space block is $c\mathbf{B}$*. When a problem hands you $\mathbf{E}$ and $\mathbf{B}$, the move is to assemble $F_{\alpha\beta}$; when it hands you $F$, the move is to read $\mathbf{E}$ and $\mathbf{B}$ off the blocks relative to whatever observer you are working in. Everything else — the transformation law, the invariants, the equation of motion — is a manipulation of this one matrix.

This is the same construction as the **angular-momentum / field-strength antisymmetric tensor** pattern throughout relativistic physics: just as the [[Def - Angular Momentum Four-Tensor|angular-momentum tensor]] $J^{\alpha\beta} = x^\alpha p^\beta - x^\beta p^\alpha$ packages the three components of orbital angular momentum and three of mass-moment into one antisymmetric tensor, $F$ packages $\mathbf{E}$ and $\mathbf{B}$. In both cases the "electric-like" part (boost-type, time-space components) and the "magnetic-like" part (rotation-type, space-space components) mix under boosts in exactly the same way, because both transform in the antisymmetric tensor representation of the Lorentz group.

---

# Examples / Corollaries

**Is an instance — a uniform magnetostatic field.** Relative to an inertial observer let $\mathbf{E} = 0$ and $\mathbf{B} = B\,e_3$. Then the only nonzero components are $F_{12} = -F_{21} = -cB$, and the field exerts the Lorentz force $f^i = qF^i{}_j U^j$ on a moving charge, producing circular or helical motion. This $F$ is a perfectly good 2-form even though one observer calls it "purely magnetic" — a different observer will measure a nonzero electric field.

**Is an instance — the Coulomb field of a point charge at rest.** With $\mathbf{B} = 0$ and $\mathbf{E} = \frac{q}{4\pi\varepsilon_0 r^2}\,\hat{\mathbf{r}}$, the tensor has only time-space components $F_{0i} = E_i$. Boosting to a frame where the charge moves produces a magnetic field — this is the content of [[Def - Field of a Charge in Uniform Translation]] and the origin of the magnetic force between currents.

**Is NOT an instance — a symmetric $(0,2)$ tensor.** The metric $\eta_{\mu\nu}$ and the [[Def - The Energy-Momentum Tensor|energy-momentum tensor]] $T_{\mu\nu}$ are symmetric, $T_{\mu\nu} = T_{\nu\mu}$. They are not electromagnetic field tensors, because the Lorentz force built from a symmetric $F$ would fail to be pure: contracting $f = qF(\cdot,U)$ with $U$ would give $qF(U,U)\ne0$ in general, a force that changes the rest mass. Only the antisymmetric part of a $(0,2)$ tensor can be a field strength.

**Is NOT an instance — an arbitrary six-component spatial pair under the wrong transformation.** Two ordinary spatial three-vectors $\mathbf{E}$, $\mathbf{B}$ that transform *separately* (each as a Euclidean vector under rotations, unchanged under boosts) do *not* assemble into a Lorentz tensor. The whole point is that the six components mix under boosts according to $F'_{\alpha\beta} = \Lambda_\alpha{}^\mu\Lambda_\beta{}^\nu F_{\mu\nu}$; a pair that does not mix is not a 2-form and is not relativistically consistent.

**Corollary — the field has six independent components.** Antisymmetry kills the four diagonal entries and identifies the lower triangle with minus the upper, leaving $\binom{4}{2}=6$ free numbers: three in the time-space block ($\mathbf{E}$) and three in the space-space block ($\mathbf{B}$). This is why the electromagnetic field is exactly $(\mathbf{E},\mathbf{B})$ relative to any observer.

**Corollary — the Lorentz force is automatically perpendicular to the four-velocity.** From antisymmetry, $f\cdot U = qF_{\alpha\beta}U^\beta U^\alpha = 0$, since $F_{\alpha\beta}U^\alpha U^\beta$ contracts a symmetric pair $U^\alpha U^\beta$ against an antisymmetric $F_{\alpha\beta}$. Hence the rest mass is conserved along the worldline of a charged particle in any electromagnetic field.

**Calibration check.** You have understood the definition if you can (i) write down $F_{\alpha\beta}$ given $\mathbf{E} = E\,e_1$, $\mathbf{B} = B\,e_2$ relative to an observer, and read it back; (ii) verify by index manipulation that $F_{\alpha\beta}U^\alpha U^\beta = 0$ for any $U$, using only antisymmetry; (iii) explain why $\mathbf{E}$ and $\mathbf{B}$ are vectors *in the observer's rest space* and not absolute objects, by pointing to the contraction with $U_0$ in their definitions.

---

# Unlocked by This

> [!tip] The Lorentz Four-Force *(from §21.1)*
> The defining relation $f = qF(\cdot,U)$ is itself the [[Def - The Lorentz Four-Force|Lorentz four-force]]; projected onto an inertial observer's rest space it reproduces the elementary $\mathbf{f} = q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$, and its time component gives the rate of working $q\,\mathbf{E}\cdot\mathbf{V}$.

> [!tip] Field Invariants and the Classification of Fields *(from §21.2)*
> From $F$ and its Hodge dual one builds the two Lorentz scalars $I_1 = \tfrac12 F_{\mu\nu}F^{\mu\nu} = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = \tfrac14 (\star F)_{\mu\nu}F^{\mu\nu} = c\,\mathbf{E}\cdot\mathbf{B}$ ([[Thm - The Electromagnetic Field Invariants]]), whose signs classify the field as mostly electric, mostly magnetic, or null — a frame-independent invariant of the geometry.

> [!tip] Maxwell's Equations and F = dA *(from Electromagnetism)*
> Writing $F = dA$ for a one-form potential $A$ makes the homogeneous pair of **Maxwell's equations** the identity $dF = ddA = 0$, and the inhomogeneous pair becomes $d\star F = \mu_0\star J$ — two tensor equations replacing the classical four. This is developed in [[Special Relativity XXII — Maxwell's Equations]]; the four-potential and four-current live there.

> [!tip] The Energy-Momentum Tensor of the Field *(from Field Theory and General Relativity)*
> Quadratic in $F$, the symmetric tensor $T^{\mu\nu} = \frac{1}{\mu_0}\big(F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\big)$ encodes the energy density $\tfrac12(\varepsilon_0\mathbf{E}^2 + \mathbf{B}^2/\mu_0)$, the Poynting momentum density, and the Maxwell stress. It is the source of gravity in **general relativity** and the conserved current of the field's spacetime translations; see [[Def - The Energy-Momentum Tensor]].

> [!tip] Curvature of a U(1) Connection *(from Gauge Theory)*
> The identification $F = dA$ makes $F$ the **curvature** of a connection on a $U(1)$ principal bundle, with $A$ the connection one-form; $dF = 0$ is the **Bianchi identity**. Electromagnetism is the abelian case of [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection|Yang–Mills theory]], and the non-abelian generalisation — replacing $U(1)$ by $SU(2)$ or $SU(3)$, so that $F = dA + A\wedge A$ acquires a self-interaction term — is the foundation of the electroweak and strong interactions.

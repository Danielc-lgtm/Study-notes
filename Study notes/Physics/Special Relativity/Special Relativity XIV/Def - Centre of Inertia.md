---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Observer and Local Rest Space"
  - "Def - Angular Momentum Four-Tensor"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A system $\mathscr{S}$ has particles of [[Def - Four-Momentum and Rest Mass|four-momentum]] $p_a$; relative to an observer $\mathcal{O}$ of four-velocity $U_0$ and worldline through $O(t)$ at proper time $t$, the position of particle $a$ is the event $M_a(t) = \mathscr{L}_a\cap E_{u_0}(t)$ where it crosses $\mathcal{O}$'s local rest space, with energy $E_a = p_a\cdot U_0$. The total energy is $E = \sum_a E_a$, the total momentum $P = \sum_a p_a$, the rest mass $m$ with $P\cdot P = m^2$, and the system four-velocity $\vec u = P/m$. The mass-energy dipole moment is $\vec D = \frac{1}{c^2}\sum_a E_a\overrightarrow{OM_a}$ (with $c=1$, $\vec D = \sum_a E_a\overrightarrow{OM_a}$). Full registry on [[Special Relativity XIV — Angular Momentum and Spin]].

This is a compound page: it defines two interlocking notions — the **centroid** $G_\mathcal{O}$ (observer-dependent) and the **centre of inertia** $G$ (intrinsic, for an isolated system) — because the second is the first with a particular choice of observer, and the surprising relativistic content lives in the gap between them.

---

# Axiom Motivation

We want a relativistic "centre of mass" — a single point that represents where the mass of a system is concentrated, so that the system can be treated, for many purposes, as a point particle sitting there. In Newtonian mechanics this is the unproblematic $\mathbf{R} = \frac{1}{M}\sum m_a\mathbf{r}_a$, the mass-weighted mean position, and it has two properties so obvious they are never stated: it is a definite point, and every observer agrees on where it is. The motivation of this definition is the discovery that *neither* property survives relativity cleanly, and the careful construction needed to recover a usable notion.

The first issue is **what to weight by**. Newton weights by mass $m_a$. But in relativity mass is not additive — the rest mass of a system is *not* the sum of the rest masses of its parts (binding energy and kinetic energy contribute). The additive, conserved quantity is energy. So the natural weighting is by energy: $\overrightarrow{OG_\mathcal{O}} = \frac{1}{E}\sum_a E_a\overrightarrow{OM_a}$. In the nonrelativistic limit $E_a\to m_ac^2$ this reduces to the mass-weighted mean, recovering Newton; but the relativistic object is the energy-weighted mean. This is forced: only the energy-weighted point has a constant-velocity worldline for an isolated system (the mass-weighted point does not), which is the property a "centre of mass" must have to be useful.

The second issue, the deep one, is that **the energy-weighted mean depends on the observer in two separate ways**. First, the positions $\overrightarrow{OM_a}$ are taken in the observer's rest space $E_{u_0}(t)$ — the simultaneity slice — and a different observer slices spacetime differently, so the "positions at the same time" are different events. Second, the weights $E_a = p_a\cdot U_0$ are the energies *relative to this observer*, and a moving observer assigns different energies. Both the points being averaged and the weights averaging them change with the observer. There is no reason the answers should agree, and they do not: the centroid is genuinely observer-dependent. This is the relativistic surprise that has no Newtonian shadow — in Newton both the simultaneity (absolute time) and the weights (rest masses) are observer-independent, so the centre of mass is objective.

How do we recover an **intrinsic point**? We cannot make the centroid observer-independent, but we can *select a canonical observer*. For an isolated system there is a distinguished family: the observers comoving with the system, whose four-velocity equals the system's own $\vec u = P/m$. Two inertial observers sharing a four-velocity agree on the centroid (their rest spaces coincide and their energy assignments agree), so the comoving observers all compute the *same* centroid. That common point is the **centre of inertia** $G$ — intrinsic because it no longer depends on a choice within the comoving family. Its worldline is a straight timelike line, the worldline of the centre-of-momentum frame.

Why does the centre of inertia exist only for an **isolated** system? Because the construction needs a well-defined total four-velocity $\vec u = P/m$ to single out the comoving observers, and that requires $P$ conserved and $m$ nonvanishing — which is exactly isolation plus nonzero rest mass. For a general system, or a massless one, there is no canonical comoving family and hence no centre of inertia; only the observer-dependent centroid survives. This is why the definition is two-tiered: the centroid always exists but is relative; the centre of inertia is intrinsic but exists only under isolation.

---

# The Definition

Let $\mathscr{S}$ be a system and $\mathcal{O}$ an observer of four-velocity $U_0$, with position $O(t)$ on its worldline at proper time $t$. The **centroid of $\mathscr{S}$ relative to $\mathcal{O}$** is the event $G_\mathcal{O}(t)$ in $\mathcal{O}$'s local rest space $E_{u_0}(t)$ defined by the energy-weighted mean
$$
\overrightarrow{OG_\mathcal{O}}(t) \;:=\; \frac{1}{E}\sum_a E_a\,\overrightarrow{OM_a}(t) \;=\; \frac{c^2}{E}\,\vec D,
$$
where $M_a(t)$ is the position of particle $a$ in $E_{u_0}(t)$, $E_a = p_a\cdot U_0$ its energy, $E = \sum_a E_a$ the total energy, and $\vec D$ the mass-energy dipole moment. The centroid is **observer-dependent**: it depends on $\mathcal{O}$ both through the rest space $E_{u_0}(t)$ in which the positions are taken and through the energies $E_a$ that weight them.

Two inertial observers with the *same* four-velocity $U_0$ compute the same centroid; equivalently, all observers belonging to one rigid array of inertial observers agree.

Now suppose $\mathscr{S}$ is **isolated** with nonvanishing rest mass $m$, so it has a well-defined four-velocity $\vec u = P/m$. A **barycentric observer** is an inertial observer comoving with $\mathscr{S}$, i.e. of four-velocity $\vec u$; the frame of such an observer is a **centre-of-momentum** (or centre-of-inertia, or centre-of-mass) **frame**. All barycentric observers compute the same centroid, the intrinsic point called the **centre of inertia** $G$ of $\mathscr{S}$. Its worldline $\mathscr{L}_G$ is a straight timelike line with tangent $\vec u$.

For a barycentric observer the defining quantities simplify:
$$
\vec D = 0,
\qquad
\mathbf{P} = 0
\quad(\text{vanishing total three-momentum}),
\qquad
E = mc^2,
$$
so the mass-energy dipole moment vanishes, the total spatial momentum vanishes, and the energy reduces to the rest mass. The centre of inertia admits an equivalent, observer-free characterisation through the angular momentum: $G$ is the unique worldline about which the [[Def - Spin Four-Vector|spin supplementary condition]]
$$
J_G(P,\cdot) = 0
$$
holds (the Tulczyjew/Synge condition), i.e. the worldline about which the angular momentum two-form is purely "magnetic" with respect to $P$.

The velocity of the centroid relative to a general inertial observer $\mathcal{O}$ is constant, $\vec V_{G_\mathcal{O}} = \frac{c^2}{E}\,\mathbf{P}$, equal to the velocity of a point particle carrying the system's four-velocity $\vec u$; in particular for an isolated system every centroid moves uniformly along a line parallel to $\vec u$.

---

# Relate to Other Fields / Compression

This is the relativistic upgrade of the **Newtonian centre of mass**, with two modifications: weight by energy rather than rest mass (because energy, not mass, is additive and conserved), and accept that the resulting point is observer-dependent. The Newtonian centre of mass is recovered in the limit $E_a\to m_ac^2$, where the energy weighting becomes mass weighting and the observer-dependence (of order $v^2/c^2$) vanishes.

In the geometry of [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|Hamiltonian mechanics]] the centre of inertia is the point about which the **moment map** of the translation–boost subgroup takes a canonical form; the observer-dependence of the centroid reflects the non-commutativity of boosts with translations in the Poincaré group, the same non-commutativity that produces the Thomas rotation.

**True name:** the centre of inertia is *the worldline about which the angular momentum has no orbital part*, i.e. the unique worldline satisfying $J_G(P,\cdot) = 0$. The energy-weighted-mean definition is how you compute it; the supplementary-condition characterisation is what it *is* — the reference worldline that makes the [[Thm - König Theorem (Relativistic)|König decomposition]] clean, with the spin as the entire angular momentum about it.

---

# Examples / Corollaries

**Is an instance — the centre of inertia of two equal masses.** Two particles of equal rest mass at rest, separated by a distance $d$, have their centre of inertia at the midpoint, exactly as in Newtonian mechanics. The energy weighting equals the mass weighting because both are at rest, and the system's rest frame is the obvious one. No surprise here — the relativistic and Newtonian answers coincide because nothing is moving.

**Is an instance — a moving observer's centroid of a spinning body.** A spinning body of mass $m$ and spin vector $\vec\sigma$ at rest in frame $S$ has its centre of inertia at the origin of $S$. An observer $\mathcal{O}$ moving at velocity $\vec V$ relative to $S$ computes a centroid displaced from the centre of inertia by $\overrightarrow{GG_\mathcal{O}} = \frac{1}{mc^2}\vec\sigma\times\vec V$ — a genuinely different point, perpendicular to both the spin and the relative velocity. This is the [[Thm - Minimal Size of a Spinning System|Møller displacement]], the concrete witness of observer-dependence.

**Is NOT an instance — a "centre of inertia" for a single photon.** A photon has $m = 0$, so $\vec u = P/m$ is undefined and there is no comoving family and no centre of inertia. One can still compute a *centroid* relative to a given observer, but there is no intrinsic point. The centre of inertia requires nonzero rest mass.

**Is NOT an instance — the mass-weighted mean position.** The point $\frac{1}{M}\sum m_a\overrightarrow{OM_a}$ (weighting by rest mass, with $M = \sum m_a$) is *not* the relativistic centre of inertia: it does not have a constant-velocity worldline for an isolated system, and it does not satisfy the supplementary condition. The correct weighting is by energy.

**Corollary — agreement under shared four-velocity.** If $\mathcal{O}$ and $\mathcal{O}'$ are inertial with the same four-velocity $U_0$, their centroids coincide, $G_{\mathcal{O}'} = G_\mathcal{O}$, because their rest spaces coincide and (having the same $U_0$) they assign the same energies $E_a$. This is what makes the centre of inertia well-defined as the common centroid of the comoving family.

**Corollary — the centroid moves uniformly.** Since $\vec V_{G_\mathcal{O}} = \frac{c^2}{E}\mathbf{P}$ and both $E$ and $\mathbf{P}$ are constant for an isolated system, the centroid follows a straight line at constant velocity relative to any inertial observer — the relativistic version of "the centre of mass of an isolated system moves uniformly".

**Calibration check.** You should be able to: (1) state the two distinct ways the centroid depends on the observer (rest space for the positions; energies for the weights); (2) explain why the centre of inertia exists for an isolated massive system but not for a photon (need $\vec u = P/m$); and (3) recover the Newtonian centre of mass from the energy-weighted definition by taking $E_a\to m_ac^2$.

---

# Unlocked by This

> [!tip] The Newton–Wigner Position and Localisation in QFT *(from Quantum Field Theory)*
> The observer-dependence of the relativistic centre of mass forces a hard question in quantum theory: what operator represents the *position* of a relativistic particle? The answer, the **Newton–Wigner position operator**, is the quantum analogue of the centre of inertia, and it inherits the supplementary condition as an operator constraint. Its components do not commute when the particle has spin — a direct quantum echo of the classical Møller displacement $\vec\sigma\times\vec V/(mc^2)$ — and it cannot localise a particle below its Compton wavelength. The classical observer-dependence of the centroid is the seed of the deep fact that relativistic quantum particles have no sharp position.

> [!tip] Centre-of-Mass Energy and Collider Physics *(from Particle Physics)*
> The barycentric frame defined here is the **centre-of-momentum frame** of a collision, in which $\mathbf{P} = 0$ and the total energy is the invariant mass $\sqrt{s} = E_{\text{cm}} = mc^2$. Every collider experiment is designed around this frame: the threshold for producing a new particle of mass $M$ is $\sqrt{s} \geq Mc^2$, and the centre-of-momentum energy is the single number that determines what reactions are kinematically allowed. The centre of inertia of this page is the worldline of that frame, and the invariant mass it carries is the quantity colliders are built to maximise.

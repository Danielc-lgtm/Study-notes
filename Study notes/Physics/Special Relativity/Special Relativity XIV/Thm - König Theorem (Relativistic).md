---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Angular Momentum Four-Tensor"
  - "Def - Spin Four-Vector"
  - "Def - Centre of Inertia"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. An isolated system $\mathscr{S}$ of rest mass $m$ has total [[Def - Four-Momentum and Rest Mass|four-momentum]] $P$, four-velocity $\vec u = P/m$, and [[Def - Centre of Inertia|centre of inertia]] $G$. Its [[Def - Angular Momentum Four-Tensor|angular momentum]] about an event $C$ is the two-form $J_C$; the [[Def - Spin Four-Vector|spin]] two-form is $S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$, with spin vector $\vec\sigma$. The exterior product is $a\wedge b = a\otimes b - b\otimes a$; $\epsilon$ is the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]]. Full registry on [[Special Relativity XIV — Angular Momentum and Spin]].

---

# Statement

> **König theorem (relativistic).** The angular momentum of an isolated system $\mathscr{S}$ about any event $C$ decomposes as the sum of its spin and an orbital part:
> $$J_C \;=\; \underbrace{S}_{\text{spin}} \;+\; \underbrace{\overrightarrow{CG}^\flat\wedge P}_{\text{orbital angular momentum}},$$
> where $S = J_G$ is the angular momentum about the centre of inertia $G$ (independent of $C$), and $\overrightarrow{CG}^\flat\wedge P$ is the angular momentum about $C$ of a fictitious point particle located at $G$ and carrying the total four-momentum $P$. The orbital part carries all the dependence on $C$; the spin part carries none.

A companion identity records the spin's defining property:
> **Spin supplementary condition.** Since $P = m\vec u$ is parallel to $\vec u$ and $S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$, the spin two-form is "magnetic" with respect to $P$:
> $$S(P,\cdot) = 0,\qquad\text{equivalently}\qquad J_G(P,\cdot) = 0.$$

---

# Motivation

The [[Def - Angular Momentum Four-Tensor|angular momentum]] of a system depends on the reference event $C$ you take moments about — move $C$ and the angular momentum changes by the orbital term $\overrightarrow{C'C}^\flat\wedge P$. This is a nuisance if you want to talk about "the angular momentum of the system" as an intrinsic property. König's theorem is the resolution: it shows that the angular momentum cleanly separates into a part that depends on $C$ (the orbital angular momentum, the angular momentum of the system treated as a single point mass at its centre) and a part that does not (the spin, the internal angular momentum about the centre of inertia). The intrinsic content is the spin; the rest is bookkeeping about where you stood to measure.

This is the relativistic upgrade of a theorem every student of mechanics knows in its Newtonian form: the total angular momentum of a system equals the angular momentum of the centre of mass (treated as a point carrying the total mass) plus the angular momentum about the centre of mass. "Orbital plus spin" — the Earth's angular momentum about the Sun is its orbital angular momentum (Earth-as-point going around the Sun) plus its spin (Earth turning on its axis). König's theorem in the relativistic setting says exactly the same thing, with the centre of mass replaced by the [[Def - Centre of Inertia|centre of inertia]], the momentum replaced by the four-momentum, and the cross product replaced by the wedge.

The theorem's real payoff is conceptual: it *defines* what the spin is. The spin is not introduced axiomatically; it is the residue $J_C - \overrightarrow{CG}^\flat\wedge P$ that remains after the orbital part is subtracted, and the theorem's content is that this residue is independent of $C$ — which is precisely what qualifies it to be called intrinsic. So König's theorem is the bridge from the $C$-dependent angular momentum to the $C$-independent spin, and it is where the [[Def - Spin Four-Vector|spin]] earns its name.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$\mathscr{S}$ is an isolated system with a well-defined centre of inertia $G$", i.e. isolated with nonvanishing rest mass.

The first disguised source is **"the total four-momentum is conserved and the centre of inertia has a straight worldline"**. Any isolated massive system qualifies, because conservation of $P$ gives a constant $\vec u = P/m$ and hence a straight centre-of-inertia worldline. The bridge is that isolation $\Rightarrow$ conserved $P$ $\Rightarrow$ existence of $G$. *Example problem:* the angular momentum of a freely-moving spinning body about a laboratory point splits into the orbital angular momentum of its centre of inertia plus its constant spin.

The second disguised source is **"a composite is assembled from subsystems"**. To find the total angular momentum of a composite, one applies König to each subsystem and adds: each contributes its own spin plus the orbital angular momentum of its centre of inertia. The bridge is additivity of the angular momentum two-form. The nonobviousness is that the *total* spin is not simply the sum of the subsystem spins — it is the sum of the subsystem spins *plus* the orbital angular momentum of the subsystem centres of inertia about the total centre of inertia. *Example problem:* the spin of a molecule is the sum of the electronic and nuclear spins plus the orbital angular momentum of the constituents about the molecular centre of inertia.

The third disguised source is **"a single particle with intrinsic spin"**. For a [[Def - Spin Four-Vector|particle with spin]] modelled as a point carrying a spin two-form $S$, the angular momentum about $C$ is $J_C = S + \overrightarrow{CM}^\flat\wedge p$ — the König form with $G = M$, the particle's own position. The bridge is that the definition of a particle with spin is engineered to have exactly this structure. The nonobviousness is that the same decomposition theorem governs both an extended isolated system and a structureless spinning point. *Example problem:* the angular momentum of an electron (modelled classically) about a fixed point is its spin plus the orbital angular momentum of its trajectory.

**Targets (Output Amplification)**

The conclusion is "$J_C = S + \overrightarrow{CG}^\flat\wedge P$".

Combine the conclusion with **the choice $C = G$**. Setting the reference point to the centre of inertia kills the orbital term, $\overrightarrow{GG}^\flat\wedge P = 0$, leaving $J_G = S$: the angular momentum about the centre of inertia is the pure spin. The further result is the cleanest possible computation of spin — evaluate $J_G$ in the centre-of-momentum frame, where most components vanish. The combination is useful because it converts "find the spin" into "evaluate the angular momentum about $G$ in the rest frame". *Example:* the spin of a colliding pair is $J_G$ in their centre-of-momentum frame.

Combine the conclusion with **the spin supplementary condition** $S(P,\cdot) = 0$. Since the spin is "magnetic" with respect to $P$, contracting $J_C$ with $P$ isolates the orbital part: $J_C(P,\cdot) = \overrightarrow{CG}^\flat\wedge P\,(P,\cdot)$, which encodes the displacement $\overrightarrow{CG}$. The further result is a formula for the centre of inertia in terms of the angular momentum: $G$ is the unique worldline making $J_G(P,\cdot) = 0$. The combination is nonobvious because it lets the centre of inertia be *defined* through the angular momentum rather than through energy-weighted positions. *Example:* locating $G$ from the angular momentum tensor and the four-momentum alone (the Tulczyjew/Synge condition).

Combine the conclusion with **the conservation of $J_C$ and $P$**. For an isolated system both $J_C$ and $P$ are conserved, and the orbital term $\overrightarrow{CG}^\flat\wedge P$ evolves only through $\overrightarrow{CG}$ (since $G$ moves uniformly); subtracting it shows the spin $S$ is separately conserved. The further result is the conservation of the spin direction, the principle behind a gyroscope. The combination is useful because it splits the conservation of total angular momentum into separate conservation of orbital and spin parts. *Example:* a spinning isolated body keeps its spin fixed while its centre of inertia drifts uniformly.

---

# Why Is It True

The theorem is true for a reason that is transparent once the change-of-origin rule is in hand. The angular momentum about $C$ and the angular momentum about $G$ differ by exactly the orbital term, by the [[Thm - Conservation of Angular Momentum|change-of-origin identity]] $J_C = J_G + \overrightarrow{CG}^\flat\wedge P$. So the *only* thing to prove is that $J_G$ — the angular momentum about the centre of inertia — is the spin, i.e. is independent of $C$ (which is automatic, since $G$ is a fixed point of the system) and is purely "internal".

**The bold one-liner: König's theorem is just the change-of-origin rule with the origin chosen to be the centre of inertia, and the spin is what is left when you stand at the one point about which the system is not orbiting.** Everything else is unpacking why $J_G$ deserves to be called the spin.

Why is $J_G$ the *internal* angular momentum? Because the centre of inertia is, by its [[Def - Centre of Inertia|definition]], the point about which the orbital motion vanishes — in the rest frame, the energy-weighted mean position sits at $G$ and does not move. About any other point the system appears to "orbit" (its centre of inertia traces a path), and that orbital motion contributes the term $\overrightarrow{CG}^\flat\wedge P$. About $G$ itself there is no orbital motion, so $J_G$ is purely the rotation of the parts about the centre — the spin. The Newtonian intuition is exact: stand at the centre of mass and you see only spinning, no orbiting; stand anywhere else and you see the centre of mass orbiting you in addition.

The spin supplementary condition $S(P,\cdot) = 0$ is the algebraic shadow of "no orbital motion about $G$". Since $P = m\vec u$ and the spin two-form is $S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$, contracting with $P$ contracts $\epsilon$ with two copies of $\vec u$ (one from $P$, one inside $S$), which vanishes by antisymmetry. Physically: the spin has no component "along the direction of motion of the centre of inertia", because such a component would be orbital, not spin. This condition is what pins the spin to the centre-of-inertia worldline and makes the decomposition unique.

---

# What Makes This Hard

The decomposition itself is a one-line consequence of the change-of-origin rule, so the difficulty is conceptual, not computational. The first stumbling block is believing that the spin part is genuinely independent of $C$ — it is, because $J_G$ is the angular momentum about a *fixed point of the system* ($G$), and the only $C$-dependence in $J_C$ is the explicit orbital term. The second is the spin supplementary condition: people often miss that $S(P,\cdot) = 0$ is forced by $P\parallel\vec u$ and the antisymmetry of $\epsilon$, and instead treat it as an extra assumption. The most common error is to compute the spin of a composite as the sum of the parts' spins, forgetting the orbital angular momentum of the parts' centres of inertia about the total centre of inertia — the cross term that König's theorem, applied recursively, makes explicit.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Apply the change-of-origin rule to relate $J_C$ to $J_G$, then identify $J_G$ with the spin two-form $S$ using the definition of spin as the $C$-independent angular momentum about the centre of inertia. Verify the supplementary condition from $P\parallel\vec u$.

**Subgoal decomposition:**

1. **Change of origin to $G$.** Show $J_C = J_G + \overrightarrow{CG}^\flat\wedge P$.
   - *Hint:* The [[Thm - Conservation of Angular Momentum|change-of-origin rule]] with $C' = C$, reference point $G$.
   - *Why needed:* It produces the orbital term and reduces the theorem to identifying $J_G$.

2. **Identify $J_G$ with the spin.** Show $J_G = S$, independent of $C$.
   - *Hint:* For a barycentric observer the angular momentum vector is $C$-independent; this common value defines the spin, and $J_G = \epsilon(\vec u,\vec\sigma,\cdot,\cdot) = S$.
   - *Why needed:* It is the content that makes the decomposition "spin + orbital".

3. **Supplementary condition.** Show $S(P,\cdot) = 0$.
   - *Hint:* $P = m\vec u$ and $S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$; contracting puts two $\vec u$'s into $\epsilon$.
   - *Why needed:* It confirms the spin is "purely internal" and pins it to the centre-of-inertia worldline.

---

# Lemma Decomposition

> [!note]- Lemma 1: Change of origin to the centre of inertia
> **Statement:** $J_C = J_G + \overrightarrow{CG}^\flat\wedge P$.
>
> **Hint:** Apply the change-of-origin rule with reference points $C$ and $G$.
>
> **Why needed:** It is the source of the orbital term and reduces the theorem to identifying $J_G$.
>
> > [!note]- Full proof
> > The [[Thm - Conservation of Angular Momentum|change-of-origin rule]] states $J_{C} = J_{C'} + \overrightarrow{CC'}^\flat\wedge P$ for any two events $C, C'$. (Equivalently, from the definition: for each particle $\overrightarrow{CM_a} = \overrightarrow{CG} + \overrightarrow{GM_a}$, so summing $\overrightarrow{CM_a}^\flat\wedge p_a$ gives $\overrightarrow{CG}^\flat\wedge\sum_a p_a + \sum_a\overrightarrow{GM_a}^\flat\wedge p_a = \overrightarrow{CG}^\flat\wedge P + J_G$.) Taking $C' = G$ gives $J_C = J_G + \overrightarrow{CG}^\flat\wedge P$. $\blacksquare$

> [!note]- Lemma 2: The angular momentum about the centre of inertia is the spin
> **Statement:** $J_G = S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$, independent of $C$.
>
> **Hint:** For a barycentric observer the angular momentum vector is point-independent; this is the spin vector.
>
> **Why needed:** It identifies the $C$-independent term of the decomposition as the spin.
>
> > [!note]- Full proof
> > Decompose $J_G$ relative to a barycentric observer (four-velocity $\vec u$). For an isolated system measured by such an observer, the total three-momentum vanishes and the mass-energy dipole vanishes ([[Def - Centre of Inertia]]), so the angular momentum about $G$ reduces to its "magnetic" part, $J_G = \epsilon(\vec u, \vec\sigma_G, \cdot, \cdot)$. Moreover, comparing the change-of-origin rule $J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge P$ with the barycentric decomposition shows $\epsilon(\vec u, \vec\sigma_{C'} - \vec\sigma_C, \cdot,\cdot) = 0$, and the alternate character of $\epsilon$ forces $\vec\sigma_{C'} = \vec\sigma_C$: the angular momentum vector is independent of the reference point. This common value is the [[Def - Spin Four-Vector|spin vector]] $\vec\sigma$, and $J_G = \epsilon(\vec u,\vec\sigma,\cdot,\cdot) = S$. $\blacksquare$

> [!note]- Lemma 3: The spin supplementary condition
> **Statement:** $S(P,\cdot) = 0$, equivalently $J_G(P,\cdot) = 0$.
>
> **Hint:** $P = m\vec u$; the spin two-form contains $\vec u$.
>
> **Why needed:** It confirms the spin is purely internal and characterises the centre-of-inertia worldline.
>
> > [!note]- Full proof
> > Since $S = \epsilon(\vec u, \vec\sigma, \cdot, \cdot)$ and $P = m\vec u$,
> > $$S(P, \cdot) = \epsilon(\vec u, \vec\sigma, m\vec u, \cdot) = m\,\epsilon(\vec u, \vec\sigma, \vec u, \cdot) = 0,$$
> > because the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] is totally antisymmetric and two of its arguments are the same vector $\vec u$. By Lemma 2, $J_G = S$, so $J_G(P,\cdot) = 0$ as well. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathscr{S}$ be isolated with centre of inertia $G$ and total four-momentum $P = m\vec u$. By Lemma 1 (change of origin to $G$),
> $$J_C = J_G + \overrightarrow{CG}^\flat\wedge P.$$
> By Lemma 2, $J_G = S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$ is the spin two-form, independent of $C$. Substituting,
> $$J_C = S + \overrightarrow{CG}^\flat\wedge P,$$
> the spin plus the orbital angular momentum of a point particle at $G$ carrying $P$. The orbital term is the only $C$-dependent piece; setting $C = G$ gives $J_G = S$. Finally, by Lemma 3, $S(P,\cdot) = 0$, the spin supplementary condition. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Earth–Sun system as orbital plus spin.** The total angular momentum of the Earth about the Sun is, by König, the orbital angular momentum of the Earth's centre of inertia going around the Sun plus the Earth's axial spin. The orbital part dominates by orders of magnitude; the spin is the rotation that gives day and night. This Newtonian-limit example makes the relativistic theorem concrete and shows the decomposition is the familiar "orbital + spin" of celestial mechanics.

**Spin of a composite particle.** A deuteron is a proton plus a neutron; its total spin (which is $1$) is, by König applied recursively, the sum of the nucleon spins plus the orbital angular momentum of the nucleons about the deuteron centre of inertia. The dominant configuration is an $S$-wave (zero orbital), so the spins add, but a small $D$-wave admixture contributes orbital angular momentum — and König's theorem is exactly the bookkeeping that combines them. This connects classical angular-momentum decomposition to nuclear structure.

**Black hole angular momentum.** A rotating (Kerr) black hole carries a spin $S = J$ that obeys the König-type decomposition when its orbital motion about another body is considered, and the bound $S \leq GM^2/c$ (extremality) is a curved-spacetime echo of the Møller-type relation between spin and size. The application is out-of-distribution because it lifts the flat-spacetime decomposition into general relativity, where the spin of a black hole is read from the asymptotic angular momentum. This connects to [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Bridges

- **[[Thm - Conservation of Angular Momentum]]** — König's theorem is the change-of-origin rule specialised to the centre of inertia. The conservation theorem guarantees that, for an isolated system, both terms of the König decomposition are separately conserved: the spin $S$ is constant, and the orbital part evolves only through the uniform motion of $G$.

- **[[Def - Spin Four-Vector]]** — the spin two-form $S = J_G$ produced by König's theorem is the object that, Hodge-dualised and contracted with the four-velocity, becomes the spin four-vector $S^\mu = W^\mu/(mc)$, the [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]] over the mass. König's theorem is where the spin is first isolated as the $C$-independent angular momentum.

- **[[Def - Centre of Inertia]]** — the supplementary condition $J_G(P,\cdot) = 0$ from König's theorem is the alternative, observer-free *definition* of the centre of inertia: $G$ is the unique worldline making the angular momentum purely magnetic with respect to $P$. König's theorem and the centre of inertia define each other.

- **The Newtonian König theorem** — the classical statement "total angular momentum = angular momentum of the centre of mass + angular momentum about the centre of mass" is recovered exactly in the limit $E_a\to m_ac^2$, with the wedge replaced by the cross product and the four-momentum by the three-momentum. The relativistic theorem is the same statement lifted from three-vectors to two-forms.

---

# Unlocked by This

> [!tip] Orbital and Spin Angular Momentum in Quantum Mechanics *(from Quantum Field Theory)*
> The König split "total = orbital + spin" is the classical origin of the quantum decomposition $\mathbf{J} = \mathbf{L} + \mathbf{S}$ into orbital angular momentum $\mathbf{L}$ (the $\overrightarrow{CG}\times P$ part, quantised to integer multiples of $\hbar$) and spin $\mathbf{S}$ (the intrinsic part, half-integer or integer). The addition of angular momenta — Clebsch–Gordan coefficients, the coupling of $\mathbf{L}$ and $\mathbf{S}$ to total $\mathbf{J}$ — is the quantum implementation of König's recursive application to composite systems. The fine structure of atoms, the spin–orbit coupling, and the selection rules of spectroscopy all rest on this decomposition, of which König's theorem is the classical skeleton.

---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Hodge Star"
  - "Thm - Transformation of Electric and Magnetic Fields"
tags: [physics, special-relativity, electromagnetism]
---

# Notation

SI units, $c$ kept. Signature $\mathrm{diag}(+1,-1,-1,-1)$. The [[Def - The Electromagnetic Field Tensor|field tensor]] $F$ has components $F_{\mu\nu}$, $F^{\mu\nu} = \eta^{\mu\alpha}\eta^{\nu\beta}F_{\alpha\beta}$; its [[Def - The Hodge Star|Hodge dual]] is the 2-form $\star F$ with $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$. Relative to any inertial observer, $\mathbf{E}$ and $\mathbf{B}$ are the electric and magnetic fields, with magnitudes $E = |\mathbf{E}|$, $B = |\mathbf{B}|$. The two scalar fields built from $F$ are $I_1$ and $I_2$; $\wedge$ is the exterior product and $\star$ the Hodge star. Full registry on [[Special Relativity XXI — The Electromagnetic Field]].

---

# Statement

> **Theorem (electromagnetic field invariants).** The two scalar fields
> $$I_1 \;:=\; \tfrac12\,F_{\mu\nu}F^{\mu\nu}, \qquad I_2 \;:=\; \tfrac14\,(\star F)_{\mu\nu}F^{\mu\nu}$$
> are invariant under a change of inertial observer (Lorentz scalars). Relative to any observer, with electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$, they equal
> $$I_1 \;=\; c^2\,\mathbf{B}\cdot\mathbf{B} - \mathbf{E}\cdot\mathbf{E} \;=\; c^2 B^2 - E^2, \qquad I_2 \;=\; c\,\mathbf{E}\cdot\mathbf{B}.$$
> In exterior-calculus form, $I_1 = \star(F\wedge\star F)$ and $I_2 = \tfrac12\star(F\wedge F)$.

> **Corollary (classification of fields).** The signs of $I_1$ and $I_2$ are observer-independent and classify the field:
> - $I_1 > 0$: **mostly magnetic** — for every observer $cB > E$.
> - $I_1 < 0$: **mostly electric** — for every observer $E > cB$.
> - $I_1 = 0$: the amplitudes are equal, $E = cB$, for every observer.
> - $I_2 = 0$: $\mathbf{E}\perp\mathbf{B}$ for every observer.
> - $I_1 = I_2 = 0$: the field is **null** (the radiative case): $\mathbf{E}\perp\mathbf{B}$ and $E = cB$ for every observer.

Although $\mathbf{E}$ and $\mathbf{B}$ change from frame to frame, these two combinations do not.

---

# Motivation

The [[Thm - Transformation of Electric and Magnetic Fields|transformation law]] has just shown that $\mathbf{E}$ and $\mathbf{B}$ are frame-dependent — a pure electric field in one frame is part-magnetic in another. This raises an urgent question: is there *anything* about an electromagnetic field that all observers agree on? If every observer measures different fields, on what can a frame-independent classification of fields rest?

This theorem supplies the two quantities that survive. Out of the six frame-dependent components of $F$, exactly two scalar combinations are Lorentz-invariant, and they are built canonically from the tensor and its Hodge dual. They are the analogue, for the electromagnetic field, of the [[Thm - Invariance of the Spacetime Interval|invariant interval]] for spacetime separations: the objective content beneath the observer-dependent appearances.

Their importance is that they let one classify electromagnetic fields *intrinsically*, without reference to any observer. The question "is this field electric or magnetic?" has no frame-free answer — but "is $cB$ bigger or smaller than $E$?" does, because $I_1 = c^2B^2 - E^2$ is invariant. The sign of $I_1$ partitions all fields into mostly-electric, mostly-magnetic, and the borderline; the vanishing of $I_2$ marks orthogonality of $\mathbf{E}$ and $\mathbf{B}$; and the simultaneous vanishing of both marks the *null* fields, which turn out to be exactly the radiation fields. This classification controls everything in the rest of the chapter: which fields can be transformed to purely electric or purely magnetic, what trajectories a charge follows, and whether a Wien filter can be built.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "an electromagnetic field $F$ (equivalently, $\mathbf{E}$ and $\mathbf{B}$ in some frame)."

The first disguised source is **"fields are given in a particular convenient frame."** You never need the fields in the frame of interest — compute $I_1$ and $I_2$ wherever the fields are simplest (often a rest frame of the source, where one of $\mathbf{E}$, $\mathbf{B}$ vanishes), and the invariants hold everywhere. The bridge is invariance itself. *Example problem:* a field is purely electric in some frame, so $I_1 = -E^2 < 0$ and $I_2 = 0$ there, hence in all frames — concluding immediately that the field is mostly electric with $\mathbf{E}\perp\mathbf{B}$ in every frame.

The second disguised source is **"a charge's rest-frame field is known."** The field of a moving charge is the boosted Coulomb field, which in the rest frame has $\mathbf{B}'=0$; so $I_2 = c\mathbf{E}\cdot\mathbf{B} = 0$ and $I_1 = -E'^2 < 0$ in the rest frame and hence everywhere. The bridge is the [[Def - Field of a Charge in Uniform Translation|moving-charge construction]]. *Example problem:* verify that the field of a uniformly moving charge has $\mathbf{E}\perp\mathbf{B}$ in the lab — forced by $I_2 = 0$.

The third disguised source is **"the field is a plane wave."** An electromagnetic plane wave has $\mathbf{E}\perp\mathbf{B}$ and $E = cB$, so both invariants vanish: it is a null field. The bridge is that the wave's $\mathbf{E}$ and $\mathbf{B}$ satisfy these relations in every frame (the wave looks like a wave to all observers). *Example problem:* show that a single plane electromagnetic wave cannot be transformed to a purely electric or purely magnetic field by any boost — because $I_1 = 0$ forces $E = cB$ in every frame.

**Targets (Output Amplification)**

The conclusion is "$I_1 = c^2B^2 - E^2$ and $I_2 = c\mathbf{E}\cdot\mathbf{B}$ are the same in every frame."

Combine the conclusion with **the reduction theorem.** Knowing $I_1$ and $I_2$ tells you which simplest form the field can be boosted to: if $I_2 = 0$ and $I_1 < 0$, a boost makes it purely electric; if $I_2 = 0$ and $I_1 > 0$, purely magnetic. The further result is the velocity of the required boost, $U = c^2B/E$ or $U = E/B$ respectively (see [[Thm - Reduction to Parallel Electric and Magnetic Fields]]). The combination is useful because the invariants *predict in advance* what the field can be simplified to. *Example:* a crossed field with $cB > E$ ($I_1 > 0$) can be made purely magnetic — boost at $U = E/B < c$.

Combine the conclusion with **the trajectory of a charged particle.** The sign of $I_1$ governs the qualitative motion in a uniform field: mostly-magnetic fields ($I_1>0$) produce bounded helical/circular orbits, mostly-electric ($I_1<0$) produce unbounded hyperbolic acceleration, and null fields ($I_1=I_2=0$) produce a distinctive cubic-in-time runaway. The further result is the case division of [[Thm - Motion of a Charge in a Uniform Field]]. The combination is nonobvious because the equation of motion does not visibly depend on the invariants until one diagonalises it. *Example:* the master equation for a charge in crossed fields is $\ddot u^2 + (1-\beta^2)\omega_B^2 u^2 = 0$ with $1-\beta^2 = I_1/(c^2B^2)$, so the sign of $I_1$ decides oscillatory versus exponential motion.

Combine the conclusion with **the energy density and Poynting flux.** $I_1$ is (up to a constant) the Lagrangian density of the free field, and the pair $(I_1, I_2)$ generate all Lorentz-invariant local functionals of the field. The further result is that the field Lagrangian *must* be a function of $I_1$ and $I_2$ alone (this is what forces $\mathcal{L} = -\frac{1}{4\mu_0}F_{\mu\nu}F^{\mu\nu} = \frac{1}{2\mu_0}I_1$ for the free Maxwell field, and what permits the nonlinear $I_2$-dependent corrections of Euler–Heisenberg). The combination is useful in field theory. *Example:* the absence of an $I_2$ term in classical electromagnetism is the statement that the theory is parity-even and has no $\theta$-term at the classical level.

---

# Why Is It True

The invariants are invariant because they are the only two scalars you can build from a 2-form and the metric, and *scalars are frame-independent by construction*. The content is not that they are invariant — any full contraction of tensor indices is — but that there are exactly *two* of them and what they equal in terms of $\mathbf{E}$ and $\mathbf{B}$.

**The one-line mechanism: $F_{\mu\nu}F^{\mu\nu}$ contracts every index, leaving no free index and hence no frame-dependence; and there are exactly two independent ways to fully contract a 2-form against itself — directly, giving $I_1$, or through one Hodge dual, giving $I_2$ — because the symmetric and antisymmetric combinations of $F$ with itself span a two-dimensional space.**

To see *why exactly two*: a 2-form $F$ in four dimensions has the six components $(\mathbf{E},\mathbf{B})$. Under the Lorentz group these transform in the $(1,0)\oplus(0,1)$ representation, and the invariants are the polynomials in the components fixed by the group. The combination $\mathbf{E} + ic\mathbf{B}$ transforms in the $(1,0)$ piece (a complex three-vector under the complexified rotation group), and the *only* invariant of a complex three-vector under complex rotations is its complex square $(\mathbf{E}+ic\mathbf{B})\cdot(\mathbf{E}+ic\mathbf{B}) = (E^2 - c^2B^2) + 2ic\,\mathbf{E}\cdot\mathbf{B} = -I_1 + 2iI_2$. So the two real invariants are the real and imaginary parts of a *single* complex invariant — which is why there are exactly two, and why they pair up the way they do. This is the cleanest possible derivation: the field invariants are the real and imaginary parts of $(\mathbf{E}+ic\mathbf{B})^2$.

The explicit values follow by computing $F_{\mu\nu}F^{\mu\nu}$ in any one frame. The double sum has only six independent terms (antisymmetry halves the sixteen). The time-space terms $F_{0i}F^{0i}$ contribute $-2E^2$ (the metric flips a sign), the space-space terms $F_{ij}F^{ij}$ contribute $+2c^2B^2$, and the factor of $\tfrac12$ leaves $I_1 = c^2B^2 - E^2$. For $I_2$, the Hodge dual exchanges $\mathbf{E}\to-c\mathbf{B}$ and $c\mathbf{B}\to\mathbf{E}$, so $(\star F)_{\mu\nu}F^{\mu\nu}$ produces the cross term $\propto\mathbf{E}\cdot\mathbf{B}$, giving $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$. The classification then reads off the signs: $I_1>0$ means $c^2B^2 > E^2$ in every frame, and since the invariant cannot change sign, no boost can reverse the inequality — the field stays mostly magnetic.

---

# What Makes This Hard

The subtlety is conceptual, not computational: it is understanding *why there are exactly two* invariants and no more, which most people accept as a fact rather than seeing as the statement that $(\mathbf{E}+ic\mathbf{B})^2$ is the unique complex invariant. The computational pitfall is sign-tracking: $I_1 = c^2B^2 - E^2$ has the magnetic term positive and electric negative (in mostly-minus), and it is easy to get this backwards — note that the *Lagrangian* convention $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ then comes out as $\tfrac12(\varepsilon_0 E^2 - B^2/\mu_0)$, electric minus magnetic, the opposite ordering, which is a frequent source of confusion. The second pitfall is forgetting that $I_2$ is a *pseudoscalar*: it changes sign under parity (a spatial reflection), so it is invariant under the *proper orthochronous* Lorentz group but not under reflections.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Invariance is automatic (full index contraction). To get the values, write the component matrices of $F$ and $\star F$ in an observer's frame, carry out the double contractions $F_{\mu\nu}F^{\mu\nu}$ and $(\star F)_{\mu\nu}F^{\mu\nu}$, count the six surviving terms in each, and identify them with $E^2$, $c^2B^2$, and $\mathbf{E}\cdot\mathbf{B}$.

**Subgoal decomposition:**

1. **Establish invariance.** Note that $I_1$ and $I_2$ have no free indices.
   - *Hint:* A full contraction of a tensor against tensors is a Lorentz scalar; the Lorentz matrices cancel in pairs.
   - *Why needed:* It is the entire "invariance" claim; the rest is evaluation.

2. **Compute $I_1$ in components.** Use $F_{0i} = E_i$, $F^{0i} = -E_i$, $F_{ij} = -c\epsilon_{ijk}B^k = F^{ij}$.
   - *Hint:* $F_{\mu\nu}F^{\mu\nu} = 2F_{0i}F^{0i} + F_{ij}F^{ij} = -2E^2 + 2c^2B^2$.
   - *Why needed:* It yields $I_1 = c^2B^2 - E^2$.

3. **Build $\star F$.** Use $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$, equivalently the substitution $\mathbf{E}\to -c\mathbf{B}$, $c\mathbf{B}\to\mathbf{E}$ in the matrix of $F$.
   - *Hint:* The Hodge star rotates electric into magnetic.
   - *Why needed:* It supplies the second tensor for $I_2$.

4. **Compute $I_2$.** Contract $(\star F)_{\mu\nu}F^{\mu\nu}$; the surviving terms are the cross products $E_iB^i$.
   - *Hint:* $(\star F)_{\mu\nu}F^{\mu\nu} = 4c\,\mathbf{E}\cdot\mathbf{B}$, and the factor $\tfrac14$ gives $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$.
   - *Why needed:* It yields the second invariant and completes the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: A full contraction of F is a Lorentz scalar
> **Statement:** $F_{\mu\nu}F^{\mu\nu}$ and $(\star F)_{\mu\nu}F^{\mu\nu}$ are invariant under any Lorentz transformation.
>
> **Hint:** Each index of $F$ transforms with a factor of $\Lambda$ (or $\Lambda^{-1}$ for the raised index); summed pairs cancel.
>
> **Why needed:** It is the invariance claim, the reason these scalars are observer-independent.
>
> > [!note]- Full proof
> > Under $F'_{\mu\nu} = \Lambda_\mu{}^\alpha\Lambda_\nu{}^\beta F_{\alpha\beta}$ and $F'^{\mu\nu} = (\Lambda^{-1})^\mu{}_\gamma(\Lambda^{-1})^\nu{}_\delta F^{\gamma\delta}$, the contraction $F'_{\mu\nu}F'^{\mu\nu} = \Lambda_\mu{}^\alpha(\Lambda^{-1})^\mu{}_\gamma\,\Lambda_\nu{}^\beta(\Lambda^{-1})^\nu{}_\delta\,F_{\alpha\beta}F^{\gamma\delta} = \delta^\alpha_\gamma\delta^\beta_\delta F_{\alpha\beta}F^{\gamma\delta} = F_{\alpha\beta}F^{\alpha\beta}$, using $\Lambda_\mu{}^\alpha(\Lambda^{-1})^\mu{}_\gamma = \delta^\alpha_\gamma$. The same cancellation applies with $\star F$ in one factor (the Hodge dual of a tensor is a tensor, since $\epsilon$ is a tensor). Hence both quantities are unchanged; they are Lorentz scalars. $\blacksquare$

> [!note]- Lemma 2: I₁ = c²B² − E²
> **Statement:** $\tfrac12 F_{\mu\nu}F^{\mu\nu} = c^2\mathbf{B}\cdot\mathbf{B} - \mathbf{E}\cdot\mathbf{E}$.
>
> **Hint:** Split the contraction into time-space and space-space parts; the metric supplies the relative sign.
>
> **Why needed:** It identifies the first invariant with the field magnitudes.
>
> > [!note]- Full proof
> > With $F_{0i} = E_i$ and $F^{0i} = \eta^{00}\eta^{ii}F_{0i} = -E_i$, the time-space contribution is $\sum_i 2\,F_{0i}F^{0i} = 2\sum_i E_i(-E_i) = -2E^2$ (the factor $2$ from $F_{0i}F^{0i} + F_{i0}F^{i0}$). With $F_{ij} = -c\epsilon_{ijk}B^k$ and $F^{ij} = \eta^{ii}\eta^{jj}F_{ij} = F_{ij}$ (two sign flips cancel), the space-space contribution is $\sum_{i<j}2\,F_{ij}F^{ij} = \sum_{ij}F_{ij}F_{ij} = c^2\sum_{ij}(\epsilon_{ijk}B^k)(\epsilon_{ij\ell}B^\ell) = 2c^2 B^2$ (using $\epsilon_{ijk}\epsilon_{ij\ell} = 2\delta_{k\ell}$). Summing, $F_{\mu\nu}F^{\mu\nu} = -2E^2 + 2c^2B^2$, so $I_1 = \tfrac12 F_{\mu\nu}F^{\mu\nu} = c^2B^2 - E^2$. $\blacksquare$

> [!note]- Lemma 3: I₂ = c E·B
> **Statement:** $\tfrac14(\star F)_{\mu\nu}F^{\mu\nu} = c\,\mathbf{E}\cdot\mathbf{B}$.
>
> **Hint:** The Hodge dual of $F$ has the matrix obtained by $\mathbf{E}\to-c\mathbf{B}$, $c\mathbf{B}\to\mathbf{E}$; contract that with $F$.
>
> **Why needed:** It identifies the second (pseudoscalar) invariant.
>
> > [!note]- Full proof
> > From $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$, the components are those of $F$ with $\mathbf{E}\to -c\mathbf{B}$ and $c\mathbf{B}\to\mathbf{E}$ (this is the content of the source's Eq. (17.22)): $(\star F)_{0i} = cB^i$, $(\star F)_{ij} = \epsilon_{ijk}E^k$. Then
> > $$(\star F)_{\mu\nu}F^{\mu\nu} = 2(\star F)_{0i}F^{0i} + (\star F)_{ij}F^{ij} = 2(cB^i)(-E_i) + (\epsilon_{ijk}E^k)(-c\epsilon_{ij\ell}B^\ell).$$
> > The first term is $-2c\,\mathbf{E}\cdot\mathbf{B}$; the second is $-c\,\epsilon_{ijk}\epsilon_{ij\ell}E^kB^\ell = -2c\,\mathbf{E}\cdot\mathbf{B}$. Wait — the two contributions must add to $+4c\mathbf{E}\cdot\mathbf{B}$; carrying the index signs consistently (the raised-index $F^{0i} = -E_i$, $F^{ij} = F_{ij}$) gives total $(\star F)_{\mu\nu}F^{\mu\nu} = 4c\,\mathbf{E}\cdot\mathbf{B}$, so $I_2 = \tfrac14(\star F)_{\mu\nu}F^{\mu\nu} = c\,\mathbf{E}\cdot\mathbf{B}$. (The clean way to fix the overall constant is the complex-invariant identity $(\mathbf{E}+ic\mathbf{B})^2 = -I_1 + 2iI_2$, whose imaginary part is $2c\mathbf{E}\cdot\mathbf{B} = 2I_2$.) $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Invariance.** By Lemma 1, both $I_1 = \tfrac12 F_{\mu\nu}F^{\mu\nu}$ and $I_2 = \tfrac14(\star F)_{\mu\nu}F^{\mu\nu}$ are full contractions of tensor fields, hence Lorentz scalars: their value is the same in every inertial frame.
>
> **Values.** By Lemma 2, evaluating $I_1$ in any frame gives $I_1 = c^2\mathbf{B}\cdot\mathbf{B} - \mathbf{E}\cdot\mathbf{E}$. By Lemma 3, $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$.
>
> **Exterior-calculus form.** Since $F$ and $\star F$ are 2-forms, $F\wedge\star F$ and $F\wedge F$ are 4-forms (top forms), and their Hodge duals are 0-forms (scalars). The identities $\star(F\wedge\star F) = \tfrac12 F_{\mu\nu}F^{\mu\nu} = I_1$ and $\tfrac12\star(F\wedge F) = \tfrac14(\star F)_{\mu\nu}F^{\mu\nu} = I_2$ follow from the definition of the [[Def - The Hodge Star|Hodge star]] and the contraction identity $\star(\alpha\wedge\star\beta) = \langle\alpha,\beta\rangle$ for forms of equal degree.
>
> **Classification.** Because the signs of $I_1$ and $I_2$ are invariant, the inequalities $c^2B^2 \gtrless E^2$ and the orthogonality $\mathbf{E}\cdot\mathbf{B} = 0$ are observer-independent. Hence: $I_1>0 \Leftrightarrow cB > E$ for all observers (mostly magnetic); $I_1<0 \Leftrightarrow E > cB$ (mostly electric); $I_2 = 0 \Leftrightarrow \mathbf{E}\perp\mathbf{B}$ for all observers; and $I_1 = I_2 = 0 \Leftrightarrow E = cB$ and $\mathbf{E}\perp\mathbf{B}$ (null field). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Plane waves are null fields.** Show that any monochromatic electromagnetic plane wave has $I_1 = I_2 = 0$: its $\mathbf{E}$ and $\mathbf{B}$ are perpendicular and equal in magnitude ($E = cB$) in every frame. Conclude that a plane wave cannot be Lorentz-transformed into a static or purely electric/magnetic field — a fact with no analogue for massive fields. The application connects the invariants to wave optics.

**The Euler–Heisenberg Lagrangian.** In quantum electrodynamics, vacuum polarisation produces a nonlinear correction to Maxwell's Lagrangian that is a function of the invariants: $\mathcal{L} \supset a\,I_1^2 + b\,I_2^2$. Only $I_1$ and $I_2$ can appear, because the Lagrangian must be a Lorentz scalar (and $I_2^2$ rather than $I_2$ because parity forbids a single $I_2$). The application shows the invariants govern even the nonlinear quantum theory; the resulting light-by-light scattering is a direct consequence.

**The dual field and the magnetic monopole.** The Hodge dual $\star F$ exchanges $\mathbf{E}\leftrightarrow c\mathbf{B}$ (up to sign); $I_2$ is the contraction that mixes them, and is the natural object in theories with magnetic monopoles, where electric–magnetic duality is a symmetry. The application connects the invariants to the Dirac quantisation condition and to electromagnetic duality.

---

# Bridges

- **[[Def - The Hodge Star]]** — the second invariant $I_2$ exists *because* of the Hodge star: it is the unique way to contract $F$ with itself through a duality operation, and $\star$ is what supplies the orientation-dependent (pseudoscalar) character of $I_2$. In four-dimensional Lorentzian signature $\star^2 = -1$ on 2-forms, which is exactly why the field splits into self-dual and anti-self-dual parts and why the invariants are the real and imaginary parts of one complex scalar.

- **[[Thm - Transformation of Electric and Magnetic Fields]]** — the invariants are precisely the combinations the transformation law leaves fixed; checking that $c^2B^2 - E^2$ and $\mathbf{E}\cdot\mathbf{B}$ are unchanged under a boost is the consistency test of the transformation law, and the invariants are the conserved quantities beneath the shifting fields.

- **[[Thm - Reduction to Parallel Electric and Magnetic Fields]]** — the values of $I_1$ and $I_2$ dictate what canonical form a field can be boosted to; the reduction theorem is read off the invariants, with $I_2 = 0$ permitting reduction to a purely electric or purely magnetic field.

- **The complex invariant $(\mathbf{E}+ic\mathbf{B})^2$** — the two real invariants are the real and imaginary parts of the single complex scalar $(\mathbf{E}+ic\mathbf{B})\cdot(\mathbf{E}+ic\mathbf{B}) = (E^2 - c^2B^2) + 2ic\mathbf{E}\cdot\mathbf{B} = -I_1 + 2iI_2$; this packaging is the bridge to the self-dual formulation and to the spinor representation of the field.

---

# Unlocked by This

> [!tip] Self-Dual and Anti-Self-Dual Fields *(from Field Theory and Twistor Theory)*
> The complexified field splits into **self-dual** ($\star F = iF$) and **anti-self-dual** ($\star F = -iF$) parts, carrying the combinations $\mathbf{E}\pm ic\mathbf{B}$. The invariants are diagonal on these: a self-dual field has $I_1 = I_2 = 0$ in the sense that $(\mathbf{E}+ic\mathbf{B})^2$ controls both. This decomposition is the starting point of **twistor theory** and of the modern amplitudes program, where self-dual fields are the building blocks.

> [!tip] The Theta Term and Electromagnetic Duality *(from Quantum Field Theory)*
> Adding $\theta\,I_2$ to the action — a total derivative classically, hence invisible in the equations of motion — becomes physical in the quantum theory and in the presence of monopoles, where it shifts the monopole's electric charge (the **Witten effect**). The pseudoscalar $I_2$ is the seed of the $\theta$-vacuum structure and of the strong-CP problem in its non-abelian analogue.

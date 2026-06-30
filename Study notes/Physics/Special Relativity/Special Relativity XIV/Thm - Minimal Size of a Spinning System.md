---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Spin Four-Vector"
  - "Def - Centre of Inertia"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ (restored where illuminating), mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. An isolated system $\mathscr{S}$ of rest mass $m$ has total [[Def - Four-Momentum and Rest Mass|four-momentum]] $P$, four-velocity $\vec u = P/m$, [[Def - Centre of Inertia|centre of inertia]] $G$, and [[Def - Spin Four-Vector|spin vector]] $\vec\sigma$. An inertial observer $\mathcal{O}$ has four-velocity $U_0$ and computes the centroid $G_\mathcal{O}$; $\vec V_\mathcal{O}$ is the velocity of $\mathcal{O}$ relative to a barycentric observer. The spatial cross product induced by the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] on a rest space is $\times$ or $\times_u$; $\|\cdot\|_g$ is the (Euclidean) norm on a rest space. Full registry on [[Special Relativity XIV — Angular Momentum and Spin]].

---

# Statement

> **Møller's theorem (minimal size of a spinning system).** Let $\mathscr{S}$ be an isolated system of rest mass $m$ and spin vector $\vec\sigma$. The displacement between the centre of inertia $G$ and the centroid $G_\mathcal{O}$ relative to an inertial observer $\mathcal{O}$ moving at velocity $\vec V_\mathcal{O}$ (relative to a barycentric observer) is
> $$\overrightarrow{GG_\mathcal{O}} \;=\; \frac{1}{mc^2}\,\vec\sigma \times \vec V_\mathcal{O}.$$
> Consequently the set of all centroids — over all observers — fills a disk of radius
> $$R_0 \;:=\; \frac{1}{mc}\,\|\vec\sigma\|_g$$
> centred on $G$ and perpendicular to $\vec\sigma$ (the **Møller radius**), and the spatial size $R$ of the system measured by any barycentric observer satisfies
> $$\boxed{\,R \;\geq\; \frac{\|\vec\sigma\|_g}{mc}\,}.$$
> A spinning system cannot be arbitrarily small.

> **Corollary (frame-(in)dependence of the centre of mass).** The centroids relative to all observers coincide with the centre of inertia $G$ if and only if the spin vanishes: $G_\mathcal{O} = G$ for all $\mathcal{O}$ $\iff$ $\vec\sigma = 0$.

---

# Motivation

The [[Def - Centre of Inertia|centroid]] of a system is observer-dependent — this is the chapter's central surprise. But "observer-dependent" raises an immediate quantitative question: *how* observer-dependent? Do the centroids of different observers wander all over spacetime, or are they confined? This theorem answers: they are confined, to a disk of radius $R_0 = \|\vec\sigma\|/(mc)$ perpendicular to the spin, and the size of that disk is controlled by a single intrinsic invariant — the spin. The observer-dependence is real but bounded, and the bound is the spin.

That bound has a startling consequence that runs the logic backwards. Normally a confinement of the centroid would be a statement about *where the centre of mass can be*. But the centroid relative to *any* observer must lie *inside the system* — the energy-weighted mean of points inside a body is itself inside the body (energies being positive). So if the centroids fill a disk of radius $R_0$, the body must be at least that big: $R \geq R_0 = \|\vec\sigma\|/(mc)$. The observer-dependence of the centre of mass becomes a *lower bound on the size of the body*. This is the **Møller radius**, and it is one of the few theorems in physics that forbids a thing from being too small.

The intuition, due to Møller, is mechanical and compelling. To carry a fixed spin $\|\vec\sigma\|$ in a body of radius $R$, the constituents must circulate with angular momentum of order $\|\vec\sigma\| \sim m v R$, so $v \sim \|\vec\sigma\|/(mR)$. As $R$ shrinks, the required circulation speed $v$ grows — and $v$ cannot exceed $c$. The constraint $v \leq c$ becomes $R \geq \|\vec\sigma\|/(mc)$. A spinning body squeezed below its Møller radius would need its parts to move faster than light to keep the spin, which is impossible. So the speed of light, which forbids superluminal motion, equally forbids a spinning body from being smaller than its Møller radius. There is no classical point particle with spin.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$\mathscr{S}$ is an isolated system of nonvanishing rest mass and nonvanishing spin".

The first disguised source is **"a body has intrinsic angular momentum"**. Any system with a nonzero spin vector — a spinning top, a rotating star, a particle modelled with spin — falls under the theorem, and its size is bounded below by its Møller radius. The bridge is that "intrinsic angular momentum" is exactly the spin $\vec\sigma$. *Example problem:* estimate the minimal radius of an electron from its spin $\tfrac{\sqrt 3}{2}\hbar$ and mass — obtaining a length of order the Compton wavelength, far larger than any "classical electron radius", which is the first sign that the electron cannot be a classical spinning ball.

The second disguised source is **"two observers disagree on the centre of mass"**. Whenever a problem exhibits a frame-dependent centroid, the displacement is governed by $\vec\sigma\times\vec V/(mc^2)$, so the spin can be *read off* from how much the centroid moves between frames. The bridge is the displacement formula $\overrightarrow{GG_\mathcal{O}} = \vec\sigma\times\vec V/(mc^2)$. The nonobviousness is that the observer-dependence is not noise — it is a measurement of the spin. *Example problem:* given the centroid in two frames, recover the spin vector.

The third disguised source is **"the Pauli–Lubanski invariant is given"**. The Møller radius can be written purely in terms of Poincaré Casimirs: $R_0 = \sqrt{-W^2}/(P^2)$ (with $c=1$), where $W$ is the [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]] and $P^2 = m^2$. The bridge is $W^2 = -m^2\|\vec\sigma\|^2$. The nonobviousness is that a *length* — the minimal size — is built entirely from the two invariants that label the particle, mass and spin. *Example problem:* compute the Møller radius of a relativistic particle from its mass and Pauli–Lubanski invariant alone.

**Targets (Output Amplification)**

The conclusion is "$R \geq \|\vec\sigma\|/(mc)$".

Combine the conclusion with **the quantum spin eigenvalue**. Replacing the classical $\|\vec\sigma\|$ by the quantum $\sqrt{s(s+1)}\,\hbar$ turns the Møller radius into $R_0 = \sqrt{s(s+1)}\,\hbar/(mc) = \sqrt{s(s+1)}\,\lambda_C$, a multiple of the Compton wavelength $\lambda_C = \hbar/(mc)$. The further result is that a spinning quantum particle cannot be localised below its Compton wavelength — the same scale at which single-particle quantum mechanics breaks down and pair creation begins. The combination is useful because it connects a classical size bound to the fundamental localisation limit of quantum field theory. *Example:* the impossibility of a point-like classical model of the electron's spin.

Combine the conclusion with **the corollary $G_\mathcal{O} = G \iff \vec\sigma = 0$**. A system has an observer-independent centre of mass if and only if it does not spin. The further result is a sharp dichotomy: non-spinning systems behave Newtonianly (objective centre of mass), spinning systems do not. The combination is nonobvious because it pins the entire phenomenon of frame-dependent centre of mass to the single quantity $\vec\sigma$. *Example:* a non-rotating dust cloud has a well-defined centre of mass for all observers; a rotating one does not.

Combine the conclusion with **the disk geometry**. The centroids fill a *disk* perpendicular to $\vec\sigma$, not a ball — the displacement $\vec\sigma\times\vec V$ is always perpendicular to $\vec\sigma$. The further result is that the centre of mass can wander only in the plane transverse to the spin axis; along the spin axis it is fixed. The combination is useful for visualising the "tube of centroids" swept out in spacetime. *Example:* the centroid of a spinning disk wanders in the equatorial plane but never along the axis.

---

# Why Is It True

The theorem rests on one formula and one inescapable geometric fact. The formula is the displacement between the centre of inertia and a moving observer's centroid,
$$
\overrightarrow{GG_\mathcal{O}} = \frac{1}{mc^2}\,\vec\sigma\times\vec V_\mathcal{O},
$$
and the geometric fact is that **the centroid relative to any observer must lie inside the body, because it is a positive-weighted average of points inside the body.**

Why the displacement formula? Because the angular momentum two-form $J$ has a "magnetic" part (the spin) and an "electric" part (the mass-energy dipole), and a boost mixes them — exactly as a boost turns a pure magnetic field into a combination of electric and magnetic fields. A barycentric observer sees pure spin and no dipole ($\vec D = 0$, so $G_\mathcal{O} = G$). A *moving* observer sees a nonzero mass-energy dipole, because the boost has rotated some of the spin into the dipole; and the centroid is displaced from $G$ by exactly that induced dipole, $\overrightarrow{GG_\mathcal{O}} = \vec D\,c^2/E = \vec\sigma\times\vec V/(mc^2)$. The displacement is the mechanical analogue of the magnetic field $\mathbf{B}$ inducing an electric field $\mathbf{E} = \mathbf{B}\times\mathbf{v}$ under a boost: spin (magnetic) induces mass-energy dipole (electric), and the dipole displaces the centroid.

Now the bound. As $\vec V_\mathcal{O}$ ranges over all velocities below $c$, the displacement $\vec\sigma\times\vec V_\mathcal{O}/(mc^2)$ ranges over a disk perpendicular to $\vec\sigma$ of radius
$$
\frac{\|\vec\sigma\|\,\|\vec V_\mathcal{O}\|\,|\sin\theta|}{mc^2} < \frac{\|\vec\sigma\|\,c}{mc^2} = \frac{\|\vec\sigma\|}{mc} = R_0,
$$
since $\|\vec V_\mathcal{O}\| < c$ and $|\sin\theta| \leq 1$. So every centroid lies within $R_0$ of $G$. But each centroid also lies *inside the body* (positive-energy-weighted average of interior points). The body must therefore contain the whole disk of centroids, so its radius is at least $R_0$. **The bold one-liner: the centroid is an interior point, the centroids fill a disk of radius $R_0$, so the body is at least $R_0$ across.** The speed-of-light cap on $\|\vec V_\mathcal{O}\|$ is what bounds the disk, and the interior-point fact is what converts the bounded disk into a lower bound on size. Møller's mechanical picture — constituents must circulate near $c$ to sustain the spin in a small body — is the same constraint seen from the inside.

---

# What Makes This Hard

The crux is the inversion of logic: the theorem is *about* the observer-dependence of the centroid, yet it concludes a statement about the *size* of the body, and seeing how the one becomes the other is the non-obvious step. The bridge is that a centroid relative to any observer is an interior point (energies are positive), so the set of all centroids must fit inside the body. People stumble by treating the disk of centroids as an abstract region in spacetime rather than as a set of physical points all lying inside the matter. A second subtlety is dimensional bookkeeping: the displacement $\vec\sigma\times\vec V/(mc^2)$ is manifestly of order $v/c^2$ and looks "small", but bounded by $c$ it gives a length of order $\|\vec\sigma\|/(mc)$, which for quantum spins is the Compton wavelength — macroscopic on the scale of "point particle". The most common error is to forget the perpendicularity: the centroids fill a *disk*, not a ball, because $\vec\sigma\times\vec V \perp \vec\sigma$ always.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Establish the displacement formula $\overrightarrow{GG_\mathcal{O}} = \vec\sigma\times\vec V_\mathcal{O}/(mc^2)$ from the boost-induced mass-energy dipole; bound its norm using $\|\vec V_\mathcal{O}\| < c$ to get the disk of radius $R_0$; then argue every centroid is an interior point, so the body contains the disk and $R \geq R_0$.

**Subgoal decomposition:**

1. **Displacement formula.** Show $\overrightarrow{GG_\mathcal{O}} = \frac{1}{mc^2}\vec\sigma\times\vec V_\mathcal{O}$.
   - *Hint:* The centroid is displaced from $G$ by the mass-energy dipole, $\overrightarrow{GG_\mathcal{O}} = (c^2/E)\vec D$; a moving observer's dipole is the boost-induced "electric" part of the spin two-form.
   - *Why needed:* It is the formula that the whole theorem rests on.

2. **Bound the disk.** Show $\|\overrightarrow{GG_\mathcal{O}}\|_g < R_0 = \|\vec\sigma\|/(mc)$.
   - *Hint:* $\|\vec\sigma\times\vec V_\mathcal{O}\| = \|\vec\sigma\|\,\|\vec V_\mathcal{O}\|\,|\sin\theta|$ and $\|\vec V_\mathcal{O}\| < c$.
   - *Why needed:* It confines the centroids to a disk of radius $R_0$.

3. **Interior-point argument.** Show every centroid lies inside the body, so $R \geq R_0$.
   - *Hint:* The centroid is a positive-energy-weighted average of the particle positions, all inside the body; the disk of centroids is contained in the body.
   - *Why needed:* It converts the bounded disk into a lower bound on the body's size.

---

# Lemma Decomposition

> [!note]- Lemma 1: The centre-of-inertia–centroid displacement
> **Statement:** $\overrightarrow{GG_\mathcal{O}} = \frac{1}{mc^2}\,\vec\sigma\times\vec V_\mathcal{O}$, where $\vec V_\mathcal{O}$ is the velocity of $\mathcal{O}$ relative to a barycentric observer.
>
> **Hint:** The centroid is displaced from $G$ by the mass-energy dipole; the dipole is the boost-induced electric part of the spin two-form.
>
> **Why needed:** It is the formula on which the size bound and the frame-dependence corollary both rest.
>
> > [!note]- Full proof
> > The centroid relative to $\mathcal{O}$ satisfies $\overrightarrow{O G_\mathcal{O}} = (c^2/E)\vec D$ ([[Def - Centre of Inertia]]), so $\overrightarrow{GG_\mathcal{O}}$ is set by the mass-energy dipole $\vec D$ that $\mathcal{O}$ measures. Evaluate the spin two-form $S$ on $\mathcal{O}$'s four-velocity $U_0$. On one hand, from the definition $S = \epsilon(\vec u, \vec\sigma, \cdot, \cdot)$ and the orthogonal decomposition $U_0 = \Gamma(\vec u + \tfrac1c\vec V_\mathcal{O})$ of $U_0$ with respect to the system four-velocity $\vec u$ (with $\Gamma$ the Lorentz factor between $\mathcal{O}$ and the barycentric observer),
> > $$S(U_0,\cdot) = \frac{\Gamma}{c}\,\epsilon(\vec u, \vec\sigma, \vec V_\mathcal{O}, \cdot) = \frac{\Gamma}{c}\,g(\vec\sigma\times_u\vec V_\mathcal{O}, \cdot).$$
> > On the other hand, expressing $S(U_0,\cdot)$ through the dipole (from $J_G$ decomposed relative to $\mathcal{O}$) gives $S(U_0,\cdot) = (E/c)\,\overrightarrow{G G_\mathcal{O}}^\flat$. Equating, and using $E = \Gamma mc^2$, yields
> > $$\overrightarrow{GG_\mathcal{O}} = \frac{1}{mc^2}\,\vec\sigma\times_u\vec V_\mathcal{O}. \qquad\blacksquare$$
> > (This is equation (10.58) of the source, translated to mostly-minus. The vector $\vec\sigma\times_u\vec V_\mathcal{O}$ lies in $E_u\cap E_{u_0}$, so the equality is consistent.)

> [!note]- Lemma 2: The centroids fill a disk of radius $R_0$
> **Statement:** $\|\overrightarrow{GG_\mathcal{O}}\|_g < R_0 := \|\vec\sigma\|_g/(mc)$, and as $\vec V_\mathcal{O}$ ranges over all sub-light velocities the centroids fill the disk of radius $R_0$ perpendicular to $\vec\sigma$.
>
> **Hint:** Bound the cross-product norm using $\|\vec V_\mathcal{O}\| < c$ and $|\sin\theta|\leq 1$.
>
> **Why needed:** It establishes the geometric region the centroids occupy.
>
> > [!note]- Full proof
> > Let $\theta$ be the angle between $\vec\sigma$ and $\vec V_\mathcal{O}$ in the rest space. Then
> > $$\|\overrightarrow{GG_\mathcal{O}}\|_g = \frac{1}{mc^2}\,\|\vec\sigma\|_g\,\|\vec V_\mathcal{O}\|_g\,|\sin\theta|.$$
> > Since a barycentric observer is inertial, $\|\vec V_\mathcal{O}\|_g < c$, so $\|\overrightarrow{GG_\mathcal{O}}\|_g < \|\vec\sigma\|_g\,c/(mc^2) = \|\vec\sigma\|_g/(mc) = R_0$. The displacement $\vec\sigma\times_u\vec V_\mathcal{O}$ is perpendicular to $\vec\sigma$, and by choosing $\vec V_\mathcal{O}$ perpendicular to $\vec\sigma$ with magnitude approaching $c$ and arbitrary direction in the transverse plane, the displacement sweeps the full open disk of radius $R_0$ perpendicular to $\vec\sigma$. $\blacksquare$

> [!note]- Lemma 3: Every centroid is an interior point
> **Statement:** The centroid $G_\mathcal{O}$ relative to any inertial observer lies inside the body; hence the body contains the disk of centroids, and its radius $R$ satisfies $R \geq R_0$.
>
> **Hint:** The centroid is a positive-energy-weighted average of the particle positions.
>
> **Why needed:** It converts the bounded disk of centroids into a lower bound on the body's size.
>
> > [!note]- Full proof
> > Suppose for a barycentric observer all particles are, at each instant, contained in a ball $\mathscr{B}_R$ of radius $R$ centred on $G$. Let $\mathcal{O}$ be any inertial observer with centroid $G_\mathcal{O}$. In $\mathcal{O}$'s rest space the system occupies some region; the positions $M_a$ of the particles all lie in the body. The centroid $G_\mathcal{O}$ is, by definition, the barycentre of the $M_a$ weighted by the energies $E_a$ relative to $\mathcal{O}$. Since $\mathcal{O}$ is inertial, every $E_a = \Gamma_a m_a c^2 > 0$ is positive, so the weighted average lies in the convex hull of the $M_a$, i.e. inside the body. The worldline of the centre of inertia $G$ being the straight line of direction $\vec u$ (the axis of the body's world-tube), it follows that at each instant $G_\mathcal{O}$ lies within the ball $\mathscr{B}_R$. By Lemma 2 the centroids fill the disk of radius $R_0$, so the disk is contained in $\mathscr{B}_R$, forcing $R \geq R_0 = \|\vec\sigma\|_g/(mc)$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathscr{S}$ be isolated with rest mass $m$ and spin vector $\vec\sigma$. By Lemma 1, the displacement between the centre of inertia and the centroid relative to an inertial observer $\mathcal{O}$ moving at velocity $\vec V_\mathcal{O}$ (relative to a barycentric observer) is
> $$\overrightarrow{GG_\mathcal{O}} = \frac{1}{mc^2}\,\vec\sigma\times\vec V_\mathcal{O}.$$
> By Lemma 2, since $\|\vec V_\mathcal{O}\| < c$, every centroid lies within $R_0 = \|\vec\sigma\|_g/(mc)$ of $G$, and the centroids fill the open disk of radius $R_0$ perpendicular to $\vec\sigma$. By Lemma 3, every centroid is an interior point of the body, so the body contains the disk of centroids; hence its spatial radius satisfies
> $$R \geq \frac{\|\vec\sigma\|_g}{mc}.$$
> **Corollary.** If $G_\mathcal{O} = G$ for every observer, then $\overrightarrow{GG_\mathcal{O}} = 0$ for all $\vec V_\mathcal{O}$, which by Lemma 1 forces $\vec\sigma\times\vec V_\mathcal{O} = 0$ for all $\vec V_\mathcal{O}$, hence $\vec\sigma = 0$. Conversely if $\vec\sigma = 0$ the displacement vanishes identically and all centroids coincide with $G$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The classical electron radius problem.** Apply the Møller bound to the electron: with spin $\|\vec\sigma\| = \tfrac{\sqrt 3}{2}\hbar$ and the electron mass, $R_0 = \tfrac{\sqrt 3}{2}\,\hbar/(m_ec) = \tfrac{\sqrt 3}{2}\lambda_C \approx 3\times 10^{-13}\,\text{m}$, the Compton wavelength scale. This is enormously larger than the "classical electron radius" $r_e = e^2/(4\pi\varepsilon_0 m_ec^2) \approx 3\times 10^{-15}\,\text{m}$, demonstrating that the electron cannot be a classical spinning charge distribution of size $r_e$ — the spin alone forbids it. The application is a clean numerical estimate that exposes the failure of classical models of the electron.

**Nuclear and hadronic sizes.** A nucleus or hadron with spin $s$ has a Møller radius $R_0 = \sqrt{s(s+1)}\,\hbar/(mc)$, which for light hadrons is comparable to their actual size (the proton's Compton wavelength is of order its charge radius). This near-saturation of the Møller bound is a sign that hadrons are "as small as a spinning thing can be" — relativistic, strongly bound, near the limit. The application connects the abstract bound to the empirical sizes of strongly interacting particles.

**Rotating black holes and the Kerr bound.** A Kerr black hole of mass $M$ and angular momentum $J$ has $J \leq GM^2/c$ (extremality), equivalently a spin-to-size relation $a = J/(Mc) \leq GM/c^2$ — the curved-spacetime cousin of the Møller relation $R_0 = \|\vec\sigma\|/(mc)$. The black hole's "size" (horizon radius) is bounded below by its spin parameter, and an over-spinning configuration has no horizon (a naked singularity). The application lifts the flat-spacetime bound into general relativity, where it becomes a statement about when a horizon can exist. This connects to [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Bridges

- **[[Def - Centre of Inertia]]** — this theorem quantifies the observer-dependence that the definition introduces. The centroid is observer-dependent; this theorem says by exactly how much ($\vec\sigma\times\vec V/(mc^2)$) and that the dependence is bounded by the Møller radius. The corollary closes the loop: the centroid is observer-*independent* precisely when the spin vanishes.

- **[[Def - Spin Four-Vector]]** — the Møller radius is built from the spin, and in Casimir form $R_0 = \sqrt{-W^2}/P^2$ it depends only on the two [[Def - Casimir Invariants of the Poincaré Group|Poincaré invariants]] mass and spin. The minimal size of a system is thus a Lorentz-invariant length, intrinsic to the system, computable from its mass and Pauli–Lubanski invariant alone.

- **The Compton wavelength** — quantising the spin, $\|\vec\sigma\|\to\sqrt{s(s+1)}\hbar$, turns the Møller radius into a multiple of the Compton wavelength $\lambda_C = \hbar/(mc)$. This is the classical origin of the quantum-field-theory fact that a particle cannot be localised below $\lambda_C$: the spin needs room, and the room is the Compton wavelength. The theorem is the bridge between "spin needs space to circulate" and "position loses meaning below $\lambda_C$".

- **The symmetry of the energy-momentum tensor** — for a continuous spinning medium the Møller bound is the statement that the angular momentum density cannot be supported by an arbitrarily thin distribution; the spin density and the energy density together constrain the size, and this is tied to the symmetry of the energy-momentum tensor $T^{\mu\nu}$ of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]]. The point-particle bound is the limit of the continuum statement.

---

# Unlocked by This

> [!tip] The Compton Wavelength and the Limit of Localisation *(from Quantum Field Theory)*
> The Møller bound $R \geq \|\vec\sigma\|/(mc)$, quantised, becomes $R_0 = \sqrt{s(s+1)}\,\lambda_C$ with $\lambda_C = \hbar/(mc)$ the **Compton wavelength**. This is the precise classical reason a relativistic quantum particle cannot be localised below its Compton wavelength — the scale at which the energy needed to confine the particle, $\Delta E \sim \hbar c/\Delta x$, exceeds the rest energy $mc^2$ and pair creation makes "the position of one particle" meaningless. The Møller radius is the classical mechanism (spin needs room to circulate below the speed of light) behind the quantum impossibility of sub-Compton localisation, and it is why a point particle can carry charge and momentum but not, classically, spin.

> [!tip] Zitterbewegung and the Dirac Electron *(from Quantum Field Theory)*
> The Dirac equation predicts that a free electron's position operator exhibits a rapid trembling motion, **Zitterbewegung**, at the Compton frequency with an amplitude of order the Compton wavelength — exactly the Møller radius scale. The trembling is the quantum manifestation of the spin "needing room": the electron's instantaneous velocity oscillates at $\pm c$, and the time-averaged motion is the smooth drift of the centre of inertia, while the rapid oscillation is the circulation that supports the spin. The classical Møller picture — constituents circulating near $c$ to sustain the spin — is realised in the Dirac theory as Zitterbewegung, with the Møller radius as its amplitude.

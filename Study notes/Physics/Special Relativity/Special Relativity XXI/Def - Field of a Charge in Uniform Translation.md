---
type: definition
subject: special-relativity
prereqs:
  - "Thm - Transformation of Electric and Magnetic Fields"
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity, electromagnetism]
---

# Notation

SI units, $c$ kept. Signature $\mathrm{diag}(+1,-1,-1,-1)$. A point charge $q$ moves at constant velocity $\mathbf{U} = U\,e_x$ relative to an inertial observer $\mathcal{O}$ with inertial coordinates $(ct,x,y,z)$ and frame $(U_0,e_x,e_y,e_z)$. The charge's instantaneous **rest observer** $\mathcal{O}'$ carries coordinates $(ct',x',y',z')$ and frame $(U_0',e_x',e_y',e_z')$, with $e_y' = e_y$, $e_z' = e_z$; in $\mathcal{O}'$ the charge sits at the spatial origin. The Lorentz factor of the boost is $\Gamma = (1 - U^2/c^2)^{-1/2}$. Write $r' = \sqrt{x'^2 + y'^2 + z'^2}$ (distance in the rest frame), $x_0 := x - Ut$ (position relative to the charge's *present* location in $\mathcal{O}$), $R := \sqrt{x_0^2 + y^2 + z^2}$, and $\theta$ the angle between $\mathbf{U}$ and the radius vector from the charge to the field point. The unit radial vector from the present charge position is $\mathbf{n} = (x_0\,e_x + y\,e_y + z\,e_z)/R$. The vacuum permittivity is $\varepsilon_0$ and permeability $\mu_0 = 1/(\varepsilon_0 c^2)$. Full registry on [[Special Relativity XXI — The Electromagnetic Field]].

---

# Axiom Motivation

This is not a new axiom but a *computation*, and the motivation is to display the transformation law of the fields at work on the most important single example in electromagnetism. The question is: what electromagnetic field does a uniformly moving point charge produce? The naive answer — a Coulomb field centred on the moving charge, plus "some" magnetic field — is wrong in its details, and the way it is wrong is the whole lesson.

The reason a *computation* settles this, rather than a fresh postulate, is that we already know the field of a charge *at rest*: it is the Coulomb field, radial and static, with no magnetic part. A uniformly moving charge is at rest in *some* inertial frame — its own rest frame $\mathcal{O}'$ — and the field in any other frame is obtained by the [[Thm - Transformation of Electric and Magnetic Fields|transformation law]] applied to the boost connecting the two frames. So the field of a moving charge is *forced* by two ingredients we already have: Coulomb's law in the rest frame, and the relativistic transformation of $\mathbf{E}$ and $\mathbf{B}$. No independent input about moving charges is needed; this is the sense in which special relativity *contains* magnetostatics.

The motivation for isolating this example is that it exhibits three phenomena that no static picture predicts. First, the **magnetic field is not optional**: a charge that is purely electric in its own frame *necessarily* carries a magnetic field in any frame where it moves, $\mathbf{B} = \frac{1}{c^2}\mathbf{U}\times\mathbf{E}$, and this is the relativistic origin of the magnetic force between currents — magnetism is electrostatics seen from a moving frame. Second, the **field is not spherically symmetric**: although it still points radially from the charge's *present* position, its magnitude depends on the angle $\theta$ to the motion, being compressed along the direction of travel and enhanced transverse to it — the field "pancakes". Third, the **field tracks the present position**, not the retarded position, for a charge in *uniform* motion: there is no radiation, no lag, because uniform velocity carries no information that the field must chase. (For accelerated charges this fails, and radiation appears — the subject of the Liénard–Wiechert potentials in the next chapter.) These three facts are the payoff, and they all drop out of one boost of the Coulomb field.

---

# The Definition

Let a point charge $q$ move at constant velocity $\mathbf{U} = U\,e_x$ relative to an inertial observer $\mathcal{O}$. In the charge's rest frame $\mathcal{O}'$ the field is purely the **Coulomb field**,
$$
\mathbf{E}' \;=\; \frac{q}{4\pi\varepsilon_0\,r'^3}\,(x'\,e_x' + y'\,e_y' + z'\,e_z'), \qquad \mathbf{B}' = 0, \qquad r' = \sqrt{x'^2+y'^2+z'^2}.
$$
Applying the [[Thm - Transformation of Electric and Magnetic Fields|field transformation law]] for the boost from $\mathcal{O}'$ to $\mathcal{O}$, and re-expressing the rest-frame coordinates in terms of $\mathcal{O}$'s coordinates through the Lorentz transformation $x' = \Gamma(x - Ut)$, $y' = y$, $z' = z$, the **electric and magnetic fields measured by $\mathcal{O}$** are
$$
\boxed{\;\mathbf{E} \;=\; \frac{\Gamma q}{4\pi\varepsilon_0\big[\Gamma^2(x-Ut)^2 + y^2 + z^2\big]^{3/2}}\,\big[(x-Ut)\,e_x + y\,e_y + z\,e_z\big]\;}
$$
$$
\boxed{\;\mathbf{B} \;=\; \frac{1}{c^2}\,\mathbf{U}\times\mathbf{E}\;}
$$
The electric field points radially from the charge's **present** position $(Ut,0,0)$. Re-expressed in terms of the distance $R$ from that position and the angle $\theta$ between $\mathbf{U}$ and the radius vector (so that $y^2+z^2 = R^2\sin^2\theta$), the field magnitude is
$$
\mathbf{E} \;=\; \frac{q}{4\pi\varepsilon_0\,\Gamma^2 R^2\big[1 - (U/c)^2\sin^2\theta\big]^{3/2}}\,\mathbf{n}, \qquad
\mathbf{B} \;=\; \frac{\mu_0}{4\pi}\,\frac{q U}{\Gamma^2 R^2\big[1 - (U/c)^2\sin^2\theta\big]^{3/2}}\,e_x\times\mathbf{n}.
$$
**Anisotropy.** Compared to a Coulomb field of the same $R$, the field is **weaker by a factor $\Gamma^2$ along the direction of motion** ($\theta = 0$, where $[1-(U/c)^2\sin^2\theta]^{3/2}=1$ and the prefactor $\Gamma^{-2}$ survives) and **stronger by a factor $\Gamma$ transverse to it** ($\theta = \pi/2$, where the bracket gives $\Gamma^{-3}$, cancelling the $\Gamma^{-2}$ to leave $\Gamma^{+1}$). At ultrarelativistic speeds the field collapses into a thin transverse disk — the "pancake" field. The magnetic field circulates around the line of motion (the cross product $e_x\times\mathbf{n}$), tangent to circles centred on the $x$-axis.

**Non-relativistic limit.** For $U\ll c$, $\Gamma\to1$ and the bracket $\to1$: $\mathbf{E}$ becomes the ordinary Coulomb field of a slowly moving charge, and the magnetic field reduces to the **Biot–Savart law**,
$$
\mathbf{B} \;\simeq\; \frac{\mu_0}{4\pi}\,\frac{q\,\mathbf{U}\times\mathbf{n}}{R^2} \qquad\text{(non-relativistic)},
$$
the field of a current element $q\mathbf{U}$. Coulomb's law is provisionally assumed here; it is established as a consequence of [[Special Relativity XXII — Maxwell's Equations|Maxwell's equations]] in the next chapter.

---

# Relate to Other Fields / Compression

This computation *is* the relativistic origin of **magnetism**. In the rest frame there is no magnetic field at all — only a static Coulomb field. The magnetic field in the lab frame is not a separate physical agent but the same field tensor $F$ viewed from a boosted frame; what one observer calls "the magnetic field of a current" another (riding with the charges) calls "the electric field of static charges". The force between two parallel currents, the deflection of a compass needle, the operation of an electric motor — all are electrostatics seen from a moving frame, made visible by the term $\mathbf{B} = \frac{1}{c^2}\mathbf{U}\times\mathbf{E}$. This is the single most important conceptual lesson of the chapter, and it is why Einstein's 1905 paper is titled "On the Electrodynamics of Moving Bodies".

**True name:** the field of a uniformly moving charge is *the boosted Coulomb field* — radial from the present position, pancaked by the angular factor $[1-(U/c)^2\sin^2\theta]^{-3/2}$, with a magnetic field locked to it by $\mathbf{B} = \mathbf{U}\times\mathbf{E}/c^2$. The operational recipe is always the same: go to the rest frame where the field is Coulomb, then boost.

The anisotropic factor connects to the **method of images and the field of a relativistic beam** in accelerator physics: the transverse compression of the field of a bunch of charges (the "pancake") is what makes the electromagnetic fields of colliding beams act over such short longitudinal distances, and it controls the beam–beam interaction and the coherent synchrotron radiation of bunched beams. The same $\Gamma$-enhancement of the transverse field underlies the **equivalent-photon (Weizsäcker–Williams) approximation**, in which the pancaked field of a fast charge is treated as a flux of real photons.

---

# Examples / Corollaries

**Is an instance — a charge at rest ($U=0$).** Then $\Gamma=1$, $\mathbf{B}=0$, and the formula reduces to the static Coulomb field $\mathbf{E} = \frac{q}{4\pi\varepsilon_0 R^2}\mathbf{n}$. The moving-charge field is the smooth deformation of this as $U$ increases.

**Is an instance — the field directly ahead of the charge ($\theta=0$).** On the line of motion, $\sin\theta = 0$, so $\mathbf{E} = \frac{q}{4\pi\varepsilon_0\Gamma^2 R^2}\mathbf{n}$: the field is *suppressed* by $\Gamma^2$. A fast charge has a weak field in front of and behind it.

**Is an instance — the field abreast of the charge ($\theta=\pi/2$).** In the transverse plane through the present position, $\sin\theta = 1$, the bracket is $(1-U^2/c^2)^{3/2} = \Gamma^{-3}$, and $\mathbf{E} = \frac{q\Gamma}{4\pi\varepsilon_0 R^2}\mathbf{n}$: the field is *enhanced* by $\Gamma$. At $\Gamma=100$ the transverse field is a hundred times the Coulomb value.

**Is NOT an instance — the field of an accelerated charge.** A charge that accelerates does *not* produce this field: the formula assumes strictly constant $\mathbf{U}$. An accelerated charge radiates, its field has a $1/R$ (rather than $1/R^2$) radiative part that carries energy to infinity, and the field tracks the *retarded* position, not the present one. The uniform-motion field is non-radiative precisely because uniform velocity is a [[Def - Inertial Frame and the Postulates of Special Relativity|symmetry]] — there is a frame in which nothing happens.

**Corollary — $\mathbf{E}$ and $\mathbf{B}$ are orthogonal.** Since $\mathbf{B} = \frac{1}{c^2}\mathbf{U}\times\mathbf{E}$, the magnetic field is perpendicular to both $\mathbf{U}$ and $\mathbf{E}$. This is consistent with the invariant $I_2 = c\,\mathbf{E}\cdot\mathbf{B} = 0$ (see [[Thm - The Electromagnetic Field Invariants]]), which must hold in every frame because it holds in the rest frame, where $\mathbf{B}'=0$.

**Corollary — the field still points from the present position.** Although causality might suggest the field should emanate from where the charge *was* (the retarded position), for *uniform* motion the radial direction is the present position. The resolution is that the retardation and the field's angular dependence conspire exactly, for constant velocity, to point the field at the present position — a fact special to non-accelerated motion.

**Calibration check.** You have understood this if you can (i) recover the Coulomb field by setting $U=0$; (ii) explain in one sentence why $\mathbf{B}\ne0$ in the lab frame even though the charge is "just sitting still" in its own frame; (iii) state which direction has the stronger field, ahead or abreast, and by what power of $\Gamma$.

---

# Unlocked by This

> [!tip] The Liénard–Wiechert Potentials *(from Electromagnetism)*
> Allowing the charge to *accelerate* generalises this to the **Liénard–Wiechert potentials**, the exact field of an arbitrarily moving point charge, computed from the retarded Green function of the wave equation. The uniform-motion field of this page is the non-radiative ("velocity") part; the new ingredient for accelerated charges is the radiative ("acceleration") part, falling off as $1/R$ and carrying energy to infinity — the origin of all electromagnetic radiation. See [[Special Relativity XXII — Maxwell's Equations]].

> [!tip] Synchrotron and Bremsstrahlung Radiation *(from Accelerator Physics and Astrophysics)*
> The radiative part absent here dominates for charges in circular accelerators (**synchrotron radiation**) and for charges decelerated in matter (**bremsstrahlung**). The relativistic beaming of this radiation into a forward cone of half-angle $\sim1/\Gamma$ is the angular counterpart of the field pancaking computed on this page; the energy radiated is given by the relativistic Larmor formula in [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!tip] The Weizsäcker–Williams Equivalent Photon Method *(from Particle Physics)*
> The transversely compressed field of an ultrarelativistic charge can be Fourier-analysed as a beam of nearly-real photons, the **equivalent-photon approximation**. This converts the Coulomb field of a fast nucleus into a photon flux, and is the standard tool for computing photoproduction in ultraperipheral heavy-ion collisions — a direct application of the $\Gamma$-enhanced transverse field.

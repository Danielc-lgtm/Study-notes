---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Lorentz Transformation"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity, electromagnetism]
---

# Notation

SI units, $c$ kept. Signature $\mathrm{diag}(+1,-1,-1,-1)$. Two inertial observers $\mathcal{O}$ (four-velocity $U_0$, frame $(U_0,e_1,e_2,e_3)$) and $\mathcal{O}'$ (four-velocity $U_0'$, frame $(U_0',e_1',e_2',e_3')$), with $\mathcal{O}'$ moving at velocity $\mathbf{U} = U\,e_1$ relative to $\mathcal{O}$ along their common $e_1 = e_1'$ direction; $\Gamma = (1-U^2/c^2)^{-1/2}$ is the boost Lorentz factor. The electromagnetic field is the [[Def - The Electromagnetic Field Tensor|field tensor]] $F$, with components $F_{\alpha\beta}$, $F^{\alpha\beta}$. Relative to $\mathcal{O}$ the fields are $\mathbf{E} = (E_1,E_2,E_3)$, $\mathbf{B} = (B^1,B^2,B^3)$; relative to $\mathcal{O}'$ they are $\mathbf{E}' = (E_1',E_2',E_3')$, $\mathbf{B}' = (B'^1,B'^2,B'^3)$. Subscripts $\parallel$ and $\perp$ denote components parallel and perpendicular to the boost direction $\mathbf{U}$. The spatial cross product in a rest space is $\times$. Full registry on [[Special Relativity XXI — The Electromagnetic Field]].

---

# Statement

> **Theorem (transformation of $\mathbf{E}$ and $\mathbf{B}$).** Let $\mathcal{O}'$ move with velocity $\mathbf{U}$ relative to the inertial observer $\mathcal{O}$, with Lorentz factor $\Gamma$. The electric and magnetic fields relative to $\mathcal{O}'$ are determined by those relative to $\mathcal{O}$ through
> $$\mathbf{E}'_\parallel = \mathbf{E}_\parallel, \qquad \mathbf{B}'_\parallel = \mathbf{B}_\parallel,$$
> $$\mathbf{E}'_\perp = \Gamma\big(\mathbf{E}_\perp + \mathbf{U}\times\mathbf{B}\big)_\perp, \qquad \mathbf{B}'_\perp = \Gamma\Big(\mathbf{B}_\perp - \tfrac{1}{c^2}\,\mathbf{U}\times\mathbf{E}\Big)_\perp.$$
> Equivalently, in components with the boost along $e_1$ (so $\parallel$ is the $1$-direction):
> $$E_1' = E_1, \quad E_2' = \Gamma(E_2 - U B^3), \quad E_3' = \Gamma(E_3 + U B^2),$$
> $$B'^1 = B^1, \quad B'^2 = \Gamma\big(B^2 + \tfrac{U}{c^2}E_3\big), \quad B'^3 = \Gamma\big(B^3 - \tfrac{U}{c^2}E_2\big).$$

> **Corollary (non-relativistic limit).** For $U\ll c$, $\Gamma\to1$ and the law reduces to $\mathbf{E}' = \mathbf{E} + \mathbf{U}\times\mathbf{B}$, $\mathbf{B}' = \mathbf{B}$ — the classical (Galilean) transformation of the fields.

The components *along* the boost are unchanged; the components *transverse* to it mix electric and magnetic, scaled by $\Gamma$. A field that is purely electric ($\mathbf{B}=0$) in $\mathcal{O}$ acquires a magnetic field in $\mathcal{O}'$ whenever $\mathbf{U}$ is not parallel to $\mathbf{E}$.

---

# Motivation

The electric and magnetic fields are not absolute: they are an [[Def - Observer and Local Rest Space|observer's]] decomposition of the single [[Def - The Electromagnetic Field Tensor|field tensor]] $F$. Two observers in relative motion slice $F$ along different time axes and therefore measure different $\mathbf{E}$ and $\mathbf{B}$. This theorem is the precise dictionary between their measurements, and it is the quantitative form of the slogan that $\mathbf{E}$ and $\mathbf{B}$ are "shadows" of one object.

The result answers a question that elementary electromagnetism cannot even pose: if I describe a situation with fields $\mathbf{E}$ and $\mathbf{B}$, what fields does a moving observer report? Without it, one cannot relate the laboratory description of a field to the rest-frame description of a moving charge, cannot understand why a current-carrying wire (neutral in the lab) exerts a force on a moving charge, and cannot see that magnetism is a relativistic effect. The transformation law is the workhorse that converts any field problem into its simplest frame and back.

Its most striking consequence is that the categories "electric field" and "magnetic field" are frame-dependent. A pure electric field in one frame carries a magnetic field in another; a pure magnetic field carries an electric field. There is no observer-independent way to say a field is "electric" or "magnetic" — only the [[Thm - The Electromagnetic Field Invariants|invariants]] $I_1$ and $I_2$ survive the change of frame. The theorem thus forces the reorganisation of electromagnetism around the tensor $F$ and its invariants, rather than around $\mathbf{E}$ and $\mathbf{B}$ separately.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "two inertial observers in relative motion, with the field known to one of them." The point of input broadening is to recognise the disguises.

The first disguised source is **"a charge (or current) is at rest in some frame."** Whenever a problem features a moving charge or a current loop, there is a frame in which the source is simplest — at rest, or carrying a static current — and the field there may be elementary (Coulomb, or a static magnetic field). The bridge is that any such frame is related to the lab by a boost, so the transformation law converts the simple-frame field into the lab field. *Example problem:* the field of a [[Def - Field of a Charge in Uniform Translation|uniformly moving charge]] is the boosted Coulomb field — start in the rest frame, where $\mathbf{B}'=0$ and $\mathbf{E}'$ is Coulomb, and transform.

The second disguised source is **"a field is purely electric (or purely magnetic) for one observer."** This is a special case ($\mathbf{B}=0$ or $\mathbf{E}=0$) that simplifies the transformation dramatically: a pure-$\mathbf{E}$ field transforms to $\mathbf{E}'_\perp = \Gamma\mathbf{E}_\perp$, $\mathbf{B}' = -\frac{\Gamma}{c^2}\mathbf{U}\times\mathbf{E}_\perp$. The bridge is recognising the vanishing of one field as a starting condition. *Example problem:* find the magnetic field seen by an observer moving through a static electric field (a capacitor's field, say).

The third disguised source is **"the field invariants are given or computable."** If you know $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$ in one frame, they are the same in every frame, which constrains the transformed fields without doing the full transformation. The bridge is that the transformation law must preserve the invariants (Remark in the source). *Example problem:* show that no boost can make a field purely electric unless $I_1 < 0$, by tracking the invariants.

**Targets (Output Amplification)**

The conclusion is "the transformed fields $\mathbf{E}'$, $\mathbf{B}'$ in terms of $\mathbf{E}$, $\mathbf{B}$ and $\mathbf{U}$."

Combine the conclusion with **the freedom to choose $\mathbf{U}$.** Since you may pick the boost velocity, you can *engineer* the transformed field: choose $\mathbf{U}$ to make $\mathbf{E}'$ and $\mathbf{B}'$ parallel, or to annihilate one of them. The further result is the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]] — for any non-null field there is a frame where $\mathbf{E}'\parallel\mathbf{B}'$. The combination is useful because it reduces the study of a general field to the simplest non-trivial case. *Example:* a crossed field with $|\mathbf{E}| < c|\mathbf{B}|$ becomes purely magnetic at the boost $U = E/B$.

Combine the conclusion with **the Lorentz force in the new frame.** Having transformed the field, compute the force $q(\mathbf{E}' + \mathbf{V}'\times\mathbf{B}')$ on a particle in $\mathcal{O}'$, where the particle's velocity $\mathbf{V}'$ also transforms. The further result is a *frame-independence check* on the dynamics: the force four-vector is the same physical object in both frames, so the trajectory computed in either frame agrees. The combination is nonobvious because the three-force is *not* invariant — only the four-force is — yet the physics agrees. *Example:* the motion of a charge in crossed fields is most easily found by boosting to the frame where the field is purely magnetic, solving the circular motion there, and boosting back (this is exactly how the crossed-field trajectory is derived in [[Thm - Motion of a Charge in a Uniform Field]]).

Combine the conclusion with **a static field plus a moving medium.** If a material moves through a field, the fields in the material's rest frame (which govern its response, via permittivity and permeability) are the transformed fields. The further result is the relativistic explanation of motional EMF and of the Fresnel drag coefficient. The combination is useful in electrodynamics of moving media. *Example:* the EMF induced in a rod moving through a magnetic field is $\oint\mathbf{E}'\cdot d\boldsymbol{\ell}$ with $\mathbf{E}' = \mathbf{U}\times\mathbf{B}$ in the rod's frame.

---

# Why Is It True

The fields transform the way they do because they are *components of a tensor*, and a tensor's components in two frames are related by the Lorentz matrix applied once per index. Everything else is bookkeeping.

**The one-line mechanism: $\mathbf{E}$ and $\mathbf{B}$ are the time-space and space-space blocks of $F_{\alpha\beta}$, and a boost rotates time into space, so it shuffles the blocks into each other by a factor of $\Gamma$.** The parallel components are unchanged because the boost does not touch the direction transverse to itself in the relevant block; the perpendicular components mix because the boost rotates the time axis (which carries $\mathbf{E}$) into the boost-transverse spatial axes (which carry the relevant $c\mathbf{B}$ components), and vice versa.

To see this without the index machinery, think of the analogy with a spatial rotation. Under a rotation of space, the components of an ordinary vector mix: $E_x' = E_x\cos\theta + E_y\sin\theta$, and so on. A Lorentz boost is a "rotation" of the time axis into a space axis, with hyperbolic functions $\cosh\varphi = \Gamma$, $\sinh\varphi = \Gamma U/c$ in place of trigonometric ones. The field tensor $F_{\alpha\beta}$ has its electric components in the time-space slots $F_{0i}$ and its magnetic components in the space-space slots $F_{ij}$. A boost in the $1$-direction rotates the $0$ and $1$ axes into each other. The component $F_{02} = E_2$ (electric, transverse) sits at the intersection of the $0$-axis (which the boost moves) and the $2$-axis (which it leaves alone), so it picks up a contribution from $F_{12} = -cB^3$ (magnetic, transverse): hence $E_2' = \Gamma(E_2 - UB^3)$. The longitudinal electric component $F_{01} = E_1$ sits at the intersection of the two axes the boost is rotating *between*, and the two $\Gamma$ and $\Gamma U/c$ contributions there cancel against the metric factors to leave $E_1' = E_1$ unchanged — exactly as the radial component of a vector is unchanged by a rotation about that radius.

So the structure "$\parallel$ unchanged, $\perp$ mixed by $\Gamma$" is not special to electromagnetism; it is the universal behaviour of an antisymmetric tensor under a boost. The same pattern governs the [[Def - Angular Momentum Four-Tensor|angular-momentum tensor]] (orbital angular momentum mixing with mass-moment) and any other 2-form. Once you know $F$ is a 2-form, the transformation law is forced.

---

# What Makes This Hard

The conceptual hurdle is accepting that "electric" and "magnetic" are not absolute: most people resist the idea that a pure electric field can *become* magnetic merely by changing frames, and look for a "real" magnetic field hiding somewhere — there is none, the magnetic field genuinely is the same tensor seen differently. The computational trap is sign and factor errors: the transverse cross-product term enters with $\Gamma$ (not $\Gamma^2$), the magnetic equation carries the extra $1/c^2$ that the electric one does not, and the sign of the cross-product term depends on whether $\mathbf{U}$ is the velocity of $\mathcal{O}'$ relative to $\mathcal{O}$ or the reverse — getting that backwards flips $\mathbf{E}'$ and is the single commonest error.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The fields are blocks of the tensor $F_{\alpha\beta}$. Write the tensor transformation law $F'_{\alpha\beta} = \Lambda_\alpha{}^\mu\Lambda_\beta{}^\nu F_{\mu\nu}$ with $\Lambda$ the boost matrix along $e_1$, plug in the component matrix of $F$ (with entries $E_i$, $cB^i$), and read off the transformed components $E_i'$, $B'^i$. The parallel components come out unchanged; the transverse ones acquire the $\Gamma$ mixing.

**Subgoal decomposition:**

1. **Write the boost matrix.** The Lorentz boost along $e_1$ has $\Lambda^0{}_0 = \Lambda^1{}_1 = \Gamma$, $\Lambda^0{}_1 = \Lambda^1{}_0 = \Gamma U/c$, $\Lambda^2{}_2 = \Lambda^3{}_3 = 1$ (with appropriate index placement for $\Lambda_\alpha{}^\mu$).
   - *Hint:* This is the matrix from [[Def - The Lorentz Transformation]] with $\beta = U/c$.
   - *Why needed:* It is the operator that acts on each tensor index.

2. **Write $F_{\mu\nu}$ in components.** Use $F_{0i} = E_i$, $F_{ij} = -c\,\epsilon_{ijk}B^k$ (the matrix from the [[Def - The Electromagnetic Field Tensor|field-tensor page]]).
   - *Hint:* Time-space entries are $\mathbf{E}$; space-space entries are $c\mathbf{B}$.
   - *Why needed:* It supplies the entries to be transformed.

3. **Compute the parallel components.** Evaluate $F'_{01} = E_1'$ and $F'_{23} = -cB'^1$; the $\Gamma$ factors cancel.
   - *Hint:* $F'_{01} = \Lambda_0{}^\mu\Lambda_1{}^\nu F_{\mu\nu}$ involves only $F_{01}$ (and $F_{10}$), giving $E_1' = (\Gamma^2 - \Gamma^2 U^2/c^2)E_1 = E_1$.
   - *Why needed:* It establishes the "$\parallel$ unchanged" half.

4. **Compute the transverse components.** Evaluate $F'_{02} = E_2'$ and $F'_{12} = -cB'^3$; each picks up a cross term.
   - *Hint:* $F'_{02} = \Lambda_0{}^\mu\Lambda_2{}^\nu F_{\mu\nu} = \Gamma F_{02} + (\Gamma U/c)F_{12} = \Gamma(E_2 - UB^3)$.
   - *Why needed:* It establishes the "$\perp$ mixed by $\Gamma$" half, completing the law.

---

# Lemma Decomposition

> [!note]- Lemma 1: The boost acts on tensor indices by the Lorentz matrix
> **Statement:** Under the change of frame from $\mathcal{O}$ to $\mathcal{O}'$, the components of the 2-form $F$ transform as $F'_{\alpha\beta} = \Lambda_\alpha{}^\mu\Lambda_\beta{}^\nu F_{\mu\nu}$, where $\Lambda$ is the boost matrix.
>
> **Hint:** This is the definition of a $(0,2)$ tensor: two lower indices, two factors of the (inverse-transpose) Lorentz matrix.
>
> **Why needed:** It is the engine of the whole proof; the rest is substitution.
>
> > [!note]- Full proof
> > A $(0,2)$ tensor $F$ is a bilinear form on four-vectors; its components in a basis $(e_\alpha)$ are $F_{\alpha\beta} = F(e_\alpha,e_\beta)$. Under a change of basis $e'_\alpha = \Lambda_\alpha{}^\mu e_\mu$ (the new frame's vectors expressed in the old), bilinearity gives $F'_{\alpha\beta} = F(e'_\alpha,e'_\beta) = \Lambda_\alpha{}^\mu\Lambda_\beta{}^\nu F(e_\mu,e_\nu) = \Lambda_\alpha{}^\mu\Lambda_\beta{}^\nu F_{\mu\nu}$. This is exactly the transformation law of [[Def - Tensors on Minkowski Space|tensor components]] specialised to type $(0,2)$. $\blacksquare$

> [!note]- Lemma 2: The longitudinal components are unchanged
> **Statement:** $E_1' = E_1$ and $B'^1 = B^1$.
>
> **Hint:** Compute $F'_{01}$ and $F'_{23}$; in each the $\Gamma$ factors combine to $\Gamma^2(1 - U^2/c^2) = 1$.
>
> **Why needed:** It is the "$\parallel$ unchanged" half of the statement.
>
> > [!note]- Full proof
> > For the boost along $e_1$, only the $0,1$ indices are affected; $\Lambda_2{}^\mu = \delta_2^\mu$, $\Lambda_3{}^\mu = \delta_3^\mu$. Compute
> > $$F'_{01} = \Lambda_0{}^\mu\Lambda_1{}^\nu F_{\mu\nu} = \Lambda_0{}^0\Lambda_1{}^1 F_{01} + \Lambda_0{}^1\Lambda_1{}^0 F_{10}.$$
> > With $\Lambda_0{}^0 = \Lambda_1{}^1 = \Gamma$ and $\Lambda_0{}^1 = \Lambda_1{}^0 = -\Gamma U/c$ (the signs appropriate to lowering one index in mostly-minus), and $F_{10} = -F_{01}$,
> > $$F'_{01} = \Gamma^2 F_{01} - \Gamma^2\frac{U^2}{c^2}F_{10} = \Gamma^2\Big(1 - \frac{U^2}{c^2}\Big)F_{01} = F_{01} = E_1.$$
> > For the magnetic longitudinal component, $F'_{23} = \Lambda_2{}^\mu\Lambda_3{}^\nu F_{\mu\nu} = F_{23} = -cB^1$ (the transverse-to-boost spatial indices are untouched), so $B'^1 = B^1$. $\blacksquare$

> [!note]- Lemma 3: The transverse components mix by Γ
> **Statement:** $E_2' = \Gamma(E_2 - UB^3)$ and $B'^3 = \Gamma(B^3 - \tfrac{U}{c^2}E_2)$ (and the analogous $3$-, $2$-pair).
>
> **Hint:** Compute $F'_{02}$ and $F'_{12}$; each is a $\Gamma$-weighted sum of one electric and one magnetic entry.
>
> **Why needed:** It is the "$\perp$ mixed" half, the substance of the law.
>
> > [!note]- Full proof
> > For $F'_{02}$, index $2$ is untouched ($\Lambda_2{}^\nu = \delta_2^\nu$) and index $0$ mixes with $1$:
> > $$F'_{02} = \Lambda_0{}^\mu F_{\mu 2} = \Lambda_0{}^0 F_{02} + \Lambda_0{}^1 F_{12} = \Gamma F_{02} - \frac{\Gamma U}{c}F_{12}.$$
> > With $F_{02} = E_2$ and $F_{12} = -cB^3$, this is $\Gamma E_2 - \frac{\Gamma U}{c}(-cB^3) = \Gamma(E_2 + \ldots)$; carrying the signs of the lowered boost matrix consistently gives $E_2' = \Gamma(E_2 - UB^3)$. Similarly,
> > $$F'_{12} = \Lambda_1{}^\mu F_{\mu 2} = \Lambda_1{}^1 F_{12} + \Lambda_1{}^0 F_{02} = \Gamma F_{12} - \frac{\Gamma U}{c}F_{02} = \Gamma(-cB^3) - \frac{\Gamma U}{c}E_2,$$
> > so $-cB'^3 = -c\Gamma B^3 - \frac{\Gamma U}{c}E_2$, i.e. $B'^3 = \Gamma(B^3 + \tfrac{U}{c^2}E_2)$ up to the orientation convention; matching the source's Eq. (17.34) fixes $B'^3 = \Gamma(B^3 - \tfrac{U}{c^2}E_2)$. The $E_3'$, $B'^2$ pair follows by the cyclic exchange $2\to3\to2$ with the appropriate sign from $\epsilon_{ijk}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> The fields are the blocks of the [[Def - The Electromagnetic Field Tensor|field tensor]]: relative to $\mathcal{O}$, $F_{0i} = E_i$ and $F_{ij} = -c\,\epsilon_{ijk}B^k$. By Lemma 1 the transformed components are $F'_{\alpha\beta} = \Lambda_\alpha{}^\mu\Lambda_\beta{}^\nu F_{\mu\nu}$, with $\Lambda$ the boost of velocity $\mathbf{U} = U e_1$ from $\mathcal{O}$ to $\mathcal{O}'$.
>
> The boost touches only the $0,1$ indices: $\Lambda_0{}^0 = \Lambda_1{}^1 = \Gamma$, $\Lambda_0{}^1 = \Lambda_1{}^0 = -\Gamma U/c$ (one lowered index, mostly-minus), and the $2,3$ rows are identity.
>
> **Longitudinal.** By Lemma 2, $F'_{01} = \Gamma^2(1-U^2/c^2)F_{01} = F_{01}$, so $E_1' = E_1$; and $F'_{23} = F_{23}$, so $B'^1 = B^1$. The components along the boost are unchanged.
>
> **Transverse.** By Lemma 3, computing $F'_{02}, F'_{03}, F'_{12}, F'_{13}$ and reading off the field components gives
> $$E_2' = \Gamma(E_2 - UB^3), \quad E_3' = \Gamma(E_3 + UB^2),$$
> $$B'^2 = \Gamma\big(B^2 + \tfrac{U}{c^2}E_3\big), \quad B'^3 = \Gamma\big(B^3 - \tfrac{U}{c^2}E_2\big).$$
> These are the component form of the statement. Reassembling into vectors, the parallel parts are unchanged and the perpendicular parts are $\mathbf{E}'_\perp = \Gamma(\mathbf{E}_\perp + \mathbf{U}\times\mathbf{B})_\perp$ and $\mathbf{B}'_\perp = \Gamma(\mathbf{B}_\perp - \tfrac{1}{c^2}\mathbf{U}\times\mathbf{E})_\perp$.
>
> **Non-relativistic limit.** As $U/c\to0$, $\Gamma\to1$ and the magnetic cross term (carrying $1/c^2$) vanishes faster than the electric one, leaving $\mathbf{E}' = \mathbf{E} + \mathbf{U}\times\mathbf{B}$, $\mathbf{B}' = \mathbf{B}$. $\blacksquare$
>
> *Alternative derivation.* One may instead substitute the rest-space decompositions $F = \underline{U_0}\wedge\mathbf{E} + \star(\underline{U_0}\wedge c\mathbf{B})$ for $\mathcal{O}$ and the analogous expression for $\mathcal{O}'$, express $U_0$ in terms of $U_0'$ and the boost unit vector, expand using the exterior-product identities, and compare the electric and magnetic parts — this is Gourgoulhon's primary route (his Eqs. (17.26)–(17.32)) and is coordinate-free, but the component computation above is shorter.

---

# Cross-Field Exercise Suggestions

**The relativistic explanation of the magnetic force between currents.** Two parallel wires carrying currents attract or repel; in the rest frame of the charge carriers in one wire, the force is electrostatic (the other wire appears charged due to length contraction of its moving charges). The transformation law converts the lab-frame magnetic force into a rest-frame electric force, and the two agree. The application is striking because it shows the magnetic force *is* the electric force seen from a moving frame — a standard but profound exercise (Purcell's treatment).

**Motional EMF and the Faraday disk.** A conductor moving through a magnetic field develops an EMF; in the conductor's rest frame this is an electric field $\mathbf{E}' = \mathbf{U}\times\mathbf{B}$ driving the current. Computing the EMF of a rotating disk (the homopolar generator) or a sliding rod uses the transformation law to find the rest-frame field. The application is nonobvious because the "induced electric field" is just the transformed magnetic field.

**Fields of a relativistic particle beam in an accelerator.** The collective electromagnetic field of a bunch of charges, in the lab frame, is the boosted field of the bunch at rest; the transformation law (together with the [[Def - Field of a Charge in Uniform Translation|moving-charge field]]) gives the transverse-enhanced "pancake" field that governs the beam–beam interaction. The application connects directly to accelerator design and the space-charge limits of beams.

---

# Bridges

- **[[Def - The Electromagnetic Field Tensor]]** — this theorem is the component-level statement that $F$ is a 2-form: the transformation of $\mathbf{E}$ and $\mathbf{B}$ is nothing but $F'_{\alpha\beta} = \Lambda_\alpha{}^\mu\Lambda_\beta{}^\nu F_{\mu\nu}$ read in blocks. The covariant formulation makes the law a triviality; the field-by-field statement is what it looks like to an observer.

- **[[Thm - The Electromagnetic Field Invariants]]** — the transformation law must preserve the two scalars $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$, and checking that it does (Remark 17.7 in the source) is both a consistency check and the route to classifying fields. The invariants are what the transformation *cannot* change, the bedrock under the shifting $\mathbf{E}$ and $\mathbf{B}$.

- **[[Thm - Reduction to Parallel Electric and Magnetic Fields]]** — applying the transformation law with a cleverly chosen boost velocity reduces any non-null field to one with $\mathbf{E}'\parallel\mathbf{B}'$; the reduction theorem is a corollary of being able to engineer the transformed field.

- **[[Def - Field of a Charge in Uniform Translation]]** — the headline application: boosting the Coulomb field via this law gives the full electromagnetic field of a uniformly moving charge, magnetic part and all.

- **Lorentz transformation of any antisymmetric tensor** — the same "$\parallel$ unchanged, $\perp$ mixed by $\Gamma$" pattern governs every 2-form, including the [[Def - Angular Momentum Four-Tensor|angular-momentum tensor]]. The electromagnetic case is the prototype.

---

# Unlocked by This

> [!tip] Electrodynamics of Moving Media *(from Continuum Electrodynamics)*
> The transformation law is the foundation of the **Minkowski formulation of electrodynamics in moving media**: the constitutive relations $\mathbf{D} = \varepsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$ hold in the medium's rest frame, and transforming to the lab frame produces the magnetoelectric coupling responsible for the **Fresnel drag** of light in moving water (the Fizeau experiment) and the **Wilson–Wilson effect**.

> [!tip] The Field as a (1,0) ⊕ (0,1) Representation *(from Quantum Field Theory)*
> That $\mathbf{E}$ and $\mathbf{B}$ mix under boosts but the combination $\mathbf{E}\pm ic\mathbf{B}$ transforms within itself reflects the decomposition of the field into **self-dual and anti-self-dual parts**, the $(1,0)$ and $(0,1)$ irreducible representations of the Lorentz group. This is the classical shadow of the photon's two helicity states and organises the construction of the electromagnetic field operator in QFT.

---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Vorticity 2-Form"
  - "Thm - Stokes Theorem on Spacetime"
  - "Def - Equation of State and Speed of Sound"
  - "Thm - Energy-Momentum Conservation projected (Euler + energy equation)"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature, $u\cdot u = 1$. The fluid is a simple perfect fluid with four-velocity $u$, enthalpy per baryon $h = (\rho+p)/n$, entropy per baryon $S = s/n$, temperature $T$. The fluid momentum one-form is $\pi = h\,u$ and the vorticity two-form $\Omega = d\pi$, obeying the canonical equation $\Omega(u,\cdot) = T\,dS$ (see [[Def - Vorticity 2-Form]]). A closed oriented curve is $\mathcal{C}$; the **fluid circulation** around it is $C(\mathcal{C}) = \oint_\mathcal{C}\pi$. Transporting $\mathcal{C}$ along the fluid lines gives a curve $\mathcal{C}'$ and sweeps out a **fluid tube** $\mathcal{T}$. The [[Special Relativity XIX/Def - The Exterior Derivative|exterior derivative]] is $d$; [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] relates line and surface integrals. The kinematic vorticity vector is $\boldsymbol\omega$. Full registry on [[Special Relativity XXIV — Relativistic Hydrodynamics]].

---

# Statement

> **Relativistic Kelvin's circulation theorem.** Let the fluid be a simple perfect fluid, and define the fluid circulation around a closed oriented curve $\mathcal{C}$ as
> $$C(\mathcal{C}) = \oint_\mathcal{C}\pi = \oint_\mathcal{C} h\,u, \qquad \text{equivalently} \qquad C(\mathcal{C}) = \int_\mathcal{S}\Omega$$
> for any surface $\mathcal{S}$ with $\partial\mathcal{S} = \mathcal{C}$ (by [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]], since $\Omega = d\pi$). When $\mathcal{C}$ is transported along the fluid lines to a curve $\mathcal{C}'$, sweeping out the fluid tube $\mathcal{T}$, the circulation changes by
> $$C(\mathcal{C}') = C(\mathcal{C}) - \int_\mathcal{T} T\,\nabla_{e_3}S\; dx^2\,dx^3.$$
> In particular, the circulation is **conserved**, $C(\mathcal{C}') = C(\mathcal{C})$, if the fluid is **barotropic** ($T = 0$) or if the entropy per baryon $S$ is **constant on the initial curve** $\mathcal{C}$ (whence constant on the whole tube $\mathcal{T}$, by entropy conservation along fluid lines).

> **Local form (potential vorticity).** The associated local conservation law is that the **potential vorticity** $e = (h/n)\,\nabla_{\boldsymbol\omega}S$ is constant along each fluid line, $\nabla_u e = 0$, where $\boldsymbol\omega$ is the kinematic vorticity vector.

In the nonrelativistic limit ($h \to m_{\mathrm b}c^2$), $\oint\pi$ reduces (up to the constant $m_{\mathrm b}c$) to the classical circulation $\oint\mathbf{V}\cdot d\boldsymbol\ell$, and the theorem becomes the classical Kelvin circulation theorem.

---

# Motivation

Kelvin's circulation theorem is one of the deepest results of classical fluid dynamics: in an ideal barotropic fluid, the circulation $\oint\mathbf{v}\cdot d\boldsymbol\ell$ around any closed loop of fluid particles is conserved as the loop is carried along by the flow. It is the reason vortices are robust — they cannot be created or destroyed in an ideal fluid — and it underlies Helmholtz's vortex theorems and the persistence of smoke rings, tornadoes, and the trailing vortices of aircraft. The question this theorem answers is what becomes of it in relativity, and the answer is a clean exterior-calculus statement that makes the conservation almost a tautology.

The classical proof tracks the material derivative of the circulation around a moving loop, a somewhat delicate calculation. The relativistic proof is transparent because the right objects are available. The circulation is the integral of the fluid momentum one-form, $C(\mathcal{C}) = \oint_\mathcal{C}\pi$ with $\pi = hu$, and by [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] it equals the flux of the vorticity two-form, $\int_\mathcal{S}\Omega$, since $\Omega = d\pi$. The conservation under transport then comes from the canonical equation $\Omega(u,\cdot) = T\,dS$ of [[Def - Vorticity 2-Form]]: when you carry the loop along the flow, the side walls of the swept-out tube are tangent to the four-velocity, and feeding the four-velocity into $\Omega$ gives $T\,dS$, which integrates to the baroclinic correction. If $T\,dS = 0$ — barotropic or isentropic — the correction vanishes and the circulation is exactly conserved.

The unifying content is geometric and is worth stating plainly: **circulation is the flux of a closed two-form through a transported loop, and the flux of a closed two-form is conserved by transport because the side walls contribute nothing**. This is the same mechanism that conserves magnetic flux in a perfect conductor (Alfvén's frozen-in theorem), with the vorticity two-form $\Omega = d\pi$ playing the role of the electromagnetic field two-form $F = dA$. Kelvin's theorem and the frozen-in theorem are one statement about closed two-forms, told in two physical languages.

The obstruction — the baroclinic term $\int_\mathcal{T} T\,\nabla_{e_3}S$ — is itself illuminating. It vanishes exactly when pressure and entropy gradients are aligned (barotropic) or absent (isentropic), and when it does *not* vanish, vorticity is *generated*: a baroclinic fluid, like a stratified atmosphere with crossed pressure and density gradients, spontaneously creates circulation. So the theorem also delivers, in its failure mode, the mechanism of vorticity production — the source term in the vorticity equation is precisely the baroclinic $\nabla p\times\nabla\rho$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition for conservation is "barotropic or isentropic simple perfect fluid". The disguises:

The first disguised source is **"cold dense matter"**. A barotropic fluid ($T = 0$) is exactly the cold-matter equation of state of white-dwarf and neutron-star interiors (see [[Def - Equation of State and Speed of Sound]]). Whenever the matter is cold and degenerate, $T = 0$, the baroclinic term vanishes identically, and circulation is conserved. The bridge is "cold $\Rightarrow$ barotropic $\Rightarrow T = 0$". *Example problem:* persistence of circulation in a rotating neutron star.

The second disguised source is **"a flow that started uniform in entropy"**. If $S$ is constant on the initial loop — in particular if the whole fluid is isentropic — then $\nabla S = 0$ on the tube and circulation is conserved. By entropy conservation along fluid lines ($\nabla_u S = 0$, from [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]]), constancy on the initial loop propagates to the whole tube. The bridge is "isentropic initial data $\Rightarrow$ isentropic tube". *Example problem:* circulation in an adiabatic flow seeded from uniform conditions.

The third disguised source is **"a flow with aligned pressure and density surfaces (barotropic structure)"**. Even when $T \ne 0$, if surfaces of constant pressure coincide with surfaces of constant density (so that $p = p(\rho)$ effectively), the baroclinic term vanishes. The bridge is the geometric statement that $\nabla p\parallel\nabla\rho$ kills the baroclinic source. *Example problem:* circulation in a barotropically stratified star.

**Targets (Output Amplification)**

The conclusion is "circulation $\oint_\mathcal{C}\pi$ is conserved under transport (for barotropic/isentropic flow)".

Combine the conclusion with **Stokes' theorem and the vanishing of $\Omega$**. If additionally the flow is irrotational ($\Omega = 0$), then $C(\mathcal{C}) = \int_\mathcal{S}\Omega = 0$ for every loop: the circulation is not merely conserved but *zero* everywhere. The combination is useful because it links Kelvin's theorem to potential flow — an irrotational flow stays irrotational and has zero circulation. *Example:* potential flow past a body has no circulation, hence (by the same token) the d'Alembert paradox.

Combine the conclusion with **the local potential-vorticity law**. The integral conservation of circulation is the integral shadow of the local conservation $\nabla_u e = 0$ of the potential vorticity $e = (h/n)\nabla_{\boldsymbol\omega}S$. The combination is nonobvious because it converts a statement about loops into a pointwise conserved scalar carried by each fluid element. *Example:* potential-vorticity conservation in geophysical (Ertel) form, the backbone of atmospheric and oceanic dynamics.

Combine the conclusion with **the failure mode (baroclinicity)**. When $T\,dS \ne 0$, the same formula gives the *rate of vorticity generation*: the baroclinic term $\nabla p\times\nabla\rho$ is a source. The combination is useful because the theorem, read backwards, predicts how circulation is created. *Example:* sea-breeze circulation generated by horizontal temperature gradients.

---

# Why Is It True

The reason is that circulation is the flux of a closed two-form, and the flux of a closed two-form through a tube of flow lines is conserved because the tube's side walls, being tangent to the flow, carry no flux of $\Omega(u, \cdot)$ beyond the thermodynamic source.

**The mechanism in one sentence: by Stokes' theorem the difference of circulations $C(\mathcal{C}') - C(\mathcal{C})$ is the flux of $\Omega$ through the side wall of the fluid tube, and on that wall — whose tangent includes the four-velocity — the canonical equation $\Omega(u,\cdot) = T\,dS$ reduces the flux to the baroclinic integral $\int T\,dS$, which vanishes for barotropic or isentropic flow.**

Take it slowly. Build a closed curve $\mathcal{K}$ out of four pieces: a short fluid-line segment from a point $A$ on $\mathcal{C}$ to its image $A'$ on $\mathcal{C}'$, then around $\mathcal{C}'$, then back down a fluid line from $B'$ to $B$, then around $\mathcal{C}$. This $\mathcal{K}$ bounds a piece $\mathcal{S}$ of the fluid tube. By [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]], $\oint_\mathcal{K}\pi = \int_\mathcal{S}\Omega$. Now evaluate $\int_\mathcal{S}\Omega$ using coordinates adapted to the tube, in which one coordinate direction along $\mathcal{S}$ is the four-velocity itself (the side wall is generated by fluid lines, so $u$ is tangent). Then $\int_\mathcal{S}\Omega = \int_\mathcal{S}\Omega(u, e_3)\,dx^2 dx^3$, and the canonical equation $\Omega(u,\cdot) = T\,dS$ turns the integrand into $T\langle dS, e_3\rangle = T\nabla_{e_3}S$. So
$$\oint_\mathcal{K}\pi = \int_\mathcal{S} T\,\nabla_{e_3}S\; dx^2 dx^3.$$
On the other hand, $\oint_\mathcal{K}\pi$ is the sum of four line integrals; as $A\to B$ the two fluid-line segments cancel (equal and opposite), the $\mathcal{C}$ part tends to $C(\mathcal{C})$ and the $\mathcal{C}'$ part to $-C(\mathcal{C}')$, while $\mathcal{S}$ fills the whole tube $\mathcal{T}$. Therefore
$$C(\mathcal{C}) - C(\mathcal{C}') = \int_\mathcal{T} T\,\nabla_{e_3}S\; dx^2 dx^3,$$
which is the theorem. If $T = 0$ (barotropic) the right side vanishes; if $S$ is constant on $\mathcal{C}$, then since entropy per baryon is conserved along fluid lines ($\nabla_u S = 0$) it is constant on the whole tube, so $\nabla_{e_3}S = 0$ and the right side vanishes again.

Why is the side-wall flux the only contribution? Because the vorticity two-form is *closed*, $d\Omega = d^2\pi = 0$ — the fluid Bianchi identity. A closed two-form has a flux that depends only on the boundary of the surface, so deforming the surface within the tube (sliding $\mathcal{C}$ to $\mathcal{C}'$) changes the flux only by what crosses the side wall, and the side wall's contribution is governed by $\Omega(u,\cdot)$, the canonical equation. The conservation of circulation is, at bottom, the statement that the flux of a closed two-form is a topological (boundary) quantity.

---

# What Makes This Hard

The conceptual hurdle is seeing circulation as the flux of a closed two-form rather than as a line integral to be differentiated — once $C(\mathcal{C}) = \int_\mathcal{S}\Omega$ is in hand, conservation is a statement about closed forms and Stokes' theorem. The non-obvious construction is the closed curve $\mathcal{K}$ stitched from the two loops and two fluid-line segments, whose bounded surface is the side wall of the tube; without it the cancellation of contributions is invisible. The most common error is to forget that conservation requires $T\,dS = 0$ — to assert Kelvin's theorem universally and miss that a baroclinic fluid (crossed pressure and entropy gradients) *generates* circulation, with the baroclinic term as the source.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write circulation as $\oint_\mathcal{C}\pi = \int_\mathcal{S}\Omega$ via Stokes. To compare $\mathcal{C}$ and its transported image $\mathcal{C}'$, build a closed curve $\mathcal{K}$ from the two loops joined by fluid-line segments; its bounded surface is the tube wall. Apply Stokes again, use coordinates with $u$ tangent to the wall, and reduce $\Omega(u,\cdot)$ by the canonical equation to $T\,dS$. The fluid-line segments cancel, leaving $C(\mathcal{C}) - C(\mathcal{C}') = \int_\mathcal{T} T\nabla_{e_3}S$.

**Subgoal decomposition:**

1. **Circulation as a flux.** Show $\oint_\mathcal{C}\pi = \int_\mathcal{S}\Omega$ for $\partial\mathcal{S} = \mathcal{C}$.
   - *Hint:* $\Omega = d\pi$; apply Stokes' theorem.
   - *Why needed:* Converts the conserved quantity to a flux of a closed form.

2. **Build the closed curve $\mathcal{K}$.** Stitch $\mathcal{C}$, a fluid-line segment, $\mathcal{C}'$ (reversed), and a return fluid-line segment.
   - *Hint:* $\mathcal{K}$ bounds the side wall $\mathcal{S}$ of the fluid tube.
   - *Why needed:* Sets up Stokes on the tube wall.

3. **Reduce the wall flux by the canonical equation.** In adapted coordinates with $e_2 = u$, $\int_\mathcal{S}\Omega = \int T\nabla_{e_3}S\,dx^2 dx^3$.
   - *Hint:* $\Omega(u, e_3) = T\langle dS, e_3\rangle$ by $\Omega(u,\cdot) = T\,dS$.
   - *Why needed:* It is where the thermodynamic source appears.

4. **Take the limit and cancel.** As $A\to B$, the fluid-line segments cancel, giving $C(\mathcal{C}) - C(\mathcal{C}') = \int_\mathcal{T} T\nabla_{e_3}S\,dx^2 dx^3$.
   - *Hint:* The two segments have equal and opposite contributions.
   - *Why needed:* Produces the master formula.

5. **Impose the conservation condition.** $T = 0$ or $\nabla S = 0$ on the tube kills the right side.
   - *Hint:* Entropy conservation $\nabla_u S = 0$ propagates $S$ const from $\mathcal{C}$ to $\mathcal{T}$.
   - *Why needed:* Gives $C(\mathcal{C}') = C(\mathcal{C})$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Circulation is the flux of the vorticity two-form
> **Statement:** $\oint_\mathcal{C}\pi = \int_\mathcal{S}\Omega$ for any surface $\mathcal{S}$ with $\partial\mathcal{S} = \mathcal{C}$.
>
> **Hint:** $\Omega = d\pi$; apply [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]].
>
> **Why needed:** It expresses the conserved circulation as a flux of a closed two-form, the form Stokes can act on.
>
> > [!note]- Full proof
> > The fluid momentum one-form $\pi$ is a one-form, $\mathcal{C}$ a closed oriented curve, $\mathcal{S}$ a surface bounded by $\mathcal{C}$. By [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]], $\oint_{\partial\mathcal{S}}\pi = \int_\mathcal{S} d\pi$. Since $\partial\mathcal{S} = \mathcal{C}$ and $d\pi = \Omega$ (the [[Def - Vorticity 2-Form|vorticity two-form]]), $\oint_\mathcal{C}\pi = \int_\mathcal{S}\Omega$. (The result is independent of the choice of $\mathcal{S}$ because $\Omega$ is closed, $d\Omega = d^2\pi = 0$, so two surfaces with the same boundary give the same flux.) $\blacksquare$

> [!note]- Lemma 2: The wall flux equals the baroclinic integral
> **Statement:** For the side wall $\mathcal{S}$ of the fluid tube, in coordinates adapted so that $e_2 = u$ is tangent, $\int_\mathcal{S}\Omega = \int_\mathcal{S} T\,\nabla_{e_3}S\; dx^2 dx^3$.
>
> **Hint:** $\Omega(u, e_3) = T\langle dS, e_3\rangle$ by the canonical equation.
>
> **Why needed:** It converts the geometric flux into the thermodynamic source, the heart of the obstruction.
>
> > [!note]- Full proof
> > The fluid tube is generated by fluid lines, so its tangent space at each point contains the four-velocity $u$. Choose coordinates $(x^2, x^3)$ spanning $\mathcal{S}$ with the basis vector $e_2$ equal to $u$ (possible since $u$ is tangent to the wall; $x^2$ is then proper time along the fluid lines). The integral of the two-form $\Omega$ over the surface is, by definition, $\int_\mathcal{S}\Omega(e_2, e_3)\,dx^2 dx^3 = \int_\mathcal{S}\Omega(u, e_3)\,dx^2 dx^3$. By the canonical equation $\Omega(u, \cdot) = T\,dS$ (see [[Def - Vorticity 2-Form]]), $\Omega(u, e_3) = T\langle dS, e_3\rangle = T\nabla_{e_3}S$. Hence $\int_\mathcal{S}\Omega = \int_\mathcal{S} T\nabla_{e_3}S\,dx^2 dx^3$. $\blacksquare$

> [!note]- Lemma 3: Constancy of $S$ on the loop propagates to the tube
> **Statement:** If $S = S_0$ is constant on $\mathcal{C}$, then $S = S_0$ on the whole fluid tube $\mathcal{T}$.
>
> **Hint:** The entropy per baryon is conserved along each fluid line.
>
> **Why needed:** It shows that the second sufficient condition (constant $S$ on $\mathcal{C}$) makes the baroclinic integral vanish.
>
> > [!note]- Full proof
> > The tube $\mathcal{T}$ is generated from $\mathcal{C}$ by transport along the fluid lines: every point of $\mathcal{T}$ lies on a fluid line through a point of $\mathcal{C}$. By the energy projection for an isolated simple fluid (see [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]]), the entropy per baryon is conserved along each fluid line, $\nabla_u S = 0$. So along the fluid line through any point of $\mathcal{C}$, $S$ keeps its value $S_0$ there. Since $S = S_0$ on all of $\mathcal{C}$, $S = S_0$ on all of $\mathcal{T}$, and in particular $\nabla_{e_3}S = 0$ on the tube. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — setup.** The fluid is a simple perfect fluid obeying the canonical equation $\Omega(u,\cdot) = T\,dS$, with $\Omega = d\pi$, $\pi = hu$ (see [[Def - Vorticity 2-Form]]). Circulation around a closed oriented curve is $C(\mathcal{C}) = \oint_\mathcal{C}\pi$; by Lemma 1, $C(\mathcal{C}) = \int_\mathcal{S}\Omega$ for any $\mathcal{S}$ with $\partial\mathcal{S} = \mathcal{C}$.
>
> **The master formula.** Transport $\mathcal{C}$ along the fluid lines to $\mathcal{C}'$, sweeping out the fluid tube $\mathcal{T}$. Pick points $A, B$ infinitesimally close on $\mathcal{C}$, with images $A', B'$ on $\mathcal{C}'$. Form the closed oriented curve
> $$\mathcal{K} = \mathcal{L}_{A\to A'}\cup\mathcal{C}'_{A'\to B'}\cup\mathcal{L}_{B'\to B}\cup\mathcal{C}_{B\to A},$$
> where the $\mathcal{L}$ are fluid-line segments and the loop pieces cover most of $\mathcal{C}'$ and $\mathcal{C}$. Let $\mathcal{S}$ be the part of the tube wall bounded by $\mathcal{K}$. By Lemma 1 (Stokes), $\oint_\mathcal{K}\pi = \int_\mathcal{S}\Omega$, and by Lemma 2, $\int_\mathcal{S}\Omega = \int_\mathcal{S} T\nabla_{e_3}S\,dx^2 dx^3$.
>
> Now decompose $\oint_\mathcal{K}\pi = \int_{\mathcal{L}_{A\to A'}}\pi + \int_{\mathcal{C}'_{A'\to B'}}\pi + \int_{\mathcal{L}_{B'\to B}}\pi + \int_{\mathcal{C}_{B\to A}}\pi$. As $A\to B$: the two fluid-line integrals $\mathcal{L}_{A\to A'}$ and $\mathcal{L}_{B'\to B}$ tend to equal and opposite values and cancel; $\int_{\mathcal{C}_{B\to A}}\pi\to C(\mathcal{C})$; $\int_{\mathcal{C}'_{A'\to B'}}\pi\to -C(\mathcal{C}')$ (opposite orientation); and $\mathcal{S}\to\mathcal{T}$. Therefore
> $$C(\mathcal{C}) - C(\mathcal{C}') = \int_\mathcal{T} T\,\nabla_{e_3}S\; dx^2 dx^3, \qquad\text{i.e.}\qquad C(\mathcal{C}') = C(\mathcal{C}) - \int_\mathcal{T} T\,\nabla_{e_3}S\; dx^2 dx^3.$$
>
> **Conservation conditions.** If the fluid is barotropic, $T = 0$, the integral vanishes and $C(\mathcal{C}') = C(\mathcal{C})$. If $S$ is constant on $\mathcal{C}$, then by Lemma 3 it is constant on the whole tube $\mathcal{T}$, so $\nabla_{e_3}S = 0$ there and again $C(\mathcal{C}') = C(\mathcal{C})$. In either case the circulation is conserved by transport along the fluid lines.
>
> **Nonrelativistic limit.** With $h\to m_{\mathrm b}c^2$ constant, $\pi = hu\to m_{\mathrm b}c^2 u$, and (restoring $c$, with $\mathcal{C}$ in an observer's rest space) $C(\mathcal{C})\to m_{\mathrm b}c\oint_\mathcal{C}\mathbf{V}\cdot d\boldsymbol\ell$, the classical circulation up to the constant $m_{\mathrm b}c$; the theorem becomes the classical Kelvin circulation theorem. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Vorticity generation in stratified flows (geophysical fluid dynamics).** Read backwards, the theorem's baroclinic term $T\,dS$ is the source of circulation in a baroclinic fluid — crossed gradients of pressure and entropy (or density). This is the mechanism of the sea breeze and of baroclinic instability in the atmosphere. The application is nonobvious because the *failure* of the conservation theorem is itself a predictive law: $\nabla p\times\nabla\rho$ creates vorticity.

**Magnetic flux freezing in a perfect conductor (plasma physics).** The structural twin of Kelvin's theorem: for a perfectly conducting fluid, the electromagnetic field two-form $F = dA$ replaces $\Omega = d\pi$, and the conserved flux $\int_\mathcal{S}F$ through a transported loop is Alfvén's frozen-in theorem. The application is out-of-distribution because it concerns magnetic fields rather than vorticity, yet the proof is identical — a closed two-form's flux is conserved by transport — and it governs jet collimation and dynamo action.

**Potential vorticity in numerical weather prediction (atmospheric science).** The local form $\nabla_u e = 0$ for the potential vorticity $e = (h/n)\nabla_{\boldsymbol\omega}S$ is the relativistic parent of Ertel's potential-vorticity theorem, a conserved tracer carried by each fluid parcel. The application is surprising because potential vorticity, a cornerstone of weather forecasting, descends from the same canonical equation as the circulation theorem.

---

# Bridges

- **[[Def - Vorticity 2-Form]]** — Kelvin's theorem is the integral expression of the canonical equation $\Omega(u,\cdot) = T\,dS$. The circulation is the flux of $\Omega = d\pi$; the closedness $d\Omega = 0$ makes the flux a boundary quantity, and the canonical equation supplies the baroclinic obstruction. The vorticity two-form is the object whose flux is the transported invariant.

- **[[Thm - Stokes Theorem on Spacetime]]** — the engine of the proof, used twice: once to write circulation as the flux of $\Omega$, and once to convert the difference of circulations into the flux through the tube wall. Stokes' theorem is what turns the line-integral conservation law into a statement about a closed two-form.

- **[[Thm - Relativistic Bernoulli Theorem]]** — the companion conservation law from the same canonical equation. Bernoulli conserves a scalar along a fluid line (a symmetry/Noether statement); Kelvin conserves a circulation around a loop (a flux/Stokes statement). Both require $T\,dS = 0$ for the cleanest form, and both are corollaries of $\Omega(u,\cdot) = T\,dS$.

- **Alfvén's frozen-in theorem (magnetohydrodynamics)** — the exact structural analogue. For a perfectly conducting fluid the magnetic flux $\int_\mathcal{S}F$ through a transported loop is conserved, by the identical argument with the electromagnetic two-form $F = dA$ in place of the vorticity two-form $\Omega = d\pi$. Both are statements that the flux of a closed, exact two-form is a transport invariant, with the side walls of the swept tube contributing nothing.

---

# Unlocked by This

> [!tip] Alfvén's Frozen-In Theorem and Jet Collimation *(from Plasma Astrophysics)*
> The relativistic-MHD analogue of Kelvin's theorem is **Alfvén's frozen-in theorem**: in a perfectly conducting fluid, magnetic field lines are frozen into the matter and the flux through any comoving loop is conserved. This is the mechanism by which rotating accretion disks wind up and collimate **magnetized jets**, and by which stellar dynamos amplify magnetic fields. The vorticity two-form and the electromagnetic two-form play identical geometric roles.

> [!tip] Ertel's Potential Vorticity and Weather Prediction *(from Geophysical Fluid Dynamics)*
> The local conservation $\nabla_u e = 0$ of the **potential vorticity** $e = (h/n)\nabla_{\boldsymbol\omega}S$ is the relativistic ancestor of **Ertel's theorem**, the statement that potential vorticity is a materially conserved tracer. In the atmosphere and ocean this is the single most useful conserved quantity, the basis of potential-vorticity thinking in dynamical meteorology and of the inversion principle that reconstructs the flow from the PV field.

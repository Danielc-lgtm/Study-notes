---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - Stokes Theorem on Spacetime"
  - "Def - Volume, Area, Length Elements and Flux Integrals"
  - "Def - The Hodge Star"
  - "Thm - Divergence of a Vector and Tensor Field"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$. $\mathscr{V}$ is an oriented compact submanifold-with-boundary, with boundary $\partial\mathscr{V}$; $\vec{v}$ is a vector field with metric dual 1-form $\underline{v}$ and four-divergence $\nabla\cdot\vec{v} = \nabla_\mu v^\mu$ (see [[Thm - Divergence of a Vector and Tensor Field]]). $\star$ is the [[Def - The Hodge Star|Hodge star]], $\epsilon$ the Levi-Civita tensor, $\mathrm{d}U = \sqrt{|g|}\,\mathrm{d}^4x$ the four-volume element, $\mathrm{d}V$ the hypersurface volume element, and $\Phi_{\mathscr{V}}(\vec{v}) = \int_{\mathscr{V}}\star\underline{v}$ the [[Def - Volume, Area, Length Elements and Flux Integrals|flux]]. In the 3D statement $\mathrm{d}\vec{S}$ is the outward area-element vector of a surface in a spatial slice. Full registry on [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem]].

---

# Statement

> **Four-dimensional Gauss–Ostrogradsky theorem.** Let $\mathscr{V}$ be a four-dimensional compact submanifold-with-boundary of $\mathscr{E}$, with boundary the closed hypersurface $\partial\mathscr{V}$. For any vector field $\vec{v}$ on $\mathscr{E}$, the flux of $\vec{v}$ out through $\partial\mathscr{V}$ equals the integral of its four-divergence over $\mathscr{V}$:
> $$\Phi_{\partial\mathscr{V}}(\vec{v}) \;=\; \int_{\partial\mathscr{V}}\star\underline{v} \;=\; \int_{\mathscr{V}} \nabla\cdot\vec{v}\,\,\mathrm{d}U .$$

> **Three-dimensional Gauss–Ostrogradsky theorem.** Let $\mathscr{V}$ be a three-dimensional compact submanifold-with-boundary contained in a spacelike hyperplane $\Sigma$ ($t = \mathrm{const}$), and let $\vec{v}$ be a vector field tangent to $\Sigma$. Then
> $$\int_{\mathscr{V}} \nabla\cdot\vec{v}\,\,\mathrm{d}V \;=\; \oint_{\partial\mathscr{V}} \vec{v}\cdot\mathrm{d}\vec{S} ,$$
> where $\nabla\cdot\vec{v} = \partial v^i/\partial x^i$ is the ordinary three-dimensional divergence within $\Sigma$ and $\mathrm{d}\vec{S}$ the outward area element. This is the classical divergence (Gauss) theorem.

Both are corollaries of [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] applied to a flux integral. Unlike Stokes' theorem itself, **they depend on the metric** — through the divergence, the volume element, and the flux.

---

# Motivation

Stokes' theorem, $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$, is metric-free and abstract: it relates two integrals of forms. But the conservation laws of physics are not stated about forms — they are stated about *divergences* ("$\nabla\cdot J = 0$") and *fluxes* ("the current crossing the boundary"). The Gauss–Ostrogradsky theorems are the translation: they convert Stokes' abstract identity into the concrete statement that the flux of a vector field out of a closed boundary equals the integral of its divergence inside. This is the form in which every conservation law in the rest of the relativity course will be used.

The two versions answer two physically distinct questions. The three-dimensional version lives inside a single instant of time: it relates the divergence of a spatial vector field over a region of space to its flux through the bounding surface, and it is the divergence theorem of ordinary vector calculus — the tool behind Gauss's law, the continuity of a fluid in a fixed volume, and so on. The four-dimensional version lives in spacetime: its "region" is a four-dimensional chunk of spacetime, its "boundary" is a closed hypersurface (which typically consists of two spacelike slices capped by a timelike tube), and it relates the four-divergence over the chunk to the net flux out through the closed hypersurface. *This* is the one that matters for relativity, because it is the bridge between the local conservation law $\nabla\cdot J = 0$ and the global statement that total charge is conserved and the same on every slice.

Why should the flux out of a boundary equal the integral of the divergence inside? Because the divergence *is* the local rate at which the field "spreads out", the infinitesimal flux per unit volume out of an infinitesimal box. Summing this local outflow over all the boxes that tile the region, the outflow from each internal box face is the inflow to its neighbour and cancels, leaving only the outflow through the region's outer boundary. That is the same telescoping that powers Stokes' theorem, and indeed the Gauss–Ostrogradsky theorem is *literally* Stokes applied to the Hodge dual of the field — the divergence appearing because $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$.

---

# Sources and Targets

**Sources (Input Broadening)**

The 4D theorem's precondition is "a vector field $\vec{v}$ on a four-region $\mathscr{V}$ with closed boundary".

The first disguised source is **"a conserved current is given"**: any $\vec{v}$ with $\nabla\cdot\vec{v} = 0$. The theorem then says the net flux out of *every* closed hypersurface vanishes. The bridge is that the right-hand side $\int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$ is zero. The nonobviousness is that a *local* condition (divergence vanishes at every point) yields a *global* one (flux through any closed surface vanishes), which is exactly the local-to-global passage conservation laws need. *Example problem:* charge conservation, $\nabla\cdot J = 0$, giving slice-independence of total charge ([[Ex - Charge conservation as a flux statement]]).

The second disguised source is **"a symmetric tensor with a conserved index"**: a type-$(2,0)$ tensor $T^{\mu\nu}$ with $\nabla_\mu T^{\mu\nu} = 0$ supplies, for each fixed $\nu$, a conserved vector $v^\mu = T^{\mu\nu}$. The theorem applied to each such vector gives the conservation of the corresponding component of total four-momentum. The bridge is "freeze the free index and treat the result as a vector". The nonobviousness is that a *tensor* conservation law unpacks into four *vector* conservation laws, each handled by this theorem. *Example problem:* energy-momentum conservation $\nabla_\mu T^{\mu\nu} = 0$ in [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

The third disguised source is **"a flux must be compared across two surfaces"**: whenever you want to show two flux integrals agree (or differ by a known amount), enclose the spacetime between the two surfaces and apply the theorem. The bridge is that the difference of the two fluxes is the net flux out of the enclosing boundary, hence the integral of the divergence in between. *Example problem:* showing the total charge on slice $\Sigma_1$ equals that on $\Sigma_2$.

**Targets (Output Amplification)**

The conclusion is "$\int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$".

Combine the conclusion with **a closed boundary made of two spacelike slices plus a tube at spatial infinity, with $\vec{v}\to 0$ at infinity**. The tube contributes nothing, so the net flux is the difference of the two slice-fluxes; if $\nabla\cdot\vec{v}=0$ this difference is zero. The further result is that the total charge $Q_\Sigma = \int_\Sigma\star\underline{v}$ is the *same on every spacelike slice* — conservation and slice-independence at once. The combination is the central application of the theorem and the reason it exists.

Combine the conclusion with **a four-region shrunk to an infinitesimal box**. Dividing by the box's four-volume and taking the limit, the theorem reduces to the *definition* of the divergence as flux per unit volume: $\nabla\cdot\vec{v} = \lim\frac{1}{\mathrm{vol}}\oint\star\underline{v}$. The further result is an operational, coordinate-free characterisation of the divergence. The combination is useful because it inverts the theorem to *define* the very quantity it relates fluxes to.

Combine the conclusion with **a region where $\nabla\cdot\vec{v} = \sigma$ is a known source**. Then $\int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\sigma\,\mathrm{d}U$: the net flux out equals the total source enclosed. The further result is Gauss's-law-type counting — the flux of a field through a closed surface counts the charge inside. The combination is the relativistic generalisation of Gauss's law for electromagnetism.

---

# Why Is It True

The intuition is that the divergence is "outflow per unit volume", and summing outflows lets all the internal flows cancel.

Picture the four-region $\mathscr{V}$ tiled by tiny four-dimensional boxes. For each box, the net flux of $\vec{v}$ out through its eight faces, divided by the box's four-volume, is — in the limit of a small box — exactly the four-divergence $\nabla\cdot\vec{v}$ at that point. (This is what the divergence *means*: the local tendency of the field to spread out, measured as flux per volume.) So the integral of $\nabla\cdot\vec{v}$ over $\mathscr{V}$ is the sum, over all the boxes, of their individual net outflows. Now comes the cancellation: every internal face is shared by two adjacent boxes, and what flows *out* of one box through that face flows *into* the other — the two contributions are equal and opposite and cancel. Only the faces on the outer boundary $\partial\mathscr{V}$ are unshared, and their outflows survive. The grand total is therefore the net flux out through $\partial\mathscr{V}$.

**The divergence is flux-per-volume, so integrating it sums every box's outflow, and all the internal outflows cancel against the neighbouring inflows, leaving only the flux through the outer skin.** This is word-for-word the mechanism of Stokes' theorem, and indeed the cleanest proof is just Stokes applied to the 3-form $\star\underline{v}$: its exterior derivative is $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$ (the precise statement that "the derivative of the flux-form is the divergence times the volume-form"), so $\int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\mathrm{d}\star\underline{v} = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$. The Gauss–Ostrogradsky theorem is Stokes' theorem wearing the clothes of vector calculus.

The metric dependence, absent from Stokes' theorem, enters through three places, all on the way from forms to vectors: the divergence $\nabla\cdot\vec{v} = \nabla_\mu v^\mu$ uses the connection (hence the metric); the volume element $\mathrm{d}U = \sqrt{|g|}\,\mathrm{d}^4x$ uses the metric; and the flux $\int\star\underline{v}$ uses the Hodge star and the metric dual. Stokes' theorem about the *form* $\star\underline{v}$ is metric-free; the *interpretation* of $\star\underline{v}$ as a flux and of $\mathrm{d}\star\underline{v}$ as a divergence is where the metric lives.

---

# What Makes This Hard

The proof itself is short once Stokes' theorem and the identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$ are in hand; the difficulty is conceptual and in the book-keeping of the *closed* boundary. Most people stumble on the geometry of the 4D boundary: a typical four-region is bounded by two spacelike slices *and* a timelike tube, and getting the orientations right — so that the past slice contributes with a flipped sign and the tube drops out when the field vanishes at infinity — is where errors creep in. The other subtlety is keeping straight that this theorem, unlike Stokes', is metric-dependent: a reader who has just absorbed "Stokes is metric-free" can wrongly assume the same of its corollary.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct both theorems.**

**High-level strategy:**
For the 4D theorem, write the flux through the closed boundary as $\int_{\partial\mathscr{V}}\star\underline{v}$, apply Stokes' theorem to turn it into $\int_{\mathscr{V}}\mathrm{d}\star\underline{v}$, and use $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$. For the 3D theorem, build the 2-form $A = \epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$ from the spatial field $\vec{v}$, compute that $\mathrm{d}A$ has the 3D divergence as its surviving component and that $A$ on the boundary is $\vec{v}\cdot\mathrm{d}\vec{S}$, and apply Stokes.

**Subgoal decomposition:**

1. **(4D) Express the flux as a form integral.** Write $\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\partial\mathscr{V}}\star\underline{v}$.
   - *Hint:* This is the definition of the flux ([[Def - Volume, Area, Length Elements and Flux Integrals]]).
   - *Why needed:* It puts the flux into the shape Stokes consumes.

2. **(4D) Apply Stokes and the divergence identity.** $\int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\mathrm{d}\star\underline{v} = \int_{\mathscr{V}}(\nabla\cdot\vec{v})\epsilon = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$.
   - *Hint:* $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$ and $\int_{\mathscr{V}}f\epsilon = \int_{\mathscr{V}}f\,\mathrm{d}U$.
   - *Why needed:* It is the whole derivation; the result is the 4D theorem.

3. **(3D) Build the 2-form from the spatial field.** For $\vec{v}$ tangent to $\Sigma$ ($t=0$), set $A := \epsilon(\vec{e}_0, \vec{v}, \cdot, \cdot)$.
   - *Hint:* In an orthonormal inertial basis $A_{0\alpha} = 0$ and $A_{ij} = \epsilon_{0ijk}v^k$ — only spatial-spatial components.
   - *Why needed:* It packages the spatial vector into a 2-form whose exterior derivative is the 3D divergence.

4. **(3D) Compute $\mathrm{d}A$ and $A|_{\partial\mathscr{V}}$, apply Stokes.** Show $\int_{\mathscr{V}}\mathrm{d}A = \int_{\mathscr{V}}(\partial_i v^i)\,\mathrm{d}V$ and $\int_{\partial\mathscr{V}} A = \oint_{\partial\mathscr{V}}\vec{v}\cdot\mathrm{d}\vec{S}$.
   - *Hint:* $\mathrm{d}A$ picks out $\partial_1 A_{23} + \partial_2 A_{31} + \partial_3 A_{12} = \partial_i v^i$; on the boundary $A$ contracts the area-element vector to $\vec{v}\cdot\mathrm{d}\vec{S}$.
   - *Why needed:* It identifies both sides of Stokes with the classical divergence theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The exterior derivative of the flux 3-form is the divergence times the volume form
> **Statement:** For a vector field $\vec{v}$, $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\,\epsilon$.
>
> **Hint:** Compute in components: $(\star\underline{v})_{\alpha\beta\gamma} = v^\mu\epsilon_{\mu\alpha\beta\gamma}$, and the exterior derivative contracts an index that, via the divergence formula $\nabla\cdot\vec{v} = \frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\,v^\mu)$, reproduces the divergence.
>
> **Why needed:** It is the single identity that turns Stokes' theorem into the Gauss–Ostrogradsky theorem; without it the flux form's exterior derivative would not visibly be the divergence.
>
> > [!note]- Full proof
> > The Hodge dual of $\underline{v}$ is the 3-form with components $(\star\underline{v})_{\alpha\beta\gamma} = \epsilon_{\mu\alpha\beta\gamma}v^\mu$. Its exterior derivative is the 4-form $\mathrm{d}\star\underline{v}$ with the single independent component $(\mathrm{d}\star\underline{v})_{0123}$. Using the coordinate expression of $\mathrm{d}$ on a 3-form and the constancy of the Levi-Civita components up to the $\sqrt{|g|}$ factor, one finds $(\mathrm{d}\star\underline{v})_{0123} = \partial_\mu(\sqrt{|g|}\,v^\mu)$. The four-divergence in arbitrary coordinates is $\nabla\cdot\vec{v} = \nabla_\mu v^\mu = \frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\,v^\mu)$ (see [[Thm - Divergence of a Vector and Tensor Field]]), so $(\mathrm{d}\star\underline{v})_{0123} = \sqrt{|g|}\,\nabla\cdot\vec{v} = (\nabla\cdot\vec{v})\,\epsilon_{0123}$. Since both $\mathrm{d}\star\underline{v}$ and $(\nabla\cdot\vec{v})\epsilon$ are 4-forms agreeing in their single component, they are equal. $\blacksquare$

> [!note]- Lemma 2: The 2-form $\epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$ has the 3D divergence as its surviving derivative
> **Statement:** For $\vec{v}$ tangent to the slice $\Sigma$ ($t=0$) in inertial coordinates, $A := \epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$ satisfies $A_{0\alpha}=0$, $A_{ij} = \epsilon_{0ijk}v^k$, and $\int_{\mathscr{V}}\mathrm{d}A = \int_{\mathscr{V}}(\partial_i v^i)\,\mathrm{d}V$.
>
> **Hint:** With $\det g = -1$ in the inertial frame, $A_{23}=v^1$, $A_{31}=v^2$, $A_{12}=v^3$, and the $0123$-component of $\mathrm{d}A$ is $\partial_1 A_{23}+\partial_2 A_{31}+\partial_3 A_{12}$.
>
> **Why needed:** It is the bridge from the spatial vector field to a form Stokes can act on, producing the 3D divergence on the bulk side.
>
> > [!note]- Full proof
> > In the inertial frame $(\vec{e}_\alpha)$ is orthonormal and $\epsilon_{0123}=1$. The components of $A = \epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$ are $A_{\alpha\beta} = \epsilon_{\mu\nu\alpha\beta}\,\delta^\mu_0\,v^\nu = \epsilon_{0\nu\alpha\beta}v^\nu$. Since $\epsilon_{0\nu\alpha\beta}$ vanishes unless $\nu,\alpha,\beta$ are a permutation of $1,2,3$, all components with a $0$ index vanish, $A_{0\alpha}=0$, and the spatial components are $A_{ij}=\epsilon_{0ijk}v^k$, explicitly $A_{23}=v^1$, $A_{31}=v^2$, $A_{12}=v^3$. As $(x^\alpha)$ is adapted to $\mathscr{V}$, the integral of the 3-form $\mathrm{d}A$ uses its $123$-component, $(\mathrm{d}A)_{123} = \partial_1 A_{23}+\partial_2 A_{31}+\partial_3 A_{12} = \partial_1 v^1+\partial_2 v^2+\partial_3 v^3 = \partial_i v^i$, the 3D divergence. With $\mathrm{d}V = \mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$ ($n^0=1$, $\sqrt{|g|}=1$), $\int_{\mathscr{V}}\mathrm{d}A = \int_{\mathscr{V}}\partial_i v^i\,\mathrm{d}V$. $\blacksquare$

> [!note]- Lemma 3: The boundary integral is the classical surface flux
> **Statement:** With $A = \epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$ as above, $\int_{\partial\mathscr{V}} A = \oint_{\partial\mathscr{V}}\vec{v}\cdot\mathrm{d}\vec{S}$.
>
> **Hint:** Parametrise $\partial\mathscr{V}$ by $(u,v)$; the area-element vector is $\mathrm{d}\vec{S} = \mathrm{d}\vec{\ell}_u\times\mathrm{d}\vec{\ell}_v$, and $A$ applied to $(\mathrm{d}\vec{\ell}_u, \mathrm{d}\vec{\ell}_v)$ equals $\vec{v}\cdot\mathrm{d}\vec{S}$.
>
> **Why needed:** It identifies the boundary side of Stokes with the classical "$\vec{v}\cdot\mathrm{d}\vec{S}$" flux, completing the divergence theorem.
>
> > [!note]- Full proof
> > Let $(x'^\alpha) = (ct, w, u, v)$ be adapted to $\partial\mathscr{V}$, with $w=0$ on the boundary and $w<0$ inside. The integral of the 2-form $A$ over the surface uses the component $A'_{uv}$ in these coordinates, related to the inertial components by $A'_{uv} = A_{\alpha\beta}\,\frac{\partial x^\alpha}{\partial u}\frac{\partial x^\beta}{\partial v}$. Substituting the values of $A_{ij}$ from Lemma 2 and expanding, $A'_{uv} = v^x(\partial_u y\,\partial_v z - \partial_u z\,\partial_v y) + v^y(\partial_u z\,\partial_v x - \partial_u x\,\partial_v z) + v^z(\partial_u x\,\partial_v y - \partial_u y\,\partial_v x)$. The three parentheses are exactly the components of the cross product $\mathrm{d}\vec{\ell}_u\times\mathrm{d}\vec{\ell}_v$, i.e. the components of the area-element vector $\mathrm{d}\vec{S}$, so $A'_{uv}\,\mathrm{d}u\,\mathrm{d}v = v^x\,\mathrm{d}S^x + v^y\,\mathrm{d}S^y + v^z\,\mathrm{d}S^z = \vec{v}\cdot\mathrm{d}\vec{S}$. Integrating gives $\int_{\partial\mathscr{V}} A = \oint_{\partial\mathscr{V}}\vec{v}\cdot\mathrm{d}\vec{S}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Four-dimensional theorem.** Let $\mathscr{V}$ be a four-dimensional compact submanifold-with-boundary with closed boundary $\partial\mathscr{V}$. By the definition of the flux ([[Def - Volume, Area, Length Elements and Flux Integrals]]), $\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\partial\mathscr{V}}\star\underline{v}$, where $\star\underline{v}$ is the Hodge dual of the metric dual 1-form. The 3-form $\star\underline{v}$ is a $(4-1)$-form, so [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] applies to it on the four-region $\mathscr{V}$:
> $$\int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\mathrm{d}\star\underline{v} .$$
> By Lemma 1, $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\,\epsilon$, and by the definition of the integral of a 4-form, $\int_{\mathscr{V}}(\nabla\cdot\vec{v})\,\epsilon = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$. Combining,
> $$\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U. \qquad\blacksquare$$
>
> **Three-dimensional theorem.** Let $\mathscr{V}\subset\Sigma$ be a three-dimensional compact submanifold-with-boundary in the spacelike hyperplane $\Sigma$ ($t=0$), in inertial coordinates $(ct,x,y,z)$, with $\vec{v}$ tangent to $\Sigma$. Form the 2-form $A := \epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$. By Lemma 2, $\int_{\mathscr{V}}\mathrm{d}A = \int_{\mathscr{V}}\partial_i v^i\,\mathrm{d}V = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}V$ (the 3D divergence). Since $\mathscr{V}$ is three-dimensional and $A$ is a $2$-form (a $(p-1)$-form with $p=3$), [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] applies: $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$. By Lemma 3, $\int_{\partial\mathscr{V}} A = \oint_{\partial\mathscr{V}}\vec{v}\cdot\mathrm{d}\vec{S}$. Combining,
> $$\int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}V = \oint_{\partial\mathscr{V}}\vec{v}\cdot\mathrm{d}\vec{S}. \qquad\blacksquare$$
>
> Both results use Stokes' theorem (metric-free) plus identities relating forms to the divergence and flux (metric-dependent), which is why the Gauss–Ostrogradsky theorems depend on the metric while Stokes' theorem does not.

---

# Cross-Field Exercise Suggestions

**Gauss's law in electrostatics.** The flux of the electric field through a closed surface equals the enclosed charge over $\varepsilon_0$: $\oint\vec{E}\cdot\mathrm{d}\vec{S} = Q_{\text{enc}}/\varepsilon_0$. This is the 3D Gauss theorem applied to $\vec{E}$ with $\nabla\cdot\vec{E} = \rho/\varepsilon_0$. The application is the historical origin of the theorem and the workhorse of electrostatics; recognising it as a special case of the relativistic 4D statement (with the static current) unifies it with charge conservation.

**Hydrodynamic continuity in a fixed volume.** For a fluid of density $\rho$ and velocity $\mathbf{u}$, the rate of change of mass in a fixed spatial region equals minus the flux of $\rho\mathbf{u}$ through its surface: $\frac{d}{dt}\int_V\rho\,\mathrm{d}V = -\oint_{\partial V}\rho\mathbf{u}\cdot\mathrm{d}\vec{S}$, which is the 3D Gauss theorem applied to the mass current. The relativistic upgrade is the 4D version applied to the baryon four-current in [[Special Relativity XXIV — Relativistic Hydrodynamics]], where the "fixed volume" is replaced by a spacetime region.

**The Aharonov–Bohm phase and flux quantisation.** The magnetic flux through a surface is $\int\vec{B}\cdot\mathrm{d}\vec{S} = \oint\vec{A}\cdot\mathrm{d}\vec{\ell}$ by the Kelvin–Stokes theorem (the surface companion of Gauss), and when the surface surrounds a region the field cannot enter, this flux is a topological invariant detectable only quantum-mechanically. The application is out-of-distribution because it uses the theorem to expose a *physical effect of a potential in a field-free region* — the deepest demonstration that the form-level statement carries information the field-level statement loses.

---

# Bridges

- **[[Thm - Stokes Theorem on Spacetime]]** — both Gauss–Ostrogradsky theorems are this theorem applied to a particular form: the 4D version to the 3-form $\star\underline{v}$ (using $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$), the 3D version to the 2-form $\epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$ inside a spatial slice. Stokes' theorem is metric-free; the Gauss–Ostrogradsky theorems acquire metric dependence through the divergence, volume element, and flux that translate the abstract forms into vector-calculus quantities.

- **[[Thm - Divergence of a Vector and Tensor Field]]** — the four-divergence $\nabla\cdot\vec{v} = \frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\,v^\mu)$ is the quantity this theorem integrates, and the identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$ (Lemma 1) is what links it to the exterior derivative of the flux form. The $\sqrt{|g|}$ in the divergence formula is the *same* $\sqrt{|g|}$ as in the volume element — both are the metric volume factor — which is why the divergence and the volume element conspire to make the theorem coordinate-independent.

- **The classical divergence theorem of vector calculus** — the 3D version *is* the ordinary Gauss divergence theorem, recovered here as the spatial-slice special case. The relativistic content is the 4D version, which ordinary vector calculus cannot state (it has no fourth dimension): the flux through a *closed hypersurface in spacetime* equals the integral of the *four*-divergence, and it is this that elevates "flux out of a box of space" to "flux out of a box of spacetime", the statement conservation laws need.

- **[[Special Relativity XXII — Maxwell's Equations]]** — charge conservation, $\nabla\cdot J = 0$, becomes via the 4D theorem the vanishing of the flux of $J$ through every closed hypersurface, hence the slice-independence of total charge; this is the rigorous content of "Maxwell's equations conserve charge", and it is forced by $\mathrm{d}\circ\mathrm{d}=0$ applied to the inhomogeneous equation $\mathrm{d}\star F = \mu_0\star J$. The theorem is the bridge between the local field equations and the global conservation they imply.

---

# Unlocked by This

> [!tip] Conservation of Energy-Momentum and the ADM Mass *(from General Relativity)*
> Applied to each component of a conserved energy-momentum tensor, $\nabla_\mu T^{\mu\nu}=0$, this theorem gives the conservation and slice-independence of the total four-momentum $P^\nu = \int_\Sigma T^{\nu\mu}\,\mathrm{d}\Sigma_\mu$ — the relativistic statement of energy and momentum conservation, derived in [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]]. In **general relativity** the gravitational field carries energy that no local tensor captures, and the only well-defined total energy of an isolated system is the **ADM mass**, a flux integral of the metric's deviation from flatness over a sphere at spatial infinity — the 4D Gauss theorem applied in the asymptotic region. The failure of a local, slice-by-slice energy in curved spacetime, and its replacement by a boundary flux at infinity, is one of the deepest features of gravitation, and it is this theorem operating where no global conservation otherwise exists.

> [!tip] Noether's Theorem and the Current–Charge Correspondence *(from Field Theory)*
> This theorem is the second half of **Noether's theorem**: Noether's first half produces, from a continuous symmetry, a current $J$ with $\nabla\cdot J=0$; this theorem then converts that local conservation into a conserved charge $Q = \int_\Sigma\star\underline{J}$, constant in time and independent of the slice. The pairing is exact and universal — phase symmetry gives electric charge, spacetime-translation symmetry gives energy-momentum, Lorentz symmetry gives angular momentum — and the 4D Gauss theorem is precisely the step "local conservation $\Rightarrow$ conserved total" in every case. It is the reason symmetries and conservation laws are two sides of one coin.

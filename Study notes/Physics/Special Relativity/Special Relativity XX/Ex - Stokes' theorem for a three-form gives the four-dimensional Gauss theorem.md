---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Stokes Theorem on Spacetime"
  - "Thm - Gauss-Ostrogradsky Theorem (3D and 4D)"
  - "Def - Volume, Area, Length Elements and Flux Integrals"
  - "Def - The Hodge Star"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$.

1. Let $\mathscr{V}$ be a four-dimensional compact submanifold-with-boundary of spacetime, with closed boundary hypersurface $\partial\mathscr{V}$. Starting from the flux of a vector field $\vec{v}$ through $\partial\mathscr{V}$, written as $\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\partial\mathscr{V}}\star\underline{v}$, apply Stokes' theorem to convert it into a four-volume integral.
2. Prove the identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\,\epsilon$, where $\nabla\cdot\vec{v} = \nabla_\mu v^\mu$ is the four-divergence, by computing the single component $(\mathrm{d}\star\underline{v})_{0123}$ in arbitrary coordinates.
3. Combine parts 1 and 2 to obtain the four-dimensional Gauss–Ostrogradsky theorem $\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$.
4. Carry out the analogous derivation for a three-dimensional region inside a spatial slice, recovering the classical divergence theorem $\int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}V = \oint_{\partial\mathscr{V}}\vec{v}\cdot\mathrm{d}\vec{S}$, and identify which step is metric-dependent.

**Recall:**

Stokes' theorem and the flux are as follows.

![[Thm - Stokes Theorem on Spacetime#Statement]]

The flux of $\vec{v}$ through a hypersurface is $\Phi_{\mathscr{V}}(\vec{v}) = \int_{\mathscr{V}}\star\underline{v}$ ([[Def - Volume, Area, Length Elements and Flux Integrals]]). The four-divergence in arbitrary coordinates is $\nabla\cdot\vec{v} = \nabla_\mu v^\mu = \frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\,v^\mu)$. The Hodge dual of $\underline{v}$ has components $(\star\underline{v})_{\alpha\beta\gamma} = v^\mu\epsilon_{\mu\alpha\beta\gamma}$, with $\epsilon_{0123} = \sqrt{|g|}$.

---

# Convergent Strategy

**Problem class.** A *derive-a-theorem-from-a-more-fundamental-one* problem: obtain the Gauss–Ostrogradsky divergence theorems as corollaries of the master Stokes theorem. It is the central derivation of [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem#Problem-Solving Strategy|§20.3]].

**Assumption pattern.** A four-region with closed boundary and a vector field. The signpost is that the flux $\int_{\partial\mathscr{V}}\star\underline{v}$ is the integral of a *3-form over a closed 3-boundary* — exactly the right-hand side of Stokes' theorem with $A = \star\underline{v}$. The whole derivation is recognising this and supplying the identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$.

**Theorem routing.** Part 1 applies [[Thm - Stokes Theorem on Spacetime]] to $A = \star\underline{v}$. Part 2 is a component computation establishing $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$ ([[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)|Lemma 1]]). Part 3 combines them. Part 4 repeats the pattern with the 2-form $\epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$ inside a slice.

**Key decision point.** The crux is the identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\,\epsilon$: it is what makes "the exterior derivative of the flux form" equal to "the divergence times the volume form", and without it Stokes would give an uninterpreted four-volume integral. The non-obvious part is verifying that the $\frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}v^\mu)$ form of the divergence is exactly what the exterior derivative of $\star\underline{v}$ produces — the two $\sqrt{|g|}$ factors (one in $\epsilon$, one in the divergence) must conspire.

---

# Legal Operations Used

1. **Operation 4 from the topic page (express a flux as the integral of a Hodge dual).** The flux is written $\int_{\partial\mathscr{V}}\star\underline{v}$, putting it into the form Stokes consumes.

2. **Operation 5 from the topic page (apply Stokes' theorem to trade $\mathrm{d}$ for $\partial$).** Stokes converts the boundary flux into a four-volume integral of $\mathrm{d}\star\underline{v}$.

3. **Operation 6 from the topic page (use the identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$).** This identity, proved in part 2, is the bridge from the abstract four-volume integral to the divergence.

---

# Hints

> [!note]- Hint 1
> $\star\underline{v}$ is a 3-form, which is a $(4-1)$-form, so Stokes' theorem applies to it on the four-region $\mathscr{V}$: $\int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\mathrm{d}\star\underline{v}$.

> [!note]- Hint 2
> Compute $(\mathrm{d}\star\underline{v})_{0123}$. The exterior derivative of a 3-form $B$ has $(\mathrm{d}B)_{0123} = \partial_0 B_{123} - \partial_1 B_{023} + \dots$ (antisymmetrised). With $B = \star\underline{v}$, $B_{\alpha\beta\gamma} = v^\mu\epsilon_{\mu\alpha\beta\gamma}$, this collapses to $\partial_\mu(\sqrt{|g|}\,v^\mu)$.

> [!note]- Hint 3
> Then $(\mathrm{d}\star\underline{v})_{0123} = \partial_\mu(\sqrt{|g|}v^\mu) = \sqrt{|g|}\cdot\frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}v^\mu) = \sqrt{|g|}\,\nabla\cdot\vec{v} = (\nabla\cdot\vec{v})\,\epsilon_{0123}$. So $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$.

> [!note]- Hint 4
> Combining: $\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\mathrm{d}\star\underline{v} = \int_{\mathscr{V}}(\nabla\cdot\vec{v})\epsilon = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$. For the 3D case, replace $\star\underline{v}$ by the 2-form $\epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$ whose exterior derivative carries the 3D divergence.

---

# Solution

The 4D divergence theorem is Stokes' theorem applied to the flux 3-form $\star\underline{v}$, using the one identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$ that turns "$\mathrm{d}$ of the flux form" into "divergence times volume form". The plan: write the flux as a 3-form integral; apply Stokes; prove and insert the divergence identity; then mirror the argument in three dimensions.

**Step 1: Stokes converts the boundary flux to a four-volume integral.**

> [!note]- Derivation
> The flux of $\vec{v}$ through the closed boundary hypersurface $\partial\mathscr{V}$ is, by definition, $\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\partial\mathscr{V}}\star\underline{v}$. The integrand $\star\underline{v}$ is a 3-form on spacetime, i.e. a $(p-1)$-form with $p = 4$. Since $\mathscr{V}$ is a four-dimensional compact submanifold-with-boundary, [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] applies with $A = \star\underline{v}$:
> $$\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\mathrm{d}\star\underline{v} .$$
> The flux through the boundary has become the integral over the interior of the exterior derivative of the flux form. What remains is to interpret $\mathrm{d}\star\underline{v}$.

**Step 2: $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\,\epsilon$.**

> [!note]- Derivation
> The 3-form $\star\underline{v}$ has components $(\star\underline{v})_{\alpha\beta\gamma} = v^\mu\epsilon_{\mu\alpha\beta\gamma}$. Its exterior derivative is a 4-form, determined by its single component $(\mathrm{d}\star\underline{v})_{0123}$. The exterior derivative of a 3-form $B$ is $(\mathrm{d}B)_{\lambda\alpha\beta\gamma} = 4\,\partial_{[\lambda}B_{\alpha\beta\gamma]}$ (antisymmetrisation over all four indices). For the top component,
> $$(\mathrm{d}\star\underline{v})_{0123} = \partial_0(\star\underline{v})_{123} - \partial_1(\star\underline{v})_{023} + \partial_2(\star\underline{v})_{013} - \partial_3(\star\underline{v})_{012} .$$
> Now $(\star\underline{v})_{123} = v^\mu\epsilon_{\mu123} = v^0\epsilon_{0123} = v^0\sqrt{|g|}$, and similarly $(\star\underline{v})_{023} = v^1\epsilon_{1023} = -v^1\sqrt{|g|}$, $(\star\underline{v})_{013} = v^2\epsilon_{2013} = v^2\sqrt{|g|}$, $(\star\underline{v})_{012} = v^3\epsilon_{3012} = -v^3\sqrt{|g|}$ (tracking the sign of each Levi-Civita permutation). Substituting and combining the signs,
> $$(\mathrm{d}\star\underline{v})_{0123} = \partial_0(\sqrt{|g|}v^0) + \partial_1(\sqrt{|g|}v^1) + \partial_2(\sqrt{|g|}v^2) + \partial_3(\sqrt{|g|}v^3) = \partial_\mu(\sqrt{|g|}\,v^\mu) .$$
> The four-divergence in arbitrary coordinates is $\nabla\cdot\vec{v} = \frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\,v^\mu)$, so $\partial_\mu(\sqrt{|g|}v^\mu) = \sqrt{|g|}\,\nabla\cdot\vec{v} = (\nabla\cdot\vec{v})\,\epsilon_{0123}$. Both $\mathrm{d}\star\underline{v}$ and $(\nabla\cdot\vec{v})\epsilon$ are 4-forms agreeing in their single component, hence equal:
> $$\boxed{\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\,\epsilon.}$$
> The two appearances of $\sqrt{|g|}$ — one inside $\epsilon$, one inside the divergence formula — are exactly what conspire to make this clean.

**Step 3: The four-dimensional Gauss–Ostrogradsky theorem.**

> [!note]- Derivation
> Insert Step 2 into Step 1. Using $\int_{\mathscr{V}}f\,\epsilon = \int_{\mathscr{V}}f\,\mathrm{d}U$ (the integral of a 4-form),
> $$\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\mathscr{V}}\mathrm{d}\star\underline{v} = \int_{\mathscr{V}}(\nabla\cdot\vec{v})\,\epsilon = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U .$$
> This is the four-dimensional Gauss–Ostrogradsky theorem: the flux of $\vec{v}$ out through the closed boundary equals the integral of its four-divergence over the enclosed four-region. It is the statement that "net outflow = total source inside", in four dimensions.

**Step 4: The three-dimensional version and the metric-dependent step.**

> [!note]- Derivation
> For a three-dimensional region $\mathscr{V}\subset\Sigma$ in a spacelike slice ($t=0$) with $\vec{v}$ tangent to $\Sigma$, form the 2-form $A := \epsilon(\vec{e}_0, \vec{v}, \cdot, \cdot)$ (a $(p-1)$-form with $p=3$). One computes (as in [[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)|Lemmas 2–3]]) that $(\mathrm{d}A)_{123} = \partial_i v^i = \nabla\cdot\vec{v}$ (the 3D divergence) and that $A$ on the boundary surface is $\vec{v}\cdot\mathrm{d}\vec{S}$. Applying Stokes' theorem to $A$ on the three-region $\mathscr{V}$:
> $$\int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}V = \int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A = \oint_{\partial\mathscr{V}}\vec{v}\cdot\mathrm{d}\vec{S} ,$$
> the classical divergence theorem.
>
> *The metric-dependent step.* Stokes' theorem itself ($\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$) is metric-free. The metric enters in the *interpretation*: identifying $\mathrm{d}\star\underline{v}$ (or $\mathrm{d}A$) with the divergence uses $\nabla\cdot\vec{v} = \frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}v^\mu)$, which is metric-dependent; the volume element $\mathrm{d}U = \sqrt{|g|}\,\mathrm{d}^4x$ and the flux $\int\star\underline{v}$ both use the metric. So the Gauss–Ostrogradsky theorems are metric-dependent, *even though* the Stokes theorem they are derived from is not — the metric lives entirely in the translation between forms and the vector-calculus quantities (divergence, volume, flux).

> [!note]- Complete formal solution
> $\star\underline{v}$ is a 3-form, so Stokes gives $\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\mathrm{d}\star\underline{v}$. Computing the top component, $(\mathrm{d}\star\underline{v})_{0123} = \partial_\mu[(\star\underline{v})\text{-components}] = \partial_\mu(\sqrt{|g|}v^\mu) = \sqrt{|g|}\,\nabla\cdot\vec{v} = (\nabla\cdot\vec{v})\epsilon_{0123}$, so $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$. Hence $\Phi_{\partial\mathscr{V}}(\vec{v}) = \int_{\mathscr{V}}(\nabla\cdot\vec{v})\epsilon = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$ — the 4D Gauss theorem. For a 3D region in a slice, the 2-form $A=\epsilon(\vec{e}_0,\vec{v},\cdot,\cdot)$ has $(\mathrm{d}A)_{123}=\partial_i v^i$ and $A|_{\partial\mathscr{V}}=\vec{v}\cdot\mathrm{d}\vec{S}$, so Stokes gives $\int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}V=\oint_{\partial\mathscr{V}}\vec{v}\cdot\mathrm{d}\vec{S}$. Stokes is metric-free; the metric enters only in identifying $\mathrm{d}(\text{flux form})$ with the divergence and in the volume element and flux. $\blacksquare$

---

# Key Takeaways

**The divergence theorem is Stokes' theorem applied to the Hodge dual of the field — one line, one identity.** The entire content of the four-dimensional Gauss–Ostrogradsky theorem is: write the flux as $\int_{\partial\mathscr{V}}\star\underline{v}$, apply Stokes to get $\int_{\mathscr{V}}\mathrm{d}\star\underline{v}$, and use $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$. Recognising that the divergence theorem is *not a separate theorem* but a corollary of Stokes — the corollary obtained by feeding the flux form $\star\underline{v}$ — is the organising insight, and it generalises: in any dimension, the divergence theorem is Stokes for the Hodge dual of the vector field. The trigger is any "flux out of a closed boundary = integral of a divergence inside" statement; it is always Stokes plus the divergence identity. This unifies the three-dimensional divergence theorem of vector calculus, its four-dimensional spacetime generalisation, and the Riemannian divergence theorem on any manifold into a single derivation.

**The identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$ is where the two $\sqrt{|g|}$ factors meet.** The cleanest part of the derivation is also the most easily fumbled: the exterior derivative of $\star\underline{v}$ produces $\partial_\mu(\sqrt{|g|}v^\mu)$, with the $\sqrt{|g|}$ coming from the Levi-Civita component $\epsilon_{0123}$; the divergence formula $\nabla\cdot\vec{v} = \frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}v^\mu)$ contributes a *compensating* $\frac{1}{\sqrt{|g|}}$; and the two combine to give $(\nabla\cdot\vec{v})\epsilon_{0123}$. The transferable insight is that the curvilinear-coordinate form of the divergence — the one with the $\sqrt{|g|}$ inside the derivative — is not an arbitrary formula but is *forced* by the requirement that $\mathrm{d}\star\underline{v}$ be the divergence times the volume form. Whenever you see $\frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}v^\mu)$, recognise it as "the exterior derivative of the flux form, normalised by the volume form"; this is both why the formula has that shape and why it is coordinate-independent.

**Stokes is metric-free but its divergence-theorem corollary is not — the metric lives in the translation.** A subtle but important point: the master Stokes theorem relates two integrals of forms and never touches the metric, yet the Gauss–Ostrogradsky theorems derived from it are thoroughly metric-dependent. The resolution is that the metric enters not in Stokes itself but in *interpreting* the forms — the divergence ($\nabla\cdot\vec{v}$), the volume element ($\mathrm{d}U = \sqrt{|g|}\,\mathrm{d}^4x$), and the flux ($\int\star\underline{v}$) all use $g$. The diagnostic this provides is valuable: when you suspect a theorem is or is not metric-dependent, ask whether it is a statement purely about forms (then metric-free, like Stokes) or whether it mentions divergences, volumes, or fluxes (then metric-dependent, like Gauss). This distinction prevents the common error of assuming the corollary inherits the metric-independence of the parent, and it clarifies *why* the same Stokes theorem governs both the topological (cohomological) and the metric (divergence-theorem) applications.

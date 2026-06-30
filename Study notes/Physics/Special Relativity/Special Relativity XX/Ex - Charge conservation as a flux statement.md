---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Gauss-Ostrogradsky Theorem (3D and 4D)"
  - "Thm - Stokes Theorem on Spacetime"
  - "Def - Volume, Area, Length Elements and Flux Integrals"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$. Let $J$ be the electric four-current, $J^\mu = (\rho, \mathbf{j})$, with $\rho$ the charge density and $\mathbf{j}$ the three-current density. The total charge on a spacelike slice $\Sigma$ is the flux $Q_\Sigma = \int_\Sigma\star\underline{J}$.

1. Show that the local conservation law $\nabla\cdot J = 0$ (the continuity equation $\partial_\mu J^\mu = 0$, i.e. $\partial_t\rho + \nabla\cdot\mathbf{j} = 0$) is equivalent to the vanishing of the flux $\int_{\partial\mathscr{V}}\star\underline{J}$ through *every* closed hypersurface $\partial\mathscr{V}$.
2. Consider two spacelike slices $\Sigma_1$ (at $t = t_1$) and $\Sigma_2$ (at $t = t_2 > t_1$), and the four-region $\mathscr{V}$ between them, capped by a timelike tube $\mathscr{T}$ at large spatial radius. Assume the current vanishes at spatial infinity ($J\to 0$ as $r\to\infty$, fast enough). Apply the four-dimensional Gauss–Ostrogradsky theorem to show $Q_{\Sigma_2} = Q_{\Sigma_1}$.
3. Conclude that the total electric charge is **conserved** (the same at every time) *and* **slice-independent** (the same for every observer's notion of "now", including tilted/boosted slices).
4. Explain in what precise sense "$\nabla\cdot J = 0$ at every point" and "the total charge is the same on every slice" are the *same* statement.

**Recall:**

The four-dimensional Gauss–Ostrogradsky theorem and the flux are as follows.

![[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)#Statement]]

The flux of $\vec{v}$ through a hypersurface is $\Phi_{\mathscr{V}}(\vec{v}) = \int_{\mathscr{V}}\star\underline{v}$, and through a constant-time slice it equals $\int_\Sigma v^0\,\mathrm{d}^3x$ ([[Def - Volume, Area, Length Elements and Flux Integrals]]). The four-divergence is $\nabla\cdot J = \nabla_\mu J^\mu$, and $\mathrm{d}\star\underline{J} = (\nabla\cdot J)\,\epsilon$.

---

# Convergent Strategy

**Problem class.** The defining *conservation-law* problem of [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem#Problem-Solving Strategy|the chapter]]: given a vanishing four-divergence, prove a total quantity is conserved and slice-independent. This is the template every relativistic conservation law follows.

**Assumption pattern.** A conserved current ($\nabla\cdot J = 0$) and a four-region bounded by two spacelike slices plus a tube at infinity where the current dies. The signpost is the vanishing four-divergence, which is *precisely* the hypothesis that makes the right-hand side of the 4D Gauss theorem zero. The decaying-at-infinity assumption is what kills the tube contribution.

**Theorem routing.** Part 1 uses the 4D Gauss theorem $\int_{\partial\mathscr{V}}\star\underline{J} = \int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U$ in both directions (divergence vanishes $\Leftrightarrow$ all closed-surface fluxes vanish). Part 2 applies it to the specific slab, with the boundary $\partial\mathscr{V} = \Sigma_2 - \Sigma_1 + \mathscr{T}$ and the orientation making $\Sigma_1$ contribute with a flipped sign. Parts 3–4 interpret.

**Key decision point.** The crux is the *orientation bookkeeping* of the closed boundary: $\partial\mathscr{V}$ consists of the future slice $\Sigma_2$ (outward orientation = future), the past slice $\Sigma_1$ (outward orientation = past, i.e. *reversed* from its natural future orientation), and the tube $\mathscr{T}$. The net flux out is $Q_{\Sigma_2} - Q_{\Sigma_1} + (\text{tube})$, and the sign flip on $\Sigma_1$ is exactly what turns "net flux out = 0" into "$Q_{\Sigma_2} = Q_{\Sigma_1}$". Getting this sign wrong gives $Q_{\Sigma_2} + Q_{\Sigma_1} = 0$, which is nonsense.

---

# Legal Operations Used

1. **Operation 7 from the topic page (turn a vanishing divergence into a slice-independent charge).** This exercise *is* that operation, worked in full: the engine is the 4D Gauss theorem applied to the slab.

2. **Operation 4 from the topic page (express a flux as the integral of a Hodge dual).** The total charge is $Q_\Sigma = \int_\Sigma\star\underline{J}$, the flux of the current through the slice.

3. **Illegal-but-tempting operation 3 from the topic page (using the wrong induced orientation on the boundary).** Avoiding this is the crux: the past slice $\Sigma_1$ must carry the *reversed* (past-pointing outward) orientation, or the conservation statement comes out wrong.

---

# Hints

> [!note]- Hint 1
> By the 4D Gauss theorem, $\int_{\partial\mathscr{V}}\star\underline{J} = \int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U$ for *any* four-region $\mathscr{V}$. If $\nabla\cdot J = 0$ everywhere, the right side is $0$ for every $\mathscr{V}$, so the flux through every closed boundary vanishes. Conversely, if the flux vanishes for every $\mathscr{V}$, then $\int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U = 0$ for all $\mathscr{V}$, forcing $\nabla\cdot J = 0$ pointwise (a continuous function with vanishing integral over every region is zero).

> [!note]- Hint 2
> The boundary of the slab is $\partial\mathscr{V} = \Sigma_2 \cup \Sigma_1 \cup \mathscr{T}$. The outward normal on $\Sigma_2$ (the top) points to the future; on $\Sigma_1$ (the bottom) it points to the *past*. So the flux out through $\Sigma_1$ is $-Q_{\Sigma_1}$ (the charge with reversed orientation). The tube $\mathscr{T}$ contributes $\int_{\mathscr{T}}\star\underline{J}$, which involves the spatial current $\mathbf{j}$ at large radius.

> [!note]- Hint 3
> Since $\nabla\cdot J = 0$, the total flux out vanishes: $Q_{\Sigma_2} - Q_{\Sigma_1} + \Phi_{\mathscr{T}}(J) = 0$. As $J\to 0$ at spatial infinity (faster than $1/r^2$), the tube flux $\Phi_{\mathscr{T}}(J)\to 0$, leaving $Q_{\Sigma_2} = Q_{\Sigma_1}$.

> [!note]- Hint 4
> For part 4: "$\nabla\cdot J = 0$ pointwise" and "$Q$ is slice-independent" are related by the Gauss theorem, which says the integral of the divergence over the slab *equals* the difference of the slice charges. Zero divergence $\Leftrightarrow$ zero difference. They are the local and global faces of one fact.

---

# Solution

The local conservation law $\nabla\cdot J = 0$ and the global statement "total charge is the same on every slice" are the two faces of one fact, joined by the 4D Gauss theorem. The plan: show divergence-free $\Leftrightarrow$ all-closed-fluxes-vanish; apply this to a slab between two slices, watching the orientation flip on the past slice and the tube dying at infinity; conclude conservation and slice-independence; then articulate the equivalence.

**Step 1: $\nabla\cdot J = 0$ everywhere $\Leftrightarrow$ flux vanishes through every closed hypersurface.**

> [!note]- Derivation
> By the four-dimensional Gauss–Ostrogradsky theorem ([[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)]]), for any four-dimensional compact region $\mathscr{V}$ with closed boundary $\partial\mathscr{V}$,
> $$\int_{\partial\mathscr{V}}\star\underline{J} = \int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U .$$
> *($\Rightarrow$)* If $\nabla\cdot J = 0$ at every point, the right-hand side is $0$ for *every* region $\mathscr{V}$, so the flux $\int_{\partial\mathscr{V}}\star\underline{J}$ through every closed hypersurface vanishes.
>
> *($\Leftarrow$)* Conversely, if $\int_{\partial\mathscr{V}}\star\underline{J} = 0$ for every $\mathscr{V}$, then $\int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U = 0$ for every $\mathscr{V}$. A continuous function whose integral over *every* region vanishes must be identically zero (otherwise it would be nonzero on some small region, whose integral would not vanish). Hence $\nabla\cdot J = 0$ pointwise.
>
> The continuity equation $\partial_\mu J^\mu = \partial_t\rho + \nabla\cdot\mathbf{j} = 0$ — local conservation of charge — is therefore *equivalent* to the geometric statement that no net charge flows out of any closed surface in spacetime.

**Step 2: $Q_{\Sigma_2} = Q_{\Sigma_1}$ for the slab between two slices.**

> [!note]- Derivation
> Take the four-region $\mathscr{V}$ bounded below by the slice $\Sigma_1$ ($t = t_1$), above by $\Sigma_2$ ($t = t_2$), and on the side by a timelike tube $\mathscr{T}$ at large spatial radius $r = \mathcal{R}$. Its boundary is the closed hypersurface $\partial\mathscr{V} = \Sigma_2 \cup \Sigma_1 \cup \mathscr{T}$, oriented outward.
>
> The outward normal points *to the future* on the top slice $\Sigma_2$ and *to the past* on the bottom slice $\Sigma_1$. With the convention that the charge $Q_\Sigma = \int_\Sigma\star\underline{J}$ uses the future-pointing normal, the outward flux through $\Sigma_2$ is $+Q_{\Sigma_2}$ and the outward flux through $\Sigma_1$ is $-Q_{\Sigma_1}$ (the past-pointing outward orientation reverses the sign). The tube contributes $\Phi_{\mathscr{T}}(J) = \int_{\mathscr{T}}\star\underline{J}$. So the total outward flux is
> $$\int_{\partial\mathscr{V}}\star\underline{J} = Q_{\Sigma_2} - Q_{\Sigma_1} + \Phi_{\mathscr{T}}(J) .$$
> By the 4D Gauss theorem and $\nabla\cdot J = 0$, the left-hand side equals $\int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U = 0$:
> $$Q_{\Sigma_2} - Q_{\Sigma_1} + \Phi_{\mathscr{T}}(J) = 0 .$$
> The tube flux involves the *spatial* current $\mathbf{j}$ crossing the surface $r = \mathcal{R}$. For a localised charge distribution (or any current decaying faster than $1/r^2$ at spatial infinity), $\Phi_{\mathscr{T}}(J)\to 0$ as $\mathcal{R}\to\infty$ — no charge escapes to infinity. Taking the limit,
> $$Q_{\Sigma_2} = Q_{\Sigma_1} .$$

**Step 3: Conservation and slice-independence.**

> [!note]- Derivation
> Step 2 shows the total charge is the same on the two slices $\Sigma_1$ and $\Sigma_2$. Since these were arbitrary constant-time slices, the total charge is **the same at every time** — it is *conserved*. But the argument used nothing about the slices except that they are spacelike and bound the slab; it applies equally to *tilted* (boosted) spacelike slices, which are the "now"-slices of moving observers. So the total charge is also **the same for every observer's notion of simultaneity** — it is *slice-independent*, and in particular Lorentz-invariant (every inertial observer measures the same total charge). Conservation in time and agreement between observers are not two facts but one: the charge is the flux of $J$ through *any* spacelike slice, and that flux is independent of which slice, by the Gauss theorem applied to the region between any two.

**Step 4: The local and global statements are identical.**

> [!note]- Derivation
> The 4D Gauss theorem says the integral of the divergence over the slab *equals* the difference of the slice charges (plus the tube term, which vanishes):
> $$\int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U = Q_{\Sigma_2} - Q_{\Sigma_1} .$$
> So "$\nabla\cdot J = 0$ at every point of the slab" (the integrand vanishes) and "$Q_{\Sigma_2} = Q_{\Sigma_1}$" (the difference vanishes) are *logically equivalent* — the theorem is an equality between them. The local conservation law is the differential, pointwise form; the global conservation is the integral form; and they are connected not by a chain of physical reasoning but by a single mathematical identity. To say charge is locally conserved (it does not appear or disappear at any point, only flows) is *the same as* to say the total is constant in time and the same for all observers. This is the deepest content of the chapter, and it is the template for energy-momentum, baryon number, and every other conserved quantity in relativity.

> [!note]- Complete formal solution
> By the 4D Gauss theorem $\int_{\partial\mathscr{V}}\star\underline{J} = \int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U$ for every region $\mathscr{V}$, so $\nabla\cdot J = 0$ everywhere $\Leftrightarrow$ the flux vanishes through every closed hypersurface (the converse by "vanishing integral over every region $\Rightarrow$ vanishing integrand"). For the slab between $\Sigma_1$ and $\Sigma_2$ capped by a tube $\mathscr{T}$ at radius $\mathcal{R}$, the outward boundary flux is $Q_{\Sigma_2} - Q_{\Sigma_1} + \Phi_{\mathscr{T}}(J)$ (the past slice $\Sigma_1$ carrying reversed orientation). Setting this to $\int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U = 0$ and letting $\mathcal{R}\to\infty$ so $\Phi_{\mathscr{T}}(J)\to 0$ (localised current) gives $Q_{\Sigma_2}=Q_{\Sigma_1}$. As the slices were arbitrary spacelike surfaces, the total charge is conserved in time and the same for every observer's "now" — Lorentz-invariant. The local law $\nabla\cdot J=0$ and the global law "$Q$ slice-independent" are identical, joined by the Gauss-theorem equality $\int_{\mathscr{V}}\nabla\cdot J\,\mathrm{d}U = Q_{\Sigma_2}-Q_{\Sigma_1}$. $\blacksquare$

---

# Key Takeaways

**Local conservation and global conservation are one statement, joined by the Gauss theorem.** The single most important idea in the chapter is that "$\nabla\cdot J = 0$ at every point" and "total charge is conserved and slice-independent" are not two physical facts linked by reasoning but the *same* fact, because the 4D Gauss theorem is an equality between the integral of the divergence and the difference of the slice charges. The differential (pointwise) form and the integral (global) form of any conservation law are interchangeable, and which one you reach for is a matter of convenience: the differential form is local and good for field equations, the integral form is global and good for total quantities. The trigger is any conserved current $\nabla\cdot(\text{current}) = 0$; the move is to enclose a spacetime slab and apply Gauss, and the result is always "the total is the same on every slice". This template is reused verbatim for energy-momentum ($\nabla_\mu T^{\mu\nu} = 0$), baryon number, and probability, and recognising it turns every "prove this is conserved" problem into a routine application of one theorem.

**Conservation in time and agreement between observers are the same thing — the charge is a flux through any spacelike slice.** A subtle payoff of the geometric formulation is that "the charge does not change over time" and "all inertial observers measure the same total charge" are revealed to be a single statement, because both are instances of "the flux of $J$ through a spacelike slice is independent of which slice". A constant-time slice of one observer and a tilted slice of a boosted observer are both just spacelike hypersurfaces, and the Gauss theorem applied to the region between *any* two of them gives equality. So Lorentz invariance of total charge is not an extra assumption to be checked but an automatic consequence of local conservation — the same argument that gives time-independence gives observer-independence. The transferable insight is that whenever a conserved quantity is expressed as a flux through a Cauchy surface, its value is automatically slice-independent, hence frame-independent; this is why "total charge", "total energy-momentum", and "total baryon number" are well-defined invariants of an isolated system.

**The orientation flip on the past slice is what makes "in equals out" come out right.** The one place this argument can go wrong is the orientation of the closed boundary: the future slice $\Sigma_2$ and the past slice $\Sigma_1$ both bound the slab, but the *outward* normal points to the future on $\Sigma_2$ and to the *past* on $\Sigma_1$, so the past slice contributes $-Q_{\Sigma_1}$ to the outward flux. This sign flip is exactly what turns "net flux out = 0" into "$Q_{\Sigma_2} = Q_{\Sigma_1}$" rather than the nonsensical "$Q_{\Sigma_2} + Q_{\Sigma_1} = 0$". The diagnostic lesson is that the outward-normal-first convention of Stokes' theorem is not a formality but the load-bearing detail in every conservation argument, and the place to check first if a conserved quantity comes out with the wrong sign. The general pattern — future cap positive, past cap negative, side tube vanishing at infinity — recurs in every flux-conservation argument, and getting it right is the difference between a correct conservation law and a sign error masquerading as a paradox. This same slab construction, with the tube flux now possibly nonzero, is how one computes the *rate* of change of a charge when the current does *not* vanish at infinity — the boundary flux through the tube measures exactly the charge leaving the region.

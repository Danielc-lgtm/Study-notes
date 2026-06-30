---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Volume, Area, Length Elements and Flux Integrals"
  - "Def - The Hodge Star"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$.

1. Let $\Sigma$ be the constant-time hyperplane $t = 0$ in an inertial frame, with future-directed timelike unit normal $\vec{n} = \vec{e}_0$. For a vector field $\vec{v}$ with components $v^\mu = (v^0, \mathbf{v})$, compute the flux $\Phi_\Sigma(\vec{v}) = \int_\Sigma\star\underline{v}$ two ways — directly as $\pm\int_\Sigma\vec{v}\cdot\vec{n}\,\mathrm{d}V$, and by evaluating the 3-form $\star\underline{v}$ on the slice — and show both give (up to sign) $\int_\Sigma v^0\,\mathrm{d}^3x$.
2. Interpret the result: explain why the flux through a constant-time slice is the integral of the *time component* $v^0$, the "density" being transported.
3. Show that a vector field $\vec{v}$ that is everywhere *tangent* to $\Sigma$ (i.e. $v^0 = 0$) has zero flux through $\Sigma$, and explain physically why.
4. Apply this to the electric four-current $J^\mu = (\rho, \mathbf{j})$: identify the flux $\Phi_\Sigma(J)$ with the total electric charge $Q$ on the slice.

**Recall:**

The flux of a vector field through a hypersurface is defined as follows.

![[Def - Volume, Area, Length Elements and Flux Integrals#The Definition]]

The Hodge dual of a 1-form $\underline{v}$ (with $v_\mu = \eta_{\mu\nu}v^\nu$) is the 3-form $\star\underline{v}$ with components $(\star\underline{v})_{\alpha\beta\gamma} = v^\mu\epsilon_{\mu\alpha\beta\gamma}$. In the inertial frame $\epsilon_{0123} = 1$ and $\sqrt{|g|} = 1$. The metric dual lowers indices: $v_0 = v^0$, $v_i = -v^i$.

---

# Convergent Strategy

**Problem class.** A *compute-a-flux* problem, the second core class of [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem#Problem-Solving Strategy|the chapter]]. The routine is to recast the flux as the integral of the Hodge dual $\star\underline{v}$ and evaluate it on the slice, which reduces to the integral of one component.

**Assumption pattern.** A vector field and a constant-time slice with a specified unit normal. The signpost that the answer will be "$\int v^0$" is that the normal $\vec{n} = \vec{e}_0$ is purely temporal, so the inner product $\vec{v}\cdot\vec{n}$ picks out exactly the time component. The tangency condition $v^0 = 0$ in part 3 is the recognisable special case where the flux vanishes.

**Theorem routing.** Parts 1–2 use the flux definition $\Phi_\Sigma(\vec{v}) = \int_\Sigma\star\underline{v} = \pm\int_\Sigma\vec{v}\cdot\vec{n}\,\mathrm{d}V$ ([[Def - Volume, Area, Length Elements and Flux Integrals]]) and the component formula for the Hodge star. Part 3 uses the general fact that a tangent field has zero flux. Part 4 specialises to $\vec{v} = J$, where $v^0 = \rho$ is the charge density.

**Key decision point.** The instructive choice is to compute the flux *both* ways — elementary ($\vec{v}\cdot\vec{n}\,\mathrm{d}V$) and via the Hodge dual ($\int\star\underline{v}$) — and check they agree. The elementary way is faster, but the Hodge-dual way is the one that makes the flux Stokes-ready for the conservation arguments of §20.3, so seeing the two coincide is the point.

---

# Legal Operations Used

1. **Operation 4 from the topic page (express a flux as the integral of a Hodge dual).** The whole exercise is built on $\Phi_\Sigma(\vec{v}) = \int_\Sigma\star\underline{v}$; part 1 verifies it against the elementary form.

2. **Operation 3 from the topic page (build the submanifold's volume form from its normals).** The volume element $\mathrm{d}V = \star\underline{n}$ of the slice, with $\vec{n} = \vec{e}_0$, gives $\mathrm{d}V = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$, the measure against which $v^0$ is integrated.

3. **Operation 9 from the topic page (classify a hypersurface by its normal).** The slice is spacelike (timelike normal $\vec{e}_0$), which fixes the sign convention in $\Phi = \pm\int\vec{v}\cdot\vec{n}\,\mathrm{d}V$.

---

# Hints

> [!note]- Hint 1
> The inner product $\vec{v}\cdot\vec{n} = v^\mu n_\mu$. With $\vec{n} = \vec{e}_0$, $n^\mu = (1,0,0,0)$ and $n_\mu = \eta_{\mu\nu}n^\nu = (1,0,0,0)$, so $\vec{v}\cdot\vec{n} = v^0 n_0 = v^0$.

> [!note]- Hint 2
> For the Hodge-dual route, the slice $\Sigma$ has tangent vectors $\vec{e}_1, \vec{e}_2, \vec{e}_3$, and $\star\underline{v}$ evaluated on them is $(\star\underline{v})_{123} = v^\mu\epsilon_{\mu123} = v^0\epsilon_{0123} = v^0$. So $\int_\Sigma\star\underline{v} = \int v^0\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$.

> [!note]- Hint 3
> A vector tangent to $\Sigma$ has no time component, $v^0 = 0$, so both expressions for the flux vanish. Physically, a field that runs *along* the slice never crosses it.

> [!note]- Hint 4
> For the four-current $J^\mu = (\rho,\mathbf{j})$, the time component is $v^0 = J^0 = \rho$, the charge density. So $\Phi_\Sigma(J) = \pm\int_\Sigma\rho\,\mathrm{d}^3x = \pm Q$, the total charge on the slice (sign by orientation convention).

---

# Solution

The flux through a constant-time slice is, up to an orientation sign, the integral of the time component $v^0$ — the density of $\vec{v}$ crossing the instant. The plan: compute $\vec{v}\cdot\vec{n} = v^0$ for the elementary route; compute $(\star\underline{v})_{123} = v^0$ for the Hodge-dual route; check they agree; then read off the tangent-field and charge cases.

**Step 1: Both routes give $\Phi_\Sigma(\vec{v}) = -\int_\Sigma v^0\,\mathrm{d}^3x$.**

> [!note]- Derivation
> *Elementary route.* The slice $\Sigma$ ($t=0$) is spacelike with future timelike unit normal $\vec{n} = \vec{e}_0$, so the flux sign is $-$ (the $\vec{n}$-is-timelike case). The volume element is $\mathrm{d}V = n^0\sqrt{|g|}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3 = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ (since $n^0 = 1$, $\sqrt{|g|}=1$). The inner product is $\vec{v}\cdot\vec{n} = v^\mu n_\mu$; with $n_\mu = \eta_{\mu\nu}n^\nu = (1,0,0,0)$, this is $\vec{v}\cdot\vec{n} = v^0$. Hence
> $$\Phi_\Sigma(\vec{v}) = -\int_\Sigma \vec{v}\cdot\vec{n}\,\mathrm{d}V = -\int_\Sigma v^0\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z .$$
>
> *Hodge-dual route.* The 3-form $\star\underline{v}$ has components $(\star\underline{v})_{\alpha\beta\gamma} = v^\mu\epsilon_{\mu\alpha\beta\gamma}$. Integrating over the slice $\Sigma$ (adapted coordinates $x^1,x^2,x^3$) uses the component $(\star\underline{v})_{123} = v^\mu\epsilon_{\mu123} = v^0\epsilon_{0123} = v^0$ (only $\mu=0$ survives). So
> $$\int_\Sigma\star\underline{v} = \int_\Sigma (\star\underline{v})_{123}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3 = \int_\Sigma v^0\,\mathrm{d}^3x .$$
> The two routes agree up to the overall sign, which is the orientation convention; with the boundary orientation that makes the conservation argument come out "charge in minus charge out", the flux is $\Phi_\Sigma(\vec{v}) = \int_\Sigma v^0\,\mathrm{d}^3x$. The elementary "$\vec{v}\cdot\vec{n}\,\mathrm{d}V$" and the geometric "$\int\star\underline{v}$" compute the same number.

**Step 2: The flux is the integral of the transported density.**

> [!note]- Derivation
> The time component $v^0$ is the *density* associated with the vector field $\vec{v}$: in $\vec{v} = (v^0, \mathbf{v})$, the spatial part $\mathbf{v}$ is the spatial flux density (how much flows per area per time) and the time part $v^0$ is the amount per volume present at the instant. The flux through the slice $t=0$ counts the total amount "present now", which is $\int_\Sigma v^0\,\mathrm{d}^3x$. This is why a flux through a *spacelike* slice (an instant) integrates the time component, whereas a flux through a *timelike* wall would integrate a spatial component — the slice's normal selects which component is the "crossing" one.

**Step 3: A tangent field has zero flux.**

> [!note]- Derivation
> If $\vec{v}$ is everywhere tangent to $\Sigma$, then by the normal-tangent criterion $\vec{v}\cdot\vec{n} = 0$; equivalently $v^0 = 0$ since the only normal direction is $\vec{e}_0$. Either expression for the flux then vanishes: $\Phi_\Sigma(\vec{v}) = -\int 0\,\mathrm{d}V = 0$, or $(\star\underline{v})_{123} = v^0 = 0$. Physically, a vector field that lies entirely within the slice "runs along" it and never crosses it, so nothing fluxes through — flux measures only the component piercing the surface, and a tangent field has none.

**Step 4: For the four-current, the flux is the total charge.**

> [!note]- Derivation
> The electric four-current is $J^\mu = (\rho, \mathbf{j})$, with $\rho$ the charge density and $\mathbf{j}$ the spatial current density. Its time component is $J^0 = \rho$, so by Step 1,
> $$\Phi_\Sigma(J) = \int_\Sigma J^0\,\mathrm{d}^3x = \int_\Sigma\rho\,\mathrm{d}^3x = Q,$$
> the total electric charge on the slice $\Sigma$. The flux of the four-current through an instant *is* the total charge present at that instant — which is exactly the quantity whose slice-independence (conservation) the 4D Gauss theorem will establish in [[Ex - Charge conservation as a flux statement]].

> [!note]- Complete formal solution
> For the slice $\Sigma$ ($t=0$) with future timelike unit normal $\vec{n}=\vec{e}_0$ (spacelike hypersurface, flux sign $-$): the volume element is $\mathrm{d}V = n^0\sqrt{|g|}\,\mathrm{d}^3x = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$, the inner product is $\vec{v}\cdot\vec{n}=v^\mu n_\mu = v^0$ (since $n_\mu=(1,0,0,0)$), so $\Phi_\Sigma(\vec{v}) = -\int_\Sigma v^0\,\mathrm{d}^3x$. Equivalently $\int_\Sigma\star\underline{v}$ uses $(\star\underline{v})_{123}=v^\mu\epsilon_{\mu123}=v^0$, giving $\int_\Sigma v^0\,\mathrm{d}^3x$ — the same up to the orientation sign. The flux is the integral of the transported density $v^0$. A tangent field has $v^0=0$, hence zero flux. For $J^\mu=(\rho,\mathbf{j})$, $v^0=\rho$ and $\Phi_\Sigma(J)=\int_\Sigma\rho\,\mathrm{d}^3x=Q$, the total charge. $\blacksquare$

---

# Key Takeaways

**The flux through a spacelike slice is the integral of the time component — the density crossing the instant.** When the slice is "space at an instant", its unit normal is timelike (the observer's four-velocity), and the inner product $\vec{v}\cdot\vec{n}$ picks out the time component $v^0$. So the flux is $\int v^0\,\mathrm{d}^3x$, which is the *total amount* of whatever $\vec{v}$ describes present at that instant: total charge for the current, total energy for the energy flux, total probability for the probability current. The trigger to recognise this is any flux through a constant-time surface — the answer is always the integral of the conserved density. This is the bridge between the four-dimensional language ("flux of a four-vector through a hypersurface") and the everyday three-dimensional one ("total charge in space"), and seeing them as the same quantity is the conceptual payoff.

**Recasting a flux as $\int\star\underline{v}$ costs nothing and makes it Stokes-ready.** The elementary formula $\pm\int\vec{v}\cdot\vec{n}\,\mathrm{d}V$ and the geometric formula $\int\star\underline{v}$ compute the same number, as Step 1 verifies, so there is no penalty for using the Hodge-dual form — and there is a large reward. The 3-form $\star\underline{v}$ is exactly what Stokes' theorem consumes, so writing the flux this way means a single application of $\mathrm{d}$ converts it to a volume integral of the divergence, which is the entire mechanism of the conservation laws in §20.3. The trigger is: whenever you compute a flux that is "really about" a conservation law (and almost all are), write it as $\int\star\underline{v}$ from the start. The elementary form is for getting a number; the Hodge-dual form is for proving a theorem.

**A tangent field has zero flux — flux sees only the crossing component.** That a field lying entirely within a surface contributes no flux through it is obvious once stated but is a constant sanity check: it confirms the flux measures the *normal* (piercing) component and nothing else. The diagnostic use is in spotting errors — if a computation assigns nonzero flux to a manifestly tangent field, a sign or projection has gone wrong. More broadly, the decomposition $\vec{v} = v^0\vec{n} + (\text{tangent part})$ shows that only the normal piece matters for flux, which is why the flux of $\vec{v}$ equals the flux of its normal projection, and why "flux of the unit normal through a slice = volume of the slice" (the corollary in [[Def - Volume, Area, Length Elements and Flux Integrals]]). Recognising that flux annihilates tangent fields lets you discard the tangential part of any field before computing, often simplifying the work.

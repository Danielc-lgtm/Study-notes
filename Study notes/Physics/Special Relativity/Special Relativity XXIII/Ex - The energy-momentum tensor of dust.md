---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Energy-Momentum Tensor"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Thm - Energy-Momentum Conservation"
tags: [physics, special-relativity]
---

# Problem Statement

Consider **pressureless dust**: a cloud of non-interacting particles which, in a small neighbourhood of each event, all share a common four-velocity field $U$ and have proper energy density $\varepsilon_0$ (energy per unit volume measured in the local rest frame). Working with $c = 1$ and the mostly-minus signature:

1. Write down the energy-momentum tensor $T^{\mu\nu}$ of the dust as a tensor built from $U$ and $\varepsilon_0$, and verify by contraction with an arbitrary observer's four-velocity $U_0$ that the energy density it predicts is $T(U_0,U_0)$.
2. Show that in a frame where the dust moves at speed $v$ along the $x$-axis, the energy density is $T^{00} = \gamma^2\varepsilon_0$, and interpret the two factors of $\gamma$.
3. Compute the momentum density $T^{0i}$ and the stress $T^{ij}$ in that frame, and confirm there is no pressure (no rest-frame stress).
4. Show that the conservation law $\nabla_\mu T^{\mu\nu} = 0$ for dust splits into the continuity equation $\nabla_\mu(\varepsilon_0 U^\mu) = 0$ (rest-energy conservation) and the geodesic equation $U^\mu\nabla_\mu U^\nu = 0$ (free fall), and explain why both must hold.

**Recall:**

The exercise rests on the definition of the energy-momentum tensor and its conservation.

![[Def - The Energy-Momentum Tensor#The Definition]]

A [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$ satisfies $U\cdot U = 1$ (with $c=1$); in a frame where the matter moves with three-velocity $\mathbf v$, $U^\mu = \gamma(1, \mathbf v)$ with $\gamma = (1-v^2)^{-1/2}$. The energy density measured by an observer of four-velocity $U_0$ is $\varepsilon = T(U_0, U_0)$, and [[Thm - Energy-Momentum Conservation|conservation]] is $\nabla_\mu T^{\mu\nu} = 0$.

---

# Convergent Strategy

**Problem class.** A *compute-and-verify-a-tensor* problem, the chapter's basic literacy. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] says: write down $T^{\mu\nu}$, contract with the observer to extract measured quantities, then take the divergence for the conservation content.

**Assumption pattern.** "Pressureless" and "common four-velocity field" are the signposts. Pressureless means no stress in the rest frame, so the rest-frame tensor is $\mathrm{diag}(\varepsilon_0, 0, 0, 0)$ — pure energy density. A common four-velocity means a single $U$ at each point, so the covariant form must be quadratic in $U$.

**Theorem routing.** Part 1: build the covariant tensor whose rest-frame form is $\mathrm{diag}(\varepsilon_0,0,0,0)$, which forces $T^{\mu\nu} = \varepsilon_0 U^\mu U^\nu$ ([[Def - The Energy-Momentum Tensor]]); verify by contraction. Parts 2–3: substitute $U^\mu = \gamma(1,\mathbf v)$. Part 4: expand $\nabla_\mu(\varepsilon_0 U^\mu U^\nu) = 0$ using the Leibniz rule and project along and orthogonal to $U$ ([[Thm - Energy-Momentum Conservation]]).

**Key decision point.** The crux of Part 4 is recognising that the single conservation law $\nabla_\mu(\varepsilon_0 U^\mu U^\nu) = 0$ contains *two* independent physical statements, separated by projecting onto $U$ (giving rest-energy conservation) and orthogonal to $U$ (giving free fall). Projecting is the non-obvious move; without it the two laws stay entangled.

---

# Legal Operations Used

1. **Build the dust tensor from the four-velocity field** (operation 2 from the topic page): the rest-frame form $\mathrm{diag}(\varepsilon_0,0,0,0)$ has the unique covariant extension $\varepsilon_0 U^\mu U^\nu$.

2. **Read off measured quantities by contracting $T$** (operation 1): the energy density is $T(U_0,U_0) = \varepsilon_0(U\cdot U_0)^2$, which is $\gamma^2\varepsilon_0$ for an observer moving at relative speed $v$.

3. **Take the divergence and project along and orthogonal to $U$** (operations 3 and 4): $\nabla_\mu(\varepsilon_0 U^\mu U^\nu) = 0$ split by projection into rest-energy conservation and the geodesic equation.

---

# Hints

> [!note]- Hint 1
> A pressureless, momentum-free medium has, in its rest frame, only an energy density: $T^{\mu\nu}_{\text{rest}} = \mathrm{diag}(\varepsilon_0, 0, 0, 0)$. What covariant object, built from $U^\mu = (1,0,0,0)$ in the rest frame, reproduces this? The only quadratic-in-$U$ tensor is $\varepsilon_0 U^\mu U^\nu$, and in the rest frame $U^0 U^0 = 1$, all else zero — it matches.

> [!note]- Hint 2
> For an observer of four-velocity $U_0$, the energy density is $T(U_0, U_0) = \varepsilon_0(U\cdot U_0)^2$. The contraction $U\cdot U_0$ is the relative Lorentz factor $\gamma$ (this is the standard result that $U\cdot U_0 = \gamma$ for two four-velocities at relative speed $v$). So $\varepsilon = \gamma^2\varepsilon_0$.

> [!note]- Hint 3
> The two factors of $\gamma$ are physically distinct: one comes from each particle's *energy* being $\gamma m$ instead of $m$, and the other from the volume being Lorentz-*contracted* by $\gamma$, so the same particles occupy a smaller volume and the density rises. Energy per particle up by $\gamma$, number per volume up by $\gamma$, energy density up by $\gamma^2$.

> [!note]- Hint 4
> Expand $\nabla_\mu(\varepsilon_0 U^\mu U^\nu) = U^\nu\nabla_\mu(\varepsilon_0 U^\mu) + \varepsilon_0 U^\mu\nabla_\mu U^\nu = 0$. Contract this $1$-form equation (in $\nu$) with $U_\nu$: using $U\cdot U = 1$ (so $U_\nu\nabla_\mu U^\nu = 0$), only the first term survives, giving $\nabla_\mu(\varepsilon_0 U^\mu) = 0$. Substituting back leaves $\varepsilon_0 U^\mu\nabla_\mu U^\nu = 0$, the geodesic equation.

---

# Solution

The dust tensor is $T^{\mu\nu} = \varepsilon_0 U^\mu U^\nu$, the rank-one symmetric tensor built from the flow. Contracting with an observer gives energy density $\gamma^2\varepsilon_0$ (one $\gamma$ for energy, one for contracted volume), no rest-frame stress, and the conservation law splits — by projecting along and orthogonal to $U$ — into rest-energy conservation and free-fall geodesic motion.

**Step 1: The dust tensor is $T^{\mu\nu} = \varepsilon_0 U^\mu U^\nu$, with $T(U_0,U_0) = \varepsilon_0(U\cdot U_0)^2$.**

> [!note]- Derivation
> In the local rest frame of the dust, $U^\mu = (1,0,0,0)$, there is no momentum and no stress (the particles are at rest and non-interacting), so the only nonzero component of the energy-momentum tensor is the energy density: $T^{\mu\nu}_{\text{rest}} = \mathrm{diag}(\varepsilon_0, 0, 0, 0)$. We seek a covariant tensor reproducing this. The candidate $\varepsilon_0 U^\mu U^\nu$ has rest-frame components $\varepsilon_0 U^\mu U^\nu = \varepsilon_0\,\mathrm{diag}(1,0,0,0)$ — exactly the required form — and being built from the tensor $U^\mu U^\nu$ it transforms correctly under Lorentz changes of frame. Hence
> $$T^{\mu\nu} = \varepsilon_0\, U^\mu U^\nu, \qquad T = \varepsilon_0\, U^\flat\otimes U^\flat.$$
> It is manifestly symmetric. Contracting both slots with an observer's four-velocity $U_0$,
> $$T(U_0, U_0) = \varepsilon_0\,(U\cdot U_0)(U\cdot U_0) = \varepsilon_0\,(U\cdot U_0)^2,$$
> which is the energy density that observer measures, confirming the structure of [[Def - The Energy-Momentum Tensor]].

**Step 2: In a frame where the dust moves at speed $v$, $T^{00} = \gamma^2\varepsilon_0$.**

> [!note]- Derivation
> In a frame where the dust moves at three-velocity $\mathbf v$ (speed $v$ along $x$), the four-velocity is $U^\mu = \gamma(1, v, 0, 0)$ with $\gamma = (1-v^2)^{-1/2}$. Then
> $$T^{00} = \varepsilon_0 (U^0)^2 = \varepsilon_0\gamma^2.$$
> Equivalently, the observer at rest in this frame has $U_0 = (1,0,0,0)$, so $U\cdot U_0 = \gamma\cdot1 - 0 = \gamma$ and $T(U_0,U_0) = \varepsilon_0\gamma^2$ — the same result by the contraction recipe.
>
> **Interpretation.** The two factors of $\gamma$ have separate physical origins. First, each dust particle's energy is $\gamma m$ rather than its rest energy $m$ — the relativistic energy increase, one factor of $\gamma$. Second, the volume containing a fixed set of particles is Lorentz-contracted along the direction of motion by a factor $\gamma$, so the *number* of particles per unit volume rises by $\gamma$ — the second factor. Energy per particle ($\times\gamma$) times number density ($\times\gamma$) gives energy density $\times\gamma^2$. This is why a relativistic flow is energetically much "heavier" than its rest-frame density suggests.

**Step 3: The momentum density and stress.**

> [!note]- Derivation
> With $U^\mu = \gamma(1, v, 0, 0)$,
> $$T^{0i} = \varepsilon_0 U^0 U^i = \varepsilon_0\gamma^2 v\,\delta^i_x, \qquad T^{ij} = \varepsilon_0 U^i U^j = \varepsilon_0\gamma^2 v^2\,\delta^i_x\delta^j_x.$$
> So the momentum density is $\varepsilon_0\gamma^2 v$ along $x$ (the energy density times the velocity — energy flowing at speed $v$ carries momentum), and the only nonzero stress component is $T^{xx} = \varepsilon_0\gamma^2 v^2$, which is *not* a pressure: it is the *ram* (momentum flux) of the moving stream, the rate at which $x$-momentum is carried across a surface by the bulk motion, not an isotropic internal pressure. In the rest frame ($v = 0$) all of $T^{0i}$ and $T^{ij}$ vanish: dust has *no pressure*. The appearance of $T^{xx} \ne 0$ in a moving frame is pure bulk transport, the hallmark distinguishing dust ($p = 0$) from a fluid ($p \ne 0$, with isotropic $T^{ii}$ even at rest).

**Step 4: Conservation splits into rest-energy conservation and the geodesic equation.**

> [!note]- Derivation
> Apply $\nabla_\mu T^{\mu\nu} = 0$ with $T^{\mu\nu} = \varepsilon_0 U^\mu U^\nu$, using the Leibniz rule:
> $$\nabla_\mu(\varepsilon_0 U^\mu U^\nu) = U^\nu\,\nabla_\mu(\varepsilon_0 U^\mu) + \varepsilon_0 U^\mu\,\nabla_\mu U^\nu = 0. \tag{$\ast$}$$
> This is a $1$-form equation (free index $\nu$). To disentangle it, project onto $U$ by contracting with $U_\nu$. Using $U_\nu U^\nu = 1$ and the key identity $U_\nu\nabla_\mu U^\nu = \tfrac12\nabla_\mu(U\cdot U) = \tfrac12\nabla_\mu(1) = 0$ (the four-velocity has constant unit norm, so its derivative is orthogonal to it):
> $$U_\nu\,U^\nu\,\nabla_\mu(\varepsilon_0 U^\mu) + \varepsilon_0 U^\mu\underbrace{U_\nu\nabla_\mu U^\nu}_{0} = 0 \;\Longrightarrow\; \nabla_\mu(\varepsilon_0 U^\mu) = 0.$$
> This is the **continuity equation** for the rest energy: the proper energy density flows without sources, i.e. the rest energy (equivalently rest mass, for dust) is conserved. Substituting this back into $(\ast)$ kills the first term, leaving
> $$\varepsilon_0\,U^\mu\nabla_\mu U^\nu = 0 \;\Longrightarrow\; U^\mu\nabla_\mu U^\nu = 0,$$
> the **geodesic equation**: the dust particles are in free fall, moving on straight worldlines (zero four-acceleration). Both laws must hold: the first because particles are neither created nor destroyed, the second because non-interacting particles feel no force. The single tensor conservation law encodes exactly these two facts, separated by the projection along and orthogonal to the flow.

> [!note]- Complete formal solution
> The energy-momentum tensor of pressureless dust is $T^{\mu\nu} = \varepsilon_0 U^\mu U^\nu$, the unique symmetric tensor whose local-rest-frame form is $\mathrm{diag}(\varepsilon_0,0,0,0)$. For an observer $U_0$ the energy density is $T(U_0,U_0) = \varepsilon_0(U\cdot U_0)^2$; in a frame where the dust moves at speed $v$, $U\cdot U_0 = \gamma$, so $T^{00} = \gamma^2\varepsilon_0$ — one factor of $\gamma$ from each particle's relativistic energy $\gamma m$, one from the Lorentz contraction of the volume. The momentum density is $T^{0i} = \varepsilon_0\gamma^2 v\,\delta^i_x$ (energy density times velocity) and the stress $T^{ij} = \varepsilon_0\gamma^2 v^2\delta^i_x\delta^j_x$ is pure bulk ram, vanishing in the rest frame — dust has no pressure. Conservation $\nabla_\mu T^{\mu\nu} = U^\nu\nabla_\mu(\varepsilon_0 U^\mu) + \varepsilon_0 U^\mu\nabla_\mu U^\nu = 0$, contracted with $U_\nu$ (using $U\cdot U = 1$, $U_\nu\nabla_\mu U^\nu = 0$), gives the continuity equation $\nabla_\mu(\varepsilon_0 U^\mu) = 0$ (rest-energy conservation); the remainder gives the geodesic equation $U^\mu\nabla_\mu U^\nu = 0$ (free fall). $\blacksquare$

---

# Key Takeaways

**The dust tensor $\varepsilon_0 U^\mu U^\nu$ is the simplest non-vacuum $T$, and it is rank one — the prototype of "degenerate energy-momentum tensor".** The construction is the model for every matter tensor: write the simplest object in the rest frame (here pure energy density, $\mathrm{diag}(\varepsilon_0,0,0,0)$) and find its covariant extension (here $\varepsilon_0 U^\mu U^\nu$). The trigger for this approach is any continuous medium with a flow field: ask what its tensor looks like in the rest frame, where the physics is simplest, then promote to covariant form using $U^\mu$. The rank-one degeneracy — $\varepsilon_0 U^\mu U^\nu$ annihilates every vector orthogonal to $U$ — is the concrete reminder, drilled by the topic page's first illegal operation, that the energy-momentum tensor is *not* a metric: it can be degenerate, it can vanish, and you must never invert it. Adding an isotropic pressure term $-p\,\eta^{\mu\nu}$ promotes dust to a perfect fluid and restores full rank.

**Energy density carries two factors of $\gamma$ under a boost, and recognising *why* prevents a whole class of errors.** When a medium moves, its energy density is not boosted by one factor of $\gamma$ (as a naive "energy goes up by $\gamma$" would suggest) but by $\gamma^2$, because *both* the energy per particle *and* the number density rise by $\gamma$ — the latter from Lorentz contraction of the volume. The trigger is any computation of how a density transforms: densities are *per unit volume*, and volumes contract, so a density always picks up an extra $\gamma$ beyond whatever its numerator does. This same $\gamma^2$ appears in the boosted charge density, the boosted number flux, and the transformation of the electromagnetic field energy density, and forgetting the volume-contraction factor is one of the most common slips in relativistic continuum problems. The diagnostic: whenever you boost a "density of something", count one $\gamma$ for the thing and one for the volume.

**One tensor conservation law is several physical laws, separated by projection — this is the master technique for $\nabla_\mu T^{\mu\nu} = 0$.** The single equation $\nabla_\mu(\varepsilon_0 U^\mu U^\nu) = 0$ contains both rest-energy conservation and the geodesic equation, and the move that separates them is projecting the $1$-form equation along $U$ (giving the scalar continuity equation) and orthogonal to $U$ (giving the vector equation of motion). This projection technique is completely general and is the engine of the whole subject: for a perfect fluid it gives the energy/entropy equation (parallel) and the relativistic Euler equation (orthogonal); for the electromagnetic field it gives Poynting's theorem (parallel) and the momentum-balance law (orthogonal). The trigger is any tensor conservation law from which you want recognisable scalar or vector balance laws: contract with $U_\nu$ for the energy/entropy content, project with $\perp_U$ for the momentum content. The reusable insight is that $\nabla_\mu T^{\mu\nu} = 0$ is never *one* law — it is energy plus momentum, and the projection chooses which you read.

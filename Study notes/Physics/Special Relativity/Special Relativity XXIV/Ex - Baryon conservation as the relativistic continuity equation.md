---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Baryon Four-Current and Its Conservation"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

1. Starting from the local baryon-conservation law $\nabla_\mu(n u^\mu) = 0$, decompose relative to an inertial observer $\mathcal{O}$ (using $u = \Gamma(u_0 + \mathbf{V})$, observed density $N = \Gamma n$) and derive the continuity equation $\partial_t N + \nabla\cdot(N\mathbf{V}) = 0$. Note that it has the same form as the nonrelativistic continuity equation, with no extra factor of $\Gamma$ or $c^{-1}$.
2. Establish the companion identity $\nabla_\mu u^\mu = \frac{1}{V}\frac{dV}{d\tau}$, interpreting the four-divergence of the four-velocity as the fractional expansion rate of a comoving volume element.
3. Combine the two to show the baryon number $\mathcal{N} = nV$ in a comoving volume is constant: $\frac{d(nV)}{d\tau} = 0$.

**Recall:**

![[Def - Baryon Four-Current and Its Conservation#The Definition]]

The fluid four-velocity is $u$, $u\cdot u = 1$; an inertial observer has four-velocity $u_0$, and $\Gamma = u\cdot u_0$ is the fluid Lorentz factor, with $u = \Gamma(u_0 + \mathbf{V})$ and $\mathbf{V}$ the fluid three-velocity. The observed baryon density is $N = \Gamma n$ (see [[Def - Baryon Four-Current and Its Conservation]]).

---

# Convergent Strategy

**Problem class.** A *decompose-a-covariant-law-relative-to-an-observer* problem, together with a geometric identity. Per the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]], a conserved current $\nabla_\mu J^\mu = 0$ becomes a continuity equation when written in an observer's coordinates.

**Assumption pattern.** The covariant conservation law $\nabla_\mu(nu^\mu) = 0$ plus the decomposition $u = \Gamma(u_0 + \mathbf{V})$ are the inputs. The signpost is "continuity equation" or "conservation of number/mass" — write the four-divergence in $3+1$ form.

**Theorem routing.** Part 1 substitutes $nu^\mu = N(u_0 + \mathbf{V})^\mu$ (with $N = \Gamma n$) into $\nabla_\mu(nu^\mu) = 0$ and reads off the time and space parts. Part 2 transports a comoving volume and uses the geometric meaning of the divergence (see [[Def - Baryon Four-Current and Its Conservation]]). Part 3 combines.

**Key decision point.** The instructive observation is that the relativistic continuity equation has *no* relativistic correction factor — it is identical in form to the Newtonian one. The reason is that the relativistic enhancement of the density ($N = \Gamma n$) and the relativistic flux conspire so that the conservation law remains classical. The natural expectation of a stray $\Gamma$ or $c$ is wrong; the kinematics of number conservation is "Newtonian".

---

# Legal Operations Used

1. **Invoke baryon-number conservation** (operation 6 from the topic page): the starting law $\nabla_\mu(nu^\mu) = 0$.

2. **Take the nonrelativistic-form decomposition relative to an observer** (related to operation 4): write the four-divergence in $3+1$ coordinates with $N = \Gamma n$.

3. **Use the volume-expansion identity** (operation 6, companion): $\nabla_\mu u^\mu = \dot V/V$ relates the four-divergence to comoving volume change.

---

# Hints

> [!note]- Hint 1
> Write $j_{\mathrm b}^\mu = nu^\mu = \Gamma n(u_0 + \mathbf{V})^\mu = N(u_0 + \mathbf{V})^\mu$ with $N = \Gamma n$. In $\mathcal{O}$'s coordinates $u_0 = (1, \mathbf{0})$, so $j_{\mathrm b}^0 = N$, $j_{\mathrm b}^i = N V^i$. The conservation $\partial_\mu j_{\mathrm b}^\mu = 0$ reads $\partial_t N + \partial_i(NV^i) = 0$.

> [!note]- Hint 2
> Transport a small 3-volume $V$ with the fluid (its boundary worldlines are fluid lines). The four-dimensional Gauss theorem applied to $u$ over the slab between $\tau$ and $\tau + d\tau$ gives $\int\nabla_\mu u^\mu\,d^4x = V(\tau+d\tau) - V(\tau)$, so $\nabla_\mu u^\mu = \dot V/V$ (with $c = 1$).

> [!note]- Hint 3
> $\nabla_\mu(nu^\mu) = u^\mu\nabla_\mu n + n\nabla_\mu u^\mu = \dot n + n\dot V/V = 0$, so $\dot n/n = -\dot V/V$, i.e. $\dot n V + n\dot V = d(nV)/d\tau = 0$.

---

# Solution

The covariant baryon-conservation law becomes, in an observer's frame, the ordinary continuity equation with no relativistic correction; combined with the identification of the four-divergence as the comoving expansion rate, it says the baryon count in a comoving volume is constant.

**Step 1: The continuity equation.**

> [!note]- Derivation
> Decompose the baryon four-current relative to $\mathcal{O}$: with $u = \Gamma(u_0 + \mathbf{V})$ and the observed density $N = \Gamma n$,
> $$j_{\mathrm b}^\mu = n u^\mu = \Gamma n\,(u_0 + \mathbf{V})^\mu = N\,(u_0 + \mathbf{V})^\mu.$$
> In $\mathcal{O}$'s inertial coordinates $u_0 = (1, \mathbf{0})$ and $\mathbf{V} = (0, V^i)$, so $j_{\mathrm b}^0 = N$ and $j_{\mathrm b}^i = N V^i$. The conservation law $\nabla_\mu j_{\mathrm b}^\mu = \partial_\mu j_{\mathrm b}^\mu = 0$ (Christoffel symbols vanish in inertial coordinates) is
> $$\frac{\partial N}{\partial t} + \frac{\partial}{\partial x^i}(N V^i) = 0, \qquad\text{i.e.}\qquad \frac{\partial N}{\partial t} + \nabla\cdot(N\mathbf{V}) = 0.$$
> This is the **continuity equation**, identical in form to the nonrelativistic one — *no* factor of $\Gamma$ or $c^{-1}$ appears. The relativistic content is hidden in $N = \Gamma n$ (the observed density is the proper density enhanced by length contraction), but the conservation law itself is classical in form.

**Step 2: The four-divergence is the comoving expansion rate.**

> [!note]- Derivation
> Consider a small three-dimensional volume $V$ transported by the fluid: the worldlines of its boundary are fluid lines, tangent to $u$. Over an infinitesimal proper-time step $d\tau$, the volume sweeps a four-dimensional slab. Applying the four-dimensional Gauss–Ostrogradsky theorem to the four-velocity $u$ over this slab, the flux through the top ($\tau + d\tau$) and bottom ($\tau$) faces gives $V(\tau+d\tau) - V(\tau)$ (the side walls are tangent to $u$ and contribute no flux), while the volume integral is $\nabla_\mu u^\mu\cdot V\,d\tau$. Equating,
> $$\nabla_\mu u^\mu\;V\,d\tau = dV \quad\Longrightarrow\quad \nabla_\mu u^\mu = \frac{1}{V}\frac{dV}{d\tau}.$$
> The four-divergence of the four-velocity is the **fractional rate of expansion** of a comoving volume element — positive where the fluid spreads, negative where it compresses. (Cosmologically, this is the Hubble expansion: $\nabla_\mu u^\mu = 3\dot a/a$.)

**Step 3: The comoving baryon count is constant.**

> [!note]- Derivation
> Expand the conservation law along the flow:
> $$\nabla_\mu(nu^\mu) = u^\mu\nabla_\mu n + n\nabla_\mu u^\mu = \dot n + n\frac{\dot V}{V} = 0,$$
> using Step 2 (here $\dot{} = d/d\tau = u^\mu\nabla_\mu$). Multiply by $V$:
> $$\dot n V + n\dot V = \frac{d(nV)}{d\tau} = 0.$$
> The baryon number $\mathcal{N} = nV$ in a comoving volume is **constant** along the flow — the actual count carried by a fluid element does not change, which is the cleanest statement of conservation.

> [!note]- Complete formal solution
> Writing $j_{\mathrm b}^\mu = nu^\mu = N(u_0 + \mathbf{V})^\mu$ with $N = \Gamma n$, the conservation $\partial_\mu j_{\mathrm b}^\mu = 0$ in $\mathcal{O}$'s coordinates is $\partial_t N + \nabla\cdot(N\mathbf{V}) = 0$, the continuity equation in classical form (the relativistic content is in $N = \Gamma n$). Transporting a comoving volume and applying the Gauss theorem to $u$ gives $\nabla_\mu u^\mu = \dot V/V$. Then $\nabla_\mu(nu^\mu) = \dot n + n\dot V/V = 0$ implies $d(nV)/d\tau = 0$: the comoving baryon count $nV$ is constant. $\blacksquare$

---

# Key Takeaways

**A conserved current becomes a continuity equation, and number conservation is kinematically Newtonian.** The basic lesson is that the covariant law $\nabla_\mu J^\mu = 0$, written in an observer's coordinates, is always a continuity equation $\partial_t(\text{density}) + \nabla\cdot(\text{flux}) = 0$. The striking feature for the baryon current is that the relativistic continuity equation has *no* extra relativistic factor — it is identical in form to the Newtonian one. The reason is a conspiracy: the observed density is enhanced to $N = \Gamma n$ (length contraction packs more baryons into a moving volume), and the flux transforms correspondingly, so the conservation law keeps its classical shape. The transferable insight is that conservation of a counted quantity (number, charge) is "kinematically Newtonian" — the relativistic physics lives in *how the density is measured* ($\Gamma n$), not in the form of the conservation law. This is in contrast to the energy–momentum conservation, where genuinely relativistic terms (the inertia $\rho + p$) do appear.

**The four-divergence of the velocity is the comoving expansion rate.** The identity $\nabla_\mu u^\mu = \dot V/V$ is one of the most useful in the chapter: it gives a geometric, frame-independent meaning to the four-divergence of the flow as the fractional rate at which a comoving volume element expands. This is what lets the energy equation be read as the first law $d(\rho V) = -p\,dV$, and it is the quantity that becomes the Hubble expansion $3\dot a/a$ in cosmology. The trigger to recall it: any time $\nabla_\mu u^\mu$ appears in a fluid equation, read it as "how fast a comoving blob is growing", and a positive divergence means expansion (dilution), a negative one compression. This converts an abstract covariant operator into a concrete physical rate, which is exactly what makes the projected fluid equations interpretable.

**The cleanest conservation statement is "the comoving count is constant".** Combining the continuity equation with the expansion identity gives $d(nV)/d\tau = 0$: the baryon number $nV$ in a volume carried by the flow does not change. This is more intuitive than the differential form — it says, simply, that a fluid element keeps its baryons as it moves, expanding (so $n$ falls) or compressing (so $n$ rises) but never gaining or losing count. The reusable diagnostic: to track a conserved quantity in a flow, follow a comoving volume and assert its total content is constant; the density then scales inversely with the volume. In cosmology this immediately gives $n \propto a^{-3}$ (number density dilutes as the inverse cube of the scale factor), and the same logic, applied to energy with the $pdV$ work included, gives the scaling of every cosmic component.

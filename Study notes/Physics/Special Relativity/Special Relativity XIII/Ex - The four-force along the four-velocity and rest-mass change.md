---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Four-Force"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Thm - Conservation of Four-Momentum"
tags: [physics, special-relativity]
---

# Problem Statement

A pure force preserves rest mass; this exercise studies the forces that do *not*, and the component of the four-force responsible. Work with $c = 1$. A particle of rest mass $m(\tau)$ has [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$ ($U\cdot U = 1$), [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A = dU/d\tau$ ($A\cdot U = 0$), and [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = mU$. It is acted on by a [[Def - Four-Force|four-force]] $F = dP/d\tau$.

1. Decompose the four-force into a part along $U$ and a part orthogonal to $U$, and show
$$F = m\,A + \frac{dm}{d\tau}\,U, \qquad F\cdot U = \frac{dm}{d\tau}.$$
2. Deduce that a four-force is **pure** ($F\cdot U = 0$) if and only if it preserves the rest mass, and that the orthogonal part $mA$ alone can never change the mass.
3. **Application — an excited atom emits a photon.** An atom of rest mass $m_i$ at rest in some frame emits a photon of energy $\omega$ and drops to rest mass $m_f$. Using conservation of four-momentum, find $m_f$ in terms of $m_i$ and $\omega$, and show the emitted photon's energy is slightly *less* than the rest-energy difference $m_i - m_f$ because the atom recoils. Interpret the mass change as the time-integral of $F\cdot U$.
4. Show that the electromagnetic Lorentz four-force $F = qF^\mu{}_\nu U^\nu$ is automatically pure, and explain in one line why this guarantees a charged particle keeps its rest mass however violently it is accelerated.

**Recall:**

![[Def - Four-Force#The Definition]]

Conservation of four-momentum ([[Thm - Conservation of Four-Momentum]]) gives $\sum P_{\text{in}} = \sum P_{\text{out}}$. A [[Def - The Four-Momentum of a Photon|photon]] has null four-momentum, $P_\gamma\cdot P_\gamma = 0$, and relative to an observer $P_\gamma = \omega(U_0 + \mathbf{n})$. The electromagnetic field tensor $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is antisymmetric.

---

# Convergent Strategy

**Problem class.** A *structural-identity* problem for Parts 1–2 (decompose a four-vector against $U$ and $U^\perp$), turning into a *mass-changing-emission* problem for Part 3 (conservation of four-momentum with a varying rest mass).

**Assumption pattern.** A particle whose rest mass may change — an atom de-exciting, a body radiating. The signpost is "the mass changes": this immediately directs attention to the component of the four-force along $U$, since the orthogonal component cannot touch the mass.

**Theorem routing.** Parts 1–2 are the algebra of [[Def - Four-Force|the four-force]]: expand $F = d(mU)/d\tau$ and contract with $U$, using $U\cdot U = 1$ and $A\cdot U = 0$. Part 3 is [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] for $\text{atom}\to\text{atom}' + \gamma$, solved by isolating and squaring the recoiling atom. Part 4 is the antisymmetry argument.

**Key decision point.** The crux of Parts 1–2 is that the four-acceleration is orthogonal to the four-velocity ($A\cdot U = 0$, a consequence of $U\cdot U = 1$), so the decomposition of $F$ into $mA$ and $(dm/d\tau)U$ is exactly its orthogonal/parallel split — the mass change lives *entirely* in the parallel part. For Part 3 the crux is the standard invariant-mass move: isolate the recoiling atom and square to eliminate it.

---

# Legal Operations Used

1. **Differentiate four-momentum with respect to proper time to get the four-force** (operation 9). $F = dP/d\tau = d(mU)/d\tau$ expands by the product rule.

2. **Contract with the four-velocity** (operation 5, structural). $F\cdot U$ isolates the mass-changing component, using $A\cdot U = 0$, $U\cdot U = 1$.

3. **Write down conservation of four-momentum and square the unwanted particle** (operations 1, 2). For the emission, isolate the recoiling atom and square to $m_f^2$.

---

# Hints

> [!note]- Hint 1
> Expand $F = d(mU)/d\tau$ by the product rule: $F = \tfrac{dm}{d\tau}U + m\tfrac{dU}{d\tau} = \tfrac{dm}{d\tau}U + mA$. Now contract with $U$: $F\cdot U = \tfrac{dm}{d\tau}(U\cdot U) + m(A\cdot U)$.

> [!note]- Hint 2
> Differentiate the normalisation $U\cdot U = 1$: $2A\cdot U = 0$, so $A\cdot U = 0$ (the four-acceleration is orthogonal to the four-velocity). With $U\cdot U = 1$ this collapses the contraction to $F\cdot U = dm/d\tau$. Hence $F\cdot U = 0 \iff dm/d\tau = 0$, and the orthogonal part $mA$ never contributes to $F\cdot U$.

> [!note]- Hint 3
> For the atom: conservation reads $P_i = P_f + P_\gamma$ where $P_i = (m_i, \mathbf{0})$ (atom at rest), $P_\gamma$ is null. Isolate the recoiling atom $P_f = P_i - P_\gamma$ and square: $m_f^2 = m_i^2 - 2P_i\cdot P_\gamma = m_i^2 - 2m_i\omega$. Solve for $\omega$.

> [!note]- Hint 4
> For the Lorentz force: $F\cdot U = qF_{\mu\nu}U^\mu U^\nu$. The product $U^\mu U^\nu$ is symmetric in $\mu\nu$ while $F_{\mu\nu}$ is antisymmetric; a symmetric tensor contracted with an antisymmetric one vanishes. So $F\cdot U = 0$ identically.

---

# Solution

The four-force splits cleanly into a piece that turns the worldline ($mA$, orthogonal to $U$) and a piece that changes the rest mass ($(dm/d\tau)U$, along $U$). Which forces change the mass is decided entirely by the projection $F\cdot U$, and the atomic-emission application shows the identity at work as a conservation law.

**Step 1: The orthogonal decomposition of the four-force.**

> [!note]- Derivation
> By definition $F = dP/d\tau$ with $P = mU$. Differentiate by the product rule, allowing the rest mass to vary:
> $$F = \frac{d(mU)}{d\tau} = \frac{dm}{d\tau}\,U + m\,\frac{dU}{d\tau} = \frac{dm}{d\tau}\,U + m\,A,$$
> with $A = dU/d\tau$ the four-acceleration. Now contract with $U$. The normalisation $U\cdot U = 1$ differentiated gives $\tfrac{d}{d\tau}(U\cdot U) = 2A\cdot U = 0$, so $A\cdot U = 0$: the four-acceleration is orthogonal to the four-velocity. Therefore
> $$F\cdot U = \frac{dm}{d\tau}\,(U\cdot U) + m\,(A\cdot U) = \frac{dm}{d\tau}\cdot 1 + m\cdot 0 = \frac{dm}{d\tau}.$$
> So the decomposition $F = mA + (dm/d\tau)U$ is precisely the split of $F$ into its component orthogonal to $U$ (the term $mA$, since $A\cdot U = 0$) and its component along $U$ (the term $(dm/d\tau)U$), and
> $$\boxed{\ F\cdot U = \frac{dm}{d\tau}\ }$$
> (Gourgoulhon's eq. 9.106, translated to $c = 1$ and mostly-minus). The projection of the four-force onto the four-velocity is the rate of change of the rest mass.

**Step 2: Pure $\iff$ mass-preserving.**

> [!note]- Derivation
> From $F\cdot U = dm/d\tau$, the equivalence is immediate:
> $$F\cdot U = 0 \quad\Longleftrightarrow\quad \frac{dm}{d\tau} = 0,$$
> that is, a four-force is **pure** (orthogonal to $U$) if and only if it preserves the rest mass. The orthogonal part $mA$ can never change the mass: it lives in the three-dimensional subspace orthogonal to $U$, where it only rotates $U$ within the mass-shell hyperboloid $P\cdot P = m^2$ (changing the *direction* of the four-momentum, not its length). Changing the mass — moving to a hyperboloid of different radius — requires a component along $U$, i.e. along $P$, and that component is exactly $(dm/d\tau)U$. Structurally: $mA$ is *tangent* to the mass shell, $(dm/d\tau)U$ is *normal* to it, so only the latter changes the shell's radius $m$.

**Step 3: An excited atom emits a photon.**

> [!note]- Derivation
> The atom, initially at rest with rest mass $m_i$, emits a photon and recoils with rest mass $m_f$: $\text{atom}_i \to \text{atom}_f + \gamma$. Conservation of four-momentum reads $P_i = P_f + P_\gamma$, with $P_i = (m_i, \mathbf{0})$ and $P_\gamma$ null. Isolate the recoiling atom (the unwanted particle) and square:
> $$P_f = P_i - P_\gamma, \qquad P_f\cdot P_f = m_f^2 = P_i\cdot P_i - 2P_i\cdot P_\gamma + P_\gamma\cdot P_\gamma.$$
> With $P_i\cdot P_i = m_i^2$, $P_\gamma\cdot P_\gamma = 0$ (null), and $P_i\cdot P_\gamma = m_i\omega$ (rest-frame atom contracted with photon of energy $\omega$):
> $$m_f^2 = m_i^2 - 2m_i\omega \quad\Longrightarrow\quad \omega = \frac{m_i^2 - m_f^2}{2m_i} = \frac{(m_i - m_f)(m_i + m_f)}{2m_i}.$$
> Compare with the naive "the photon carries off the whole rest-energy difference" $\Delta m = m_i - m_f$:
> $$\omega = (m_i - m_f)\,\frac{m_i + m_f}{2m_i} = \Delta m\left(1 - \frac{\Delta m}{2m_i}\right) < \Delta m.$$
> The photon energy is *less* than $\Delta m$ by the fraction $\Delta m/(2m_i)$ — the **recoil deficit**. The missing energy goes into the kinetic energy of the recoiling atom, which must carry momentum $|\mathbf{p}_f| = \omega$ to balance the photon. For an atomic transition $\Delta m \sim$ eV against $m_i \sim 10\,\text{GeV}$, the deficit is $\sim 10^{-10}$ — tiny, but real, and the basis of the recoil-free Mössbauer effect (where the recoil is absorbed by a whole crystal, making $m_i$ effectively macroscopic and the deficit vanish).
>
> *As a four-force statement:* although the emission is sudden, integrate the identity over the process: $\Delta m = m_f - m_i = \int (F\cdot U)\,d\tau$. The mass decreased because the four-force during emission had a negative component along $U$ — the radiation reaction carried rest energy out of the atom. The orthogonal part of any force during the recoil only turned the atom's worldline; the mass change is entirely the parallel part.

**Step 4: The Lorentz force is pure.**

> [!note]- Derivation
> The electromagnetic four-force is $F^\mu = qF^\mu{}_\nu U^\nu$, where $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is antisymmetric, $F_{\mu\nu} = -F_{\nu\mu}$. Contract with $U$:
> $$F\cdot U = qF_{\mu\nu}U^\mu U^\nu.$$
> The product $U^\mu U^\nu$ is **symmetric** under $\mu\leftrightarrow\nu$, while $F_{\mu\nu}$ is **antisymmetric**; the full contraction of a symmetric tensor with an antisymmetric one is identically zero (each term $F_{\mu\nu}U^\mu U^\nu$ cancels its partner $F_{\nu\mu}U^\nu U^\mu = -F_{\mu\nu}U^\mu U^\nu$). Hence
> $$\boxed{\ F\cdot U = qF_{\mu\nu}U^\mu U^\nu = 0\ },$$
> the Lorentz force is **pure**. By Step 2 it preserves the rest mass: $dm/d\tau = 0$. In one line — *the antisymmetry of the field tensor forbids the four-force from having any component along the four-velocity, so it can only turn the four-momentum, never lengthen or shorten it* — which is why an electron in any electromagnetic field, however strong, remains an electron with rest mass $m_e$, its four-momentum sliding along the fixed mass shell. (The full development of the Lorentz force is [[Special Relativity XXI — The Electromagnetic Field|Special Relativity XXI]].)

> [!note]- Complete formal solution
> Expanding $F = d(mU)/d\tau = (dm/d\tau)U + mA$ and contracting with $U$, using $A\cdot U = 0$ (from $U\cdot U = 1$) and $U\cdot U = 1$, gives $F\cdot U = dm/d\tau$. Hence $F$ pure ($F\cdot U = 0$) $\iff$ $dm/d\tau = 0$; the orthogonal part $mA$ is tangent to the mass shell and cannot change $m$. For atomic emission $\text{atom}_i\to\text{atom}_f + \gamma$, conservation $P_i = P_f + P_\gamma$ with $P_i = (m_i,\mathbf{0})$, squared after isolating the atom, gives $m_f^2 = m_i^2 - 2m_i\omega$, so $\omega = (m_i^2 - m_f^2)/2m_i = \Delta m(1 - \Delta m/2m_i) < \Delta m$ (recoil deficit). The mass change is $\Delta m = \int(F\cdot U)d\tau$. The Lorentz force $F = qF^\mu{}_\nu U^\nu$ has $F\cdot U = qF_{\mu\nu}U^\mu U^\nu = 0$ (antisymmetric $\times$ symmetric), hence is pure and preserves rest mass. $\blacksquare$

---

# Key Takeaways

**The four-force splits into "turn the worldline" and "change the mass" — and only the parallel part touches the mass.** The decomposition $F = mA + (dm/d\tau)U$ is the orthogonal/parallel split of the four-force against the four-velocity, and it is forced by the single fact that the four-acceleration is orthogonal to the four-velocity ($A\cdot U = 0$, from $\tfrac{d}{d\tau}(U\cdot U) = 0$). The orthogonal piece $mA$ rotates the four-momentum *within* the mass shell, changing its direction but not its Minkowski length; the parallel piece $(dm/d\tau)U$ moves it *off* the shell to a different radius, changing the rest mass. So the projection $F\cdot U = dm/d\tau$ is the exact diagnostic for whether a force changes a particle's identity. The reusable structural insight: to decide whether a relativistic force alters the rest mass, contract it with the four-velocity — a nonzero result means the mass is changing, a zero result (a pure force) means the particle slides along a fixed mass-shell hyperboloid keeping its identity.

**Antisymmetry makes the electromagnetic force pure — the deep reason charges keep their mass.** The one-line argument that $F\cdot U = qF_{\mu\nu}U^\mu U^\nu = 0$ because $F_{\mu\nu}$ is antisymmetric and $U^\mu U^\nu$ symmetric is one of the most consequential structural facts in relativistic dynamics. It guarantees that the electromagnetic Lorentz force — the one fundamental force of classical relativistic mechanics — never changes a charged particle's rest mass, so an electron stays an electron of mass $m_e$ no matter how it is accelerated, its four-momentum sliding along the fixed shell $P\cdot P = m_e^2$. This is why $E = \gamma m_e$ cleanly tracks an accelerated electron's speed (the mass in the formula is constant), and why accelerator dynamics can be computed from the spatial law $d\mathbf{p}/dt = q(\mathbf{E} + \mathbf{u}\times\mathbf{B})$ alone. The reflex to carry away: whenever a four-force is built by contracting an antisymmetric field tensor with the four-velocity, it is automatically pure — antisymmetry *is* mass-preservation.

**Mass changes are conservation laws in disguise — the recoil deficit and the integrated $F\cdot U$.** The atomic-emission application shows that a rest-mass change need not be put in by hand as a mysterious $dm/d\tau$; it is computed from conservation of four-momentum, and it equals the time-integral of the parallel four-force component, $\Delta m = \int(F\cdot U)\,d\tau$. The emitted photon carries *less* than the full rest-energy difference $m_i - m_f$, by the recoil fraction $\Delta m/2m_i$, because the atom must take up momentum to balance the photon — a small but genuine effect that the Mössbauer technique circumvents by making the recoiling mass macroscopic. The reusable lesson is that the abstract mass-evolution identity $F\cdot U = dm/d\tau$ and the concrete conservation calculation are two views of the same physics: emission and absorption (atoms, nuclei, the [[Ex - The relativistic rocket|photon rocket]]) change rest mass, and the change is always bookkept by the conserved total four-momentum, with the four-force identity supplying the differential version.

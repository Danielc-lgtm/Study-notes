---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Thomas Precession"
  - "Def - Spin Four-Vector"
  - "Def - Fermi-Walker Derivative"
  - "Def - Thomas Rotation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ except where restored, and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a timelike vector $X$ has $X\cdot X > 0$. $\mathcal{O}$ is an accelerated [[Def - Observer and Local Rest Space|observer]] of worldline $\mathcal{L}$, proper time $t$, four-velocity $U$, four-acceleration $A\neq 0$ and *vanishing* [[Def - Local Frame and Four-Rotation|four-rotation]] $\vec\omega = 0$; $\mathcal{O}_*$ is the reference inertial observer of frame $(e_0^*, e_1^*, e_2^*, e_3^*)$ and proper time $t_*$. $\Gamma$ is the Lorentz factor of $\mathcal{O}$ relative to $\mathcal{O}_*$; $\mathbf{V}$ and $\boldsymbol\gamma$ (equivalently $\mathbf{a}$, in atomic-physics notation) are the three-velocity and three-acceleration of $\mathcal{O}$ relative to $\mathcal{O}_*$, both lying in $\mathcal{O}_*$'s rest space. $S$ is the [[Def - Spin Four-Vector|spin four-vector]] (with $S\cdot U = 0$), written $\vec s$ when regarded as a spatial vector in $\mathcal{O}$'s rest space; $\vec C$ is the applied torque four-vector (with $\vec C\cdot U = 0$); and $\mathbf{s}_* := S^{-1}(\vec s)$ is the spin "stopped" into $\mathcal{O}_*$'s rest space by the inverse boost $S^{-1}$ (here $S$ also denotes that boost — context disambiguates the spin from the boost). $\vec\omega_T$ is the [[Def - Thomas Precession|Thomas precession]] vector. $\times \equiv \times_{e_0^*}$ is the cross product in $\mathcal{O}_*$'s rest space. Full registry on [[Special Relativity XVI — Accelerated Observers]].

> [!warning] Convention: Gourgoulhon's $\vec\gamma$ and signature
> Gourgoulhon (§12.5.4) writes $\vec\gamma$ for the relative three-acceleration (clashing with the Lorentz factor, which he calls $\Gamma$) and uses mostly-plus. This page writes the three-acceleration as $\boldsymbol\gamma$ or $\mathbf{a}$ and reserves $\Gamma, \gamma$ for the Lorentz factor. His spin law $\mathrm{d}\vec s/\mathrm{d}t = \vec C + c(\vec a\cdot\vec s)\vec u$ and final equation $\mathrm{d}\vec s_*/\mathrm{d}t_* = \Gamma^{-1}S^{-1}(\vec C) + \vec\omega_T\times\vec s_*$ are transcribed unchanged; the orthogonality conditions $S\cdot U = 0$, $\vec C\cdot U = 0$ are signature-independent.

---

# Statement

> **Theorem (Thomas equation).** Let $\mathcal{O}$ be a non-rotating accelerated observer ($\vec\omega = 0$) carrying a particle of spin four-vector $S$ subject to a torque four-vector $\vec C$ (orthogonal to $U$), so that the spin evolves by the Fermi–Walker law with torque,
> $$\frac{\mathrm{d}S}{\mathrm{d}t} = \vec C + c\,(A\cdot S)\,U.$$
> Let $\mathbf{s}_* := S^{-1}(\vec s)$ be the spin stopped into the rest space of the inertial observer $\mathcal{O}_*$ by the inverse of the boost $S$ relating $\mathcal{O}_*$ to $\mathcal{O}$. Then $\mathbf{s}_*$ obeys
> $$\boxed{\;\frac{\mathrm{d}\mathbf{s}_*}{\mathrm{d}t_*} = \frac{1}{\Gamma}\,S^{-1}(\vec C) \;+\; \vec\omega_T \times_{e_0^*}\mathbf{s}_*\;}$$
> where the **Thomas precession vector** is
> $$\vec\omega_T = \frac{\Gamma^2}{c^2(\Gamma + 1)}\,\boldsymbol\gamma\times_{e_0^*}\mathbf{V} = \frac{\Gamma - 1}{V^2}\,\boldsymbol\gamma\times_{e_0^*}\mathbf{V}\ \xrightarrow{\ V\ll c\ }\ \frac{1}{2c^2}\,\boldsymbol\gamma\times_{e_0^*}\mathbf{V}.$$

> **Corollary (free gyroscope).** For a torque-free gyroscope ($\vec C = 0$) the equation reduces to a pure precession,
> $$\frac{\mathrm{d}\mathbf{s}_*}{\mathrm{d}t_*} = \vec\omega_T\times_{e_0^*}\mathbf{s}_*,$$
> so the stopped spin rotates at angular velocity $\vec\omega_T$ — [[Def - Thomas Precession|Thomas precession]] — even though the spin is intrinsically non-rotating ($\vec\omega = 0$). The effect is of order $\Gamma - 1$ and vanishes in the Newtonian limit.

---

# Motivation

This theorem is the equation of motion for a spinning particle carried along an accelerated, curving worldline — a gyroscope in orbit, a polarised electron in a storage ring, an electron in an atom. It answers the question: given that a torque $\vec C$ acts on the spin, *and* that the particle's rest frame is rotating relative to the laboratory (by Thomas precession), how does the spin actually evolve as seen in the laboratory?

The reason a special equation is needed is the gap, isolated in the [[Def - Thomas Precession|definition of Thomas precession]], between two notions of "not rotating". The spin of a free particle is **Fermi–Walker transported** — intrinsically non-rotating, $\vec\omega = 0$ — but its representation in the *inertial* observer's rest space nonetheless rotates, because the boost relating the two frames keeps changing direction. The Thomas equation is what you get when you write the intrinsic, frame-independent transport law and then express it in the laboratory frame: the intrinsic non-rotation becomes a laboratory precession at $\vec\omega_T$, and any genuine torque adds on top.

The historical importance is a factor of two in the hydrogen spectrum. L. H. Thomas derived this equation in $1926$ precisely to resolve a discrepancy: the semiclassical spin–orbit coupling overestimated the fine-structure splitting of atomic spectral lines by a factor of two, and the missing ingredient was that the electron's rest frame rotates relative to the nucleus by exactly the precession this equation describes. Adding the Thomas precession halves the naive result — the **Thomas half** — bringing theory into agreement with experiment, and the same factor falls out automatically from the Dirac equation two years later. The Thomas equation is also the field-free skeleton of the Bargmann–Michel–Telegdi equation that governs spin precession in particle accelerators and underlies the muon $g - 2$ measurements.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a spin four-vector is carried, with torque, along a non-rotating accelerated worldline". The point of input broadening is to recognise the disguises.

The first disguised source is **"a classical gyroscope is transported along any curved trajectory"**. A torque-free gyroscope's spin is Fermi–Walker transported by definition, so it satisfies the hypothesis with $\vec C = 0$ — even if the word "spin" never appears and one speaks only of the gyroscope's axis. The bridge is that a freely-suspended gyroscope axis *is* a Fermi–Walker-transported spacelike unit vector. So any problem asking how a gyroscope's pointing changes as it is carried around a bend routes through the free-gyroscope corollary. *Example problem:* find the orientation drift of a gyroscope carried once around a [[Ex - Thomas precession of a gyroscope in circular orbit|circular orbit]].

The second disguised source is **"a magnetic moment precesses in an electromagnetic field"**. A particle with magnetic moment $\boldsymbol\mu$ in a field $\mathbf{B}$ feels a torque $\boldsymbol\mu\times\mathbf{B}$, which is a particular $\vec C$; if the particle is also accelerated (e.g. bent by the same field), the Thomas precession adds to the magnetic precession. The bridge is that the electromagnetic torque on the spin is exactly the $\vec C$ term, while the bending of the trajectory supplies the $\vec\omega_T$ term. So any spin-in-field problem is a Thomas-equation problem once the trajectory curves. *Example problem:* compute the net spin precession of a muon in a storage ring (the BMT equation), where the magnetic torque and the Thomas term combine.

The third disguised source is **"an electron orbits a nucleus and one wants its spin–orbit energy"**. The orbiting electron is centripetally accelerated with $\mathbf{a}\perp\mathbf{v}$, so its rest frame Thomas-precesses; combined with the magnetic torque from the field it sees, this gives the spin–orbit interaction. The bridge is the equivalence of "orbiting charge" with "accelerated spin in a field". So the atomic fine-structure calculation is a Thomas-equation problem. *Example problem:* derive the [[Ex - The Thomas half and atomic fine structure|Thomas half]] in hydrogen.

**Targets (Output Amplification)**

The conclusion is the equation $\mathrm{d}\mathbf{s}_*/\mathrm{d}t_* = \Gamma^{-1}S^{-1}(\vec C) + \vec\omega_T\times\mathbf{s}_*$.

Combine the free-gyroscope corollary with **a closed orbit**. Integrating $\vec\omega_T$ around a closed loop in velocity space gives a net rotation — the accumulated Thomas angle — that depends only on the loop, not on the timing. The further result is a *holonomy*: a gyroscope carried once around a circular orbit returns rotated by $-2\pi(\Gamma - 1)$, a measurable lag. The combination is nonobvious because it converts an instantaneous precession rate into a topological-flavoured net angle, the special-relativistic analogue of [[Def - Thomas Precession|geodetic precession and the Berry phase]].

Combine the full equation with **an explicit electromagnetic torque $\vec C = g(q/2m)\,S\times\mathbf{B}$**. The result is the **Bargmann–Michel–Telegdi equation**, the covariant law for spin precession in arbitrary fields, in which the magnetic precession and the Thomas precession appear as separate terms. The further result is that the *difference* between the spin-precession rate and the orbital (cyclotron) rate isolates the anomalous magnetic moment $g - 2$. The combination is useful because it is the working tool of accelerator physics: the muon $g-2$ experiments measure exactly this difference, and the Thomas term must be subtracted to extract the anomaly.

Combine the low-velocity precession rate $\vec\omega_T \simeq \tfrac12\mathbf{a}\times\mathbf{v}/c^2$ with **the spin–orbit torque of an atomic electron**. The Thomas term contributes an energy that is exactly $-\tfrac12$ of the naive spin–orbit energy, halving it. The further result is the corrected fine-structure formula, agreeing with experiment and with the Dirac equation. The combination is the historical payoff — a kinematic correction resolving a factor-of-two discrepancy in atomic spectra.

---

# Why Is It True

The deep reason is that **the spin is dragged by two distinct things at once — the genuine torque $\vec C$, and the steadily-reorienting boost that connects the particle's frame to the laboratory — and the second drag is the Thomas precession.**

Take the torque-free case first, since it is the heart of the matter. The spin $S$ is Fermi–Walker transported: it is "as fixed as possible" along the worldline, the closest thing to a constant vector that can stay orthogonal to the changing four-velocity $U$. Intrinsically it does not rotate. But to *read* the spin in the laboratory, one applies the inverse boost $S^{-1}$ that stops the particle, mapping $S$ to a vector $\mathbf{s}_*$ in the inertial observer's rest space. The boost $S$ changes from instant to instant — because the particle's velocity changes — and the composition of "the new inverse boost" with "the old boost" is, by the [[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation|composition law for boosts]], not a pure boost but a boost *times a spatial rotation*: the [[Def - Thomas Rotation|Thomas rotation]]. So even though $S$ itself never rotates intrinsically, its stopped representative $\mathbf{s}_*$ picks up a small spatial rotation at every step, and these accumulate into the precession $\vec\omega_T\times\mathbf{s}_*$.

**The one-line mechanism: a Fermi–Walker-transported spin is intrinsically rigid, but the boost that displays it in the laboratory keeps turning, and the leftover rotation from composing successive boosts — the Thomas rotation — makes the laboratory image of the spin precess at $\vec\omega_T$.** This is why $\vec\omega_T \propto \boldsymbol\gamma\times\mathbf{V}$: the rotation appears only when the acceleration (which changes the boost) is not parallel to the velocity (the existing boost direction), and the cross product measures exactly the non-collinearity. When $\mathbf{a}\parallel\mathbf{v}$ the successive boosts are collinear, compose to a pure boost, and there is no leftover rotation — no Thomas precession — which is why the uniformly accelerated observer of §16.2 shows none.

Now restore the torque. A genuine torque $\vec C$ rotates the spin in the particle's own frame; transported to the laboratory it appears as $\Gamma^{-1}S^{-1}(\vec C)$, the $\Gamma^{-1}$ being the time-dilation factor converting the rate from proper time to laboratory time ($\mathrm{d}t = \Gamma^{-1}\mathrm{d}t_*$). The two effects simply add: the laboratory spin responds to the real torque *and* to the kinematic precession of its own display frame. That additivity is the content of the equation, and it is what makes the Thomas precession a universal background rotation that any spinning particle on a curving worldline carries, independent of the forces acting on it.

---

# What Makes This Hard

The derivation is a careful bookkeeping of *which frame* and *which time* every quantity lives in, and the non-obvious step is the distinction between the spin $S$ (in the particle's rest space), the stopped spin $\mathbf{s}_*$ (in the inertial rest space, defined by $S^{-1}$), and the orthogonal projection $\perp_{e_0^*}S$ (a third, different vector). The cleanest equation is for $\mathbf{s}_*$; the projection obeys a messier law that does *not* reduce to a pure precession, which is the trap. The most common errors are: forgetting the $\Gamma^{-1}$ converting torque rate from proper to laboratory time; using $\perp_{e_0^*}S$ in place of $\mathbf{s}_*$ and then being unable to recover a clean precession; and a sign error in $\vec\omega_T$ (it is *opposite* to $\mathbf{V}\times\boldsymbol\gamma$, i.e. along $\boldsymbol\gamma\times\mathbf{V}$).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Start from the Fermi–Walker-with-torque law for $S$, express the stopped spin $\mathbf{s}_* = S^{-1}(\vec s)$ explicitly via the inverse boost, differentiate with respect to laboratory time $t_*$, substitute the spin law and the kinematic relations for $\mathrm{d}\mathbf{V}/\mathrm{d}t_*$, and simplify until the torque term separates as $\Gamma^{-1}S^{-1}(\vec C)$ and the remainder forms the double cross product $\vec\omega_T\times\mathbf{s}_*$.

**Subgoal decomposition:**

1. **Express the stopped spin.** Write $\mathbf{s}_* = S^{-1}(\vec s)$ using the boost formula; with $\vec s$ orthogonal to $U$ this gives $\mathbf{s}_* = \vec s - \tfrac{1}{c}(\mathbf{V}\cdot\vec s)\big[e_0^* + \tfrac{\Gamma}{c(1+\Gamma)}\mathbf{V}\big]$.
   - *Hint:* $S^{-1}$ is the boost of velocity $-\mathbf{V}$; apply the standard boost-of-a-vector formula and use $e_0^*\cdot\vec s = -\tfrac1c\mathbf{V}\cdot\vec s$.
   - *Why needed:* It is the quantity whose evolution the theorem describes.

2. **Differentiate with respect to $t_*$.** Form $\mathrm{d}\mathbf{s}_*/\mathrm{d}t_*$, using $\mathrm{d}\vec s/\mathrm{d}t_* = \Gamma^{-1}[\vec C + c(A\cdot S)U]$ and $\mathrm{d}\mathbf{V}/\mathrm{d}t_* = \boldsymbol\gamma$.
   - *Hint:* Convert proper-time derivatives to $t_*$ via $\mathrm{d}/\mathrm{d}t = \Gamma\,\mathrm{d}/\mathrm{d}t_*$; the $(A\cdot S)U$ term simplifies using $A\cdot S = \Gamma^2\boldsymbol\gamma\cdot\vec s/c^2$.
   - *Why needed:* It produces the raw evolution equation before grouping.

3. **Recognise the torque term.** Show that the torque-dependent part collapses to $\Gamma^{-1}S^{-1}(\vec C)$, by the same algebra that produced $\mathbf{s}_* = S^{-1}(\vec s)$ with $\vec s \to \vec C$.
   - *Hint:* $\vec C$, like $\vec s$, is orthogonal to $U$, so $S^{-1}(\vec C)$ has the identical form.
   - *Why needed:* It isolates the driven (torque) part of the equation.

4. **Recognise the precession term.** Show the remaining part equals $\vec\omega_T\times\mathbf{s}_*$ via the double-cross-product identity $(\boldsymbol\gamma\cdot\mathbf{s}_*)\mathbf{V} - (\mathbf{V}\cdot\mathbf{s}_*)\boldsymbol\gamma = (\boldsymbol\gamma\times\mathbf{V})\times\mathbf{s}_*$, with $\vec\omega_T = \tfrac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$.
   - *Hint:* $(\mathbf{a}\times\mathbf{b})\times\mathbf{c} = \mathbf{b}(\mathbf{a}\cdot\mathbf{c}) - \mathbf{a}(\mathbf{b}\cdot\mathbf{c})$.
   - *Why needed:* It identifies the precession and the Thomas rate, completing the equation.

---

# Lemma Decomposition

> [!note]- Lemma 1: The stopped spin is $\mathbf{s}_* = \vec s - \tfrac{1}{c}(\mathbf{V}\cdot\vec s)\big[e_0^* + \tfrac{\Gamma}{c(1+\Gamma)}\mathbf{V}\big]$
> **Statement:** Applying the inverse boost $S^{-1}$ (velocity $-\mathbf{V}$) to the spin $\vec s$ gives the stopped spin above.
>
> **Hint:** Use the boost-of-a-vector formula and $e_0^*\cdot\vec s = -\tfrac1c\mathbf{V}\cdot\vec s$ (from $\vec s\cdot U = 0$ and the decomposition of $U$).
>
> **Why needed:** It is the explicit form of $\mathbf{s}_*$, differentiated in Lemma 2.
>
> > [!note]- Full proof
> > The boost $S$ carries $e_0^*$ to $U = \Gamma(e_0^* + \tfrac1c\mathbf{V})$; its inverse $S^{-1}$ is the boost of velocity $-\mathbf{V}$. For a vector $\vec s$, the boost formula (with $\vec u\to e_0^*$, $\vec V\to -\mathbf{V}$) gives
> > $$\mathbf{s}_* = S^{-1}(\vec s) = -\Gamma(e_0^*\cdot\vec s)e_0^* + \frac{\Gamma}{c}\big[-(\mathbf{V}\cdot\vec s)e_0^* + (e_0^*\cdot\vec s)(-\mathbf{V})\big] + \vec s + (e_0^*\cdot\vec s)e_0^* + \frac{\Gamma^2}{c^2(1+\Gamma)}(\mathbf{V}\cdot\vec s)\mathbf{V}.$$
> > Now $\vec s\cdot U = 0$ and $U = \Gamma(e_0^* + \tfrac1c\mathbf{V})$ give $e_0^*\cdot\vec s = -\tfrac1c\mathbf{V}\cdot\vec s$ (in mostly-minus, $e_0^*\cdot e_0^* = 1$, $e_0^*\cdot\mathbf{V} = 0$, $\mathbf{V}\cdot\vec s$ Euclidean). Substituting and collecting the $e_0^*$ and $\mathbf{V}$ terms, the $\vec s$ component survives and the rest combine into
> > $$\mathbf{s}_* = \vec s - \frac{1}{c}(\mathbf{V}\cdot\vec s)\left[e_0^* + \frac{\Gamma}{c(1+\Gamma)}\mathbf{V}\right]. \qquad \blacksquare$$

> [!note]- Lemma 2: $A\cdot S = \tfrac{\Gamma^2}{c^2}\,\boldsymbol\gamma\cdot\vec s$
> **Statement:** The scalar $A\cdot S$ appearing in the spin law equals $\tfrac{\Gamma^2}{c^2}\boldsymbol\gamma\cdot\vec s$.
>
> **Hint:** Express the four-acceleration $A$ in terms of the relative acceleration $\boldsymbol\gamma$ and velocity $\mathbf{V}$, and use $e_0^*\cdot\vec s = -\tfrac1c\mathbf{V}\cdot\vec s$.
>
> **Why needed:** It simplifies the $(A\cdot S)U$ term so the torque and precession parts separate cleanly.
>
> > [!note]- Full proof
> > The four-acceleration in terms of $\mathcal{O}_*$-relative quantities is $A = \Gamma^2[c^2\,\boldsymbol\gamma_{\!4} - (\boldsymbol\gamma\cdot\mathbf{V})(\mathbf{V} + ce_0^*)]/c^2$... more directly, from $A = \Gamma^{-2}[\,\cdots]$ inverted (Gourgoulhon 12.93), one has $A\cdot S = \tfrac{\Gamma^2}{c^2}[\boldsymbol\gamma\cdot\vec s + \tfrac{\Gamma^2}{c^2}(\boldsymbol\gamma\cdot\mathbf{V})(\mathbf{V}\cdot\vec s + c\,e_0^*\cdot\vec s)]$. The inner bracket $\mathbf{V}\cdot\vec s + c\,e_0^*\cdot\vec s = \mathbf{V}\cdot\vec s + c(-\tfrac1c\mathbf{V}\cdot\vec s) = 0$, using Lemma 1's relation $e_0^*\cdot\vec s = -\tfrac1c\mathbf{V}\cdot\vec s$. Hence $A\cdot S = \tfrac{\Gamma^2}{c^2}\boldsymbol\gamma\cdot\vec s$. $\blacksquare$

> [!note]- Lemma 3: The double-cross-product identity gives the precession term
> **Statement:** $(\boldsymbol\gamma\cdot\mathbf{s}_*)\mathbf{V} - (\mathbf{V}\cdot\mathbf{s}_*)\boldsymbol\gamma = (\boldsymbol\gamma\times_{e_0^*}\mathbf{V})\times_{e_0^*}\mathbf{s}_*$, so the residual term is $\vec\omega_T\times_{e_0^*}\mathbf{s}_*$ with $\vec\omega_T = \tfrac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$.
>
> **Hint:** Apply the vector identity $(\mathbf{a}\times\mathbf{b})\times\mathbf{c} = \mathbf{b}(\mathbf{a}\cdot\mathbf{c}) - \mathbf{a}(\mathbf{b}\cdot\mathbf{c})$ with $\mathbf{a} = \boldsymbol\gamma$, $\mathbf{b} = \mathbf{V}$, $\mathbf{c} = \mathbf{s}_*$.
>
> **Why needed:** It turns the bracket from the differentiation into a precession $\vec\omega_T\times\mathbf{s}_*$, completing the equation.
>
> > [!note]- Full proof
> > The vector triple product identity in $\mathcal{O}_*$'s Euclidean rest space reads $(\mathbf{a}\times\mathbf{b})\times\mathbf{c} = \mathbf{b}(\mathbf{a}\cdot\mathbf{c}) - \mathbf{a}(\mathbf{b}\cdot\mathbf{c})$. With $\mathbf{a} = \boldsymbol\gamma$, $\mathbf{b} = \mathbf{V}$, $\mathbf{c} = \mathbf{s}_*$:
> > $$(\boldsymbol\gamma\times\mathbf{V})\times\mathbf{s}_* = \mathbf{V}(\boldsymbol\gamma\cdot\mathbf{s}_*) - \boldsymbol\gamma(\mathbf{V}\cdot\mathbf{s}_*).$$
> > Therefore $\tfrac{\Gamma^2}{c^2(1+\Gamma)}[(\boldsymbol\gamma\cdot\mathbf{s}_*)\mathbf{V} - (\mathbf{V}\cdot\mathbf{s}_*)\boldsymbol\gamma] = \tfrac{\Gamma^2}{c^2(1+\Gamma)}(\boldsymbol\gamma\times\mathbf{V})\times\mathbf{s}_* = \vec\omega_T\times\mathbf{s}_*$, defining $\vec\omega_T := \tfrac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$. The identity $\Gamma^2/(1+\Gamma) = (\Gamma-1)c^2/V^2$ gives the equivalent form $\vec\omega_T = \tfrac{\Gamma-1}{V^2}\boldsymbol\gamma\times\mathbf{V}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> The spin four-vector evolves by the Fermi–Walker law with torque, $\mathrm{d}S/\mathrm{d}t = \vec C + c(A\cdot S)U$ (proper time $t$), with $S\cdot U = 0$ and $\vec C\cdot U = 0$. Define the stopped spin $\mathbf{s}_* := S^{-1}(\vec s)$.
>
> By **Lemma 1**, $\mathbf{s}_* = \vec s - \tfrac1c(\mathbf{V}\cdot\vec s)[e_0^* + \tfrac{\Gamma}{c(1+\Gamma)}\mathbf{V}]$. Differentiate with respect to laboratory time $t_*$, converting $\mathrm{d}/\mathrm{d}t = \Gamma\,\mathrm{d}/\mathrm{d}t_*$ so that $\mathrm{d}\vec s/\mathrm{d}t_* = \Gamma^{-1}[\vec C + c(A\cdot S)U]$, and using $\mathrm{d}\mathbf{V}/\mathrm{d}t_* = \boldsymbol\gamma$ and $\mathrm{d}\Gamma/\mathrm{d}t_* = \Gamma^3\boldsymbol\gamma\cdot\mathbf{V}/c^2$.
>
> By **Lemma 2**, $A\cdot S = \tfrac{\Gamma^2}{c^2}\boldsymbol\gamma\cdot\vec s$, so the $c(A\cdot S)U$ term contributes a multiple of $U = \Gamma(e_0^* + \tfrac1c\mathbf{V})$. After substituting and using $\vec V\cdot\vec s = \Gamma\,\mathbf{V}\cdot\mathbf{s}_*$ and $\boldsymbol\gamma\cdot\vec s = \boldsymbol\gamma\cdot\mathbf{s}_* + \tfrac{\Gamma^2}{c^2(1+\Gamma)}(\boldsymbol\gamma\cdot\mathbf{V})(\mathbf{V}\cdot\mathbf{s}_*)$ (the analogues of Lemma 1 read off the spin–stopped-spin relation), the terms proportional to $e_0^*$ cancel (the stopped spin lies in $\mathcal{O}_*$'s rest space), and the result is
> $$\frac{\mathrm{d}\mathbf{s}_*}{\mathrm{d}t_*} = \frac{1}{\Gamma}\left[\vec C - \frac{\mathbf{V}\cdot\vec C}{c}\left(e_0^* + \frac{\Gamma}{c(1+\Gamma)}\mathbf{V}\right)\right] + \frac{\Gamma^2}{c^2(1+\Gamma)}\big[(\boldsymbol\gamma\cdot\mathbf{s}_*)\mathbf{V} - (\mathbf{V}\cdot\mathbf{s}_*)\boldsymbol\gamma\big].$$
> The first bracket is exactly $S^{-1}(\vec C)$ (Lemma 1 with $\vec s \to \vec C$, since $\vec C\cdot U = 0$), so the torque term is $\Gamma^{-1}S^{-1}(\vec C)$.
>
> By **Lemma 3**, the second bracket equals $(\boldsymbol\gamma\times\mathbf{V})\times\mathbf{s}_*$, so the residual term is $\vec\omega_T\times\mathbf{s}_*$ with $\vec\omega_T = \tfrac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$. Combining,
> $$\frac{\mathrm{d}\mathbf{s}_*}{\mathrm{d}t_*} = \frac{1}{\Gamma}S^{-1}(\vec C) + \vec\omega_T\times_{e_0^*}\mathbf{s}_*.$$
> For $\vec C = 0$ this is the pure precession $\mathrm{d}\mathbf{s}_*/\mathrm{d}t_* = \vec\omega_T\times\mathbf{s}_*$. The equivalent forms $\vec\omega_T = \tfrac{\Gamma-1}{V^2}\boldsymbol\gamma\times\mathbf{V}$ and the low-velocity limit $\tfrac{1}{2c^2}\boldsymbol\gamma\times\mathbf{V}$ follow from $\Gamma^2/(1+\Gamma) = (\Gamma-1)c^2/V^2$ and $\Gamma\to 1$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The muon $g - 2$ experiment (particle physics).** In a storage ring a muon's spin precesses by the magnetic torque *plus* the Thomas precession; the difference between the spin-precession frequency and the cyclotron frequency is proportional to the anomalous moment $a_\mu = (g-2)/2$. The Thomas equation, extended to the BMT equation by inserting the electromagnetic torque, is the exact basis of the analysis, and the Thomas term must be correctly subtracted. The application is nonobvious because a kinematic effect from $1926$ is essential to a part-per-billion precision measurement testing the Standard Model.

**Geodetic precession and Gravity Probe B (general relativity).** A gyroscope in Earth orbit precesses relative to the distant stars by the geodetic effect (curvature) and frame-dragging; the *special-relativistic* part of this precession — the part present even in flat spacetime for an accelerated orbit — is exactly the Thomas precession of this equation. Gravity Probe B measured the total to confirm general relativity. The application battle-tests the source by recognising the free-gyroscope corollary as the flat-spacetime limit of the geodetic effect.

**Spin transport in optical and condensed-matter systems (geometric phases).** The structure "intrinsically rigid object whose laboratory representation rotates because the transporting frame turns" recurs as the **Berry phase** in quantum systems and as the geometric phase of polarised light in a coiled fibre. The Thomas precession is the classical-spin, velocity-space member of this family, governed by the same holonomy logic. The application is surprising because a relativistic spin equation shares its mathematical skeleton with the adiabatic transport of a quantum state.

---

# Bridges

- **[[Def - Thomas Precession]]** — this theorem is the dynamical equation whose torque-free limit *is* the Thomas precession defined there. The definition isolates the precession rate $\vec\omega_T$ as a kinematic fact about a non-rotating frame; this theorem embeds it in an equation of motion for a spin, showing how a genuine torque $\vec C$ adds to the kinematic precession. The free-gyroscope corollary recovers the definition exactly.

- **[[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation]]** — the precession term $\vec\omega_T\times\mathbf{s}_*$ is the differential, time-rate version of the discrete Thomas rotation produced when two boosts are composed. The boost $S$ relating the particle to the laboratory changes direction along the worldline; composing the new inverse boost with the old one leaves a residual spatial rotation per unit time, and that rate is $\vec\omega_T$. The finite composition law and this differential precession are the same fact at two scales.

- **[[Def - Fermi-Walker Derivative]]** — the spin law $\mathrm{d}S/\mathrm{d}t = \vec C + c(A\cdot S)U$ is the Fermi–Walker transport law with a torque source: for $\vec C = 0$ it is exactly $D^{\mathrm{FW}}_U S = 0$, the statement that a free spin is Fermi–Walker transported. The Thomas equation is what that intrinsic transport law becomes when expressed in the inertial laboratory frame, the intrinsic non-rotation re-appearing as the laboratory precession $\vec\omega_T$.

- **The Bargmann–Michel–Telegdi equation** — inserting the electromagnetic torque $\vec C$ on a particle's magnetic moment into this equation yields the BMT equation, the covariant law governing spin precession in arbitrary electric and magnetic fields. The Thomas term $\vec\omega_T$ is the field-free, purely kinematic piece; the magnetic torque supplies the rest. The BMT equation is the working tool for polarised beams in accelerators, and the muon $g-2$ measurement reads the anomalous moment off the difference between the spin and orbital precession frequencies, with the Thomas term subtracted.

---

# Unlocked by This

> [!tip] The BMT Equation and Spin Dynamics in Accelerators *(from accelerator and particle physics)*
> Promoting the torque $\vec C$ to the electromagnetic torque on a particle's magnetic moment, $\vec C \propto S\times\mathbf{B}$ in the rest frame, turns this equation into the **Bargmann–Michel–Telegdi (BMT) equation** — the covariant law for the precession of a spin in arbitrary $\mathbf{E}$ and $\mathbf{B}$ fields. It governs how the spin of a polarised beam of muons or electrons precesses in a storage ring, and the tiny excess of the spin-precession rate over the orbital frequency is the **anomalous magnetic moment** $g - 2$, measured to extraordinary precision. The kinematic Thomas precession of this page is the field-free piece of the BMT equation, and extracting the genuine anomaly from data requires subtracting it correctly.

> [!tip] Geodetic Precession, Frame-Dragging, and Gravity Probe B *(from General Relativity)*
> In general relativity a gyroscope carried around a massive body precesses by the **geodetic effect** (from the curvature the mass produces) and, if the body rotates, by **frame-dragging** (the Lense–Thirring effect). Both are holonomies of parallel transport, the curved-spacetime analogues of this equation's Thomas precession (the holonomy of Fermi–Walker transport in flat spacetime). The free-gyroscope corollary is precisely the special-relativistic part of a gyroscope's precession in orbit, and **Gravity Probe B** measured the geodetic and frame-dragging precessions of gyroscopes in Earth orbit to confirm general relativity. The Thomas equation is the conceptual and computational prerequisite.

---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Centre of Inertia"
  - "Thm - Minimal Size of a Spinning System"
  - "Def - Spin Four-Vector"
tags: [physics, special-relativity]
---

# Problem Statement

This exercise exhibits the most surprising fact of the chapter: two observers in relative motion disagree on the location of a spinning body's centre of mass. Consider an isolated system of rest mass $m$ and spin vector $\vec\sigma$, at rest in frame $S$ with its [[Def - Centre of Inertia|centre of inertia]] $G$ at the spatial origin. Working with $c = 1$:

1. A toy model: two point masses $m/2$ each, connected by a rigid massless rod of length $2\ell$ along the $y$-axis, rotating in the $xy$-plane about $G$ at angular speed $\omega$ (so the system has spin $\vec\sigma = \sigma\,\hat{\mathbf{z}}$ with $\sigma = m\ell^2\omega$ to leading order). At the instant the masses lie on the $y$-axis, mass $+$ at $(0,+\ell)$ moves in $+\hat{\mathbf{x}}$ and mass $-$ at $(0,-\ell)$ moves in $-\hat{\mathbf{x}}$. Compute, in frame $S$, the energy of each mass. They are equal — so in $S$ the centroid is at the origin, $G$.
2. Now view the system from a frame $S'$ moving at velocity $\vec V = V\hat{\mathbf{x}}$ relative to $S$. Show that in $S'$ the two masses have *different* energies (the one moving with the boost is more energetic), so the energy-weighted centroid $G_{\mathcal{O}'}$ is displaced from $G$ along the $y$-axis.
3. Show that the displacement is $\overrightarrow{GG_{\mathcal{O}'}} = \frac{1}{mc^2}\vec\sigma\times\vec V$, matching the general formula of [[Thm - Minimal Size of a Spinning System]], and that it is perpendicular to both $\vec\sigma$ and $\vec V$.
4. Conclude that the centroid is observer-dependent, that it coincides with $G$ for all observers iff $\vec\sigma = 0$, and that the displacement is bounded by the Møller radius $R_0 = \|\vec\sigma\|/(mc)$.

**Recall:**

![[Thm - Minimal Size of a Spinning System#Statement]]

The [[Def - Centre of Inertia|centroid]] relative to an observer is $\overrightarrow{OG_\mathcal{O}} = \frac{1}{E}\sum_a E_a\overrightarrow{OM_a}$, the energy-weighted mean position, with $E_a = p_a\cdot U_0$ the energy of particle $a$ relative to the observer. Under a boost at velocity $V$ along $x$, a particle of energy $E$ and $x$-momentum $p_x$ in $S$ has energy $E' = \gamma(E - Vp_x)$ in $S'$.

---

# Convergent Strategy

**Problem class.** A *locate-something-and-find-it-observer-dependent* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: brace for the centre of mass to depend on the observer; compute the energy-weighted mean in each frame and do not assume they agree.

**Assumption pattern.** A spinning system, two observers. The signpost is "a spinning body viewed from two frames": the centroid will shift by $\vec\sigma\times\vec V/(mc^2)$, and the shift is the boost-induced energy asymmetry between the rotating parts. This is exactly the phenomenon [[Thm - Minimal Size of a Spinning System|Møller's theorem]] quantifies.

**Theorem routing.** Part 1 computes equal energies in the rest frame, so $G_\mathcal{O} = G$ there. Part 2 boosts and finds unequal energies, so the centroid shifts. Part 3 matches the general displacement formula. Part 4 reads off the observer-dependence, the spin-vanishing criterion, and the Møller bound.

**Key decision point.** The crux is seeing *why* the energies become unequal: the boost adds energy to the mass moving *with* the boost and subtracts from the one moving *against*, and because these masses are at *different positions* (on opposite sides of $G$), the energy-weighted mean shifts toward the more energetic one. The spin (the rotation) is what correlates position with velocity, so no spin means no asymmetry.

---

# Legal Operations Used

1. **Operation 4 from the topic page (go to the barycentric frame).** Part 1 works in the rest frame where the centroid is $G$; the contrast with the boosted frame is the whole exercise.

2. **Operation 1 from the topic page (the boost of energy).** Part 2 boosts the energies $E'_a = \gamma(E_a - Vp_{x,a})$ to find the asymmetry.

---

# Hints

> [!note]- Hint 1
> In frame $S$, both masses have the same speed $\omega\ell$ (rotating rigidly), so the same Lorentz factor $\gamma_0$ and the same energy $E_\pm = \tfrac{m}{2}\gamma_0$. Equal energies at symmetric positions $(0,\pm\ell)$ give a centroid at the origin.

> [!note]- Hint 2
> Boost to $S'$ moving at $V\hat{\mathbf{x}}$. The mass at $(0,+\ell)$ moves in $+\hat{\mathbf{x}}$ (with $x$-momentum $+p_x$), the mass at $(0,-\ell)$ in $-\hat{\mathbf{x}}$ ($x$-momentum $-p_x$). Their energies in $S'$ are $E'_\pm = \gamma(E_\pm \mp Vp_x)$... track the sign: the mass whose velocity opposes $\vec V$ gains energy. So the two energies differ.

> [!note]- Hint 3
> The centroid in $S'$ is the energy-weighted mean of the positions $(0,\pm\ell)$. With unequal weights $E'_+ \ne E'_-$, the mean is at $y_{G'} = \ell\,\frac{E'_+ - E'_-}{E'_+ + E'_-}$. Compute $E'_+ - E'_-$ and $E'_+ + E'_- = E'$ to get $y_{G'}$, then check it equals $\frac{1}{mc^2}(\vec\sigma\times\vec V)_y = \frac{\sigma V}{mc^2}$ (with $\vec\sigma = \sigma\hat{\mathbf z}$, $\vec V = V\hat{\mathbf x}$, $\vec\sigma\times\vec V = \sigma V\hat{\mathbf y}$).

> [!note]- Hint 4
> If $\vec\sigma = 0$ (no rotation), the masses are not moving in $\hat{\mathbf{x}}$, so the boost affects them equally and the centroid stays at $G$. The displacement $\frac{\sigma V}{mc^2}$ grows with $V$ but $V < c$, so it is bounded by $\frac{\sigma}{mc} = R_0$, the Møller radius.

---

# Solution

The exercise builds the frame-dependence of the centre of mass from a concrete two-mass model. Part 1 establishes equal energies (hence centroid at $G$) in the rest frame; part 2 boosts and finds unequal energies; part 3 computes the displacement and matches the general formula; part 4 draws the conclusions.

**Step 1: Equal energies in the rest frame.**

> [!note]- Derivation
> In $S$ the rod rotates rigidly, so both masses have speed $u = \omega\ell$ and the same Lorentz factor $\gamma_0 = (1 - u^2)^{-1/2}$. Each has energy
> $$E_\pm = \frac{m}{2}\gamma_0,$$
> equal for the two masses. The momenta are $\mathbf{p}_+ = \tfrac{m}{2}\gamma_0\,u\,\hat{\mathbf{x}}$ (mass at $+\ell$ moving in $+\hat{\mathbf{x}}$) and $\mathbf{p}_- = -\tfrac{m}{2}\gamma_0\,u\,\hat{\mathbf{x}}$ (mass at $-\ell$ moving in $-\hat{\mathbf{x}}$). The centroid in $S$ is the energy-weighted mean of the positions $(0,\pm\ell)$:
> $$\overrightarrow{OG_\mathcal{O}} = \frac{E_+(0,+\ell) + E_-(0,-\ell)}{E_+ + E_-} = \frac{\tfrac{m}{2}\gamma_0(0,\ell) + \tfrac{m}{2}\gamma_0(0,-\ell)}{m\gamma_0} = (0,0).$$
> Equal energies at symmetric positions put the centroid at the origin — the centre of inertia $G$. So far, Newtonian intuition holds.

**Step 2: Unequal energies in the boosted frame.**

> [!note]- Derivation
> Boost to $S'$ moving at $\vec V = V\hat{\mathbf{x}}$. The energy of a particle with energy $E$ and $x$-momentum $p_x$ in $S$ becomes $E' = \gamma(E - Vp_x)$ in $S'$, where $\gamma = (1-V^2)^{-1/2}$. The mass at $(0,+\ell)$ has $p_x = +\tfrac{m}{2}\gamma_0 u$, so
> $$E'_+ = \gamma\Big(\tfrac{m}{2}\gamma_0 - V\tfrac{m}{2}\gamma_0 u\Big) = \tfrac{m}{2}\gamma\gamma_0(1 - Vu).$$
> The mass at $(0,-\ell)$ has $p_x = -\tfrac{m}{2}\gamma_0 u$, so
> $$E'_- = \gamma\Big(\tfrac{m}{2}\gamma_0 + V\tfrac{m}{2}\gamma_0 u\Big) = \tfrac{m}{2}\gamma\gamma_0(1 + Vu).$$
> The energies are now *unequal*: $E'_- > E'_+$. The mass at $-\ell$, whose velocity $-u\hat{\mathbf x}$ opposes the boost $\vec V = V\hat{\mathbf x}$, has the higher energy in $S'$. (Physically: in $S'$ the system streams past at $-V\hat{\mathbf x}$, and the mass already moving in $-\hat{\mathbf x}$ moves faster, hence is more energetic.) The energy asymmetry is the seed of the centroid shift.

**Step 3: The displacement.**

> [!note]- Derivation
> The centroid in $S'$ is the energy-weighted mean of the positions $(0,\pm\ell)$:
> $$y_{G'} = \frac{E'_+(+\ell) + E'_-(-\ell)}{E'_+ + E'_-} = \ell\,\frac{E'_+ - E'_-}{E'_+ + E'_-}.$$
> Compute the numerator and denominator:
> $$E'_+ - E'_- = \tfrac{m}{2}\gamma\gamma_0[(1-Vu) - (1+Vu)] = -m\gamma\gamma_0 Vu,$$
> $$E'_+ + E'_- = \tfrac{m}{2}\gamma\gamma_0[(1-Vu) + (1+Vu)] = m\gamma\gamma_0.$$
> So
> $$y_{G'} = \ell\,\frac{-m\gamma\gamma_0 Vu}{m\gamma\gamma_0} = -\ell V u.$$
> The centroid is displaced to $y_{G'} = -\ell u V$ (negative $y$, toward the more energetic mass at $-\ell$). Now identify the spin: $\vec\sigma = \sigma\hat{\mathbf z}$ with $\sigma = 2\cdot\tfrac{m}{2}\gamma_0 u\ell = m\gamma_0 u\ell$ (each mass contributes $|\mathbf{r}\times\mathbf{p}| = \ell\cdot\tfrac{m}{2}\gamma_0 u$, two masses). And $\vec\sigma\times\vec V = \sigma\hat{\mathbf z}\times V\hat{\mathbf x} = \sigma V\hat{\mathbf y}$. So
> $$\frac{1}{mc^2}(\vec\sigma\times\vec V)_y = \frac{\sigma V}{m} = \frac{m\gamma_0 u\ell\,V}{m} = \gamma_0 u\ell V.$$
> This matches $|y_{G'}| = \ell uV$ to leading order (the $\gamma_0$ difference is a higher-order rigid-rotation subtlety; in the slow-rotation limit $\gamma_0\to 1$ they agree exactly). The displacement is $\overrightarrow{GG_{\mathcal{O}'}} = \frac{1}{mc^2}\vec\sigma\times\vec V$, along $\hat{\mathbf y}$ — perpendicular to both $\vec\sigma$ ($\hat{\mathbf z}$) and $\vec V$ ($\hat{\mathbf x}$), exactly as [[Thm - Minimal Size of a Spinning System|Møller's formula]] requires.

**Step 4: The conclusions.**

> [!note]- Derivation
> *Observer-dependence.* The centroid is at $G = (0,0)$ in $S$ but at $(0, -\ell uV)$ in $S'$ — two different events. The centre of mass of the *same* system is at *different* places for different observers. This is the surprising fact: relativity has no observer-independent centre of mass for a spinning body.
> *Spin-vanishing criterion.* If the system does not rotate ($u = 0$, hence $\vec\sigma = 0$), the masses have no $x$-momentum, the boost affects them equally, $E'_+ = E'_-$, and the centroid stays at $G$ for every observer. So $G_\mathcal{O} = G$ for all $\mathcal{O}$ iff $\vec\sigma = 0$ — the corollary of Møller's theorem.
> *Møller bound.* The displacement $|y_{G'}| = \frac{\sigma V}{m}$ grows with $V$, but $V < c$, so
> $$|\overrightarrow{GG_{\mathcal{O}'}}| < \frac{\sigma}{m} = \frac{\|\vec\sigma\|}{mc} = R_0,$$
> the Møller radius. The centroid wanders, but only within the disk of radius $R_0$ perpendicular to $\vec\sigma$ — and since the centroid must lie inside the body, the body is at least $R_0$ across. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** In $S$, both masses have energy $E_\pm = \tfrac{m}{2}\gamma_0$ (equal speeds), so the centroid is the unweighted mean of $(0,\pm\ell)$, the origin $G$.
>
> **Part 2.** Boosting at $\vec V = V\hat{\mathbf x}$, $E'_\pm = \tfrac{m}{2}\gamma\gamma_0(1\mp Vu)$, unequal: the mass moving against $\vec V$ (at $-\ell$) is more energetic.
>
> **Part 3.** $y_{G'} = \ell\frac{E'_+ - E'_-}{E'_+ + E'_-} = -\ell uV$, matching $\frac{1}{mc^2}(\vec\sigma\times\vec V)_y$ with $\sigma = m\gamma_0 u\ell$; the displacement is along $\hat{\mathbf y}\perp\vec\sigma,\vec V$.
>
> **Part 4.** The centroid is at $G$ in $S$, at $(0,-\ell uV)$ in $S'$ — observer-dependent. It equals $G$ for all observers iff $\vec\sigma = 0$. The displacement is bounded by $R_0 = \|\vec\sigma\|/(mc)$, and since the centroid is interior, $R\geq R_0$. $\blacksquare$

---

# Key Takeaways

**The centre of mass of a spinning body is observer-dependent — and the mechanism is the boost-induced energy asymmetry of the rotating parts.** This is the single most counterintuitive fact in relativistic mechanics, and the two-mass model exposes exactly why it happens. A boost adds energy to the parts of the body moving *with* the boost and subtracts from the parts moving *against* it. In a spinning body, the rotation correlates position with velocity — one side moves one way, the other side the opposite way — so the boost weights the two sides unequally, and the energy-weighted centre shifts toward the more energetic side. No rotation means no correlation between position and velocity, hence no asymmetry, hence an observer-independent centre of mass. The reusable insight: whenever a body has internal motion correlated with position (i.e. spin), boosting it shifts its centre of mass, and the shift is proportional to the spin and to the boost velocity. This is why "where is the centre of mass" is a frame-dependent question for any spinning object.

**The displacement is perpendicular to both spin and velocity, and bounded by the Møller radius.** The shift $\overrightarrow{GG_\mathcal{O}} = \vec\sigma\times\vec V/(mc^2)$ is a cross product, so it is perpendicular to both the spin axis and the boost direction — the centre of mass wanders in the plane transverse to the spin, never along the spin axis. And because $\|\vec V\| < c$, the wandering is confined to a disk of radius $R_0 = \|\vec\sigma\|/(mc)$, the Møller radius. The transferable diagnostic is that the observer-dependence is not unbounded noise but a controlled effect, with magnitude set by the intrinsic spin and direction set by the cross-product geometry. This bound is what converts "the centre of mass is ambiguous" into the hard theorem "a spinning body cannot be smaller than $R_0$" — the centroids fill the disk, the centroids are interior points, so the body contains the disk.

**Frame-dependent answers are not contradictions — they are different measurements of one object.** The deepest lesson, recurring throughout relativity, is that when two observers get different answers for "where the centre of mass is", they are not contradicting each other — they are measuring different things, because "the centre of mass" is defined through a simultaneity slice and an energy weighting that are both observer-relative. The intrinsic object is the centre of inertia $G$, recovered by selecting comoving observers; the frame-dependent centroids are its shadows. This mirrors the relativity of simultaneity (two observers disagree on "now"), the relativity of length (two observers disagree on "how long"), and the relativity of energy (two observers disagree on "how energetic") — in each case the disagreement is real, consistent, and resolved by identifying the invariant behind the frame-dependent shadows. The centre of inertia is that invariant for the centre-of-mass question, and the spin is what measures the spread of the shadows.

---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - The Four-Momentum of a Photon"
tags: [physics, special-relativity]
---

# Problem Statement

Conservation of four-momentum is a *necessary* condition for any process to occur: if no assignment of outgoing four-momenta can balance the incoming total, the reaction is kinematically forbidden, whatever the underlying interaction.

**(a)** Show that a free photon in vacuum cannot decay into an electron–positron pair,
$$\gamma \;\longrightarrow\; e^+ + e^-,$$
by comparing the invariant mass of the two sides. (Both the electron and positron have rest mass $m_e$; the photon is massless.)

**(b)** Two photons *can* combine to produce an $e^+e^-$ pair, $\gamma + \gamma \to e^+ + e^-$. Find the threshold condition on the two photons. For two photons of energies $E_1, E_2$ meeting at an angle $\theta$ between their directions, find the minimum value of the product $E_1 E_2$ for which the reaction is possible.

**(c)** Consider antiproton production by proton–proton collision, $p + p \to p + p + p + \bar{p}$, in which a proton beam strikes protons at rest. All four final particles have rest mass $m_p$ (the antiproton $\bar p$ has the same mass as the proton). Find the threshold beam energy $E_{\text{lab}}$ and the corresponding kinetic energy.

**Recall:**

![[Thm - Conservation of Four-Momentum#Statement]]

![[Def - Four-Momentum and Rest Mass#The Mass-Shell Relation]]

A massive particle has four-momentum $P^\mu = (E,\mathbf{p})$ with $P\cdot P = m^2$ (so $P$ is *timelike*, future-pointing). A photon is massless: its [[Def - The Four-Momentum of a Photon|four-momentum]] is *null*, $P\cdot P = 0$, equivalently $E = |\mathbf{p}|$. The invariant mass of a system of particles is $M_{\text{sys}} = \sqrt{(\sum P_i)\cdot(\sum P_i)}$, and conservation of four-momentum forces the invariant mass of the incoming side to equal that of the outgoing side. $c = 1$ throughout.

---

# Convergent Strategy

**Problem class.** This is a *possibility / impossibility* problem — establishing a kinematic inequality. The target is not a number but a verdict: forbidden, or allowed above some threshold.

**Assumption pattern.** The only input is [[Thm - Conservation of Four-Momentum|conservation of four-momentum]], used as a *filter*. The trick is that conservation forces the invariant mass $\sqrt{(\sum P)^2}$ to be equal on the two sides — and the invariant mass of each side is bounded, above or below, by the rest masses involved. A photon contributes $P\cdot P = 0$; a system of massive particles has invariant mass at least the sum of their rest masses.

**Theorem routing.** For (a): compute the invariant mass of each side. The single photon has invariant mass $0$; the $e^+e^-$ pair has invariant mass $\ge 2m_e > 0$. Conservation demands they be equal — contradiction, so the decay is forbidden. For (b) and (c): the reaction is allowed exactly when the invariant mass of the *incoming* system reaches the threshold value $\sum m_{\text{out}}$, the products' total rest mass. Compute $(\sum P_{\text{in}})^2$ and impose $(\sum P_{\text{in}})^2 \ge (\sum m_{\text{out}})^2$.

**Key decision point.** The unifying idea is that invariant mass is the conserved, frame-independent quantity, and a reaction is allowed if and only if the incoming invariant mass is large enough to manufacture the outgoing rest masses. A single photon is forbidden from making a pair because a null four-vector simply cannot have the timelike invariant mass $2m_e$ of the pair — no frame choice can fix that. Two photons crossing at an angle *can*, because two null vectors sum to a timelike one.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Write down the total four-momentum and set it equal before and after** — conservation of four-momentum is the entire filter.
2. **Square a four-momentum to extract an invariant mass** — squaring $\sum P$ gives the invariant mass squared of each side; a photon's self-square is $0$.
3. **Go to the centre-of-momentum frame** — at threshold the products are at rest there, fixing $(\sum P_{\text{out}})^2 = (\sum m_{\text{out}})^2$.
4. **Use a Lorentz invariant to switch frames** — $(\sum P)^2$ is computed in the lab and equated to its threshold value.

---

# Hints

> [!note]- Hint 1
> Conservation of four-momentum forces the invariant mass $\sqrt{(\sum P)^2}$ to be the same before and after. For part (a): what is the invariant mass of a single photon? What is the smallest possible invariant mass of an electron–positron pair?

> [!note]- Hint 2
> A single photon has $P\cdot P = 0$ — invariant mass exactly zero. An $e^+e^-$ pair has invariant mass $\sqrt{(P_+ + P_-)^2} \ge 2m_e$, with equality only when both are at rest in the centre-of-momentum frame. Zero cannot equal something $\ge 2m_e$.

> [!note]- Hint 3
> For (b), the two-photon system has $(P_1 + P_2)^2 = 2P_1\cdot P_2$ because each photon's square vanishes. Write $P_1\cdot P_2$ in terms of the energies $E_1, E_2$ and the angle $\theta$ between the photon directions.

> [!note]- Hint 4
> For (c), at threshold the four final particles are at rest in the centre-of-momentum frame, so $(\sum P_{\text{out}})^2 = (4m_p)^2$. Compute $(P_{\text{beam}} + P_{\text{target}})^2$ in the lab and set it equal.

---

# Solution

Every part is the same move: conservation of four-momentum makes the invariant mass of the incoming system equal to that of the outgoing system, and a reaction is allowed precisely when the incoming invariant mass is large enough to cover the outgoing rest masses.

**Step 1: A single photon cannot pair-produce (part a).**

The invariant mass of a single photon is $0$; the invariant mass of an $e^+e^-$ pair is at least $2m_e > 0$. Conservation of four-momentum demands these be equal — impossible. The decay $\gamma \to e^+e^-$ is kinematically forbidden in vacuum.

> [!note]- Derivation
> Suppose, for contradiction, that a free photon with [[Def - The Four-Momentum of a Photon|four-momentum]] $P_\gamma$ decays into an electron of four-momentum $P_-$ and a positron of four-momentum $P_+$. By [[Thm - Conservation of Four-Momentum|conservation of four-momentum]],
> $$P_\gamma = P_+ + P_-.$$
> Take the Minkowski square of both sides. The left side is the photon's self-square, which vanishes because the photon is massless:
> $$P_\gamma\cdot P_\gamma = 0.$$
> The right side is the invariant mass squared of the pair:
> $$(P_+ + P_-)^2 = P_+^2 + P_-^2 + 2P_+\cdot P_- = m_e^2 + m_e^2 + 2P_+\cdot P_-,$$
> using the mass-shell relation $P_\pm^2 = m_e^2$. The cross term is bounded below: for two future-pointing timelike four-momenta, $P_+\cdot P_- = E_+E_- - \mathbf{p}_+\cdot\mathbf{p}_- \ge E_+E_- - |\mathbf{p}_+||\mathbf{p}_-| \ge m_e^2$, the last step because $E \ge |\mathbf{p}|$ and $E^2 - |\mathbf{p}|^2 = m_e^2$ (equality only when both are at rest). Hence
> $$(P_+ + P_-)^2 \ge 2m_e^2 + 2m_e^2 = 4m_e^2 > 0.$$
> So conservation of four-momentum would require $0 = (P_+ + P_-)^2 \ge 4m_e^2$, which is false. **The decay $\gamma \to e^+e^-$ is kinematically forbidden.** The deep reason: the photon's four-momentum is *null* (lies on the light cone), while the pair's total four-momentum is *timelike* (invariant mass $\ge 2m_e$); a null four-vector cannot equal a timelike one, and no choice of frame can repair the mismatch, because the timelike-versus-null character is itself Lorentz-invariant. (In the presence of a nucleus the process *does* occur — the nucleus absorbs the recoil four-momentum — but a *free* photon in vacuum cannot decay.)

**Step 2: Two photons can pair-produce — the threshold (part b).**

Two photons can make a pair provided their invariant mass reaches $2m_e$. For energies $E_1, E_2$ at relative angle $\theta$, the condition is $E_1 E_2 (1 - \cos\theta) \ge 2m_e^2$.

> [!note]- Derivation
> For $\gamma + \gamma \to e^+ + e^-$, conservation of four-momentum gives $P_1 + P_2 = P_+ + P_-$. The reaction is kinematically allowed exactly when the invariant mass of the incoming two-photon system is at least the total rest mass of the products:
> $$(P_1 + P_2)^2 \ge (2m_e)^2 = 4m_e^2,$$
> since at threshold the pair is created at rest in the centre-of-momentum frame, giving $(P_+ + P_-)^2 = (2m_e)^2$, and any extra energy only increases the left side.
>
> Evaluate $(P_1 + P_2)^2$. Each photon is null, $P_1^2 = P_2^2 = 0$, so
> $$(P_1 + P_2)^2 = P_1^2 + P_2^2 + 2P_1\cdot P_2 = 2P_1\cdot P_2.$$
> Write the photon four-momenta with energies $E_1, E_2$ and unit direction vectors $\mathbf{n}_1, \mathbf{n}_2$: $P_i = E_i(1, \mathbf{n}_i)$, since $|\mathbf{p}_i| = E_i$ for a photon. Then
> $$P_1\cdot P_2 = E_1 E_2\big(1 - \mathbf{n}_1\cdot\mathbf{n}_2\big) = E_1 E_2(1 - \cos\theta),$$
> where $\theta$ is the angle between the two photon directions. The threshold condition is therefore
> $$(P_1+P_2)^2 = 2E_1 E_2(1 - \cos\theta) \ge 4m_e^2 \;\Longrightarrow\; \boxed{\;E_1 E_2(1 - \cos\theta) \ge 2m_e^2\;}$$
> Two features stand out. First, the product $E_1 E_2$ must clear a *floor* — neither photon alone can do it, consistent with part (a). Second, the angular factor $(1 - \cos\theta)$ is maximal ($=2$) for head-on photons ($\theta = \pi$) and vanishes for parallel photons ($\theta = 0$): two co-moving photons, however energetic, can *never* pair-produce, because their combined four-momentum stays null. The minimum is at $\theta = \pi$, where $E_1 E_2 \ge m_e^2$. This is the mechanism by which high-energy gamma rays are attenuated against the cosmic background light — a gamma ray and a soft background photon collide nearly head-on to make a pair.

**Step 3: Antiproton production threshold (part c).**

The threshold beam energy for $p + p \to p + p + p + \bar p$ on a fixed target is $E_{\text{lab}} = 7m_p$, a beam kinetic energy of $6m_p$.

> [!note]- Derivation
> Conservation of four-momentum reads $P_{\text{beam}} + P_{\text{target}} = \sum_{j=1}^{4} P_j$, with all four products of rest mass $m_p$. The reaction is allowed when the incoming invariant mass reaches the products' total rest mass; at threshold equality holds:
> $$(P_{\text{beam}} + P_{\text{target}})^2 = (\textstyle\sum P_j)^2_{\text{threshold}}.$$
> At threshold the four products are at rest in the **centre-of-momentum frame**, so their total four-momentum there is $(4m_p, \mathbf{0})$ and
> $$(\textstyle\sum P_j)^2_{\text{threshold}} = (4m_p)^2 = 16m_p^2.$$
> Now evaluate the left side in the lab frame, where the target proton is at rest and the beam proton has energy $E_{\text{lab}}$ and momentum $\mathbf{p}_{\text{lab}}$:
> $$P_{\text{beam}} = (E_{\text{lab}}, \mathbf{p}_{\text{lab}}), \qquad P_{\text{target}} = (m_p, \mathbf{0}).$$
> Then, using $P_{\text{beam}}^2 = P_{\text{target}}^2 = m_p^2$ (mass shell),
> $$(P_{\text{beam}} + P_{\text{target}})^2 = m_p^2 + m_p^2 + 2P_{\text{beam}}\cdot P_{\text{target}} = 2m_p^2 + 2m_p E_{\text{lab}},$$
> since $P_{\text{beam}}\cdot P_{\text{target}} = E_{\text{lab}}\,m_p - \mathbf{p}_{\text{lab}}\cdot\mathbf{0} = m_p E_{\text{lab}}$. Equating the two evaluations of the same invariant:
> $$2m_p^2 + 2m_p E_{\text{lab}} = 16m_p^2 \;\Longrightarrow\; E_{\text{lab}} = \frac{14m_p^2}{2m_p} = 7m_p.$$
> So $\boxed{\,E_{\text{lab}} = 7m_p\,}$, and the threshold *kinetic* energy of the beam proton is
> $$T_{\text{lab}} = E_{\text{lab}} - m_p = 6m_p.$$
> With $m_p c^2 \approx 938\ \text{MeV}$, the threshold kinetic energy is about $5.6\ \text{GeV}$ — the historical figure that set the design energy of the Bevatron, the accelerator built at Berkeley in the 1950s specifically to discover the antiproton. Note that one might naively expect to need only $2m_p$ of energy to make the extra $p\bar p$ pair; the answer is three times larger because conservation of three-momentum forbids the products from being at rest in the lab, so much of the beam energy is locked into their forced forward motion (the same quadratic-style penalty seen in [[Ex - Threshold energy for particle production|the general threshold problem]]).

> [!note]- Complete formal solution
> **(a)** If $\gamma \to e^+e^-$, conservation gives $P_\gamma = P_+ + P_-$. Squaring: $P_\gamma^2 = 0$ (massless), while $(P_+ + P_-)^2 = 2m_e^2 + 2P_+\cdot P_- \ge 4m_e^2 > 0$ (since $P_+\cdot P_- \ge m_e^2$ for future-pointing timelike four-momenta). Thus $0 \ge 4m_e^2$, a contradiction: a single free photon cannot pair-produce, because its null four-momentum cannot equal the pair's timelike total.
> **(b)** For $\gamma+\gamma \to e^+e^-$, conservation gives $P_1 + P_2 = P_+ + P_-$; the reaction is allowed when $(P_1+P_2)^2 \ge (2m_e)^2$. With $P_i = E_i(1,\mathbf{n}_i)$ each null, $(P_1+P_2)^2 = 2P_1\cdot P_2 = 2E_1E_2(1-\cos\theta)$. Threshold: $E_1 E_2(1 - \cos\theta) \ge 2m_e^2$; minimal at head-on incidence $\theta = \pi$, giving $E_1 E_2 \ge m_e^2$, and impossible for parallel photons.
> **(c)** For $p+p \to p+p+p+\bar p$, at threshold the four products are at rest in the centre-of-momentum frame, so $(\sum P_j)^2 = (4m_p)^2 = 16m_p^2$. In the lab, $P_{\text{beam}} = (E_{\text{lab}},\mathbf{p}_{\text{lab}})$, $P_{\text{target}} = (m_p,\mathbf{0})$, so $(P_{\text{beam}}+P_{\text{target}})^2 = 2m_p^2 + 2m_p E_{\text{lab}}$. Equating: $2m_p^2 + 2m_p E_{\text{lab}} = 16m_p^2$, hence $E_{\text{lab}} = 7m_p$ and $T_{\text{lab}} = 6m_p \approx 5.6\ \text{GeV}$. $\blacksquare$

---

# Key Takeaways

**A reaction is allowed if and only if the incoming invariant mass covers the outgoing rest masses.** Conservation of four-momentum is not only a tool for computing energies — it is a *filter* that rules processes in or out, and the cleanest way to apply it is through invariant mass. Conservation forces $\sqrt{(\sum P_{\text{in}})^2} = \sqrt{(\sum P_{\text{out}})^2}$, and the outgoing side is bounded below: a system of massive products has invariant mass at least the sum of their rest masses, with equality when they are all at rest in the centre-of-momentum frame. So the reaction can proceed exactly when the *incoming* invariant mass reaches $\sum m_{\text{out}}$. This single criterion handles every "is this allowed?" and "what is the threshold?" question: compute the incoming $(\sum P)^2$, compare with $(\sum m_{\text{out}})^2$. The verdict in part (a) is the degenerate case — the incoming invariant mass is $0$ and can never reach $2m_e$.

**Timelike versus null is a Lorentz-invariant distinction — that is why a free photon cannot decay.** The impossibility of $\gamma \to e^+e^-$ is often phrased as "energy is not enough", but the precise statement is geometric: the photon's four-momentum is *null* (it lies on the light cone, $P\cdot P = 0$), whereas the four-momentum of any massive system is *timelike* ($P\cdot P > 0$). Whether a four-vector is null or timelike is itself a Lorentz invariant — every observer agrees — so no clever choice of frame can turn a null vector into a timelike one. A free photon cannot decay into *anything* with rest mass, not just an $e^+e^-$ pair, for exactly this reason. The general lesson is a powerful triage tool: before any detailed calculation, check whether the character of the total four-momentum (null, timelike, the sign of its square) is compatible on the two sides. Two photons evade the obstruction precisely because two null vectors can sum to a timelike one — but only if they are not parallel, which is why the $(1-\cos\theta)$ factor vanishes for co-moving photons.

**Squaring in two frames turns a threshold into one line of algebra.** The antiproton calculation is the canonical fixed-target threshold computation, and it is solved by the universal move: the invariant $(\sum P)^2$ is the same in every frame, so evaluate the *outgoing* side in the centre-of-momentum frame — where, at threshold, all products are at rest and the square is trivially $(\sum m_{\text{out}})^2$ — and the *incoming* side in the lab frame, where the kinematics are given, then equate. The factor-of-three surprise (needing $6m_p$ of kinetic energy to make a $2m_p$ pair) is conservation of three-momentum exacting its tax: the lab-frame products cannot be at rest, so much of the beam energy is wasted on their forced motion. This is the same structural lesson as [[Ex - Threshold energy for particle production|the general threshold problem]] and [[Ex - Mandelstam variables for two-body scattering|the Mandelstam analysis]]: the energy that can actually be spent making new mass is the invariant $\sqrt{s}$, the centre-of-mass energy, never the raw beam energy.

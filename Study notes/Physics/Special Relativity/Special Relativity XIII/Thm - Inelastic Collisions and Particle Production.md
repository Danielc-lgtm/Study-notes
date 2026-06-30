---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ but restore it where instructive, with $\eta = \operatorname{diag}(+1,-1,-1,-1)$. Incoming particles $\mathcal{P}_1, \mathcal{P}_2$ of masses $m_1, m_2$ and [[Def - Four-Momentum and Rest Mass|four-momenta]] $P_1, P_2$ produce outgoing particles $\mathcal{P}_1', \ldots, \mathcal{P}_N'$ of masses $m_a'$. The total four-momentum is $P = P_1 + P_2$, its invariant mass $m = \sqrt{P\cdot P}$ (the **Mandelstam** $s = m^2$). "Lab frame" has $\mathcal{P}_2$ at rest; "centre-of-momentum frame" (denoted by a star) has zero total spatial momentum. $E_1$ is the lab energy of $\mathcal{P}_1$; $m_{\text{thres}} = \sum_a m_a'$. Full registry on [[Special Relativity XIII — Energy and Momentum]].

---

# Statement

> **Threshold for an inelastic reaction.** Consider an inelastic collision $\mathcal{P}_1 + \mathcal{P}_2 \to \mathcal{P}_1' + \cdots + \mathcal{P}_N'$ of an isolated system. By [[Thm - Conservation of Four-Momentum|conservation of four-momentum]], the reaction is **kinematically possible if and only if** the invariant mass of the incoming system reaches the sum of the product masses:
> $$\boxed{\ m = \sqrt{(P_1+P_2)\cdot(P_1+P_2)} \;\ge\; m_{\text{thres}} := \sum_{a=1}^N m_a'\ }.$$
> At **threshold** ($m = m_{\text{thres}}$) all the products are at rest in the centre-of-momentum frame (no energy is "wasted" on their relative motion).

> **Fixed-target threshold.** When $\mathcal{P}_2$ is at rest in the lab, the criterion becomes a condition on the energy $E_1$ of the projectile:
> $$E_1 \;\ge\; \frac{m_{\text{thres}}^2 - m_1^2 - m_2^2}{2\,m_2}\qquad\big(\text{with } c:\ E_1 \ge \tfrac{(m_{\text{thres}}^2 - m_1^2 - m_2^2)c^2}{2m_2}\big),$$
> which grows as the **square** of $m_{\text{thres}}$. In a **collider** (centre-of-momentum frame is the lab) the required energy grows only **linearly** with $m_{\text{thres}}$ — for equal-mass beams, each needs energy $\tfrac12 m_{\text{thres}}$ — which is why colliders, not fixed targets, are used to reach high masses.

> **Forbidden reactions.** A reaction whose two sides have four-momenta of incompatible causal character is forbidden in every frame. In particular a single photon cannot decay or pair-produce in vacuum: a null four-momentum cannot equal the timelike sum of massive four-momenta.

---

# Motivation

Conservation of four-momentum forbids some reactions outright and permits others only above a minimum energy, and this theorem is the precise statement of both. The physics is mass–energy equivalence in action: to create new particles you must supply, as kinetic energy of the colliding partners, at least enough to build the rest masses of the products. But "at least enough" is subtler than it looks, because conservation of *momentum* forbids the products from being created at rest in the lab — they must carry away the incoming momentum, and that unavoidable kinetic energy is energy *not* available for making mass. The theorem disentangles this and gives the exact threshold.

The governing idea, and the one to internalise, is that the available energy is a Lorentz invariant: the **invariant mass** $m = \sqrt{(P_1+P_2)^2}$ of the colliding system, which in the centre-of-momentum frame is simply the total energy there (all momentum cancels). A reaction is possible exactly when this invariant mass reaches the sum of the product masses — because at threshold the products sit at rest in the centre-of-momentum frame, where the total four-momentum is $(\sum m_a', \mathbf{0})$ and its invariant mass is $\sum m_a'$. Evaluating the *same* invariant in the lab frame, where the kinematics are given, then converts this into a condition on the projectile energy. This two-frame evaluation of one invariant — compute it where it is simple (centre-of-momentum, at threshold), equate to its value where the data live (lab) — is the master technique of threshold problems.

The practical consequence is the *raison d'être* of particle colliders. In a fixed-target experiment the required beam energy grows as the square of the mass you want to create, because most of the beam energy goes into the kinetic energy of the recoiling products. In a collider, where two beams meet head-on so that the lab *is* the centre-of-momentum frame, no energy is wasted on net motion and the required energy grows only linearly. To reach the LHC's available energy of $14$ TeV with a fixed target, one would need a single proton at about $10^5$ TeV — physically impossible. The whole engineering of two counter-rotating beams is the realisation of "make the lab the centre-of-momentum frame so that no energy is wasted on motion of the products". The antiproton was discovered this way (the Bevatron, $6.2$ GeV protons on a fixed target, reaching the $6.57$ GeV threshold for $p + p \to p + p + p + \bar p$), and the contrast between fixed-target and collider thresholds is the lesson that built every modern accelerator.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "an inelastic reaction whose feasibility or threshold is asked", and input-broadening is about recognising reaction-feasibility questions.

The first disguised source is **"can this reaction happen?"** — a yes/no question about a proposed process. The answer is "yes iff the incoming invariant mass reaches $\sum m_a'$", or, for incompatible causal character, an outright "no". The bridge is conservation of four-momentum constraining the total. *Example problem:* whether a single photon can pair-produce ([[Ex - Whether a particle reaction is kinematically allowed]]).

The second disguised source is **"what is the minimum energy to produce particle X?"** — the threshold question. The criterion $E_1 \ge (m_{\text{thres}}^2 - m_1^2 - m_2^2)/2m_2$ gives it for a fixed target. The bridge is the two-frame evaluation of the invariant $s$. *Example problem:* the antiproton-production threshold $E_1 \ge 7m_p$ ([[Ex - Threshold energy for particle production]]).

The third disguised source is **"a high-energy projectile hits a low-energy background"** — the astrophysical setting. A cosmic-ray proton on a CMB photon, or a gamma-ray on a starlight photon, is an inelastic reaction whose threshold determines whether pions or pairs are produced. The bridge is the general (non-fixed-target) threshold $E_1 E_2 - \mathbf{p}_1\cdot\mathbf{p}_2 \ge \tfrac12(m_{\text{thres}}^2 - m_1^2 - m_2^2)$. *Example problem:* the GZK cutoff and pion photoproduction on the CMB ([[Ex - Inverse Compton scattering and the GZK cutoff]]).

**Targets (Output Amplification)**

The conclusions are the invariant-mass threshold, the fixed-target energy threshold, and the forbidden-reaction filter.

Combine the threshold with **the collider-versus-fixed-target contrast**. The fixed-target threshold grows as $m_{\text{thres}}^2$ while the collider threshold grows linearly. The further result is the quantitative case for colliders: the ratio of required energies is roughly $m_{\text{thres}}/m$, enormous for heavy products. The combination is useful because it explains a multi-billion-dollar engineering decision from a one-line kinematic comparison. *Example:* the LHC's $14$ TeV versus the $10^5$ TeV a fixed target would need ([[Ex - Threshold energy for particle production]]).

Combine the forbidden-reaction filter with **the causal character of four-momenta**. A sum of future-timelike four-momenta is timelike; a single photon is null; a null vector cannot equal a timelike one in any frame. The further result is a kinematic *selection rule* — certain reactions are forbidden purely by four-vector character, before any dynamics. The combination is nonobvious because the forbidden reaction (single-photon decay) looks energetically allowed. *Example:* $\gamma \not\to e^+e^-$, requiring a third body ([[Ex - Whether a particle reaction is kinematically allowed]]).

Combine the threshold with **mass–energy equivalence**. The threshold is the statement that the kinetic energy supplied must at least equal the rest energy of the new mass created, $E_{\text{kin}} \ge (\sum m_a' - \sum m_{\text{in}})c^2$ in the centre-of-momentum frame. The further result connects thresholds to the energy balance of [[Thm - Mass-Energy Equivalence|E = mc²]]. The combination is the physical reading: kinetic energy is being converted into rest mass. *Example:* the energy released or absorbed in a nuclear reaction (the $Q$-value).

---

# Why Is It True

The reason is the two-frame evaluation of a single Lorentz invariant, and it is the cleanest argument for thresholds. **The whole theorem is: the available energy is the invariant mass $\sqrt{(P_1+P_2)^2}$, which at threshold equals $\sum m_a'$ because the products are then at rest in the centre-of-momentum frame.**

Start with the invariant $s = (P_1 + P_2)^2 = (P_{\text{total}})^2$. Because $P_{\text{total}}$ is conserved, $s$ is the same before and after the reaction. Evaluate it *after*, in the centre-of-momentum frame, where by definition the total spatial momentum vanishes, so $P_{\text{total}} = (E_{\text{cm}}, \mathbf{0})$ and $s = E_{\text{cm}}^2$. The total centre-of-momentum energy is $E_{\text{cm}} = \sum_a E_a^* \ge \sum_a m_a'$ (each product's energy is at least its rest mass, $E_a^* \ge m_a'$, with equality only when the product is at rest). So $\sqrt{s} = E_{\text{cm}} \ge \sum_a m_a' = m_{\text{thres}}$, and the minimum — threshold — is achieved when *every* product is at rest in the centre-of-momentum frame, $E_a^* = m_a'$. There is no spare kinetic energy at threshold: all the available energy goes into rest mass. Since $\sqrt{s}$ is the invariant mass $m$ of the incoming system, the criterion is $m \ge m_{\text{thres}}$.

Now evaluate the *same* invariant $s$ *before*, in the lab frame, where $\mathcal{P}_2$ is at rest ($P_2 = (m_2, \mathbf{0})$) and $\mathcal{P}_1$ has energy $E_1$:
$$s = (P_1 + P_2)^2 = m_1^2 + m_2^2 + 2P_1\cdot P_2 = m_1^2 + m_2^2 + 2m_2 E_1,$$
using $P_1\cdot P_2 = m_2 E_1$ (the rest-frame electron-style contraction). Setting $s \ge m_{\text{thres}}^2$ and solving for $E_1$ gives $E_1 \ge (m_{\text{thres}}^2 - m_1^2 - m_2^2)/2m_2$. The quadratic dependence on $m_{\text{thres}}$ is now manifest, and it is the reason fixed-target experiments are inefficient: the available energy $\sqrt{s} \approx \sqrt{2m_2 E_1}$ grows only as the *square root* of the beam energy, so doubling the available energy requires *quadrupling* the beam energy.

In a collider the contrast is stark. There the lab *is* the centre-of-momentum frame, so $\sqrt{s} = E_1 + E_2$ directly (for two beams), and reaching $\sqrt{s} = m_{\text{thres}}$ needs only $E_1 + E_2 = m_{\text{thres}}$ — linear growth. The deep statement is that $s = (P_{\text{total}})^2$ measures the energy *available* for the reaction, and it equals the lab energy only when the momenta cancel; in a fixed-target experiment the un-cancelled momentum carries away energy that cannot be used.

For the forbidden reactions, the mechanism is the causal character of four-momenta. A single photon has a *null* four-momentum, $P_\gamma\cdot P_\gamma = 0$. The proposed products $e^+ e^-$ have four-momenta whose sum is *timelike*: each is future-directed timelike, and the sum of future-directed timelike vectors is future-directed timelike with $(P_{e^+} + P_{e^-})^2 > 0$ (strictly, unless they are parallel, which massive particles' four-momenta cannot be while distinct). A null vector can never equal a timelike one — their Minkowski squares ($0$ versus $> 0$) differ, and the Minkowski square is frame-independent — so conservation $P_\gamma = P_{e^+} + P_{e^-}$ cannot hold in any frame. Equivalently, in the would-be centre-of-momentum frame of the pair the photon would have to be at rest, which no photon can be. A third body (a nucleus) supplies the four-momentum to balance the books, allowing $\gamma + p \to p + e^+ + e^-$.

---

# What Makes This Hard

The conceptual hurdle is understanding *why* the products are at rest in the centre-of-momentum frame at threshold — it is because any relative motion of the products would require extra energy beyond their rest masses, so the minimum-energy configuration has them all stationary in that frame. The non-obvious step is evaluating the *same* invariant $s$ in two frames (centre-of-momentum, where it is $E_{\text{cm}}^2$, and lab, where it is $m_1^2 + m_2^2 + 2m_2 E_1$) and equating; students often try to work entirely in the lab frame and get tangled in the products' momenta. The most common error is forgetting that the fixed-target threshold grows as $m_{\text{thres}}^2$, not linearly — intuiting (wrongly) that creating a particle of mass $M$ just needs beam kinetic energy $M$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use the invariance of $s = (P_1+P_2)^2$. Evaluate it after the reaction in the centre-of-momentum frame (at threshold, products at rest, $s = m_{\text{thres}}^2$); evaluate it before in the lab ($s = m_1^2 + m_2^2 + 2m_2 E_1$); equate to get the threshold energy. For forbidden reactions, compare the causal character of the two sides' four-momenta.

**Subgoal decomposition:**

1. **Invariant mass threshold.** Evaluate $s = (\sum P_{\text{out}})^2$ in the centre-of-momentum frame; at threshold all products are at rest, $\sum P_{\text{out}} = (\sum m_a', \mathbf{0})$, so $s = m_{\text{thres}}^2$.
   - *Hint:* In the centre-of-momentum frame the total momentum vanishes; minimum energy means products at rest.
   - *Why needed:* It gives the invariant criterion $m = \sqrt{s} \ge m_{\text{thres}}$.

2. **Lab-frame evaluation.** Evaluate $s = (P_1 + P_2)^2$ in the lab with $\mathcal{P}_2$ at rest: $s = m_1^2 + m_2^2 + 2m_2 E_1$.
   - *Hint:* $P_1\cdot P_2 = m_2 E_1$ when $P_2 = (m_2, \mathbf{0})$.
   - *Why needed:* It converts the invariant criterion into a condition on the lab energy $E_1$.

3. **Solve for the threshold energy.** Set $m_1^2 + m_2^2 + 2m_2 E_1 \ge m_{\text{thres}}^2$ and solve for $E_1$.
   - *Hint:* Linear in $E_1$; isolate it.
   - *Why needed:* It gives $E_1 \ge (m_{\text{thres}}^2 - m_1^2 - m_2^2)/2m_2$, quadratic in $m_{\text{thres}}$.

4. **Forbidden reactions.** Compare $(P_{\text{in}})^2$ and $(P_{\text{out}})^2$ — if one is null and the other timelike, the reaction is impossible.
   - *Hint:* A null four-momentum cannot equal a timelike one in any frame.
   - *Why needed:* It is the kinematic selection rule, e.g. $\gamma\not\to e^+e^-$.

---

# Lemma Decomposition

> [!note]- Lemma 1: At threshold the products are at rest in the centre-of-momentum frame
> **Statement:** The minimum total energy $\sqrt{s}$ for which the products can exist is $\sum_a m_a'$, achieved when all products are at rest in the centre-of-momentum frame.
>
> **Hint:** In the centre-of-momentum frame $\sqrt{s} = \sum_a E_a^*$ with $E_a^* \ge m_a'$.
>
> **Why needed:** It identifies the threshold configuration and gives $s = m_{\text{thres}}^2$.
>
> > [!note]- Full proof
> > In the centre-of-momentum frame the total spatial momentum vanishes, so $P_{\text{total}} = (E_{\text{cm}}, \mathbf{0})$ and $s = P_{\text{total}}\cdot P_{\text{total}} = E_{\text{cm}}^2$. The total energy is $E_{\text{cm}} = \sum_a E_a^*$, and each product satisfies $E_a^* = \sqrt{m_a'^2 + |\mathbf{p}_a^*|^2} \ge m_a'$, with equality iff $\mathbf{p}_a^* = 0$. Hence $E_{\text{cm}} \ge \sum_a m_a' = m_{\text{thres}}$, so $\sqrt{s} \ge m_{\text{thres}}$, and the minimum is attained when every $\mathbf{p}_a^* = 0$, i.e. all products at rest in the centre-of-momentum frame. At threshold $s = m_{\text{thres}}^2$. $\blacksquare$

> [!note]- Lemma 2: The lab-frame value of the invariant $s$
> **Statement:** With $\mathcal{P}_2$ at rest in the lab and $\mathcal{P}_1$ of energy $E_1$, $s = (P_1+P_2)^2 = m_1^2 + m_2^2 + 2m_2 E_1$.
>
> **Hint:** Expand the square and use $P_2 = (m_2, \mathbf{0})$ so $P_1\cdot P_2 = m_2 E_1$.
>
> **Why needed:** It expresses the invariant in lab-frame data, converting the threshold to a condition on $E_1$.
>
> > [!note]- Full proof
> > $s = (P_1 + P_2)\cdot(P_1 + P_2) = P_1\cdot P_1 + 2P_1\cdot P_2 + P_2\cdot P_2 = m_1^2 + 2P_1\cdot P_2 + m_2^2$. With $\mathcal{P}_2$ at rest, $P_2 = (m_2, \mathbf{0})$, so $P_1\cdot P_2 = E_1 m_2 - \mathbf{p}_1\cdot\mathbf{0} = m_2 E_1$. Hence $s = m_1^2 + m_2^2 + 2m_2 E_1$. $\blacksquare$

> [!note]- Lemma 3: A null four-momentum cannot equal a timelike one
> **Statement:** If $A\cdot A = 0$ (null) and $B\cdot B > 0$ (timelike), then $A \ne B$ in every frame.
>
> **Hint:** The Minkowski square is frame-independent.
>
> **Why needed:** It is the kinematic selection rule forbidding single-photon pair production and decay.
>
> > [!note]- Full proof
> > If $A = B$ then $A\cdot A = B\cdot B$. But $A\cdot A = 0$ and $B\cdot B > 0$, a contradiction. Since the Minkowski square is a Lorentz scalar (the same in every frame), the inequality $A\cdot A \ne B\cdot B$ holds in all frames, so $A \ne B$ in all frames. Applied to $A = P_\gamma$ (null) and $B = P_{e^+} + P_{e^-}$ (timelike, as a sum of future-directed timelike four-momenta), this forbids $P_\gamma = P_{e^+} + P_{e^-}$, i.e. $\gamma\not\to e^+e^-$ in vacuum. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Threshold criterion.** By [[Thm - Conservation of Four-Momentum|conservation of four-momentum]], the total four-momentum $P_{\text{total}} = P_1 + P_2$ is conserved, so the invariant $s = P_{\text{total}}\cdot P_{\text{total}}$ has the same value before and after. By Lemma 1, evaluating $s$ after the reaction in the centre-of-momentum frame, the minimum value consistent with producing the rest masses $m_a'$ is $s = m_{\text{thres}}^2 = (\sum_a m_a')^2$, attained with all products at rest there. Hence the reaction is possible iff the incoming invariant mass satisfies
> $$m = \sqrt{s} = \sqrt{(P_1+P_2)^2} \ge m_{\text{thres}} = \sum_a m_a'.$$
>
> **Fixed-target threshold.** By Lemma 2, evaluating $s$ in the lab with $\mathcal{P}_2$ at rest gives $s = m_1^2 + m_2^2 + 2m_2 E_1$. Setting $s \ge m_{\text{thres}}^2$ and solving,
> $$E_1 \ge \frac{m_{\text{thres}}^2 - m_1^2 - m_2^2}{2m_2},$$
> quadratic in $m_{\text{thres}}$. For a collider (lab = centre-of-momentum frame) the same invariant is $s = (E_1 + E_2)^2$, so $\sqrt{s} = E_1 + E_2 \ge m_{\text{thres}}$ is *linear* in $m_{\text{thres}}$; for equal-mass beams each needs energy $\tfrac12 m_{\text{thres}}$.
>
> **Forbidden reactions.** By Lemma 3, a reaction whose incoming and outgoing total four-momenta have different causal character (one null, one timelike) is impossible in every frame; in particular a single photon ($P_\gamma\cdot P_\gamma = 0$) cannot decay or pair-produce in vacuum, since the products' total four-momentum is timelike. A third body restores conservation. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Accelerator design — the collider imperative.** The quadratic ($m_{\text{thres}}^2$) growth of the fixed-target threshold versus the linear ($m_{\text{thres}}$) growth of the collider threshold is the kinematic argument that built every modern collider: to reach $14$ TeV of available energy at the LHC with a fixed target would require a single proton at $\sim 10^5$ TeV. The application is a direct comparison of the two thresholds; see [[Ex - Threshold energy for particle production]].

**Astrophysics — the GZK cutoff.** A cosmic-ray proton above $\sim 6\times10^{19}$ eV exceeds the threshold for pion photoproduction on the cosmic microwave background, $\gamma_{\text{CMB}} + p \to \pi^0 + p$, and so loses energy over $\sim 100$ Mpc; this truncates the observed cosmic-ray spectrum (the GZK cutoff, confirmed 2008). The application uses the general (non-fixed-target) threshold with a low-energy photon target; see [[Ex - Inverse Compton scattering and the GZK cutoff]].

**Nuclear physics — the reaction $Q$-value.** Whether a nuclear reaction is exothermic or endothermic, and its threshold if endothermic, is the same invariant-mass calculation: the reaction is possible iff the incoming invariant mass reaches the products' total mass, and the $Q$-value is the rest-mass difference times $c^2$. The application carries the particle-physics threshold into nuclear physics; the energy balance is mass–energy equivalence, $Q = (\sum m_{\text{in}} - \sum m_{\text{out}})c^2$.

---

# Bridges

- **[[Thm - Conservation of Four-Momentum]]** — the threshold criterion is conservation of four-momentum read through the invariant $s = (P_{\text{total}})^2$, which is conserved and so can be evaluated in any frame. The two-frame evaluation (centre-of-momentum at threshold, lab for the data) is the conservation law's most powerful application.

- **[[Thm - Mass-Energy Equivalence]]** — the threshold is mass–energy equivalence as a budget: the kinetic energy supplied (in the centre-of-momentum frame) must at least equal the rest energy of the new mass created. The non-additivity of mass is why the available energy is the invariant mass $\sqrt{s}$, not the sum of beam energies.

- **The Mandelstam variable $s$ and collider physics** — the invariant $s = (P_1+P_2)^2$ is the first Mandelstam variable, equal to the centre-of-mass energy squared $E_{\text{cm}}^2$; it is the single most important number characterising a collision, the "$\sqrt{s}$" that headlines every collider. Its quadratic-versus-linear behaviour in fixed-target versus collider geometry is the kinematic basis of accelerator design; see [[Ex - Mandelstam variables for two-body scattering]].

- **The causal-character selection rule** — that a null four-momentum cannot equal a timelike one is a kinematic selection rule that forbids reactions before any dynamics, the four-vector analogue of a conservation-law selection rule. It is why single-photon decay needs a third body, and the same logic (comparing causal character) decides many "is this reaction allowed?" questions; see [[Ex - Whether a particle reaction is kinematically allowed]].

---

# Unlocked by This

> [!tip] Particle Creation and the Discovery of New Particles *(from Particle Physics)*
> Above threshold, kinetic energy is converted into the rest mass of new particles — the way particles are discovered. The antiproton was found at the Bevatron ($p + p \to p + p + p + \bar p$, threshold $7m_p \simeq 6.57$ GeV), the Higgs at the LHC. The quadratic fixed-target threshold versus linear collider threshold is the reason high-energy physics is done with colliders; see [[Ex - Threshold energy for particle production]].

> [!tip] The GZK Cutoff and Ultra-High-Energy Cosmic Rays *(from Astrophysics)*
> A cosmic-ray proton above $\sim 6\times10^{19}$ eV crosses the threshold for pion photoproduction on the cosmic microwave background, losing energy over cosmological distances — the **GZK cutoff** that should truncate the cosmic-ray spectrum and was observed in 2008. The same threshold machinery, applied to a low-energy photon target, predicts it; see [[Ex - Inverse Compton scattering and the GZK cutoff]].

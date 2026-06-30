---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Four-Momentum of a Photon"
  - "Thm - Inelastic Collisions and Particle Production"
tags: [physics, special-relativity]
---

# Problem Statement

Use conservation of four-momentum as a filter to decide whether each reaction is kinematically possible:

1. Show that a single free photon cannot decay into an electron–positron pair: $\gamma \not\to e^+ + e^-$ in vacuum.
2. Show, conversely, that two photons *can* collide to make a pair, $\gamma + \gamma \to e^+ + e^-$, and find the threshold condition $E_1 E_2(1-\cos\theta) \ge 2m_e^2$ for two photons of energies $E_1, E_2$ at angle $\theta$.
3. Show that a free electron cannot emit a single photon, $e^- \not\to e^- + \gamma$ (an electron cannot spontaneously radiate).
4. Explain why $\gamma + p \to p + e^+ + e^-$ (pair production in the field of a proton) *is* allowed, identifying the role of the proton.

Work with $c = 1$.

**Recall:**

A [[Def - The Four-Momentum of a Photon|photon]] has a null four-momentum, $P_\gamma\cdot P_\gamma = 0$. A massive particle has a timelike four-momentum, $P\cdot P = m^2 > 0$. Conservation of four-momentum ([[Thm - Conservation of Four-Momentum]]) requires $\sum P_{\text{in}} = \sum P_{\text{out}}$, and the Minkowski square of both sides must agree (it is a Lorentz invariant). A sum of future-directed timelike four-momenta is timelike.

---

# Convergent Strategy

**Problem class.** A *possibility/impossibility* problem of the [[Special Relativity XIII — Energy and Momentum#Problem-Solving Strategy|causal-filter]] type: a reaction is forbidden if the two sides' total four-momenta have incompatible causal character (one null, one timelike), a kinematic statement requiring no dynamics.

**Assumption pattern.** A proposed reaction with photons and/or massive particles. The signpost is "can this happen?" — compute the causal character (null vs timelike) of each side's total four-momentum, or evaluate the invariant mass and compare to the product masses.

**Theorem routing.** Parts 1, 3 use the causal-character selection rule ([[Thm - Inelastic Collisions and Particle Production]] Lemma 3): a null four-momentum cannot equal a timelike one. Part 2 uses the threshold criterion $\sqrt{s} \ge 2m_e$ with $s = 2P_1\cdot P_2$ for two photons. Part 4 shows the third body makes the four-momenta compatible.

**Key decision point.** The crux is comparing the Minkowski *square* of the two sides — a frame-independent quantity. If one side is null ($\text{square} = 0$) and the other timelike ($\text{square} > 0$), the reaction is impossible in every frame. The non-obvious content is that this is a purely kinematic veto, independent of any interaction strength.

---

# Legal Operations Used

1. **Square a four-momentum to extract an invariant mass** (operation 2 from the topic page). Comparing the Minkowski squares of the two sides decides compatibility: null ($0$) cannot equal timelike ($>0$).

2. **Go to the centre-of-momentum frame** (operation 3). The impossibility can also be seen frame-independently: in the would-be centre-of-momentum frame of the products, the single photon would have to be at rest, which no photon can be.

3. **Use a Lorentz invariant to switch frames** (operation 6). The causal character (sign of $P\cdot P$) is invariant, so an impossibility in one frame is an impossibility in all.

---

# Hints

> [!note]- Hint 1
> If $\gamma\to e^+e^-$ then $P_\gamma = P_{e^+} + P_{e^-}$. Square both sides: the left is $P_\gamma\cdot P_\gamma = 0$ (null), the right is $(P_{e^+}+P_{e^-})^2 \ge (2m_e)^2 > 0$ (timelike). A null vector cannot equal a timelike one.

> [!note]- Hint 2
> For $\gamma\gamma\to e^+e^-$, the *two* photons' total four-momentum can be timelike: $s = (P_1+P_2)^2 = 2P_1\cdot P_2 = 2E_1 E_2(1-\cos\theta) > 0$ for $\theta\ne 0$. The reaction is possible iff $\sqrt{s} \ge 2m_e$, i.e. $E_1 E_2(1-\cos\theta) \ge 2m_e^2$.

> [!note]- Hint 3
> If $e^-\to e^- + \gamma$, square as $P_\gamma = P_e - P_e'$, giving $0 = m_e^2 + m_e^2 - 2P_e\cdot P_e' = 2m_e^2 - 2P_e\cdot P_e'$, so $P_e\cdot P_e' = m_e^2$. But for two timelike electron four-momenta $P_e\cdot P_e' \ge m_e^2$ with equality iff $P_e \parallel P_e'$ — meaning the electron doesn't change, so no photon. Contradiction.

> [!note]- Hint 4
> With a proton, $P_\gamma + P_p = P_p' + P_{e^+} + P_{e^-}$. Now the *left* side is timelike ($P_\gamma + P_p$, a null plus a timelike vector, is timelike), matching the timelike right side. The proton supplies the four-momentum to make both sides compatible.

---

# Solution

A reaction is forbidden when the two sides' total four-momenta have incompatible causal character — a null four-momentum (single photon) cannot equal a timelike one (massive products). Part 1 vetoes single-photon decay; Part 2 shows two photons suffice and finds the threshold; Part 3 vetoes spontaneous electron radiation; Part 4 shows how a third body rescues pair production.

**Step 1: A single photon cannot decay to a pair.**

> [!note]- Derivation
> Suppose $\gamma \to e^+ + e^-$ were possible. Conservation of four-momentum requires
> $$P_\gamma = P_{e^+} + P_{e^-}.$$
> Take the Minkowski square of both sides. The left side is the photon mass-shell:
> $$P_\gamma\cdot P_\gamma = 0 \quad(\text{null}).$$
> The right side is the squared total four-momentum of the pair:
> $$(P_{e^+} + P_{e^-})^2 = m_e^2 + m_e^2 + 2P_{e^+}\cdot P_{e^-} = 2m_e^2 + 2P_{e^+}\cdot P_{e^-}.$$
> For two future-directed timelike four-momenta, $P_{e^+}\cdot P_{e^-} \ge m_e^2$ (reversed Cauchy–Schwarz), so $(P_{e^+}+P_{e^-})^2 \ge 4m_e^2 > 0$ (timelike). But the Minkowski square is a Lorentz invariant, so $0 = P_\gamma\cdot P_\gamma$ would have to equal $(P_{e^+}+P_{e^-})^2 \ge 4m_e^2 > 0$ — a contradiction. **The reaction is impossible in every frame.**
>
> Equivalently: go to the centre-of-momentum frame of the would-be pair, where their total spatial momentum vanishes. There the photon (equal to the total four-momentum) would have to be at rest, $\mathbf{p}_\gamma = 0$ — but a photon always moves at $c$. A single photon simply has nowhere to "stop", so it cannot convert entirely into massive particles.

**Step 2: Two photons can make a pair.**

> [!note]- Derivation
> For $\gamma + \gamma \to e^+ + e^-$, the incoming system is *two* photons, whose total four-momentum can be **timelike** even though each is null. The invariant mass squared is
> $$s = (P_1 + P_2)^2 = \underbrace{P_1\cdot P_1}_{0} + \underbrace{P_2\cdot P_2}_{0} + 2P_1\cdot P_2 = 2P_1\cdot P_2 = 2E_1 E_2(1-\cos\theta),$$
> with $\theta$ the angle between the photon directions; this is $> 0$ for any $\theta \ne 0$ (non-collinear photons), so the system is timelike and *has* a rest frame. The reaction is possible iff the invariant mass reaches the pair's rest mass:
> $$\sqrt{s} \ge 2m_e \;\Longleftrightarrow\; 2E_1 E_2(1-\cos\theta) \ge 4m_e^2 \;\Longleftrightarrow\; \boxed{\ E_1 E_2(1-\cos\theta) \ge 2m_e^2\ }.$$
> The threshold is easiest for head-on photons ($\theta = \pi$, $1-\cos\theta = 2$, so $E_1 E_2 \ge m_e^2$) and impossible for collinear ones ($\theta = 0$, $s = 0$). Two gamma rays, or a gamma ray and a starlight photon, can pair-produce — relevant to the opacity of the universe to high-energy gamma rays (they pair-produce on the extragalactic background light).

**Step 3: A free electron cannot radiate a photon.**

> [!note]- Derivation
> Suppose $e^- \to e^- + \gamma$ were possible. Conservation: $P_e = P_e' + P_\gamma$. Isolate the photon, $P_\gamma = P_e - P_e'$, and square (it is null):
> $$0 = P_\gamma\cdot P_\gamma = (P_e - P_e')^2 = m_e^2 + m_e^2 - 2P_e\cdot P_e' = 2m_e^2 - 2P_e\cdot P_e',$$
> so $P_e\cdot P_e' = m_e^2$. But for two future-timelike electron four-momenta, $P_e\cdot P_e' = m_e^2\,(U_e\cdot U_e') \ge m_e^2$, with equality *only* when $U_e = U_e'$ — i.e. the initial and final electron have the *same* four-velocity, meaning the electron is unchanged and there is no recoil. With no recoil there is no photon. **Contradiction:** a free electron cannot spontaneously emit a photon. (Physically, in the electron's rest frame, emitting a photon would give the electron recoil momentum but no source of energy to pay for the photon plus recoil — energy and momentum cannot both balance.) An electron radiates only when *accelerated* by an external field, which supplies the needed four-momentum.

**Step 4: Pair production on a proton is allowed.**

> [!note]- Derivation
> For $\gamma + p \to p + e^+ + e^-$, the incoming system is a photon *plus a proton*. Its total four-momentum,
> $$P_\gamma + P_p,$$
> is a null vector plus a future-timelike vector, which is future-**timelike**: $(P_\gamma + P_p)^2 = 0 + m_p^2 + 2P_\gamma\cdot P_p = m_p^2 + 2P_\gamma\cdot P_p > 0$. So the incoming side is timelike, matching the timelike outgoing side $P_p' + P_{e^+} + P_{e^-}$ — the causal characters agree, and the reaction is *not* vetoed. It then proceeds above the threshold computed in [[Ex - Threshold energy for particle production|threshold]], $E_\gamma \approx 2m_e$ for a heavy nucleus.
>
> The proton's role is to **supply four-momentum** so that both sides can be timelike with the same invariant mass. The single-photon reaction failed because a lone null four-momentum cannot equal a timelike one; adding the proton makes the incoming four-momentum timelike, and the heavy proton (or nucleus) can absorb the recoil momentum at little energy cost. This is why pair production happens in matter (near nuclei) but not in vacuum.

> [!note]- Complete formal solution
> **(1)** $\gamma\to e^+e^-$: $P_\gamma = P_{e^+}+P_{e^-}$ gives $0 = P_\gamma^2 = (P_{e^+}+P_{e^-})^2 \ge 4m_e^2 > 0$, contradiction — forbidden in every frame. **(2)** $\gamma\gamma\to e^+e^-$: $s = 2P_1\cdot P_2 = 2E_1E_2(1-\cos\theta) > 0$ (timelike for $\theta\ne0$), possible iff $\sqrt{s}\ge 2m_e$, i.e. $E_1 E_2(1-\cos\theta)\ge 2m_e^2$. **(3)** $e^-\to e^-\gamma$: $P_\gamma = P_e - P_e'$ squared gives $P_e\cdot P_e' = m_e^2$, but $P_e\cdot P_e' \ge m_e^2$ with equality iff $U_e = U_e'$ (no recoil, no photon), contradiction — forbidden. **(4)** $\gamma+p\to p+e^+e^-$: incoming $P_\gamma + P_p$ is timelike (null plus timelike), matching the timelike products, so allowed; the proton supplies the four-momentum and absorbs recoil. $\blacksquare$

---

# Key Takeaways

**Compare causal character — a null four-momentum cannot equal a timelike one.** The fastest way to veto a reaction is to compute the *causal character* (the sign of $P\cdot P$) of each side's total four-momentum. A single photon contributes a null four-momentum ($P\cdot P = 0$); a collection of massive particles contributes a timelike one ($> 0$); and since the Minkowski square is frame-independent, a null total can never equal a timelike total in *any* frame. This kills $\gamma\to e^+e^-$ and $e^-\to e^-\gamma$ at a glance, with no dynamics, no interaction strength, no calculation of energies. The reusable diagnostic: for any "can this reaction happen?" question, square both sides and compare — if the squares are forced to differ in sign, the reaction is impossible. This is a kinematic *selection rule*, the four-vector analogue of a conservation-law forbiddenness, and it is the first thing to check before any threshold calculation.

**A single photon has no rest frame, so it cannot convert entirely into mass.** The deep reason $\gamma\to e^+e^-$ fails is geometric: in the centre-of-momentum frame of the would-be products, the photon (equal to the total four-momentum) would have to be at rest, but a photon moves at $c$ in *every* frame. A single massless particle has no rest frame to "stop" in, so it cannot turn entirely into massive particles, which always have a rest frame. The fix in every case is a *third body*: two photons (whose total four-momentum is timelike and *does* have a rest frame) can pair-produce, and a photon plus a nucleus can too. The trigger: whenever a reaction with a lone photon (or any massless particle) on one side is forbidden, ask whether adding a spectator makes the four-momentum timelike — it usually does, and a heavy spectator does so at negligible energy cost. This is why the universe's gamma-ray opacity comes from $\gamma\gamma$ pair production on background light, and why pair production in detectors happens near nuclei.

**Forbiddenness is kinematic, not dynamical — it holds regardless of interaction strength.** A crucial conceptual point is that these vetoes have nothing to do with how strongly the particles interact; they follow purely from conservation of four-momentum and the causal character of four-vectors. $\gamma\to e^+e^-$ is forbidden not because the coupling is weak but because *no* coupling could conserve four-momentum. This distinguishes kinematic impossibility (the reaction cannot conserve $P^\mu$, so it never happens) from dynamical suppression (the reaction conserves $P^\mu$ but has a small amplitude, so it happens rarely). The reusable lesson: before computing any rate or cross-section, check the kinematics — if the reaction violates four-momentum conservation (incompatible causal character, or invariant mass below threshold), no amount of dynamics will make it occur. This is the cheapest and most decisive filter in particle physics, and it is why "is it kinematically allowed?" is always the first question.

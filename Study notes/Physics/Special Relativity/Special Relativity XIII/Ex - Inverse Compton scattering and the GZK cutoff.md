---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Elastic Collisions and the Compton Effect"
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Four-Momentum of a Photon"
  - "Thm - Inelastic Collisions and Particle Production"
tags: [physics, special-relativity]
---

# Problem Statement

In ordinary [[Ex - Compton scattering|Compton scattering]] a photon hands energy to a stationary electron. Here the electron is *moving*, and we shall see it can do the reverse — pump a low-energy photon up to enormous energy. This is the engine of the high-energy sky.

Work with $c = 1$. An observer $\mathcal{O}$ sees a photon of energy $E_1$ scatter off an electron moving with velocity $\mathbf{V}_2 = V_e\,\mathbf{e}$ (a unit vector $\mathbf{e}$), the electron having energy $E_2 = \Gamma_e m_e$ and Lorentz factor $\Gamma_e$. The photon comes in along $\mathbf{n}$ at angle $\varphi$ to the electron's direction ($\mathbf{e}\cdot\mathbf{n} = \cos\varphi$), and leaves along $\mathbf{n}'$ at angle $\varphi'$ ($\mathbf{e}\cdot\mathbf{n}' = \cos\varphi'$); the photon deflection angle is $\theta_1$ ($\mathbf{n}\cdot\mathbf{n}' = \cos\theta_1$).

1. Starting from the *frame-independent* Compton relation between the photon four-momenta and the electron four-momentum, derive the ratio of scattered to incident photon energy as measured by $\mathcal{O}$:
$$\frac{E_1'}{E_1} = \frac{1 - V_e\cos\varphi}{1 - V_e\cos\varphi' + (E_1/E_2)(1 - \cos\theta_1)}.$$
2. In the regime where the electron is far more energetic than the photon, $E_1/E_2 \ll 1$, find the geometry that maximises the photon energy gain and show that for an ultra-relativistic electron
$$\max\frac{E_1'}{E_1} \simeq 4\Gamma_e^2.$$
3. Apply this to a cosmic-microwave-background photon ($E_1 \approx 6\times10^{-4}$ eV) up-scattered by a relativistic electron, and estimate the electron Lorentz factor needed to boost it into the X-ray/gamma band.
4. Now treat the **GZK cutoff**: an ultra-high-energy proton ploughs into the CMB and photoproduces a pion, $p + \gamma_{\text{CMB}} \to p + \pi^0$. Using the invariant-mass technique, find the threshold proton energy $E_p$ for a head-on collision with a CMB photon of energy $\omega$, and evaluate it.

**Recall:**

![[Thm - Elastic Collisions and the Compton Effect#Statement]]

The [[Def - The Four-Momentum of a Photon|photon four-momentum]] relative to $\mathcal{O}$ is $P_\gamma = E(U_0 + \mathbf{n})$, null ($P_\gamma\cdot P_\gamma = 0$). The electron four-momentum is $P_2 = E_2(U_0 + V_e\,\mathbf{e})$ with $P_2\cdot P_2 = m_e^2$. The Compton derivation (conservation of four-momentum $P_1 + P_2 = P_1' + P_2'$, then isolate and square the recoil electron) yields the *frame-independent* relation
$$P_2\cdot(P_1 - P_1') = P_1\cdot P_1',$$
valid whatever the electron's state of motion. A reaction $a + b \to c + \cdots$ is allowed when the invariant mass of the incoming system reaches the sum of product masses ([[Thm - Inelastic Collisions and Particle Production]]).

---

# Convergent Strategy

**Problem class.** A *collision measured by a moving observer* problem: the Compton algebra is unchanged (it is frame-independent), but now the electron carries velocity, so the inner products $P_\gamma\cdot P_2$ depend on the angles between the photon directions and the electron's motion. Parts 1–3 are inverse Compton; Part 4 is a threshold problem of the [[Ex - Threshold energy for particle production|invariant-mass]] type.

**Assumption pattern.** Parts 1–2: a fast electron and a soft photon — the signpost "moving electron" tells you the rest-frame Compton shift will be boosted, and the question "how much energy can the photon *gain*?" tells you to maximise $E_1'/E_1$. Part 4: "minimum energy to make a pion" is the threshold flag.

**Theorem routing.** The frame-independent Compton relation $P_2\cdot(P_1 - P_1') = P_1\cdot P_1'$ comes straight from [[Thm - Elastic Collisions and the Compton Effect]]; expanding each inner product in $\mathcal{O}$'s frame with the given angles produces the energy-ratio formula. The $4\Gamma_e^2$ limit is two successive boosts (the maximum photon-electron head-on geometry, then back), cleanly seen via $V_e \simeq 1 - 1/(2\Gamma_e^2)$. Part 4 routes through [[Thm - Inelastic Collisions and Particle Production]]: equate $(P_p + P_\gamma)^2$ to $(m_p + m_\pi)^2$ at threshold.

**Key decision point.** For Parts 1–2 the crux is that *the Compton relation does not care about the electron's motion* — equation $P_2\cdot(P_1 - P_1') = P_1\cdot P_1'$ holds in any frame — so you may keep working in $\mathcal{O}$'s frame and simply carry the electron-velocity-dependent inner products. The $4\Gamma_e^2$ comes from choosing the optimal geometry ($\varphi = \pi$ head-on in, $\varphi' = 0$ out) and Taylor-expanding $V_e$. For Part 4 the crux is the standard one: evaluate the conserved invariant $(P_p + P_\gamma)^2$ in the lab and set it equal to its threshold value.

---

# Legal Operations Used

1. **Use a Lorentz invariant to switch frames** (operation 6). The Compton relation $P_2\cdot(P_1 - P_1') = P_1\cdot P_1'$ is a scalar equation, true in $\mathcal{O}$'s frame; expand the invariants there.

2. **Use $E = P\cdot U_0$ and the observer decomposition** (operation 5). Each photon and electron four-momentum is written $E(U_0 + \cdots)$, and the inner products reduce to energies times $(1 - \cos\text{angle})$ factors.

3. **Square the total four-momentum to extract the invariant mass** (operations 2, 3). For the GZK threshold, $(P_p + P_\gamma)^2$ is the system invariant mass squared, evaluated in the lab and equated to $(m_p + m_\pi)^2$.

4. **Taylor-expand the ultra-relativistic Lorentz factor.** $V_e = \sqrt{1 - \Gamma_e^{-2}} \simeq 1 - 1/(2\Gamma_e^2)$ converts the exact ratio into the compact $4\Gamma_e^2$.

---

# Hints

> [!note]- Hint 1
> The Compton derivation isolates and squares the recoil electron: from $P_1 + P_2 = P_1' + P_2'$, write $P_2' = P_1 + P_2 - P_1'$ and square to $m_e^2$, using $P_1\cdot P_1 = P_1'\cdot P_1' = 0$ (null photons) and $P_2\cdot P_2 = m_e^2$. This gives $P_2\cdot P_1 - P_2\cdot P_1' = P_1\cdot P_1'$, i.e. $P_2\cdot(P_1 - P_1') = P_1\cdot P_1'$ — and *nowhere* did we assume the electron is at rest, so it holds for a moving electron too.

> [!note]- Hint 2
> Expand the inner products in $\mathcal{O}$'s frame. With $P_1 = E_1(U_0 + \mathbf{n})$, $P_1' = E_1'(U_0 + \mathbf{n}')$, $P_2 = E_2(U_0 + V_e\mathbf{e})$ and the orthonormality $U_0\cdot U_0 = 1$, $U_0\cdot\mathbf{n} = 0$, $\mathbf{n}\cdot\mathbf{n} = -1$: $P_2\cdot P_1 = E_2 E_1(1 - V_e\cos\varphi)$, $P_2\cdot P_1' = E_2 E_1'(1 - V_e\cos\varphi')$, $P_1\cdot P_1' = E_1 E_1'(1 - \cos\theta_1)$. Substitute into $P_2\cdot(P_1 - P_1') = P_1\cdot P_1'$ and solve for $E_1'/E_1$.

> [!note]- Hint 3
> For $E_1/E_2 \ll 1$ the last term in the denominator drops, leaving $E_1'/E_1 \simeq (1 - V_e\cos\varphi)/(1 - V_e\cos\varphi')$. The numerator is largest and the denominator smallest when $\cos\varphi = -1$ (photon incoming *against* the electron, $\varphi = \pi$) and $\cos\varphi' = +1$ (photon outgoing *along* the electron, $\varphi' = 0$): $\max E_1'/E_1 = (1 + V_e)/(1 - V_e)$.

> [!note]- Hint 4
> Use $V_e = \sqrt{1 - \Gamma_e^{-2}} \simeq 1 - 1/(2\Gamma_e^2)$ for $\Gamma_e \gg 1$: then $1 - V_e \simeq 1/(2\Gamma_e^2)$ and $1 + V_e \simeq 2$, so $(1+V_e)/(1-V_e) \simeq 2/(1/2\Gamma_e^2) = 4\Gamma_e^2$. For the GZK part: $(P_p + P_\gamma)^2 = m_p^2 + 2P_p\cdot P_\gamma$ (photon null), with $P_p\cdot P_\gamma = E_p\omega(1 + V_p) \approx 2E_p\omega$ for a head-on ultra-relativistic proton; set equal to $(m_p + m_\pi)^2$ and solve for $E_p$.

---

# Solution

Inverse Compton is the ordinary Compton calculation read in a frame where the electron moves: the same frame-independent relation, now carrying the electron's velocity through the angle factors. The dramatic content is that a fast electron can multiply a photon's energy by up to $4\Gamma_e^2$. The GZK cutoff is then a threshold problem on the cosmic microwave background.

**Step 1: The inverse Compton energy ratio.**

> [!note]- Derivation
> Conservation of four-momentum is $P_1 + P_2 = P_1' + P_2'$ (incident photon $1$, electron $2$). Isolate the recoil electron and square — the standard [[Thm - Elastic Collisions and the Compton Effect|Compton move]]:
> $$P_2' = P_1 + P_2 - P_1', \qquad P_2'\cdot P_2' = m_e^2.$$
> Expanding the right side with $P_1\cdot P_1 = P_1'\cdot P_1' = 0$ (null photons) and $P_2\cdot P_2 = m_e^2$:
> $$m_e^2 = m_e^2 + 2P_2\cdot P_1 - 2P_2\cdot P_1' - 2P_1\cdot P_1',$$
> hence the **frame-independent Compton relation**
> $$P_2\cdot(P_1 - P_1') = P_1\cdot P_1'.$$
> No assumption was made about the electron's motion, so this is valid for a *moving* electron. Now expand each invariant in $\mathcal{O}$'s frame, using $P_1 = E_1(U_0 + \mathbf{n})$, $P_1' = E_1'(U_0 + \mathbf{n}')$, $P_2 = E_2(U_0 + V_e\mathbf{e})$ and the rest-space orthonormality ($U_0\cdot U_0 = 1$, $U_0\cdot\mathbf{n} = 0$, $\mathbf{n}\cdot\mathbf{n}' = -\cos\theta_1$, etc.):
> $$P_2\cdot P_1 = E_2 E_1(1 - V_e\cos\varphi), \quad P_2\cdot P_1' = E_2 E_1'(1 - V_e\cos\varphi'), \quad P_1\cdot P_1' = E_1 E_1'(1 - \cos\theta_1).$$
> Substituting,
> $$E_2 E_1(1 - V_e\cos\varphi) - E_2 E_1'(1 - V_e\cos\varphi') = E_1 E_1'(1 - \cos\theta_1).$$
> Divide through by $E_2 E_1$ and collect the $E_1'$ terms:
> $$1 - V_e\cos\varphi = \frac{E_1'}{E_1}\Big[(1 - V_e\cos\varphi') + \frac{E_1}{E_2}(1 - \cos\theta_1)\Big],$$
> giving the result
> $$\boxed{\ \frac{E_1'}{E_1} = \frac{1 - V_e\cos\varphi}{1 - V_e\cos\varphi' + (E_1/E_2)(1 - \cos\theta_1)}\ }.$$
> Setting $V_e = 0$ recovers the stationary-electron Compton formula $E_1'/E_1 = 1/[1 + (E_1/m_e)(1-\cos\theta_1)]$, as it must. With $V_e \ne 0$ the ratio can exceed $1$: the photon *gains* energy. This is the **inverse Compton effect**.

**Step 2: The $4\Gamma_e^2$ energy boost.**

> [!note]- Derivation
> When the electron is far more energetic than the photon, $E_1/E_2 = E_1/(\Gamma_e m_e) \ll 1$, the recoil term $(E_1/E_2)(1-\cos\theta_1)$ in the denominator is negligible, and
> $$\frac{E_1'}{E_1} \simeq \frac{1 - V_e\cos\varphi}{1 - V_e\cos\varphi'}.$$
> The photon energy gain is maximised by making the numerator as large and the denominator as small as possible. The numerator $1 - V_e\cos\varphi$ is largest at $\cos\varphi = -1$ — the photon comes in *head-on against* the electron ($\varphi = \pi$). The denominator $1 - V_e\cos\varphi'$ is smallest at $\cos\varphi' = +1$ — the photon goes out *forward along* the electron ($\varphi' = 0$). Then
> $$\max\frac{E_1'}{E_1} = \frac{1 + V_e}{1 - V_e}.$$
> For an ultra-relativistic electron, $\Gamma_e \gg 1$, expand $V_e = \sqrt{1 - \Gamma_e^{-2}} \simeq 1 - \tfrac{1}{2\Gamma_e^2}$, so $1 - V_e \simeq \tfrac{1}{2\Gamma_e^2}$ and $1 + V_e \simeq 2$:
> $$\boxed{\ \max\frac{E_1'}{E_1} \simeq \frac{2}{1/(2\Gamma_e^2)} = 4\Gamma_e^2\ }.$$
> The photon energy is amplified by *four times the square of the electron Lorentz factor*. Physically: boost into the electron rest frame (one factor $\sim 2\Gamma_e$ Doppler blueshift of the incoming photon), scatter nearly elastically there (Thomson regime, energy roughly preserved in that frame), then boost back out (another factor $\sim 2\Gamma_e$ blueshift) — two blueshifts of $2\Gamma_e$ each multiply to $4\Gamma_e^2$.

**Step 3: Up-scattering the CMB.**

> [!note]- Derivation
> A CMB photon at the $2.725$ K blackbody peak has energy $E_1 \approx 2.7\,k_B T \approx 6\times10^{-4}$ eV. To boost it to an X-ray energy $E_1' \approx 1$ keV $= 10^3$ eV requires
> $$4\Gamma_e^2 \approx \frac{E_1'}{E_1} = \frac{10^3}{6\times10^{-4}} \approx 1.7\times10^{6} \quad\Longrightarrow\quad \Gamma_e \approx \sqrt{\frac{1.7\times10^6}{4}} \approx 650.$$
> An electron of $\Gamma_e \approx 650$ (energy $\Gamma_e m_e \approx 650 \times 0.511\,\text{MeV} \approx 330$ MeV) up-scatters microwave photons into soft X-rays. To reach a $1$ MeV gamma ray, $E_1'/E_1 \approx 1.7\times10^9$, so $\Gamma_e \approx 2\times10^4$ (energy $\approx 10$ GeV). This is exactly the mechanism of the **Sunyaev–Zel'dovich effect** (hot cluster-gas electrons distorting the CMB spectrum) and of the TeV gamma-ray emission of **blazar** jets, whose relativistic electrons inverse-Compton-scatter their own synchrotron photons to produce the high-energy hump of the spectrum. The $\Gamma_e^2$ scaling is what lets modest electron energies reach into the gamma band.

**Step 4: The GZK cutoff.**

> [!note]- Derivation
> The reaction $p + \gamma_{\text{CMB}} \to p + \pi^0$ (pion photoproduction) is an [[Thm - Inelastic Collisions and Particle Production|inelastic collision]]; it proceeds once the invariant mass of the proton-plus-photon system reaches $m_p + m_\pi$. The conserved invariant is $(P_p + P_\gamma)^2$:
> $$(P_p + P_\gamma)^2 = P_p\cdot P_p + 2P_p\cdot P_\gamma + P_\gamma\cdot P_\gamma = m_p^2 + 2P_p\cdot P_\gamma,$$
> using $P_\gamma\cdot P_\gamma = 0$. For a proton of energy $E_p$ and speed $V_p$ meeting a photon of energy $\omega$ head-on (the easiest geometry, lowest threshold), $P_p\cdot P_\gamma = E_p\omega(1 + V_p) \approx 2E_p\omega$ for $V_p \approx 1$. At threshold the invariant equals $(m_p + m_\pi)^2$:
> $$m_p^2 + 4 E_p\omega = (m_p + m_\pi)^2 = m_p^2 + 2m_p m_\pi + m_\pi^2,$$
> so
> $$\boxed{\ E_p^{\text{thres}} = \frac{2m_p m_\pi + m_\pi^2}{4\omega} = \frac{m_\pi(2m_p + m_\pi)}{4\omega}\ }.$$
> Numerically, with $m_p = 938$ MeV, $m_\pi = 135$ MeV (the $\pi^0$), and a typical CMB photon $\omega \approx 6\times10^{-4}$ eV $= 6\times10^{-13}$ MeV:
> $$E_p^{\text{thres}} = \frac{135\,(2\cdot938 + 135)}{4\cdot 6\times10^{-13}}\ \text{MeV} = \frac{135\times 2011}{2.4\times10^{-12}}\ \text{MeV} \approx 1.1\times10^{17}\ \text{MeV} = 1.1\times10^{20}\ \text{eV}.$$
> So protons above $\sim 10^{20}$ eV (a few times $10^{19}$ eV for the more numerous higher-energy tail of the CMB) photoproduce pions on the microwave background, losing energy over a path length of order $100$ Mpc — the **Greisen–Zatsepin–Kuz'min (GZK) cutoff**. Cosmic-ray protons of higher energy cannot reach us from cosmological distances; the suppression of the spectrum near this energy was observed in 2008.

> [!note]- Complete formal solution
> Isolating and squaring the recoil electron in $P_1 + P_2 = P_1' + P_2'$ gives the frame-independent Compton relation $P_2\cdot(P_1 - P_1') = P_1\cdot P_1'$, valid for a moving electron. Expanding in $\mathcal{O}$'s frame ($P_2\cdot P_1 = E_2 E_1(1-V_e\cos\varphi)$, etc.) yields $E_1'/E_1 = (1 - V_e\cos\varphi)/[1 - V_e\cos\varphi' + (E_1/E_2)(1-\cos\theta_1)]$. For $E_1/E_2\ll 1$ the recoil term drops; maximising over geometry ($\varphi=\pi$, $\varphi'=0$) gives $\max E_1'/E_1 = (1+V_e)/(1-V_e)$, and $V_e\simeq 1 - 1/(2\Gamma_e^2)$ gives $\max E_1'/E_1\simeq 4\Gamma_e^2$. A CMB photon ($6\times10^{-4}$ eV) reaches keV X-rays at $\Gamma_e\approx 650$, MeV gammas at $\Gamma_e\approx 2\times10^4$. For GZK, $(P_p+P_\gamma)^2 = m_p^2 + 2P_p\cdot P_\gamma$ with head-on $P_p\cdot P_\gamma\approx 2E_p\omega$; threshold $(m_p+m_\pi)^2$ gives $E_p^{\text{thres}} = m_\pi(2m_p+m_\pi)/(4\omega)\approx 1\times10^{20}$ eV. $\blacksquare$

---

# Key Takeaways

**The Compton relation is frame-independent, so inverse Compton is "the same process seen by a moving observer".** The deep economy of this exercise is that *no new calculation* is needed to make a photon gain energy: the relation $P_2\cdot(P_1 - P_1') = P_1\cdot P_1'$ derived for Compton scattering never used the electron's rest, so it already governs the moving-electron case. Whether the photon loses energy (Compton) or gains it (inverse Compton) is decided entirely by the inner products $P_2\cdot P_1$ and $P_2\cdot P_1'$, which carry the electron's velocity through the angle factors $1 - V_e\cos\varphi$. Remark 9.16 of Gourgoulhon makes the point sharpest: in the electron's own rest frame, Compton and inverse Compton are *literally the same scattering event* — the distinction is a statement about which observer is watching. The reusable lesson is that relations built purely from four-vector inner products are automatically valid in every frame, so a result proved in one convenient configuration (electron at rest) extends for free to all others (electron moving) — provided you resisted the temptation to specialise the frame mid-derivation.

**The energy boost is $4\Gamma_e^2$ — two Doppler blueshifts of $2\Gamma_e$ each.** The factor $4\Gamma_e^2$ is the signature of inverse Compton scattering and the reason it dominates high-energy astrophysics. Its origin is transparent in the rest-frame picture: boosting into the ultra-relativistic electron's frame blueshifts the incoming photon by $\sim 2\Gamma_e$ (the head-on Doppler factor $\gamma(1+V_e) \approx 2\Gamma_e$), the photon scatters with little energy change in that frame, and boosting back out blueshifts it again by $\sim 2\Gamma_e$ — the two factors multiplying to $4\Gamma_e^2$. This quadratic dependence on the electron Lorentz factor is what allows electrons of merely hundreds of MeV to lift microwave photons into X-rays, and GeV electrons to reach the gamma band; it powers the Sunyaev–Zel'dovich distortion of the CMB and the TeV emission of blazars. The reflex to carry away: an ultra-relativistic scatterer multiplies a photon's energy by the *square* of its Lorentz factor, because the photon is blueshifted both on the way in and on the way out.

**The GZK cutoff is a threshold problem on the coldest radiation in the universe — and it bounds the cosmic-ray spectrum.** Part 4 shows the invariant-mass technique reaching across forty orders of magnitude in energy: the same $(\sum P)^2$ that fixes accelerator thresholds, evaluated for a $10^{20}$ eV proton against a $10^{-3}$ eV CMB photon, predicts a sharp ceiling on the energy of cosmic rays that travel cosmological distances. The structure is the universal threshold recipe — the conserved invariant $(P_p + P_\gamma)^2$ equals $m_p^2 + 2P_p\cdot P_\gamma$ (photon null), set equal to $(m_p + m_\pi)^2$ — and the only physics input is the pion mass and the CMB temperature. That the answer, $\sim 10^{20}$ eV, sits right at the highest cosmic-ray energies observed is one of the most striking quantitative successes of relativistic kinematics applied to astrophysics, and it is the reason ultra-high-energy cosmic rays must originate within our cosmic neighbourhood (the "GZK horizon", $\sim 100$ Mpc). The reusable diagnostic: to find whether an energetic particle can interact with a soft background, compute the invariant mass of the pair and compare it with the threshold for the process — a single contraction $P\cdot P$ settles a question that spans the whole observable universe.

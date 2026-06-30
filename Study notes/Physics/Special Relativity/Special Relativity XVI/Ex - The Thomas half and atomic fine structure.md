---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Thomas Precession"
  - "Thm - The Thomas Equation"
  - "Def - Spin Four-Vector"
tags: [physics, special-relativity]
---

# Problem Statement

Carry out the semiclassical spin–orbit calculation for a hydrogen-like atom and show that Thomas precession supplies the **factor of one-half** ("the Thomas half") needed to match the observed fine-structure splitting of atomic spectral lines. An electron of charge $-e$, mass $m$, and spin $\mathbf{S}$ orbits a nucleus in a central electrostatic potential $\phi(r)$ (so the potential energy is $V(r) = -e\phi(r)$). Working with $c$ restored:

1. Find the magnetic field $\mathbf{B}'$ the electron sees in its instantaneous rest frame, due to the (apparently moving) nuclear charge, to first order in $v/c$.
2. Write the *naive* spin–orbit interaction energy $H_{\mathrm{SO}}^{\mathrm{naive}} = -\boldsymbol\mu\cdot\mathbf{B}'$ with the electron magnetic moment $\boldsymbol\mu = -g_s(e/2mc)\mathbf{S}$ ($g_s \approx 2$), and express it in terms of $\mathbf{L}\cdot\mathbf{S}$.
3. Compute the Thomas-precession energy: the electron's rest frame rotates at $\boldsymbol\Omega_T = \tfrac12\mathbf{a}\times\mathbf{v}/c^2$, contributing an additional precession of the spin that corresponds to an energy $H_T = \mathbf{S}\cdot\boldsymbol\Omega_T$.
4. Add the two contributions and show the Thomas term *halves* the naive result, giving the correct $H_{\mathrm{SO}} = \frac{1}{2m^2c^2}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\,\mathbf{L}\cdot\mathbf{S}$ — the **Thomas half** — which agrees with the Dirac equation.

**Recall:**

![[Def - Thomas Precession#The Definition]]

An electron orbiting a nucleus is centripetally accelerated, $\mathbf{a}\perp\mathbf{v}$, so its spin undergoes [[Def - Thomas Precession|Thomas precession]] at the low-velocity rate $\boldsymbol\Omega_T = \tfrac{1}{2c^2}\mathbf{a}\times\mathbf{v}$ (the [[Thm - The Thomas Equation|Thomas equation]], free-spin limit). The orbital angular momentum is $\mathbf{L} = m\mathbf{r}\times\mathbf{v}$. The electron's acceleration in the central field is $\mathbf{a} = -\tfrac{1}{m}\nabla V = -\tfrac{1}{m}\tfrac{\mathrm{d}V}{\mathrm{d}r}\hat{\mathbf{r}}$. **This calculation supplements Gourgoulhon Chapter 12** (which derives the Thomas equation but not the atomic application); the spin–orbit physics is standard (Jackson, *Classical Electrodynamics* §11.8).

---

# Convergent Strategy

**Problem class.** A *compute-a-precession* problem with a physical-energy payoff, bridging into atomic physics: find the spin–orbit energy and show Thomas precession corrects it. The decisive move is to recognise that the electron's rest frame *rotates* (Thomas precession), so the spin's energy includes a kinematic term beyond the naive magnetic one.

**Assumption pattern.** The electron orbits with $\mathbf{a}\perp\mathbf{v}$ (centripetal), so Thomas precession occurs at $\boldsymbol\Omega_T = \tfrac12\mathbf{a}\times\mathbf{v}/c^2$. The signpost is the well-known factor-of-two discrepancy: the naive spin–orbit coupling overestimates the fine-structure splitting by exactly $2$, and the missing ingredient is the rotation of the electron's rest frame.

**Theorem routing.** The route is: transform the nuclear Coulomb field to the electron rest frame to get $\mathbf{B}'$ $\Rightarrow$ naive energy $-\boldsymbol\mu\cdot\mathbf{B}' \propto +\mathbf{L}\cdot\mathbf{S}$ $\Rightarrow$ Thomas precession energy $H_T = \mathbf{S}\cdot\boldsymbol\Omega_T \propto -\tfrac12\mathbf{L}\cdot\mathbf{S}$ (the [[Thm - The Thomas Equation|Thomas equation]] / low-velocity [[Def - Thomas Precession|rate]]) $\Rightarrow$ sum halves the naive coefficient. The Dirac equation confirms the result.

**Key decision point.** The crux is that the spin in the electron's rest frame precesses *both* from the magnetic torque ($-\boldsymbol\mu\cdot\mathbf{B}'$) *and* from the kinematic Thomas rotation of that frame, and the two must be added. The trap is to include only the magnetic torque (the naive calculation), which double-counts the splitting. The Thomas term is *opposite in sign* and *half the magnitude* of the naive term, so it subtracts exactly half — the precession opposing the orbit (from [[Ex - Thomas precession of a gyroscope in circular orbit|the gyroscope exercise]]) is what makes the sign work.

---

# Legal Operations Used

1. **Transport a frame / decompose boost-times-rotation** (operation 7 from the topic page). The electron's instantaneous rest frame rotates relative to the lab by the [[Def - Thomas Rotation|Thomas rotation]]; the precession rate $\boldsymbol\Omega_T = \tfrac12\mathbf{a}\times\mathbf{v}/c^2$ is the kinematic contribution to the spin's evolution.

2. **Work in the rest frame, then boost out** (operation 2 from the topic page). The magnetic field $\mathbf{B}'$ the electron experiences is computed by boosting the nuclear Coulomb field into the electron's instantaneous rest frame.

3. **Take the low-velocity / small-distance limit** (operation 9 from the topic page). Everything is computed to first order in $v/c$, the regime of atomic electrons ($v/c\sim Z\alpha\sim 1\%$ for hydrogen), where $\boldsymbol\Omega_T \approx \tfrac12\mathbf{a}\times\mathbf{v}/c^2$.

---

# Hints

> [!note]- Hint 1
> In the lab frame the nucleus produces a purely electric field $\mathbf{E} = -\nabla\phi = -\tfrac{1}{e}\tfrac{\mathrm{d}V}{\mathrm{d}r}\hat{\mathbf{r}}\cdot(\ldots)$; more usefully $\mathbf{E} = \tfrac{1}{e}\nabla V = \tfrac{1}{e}\tfrac{\mathrm{d}V}{\mathrm{d}r}\hat{\mathbf{r}}$ (force on electron is $-e\mathbf{E} = -\nabla V$). Boosting to the electron rest frame (moving at $\mathbf{v}$), the transformed magnetic field to first order in $v/c$ is $\mathbf{B}' = -\tfrac{1}{c}\mathbf{v}\times\mathbf{E} = -\tfrac{1}{ec}\mathbf{v}\times\nabla V$.

> [!note]- Hint 2
> The interaction is $H_{\mathrm{SO}}^{\mathrm{naive}} = -\boldsymbol\mu\cdot\mathbf{B}'$ with $\boldsymbol\mu = -g_s\tfrac{e}{2mc}\mathbf{S}$, $g_s = 2$. Substitute $\mathbf{B}' = -\tfrac{1}{ec}\mathbf{v}\times\nabla V = -\tfrac{1}{ecr}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{v}\times\mathbf{r}$. Using $\mathbf{v}\times\mathbf{r} = -\mathbf{r}\times\mathbf{v} = -\mathbf{L}/m$: get $H_{\mathrm{SO}}^{\mathrm{naive}} = \tfrac{1}{m^2c^2}\tfrac{1}{r}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S}$ (with $g_s = 2$). This is *twice* the correct answer.

> [!note]- Hint 3
> The electron's acceleration is $\mathbf{a} = -\tfrac{1}{m}\nabla V = -\tfrac{1}{m}\tfrac{\mathrm{d}V}{\mathrm{d}r}\hat{\mathbf{r}}$. The Thomas precession rate is $\boldsymbol\Omega_T = \tfrac{1}{2c^2}\mathbf{a}\times\mathbf{v} = -\tfrac{1}{2mc^2}\tfrac{1}{r}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{r}\times\mathbf{v} = -\tfrac{1}{2m^2c^2}\tfrac{1}{r}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}$. The associated energy of the precessing spin is $H_T = \mathbf{S}\cdot\boldsymbol\Omega_T = -\tfrac{1}{2m^2c^2}\tfrac{1}{r}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S}$ — *half the naive term, opposite sign*.

> [!note]- Hint 4
> Add: $H_{\mathrm{SO}} = H_{\mathrm{SO}}^{\mathrm{naive}} + H_T = \tfrac{1}{m^2c^2}\tfrac{1}{r}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S} - \tfrac{1}{2m^2c^2}\tfrac{1}{r}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S} = \tfrac{1}{2m^2c^2}\tfrac{1}{r}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S}$. The factor of $\tfrac12$ is the Thomas half. This matches the Dirac equation.

---

# Solution

The naive spin–orbit coupling is twice too large; Thomas precession subtracts exactly half. Step 1 boosts the nuclear field to the electron rest frame. Step 2 writes the naive magnetic energy, proportional to $\mathbf{L}\cdot\mathbf{S}$. Step 3 computes the Thomas precession energy — half the naive term, opposite sign. Step 4 adds them to get the correct fine-structure Hamiltonian. The non-obvious content is that the electron's rest frame *rotates* (Thomas precession), contributing a kinematic energy that the naive calculation omits.

**Step 1: The electron sees $\mathbf{B}' = -\frac{1}{ec}\,\mathbf{v}\times\nabla V$.**

> [!note]- Derivation
> The nucleus produces a static, purely electric field in the lab frame. The force on the electron is $\mathbf{F} = -\nabla V(r) = -\tfrac{\mathrm{d}V}{\mathrm{d}r}\hat{\mathbf{r}}$, so writing the field through $\mathbf{F} = -e\mathbf{E}$ gives $\mathbf{E} = \tfrac{1}{e}\nabla V = \tfrac{1}{e}\tfrac{\mathrm{d}V}{\mathrm{d}r}\hat{\mathbf{r}}$ (radial, lab frame, $\mathbf{B}_{\mathrm{lab}} = 0$).
>
> Transform to the electron's instantaneous rest frame, which moves at velocity $\mathbf{v}$ relative to the lab. The field-transformation law for a boost, to first order in $v/c$, gives a magnetic field
> $$\mathbf{B}' = -\frac{1}{c}\mathbf{v}\times\mathbf{E} = -\frac{1}{ec}\,\mathbf{v}\times\nabla V = -\frac{1}{ec}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\,\mathbf{v}\times\mathbf{r},$$
> using $\nabla V = \tfrac{\mathrm{d}V}{\mathrm{d}r}\hat{\mathbf{r}} = \tfrac{1}{r}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{r}$. Physically, the electron sees the nuclear charge as a current loop, producing a magnetic field at the electron's location — this is the field that couples to the electron's spin. (This is the standard transformation $\mathbf{B}' \approx \mathbf{B} - \tfrac{1}{c}\mathbf{v}\times\mathbf{E}$ with $\mathbf{B} = 0$.)

**Step 2: The naive spin–orbit energy is $H_{\mathrm{SO}}^{\mathrm{naive}} = \frac{1}{m^2c^2}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\,\mathbf{L}\cdot\mathbf{S}$.**

> [!note]- Derivation
> The electron's spin magnetic moment is $\boldsymbol\mu = -g_s\tfrac{e}{2mc}\mathbf{S}$ with $g_s = 2$ (the Dirac value). The naive interaction energy of the moment with the rest-frame field is
> $$H_{\mathrm{SO}}^{\mathrm{naive}} = -\boldsymbol\mu\cdot\mathbf{B}' = g_s\frac{e}{2mc}\mathbf{S}\cdot\mathbf{B}' = \frac{e}{mc}\mathbf{S}\cdot\mathbf{B}' \quad(g_s = 2).$$
> Substituting $\mathbf{B}' = -\tfrac{1}{ecr}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{v}\times\mathbf{r}$ and using $\mathbf{v}\times\mathbf{r} = -\mathbf{r}\times\mathbf{v} = -\tfrac{1}{m}\mathbf{L}$ (with $\mathbf{L} = m\mathbf{r}\times\mathbf{v}$):
> $$H_{\mathrm{SO}}^{\mathrm{naive}} = \frac{e}{mc}\cdot\Big(-\frac{1}{ecr}\frac{\mathrm{d}V}{\mathrm{d}r}\Big)\mathbf{S}\cdot(\mathbf{v}\times\mathbf{r}) = \frac{e}{mc}\cdot\Big(-\frac{1}{ecr}\frac{\mathrm{d}V}{\mathrm{d}r}\Big)\Big(-\frac{1}{m}\Big)\mathbf{L}\cdot\mathbf{S} = \frac{1}{m^2c^2}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\,\mathbf{L}\cdot\mathbf{S}.$$
> This is the spin–orbit coupling as naively computed — and it is *twice too large*. Comparing with the experimentally observed fine-structure splitting (and with the Dirac equation), this coefficient must be halved. The naive calculation has omitted a purely kinematic effect: the electron's rest frame is *rotating*.

**Step 3: The Thomas-precession energy is $H_T = -\frac{1}{2m^2c^2}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\,\mathbf{L}\cdot\mathbf{S}$ — half the naive term, opposite sign.**

> [!note]- Derivation
> The electron is centripetally accelerated, $\mathbf{a}\perp\mathbf{v}$, so its instantaneous rest frame undergoes [[Def - Thomas Precession|Thomas precession]] relative to the lab at the low-velocity rate (the [[Thm - The Thomas Equation|Thomas equation]], free-spin limit)
> $$\boldsymbol\Omega_T = \frac{1}{2c^2}\mathbf{a}\times\mathbf{v}.$$
> The electron's acceleration is $\mathbf{a} = \mathbf{F}/m = -\tfrac{1}{m}\nabla V = -\tfrac{1}{m}\tfrac{\mathrm{d}V}{\mathrm{d}r}\hat{\mathbf{r}} = -\tfrac{1}{mr}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{r}$. Hence
> $$\boldsymbol\Omega_T = \frac{1}{2c^2}\Big(-\frac{1}{mr}\frac{\mathrm{d}V}{\mathrm{d}r}\mathbf{r}\Big)\times\mathbf{v} = -\frac{1}{2mc^2 r}\frac{\mathrm{d}V}{\mathrm{d}r}\,\mathbf{r}\times\mathbf{v} = -\frac{1}{2m^2c^2 r}\frac{\mathrm{d}V}{\mathrm{d}r}\,\mathbf{L},$$
> using $\mathbf{r}\times\mathbf{v} = \mathbf{L}/m$. A spin precessing at angular velocity $\boldsymbol\Omega_T$ has an associated interaction energy $H_T = \mathbf{S}\cdot\boldsymbol\Omega_T$ (the energy of a moment whose precession is $\boldsymbol\Omega_T$; equivalently, transforming the spin's equation of motion to the rotating frame adds this term to the Hamiltonian). Thus
> $$H_T = \mathbf{S}\cdot\boldsymbol\Omega_T = -\frac{1}{2m^2c^2}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\,\mathbf{L}\cdot\mathbf{S}.$$
> This is *exactly half* the naive spin–orbit term of Step 2, and with the *opposite sign* — the minus sign coming from the Thomas precession opposing the orbital sense (as found for [[Ex - Thomas precession of a gyroscope in circular orbit|the orbiting gyroscope]]). The Thomas term subtracts.

**Step 4: The sum is the correct $H_{\mathrm{SO}} = \frac{1}{2m^2c^2}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S}$ — the Thomas half.**

> [!note]- Derivation
> The total spin–orbit Hamiltonian is the sum of the magnetic interaction and the Thomas-precession energy:
> $$H_{\mathrm{SO}} = H_{\mathrm{SO}}^{\mathrm{naive}} + H_T = \frac{1}{m^2c^2}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S} - \frac{1}{2m^2c^2}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S} = \frac{1}{2m^2c^2}\frac{1}{r}\frac{\mathrm{d}V}{\mathrm{d}r}\,\mathbf{L}\cdot\mathbf{S}.$$
> The Thomas term has *halved* the naive coefficient: the factor of $\tfrac12$ in front is the **Thomas half**. This is the correct spin–orbit interaction, and it agrees with the experimentally observed fine-structure splitting of atomic spectral lines (the sodium D doublet, the hydrogen $2p$ splitting). It also agrees *exactly* with the result of the relativistic **Dirac equation**, in which the factor of $\tfrac12$ emerges automatically from the relativistic structure of the electron, with no separate Thomas-precession argument needed.
>
> The historical significance: in $1926$ a calculation of the spin–orbit coupling (predating Dirac) gave the doublet splitting *twice* too large. L. H. Thomas resolved the discrepancy by recognising that the electron's rest frame rotates relative to the laboratory — the precession this exercise computes — and that this rotation contributes an energy halving the naive result. The agreement of Thomas's kinematic argument ($1926$) with Dirac's equation ($1928$) is one of the cleaner confirmations that fine structure is a relativistic effect, and that the Thomas half is real, measurable physics.

> [!note]- Complete formal solution
> In the electron's instantaneous rest frame the nuclear Coulomb field becomes (to first order in $v/c$) a magnetic field $\mathbf{B}' = -\tfrac{1}{c}\mathbf{v}\times\mathbf{E} = -\tfrac{1}{ecr}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{v}\times\mathbf{r}$, with $\mathbf{E} = \tfrac{1}{e}\nabla V$. The naive interaction $H^{\mathrm{naive}}_{\mathrm{SO}} = -\boldsymbol\mu\cdot\mathbf{B}'$ with $\boldsymbol\mu = -\tfrac{e}{mc}\mathbf{S}$ ($g_s=2$) gives, using $\mathbf{v}\times\mathbf{r} = -\mathbf{L}/m$, $H^{\mathrm{naive}}_{\mathrm{SO}} = \tfrac{1}{m^2c^2}\tfrac{1}{r}\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S}$ — twice too large. The electron's centripetal acceleration $\mathbf{a} = -\tfrac1m\nabla V$ makes its rest frame Thomas-precess at $\boldsymbol\Omega_T = \tfrac{1}{2c^2}\mathbf{a}\times\mathbf{v} = -\tfrac{1}{2m^2c^2}\tfrac1r\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}$, contributing $H_T = \mathbf{S}\cdot\boldsymbol\Omega_T = -\tfrac{1}{2m^2c^2}\tfrac1r\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S}$ — half the naive term, opposite sign. The sum is $H_{\mathrm{SO}} = \tfrac{1}{2m^2c^2}\tfrac1r\tfrac{\mathrm{d}V}{\mathrm{d}r}\mathbf{L}\cdot\mathbf{S}$: the Thomas half, matching experiment and the Dirac equation. $\blacksquare$

---

# Key Takeaways

**The electron's rest frame rotates, and that rotation is half the spin–orbit energy.** The central physical insight is that the naive spin–orbit calculation — coupling the electron's moment to the magnetic field it sees — is *incomplete*, because it ignores that the electron's instantaneous rest frame is *rotating* relative to the laboratory (Thomas precession). Including this kinematic rotation contributes an energy $H_T = \mathbf{S}\cdot\boldsymbol\Omega_T$ that is exactly half the naive term and opposite in sign, halving the result. The trigger to recognise this elsewhere: whenever a spin (or any internal degree of freedom) is carried on a curving trajectory and you compute its energy by working in its rest frame, you must account for the *rotation* of that rest frame, not just the fields in it. Forgetting the frame rotation is the standard error, and it produces a factor-of-two discrepancy that is the historical fingerprint of a missing Thomas precession.

**The Thomas half is purely kinematic — no quantum mechanics, no dynamics, just the geometry of accelerated frames.** The factor of $\tfrac12$ that fixes atomic fine structure comes entirely from the low-velocity Thomas precession rate $\boldsymbol\Omega_T = \tfrac12\mathbf{a}\times\mathbf{v}/c^2$, which is a consequence of how Lorentz boosts compose — no quantum mechanics enters its derivation. The reusable principle: a "factor of two" puzzle in a relativistic calculation involving a spin on a curved path is very often a Thomas-precession effect, resolvable by the kinematic rate alone. The diagnostic is the $\tfrac12$ in $\boldsymbol\Omega_T$: it is *the same* $\tfrac12$ as in the fine-structure formula, traceable to the $\Gamma^2/(1+\Gamma)\to\tfrac12$ low-velocity limit of the [[Thm - The Thomas Equation|Thomas equation]]. That a $1926$ kinematic argument agrees exactly with the $1928$ Dirac equation confirms the effect is real and that fine structure is relativistic.

**The sign matters — Thomas precession opposes the orbit, so it subtracts.** The Thomas term *subtracts* half the naive energy rather than adding, because the precession is *opposite* to the orbital sense (the gyroscope lags, as in [[Ex - Thomas precession of a gyroscope in circular orbit|the orbiting-gyroscope exercise]]). Had the sign been the other way, the correction would have *trebled* the splitting rather than halving it, and the agreement with experiment would fail. The reusable check: the Thomas precession $\boldsymbol\Omega_T\propto\mathbf{a}\times\mathbf{v}$ always opposes the orbital rotation, so its energy contribution opposes the naive spin–orbit term. The general lesson is that getting the *sign* of a kinematic correction right is as important as getting its magnitude — and the sign here is dictated by the geometry of how a non-rotating frame appears in the laboratory, the same geometry that makes a carried gyroscope lag.

**Two routes to the fine structure converge — Thomas's kinematic half and Dirac's automatic factor.** The deepest takeaway is that the same factor of $\tfrac12$ emerges two ways: from Thomas's explicit kinematic argument (add the precession energy by hand) and from the Dirac equation (where it falls out automatically from the relativistic wave equation, with no separate Thomas-precession step). The agreement is not a coincidence — both are computing the same physical energy — and it is a model of how a semiclassical, intuition-building calculation can capture a result that a full relativistic theory delivers without comment. The reusable meta-lesson: when a fundamental theory produces a number "for free", there is often an illuminating semiclassical reason for it, and finding that reason (here, the rotation of the electron's rest frame) deepens understanding even though the fundamental theory needs no such crutch. This completes the §16.3 trio, showing the [[Def - Thomas Precession|Thomas precession]] running from a deep-space gyroscope ([[Ex - Thomas precession of a gyroscope in circular orbit]]) through its group-theoretic origin ([[Ex - Thomas precession from the composition of two boosts]]) to the hydrogen spectrum.

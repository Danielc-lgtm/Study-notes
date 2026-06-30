---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Acceleration Relative to an Observer"
  - "Thm - Law of Velocity Composition"
  - "Def - Velocity Relative to an Observer"
  - "Thm - Expression of the Four-Acceleration"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature, $u\cdot u = +1$. A particle $\mathcal{P}$ has four-velocity $v$ and four-acceleration $a_{\mathcal{P}} = \mathrm{d}v/\mathrm{d}\tau$. Two observers $\mathcal{O}, \mathcal{O}'$ with four-velocities $u, u'$ measure $\mathcal{P}$'s [[Def - Velocity Relative to an Observer|relative velocity]] $V, V'$ and [[Def - Acceleration Relative to an Observer|relative acceleration]] $\boldsymbol{\gamma}, \boldsymbol{\gamma}'$ (the rate of change of relative velocity per unit of the observer's proper time, projected into the observer's rest space). The Lorentz factors are $\Gamma = u\cdot v$, $\Gamma' = u'\cdot v$, and $\Gamma_0 = u\cdot u'$ between observers; $U$ is the velocity of $\mathcal{O}'$ relative to $\mathcal{O}$. **Throughout we assume $\mathcal{O}'$ is inertial**, so its four-acceleration and four-rotation vanish; this is the simplifying hypothesis that makes the law tractable. The [[Def - The Orthogonal Projector onto the Local Rest Space|projector]] onto $E_{u'}$ is $\perp_{u'}$. Full registry on [[Special Relativity VIII — Kinematics II, Change of Observer]].

---

# Statement

> **Law of acceleration composition (for an inertial second observer).** Let $\mathcal{P}$ have relative velocity $V$ and relative acceleration $\boldsymbol{\gamma}$ with respect to $\mathcal{O}$, and $V', \boldsymbol{\gamma}'$ with respect to an **inertial** observer $\mathcal{O}'$. Then the four-acceleration, expressed through $\mathcal{O}'$'s data, is
> $$a_{\mathcal{P}} = \frac{\Gamma'^2}{c^2}\left[\boldsymbol{\gamma}' + \frac{\Gamma'^2}{c^2}(\boldsymbol{\gamma}'\cdot V')\,(V' + c\,u')\right],$$
> and projecting the corresponding relation between $\boldsymbol{\gamma}$ and $\boldsymbol{\gamma}'$ gives, in the **collinear rectilinear case** (particle accelerating along the common direction of motion, $\mathcal{O}'$ inertial), the simple law
> $$\boldsymbol{\gamma}' = \frac{\boldsymbol{\gamma}}{\Gamma_0^3\,(1 - U V_\parallel/c^2)^3}.$$
> Unlike the velocity law, **relative acceleration is not invariant**: $\boldsymbol{\gamma}' \ne \boldsymbol{\gamma}$ even when the relative velocity is instantaneously zero, and the transformation involves the *cube* of the boost factors. In the Galilean limit it reduces to $\boldsymbol{\gamma}' = \boldsymbol{\gamma} + \boldsymbol{\gamma}'_{\mathcal{O}} + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\overrightarrow{OM}) + 2\boldsymbol{\omega}\times V + \dot{\boldsymbol{\omega}}\times\overrightarrow{OM}$, the classical law with centrifugal and Coriolis terms.

---

# Motivation

Having composed velocities, the natural next question is: how do two observers compare the *accelerations* they measure for the same particle? In Newtonian mechanics the answer is the familiar transformation of acceleration between frames — and for two *inertial* frames it is the cleanest possible statement: acceleration is *the same* in all inertial frames, $\mathbf{a}' = \mathbf{a}$. This Galilean invariance of acceleration is the bedrock of Newton's second law: $\mathbf{F} = m\mathbf{a}$ holds identically in every inertial frame because both sides are frame-independent.

Relativity destroys this invariance, and the theorem says by how much. Even between two inertial observers, and even at the instant the particle is momentarily at rest relative to one of them, the relative acceleration is *not* the same — it transforms by powers of the Lorentz factor, with the *cube* appearing in the rectilinear case. The physical reason is that acceleration is (change of velocity)/(change of time), and *both* the velocity increment and the time interval transform relativistically, so their ratio picks up a compounded factor. The velocity-composition law already showed that velocity increments transform nontrivially; differentiating it with respect to the (also-transforming) time produces the extra powers.

This non-invariance is the reason relativistic dynamics cannot keep Newton's second law in the form $\mathbf{F} = m\mathbf{a}$ with frame-independent $\mathbf{a}$: the relativistic law is $f = \mathrm{d}P/\mathrm{d}\tau$ for the [[Def - Four-Momentum and Rest Mass|four-momentum]], a four-vector equation, precisely because three-acceleration is *not* a good frame-independent object. The acceleration-composition law is the kinematic statement that forces dynamics to be rewritten covariantly. It is worth deriving carefully because it is the place where the comfortable Galilean invariance of acceleration visibly fails, and understanding *which* powers of $\Gamma$ appear — and why the cube, not the square — is essential to setting up [[Special Relativity XIII — Energy and Momentum|relativistic dynamics]]. We restrict to an inertial second observer $\mathcal{O}'$ because the fully general law (with $\mathcal{O}'$ accelerating and rotating) carries centrifugal, Coriolis, Euler, and four-rotation terms that obscure the essential relativistic effect; the inertial case isolates it.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a particle's relative acceleration measured by $\mathcal{O}$, transformed to an inertial $\mathcal{O}'$". Its disguises:

The first disguised source is **"a particle under a known force in the lab, viewed from a moving frame"**. A charge in a uniform field, a mass on a relativistic rocket, an electron in an accelerator — each has a lab-frame acceleration that one wants in a co-moving or boosted frame. The bridge is that the lab is $\mathcal{O}$ and the moving frame is the inertial $\mathcal{O}'$. *Example problem:* a charge undergoing constant proper acceleration (hyperbolic motion) has its lab acceleration decrease as it speeds up; the composition law quantifies the decrease.

The second disguised source is **"the instantaneous rest frame of an accelerating particle"**. The particle's *proper acceleration* — its acceleration in its own momentary inertial rest frame — is the natural invariant, and relating it to the lab acceleration is an acceleration-composition with $\mathcal{O}'$ the momentary rest frame. The bridge is that proper acceleration is $\boldsymbol{\gamma}'$ when $V' = 0$. *Example problem:* relate the proper acceleration felt by a rocket passenger to the coordinate acceleration measured from the ground.

The third disguised source is **"the velocity-composition law differentiated"**. Whenever a velocity-transformation result is given as a function of time, its time-derivative is an acceleration-transformation, and the chain rule through the transforming time produces the law. The bridge is that acceleration composition *is* the derivative of velocity composition. *Example problem:* differentiate $V' = (V-U)/(1-UV)$ along the particle's worldline to obtain the longitudinal acceleration transformation $\boldsymbol{\gamma}' = \boldsymbol{\gamma}/[\Gamma_0^3(1-UV)^3]$.

**Targets (Output Amplification)**

The conclusion is the transformed relative acceleration $\boldsymbol{\gamma}'$.

Combine the conclusion with **the four-force law**. Because $\boldsymbol{\gamma}$ is not invariant but the four-acceleration $a_{\mathcal{P}}$ is a genuine four-vector, the natural statement of dynamics is $f = m\,a_{\mathcal{P}}$, a four-vector equation. The further result is relativistic Newton's second law $f = \mathrm{d}P/\mathrm{d}\tau$, manifestly covariant. The combination is useful because it explains *why* dynamics must be written with four-vectors: three-acceleration's non-invariance is the obstruction to a frame-independent $\mathbf{F} = m\mathbf{a}$.

Combine the conclusion with **hyperbolic (constant-proper-acceleration) motion**. A particle with constant proper acceleration $a$ has, by the composition law, a lab acceleration that falls as $a/\Gamma^3$ as the particle approaches $c$. The further result is the hyperbolic worldline $x^2 - t^2 = 1/a^2$ and the asymptotic approach to the light cone without ever reaching it. The combination is nonobvious because "constant acceleration" in the proper sense looks like *decreasing* acceleration from the lab, and the composition law is what reconciles them; see [[Special Relativity XVI — Accelerated Observers]].

Combine the conclusion with **the Galilean limit**. As $U \to 0$ the law degenerates to the classical acceleration-composition with centrifugal, Coriolis, and Euler terms (when the second observer rotates). The further result is the recovery of the rotating-frame fictitious forces of Newtonian mechanics. The combination is useful as a check and as the bridge to the classical theory: the relativistic law contains the entire Newtonian apparatus as its low-speed shadow.

---

# Why Is It True

Acceleration is a *second* derivative — the rate of change of velocity — and the relativistic non-invariance comes from the fact that *two* things transform: the velocity increment and the time over which it occurs.

**The one-line mechanism: $\boldsymbol{\gamma} = \mathrm{d}V/\mathrm{d}t$ transforms badly because both the numerator (velocity increment, by the velocity-composition law) and the denominator (the time interval, by time dilation) transform, and the compounded ratio brings in the cube of the boost factor.**

Take the rectilinear case to see the cube cleanly. The velocity-composition law $V' = (V - U)/(1 - UV)$ says how a velocity increment $\mathrm{d}V$ maps to $\mathrm{d}V'$: differentiating, $\mathrm{d}V' = \mathrm{d}V/[\Gamma_0^2(1 - UV)^2]$ — *two* powers of the boost factor come from differentiating the rational function (the quotient rule produces $(1-UV)^{-2}$, and the $\Gamma_0^2 = 1/(1-U^2)$ is the overall scale). That is two powers. The third power comes from the *time*: $\boldsymbol{\gamma}' = \mathrm{d}V'/\mathrm{d}t'$ uses $\mathcal{O}'$'s time $t'$, and the ratio $\mathrm{d}t'/\mathrm{d}t$ is the time-dilation factor between the frames along the particle's motion, namely $\Gamma_0(1 - UV)$. Dividing the two-power velocity increment by this one-power time increment gives $\boldsymbol{\gamma}' = \boldsymbol{\gamma}\cdot[\Gamma_0^2(1-UV)^2]^{-1}\cdot[\Gamma_0(1-UV)]^{... }$ — assembling the powers, the result is $\boldsymbol{\gamma}/[\Gamma_0^3(1-UV)^3]$. The cube is "two from the velocity, one from the time".

Why is there no invariant analogue — why can't we just absorb the factors into a redefinition? Because the factors depend on the *instantaneous velocity* $V$, which changes along the worldline, so there is no constant rescaling that makes acceleration frame-independent. The four-acceleration $a_{\mathcal{P}} = \mathrm{d}v/\mathrm{d}\tau$ *is* invariant (it is a four-vector, differentiated with respect to the invariant proper time $\tau$), but its projection into an observer's rest space — the three-acceleration $\boldsymbol{\gamma}$ — is not, exactly because the projection and the proper-time-to-observer-time conversion are velocity-dependent. The lesson is that acceleration "wants" to be a four-vector; forcing it into a single observer's rest space is what spoils its invariance.

The Galilean limit confirms the structure: as $U \to 0$ all the boost factors go to $1$, the rest spaces coincide, and the only surviving terms are the kinematic ones from a rotating/accelerating second observer — the centrifugal $\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\overrightarrow{OM})$ and Coriolis $2\boldsymbol{\omega}\times V$ terms of classical mechanics. Relativity adds the powers of $\Gamma$; Newtonian mechanics keeps only the rotation terms.

---

# What Makes This Hard

The conceptual obstacle is the loss of an invariance that feels axiomatic — acceleration is the *same* in all inertial frames in Newtonian physics, and giving that up (even between inertial frames, even at zero relative velocity) is counterintuitive. The non-obvious technical point is the *count* of powers: it is the cube, not the square, in the rectilinear case, and getting this right requires carefully tracking that the velocity increment contributes two powers (from differentiating the rational composition law) and the time dilation contributes one more. The most common error is to differentiate the velocity-composition law but forget that the *time* in the denominator of acceleration also transforms, thereby losing the third power and getting a square instead of a cube.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof (rectilinear case).**

**High-level strategy:**
Start from the rectilinear velocity-composition law $V' = (V-U)/(1-UV)$. Differentiate with respect to the *particle's worldline parameter* to get $\mathrm{d}V'$ in terms of $\mathrm{d}V$ (two powers). Then convert from $\mathcal{O}$'s time to $\mathcal{O}'$'s time using the time-dilation factor $\mathrm{d}t'/\mathrm{d}t = \Gamma_0(1-UV)$ (one more power). Assemble.

**Subgoal decomposition:**

1. **Differentiate the velocity-composition law.** Show $\dfrac{\mathrm{d}V'}{\mathrm{d}V} = \dfrac{1}{\Gamma_0^2(1 - UV)^2}$ (with $U$ constant, since $\mathcal{O}'$ is inertial).
   - *Hint:* Quotient rule on $(V-U)/(1-UV)$; the numerator simplifies to $1 - U^2 = 1/\Gamma_0^2$.
   - *Why needed:* This is the two-power velocity-increment transformation.

2. **Relate the time elements.** Show $\dfrac{\mathrm{d}t'}{\mathrm{d}t} = \Gamma_0(1 - UV)$, where $t, t'$ are the proper times of $\mathcal{O}, \mathcal{O}'$... more precisely the coordinate-time relation along the particle's motion.
   - *Hint:* This is the time-dilation/Doppler-type factor; it equals $\Gamma'/\Gamma$ from the velocity-composition Lorentz-factor law.
   - *Why needed:* It supplies the third power converting $\mathrm{d}V'/\mathrm{d}t$ to $\mathrm{d}V'/\mathrm{d}t'$.

3. **Assemble the acceleration ratio.** Combine $\boldsymbol{\gamma} = \mathrm{d}V/\mathrm{d}t$, $\boldsymbol{\gamma}' = \mathrm{d}V'/\mathrm{d}t'$ via the chain rule.
   - *Hint:* $\boldsymbol{\gamma}' = \dfrac{\mathrm{d}V'}{\mathrm{d}t'} = \dfrac{\mathrm{d}V'}{\mathrm{d}V}\cdot\dfrac{\mathrm{d}V}{\mathrm{d}t}\cdot\dfrac{\mathrm{d}t}{\mathrm{d}t'}$.
   - *Why needed:* It produces $\boldsymbol{\gamma}' = \boldsymbol{\gamma}/[\Gamma_0^3(1-UV)^3]$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Differentiated velocity-composition (rectilinear)
> **Statement:** For an inertial $\mathcal{O}'$ (constant $U$), $\dfrac{\mathrm{d}V'}{\mathrm{d}V} = \dfrac{1}{\Gamma_0^2(1 - UV)^2}$.
>
> **Hint:** Quotient rule.
>
> **Why needed:** It is the two-power velocity-increment factor.
>
> > [!note]- Full proof
> > With $V' = (V - U)/(1 - UV)$ and $U$ constant,
> > $$\frac{\mathrm{d}V'}{\mathrm{d}V} = \frac{(1)(1 - UV) - (V - U)(-U)}{(1 - UV)^2} = \frac{1 - UV + UV - U^2}{(1 - UV)^2} = \frac{1 - U^2}{(1 - UV)^2} = \frac{1}{\Gamma_0^2(1 - UV)^2},$$
> > using $1 - U^2 = 1/\Gamma_0^2$. $\blacksquare$

> [!note]- Lemma 2: The time-dilation factor along the motion
> **Statement:** $\dfrac{\mathrm{d}t'}{\mathrm{d}t} = \Gamma_0(1 - UV)$, where $t', t$ are the proper times of $\mathcal{O}', \mathcal{O}$ parametrising the particle's worldline.
>
> **Hint:** This is $\Gamma'/\Gamma$ from the velocity-composition Lorentz-factor law.
>
> **Why needed:** It supplies the third power.
>
> > [!note]- Full proof
> > Along the particle's worldline, the proper-time element of $\mathcal{P}$ is $\mathrm{d}\tau = \mathrm{d}t/\Gamma = \mathrm{d}t'/\Gamma'$ (each observer's time dilated relative to the particle by its own Lorentz factor). Hence $\mathrm{d}t'/\mathrm{d}t = \Gamma'/\Gamma$. By the velocity-composition Lorentz-factor law ([[Thm - Law of Velocity Composition]]), $\Gamma' = \Gamma\Gamma_0(1 - UV)$, so $\Gamma'/\Gamma = \Gamma_0(1 - UV)$, giving $\mathrm{d}t'/\mathrm{d}t = \Gamma_0(1 - UV)$. $\blacksquare$

> [!note]- Lemma 3: Assembling the cube
> **Statement:** $\boldsymbol{\gamma}' = \dfrac{\boldsymbol{\gamma}}{\Gamma_0^3(1 - UV)^3}$.
>
> **Hint:** Chain rule.
>
> **Why needed:** It is the conclusion in the rectilinear case.
>
> > [!note]- Full proof
> > By the chain rule,
> > $$\boldsymbol{\gamma}' = \frac{\mathrm{d}V'}{\mathrm{d}t'} = \frac{\mathrm{d}V'}{\mathrm{d}V}\cdot\frac{\mathrm{d}V}{\mathrm{d}t}\cdot\frac{\mathrm{d}t}{\mathrm{d}t'} = \frac{1}{\Gamma_0^2(1-UV)^2}\cdot\boldsymbol{\gamma}\cdot\frac{1}{\Gamma_0(1-UV)} = \frac{\boldsymbol{\gamma}}{\Gamma_0^3(1-UV)^3},$$
> > using Lemma 1, $\boldsymbol{\gamma} = \mathrm{d}V/\mathrm{d}t$, and Lemma 2 (inverted: $\mathrm{d}t/\mathrm{d}t' = 1/[\Gamma_0(1-UV)]$). $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> *General invariant form.* Since $\mathcal{O}'$ is inertial, the four-acceleration of $\mathcal{P}$ expressed through $\mathcal{O}'$'s relative velocity and acceleration is (translating [[Thm - Expression of the Four-Acceleration]] / Gourgoulhon eq. 5.54 to mostly-minus)
> $$a_{\mathcal{P}} = \Gamma'^2\left[\boldsymbol{\gamma}' + \Gamma'^2(\boldsymbol{\gamma}'\cdot V')(V' + u')\right]\qquad(c=1),$$
> a genuine four-vector. Projecting this and the corresponding $\mathcal{O}$-expression onto the rest spaces relates $\boldsymbol{\gamma}$ and $\boldsymbol{\gamma}'$.
>
> *Rectilinear case.* Suppose $\mathcal{P}$ moves and accelerates along the common direction $e$ of the relative motion, with $\mathcal{O}'$ inertial. Then by Lemmas 1–3,
> $$\boldsymbol{\gamma}' = \frac{\mathrm{d}V'}{\mathrm{d}V}\cdot\frac{\mathrm{d}V}{\mathrm{d}t}\cdot\frac{\mathrm{d}t}{\mathrm{d}t'} = \frac{1}{\Gamma_0^2(1-UV)^2}\cdot\boldsymbol{\gamma}\cdot\frac{1}{\Gamma_0(1-UV)} = \frac{\boldsymbol{\gamma}}{\Gamma_0^3(1-UV)^3}.$$
>
> *Non-invariance.* At the instant $V = U$ (particle momentarily at rest relative to $\mathcal{O}'$), $1 - UV = 1 - U^2 = 1/\Gamma_0^2$, so $\boldsymbol{\gamma}' = \boldsymbol{\gamma}\Gamma_0^3/\Gamma_0^3\cdot\Gamma_0^{... }$; substituting gives $\boldsymbol{\gamma}' = \boldsymbol{\gamma}\,\Gamma_0^3$ — the relative acceleration is *not* equal to $\boldsymbol{\gamma}$ even at zero relative velocity, confirming acceleration is frame-dependent.
>
> *Galilean limit.* As $U \to 0$, $\Gamma_0 \to 1$, $1 - UV \to 1$, and (restoring a possibly non-inertial, rotating second observer) the general law degenerates to $\boldsymbol{\gamma}' = \boldsymbol{\gamma} + \boldsymbol{\gamma}'_{\mathcal{O}} + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\overrightarrow{OM}) + 2\boldsymbol{\omega}\times V + \dot{\boldsymbol{\omega}}\times\overrightarrow{OM}$, the classical acceleration-composition law with centrifugal and Coriolis terms. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Accelerator physics — synchrotron radiation and the $\Gamma^3$.** The power radiated by an accelerated charge depends on its *proper* acceleration, and translating between the lab acceleration (set by the bending magnets) and the proper acceleration brings in exactly the boost powers of this law; the transverse (circular-motion) case gives the characteristic $\Gamma^4$ enhancement of synchrotron radiation. The application is nonobvious because the radiated power, an electromagnetic quantity, is governed by the kinematic acceleration-transformation derived here; see [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

**Rocketry — the relativistic rocket and constant proper acceleration.** A rocket maintaining constant proper acceleration $g$ (for comfort) has a lab acceleration that falls as $g/\Gamma^3$, so it asymptotes to $c$ without reaching it; the worldline is the hyperbola of [[Special Relativity XVI — Accelerated Observers]]. The application is out-of-distribution because "constant acceleration" means two different things (proper vs. coordinate), and the composition law is the bridge.

**General relativity — geodesic deviation and tidal acceleration.** The relativistic transformation of relative acceleration between observers is the flat-spacetime precursor of the geodesic-deviation equation, where the relative acceleration of nearby freely-falling particles is governed by the Riemann curvature. The application is surprising because the same "acceleration is observer-dependent" theme reappears in curved spacetime as the statement that tidal acceleration is curvature; see [[Riemannian Geometry III — Riemann Curvature and Topology]].

---

# Bridges

- **[[Thm - Law of Velocity Composition]]** — acceleration composition is literally the *derivative* of velocity composition along the worldline. The two powers of the boost factor in $\mathrm{d}V'/\mathrm{d}V$ come from differentiating the rational velocity-composition law, and the third power from the time dilation that is itself the Lorentz-factor part of the velocity law. The acceleration law cannot be stated without the velocity law as its integrand.

- **[[Def - Acceleration Relative to an Observer]]** — the relative acceleration $\boldsymbol{\gamma}$ is the projection of the invariant four-acceleration $a_{\mathcal{P}}$ into an observer's rest space, divided by the appropriate power of $\Gamma$. This theorem is the statement that *that projection* is observer-dependent, even though $a_{\mathcal{P}}$ itself is a frame-free four-vector.

- **Relativistic Newton's second law** — because three-acceleration is not invariant, dynamics must be written as $f = m\,a_{\mathcal{P}} = \mathrm{d}P/\mathrm{d}\tau$, a four-vector equation, rather than $\mathbf{F} = m\mathbf{a}$. This theorem is precisely the kinematic obstruction that forces the covariant formulation of [[Special Relativity XIII — Energy and Momentum]].

- **[[Special Relativity XVI — Accelerated Observers]]** — the constant-proper-acceleration (hyperbolic) worldline is the integral of this law with $\boldsymbol{\gamma}'$ held constant in the momentary rest frame; the lab acceleration $\boldsymbol{\gamma} = \boldsymbol{\gamma}'/\Gamma^3$ then decreases as the particle speeds up, producing the asymptotic approach to the light cone.

---

# Unlocked by This

> [!tip] Why Dynamics Must Be Covariant *(from Relativistic Dynamics)*
> The non-invariance of three-acceleration proven here is the reason relativistic mechanics is written with four-vectors. Newton's $\mathbf{F} = m\mathbf{a}$ relied on acceleration being the same in all inertial frames; once that fails, the only frame-independent law is $f = \mathrm{d}P/\mathrm{d}\tau$ for the [[Def - Four-Momentum and Rest Mass|four-momentum]]. This theorem is the kinematic motivation for the entire covariant dynamics of [[Special Relativity XIII — Energy and Momentum]] and the **[[Special Relativity XV — The Principle of Least Action|action principle]]**.

> [!tip] Geodesic Deviation and Tidal Forces *(from General Relativity)*
> The relativistic transformation of relative acceleration is the special-relativistic seed of the **geodesic-deviation equation** of general relativity, in which the relative acceleration of two nearby freely-falling particles equals (minus) the **Riemann curvature** contracted with their separation and four-velocities. The flat-spacetime statement "relative acceleration is observer-dependent" becomes, in curved spacetime, "relative acceleration of geodesics is tidal force is curvature" — the physical content of [[General Relativity I — Einstein's Equations and Schwarzschild]].

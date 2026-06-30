---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Photon Propagation Direction and Velocity"
  - "Def - Observer and Local Rest Space"
  - "Def - Classification of Four-Vectors"
  - "Def - Velocity Relative to an Observer"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a null vector has $X \cdot X = 0$. The observer $\mathcal{O}$ has four-velocity $U_0$ (future timelike unit, $U_0 \cdot U_0 = 1$), four-acceleration $A_0$, four-rotation $\boldsymbol\omega$, and [[Def - Observer and Local Rest Space|local rest space]] $E_{U_0} = U_0^\perp$. A photon has [[Def - Photon Propagation Direction and Velocity|adapted null vector]] $\ell = U_0 + N$ with $\ell \cdot U_0 = 1$ and propagation direction $N$ ($N \cdot U_0 = 0$, $|\mathbf N| = 1$). The photon's position vector in the rest space is $\overrightarrow{OM}$; $\mathbf V$ is the photon's velocity relative to $\mathcal{O}$ and $\|\mathbf V\|_g$ its norm. Full registry on [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]].

---

# Statement

> **Theorem (invariance of the velocity of light).** Let $\mathcal{O}$ be any observer and $\mathcal{P}$ a photon crossing $\mathcal{O}$'s worldline at the instant considered (position vector $\overrightarrow{OM} = 0$), or let $\mathcal{O}$ be inertial. Then the velocity of the photon relative to $\mathcal{O}$ has norm exactly the speed of light:
> $$\boxed{\;\|\mathbf V\|_g = c\;}\qquad(\text{with }c=1:\ |\mathbf V| = 1),$$
> independent of the observer's state of motion — its velocity, its acceleration, or its rotation.

> **Corollary (general observer at a distance).** For an arbitrary observer measuring a photon at $\overrightarrow{OM} \neq 0$, the velocity is $\mathbf V = (1 + A_0 \cdot \overrightarrow{OM})\,c\,N - \boldsymbol\omega \times_{U_0} \overrightarrow{OM}$, whose norm may differ from $c$ when the observer is non-inertial. The invariance $\|\mathbf V\|_g = c$ is exact only locally (at the observer's position) or for inertial observers everywhere.

The constancy of the speed of light, which Einstein elevated to a postulate, is here a *derived* consequence of two facts: photons travel on null geodesics, and the adapted null vector decomposes as $\ell = U_0 + N$ with $N$ a unit vector. The experimental confirmations are the Michelson–Morley experiment (independence from the *direction* of the observer's motion) and the Kennedy–Thorndike experiment (independence from its *magnitude*).

---

# Motivation

Einstein's 1905 derivation of special relativity took the constancy of the speed of light as one of two postulates: light propagates at $c$ in every inertial frame, regardless of the motion of the source or the observer. This is the bombshell that forces the [[Def - The Lorentz Transformation|Lorentz transformation]] and the relativity of simultaneity. But a postulate is an assumption, and a natural question is whether, once the geometric structure of spacetime is in place, the constancy of light can be *derived* rather than assumed — and if so, what its precise scope is.

This theorem answers both. Given that photons travel on null geodesics (the geometric statement that light moves along the light cone), the constancy of its speed follows from pure algebra: the adapted null vector $\ell$, normalised against the observer by $\ell \cdot U_0 = 1$, has a rest-space part $N$ that the null condition forces to be a *unit* vector, and the speed of light is the norm of that unit vector, exactly $c$. No coordinate transformation is needed; the result holds for *any* observer's four-velocity $U_0$, not just inertial ones, provided the measurement is local. The role of the theorem is thus to demote the constancy of light from an axiom to a theorem — to show it is built into the null character of light and the geometry of the rest space — and simultaneously to *sharpen its scope*: it is exactly true locally, and for distant measurements by a non-inertial observer it acquires corrections.

The deeper significance is that the corrections are not a failure but a preview of gravity. A uniformly accelerated observer measuring a distant photon finds a *position-dependent* coordinate speed, $c(1 + A_0\cdot\overrightarrow{OM})$, less than $c$ behind them and more in front. By the equivalence principle this is indistinguishable from light in a uniform gravitational field, where light bends and slows in a potential. So the precise statement of the theorem — local invariance, with position-dependent corrections for accelerated observers — is exactly the structure that, promoted to a curved metric, becomes the bending of starlight and the Shapiro time delay. The constancy of light is exact in the tangent space at each event and approximate in a neighbourhood, which is the hallmark of every local-versus-global statement in relativity.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\mathcal{P}$ is a photon (null worldline) and the measurement is local ($\overrightarrow{OM} = 0$) or the observer is inertial". The point is to recognise the configuration.

The first disguised source is **"a beam of light is observed by a moving detector"**. Any laboratory measurement of the speed of light is an observer (the detector) clocking a photon at the detector's own location, so $\overrightarrow{OM} = 0$ and the theorem applies: the measured speed is $c$ regardless of how the lab moves. The bridge is that a local measurement is the $\overrightarrow{OM} = 0$ case. *Example problem:* the Michelson–Morley interferometer, in which two perpendicular light paths are compared as the apparatus moves with the Earth, finds no difference. See [[Ex - Michelson-Morley null result]].

The second disguised source is **"the photon's tangent is null"**. Any massless particle — photon, gluon, graviton — has a null worldline, hence an adapted null vector $\ell = U_0 + N$ with unit $N$, hence relative speed $c$. The bridge is that "massless" is equivalent to "null worldline", and the null condition is what forces $|\mathbf N| = 1$. The nonobviousness is that the result depends only on nullity, not on the particle being electromagnetic. *Example problem:* show any massless particle travels at $c$ for every local observer, so the speed $c$ is the universal speed of massless particles, not specifically of light.

The third disguised source is **"a source emits light while moving"**. The constancy holds regardless of the source's velocity, because the photon's worldline is null independent of how it was produced — the speed of light does not inherit the source's velocity. The bridge is that the emission process fixes the photon's direction and frequency but not its speed, which is locked to $c$ by nullity. *Example problem:* light from the two halves of a binary star's orbit, emitted by sources moving toward and away from us, arrives at the same speed; de Sitter's analysis bounds any source-velocity dependence to $|k| < 0.002$, and the decay $\pi^0 \to \gamma\gamma$ of fast pions to $k = (-3\pm13)\times10^{-5}$.

**Targets (Output Amplification)**

The conclusion is "$\|\mathbf V_{\mathrm{light}}\| = c$ for every local observer".

Combine the conclusion with **the relativity of two perpendicular directions**. If the speed of light is $c$ in every direction for a moving observer, then no orientation of an interferometer arm is special, and rotating the apparatus produces no fringe shift. The further result is the Michelson–Morley null result, which tests the *isotropy* of $\|\mathbf V_{\mathrm{light}}\|$ — its independence from the direction of the observer's motion through any hypothetical aether. The combination is useful because it converts the abstract invariance into a concrete, falsifiable optical experiment.

Combine the conclusion with **the variation of the observer's speed over a year**. If the speed of light is independent of the *magnitude* of the observer's velocity, then as the Earth's orbital speed changes through the seasons, an unequal-arm interferometer held fixed shows no fringe drift. The further result is the Kennedy–Thorndike null result, which tests independence from the *magnitude* of the observer's velocity — the half of the constancy postulate that Michelson–Morley does not reach. The combination is nonobvious because it isolates a different free parameter (magnitude versus direction) and requires unequal arms and long observation rather than rotation.

Combine the conclusion with **the equivalence principle**. If a *uniformly accelerated* observer measures a position-dependent speed of light $c(1 + A_0\cdot\overrightarrow{OM})$, then — since acceleration is locally indistinguishable from a gravitational field — light in a gravitational potential travels at a position-dependent coordinate speed, bending toward higher potential and arriving delayed. The further result is gravitational light deflection and the Shapiro time delay. The combination is the deepest one: a kinematic correction in flat spacetime becomes a gravitational effect, the bridge to [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]].

---

# Why Is It True

The theorem is one algebraic identity dressed in physical clothing, and the identity is that the spatial part of a null vector normalised by $\ell \cdot U_0 = 1$ has Euclidean length exactly one.

Here is the whole argument. A photon's tangent is null, so the adapted vector satisfies $\ell \cdot \ell = 0$. Decompose it orthogonally against the observer: $\ell = U_0 + N$, where $U_0$ is the timelike part (with the normalisation $\ell \cdot U_0 = 1$ ensuring the coefficient of $U_0$ is exactly $1$) and $N$ is the rest-space part. Expand the null condition:
$$
0 = (U_0 + N)\cdot(U_0 + N) = \underbrace{U_0 \cdot U_0}_{1} + 2\underbrace{N \cdot U_0}_{0} + N \cdot N = 1 + N\cdot N.
$$
So $N \cdot N = -1$, which in the Euclidean rest-space metric is $|\mathbf N| = 1$. The propagation direction is automatically a *unit* vector. Since the photon's velocity (for a local or inertial observer) is $\mathbf V = cN$, its norm is $c|\mathbf N| = c$. **The constancy of the speed of light is the statement that the timelike part $U_0$ and the spacelike part $N$ of a null vector have equal and opposite norms — and since $U_0$ has norm one, $N$ has norm one, so the speed is one.** The $+1$ from the timelike part is exactly cancelled by the $-1$ from the spacelike part, which is what "null" means.

Why does this hold for *any* observer, not just inertial ones? Because the argument used only two facts: $U_0 \cdot U_0 = 1$ (every observer's four-velocity is a unit vector, inertial or not) and the null condition $\ell \cdot \ell = 0$ (the photon's worldline is null, a property of the photon, not the observer). Neither mentions the observer's acceleration or rotation. So every observer at a point of their own worldline measures the same unit propagation direction and the same speed $c$. The observer-dependence enters only in the *direction* $N$ (different observers see the photon coming from different directions — aberration) and the *frequency* (Doppler), never in the *speed*.

Why does the result acquire corrections for a distant, accelerated observer? Because then the photon is not at the observer's location, and computing the rate of change of its rest-space position involves the tilting and rotating of the observer's rest space as the observer accelerates. The extra factor $1 + A_0 \cdot \overrightarrow{OM}$ measures how much the observer's notion of "now" and "here" shifts between the photon's successive positions, and the cross term $\boldsymbol\omega \times \overrightarrow{OM}$ is the rotation of the axes. These are exactly the inertial-frame effects of a non-inertial observer, and they vanish at the observer's own position ($\overrightarrow{OM} = 0$) and for an inertial observer ($A_0 = 0$, $\boldsymbol\omega = 0$). The local invariance is exact; the global statement is the inertial special case.

---

# What Makes This Hard

The local proof is a three-line expansion of $\ell \cdot \ell = 0$, so the difficulty is not the algebra but two conceptual hurdles. First, accepting that the constancy of light is a *theorem* rather than a postulate — that it follows from nullity and the unit-norm of $U_0$, with no appeal to a Lorentz transformation — which inverts the usual logical order students learn. Second, getting the *scope* right: the result is exact only locally, and a uniformly accelerated observer measures a position-dependent speed for distant light. The common error is to over-generalise the theorem to "the speed of light is always $c$ for everyone everywhere", missing the $\overrightarrow{OM} = 0$ qualification and thereby missing the entire bridge to gravitational light-bending. The non-obvious step is recognising that the $+1$ from the timelike part and the $-1$ from the spacelike part of a null vector cancel by definition, and that this cancellation *is* the constancy of light.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Adapt a null vector to the observer by $\ell \cdot U_0 = 1$, decompose it orthogonally as $\ell = U_0 + N$, and expand the null condition $\ell \cdot \ell = 0$ to force $|\mathbf N| = 1$. The photon's velocity (locally, or for an inertial observer) is $\mathbf V = cN$, of norm $c$. For the general case, compute the rate of change of the rest-space position and read off the correction factor.

**Subgoal decomposition:**

1. **Decompose the adapted null vector.** Show $\ell = U_0 + N$ with $N \cdot U_0 = 0$, given $\ell \cdot U_0 = 1$.
   - *Hint:* The orthogonal decomposition of $\ell$ against $U_0$ has timelike part $(\ell \cdot U_0)U_0 = U_0$ and rest-space part $N = \perp_{U_0}\ell$.
   - *Why needed:* It isolates the spatial propagation direction $N$, whose norm is the speed.

2. **Force the propagation direction to be a unit vector.** Expand $\ell \cdot \ell = 0$ to get $N \cdot N = -1$, i.e. $|\mathbf N| = 1$.
   - *Hint:* $(U_0 + N)\cdot(U_0 + N) = U_0\cdot U_0 + 2N\cdot U_0 + N\cdot N = 1 + 0 + N\cdot N$.
   - *Why needed:* It is the crux — the null condition makes the spatial direction unit length, hence the speed $c$.

3. **Read off the speed.** Conclude $\mathbf V = cN$ (local or inertial) has norm $\|\mathbf V\| = c|\mathbf N| = c$.
   - *Hint:* The velocity of light relative to a local/inertial observer is $c$ times the propagation direction.
   - *Why needed:* It is the statement of the theorem.

4. **General case: compute the correction.** For $\overrightarrow{OM} \neq 0$, work out $\mathbf V = (1 + A_0\cdot\overrightarrow{OM})cN - \boldsymbol\omega\times_{U_0}\overrightarrow{OM}$ and note its norm departs from $c$ for non-inertial observers.
   - *Hint:* Differentiate the photon's rest-space position, accounting for the tilt ($A_0$) and rotation ($\boldsymbol\omega$) of the observer's frame.
   - *Why needed:* It delimits the scope and exposes the gravitational analogy.

---

# Lemma Decomposition

> [!note]- Lemma 1: The adapted null vector decomposes as $\ell = U_0 + N$
> **Statement:** A future null vector $\ell$ normalised by $\ell \cdot U_0 = 1$ decomposes orthogonally with respect to $U_0$ as $\ell = U_0 + N$, where $N := \perp_{U_0}\ell$ lies in the rest space ($N \cdot U_0 = 0$).
>
> **Hint:** Use the orthogonal decomposition of any vector against the unit timelike $U_0$.
>
> **Why needed:** It produces the propagation direction $N$, the object whose norm is the speed of light.
>
> > [!note]- Full proof
> > Any vector $X$ decomposes against the unit timelike $U_0$ (with $U_0 \cdot U_0 = 1$) as $X = (X \cdot U_0)U_0 + \perp_{U_0}X$, where $\perp_{U_0}X = X - (X\cdot U_0)U_0$ is the rest-space part, orthogonal to $U_0$. Applying this to $\ell$ with $\ell \cdot U_0 = 1$ gives $\ell = 1\cdot U_0 + \perp_{U_0}\ell = U_0 + N$ where $N := \perp_{U_0}\ell$. By construction $N \cdot U_0 = (\perp_{U_0}\ell)\cdot U_0 = 0$. $\blacksquare$

> [!note]- Lemma 2: The propagation direction is a unit vector
> **Statement:** The null condition $\ell \cdot \ell = 0$ forces $N \cdot N = -1$, i.e. $|\mathbf N| = \sqrt{-N\cdot N} = 1$.
>
> **Hint:** Expand $(U_0 + N)\cdot(U_0 + N) = 0$ using $U_0 \cdot U_0 = 1$ and $N \cdot U_0 = 0$.
>
> **Why needed:** It is the algebraic heart of the theorem — the source of the speed being exactly $c$.
>
> > [!note]- Full proof
> > Since $\ell$ is null, $\ell \cdot \ell = 0$. Substituting $\ell = U_0 + N$ and expanding the bilinear form, $0 = (U_0 + N)\cdot(U_0 + N) = U_0 \cdot U_0 + 2\,N \cdot U_0 + N \cdot N$. By Lemma 1, $N \cdot U_0 = 0$, and the observer four-velocity is unit, $U_0 \cdot U_0 = 1$. Hence $0 = 1 + 0 + N\cdot N$, so $N \cdot N = -1$. As $N$ is spacelike, its Euclidean rest-space norm is $|\mathbf N| = \sqrt{-N\cdot N} = \sqrt{1} = 1$. This used only $U_0 \cdot U_0 = 1$ (true for any observer) and $\ell \cdot \ell = 0$ (the photon's nullity), so it holds for every observer. $\blacksquare$

> [!note]- Lemma 3: The photon velocity is $cN$ locally or for an inertial observer
> **Statement:** When the photon crosses the observer's worldline ($\overrightarrow{OM} = 0$) or the observer is inertial, the photon's velocity relative to $\mathcal{O}$ is $\mathbf V = cN$, of norm $c$.
>
> **Hint:** The velocity is the rate of change of the rest-space position; for a local or inertial observer the correction terms vanish.
>
> **Why needed:** It connects the unit propagation direction to the measured speed, giving $\|\mathbf V\| = c$.
>
> > [!note]- Full proof
> > The velocity of the photon relative to $\mathcal{O}$ is, in general, $\mathbf V = (1 + A_0\cdot\overrightarrow{OM})\,c\,N - \boldsymbol\omega\times_{U_0}\overrightarrow{OM}$ (derived in [[Def - Photon Propagation Direction and Velocity]] by differentiating the photon's rest-space position). When $\overrightarrow{OM} = 0$ (photon at the observer's location) both correction terms vanish, giving $\mathbf V = cN$. When $\mathcal{O}$ is inertial, $A_0 = 0$ and $\boldsymbol\omega = 0$, again giving $\mathbf V = cN$ for all $\overrightarrow{OM}$. By Lemma 2, $|\mathbf N| = 1$, so $\|\mathbf V\|_g = c|\mathbf N| = c$. $\blacksquare$

> [!note]- Lemma 4: The general (distant, non-inertial) correction
> **Statement:** For an arbitrary observer at $\overrightarrow{OM} \neq 0$, $\mathbf V = (1 + A_0\cdot\overrightarrow{OM})\,c\,N - \boldsymbol\omega\times_{U_0}\overrightarrow{OM}$, whose norm differs from $c$ when $A_0 \neq 0$ or $\boldsymbol\omega \neq 0$.
>
> **Hint:** The factor $1 + A_0\cdot\overrightarrow{OM}$ comes from the tilt of the observer's simultaneity surfaces between the photon's successive positions.
>
> **Why needed:** It delimits the scope of the invariance and exposes the gravitational analogy.
>
> > [!note]- Full proof
> > Computing $\mathbf V = \mathrm{d}\mathbf x/\mathrm{d}t$ for the photon requires the rate of change of its position vector $\overrightarrow{OM}$ in the observer's rest space. For a non-inertial observer this rest space tilts (rate set by the four-acceleration $A_0$) and rotates (rate set by the four-rotation $\boldsymbol\omega$), so the derivative of $\overrightarrow{OM}$ picks up the terms $c(A_0\cdot\overrightarrow{OM})N$ (from the tilt) and $-\boldsymbol\omega\times_{U_0}\overrightarrow{OM}$ (from the rotation), giving $\mathbf V = (1 + A_0\cdot\overrightarrow{OM})cN - \boldsymbol\omega\times_{U_0}\overrightarrow{OM}$. Its norm is $c|1 + A_0\cdot\overrightarrow{OM}|$ along $N$ plus the rotation contribution, which equals $c$ only when $\overrightarrow{OM} = 0$ or the observer is inertial. For a uniformly accelerated observer, light behind them ($A_0\cdot\overrightarrow{OM} < -1$) can even appear to stand still or recede — the kinematic precursor of a horizon. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{P}$ be a photon, so its worldline is a null geodesic and the adapted null vector $\ell$ (normalised by $\ell \cdot U_0 = 1$) satisfies $\ell \cdot \ell = 0$.
>
> By Lemma 1, $\ell$ decomposes orthogonally against the observer's four-velocity as $\ell = U_0 + N$ with $N = \perp_{U_0}\ell$ in the rest space, $N \cdot U_0 = 0$.
>
> By Lemma 2, the null condition gives $1 + N\cdot N = 0$, so $N \cdot N = -1$ and the propagation direction is a unit vector, $|\mathbf N| = 1$. This used only $U_0 \cdot U_0 = 1$ and $\ell \cdot \ell = 0$, so it holds for *any* observer.
>
> By Lemma 3, when the photon crosses $\mathcal{O}$'s worldline ($\overrightarrow{OM} = 0$) or $\mathcal{O}$ is inertial, the photon's velocity relative to $\mathcal{O}$ is $\mathbf V = cN$, of norm
> $$\|\mathbf V\|_g = c\,|\mathbf N| = c,$$
> independent of the observer's velocity, acceleration, or rotation. This is the statement of the theorem.
>
> By Lemma 4, for a general non-inertial observer measuring a photon at $\overrightarrow{OM} \neq 0$, the velocity is $\mathbf V = (1 + A_0\cdot\overrightarrow{OM})cN - \boldsymbol\omega\times_{U_0}\overrightarrow{OM}$, whose norm departs from $c$ — establishing the corollary and delimiting the invariance to local measurements (or inertial observers). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Metrology — the speed of light as a defined constant.** Since 1983 the metre is *defined* by fixing $c = 299\,792\,458\ \mathrm{m\,s^{-1}}$ exactly, so the speed of light is no longer measured but used to define length. This is only coherent because the speed is observer-independent — the theorem is what licenses making $c$ a defining constant. Computing how a length standard would drift if the speed of light depended on the laboratory's motion (it does not, to better than $10^{-17}$ in modern cavity experiments) is the metrological reading of the invariance.

**Astronomy — stellar aberration and the constancy of the *speed* but not *direction* of light.** The annual aberration of starlight — the $20.5''$ ellipse a star traces as the Earth orbits — is the observer-dependence of the propagation *direction* $N$, while the *speed* stays $c$. Computing the aberration angle from the Earth's orbital velocity, and confirming it affects direction not speed, separates the two observer-dependent aspects of light. This connects directly to the [[Thm - Aberration of Light|aberration]] law of [[Special Relativity VIII — Kinematics II, Change of Observer]] and was historically the first measurement (Bradley 1728) consistent with a finite, frame-independent $c$.

**General relativity — the Shapiro delay as position-dependent light speed.** A radar signal grazing the Sun on its way to a planet and back is delayed by tens of microseconds relative to flat-spacetime expectation, because the coordinate speed of light is reduced in the Sun's gravitational potential. This is the corollary's factor $1 + A_0\cdot\overrightarrow{OM}$ promoted to a gravitational potential via the equivalence principle. Estimating the Shapiro delay from the position-dependent coordinate speed is the gravitational application, the bridge from this theorem to the tests of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]].

---

# Bridges

- **[[Def - Photon Propagation Direction and Velocity]]** — the construction this theorem rests on. The propagation direction $N$ is defined there as the rest-space part of the adapted null vector, and the unit-norm property $|\mathbf N| = 1$ proved there *is* the constancy of the speed of light. This theorem is the statement that $|\mathbf N| = 1$ for every observer, with the scope (local, or inertial) made explicit; the definition supplies the object, the theorem certifies its universality.

- **[[Thm - Maximum Relative Velocity is c]]** — the companion bound. That theorem gives $|\mathbf V| < c$ strictly for massive particles; this one gives $|\mathbf V| = c$ exactly for photons. Together they say $c$ is simultaneously the unreachable ceiling for massive particles and the universal, observer-independent speed of light, both forced by the geometry of timelike and null vectors — the strict inequality from the unit-norm of a timelike four-velocity, the equality from the nullity of the photon's tangent.

- **[[Def - The Lorentz Transformation]]** — the logical inversion. Einstein took the constancy of light as a postulate and *derived* the Lorentz transformation; this theorem derives the constancy from the geometry, closing the logical loop. The two are equivalent — the constancy of light and the Lorentz invariance of the metric each imply the other — but the geometric route shows the constancy is a property of null vectors in a Minkowski metric, valid for accelerated observers too, which the postulate-based route (about inertial frames) does not make manifest.

- **Gravitational light deflection** — the curved-spacetime sequel. The corollary's position-dependent speed for accelerated observers, $c(1 + A_0\cdot\overrightarrow{OM})$, becomes, via the equivalence principle, the statement that light bends and slows in a gravitational potential. Promoting the flat metric to a curved $g_{\mu\nu}(x)$ turns the factor $1 + A_0\cdot\overrightarrow{OM}$ into the gravitational redshift factor and produces the deflection of starlight and the Shapiro delay — the bridge from this chapter to [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Unlocked by This

> [!tip] Aberration, Doppler, and the Conformal Sky *(from Change of Observer and the Spinor Map)*
> The speed of light is observer-independent, but its *direction* $N$ and *frequency* are not. Changing the observer maps the propagation direction by a conformal transformation of the celestial sphere — a **Möbius transformation** of $\mathbb{CP}^1$ — giving stellar [[Thm - Aberration of Light|aberration]], and shifts the frequency, giving the [[Thm - The Doppler Effect|Doppler effect]]. These are the content of **Special Relativity VIII** and, in spinor form, **Special Relativity XI**, where the Lorentz group is realised as the conformal automorphisms of the sky.

> [!tip] The Equivalence Principle and the Bending of Light *(from General Relativity)*
> The position-dependent coordinate speed of light for an accelerated observer, $c(1 + A_0\cdot\overrightarrow{OM})$, is — by the **equivalence principle** — the speed of light in a gravitational potential. Promoting the flat metric to a curved $g_{\mu\nu}(x)$, light follows null geodesics that bend toward stronger potential and arrive delayed: the **deflection of starlight by the Sun** (Eddington 1919) and the **Shapiro time delay**, the classic confirmations of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]]. The local invariance of the speed of light, holding exactly only at a point, is precisely the statement that special relativity is the tangent-space approximation to a curved spacetime.

---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \operatorname{diag}(+1,-1,-1,-1)$. A particle has [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu$. An [[Def - Observer and Local Rest Space|observer]] $\mathcal{O}$ has four-velocity $U_0$ ($U_0\cdot U_0 = 1$, future-directed) and [[Def - Observer and Local Rest Space|local rest space]] $U_0^\perp$ (the three-dimensional space of vectors orthogonal to $U_0$). The orthogonal projector onto $U_0^\perp$ is $\perp_{U_0}$. The energy of the particle measured by $\mathcal{O}$ is $E$, its three-momentum $\mathbf{p}$ (a vector in $U_0^\perp$). Full registry on [[Special Relativity XIII — Energy and Momentum]].

---

# Statement

> **Energy and momentum relative to an observer.** Let a particle have [[Def - Four-Momentum and Rest Mass|four-momentum]] $P$, and let $\mathcal{O}$ be an [[Def - Observer and Local Rest Space|observer]] with four-velocity $U_0$. The **energy** of the particle measured by $\mathcal{O}$ is the invariant contraction
> $$E \;=\; P\cdot U_0 \qquad\big(\text{with } c:\ E = c\,P\cdot U_0\big),$$
> and the **three-momentum** measured by $\mathcal{O}$ is the orthogonal projection of $P$ onto the local rest space,
> $$\mathbf{p} \;=\; \perp_{U_0} P \;=\; P - (P\cdot U_0)\,U_0,$$
> a vector orthogonal to $U_0$ ($\mathbf{p}\cdot U_0 = 0$) and spacelike. Together they give the **orthogonal decomposition**
> $$P \;=\; E\,U_0 + \mathbf{p}, \qquad \mathbf{p}\cdot U_0 = 0,$$
> whose Minkowski square reproduces the **energy–momentum relation**
> $$P\cdot P = E^2 - \mathbf{p}\cdot\mathbf{p}\,(-1) \;\Longrightarrow\; E^2 = m^2 + |\mathbf{p}|^2,$$
> where $|\mathbf{p}|^2 = -\mathbf{p}\cdot\mathbf{p} \ge 0$ is the Euclidean square of the spatial momentum and $m^2 = P\cdot P$ is the rest mass squared. The energy and momentum are **relative** to the observer; the rest mass $m$ is absolute.

---

# Motivation

The [[Def - Four-Momentum and Rest Mass|four-momentum]] $P$ is an *absolute* object: it belongs to the particle, the same four-vector for every observer. But energy and momentum are things observers *measure*, and different observers measure different values — a particle that is fast (high energy) to one observer is at rest (energy $= m$) to another. So there must be a map from the absolute four-momentum and a chosen observer to the energy and momentum that observer reads off. This theorem is that map, and it is the cleanest possible one: a single contraction for the energy, a single projection for the momentum.

The reason the construction is forced is that an observer's worldline picks out a *splitting* of spacetime at each event: a time direction (the observer's four-velocity $U_0$) and a complementary space (the [[Def - Observer and Local Rest Space|local rest space]] $U_0^\perp$, the events the observer calls "simultaneous and here"). Any four-vector, including the four-momentum, decomposes along this splitting into a time part and a space part. The time part — the component along $U_0$ — is the energy; the space part — the projection onto $U_0^\perp$ — is the three-momentum. This is exactly the relativistic statement that "energy is the time-component of the four-momentum" and "momentum is its space-component", made precise by *which* observer's time and space.

The elegance is that the energy is an *inner product*, $E = P\cdot U_0$, hence a Lorentz scalar in the combined particle-plus-observer system. This is not a contradiction with energy being observer-dependent: the energy depends on *which* $U_0$ you contract with, but for a fixed observer it is an invariant, computable in any frame. The practical payoff is enormous: to find the energy a moving observer assigns to a particle, you do not transform coordinates and recompute — you contract the particle's four-momentum with the observer's four-velocity, a single scalar operation. For a photon this gives the relativistic Doppler effect in one line, $E = \hbar\,U_0\cdot K$; for a massive particle it gives the energy in any frame without boosting.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a four-momentum and an observer", and input-broadening is about recognising when the contraction/projection is the right tool.

The first disguised source is **"a particle's energy is wanted in a frame other than the one it is given in"**. Rather than Lorentz-transform the components, recognise the energy as $P\cdot U_0$ with $U_0$ the new observer's four-velocity. The bridge is that energy is a contraction, hence frame-independent once $U_0$ is fixed. *Example problem:* finding the energy of a cosmic ray as measured by an observer moving towards it.

The second disguised source is **"a photon's frequency is wanted relative to a moving observer"**. The photon energy is $E = P\cdot U_0 = \hbar\,U_0\cdot K$, so the Doppler-shifted frequency is the contraction of the wave four-vector with the observer's four-velocity. The bridge is $P = \hbar K$ ([[Def - The Four-Momentum of a Photon]]). *Example problem:* the relativistic Doppler effect, $\omega_{\text{obs}} = U_0\cdot K$.

The third disguised source is **"the relative energy of two particles is wanted"**. The energy of particle 2 in the rest frame of particle 1 is $E_{2,1} = P_2\cdot U_1$, where $U_1 = P_1/m_1$ is particle 1's four-velocity. The bridge is that any particle's rest frame is an observer whose four-velocity is its normalised four-momentum. *Example problem:* the energy of an incoming particle as seen by a target at rest, the starting point of fixed-target threshold calculations.

**Targets (Output Amplification)**

The conclusions are $E = P\cdot U_0$, $\mathbf{p} = \perp_{U_0}P$, and the decomposition $P = E U_0 + \mathbf{p}$.

Combine the decomposition with **squaring**. Taking $P\cdot P$ of $P = EU_0 + \mathbf{p}$ and using $U_0\cdot U_0 = 1$, $\mathbf{p}\cdot U_0 = 0$, $\mathbf{p}\cdot\mathbf{p} = -|\mathbf{p}|^2$ gives $m^2 = E^2 - |\mathbf{p}|^2$, the energy–momentum relation. The further result is that the [[Thm - Mass-Energy Equivalence|mass–energy relation]] is just the squared decomposition. The combination is useful because it shows the dispersion relation is a *Pythagorean* statement in the observer's splitting. *Example:* deriving $E^2 = \mathbf{p}^2 + m^2$ geometrically.

Combine $E = P\cdot U_0$ with **the future-directedness of $U_0$ and $P$**. Both being future-directed timelike (or $P$ null), their inner product is *positive*, $E = P\cdot U_0 > 0$: every observer measures positive energy for every particle. The further result is the positivity of energy, frame-independent. The combination is nonobvious because individual components of a four-vector can be negative, but the contraction of two future-directed vectors cannot. *Example:* the impossibility of an observer measuring negative photon energy, even when chasing the photon (the frequency shrinks but stays positive).

---

# Why Is It True

The clean reason is that an observer is a *splitting* of spacetime, and any four-vector splits accordingly. The observer's four-velocity $U_0$ is a future-directed unit timelike vector; it spans the observer's "time axis". The orthogonal complement $U_0^\perp$ — the [[Def - Observer and Local Rest Space|local rest space]] — is a three-dimensional spacelike subspace, the observer's "space". Every vector $V$ in spacetime decomposes uniquely as a piece along $U_0$ plus a piece in $U_0^\perp$:
$$V = (V\cdot U_0)\,U_0 + \big(V - (V\cdot U_0)U_0\big),$$
the first term the projection onto the time axis (using $U_0\cdot U_0 = 1$), the second the projection onto the rest space (orthogonal to $U_0$ by construction). **The energy and momentum are simply the time and space parts of the four-momentum in the observer's own splitting of spacetime.**

For the four-momentum, the time part is $(P\cdot U_0)U_0$, with coefficient $E = P\cdot U_0$ — the energy — and the space part is $P - (P\cdot U_0)U_0 = \mathbf{p}$ — the momentum. In the observer's *own rest frame*, where $U_0 = (1,\mathbf{0})$, the contraction $P\cdot U_0 = P^0$ recovers the familiar "energy is the time component" and the projection recovers "momentum is the spatial components". The theorem is the frame-independent version of these familiar statements: it says *which* time and space, namely the observer's, and packages them as a contraction and a projection so that no coordinates are needed.

That the energy is positive is the geometric fact that the inner product of two future-directed causal vectors is positive — a special feature of the Lorentzian signature. Two future timelike vectors lie in the same half of the light cone, and their Minkowski inner product, $E_1 E_2 - \mathbf{p}_1\cdot\mathbf{p}_2$, is dominated by the energy product (this is the reversed Cauchy–Schwarz inequality). So $E = P\cdot U_0 > 0$ always: there is no observer for whom a particle has negative energy. This is why a photon chased by an observer is redshifted to ever-lower but never-zero frequency.

---

# What Makes This Hard

The subtlety is that energy is *both* observer-dependent and an invariant: it depends on which observer's $U_0$ you choose, but for a fixed observer it is the scalar $P\cdot U_0$, computable in any frame. Beginners either think energy is absolute (it is not — different observers disagree) or think the contraction $P\cdot U_0$ is frame-dependent (it is not — it is a Lorentz scalar). The non-obvious step is realising that "energy" requires *two* inputs, the particle and the observer, and the contraction is the unique bilinear map combining them. The common error is to forget the projection for the momentum and write $\mathbf{p} = $ (spatial part of $P$) in the *wrong* frame, rather than projecting onto the chosen observer's rest space.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Decompose the four-momentum along the observer's four-velocity and its orthogonal complement; identify the time-coefficient as the energy and the orthogonal part as the momentum; verify in the observer's rest frame; square the decomposition to recover the energy–momentum relation.

**Subgoal decomposition:**

1. **Decompose $P$ along $U_0$ and $U_0^\perp$.** Write $P = (P\cdot U_0)U_0 + (P - (P\cdot U_0)U_0)$, the unique split into a part parallel to $U_0$ and a part orthogonal to it.
   - *Hint:* Use $U_0\cdot U_0 = 1$ to verify the parallel coefficient and orthogonality of the remainder.
   - *Why needed:* It produces the energy (coefficient) and momentum (remainder) at once.

2. **Identify the pieces in the observer's rest frame.** Set $U_0 = (1,\mathbf{0})$; then $P\cdot U_0 = P^0$ and the orthogonal part is the spatial $(0,\mathbf{p})$.
   - *Hint:* In the rest frame "energy is the time component, momentum the space components" is recovered.
   - *Why needed:* It confirms the abstract contraction/projection are the familiar energy and momentum.

3. **Square the decomposition.** Compute $P\cdot P = E^2(U_0\cdot U_0) + 2E\,(U_0\cdot\mathbf{p}) + \mathbf{p}\cdot\mathbf{p}$ and simplify.
   - *Hint:* $U_0\cdot U_0 = 1$, $U_0\cdot\mathbf{p} = 0$, $\mathbf{p}\cdot\mathbf{p} = -|\mathbf{p}|^2$.
   - *Why needed:* It yields $m^2 = E^2 - |\mathbf{p}|^2$, the energy–momentum relation.

---

# Lemma Decomposition

> [!note]- Lemma 1: The orthogonal decomposition is unique
> **Statement:** Every four-vector $P$ decomposes uniquely as $P = aU_0 + \mathbf{w}$ with $a = P\cdot U_0$ a scalar and $\mathbf{w} = P - aU_0 \in U_0^\perp$.
>
> **Hint:** Take the inner product of $P = aU_0 + \mathbf{w}$ with $U_0$, using $U_0\cdot U_0 = 1$ and $\mathbf{w}\cdot U_0 = 0$.
>
> **Why needed:** It is what makes "the energy" and "the momentum" well-defined — the splitting into time and space parts is unambiguous.
>
> > [!note]- Full proof
> > Since $U_0$ is timelike with $U_0\cdot U_0 = 1$, the line $\mathbb{R}U_0$ and its orthogonal complement $U_0^\perp$ together span Minkowski space (non-degeneracy of the metric), and they intersect only at $0$, so the decomposition $P = aU_0 + \mathbf{w}$ with $\mathbf{w}\in U_0^\perp$ exists and is unique. Taking the inner product with $U_0$: $P\cdot U_0 = a(U_0\cdot U_0) + \mathbf{w}\cdot U_0 = a\cdot 1 + 0 = a$, so $a = P\cdot U_0$, and $\mathbf{w} = P - (P\cdot U_0)U_0$. $\blacksquare$

> [!note]- Lemma 2: The momentum is spacelike
> **Statement:** The projected momentum $\mathbf{p} = P - (P\cdot U_0)U_0$ satisfies $\mathbf{p}\cdot\mathbf{p} \le 0$ (spacelike or zero).
>
> **Hint:** Compute $\mathbf{p}\cdot\mathbf{p} = m^2 - E^2$ and use $E \ge m$.
>
> **Why needed:** It confirms $|\mathbf{p}|^2 = -\mathbf{p}\cdot\mathbf{p} \ge 0$ is a genuine Euclidean length, so the energy–momentum relation $E^2 = m^2 + |\mathbf{p}|^2$ has the right signs.
>
> > [!note]- Full proof
> > Squaring the decomposition $P = EU_0 + \mathbf{p}$ with $U_0\cdot U_0 = 1$, $\mathbf{p}\cdot U_0 = 0$: $P\cdot P = E^2 + \mathbf{p}\cdot\mathbf{p}$, so $\mathbf{p}\cdot\mathbf{p} = P\cdot P - E^2 = m^2 - E^2$. Since $E = \gamma m \ge m$ for a massive particle (and $E = |\mathbf{p}| \ge 0$ for a photon), $\mathbf{p}\cdot\mathbf{p} = m^2 - E^2 \le 0$: the momentum is spacelike (or zero, when the particle is at rest relative to $\mathcal{O}$). Hence $|\mathbf{p}|^2 := -\mathbf{p}\cdot\mathbf{p} = E^2 - m^2 \ge 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $P$ be the particle's four-momentum and $U_0$ the observer's four-velocity ($U_0\cdot U_0 = 1$). By Lemma 1, $P$ decomposes uniquely as
> $$P = (P\cdot U_0)\,U_0 + \big(P - (P\cdot U_0)U_0\big) = E\,U_0 + \mathbf{p},$$
> with $E := P\cdot U_0$ a Lorentz scalar and $\mathbf{p} := P - (P\cdot U_0)U_0 \in U_0^\perp$, so $\mathbf{p}\cdot U_0 = 0$. In the observer's rest frame $U_0 = (1,\mathbf{0})$, giving $E = P^0$ (the time component) and $\mathbf{p} = (0, P^1, P^2, P^3)$ (the spatial part), confirming that $E$ is the energy and $\mathbf{p}$ the three-momentum the observer measures. By Lemma 2, $\mathbf{p}$ is spacelike with $|\mathbf{p}|^2 = -\mathbf{p}\cdot\mathbf{p} = E^2 - m^2 \ge 0$, and squaring the decomposition gives the **energy–momentum relation**
> $$P\cdot P = E^2 + \mathbf{p}\cdot\mathbf{p} = E^2 - |\mathbf{p}|^2 = m^2 \;\Longrightarrow\; E^2 = m^2 + |\mathbf{p}|^2.$$
> Finally, since $P$ and $U_0$ are both future-directed timelike (or $P$ future-directed null), $E = P\cdot U_0 > 0$: every observer measures positive energy. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Relativistic Doppler effect from the four-momentum.** For a photon, $E = P\cdot U_0 = \hbar\,U_0\cdot K$, so the frequency measured by an observer is the contraction of the wave four-vector with the observer's four-velocity; computing this for emitter and receiver gives the Doppler formula in one line, without coordinate transformations. The application is the cleanest derivation of the Doppler effect, and it generalises immediately to aberration (the *direction* of $\mathbf{p}$ in the observer's rest space). See [[Def - The Four-Momentum of a Photon]].

**Thermodynamics — the energy of a gas in a moving frame.** The total energy of a system measured by a moving observer is $E = (\sum P_a)\cdot U_0$, the contraction of the total four-momentum with the observer's four-velocity. For a box of gas this shows how the internal energy and the kinetic energy of the box combine under a boost, the relativistic transformation of thermodynamic energy. The application connects the contraction formula to relativistic thermodynamics.

**General relativity — the energy measured by a local observer.** In curved spacetime the energy a local observer measures is still $E = -g_{\mu\nu}P^\mu U_0^\nu$ (the metric contraction with the observer's four-velocity), now using the curved metric $g_{\mu\nu}$. This is how gravitational redshift is computed — the same photon contracted with the four-velocities of observers at different gravitational potentials gives different energies. The application carries the contraction formula into general relativity, where it underlies the Pound–Rebka experiment.

---

# Bridges

- **[[Def - Four-Momentum and Rest Mass]]** — this theorem assigns physical names to the components of the four-momentum *relative to an observer*: the contraction with $U_0$ is the energy, the projection is the momentum. It is the bridge between the absolute four-momentum and the observer-dependent energy and momentum, exactly as velocity relative to an observer is built from the absolute four-velocity.

- **[[Thm - Mass-Energy Equivalence]]** — squaring the orthogonal decomposition $P = EU_0 + \mathbf{p}$ reproduces the energy–momentum relation $E^2 = m^2 + |\mathbf{p}|^2$, so mass–energy equivalence is the Pythagorean content of this decomposition in the observer's splitting of spacetime.

- **[[Def - Observer and Local Rest Space]]** — the entire theorem is the action of an observer's splitting (time axis $U_0$, rest space $U_0^\perp$) on the four-momentum. The orthogonal projector $\perp_{U_0}$ onto the rest space is what produces the three-momentum, exactly the same projector that produces velocity relative to the observer from the four-velocity.

- **The contraction $P\cdot U_0$ as a general measurement principle** — that a physical measurement is the contraction of an absolute tensor with the observer's four-velocity is a recurring pattern: energy is $P\cdot U_0$, the frequency an observer sees is $K\cdot U_0$, the proper time rate is $1$, and (for fields) the energy density is $T_{\mu\nu}U_0^\mu U_0^\nu$. The observer's four-velocity is the universal probe that turns absolute geometry into measured numbers.

---

# Unlocked by This

> [!tip] The Relativistic Doppler Effect *(from §13.2)*
> Because a photon's energy is $E = P\cdot U_0 = \hbar\,U_0\cdot K$, the frequency one observer measures is the contraction of the wave four-vector with the observer's four-velocity. Computing this for the emitter and the receiver gives the relativistic **Doppler formula** directly, and the change in the *direction* of the projected momentum gives **aberration** — both without any coordinate transformation.

> [!tip] Energy Density and the Energy–Momentum Tensor *(from Field Theory and General Relativity)*
> The contraction principle generalises from particles to fields: an observer measures the **energy density** of a field as $T_{\mu\nu}U_0^\mu U_0^\nu$, the double contraction of the **energy–momentum tensor** with the observer's four-velocity, and the momentum density and stress are the other projections. This is the field-theoretic analogue of $E = P\cdot U_0$, developed in [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|Special Relativity XXIII]].

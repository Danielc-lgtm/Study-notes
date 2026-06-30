---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Uniformly Rotating Observer"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Local Frame and Four-Rotation"
  - "Def - Lorentz Factor and Relative Velocity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The central [[Def - Uniformly Rotating Observer|uniformly rotating observer]] $\mathcal{O}$ has four-velocity $U$, four-rotation $\vec\omega = \omega e^*_3$, and inertial twin $\mathcal{O}_*$. A corotating observer $\mathcal{O}'$ at radius $r$ has four-velocity $U'$, proper time $t'$, local frame $(e'_\alpha) = (U', e'_1, e'_2, e'_3)$, velocity $\vec V = r\omega\,\vec n$ relative to $\mathcal{O}_*$, and Lorentz factor $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$. The azimuthal unit vector is $\vec n = -\sin\varphi\,e_1 + \cos\varphi\,e_2$; the boost from $U$ to $U'$ is $\Lambda$. The cross product in the rest space of $U'$ is $\times_{U'}$. Full registry on [[Special Relativity XVII — Rotating Observers]].

> [!warning] Convention: Gourgoulhon's opposite signature
> Gourgoulhon (Chapter 13) uses $\mathrm{diag}(-1,+1,+1,+1)$. The norms $\|\vec a'\|$ and $\|\vec\omega'\|$ and the factor $\Gamma$ are positive scalars carried over unchanged; the direction $e'_2$ (radially inward) and the relations below hold in mostly-minus.

---

# Statement

> **Four-acceleration and four-rotation of a corotating observer.** Let $\mathcal{O}'$ be a [[Def - Uniformly Rotating Observer|corotating observer]] at radius $r$ on a disk of angular velocity $\omega$, with Lorentz factor $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$. Then its [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] is
> $$\vec a' = \frac{\Gamma^2}{c^2}\,r\omega^2\, e'_2,$$
> directed radially **inward** (along $e'_2$), with magnitude $\|\vec a'\| = \Gamma^2 r\omega^2$ (in $c = 1$ units) — the relativistic centripetal acceleration, exceeding the Newtonian value $r\omega^2$ by the factor $\Gamma^2$. Its [[Def - Local Frame and Four-Rotation|four-rotation]] is
> $$\vec\omega' = \Gamma^2\,\vec\omega,$$
> larger than the central four-rotation $\vec\omega$ by the same factor $\Gamma^2$. Both are constant along $\mathcal{O}'$'s worldline, so $\mathcal{O}'$ is a stationary observer; both reduce to their Newtonian values only in the limit $\Gamma\to 1$ ($r\omega\ll c$).

---

# Motivation

A point on the rim of a turntable is, intuitively, "just going around in a circle" — and in Newtonian physics that is the end of the story: it has centripetal acceleration $r\omega^2$ and, if it carries no torque, its gyroscopes do not precess. This theorem is the relativistic correction to both halves of that intuition, and the corrections are large and physically important.

The first correction is to the acceleration. The relativistic centripetal acceleration is not $r\omega^2$ but $\Gamma^2 r\omega^2$, enhanced by the square of the Lorentz factor. For a rim approaching the speed of light this enhancement diverges — it costs ever more four-acceleration to keep a fast-moving point on its circular track. This is the rotational analogue of the fact that it takes increasing force to accelerate a fast particle, and it matters for, say, particles in a storage ring or matter at the rim of a rapidly spinning neutron star.

The second correction is deeper and more surprising. A corotating observer's *own* four-rotation $\vec\omega'$ is not equal to the disk's angular velocity $\vec\omega$, but exceeds it by $\Gamma^2$. This means a gyroscope carried by a rim observer precesses *faster* than the disk turns — and, crucially, faster than a gyroscope at the hub. The excess $\vec\omega' - \vec\omega = (\Gamma^2 - 1)\vec\omega$ is a purely relativistic effect with no Newtonian counterpart, and for a particle in circular orbit it is exactly the **Thomas precession**: a torque-free gyroscope dragged around a circle precesses relative to the inertial frame, because the succession of boosts that hold it on its track do not commute. The theorem thus quantifies, for the rotating disk, the kinematic precession that in atomic physics produces the Thomas factor of $\tfrac12$ in the spin–orbit coupling.

The role of the theorem in the chapter is foundational: it supplies the kinematic invariants of the corotating congruence, and the constancy of $\vec a'$ and $\vec\omega'$ along each worldline is what makes the corotating observers *stationary*, hence what makes the Sagnac frequency well-defined and the whole geometry time-independent.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem applies whenever a worldline is a circular helix in some inertial frame — and that hypothesis wears several disguises.

The first disguised source is **"a point fixed on a rigidly rotating body"**. Any speck of dust on a turntable, any atom in a spinning flywheel, any component of a centrifuge is a corotating observer at its radius, and the theorem gives its acceleration and gyroscopic precession directly. The bridge is the definition of the corotating worldline as a helix; once a body rotates rigidly, every point of it is a source for this theorem. *Example problem:* find the precession rate of a gyroscope mounted at radius $r$ on a spinning space station.

The second disguised source is **"a particle in uniform circular motion in a uniform magnetic field"**. A charged particle in a cyclotron or storage ring moves on a circle at constant speed, so its worldline is a helix and the theorem's $\Gamma^2 r\omega^2$ is its proper acceleration, while $\vec\omega' = \Gamma^2\vec\omega$ governs its spin precession. The bridge is that uniform circular motion, whatever its dynamical cause, has a helical worldline. *Example problem:* compute the Thomas precession contribution to the spin precession of an electron circulating in a storage ring (the basis of $g$-$2$ experiments).

The third disguised source is **"an observer at rest on a rotating planet"**. A point on the surface of the spinning Earth is a corotating observer at radius $R_\oplus\cos\lambda$, so the theorem gives the centripetal acceleration and the (tiny) gyroscopic precession experienced there. The bridge is that "at rest on a rotating body" means "fixed cylindrical coordinates", i.e. corotating. *Example problem:* estimate the Thomas-precession rate of a gyroscope carried on the equator.

**Targets (Output Amplification)**

The conclusions are $\vec a' = (\Gamma^2/c^2)r\omega^2 e'_2$ and $\vec\omega' = \Gamma^2\vec\omega$.

Combine the four-rotation conclusion with **the central observer's four-rotation** $\vec\omega$. The *difference* $\vec\omega' - \vec\omega = (\Gamma^2 - 1)\vec\omega$ is the Thomas precession of a gyroscope carried by $\mathcal{O}'$ relative to the inertial frame, with no torque applied. The combination is useful because it isolates the purely kinematic precession from any dynamical torque, and it is nonobvious because one expects a rigidly rotating frame to carry its gyroscopes at the disk's own rate, not faster. *Example:* the Thomas factor in the spin–orbit Hamiltonian.

Combine the acceleration conclusion with **the equivalence principle**. The inward four-acceleration $\Gamma^2 r\omega^2$ is, to a corotating observer, indistinguishable from an outward (centrifugal) gravitational field of that strength. The combination yields the artificial-gravity design rule for rotating space habitats and, conceptually, feeds the equivalence-principle bridge to general relativity. It is nonobvious that the *relativistic* enhancement $\Gamma^2$ appears, though for habitat speeds it is negligible.

Combine the constancy of $\vec a'$ and $\vec\omega'$ with **the definition of a stationary observer**. Because both invariants have constant norm along the worldline, $\mathcal{O}'$ is stationary, which guarantees that signals it emits and receives have a well-defined frequency relationship — the fact that makes the [[Thm - Sagnac Delay and the Optical Sagnac Interferometer|Sagnac interferometer]] frequencies equal at emission and reception. The combination is the bridge from kinematics to the Sagnac phase.

---

# Why Is It True

The two factors of $\Gamma$ in each result come from two different applications of time dilation, and seeing where each enters demystifies the whole theorem.

**The $\Gamma^2$ in the acceleration is two factors of $dt/d\tau'$.** The four-acceleration is the second derivative of position with respect to the corotating observer's *proper time* $t'$, not with respect to the inertial time $t$. Differentiating the helix once with respect to inertial time gives a velocity, and the magnitude of the *coordinate* acceleration $d^2\vec x_*/dt^2$ is the Newtonian $r\omega^2$. But proper time runs slow, $dt = \Gamma\,dt'$, so each derivative with respect to $t'$ rather than $t$ brings a factor $dt/dt' = \Gamma$. The four-acceleration involves two proper-time derivatives in the relevant sense, hence two factors of $\Gamma$, giving $\Gamma^2 r\omega^2$. The direction is inward because the acceleration of circular motion always points toward the centre, and $e'_2$ is the inward radial unit vector of the corotating frame.

**The $\Gamma^2$ in the four-rotation is time dilation applied to the precession rate.** The corotating frame vector $e'_1$ rotates, as seen by the central observer $\mathcal{O}$, essentially at the disk rate $\omega$. But $\vec\omega'$ is the rotation rate *per unit of $\mathcal{O}'$'s proper time* $t'$, and there are in fact two contributions: the bodily rotation of the disk (rate $\omega$, dilated by one factor of $\Gamma$ on conversion to $t'$) plus the Thomas precession from the changing boost direction (which contributes the remaining $\Gamma^2 - \Gamma$). When the dust settles, the rate per proper time is $\Gamma^2\omega$. The clean way to see the result is the computation $de'_1/dt' = \Gamma^2\,\vec\omega\times_{U'}e'_1$, which exhibits the angular velocity directly as $\Gamma^2\vec\omega$.

**The one-line mechanism:** *the corotating observer measures everything against its own slow proper time, and converting the disk-frame rotation rate and coordinate acceleration to that proper time costs two factors of $\Gamma$ each, enhanced further by the Thomas precession the curving worldline forces on a non-rotating gyroscope.*

The non-obvious physical content is that even a "rigidly corotating" observer is *not* simply turning with the disk: its gyroscopes precess faster, by the Thomas effect, which is why $\vec\omega' \ne \vec\omega$. The disk turns at $\omega$; the rim observer's local sense of rotation is $\Gamma^2\omega$.

---

# What Makes This Hard

The conceptual trap is expecting $\vec\omega' = \vec\omega$ — assuming that an observer rigidly attached to the disk shares the disk's angular velocity. They do not: the corotating observer's four-rotation exceeds the disk's by $\Gamma^2$, because of the Thomas precession the curving worldline imposes on its frame. The computational pitfall is mishandling the two distinct time variables — the central proper time $t$ (equal to inertial time) and the corotating proper time $t'$, related by $dt = \Gamma\,dt'$ — and dropping a factor of $\Gamma$ when converting derivatives between them. The most common error is to compute the coordinate acceleration $r\omega^2$ and forget the two factors of $\Gamma$ that convert it to the proper four-acceleration.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the corotating four-velocity as a boost of the central one, $U' = \Lambda(U) = \Gamma(U + c^{-1}\vec V)$. Differentiate it with respect to $\mathcal{O}'$'s proper time $t'$ (using $dt = \Gamma\,dt'$ and the constancy of $\Gamma, r, \omega$) to get the four-acceleration. Then differentiate the spatial frame vector $e'_1$ with respect to $t'$ and read off the angular velocity as the coefficient of the cross product, giving the four-rotation.

**Subgoal decomposition:**

1. **Express the corotating frame in terms of the central frame.** Show $U' = \Gamma(U + (r\omega/c)\vec n)$, $e'_1 = \Gamma((r\omega/c)U + \vec n)$, and $e'_2 = -\cos\varphi\,e_1 - \sin\varphi\,e_2$ (inward radial).
   - *Hint:* Apply the boost $\Lambda$ of velocity $\vec V = r\omega\,\vec n$ to $U$ and to $\vec n$; use $\overrightarrow{O'(t')O(t)} = r\,e'_2$ to fix $e'_2$.
   - *Why needed:* Everything is computed by differentiating these frame vectors.

2. **Differentiate $U'$ to get the four-acceleration.** Compute $\vec a' = dU'/dt' = \Gamma\,dU'/dt$ and simplify using $d\vec n/dt = -\omega\,(\cos\varphi\,e_1 + \sin\varphi\,e_2)$ rotated appropriately.
   - *Hint:* Only $\vec n$ depends on $t$ (through the disk rotation); $\Gamma, r, \omega$ are constant. The result lands along $e'_2$.
   - *Why needed:* It yields $\vec a' = (\Gamma^2/c^2)r\omega^2 e'_2$.

3. **Differentiate $e'_1$ to get the four-rotation.** Compute $de'_1/dt' = \Gamma\,de'_1/dt$ and write the result as $\Gamma^2\,\vec\omega\times_{U'}e'_1$.
   - *Hint:* Use $de_i/dt = \vec\omega\times_U e_i$ for the central frame; the Levi-Civita identity converts $\vec\omega\times_U(\cdot)$ to $\vec\omega\times_{U'}(\cdot)$ up to the factor that produces $\Gamma^2$.
   - *Why needed:* Comparing with the general frame-evolution law $de'_\alpha/dt' = \vec\omega'\times_{U'}e'_\alpha + (\text{FW part})$ reads off $\vec\omega' = \Gamma^2\vec\omega$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The corotating frame in terms of the central frame
> **Statement:** $U' = \Gamma\big(U + \tfrac{r\omega}{c}\vec n\big)$, $e'_1 = \Gamma\big(\tfrac{r\omega}{c}U + \vec n\big) = \Gamma\big(\tfrac{r\omega}{c}U - \sin\varphi\,e_1 + \cos\varphi\,e_2\big)$, $e'_2 = -\cos\varphi\,e_1 - \sin\varphi\,e_2$, $e'_3 = e_3$.
>
> **Hint:** Boost $U$ and the azimuthal vector $\vec n$ by the velocity $\vec V = r\omega\,\vec n$; determine $e'_2$ from the requirement that $\overrightarrow{O'(t')O(t)} = r\,e'_2$ point from $\mathcal{O}'$ to the axis.
>
> **Why needed:** The four-acceleration and four-rotation are obtained by differentiating $U'$ and $e'_1$, so they must first be written explicitly in the central frame.
>
> > [!note]- Full proof
> > The boost $\Lambda$ taking the central four-velocity $U$ to the corotating one acts on a four-vector $X$ by $\Lambda(X) = X + [\,(\Gamma-1)(X\cdot\hat V)/\hat V\cdot\hat V + \Gamma\,(X\cdot U)\,]\dots$; more simply, for the four-velocity, $U' = \Lambda(U) = \Gamma(U + c^{-1}\vec V) = \Gamma(U + (r\omega/c)\vec n)$, the standard boosted four-velocity (see [[Def - Lorentz Factor and Relative Velocity]]). Since $e'_1 \in \mathrm{Span}(U, U')$ and is the boosted azimuthal direction, $e'_1 = \Lambda(\vec n) = \Gamma((r\omega/c)U + \vec n)$. Substituting $\vec n = -\sin\varphi\,e_1 + \cos\varphi\,e_2$ gives the stated form. The vector from $\mathcal{O}'$ to the axis point $O(t)$ simultaneous with $\mathcal{O}'$, expressed as $\overrightarrow{O'(t')O(t)} = r\,e'_2$, together with $\overrightarrow{O(t)O'(t')} = r\cos\varphi\,e_1 + r\sin\varphi\,e_2$, forces $e'_2 = -\cos\varphi\,e_1 - \sin\varphi\,e_2$ — the inward radial unit vector. Finally $e'_3 = e_3 = e^*_3$ is fixed (the axis direction, unaffected by the boost in the plane). $\blacksquare$

> [!note]- Lemma 2: The four-acceleration is inward centripetal $\Gamma^2 r\omega^2/c^2$
> **Statement:** $\vec a' = dU'/dt' = \dfrac{\Gamma^2}{c^2}r\omega^2\,e'_2$.
>
> **Hint:** Use $dt = \Gamma\,dt'$ to write $dU'/dt' = \Gamma\,dU'/dt$; only $\vec n$ varies with $t$.
>
> **Why needed:** This is the first half of the theorem.
>
> > [!note]- Full proof
> > With $\Gamma, r, \omega$ constant, $\dfrac{dU'}{dt'} = \Gamma\dfrac{dU'}{dt} = \Gamma\cdot\Gamma\dfrac{r\omega}{c}\dfrac{d\vec n}{dt}$. The azimuthal vector $\vec n = -\sin\varphi\,e_1 + \cos\varphi\,e_2$ rotates with the central frame; using $de_i/dt = \vec\omega\times_U e_i$ with $\vec\omega = \omega e_3$, one finds $d\vec n/dt = -\omega(\cos\varphi\,e_1 + \sin\varphi\,e_2) = \omega\,e'_2$ (the inward radial vector). Hence $\dfrac{dU'}{dt'} = \Gamma^2\dfrac{r\omega}{c}\cdot\omega\,e'_2 = \dfrac{\Gamma^2 r\omega^2}{c}\,e'_2$; restoring the $c$ in $\vec V/c$ gives the four-acceleration $\vec a' = (\Gamma^2/c^2)r\omega^2\,e'_2$. It points along $e'_2$, radially inward — the centripetal direction — with magnitude $\Gamma^2 r\omega^2$ in $c = 1$ units. $\blacksquare$

> [!note]- Lemma 3: The four-rotation is $\Gamma^2\vec\omega$
> **Statement:** $\vec\omega' = \Gamma^2\vec\omega$, obtained from $de'_1/dt' = \Gamma^2\,\vec\omega\times_{U'}e'_1$.
>
> **Hint:** Differentiate $e'_1$ with respect to $t'$, use the central frame law and the Levi-Civita definition of the cross product to re-express $\vec\omega\times_U$ as $\vec\omega\times_{U'}$.
>
> **Why needed:** This is the second half of the theorem.
>
> > [!note]- Full proof
> > From Lemma 1, $e'_1 = \Gamma((r\omega/c)U - \sin\varphi\,e_1 + \cos\varphi\,e_2)$. Differentiating with $dt = \Gamma\,dt'$ and constant $\Gamma, r, \omega, \varphi$ (along the worldline $\varphi$ is fixed; the $t$-dependence is in $e_1, e_2$): $\dfrac{de'_1}{dt'} = \Gamma\dfrac{de'_1}{dt} = \Gamma^2(-\sin\varphi\,\dot e_1 + \cos\varphi\,\dot e_2) = \Gamma^2(-\sin\varphi\,\vec\omega\times_U e_1 + \cos\varphi\,\vec\omega\times_U e_2) = \Gamma^2\,\vec\omega\times_U\vec n$. Now $\vec n = \Gamma^{-1}e'_1 - (r\omega/c)U$, and the Levi-Civita tensor satisfies $\epsilon(U,\vec\omega,\vec n,\cdot) = \Gamma^{-1}\epsilon(U,\vec\omega,e'_1,\cdot)$ (the $U$ term drops by antisymmetry), while $U = \Lambda^{-1}(U') = \Gamma(U' - (r\omega/c)e'_1)$ converts $\epsilon(U,\vec\omega,e'_1,\cdot) = \Gamma\,\epsilon(U',\vec\omega,e'_1,\cdot)$. Combining, $\vec\omega\times_U\vec n = \vec\omega\times_{U'}e'_1$, so $\dfrac{de'_1}{dt'} = \Gamma^2\,\vec\omega\times_{U'}e'_1$. Comparing with the general law $de'_1/dt' = \vec\omega'\times_{U'}e'_1$ (the Fermi–Walker part is orthogonal, contributing along $U'$, and vanishes here for the spatial component) gives $\vec\omega' = \Gamma^2\vec\omega$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, the corotating four-velocity and frame are $U' = \Gamma(U + (r\omega/c)\vec n)$, $e'_1 = \Gamma((r\omega/c)U + \vec n)$, $e'_2 = -\cos\varphi\,e_1 - \sin\varphi\,e_2$ (inward radial), $e'_3 = e_3$, where $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$ and $\vec n = -\sin\varphi\,e_1 + \cos\varphi\,e_2$.
>
> *Four-acceleration.* By Lemma 2, differentiating $U'$ with respect to $\mathcal{O}'$'s proper time (using $dt = \Gamma\,dt'$, and $d\vec n/dt = \omega\,e'_2$ from the central frame law $de_i/dt = \vec\omega\times_U e_i$),
> $$\vec a' = \frac{dU'}{dt'} = \frac{\Gamma^2}{c^2}\,r\omega^2\,e'_2,$$
> directed radially inward, of magnitude $\Gamma^2 r\omega^2$ — the relativistic centripetal acceleration.
>
> *Four-rotation.* By Lemma 3, differentiating $e'_1$ with respect to $t'$ and converting the cross product from the rest space of $U$ to that of $U'$ via the Levi-Civita identities and the inverse boost,
> $$\frac{de'_1}{dt'} = \Gamma^2\,\vec\omega\times_{U'}e'_1,$$
> and comparison with the general frame-evolution law identifies the four-rotation as
> $$\vec\omega' = \Gamma^2\vec\omega.$$
> One checks consistency with $de'_2/dt' = (\Gamma^2/c)r\omega^2\,U' + \vec\omega'\times_{U'}e'_2$ (the Fermi–Walker part with $\vec a'\cdot e'_2 = \Gamma^2 r\omega^2/c^2$ plus the spatial rotation), in full agreement with the general law. Since $\Gamma, r, \omega$ are constant along the worldline, both $\vec a'$ and $\vec\omega'$ are constant, so $\mathcal{O}'$ is a stationary observer. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Storage-ring spin precession ($g$-$2$ experiments).** An electron or muon circulating in a storage ring at relativistic speed has a spin that precesses by the Thomas rate $(\Gamma^2 - 1)\vec\omega$ relative to the inertial lab frame, on top of the magnetic precession. Disentangling the kinematic Thomas precession from the dynamical (magnetic-moment) precession is exactly the analysis behind the celebrated measurements of the anomalous magnetic moment $g$-$2$. The application is nonobvious because the kinematic precession of this theorem must be subtracted to isolate the quantum-field-theoretic anomaly.

**Artificial gravity in rotating space habitats.** A rotating cylindrical habitat (an O'Neill cylinder) provides artificial gravity equal to the centripetal acceleration $\Gamma^2 r\omega^2$ at its rim. For habitat speeds $\Gamma\approx 1$, but the design rule "spin rate and radius set the felt gravity" is this theorem, and the equivalence-principle reading (the inward four-acceleration feels like an outward gravitational field) is the bridge to general relativity.

**Pulsar surface dynamics.** Matter at the equator of a millisecond pulsar moves at a substantial fraction of $c$, so the relativistic enhancement $\Gamma^2$ of the centripetal acceleration is significant in modelling the forces on, and the precession of, surface features and accreted matter. The application is out-of-distribution because it places the rotating-disk kinematics in an astrophysical, strong-field-adjacent setting.

---

# Bridges

- **[[Special Relativity XVI — Accelerated Observers|Thomas precession (Chapter XVI)]]** — the excess $\vec\omega' - \vec\omega = (\Gamma^2 - 1)\vec\omega$ of the corotating four-rotation over the disk's is precisely the Thomas precession of a gyroscope in circular orbit, derived there from the non-commutativity of boosts. This theorem rederives the same precession from the rotating-disk congruence: a torque-free gyroscope carried around the circle precesses relative to the inertial frame at the Thomas rate, because the boost holding it on the circle continuously changes direction. The two derivations agree, and the link is that circular motion is a continuous succession of infinitesimal non-collinear boosts whose net effect is a rotation.

- **[[Def - Local Frame and Four-Rotation|The four-rotation ω⃗]]** — this theorem computes the four-rotation of a *specific* observer (the corotating one) and finds it differs from the four-rotation of the central observer on the same disk. It illustrates that four-rotation is observer-dependent even within a single rigid congruence, and that the Fermi–Walker and spatial-rotation decomposition of the frame evolution carries the full information.

- **The relativistic centripetal acceleration** — the result $\|\vec a'\| = \Gamma^2 r\omega^2$ is the rotational counterpart of the longitudinal/transverse mass distinction: the four-acceleration needed to maintain circular motion grows as $\Gamma^2$, just as the transverse force on a relativistic particle exceeds the Newtonian expectation. The bridge is that circular motion is transverse acceleration, and transverse acceleration carries the factor $\Gamma^2$ in the relation between three-acceleration and four-acceleration.

---

# Unlocked by This

> [!tip] The Thomas Factor in Atomic Spectra *(from Quantum Mechanics)*
> The kinematic precession $(\Gamma^2 - 1)\vec\omega$ of a corotating gyroscope is, for an electron orbiting a nucleus, the origin of the **Thomas factor** of $\tfrac12$ in the spin–orbit coupling. A naive calculation of the spin–orbit interaction overestimates it by a factor of two; the missing factor is the Thomas precession of the electron's rest frame as it orbits, exactly the effect this theorem quantifies for the rotating disk. The correct fine structure of hydrogen — and hence the agreement of the Dirac equation with experiment — depends on getting this kinematic precession right.

> [!tip] Spin Precession and the BMT Equation *(from Relativistic Spin Dynamics)*
> The four-rotation $\vec\omega' = \Gamma^2\vec\omega$ of a corotating observer is the kinematic piece of the general **Bargmann–Michel–Telegdi (BMT) equation** governing the precession of a particle's spin in electromagnetic fields. When a charged particle moves on a circle in a magnetic field, its spin precesses at a rate combining the Thomas (kinematic) part computed here with the magnetic-moment (dynamical) part, and the BMT equation packages both covariantly — the foundation of all precision spin-precession experiments.

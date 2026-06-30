---
type: definition
subject: special-relativity
prereqs:
  - "Def - Synge World Function and Spatial Distance"
  - "Def - Observer and Local Rest Space"
  - "Def - Worldline of a Particle"
  - "Thm - Euclidean Character of the Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so spatial length is $\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}}$. An **infinitesimal ruler** is a pair of neighbouring timelike worldlines $(\mathcal{L}_0, \mathcal{L}_1)$, the two ends of the ruler; $\mathcal{O}$ is the observer on $\mathcal{L}_0$ with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$, reading [[Def - Proper Time|proper time]] $t$. $A\in\mathcal{L}_0$ and $B\in\mathcal{L}_1$ are simultaneous events ($\overrightarrow{AB}\in U_0^\perp$); the photon round trip $\mathcal{L}_0\to\mathcal{L}_1\to\mathcal{L}_0$ has emission $t_1$ and reception $t_2$. Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

---

# Axiom Motivation

A ruler in Newtonian physics is a rigid body: a collection of points whose mutual distances never change, which can be picked up, carried, accelerated, and rotated while keeping its shape. We have just learned to *measure* distance chronometrically with [[Def - Synge World Function and Spatial Distance|Synge's formula]]; the question now is whether a moving ruler keeps a *constant* length — what it means for an extended object to be rigid in relativity, and whether such objects exist. The answer is subtle and ultimately negative for extended bodies, and confronting it is the point of this page.

Start with the cleanest case: a ruler so short it is essentially a *pair* of worldlines, $\mathcal{L}_0$ and $\mathcal{L}_1$, tracing the two ends. The observer $\mathcal{O}$ on $\mathcal{L}_0$ measures the length to the other end by the radar method: bounce a photon off $\mathcal{L}_1$ and apply Synge. For a length to be well-defined, the displacement $\overrightarrow{AB}$ between the ends must be *spatial* for $\mathcal{O}$ — orthogonal to $U_0$, lying in the [[Def - Observer and Local Rest Space|rest space]], where the [[Thm - Euclidean Character of the Local Rest Space|metric is Euclidean]]. Then the length is the radar distance, and for a *simultaneous* measurement (the natural one) it is $\|\overrightarrow{AB}\| = \tfrac12 c(t_2 - t_1)$, half the round-trip time.

What should "rigid" mean? The Newtonian instinct — "the distance between the ends never changes" — needs care, because "distance" and "never" are both observer-laden in relativity. The clean, operational definition is: the ruler is **rigid** if the radar length $\|\overrightarrow{AB}\|$ is the same at every proper time, for $\overrightarrow{AB}$ taken orthogonal to $U_0$. Equivalently — and this is the beauty of the chronometric viewpoint — the ruler is rigid iff the *photon round-trip time between its ends is constant*. No ruler is needed to check rigidity of a ruler; you bounce light between the ends and watch whether the round-trip time drifts. This is **Born's rigidity criterion**, and it makes rigidity a measurable, frame-independent property of the pair of worldlines.

Why insist on $\overrightarrow{AB}$ orthogonal to $U_0$? Because length is only meaningful in the rest space, where it is Euclidean; a non-orthogonal "separation" would mix in a time component and not be a spatial length at all. The orthogonality is the condition that makes "the length of the ruler" well-posed, and Synge's reduction to $\tfrac12 c(t_2 - t_1)$ uses exactly $t - t_1 = t_2 - t$, which is the simultaneity of $A$ and $B$.

Now the sobering part — why this is a *definition* of one-dimensional rigidity and not of a rigid solid. The construction governs a *pair* of worldlines: it is one-dimensional, controlling only the distance between two points. The natural three-dimensional generalisation would demand that *every* pair of neighbouring points of an extended body form a rigid ruler. But this is wildly overdetermined: it imposes six conditions (the time-derivatives of the six independent components of the spatial metric) on the three-component velocity field of the body, and the Noether–Herglotz theorem shows the only motions satisfying all of them form a mere six-parameter family — essentially the isometric and uniformly rotating motions — far too few to describe a real solid being accelerated or deformed. A rotating disk cannot even be spun up rigidly (the Ehrenfest paradox). So *there is no satisfactory notion of a rigid solid in relativity*: rigidity survives only as the infinitesimal, one-dimensional criterion for a pair of worldlines, or as the restricted Born-rigid congruences. The reason it matters to state this carefully is that "rigid rod" is a constant temptation in relativity problems, and it is almost always illegitimate for an extended body.

---

# The Definition

Let $(\mathcal{L}_0, \mathcal{L}_1)$ be a pair of neighbouring timelike [[Def - Worldline of a Particle|worldlines]] — the two ends of an **infinitesimal ruler** — and let $\mathcal{O}$ be the observer on $\mathcal{L}_0$ with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$. For an event $A\in\mathcal{L}_0$, let $B\in\mathcal{L}_1$ be the event *simultaneous* with $A$ for $\mathcal{O}$, i.e. $\overrightarrow{AB}\in U_0^\perp$ (the [[Def - Observer and Local Rest Space|local rest space]]). The **length of the infinitesimal ruler** at proper time $t$ is the radar distance
$$
\|\overrightarrow{AB}\| \;=\; \tfrac12\,c\,(t_2 - t_1),
$$
where $t_1, t_2$ are the emission and reception proper times of a photon making the round trip $\mathcal{L}_0\to\mathcal{L}_1\to\mathcal{L}_0$ ([[Def - Synge World Function and Spatial Distance|Synge's formula]] with $t - t_1 = t_2 - t$).

**Born's rigidity criterion.** The ruler is **(Born-)rigid** if its length $\|\overrightarrow{AB}\|$ does not vary along the worldlines — equivalently, if the photon round-trip time between its ends is constant:
$$
\boxed{\,\tfrac12\,c\,(t_2 - t_1) \;=\; \mathrm{const} \quad\text{in proper time}\,}.
$$
This is a chronometric, ruler-free criterion: one tests the rigidity of a ruler by bouncing light between its ends and checking that the round-trip time is steady.

**No rigid solid.** The three-dimensional generalisation — every pair of neighbouring points of an extended body forms a Born-rigid ruler — is overdetermined: by the **Noether–Herglotz theorem** the Born-rigid motions of an extended body form only a six-parameter family (the isometric and uniformly rotating motions). Hence there is no Lorentz-invariant notion of a rigid solid; "rigidity" is meaningful only for an infinitesimal ruler (a pair of worldlines) or for the restricted Born-rigid congruences.

---

# Categorical / Structural Definition

Phrased through the kinematics of a worldline congruence, Born rigidity is the vanishing of the **expansion** and **shear** of the congruence as measured in the rest spaces. Projecting the gradient of the four-velocity field onto the rest space with the [[Def - The Orthogonal Projector onto the Local Rest Space|projector]] $\Pi$ and symmetrising gives the spatial deformation rate $\theta_{ij}$ (the analogue of the Newtonian rate-of-strain tensor); the congruence is Born-rigid iff $\theta_{ij} = 0$, i.e. the rest-space distances between neighbouring worldlines are frozen. The trace of $\theta_{ij}$ is the expansion (volume change) and its trace-free part the shear (shape change); Born rigidity is "no expansion, no shear", leaving only rotation $\vec\omega$ as a permitted relative motion. This is exactly the relativistic version of a rigid body's velocity field $\mathbf v = \mathbf v_0 + \boldsymbol\omega\times\mathbf r$, where the only allowed neighbour-relative motion is rotation; the Noether–Herglotz theorem is the statement that, unlike the Newtonian case, the relativistic constraints are so tight that the rotation cannot be time-varying and the family of solutions is only six-parameter.

---

# Relate to Other Fields / Compression

Born rigidity is the relativistic descendant of the **rigid body** of classical mechanics, and its near-total collapse is one of the sharpest illustrations of how relativity forbids instantaneous action: a truly rigid rod would transmit a push from one end to the other faster than light, so rigidity and causality are in tension, and causality wins. In continuum mechanics, the rate-of-strain tensor $\theta_{ij}$ whose vanishing defines Born rigidity is the relativistic analogue of the **strain-rate tensor** of elasticity and fluid mechanics, and the expansion/shear/rotation decomposition is the same one used for the **expansion, shear, and vorticity** of a fluid congruence in [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]] (Raychaudhuri's equation governs the expansion).

**True name:** Born rigidity is *constant radar distance between neighbouring worldlines* — operationally, *constant photon round-trip time between the ends*. The deep companion fact is that this is only consistently imposable in one dimension (a pair of worldlines) or for a six-parameter family of three-dimensional motions; there is no rigid solid.

---

# Examples / Corollaries

**Is an instance — a uniformly accelerated (Rindler) congruence.** A family of observers with appropriately graded constant proper accelerations (greater at the trailing end) maintains constant proper distances and constant photon round-trip times between neighbours: it is Born-rigid. This is the relativistic "rigid rod accelerated along its length", and the grading of accelerations is forced precisely by the rigidity constraint. (See [[Special Relativity XVI — Accelerated Observers]].)

**Is an instance — uniform translation.** A body in uniform inertial motion trivially satisfies Born rigidity: all worldlines are parallel straight lines, the rest-space distances are constant, and the round-trip times never change. Inertial motion is the simplest Born-rigid motion.

**Is NOT an instance — a disk being spun up from rest.** Setting a disk into rotation cannot be done Born-rigidly: the circumference would need to contract (length contraction) while the radius does not, an impossibility for a rigid disk — the **Ehrenfest paradox**. A disk in *steady* uniform rotation is Born-rigid (it is one of the Noether–Herglotz motions), but the *process* of spinning it up is not. This is the calibration that Born rigidity constrains the whole history, not just an instant.

**Is NOT an instance — a generic accelerating solid.** An ordinary solid given an arbitrary acceleration profile does *not* move Born-rigidly: its parts must expand, shear, or both, because the Noether–Herglotz family is far too small to contain arbitrary motions. Real solids deform; only the six-parameter family stays rigid. This is the concrete content of "no rigid solid".

**Corollary — rigidity permits rotation but not expansion or shear.** A Born-rigid congruence has vanishing expansion and shear ($\theta_{ij} = 0$) but may have nonzero rotation $\vec\omega$. So the allowed relative motions of a rigid body's parts are exactly rotations — the relativistic echo of $\mathbf v = \boldsymbol\omega\times\mathbf r$ — with the Noether–Herglotz restriction that the rotation rate is tightly constrained.

**Calibration check.** You should be able to: (1) state Born's criterion both as "constant radar distance" and as "constant round-trip time", and say why they are equivalent; (2) explain why $\overrightarrow{AB}$ must be orthogonal to $U_0$ for the length to be meaningful; and (3) explain in one sentence why there is no rigid solid in relativity (the three-dimensional constraints are overdetermined — Noether–Herglotz — leaving only a six-parameter family).

---

# Unlocked by This

> [!tip] The Rindler Congruence and the Accelerated Frame *(from Accelerated Observers)*
> The Born-rigid uniformly accelerated congruence — with graded proper accelerations — is the **Rindler frame** of [[Special Relativity XVI — Accelerated Observers]], whose rest spaces sweep the Rindler wedge and whose trailing edge has a horizon; the constant-round-trip-time rigidity is what makes it a coherent extended accelerated reference frame.

> [!tip] The Ehrenfest Paradox and Rotating Disks *(from Rotating Observers)*
> The impossibility of Born-rigidly spinning up a disk is the **Ehrenfest paradox** of [[Special Relativity XVII — Rotating Observers]]; the failure of the rotating congruence's rest spaces to close up globally (no consistent clock synchronisation) is the same non-integrability that produces the Sagnac effect.

> [!tip] Expansion, Shear, and Vorticity of a Congruence *(from General Relativity)*
> The deformation tensor $\theta_{ij}$ whose vanishing defines Born rigidity decomposes into **expansion, shear, and vorticity**, the kinematic invariants of a worldline congruence that drive the **Raychaudhuri equation** in [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]] — the equation behind the focusing theorems and the singularity theorems.

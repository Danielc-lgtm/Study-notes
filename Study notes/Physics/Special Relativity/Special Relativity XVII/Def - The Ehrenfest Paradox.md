---
type: definition
subject: special-relativity
prereqs:
  - "Def - Uniformly Rotating Observer"
  - "Def - Born Rigidity Criterion"
  - "Thm - Length Contraction (General)"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The disk rotates at angular velocity $\omega$ about its axis; a corotating observer at radius $r$ has rim speed $r\omega$ and [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$. The inertial observer $\mathcal{O}_*$ measures the disk's circumference as $L$ and radius as $R$; corotating observers measure them as $L'$ and $R'$. The proper separation vector between neighbouring corotating observers is $d\vec\ell$, with proper length $d\ell'$. Subscript $0$ denotes the disk at rest before spin-up: $L_0 = 2\pi R_0$. Full registry on [[Special Relativity XVII — Rotating Observers]].

> [!warning] Convention: Gourgoulhon's opposite signature
> Gourgoulhon (Chapter 13) uses $\mathrm{diag}(-1,+1,+1,+1)$. The Lorentz factor $\Gamma$ and all proper lengths are positive scalars, unaffected by the signature choice; only relative signs of scalar products of distinct four-vectors flip.

This is a compound page: it defines two interlocking notions — the **non-Euclidean rest geometry of the rotating disk** (the relation $L' = \Gamma\,2\pi R'$ between measured circumference and radius) and the **Ehrenfest paradox** itself (the apparent contradiction with rigid spin-up, and its resolution) — because the paradox is precisely the clash between the non-Euclidean relation and the false assumption of Born rigidity, and neither is intelligible without the other.

---

# Axiom Motivation

We have a flat, ordinary disk lying at rest, and we set it spinning. The question is the most innocent imaginable: what is the ratio of its circumference to its radius, as measured by observers riding on the disk? In Euclidean geometry the answer is $2\pi$, always. The motivation for this page is that in special relativity the answer is *not* $2\pi$, and that this single fact — acceleration producing non-Euclidean geometry — is the conceptual hinge on which the door from special to general relativity swings.

Start with what the inertial observer $\mathcal{O}_*$ measures. For $\mathcal{O}_*$, the disk is a disk: its circumference and radius satisfy $L = 2\pi R$, with $R = R_0$ the rest radius (the disk's overall size, viewed from outside, is whatever it is). Nothing strange here. The strangeness is entirely in what the *corotating* observers measure, and it comes from the direction-dependence of length contraction.

Consider the circumference first. The velocity of a rim observer is tangent to the rim — along the direction of the circumference. A small arc of the rim is therefore a rod oriented *along the motion*, and by [[Thm - Length Contraction (General)|length contraction]] the inertial observer sees each such rod contracted relative to its proper (corotating-frame) length. Turn this around: the proper length of an arc, measured by corotating rulers, is *longer* than the inertial-frame length by the factor $\Gamma$. Summing around the rim, the corotating circumference is $L' = \Gamma L = \Gamma\,2\pi R$. The key per-direction observation is that contraction acts *only along the motion*, so the circumference — entirely tangential — is fully affected.

Now the radius. The velocity is tangential, hence *perpendicular* to the radial direction. A radial rod is oriented across the motion, and there is no length contraction perpendicular to the velocity. So the radius measured by corotating observers equals the inertial-frame radius: $R' = R = R_0$. The radial direction is the one direction the motion does not touch, and this asymmetry — circumference contracted, radius not — is the whole source of the effect.

Combining, the corotating observers find $L' = \Gamma\,2\pi R'$ with $\Gamma > 1$, so $L' > 2\pi R'$: the ratio of circumference to radius exceeds $2\pi$. This is a **non-Euclidean** relation. A flat disk, measured from within its own rotating rest frame, has the circumference-to-radius ratio of a surface of negative curvature (like a saddle, where circles are "too big" for their radius). The geometry the corotating observers measure is genuinely curved, even though the spacetime is perfectly flat.

So far there is no paradox — only a surprising but consistent non-Euclidean measurement. The paradox enters when one asks what happens during *spin-up*. Suppose the disk is rigid in the strongest sense — **Born-rigid**, meaning every proper distance between its parts stays fixed as it is set spinning. Then its circumference, an internal proper distance, cannot change: $L' = L_0 = 2\pi R_0$. But we just derived $L' = \Gamma\,2\pi R' = \Gamma\,2\pi R_0 > 2\pi R_0$. The two statements contradict each other. This is **Ehrenfest's paradox** (1909), and the motivation for stating it carefully is that the contradiction is real *given the rigidity assumption*, so the assumption must be the culprit.

The resolution is that **Born rigidity fails for spin-up**. The Herglotz–Noether theorem classifies the rigid motions in special relativity, and a disk going from rest to rotation is not among them: no material body can be spun up while keeping all proper distances fixed. Physically, the rim must *stretch* tangentially — acquiring elastic stress, and possibly tearing if spun too fast — while the radius stays put. The circumference genuinely grows from $2\pi R_0$ to $\Gamma\,2\pi R_0$ during spin-up, so there is no contradiction: $L' = \Gamma\,2\pi R_0 \ne L_0$, and the "$L' = L_0$" premise was the false assumption smuggled in by imagining the disk perfectly rigid. The lesson, which the per-axis analysis makes precise, is that the tangential and radial directions transform differently, and no rigid motion can reconcile a $\Gamma$-stretched circumference with an unchanged radius.

---

# The Definition

For a disk rotating at angular velocity $\omega$, the **circumference and radius measured by corotating observers** are
$$
L' = \Gamma\,2\pi R = \frac{2\pi R}{\sqrt{1 - (R\omega/c)^2}},\qquad R' = R,
$$
where $\Gamma = (1 - R^2\omega^2/c^2)^{-1/2}$ is the rim Lorentz factor and $R = R_0$ is the inertial-frame radius. The tangential proper-length element is $d\ell' = \Gamma\, r\,d\varphi$ (length-contracted measurement along the motion), while the radial proper-length element is $d\ell' = dr$ (no contraction perpendicular to the motion); integrating gives $L' = \int_0^{2\pi}\Gamma R\,d\varphi = \Gamma\,2\pi R$ and $R' = \int_0^R dr = R$. Consequently
$$
\boxed{\,L' = \Gamma\,2\pi R' = \frac{2\pi R'}{\sqrt{1 - (R'\omega/c)^2}} > 2\pi R'\,}\qquad(\omega\ne 0),
$$
a **non-Euclidean** relation: the circumference-to-radius ratio measured on the disk exceeds $2\pi$.

The **Ehrenfest paradox** is the apparent contradiction obtained by assuming the disk remains **Born-rigid** during spin-up. Born rigidity (constant proper distances between all parts) would force the circumference to keep its rest value $L' = L_0 = 2\pi R_0$, contradicting $L' = \Gamma\,2\pi R_0 > 2\pi R_0$.

**Resolution.** The contradiction is removed by abandoning the rigidity assumption. By the Herglotz–Noether theorem, no material body can be spun up from rest while remaining Born-rigid; the disk's rim necessarily stretches tangentially (acquiring elastic stress) as it is set into rotation, so $L'$ genuinely increases to $\Gamma\,2\pi R_0$ and there is no contradiction. The radius, perpendicular to the motion, is unchanged ($R' = R = R_0$), and the resulting non-Euclidean ratio $L'/R' = \Gamma\,2\pi$ is the true rest geometry of the rotating disk.

---

# Categorical / Structural Definition

Structurally, the non-Euclidean disk geometry is the **spatial metric induced on the quotient of the corotating congruence by its flow** — the geometry of $\mathcal{O}$'s reference space $R_{\mathcal{O}}$ with the proper distances corotating observers actually measure. Because the corotating congruence has nonzero vorticity $\vec\omega$, it admits no global orthogonal hypersurface (no family of corotating observers shares a simultaneity surface), so "the rest space of the disk" is not a slice of spacetime but the quotient manifold, and the metric on it is the projected spatial metric. That projected metric has the line element (in corotating coordinates) $d\ell'^2 = dr^2 + \dfrac{r^2\,d\varphi^2}{1 - r^2\omega^2/c^2}$, whose Gaussian curvature is *negative* — the disk's rest geometry is a surface of negative curvature, which is the invariant statement of "$C/R > 2\pi$".

This is the precise sense in which the Ehrenfest disk is the bridge to general relativity: it is an example, entirely within flat Minkowski spacetime, of a non-flat spatial metric arising from the motion of the observers. The spacetime is flat (zero Riemann tensor), but the rest space of an accelerated congruence is curved (nonzero spatial Gaussian curvature). General relativity removes the qualifier "spatial": there the *spacetime* metric is curved, and the curvature is sourced by energy rather than by the choice of observer, but the structural lesson — that the geometry one measures depends on the metric, and the metric can be non-flat — is rehearsed in full here.

---

# Relate to Other Fields / Compression

The non-Euclidean rest geometry of the rotating disk is the **hyperbolic-geometry** analogue for rotation: the spatial metric has constant-sign negative curvature near the centre, and circles have circumference exceeding $2\pi$ times their radius, the defining feature of a surface of negative Gaussian curvature (as in the Poincaré disk model of the hyperbolic plane, where circles are likewise "too large"). The corotating observers, confined to their own rest frame, would do non-Euclidean geometry without ever suspecting that the underlying spacetime is flat.

In materials science, the impossibility of Born-rigid spin-up is the relativistic root of a real effect: setting any extended body into rotation induces **elastic stress** (tangential tension from the stretching circumference), which limits the maximum rotation rate before a flywheel or centrifuge bursts. The relativistic statement that the circumference *must* grow by $\Gamma$ is the extreme-speed limit of the everyday fact that a spun-up disk is under hoop stress.

**True name:** the Ehrenfest disk is *a flat object with a curved rest geometry* — the operational point is that corotating rulers measure $C/R = \Gamma\,2\pi \ne 2\pi$, and the "paradox" dissolves the instant one accepts that no disk can be spun up rigidly, so the circumference genuinely stretches while the radius does not.

---

# Examples / Corollaries

**Is an instance — a relativistic flywheel.** A flywheel spun close to the speed at which its rim approaches $c$ would, in principle, have its rim circumference measured by corotating observers as $\Gamma\,2\pi R$, far exceeding $2\pi R$. Long before this regime, real flywheels burst from hoop stress — the everyday shadow of the relativistic stretching requirement.

**Is an instance — the rotating Earth's spatial geometry.** Strictly, the geometry measured by corotating observers on the spinning Earth is non-Euclidean, with $C/R$ exceeding $2\pi$ by a factor $\Gamma$. The effect is utterly negligible ($r\omega/c \sim 10^{-6}$), but it is real and of the same nature as the dramatic case.

**Is NOT an instance — the disk as measured by the inertial observer.** For the inertial $\mathcal{O}_*$, the disk satisfies $L = 2\pi R$, perfectly Euclidean. The non-Euclidean relation holds *only* for corotating observers; an external inertial observer sees an ordinary disk (with a Lorentz-contracted rim, consistently). Attributing the non-Euclidean ratio to the inertial frame is an error.

**Is NOT an instance — a disk in uniform translation.** A disk moving inertially in a straight line is length-contracted along the motion, but this does *not* produce a non-Euclidean rest geometry: in the disk's own (inertial) rest frame it is a perfectly ordinary Euclidean disk. The non-Euclidean geometry requires *rotation* — the vorticity that prevents a common rest space — not mere motion. This non-example isolates rotation as the essential ingredient.

**Corollary — the paradox is resolved by the failure of rigidity, not by any error in the contraction.** Both halves of the contradiction are correct: corotating observers really do measure $L' = \Gamma\,2\pi R$, and a Born-rigid disk really would keep $L' = 2\pi R_0$. What is false is that the disk can be *both* spun up *and* Born-rigid. The resolution is a statement about which motions are physically realizable, not about the kinematics of measurement.

**Corollary — the radius is the one undistorted length.** Because the motion is purely tangential, the radial direction is the unique direction with no length contraction, so $R' = R = R_0$ exactly, for any $\omega$. Every distortion of the disk's geometry is concentrated in the tangential (circumferential) direction.

**Calibration check.** Verify that (i) on the axis $r = 0$, $\Gamma = 1$ and $L'/R' \to 2\pi$, so the geometry is Euclidean at the centre and the non-Euclideanness grows outward; (ii) the radial measurement $R' = R$ uses $\theta = \pi/2$ (velocity perpendicular to $d\vec\ell$) in the proper-length formula, while the circumferential measurement $L' = \Gamma\,2\pi R$ uses $\theta = 0$ (velocity parallel to $d\vec\ell$); (iii) the limit $\omega\to 0$ recovers $L_0 = 2\pi R_0$, the Euclidean rest disk, confirming the effect is purely rotational.

---

# Unlocked by This

> [!tip] The Equivalence Principle and the Curvature of Space *(from General Relativity)*
> This page is, historically, the single most important stepping stone from special to general relativity. Einstein's reasoning ran: by the **equivalence principle**, the centrifugal field on a rotating disk is locally indistinguishable from a gravitational field; and on the disk, corotating rulers measure a non-Euclidean geometry, $C/R > 2\pi$. Therefore a gravitational field must make the geometry of space non-Euclidean, and the flat constant metric $\eta_{\mu\nu}$ cannot describe gravity — one needs a position-dependent metric $g_{\mu\nu}(x)$ on a curved manifold. The rotating disk is the only fully special-relativistic example in which acceleration *provably* produces curved spatial geometry, which is why it convinced Einstein that **general relativity must be a theory of curved spacetime**. The chapter [[Special Relativity XXV — Toward Relativistic Gravitation|Toward Relativistic Gravitation]] develops the bridge; the curved metric itself is the subject of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]].

> [!tip] The Herglotz–Noether Theorem and Relativistic Rigidity *(from Continuum Mechanics)*
> The resolution of the paradox rests on a deep structural result: the **Herglotz–Noether theorem**, which classifies all Born-rigid motions in special relativity and shows that the rotational ones form only a three-parameter family (isometric rotations of an already-rotating body), with *no* rigid motion connecting rest to rotation. This is the relativistic replacement for the Newtonian rigid body, and it reveals that "rigid body" is a far more restrictive concept in relativity than in classical mechanics — the infinite speed of sound implicit in a Newtonian rigid body is forbidden, so rigidity must be redefined as **constancy of proper distances**, and that redefinition makes spin-up non-rigid.

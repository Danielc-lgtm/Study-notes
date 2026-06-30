---
type: definition
subject: special-relativity
prereqs:
  - "Def - Observer and Local Rest Space"
  - "Def - Local Frame and Four-Rotation"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Lorentz Factor and Relative Velocity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a timelike four-vector $X$ has $X\cdot X > 0$. The central observer is $\mathcal{O}$, with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$, proper time $t$, and four-acceleration $\vec a = dU/d\tau$; its [[Def - Local Frame and Four-Rotation|four-rotation]] is $\vec\omega$, a spacelike vector with $U\cdot\vec\omega = 0$ and magnitude $\omega = \|\vec\omega\|$. The inertial observer $\mathcal{O}_*$ shares $\mathcal{O}$'s worldline and carries the non-rotating inertial frame $(e^*_\alpha)$ and inertial coordinates $(t, x_*, y_*, z_*)$. A corotating observer is $\mathcal{O}'$, with four-velocity $U'$ and proper time $t'$. The cross product in the rest space of $U$ is written $\vec a\times_U\vec b = \epsilon(U,\vec a,\vec b,\cdot)$ (index raised), $\epsilon$ the spacetime Levi-Civita tensor. Full registry on [[Special Relativity XVII — Rotating Observers]].

> [!warning] Convention: Gourgoulhon's opposite signature
> Gourgoulhon (Chapter 13) uses $\mathrm{diag}(-1,+1,+1,+1)$ with $\vec u\cdot\vec u = -1$. The magnitudes $\omega = \|\vec\omega\|$ and $V = \|\vec V\|$ are positive in either signature and carried over unchanged; scalar products of two distinct four-vectors flip overall sign.

This is a compound page: it defines two interlocking notions — the **uniformly rotating observer** $\mathcal{O}$ (the axis observer with constant four-rotation) and the **corotating observer** $\mathcal{O}'$ (a point fixed on the spinning disk) — because the disk is the congruence built from a uniformly rotating central observer, and neither is fully usable without the other.

---

# Axiom Motivation

We want the cleanest, most symmetric example of an observer whose [[Def - Local Frame and Four-Rotation|four-rotation]] is nonzero, just as the previous chapter built the cleanest example of nonzero four-acceleration (the uniformly accelerated, hyperbolic-motion observer). The four-rotation $\vec\omega$ measures how fast an observer's spatial frame spins relative to a gyroscope-defined non-rotating frame. To make the example tractable and physically meaningful, two design decisions present themselves, and examining why each is the right one is the whole motivation.

The first decision is to **demand vanishing four-acceleration** of the central observer: $\vec a = 0$. Why insist the central observer be inertial? Because we want to isolate rotation from acceleration. An observer can in general both accelerate and rotate, and the evolution of their frame mixes the two (a Fermi–Walker part from $\vec a$ and a spatial-rotation part from $\vec\omega$). If we let the central observer accelerate, the frame evolution would carry both contributions and the rotation would be entangled with the acceleration of the worldline. Setting $\vec a = 0$ makes the central worldline a straight inertial line — the observer goes nowhere, like a figure skater spinning in place at the centre — and the frame evolution then reduces to *pure* spatial rotation, $de_i/dt = \vec\omega\times_U e_i$. This is the canonical model of "rotation with no translation". Drop this axiom and you no longer have a *rotating disk* but some general accelerated-and-rotating motion; the disk's defining feature is a fixed centre.

The second decision is to **demand the four-rotation be constant**: $\vec\omega = \text{const}$. Why constant rather than time-varying? Because we want a *stationary* situation — a disk turning at a steady rate, whose geometry does not change in time. If $\vec\omega$ varied, the angular velocity of the disk would change, the rim speed and Lorentz factor would be functions of time, and none of the clean stationary results (constant proper-time ratios, time-independent circumference, a well-defined Sagnac delay) would hold. Constancy of $\vec\omega$ is exactly the statement "uniform rotation", the rotational analogue of "uniform acceleration". With both axioms, the central observer is inertial and spins steadily, and an inertial observer $\mathcal{O}_*$ sharing its worldline can be chosen with its third axis along $\vec\omega$, so $\vec\omega = \omega e^*_3$.

Now the corotating observers. Having a spinning central frame, we populate the disk with observers *fixed* in that frame — at constant cylindrical coordinates $(r,\varphi)$ relative to $\mathcal{O}$. Why fixed coordinates? Because that is what "a point of the rigid disk" means: a speck of dust glued to the turntable keeps its distance $r$ from the axis and its angular position $\varphi$ in the rotating frame. Relative to the *inertial* frame $\mathcal{O}_*$, such a point moves in a circle, tracing the helix $x_*(t) = r\cos(\omega t + \varphi)$, $y_*(t) = r\sin(\omega t + \varphi)$. The crucial constraint emerges immediately: the rim speed is $r\omega$, and an observer's worldline must be timelike, so $r\omega < c$, i.e. $r < c/\omega$. Beyond this radius — the **light cylinder** — a corotating "observer" would have to move faster than light, which is impossible; at exactly $r = c/\omega$ the worldline is null. This is not an artifact of the construction but a genuine physical limit: you cannot rigidly rotate a disk of arbitrary size at fixed $\omega$, because the rim would exceed $c$. The radius bound is forced by the timelike-worldline requirement, and it is the first place the relativity of rotation bites.

One subtlety deserves stress. The cylindrical coordinates $(r,\varphi)$ are *labels*, not direct physical measures. As the chapter shows ([[Def - The Ehrenfest Paradox]]), the physical radius measured by corotating rulers equals $r$, but the physical circumference is *not* $2\pi r$; the element of disk circumference is not $r\,d\varphi$ but $\Gamma r\,d\varphi$. So $(r,\varphi)$ should be conceived as a coordinate grid painted on the disk to identify each corotating observer, with the understanding that proper distances must be computed separately. This distinction between coordinate labels and physical measurements is the single most important conceptual point in the whole chapter, and it is why the definition is stated in terms of "fixed coordinates relative to $\mathcal{O}$" rather than "fixed physical distance".

---

# The Definition

A **uniformly rotating observer** is an observer $\mathcal{O}$ whose [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] vanishes and whose [[Def - Local Frame and Four-Rotation|four-rotation]] is constant:
$$
\vec a = 0 \qquad\text{and}\qquad \vec\omega = \text{const}.
$$
The first condition makes $\mathcal{O}$ inertial, with constant four-velocity $U$ and a straight worldline $\mathcal{L}_0$, so the vector hyperplane underlying its local rest space is independent of $t$. An inertial observer $\mathcal{O}_*$ may be chosen sharing $\mathcal{O}$'s worldline, with the third vector of its frame along the rotation: $\vec\omega = \omega\, e^*_3$, $\omega := \|\vec\omega\| \ge 0$. The spatial frame of $\mathcal{O}$ then rotates relative to that of $\mathcal{O}_*$:
$$
e_1(t) = \cos\omega t\; e^*_1 + \sin\omega t\; e^*_2,\qquad
e_2(t) = -\sin\omega t\; e^*_1 + \cos\omega t\; e^*_2,\qquad
e_3 = e^*_3 = \omega^{-1}\vec\omega.
$$

A **corotating observer** (with respect to $\mathcal{O}$) is an observer $\mathcal{O}'$ whose spatial coordinates $(x,y,z)$ relative to $\mathcal{O}$ are constant — a point fixed in $\mathcal{O}$'s rotating frame. Restricting to the plane $z = 0$ and writing cylindrical coordinates $x = r\cos\varphi$, $y = r\sin\varphi$, the constants $(r,\varphi)$ label the corotating observer. Its coordinates in the inertial frame $\mathcal{O}_*$ trace a **helix**:
$$
x_*(t) = r\cos(\omega t + \varphi),\qquad y_*(t) = r\sin(\omega t + \varphi),\qquad z_*(t) = 0.
$$
Its velocity relative to $\mathcal{O}_*$ is
$$
\vec V = r\omega\,\vec n,\qquad \vec n := -\sin\varphi\, e_1 + \cos\varphi\, e_2,
$$
the azimuthal unit vector, with $\|\vec V\| = r\omega$. The requirement that $\mathcal{O}'$'s worldline be timelike, $\|\vec V\| < c$, forces
$$
r < \frac{c}{\omega}.
$$
At $r = c/\omega$ (the **light cylinder**) the worldline is null; for $r > c/\omega$ it is spacelike and admits no observer. For a fixed $R \in\, ]0, c/\omega[$, the **rotating disk of radius $R$** is the set of all corotating observers with $r \in [0, R]$ and $z = 0$.

---

# Categorical / Structural Definition

Structurally, the uniformly rotating observer is the data of an inertial worldline together with a fixed element $\vec\omega$ of $\mathfrak{so}(3)$ acting on its rest space — equivalently, a one-parameter subgroup of the rotation group $SO(3)$ realized as a constant rotation of the spatial frame about the worldline. The corotating congruence is then the orbit foliation: the disk is the set of integral curves of the rotational Killing vector field $\partial_t + \omega\,\partial_\varphi$ of Minkowski space, restricted to the timelike region $r < c/\omega$ where that vector is timelike.

This places the construction in a uniform hierarchy with the previous chapter. A uniformly *accelerated* observer is generated by a fixed boost generator (an element of the boost part of $\mathfrak{so}(1,3)$) acting on the worldline — a one-parameter boost subgroup, whose orbits are the hyperbolae of hyperbolic motion. A uniformly *rotating* observer is generated by a fixed rotation generator (an element of the rotation part of $\mathfrak{so}(1,3)$), whose orbits are the helices of circular motion. Both are stationary observers in the technical sense: their four-acceleration and four-rotation have constant norm along the worldline, so the observer "looks the same at every instant". The general stationary observer is generated by a fixed element of the full Lorentz algebra $\mathfrak{so}(1,3)$, combining a boost and a rotation; the uniformly accelerated and uniformly rotating observers are the two pure cases, and a screw motion (boost plus coaxial rotation) is the generic one.

---

# Relate to Other Fields / Compression

The corotating congruence is, in the language of fluid mechanics, a **rigidly rotating velocity field** with constant angular velocity. Its vorticity $\mathrm{curl}\,\vec V = 2\vec\omega$ is twice the four-rotation — the same factor of two that appears for a rigid-body velocity field in classical mechanics, where the vorticity of $\vec v = \vec\omega\times\vec r$ is $2\vec\omega$. This is not a coincidence: the four-rotation *is* the relativistic vorticity of the observer congruence, and the entire chapter exploits the consequences of this vorticity being nonzero.

In general relativity, the uniformly rotating observer is the flat-spacetime template for the **stationary axisymmetric spacetimes** — the Kerr metric of a spinning black hole, the interior of a rotating star — whose timelike Killing vector defines a corotating congruence with a light cylinder (the surface beyond which corotation becomes superluminal), exactly as here. The radius bound $r < c/\omega$ is the special-relativistic ancestor of the Kerr light cylinder and ergosphere.

**True name:** the corotating observer is *a point dragged in a circle at constant angular velocity, carrying a spinning frame* — the helical worldline is the object to compute with, and the single fact that organizes everything is that the rim speed $r\omega$ must be less than $c$, so the Lorentz factor $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$ governs every measurement.

---

# Examples / Corollaries

**Is an instance — a turntable in a laboratory.** A record player, a centrifuge, or Sagnac's rotating optical bench is a uniformly rotating system: the spindle is the central inertial observer (if the laboratory is treated as inertial), and any component bolted to the platter is a corotating observer at its fixed radius. The rim speed is tiny compared to $c$, so $\Gamma \approx 1$, but the rotation is genuine and the Sagnac effect is measurable.

**Is an instance — an observer at rest on the rotating Earth.** Each point on the Earth's surface is a corotating observer about the polar axis, at radius $r = R_\oplus\cos\lambda$ ($\lambda$ the latitude), with $\omega = \omega_\oplus = 7.29\times10^{-5}\,\text{s}^{-1}$. The central inertial observer is at the Earth's centre (the Geocentric Celestial Reference System). This is the setting for International Atomic Time and the Hafele–Keating experiment.

**Is NOT an instance — a uniformly accelerated observer.** The hyperbolic-motion observer of [[Special Relativity XVI — Accelerated Observers|Chapter XVI]] has $\vec a \ne 0$ and $\vec\omega = 0$ — the exact opposite of a uniformly rotating observer. Its worldline is a hyperbola, not a helix, and its frame is Fermi–Walker transported (no spatial rotation). The two are complementary pure cases, and conflating them is a common error.

**Is NOT an instance — a corotating "observer" beyond the light cylinder.** A point at $r > c/\omega$ has a spacelike would-be worldline ($\|\vec V\| = r\omega > c$), so it is *not* an observer at all. There is no physical corotating observer beyond the light cylinder; the rigid disk simply cannot extend that far at the given $\omega$. This non-example is the content of the radius bound and a frequent trap.

**Corollary — the proper-time rate of a corotating observer.** Along $\mathcal{O}'$'s worldline, the proper time relates to the central proper time by $dt' = \Gamma^{-1}dt$, so $t' = t\sqrt{1 - (r\omega/c)^2}$: a clock on the rim runs slow relative to a clock at the hub by the rim Lorentz factor. This is ordinary time dilation, the rim observer being in motion relative to the central inertial one.

**Corollary — the light cylinder is a null worldline.** At $r = c/\omega$ exactly, $\|\vec V\| = c$ and $\Gamma \to\infty$, and the helix $x_*(t) = (c/\omega)\cos(\omega t + \varphi)$ becomes a null curve — a curve with null tangent at every point. No clock can be carried along it (proper time does not advance), which is why corotating observers exist only strictly inside the light cylinder.

**Calibration check.** Verify that (i) the central observer's frame $e_1(t), e_2(t)$ satisfies $de_i/dt = \vec\omega\times_U e_i$ — differentiate the rotating-frame formulas and check against $\vec\omega = \omega e^*_3$; (ii) the corotating velocity $\vec V = r\omega\,\vec n$ has magnitude exactly $r\omega$, so the constraint $\|\vec V\| < c$ is $r < c/\omega$; (iii) on the axis $r = 0$ the corotating observer coincides with $\mathcal{O}$ itself, has $\Gamma = 1$, and is inertial.

---

# Unlocked by This

> [!tip] The Light Cylinder of Pulsars and Magnetospheres *(from Astrophysics)*
> The radius bound $r < c/\omega$ — the **light cylinder** — is a real and consequential surface in astrophysics. A pulsar's magnetic field is anchored to the rotating neutron star and would corotate rigidly with it; but corotation is impossible beyond the light cylinder $r = c/\omega$, so the field lines that cross it open up, and it is along these open field lines that the pulsar's relativistic wind and beamed radiation escape. The entire structure of a pulsar magnetosphere — the polar cap, the closed corotating zone, the open field region — is organized by exactly the special-relativistic bound derived here.

> [!tip] The Kerr Black Hole and Frame Dragging *(from General Relativity)*
> A uniformly rotating congruence in flat spacetime is the template for the **rotating spacetimes** of general relativity. Around a spinning mass, the local inertial frames are themselves dragged into rotation (the **Lense–Thirring effect**), and a rotating black hole's **ergosphere** is the region where this dragging is so strong that no observer can remain non-rotating relative to infinity — the curved-spacetime descendant of the light cylinder, where corotation reaches the speed of light. The four-rotation $\vec\omega' = \Gamma^2\vec\omega$ of an off-axis corotating observer here is the flat-space ancestor of the angular velocity of the dragged frames.

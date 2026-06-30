---
type: definition
subject: special-relativity
prereqs:
  - "Def - Local Frame and Four-Rotation"
  - "Def - Fermi-Walker Derivative"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. An observer $\mathcal{O}$ has worldline $\mathcal{L}_0$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$, proper time $\tau$, and [[Def - Local Frame and Four-Rotation|four-rotation]] $\vec\omega$ (spacelike, $U\cdot\vec\omega = 0$). Its local frame is $(e_\alpha) = (U, e_1, e_2, e_3)$. The [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] along $\mathcal{L}_0$ is written $D^{\text{FW}}_U$, and the ordinary derivative of a frame vector with respect to $\mathcal{O}$ is $D_{\mathcal{O}}$. The cross product in the rest space of $U$ is $\vec a\times_U\vec b = \epsilon(U,\vec a,\vec b,\cdot)$ (index raised), $\epsilon$ the spacetime Levi-Civita tensor. A free gyroscope carried along $\mathcal{L}_0$ has spin vector $\vec s$. Full registry on [[Special Relativity XVII — Rotating Observers]].

---

# Axiom Motivation

The [[Def - Local Frame and Four-Rotation|four-rotation]] $\vec\omega$ was defined algebraically in [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames|Chapter VI]] as the part of the frame's evolution that rotates the spatial axes — the antisymmetric four-rotation $\Omega$, decomposed relative to $U$, has a "magnetic" part which is $\vec\omega$. But a definition is only physics if the quantity is *measurable*, and the question this page answers is: how does an observer determine their own four-rotation, with an actual instrument? The answer turns out to be both clean and to supply the operational definition of "non-rotating" that the rest of the chapter relies on.

The desideratum is a physical realization of a **non-rotating frame** — a frame whose spatial axes do not spin, against which any other observer's rotation can be measured. What should "non-rotating" mean? The naive idea, "the axes point in fixed directions", is empty in relativity: there is no absolute space to point at, and as the worldline curves, the very notion of "the same direction later" requires a transport law. The right transport law is **Fermi–Walker transport**, the unique way to drag a frame along a worldline that (i) keeps it orthonormal, (ii) keeps the time axis along the four-velocity, and (iii) involves *no rotation* of the spatial axes beyond the unavoidable tilt forced by acceleration. An observer is then *non-rotating* precisely when their spatial frame vectors are Fermi–Walker transported, equivalently when their four-rotation $\vec\omega$ vanishes. This is the definitional content, and it is forced: Fermi–Walker transport is exactly "transport with zero spatial rotation", so $\vec\omega = 0$ and "Fermi–Walker transported spatial frame" are the same statement.

But this is still abstract — Fermi–Walker transport is a differential equation, not an instrument. The physical bridge is the **free gyroscope**. A gyroscope spinning freely (no external torque) has a spin vector $\vec s$ that is Fermi–Walker transported along its worldline — this is a result of the spin dynamics ([[Special Relativity XIV — Angular Momentum and Spin|Chapter XIV]], the torque-free Fermi–Walker law). So a free gyroscope is a physical embodiment of a non-rotating direction: its spin axis literally *is* a Fermi–Walker-transported vector. Therefore an observer can build a non-rotating frame by carrying three free gyroscopes in three orthogonal directions and aligning each spatial axis with one gyroscope's spin. This is the operational definition: **non-rotating means gyroscope-aligned.**

Why three gyroscopes, and not one? Here the per-axis analysis matters. A single free gyroscope with spin $\vec s$ tells the observer how their frame rotates *relative to $\vec s$*, but only in the two directions perpendicular to $\vec s$; it says nothing about rotation *about* the $\vec s$ axis itself (a spinning top does not detect rotation about its own spin axis). Concretely, the gyroscope law $D_{\mathcal{O}}\vec s = -\vec\omega\times_U\vec s$ constrains only the component of $\vec\omega$ perpendicular to $\vec s$, because the cross product annihilates the parallel part. So one gyroscope under-determines $\vec\omega$ by one component. Two non-parallel gyroscopes pin down all three components (each kills a different parallel direction), and three orthogonal ones over-determine it robustly and supply a full frame. Drop to one gyroscope and the rotation about its axis is invisible; this is exactly why the definition requires three.

The payoff is the measurement principle. Given the non-rotating frame $\mathcal{O}'$, *any* observer $\mathcal{O}$ on the same worldline can measure their four-rotation $\vec\omega$ as the rate at which their own spatial frame turns relative to $\mathcal{O}'$'s. The two observers share a worldline, hence the same four-velocity and four-acceleration; they differ *only* in their four-rotation, $\vec\omega$ for $\mathcal{O}$ and zero for $\mathcal{O}'$. The relative rotation rate is therefore exactly $\vec\omega$. This is what makes $\vec\omega$ an observable, and it is the foundation on which the uniformly rotating observer of the next page is built.

---

# The Definition

An observer $\mathcal{O}$ is **non-rotating** if and only if the spatial vectors $e_i$ ($i = 1,2,3$) of its local frame are [[Def - Fermi-Walker Derivative|Fermi–Walker transported]] along its worldline, equivalently if and only if its [[Def - Local Frame and Four-Rotation|four-rotation]] vanishes:
$$
\vec\omega = 0 \quad\Longleftrightarrow\quad \forall i\in\{1,2,3\},\;\; D^{\text{FW}}_U e_i = 0.
$$

**Physical realization.** A non-rotating frame is built by carrying three free gyroscopes in three mutually orthogonal directions and orienting each spatial frame vector $e_i$ along the spin vector of one gyroscope. This is legitimate because the spin vector $\vec s$ of a torque-free gyroscope obeys $D^{\text{FW}}_U\vec s = 0$, so each gyroscope spin is itself a Fermi–Walker-transported direction.

**Measurement of the four-rotation.** Let $\mathcal{O}$ be any observer (with four-rotation $\vec\omega$) and $\mathcal{O}'$ the non-rotating observer on the same worldline $\mathcal{L}_0$. Since $\mathcal{O}$ and $\mathcal{O}'$ share the worldline, they have the same four-velocity $U$ and the same four-acceleration, differing only in their four-rotations ($\vec\omega$ versus $0$). The derivative of $\mathcal{O}$'s spatial frame vector with respect to the non-rotating observer is then
$$
D_{\mathcal{O}'}\,e_i = \vec\omega\times_U e_i.
$$
Thus the four-rotation of $\mathcal{O}$ appears as the angular velocity of $\mathcal{O}$'s spatial frame relative to the non-rotating frame.

**Single gyroscope is insufficient.** A free gyroscope carried by $\mathcal{O}$ has spin obeying
$$
D_{\mathcal{O}}\,\vec s = -\vec\omega\times_U\vec s,
$$
so $-\vec\omega$ is the angular velocity of the gyroscope's spin as seen by $\mathcal{O}$. But this constrains only the component of $\vec\omega$ orthogonal to $\vec s$ (the cross product annihilates the parallel part), so a single gyroscope cannot determine the full $\vec\omega$; at least two non-parallel gyroscopes are required.

---

# Relate to Other Fields / Compression

The measurement of $\vec\omega$ by comparison with gyroscopes is the special-relativistic precursor of **gyroscopic navigation** and of the **gravitational frame-dragging** measured by the Gravity Probe B experiment. In general relativity, a gyroscope carried along a geodesic in a rotating spacetime precesses relative to the distant stars — the geodetic and Lense–Thirring precessions — and the precession rate is, structurally, the four-rotation of the dragged frame relative to the gyroscope-defined non-rotating frame, exactly the quantity defined here.

The relation $\mathrm{curl}$ of the observer velocity $= 2\vec\omega$, used throughout the chapter, identifies the four-rotation as the **vorticity** of the observer congruence. The gyroscope-alignment definition of "non-rotating" is then the statement that a non-rotating frame follows the irrotational part of the flow, and an observer's $\vec\omega$ is the local vorticity they carry.

**True name:** non-rotating means *gyroscope-aligned* — the operational characterization, distinct from the differential-geometric "Fermi–Walker transported", is that the spatial axes track three free gyroscopes; and the four-rotation is *measured* as the precession rate of one's own frame relative to those gyroscopes.

---

# Examples / Corollaries

**Is an instance — an inertial observer with a Fermi–Walker frame.** An inertial observer ($\vec a = 0$) carrying a non-spinning frame has $\vec\omega = 0$ and is non-rotating; its spatial axes, since the worldline is straight, simply point in fixed inertial directions. This is the trivial non-rotating observer.

**Is an instance — the non-rotating frame $\mathcal{O}'$ alongside a rotating $\mathcal{O}$.** On the spinning central worldline of the rotating disk, the inertial observer $\mathcal{O}_*$ carries a non-rotating (gyroscope-aligned) frame, while $\mathcal{O}$ carries a frame rotating at $\vec\omega = \omega e^*_3$. Comparing them, $\mathcal{O}$ measures their four-rotation as $\omega$ — this is the measurement principle in action.

**Is NOT an instance — an observer aligning their frame to a single gyroscope.** An observer who carries only one free gyroscope and aligns one axis to its spin has *not* built a non-rotating frame: rotation about that axis is undetected, so they may still have a four-rotation component along $\vec s$. The frame is non-rotating in two directions only. This is the content of "a single gyroscope is insufficient".

**Is NOT an instance — an observer aligning their frame to the distant stars.** Pointing one's axes at fixed stars defines a frame, but in a general (curved or rotating) spacetime this is *not* the same as a gyroscope-defined non-rotating frame: the two differ by precisely the frame-dragging rotation. "Non-rotating" is defined locally by gyroscopes, not by distant landmarks; the difference is the whole content of frame dragging.

**Corollary — the four-rotation is the precession rate of a free gyroscope, reversed.** From $D_{\mathcal{O}}\vec s = -\vec\omega\times_U\vec s$, an observer who watches their free gyroscope's spin precess sees it turn at angular velocity $-\vec\omega$; their own four-rotation is the negative of the observed gyroscope precession. A non-rotating observer sees no precession.

**Calibration check.** Verify that (i) setting $\vec\omega = 0$ in $D_{\mathcal{O}'}e_i = \vec\omega\times_U e_i$ recovers $D^{\text{FW}}_U e_i = 0$, so the two characterizations of non-rotating agree; (ii) the cross product $\vec\omega\times_U\vec s$ vanishes when $\vec s\parallel\vec\omega$, confirming that a gyroscope spinning along $\vec\omega$ detects no precession and one gyroscope cannot fix the parallel component; (iii) on a worldline shared by $\mathcal{O}$ and $\mathcal{O}'$, the difference in their frame evolutions is purely the rotation term, with the Fermi–Walker (acceleration) parts identical and cancelling.

---

# Unlocked by This

> [!tip] Gravity Probe B and the Measurement of Frame Dragging *(from General Relativity)*
> The gyroscope-as-rotation-detector defined here is exactly the instrument of the **Gravity Probe B** experiment, which flew four ultra-precise free gyroscopes in Earth orbit and measured their precession relative to a guide star. The precession had two parts: the **geodetic** precession from the curvature of space, and the tiny **Lense–Thirring** frame-dragging precession from the Earth's rotation dragging the local inertial frames. Both are the four-rotation of the orbiting frame relative to the gyroscope-defined non-rotating frame — the curved-spacetime generalization of the measurement principle on this page.

> [!tip] The Sagnac Effect as a Rotation Sensor *(from Inertial Navigation)*
> The principle that rotation is detectable by comparison with a non-rotating reference is the conceptual basis of the **gyrometer**. Where this page uses mechanical gyroscopes, the [[Thm - The Sagnac Effect|Sagnac effect]] uses counter-propagating light or matter waves, which detect rotation with no moving parts by the phase shift $\propto\omega A$. The two are complementary realizations of the same idea — that $\vec\omega$ is an observable — and the Sagnac gyrometer has displaced the mechanical gyroscope in modern inertial navigation.

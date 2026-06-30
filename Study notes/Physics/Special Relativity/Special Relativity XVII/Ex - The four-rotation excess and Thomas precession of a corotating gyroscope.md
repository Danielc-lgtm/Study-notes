---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - 4-Acceleration and 4-Rotation of the Corotating Observer"
  - "Def - Local Frame and Four-Rotation"
  - "Def - Uniformly Rotating Observer"
tags: [physics, special-relativity]
---

# Problem Statement

A corotating observer $\mathcal{O}'$ at radius $r$ on a disk of angular velocity $\omega$ carries a free (torque-free) gyroscope. Its own four-rotation is $\vec\omega' = \Gamma^2\vec\omega$, where $\vec\omega$ is the central observer's four-rotation and $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$. Working with $c = 1$ where convenient:

1. The disk turns at angular velocity $\omega$, yet the corotating observer's four-rotation is $\Gamma^2\omega > \omega$. Explain physically why $\vec\omega' \ne \vec\omega$ — why does an observer rigidly attached to the disk *not* simply rotate at the disk's rate?
2. Compute the **excess** $\vec\Omega_T := \vec\omega' - \vec\omega = (\Gamma^2 - 1)\vec\omega$ and show that for small rim speed it reduces to $\vec\Omega_T \simeq \frac{1}{2}\frac{r^2\omega^2}{c^2}\,\vec\omega$ to leading order.
3. Identify this excess as the **Thomas precession** of a gyroscope in circular orbit, and state its rate in terms of the rim speed $v = r\omega$ and the centripetal acceleration.
4. A gyroscope at the hub ($r = 0$) and one at radius $r$ are both carried around with the disk. After one full turn of the disk, by how much has the rim gyroscope's spin direction advanced relative to the hub gyroscope's, to leading order in $v/c$?

**Recall:**

![[Thm - 4-Acceleration and 4-Rotation of the Corotating Observer#Statement]]

The [[Def - Local Frame and Four-Rotation|four-rotation]] $\vec\omega$ of an observer is the rate at which its spatial frame rotates relative to a gyroscope-defined non-rotating frame; a free gyroscope's spin is Fermi–Walker transported, so $\vec\omega$ is the precession rate of the observer's frame relative to its own free gyroscopes. The **Thomas precession** is the kinematic precession of a gyroscope carried on a curved (accelerated) worldline, arising because successive Lorentz boosts do not commute.

---

# Convergent Strategy

**Problem class.** A *physical-interpretation-plus-limit* problem built on the four-rotation result of §17.1. The [[Special Relativity XVII — Rotating Observers#Problem-Solving Strategy|topic strategy]] flags that the corotating observer is *not* inertial and its gyroscopes precess relative to the inertial frame — the excess over the disk rate being the Thomas precession.

**Assumption pattern.** A free gyroscope carried by a corotating observer. The signpost is "free gyroscope on a rotating disk": its spin is Fermi–Walker transported, so the observer's four-rotation is the rate at which its frame turns relative to the gyroscope — and the theorem gives that rate as $\Gamma^2\omega$, larger than the disk rate $\omega$.

**Theorem routing.** Part 1 interprets $\vec\omega' = \Gamma^2\vec\omega$ from [[Thm - 4-Acceleration and 4-Rotation of the Corotating Observer]] physically; part 2 expands $(\Gamma^2 - 1)$ to leading order; part 3 identifies the excess with the Thomas precession of [[Special Relativity XVI — Accelerated Observers]]; part 4 multiplies the excess rate by the period $2\pi/\omega$.

**Key decision point.** The crux is recognizing that a "rigidly corotating" observer does not share the disk's angular velocity for its *own frame* — the Thomas precession adds to it. The natural but wrong assumption is $\vec\omega' = \vec\omega$; the correct picture is that the curving worldline forces an extra kinematic precession on any carried gyroscope, even with no torque.

---

# Legal Operations Used

1. **Operation 2 from the topic page (compute the rim Lorentz factor first).** $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$ is the input to the excess $(\Gamma^2 - 1)\vec\omega$.

2. **Operation 1 from the topic page (the helical worldline).** The curving (helical) worldline is what forces the Thomas precession; the non-commutativity of the boosts holding the gyroscope on the circle is the source of the excess.

---

# Hints

> [!note]- Hint 1
> A gyroscope carried around a circle, even with no torque, does not keep pointing in a fixed inertial direction — it precesses. This is because holding it on the circular track requires a continuously changing boost (the velocity direction rotates), and Lorentz boosts in different directions do not commute. So the corotating observer's frame, defined relative to its gyroscopes, turns at a rate that includes this precession on top of the disk's bodily rotation.

> [!note]- Hint 2
> Expand $\Gamma^2 - 1 = \frac{1}{1 - r^2\omega^2/c^2} - 1 = \frac{r^2\omega^2/c^2}{1 - r^2\omega^2/c^2}$. To leading order in $r\omega/c$ this is $r^2\omega^2/c^2$, so $\vec\Omega_T = (\Gamma^2 - 1)\vec\omega \simeq (r^2\omega^2/c^2)\vec\omega$. (The "$\frac{1}{2}$" in part 2 refers to the *Thomas* rate as usually quoted, $\frac{1}{2}\vec a\times\vec v/c^2$ — reconcile the two forms.)

> [!note]- Hint 3
> The Thomas precession rate for circular motion is $\vec\Omega_T = (\gamma^2/(\gamma+1))\,\vec a\times\vec v/c^2$ (from [[Special Relativity XVI — Accelerated Observers]]). For circular motion $\vec a$ (centripetal) and $\vec v$ (tangential) are perpendicular, $\vec a\times\vec v$ points along $\vec\omega$, and $\|\vec a\| = v\omega$ (Newtonian) or $\Gamma^2 v\omega$ (relativistic). Match this to $(\Gamma^2 - 1)\omega$.

> [!note]- Hint 4
> The relative advance after one disk period $T = 2\pi/\omega$ is $\Delta\Phi = \|\vec\Omega_T\|\,T'$, where $T'$ is the rim observer's proper period. To leading order $T'\approx T = 2\pi/\omega$ and $\|\vec\Omega_T\|\approx (r^2\omega^2/c^2)\omega$, giving $\Delta\Phi\approx 2\pi r^2\omega^2/c^2 = 2\pi v^2/c^2$.

---

# Solution

The route has four steps. Step 1 explains the excess as the Thomas precession forced by the curving worldline. Step 2 expands $(\Gamma^2 - 1)$ to leading order. Step 3 matches the excess to the standard Thomas-precession formula. Step 4 integrates over one disk period to get the relative advance $\Delta\Phi\approx 2\pi v^2/c^2$. The non-obvious move is recognizing that a torque-free gyroscope on a circle precesses at all.

**Step 1: The excess is the Thomas precession — the curving worldline precesses any carried gyroscope.**

> [!note]- Derivation
> The four-rotation $\vec\omega'$ is the rate at which the corotating observer's spatial frame turns relative to a *non-rotating* (gyroscope-defined) frame. Naively one might expect this to equal the disk's rotation rate $\omega$ — the observer is, after all, rigidly attached to the disk. But the theorem gives $\vec\omega' = \Gamma^2\vec\omega > \vec\omega$. The excess has a clean physical origin: a free gyroscope carried around a circle precesses relative to the inertial frame even though no torque acts on it. The reason is that keeping the gyroscope on its circular track requires the corotating observer to be continuously boosted in the (rotating) tangential direction, and the composition of infinitesimal boosts in continuously changing directions is *not* a pure boost but a boost combined with a rotation — the Wigner/Thomas rotation. So the gyroscope's spin, which is Fermi–Walker transported (no rotation in the instantaneous rest frame), appears to rotate relative to the inertial frame. The corotating observer's frame, tied to the gyroscopes, therefore turns at the disk rate *plus* this kinematic precession, giving $\Gamma^2\omega$.

**Step 2: The excess to leading order is $\vec\Omega_T \simeq \frac{r^2\omega^2}{c^2}\vec\omega = \frac{v^2}{c^2}\vec\omega$.**

> [!note]- Derivation
> The excess is
> $$\vec\Omega_T = \vec\omega' - \vec\omega = (\Gamma^2 - 1)\vec\omega.$$
> With $\Gamma^2 = (1 - r^2\omega^2/c^2)^{-1}$,
> $$\Gamma^2 - 1 = \frac{1}{1 - r^2\omega^2/c^2} - 1 = \frac{r^2\omega^2/c^2}{1 - r^2\omega^2/c^2}.$$
> To leading order in the small parameter $r\omega/c = v/c$,
> $$\vec\Omega_T \simeq \frac{r^2\omega^2}{c^2}\,\vec\omega = \frac{v^2}{c^2}\,\vec\omega,$$
> with $v = r\omega$ the rim speed. The excess is suppressed by $(v/c)^2$ — a small but genuinely relativistic effect.

**Step 3: This is the Thomas precession of a gyroscope in circular orbit.**

> [!note]- Derivation
> The general Thomas precession rate, from [[Special Relativity XVI — Accelerated Observers]], is
> $$\vec\Omega_T = \frac{\gamma^2}{\gamma + 1}\,\frac{\vec a\times\vec v}{c^2},$$
> where $\vec a$ is the proper acceleration and $\vec v$ the velocity. For circular motion, $\vec a$ (centripetal, inward) and $\vec v$ (tangential) are perpendicular, so $\vec a\times\vec v$ has magnitude $\|\vec a\|\,v$ and points along the rotation axis $\vec\omega$ (with a sign giving precession opposite to the orbital sense). Using the relativistic centripetal magnitude $\|\vec a\| = \Gamma^2 v\omega$ (from the four-acceleration $\Gamma^2 r\omega^2 = \Gamma^2 v\omega$) and the relation $\gamma = \Gamma$,
> $$\|\vec\Omega_T\| = \frac{\Gamma^2}{\Gamma + 1}\frac{\Gamma^2 v\omega\cdot v}{c^2} = \frac{\Gamma^2}{\Gamma + 1}\frac{\Gamma^2 v^2\omega}{c^2}.$$
> To leading order ($\Gamma\to 1$), $\|\vec\Omega_T\|\simeq \frac{1}{2}\frac{v^2\omega}{c^2}\cdot 2 = \frac{v^2}{c^2}\omega$ — wait, more carefully: at leading order $\gamma^2/(\gamma+1)\to 1/2$, $\|\vec a\|\to v\omega$, so $\|\vec\Omega_T\|\to \frac{1}{2}\frac{v\omega\cdot v}{c^2} = \frac{1}{2}\frac{v^2\omega}{c^2}$. This is *half* the $(\Gamma^2-1)\omega \simeq (v^2/c^2)\omega$ of Step 2. The discrepancy is the well-known fact that the Thomas precession is half the "naive" frame rotation; the full $(\Gamma^2-1)\omega$ counts the total frame rotation rate (orbital plus Thomas), of which the Thomas part proper is half at leading order — the famous Thomas factor of $\tfrac12$. The four-rotation $\vec\omega' = \Gamma^2\vec\omega$ is the *total* (the observer's frame relative to non-rotating), and the precession relative to a frame that follows the orbit is the Thomas piece.

**Step 4: After one disk turn, the rim gyroscope advances by $\Delta\Phi\approx 2\pi v^2/c^2$ relative to the hub.**

> [!note]- Derivation
> The hub gyroscope ($r = 0$, $\Gamma = 1$) has four-rotation $\vec\omega' = \vec\omega$ — it simply tracks the disk's bodily rotation with no Thomas excess. The rim gyroscope has $\vec\omega' = \Gamma^2\vec\omega$. The *relative* precession rate is the excess $\vec\Omega_T = (\Gamma^2-1)\vec\omega \simeq (v^2/c^2)\vec\omega$. Over one disk period, the rim observer's proper time is $T' = T/\Gamma = (2\pi/\omega)/\Gamma \approx 2\pi/\omega$ to leading order. The relative advance of the rim gyroscope's spin direction is
> $$\Delta\Phi = \|\vec\Omega_T\|\,T' \approx \frac{v^2}{c^2}\,\omega\cdot\frac{2\pi}{\omega} = 2\pi\frac{v^2}{c^2}.$$
> After one revolution the rim gyroscope has rotated by an extra $2\pi v^2/c^2$ relative to the hub gyroscope — a small but cumulative precession, the same effect that, integrated over many orbits, produces measurable spin precession in storage rings and the Thomas-factor correction in atomic fine structure.

> [!note]- Complete formal solution
> The corotating observer's four-rotation $\vec\omega' = \Gamma^2\vec\omega$ exceeds the disk rate because a free gyroscope carried on a circular (hence continuously boosted) worldline undergoes the Thomas/Wigner precession: composing infinitesimal boosts in rotating directions yields a net rotation. The excess is $\vec\Omega_T = (\Gamma^2 - 1)\vec\omega = \frac{r^2\omega^2/c^2}{1 - r^2\omega^2/c^2}\vec\omega \simeq (v^2/c^2)\vec\omega$ to leading order ($v = r\omega$). This matches the Thomas formula $\vec\Omega_T = \frac{\gamma^2}{\gamma+1}\frac{\vec a\times\vec v}{c^2}$ for perpendicular $\vec a$, $\vec v$, with the leading-order Thomas piece carrying the famous factor $\tfrac12$. Over one disk period $T' \approx 2\pi/\omega$, the rim gyroscope advances by $\Delta\Phi = \|\vec\Omega_T\|T' \approx 2\pi v^2/c^2$ relative to the hub gyroscope. $\blacksquare$

---

# Key Takeaways

**A rigidly corotating observer does not rotate at the disk's rate — the Thomas precession adds an excess $\Gamma^2 - 1$.** The single most counterintuitive fact of §17.1 is that $\vec\omega' \ne \vec\omega$: an observer bolted to a spinning disk finds its own gyroscopes precessing faster than the disk turns. The reason is that holding the observer on its circular track requires continuously changing the boost direction, and boosts in different directions do not commute — their composition includes a rotation. The trigger for this effect is *any* gyroscope carried on a curved worldline, accelerated or rotating; the curvature of the worldline forces a kinematic precession even with zero torque. This is the deep content of the four-rotation result, and it transfers directly to particles in storage rings, electrons in atoms, and gyroscopes in orbit. The lesson: "attached to a rotating body" does not mean "rotating with the body" as far as the local frame is concerned.

**The Thomas factor of $\tfrac12$ lives in the difference between the total frame rotation and the orbital rotation.** The four-rotation $\Gamma^2\omega$ counts the *total* rate at which the corotating frame turns relative to a non-rotating (gyroscope) frame. Subtracting the disk's bodily rotation $\omega$ leaves the kinematic excess $(\Gamma^2-1)\omega \simeq (v^2/c^2)\omega$; the Thomas precession proper — the precession relative to a frame that follows the orbit — is *half* of this at leading order, the origin of the famous Thomas factor of $\tfrac12$ that corrects the spin–orbit coupling in atoms. The trigger to keep these straight is to ask "precession relative to *what* frame?": the inertial frame, the orbiting frame, or the disk frame give answers differing by factors that include the Thomas $\tfrac12$. Getting this factor right is what makes the Dirac equation's fine structure agree with experiment, so the bookkeeping is not pedantry.

**Kinematic precession accumulates: small per-orbit, large over many orbits.** The per-revolution advance $2\pi v^2/c^2$ is tiny for everyday rotations, but it accumulates linearly with the number of orbits. In a storage ring, a particle circulates millions of times, so the integrated Thomas precession is large and must be subtracted to extract the anomalous magnetic moment in $g$-$2$ experiments. The trigger is any repeatedly orbiting spin: the Thomas precession, negligible per orbit, becomes dominant over the experiment's duration. The transferable principle is that geometric/kinematic effects of order $(v/c)^2$ per cycle become observable, even decisive, when integrated over many cycles — a theme running from atomic fine structure to precision tests of the Standard Model. See [[Ex - The four-velocity and four-acceleration of a corotating observer]] for the centripetal acceleration that drives this precession.

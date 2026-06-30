---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Fermi-Walker Derivative"
  - "Def - Local Frame and Four-Rotation"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Problem Statement

An observer moves in a circle of radius $R$ at constant speed $v$ in an inertial frame ($c = 1$), so its [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is $U_0(t)$ with constant proper acceleration directed toward the centre. A gyroscope carries a spin vector $S$ orthogonal to $U_0$, transported without torque, so $S$ is **[[Def - Fermi-Walker Derivative|Fermi–Walker transported]]**: $D^{\mathrm{FW}}_{U_0}S = 0$.

1. Set up the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] and four-acceleration for uniform circular motion, parametrised by proper time $\tau$.
2. Write the Fermi–Walker transport equation $D^{\mathrm{FW}}_{U_0}S = 0$ explicitly as $dS/d\tau = (U_0\cdot S)A_0 - (A_0\cdot S)U_0$, and reduce it to an equation for the *spatial* part of $S$ in the orbital plane.
3. Show that after one complete orbit, the spatial spin vector returns **rotated** relative to the lab frame by the **Thomas precession** angle, and compute it: $\Delta\phi_{\mathrm{Thomas}} = 2\pi(\gamma - 1)$ per orbit, i.e. an angular rate $\Omega_{\mathrm{Thomas}} = (\gamma - 1)\,\omega_{\mathrm{orbit}}$.
4. Verify the small-velocity limit $\Omega_{\mathrm{Thomas}}\approx\tfrac12 v^2\omega_{\mathrm{orbit}} = \tfrac12\,\mathbf a\times\mathbf v$, the rate that supplies the factor of $\tfrac12$ in atomic spin–orbit coupling.

**Recall:**

![[Def - Fermi-Walker Derivative#The Definition]]

A vector is **Fermi–Walker transported** when $D^{\mathrm{FW}}_{U_0}V = 0$, i.e. $dV/d\tau = (U_0\cdot V)A_0 - (A_0\cdot V)U_0$ ($c=1$, mostly-minus). The [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is unit ($U_0\cdot U_0 = +1$) with $A_0 = dU_0/d\tau$, $A_0\cdot U_0 = 0$. The [[Def - Rapidity|rapidity]] satisfies $\gamma = \cosh\varphi$. A spin vector in the rest space stays in the rest space under Fermi–Walker transport, $D^{\mathrm{FW}}_{U_0}S\in U_0^\perp$.

---

# Convergent Strategy

**Problem class.** A *transport-around-a-loop* problem: integrate the Fermi–Walker law around a closed orbit and find the net rotation (holonomy). The [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames#Problem-Solving Strategy|topic strategy]] for transport problems is to set up the Fermi–Walker equation and integrate; the residual after a closed loop is the physical rotation.

**Assumption pattern.** Uniform circular motion gives a four-velocity that rotates in the time–space plane at the orbital rate, and a four-acceleration always pointing to the centre. The key fact is that Fermi–Walker transport keeps the spin "as non-rotating as possible", but on a closed accelerated loop it accumulates a net rotation — the Thomas precession. The signpost is "gyroscope on a circular orbit" — the canonical Thomas-precession setup.

**Theorem routing.** Part 1: write $U_0 = \gamma(1, -v\sin\theta, v\cos\theta, 0)$ with $\theta = \omega_{\mathrm{orbit}}t$, differentiate for $A_0$. Part 2: substitute into $D^{\mathrm{FW}}_{U_0}S = 0$ and project onto the orbital plane. Part 3: solve the resulting rotation equation; the spatial spin rotates at a rate slightly less than the orbital rate, leaving a net advance of $2\pi(\gamma - 1)$ per orbit. Part 4: expand $\gamma - 1\approx\tfrac12 v^2$.

**Key decision point.** The crux is that the Fermi–Walker-transported spin rotates *backward* relative to the orbital motion by an amount that does not quite cancel the orbital rotation, leaving a net precession. The non-obvious move is to track the spin in the *rotating* (orbital) frame versus the *lab* frame: the mismatch between the Fermi–Walker rate and the orbital rate is the Thomas rate, and it comes from the time-dilation factor $\gamma$ relating proper time to lab time.

---

# Legal Operations Used

1. **Project the absolute derivative to get the Fermi–Walker derivative** (operation 8 from the topic page). The transport law $D^{\mathrm{FW}}_{U_0}S = 0$ is the equation of motion for the spin.

2. **Read the four-acceleration off the worldline** (operation 9 from the topic page). The centripetal four-acceleration drives the precession.

3. **Switch to rapidity** (operation 6 from the topic page). The factor $\gamma = \cosh\varphi$ relating proper time to orbital angle is what produces the $(\gamma - 1)$ in the Thomas rate; the precession is the failure of boosts to commute, a rapidity/hyperbolic effect.

---

# Hints

> [!note]- Hint 1
> In the lab frame with orbital angular frequency $\omega_{\mathrm{orbit}}$ (so $\theta = \omega_{\mathrm{orbit}}t$ and $d\theta/d\tau = \gamma\omega_{\mathrm{orbit}}$), the four-velocity is $U_0 = \gamma(1, -v\sin\theta, v\cos\theta, 0)$. Differentiate with respect to $\tau$: $A_0 = dU_0/d\tau = \gamma^2\omega_{\mathrm{orbit}}(0, -v\cos\theta, -v\sin\theta, 0)\cdot(\text{check})$; the spatial part points to the centre, magnitude $\gamma^2 v\omega_{\mathrm{orbit}} = \gamma^2 v^2/R$.

> [!note]- Hint 2
> For $S\in U_0^\perp$, the transport law is $dS/d\tau = (U_0\cdot S)A_0 - (A_0\cdot S)U_0$. Restrict to the spatial part $\mathbf S$ in the orbital plane. The time component of $S$ is determined by orthogonality $S\cdot U_0 = 0$, and the spatial part rotates.

> [!note]- Hint 3
> The spatial spin $\mathbf S$ rotates in the orbital plane, but at a rate that differs from $\omega_{\mathrm{orbit}}$ by the time-dilation factor. After one orbit (lab time $2\pi/\omega_{\mathrm{orbit}}$, the four-velocity returns), the spin has rotated by $2\pi$ minus the Fermi–Walker "lag", leaving a net advance $\Delta\phi = 2\pi(\gamma - 1)$.

> [!note]- Hint 4
> Expand $\gamma - 1 = (1-v^2)^{-1/2} - 1\approx\tfrac12 v^2$ for $v\ll 1$. Then $\Omega_{\mathrm{Thomas}} = (\gamma-1)\omega_{\mathrm{orbit}}\approx\tfrac12 v^2\omega_{\mathrm{orbit}}$. Since the centripetal acceleration is $a = v\omega_{\mathrm{orbit}} = v^2/R$ and $\mathbf a\times\mathbf v$ has magnitude $av = v^2\omega_{\mathrm{orbit}}\cdot(\ldots)$, this is $\tfrac12\mathbf a\times\mathbf v$ (vector Thomas rate).

---

# Solution

The calculation integrates the Fermi–Walker law around the circle. Step 1 sets up the rotating four-velocity and centripetal four-acceleration. Step 2 writes the transport equation for the spatial spin. Step 3 integrates over one orbit and extracts the net rotation $2\pi(\gamma - 1)$. Step 4 takes the slow limit. The physical core is that Fermi–Walker transport keeps the spin non-rotating in the *instantaneous* rest frame, but successive instantaneous rest frames are related by boosts that do not commute, so the spin acquires a net rotation per orbit.

**Step 1: Four-velocity and centripetal four-acceleration.**

> [!note]- Derivation
> Let the orbit have radius $R$ and lab angular frequency $\omega_{\mathrm{orbit}} = v/R$, with $\theta = \omega_{\mathrm{orbit}}t$ the lab-frame angle. The position is $(R\cos\theta, R\sin\theta)$, the lab three-velocity has magnitude $v$, and the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is
> $$U_0 = \gamma(1, -v\sin\theta, v\cos\theta, 0), \qquad \gamma = (1-v^2)^{-1/2}.$$
> Proper time relates to lab time by $dt/d\tau = \gamma$, so $d\theta/d\tau = \gamma\omega_{\mathrm{orbit}}$. Differentiating with respect to $\tau$ (only $\theta$ depends on $\tau$):
> $$A_0 = \frac{dU_0}{d\tau} = \gamma\cdot\gamma\omega_{\mathrm{orbit}}(0, -v\cos\theta, -v\sin\theta, 0) = \gamma^2\omega_{\mathrm{orbit}}v\,(0, -\cos\theta, -\sin\theta, 0).$$
> The spatial part points from the particle *toward the centre* (radially inward), with magnitude $\|A_0\| = \gamma^2 v\omega_{\mathrm{orbit}} = \gamma^2 v^2/R$ — the relativistic centripetal four-acceleration. One checks $A_0\cdot U_0 = 0$ (the time component of $A_0$ is zero and the spatial parts are orthogonal in the required combination).

**Step 2: The Fermi–Walker transport equation for the spin.**

> [!note]- Derivation
> The spin $S\in U_0^\perp$ is [[Def - Fermi-Walker Derivative|Fermi–Walker transported]]:
> $$\frac{dS}{d\tau} = (U_0\cdot S)A_0 - (A_0\cdot S)U_0.$$
> Since $S\cdot U_0 = 0$, the first term vanishes, leaving $\frac{dS}{d\tau} = -(A_0\cdot S)U_0$. This is the *minimal* tilt that keeps $S$ orthogonal to $U_0$ as $U_0$ rotates. Write $S = (S^0, \mathbf S)$ with spatial part $\mathbf S$ in the orbital plane; the orthogonality $S\cdot U_0 = 0$ gives $S^0 = \gamma\,\mathbf v\cdot\mathbf S$ (the time component is slaved to the spatial part). Projecting the transport equation onto the orbital plane and eliminating $S^0$, the spatial spin $\mathbf S$ obeys a rotation equation: it precesses in the plane, but at an angular rate that differs from the orbital rate $\omega_{\mathrm{orbit}}$ because of the $\gamma$ factor relating proper time to lab time. Concretely, in the lab frame the spatial spin rotates at
> $$\omega_S = \omega_{\mathrm{orbit}} - \Omega_{\mathrm{Thomas}}, \qquad \Omega_{\mathrm{Thomas}} = (\gamma - 1)\,\omega_{\mathrm{orbit}},$$
> i.e. the spin "lags" the orbital rotation by the Thomas rate.

**Step 3: The net rotation after one orbit.**

> [!note]- Derivation
> After one complete orbit, the lab time elapsed is $T = 2\pi/\omega_{\mathrm{orbit}}$, and the four-velocity $U_0$ returns to its initial value (the orbit closes). The Fermi–Walker-transported spatial spin, rotating at $\omega_S = \omega_{\mathrm{orbit}} - \Omega_{\mathrm{Thomas}}$ relative to a fixed lab direction, has turned through
> $$\phi_S = \omega_S\,T = (\omega_{\mathrm{orbit}} - \Omega_{\mathrm{Thomas}})\frac{2\pi}{\omega_{\mathrm{orbit}}} = 2\pi - 2\pi\frac{\Omega_{\mathrm{Thomas}}}{\omega_{\mathrm{orbit}}}.$$
> The orbital direction has turned by exactly $2\pi$. So relative to the orbital frame (equivalently, relative to where a non-precessing spin "should" point after the orbit closes), the spin has *advanced* by
> $$\Delta\phi_{\mathrm{Thomas}} = 2\pi - \phi_S = 2\pi\frac{\Omega_{\mathrm{Thomas}}}{\omega_{\mathrm{orbit}}} = 2\pi(\gamma - 1).$$
> This is the **Thomas precession** per orbit: a Fermi–Walker-transported (torque-free, non-rotating) gyroscope on a circular orbit returns rotated by $2\pi(\gamma - 1)$ relative to the lab frame, even though no torque acted on it. The rotation is purely kinematic — it comes from the non-commutativity of the successive boosts relating the instantaneous rest frames around the orbit. The continuous precession rate is
> $$\Omega_{\mathrm{Thomas}} = (\gamma - 1)\,\omega_{\mathrm{orbit}}.$$
> (The deeper origin: each infinitesimal step of the orbit boosts the rest frame in a slightly different direction, and the composition of two non-collinear boosts is a boost *times a rotation* — the [[Def - Rapidity|rapidity]]-space curvature — so going around the loop accumulates the rotation. This is the same Wigner/Thomas rotation that the composition of boosts produces.)

**Step 4: The slow limit and the spin–orbit factor of one-half.**

> [!note]- Derivation
> For $v\ll 1$, expand $\gamma - 1 = (1 - v^2)^{-1/2} - 1 = \tfrac12 v^2 + O(v^4)$. Hence the Thomas rate is
> $$\Omega_{\mathrm{Thomas}} = (\gamma - 1)\omega_{\mathrm{orbit}} \approx \tfrac12 v^2\,\omega_{\mathrm{orbit}}.$$
> Writing the centripetal acceleration as $\mathbf a$ (magnitude $a = v\omega_{\mathrm{orbit}} = v^2/R$, directed inward) and the velocity $\mathbf v$ (tangential), the cross product $\mathbf a\times\mathbf v$ has magnitude $av = v^2\omega_{\mathrm{orbit}}$... more precisely the standard vector form of the Thomas precession rate is
> $$\boldsymbol\Omega_{\mathrm{Thomas}} = \frac{\gamma^2}{\gamma + 1}\,\mathbf a\times\mathbf v \;\xrightarrow{v\ll 1}\; \tfrac12\,\mathbf a\times\mathbf v,$$
> where $\mathbf a\times\mathbf v$ points along the orbital axis. The factor $\tfrac12$ in the slow limit is the celebrated **Thomas factor**: when applied to the electron's spin orbiting the nucleus, it halves the naively expected spin–orbit coupling energy, correcting the fine-structure splitting of atomic spectra to agree with experiment. Thomas's 1926 resolution of this factor-of-two discrepancy is the historical origin of the effect, and it is a *purely kinematic* relativistic phenomenon — no magnetic field or torque is needed, only the accelerated motion of the spin.

> [!note]- Complete formal solution
> For uniform circular motion, $U_0 = \gamma(1, -v\sin\theta, v\cos\theta, 0)$ with $\theta = \omega_{\mathrm{orbit}}t$ and $d\theta/d\tau = \gamma\omega_{\mathrm{orbit}}$; the four-acceleration $A_0 = dU_0/d\tau$ is centripetal with $\|A_0\| = \gamma^2 v^2/R$. A torque-free spin $S\in U_0^\perp$ obeys $dS/d\tau = -(A_0\cdot S)U_0$ (Fermi–Walker); eliminating the slaved time component $S^0 = \gamma\mathbf v\cdot\mathbf S$, the spatial spin precesses at lab rate $\omega_S = \omega_{\mathrm{orbit}} - (\gamma - 1)\omega_{\mathrm{orbit}}$. After one orbit ($T = 2\pi/\omega_{\mathrm{orbit}}$, $U_0$ returns), the spin has turned $\phi_S = 2\pi - 2\pi(\gamma - 1)$, advancing relative to the orbital frame by $\Delta\phi_{\mathrm{Thomas}} = 2\pi(\gamma - 1)$ — the Thomas precession. The continuous rate is $\Omega_{\mathrm{Thomas}} = (\gamma - 1)\omega_{\mathrm{orbit}}$, with vector form $\boldsymbol\Omega_{\mathrm{Thomas}} = \frac{\gamma^2}{\gamma+1}\mathbf a\times\mathbf v\to\tfrac12\mathbf a\times\mathbf v$ for $v\ll 1$ — the kinematic factor of $\tfrac12$ in atomic spin–orbit coupling. $\blacksquare$

---

# Key Takeaways

**Thomas precession is the holonomy of Fermi–Walker transport around a closed accelerated loop — a purely kinematic rotation with no torque.** The striking result is that a gyroscope carried torque-free around a circle returns *rotated* by $2\pi(\gamma - 1)$ per orbit, even though the Fermi–Walker law is the "non-rotating" transport. There is no contradiction: Fermi–Walker transport keeps the spin non-rotating relative to the *instantaneous* rest frame at each moment, but the instantaneous rest frames around the orbit are related by boosts in continuously changing directions, and the composition of non-collinear boosts is a boost *times a rotation*. Going around the loop accumulates that rotation — it is the holonomy of the transport, the failure of the spin to return to its start. The transferable insight: transport around a closed path in an accelerated motion generically produces a net rotation (a holonomy), and computing it means integrating the transport law around the loop. This is the special-relativistic ancestor of geometric (Berry) phases and of the geodetic precession of gyroscopes in curved spacetime — all are holonomies of a connection around a loop.

**The $(\gamma - 1)$ in the Thomas rate is the relativistic time-dilation mismatch, and the slow limit gives the famous factor of $\tfrac12$.** The Thomas rate $\Omega_{\mathrm{Thomas}} = (\gamma - 1)\omega_{\mathrm{orbit}}$ has a clean interpretation: the spin, transported by proper time, rotates at a rate slightly out of step with the orbital motion, measured in lab time, by exactly the time-dilation factor $\gamma$. In the slow limit $\gamma - 1\approx\tfrac12 v^2$, giving $\boldsymbol\Omega_{\mathrm{Thomas}}\approx\tfrac12\mathbf a\times\mathbf v$ — the factor of $\tfrac12$ that Thomas found in 1926 to fix the electron's spin–orbit coupling and bring atomic fine structure into agreement with experiment. The reusable principle: relativistic precession effects of this kind are controlled by $\gamma - 1$ (or its low-velocity form $\tfrac12 v^2$), and the factor of $\tfrac12$ is the universal kinematic signature of Thomas precession. Whenever a spin or a frame is carried around an accelerated path and a "half" appears unexpectedly in a coupling, suspect Thomas precession.

**This is the kinematic skeleton of spin dynamics — the BMT equation and gyroscope experiments build on it.** The Fermi–Walker transport law for a torque-free spin is the kinematic core; adding the electromagnetic torque turns it into the Bargmann–Michel–Telegdi equation governing how a particle's spin precesses in a field, the basis of the precision $g{-}2$ measurements of the muon and electron magnetic moments. In curved spacetime, the same Fermi–Walker transport along an orbit produces the geodetic and frame-dragging (Lense–Thirring) precessions measured by Gravity Probe B. The diagnostic to carry forward: any time a spinning object is carried along a worldline — a gyroscope, an electron, a satellite-borne sphere — its "non-rotating" evolution is Fermi–Walker transport, and the deviation from a fixed lab orientation is a precession with a kinematic (Thomas) piece plus, if present, torque and curvature pieces. The flat-spacetime Thomas precession computed here is the term that survives even with no field and no gravity, the irreducible relativistic kinematic rotation of an accelerated spin.

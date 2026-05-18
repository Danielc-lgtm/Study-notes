---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Proper Time"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

A clock is carried around a circle of radius $R$ at constant speed $v$, so that it completes one revolution in a coordinate time $T = 2\pi R / v$ as measured in the inertial lab frame. A second, identical clock sits at rest at the centre of the circle.

**(a)** Compute the **proper time** $\Delta\tau$ elapsed on the orbiting clock over one complete revolution, by integrating $d\tau = dt/\gamma$ along its (curved, accelerated) worldline.

**(b)** Compare $\Delta\tau$ with the proper time $\Delta\tau_0$ elapsed on the central clock over the same coordinate interval. Which clock has aged less, and by what factor?

**(c)** The orbiting clock is *not* in an inertial frame — it is continuously accelerated towards the centre. Does that invalidate the calculation? Explain why the result depends only on the *speed* $v$ and not on the centripetal acceleration, and relate the setup to the CERN muon storage-ring measurement of relativistic time dilation.

**Recall:**

![[Def - Proper Time#The Definition]]

A particle moving with speed $u$ in an inertial frame has Lorentz factor $\gamma(u) = (1 - u^2/c^2)^{-1/2} \ge 1$. The proper time along any timelike worldline depends only on the worldline as a geometric curve, not on how it is parametrised; it is the integral $\Delta\tau = \int d\tau = \int dt/\gamma$ of the local time-dilation factor along the path.

---

# Convergent Strategy

**Problem class.** This is a *proper-time-along-a-worldline* problem — the §2.1 ageing problem, of which the twin paradox is the archetype. The target is an elapsed time on an accelerated clock, and the tool is the proper-time integral $\Delta\tau = \int dt/\gamma$.

**Assumption pattern.** The decisive feature is that the speed $v$ is *constant*. Circular motion is accelerated motion, so the worldline is curved and not inertial — but the *magnitude* of the velocity never changes, so $\gamma$ is constant along the entire path. A constant integrand makes the proper-time integral collapse to a multiplication.

**Theorem routing.** The proper time is defined ([[Def - Proper Time|Def - Proper Time]]) as $\Delta\tau = \int dt/\gamma$. Because $\gamma$ is constant, $\Delta\tau = T/\gamma$ immediately, with $T$ the coordinate period. The central clock is inertial with $u = 0$, so $\gamma_0 = 1$ and $\Delta\tau_0 = T$. The ratio is $\Delta\tau/\Delta\tau_0 = 1/\gamma$.

**Key decision point.** The conceptual hurdle is part (c): the worldline is accelerated, so it is tempting to think a special-relativistic calculation is illegitimate or that an acceleration-dependent correction is needed. The resolution is that proper time is a *functional of the worldline*, and at each instant the integrand $\sqrt{1 - u^2/c^2}$ depends only on the instantaneous *speed*, never on the acceleration. Special relativity handles accelerated worldlines perfectly well; what it cannot handle is accelerated *coordinate frames*, and the calculation is done entirely in the inertial lab frame.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Differentiate with respect to proper time, not coordinate time** — the relation $dt/d\tau = \gamma$ is the conversion factor used to integrate $d\tau = dt/\gamma$ along the worldline.
2. **Use a Lorentz invariant to switch frames** — proper time is a Lorentz invariant, so the elapsed $\Delta\tau$ computed in the lab frame is the time the orbiting clock genuinely reads, agreed on by all observers.

---

# Hints

> [!note]- Hint 1
> Proper time along a worldline is $\Delta\tau = \int d\tau = \int dt/\gamma$, where $\gamma$ is evaluated using the *instantaneous speed* at each point of the path. What is special about the speed of a particle in uniform circular motion?

> [!note]- Hint 2
> The speed $v$ is constant — only the *direction* of the velocity rotates. So $\gamma(v)$ is the same at every point of the orbit, and it can be pulled outside the integral $\int dt/\gamma$.

> [!note]- Hint 3
> The central clock has speed zero, so $\gamma_0 = 1$ and its proper time equals the coordinate time. For part (c), ask: does the integrand $\sqrt{1 - u^2/c^2}$ contain the acceleration anywhere, or only the speed?

---

# Solution

The entire problem turns on one observation: in uniform circular motion the *speed* is constant even though the velocity is not, so $\gamma$ is constant along the worldline and the proper-time integral becomes a plain multiplication.

**Step 1: Proper time on the orbiting clock (part a).**

Since the speed $v$ is constant, $\gamma$ is constant along the worldline, and
$$\Delta\tau = \frac{T}{\gamma} = T\sqrt{1 - v^2/c^2} = \frac{2\pi R}{v}\sqrt{1 - v^2/c^2}.$$

> [!note]- Derivation
> By the definition of [[Def - Proper Time|proper time]], the time read by the orbiting clock over one revolution is the integral of the local time-dilation factor along its worldline:
> $$\Delta\tau = \int_0^T \frac{dt}{\gamma\big(u(t)\big)} = \int_0^T \sqrt{1 - \frac{u(t)^2}{c^2}}\;dt,$$
> where $u(t)$ is the instantaneous speed at coordinate time $t$.
>
> In uniform circular motion the position is $\mathbf{x}(t) = R\big(\cos\omega t,\ \sin\omega t,\ 0\big)$ with $\omega = v/R$, so the velocity is $\mathbf{u}(t) = R\omega\big(-\sin\omega t,\ \cos\omega t,\ 0\big)$, and its magnitude is
> $$u(t) = |\mathbf{u}(t)| = R\omega\sqrt{\sin^2\omega t + \cos^2\omega t} = R\omega = v.$$
> The speed is *constant* — the velocity vector merely rotates, its length fixed. Consequently $\gamma\big(u(t)\big) = \gamma(v) = (1-v^2/c^2)^{-1/2}$ is constant, and the integral collapses:
> $$\Delta\tau = \int_0^T \frac{dt}{\gamma(v)} = \frac{T}{\gamma(v)} = T\sqrt{1 - \frac{v^2}{c^2}}.$$
> With the coordinate period $T = 2\pi R/v$,
> $$\boxed{\;\Delta\tau = \frac{2\pi R}{v}\sqrt{1 - \frac{v^2}{c^2}}\;}$$

**Step 2: Comparison with the central clock (part b).**

The central clock is inertial with $\gamma_0 = 1$, so it ages $\Delta\tau_0 = T$; the orbiting clock ages less by exactly the factor $1/\gamma$.

> [!note]- Derivation
> The clock at the centre is at rest in the lab frame, $u = 0$, hence $\gamma_0 = 1$. Its proper time over the coordinate interval $T$ is
> $$\Delta\tau_0 = \int_0^T \frac{dt}{\gamma_0} = \int_0^T dt = T.$$
> The ratio of the two elapsed proper times is therefore
> $$\frac{\Delta\tau}{\Delta\tau_0} = \frac{T/\gamma}{T} = \frac{1}{\gamma} = \sqrt{1 - \frac{v^2}{c^2}} \;\le\; 1.$$
> The orbiting clock ages *less* than the central clock by the factor $1/\gamma$. After one revolution the two clocks are reunited at the same place (the orbiting clock returns to its starting point, a fixed lab location radially out from the centre), so the comparison is unambiguous and frame-independent: this is a genuine twin-paradox scenario, with the orbiting clock playing the travelling twin. The asymmetry between the two clocks is real — one worldline is straight (inertial), the other is curved (accelerated) — and proper time, like Euclidean arc length, depends on the path.

**Step 3: Why the acceleration is irrelevant (part c).**

The proper-time integrand $\sqrt{1 - u^2/c^2}$ depends only on the instantaneous *speed*, never on the acceleration; the calculation is done entirely in the inertial lab frame, so no accelerated coordinate system is ever used.

> [!note]- Derivation
> The orbiting clock is continuously accelerated — it has a centripetal four-acceleration of magnitude set by $v^2/R$ — and one might worry that special relativity, "the theory of inertial frames", cannot be applied. It can, and the reason is a sharp distinction.
>
> Special relativity forbids treating an *accelerated frame* as if it were inertial: an observer riding the clock would need a non-inertial coordinate system, and the naive rules would fail there. But this calculation never enters the clock's frame. Everything is done in the *inertial lab frame*, and in that frame the worldline of the clock — accelerated or not — is just a curve, $\mathbf{x}(t)$. The proper time along any curve is the integral $\int\sqrt{1 - u^2/c^2}\,dt$, and the integrand at each instant contains only the instantaneous *speed* $u(t)$. It does not contain $du/dt$, the acceleration; it does not contain any higher derivative. Proper time is a *functional of the worldline as a geometric object*, and the time-dilation factor is determined pointwise by the velocity's magnitude alone.
>
> This is the **clock hypothesis**: an ideal clock's rate depends only on its instantaneous velocity, not on its acceleration. It is an assumption about what counts as an "ideal clock", and it is the same assumption that underlies the [[Def - Proper Time|proper-time]] integral itself. Under it, the result $\Delta\tau = T/\gamma$ is exact for *any* accelerated motion at constant speed — circular, or otherwise — and depends on $R$ only through $v$ and $T$.
>
> The cleanest experimental confirmation is the **CERN muon storage ring**. Muons are unstable, decaying with a proper lifetime $\tau_\mu \approx 2.2\ \mu\text{s}$ at rest. Stored in a ring and circulating at $v \approx 0.9994\,c$, they are accelerated enormously by the magnetic field that holds them on the circle — an acceleration of order $10^{18}\,g$. Yet their measured laboratory lifetime is dilated by exactly the factor $\gamma \approx 29.3$ predicted by the *speed* alone: the lab sees them survive $\gamma\tau_\mu$ before decaying. The enormous centripetal acceleration produces *no* additional correction, confirming the clock hypothesis to high precision and showing that the constant-speed circular case is the standard, experimentally vindicated warm-up for the general-relativistic proper-time integral, where the same $\int\sqrt{g_{\mu\nu}dx^\mu dx^\nu}$ is evaluated along worldlines in a curved metric.

> [!note]- Complete formal solution
> **(a)** For uniform circular motion $\mathbf{x}(t) = R(\cos\omega t, \sin\omega t, 0)$ with $\omega = v/R$, the velocity $\mathbf{u}(t) = R\omega(-\sin\omega t, \cos\omega t, 0)$ has constant magnitude $u(t) = R\omega = v$. Hence $\gamma$ is constant and
> $$\Delta\tau = \int_0^T \frac{dt}{\gamma} = \frac{T}{\gamma} = T\sqrt{1 - v^2/c^2} = \frac{2\pi R}{v}\sqrt{1 - v^2/c^2}.$$
> **(b)** The central clock has $u = 0$, $\gamma_0 = 1$, so $\Delta\tau_0 = T$. Therefore $\Delta\tau/\Delta\tau_0 = 1/\gamma = \sqrt{1 - v^2/c^2} \le 1$: the orbiting clock ages less, by the factor $1/\gamma$.
> **(c)** The proper-time integrand $\sqrt{1 - u^2/c^2}$ depends only on the instantaneous speed, not on the acceleration (the clock hypothesis), and the whole computation is performed in the inertial lab frame, never in the clock's accelerated frame. The result is therefore exact and independent of the centripetal acceleration. The CERN muon storage ring confirms this: muons at $v \approx 0.9994\,c$ on a circular orbit show time dilation by the $\gamma$ set by their speed alone, despite an acceleration of order $10^{18}\,g$. $\blacksquare$

---

# Key Takeaways

**Constant speed makes the proper-time integral collapse — recognise it instantly.** The general proper-time formula $\Delta\tau = \int\sqrt{1 - u^2/c^2}\,dt$ is an integral, and integrals are work. But the integrand depends only on the *speed* $u$, so whenever the speed is constant — uniform circular motion, a particle on any closed orbit at fixed $|\mathbf{u}|$, a constant-velocity straight worldline — the integral degenerates to a multiplication, $\Delta\tau = T/\gamma$. The trigger to look for is the phrase "constant speed" or "uniform circular motion": the moment you see it, $\gamma$ comes out of the integral and the problem is essentially done. This is the same simplification that makes the inertial twin's worldline trivial in the twin paradox, and it is worth contrasting with [[Ex - Proper time along an accelerated worldline|the genuinely accelerated worldline]], where the speed changes and the integral must actually be performed.

**Proper time is a functional of the worldline, and depends only on speed — not on acceleration.** The single most important conceptual point is that proper time is a property of the *curve* a clock traces through spacetime, exactly as arc length is a property of a curve in space, and the integrand is fixed pointwise by the instantaneous velocity's *magnitude*. Acceleration does not appear. This is what licenses the use of special relativity for accelerated motion: SR cannot treat an accelerated *frame* as inertial, but it computes the proper time along an accelerated *worldline* with no difficulty, provided the computation is carried out in an inertial frame. The "clock hypothesis" — that an ideal clock's rate depends only on its speed — is the precise statement, and it is what makes the orbiting clock, despite its colossal centripetal acceleration, dilate by the $\gamma$ of its speed alone. Whenever a problem worries you with the word "accelerated", remember: stay in an inertial frame, integrate $\sqrt{1-u^2/c^2}\,dt$, and the acceleration takes care of itself.

**The circular clock is the standard warm-up for the curved-spacetime proper-time integral.** This exercise is pure special relativity, but its structure is exactly that of the general-relativistic proper-time computation: a worldline through spacetime, and a proper time $\int\sqrt{g_{\mu\nu}\,dx^\mu dx^\nu}$ read off along it. In flat space the metric is $\eta$ and the integrand reduces to $\sqrt{1 - u^2/c^2}\,dt$; in a curved spacetime the same integral, with a position-dependent $g_{\mu\nu}$, gives the ageing of a clock in a gravitational field, and extremising it yields the geodesic equation. The CERN muon storage ring is the experiment that anchors this whole chain: it confirms that a clock circulating at $0.9994\,c$ ages by the factor set by its speed, the acceleration contributing nothing — the empirical foundation for trusting the proper-time integral, in both special and general relativity, as the true elapsed time on any worldline.

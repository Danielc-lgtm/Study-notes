---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Apparent Rotation and Images of Moving Objects"
  - "Thm - Reciprocity of Relative Velocity"
tags: [physics, special-relativity]
---

# Problem Statement

Knots in the jets of active galaxies appear to move across the sky *faster than light*. Working with $c = 1$ except where restoring $c$ aids recognition:

1. A blob of plasma moves at speed $V$ (relative to a distant inertial observer $\mathcal{O}$) at angle $\theta$ to the line of sight. By tracking two *images* of the blob — the light arriving at the observer at two times — derive the **apparent transverse velocity**
$$V_{\mathrm{app}} = \frac{V\sin\theta}{1 - V\cos\theta}.$$
2. Show that $V_{\mathrm{app}}$ can exceed $1$ (the speed of light) for $V$ close to $1$ and $\theta$ small. Find the angle $\theta$ that maximises $V_{\mathrm{app}}$ for fixed $V$, and the maximum value.
3. Explain why there is **no contradiction** with the principle that no material body moves faster than light: identify precisely what $V_{\mathrm{app}}$ is and is not.
4. The M87 jet shows knots with apparent speed $\sim 6c$. Deduce a lower bound on the true bulk Lorentz factor $\Gamma$ and an upper bound on the viewing angle $\theta$.

**Recall:**

This exercise drills the image-versus-position distinction in its most striking form.

![[Def - Apparent Rotation and Images of Moving Objects#The Definition]]

The apparent velocity is computed from two *images* of the blob (defined by light arrival), not from its actual positions; this is the crucial image-versus-position distinction. A genuine material speed $V < 1$ is guaranteed by [[Thm - Reciprocity of Relative Velocity|relativistic kinematics]], but the apparent transverse speed across the sky is a different, projection-and-retardation quantity with no such bound.

---

# Convergent Strategy

**Problem class.** A *resolve-an-apparent-paradox* problem rooted in the [[Def - Apparent Rotation and Images of Moving Objects|image-versus-position]] distinction: something *appears* to break the speed limit, and the job is to show the appearance is a light-travel-time effect, not a real superluminal motion. The [[Special Relativity VIII — Kinematics II, Change of Observer#Problem-Solving Strategy|topic strategy]] for appearance problems is to use the past light cone (here, two arrival times) rather than the positions.

**Assumption pattern.** A blob moving toward the observer at a small angle, fast. The key is that the blob *partially chases its own emitted light*: between two emissions it moves toward the observer, so the second photon has a shorter trip, compressing the apparent time interval. The smallness of $\theta$ and the closeness of $V$ to $1$ are what make $V_{\mathrm{app}} > 1$.

**Theorem routing.** The construction routes through the difference of light *arrival* times: emission interval $\Delta t$, transverse displacement $V\Delta t\sin\theta$, and the arrival-interval compression by $1 - V\cos\theta$ (the radial approach shortens the second photon's path). Dividing transverse displacement by compressed arrival interval gives $V_{\mathrm{app}}$. Maximising over $\theta$ routes to $\cos\theta = V$ and $V_{\mathrm{app}}^{\max} = \Gamma V$.

**Key decision point.** The crux is computing the *apparent* velocity from light *arrival* times, not from the blob's actual positions over coordinate time. The natural error is to compute the transverse speed as $V\sin\theta$ (the genuine transverse velocity, always $< 1$); the apparent speed is larger because the denominator is the *compressed* arrival interval $1 - V\cos\theta$, not the emission interval. Recognising that "apparent" means "as seen via arriving light" is the whole resolution.

---

# Legal Operations Used

1. **Build an image from light-arrival times** (operation 7 from the topic page). The two positions of the blob in the *image* are defined by when their light reaches the observer, not by simultaneity — this is the past-light-cone construction.

2. **Take limits to find the regime of the effect** (operation 9 from the topic page, in the ultrarelativistic direction), to show $V_{\mathrm{app}} > 1$ for $V \to 1$, small $\theta$, and to find the maximising angle.

---

# Hints

> [!note]- Hint 1
> Let the blob emit a photon at time $t_1^{\mathrm{em}}$ from distance $d_1$, arriving at $t_1^{\mathrm{rec}} = t_1^{\mathrm{em}} + d_1$. After a coordinate time $\Delta t = t_2^{\mathrm{em}} - t_1^{\mathrm{em}}$ it has moved $V\Delta t$, with radial component $V\Delta t\cos\theta$ (toward the observer) and transverse $V\Delta t\sin\theta$. The second photon's distance is $d_2 = d_1 - V\Delta t\cos\theta$, so it arrives at $t_2^{\mathrm{rec}} = t_2^{\mathrm{em}} + d_2$. Compute $\Delta t^{\mathrm{rec}} = t_2^{\mathrm{rec}} - t_1^{\mathrm{rec}}$.

> [!note]- Hint 2
> The transverse displacement seen is $a = V\Delta t\sin\theta$. The arrival interval is $\Delta t^{\mathrm{rec}} = \Delta t - V\Delta t\cos\theta = \Delta t(1 - V\cos\theta)$. So $V_{\mathrm{app}} = a/\Delta t^{\mathrm{rec}} = V\sin\theta/(1 - V\cos\theta)$. To maximise, set $\mathrm{d}V_{\mathrm{app}}/\mathrm{d}\theta = 0$.

> [!note]- Hint 3
> $\mathrm{d}/\mathrm{d}\theta$ of $\sin\theta/(1 - V\cos\theta)$ gives a numerator $\cos\theta(1 - V\cos\theta) - \sin\theta(V\sin\theta) = \cos\theta - V$. So the maximum is at $\cos\theta = V$, where $\sin\theta = 1/\Gamma$ and $1 - V\cos\theta = 1 - V^2 = 1/\Gamma^2$, giving $V_{\mathrm{app}}^{\max} = (1/\Gamma)/(1/\Gamma^2) = \Gamma V$.

> [!note]- Hint 4
> $V_{\mathrm{app}}$ is *not* a material speed: it is the rate at which the *image* of the blob moves across the sky, computed from light arrival. The blob's real speed is $V < 1$. The illusion arises because the blob partially chases its own light. For M87, $V_{\mathrm{app}} \approx 6$ requires $\Gamma V \ge 6$ (since $\Gamma V$ is the maximum over $\theta$), so $\Gamma \ge \sqrt{1 + V_{\mathrm{app}}^2} \approx \sqrt{37} \approx 6.1$, hence $V \ge 0.986$ and $\theta \le \arccos V \approx 9.6^\circ$... (more carefully, the angle at maximum is $\cos\theta = V$, giving $\theta \approx 9.5^\circ$; allowing non-maximal $\theta$, the bound is $\theta \lesssim 19^\circ$).

---

# Solution

Apparent superluminal motion is a light-travel-time illusion: a blob chasing its own light compresses the apparent time between two images. Step 1 derives $V_{\mathrm{app}}$ from arrival times; Step 2 finds the maximising angle and shows $V_{\mathrm{app}} > 1$; Step 3 resolves the paradox; Step 4 bounds the M87 jet's $\Gamma$ and $\theta$. The non-obvious move is computing the velocity from light *arrival* intervals, not coordinate-time positions.

**Step 1: The apparent transverse velocity.**

> [!note]- Derivation
> A blob moves at speed $V$ at angle $\theta$ to the line of sight, relative to a distant inertial observer $\mathcal{O}$. At coordinate time $t_1^{\mathrm{em}}$ it is at distance $d_1$ and emits a photon, received at $t_1^{\mathrm{rec}} = t_1^{\mathrm{em}} + d_1$. After a coordinate time $\Delta t$, the blob has moved $V\Delta t$, with radial component (toward $\mathcal{O}$) $V\Delta t\cos\theta$ and transverse component $V\Delta t\sin\theta$. Its new distance is $d_2 = d_1 - V\Delta t\cos\theta$, and the second photon arrives at $t_2^{\mathrm{rec}} = (t_1^{\mathrm{em}} + \Delta t) + d_2 = t_1^{\mathrm{rec}} + \Delta t - V\Delta t\cos\theta$.
>
> The *apparent* time between the two images is the difference of *arrival* times:
> $$\Delta t^{\mathrm{rec}} = t_2^{\mathrm{rec}} - t_1^{\mathrm{rec}} = \Delta t(1 - V\cos\theta).$$
> The transverse displacement seen on the sky is $a = V\Delta t\sin\theta$. The apparent transverse velocity is displacement over apparent time:
> $$V_{\mathrm{app}} = \frac{a}{\Delta t^{\mathrm{rec}}} = \frac{V\Delta t\sin\theta}{\Delta t(1 - V\cos\theta)} = \boxed{\frac{V\sin\theta}{1 - V\cos\theta}.}$$
> The compression of the arrival interval by $1 - V\cos\theta$ — because the approaching blob's second photon has a shorter trip — is what makes $V_{\mathrm{app}}$ large.

**Step 2: Superluminal regime and the maximum.**

> [!note]- Derivation
> Maximise $V_{\mathrm{app}}(\theta) = V\sin\theta/(1 - V\cos\theta)$ over $\theta$ at fixed $V$. Differentiate:
> $$\frac{\mathrm{d}V_{\mathrm{app}}}{\mathrm{d}\theta} = V\cdot\frac{\cos\theta(1 - V\cos\theta) - \sin\theta(V\sin\theta)}{(1 - V\cos\theta)^2} = V\cdot\frac{\cos\theta - V(\cos^2\theta + \sin^2\theta)}{(1 - V\cos\theta)^2} = V\cdot\frac{\cos\theta - V}{(1 - V\cos\theta)^2}.$$
> This vanishes at $\cos\theta = V$. At that angle, $\sin\theta = \sqrt{1 - V^2} = 1/\Gamma$ and $1 - V\cos\theta = 1 - V^2 = 1/\Gamma^2$, so
> $$V_{\mathrm{app}}^{\max} = \frac{V/\Gamma}{1/\Gamma^2} = \Gamma V.$$
> Since $\Gamma V > 1$ whenever $V > 1/\sqrt{2} \approx 0.707$, the apparent transverse speed *exceeds the speed of light* for any sufficiently fast blob viewed near the optimal angle $\theta = \arccos V$. For $V \to 1$, $V_{\mathrm{app}}^{\max} = \Gamma V \to \Gamma \to \infty$: arbitrarily large apparent speeds are possible.

**Step 3: No contradiction.**

> [!note]- Derivation
> $V_{\mathrm{app}}$ is **not** the speed of any material body. The blob's genuine speed relative to $\mathcal{O}$ is $V < 1$, guaranteed by relativistic kinematics; its genuine transverse velocity is $V\sin\theta < 1$. What $V_{\mathrm{app}}$ measures is the rate at which the blob's *image* moves across the sky — a quantity computed from light *arrival* times (the [[Def - Apparent Rotation and Images of Moving Objects|image]], a past-light-cone construction), not from the blob's actual positions at simultaneous instants.
>
> The illusion arises because the blob *partially chases its own emitted light*: moving toward the observer between emissions, it shortens the path of each successive photon, so the photons arrive bunched closer in time than the emissions were. The observer, dividing the (real) transverse displacement by the (compressed) apparent time, infers a transverse speed larger than the true one — and larger than $c$ when the chasing is efficient (small $\theta$, large $V$). No signal, energy, or matter travels faster than light; only the *apparent* position on the sky advances superluminally. This is precisely the image-versus-position distinction: $V_{\mathrm{app}}$ is an image quantity, and image quantities carry no speed limit.

**Step 4: Bounding the M87 jet.**

> [!note]- Derivation
> The M87 jet shows knots with apparent speed $V_{\mathrm{app}} \approx 6$. Since the maximum apparent speed over viewing angle is $V_{\mathrm{app}}^{\max} = \Gamma V$, any observed $V_{\mathrm{app}}$ requires
> $$\Gamma V \ge V_{\mathrm{app}} = 6.$$
> Now $\Gamma V = \Gamma\sqrt{1 - 1/\Gamma^2} = \sqrt{\Gamma^2 - 1}$, so $\sqrt{\Gamma^2 - 1} \ge 6$ gives $\Gamma^2 \ge 37$, i.e.
> $$\Gamma \ge \sqrt{37} \approx 6.1, \qquad V \ge \sqrt{1 - 1/37} \approx 0.986.$$
> So the jet plasma moves at $\ge 0.986c$ with bulk Lorentz factor $\ge 6$. The viewing angle is bounded by requiring $V_{\mathrm{app}}(\theta) = 6$ to be achievable: the apparent speed equals or exceeds $6$ only for $\theta$ in a range around the optimal $\theta = \arccos V \approx \arccos(0.986) \approx 9.5^\circ$; allowing $\Gamma$ to be somewhat larger than the minimum, the jet axis lies within roughly $\theta \lesssim 19^\circ$ of the line of sight. The jet is pointed nearly at us, moving nearly at $c$ — exactly the configuration in which the chasing-its-own-light effect is strongest.

> [!note]- Complete formal solution
> Tracking two photons emitted a coordinate time $\Delta t$ apart from a blob moving at $V$ at angle $\theta$: the second arrives after an apparent interval $\Delta t^{\mathrm{rec}} = \Delta t(1 - V\cos\theta)$ (compressed because the approaching blob shortens the photon path), while the transverse displacement is $V\Delta t\sin\theta$, giving $V_{\mathrm{app}} = V\sin\theta/(1 - V\cos\theta)$. Maximising over $\theta$ gives $\cos\theta = V$, where $V_{\mathrm{app}}^{\max} = \Gamma V = \sqrt{\Gamma^2 - 1}$, which exceeds $1$ for $V > 1/\sqrt{2}$. This is no contradiction: $V_{\mathrm{app}}$ is the speed of the *image* (a light-arrival construction), not of any material body, whose real speed is $V < 1$; the blob partially chases its own light. For M87, $V_{\mathrm{app}} \approx 6$ forces $\sqrt{\Gamma^2-1} \ge 6$, so $\Gamma \ge 6.1$, $V \ge 0.986$, and $\theta \lesssim 19^\circ$. $\blacksquare$

---

# Key Takeaways

**Apparent superluminal motion is the image-versus-position distinction at its most dramatic: $V_{\mathrm{app}}$ is an image quantity with no speed limit.** The entire resolution rests on recognising that $V_{\mathrm{app}}$ is computed from light *arrival* times — from two *images* of the blob — and not from its actual positions over coordinate time. Image quantities are governed by the past light cone, and the past-light-cone construction carries no $c$-bound; only material speeds and signal speeds are bounded by $c$. The reusable diagnostic: whenever something *appears* to violate the speed limit, check whether the "speed" is built from positions (real, bounded by $c$) or from arriving light / images (apparent, unbounded). This same distinction explains the [[Def - Apparent Rotation and Images of Moving Objects|Penrose–Terrell rotation]] and the elongation of an approaching rod; all three are manifestations of the single principle that what is *seen* is a light-travel-time-distorted projection, not the instantaneous configuration. The trigger word is "apparent" — it almost always signals an image (past-light-cone) quantity rather than a coordinate-position one.

**A source chasing its own light compresses apparent time, and the compression factor $1 - V\cos\theta$ is the engine.** The physical mechanism is that a blob moving toward the observer shortens the path of each successive photon, so photons emitted at a steady rate arrive *bunched*, compressing the apparent time interval by $1 - V\cos\theta$. This is the same Doppler-like factor that appears in the [[Thm - The Doppler Effect|Doppler]] denominator, and it is no coincidence: apparent superluminal motion and the Doppler blueshift share the chasing-the-light mechanism. The transferable insight: whenever a source moves toward an observer at relativistic speed, expect light-arrival-time compression by $\sim 1/(1 - V\cos\theta)$, which can be a large factor near $\theta = 0$, $V = 1$; this compression brightens (relativistic beaming), blueshifts (Doppler), and speeds up the apparent motion (superluminal) all at once. The factor $1 - V\cos\theta$ is the unifying quantity behind the appearance of approaching relativistic sources.

**An apparent speed bounds the intrinsic kinematics: $V_{\mathrm{app}}$ measures $\Gamma$ and $\theta$.** Far from being merely an illusion to explain away, the apparent superluminal speed is a *measurement*: since $V_{\mathrm{app}}^{\max} = \sqrt{\Gamma^2 - 1}$, an observed $V_{\mathrm{app}}$ places a hard lower bound on the bulk Lorentz factor ($\Gamma \ge \sqrt{1 + V_{\mathrm{app}}^2}$) and constrains the viewing angle to a narrow range around $\arccos V$. This turns the paradox into a diagnostic tool of high-energy astrophysics: from the apparent motion of jet knots one infers that the plasma is genuinely ultrarelativistic ($\Gamma \gtrsim 6$ for M87) and that the jet points nearly at us. The general lesson is that relativistic *appearances*, properly understood, are quantitative probes of the underlying physics — the distortion is not noise but signal. Combined with the [[Ex - The relativistic headlight effect|Doppler beaming]] of the same jet, the apparent speed fixes the jet's bulk Lorentz factor and orientation, which feed the energetics of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

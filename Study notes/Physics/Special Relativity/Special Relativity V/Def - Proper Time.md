---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Spacetime Interval"
  - "Def - Minkowski Space and the Metric"
  - "Def - Worldline of a Particle"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector has $X \cdot X > 0$ and the infinitesimal interval along a timelike step is $ds^2 = \eta_{\mu\nu}\,dx^\mu dx^\nu = dt^2 - d\mathbf{x}^2 > 0$. A worldline is $\mathcal{L}$, its tangent field $V(\lambda) = dX/d\lambda$. Proper time is $\tau$; coordinate time in an inertial frame is $t$; a particle's speed in that frame is $u = |\mathbf{u}|$ with $\gamma = (1 - u^2)^{-1/2}$. Events on $\mathcal{L}$ are $A, B$. Full registry on [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]].

> [!warning] Convention
> With $c$ restored, the proper time is $d\tau = c^{-1}\sqrt{c^2 dt^2 - d\mathbf{x}^2} = \sqrt{ds^2}/c$, so that $d\tau$ has the dimension of time. Gourgoulhon (whose Chapter 2 this follows) uses the **mostly-plus** signature, in which the timelike interval is $-g(d\vec{x}, d\vec{x}) > 0$ and he writes $c\,d\tau = \sqrt{-g(d\vec{x}, d\vec{x})}$. We have flipped the metric sign, so for us $c\,d\tau = \sqrt{+g(d\vec{x}, d\vec{x})} = \sqrt{ds^2}$, with the square root taken of the *positive* quantity $ds^2 = dt^2 - d\mathbf{x}^2$. Every "$\sqrt{-g}$" in the source becomes "$\sqrt{+ds^2}$" here.

---

# Axiom Motivation

By the end of [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group|the kinematic groundwork]] we know the unsettling news: the elapsed time $\Delta t$ between two events and the spatial distance between them are each frame-dependent, and there is no universal clock. Yet a [[Def - Worldline of a Particle|worldline]] is a genuine, observer-independent curve in $\mathbb{M}$, and a real clock carried along it ticks a definite number of times between any two events on it. That tick count is a physical fact, the same for everyone who looks at the clock. The question is: what frame-independent quantity does the clock measure?

The answer is forced by a single observation. Consider the clock in *its own* momentary rest frame. There it sits still, so between two infinitesimally close ticks the spatial displacement vanishes, $d\mathbf{x} = 0$, and the only separation is in time: $ds^2 = dt^2$. The elapsed time the clock reads is therefore $\sqrt{ds^2}$. But $ds^2$ is the [[Def - The Spacetime Interval|spacetime interval]], and the interval is [[Thm - Invariance of the Spacetime Interval|Lorentz invariant]] — every frame computes the same value of $\sqrt{ds^2}$, even though only the rest frame sees it as pure time. So the quantity "interval along the worldline" is at once (i) frame-independent and (ii) equal, in the rest frame, to the clock's reading. It is the unique candidate for "the time the clock measures", and we name it the **proper time** $\tau$.

This single requirement — that proper time reduce to coordinate time in the rest frame and be Lorentz invariant — pins the definition down completely; there is no nearby variant that survives. Suppose one tried, instead, to call the clock's reading the *coordinate* time $t$ of some fixed inertial frame. That fails because $t$ is frame-dependent: two observers would assign two different "clock readings" to the same pair of ticks, contradicting the fact that the clock displays one number. Suppose one tried to use the spatial arc length $\int |d\mathbf{x}|$ travelled. That fails because it is zero in the rest frame, where the clock is plainly still ticking. Only the metric interval $\int \sqrt{ds^2}$ does both jobs. Notice the role the **indefiniteness** of the metric plays: on a Euclidean space the analogous arc length would be $\int\sqrt{dt^2 + d\mathbf{x}^2}$ and a moving clock would read *more*, not less; it is the minus sign in $ds^2 = dt^2 - d\mathbf{x}^2$ that makes spatial motion *subtract* from the elapsed time, producing time dilation.

There is a further, subtler design decision hidden in "$\int \sqrt{ds^2}$ along the worldline": the integral is taken along the *actual* curve, and so its value **depends on the curve**, not merely on its endpoints. Two worldlines joining the same two events generically accumulate different proper times. A sceptic might call this a mere artefact of an arbitrary definition of "time". It is not, and the reason is physical: the laws of dynamics, written in terms of proper time, take their simplest form (the equations of motion involve the metric, to which proper time is directly tied), and atomic clocks flown on different worldlines *do* read different elapsed times when reunited (the [[Ex - The Hafele-Keating experiment|Hafele–Keating]] and Alley experiments). Proper time is the *physical* time, not a bookkeeping convenience, and its path-dependence is the precise statement that relativity has abolished absolute time and replaced it by a privileged time *per worldline*.

Finally, the requirement that the integrand be a **metric** quantity — built from $\eta$ — is what makes the construction the seed of gravitation. The metric tensor is being used here as "the operator that gives the elapsed time along a trajectory". The moment one allows the metric to vary from event to event, $\eta_{\mu\nu} \to g_{\mu\nu}(x)$, the very same integral $\int\sqrt{g_{\mu\nu}\,dx^\mu dx^\nu}$ becomes the proper time of general relativity, and "the worldline that extremises it" becomes a geodesic of curved spacetime.

---

# The Definition

Let $\mathcal{L}$ be a [[Def - Worldline of a Particle|timelike worldline]] and let $A, B$ be two events on it. The **proper time** elapsed between $A$ and $B$ along $\mathcal{L}$ is the metric arc length of the worldline,
$$
\tau(A, B) \;:=\; \int_A^B d\tau \;=\; \int_A^B \sqrt{ds^2} \;=\; \int_A^B \sqrt{dt^2 - d\mathbf{x}^2}
\qquad (c = 1),
$$
where the integral is taken along $\mathcal{L}$. In terms of any future-directed parametrisation $\varphi(\lambda)$ of $\mathcal{L}$, with tangent field $V(\lambda) = d\vec{x}/d\lambda$,
$$
\tau(A, B) \;=\; \int_{\lambda_1}^{\lambda_2} \sqrt{V(\lambda) \cdot V(\lambda)}\;\, d\lambda,
\qquad A = \varphi(\lambda_1),\; B = \varphi(\lambda_2),
$$
and the integrand $\sqrt{V \cdot V}$ is real because $V$ is timelike, $V \cdot V > 0$. The value of $\tau(A,B)$ is **independent of the parametrisation** $\varphi$ (a change of parameter rescales $V$ and $d\lambda$ reciprocally) but **depends on the worldline** $\mathcal{L}$ joining $A$ to $B$.

The **infinitesimal proper time** along $\mathcal{L}$ is
$$
d\tau \;=\; \sqrt{ds^2} \;=\; \sqrt{dt^2 - d\mathbf{x}^2} \;=\; dt\sqrt{1 - u^2} \;=\; \frac{dt}{\gamma},
$$
the last forms holding in an inertial frame where the particle has speed $u$ and $\gamma = (1 - u^2)^{-1/2}$. Equivalently $dt/d\tau = \gamma$. The total time read by a clock travelling along $\mathcal{L}$ is therefore
$$
T \;=\; \int d\tau \;=\; \int \frac{dt}{\gamma},
$$
which is **less** than the coordinate time $\int dt$ whenever the particle moves ($\gamma > 1$) — this is time dilation, now seen as a statement about arc length.

Proper time is defined only along **timelike** worldlines. Along a [[Def - Photons and Null Geodesics|null worldline]] (a photon's history) one has $ds^2 = 0$, so $d\tau = 0$ identically: proper time does not advance, and the construction does not apply.

---

# Categorical / Structural Definition

Proper time is the **arc-length functional of the pseudo-Riemannian metric**, restricted to the timelike curves on which it is real-valued. On any (pseudo-)Riemannian manifold $(M, g)$ the metric assigns to a curve $\gamma : [\lambda_1, \lambda_2] \to M$ the length $L[\gamma] = \int \sqrt{|g(\dot\gamma, \dot\gamma)|}\, d\lambda$; proper time is this functional with the absolute value dropped (the timelike sign is positive in mostly-minus) and a factor of $c^{-1}$ to give units of time. Two features of the functional are structural, not incidental:

It is a **reparametrisation invariant**: $L[\gamma \circ f] = L[\gamma]$ for any $C^1$ orientation-preserving reparametrisation $f$, because $\sqrt{g(\dot\gamma, \dot\gamma)}\, d\lambda$ is a $1$-form on the curve (it transforms as the differential it is). This is exactly why $\tau(A,B)$ depends on the geometric curve $\mathcal{L}$ but not on how it is parametrised, and it is what allows proper time *itself* to be used as the distinguished parameter ($\lambda = \tau$ makes the tangent a unit vector, the [[Def - Four-Velocity and Four-Acceleration|four-velocity]]).

It is the **action** of the free relativistic particle, up to the constant $-m$ (with $m$ the [[Def - Four-Momentum and Rest Mass|rest mass]]): the dynamics "$S = -m\int d\tau$, extremise" has as its extremals the unparametrised-length critical curves, which in flat space are the straight timelike lines ([[Thm - Inertial Worldlines Maximise Proper Time]]). This is the cleanest entry to the [[Special Relativity XV — The Principle of Least Action|variational formulation]] of relativistic mechanics, and it generalises to the curved case verbatim: a freely-falling particle in $(M, g)$ extremises $\int\sqrt{g_{\mu\nu}\dot x^\mu \dot x^\nu}\, d\lambda$, the geodesic principle of gravitation.

---

# Relate to Other Fields / Compression

Proper time is the Lorentzian analogue of **arc length** in Riemannian geometry, with one sign and one sign of attitude flipped: where Euclidean arc length is minimised by straight lines, the indefinite metric makes the timelike arc length (proper time) *maximised* by straight worldlines. The whole of [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames|the kinematics that follows]], and of relativistic dynamics, is "do Newtonian mechanics, but differentiate with respect to proper time instead of coordinate time" — the substitution that converts frame-dependent triples of numbers into genuine four-vectors.

**True name:** proper time is *the metric arc length of a timelike worldline* — the same number for every observer, the time a comoving clock reads, and the privileged parameter that turns kinematic quantities into four-vectors. The operational consequence is a reflex: whenever a problem asks "how much time passes for the particle / traveller / clock / muon", the answer is $\int d\tau = \int dt/\gamma$ along its worldline, and *never* the coordinate time of some bystander's frame.

In information-geometric and statistical-mechanical settings the same arc-length-of-a-metric construction recurs (a path's "length" in a Fisher or thermodynamic metric), but the load-bearing physical fact unique to relativity is the *indefiniteness*, which flips the extremum and creates the causal trichotomy. In the calculus of variations proper time is a length functional whose Euler–Lagrange equation is the geodesic equation; in the theory of clocks (next section) it is what an **ideal clock** is *defined* to display.

---

# Examples / Corollaries

**Is an instance — an inertial clock.** A clock at rest in an inertial frame has worldline $x^\mu(\lambda) = (\lambda, \mathbf{0})$; here $d\mathbf{x} = 0$, so $d\tau = dt$ and $\tau(A,B) = \Delta t$. The proper time of a clock at rest equals the coordinate time of its own frame — the calibration case from which everything else is a dilation.

**Is an instance — a uniformly moving clock.** A clock moving at constant speed $u$ between two events separated (in the lab) by $(\Delta t, \Delta \mathbf{x})$ with $|\Delta\mathbf{x}| = u\,\Delta t$ accumulates $\tau = \sqrt{\Delta t^2 - u^2\Delta t^2} = \Delta t\sqrt{1 - u^2} = \Delta t/\gamma < \Delta t$. This is the time-dilation formula, read off as the length of the straight timelike segment.

**Is an instance — the travelling twin.** The [[Ex - The twin paradox|Langevin traveller]] who goes out at speed $v$ and returns reads $\tau = 2T/\gamma$, while the stay-at-home twin reads $2T$; the difference is purely that the two worldlines between the same events $A$ and $B$ have different arc lengths. The bent worldline is shorter in proper time than the straight one.

**Is NOT an instance — a photon's history.** Along the null line $x^\mu(\lambda) = \lambda(1,1,0,0)$ one has $ds^2 = d\lambda^2 - d\lambda^2 = 0$, so $\tau = 0$ identically. A photon accumulates no proper time; a clock "carried by light" would be frozen. Proper time is undefined for null worldlines, which is why photons are parametrised by an [[Def - Photons and Null Geodesics|affine parameter]] instead.

**Is NOT an instance — the spatial path length.** The quantity $\int |d\mathbf{x}|$ (how far the particle travels in space) is *not* proper time: it is frame-dependent and vanishes in the rest frame, where proper time is maximal. Confusing the two is the most common conceptual slip; proper time involves the *difference* $dt^2 - d\mathbf{x}^2$, not either piece alone.

**Corollary — proper time is bounded above by coordinate time.** Since $d\tau = dt\sqrt{1 - u^2} \le dt$ for any $u$ in any inertial frame, $\tau(A,B) \le t(B) - t(A)$ along any worldline, with equality iff the particle is at rest in that frame. The supremum over worldlines joining two fixed timelike-separated events is attained by the straight (inertial) one — the content of [[Thm - Inertial Worldlines Maximise Proper Time]].

**Corollary — the lower bound is zero.** By bending the worldline ever closer to a sequence of null segments (a light ray out and back), the proper time between two fixed events can be made arbitrarily small. There is no positive lower bound; the infimum $0$ is approached but not attained by any timelike worldline.

**Calibration check.** You have understood proper time if you can: (i) compute $\tau$ for the straight worldline between $(0,\mathbf{0})$ and $(\Delta t, u\Delta t, 0, 0)$ and recover $\Delta t/\gamma$; (ii) explain why a photon has $\tau = 0$ while a slow massive particle has $\tau \approx \Delta t$; and (iii) state, without computing, which of two worldlines between the same events has the larger proper time — the straighter one.

---

# Unlocked by This

> [!tip] Four-Velocity and Four-Acceleration *(from this chapter)*
> Because proper time is a Lorentz scalar, differentiating the four-position with respect to it yields genuine four-vectors: the **four-velocity** $U = dX/d\tau$, normalised $U \cdot U = 1$, and the **four-acceleration** $A = dU/d\tau$, orthogonal to $U$ ([[Def - Four-Velocity and Four-Acceleration]]). Differentiating with respect to coordinate time $t$ instead would *not* produce four-vectors, because $t$ is frame-dependent — the whole reason proper time is introduced.

> [!tip] The Relativistic Action and Four-Momentum *(from the Principle of Least Action)*
> The free particle extremises $S = -m\int d\tau$, the proper time along its worldline weighted by minus its [[Def - Four-Momentum and Rest Mass|rest mass]]. The conjugate momentum of this action is exactly the **four-momentum** $P_\mu$, and the Euler–Lagrange equations say the worldline is straight, $dU/d\tau = 0$ — see [[Special Relativity XV — The Principle of Least Action]]. Because the metric is indefinite, the extremum is a **maximum** of proper time, not a minimum.

> [!tip] The Geodesic Principle of Gravitation *(from General Relativity)*
> This is the deepest thing the page seeds, and it is worth stating in full. The metric tensor has been used here as the operator that converts a worldline into an elapsed time, $\tau = \int\sqrt{\eta_{\mu\nu}\,dx^\mu dx^\nu}$. In special relativity $\eta_{\mu\nu}$ is a fixed, constant background; the only freedom is in the worldline. **General relativity** promotes the metric to a position-dependent dynamical field $g_{\mu\nu}(x)$ and keeps the proper-time integral unchanged in form, $\tau = \int\sqrt{g_{\mu\nu}\,dx^\mu dx^\nu}$. Two consequences follow immediately. First, the *clocks-and-rods* content survives intact: an ideal clock still reads the arc length of its worldline, now in the curved metric, which is why gravitational time dilation is computed by exactly this integral with $g_{00}(x)$ in place of $1$. Second, and more structurally, the variational principle survives: a freely-falling particle extremises $\int d\tau$, and the resulting extremal is a **timelike geodesic** of $g$, obeying the geodesic equation $\dfrac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu{}_{\nu\rho}\dfrac{dx^\nu}{d\tau}\dfrac{dx^\rho}{d\tau} = 0$, with the **Christoffel symbols** $\Gamma$ built from first derivatives of $g_{\mu\nu}$. In flat space, in inertial coordinates, $\Gamma = 0$ and this reduces to the straight worldline of [[Thm - Inertial Worldlines Maximise Proper Time]]. So the single sentence "proper time is the metric arc length of a timelike worldline, and free particles extremise it" *is* the kinematic core of both special and general relativity; the only difference between the theories is whether the metric in the integral is the constant $\eta$ or the field $g(x)$. Setting proper time up this way — as arc length, frame-independently — is precisely what makes the bridge to gravitation immediate rather than a fresh start.

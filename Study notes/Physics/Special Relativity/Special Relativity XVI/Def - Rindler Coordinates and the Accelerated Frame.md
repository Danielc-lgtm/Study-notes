---
type: definition
subject: special-relativity
prereqs:
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
  - "Def - Local Frame and Four-Rotation"
  - "Def - Fermi-Walker Derivative"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] $\mathcal{O}$ has proper acceleration $a$, four-velocity $U$, four-acceleration $A$, proper time $t$. The reference inertial observer $\mathcal{O}_*$ carries the orthonormal frame $(e_0^*, e_1^*, e_2^*, e_3^*)$ and inertial coordinates $(ct_*, x_*, y_*, z_*)$, tangent to $\mathcal{O}$ at $t = 0$. The [[Def - Local Frame and Four-Rotation|local frame]] of $\mathcal{O}$ is $(e_0, e_1, e_2, e_3)$. The **local rest space** $\mathcal{E}_u(t)$ at proper time $t$ is the hyperplane through $O(t)$ orthogonal to $U(t)$; the **simultaneity hypersurface** $\Sigma_u(t)$ is the set of events Einstein–Poincaré-simultaneous to $O(t)$ for $\mathcal{O}$. This is a compound page: it defines the **local frame** of the uniformly accelerated observer, the **Rindler coordinates** they carry, and the relation between $\mathcal{E}_u(t)$ and $\Sigma_u(t)$ — because the coordinates are built from the frame and are only well-defined once one knows that the simultaneity slices are the rest spaces. Full registry on [[Special Relativity XVI — Accelerated Observers]].

---

# Axiom Motivation

An accelerated observer needs coordinates — a way to label the events around them by a time and three spatial positions — and the natural ones are built from the frame they carry. The motivation is to construct, for the uniformly accelerated observer, the analogue of the inertial coordinates an inertial observer uses, and to discover what is strange about them.

For an inertial observer the construction is trivial: carry a fixed orthonormal frame, label each event by its time (proper time of the observer when the event is simultaneous) and its spatial position (components in the frame). The result is the global inertial coordinates, and the metric is $\eta$ everywhere. For an accelerated observer two things go wrong, and the definition must handle both. First, the frame the observer carries is not fixed — it must be transported along the curved worldline, and the question is *how*. Second, "simultaneous" is no longer a global notion, so the time-labelling is delicate.

Take the frame first. The observer carries an orthonormal tetrad $(e_\alpha)$ with $e_0 = U$ always (the time leg is the four-velocity). The natural choice for the first spatial leg is $e_1 = a^{-1}A$, the unit vector along the four-acceleration — the direction the observer feels pushed. The remaining two legs $e_2, e_3$ span the plane orthogonal to the motion; since nothing distinguishes a direction there, take them constant, equal to $e_2^*, e_3^*$. The decisive requirement is that the frame be **non-rotating** — that its four-rotation vanish, $\vec\omega = 0$ — which is the third defining condition of the uniformly accelerated observer. Non-rotating transport of a frame along a worldline is **Fermi–Walker transport** ([[Def - Fermi-Walker Derivative]]): the rule that drags the frame along while correcting for the acceleration so that gyroscopes held in the frame stay fixed relative to it. The motivation for Fermi–Walker rather than naive parallel transport is that a naively parallel-transported frame along an accelerated worldline would tip over (its time leg would cease to be $U$); Fermi–Walker is exactly the correction that keeps $e_0 = U$ while introducing no spatial rotation. So the local frame is forced: $e_0 = U$, $e_1 = a^{-1}A$, $e_2 = e_2^*$, $e_3 = e_3^*$, Fermi–Walker transported.

Now the coordinates. Label an event $M$ by the proper time $t$ of the observer whose rest space $\mathcal{E}_u(t)$ contains $M$, and by the components $(x, y, z)$ of the vector from $O(t)$ to $M$ in the spatial frame $(e_1, e_2, e_3)$. This is the same recipe as for an inertial observer, with "rest space" replacing "global simultaneity slice". The result is the **Rindler coordinates** $(ct, x, y, z)$. The subtlety is whether the rest spaces $\mathcal{E}_u(t)$ actually slice spacetime cleanly — and they do not, globally: they all pivot about the centre event $A = (0, -a^{-1})$, so they intersect there, and the coordinates are only good on one side, $x > -a^{-1}$. This is not a defect to be patched but the honest content of the definition: an accelerated observer simply cannot coordinatise all of spacetime, and the boundary of the region they can is the Rindler horizon.

One more motivational point underlies the whole construction and deserves its own treatment: *should the time-labelling use the tangent rest space $\mathcal{E}_u(t)$ or the exact simultaneity hypersurface $\Sigma_u(t)$?* For a general accelerated observer these differ — the rest space is the flat tangent plane, the simultaneity hypersurface is the genuinely curved set of Einstein-simultaneous events — and they agree only to second order in the distance. The motivation for using $\mathcal{E}_u(t)$ anyway is that for a *uniformly* accelerated observer the two coincide **exactly** (proved below and in [[Thm - Worldline of a Uniformly Accelerated Observer]]), so the Rindler coordinates built from the rest spaces *are* the coordinates built from genuine simultaneity. This exact coincidence is special to uniform acceleration; it is why the uniformly accelerated observer is the one for which the accelerated frame is cleanest.

---

# The Definition

**The local frame.** The **local frame** of the uniformly accelerated observer $\mathcal{O}$ is the orthonormal tetrad $(e_\alpha(t))$ along $\mathcal{L}_0$ defined by
$$
e_0(t) = U(t), \qquad e_1(t) = \frac{1}{a}A(t), \qquad e_2(t) = e_2^*, \qquad e_3(t) = e_3^*.
$$
It is Fermi–Walker transported (its [[Def - Local Frame and Four-Rotation|four-rotation]] vanishes), and evolves along the worldline by
$$
\frac{de_0}{dt} = a\,e_1, \qquad \frac{de_1}{dt} = a\,e_0, \qquad \frac{de_2}{dt} = \frac{de_3}{dt} = 0
$$
(with $c$: each $d/dt$ carries a factor $c^{-1}$). In terms of the reference frame, $e_0(t) = \cosh(act)e_0^* + \sinh(act)e_1^*$ and $e_1(t) = \sinh(act)e_0^* + \cosh(act)e_1^*$; the change of frame from $(e_\alpha^*)$ to $(e_\alpha(t))$ is a Lorentz boost of rapidity $\psi = act$.

**Rindler coordinates.** The **Rindler coordinates** $(ct, x, y, z)$ of an event $M\in\mathcal{E}_u(t)$ are the proper time $t$ of the observer whose local rest space contains $M$, together with the components of $\overrightarrow{O(t)M} = x\,e_1(t) + y\,e_2(t) + z\,e_3(t)$. They are related to the inertial coordinates of $\mathcal{O}_*$ by
$$
\boxed{\;
\begin{cases}
ct_* = (x + a^{-1})\sinh(act),\\[2pt]
x_* = (x + a^{-1})\cosh(act) - a^{-1},\\[2pt]
y_* = y,\\[2pt]
z_* = z,
\end{cases}
\qquad t\in\mathbb{R},\ \ x > -a^{-1}.
\;}
$$
The restriction $x > -a^{-1}$ is the region the observer can perceive by light signals (everything else is behind the [[Def - Rindler Horizon|Rindler horizon]]). The lines $x = \mathrm{const}$ are hyperbola branches with the same centre $A = (0,-a^{-1})$ and asymptotes as $\mathcal{L}_0$; the lines $t = \mathrm{const}$ are straight lines through $A$ of slope $\tanh(act)$. Substituting the transformation into $ds^2 = c^2 dt_*^2 - dx_*^2 - dy_*^2 - dz_*^2$ gives the **Rindler metric**
$$
\boxed{\,ds^2 = (1 + ax)^2\,c^2\,dt^2 - dx^2 - dy^2 - dz^2\,}.
$$

**Rest space versus simultaneity hypersurface.** For a *generic* accelerated observer (four-acceleration norm $a$ varying, possibly nonzero torsion $T_1$), the local rest space $\mathcal{E}_u(t)$ and the exact Einstein–Poincaré [[Def - Einstein-Poincaré Simultaneity|simultaneity hypersurface]] $\Sigma_u(t)$ differ; writing $s = cT$ for the round-trip light distance to an event $M$ on $\Sigma_u(t)$, the discrepancy is second order in $as$:
$$
U(t)\cdot\overrightarrow{O M} = -\frac{(as)^2}{6}\!\left[\frac{\dot a}{a^3}\,A(t)\cdot\overrightarrow{OM} + \frac{T_1}{a}\,e_2^{\,\mathrm{SF}}\cdot\overrightarrow{OM}\right] + O((as)^3).
$$
(Here $\dot a = c^{-1}da/dt$ and $e_2^{\,\mathrm{SF}}$ is a Serret–Frenet leg; if $M\in\mathcal{E}_u(t)$ exactly then the left side is zero.) The two hypersurfaces therefore coincide to first order in $as$ for any observer, and to second order whenever $|\dot a|/a^2 \ll as$ and $|T_1|/a \ll as$. For a **uniformly accelerated** observer one has $\dot a = 0$ (constant proper acceleration) and $T_1 = 0$ (planar worldline), and in fact the coincidence is *exact at all orders*:
$$
\forall t\in\mathbb{R},\qquad \Sigma_u(t) = \mathcal{E}_u(t).
$$

---

# Relate to Other Fields / Compression

The Rindler metric $ds^2 = (1 + ax)^2 c^2 dt^2 - dx^2 - \cdots$ is the flat metric written in accelerated coordinates: spacetime is genuinely flat (the coordinate transformation to $(ct_*, x_*)$ exists and is smooth on $x > -a^{-1}$), but the metric *components* depend on position through the factor $(1+ax)^2$ in $g_{tt}$. This is the template for how a metric encodes a gravitational potential. Comparing with the weak-field form $g_{tt} = (1 + \Phi/c^2)^2$ of general relativity, the Rindler potential is $\Phi = c^2 a x = gx$ — exactly the Newtonian potential of a uniform gravitational field of strength $g = c^2 a$. The position-dependent $g_{tt}$ is what produces the gravitational time dilation $d\tau = (1+ax)\,dt$ for a clock at fixed $x$, and the equivalence principle reads the accelerated coordinates as a uniform gravitational field.

**True name:** Rindler coordinates are *the coordinates adapted to a family of uniformly accelerated observers* — a comoving grid in which each observer sits at fixed $(x, y, z)$ — and the time coordinate $t$ is the proper time of the fiducial observer at $x = 0$, dilated to $(1+ax)t$ for the observer at $x$. The metric component $g_{tt} = (1+ax)^2$ is the squared clock rate, i.e. the squared lapse function.

The construction is the special-relativistic instance of the **moving-frame** (repère mobile) method of differential geometry: a frame field is transported along a curve, and the transport law (here Fermi–Walker) is encoded in a connection-like object (the four-rotation $\Omega$). The exact coincidence $\Sigma_u(t) = \mathcal{E}_u(t)$ is special to constant curvature; for a general worldline only the first-order (and conditionally second-order) agreement holds, which is the statement that the rest space is the *osculating* simultaneity hypersurface.

---

# Examples / Corollaries

**Is an instance — the fiducial observer at $x = 0$.** Setting $x = y = z = 0$ in the transformation recovers $ct_* = a^{-1}\sinh(act)$, $x_* = a^{-1}[\cosh(act)-1]$, the worldline of $\mathcal{O}$ itself. The line $x = 0$ is the observer's own worldline, with $t$ their proper time.

**Is an instance — the Rindler metric reproduces the clock rate.** A clock fixed at Rindler position $x$ has $dx = dy = dz = 0$, so $ds^2 = (1+ax)^2 c^2 dt^2$ and its proper time is $d\tau = (1+ax)\,dt$. This is the position-dependent rate that drives clock desynchronisation and the redshift; see [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame]].

**Is NOT an instance — coordinates beyond the horizon.** The transformation is not valid for $x \le -a^{-1}$: at $x = -a^{-1}$ the metric factor $(1+ax)$ vanishes (the coordinate degenerates, like the pole of a sphere), and beyond it the "coordinates" would label events the observer cannot causally reach. The Rindler chart covers only the wedge $x_* > |ct_*|$, not all of Minkowski space — a single accelerated observer cannot coordinatise spacetime globally.

**Is NOT an instance — the rest space and simultaneity hypersurface of a *non-uniformly* accelerated observer.** For an observer whose proper acceleration varies ($\dot a\neq 0$) or whose worldline twists out of a plane ($T_1\neq 0$), the tangent rest space $\mathcal{E}_u(t)$ and the exact simultaneity hypersurface $\Sigma_u(t)$ differ at second order in the distance. Only for the uniformly accelerated observer do they coincide exactly; assuming the coincidence for a general accelerated observer is an error.

**Corollary — Rindler time-translation is a Lorentz boost.** Shifting $t\to t + t_0$ at fixed $x$ maps the worldline to itself and acts on the inertial coordinates as a boost of rapidity $act_0$. This is the statement that the uniformly accelerated observer is *stationary*: all events along the worldline are equivalent, related by a symmetry of Minkowski space.

**Calibration check.** If the construction is understood, the reader should be able to: (i) verify the Rindler metric by differentiating the coordinate transformation and substituting into $ds^2 = c^2 dt_*^2 - dx_*^2$; (ii) read off the proper-time rate $d\tau = (1+ax)\,dt$ for a static clock and identify $(1+ax)$ as the lapse; and (iii) explain in one sentence why $\Sigma_u(t) = \mathcal{E}_u(t)$ exactly here but only approximately for a generic accelerated observer ($\dot a = 0$, $T_1 = 0$).

---

# Unlocked by This

> [!tip] The Equivalence Principle and the Metric of Gravity *(from General Relativity)*
> The Rindler metric $ds^2 = (1+ax)^2 c^2 dt^2 - dx^2 - \cdots$ is the prototype of a metric carrying a gravitational potential: $g_{tt} = (1+\Phi/c^2)^2$ with $\Phi = gx$. In **general relativity** the metric components $g_{\mu\nu}(x)$ become genuinely position-dependent in a way that *cannot* be transformed away (curvature), but the local structure is always Rindler: at any event one can choose a freely-falling frame in which the metric is $\eta$ and its first derivatives vanish, and an observer who resists free fall — hovering in the field — is uniformly accelerated and sees exactly the Rindler metric locally. The factor $(1+ax)$ is the **lapse function**, and its gradient is the local "gravitational acceleration" felt by the static observer. This is the bridge from the flat accelerated frame of this page to [[Special Relativity XXV — Toward Relativistic Gravitation|the curved metric of gravitation]].

> [!tip] Horizons and Coordinate Singularities *(from General Relativity)*
> The breakdown of Rindler coordinates at $x = -a^{-1}$, where $g_{tt}\to 0$, is the flat-spacetime model of a **coordinate singularity at a horizon**. The Schwarzschild metric has exactly such a vanishing of $g_{tt}$ at the event horizon $r = 2GM/c^2$, and the lesson the Rindler case teaches is that this is *not* a real singularity: spacetime is perfectly smooth there (Minkowski space has no singularity at $x = -a^{-1}$), and a different coordinate system (the inertial one for Rindler; Kruskal coordinates for Schwarzschild) crosses the horizon without incident. Distinguishing coordinate singularities from genuine curvature singularities, learned here in the cleanest possible setting, is essential to understanding black holes.

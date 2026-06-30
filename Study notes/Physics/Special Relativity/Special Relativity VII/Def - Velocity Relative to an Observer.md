---
type: definition
subject: special-relativity
prereqs:
  - "Def - Lorentz Factor and Relative Velocity"
  - "Def - Observer and Local Rest Space"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
  - "Def - Local Frame and Four-Rotation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$. The observer $\mathcal{O}$ has four-velocity $U_0$, proper time $\tau$ (also written $t$, the observer's clock), and an orthonormal [[Def - Local Frame and Four-Rotation|local frame]] $(e_\alpha) = (e_0 = U_0, e_1, e_2, e_3)$ spanning, with the $e_i$, the [[Def - Observer and Local Rest Space|local rest space]] $E_{U_0} = U_0^\perp$. The particle $\mathcal{P}$ has four-velocity $U$; its perceived position in the rest space at the observer's instant is $M$, with position vector $\overrightarrow{OM} = x^i(t)\,e_i$, where $O$ is the event on $\mathcal{O}$'s worldline at proper time $t$. The [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]] onto the rest space is $\perp_{U_0} = \mathrm{Id} - (\,\cdot\,U_0)U_0$. Full registry on [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]].

---

# Axiom Motivation

The velocity of a particle relative to an observer ought to be the simplest thing in the world — the rate at which its position changes — and the only question is *whose* position and *whose* time. The previous chapter on observers supplies the answer to both: the position is the particle's location in the observer's [[Def - Observer and Local Rest Space|local rest space]], the three-dimensional spacelike hyperplane the observer regards as "space now", and the time is the observer's [[Def - Proper Time|proper time]], read off their own clock. With those two choices fixed, the velocity is forced: it is the derivative of the rest-space position vector with respect to the observer's proper time.

Why the rest space and not some other notion of "space"? Because the rest space $U_0^\perp$ is the locus of events the observer judges simultaneous with a given event on their worldline (the [[Def - Einstein-Poincaré Simultaneity|Einstein–Poincaré]] convention), and "where the particle is now" can only mean "the point of the particle's worldline simultaneous with now". Any other hyperplane would correspond to a different observer's simultaneity and would give that observer's velocity, not this one's. The rest space is the unique spacelike hyperplane orthogonal to $U_0$, and orthogonality to $U_0$ is exactly the simultaneity condition — so the rest space is not a choice but a consequence of the observer's four-velocity.

Why differentiate with respect to the observer's proper time rather than the particle's? Because we want the velocity *this observer measures with their own instruments* — rulers laid out in their rest space and their own clock ticking. If we differentiated with respect to the particle's proper time instead, we would get the proper velocity (celerity), which is a perfectly good four-vector quantity but is unbounded and is not what a ruler-and-clock measurement returns. The choice of the observer's clock is what makes the result the physical speed, bounded by $c$, that the observer would report.

The subtle point — and the reason this definition needs the machinery of the previous chapter — is that "the derivative of the position vector" is ambiguous in a non-inertial frame. The position vector $\overrightarrow{OM}$ is a vector that lives in a rest space which is itself *tilting and rotating* as the observer moves, so its ordinary coordinate derivative mixes the genuine motion of the particle with the rotation of the observer's axes. The clean definition uses the [[Def - Fermi-Walker Derivative|derivative with respect to the observer]] — the rate of change of the position vector as seen in the observer's rotating-and-tilting rest frame — so that the velocity captures the particle's motion alone, with the frame's rotation accounted for separately. For an inertial observer the distinction vanishes and the velocity is just $\mathrm{d}\mathbf x/\mathrm{d}t$; for a rotating observer it is the source of the Coriolis term, exactly as in Newtonian mechanics.

What would go wrong with variants? If you used the particle's proper time, you would get the unbounded celerity, not the physical speed. If you used a hyperplane other than $U_0^\perp$, you would compute a different observer's velocity. If you used the ordinary coordinate derivative for a rotating observer, the "velocity" of a particle sitting still in space would spuriously include the rotation of the axes. And if you tried to define the velocity as a four-vector $U - U_0$ rather than a rest-space three-vector, it would not be orthogonal to $U_0$, not spacelike, and its norm would not be the speed. The definition is pinned by the demand that it be the rate of change of the rest-space position with respect to the observer's clock, computed in a way that does not contaminate the particle's motion with the frame's rotation.

---

# The Definition

Let $\mathcal{O}$ be an observer with four-velocity $U_0$, proper time $t$, and local frame $(e_\alpha)$. For each instant $t$, the position of the particle $\mathcal{P}$ is marked in the rest space by coordinates $x^i(t)$ via the position vector $\overrightarrow{OM} = x^i(t)\,e_i$.

**The velocity of the particle $\mathcal{P}$ relative to the observer $\mathcal{O}$** is the derivative of the rest-space position vector with respect to the observer's proper time:
$$
\boxed{\;\mathbf V := \frac{\mathrm{d}\mathbf x}{\mathrm{d}t},\qquad V(t) := \frac{\mathrm{d}x^i}{\mathrm{d}t}\,e_i(t)\;}
$$
a vector in the local rest space $E_{U_0}(t)$. Equivalently, $V$ is the rest-space part of the particle's four-velocity, obtained by orthogonal projection and rescaled by the Lorentz factor:
$$
V = \frac{1}{\Gamma}\,\perp_{U_0}U,
$$
where $\Gamma = U \cdot U_0$ is the [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]]; this is the rest-space term of the orthogonal decomposition $U = \Gamma(U_0 + V)$.

The vector $V$ is spacelike and orthogonal to $U_0$ ($V \cdot U_0 = 0$). Its components in the observer's frame are
$$
V^\alpha = (0, V^1, V^2, V^3),\qquad V^i = \frac{\mathrm{d}x^i}{\mathrm{d}t},
$$
and the **speed** of $\mathcal{P}$ relative to $\mathcal{O}$ is the Euclidean norm of these spatial components,
$$
|\mathbf V| = \|V\|_g = \sqrt{(V^1)^2 + (V^2)^2 + (V^3)^2} = \sqrt{-\,V\cdot V}.
$$
The four-velocity of $\mathcal{P}$ has components, in the observer's frame,
$$
u^\alpha = \big(\Gamma,\ \Gamma V^1,\ \Gamma V^2,\ \Gamma V^3\big).
$$

For a **general (accelerated, rotating) observer** the relation between the relative velocity and the four-velocity carries correction terms,
$$
V = \frac{1}{\Gamma}\,\perp_{U_0}U \;-\; \boldsymbol\omega \times_{U_0}\overrightarrow{OM},
$$
where $\boldsymbol\omega$ is the observer's four-rotation and $\times_{U_0}$ the rest-space cross product; the extra term is the velocity the particle appears to have purely because the observer's axes rotate. For an **inertial observer** ($\boldsymbol\omega = 0$) or when the particle is at the observer's location ($\overrightarrow{OM} = 0$), the simple form $V = (1/\Gamma)\perp_{U_0}U$ holds.

---

# Categorical / Structural Definition

The relative velocity is the image of the particle's four-velocity under a fibre-wise linear map determined by the observer. At each event of the observer's worldline, the observer's four-velocity $U_0$ determines the orthogonal splitting $\mathbb{R}^{1,3} = \mathbb{R}U_0 \oplus U_0^\perp$, and the **kinematic map** sends a future timelike unit vector $U$ to the pair (Lorentz factor, relative velocity):
$$
U \;\longmapsto\; \big(\Gamma, V\big) = \Big(U \cdot U_0,\ \tfrac{1}{U\cdot U_0}\,\perp_{U_0}U\Big).
$$
The relative velocity is the second component. The target space of $V$ is the rest space $U_0^\perp$ with its induced (negative-definite, hence Euclidean up to sign) metric, restricted to the open unit ball $\{|\mathbf V| < 1\}$ — the **velocity ball**. This ball, with the metric induced from the unit hyperboloid via the kinematic map, is the **Klein** (or Beltrami) model of hyperbolic space $\mathbb{H}^3$: straight chords of the ball are geodesics, the boundary sphere $|\mathbf V| = 1$ is the speed-of-light limit at infinity, and the Lorentz group acts on the ball by the projective transformations preserving it. The relative velocity is thus a coordinate on the Klein model of velocity space, and the velocity-composition law of [[Special Relativity VIII — Kinematics II, Change of Observer]] is the (non-commutative) addition rule this model carries — a **gyrogroup** operation, whose failure of associativity is the Thomas rotation.

---

# Relate to Other Fields / Compression

In differential geometry, the construction is the projection of an ambient tangent vector onto a hypersurface, with the rotation correction being the difference between the ambient derivative and the intrinsic (rotating-frame) derivative — the same bookkeeping that produces the connection coefficients of a moving frame. The Coriolis term $\boldsymbol\omega \times_{U_0}\overrightarrow{OM}$ is the special-relativistic instance of the inertial terms that appear whenever you differentiate a vector field expressed in a rotating basis, familiar from the rotating-frame mechanics of [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|classical mechanics]].

In hyperbolic geometry, the relative velocity is a coordinate on the Klein model of $\mathbb{H}^3$, the unit ball with the projective (Beltrami–Klein) structure. The speed $|\mathbf V|$ is the Euclidean radius in this model, and the rapidity (the true hyperbolic distance from the centre) is $\tanh^{-1}|\mathbf V|$ — which is why velocities below $c$ map to a *bounded* ball while rapidities fill all of $\mathbb{H}^3$.

**True name:** The relative velocity is the rate of change of the particle's rest-space position with respect to the observer's own clock — equivalently, the rest-space part of the particle's four-velocity divided by the Lorentz factor. Operationally: in the observer's frame, $V^i = \mathrm{d}x^i/\mathrm{d}t = u^i/\Gamma$, and the speed is the Euclidean length of the spatial components.

---

# Examples / Corollaries

**Is an instance — uniform circular motion.** Let $\mathcal{O}$ be inertial and let $\mathcal{P}$ orbit in the $e_1$–$e_2$ plane: $x^1 = R\cos\Omega t$, $x^2 = R\sin\Omega t$, $x^3 = 0$. Then $V = -R\Omega\sin\Omega t\,e_1 + R\Omega\cos\Omega t\,e_2$, a vector of constant speed $|\mathbf V| = R\Omega$ tangent to the circle, with $\Gamma = (1 - R^2\Omega^2)^{-1/2}$ constant. This is the relative velocity of a point on a relativistically rotating rim.

**Is an instance — a photon's velocity.** Although a photon has no four-velocity, the same definition $\mathbf V = \mathrm{d}\mathbf x/\mathrm{d}t$ applies to its rest-space track, giving $\mathbf V = c\mathbf N = \mathbf N$ (with $c=1$), a vector of speed exactly $1$; see [[Def - Photon Propagation Direction and Velocity]]. The relative velocity of light is the propagation direction.

**Is NOT an instance — the proper velocity $\Gamma\mathbf V$.** The rest-space part of the four-velocity *without* the $1/\Gamma$ factor, namely $\Gamma\mathbf V$, is the proper velocity (celerity) $\mathrm{d}\mathbf x/\mathrm{d}\tau'$, differentiated with respect to the particle's proper time. It is not the relative velocity: it is unbounded, tending to infinity as $|\mathbf V| \to c$, whereas the relative velocity is capped at $c$. The two differ by the factor $\Gamma$ that converts the particle's clock to the observer's.

**Is NOT an instance — the coordinate velocity in a rotating frame, uncorrected.** For a rotating observer, the bare derivative $\mathrm{d}x^i/\mathrm{d}t$ of the components in the rotating basis is *not* the relative velocity of the particle: a particle held fixed in the observer's rest space (genuinely at rest relative to the observer) still has changing components if the basis rotates, yet its relative velocity is zero. The correct relative velocity uses the derivative with respect to the observer, which subtracts the basis rotation; equivalently the corrected formula $V = (1/\Gamma)\perp_{U_0}U - \boldsymbol\omega\times_{U_0}\overrightarrow{OM}$ removes the spurious term.

**Corollary — the speed is the Euclidean norm of the spatial four-velocity components, divided by the time component.** From $u^\alpha = (\Gamma, \Gamma V^i)$, the speed is $|\mathbf V| = \sqrt{\sum (u^i)^2}\,/\,u^0$. This is the fastest route to a speed when the four-velocity components are known: form the ratio of the spatial magnitude to the time component.

**Corollary — the relative velocity vanishes if and only if the four-velocities are equal.** $V = 0 \iff \perp_{U_0}U = 0 \iff U \parallel U_0 \iff U = U_0$ (both being future unit timelike). A particle is at rest relative to an observer exactly when it shares the observer's four-velocity — the defining case $\Gamma = 1$.

**Calibration check.** If you have understood the definition you should be able to: (i) compute the relative velocity and speed of a particle given its worldline $x^i(t)$ in an inertial observer's frame, and check that the four-velocity components are $(\Gamma, \Gamma V^i)$; (ii) explain why a particle at rest in a *rotating* observer's frame has zero relative velocity despite its coordinates changing, and which term in the general formula accounts for this; (iii) distinguish the relative velocity from the proper velocity by the clock used in the differentiation, and state which one is bounded by $c$.

---

# Unlocked by This

> [!tip] Aberration of Light *(from Change of Observer)*
> The direction of the relative velocity is observer-dependent: a star seen overhead by one observer appears displaced toward the direction of motion for a second observer moving relative to the first. Transforming the velocity direction — for a photon, the [[Def - Photon Propagation Direction and Velocity|propagation direction]] $N$ — between observers is the [[Thm - Aberration of Light|aberration]] law of **Special Relativity VIII**, the relativistic correction astronomers apply to stellar positions.

> [!tip] The Velocity-Composition Law and Gyrogroups *(from Change of Observer)*
> Because the relative velocity is a coordinate on the Klein model of hyperbolic velocity space, composing velocities — finding the velocity relative to observer $C$ given the velocities relative to $B$ and of $B$ relative to $C$ — is a non-commutative, non-associative operation, a **gyrogroup** addition. Its non-associativity is the [[Def - Thomas Rotation|Thomas rotation]]; the collinear special case recovers the [[Thm - Relativistic Velocity Addition|velocity-addition formula]] of Special Relativity II. This is the content of **Special Relativity VIII**.

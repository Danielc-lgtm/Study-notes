---
type: definition
subject: special-relativity
prereqs:
  - "Def - Observer and Local Rest Space"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
  - "Def - Velocity Relative to an Observer"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a null vector has $X \cdot X = 0$ and a spacelike vector has $X \cdot X < 0$. The observer $\mathcal{O}$ has four-velocity $U_0$ (future timelike unit, $U_0 \cdot U_0 = 1$), proper time $t$, four-acceleration $A_0$, four-rotation $\boldsymbol\omega$, and [[Def - Observer and Local Rest Space|local rest space]] $E_{U_0} = U_0^\perp$. A photon $\mathcal{P}$ moves on a null geodesic $\Delta$; its tangent is a future-directed null vector. The [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]] onto the rest space is $\perp_{U_0} = \mathrm{Id} - (\,\cdot\,U_0)U_0$, and $\overrightarrow{OM}$ is the photon's position vector in the rest space. Full registry on [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]].

> [!warning] Convention: Gourgoulhon uses the opposite signature
> Gourgoulhon (mostly-plus) adapts the null vector by $\vec\ell \cdot \vec u = -1$ and finds the propagation direction $\vec n$ with $\vec n \cdot \vec n = +1$. Flipping the sign of every scalar product gives our adaptation $\ell \cdot U_0 = +1$ and our unit condition $N \cdot N = -1$ (since $N$ is spacelike in mostly-minus). In both signatures the *physical* magnitude of the propagation direction is $|\mathbf N| = 1$, and the speed of light is $c$.

---

# Axiom Motivation

Everything in this chapter so far has been built on the particle's [[Def - Four-Velocity and Four-Acceleration|four-velocity]] — the unit timelike tangent to its worldline. A photon does not have one. Its worldline is a null geodesic, and a tangent to a null geodesic is a null vector, with $X \cdot X = 0$; such a vector cannot be normalised to unit length, because dividing by its (zero) Minkowski norm is meaningless. So the entire apparatus — Lorentz factor as $U \cdot U_0$, relative velocity as $(1/\Gamma)\perp_{U_0}U$ — breaks down at the first step, and we need a replacement for "the four-velocity" that works for light.

The desideratum is a single vector along the photon's worldline that plays, as far as possible, the role the four-velocity played for a massive particle: it should be canonically determined by the photon and the observer, and its rest-space part should give the photon's direction and speed. The four-velocity was pinned down by *two* conditions — it points along the worldline, and it has unit norm. The first condition survives for a photon (point along the null geodesic), but the second is impossible (the norm is zero). We need a substitute for "unit norm", and the natural one is to fix the *normalisation* against the observer instead: demand that the vector's scalar product with the observer's four-velocity be one.

Why $\ell \cdot U_0 = 1$ specifically? Because $\ell \cdot U_0$ is, for a timelike particle, exactly the Lorentz factor — the time component in the observer's frame — and setting it to one is the photon analogue of "let the time component be the natural unit". More concretely, the scalar product with $U_0$ is the only Lorentz-covariant scaling available (there is no norm to use), and choosing it to be $1$ makes the rest-space part come out *unit* length, as we will see. Any nonzero choice would work to fix the scale, but $1$ is the choice that makes the propagation direction a unit vector and the speed exactly $c$, so it is the canonical one.

Now the geometry that makes it all fit. Decompose the adapted null vector orthogonally: $\ell = (\ell \cdot U_0)U_0 + \perp_{U_0}\ell = U_0 + N$, where $N := \perp_{U_0}\ell$ is the rest-space part. The null condition $\ell \cdot \ell = 0$ is the constraint that does the work. Expand it:
$$
0 = \ell \cdot \ell = (U_0 + N)\cdot(U_0 + N) = \underbrace{U_0\cdot U_0}_{=1} + 2\underbrace{U_0 \cdot N}_{=0} + N\cdot N = 1 + N \cdot N,
$$
using $U_0 \cdot U_0 = 1$ and $N \cdot U_0 = 0$. Therefore $N \cdot N = -1$, which in the Euclidean rest-space metric means $|\mathbf N| = \sqrt{-N\cdot N} = 1$: the rest-space part is automatically a *unit* vector. This is the whole point. The null character of light, expressed through the adaptation $\ell \cdot U_0 = 1$, forces the spatial direction to have length exactly one — and since the speed of light will be the norm of this direction, the speed comes out exactly $c$. The constancy of the speed of light is *this algebraic fact*, and it holds for any observer $U_0$ whatsoever.

What would go wrong with variants? If you tried to normalise the tangent to unit Minkowski norm, you would divide by zero. If you adapted by $\ell \cdot U_0 = \kappa$ for some other constant $\kappa$, the propagation direction would have norm $\kappa$ instead of $1$ and you would have to remember the rescaling everywhere. If you tried to define the photon's "velocity" as a four-vector rather than projecting to the rest space, you would not get a unit spatial direction. The definition is pinned by the impossibility of unit-norm normalisation (forcing the adaptation against $U_0$) and the demand that the spatial part be the unit direction of propagation (fixing the constant to $1$).

---

# The Definition

Let $\mathcal{O}$ be an observer with four-velocity $U_0$, and let $\mathcal{P}$ be a photon moving on a null geodesic $\Delta$ in the vicinity of $\mathcal{O}$'s worldline.

**The adapted null vector** of the photon with respect to $\mathcal{O}$ is the unique future-directed null vector $\ell$ parallel to $\Delta$ normalised by
$$
\ell \cdot U_0 = 1.
$$
Its orthogonal decomposition with respect to $U_0$ is
$$
\boxed{\;\ell = U_0 + N,\qquad N \cdot U_0 = 0\;}
$$
where $N := \perp_{U_0}\ell$ is a spacelike vector in the local rest space.

**The propagation direction of the photon $\mathcal{P}$ relative to the observer $\mathcal{O}$** is the vector $N$. The null condition $\ell \cdot \ell = 0$ forces it to be a **unit** vector,
$$
\boxed{\;N \cdot N = -1,\qquad |\mathbf N| = \sqrt{-N \cdot N} = 1\;}
$$
in the Euclidean metric of the rest space.

**The velocity of the photon relative to $\mathcal{O}$** is, as for a massive particle, the derivative of its rest-space position with respect to the observer's proper time, $\mathbf V = \mathrm{d}\mathbf x/\mathrm{d}t$. Working it out,
$$
\mathbf V = c\,(1 + A_0 \cdot \overrightarrow{OM})\,N \;-\; \boldsymbol\omega\times_{U_0}\overrightarrow{OM}
$$
in general. When the photon crosses the observer's worldline ($\overrightarrow{OM} = 0$) or the observer is inertial ($A_0 = 0$, $\boldsymbol\omega = 0$), this reduces to
$$
\boxed{\;\mathbf V = c\,N = N\;(\text{with }c=1)\;}
$$
a vector whose norm is exactly the speed of light:
$$
\|\mathbf V\|_g = c.
$$
The propagation direction $N$ is thus the unit vector along the photon's spatial track, and the photon's velocity relative to a local or inertial observer is $c$ times this unit vector.

---

# Categorical / Structural Definition

Structurally, the adapted null vector realises the **celestial sphere** as a section of the future null cone. The future null directions at an event form a cone $\mathcal{N}^+ = \{X : X \cdot X = 0,\ X^0 > 0\}/\sim$ (modulo positive rescaling), a two-sphere's worth of directions. An observer $U_0$ provides a *section* of this projectivisation: the affine hyperplane $\{\ell : \ell \cdot U_0 = 1\}$ intersects each null ray exactly once, and the intersection is the adapted vector $\ell = U_0 + N$. The map $\ell \mapsto N$ identifies the section with the unit sphere $\mathbb{S}^2 = \{N \in U_0^\perp : |\mathbf N| = 1\}$ in the rest space — the observer's **celestial sphere**, the set of directions from which the observer can receive light.

This construction is observer-dependent in a precise and beautiful way. A different observer $U_0'$ slices the same null cone by a different hyperplane and obtains a different identification with a sphere; the map between the two spheres — the change of propagation direction under a change of observer — is the **aberration** map, and it is a *conformal* (angle-preserving) transformation of the sphere. Identifying $\mathbb{S}^2$ with the Riemann sphere $\mathbb{CP}^1$ by stereographic projection, the change-of-observer map becomes a **Möbius transformation** $z \mapsto (az+b)/(cz+d)$, the action of $SL(2,\mathbb{C})$ on $\mathbb{CP}^1$. Thus the propagation direction is a point of $\mathbb{CP}^1$, the future null cone is the cone over $\mathbb{CP}^1$, and the Lorentz group acts as the conformal automorphisms $\mathrm{PSL}(2,\mathbb{C})$ of the sphere — the structural heart of [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

---

# Relate to Other Fields / Compression

In projective and conformal geometry, the propagation direction is a point of the projectivised future null cone, which is a two-sphere, and the observer's choice of section turns it into a unit sphere in the rest space. The conformal structure on this sphere — preserved under change of observer — is the reason the Lorentz group is the conformal group of $\mathbb{S}^2$, equivalently of $\mathbb{CP}^1$.

In optics, $N$ is the unit wave-normal of the light ray as the observer measures it, and $\mathbf V = cN$ is the ray velocity. The observer-dependence of $N$ is stellar aberration; the observer-dependence of the photon's frequency (carried separately by the time component of the photon's four-momentum) is the Doppler shift.

**True name:** The propagation direction is the rest-space part of the photon's null tangent, normalised against the observer by $\ell \cdot U_0 = 1$; the null condition makes it automatically a unit vector, so the velocity of light is $c$ times a unit direction. Operationally: take any null vector along the photon's worldline, scale it so its scalar product with $U_0$ is $1$, and read off the spatial part — it has unit length, and the speed is $c$.

---

# Examples / Corollaries

**Is an instance — a photon along an inertial observer's $x$-axis.** In the inertial frame with $U_0 = e_0$, a photon moving in the $+e_1$ direction has adapted null vector $\ell = e_0 + e_1$ (check: $\ell \cdot U_0 = e_0 \cdot e_0 = 1$, $\ell \cdot \ell = 1 - 1 = 0$). The propagation direction is $N = e_1$, a unit vector, and the velocity is $\mathbf V = e_1$ with $\|\mathbf V\| = 1 = c$.

**Is an instance — a photon at an angle.** A photon in the $e_1$–$e_2$ plane at angle $\theta$ to $e_1$ has $\ell = e_0 + \cos\theta\,e_1 + \sin\theta\,e_2$, propagation direction $N = \cos\theta\,e_1 + \sin\theta\,e_2$ (unit length), velocity $\mathbf V = N$ of norm $1$. The angle $\theta$ is the photon's position on the observer's celestial sphere; a boost changes $\theta$ by the aberration formula.

**Is NOT an instance — a timelike unit vector as a "photon direction".** The four-velocity of a fast massive particle, $U = \Gamma(U_0 + V)$ with $|\mathbf V|$ close to but below $1$, is timelike ($U \cdot U = 1 \neq 0$), so it is not the tangent to a null geodesic and does not admit the adaptation $\ell \cdot U_0 = 1$ with a *unit* spatial part. Its spatial part $\Gamma V$ has norm $\Gamma|\mathbf V| < \Gamma$, not $1$. Only a genuinely null tangent yields a unit propagation direction.

**Is NOT an instance — the speed of light measured by an accelerated observer at a distance.** If $\mathcal{O}$ is uniformly accelerated and the photon is at $\overrightarrow{OM} \neq 0$, the coordinate speed $\mathbf V = c(1 + A_0\cdot\overrightarrow{OM})N$ has norm $c\,|1 + A_0\cdot\overrightarrow{OM}| \neq c$: light is *not* measured at speed $c$ far from such an observer. This does not contradict [[Thm - Invariance of the Velocity of Light]], which is local; it is the kinematic origin of the gravitational bending of light.

**Corollary — the speed of light is the same for every observer at a point of their worldline.** For any $U_0$, the propagation direction is a unit vector, so $\|\mathbf V\| = c$ whenever $\overrightarrow{OM} = 0$. The constancy of the speed of light is the universality of $|\mathbf N| = 1$, independent of the observer's four-velocity — proved, not postulated.

**Corollary — the photon's four-momentum.** Multiplying the adapted null vector by the energy $E = h\nu$ the observer measures gives the photon's [[Def - The Four-Momentum of a Photon|four-momentum]] $P = E\,\ell = E(U_0 + N)$, with $P \cdot U_0 = E$ the energy and the rest-space part $E N$ the momentum, of magnitude $E$ (so $|\mathbf p| = E$ for a photon, the massless relation). The propagation direction is the direction of the photon's momentum.

**Calibration check.** If you have understood the definition you should be able to: (i) verify that the null condition $\ell \cdot \ell = 0$ together with $\ell \cdot U_0 = 1$ forces $|\mathbf N| = 1$, doing the one-line expansion; (ii) explain why a photon has no four-velocity but does have an adapted null vector, and what plays the role of the unit-norm constraint; (iii) state the precise qualification under which $\|\mathbf V_{\mathrm{light}}\| = c$, and give an example of an observer for whom a *distant* photon is measured at a speed other than $c$.

---

# Unlocked by This

> [!tip] The Doppler Effect and Aberration of Light *(from Change of Observer)*
> The adapted null vector $\ell = U_0 + N$ depends on the observer through $U_0$. Changing the observer changes both the propagation direction $N$ (this is [[Thm - Aberration of Light|aberration]]) and the photon's energy $E = P \cdot U_0$ (this is the [[Thm - The Doppler Effect|Doppler effect]]). The two laws of **Special Relativity VIII** are precisely the transformation of $\ell$ under a change of $U_0$, decomposed into its direction and magnitude parts.

> [!tip] The Celestial Sphere and the Spinor Map *(from SL(2,C) and Spinors)*
> The propagation directions form the observer's celestial sphere $\mathbb{S}^2 \cong \mathbb{CP}^1$, and a change of observer acts on it by a **Möbius transformation** — the action of $SL(2,\mathbb{C})$ on the Riemann sphere. This realises the restricted Lorentz group as the conformal group of the sphere and is the geometric meaning of the double cover $SL(2,\mathbb{C}) \to SO^+(1,3)$, developed in **Special Relativity XI**. Aberration is the statement that boosting the sky is a conformal map, distorting it like a fish-eye lens while preserving angles between nearby stars.

> [!tip] Gravitational Light Bending *(from General Relativity)*
> The failure of $\|\mathbf V_{\mathrm{light}}\| = c$ for an accelerated observer measuring distant light — the factor $1 + A_0 \cdot \overrightarrow{OM}$ — is, via the equivalence principle, the statement that light bends and slows in a gravitational potential. This is the kinematic seed of the deflection of starlight by the Sun and the Shapiro time delay, the classic tests carried out in [[General Relativity I — Einstein's Equations and Schwarzschild]].

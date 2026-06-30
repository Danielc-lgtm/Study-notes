---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Observer and Local Rest Space"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
  - "Def - Proper Time"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector has $X \cdot X > 0$ and a four-velocity is a future-directed timelike **unit** vector, $U \cdot U = 1$. The observer is $\mathcal{O}$, with four-velocity $U_0$ and proper time $\tau$; the particle is $\mathcal{P}$, with four-velocity $U$ and proper time $\tau'$. The [[Def - Observer and Local Rest Space|local rest space]] of $\mathcal{O}$ is the spacelike hyperplane $E_{U_0} = U_0^\perp$, and $\perp_{U_0} = \mathrm{Id} - (\,\cdot\,U_0)U_0$ is the [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]] onto it. Full registry on [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]].

> [!warning] Convention: Gourgoulhon uses the opposite signature
> Gourgoulhon (mostly-plus, $\eta = \mathrm{diag}(-1,+1,+1,+1)$) writes the Lorentz factor as $\Gamma = -\vec u \cdot \vec u'$ and the four-velocity normalisation as $\vec u' \cdot \vec u' = -1$. Flipping the sign of every scalar product translates these to our $\Gamma = U_0 \cdot U$ and $U \cdot U = +1$. The velocity decomposition $\vec u' = \Gamma(\vec u + \vec V/c)$ keeps its form, because the relative velocity $\vec V$ is spacelike and its physical magnitude is unchanged by the signature flip.

This is a compound page: it defines two interlocking notions — the **Lorentz factor** $\Gamma$ and the **relative velocity** $V$ — because they are introduced together as the two pieces of one orthogonal decomposition, and neither is fully usable without the other. (The relative velocity gets its own dedicated page, [[Def - Velocity Relative to an Observer]], expanding the coordinate description and the projection formula; here it appears as the rest-space part of the four-velocity decomposition.)

---

# Axiom Motivation

The problem this definition solves is comparison. An observer $\mathcal{O}$ carries a clock and wants to say how fast a passing particle $\mathcal{P}$ is moving and how fast $\mathcal{P}$'s clock runs relative to their own. In Newtonian physics this is trivial — there is one universal time, so $\mathcal{P}$'s clock and $\mathcal{O}$'s clock agree, and "velocity" is the rate of change of position with respect to that shared time. Relativity has destroyed the shared time: $\mathcal{P}$ has its own [[Def - Proper Time|proper time]] $\tau'$, $\mathcal{O}$ has its own proper time $\tau$, and there is no reason for the increments to match. So the first thing to define is the *ratio* of the two increments, and the second is the velocity built from the observer's time.

Why define the Lorentz factor as a ratio of proper times, $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$, rather than by the velocity formula $\Gamma = (1 - v^2)^{-1/2}$? Because the velocity formula presupposes a global inertial frame and a single relative velocity, neither of which exists for an accelerated observer. The ratio-of-proper-times definition is primary: it is meaningful for *any* observer, inertial or not, because both proper times are intrinsic to their respective worldlines. The observer reads $\mathrm{d}\tau$ on their own clock; using the [[Def - Einstein-Poincaré Simultaneity|Einstein–Poincaré simultaneity]] of the previous chapter, they identify the two events on $\mathcal{P}$'s worldline that are "simultaneous" with the endpoints of their own $\mathrm{d}\tau$, and $\mathrm{d}\tau'$ is the proper time $\mathcal{P}$ records between them. The factor relating the two is $\Gamma$, and the entire definition rests on the simultaneity convention making "$\mathrm{d}\tau'$ corresponding to $\mathrm{d}\tau$" well-defined.

Now, why does this ratio turn out to equal the scalar product $\Gamma = U \cdot U_0$? Here is the geometry that forces it. Over the observer's increment $\mathrm{d}\tau$, the observer moves by $\mathrm{d}\tau\,U_0$ and the particle moves by $\mathrm{d}\tau'\,U$. The condition that the endpoints be simultaneous — that the particle's displacement from the observer's new position lie in the new rest space — is an orthogonality condition, and working it out (for crossing worldlines, where the position vector $\overrightarrow{OM}$ vanishes) gives exactly $\mathrm{d}\tau = (U \cdot U_0)\,\mathrm{d}\tau'$. So the scalar product is not an independent definition but a *theorem*: the ratio of proper times equals $U \cdot U_0$. This is the operational characterisation, the one that makes every later result a one-liner, and it is why the page treats $\Gamma = U \cdot U_0$ as the working definition while keeping $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$ as the conceptual one.

The relative velocity then has to be the *rest of* the particle's four-velocity. The four-velocity $U$ is a unit timelike vector; the observer splits it into a part along their own time direction $U_0$ and a part in their rest space. The part along $U_0$ is $\Gamma U_0$ (that is what $\Gamma = U \cdot U_0$ measures), and the leftover, divided by $\Gamma$ to make the decomposition $U = \Gamma(U_0 + V)$ clean, is the velocity $V$. Why divide by $\Gamma$? So that $V$ is the *velocity* — the rate of change of position with respect to the observer's time — rather than the rate with respect to the particle's proper time; the factor $\Gamma$ is exactly the conversion $\mathrm{d}\tau'/\mathrm{d}\tau$ between the two clocks. And $V$ *must* be orthogonal to $U_0$ because it is, by construction, the projection onto the rest space; this orthogonality is what makes the unit-norm constraint $U \cdot U = 1$ separate cleanly into a time piece and a space piece. Drop the orthogonality and you could not read off $\Gamma$ and $|\mathbf V|$ independently; insist on it and the geometry of the chapter unlocks.

What would go wrong with nearby variants? If you defined $\Gamma$ by the velocity formula directly, you would have no definition for an accelerated observer and no clean proof of time dilation. If you defined the relative velocity as a four-vector without projecting onto the rest space — say, just $U - U_0$ — it would not be orthogonal to $U_0$, would not be spacelike, and its norm would not be the speed. If you forgot the factor $\Gamma$ in the decomposition, writing $U = U_0 + V'$, then $V'$ would be the rate of change of position with respect to the particle's proper time (the "celerity" or "proper velocity"), which is unbounded and is *not* what an observer measures with rulers and their own clock. The definition is pinned down by three demands: meaningful for any observer (hence the proper-time ratio), operational and computable (hence the scalar product), and yielding the physical speed (hence the orthogonal projection with the $\Gamma$ normalisation).

---

# The Definition

Let $\mathcal{O}$ be an observer with four-velocity $U_0$ and proper time $\tau$, and let $\mathcal{P}$ be a particle with four-velocity $U$ and proper time $\tau'$, whose worldline lies in the vicinity of $\mathcal{O}$'s.

**The Lorentz factor** of $\mathcal{P}$ relative to $\mathcal{O}$ is the factor $\Gamma$ relating the proper-time increments of the two worldlines, as identified by $\mathcal{O}$'s simultaneity:
$$
\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'.
$$
When the worldline of $\mathcal{P}$ crosses that of $\mathcal{O}$ at the instant considered (position vector $\overrightarrow{OM} = 0$), or when $\mathcal{O}$ is an inertial observer, the Lorentz factor equals the Minkowski scalar product of the two four-velocities:
$$
\boxed{\;\Gamma = U \cdot U_0\;}
$$
In the general case (an accelerated observer measuring a particle at a distance $\overrightarrow{OM} \neq 0$),
$$
\Gamma = \frac{U \cdot U_0}{1 - A_0 \cdot \overrightarrow{OM}},
$$
where $A_0 = \mathrm{d}U_0/\mathrm{d}\tau$ is the observer's four-acceleration.

**The velocity of $\mathcal{P}$ relative to $\mathcal{O}$** is the spacelike vector $V$ in the local rest space $E_{U_0} = U_0^\perp$ appearing in the orthogonal decomposition of the four-velocity:
$$
\boxed{\;U = \Gamma\,(U_0 + V),\qquad V \cdot U_0 = 0\;}
$$
(valid for crossing worldlines or an inertial observer). Equivalently $V = (1/\Gamma)\,\perp_{U_0}U$ is the projection of $U$ onto the rest space, divided by $\Gamma$. Its Euclidean magnitude — the **speed** measured by $\mathcal{O}$ — is
$$
|\mathbf V| = \sqrt{-\,V \cdot V},
$$
the square root being of $-V\cdot V > 0$ because $V$ is spacelike. The unit-norm constraint $U \cdot U = 1$, applied to the decomposition, gives the master relation
$$
\Gamma^2\big(1 - |\mathbf V|^2\big) = 1,\qquad\text{equivalently}\qquad \Gamma = \big(1 - |\mathbf V|^2\big)^{-1/2}.
$$

In the observer's own orthonormal frame $(e_\alpha)$ with $e_0 = U_0$, the four-velocity has components $u^\alpha = (\Gamma, \Gamma V^1, \Gamma V^2, \Gamma V^3)$, the relative velocity has components $V^\alpha = (0, V^1, V^2, V^3)$, and $\Gamma = u^0$.

---

# Categorical / Structural Definition

Structurally, the Lorentz factor and relative velocity are the two components of an orthogonal-decomposition map. Fix the observer's four-velocity $U_0$, a future-directed timelike unit vector. Minkowski space splits as an orthogonal direct sum
$$
\mathbb{R}^{1,3} = \mathbb{R}\,U_0 \;\oplus\; U_0^\perp,
$$
where $\mathbb{R}U_0$ is the timelike line spanned by $U_0$ (on which the metric is positive-definite, $+1$) and $U_0^\perp$ is the spacelike rest space (on which the metric is negative-definite, signature $(0,3)$, i.e. Euclidean up to sign). This is a genuine direct sum because $U_0 \cdot U_0 = 1 \neq 0$, so the metric is non-degenerate on the line and the projection onto $U_0^\perp$ is well-defined.

The decomposition of a future timelike unit vector $U$ in this splitting is
$$
U = (U \cdot U_0)\,U_0 \;+\; \perp_{U_0}U,
$$
and the two summands are renamed: the coefficient of $U_0$ is the Lorentz factor $\Gamma = U \cdot U_0$, and the rest-space part, rescaled by $\Gamma^{-1}$, is the relative velocity $V$. The map $U \mapsto (\Gamma, V)$ is a chart on the **future unit hyperboloid** $\mathcal{H}^+ = \{U : U \cdot U = 1,\ U^0 > 0\}$ — the space of all possible four-velocities — adapted to the observer $U_0$. The hyperboloid is a model of three-dimensional hyperbolic space, and the relative velocity $V$ is a coordinate on it centred at $U_0$ (which sits at $V = 0$, $\Gamma = 1$). Changing the observer $U_0$ is an isometry of the hyperboloid (a Lorentz transformation), and the transformation law of $(\Gamma, V)$ under such a change is the relativistic velocity-composition law, the subject of [[Special Relativity VIII — Kinematics II, Change of Observer]]. This is the cleanest structural statement of the chapter: the Lorentz factor and relative velocity are hyperboloid coordinates centred at the observer.

---

# Relate to Other Fields / Compression

In hyperbolic geometry, the future unit hyperboloid $\{U \cdot U = 1,\ U^0 > 0\}$ with the induced metric is the **hyperboloid model** of $\mathbb{H}^3$, and the relative velocity is geodesic-normal-coordinate data on it. The hyperbolic distance from the observer's point $U_0$ to the particle's point $U$ is the **rapidity** $\varphi$, related to the Lorentz factor by $\Gamma = \cosh\varphi$ and to the speed by $|\mathbf V| = \tanh\varphi$ ([[Def - Rapidity]]). So $\Gamma = U \cdot U_0 = \cosh(\text{hyperbolic distance})$, the Lorentzian analogue of the Euclidean fact that the dot product of two unit vectors is the cosine of the angle between them. The minus signs turn $\cos$ into $\cosh$, the circle into a hyperbola, and the bounded angle into an unbounded rapidity — which is exactly why the speed is bounded by $c$ while the rapidity runs over all of $\mathbb{R}$.

In linear algebra, the construction is the orthogonal decomposition of a vector with respect to a non-null direction, specialised to an indefinite inner product. The novelty relative to the Euclidean case is that the "axis" $U_0$ has positive norm while the orthogonal complement has negative-definite norm, so the Pythagorean relation $\|U\|^2 = (\text{axial part})^2 + \|\text{orthogonal part}\|^2$ becomes $1 = \Gamma^2 - \Gamma^2|\mathbf V|^2$ with a *minus* sign on the orthogonal part — the source of every relativistic bound.

**True name:** The Lorentz factor is the Minkowski scalar product of the two four-velocities, $\Gamma = U \cdot U_0 = \cosh(\text{rapidity between them})$; the relative velocity is the rest-space part of the particle's four-velocity, normalised so that it is a rate of change of position with respect to the *observer's* clock. Operationally: to get $\Gamma$, dot the four-velocities; to get $V$, project the particle's four-velocity onto the observer's rest space and divide by $\Gamma$.

---

# Examples / Corollaries

**Is an instance — uniform linear motion seen by an inertial observer.** Let $\mathcal{O}$ be inertial with frame $(e_\alpha)$, $U_0 = e_0$, and let $\mathcal{P}$ move at constant speed $v$ along $e_1$: its four-velocity is $U = \Gamma(e_0 + v e_1)$ with $\Gamma = (1 - v^2)^{-1/2}$. Then $\Gamma = U \cdot U_0 = \Gamma(e_0 \cdot e_0) = \Gamma$ (consistent), the relative velocity is $V = v e_1$, and the decomposition $U = \Gamma(U_0 + V)$ holds with $|\mathbf V| = v < 1$. This is the case **Special Relativity II** treated by a Lorentz boost; here it is a scalar product.

**Is an instance — the observer measuring itself.** If $\mathcal{P} = \mathcal{O}$, then $U = U_0$, so $\Gamma = U_0 \cdot U_0 = 1$ and $V = 0$. An observer is always at rest relative to itself, with Lorentz factor one — the boundary case of the bound $\Gamma \geq 1$.

**Is NOT an instance — the four-vector $U - U_0$ as a "relative velocity".** One might guess the relative velocity is simply $U - U_0$. It is not: $U - U_0$ is not orthogonal to $U_0$ (its scalar product with $U_0$ is $\Gamma - 1 \neq 0$ in general), not spacelike, and its norm is not the speed. The correct relative velocity requires projecting onto the rest space and dividing by $\Gamma$. The difference $U - U_0$ mixes the time and space parts and is not what any ruler-and-clock measurement returns.

**Is NOT an instance — the proper velocity (celerity).** The rest-space vector $\Gamma V$ — the spatial part of the four-velocity *without* dividing by $\Gamma$ — is the **proper velocity** or celerity, the rate of change of position with respect to the *particle's* proper time. It is a legitimate and sometimes useful quantity, but it is not the relative velocity: it is unbounded (it tends to infinity as $|\mathbf V| \to 1$), whereas the relative velocity $V$ is bounded by $c$. Confusing the two drops or inserts a factor $\Gamma$ and is a common error.

**Corollary — the Lorentz factor is symmetric.** Because the scalar product is symmetric, $\Gamma = U \cdot U_0 = U_0 \cdot U$: the Lorentz factor of $\mathcal{P}$ relative to $\mathcal{O}$ equals that of $\mathcal{O}$ relative to $\mathcal{P}$ (when their worldlines cross). Each sees the other's clock running slow by the same factor — the reciprocity that drives the twin "paradox", and a direct consequence of the symmetry of the inner product.

**Corollary — the speed determines the Lorentz factor and conversely.** From $\Gamma^2(1 - |\mathbf V|^2) = 1$, knowing $|\mathbf V|$ gives $\Gamma = (1 - |\mathbf V|^2)^{-1/2}$ and knowing $\Gamma$ gives $|\mathbf V| = \sqrt{1 - \Gamma^{-2}}$. The two are interchangeable descriptions of the same relative motion; the Lorentz factor is the better one for dynamics (it is the energy per unit mass), the speed for everyday intuition.

**Calibration check.** If you have understood the definition you should be able to: (i) verify that $U = \Gamma(U_0 + V)$ with $V \cdot U_0 = 0$ and $U_0 \cdot U_0 = 1$ forces $\Gamma^2(1 - |\mathbf V|^2) = 1$ by expanding $U \cdot U = 1$; (ii) explain why $V$ must be divided by $\Gamma$ for it to be a velocity with respect to the observer's clock rather than the particle's; (iii) confirm that in the observer's frame $\Gamma$ is just the time component $u^0$ of the particle's four-velocity, and that this immediately gives $\Gamma \geq 1$ since $u^0 = \sqrt{1 + \sum (u^i)^2}$.

---

# Unlocked by This

> [!tip] Energy and Momentum Relative to an Observer *(from Relativistic Dynamics)*
> Attaching the rest mass $m$ to the decomposition $U = \Gamma(U_0 + V)$ gives the [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = mU$, whose component along $U_0$ is the energy $E = P \cdot U_0 = \Gamma m$ measured by $\mathcal{O}$, and whose rest-space part is the spatial momentum $\mathbf p = \Gamma m\mathbf V$. The Lorentz factor is therefore the energy per unit mass; the expansion $\Gamma m \approx m + \tfrac12 m|\mathbf V|^2$ is the rest energy plus the Newtonian kinetic energy. The whole of **Special Relativity XIII** is this page with a mass attached.

> [!tip] The Velocity-Composition Law *(from Change of Observer)*
> The relative velocity $V$ depends on the observer $U_0$; expressing the velocity relative to a second observer in terms of the velocity relative to the first, and their mutual velocity, is the relativistic [[Thm - Law of Velocity Composition|velocity-composition law]]. Geometrically it is the change of the hyperboloid coordinate $V$ under a change of base point $U_0$, and it is non-commutative — the residual rotation is the **Thomas rotation**, the seed of Thomas precession in **Special Relativity XVI**.

> [!tip] The Hyperbolic Geometry of Velocity Space *(from the Lorentz Group)*
> The set of all four-velocities is the future unit hyperboloid, a model of hyperbolic space $\mathbb{H}^3$, on which the relative velocity is a coordinate and the rapidity is the hyperbolic distance. The Lorentz group acts on this hyperboloid as its full isometry group, $\mathrm{Isom}(\mathbb{H}^3) \cong SO^+(1,3)$ — the bridge that makes the structure of relative velocities a chapter of non-Euclidean geometry, developed in **Special Relativity IX** and **Special Relativity X**.

---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, so velocities satisfy $|v| < 1$. The **Lorentz factor** is $\gamma = \gamma_v = (1 - v^2)^{-1/2}$ (with $c$ restored, $\gamma = (1 - v^2/c^2)^{-1/2}$). The **rapidity** is denoted $\varphi$ (also $\phi$ or $\psi$ when several appear). A boost along $x$ of rapidity $\varphi$ is written $\Lambda[\varphi]$; the same boost by velocity $v$ is $\Lambda[v]$. The hyperbolic functions are $\cosh\varphi = \tfrac12(e^\varphi + e^{-\varphi})$, $\sinh\varphi = \tfrac12(e^\varphi - e^{-\varphi})$, $\tanh\varphi = \sinh\varphi/\cosh\varphi$, satisfying $\cosh^2\varphi - \sinh^2\varphi = 1$. Full registry on [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group]].

---

# Axiom Motivation

The velocity-addition law $u = (u' + v)/(1 + u'v)$ is correct but ugly: it is nonlinear, it has to be memorised, and composing three or four boosts by iterating it is a chore. The motivation for rapidity is to find the *natural* coordinate on the set of boosts — the one in which the group law is as simple as it can possibly be, namely ordinary addition. Such a coordinate must exist, and seeing why it must exist is the whole point.

The clue is the rotation analogy. A boost is a [[Def - Boosts as Hyperbolic Rotations|hyperbolic rotation]] of the $(t, x)$-plane, structurally identical to an ordinary rotation of the $(x, y)$-plane with circular functions replaced by hyperbolic ones. For ordinary rotations we know the natural coordinate: it is the **angle** $\theta$, and its decisive property is that *angles add*, $R[\theta_1]R[\theta_2] = R[\theta_1 + \theta_2]$. This additivity is not automatic in just any parametrisation — it works *because* the angle is the arc length along the unit circle, the canonical coordinate on the one-parameter group of rotations. The boost group is also one-parameter (for a fixed direction), so it too has a canonical additive coordinate. Rapidity is that coordinate: the "hyperbolic angle", the arc length along the unit hyperbola.

Now the question is which function of $v$ to call $\varphi$. The constraint is that the boost matrix, written in $\varphi$, should look exactly like a rotation matrix with $\cos, \sin$ replaced by $\cosh, \sinh$:
$$
\Lambda[\varphi] = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}.
$$
Comparing with the boost in velocity form, $\Lambda[v] = \gamma\begin{pmatrix} 1 & v \\ v & 1 \end{pmatrix}$, forces $\gamma = \cosh\varphi$ and $\gamma v = \sinh\varphi$, hence $v = \tanh\varphi$. These three relations are not three independent choices — any one of them defines $\varphi$ and the other two follow from $\cosh^2 - \sinh^2 = 1$ together with $\gamma^2(1 - v^2) = 1$. So the definition is forced the moment you ask for the boost to be a hyperbolic rotation.

Why is *this* the right definition and not, say, $\varphi = v$ itself or $\varphi = \gamma$? Because neither of those adds. If you parametrised boosts by velocity, composition would be the messy $(u' + v)/(1 + u'v)$; if you parametrised by $\gamma$, composition would be messier still. The function $v = \tanh\varphi$ is singled out by the addition formula for $\tanh$:
$$
\tanh(\varphi_1 + \varphi_2) = \frac{\tanh\varphi_1 + \tanh\varphi_2}{1 + \tanh\varphi_1\tanh\varphi_2},
$$
which is *exactly* the relativistic velocity-addition law. Rapidity is the unique (up to scale) parametrisation in which boosts compose additively, and the velocity-addition law is nothing but the $\tanh$ addition formula in disguise. The ugliness of velocity addition was an artefact of using the wrong coordinate.

There is a second, equally forcing motivation: the *range*. Velocity is confined to the open interval $(-1, 1)$ — you cannot reach the speed of light. This makes velocity an awkward coordinate, bounded and with the physically crucial endpoint $v = \pm 1$ unreachable. Rapidity unfolds this interval onto the whole real line: as $v \to 1^-$, $\varphi = \tanh^{-1}v \to +\infty$. The "you cannot reach $c$" statement becomes the transparent "$c$ is rapidity infinity", and the unboundedness of $\cosh$ (against the boundedness of $\cos$) is the precise reflection of the non-compactness of the boost group against the compactness of the rotation group.

---

# The Definition

The **rapidity** $\varphi$ of a Lorentz boost with velocity $v$ (with $c = 1$, so $|v| < 1$) is defined by any one of the three equivalent relations
$$
v = \tanh\varphi,
\qquad
\gamma = \cosh\varphi,
\qquad
\gamma v = \sinh\varphi,
$$
where $\gamma = (1 - v^2)^{-1/2}$ is the [[Def - The Lorentz Transformation|Lorentz factor]]. Equivalently $\varphi = \tanh^{-1}v = \tfrac12 \ln\!\big(\tfrac{1+v}{1-v}\big)$, a map carrying the velocity interval $(-1, 1)$ bijectively onto the real line $\mathbb{R}$. With $c$ restored, $v/c = \tanh\varphi$ and $\gamma = \cosh\varphi$.

In terms of rapidity the **boost matrix** along $x$ is the [[Def - Boosts as Hyperbolic Rotations|hyperbolic rotation]]
$$
\Lambda[\varphi] = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}
\quad\text{on } (t, x),
$$
extended by the identity on $(y, z)$. Its defining and characteristic property is that **rapidities add** for collinear boosts:
$$
\Lambda[\varphi_1]\,\Lambda[\varphi_2] = \Lambda[\varphi_1 + \varphi_2],
$$
so the boost group along a fixed direction is the additive group $(\mathbb{R}, +)$, parametrised by $\varphi$.

(The sign convention here is the *active* one, matching the boost-as-hyperbolic-rotation matrix with $+\sinh\varphi$ off the diagonal: $\Lambda[\varphi]$ carries the coordinates of $S'$ to those of $S$, with $x = \gamma(x' + vt')$. Tong writes the *passive* boost $S \to S'$ with $-\sinh\varphi$; the two differ only by the sign of $v$, i.e. $\varphi \to -\varphi$.)

---

# Categorical / Structural Definition

Rapidity is the **canonical coordinate (logarithmic chart) on the one-parameter subgroup of boosts along a fixed axis**. That subgroup is a one-dimensional connected Lie group, hence isomorphic to $(\mathbb{R}, +)$; rapidity is the isomorphism. Concretely, the boosts along $x$ form a one-parameter subgroup $t \mapsto \exp(\varphi K)$ of $SO^+(1,3)$, where $K = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ (on the $(t,x)$ block) is the **boost generator** in the [[Def - Lie Algebra of the Lorentz Group|Lie algebra]] $\mathfrak{so}(1,3)$. Because $K^2 = I$ on the $(t,x)$ block, the exponential series sums to hyperbolic functions,
$$
\exp(\varphi K) = \cosh\varphi\, I + \sinh\varphi\, K = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix},
$$
and additivity $\exp(\varphi_1 K)\exp(\varphi_2 K) = \exp((\varphi_1 + \varphi_2)K)$ is automatic because all the matrices commute (same generator). So "$\varphi$ is the additive parameter" is the Lie-theoretic statement that $\varphi$ is the coordinate in which the one-parameter subgroup $\exp(\varphi K)$ is parametrised by its own Lie-algebra direction — the exponential coordinate.

This is the precise sense in which rapidity is to a boost as angle is to a rotation. The rotation generator $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has $J^2 = -I$, so $\exp(\theta J) = \cos\theta\, I + \sin\theta\, J$ sums to *circular* functions and the angle is periodic ($\theta \sim \theta + 2\pi$, the group is the circle $SO(2)$). The boost generator has $K^2 = +I$, so $\exp(\varphi K)$ sums to *hyperbolic* functions and the rapidity is non-periodic ($\varphi$ ranges over all of $\mathbb{R}$, the group is the line). The single sign difference $J^2 = -I$ versus $K^2 = +I$ — itself a shadow of the metric signature — is the whole difference between the compact circle of rotations and the non-compact line of boosts.

---

# Relate to Other Fields / Compression

Rapidity is the **hyperbolic-angle / arc-length parameter on the unit hyperbola** $t^2 - x^2 = 1$, exactly as the angle is the arc-length parameter on the unit circle $x^2 + y^2 = 1$. A point on the unit hyperbola is $(\cosh\varphi, \sinh\varphi)$, and $\varphi$ is twice the hyperbolic-sector area it subtends — the literal "hyperbolic angle" of classical geometry. The set of physical four-velocities is a sheet of this hyperboloid (in $3+1$ dimensions, $V \cdot V = 1$), so rapidity is **distance in the hyperbolic geometry of velocity space**: the velocity space of special relativity is the hyperbolic space $\mathbb{H}^3$, and rapidity is its radial distance coordinate. This is why composing non-collinear boosts is governed by hyperbolic trigonometry and produces the Thomas rotation — it is the angular defect of a hyperbolic triangle.

**True name:** rapidity is **"the additive boost parameter"** — the coordinate in which boosts compose by $+$ instead of by the velocity-addition law. When a problem asks you to compose, iterate, or invert boosts, do not reach for $(u' + v)/(1 + u'v)$; convert each velocity to its rapidity $\varphi = \tanh^{-1}v$, add (or subtract for an inverse, since $\Lambda[\varphi]^{-1} = \Lambda[-\varphi]$), and convert back with $v = \tanh\varphi$. The nonlinear group law becomes a straight sum.

In particle physics, rapidity (and its experimental cousin, *pseudorapidity*) is the standard longitudinal coordinate precisely because of additivity: under a boost along the beam axis, the rapidity of every particle shifts by the *same* constant, so rapidity *differences* are boost-invariant. A detector built around a collision uses rapidity rather than velocity or angle for exactly the reason this page gives: the boost group acts on it by translation.

---

# Examples / Corollaries

**Is an instance — a slow boost.** For $v = 0.1$ (a tenth of light speed), $\varphi = \tanh^{-1}(0.1) \approx 0.1003$. At small $v$, $\varphi \approx v$ (since $\tanh^{-1}v = v + v^3/3 + \cdots$), so rapidity and velocity nearly coincide in the Newtonian regime — the curve $\varphi(v)$ leaves the origin with unit slope. This is why Galilean velocity addition ($u \approx u' + v$) is the small-rapidity limit of $\varphi_1 + \varphi_2$.

**Is an instance — composing two equal boosts.** Two collinear boosts each of velocity $v = 0.5$ have $\varphi = \tanh^{-1}(0.5) \approx 0.5493$ each; composed, the total rapidity is $2\varphi \approx 1.0986$, and the combined velocity is $\tanh(1.0986) = 0.8$ — not $1.0$, as the naive sum $0.5 + 0.5$ would give. The velocity-addition formula reproduces this: $(0.5 + 0.5)/(1 + 0.25) = 1/1.25 = 0.8$. Adding rapidities and adding velocities give the same answer; rapidity just makes the addition trivial.

**Is an instance — the Doppler factor.** The combination $k = e^\varphi = \cosh\varphi + \sinh\varphi = \gamma(1 + v)$ (for motion along the line of sight) is the **relativistic Doppler shift factor** and the eigenvalue of the boost on a null direction. Because $\varphi$ adds, $k$ *multiplies*: composing boosts multiplies their Doppler factors, $k_1 k_2 = e^{\varphi_1}e^{\varphi_2} = e^{\varphi_1 + \varphi_2}$. The Doppler factor is the exponential of the rapidity.

**Is NOT an instance — velocity is not a rapidity.** The velocity $v$ itself is *not* an additive parameter: $\Lambda[v_1]\Lambda[v_2] \neq \Lambda[v_1 + v_2]$ in general (it equals $\Lambda\big[(v_1 + v_2)/(1 + v_1 v_2)\big]$). Velocity is the *wrong* coordinate on the boost group — bounded, with a nonlinear composition law. The contrast is the whole motivation for introducing $\varphi$.

**Corollary — the boost group along a line is $(\mathbb{R}, +)$.** Since $\varphi \mapsto \Lambda[\varphi]$ is a bijection from $\mathbb{R}$ to the collinear boosts and turns $+$ into matrix multiplication, the boosts along a fixed direction form a one-parameter subgroup isomorphic to the additive reals. In particular the inverse of $\Lambda[\varphi]$ is $\Lambda[-\varphi]$, and the identity is $\Lambda[0]$.

**Calibration check.** You should be able to: (1) derive $v = \tanh\varphi$ from $\gamma = \cosh\varphi$ alone, using $\gamma^2(1 - v^2) = 1$ and $\cosh^2 - \sinh^2 = 1$; (2) show $\tanh(\varphi_1 + \varphi_2)$ equals the velocity-addition formula by expanding the hyperbolic addition law; (3) explain why $\varphi \to \infty$ corresponds to $v \to 1$ and what that says about reaching the speed of light.

---

# Unlocked by This

> [!tip] Boosts as Hyperbolic Rotations and the Lie Algebra *(from the Lorentz Group as a Lie Group)*
> Rapidity is the canonical coordinate along the boost generator $K$ in $\mathfrak{so}(1,3)$, so a finite boost is $\exp(\varphi K)$ — the exponential map of [[Def - Lie Algebra of the Lorentz Group|the Lorentz Lie algebra]] evaluated on a boost direction. Writing rotations as $\exp(\theta J)$ and boosts as $\exp(\varphi K)$ side by side is the cleanest entry to the Lie theory of [[Special Relativity X — The Lorentz Group as a Lie Group]]; the commutator $[K_i, K_j] = -\epsilon_{ijk}J_k$ (a boost-boost commutator is a rotation) is the algebraic seed of the Thomas rotation.

> [!tip] Hyperbolic Geometry of Velocity Space *(from the Structure of the Lorentz Group)*
> The physical velocities, parametrised by rapidity, form the hyperbolic space $\mathbb{H}^3$ with rapidity as radial distance. Non-collinear velocity composition is governed by the hyperbolic law of cosines, and the failure of associativity of velocity addition is a **gyrogroup** structure — the velocities form a gyrocommutative gyrogroup, whose defect is precisely the **Thomas–Wigner rotation**. See [[Special Relativity IX — The Lorentz Group — Structure and Classification]].

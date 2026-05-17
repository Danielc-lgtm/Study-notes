---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, so a velocity $v$ satisfies $|v| < 1$. The Lorentz factor is $\gamma = (1-v^2)^{-1/2}$. Rapidity is denoted $\varphi$ (also $\phi, \psi$). A boost along $x$, restricted to the $(t,x)$-plane, is the $2\times 2$ matrix $\Lambda[v]$ or $\Lambda[\varphi]$. The hyperbolic functions: $\cosh\varphi = \tfrac12(e^\varphi+e^{-\varphi})$, $\sinh\varphi = \tfrac12(e^\varphi-e^{-\varphi})$, $\tanh\varphi = \sinh\varphi/\cosh\varphi$, with $\cosh^2\varphi - \sinh^2\varphi = 1$. Full registry on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Axiom Motivation

The [[Def - The Lorentz Transformation|boost]] $\Lambda[v]$, parametrised by velocity, has an ugly composition law. Compose two collinear boosts of velocities $v_1$ and $v_2$ and the result is a boost — the [[Def - The Lorentz Group|Lorentz group]] is closed — but its velocity is the awkward $(v_1+v_2)/(1+v_1v_2)$, not $v_1+v_2$. Velocity is a *bad coordinate* on the boost subgroup: the group operation, written in velocity, is nonlinear.

This is a familiar situation. The rotations of a plane also form a one-parameter group, and the rotation matrix can be parametrised by all sorts of quantities — but only one parametrisation makes composition trivial: the **angle**. Two rotations by angles $\theta_1, \theta_2$ compose to a rotation by $\theta_1+\theta_2$. The angle is the *good* coordinate, the one in which the group law is just addition, because the map $\theta \mapsto R[\theta]$ is a group homomorphism from $(\mathbb{R},+)$ onto the rotation subgroup.

The desideratum for boosts is the same: find the coordinate $\varphi$ in which the boost subgroup is parametrised so that $\varphi \mapsto \Lambda[\varphi]$ is a homomorphism from $(\mathbb{R},+)$ — so that boosts compose by *adding* $\varphi$. We can see what $\varphi$ must be from the boost matrix itself. Written out, $\Lambda[v] = \begin{pmatrix}\gamma & \gamma v\\\gamma v & \gamma\end{pmatrix}$ (with the sign convention of the inverse boost; either sign works for this argument). The defining property $\Lambda^{\mathsf T}\eta\Lambda = \eta$ forces $\gamma^2 - (\gamma v)^2 = 1$. This is *exactly* the hyperbolic identity $\cosh^2\varphi - \sinh^2\varphi = 1$. So there is a unique $\varphi$ with
$$\gamma = \cosh\varphi, \qquad \gamma v = \sinh\varphi,$$
and dividing, $v = \tanh\varphi$. In this parametrisation the boost matrix becomes $\begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}$ — the rotation matrix with $\cos,\sin$ replaced by $\cosh,\sinh$. And the hyperbolic angle-addition formulas $\cosh(\varphi_1+\varphi_2) = \cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2$, etc., are precisely the statement $\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1+\varphi_2]$. Rapidity is the angle of the hyperbolic rotation.

Why $\varphi$ and not some other monotone function of $v$? Because $\varphi$ is the *unique* one (up to scale) making composition additive — it is the canonical coordinate on the one-parameter subgroup, the analogue of arc length along the group. A bonus appears at the edges: as $v$ ranges over the physical interval $(-1,1)$, $\varphi = \tanh^{-1}v$ ranges over all of $\mathbb{R}$. Velocity is trapped below the speed of light; rapidity is unconstrained. The light-speed barrier, awkward to see in $v$, becomes the simple statement "$\varphi = \infty$" in rapidity.

---

# The Definition

For a relative velocity $v$ with $|v| < 1$ (with $c$: $|v| < c$), the **rapidity** $\varphi$ of the corresponding boost is
$$
\boxed{\quad \varphi \;=\; \tanh^{-1} v \qquad\Longleftrightarrow\qquad v = \tanh\varphi \quad}
$$
(with $c$: $\varphi = \tanh^{-1}(v/c)$). Equivalently, $\varphi$ is defined by
$$\gamma = \cosh\varphi, \qquad \gamma v = \sinh\varphi,$$
which are consistent because the boost condition $\gamma^2 - (\gamma v)^2 = 1$ is the identity $\cosh^2\varphi - \sinh^2\varphi = 1$. In rapidity variables, a boost along $x$ acts on $(t,x)$ by the **hyperbolic rotation matrix**
$$
\Lambda[\varphi] = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix},
\qquad
\begin{aligned} t' &= t\cosh\varphi + x\sinh\varphi,\\ x' &= t\sinh\varphi + x\cosh\varphi. \end{aligned}
$$
(With the opposite sign convention, $\sinh\varphi \to -\sinh\varphi$, corresponding to $v \to -v$.) The defining property of rapidity is **additivity**: collinear boosts compose by adding rapidities,
$$\Lambda[\varphi_1]\,\Lambda[\varphi_2] = \Lambda[\varphi_1 + \varphi_2].$$
As $v$ runs over $(-1,1)$, $\varphi$ runs over all of $\mathbb{R}$; the map $\varphi \mapsto \Lambda[\varphi]$ is a group isomorphism $(\mathbb{R},+) \xrightarrow{\sim} SO^+(1,1)$.

---

# Relate to Other Fields / Compression

Rapidity is to a boost exactly what an angle is to a rotation. The rotation group $SO(2)$ of the plane is parametrised by $\theta$ with $R[\theta_1]R[\theta_2] = R[\theta_1+\theta_2]$; the boost group $SO^+(1,1)$ is parametrised by $\varphi$ with $\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1+\varphi_2]$. The two are the same construction — the **canonical coordinate on a one-parameter Lie subgroup**, the parameter in which the exponential map $\varphi \mapsto \exp(\varphi K)$ (for $K$ the boost generator) becomes the identity reparametrisation. The one structural difference is the range: $SO(2)$ is compact, a circle, so $\theta$ wraps with period $2\pi$; $SO^+(1,1)$ is non-compact, isomorphic to the line $\mathbb{R}$, so $\varphi$ runs off to infinity without returning. Compactness versus non-compactness is the deep reason a rotation angle is periodic while a rapidity is not — and the non-compactness is why $v = \tanh\varphi$ saturates at $\pm 1$ rather than oscillating.

In hyperbolic geometry, rapidity is a genuine *distance*. The physical four-velocities sit on a hyperboloid $V\cdot V = 1$, which carries the metric of hyperbolic space; the rapidity difference between two four-velocities is the hyperbolic distance between the corresponding points. Relativistic velocity addition is then literally the law of addition of displacements along a geodesic of hyperbolic space — and the failure of velocities to add linearly is the hyperbolic-geometry fact that the space is curved.

---

# Examples / Corollaries

**Is an instance — small rapidity is small velocity.** For $\varphi \ll 1$, $\tanh\varphi \approx \varphi$, so $v \approx \varphi$: at low speeds rapidity and velocity coincide, and boosts approximately add velocities — the Galilean limit. Rapidity and velocity differ only when the speed is relativistic.

**Is an instance — light is rapidity infinity.** As $v \to 1$, $\varphi = \tanh^{-1}v \to +\infty$. The speed of light corresponds to infinite rapidity. This is why no finite chain of boosts reaches $c$: adding finitely many finite rapidities gives a finite rapidity, hence a velocity strictly below $1$.

**Is an instance — the boost matrix is a hyperbolic rotation.** $\Lambda[\varphi] = \begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}$ has $\det = \cosh^2\varphi - \sinh^2\varphi = 1$ and satisfies $\Lambda^{\mathsf T}\eta\Lambda = \eta$ — a direct check, the hyperbolic analogue of $R^{\mathsf T}R = I$ for rotations. It is the general element of $SO^+(1,1)$.

**Is NOT an instance — rapidity does not add for non-collinear boosts.** The clean additivity $\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1+\varphi_2]$ holds only when the two boosts are along the *same* direction. Two boosts in different directions compose to a boost *plus a rotation* (the Wigner rotation), and the rapidities do not simply add. Rapidity linearises the *one-dimensional* boost subgroup only.

**Corollary — velocity addition is rapidity addition.** Since $v = \tanh\varphi$ and rapidities add, the combined velocity of two collinear boosts is $\tanh(\varphi_1+\varphi_2)$, which the hyperbolic tangent addition formula expands to $(v_1+v_2)/(1+v_1v_2)$. This is the entire content of [[Thm - Relativistic Velocity Addition]] — the messy formula is just $\tanh$ of a sum.

**Corollary — the inverse boost has negated rapidity.** $\Lambda[\varphi]^{-1} = \Lambda[-\varphi]$, since $\varphi + (-\varphi) = 0$ gives the identity. Inverting a boost flips the sign of the rapidity, hence (via $\tanh$) the sign of the velocity — consistent with the inverse Lorentz transformation having $v \to -v$.

---

# Unlocked by This

> [!tip] Relativistic Velocity Addition *(from §1.2)*
> Because collinear boosts compose by adding rapidities, the relativistic velocity-addition law ([[Thm - Relativistic Velocity Addition]]) is simply $\tanh(\varphi_1+\varphi_2)$. Rapidity converts the nonlinear group law of boosts into ordinary addition.

> [!tip] The Boost Generator and the Lie Algebra *(from QFT and Gauge Theory)*
> Writing $\Lambda[\varphi] = \exp(\varphi K)$ identifies the **boost generator** $K = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, an element of the Lie algebra $\mathfrak{so}(1,3)$. Rapidity is the canonical parameter along the one-parameter subgroup $\exp(\varphi K)$, and the commutators of boost and rotation generators define the algebra whose representations classify particle **spin**.

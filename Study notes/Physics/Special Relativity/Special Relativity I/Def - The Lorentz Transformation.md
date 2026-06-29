---
type: definition
subject: special-relativity
prereqs:
  - "Def - Inertial Frame and the Postulates of Special Relativity"
  - "Def - Galilean Spacetime and Its Failure"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ throughout, giving the $c$-restored form wherever it aids recognition. Two inertial frames $S$ and $S'$ have coordinates $(t,x,y,z)$ and $(t',x',y',z')$, with $S'$ moving at velocity $v$ along the common $x$-axis and origins coinciding at $t = t' = 0$. The **Lorentz factor** is $\gamma = \gamma_v = (1 - v^2)^{-1/2}$ (with $c$: $(1 - v^2/c^2)^{-1/2}$). We write four-component coordinate tuples as $x^\mu$, $\mu = 0,1,2,3$, with $x^0 = t$ (or $ct$); $\Lambda$ denotes the transformation as a matrix, with components $\Lambda^\mu{}_\nu$. Spatial three-vectors are bold. Full registry on [[Special Relativity I — Postulates and Lorentz Transformations]].

---

# Axiom Motivation

The Lorentz transformation is not guessed and not postulated — it is *forced*, and the motivation is to see that it is the only law that can do its job. The job is precise: relate the coordinates of an event in two inertial frames in a way compatible with both [[Def - Inertial Frame and the Postulates of Special Relativity|postulates]], replacing the [[Def - Galilean Spacetime and Its Failure|Galilean transformation]] that the constancy of light has just demolished. Three demands, each from physics, narrow the candidate down to a single formula, and understanding the three demands is understanding the transformation.

The first demand is **linearity**, and it comes from the law of inertia. A free particle moves in a straight line at constant velocity in any inertial frame; its worldline is a straight line in the $(t,x)$ plane of $S$ and must remain a straight line in $S'$. A coordinate map that sends every straight line to a straight line (and the origin to the origin, since the frames coincide at the start) is, by an elementary theorem of affine geometry, *linear*. So $x' = \alpha_1 x + \alpha_2 t$ and $t' = \alpha_3 x + \alpha_4 t$ with constant coefficients. Drop linearity — allow the map to bend straight lines — and the law of inertia would fail in $S'$, contradicting that $S'$ is inertial. This is why the transformation is a matrix and not something worse; it is also why special relativity, unlike general relativity, needs no curvature: the coordinate changes are *global* linear maps with constant Jacobian.

The second demand fixes most of the coefficients: the **origin of $S'$ moves at $v$ in $S$**. The spatial origin of $S'$ is the locus $x' = 0$; in $S$ this locus is the worldline $x = vt$. So $x' = 0$ exactly when $x = vt$, which forces the spatial equation into the form $x' = \gamma(x - vt)$ for some coefficient $\gamma$ — the factor $(x - vt)$ vanishes precisely on the moving origin, and an overall scale $\gamma$ (possibly depending on $v$) remains free. This single requirement collapses the two spatial coefficients $\alpha_1, \alpha_2$ into one unknown $\gamma$. The corresponding inverse, viewed from $S'$ in which $S$ moves backwards at $-v$, gives $x = \gamma(x' + vt')$ with the *same* $\gamma$, by the next demand.

The third demand — the principle of relativity through **isotropy and reciprocity** — pins $\gamma$ to be an *even* function of $v$, $\gamma_v = \gamma_{-v}$. Two arguments give it. Rotational invariance: $\gamma$ can depend only on the magnitude $v^2 = \mathbf{v}\cdot\mathbf{v}$, not on the direction of motion, because no direction in space is preferred. Or, more carefully, consider the mirror-image frames $\tilde S, \tilde S'$ with $\tilde x = -x$, $\tilde x' = -x'$: relative to $\tilde S'$ the frame $\tilde S$ moves at $-v$, and running the same argument yields $\tilde x' = \gamma_{-v}(\tilde x + v\tilde t)$, which compared with the original forces $\gamma_v = \gamma_{-v}$ (see [[Ex - Reciprocity and the evenness of the Lorentz factor]]). Evenness is what makes the forward and inverse transformations have the same $\gamma$, which is the principle of relativity made quantitative: neither frame is special, so the relation between them is symmetric under swapping their roles and reversing $v$.

With these three, only the *value* of $\gamma$ is unknown, and the **second postulate** supplies it. A light ray $x = t$ in $S$ must be $x' = t'$ in $S'$. Substituting the form $x' = \gamma(x - vt)$ and its inverse into these two light-trajectory conditions yields two equations, $t' = \gamma(1 - v)t$ and $t = \gamma(1 + v)t'$; multiplying them gives $1 = \gamma^2(1 - v^2)$, hence $\gamma = (1 - v^2)^{-1/2}$. The constancy of light is the one numerical input, and it determines $\gamma$ completely. The time transformation $t' = \gamma(t - vx)$ then falls out by substituting the now-known spatial equation back into the inverse and solving — the clock equation was "already lurking", as Tong puts it, in the consistency of the two spatial relations.

It is worth dwelling on what each ingredient would cost if removed, because that is the test of whether the definition is forced. Without linearity, free particles curve in $S'$. Without the moving-origin condition, $S'$ is not actually moving at $v$. Without evenness of $\gamma$, the forward and inverse transformations disagree and one frame is secretly preferred — a violation of Postulate 1. Without the light condition, $\gamma$ is undetermined and *any* $\gamma_v$ gives a one-parameter family of "transformations" (these are the most general transformations compatible with the relativity principle alone — they fix some invariant speed, possibly infinite); Postulate 2 selects the member with invariant speed exactly $c$. Set $\gamma = 1$ — equivalently take the invariant speed to infinity — and you recover the [[Def - Galilean Spacetime and Its Failure|Galilean transformation]]. So the Lorentz transformation sits at the unique value of $\gamma$ forced by a *finite* universal speed, and the Galilean transformation is its $c \to \infty$ degeneration.

---

# The Definition

The **Lorentz transformation** (a Lorentz **boost** along $x$) relating two inertial frames $S$, $S'$ with $S'$ moving at velocity $v$ along the common $x$-axis, origins coinciding at $t = t' = 0$, is the linear coordinate change (with $c = 1$)
$$
x' = \gamma(x - vt), \qquad
t' = \gamma(t - vx), \qquad
y' = y, \qquad
z' = z,
\qquad \gamma = \frac{1}{\sqrt{1 - v^2}}.
$$
With $c$ restored, writing $x^0 = ct$, it is most symmetric as
$$
x' = \gamma\!\left(x - \frac{v}{c}\,ct\right), \qquad
ct' = \gamma\!\left(ct - \frac{v}{c}\,x\right), \qquad
y' = y, \qquad
z' = z,
\qquad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}.
$$
In matrix form, with the column $(ct, x, y, z)^{\mathsf T}$,
$$
\begin{pmatrix} ct' \\ x' \\ y' \\ z' \end{pmatrix}
=
\begin{pmatrix}
\gamma & -\gamma v/c & 0 & 0 \\
-\gamma v/c & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix} ct \\ x \\ y \\ z \end{pmatrix}.
$$
The **inverse** is obtained by replacing $v$ with $-v$ (the principle of relativity at work): $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$, $y = y'$, $z = z'$. The transformation reduces to the [[Def - Galilean Spacetime and Its Failure|Galilean transformation]] when $|v| \ll 1$ (so $\gamma \to 1$), and $\gamma$ becomes imaginary for $|v| > c$, which is the statement that no inertial frame can move faster than light relative to another.

The matrix is the unique linear map compatible with both postulates: linearity from inertia, the off-diagonal structure from the moving origin, the symmetry $\gamma_v = \gamma_{-v}$ from isotropy, and the value $\gamma = (1-v^2)^{-1/2}$ from the constancy of light. Its full justification and uniqueness are the content of [[Thm - Uniqueness of the Lorentz Transformation from the Postulates]]. A general Lorentz transformation is a composition of such boosts (in arbitrary directions) with ordinary spatial rotations; the complete set forms the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$, and adjoining translations gives the [[Def - The Poincaré Group|Poincaré group]].

---

# Categorical / Structural Definition

The structural definition is the one that generalises and explains the group law: **a Lorentz transformation is a linear map of spacetime that preserves the spacetime interval.** Defining $\Delta s^2 = \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ (see [[Def - The Spacetime Interval]]), a linear map $\Lambda$ is a Lorentz transformation precisely when it leaves $\Delta s^2$ unchanged for every pair of events — equivalently, in matrix form, when
$$
\Lambda^{\mathsf T}\,\eta\,\Lambda = \eta, \qquad \eta = \mathrm{diag}(1,-1,-1,-1).
$$
This characterisation is logically downstream of the postulates (it is proved equivalent to them in [[Thm - Invariance of the Spacetime Interval]]) but conceptually primary: from it the boost formula is *recovered* as one special solution, while closure under composition, the existence of inverses, and the connection to ordinary rotations all become automatic. The composite of two interval-preserving maps preserves the interval, so the Lorentz transformations form a group with no further checking; that group is the [[Def - The Lorentz Group|Lorentz group]], the isometry group of the indefinite form $\eta$, exactly as the orthogonal group $O(3)$ is the isometry group of the Euclidean form. A boost is then a "rotation between space and time": parametrised by [[Def - Rapidity|rapidity]] $\varphi$ with $v = \tanh\varphi$, the boost matrix is
$$
\begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix},
$$
formally a rotation with trigonometric functions replaced by hyperbolic ones, and collinear boosts compose by *adding* rapidities — the structural fact behind [[Thm - Relativistic Velocity Addition|relativistic velocity addition]].

---

# Relate to Other Fields / Compression

A Lorentz transformation is, mathematically, the simplest interesting object in several fields at once. To **linear algebra** it is a change between *pseudo-orthonormal bases* of an indefinite inner-product space: where an orthogonal matrix preserves $\sum x_i^2$, a Lorentz matrix preserves $t^2 - \sum x_i^2$, and the only difference is the signature of the form. To **multivariate calculus** it is a linear change of coordinates with *constant* Jacobian equal to the matrix $\Lambda$ itself — there is no position dependence, which is precisely why special relativity needs no differential geometry while general relativity does. To **Lie theory** it is an element of the group $O(1,3)$, and the boost is the exponential of a Lie-algebra generator with rapidity as the canonical coordinate along the one-parameter subgroup.

**True name:** the operational form to *compute* with is the boost formula $x' = \gamma(x - vt)$, $t' = \gamma(t - vx)$; the form to *think* with is "the linear map that preserves the interval $\Delta s^2$." The first is one boost in one direction and hides the structure; the second explains why the transformations form a group, why a boost is a hyperbolic rotation, and why the matrix condition is $\Lambda^{\mathsf T}\eta\Lambda = \eta$. When you read "Lorentz transformation", picture the interval and the maps that leave it alone, not the boost matrix.

---

# Examples / Corollaries

**Is an instance — the boost itself.** With $v = 0.6$ (so $\gamma = 1.25$), an event at $(t,x) = (0, 1)$ in $S$ maps to $(t', x') = (1.25(0 - 0.6\cdot 1),\ 1.25(1 - 0.6\cdot 0)) = (-0.75,\ 1.25)$ in $S'$. The event acquires a nonzero time coordinate in $S'$ even though it was at $t = 0$ in $S$ — this is the relativity of simultaneity, an immediate consequence of $t' = \gamma(t - vx)$ depending on $x$.

**Is an instance — a spatial rotation.** A pure rotation of the $x,y$ axes (mixing space with space, leaving $t$ alone) is also a Lorentz transformation: it preserves $\Delta s^2$ because it preserves $\Delta x^2 + \Delta y^2$ and fixes $\Delta t$. The full Lorentz group is generated by boosts and rotations together; a boost is the genuinely new, time-mixing ingredient.

**Is NOT an instance — the Galilean transformation.** The map $x' = x - vt$, $t' = t$ is *not* a Lorentz transformation: it does not preserve the interval ($\Delta t'^2 - \Delta x'^2 = \Delta t^2 - (\Delta x - v\Delta t)^2 \ne \Delta t^2 - \Delta x^2$), and it sends light at $c$ to light at $c - v$. It is the $\gamma \to 1$ approximation, valid only at low speed.

**Is NOT an instance — a generic linear map with $\det = 1$.** Not every unit-determinant $2\times 2$ matrix is a boost; for example $\begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix}$ has determinant $1$ but does not satisfy $\Lambda^{\mathsf T}\eta\Lambda = \eta$ (it scales $t$ and $x$ independently, changing the interval). Being a Lorentz transformation is the *interval-preserving* condition, strictly stronger than unit determinant.

**Corollary — the speed of light is a fixed point.** A worldline with $x = t$ (speed $1$) maps to $x' = \gamma(t - vt) = \gamma t(1 - v)$ and $t' = \gamma(t - vt) = \gamma t(1 - v)$, so $x' = t'$ (speed $1$ again). Light has the same speed in both frames — the second postulate, recovered as a check on the formula. No worldline with $|u| < 1$ maps to one with $|u| \ge 1$.

**Corollary — composition of collinear boosts is a boost.** Two boosts along the same axis, velocities $v_1$ and $v_2$, compose to a single boost of velocity $(v_1 + v_2)/(1 + v_1 v_2)$, not $v_1 + v_2$; in [[Def - Rapidity|rapidity]] this is simply $\varphi_1 + \varphi_2$. This is [[Thm - Relativistic Velocity Addition|relativistic velocity addition]], and it shows the boosts along one axis form a one-parameter subgroup isomorphic to $(\mathbb{R}, +)$.

**Calibration check.** You have understood the transformation if you can: (1) write the boost and its inverse from memory and confirm the inverse is "$v \to -v$"; (2) verify in one line that the light ray $x = t$ maps to $x' = t'$; and (3) check that setting $\gamma = 1$ and dropping the $vx$ term in the clock equation returns the [[Def - Galilean Spacetime and Its Failure|Galilean transformation]], identifying which physical input ($c \to \infty$) you have used to do so.

---

# Unlocked by This

> [!tip] The Lorentz Group and Rapidity *(from SR IV)*
> The collection of all Lorentz transformations forms the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$, the isometry group of the indefinite metric; parametrising a boost by [[Def - Rapidity|rapidity]] turns the nonlinear composition of velocities into ordinary addition, and the entire boost subgroup becomes a one-parameter group $\exp(\varphi K)$ generated by a boost generator $K$.

> [!tip] Relativistic Kinematics: Proper Time and Four-Velocity *(from SR V)*
> Because the transformation preserves the [[Def - The Spacetime Interval|interval]], the interval along a worldline is frame-independent and can be integrated to give the [[Def - Proper Time|proper time]] — the time a clock actually reads. Differentiating an event's position with respect to proper time gives the [[Def - Four-Velocity and Four-Acceleration|four-velocity]], the first object of relativistic dynamics, and $E = mc^2$ follows three steps later.

> [!tip] The Lorentz Transformation of Fields *(from Electromagnetism)*
> Once coordinates transform by $\Lambda$, so does everything built from them: the electric and magnetic fields assemble into a single antisymmetric **field-strength tensor** $F_{\mu\nu}$ that boosts by $F'_{\mu\nu} = \Lambda_\mu{}^\alpha \Lambda_\nu{}^\beta F_{\alpha\beta}$, mixing $\mathbf{E}$ and $\mathbf{B}$. A field that is purely electric in one frame carries a magnetic field in another — the relativistic origin of magnetism.

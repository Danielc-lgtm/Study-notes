---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Proper Time"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector has $X \cdot X > 0$ and a spacelike vector $X \cdot X < 0$. A timelike worldline is $\mathcal{L}$, parametrised by [[Def - Proper Time|proper time]] $\tau$; its [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is $U$ and its four-acceleration $A$. The **Serret–Frenet tetrad** is the orthonormal frame $(e_0, e_1, e_2, e_3)$ defined below, with $e_0 = U$. The **curvature** is $a$, the **first torsion** $T_1$, the **second torsion** $T_2$. The derivative of a vector field along $\mathcal{L}$ is $dW/d\tau = (dW^\mu/d\tau)\,e_\mu$. This is a compound page: it defines four interlocking notions — the **Serret–Frenet tetrad**, the **curvature** $a$, the **first torsion** $T_1$, and the **second torsion** $T_2$ — because they are constructed together, each from the proper-time derivative of the previous tetrad vector, and none is meaningful without the frame that carries it. Full registry on [[Special Relativity V — Worldlines, Proper Time and Four-Velocity]].

> [!warning] Convention
> Gourgoulhon builds this apparatus in his mostly-plus signature, where the four-acceleration is spacelike with $\vec a \cdot \vec a > 0$ and the curvature is $a = \sqrt{\vec a \cdot \vec a}$. In our mostly-minus signature the four-acceleration has $A \cdot A < 0$, so the curvature is $a = \sqrt{-A\cdot A} = \|A\|$. The Frenet relations and the antisymmetric structure of the connection matrix are unchanged; only the sign inside the square root for the spacelike norm differs. (This section may be skipped on a first reading — it is the most advanced material of the chapter.)

---

# Axiom Motivation

We have two natural fields along a timelike worldline: the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$ (the unit tangent) and the four-acceleration $A$ (which is nowhere tangent, being orthogonal to $U$). A natural question is whether these, together with their further derivatives, assemble into a complete *moving frame* that travels with the particle and encodes the full local shape of the worldline — its bending, its twisting out of a plane, its twisting out of a hyperplane. In Euclidean geometry this is exactly what the **Serret–Frenet apparatus** of a curve does: it attaches an orthonormal frame to each point and packages the curve's shape into a few scalar invariants (curvature and torsion). The motivation here is to do the same in Minkowski space, which produces one curvature and *two* torsions because spacetime is four-dimensional.

The construction is forced step by step by a single rule: differentiate each frame vector along the worldline and decompose the result in the frame. Begin with $e_0 := U$, the unit timelike tangent. Its derivative is the four-acceleration, $de_0/d\tau = A$, which is spacelike and orthogonal to $e_0$. Assuming the worldline is not straight ($A \ne 0$), normalise it to get the second frame vector $e_1 := A/\|A\|$, a unit spacelike vector. The normalising factor is the **curvature** $a := \|A\| = \sqrt{-A \cdot A}$ — the magnitude of the four-acceleration, promoted to the first invariant. (If $A = 0$ the worldline is a straight line, the frame degenerates, and the Serret–Frenet approach is vacuous: a straight worldline has no shape to record.)

Now differentiate $e_1$. Because $e_1$ is a *unit* vector, $de_1/d\tau$ is orthogonal to $e_1$ (differentiate $e_1 \cdot e_1 = -1$). It therefore lies in the span of $e_0$ and a new direction. Its $e_0$-component is fixed to be $a$ by differentiating the identity $e_0 \cdot e_1 = 0$; the remaining piece defines a new unit vector $e_2$ orthogonal to both $e_0$ and $e_1$, with coefficient $T_1 \ge 0$, the **first torsion**. The relation reads $de_1/d\tau = a\,e_0 + T_1\,e_2$. The first torsion measures the worldline's departure from the *plane* spanned by $(e_0, e_1)$ — the **osculating plane**: if $T_1 = 0$, the worldline stays in that plane (a planar worldline, like hyperbolic motion in a fixed $(t,x)$-plane).

The pattern continues. Differentiating $e_2$ produces, by the same orthogonality bookkeeping, $de_2/d\tau = -T_1\,e_1 + T_2\,e_3$, defining the last frame vector $e_3$ and the **second torsion** $T_2 \ge 0$, which measures the worldline's departure from the *hyperplane* spanned by $(e_0, e_1, e_2)$ — the **osculating hyperplane**. Finally $e_3$ is fixed (the frame is now complete in four dimensions), and its derivative closes the system: $de_3/d\tau = -T_2\,e_2$. Three invariants — $a, T_1, T_2$ — and the frame is exhausted, because spacetime has four dimensions and each new derivative can only point into the one remaining orthogonal direction. The whole system assembles into a single matrix equation whose coefficient matrix turns out to be (the mixed-index form of) an **antisymmetric** matrix — an element of the [[Def - Lie Algebra of the Lorentz Group|Lorentz Lie algebra]] — which is the statement that the Serret–Frenet frame is carried along the worldline by an infinitesimal Lorentz transformation, a **four-rotation**.

Why does this matter beyond curve geometry? Because the magnitude of the four-acceleration — the curvature $a$ — is what an accelerometer reads, and the full apparatus is the kinematic skeleton of an **accelerated observer's** carried frame. The antisymmetric coefficient matrix is precisely the generator of the rotation-plus-boost that the observer's spatial axes undergo, and separating the genuinely-rotating part from the unavoidable boost part is what defines **Fermi–Walker transport** and the behaviour of gyroscopes — the subject of [[Special Relativity XVI — Accelerated Observers|the accelerated-observers chapter]].

---

# The Definition

Let $\mathcal{L}$ be a timelike worldline parametrised by [[Def - Proper Time|proper time]] $\tau$, with nonvanishing four-acceleration. The **Serret–Frenet tetrad** of $\mathcal{L}$ is the orthonormal frame $(e_0, e_1, e_2, e_3)$ — with $e_0 \cdot e_0 = 1$ and $e_i \cdot e_i = -1$, all mutually orthogonal — defined as follows.

**Tangent and curvature.** The first vector is the four-velocity, $e_0 := U$. Its proper-time derivative is the four-acceleration; normalising gives the second vector and the first invariant:
$$
e_1 \;:=\; \frac{1}{a}\,A \;=\; \frac{1}{a}\,\frac{de_0}{d\tau}, \qquad a \;:=\; \|A\| \;=\; \sqrt{-A \cdot A} \;>\; 0.
$$
The positive scalar $a$ is the **curvature** of $\mathcal{L}$, and $a^{-1}$ is its **curvature radius**. (In a Euclidean space $a^{-1}$ would be the radius of the best-approximating circle; in Minkowski space, which is not a metric space, the circle interpretation is replaced — $a^{-1}$ is the distance to $\mathcal{L}$ at which two hyperplanes orthogonal to $U$ at neighbouring points of $\mathcal{L}$ intersect.)

**First torsion.** Differentiating $e_1$ and decomposing in the frame defines a unit spacelike $e_2 \perp e_0, e_1$ and the scalar $T_1 \ge 0$:
$$
\frac{de_1}{d\tau} \;=\; a\,e_0 \;+\; T_1\,e_2.
$$
$T_1$ is the **first torsion**. If $T_1 = 0$, the worldline lies in the **osculating plane** $(e_0, e_1)$.

**Second torsion.** Differentiating $e_2$ defines $e_3$ and the scalar $T_2 \ge 0$:
$$
\frac{de_2}{d\tau} \;=\; -T_1\,e_1 \;+\; T_2\,e_3.
$$
$T_2$ is the **second torsion**. If $T_2 = 0$, the worldline lies in the **osculating hyperplane** $(e_0, e_1, e_2)$. The frame closes with
$$
\frac{de_3}{d\tau} \;=\; -T_2\,e_2.
$$

**The Serret–Frenet system.** Collecting all four relations (with $c$ restored as a factor $c^{-1}$ on the left),
$$
\frac{d}{d\tau}\begin{pmatrix} e_0 \\ e_1 \\ e_2 \\ e_3 \end{pmatrix}
=
\begin{pmatrix}
0 & a & 0 & 0 \\
a & 0 & T_1 & 0 \\
0 & -T_1 & 0 & T_2 \\
0 & 0 & -T_2 & 0
\end{pmatrix}
\begin{pmatrix} e_0 \\ e_1 \\ e_2 \\ e_3 \end{pmatrix}.
$$
The coefficient matrix is the mixed-index form $\Omega^\alpha{}_\beta$ of an antisymmetric tensor $\Omega_{\alpha\beta} = -\Omega_{\beta\alpha}$ (the boost-like entries with $e_0$ carry the sign pattern of the indefinite metric); it is an element of the [[Def - Lie Algebra of the Lorentz Group|Lie algebra of the Lorentz group]], and it generates the **four-rotation** by which the tetrad is carried along $\mathcal{L}$ — see [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

A worldline with $a = \text{const}$, $T_1 = T_2 = 0$ is an arc of hyperbola (uniformly accelerated motion); $a = 0$ is a straight line, for which the apparatus is undefined.

---

# Categorical / Structural Definition

The Serret–Frenet apparatus is the **moving-frame (repère mobile) construction of Cartan** applied to a timelike curve in $(\mathbb{M}, \eta)$. Abstractly: a curve with a chosen orthonormal frame field defines a map $\tau \mapsto (\text{point}, \text{frame})$ into the **frame bundle**, and differentiating pulls back the connection $1$-form to a curve of Lie-algebra elements $\Omega(\tau) \in \mathfrak{so}(1,3)$. The Frenet relations are exactly the statement that this pulled-back connection is the matrix $\Omega$ above, and the invariants $(a, T_1, T_2)$ are its independent entries. That $\Omega$ lands in $\mathfrak{so}(1,3)$ rather than a general matrix algebra is the structural reason the frame stays orthonormal: an orthonormal frame can only evolve by an infinitesimal isometry, i.e. an infinitesimal Lorentz transformation.

The counting is structural. In an $n$-dimensional space the Serret–Frenet apparatus of a generic curve has $n - 1$ invariants (one curvature and $n - 2$ torsions), because the antisymmetric $n \times n$ connection matrix, restricted to its sub- and super-diagonal by the orthonormality bookkeeping, has exactly $n - 1$ free entries. For $n = 4$ this gives $3$: the curvature $a$ and two torsions $T_1, T_2$. The classical Euclidean case $n = 3$ gives the familiar one curvature and one torsion. The fundamental theorem of curve theory then applies in spirit: a timelike worldline is determined up to a Poincaré transformation by its three invariant functions $a(\tau), T_1(\tau), T_2(\tau)$, because the Frenet system is a linear ODE for the frame whose solution, given initial conditions, is unique.

The structural payoff is the identification of $\Omega$ as the **angular-velocity-and-boost generator** of the carried frame. Splitting $\Omega \in \mathfrak{so}(1,3)$ into its boost part (the entries coupling $e_0$ to the $e_i$, governed by the curvature $a$) and its rotation part (the entries coupling the $e_i$ among themselves, governed by the torsions) is precisely the decomposition that distinguishes the *unavoidable* relativistic rotation of an accelerated frame (Thomas precession) from any *additional* spatial rotation. A frame whose only evolution is the boost part — no genuine spatial rotation — is **Fermi–Walker transported**; that is the relativistic notion of a non-rotating (gyroscope) frame.

---

# Relate to Other Fields / Compression

This is the **Frenet–Serret theory of curves**, transposed from Euclidean $\mathbb{R}^3$ to Lorentzian $\mathbb{M}^4$. Where a space curve has a tangent–normal–binormal frame with curvature $\kappa$ and torsion $\tau_{\text{F}}$, a worldline has a tetrad $e_0, e_1, e_2, e_3$ with curvature $a$ and torsions $T_1, T_2$. The single most important specialisation to physics is that the curvature $a$ *is* the magnitude of the four-acceleration, $a = \|A\|$ — the proper acceleration an accelerometer reads.

**True name:** the curvature is *the proper acceleration $\|A\|$* and the torsions are *the rates at which the carried spatial frame twists out of its osculating plane and hyperplane*. The compression is that the entire local shape of a worldline — to all orders in the proper-time Taylor expansion — is encoded in three scalar functions $(a, T_1, T_2)$ and the antisymmetric generator $\Omega$, and the leading behaviour appears in order: the curvature at order $(a\,c\tau)^2$ in the expansion of the displacement, the first torsion at order $(a\,c\tau)^3$, the second at order $(a\,c\tau)^4$.

In Riemannian geometry the curvature vector of a curve and its higher torsions are the same construction; in the theory of moving frames it is Cartan's *repère mobile*; in the kinematics of rigid bodies and gyroscopes the antisymmetric generator $\Omega$ is the angular-velocity tensor, here generalised to include the boost that any accelerated frame must undergo. The connection to [[Special Relativity XVI — Accelerated Observers|accelerated observers]] is direct: $\Omega$ is the generator of the local frame's four-rotation, and its rotation part is Thomas precession.

---

# Examples / Corollaries

**Is an instance — uniformly accelerated (hyperbolic) motion.** A particle with constant proper acceleration $a$ along $x$ has $U = (\cosh a\tau, \sinh a\tau, 0, 0)$, so $A = a(\sinh a\tau, \cosh a\tau, 0, 0)$, giving $e_0 = U$, $e_1 = (\sinh a\tau, \cosh a\tau, 0, 0)$, curvature $\|A\| = a$ constant, and both torsions zero. The worldline lies in the $(t, x)$-plane, the osculating plane — consistent with $T_1 = T_2 = 0$. This is the worldline of the [[Ex - The twin paradox|twin-paradox traveller]] on each arc.

**Is an instance — a uniformly rotating particle.** A particle in uniform circular motion in the $(x, y)$-plane has a worldline (a helix in spacetime) with constant curvature *and* nonzero first torsion: the four-acceleration (centripetal) rotates within the spatial plane as the particle goes around, so the worldline does not stay in a single $(e_0, e_1)$-plane, $T_1 \ne 0$. This is the worldline relevant to the [[Ex - The ideal clock hypothesis and a circular-motion clock|circular-motion clock]] and to [[Special Relativity XVII — Rotating Observers|rotating observers]].

**Is NOT an instance — a straight worldline.** An inertial particle has $A = 0$, so $a = 0$ and the construction fails at the first step ($e_1 = A/a$ is $0/0$). A straight worldline has no Serret–Frenet frame because it has no shape to record — the apparatus is meaningful only for $a > 0$.

**Corollary — vanishing torsions reduce the dimension the worldline occupies.** $T_2 = 0$ confines $\mathcal{L}$ to a three-dimensional hyperplane; $T_1 = T_2 = 0$ confines it to a two-dimensional plane. A worldline with all invariants constant and $T_1 = T_2 = 0$ is exactly an arc of hyperbola — the unique relativistic "uniformly accelerated" motion, the analogue of a circle (constant curvature, zero torsion) in Euclidean space, with the circle replaced by a hyperbola because the metric is indefinite.

**Corollary — the curvature radius is not a circle's radius.** Because Minkowski space is not a metric space, $a^{-1}$ is not the radius of an osculating circle; instead, $a^{-1}$ is the distance along $e_1$ at which the hyperplanes orthogonal to $U$ at two neighbouring events of $\mathcal{L}$ meet. This is the correct Lorentzian replacement for the Euclidean osculating-circle picture.

**Calibration check.** You have understood the apparatus if you can: (i) compute the Serret–Frenet tetrad and curvature for hyperbolic motion and confirm $T_1 = T_2 = 0$; (ii) explain why a straight worldline has no Frenet frame; and (iii) state what the antisymmetry of the coefficient matrix $\Omega$ says about how the tetrad is transported (it evolves by an infinitesimal Lorentz transformation, a four-rotation).

---

# Unlocked by This

> [!tip] Fermi–Walker Transport and Thomas Precession *(from Accelerated Observers)*
> The antisymmetric generator $\Omega$ of the Serret–Frenet system is the **four-rotation** of the carried frame. Splitting it into its boost part (set by the curvature $a$) and its spatial-rotation part (set by the torsions) separates the unavoidable relativistic rotation of an accelerated frame — **Thomas precession** — from any extra spin. A frame whose only evolution is the boost part is **Fermi–Walker transported**, the relativistic definition of a non-rotating gyroscope; this is developed in [[Special Relativity XVI — Accelerated Observers]] and underlies the carried [[Def - Local Frame and Four-Rotation|local frame]] of an observer.

> [!tip] The Local Frame of an Observer and its Four-Rotation *(from Observers)*
> An observer carries an orthonormal [[Def - Local Frame and Four-Rotation|local frame]] $(e_0, e_1, e_2, e_3)$ along their worldline exactly as the Serret–Frenet tetrad is carried here, with $e_0$ their four-velocity. The variation of that frame along the worldline is governed by an antisymmetric generator of the same kind, and its decomposition into acceleration and rotation parts is the content of [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]]. The curvature and torsions of this page are the invariants of that carried frame.

> [!tip] Curve Curvature as Spacetime Curvature's Cousin *(from General Relativity)*
> The curvature of a *worldline* is an extrinsic quantity — how a one-dimensional curve bends inside flat spacetime — and must not be confused with the intrinsic **curvature of spacetime itself**, the Riemann tensor of general relativity. They are cousins: both measure failure of straightness, but the Riemann tensor measures the failure of *parallel transport around a loop* to return a vector unchanged, an intrinsic property of the metric $g_{\mu\nu}(x)$, whereas the worldline curvature measures the failure of a *single curve* to be geodesic. In curved spacetime the four-acceleration becomes the covariant $A^\mu = \nabla_U U^\mu$, its magnitude is still the proper acceleration an accelerometer reads, and a geodesic (free-fall) worldline has $a = 0$ even as spacetime curves around it — the precise sense in which gravity is locally indistinguishable from no force at all.

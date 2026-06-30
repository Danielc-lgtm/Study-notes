---
type: definition
subject: special-relativity
prereqs:
  - "Def - Observer and Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Thm - Euclidean Character of the Local Rest Space"
  - "Def - Spacetime Orientation"
  - "Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$. An observer $\mathcal{O}$ has worldline $\mathcal{L}_0$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ ($U_0\cdot U_0 = +1$) and four-acceleration $A_0 = dU_0/d\tau$ ($A_0\cdot U_0 = 0$, spacelike), parametrised by [[Def - Proper Time|proper time]] $\tau$ (also written $t$). The **local frame** is the orthonormal tetrad $(e_\alpha) = (e_0, e_1, e_2, e_3)$ with $e_0 = U_0$; Greek indices $\alpha,\beta = 0$–$3$, Latin $i,j = 1,2,3$. The **four-rotation** is the endomorphism $\Omega$ with $de_\alpha/d\tau = \Omega^\beta{}_\alpha e_\beta$ and its associated bilinear form $\underline\Omega(X,Y) = X\cdot\Omega(Y)$; the **spatial rotation rate** is $\vec\omega\in U_0^\perp$; $\times_{U_0}$ is the rest-space cross product. This is a compound page: it defines four interlocking notions — the **local frame**, the **observer's coordinates and reference space**, the **four-rotation**, and its **decomposition into four-acceleration and spatial rotation** — because the frame, its evolution, and the split of that evolution are introduced together and none is fully usable without the others. Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

> [!warning] Convention
> Gourgoulhon (mostly-plus, $\vec u\cdot\vec u = -1$, and a dimensionless $\vec u = c^{-1}dX/d\tau$ with four-acceleration $\vec a = c^{-1}d\vec u/d\tau$) writes the frame evolution as $d\vec e_\alpha/dt = c(\vec a\cdot\vec e_\alpha)\vec u - c(\vec u\cdot\vec e_\alpha)\vec a + \vec\omega\times_u\vec e_\alpha$. Translating to our mostly-minus convention with $U_0\cdot U_0 = +1$ and $A_0 = dU_0/d\tau$ (so $A_0 = c\vec a$ with $c = 1$), the Fermi–Walker bracket has its two terms **swapped in sign**, becoming $de_\alpha/d\tau = c[(U_0\cdot e_\alpha)A_0 - (A_0\cdot e_\alpha)U_0] + \vec\omega\times_{U_0}e_\alpha$. The swap is exactly what is needed to keep $de_0/d\tau = dU_0/d\tau = A_0$ consistent with $U_0\cdot U_0 = +1$ (verified below). The physics — Fermi–Walker tilt plus spatial rotation — is identical.

---

# Axiom Motivation

A local rest space tells the observer which directions are spatial, but it is an abstract three-plane: to assign actual spatial coordinates $(x^1, x^2, x^3)$ to nearby events, the observer needs *axes*. This page builds those axes — the **local frame** — and then asks the question that turns out to organise all of relativistic observer-kinematics: as the observer moves along the worldline, *how does the frame change*? The answer is the **four-rotation**, and its decomposition into a four-acceleration piece and a spatial-rotation piece is the deepest single result of the chapter.

First, the frame itself. We want four vectors $(e_\alpha)$ carried along the worldline that serve as orthonormal axes at each instant. Three requirements pin them down. They must be **orthonormal**, $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$, so that lengths and angles read off correctly — one timelike unit vector and three spacelike unit vectors, mutually orthogonal. The time vector must be **$e_0 = U_0$**, because the observer's own four-velocity *is* their time direction; the three spatial vectors $e_i$ then automatically lie in the [[Def - Observer and Local Rest Space|rest space]] $U_0^\perp$ (orthogonal to $e_0 = U_0$), where the [[Thm - Euclidean Character of the Local Rest Space|metric is Euclidean]] so an orthonormal triad exists by Gram–Schmidt. And the frame must be **right-handed and differentiable**: right-handed so the spatial axes have a consistent orientation (for cross products), differentiable so that "how the frame changes" is a meaningful question. Drop orthonormality and lengths/angles are wrong; drop $e_0 = U_0$ and the time axis is not the observer's time; drop differentiability and there is no four-rotation. Each requirement is forced by what the frame is for.

With the frame, coordinates are immediate: an event $M$ in the rest space $\mathscr{E}_{U_0}(t)$ at proper time $t$ has displacement $\overrightarrow{O(t)M} = x^i e_i(t)$ from the worldline, and $(t, x^1, x^2, x^3)$ are its coordinates with respect to $\mathcal{O}$. Because the three spatial axes can be held *fixed* in an abstract Euclidean **reference space** $R_{\mathcal{O}}$ (the same $\mathbb{R}^3$ at every instant) while they *evolve* in spacetime, the observer has a stable "map" of their surroundings — the cartography an observer makes of their environment.

Now the central question. The four vectors $e_\alpha(\tau)$ evolve along the worldline, and since they always form a basis, their derivative is a linear combination of themselves:
$$
\frac{de_\alpha}{d\tau} \;=\; \Omega^\beta{}_\alpha\, e_\beta,
$$
defining the **four-rotation** $\Omega$ as the endomorphism with these components. Two facts make $\Omega$ special. First, it is **antisymmetric** (as a bilinear form $\underline\Omega(X,Y) = X\cdot\Omega(Y)$): differentiating the constant orthonormality $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$ gives $\dot e_\alpha\cdot e_\beta + e_\alpha\cdot\dot e_\beta = 0$, i.e. $\underline\Omega(e_\beta, e_\alpha) = -\underline\Omega(e_\alpha, e_\beta)$. Antisymmetry is the statement that the frame stays orthonormal — that the dragging is by *infinitesimal Lorentz transformations*, not arbitrary linear maps. Second, its action on the time vector is the four-acceleration: $\Omega(U_0) = \Omega(e_0) = de_0/d\tau = A_0$ (with $c$: $cA_0/c = A_0$; in Gourgoulhon's units $c\vec a$).

Here the unifying idea arrives. Antisymmetric bilinear forms on Minkowski space have a canonical structure: relative to any timelike direction they split, by the [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|orthogonal decomposition theorem]], into an "electric" part (a rest-space vector/form) and a "magnetic" part (another rest-space vector). Applied to the four-rotation $\underline\Omega$ with the timelike direction $U_0$, the electric part is fixed by $\Omega(U_0) = A_0$ to be the four-acceleration, and the magnetic part is (minus) a rest-space vector $\vec\omega$. The decomposition splits the frame's evolution into two physically distinct motions:
$$
\frac{de_\alpha}{d\tau} \;=\; \underbrace{c\big[(U_0\cdot e_\alpha)A_0 - (A_0\cdot e_\alpha)U_0\big]}_{\text{Fermi–Walker part (four-acceleration)}} \;+\; \underbrace{\vec\omega\times_{U_0} e_\alpha}_{\text{spatial rotation part}}.
$$
The **Fermi–Walker part** tilts the time axis $e_0 = U_0$ by the four-acceleration — it is present whenever the observer accelerates, *even if nothing spins*, because in spacetime the time axis itself must rotate to track the changing velocity. The **spatial rotation part** rotates the three spatial axes at angular velocity $\vec\omega$, the genuine spinning of the observer's gyroscopes; $\vec\omega$ is the **four-rotation vector**, spacelike with $U_0\cdot\vec\omega = 0$. The motivation for the whole construction is to separate these: the unavoidable kinematic tilt forced by acceleration, versus the optional, physical rotation of the spatial frame.

Why does this specific decomposition matter rather than some other split? Because it is the *unique* one into pieces orthogonal to $U_0$, it is observer-natural, and it isolates the two measurable quantities an observer can determine about their own motion: the four-acceleration $A_0$ (read by an accelerometer) and the four-rotation $\vec\omega$ (read by a gyroscope). The four-velocity $U_0$ itself is *not* directly measurable (no experiment detects absolute velocity), but $A_0$ and $\vec\omega$ are. The decomposition is the algebraic expression of that physical fact, and it characterises an **inertial observer** as one with *both* pieces zero: $A_0 = 0$ and $\vec\omega = 0$.

---

# The Definition

Let $\mathcal{O}$ be an observer with worldline $\mathcal{L}_0$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$, and four-acceleration $A_0 = dU_0/d\tau$.

**Local frame.** A **local frame** along $\mathcal{L}_0$ is a quadruple of vector fields $(e_\alpha(\tau)) = (e_0, e_1, e_2, e_3)$ defined at each event $O(\tau)\in\mathcal{L}_0$, satisfying:
1. **orthonormality and right-handedness:** $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$ and $\epsilon(e_0, e_1, e_2, e_3) = +1$ (the [[Def - Spacetime Orientation|Levi-Civita tensor]] is positive on the frame);
2. **time vector:** $e_0 = U_0$;
3. **differentiability:** each $e_\alpha(\tau)$ is differentiable in $\tau$.

The three spatial vectors $e_1, e_2, e_3$ form an orthonormal basis of the [[Def - Observer and Local Rest Space|local rest space]] $E_{U_0}$. An **observer** is formally a worldline together with a carried local frame.

**Coordinates and reference space.** For an event $M$ in the rest space $\mathscr{E}_{U_0}(t)$ at proper time $t$, with $O(t)\in\mathcal{L}_0$ the worldline event of that rest space, the **spatial coordinates** of $M$ relative to $\mathcal{O}$ are the components $x^i$ of $\overrightarrow{O(t)M}$ in the spatial frame:
$$
\overrightarrow{O(t)M} \;=\; x^i\, e_i(t), \qquad\text{coordinates of } M:\ (t, x^1, x^2, x^3).
$$
The **reference space** $R_{\mathcal{O}}$ is a fixed three-dimensional Euclidean vector space with orthonormal basis $(\vec e_1, \vec e_2, \vec e_3)$, and the map $\varphi: M(t, x^i)\mapsto x^i\vec e_i$ sends events to their fixed image; the spatial axes are held fixed in $R_{\mathcal{O}}$ while they evolve in spacetime. A vector field $V(\tau) = V^\alpha e_\alpha(\tau)$ along $\mathcal{L}_0$ is **fixed with respect to $\mathcal{O}$** if its components $V^\alpha$ are constant.

**Four-rotation.** The **four-rotation** of the local frame is the endomorphism $\Omega$ defined by
$$
\boxed{\,\frac{de_\alpha}{d\tau} \;=\; \Omega^\beta{}_\alpha\, e_\beta\,},
$$
with associated bilinear form $\underline\Omega(X, Y) := X\cdot\Omega(Y)$. It is **antisymmetric**, $\underline\Omega(Y, X) = -\underline\Omega(X, Y)$, and satisfies $\Omega(U_0) = c\,A_0$ (with $c=1$, $\Omega(U_0) = A_0$). For a vector field $V$ fixed with respect to $\mathcal{O}$, $dV/d\tau = \Omega(V)$.

## The four-rotation and its decomposition

By the [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|orthogonal decomposition of antisymmetric bilinear forms]] relative to $U_0$, the four-rotation splits into a four-acceleration part and a spatial-rotation part. Its electric part is $q = c\,\underline{A_0}$ (fixed by $\Omega(U_0) = cA_0$), and its magnetic part is $-\vec\omega$ for a spacelike vector $\vec\omega\in U_0^\perp$ (the **four-rotation vector**, or **spatial rotation rate**, with $U_0\cdot\vec\omega = 0$). The endomorphism is
$$
\boxed{\,\Omega(V) \;=\; c\big[(U_0\cdot V)\,A_0 - (A_0\cdot V)\,U_0\big] \;+\; \vec\omega\times_{U_0} V\,},
$$
and applied to the frame,
$$
\boxed{\,\frac{de_\alpha}{d\tau} \;=\; \underbrace{c\big[(U_0\cdot e_\alpha)\,A_0 - (A_0\cdot e_\alpha)\,U_0\big]}_{\text{Fermi–Walker part } \Omega_{\mathrm{FW}}} \;+\; \underbrace{\vec\omega\times_{U_0} e_\alpha}_{\text{spatial rotation part } \Omega_{\mathrm{rot}}}\,},
$$
where $\vec v\times_{U_0}\vec w := \epsilon(U_0, \vec v, \vec w, \cdot)^\sharp$ is the rest-space cross product. The **Fermi–Walker tensor** $\Omega_{\mathrm{FW}}$ depends only on the four-acceleration; the **spatial rotation tensor** $\Omega_{\mathrm{rot}}$ rotates the three spatial axes at rate $\vec\omega$. An observer is:
- **accelerated** iff $A_0\neq 0$;
- **rotating** iff $\vec\omega\neq 0$;
- **inertial** iff the frame is constant, $de_\alpha/d\tau = 0$ for all $\alpha$, which holds **iff $A_0 = 0$ and $\vec\omega = 0$**.

The four-acceleration $A_0$ and four-rotation $\vec\omega$ are *measurable* by $\mathcal{O}$ (by accelerometer and gyroscope); the four-velocity $U_0$ is not.

> [!note]- Derivation of the decomposition and the consistency check $de_0/d\tau = A_0$
> **Antisymmetry of $\underline\Omega$.** Differentiate the constant $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$:
> $$0 = \frac{d}{d\tau}(e_\alpha\cdot e_\beta) = \frac{de_\alpha}{d\tau}\cdot e_\beta + e_\alpha\cdot\frac{de_\beta}{d\tau} = \Omega(e_\alpha)\cdot e_\beta + e_\alpha\cdot\Omega(e_\beta) = \underline\Omega(e_\beta, e_\alpha) + \underline\Omega(e_\alpha, e_\beta),$$
> using $\underline\Omega(X,Y) = X\cdot\Omega(Y)$ and the symmetry of $g$. Hence $\underline\Omega$ is antisymmetric.
>
> **Electric part.** The electric part of $\underline\Omega$ is $q = \underline\Omega(\cdot, U_0)$. Now $\underline\Omega(V, U_0) = V\cdot\Omega(U_0) = V\cdot(cA_0) = c\,A_0\cdot V$, so $q = c\,\underline{A_0}$ (the lowered four-acceleration, times $c$).
>
> **The decomposition.** By the [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|decomposition theorem]] (in our mostly-minus form, where the coefficient signs are fixed by $U_0\cdot U_0 = +1$), the endomorphism is $\Omega(V) = c[(U_0\cdot V)A_0 - (A_0\cdot V)U_0] + \vec\omega\times_{U_0}V$, with $\vec\omega$ the (negated) magnetic part.
>
> **Consistency check $de_0/d\tau = A_0$.** Set $V = e_0 = U_0$. Then $U_0\cdot U_0 = +1$, $A_0\cdot U_0 = 0$, and $\vec\omega\times_{U_0}U_0 = \epsilon(U_0, \vec\omega, U_0, \cdot)^\sharp = 0$ (two equal arguments in the antisymmetric $\epsilon$). So
> $$\Omega(U_0) = c[(+1)A_0 - 0\cdot U_0] + 0 = cA_0,$$
> i.e. $de_0/d\tau = cA_0$ ($= A_0$ with $c=1$), as required by the definition of the four-acceleration $A_0 = dU_0/d\tau$. This is the check that fixes the sign of the bracket in our convention (the *opposite* order would give $-cA_0$). For a spatial vector $e_i$ ($U_0\cdot e_i = 0$): $de_i/d\tau = -c(A_0\cdot e_i)U_0 + \vec\omega\times_{U_0}e_i$, and orthonormality is preserved: $\tfrac{d}{d\tau}(e_0\cdot e_i) = A_0\cdot e_i + U_0\cdot[-c(A_0\cdot e_i)U_0 + \vec\omega\times_{U_0}e_i] = A_0\cdot e_i - (A_0\cdot e_i) + 0 = 0$ (with $c=1$). $\blacksquare$

---

# Categorical / Structural Definition

A local frame is a **lift of the worldline to the frame bundle**: at each event $O(\tau)$ it selects an ordered orthonormal basis, i.e. a point in the bundle of (oriented, time-oriented) orthonormal frames over spacetime, whose structure group is the [[Def - The Lorentz Group|Lorentz group]] $SO^+(1,3)$ (or, fixing $e_0 = U_0$, the rotation subgroup $SO(3)$). The four-rotation $\underline\Omega$ is the **connection one-form pulled back to the worldline**: it is the $\mathfrak{so}(1,3)$-valued object telling you how the frame is transported, $de_\alpha/d\tau = \Omega^\beta{}_\alpha e_\beta$, and its antisymmetry is precisely the condition that $\Omega\in\mathfrak{so}(1,3)$ — an infinitesimal isometry. In this language the frame is dragged along the worldline by a one-parameter family of infinitesimal Lorentz transformations generated by $\underline\Omega(\tau)$, and the decomposition into electric and magnetic parts is the decomposition of the Lie algebra $\mathfrak{so}(1,3) = \mathfrak{boost}\oplus\mathfrak{rotation}$ relative to the time direction $U_0$ (developed fully in [[Special Relativity X — The Lorentz Group as a Lie Group]]).

The **reference space** $R_{\mathcal{O}}$ with its map $\varphi$ realises the abstract three-plane $E_{U_0}(\tau)$ as a *fixed* Euclidean $\mathbb{R}^3$: the isomorphisms $\bar\varphi_t: E_{U_0}(t)\to R_{\mathcal{O}}$, $v^i e_i(t)\mapsto v^i\vec e_i$, trivialise the family of rest spaces, sending the moving spatial frame to a fixed Euclidean basis. This is the structural reason an observer perceives a single, stable "space" even though the rest spaces form a one-parameter family in spacetime.

---

# Relate to Other Fields / Compression

The local frame is the relativistic **moving frame** (*repère mobile* of Cartan), and the four-rotation is Cartan's structure equation for it along a curve — the same apparatus as the Frenet–Serret frame of a space curve, generalised to a timelike worldline in spacetime. In rotating-frame mechanics, the spatial-rotation part $\vec\omega\times_{U_0}$ is exactly the operator producing **Coriolis and centrifugal** terms: $\vec\omega$ is the relativistic angular velocity of the observer's frame. In [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]] a Fermi–Walker-transported local frame furnishes **Fermi normal coordinates**, the natural coordinates of a freely-falling laboratory, and the four-rotation generalises to the connection along the worldline.

**True name:** the four-rotation is *the infinitesimal Lorentz transformation that drags the orthonormal frame along the worldline* — an element of $\mathfrak{so}(1,3)$ — and its decomposition is *boost part (four-acceleration $A_0$) plus rotation part (spatial rotation $\vec\omega$)*. The two pieces are the two things an observer can measure about their own motion: acceleration (accelerometer) and rotation (gyroscope).

---

# Examples / Corollaries

**Is an instance — the inertial frame.** An inertial observer has $A_0 = 0$ and may carry a non-rotating frame ($\vec\omega = 0$), so $de_\alpha/d\tau = 0$: the frame is constant, the axes are fixed in spacetime, and the rest spaces are parallel global hyperplanes. This is the simplest local frame and the only one that extends globally.

**Is an instance — the Serret–Frenet tetrad.** Taking $(e_\alpha)$ to be the Frenet frame of the worldline (with $e_1 = A_0/\|A_0\|$ the unit four-acceleration), the four-rotation becomes $\Omega_{\mathrm{FW}} = ca(\underline{e_1}\otimes\underline{e_0} - \underline{e_0}\otimes\underline{e_1})$ and the spatial rotation is $\vec\omega = cT_2\,e_1 + cT_1\,e_3$, where $a = \|A_0\|$ is the curvature and $T_1, T_2$ are the first and second torsions of the worldline (from [[Special Relativity V — Worldlines, Proper Time and Four-Velocity|Special Relativity V]]). This ties the four-rotation directly to the worldline's intrinsic geometry.

**Is NOT an instance — a non-orthonormal "frame".** A quadruple of vectors that spans the tangent space but is not orthonormal (say, with $e_0$ not unit, or axes not orthogonal) is *not* a local frame: its four-rotation form is not antisymmetric, the coordinates it furnishes are not metric, and lengths read off it are wrong. Orthonormality is what makes the frame a metric measuring apparatus.

**Is NOT an instance — a globally valid frame for an accelerated observer.** For $A_0\neq 0$, the local frame coordinates are single-valued only within the locality radius $r \ll \|A_0\|^{-1}$; beyond it the rest spaces intersect and a single event gets two coordinate sets. A frame purporting to cover all of spacetime for an accelerated observer does not exist. This is the calibration of the word *local*.

**Corollary — non-rotating is not the same as inertial.** An observer with $\vec\omega = 0$ but $A_0\neq 0$ is non-rotating yet *not* inertial: the spatial axes do not spin, but the time axis still tilts ($de_0/d\tau = cA_0\neq 0$), so the frame is not constant. The residual evolution is pure Fermi–Walker transport, and integrating it around a loop gives Thomas precession.

**Corollary — the time axis tilts at the four-acceleration.** Regardless of $\vec\omega$, the time vector evolves by $de_0/d\tau = cA_0$. So an accelerometer (which measures $\|A_0\|$) and a gyroscope (which measures $\vec\omega$) together determine the entire four-rotation, while no instrument measures $U_0$ itself.

**Calibration check.** You should be able to: (1) write the three defining properties of a local frame and explain why each is forced; (2) verify $de_0/d\tau = cA_0$ from the decomposition and use it to fix the sign of the Fermi–Walker bracket; and (3) state the three-way classification (inertial / accelerated / rotating) and explain why "non-rotating" ($\vec\omega = 0$) is weaker than "inertial" ($A_0 = \vec\omega = 0$).

---

# Unlocked by This

> [!tip] The Fermi–Walker Derivative and Non-Rotating Transport *(from §6.3)*
> Subtracting the Fermi–Walker part of the frame evolution defines the [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] $D^{\mathrm{FW}}_{U_0}V = dV/d\tau - \Omega_{\mathrm{FW}}(V)$, the relativistic notion of non-rotating transport — the law a gyroscope obeys — and the derivative with respect to the observer adds back the spatial rotation, $D_{\mathcal{O}}V = D^{\mathrm{FW}}_{U_0}V - \vec\omega\times_{U_0}V$.

> [!tip] The Four-Rotation as a Lorentz Lie-Algebra Element *(from the Lie Theory of the Lorentz Group)*
> The antisymmetric four-rotation $\underline\Omega$ is literally an element of $\mathfrak{so}(1,3)$, the [[Def - The Lorentz Group|Lorentz]] Lie algebra; its electric/magnetic decomposition is the boost/rotation split of the algebra, and exponentiating the boost part around a closed orbit produces the **Thomas rotation** of [[Special Relativity X — The Lorentz Group as a Lie Group]].

> [!tip] Fermi Normal Coordinates and Tidal Forces *(from General Relativity)*
> A Fermi–Walker-transported local frame gives **Fermi normal coordinates** in curved spacetime — the coordinates of a freely-falling, non-rotating laboratory — in which the metric departs from $\eta_{\mu\nu}$ at second order through the **Riemann tidal tensor**; the locality bound $r \ll \|A_0\|^{-1}$ derived here is the flat precursor of the tidal radius of validity. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] Thomas Precession and Spin Dynamics *(from Accelerated Observers)*
> The Fermi–Walker part of the four-rotation, integrated around a circular orbit, yields **Thomas precession** — the kinematic rotation of an accelerated, non-rotating gyroscope — which supplies the factor of $\tfrac12$ in atomic fine structure and is the kinematic core of the BMT spin-precession equation in [[Special Relativity XVI — Accelerated Observers]].

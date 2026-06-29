---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - The Lorentz Transformation"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. Four-vectors are written with capital Latin letters and no arrows: $X, Y, U, V, P$ (arrows are reserved for spatial three-vectors, $\mathbf{v}$). Their components in an orthonormal frame are $X^\mu = (X^0, X^1, X^2, X^3)$, $\mu = 0,1,2,3$, the index **upper**. A Lorentz transformation is the matrix $\Lambda$, with components $\Lambda^\mu{}_\nu$ satisfying $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ where $\eta = \mathrm{diag}(1,-1,-1,-1)$. The space of four-vectors is $E$, the vector space underlying [[Def - Minkowski Space and the Metric|Minkowski space]]. Full registry on [[Special Relativity III — Minkowski Spacetime and the Metric]].

---

# Axiom Motivation

A four-vector ought to be "the relativistic analogue of a vector" — an object with four components, one for time and three for space, that the laws of physics can be written in terms of. The naive definition is wrong, and seeing why is the motivation: a four-vector is *not* simply "a list of four numbers attached to an event". The coordinate tuple $(t,x,y,z)$ of an event is such a list, yet it is not a four-vector, and the reason exposes exactly what the definition must capture.

The trouble is the affine structure of spacetime. [[Def - Minkowski Space and the Metric|Minkowski space]] has no canonical origin: choosing a different origin event $O'$ shifts every event's coordinates by a constant, $x^\mu \mapsto x^\mu + a^\mu$. This is an *inhomogeneous* transformation — it adds a constant rather than acting linearly — so the tuple $(t,x,y,z)$ does not transform by a matrix and cannot be a vector in the model space $E$. A genuine vector must transform *homogeneously*: under a change of inertial frame its components must be related by the [[Def - The Lorentz Transformation|Lorentz matrix]] alone, with no additive constant. The displacement *between* two events, $q^\mu - p^\mu$, does transform this way, because the constant $a^\mu$ cancels in the difference. So the defining requirement is the homogeneous transformation law, and the prototype of an object satisfying it is the displacement four-vector.

Why insist on *this* transformation law and not some other? Because it is exactly the law that makes scalar products invariant. If $X^\mu$ and $Y^\mu$ both transform by $\Lambda$, then $g(X,Y) = \eta_{\mu\nu}X^\mu Y^\nu$ is unchanged, since $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$. Demanding that four-vectors transform by $\Lambda$ is precisely demanding that their inner products be Lorentz scalars — frame-independent numbers — and that is the property that makes four-vectors useful: any physical quantity built as a scalar product of four-vectors is automatically the same for all observers. A list of four numbers that did *not* transform by $\Lambda$ would produce frame-dependent "scalar products", useless for stating laws of physics.

There are two equivalent ways to phrase the definition, and each illuminates the other. The *intrinsic* phrasing: a four-vector is an element of the vector space $E$ underlying the affine Minkowski space — a displacement, or a tangent vector — defined without reference to any frame. The *operational* phrasing: a four-vector is an assignment of four components to each orthonormal frame, such that the components in two frames are related by the Lorentz matrix. The intrinsic phrasing is what the object *is*; the operational phrasing is how you *recognise* and *compute* with it, and it is the one a physicist reaches for, because the test "do the components transform by $\Lambda$?" is exactly the test that a candidate quantity (a velocity, a momentum, a current) is a legitimate four-vector.

---

# The Definition

A **four-vector** is an element $X$ of the vector space $E \cong \mathbb{R}^4$ underlying [[Def - Minkowski Space and the Metric|Minkowski space]] — the space of displacements between events, equivalently the tangent space at any event (the two coincide for a flat affine space). Concretely, $X$ is given in each orthonormal frame by four components $X^\mu = (X^0, X^1, X^2, X^3)$, and the components in two frames $S, S'$ related by a [[Def - The Lorentz Transformation|Lorentz transformation]] $\Lambda$ satisfy the **transformation law**
$$
X^\mu = \Lambda^\mu{}_\nu\, X'^\nu.
$$
The prototype is the displacement $\overrightarrow{PQ}$ between two events, with components $q^\mu - p^\mu$; further examples are the four-velocity, four-acceleration, four-momentum, and four-current. Spatial three-vectors are written $\mathbf{v}$ with components $v^i$, $i = 1,2,3$.

The **scalar product** of two four-vectors is $X\cdot Y = g(X,Y) = \eta_{\mu\nu}X^\mu Y^\nu = X^0Y^0 - X^1Y^1 - X^2Y^2 - X^3Y^3$, and it is **Lorentz invariant**: $X\cdot Y$ has the same value in every orthonormal frame, because $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$. The scalar square $X\cdot X$ gives the [[Def - Classification of Four-Vectors|classification]] of $X$ as timelike, spacelike, or null.

A vector $X^\mu$ with an upper index is **contravariant**; its [[Def - Metric Duality and Index Manipulation|metric dual]], the linear form $X_\mu = \eta_{\mu\nu}X^\nu$ with a lower index, is **covariant** and transforms by the inverse-transpose matrix.

---

# Categorical / Structural Definition

Structurally, "four-vector" is the statement that a quantity is a vector in the **defining (fundamental) representation** of the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$. A representation of a group $G$ on a vector space $V$ is a homomorphism $G \to GL(V)$ assigning to each group element a linear map, compatibly with composition; the defining representation of $O(1,3)$ is the tautological one, $\Lambda \mapsto \Lambda$ acting on $\mathbb{R}^4$. To say "$X$ is a four-vector" is to say "$X$ lives in this representation", i.e. its components transform by $\Lambda$ under a change of frame.

This is the entry point to the representation-theoretic organisation of relativistic physics. Scalars live in the trivial representation (they do not transform); four-vectors in the defining representation; tensors of rank $k$ in tensor powers of it; and — once one passes to the double cover $SL(2,\mathbb{C})$ — spinors live in representations with no tensor analogue. The classification of fields by *spin* is the classification of the irreducible representations under which they transform, and "four-vector" is the spin-one (vector) case. The metric $\eta_{\mu\nu}$ is the invariant bilinear form of the defining representation — the structure that makes $X\cdot Y$ a scalar — which is the representation-theoretic content of "$O(1,3)$ preserves $\eta$".

The intrinsic and operational definitions are reconciled categorically: the intrinsic object is an element of $E$; a choice of orthonormal frame is a choice of isomorphism $E \cong \mathbb{R}^4$; and the transformation law is the statement that two such isomorphisms differ by an element of $O(1,3)$, so the *components* depend on the frame but the *vector* does not.

---

# Relate to Other Fields / Compression

A four-vector is a **tangent vector** on a flat affine space, and its transformation law is the [[Thm - The Chain Rule|chain rule]] specialised to a linear change of coordinates. In [[Multivariate Analysis I — Differentiation in Several Variables|multivariate analysis]], a change of coordinates $x^\mu = x^\mu(x')$ transforms tangent-vector components by the Jacobian $\partial x^\mu/\partial x'^\nu$; for a Lorentz transformation this Jacobian is the constant matrix $\Lambda^\mu{}_\nu$, the same at every event because the transformation is linear. The four-vector transformation law $X^\mu = \Lambda^\mu{}_\nu X'^\nu$ is therefore nothing but the tangent-vector transformation law in the special case of a constant Jacobian — which is why special relativity, unlike general relativity, needs no differential geometry: the coordinate changes are global linear maps.

The contravariant/covariant distinction (upper versus lower index) is the vector/dual-vector distinction: a four-vector transforms by $\Lambda$, its [[Def - Metric Duality and Index Manipulation|metric dual]] one-form by $(\Lambda^{-1})^{\mathsf T}$, exactly as a tangent vector transforms by the Jacobian and a gradient one-form by the inverse Jacobian. Pedantic in $\mathbb{R}^n$ with a canonical basis, the distinction becomes structural the moment the basis is not canonical — which it is not here, because $\eta \neq I$.

**True name:** a four-vector is *a quantity whose components transform by $Λ$ between frames* — equivalently, *an element of the model vector space $E$, not of the affine space $\mathcal{E}$*. The operational test that decides whether a candidate (a velocity, a current, a field) is a genuine four-vector is precisely: do its components transform by $\Lambda$? If yes, its scalar products are invariants; if no, it is not a four-vector and building "scalars" from it is illegal.

---

# Examples / Corollaries

**Is an instance — the displacement between two events.** $\overrightarrow{PQ}$ with components $q^\mu - p^\mu$ is the prototypical four-vector: under a change of origin the constant cancels, under a boost it transforms by $\Lambda$, and its scalar square is the [[Def - The Spacetime Interval|interval]].

**Is an instance — the four-velocity.** The tangent to a worldline parametrised by [[Def - Proper Time|proper time]], $U^\mu = dx^\mu/d\tau$, is a four-vector: it is a ratio of the four-vector $dx^\mu$ to the invariant scalar $d\tau$, so it transforms by $\Lambda$. It satisfies $U\cdot U = 1$ (with $c$: $c^2$), a frame-independent normalisation.

**Is NOT an instance — the coordinate tuple of a single event.** $(t,x,y,z)$ for one event is *not* a four-vector: a change of origin shifts it by a constant $a^\mu$, an inhomogeneous (non-linear) transformation, so it does not transform by $\Lambda$ alone. Only differences of event-tuples are four-vectors. This is the single most important non-example, and the reason the affine structure matters.

**Is NOT an instance — the spatial velocity $\mathbf{v} = d\mathbf{x}/dt$.** The ordinary three-velocity is *not* the spatial part of any four-vector, because it is the derivative with respect to *coordinate* time $t$ (frame-dependent) rather than proper time $\tau$ (invariant). Under a boost it transforms by the nonlinear velocity-addition rule, not by $\Lambda$. The four-velocity $U^\mu = dx^\mu/d\tau$ is its proper relativistic upgrade.

**Corollary — scalar products are invariants.** For four-vectors $X, Y$, the number $X\cdot Y = \eta_{\mu\nu}X^\mu Y^\nu$ is the same in all frames. This is the workhorse of relativistic computation: any quantity recognised as a scalar product of four-vectors can be evaluated in whatever frame is convenient.

**Corollary — the classification is frame-independent.** Since $X\cdot X$ is invariant, the [[Def - Classification of Four-Vectors|timelike/spacelike/null classification]] of a four-vector is the same for all observers, even though the components are not.

**Calibration check.** If you have understood the definition you can: (i) explain why $(t,x,y,z)$ for an event is not a four-vector but $q^\mu - p^\mu$ is, by appeal to the inhomogeneity of an origin shift; (ii) verify that if $X^\mu = \Lambda^\mu{}_\nu X'^\nu$ and $Y^\mu = \Lambda^\mu{}_\nu Y'^\nu$ then $\eta_{\mu\nu}X^\mu Y^\nu = \eta_{\mu\nu}X'^\mu Y'^\nu$, using $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$; (iii) say why the three-velocity $d\mathbf{x}/dt$ is not part of a four-vector but $dx^\mu/d\tau$ is.

---

# Unlocked by This

> [!tip] Four-Velocity, Four-Momentum and Four-Force *(from Relativistic Dynamics)*
> The whole apparatus of relativistic mechanics is the construction of physically meaningful four-vectors: the **four-velocity** $U^\mu = dx^\mu/d\tau$, the **four-momentum** $P^\mu = mU^\mu$ whose time component is energy, and the **four-force** $dP^\mu/d\tau$; see [[Def - Four-Velocity and Four-Acceleration]] and [[Def - Four-Momentum and Rest Mass]]. Conservation laws and $E = mc^2$ are statements about these four-vectors and their invariant scalar squares.

> [!tip] Tensors and the Representations of the Lorentz Group *(from QFT)*
> A four-vector is a rank-one **tensor**, transforming with one factor of $\Lambda$; rank-$k$ tensors transform with $k$ factors, and they live in tensor powers of the defining representation; see [[Def - Tensors on Minkowski Space]]. Passing to the double cover $SL(2,\mathbb{C})$ adds **spinor** representations with no tensor analogue, and the classification of all such representations by mass and spin (Wigner) is the organising principle of relativistic **quantum field theory**.

---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Distribution on a Manifold"
  - "Def - Involutive Distribution"
  - "Def - Integrable Distribution"
  - "Thm - The Frobenius Theorem"
tags: [geometry, differential-geometry, constraints, mechanics]
---

# Notation

This page works on a smooth manifold $M^n$, thought of as the configuration space of a mechanical system. A point $q \in M$ is a **configuration**, a tangent vector $v \in T_qM$ is a **velocity**, and a curve $q : I \to M$ is a **motion**. Constraints restrict either the allowed configurations (constraints on $M$) or the allowed velocities at each configuration (constraints on $TM$).

- $D \subseteq TM$ — a **distribution** of rank $k$: at each $q \in M$, $D_q \subseteq T_qM$ is a $k$-dimensional subspace; the assignment $q \mapsto D_q$ is smooth.
- $\theta^1, \dots, \theta^{n-k}$ — local **annihilating $1$-forms** for $D$: pointwise linearly independent $1$-forms on a neighborhood, with $D_q = \bigcap_i\ker\theta^i_q$.
- $[X, Y]$ — the [[Def - The Lie Bracket of Vector Fields|Lie bracket]] of two vector fields.
- $d\theta$ — the [[Def - Exterior Derivative on a Manifold|exterior derivative]] of $\theta$.

The full notation registry for this topic is on [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]].

---

# Axiom Motivation

In classical mechanics, constraints come in two genuinely different flavors, and the distinction has nothing to do with mathematical sophistication: it is a physical fact about which configurations the system can reach. A bead on a wire is constrained to lie on a $1$-dimensional curve embedded in $3$-space; no matter how you push it, it stays on the wire. A skater on ice is constrained to move at each instant in a single direction (parallel to the blade) — but by combining a sequence of small motions in different directions (push, glide, turn, push) the skater can reach *every* position and orientation, including those the instantaneous constraint seemed to forbid. The first kind of constraint locks the system to a *submanifold*; the second locks the system to a *distribution* of allowed velocities, but the configurations remain free in the entire ambient manifold.

This dichotomy is the motivation for the definition of holonomic vs nonholonomic constraints. The mathematical content is precisely the Frobenius integrability criterion: a constraint distribution that is involutive (closed under the Lie bracket) is locally integrable, i.e., the configurations accessible from any starting point form a submanifold — the constraint *reduces the configuration space*. A non-involutive distribution cannot be integrated to a submanifold, even though it still restricts velocities at every point — the constraint reduces the *instantaneous* degrees of freedom but not the configurations accessible.

Why these are the right definitions can be motivated from the bead-and-skater examples. For the bead on a wire, the local constraint is "velocity must be tangent to the wire" — a rank-$1$ distribution. This is automatically involutive (any rank-$1$ distribution is, because the only Lie brackets involve scaling a single vector field by a function, and the bracket of $X$ with $fX$ is $f[X, X] + (Xf)X = (Xf)X$, which lies in the same rank-$1$ [[Def - Subspace|subspace]]). The bead's accessible positions form a $1$-dimensional submanifold (the wire itself) — that is the integral manifold. The constraint is *holonomic*.

For the skater, the local constraint is "the velocity at the skate must lie in the plane spanned by the blade direction $\partial_x$ and the direction of body rotation $\partial_\theta$" (in suitable coordinates) — a rank-$2$ distribution in a $4$-dimensional configuration space (position $(x, y)$ plus blade angle $\theta$ plus body rotation $\psi$ — actually $5$D for full description). The Lie bracket $[\partial_x, \partial_\theta]$ does *not* lie in the span — it involves a $\partial_y$ component (the direction perpendicular to the blade) — so the distribution is not involutive. By the Frobenius theorem (in its contrapositive form), no integral $2$-manifold exists, and the accessible configurations from a starting point form a higher-dimensional set than $2$. The skater can reach all of $\mathbb{R}^2 \times S^1 \times S^1$, even though only $2$ velocity directions are allowed at any instant. The constraint is *nonholonomic*.

What forces this specific definition. **Why involutivity?** The Frobenius theorem says involutivity is exactly the necessary-and-sufficient condition for the local existence of integral submanifolds. If we require holonomic constraints to "reduce the configuration space to a submanifold", involutivity is the precise mathematical condition. **Why not just "integrable"?** Integrability and involutivity are equivalent for smooth distributions of constant rank (Frobenius's theorem). The two terms can be used interchangeably in the smooth setting; "involutive" emphasizes the Lie-bracket condition, "integrable" emphasizes the existence of integral manifolds. **Why call non-involutive constraints "nonholonomic"?** The Greek roots are "holos" (whole) plus "nomos" (law); "holonomic" suggests the constraint is governed by a single global law (an equation $F(q) = 0$ defining a submanifold), and "nonholonomic" the absence of such a global law.

What breaks if we used a different definition. **Dropping involutivity and just requiring the distribution to be smooth**: then every constraint would be holonomic by fiat, and we lose the distinction between bead-on-wire (true holonomic) and skater (true nonholonomic). The physics would be wrong. **Requiring closedness instead of involutivity** (e.g., demanding the annihilating forms be closed, $d\theta = 0$): closedness is stronger than involutivity for $1$-forms (a closed $1$-form is involutive in the constraint sense, but the converse fails), so this would miss some holonomic constraints — e.g., the constraint $\theta = d(\phi/r)$ defines a closed-up-to-conformal-factor constraint that is integrable but not exact. **Demanding a global potential function**: that would miss locally holonomic constraints on globally non-simply-connected spaces, like the constraint that defines a [[Def - Foliation|foliation]] with non-trivial holonomy. The Frobenius criterion (involutivity = integrability) is the cleanest characterization that catches all the right phenomena.

---

# The Definition

Let $D \subseteq TM$ be a smooth rank-$k$ distribution on $M$, representing a constraint on the allowed velocities of a mechanical system on the configuration space $M$. The distribution $D$ — equivalently, the constraint it represents — is called

- **holonomic** (or **integrable**) if $D$ is **involutive**: for every pair of smooth vector fields $X, Y$ that are sections of $D$, the Lie bracket $[X, Y]$ is also a section of $D$. Equivalently (by the [[Thm - The Frobenius Theorem|Frobenius theorem]]), $D$ admits an [[Def - Integral Manifold of a Distribution|integral submanifold]] through every point — a $k$-dimensional submanifold $N$ with $T_qN = D_q$ for all $q \in N$. The accessible configurations from a starting point $q$ form precisely this integral manifold.

- **nonholonomic** (or **nonintegrable**) if $D$ is *not* involutive: there exist sections $X, Y$ of $D$ with $[X, Y]$ not in $D$. Equivalently, no integral submanifold exists through (at least some) points. The constraint restricts velocities pointwise but the accessible configurations form a higher-dimensional set than the rank of $D$ — by **Chow's theorem**, if the iterated Lie brackets of sections of $D$ span the full tangent space at each point, every two points are connected by a piecewise-smooth path tangent to $D$.

**Equivalent definitions via annihilating forms.** A rank-$k$ distribution $D$ on $M^n$ is locally cut out by $n - k$ linearly independent $1$-forms $\theta^1, \dots, \theta^{n-k}$ via $D_q = \bigcap_i\ker\theta^i_q$. The Frobenius integrability criterion in form language is

$$D\text{ holonomic} \iff d\theta^i\wedge\theta^1\wedge\cdots\wedge\theta^{n-k} = 0 \text{ for every } i,$$

i.e., the differential [[Def - Ideal|ideal]] generated by the $\theta^i$ is closed under $d$.

**Exact special case: an exact constraint $\theta = dF = 0$.** When the constraint can be written as $dF = 0$ for some smooth function $F : M \to \mathbb{R}$, the constraint distribution is the kernel of $dF$, which is the tangent space of the level set $\{F = 0\}$. This is automatically holonomic — the integral manifolds are the level sets — and the constraint reduces to "stay on the submanifold $\{F = 0\}$". This is the situation for the bead on a wire ($F(\vec x) =$ distance from wire, level set $F = 0$ is the wire) and for any constraint expressible as "stay on a submanifold given by an equation".

---

# Categorical / Structural Definition

A constraint distribution $D \subseteq TM$ has a **structural reformulation** in terms of a smooth section of the Grassmann bundle $\mathrm{Gr}_k(TM)$ — the bundle whose fiber at $q$ is the Grassmannian of $k$-planes in $T_qM$. The constraint $D$ is then a smooth map $q \mapsto D_q \in \mathrm{Gr}_k(T_qM)$, and holonomy is the integrability condition for this Grassmann-bundle section.

In the language of **groupoids** (relevant for the moduli problems of constrained mechanics): a distribution $D$ defines a *holonomy groupoid* $\mathcal{H}(D)$, whose objects are points of $M$ and whose morphisms $q \to q'$ are equivalence classes of $D$-tangent paths from $q$ to $q'$. The distribution is holonomic iff this groupoid is *not* connected (the orbits are the integral manifolds, strictly smaller than the connected components of $M$); it is nonholonomic iff the groupoid is connected on each connected component of $M$ (Chow's theorem: every two points are connected by a $D$-tangent path).

The categorical view explains why holonomy and Lie brackets are the same thing: the Lie bracket measures the failure of two infinitesimal flows to commute, and the commutator of two morphisms in the holonomy groupoid is the non-trivial morphism that records "how much we have moved off the candidate integral manifold." When the bracket lies inside $D$, the candidate motion can be undone by motion within $D$, hence integral manifolds exist; when it does not, motion in $D$ produces motion *outside* $D$, hence no integral submanifold can contain the iterated commutator path.

---

# Relate to Other Fields / Compression

**True name.** The true name of "holonomic" is *"the constraint distribution is involutive (closed under the Lie bracket) and hence integrable (admits integral submanifolds)."* The true name of "nonholonomic" is *"the constraint distribution is not involutive — the Lie bracket of constraint-satisfying velocities produces motion not satisfying the constraint."* The terminology is misleading: "nonholonomic" sounds like the negation of "holonomic," but the *physical* content is that nonholonomic constraints leave more configurations accessible, not fewer. The bead-on-wire (holonomic) is restricted to a $1$-D wire from a $3$-D ambient space — drastic reduction of degrees of freedom. The skater (nonholonomic) is restricted only at the velocity level — all of $\mathbb{R}^2\times S^1\times S^1$ remains accessible, no reduction of configuration space at all. The Lie-bracket non-involutivity is precisely what generates the *additional* accessibility.

**Distinction with Pfaffian constraints in differential equations.** In the theory of overdetermined PDEs and Pfaffian systems, a system of $n - k$ first-order PDEs on $n$ variables corresponds to a rank-$k$ distribution on the configuration space, and **integrability** of the Pfaffian system corresponds to holonomy of the distribution. Frobenius's theorem is what tells you when an overdetermined system admits a solution. So holonomic constraint = integrable Pfaffian system = solvable PDE system. The nonholonomic case corresponds to an overdetermined system that admits no solution unless the data is consistent — and is the source of **integrability obstructions** in geometric mechanics and elsewhere.

**Connection to sub-Riemannian geometry.** A nonholonomic distribution equipped with a metric (i.e., an inner product on $D_q$ at each point) defines a **sub-Riemannian geometry** on $M$: distances are measured along $D$-tangent paths only. By Chow's theorem, any two points are connected by such a path when the bracket-generating condition holds (the iterated brackets of $D$ sections span $TM$), so the sub-Riemannian distance is finite — but the resulting metric space is *not* a Riemannian manifold; the ball of radius $r$ has volume $r^{Q}$ for a "Hausdorff dimension" $Q > n$ that exceeds the topological dimension. Sub-Riemannian geometry is the natural geometry of nonholonomic systems, and includes the **Heisenberg group**, the **rolling sphere**, and many others.

**Connection to control theory.** A nonholonomic system, viewed dynamically, is a **control system** $\dot q = u_1 X_1(q) + \cdots + u_k X_k(q)$ with controls $u_i : I \to \mathbb{R}$ and constraint vector fields $X_i$ spanning $D$. The control problem is to reach a target configuration from the initial one. Chow's theorem (controllability) and the **Pontryagin maximum principle** govern when target reachability is possible and what optimal-control trajectories look like. The car-parking example mentioned in Frankel — where the constraint is "the car wheels are aligned with the velocity" (nonholonomic) — is the prototype of a controllable nonholonomic system in robotics.

---

# Examples / Corollaries

**Is an instance (holonomic): the bead on a circular wire.** The configuration space is $\mathbb{R}^3$, the wire is the unit circle $\{x^2 + y^2 = 1, z = 0\}$. The constraint is "the bead must stay on the wire": two equations $x^2 + y^2 = 1$ and $z = 0$, equivalently the rank-$1$ distribution $D_q = T_qC$ where $C$ is the circle. Every rank-$1$ smooth distribution is automatically involutive (because $[X, fX] = (Xf)X$ stays in the span), and the integral manifold is exactly the circle. So the constraint is holonomic; the reduced configuration space is $C \cong S^1$.

**Is an instance (holonomic): a thin rod on a horizontal plane with the constraint "the rod's center moves perpendicular to its length."** Surprisingly, this constraint is holonomic *if* we restrict to the rod's center plus its orientation. The constraint $dx\cos\theta + dy\sin\theta = 0$ (where $\theta$ is the orientation angle and $(x, y)$ is the center) is not closed when treated as a $1$-form, but it can be re-expressed as $d(x\cos\theta + y\sin\theta) - x\sin\theta\,d\theta\cdot\cos\theta + \ldots$ — actually, let's give a *cleaner* example: a particle on a plane with the constraint $\dot z = 0$ (where $z$ is the height) is holonomic and reduces motion to a $2$-plane. Many such examples; the test is involutivity.

**Is an instance (nonholonomic): the skater / ice skate.** The configuration space is $M = \mathbb{R}^2 \times S^1$ with coordinates $(x, y, \theta)$, where $(x, y)$ is the skate's position and $\theta$ is the blade's orientation. The constraint is "the velocity is parallel to the blade", giving the $1$-form $\theta_{\text{constraint}} = \sin\theta\,dx - \cos\theta\,dy = 0$. This defines a rank-$2$ distribution $D = \mathrm{span}(\cos\theta\,\partial_x + \sin\theta\,\partial_y, \partial_\theta)$.

Compute the Lie bracket: with $X_1 = \cos\theta\,\partial_x + \sin\theta\,\partial_y$ and $X_2 = \partial_\theta$, $[X_1, X_2] = -(\partial_\theta\cos\theta)\partial_x - (\partial_\theta\sin\theta)\partial_y = \sin\theta\,\partial_x - \cos\theta\,\partial_y$. This is *not* in $D$ — it is the perpendicular-to-blade direction. The bracket is exactly the direction the skater "can't directly move", but by composing $X_1$ and $X_2$ flows, the skater *can* reach. The distribution is nonholonomic, the skater can reach all of $\mathbb{R}^2 \times S^1$.

**Is an instance (nonholonomic): the rolling vertical disc on a horizontal plane.** This is Frankel's example. The configuration space $M^4 = \mathbb{R}^2 \times S^1 \times S^1$ has coordinates $(x, y, \psi, \phi)$: position of center $(x, y)$, plane orientation $\psi$ (angle the disc plane makes with the $x$-axis), and angle rolled $\phi$. The rolling-without-slipping constraints are
$$\theta^1 = dx - \cos\psi\,d\phi = 0, \quad\theta^2 = dy - \sin\psi\,d\phi = 0,$$
giving a rank-$2$ distribution $D \subseteq TM$. The Frobenius criterion: compute $d\theta^1 = \sin\psi\,d\psi\wedge d\phi$, and $d\theta^1\wedge\theta^1\wedge\theta^2 = \sin\psi\,d\psi\wedge d\phi\wedge dx\wedge dy + \cdots \neq 0$ on regions where $\sin\psi \neq 0$. So the distribution is nonholonomic. By a sequence of rollings (translate, rotate plane, roll back, rotate again), the disc can reach any configuration in $M^4$, including those at the same position with different orientations — even though "infinitesimally" only $2$ directions of motion are allowed.

**Is NOT an instance: a holonomic constraint expressed in a misleading form.** Consider on $\mathbb{R}^3$ the $1$-form $\theta = dx + y\,dz$. This *looks* nonholonomic — there is no obvious antiderivative. But check: $d\theta = dy\wedge dz$, so $d\theta\wedge\theta = dy\wedge dz\wedge(dx + y\,dz) = dy\wedge dz\wedge dx + 0 = -dx\wedge dy\wedge dz \neq 0$. So $\theta$ is *nonholonomic* — the differential [[Def - Ideal|ideal]] generated by $\theta$ is not closed under $d$. The constraint cannot be integrated to a $2$-submanifold. This is the **standard contact form** on $\mathbb{R}^3$, and it is the prototype of a contact structure.

**Corollary (every rank-$1$ distribution is holonomic).** The integral curves of a single vector field always exist (by [[Thm - Existence and Uniqueness of Integral Curves]]), and they are the integral manifolds. Equivalently, $[X, fX] = (Xf)X$ lies in the rank-$1$ span, so the involutivity is automatic. So nonholonomic constraints require *at least* rank $2$.

**Corollary (the codimension-$1$ case).** A codimension-$1$ distribution on $M^n$ is cut out by a single $1$-form $\theta$, and Frobenius reads $d\theta\wedge\theta = 0$. So holonomy is the *single equation* $d\theta\wedge\theta = 0$. If $\theta$ is closed ($d\theta = 0$), this is automatic and the constraint is holonomic with integral hypersurfaces $\theta^{-1}(c) = 0$. If $\theta$ is exact ($\theta = dF$), the integral hypersurfaces are the level sets $\{F = \mathrm{const}\}$. The nonholonomic case is when $d\theta \neq 0$ but $d\theta\wedge\theta \neq 0$ either — the rotation form $\theta = dx + y\,dz$ above is the canonical example, the contact structure.

**Corollary (Frankel's example: the constraint surface $F(x,y,z) = c$).** A constraint of the form $\theta = dF = 0$ is automatically holonomic, with integral submanifolds the level sets $F^{-1}(c)$. This is because $d^2 = 0$ gives $d\theta = ddF = 0$, so the Frobenius condition $d\theta\wedge\theta = 0$ is trivially satisfied. This is the cleanest case: an explicit potential $F$ produces a holonomic constraint, and the constraint distribution is the kernel of $dF$.

**Calibration check.** First, write down a rank-$2$ distribution on $\mathbb{R}^3$, compute the Lie bracket of two spanning vector fields, and check whether the bracket lies in the span — confirming holonomy or nonholonomy. Second, take the contact form $\theta = dz - y\,dx$ on $\mathbb{R}^3$, compute $d\theta\wedge\theta$, and verify it is the volume form $-dx\wedge dy\wedge dz$ (so the constraint is maximally nonholonomic). Third, in the rolling-disc example, derive the constraint $\theta^1, \theta^2$ from the geometric condition "the velocity of the contact point is zero", and verify the resulting distribution is nonholonomic by the Frobenius test.

---

# Unlocked by This

> [!tip] Nonholonomic Mechanics *(from Geometric Mechanics)*
> The Lagrange–Hamilton framework for mechanics needs adjustment in the presence of nonholonomic constraints. The standard Euler–Lagrange equations $\frac{d}{dt}\partial L/\partial\dot q^i - \partial L/\partial q^i = 0$ apply only to holonomic systems (where one can effectively reduce to the constraint submanifold and apply Lagrangian mechanics on it). For nonholonomic systems, one uses **Lagrange's method of multipliers** with the constraint $1$-forms, or the **d'Alembert–Lagrange principle**, or the more modern **Lagrange–d'Alembert principle** with a horizontal lift of the connection on $TM$. The dynamics is genuinely different from the "constrained Hamiltonian" picture — nonholonomic systems do *not* in general preserve a symplectic form on the constraint distribution, and energy conservation requires extra hypotheses. See **Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics** for the unconstrained Hamiltonian theory and the discussion of how constraints modify it.

> [!tip] Sub-Riemannian Geometry *(from Geometric Analysis)*
> A nonholonomic distribution equipped with an inner product (on each $D_q$) defines a **sub-Riemannian metric** on $M$ — distances are infima of lengths of $D$-tangent paths. The Heisenberg group ($\mathbb{R}^3$ with the contact distribution $\ker(dz - y\,dx)$ and the standard metric on $\mathrm{span}(\partial_x, \partial_y)$) is the simplest non-trivial example; the unit ball has "Hausdorff dimension" $4$ in the topological $3$-manifold, and the geodesics are spirals. Sub-Riemannian geometry is the natural language for nonholonomic systems and connects to **harmonic analysis on nilpotent Lie groups**, **hypoelliptic PDE** (the sub-Laplacian, the Kohn Laplacian), and **rough path theory**.

> [!tip] Geometric Control Theory and Lie-Bracket Steering *(from Control Theory)*
> A nonholonomic control system $\dot q = \sum u_i X_i(q)$ with controls $u_i$ steering along the constraint distribution $D = \mathrm{span}(X_1, \dots, X_k)$ is **controllable** (every two points connectible) iff the iterated brackets $\{X_i, [X_i, X_j], [X_i, [X_j, X_l]], \dots\}$ span $T_qM$ everywhere — the **Lie Algebra Rank Condition** (Chow's theorem). The constructive procedure for steering uses Lie-bracket-like "wiggle" motions: oscillating between two controls produces an effective motion in the bracket direction. This is the geometric backbone of **path planning** in robotics (car parking, satellite reorientation, space-craft attitude control), and the theory of **Lie-bracket extensions** systematically improves controllability bounds.

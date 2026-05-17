---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - Submanifold of Euclidean Space"
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - The Chain Rule"
tags: [analysis, multivariate-analysis]
---

# Notation

$M \subseteq \mathbb{R}^n$ is a $d$-dimensional $C^1$ [[Def - Submanifold of Euclidean Space|submanifold]] and $p \in M$ is a point. A **$C^1$ curve in $M$ through $p$** is a $C^1$ map $\gamma : (-\varepsilon, \varepsilon) \to \mathbb{R}^n$ with $\gamma(t) \in M$ for all $t$ and $\gamma(0) = p$; its **velocity** at $p$ is $\gamma'(0) \in \mathbb{R}^n$. For a map $f$, $Df_p$ is the total derivative; $\operatorname{im}$ and $\ker$ denote image and kernel of a linear map. We write $T_p M$ for the tangent space. The full registry is on [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Axiom Motivation

A submanifold $M$ is curved, and at each point we want its *best flat approximation* — the higher-dimensional analogue of the tangent line to a curve and the tangent plane to a surface. The question is how to define "the tangent space at $p$" so that it (i) is genuinely a linear object, a $d$-dimensional subspace, (ii) does not depend on any chosen parametrization or chart, and (iii) is computable.

The most honest starting point is *motion*. A tangent direction at $p$ should be a direction in which you can actually *move along $M$*. So consider all $C^1$ curves $\gamma$ that live inside $M$ and pass through $p$ at time $0$, and collect their velocity vectors $\gamma'(0)$. A vector is "tangent" if some genuine motion within $M$ has that velocity. This definition is manifestly *intrinsic* — it mentions only $M$ and curves in $M$, no parametrization — which secures desideratum (ii). It is also the *true name* of the concept: a tangent vector is a velocity of motion constrained to $M$.

But it is not obvious from this definition that the set of such velocities is a *linear subspace*. Why should the sum of two velocities of curves in $M$ again be the velocity of a curve in $M$? On a sphere, the velocities of two curves through the north pole are both horizontal, and their sum is horizontal — but is the sum realized by an actual curve *on the sphere*? It is, but proving it requires work, and that work is exactly where the submanifold hypothesis is consumed: because $M$ is locally a graph (or locally straightenable), the curves can be transported to a *flat* model where addition of velocities is obvious, and transported back. So linearity — desideratum (i) — is a *theorem*, not an assumption, and it is a theorem precisely because $M$ is a submanifold and not a cusped or crossing set. At a cusp, the velocity definition still makes sense but produces a non-linear set (a half-line, or a union of lines) — which is another way to see that cusps are not submanifolds.

For desideratum (iii), computability, the two representations of a submanifold each hand over a formula. If $M$ is the *level set* $\{f = c\}$, then a curve in $M$ satisfies $f(\gamma(t)) = c$ identically; differentiating, $Df_p(\gamma'(0)) = 0$, so every tangent vector lies in $\ker Df_p$ — and a dimension count shows the tangent space *is* exactly $\ker Df_p$. If $M$ is the *image* of a parametrization $G$, then curves in $M$ are $G\circ(\text{curves in parameter space})$, and the chain rule shows every tangent vector lies in $\operatorname{im}DG$ — and again equality holds. So the curve definition is the conceptually correct one, and the kernel/image descriptions are the computational ones, related to it by the chain rule.

Why not define the tangent space *directly* as $\ker Df_p$ and skip the curves? Because that definition would *depend on the choice of defining function $f$* — it would not be manifestly intrinsic, and one would have to prove it is independent of $f$. The curve definition has invariance built in. The right move is: define via curves (intrinsic, true name), then prove equality with the kernel and image descriptions (computable). That is the structure below.

---

# The Definition

Let $M \subseteq \mathbb{R}^n$ be a $d$-dimensional $C^1$ [[Def - Submanifold of Euclidean Space|submanifold]] and $p \in M$.

**Tangent space (curve definition).** A vector $\tau \in \mathbb{R}^n$ is **tangent to $M$ at $p$** if there is a $C^1$ curve $\gamma : (-\varepsilon, \varepsilon) \to \mathbb{R}^n$ with $\gamma(t) \in M$ for all $t$, $\gamma(0) = p$, and $\gamma'(0) = \tau$. The set of all such vectors is the **tangent space**
$$T_p M = \{\gamma'(0) : \gamma \text{ a } C^1 \text{ curve in } M \text{ with } \gamma(0) = p\}.$$

Equivalently (and this is part of the content of the definition), $\tau$ is tangent to $M$ at $p$ if and only if there is a sequence of points $p_k \in M$, $p_k \neq p$, with $p_k \to p$, and positive scalars $r_k \to 0$, such that
$$\frac{p_k - p}{r_k} \to \tau.$$

**It is a linear subspace.** For a submanifold, $T_p M$ is a $d$-dimensional linear subspace of $\mathbb{R}^n$. Concretely:

- **(Implicit form)** If, near $p$, $M = \{f = c\}$ with $f \in C^1$ and $Df_p$ of maximal rank, then
$$T_p M = \ker Df_p = \{v \in \mathbb{R}^n : Df_p(v) = 0\}.$$

- **(Parametric form)** If, near $p$, $M = G(V)$ with $G \in C^1$ a parametrization, $G(y_0) = p$, and $DG_{y_0}$ of maximal rank, then
$$T_p M = \operatorname{im} DG_{y_0} = DG_{y_0}(\mathbb{R}^d).$$

The affine subspace $p + T_p M$ is the **tangent plane** (or tangent line / hyperplane) — the best flat approximation to $M$ at $p$. A vector $\nu$ is **normal to $M$ at $p$** if $\nu \perp \tau$ for every $\tau \in T_p M$; the normal vectors form the orthogonal complement $(T_p M)^\perp$, of dimension $n - d$, and in the implicit form it is spanned by the rows of $Df_p$ (the gradients of the components of $f$).

---

# Relate to Other Fields / Compression

The tangent space defined here as a subspace of $\mathbb{R}^n$ is the concrete shadow of the **abstract tangent space** of differential geometry. On an abstract manifold there is no ambient $\mathbb{R}^n$ in which to draw velocity vectors, so the tangent space is built intrinsically — as the space of equivalence classes of curves with the same velocity, or as the space of *derivations* of smooth functions at the point. Both abstract constructions specialize, for a submanifold of $\mathbb{R}^n$, to the subspace $T_p M$ defined here; the curve definition is exactly the one that survives the abstraction.

The collection of all tangent spaces, glued together as $p$ varies over $M$, forms the **tangent bundle** $TM$ — itself a manifold, of dimension $2d$. The tangent bundle is the natural home of vector fields and of the velocity of any motion on $M$, and it is the setting for Lagrangian mechanics, where the configuration space is a manifold and velocities live in $TM$.

For a [[Def - Submanifold of Euclidean Space|matrix Lie group]] such as $O(n)$, the tangent space *at the identity element* carries an extra structure: the commutator bracket of matrices makes it a **Lie algebra**. The tangent space at the identity of $O(n)$ is the space of skew-symmetric matrices $\mathfrak{so}(n)$ — see [[Ex - The orthogonal group as a submanifold]] — and the tangent space "is" the infinitesimal version of the group, with the exponential map sending the Lie algebra back into the group. This is the meeting point of geometry and the algebra of [[Group Theory I — §1.1–1.2|groups]].

In **special relativity** and general relativity the tangent space at a point of the spacetime manifold is where four-velocities, four-momenta, and the metric live; the distinction between a point of spacetime and a tangent vector at that point is the same platonic distinction as here between $p \in M$ and $\tau \in T_p M$.

---

# Examples / Corollaries

**The tangent space to a sphere.** For $S^{n-1} = \{|x|^2 = 1\} = \{f = 0\}$ with $f(x) = |x|^2 - 1$, the derivative is $Df_p(v) = 2\langle p, v\rangle$. So $T_p S^{n-1} = \ker Df_p = \{v : \langle p, v\rangle = 0\} = p^\perp$ — the tangent space at $p$ is the hyperplane orthogonal to the radius vector $p$, which is geometrically exactly right. The normal direction is $p$ itself.

**The tangent space to a graph.** For $M = \operatorname{graph}(g) = \{(x, g(x))\}$, parametrized by $G(x) = (x, g(x))$, the derivative is $DG_x = \begin{pmatrix} I \\ Dg(x)\end{pmatrix}$, so $T_{(x,g(x))}M = \operatorname{im}DG_x = \{(v, Dg(x)\,v) : v \in \mathbb{R}^d\}$ — the graph of the *linear map* $Dg(x)$. The tangent space to a graph is the graph of the derivative: the linearization of the function is the tangent space. This is the cleanest case and the picture to keep.

**The tangent space at the identity of $O(n)$ is the skew-symmetric matrices.** Differentiating a curve $A(t)$ of orthogonal matrices through $A(0) = I$: from $A(t)^TA(t) = I$, the product rule gives $A'(0)^T + A'(0) = 0$, so the velocity $A'(0)$ is skew-symmetric. Conversely every skew-symmetric matrix is such a velocity. So $T_I O(n) = \{H : H^T = -H\}$, the Lie algebra $\mathfrak{so}(n)$.

**Is NOT a tangent vector — a secant direction that does not survive the limit.** A vector pointing from $p$ to a far-away point of $M$ is generally *not* tangent: the tangent space is built from *infinitesimal* secants $(p_k - p)/r_k$ in the limit $p_k \to p$. A chord of a circle is not tangent to it; only the limiting direction as the chord shrinks is.

**Corollary — the tangent space is independent of representation.** The two formulas $\ker Df_p$ and $\operatorname{im}DG_{y_0}$ give the *same* subspace, because both equal the curve-defined $T_p M$. This is a calibration check: for a submanifold described both ways, computing the tangent space by each route must agree — see [[Ex - Computing a tangent space]].

**Corollary — Lagrange multipliers, restated.** At a constrained extremum of $f$ on $M = \{g = 0\}$, the [[Thm - The Method of Lagrange Multipliers|Lagrange condition]] $\nabla f \in \operatorname{span}\{\nabla g_j\}$ says exactly $\nabla f \perp T_p M$, since $T_p M = \ker Dg_p$ and the $\nabla g_j$ span its orthogonal complement. The tangent space is what makes the geometric statement of Lagrange's theorem precise.

**Calibration check.** Verify that the tangent space to the circle $x^2 + y^2 = 1$ at $(1,0)$ is the vertical line $\{(0, t)\}$; that for the paraboloid $z = x^2 + y^2$ the tangent plane at $(1,1,2)$ is the graph of $(v_1, v_2)\mapsto 2v_1 + 2v_2$; and that a tangent vector and a normal vector at the same point are orthogonal. If you can also explain why the curve definition makes $T_p M$ automatically independent of any chosen $f$, you have understood the definition.

---

# Unlocked by This

> [!tip] The Regular Value Theorem *(from this topic)*
> The [[Thm - The Regular Value Theorem|regular value theorem]] not only certifies that a level set is a submanifold but also identifies its tangent space as $\ker Df_p$ — the kernel description is part of the theorem's conclusion.

> [!tip] The Tangent Bundle and Vector Fields *(from Differential Geometry)*
> Gluing the tangent spaces $T_p M$ over all $p \in M$ produces the **tangent bundle** $TM$, a manifold of dimension $2d$. Sections of the tangent bundle are **vector fields**, the objects whose flows are dynamical systems on $M$.

> [!tip] Lie Algebras *(from Lie Theory)*
> The tangent space at the identity of a [[Def - Submanifold of Euclidean Space|matrix Lie group]], equipped with the commutator bracket, is its **Lie algebra** — the infinitesimal version of the group, linked to it by the exponential map.

> [!tip] Riemannian Metrics and Geodesics *(from Riemannian Geometry)*
> Equipping each tangent space with an inner product, varying smoothly with $p$, gives a **Riemannian metric**; the shortest curves it determines are **geodesics**, found by an infinite-dimensional version of constrained optimization.

---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - Riemannian Metric"
  - "Def - Riemannian Manifold"
tags: [geometry, riemannian-geometry, connections]
---

# Notation

$(M, g)$ — a Riemannian (or semi-Riemannian) manifold. $\nabla$ — an affine connection on $TM$. $X, Y, Z$ — smooth vector fields on $M$. $g(Y, Z)$ — the inner product, a smooth function on $M$. $X g(Y, Z) = X(g(Y, Z))$ — the action of $X$ as a derivation on this function. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

We have an affine connection $\nabla$ on $TM$ — an operation that differentiates vector fields. We have a Riemannian metric $g$ — a smoothly-varying inner product on tangent spaces. **Are these two pieces of data compatible?** That is, is there a natural relationship between $\nabla$ and $g$, or are they completely independent? A priori they are independent: any manifold $M$ admits both metrics and connections, and there is no reason for an arbitrary $\nabla$ to know anything about $g$. The metric-compatibility condition is the natural relationship that demands they cooperate.

Here is the motivation. Consider two vector fields $Y, Z$ along a curve $\gamma$, parallel-transported by $\nabla$. Their inner product $g(Y, Z)$ is a real-valued function of $t$ — and one might hope that, since the vectors are "not changing", the inner product is constant. This would mean: parallel transport preserves the metric structure, i.e., is a linear [[Def - Isometry|isometry]] between the source and target tangent spaces. **This is exactly the metric-compatibility condition.** In integrated form: $g(P_\gamma v, P_\gamma w) = g(v, w)$ for any curve $\gamma$ and any tangent vectors $v, w$ at the source — see [[Thm - Parallel Transport is an Isometry for Metric-Compatible Connections]].

The infinitesimal version of "the inner product is preserved" is the Leibniz rule for $g$:
$$
X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z).
$$
The left side is the derivative of $g(Y, Z)$ in the direction of $X$ — the rate of change of the inner product. The right side is the rate of change attributable to the change in $Y$ (its covariant derivative $\nabla_X Y$) plus the rate attributable to the change in $Z$ (its covariant derivative $\nabla_X Z$). The condition says: the rate of change of the inner product is exactly what you would compute by "differentiating one factor at a time" — there is no additional contribution from $g$ itself "rotating" relative to the connection. This is the Leibniz rule for $g$, and it is the *defining* infinitesimal condition for the connection to be compatible with the metric.

**Equivalent: $\nabla g = 0$, where $g$ is regarded as a $(0,2)$-tensor and $\nabla$ is the [[Def - Induced Connection on Tensor Bundles|induced connection]] on tensor bundles.** The induced connection $\nabla g$ on a $(0,2)$-tensor is defined by $(\nabla_X g)(Y, Z) := X g(Y, Z) - g(\nabla_X Y, Z) - g(Y, \nabla_X Z)$ (this is the Leibniz extension of $\nabla$ from $TM$ to $T^*M \otimes T^*M$). The metric-compatibility condition is then exactly $\nabla g = 0$, the statement that $g$ is **covariantly constant**. This is the cleanest formulation; many texts give it as the definition.

**Why is this the natural condition, and not something else?** Two alternative conditions one could imagine are: (a) parallel transport preserves lengths but not angles; (b) parallel transport scales the metric by a uniform factor. Condition (a) leaves angles to drift freely under parallel transport, which is geometrically ugly and breaks the connection between parallel transport and the orthogonal group. Condition (b) (called a **Weyl connection** in geometry) is genuinely interesting and corresponds to "conformal" geometry — the metric is determined only up to a positive scalar — but is not the right structure for "ordinary" Riemannian geometry where we care about lengths absolutely, not just conformally. The metric-compatibility condition $\nabla g = 0$ is the one that makes lengths *and* angles absolute, and it is what's needed to set up Hopf-Rinow completeness, the variational formulation of [[Def - Geodesic|geodesics]], and the harmonic-analysis structure on Riemannian manifolds.

**What does metric-compatibility *exclude*?** It excludes connections where parallel-transported vectors change length or where the inner product of parallel-transported vectors changes along the curve. The Weitzenböck connection on a Lie group with a non-bi-invariant metric is a concrete example: declaring all left-invariant fields parallel means a parallel vector has constant left-invariant components, but its length (in the metric) can change as you move around the group. So the Weitzenböck connection is generally *not* metric-compatible with a left-invariant Riemannian metric unless the metric is also right-invariant (i.e., bi-invariant).

**What is the relation to the Levi-Civita connection?** The [[Def - Levi-Civita Connection|Levi-Civita connection]] is the unique connection that is both torsion-free *and* metric-compatible. Neither condition alone determines the connection — there are infinitely many torsion-free non-compatible connections (e.g., on a Riemannian $M$ start with the Levi-Civita connection and add a non-symmetric tensor field $A$ with appropriate index symmetries) and infinitely many compatible non-torsion-free connections (e.g., on a Lie group, the Cartan-Schouten connections $\nabla^\pm_X Y = 0$ or $\nabla^\pm_X Y = [X, Y]$ on bi-invariantly-metric Lie [[Def - Group|groups]] have specific torsion and are compatible). Together the two conditions select exactly one — by the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem]] via the [[Thm - Koszul Formula|Koszul formula]].

---

# The Definition

Let $(M, g)$ be a Riemannian (or semi-Riemannian) manifold. A connection $\nabla$ on $TM$ is **metric-compatible** (with respect to $g$), also called **compatible with $g$** or **Riemannian**, if any (equivalently all) of the following equivalent conditions hold:

1. **Leibniz rule for $g$.** For all vector fields $X, Y, Z \in \mathfrak{X}(M)$,
$$
X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z).
$$

2. **Covariantly constant metric.** The induced connection on tensor bundles satisfies $\nabla g = 0$; equivalently, $(\nabla_X g)(Y, Z) = 0$ for all $X, Y, Z$.

3. **Parallel transport is a linear isometry.** For every smooth curve $\gamma$ from $p$ to $q$, the parallel transport operator $P_\gamma : T_pM \to T_qM$ is a linear isometry: $g_q(P_\gamma v, P_\gamma w) = g_p(v, w)$ for all $v, w \in T_pM$. (See [[Thm - Parallel Transport is an Isometry for Metric-Compatible Connections]] for the equivalence.)

4. **Constant inner product along parallel vector fields.** For any vector fields $V, W$ that are parallel along a smooth curve $\gamma$ (i.e., $\nabla_t V = \nabla_t W = 0$), the inner product $g_{\gamma(t)}(V(t), W(t))$ is constant in $t$.

In a coordinate frame $(x^i)$, condition (2) reads
$$
\partial_k g_{ij} - \Gamma^l_{ki}g_{lj} - \Gamma^l_{kj}g_{il} = 0,
$$
or equivalently $\partial_k g_{ij} = \Gamma_{kij} + \Gamma_{kji}$ where $\Gamma_{kij} := g_{il}\Gamma^l_{kj}$ is the connection with the upper index lowered. This is the **Ricci identity** for the metric.

**In an orthonormal frame.** When $(e_a)$ is a local orthonormal frame ($g(e_a, e_b) = \delta_{ab}$ in Riemannian signature, $\eta_{ab}$ in Lorentzian), metric-compatibility takes the very clean form
$$
\omega^a{}_b + \omega^b{}_a = 0,
$$
i.e., the matrix of connection 1-forms is **antisymmetric** (with the second index lowered by $\delta$ or $\eta$). This is why orthonormal frames are so convenient for computing the Levi-Civita connection.

---

# Relate to Other Fields / Compression

The compression: **metric-compatibility says the connection respects the metric — equivalently, parallel transport is an isometry.** This is one of the two conditions (the other being torsion-freeness) that uniquely select the Levi-Civita connection on a Riemannian manifold.

In **physics**, metric-compatibility of the spacetime connection in general relativity is the statement that **proper time and proper length are well-defined along worldlines**: a parallel-transported timelike vector remains timelike with the same proper time, a parallel-transported spacelike vector remains spacelike with the same proper length. Without metric-compatibility, a clock's tick rate would change along its worldline in a way unrelated to the metric — a physically untenable situation. So metric-compatibility is built into the GR formulation as a physical requirement, not just a mathematical convenience.

In **gauge theory**, the analogue is **G-compatibility** for the structure group $G$: a connection on a principal $G$-bundle has the property that parallel transport lies in $G$ (which is automatic for a $G$-bundle) — so the gauge-theory analogue of metric-compatibility is built into the principal-bundle definition by construction. The reduction from $\mathrm{GL}(n)$-connections to $O(n)$-connections on the frame bundle of a Riemannian manifold is precisely the metric-compatibility condition, and the corresponding reduction of structure group is the geometric content.

**True name:** The "true name" of metric-compatibility is **parallel transport is an isometry of inner-product spaces**. This is the operational picture: the connection ferries inner-product spaces around without distorting them. The infinitesimal Leibniz form is the local-coordinate statement of the same idea, and the algebraic form $\nabla g = 0$ is the most concise statement, but the picture to keep in mind is "parallel transport = isometry".

---

# Examples / Corollaries

**Example: the flat connection on Euclidean $\mathbb{R}^n$ is metric-compatible with the Euclidean metric.** In Cartesian coordinates all Christoffel symbols vanish, and $\partial_k g_{ij} = \partial_k \delta_{ij} = 0$, so the Ricci identity is satisfied trivially. Parallel transport is also trivial (constant components), and the Euclidean inner product of two vectors with constant components is constant — confirming the isometry interpretation.

**Example: the Levi-Civita connection of any Riemannian manifold is metric-compatible.** By construction. The Christoffel formula $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$ is derived from the Koszul formula precisely to enforce both torsion-freeness and metric-compatibility — the formula is the unique solution to the two conditions, by the fundamental theorem.

**Example: a non-metric-compatible connection on $\mathbb{R}^2$.** Take the flat connection on $\mathbb{R}^2$ (all $\Gamma = 0$) but the metric $g = e^{2x}(dx^2 + dy^2)$. Then $\partial_x g_{xx} = 2e^{2x} \neq 0$, but $\Gamma^l_{xx}g_{lx} + \Gamma^l_{xx}g_{lx} = 0$ since all $\Gamma$ vanish. So the Ricci identity $\partial_x g_{xx} = 2\Gamma^l_{xx}g_{lx}$ fails — the flat connection is *not* metric-compatible with the rescaled metric. The Levi-Civita connection of $g$ has $\Gamma^x_{xx} = \Gamma^y_{xy} = 1$ and others, which can be checked to satisfy the Ricci identity.

**Example: the Weitzenböck connection on a Lie group with non-bi-invariant metric.** On $SU(2) \cong S^3$, take a left-invariant frame $(e_1, e_2, e_3)$ corresponding to the standard $\mathfrak{su}(2)$ basis. Declare $\nabla e_a = 0$ for all $a$ (the Weitzenböck connection). Suppose the metric in the frame is $g = e^{2t}(\sigma^1)^2 + (\sigma^2)^2 + (\sigma^3)^2$ where $t$ is a function of position (a *scaled* left-invariant metric). Then $e_1 g(e_1, e_1) = 2e^{2t}\,e_1(t) \neq 0$ in general, but $g(\nabla_{e_1}e_1, e_1) + g(e_1, \nabla_{e_1}e_1) = 0$ since the connection is zero on the frame. So the Leibniz identity fails — the Weitzenböck connection is not compatible with this scaled metric. (For the unscaled bi-invariant metric where $t \equiv 0$, the Weitzenböck connection *is* metric-compatible — but it still has nonzero torsion.)

**Non-example: the trivial connection on $S^2$.** There is no globally defined trivial connection on $TS^2$ because $S^2$ is not parallelisable (the hairy ball theorem). Any well-defined connection on $TS^2$ has nontrivial Christoffel structure; the Levi-Civita connection of the round metric is metric-compatible by construction, but neither "torsion-free" nor "metric-compatible" alone selects it — both conditions are essential.

**Corollary (metric-compatibility implies constant speed along geodesics).** If $\gamma$ is a geodesic ($\nabla_t\dot\gamma = 0$) and $\nabla$ is metric-compatible, then $\frac{d}{dt}g(\dot\gamma, \dot\gamma) = 2g(\nabla_t\dot\gamma, \dot\gamma) = 0$, so $|\dot\gamma|^2$ is constant along $\gamma$. This is the geometric content of "geodesics are unit-speed straight lines when parametrised by arc length": metric-compatibility is what makes "constant speed" meaningful.

**Corollary (the orthogonal complement is preserved by parallel transport).** If a [[Def - Subbundle|subbundle]] $E \subseteq TM$ is orthogonal-complement-invariant under parallel transport — meaning parallel transport of vectors in $E^\perp$ stays in $E^\perp$ — and $\nabla$ is metric-compatible, then the orthogonal projection onto $E$ is parallel along any curve. This is the foundation of **isometric immersions** of submanifolds and is what makes the **Gauss formula** $\nabla^M_X Y = \nabla^S_X Y + II(X, Y)$ work — the second fundamental form lives in the normal bundle, orthogonal to $TS$.

**Corollary (metric-compatibility implies $\nabla(g^{-1}) = 0$).** Since the inverse metric $g^{-1}$ is determined algebraically from $g$ by $g^{ij}g_{jk} = \delta^i_k$, and since $\nabla\delta = 0$ trivially, the induced connection on the inverse metric also vanishes: $\nabla g^{-1} = 0$. So metric-compatibility automatically gives compatibility with raising and lowering operations on tensor indices.

**Calibration check.** If you can perform the following three verifications, you have understood metric-compatibility. (i) Verify that for the round 2-sphere with $g = d\theta^2 + \sin^2\theta\,d\varphi^2$ and the Christoffel symbols $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$, $\Gamma^\varphi_{\theta\varphi} = \cot\theta$, the Ricci identity $\partial_k g_{ij} = \Gamma_{kij} + \Gamma_{kji}$ holds. (ii) Show that for a metric-compatible connection in an orthonormal frame, the connection 1-forms satisfy $\omega^a{}_b + \omega^b{}_a = 0$ (lowering with $\delta$). (iii) Show that the inner product of two parallel vector fields along a curve is constant, using the Leibniz rule applied to $g(V, W)$ with $\nabla_t V = \nabla_t W = 0$.

---

# Unlocked by This

> [!tip] The Fundamental Theorem of Riemannian Geometry *(from Riemannian Geometry)*
> The metric-compatibility condition is one of the two hypotheses (the other being torsion-freeness) that uniquely select the Levi-Civita connection on a Riemannian manifold; see [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)]]. The proof works by symmetrising the metric-compatibility identity over the three slots $(X, Y, Z)$ and using torsion-freeness to eliminate cross-terms, producing the [[Thm - Koszul Formula|Koszul formula]] that pins down $\nabla_X Y$ from $g$ alone. Neither condition alone determines the connection; their conjunction does, and this is the algebraic miracle at the heart of Riemannian geometry.

> [!tip] Reduction to the Orthonormal Frame Bundle *(from Gauge Theory)*
> A metric-compatible connection on $TM$ for a Riemannian manifold $(M, g)$ is equivalent to a principal connection on the **orthonormal frame bundle** $O(M, g) \to M$, with structure group $O(n)$ (or $\mathrm{SO}(n)$ for orientable manifolds, or $O(p, q)$ for semi-Riemannian). The frame bundle of all frames is a $\mathrm{GL}(n)$-bundle; the metric-compatibility condition is the *reduction of structure group* from $\mathrm{GL}(n)$ to $O(n)$. This is the bridge between the connection theory of [[Riemannian Geometry I — Connections and Covariant Differentiation|Riemannian Geometry I]] and the principal-bundle / gauge-theory framework of [[Gauge Theory III — Principal Connections, Curvature, Holonomy, and Gauge Symmetry|Gauge Theory III]]. Special holonomy reductions (Kähler $\to U(n)$, Calabi-Yau $\to SU(n)$, $G_2$, $\mathrm{Spin}(7)$) are further structure-group reductions of the orthonormal frame bundle.

> [!tip] Killing Fields and Conserved Quantities *(from Riemannian Geometry)*
> A **Killing vector field** $K$ is a vector field whose flow consists of isometries — equivalently $\mathcal{L}_K g = 0$, or in terms of the Levi-Civita connection $\nabla_X K \cdot Y + \nabla_Y K \cdot X = 0$ (i.e., $\nabla K$ is antisymmetric in $X, Y$ after lowering an index). The crucial consequence: for any geodesic $\gamma$, the inner product $g(\dot\gamma, K)$ is constant along $\gamma$. This delivers a **conserved quantity** for every Killing field, which is the geometric basis of Noether's theorem for spacetime symmetries: time-translation Killing gives energy conservation, space-translation gives momentum, rotational Killing gives angular momentum. In Schwarzschild spacetime the Killing fields $\partial_t$ and $\partial_\varphi$ give the conserved energy and angular momentum used to reduce the geodesic equation to a one-dimensional effective-potential problem — central to computing the perihelion precession of Mercury.

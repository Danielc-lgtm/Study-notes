---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Levi-Civita Connection"
  - "Def - Vector Field on a Manifold"
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Tensor Field on a Manifold"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a smooth Riemannian manifold of dimension $n$ with [[Def - Levi-Civita Connection|Levi-Civita connection]] $\nabla$. Vector fields are denoted $X, Y, Z, W \in \mathfrak{X}(M)$; $[X, Y]$ is the [[Def - The Lie Bracket of Vector Fields|Lie bracket]]. We use the **Lee/do Carmo/Frankel sign convention** for the Riemann tensor: $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$. The opposite sign appears in some textbooks (Petersen, older Russian sources); under the opposite convention, sectional curvature of the round sphere comes out negative, so check any source's first formula.

> [!warning] Convention: index placement
> Components are defined by $R(\partial_c, \partial_d)\partial_b = R^a_{\;bcd}\,\partial_a$. The covariant version is $R_{abcd} = g_{ae}R^e_{\;bcd}$, so $R_{abcd} = \langle R(\partial_c, \partial_d)\partial_b, \partial_a\rangle$. Some sources permute the indices; ours matches Lee's *Riemannian Manifolds*.

---

# Axiom Motivation

The Riemann tensor's job is to measure the failure of the second covariant derivative to commute. On Euclidean space with the flat connection, $\nabla_X = X^i \partial_i$ acts as a directional derivative on components, and two directional derivatives commute up to a Lie-bracket correction: $\partial_i \partial_j - \partial_j \partial_i = 0$ but $X^i \partial_i Y^j \partial_j - Y^i \partial_i X^j \partial_j = [X, Y]$. The flat-connection statement is $\nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z = \nabla_{[X, Y]}Z$. On a curved manifold, this equality *fails*, and the failure is what we want to capture. We define

$$R(X, Y)Z := \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]}Z$$

as the precise measurement of that failure. The three desiderata are: $R$ should *vanish identically* on flat space (it does, by the Euclidean computation above); $R$ should be a *tensor* (i.e., $\mathcal{C}^\infty(M)$-multilinear in all three slots, so its value at a point depends only on the values of $X, Y, Z$ at that point); and the algebraic structure of $R$ should *naturally encode* parallel-transport-around-a-loop information.

Why does the $-\nabla_{[X, Y]}Z$ correction term belong in the definition? Without it, the expression $\nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z$ fails to be tensorial: it depends on the values of $X$ and $Y$ in a neighbourhood, not just at the point, because $\nabla_X$ contains derivatives of the first argument's components. Dropping the Lie-bracket term spoils tensoriality. Equivalently: the operator $[\nabla_X, \nabla_Y]$ is a second-order differential operator on $Z$ in general, but its symbol kills the contribution of $\nabla_{[X, Y]}$, leaving a zeroth-order operator — which is what a tensor is. **The Lie-bracket correction is *exactly* the term needed to cancel the second-order part of the commutator and leave a tensor behind.** Concretely, if you replace $X$ by $fX$ for a smooth function $f$, the extra terms $Y(f)\nabla_X Z$ from $\nabla_{fX}\nabla_Y Z = f\nabla_X\nabla_Y Z + 0$ versus $\nabla_Y\nabla_{fX} Z = Y(f)\nabla_X Z + f\nabla_Y\nabla_X Z$ produce a discrepancy $-Y(f)\nabla_X Z$, while $\nabla_{[fX, Y]} = \nabla_{f[X, Y] - Y(f)X} = f\nabla_{[X, Y]} - Y(f)\nabla_X$, contributing exactly $+Y(f)\nabla_X Z$ to $R$. The cancellation is the proof of tensoriality.

Why the signs as stated? With this convention, the sectional curvature $K = \langle R(X, Y)Y, X\rangle / (|X|^2|Y|^2 - \langle X, Y\rangle^2)$ comes out *positive* for the round sphere (where geodesics converge) and *negative* for hyperbolic space (where geodesics diverge). This matches the universal physical intuition "positive curvature = converging." The opposite sign convention flips all comparison-theorem inequalities; it is not wrong, just inconvenient.

Why a $(1, 3)$-tensor rather than $(0, 4)$? The output $R(X, Y)Z$ is naturally a vector (a Jacobi field "force" on $Z$ as it transports), and only after we use the metric to take an inner product with a fourth vector $W$ do we get the scalar $R(X, Y, Z, W)$. The $(0, 4)$ form is the one that has all the algebraic symmetries (the pair-swap symmetry needs the metric to even be stated); the $(1, 3)$ form is the one that appears in the Jacobi equation $\nabla_T\nabla_T J + R(J, T)T = 0$.

If we strengthened the definition — for instance, demanding $R$ be the Riemann tensor of *some* metric, not just of the Levi-Civita connection of $g$ — we would be over-constraining: any connection (with or without torsion, metric-compatible or not) has a Riemann tensor by this definition. The Riemann tensor is a *general affine-connection* invariant; only its specific algebraic symmetries (the pair-swap $R(X, Y, Z, W) = R(Z, W, X, Y)$) require the connection to be metric-compatible and torsion-free.

---

# The Definition

> **Definition (Riemann curvature tensor).** Let $(M, g)$ be a Riemannian manifold with Levi-Civita connection $\nabla$. The **Riemann curvature tensor** is the $(1, 3)$-tensor field $R$ defined by
>
> $$R(X, Y)Z := \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]}Z \qquad X, Y, Z \in \mathfrak{X}(M).$$
>
> The **covariant Riemann tensor** is the $(0, 4)$-tensor $R(X, Y, Z, W) := \langle R(X, Y)Z, W\rangle$. In a local frame $(e_a)$ with dual coframe $(\omega^a)$, the components are
>
> $$R(e_c, e_d)e_b = R^a_{\;bcd}\, e_a, \qquad R_{abcd} = g_{ae} R^e_{\;bcd}.$$

**Equivalent formulation (Cartan's second structural equation).** In any local orthonormal frame $(e_a)$ with dual coframe $(\sigma^a)$, the connection 1-forms $\omega^a_{\;b}$ (defined by $\nabla_X e_b = \omega^a_{\;b}(X)e_a$) and curvature 2-forms $\Omega^a_{\;b}$ are related by

$$\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c} \wedge \omega^c_{\;b} = \tfrac{1}{2}R^a_{\;bcd}\,\sigma^c \wedge \sigma^d.$$

The components $R^a_{\;bcd}$ extracted from $\Omega^a_{\;b}$ via this expansion agree with the components defined by $R(\partial_c, \partial_d)\partial_b$ in a coordinate frame, after the appropriate frame change.

---

# Categorical / Structural Definition

The Riemann tensor is the **curvature of the Levi-Civita connection viewed as a connection on the principal $\mathrm{O}(n)$-bundle of orthonormal frames** $\mathrm{Fr}(M) \to M$. In the general theory of connections on principal $G$-bundles, a connection is specified by a $\mathfrak{g}$-valued 1-form $A$ on the total space (the **connection 1-form**), and its **curvature** is the $\mathfrak{g}$-valued 2-form

$$F = dA + \tfrac{1}{2}[A, A] = dA + A \wedge A.$$

For the Levi-Civita connection on $\mathrm{Fr}(M)$, $G = \mathrm{O}(n)$ and $\mathfrak{g} = \mathfrak{o}(n)$ (skew-symmetric matrices). The connection 1-form has components $A^a_{\;b} = \omega^a_{\;b}$ (skew in $(a, b)$), and the curvature 2-form has components $F^a_{\;b} = \Omega^a_{\;b}$. Pulling these back to $M$ via a local frame (section of $\mathrm{Fr}(M)$) recovers the structural equations above. This perspective makes the Riemann tensor an instance of the universal notion of curvature for principal bundles and connects it directly to gauge theory; see [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections]].

---

# Relate to Other Fields / Compression

In **gauge theory**, the Riemann tensor is the field strength $F = dA + A \wedge A$ of the Levi-Civita gauge field, with structure group $\mathrm{O}(n)$. Yang–Mills field strengths in other gauge groups ($\mathrm{U}(n)$ for QED, $\mathrm{SU}(n)$ for the strong force) have exactly the same algebraic shape; the difference is only the Lie algebra in which the connection takes values.

In **algebraic topology**, the Riemann tensor is the *curvature obstruction* to flatness of the tangent bundle, and the Pontryagin and Euler classes — characteristic classes detecting nontriviality of $TM$ — are built from polynomials in $R$ via **Chern–Weil theory**.

In **physics**, the Riemann tensor is the **tidal force tensor** of general relativity: a small ball of test particles initially at rest in geodesic motion has its shape deformed at rate $\ddot{J}^a = -R^a_{\;bcd}T^b T^d J^c$, where $T$ is the worldline tangent and $J$ is the deviation vector. This is the **geodesic deviation equation**, which is exactly the **Jacobi equation**.

**True name:** *The Riemann tensor is the obstruction to $\nabla^2$ commuting on tensor fields, packaged as a $(1, 3)$-tensor that picks up the second-order failure after cancelling the Lie-bracket correction.* Equivalently, in physical language, *the Riemann tensor is the tidal-force tensor felt by a small cloud of freely-falling test particles.* The operational picture you should reach for is geodesic deviation: $R(J, T)T$ is the acceleration of a Jacobi field, the rate at which initially parallel geodesics converge or diverge.

---

# Examples / Corollaries

**Example 1 (flat Euclidean space).** $M = \mathbb{R}^n$ with $g = \delta_{ij}dx^i dx^j$, $\nabla = \partial$ (the flat connection). Then $[\nabla_X, \nabla_Y]Z = \nabla_{[X,Y]}Z$ on flat space (this is just the equality of mixed partials), so $R \equiv 0$. Conversely, if $R \equiv 0$ on a connected, simply connected manifold, then $(M, g)$ is locally isometric to Euclidean space — there exists a global parallel orthonormal frame, and the connection 1-forms vanish in it. This is the geometric content of "$R$ measures the obstruction to flatness."

**Example 2 (constant sectional curvature).** A Riemannian manifold has constant sectional curvature $K_0$ if and only if

$$R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y).$$

For the unit sphere $S^n$ with $K_0 = 1$, this gives $R(X, Y)Z = \langle Y, Z\rangle X - \langle X, Z\rangle Y$. For hyperbolic $n$-space $H^n$ with $K_0 = -1$, the sign flips. These are the "simplest possible" Riemann tensors consistent with the algebraic symmetries — any constraint stronger than constant sectional curvature would force $R = 0$.

**Example 3 (product manifold).** For a product Riemannian manifold $(M_1 \times M_2, g_1 \oplus g_2)$, the Riemann tensor is **block-diagonal** in the obvious sense: it vanishes on any pair of vectors $X, Y$ split between the two factors. So on $S^2 \times S^2$ with the product round metric, the Riemann tensor has nonzero components only "within" each $S^2$ factor; sectional curvature is $+1$ on $2$-planes tangent to either factor and $0$ on "mixed" $2$-planes.

**Non-example.** The expression $\nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z$ alone (omitting the Lie-bracket correction) is **not** a tensor: $\nabla_{fX}\nabla_Y Z = f\nabla_X\nabla_Y Z$, but $\nabla_Y\nabla_{fX} Z = Y(f)\nabla_X Z + f\nabla_Y\nabla_X Z$, so the commutator picks up an extra $-Y(f)\nabla_X Z$ that does not vanish in general. This extra term is exactly cancelled by $-\nabla_{[fX, Y]}Z = -\nabla_{f[X, Y] - Y(f)X}Z = -f\nabla_{[X,Y]}Z + Y(f)\nabla_X Z$.

**Non-example.** $R = 0$ does **not** imply $M$ is globally Euclidean — only *locally* isometric. The flat torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$ has $R \equiv 0$ but is not even simply connected, let alone diffeomorphic to $\mathbb{R}^n$.

**Calibration check.** If you have understood this definition correctly you should be able to: (a) verify directly that $R(X, Y)Z = -R(Y, X)Z$ from the antisymmetry of the commutator; (b) compute $R$ for the flat metric on $\mathbb{R}^n$ and get zero; (c) state the Jacobi equation $\nabla_T\nabla_T J + R(J, T)T = 0$ along a geodesic and recognise it as the geodesic-deviation equation; (d) explain in one sentence why the Lie-bracket correction term is needed for tensoriality.

---

# Unlocked by This

> [!tip] Sectional Curvature *(from Riemannian Geometry III)*
> The full Riemann tensor is unwieldy in dimension $\ge 3$; one extracts a scalar invariant from it for each $2$-plane $\sigma \subset T_pM$, the **sectional curvature** $K(\sigma)$. The sectional curvatures determine $R$ entirely (a small but useful theorem), so no information is lost. Most global theorems in this chapter (Synge, Cartan–Hadamard, the sphere theorem) are stated in terms of sectional curvature. See [[Def - Sectional Curvature]].

> [!tip] Jacobi Field *(from Riemannian Geometry II)*
> A Jacobi field along a geodesic $\gamma$ with tangent $T$ is a vector field $J$ satisfying the Jacobi equation $\nabla_T\nabla_T J + R(J, T)T = 0$. Jacobi fields are exactly the variation vector fields of one-parameter families of geodesics, so they describe how nearby geodesics spread out or converge. The Riemann tensor enters the Jacobi equation directly, and the global comparison theorems (Bonnet–Myers, Cartan–Hadamard) all proceed by analysing solutions of this ODE under curvature bounds.

> [!tip] Einstein Tensor *(from General Relativity)*
> The Einstein tensor $G_{ab} = \mathrm{Ric}_{ab} - \tfrac{1}{2}g_{ab}S$ is built from contractions of the Riemann tensor; the contracted second Bianchi identity (a differential identity for $\nabla R$) makes it divergence-free. **Einstein's field equations** $G_{ab} = 8\pi T_{ab}$ equate this geometric tensor with the matter stress-energy. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] Geodesic Deviation Equation *(from General Relativity)*
> The Jacobi equation, viewed in spacetime, becomes the **geodesic deviation equation** describing tidal effects: a small cloud of freely-falling test particles is deformed by the Riemann tensor of the ambient spacetime. The tidal force on a particle separated from a reference geodesic by deviation vector $J$ is $-R(J, T)T$ — the Newtonian inverse-cube tidal force is the weak-field limit. This is the most direct physical manifestation of curvature.

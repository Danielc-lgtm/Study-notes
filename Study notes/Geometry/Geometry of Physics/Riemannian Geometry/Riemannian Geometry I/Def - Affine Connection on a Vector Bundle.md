---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Vector Bundle"
  - "Def - Section of a Vector Bundle"
  - "Def - Vector Field on a Manifold"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, riemannian-geometry, connections]
---

# Notation

$E \to M$ — a smooth vector bundle of rank $k$ over a smooth manifold $M$ of dimension $n$. $\Gamma(E)$ — the $C^\infty(M)$-module of smooth sections of $E$ (a section assigns to each $p \in M$ a vector in the fibre $E_p$, smoothly). $\mathfrak{X}(M) = \Gamma(TM)$ — smooth vector fields on $M$. $X \in \mathfrak{X}(M)$, $s \in \Gamma(E)$ — generic vector field and bundle section. $X(f)$ — the action of $X$ on a smooth function $f \in C^\infty(M)$, the directional derivative of $f$ in the direction of $X$. The full notation registry for the connection-theoretic context lives on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

The thing we are trying to axiomatise is **differentiation of a vector-bundle section in the direction of a vector field**. Differentiation in calculus on $\mathbb{R}^n$ has a clean meaning: to differentiate a function $f$ in the direction of $X$ at the point $p$, you compare $f(p + \varepsilon X(p))$ with $f(p)$ and take the limit. This works because the values $f(p + \varepsilon X(p))$ and $f(p)$ both live in $\mathbb{R}$, so they can be subtracted. But to differentiate a vector field $V$ in the direction of $X$, you would want to compare $V(p + \varepsilon X(p))$ with $V(p)$ — and these live in *different* tangent spaces, $T_{p + \varepsilon X(p)}M$ and $T_pM$. On $\mathbb{R}^n$ these spaces have a canonical identification (both are copies of $\mathbb{R}^n$), so the subtraction makes sense; on a general curved manifold they do not, and the naive coordinate-wise derivative $\partial_j V^i$ depends on the chart and is not a tensor. The connection is the *additional structure* that supplies this comparison and makes the differentiation well-defined.

What should the axioms say? At minimum, $\nabla_X s$ should be a bundle section (it should be a "vector at each point"). It should depend on $X$ and on $s$. It should be linear in $X$ over $\mathbb{R}$, since differentiation in the sum of two directions is the sum of the differentiations. It should be linear in $s$ over $\mathbb{R}$, since the derivative of a sum is the sum of derivatives. And it should be **localisable**: the value at $p$ should depend only on what $X$ and $s$ do in an arbitrarily small neighbourhood of $p$.

The two axioms — $C^\infty$-linearity in $X$ and the Leibniz rule in $s$ — are forced by these requirements, and each axiom is doing a specific job.

**Why $C^\infty(M)$-linearity in $X$, $\nabla_{fX}s = f\nabla_X s$, and not just $\mathbb{R}$-linearity?** This is the crucial axiom and the most subtle one. It says: the value $(\nabla_X s)(p)$ depends only on the value $X(p)$ of $X$ at $p$, not on the values of $X$ at nearby points. The reason is that if we are differentiating "in the direction of $X$", only the direction at $p$ should matter — the direction at $p$ tells us which way to walk to find a nearby point, and the rate at which we walk (which depends on $|X(p)|$) tells us how to rescale the difference quotient. The direction at nearby points $q \neq p$ should be irrelevant to the limit at $p$. The $C^\infty$-linearity is the algebraic encoding of this: if you multiply $X$ by a smooth function $f$, the value at $p$ scales by $f(p)$, so $(\nabla_{fX}s)(p) = f(p)(\nabla_X s)(p)$, which is the same as $(f\nabla_X s)(p)$. This is what makes $\nabla_X s$ at $p$ depend on $X$ only through $X(p)$ — equivalently, $\nabla_{(\cdot)}s$ is a $C^\infty$-linear map from $\mathfrak{X}(M)$ to $\Gamma(E)$, i.e., a *tensor* of type $(0,1)$ valued in $E$, the **covariant differential** $\nabla s \in \Gamma(T^*M \otimes E)$ with $(\nabla s)(X) = \nabla_X s$.

What breaks if we drop $C^\infty$-linearity in $X$ and demand only $\mathbb{R}$-linearity? Then $\nabla_X s$ at $p$ could depend on the values of $X$ at points other than $p$. The Lie derivative $\mathcal{L}_X Y = [X, Y]$ is exactly such an operation: it is $\mathbb{R}$-linear in $X$ but *not* $C^\infty$-linear ($\mathcal{L}_{fX}Y = f\mathcal{L}_X Y - Y(f)X$ — the extra $-Y(f)X$ term depends on the derivative of $X$ in the direction of $Y$). The Lie derivative is a perfectly good operation, but it is *not* a connection, because its value at $p$ depends on more than just $X(p)$. The Lie derivative does not give parallel transport — it cannot solve the "compare $V(p)$ and $V(q)$" problem — because it has no way to localise to a single direction at $p$. The lesson: $C^\infty$-linearity is what distinguishes "directional differentiation" from operations like the Lie bracket.

**Why the Leibniz rule, $\nabla_X(fs) = X(f)s + f\nabla_X s$, and not just $\mathbb{R}$-linearity in $s$?** This is the axiom that makes $\nabla$ a *derivation* — it says $\nabla$ obeys the product rule of calculus. Why is this forced? Because $\nabla_X s$ is supposed to be the derivative of $s$ in the direction of $X$, and any reasonable notion of "derivative" should satisfy the product rule. Concretely, if $s = fs_0$ for a function $f$ and a section $s_0$, then we want the rate of change of $s$ in the direction of $X$ to be: (rate of change of $f$ in direction $X$) $\times s_0$, plus $f \times$ (rate of change of $s_0$ in direction $X$). The first term is $X(f) s_0$, the second is $f\nabla_X s_0$. Without this rule, scaling a section by a smooth function would not interact properly with differentiation, and one would lose the ability to do local computations. (Try writing $s = s^i e_i$ in a local frame: without the Leibniz rule on the products $s^i e_i$, one cannot extract a useful coordinate formula for $\nabla_X s$.)

What breaks if we drop the Leibniz rule? Then $\nabla$ would be merely a $C^\infty(M)$-bilinear map $\mathfrak{X}(M) \times \Gamma(E) \to \Gamma(E)$ — that is, a tensor of type $(1, 1)$ in the bundle sense (a section of $\mathrm{End}(E) \otimes T^*M$). Tensor fields are perfectly good objects, but they are not derivatives: the trivial operation $\nabla_X s = 0$ is a "tensor field" but it tells us nothing about how $s$ changes. The Leibniz rule is the *irreducibly derivative-like* content; without it, $\nabla$ would not deserve the name "covariant derivative".

**Why no other axioms? What if we *strengthened* by demanding $\nabla_X(s + t) = \nabla_X s + \nabla_X t$ plus full $C^\infty(M)$-linearity in $s$?** Then again the operation would be a tensor field, not a derivative. There is exactly the right amount of structure in the two axioms: $C^\infty$-linearity in $X$ (to give localisation to a point), and Leibniz in $s$ (to make it a derivative). One could ask why we did not also demand metric-compatibility ($Xg(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$) or torsion-freeness ($\nabla_X Y - \nabla_Y X = [X, Y]$) — but these require a metric (the first) or the bundle to be $TM$ (the second), and we want the axioms to apply to a general vector bundle without extra structure. The two axioms here are exactly what is needed to *define a connection*; metric-compatibility and torsion-freeness are extra conditions one can *impose* on a connection, and which together select the unique [[Def - Levi-Civita Connection|Levi-Civita connection]] when both are imposed on $TM$ with a Riemannian metric.

**A different vector bundle changes the connection.** A connection on $TM$ differentiates vector fields; a connection on $T^*M$ differentiates 1-forms (induced from the $TM$ connection by Leibniz); a connection on the trivial line bundle $M \times \mathbb{C}$ differentiates complex-valued functions (the trivial connection $\nabla_X f = X(f)$, plus possibly a "gauge correction" $\nabla_X f = X(f) + A(X)f$ for some 1-form $A$ — this is the **electromagnetic connection**, with $A$ the gauge potential). A connection on the spinor bundle of a spin manifold differentiates spinors (the **spin connection**). The axioms are the *same* in all cases — only the bundle changes. This universality is the conceptual reason for stating the axioms at the level of an arbitrary vector bundle: the same definition unlocks differential geometry, electromagnetism, Yang-Mills theory, and the Dirac equation simultaneously.

**The forward-reference test of the axioms: the fundamental theorem requires both.** The [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]] says the metric uniquely determines a connection on $TM$ that is also torsion-free and metric-compatible. The proof works precisely because of the two connection axioms: $C^\infty$-linearity in $X$ ensures the value at $p$ depends only on $X(p)$ (which lets the Koszul formula be a *pointwise* identity), and the Leibniz rule in $s$ allows the symmetrisation manipulation that produces the Koszul formula. If we had only $\mathbb{R}$-linearity in $X$, the Koszul formula would not work because the values at different points would not be independently constrained. If we had only $\mathbb{R}$-linearity in $s$, the Leibniz step that converts $X g(Y, Z)$ into $g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ would not be available. Both axioms are forced by what the theorem demands.

---

# The Definition

Let $E \to M$ be a smooth vector bundle over a smooth manifold $M$. An **affine connection** (also called a **connection** or **covariant derivative**) on $E$ is an operation
$$
\nabla : \mathfrak{X}(M) \times \Gamma(E) \to \Gamma(E), \qquad (X, s) \mapsto \nabla_X s
$$
that is $\mathbb{R}$-bilinear and satisfies, for all smooth functions $f \in C^\infty(M)$, vector fields $X \in \mathfrak{X}(M)$, and sections $s \in \Gamma(E)$:

1. **$C^\infty(M)$-linearity in $X$.** $\nabla_{fX}s = f\,\nabla_X s$.

2. **Leibniz rule in $s$.** $\nabla_X(fs) = X(f)\,s + f\,\nabla_X s$.

A connection on $TM$ is called an **affine connection on $M$**. When $E$ is a vector bundle, we sometimes write **linear connection** to emphasise the vector-bundle setting (in contrast to connections on more general fibre bundles or principal bundles).

The section $\nabla_X s$ is the **covariant derivative** of $s$ in the direction of $X$.

Equivalently, the data of a connection on $E$ is a $C^\infty$-linear map
$$
\nabla : \Gamma(E) \to \Gamma(T^*M \otimes E), \qquad s \mapsto \nabla s,
$$
called the **covariant differential**, satisfying the Leibniz rule $\nabla(fs) = df \otimes s + f\,\nabla s$. The two formulations are related by $(\nabla s)(X) = \nabla_X s$, and the $C^\infty$-linearity of $\nabla s$ in $X$ comes from the $C^\infty$-linearity axiom for $\nabla_X s$.

**Local coordinates.** In a local frame $(e_1, \ldots, e_k)$ for $E$ over a neighbourhood $U$, the connection is determined by the $k^2$ sections $\nabla e_b = e_a \otimes \omega^a{}_b$ where $\omega^a{}_b \in \Omega^1(U)$ are the **connection 1-forms** in the frame (see [[Def - Connection 1-Forms (Cartan)]]). For a general section $s = s^a e_a$:
$$
\nabla_X s = \nabla_X(s^a e_a) = X(s^a)\,e_a + s^a \nabla_X e_a = \bigl[X(s^b) + \omega^b{}_a(X)\,s^a\bigr]e_b.
$$
When $E = TM$ and $(e_i) = (\partial_i)$ is a coordinate frame, $\omega^k{}_j = \Gamma^k_{ij}\,dx^i$ where $\Gamma^k_{ij}$ are the [[Def - Christoffel Symbols|Christoffel symbols]] of the connection in the chart.

**The space of connections.** Connections on a fixed vector bundle $E$ form an *affine space* modelled on $\Gamma(T^*M \otimes \mathrm{End}\,E)$ — the space of $\mathrm{End}(E)$-valued 1-forms. Given two connections $\nabla, \nabla'$, the difference $A := \nabla' - \nabla$ is $C^\infty(M)$-bilinear (the Leibniz terms cancel), so it is a *tensor field*: $A_X s$ is $C^\infty$-linear in both arguments. Conversely, given any connection $\nabla$ and any $A \in \Gamma(T^*M \otimes \mathrm{End}\,E)$, the operation $\nabla' := \nabla + A$ is again a connection. So once one connection is in hand, all others are obtained by adding tensor fields; the space of connections is non-empty on every vector bundle (by partition-of-unity construction) and has the structure of an affine space.

---

# Categorical / Structural Definition

The cleanest categorical reformulation is as follows. Let $E \to M$ be a smooth vector bundle and let $\mathcal{D}(E) = \mathrm{Der}_\mathbb{R}(\Gamma(E))$ denote the $\mathbb{R}$-linear endomorphisms of $\Gamma(E)$. A **connection** on $E$ is an $\mathbb{R}$-linear map
$$
\nabla : \mathfrak{X}(M) \to \mathcal{D}(E), \qquad X \mapsto \nabla_X,
$$
that is $C^\infty(M)$-linear (so $\nabla_{fX} = f\nabla_X$, no derivation correction in $X$) and lands in **derivations over $X$**: each $\nabla_X$ satisfies $\nabla_X(fs) = X(f)s + f\nabla_X s$. The pair (linearity in $X$, derivation in $s$) is the categorical content.

Equivalently, in the language of jet bundles: a connection on $E$ is a splitting of the short exact sequence
$$
0 \to T^*M \otimes E \to J^1 E \to E \to 0,
$$
where $J^1 E$ is the **first jet bundle** of $E$ — the bundle whose fibre at $p$ consists of equivalence classes of sections of $E$ near $p$ modulo agreement up to first order. The jet sequence breaks the data of "a section and its first-order behaviour" into "the section" plus "the first-order behaviour modulo the section". A splitting of the sequence is exactly a way to extract the first-order behaviour given a section — i.e., a covariant derivative.

This jet-bundle reformulation generalises naturally. A second-order connection (giving covariant second derivatives) is a splitting of $J^2 E \to J^1 E$. A **principal connection** on a principal $G$-bundle $P \to M$ is a $G$-equivariant splitting of $0 \to V(P) \to TP \to \pi^*(TM) \to 0$, where $V(P)$ is the vertical [[Def - Subbundle|subbundle]] (the kernel of $d\pi$). When $E$ is the vector bundle associated to a principal $G$-bundle via a representation, principal-bundle connections induce vector-bundle connections of the kind defined here. This is the bridge to [[Gauge Theory — Series Map|gauge theory]].

---

# Relate to Other Fields / Compression

The cleanest compression: **a connection is a covariant generalisation of "partial derivative" that takes sections of a bundle to sections of the same bundle, twisted by a 1-form.** The flat connection on $M \times \mathbb{R}^k \to M$ (the trivial bundle) is just $\nabla_X(s^1, \ldots, s^k) = (X(s^1), \ldots, X(s^k))$ — the componentwise directional derivative. A *general* connection is this naive operation plus a "twist" $\omega^a{}_b X$, where $\omega^a{}_b$ are the connection 1-forms. The twist is what couples the components of $s$ as you transport — and it is what allows the connection to be non-flat (have curvature).

From the physics-of-gauge-theory side, a connection is a **gauge potential**. The electromagnetic vector potential $A_\mu$ is, mathematically, the local 1-form $\omega$ of a connection on a $U(1)$-bundle, with the covariant derivative being $D_\mu = \partial_\mu + iA_\mu$ acting on complex-valued wavefunctions. Yang-Mills gauge potentials $A^a_\mu$ are local 1-forms of a connection on a principal $SU(N)$-bundle (or its associated representation bundles). The transformation law $\Gamma' = g^{-1}\Gamma g + g^{-1}dg$ ([[Thm - Gauge Transformation Law for Connection 1-Forms]]) is exactly the gauge-transformation law of the gauge potential.

**True name:** The "true name" of a connection is the **horizontal distribution** in the total space of the bundle. Given a connection $\nabla$ on $E \to M$, one can define a distribution $H \subset TE$ (the **horizontal subbundle**) that is everywhere complementary to the vertical subbundle $V = \ker(d\pi)$, where $\pi : E \to M$ is the projection. The distribution $H$ encodes "what it means to move in $E$ without moving the vector" — i.e., parallel transport along a curve in $M$ lifts uniquely to a curve in $E$ tangent to $H$. The operation $\nabla_X s$ is then the vertical part of $ds(X)$ (the "vertical component of the rate of change"), with the horizontal direction being what is "parallel" by convention. This geometric picture is what generalises to principal bundles and is the conceptual root of the **Ehresmann connection** definition.

---

# Examples / Corollaries

**Is an instance: the flat connection on $M \times \mathbb{R}^k$.** The trivial vector bundle $E = M \times \mathbb{R}^k$ over any smooth manifold admits the **flat connection** $\nabla_X(s^1, \ldots, s^k) = (X(s^1), \ldots, X(s^k))$ — just componentwise directional differentiation. This is the prototypical connection: all $\omega^a{}_b = 0$ in the standard frame, the covariant derivative is the partial derivative, and the curvature is zero. Every connection on every bundle reduces locally to the flat connection plus a "twist" — this is the content of the [[Def - Connection 1-Forms (Cartan)|connection 1-forms]].

**Is an instance: the Levi-Civita connection on $TM$ for a Riemannian manifold $(M, g)$.** The unique torsion-free metric-compatible connection on $TM$, given in coordinates by $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$ with $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. This is the connection of choice in Riemannian geometry, and the existence-uniqueness is the content of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem]]. See [[Def - Levi-Civita Connection]].

**Is an instance: the tangential connection on an embedded submanifold.** For $S \hookrightarrow \mathbb{R}^N$ an embedded submanifold with the induced metric, define $\nabla^S_X Y := (\nabla^{\mathbb{R}^N}_X Y)^\top$, the orthogonal projection of the flat $\mathbb{R}^N$-derivative onto $T_p S$. This is a connection on $TS$, it is the Levi-Civita connection of the induced metric, and it is the original Levi-Civita construction (1917) — see [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

**Is an instance: the electromagnetic connection on a $U(1)$-bundle.** On the trivial complex line bundle $E = M \times \mathbb{C}$, the operation $\nabla_X s = X(s) + i A(X) s$ for a real 1-form $A$ on $M$ is a connection. Its curvature 2-form is $F = i\,dA$, the electromagnetic field strength. This is the geometric formulation of electromagnetism in [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory|Gauge Theory VII]], and it is the prototype of the Yang-Mills gauge potential.

**Is an instance: the Weitzenböck connection on a parallelisable manifold.** If $M$ is parallelisable (i.e., $TM$ is trivial as a vector bundle), pick a global frame $(e_1, \ldots, e_n)$ and declare $\nabla e_i = 0$ for all $i$. Extend by Leibniz to define a connection on all of $TM$. This is the **Weitzenböck connection** — it is flat (curvature $0$) but has nonzero torsion on every non-abelian Lie group. The Lie [[Def - Group|groups]] $S^1, S^3 = SU(2), S^7$ are the only parallelisable spheres (a deep result of J. F. Adams using K-theory). See [[Ex - The Tangent Bundle of a Lie Group has a Canonical Flat Connection]].

**Is NOT an instance: the Lie derivative $\mathcal{L}_X Y = [X, Y]$.** The Lie bracket is an $\mathbb{R}$-bilinear operation $\mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$ satisfying the Leibniz rule $[X, fY] = X(f)Y + f[X, Y]$ in the second argument, so it satisfies axiom (2). But it *fails* axiom (1): $[fX, Y] = f[X, Y] - Y(f)X$, with an inhomogeneous $-Y(f)X$ term, so it is not $C^\infty(M)$-linear in $X$. The Lie bracket is therefore *not* a connection — its value at $p$ depends on more than $X(p)$, and it cannot define parallel transport in any meaningful sense. This is the textbook reason why "differentiation in the direction of $X$" needs the connection axioms specifically and is not captured by the Lie derivative.

**Is NOT an instance: the partial derivative $\partial_i V^k$ on a curved manifold.** In a coordinate chart, the operation $\nabla_{\partial_i}V := (\partial_i V^k)\partial_k$ (forget the Christoffel correction) satisfies both axioms locally — it is $C^\infty$-linear in $\partial_i$ and Leibniz in $V$. But it is *chart-dependent*: in a different chart, the values of $\partial_i V^k$ change, and the operation does not define a connection on the abstract manifold $M$. To get a chart-independent operation, the Christoffel correction $+\Gamma^k_{ij}V^j$ is essential — this is the inhomogeneous piece of the transformation law that makes the corrected expression a tensor.

**Corollary (the difference of two connections is a tensor).** If $\nabla, \nabla'$ are two connections on the same bundle $E$, the difference $A := \nabla' - \nabla$ is $C^\infty(M)$-bilinear: $A_X s = \nabla'_X s - \nabla_X s$ satisfies $A_{fX}s = f A_X s$ (both connections are $C^\infty$-linear in $X$, the Leibniz terms vanish on the difference) and $A_X(fs) = f A_X s$ (Leibniz terms cancel). So $A \in \Gamma(T^*M \otimes \mathrm{End}\,E)$ is a genuine tensor field; this is what makes the space of connections an affine space modelled on $\Gamma(T^*M \otimes \mathrm{End}\,E)$.

**Corollary (existence of connections on every vector bundle).** Every smooth vector bundle admits at least one connection, constructed by partition of unity: on each trivialising open set $U_\alpha$ use the flat connection $\nabla^\alpha$, then patch with a smooth partition of unity $\{\psi_\alpha\}$ to define $\nabla := \sum_\alpha \psi_\alpha \nabla^\alpha$. The convex-combination structure preserves the axioms (because both axioms are linear in $\nabla$), and the result is a smooth connection on $E$. This is the existence half of the existence-uniqueness story: connections always exist; uniqueness requires extra conditions (e.g., torsion-free + metric-compatible on $TM$).

**Calibration check.** If you can perform the following three verifications, you have understood the definition. (i) Show that the operation $\nabla_X Y := [X, Y]$ is not a connection on $TM$ — find the $C^\infty$-linearity failure explicitly. (ii) Verify that the flat connection on $\mathbb{R}^n$ in Cartesian coordinates ($\nabla_X V = (X(V^1), \ldots, X(V^n))$) satisfies both axioms. (iii) Given two connections $\nabla, \nabla'$ on $TM$, write down the $(1,2)$-tensor $A(X, Y) = \nabla'_X Y - \nabla_X Y$ and verify it is $C^\infty(M)$-bilinear; check that for the Levi-Civita and Weitzenböck connections on $\mathrm{SU}(2) = S^3$, $A(X, Y) = \tfrac{1}{2}[X, Y]$ on left-invariant fields.

---

# Unlocked by This

> [!tip] Parallel Transport and the Geodesic Equation *(from Riemannian Geometry)*
> Once a connection is in hand, [[Def - Parallel Transport|parallel transport]] along any curve is the linear-ODE solution $\dot V^k + \Gamma^k_{ij}\dot\gamma^i V^j = 0$, and the **geodesic equation** $\nabla_{\dot\gamma}\dot\gamma = 0$ is the special case "parallel-transport the velocity along itself". The geodesics of the Levi-Civita connection are the locally length-minimising curves — the analogues of straight lines on a curved manifold. The full theory of geodesics, the exponential map, normal coordinates, Hopf-Rinow completeness, the first and second variation of arc length, and Jacobi fields is the content of [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles|Riemannian Geometry II]].

> [!tip] The Riemann Curvature Tensor *(from Riemannian Geometry)*
> Given any affine connection, the **Riemann curvature tensor** is $R(X, Y)Z := \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$, a $(1, 3)$-tensor measuring the failure of $\nabla$ to commute. Equivalently it measures the path-dependence of parallel transport. The symmetries of $R$ (antisymmetry in $X, Y$; for the Levi-Civita case, antisymmetry in the lower index pair, pair symmetry, first **Bianchi identity**) are the structural content of [[Riemannian Geometry III — Riemann Curvature and Topology|Riemannian Geometry III]]. The contractions of $R$ — sectional curvature, Ricci, scalar — are the inputs to the curvature-to-topology theorems (Bonnet-Myers, Cartan-Hadamard, Synge, Gauss-Bonnet) and to the **Einstein field equations** of general relativity.

> [!tip] Gauge Theory: Connections on Principal Bundles *(from Gauge Theory)*
> Generalising from a vector bundle $E \to M$ to a principal $G$-bundle $P \to M$ gives the framework of [[Gauge Theory IV — Connections and Curvature on Principal Bundles|principal-bundle connections]] — the geometric setting of **Yang-Mills theory**. A principal connection is a $\mathfrak{g}$-valued 1-form on the total space $P$ that is $G$-equivariant and reduces to the Maurer-Cartan form on fibres; its curvature 2-form is the **Yang-Mills field strength** $F = dA + A \wedge A$, and the Yang-Mills equations are $d_A \star F = 0$. Electromagnetism is the abelian case $G = U(1)$; the strong and electroweak interactions are the non-abelian cases $G = SU(3)$ and $G = SU(2) \times U(1)$. The Levi-Civita connection on $TM$ corresponds to the principal connection on the orthonormal frame bundle of $(M, g)$ for $G = O(n)$. Once the principal-bundle setting is internalised, all of differential geometry and all of gauge theory are seen as the same theory of connections.

> [!tip] Chern-Weil Theory and Characteristic Classes *(from Algebraic Topology)*
> The curvature 2-form of any connection on a complex vector bundle gives, via invariant polynomials (trace, determinant, Pfaffian), a closed differential form whose cohomology class is independent of the connection — a **characteristic class**. The Chern classes $c_k(E) \in H^{2k}(M; \mathbb{Z})$ are constructed this way, and their integrals (Chern numbers) are integers that count topological invariants of $E$ — e.g., the topological charge of a Yang-Mills instanton on $\mathbb{R}^4$ is $\tfrac{1}{8\pi^2}\int_{\mathbb{R}^4}\mathrm{tr}(F \wedge F)$, the second Chern number of the $SU(2)$-bundle. The **Gauss-Bonnet theorem** for a closed surface, $\int_M K\,dA = 2\pi\chi(M)$, is the simplest Chern-Weil identity. The full theory is the content of **Chern-Weil theory** and is previewed in [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Levi-Civita Connection"
  - "Def - Riemannian Metric"
  - "Riemannian Geometry I — Connections and Covariant Differentiation"
tags: [geometry, gauge-theory, riemannian-geometry, principal-bundles]
---

# Problem Statement

Let $(M, g)$ be a Riemannian manifold of dimension $n$, and let $F^O(M) \to M$ be the **orthonormal frame bundle** — the principal $O(n)$-bundle whose fibre over $x \in M$ consists of orthonormal frames of $T_xM$ (linear isometries $\mathbb{R}^n \to T_xM$). Let $\nabla$ be the [[Def - Levi-Civita Connection|Levi-Civita connection]] of $(M, g)$.

**Show that the Levi-Civita connection — defined in [[Riemannian Geometry I — Connections and Covariant Differentiation|Riemannian Geometry I]] as the unique torsion-free metric-compatible connection on $TM$ — corresponds (via [[Thm - Principal Connection Induces a Connection on Every Associated Bundle]]) to a unique principal connection $\omega$ on $F^O(M)$ with values in $\mathfrak{o}(n) = $ antisymmetric $n \times n$ matrices.**

**(a)** Construct $\omega$ explicitly: for a frame $f = (e_1, \ldots, e_n) \in F^O(M)$ at $x$, define $\omega$ by specifying $\omega(X) \in \mathfrak{o}(n)$ for $X \in T_f F^O(M)$. *Hint:* split $X$ into vertical (rotation of frame) and horizontal (parallel transport) components.

**(b)** Verify the two axioms of a principal connection: **verticality** ($\omega(\xi^*) = \xi$ for $\xi \in \mathfrak{o}(n)$) and **equivariance** ($R_g^*\omega = \mathrm{Ad}_{g^{-1}}\omega$ for $g \in O(n)$).

**(c)** Show that the local gauge potential $A = s^*\omega$ in a local orthonormal frame $s = (e_1, \ldots, e_n)$ is the matrix of Cartan connection 1-forms $\omega^a{}_b$ from [[Riemannian Geometry I — Connections and Covariant Differentiation|RG I §1.3]]: $\nabla_X e_b = e_a\,\omega^a{}_b(X)$.

**Recall:**

A principal $G$-bundle $P \to M$: smooth surjective submersion, free transitive right $G$-action on each fibre, locally trivial.

A connection 1-form on $P$: $\mathfrak{g}$-valued 1-form $\omega$ satisfying ![[Def - Connection 1-Form on a Principal Bundle#The Definition]]

The Levi-Civita connection $\nabla$ of $(M, g)$ is the unique torsion-free metric-compatible connection on $TM$: $\nabla_X Y - \nabla_Y X = [X, Y]$ and $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ for all vector fields $X, Y, Z$ on $M$.

---

# Convergent Strategy

**Problem class:** This is a *correspondence-of-formalisms* problem. The general pattern is: given a connection in one formalism (here: vector-bundle covariant derivative on $TM$), construct the equivalent connection in another formalism (here: principal-bundle connection 1-form on $F^O(M)$). The exercise establishes the bridge between [[Riemannian Geometry I — Connections and Covariant Differentiation|Riemannian Geometry I]]'s "Cartan structural equations" formalism and the [[Def - Connection 1-Form on a Principal Bundle|principal-bundle formalism]] of this chapter.

**Assumption pattern:** A Riemannian manifold $(M, g)$ provides a metric on every tangent space, hence the existence of orthonormal frames (locally). The Levi-Civita connection's existence and uniqueness are guaranteed by [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|Riemannian Geometry's fundamental theorem]]. The structure group $O(n)$ acts on orthonormal frames by post-composition with orthogonal matrices.

**Theorem routing:** [[Thm - Principal Connection Induces a Connection on Every Associated Bundle|Induced-connection theorem]] gives the bridge: every vector-bundle connection corresponds uniquely to a principal connection on the frame bundle. The route is "Levi-Civita on $TM$ → principal connection on $F(M)$ → restrict to $F^O(M)$ via metric-compatibility". The metric-compatibility of Levi-Civita means parallel transport preserves orthonormality, which is exactly the condition for the principal connection to descend to the orthonormal frame bundle.

**Key decision point:** The non-obvious choice is whether to view $\omega$ as defined *on* $F^O(M)$ (the principal-bundle picture) or via *pullback* by a section (the local-trivialisation / gauge-potential picture). Both views are necessary: the principal picture for the axioms, the local picture for matching to the Cartan structural equations of [[Riemannian Geometry I — Connections and Covariant Differentiation|RG I §1.3]]. The decision is to *do both* and verify their equivalence in part (c).

---

# Legal Operations Used

1. **Operation 1 (pull back a connection along a section).** $A = s^*\omega$ for a local section $s$ — here, an orthonormal frame on a chart $U$.

5. **Operation 5 (decompose tangent vectors into vertical and horizontal).** Tangent vectors at a frame $f \in F^O(M)$ split into "horizontal" (parallel transport of $f$ along a base direction) and "vertical" (rotation of $f$ within its fibre by an antisymmetric matrix). Use this decomposition to define $\omega$.

7. **Operation 7 (use the induced connection $\nabla^\rho$).** The defining representation $\rho : O(n) \hookrightarrow \mathrm{GL}(n)$ on $\mathbb{R}^n$ produces, via the induced-connection theorem, the connection on the associated bundle $F^O(M) \times_\rho \mathbb{R}^n = TM$. This recovers the original Levi-Civita connection on $TM$.

---

# Hints

> [!note]- Hint 1
> The orthonormal frame bundle is a *reduction* of the general linear frame bundle $F(M) = \mathrm{Fr}(TM)$ (a principal $\mathrm{GL}(n)$-bundle) to its $O(n)$-subgroup. The reduction is possible because $(M, g)$ has a Riemannian metric: at each $x$, the metric $g_x$ singles out the orthonormal frames of $T_xM$, and the right $O(n)$-action preserves orthonormality.

> [!note]- Hint 2
> A tangent vector $X \in T_f F^O(M)$ at a frame $f = (e_1, \ldots, e_n)$ has two contributions:
> - **Horizontal part:** infinitesimal parallel transport of $f$ along a vector $\pi_* X \in T_xM$ (where $x = \pi(f)$).
> - **Vertical part:** infinitesimal rotation of the frame by an element $A \in \mathfrak{o}(n)$ (an antisymmetric matrix).
> The principal connection $\omega$ should return *only* the vertical part — the rotation $A$ — as an element of $\mathfrak{o}(n)$.

> [!note]- Hint 3
> Concretely: for a local orthonormal frame $s = (e_1, \ldots, e_n)$ on a chart $U$, the **Cartan connection 1-forms** $\omega^a{}_b$ are defined by $\nabla e_b = e_a \otimes \omega^a{}_b$ (or equivalently $\nabla_X e_b = e_a\,\omega^a{}_b(X)$ for $X \in T_xM$). The matrix-valued $\omega^a{}_b$ is *antisymmetric* in $(a, b)$ iff $\nabla$ is metric-compatible — which the Levi-Civita connection is. So $\omega^a{}_b \in \Omega^1(U; \mathfrak{o}(n))$.

> [!note]- Hint 4
> The local gauge potential $A = s^*\omega$ is exactly the matrix $\omega^a{}_b$ in part (c). Verification: by the induced-connection formula, $\nabla_X s = (d s)(X) + d\rho(A(X))(s) = \rho(s)\cdot 0 + A(X) \cdot s$ (in component notation, since the section "lifted" is just the identity in the chosen trivialisation). Matching coefficients gives $\nabla e_b = e_a\,\omega^a{}_b$, i.e., $A^a{}_b = \omega^a{}_b$.

> [!note]- Hint 5
> For equivariance: under a change of orthonormal frame $s_\beta = s_\alpha \cdot g$ for $g : U \to O(n)$, the matrices of Cartan connection 1-forms transform by $\omega^a{}_b \mapsto g^{-1}\omega^a{}_b g + g^{-1}dg$ — exactly the gauge transformation law of [[Thm - Gauge Transformation Law for Local Connection 1-Forms]]. This is the *change-of-orthonormal-frame law* familiar from Riemannian geometry.

---

# Solution

**Plan:** The proof breaks into three steps. Step 1 constructs $\omega$ on $F^O(M)$ by specifying its value on horizontal and vertical tangent vectors using the Levi-Civita connection's parallel transport. Step 2 verifies the two axioms (verticality and equivariance). Step 3 identifies the local gauge potential $A = s^*\omega$ with the matrix of Cartan connection 1-forms from [[Riemannian Geometry I — Connections and Covariant Differentiation|RG I §1.3]].

**Step 1: Construct $\omega$ on $F^O(M)$.**

At each frame $f = (e_1, \ldots, e_n) \in F^O(M)_x$, define $\omega \in T_f^* F^O(M) \otimes \mathfrak{o}(n)$ by

> [!note]- Derivation
> The tangent space $T_f F^O(M)$ decomposes as
> $$
> T_f F^O(M) = V_f F^O(M) \oplus H_f F^O(M),
> $$
> where $V_f$ is the vertical subspace (kernel of $d\pi$, generated by fundamental vector fields of $\mathfrak{o}(n)$) and $H_f$ is the horizontal subspace (the parallel-transport lift of $T_xM$ via Levi-Civita).
> 
> The **vertical-space isomorphism** identifies $V_f F^O(M) \cong \mathfrak{o}(n)$: each $\xi \in \mathfrak{o}(n)$ generates a fundamental vector field $\xi^*$, whose value at $f$ is the velocity of $t \mapsto f \cdot \exp(t\xi)$, i.e., infinitesimal rotation of the frame by $\xi$.
> 
> The **horizontal subspace** $H_f$ is the lift of $T_xM$ via Levi-Civita parallel transport: for each $v \in T_xM$, the horizontal lift $\tilde v_f$ is the unique tangent vector to $F^O(M)$ at $f$ that projects to $v$ and is "parallel-transport" (i.e., the curve $\gamma$ with $\gamma(0) = x, \dot\gamma(0) = v$ lifts uniquely to a horizontal curve $\tilde\gamma$ in $F^O(M)$ with $\tilde\gamma(0) = f$ and $\dot{\tilde\gamma}(0) = \tilde v_f$).
> 
> **Define $\omega$:** for $X \in T_f F^O(M)$ with decomposition $X = X^V + X^H$:
> $$
> \omega(X) := (\text{inverse vertical-space isomorphism})(X^V) \in \mathfrak{o}(n).
> $$
> Equivalently, $\omega(X^H) = 0$ on horizontal vectors and $\omega(\xi^*_f) = \xi$ on fundamental vector fields.

**Step 2: Verify the connection axioms.**

> [!note]- Derivation
> **Verticality:** $\omega(\xi^*) = \xi$ for $\xi \in \mathfrak{o}(n)$. This is immediate from the construction: $\xi^*$ is vertical at every $f$, so $\omega(\xi^*_f) = (\text{inverse vertical-space iso})(\xi^*_f) = \xi$. ✓
> 
> **Equivariance:** $R_g^*\omega = \mathrm{Ad}_{g^{-1}}\omega$ for $g \in O(n)$. Need: $\omega_{f \cdot g}((R_g)_*X) = \mathrm{Ad}_{g^{-1}}\omega_f(X)$ for $X \in T_f F^O(M)$.
> 
> Decompose $X = X^V + X^H$. The right action $R_g$ carries vertical to vertical (preserves the fibre) and horizontal to horizontal (this is the *key step*, and follows from the metric-compatibility of Levi-Civita: parallel transport preserves orthonormality, so $O(n)$-action commutes with horizontal lifts). So $(R_g)_*X = (R_g)_*X^V + (R_g)_*X^H$ with the first vertical at $f \cdot g$ and the second horizontal.
> 
> $\omega_{f \cdot g}((R_g)_*X) = (\text{inverse vertical iso at } f \cdot g)((R_g)_*X^V) = $ ?
> 
> The vertical iso at $f \cdot g$ sends $\eta \in \mathfrak{o}(n)$ to the fundamental vector field $\eta^*$ at $f \cdot g$, which is the velocity of $t \mapsto (f \cdot g)\exp(t\eta) = f \cdot (g\,\exp(t\eta)) = f \cdot \exp(t\,g\eta g^{-1})\cdot g$ (for the orthonormal frame bundle, the right action is matrix multiplication of frame components). So $\eta^*_{f \cdot g} = (R_g)_*(g\eta g^{-1})^*_f = (R_g)_*(\mathrm{Ad}_g\eta)^*_f$. Inverting: the vertical iso at $f \cdot g$ sends a vertical vector $(R_g)_*\eta^*_f$ to $\mathrm{Ad}_{g^{-1}}\eta$.
> 
> Applied to $X^V = \omega_f(X)^*_f$: $(R_g)_*X^V = (R_g)_*(\omega_f(X))^*_f$ has vertical iso $\mathrm{Ad}_{g^{-1}}\omega_f(X)$.
> 
> So $\omega_{f \cdot g}((R_g)_*X) = \mathrm{Ad}_{g^{-1}}\omega_f(X)$ — equivariance verified. ✓

**Step 3: Local gauge potential equals Cartan connection 1-forms.**

> [!note]- Derivation
> Let $s = (e_1, \ldots, e_n) : U \to F^O(M)$ be a local orthonormal frame. The local gauge potential is $A := s^*\omega \in \Omega^1(U; \mathfrak{o}(n))$.
> 
> By [[Thm - Principal Connection Induces a Connection on Every Associated Bundle|the induced-connection theorem]], the connection on the associated bundle $TM = F^O(M) \times_\rho \mathbb{R}^n$ (with $\rho : O(n) \hookrightarrow \mathrm{GL}(n)$ the defining rep) is $\nabla^\rho \psi = d\psi + d\rho(A)\psi$. For $\rho$ the defining rep, $d\rho = $ identity on $\mathfrak{o}(n) \subset \mathfrak{gl}(n)$. So $\nabla^\rho\psi = d\psi + A\psi$ where $A$ acts on $\psi \in \mathbb{R}^n$ as a matrix.
> 
> In the basis $(e_a)$, a section $V \in \Gamma(TM)$ has components $V^a$, and the covariant derivative is $\nabla_X V = (X V^a + A^a{}_b(X) V^b)e_a$. This matches the standard formula $\nabla_X V^a = X V^a + \omega^a{}_b(X) V^b$ from [[Riemannian Geometry I — Connections and Covariant Differentiation|RG I]] iff $A^a{}_b = \omega^a{}_b$.
> 
> Specifically: $\nabla_X e_b = e_a \omega^a{}_b(X)$ by definition of the Cartan connection 1-forms; in the principal-bundle formulation, $\nabla_X e_b = e_a A^a{}_b(X)$ by the induced-connection formula. So $A^a{}_b = \omega^a{}_b$ — the local gauge potential is the matrix of Cartan connection 1-forms.

> [!note]- Complete formal solution
> **Setup.** $(M, g)$ a Riemannian manifold, $F^O(M) \to M$ its orthonormal frame bundle (principal $O(n)$-bundle), $\nabla$ the Levi-Civita connection on $TM$.
> 
> **Step 1: Construct $\omega$.** At each $f \in F^O(M)$, define $\omega \in T_f^* F^O(M) \otimes \mathfrak{o}(n)$ to be the projection onto the vertical subspace (via the metric-compatible horizontal distribution induced by Levi-Civita parallel transport), composed with the inverse vertical-space isomorphism $V_f F^O(M) \xrightarrow{\sim} \mathfrak{o}(n)$, $\xi^*_f \mapsto \xi$.
> 
> **Step 2: Verify axioms.**
> - *Verticality:* $\omega(\xi^*_f) = \xi$ by construction.
> - *Equivariance:* the right action $R_g$ preserves horizontality (by metric-compatibility), and the vertical-space isomorphism intertwines the right action with $\mathrm{Ad}$: $\omega_{f \cdot g}((R_g)_*X) = \mathrm{Ad}_{g^{-1}}\omega_f(X)$.
> 
> **Step 3: Local form.** For a local orthonormal section $s = (e_1, \ldots, e_n) : U \to F^O(M)$, the local gauge potential $A = s^*\omega \in \Omega^1(U; \mathfrak{o}(n))$ has components $A^a{}_b = \omega^a{}_b$, where $\omega^a{}_b$ are the [[Riemannian Geometry I — Connections and Covariant Differentiation|Cartan connection 1-forms]] defined by $\nabla e_b = e_a\,\omega^a{}_b$. The antisymmetry $\omega^a{}_b = -\omega^b{}_a$ (equivalent to $A \in \mathfrak{o}(n)$) is the metric-compatibility of Levi-Civita.
> 
> **Conclusion.** The Levi-Civita connection on $TM$ is equivalent to a principal connection on $F^O(M)$ with values in $\mathfrak{o}(n)$, with the local gauge potential equal to the matrix of Cartan connection 1-forms. The torsion-freeness of Levi-Civita corresponds to **Cartan's first structural equation** $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$ for the canonical 1-form $\theta^a$ on $F^O(M)$, and the curvature 2-form $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$ gives the Riemann tensor components in the orthonormal frame. ∎

---

# Key Takeaways

**The Levi-Civita connection is a principal connection on the orthonormal frame bundle.** This is the bridge between the *vector-bundle* picture of Riemannian geometry (where the connection is a covariant derivative $\nabla : \Gamma(TM) \to \Gamma(T^*M \otimes TM)$) and the *principal-bundle* picture (where the connection is a $\mathfrak{o}(n)$-valued 1-form on $F^O(M)$). The two pictures are equivalent — they are two views of the same geometric structure. The vector-bundle picture is what Levi-Civita and Christoffel used in the 1900s; the principal-bundle picture is what Cartan introduced in the 1920s and is now the standard formulation. Recognising this equivalence is the entry point to understanding "gravity as a gauge theory" — the Levi-Civita connection is a gauge field, with structure group $O(n)$ (or $SO(n)$ for orientable manifolds, or $\mathrm{Spin}(n)$ for spin manifolds).

**Metric-compatibility = horizontal distribution preserves orthonormality = principal connection on $F^O(M)$.** A general affine connection on $TM$ corresponds to a principal connection on the *general* linear frame bundle $F(M)$ (a $\mathrm{GL}(n)$-bundle). The metric-compatibility condition $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ is exactly the condition that parallel transport preserves orthonormality, equivalently that the horizontal distribution on $F(M)$ descends to a horizontal distribution on the reduced bundle $F^O(M) \subset F(M)$. So metric-compatibility *is* the principal-bundle reduction. This is one of the most important conceptual unifications in modern differential geometry.

**Trigger-reaction pattern: "Cartan connection 1-forms $\omega^a{}_b$" → "local gauge potential of the Levi-Civita principal connection".** Whenever you encounter the matrix $\omega^a{}_b$ in Riemannian geometry, recognise it as the local gauge potential $A = s^*\omega$ in a chosen orthonormal frame. The Cartan structural equations $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$ (torsion) and $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$ (curvature) are the principal-bundle structural equation in matrix form, with the Levi-Civita connection picked out by the two conditions (torsion-free + metric-compatible).

**The bridge to physics: "gravity is a gauge theory of $O(n)$".** Once the Levi-Civita connection is recognised as a principal connection, the analogy with Yang-Mills theory becomes precise: gravity is gauge theory with structure group $O(n)$ (or $\mathrm{Spin}(n)$ for spin manifolds), gauge potential $\omega^a{}_b$, field strength = Riemann curvature tensor. The Einstein-Hilbert action $\int R\sqrt{-g}\,d^n x$ is a "scalar curvature" Lagrangian — different from the Yang-Mills $-\tfrac{1}{4}\int F^a_{\mu\nu}F^{a\,\mu\nu}$ Lagrangian, but built from the same kind of geometric data. The differences (gravity is dynamical metric vs. fixed metric; gravity has the $\sqrt{-g}$ measure; gravity has a different action principle) are real, but the geometric foundation is the same.

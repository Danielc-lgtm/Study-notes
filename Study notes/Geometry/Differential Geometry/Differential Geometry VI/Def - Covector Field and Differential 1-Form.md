---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Cotangent Space and Cotangent Bundle"
  - "Def - Section of a Vector Bundle"
  - "Def - The Smooth Functions Ring"
tags: [geometry, differential-geometry, cotangent, forms]
---

# Notation

$M$ is a smooth manifold of dimension $n$, and $T^*M$ is its cotangent bundle ([[Def - Cotangent Space and Cotangent Bundle]]). A covector field — equivalently a 1-form — is denoted $\omega, \eta : M \to T^*M$, with values $\omega_p \in T_p^*M$ at each point. The space of smooth global 1-forms is denoted $\Omega^1(M) = \Gamma(T^*M)$. In a chart $(U, x^i)$, a 1-form has the unique local expression $\omega|_U = \omega_i \, dx^i$ for smooth functions $\omega_i \in C^\infty(U)$ — its **component functions** in the coordinate frame.

---

# Axiom Motivation

A covector field is what becomes of "linear measurements of tangent vectors" when the point $p$ is allowed to vary smoothly across $M$. Pointwise, at $p$, a covector is a linear map $T_pM \to \mathbb{R}$; collectively across $M$, a smoothly varying choice of such measurements is a covector field. The 1-form terminology comes from the higher-form context: a 1-form is a degree-$1$ differential form, the first in the sequence $\Omega^0(M), \Omega^1(M), \Omega^2(M), \dots$ that culminates in the full exterior algebra.

The defining condition is structural: a covector field is a smooth section of $T^*M$, in the sense of [[Def - Section of a Vector Bundle]]. Smoothness of the section is the precise meaning of "smoothly varying" at the level of sections. Equivalently, smoothness of $\omega : M \to T^*M$ in the manifold sense, with $T^*M$ carrying the bundle's smooth structure.

What is forced by demanding **smoothness** of the section rather than just continuity? Smoothness is what allows differential operations on 1-forms: the exterior derivative $d : \Omega^1(M) \to \Omega^2(M)$ requires smoothness; the Lie derivative $\mathcal{L}_X \omega$ requires smoothness; pullback by smooth maps preserves smoothness. Without smoothness, the apparatus of differential forms does not function.

What is forced by demanding the section be **defined on all of $M$**? This is what makes the 1-form a *global* object. Local 1-forms (defined on open $U \subseteq M$) are useful and arise naturally; global 1-forms are the special case where the local pieces extend to $M$. The transition from local to global is the key nontrivial step: not every smoothly-varying-locally object extends globally, and the obstruction is topological.

What is forced by demanding the covector at each $p$ be **linear** on $T_pM$? Linearity is built into the definition of $T_p^*M$: covectors *are* linear functionals on tangent vectors. The 1-form structure on $\Omega^1(M)$ inherits this linearity: $\omega_p(v + w) = \omega_p(v) + \omega_p(w)$ and $\omega_p(cv) = c\omega_p(v)$ at each point. This linearity is what allows pairing $\omega$ with a vector field $X$ pointwise to produce a smooth function $\omega(X) \in C^\infty(M)$.

What about the $C^\infty(M)$-module structure on $\Omega^1(M)$? Multiplication of a 1-form $\omega$ by a smooth function $f$ is defined pointwise: $(f\omega)_p := f(p) \omega_p$, where the right-hand side uses the vector-space structure of $T_p^*M$. This makes $\Omega^1(M)$ a $C^\infty(M)$-module, and the module structure is the natural algebraic structure of 1-forms: addition, scalar-function multiplication, and the resulting *tensoriality* — every "tensor field" operation respects this structure.

A useful consequence of the module structure: every smooth function $f \in C^\infty(M)$ produces a 1-form $df$ via the differential ([[Def - The Differential of a Function as a 1-Form]]), and $f \, dg$ for $f, g \in C^\infty(M)$ is the product of a 1-form with a smooth function, giving another 1-form. In coordinates, $\omega = \omega_i \, dx^i$ — every 1-form is locally a $C^\infty(U)$-linear combination of the coordinate 1-forms $dx^i$.

What if we **strengthened** by demanding 1-forms be *exact* — that is, of the form $df$ for some smooth function $f$? Then we would only have a strict subset of 1-forms. The form $d\theta$ on $S^1$, where $\theta$ is the angular coordinate (well-defined locally but not globally), is the classic example: $d\theta$ is a globally defined smooth 1-form on $S^1$, but there is no smooth function $\theta : S^1 \to \mathbb{R}$ with $d\theta$ equal to the differential. So exact 1-forms are strictly fewer than 1-forms in general; the difference is detected by [[Def - de Rham Cohomology|de Rham cohomology]].

What if we **weakened** by allowing 1-forms with rough (distributional) coefficients? Then we get currents — 1-currents are continuous linear functionals on smooth compactly-supported vector fields. Currents generalize 1-forms and are essential in geometric measure theory.

---

# The Definition

Let $M$ be a smooth manifold and $T^*M$ its cotangent bundle ([[Def - Cotangent Space and Cotangent Bundle]]).

A **covector field** on $M$ is a smooth section of the cotangent bundle: a smooth map
$$\omega : M \to T^*M$$
such that $\pi \circ \omega = \mathrm{id}_M$, where $\pi : T^*M \to M$ is the bundle projection. Equivalently, $\omega(p) =: \omega_p \in T_p^*M$ for every $p \in M$, with the assignment $p \mapsto \omega_p$ smooth.

A **differential 1-form** on $M$ is exactly the same thing: a smooth covector field. The terminology is a matter of context — "covector field" emphasizes the linear-algebra perspective (a smoothly varying covector); "differential 1-form" emphasizes the differential-forms perspective (a degree-$1$ form in the exterior algebra).

The space of smooth 1-forms is denoted
$$\Omega^1(M) := \Gamma(T^*M),$$
a real vector space and a $C^\infty(M)$-module under pointwise operations: $(\omega + \eta)_p := \omega_p + \eta_p$, $(c\omega)_p := c \omega_p$ for $c \in \mathbb{R}$, $(f \omega)_p := f(p) \omega_p$ for $f \in C^\infty(M)$.

**Coordinate expression.** In a chart $(U, \varphi)$ with coordinate functions $x^1, \dots, x^n$, every 1-form on $U$ has a unique expression
$$\omega|_U = \omega_i \, dx^i \quad (\text{summation over } i = 1, \dots, n)$$
for unique smooth functions $\omega_i \in C^\infty(U)$, called the **component functions** of $\omega$ in the coordinate frame. The smoothness of $\omega$ is equivalent to the smoothness of all $\omega_i$.

**Pairing with vector fields.** For $\omega \in \Omega^1(M)$ and $X \in \mathfrak{X}(M)$ (a smooth vector field), the pointwise pairing $\omega_p(X_p)$ produces a smooth function $M \to \mathbb{R}$, denoted $\omega(X)$. This pairing is $\mathbb{R}$-bilinear and $C^\infty(M)$-bilinear: $\omega(fX + gY) = f \omega(X) + g \omega(Y)$ and $(f\omega + g\eta)(X) = f \omega(X) + g \eta(X)$. The pairing realises $\Omega^1(M) = \mathrm{Hom}_{C^\infty(M)}(\mathfrak{X}(M), C^\infty(M))$ — 1-forms are exactly the $C^\infty(M)$-linear maps from vector fields to scalar functions.

---

# Relate to Other Fields / Compression

A 1-form is **the smoothly-varying-with-$p$ version of a linear functional on a vector space**. Pointwise, $\omega_p$ is a linear functional on $T_pM$; globally, $\omega$ is a smooth choice of such functionals over $M$. The bundle structure of $T^*M$ packages the "smoothly varying" data, and the section condition is exactly the smoothness requirement.

A 1-form is also the **degree-$1$ object in the algebra of differential forms**. The full algebra $\Omega^\bullet(M) = \bigoplus_k \Omega^k(M)$ is a graded-commutative algebra over $C^\infty(M)$, with the wedge product and the exterior derivative. The 1-forms generate this algebra: every $k$-form is a $C^\infty(M)$-linear combination of wedges $dx^{i_1} \wedge \cdots \wedge dx^{i_k}$, and these arise from 1-forms by repeated wedging.

A 1-form is **the integrand of a line integral**. The line integral $\int_\gamma \omega$ along a curve $\gamma : [a, b] \to M$ is defined by pulling back $\omega$ via $\gamma$ (giving a 1-form on $[a, b]$, which is $f(t) dt$ for some smooth $f$) and integrating $f$ over $[a, b]$. The naturality of this construction — invariance under reparameterization, additivity over concatenated paths — is the structural reason 1-forms are the "right" integrands on curves.

**True name:** the true name of a 1-form is "**a $C^\infty(M)$-linear functional on the module of vector fields**", or equivalently "**a smooth choice of linear measurement of tangent vectors at every point of $M$**". The first phrasing is the categorical content (1-forms are dual to vector fields in the module sense); the second is the operational content (1-forms eat vectors and produce numbers).

A useful slogan: **functions are $0$-forms; 1-forms are differentials of functions plus more; $k$-forms generalize**. The sequence $\Omega^0(M) \to \Omega^1(M) \to \Omega^2(M) \to \cdots$ via the exterior derivative is the de Rham complex, and the cohomology of this complex detects the topology of $M$.

In **classical electromagnetism** on Minkowski space, the electromagnetic potential $A$ is a 1-form: $A = -\phi \, dt + A_i \, dx^i$ where $\phi$ is the scalar potential and $A_i$ are the spatial components of the vector potential. Maxwell's equations become $dA = F$ and $d \star F = J$ — purely differential-form equations.

In **statistical thermodynamics**, the entropy and energy variations $dS, dU$ and the work-and-heat 1-form $\delta Q = T dS - p \, dV$ etc. all live in $\Omega^1$ of state space.

---

# Examples / Corollaries

**Is an instance — the differential $df$ of a smooth function.** For $f \in C^\infty(M)$, $df \in \Omega^1(M)$ with $df_p(v) = v(f)$ for $v \in T_pM$, and in coordinates $df = (\partial f / \partial x^i) dx^i$. See [[Def - The Differential of a Function as a 1-Form]]. Every smooth function gives a 1-form.

**Is an instance — the coordinate 1-forms $dx^i$.** The coordinate functions $x^i : U \to \mathbb{R}$ are smooth, and their differentials $dx^i$ are 1-forms on $U$, forming a local frame for $T^*U$. Every other 1-form on $U$ is a $C^\infty(U)$-linear combination of them.

**Is an instance — the angle form on $S^1$.** The 1-form $d\theta$ on $S^1$ (defined locally on charts and patched globally) is a smooth, nowhere-vanishing 1-form, but it is *not* exact — there is no globally defined smooth function $\theta : S^1 \to \mathbb{R}$ with $d\theta$ as its differential. This is the prototypical example of a closed but not exact 1-form.

**Is an instance — the "winding form" on the punctured plane.** On $\mathbb{R}^2 \setminus \{0\}$, the 1-form $\omega = (x \, dy - y \, dx) / (x^2 + y^2)$ is smooth, closed ($d\omega = 0$), and *not* exact — see [[Ex - A Conservative 1-Form on R² Minus Origin]]. Its integral around any loop encircling the origin once is $2\pi$.

**Is an instance — the electromagnetic potential 1-form.** On Minkowski space $\mathbb{R}^4$, the electromagnetic potential $A = -\phi \, dt + A_x \, dx + A_y \, dy + A_z \, dz$ is a 1-form, with $\phi$ the scalar potential and $A_x, A_y, A_z$ the components of the vector potential. The field strength $F = dA$ is a 2-form, and Maxwell's equations have a clean form-theoretic statement.

**Is an instance — the tautological 1-form on $T^*Q$.** For any manifold $Q$, the cotangent bundle $T^*Q$ carries the canonical 1-form $\theta = p_i \, dq^i$, foundational for symplectic geometry and Hamiltonian mechanics.

**Is NOT a 1-form — a non-smooth covector field.** Define $\omega : \mathbb{R} \to T^*\mathbb{R}$ by $\omega_p = |p| \, dx$ — pointwise this is a covector at each $p$, but the coefficient function $|p|$ is not smooth at $0$, so this is a continuous but not smooth section. It is not a 1-form in the smooth-differential-forms sense.

**Is NOT a 1-form — a higher-degree form.** A 2-form like $\omega = dx \wedge dy$ on $\mathbb{R}^2$ is not a 1-form; it lives in $\Omega^2(\mathbb{R}^2)$, the bundle of alternating $2$-linear forms. The wedge product reduces degree-counting precisely.

**Is NOT a 1-form — a function (a 0-form).** A smooth function $f : M \to \mathbb{R}$ is a $0$-form, not a $1$-form. The exterior derivative $d$ takes $0$-forms to $1$-forms ($df$), and the input and output spaces are different.

**Corollary — $\Omega^1(M) = \mathrm{Hom}_{C^\infty(M)}(\mathfrak{X}(M), C^\infty(M))$.** The space of 1-forms is naturally isomorphic to the $C^\infty(M)$-module of $C^\infty(M)$-linear maps from vector fields to smooth functions. This is the *tensoriality characterization*: 1-forms are exactly the $C^\infty(M)$-linear functionals on vector fields.

**Corollary — pointwise zero implies global zero.** If $\omega_p = 0 \in T_p^*M$ for all $p$, then $\omega = 0$ in $\Omega^1(M)$. The 1-form is determined by its pointwise values, and the zero 1-form is the unique 1-form vanishing everywhere.

**Corollary — every 1-form admits a coordinate expression.** In any chart $(U, x^i)$, every 1-form has the unique expression $\omega = \omega_i \, dx^i$ for smooth $\omega_i \in C^\infty(U)$, by the local-frame criterion ([[Thm - Local Frames Span Sections]]).

**Calibration check.** Verify that for $f \in C^\infty(\mathbb{R}^n)$, the 1-form $df = (\partial f/\partial x^i) dx^i$ pairs with a vector field $X = X^j \partial/\partial x^j$ to give $df(X) = X^j \partial f/\partial x^j = X(f)$, the directional derivative. Verify that $(f\omega)(X) = f \omega(X)$ pointwise, confirming the $C^\infty(M)$-module structure. Convince yourself that $\Omega^1(M)$ is naturally a $C^\infty(M)$-module by checking the module axioms directly.

---

# Unlocked by This

> [!tip] Higher Differential Forms *(from Differential Geometry VIII)*
> Once 1-forms are in hand, the wedge product $\omega \wedge \eta$ produces 2-forms, and iteration gives all higher $k$-forms. The space $\Omega^k(M) = \Gamma(\Lambda^k T^*M)$ is the smooth sections of the $k$-th exterior power of the cotangent bundle. The wedge product makes $\Omega^\bullet(M) = \bigoplus_k \Omega^k(M)$ a graded-commutative algebra, and the exterior derivative $d : \Omega^k \to \Omega^{k+1}$ is its derivation. See [[Def - Differential Form]] for the Euclidean case and [[Differential Geometry VIII — Differential Forms]] for the manifold case.

> [!tip] Closed and Exact 1-Forms *(from this topic)*
> A 1-form $\omega$ is **closed** if $d\omega = 0$, **exact** if $\omega = df$ for some smooth function $f$. Exact implies closed (by $d^2 = 0$), but the converse fails: $H^1_{dR}(M) := \{\text{closed 1-forms}\}/\{\text{exact 1-forms}\}$ measures the gap, and is a topological invariant of $M$ — see [[Thm - A Closed 1-Form on a Simply Connected Manifold is Exact]] and [[Def - Closed and Exact Forms]].

> [!tip] Pullback and Naturality *(from this topic)*
> Covector fields pull back along arbitrary smooth maps $F : M \to N$: $F^*\omega \in \Omega^1(M)$ for $\omega \in \Omega^1(N)$ — see [[Def - Pullback of a Covector Field]]. This is *contravariance* — $F^*$ goes from $N$ to $M$, opposite to $F$ — and the operation respects the exterior derivative: $F^*(dg) = d(g \circ F)$. The pullback is the structural reason 1-forms are "natural integrands" — they pull back along any smooth map without needing the map to be invertible.

> [!tip] Symplectic and Contact Geometry *(from Differential Geometry XII and beyond)*
> Closed nondegenerate 2-forms on even-dimensional manifolds — built from 1-forms via wedge product and exterior derivative — define **symplectic manifolds**, the geometric setting of Hamiltonian mechanics. Nondegenerate 1-forms on odd-dimensional manifolds (whose kernel distribution is maximally non-integrable) define **contact manifolds**, dual to symplectic and important in optics, thermodynamics, and geometric mechanics. The 1-form theory of this chapter is the entry point to both.

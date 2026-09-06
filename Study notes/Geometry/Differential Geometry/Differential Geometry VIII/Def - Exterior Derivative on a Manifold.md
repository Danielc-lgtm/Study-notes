---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - The Wedge Product on a Manifold"
  - "Def - Smooth Manifold"
  - "Def - Smooth Function on a Manifold"
  - "Def - The Differential of a Function as a 1-Form"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold. $\Omega^k(M)$ is the space of smooth differential $k$-forms on $M$, $\Omega^\bullet(M) = \bigoplus_k \Omega^k(M)$ is the exterior algebra. Forms are denoted $\omega, \eta$ with degrees $k, \ell$. In a chart $(U, x^i)$, $\partial_j = \partial/\partial x^j$ and $dx^I = dx^{i_1} \wedge \cdots \wedge dx^{i_k}$ for an increasing multi-index $I$. The differential of a function $f \in C^\infty(M)$ is the $1$-form $df$, satisfying $df(X) = X(f)$ for any vector field $X$ ([[Def - The Differential of a Function as a 1-Form]]). $X \in \mathfrak{X}(M)$ is a vector field. A form $\omega$ is **closed** if $d\omega = 0$ and **exact** if $\omega = d\eta$ for some $\eta$. The full registry is on [[Differential Geometry VIII — Differential Forms]].

---

# Axiom Motivation

The motivation begins where MA IV left off: in $\mathbb{R}^n$ we have an operator $d$ on differential forms, defined by a coordinate formula, that generalizes the gradient and unifies grad/curl/div. We want to lift it to a manifold. The obstacle is that the chart formula is not *manifestly* chart-independent — and any coordinate-based definition on a manifold must produce the same form regardless of which chart we use to define it. Two paths give the right operator, and they coincide.

**Path 1: characterize $d$ by its algebraic properties on functions.** Demand that $d$ be a graded derivation that (i) is $\mathbb{R}$-linear, (ii) agrees with the differential of functions on $\Omega^0$, (iii) satisfies the graded Leibniz rule with respect to wedge, and (iv) squares to zero. These four properties uniquely determine $d$ on all forms, on any smooth manifold. This is the content of [[Thm - Uniqueness of the Exterior Derivative]]: there is at most one such operator on $\Omega^\bullet(M)$, and the chart formula defines one. The uniqueness is what justifies the chart formula: any operator satisfying the axioms must agree with $d$, and conversely $d$ is forced by the axioms.

Why these four properties and not others? Each does specific work. **Linearity** is the bare minimum for $d$ to be useful. **Agreement with the differential on functions** is the boundary condition: $d$ must reduce to a known operator on $\Omega^0$, and the only canonical first-order operator from functions to $1$-forms is the differential. **Graded Leibniz** is the bookkeeping rule for $d$ on products, with the sign $(-1)^{\deg\omega}$ accounting for the wedge's anticommutativity; without it $d$ would not be a derivation, and the chart formulas would not patch. **$d^2 = 0$** is the deep condition, encoding the equality of mixed partial derivatives: $d(df) = \sum_{j,m} \partial_m \partial_j f\,dx^m \wedge dx^j$, where $\partial_m \partial_j$ is symmetric (Schwarz) and $dx^m \wedge dx^j$ is antisymmetric, so the sum vanishes. This is not an extra axiom imposed on $d$; it is an automatic consequence of the coordinate formula. We list it as an axiom because it pins down the operator's behavior on higher-degree forms, and because it is the seed of the entire de Rham theory.

**Path 2: define $d$ chart by chart, then prove naturality.** In a chart $(U, x^i)$, the formula $d(\sum'_I \omega_I\,dx^I) = \sum'_I d\omega_I \wedge dx^I$ is meaningful — $d\omega_I$ is the differential of a function. Define $d$ this way in every chart; the chart formula is well-defined on overlaps because (i) the four axiomatic properties uniquely characterize $d$, (ii) the chart formula satisfies them, and (iii) two chart-defined operators on the overlap both satisfy the axioms, so they agree.

The Lee Theorem 14.24 combines the two paths: existence is via the chart formula, and uniqueness is via the axiomatic characterization.

**What breaks if we drop any axiom?**

- **Drop linearity.** Then $d$ would not be a function in the usual sense. Disallowed by the requirement that $d$ be useful.

- **Drop the boundary condition $df =$ differential.** Then $d$ is undetermined on functions; many other operators (e.g., the zero operator, or multiplication by a constant) trivially satisfy the other three axioms.

- **Drop graded Leibniz.** Then $d(f \cdot g)$ for two functions need not equal $df \cdot g + f \cdot dg$; the chart formula would not patch correctly across overlaps. Moreover, $d$ on higher-degree forms would be unconstrained — there are many degree-raising linear operators satisfying $d^2 = 0$ that fail Leibniz, and none of them is geometric.

- **Drop $d^2 = 0$.** Then there would be no de Rham complex, no notion of closed-versus-exact, no Stokes-style adjunction with $\partial$. Worst of all, the chart formula no longer satisfies the other axioms compatibly; without $d^2 = 0$ the alternation-of-wedge-against-symmetry-of-mixed-partials cancellation would not produce a well-defined operator. The axiom is forced.

**Why is there a *unique* operator and not many?** Because the axioms are highly constraining. On functions, $df =$ differential is forced. On a $1$-form $u\,dv$ (every $1$-form is locally a sum of these), graded Leibniz forces $d(u\,dv) = du \wedge dv + u \cdot d(dv) = du \wedge dv$ (using $d^2 = 0$). Inducting on degree, every higher-degree form is locally a wedge of $1$-forms times functions, and $d$ of it is determined by Leibniz. So the four axioms pin $d$ down to a single operator. This is a substantive uniqueness theorem, not an obvious algebraic identity.

**Why bother with the axiomatic characterization when the chart formula works?** Because the chart formula is *opaque* — proofs that use it must work in coordinates and verify chart-independence. Proofs using the axiomatic characterization are usually much cleaner. For example, to show $F^*$ commutes with $d$, the chart proof requires substituting the pullback formula into the chart formula and tediously matching terms; the axiomatic proof observes that $F^*d$ satisfies the four axioms (because $F^*$ commutes with the differential of functions, with linearity, with $\wedge$, and with $d^2 = 0$), hence equals $d$ by uniqueness. Same conclusion, dramatically cleaner argument.

---

# The Definition

Let $M$ be a smooth manifold (with or without boundary). The **exterior derivative** is the unique $\mathbb{R}$-linear operator
$$d : \Omega^k(M) \longrightarrow \Omega^{k+1}(M) \quad \text{for all } 0 \le k \le n-1$$
(with $d \equiv 0$ for $k \geq n$) satisfying:

1. **Linearity:** $d$ is $\mathbb{R}$-linear.
2. **Boundary condition on functions:** For $f \in \Omega^0(M) = C^\infty(M)$, $df$ is the ordinary differential, the $1$-form characterized by $df(X) = X(f)$ for every vector field $X$.
3. **Graded Leibniz rule:** For $\omega \in \Omega^k(M)$ and $\eta \in \Omega^\ell(M)$,
$$d(\omega \wedge \eta) = d\omega \wedge \eta + (-1)^k\,\omega \wedge d\eta.$$
4. **Nilpotence:** $d \circ d = 0$.

The existence and uniqueness of such an operator is [[Thm - Uniqueness of the Exterior Derivative]].

**Coordinate expression.** In any smooth chart $(U, x^i)$, a $k$-form $\omega = \sum'_I \omega_I\,dx^I$ has exterior derivative
$$d\omega = \sum'_I d\omega_I \wedge dx^I = \sum'_I \sum_{j=1}^n \frac{\partial \omega_I}{\partial x^j}\,dx^j \wedge dx^I.$$
This is [[Thm - Coordinate Expression for the Exterior Derivative]]. On a $0$-form, this reduces to $df = \sum_j(\partial f/\partial x^j)\,dx^j$.

**Invariant formula for $1$-forms.** For $\omega \in \Omega^1(M)$ and vector fields $X, Y$,
$$d\omega(X, Y) = X\omega(Y) - Y\omega(X) - \omega([X, Y]),$$
where $[X, Y]$ is the [[Def - The Lie Bracket of Vector Fields|Lie bracket]]. This formula is manifestly chart-independent — every term is a scalar function defined without reference to a chart. The higher-degree analogue (Lee Proposition 14.32) is
$$d\omega(X_0, \dots, X_k) = \sum_i(-1)^i X_i\,\omega(X_0, \dots, \widehat{X_i}, \dots, X_k) + \sum_{i<j}(-1)^{i+j}\omega([X_i, X_j], X_0, \dots, \widehat{X_i}, \dots, \widehat{X_j}, \dots, X_k),$$
where hats indicate omitted arguments. For $k = 1$ this recovers the simpler formula.

**Closed and exact.** A form $\omega \in \Omega^k(M)$ is **closed** if $d\omega = 0$, and **exact** if there exists $\eta \in \Omega^{k-1}(M)$ with $\omega = d\eta$. By nilpotence, every exact form is closed: $d(d\eta) = 0$. The converse — every closed form is exact — holds *locally* (the Poincaré lemma) but not *globally*. See [[Def - Closed and Exact Forms]] and [[Thm - The Poincaré Lemma]].

**Naturality.** For any smooth map $F : M \to N$ and any $\omega \in \Omega^k(N)$,
$$F^*(d\omega) = d(F^*\omega).$$
This is [[Thm - Pullback Commutes with d for Forms on Manifolds]]. It says $d$ is intrinsic — the same operator in every chart and compatible with every smooth map.

**Vector calculus correspondence.** Under the identification of vector fields on $\mathbb{R}^3$ with $1$-forms (via the flat $\flat$ from the Euclidean metric) and with $2$-forms (via $X \mapsto \iota_X(dx \wedge dy \wedge dz)$), the exterior derivative acts as: gradient on $0$-forms, curl on $1$-forms, divergence on $2$-forms. The vector-calculus identities $\operatorname{curl}\operatorname{grad} = 0$ and $\operatorname{div}\operatorname{curl} = 0$ are both instances of $d^2 = 0$ in different degrees.

---

# Categorical Definition

The exterior derivative is the **differential** of the de Rham cochain complex of $M$. A **cochain complex** is a sequence of vector spaces connected by linear maps with consecutive composites zero:
$$\Omega^0(M) \xrightarrow{d} \Omega^1(M) \xrightarrow{d} \cdots \xrightarrow{d} \Omega^n(M),$$
and the property $d \circ d = 0$ is exactly the cochain-complex axiom. The **cohomology** of this complex is the **de Rham cohomology** of $M$:
$$H^k_{dR}(M) = \frac{\ker(d : \Omega^k \to \Omega^{k+1})}{\operatorname{im}(d : \Omega^{k-1} \to \Omega^k)}.$$
By de Rham's theorem these vector spaces are isomorphic to the singular cohomology of $M$ with real coefficients — a remarkable bridge from calculus to topology.

The naturality identity $F^*(d\omega) = d(F^*\omega)$ says that $d$ is a **natural transformation** between contravariant functors $\Omega^k \Rightarrow \Omega^{k+1}$ from smooth manifolds to vector spaces. Concretely, $d$ does not depend on a choice of coordinates: it is the *same* operator in every smooth chart, and the chart-by-chart definitions agree on overlaps because they all satisfy the four-axiom characterization. A reader who finds the language of natural transformations heavy can read this paragraph as the strongest possible statement of chart-independence: not merely "$d$ has a coordinate-free description" but "$d$ commutes, compatibly, with every smooth map between every pair of manifolds".

Together with the [[Def - The Wedge Product on a Manifold|wedge product]], $(\Omega^\bullet(M), \wedge, d)$ is a **differential graded algebra (DGA)**: an associative graded algebra with a degree-$1$ derivation $d$ satisfying $d^2 = 0$ and the graded Leibniz rule. DGAs are the basic objects of rational [[Def - Homotopy|homotopy]] theory; the de Rham DGA is one of the central examples.

---

# Relate to Other Fields / Compression

**The exterior derivative is the universal generalization of grad, curl, and div.** In $\mathbb{R}^3$, the three vector-calculus operators look unrelated: grad takes functions to vector fields, curl takes vector fields to vector fields, div takes vector fields to functions. They have separate notations, separate product rules, separate identities. The calculus of forms reveals that they are *one* operator $d$, acting in degrees $0, 1, 2$ respectively. The identities $\operatorname{curl}\operatorname{grad} = 0$ and $\operatorname{div}\operatorname{curl} = 0$ are both $d^2 = 0$. The product rules $\operatorname{grad}(fg) = f\nabla g + g\nabla f$, $\operatorname{curl}(fF) = f\operatorname{curl}F + \nabla f \times F$, $\operatorname{div}(F \times G) = (\operatorname{curl}F) \cdot G - F \cdot \operatorname{curl}G$ are all instances of the single graded Leibniz rule. The reason the classical picture looks like a zoo is the dimension-three coincidence $\binom{3}{1} = \binom{3}{2} = 3$, which lets $1$-forms and $2$-forms both be disguised as vector fields; in general dimensions, there is only $d$. **The bridge to [[Def - The Exterior Derivative]] in MA IV is verbatim**: $d$ on a manifold reduces in any chart to $d$ on $\mathbb{R}^n$.

**True name:** The exterior derivative is "the unique linear operator extending the differential of functions, satisfying the graded Leibniz rule, and squaring to zero."

A trigger-reaction pattern: **see "verify that an operator equals $d$" → invoke the uniqueness theorem and check the four axioms**. The reactive habit is to compute in coordinates; the productive habit is to check the axioms. The axiom check is usually trivial — boundary condition on functions plus linearity plus Leibniz plus $d^2 = 0$ — and the uniqueness theorem then does all the rest.

**Bridge to gauge theory.** The exterior derivative is the *flat* prototype of a **covariant exterior derivative** $d_\nabla$ on a vector bundle. On a vector bundle $E \to M$ with connection $\nabla$, sections can be extended to bundle-valued forms, and $d_\nabla$ acts on these. But — crucially — $d_\nabla^2$ need *not* vanish. The obstruction is the **curvature** $\mathcal{F}_\nabla = d_\nabla^2 \in \Omega^2(M; \operatorname{End}(E))$. In gauge theory the connection is encoded as a Lie-algebra-valued $1$-form $A$, and the curvature is $F = dA + \tfrac12[A, A]$. The whole story of general relativity and Yang–Mills theory lives in the failure of $d^2 = 0$ once one moves from forms-on-$M$ to forms-with-values-in-a-bundle.

**Bridge to PDE.** Many partial differential equations of mathematical physics can be packaged as form-equations. Maxwell: $dF = 0$, $d\star F = J$. The wave equation: $d(\star d\phi) = 0$ on a Lorentzian manifold. The Yang–Mills equation: $d_A(\star F_A) = 0$. The exterior derivative is the universal first-order differential operator, and the form-theoretic packaging often reveals symmetries and conservation laws (via $d^2 = 0$) that are invisible in coordinate language.

---

# Examples / Corollaries

**Is an instance — differential of a function.** For $f(x, y, z) = x^2 y + z$, $df = 2xy\,dx + x^2\,dy + dz$. The coefficient triple $(2xy, x^2, 1)$ is $\nabla f$. The differential of a $0$-form is the gradient repackaged as a $1$-form.

**Is an instance — $d$ of a $1$-form is the curl.** For $\omega = P\,dx + Q\,dy + R\,dz$ on $\mathbb{R}^3$,
$$d\omega = \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dx \wedge dy + \left(\frac{\partial R}{\partial x} - \frac{\partial P}{\partial z}\right)dx \wedge dz + \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}\right)dy \wedge dz.$$
The coefficients are the three components of $\operatorname{curl}(P, Q, R)$, with appropriate signs. The full Grad–Curl–Div correspondence is in [[Ex - The Exterior Derivative on R^3 Recovers Grad-Curl-Div]].

**Is an instance — $d$ of a $2$-form is the divergence.** For $\omega = u\,dy \wedge dz + v\,dz \wedge dx + w\,dx \wedge dy$ on $\mathbb{R}^3$,
$$d\omega = \left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z}\right)dx \wedge dy \wedge dz = (\operatorname{div}(u, v, w))\,dx \wedge dy \wedge dz.$$
The divergence is $d$ on $2$-forms in [[Def - Dimension|dimension]] three.

**Is an instance — the closed-not-exact angular form.** On $\mathbb{R}^2\setminus\{0\}$, write
$$\omega=P\,dx+Q\,dy,\qquad P=-\frac{y}{x^2+y^2},\quad Q=\frac{x}{x^2+y^2}.$$
Then $d\omega=(\partial_xQ-\partial_yP)\,dx\wedge dy$. Direct differentiation gives
$$\partial_xQ=\frac{y^2-x^2}{(x^2+y^2)^2}=\partial_yP,$$
so $d\omega=0$. Nevertheless $\int_{S^1}\omega=2\pi$, so $\omega$ is not exact; see [[Ex - A Form that is Closed but Not Exact on the Punctured Plane]].

**Is NOT an instance — partial differentiation alone.** The operator "differentiate each coefficient and put the result back where it was" is *not* the exterior derivative. The exterior derivative wedges on a new $dx^j$, raising the degree; without that wedge the operator would not satisfy $d^2 = 0$, would not commute with pullbacks, and would not have an invariant formula. The degree-raising wedge is essential.

**Is NOT an instance — a Lie derivative.** The Lie derivative $\mathcal{L}_X\omega$ preserves the degree of $\omega$, while the exterior derivative raises it by one. They are related by Cartan's magic formula $\mathcal{L}_X = d\iota_X + \iota_X d$, but they are different operators.

**Corollary — exact $\Rightarrow$ closed.** If $\omega = d\eta$ then $d\omega = d(d\eta) = 0$ by nilpotence. This is the cheapest and most-used consequence: it is the mandatory *first test* for exactness — compute $d\omega$, and if it is nonzero, $\omega$ is not exact and the question is settled.

**Corollary — the de Rham complex is finite.** Since $\Omega^k(M) = 0$ for $k > n = \dim M$, the de Rham complex has length $n + 1$: $\Omega^0 \xrightarrow{d} \cdots \xrightarrow{d} \Omega^n$. The top cohomology $H^n_{dR}(M)$ is therefore the cokernel of $d : \Omega^{n-1} \to \Omega^n$, and is one-dimensional for compact connected oriented manifolds (de Rham's theorem applied to $H^n(M; \mathbb{R}) \cong \mathbb{R}$).

**Corollary — change of coordinates is a pullback.** A change of chart $\tilde x = F(x)$ pulls forms back: $d\tilde x^j = dF^j = \sum_i (\partial F^j/\partial x^i)\,dx^i$. Combined with $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$ and $F^*d = dF^*$, this implies that the chart formula for $d$ agrees on overlaps — which is exactly the well-definedness of $d$ as a global operator.

**Corollary — wedge with a closed form.** If $\eta$ is closed ($d\eta = 0$), then $d(\omega \wedge \eta) = d\omega \wedge \eta$ for any $\omega$, by graded Leibniz. This is a constant-source-of-simplification when one factor of a product is known to be closed.

**Calibration check.** Compute $d(x\,dy)$ on $\mathbb{R}^2$ (answer: $dx \wedge dy$); compute $d(y\,dz \wedge dx)$ on $\mathbb{R}^3$ (answer: $dx \wedge dy \wedge dz$, after sign cancellation); verify $d(df) = 0$ for $f = x^2 y$ by direct computation; compute $d$ of $\omega = e^{xy}(dx + dy)$ on $\mathbb{R}^2$. If you can also state, without computing, why $d$ of a top-degree $n$-form on an $n$-manifold is zero (answer: because $\Omega^{n+1}(M) = 0$), you have understood the operator.

---

# Unlocked by This

> [!tip] de Rham Cohomology *(from Algebraic Topology)*
> Because $d \circ d = 0$, closed forms contain exact forms, and the quotient $H^k_{dR}(M) = \ker d / \operatorname{im} d$ is well-defined. By **de Rham's theorem**, $H^k_{dR}(M) \cong H^k(M; \mathbb{R})$, the singular cohomology with real coefficients. The dimension counts $k$-dimensional holes. The whole construction lives one identity downstream from $d^2 = 0$.

> [!tip] The Poincaré Lemma *(this chapter)*
> On a contractible region, every closed form is exact ([[Thm - The Poincaré Lemma]] in MA IV). The proof constructs a primitive by integrating along the contracting homotopy, and the construction uses only $d$ and integration. The global failure of closed-to-exact, on a non-contractible manifold, is what de Rham cohomology measures.

> [!tip] Curvature as the Failure of $d^2 = 0$ *(from Gauge Theory / General Relativity)*
> Replacing $d$ on $\Omega^\bullet(M)$ by the covariant exterior derivative $d_\nabla$ on bundle-valued forms, the identity $d^2 = 0$ generically *fails*. The obstruction is the **curvature** $2$-form $\mathcal{F}_\nabla = d_\nabla^2$. In gauge theory $F_A = dA + \tfrac12[A, A]$ is the curvature of a Lie-algebra-valued connection $A$; in Riemannian geometry the Riemann curvature tensor is the curvature of the Levi-Civita connection. The whole story of general relativity, Yang–Mills theory, and characteristic classes is the geometry of $d_\nabla^2 \neq 0$.

> [!tip] Hodge Decomposition *(from Hodge Theory)*
> On a compact oriented Riemannian manifold, the operator $d$ has a metric-dependent adjoint $d^*$, and the Hodge Laplacian $\Delta = dd^* + d^*d$ has finite-dimensional kernel. Every form decomposes uniquely as $\omega = d\alpha + d^*\beta + h$ with $\Delta h = 0$. Each de Rham class contains exactly one harmonic representative, giving $H^k_{dR}(M) \cong \{\text{harmonic } k\text{-forms}\}$ — the analytic incarnation of cohomology.

> [!tip] Yang–Mills and Maxwell Equations *(from Physics)*
> Maxwell's homogeneous equations $\nabla \cdot B = 0$, $\nabla \times E + \partial_t B = 0$ become the single statement $dF = 0$ for the field strength $2$-form. The inhomogeneous equations become $d\star F = J$. The Bianchi identity $dF = 0$ then implies, on a contractible region via the Poincaré lemma, that $F = dA$ for a potential $1$-form $A$, with gauge freedom $A \mapsto A + d\chi$ (the exact-form additions, which leave $dA$ unchanged). Yang–Mills theory generalizes to non-abelian connections.

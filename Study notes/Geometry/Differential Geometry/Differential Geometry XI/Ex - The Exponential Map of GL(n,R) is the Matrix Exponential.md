---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Exponential Map of a Lie Group"
  - "Def - One-Parameter Subgroup"
  - "Def - Left-Invariant Vector Field"
tags: [geometry, differential-geometry, lie-groups]
---

# Problem Statement

Show that the [[Def - Exponential Map of a Lie Group|exponential map]] $\exp_{\mathrm{GL}} : \mathfrak{gl}(n, \mathbb{R}) \to \mathrm{GL}(n, \mathbb{R})$ of the general linear group coincides with the **matrix exponential**:

$$\exp_{\mathrm{GL}}(A) = e^A := \sum_{k = 0}^{\infty} \frac{A^k}{k!} = I + A + \frac{A^2}{2} + \frac{A^3}{6} + \cdots$$

That is: for any $A \in \mathfrak{gl}(n, \mathbb{R}) = M(n, \mathbb{R})$, the abstract Lie-theoretic $\exp(A)$ equals the matrix exponential $e^A$.

**Recall:**

The exponential map $\exp : \mathfrak{g} \to G$ is defined by $\exp(X) = \gamma_X(1)$, where $\gamma_X : \mathbb{R} \to G$ is the unique [[Def - One-Parameter Subgroup|one-parameter subgroup]] with $\gamma_X'(0) = X$. Equivalently, $\gamma_X$ is the integral curve of the [[Def - Left-Invariant Vector Field|left-invariant vector field]] $X^L$ through the identity $e$. For $G = \mathrm{GL}(n, \mathbb{R})$, $\mathfrak{g} = \mathfrak{gl}(n, \mathbb{R}) = M(n, \mathbb{R})$ and $e = I$.

---

# Convergent Strategy

**Problem class:** Identification of an abstract Lie-theoretic construction (the exponential map) with a concrete classical construction (the matrix exponential). The route is: characterize each side as the solution of a specific ODE, show the ODEs coincide, conclude the solutions coincide.

**Assumption pattern:** $\mathrm{GL}(n, \mathbb{R})$ is an open subset of $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$, so curves in $\mathrm{GL}(n, \mathbb{R})$ are curves of matrices, and their derivatives are matrix-valued. The left-invariant vector field for $A \in \mathfrak{gl}(n)$ has value at $g \in \mathrm{GL}(n)$ given by $A^L|_g = gA$ (matrix multiplication), because left translation $L_g$ on $\mathrm{GL}(n) \subseteq M(n)$ is the linear map $h \mapsto gh$, with differential $h \mapsto gh$ at every point.

**Theorem routing:** Route is: (1) compute the left-invariant vector field $A^L$ as $A^L|_g = gA$. (2) Identify the integral curve of $A^L$ through $I$ as the solution of the matrix ODE $g'(t) = g(t) A$, $g(0) = I$. (3) Verify by direct computation that $g(t) = e^{tA}$ solves this ODE, where $e^{tA}$ is the matrix exponential. (4) Conclude $\gamma_A(t) = e^{tA}$, hence $\exp_{\mathrm{GL}}(A) = \gamma_A(1) = e^A$.

**Key decision point:** The non-obvious step is **computing the left-invariant vector field** $A^L|_g = gA$. The temptation is to expect $A^L|_g = A$ (constant matrix), but this is wrong — left translation on $\mathrm{GL}(n)$ is multiplication by $g$, not a translation in any additive sense, and the differential is *non-trivial*. Computing the left-invariant vector field correctly is the heart of the calculation.

---

# Legal Operations Used

1. **Compute the exponential map as the matrix exponential (operation 2 from the topic page).** This exercise is the foundational case: it establishes the identification $\exp_{\mathrm{GL}} = (\cdot \mapsto e^{(\cdot)})$ for $\mathrm{GL}(n)$, which then transfers to every matrix Lie subgroup $G \leq \mathrm{GL}(n)$ via [[Thm - Naturality of the Exponential Map|naturality]] applied to the inclusion.

2. **Recognize a one-parameter subgroup (operation 10 from the topic page).** The matrix exponential $t \mapsto e^{tA}$ is a one-parameter subgroup of $\mathrm{GL}(n)$ — smooth, homomorphism, $\gamma(0) = I$, $\gamma'(0) = A$. By uniqueness of one-parameter subgroups with a given initial velocity, this identifies it as $\gamma_A$.

---

# Hints

> [!note]- Hint 1
> $\mathrm{GL}(n, \mathbb{R})$ is an open subset of $M(n, \mathbb{R})$, so left translation $L_g : \mathrm{GL}(n) \to \mathrm{GL}(n)$ is the restriction of the linear map $L_g : M(n) \to M(n)$, $h \mapsto gh$. What is the differential of $L_g$ at $I$?

> [!note]- Hint 2
> Since $L_g(h) = gh$ is linear in $h$, its differential at any point — in particular at $I$ — is the same linear map: $d(L_g)_I : M(n) \to M(n)$, $A \mapsto gA$. So the left-invariant vector field with value $A$ at $I$ has value $A^L|_g = gA$ at any $g$.

> [!note]- Hint 3
> The integral curve of $A^L$ through $I$ is the smooth curve $g(t) \in \mathrm{GL}(n)$ satisfying $g'(t) = A^L|_{g(t)} = g(t) A$ and $g(0) = I$. This is a linear matrix ODE with constant coefficients (multiplication by $A$ on the right).

> [!note]- Hint 4
> Verify that $g(t) = e^{tA}$ satisfies $g'(t) = g(t) A$. Differentiate the series $e^{tA} = \sum_k (tA)^k/k!$ term by term and reassemble.

> [!note]- Hint 5
> By uniqueness of ODE solutions (or equivalently uniqueness of one-parameter subgroups with given initial velocity), $\gamma_A(t) = e^{tA}$. Evaluating at $t = 1$: $\exp_{\mathrm{GL}}(A) = \gamma_A(1) = e^A$.

---

# Solution

The proof identifies the integral curve defining $\exp_{\mathrm{GL}}(A)$ as the solution of a matrix ODE, then verifies the matrix exponential is that solution.

**Step 1: The left-invariant vector field for $A \in \mathfrak{gl}(n)$ has value $A^L|_g = gA$.**

Left translation on $\mathrm{GL}(n)$ is $L_g(h) = gh$ for $h \in \mathrm{GL}(n)$. Extending to $M(n)$ (the ambient vector space), this is the linear map $h \mapsto gh$. Linear maps have the same differential at every point, equal to the map itself: $d(L_g)_h = L_g$ as a linear map $M(n) \to M(n)$, with $d(L_g)_I(A) = gA$.

The left-invariant vector field $A^L$ for $A \in T_I \mathrm{GL}(n) = M(n)$ is defined by $A^L|_g = d(L_g)_I(A) = gA$.

> [!note]- Derivation
> $L_g : M(n) \to M(n)$, $h \mapsto gh$, is a linear map. Its differential at any point $h_0 \in M(n)$ is $d(L_g)_{h_0} : T_{h_0} M(n) \to T_{gh_0} M(n)$. Under the canonical identification $T_{h_0} M(n) \cong M(n)$ (for the vector space $M(n)$), $d(L_g)_{h_0}$ is the map $A \mapsto gA$ itself (the differential of a linear map is the linear map). Applied at $h_0 = I$ with input $A \in T_I \mathrm{GL}(n) = M(n)$: $d(L_g)_I(A) = gA$. So the left-invariant vector field has $A^L|_g = gA$, treating the tangent space at $g$ as $M(n)$.

**Step 2: The one-parameter subgroup $\gamma_A$ satisfies the ODE $g'(t) = g(t) A$, $g(0) = I$.**

The one-parameter subgroup $\gamma_A : \mathbb{R} \to \mathrm{GL}(n)$ is the integral curve of $A^L$ through $I$. By definition of integral curve, $\gamma_A'(t) = A^L|_{\gamma_A(t)} = \gamma_A(t) A$, with $\gamma_A(0) = I$. So $\gamma_A$ satisfies the matrix ODE

$$g'(t) = g(t) A, \qquad g(0) = I.$$

> [!note]- Derivation
> The defining equation of an integral curve of a vector field $V$ is $\gamma'(t) = V|_{\gamma(t)}$ with prescribed initial point $\gamma(0)$. For $V = A^L$ and $\gamma(0) = I$, substituting $A^L|_{\gamma(t)} = \gamma(t) A$ from Step 1: $\gamma'(t) = \gamma(t) A$, $\gamma(0) = I$. This is a linear matrix ODE.

**Step 3: $g(t) = e^{tA}$ solves the matrix ODE.**

Compute the derivative of $e^{tA} = \sum_{k=0}^\infty (tA)^k/k!$ term by term:

$$\frac{d}{dt} e^{tA} = \frac{d}{dt} \sum_{k=0}^\infty \frac{t^k A^k}{k!} = \sum_{k=1}^\infty \frac{k t^{k-1} A^k}{k!} = \sum_{k=1}^\infty \frac{t^{k-1} A^{k-1}}{(k-1)!} A = e^{tA} \cdot A.$$

And $e^{0 \cdot A} = I$. So $g(t) = e^{tA}$ satisfies $g'(t) = g(t) A$ and $g(0) = I$. By Picard–Lindelöf uniqueness of solutions to linear ODEs, $\gamma_A(t) = e^{tA}$.

> [!note]- Derivation
> Term-by-term differentiation of $e^{tA}$ is justified by uniform convergence on bounded sets (Weierstrass M-test against $\sum t^k \|A\|^k / k!$). Compute:
> $$\frac{d}{dt} e^{tA} = \frac{d}{dt} \left( I + tA + \frac{t^2 A^2}{2!} + \frac{t^3 A^3}{3!} + \cdots \right) = A + t A^2 + \frac{t^2 A^3}{2!} + \frac{t^3 A^4}{3!} + \cdots = e^{tA} \cdot A.$$
> Equivalently, this equals $A \cdot e^{tA}$ since $A$ commutes with all powers of itself. The initial value $e^{0 \cdot A} = e^0 = I$ holds by the $k = 0$ term of the series. So $g(t) = e^{tA}$ is the unique solution of $g'(t) = g(t) A$, $g(0) = I$, and hence equals $\gamma_A(t)$.

**Step 4: Conclude $\exp_{\mathrm{GL}}(A) = e^A$.**

By definition, $\exp_{\mathrm{GL}}(A) = \gamma_A(1)$. By Step 3, $\gamma_A(t) = e^{tA}$, so $\gamma_A(1) = e^A$. Hence

$$\exp_{\mathrm{GL}}(A) = e^A.$$

> [!note]- Complete formal solution
> Let $A \in \mathfrak{gl}(n, \mathbb{R}) = M(n, \mathbb{R})$. The left-invariant vector field $A^L$ has value $A^L|_g = gA$ at $g \in \mathrm{GL}(n, \mathbb{R})$, because left translation $L_g : M(n) \to M(n)$ is the linear map $h \mapsto gh$ with differential at any point $A \mapsto gA$. The one-parameter subgroup $\gamma_A$ is the integral curve of $A^L$ through $I$, satisfying $\gamma_A'(t) = \gamma_A(t) A$, $\gamma_A(0) = I$.
>
> The matrix exponential $e^{tA} = \sum_{k=0}^\infty (tA)^k/k!$ converges uniformly on bounded sets (Weierstrass M-test), and term-by-term differentiation gives $\frac{d}{dt} e^{tA} = A e^{tA} = e^{tA} A$. With $e^{0 \cdot A} = I$, this satisfies the same ODE. By uniqueness of ODE solutions, $\gamma_A(t) = e^{tA}$. Evaluating at $t = 1$:
> $$\exp_{\mathrm{GL}}(A) = \gamma_A(1) = e^A. \qquad\blacksquare$$

---

# Key Takeaways

**The exponential map of every matrix Lie group is the matrix exponential.**

By naturality of $\exp$ applied to the inclusion $G \hookrightarrow \mathrm{GL}(n)$ for any matrix Lie subgroup, the exponential of $G$ is the restriction of $\exp_{\mathrm{GL}}$ to $\mathfrak{g} \subseteq \mathfrak{gl}(n)$. Combined with this exercise, the exponential of any matrix Lie group is the matrix exponential applied to elements of the appropriate Lie subalgebra. So all $\exp$-computations on matrix Lie groups reduce to computing matrix exponentials — a concrete, classical problem solved by series expansion, diagonalization, or Jordan-form analysis.

**The integral-curve definition of $\exp$ generalizes the matrix exponential.**

The matrix exponential $e^A = \sum A^k/k!$ is defined only for matrices; the abstract Lie group exponential is defined for any Lie group via integral curves of left-invariant vector fields. This exercise shows the two agree on matrix Lie groups, and conceptually it explains *why* the matrix exponential is the right generalization of the scalar exponential $e^x$ to non-commutative settings — both are the unique solution of the ODE "derivative equals multiplication-by-self-times-$A$", with multiplication interpreted appropriately. The series expansion is one of many representations; the more intrinsic characterization is via the ODE.

**The matrix exponential is generally not a group homomorphism.**

The series identity $e^{A + B} = e^A e^B$ holds **only when $A$ and $B$ commute** ($[A, B] = 0$). For non-commuting $A, B$, the correct formula is the [[Thm - Naturality of the Exponential Map|Baker–Campbell–Hausdorff]]: $\log(e^A e^B) = A + B + \tfrac{1}{2}[A, B] + \cdots$. So the matrix exponential — like the abstract Lie group exponential — fails to be a group homomorphism on its domain, with the failure measured by the bracket. This is the operational form of the abstract fact that $\exp : \mathfrak{g} \to G$ is generally not a homomorphism unless $G$ is abelian.

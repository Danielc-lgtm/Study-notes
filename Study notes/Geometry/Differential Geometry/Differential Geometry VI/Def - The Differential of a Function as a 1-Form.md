---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Covector Field and Differential 1-Form"
  - "Def - The Tangent Space"
  - "Def - The Differential of a Smooth Map"
  - "Def - Smooth Function on a Manifold"
tags: [geometry, differential-geometry, differential, 1-form]
---

# Notation

$M$ is a smooth manifold, $f \in C^\infty(M)$ is a smooth function, and $df$ is the differential of $f$ as a 1-form, $df \in \Omega^1(M)$. At a point $p \in M$, $df_p$ is the covector at $p$, with $df_p(v) = v(f)$ for $v \in T_pM$. The notation $df$ overlaps with the differential of a smooth map $f : M \to \mathbb{R}$ in the sense of [[Def - The Differential of a Smooth Map]] — they are the same object, viewed two ways. In coordinates, $df = (\partial f / \partial x^i) \, dx^i$.

---

# Axiom Motivation

This page makes precise an old computation: in ordinary calculus, $df$ is a "small change" or "infinitesimal increment" of $f$. The pedagogical aim is to give $df$ a single, precise, manifold-native meaning that subsumes all the informal intuitions about differentials.

The clean operational definition is: $df_p$ is the linear functional on $T_pM$ that evaluates a tangent vector $v \in T_pM$ by letting $v$ derive $f$. That is, $df_p(v) := v(f)$. Recall (from [[Def - The Tangent Space]]) that a tangent vector at $p$ *is* a directional-derivative operator: $v : C^\infty(M) \to \mathbb{R}$ is a derivation at $p$, so $v(f) \in \mathbb{R}$. So $df_p$ is the **dual operation**: it eats vectors and produces numbers, exactly the operational signature of a covector. This single formula does three jobs at once.

First, it identifies $df_p$ as an element of $T_p^*M$. The linearity in $v$ — i.e., $df_p(v + w) = df_p(v) + df_p(w)$ and $df_p(cv) = c \, df_p(v)$ — follows directly from the fact that tangent vectors form a vector space, with $(v + w)(f) = v(f) + w(f)$ and $(cv)(f) = c v(f)$ by definition.

Second, it makes $df$ a smooth covector field. The smoothness of $df$ on $M$ follows from the smoothness of $f$: in coordinates, $df = (\partial f / \partial x^i) dx^i$, with each coefficient $\partial f / \partial x^i$ a smooth function (because $f$ is smooth). So $df$ is a smooth section of $T^*M$, that is, an element of $\Omega^1(M)$.

Third, it recovers the classical formula. The pairing of $df$ with a tangent vector $v = v^i \partial/\partial x^i$ at $p$ is
$$df_p(v) = v(f) = v^i \frac{\partial f}{\partial x^i}(p) = \text{the directional derivative of } f \text{ at } p \text{ along } v.$$
This recovers the classical interpretation of $df$ as "the small change in $f$ when you move in direction $v$ by an infinitesimal step" — but now without any infinitesimals, only ordinary linear algebra.

What is forced by demanding $df_p$ be **linear** in $v$? Linearity follows automatically from the vector-space structure of $T_pM$ and the definition $df_p(v) = v(f)$. We are not choosing to impose linearity; it is forced.

What is forced by demanding $df$ be **smooth** in $p$? Smoothness is the content of "differential of a smooth function is a smooth 1-form". It follows from the smoothness of $f$ via the coordinate formula. If $f$ were only $C^1$, then $df$ would be a continuous but not smooth 1-form; if $f$ were merely continuous, $df$ would be a distribution (a $1$-current), not a 1-form. The smoothness hypothesis on $f$ is what makes $df$ a smooth 1-form.

What is forced by the **Leibniz rule** $d(fg) = f \, dg + g \, df$? This is a consequence of the Leibniz rule for tangent vectors: $v(fg) = v(f) g(p) + f(p) v(g)$ for any derivation $v$ at $p$. Pairing both sides with $v$, the identity for $d(fg)$ follows. So Leibniz on 1-forms is the dual of Leibniz on tangent vectors.

What is forced by demanding the operator $d : C^\infty(M) \to \Omega^1(M)$ be **$\mathbb{R}$-linear**? It is: $d(f + g) = df + dg$ and $d(cf) = c \, df$ for $c \in \mathbb{R}$. The verification is from the corresponding linearity of the directional-derivative operation $v \mapsto v(f)$.

What is forced by demanding $df$ identify with the **differential of a smooth map** in the sense of [[Def - The Differential of a Smooth Map]]? For $f : M \to \mathbb{R}$, the bundle differential $df : TM \to T\mathbb{R} = \mathbb{R} \times \mathbb{R}$ is a bundle homomorphism over $f$. Restricting to a fibre $T_pM$, $df_p : T_pM \to T_{f(p)}\mathbb{R}$, and identifying $T_{f(p)}\mathbb{R} \cong \mathbb{R}$ (since $\mathbb{R}$ has a canonical basis $\partial/\partial t$), $df_p$ becomes a linear map $T_pM \to \mathbb{R}$ — an element of $T_p^*M$. This identification is the bridge between the bundle-homomorphism perspective on $df$ and the covector-field perspective.

What if we **strengthened** by demanding $df$ also be exact in the sense of $df =$ differential of another function? It already is — $f$ itself is that function. The point of the definition is that $df$ produces *the* canonical exact 1-form associated with $f$.

What if we **weakened** by allowing $df$ to be only continuous? Then we would need $f$ to be only $C^1$, losing the smooth-bundle apparatus.

---

# The Definition

Let $M$ be a smooth manifold and $f \in C^\infty(M)$ a smooth real-valued function. The **differential** of $f$ is the 1-form $df \in \Omega^1(M)$ defined pointwise by
$$df_p(v) := v(f) \qquad \text{for every } p \in M \text{ and every } v \in T_pM,$$
where $v(f) \in \mathbb{R}$ is the directional derivative of $f$ at $p$ along $v$ (recalling that tangent vectors are derivations on $C^\infty(M)$ at $p$).

**Equivalence with the bundle differential.** Viewing $f$ as a smooth map $f : M \to \mathbb{R}$, the bundle differential $df : TM \to T\mathbb{R}$ is a bundle homomorphism over $f$ ([[Def - The Differential of a Smooth Map]]). Identifying the fibre $T_{f(p)}\mathbb{R}$ with $\mathbb{R}$ via the canonical basis $\partial/\partial t|_{f(p)} \mapsto 1$, the fibre map $df_p : T_pM \to \mathbb{R}$ is exactly the covector $df_p$ defined above. So "the differential of $f$ as a 1-form" and "the differential of $f$ as a bundle homomorphism" are the same object.

**Coordinate expression.** In a chart $(U, \varphi)$ with coordinate functions $x^1, \dots, x^n$, the differential is
$$df|_U = \sum_{i=1}^{n} \frac{\partial f}{\partial x^i} \, dx^i \quad (\text{Einstein summation: } df = \tfrac{\partial f}{\partial x^i} dx^i).$$
The coefficients $\partial f / \partial x^i$ are the partial derivatives of $f$ with respect to the coordinates (smooth functions on $U$, since $f$ is smooth); the $dx^i$ are the coordinate covector fields (the dual coordinate frame to $\partial/\partial x^i$). The formula is verified by pairing both sides with a coordinate tangent vector: $df(\partial/\partial x^j) = \partial f/\partial x^j$ (by definition $df(v) = v(f)$) and $(\sum_i (\partial f/\partial x^i) dx^i)(\partial/\partial x^j) = \sum_i (\partial f/\partial x^i) \delta^i_j = \partial f/\partial x^j$ (by linearity and dual-basis biorthogonality). See [[Thm - Coordinate Expression for df]].

**Properties of the operator $d : C^\infty(M) \to \Omega^1(M)$.**

- **$\mathbb{R}$-linearity:** $d(f + g) = df + dg$ and $d(cf) = c \, df$ for $c \in \mathbb{R}$.
- **Leibniz rule:** $d(fg) = f \, dg + g \, df$ — the product rule for differentials.
- **Constants vanish:** $d c = 0$ for any constant function $c$.
- **Naturality:** for smooth $F : M \to N$ and $g \in C^\infty(N)$, $F^*(dg) = d(g \circ F) = d(F^*g)$. See [[Thm - Pullback Commutes with d for 1-Forms]].

A 1-form $\omega$ that equals $df$ for some smooth function $f$ is called **exact**. Not every 1-form is exact; the obstruction is the first de Rham cohomology $H^1_{dR}(M)$.

---

# Relate to Other Fields / Compression

The differential of a function is the **manifold version of the gradient**, with one crucial structural difference: it does not require an inner product. The gradient $\nabla f$ on Euclidean space (see [[Def - Directional Derivative and the Gradient]]) is a *vector field*, while $df$ is a 1-form. To convert between them, one needs an identification $TM \cong T^*M$, which is exactly an inner product or Riemannian metric. The 1-form $df$ is metric-independent; the gradient is metric-dependent. This is the formal reason the 1-form notation is preferred in modern differential geometry: it makes the metric structure visible when present and absent when not.

The differential is also a **special case of the exterior derivative**. The full exterior derivative $d : \Omega^k(M) \to \Omega^{k+1}(M)$ is defined on $k$-forms for all $k \geq 0$, with $d : \Omega^0(M) = C^\infty(M) \to \Omega^1(M)$ the differential of this page as the $k = 0$ case. The higher-$k$ exterior derivatives satisfy the same naturality and Leibniz-type rules, generalized appropriately for higher forms. The differential is the first instance of the full machinery of differential forms.

**True name:** the true name of $df$ is "**the 1-form that pairs with any tangent vector $v$ at $p$ to give the directional derivative $v(f)$**". The formula $df_p(v) = v(f)$ is the operational definition; the coordinate formula $df = (\partial f/\partial x^i) dx^i$ is the computational tool; the bundle-homomorphism perspective is the categorical content. All three are the same object, viewed from different angles.

A useful slogan: **the differential of a function is the cotangent-bundle gradient, and it lives one step below the exterior derivative in the de Rham complex**. The de Rham complex starts $0 \to C^\infty(M) \xrightarrow{d} \Omega^1(M) \xrightarrow{d} \Omega^2(M) \xrightarrow{d} \cdots$, and the first map is exactly the differential.

In **classical mechanics**, the "Hamiltonian 1-form" $dH$ on phase space $T^*Q$ is the differential of the Hamiltonian function $H : T^*Q \to \mathbb{R}$, and Hamilton's equations $\iota_{X_H}\omega = dH$ involve $dH$ as the right-hand side. So $dH$ is what determines the dynamics: solve for the unique vector field $X_H$ contracting with $\omega$ to give $dH$, and the integral curves are the trajectories.

In **physics**, the **first law of thermodynamics** can be written as $dU = T \, dS - p \, dV$, an equation among 1-forms on the manifold of thermodynamic states. The differentials encode all the thermodynamic relations including Maxwell's relations (which are essentially $d^2 = 0$ applied to thermodynamic potentials).

---

# Examples / Corollaries

**Is an instance — $df$ for $f(x, y) = x^2 + y^2$ on $\mathbb{R}^2$.** $df = 2x \, dx + 2y \, dy$. Pairing with $v = (a, b) \in T_pM = \mathbb{R}^2$ at the point $p = (x_0, y_0)$: $df_p(v) = 2x_0 a + 2y_0 b$, the classical directional derivative.

**Is an instance — $df$ for $f(\theta) = \theta$ on $\mathbb{R}$.** $df = d\theta$. The "angular coordinate" 1-form on $\mathbb{R}$ is just the differential of the identity function.

**Is an instance — the angle 1-form on $S^1$.** On $S^1$, the angle $\theta$ is only locally well-defined as a function (since $\theta$ and $\theta + 2\pi$ are the same point), but $d\theta$ is globally well-defined as a 1-form — the local expressions $d\theta$ in different charts agree on overlaps (since the chart transition is $\theta \mapsto \theta + 2\pi$, with differential $d\theta$). So $d\theta \in \Omega^1(S^1)$ is a globally smooth 1-form, but it is *not* of the form $df$ for any globally defined smooth function on $S^1$ — it is **closed but not exact**.

**Is an instance — $d(x^i)$ in a coordinate chart.** The coordinate functions $x^i : U \to \mathbb{R}$ are smooth, and their differentials $d(x^i) = dx^i$ are exactly the coordinate covector fields — this is consistent because $dx^i(\partial/\partial x^j) = \delta^i_j$ matches the dual-basis defining condition.

**Is an instance — the energy 1-form in mechanics.** For the Hamiltonian $H = p^2/(2m) + V(q)$ on $T^*\mathbb{R}$, $dH = (p/m) dp + V'(q) dq$. Hamilton's equations come from $\iota_{X_H}(dp \wedge dq) = dH$.

**Is NOT an instance — a 1-form $\omega$ that does not equal $df$ for any $f$.** The form $\omega = y \, dx$ on $\mathbb{R}^2$: if $\omega = df$ for some smooth $f$, then $\partial f/\partial x = y$ and $\partial f/\partial y = 0$. From the second, $f$ depends only on $x$; but then $\partial f/\partial x$ depends only on $x$, contradicting $\partial f/\partial x = y$ which depends on $y$. So $\omega$ is not exact. Note: $d\omega = dy \wedge dx = - dx \wedge dy \neq 0$, so $\omega$ is also not closed.

**Is NOT an instance — a 1-form $\omega$ that is closed but not exact.** The form $\omega = (x \, dy - y \, dx)/(x^2 + y^2)$ on $\mathbb{R}^2 \setminus \{0\}$ is closed ($d\omega = 0$, by direct computation) but not exact — see [[Ex - A Conservative 1-Form on R² Minus Origin]]. The obstruction is topological: $\mathbb{R}^2 \setminus \{0\}$ is not simply connected.

**Corollary — $d$ is $\mathbb{R}$-linear but not $C^\infty(M)$-linear.** From the Leibniz rule, $d(fg) = f \, dg + g \, df \neq f \, dg$ unless $g$ is constant. So $d$ is not a bundle homomorphism — it is a differential operator. This is the tensoriality criterion in action.

**Corollary — $df = 0$ if and only if $f$ is locally constant.** $df_p = 0$ means $v(f) = 0$ for all $v \in T_pM$, which means $\partial f / \partial x^i (p) = 0$ for all $i$ in any chart. This vanishing at every $p$ forces $f$ to be locally constant. On a connected $M$, locally constant means constant.

**Corollary — coordinate expression in terms of local frames.** Any smooth 1-form $\omega$ on $U$ has $\omega = \omega_i \, dx^i$ with $\omega_i$ smooth functions, and the special case $\omega = df$ has $\omega_i = \partial f / \partial x^i$. So the differential of $f$ has components equal to the partial derivatives of $f$ in any coordinate chart.

**Corollary — Leibniz rule.** $d(fg) = f \, dg + g \, df$ follows from the Leibniz rule for tangent vectors: $v(fg) = v(f) g(p) + f(p) v(g)$, so $d(fg)_p(v) = v(fg) = v(f) g(p) + f(p) v(g) = g(p) df_p(v) + f(p) dg_p(v) = (g \, df + f \, dg)_p(v)$.

**Calibration check.** Compute $d(x^2 + y^2)$ in $\mathbb{R}^2$ and confirm it gives $2x \, dx + 2y \, dy$. Pair $df_p$ with a tangent vector at a specific point and confirm the result equals the directional derivative. Verify that $d(fg) = f \, dg + g \, df$ for two specific smooth functions on $\mathbb{R}^n$.

---

# Unlocked by This

> [!tip] The de Rham Complex *(from this topic and Differential Geometry X)*
> Once the differential is in hand, the **de Rham complex** begins: $0 \to \Omega^0(M) \xrightarrow{d} \Omega^1(M) \xrightarrow{d} \Omega^2(M) \to \cdots$, with $d^2 = 0$. Cohomology of this complex is **de Rham cohomology** $H^k_{dR}(M)$, a topological invariant of $M$ (de Rham theorem identifies it with singular cohomology). The differential of a function is the first non-trivial map in this complex, and the closed-not-exact obstruction at degree $1$ is $H^1_{dR}(M)$ — see [[Thm - A Closed 1-Form on a Simply Connected Manifold is Exact]].

> [!tip] Conservative Force Fields *(from Classical Mechanics)*
> A force field $\mathbf{F}$ on Euclidean space is **conservative** if $\mathbf{F} = -\nabla U$ for some scalar potential $U$. In 1-form language, the work 1-form $\omega = \mathbf{F} \cdot d\mathbf{r}$ is exact: $\omega = -dU$. Conservation of energy follows automatically from $dU$ being exact: $\int_\gamma \omega = U(\gamma(a)) - U(\gamma(b))$ depends only on endpoints. The differential-of-a-function structure of conservative forces is the natural language for energy conservation.

> [!tip] Lagrangian Mechanics and the Calculus of Variations *(from Geometric Mechanics)*
> The variational principle $\delta S = 0$, where $S = \int L \, dt$ is the action of a Lagrangian $L : TQ \to \mathbb{R}$, becomes a statement about differentials of functions on path space. The Euler–Lagrange equations $d(\partial L / \partial \dot q) - \partial L / \partial q = 0$ involve differentials in the classical sense; in geometric mechanics, they translate to a statement about a specific 1-form on the tangent bundle vanishing on the critical paths.

> [!tip] Differential of Function in Algebraic Geometry *(from Algebraic Geometry)*
> The algebraic analogue of $df$ is the **Kähler differential** $df \in \Omega^1_{X/k}$, defined on schemes via the universal property of the module of relative differentials. For affine $X = \mathrm{Spec}(A)$, $\Omega^1_{A/k}$ is the $A$-module generated by symbols $da$ for $a \in A$ modulo the Leibniz rule and $k$-linearity. This algebraic definition recovers the smooth $df$ when $A = C^\infty(M)$, but extends to far more general settings, including singular varieties and arithmetic schemes. The category of Kähler differentials is the algebraic geometer's home for the differential of a function.

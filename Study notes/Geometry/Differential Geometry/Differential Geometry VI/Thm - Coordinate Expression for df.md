---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - The Differential of a Function as a 1-Form"
  - "Def - Covector Field and Differential 1-Form"
  - "Def - The Tangent Space"
  - "Def - Coordinate Tangent Vectors"
tags: [geometry, differential-geometry, differential, coordinates]
---

# Notation

$M$ is a smooth manifold, $f \in C^\infty(M)$. $(U, \varphi)$ is a smooth chart with coordinate functions $x^1, \dots, x^n$. The coordinate vector fields are $\partial/\partial x^i \in \mathfrak{X}(U)$ and the coordinate covector fields are $dx^i \in \Omega^1(U)$. The differential of $f$ as a 1-form is $df \in \Omega^1(M)$ ([[Def - The Differential of a Function as a 1-Form]]).

---

# Statement

> **Theorem (Coordinate Expression for $df$).** Let $M$ be a smooth manifold, $f \in C^\infty(M)$, and $(U, \varphi)$ a smooth chart on $M$ with coordinate functions $x^1, \dots, x^n$. Then on $U$,
> $$df = \sum_{i=1}^{n} \frac{\partial f}{\partial x^i} \, dx^i,$$
> where $\partial f / \partial x^i \in C^\infty(U)$ is the partial derivative of $f$ with respect to the $i$-th coordinate and $dx^i$ is the $i$-th coordinate 1-form. In Einstein summation, $df = (\partial f/\partial x^i) dx^i$.

---

# Motivation

This theorem is the **bridge between abstract differential geometry and the classical multivariable calculus formula for the differential**. In classical calculus, the "differential" $df = (\partial f/\partial x) dx + (\partial f/\partial y) dy + \dots$ is taught as a formal symbol or as an "infinitesimal increment". On a manifold, $df$ has a precise meaning as a 1-form ([[Def - The Differential of a Function as a 1-Form]]), and the theorem says that in any coordinate chart, the abstract object equals the classical formula. The classical formula is recovered as a special case of the manifold-native definition.

The theorem matters because it makes **calculations possible**. The abstract definition $df_p(v) = v(f)$ is conceptually clean but computationally indirect. The coordinate formula $df = (\partial f/\partial x^i) dx^i$ is what you actually use to compute a specific differential. Together with the chain rule and the linearity of $d$, the formula handles every computation involving differentials in a chart.

A second reason the theorem matters is that it provides the **link between the two faces of the cotangent space**: the abstract face (linear functionals on $T_pM$) and the concrete face (vectors of partial derivatives). The dual coordinate coframe $dx^i$ at a point realises this link explicitly — each $dx^i|_p$ is the linear functional "extract the $i$-th coordinate of a tangent vector" — and the differential of $f$ assembled in this coframe has components equal to the partial derivatives of $f$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a smooth function $f$ and a coordinate chart $(U, x^i)$". This setup arises whenever any concrete differential is computed in a chart.

The most common source is **a smooth function defined by an explicit formula in coordinates**. If $f(x, y) = x^2 + y^2$ on $\mathbb{R}^2$, the partial derivatives are $\partial f/\partial x = 2x$ and $\partial f/\partial y = 2y$, and the theorem gives $df = 2x \, dx + 2y \, dy$ directly. Every textbook calculation of a differential is an application of this source.

A second source is **the coordinate functions themselves**. Applying the theorem to $f = x^j$ (the $j$-th coordinate function) gives $d(x^j) = (\partial x^j/\partial x^i) dx^i = \delta^j_i dx^i = dx^j$. So the theorem is self-consistent: the differential of the coordinate function $x^j$ is the coordinate 1-form $dx^j$, recovering the definition.

A third source is **a smooth function $f$ on a manifold given by an abstract construction** (a quotient, a limit, an integral). To compute $df$ in a specific chart, pull back $f$ to the chart's coordinate representation $f \circ \varphi^{-1}$ on $\varphi(U) \subseteq \mathbb{R}^n$, compute partial derivatives, and apply the formula. The theorem provides the bridge from the abstract construction to a concrete expression in the chart.

**Targets (Output Amplification)**

The conclusion is "$df = (\partial f/\partial x^i) dx^i$ in any chart". Combined with one further fact, this gives a wide range of structural and computational results.

The first combination is **theorem plus the chain rule gives transformation of $df$ under coordinate changes**. If $(\tilde U, \tilde x^j)$ is another chart on the overlap with $(U, x^i)$, then $df = (\partial f/\partial x^i) dx^i$ in the first chart and $df = (\partial f/\partial \tilde x^j) d\tilde x^j$ in the second. The relation between $(\partial f/\partial x^i)$ and $(\partial f/\partial \tilde x^j)$ is given by the chain rule: $\partial f/\partial \tilde x^j = (\partial f/\partial x^i)(\partial x^i / \partial \tilde x^j)$. The 1-forms transform contravariantly: $dx^i = (\partial x^i/\partial \tilde x^j) d\tilde x^j$. So $df$ is invariant under coordinate change, as it must be (it is a well-defined 1-form).

A second combination is **theorem plus pairing with a tangent vector gives the directional derivative formula**. For $v = v^i \partial/\partial x^i$ at $p$, $df_p(v) = v^i (\partial f/\partial x^i)(p) = v(f)$. This recovers the definition $df_p(v) = v(f)$ in coordinates and ties the abstract and concrete formulations together.

A third combination is **theorem plus the Leibniz rule gives the product rule for differentials**. For $f, g \in C^\infty(M)$, $d(fg) = ((\partial(fg)/\partial x^i)) dx^i = (g \partial f/\partial x^i + f \partial g/\partial x^i) dx^i = g \, df + f \, dg$. So the abstract Leibniz rule $d(fg) = f \, dg + g \, df$ is verified by the coordinate formula.

A fourth combination is **theorem plus pullback gives the change-of-variables formula**. For a smooth $F : M \to N$ and $g \in C^\infty(N)$, the pullback formula gives $F^*(dg) = d(g \circ F) = (\partial(g \circ F)/\partial x^i) dx^i$, which by the chain rule equals $(\partial g/\partial y^j)(F(x)) (\partial F^j/\partial x^i) dx^i$. This recovers the change-of-variables for 1-forms.

---

# Why Is It True

The intuition is direct: both sides are 1-forms on $U$, and they agree on a frame, so they are equal.

**The one-line mechanism summary: both $df$ and $(\partial f/\partial x^i) dx^i$ pair with the coordinate tangent vector $\partial/\partial x^j$ to give the partial derivative $\partial f/\partial x^j$, so they are equal as 1-forms.**

The check that they agree on a frame:

For the abstract differential, $df_p(\partial/\partial x^j|_p) = (\partial/\partial x^j|_p)(f) = \partial f/\partial x^j(p)$, using the definition that $\partial/\partial x^j|_p$ is the derivation that takes the $j$-th partial derivative.

For the coordinate formula, $((\partial f/\partial x^i) dx^i)_p (\partial/\partial x^j|_p) = (\partial f/\partial x^i)(p) \cdot dx^i_p(\partial/\partial x^j|_p) = (\partial f/\partial x^i)(p) \cdot \delta^i_j = \partial f/\partial x^j(p)$, using the dual-basis property $dx^i(\partial/\partial x^j) = \delta^i_j$ and the linearity of the pairing.

The two pairings agree on every $\partial/\partial x^j$, and since the $\partial/\partial x^j$ form a basis of each $T_pU$, the two 1-forms agree at every point. Both are smooth, so they agree as smooth 1-forms.

This proof has the same shape as proving two linear maps are equal by showing they agree on a basis. The bundle structure of $T^*U$ and the locality of 1-forms (they are determined pointwise) make this argument complete.

---

# What Makes This Hard

The substantive step is the *check on the basis*, which requires both the definition of $\partial/\partial x^j$ as a derivation and the definition of $dx^i$ as the dual coordinate covector. Beginners sometimes attempt to "verify" the theorem by expanding both sides in different coordinates and matching, which gets tangled in chain-rule bookkeeping; the basis-pairing argument is shorter and structurally cleaner.

A common error is to **confuse the partial derivative as a real number vs as a smooth function**: $\partial f/\partial x^i$ is a smooth function on $U$ (the value at each point), and its appearance as the coefficient of $dx^i$ in the formula requires this function-valued interpretation. Treating it as a single number leads to dimensional confusion.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Two 1-forms on $U$ are equal if and only if they agree pointwise. Two covectors at $p$ are equal if and only if they agree on a basis of $T_pU$. Pair both sides of the identity with the coordinate basis $\partial/\partial x^j$ and check the values agree using the dual-basis biorthogonality $dx^i(\partial/\partial x^j) = \delta^i_j$ and the derivative definition $\partial/\partial x^j(f) = \partial f/\partial x^j$.

**Subgoal decomposition:**

1. **Identify both sides as 1-forms on $U$.** $df$ is a 1-form on $M$ by definition, restricted to $U$. The right-hand side $(\partial f/\partial x^i) dx^i$ is a $C^\infty(U)$-linear combination of the coordinate 1-forms $dx^i$, hence a 1-form on $U$.
   - *Hint:* Both sides live in $\Omega^1(U)$.
   - *Why needed:* The comparison happens in $\Omega^1(U)$.

2. **Pair the left-hand side with $\partial/\partial x^j$.** By the definition of $df$, $df(\partial/\partial x^j) = \partial/\partial x^j(f) = \partial f/\partial x^j$.
   - *Hint:* This uses the derivation definition of tangent vectors.
   - *Why needed:* Determines the value of $df$ on the coordinate basis.

3. **Pair the right-hand side with $\partial/\partial x^j$.** By linearity and $dx^i(\partial/\partial x^j) = \delta^i_j$, $((\partial f/\partial x^i) dx^i)(\partial/\partial x^j) = (\partial f/\partial x^i) \delta^i_j = \partial f/\partial x^j$.
   - *Hint:* This uses the dual-basis biorthogonality.
   - *Why needed:* Determines the value of the right-hand side on the coordinate basis.

4. **Agree on a basis $\implies$ agree as covectors.** Two covectors at $p$ that agree on a basis of $T_pU$ are equal as elements of $T_p^*U$.
   - *Hint:* Standard linear algebra.
   - *Why needed:* Equates the two 1-forms pointwise.

5. **Agree pointwise $\implies$ agree as 1-forms.** Two 1-forms that agree at every point are equal as 1-forms.
   - *Hint:* This is the definition of equality of 1-forms.
   - *Why needed:* Final identification.

---

# Lemma Decomposition

> [!note]- Lemma 1: Pairing $df$ with the coordinate basis gives partial derivatives
> **Statement:** $df_p(\partial/\partial x^j|_p) = \partial f / \partial x^j(p)$ at every $p \in U$.
>
> **Hint:** Use the definition $df_p(v) = v(f)$ and the derivation definition of $\partial/\partial x^j|_p$.
>
> **Why needed:** Computes the values of $df$ on the coordinate basis.
>
> > [!note]- Full proof
> > By [[Def - The Differential of a Function as a 1-Form]], $df_p(v) = v(f)$ for $v \in T_pU$. The coordinate tangent vector $\partial/\partial x^j|_p$ is the derivation at $p$ that takes the $j$-th partial derivative of $f$ in the chart $(U, \varphi)$. Explicitly, $(\partial/\partial x^j|_p)(f) := (\partial (f \circ \varphi^{-1})/\partial r^j)(\varphi(p))$, the standard partial derivative of the coordinate representation of $f$ at the image point $\varphi(p) \in \mathbb{R}^n$. This is exactly the partial derivative $\partial f/\partial x^j$ evaluated at $p$. So $df_p(\partial/\partial x^j|_p) = \partial f/\partial x^j(p)$.

> [!note]- Lemma 2: Pairing the right-hand side with the coordinate basis
> **Statement:** $((\partial f/\partial x^i) dx^i)_p(\partial/\partial x^j|_p) = \partial f / \partial x^j(p)$ at every $p \in U$.
>
> **Hint:** Use linearity of the pairing and $dx^i_p(\partial/\partial x^j|_p) = \delta^i_j$.
>
> **Why needed:** Computes the values of the right-hand side on the coordinate basis.
>
> > [!note]- Full proof
> > By linearity of the pairing in the covector slot,
> > $$\left( (\partial f/\partial x^i) dx^i \right)_p \left( \partial/\partial x^j|_p \right) = \sum_i (\partial f/\partial x^i)(p) \cdot dx^i_p(\partial/\partial x^j|_p).$$
> > By the dual-basis biorthogonality of the coordinate coframe, $dx^i_p(\partial/\partial x^j|_p) = \delta^i_j$. So the sum collapses to the $i = j$ term: $(\partial f/\partial x^j)(p)$.

> [!note]- Lemma 3: Agree on a basis implies equal as covectors
> **Statement:** If $\omega, \eta \in T_p^*U$ satisfy $\omega(\partial/\partial x^j|_p) = \eta(\partial/\partial x^j|_p)$ for all $j = 1, \dots, n$, then $\omega = \eta$ in $T_p^*U$.
>
> **Hint:** Both $\omega$ and $\eta$ are linear functionals on $T_pU$, which has basis $\partial/\partial x^1|_p, \dots, \partial/\partial x^n|_p$.
>
> **Why needed:** Equates the two 1-forms pointwise.
>
> > [!note]- Full proof
> > A linear functional on a finite-dimensional vector space is determined by its values on a basis. The coordinate tangent vectors form a basis of $T_pU$. So $\omega - \eta$ vanishes on every basis vector, hence on every linear combination — i.e., on all of $T_pU$. So $\omega - \eta = 0$ in $T_p^*U$, that is, $\omega = \eta$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Setup.** Both sides of $df = (\partial f/\partial x^i) dx^i$ are 1-forms on $U$: the left by [[Def - The Differential of a Function as a 1-Form]], the right as a $C^\infty(U)$-linear combination of the coordinate coframe $(dx^i)$.
>
> **Step 1 — Pair with the coordinate frame at each $p \in U$.** Compute $\mathrm{LHS}_p(\partial/\partial x^j|_p)$:
> $$\mathrm{LHS}_p(\partial/\partial x^j|_p) = df_p(\partial/\partial x^j|_p) = (\partial/\partial x^j|_p)(f) = \partial f / \partial x^j(p),$$
> using the definition $df(v) = v(f)$ and the definition of $\partial/\partial x^j$ as a derivation.
>
> **Step 2 — Pair the right-hand side with the coordinate frame at each $p \in U$.**
> $$\mathrm{RHS}_p(\partial/\partial x^j|_p) = \sum_i (\partial f/\partial x^i)(p) \cdot dx^i_p(\partial/\partial x^j|_p) = \sum_i (\partial f/\partial x^i)(p) \cdot \delta^i_j = \partial f / \partial x^j(p),$$
> using the dual-basis property $dx^i(\partial/\partial x^j) = \delta^i_j$ and the linearity of the pairing.
>
> **Step 3 — Equate covectors.** $\mathrm{LHS}_p$ and $\mathrm{RHS}_p$ agree on every coordinate basis vector $\partial/\partial x^j|_p$, hence agree as elements of $T_p^*U$ (a linear functional on $T_pU$ is determined by its values on a basis).
>
> **Step 4 — Equate 1-forms.** Since $\mathrm{LHS}_p = \mathrm{RHS}_p$ in $T_p^*U$ for every $p \in U$, the two 1-forms agree pointwise; hence they are equal as elements of $\Omega^1(U)$.
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Multivariable analysis: gradient as the differential.** Apply the theorem to $\mathbb{R}^n$ with standard coordinates: $df = (\partial f/\partial x^1) dx^1 + \dots + (\partial f/\partial x^n) dx^n$ is the classical "total differential" of $f$. The gradient $\nabla f$ is the same data viewed as a vector (via the standard inner product on $\mathbb{R}^n$); $df$ is the same data viewed as a 1-form. The theorem makes precise the identification.

**Classical thermodynamics: differential of state functions.** For thermodynamic potentials like enthalpy $H(S, p)$, the theorem gives $dH = (\partial H/\partial S) dS + (\partial H/\partial p) dp$. Identifying the partial derivatives with thermodynamic variables ($\partial H/\partial S = T$, $\partial H/\partial p = V$) recovers $dH = T \, dS + V \, dp$. Maxwell's relations arise from $d^2H = 0$ applied to the formula.

**Physics: Hamilton's equations from $dH$.** For a Hamiltonian $H(q, p)$ on phase space $T^*Q$, the theorem gives $dH = (\partial H/\partial q^i) dq^i + (\partial H/\partial p_i) dp_i$. Hamilton's equations $\dot q^i = \partial H/\partial p_i$ and $\dot p_i = -\partial H/\partial q^i$ then read off from the symplectic-form equation $\iota_{X_H}\omega = dH$ once the components of $X_H$ in $\partial/\partial q^i, \partial/\partial p_i$ are extracted.

**Algebraic geometry: Kähler differentials in local coordinates.** On an affine variety $\mathrm{Spec}(A)$ with coordinate [[Def - Ring|ring]] $A$, the [[Def - Module|module]] of Kähler differentials $\Omega^1_{A/k}$ contains the symbols $df$ for $f \in A$, and these satisfy the Leibniz rule. For $A = k[x_1, \dots, x_n]$, $\Omega^1_{A/k}$ is a free $A$-module with basis $dx_1, \dots, dx_n$, and $df = \sum_i (\partial f/\partial x_i) dx_i$ algebraically — the algebraic counterpart of this theorem.

---

# Bridges

- **[[Def - Dual Basis]]** — The theorem's correctness rests on the dual-basis property $dx^i(\partial/\partial x^j) = \delta^i_j$. In linear algebra, every basis has a unique dual basis with this property; in differential geometry, the dual basis at each point varies smoothly with $p$ to form the dual coordinate coframe.

- **[[Thm - Local Frames Span Sections]]** — The theorem is a specific instance of the local-frame expansion: every 1-form has a unique expression in any local frame, with smooth components. For the differential of a function in the coordinate coframe, the components happen to be the partial derivatives.

- **Chain rule under coordinate change** — Under a chart transition $\tilde x^j = \tilde x^j(x^1, \dots, x^n)$, the partial derivatives of $f$ transform as $\partial f/\partial \tilde x^j = (\partial x^i/\partial \tilde x^j)(\partial f/\partial x^i)$, and the coordinate 1-forms transform contravariantly as $d\tilde x^j = (\partial \tilde x^j/\partial x^i) dx^i$. The combination $df = (\partial f/\partial x^i) dx^i = (\partial f/\partial \tilde x^j) d\tilde x^j$ is invariant — as it must be — and the chain rule is what makes both transformations consistent.

- **[[Def - Partial Derivatives and the Jacobian Matrix]]** — The partial derivatives of $f$ in a chart are the components of the Jacobian matrix of $f : \varphi(U) \subseteq \mathbb{R}^n \to \mathbb{R}$ (a $1 \times n$ matrix, i.e., a row vector). The theorem says $df$ realises this row vector in the dual coordinate basis $(dx^i)$, recovering the classical view of the differential as the Jacobian.

---

# Unlocked by This

> [!tip] Gradient on Riemannian Manifolds *(from Riemannian Geometry)*
> The differential $df$ is a 1-form, but the **gradient** $\nabla f$ on a Riemannian manifold is the vector field obtained from $df$ via the musical isomorphism $\sharp : T^*M \to TM$ induced by the Riemannian metric: $\nabla f := (df)^\sharp$. In a coordinate frame, $\nabla f = g^{ij} (\partial f/\partial x^i) \partial/\partial x^j$, where $g^{ij}$ are the components of the inverse metric. The theorem combined with the musical isomorphism gives the coordinate expression for the gradient.

> [!tip] Hamilton's Equations from the Coordinate Differential *(from Symplectic Geometry)*
> On phase space $T^*Q$ with coordinates $(q^i, p_i)$ and canonical symplectic form $\omega = dp_i \wedge dq^i$, the Hamiltonian vector field $X_H$ of a Hamiltonian $H : T^*Q \to \mathbb{R}$ is the unique vector field with $\iota_{X_H}\omega = dH$. Using the theorem, $dH = (\partial H/\partial q^i) dq^i + (\partial H/\partial p_i) dp_i$, and the equation $\iota_{X_H}\omega = dH$ becomes the system $\dot q^i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q^i$ — Hamilton's canonical equations.

> [!tip] Lagrangian Mechanics *(from Geometric Mechanics)*
> The Euler–Lagrange equations $d/dt(\partial L/\partial \dot q^i) - \partial L/\partial q^i = 0$ are the coordinate expression of the variational principle $\delta S = 0$ for the action $S = \int L \, dt$. The theorem's role: the differentials of $L : TQ \to \mathbb{R}$ at each point have coordinate expressions in terms of partial derivatives, and the calculus of variations is built on integrating these differentials along paths.

> [!tip] Stokes's Theorem in Coordinates *(from Differential Geometry IX)*
> For a 1-form $\omega = \omega_i \, dx^i$ in a chart and a surface $S$ with boundary, Stokes's theorem $\int_{\partial S} \omega = \int_S d\omega$ in coordinates expresses both integrals as Riemann integrals of partial-derivative expressions. The theorem is the building block of this coordinate computation: $d\omega = (\partial \omega_j/\partial x^i) dx^i \wedge dx^j$, and the integration is then standard multivariable calculus.

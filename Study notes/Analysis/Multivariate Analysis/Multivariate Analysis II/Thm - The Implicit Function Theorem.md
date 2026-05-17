---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - The Chain Rule"
  - "Thm - The Inverse Function Theorem"
  - "Def - Higher-Order Derivatives and Ck Maps"
tags: [analysis, multivariate-analysis]
---

# Notation

A point of $\mathbb{R}^n = \mathbb{R}^d \times \mathbb{R}^{n-d}$ is written $(x, y)$ with $x \in \mathbb{R}^d$ the "free" variables and $y \in \mathbb{R}^{n-d}$ the "dependent" variables. For a map $f : U \to \mathbb{R}^{n-d}$, the **partial Jacobian** $D_x f$ is the $(n-d)\times d$ matrix of derivatives in the $x$-variables, and $D_y f$ the $(n-d)\times(n-d)$ matrix of derivatives in the $y$-variables; together they form the full Jacobian $Df = [\,D_x f \mid D_y f\,]$. The map $f$ is $C^k$ if all partials up to order $k$ are continuous. $B_r(x_0)$ is the open ball; the **cylinder** $B_r(x_0)\times B_s(y_0)$ is a product of balls. The full registry is on [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Statement

> **Implicit function theorem.** Let $0 < d < n$ and $k \geq 1$ be integers, let $U \subseteq \mathbb{R}^d \times \mathbb{R}^{n-d}$ be open, and let $f \in C^k(U, \mathbb{R}^{n-d})$. Suppose $(x_0, y_0) \in U$ satisfies
> $$f(x_0, y_0) = 0,$$
> and that the partial Jacobian in the $y$-variables,
> $$D_y f(x_0, y_0) = \big(\partial_{y_j}f_i(x_0,y_0)\big)_{1 \leq i,j \leq n-d},$$
> is an **invertible** $(n-d)\times(n-d)$ matrix. Then there are radii $r, s > 0$ and a unique map $g \in C^k(B_r(x_0), \mathbb{R}^{n-d})$ with $g(x_0) = y_0$ such that, for all $(x,y)$ in the cylinder $B_r(x_0)\times B_s(y_0)$,
> $$f(x, y) = 0 \quad\Longleftrightarrow\quad y = g(x).$$
> Moreover, the derivative of the implicit function is
> $$Dg(x) = -\big(D_y f(x, g(x))\big)^{-1}\,D_x f(x, g(x)).$$
>
> The conclusion is **local**: it describes the solution set only within the cylinder around $(x_0, y_0)$.

---

# Motivation

An equation and a function are different kinds of object. The equation $x^2 + y^2 = 1$ describes a circle; the function $y = \sqrt{1 - x^2}$ describes a curve you can evaluate, differentiate, plot. The implicit function theorem is the bridge between them: it says *when*, and with what guarantees, an equation can be turned into a function.

In one variable the picture is familiar. The curve $f(x,y) = 0$ can be solved for $y$ as a function of $x$ near a point — written $y = g(x)$ — provided the curve is not vertical there, that is, provided $\partial_y f \neq 0$. Where $\partial_y f = 0$, the curve has a vertical tangent and "$y$ as a function of $x$" breaks down: at $(\pm 1, 0)$ on the circle, $y$ doubles back and is not a function of $x$.

This theorem is the several-variable, several-equation version. You have $n-d$ equations $f_i(x,y) = 0$ in $n$ unknowns, split into $d$ free variables $x$ and $n-d$ dependent variables $y$. The question is whether you can solve the equations for $y$ in terms of $x$. The answer is: yes, locally, provided the *partial Jacobian $D_y f$ in the dependent variables is invertible*. This is the exact multivariable shadow of "$\partial_y f \neq 0$" — it says the equations, linearized, can be solved for the $y$-variables, and the theorem propagates that linear solvability to the genuine nonlinear system.

The value of the theorem is enormous and twofold. First, it lets you treat a set defined by equations *as if* it were a graph — and graphs are the simplest curved objects, the foundation of the entire notion of [[Def - Submanifold of Euclidean Space|submanifold]] in §2.3. Second, it gives you the derivative of the implicit solution *without solving the equation*: the formula $Dg = -(D_y f)^{-1}D_x f$ comes from differentiating $f(x,g(x)) = 0$, and it works even when $g$ has no closed form. This is what makes comparative statics in economics, sensitivity analysis in engineering, and the tangent-space computations of geometry all possible.

As always in this topic the conclusion is **local**. The full solution set of $f = 0$ may be a circle, a figure-eight, several components — globally it is rarely a graph. The theorem promises only a *cylinder* around the chosen base point inside which the equation and the graph coincide, and being precise about this — and about when $D_y f$ can fail to be invertible — is part of the discipline.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f(x_0,y_0) = 0$ and $D_y f(x_0,y_0)$ is invertible". The skill is recognizing this and, in particular, choosing the variable split.

The first disguised source is **a level set with nonvanishing gradient (the scalar case).** Property $B$: $f : \mathbb{R}^n \to \mathbb{R}$ with $\nabla f(p_0) \neq 0$. The bridge: if $\nabla f \neq 0$, then *some* partial $\partial_{x_j}f(p_0) \neq 0$; permute the variables so this is the last one, and the $1\times 1$ partial Jacobian $D_y f$ is that nonzero scalar, hence invertible. So the level set can always be solved for *some* variable. The non-obviousness: a single nonvanishing-gradient condition guarantees solvability without specifying which variable. *Example:* the regular value theorem for hypersurfaces — see [[Thm - The Regular Value Theorem]].

The second disguised source is **a map with surjective derivative.** Property $B$: $f : \mathbb{R}^n \to \mathbb{R}^{n-d}$ with $Df(p_0)$ surjective (maximal rank $n-d$). The bridge: a surjective $(n-d)\times n$ matrix has $n-d$ linearly independent columns; choose those columns as the $y$-variables, and the resulting square block $D_y f$ is invertible. So *surjectivity of the full derivative* is equivalent to "*some* split makes $D_y f$ invertible". The non-obviousness: the abstract rank condition is converted into a concrete variable split. *Example:* this is exactly the hypothesis of the [[Thm - The Regular Value Theorem|regular value theorem]].

The third disguised source is **a parametrized family of equations near a known root.** Property $B$: an equation $\Phi(y; x) = 0$ depending on a parameter $x$, with a known solution $y_0$ at $x = x_0$ and $\partial_y\Phi(y_0; x_0)$ invertible. The bridge: rename, this is exactly $f(x,y) = \Phi(y;x)$, and the theorem says the root $y$ moves *smoothly* with the parameter $x$. The non-obviousness: "the root depends smoothly on the parameter" is a structural fact bought by one invertibility check. *Example:* perturbation theory — eigenvalues and equilibria depending smoothly on a parameter.

**Targets (Output Amplification)**

The conclusion is "$y = g(x)$ locally, with $g$ a $C^k$ map and $Dg = -(D_y f)^{-1}D_x f$".

Combine the conclusion with **the goal of computing a rate of change.** Property $D$: you want $\partial g/\partial x_j$ — how a dependent quantity responds to a free one — but $g$ has no formula. The amplified result $E$: the derivative formula $Dg = -(D_y f)^{-1}D_x f$ delivers the rate of change purely from the partials of $f$, no closed-form $g$ required. This is *comparative statics* in economics, *sensitivity analysis* in engineering — the most-used consequence of the theorem.

Combine the conclusion with **the regular value condition holding at every point.** Property $D$: $Df$ has maximal rank not just at $p_0$ but at every point of $f^{-1}(0)$. The amplified result $E$: the *whole* level set is locally a graph at each of its points, so it is a [[Def - Submanifold of Euclidean Space|submanifold]] — the local graph pictures assemble into a global manifold structure. This local-to-global assembly is the [[Thm - The Regular Value Theorem|regular value theorem]] and the heart of §2.3.

Combine the conclusion with **a second function to be optimized on the solution set.** Property $D$: you wish to extremise $h$ subject to $f = 0$. The amplified result $E$: the implicit function theorem locally turns the *constrained* problem into an *unconstrained* one — substitute $y = g(x)$ into $h$ and minimise the function $x \mapsto h(x, g(x))$ freely. Carrying out the chain rule on this recovers the [[Thm - The Method of Lagrange Multipliers|Lagrange multiplier]] equations.

---

# Why Is It True

The theorem looks like a new result but it is the [[Thm - The Inverse Function Theorem|inverse function theorem]] in disguise, and seeing the disguise *is* the intuition.

Here is the trick. You have a map $f$ from $\mathbb{R}^d\times\mathbb{R}^{n-d}$ to $\mathbb{R}^{n-d}$, which is "not square" — it cannot be inverted as it stands. So *make it square*. Define an auxiliary map
$$\Phi(x, y) = (x,\ f(x,y)),$$
which sends $\mathbb{R}^n$ to $\mathbb{R}^n$ by simply *carrying the $x$-variables along untouched* and putting $f$ in the remaining slots. This is now a square map, and you can ask whether it is invertible. Its derivative has a beautiful block-triangular form:
$$D\Phi(x_0,y_0) = \begin{pmatrix} I_d & 0 \\ D_x f & D_y f\end{pmatrix}.$$
The determinant of a block-triangular matrix is the product of the diagonal blocks' determinants, so $\det D\Phi = \det I_d\cdot\det D_y f = \det D_y f$. Therefore $D\Phi$ is invertible *exactly when $D_y f$ is* — and that is precisely the hypothesis. The inverse function theorem now applies to $\Phi$ and hands you a local $C^k$ inverse $\Psi$.

The rest is reading off what $\Psi$ says. Because $\Phi$ leaves the $x$-coordinate alone, so does $\Psi$ — it has the form $\Psi(\xi, \eta) = (\xi,\ G(\xi,\eta))$ for some $C^k$ map $G$. Now chase the equivalences. The equation $f(x,y) = 0$ says the second component of $\Phi(x,y) = (x, f(x,y))$ is zero, i.e. $\Phi(x,y) = (x, 0)$. Applying $\Psi$: $(x,y) = \Psi(x,0) = (x, G(x,0))$. So $f(x,y) = 0$ is equivalent to $y = G(x,0)$. Define $g(x) := G(x,0)$, and you are done — the implicit function is just the inverse of the auxiliary map, restricted to the slice $\eta = 0$.

So one should expect the theorem because *solving an equation for some variables is inverting a map* — you just have to build the right square map to invert, and "carry the free variables along" is the way to build it. The invertibility of $D_y f$ is exactly the invertibility of that square map's derivative.

The derivative formula then needs no separate machinery. The implicit function $g$ satisfies the *identity* $f(x, g(x)) = 0$ for all $x$ near $x_0$. Differentiate both sides with the [[Thm - The Chain Rule|chain rule]] — the left side has an $x$-dependence both directly and through $g(x)$:
$$0 = D_x f(x, g(x)) + D_y f(x, g(x))\cdot Dg(x).$$
Since $D_y f$ is invertible (it stays invertible near $(x_0,y_0)$ by continuity), solve the linear system:
$$Dg(x) = -\big(D_y f\big)^{-1}D_x f.$$
The formula is just the chain rule applied to the defining identity, then a linear solve. It is worth noticing it requires *nothing* about $g$ beyond its existence and differentiability — both supplied by the theorem — so the rate of change of the implicit solution is computable the moment the theorem applies.

The locality is inherited from the inverse function theorem: $\Psi$ exists only on a neighbourhood, so $g = G(\cdot, 0)$ exists only on a ball, and the equivalence $f = 0 \iff y = g(x)$ holds only inside the cylinder where $\Psi$ is defined.

---

# What Makes This Hard

The non-obvious step is the *construction of the auxiliary square map* $\Phi(x,y) = (x, f(x,y))$ — the device of "carrying the free variables along" to turn the non-square $f$ into an invertible map, after which the [[Thm - The Inverse Function Theorem|inverse function theorem]] does everything. The most common error is in the *choice of variable split*: the theorem solves for $y$ only when the $y$-block $D_y f$ is invertible, and a student picks a split whose block is singular and wrongly concludes the equation cannot be solved — when a *different* split would work; the rule is that solvability for *some* variables needs only $Df$ to have maximal rank. A second frequent slip is treating the result as global, when the equivalence $f = 0 \iff y = g(x)$ holds only inside the cylinder.

---

# Rederivation Scaffold

**High-level strategy:**
Build the auxiliary map $\Phi(x,y) = (x, f(x,y))$, a square map from $\mathbb{R}^n$ to $\mathbb{R}^n$. Its derivative is block-triangular with determinant $\det D_y f$, so it is invertible exactly under the hypothesis. Apply the inverse function theorem to $\Phi$; its inverse has the form $\Psi(\xi,\eta) = (\xi, G(\xi,\eta))$; set $g(x) = G(x,0)$. Get the derivative by differentiating $f(x,g(x)) = 0$.

**Subgoal decomposition:**

1. **Build the auxiliary map.** Define $\Phi(x,y) = (x, f(x,y)) : U \to \mathbb{R}^n$.
   - *Hint:* Carry the $x$-coordinates through unchanged; put $f$ in the remaining $n-d$ slots.
   - *Why needed:* It is a *square* map, so the inverse function theorem can be applied to it.

2. **Compute its derivative and check invertibility.** Show $D\Phi$ is block-triangular with $\det D\Phi = \det D_y f \neq 0$.
   - *Hint:* $D\Phi = \begin{pmatrix} I_d & 0 \\ D_x f & D_y f\end{pmatrix}$; the determinant of a block-triangular matrix is the product of the diagonal blocks.
   - *Why needed:* It transfers the hypothesis "$D_y f$ invertible" into "$D\Phi$ invertible".

3. **Invert $\Phi$.** Apply the [[Thm - The Inverse Function Theorem|inverse function theorem]] to get a $C^k$ local inverse $\Psi$.
   - *Hint:* $\Phi(x_0,y_0) = (x_0, 0)$; the theorem gives $\Psi$ on a neighbourhood of $(x_0,0)$.
   - *Why needed:* $\Psi$ contains the implicit function.

4. **Read off the implicit function.** Show $\Psi(\xi,\eta) = (\xi, G(\xi,\eta))$ and set $g(x) = G(x,0)$.
   - *Hint:* $\Phi$ fixes the first coordinate, so $\Psi$ does too. Then $f(x,y) = 0 \iff \Phi(x,y) = (x,0) \iff (x,y) = \Psi(x,0) \iff y = G(x,0)$.
   - *Why needed:* It produces $g$ with the equivalence and the $C^k$ regularity.

5. **Differentiate the defining identity.** From $f(x,g(x)) = 0$, chain-rule to $Dg = -(D_y f)^{-1}D_x f$.
   - *Hint:* $0 = D_x f + D_y f\cdot Dg$; solve the linear system.
   - *Why needed:* It yields the derivative formula.

---

# Lemma Decomposition

> [!note]- Lemma 1: The auxiliary map has block-triangular derivative
> **Statement:** For $\Phi(x,y) = (x, f(x,y))$, the Jacobian is $D\Phi(x_0,y_0) = \begin{pmatrix} I_d & 0 \\ D_x f & D_y f\end{pmatrix}$, with $\det D\Phi = \det D_y f$.
>
> **Hint:** Differentiate component-by-component; the first $d$ components of $\Phi$ are just $x$.
>
> **Why needed:** It is what converts the hypothesis on $D_y f$ into the invertibility of $D\Phi$ that the inverse function theorem requires.
>
> > [!note]- Full proof
> > The first $d$ components of $\Phi$ are $\Phi_i(x,y) = x_i$, so the top block of $D\Phi$ is $\partial(x)/\partial(x,y) = [\,I_d \mid 0\,]$ — the $x$-coordinates contribute the identity, and they do not depend on $y$ so the top-right block is $0$. The last $n-d$ components are $f(x,y)$, contributing the bottom block $[\,D_x f \mid D_y f\,]$. Hence $D\Phi = \begin{pmatrix} I_d & 0 \\ D_x f & D_y f\end{pmatrix}$. This is block lower-triangular, and the determinant of a block-triangular matrix is the product of the determinants of the diagonal blocks: $\det D\Phi = \det(I_d)\cdot\det(D_y f) = \det D_y f$. So $D\Phi$ is invertible iff $D_y f$ is.

> [!note]- Lemma 2: The inverse of the auxiliary map preserves the first coordinate
> **Statement:** The local inverse $\Psi$ of $\Phi$ has the form $\Psi(\xi, \eta) = (\xi, G(\xi, \eta))$ for some $C^k$ map $G$.
>
> **Hint:** $\Phi$ leaves the first coordinate unchanged; an inverse must too.
>
> **Why needed:** It is what lets the implicit function be extracted as $g(x) = G(x, 0)$.
>
> > [!note]- Full proof
> > Write $\Psi(\xi,\eta) = (\Psi_1(\xi,\eta), \Psi_2(\xi,\eta))$ with $\Psi_1 \in \mathbb{R}^d$, $\Psi_2 \in \mathbb{R}^{n-d}$. Since $\Phi\circ\Psi = \operatorname{Id}$ and the first component of $\Phi(x,y)$ is $x$, the first component of $\Phi(\Psi(\xi,\eta))$ is $\Psi_1(\xi,\eta)$. But $\Phi\circ\Psi = \operatorname{Id}$ forces this to equal $\xi$. Hence $\Psi_1(\xi,\eta) = \xi$, and writing $G := \Psi_2$ gives $\Psi(\xi,\eta) = (\xi, G(\xi,\eta))$. $\Psi$ is $C^k$ by the inverse function theorem, so $G$ is $C^k$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f \in C^k(U, \mathbb{R}^{n-d})$, $f(x_0,y_0) = 0$, $D_y f(x_0,y_0)$ invertible.
>
> **Auxiliary map.** Define $\Phi : U \to \mathbb{R}^n$ by $\Phi(x,y) = (x, f(x,y))$. Then $\Phi \in C^k$ and $\Phi(x_0,y_0) = (x_0, 0)$. By Lemma 1, $D\Phi(x_0,y_0)$ is block-triangular with determinant $\det D_y f(x_0,y_0) \neq 0$, so $D\Phi(x_0,y_0)$ is invertible.
>
> **Inversion.** By the [[Thm - The Inverse Function Theorem|inverse function theorem]], there is an open neighbourhood $U_0$ of $(x_0,y_0)$, which we may take to be a cylinder $B_r(x_0)\times B_s(y_0) \subseteq U$, mapped by $\Phi$ diffeomorphically onto an open set $V \ni (x_0, 0)$, with a $C^k$ inverse $\Psi : V \to U_0$.
>
> **Form of the inverse.** By Lemma 2, $\Psi(\xi,\eta) = (\xi, G(\xi,\eta))$ with $G \in C^k$.
>
> **The implicit function.** For $(x,y) \in U_0$,
> $$f(x,y) = 0 \iff \Phi(x,y) = (x, 0) \iff (x,y) = \Psi(x,0) \iff (x,y) = (x, G(x,0)) \iff y = G(x,0),$$
> where the middle equivalence uses that $\Psi$ is the inverse of $\Phi|_{U_0}$ and that $(x,0) \in V$ for $x$ near $x_0$. Define $g(x) := G(x, 0)$, a $C^k$ map $B_r(x_0) \to \mathbb{R}^{n-d}$ (shrinking $r$ so that $(x,0) \in V$ throughout). Then for $(x,y)$ in the cylinder, $f(x,y) = 0 \iff y = g(x)$, and $g(x_0) = G(x_0,0) = y_0$ since $\Psi(x_0,0) = (x_0,y_0)$. Uniqueness: any $\tilde g$ with $f(x,\tilde g(x)) = 0$ and values in $B_s(y_0)$ satisfies $\tilde g(x) = g(x)$ by the equivalence just proved.
>
> **Derivative formula.** The identity $f(x, g(x)) = 0$ holds for all $x \in B_r(x_0)$. Differentiate with the [[Thm - The Chain Rule|chain rule]]:
> $$0 = D_x f(x, g(x)) + D_y f(x, g(x))\cdot Dg(x).$$
> Since $D_y f$ is invertible at $(x_0,y_0)$, it remains invertible on a (possibly smaller) cylinder by continuity of the entries and of the determinant. Solving the linear system,
> $$Dg(x) = -\big(D_y f(x, g(x))\big)^{-1}\,D_x f(x, g(x)). \qquad\blacksquare$$

---

# Cross-Field Exercise Suggestions

**Comparative statics in economics.** An economic equilibrium is the solution of a system $f(\text{quantities}, \text{parameters}) = 0$. The implicit function theorem says the equilibrium quantities are smooth functions of the parameters, and the derivative formula $Dg = -(D_y f)^{-1}D_x f$ computes *how the equilibrium shifts when a parameter changes* — the central calculation of comparative statics. The application is nonobvious because the equilibrium is never solved for explicitly, yet its sensitivity is fully computable.

**Persistence of equilibria under perturbation.** A dynamical system $\dot y = F(y; \mu)$ has an equilibrium where $F(y;\mu) = 0$. If the Jacobian $D_y F$ is invertible at an equilibrium $y_0$ for $\mu = \mu_0$ (a *hyperbolic* or at least nondegenerate equilibrium), the implicit function theorem guarantees the equilibrium *persists* and moves smoothly as $\mu$ varies. The application battle-tests the theorem: it explains why generic equilibria do not suddenly vanish under small perturbations — and the failure of invertibility is exactly where bifurcations occur.

**The level set of the determinant.** Apply the theorem to $f(X) = \det X - a$ on the space of $n\times n$ matrices. Wherever $\det X = a \neq 0$ one has $D(\det)(X) \neq 0$, so one matrix entry $x_{\mu\nu}$ is locally a smooth function of all the others, subject to keeping the determinant fixed. The application is out-of-distribution because the "variables" are matrix entries and the equation is a polynomial constraint — yet the theorem coordinatizes the level set $\{\det = a\}$ as a graph.

---

# Bridges

- **[[Thm - The Inverse Function Theorem]]** — the parent. The implicit function theorem *is* the inverse function theorem applied to the auxiliary square map $\Phi(x,y) = (x, f(x,y))$. The two are logically equivalent: each is a quick corollary of the other.

- **[[Thm - The Chain Rule]]** — supplies the derivative formula. Differentiating the defining identity $f(x,g(x)) = 0$ is a chain-rule computation.

- **[[Thm - The Regular Value Theorem]]** — the local-to-global assembly. When the rank condition holds at *every* point of a level set, the implicit function theorem makes the set locally a graph at each point; assembling these gives the submanifold structure.

- **[[Thm - The Method of Lagrange Multipliers]]** — an alternative derivation of Lagrange's theorem uses the implicit function theorem to reduce constrained optimization to an unconstrained problem in the graph coordinates.

- **[[Def - Submanifold of Euclidean Space]]** — the *implicit* and *graphical* representations of a submanifold are linked precisely by this theorem.

---

# Unlocked by This

> [!tip] Submanifolds and the Regular Value Theorem *(from this topic)*
> Applying the implicit function theorem at every point of a level set $\{f = c\}$ where $Df$ has maximal rank turns the set into a [[Def - Submanifold of Euclidean Space|submanifold]] — locally a graph at each point. This is the content of the [[Thm - The Regular Value Theorem|regular value theorem]] and the gateway to §2.3.

> [!tip] The Constant Rank Theorem *(from Differential Geometry)*
> When $Df$ has *constant rank* (not necessarily maximal), a refinement of the implicit and inverse function theorems — the **rank theorem** — gives a local normal form in which $f$ is a linear projection. It is the structural basis for the theory of immersions, submersions, and embeddings.

> [!tip] Bifurcation Theory *(from Dynamical Systems)*
> The implicit function theorem guarantees equilibria persist *where $D_y f$ is invertible*. **Bifurcation theory** studies exactly the points where this invertibility fails — where equilibria appear, disappear, or split — the boundary of the theorem's domain of applicability.

---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open; $f : U \to \mathbb{R}^m$; $x_\circ \in U$; $v \in \mathbb{R}^n$ a direction (not necessarily a unit vector). The dot product on $\mathbb{R}^n$ is $u \cdot v = \sum_i u_i v_i$, and $|v| = (v \cdot v)^{1/2}$. The total derivative is $Df_{x_\circ}$ (see [[Def - The Total Derivative and Differentiability]]) and $\partial_j f$ is the $j$-th partial (see [[Def - Partial Derivatives and the Jacobian Matrix]]). The full symbol registry is on [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Axiom Motivation

The partial derivatives probe $f$ along the $n$ coordinate axes. But there is nothing special about the coordinate axes — they are an artefact of how we chose to set up $\mathbb{R}^n$. The natural and basis-independent question is: at what rate does $f$ change as we move away from $x_\circ$ in an *arbitrary* direction $v$? Answering it gives the **directional derivative**, and the partials become the special case $v = e_j$.

The construction is forced. To measure the rate of change of $f$ along the direction $v$, walk along the straight line $t \mapsto x_\circ + tv$, which produces a one-variable function, and take its ordinary derivative at $t = 0$. That derivative — the limit of $\big(f(x_\circ + tv) - f(x_\circ)\big)/t$ — is the directional derivative $\partial_v f(x_\circ)$. It exists as a vector in $\mathbb{R}^m$ exactly when this one-variable limit exists.

Here is where the directional derivative earns its keep, and where it exposes a subtlety. Compute the directional derivatives of a function in *every* direction $v$ and ask: how do they depend on $v$? For a merely-partially-differentiable function the answer can be anything — the directional derivative can fail to exist in some directions, or exist in all directions but depend on $v$ in a wild, non-linear way. But if $f$ is **differentiable** at $x_\circ$, something rigid happens: $\partial_v f(x_\circ) = Df_{x_\circ}(v)$, and since $Df_{x_\circ}$ is *linear*, the directional derivative is **linear in the direction**. Doubling $v$ doubles the rate; the rate along $v + w$ is the sum of the rates along $v$ and $w$. This linearity is a strong, falsifiable consequence of differentiability — and it gives the cheapest test for *non*-differentiability: compute directional derivatives, and if they are not linear in $v$, the function is not differentiable. A function whose directional derivatives all exist but are not linear in $v$ is a function that has a "derivative in every direction" without having a derivative.

For a *scalar* function $f : U \to \mathbb{R}$, the linear map $Df_{x_\circ} : \mathbb{R}^n \to \mathbb{R}$ is a linear functional, and every linear functional on $\mathbb{R}^n$ is "dot product with a fixed vector" — this is the Riesz representation in finite dimensions, the statement that $\mathbb{R}^n$ is its own dual. That fixed vector is the **gradient** $\nabla f(x_\circ)$. So for scalar functions the derivative, abstractly a linear functional, can be repackaged as an honest vector, and $\partial_v f = \nabla f \cdot v$. This repackaging is enormously convenient but it conceals a choice: it used the dot product. The gradient is the dual object to the differential, converted into a vector by the metric. In $\mathbb{R}^n$ with its standard dot product this is free; on a manifold with a general metric, the differential (a covector) and the gradient (a vector) genuinely part ways, and which one is "natural" depends on what you are doing. Worth knowing now, so the later distinction is not a surprise.

---

# The Definition

Let $U \subseteq \mathbb{R}^n$ be open, $f : U \to \mathbb{R}^m$, $x_\circ \in U$, and $v \in \mathbb{R}^n$.

**Directional derivative.** The **directional derivative** of $f$ at $x_\circ$ in the direction $v$ is
$$\partial_v f(x_\circ) \;=\; \frac{d}{ds}\Big|_{s=0} f(x_\circ + s v) \;=\; \lim_{s \to 0} \frac{f(x_\circ + s v) - f(x_\circ)}{s} \;\in\; \mathbb{R}^m,$$
when the limit exists. The $j$-th partial derivative is the special case $v = e_j$: $\partial_{e_j} f = \partial_j f$.

**Relation to the total derivative.** If $f$ is **differentiable** at $x_\circ$, then $\partial_v f(x_\circ)$ exists for *every* $v \in \mathbb{R}^n$ and
$$\partial_v f(x_\circ) \;=\; Df_{x_\circ}(v).$$
Consequently the directional derivative is **linear in the direction**:
$$\partial_{\alpha v + \beta w} f(x_\circ) \;=\; \alpha\,\partial_v f(x_\circ) + \beta\,\partial_w f(x_\circ) \qquad \text{for all } \alpha, \beta \in \mathbb{R},\; v, w \in \mathbb{R}^n.$$

**Gradient.** Let $f : U \to \mathbb{R}$ be a *scalar*-valued function, differentiable at $x_\circ$. The linear functional $Df_{x_\circ} : \mathbb{R}^n \to \mathbb{R}$ is represented by a unique vector, the **gradient**
$$\nabla f(x_\circ) \;=\; \big(\partial_1 f(x_\circ),\, \dots,\, \partial_n f(x_\circ)\big)^{\mathsf T} \;\in\; \mathbb{R}^n,$$
characterised by
$$\partial_v f(x_\circ) \;=\; Df_{x_\circ}(v) \;=\; \nabla f(x_\circ) \cdot v \qquad \text{for all } v \in \mathbb{R}^n.$$
The gradient is the transpose of the (single-row) Jacobian. Among all unit directions $v$, the directional derivative $\nabla f \cdot v$ is largest when $v$ points along $\nabla f$ — so $\nabla f(x_\circ)$ points in the **direction of steepest ascent** and $|\nabla f(x_\circ)|$ is the maximal rate of increase. The gradient is orthogonal to the level set $\{f = f(x_\circ)\}$ through $x_\circ$, since moving tangent to a level set leaves $f$ unchanged, forcing $\nabla f \cdot v = 0$ for tangent directions $v$.

---

# Relate to Other Fields / Compression

The directional derivative is just the one-variable derivative of $f$ along a line — the same construction as the partial derivative, with an arbitrary direction in place of a coordinate axis. The genuinely new content is the rigidity theorem: differentiability forces the directional derivative to be linear in $v$.

The gradient is the finite-dimensional **Riesz representative** of the differential: it converts the linear functional $Df_{x_\circ}$ into a vector using the dot product. In differential geometry this conversion is the **musical isomorphism** raising and lowering indices, and it requires a metric — the differential is a covector (a $1$-form), the gradient is a vector, and they are distinct objects identified only via the metric tensor. The "steepest ascent" property of the gradient is the analytic basis of **gradient descent** in optimisation: to decrease $f$ fastest, step along $-\nabla f$. The orthogonality of the gradient to level sets is the mechanism behind **Lagrange multipliers** (see **Multivariate Analysis II**): at a constrained extremum the gradient of the objective is parallel to the gradient of the constraint, because both are normal to the constraint surface.

---

# Examples / Corollaries

**Is an instance — $f(x,y,z) = x(y^2 + \sin z)$.** The partials are $\partial_x f = y^2 + \sin z$, $\partial_y f = 2xy$, $\partial_z f = x\cos z$, so $\nabla f = (y^2 + \sin z,\; 2xy,\; x\cos z)$. The directional derivative along $v = (1,1,1)$ is $\nabla f \cdot v = y^2 + \sin z + 2xy + x\cos z$ — computed by a dot product, no limit required, because $f$ is differentiable.

**Is an instance — a linear functional $f(x) = a \cdot x$.** Here $\nabla f \equiv a$ everywhere, constant: a linear function has constant gradient, and its directional derivative along $v$ is $a \cdot v$ at every point.

**Is NOT an instance of "directional derivatives linear in $v$" — $f(x,y) = x^3/(x^2+y^2)$, $f(0,0) = 0$.** Along $v = (v_1, v_2)$, one computes $\partial_v f(0,0) = v_1^3/(v_1^2 + v_2^2)$. This limit exists for every direction $v$ — the function has a directional derivative in *all* directions at the origin. But $v \mapsto v_1^3/(v_1^2+v_2^2)$ is *not linear* in $v$: it is not even additive. Therefore $f$ is not differentiable at the origin, even though it is continuous there and has every directional derivative. This is the canonical example separating "all directional derivatives exist" from "differentiable", and it shows the directional-derivative test is a genuine, usable obstruction.

**Is NOT an instance — a non-differentiable function need not even have all directional derivatives.** For $f(x,y) = xy/(x^2+y^2)$ extended by $0$, the directional derivative along a non-axis direction $v = (v_1, v_2)$ with $v_1, v_2 \neq 0$ does not exist: $f(sv_1, sv_2)/s = v_1 v_2/(s(v_1^2+v_2^2))$ blows up as $s \to 0$. Only the two axis directions yield finite partials. So directional derivatives can fail to exist entirely.

**Corollary — steepest ascent.** For a differentiable scalar $f$ with $\nabla f(x_\circ) \neq 0$, the Cauchy–Schwarz inequality gives $|\partial_v f| = |\nabla f \cdot v| \le |\nabla f|\,|v|$, with equality exactly when $v$ is parallel to $\nabla f$. So among unit directions, $f$ increases fastest along $+\nabla f$, decreases fastest along $-\nabla f$, and is momentarily flat along any direction orthogonal to $\nabla f$ — the directions tangent to the level set.

**Calibration check.** Verify that for $f(x,y) = x^2 + y^2$ the gradient at $(1,1)$ is $(2,2)$, that it points radially outward (steepest ascent away from the minimum at the origin), and that it is orthogonal to the level circle $x^2+y^2=2$. Confirm that the directional derivative of a differentiable $f$ along $v$ and along $2v$ differ by a factor of exactly $2$, and explain why this would *not* be forced for a merely-partially-differentiable function.

---

# Unlocked by This

> [!tip] Gradient Descent *(from Convex Optimization)*
> The gradient points along steepest ascent, so $-\nabla f$ points along steepest descent. The iteration $x_{k+1} = x_k - \eta\,\nabla f(x_k)$ — **gradient descent** — is the basic algorithm of smooth optimisation, and convergence rates are governed by the mean value inequality applied to $\nabla f$.

> [!tip] One-Forms and the Musical Isomorphism *(from Differential Geometry)*
> The differential $Df_{x_\circ}$ is naturally a covector — a **$1$-form** — and the gradient is the vector obtained from it by the metric. On a curved space the two are genuinely different objects, and the conversion between them is the index-raising musical isomorphism.

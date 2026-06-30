---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Arbitrary Coordinates and the Coordinate Basis"
  - "Def - The Covariant Derivative"
tags: [physics, special-relativity]
---

# Problem Statement

Let $(x^\alpha)$ be an arbitrary coordinate system on flat spacetime, with coordinate basis $(\vec{e}_\alpha)$.

1. Regarding each coordinate $x^\alpha$ (for fixed $\alpha$) as a scalar field on spacetime, show that its gradient satisfies $\langle\boldsymbol{\nabla}x^\alpha, \vec{e}_\beta\rangle = \delta^\alpha{}_\beta$. Conclude that the four gradients $(\boldsymbol{\nabla}x^\alpha)$ are exactly the **dual basis** of the coordinate basis: $e^\alpha = \boldsymbol{\nabla}x^\alpha = \mathbf{d}x^\alpha$.
2. For a general scalar field $f$, show that the components of its gradient in the coordinate basis are the partial derivatives, $\nabla_\alpha f = \partial f/\partial x^\alpha$, so that $\boldsymbol{\nabla}f = \dfrac{\partial f}{\partial x^\alpha}\,\mathbf{d}x^\alpha$.
3. Explain why the gradient is fundamentally a *linear form* (a covector), not a vector, and what extra structure is needed to make a "gradient vector".

**Recall:**

![[Def - Arbitrary Coordinates and the Coordinate Basis#The Definition]]

The gradient of a scalar field $f$ is the linear form $\boldsymbol{\nabla}f$ defined by $\mathrm{d}f = \langle\boldsymbol{\nabla}f, \mathrm{d}\vec{x}\rangle$, where $\mathrm{d}f = f(M')-f(M)$ is the first-order variation between events $M$ and $M'$ with $\overrightarrow{MM'} = \mathrm{d}\vec{x}$ (see [[Def - The Covariant Derivative]]). The dual basis $(e^\alpha)$ of $(\vec{e}_\alpha)$ is defined by $\langle e^\alpha, \vec{e}_\beta\rangle = \delta^\alpha{}_\beta$.

---

# Convergent Strategy

**Problem class.** A *definition-unpacking* problem establishing the foundational identities $e^\alpha = \mathbf{d}x^\alpha$ and $\nabla_\alpha f = \partial_\alpha f$. The route is to feed coordinate displacements into the definition of the gradient.

**Assumption pattern.** Only the definition of the gradient and of the coordinate basis are needed; the key fact is that the displacement $\overrightarrow{MM'}$ produced by incrementing $x^\beta$ alone is $\mathrm{d}x^\beta\,\vec{e}_\beta$.

**Theorem routing.** Part 1 evaluates $\langle\boldsymbol{\nabla}x^\alpha,\vec{e}_\beta\rangle$ using the definition of the gradient and the coordinate-basis displacement. Part 2 applies the same definition to a general $f$ and matches against $\mathrm{d}f = (\partial f/\partial x^\alpha)\mathrm{d}x^\alpha$. Part 3 is the conceptual observation that the gradient is metric-independent.

**Key decision point.** The crux is recognising that the variation $\mathrm{d}x^\alpha$ of the coordinate *is* the value of the linear form $\boldsymbol{\nabla}x^\alpha$ on the displacement — the same symbol $\mathrm{d}x^\alpha$ wears two hats (infinitesimal increment and exterior derivative of the coordinate function), and seeing they agree is the content.

---

# Legal Operations Used

1. **Covariantly differentiate a scalar** (operations 1 and 3 from the topic page, scalar case). The gradient $\boldsymbol{\nabla}f$ has components $\partial f/\partial x^\alpha$ with no Christoffel correction, because a scalar has no index to dress.

---

# Hints

> [!note]- Hint 1
> Apply the defining relation $\mathrm{d}f = \langle\boldsymbol{\nabla}f,\mathrm{d}\vec{x}\rangle$ to $f = x^\alpha$ and to the displacement $\mathrm{d}\vec{x} = \overrightarrow{MM'}$ where only the $\beta$-coordinate is incremented, so $\mathrm{d}\vec{x} = \mathrm{d}x^\beta\,\vec{e}_\beta$.

> [!note]- Hint 2
> The variation of the coordinate $x^\alpha$ under that displacement is $\mathrm{d}x^\alpha = \delta^\alpha{}_\beta\,\mathrm{d}x^\beta$ (incrementing $x^\beta$ changes $x^\alpha$ only if $\alpha=\beta$). Equate to $\langle\boldsymbol{\nabla}x^\alpha, \mathrm{d}x^\beta\vec{e}_\beta\rangle = \mathrm{d}x^\beta\langle\boldsymbol{\nabla}x^\alpha,\vec{e}_\beta\rangle$.

> [!note]- Hint 3
> For a general $f$, expand $\boldsymbol{\nabla}f = (\nabla_\alpha f)\,e^\alpha = (\nabla_\alpha f)\,\mathbf{d}x^\alpha$ and compare with $\mathrm{d}f = (\partial f/\partial x^\alpha)\mathrm{d}x^\alpha$ (ordinary chain rule). The components must match.

> [!note]- Hint 4
> The gradient eats a *vector* (the displacement) and returns a *number* (the variation). That is the definition of a linear form / covector. To turn it into a vector you must use the metric to raise its index, $(\boldsymbol{\nabla}f)^\alpha = g^{\alpha\beta}\partial_\beta f$ — which requires the scalar product, an extra structure the bare gradient does not need.

---

# Solution

The plan: Part 1 evaluates the gradient of a coordinate on a basis vector and gets the Kronecker delta, identifying the gradients with the dual basis. Part 2 extends to a general scalar and reads off that the components are partials. Part 3 notes the gradient is metric-free, hence a covector.

**Step 1: The gradients of the coordinates are the dual basis.**

> [!note]- Derivation
> Fix $\alpha$ and regard $x^\alpha$ as a scalar field. By the definition of the gradient, for any infinitesimal displacement $\mathrm{d}\vec{x}$,
> $$\mathrm{d}x^\alpha = \langle\boldsymbol{\nabla}x^\alpha, \mathrm{d}\vec{x}\rangle.$$
> Choose $\mathrm{d}\vec{x}$ to increment only the coordinate $x^\beta$, so that $\mathrm{d}\vec{x} = \mathrm{d}x^\beta\,\vec{e}_\beta$ (no sum; from the coordinate-basis definition $\overrightarrow{MM'} = \mathrm{d}x^\beta\vec{e}_\beta$). Under this displacement the variation of $x^\alpha$ is $\mathrm{d}x^\alpha = \delta^\alpha{}_\beta\,\mathrm{d}x^\beta$ (it changes only if $\alpha = \beta$). On the other hand, by linearity of the form,
> $$\langle\boldsymbol{\nabla}x^\alpha, \mathrm{d}x^\beta\vec{e}_\beta\rangle = \mathrm{d}x^\beta\,\langle\boldsymbol{\nabla}x^\alpha, \vec{e}_\beta\rangle.$$
> Equating the two expressions and cancelling the arbitrary $\mathrm{d}x^\beta$ gives
> $$\langle\boldsymbol{\nabla}x^\alpha, \vec{e}_\beta\rangle = \delta^\alpha{}_\beta.$$
> This is precisely the defining property of the dual basis. Therefore the four linear forms $(\boldsymbol{\nabla}x^\alpha)$ are the dual basis of the coordinate basis $(\vec{e}_\alpha)$:
> $$e^\alpha = \boldsymbol{\nabla}x^\alpha = \mathbf{d}x^\alpha.$$

**Step 2: The gradient's components are the partial derivatives.**

> [!note]- Derivation
> Let $f$ be any scalar field. Expand its gradient on the dual basis just found: $\boldsymbol{\nabla}f = (\nabla_\alpha f)\,e^\alpha = (\nabla_\alpha f)\,\mathbf{d}x^\alpha$, where $\nabla_\alpha f := \langle\boldsymbol{\nabla}f,\vec{e}_\alpha\rangle$ are the components. For an infinitesimal displacement $\mathrm{d}\vec{x} = \mathrm{d}x^\alpha\vec{e}_\alpha$,
> $$\mathrm{d}f = \langle\boldsymbol{\nabla}f, \mathrm{d}\vec{x}\rangle = (\nabla_\alpha f)\,\mathrm{d}x^\alpha.$$
> But by the ordinary chain rule for the multivariable function $f(x^0,\dots,x^3)$,
> $$\mathrm{d}f = \frac{\partial f}{\partial x^\alpha}\,\mathrm{d}x^\alpha.$$
> Since both hold for arbitrary independent increments $\mathrm{d}x^\alpha$, the coefficients match:
> $$\boxed{\;\nabla_\alpha f = \frac{\partial f}{\partial x^\alpha}\;}\qquad\Longrightarrow\qquad \boldsymbol{\nabla}f = \frac{\partial f}{\partial x^\alpha}\,\mathbf{d}x^\alpha.$$
> The components of a gradient in *any* coordinate basis are the partial derivatives — with no Christoffel correction, because a scalar field carries no index for the connection to act on. (This is why the gradient was already definable before the connection was introduced.)

**Step 3: The gradient is a covector, not a vector.**

> [!note]- Derivation
> By construction $\boldsymbol{\nabla}f$ takes a vector — the displacement $\mathrm{d}\vec{x}$ — and returns a number — the variation $\mathrm{d}f$. An object that linearly maps vectors to numbers is a *linear form* (covector), an element of the dual space, not a vector. This is intrinsic and uses no scalar product: the variation of $f$ along a displacement is defined whether or not spacetime has a metric.
>
> To manufacture a "gradient *vector*" $\overrightarrow{\boldsymbol{\nabla}}f$ one must raise the index using the metric, $(\overrightarrow{\boldsymbol{\nabla}}f)^\alpha = g^{\alpha\beta}\partial_\beta f$ — and this requires the scalar product, an additional structure. In non-relativistic physics one tacitly uses the Euclidean scalar product to identify the gradient with a vector, which is harmless there; but the clean, metric-independent object is the linear form $\boldsymbol{\nabla}f = (\partial f/\partial x^\alpha)\mathbf{d}x^\alpha$. Keeping this distinction is what makes the upper/lower index bookkeeping of relativity unavoidable.

> [!note]- Complete formal solution
> For fixed $\alpha$, regard $x^\alpha$ as a scalar field. The gradient obeys $\mathrm{d}x^\alpha = \langle\boldsymbol{\nabla}x^\alpha,\mathrm{d}\vec{x}\rangle$; taking $\mathrm{d}\vec{x} = \mathrm{d}x^\beta\vec{e}_\beta$ gives $\delta^\alpha{}_\beta\,\mathrm{d}x^\beta = \mathrm{d}x^\beta\langle\boldsymbol{\nabla}x^\alpha,\vec{e}_\beta\rangle$, so $\langle\boldsymbol{\nabla}x^\alpha,\vec{e}_\beta\rangle = \delta^\alpha{}_\beta$ — the gradients $\boldsymbol{\nabla}x^\alpha = \mathbf{d}x^\alpha$ are the dual basis $e^\alpha$. For general $f$, $\mathrm{d}f = \langle\boldsymbol{\nabla}f,\mathrm{d}\vec{x}\rangle = (\nabla_\alpha f)\mathrm{d}x^\alpha$ and $\mathrm{d}f = (\partial f/\partial x^\alpha)\mathrm{d}x^\alpha$ by the chain rule, so $\nabla_\alpha f = \partial f/\partial x^\alpha$ and $\boldsymbol{\nabla}f = (\partial f/\partial x^\alpha)\mathbf{d}x^\alpha$. The gradient maps the displacement vector to the number $\mathrm{d}f$, hence is a linear form; the corresponding vector requires raising the index with the metric, $g^{\alpha\beta}\partial_\beta f$. $\blacksquare$

---

# Key Takeaways

**The dual basis of a coordinate basis is the exterior derivatives of the coordinates, $e^\alpha = \mathbf{d}x^\alpha$.** This identity is the quiet workhorse behind every component computation in the chapter, and it is what lets a $p$-form be expanded as $A = \sum A_{\alpha_1\cdots\alpha_p}\mathbf{d}x^{\alpha_1}\wedge\cdots$. The symbol $\mathbf{d}x^\alpha$ does double duty — it is both the infinitesimal increment of the coordinate and the exterior derivative of the coordinate function — and the exercise shows these two readings coincide, which is exactly why the notation is consistent. The trigger for using this fact is any time you need to write a tensor or form in components in a coordinate system; the dual basis is automatically the coordinate differentials, and you never have to compute it separately.

**The gradient is a covector, and the relativistic up/down index bookkeeping is forced by the refusal to use the metric prematurely.** The single most clarifying realisation is that the gradient $\partial f/\partial x^\alpha$ has a *lower* index because it is a linear form, an object that eats vectors and returns numbers, defined without any scalar product. Non-relativistic vector calculus hides this by silently raising the index with the Euclidean metric, so that "$\mathrm{grad}\,f$" is presented as a vector; but on spacetime, where the metric is indefinite and the up/down distinction is physical, the gradient must be kept as a covector. This is the prototype of the whole contravariant/covariant distinction: vectors (displacements, velocities) carry upper indices and transform by the Jacobian, while covectors (gradients, momenta-as-derivatives) carry lower indices and transform by the inverse Jacobian. Recognising the gradient as the founding example of a covector is what makes the index gymnastics feel inevitable rather than arbitrary.

**A scalar field has no Christoffel correction — its covariant derivative is its partial derivative in every coordinate system.** This is the one case where $\boldsymbol{\nabla}$ and $\partial$ agree even in curvilinear coordinates, and the reason is structural: the Christoffel terms in the covariant derivative dress the *indices* of a tensor, accounting for the turning of the *basis vectors*, and a scalar has no indices and no basis to turn. This is why the gradient could be defined in the previous section before the connection existed, and it is the base case from which the covariant derivatives of vectors and higher tensors are built by the Leibniz rule. The transferable diagnostic: whenever you are differentiating something with no free indices (a scalar invariant, a contraction like $v_\alpha v^\alpha$), the covariant derivative is just the partial derivative — a fact that often shortcuts a computation by letting you differentiate an invariant in whatever coordinates are convenient.

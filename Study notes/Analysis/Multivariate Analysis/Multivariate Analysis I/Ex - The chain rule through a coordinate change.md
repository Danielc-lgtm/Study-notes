---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Thm - The Chain Rule"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Def - Directional Derivative and the Gradient"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $g : \mathbb{R}^2 \to \mathbb{R}$ be a differentiable function, and let $\Phi : (0,\infty)\times\mathbb{R} \to \mathbb{R}^2$ be the polar-coordinate map $\Phi(r,\theta) = (r\cos\theta,\, r\sin\theta)$. Define $\tilde g = g \circ \Phi$, so $\tilde g(r,\theta) = g(r\cos\theta,\, r\sin\theta)$ is the function $g$ expressed in polar coordinates.

1. Use the chain rule to express the partial derivatives $\partial_r\tilde g$ and $\partial_\theta\tilde g$ in terms of the partial derivatives $\partial_x g$, $\partial_y g$ of $g$.
2. As a concrete check, take $g(x,y) = x^2 + y^2$ and compute $\partial_r\tilde g$, $\partial_\theta\tilde g$ both via the chain rule and by direct substitution; confirm they agree.
3. Solve for $\partial_x g$ and $\partial_y g$ in terms of $\partial_r\tilde g$ and $\partial_\theta\tilde g$ — the inverse coordinate transformation of the gradient.

**Recall:**

The tool is the chain rule, applied to the composite of $g$ with the coordinate map $\Phi$.

![[Thm - The Chain Rule#Statement]]

The [[Thm - The Chain Rule|chain rule]] says $J(g\circ\Phi) = Jg(\Phi)\cdot J\Phi$ — the Jacobian of a composite is the matrix product of the Jacobians. Componentwise, $\partial(g\circ\Phi)/\partial(\text{input variable})$ is the sum over intermediate variables of $(\partial g/\partial\text{intermediate})\cdot(\partial\text{intermediate}/\partial\text{input})$.

The [[Def - Partial Derivatives and the Jacobian Matrix|Jacobian]] of $\Phi$ is the $2\times2$ matrix of partials of $r\cos\theta$ and $r\sin\theta$ with respect to $r$ and $\theta$. The [[Def - Directional Derivative and the Gradient|gradient]] $\nabla g = (\partial_x g, \partial_y g)$ collects the partials of $g$.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-derivative* problem in its purest form: differentiate a composite. As the [[Multivariate Analysis I — Differentiation in Several Variables#Problem-Solving Strategy|topic page strategy]] states, any function presented as a composite or a coordinate change is differentiated by the [[Thm - The Chain Rule|chain rule]], and the payoff is that one multiplies known Jacobians instead of differentiating a messy explicit formula.

**Assumption pattern.** The function $\tilde g$ is literally a composite $g\circ\Phi$, with the inner map $\Phi$ a coordinate change whose Jacobian is already known. The recognisable feature: "the same quantity expressed in different coordinates", which is the universal trigger for the chain rule.

**Theorem routing.** Part 1 is the chain rule, $J\tilde g = Jg(\Phi)\cdot J\Phi$, unpacked into its two components. Part 2 checks the abstract formula against a concrete $g$. Part 3 inverts the relationship by inverting the matrix $J\Phi$ — which is legal exactly because $\det J\Phi = r \neq 0$ on the domain.

**Key decision point.** The only subtlety is keeping straight *which* function's partials are *which*. The chain rule expresses derivatives of the outer-composed function ($\tilde g$, depending on $r,\theta$) through derivatives of the inner-composed function ($g$, depending on $x,y$) evaluated at the moved point $\Phi(r,\theta)$. The phrase "evaluated at $\Phi(r,\theta)$" is the part most often dropped: $\partial_x g$ in the formula means $\partial_x g$ at the point $(r\cos\theta, r\sin\theta)$, not at $(r,\theta)$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Compose with the chain rule.** Write $J\tilde g = Jg(\Phi)\cdot J\Phi$ and read off the components.

2. **Compute partials by Analysis I rules.** Differentiate $r\cos\theta$ and $r\sin\theta$ to assemble $J\Phi$.

3. **Recover the derivative from the partials.** Since $g$ is differentiable, $Jg = (\partial_x g, \partial_y g)$ genuinely is the derivative.

4. **Invert the coordinate change via the inverse derivative.** Since $\det J\Phi = r \neq 0$, the matrix $J\Phi$ is invertible, and $\partial_x g, \partial_y g$ are recovered by multiplying by $(J\Phi)^{-1}$.

---

# Hints

> [!note]- Hint 1
> The chain rule for $\tilde g = g\circ\Phi$ says $J\tilde g(r,\theta) = Jg(\Phi(r,\theta))\cdot J\Phi(r,\theta)$. Here $J\tilde g = (\partial_r\tilde g,\ \partial_\theta\tilde g)$ is a $1\times2$ row, $Jg = (\partial_x g,\ \partial_y g)$ is a $1\times2$ row, and $J\Phi$ is the $2\times2$ Jacobian of the polar map. Multiply the row by the matrix.

> [!note]- Hint 2
> The Jacobian of the polar map is $J\Phi = \begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}$. The first column holds $\partial_r$ of the two components, the second holds $\partial_\theta$. Multiplying $(\partial_x g,\ \partial_y g)$ by this matrix gives the two entries of $J\tilde g$.

> [!note]- Hint 3
> For Part 3, you have $J\tilde g = Jg\cdot J\Phi$, a row equals a row times a matrix. To isolate $Jg$, multiply on the right by $(J\Phi)^{-1}$: $Jg = J\tilde g\cdot(J\Phi)^{-1}$. The inverse of $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ is $\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$, and $ad-bc = \det J\Phi = r$.

---

# Solution

Expressing $g$ in polar coordinates is composing $g$ with the polar map, and the chain rule converts that composition into a matrix product of two Jacobians — one of them, the polar Jacobian, already in hand. The whole exercise is one matrix multiplication and its inverse.

**Step 1: The chain rule gives $\partial_r\tilde g = \cos\theta\,\partial_x g + \sin\theta\,\partial_y g$ and $\partial_\theta\tilde g = -r\sin\theta\,\partial_x g + r\cos\theta\,\partial_y g$.**

> [!note]- Derivation
> By [[Thm - The Chain Rule|the chain rule]] applied to $\tilde g = g\circ\Phi$,
> $$J\tilde g(r,\theta) = Jg(\Phi(r,\theta))\cdot J\Phi(r,\theta).$$
> The polar Jacobian is $J\Phi(r,\theta) = \begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}$ (partials of $r\cos\theta$, $r\sin\theta$ with respect to $r$ then $\theta$). With $Jg = (\partial_x g,\ \partial_y g)$ evaluated at $\Phi(r,\theta)$,
> $$(\partial_r\tilde g,\ \partial_\theta\tilde g) = (\partial_x g,\ \partial_y g)\begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}.$$
> Multiplying the row by the matrix, column by column:
> $$\partial_r\tilde g = (\partial_x g)\cos\theta + (\partial_y g)\sin\theta,$$
> $$\partial_\theta\tilde g = (\partial_x g)(-r\sin\theta) + (\partial_y g)(r\cos\theta) = -r\sin\theta\,\partial_x g + r\cos\theta\,\partial_y g.$$
> Throughout, $\partial_x g$ and $\partial_y g$ are evaluated at the point $\Phi(r,\theta) = (r\cos\theta, r\sin\theta)$.

**Step 2: For $g(x,y) = x^2+y^2$, both methods give $\partial_r\tilde g = 2r$, $\partial_\theta\tilde g = 0$.**

> [!note]- Derivation
> *Via the chain rule.* For $g = x^2+y^2$, $\partial_x g = 2x$, $\partial_y g = 2y$; at the moved point $\Phi(r,\theta)$ these are $\partial_x g = 2r\cos\theta$, $\partial_y g = 2r\sin\theta$. Substituting into Step 1:
> $$\partial_r\tilde g = (2r\cos\theta)\cos\theta + (2r\sin\theta)\sin\theta = 2r(\cos^2\theta+\sin^2\theta) = 2r,$$
> $$\partial_\theta\tilde g = -r\sin\theta(2r\cos\theta) + r\cos\theta(2r\sin\theta) = -2r^2\sin\theta\cos\theta + 2r^2\sin\theta\cos\theta = 0.$$
>
> *Via direct substitution.* $\tilde g(r,\theta) = g(r\cos\theta, r\sin\theta) = (r\cos\theta)^2 + (r\sin\theta)^2 = r^2(\cos^2\theta+\sin^2\theta) = r^2$. So $\partial_r\tilde g = 2r$ and $\partial_\theta\tilde g = 0$ directly.
>
> The two methods agree. (The vanishing of $\partial_\theta\tilde g$ reflects that $x^2+y^2$ is rotationally symmetric — it does not depend on the angle.)

**Step 3: Inverting the coordinate change: $\partial_x g = \cos\theta\,\partial_r\tilde g - \dfrac{\sin\theta}{r}\,\partial_\theta\tilde g$ and $\partial_y g = \sin\theta\,\partial_r\tilde g + \dfrac{\cos\theta}{r}\,\partial_\theta\tilde g$.**

> [!note]- Derivation
> Step 1 reads $J\tilde g = Jg\cdot J\Phi$. To solve for $Jg$, multiply on the right by $(J\Phi)^{-1}$ — legal because $\det J\Phi = r > 0$ on the domain, so $J\Phi$ is invertible (the derivative of an invertible coordinate change is an invertible linear map, by [[Thm - The Chain Rule|the chain rule]] applied to $\Phi\circ\Phi^{-1} = \mathrm{id}$). The inverse of a $2\times2$ matrix is
> $$(J\Phi)^{-1} = \frac{1}{r}\begin{pmatrix}r\cos\theta & r\sin\theta\\ -\sin\theta & \cos\theta\end{pmatrix} = \begin{pmatrix}\cos\theta & \sin\theta\\ -\sin\theta/r & \cos\theta/r\end{pmatrix}.$$
> Then $Jg = J\tilde g\cdot(J\Phi)^{-1}$, i.e.
> $$(\partial_x g,\ \partial_y g) = (\partial_r\tilde g,\ \partial_\theta\tilde g)\begin{pmatrix}\cos\theta & \sin\theta\\ -\sin\theta/r & \cos\theta/r\end{pmatrix}.$$
> Multiplying out,
> $$\partial_x g = \cos\theta\,\partial_r\tilde g - \frac{\sin\theta}{r}\,\partial_\theta\tilde g, \qquad \partial_y g = \sin\theta\,\partial_r\tilde g + \frac{\cos\theta}{r}\,\partial_\theta\tilde g.$$
> These are the formulas that re-express the Cartesian gradient in polar data — the basis of writing differential operators such as the Laplacian in polar coordinates.

> [!note]- Complete formal solution
> **Claim.** With $\tilde g = g\circ\Phi$ and $\Phi$ the polar map, $\partial_r\tilde g = \cos\theta\,\partial_x g + \sin\theta\,\partial_y g$ and $\partial_\theta\tilde g = -r\sin\theta\,\partial_x g + r\cos\theta\,\partial_y g$ (with $\partial g$ at $\Phi(r,\theta)$); inversely $\partial_x g = \cos\theta\,\partial_r\tilde g - \frac{\sin\theta}{r}\partial_\theta\tilde g$, $\partial_y g = \sin\theta\,\partial_r\tilde g + \frac{\cos\theta}{r}\partial_\theta\tilde g$.
>
> By [[Thm - The Chain Rule]], $J\tilde g = Jg(\Phi)\cdot J\Phi$ with $J\Phi = \begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}$. The row–matrix product gives the two forward formulas. Since $\det J\Phi = r \neq 0$, $J\Phi$ is invertible; multiplying $J\tilde g = Jg\cdot J\Phi$ on the right by $(J\Phi)^{-1} = \begin{pmatrix}\cos\theta & \sin\theta\\ -\sin\theta/r & \cos\theta/r\end{pmatrix}$ gives the two inverse formulas. For $g = x^2+y^2$: the chain rule gives $\partial_r\tilde g = 2r$, $\partial_\theta\tilde g = 0$, and direct substitution gives $\tilde g = r^2$ with the same partials. $\blacksquare$

---

# Key Takeaways

**Expressing a quantity in new coordinates is composition, and the chain rule is the mechanical translator.** Whenever the same function is written in two coordinate systems — Cartesian and polar, lab frame and rotating frame, old variables and new — the two versions are related by composition with the coordinate map, and the chain rule converts that composition into a matrix product of Jacobians. This is the universal trigger: see "the same thing in different coordinates" and reach for $J(g\circ\Phi) = Jg\cdot J\Phi$. The practical advantage is that you never differentiate the messy composed formula directly; you multiply two Jacobians, and one of them — the coordinate map's — is usually a standard matrix you already know. Every appearance of the Laplacian, the divergence, or the gradient in non-Cartesian coordinates is this computation.

**The chain rule evaluates the inner function's derivative at the moved point — never drop the evaluation point.** The single most common error in chain-rule computations is to write $\partial_x g$ and forget that it means $\partial_x g$ *at* $\Phi(r,\theta)$, not at $(r,\theta)$. The outer function $g$ lives in $(x,y)$-space; its derivative is a function of $(x,y)$; in the chain rule it is sampled at the image point $\Phi(r,\theta) = (r\cos\theta, r\sin\theta)$. Keeping the evaluation point explicit — writing $\partial_x g\big|_{\Phi(r,\theta)}$ until the substitution is actually made — is the discipline that prevents the error. In the worked check, this is why $\partial_x g = 2x$ became $2r\cos\theta$: $x$ was the *image* coordinate $r\cos\theta$.

**A coordinate change can be inverted at the level of derivatives by inverting its Jacobian — and this is legal exactly where the Jacobian determinant is non-zero.** Part 3 turned "$\tilde g$'s partials in terms of $g$'s" into "$g$'s partials in terms of $\tilde g$'s" by inverting the matrix $J\Phi$. This works because the chain rule applied to $\Phi\circ\Phi^{-1} = \mathrm{id}$ forces $D(\Phi^{-1}) = (D\Phi)^{-1}$ — the derivative of the inverse coordinate change is the inverse of the derivative. The operation is valid precisely where $J\Phi$ is invertible, i.e. where $\det J\Phi \neq 0$; for the polar map that is $r \neq 0$, the whole domain. This is the first glimpse of the inverse function theorem: a non-vanishing Jacobian determinant is what makes a coordinate change locally invertible, and the inverse is then automatically differentiable with the inverse Jacobian.

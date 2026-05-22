---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Affine and Linear Functions on Rn"
tags: [algebra, linear-algebra, applied, calculus]
---

# Notation

Throughout, $f : \mathbb{R}^n \to \mathbb{R}^m$ is a differentiable function and $z \in \mathbb{R}^n$ is the point at which the approximation is built. The partial derivative of the $i$-th component of $f$ with respect to its $j$-th argument is $\partial f_i / \partial x_j$, evaluated at $z$ unless stated otherwise. The **gradient** of a scalar-valued $f : \mathbb{R}^n \to \mathbb{R}$ at $z$ is the column $n$-vector $\nabla f(z) = (\partial f/\partial x_1(z), \dots, \partial f/\partial x_n(z))$. The **Jacobian matrix** $Df(z)$ of a vector-valued $f$ at $z$ is the $m \times n$ matrix with entries $Df(z)_{ij} = \partial f_i / \partial x_j(z)$; its $i$-th row is $\nabla f_i(z)^T$. The hat $\hat f$ denotes the Taylor approximation (Boyd's convention).

---

# Axiom Motivation

The need for a "best linear approximation" is the oldest in calculus: given a complicated function $f$ and a working point $z$, you want a simple function $\hat f$ that agrees with $f$ at $z$ and stays close to $f$ in a small neighbourhood of $z$. The question is *what kind of simple function* and *in what sense close*.

The candidate simple classes, ordered by complexity, are: constants ($\hat f(x) = c$, one parameter), affine functions ($\hat f(x) = a^T x + b$, $n + 1$ parameters), quadratic functions ($\hat f(x) = (1/2) x^T H x + a^T x + b$, more parameters), and so on. The right trade-off in practice is *affine*: it is just complex enough to track the first-derivative information at $z$, but simple enough to be cheap to compute and to interpret.

For an affine $\hat f(x) = a^T x + b$ to be a "good" approximation of $f$ near $z$, three things must hold: (a) the value at $z$ matches, $\hat f(z) = f(z)$; (b) the first-order behaviour matches, meaning every directional derivative agrees, $\nabla \hat f(z)^T h = \nabla f(z)^T h$ for every direction $h$; and (c) the approximation error is *higher order* in the displacement, meaning $|f(x) - \hat f(x)|$ decays faster than $\|x - z\|$ as $x \to z$. These three requirements together determine $\hat f$ uniquely: the constant must be $b$ such that $b + a^T z = f(z)$, the gradient $a$ must equal $\nabla f(z)$, and the resulting affine function is
$$
\hat f(x) = f(z) + \nabla f(z)^T (x - z).
$$
The proof that this is the *unique* affine function satisfying all three desiderata is a direct consequence of the definition of differentiability: $f$ is differentiable at $z$ exactly when the affine function above has approximation error $o(\|x - z\|)$.

Why this specific formulation rather than nearby variants? **Suppose we drop the requirement that $\hat f(z) = f(z)$.** Then $\hat f$ can shift by a constant, and the approximation becomes useless near $z$ (the error at $z$ is the shift itself, which doesn't go to zero). The match at $z$ is the anchor of the approximation. **Suppose we drop the gradient-matching requirement.** Then $\hat f$ can be any affine function passing through $(z, f(z))$, and even the linear approximation $\hat f(x) = f(z)$ (which ignores derivatives entirely) qualifies. But this approximation has error $O(\|x - z\|)$, not $o(\|x - z\|)$ — it is *first-order* in the displacement rather than zeroth-order. The gradient term is what buys the extra order of accuracy. **Suppose we strengthen by also matching the second derivatives.** Then $\hat f$ becomes a quadratic approximation $\hat f(x) = f(z) + \nabla f(z)^T (x-z) + (1/2)(x-z)^T H(z)(x-z)$, which is more accurate but no longer affine — it sacrifices the linear-algebra-friendliness for accuracy. Boyd stays with the first-order approximation because it is the *simplest object that captures the first-order information*, and most applied modelling needs first-order accuracy at most.

The vector-valued case is no harder: for $f : \mathbb{R}^n \to \mathbb{R}^m$, apply the scalar argument to each component $f_i$ separately. The component-wise affine approximations stack into a single affine function $\hat f(x) = f(z) + Df(z)(x - z)$, with the same desiderata generalising entry-wise. The Jacobian $Df(z)$ is the matrix whose $i$-th row is the gradient $\nabla f_i(z)^T$, equivalently the matrix of all $m \cdot n$ partial derivatives.

A reader might worry: doesn't the Taylor approximation depend on the *choice* of $z$? Yes — every working point gives a *different* approximation, and the approximation is genuinely useful only near $z$. Boyd's notation $\hat f(x; z)$ makes the dependence on $z$ explicit when it matters. The intuition is that the approximation tracks $f$ as long as you stay in the region where the first-order information is representative; far from $z$, the approximation is unreliable and one needs either a higher-order Taylor expansion or a different model.

---

# The Definition

**Scalar-valued first-order Taylor approximation.** Let $f : \mathbb{R}^n \to \mathbb{R}$ be differentiable, and let $z \in \mathbb{R}^n$. The **first-order Taylor approximation of $f$ at $z$** is the affine function $\hat f : \mathbb{R}^n \to \mathbb{R}$ defined by
$$
\hat f(x) = f(z) + \nabla f(z)^T (x - z) = f(z) + \sum_{i=1}^n \frac{\partial f}{\partial x_i}(z)\,(x_i - z_i).
$$

**Vector-valued first-order Taylor approximation.** Let $f : \mathbb{R}^n \to \mathbb{R}^m$ be differentiable, and let $z \in \mathbb{R}^n$. The **first-order Taylor approximation of $f$ at $z$** is the affine function $\hat f : \mathbb{R}^n \to \mathbb{R}^m$ defined by
$$
\hat f(x) = f(z) + D f(z) \, (x - z),
$$
where the **Jacobian matrix** $Df(z) \in \mathbb{R}^{m \times n}$ has entries $Df(z)_{ij} = \partial f_i/\partial x_j(z)$. The $i$-th component of $\hat f$ is exactly the scalar Taylor approximation of $f_i$.

**Properties (immediate from the definition).** (i) The approximation matches $f$ at $z$: $\hat f(z) = f(z)$. (ii) The Jacobian of $\hat f$ at any point is the constant matrix $Df(z)$. (iii) For any direction $h \in \mathbb{R}^n$, the directional derivative $\partial_h \hat f(z) = Df(z) h$ equals $\partial_h f(z)$. (iv) The approximation error is $o(\|x - z\|)$ as $x \to z$, in the sense that $\|f(x) - \hat f(x)\|/\|x - z\| \to 0$.

---

# Relate to Other Fields / Compression

Boyd's Taylor approximation is precisely the [[Def - The Total Derivative and Differentiability|total derivative]] of $f$ at $z$, packaged with the affine offset $f(z)$. The total derivative in multivariate analysis is the unique linear map $Df(z) : \mathbb{R}^n \to \mathbb{R}^m$ satisfying $\|f(z + h) - f(z) - Df(z) h\| / \|h\| \to 0$ as $h \to 0$; rearranging, $f(z + h) \approx f(z) + Df(z) h$, which is the Taylor approximation in displacement form. So $\hat f(x) - f(z) = Df(z)(x - z)$ *is* the total derivative applied to the displacement $x - z$. The [[Def - Partial Derivatives and the Jacobian Matrix|Jacobian matrix]] is the matrix of $Df(z)$ in the standard basis.

The scalar special case — the gradient — generalises in two further directions worth naming. In differential geometry, $\nabla f$ at a point is a covector (an element of the cotangent space), and the directional derivative $\nabla f \cdot h$ is the natural pairing with a tangent vector $h$. In probability, the gradient of a log-density is the **score function**, and Taylor approximation is the basis of Laplace approximation, the saddle-point method, and the asymptotic theory of maximum-likelihood estimators.

**True name:** The Taylor approximation is *the best affine approximation*, in the sense that no other affine function has approximation error of smaller order in the displacement. It is the unique linearisation of $f$ at $z$.

---

# Examples / Corollaries

**Is an instance — exact for affine functions.** If $f(x) = Ax + b$ is itself affine, then $Df(z) = A$ at every $z$ (the partial derivatives are the entries of $A$), and the Taylor approximation is $\hat f(x) = (Az + b) + A(x - z) = Ax + b = f(x)$. So the Taylor approximation of an affine function is the function itself, regardless of the choice of expansion point $z$.

**Is an instance — scalar quadratic.** For $f(x) = x_1 x_2$ on $\mathbb{R}^2$ with expansion point $z = (1, 1)$, we have $\nabla f(z) = (z_2, z_1) = (1, 1)$ and $f(z) = 1$, so
$$\hat f(x) = 1 + (1, 1)^T (x - (1, 1)) = x_1 + x_2 - 1.$$
The errors: at $x = (1.05, 0.95)$, $f(x) = 0.9975$ and $\hat f(x) = 1.00$, error $0.0025$. At $x = (0.85, 1.25)$, $f(x) = 1.0625$ and $\hat f(x) = 1.10$, error $0.0375$. The approximation degrades with the size of the displacement, as expected.

**Is an instance — Boyd's example $f(x) = x_1 + \exp(x_2 - x_1)$.** At $z = (1, 2)$, the gradient is $\nabla f(z) = (1 - \exp(z_2 - z_1), \exp(z_2 - z_1)) = (1 - e, e) \approx (-1.7183, 2.7183)$ and $f(z) = 1 + e \approx 3.7183$. The Taylor approximation is
$$\hat f(x) = 3.7183 - 1.7183(x_1 - 1) + 2.7183(x_2 - 2),$$
which Boyd verifies numerically agrees with $f$ to four decimal places for $x$ within $0.05$ of $z$.

**Is NOT an instance — the absolute value $f(x) = |x|$ at $z = 0$.** The function is not differentiable at $0$ (the left and right derivatives are $-1$ and $+1$), so no Taylor approximation exists at $z = 0$. Away from $z = 0$, the Taylor approximation is $\hat f(x) = |z| + \operatorname{sign}(z)(x - z) = \operatorname{sign}(z) x$, which agrees with $f$ only on the same side of $0$ as $z$. The failure at $z = 0$ illustrates that the Taylor framework requires differentiability — non-smooth functions need different approximation tools.

**Corollary — gradient as the steepest-ascent direction.** For scalar $f$, the directional derivative in direction $h$ (with $\|h\| = 1$) is $\nabla f(z)^T h$, maximised when $h = \nabla f(z) / \|\nabla f(z)\|$. So the gradient points in the direction of steepest *ascent* of $f$ at $z$, and its negative is the direction of steepest descent. This is the foundation of gradient-based optimisation.

**Corollary — affine approximation accuracy.** If $f : \mathbb{R}^n \to \mathbb{R}^m$ is $C^2$ on a neighbourhood of $z$ with bounded second derivatives, then $\|f(x) - \hat f(x)\| \leq C \|x - z\|^2$ for some constant $C$ and all $x$ near $z$. The approximation error is *quadratic* in the displacement, which is what justifies the use of first-order Taylor expansion in algorithms like Newton's method (which uses *quadratic* approximation) and gradient descent (which uses *linear* approximation, with step size chosen to control the quadratic error).

**Calibration check.** Verify that for $f(x_1, x_2) = x_1^2 + x_2^2$ at $z = (1, 1)$, the Taylor approximation is $\hat f(x) = 2 + 2(x_1 - 1) + 2(x_2 - 1) = 2x_1 + 2x_2 - 2$. Verify that at $x = (1.1, 1.1)$, $f(x) = 2.42$ and $\hat f(x) = 2.4$, error $0.02 = (0.1)^2 + (0.1)^2$ — exactly the quadratic remainder. Verify that for $f(x) = (x_1 x_2, x_1 + x_2)$ at $z = (1, 1)$, the Jacobian is $Df(z) = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ and $\hat f(x) = (1, 2) + Df(z)(x - z)$.

---

# Unlocked by This

> [!tip] Newton's Method and Optimization *(from Numerical Methods)*
> The first-order Taylor approximation underlies gradient descent; the **second-order** Taylor approximation $f(x) \approx f(z) + \nabla f(z)^T(x - z) + (1/2)(x - z)^T H(z)(x - z)$ with Hessian $H(z)$ underlies **Newton's method**, the fastest classical algorithm for finding stationary points of smooth functions. Newton steps solve the *linear* system $H(z) \Delta x = -\nabla f(z)$ — bringing us back to the central problem of this topic, solving $Ax = b$.

> [!tip] Implicit and Inverse Function Theorems *(from Multivariate Analysis)*
> The Taylor approximation's invertibility — when is $\hat f : \mathbb{R}^n \to \mathbb{R}^n$ a bijection? — is the gateway to the **inverse function theorem**: if $Df(z)$ is invertible, then $f$ itself is locally invertible at $z$. The proof linearises, inverts, and bootstraps — the canonical use of Taylor approximation in pure analysis.

> [!tip] Linearization of Dynamical Systems *(from Dynamical Systems)*
> A nonlinear discrete-time dynamical system $x_{t+1} = f(x_t)$ near an equilibrium $z$ (where $f(z) = z$) is approximated by the linear system $\Delta_{t+1} = Df(z) \Delta_t$ in the displacement $\Delta_t = x_t - z$. Stability of the equilibrium is then read off from the eigenvalues of $Df(z)$ — the same kind of spectral question that controls Boyd's linear dynamical systems in Ch 9.

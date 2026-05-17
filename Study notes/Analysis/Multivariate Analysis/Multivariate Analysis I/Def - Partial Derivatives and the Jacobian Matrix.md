---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - The Total Derivative and Differentiability"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open; $f : U \to \mathbb{R}^m$ a function with components $f_1, \dots, f_m : U \to \mathbb{R}$; $x_\circ \in U$. The standard basis of $\mathbb{R}^n$ is $e_1, \dots, e_n$, where $e_j$ has a $1$ in slot $j$ and $0$ elsewhere. We write $\partial_j f$, $\partial f / \partial x_j$, or $D_j f$ for the $j$-th partial derivative. The total derivative is $Df_{x_\circ} : \mathbb{R}^n \to \mathbb{R}^m$ (see [[Def - The Total Derivative and Differentiability]]). The full symbol registry is on [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Axiom Motivation

The total derivative $Df_{x_\circ}$ is a linear map, which is conceptually clean but not yet *computable*: the definition tells you what $Df_{x_\circ}$ is for, not how to find it. We need a recipe. The recipe comes from the one thing we already know how to do — differentiate functions of a *single* variable — and the idea is to extract single-variable problems from $f$ by freezing all coordinates but one.

Fix $x_\circ$ and look at $f$ as you move only in the $j$-th coordinate direction: the function $t \mapsto f(x_\circ + t e_j)$ is an honest function of one real variable $t$. Its ordinary derivative at $t = 0$ is a vector in $\mathbb{R}^m$, and we call it the **$j$-th partial derivative** $\partial_j f(x_\circ)$. There are $n$ of them, one per coordinate, and each is computed by the rules of Analysis I with the other variables treated as constants. This is the most concrete handle on $f$ available.

Now the design question: how do the partials relate to the total derivative, and is the relationship strong enough to *define* one from the other? The honest answer — and the source of every subtlety in the topic — is that the relationship is one-directional. If $f$ is differentiable, then each partial exists and equals $Df_{x_\circ}(e_j)$, because $\partial_j f(x_\circ)$ is the directional derivative along $e_j$ and a differentiable function's directional derivatives are read off from $Df_{x_\circ}$. A linear map is determined by its values on a basis, so the $n$ vectors $\partial_j f(x_\circ) = Df_{x_\circ}(e_j)$ determine $Df_{x_\circ}$ completely. Arranging them as the columns of a matrix gives the **Jacobian**, and the Jacobian is the matrix of $Df_{x_\circ}$.

But the converse fails, and this is why partial derivatives are a *representation* of the derivative rather than a definition of it. The partials only probe $f$ along the $n$ coordinate axes. They are blind to every other direction. A function can have all $n$ partials at a point — can be perfectly differentiable along each axis — and still be wildly discontinuous along a diagonal, hence not differentiable at all. So we cannot define "differentiable" as "all partials exist"; that would admit pathological functions. The Jacobian is best thought of as a *candidate* for the derivative: it is the matrix that $Df_{x_\circ}$ must equal *if* $f$ is differentiable, and the separate question of whether $f$ actually is differentiable still has to be settled. The point of [[Thm - Continuous Partials Imply Differentiability]] is exactly to give a checkable condition — continuity of the partials — under which the candidate is the genuine article.

Why keep two notations, $Df_{x_\circ}$ for the linear map and $Jf(x_\circ)$ for its matrix, when in $\mathbb{R}^n$ they carry the same information? Because the linear map is the invariant object and the matrix depends on the choice of basis. In $\mathbb{R}^n$ the standard basis is so canonical the distinction looks pedantic. The moment you change coordinates — and certainly the moment you work on a manifold, where no basis is distinguished — the linear map survives unchanged while the matrix transforms. Keeping the two notations separate now is cheap insurance for later.

---

# The Definition

Let $U \subseteq \mathbb{R}^n$ be open, $f : U \to \mathbb{R}^m$, and $x_\circ \in U$.

**Partial derivative.** For $j \in \{1, \dots, n\}$, the **$j$-th partial derivative** of $f$ at $x_\circ$ is
$$\partial_j f(x_\circ) \;=\; \frac{\partial f}{\partial x_j}(x_\circ) \;=\; \lim_{t \to 0} \frac{f(x_\circ + t e_j) - f(x_\circ)}{t} \;\in\; \mathbb{R}^m,$$
when this limit exists. It is the ordinary one-variable derivative of $t \mapsto f(x_\circ + t e_j)$ at $t = 0$ — the derivative with respect to the $j$-th coordinate, all others held constant. For a vector-valued $f$, $\partial_j f$ is the column vector of the partials $\partial_j f_1, \dots, \partial_j f_m$ of the components.

**Jacobian matrix.** If $f$ is **differentiable** at $x_\circ$, then every partial $\partial_j f(x_\circ)$ exists and equals $Df_{x_\circ}(e_j)$. The matrix of the linear map $Df_{x_\circ} : \mathbb{R}^n \to \mathbb{R}^m$ in the standard bases is the **Jacobian matrix**
$$J f(x_\circ) \;=\; \Big(\, \partial_1 f(x_\circ) \;\big|\; \partial_2 f(x_\circ) \;\big|\; \cdots \;\big|\; \partial_n f(x_\circ) \,\Big) \;=\; \left( \frac{\partial f_i}{\partial x_j}(x_\circ) \right)_{\substack{1 \le i \le m \\ 1 \le j \le n}},$$
an $m \times n$ matrix: row $i$ holds the partials of the component $f_i$, column $j$ holds the partial $\partial_j f$. For $v = \sum_j v_j e_j \in \mathbb{R}^n$, the derivative acts by matrix–vector multiplication,
$$Df_{x_\circ}(v) \;=\; J f(x_\circ)\, v \;=\; \sum_{j=1}^n v_j \, \partial_j f(x_\circ).$$
When $m = 1$ the Jacobian is a single row, the **gradient written as a row** (see [[Def - Directional Derivative and the Gradient]]); when $n = 1$ it is a single column, the velocity vector of a curve.

**Warning on logical order.** The Jacobian as the matrix *of the derivative* is meaningful only once $f$ is known to be differentiable. The array of partials can always be written down whenever the partials exist, but if $f$ is not differentiable that array is not the matrix of any linear approximation — it is a candidate that has failed.

---

# Relate to Other Fields / Compression

The partial derivative is the one-variable derivative, no more: it is $f'$ applied to the restriction of $f$ to a coordinate axis. Everything genuinely multivariate is in the *assembly* — the claim that the $n$ partials, when $f$ is differentiable, fit together into a single linear map.

The Jacobian is the bridge between analysis and linear algebra. It says the derivative, an analytic object defined by a limit, is *represented* by a matrix, an algebraic object — and the representation is faithful exactly when $f$ is differentiable. This is the same relationship as between a linear transformation and its matrix in linear algebra, localised to a point. In differential geometry the Jacobian is the matrix of the differential $df_p$ in a pair of charts, and the transformation rule for Jacobians under change of charts *is* the chain rule; demanding that physical or geometric statements be independent of the chart is what forces them to be tensor equations. The determinant of a square Jacobian, $\det Jf$, measures the local volume-scaling factor of $f$ and is the kernel of the change-of-variables formula for integrals (see **Multivariate Analysis III**).

---

# Examples / Corollaries

**Is an instance — $f(x, y, z) = (x^2 + y,\; y^2 + z,\; x + z^2,\; xyz)$, a map $\mathbb{R}^3 \to \mathbb{R}^4$.** Each partial is computed by Analysis I rules with the other variables frozen. The Jacobian is the $4 \times 3$ matrix
$$Jf(x,y,z) = \begin{pmatrix} 2x & 1 & 0 \\ 0 & 2y & 1 \\ 1 & 0 & 2z \\ yz & xz & xy \end{pmatrix},$$
row $i$ holding the partials of $f_i$. The entries are continuous, so $f$ is differentiable everywhere and this is genuinely the matrix of $Df$.

**Is an instance — $f(x,y) = (x^2 - \cos(xy),\; y^4 - e^x)$.** The Jacobian is
$$Jf(x,y) = \begin{pmatrix} 2x + y\sin(xy) & x\sin(xy) \\ -e^x & 4y^3 \end{pmatrix}.$$
Again continuous, hence the true derivative. Computing a Jacobian is bookkeeping: differentiate each component with respect to each variable.

**Is an instance — the squaring map on matrices, $S(X) = X^2$ on $M(n,\mathbb{R}) \cong \mathbb{R}^{n^2}$.** From $(X + Y)^2 = X^2 + (XY + YX) + Y^2$, the linear-in-$Y$ part is $DS(X)\,Y = XY + YX$ and the remainder $Y^2$ is $o(|Y|)$. The "partials" here are with respect to the $n^2$ matrix entries, but the slick route is to read the derivative straight off the algebraic expansion — a reminder that the Jacobian is a representation, and sometimes the linear map is clearer than its matrix.

**Is NOT an instance of "Jacobian = derivative" — $f(x,y) = xy/(x^2+y^2)$, $f(0,0) = 0$.** Both partials at the origin exist and equal $0$, so the array of partials is the zero row vector. But $f$ is discontinuous at $0$ (it equals $\tfrac12$ along $y = x$), hence not differentiable, so the zero row vector is **not** the matrix of any derivative — there is no derivative. The array of partials existed; it just was not a Jacobian in the sense of "matrix of $Df$". See [[Ex - Partial derivatives exist without differentiability]].

**Corollary — the derivative of a known-differentiable map is computed by partial differentiation.** If $f$ is differentiable, then $Df_{x_\circ}$ is the linear map with matrix $Jf(x_\circ)$, and $Df_{x_\circ}(v) = \sum_j v_j \partial_j f(x_\circ)$. So once differentiability is established, all computation reduces to one-variable differentiation. This is the legal operation "recover the derivative from the partials".

**Calibration check.** Compute the Jacobian of the polar-coordinate map $(r,\theta) \mapsto (r\cos\theta,\, r\sin\theta)$ — see [[Ex - The Jacobian of polar coordinates]] — and verify its determinant is $r$. Confirm that for a linear map $f(x) = Ax$ the Jacobian is the constant matrix $A$ everywhere. Check that for $f(x,y) = e^x \cos y$ the Jacobian row is $(e^x\cos y,\; -e^x \sin y)$, and that, because these are continuous, this row genuinely is the derivative.

---

# Unlocked by This

> [!tip] The Jacobian Determinant and Change of Variables *(from Multivariate Analysis III)*
> For a map $\mathbb{R}^n \to \mathbb{R}^n$, the determinant $\det Jf$ is the local volume-scaling factor. It is the weight in the **change of variables formula** $\int_{f(U)} g = \int_U (g \circ f)\,|\det Jf|$, the multivariate substitution rule.

> [!tip] The Rank of the Derivative *(from Multivariate Analysis II)*
> The rank of $Jf(x_\circ)$ — the rank of $Df_{x_\circ}$ as a linear map — governs local behaviour. Full rank makes $f$ a local diffeomorphism (inverse function theorem) or a submersion (implicit function theorem); a **regular value** is one whose preimage is everywhere full-rank.

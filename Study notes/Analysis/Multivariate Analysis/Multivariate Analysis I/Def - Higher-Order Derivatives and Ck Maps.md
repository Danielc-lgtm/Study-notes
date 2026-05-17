---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - Continuous Partials Imply Differentiability"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open; $f : U \to \mathbb{R}^m$. The first-order partials are $\partial_j f$ (see [[Def - Partial Derivatives and the Jacobian Matrix]]); second-order partials are $\partial_i\partial_j f = \partial_i(\partial_j f)$. A **multi-index** is $\alpha = (\alpha_1, \dots, \alpha_n) \in \mathbb{N}^n$, with length $|\alpha| = \alpha_1 + \cdots + \alpha_n$, factorial $\alpha! = \alpha_1!\cdots\alpha_n!$, and associated differential operator $\partial^\alpha = \partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}$ and monomial $x^\alpha = x_1^{\alpha_1}\cdots x_n^{\alpha_n}$. The class $C^0$ is the continuous functions. The full symbol registry is on [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Axiom Motivation

First derivatives capture how a function changes; second and higher derivatives capture how the *change itself* changes — curvature, acceleration, the bending of a graph. In one variable this is routine: differentiate, then differentiate again. The question is how to organise it in several variables, where the first derivative is already an $m\times n$ matrix of partials and a second differentiation could be taken with respect to any of $n$ further variables.

The recursive definition is the obvious one and it is correct: a function is **twice continuously differentiable** if each of its first partials $\partial_j f$ is itself continuously differentiable, **$k$-times continuously differentiable** ($C^k$) if each first partial is $C^{k-1}$. The recursion bottoms out at $C^0$, the continuous functions, and $C^1$, the functions with continuous first partials. This builds a ladder of regularity classes $C^0 \supseteq C^1 \supseteq C^2 \supseteq \cdots \supseteq C^\infty$, each rung strictly smaller than the last.

Why phrase it through *continuity* of the partials rather than mere existence? Because of [[Thm - Continuous Partials Imply Differentiability]]. Continuity of the first partials is exactly the hypothesis that makes a function genuinely differentiable; mere existence of partials is the weaker, pathology-admitting condition. By baking continuity into the definition of $C^k$, the classes become the *useful* regularity classes — the ones the theorems take as hypotheses. "$f \in C^k$" should mean "$f$ has $k$ honest derivatives", and continuity is what makes a derivative honest.

Now the genuinely multivariate complication, and the reason higher derivatives need *more* than the recursion. A second partial can be taken in two orders: $\partial_i\partial_j f$ or $\partial_j\partial_i f$. Are they equal? For a general function with merely-existing second partials, **no** — there are functions whose mixed partials disagree. If the order mattered, then a derivative of order $k$ would be specified by an *ordered* string of $k$ indices, and the bookkeeping would be a combinatorial mess. The rescue is [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]]: for $C^2$ functions, $\partial_i\partial_j f = \partial_j\partial_i f$, and for $C^k$ functions every partial of order $\le k$ is independent of the order of differentiation. This is *why* the definition of $C^k$ is worth making with continuity built in: continuity of the partials is precisely the hypothesis that makes Schwarz's theorem hold, and Schwarz's theorem is what makes higher derivatives manageable.

Schwarz's theorem licenses the **multi-index** notation. Since the order does not matter, a $k$-th order partial of a $C^k$ function is determined not by an ordered string $(j_1, \dots, j_k)$ but only by *how many times each variable appears* — a tuple $\alpha = (\alpha_1, \dots, \alpha_n)$ counting the differentiations in each variable. This is the multi-index, and $\partial^\alpha = \partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}$ is the corresponding operator, unambiguous exactly because of Schwarz. The multi-index is not a mere abbreviation; it is the correct data type for a higher derivative once the order-independence is in place, and it is what makes the statement of Taylor's theorem in several variables compact rather than monstrous.

---

# The Definition

Let $U \subseteq \mathbb{R}^n$ be open and $f : U \to \mathbb{R}^m$.

**The class $C^k$.** Define recursively:
- $f \in C^0(U, \mathbb{R}^m)$ means $f$ is continuous on $U$.
- $f \in C^1(U, \mathbb{R}^m)$ means all first partials $\partial_1 f, \dots, \partial_n f$ exist on $U$ and are continuous on $U$.
- For $k > 1$, $f \in C^k(U, \mathbb{R}^m)$ means all first partials $\partial_j f$ exist on $U$ and each $\partial_j f \in C^{k-1}(U, \mathbb{R}^m)$.

Equivalently, $f \in C^k(U)$ if and only if every partial derivative of $f$ of order at most $k$ — every iterated partial $\partial_{i_1}\cdots\partial_{i_\ell} f$ with $\ell \le k$ — exists and is continuous on $U$. A function is **$k$-times continuously differentiable**, or **of class $C^k$**, when it is in $C^k(U)$. We write $C^k(U)$ for $C^k(U, \mathbb{R})$. The class $C^\infty(U, \mathbb{R}^m) = \bigcap_{k\ge0} C^k(U, \mathbb{R}^m)$ consists of the **smooth** functions — those of class $C^k$ for every $k$.

**Higher-order partial derivatives.** For indices $i_1, \dots, i_\ell \in \{1, \dots, n\}$, the **$\ell$-th order partial derivative** is defined recursively by
$$\partial_{i_1}\partial_{i_2}\cdots\partial_{i_\ell} f = \partial_{i_1}\big(\partial_{i_2}\cdots\partial_{i_\ell} f\big),$$
each step an ordinary partial derivative. When $f \in C^\ell$, all such derivatives exist and are continuous.

**Multi-index notation.** A **multi-index** is a tuple $\alpha = (\alpha_1, \dots, \alpha_n)$ of non-negative integers. Its **length** (or order) is $|\alpha| = \alpha_1 + \cdots + \alpha_n$ and its **factorial** is $\alpha! = \alpha_1!\cdots\alpha_n!$. For $f \in C^{|\alpha|}$, the **multi-index derivative** is
$$\partial^\alpha f = \partial_1^{\alpha_1}\partial_2^{\alpha_2}\cdots\partial_n^{\alpha_n} f$$
— the partial taking $\alpha_j$ derivatives in the $j$-th variable. By [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]], for $f \in C^{|\alpha|}$ this is well-defined: it does not depend on the order in which the differentiations are performed, only on the counts $\alpha_j$. The associated **monomial** is $x^\alpha = x_1^{\alpha_1}\cdots x_n^{\alpha_n}$, a polynomial of degree $|\alpha|$. We write $\beta \le \alpha$ when $\beta_j \le \alpha_j$ for every $j$.

**The Hessian.** For a *scalar* $f \in C^2(U)$, the **Hessian** at $x_\circ$ is the $n\times n$ matrix of second partials
$$D^2 f(x_\circ) = \big(\partial_i\partial_j f(x_\circ)\big)_{1\le i,j\le n}.$$
By Schwarz's theorem the Hessian is a **symmetric matrix**.

---

# Categorical Definition

The classes $C^k$ are best understood as the objects of a tower of categories. For each $k$ there is a category $\mathbf{C}^k$ whose objects are open subsets of Euclidean spaces and whose morphisms are the $C^k$ maps between them; the identity is $C^k$ and the composite of two $C^k$ maps is $C^k$ (this is a genuine theorem — see Examples below), so $\mathbf{C}^k$ really is a category. The inclusions $C^\infty \subseteq \cdots \subseteq C^2 \subseteq C^1 \subseteq C^0$ are *forgetful functors* $\mathbf{C}^{k+1} \to \mathbf{C}^k$, each remembering less regularity. A function being "exactly $C^k$" means it lives in $\mathbf{C}^k$ but not in the image of $\mathbf{C}^{k+1}$. In differential geometry the category $\mathbf{C}^\infty$ is the one in which smooth manifolds and smooth maps are defined; the choice of $k$ is the choice of how much regularity the geometry is built on, and $k = \infty$ is the standard, most convenient choice because then no rung-counting is ever needed.

---

# Relate to Other Fields / Compression

The $C^k$ classes are the regularity scale of analysis, and almost every theorem in the subject is the statement that some operation lands a function on a particular rung. The recursive definition is the direct generalisation of the one-variable $C^k$ classes; the only genuinely new content is multi-dimensional, namely the order-independence of mixed partials, which has no one-variable analogue.

In the theory of partial differential equations, the order of a PDE and the $C^k$ class of its solutions are the central bookkeeping: a second-order equation expects $C^2$ solutions, and *elliptic regularity* theorems are statements that solutions are smoother than the equation a priori requires. In differential geometry, $C^\infty$ is the default category — manifolds, tensor fields, and connections are all smooth — and the multi-index notation is exactly what makes the local coordinate expressions of curvature and covariant derivatives writable. The multi-index is also the indexing set for the monomials in a power series and for the terms of the multivariate Taylor expansion; it is the same combinatorial object that organises the multinomial theorem $(x_1 + \cdots + x_n)^k = \sum_{|\alpha|=k}\frac{k!}{\alpha!}x^\alpha$.

---

# Examples / Corollaries

**Is an instance — every polynomial is $C^\infty$.** A polynomial in $n$ variables has partials that are again polynomials, of one degree lower; these are continuous, and iterating, every partial of every order exists and is continuous. So polynomials are smooth. Likewise $\exp$, $\sin$, $\cos$, and any function built from these by sums, products, and composition is $C^\infty$ on its natural domain.

**Is an instance — sums, products, and composites of $C^k$ functions are $C^k$.** If $f, g \in C^k(U)$, then $f + g$ and $fg$ are $C^k$: the recursion plus the product rule expresses $\partial_j(fg) = (\partial_j f)g + f(\partial_j g)$ as a sum of products of a $C^{k-1}$ and a $C^k$ function, and induction on $k$ closes the argument. If $h \in C^k(V)$ with $h(V) \subseteq U$, then $f \circ h \in C^k$: the chain rule expresses $\partial_j(f\circ h) = \sum_\ell (\partial_\ell f\circ h)\,\partial_j h_\ell$, a sum of products of $C^{k-1}$ functions, and induction again closes it. This is what makes $\mathbf{C}^k$ a category.

**Is NOT an instance of $C^2$ — a function with discontinuous (or unequal) second partials.** The function $f(x,y) = xy(x^2-y^2)/(x^2+y^2)$, extended by $f(0,0)=0$, has both mixed second partials at the origin, but they are *unequal*: $\partial_x\partial_y f(0,0) = -1$ while $\partial_y\partial_x f(0,0) = +1$ (see [[Ex - A function with unequal mixed partials]]). The reason is that the second partials, while existing, are *not continuous* at the origin — so $f \notin C^2$ there. This shows the gap between "second partials exist" and "$C^2$", and shows that the order-independence baked into multi-index notation is a genuine hypothesis, not a definition.

**Is NOT an instance — a function that is $C^1$ but not $C^2$.** The two-variable promotion of $x^2\sin(1/x)$ (see [[Ex - A function differentiable but not continuously differentiable]]) is differentiable but not $C^1$; by adjusting the prefactor power one builds, for any $k$, functions that are $C^k$ but not $C^{k+1}$ — the rungs of the ladder are strictly nested.

**Corollary — the multi-index notation is unambiguous for $C^k$ functions.** For $f \in C^{|\alpha|}$, the expression $\partial^\alpha f$ denotes a single well-defined function regardless of the order in which the $|\alpha|$ differentiations are carried out. This is a corollary of [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]] and is the precondition for everything multi-index notation is used for.

**Corollary — the Hessian of a $C^2$ scalar function is symmetric.** Since $\partial_i\partial_j f = \partial_j\partial_i f$ for $f \in C^2$, the matrix $D^2 f(x_\circ) = (\partial_i\partial_j f(x_\circ))$ equals its transpose. Symmetric real matrices have an orthonormal eigenbasis and real eigenvalues — which is what makes the second-derivative test for extrema (positive/negative definiteness of the Hessian) a clean spectral criterion.

**Calibration check.** Verify that $f(x,y) = x^3 y^2$ is $C^\infty$ and compute $\partial^\alpha f$ for $\alpha = (1,1)$, $(2,0)$, $(3,2)$; check $\partial^{(3,2)}f$ is the constant $3!\cdot2! = 12$. Confirm that for $\alpha = (2,1,0)$, $|\alpha| = 3$ and $\alpha! = 2$. Explain why $\partial^\alpha f$ is well-defined for a $C^{|\alpha|}$ function but the notation would be ambiguous for a function with merely-existing partials.

---

# Unlocked by This

> [!tip] Smooth Manifolds *(from Differential Geometry)*
> A **smooth manifold** is a space modelled on $\mathbb{R}^n$ with transition maps of class $C^\infty$. The whole edifice of differential geometry is built in the category $\mathbf{C}^\infty$, and the multi-index notation is what makes the local coordinate formulas for curvature and covariant derivatives writable.

> [!tip] Elliptic Regularity *(from Partial Differential Equations)*
> The $C^k$ ladder is the scale on which the regularity of PDE solutions is measured. **Elliptic regularity** theorems state that solutions of elliptic equations are smoother than the equation forces a priori — a solution of a $C^\infty$-coefficient elliptic equation is itself $C^\infty$.

> [!tip] Taylor's Theorem and Jets *(from this topic and Algebraic Geometry)*
> Being $C^k$ is exactly the hypothesis under which the $k$-th order **Taylor expansion** exists ([[Thm - Taylor's Theorem in Several Variables]]). The collection of all partials of order $\le k$ at a point is the **$k$-jet** of the function, the basic object of jet bundles and of the local algebra of singularities.

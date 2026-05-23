---
type: definition
subject: linear-algebra
prereqs:
tags: [algebra, linear-algebra, applied]
---

# Notation

Throughout, $\mathbb{R}^n$ is the space of real $n$-vectors written as columns, and $\mathbb{R}^{m \times n}$ is the space of real $m \times n$ matrices. The standard unit vectors are $e_1, \dots, e_n \in \mathbb{R}^n$, with $e_i$ having a $1$ in slot $i$ and zeros elsewhere. The inner product is $a^T x = \sum_i a_i x_i$, and the matrix–vector product $A x$ has $i$-th entry $\sum_j A_{ij} x_j$. The zero vector and zero matrix are written $0$, with size inferred from context.

This is a compound page: it defines four interlocking notions — linear function $\mathbb{R}^n \to \mathbb{R}$, affine function $\mathbb{R}^n \to \mathbb{R}$, linear function $\mathbb{R}^n \to \mathbb{R}^m$, and affine function $\mathbb{R}^n \to \mathbb{R}^m$ — because they are introduced together in Boyd Ch 2 and Ch 8, and the vector-valued versions are direct generalisations of the scalar-valued ones. The unifying fact is that each linear function has a unique matrix representation and each affine function has a unique matrix-plus-vector representation; this lets us pass freely between functions and the matrices that represent them.

---

# Axiom Motivation

Why this specific notion of "linear" and not some nearby variant? The story starts with two desiderata that any "tractable" function should satisfy in the applied setting. First, **scaling the input should scale the output**: if you double the loadings on a bridge, the sag should double (assuming the bridge is not damaged). Second, **adding two inputs should add the outputs**: if loading $w$ produces sag $s$ and loading $w'$ produces sag $s'$, then loading $w + w'$ should produce sag $s + s'$. These two properties together — homogeneity $f(\alpha x) = \alpha f(x)$ and additivity $f(x + y) = f(x) + f(y)$ — are equivalent to the single statement $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$ for all $\alpha, \beta, x, y$, which is called **superposition**.

What goes wrong if we *weaken* superposition to hold only for *positive* coefficients? Then $f$ is what's called a "homogeneous function of degree one in the cone of nonnegative inputs", and this class includes things like $f(x) = \max(x_1, x_2)$, which is not linear in the usual sense: $f(1, -1) + f(-1, 1) = 1 + 1 = 2$ but $f(0, 0) = 0$. The negative directions are what give linear functions their power — they let you cancel, subtract, and invert, all moves that the applied modeller relies on.

What goes wrong if we *strengthen* superposition by also requiring multiplicativity, $f(x_1 x_2) = f(x_1)f(x_2)$? Then $f$ becomes a power function, like $x \mapsto x^a$ for some $a$, which is too restrictive for modelling — most real-world relationships are not power laws.

So linear functions are the Goldilocks class: closed under arbitrary linear combinations, including those with negative coefficients, but not so restricted that they exclude everything interesting. The **representation theorem** $f(x) = a^T x$ is what makes the class operational: a linear function is *exactly* a weighted sum of the input entries, with weights $a_i = f(e_i)$ extracted by probing the function at each standard unit vector. To know a linear function it suffices to know its $n$ values $f(e_i)$, and these values determine $f$ everywhere by superposition.

Now consider why we need the **affine** class as well. The fundamental observation is that real-world models almost never pass through the origin. A regression model has an intercept ($v \neq 0$ in $\hat y = x^T \beta + v$); a temperature has a reference value; a price has a level; a Taylor approximation has a constant term $f(z) \neq 0$. The class of functions $f(x) = a^T x + b$ — linear plus a constant — captures all of these. The cost of admitting the constant $b$ is that superposition holds only when $\alpha + \beta = 1$ (an **affine combination**), not for arbitrary coefficients:
$$f(\alpha x + \beta y) = a^T(\alpha x + \beta y) + b = \alpha(a^T x) + \beta(a^T y) + b = \alpha f(x) + \beta f(y) - (\alpha + \beta - 1) b.$$
The right-hand side equals $\alpha f(x) + \beta f(y)$ precisely when $\alpha + \beta = 1$. So affine functions preserve *affine* (or weighted-average-like) combinations, not general linear combinations.

What if we strengthened "affine" by additionally requiring affinity to hold under arbitrary linear combinations? That would force $b = 0$, i.e., the function would have to be linear. So affine is the unique relaxation of linear that admits a constant term, and it is exactly the right class for applied modelling.

The vector-valued cases — functions $\mathbb{R}^n \to \mathbb{R}^m$ — are direct generalisations: a function $f : \mathbb{R}^n \to \mathbb{R}^m$ is linear if it satisfies superposition (in the obvious sense, with vector outputs), and affine if it satisfies affine superposition. The representation theorems become: every linear $f$ has the form $f(x) = Ax$ for a unique $A \in \mathbb{R}^{m \times n}$, with columns $A e_i = f(e_i)$; every affine $f$ has the form $f(x) = Ax + b$ for a unique pair $(A, b)$, with $b = f(0)$ and $A$'s columns $A e_i = f(e_i) - f(0)$.

---

# The Definition

**Linear function $\mathbb{R}^n \to \mathbb{R}$.** A function $f : \mathbb{R}^n \to \mathbb{R}$ is **linear** if it satisfies the superposition property
$$
f(\alpha x + \beta y) = \alpha f(x) + \beta f(y) \quad \text{for all } x, y \in \mathbb{R}^n,\ \alpha, \beta \in \mathbb{R}.
$$

**Inner-product representation theorem (scalar case).** A function $f : \mathbb{R}^n \to \mathbb{R}$ is linear if and only if there exists a unique $a \in \mathbb{R}^n$ with $f(x) = a^T x$ for all $x \in \mathbb{R}^n$. The components of $a$ are $a_i = f(e_i)$.

**Affine function $\mathbb{R}^n \to \mathbb{R}$.** A function $f : \mathbb{R}^n \to \mathbb{R}$ is **affine** if it satisfies the restricted superposition property
$$
f(\alpha x + \beta y) = \alpha f(x) + \beta f(y) \quad \text{for all } x, y \in \mathbb{R}^n,\ \alpha, \beta \in \mathbb{R} \text{ with } \alpha + \beta = 1.
$$

**Representation theorem for affine functions (scalar case).** A function $f : \mathbb{R}^n \to \mathbb{R}$ is affine if and only if there exists a unique pair $(a, b)$ with $a \in \mathbb{R}^n$, $b \in \mathbb{R}$, such that $f(x) = a^T x + b$ for all $x \in \mathbb{R}^n$. The data are extracted by $b = f(0)$ and $a_i = f(e_i) - f(0)$.

**Linear function $\mathbb{R}^n \to \mathbb{R}^m$.** A function $f : \mathbb{R}^n \to \mathbb{R}^m$ is **linear** if $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$ for all $x, y \in \mathbb{R}^n$, $\alpha, \beta \in \mathbb{R}$.

**Matrix representation theorem (vector case).** A function $f : \mathbb{R}^n \to \mathbb{R}^m$ is linear if and only if there exists a unique matrix $A \in \mathbb{R}^{m \times n}$ with $f(x) = A x$ for all $x \in \mathbb{R}^n$. The columns of $A$ are $f(e_1), \dots, f(e_n)$.

**Affine function $\mathbb{R}^n \to \mathbb{R}^m$.** A function $f : \mathbb{R}^n \to \mathbb{R}^m$ is **affine** if affine superposition (above) holds with vector outputs. Equivalently, $f(x) = A x + b$ for a unique pair $(A, b) \in \mathbb{R}^{m \times n} \times \mathbb{R}^m$, with $b = f(0)$ and $A$'s columns $A e_i = f(e_i) - f(0)$.

---

# Categorical / Structural Definition

A linear function $\mathbb{R}^n \to \mathbb{R}^m$ is exactly a [[Def - Linear Map|linear map]] of vector spaces, in the sense of LADR Ch 3, between the concrete spaces $\mathbb{R}^n$ and $\mathbb{R}^m$. The space of all such linear maps is itself a vector space (under pointwise addition and scalar multiplication), denoted $\mathcal L(\mathbb{R}^n, \mathbb{R}^m)$ in LADR or $\mathbb{R}^{m \times n}$ in Boyd; the bijection between linear maps and $m \times n$ matrices makes this identification clean.

An affine function is a linear map followed by a translation. In more structural terms, affine functions are the morphisms in the category of *affine spaces* — sets equipped with a free transitive action of a vector space — and they form the natural setting for geometric models where "the origin" is not distinguished. An affine subspace of $\mathbb{R}^n$ is the preimage $f^{-1}(c)$ of a single value under an affine function $f$, and affine functions are exactly those that map affine [[Def - Subspace|subspaces]] to affine [[Def - Subspace|subspaces]].

Composing two affine functions gives an affine function: if $f(x) = Ax + b$ and $g(y) = Cy + d$, then $(f \circ g)(x) = (CA)x + (Cb + d)$. So linear and affine functions form categories under composition, with the categorical identity being the literal identity function and the matrix-side identity being $I$.

---

# Relate to Other Fields / Compression

A linear function on $\mathbb{R}^n$ is the simplest possible function: it is fully determined by its $n$ values on the standard basis $e_1, \dots, e_n$, and once those values are known the function can be evaluated anywhere by a single inner product. This is the analog of a "matrix element" in quantum mechanics, the "linear functional" in functional analysis, the "1-form" in differential geometry, and the "linear regression weight vector" in statistics. Every one of those objects is the same algebraic object — a linear map to the scalar field — wearing a different disciplinary hat.

An affine function is a linear function plus a constant; geometrically, it is a hyperplane in $\mathbb{R}^{n+1}$ regarded as the graph $\{(x, f(x)) : x \in \mathbb{R}^n\} \subset \mathbb{R}^{n+1}$. Affine functions and linear functions are connected by the standard trick of **homogenisation**: prepend a $1$ to every input vector, so $x \in \mathbb{R}^n$ becomes $(1, x) \in \mathbb{R}^{n+1}$, and then $f(x) = a^T x + b$ becomes $\tilde f(\tilde x) = \tilde a^T \tilde x$ with $\tilde a = (b, a)$ — genuinely linear. This is why software libraries that handle "linear models with bias" silently add a constant feature to every input.

**True name:** A linear function is a *weighted sum*. An affine function is a *weighted sum plus an offset*. Every formula in this topic that involves either is best read by extracting the weight vector $a$ and (if present) the offset $b$, then thinking of $f$ as "the weighted sum with these weights".

---

# Examples / Corollaries

**Is an instance — the inner product with a fixed vector.** For any fixed $a \in \mathbb{R}^n$, the function $f(x) = a^T x$ is linear; this is the prototypical example, and the representation theorem says it is essentially the only one. Concrete cases: the average $f(x) = (1/n)\mathbf{1}^T x$, the sum $f(x) = \mathbf{1}^T x$, the dot product with a coefficient vector. Each is linear, and the weight vector is read off immediately.

**Is an instance — the regression prediction with an intercept.** The function $\hat y(x) = x^T \beta + v$ is affine (in $x$), not linear (when $v \neq 0$). The standard trick: define $\tilde x = (1, x) \in \mathbb{R}^{n+1}$ and $\tilde \beta = (v, \beta) \in \mathbb{R}^{n+1}$; then $\hat y(x) = \tilde x^T \tilde \beta$ is genuinely linear in $\tilde x$. This is what statistics software does internally when fitting a regression with a "constant term".

**Is an instance — vector-valued linear function from a matrix.** Any $A \in \mathbb{R}^{m \times n}$ defines a linear function $f(x) = A x$. Conversely, every linear function $\mathbb{R}^n \to \mathbb{R}^m$ arises this way. The negation map $f(x) = -x$ (matrix $A = -I$), the reversal map $f(x) = (x_n, \dots, x_1)$ (matrix the reverser, with $1$s on the anti-diagonal), the running-sum map (lower-triangular all-ones matrix), and the de-meaning map (matrix $I - (1/n)\mathbf{1}\mathbf{1}^T$) are all linear.

**Is NOT an instance — the maximum function.** $f(x) = \max\{x_1, \dots, x_n\}$ is not linear (for $n \geq 2$). Witness: with $x = (1, -1)$, $y = (-1, 1)$, $\alpha = \beta = 1/2$, we have $f(\alpha x + \beta y) = f(0, 0) = 0$, but $\alpha f(x) + \beta f(y) = 1/2 + 1/2 = 1 \neq 0$. It is *not* affine either, as the same counterexample shows with $\alpha + \beta = 1$. The maximum is **piecewise linear** — linear on each region where the order of the entries is fixed — but globally neither linear nor affine.

**Is NOT an instance — the absolute value (vector form).** The componentwise absolute-value function $f(x) = (|x_1|, \dots, |x_n|)$ is not linear: $f(-x) = f(x) \neq -f(x)$ unless $x = 0$. It is the canonical example of a function that obeys homogeneity for *positive* scalars only.

**Corollary — sums of linear functions are linear.** If $f, g : \mathbb{R}^n \to \mathbb{R}^m$ are linear with matrices $A, B$, then $f + g$ has matrix $A + B$. If $f$ is linear with matrix $A$ and $\gamma$ is a scalar, then $\gamma f$ has matrix $\gamma A$. So linear functions form a vector space, with matrix-vector identification preserved.

**Corollary — compositions of affine functions are affine.** If $f(x) = Ax + b$ and $g(y) = Cy + d$, then $(g \circ f)(x) = C(Ax + b) + d = (CA)x + (Cb + d)$, an affine function with matrix $CA$ and offset $Cb + d$. The matrix-side composition is matrix multiplication; the offset transforms additively.

**Calibration check.** Verify that the function $f(x_1, x_2) = 2 x_1 - x_2 + 3$ is affine but not linear (compute $f(0) = 3 \neq 0$ to refute linearity, and the representation $a = (2, -1)$, $b = 3$ to confirm affineness). Verify that the de-meaning function $f(x) = x - \operatorname{avg}(x)\mathbf{1}$ is linear (it factors as $f(x) = (I - (1/n)\mathbf{1}\mathbf{1}^T) x$, so the matrix is $I - (1/n)\mathbf{1}\mathbf{1}^T$). Verify that the sort function — which permutes the entries of $x$ into decreasing order — is *not* linear by finding a counterexample $f(x + y) \neq f(x) + f(y)$.

---

# Unlocked by This

> [!tip] Linear Maps and Matrices *(from Linear Algebra III)*
> Once you have a linear function and a matrix representation, you have everything needed to develop the systematic theory of linear maps: kernels, ranges, the rank-nullity theorem, invertibility, change of basis. See [[Linear Algebra III — §3A–D Linear Maps]].

> [!tip] Regression and Generalized Linear Models *(from Statistics)*
> The regression model $\hat y = x^T \beta + v$ is the foundation of supervised learning. Extensions include logistic regression (where the link function is non-linear but the regression model lives "inside"), Gaussian process regression, and the wide class of **generalised linear models** $g(\mathbb{E}[y \mid x]) = x^T \beta + v$ with a link function $g$. All are built on top of the affine function class.

> [!tip] Linear Programming and Convex Optimization *(from Optimization)*
> Affine functions are the building blocks of **linear programming**: minimise a linear function subject to affine inequality constraints. They are also the defining objects of **affine subspaces** (the feasible sets of equality-constrained problems) and **half-spaces** (the feasible sets of inequality-constrained problems). Convex optimisation rests entirely on the affine framework, extended by convex combinations.

---
type: topic
subject: linear-algebra
chapter: "Applied I (Boyd Ch 1-11)"
title: "Linear Algebra X — Applied I: Vectors, Distance, Equations, Dynamics"
tags: [algebra, linear-algebra, applied]
---

# Notation Registry

This topic is Boyd-and-Vandenberghe's applied half of linear algebra: vectors are tuples of real numbers, matrices are two-dimensional arrays, and the goal is always to encode some real-world phenomenon — a dataset, a network, a dynamical system — as a linear-algebraic object and then exploit linearity to compute something useful. Throughout, $\mathbb{R}^n$ is the space of real $n$-vectors, written as columns by default, and $\mathbb{R}^{m \times n}$ is the space of real $m \times n$ matrices. The abstract LADR-side notions of [[Def - Vector Space|vector space]], [[Def - Linear Map|linear map]], and [[Def - Inner Product Space|inner product space]] specialise here to $\mathbb{R}^n$ with the standard basis, the standard inner product, and the Euclidean norm — Boyd's vectors and matrices *are* the elements of those abstract structures, restricted to a concrete coordinate system.

> [!warning] Convention: indices start at $1$
> Boyd indexes vector and matrix entries from $1$, not $0$. So a $4$-vector $x$ has entries $x_1, x_2, x_3, x_4$, and an $m \times n$ matrix $A$ has entries $A_{ij}$ for $1 \leq i \leq m$, $1 \leq j \leq n$. Computer languages like Python and C use $0$-based indexing — the recipe for converting is to subtract one from every index.

- $x, y, a, b$ — column $n$-vectors in $\mathbb{R}^n$, written $x = (x_1, \dots, x_n)$
- $e_i$ — the $i$-th standard unit vector, with a $1$ in slot $i$ and $0$ elsewhere
- $\mathbf{1}$ — the vector of all ones; $\mathbf{1}_n$ if dimension is emphasised
- $x^T y = \sum_i x_i y_i$ — the standard inner product (Boyd writes $x^T y$ rather than $\langle x, y \rangle$)
- $\|x\| = \sqrt{x^T x}$ — the Euclidean norm; sometimes $\|x\|_2$
- $\operatorname{avg}(x) = \mathbf{1}^T x / n$ — the average of the entries
- $\operatorname{rms}(x) = \|x\|/\sqrt{n}$ — the root-mean-square value
- $\operatorname{std}(x) = \|x - \operatorname{avg}(x)\mathbf{1}\|/\sqrt{n}$ — the standard deviation
- $\angle(x, y) = \arccos\big(x^T y/(\|x\|\|y\|)\big)$ — the angle between two nonzero vectors
- $\rho(x, y)$ — the correlation coefficient, the angle's cosine after de-meaning
- $A, B, C$ — matrices; $A_{ij}$ is the $(i,j)$ entry; $a_j$ is the $j$-th column; $b_i^T$ is the $i$-th row
- $A^T$ — the transpose, $(A^T)_{ij} = A_{ji}$
- $\|A\| = \sqrt{\sum_{ij} A_{ij}^2}$ — the Frobenius norm of a matrix
- $I$ — the identity matrix of the appropriate size
- $a \ast b$ — the convolution of two vectors
- $x_t$ — the state at time $t$ in a linear dynamical system; $x_{t+1} = A x_t$ is the update
- $A^{-1}$ — the inverse of a square invertible matrix; $A^\dagger$ — the pseudoinverse
- $\operatorname{nnz}(x)$ — the number of nonzero entries of $x$

The Boyd register differs from LADR in two visible ways. First, a vector is always a tuple — $x = (1, 2, -3) \in \mathbb{R}^3$ — and there is no need to talk about abstract bases. Second, matrices are arrays rather than coordinate representations of linear maps; when Boyd writes $A x$ he means a specific numerical computation, not the action of an abstract operator. The connection is not lost — every Boyd matrix *is* the matrix of a [[Def - Linear Map|linear map]] $\mathbb{R}^n \to \mathbb{R}^m$ in the standard basis — but the emphasis is computational throughout.

---

# Motivation

Here is the entire topic in one sentence: every Boyd construction is a way to encode real-world data as vectors and matrices, and then exploit linearity to compute. The pattern recurs in every chapter and is worth stating as a display, because every later section is an instance of it:

$$
\text{phenomenon} \;\longrightarrow\; \text{linear-algebra object} \;\longrightarrow\; \text{standard algorithm} \;\longrightarrow\; \text{numerical answer}.
$$

A time series of monthly rainfall is a vector; the difference of two rainfall vectors is a vector you can take a norm of, and that norm is the root-mean-square deviation between two cities. A network of warehouses with goods flowing along edges is an incidence matrix, and the matrix–vector product of that incidence matrix with the flow vector is the net surplus at each node. A population sorted by age and updated each year by birth and death rates is a state vector and a matrix; iterating the matrix predicts the demographic profile a decade from now. A set of measurements of a function of $n$ variables, well-approximated near a point, is a Taylor expansion — and the Taylor expansion of any differentiable function is an affine function $\hat f(x) = f(z) + Df(z)(x - z)$, the simplest object in this entire topic.

Two distinctions thread through everything below and deserve to be foregrounded. The first is the distinction between **linear** and **affine** functions. A linear function $f(x) = a^T x$ satisfies $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$ for *all* scalars $\alpha, \beta$. An affine function $f(x) = a^T x + b$ satisfies superposition only when $\alpha + \beta = 1$. The class of affine functions is what applied modelling actually wants — a regression model has an intercept, a line in the plane has a $y$-intercept, a Taylor approximation has a constant term — but it is a single translation away from being linear, and almost every theorem stated for linear functions has an affine version that requires only re-centering. The second is the distinction between **square**, **over-determined** ($m > n$), and **under-determined** ($m < n$) systems of linear equations: when you encounter $Ax = b$, the very first thing to ask is which case you are in, because the answer dictates which algorithm (back-substitution, QR with normal equations, or the pseudoinverse) is the right tool.

The four sections cover Boyd Ch 1–11 in order. §X.1 builds vectors, inner products, linear functions, the regression model, and the Taylor approximation — the vector-and-function foundation. §X.2 develops norm, distance, angle, standard deviation, correlation, clustering by $k$-means, linear independence, basis, orthonormality, and the Gram–Schmidt algorithm — the geometry of $\mathbb{R}^n$. §X.3 introduces matrices proper, the matrix examples that underlie applications (geometric transformations, selectors, incidence matrices, convolutions), the linear-and-affine function picture in vector-valued form, and systems of linear equations. §X.4 covers linear dynamical systems, matrix multiplication and composition, the QR factorization, and matrix inverses (left, right, two-sided, and pseudo-).

The reader is assumed to be comfortable with first-year calculus, partial derivatives, and elementary geometry of $\mathbb{R}^2$ and $\mathbb{R}^3$, but no prior exposure to abstract linear algebra is needed; this topic is self-contained. Readers who have already worked through [[Linear Algebra I — §1 Vector Spaces|Linear Algebra I]] through [[Linear Algebra VI — §6 Inner Product Spaces|Linear Algebra VI]] will find this topic mostly a recovery of familiar facts in concrete coordinates, with the genuinely new content being the *applications* — population dynamics, $k$-means, convolution, incidence matrices, the pseudoinverse interpreted as least squares — rather than the underlying linear algebra.

---

# Concept Map

## §X.1 Vectors and Linear Functions

This section covers Boyd Ch 1–2: vectors as tuples, vector addition and scalar multiplication, the inner product as a weighted sum, linear functions characterised by superposition, the inner-product representation theorem $f(x) = a^T x$, affine functions as linear plus constant, the first-order Taylor approximation, and the regression model.

- **[[Def - Affine and Linear Functions on Rn]]**
	- A function $f : \mathbb{R}^n \to \mathbb{R}$ is **linear** if $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$ for all vectors $x, y$ and all scalars $\alpha, \beta$ (superposition); it is **affine** if the same holds only when $\alpha + \beta = 1$. The representation theorem says every linear $f$ has the form $f(x) = a^T x$ for a unique vector $a$, and every affine $f$ has the form $f(x) = a^T x + b$ for a unique pair $(a, b)$ — extracted by $a_i = f(e_i) - f(0)$, $b = f(0)$. Linear is the special case $b = 0$. The class extends verbatim to vector-valued functions $f : \mathbb{R}^n \to \mathbb{R}^m$, where the data become $f(x) = Ax$ (linear) and $f(x) = Ax + b$ (affine) with $A \in \mathbb{R}^{m \times n}$, $b \in \mathbb{R}^m$.

- **[[Def - Taylor Approximation (Boyd)]]**
	- For a differentiable $f : \mathbb{R}^n \to \mathbb{R}$ and a point $z \in \mathbb{R}^n$, the **first-order Taylor approximation at $z$** is the affine function $\hat f(x) = f(z) + \nabla f(z)^T (x - z)$, where $\nabla f(z)$ is the gradient — the vector of partial derivatives at $z$. For vector-valued $f : \mathbb{R}^n \to \mathbb{R}^m$ the gradient is replaced by the **Jacobian** $Df(z)$, an $m \times n$ matrix of partial derivatives, giving $\hat f(x) = f(z) + Df(z)(x - z)$. The approximation is exact when $f$ is itself affine. This is the [[Def - The Total Derivative and Differentiability|total derivative]] in Boyd's notation: $Df(z)$ is the matrix of the best linear approximation to $f$ at $z$, and the [[Def - Partial Derivatives and the Jacobian Matrix|Jacobian]] is its representation in the standard basis.

> [!tip] Unlocked: The Total Derivative *(from Multivariate Analysis)*
> Boyd's Taylor approximation is the same construction as the total derivative in multivariate analysis, specialised to functions $\mathbb{R}^n \to \mathbb{R}^m$. The total derivative at $z$ is a linear map $Df(z) : \mathbb{R}^n \to \mathbb{R}^m$ characterised intrinsically by the limit $\|f(z + h) - f(z) - Df(z) h\|/\|h\| \to 0$ as $h \to 0$; Boyd's gradient and Jacobian are the matrices of that map in the standard basis. See [[Def - The Total Derivative and Differentiability]].

> [!tip] Unlocked: Numerical Methods for Linear Systems *(from Numerical Linear Algebra)*
> Once $Ax = b$ is identified as the central computational primitive, the whole subject of numerical linear algebra — Gaussian elimination, LU factorization, iterative methods like conjugate gradient, sparse direct solvers — opens up. The driving question is how to solve $Ax = b$ efficiently when $A$ is huge, sparse, or ill-conditioned.

- **[[Ex - Regression model as an affine function]]** (⭐)
	- Verify that the regression model $\hat y = x^T \beta + v$ is an affine function of the feature vector $x$, identify the linear part and the offset, and re-express it as a single inner product after the standard trick of prepending a constant feature equal to $1$.

> [!note] Exercise Index — §X.1
> [[Exercise Index - §X.1 Vectors and Linear Functions]]

## §X.2 Distance, Clustering, and Independence

This section covers Boyd Ch 3–5: the Euclidean norm and its properties, the distance between vectors, root-mean-square and standard deviation, the angle between vectors via Cauchy–Schwarz, the correlation coefficient, $k$-means clustering, linear dependence and independence, basis, orthonormal vectors, and the Gram–Schmidt algorithm.

- **[[Def - Norm and Distance]]**
	- The **Euclidean norm** of an $n$-vector is $\|x\| = \sqrt{x^T x} = \sqrt{x_1^2 + \cdots + x_n^2}$, generalising absolute value of a scalar; the **distance** between $x$ and $y$ is $\|x - y\|$. The norm is nonnegative, homogeneous ($\|\alpha x\| = |\alpha|\|x\|$), positive-definite ($\|x\| = 0 \iff x = 0$), and obeys the **triangle inequality** $\|x + y\| \leq \|x\| + \|y\|$. The companion notions are the **mean square value** $\operatorname{ms}(x) = \|x\|^2/n$ and the **root-mean-square** $\operatorname{rms}(x) = \|x\|/\sqrt n$; the RMS gives a dimension-independent "typical size" of an entry, equal to $|\alpha|$ when every entry of $x$ is $\alpha$. The norm of a stacked vector $(a, b, c)$ is $\|(a, b, c)\|^2 = \|a\|^2 + \|b\|^2 + \|c\|^2$.

- **[[Def - Standard Deviation and Correlation Coefficient]]**
	- The **de-meaned vector** of $x$ is $\tilde x = x - \operatorname{avg}(x)\mathbf{1}$; the **standard deviation** is $\operatorname{std}(x) = \|\tilde x\|/\sqrt n = \operatorname{rms}(\tilde x)$, the typical deviation from the mean. The fundamental identity is $\operatorname{rms}(x)^2 = \operatorname{avg}(x)^2 + \operatorname{std}(x)^2$. The **correlation coefficient** of two non-constant $n$-vectors $a, b$ is $\rho = \tilde a^T \tilde b / (\|\tilde a\|\|\tilde b\|)$, the cosine of the angle between their de-meaned versions; it always lies in $[-1, 1]$ by Cauchy–Schwarz. In matrix-finance language $\operatorname{std}$ is "risk" and $\rho$ measures hedging power: $\operatorname{std}(a + b)^2 = \operatorname{std}(a)^2 + 2\rho \operatorname{std}(a)\operatorname{std}(b) + \operatorname{std}(b)^2$.

- **[[Def - Angle Between Vectors]]**
	- For nonzero $a, b \in \mathbb{R}^n$, the **angle** is $\angle(a, b) = \arccos\big(a^T b/(\|a\|\|b\|)\big) \in [0, \pi]$. The definition rests on the [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz inequality]] $|a^T b| \leq \|a\|\|b\|$, which guarantees the arccos argument lies in $[-1, 1]$. Special cases name themselves: $\angle = \pi/2$ is orthogonal ($a^T b = 0$), $\angle = 0$ is aligned (positive scalar multiple), $\angle = \pi$ is anti-aligned (negative scalar multiple), and $\angle < \pi/2$ is acute (positive inner product). In two and three dimensions the formula recovers the school geometry definition.

- **[[Thm - Cauchy-Schwarz and the Angle in Rn]]**
	- For any $a, b \in \mathbb{R}^n$, $|a^T b| \leq \|a\|\|b\|$, with equality if and only if one of the vectors is a scalar multiple of the other. The proof expands $\|\beta a - \alpha b\|^2 \geq 0$ with $\alpha = \|a\|$, $\beta = \|b\|$ and rearranges. This inequality is the bedrock that makes angle, correlation, and the triangle inequality all well-defined; it is one of the most-used facts in applied mathematics, recurring in probability (as $|\mathbb{E}[XY]| \leq \sqrt{\mathbb{E}[X^2]\mathbb{E}[Y^2]}$), in functional analysis (in any [[Def - Inner Product Space|inner product space]]), and in statistics (as the bound on the correlation coefficient).

- **[[Def - Clustering and k-Means]]**
	- Given $N$ vectors $x_1, \dots, x_N \in \mathbb{R}^n$ and an integer $k \geq 1$, **clustering** is an assignment $c : \{1, \dots, N\} \to \{1, \dots, k\}$ together with **group representatives** $z_1, \dots, z_k \in \mathbb{R}^n$, chosen to make the **clustering objective** $J^{\text{clust}} = (1/N)\sum_i \|x_i - z_{c_i}\|^2$ small. The **$k$-means algorithm** alternates two steps: (1) with $z_j$ fixed, assign each $x_i$ to the nearest representative; (2) with the assignment fixed, set each $z_j$ to the centroid of its group. Each step decreases $J^{\text{clust}}$, so the algorithm converges in finitely many steps. It is the simplest non-convex EM-style algorithm, and is the workhorse of unsupervised learning.

- **[[Thm - Convergence of k-Means]]**
	- The $k$-means algorithm terminates in finitely many iterations. At every iteration the objective $J^{\text{clust}}$ is non-increasing (Step 1 minimises $J^{\text{clust}}$ over assignments with $z_j$ fixed; Step 2 minimises $J^{\text{clust}}$ over $z_j$ with assignments fixed). Because there are only finitely many partitions of $N$ items into $k$ groups — at most $k^N$ — the sequence of distinct objective values is finite, and the algorithm must stabilise once both steps cease to change anything. Convergence is to a *local* minimum of $J^{\text{clust}}$; running from several random initialisations and keeping the best is the standard remedy.

> [!tip] Unlocked: Principal Component Analysis *(from Statistics)*
> Once you have centring, norms, and the Gram matrix, **principal component analysis** is the next conceptual step: find the orthogonal directions of maximal variance in a dataset, equivalent to finding the eigenvectors of $X X^T$ for the centred data matrix $X$. PCA is the linear analogue of $k$-means with continuous "clusters" — one writes data as a low-rank approximation in the directions of greatest spread.

> [!tip] Unlocked: Spectral Clustering *(from Machine Learning)*
> $k$-means clusters points by Euclidean distance, but many natural datasets cluster along curves or manifolds where Euclidean distance is misleading. **Spectral clustering** replaces the distance with a graph Laplacian eigenstructure: build a similarity graph, take its Laplacian $L = D - W$, find the smallest eigenvectors, and run $k$-means in that embedded space. It is the gateway from Boyd to graph signal processing.

- **[[Ex - Triangle inequality for the Euclidean norm]]** (⭐)
	- Prove the triangle inequality $\|a + b\| \leq \|a\| + \|b\|$ by expanding $\|a + b\|^2$, applying Cauchy–Schwarz to bound the cross term $a^T b$, and taking the square root.

- **[[Ex - Correlation coefficient via Cauchy-Schwarz]]** (⭐)
	- Show that the correlation coefficient $\rho(a, b) \in [-1, 1]$ for any two non-constant vectors $a, b$, and characterise when equality holds at $\pm 1$.

- **[[Ex - k-Means with two clusters on a one-dimensional dataset]]** (⭐⭐)
	- Run the $k$-means algorithm by hand on a small one-dimensional dataset with $k = 2$, verify that the algorithm converges to a partition where one cluster contains all points below some threshold and the other contains all points above it, and identify the optimal threshold.

> [!note] Exercise Index — §X.2
> [[Exercise Index - §X.2 Distance, Clustering, and Independence]]

## §X.3 Matrices and Linear Equations

This section covers Boyd Ch 6–8: matrices as two-dimensional arrays, transpose, addition, the matrix Frobenius norm, matrix–vector multiplication, the matrix examples that drive applications (geometric transformations, selectors, incidence matrices, convolution), vector-valued linear and affine functions, and systems of linear equations $Ax = b$.

- **[[Def - Convolution]]**
	- The **convolution** of an $n$-vector $a$ and an $m$-vector $b$ is the $(n + m - 1)$-vector $c = a \ast b$ with $c_k = \sum_{i + j = k + 1} a_i b_j$. Equivalently, the coefficients of the polynomial product: if $a$ holds the coefficients of $p(t)$ and $b$ holds those of $q(t)$, then $a \ast b$ holds the coefficients of $p(t)q(t)$. Convolution is symmetric ($a \ast b = b \ast a$), associative, and bilinear; as a function of one argument with the other fixed it is a linear map, with matrix the **Toeplitz** form $T(b)$ where each diagonal is constant. Convolution is the connection from linear algebra to signal processing: a moving average is convolution with $(1/3, 1/3, 1/3)$, a first difference is convolution with $(1, -1)$, an audio filter is convolution with a short kernel, and the response of a discrete linear time-invariant system to an input is the convolution of the input with the system's impulse response.

- **[[Def - Incidence Matrix]]**
	- For a directed graph with $n$ nodes and $m$ edges, the **incidence matrix** $A \in \mathbb{R}^{n \times m}$ has $A_{ij} = 1$ if edge $j$ points *into* node $i$, $A_{ij} = -1$ if edge $j$ points *out of* node $i$, and $A_{ij} = 0$ otherwise — exactly two nonzero entries per column. If $f \in \mathbb{R}^m$ is a flow vector, then $Af$ is the $n$-vector of net flows *into* each node; **flow conservation** is $Af + s = 0$ where $s$ is the source vector. For node potentials $v \in \mathbb{R}^n$, the edge potential differences are $A^T v$, and the **Dirichlet energy** $D(v) = \|A^T v\|^2 = \sum_{\text{edges}} (v_l - v_k)^2$ measures roughness. The incidence matrix is the bridge from linear algebra to graph theory: $A A^T$ minus its diagonal is the negative of the graph Laplacian.

> [!tip] Unlocked: Sparse Linear Algebra *(from Numerical Linear Algebra)*
> Incidence matrices and convolution Toeplitz matrices are both **sparse** — most entries are zero. Sparse linear algebra is the systematic study of how to store, manipulate, and factor matrices in time and memory proportional to the number of nonzeros, not the total number of entries. It is what makes large-scale optimisation, finite-element methods, and graph algorithms tractable.

> [!tip] Unlocked: Graph Theory and Laplacians *(from Discrete Mathematics)*
> The incidence matrix $A$ of a graph contains *all* the algebraic information about the graph. The product $L = AA^T$ (with appropriate sign conventions) is the **graph Laplacian**, a matrix whose eigenvalues encode connectivity, expansion, mixing times of random walks, and many other graph invariants. Spectral graph theory is the systematic exploitation of this matrix.

- **[[Ex - Triangle inequality for the Euclidean norm|Triangle inequality for the Euclidean norm]]** *(see §X.2; cross-referenced here for the matrix norm version $\|A + B\| \leq \|A\| + \|B\|$, which is the same statement applied to the $mn$-vector of entries)*

> [!note] Exercise Index — §X.3
> [[Exercise Index - §X.3 Matrices and Linear Equations]]

## §X.4 Dynamical Systems, Multiplication, and Inverses

This section covers Boyd Ch 9–11: linear dynamical systems and their applications (population, epidemic, mechanical, supply-chain), matrix–matrix multiplication as composition of linear functions, matrix powers and their interpretation in graphs and dynamical systems, the QR factorization via Gram–Schmidt, left and right inverses, the unique two-sided inverse for square invertible matrices, solving linear equations $Ax = b$ via the inverse, and the pseudoinverse $A^\dagger = (A^T A)^{-1} A^T$ for tall full-column-rank matrices.

- **[[Def - Linear Dynamical System]]**
	- A **linear dynamical system** is a sequence of $n$-vectors $x_1, x_2, \dots$ — the **state trajectory** — evolving via $x_{t+1} = A_t x_t$, with the $n \times n$ matrix $A_t$ called the **dynamics matrix**. When $A_t = A$ does not depend on $t$ the system is **time-invariant**, and iterating gives $x_{t+\ell} = A^\ell x_t$. A linear dynamical system **with input** has the form $x_{t+1} = A_t x_t + B_t u_t + c_t$, with $u_t$ an exogenous $m$-vector input. The state $x_t$ contains all the information needed to predict the future, by definition; this is what makes it the "state". Special cases: a **Markov model** is exactly the time-invariant case; a $K$-Markov model $x_{t+1} = \sum_{j=0}^{K-1} A_{j+1} x_{t-j}$ can be reduced to a standard linear dynamical system in the larger state $(x_t, x_{t-1}, \dots, x_{t-K+1})$.

- **[[Def - Left and Right Inverse of a Matrix]]**
	- A **left inverse** of an $m \times n$ matrix $A$ is an $n \times m$ matrix $X$ with $XA = I_n$; a **right inverse** is an $n \times m$ matrix $X$ with $AX = I_m$. A left inverse exists if and only if the columns of $A$ are linearly independent, and forces $m \geq n$ (the matrix is square or tall). A right inverse exists if and only if the rows of $A$ are linearly independent, and forces $m \leq n$ (the matrix is square or wide). For square matrices, left- and right-invertibility coincide and the inverse is unique, denoted $A^{-1}$; the matrix is then called **invertible** or **nonsingular**. For a non-square left-invertible $A$, the **pseudoinverse** $A^\dagger = (A^T A)^{-1} A^T$ is a canonical choice of left inverse, with $A^\dagger A = I$.

- **[[Thm - Conditions for a Square Matrix to be Invertible]]**
	- For an $n \times n$ matrix $A$, the following are equivalent: (1) $A$ is invertible; (2) the columns of $A$ are linearly independent; (3) the rows of $A$ are linearly independent; (4) $A$ has a left inverse; (5) $A$ has a right inverse; (6) the linear system $Ax = b$ has a unique solution for every $b$; (7) the homogeneous system $Ax = 0$ has only the trivial solution $x = 0$. The unifying reason these conditions are equivalent is that for a *square* matrix, having $n$ linearly independent columns means the columns form a basis of $\mathbb{R}^n$, so every $b$ can be uniquely expressed as $Ax$.

- **[[Thm - QR Factorization via Gram-Schmidt (Boyd)]]**
	- Let $A \in \mathbb{R}^{n \times k}$ be a matrix with linearly independent columns $a_1, \dots, a_k$ (which forces $n \geq k$). Then $A$ admits a **QR factorization** $A = QR$ where $Q \in \mathbb{R}^{n \times k}$ has orthonormal columns ($Q^T Q = I$) and $R \in \mathbb{R}^{k \times k}$ is upper triangular with positive diagonal entries. The columns of $Q$ are the Gram–Schmidt orthonormalisation of $a_1, \dots, a_k$, the diagonal entries of $R$ are the norms of the residual vectors $\tilde q_i$ in the Gram–Schmidt process, and the off-diagonal entries $R_{ij} = q_i^T a_j$ (for $i < j$) record the projection coefficients. The factorization is essentially unique once the sign convention $R_{ii} > 0$ is fixed.

- **[[Thm - Block Matrix Multiplication]]**
	- For compatible block matrices, the product is computed by the usual matrix-multiplication formula treating each block as an entry: $\begin{pmatrix} A & B \\ C & D \end{pmatrix}\begin{pmatrix} E & F \\ G & H \end{pmatrix} = \begin{pmatrix} AE + BG & AF + BH \\ CE + DG & CF + DH \end{pmatrix}$, provided the inner block dimensions match. The proof is direct from the definition of matrix multiplication. This is more than a notational convenience: it permits parallel and recursive algorithms (Strassen multiplication, divide-and-conquer matrix inversion), it underlies the Schur complement formula for inverting block matrices, and it lets one read off properties of compound systems from the structure of their blocks.

> [!tip] Unlocked: Markov Chains *(from Probability)*
> A discrete-time Markov chain on a finite state space is a linear dynamical system $p_{t+1} = P p_t$, where $p_t$ is the probability distribution at time $t$ and $P$ is the **transition matrix** with $P_{ij} = \Pr(\text{state } i \mid \text{previous state } j)$, columns summing to $1$. Boyd's linear dynamical system framework specialises to Markov chains by restricting $A$ to a *stochastic matrix*. Stationary distributions are eigenvectors with eigenvalue $1$.

> [!tip] Unlocked: Discrete Dynamical Systems *(from Dynamical Systems)*
> The behaviour of $x_{t+1} = Ax_t$ as $t \to \infty$ is entirely controlled by the **eigenvalues** of $A$: the trajectory decays to zero if all $|\lambda_i| < 1$, blows up if any $|\lambda_i| > 1$, and oscillates or grows polynomially in the boundary case $|\lambda_i| = 1$. The full theory of linear discrete dynamical systems — stable, unstable, and centre manifolds, fixed points, periodic orbits, normal forms — is the natural sequel to this chapter, accessible after [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|Linear Algebra V]] introduces eigenvalues.

- **[[Ex - Population dynamics matrix as a linear dynamical system]]** (⭐⭐)
	- Write down the matrix $A$ for the Boyd population model with birth-rate vector $b$ and death-rate vector $d$, verify that $x_{t+1} = A x_t$ correctly propagates the age distribution one year forward, and use the model to compute a one-step prediction from given data.

- **[[Ex - Existence of a left inverse forces linear independence of columns]]** (⭐)
	- Show that if an $m \times n$ matrix $A$ has a left inverse $C$ ($CA = I_n$), then the columns of $A$ are linearly independent, by combining linear-combination notation with the cancellation $C(Ax) = (CA)x = x$.

- **[[Ex - Pseudoinverse for least squares (Boyd)]]** (⭐⭐)
	- For an $m \times n$ matrix $A$ with $m \geq n$ and linearly independent columns, show that the **pseudoinverse** $A^\dagger = (A^T A)^{-1} A^T$ is a left inverse and that $\hat x = A^\dagger b$ minimises $\|Ax - b\|^2$ — converting the over-determined linear system $Ax = b$ into the closest possible approximate solution.

> [!note] Exercise Index — §X.4
> [[Exercise Index - §X.4 Dynamical Systems and Inverses]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

The exercises of an applied linear algebra topic fall into a small set of recurring goals. The most common is **set up a model**: given a phenomenon (a dataset, a network, a dynamical system), express it as $y = Ax + b$, $x_{t+1} = Ax_t$, or $Ax = b$ for explicit $A$, $b$, $x$. The skill here is in *recognising* which linear-algebra object encodes the phenomenon — a Boolean indicator becomes a $0/1$ vector, a network becomes an incidence matrix, a system that updates by a recurrence becomes a linear dynamical system. A second target is to **compute a numerical quantity** that is meaningful: a distance, an angle, a correlation coefficient, a Dirichlet energy, a trajectory at $t = 10$, a prediction from a regression model. A third is to **solve a system of linear equations** $Ax = b$ and identify whether the system is over-, under-, or exactly determined — because the answer chooses the algorithm. A fourth is to **verify a structural property**: that a matrix is invertible, that columns are linearly independent, that a set of vectors is a basis, that a function is linear or affine. A fifth, present only in the more theoretical exercises, is to **derive an inequality or equality** — Cauchy–Schwarz, the triangle inequality, the standard-deviation decomposition $\operatorname{rms}^2 = \operatorname{avg}^2 + \operatorname{std}^2$ — that turns out to be the bedrock of one of the modelling steps elsewhere. Each of these targets has a characteristic shape, and recognising it is half the battle.

**Sources — What assumptions do we usually leverage?**

The recurring sources are equally stereotyped. **Numerical data** — a vector, a matrix, an indexed list of vectors — is the rawest source, and it almost always wants to become an inner product, a norm, or a distance. **An affine relationship is hypothesised** — "the predicted price is a function of the features", "the temperature rise is a function of the loadings" — and this is the cue to introduce a regression model $\hat y = x^T \beta + v$ or a compliance matrix. **A graph or network is given** — vertices and edges, sources and sinks — and the incidence matrix is the standard encoding; once it is in hand, all subsequent questions become matrix–vector questions about that matrix. **A system updates by a recurrence** — the next-period value is a function of the current values — and if the recurrence is linear in the state then $x_{t+1} = A x_t + Bu_t$ captures it, and the spectrum of $A$ determines the long-time behaviour. **A function is given by a formula and one wants a linear approximation** — the Jacobian provides it, and the Taylor approximation makes the linearisation honest with an error term. The recurring move is to route a source to a target through one of these standard objects: data $\to$ vector $\to$ inner product $\to$ scalar invariant; network $\to$ incidence matrix $\to$ matrix–vector product $\to$ flow surplus or Dirichlet energy; recurrence $\to$ dynamics matrix $\to$ matrix power $\to$ long-time behaviour; nonlinear function $\to$ Jacobian at a point $\to$ affine approximation $\to$ linearised problem. Almost every exercise in this topic is a single edge of one of these routes.

---

# Legal Operations

The moves below are the assembly kit for problems in this topic. When stuck, scan the list and try each one in turn. Everything is self-contained: a reader with no prior linear algebra should be able to follow each operation from the description alone.

**Legal operations:**

1. **Encode a phenomenon as a vector or matrix.** Given a dataset, a network, a dynamical system, or a function, the very first step is to write it as a linear-algebraic object: a vector for one-dimensional data (Boolean indicators, time series, histograms, feature vectors), a matrix for two-dimensional data (images, document–term tables, asset returns over time), an incidence matrix for graphs, a dynamics matrix for recurrences. *Trigger:* any problem stated in words about a real-world phenomenon. *Pattern:* identify the natural indices ("one index per node, one index per time period, one index per feature") and write the object explicitly.

2. **Reduce a question to an inner product.** Inner products $a^T x$ compute weighted sums, projections, similarities, and linear functions all in the same notation. When a problem asks for a sum-with-weights, a dot product, a Boolean count, or the value of a linear function at a point, write it as $a^T x$ for an appropriate $a$. *Trigger:* "sum of selected entries", "weighted total", "feature value of a linear classifier". *Pattern:* "the answer is $a^T x$ where $a_i = \ldots$".

3. **Use Cauchy–Schwarz to bound an inner product.** The Cauchy–Schwarz inequality $|a^T b| \leq \|a\|\|b\|$ is the most-deployed inequality in this topic. It bounds the cross term $a^T b$ that appears when expanding $\|a + b\|^2$, it makes the cosine of an angle well-defined, and it caps the correlation coefficient at $\pm 1$. *Trigger:* any time a stray inner product appears in the middle of an estimate. *Pattern:* "by Cauchy–Schwarz, $|a^T b| \leq \|a\|\|b\|$, and this bound is tight when $a$ and $b$ are aligned".

4. **Expand a squared norm.** The identity $\|a + b\|^2 = \|a\|^2 + 2 a^T b + \|b\|^2$ converts norm questions into inner-product questions. It is the engine behind the triangle inequality, the parallelogram law $\|a + b\|^2 + \|a - b\|^2 = 2\|a\|^2 + 2\|b\|^2$, the decomposition $\operatorname{rms}^2 = \operatorname{avg}^2 + \operatorname{std}^2$, and the standard-deviation-of-sum formula. *Trigger:* a problem involving $\|a \pm b\|$ where direct calculation is unenlightening. *Pattern:* "expand $\|a + b\|^2$, use Cauchy–Schwarz on the cross term, take square roots".

5. **De-mean to extract variability.** Replacing $x$ by $\tilde x = x - \operatorname{avg}(x)\mathbf{1}$ removes the mean and leaves the fluctuation. This is the move that turns a question about absolute values into a question about deviations, separating "level" from "variation". *Trigger:* a problem about how much something varies, or about correlation. *Pattern:* "let $\tilde x = x - \operatorname{avg}(x)\mathbf{1}$; then $\operatorname{std}(x) = \|\tilde x\|/\sqrt n$ and the rest of the argument is about $\tilde x$".

6. **Recognise a Toeplitz / convolution structure.** Convolution $a \ast b$ shows up disguised as polynomial multiplication, moving averages, first differences, finite-impulse-response filters, and any matrix where each diagonal is constant. When such a matrix appears, treat it as convolution with an explicit kernel — most algorithms (and many identities, like $\mathbf{1}^T (a \ast b) = (\mathbf{1}^T a)(\mathbf{1}^T b)$) become trivial in that view. *Trigger:* a matrix whose entries depend only on $i - j$, or a sum of products with shifted indices.

7. **Build an incidence matrix and exploit flow conservation.** When a problem mentions a graph with edges carrying flows, write the $n \times m$ incidence matrix $A$ (with $\pm 1$ entries indicating edge direction). Then $Af$ is the net flow at each node, $A^T v$ is the potential difference across each edge, and the Dirichlet energy $\|A^T v\|^2$ measures roughness. *Trigger:* any graph problem with directional quantities. *Pattern:* "Build $A$, then the flow-conservation condition is $Af + s = 0$, a linear system in the unknown $f$".

8. **Iterate the dynamics matrix.** When the state of a system updates linearly each period, $x_{t+1} = Ax_t$, the trajectory is $x_{t+\ell} = A^\ell x_t$. The matrix power $A^\ell$ contains everything about the system's long-time behaviour, and for many applications (population projection, page-rank, paths in a graph) it is the explicit object to compute. *Trigger:* "what is the state in $\ell$ years?", "what is the asymptotic population/distribution?". *Pattern:* "the answer is $A^\ell x_0$; if $\ell$ is small, iterate directly; if $\ell$ is large, look at eigenvalues".

9. **Diagnose a linear system by counting equations and unknowns.** Given $Ax = b$ with $A \in \mathbb{R}^{m \times n}$, the very first question is whether $m > n$ (over-determined, may be unsolvable, look for least-squares solution via the pseudoinverse), $m = n$ (square, exactly one solution if $A$ is invertible), or $m < n$ (under-determined, infinitely many solutions if any). The algorithm follows. *Trigger:* any $Ax = b$. *Pattern:* "this is an $m \times n$ system with $m \;? \; n$, so use [QR / inverse / least-squares] to solve".

10. **Invoke linear independence to count and eliminate.** The columns of $A$ are linearly independent iff $Ax = 0 \Rightarrow x = 0$ iff $A$ has a left inverse iff (for square $A$) $A$ is invertible. This is the single most common structural-feasibility check in the topic: "can I solve $Ax = b$?", "is this a basis?", "does this matrix have an inverse?" all reduce to a linear-independence question.

**Illegal but tempting operations:**

> [!warning] 1. Treating an affine function as linear
> An affine function $f(x) = Ax + b$ with $b \neq 0$ satisfies superposition only on affine combinations ($\alpha + \beta = 1$), not on arbitrary linear combinations. Concretely: the regression model $\hat y(x) = x^T \beta + v$ does *not* satisfy $\hat y(\alpha x_1 + \beta x_2) = \alpha \hat y(x_1) + \beta \hat y(x_2)$ in general — try $x_1 = e_1$, $x_2 = 0$, $\alpha = \beta = 1$ to see the mismatch by $-v$. The repair: include a "constant feature" of $1$ at the start of every feature vector and absorb $v$ into the first coefficient, after which $\hat y(\tilde x) = \tilde x^T \tilde \beta$ is genuinely linear.

> [!warning] 2. Assuming $Ax = b$ has a solution because $A$ has more columns than rows
> An under-determined system $Ax = b$ ($m < n$) often has many solutions, but it can also have *zero* solutions if $b$ does not lie in the range of $A$. The standard counterexample is $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, $b = (1, 2)$: this is square, but the two rows are linearly dependent and $b$ is not a linear combination of the columns, so no solution exists. Solvability requires $b \in \operatorname{range}(A)$, not just $m \leq n$.

> [!warning] 3. Computing $(AB)C$ when $A(BC)$ is much cheaper (or vice versa)
> Matrix multiplication is associative, but the *flop count* depends drastically on the order. To compute $a b^T c$ where $a, b, c$ are $n$-vectors: forming $(ab^T)c$ first builds an $n \times n$ outer product ($n^2$ storage, $n^2$ flops) and then multiplies, costing $3n^2$ flops; forming $a(b^T c)$ first computes the scalar $b^T c$ ($2n$ flops) and then scales $a$, costing $3n$ flops. The order matters: for $n = 10^6$ the difference is $10^{12}$ versus $3 \times 10^6$ flops. The repair: always associate so the *intermediate* matrices stay small.

> [!warning] 4. Concluding $A$ is invertible from $\det(A) \neq 0$ in numerical work
> Mathematically, a square matrix is invertible iff its determinant is nonzero. Numerically, this is essentially useless: the determinant of an ill-conditioned matrix can be tiny but nonzero, and "tiny" depends on the scaling. The robust diagnostic is the **condition number** $\kappa(A) = \sigma_{\max}/\sigma_{\min}$ (the ratio of largest to smallest singular value): when $\kappa(A)$ is comparable to $1/\epsilon$ where $\epsilon$ is machine precision, the matrix is *numerically* singular, and solving $Ax = b$ is hopeless regardless of what $\det A$ says.

---

# Problem-Solving Strategy

The problems in this topic are won at the moment you recognise which of the standard objects encodes the question, so begin there. Almost every exercise is one of five types, and each type has a characteristic source pattern and a characteristic route to the answer.

If the problem **describes a real-world phenomenon and asks for a numerical quantity** — a total, an average, a distance, a similarity score — then the route is *encode then compute*. First identify the natural indices and write the data as a vector or matrix. Then express the requested quantity in vector–matrix notation: a weighted total is an inner product $w^T x$, a Euclidean distance is $\|x - y\|$, a similarity is the cosine of an angle. The compactness is the point: once the question is in vector form, computing it is mechanical, and you have also produced a *formula* that generalises to other inputs. A regression model price prediction, a portfolio's sector exposure, the RMS deviation of a forecast — all are inner products.

If the problem **gives you a function and asks for its best linear or affine approximation near a point**, the answer is the Taylor approximation $\hat f(x) = f(z) + Df(z)(x - z)$. The route runs: compute the gradient or Jacobian at $z$, write the affine function explicitly, verify that the approximation is exact at $z$. When the function is itself linear or affine the Taylor approximation equals the function, and this is sometimes the cleanest way to *prove* a function is affine — by showing it equals its own first-order Taylor expansion. Conversely, when a problem tells you that a function is "well approximated by an affine model", it is signalling that you should set up the affine model and treat it as exact for the purposes of the question.

If the problem **describes a graph or network**, the incidence matrix is almost certainly the right object. Write down the $n \times m$ matrix $A$ with $\pm 1$ entries; then flow conservation becomes the linear equation $Af + s = 0$, the Dirichlet energy of a node potential becomes $\|A^T v\|^2$, and the question of whether two graphs differ becomes the matrix-distance $\|A - B\|$. The incidence matrix is also the cleanest place to see the duality between flows (vectors indexed by edges) and potentials (vectors indexed by nodes): $A$ acts on edge data to give node data, and $A^T$ acts on node data to give edge data. Many graph problems are explicitly solvable once one realises that the answer is an entry, sum, or norm of $A f$ or $A^T v$ for some $f$ or $v$.

If the problem **gives a recurrence** — "next year's value is a linear function of this year's" — write $x_{t+1} = A x_t + B u_t$. The state $x_t$ should include everything the next state depends on; if the recurrence involves more than one previous time step, expand the state to include them ($K$-Markov $\to$ standard Markov on $\mathbb{R}^{nK}$). Once the linear-dynamical-system form is in hand, future trajectories are $x_{t+\ell} = A^\ell x_t$ when there is no input, or the inhomogeneous formula $x_{t+\ell} = A^\ell x_t + \sum_{j=0}^{\ell-1} A^{\ell - 1 - j} B u_{t+j}$ with an input. Equilibrium states satisfy $(I - A)z = c$ for the offset $c$, a linear system in $z$.

If the problem **gives a system of linear equations** $Ax = b$, the first question is the shape. If $A$ is *square and invertible*, the unique solution is $x = A^{-1} b$, computed in practice by QR factorization plus back-substitution rather than by literally forming the inverse. If $A$ is *tall* ($m > n$) and the columns are linearly independent, the system is over-determined and typically has no exact solution; the least-squares solution $\hat x = A^\dagger b = (A^T A)^{-1} A^T b$ minimises $\|Ax - b\|^2$ and is the right answer. If $A$ is *wide* ($m < n$) with rows linearly independent, the system is under-determined and has many solutions; the minimum-norm solution $\hat x = A^T (AA^T)^{-1} b$ is the canonical choice. These three regimes — over, square, under — correspond to the three pseudoinverse formulas and to three different practical algorithms. Choosing the right one first is non-negotiable.

The meta-strategy that unifies everything in this topic: **before computing, identify which of the four canonical objects you are working with** — a vector, a matrix, a linear dynamical system, or a system of linear equations. Each canonical object has a small palette of operations (norm, inner product, matrix–vector product, iteration, solve), and recognising the object is the same as recognising which operation to perform. The novice's mistake is to compute first; the experienced reader's habit is to *classify* first and then let the standard algorithm take over.

---

# Most Reusable Properties

- **[[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz]]**: $|a^T b| \leq \|a\|\|b\|$. The most-used inequality in applied mathematics. It bounds the cross term in $\|a + b\|^2$, it makes the angle between vectors well-defined, it caps correlation coefficients, and it provides the standard estimate $|f(x) - f(y)| \leq \|\beta\|\|x - y\|$ for a regression model with weight vector $\beta$. Whenever an inner product appears in the middle of an estimate, this is the first thing to reach for. **Typical use:** convert an unbounded cross term into a product of norms, then use known bounds on the norms.

- **The expansion $\|a + b\|^2 = \|a\|^2 + 2 a^T b + \|b\|^2$.** This is the only norm identity you actually need, and the engine behind the triangle inequality, the parallelogram law, the variance-decomposition $\operatorname{rms}^2 = \operatorname{avg}^2 + \operatorname{std}^2$, the standard-deviation-of-sum formula $\operatorname{std}(a + b)^2 = \operatorname{std}(a)^2 + 2\rho\operatorname{std}(a)\operatorname{std}(b) + \operatorname{std}(b)^2$, and the Pythagorean theorem when $a^T b = 0$. **Typical use:** any time you see a squared norm of a sum or difference; expand, then bound or simplify the cross term.

- **[[Thm - QR Factorization via Gram-Schmidt (Boyd)|QR factorization]] $A = QR$**. For any matrix with linearly independent columns, this gives an orthonormal basis $Q$ for the column space and an upper-triangular coordinate matrix $R$. Almost every algorithm for solving linear systems, computing least-squares, and finding eigenvalues runs through QR. **Typical use:** solve $Ax = b$ as $Rx = Q^T b$ by back-substitution; the upper-triangular structure makes the second step trivial.

- **The conditions for square-matrix invertibility (linearly independent columns $\Leftrightarrow$ linearly independent rows $\Leftrightarrow$ left-invertible $\Leftrightarrow$ right-invertible $\Leftrightarrow$ unique solution of $Ax = b$ for all $b$).** This single chain of equivalences turns every invertibility question into whichever form is easiest to check in the problem at hand. **Typical use:** prove a square matrix is invertible by exhibiting a left inverse, or refute invertibility by finding a nonzero $x$ with $Ax = 0$ — whichever is more convenient.

- **The pseudoinverse $A^\dagger = (A^T A)^{-1} A^T$ for tall full-column-rank $A$**. This is the canonical left inverse, and $\hat x = A^\dagger b$ is exactly the least-squares solution of $Ax = b$. It is the bridge from "over-determined system has no solution" to "find the closest-thing-to-a-solution" — the foundation of regression and data fitting. **Typical use:** any time an over-determined system is presented, reach for $A^\dagger$.

---

# Bridges

1. **The abstract linear algebra developed in LADR specialises here to $\mathbb{R}^n$ in the standard basis.** A vector space, in [[Def - Vector Space|the LADR sense]], is a set with addition and scalar multiplication satisfying eight axioms; $\mathbb{R}^n$ is the canonical example, and every finite-dimensional real vector space is isomorphic to some $\mathbb{R}^n$ once a basis is chosen. A [[Def - Linear Map|linear map]] $T : V \to W$ between abstract vector spaces specialises to a matrix $A \in \mathbb{R}^{m \times n}$ once bases of $V$ and $W$ are fixed; Boyd's $f(x) = Ax$ is the coordinate version of $T$. An [[Def - Inner Product Space|inner product space]] specialises to $\mathbb{R}^n$ with the standard $a^T b$; the [[Def - Norm Induced by an Inner Product|induced norm]] is $\|x\| = \sqrt{x^T x}$. The bridge is that *every theorem in Boyd is a theorem about a specific $V = \mathbb{R}^n$ with a specific basis*; the LADR-side proofs go through verbatim once one substitutes column vectors for abstract vectors. Conversely, the abstract LADR statements gain concreteness when one realises that they are saying exactly the same thing as Boyd's computational claims, but in a basis-free language.

2. **Taylor approximation is the total derivative as the best linear approximation.** The [[Def - The Total Derivative and Differentiability|total derivative]] of a function $f : \mathbb{R}^n \to \mathbb{R}^m$ at a point $z$ is the unique linear map $Df(z) : \mathbb{R}^n \to \mathbb{R}^m$ satisfying $\|f(z + h) - f(z) - Df(z) h\|/\|h\| \to 0$ as $h \to 0$. Boyd's Taylor approximation $\hat f(x) = f(z) + Df(z)(x - z)$ is exactly the affine function whose "linear part" is the total derivative. The Jacobian matrix is the matrix of $Df(z)$ in the standard basis. In multivariate analysis the total derivative is treated as a coordinate-free notion (an element of a space of linear maps); in Boyd it is a matrix of numerical partial derivatives. The connection is that the matrix–vector product $Df(z) h$ in Boyd's notation is precisely the evaluation of the abstract linear map on the displacement $h$.

3. **The incidence matrix is the bridge from linear algebra to graph theory.** For a directed graph $G = (V, E)$ with $n$ nodes and $m$ edges, the incidence matrix $A \in \mathbb{R}^{n \times m}$ records edge directions in a $\pm 1$ pattern. Three matrix-valued invariants of $G$ then appear: the **adjacency matrix** $\operatorname{Adj}(G)$ records which pairs of nodes are connected, and is *different* from the incidence matrix (a $\{0, 1\}$ matrix of size $n \times n$ rather than $n \times m$); the **graph Laplacian** $L = A A^T$ (with sign convention adjusted so that off-diagonals are nonpositive) has all-ones in its kernel for a connected graph and its second-smallest eigenvalue, the **Fiedler value**, measures graph connectivity; and the **cycle space** of $G$ is exactly the null space of $A$, with dimension equal to the cyclomatic number $m - n + (\text{components})$. Every fact in spectral graph theory — random-walk mixing times, expansion, chromatic number bounds, Cheeger inequalities — is ultimately a statement about $A$, $\operatorname{Adj}(G)$, or $L$.

4. **Convolution is multiplication by a Toeplitz matrix, and a circulant matrix when the inputs are periodic.** The convolution $a \ast b$ of two finite vectors can be written as $T(b) a$ where $T(b)$ is a Toeplitz matrix (each diagonal constant) whose columns are shifted copies of $b$ padded with zeros. When $a$ and $b$ are periodic (or one wraps the indices modulo $n$), $T(b)$ becomes a **circulant** matrix, which is diagonalised by the discrete Fourier transform — every circulant matrix's eigenvectors are the columns of the DFT matrix, and its eigenvalues are the DFT of its first column. This is the algebraic foundation of fast convolution via FFT, the basis of digital signal processing. In Boyd's matrix notation: $a \ast b = T(b) a$ in time $O(n^2)$, but the same product equals $F^{-1} \operatorname{diag}(Fb) F a$ in time $O(n \log n)$, where $F$ is the DFT matrix.

5. **The pseudoinverse $A^\dagger$ is the QR-derived solution of the least-squares problem.** For a tall full-rank $A$, the pseudoinverse can be computed via $A^\dagger = R^{-1} Q^T$ where $A = QR$ is the QR factorization: $\hat x = R^{-1} Q^T b$ minimises $\|Ax - b\|^2$. This is much more numerically stable than $A^\dagger = (A^T A)^{-1} A^T$, which involves the explicit Gram matrix $A^T A$ whose condition number is the *square* of $A$'s. The bridge is that QR + back-substitution is the practical algorithm for least-squares, even though the pseudoinverse formula is the cleaner conceptual statement. This is the foundation of [[Linear Algebra XI — Applied II — Least Squares|Boyd's Part III]] on least-squares.

---

# Insights

**The unifying frame: model, encode, solve, interpret.** Every problem in this topic is an instance of a four-step pattern. First, model the real-world phenomenon — what changes over time, what depends on what, what is observed and what is to be predicted. Second, encode the model as a linear-algebraic object — a vector, a matrix, a linear dynamical system, or a linear system of equations. Third, solve the resulting linear-algebra problem using a standard algorithm — inner product, matrix–vector multiplication, iteration, QR factorization, back-substitution. Fourth, interpret the numerical answer back in the language of the original phenomenon. The applied-linear-algebra reader's working memory should contain a small library of *(phenomenon, object)* pairs: time series $\to$ vector, network $\to$ incidence matrix, dynamical system $\to$ dynamics matrix, model $\to$ regression matrix, dataset $\to$ feature matrix, function $\to$ Jacobian. The skill is in recognising the pair, not in computing once it is fixed.

**The true name of "linear" is "preserves arbitrary linear combinations", but the true name of "affine" is "preserves affine combinations".** The distinction matters because applied modelling overwhelmingly produces affine functions, not linear ones: regression has an intercept, prices have a level, dynamics have an offset, Taylor expansion has a constant term. The standard trick of absorbing the constant by adding a "constant feature" $1$ to the input vector makes the affine function linear in the enlarged input — and this trick is so universal that it should be a reflex. Once you internalise that "linear after prepending $1$" is the practical meaning of "affine", many otherwise-ugly formulas become clean inner products.

**Trigger-reaction patterns for this topic.** *"Have a dataset"* $\to$ look for a linear or affine model first; the regression model $\hat y = x^T \beta + v$ is the default starting point and at minimum gives a baseline against which more sophisticated models can be compared. *"See a discrete dynamical system"* $\to$ write it as $x_{t+1} = A x_t + B u_t$ and study $A$'s spectrum; the long-time behaviour is determined entirely by $A$'s eigenvalues, even if you cannot diagonalise. *"See a system of linear equations $Ax = b$"* $\to$ classify by shape (over-, under-, exactly-determined) and use the corresponding algorithm (least-squares, minimum-norm, back-substitution); the classification is non-negotiable. *"See a network"* $\to$ build the incidence matrix; everything else flows from it. *"See a convolution or moving average or filter"* $\to$ remember it is matrix-multiplication by a Toeplitz matrix, and use FFT if you need it to be fast. *"See a sum-of-squared-errors objective"* $\to$ it is a squared-norm $\|Ax - b\|^2$, minimised by the pseudoinverse.

**$k$-means as alternating optimisation.** The $k$-means algorithm is the simplest non-trivial example of an *alternating-optimisation* algorithm: an objective $J(c, z)$ in two coupled variables is hard to minimise jointly, but easy to minimise in each variable with the other fixed. Alternating these two minimisations produces a sequence of objective values that decreases monotonically, so the algorithm converges (to a local minimum, not necessarily the global one). Once the pattern is named, it is everywhere: the Expectation–Maximisation algorithm in statistics, coordinate descent in optimisation, Gauss–Seidel iteration in numerical linear algebra, two-block ADMM in convex optimisation. The lesson of $k$-means is that *when the objective decomposes into two convex sub-problems coupled by a hard discrete choice, alternating them is the default algorithm*, even when no clean convergence theory promises a global optimum.

**Affine vs. linear is a translation, and almost every result has an affine version.** A linear function passes through the origin; an affine one does not, but only by an additive constant. Almost every theorem about linear functions has a one-line affine analogue: superposition becomes affine superposition (with coefficients summing to $1$); the matrix representation $f(x) = Ax$ becomes $f(x) = Ax + b$; the kernel of a linear function becomes an affine subspace (a translate of a subspace); the eigenvalue equation $Ax = \lambda x$ becomes a fixed-point equation $Ax + b = x$. Memorising the linear theorems is enough as long as you carry the "plus translation" mental footnote — and this is what makes the Boyd-Vandenberghe style so practical, because real models almost always have a translation.

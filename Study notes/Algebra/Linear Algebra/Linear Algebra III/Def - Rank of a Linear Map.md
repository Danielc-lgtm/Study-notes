---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Null Space and Range"
  - "Def - Matrix of a Linear Map"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $T \in \mathcal{L}(V, W)$ is a linear map with $V$ finite-dimensional, and $A \in \mathbf{F}^{m, n}$ is a matrix. The **rank** of $T$ is denoted $\operatorname{rank} T$ or $\dim \operatorname{range} T$; the **rank** of $A$ is denoted $\operatorname{rank} A$. The **nullity** is $\dim \operatorname{null} T$. Full notation on [[Linear Algebra III — §3A–D Linear Maps]].

This is a compound page: it defines three interlocking notions — **rank of a linear map**, **rank of a matrix**, and **column rank vs. row rank** — because the theorem "column rank equals row rank" is what makes "the rank" a single well-defined number, and one cannot prove rank–nullity cleanly without all three.

---

# Axiom Motivation

The rank of a linear map is the answer to the most basic question: **how big is the actual output?** A linear map $T : V \to W$ has its output set $\operatorname{range} T \subseteq W$, and this is a subspace; its dimension is the rank. Rank is the cleanest single-number summary of "what $T$ does" — it measures the *effective dimension* of the operation, ignoring whatever happens inside the null space.

Why a *single number* and not the whole range subspace? Two reasons. First, the dimension is what one can manipulate algebraically: dimensions add, the inequality $\operatorname{rank}(ST) \leq \min\{\operatorname{rank} S, \operatorname{rank} T\}$ becomes a numerical bound, and conservation laws like [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] connect ranks to other dimensions. Second, the rank is a *basis-free invariant* of $T$: it does not depend on any choice of basis in $V$ or $W$. The range itself is a subspace of $W$, and its identity-as-a-set depends on $W$'s structure; but its dimension is a single integer attached to $T$ alone.

For matrices, the question is more delicate. Given a matrix $A \in \mathbf{F}^{m, n}$, there are *two* obvious things to call "rank":

- **Column rank** = $\dim \operatorname{span}(A_{\cdot, 1}, \ldots, A_{\cdot, n})$, the dimension of the column span in $\mathbf{F}^{m, 1}$. This is the rank of the linear map $\mathbf{F}^n \to \mathbf{F}^m$, $x \mapsto Ax$, in the standard bases.
- **Row rank** = $\dim \operatorname{span}(A_{1, \cdot}, \ldots, A_{m, \cdot})$, the dimension of the row span in $\mathbf{F}^{1, n}$. This is the rank of the transpose map.

A priori these two numbers could differ. They are dimensions of subspaces of completely different ambient spaces ($\mathbf{F}^m$ versus $\mathbf{F}^n$). The non-trivial theorem $3.57$ in LADR — that the column rank equals the row rank — collapses the distinction and lets us call the common value simply the **rank** of $A$. The proof is short but beautiful: it factors $A = CR$ with $C \in \mathbf{F}^{m, c}$, $R \in \mathbf{F}^{c, n}$, where $c$ is the column rank; the columns of $C$ are a basis of the column space. Then every row of $A$ is a linear combination of the $c$ rows of $R$, so the row rank is at most $c$. The same argument applied to $A^T$ gives the reverse inequality.

This collapse is the structural reason rank–nullity is **symmetric in domain and codomain**. The dimension formula

$$\dim V \;=\; \dim \operatorname{null} T + \dim \operatorname{range} T$$

uses the dimension of the *range*, which is the column rank of $\mathcal{M}(T)$. The dual formula for the dual map would use the row rank. Because column rank equals row rank, the dimension of the range equals the dimension of the range of the dual map, and the two rank–nullity statements (for $T$ and for $T^*$) collapse to a single fact about the rank of $T$. The seemingly-asymmetric formula has a hidden symmetry.

A further motivation: rank measures the **information content** of a linear map. A rank-$r$ linear map is determined by $r$ "independent pieces" — its action on $r$ basis vectors of a complement of $\operatorname{null} T$ determines everything. From a data-compression standpoint, a rank-$r$ matrix $A \in \mathbf{F}^{m, n}$ can be stored using $r(m + n)$ entries (via the column-row factorisation $A = CR$) instead of $mn$, a huge saving when $r \ll \min(m, n)$. This perspective drives the **low-rank approximation** problem in numerical linear algebra and applied data analysis, and underlies the **singular value decomposition** (see [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]).

---

# The Definition

Let $T \in \mathcal{L}(V, W)$ be a linear map with $V$ finite-dimensional, and let $A \in \mathbf{F}^{m, n}$ be a matrix over a field $\mathbf{F}$.

**Rank of a linear map.** The **rank** of $T$ is
$$\operatorname{rank} T \;:=\; \dim \operatorname{range} T.$$
The **nullity** of $T$ is $\dim \operatorname{null} T$.

**Column rank of a matrix.** The **column rank** of $A$ is the dimension of the span of the columns of $A$:
$$\text{column rank of } A \;:=\; \dim \operatorname{span}(A_{\cdot, 1},\, A_{\cdot, 2},\, \ldots,\, A_{\cdot, n}) \;\subseteq\; \mathbf{F}^{m, 1}.$$

**Row rank of a matrix.** The **row rank** of $A$ is the dimension of the span of the rows of $A$:
$$\text{row rank of } A \;:=\; \dim \operatorname{span}(A_{1, \cdot},\, A_{2, \cdot},\, \ldots,\, A_{m, \cdot}) \;\subseteq\; \mathbf{F}^{1, n}.$$

**Theorem (column rank equals row rank).** For every matrix $A \in \mathbf{F}^{m, n}$, the column rank and row rank are equal. Their common value is the **rank** of $A$, denoted $\operatorname{rank} A$.

**Linking the two.** For $T \in \mathcal{L}(V, W)$ and any choice of bases of $V$ and $W$,
$$\operatorname{rank} T \;=\; \dim \operatorname{range} T \;=\; \operatorname{rank} \mathcal{M}(T).$$
So the rank of a linear map equals the rank of its matrix in any choice of bases — making rank a well-defined invariant of the map alone.

---

# Categorical / Structural Definition

The rank of a linear map is the **dimension of its image** in the categorical sense — the rank is the size of the **image factorisation** $V \twoheadrightarrow V / \operatorname{null} T \xrightarrow{\sim} \operatorname{range} T \hookrightarrow W$. The middle isomorphism, the first isomorphism theorem for vector spaces, identifies the rank with $\dim(V / \operatorname{null} T) = \dim V - \dim \operatorname{null} T$ — exactly [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]].

In the category of finite-dimensional vector spaces, every linear map $T : V \to W$ factors uniquely as $\pi$ (surjective) followed by $\iota$ (injective): $V \xrightarrow{\pi} \operatorname{range} T \xrightarrow{\iota} W$. The rank is the dimension of the intermediate space. Two linear maps of the same rank are related by an isomorphism on the intermediate space — they "have the same image structure" up to relabelling.

For the matrix viewpoint: a matrix $A \in \mathbf{F}^{m, n}$ factors as $A = CR$ with $C \in \mathbf{F}^{m, r}$ and $R \in \mathbf{F}^{r, n}$ exactly when $\operatorname{rank} A \leq r$ — the **column-row factorisation**. The minimum such $r$ is the rank. Equivalently, $A$ has rank $\leq r$ iff $A$ is a sum of $r$ rank-$1$ matrices, each of the form $\mathbf{c} \mathbf{r}^T$ for a column $\mathbf{c}$ and a row $\mathbf{r}$. The set of rank-$\leq r$ matrices is an algebraic variety of dimension $r(m + n - r)$ in $\mathbf{F}^{m, n}$ — the **determinantal variety** — and is a fundamental object in algebraic geometry.

---

# Relate to Other Fields / Compression

**True name:** "rank is the size of the actual content" — the dimension of what the operator actually produces, ignoring the redundancy in the input (null space). Two linear maps with the same rank are operationally equivalent up to a relabelling of input and output.

In **graph theory**, the rank of the incidence matrix or the adjacency matrix encodes structural properties: for an undirected graph on $n$ vertices, the rank of the **Laplacian matrix** is $n - c$ where $c$ is the number of connected components — a dimensional count of "how independent the structure is".

In **statistics**, the rank of a data matrix is the effective dimensionality of the data. **Principal component analysis** seeks the best low-rank approximation of a data matrix; the rank of the residual measures how much variance is captured. This is the bridge to the **singular value decomposition** (see [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]).

In **algebraic geometry**, the rank of a coherent sheaf at a point measures its "thickness" there; the set of points where the rank is at least $r$ is an algebraic subvariety. For a vector bundle on a manifold, the rank is a constant (the dimension of each fibre) — the same number that we would call "the rank" of the bundle.

In **representation theory**, the dimension of a representation $\rho : G \to \operatorname{GL}(V)$ — equivalently, the rank of $V$ as a $G$-module — is a basic invariant; irreducible representations of a finite group $G$ have dimensions summing in a specific way (the sum of squares equals $|G|$).

In **functional analysis**, the **finite-rank operators** on a Banach space — those with finite-dimensional range — are the cleanest infinite-dimensional analogues of matrices, and they are dense in the compact operators (in the operator norm). The Fredholm alternative says that a compact perturbation of the identity behaves "like a finite-dimensional operator" for the purposes of rank–nullity-like results, despite the spaces being infinite-dimensional.

---

# Examples / Corollaries

**Example: zero map.** $T = 0 : V \to W$ has $\operatorname{rank} T = 0$. The zero matrix has rank $0$.

**Example: identity operator.** $I : V \to V$ has $\operatorname{rank} I = \dim V$. The identity matrix $I_n$ has rank $n$ — full rank.

**Example: rank-$1$ matrix.** $A = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \begin{pmatrix} 3 & 4 \end{pmatrix} = \begin{pmatrix} 3 & 4 \\ 6 & 8 \end{pmatrix}$. Both columns are multiples of $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$, so column rank is $1$. Both rows are multiples of $\begin{pmatrix} 3 & 4 \end{pmatrix}$, so row rank is $1$. The rank is $1$. In general, rank-$1$ matrices are exactly the nonzero outer products $\mathbf{c} \mathbf{r}^T$.

**Example: a $2$-by-$4$ matrix.** $A = \begin{pmatrix} 4 & 7 & 1 & 8 \\ 3 & 5 & 2 & 9 \end{pmatrix}$. The first two columns are not parallel, so they span a $2$-dimensional subspace of $\mathbf{F}^{2, 1}$; the dimension cannot exceed $2 = \dim \mathbf{F}^{2, 1}$, so column rank is $2$. The two rows are not parallel in $\mathbf{F}^{1, 4}$, so row rank is $2$. Rank is $2$ — full row rank.

**Example: differentiation on $\mathcal{P}_3$.** $D : \mathcal{P}_3(\mathbb{R}) \to \mathcal{P}_2(\mathbb{R})$ has $\dim \operatorname{range} D = 3$ (every polynomial of degree $\leq 2$ has an antiderivative in $\mathcal{P}_3$), and $\dim \operatorname{null} D = 1$ (only constants are killed). Rank–nullity: $4 = 1 + 3$.

**Example: a singular matrix.** $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$. The second column is twice the first, so column rank is $1$. The second row is twice the first, so row rank is $1$. Rank is $1$. This matrix is *singular* (not invertible) — square matrices are invertible exactly when full rank.

**Non-example (rank is not size).** A $3$-by-$3$ matrix can have any rank from $0$ to $3$. A common misconception is that the rank is "the size of the matrix" — but the rank measures *content*, not *shape*.

**Corollary (rank bound by dimensions).** For $T \in \mathcal{L}(V, W)$ with $V, W$ finite-dimensional, $\operatorname{rank} T \leq \min\{\dim V, \dim W\}$. The bound by $\dim V$ comes from rank–nullity ($\operatorname{rank} T \leq \dim V$); the bound by $\dim W$ comes from $\operatorname{range} T \subseteq W$.

**Corollary (rank of a product).** $\operatorname{rank}(ST) \leq \min\{\operatorname{rank} S, \operatorname{rank} T\}$. The image of $ST$ is contained in the image of $S$, giving the first bound; and the image of $ST$ is $S$ applied to the image of $T$, so its dimension is at most the dimension of the image of $T$, giving the second. See [[Ex - Rank of a product is bounded by individual ranks]].

**Corollary (full-rank square matrix is invertible).** A square matrix $A \in \mathbf{F}^{n, n}$ is invertible iff $\operatorname{rank} A = n$. Proof via rank–nullity: $\operatorname{rank} A = n$ iff $\dim \operatorname{null} A = 0$ iff $A$ is injective iff $A$ is invertible (by [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]]).

**Corollary (rank under invertible left/right multiplication).** If $E_1, E_2$ are invertible square matrices of compatible sizes, then $\operatorname{rank}(E_1 A) = \operatorname{rank}(A E_2) = \operatorname{rank}(E_1 A E_2) = \operatorname{rank} A$. Multiplying by an invertible matrix is the same as a change of basis on one side — see [[Thm - Change of Basis Formula]] — and rank is basis-independent.

**Corollary (column rank = row rank, sketch).** Let $c$ = column rank of $A$. By the column-row factorisation, $A = CR$ for some $C \in \mathbf{F}^{m, c}$ and $R \in \mathbf{F}^{c, n}$. The rows of $A$ are linear combinations of the $c$ rows of $R$ (by the row-wise view of matrix multiplication), so row rank $\leq c$. Applying the same argument to $A^T$ (whose column rank is the row rank of $A$, and vice versa) gives column rank $\leq$ row rank. Combining, the two are equal.

**Calibration check.** A reader who has understood the definitions should be able to verify, in under a minute each: (1) the rank of the $2$-by-$2$ matrix $\begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix}$ is $1$ (the second row is $3$ times the first); (2) the rank of the $3$-by-$3$ identity matrix is $3$; (3) the rank of a matrix is the same as the rank of its transpose.

---

# Unlocked by This

> [!tip] Fundamental Theorem of Linear Maps *(in §3B)*
> The whole conservation law $\dim V = \dim \operatorname{null} T + \operatorname{rank} T$ is the central theorem of the chapter, and rank is the natural object on the right-hand side. See [[Thm - Fundamental Theorem of Linear Maps]].

> [!tip] Singular Value Decomposition *(from Linear Algebra VII)*
> The **singular values** of a matrix $A$ are the non-negative square roots of the eigenvalues of $A^* A$; the number of nonzero singular values is the rank of $A$. The SVD provides the **best low-rank approximation** to a matrix (in operator norm and in Frobenius norm — the Eckart–Young theorem), which is the workhorse of modern data science, image compression, and recommendation systems. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]].

> [!tip] Determinantal Variety *(from Algebraic Geometry)*
> The set of $m$-by-$n$ matrices of rank at most $r$ is an irreducible algebraic variety, cut out by the vanishing of all $(r+1)$-by-$(r+1)$ minors. Its dimension is $r(m + n - r)$. **Determinantal varieties** are central objects in classical algebraic geometry, and they explain why rank conditions appear so naturally in geometric problems.

> [!tip] Bias-Variance and Effective Degrees of Freedom *(from Statistics)*
> In statistical model fitting, the rank of the **design matrix** measures the effective number of free parameters. Low-rank approximations underlie **principal component regression**, **ridge regression** (where the effective rank decreases as the regularisation increases), and the entire bias-variance tradeoff. See [[Linear Algebra XI — Applied II — Least Squares]].

---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Matrix of a Linear Map"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $F = \mathbb{R}$ or $\mathbb{C}$, $T \in \mathcal{L}(V)$ an operator, $v_1, \ldots, v_n$ a basis of $V$, and $A = \mathcal{M}(T, (v_1, \ldots, v_n))$ the matrix of $T$ in this basis with entries $A_{j,k}$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---

# Statement

> **Definition (Gershgorin Disks).** Let $T \in \mathcal{L}(V)$ have matrix $A$ in some basis. For each $j \in \{1, \ldots, n\}$, the **$j$th Gershgorin disk** of $T$ with respect to this basis is the closed disk
> $$D_j = \left\{ z \in F : |z - A_{j,j}| \leq \sum_{k \neq j} |A_{j,k}| \right\}.$$
> Equivalently, $D_j$ is the closed disk centred at the $j$th diagonal entry with radius equal to the sum of absolute values of the off-diagonal entries in row $j$.

> **Theorem (Gershgorin Disk Theorem).** Every eigenvalue of $T$ is contained in some Gershgorin disk $D_j$ with respect to the basis $v_1, \ldots, v_n$. That is,
> $$\sigma(T) \subseteq D_1 \cup D_2 \cup \cdots \cup D_n.$$

> **Corollary (Diagonally dominant matrices are invertible).** If for every $j$, $|A_{j,j}| > \sum_{k \neq j}|A_{j,k}|$ — the matrix is **strictly diagonally dominant** — then no Gershgorin disk contains $0$, so $0$ is not an eigenvalue, so $T$ is invertible.

---

# Motivation

Gershgorin's theorem is the **cheapest non-trivial eigenvalue estimate** in linear algebra: it gives a region in the complex plane containing all eigenvalues, with the region computed directly from the matrix entries in any basis. No characteristic polynomial, no iterative computation — just look at the diagonal entries and the row sums.

The result is *qualitative* in nature: it does not pin down eigenvalues, it just localises them. But the localisation is often enough. If you want to show an operator is invertible, you do not need to find its eigenvalues — you just need to show $0$ is not an eigenvalue, which (by the contrapositive of the disk theorem) you can do by showing $0$ is in none of the Gershgorin disks. This is the **diagonal dominance** criterion: an operator with much larger diagonal entries than off-diagonal entries is invertible.

The theorem is the foundation of many practical results:
- **Strictly diagonally dominant matrices are invertible** (immediate from the disk theorem and the corollary).
- **The spectrum of a perturbed operator stays close to the spectrum of the unperturbed one** (if you add a small matrix to $T$, the Gershgorin disks barely move).
- **Real symmetric matrices with positive diagonal and small off-diagonal entries are positive definite** (the disks lie in the positive half-plane).
- **Convergence of iterative methods for solving $Ax = b$** (Jacobi, Gauss-Seidel) uses Gershgorin to bound the spectral radius of the iteration matrix.

The theorem is *basis-dependent*: changing basis changes the disks, and a good basis can give much sharper localisation. The Schur basis (which makes the matrix upper triangular) reduces every Gershgorin disk to a single point — the corresponding diagonal entry, which is the eigenvalue. So the Gershgorin disks are *upper bounds* on where the eigenvalues can be, and the bound can be tightened by basis choice.

A nice intuition: the disks are "fuzzy versions" of the diagonal entries. In an upper-triangular matrix the diagonal entries are exactly the eigenvalues; in a not-necessarily-upper-triangular matrix the diagonal entries are still an approximation, and the disks measure how far off the eigenvalues can be from this approximation.

---

# Sources and Targets

**Sources (Input Broadening)**

The first disguised source is **an operator presented as a matrix in an explicit basis**. This is the default setting in numerical linear algebra. The Gershgorin disks are *immediate* to compute — no factoring, no iterations. *Example problem:* "Show that the matrix $\begin{pmatrix} 5 & 0.1 \\ 0.2 & 4 \end{pmatrix}$ is invertible." Gershgorin disks: $\{|z - 5| \leq 0.1\}$ and $\{|z - 4| \leq 0.2\}$, neither contains $0$, so $T$ is invertible.

The second disguised source is **a perturbation $A + \varepsilon B$ of a diagonal matrix $A$**. The Gershgorin disks of $A + \varepsilon B$ are small perturbations of the singleton disks of $A$, so the eigenvalues of $A + \varepsilon B$ are close to the diagonal entries of $A$. *Example problem:* "The eigenvalues of a nearly-diagonal matrix are close to its diagonal entries." Disguised source: small off-diagonal entries means small Gershgorin radii.

The third disguised source is **a diagonally dominant matrix arising in PDE discretisation or graph theory**. The discrete Laplacian on a graph and the discretisation of elliptic operators both produce strictly diagonally dominant matrices in suitable bases, and Gershgorin gives their invertibility for free. *Example problem:* "Show that the discretisation matrix of the Poisson equation $-\Delta u = f$ with Dirichlet boundary conditions on a uniform grid is invertible." Disguised source: the matrix is strictly diagonally dominant by construction.

**Targets (Output Amplification)**

Combined with **continuity of eigenvalues as functions of matrix entries**, the theorem amplifies to: *small perturbations of a matrix move the eigenvalues by amounts bounded by the Gershgorin radii*. This is the **Bauer-Fike theorem** in its rough form.

Combined with **the fact that the union of disjoint Gershgorin disks separates the eigenvalues**, the theorem amplifies to: *if the disks split into disjoint groups, the eigenvalues split correspondingly (counted with multiplicity)*. Specifically, if $D_1 \cup D_2 \cup \cdots \cup D_k$ is disjoint from $D_{k+1} \cup \cdots \cup D_n$, then exactly $k$ eigenvalues lie in the first union and the remaining $n - k$ in the second.

Combined with **a column version of the theorem**, the eigenvalues are also in the union of disks centered at the diagonal entries with radii given by the *column* off-diagonal sums (not just row). The intersection of the two unions is often tighter than either alone.

---

# Why Is It True

The mechanism is **the "largest coefficient picks out the diagonal entry it lives near"**: write an eigenvector $w$ in the basis as $w = c_1 v_1 + \cdots + c_n v_n$; the largest coefficient $|c_j|$ comes from a row $j$ whose action on $w$ produces a relation in which $A_{j,j}$ plays a privileged role.

Explicitly: $Tw = \lambda w$ becomes, in the basis,
$$\sum_k A_{j,k} c_k = \lambda c_j \quad \text{for each } j.$$
Rearranging:
$$(\lambda - A_{j,j}) c_j = \sum_{k \neq j} A_{j,k} c_k.$$
If $j$ is the index where $|c_j|$ is maximal (say $|c_j| = \max_i |c_i|$, which is positive since $w \neq 0$), then taking absolute values:
$$|\lambda - A_{j,j}| \cdot |c_j| = \left| \sum_{k \neq j} A_{j,k} c_k \right| \leq \sum_{k \neq j} |A_{j,k}| \cdot |c_k| \leq \sum_{k \neq j} |A_{j,k}| \cdot |c_j|.$$
Dividing by $|c_j| > 0$:
$$|\lambda - A_{j,j}| \leq \sum_{k \neq j} |A_{j,k}|,$$
which is exactly the condition $\lambda \in D_j$.

> **The mechanism in one sentence: the eigenvector's largest coordinate sits in a row where the diagonal entry contributes most to the eigenvalue equation; the rest of the row contributes at most its absolute-value sum.**

The key step is the **triangle inequality** combined with the choice of $j$ to maximise $|c_j|$. The choice is what makes the bound $|c_k| \leq |c_j|$ uniform across $k$.

---

# What Makes This Hard

The non-obvious step is the **choice of the index $j$ — the one with the largest eigenvector coefficient**. Beginners try to use the diagonal entry on each row equally; the argument only works for the *maximum* row index. The other common slip is forgetting that the radius involves the *off-diagonal* entries of the row, not including the diagonal entry itself. The theorem is "diagonal-centric" and the proof is "max-coefficient-centric"; lining these up correctly requires care.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Write an eigenvector in the basis; identify the index $j$ with the largest coefficient; expand the eigenvalue equation in coordinates and isolate the term $(\lambda - A_{j,j}) c_j$; use the triangle inequality.

**Subgoal decomposition:**

1. **Set up the eigenvalue equation in coordinates.** Write $w = c_1 v_1 + \cdots + c_n v_n$ with $w \neq 0$ an eigenvector for $\lambda$. The equation $Tw = \lambda w$ becomes $\sum_k A_{j,k} c_k = \lambda c_j$ for each $j$.
   - *Hint:* expand $Tw = \sum_k c_k T v_k = \sum_k c_k \sum_j A_{j,k} v_j = \sum_j (\sum_k A_{j,k} c_k) v_j$ and compare with $\lambda w = \sum_j \lambda c_j v_j$.
   - *Why needed:* gives the coordinate equation that drives the rest.

2. **Pick $j$ with $|c_j|$ maximal.** Since $w \neq 0$, some $|c_j| > 0$; let $j$ be the index achieving the maximum.
   - *Hint:* there are finitely many coefficients, so the max is achieved.
   - *Why needed:* makes the inequality $|c_k| \leq |c_j|$ uniform.

3. **Isolate $(\lambda - A_{j,j}) c_j$.** Move the diagonal term to the left and the off-diagonal terms to the right:
$$(\lambda - A_{j,j}) c_j = \sum_{k \neq j} A_{j,k} c_k.$$
   - *Hint:* rearrange the $j$th coordinate equation.
   - *Why needed:* puts the bound in Gershgorin form.

4. **Apply triangle inequality and bound.** Take absolute values:
$$|\lambda - A_{j,j}| \cdot |c_j| \leq \sum_{k \neq j}|A_{j,k}| \cdot |c_k| \leq \sum_{k \neq j}|A_{j,k}| \cdot |c_j|.$$
Divide by $|c_j| > 0$.
   - *Hint:* triangle inequality for the sum, then $|c_k| \leq |c_j|$ for each $k$ in the sum.
   - *Why needed:* yields the Gershgorin inequality $|\lambda - A_{j,j}| \leq \sum_{k \neq j}|A_{j,k}|$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The matrix of $T$ in basis $v_1, \ldots, v_n$ gives $T v_k = \sum_j A_{j,k} v_j$, hence $Tw = \sum_j (\sum_k A_{j,k} c_k) v_j$ for $w = \sum_k c_k v_k$
> **Statement:** Let $T$ have matrix $A$ in a basis $v_1, \ldots, v_n$. For any $w = \sum_k c_k v_k$, the coordinates of $Tw$ in the basis are $(Tw)_j = \sum_k A_{j,k} c_k$.
>
> **Hint:** by definition of matrix-of-linear-map, $T v_k = \sum_j A_{j,k} v_j$; sum over $k$ with coefficients $c_k$.
>
> **Why needed:** rewrites the operator equation $Tw = \lambda w$ in matrix-coordinate form.
>
> > [!note]- Full proof
> > By definition of the matrix $A = \mathcal{M}(T, (v_1, \ldots, v_n))$, $T v_k = \sum_j A_{j,k} v_j$ for each $k$. Linearity:
> > $$T w = T \sum_k c_k v_k = \sum_k c_k T v_k = \sum_k c_k \sum_j A_{j,k} v_j = \sum_j \left(\sum_k A_{j,k} c_k\right) v_j.$$
> > So the $j$th coordinate of $Tw$ is $\sum_k A_{j,k} c_k$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $T \in \mathcal{L}(V)$ have matrix $A$ in the basis $v_1, \ldots, v_n$, and let $\lambda \in F$ be an eigenvalue of $T$ with eigenvector $w \neq 0$.
>
> **Step 1 — coordinate form of the eigenvalue equation.** Write $w = c_1 v_1 + c_2 v_2 + \cdots + c_n v_n$ for some $c_1, \ldots, c_n \in F$, not all zero. By Lemma 1, $Tw$ has $j$th coordinate $\sum_k A_{j,k} c_k$, and the eigenvalue equation $Tw = \lambda w$ has $j$th coordinate equation
> $$\sum_{k=1}^{n} A_{j,k} c_k = \lambda c_j \qquad \text{for each } j \in \{1, \ldots, n\}.$$
>
> **Step 2 — pick $j$ with maximal $|c_j|$.** Since $w \neq 0$, at least one $c_i$ is nonzero, so $\max_i |c_i| > 0$. Let $j \in \{1, \ldots, n\}$ be an index where this max is achieved:
> $$|c_j| = \max_{i \in \{1, \ldots, n\}} |c_i| > 0.$$
>
> **Step 3 — rearrange to isolate $A_{j,j} c_j$.** From the $j$th coordinate equation:
> $$\lambda c_j = A_{j,j} c_j + \sum_{k \neq j} A_{j,k} c_k,$$
> so
> $$(\lambda - A_{j,j}) c_j = \sum_{k \neq j} A_{j,k} c_k.$$
>
> **Step 4 — triangle inequality.** Take absolute values:
> $$|\lambda - A_{j,j}| \cdot |c_j| = \left| \sum_{k \neq j} A_{j,k} c_k \right| \leq \sum_{k \neq j} |A_{j,k}| \cdot |c_k|.$$
> By the choice of $j$, $|c_k| \leq |c_j|$ for every $k$, so:
> $$\sum_{k \neq j} |A_{j,k}| \cdot |c_k| \leq \sum_{k \neq j} |A_{j,k}| \cdot |c_j| = |c_j| \sum_{k \neq j} |A_{j,k}|.$$
> Combining:
> $$|\lambda - A_{j,j}| \cdot |c_j| \leq |c_j| \sum_{k \neq j} |A_{j,k}|.$$
>
> **Step 5 — divide and conclude.** Since $|c_j| > 0$, divide:
> $$|\lambda - A_{j,j}| \leq \sum_{k \neq j} |A_{j,k}|.$$
> This is exactly the condition that $\lambda \in D_j$. So $\lambda$ is contained in some Gershgorin disk. $\blacksquare$

> [!note]- Proof of the corollary (strictly diagonally dominant matrices are invertible)
> If for every $j$, $|A_{j,j}| > \sum_{k \neq j}|A_{j,k}|$, then for every $j$ the Gershgorin disk $D_j$ centred at $A_{j,j}$ with radius $\sum_{k \neq j}|A_{j,k}|$ does not contain $0$: the distance from $A_{j,j}$ to $0$ is $|A_{j,j}|$, which exceeds the radius. So $0 \notin \cup_j D_j$, hence (by the theorem) $0$ is not an eigenvalue of $T$, hence $T$ is invertible.

---

# Cross-Field Exercise Suggestions

**Convergence of iterative methods (numerical linear algebra).** Iterative methods for solving $Ax = b$ — Jacobi, Gauss-Seidel, SOR — rest on the spectral radius of an iteration matrix being less than $1$. Gershgorin gives a quick test: bound the spectral radius by the maximum Gershgorin disk radius (plus the corresponding diagonal entry). For strictly diagonally dominant $A$, this gives convergence of Jacobi and Gauss-Seidel methods unconditionally.

**Stability of discretised PDEs (applied analysis).** The discretisation of a second-order elliptic PDE on a grid produces a matrix with positive diagonal and small negative off-diagonal entries (for the standard 5-point stencil of the Laplacian, for instance). The Gershgorin disks lie in the right half-plane and are bounded away from zero, so the matrix is positive definite — and the discretised problem has a unique solution. The same Gershgorin disks bound the condition number of the matrix, controlling the numerical sensitivity.

**Markov chain spectral gap (probability).** The transition matrix $P$ of a Markov chain has the property that its row sums are all $1$. The Gershgorin disks all have centre and radius adding to at most $1 + |P_{jj}|$ (the row sum minus the diagonal plus the diagonal), so all eigenvalues are in the closed unit disk. The mixing rate of the chain is governed by the second-largest eigenvalue (in absolute value), and Gershgorin gives crude but useful bounds on this.

**Stability of fixed points (dynamical systems).** Near a fixed point $x_*$ of a discrete-time dynamical system $x_{n+1} = f(x_n)$, the linearisation has eigenvalues whose absolute values control stability. Gershgorin gives a quick check: if the Jacobian has small off-diagonal entries and diagonal entries less than $1$ in absolute value, the fixed point is attracting (all eigenvalues in the unit disk). This is the "diagonally dominant stability criterion" used in control theory.

---

# Bridges

- **[[Thm - Existence of Eigenvalues on Complex Vector Spaces|Existence of Eigenvalues on ℂ]]** — the prerequisite. Gershgorin says eigenvalues *exist* and are in certain disks; existence is provided by the existence theorem (when $F = \mathbb{C}$).

- **The Bauer-Fike theorem** — the perturbation refinement. For a diagonalisable matrix $A = X D X^{-1}$ and a perturbation $B$, every eigenvalue of $A + B$ is within $\|B\|_2 \cdot \kappa(X)$ of some eigenvalue of $A$ (where $\kappa(X)$ is the condition number of the diagonalisation). Gershgorin is the special case where $A$ is diagonal, where $X = I$ and the bound becomes the row-sum estimate.

- **The Perron-Frobenius theorem** — the positive matrix refinement. For a matrix $A$ with all entries positive, the spectral radius is itself an eigenvalue (the Perron eigenvalue), with a positive eigenvector. The Gershgorin disks for such matrices are all in the right half-plane (or in a disk centred on the real positive axis), supporting the Perron-Frobenius conclusion.

- **The Schur decomposition** — the tight basis. Schur gives an upper-triangular form, in which the Gershgorin disks collapse to the diagonal entries (the eigenvalues themselves). So the Gershgorin localisation is as tight as possible in the Schur basis, and the natural question becomes "what is the cost of using a non-Schur basis?" — answered by the Bauer-Fike bound.

---

# Unlocked by This

> [!tip] Bauer-Fike Theorem *(from Numerical Linear Algebra)*
> The perturbation refinement of Gershgorin: for a diagonalisable matrix and a perturbation, the eigenvalues move by at most $\|B\|_2 \cdot \kappa(X)$. The proof factorises $A + B = X(D + X^{-1} B X) X^{-1}$ and applies Gershgorin to $D + X^{-1} B X$.

> [!tip] Diagonal Dominance and Iterative Methods *(from Numerical Analysis)*
> Strictly diagonally dominant matrices are invertible (Gershgorin corollary), and Jacobi / Gauss-Seidel iterations converge for them. This is the foundation of practical iterative linear solvers.

> [!tip] Perron-Frobenius Theory *(from Linear Algebra and Probability)*
> For matrices with non-negative entries, the Perron-Frobenius theorem refines Gershgorin: the spectral radius is itself an eigenvalue, with a non-negative eigenvector. The proof uses Gershgorin to locate the disk containing the spectral radius and then uses positivity to extract the maximum eigenvalue from it.

> [!tip] Markov Chain Mixing Rates *(from Probability)*
> The mixing rate of a Markov chain is bounded by Gershgorin disks of the transition matrix. The Cheeger inequality refines this for symmetric Markov chains.

---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Topological Group"
  - "Def - Connected Space"
  - "Def - Path-Connected Space"
  - "Thm - Closure of a Subgroup is a Subgroup"
tags: [analysis, topology, topological-group, connectedness]
---

# Problem Statement

Show that the special orthogonal group $\operatorname{SO}(n) := \{A \in M_n(\mathbb{R}) : AA^T = I, \det A = 1\}$ is path-connected (and hence connected) for every $n \geq 1$.

**Recall:**

$\operatorname{SO}(n)$ is a closed subgroup of $\operatorname{O}(n)$, the orthogonal group. It is a [[Def - Topological Group|topological group]] under matrix multiplication, sitting inside $\operatorname{GL}_n(\mathbb{R}) \subseteq \mathbb{R}^{n^2}$ with the subspace topology. A space is [[Def - Path-Connected Space|path-connected]] if any two points can be joined by a continuous path.

**Geometric interpretation:** $\operatorname{SO}(n)$ is the group of orientation-preserving rotations of $\mathbb{R}^n$ — i.e., orthogonal transformations with $\det = +1$.

---

# Convergent Strategy

**Problem class:** Prove path-connectedness of a Lie group by constructing explicit paths from the identity.

**Assumption pattern:** $\operatorname{SO}(n)$ is a topological group, and the identity matrix $I$ is a distinguished point. To show path-connectedness, it suffices to show any matrix $A \in \operatorname{SO}(n)$ has a path to $I$ in $\operatorname{SO}(n)$.

**Theorem routing:** Induction on $n$. Base case $\operatorname{SO}(1) = \{1\}$, a single point. Inductive step: use that $\operatorname{SO}(n)$ acts transitively on the sphere $S^{n-1}$ with stabilizer $\operatorname{SO}(n-1)$, giving a fibration $\operatorname{SO}(n-1) \to \operatorname{SO}(n) \to S^{n-1}$. Path-connectedness of total space follows from path-connectedness of base and fiber.

Alternative (the "constructive" route in Bredon Problem 8): every rotation is a product of plane rotations, and each plane rotation is connected to the identity by a continuous path in the rotation angle.

**Key decision point:** Use the fibration approach or the constructive plane-rotation approach. The constructive approach is more elementary and works directly with matrices.

---

# Legal Operations Used

1. **Path-connected = path to a base point.** A space is path-connected iff every point has a path to a fixed base point. Use $I$ as the base point.

2. **Path concatenation.** If $A$ has a path to $B$ and $B$ has a path to $C$, then $A$ has a path to $C$.

3. **Continuous image of a connected space is connected.** $S^{n-1} = \operatorname{SO}(n)/\operatorname{SO}(n-1)$ is connected (it's a sphere for $n \geq 2$).

4. **Connectedness from fibration.** If both fiber and base of a Serre-like fibration are connected, so is the total space.

---

# Hints

> [!note]- Hint 1
> Induction on $n$. $\operatorname{SO}(1) = \{1\}$ trivially connected.

> [!note]- Hint 2
> For $n \geq 2$: $\operatorname{SO}(n)$ acts transitively on the sphere $S^{n-1}$ (any unit vector can be rotated to any other). The stabilizer of $(0, \dots, 0, 1)$ is $\operatorname{SO}(n-1)$ (rotations of the perpendicular $\mathbb{R}^{n-1}$). So $\operatorname{SO}(n)/\operatorname{SO}(n-1) \cong S^{n-1}$ as homogeneous spaces.

> [!note]- Hint 3
> Use Bredon's Section 15, Problem 5: if $G$ is a topological group and $H \leq G$ is a closed subgroup with both $H$ and $G/H$ connected, then $G$ is connected. (This is the key tool — apply with $G = \operatorname{SO}(n)$, $H = \operatorname{SO}(n-1)$, $G/H = S^{n-1}$.)

> [!note]- Hint 4
> The constructive alternative: use that any $A \in \operatorname{SO}(n)$ can be diagonalized (in real form) into a product of plane rotations $R(\theta_1) \oplus R(\theta_2) \oplus \dots$ (plus possibly a $\pm 1$ on real eigenvalues). Each plane rotation $R(\theta)$ has a continuous path $R(s\theta)$ to $I$ as $s$ runs from $1$ to $0$.

---

# Solution

The proof presents two routes. Step 1 handles the base case $\operatorname{SO}(1) = \{1\}$; Step 2 gives the inductive route via the homogeneous space $\operatorname{SO}(n)/\operatorname{SO}(n-1) \cong S^{n-1}$, lifting paths in the sphere back to paths in the rotation group; Step 3 gives the alternative constructive route, decomposing any rotation as a block diagonal of plane rotations $R(\theta_i)$ and using $\gamma(s) = \bigoplus R(s\theta_i)$ to interpolate to the identity. The non-obvious move is in Step 3 — the real-Jordan-form decomposition combined with the fact that the pairs of $-1$ eigenvalues combine into $R(\pi)$ is what makes the explicit path construction work for *every* element of $\operatorname{SO}(n)$, including reflections that don't look like rotations at first glance.

**Step 1: Base case.**

$\operatorname{SO}(1) = \{(1)\}$ is a single point, trivially path-connected.

**Step 2: Inductive step via the homogeneous space.**

> [!note]- Derivation
> Assume $\operatorname{SO}(n-1)$ is path-connected. The action of $\operatorname{SO}(n)$ on $\mathbb{R}^n$ restricts to a transitive action on $S^{n-1}$. The isotropy at $(0, \dots, 0, 1)$ is $\operatorname{SO}(n-1)$ (matrices fixing the last coordinate and rotating the perpendicular $\mathbb{R}^{n-1}$).
>
> By Bredon Proposition 15.14 (a compact topological group acting transitively on Hausdorff gives a homeomorphism with the homogeneous space): $\operatorname{SO}(n)/\operatorname{SO}(n-1) \cong S^{n-1}$.
>
> $S^{n-1}$ is path-connected for $n \geq 2$ (it's the unit sphere, easily seen path-connected via great-circle arcs).
>
> Now use Bredon Problem 15.5: if $H \leq G$ is closed and both $H$ and $G/H$ are connected (path-connected), then $G$ is connected (path-connected). Specifically, for $A \in \operatorname{SO}(n)$, consider the coset $A \cdot \operatorname{SO}(n-1)$; this lies in $\operatorname{SO}(n)/\operatorname{SO}(n-1) = S^{n-1}$, path-connected to $I \cdot \operatorname{SO}(n-1)$. Lift the path in the quotient back to a path in $\operatorname{SO}(n)$ ending at some point $A' \in A \cdot \operatorname{SO}(n-1)$. Then $A^{-1}A' \in \operatorname{SO}(n-1)$, path-connected to $I$ by induction. Concatenate the two paths.

**Step 3: Alternative constructive proof using plane rotations.**

> [!note]- Derivation
> Every $A \in \operatorname{SO}(n)$ can be written in a suitable orthonormal basis as a block-diagonal matrix
> $$A \sim \begin{pmatrix} R(\theta_1) & & \\ & \ddots & \\ & & R(\theta_k) \end{pmatrix} \oplus I_m$$
> where each $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ is a $2 \times 2$ rotation, and $I_m$ is a $\pm 1$-block. (Real eigenvalues come in $\pm 1$ pairs since $\det A = 1$; complex eigenvalues come in conjugate pairs $e^{\pm i\theta}$, giving real rotation blocks.) An odd number of $-1$ eigenvalues is impossible since $\det A = (-1)^{\text{count of }-1} \cdot \prod(\det R(\theta_i)) = (-1)^{\text{count of }-1} \cdot 1$, so the count of $-1$s must be even.
>
> Now, two $-1$s in the spectrum can be combined into a rotation by $\pi$: $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = R(\pi)$. So we can rewrite $A$ as a block-diagonal matrix of $R(\theta_i)$'s and an $I_m$ ($+1$ block).
>
> Define the path $\gamma(s) = \bigoplus_i R(s\theta_i) \oplus I_m$ for $s \in [0, 1]$. At $s = 1$, $\gamma(1) = A$. At $s = 0$, each $R(0) = I_2$, so $\gamma(0) = I_n$. Continuous in $s$ (each entry of $R(s\theta_i)$ is a continuous function of $s\theta_i$, hence of $s$). And $\gamma(s) \in \operatorname{SO}(n)$ for all $s$ (orthogonal: each block is orthogonal; determinant $+1$: each block has $\det R(s\theta_i) = 1$, and $\det I_m = 1$).
>
> Hence $A$ is path-connected to $I$ in $\operatorname{SO}(n)$. Since this holds for any $A$, $\operatorname{SO}(n)$ is path-connected.

> [!note]- Complete formal solution
> *Inductive proof.* Base: $\operatorname{SO}(1) = \{1\}$ path-connected. Inductive step: assume $\operatorname{SO}(n-1)$ path-connected. The action of $\operatorname{SO}(n)$ on $S^{n-1}$ is transitive with isotropy $\operatorname{SO}(n-1)$, giving $\operatorname{SO}(n)/\operatorname{SO}(n-1) \cong S^{n-1}$ (path-connected). By Bredon Problem 15.5, $\operatorname{SO}(n)$ is path-connected.
>
> *Constructive proof.* For $A \in \operatorname{SO}(n)$, decompose into block-diagonal plane rotations $R(\theta_i)$ in an orthonormal basis. The path $\gamma(s) = \bigoplus R(s\theta_i) \oplus I_m$ is continuous from $\gamma(0) = I$ to $\gamma(1) = A$, lying entirely in $\operatorname{SO}(n)$. $\blacksquare$

---

# Key Takeaways

**Topological groups can be analyzed by reducing to homogeneous spaces.** A topological group $G$ has a transitive action on $G/H$ for any closed subgroup $H$. Properties of $G$ (connectedness, compactness, fundamental group) decompose into properties of $H$ and $G/H$. The trigger-reaction pattern: "want to show topological property of $G$ $\Rightarrow$ find a closed subgroup $H$ whose quotient $G/H$ is a familiar space (sphere, projective space) and reduce".

**Plane rotations are the "atoms" of $\operatorname{SO}(n)$.** Every special orthogonal matrix decomposes into a product of plane rotations and a $+1$-block. This is the real Jordan form for orthogonal matrices and the geometric content of "Lie algebra of $\operatorname{SO}(n)$ is spanned by skew-symmetric matrices, generating plane rotations via exponentiation". Each plane rotation is parametrized by an angle $\theta$, giving the $\theta = 0$ path back to the identity.

**Connectedness of orthogonal group has two components.** Contrast with $\operatorname{O}(n) = \operatorname{SO}(n) \sqcup \operatorname{SO}(n) \cdot D$ where $D$ is a reflection (any matrix with $\det = -1$). These two pieces are each path-connected (as $\operatorname{SO}(n)$ and its translate), but $\operatorname{O}(n)$ as a whole has *two* connected components, distinguished by the determinant. See [[Ex - The orthogonal group has two components]].

**Generalization to other classical groups.** The same argument (induction + homogeneous space) shows:
- $\operatorname{U}(n)$ is path-connected (via $\operatorname{U}(n)/\operatorname{U}(n-1) \cong S^{2n-1}$).
- $\operatorname{SU}(n)$ is path-connected (via $\operatorname{SU}(n)/\operatorname{SU}(n-1) \cong S^{2n-1}$).
- $\operatorname{Sp}(n)$ is path-connected (via $\operatorname{Sp}(n)/\operatorname{Sp}(n-1) \cong S^{4n-1}$).

For $\operatorname{SL}_n$, the argument needs to handle the unbounded nature (compactness of base fails), but the connectedness still holds via different techniques.

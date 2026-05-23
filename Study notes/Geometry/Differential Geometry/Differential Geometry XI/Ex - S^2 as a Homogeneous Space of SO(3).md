---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Lie Group"
  - "Def - Smooth Action of a Lie Group"
  - "Def - Homogeneous Space"
  - "Thm - Orbit-Stabilizer for Lie Group Actions"
tags: [geometry, differential-geometry, lie-groups]
---

# Problem Statement

Show that the natural action of $\mathrm{SO}(3)$ on the unit $2$-sphere $S^2 \subseteq \mathbb{R}^3$ is smooth and transitive, with stabilizer at the north pole $N = (0, 0, 1) \in S^2$ isomorphic to $\mathrm{SO}(2)$. Conclude that

$$S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$$

as smooth manifolds, with the dimensions agreeing: $\dim S^2 = 2 = \dim \mathrm{SO}(3) - \dim \mathrm{SO}(2) = 3 - 1$.

**Recall:**

$\mathrm{SO}(3)$ acts on $\mathbb{R}^3$ by matrix multiplication: $A \cdot v = Av$. This restricts to an action on $S^2$ (the sphere is preserved by orthogonal matrices, $|Av| = |v|$). The [[Thm - Orbit-Stabilizer for Lie Group Actions|orbit-stabilizer theorem]] says that for a smooth transitive action, $M \cong G/G_p$ where $G_p$ is the stabilizer.

---

# Convergent Strategy

**Problem class:** Realize a familiar manifold ($S^2$) as a homogeneous space $G/H$ for a Lie group $G$ with closed subgroup $H$. The route is orbit-stabilizer: verify the action is smooth and transitive, compute the stabilizer.

**Assumption pattern:** $\mathrm{SO}(3)$ is the rotation group of $\mathbb{R}^3$; its action on $S^2$ is the restriction of the linear action on $\mathbb{R}^3$. Two key facts: (1) any rotation can be decomposed as a sequence of two simpler rotations (e.g., Euler angles), making the action transitive; (2) the stabilizer of a single point on the sphere is the subgroup fixing the line through that point, which is rotations around that axis — a copy of $\mathrm{SO}(2)$.

**Theorem routing:** (1) Verify smoothness of the action (multiplication and restriction are smooth). (2) Verify transitivity by constructing, for any $v \in S^2$, a rotation $A \in \mathrm{SO}(3)$ with $A \cdot N = v$. (3) Compute the stabilizer of $N$ explicitly: rotations of $\mathbb{R}^3$ fixing $N$ are rotations around the $z$-axis, parametrized by an angle. (4) Apply [[Thm - Orbit-Stabilizer for Lie Group Actions|smooth orbit-stabilizer]] to conclude $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$.

**Key decision point:** The transitivity verification is the most substantive step. Given an arbitrary unit vector $v \in S^2$, one must exhibit a specific rotation taking $N = (0, 0, 1)$ to $v$. The construction uses Euler angles or the Gram–Schmidt orthogonalization: extend $\{v\}$ to an oriented orthonormal basis $\{e_1', e_2', v\}$ of $\mathbb{R}^3$, and the matrix $A = [e_1', e_2', v]$ (with columns $e_1', e_2', v$) is in $\mathrm{SO}(3)$ and sends $N$ to $v$.

---

# Legal Operations Used

1. **Identify a manifold as a homogeneous space (operation 5 from the topic page).** Applied here: identify $S^2$ as $\mathrm{SO}(3)/\mathrm{SO}(2)$ via the natural rotation action.

2. **Use the orbit map to embed a homogeneous space (operation 9 from the topic page).** The orbit map $\theta^{(N)} : \mathrm{SO}(3) \to S^2$, $A \mapsto A \cdot N$, descends to a $G$-equivariant diffeomorphism $\mathrm{SO}(3)/\mathrm{SO}(2) \to S^2$.

---

# Hints

> [!note]- Hint 1
> Smoothness of the action: $\theta : \mathrm{SO}(3) \times S^2 \to S^2$, $(A, v) \mapsto Av$. The map $A v$ is a polynomial in the entries of $A$ and components of $v$, so it is smooth. Restricting to $\mathrm{SO}(3) \times S^2 \subseteq \mathrm{GL}(3, \mathbb{R}) \times \mathbb{R}^3$ is still smooth.

> [!note]- Hint 2
> Transitivity: given $v \in S^2$, find a rotation $A \in \mathrm{SO}(3)$ with $AN = v$. Use the Gram–Schmidt extension: extend $\{v\}$ to a positively-oriented orthonormal basis of $\mathbb{R}^3$, and the matrix with these vectors as columns is the desired rotation.

> [!note]- Hint 3
> Stabilizer at $N = (0, 0, 1)$: $A \cdot N = N$ means $A$ has third column $(0, 0, 1)^T$. With $A^T A = I$ and $\det A = 1$, this forces $A$ to have the block form $A = \begin{pmatrix} B & 0 \\ 0 & 1 \end{pmatrix}$ with $B \in \mathrm{SO}(2)$. So the stabilizer is the embedded $\mathrm{SO}(2) \hookrightarrow \mathrm{SO}(3)$ as $2 \times 2$ rotations of the $xy$-plane.

> [!note]- Hint 4
> Apply orbit-stabilizer: $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$ as smooth manifolds (via the orbit map descended through the quotient). Dimensions check out: $\dim \mathrm{SO}(3) = 3$, $\dim \mathrm{SO}(2) = 1$, $\dim S^2 = 2 = 3 - 1$.

---

# Solution

The proof works through orbit-stabilizer: verify smoothness, verify transitivity, compute the stabilizer.

**Step 1: The action $\theta : \mathrm{SO}(3) \times S^2 \to S^2$, $(A, v) \mapsto Av$, is smooth.**

The matrix-vector product $(A, v) \mapsto Av$ is a polynomial in the entries of $A$ and components of $v$, hence smooth as a map $M(3, \mathbb{R}) \times \mathbb{R}^3 \to \mathbb{R}^3$. Restricted to $\mathrm{SO}(3) \times S^2$, the image lies in $S^2$ (orthogonal matrices preserve norms: $|Av|^2 = v^T A^T A v = v^T v = |v|^2$), so the restriction is smooth $\mathrm{SO}(3) \times S^2 \to S^2$.

> [!note]- Derivation
> The matrix product $Av$ has components $(Av)^i = A^i_j v^j$, a sum of products of entries — polynomial, hence smooth, hence the action is smooth $M(3, \mathbb{R}) \times \mathbb{R}^3 \to \mathbb{R}^3$. The norm-preservation $|Av| = |v|$ uses $A \in \mathrm{O}(3)$: $|Av|^2 = (Av)^T(Av) = v^T A^T A v = v^T I v = v^T v = |v|^2$. So for $v \in S^2$ ($|v| = 1$) and $A \in \mathrm{SO}(3) \subseteq \mathrm{O}(3)$, $Av \in S^2$. The restriction is smooth as the composition of smooth maps.

**Step 2: The action is transitive.**

Given $v \in S^2$, we construct $A \in \mathrm{SO}(3)$ with $AN = v$ where $N = (0, 0, 1)$. Choose an orthonormal basis $\{e_1', e_2', v\}$ of $\mathbb{R}^3$ with $\det[e_1', e_2', v] = 1$ (positive orientation). Such a basis exists: extend $\{v\}$ to an orthonormal basis $\{e_1', e_2', v\}$ by Gram–Schmidt; if the resulting basis has $\det = -1$, swap $e_1'$ and $e_2'$ to flip orientation. Define $A = [e_1', e_2', v]$, the $3 \times 3$ matrix with these columns. Then $A^T A = I$ (orthonormality of columns), $\det A = 1$ (positive orientation), and $A N = A \cdot (0, 0, 1)^T = $ (third column of $A$) $= v$. So $A \in \mathrm{SO}(3)$ and $A \cdot N = v$, proving transitivity.

> [!note]- Derivation
> Let $v \in S^2$. Extend $\{v\}$ to an orthonormal basis of $\mathbb{R}^3$: pick any unit vector $u_1$ orthogonal to $v$ (exists since $v^\perp \subseteq \mathbb{R}^3$ is $2$-dimensional, nontrivial), then $u_2 = v \times u_1$ is a unit vector orthogonal to both. The triple $\{u_1, u_2, v\}$ is orthonormal. Check orientation: $\det[u_1 | u_2 | v]$. We have $u_2 = v \times u_1$, so $\det[u_1 | u_2 | v] = \det[u_1 | v \times u_1 | v]$. Use that $\det[a, b, c] = a \cdot (b \times c)$: $\det[u_1, v \times u_1, v] = u_1 \cdot ((v \times u_1) \times v) = u_1 \cdot (|v|^2 u_1 - (v \cdot u_1) v) = u_1 \cdot u_1 - 0 = 1$ (using $|v|^2 = 1$, $v \perp u_1$). So $\det A = 1$, $A \in \mathrm{SO}(3)$. And $A \cdot (0, 0, 1)^T = v$ (the third column of $A$).

**Step 3: The stabilizer of $N$ is isomorphic to $\mathrm{SO}(2)$.**

The stabilizer $G_N = \{A \in \mathrm{SO}(3) : AN = N\}$ consists of rotations fixing the vector $N = (0, 0, 1)$. A rotation $A$ fixes $N$ iff the third column of $A$ is $N$ (since $AN = $ third column of $A$). With $A \in \mathrm{O}(3)$, the columns are orthonormal, so the first two columns lie in $N^\perp = $ the $xy$-plane $= \mathbb{R}^2 \times \{0\}$. The orthonormality of the first two columns gives $A \in \mathrm{SO}(3)$ if the resulting $2 \times 2$ block has determinant $+1$. So

$$G_N = \left\{ \begin{pmatrix} B & 0 \\ 0 & 1 \end{pmatrix} : B \in \mathrm{SO}(2) \right\} \cong \mathrm{SO}(2).$$

This is the embedded $\mathrm{SO}(2) \hookrightarrow \mathrm{SO}(3)$ as the block-diagonal rotations of the $xy$-plane.

> [!note]- Derivation
> $A N = N$ with $N = (0, 0, 1)^T$ means the third column of $A$ is $(0, 0, 1)^T$, i.e., $A^i_3 = \delta^i_3$. So $A = \begin{pmatrix} A^1_1 & A^1_2 & 0 \\ A^2_1 & A^2_2 & 0 \\ A^3_1 & A^3_2 & 1 \end{pmatrix}$. The orthogonality $A^T A = I$ forces the third row also to be $(0, 0, 1)$: $\sum_j A^j_3 A^j_1 = 0$ becomes $A^3_1 = 0$ (only $j = 3$ contributes), similarly $A^3_2 = 0$. So $A = \begin{pmatrix} A^1_1 & A^1_2 & 0 \\ A^2_1 & A^2_2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$. The top-left $2 \times 2$ block $B = \begin{pmatrix} A^1_1 & A^1_2 \\ A^2_1 & A^2_2 \end{pmatrix}$ has $B^T B = I_2$ (from the upper-left block of $A^T A = I$), so $B \in \mathrm{O}(2)$. The determinant $\det A = \det B \cdot 1 = \det B = 1$ forces $B \in \mathrm{SO}(2)$. Conversely, any $B \in \mathrm{SO}(2)$ gives such an $A \in G_N$. So $G_N \cong \mathrm{SO}(2)$.

**Step 4: Apply orbit-stabilizer to conclude $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$.**

By [[Thm - Orbit-Stabilizer for Lie Group Actions|smooth orbit-stabilizer]] applied to the smooth transitive action of $\mathrm{SO}(3)$ on $S^2$ with stabilizer $G_N \cong \mathrm{SO}(2)$ at the basepoint $N$, the orbit map $\theta^{(N)} : \mathrm{SO}(3) \to S^2$ descends to a $\mathrm{SO}(3)$-equivariant diffeomorphism

$$\overline{\theta^{(N)}} : \mathrm{SO}(3)/G_N \xrightarrow{\;\sim\;} S^2.$$

Identifying $G_N \cong \mathrm{SO}(2)$:

$$S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2).$$

The dimensions match: $\dim S^2 = 2 = 3 - 1 = \dim \mathrm{SO}(3) - \dim \mathrm{SO}(2)$.

> [!note]- Complete formal solution
> *Smoothness:* The action $\theta : \mathrm{SO}(3) \times S^2 \to S^2$, $(A, v) \mapsto Av$, is smooth (matrix-vector multiplication, polynomial in the entries).
>
> *Transitivity:* For any $v \in S^2$, choose an orthonormal basis $\{u_1, u_2, v\}$ of $\mathbb{R}^3$ with $u_2 = v \times u_1$. Then $A = [u_1 \mid u_2 \mid v] \in \mathrm{SO}(3)$ (orthonormal columns; $\det = u_1 \cdot (u_2 \times v) = u_1 \cdot u_1 = 1$), and $A \cdot N = v$. So the action is transitive.
>
> *Stabilizer:* $G_N = \{A \in \mathrm{SO}(3) : AN = N\}$ consists of $A$ whose third column equals $N = (0,0,1)^T$. Orthogonality forces the third row to also equal $(0,0,1)$. The remaining $2 \times 2$ upper-left block lies in $\mathrm{SO}(2)$. So $G_N \cong \mathrm{SO}(2)$, embedded as the block-diagonal subgroup of $\mathrm{SO}(3)$.
>
> *Conclusion:* By orbit-stabilizer, $S^2 \cong \mathrm{SO}(3)/G_N \cong \mathrm{SO}(3)/\mathrm{SO}(2)$. Dimensions: $\dim S^2 = 2 = 3 - 1$. $\qquad\blacksquare$

---

# Key Takeaways

**Spheres as homogeneous spaces of orthogonal groups.**

The construction $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$ generalizes: $S^n = \mathrm{SO}(n+1)/\mathrm{SO}(n)$ for every $n \geq 0$. The proof structure is identical: $\mathrm{SO}(n+1)$ acts on $\mathbb{R}^{n+1}$ by matrix multiplication, restricts transitively to $S^n$, and the stabilizer of any unit vector is the rotation group preserving the orthogonal hyperplane, which is $\mathrm{SO}(n)$. The dimension count $\dim S^n = \dim \mathrm{SO}(n+1) - \dim \mathrm{SO}(n) = \binom{n+1}{2} - \binom{n}{2} = n$ provides immediate verification. This realization is the foundation for harmonic analysis on the sphere: $L^2(S^n)$ decomposes into representations of $\mathrm{SO}(n+1)$ via the Peter–Weyl theorem, and the spherical harmonics are the natural basis adapted to this group action.

**Stabilizers preserve transverse data.**

At the north pole $N$, the stabilizer $\mathrm{SO}(2)$ acts on the tangent space $T_N S^2 \cong N^\perp = \mathbb{R}^2$ as the **defining representation**: rotations around the $z$-axis act on the $xy$-tangent plane as standard $2$D rotations. This is the **isotropy representation** of the homogeneous space $\mathrm{SO}(3)/\mathrm{SO}(2)$. The isotropy representation is the key object for classifying invariant geometric structures: invariant Riemannian metrics on $S^2$ correspond to invariant inner products on $T_N S^2$ — which, by $\mathrm{SO}(2)$-invariance, are all proportional to the standard inner product, giving the round metric uniquely up to scaling. The general principle: $G$-invariant geometric objects on $G/H$ are determined by $H$-invariant linear-algebraic data at the basepoint.

**The Hopf fibration is the next level of structure.**

The construction $S^3 = \mathrm{SU}(2)$ acts on $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$ via the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$, with stabilizer at $N$ being a circle (the preimage of $\mathrm{SO}(2)$ under the double cover is a circle subgroup of $\mathrm{SU}(2)$, which is $S^1 \cong \mathrm{U}(1)$). So $S^2 \cong \mathrm{SU}(2)/\mathrm{U}(1) \cong S^3/S^1$ — the famous **Hopf fibration** $S^1 \to S^3 \to S^2$. This is the first non-trivial example of a non-trivial principal $S^1$-bundle, and it is the simplest case of the **Yang–Mills monopole** in physics. The construction in this exercise is the first step of an extended chain of homogeneous-space identifications leading to fundamental examples in topology and physics.

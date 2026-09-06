---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Lie Group"
  - "Def - Diffeomorphism"
  - "Def - The Lie Algebra of a Lie Group"
tags: [geometry, differential-geometry, lie-groups]
---

# Problem Statement

Show that the special unitary group

$$\mathrm{SU}(2) = \{U \in \mathrm{GL}(2, \mathbb{C}) : U^* U = I, \det U = 1\}$$

is diffeomorphic to the unit $3$-sphere $S^3 \subseteq \mathbb{R}^4 \cong \mathbb{C}^2$ as smooth manifolds, exhibiting an explicit diffeomorphism. Identify the Lie algebra $\mathfrak{su}(2)$ as the space of traceless skew-Hermitian $2 \times 2$ matrices, and outline how the construction reveals the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$.

**Recall:**

$S^3 = \{(z, w) \in \mathbb{C}^2 : |z|^2 + |w|^2 = 1\}$, identified with $\{(a, b, c, d) \in \mathbb{R}^4 : a^2 + b^2 + c^2 + d^2 = 1\}$ via $z = a + ib$, $w = c + id$. A **diffeomorphism** is a smooth bijection whose inverse is also smooth. The [[Def - The Lie Algebra of a Lie Group|Lie algebra]] of $\mathrm{SU}(2)$ is $\mathfrak{su}(2) = T_I \mathrm{SU}(2) \subseteq \mathfrak{gl}(2, \mathbb{C}) = M(2, \mathbb{C})$.

---

# Convergent Strategy

**Problem class:** Identification of a Lie group with a smooth manifold by exhibiting an explicit parametrization, plus a Lie algebra computation that connects to a deeper structural result (the double cover).

**Assumption pattern:** $\mathrm{SU}(2)$ is given by two equations: $U^* U = I$ and $\det U = 1$. For $U = \begin{pmatrix} z & -\bar w \\ w & \bar z \end{pmatrix}$, the equations reduce to $|z|^2 + |w|^2 = 1$ — which is exactly the equation cutting out $S^3$. This **parametrization** is the heart of the construction.

**Theorem routing:** Route: (1) parametrize the most general unitary $2 \times 2$ matrix; (2) impose $\det = 1$ to reduce to the special-unitary case; (3) read off the resulting matrix as a point of $S^3$; (4) verify the parametrization is a diffeomorphism. For the Lie algebra, differentiate the defining equations at $I$ to get traceless skew-Hermitian matrices, three-dimensional. For the double cover, the action of $\mathrm{SU}(2)$ on $\mathfrak{su}(2)$ by conjugation preserves the trace-zero condition and gives a homomorphism $\mathrm{SU}(2) \to \mathrm{SO}(\mathfrak{su}(2)) = \mathrm{SO}(3)$ — a covering map with kernel $\{\pm I\}$.

**Key decision point:** The non-obvious step is **recognizing the general form of a unitary $2 \times 2$ matrix with determinant $1$**. The constraint $U^* U = I$ alone forces unitarity, which in $2 \times 2$ means the columns are orthonormal. Writing the first column as $\binom{z}{w}$ with $|z|^2 + |w|^2 = 1$ and the second column determined up to phase, the $\det = 1$ condition then pins down the second column as $\binom{-\bar w}{\bar z}$. This is the **quaternion parametrization** of $\mathrm{SU}(2)$.

---

# Legal Operations Used

1. **Compute the Lie algebra by differentiating the defining equation (operation 1 from the topic page).** Applied to the equations $U^* U = I$ and $\det U = 1$, yielding traceless skew-Hermitian matrices.

2. **Use the adjoint representation to convert group conjugation to a linear action (operation 6 from the topic page).** The conjugation action of $\mathrm{SU}(2)$ on $\mathfrak{su}(2)$ is a linear action preserving the Killing form, hence factors through $\mathrm{SO}(\mathfrak{su}(2)) \cong \mathrm{SO}(3)$.

---

# Hints

> [!note]- Hint 1
> The most general $2 \times 2$ unitary matrix has columns that are orthonormal in $\mathbb{C}^2$. Set the first column to $(z, w)^T$ with $|z|^2 + |w|^2 = 1$. What is the second column, up to a phase?

> [!note]- Hint 2
> The second column $\binom{a}{b}$ must satisfy $\bar z a + \bar w b = 0$ (orthogonality) and $|a|^2 + |b|^2 = 1$ (norm). The orthogonality condition forces $\binom{a}{b} = \alpha \binom{-\bar w}{\bar z}$ for some $\alpha \in \mathbb{C}$, and the norm forces $|\alpha| = 1$.

> [!note]- Hint 3
> The determinant condition $\det U = 1$ pins down the phase $\alpha$. Compute $\det \begin{pmatrix} z & \alpha (-\bar w) \\ w & \alpha \bar z \end{pmatrix} = \alpha(|z|^2 + |w|^2) = \alpha$. So $\alpha = 1$, giving $U = \begin{pmatrix} z & -\bar w \\ w & \bar z \end{pmatrix}$.

> [!note]- Hint 4
> The map $\Phi : S^3 \to \mathrm{SU}(2)$, $(z, w) \mapsto \begin{pmatrix} z & -\bar w \\ w & \bar z \end{pmatrix}$, is smooth (entries are polynomial in real and imaginary parts), bijective (every $\mathrm{SU}(2)$ element has this form), with smooth inverse $(\text{first column of } U)$.

> [!note]- Hint 5
> For the Lie algebra, differentiate $U^* U = I$ at $I$ to get $X^* + X = 0$ (skew-Hermitian), and $\det U = 1$ to get $\mathrm{tr} X = 0$. The skew-Hermitian + traceless conditions give $\mathfrak{su}(2)$, three-dimensional over $\mathbb{R}$.

> [!note]- Hint 6
> For the double cover, consider the action of $\mathrm{SU}(2)$ on $\mathfrak{su}(2)$ by conjugation $U \cdot X = UXU^{-1}$. Since $\mathfrak{su}(2)$ is $3$-dimensional and has a natural inner product (the Killing form, up to scaling), and conjugation preserves both, the action gives a homomorphism $\mathrm{SU}(2) \to \mathrm{SO}(\mathfrak{su}(2)) \cong \mathrm{SO}(3)$. The kernel is the center $\{\pm I\}$.

---

# Solution

The diffeomorphism is constructed via the quaternion parametrization. The Lie algebra is computed by differentiation. The double cover is the adjoint representation modulo center.

**Step 1: Parametrize $\mathrm{SU}(2)$ as the set of matrices $\begin{pmatrix} z & -\bar w \\ w & \bar z \end{pmatrix}$ with $|z|^2 + |w|^2 = 1$.**

A unitary $2\times2$ matrix has orthonormal columns for the Hermitian product $\langle u,v\rangle=\bar u_1v_1+\bar u_2v_2$. Write its first column as $\binom zw$, where $|z|^2+|w|^2=1$. The vector $\binom{-\bar w}{\bar z}$ is unit and orthogonal to it because
$$\left\langle\binom zw,\binom{-\bar w}{\bar z}\right\rangle=-\bar z\bar w+\bar w\bar z=0.$$
Every unit vector orthogonal to the first is a phase multiple of this one. Since
$$\det\begin{pmatrix}z&-\bar w\\w&\bar z\end{pmatrix}=|z|^2+|w|^2=1,$$
the determinant-one condition forces that phase to be $1$.

> [!note]- Derivation
> The complex inner product on $\mathbb{C}^2$ is $\langle u, v \rangle = u_1 \bar v_1 + u_2 \bar v_2$ (linear in the first slot, conjugate-linear in the second). The second column $\binom{a}{b}$ orthogonal to $\binom{z}{w}$ satisfies $\langle (a, b), (z, w) \rangle = a \bar z + b \bar w = 0$. Up to phase, the unit orthogonal direction is $\binom{-\bar w}{\bar z}/|(-\bar w, \bar z)| = \binom{-\bar w}{\bar z}$ (already unit since $|-\bar w|^2 + |\bar z|^2 = |w|^2 + |z|^2 = 1$). So the second column is $\alpha \binom{-\bar w}{\bar z}$ with $|\alpha| = 1$. Computing $\det U = z \cdot \alpha \bar z - (-\bar w \alpha) \cdot w = \alpha(|z|^2 + |w|^2) = \alpha$. Setting $\det U = 1$ gives $\alpha = 1$, so $U = \begin{pmatrix} z & -\bar w \\ w & \bar z \end{pmatrix}$.

**Step 2: The map $\Phi : S^3 \to \mathrm{SU}(2)$ is a smooth bijection with smooth inverse.**

Define $\Phi(z, w) = \begin{pmatrix} z & -\bar w \\ w & \bar z \end{pmatrix}$ for $(z, w) \in S^3$. By Step 1, this is well-defined into $\mathrm{SU}(2)$ and is surjective. It is injective because the first column determines $(z, w)$. Smoothness in both directions follows because the entries are polynomial in the real and imaginary parts of $z$ and $w$.

> [!note]- Derivation
> *Smoothness of $\Phi$.* Write $z = a + ib$, $w = c + id$ for real $a, b, c, d$ with $a^2 + b^2 + c^2 + d^2 = 1$. Then $\Phi(z, w) = \begin{pmatrix} a + ib & -c + id \\ c + id & a - ib \end{pmatrix}$, with real and imaginary parts of each entry polynomial in $(a, b, c, d)$. So $\Phi$ is smooth as a map $S^3 \subseteq \mathbb{R}^4 \to M(2, \mathbb{C}) \cong \mathbb{R}^8$.
>
> *Smoothness of $\Phi^{-1}$.* For $U = \begin{pmatrix} U_{11} & U_{12} \\ U_{21} & U_{22} \end{pmatrix} \in \mathrm{SU}(2)$, $\Phi^{-1}(U) = (U_{11}, U_{21}) \in \mathbb{C}^2$. This is the projection onto the first column, restricted to $\mathrm{SU}(2)$, which is smooth.
>
> $\Phi \circ \Phi^{-1} = \mathrm{id}_{\mathrm{SU}(2)}$ and $\Phi^{-1} \circ \Phi = \mathrm{id}_{S^3}$ are immediate. So $\Phi$ is a diffeomorphism.

**Step 3: $\mathfrak{su}(2) = \{X \in M(2, \mathbb{C}) : X^* = -X, \mathrm{tr} X = 0\}$, a $3$-dimensional real vector space.**

Differentiate the defining equations of $\mathrm{SU}(2)$ at $I$. For a curve $U(t) = I + tX + O(t^2)$:

- $U^* U = I$ gives $X^* + X = 0$ (skew-Hermiticity);
- $\det U = 1$ gives $\mathrm{tr} X = 0$ (tracelessness).

A traceless skew-Hermitian $2 \times 2$ matrix has the form $X = \begin{pmatrix} ix_3 & x_1 + ix_2 \\ -x_1 + ix_2 & -ix_3 \end{pmatrix}$ for real $x_1, x_2, x_3$, three parameters. So $\dim_\mathbb{R} \mathfrak{su}(2) = 3$, matching $\dim \mathrm{SU}(2) = 3 = \dim S^3$.

> [!note]- Derivation
> Skew-Hermiticity $X^* = -X$ for a $2 \times 2$ complex matrix $X = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ means $\begin{pmatrix} \bar a & \bar c \\ \bar b & \bar d \end{pmatrix} = \begin{pmatrix} -a & -b \\ -c & -d \end{pmatrix}$. So $a = -\bar a$ (purely imaginary), $d = -\bar d$ (purely imaginary), and $c = -\bar b$. Writing $a = ix_3$, $d = ix_3'$, $b = x_1 + ix_2$: $X = \begin{pmatrix} ix_3 & x_1 + ix_2 \\ -x_1 + ix_2 & ix_3' \end{pmatrix}$. The trace-zero condition $\mathrm{tr} X = i(x_3 + x_3') = 0$ gives $x_3' = -x_3$. So $X = \begin{pmatrix} ix_3 & x_1 + ix_2 \\ -x_1 + ix_2 & -ix_3 \end{pmatrix}$ — three real parameters $x_1, x_2, x_3$. A canonical basis is $\{i\sigma_a / 2\}_{a=1,2,3}$ where $\sigma_a$ are the Pauli matrices.

**Step 4: The adjoint representation $\mathrm{Ad} : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is the double cover.**

The conjugation action $U \cdot X = U X U^{-1} = U X U^*$ on $\mathfrak{su}(2)$ preserves the trace-zero and skew-Hermitian conditions, hence maps $\mathfrak{su}(2) \to \mathfrak{su}(2)$. The map $X \mapsto X^* X$ is a positive-definite Hermitian form on $\mathfrak{su}(2)$ (the Killing form up to scaling), and conjugation preserves it (since $(UXU^*)^*(UXU^*) = U X^* X U^*$, with the same trace under cyclic invariance). So $\mathrm{Ad} : \mathrm{SU}(2) \to \mathrm{SO}(\mathfrak{su}(2))$ lands in $\mathrm{SO}(3)$ (since $\dim_\mathbb{R} \mathfrak{su}(2) = 3$).

The kernel is $\{U \in \mathrm{SU}(2) : UXU^{-1} = X \text{ for all } X \in \mathfrak{su}(2)\}$ — the center of $\mathrm{SU}(2)$, which is $\{\pm I\}$ (since $\mathfrak{su}(2)$ contains a basis that does not commute with any non-scalar matrix, and the only scalars in $\mathrm{SU}(2)$ are $\pm I$). So $\mathrm{Ad}$ is a double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$, with kernel $\mathbb{Z}/2$.

> [!note]- Derivation
> The Killing-form-style inner product on $\mathfrak{su}(2)$ is $\langle X, Y \rangle = -\mathrm{tr}(XY)/2$ (with the sign and factor chosen to make Pauli generators orthonormal). It is $\mathrm{Ad}$-invariant: $\langle UXU^{-1}, UYU^{-1} \rangle = -\mathrm{tr}(UXU^{-1} UYU^{-1})/2 = -\mathrm{tr}(UXY U^{-1})/2 = -\mathrm{tr}(XY)/2 = \langle X, Y \rangle$ by cyclic invariance of trace. So $\mathrm{Ad}_U \in \mathrm{O}(\mathfrak{su}(2)) \cong \mathrm{O}(3)$. Connectedness of $\mathrm{SU}(2)$ (it's $S^3$, which is connected) forces $\mathrm{Ad}_U \in \mathrm{SO}(3)$ (the identity component). The differential at $I$ is $\mathrm{ad}$, which surjects onto $\mathfrak{so}(3)$ (since both algebras are $3$-dimensional and the map is injective by the bracket computation $[\sigma_a, \sigma_b] = 2i\epsilon_{abc}\sigma_c$ matching $[e_a, e_b]_\times = \epsilon_{abc} e_c$ up to scaling), so $\mathrm{Ad}$ is surjective onto $\mathrm{SO}(3)$. The kernel is $\{U : UXU^{-1} = X \forall X\} = Z(\mathrm{SU}(2)) = \{\pm I\}$. Hence $\mathrm{Ad} : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is a $2$-to-$1$ surjective Lie group homomorphism — a double cover.

> [!note]- Complete formal solution
> *[[Def - Diffeomorphism|Diffeomorphism]] $\mathrm{SU}(2) \cong S^3$.* Every $U \in \mathrm{SU}(2)$ has the form $U = \begin{pmatrix} z & -\bar w \\ w & \bar z \end{pmatrix}$ with $|z|^2 + |w|^2 = 1$, by the unitary-orthonormal-column argument plus the $\det = 1$ phase pinning. The map $\Phi : S^3 \to \mathrm{SU}(2)$, $(z, w) \mapsto \Phi(z, w)$ given by this formula, is smooth (polynomial entries), bijective (every $\mathrm{SU}(2)$ element has this form, and the form determines $(z, w)$), with smooth inverse "first column". Hence $\Phi$ is a diffeomorphism.
>
> *Lie algebra.* Differentiating $U^* U = I$ at $I$ gives $X^* + X = 0$ (skew-Hermitian). Differentiating $\det U = 1$ gives $\mathrm{tr} X = 0$. So $\mathfrak{su}(2) = \{X : X^* = -X, \mathrm{tr} X = 0\}$, three-dimensional over $\mathbb{R}$, with canonical basis $\{i\sigma_a/2\}$ from the Pauli matrices.
>
> *Double cover.* The conjugation action of $\mathrm{SU}(2)$ on $\mathfrak{su}(2)$ preserves trace-zero and skew-Hermitian, and preserves the Hermitian form $\langle X, Y \rangle = -\mathrm{tr}(XY)/2$ (by cyclic invariance of trace). So $\mathrm{Ad} : \mathrm{SU}(2) \to \mathrm{SO}(\mathfrak{su}(2)) \cong \mathrm{SO}(3)$ is a Lie group homomorphism. Its kernel is the center $Z(\mathrm{SU}(2)) = \{\pm I\} \cong \mathbb{Z}/2$. Its image is $\mathrm{SO}(3)$ (by [[Def - Dimension|dimension]] and connectedness arguments). So $\mathrm{Ad}$ is a double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$. $\qquad\blacksquare$

> [!warning] Illegal but tempting: assuming $\mathrm{SU}(2) \cong \mathrm{SO}(3)$ because both have the same Lie algebra
> Two Lie [[Def - Group|groups]] with isomorphic Lie algebras are not in general isomorphic — they can differ by a discrete center, as $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ do. The temptation comes from over-trusting the Lie functor; the corrective is **simple connectivity**. $\mathrm{SU}(2) \cong S^3$ is simply connected; $\mathrm{SO}(3)$ has $\pi_1 = \mathbb{Z}/2$. The Lie correspondence works only on the simply-connected side, so all Lie algebra [[Def - Homomorphism|homomorphisms]] integrate uniquely to $\mathrm{SU}(2)$, but not all integrate to $\mathrm{SO}(3)$ — only those that vanish on the kernel $\{\pm I\}$.

---

# Key Takeaways

**Quaternion parametrization is the source of "$\mathrm{SU}(2) \cong S^3$".**

The parametrization $U = \begin{pmatrix} z & -\bar w \\ w & \bar z \end{pmatrix}$ is the matrix form of the unit quaternion $q = z + j w$ (with the quaternionic identification $j w = -\bar w + j \cdot \bar z$). Multiplication of such matrices corresponds to quaternion multiplication, so $\mathrm{SU}(2)$ is the group of unit [[Def - Quaternions|quaternions]], and $S^3 = \{q \in \mathbb{H} : |q| = 1\}$ inherits this Lie group structure. The fact that $S^3$ admits a Lie group structure is exceptional: among spheres, only $S^0, S^1, S^3$ are Lie groups (by Bott–Milnor–Kervaire), with the quaternion structure on $S^3$ being the third (and last) example.

**The double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ is the origin of spinors.**

The Lie correspondence on the simply-connected side: every $\mathfrak{so}(3) \cong \mathfrak{su}(2)$ representation integrates uniquely to a representation of $\mathrm{SU}(2)$ (the simply connected group). Only those representations whose value on $-I \in \mathrm{SU}(2)$ is the identity descend to representations of $\mathrm{SO}(3)$. The "half-integer spin" representations of $\mathfrak{su}(2)$ (those of even-dimensional weight spaces) fail this — for them, $\rho(-I) = -\mathrm{id}$, not $+\mathrm{id}$. Physically, a $2\pi$ rotation acts by $-1$ on a half-integer-spin state, the geometric origin of **spinors** in quantum mechanics. Electrons, quarks, and other fermions transform under spinor representations, which exist on $\mathrm{SU}(2)$ but not $\mathrm{SO}(3)$. The takeaway: the trivial-looking diffeomorphism $\mathrm{SU}(2) \cong S^3$ is the gateway to the entire theory of spinors and the Pauli exclusion principle.

**Computing Lie algebras by differentiation is universal.**

The pattern used here — substitute $U(t) = I + tX + O(t^2)$, expand to first order, read off the constraint — works for every classical matrix Lie group. For $\mathrm{SU}(n)$, the result is skew-Hermitian + traceless. For $\mathrm{Sp}(n)$, symplectic-compatibility. For the Lorentz group $\mathrm{O}(3, 1)$, the corresponding Lorentz-algebra condition. The technique is mechanical, and once internalized, one can compute the Lie algebra of any classical matrix group in under a minute. The trigger: a matrix Lie group is given by polynomial constraints; differentiate at $I$ to find $\mathfrak{g}$.

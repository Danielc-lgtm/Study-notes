---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Norm Induced by an Inner Product"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F}$. The relation $u \perp v$ reads "$u$ is orthogonal (or perpendicular) to $v$". A list of vectors $e_1, \dots, e_m$ uses subscripts to index entries; the **Kronecker delta** $\delta_{jk}$ equals $1$ if $j = k$ and $0$ otherwise. See [[Linear Algebra VI — §6 Inner Product Spaces]] for the full notation registry.

This is a compound page: it defines two interlocking notions — **orthogonality** of a pair of vectors, and **orthonormality** of a list of vectors — because the second is built on the first and neither is fully usable without the other.

---

# Axiom Motivation

The thing we are trying to axiomatize is **perpendicularity**, the relation between two vectors that meet at a right angle. In $\mathbb{R}^2$ with the dot product, two vectors are perpendicular precisely when their dot product is zero: the vectors $(1, 0)$ and $(0, 1)$ are perpendicular and $(1, 0) \cdot (0, 1) = 0$. The vectors $(1, 1)$ and $(1, -1)$ are perpendicular and $(1, 1) \cdot (1, -1) = 0$. The conjecture, then, is that "$\langle u, v\rangle = 0$" is the right algebraic generalization of "the angle between $u$ and $v$ is $90°$" to any inner product space, and the Cauchy-Schwarz inequality justifies this: $\langle u, v\rangle = \|u\|\,\|v\| \cos\theta$ in the $\mathbb{R}^2$ case, so $\langle u, v\rangle = 0$ corresponds exactly to $\cos\theta = 0$. We promote this to a definition: $u \perp v$ means $\langle u, v\rangle = 0$.

Note the order does not matter: $\langle u, v\rangle = 0$ if and only if $\langle v, u\rangle = \overline{\langle u, v\rangle} = 0$. So orthogonality is symmetric. The zero vector is orthogonal to *everything*, because $\langle 0, v\rangle = 0$ always (linearity); conversely, $\langle v, v\rangle = 0$ forces $v = 0$ by definiteness, so the zero vector is the only vector orthogonal to itself.

Now move from a pair to a list. We want lists of vectors that are mutually orthogonal — a "perpendicular frame" — and we additionally want each vector to have unit length, so that the geometry is fully normalised. If we have such a list $e_1, \dots, e_m$, then for any vector $v$, computing $\langle v, e_k\rangle$ extracts something like "the $k$-th coordinate of $v$ in this frame". This is the geometric intuition that motivates **orthonormality**: a list of vectors that are pairwise orthogonal and each of unit length. The compact algebraic statement is $\langle e_j, e_k\rangle = \delta_{jk}$, where the Kronecker delta packages "1 on the diagonal, 0 off-diagonal" into a single symbol.

Why both *orthogonal* and *unit length*? Without orthogonality, the inner products $\langle v, e_k\rangle$ pick up cross-terms and the expansion-coefficient formula $v = \sum_k \langle v, e_k\rangle e_k$ breaks. Without unit length, the formula picks up unwanted $\|e_k\|^2$ factors: $v = \sum_k \langle v, e_k\rangle / \|e_k\|^2 \cdot e_k$, which is correct but bookkeeping-heavy. Imposing both makes the formula maximally clean.

Why not require orthonormality from the start of the definition of "orthogonal"? Because pairs of vectors can be orthogonal without being unit-length — the pair $(2, 0)$ and $(0, 3)$ is orthogonal in $\mathbb{R}^2$ — and forcing unit length would conflate the two notions. The clean separation is: **orthogonality** is the angle condition, **orthonormality** is orthogonality plus unit-length-of-each.

A reader could also ask: is there an axiom for orthogonality of a *list*? Yes — a list is **orthogonal** (without the "normal") if the vectors are pairwise orthogonal, *without* the unit-length requirement. The orthonormal lists are then the orthogonal lists in which each vector has norm $1$. The two-step definition mirrors the one-vs-many distinction, with normalisation always available as the cheap final step ($e_k = v_k / \|v_k\|$).

---

# The Definition

Let $V$ be an inner product space.

**Orthogonal vectors.** Two vectors $u, v \in V$ are **orthogonal** if $\langle u, v\rangle = 0$. This is written $u \perp v$.

**Orthonormal list.** A list of vectors $e_1, \dots, e_m$ in $V$ is **orthonormal** if every vector has norm $1$ and any two distinct vectors are orthogonal. Equivalently,

$$
\langle e_j, e_k\rangle = \delta_{jk} = \begin{cases} 1 & \text{if } j = k, \\ 0 & \text{if } j \neq k. \end{cases}
$$

**Orthogonal list.** A list $v_1, \dots, v_m$ in $V$ is **orthogonal** if the vectors are pairwise orthogonal, i.e. $\langle v_j, v_k\rangle = 0$ for $j \neq k$. (No normalisation is imposed.)

The relation $u \perp v$ is symmetric ($u \perp v \iff v \perp u$, because $\langle u, v\rangle = 0 \iff \overline{\langle u, v\rangle} = 0 \iff \langle v, u\rangle = 0$). The zero vector is orthogonal to every vector. The only vector orthogonal to itself is the zero vector.

---

# Relate to Other Fields / Compression

**Generalization to non-Euclidean settings.** In a [[Def - Minkowski Space and the Metric|Minkowski-space]] setting, "orthogonal" is defined the same way — $\langle u, v\rangle = 0$ — but with the indefinite metric, and the geometric meaning changes dramatically. A vector can be orthogonal to itself (lightlike vectors), and "orthogonal complement" no longer means "perpendicular" in the Euclidean sense. The algebraic definition transfers; the geometry does not.

**Connection to bases.** Orthonormal lists are special bases when they span: an **orthonormal basis** is an orthonormal list that is also a basis. The result that orthonormal lists are linearly independent (see [[Ex - Orthonormal lists are linearly independent]]) means that an orthonormal list of length $\dim V$ is automatically a basis.

**True name:** an orthonormal list is a list whose Gram matrix is the identity, where the Gram matrix is the $m \times m$ matrix with entries $G_{jk} = \langle e_j, e_k\rangle$. The general Gram matrix is positive semi-definite and positive-definite iff the vectors are linearly independent; orthonormality is the maximally clean case of "Gram matrix is the identity matrix".

---

# Examples / Corollaries

**Is an instance: the standard basis $e_1, \dots, e_n$ of $\mathbf{F}^n$.** Each $e_k$ has the $k$-th coordinate equal to $1$ and the rest $0$; with the Euclidean inner product, $\langle e_j, e_k\rangle = \delta_{jk}$. This is the prototype orthonormal basis.

**Is an instance: $(\cos\theta, \sin\theta), (-\sin\theta, \cos\theta)$ in $\mathbb{R}^2$.** For any $\theta$, this rotated pair is an orthonormal basis of $\mathbb{R}^2$. Compute: $\cos^2\theta + \sin^2\theta = 1$ gives both norms equal to $1$, and $\cos\theta \cdot (-\sin\theta) + \sin\theta \cdot \cos\theta = 0$ gives orthogonality. Every orthonormal basis of $\mathbb{R}^2$ is of this form (or this form with a reflection).

**Is an instance: trigonometric functions on $[-\pi, \pi]$.** With $\langle f, g\rangle = \int_{-\pi}^\pi fg$, the list $\tfrac{1}{\sqrt{2\pi}}, \tfrac{\cos x}{\sqrt{\pi}}, \tfrac{\sin x}{\sqrt{\pi}}, \tfrac{\cos 2x}{\sqrt{\pi}}, \tfrac{\sin 2x}{\sqrt{\pi}}, \dots$ is orthonormal in $C[-\pi, \pi]$. The orthogonality comes from product-to-sum identities ($\sin nx \sin mx = \tfrac{1}{2}(\cos(n-m)x - \cos(n+m)x)$ and similar), each of which integrates to zero on $[-\pi, \pi]$ when $n \neq m$. This is the orthonormal basis underlying Fourier series.

**Is an instance: the four vectors $\tfrac{1}{2}(\pm 1, \pm 1, \pm 1, \pm 1)$ in $\mathbb{R}^4$, with appropriate sign choices.** LADR example 6.29 gives one such basis: $(\tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}), (\tfrac{1}{2}, \tfrac{1}{2}, -\tfrac{1}{2}, -\tfrac{1}{2}), (\tfrac{1}{2}, -\tfrac{1}{2}, -\tfrac{1}{2}, \tfrac{1}{2}), (-\tfrac{1}{2}, \tfrac{1}{2}, -\tfrac{1}{2}, \tfrac{1}{2})$. These appear in coding theory as the rows of a Hadamard matrix, scaled to unit norm.

**Is NOT an instance: $(1, 0)$ and $(1, 1)$ in $\mathbb{R}^2$.** These are linearly independent and each has norm $\geq 1$, but $\langle (1,0), (1,1)\rangle = 1 \neq 0$, so they are not orthogonal. This non-example highlights that "linearly independent" is strictly weaker than "orthogonal".

**Is NOT an instance: $(1, 0)$ and $(0, 2)$ in $\mathbb{R}^2$.** Orthogonal, since $\langle (1,0), (0,2)\rangle = 0$, but the second vector has norm $2$, not $1$. So this is orthogonal but not orthonormal. To make it orthonormal, normalise: $(1, 0)$ and $(0, 1)$.

**Is NOT an instance: any list containing the zero vector.** The zero vector has norm $0$, not $1$, so cannot belong to an orthonormal list. Any orthonormal list has all vectors of norm exactly $1$, hence all are nonzero.

**Corollary (norm of an orthonormal combination).** If $e_1, \dots, e_m$ is orthonormal and $a_1, \dots, a_m \in \mathbf{F}$, then
$$
\|a_1 e_1 + \cdots + a_m e_m\|^2 = |a_1|^2 + \cdots + |a_m|^2.
$$
This is repeated application of the Pythagorean theorem: each pair of terms $a_j e_j, a_k e_k$ for $j \neq k$ is orthogonal, and $\|a_k e_k\|^2 = |a_k|^2 \|e_k\|^2 = |a_k|^2$. It is the formula for the squared length of a vector expressed in orthonormal coordinates.

**Corollary (orthonormal expansion).** If $e_1, \dots, e_n$ is an orthonormal basis of $V$, then for every $v \in V$,
$$
v = \langle v, e_1\rangle e_1 + \cdots + \langle v, e_n\rangle e_n,
$$
with $\|v\|^2 = |\langle v, e_1\rangle|^2 + \cdots + |\langle v, e_n\rangle|^2$ (**Parseval's identity**). The coefficients $\langle v, e_k\rangle$ are the "coordinates" of $v$ in the orthonormal basis, and they are computed by a single inner product each — no linear-equation-solving required.

**Calibration check.** Three verifications: (i) the standard basis of $\mathbf{F}^n$ is orthonormal — check $\langle e_j, e_k\rangle$ directly; (ii) the list $(1, 1), (1, -1)$ in $\mathbb{R}^2$ is *orthogonal* but not orthonormal — each vector has norm $\sqrt{2}$, not $1$; normalize to get an orthonormal basis; (iii) for $f(x) = 1$ and $g(x) = x$ on $[-1, 1]$ with $\langle f, g\rangle = \int fg$, compute $\langle f, g\rangle = 0$ (since the integrand is odd) — so $1$ and $x$ are orthogonal, but not orthonormal because $\|1\|^2 = 2$ and $\|x\|^2 = 2/3$.

---

# Unlocked by This

> [!tip] Orthogonal Group $O(n)$ and Unitary Group $U(n)$ *(from Lie Theory and Physics)*
> The **orthogonal group** $O(n)$ is the group of linear isometries of $\mathbb{R}^n$ — equivalently, the group of real $n \times n$ matrices whose columns form an orthonormal basis. Its complex analogue is the **unitary group** $U(n)$. These are compact Lie groups of central importance: they are the rotation symmetry groups of Euclidean and Hermitian geometry, the gauge groups of much of physics, and the structure groups of the orthonormal frame bundle in Riemannian geometry. Every linear isometry of an $n$-dimensional inner product space is, in some orthonormal basis, an element of $O(n)$ or $U(n)$.

> [!tip] Quantum Mechanics Basis States *(from Physics)*
> In quantum mechanics, the state space of a system is a Hilbert space, and orthonormal bases play a privileged role: each orthonormal basis corresponds to a maximal set of mutually exclusive measurement outcomes. The expansion $|\psi\rangle = \sum_k c_k |e_k\rangle$ has coefficients $c_k = \langle e_k|\psi\rangle$ whose squared moduli $|c_k|^2$ are the probabilities of observing outcome $k$ in a measurement in that basis. The completeness $\sum_k |c_k|^2 = 1$ (Parseval) is the statement that probabilities sum to one. Different orthonormal bases correspond to different (non-commuting) observables, and the change-of-basis between them is the heart of quantum measurement theory.

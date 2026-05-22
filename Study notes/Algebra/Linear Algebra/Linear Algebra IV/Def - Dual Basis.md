---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Basis"
  - "Def - Linear Map"
  - "Def - Dual Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional vector space over $\mathbb{F}$ with basis $v_1, \dots, v_n$. The **dual basis** is the list $\varphi_1, \dots, \varphi_n$ of [[Def - Dual Space|linear functionals]] in $V'$ characterised by $\varphi_j(v_k) = \delta_{jk}$, where $\delta_{jk} = 1$ if $j = k$ and $0$ otherwise (the *Kronecker delta*). Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

---

# Axiom Motivation

The dual basis exists to answer one question: *given a basis $v_1, \dots, v_n$ of $V$, what is the corresponding "coordinate-extracting" basis of $V'$?*

A basis of $V$ does two jobs simultaneously: it provides a list of vectors that span $V$ and are independent (the "constructive" face), and it provides a *coordinate system* — every $v \in V$ can be written uniquely as $v = c_1 v_1 + \cdots + c_n v_n$, and the scalars $c_1, \dots, c_n$ are the coordinates. The dual basis isolates the coordinate-extracting face: we want functionals $\varphi_1, \dots, \varphi_n$ that *read off* the coordinates.

For this we need $\varphi_j$ to extract the $j$-th coordinate. That is, applied to a vector $v = c_1 v_1 + \cdots + c_n v_n$, it should return $c_j$. Plugging in: $\varphi_j(v_k) = \varphi_j(0 \cdot v_1 + \cdots + 1 \cdot v_k + \cdots + 0 \cdot v_n) = 0$ if $k \neq j$ and $1$ if $k = j$. So the defining property is exactly $\varphi_j(v_k) = \delta_{jk}$.

Does such a $\varphi_j$ exist? Yes — by the [[Def - Linear Map|linear-map extension lemma]]: a linear map out of $V$ is determined freely by its action on a basis. We specify $\varphi_j$ on each $v_k$ separately (sending $v_j$ to $1$ and all other $v_k$ to $0$), and the lemma extends this prescription to a unique linear map $\varphi_j : V \to \mathbb{F}$. So the dual basis exists and is uniquely determined by the basis of $V$ that we started from.

Is it a basis of $V'$? This is the theorem (see Examples below): the dual basis is linearly independent in $V'$, has $n$ elements, and $\dim V' = n$, so it is a basis of $V'$. The name "dual basis" is therefore justified.

What is essential about $\varphi_j(v_k) = \delta_{jk}$? It says the dual basis is *biorthogonal* to the basis of $V$: $\varphi_j$ pairs with $v_j$ to give $1$, and with every other $v_k$ to give $0$. The biorthogonality relation is what makes the dual basis a *coordinate system on $V'$*: any functional $\psi \in V'$ can be expanded as
$$\psi = \psi(v_1) \varphi_1 + \cdots + \psi(v_n) \varphi_n$$
because both sides agree on the basis $v_1, \dots, v_n$, and a linear functional is determined by its values on a basis. So $\psi(v_k)$ are the coordinates of $\psi$ in the dual basis. The roles of $V$ and $V'$ are dual to each other — coordinates of a vector are values of dual-basis functionals, and coordinates of a functional are values on basis vectors.

What if we tried to define a different basis of $V'$, say one that depends on $V$ in a "natural" way without choosing a basis? You cannot: every basis of $V'$ requires you to pick a basis of $V$ first. In particular, $V$ and $V'$ are isomorphic but the isomorphism is *not canonical* — it depends on the choice of basis of $V$. This is the cleanest first instance of *natural vs unnatural isomorphism* in linear algebra (see [[Ex - Double dual is naturally isomorphic to the original]]).

---

# The Definition

Let $V$ be a finite-dimensional vector space over $\mathbb{F}$ and $v_1, \dots, v_n$ a basis of $V$. The **dual basis** of $v_1, \dots, v_n$ is the list $\varphi_1, \dots, \varphi_n$ of linear functionals in $V' = \mathcal{L}(V, \mathbb{F})$ defined by the conditions
$$\varphi_j(v_k) = \delta_{jk} = \begin{cases} 1 & \text{if } k = j, \\ 0 & \text{if } k \neq j, \end{cases} \qquad j, k \in \{1, \dots, n\}.$$
Each $\varphi_j$ is uniquely determined by these conditions via the linear-map extension lemma applied to the basis $v_1, \dots, v_n$.

The list $\varphi_1, \dots, \varphi_n$ is a basis of $V'$ ([[Thm - Dimension of Dual Space]]).

The dual basis has the **coordinate-extraction property**: for every $v \in V$,
$$v = \varphi_1(v) v_1 + \varphi_2(v) v_2 + \cdots + \varphi_n(v) v_n.$$
That is, the scalars $\varphi_j(v)$ are exactly the coordinates of $v$ in the basis $v_1, \dots, v_n$.

The dual basis has the **dual coordinate-extraction property**: for every $\psi \in V'$,
$$\psi = \psi(v_1) \varphi_1 + \psi(v_2) \varphi_2 + \cdots + \psi(v_n) \varphi_n.$$
The scalars $\psi(v_k)$ are the coordinates of $\psi$ in the dual basis $\varphi_1, \dots, \varphi_n$.

The two formulas are duals of each other; one is the "$\varphi_j$ reads coordinates of $v$" identity, the other is the "$v_k$ reads coordinates of $\psi$" identity (where we use the [[Ex - Double dual is naturally isomorphic to the original|double dual]] identification of $v_k$ with the evaluation functional on $V'$).

---

# Relate to Other Fields / Compression

The dual basis is the **biorthogonal basis** in the sense of $\langle \varphi_j, v_k \rangle = \delta_{jk}$ under the natural pairing $V' \times V \to \mathbb{F}$, $(\varphi, v) \mapsto \varphi(v)$. The biorthogonality relation is the basic identity from which all explicit computations with duals flow.

In coordinates, the dual basis of the standard basis $e_1, \dots, e_n$ of $\mathbb{F}^n$ is the list of coordinate projections $\varphi_j(x_1, \dots, x_n) = x_j$. The matrix of $\varphi_j$ with respect to standard bases is the row vector with $1$ in position $j$ and $0$ elsewhere. *Linear functionals are row vectors* in coordinates, while vectors are column vectors, and the pairing $\varphi(v)$ is the row-times-column product.

In inner product spaces, the dual basis has a particularly clean form: if $v_1, \dots, v_n$ is an [[Def - Orthonormal Basis|orthonormal basis]] of an inner product space $V$, then the dual basis is $\varphi_j(v) = \langle v, v_j \rangle$ (the [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation]] — see [[Linear Algebra VI — §6 Inner Product Spaces|Chapter 6]]). In this setting the dual basis is *induced* by the inner product rather than chosen by hand.

**True name:** the dual basis is the *coordinate functionals* of a chosen basis — the functionals $\varphi_j$ that extract the $j$-th coordinate of a vector with respect to the basis $v_1, \dots, v_n$.

---

# Examples / Corollaries

**Is an instance — dual basis of the standard basis of $\mathbb{F}^n$.** Let $e_1, \dots, e_n$ be the standard basis of $\mathbb{F}^n$. The dual basis is $\varphi_1, \dots, \varphi_n$ with $\varphi_j(x_1, \dots, x_n) = x_j$. Check biorthogonality: $\varphi_j(e_k) = \delta_{jk}$ by construction. So the dual basis of the standard basis is the list of coordinate projections, and the matrix of $\varphi_j$ is the row vector $(0, \dots, 1, \dots, 0)$ with $1$ in position $j$.

**Is an instance — dual basis of $1, x, x^2$ in $\mathcal{P}_2(\mathbb{R})$.** Let $V = \mathcal{P}_2(\mathbb{R})$, the polynomials of degree at most $2$, with basis $v_0 = 1, v_1 = x, v_2 = x^2$. By the coordinate-extraction property, a polynomial $p(x) = a_0 + a_1 x + a_2 x^2$ should satisfy $\varphi_j(p) = a_j$. Using Taylor's formula at $0$: $a_j = p^{(j)}(0) / j!$. So the dual basis is
$$\varphi_0(p) = p(0), \quad \varphi_1(p) = p'(0), \quad \varphi_2(p) = \tfrac{1}{2} p''(0).$$
Verify: $\varphi_0(1) = 1, \varphi_0(x) = 0, \varphi_0(x^2) = 0$; $\varphi_1(1) = 0, \varphi_1(x) = 1, \varphi_1(x^2) = 0$; $\varphi_2(1) = 0, \varphi_2(x) = 0, \varphi_2(x^2) = 1$. The biorthogonality holds.

**Is an instance — dual basis of $1, x - 5, (x-5)^2$.** A shifted basis of $\mathcal{P}_2(\mathbb{R})$. By the same Taylor argument at $a = 5$, the dual basis is $\varphi_j(p) = p^{(j)}(5)/j!$. So $\varphi_0(p) = p(5)$, $\varphi_1(p) = p'(5)$, $\varphi_2(p) = p''(5)/2$. Different basis of $V$, different dual basis of $V'$ — the dual basis depends on the basis you start from.

**Is NOT a basis of $V$ — the dual basis lives in $V'$, not $V$.** The dual basis $\varphi_1, \dots, \varphi_n$ is a basis of the *dual space* $V'$, not of $V$ itself. A common slip is to conflate the two. The vectors $v_j$ live in $V$; the functionals $\varphi_j$ live in $V'$; the biorthogonality pairing $\varphi_j(v_k) = \delta_{jk}$ pairs across the two spaces.

**Is NOT canonical — the dual basis depends on the choice of basis.** There is no canonical (basis-independent) basis of $V'$. Two different bases of $V$ give two different dual bases. This is the contrast with the [[Ex - Double dual is naturally isomorphic to the original|double dual]], where the canonical evaluation map $\Lambda : V \to V''$ does not require choosing a basis.

**Corollary — the coordinate-extraction formula.** For $v = \sum_k c_k v_k$, applying $\varphi_j$ gives $\varphi_j(v) = \sum_k c_k \varphi_j(v_k) = c_j$. So $\varphi_j(v)$ is the $j$-th coordinate of $v$, confirming the coordinate-extraction property. The formula $v = \sum_j \varphi_j(v) v_j$ is the universal "expand in this basis" identity.

**Corollary — the dual coordinate-extraction formula.** For any $\psi \in V'$, the values $\psi(v_1), \dots, \psi(v_n)$ are the coordinates of $\psi$ in the dual basis. Proof: both $\psi$ and $\sum_j \psi(v_j) \varphi_j$ are linear functionals on $V$; they agree on each $v_k$ (the right-hand side gives $\sum_j \psi(v_j) \delta_{jk} = \psi(v_k)$); two linear functionals agreeing on a basis are equal. So $\psi = \sum_j \psi(v_j) \varphi_j$.

**Corollary — change of basis dualises contravariantly.** If $v_1, \dots, v_n$ and $w_1, \dots, w_n$ are two bases of $V$ with change of basis matrix $A$ (so $w_k = \sum_j A_{jk} v_j$), then the corresponding dual bases $\varphi_1, \dots, \varphi_n$ and $\psi_1, \dots, \psi_n$ are related by the *inverse-transpose* of $A$. This is the structural source of contravariance for the dual: vectors transform by $A$, but their measurements transform by $(A^{-1})^t$.

**Calibration check.** Verify that for a basis $v_1, \dots, v_n$, applying $\varphi_j$ to $v_k$ gives $\delta_{jk}$. Confirm the coordinate-extraction identity $v = \sum_j \varphi_j(v) v_j$ for a specific vector — for instance $v = 2 v_1 + 3 v_2$, checking $\varphi_1(v) = 2$ and $\varphi_2(v) = 3$. Confirm the dual identity $\psi = \sum_j \psi(v_j) \varphi_j$ for a specific functional.

---

# Unlocked by This

> [!tip] Matrix of the Dual Map *(from this topic)*
> With dual bases in hand, you can write down the matrix of the [[Def - Dual Map|dual map]] $T'$ in the dual bases of bases of $V$ and $W$. The astonishing fact is that this matrix is exactly the *transpose* of the matrix of $T$ — see [[Thm - Matrix of Dual Map is Transpose]]. This is the structural source of the transpose operation in linear algebra.

> [!tip] Trace as a Dual-Basis Sum *(from Linear Algebra VIII)*
> The trace $\operatorname{tr}(A) = \sum_k A_{kk}$ of a matrix can be written as $\operatorname{tr}(T) = \sum_k \varphi_k(T(v_k))$ where $\varphi_k$ is the dual basis of $v_k$. This shows the trace is independent of the basis chosen, since both $v_k$ and $\varphi_k$ change consistently — see [[Def - Trace]] in [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces|Chapter 8]].

> [!tip] Differential Forms *(from Differential Geometry)*
> If $x^1, \dots, x^n$ are local coordinates on a manifold, then $\partial / \partial x^1, \dots, \partial / \partial x^n$ is a basis of the tangent space at each point, and the dual basis $dx^1, \dots, dx^n$ is a basis of the **cotangent space**. The differentials $dx^j$ are the basic 1-forms, and tensor products of them give all higher-rank forms. The biorthogonality $dx^j(\partial / \partial x^k) = \delta_{jk}$ is the foundational identity of differential geometry.

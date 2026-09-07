---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Ad is a Smooth Representation and its Differential is ad"
  - "Ex - su(2) in the Basis of Anti-Hermitian Pauli Matrices"
  - "Def - Adjoint Representation"
  - "Def - Representation of a Lie Group"
tags: [geometry, gauge-theory]
---

# Problem Statement

We work throughout in the special unitary group $SU(2) = \{g \in \operatorname{Mat}(2\times 2;\mathbb{C}) : g^{*}g = 1_2,\ \det g = 1\}$ and its Lie algebra
$$\mathfrak{su}(2) = \{X \in \operatorname{Mat}(2\times 2;\mathbb{C}) : X^{*} = -X,\ \operatorname{tr}X = 0\} = \left\{\begin{pmatrix} it & z \\ -\bar z & -it\end{pmatrix} : z \in \mathbb{C},\ t \in \mathbb{R}\right\},$$
a real three-dimensional vector space. Here $g^{*} = \bar g^{\,\mathsf{T}}$ is the conjugate transpose and $1_2$ is the $2\times 2$ identity. Fix, following Bär's Example 1.3.8, the basis of $\mathfrak{su}(2)$ consisting of $-i$ times the three Pauli matrices,
$$E_1 := -i\sigma_1 = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}, \qquad E_2 := -i\sigma_2 = \begin{pmatrix} 0 & i \\ i & 0\end{pmatrix}, \qquad E_3 := -i\sigma_3 = \begin{pmatrix} i & 0 \\ 0 & -i\end{pmatrix}.$$

The **adjoint representation** $\operatorname{Ad} : SU(2) \to GL(\mathfrak{su}(2))$ sends $g$ to the linear map $\operatorname{Ad}_g : \mathfrak{su}(2) \to \mathfrak{su}(2)$, $X \mapsto gXg^{-1}$.

**Part (a).** For the one-parameter family of diagonal elements
$$g_\varphi := \begin{pmatrix} e^{i\varphi} & 0 \\ 0 & e^{-i\varphi}\end{pmatrix} \in SU(2), \qquad \varphi \in \mathbb{R},$$
compute $\operatorname{Ad}_{g_\varphi}(E_1)$, $\operatorname{Ad}_{g_\varphi}(E_2)$, $\operatorname{Ad}_{g_\varphi}(E_3)$, and show that with respect to the ordered basis $(E_1, E_2, E_3)$ the operator $\operatorname{Ad}_{g_\varphi}$ has matrix
$$[\operatorname{Ad}_{g_\varphi}] = \begin{pmatrix} \cos 2\varphi & -\sin 2\varphi & 0 \\ \sin 2\varphi & \cos 2\varphi & 0 \\ 0 & 0 & 1\end{pmatrix},$$
the rotation by the angle $2\varphi$ in the plane spanned by $E_1$ and $E_2$, fixing $E_3$.

**Part (b).** Deduce that the adjoint representation of $SU(2)$ is not faithful, and compute its kernel exactly:
$$\ker \operatorname{Ad} = \{\, g \in SU(2) : \operatorname{Ad}_g = \operatorname{id}_{\mathfrak{su}(2)} \,\} = \{+1_2,\, -1_2\}.$$

**Recall:**

The objects in play are the special unitary group and its Lie algebra, the adjoint representation, the fact that on a matrix group the adjoint action is conjugation, and the basis $E_1, E_2, E_3$ of $\mathfrak{su}(2)$.

![[Def - Representation of a Lie Group#The Definition]]

A [[Def - Representation of a Lie Group|representation]] of a Lie group $G$ is a Lie group homomorphism $\varrho : G \to GL(V)$ into the automorphisms of a finite-dimensional vector space $V$; it is **faithful** when $\varrho$ is injective, equivalently when $\ker\varrho = \{e\}$.

![[Thm - Ad is a Smooth Representation and its Differential is ad#Statement]]

The single fact from that theorem used below is part (ii): for a matrix group $G \subset GL(n;\mathbb{K})$ and $X \in \mathfrak{g}$,
$$\operatorname{Ad}_g X = g X g^{-1},$$
so that for $SU(2)$ the adjoint action is honest conjugation of matrices. The map $\operatorname{Ad} : G \to GL(\mathfrak{g})$ is a genuine representation — in particular $\operatorname{Ad}_{gh} = \operatorname{Ad}_g \operatorname{Ad}_h$ and $\operatorname{Ad}_e = \operatorname{id}$ — so its kernel is a subgroup, and computing it is a well-posed question.

The basis $E_1 = -i\sigma_1$, $E_2 = -i\sigma_2$, $E_3 = -i\sigma_3$ of $\mathfrak{su}(2)$ is verified to be a basis of the real vector space $\mathfrak{su}(2)$ in [[Ex - su(2) in the Basis of Anti-Hermitian Pauli Matrices|the companion exercise on the Pauli basis]]; there one also checks the bracket relations $[E_a, E_b] = 2\,\varepsilon_{abc}\,E_c$. We take the basis as given here and use only that $\{E_1, E_2, E_3\}$ is linearly independent and spans $\mathfrak{su}(2)$ over $\mathbb{R}$, so that a linear operator on $\mathfrak{su}(2)$ is determined by its values on the three $E_a$ and represented by the $3\times 3$ matrix whose columns are the coordinate vectors of those values.

> [!warning] Convention: Bär's labelling of the Pauli matrices
> The three matrices displayed above are exactly Bär's $-i\sigma_1, -i\sigma_2, -i\sigma_3$ from Example 1.3.8, and we keep his labels so that every equation matches the source line for line. Relative to the **standard** physics Pauli matrices $\sigma_1 = \left(\begin{smallmatrix} 0 & 1 \\ 1 & 0\end{smallmatrix}\right)$, $\sigma_2 = \left(\begin{smallmatrix} 0 & -i \\ i & 0\end{smallmatrix}\right)$, $\sigma_3 = \left(\begin{smallmatrix} 1 & 0 \\ 0 & -1\end{smallmatrix}\right)$, Bär's printed $\sigma_1$ and $\sigma_2$ are interchanged (his $-i\sigma_1 = \left(\begin{smallmatrix} 0 & 1 \\ -1 & 0\end{smallmatrix}\right)$ equals the standard $\sigma_1$ after multiplying by $-i$ only up to this swap). Nothing in this exercise depends on which convention is chosen: the three matrices $E_1, E_2, E_3$ form a real basis of $\mathfrak{su}(2)$ either way, and the computation uses only their explicit entries. The relabelling is recorded in full on [[Ex - su(2) in the Basis of Anti-Hermitian Pauli Matrices|the Pauli-basis exercise]].

---

# Convergent Strategy

**Problem class.** This is a *represent-an-abstract-operator-as-a-matrix* problem: we are handed a linear operator (the adjoint action $\operatorname{Ad}_{g_\varphi}$ on the three-dimensional space $\mathfrak{su}(2)$) defined by an intrinsic formula, and asked to write down its matrix in a chosen basis and then read structural information — here the kernel of a homomorphism — off that matrix. Such problems always reduce to two mechanical acts followed by one interpretive act: evaluate the operator on each basis vector, assemble the coordinate columns into a matrix, and then recognise the matrix.

**Assumption pattern.** The decisive simplification is that $SU(2)$ is a *matrix* group, so the adjoint representation is not an abstract differential of a conjugation map but literal matrix conjugation $X \mapsto g X g^{-1}$. The recognisable trigger is the phrase "adjoint representation of a classical matrix group": whenever it appears, one immediately replaces $\operatorname{Ad}_g$ by $g(\cdot)g^{-1}$, converting a question about differentials into a question about multiplying three explicit $2\times 2$ matrices. The second standing feature is that $g_\varphi$ is *diagonal*; conjugating by a diagonal matrix rescales the off-diagonal entries by ratios of the diagonal entries and fixes the diagonal ones, which is exactly why the answer is a rotation.

**Theorem routing.** The route is: invoke [[Thm - Ad is a Smooth Representation and its Differential is ad|part (ii) of the adjoint-representation theorem]] to write $\operatorname{Ad}_{g_\varphi}(E_a) = g_\varphi E_a g_\varphi^{-1}$; compute each of the three conjugations as a product of three $2\times 2$ matrices, using $g_\varphi^{-1} = \operatorname{diag}(e^{-i\varphi}, e^{i\varphi})$ (the inverse of a special unitary diagonal matrix is its conjugate transpose); re-express each result in the basis $(E_1, E_2, E_3)$ using $e^{\pm 2i\varphi} = \cos 2\varphi \pm i\sin 2\varphi$; collect the coordinate columns into the $3\times 3$ matrix; and finally, for part (b), solve $\operatorname{Ad}_g = \operatorname{id}$ directly as the system of commutation equations $g E_a = E_a g$ for $a = 1, 2, 3$.

**Key decision point.** Two moves carry the exercise. First, the choice to convert $\operatorname{Ad}_{g_\varphi}$ into conjugation *before* doing anything else: without the matrix-group identity one is stuck differentiating $\alpha_{g_\varphi}$ at the identity, whereas with it the whole of part (a) is three lines of matrix arithmetic. Second, in part (b), the recognition that "$\operatorname{Ad}_g = \operatorname{id}$" means "$g$ commutes with every element of $\mathfrak{su}(2)$", and that it suffices to impose commuting with the three basis matrices $E_1, E_2, E_3$; commuting with the diagonal $E_3$ (which has distinct eigenvalues $i, -i$) forces $g$ diagonal, and then commuting with the off-diagonal $E_1$ forces the two diagonal entries equal. The genuine insight is that the kernel of $\operatorname{Ad}$ is the *centre* of the group, and the centre is pinned down by a short eigenvalue argument rather than by any appeal to abstract representation theory.

---

# Legal Operations Used

The topic page for §1.3 is not yet assembled; the operations below are named descriptively and the chapter's Legal Operations list will absorb them.

1. **Replace the adjoint action of a matrix group by conjugation.** Because $SU(2) \subset GL(2;\mathbb{C})$ is a matrix group, $\operatorname{Ad}_g X = g X g^{-1}$ by part (ii) of [[Thm - Ad is a Smooth Representation and its Differential is ad|the adjoint-representation theorem]]. This is the operation that turns the problem into arithmetic.

2. **Invert a special unitary diagonal matrix by conjugate transposition.** For $g_\varphi = \operatorname{diag}(e^{i\varphi}, e^{-i\varphi}) \in SU(2)$ we have $g_\varphi^{-1} = g_\varphi^{*} = \operatorname{diag}(e^{-i\varphi}, e^{i\varphi})$, since $g^{*}g = 1_2$ is the defining relation of the unitary group.

3. **Read a linear operator off its action on a basis.** An operator $T : \mathfrak{su}(2) \to \mathfrak{su}(2)$ is determined by the three vectors $T(E_1), T(E_2), T(E_3)$; its matrix in the basis $(E_1, E_2, E_3)$ has these as its columns, expressed in coordinates. This is the operation that produces the $3\times 3$ matrix.

4. **Convert exponentials to trigonometric coordinates.** Use $e^{\pm 2i\varphi} = \cos 2\varphi \pm i\sin 2\varphi$ to split each conjugated matrix into its $E_1$- and $E_2$-components with real coefficients.

5. **Solve a kernel as a commutation problem, one basis matrix at a time.** The condition $\operatorname{Ad}_g = \operatorname{id}_{\mathfrak{su}(2)}$ is $g E_a g^{-1} = E_a$, i.e. $g E_a = E_a g$, for $a = 1, 2, 3$; impose these in turn (the diagonal $E_3$ first, to force $g$ diagonal; then $E_1$, to force the entries equal), and finally use $\det g = 1$.

---

# Hints

> [!note]- Hint 1
> Do not differentiate anything. $SU(2)$ is a matrix group, so the adjoint action of $g$ on $X \in \mathfrak{su}(2)$ is just $gXg^{-1}$. Write $g_\varphi^{-1}$ first, then compute the three products $g_\varphi E_a g_\varphi^{-1}$ as ordinary matrix multiplications.

> [!note]- Hint 2
> Conjugating a matrix by a *diagonal* matrix $\operatorname{diag}(d_1, d_2)$ multiplies the $(j,k)$ entry by $d_j / d_k$. So the diagonal entries of $E_a$ are unchanged and the off-diagonal entries pick up $e^{\pm 2i\varphi}$. That is already almost the whole computation; only $E_1$ and $E_2$ move, and $E_3$ (diagonal) is fixed.

> [!note]- Hint 3
> To recognise the answer as a rotation, expand $e^{2i\varphi} = \cos 2\varphi + i\sin 2\varphi$ and match the result against $\cos 2\varphi\,E_1 + \sin 2\varphi\,E_2$. The columns of the $3\times 3$ matrix are the coordinate vectors of $\operatorname{Ad}_{g_\varphi}(E_1)$, $\operatorname{Ad}_{g_\varphi}(E_2)$, $\operatorname{Ad}_{g_\varphi}(E_3)$ in that order.

> [!note]- Hint 4
> For the kernel: $\operatorname{Ad}_g = \operatorname{id}$ says $g$ commutes with all of $\mathfrak{su}(2)$, hence with $E_1, E_2, E_3$. Start with $E_3 = \operatorname{diag}(i, -i)$: a matrix commuting with a diagonal matrix that has *distinct* diagonal entries must itself be diagonal. Then use $E_1$ to force the two diagonal entries of $g$ to be equal, and finish with $\det g = 1$.

---

# Solution

The plan is short. Part (a) is a direct computation: convert $\operatorname{Ad}_{g_\varphi}$ to conjugation, multiply the three $2\times 2$ matrices $g_\varphi E_a g_\varphi^{-1}$, and rewrite each answer in the basis $(E_1, E_2, E_3)$, where the trigonometric form of $e^{\pm 2i\varphi}$ makes the rotation visible. Part (b) reads the kernel of $\operatorname{Ad}$ off the requirement that $g$ commute with the three basis matrices: $E_3$ forces $g$ diagonal, $E_1$ forces its entries equal, and $\det g = 1$ leaves only $g = \pm 1_2$.

**Step 1: Reduce the adjoint action to conjugation and record the inverse of $g_\varphi$.**

By part (ii) of the adjoint-representation theorem, $\operatorname{Ad}_{g_\varphi}(X) = g_\varphi X g_\varphi^{-1}$ for every $X \in \mathfrak{su}(2)$, and $g_\varphi^{-1} = \operatorname{diag}(e^{-i\varphi}, e^{i\varphi})$.

> [!note]- Derivation
> We are given $g_\varphi = \begin{pmatrix} e^{i\varphi} & 0 \\ 0 & e^{-i\varphi}\end{pmatrix} \in SU(2)$ and must compute $\operatorname{Ad}_{g_\varphi}(E_a)$ for $a = 1, 2, 3$.
>
> **Convert the adjoint action to conjugation.** Since $SU(2) \subset GL(2;\mathbb{C})$ is one of the classical matrix groups, part (ii) of [[Thm - Ad is a Smooth Representation and its Differential is ad|the adjoint-representation theorem]] gives, for every $X \in \mathfrak{su}(2)$,
> $$\operatorname{Ad}_{g_\varphi}(X) = g_\varphi\, X\, g_\varphi^{-1} \qquad \text{(part (ii) of the adjoint-representation theorem, matrix group).}$$
>
> **Compute the inverse.** The group $SU(2)$ is unitary, so $g_\varphi^{-1} = g_\varphi^{*} = \bar g_\varphi^{\,\mathsf{T}}$ (defining relation $g^{*}g = 1_2$). As $g_\varphi$ is diagonal, its conjugate transpose is obtained by conjugating each diagonal entry:
> $$g_\varphi^{-1} = \begin{pmatrix} \overline{e^{i\varphi}} & 0 \\ 0 & \overline{e^{-i\varphi}}\end{pmatrix} = \begin{pmatrix} e^{-i\varphi} & 0 \\ 0 & e^{i\varphi}\end{pmatrix} \qquad \text{(since } \overline{e^{i\varphi}} = e^{-i\varphi}\text{).}$$
> One checks directly that $g_\varphi\, g_\varphi^{-1} = \operatorname{diag}(e^{i\varphi}e^{-i\varphi},\, e^{-i\varphi}e^{i\varphi}) = \operatorname{diag}(1, 1) = 1_2$, confirming the inverse.

**Step 2: Conjugate $E_1$ and identify the result as $\cos 2\varphi\,E_1 + \sin 2\varphi\,E_2$.**

Direct multiplication gives $\operatorname{Ad}_{g_\varphi}(E_1) = \cos 2\varphi\,E_1 + \sin 2\varphi\,E_2$.

> [!note]- Derivation
> We multiply $g_\varphi E_1 g_\varphi^{-1}$ left to right. First,
> $$g_\varphi E_1 = \begin{pmatrix} e^{i\varphi} & 0 \\ 0 & e^{-i\varphi}\end{pmatrix}\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix} = \begin{pmatrix} 0 & e^{i\varphi} \\ -e^{-i\varphi} & 0\end{pmatrix} \qquad \text{(row } j \text{ of the product is } e^{\pm i\varphi} \text{ times row } j \text{ of } E_1\text{).}$$
> Then, multiplying on the right by $g_\varphi^{-1} = \operatorname{diag}(e^{-i\varphi}, e^{i\varphi})$ scales column $k$ by the $k$-th diagonal entry:
> $$g_\varphi E_1 g_\varphi^{-1} = \begin{pmatrix} 0 & e^{i\varphi} \\ -e^{-i\varphi} & 0\end{pmatrix}\begin{pmatrix} e^{-i\varphi} & 0 \\ 0 & e^{i\varphi}\end{pmatrix} = \begin{pmatrix} 0 & e^{2i\varphi} \\ -e^{-2i\varphi} & 0\end{pmatrix} \qquad \text{(the } (1,2) \text{ entry is } e^{i\varphi}\cdot e^{i\varphi}; \text{ the } (2,1) \text{ entry is } -e^{-i\varphi}\cdot e^{-i\varphi}\text{).}$$
> **Split into the basis.** Write $e^{2i\varphi} = \cos 2\varphi + i\sin 2\varphi$ and $e^{-2i\varphi} = \cos 2\varphi - i\sin 2\varphi$ (Euler's formula). Then
> $$\begin{pmatrix} 0 & e^{2i\varphi} \\ -e^{-2i\varphi} & 0\end{pmatrix} = \cos 2\varphi\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix} + \sin 2\varphi\begin{pmatrix} 0 & i \\ i & 0\end{pmatrix} \qquad \text{(matching entries: } (1,2)\!: \cos 2\varphi + i\sin 2\varphi = e^{2i\varphi}; \ (2,1)\!: -\cos 2\varphi + i\sin 2\varphi = -e^{-2i\varphi}\text{).}$$
> The two matrices on the right are exactly $E_1$ and $E_2$, so
> $$\operatorname{Ad}_{g_\varphi}(E_1) = \cos 2\varphi\,E_1 + \sin 2\varphi\,E_2.$$

**Step 3: Conjugate $E_2$ and identify the result as $-\sin 2\varphi\,E_1 + \cos 2\varphi\,E_2$.**

Direct multiplication gives $\operatorname{Ad}_{g_\varphi}(E_2) = \cos 2\varphi\,E_2 - \sin 2\varphi\,E_1$.

> [!note]- Derivation
> As in Step 2,
> $$g_\varphi E_2 = \begin{pmatrix} e^{i\varphi} & 0 \\ 0 & e^{-i\varphi}\end{pmatrix}\begin{pmatrix} 0 & i \\ i & 0\end{pmatrix} = \begin{pmatrix} 0 & i e^{i\varphi} \\ i e^{-i\varphi} & 0\end{pmatrix} \qquad \text{(scale row } j \text{ by } e^{\pm i\varphi}\text{),}$$
> and then, scaling column $k$ by the $k$-th entry of $g_\varphi^{-1}$,
> $$g_\varphi E_2 g_\varphi^{-1} = \begin{pmatrix} 0 & i e^{i\varphi} \\ i e^{-i\varphi} & 0\end{pmatrix}\begin{pmatrix} e^{-i\varphi} & 0 \\ 0 & e^{i\varphi}\end{pmatrix} = \begin{pmatrix} 0 & i e^{2i\varphi} \\ i e^{-2i\varphi} & 0\end{pmatrix} \qquad \text{(} (1,2)\!: i e^{i\varphi}\cdot e^{i\varphi};\ (2,1)\!: i e^{-i\varphi}\cdot e^{-i\varphi}\text{).}$$
> **Split into the basis.** Using $i e^{2i\varphi} = i(\cos 2\varphi + i\sin 2\varphi) = -\sin 2\varphi + i\cos 2\varphi$ and $i e^{-2i\varphi} = i(\cos 2\varphi - i\sin 2\varphi) = \sin 2\varphi + i\cos 2\varphi$,
> $$\begin{pmatrix} 0 & i e^{2i\varphi} \\ i e^{-2i\varphi} & 0\end{pmatrix} = \cos 2\varphi\begin{pmatrix} 0 & i \\ i & 0\end{pmatrix} - \sin 2\varphi\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix} \qquad \text{(matching entries: } (1,2)\!: i\cos 2\varphi - \sin 2\varphi;\ (2,1)\!: i\cos 2\varphi + \sin 2\varphi\text{).}$$
> The right-hand matrices are $E_2$ and $E_1$, so
> $$\operatorname{Ad}_{g_\varphi}(E_2) = -\sin 2\varphi\,E_1 + \cos 2\varphi\,E_2.$$

**Step 4: Conjugate $E_3$ and find it is fixed.**

Since $E_3$ and $g_\varphi$ are both diagonal they commute, so $\operatorname{Ad}_{g_\varphi}(E_3) = E_3$.

> [!note]- Derivation
> Both $g_\varphi = \operatorname{diag}(e^{i\varphi}, e^{-i\varphi})$ and $E_3 = \operatorname{diag}(i, -i)$ are diagonal, and diagonal matrices commute (the product of two diagonal matrices is the diagonal matrix of entrywise products, and multiplication of scalars is commutative):
> $$g_\varphi E_3 = \operatorname{diag}(e^{i\varphi}\cdot i,\ e^{-i\varphi}\cdot(-i)) = \operatorname{diag}(i\cdot e^{i\varphi},\ -i\cdot e^{-i\varphi}) = E_3\, g_\varphi.$$
> Therefore
> $$\operatorname{Ad}_{g_\varphi}(E_3) = g_\varphi E_3 g_\varphi^{-1} = E_3\, g_\varphi\, g_\varphi^{-1} = E_3 \qquad \text{(commuting } g_\varphi \text{ past } E_3\text{, then } g_\varphi g_\varphi^{-1} = 1_2\text{).}$$

**Step 5: Assemble the matrix of $\operatorname{Ad}_{g_\varphi}$ in the basis $(E_1, E_2, E_3)$.**

The three coordinate columns give the claimed rotation matrix.

> [!note]- Derivation
> By operation 3, the matrix of $\operatorname{Ad}_{g_\varphi}$ in the ordered basis $(E_1, E_2, E_3)$ has as its $a$-th column the coordinate vector of $\operatorname{Ad}_{g_\varphi}(E_a)$. From Steps 2–4:
> $$\operatorname{Ad}_{g_\varphi}(E_1) = \cos 2\varphi\,E_1 + \sin 2\varphi\,E_2 + 0\cdot E_3 \ \rightsquigarrow\ \begin{pmatrix} \cos 2\varphi \\ \sin 2\varphi \\ 0\end{pmatrix},$$
> $$\operatorname{Ad}_{g_\varphi}(E_2) = -\sin 2\varphi\,E_1 + \cos 2\varphi\,E_2 + 0\cdot E_3 \ \rightsquigarrow\ \begin{pmatrix} -\sin 2\varphi \\ \cos 2\varphi \\ 0\end{pmatrix},$$
> $$\operatorname{Ad}_{g_\varphi}(E_3) = 0\cdot E_1 + 0\cdot E_2 + 1\cdot E_3 \ \rightsquigarrow\ \begin{pmatrix} 0 \\ 0 \\ 1\end{pmatrix}.$$
> Placing these as columns,
> $$[\operatorname{Ad}_{g_\varphi}] = \begin{pmatrix} \cos 2\varphi & -\sin 2\varphi & 0 \\ \sin 2\varphi & \cos 2\varphi & 0 \\ 0 & 0 & 1\end{pmatrix},$$
> which is precisely the rotation by the angle $2\varphi$ in the $(E_1, E_2)$-plane, fixing the axis $E_3$. This settles part (a).

**Step 6 (part b): The kernel of $\operatorname{Ad}$ is $\{\pm 1_2\}$.**

An element $g$ lies in $\ker\operatorname{Ad}$ exactly when it commutes with $E_1, E_2, E_3$; imposing these and $\det g = 1$ forces $g = \pm 1_2$.

> [!note]- Derivation
> We first observe non-faithfulness, then compute the kernel exactly.
>
> **$\operatorname{Ad}$ is not faithful.** Take $g = -1_2 = \operatorname{diag}(-1, -1)$. Then for every $X \in \mathfrak{su}(2)$,
> $$\operatorname{Ad}_{-1_2}(X) = (-1_2)\,X\,(-1_2)^{-1} = (-1)(-1)\,X = X \qquad \text{(the scalar } -1 \text{ commutes with } X \text{ and } (-1)^2 = 1\text{),}$$
> so $\operatorname{Ad}_{-1_2} = \operatorname{id}_{\mathfrak{su}(2)} = \operatorname{Ad}_{1_2}$. Since $-1_2 \neq 1_2$ but they have the same image, $\operatorname{Ad}$ is not injective, hence not faithful (this is Bär's Remark 1.3.9). In particular $\{+1_2, -1_2\} \subseteq \ker\operatorname{Ad}$.
>
> **The reverse containment.** Let $g \in \ker\operatorname{Ad}$, so $\operatorname{Ad}_g = \operatorname{id}_{\mathfrak{su}(2)}$. By operation 1 this means $gXg^{-1} = X$, that is
> $$gX = Xg \qquad \text{for every } X \in \mathfrak{su}(2).$$
> Because $\{E_1, E_2, E_3\}$ spans $\mathfrak{su}(2)$, it is enough that $g$ commute with each $E_a$. Write $g = \begin{pmatrix} a & b \\ c & d\end{pmatrix}$ with $a, b, c, d \in \mathbb{C}$.
>
> *Commuting with $E_3 = \operatorname{diag}(i, -i)$ forces $g$ diagonal.* We compute
> $$g E_3 = \begin{pmatrix} a & b \\ c & d\end{pmatrix}\begin{pmatrix} i & 0 \\ 0 & -i\end{pmatrix} = \begin{pmatrix} ia & -ib \\ ic & -id\end{pmatrix}, \qquad E_3 g = \begin{pmatrix} i & 0 \\ 0 & -i\end{pmatrix}\begin{pmatrix} a & b \\ c & d\end{pmatrix} = \begin{pmatrix} ia & ib \\ -ic & -id\end{pmatrix}.$$
> Equating the $(1,2)$ entries gives $-ib = ib$, hence $2ib = 0$, so $b = 0$; equating the $(2,1)$ entries gives $ic = -ic$, hence $c = 0$. Thus $g = \operatorname{diag}(a, d)$.
>
> *Commuting with $E_1 = \left(\begin{smallmatrix} 0 & 1 \\ -1 & 0\end{smallmatrix}\right)$ forces $a = d$.* With $g = \operatorname{diag}(a, d)$,
> $$g E_1 = \begin{pmatrix} a & 0 \\ 0 & d\end{pmatrix}\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix} = \begin{pmatrix} 0 & a \\ -d & 0\end{pmatrix}, \qquad E_1 g = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}\begin{pmatrix} a & 0 \\ 0 & d\end{pmatrix} = \begin{pmatrix} 0 & d \\ -a & 0\end{pmatrix}.$$
> Equating the $(1,2)$ entries gives $a = d$. Hence $g = a\,1_2$ is a scalar matrix. (Commuting with $E_2$ is then automatic and adds nothing.)
>
> *Impose the determinant.* Since $g = a\,1_2 \in SU(2)$ we need $\det g = a^2 = 1$, so $a = \pm 1$ (and indeed $|a| = 1$, consistent with unitarity). Therefore $g = +1_2$ or $g = -1_2$, giving $\ker\operatorname{Ad} \subseteq \{+1_2, -1_2\}$.
>
> Combining the two containments, $\ker\operatorname{Ad} = \{+1_2, -1_2\}$.

> [!note]- Complete formal solution
> **Claim.** For $g_\varphi = \operatorname{diag}(e^{i\varphi}, e^{-i\varphi}) \in SU(2)$, the operator $\operatorname{Ad}_{g_\varphi}$ has matrix $\left(\begin{smallmatrix} \cos 2\varphi & -\sin 2\varphi & 0 \\ \sin 2\varphi & \cos 2\varphi & 0 \\ 0 & 0 & 1\end{smallmatrix}\right)$ in the basis $(E_1, E_2, E_3)$ of $\mathfrak{su}(2)$, and $\ker\operatorname{Ad} = \{\pm 1_2\}$.
>
> *Proof.* Since $SU(2)$ is a matrix group, $\operatorname{Ad}_{g}X = gXg^{-1}$ for $X \in \mathfrak{su}(2)$ (part (ii) of [[Thm - Ad is a Smooth Representation and its Differential is ad|the adjoint-representation theorem]]). As $g_\varphi$ is unitary and diagonal, $g_\varphi^{-1} = g_\varphi^{*} = \operatorname{diag}(e^{-i\varphi}, e^{i\varphi})$.
>
> Conjugating $E_1 = \left(\begin{smallmatrix} 0 & 1 \\ -1 & 0\end{smallmatrix}\right)$: left multiplication by $g_\varphi$ scales rows by $e^{\pm i\varphi}$ and right multiplication by $g_\varphi^{-1}$ scales columns by $e^{\mp i\varphi}$, giving $g_\varphi E_1 g_\varphi^{-1} = \left(\begin{smallmatrix} 0 & e^{2i\varphi} \\ -e^{-2i\varphi} & 0\end{smallmatrix}\right)$. Writing $e^{\pm 2i\varphi} = \cos 2\varphi \pm i\sin 2\varphi$ identifies this with $\cos 2\varphi\,E_1 + \sin 2\varphi\,E_2$. The same computation for $E_2 = \left(\begin{smallmatrix} 0 & i \\ i & 0\end{smallmatrix}\right)$ gives $g_\varphi E_2 g_\varphi^{-1} = \left(\begin{smallmatrix} 0 & i e^{2i\varphi} \\ i e^{-2i\varphi} & 0\end{smallmatrix}\right) = -\sin 2\varphi\,E_1 + \cos 2\varphi\,E_2$. Finally $E_3 = \operatorname{diag}(i, -i)$ is diagonal, hence commutes with $g_\varphi$, so $g_\varphi E_3 g_\varphi^{-1} = E_3$. The three coordinate columns $(\cos 2\varphi, \sin 2\varphi, 0)$, $(-\sin 2\varphi, \cos 2\varphi, 0)$, $(0, 0, 1)$ assemble to the stated matrix, which is the rotation by $2\varphi$ in the $(E_1, E_2)$-plane fixing $E_3$.
>
> For the kernel, $-1_2$ is scalar, so $\operatorname{Ad}_{-1_2}(X) = (-1_2)X(-1_2)^{-1} = X$ for all $X$; thus $\operatorname{Ad}_{-1_2} = \operatorname{id}$ and $\operatorname{Ad}$ is not faithful, with $\{\pm 1_2\} \subseteq \ker\operatorname{Ad}$. Conversely, if $\operatorname{Ad}_g = \operatorname{id}$ then $g$ commutes with every $X \in \mathfrak{su}(2)$, hence with $E_1, E_2, E_3$. Writing $g = \left(\begin{smallmatrix} a & b \\ c & d\end{smallmatrix}\right)$: commuting with $E_3 = \operatorname{diag}(i, -i)$ (distinct diagonal entries) forces $b = c = 0$; commuting with $E_1$ then forces $a = d$; so $g = a\,1_2$, and $\det g = a^2 = 1$ gives $a = \pm 1$. Hence $\ker\operatorname{Ad} = \{+1_2, -1_2\}$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: reading the kernel off the diagonal family alone
> From part (a) one is tempted to argue "$\operatorname{Ad}_{g_\varphi} = \operatorname{id}$ iff $\cos 2\varphi = 1$ and $\sin 2\varphi = 0$, i.e. $\varphi \in \pi\mathbb{Z}$, giving $g_\varphi = \operatorname{diag}(\pm 1, \pm 1) = \pm 1_2$", and conclude $\ker\operatorname{Ad} = \{\pm 1_2\}$. This finds the right answer but is *not a proof of the kernel*: it only examines the diagonal one-parameter subgroup $\{g_\varphi\}$, not all of $SU(2)$. The gap is closed only because every element of $SU(2)$ is conjugate to some $g_\varphi$ (the diagonal matrices form a maximal torus) and $\operatorname{Ad}$ is a homomorphism, so $\operatorname{Ad}_{hg_\varphi h^{-1}} = \operatorname{Ad}_h \operatorname{Ad}_{g_\varphi}\operatorname{Ad}_h^{-1}$ is conjugate to $\operatorname{Ad}_{g_\varphi}$ and equals the identity only when $\operatorname{Ad}_{g_\varphi}$ does. The direct commutation argument in Step 6 avoids this detour and is the one to trust; the torus argument is legitimate only once the conjugacy fact is invoked explicitly.

> [!note]- Independent sanity check: $\operatorname{Ad}_{g_\varphi}$ is orthogonal and preserves orientation
> The matrix $\left(\begin{smallmatrix} \cos 2\varphi & -\sin 2\varphi & 0 \\ \sin 2\varphi & \cos 2\varphi & 0 \\ 0 & 0 & 1\end{smallmatrix}\right)$ has determinant $\cos^2 2\varphi + \sin^2 2\varphi = 1$ and its columns are orthonormal, so it lies in $SO(3)$. This is the expected outcome: the adjoint action preserves the Killing form $\langle X, Y\rangle = -\tfrac{1}{2}\operatorname{tr}(XY)$ on $\mathfrak{su}(2)$ (because $\operatorname{tr}(gXg^{-1}gYg^{-1}) = \operatorname{tr}(XY)$ by cyclicity of the trace), and in the basis $E_1, E_2, E_3$ one computes $\langle E_a, E_b\rangle = \delta_{ab}$, so $\operatorname{Ad}_g$ is an orthogonal transformation of the Euclidean space $(\mathfrak{su}(2), \langle\cdot,\cdot\rangle) \cong \mathbb{R}^3$. That every $\operatorname{Ad}_g$ lands in $SO(3)$ (not merely $O(3)$) is the statement that $\operatorname{Ad} : SU(2) \to SO(3)$ is the well-known double cover.

---

# Key Takeaways

**For a classical matrix group, the adjoint representation is conjugation, and every computation about it is matrix arithmetic in a chosen Lie-algebra basis.** The single most useful reflex this exercise trains is the immediate replacement of the intrinsic definition $\operatorname{Ad}_g = d_e\alpha_g$ by the concrete formula $\operatorname{Ad}_g X = gXg^{-1}$ whenever $G$ is a subgroup of some $GL(n;\mathbb{K})$. Once that substitution is made, "compute the adjoint action" means "conjugate each basis matrix and read off coordinates", which is entirely mechanical. The trigger condition is any appearance of $\operatorname{Ad}$, $\operatorname{ad}$, or "the adjoint action" together with a matrix group; the transferable diagnostic is that conjugation by a *diagonal* element multiplies the $(j,k)$ matrix entry by $d_j/d_k$, so the whole effect on the off-diagonal entries is a phase, which is exactly the source of the rotation seen here. The same reflex reappears throughout the series: the local gauge transformation law $A' = g^{-1}Ag + g^{-1}dg$ and the curvature law $F' = g^{-1}Fg$ are adjoint actions in disguise, and being fluent with $gXg^{-1}$ in the smallest case $SU(2)$ is what makes those later formulas readable.

**The kernel of the adjoint representation is the centre of the group, and it is found by imposing commutation with a spanning set one matrix at a time.** The condition $\operatorname{Ad}_g = \operatorname{id}$ unwinds to "$g$ commutes with all of $\mathfrak{g}$", and for a matrix group this is a small linear system: choose the basis so that one member has *distinct eigenvalues* (here $E_3 = \operatorname{diag}(i, -i)$), which pins $g$ to be diagonal, then use a member with *nonzero off-diagonal entries* (here $E_1$) to force the diagonal entries equal, and finish with the determinant constraint. The reusable principle is that the centraliser of a matrix with distinct eigenvalues consists exactly of the matrices diagonal in the same eigenbasis; layering a second, generic matrix collapses the centraliser to the scalars. This is the concrete face of a general fact — for $SU(n)$ the centre is $\{\zeta 1_n : \zeta^n = 1\}$, the $n$-th roots of unity — and for $SU(2)$ it delivers the two-element centre $\{\pm 1_2\}$ that will reappear as the deck group of the double cover $SU(2) \to SO(3)$.

**The factor of two in the rotation angle is the signature of the double cover $SU(2) \to SO(3)$, and this exercise is where it becomes visible.** As $\varphi$ runs from $0$ to $\pi$, the group element $g_\varphi$ runs from $1_2$ to $-1_2$ along the maximal torus, while the rotation angle $2\varphi$ runs from $0$ to $2\pi$ — a full turn of $SO(3)$ produced by only a half-turn of the torus in $SU(2)$. Equivalently, $g_\varphi$ and $g_{\varphi + \pi} = -g_\varphi$ have the *same* image $\operatorname{Ad}_{g_\varphi} = \operatorname{Ad}_{-g_\varphi}$, which is the kernel fact $\{\pm 1_2\}$ read dynamically. This is the two-to-one covering $\operatorname{Ad} : SU(2) \to SO(3) \cong SO(\mathfrak{su}(2))$ whose existence underlies spin: physical rotations act on spinors only up to sign, and the sign ambiguity is exactly the kernel computed here. The companion exercise [[Ex - The Adjoint Representation of SO(3) is the Defining Representation|the adjoint representation of $SO(3)$ is the defining representation]] completes the picture from the other side — for $SO(3)$ the adjoint representation *is* faithful and equals the standard action on $\mathbb{R}^3$, so the failure of faithfulness seen here is precisely what distinguishes the simply connected double cover $SU(2)$ from its quotient $SO(3)$. Returning to this problem after time, the reconstruction hinges on remembering "conjugation by $\operatorname{diag}(e^{i\varphi}, e^{-i\varphi})$ turns the off-diagonal phase into $e^{2i\varphi}$, and the $2$ is the double cover."

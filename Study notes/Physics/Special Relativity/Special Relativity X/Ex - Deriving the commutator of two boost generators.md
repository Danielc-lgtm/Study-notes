---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Generators and Structure Constants"
tags: [physics, special-relativity, lie-groups]
---

# Problem Statement

Using the explicit matrices for the boost generators, compute the commutator $[K_1, K_2] = K_1 K_2 - K_2 K_1$ and show it equals $-J_3$, confirming the structure relation $[K_i, K_j] = -\epsilon_{ijk}J_k$.

1. Write out $K_1$, $K_2$, and $J_3$ as $4\times 4$ matrices.
2. Compute the products $K_1 K_2$ and $K_2 K_1$ and subtract.
3. Identify the result as $-J_3$, and state the general relation $[K_i, K_j] = -\epsilon_{ijk}J_k$.
4. Explain why the *minus sign* matters: show that it is what distinguishes $\mathfrak{so}(1,3)$ from the compact $\mathfrak{so}(4)$, and that it forbids the boosts from forming a subgroup.

**Recall:**

![[Def - Lie Algebra of the Lorentz Group#The Definition]]

The matrix commutator is $[A, B] = AB - BA$. The boost generators $K_i$ are symmetric, with $K_i$ carrying $1$ in the $(0,i)$ and $(i,0)$ entries; the rotation generators $J_i$ are antisymmetric, acting as $\mathbf{e}_i \times$ on the spatial block. A subset closed under the bracket is a *subalgebra*.

---

# Convergent Strategy

**Problem class.** A *Lie algebra computation*: evaluate a commutator and match it to a structure relation. The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]] notes that for the *defining* relations one may compute directly from the matrices (whereas for *derived* brackets one expands in the basis and applies the known relations) — here we are establishing the defining relation, so we multiply the explicit matrices.

**Assumption pattern.** The generators are given as explicit, sparse $4\times 4$ matrices (two nonzero entries each), which makes direct matrix multiplication feasible and exact. The signpost is that the matrices are simple enough to multiply by hand, so no abstract argument is needed — the result is a direct calculation.

**Theorem routing.** The route is mechanical: (1) write $K_1, K_2$ with their nonzero $(0,i)/(i,0)$ entries; (2) multiply $K_1 K_2$ and $K_2 K_1$ using the sparse structure; (3) subtract to get a matrix nonzero only in the $(1,2)/(2,1)$ block; (4) recognise that block as $-J_3$, the rotation generator in the $x$–$y$ plane ([[Def - Generators and Structure Constants]]). The sign and the appearance of a *rotation* generator from two *boost* generators are the content.

**Key decision point.** The crux is interpreting the result: $[K_1, K_2]$ is a *rotation* generator, not a boost, and it carries a *minus* sign. The non-obvious significance is that this single sign distinguishes the Lorentz algebra from the Euclidean $\mathfrak{so}(4)$ (where the analogous bracket is $+J_3$), and it is the algebraic reason the boosts do not close into a subgroup — composing two boosts produces a rotation (the Thomas rotation). The temptation is to treat the sign as a bookkeeping detail; it is in fact the fingerprint of non-compactness.

---

# Legal Operations Used

1. **Compute a commutator from the structure relations (operation 3 from the topic page).** Here run in reverse: we *establish* the relation $[K_1,K_2] = -J_3$ by direct matrix multiplication, the computation that justifies using the relation thereafter.

2. **Check the generator condition (operation 2 from the topic page).** Implicitly, the result $-J_3$ must itself be a generator (the algebra is closed under the bracket), which one verifies by noting $\eta(-J_3)$ is antisymmetric.

---

# Hints

> [!note]- Hint 1
> $K_1$ has $1$ in positions $(0,1)$ and $(1,0)$; $K_2$ has $1$ in positions $(0,2)$ and $(2,0)$. All other entries are zero. Write them as full $4\times 4$ arrays.

> [!note]- Hint 2
> To compute $(K_1 K_2)_{\mu\nu} = \sum_\alpha (K_1)_{\mu\alpha}(K_2)_{\alpha\nu}$, note that $K_1$ is nonzero only in rows/columns $0,1$ and $K_2$ only in rows/columns $0,2$. The product is nonzero only where a column of $K_1$ meets a row of $K_2$ at a shared index — index $0$.

> [!note]- Hint 3
> $K_1 K_2$ has a single nonzero entry at position $(1,2)$ (from $(K_1)_{10}(K_2)_{02} = 1\cdot 1$). $K_2 K_1$ has a single nonzero entry at $(2,1)$. Subtract: $[K_1,K_2]$ has $+1$ at $(1,2)$ and $-1$ at $(2,1)$.

> [!note]- Hint 4
> Compare with $J_3$, which has $-1$ at $(1,2)$ and $+1$ at $(2,1)$ (it rotates $x \to y$). So $[K_1, K_2]$, with $+1$ at $(1,2)$ and $-1$ at $(2,1)$, is exactly $-J_3$.

> [!note]- Hint 5
> For part 4: in Euclidean $\mathfrak{so}(4)$ the "boost" generators are genuine rotations into a fourth spatial axis, and the analogous bracket is $[K_i,K_j] = +\epsilon_{ijk}J_k$. The sign flip to $-$ in $\mathfrak{so}(1,3)$ traces to $\eta_{00}\eta_{ii}$ having opposite signs.

---

# Solution

Direct matrix multiplication gives $K_1 K_2$ nonzero only at $(1,2)$ and $K_2 K_1$ nonzero only at $(2,1)$; their difference is the matrix with $+1$ at $(1,2)$ and $-1$ at $(2,1)$, which is $-J_3$. The minus sign distinguishes the non-compact Lorentz algebra from the compact $\mathfrak{so}(4)$ and forbids a boost subgroup.

**Step 1: The matrices.**

> [!note]- Derivation
> $$K_1 = \begin{pmatrix} 0&1&0&0\\ 1&0&0&0\\ 0&0&0&0\\ 0&0&0&0 \end{pmatrix},\qquad
> K_2 = \begin{pmatrix} 0&0&1&0\\ 0&0&0&0\\ 1&0&0&0\\ 0&0&0&0 \end{pmatrix},\qquad
> J_3 = \begin{pmatrix} 0&0&0&0\\ 0&0&-1&0\\ 0&1&0&0\\ 0&0&0&0 \end{pmatrix}.$$
> $K_1$ mixes $t$ ($\mu=0$) with $x$ ($\mu=1$); $K_2$ mixes $t$ with $y$ ($\mu=2$); $J_3$ rotates $x$ into $y$.

**Step 2: The products.**

> [!note]- Derivation
> Using $(AB)_{\mu\nu} = \sum_\alpha A_{\mu\alpha}B_{\alpha\nu}$ and the sparsity:
>
> For $K_1 K_2$: the only way to get a nonzero term is row of $K_1$ hitting column of $K_2$ through a shared middle index. $(K_1)_{10} = 1$ and $(K_2)_{02} = 1$ give $(K_1 K_2)_{12} = (K_1)_{10}(K_2)_{02} = 1$. Also $(K_1)_{01} = 1$ but column $1$ of $K_2$ is zero, so no contribution. Checking all entries, the only nonzero one is
> $$K_1 K_2 = \begin{pmatrix} 0&0&0&0\\ 0&0&1&0\\ 0&0&0&0\\ 0&0&0&0 \end{pmatrix}\quad\text{(single $1$ at position $(1,2)$).}$$
>
> For $K_2 K_1$: $(K_2)_{20} = 1$ and $(K_1)_{01} = 1$ give $(K_2 K_1)_{21} = 1$. The only nonzero entry is
> $$K_2 K_1 = \begin{pmatrix} 0&0&0&0\\ 0&0&0&0\\ 0&1&0&0\\ 0&0&0&0 \end{pmatrix}\quad\text{(single $1$ at position $(2,1)$).}$$

**Step 3: The commutator is $-J_3$.**

> [!note]- Derivation
> Subtract:
> $$[K_1, K_2] = K_1 K_2 - K_2 K_1 = \begin{pmatrix} 0&0&0&0\\ 0&0&1&0\\ 0&-1&0&0\\ 0&0&0&0 \end{pmatrix}.$$
> This has $+1$ at $(1,2)$ and $-1$ at $(2,1)$. Compare with $J_3$, which has $-1$ at $(1,2)$ and $+1$ at $(2,1)$: the commutator is its negative,
> $$[K_1, K_2] = -J_3.$$
> By the cyclic symmetry of the index labels, the general relation is
> $$[K_i, K_j] = -\sum_k\epsilon_{ijk}J_k,$$
> i.e. $[K_2,K_3] = -J_1$, $[K_3,K_1] = -J_2$. The commutator of two *boost* generators is *minus a rotation* generator. (It is a generator, as it must be: $\eta(-J_3) = J_3$ on the spatial block is antisymmetric, so $-J_3 \in \mathfrak{so}(1,3)$.)

**Step 4: Why the minus sign matters.**

> [!note]- Derivation
> *Distinguishes Lorentz from Euclidean.* In the Euclidean rotation algebra $\mathfrak{so}(4)$, the generators "$K_i$" are genuine rotations mixing the three spatial axes with a *fourth spatial* axis. The analogous commutator there is $[K_i, K_j] = +\epsilon_{ijk}J_k$ — a plus sign, because all four axes have the same metric sign. In $\mathfrak{so}(1,3)$ the "fourth axis" is *time*, with $\eta_{00} = +1$ against the spatial $\eta_{ii} = -1$, and tracking this through the bracket flips the sign: $[K_i, K_j] = -\epsilon_{ijk}J_k$. So the single sign difference between the metrics $\mathrm{diag}(1,1,1,1)$ and $\mathrm{diag}(1,-1,-1,-1)$ is exactly the sign difference between $[K,K] = +J$ (compact $\mathfrak{so}(4)$) and $[K,K] = -J$ (non-compact $\mathfrak{so}(1,3)$). This minus sign is the algebraic signature of non-compactness.
>
> *Forbids a boost subgroup.* If the boosts formed a subgroup, their generators $K_1, K_2, K_3$ would form a subalgebra — closed under the bracket. But $[K_1, K_2] = -J_3$ is a *rotation* generator, *not* a boost generator, so the span of the $K_i$ is not closed under the bracket and the boosts do *not* form a subgroup. Concretely, composing two boosts in different planes yields a boost times a rotation (the [[Def - Thomas Rotation|Thomas rotation]]), and the rotation is exactly this $[K,K] = -J$ appearing in Baker–Campbell–Hausdorff. The minus sign is therefore the source of one of the genuinely surprising effects in relativity.

> [!note]- Complete formal solution
> With $K_1$ (nonzero at $(0,1),(1,0)$), $K_2$ (nonzero at $(0,2),(2,0)$), and $J_3$ (nonzero at $(1,2) = -1$, $(2,1) = +1$): the product $K_1 K_2$ is nonzero only at $(1,2)$ (value $+1$, from $(K_1)_{10}(K_2)_{02}$), and $K_2 K_1$ only at $(2,1)$ (value $+1$). Subtracting, $[K_1,K_2] = K_1 K_2 - K_2 K_1$ has $+1$ at $(1,2)$ and $-1$ at $(2,1)$, which is $-J_3$. Hence $[K_i,K_j] = -\epsilon_{ijk}J_k$. The result is a rotation generator, so the boosts are not closed under the bracket and form no subgroup; the minus sign (versus the $+$ of Euclidean $\mathfrak{so}(4)$) is the fingerprint of non-compactness and the origin of the Thomas rotation. $\blacksquare$

---

# Key Takeaways

**Two boosts bracket to a rotation, and that is the whole strangeness of the Lorentz group in one line.** The computation delivers the single most important commutator of the chapter: $[K_1, K_2] = -J_3$. A *boost* in the $t$–$x$ plane and a *boost* in the $t$–$y$ plane, commuted, produce a *rotation* in the $x$–$y$ plane. This is not bookkeeping — it is the reason the boosts do not form a subgroup, the reason composing two non-collinear boosts gives the [[Def - Thomas Rotation|Thomas rotation]], and (after the factor of $i$ that turns the minus into a decoupling) the reason the algebra splits into two copies of $\mathfrak{su}(2)$. The trigger to recognise this structure: whenever a "translation-like" generator (here a boost, mixing a privileged direction with the others) appears, ask what *its* mutual commutators are — if they produce the "rotation-like" generators, the translations cannot form a subgroup, and a composition of them will produce an unexpected rotation.

**The minus sign is the metric's minus sign, propagated into the algebra.** The contrast $[K,K] = -J$ (Lorentz) versus $[K,K] = +J$ (Euclidean $\mathfrak{so}(4)$) traces to a single product of metric signs: a boost involves the time index ($\eta_{00} = +1$) and a space index ($\eta_{ii} = -1$), and the bracket of two boosts picks up the product of the *opposite* signs that the rotation does. The reusable lesson is that the signature of the metric is not an external label on the geometry — it propagates into every derived structure, and in the Lie algebra it appears as the sign of the boost-boost commutator. This is one more instance of the chapter's refrain that the single sign difference between Euclidean and Minkowski geometry is the source of every relativistic phenomenon: here it is the difference between a compact group (rotations all the way) and a non-compact one (with runaway boosts).

**Direct matrix multiplication establishes the structure relations; thereafter, use the relations.** This exercise computes a *defining* commutator from the explicit sparse matrices, which is the right tool when establishing the structure constants for the first time — the matrices are simple enough (two nonzero entries each) that the multiplication is exact and quick. Once the three relations $[J,J]=J$, $[J,K]=K$, $[K,K]=-J$ are in hand, one should *never* multiply $4\times 4$ matrices again: any further commutator is computed by expanding in the $K,J$ basis and applying the relations, with the antisymmetric symbol $\epsilon_{ijk}$ doing the bookkeeping. The diagnostic for which method to use: establishing a structure constant from scratch warrants the matrices; computing a derived bracket (a commutator of linear combinations) warrants the relations. This division of labour — matrices once, relations forever after — is how Lie-algebra computations stay manageable.

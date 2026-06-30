---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Null Rotations and Four-Screws"
  - "Def - Classification of Restricted Lorentz Transformations"
tags: [physics, special-relativity]
---

# Problem Statement

Consider the null-rotation matrix in the non-orthonormal null basis $(\ell, k, e_2, e_3)$, where $\ell, k$ are null with $\ell\cdot k = 2$ and $e_2, e_3$ spacelike unit:
$$
(\Lambda^*)^\alpha{}_\beta = \begin{pmatrix} 1 & 4\alpha^2 & 2\alpha & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 4\alpha & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \qquad \alpha > 0.
$$

1. Verify that $\Lambda$ fixes the null vector $\ell$ and the spacelike vector $e_3$, hence the **null plane** $\Pi_3 = \mathrm{Span}(\ell, e_3)$, and confirm this plane has degenerate induced metric (signature $(0,-)$).
2. Show that $\mathrm{Span}(\ell)$ is the *unique* invariant null direction.
3. Set $N = \Lambda - \mathrm{Id}$. Prove $N^3 = 0$ but $N^2 \ne 0$ (a single Jordan block of size three on $\mathrm{Span}(\ell, k, e_2)$), so $\Lambda$ is **not diagonalisable**, and confirm its only eigenvalue is $1$ with algebraic multiplicity four but geometric multiplicity two.

**Recall:**

![[Def - Null Rotations and Four-Screws#The Definition]]

A null plane $\Pi$ has degenerate induced metric: it contains exactly one null direction $\mathrm{Span}(\ell)$, with $\ell$ orthogonal to all of $\Pi$, and every other nonzero vector spacelike. A linear map is parabolic (unipotent with a nontrivial nilpotent part) when its matrix minus the identity is nilpotent but nonzero.

---

# Convergent Strategy

**Problem class.** A *structure-verification* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: confirm that a given matrix has the claimed invariant subspaces and Jordan structure, distinguishing the parabolic (null-rotation) type from the diagonalisable types by the nilpotency of $\Lambda - \mathrm{Id}$.

**Assumption pattern.** The matrix is given in the null basis, where its action is most transparent. The fixed vectors $\ell$ (first basis vector, first column $= e_1^*$) and $e_3$ (fourth basis vector, fourth column $= e_4^*$) are read directly from the matrix. The uniqueness of the null direction and the nilpotency are computational consequences of the specific off-diagonal entries $4\alpha^2, 2\alpha, 4\alpha$.

**Theorem routing.** The classification routes through [[Def - Null Rotations and Four-Screws]]: fixing a null plane $\Rightarrow$ null rotation; one invariant null direction $\Rightarrow$ parabolic; nilpotent $\Lambda - \mathrm{Id}$ of index three $\Rightarrow$ a single size-three Jordan block, confirming non-diagonalisability. The degeneracy of $\Pi_3$ follows from $\ell\cdot\ell = 0$ and $\ell\cdot e_3 = 0$.

**Key decision point.** The non-obvious step is recognising that the eigenvalue $1$ having algebraic multiplicity four does *not* mean $\Lambda = \mathrm{Id}$ or even that $\Lambda$ is diagonalisable — the geometric multiplicity is only two (two independent eigenvectors $\ell, e_3$), so there is a defect, and the defect is a size-three Jordan block. The natural-but-wrong assumption is that "eigenvalue $1$ with full multiplicity" implies the identity; the null rotation is the counterexample.

---

# Legal Operations Used

1. **Find an invariant null direction** (operation 3 from the topic page): identify the fixed null vector $\ell$ from the first column and verify uniqueness.

2. **Count invariant null directions to name the type** (operation 5 from the topic page): exactly one $\Rightarrow$ null rotation.

3. **Diagonalise in the null basis** (operation 9 from the topic page, used in reverse): the failure to diagonalise — the nilpotency of $\Lambda - \mathrm{Id}$ — is the signature of the null rotation.

---

# Hints

> [!note]- Hint 1
> The columns of $(\Lambda^*)^\alpha{}_\beta$ are the images of the basis vectors $\ell, k, e_2, e_3$. Read off $\Lambda(\ell)$ (first column) and $\Lambda(e_3)$ (fourth column).

> [!note]- Hint 2
> For uniqueness, a null vector is $a\ell + bk + ce_2 + de_3$ with norm $2ab\cdot(\tfrac12) - c^2 - d^2$... compute the null condition in the basis ($\ell\cdot k = 2$, $e_2\cdot e_2 = e_3\cdot e_3 = -1$) and impose $\Lambda(v) \parallel v$.

> [!note]- Hint 3
> Compute $N = \Lambda - \mathrm{Id}$ in the null basis (subtract $1$ from the diagonal). Apply $N$ repeatedly to $k$: $N(k), N^2(k), N^3(k)$. The third should vanish, the second should not.

---

# Solution

We verify the invariant subspaces (Step 1), prove uniqueness of the null direction (Step 2), and establish the nilpotent Jordan structure (Step 3).

**Step 1: $\Lambda$ fixes $\ell$ and $e_3$, and $\Pi_3 = \mathrm{Span}(\ell, e_3)$ is a degenerate null plane.**

> [!note]- Derivation
> The columns of $(\Lambda^*)^\alpha{}_\beta$ in the basis $(\ell, k, e_2, e_3)$ are the images. The first column is $(1,0,0,0)^{\mathsf T}$, so $\Lambda(\ell) = \ell$. The fourth column is $(0,0,0,1)^{\mathsf T}$, so $\Lambda(e_3) = e_3$. Hence $\Lambda$ fixes both $\ell$ and $e_3$, so it maps $\Pi_3 = \mathrm{Span}(\ell, e_3)$ to itself (indeed fixes it pointwise).
>
> *Degeneracy.* The induced metric on $\Pi_3$ has Gram matrix $\begin{pmatrix} \ell\cdot\ell & \ell\cdot e_3 \\ e_3\cdot\ell & e_3\cdot e_3 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & -1 \end{pmatrix}$, since $\ell$ is null ($\ell\cdot\ell = 0$) and orthogonal to the spacelike $e_3$ ($\ell\cdot e_3 = 0$). This Gram matrix has rank one (determinant $0$), so the induced metric is degenerate with signature $(0,-)$: $\ell$ is in the radical (orthogonal to all of $\Pi_3$, including itself). Thus $\Pi_3$ is a null plane. Note one cannot decompose $E = \Pi_3 \oplus \Pi_3^\perp$, since $\ell \in \Pi_3 \cap \Pi_3^\perp$.

**Step 2: $\mathrm{Span}(\ell)$ is the unique invariant null direction.**

> [!note]- Derivation
> Let $v = a\ell + bk + ce_2 + de_3$ be a null vector: $v\cdot v = a^2(\ell\cdot\ell) + b^2(k\cdot k) + 2ab(\ell\cdot k) + c^2(e_2\cdot e_2) + d^2(e_3\cdot e_3) = 0 + 0 + 4ab - c^2 - d^2 = 0$, so $4ab = c^2 + d^2 \ge 0$.
>
> Suppose $\mathrm{Span}(v)$ is invariant: $\Lambda(v) = \mu v$. Compute $\Lambda(v)$ from the matrix:
> $$\Lambda(v) = a\ell + b(4\alpha^2\ell + k + 4\alpha e_2) + c(2\alpha\ell + e_2) + d\,e_3 = (a + 4\alpha^2 b + 2\alpha c)\ell + b\,k + (4\alpha b + c)e_2 + d\,e_3.$$
> For $\Lambda(v) = \mu v$, match components: $b = \mu b$, $d = \mu d$, $4\alpha b + c = \mu c$, $a + 4\alpha^2 b + 2\alpha c = \mu a$.
>
> From $b = \mu b$ and $d = \mu d$: either $\mu = 1$, or $b = d = 0$.
> - If $b = d = 0$: then $4ab = c^2 + d^2$ gives $0 = c^2$, so $c = 0$, and $v = a\ell$. This is $\mathrm{Span}(\ell)$.
> - If $\mu = 1$: then $4\alpha b + c = c$ forces $b = 0$ (as $\alpha > 0$); with $b = 0$, $4ab = c^2 + d^2$ gives $c^2 + d^2 = 0$, so $c = d = 0$, and $v = a\ell$ again.
>
> Either way $v \in \mathrm{Span}(\ell)$. Hence $\mathrm{Span}(\ell)$ is the **unique** invariant null direction, so $\Lambda$ is a null rotation.

**Step 3: $N = \Lambda - \mathrm{Id}$ is nilpotent of index three.**

> [!note]- Derivation
> Subtract the identity: in the null basis,
> $$N = \Lambda - \mathrm{Id} = \begin{pmatrix} 0 & 4\alpha^2 & 2\alpha & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 4\alpha & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
> Read the action on basis vectors: $N(\ell) = 0$, $N(k) = 4\alpha^2\ell + 4\alpha e_2$, $N(e_2) = 2\alpha\ell$, $N(e_3) = 0$.
>
> Apply $N$ to $k$ repeatedly:
> $$N(k) = 4\alpha^2\ell + 4\alpha e_2,$$
> $$N^2(k) = N(4\alpha^2\ell + 4\alpha e_2) = 4\alpha^2\cdot 0 + 4\alpha\cdot 2\alpha\ell = 8\alpha^2\ell \ne 0,$$
> $$N^3(k) = N(8\alpha^2\ell) = 8\alpha^2 N(\ell) = 0.$$
> Since $N(\ell) = N(e_2) \in \mathrm{Span}(\ell, e_2)$ and $N(e_3) = 0$, and $N^3$ kills $k$ (and clearly $\ell, e_2, e_3$), we have $N^3 = 0$. But $N^2(k) = 8\alpha^2\ell \ne 0$, so $N^2 \ne 0$. Thus $N$ is nilpotent of index three.
>
> *Jordan structure.* The chain $k \xrightarrow{N} 4\alpha^2\ell + 4\alpha e_2 \xrightarrow{N} 8\alpha^2\ell \xrightarrow{N} 0$ is a single Jordan chain of length three, spanning $\mathrm{Span}(\ell, k, e_2)$ (the three vectors $8\alpha^2\ell$, $4\alpha^2\ell + 4\alpha e_2$, $k$ are independent). The vector $e_3$ is a separate eigenvector ($N(e_3) = 0$). So in the eigenvalue $1$, the Jordan form has one block of size three (on $\mathrm{Span}(\ell, k, e_2)$) and one of size one (on $e_3$). Hence the only eigenvalue is $1$, with **algebraic multiplicity four** (all four diagonal entries are $1$) but **geometric multiplicity two** (two independent eigenvectors $\ell, e_3$). The defect — algebraic minus geometric $= 2$ — is exactly the nilpotency, and $\Lambda$ is **not diagonalisable**. $\blacksquare$

> [!note]- Complete formal solution
> The first and fourth columns of $(\Lambda^*)^\alpha{}_\beta$ show $\Lambda(\ell) = \ell$, $\Lambda(e_3) = e_3$, so $\Pi_3 = \mathrm{Span}(\ell, e_3)$ is fixed; its Gram matrix $\mathrm{diag}(0,-1)$ (rank one) makes it a degenerate null plane, $\ell$ in the radical.
>
> A null vector $v = a\ell + bk + ce_2 + de_3$ satisfies $4ab = c^2 + d^2$; imposing $\Lambda(v) = \mu v$ and matching components forces $v \in \mathrm{Span}(\ell)$ (either $b = d = 0 \Rightarrow c = 0$, or $\mu = 1 \Rightarrow b = 0 \Rightarrow c = d = 0$). So $\mathrm{Span}(\ell)$ is the unique invariant null direction: $\Lambda$ is a null rotation.
>
> $N = \Lambda - \mathrm{Id}$ has $N(\ell) = 0$, $N(e_2) = 2\alpha\ell$, $N(k) = 4\alpha^2\ell + 4\alpha e_2$, $N(e_3) = 0$, giving the Jordan chain $k \to 4\alpha^2\ell + 4\alpha e_2 \to 8\alpha^2\ell \to 0$. Thus $N^2(k) = 8\alpha^2\ell \ne 0$, $N^3 = 0$: a size-three Jordan block plus a size-one block, eigenvalue $1$ of algebraic multiplicity four and geometric multiplicity two, $\Lambda$ not diagonalisable. $\blacksquare$

---

# Key Takeaways

**A null plane is a two-plane with degenerate induced metric, and it is the defining invariant of a null rotation.** The signature $(0,-)$ of the Gram matrix — one zero eigenvalue, one negative — is what makes $\Pi_3$ a null plane, and the zero eigenvalue means the null vector $\ell$ is orthogonal to the *entire* plane including itself. This degeneracy is impossible for timelike planes (signature $(+,-)$) and spacelike planes (signature $(-,-)$), so a transformation strictly invariant on a null plane cannot be a boost or rotation. The trigger "a transformation fixing a two-plane" should prompt checking the induced metric's signature: $(+,-)$ means boost, $(-,-)$ means rotation, $(0,-)$ means null rotation. The failure of the orthogonal decomposition $E = \Pi \oplus \Pi^\perp$ (because $\Pi \cap \Pi^\perp \ne \{0\}$) is the algebraic flag of degeneracy.

**High algebraic multiplicity of the eigenvalue $1$ does not imply the identity — the geometric multiplicity is what matters.** The null rotation has $1$ as its only eigenvalue with algebraic multiplicity four, yet it is far from the identity: its geometric multiplicity is only two, so there is a defect of two, realised as a size-three Jordan block. This is the canonical lesson of non-diagonalisable matrices: the algebraic multiplicity (from the characteristic polynomial) can exceed the geometric multiplicity (the dimension of the eigenspace), and the gap is the nilpotent defect. The trigger "eigenvalue with full algebraic multiplicity" should never be assumed to mean "diagonalisable" or "identity"; one must compute the eigenspace dimension. Here two independent eigenvectors $\ell, e_3$ against algebraic multiplicity four signals the parabolic structure.

**Nilpotency of $\Lambda - \mathrm{Id}$ of index three is the computable fingerprint of a null rotation.** The chain $N^0 k, N k, N^2 k$ ending in $N^3 k = 0$ with $N^2 k \ne 0$ exhibits the single size-three Jordan block, and this is the fastest confirmation that a transformation is a null rotation rather than the identity or a four-screw. The reusable computation: form $N = \Lambda - \mathrm{Id}$, find a vector $v$ with $N^2 v \ne 0$, and check $N^3 v = 0$; the existence of such a chain proves a parabolic (unipotent, non-semisimple) element. This same technique identifies parabolic elements of $SL(2,\mathbb{C})$ (where the lift has trace $\pm 2$ and $(A \mp I)^2 = 0$), connecting the relativistic null rotation to the parabolic Möbius transformations that generate the cusps of hyperbolic surfaces.

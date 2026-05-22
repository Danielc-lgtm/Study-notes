---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Linear Map"
  - "Def - Bilinear Form"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $\mathbb{F}$, and $m \geq 1$ is a positive integer. The Cartesian power is $V^m := \underbrace{V \times \cdots \times V}_{m \text{ factors}}$, and the space of $m$-linear forms is denoted $V^{(m)}$. The case $m = 1$ gives $V^{(1)} = V^*$ (the dual space of linear functionals), and the case $m = 2$ gives $V^{(2)}$ the [[Def - Bilinear Form|bilinear forms]] of §9A.

---

# Axiom Motivation

A multilinear form is the natural generalisation of a [[Def - Bilinear Form|bilinear form]] to more than two inputs. The motivating examples are obvious: the determinant $\det(v_1, \dots, v_n)$ of $n$ column vectors in $\mathbb{F}^n$ is $n$-linear (each column being independent), the volume form $\omega(v_1, \dots, v_n) = \det[v_i^j]$ that measures the signed volume of a parallelepiped is $n$-linear, the trace product $\operatorname{tr}(T_1 T_2 \cdots T_m)$ on operator spaces is $m$-linear (linear in each operator slot), and the multilinear expansions of derivatives like the $m$-th total derivative of a function. All of these take $m$ vector inputs and produce one scalar output, with linearity holding separately in each slot.

The single axiom — linearity in each of the $m$ slots when the others are held fixed — is the natural extension of the bilinear axiom. The reason to study this generality, rather than just bilinear forms, is twofold. First, the **determinant** is fundamentally an $n$-linear form in $n$ vectors (the columns of a matrix), and you cannot define it cleanly without the multilinear framework. Second, **alternating multilinear forms** (the next definition, [[Def - Alternating Multilinear Form]]) are the key to defining the determinant in a basis-free way, and they are most natural in the $m$-linear context. The bilinear case $m = 2$ does *not* exhibit the magical one-dimensionality $\dim V^{(n)}_{\mathrm{alt}} = 1$ — that requires $m = n$ specifically — so the structural theory really lives in the multilinear, not bilinear, world.

A key formal observation: an $m$-linear form on $V$ is **not** the same as a linear functional on $V^m = V \oplus V \oplus \cdots \oplus V$. The Cartesian product $V^m$ as a vector space has dimension $mn$ (for $\dim V = n$), and a linear functional on it has dimension $mn$. The $m$-linear forms, by contrast, have dimension $n^m$, because each value $\beta(e_{i_1}, \dots, e_{i_m})$ on a basis $m$-tuple is a free parameter. So $\dim V^{(m)} = n^m$, growing exponentially with $m$, while joint-linear functionals grow only linearly. This exponential growth is what makes multilinear algebra rich, and what makes tensor products the natural home for it: the tensor product $V^{\otimes m}$ has dimension $n^m$, matching $\dim V^{(m)}$ by duality $V^{(m)} \cong (V^{\otimes m})^*$.

**Why "linear in each slot separately" is the right axiom.** One could imagine weaker conditions like "linear in any subset of slots simultaneously" or stronger ones like "totally linear on $V^m$" (joint linearity). The first is harder to state and gives nothing new — linearity in slot $k$ alone, for each $k$, generates linearity in any subset. The second collapses the structure: $\dim$ of joint-linear functionals on $V^m$ is $mn$, not $n^m$, and the determinant is excluded (it is not jointly linear in all variables). Multilinearity is the *exactly right* condition for the structure-rich theory of forms attached to multiple vector inputs.

---

# The Definition

For a positive integer $m$, an **$m$-linear form** on $V$ is a function $\beta : V^m \to \mathbb{F}$ that is **linear in each slot** when the other slots are held fixed. Explicitly, for each $k \in \{1, \dots, m\}$ and all $u_1, \dots, u_m \in V$, the function

$$v \;\longmapsto\; \beta(u_1, \dots, u_{k-1}, v, u_{k+1}, \dots, u_m)$$

is a linear functional on $V$.

The set of $m$-linear forms on $V$ is denoted $V^{(m)}$. It is a vector space under pointwise addition and scalar multiplication.

A function is called a **multilinear form** if it is an $m$-linear form for some positive integer $m$. The integer $m$ is the **degree** of the form.

**Special cases.** A 1-linear form is a linear functional, so $V^{(1)} = V^*$. A 2-linear form is a [[Def - Bilinear Form|bilinear form]], so $V^{(2)}$ is the bilinear forms of §9A.

**Determination by basis values.** An $m$-linear form $\beta$ is uniquely determined by its values $\beta(e_{i_1}, e_{i_2}, \dots, e_{i_m})$ on $m$-tuples drawn from a basis $(e_1, \dots, e_n)$. There are $n^m$ such tuples (each of the $m$ slots independently chooses among $n$ basis vectors), and each value can be assigned freely:

$$\dim V^{(m)} = n^m \quad \text{where } n = \dim V.$$

For $v_k = \sum_{i_k} a^{i_k}_k e_{i_k}$, the expansion is

$$\beta(v_1, \dots, v_m) = \sum_{i_1, \dots, i_m} a^{i_1}_1 a^{i_2}_2 \cdots a^{i_m}_m \, \beta(e_{i_1}, e_{i_2}, \dots, e_{i_m}).$$

---

# Categorical / Structural Definition

The categorical formulation makes the relationship between multilinear forms and tensor products crystal clear.

**An $m$-linear form on $V$ is a linear functional on $V^{\otimes m}$.** The [[Thm - Universal Property of the Tensor Product|universal property]] of the tensor product (extended to $m$-fold tensor products) gives a natural isomorphism

$$V^{(m)} \;\cong\; \mathcal{L}(V^{\otimes m}, \mathbb{F}) \;=\; (V^{\otimes m})^*.$$

A multilinear form $\beta$ corresponds to the linear functional $\hat\beta(v_1 \otimes \cdots \otimes v_m) := \beta(v_1, \dots, v_m)$ on simple tensors, extended linearly. The bijection works because both sides have the same dimension $n^m$ and both naturally parametrise the "value on basis $m$-tuples" data.

This characterisation explains many properties. The vector space structure of $V^{(m)}$ matches that of $(V^{\otimes m})^*$. The decompositions into symmetric and alternating parts correspond to decompositions of $V^{\otimes m}$ into symmetric and alternating tensor algebras: $V^{(m)}_{\mathrm{sym}} \cong (\operatorname{Sym}^m V)^*$ and $V^{(m)}_{\mathrm{alt}} \cong (\Lambda^m V)^*$. The dimension $\binom{n}{m}$ of alternating $m$-linear forms (for $m \leq n$) is the dimension of the exterior power, and the dimension $\binom{n+m-1}{m}$ of symmetric $m$-linear forms is the dimension of the symmetric power.

**Multilinear forms as morphisms in a category.** The natural framework is the category of vector spaces with multilinear maps (rather than just linear maps) as morphisms. Tensor products in linear algebra are exactly the operation that converts multilinear maps in this enlarged category into linear maps in the ordinary category — and this conversion is captured by the universal property.

---

# Relate to Other Fields / Compression

A multilinear form is **the higher-arity generalisation of a bilinear form**, or equivalently **a tensor of type $(0, m)$**. In the index notation of differential geometry, a multilinear form on the tangent space at a point is exactly a tensor with $m$ covariant indices: $T_{i_1 i_2 \cdots i_m}$ is the coefficient of $\beta(e_{i_1}, \dots, e_{i_m})$ in a basis.

From the algebraic side, $V^{(m)}$ is the space of $m$-linear forms on $V$, and via the universal property it is canonically isomorphic to the dual of $V^{\otimes m}$. The whole theory of tensor algebra is built on understanding multilinear forms and their interactions.

**True name:** A multilinear form is a function on $m$ vectors that is linear separately in each — the natural higher-input generalisation of a linear functional.

---

# Examples / Corollaries

**Is an instance: any product of linear functionals.** For $\varphi_1, \dots, \varphi_m \in V^*$, the function

$$\beta(v_1, \dots, v_m) := \varphi_1(v_1) \cdot \varphi_2(v_2) \cdots \varphi_m(v_m)$$

is $m$-linear (linearity in slot $k$ comes from linearity of $\varphi_k$). These are the **decomposable** or **elementary** multilinear forms; they span $V^{(m)}$ but do not exhaust it.

**Is an instance: the determinant $\det(v_1, \dots, v_n)$ of $n$ vectors in $\mathbb{F}^n$.** This is $n$-linear in the columns — the column-multilinearity property of determinants. It is also *alternating*, but multilinearity is the structural feature relevant here. The map $(v_1, \dots, v_n) \mapsto \det(v_1 \cdots v_n)$ is the canonical nontrivial $n$-linear form on $\mathbb{F}^n$.

**Is an instance: the trace product $\beta(T_1, \dots, T_m) = \operatorname{tr}(T_1 T_2 \cdots T_m)$ on $\mathcal{L}(V)^m$.** Each slot is linear because matrix multiplication and trace are linear in each operator. This is an $m$-linear form on the operator space $\mathcal{L}(V)$ — note that it is *cyclic* (invariant under cyclic permutation of the arguments) but not generally symmetric.

**Is an instance: the integral pairing $\beta(p_1, p_2, p_3) = \int_0^1 p_1(x) p_2(x) p_3(x)\, dx$ on $\mathcal{P}_n(\mathbb{R})$.** A 3-linear form (linear in each $p_i$ because integration is linear), symmetric in all three arguments.

**Is an instance: the wedge product of dual vectors $(\varphi_1 \wedge \cdots \wedge \varphi_m)(v_1, \dots, v_m) = \det[\varphi_i(v_j)]$.** An $m$-linear form on $V$, *and* alternating. The wedge product is the canonical antisymmetric construction.

**Is NOT an instance: the squared inner product $f(u, v, w) = \langle u, v\rangle \langle v, w\rangle$ on $V \times V \times V$.** Fails linearity in the middle slot: $f(u, av, w) = \langle u, av\rangle \langle av, w\rangle = a^2 \langle u, v\rangle\langle v, w\rangle$, which is quadratic in $a$, not linear. The middle slot is quadratic in $v$, so this is *not* a multilinear form. It is a function of three vectors, but not linear in each.

**Is NOT an instance: the norm $g(v_1, v_2) = \|v_1 + v_2\|$ on an inner product space.** Not even linear in $v_1$ alone: $g(2v_1, v_2) = \|2v_1 + v_2\| \neq 2g(v_1, v_2)$ in general.

**Corollary (dimensions).** $\dim V^{(m)} = n^m$, where $n = \dim V$. For $m \geq 2$, this grows exponentially, which is why multilinear-form spaces become enormous quickly: even $V^{(3)}$ for $\dim V = 3$ already has dimension 27.

**Corollary (extension from basis values).** Given any choice of scalars $\beta_{i_1 \cdots i_m} \in \mathbb{F}$ for $i_1, \dots, i_m \in \{1, \dots, n\}$, there is a unique multilinear form $\beta$ on $V$ with $\beta(e_{i_1}, \dots, e_{i_m}) = \beta_{i_1 \cdots i_m}$ — the "tensor coefficients" of $\beta$. This is the multilinear analogue of "a linear map is determined by its action on a basis".

**Corollary (decomposability).** Not every multilinear form is a product of linear functionals. For instance, the determinant $\det : V^n \to \mathbb{F}$ on $\mathbb{F}^n$ for $n \geq 2$ is *not* a product of $n$ linear functionals — it is an alternating sum of such products, parametrised by permutations. The fact that decomposable forms span $V^{(m)}$ but do not exhaust it is the precise reason tensor products contain "entangled" elements that are not simple tensors.

**Calibration check.** If you have understood the definition, you should be able to verify: (i) $\dim V^{(2)} = n^2$ matches the count of $n \times n$ matrices (since bilinear forms on $\mathbb{F}^n$ are matrices); (ii) the determinant on $\mathbb{F}^2$ given by $\det((x_1, y_1), (x_2, y_2)) = x_1 y_2 - x_2 y_1$ is 2-linear by direct check, e.g., $\det((ax_1 + bx_1', y_1), (x_2, y_2)) = (ax_1 + bx_1') y_2 - x_2 y_1 = a(x_1 y_2 - x_2 y_1)\cdot$ wait, the $-x_2 y_1$ depends on $y_1$ not $x_1$, so it should be $a \det((x_1, y_1), (x_2, y_2)) + b \det((x_1', y_1), (x_2, y_2)) = a(x_1 y_2 - x_2 y_1) + b(x_1' y_2 - x_2 y_1) = (ax_1 + bx_1') y_2 - (a + b) x_2 y_1$ — the discrepancy when $a + b \neq 1$ tells us the *first slot* is *not* linear in the sense $\det(av_1 + bv_1', v_2) = a \det(v_1, v_2) + b \det(v_1', v_2)$; check the computation more carefully and see this *does* in fact hold (the corrected calculation: each occurrence of $y_1$ is fixed in the first computation, so this is linear in $x_1$; for linearity in the *first vector* $v_1 = (x_1, y_1)$, both coordinates vary, but $\det(av_1 + bv_1', v_2) = (ax_1 + bx_1')(y_2) - (x_2)(ay_1 + by_1') = a(x_1 y_2 - x_2 y_1) + b(x_1' y_2 - x_2 y_1') = a \det(v_1, v_2) + b \det(v_1', v_2)$). (iii) The 3-linear form on $\mathbb{R}^3$ given by $\beta(u, v, w) = u_1 v_2 w_3$ takes the value $\beta(e_1, e_2, e_3) = 1$ and is zero on every other ordered basis triple, illustrating the freedom of choice of coefficients.

---

# Unlocked by This

> [!tip] Alternating Multilinear Form *(LADR §9B)*
> The subclass of multilinear forms that vanish on tuples with a repeated entry. See [[Def - Alternating Multilinear Form]]. The structural theorem $\dim V^{(n)}_{\mathrm{alt}} = 1$ for $n = \dim V$ is the foundation for defining [[Def - Determinant|the determinant]].

> [!tip] Symmetric Multilinear Form
> The subclass of multilinear forms invariant under any permutation of arguments. The dimension is $\binom{n + m - 1}{m}$ — the count of multi-indices with repetition. Symmetric multilinear forms correspond to elements of $\operatorname{Sym}^m(V^*)$, the $m$-th symmetric power of the dual.

> [!tip] Tensor of Type (0, m) *(from Differential Geometry)*
> A smoothly varying family of multilinear forms on tangent spaces — that is, a multilinear-form-valued section of an appropriate tensor bundle. The Riemann curvature tensor is type $(0, 4)$ (symmetrised as $(1, 3)$); the Riemannian metric is $(0, 2)$.

> [!tip] m-th Total Derivative *(from Multivariate Analysis)*
> For a smooth function $f : \mathbb{R}^n \to \mathbb{R}$, the $m$-th total derivative $D^m f(x_0)$ at a point is a *symmetric* $m$-linear form on $\mathbb{R}^n$, given by $D^m f(x_0)(h_1, \dots, h_m) = \frac{\partial^m f}{\partial h_1 \cdots \partial h_m}(x_0)$. The Taylor expansion is $f(x_0 + h) = \sum_{m \geq 0} \frac{1}{m!} D^m f(x_0)(h, \dots, h)$, where each term is a symmetric multilinear form evaluated on the diagonal.

---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Tensor Product of Modules"
  - "Thm - Functoriality of the Tensor Product"
  - "Thm - Standard Isomorphisms of Tensor Products"
  - "Thm - Universal Property of the Tensor Product of Modules"
  - "Def - Free Module"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be a field. This exercise assembles the concrete face of [[Thm - Functoriality of the Tensor Product|functoriality]].

**(a) The Kronecker product.** For $k$-linear maps $T : k^a\to k^b$ and $S : k^c\to k^d$ with matrices $[T], [S]$ in the standard bases, compute the matrix of $T\otimes S : k^a\otimes k^c\to k^b\otimes k^d$ in the lexicographically ordered tensor bases, and show it is the block matrix
$$[T\otimes S] = \big([T]_{\ell i}\,[S]\big)_{\ell, i}\in M_{bd\times ac}(k).$$

**(b) Eigenvalues.** If $A\in M_m(k)$ has eigenvalue $\lambda$ and $B\in M_n(k)$ has eigenvalue $\mu$, show $A\otimes B$ has eigenvalue $\lambda\mu$ and $A\otimes I_n + I_m\otimes B$ has eigenvalue $\lambda+\mu$.

**(c) $V^*\otimes W\cong\operatorname{Hom}(V,W)$.** For finite-dimensional $V, W$, prove the $k$-linear isomorphism $V^*\otimes_k W\cong\operatorname{Hom}_k(V, W)$ sending $\varphi\otimes w\mapsto(v\mapsto\varphi(v)w)$.

**(d) The basis-free trace.** The pairing $V^*\otimes V\to k$, $\varphi\otimes v\mapsto\varphi(v)$, corresponds under (c) to a map $\operatorname{Hom}(V,V)\to k$. Show it is the trace, and deduce $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ for $A\in M_{ab}(k)$, $B\in M_{ba}(k)$ without coordinates.

**(e) Tensor rank.** Define the **rank** of $t\in V^*\otimes W$ as the least number of pure tensors summing to $t$. Show it equals the rank of the corresponding linear map under (c), and compute $\max_{t\in V^*\otimes W}\operatorname{rank}(t)$.

**Recall:**

![[Thm - Functoriality of the Tensor Product#Statement]]

![[Thm - Standard Isomorphisms of Tensor Products#Statement]]

A pure tensor in $V^*\otimes W$ is $\varphi\otimes w$; the rank of $t = \sum_i\varphi_i\otimes w_i$ is the minimal number of terms over all such representations. The standard bases are $e_i$ for $k^a$ (or $k^c$), $f_\ell$ for $k^b$ (or $k^d$); the lexicographic order on $\{e_i\otimes e_j\}$ is $e_1\otimes e_1, \dots, e_1\otimes e_c, e_2\otimes e_1, \dots, e_a\otimes e_c$.

---

# Convergent Strategy

**Problem class.** This is a *make-functoriality-concrete* problem: the abstract map $T\otimes S$ from [[Thm - Functoriality of the Tensor Product]] is turned into an explicit matrix, and the explicit matrix is mined for its spectral data and for the canonical identifications $V^*\otimes W\cong\operatorname{Hom}(V,W)$ and the trace. As the [[Commutative Algebra II — Tensor Products#Problem-Solving Strategy|topic strategy]] notes, every part routes through the [[Thm - Universal Property of the Tensor Product of Modules|universal property]] (to define maps) and the basis $\{e_i\otimes f_j\}$ of free tensors (to compute).

**Assumption pattern.** The trigger throughout is *both factors are free with chosen bases*, so $\{e_i\otimes e_j\}$ is a basis of the tensor product. Once you have a basis, $T\otimes S$ is a matrix, $V^*\otimes W$ has the right dimension to match $\operatorname{Hom}(V,W)$, and rank becomes the matrix rank of a coefficient array. The finite-dimensionality of $V, W$ is what makes $V^*\otimes W\cong\operatorname{Hom}(V,W)$ an isomorphism (not just an injection).

**Theorem routing.** Part (a): expand $T\otimes S$ on basis tensors using $(T\otimes S)(e_i\otimes e_j) = Te_i\otimes Se_j$ ([[Thm - Functoriality of the Tensor Product|functoriality]]) and order the bases. Part (b): an eigenvector pair $(v, w)$ gives $(A\otimes B)(v\otimes w) = Av\otimes Bw = \lambda\mu(v\otimes w)$. Part (c): define $V^*\otimes W\to\operatorname{Hom}(V,W)$ from the bilinear $(\varphi, w)\mapsto(v\mapsto\varphi(v)w)$, and dimension-count via $\dim(V^*\otimes W) = \dim V\cdot\dim W = \dim\operatorname{Hom}(V,W)$ ([[Thm - Standard Isomorphisms of Tensor Products|standard isomorphisms]]). Part (d): the evaluation pairing is basis-free, and computing it on a basis recovers $\sum_i e_i^*(Te_i) = \operatorname{tr}(T)$. Part (e): under (c), a rank-$r$ decomposition of $t$ is a rank-$r$ factorisation of the matrix.

**Key decision point.** The unifying non-obvious recognition is that **a pure tensor $\varphi\otimes w$ corresponds to a rank-one operator $v\mapsto\varphi(v)w$**, so "tensor rank" *is* "operator rank", and "$t$ is pure" *is* "the operator has rank $\leq 1$". This single identification (c) drives (d) — the trace is the canonical contraction $V^*\otimes V\to k$ — and (e) — maximal tensor rank is $\min(\dim V, \dim W)$, the maximal matrix rank. The genuine insight is that the whole circle of facts (Kronecker product, eigenvalue rules, trace, rank) is *one* identification of tensors with matrices, read in different ways.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra II — Tensor Products#Legal Operations|the topic page's Legal Operations]]:

1. **Tensor a map: apply $f\otimes g$ (operation 7).** $T\otimes S$ is the functorial map; its matrix is the Kronecker product, and eigenpairs multiply.

2. **Use that pure tensors of generators generate, and form a basis when free (operation 6).** $\{e_i\otimes e_j\}$ is a basis, making $T\otimes S$ a matrix and giving the dimension count for (c).

3. **Replace a bilinear map by a linear map out of the tensor product (operation 2).** Parts (c), (d) define maps from bilinear data via the universal property.

4. **Build an isomorphism by maps both ways / dimension count (operation 4).** Part (c) is an injection between equal-dimensional spaces, hence an isomorphism.

---

# Hints

> [!note]- Hint 1
> For (a), just expand: $(T\otimes S)(e_i\otimes e_j) = Te_i\otimes Se_j$. Write $Te_i = \sum_\ell[T]_{\ell i}f_\ell$ and $Se_j = \sum_t[S]_{tj}f_t$, multiply out, and read off the coefficient of $f_\ell\otimes f_t$. Then order the basis lexicographically and the block structure appears.

> [!note]- Hint 2
> For (b), if $Av = \lambda v$ and $Bw = \mu w$, then $(A\otimes B)(v\otimes w) = Av\otimes Bw = \lambda v\otimes\mu w = \lambda\mu(v\otimes w)$. For the sum, $(A\otimes I + I\otimes B)(v\otimes w) = Av\otimes w + v\otimes Bw = (\lambda+\mu)(v\otimes w)$.

> [!note]- Hint 3
> For (c), the map $\varphi\otimes w\mapsto(v\mapsto\varphi(v)w)$ comes from the bilinear $(\varphi, w)\mapsto(v\mapsto\varphi(v)w)$. It is injective (a pure tensor maps to a rank-one operator, and an independent set of pure tensors to independent operators); both spaces have dimension $\dim V\cdot\dim W$, so it is an isomorphism.

> [!note]- Hint 4
> For (d), evaluate the contraction $V^*\otimes V\to k$ on the basis $e_i^*\otimes e_j$: it sends this to $e_i^*(e_j) = \delta_{ij}$. Under (c), the operator $e_i^*\otimes e_j$ is the matrix unit $E_{ji}$, and the contraction picks out $\sum_i$ of the $(i,i)$ entries — the trace. Basis-freeness gives $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ since both compute the contraction of $A\otimes B$ paired appropriately.

> [!note]- Hint 5
> For (e), under (c) a representation $t = \sum_{i=1}^r\varphi_i\otimes w_i$ corresponds to the operator $v\mapsto\sum_i\varphi_i(v)w_i$, a sum of $r$ rank-one operators — so its rank is $\leq r$, and the minimal $r$ is exactly the operator rank. The maximum over $t$ is $\min(\dim V, \dim W)$.

---

# Solution

The five parts are one identification — tensors as matrices — read five ways. Step 1 (a) computes the Kronecker matrix by expanding on basis tensors. Step 2 (b) reads eigenvalues off pure-tensor eigenvectors. Step 3 (c) sets up the master isomorphism $V^*\otimes W\cong\operatorname{Hom}(V,W)$ by a dimension count. Step 4 (d) identifies the canonical contraction with the trace. Step 5 (e) reads tensor rank as matrix rank. The non-obvious thread is that "pure tensor = rank-one operator" makes every part a statement about matrices.

**Step 1 (a): The Kronecker block matrix.**

$[T\otimes S] = ([T]_{\ell i}[S])_{\ell, i}$, a $bd\times ac$ block matrix.

> [!note]- Derivation
> By [[Thm - Functoriality of the Tensor Product|functoriality]], on a basis tensor
> $$(T\otimes S)(e_i\otimes e_j) = Te_i\otimes Se_j = \Big(\sum_{\ell=1}^b[T]_{\ell i}f_\ell\Big)\otimes\Big(\sum_{t=1}^d[S]_{tj}f_t\Big) = \sum_{\ell=1}^b\sum_{t=1}^d[T]_{\ell i}[S]_{tj}\,(f_\ell\otimes f_t).$$
> Order the source basis $\{e_i\otimes e_j\}$ lexicographically (block index $i = 1,\dots,a$, inner index $j = 1,\dots,c$) and likewise the target basis $\{f_\ell\otimes f_t\}$. The column of $[T\otimes S]$ indexed by $(i,j)$ has entry $[T]_{\ell i}[S]_{tj}$ in row $(\ell, t)$. Grouping by the block indices $(\ell, i)$, the $(\ell, i)$ block is the $d\times c$ matrix $([S]_{tj})_{t,j}$ scaled by $[T]_{\ell i}$, i.e. $[T]_{\ell i}[S]$. So
> $$[T\otimes S] = \begin{pmatrix}[T]_{11}[S] & \cdots & [T]_{1a}[S]\\ \vdots & & \vdots\\ [T]_{b1}[S] & \cdots & [T]_{ba}[S]\end{pmatrix}\in M_{bd\times ac}(k),$$
> the Kronecker product. (Consequences: $\operatorname{tr}(T\otimes S) = \operatorname{tr}(T)\operatorname{tr}(S)$ and, for square $T, S$, $\det(T\otimes S) = (\det T)^d(\det S)^b$.)

**Step 2 (b): Eigenvalues multiply (and add).**

$A\otimes B$ has eigenvalue $\lambda\mu$; $A\otimes I + I\otimes B$ has eigenvalue $\lambda+\mu$.

> [!note]- Derivation
> Let $Av = \lambda v$ ($v\neq 0$) and $Bw = \mu w$ ($w\neq 0$). The pure tensor $v\otimes w$ is nonzero (it is a basis-style tensor of nonzero vectors in free modules). Then
> $$(A\otimes B)(v\otimes w) = (Av)\otimes(Bw) = (\lambda v)\otimes(\mu w) = \lambda\mu(v\otimes w),$$
> so $\lambda\mu$ is an eigenvalue with eigenvector $v\otimes w$. And
> $$(A\otimes I_n + I_m\otimes B)(v\otimes w) = Av\otimes w + v\otimes Bw = \lambda(v\otimes w)+\mu(v\otimes w) = (\lambda+\mu)(v\otimes w),$$
> so $\lambda+\mu$ is an eigenvalue. (Over an algebraically closed field, ranging over all eigenpairs gives *all* eigenvalues of $A\otimes B$ as products $\lambda_i\mu_j$ and of $A\otimes I + I\otimes B$ as sums $\lambda_i+\mu_j$.)

**Step 3 (c): $V^*\otimes W\cong\operatorname{Hom}(V,W)$.**

The map $\varphi\otimes w\mapsto(v\mapsto\varphi(v)w)$ is a $k$-linear isomorphism.

> [!note]- Derivation
> The map $\beta : V^*\times W\to\operatorname{Hom}(V, W)$, $\beta(\varphi, w) = (v\mapsto\varphi(v)w)$, is $k$-bilinear (linear in $\varphi$ and in $w$). By the [[Thm - Universal Property of the Tensor Product of Modules|universal property]] it induces $\Theta : V^*\otimes W\to\operatorname{Hom}(V, W)$ with $\Theta(\varphi\otimes w) = (v\mapsto\varphi(v)w)$.
>
> *Injective.* Take a basis $\{w_j\}$ of $W$ and write $t = \sum_j\varphi_j\otimes w_j$ (collect terms by the $W$-basis). If $\Theta(t) = 0$, then for every $v$, $\sum_j\varphi_j(v)w_j = 0$; independence of $\{w_j\}$ forces $\varphi_j(v) = 0$ for all $v, j$, so each $\varphi_j = 0$ and $t = 0$.
>
> *Surjective by dimension.* By the [[Thm - Standard Isomorphisms of Tensor Products|standard isomorphisms]], $\dim_k(V^*\otimes W) = \dim V^*\cdot\dim W = \dim V\cdot\dim W = \dim\operatorname{Hom}_k(V, W)$. An injection between finite-dimensional spaces of equal dimension is an isomorphism. (Concretely, $\Theta(e_i^*\otimes f_j)$ is the rank-one operator $E_{ji}$ sending $e_i\mapsto f_j$ and other basis vectors to $0$; these are a basis of $\operatorname{Hom}(V,W)$.)

**Step 4 (d): The contraction is the trace, and $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.**

The pairing $V^*\otimes V\to k$, $\varphi\otimes v\mapsto\varphi(v)$, is the trace under (c), giving cyclicity basis-free.

> [!note]- Derivation
> The evaluation pairing $\operatorname{ev} : V^*\otimes V\to k$, $\operatorname{ev}(\varphi\otimes v) = \varphi(v)$, is bilinear, hence well-defined. Under $\Theta$ (with $W = V$), $\varphi\otimes v$ corresponds to the operator $u\mapsto\varphi(u)v$. Compute $\operatorname{ev}$ on the basis $e_i^*\otimes e_j$: $\operatorname{ev}(e_i^*\otimes e_j) = e_i^*(e_j) = \delta_{ij}$. Under $\Theta$ this is the matrix unit $E_{ji}$, whose trace is $\delta_{ij}$. So $\operatorname{ev}\circ\Theta^{-1} = \operatorname{tr}$ on the basis $\{E_{ji}\}$ of $\operatorname{Hom}(V,V)$, hence everywhere: **the trace is the canonical contraction $V^*\otimes V\to k$, no basis chosen.**
>
> *Cyclicity.* For $A : k^b\to k^a$ (so $A\in M_{ab}$) and $B : k^a\to k^b$ (so $B\in M_{ba}$), both $AB\in\operatorname{End}(k^a)$ and $BA\in\operatorname{End}(k^b)$ correspond under $\Theta$ to the same element of the symmetric pairing $V^*\otimes V$ contracted in the two possible orders; since the contraction is basis-free and symmetric in the two factors of $A\otimes B$, $\operatorname{tr}(AB) = \operatorname{tr}(BA)$. (Coordinate check, for confirmation: $\operatorname{tr}(AB) = \sum_{i,k}A_{ik}B_{ki} = \sum_{k,i}B_{ki}A_{ik} = \operatorname{tr}(BA)$.) The basis-free derivation makes change-of-basis invariance of the trace automatic, since the contraction never referred to a basis.

**Step 5 (e): Tensor rank equals operator rank.**

$\operatorname{rank}(t) = \operatorname{rank}(\Theta(t))$, and $\max_t\operatorname{rank}(t) = \min(\dim V, \dim W)$.

> [!note]- Derivation
> Under $\Theta$, a representation $t = \sum_{i=1}^r\varphi_i\otimes w_i$ corresponds to $\Theta(t) = \big(v\mapsto\sum_{i=1}^r\varphi_i(v)w_i\big)$, a sum of $r$ rank-one operators, so $\operatorname{rank}\Theta(t)\leq r$. Hence the minimal $r$ over all representations — the tensor rank — is at least $\operatorname{rank}\Theta(t)$. Conversely, factor the operator $\Theta(t) = \sum_{i=1}^{\rho}\psi_i\otimes u_i$ as a sum of $\rho = \operatorname{rank}\Theta(t)$ rank-one operators (singular-value / rank factorisation), giving a length-$\rho$ tensor representation. So $\operatorname{rank}(t) = \operatorname{rank}(\Theta(t))$: **tensor rank = matrix rank**, and a tensor is pure iff its operator has rank $\leq 1$.
>
> The rank of an operator $V\to W$ is at most $\min(\dim V, \dim W)$, and this is attained (by any full-rank map). Therefore $\max_{t\in V^*\otimes W}\operatorname{rank}(t) = \min(\dim V, \dim W)$.

> [!note]- Complete formal solution
> **(a)** $(T\otimes S)(e_i\otimes e_j) = Te_i\otimes Se_j = \sum_{\ell,t}[T]_{\ell i}[S]_{tj}f_\ell\otimes f_t$; lexicographic ordering yields the block matrix $[T\otimes S] = ([T]_{\ell i}[S])_{\ell,i}\in M_{bd\times ac}(k)$.
>
> **(b)** $Av = \lambda v$, $Bw = \mu w$ give $(A\otimes B)(v\otimes w) = \lambda\mu(v\otimes w)$ and $(A\otimes I + I\otimes B)(v\otimes w) = (\lambda+\mu)(v\otimes w)$.
>
> **(c)** The bilinear $(\varphi, w)\mapsto(v\mapsto\varphi(v)w)$ induces $\Theta : V^*\otimes W\to\operatorname{Hom}(V,W)$, injective (collect by a $W$-basis; vanishing forces each functional zero) and surjective by $\dim(V^*\otimes W) = \dim V\dim W = \dim\operatorname{Hom}(V,W)$.
>
> **(d)** The contraction $\operatorname{ev}(\varphi\otimes v) = \varphi(v)$ sends $e_i^*\otimes e_j\mapsto\delta_{ij}$, matching $\operatorname{tr}(E_{ji})$; so $\operatorname{ev} = \operatorname{tr}\circ\Theta$ is the basis-free trace, and symmetry of the contraction gives $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
>
> **(e)** $\Theta$ carries a length-$r$ tensor representation to a sum of $r$ rank-one operators, so $\operatorname{rank}(t) = \operatorname{rank}\Theta(t)$, with maximum $\min(\dim V, \dim W)$. $\blacksquare$

---

# Key Takeaways

**One identification — $V^*\otimes W\cong\operatorname{Hom}(V,W)$, pure tensor $\leftrightarrow$ rank-one operator — generates the whole circle of facts.** The deepest lesson is that the Kronecker product, the eigenvalue rules, the basis-free trace, and tensor rank are not four separate results but four readings of the single isomorphism $\Theta$. A pure tensor $\varphi\otimes w$ *is* the rank-one operator $v\mapsto\varphi(v)w$; so "purity" is "rank $\leq 1$", "tensor rank" is "operator rank", the canonical contraction $V^*\otimes V\to k$ is the trace, and tensoring operators is the Kronecker product. The trigger for spaced recall: whenever you meet a tensor of dual-and-space type, immediately translate to operators, where matrix intuition takes over. This identification is also the bridge to quantum information, where $\mathcal{H}_A^*\otimes\mathcal{H}_B$ describes channels and the Schmidt rank *is* this tensor rank.

**Eigenvalues multiply for $\otimes$ and add for $\otimes I + I\otimes$ — the spectrum of a composite from the spectra of the parts.** The pure-tensor eigenvector $v\otimes w$ is the entire content: it is simultaneously an eigenvector of $A\otimes B$ (eigenvalue $\lambda\mu$) and of $A\otimes I + I\otimes B$ (eigenvalue $\lambda+\mu$). The transferable diagnostic: whenever a large operator decomposes as a Kronecker product or a Kronecker sum, you never diagonalise the big matrix — you read its spectrum off the two small spectra. This is exactly how the energy levels of a non-interacting composite quantum system are the *sums* $E_i + E_j$ (the Hamiltonian is $H_1\otimes I + I\otimes H_2$), and how the Sylvester/Lyapunov equation $AX + XB = C$ is solved by the eigenvalue-sum condition. The pattern "composite spectrum = combine the part spectra" is one of the highest-leverage facts in applied linear algebra, and it is a one-line consequence of functoriality on eigenvectors.

**Basis-free definitions make invariance automatic — define the trace as a contraction, not a sum of diagonal entries.** The trace, defined the usual way as $\sum_i A_{ii}$, requires a separate proof that it is invariant under change of basis. Defined as the canonical contraction $V^*\otimes V\to k$, invariance is *free*, because the contraction never mentioned a basis — and $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ falls out of the symmetry of the pairing rather than a coordinate computation. The general principle for spaced practice: when a quantity is defined by a formula in coordinates but is "really" basis-independent, look for the canonical (universal-property) definition; it both proves invariance and reveals the quantity's true nature. The determinant has the same story via $\Lambda^n$, and the same move underlies the basis-free Chern–Weil definitions of characteristic classes. The contrast with [[Ex - A pure tensor that is zero without either factor being zero]] is instructive: there the *base ring* matters and the same symbol means different things; here the *basis* does not matter and the canonical map sees through it.

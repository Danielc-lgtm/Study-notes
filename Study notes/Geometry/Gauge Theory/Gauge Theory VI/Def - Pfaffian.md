---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Alternating Multilinear Form"
  - "Def - Determinant"
  - "Thm - Lie Algebras and Dimensions of the Classical Matrix Groups"
  - "Def - Ad-Invariant Polynomial"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $m\ge1$ is a fixed integer and we work over $\mathbb{R}$. We write $\operatorname{Mat}(n\times n;\mathbb{R})$ for the real $n\times n$ matrices and, for a matrix $A$, we write $A_{ij}$ for its entry in row $i$ and column $j$ and $A^t$ for its transpose, $(A^t)_{ij}=A_{ji}$. A matrix $A$ is **skew-symmetric** (equivalently **antisymmetric**) if $A^t=-A$, that is $A_{ji}=-A_{ij}$ for all $i,j$; in particular $A_{ii}=0$. By the classification of the Lie algebras of the classical matrix groups, [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]], the Lie algebra of the special orthogonal group $SO(n)$ is exactly the space of skew-symmetric matrices,
$$\mathfrak{so}(n)=\{A\in\operatorname{Mat}(n\times n;\mathbb{R}):A^t+A=0\},\qquad \dim\mathfrak{so}(n)=\frac{n(n-1)}{2},$$
and this is the object on which the Pfaffian lives. We only ever take $n=2m$ even.

We write $S_N$ for the symmetric group on $\{1,\dots,N\}$ and $\operatorname{sign}(\sigma)\in\{+1,-1\}$ for the sign of a permutation $\sigma\in S_N$. We write $\det A$ for the [[Def - Determinant|determinant]] of $A$, the unique [[Def - Alternating Multilinear Form|alternating multilinear]] function of the columns normalised by $\det I=1$; concretely $\det A=\sum_{\sigma\in S_N}\operatorname{sign}(\sigma)\prod_{i=1}^N A_{i\,\sigma(i)}$.

Let $(e_1,\dots,e_{2m})$ be the standard ordered basis of $\mathbb{R}^{2m}$. We use the exterior algebra $\Lambda^\bullet\mathbb{R}^{2m}$ with its wedge product $\wedge$; for a $2$-vector we write $e_i\wedge e_j=-e_j\wedge e_i$, and $\Lambda^{2m}\mathbb{R}^{2m}$ is one-dimensional, spanned by $e_1\wedge\dots\wedge e_{2m}$. We fix once and for all the linear identification
$$\Lambda^{2m}\mathbb{R}^{2m}\;\xrightarrow{\ \cong\ }\;\mathbb{R},\qquad e_1\wedge\dots\wedge e_{2m}\longmapsto 1,$$
which uses the standard ordering (equivalently the standard orientation) of $\mathbb{R}^{2m}$; every occurrence of "$\in\mathbb{R}$" for a top-degree form below is via this identification. The wedge product and its sign rule $\alpha\wedge\beta=(-1)^{(\deg\alpha)(\deg\beta)}\beta\wedge\alpha$ are the ones established on [[Thm - Wedge Product Properties]]; even-degree forms therefore commute among themselves, a fact we use repeatedly. The exterior powers $\Lambda^k V^*$ and their basis are as on [[Def - Alternating Tensor and Lambda k V Dual]].

To each $A\in\mathfrak{so}(2m)$ we attach the $2$-vector
$$\sigma_A:=\sum_{1\le i<j\le 2m}A_{ij}\,e_i\wedge e_j\;\in\;\Lambda^2\mathbb{R}^{2m}.$$
The symbol $\operatorname{Pf}$ denotes the Pfaffian, defined below. An [[Def - Ad-Invariant Polynomial|invariant polynomial]] on a Lie algebra $\mathfrak{g}$ means a polynomial map $p\colon\mathfrak{g}\to\mathbb{R}$ that is homogeneous and invariant under the adjoint action of the group; the claim that $\operatorname{Pf}$ is such a polynomial on $\mathfrak{so}(2m)$ is stated and proved on [[Thm - Properties of the Pfaffian]] and only quoted here.

> [!warning] Convention: Bär's normalisation of the Pfaffian
> The source (Bär, *Gauge Theory*, Example 2.5.14) defines a symmetric $m$-linear map $\lambda\colon\mathfrak{so}(2m)^m\to\mathbb{R}$ by $\lambda(\sigma_1,\dots,\sigma_m):=\sigma_1\wedge\dots\wedge\sigma_m$ (each $\sigma_k$ regarded as a $2$-vector, the wedge landing in $\Lambda^{2m}\mathbb{R}^{2m}\cong\mathbb{R}$) and then calls the map $\sigma\mapsto\lambda(\sigma,\dots,\sigma)$ "the Pfaffian". That object equals $m!\operatorname{Pf}$ in the normalisation used on this page and throughout the series (proved in **The Definition** below). Consequently Bär's Euler-class formula $\big[\operatorname{Pf}_{\text{Bär}}(\bar\Omega)\big/((2\pi)^m m!)\big]$ is identical to the series' $\big[\operatorname{Pf}(\bar\Omega/2\pi)\big]$; the factor $m!$ in Bär's denominator is exactly the discrepancy between the two normalisations, and the two Euler classes agree. The series uses $\operatorname{Pf}$ as defined below, with $\operatorname{Pf}\left(\begin{smallmatrix}0&a\\-a&0\end{smallmatrix}\right)=a$.

---

# Axiom Motivation

The problem the Pfaffian solves is a very concrete one. We want a characteristic class for oriented real vector bundles of even rank $2m$ — the [[Def - Euler Class of an Oriented Vector Bundle|Euler class]] — built by the Chern–Weil recipe, which turns an invariant polynomial on the structure Lie algebra into a closed differential form in the curvature. For a bundle with a Euclidean structure the structure group is reduced to $SO(2m)$ and the curvature, read in an oriented orthonormal frame, is a $2$-form with values in $\mathfrak{so}(2m)$: at each point it is a skew-symmetric matrix of $2$-forms. To manufacture a $2m$-form (a top form on a $2m$-manifold, so something we can integrate) we must feed this skew matrix of $2$-forms into a homogeneous invariant polynomial of degree $m$. The determinant is a natural candidate, but it has degree $2m$, not $m$; on skew matrices the determinant turns out to be a perfect square, and its square root — a polynomial of the right degree $m$ — is precisely what we are after. That square root is the Pfaffian. So the object is forced on us by a counting of degrees: **we need the degree-$m$ invariant of a $2m\times2m$ skew matrix, and the determinant's honest square root is it.**

Why not simply use the determinant, or the coefficients of the characteristic polynomial, and be done? Because on $\mathfrak{so}(2m)$ those invariants are exactly the Pontryagin data, and they are *even* in a sense that makes them blind to orientation: they are invariant not only under $SO(2m)$ but under the full orthogonal group $O(2m)$. The Euler class is a genuinely oriented invariant — reversing the orientation of the bundle must negate it (this is what lets it count zeros of a section with sign) — so it cannot be a function of the $O(2m)$-invariants alone. The Pfaffian is the one new invariant that appears when the structure group is cut down from $O(2m)$ to $SO(2m)$: it is $SO(2m)$-invariant but changes sign under an orientation-reversing orthogonal change of basis. Dropping the requirement "orientation-sensitive" would collapse the Pfaffian back into $\pm\sqrt{\det}$ with an ambiguous sign, and the Euler class would be defined only up to sign — losing precisely the information (the *signed* count of zeros, the Euler characteristic) that the class exists to carry.

Now to the two structural choices in the definition itself, and what breaks if either is weakened. First, **restriction to skew-symmetric matrices.** The determinant of a general matrix is not a square; $\det\left(\begin{smallmatrix}1&0\\0&2\end{smallmatrix}\right)=2$ has no polynomial square root in the entries. It is only on the skew-symmetric matrices that $\det$ factors as a square of a polynomial, and only there that the Pfaffian is defined. If we tried to write the same alternating sum for a symmetric or a general matrix, the resulting expression would no longer square to the determinant and would have no invariance property worth having; we record this below as the principal non-example. Second, **even size $2m$.** For an odd-size skew matrix $A$ of size $(2m+1)$ we have $\det A=\det(A^t)=\det(-A)=(-1)^{2m+1}\det A=-\det A$, so $\det A=0$: an odd-size skew matrix is always singular, its determinant is identically zero, and there is nothing to take a square root of. The defining sum below would try to pair up an odd number of indices and simply cannot: a "product over $m$ pairs covering all $2m+1$ indices" does not exist. Evenness is not a convenience; it is the exact condition under which the object is non-trivial.

These two constraints together explain the shape of the formula. We must produce a single scalar out of a skew matrix, of degree $m$ in the entries, alternating enough that it changes sign correctly under orthogonal changes of basis, and squaring to the determinant. The unique such polynomial (up to overall sign, fixed below by the normalisation $\operatorname{Pf}(J)=1$ for the standard block matrix $J=\operatorname{diag}\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix},\dots,\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\in\mathfrak{so}(2m)$, the block-diagonal example computed below) is a signed sum over *perfect matchings* of the index set $\{1,\dots,2m\}$: split the indices into $m$ disjoint pairs, take the product of the corresponding above-diagonal entries, weight by the sign of the pairing, and add. A reader who has internalised "degree $m$, skew, orientation-odd, squares to $\det$" can reconstruct exactly this expression, which is the test the definition should pass.

---

# The Definition

Let $A\in\mathfrak{so}(2m)$ be a $2m\times2m$ skew-symmetric real matrix. The **Pfaffian** of $A$ is the real number
$$\operatorname{Pf}(A):=\frac{1}{2^m\,m!}\sum_{\sigma\in S_{2m}}\operatorname{sign}(\sigma)\prod_{i=1}^{m}A_{\sigma(2i-1)\,\sigma(2i)}.$$
It is a homogeneous polynomial of degree $m$ in the entries of $A$: each summand is a product of exactly $m$ entries.

**The smallest case, $m=1$.** Here $2m=2$ and the only skew $2\times2$ matrix is $A=\left(\begin{smallmatrix}0&a\\-a&0\end{smallmatrix}\right)$ with $a=A_{12}$. The group $S_2=\{\mathrm{id},(1\,2)\}$ contributes
$$\operatorname{Pf}(A)=\frac{1}{2^1\cdot1!}\Big(\operatorname{sign}(\mathrm{id})\,A_{12}+\operatorname{sign}((1\,2))\,A_{21}\Big)=\frac12\big(A_{12}-A_{21}\big)=\frac12\big(a-(-a)\big)=a.$$
So $\operatorname{Pf}\left(\begin{smallmatrix}0&a\\-a&0\end{smallmatrix}\right)=a$: the Pfaffian of the basic $2\times2$ rotation generator is simply its upper-right entry. This is the normalisation the whole series uses, and it is why the Euler class of an oriented plane bundle will turn out to equal the first Chern class of the corresponding Hermitian line bundle.

## The equivalent exterior-algebra form

The same number is produced by wedging the associated $2$-vector $\sigma_A=\sum_{i<j}A_{ij}\,e_i\wedge e_j$ with itself $m$ times.

> [!note]- Proposition (the two formulas agree). For every $A\in\mathfrak{so}(2m)$,
> $$\frac{1}{m!}\,\sigma_A^{\wedge m}=\operatorname{Pf}(A)\,e_1\wedge\dots\wedge e_{2m}\quad\text{in }\Lambda^{2m}\mathbb{R}^{2m},$$
> equivalently, under the identification $\Lambda^{2m}\mathbb{R}^{2m}\cong\mathbb{R}$, $\ \tfrac{1}{m!}\sigma_A^{\wedge m}=\operatorname{Pf}(A)$.
>
> > [!note]- Full proof
> > **Goal.** We are given the skew matrix $A$ and the $2$-vector $\sigma_A=\sum_{i<j}A_{ij}e_i\wedge e_j$; we must show that $\tfrac{1}{m!}\sigma_A^{\wedge m}$, expanded in the basis $e_1\wedge\dots\wedge e_{2m}$ of $\Lambda^{2m}\mathbb{R}^{2m}$, has coefficient equal to the alternating sum defining $\operatorname{Pf}(A)$.
> >
> > **Step 1: symmetrise the index range.** For each ordered pair $(i,j)$ we have $A_{ij}\,e_i\wedge e_j=A_{ji}\,e_j\wedge e_i$, since $A_{ij}=-A_{ji}$ (skew-symmetry) and $e_i\wedge e_j=-e_j\wedge e_i$ (antisymmetry of the wedge on $1$-vectors, [[Thm - Wedge Product Properties]]) contribute two sign changes that cancel; the diagonal terms $A_{ii}\,e_i\wedge e_i=0$ vanish because $A_{ii}=0$ and $e_i\wedge e_i=0$. Therefore the sum over $i<j$ is exactly half the sum over all ordered pairs,
> > $$\sigma_A=\sum_{1\le i<j\le 2m}A_{ij}\,e_i\wedge e_j=\frac12\sum_{i,j=1}^{2m}A_{ij}\,e_i\wedge e_j\qquad\text{(each unordered pair counted twice, diagonal zero).}$$
> >
> > **Step 2: expand the $m$-th wedge power.** Multiplying out the $m$-fold wedge of this symmetrised sum and using multilinearity of $\wedge$,
> > $$\sigma_A^{\wedge m}=\frac{1}{2^m}\sum_{i_1,j_1,\dots,i_m,j_m=1}^{2m}A_{i_1 j_1}\cdots A_{i_m j_m}\;e_{i_1}\wedge e_{j_1}\wedge\dots\wedge e_{i_m}\wedge e_{j_m}\qquad\text{(distributivity of }\wedge\text{ over the sums; the factor }2^{-m}\text{ from Step 1).}$$
> >
> > **Step 3: only permutations of $\{1,\dots,2m\}$ survive.** A wedge $e_{k_1}\wedge\dots\wedge e_{k_{2m}}$ of $2m$ basis $1$-vectors is nonzero if and only if the indices $k_1,\dots,k_{2m}$ are pairwise distinct, that is, if and only if $(k_1,\dots,k_{2m})=(\tau(1),\dots,\tau(2m))$ for a unique permutation $\tau\in S_{2m}$; in that case
> > $$e_{\tau(1)}\wedge\dots\wedge e_{\tau(2m)}=\operatorname{sign}(\tau)\,e_1\wedge\dots\wedge e_{2m}\qquad\text{(reordering into standard order picks up the factor }\operatorname{sign}(\tau)\text{, by the wedge reordering rule).}$$
> > Here the reordering rule is the one on [[Thm - Wedge Product Properties]]: an odd transposition of adjacent factors changes the sign, so a permutation $\tau$ of the factors contributes $\operatorname{sign}(\tau)$.
> > Writing the surviving index string as $(i_1,j_1,\dots,i_m,j_m)=(\tau(1),\tau(2),\dots,\tau(2m-1),\tau(2m))$, so that $i_k=\tau(2k-1)$ and $j_k=\tau(2k)$, the sum in Step 2 collapses to a sum over $\tau\in S_{2m}$:
> > $$\sigma_A^{\wedge m}=\frac{1}{2^m}\sum_{\tau\in S_{2m}}\operatorname{sign}(\tau)\;\prod_{k=1}^{m}A_{\tau(2k-1)\,\tau(2k)}\;\;e_1\wedge\dots\wedge e_{2m}\qquad\text{(substituting the previous display).}$$
> >
> > **Step 4: divide by $m!$ and compare.** Dividing both sides by $m!$,
> > $$\frac{1}{m!}\,\sigma_A^{\wedge m}=\left(\frac{1}{2^m\,m!}\sum_{\tau\in S_{2m}}\operatorname{sign}(\tau)\prod_{k=1}^{m}A_{\tau(2k-1)\,\tau(2k)}\right)e_1\wedge\dots\wedge e_{2m}=\operatorname{Pf}(A)\,e_1\wedge\dots\wedge e_{2m},$$
> > where the last equality is the definition of $\operatorname{Pf}(A)$ (with the bound variable $\tau$ renamed $\sigma$).
> >
> > **Conclusion.** The exterior-algebra expression $\tfrac{1}{m!}\sigma_A^{\wedge m}$ and the alternating sum define the same real number $\operatorname{Pf}(A)$. $\blacksquare$

## The combinatorial (perfect-matching) form

The alternating sum over all of $S_{2m}$ visibly overcounts, because many permutations describe the same unordered splitting of $\{1,\dots,2m\}$ into pairs. Collecting them gives the form used in hand computation.

> [!note]- Proposition (Pfaffian as a signed sum over matchings). Let a **perfect matching** of $\{1,\dots,2m\}$ be a partition $M=\{\{p_1,q_1\},\dots,\{p_m,q_m\}\}$ into $m$ two-element blocks; order each block so that $p_k<q_k$, and let $\pi_M\in S_{2m}$ be the permutation $\pi_M=(p_1,q_1,\dots,p_m,q_m)$ (read as the word listing the blocks in increasing order of their smaller element). Then
> $$\operatorname{Pf}(A)=\sum_{M}\operatorname{sign}(\pi_M)\prod_{k=1}^{m}A_{p_k q_k},$$
> the sum ranging over the $(2m-1)!!=(2m-1)(2m-3)\cdots 3\cdot 1$ perfect matchings.
>
> > [!note]- Full proof
> > **Goal.** Group the $(2m)!$ permutations in the defining sum according to the matching they induce, and show that each matching's $2^m m!$ permutations contribute equal terms, so that the prefactor $\tfrac{1}{2^m m!}$ exactly cancels the multiplicity.
> >
> > **Step 1: the map from permutations to matchings.** Each $\sigma\in S_{2m}$ determines the matching $M(\sigma)=\big\{\{\sigma(1),\sigma(2)\},\dots,\{\sigma(2m-1),\sigma(2m)\}\big\}$. Two operations change $\sigma$ without changing $M(\sigma)$: (a) swapping the two entries inside one block, $\sigma(2k-1)\leftrightarrow\sigma(2k)$; and (b) permuting the $m$ blocks among themselves. Every $\sigma$ with $M(\sigma)=M$ is obtained from the reference permutation $\pi_M$ by a sequence of such operations, and there are exactly $2^m$ within-block swaps and $m!$ block permutations, giving $2^m m!$ permutations in the fibre over each matching $M$; since $(2m)!=2^m m!\,(2m-1)!!$, the fibres partition $S_{2m}$.
> >
> > **Step 2: within-block swaps preserve the summand.** Swapping $\sigma(2k-1)\leftrightarrow\sigma(2k)$ is a transposition, so it multiplies $\operatorname{sign}(\sigma)$ by $-1$; it also replaces the factor $A_{\sigma(2k-1)\sigma(2k)}$ by $A_{\sigma(2k)\sigma(2k-1)}=-A_{\sigma(2k-1)\sigma(2k)}$ (skew-symmetry), multiplying the product by $-1$. The two sign changes cancel, so $\operatorname{sign}(\sigma)\prod_k A_{\sigma(2k-1)\sigma(2k)}$ is unchanged.
> >
> > **Step 3: block permutations preserve the summand.** Permuting the blocks by $\rho\in S_m$ replaces $\sigma$ by $\sigma'$ with $(\sigma'(2k-1),\sigma'(2k))=(\sigma(2\rho(k)-1),\sigma(2\rho(k)))$. This rearranges the $2m$ output slots by a permutation that moves entire adjacent pairs; such a permutation is a product of transpositions of blocks, each of which is an *even* permutation of the $2m$ letters (a swap of two disjoint adjacent pairs is a product of two transpositions), so $\operatorname{sign}(\sigma')=\operatorname{sign}(\sigma)$. The product $\prod_k A_{\sigma'(2k-1)\sigma'(2k)}=\prod_k A_{\sigma(2\rho(k)-1)\sigma(2\rho(k))}$ is the same product of factors in a different order, hence unchanged (multiplication in $\mathbb{R}$ is commutative). So again the summand is unchanged.
> >
> > **Step 4: reduce and normalise the reference term.** By Steps 2–3 every one of the $2^m m!$ permutations in the fibre over $M$ contributes the identical value $\operatorname{sign}(\pi_M)\prod_{k}A_{p_k q_k}$ (evaluating at the reference $\pi_M$, whose blocks are ordered with $p_k<q_k$). Therefore
> > $$\operatorname{Pf}(A)=\frac{1}{2^m m!}\sum_{\sigma\in S_{2m}}\operatorname{sign}(\sigma)\prod_{i=1}^{m}A_{\sigma(2i-1)\sigma(2i)}=\frac{1}{2^m m!}\sum_{M}\big(2^m m!\big)\,\operatorname{sign}(\pi_M)\prod_{k=1}^{m}A_{p_k q_k}=\sum_{M}\operatorname{sign}(\pi_M)\prod_{k=1}^{m}A_{p_k q_k},$$
> > combining the fibre partition of Step 1 with the constancy of the summand on each fibre.
> >
> > **Conclusion.** The Pfaffian is the signed sum, over the $(2m-1)!!$ perfect matchings, of the products of above-diagonal entries; the counting factor $2^m m!$ is exactly the size of each fibre. $\blacksquare$

## The identification $\mathfrak{so}(2m)\cong\Lambda^2\mathbb{R}^{2m}$ and Bär's $\lambda$

The exterior-algebra form rests on the map $A\mapsto\sigma_A$ used above; we record that it is an isomorphism and that Bär's multilinear form $\lambda$ is genuinely symmetric multilinear, since both facts underlie the Convention callout and the Euler-class construction.

> [!note]- Corollary (structure of the identification). (i) The map $\Phi\colon\mathfrak{so}(2m)\to\Lambda^2\mathbb{R}^{2m}$, $\Phi(A)=\sigma_A=\sum_{i<j}A_{ij}e_i\wedge e_j$, is a linear isomorphism. (ii) The map $\lambda\colon\mathfrak{so}(2m)^m\to\mathbb{R}$, $\lambda(A_1,\dots,A_m):=\sigma_{A_1}\wedge\dots\wedge\sigma_{A_m}$ (via $\Lambda^{2m}\mathbb{R}^{2m}\cong\mathbb{R}$), is symmetric and multilinear, and $\lambda(A,\dots,A)=\sigma_A^{\wedge m}=m!\operatorname{Pf}(A)$.
>
> > [!note]- Full proof
> > **Part (i): linear isomorphism.** $\Phi$ is linear because each coefficient map $A\mapsto A_{ij}$ is linear and $\Phi$ is their linear combination with fixed basis $2$-vectors. It is injective: if $\Phi(A)=0$ then, since the $2$-vectors $\{e_i\wedge e_j\}_{i<j}$ are linearly independent in $\Lambda^2\mathbb{R}^{2m}$ ([[Def - Alternating Tensor and Lambda k V Dual]]), all coefficients $A_{ij}=0$ for $i<j$; skew-symmetry then forces $A_{ji}=-A_{ij}=0$ and $A_{ii}=0$, so $A=0$. Both spaces have the same finite dimension, $\dim\mathfrak{so}(2m)=\tfrac{2m(2m-1)}2=\binom{2m}{2}=\dim\Lambda^2\mathbb{R}^{2m}$ (the first by [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]], the second by counting basis elements $e_i\wedge e_j$, $i<j$), so an injective linear map between them is an isomorphism.
> >
> > **Part (ii): multilinearity.** For fixed arguments in all but one slot, $\lambda(A_1,\dots,A_m)=\sigma_{A_1}\wedge\dots\wedge\sigma_{A_m}$ is linear in the varying slot because $A\mapsto\sigma_A$ is linear (Part (i)) and the wedge product is multilinear ([[Thm - Wedge Product Properties]]). Hence $\lambda$ is multilinear.
> >
> > **Part (ii): symmetry.** Each $\sigma_{A_k}$ is a $2$-vector, that is an even-degree element of $\Lambda^\bullet\mathbb{R}^{2m}$. By the graded-commutativity rule $\alpha\wedge\beta=(-1)^{(\deg\alpha)(\deg\beta)}\beta\wedge\alpha$ ([[Thm - Wedge Product Properties]]), two even-degree forms commute: $\sigma_{A_k}\wedge\sigma_{A_l}=(-1)^{2\cdot2}\sigma_{A_l}\wedge\sigma_{A_k}=\sigma_{A_l}\wedge\sigma_{A_k}$. Since any permutation of the $m$ factors is a composition of adjacent transpositions, each of which leaves the wedge unchanged, $\lambda$ is invariant under every permutation of its arguments; that is, $\lambda$ is symmetric.
> >
> > **Diagonal value.** Setting all arguments equal to $A$ gives $\lambda(A,\dots,A)=\sigma_A^{\wedge m}$, which by the Proposition above equals $m!\operatorname{Pf}(A)\,e_1\wedge\dots\wedge e_{2m}$, that is $m!\operatorname{Pf}(A)$ under the identification. This is Bär's $\operatorname{Pf}_{\text{Bär}}=\lambda(\sigma,\dots,\sigma)=m!\operatorname{Pf}$, as recorded in the Convention callout. $\blacksquare$

---

# Relate to Other Fields / Compression

**True name.** The Pfaffian is the *square root of the determinant on skew-symmetric matrices*, with its sign pinned down by orientation. On $\mathfrak{so}(2m)$ the determinant is a perfect square of a polynomial, $\det A=\operatorname{Pf}(A)^2$ ([[Thm - Properties of the Pfaffian]], clause (b)); the Pfaffian is the honest polynomial square root, of degree $m$ rather than $2m$, and unlike $\pm\sqrt{\det A}$ it is a genuine polynomial in the entries with a definite sign. Operationally, when you meet a $2m\times 2m$ antisymmetric object and want a *signed* invariant of degree $m$ — one that flips under orientation reversal and squares to the determinant — the Pfaffian is that invariant, and the fastest way to compute it is the signed sum over perfect matchings rather than the defining sum over $S_{2m}$.

This gives the Pfaffian three faces, each dominant in a different field. In **multilinear algebra and Lie theory** it is the top invariant polynomial that distinguishes $SO(2m)$ from $O(2m)$: the ring of $O(2m)$-invariant polynomials on $\mathfrak{so}(2m)$ is generated by the coefficients of the characteristic polynomial (the Pontryagin data), and passing to $SO(2m)$ adjoins exactly one new generator, the Pfaffian, subject to the single relation $\operatorname{Pf}^2=\det$. In **combinatorics** the matching form exhibits $\operatorname{Pf}(A)$ as the signed generating function of perfect matchings of the complete graph on $2m$ vertices weighted by the entries $A_{ij}$; this is the algebraic heart of the FKT algorithm, which counts perfect matchings of a planar graph in polynomial time by computing a single Pfaffian, and of the theory of "Pfaffian orientations". In **theoretical physics** the Pfaffian is the value of a Gaussian integral over anticommuting (Grassmann) variables, $\int e^{\frac12\sum_{i,j}\theta_i A_{ij}\theta_j}\,d\theta=\operatorname{Pf}(A)$, exactly as the ordinary Gaussian integral over commuting variables yields $(\det)^{-1/2}$; this is why free-fermion partition functions are Pfaffians and why the sign of a fermionic path integral — a notorious subtlety — is literally the sign of a Pfaffian.

A second compression worth carrying is the reason evenness and orientation are inseparable here. The determinant of a skew matrix is invariant under $O(2m)$ because $\det(B^tAB)=\det(B)^2\det(A)$ and $\det(B)^2=1$ for orthogonal $B$; but the Pfaffian transforms by $\operatorname{Pf}(B^tAB)=\det(B)\operatorname{Pf}(A)$ ([[Thm - Properties of the Pfaffian]], clause (a)), and $\det(B)=\pm1$ separates the two components of $O(2m)$. So the Pfaffian is not an $O(2m)$-invariant, only an $SO(2m)$-invariant that reports, through the factor $\det(B)$, which component a change of basis lies in. That is the precise sense in which the Pfaffian *sees orientation*, and it is inherited verbatim by the Euler class it defines.

---

# Examples / Corollaries

**Is an instance — $m=1$ (the rotation generator).** For $A=\left(\begin{smallmatrix}0&a\\-a&0\end{smallmatrix}\right)\in\mathfrak{so}(2)$ we computed $\operatorname{Pf}(A)=a$ above. Let us re-derive it from the matching form to see that agrees: the only perfect matching of $\{1,2\}$ is $M=\{\{1,2\}\}$ with $\pi_M=\mathrm{id}$, so $\operatorname{Pf}(A)=\operatorname{sign}(\mathrm{id})\,A_{12}=a$. Both forms give $a$, confirming the Proposition in the smallest case.

**Is an instance — block-diagonal matrices.** Let $A=\operatorname{diag}(B_1,\dots,B_m)$ be block-diagonal with $2\times 2$ blocks $B_k=\left(\begin{smallmatrix}0&a_k\\-a_k&0\end{smallmatrix}\right)$; that is, $A_{2k-1,2k}=a_k$ and all other above-diagonal entries vanish. We claim $\operatorname{Pf}(A)=\prod_{k=1}^m a_k$, verified clause by clause from the matching form. In $\operatorname{Pf}(A)=\sum_M\operatorname{sign}(\pi_M)\prod_{k}A_{p_k q_k}$, a matching $M$ contributes a nonzero product only if every one of its blocks $\{p_k,q_k\}$ is a pair with $A_{p_k q_k}\ne0$, hence (since the only nonzero above-diagonal entries are $A_{2k-1,2k}$) only if $M$ pairs $2k-1$ with $2k$ for each $k$. There is exactly one such matching, $M_0=\{\{1,2\},\{3,4\},\dots,\{2m-1,2m\}\}$, whose reference permutation is $\pi_{M_0}=\mathrm{id}$, so $\operatorname{sign}(\pi_{M_0})=1$. Its contribution is $\prod_{k=1}^m A_{2k-1,2k}=\prod_{k=1}^m a_k$. Every other matching contributes $0$. Therefore $\operatorname{Pf}(A)=\prod_{k=1}^m a_k$, as claimed. Cross-check via the exterior form: $\sigma_A=\sum_k a_k\,e_{2k-1}\wedge e_{2k}$, and since the distinct $2$-forms $e_{2k-1}\wedge e_{2k}$ pairwise commute (even degree) and each squares to zero, $\sigma_A^{\wedge m}=m!\,a_1\cdots a_m\,e_1\wedge\dots\wedge e_{2m}$ (only the fully mixed term survives, with the multinomial coefficient $m!$), giving $\tfrac1{m!}\sigma_A^{\wedge m}=a_1\cdots a_m$, in agreement.

**Is an instance — the general $4\times 4$ skew matrix ($m=2$).** Write a skew $A\in\mathfrak{so}(4)$ with above-diagonal entries $A_{12},A_{13},A_{14},A_{23},A_{24},A_{34}$. The perfect matchings of $\{1,2,3,4\}$ are three: $\{\{1,2\},\{3,4\}\}$, $\{\{1,3\},\{2,4\}\}$, $\{\{1,4\},\{2,3\}\}$, with reference permutations $(1,2,3,4)=\mathrm{id}$, $(1,3,2,4)$, $(1,4,2,3)$ and signs $+1$, $-1$, $+1$ respectively (the middle word is obtained from $\mathrm{id}$ by the single transposition $2\leftrightarrow3$, sign $-1$; the last by the $3$-cycle $2\to4\to3\to2$ sending $1234$ to $1423$, an even permutation, sign $+1$). Hence
$$\operatorname{Pf}(A)=A_{12}A_{34}-A_{13}A_{24}+A_{14}A_{23}.$$
This is the identity a reader will use constantly; its square is proved equal to $\det A$ by direct expansion in the companion drill [[Ex - Pfaffian of a 4 by 4 Skew Matrix and the Identity Pf Squared Equals det]].

**Is NOT an instance — symmetric or general square matrices.** The Pfaffian is defined *only* on skew-symmetric matrices, and the identity $\operatorname{Pf}^2=\det$ fails for any other class, so the object simply does not exist there. Take the symmetric matrix $S=\left(\begin{smallmatrix}1&0\\0&2\end{smallmatrix}\right)$ with $\det S=2$. If one blindly applied the $m=1$ formula $\tfrac12(S_{12}-S_{21})$ one would get $0$, whose square is $0\ne 2=\det S$; the "square root of the determinant" property collapses because $S$ is not skew. More fundamentally, the coefficient map $A_{12}$ used in the formula presupposes $A_{12}=-A_{21}$; for a symmetric or general matrix the defining sum has no invariance property and no relation to the determinant, and we do not call it a Pfaffian.

**Is NOT an instance — odd size.** There is no Pfaffian on $\mathfrak{so}(2m+1)$. For any skew $A$ of odd size $2m+1$, $\det A=\det(A^t)=\det(-A)=(-1)^{2m+1}\det A=-\det A$, so $\det A=0$ identically; there is no non-trivial polynomial to be a square root of. Correspondingly the defining sum has no meaning: it would require splitting the odd set $\{1,\dots,2m+1\}$ into two-element blocks, which is impossible, so no "product over $m'$ pairs covering all indices" exists. Evenness is a hypothesis, not a convenience.

**Corollary — parity under negation.** For every $A\in\mathfrak{so}(2m)$, $\operatorname{Pf}(-A)=(-1)^m\operatorname{Pf}(A)$. Indeed, replacing $A$ by $-A$ replaces each factor $A_{\sigma(2i-1)\sigma(2i)}$ by $-A_{\sigma(2i-1)\sigma(2i)}$, so each summand — a product of exactly $m$ such factors — is multiplied by $(-1)^m$; pulling the common factor out of the sum gives $\operatorname{Pf}(-A)=(-1)^m\operatorname{Pf}(A)$. (This is the homogeneity of degree $m$ evaluated at the scalar $-1$; more generally $\operatorname{Pf}(tA)=t^m\operatorname{Pf}(A)$ for $t\in\mathbb{R}$ by the same one-line computation.)

**Calibration check.** First, $\operatorname{Pf}(A)^2=\det A$ for $m=1$: with $A=\left(\begin{smallmatrix}0&a\\-a&0\end{smallmatrix}\right)$ we have $\det A=0\cdot 0-a\cdot(-a)=a^2$ and $\operatorname{Pf}(A)^2=a^2$, so the two agree. Second, $\operatorname{Pf}(A)^2=\det A$ for $m=2$ on the block-diagonal case: with $A=\operatorname{diag}(B_1,B_2)$, $B_k=\left(\begin{smallmatrix}0&a_k\\-a_k&0\end{smallmatrix}\right)$, the determinant is multiplicative over blocks, $\det A=\det B_1\det B_2=a_1^2 a_2^2$ (by [[Thm - Determinant is Multiplicative|multiplicativity of the determinant]] applied to the block factorisation, or directly by cofactor expansion), while $\operatorname{Pf}(A)^2=(a_1 a_2)^2=a_1^2 a_2^2$; the two agree. (The general $4\times4$ identity $\operatorname{Pf}^2=\det$, and the full statement over $\mathfrak{so}(2m)$, are proved on [[Thm - Properties of the Pfaffian|the Pfaffian-properties page]] and drilled in [[Ex - Pfaffian of a 4 by 4 Skew Matrix and the Identity Pf Squared Equals det|the 4×4 exercise]].) Third, sanity-check the parity corollary against the block example: $\operatorname{Pf}(-A)=\prod_k(-a_k)=(-1)^m\prod_k a_k=(-1)^m\operatorname{Pf}(A)$, consistent with the corollary.

---

# Unlocked by This

> [!tip] Euler Class *(from Gauge Theory VI)*
> The Pfaffian is the invariant polynomial that produces the [[Def - Euler Class of an Oriented Vector Bundle|Euler class]] of an oriented rank-$2m$ real vector bundle by the Chern–Weil recipe: $e(E)=\big[\operatorname{Pf}(F/2\pi)\big]\in H^{2m}_{dR}(M)$, where $F$ is the skew-symmetric curvature matrix of a metric connection in an oriented orthonormal frame. Its orientation-odd transformation law is exactly what makes $e(E)$ change sign under orientation reversal.

> [!tip] Properties of the Pfaffian *(from Gauge Theory VI)*
> The three structural facts quoted above — $\operatorname{Pf}(B^tAB)=\det(B)\operatorname{Pf}(A)$, $\operatorname{Pf}(A)^2=\det A$, and $SO(2m)$-invariance with an orientation sign under $O(2m)$ — are established on [[Thm - Properties of the Pfaffian]]; they promote $\operatorname{Pf}$ to an element of the ring $I(SO(2m))$ of [[Def - Ad-Invariant Polynomial|invariant polynomials]] and license every Chern–Weil use of it.

> [!tip] Pontryagin Classes and the Relation $e^2=p_m$ *(from Gauge Theory VI)*
> Because $\operatorname{Pf}^2=\det$, squaring the Euler class of an oriented rank-$2m$ bundle recovers the top [[Def - Pontryagin Classes|Pontryagin class]], $e(E)^2=p_m(E)$; this identity, one of the constraints among the characteristic classes of a manifold, is proved on the Pontryagin page from the Pfaffian identity established here.

> [!tip] Fermionic Gaussian Integrals *(from mathematical physics)*
> The identity $\int e^{\frac12\theta^t A\,\theta}\,d\theta=\operatorname{Pf}(A)$ over Grassmann variables makes the Pfaffian the free-fermion partition function; the sign of a fermionic path integral is the sign of a Pfaffian, the mechanism behind the fermion-sign problem in quantum Monte Carlo. This is developed in the physics chapters, not here, and is listed only as a forward pointer.

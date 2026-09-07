---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Lie Algebras and Dimensions of the Classical Matrix Groups"
  - "Def - Lie Subalgebra and Abelian Lie Algebra"
tags: [geometry, gauge-theory, lie-algebras]
---

# Problem Statement

Equip $\mathbb{R}^3$ with the **cross product** $[\,v,w\,]:=v\times w$ as its bracket. Bär–Wernli's Example 1.2.2.3 (source item **B-E1.2.3**, p. 10) asserts that $(\mathbb{R}^3,\times)$ is a Lie algebra; the task of this exercise is to prove that assertion, and to identify *which* Lie algebra it is, by exhibiting an explicit isomorphism onto $\mathfrak{so}(3)$.

Concretely, define the **hat map**
$$\Phi:\mathbb{R}^3\longrightarrow\operatorname{Mat}(3\times 3;\mathbb{R}),\qquad
\Phi(v)=\widehat{v}:=\begin{pmatrix}0&-v_3&v_2\\ v_3&0&-v_1\\ -v_2&v_1&0\end{pmatrix}
\quad(v=(v_1,v_2,v_3)\in\mathbb{R}^3),$$
which is exactly the assignment $v\mapsto(w\mapsto v\times w)$: $\widehat{v}$ is the matrix of the linear map "cross with $v$ on the left". Prove that $\Phi$ is a **Lie-algebra isomorphism** from $(\mathbb{R}^3,\times)$ onto $\big(\mathfrak{so}(3),[\cdot,\cdot]\big)$, where $\mathfrak{so}(3)$ is the Lie algebra of the rotation group $\operatorname{SO}(3)$ with the matrix commutator. Explicitly:

1. $\Phi$ is a linear isomorphism of $\mathbb{R}^3$ onto the space of antisymmetric $3\times 3$ real matrices;
2. that space of antisymmetric matrices is exactly $\mathfrak{so}(3)$;
3. $\Phi$ intertwines the two brackets: $\widehat{v\times w}=[\widehat{v},\widehat{w}]=\widehat{v}\widehat{w}-\widehat{w}\widehat{v}$ for all $v,w\in\mathbb{R}^3$.

Since $\mathfrak{so}(3)$ is already known to be a Lie algebra (a subalgebra of $\mathfrak{gl}(3;\mathbb{R})$), transporting its structure across the isomorphism $\Phi$ proves that $(\mathbb{R}^3,\times)$ is a Lie algebra — in particular that the cross product satisfies the Jacobi identity — with no separate triple-product grind required.

**Recall:**

The relevant classical Lie algebra and its identification with antisymmetric matrices are established on the section's theorem page.

![[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups#Statement]]

The clause we use is the one for the special orthogonal group: the Lie algebra of $\operatorname{SO}(3)$ is
$$\mathfrak{so}(3)=\{A\in\operatorname{Mat}(3\times 3;\mathbb{R}):A^{t}+A=0\}=\{A:A^{t}=-A\},$$
the space of antisymmetric (skew-symmetric) real $3\times 3$ matrices, of dimension $\tfrac{3\cdot 2}{2}=3$, taken with the commutator bracket $[A,B]=AB-BA$ inherited from $\mathfrak{gl}(3;\mathbb{R})$. That the commutator does make $\mathfrak{so}(3)$ a Lie algebra — antisymmetric matrices are closed under the commutator, and the three axioms hold — is part of that theorem; the underlying Jacobi identity for the commutator is **[[Ex - The Jacobi Identity for the Matrix Commutator Follows from Associativity|the matrix-commutator Jacobi identity]]**.

![[Def - Lie Subalgebra and Abelian Lie Algebra#The Definition]]

We also need the notion of a Lie-algebra morphism, not restated by the source: a **Lie-algebra homomorphism** between Lie algebras $(\mathfrak{g},[\cdot,\cdot]_{\mathfrak{g}})$ and $(\mathfrak{h},[\cdot,\cdot]_{\mathfrak{h}})$ is a $\mathbb{K}$-linear map $\Phi:\mathfrak{g}\to\mathfrak{h}$ with $\Phi([X,Y]_{\mathfrak{g}})=[\Phi(X),\Phi(Y)]_{\mathfrak{h}}$ for all $X,Y\in\mathfrak{g}$; it is an **isomorphism** if it is in addition bijective, and then $\Phi^{-1}$ is automatically a homomorphism (apply $\Phi^{-1}$ to the intertwining identity). A bijective linear map that intertwines the brackets is exactly a transport of Lie-algebra structure: whatever axioms one side satisfies, the other inherits.

The **cross product** on $\mathbb{R}^3$ is $v\times w=(v_2 w_3-v_3 w_2,\ v_3 w_1-v_1 w_3,\ v_1 w_2-v_2 w_1)$; it is bilinear and antisymmetric ($w\times v=-v\times w$) directly from this formula.

---

# Convergent Strategy

**Problem class.** This is a *build-and-verify-an-isomorphism* problem: the structure to be identified ($(\mathbb{R}^3,\times)$ as an abstract Lie algebra) is compared with a known one ($\mathfrak{so}(3)$) by producing an explicit linear bijection and checking it respects the brackets. The pattern is "transport of structure": rather than verify the Jacobi identity for the cross product by a bare computation, we route it through an already-established Lie algebra. The only real content is the bracket-intertwining identity $\widehat{v\times w}=[\widehat v,\widehat w]$.

**Assumption pattern.** Two facts are borrowed. First, from **[[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]]**, that $\mathfrak{so}(3)$ *equals* the space of antisymmetric $3\times 3$ matrices and is a $3$-dimensional Lie algebra under the commutator. Second, that the commutator satisfies the Jacobi identity, from **[[Ex - The Jacobi Identity for the Matrix Commutator Follows from Associativity]]**. The recognisable trigger for transport of structure is precisely this: one algebra whose axioms are cheap to state but whose Jacobi identity is a nuisance (the cross product), and a second, isomorphic algebra where the same axioms are already paid for (a matrix commutator).

**Theorem routing.** The route has four moves. (1) *Injectivity and image.* Read off from the formula for $\widehat v$ that $\Phi$ is linear, that $\Phi(v)$ is antisymmetric, that $\Phi$ is injective (its kernel is $\{0\}$ because the six off-diagonal entries recover $v_1,v_2,v_3$), and that its image is *all* antisymmetric matrices (three free off-diagonal parameters, three-dimensional target, so the injective $\Phi$ is onto by dimension). (2) *Identify the codomain* as $\mathfrak{so}(3)$ using the recalled theorem. (3) *Intertwine the brackets* by verifying $[\widehat u,\widehat v]=\widehat{u\times v}$; by bilinearity and antisymmetry of both sides this reduces to the single basis identity $[\widehat{e_1},\widehat{e_2}]=\widehat{e_3}$ together with its two cyclic partners. (4) *Transport structure*: a bracket-preserving linear bijection carries the Lie-algebra axioms of $\mathfrak{so}(3)$ back to $(\mathbb{R}^3,\times)$, so the latter is a Lie algebra isomorphic to the former.

**Key decision point.** The decisive economy is refusing to prove the Jacobi identity for the cross product directly. A direct proof would expand $u\times(v\times w)+v\times(w\times u)+w\times(u\times v)$ using the "$\mathrm{BAC}\!-\!\mathrm{CAB}$" triple-product expansion and watch the terms cancel — perfectly possible, but it duplicates work already done for the commutator. The better decision is to make the isomorphism carry the identity for us, so that the *only* new computation is the bracket-intertwining on three basis pairs. The second decision is to reduce that intertwining to basis vectors: because both $(u,v)\mapsto[\widehat u,\widehat v]$ and $(u,v)\mapsto\widehat{u\times v}$ are bilinear and antisymmetric, agreement on the ordered basis pairs $(e_1,e_2),(e_2,e_3),(e_3,e_1)$ forces agreement everywhere, turning a two-variable identity into three $3\times 3$ matrix multiplications.

---

# Legal Operations Used

Named descriptively; the section's topic page will fix the numbering.

1. **Present a linear map by its matrix in the standard basis.** The hat map is specified by the explicit antisymmetric matrix $\widehat v$; its linearity in $v$ is read off entrywise.

2. **Prove injectivity by exhibiting a left inverse / reading off the kernel.** The entries of $\widehat v$ return $v_1,v_2,v_3$, so $\widehat v=0\Rightarrow v=0$; the vee map $\widehat v\mapsto v$ is an explicit inverse.

3. **Deduce surjectivity from injectivity and equal finite dimension.** An injective linear map between vector spaces of the same finite dimension is bijective; here both $\mathbb{R}^3$ and the antisymmetric $3\times 3$ matrices are $3$-dimensional.

4. **Identify a computed tangent algebra with a named classical Lie algebra.** Invoke the theorem that $\mathfrak{so}(3)$ is the antisymmetric matrices to name the codomain of $\Phi$.

5. **Reduce a bilinear identity to basis inputs.** Both sides of $\widehat{u\times v}=[\widehat u,\widehat v]$ are bilinear and antisymmetric, so verification on the ordered basis pairs suffices.

6. **Transport a Lie-algebra structure across an intertwining bijection.** Use that a bracket-preserving linear isomorphism carries all three axioms from a known Lie algebra to the algebra under study, obtaining the Jacobi identity for the cross product without recomputation.

---

# Hints

> [!note]- Hint 1
> Write down the matrix $\widehat v$ of the map $w\mapsto v\times w$ and check the claim $\widehat v\,w=v\times w$ on the standard basis vectors $w=e_1,e_2,e_3$. Is $\widehat v$ antisymmetric? Is the assignment $v\mapsto\widehat v$ linear in $v$?

> [!note]- Hint 2
> To see $\Phi$ is a bijection onto the antisymmetric matrices, note that a general antisymmetric $3\times 3$ matrix has exactly three independent entries (those above the diagonal), and reading them off recovers $v_1,v_2,v_3$. So $\Phi$ is injective with image the full $3$-dimensional space of antisymmetric matrices — which the recalled theorem names $\mathfrak{so}(3)$.

> [!note]- Hint 3
> The heart of the problem is $\widehat{v\times w}=[\widehat v,\widehat w]$. Do not expand in general first. Both sides are bilinear and antisymmetric in $(v,w)$, so it is enough to check the three ordered basis pairs $(e_1,e_2),(e_2,e_3),(e_3,e_1)$. For the first, compute $\widehat{e_1}\widehat{e_2}-\widehat{e_2}\widehat{e_1}$ and compare with $\widehat{e_1\times e_2}=\widehat{e_3}$.

> [!note]- Hint 4
> Once $\Phi$ is a linear bijection with $\Phi(v\times w)=[\Phi v,\Phi w]$, you are done *without* checking the Jacobi identity for the cross product by hand: transport of structure. Because $\mathfrak{so}(3)$ is a Lie algebra and $\Phi^{-1}$ is also a homomorphism, the cross product inherits bilinearity, antisymmetry, and Jacobi from the commutator. Spell out why $\Phi^{-1}$ preserves brackets.

---

# Solution

The plan is to build the hat map explicitly, verify it is a linear bijection onto the antisymmetric matrices, identify those matrices as $\mathfrak{so}(3)$ via the recalled theorem, and then prove the single bracket-intertwining identity on three basis pairs. With the intertwining in hand, the isomorphism transports the Lie-algebra axioms of $\mathfrak{so}(3)$ back to $\mathbb{R}^3$, proving the cross product is a Lie bracket and naming its algebra.

**Step 1: The hat map is linear, lands in the antisymmetric matrices, and satisfies $\widehat v\,w=v\times w$.**

For $v=(v_1,v_2,v_3)$ the matrix $\widehat v$ is antisymmetric, and applying it to $w$ reproduces the cross product.

> [!note]- Derivation
> We must show three things: $\Phi$ is linear, $\widehat v^{\,t}=-\widehat v$, and $\widehat v\,w=v\times w$.
>
> **Linearity.** Each entry of $\widehat v$ is one of $0,\pm v_1,\pm v_2,\pm v_3$, hence a linear function of $v$; therefore $\widehat{v+v'}=\widehat v+\widehat{v'}$ and $\widehat{\lambda v}=\lambda\widehat v$ for $\lambda\in\mathbb{R}$ (add or scale entrywise). So $\Phi$ is linear.
>
> **Antisymmetry.** Transposing $\widehat v=\begin{pmatrix}0&-v_3&v_2\\ v_3&0&-v_1\\ -v_2&v_1&0\end{pmatrix}$ negates every off-diagonal entry, giving $\widehat v^{\,t}=-\widehat v$ (the diagonal is zero). So $\widehat v$ is antisymmetric.
>
> **Reproduces the cross product.** Multiplying,
> $$\widehat v\,w=\begin{pmatrix}0&-v_3&v_2\\ v_3&0&-v_1\\ -v_2&v_1&0\end{pmatrix}\!\begin{pmatrix}w_1\\ w_2\\ w_3\end{pmatrix}=\begin{pmatrix}-v_3 w_2+v_2 w_3\\ v_3 w_1-v_1 w_3\\ -v_2 w_1+v_1 w_2\end{pmatrix}=\begin{pmatrix}v_2 w_3-v_3 w_2\\ v_3 w_1-v_1 w_3\\ v_1 w_2-v_2 w_1\end{pmatrix}=v\times w\qquad\text{(definition of }\times\text{).}$$
> Thus $\Phi(v)$ is precisely the linear map $w\mapsto v\times w$, as required.

**Step 2: The hat map is a bijection onto the space of antisymmetric matrices.**

$\Phi$ is injective, and its image is the entire $3$-dimensional space of antisymmetric $3\times 3$ real matrices.

> [!note]- Derivation
> **Injectivity.** If $\widehat v=0$ then every off-diagonal entry vanishes; reading the entries in positions $(3,2),(1,3),(2,1)$ gives $v_1=v_2=v_3=0$, so $v=0$. Hence $\ker\Phi=\{0\}$ and $\Phi$ is injective. Equivalently, the **vee map** $\vee:\widehat v\mapsto v=(A_{32},A_{13},A_{21})$ is a linear left inverse of $\Phi$.
>
> **Image and surjectivity.** A general antisymmetric $3\times 3$ real matrix has zero diagonal and its below-diagonal entries determined by the above-diagonal ones, so it is
> $$A=\begin{pmatrix}0&-c&b\\ c&0&-a\\ -b&a&0\end{pmatrix}=\Phi\big((a,b,c)\big),$$
> with $(a,b,c)=(A_{32},A_{13},A_{21})$. Thus every antisymmetric matrix is in the image, so $\Phi$ maps *onto* the space of antisymmetric matrices. (Consistently: the antisymmetric matrices form a vector space of dimension $\binom{3}{2}=3$, equal to $\dim\mathbb{R}^3$, so the injective linear map $\Phi$ between equidimensional spaces is automatically bijective onto it.)

**Step 3: The codomain is $\mathfrak{so}(3)$.**

The space of antisymmetric $3\times 3$ real matrices is exactly the Lie algebra $\mathfrak{so}(3)$.

> [!note]- Derivation
> By **[[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups|the classification of the classical matrix Lie algebras]]** — which states $\mathfrak{so}(3)=\{A\in\operatorname{Mat}(3\times 3;\mathbb{R}):A^{t}+A=0\}$, of dimension $3$ — the codomain identified in Step 2 is $\mathfrak{so}(3)$. That theorem also records that $\mathfrak{so}(3)$ is closed under the commutator and is a Lie algebra under it. So far, then, $\Phi:\mathbb{R}^3\to\mathfrak{so}(3)$ is a linear isomorphism of vector spaces; it remains to check it respects brackets.

**Step 4: The brackets are intertwined: $\widehat{v\times w}=[\widehat v,\widehat w]$.**

For all $v,w\in\mathbb{R}^3$, the commutator of the hatted matrices equals the hat of the cross product. By bilinearity and antisymmetry of both sides, it suffices to verify this on the ordered basis pairs.

> [!note]- Derivation
> **Reduction to basis pairs.** The map $(v,w)\mapsto[\widehat v,\widehat w]$ is bilinear (the commutator is bilinear and $\Phi$ is linear) and antisymmetric ($[\widehat w,\widehat v]=-[\widehat v,\widehat w]$); the map $(v,w)\mapsto\widehat{v\times w}$ is bilinear and antisymmetric for the same reasons ($\times$ is bilinear and antisymmetric, $\Phi$ linear). Two bilinear antisymmetric maps that agree on all ordered pairs $(e_i,e_j)$ with $i<j$ agree everywhere: expand $v=\sum_i v_i e_i$, $w=\sum_j w_j e_j$, use bilinearity to reduce to the pairs $(e_i,e_j)$, note the diagonal pairs $i=j$ give zero on both sides (antisymmetry), and the pairs $i>j$ are fixed by the pairs $i<j$ (antisymmetry). So it is enough to check $(e_1,e_2),(e_2,e_3),(e_3,e_1)$.
>
> **The basis matrices.** From the formula,
> $$\widehat{e_1}=\begin{pmatrix}0&0&0\\ 0&0&-1\\ 0&1&0\end{pmatrix},\quad
> \widehat{e_2}=\begin{pmatrix}0&0&1\\ 0&0&0\\ -1&0&0\end{pmatrix},\quad
> \widehat{e_3}=\begin{pmatrix}0&-1&0\\ 1&0&0\\ 0&0&0\end{pmatrix}.$$
>
> **The pair $(e_1,e_2)$.** Multiplying entrywise, $\widehat{e_1}\widehat{e_2}=\begin{pmatrix}0&0&0\\ 1&0&0\\ 0&0&0\end{pmatrix}$ and $\widehat{e_2}\widehat{e_1}=\begin{pmatrix}0&1&0\\ 0&0&0\\ 0&0&0\end{pmatrix}$, so
> $$[\widehat{e_1},\widehat{e_2}]=\widehat{e_1}\widehat{e_2}-\widehat{e_2}\widehat{e_1}=\begin{pmatrix}0&-1&0\\ 1&0&0\\ 0&0&0\end{pmatrix}=\widehat{e_3}\qquad\text{(direct matrix multiplication).}$$
> On the other side $e_1\times e_2=e_3$, so $\widehat{e_1\times e_2}=\widehat{e_3}$. The two agree.
>
> **The pairs $(e_2,e_3)$ and $(e_3,e_1)$.** By the identical computation with the letters cyclically advanced $1\to 2\to 3\to 1$ (every entry of every matrix is permuted the same way, and matrix multiplication is unaffected by relabelling the basis), $[\widehat{e_2},\widehat{e_3}]=\widehat{e_1}=\widehat{e_2\times e_3}$ and $[\widehat{e_3},\widehat{e_1}]=\widehat{e_2}=\widehat{e_3\times e_1}$. To be explicit for the second: $\widehat{e_2}\widehat{e_3}=\begin{pmatrix}0&0&0\\ 0&0&0\\ 0&-1&0\end{pmatrix}$, $\widehat{e_3}\widehat{e_2}=\begin{pmatrix}0&0&-1\\ 0&0&0\\ 0&0&0\end{pmatrix}$, giving $[\widehat{e_2},\widehat{e_3}]=\begin{pmatrix}0&0&0\\ 0&0&-1\\ 0&1&0\end{pmatrix}=\widehat{e_1}$; and $\widehat{e_3}\widehat{e_1}=\begin{pmatrix}0&0&1\\ 0&0&0\\ 0&0&0\end{pmatrix}$, $\widehat{e_1}\widehat{e_3}=\begin{pmatrix}0&0&0\\ 0&0&0\\ 1&0&0\end{pmatrix}$, giving $[\widehat{e_3},\widehat{e_1}]=\begin{pmatrix}0&0&1\\ 0&0&0\\ -1&0&0\end{pmatrix}=\widehat{e_2}$. All three ordered basis pairs check out.
>
> By the reduction above, $[\widehat v,\widehat w]=\widehat{v\times w}$ for all $v,w\in\mathbb{R}^3$. Hence $\Phi$ is a Lie-algebra homomorphism, and being bijective (Steps 2–3), a **Lie-algebra isomorphism** $\Phi:(\mathbb{R}^3,\times)\xrightarrow{\ \cong\ }(\mathfrak{so}(3),[\cdot,\cdot])$.

**Step 5: Transport of structure — the cross product is a Lie bracket.**

Because $\Phi$ is a bracket-preserving linear bijection onto the Lie algebra $\mathfrak{so}(3)$, its inverse is also bracket-preserving, and the cross product inherits all three Lie-algebra axioms. Thus $(\mathbb{R}^3,\times)$ is a Lie algebra, isomorphic to $\mathfrak{so}(3)$.

> [!note]- Derivation
> **$\Phi^{-1}$ preserves brackets.** For $A,B\in\mathfrak{so}(3)$ set $v=\Phi^{-1}(A)$, $w=\Phi^{-1}(B)$. Applying Step 4, $\Phi(v\times w)=[\Phi v,\Phi w]=[A,B]$, so $\Phi^{-1}([A,B])=v\times w=\Phi^{-1}(A)\times\Phi^{-1}(B)$. Hence $\Phi^{-1}$ intertwines the commutator with the cross product.
>
> **Inheritance of the axioms.** The cross product is already visibly bilinear and antisymmetric (Step 1's recall). For the **Jacobi identity**, let $u,v,w\in\mathbb{R}^3$ and put $A=\widehat u$, $B=\widehat v$, $C=\widehat w$. Using $\widehat{x\times y}=[\widehat x,\widehat y]$ twice,
> $$\widehat{u\times(v\times w)}=[\widehat u,\widehat{v\times w}]=[A,[B,C]]\qquad\text{(Step 4, applied inner then outer),}$$
> and cyclically for the other two terms, so
> $$\widehat{\,u\times(v\times w)+v\times(w\times u)+w\times(u\times v)\,}=[A,[B,C]]+[B,[C,A]]+[C,[A,B]].$$
> The right-hand side is the Jacobi expression for the commutator, which vanishes by **[[Ex - The Jacobi Identity for the Matrix Commutator Follows from Associativity|the matrix-commutator Jacobi identity]]** (it equals $-\big([[A,B],C]+[[B,C],A]+[[C,A],B]\big)=0$ after using antisymmetry of the commutator to rewrite $[A,[B,C]]=-[[B,C],A]$). Since $\Phi$ is injective, the hatted left-hand side vanishes only if
> $$u\times(v\times w)+v\times(w\times u)+w\times(u\times v)=0,$$
> the Jacobi identity for the cross product. Therefore $(\mathbb{R}^3,\times)$ satisfies all three axioms and is a Lie algebra, and $\Phi$ exhibits it as isomorphic to $\mathfrak{so}(3)$. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** The hat map $\Phi:\mathbb{R}^3\to\operatorname{Mat}(3\times 3;\mathbb{R})$, $\Phi(v)=\widehat v$ with $\widehat v\,w=v\times w$, is a Lie-algebra isomorphism $(\mathbb{R}^3,\times)\cong(\mathfrak{so}(3),[\cdot,\cdot])$; in particular $(\mathbb{R}^3,\times)$ is a Lie algebra.
>
> *Linearity and image.* Every entry of $\widehat v=\begin{pmatrix}0&-v_3&v_2\\ v_3&0&-v_1\\ -v_2&v_1&0\end{pmatrix}$ is linear in $v$, so $\Phi$ is linear; $\widehat v^{\,t}=-\widehat v$, so $\Phi(v)$ is antisymmetric; and $\widehat v\,w=v\times w$ by direct multiplication. Reading the entries $(A_{32},A_{13},A_{21})$ off an antisymmetric $A$ inverts $\Phi$, so $\Phi$ is a linear bijection onto the $3$-dimensional space of antisymmetric $3\times 3$ real matrices. By [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]], that space is $\mathfrak{so}(3)$.
>
> *Bracket intertwining.* Both $(v,w)\mapsto[\widehat v,\widehat w]$ and $(v,w)\mapsto\widehat{v\times w}$ are bilinear and antisymmetric, so it suffices to check the ordered basis pairs. Direct matrix multiplication gives $[\widehat{e_1},\widehat{e_2}]=\widehat{e_3}$, $[\widehat{e_2},\widehat{e_3}]=\widehat{e_1}$, $[\widehat{e_3},\widehat{e_1}]=\widehat{e_2}$, matching $\widehat{e_i\times e_j}$ in each case. Hence $[\widehat v,\widehat w]=\widehat{v\times w}$ for all $v,w$, so $\Phi$ is a Lie-algebra homomorphism, and being bijective, an isomorphism.
>
> *Consequence.* A bracket-preserving linear bijection transports Lie-algebra structure, so $\Phi^{-1}$ is also a homomorphism and $(\mathbb{R}^3,\times)$ inherits bilinearity, antisymmetry, and — from [[Ex - The Jacobi Identity for the Matrix Commutator Follows from Associativity|the commutator's Jacobi identity]] via $\widehat{u\times(v\times w)}=[\widehat u,[\widehat v,\widehat w]]$ and injectivity of $\Phi$ — the Jacobi identity. Thus $(\mathbb{R}^3,\times)\cong\mathfrak{so}(3)$ as Lie algebras. $\blacksquare$

> [!warning]- Illegal but tempting: reading the isomorphism off dimension alone
> It is tempting to argue "$(\mathbb{R}^3,\times)$ and $\mathfrak{so}(3)$ are both $3$-dimensional, hence isomorphic as Lie algebras." This is false as a general principle: Lie algebras of equal dimension are almost never isomorphic (the abelian $\mathbb{R}^3$ and $\mathfrak{so}(3)$ are both $3$-dimensional but not isomorphic — one has zero bracket, the other does not). Equal dimension gives only a *linear* isomorphism; a Lie-algebra isomorphism additionally requires the bracket-intertwining of Step 4, which is where the real content lives. The extra condition that *would* make a dimension count conclusive is a classification theorem for the isomorphism type in that dimension — and even the three-dimensional real Lie algebras form several distinct types (abelian, Heisenberg, $\mathfrak{so}(3)$, $\mathfrak{sl}(2;\mathbb{R})$, and the solvable families), so nothing short of matching structure constants settles it.

---

# Key Takeaways

**Transport of structure lets a hard axiom be inherited rather than reproved.** The Jacobi identity for the cross product is genuinely awkward to verify head-on, because the cross product is not the commutator of any *associative* product on $\mathbb{R}^3$ — there is no associativity to inherit Jacobi from, as there was in the matrix case. The move that dissolves the difficulty is to find a linear bijection onto a Lie algebra where the identity is already secured and to check only that the bijection respects brackets. Then every axiom of the target — bilinearity, antisymmetry, and Jacobi — is pulled back for free. The trigger for this technique is exactly the present situation: a candidate bracket whose axioms are cheap to state but expensive to verify, sitting next to a familiar Lie algebra of the same dimension. The diagnostic question to ask is "is my bracket secretly the commutator (or the cross product, or the vector-field bracket) of something I already understand, viewed through a change of variables?" If yes, verify the change of variables intertwines the brackets and stop.

**The hat map $\mathfrak{so}(3)\cong(\mathbb{R}^3,\times)$ is the dictionary that turns three-dimensional vector calculus into Lie theory, and it is the anchor of the whole $\operatorname{SU}(2)$–$\operatorname{SO}(3)$ story.** Under $v\mapsto\widehat v$, "cross with $v$" becomes an infinitesimal rotation about the axis $v$, angular velocity vectors become skew-symmetric matrices, the identity $\widehat v\,w=v\times w$ is the statement that the generator of rotation about $v$ acts on $w$ by the cross product, and $\exp(\theta\,\widehat n)$ is the rotation by angle $\theta$ about the unit axis $n$ (Rodrigues' formula). This is why every "right-hand rule" computation in rigid-body mechanics and electromagnetism is a disguised $\mathfrak{so}(3)$ bracket computation. The same three-dimensional Lie algebra reappears as $\mathfrak{su}(2)$ — the traceless anti-Hermitian $2\times 2$ matrices, with the anti-Hermitian Pauli basis satisfying the same structure constants up to normalisation — and the resulting isomorphism $\mathfrak{so}(3)\cong\mathfrak{su}(2)$ at the Lie-algebra level, contrasted with the *non*-isomorphism $\operatorname{SO}(3)\not\cong\operatorname{SU}(2)$ at the group level (the latter is the simply connected double cover), is one of the load-bearing facts of gauge theory. The matrix-level identification worked out here is spelled out from the group side on **[[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices|the differential-geometry computation of the Lie algebra of SO(3)]]**, whose hat-map conventions this page matches exactly.

**Checking a bilinear identity on a basis is the routine that makes structure-constant computations finite.** The reduction in Step 4 — that two bilinear antisymmetric maps agreeing on the ordered pairs $(e_i,e_j)$, $i<j$, agree everywhere — is the standard device for verifying any bracket identity: the bracket of a Lie algebra is determined by its **structure constants** $[e_i,e_j]=\sum_k c^k_{ij}e_k$, and here the computation showed $c^k_{ij}=\varepsilon_{ijk}$, the Levi-Civita symbol, for $(\mathbb{R}^3,\times)$. Whenever a claimed map between Lie algebras must be checked to preserve brackets, do not expand in general vectors; compute both sides on basis pairs, compare structure constants, and invoke bilinearity. The transferable diagnostic is that a Lie-algebra homomorphism is precisely a linear map whose matrix carries one set of structure constants to the other, so verifying the homomorphism property is always a finite check on a basis — three matrix products here, and in general $\binom{\dim}{2}$ of them.

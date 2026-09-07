---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Lie Algebras and Dimensions of the Classical Matrix Groups"
  - "Def - The Lie Algebra of a Lie Group"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\sigma_1,\sigma_2,\sigma_3$ be the standard **Pauli matrices**
$$\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},$$
and set $X_a:=-i\sigma_a$ for $a\in\{1,2,3\}$, so that explicitly
$$X_1=-i\sigma_1=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad X_2=-i\sigma_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad X_3=-i\sigma_3=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.$$
Prove the following three assertions.

1. Each $X_a$ lies in the Lie algebra $\mathfrak{su}(2)$; that is, each $X_a$ is anti-Hermitian and traceless.
2. The triple $(X_1,X_2,X_3)$ is a real basis of $\mathfrak{su}(2)$.
3. The three generators satisfy the bracket relations
$$[X_a,X_b]=2\,\epsilon_{abc}\,X_c,\qquad\text{equivalently}\qquad [-i\sigma_a,-i\sigma_b]=2\,\epsilon_{abc}\,(-i\sigma_c),$$
where $[A,B]:=AB-BA$ is the matrix commutator, $\epsilon_{abc}$ is the totally antisymmetric Levi-Civita symbol normalised by $\epsilon_{123}=1$, and a repeated index $c$ is summed over $\{1,2,3\}$.

**Recall:**

The ambient object is the Lie algebra of the special unitary group $SU(2)$, computed on the prerequisite theorem page as a space of matrices with the commutator bracket.

![[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups#Statement]]

The one line of that statement we use is the identification of $\mathfrak{su}(2)$: with the Lie algebra $\mathfrak g=T_1G$ of a matrix group $G$ realised as a subspace of $\operatorname{Mat}(2\times 2;\mathbb C)$ carrying the commutator bracket (this is [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator|the fact that the bracket of left-invariant fields on a matrix group is the matrix commutator]], and $\mathfrak g\cong T_1G$ is [[Def - The Lie Algebra of a Lie Group|the tangent-space model of the Lie algebra]]),
$$\mathfrak{su}(2)=\{A\in\operatorname{Mat}(2\times 2;\mathbb C):A^{*}=-A,\ \operatorname{tr}A=0\},\qquad \dim_{\mathbb R}\mathfrak{su}(2)=2^2-1=3,$$
where $A^{*}=\overline{A}^{\,t}$ is the conjugate transpose. A matrix with $A^{*}=-A$ is called **anti-Hermitian** (or skew-Hermitian).

A **basis** of the real vector space $\mathfrak{su}(2)$ is a linearly independent triple whose real span is all of $\mathfrak{su}(2)$; since $\dim_{\mathbb R}\mathfrak{su}(2)=3$, any three linearly independent elements of $\mathfrak{su}(2)$ already form a basis.

> [!warning] Convention: Bär's labelling of the Pauli matrices
> This exercise uses the *standard* Pauli matrices displayed above. Bär's lecture notes (*Gauge Theory*, Example 1.3.8) print the basis of $\mathfrak{su}(2)$ as "$-i$ times the Pauli matrices" but with the explicit matrices
> $$-i\sigma_1^{\mathrm B}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad -i\sigma_2^{\mathrm B}=\begin{pmatrix}0&i\\i&0\end{pmatrix},\qquad -i\sigma_3^{\mathrm B}=\begin{pmatrix}i&0\\0&-i\end{pmatrix}.$$
> Comparing entry by entry with the standard generators $X_a=-i\sigma_a$ above, one reads off
> $$-i\sigma_1^{\mathrm B}=-X_2,\qquad -i\sigma_2^{\mathrm B}=-X_1,\qquad -i\sigma_3^{\mathrm B}=-X_3,$$
> so Bär's printed $\sigma_1$ and $\sigma_2$ are interchanged relative to the standard ones (and each generator additionally carries an overall sign). None of this affects the result: a sign change or a relabelling of a basis is again a basis, so Bär's three matrices are again a basis of $\mathfrak{su}(2)$; and, as a direct check shows, the substitution $X_a\mapsto -i\sigma_a^{\mathrm B}$ preserves the structure constants $2\epsilon_{abc}$ exactly (it is a Lie-algebra automorphism of $\mathfrak{su}(2)$, namely a rotation of the generators). The convention-independent content of the exercise — a basis of anti-Hermitian traceless matrices closing under the commutator with structure constants $2\epsilon_{abc}$ — is the same either way. We use the standard matrices throughout and flag the discrepancy only so that a reader holding Bär open beside these notes is not misled by the printed forms.

---

# Convergent Strategy

**Problem class.** This is a *concrete-basis-and-structure-constants* problem for a matrix Lie algebra: we are handed three explicit $2\times 2$ complex matrices and asked to certify that they sit inside a prescribed Lie algebra, that they exhaust its degrees of freedom, and that their commutators reproduce a named table of structure constants. Such problems recur throughout gauge theory, because a computation on a principal $SU(2)$-bundle — a curvature, a Chern–Simons integrand, a Yang–Mills field strength — is ultimately a computation in $\mathfrak{su}(2)$ done in a fixed basis, and the structure constants $2\epsilon_{abc}$ are exactly the numbers that appear when the bracket $[A\wedge A]$ of Lie-algebra-valued forms is expanded.

**Assumption pattern.** The only external input is the identification of $\mathfrak{su}(2)$ as the anti-Hermitian traceless $2\times2$ complex matrices, together with its dimension $3$, both taken from the prerequisite theorem. Everything else is a finite computation with $2\times2$ matrices: three membership checks, one determinant-free independence check, and three commutator products. There is no analysis and no limiting argument; the hypotheses do their work by turning "is a basis of $\mathfrak{su}(2)$" into the two finite conditions "lies in $\mathfrak{su}(2)$" and "linearly independent", once the dimension is known to be $3$.

**Theorem routing.** The route is: (i) verify $A^{*}=-A$ and $\operatorname{tr}A=0$ for each $X_a$, placing the three matrices inside $\mathfrak{su}(2)$ via the identification recalled from [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]]; (ii) prove linear independence directly, and combine it with $\dim_{\mathbb R}\mathfrak{su}(2)=3$ from the same theorem to conclude "basis" without ever solving a spanning system; (iii) compute the three independent commutators $[X_1,X_2]$, $[X_2,X_3]$, $[X_3,X_1]$ as matrix products and read the results back as $2X_3$, $2X_1$, $2X_2$, then extend to the full antisymmetric table $[X_a,X_b]=2\epsilon_{abc}X_c$ using antisymmetry of the commutator and the vanishing of $[X_a,X_a]$.

**Key decision point.** The one decision that keeps the argument short is to prove *linear independence* and invoke the *dimension*, rather than to solve the spanning problem $a X_1+bX_2+cX_3=\begin{pmatrix}it&z\\-\bar z&-it\end{pmatrix}$ for arbitrary $t\in\mathbb R,\ z\in\mathbb C$. Both routes are correct, but the dimension count converts a system of equations in three unknowns with a general right-hand side into a single observation that a homogeneous combination can only vanish trivially. Recognising that "three independent vectors in a three-dimensional space are automatically a basis" is what makes the second assertion a two-line check instead of a small linear-algebra exercise.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (named descriptively; the topic-page Legal Operations list will assign them numbers).

1. **Realise a matrix Lie algebra as a linear subspace of $\operatorname{Mat}(n\times n;\mathbb K)$ cut out by linear conditions.** The identification $\mathfrak{su}(2)=\{A:A^{*}=-A,\ \operatorname{tr}A=0\}$ turns membership into two linear checks. We apply it to each $X_a$ by computing the conjugate transpose and the trace.

2. **Certify a basis from independence plus the known dimension.** Instead of proving spanning, we prove linear independence and quote $\dim_{\mathbb R}\mathfrak{su}(2)=3$ from [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]]. This is the standard finite-dimensional shortcut: an independent family whose cardinality equals the dimension is a basis.

3. **Compute the Lie bracket of a matrix algebra as the commutator.** On a matrix group the Lie bracket is $[A,B]=AB-BA$ ([[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator|the bracket-is-the-commutator identity]]). We use it to reduce the abstract bracket relations to concrete matrix multiplications.

4. **Extend a relation to all index pairs by antisymmetry.** Having computed the three commutators with $a<b$, we obtain the remaining pairs from $[X_b,X_a]=-[X_a,X_b]$ and the diagonal cases from $[X_a,X_a]=0$, matching the antisymmetry $\epsilon_{bac}=-\epsilon_{abc}$ and $\epsilon_{aac}=0$ of the Levi-Civita symbol.

---

# Hints

> [!note]- Hint 1
> "Basis of $\mathfrak{su}(2)$" splits into two finite tasks once you recall two facts from the prerequisite theorem: what $\mathfrak{su}(2)$ *is* as a set of matrices, and what its real dimension is. Do not try to write a general element of $\mathfrak{su}(2)$ as a combination of the $X_a$ yet; first just check the three matrices belong to $\mathfrak{su}(2)$.

> [!note]- Hint 2
> To place each $X_a$ in $\mathfrak{su}(2)$, compute its conjugate transpose $X_a^{*}=\overline{X_a}^{\,t}$ and its trace, and compare with the defining conditions $A^{*}=-A$, $\operatorname{tr}A=0$. For the basis claim, you do not need spanning: three linearly independent vectors in a three-dimensional space are a basis. So reduce a vanishing real combination $aX_1+bX_2+cX_3=0$ to $a=b=c=0$ by reading off matrix entries.

> [!note]- Hint 3
> For the bracket relations, use $[A,B]=AB-BA$ and compute only the three products with $a<b$: $[X_1,X_2]$, $[X_2,X_3]$, $[X_3,X_1]$. Multiply the explicit $2\times2$ matrices, subtract, and recognise the answer as $2X_3$, $2X_1$, $2X_2$ respectively. Then get every other index pair from antisymmetry of the commutator and from $[X_a,X_a]=0$, and check this is exactly what $2\epsilon_{abc}X_c$ predicts.

---

# Solution

The plan is to treat the three assertions in order, each as a finite matrix computation. First we check that each $X_a$ is anti-Hermitian and traceless, so that it lies in $\mathfrak{su}(2)$ as identified by the prerequisite theorem. Then we prove the three matrices are linearly independent and invoke $\dim_{\mathbb R}\mathfrak{su}(2)=3$ to promote independence to "basis". Finally we compute the three commutators with $a<b$ directly and extend to the full table $[X_a,X_b]=2\epsilon_{abc}X_c$ by antisymmetry.

**Step 1: Each $X_a=-i\sigma_a$ lies in $\mathfrak{su}(2)$.**

Each of the three matrices is anti-Hermitian and traceless, hence an element of $\mathfrak{su}(2)=\{A:A^{*}=-A,\ \operatorname{tr}A=0\}$.

> [!note]- Derivation
> We compute the conjugate transpose $X_a^{*}=\overline{X_a}^{\,t}$ and the trace of each generator.
>
> For $X_1=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}$: the complex conjugate is $\overline{X_1}=\begin{pmatrix}0&i\\i&0\end{pmatrix}$, and transposing the symmetric result leaves it unchanged, so
> $$X_1^{*}=\overline{X_1}^{\,t}=\begin{pmatrix}0&i\\i&0\end{pmatrix}=-\begin{pmatrix}0&-i\\-i&0\end{pmatrix}=-X_1\qquad\text{(conjugate then transpose),}$$
> and $\operatorname{tr}X_1=0+0=0$ (sum of the diagonal entries).
>
> For $X_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$: the entries are real, so $\overline{X_2}=X_2$, and the transpose flips the off-diagonal signs, giving
> $$X_2^{*}=\overline{X_2}^{\,t}=X_2^{\,t}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-\begin{pmatrix}0&-1\\1&0\end{pmatrix}=-X_2\qquad\text{(real entries, then transpose),}$$
> and $\operatorname{tr}X_2=0+0=0$.
>
> For $X_3=\begin{pmatrix}-i&0\\0&i\end{pmatrix}$: it is diagonal, so the transpose is itself, and conjugation flips the signs of the imaginary diagonal entries,
> $$X_3^{*}=\overline{X_3}^{\,t}=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=-\begin{pmatrix}-i&0\\0&i\end{pmatrix}=-X_3\qquad\text{(diagonal, so transpose is trivial; conjugate the entries),}$$
> and $\operatorname{tr}X_3=-i+i=0$.
>
> Thus $X_a^{*}=-X_a$ and $\operatorname{tr}X_a=0$ for each $a\in\{1,2,3\}$, so by the identification of $\mathfrak{su}(2)$ recalled from [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]] we have $X_1,X_2,X_3\in\mathfrak{su}(2)$.

**Step 2: $(X_1,X_2,X_3)$ is a real basis of $\mathfrak{su}(2)$.**

The three matrices are linearly independent over $\mathbb R$, and $\dim_{\mathbb R}\mathfrak{su}(2)=3$, so they form a basis.

> [!note]- Derivation
> Suppose $a,b,c\in\mathbb R$ satisfy $aX_1+bX_2+cX_3=0$. Writing the left-hand side out entry by entry,
> $$aX_1+bX_2+cX_3=a\begin{pmatrix}0&-i\\-i&0\end{pmatrix}+b\begin{pmatrix}0&-1\\1&0\end{pmatrix}+c\begin{pmatrix}-i&0\\0&i\end{pmatrix}=\begin{pmatrix}-ic&-ia-b\\-ia+b&ic\end{pmatrix}\qquad\text{(add the three scaled matrices).}$$
> Setting this equal to the zero matrix forces each entry to vanish. The top-left entry gives $-ic=0$, hence $c=0$. The top-right entry gives $-ia-b=0$; separating real and imaginary parts of this complex equation (with $a,b\in\mathbb R$) yields $b=0$ (real part) and $a=0$ (imaginary part). The remaining entries $-ia+b=0$ and $ic=0$ are then satisfied automatically. Hence $a=b=c=0$, so the only real combination of $X_1,X_2,X_3$ that vanishes is the trivial one; the three matrices are linearly independent over $\mathbb R$.
>
> By Step 1 the three matrices lie in $\mathfrak{su}(2)$, and by [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]] the real dimension of $\mathfrak{su}(2)$ is $2^2-1=3$. A linearly independent family of three vectors inside a real vector space of dimension exactly three is a basis of that space: independence gives $\dim\operatorname{span}\{X_1,X_2,X_3\}=3=\dim_{\mathbb R}\mathfrak{su}(2)$, and a three-dimensional subspace of a three-dimensional space is the whole space, so $\operatorname{span}_{\mathbb R}\{X_1,X_2,X_3\}=\mathfrak{su}(2)$. Therefore $(X_1,X_2,X_3)$ is a real basis of $\mathfrak{su}(2)$.

**Step 3: The bracket relations $[X_a,X_b]=2\epsilon_{abc}X_c$.**

Direct multiplication gives the three commutators $[X_1,X_2]=2X_3$, $[X_2,X_3]=2X_1$, $[X_3,X_1]=2X_2$; antisymmetry of the commutator and the vanishing of $[X_a,X_a]$ fill in every remaining index pair, and the resulting table is exactly $2\epsilon_{abc}X_c$.

> [!note]- Derivation
> Throughout, $[A,B]=AB-BA$ is the matrix commutator, which is the Lie bracket on $\mathfrak{su}(2)\subset\operatorname{Mat}(2\times2;\mathbb C)$ by [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator|the bracket-is-the-commutator identity for matrix groups]]. We compute the three products with $a<b$.
>
> *The pair $(1,2)$.* Multiplying,
> $$X_1X_2=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}-i&0\\0&i\end{pmatrix}=X_3\qquad\text{(row-by-column product),}$$
> $$X_2X_1=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}0&-i\\-i&0\end{pmatrix}=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=-X_3\qquad\text{(row-by-column product),}$$
> so $[X_1,X_2]=X_1X_2-X_2X_1=X_3-(-X_3)=2X_3$.
>
> *The pair $(2,3)$.* Multiplying,
> $$X_2X_3=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}-i&0\\0&i\end{pmatrix}=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}=X_1\qquad\text{(row-by-column product),}$$
> $$X_3X_2=\begin{pmatrix}-i&0\\0&i\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}0&i\\i&0\end{pmatrix}=-X_1\qquad\text{(row-by-column product),}$$
> so $[X_2,X_3]=X_2X_3-X_3X_2=X_1-(-X_1)=2X_1$.
>
> *The pair $(3,1)$.* Multiplying,
> $$X_3X_1=\begin{pmatrix}-i&0\\0&i\end{pmatrix}\begin{pmatrix}0&-i\\-i&0\end{pmatrix}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=X_2\qquad\text{(row-by-column product; }(-i)(-i)=-1\text{),}$$
> $$X_1X_3=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}\begin{pmatrix}-i&0\\0&i\end{pmatrix}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-X_2\qquad\text{(row-by-column product),}$$
> so $[X_3,X_1]=X_3X_1-X_1X_3=X_2-(-X_2)=2X_2$.
>
> **Assembling the full table.** We now show $[X_a,X_b]=2\epsilon_{abc}X_c$ for every ordered pair $(a,b)$, treating the three exhaustive kinds of pair.
>
> First, the diagonal pairs $a=b$: the commutator of any matrix with itself vanishes, $[X_a,X_a]=X_aX_a-X_aX_a=0$; and on the other side $\epsilon_{aac}=0$ because the Levi-Civita symbol vanishes when two indices coincide, so $2\epsilon_{aac}X_c=0$. The two sides agree.
>
> Second, the three pairs with $a<b$, namely $(1,2),(2,3),(3,1)$ (these are the cyclic pairs). The computations above give $[X_1,X_2]=2X_3$, $[X_2,X_3]=2X_1$, $[X_3,X_1]=2X_2$. On the right-hand side, $\epsilon_{123}=\epsilon_{231}=\epsilon_{312}=1$ by cyclic invariance of the Levi-Civita symbol, and for each such pair only the single term $c$ completing the cyclic triple is nonzero, so $2\epsilon_{12c}X_c=2X_3$, $2\epsilon_{23c}X_c=2X_1$, $2\epsilon_{31c}X_c=2X_2$. The two sides agree.
>
> Third, the three remaining pairs $(2,1),(3,2),(1,3)$ (the anticyclic pairs). By antisymmetry of the commutator, $[X_b,X_a]=-[X_a,X_b]$, so $[X_2,X_1]=-2X_3$, $[X_3,X_2]=-2X_1$, $[X_1,X_3]=-2X_2$. On the right-hand side, $\epsilon_{abc}$ is antisymmetric under exchanging the first two indices, $\epsilon_{bac}=-\epsilon_{abc}$, giving $\epsilon_{213}=\epsilon_{321}=\epsilon_{132}=-1$; hence $2\epsilon_{21c}X_c=-2X_3$, $2\epsilon_{32c}X_c=-2X_1$, $2\epsilon_{13c}X_c=-2X_2$. The two sides agree.
>
> Since the diagonal, cyclic, and anticyclic pairs exhaust all nine ordered pairs $(a,b)$ with $a,b\in\{1,2,3\}$, the identity $[X_a,X_b]=2\epsilon_{abc}X_c$ holds for every pair. Rewriting $X_a=-i\sigma_a$ gives the equivalent form $[-i\sigma_a,-i\sigma_b]=2\epsilon_{abc}(-i\sigma_c)$ requested in the statement.

> [!note]- Complete formal solution
> Set $X_a=-i\sigma_a$ for $a\in\{1,2,3\}$, with the standard Pauli matrices, so that $X_1=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}$, $X_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $X_3=\begin{pmatrix}-i&0\\0&i\end{pmatrix}$. By [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]], $\mathfrak{su}(2)=\{A\in\operatorname{Mat}(2\times2;\mathbb C):A^{*}=-A,\ \operatorname{tr}A=0\}$ with the commutator bracket, and $\dim_{\mathbb R}\mathfrak{su}(2)=3$.
>
> *Membership.* A direct computation of $A^{*}=\overline{A}^{\,t}$ gives $X_1^{*}=\begin{pmatrix}0&i\\i&0\end{pmatrix}=-X_1$, $X_2^{*}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-X_2$, $X_3^{*}=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=-X_3$, and each has zero trace. Hence $X_1,X_2,X_3\in\mathfrak{su}(2)$.
>
> *Basis.* If $aX_1+bX_2+cX_3=0$ with $a,b,c\in\mathbb R$, then the entry-wise identity $\begin{pmatrix}-ic&-ia-b\\-ia+b&ic\end{pmatrix}=0$ forces $c=0$ (from $-ic=0$) and $a=b=0$ (from the real and imaginary parts of $-ia-b=0$). So the three matrices are linearly independent over $\mathbb R$. Being three independent vectors inside the three-dimensional real space $\mathfrak{su}(2)$, they span it and form a basis.
>
> *Bracket relations.* Multiplying the explicit matrices gives $X_1X_2=X_3$, $X_2X_1=-X_3$; $X_2X_3=X_1$, $X_3X_2=-X_1$; $X_3X_1=X_2$, $X_1X_3=-X_2$. Hence $[X_1,X_2]=2X_3$, $[X_2,X_3]=2X_1$, $[X_3,X_1]=2X_2$. Together with $[X_a,X_a]=0$ (any matrix commutes with itself) and $[X_b,X_a]=-[X_a,X_b]$ (antisymmetry of the commutator), these determine the commutator on all nine ordered index pairs. The Levi-Civita symbol $\epsilon_{abc}$, normalised by $\epsilon_{123}=1$, is likewise totally antisymmetric and vanishes on repeated indices, with $\epsilon_{123}=\epsilon_{231}=\epsilon_{312}=1$ and $\epsilon_{213}=\epsilon_{321}=\epsilon_{132}=-1$. Matching pair by pair — diagonal pairs give $0=0$, cyclic pairs give $2X_{c}$, anticyclic pairs give $-2X_{c}$ — yields
> $$[X_a,X_b]=2\,\epsilon_{abc}\,X_c\qquad(a,b\in\{1,2,3\}),$$
> equivalently $[-i\sigma_a,-i\sigma_b]=2\epsilon_{abc}(-i\sigma_c)$. This proves all three assertions. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to quote the school identity $[\sigma_a,\sigma_b]=2i\epsilon_{abc}\sigma_c$ and simply multiply through by $(-i)^2=-1$ to get $[-i\sigma_a,-i\sigma_b]=-2i\epsilon_{abc}\sigma_c=2\epsilon_{abc}(-i\sigma_c)$. The algebra is correct, but it *imports* the Pauli commutation relation as a fact rather than proving it, and the identity $[\sigma_a,\sigma_b]=2i\epsilon_{abc}\sigma_c$ is precisely what a from-scratch solution must establish. The shortcut is legitimate only once that identity has itself been proved by matrix multiplication (or from $\sigma_a\sigma_b=\delta_{ab}I+i\epsilon_{abc}\sigma_c$, which again needs the nine products verified); until then the three explicit commutator computations above are the honest route.

---

# Key Takeaways

**A basis claim in a matrix Lie algebra is two finite checks, not a spanning computation, once the dimension is known.** The reusable principle is that "is a basis of $\mathfrak g$" for a family whose size equals $\dim\mathfrak g$ reduces to "each member lies in $\mathfrak g$" plus "the family is linearly independent"; spanning then comes for free from the dimension count. The trigger for this move is any problem that hands you exactly $\dim\mathfrak g$ concrete elements and asks for a basis — here three anti-Hermitian traceless matrices with $\dim_{\mathbb R}\mathfrak{su}(2)=3$. The transferable diagnostic is: before solving a spanning system with a general right-hand side, ask whether you already know the dimension; if you do, prove independence (a homogeneous condition, almost always easier) and stop. This is exactly how one certifies the generators $\{E_{ij}-E_{ji}\}$ of $\mathfrak{so}(n)$, the Gell-Mann matrices of $\mathfrak{su}(3)$, or any Cartan–Weyl basis of a classical algebra without ever inverting a change-of-basis matrix.

**Structure constants are computed once, in a fixed basis, and then reused everywhere the algebra appears.** The numbers $2\epsilon_{abc}$ produced here are not a curiosity of $\mathfrak{su}(2)$ in isolation; they are the coefficients that will recur every time a gauge-theoretic quantity is expanded in this basis. When the curvature $F=dA+\tfrac12[A\wedge A]$ of an $\mathfrak{su}(2)$-connection is written as $A=\sum_a A^a X_a$, the bracket term becomes $\tfrac12[A\wedge A]=\sum_{a,b}A^a\wedge A^b\,X_aX_b$, and the antisymmetric part is governed precisely by $[X_a,X_b]=2\epsilon_{abc}X_c$; the same constants organise the Chern–Simons integrand $\operatorname{tr}(A\wedge dA+\tfrac23 A\wedge A\wedge A)$ and the Yang–Mills bracket. The trigger is any expansion of a Lie-algebra-valued form in a chosen basis; the pattern is that the algebra's structure constants, fixed once by a computation like this one, do all the bookkeeping thereafter. This is why the very first thing one does with a new gauge group is pin down a basis of its Lie algebra and its bracket table.

**Conventions for named matrices differ between sources; anchor to the invariant content, not the printed symbols.** The Pauli matrices carry a fixed standard form, but a lecture writer may permute or re-sign them while calling the result "the Pauli matrices", as Bär does here by interchanging $\sigma_1$ and $\sigma_2$ and flipping signs. The reusable lesson is that a basis is defined only up to relabelling and rescaling, and the *structure constants in a specified basis* — together with the defining conditions of the algebra — are what carry the physics and the geometry, not the particular array of entries a book prints. The trigger condition is any moment where two sources disagree on an explicit matrix; the diagnostic is to check whether the disagreement is a Lie-algebra automorphism (a relabelling or a rotation of generators), in which case every bracket relation and every invariant such as $-\operatorname{tr}(XY)$ is preserved and the two conventions are interchangeable. Recording the conversion explicitly, as the Convention callout does, is the discipline that keeps a computation portable across the two textbooks this series draws on.

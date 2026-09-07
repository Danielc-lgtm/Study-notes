---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Exponential Map of a Matrix Group is the Matrix Exponential"
  - "Ex - SU(2) is the Group of Unit Quaternions"
  - "Thm - Lie Algebras and Dimensions of the Classical Matrix Groups"
tags: [geometry, gauge-theory]
---

# Problem Statement

Work with the special unitary group $SU(2)=\{A\in\operatorname{Mat}(2\times2;\mathbb{C}):A^{*}A=I,\ \det A=1\}$ and its Lie algebra $\mathfrak{su}(2)=\{X\in\operatorname{Mat}(2\times2;\mathbb{C}):X^{*}=-X,\ \operatorname{tr}X=0\}$ of traceless anti-Hermitian matrices. Let $\sigma_{1},\sigma_{2},\sigma_{3}$ be the **Pauli matrices**
$$\sigma_{1}=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad\sigma_{2}=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad\sigma_{3}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},$$
so that the three matrices $-i\sigma_{1},-i\sigma_{2},-i\sigma_{3}$ form a basis of $\mathfrak{su}(2)$. For a unit vector $n=(n_{1},n_{2},n_{3})\in\mathbb{R}^{3}$ with $|n|=1$ and a real number $\theta$, write
$$n\cdot(-i\sigma):=n_{1}(-i\sigma_{1})+n_{2}(-i\sigma_{2})+n_{3}(-i\sigma_{3})\in\mathfrak{su}(2),\qquad X:=\theta\,\bigl(n\cdot(-i\sigma)\bigr).$$

Prove the **quaternion exponential formula**
$$e^{X}=\cos\theta\;I+\sin\theta\;\bigl(n\cdot(-i\sigma)\bigr).\tag{$\ast$}$$
Deduce two consequences:

1. the exponential map $\exp\colon\mathfrak{su}(2)\to SU(2)$ is **surjective**;
2. with the norm $|X|:=\bigl(-\tfrac12\operatorname{tr}(X^{2})\bigr)^{1/2}$ on $\mathfrak{su}(2)$ (for which $|n\cdot(-i\sigma)|=1$, so $|X|=|\theta|$), the closed ball $\overline{B}_{\pi}=\{X\in\mathfrak{su}(2):|X|\le\pi\}$ maps **onto** $SU(2)$, its **boundary sphere** $\{|X|=\pi\}$ is collapsed to the single point $-I$, and the open ball maps bijectively onto $SU(2)\setminus\{-I\}$.

This last description — a closed $3$-ball with its boundary $2$-sphere crushed to a point, presenting $SU(2)\cong S^{3}$ — is used in Gauge Theory III §3.5 for constructing and classifying maps $S^{3}\to SU(2)$.

**Recall.**

The objects in play are the special unitary group and its Lie algebra, the identification of the abstract exponential with the matrix exponential, the Pauli-matrix presentation of $\mathfrak{su}(2)$, and the identification of $SU(2)$ with the unit quaternions and with $S^{3}$.

![[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential#Statement]]

In the case at hand: $SU(2)\subset GL(2;\mathbb{C})$ is a closed subgroup with Lie algebra $\mathfrak{su}(2)$, so [[Def - Exponential Map of a Lie Group|the abstract exponential]] equals the matrix exponential, $\exp(X)=e^{X}=\sum_{k\ge0}X^{k}/k!$ (absolutely convergent), and $e^{X}\in SU(2)$ for every $X\in\mathfrak{su}(2)$.

![[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups#Statement]]

The clause we use is $\mathfrak{su}(2)=\{X:X^{*}=-X,\ \operatorname{tr}X=0\}$, of real dimension $2^{2}-1=3$; the three anti-Hermitian traceless matrices $-i\sigma_{a}$ ($a=1,2,3$) are a basis, as verified in Step 0. That $-i\sigma_{a}\in\mathfrak{su}(2)$ is checked directly: $(-i\sigma_{a})^{*}=i\sigma_{a}^{*}=i\sigma_{a}=-(-i\sigma_{a})$ (each $\sigma_{a}$ is Hermitian) and $\operatorname{tr}(-i\sigma_{a})=-i\operatorname{tr}\sigma_{a}=0$ (each $\sigma_{a}$ is traceless).

For the geometric consequences we use the quaternion picture of $SU(2)$:

The exercise [[Ex - SU(2) is the Group of Unit Quaternions]] establishes a Lie-group isomorphism from the unit quaternions $Sp(1)=\{q\in\mathbb{H}:|q|=1\}$ to $SU(2)$, $q=z+wj\mapsto\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$, under which $SU(2)$ is identified with the unit sphere $S^{3}\subset\mathbb{H}=\mathbb{R}^{4}$. Explicitly, writing $A\in SU(2)$ as $A=a_{0}I+a_{1}(-i\sigma_{1})+a_{2}(-i\sigma_{2})+a_{3}(-i\sigma_{3})$ with $a_{0},a_{1},a_{2},a_{3}\in\mathbb{R}$, membership $A\in SU(2)$ is exactly $a_{0}^{2}+a_{1}^{2}+a_{2}^{2}+a_{3}^{2}=1$ (verified in Step 3 below); the point $(a_{0},a_{1},a_{2},a_{3})\in S^{3}$ is the corresponding unit quaternion. This is the linear dictionary between $2\times2$ special unitary matrices and unit quaternions that formula $(\ast)$ is the polar form of.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-closed-form-and-read-off-its-geometry* problem. The computational core is a single algebraic fact — that $n\cdot(-i\sigma)$ squares to $-I$ — which turns the matrix exponential series into the scalar Taylor series of $\cos$ and $\sin$; formula $(\ast)$ is then the matrix analogue of Euler's formula $e^{i\theta}=\cos\theta+i\sin\theta$. Everything after $(\ast)$ is geometry extracted from the formula: surjectivity is "every unit quaternion has a polar form", and the ball-with-collapsed-boundary picture is "the polar angle ranges over $[0,\pi]$ and the endpoints degenerate".

**Assumption pattern.** The decisive hypothesis is $|n|=1$. It enters through the Pauli multiplication law $(a\cdot\sigma)(b\cdot\sigma)=(a\cdot b)I+i(a\times b)\cdot\sigma$, which for $a=b=n$ gives $(n\cdot\sigma)^{2}=|n|^{2}I=I$; the cross-product term dies because $n\times n=0$. Hence $J:=n\cdot(-i\sigma)=-i(n\cdot\sigma)$ satisfies $J^{2}=-(n\cdot\sigma)^{2}=-I$. The recognisable trigger is any element of $\mathfrak{su}(2)$ written as $\theta$ times a *unit-norm* direction: the unit-norm condition is exactly what makes the direction square to $-I$, i.e. behave like the imaginary unit.

**Theorem routing.** The route is: [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|matrix-exponential theorem]] (absolute convergence and $\exp=e^{(\cdot)}$) to justify summing the series and to place the answer in $SU(2)$; the Pauli law and $|n|=1$ to get $J^{2}=-I$; splitting the series into even and odd powers to obtain $(\ast)$; the quaternion identification of [[Ex - SU(2) is the Group of Unit Quaternions|SU(2) with unit quaternions and with S³]] to interpret $(\ast)$ as a polar decomposition and thereby read off surjectivity and the ball picture.

**Key decision point.** The one move that unlocks everything is recognising $n\cdot(-i\sigma)$ as a *square root of $-I$* and hence as a copy of the imaginary unit inside $2\times2$ matrices; once $J^{2}=-I$ is in hand, the exponential is forced to be $\cos\theta\,I+\sin\theta\,J$ by the identical bookkeeping that proves $e^{i\theta}=\cos\theta+i\sin\theta$. The second decision, for the geometry, is to parametrise a target $A\in SU(2)$ by its quaternion coordinates $(a_{0},\vec a)$ and to *choose the polar angle* $\theta\in[0,\pi]$ with $\cos\theta=a_{0}$; the subtlety, which produces the collapsed boundary, is that at $\theta\in\{0,\pi\}$ the vector part $\sin\theta\,n$ vanishes, so the direction $n$ becomes invisible and a whole sphere of $X$'s maps to one matrix.

---

# Legal Operations Used

This solution deploys the following legal operations from the topic page's Legal Operations for §1.4 (named descriptively; the topic page is written after the subpages and the orchestrator reconciles the numbering):

1. **Reduce a matrix exponential to a scalar series via an algebraic relation on the exponent.** From $J^{2}=-I$ every power $J^{k}$ is $\pm I$ or $\pm J$, so $e^{\theta J}$ separates into the even part $\cos\theta\,I$ and the odd part $\sin\theta\,J$, exactly as [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]] permits for an absolutely convergent series.

2. **Compute a product of Pauli combinations by the multiplication law.** Use $(a\cdot\sigma)(b\cdot\sigma)=(a\cdot b)I+i(a\times b)\cdot\sigma$, proved from $\sigma_{a}\sigma_{b}=\delta_{ab}I+i\varepsilon_{abc}\sigma_{c}$, to obtain $(n\cdot\sigma)^{2}=I$ from $|n|=1$.

3. **Place the exponential in the group by the closed-subgroup clause.** [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]] guarantees $e^{X}\in SU(2)$ for $X\in\mathfrak{su}(2)$; alternatively verify $A^{*}A=I$ and $\det A=1$ directly from $(\ast)$.

4. **Parametrise the target by quaternion coordinates.** Write $A\in SU(2)$ as $a_{0}I+\vec a\cdot(-i\sigma)$ with $a_{0}^{2}+|\vec a|^{2}=1$, using the identification of [[Ex - SU(2) is the Group of Unit Quaternions|SU(2) with unit quaternions]]; this is the coordinate system in which $(\ast)$ becomes a polar decomposition.

5. **Solve for the polar data.** Given $(a_{0},\vec a)$ on the unit sphere, choose $\theta\in[0,\pi]$ with $\cos\theta=a_{0}$ and, when $\sin\theta\ne0$, recover the unit direction $n=\vec a/|\vec a|$; handle the degenerate cases $\sin\theta=0$ separately to obtain surjectivity and the boundary-collapse picture.

---

# Hints

> [!note]- Hint 1
> The exponent is $\theta$ times the fixed matrix $J:=n\cdot(-i\sigma)$. Everything hinges on one number: what is $J^{2}$? Compute it using $J=-i(n\cdot\sigma)$ and the fact that $(n\cdot\sigma)^{2}$ simplifies dramatically when $|n|=1$.

> [!note]- Hint 2
> The Pauli matrices satisfy $\sigma_{a}\sigma_{b}=\delta_{ab}I+i\varepsilon_{abc}\sigma_{c}$. Contract with $n_{a}n_{b}$: the symmetric part gives $|n|^{2}I=I$ and the antisymmetric $\varepsilon_{abc}$ part gives $0$ because $n_{a}n_{b}$ is symmetric. So $(n\cdot\sigma)^{2}=I$ and hence $J^{2}=(-i)^{2}(n\cdot\sigma)^{2}=-I$. Now $J$ behaves exactly like the imaginary unit $i$.

> [!note]- Hint 3
> With $J^{2}=-I$, expand $e^{\theta J}=\sum_{k}\theta^{k}J^{k}/k!$ and separate even $k=2m$ (where $J^{2m}=(-1)^{m}I$) from odd $k=2m+1$ (where $J^{2m+1}=(-1)^{m}J$). The two subseries are the Taylor series of $\cos\theta$ and $\sin\theta$. This is Euler's formula with $J$ in place of $i$.

> [!note]- Hint 4
> For surjectivity, take any $A\in SU(2)$ and write it in quaternion coordinates $A=a_{0}I+\vec a\cdot(-i\sigma)$ with $a_{0}^{2}+|\vec a|^{2}=1$. Compare with $(\ast)$: you need $\cos\theta=a_{0}$ and $\sin\theta\,n=\vec a$. Since $a_{0}\in[-1,1]$, a $\theta\in[0,\pi]$ with $\cos\theta=a_{0}$ exists; then $\sin\theta=\sqrt{1-a_{0}^{2}}=|\vec a|\ge0$, so set $n=\vec a/|\vec a|$ when $|\vec a|\ne0$. What happens when $|\vec a|=0$, i.e. $A=\pm I$? That is where the boundary sphere collapses.

---

# Solution

The computation reduces to one identity, $J^{2}=-I$ for $J=n\cdot(-i\sigma)$, after which $e^{\theta J}=\cos\theta\,I+\sin\theta\,J$ by the same series bookkeeping that gives Euler's formula. Reading $(\ast)$ in quaternion coordinates then makes surjectivity and the ball picture immediate: $(\cos\theta,\sin\theta\,n)$ traces out every unit quaternion as $\theta$ runs over $[0,\pi]$ and $n$ over the unit sphere, with the two endpoints $\theta\in\{0,\pi\}$ contributing only $\pm I$.

**Step 0: the $-i\sigma_{a}$ form a basis of $\mathfrak{su}(2)$, and the Pauli multiplication law.**

We record the two structural facts the computation rests on.

> [!note]- Derivation
> *The basis.* Each Pauli matrix $\sigma_{a}$ is Hermitian ($\sigma_{a}^{*}=\sigma_{a}$, visible from the displayed entries) and traceless ($\operatorname{tr}\sigma_{a}=0$). Hence $-i\sigma_{a}$ is anti-Hermitian, $(-i\sigma_{a})^{*}=\overline{(-i)}\,\sigma_{a}^{*}=i\sigma_{a}=-(-i\sigma_{a})$, and traceless, $\operatorname{tr}(-i\sigma_{a})=-i\operatorname{tr}\sigma_{a}=0$; so $-i\sigma_{a}\in\mathfrak{su}(2)$ for each $a$. They are linearly independent over $\mathbb{R}$: a real relation $\sum_{a}c_{a}(-i\sigma_{a})=0$ reads $-i\sum_{a}c_{a}\sigma_{a}=0$, and $c_{1}\sigma_{1}+c_{2}\sigma_{2}+c_{3}\sigma_{3}=\begin{pmatrix}c_{3}&c_{1}-ic_{2}\\ c_{1}+ic_{2}&-c_{3}\end{pmatrix}=0$ forces $c_{3}=0$ and $c_{1}-ic_{2}=0$, hence $c_{1}=c_{2}=0$. Since $\dim_{\mathbb{R}}\mathfrak{su}(2)=3$ by [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups|the dimension count]], three independent elements span, so $\{-i\sigma_{1},-i\sigma_{2},-i\sigma_{3}\}$ is a basis.
>
> *The multiplication law.* We claim that the products $\sigma_{a}\sigma_{b}$ satisfy
> $$\sigma_{a}\sigma_{b}=\delta_{ab}I+i\,\varepsilon_{abc}\,\sigma_{c}\qquad(a,b\in\{1,2,3\}),\tag{4}$$
> where $\delta_{ab}$ is the Kronecker delta, $\varepsilon_{abc}$ the totally antisymmetric symbol with $\varepsilon_{123}=1$, and the repeated index $c$ is summed over $\{1,2,3\}$. We verify all nine products by direct matrix multiplication of the displayed $\sigma_{a}$. The three diagonal cases are
> $$\sigma_{1}^{2}=\begin{pmatrix}0&1\\1&0\end{pmatrix}^{2}=I,\qquad\sigma_{2}^{2}=\begin{pmatrix}0&-i\\i&0\end{pmatrix}^{2}=I,\qquad\sigma_{3}^{2}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}^{2}=I,$$
> each matching the right-hand side $\delta_{aa}I+i\varepsilon_{aac}\sigma_{c}=I$ (no sum on $a$ here; $\varepsilon_{aac}=0$). The three products in cyclic order $123$ are
> $$\sigma_{1}\sigma_{2}=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&-i\\i&0\end{pmatrix}=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=i\sigma_{3},$$
> $$\sigma_{2}\sigma_{3}=\begin{pmatrix}0&-i\\i&0\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&i\\i&0\end{pmatrix}=i\sigma_{1},$$
> $$\sigma_{3}\sigma_{1}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=i\sigma_{2},$$
> each matching $\delta_{ab}I+i\varepsilon_{abc}\sigma_{c}=i\sigma_{c}$ with $(a,b,c)$ a cyclic permutation of $(1,2,3)$, so $\varepsilon_{abc}=+1$. The three products in anticyclic order are the transposes of these under $a\leftrightarrow b$,
> $$\sigma_{2}\sigma_{1}=\begin{pmatrix}0&-i\\i&0\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}-i&0\\0&i\end{pmatrix}=-i\sigma_{3},$$
> $$\sigma_{3}\sigma_{2}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&-i\\i&0\end{pmatrix}=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}=-i\sigma_{1},$$
> $$\sigma_{1}\sigma_{3}=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=-i\sigma_{2},$$
> each matching $i\varepsilon_{abc}\sigma_{c}=-i\sigma_{c}$ with $(a,b,c)$ an anticyclic permutation, so $\varepsilon_{abc}=-1$. All nine products agree with (4), so (4) holds. Contracting (4) with $a_{a}b_{b}$ and summing over $a,b$ for vectors $a,b\in\mathbb{R}^{3}$ gives the vector form
> $$(a\cdot\sigma)(b\cdot\sigma)=(a\cdot b)\,I+i\,(a\times b)\cdot\sigma,\tag{5}$$
> since $\sum_{a,b}a_{a}b_{b}\delta_{ab}=a\cdot b$ and $\sum_{a,b}a_{a}b_{b}\,i\varepsilon_{abc}\sigma_{c}=i(a\times b)_{c}\sigma_{c}$ by the definition $(a\times b)_{c}=\varepsilon_{abc}a_{a}b_{b}$ of the cross product.

**Step 1: the exponent direction squares to $-I$.**

The matrix $J:=n\cdot(-i\sigma)$ satisfies $J^{2}=-I$.

> [!note]- Derivation
> Write $J=n\cdot(-i\sigma)=-i\,(n\cdot\sigma)$. Applying (5) with $a=b=n$,
> $$(n\cdot\sigma)^{2}=(n\cdot n)\,I+i\,(n\times n)\cdot\sigma=|n|^{2}\,I+0=I\qquad\text{(by }(5)\text{, and }n\times n=0\text{, and }|n|=1\text{)}.$$
> Therefore
> $$J^{2}=\bigl(-i(n\cdot\sigma)\bigr)^{2}=(-i)^{2}(n\cdot\sigma)^{2}=(-1)\,I=-I.\tag{6}$$
> Thus $J$ is a square root of $-I$: it behaves algebraically exactly like the imaginary unit. This is the only place the hypothesis $|n|=1$ is used, and it is used decisively — for a general $n$ one would get $J^{2}=-|n|^{2}I$, and the angle $\theta$ below would be rescaled by $|n|$.

**Step 2: sum the exponential series to obtain formula $(\ast)$.**

$e^{X}=e^{\theta J}=\cos\theta\,I+\sin\theta\,J$.

> [!note]- Derivation
> By [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]] the series $e^{\theta J}=\sum_{k\ge0}\theta^{k}J^{k}/k!$ converges absolutely, so we may reorder it into even and odd terms. From (6), $J^{2}=-I$, so by induction the powers are
> $$J^{2m}=(-1)^{m}I,\qquad J^{2m+1}=(-1)^{m}J\qquad(m\ge0).$$
> Splitting the sum accordingly,
> $$e^{\theta J}=\sum_{m\ge0}\frac{\theta^{2m}}{(2m)!}J^{2m}+\sum_{m\ge0}\frac{\theta^{2m+1}}{(2m+1)!}J^{2m+1}\qquad\text{(reordering the absolutely convergent series)}$$
> $$=\Bigl(\sum_{m\ge0}\frac{(-1)^{m}\theta^{2m}}{(2m)!}\Bigr)I+\Bigl(\sum_{m\ge0}\frac{(-1)^{m}\theta^{2m+1}}{(2m+1)!}\Bigr)J\qquad\text{(inserting }J^{2m}=(-1)^{m}I,\ J^{2m+1}=(-1)^{m}J\text{)}$$
> $$=\cos\theta\;I+\sin\theta\;J\qquad\text{(Taylor series of }\cos\text{ and }\sin\text{).}$$
> Substituting $J=n\cdot(-i\sigma)$ gives exactly $(\ast)$:
> $$e^{X}=\cos\theta\;I+\sin\theta\;\bigl(n\cdot(-i\sigma)\bigr).$$
> The computation is Euler's formula $e^{i\theta}=\cos\theta+i\sin\theta$ with the scalar $i$ replaced by the matrix square-root-of-$-I$, $J$.

**Step 3: $e^{X}\in SU(2)$, in quaternion coordinates.**

The matrix $(\ast)$ lies in $SU(2)$, and its four real coordinates $(\cos\theta,\sin\theta\,n)$ lie on the unit sphere $S^{3}$.

> [!note]- Derivation
> That $e^{X}\in SU(2)$ is immediate from [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]], since $X\in\mathfrak{su}(2)$ and $SU(2)$ is a closed subgroup of $GL(2;\mathbb{C})$. We verify it independently to expose the quaternion coordinates. Set $a_{0}=\cos\theta$ and $\vec a=\sin\theta\,n$, so that
> $$A:=e^{X}=a_{0}I+\vec a\cdot(-i\sigma)=\begin{pmatrix}a_{0}-ia_{3}&-a_{2}-ia_{1}\\ a_{2}-ia_{1}&a_{0}+ia_{3}\end{pmatrix}\qquad\text{(inserting the entries of }\sigma_{1},\sigma_{2},\sigma_{3}\text{)}.$$
> Writing $z=a_{0}-ia_{3}$ and $w=-a_{2}-ia_{1}$, this is $A=\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$, precisely the shape of the quaternion embedding of [[Ex - SU(2) is the Group of Unit Quaternions|Sp(1) ≅ SU(2)]]. Then
> $$\det A=|z|^{2}+|w|^{2}=a_{0}^{2}+a_{3}^{2}+a_{2}^{2}+a_{1}^{2}=\cos^{2}\theta+\sin^{2}\theta\,|n|^{2}=\cos^{2}\theta+\sin^{2}\theta=1\qquad\text{(since }|n|=1\text{)},$$
> and $A^{*}A=I$ follows because a matrix of the form $\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$ with $|z|^{2}+|w|^{2}=1$ has orthonormal columns under the standard Hermitian inner product $\langle u,v\rangle=\bar u_{1}v_{1}+\bar u_{2}v_{2}$, which is exactly the statement $A^{*}A=I$ since $(A^{*}A)_{ij}=\langle\text{column }i,\text{column }j\rangle$. Writing the columns $u=(z,-\bar w)^{t}$ and $v=(w,\bar z)^{t}$, we compute
> $$\langle u,u\rangle=\bar z z+\overline{(-\bar w)}(-\bar w)=|z|^{2}+|w|^{2}=1,\qquad\langle v,v\rangle=\bar w w+\overline{\bar z}\,\bar z=|w|^{2}+|z|^{2}=1,$$
> $$\langle u,v\rangle=\bar z w+\overline{(-\bar w)}\,\bar z=\bar z w+(-w)\bar z=\bar z w-w\bar z=0\qquad\text{(scalars commute)},$$
> using $\overline{(-\bar w)}=-w$ and $\overline{\bar z}=z$. Hence $A^{*}A=I$, so $A\in SU(2)$, with quaternion coordinates $(a_{0},a_{1},a_{2},a_{3})=(\cos\theta,\sin\theta\,n)$ satisfying $a_{0}^{2}+|\vec a|^{2}=1$, i.e. lying on $S^{3}$.

**Step 4 (Consequence 1): the exponential is surjective.**

Every $A\in SU(2)$ equals $e^{X}$ for some $X\in\mathfrak{su}(2)$.

> [!note]- Derivation
> Let $A\in SU(2)$. By the quaternion identification of [[Ex - SU(2) is the Group of Unit Quaternions|SU(2) with unit quaternions]], $A$ has real coordinates
> $$A=a_{0}I+a_{1}(-i\sigma_{1})+a_{2}(-i\sigma_{2})+a_{3}(-i\sigma_{3}),\qquad a_{0}^{2}+a_{1}^{2}+a_{2}^{2}+a_{3}^{2}=1,$$
> with $a_{0},\dots,a_{3}\in\mathbb{R}$; write $\vec a=(a_{1},a_{2},a_{3})$, so $a_{0}^{2}+|\vec a|^{2}=1$ and in particular $a_{0}\in[-1,1]$.
>
> *Choose the polar angle.* Since $a_{0}\in[-1,1]$, there is a unique $\theta\in[0,\pi]$ with $\cos\theta=a_{0}$ ($\cos$ is a bijection $[0,\pi]\to[-1,1]$). For this $\theta$, $\sin\theta\ge0$ and $\sin^{2}\theta=1-\cos^{2}\theta=1-a_{0}^{2}=|\vec a|^{2}$, hence $\sin\theta=|\vec a|$.
>
> *Choose the direction.* If $|\vec a|\ne0$, set $n=\vec a/|\vec a|$, a unit vector; then $\sin\theta\,n=|\vec a|\cdot\vec a/|\vec a|=\vec a$, and $X:=\theta\,(n\cdot(-i\sigma))\in\mathfrak{su}(2)$ satisfies, by $(\ast)$,
> $$e^{X}=\cos\theta\,I+\sin\theta\,(n\cdot(-i\sigma))=a_{0}I+\vec a\cdot(-i\sigma)=A.$$
> If $|\vec a|=0$, then $a_{0}=\pm1$ and $A=a_{0}I=\pm I$; take any unit vector $n$ and set $\theta=0$ (giving $e^{0}=I$) or $\theta=\pi$ (giving, by $(\ast)$, $e^{\pi(n\cdot(-i\sigma))}=\cos\pi\,I+\sin\pi\,(\ldots)=-I$), matching $A=\pm I$ respectively.
>
> In every case $A=e^{X}$ with $X\in\mathfrak{su}(2)$, so $\exp\colon\mathfrak{su}(2)\to SU(2)$ is surjective.

**Step 5 (Consequence 2): the ball of radius $\pi$ maps onto $SU(2)$ with boundary crushed to $-I$.**

With $|X|=|\theta|$ for $X=\theta\,(n\cdot(-i\sigma))$, the closed ball $\overline{B}_{\pi}$ maps onto $SU(2)$, the sphere $|X|=\pi$ maps to $\{-I\}$, and the open ball maps bijectively onto $SU(2)\setminus\{-I\}$.

> [!note]- Derivation
> *The norm.* For $X=\theta\,(n\cdot(-i\sigma))=\theta J$ we have $X^{2}=\theta^{2}J^{2}=-\theta^{2}I$ by (6), so
> $$-\tfrac12\operatorname{tr}(X^{2})=-\tfrac12\operatorname{tr}(-\theta^{2}I)=-\tfrac12(-\theta^{2})\cdot2=\theta^{2}\qquad\text{(}\operatorname{tr}I=2\text{ in }2\times2\text{)},$$
> hence $|X|=|\theta|$; in particular $|n\cdot(-i\sigma)|=1$ ($\theta=1$). We may take $\theta\ge0$ throughout, since the direction of the sign is absorbed into $n\mapsto-n$: $\theta\,(n\cdot(-i\sigma))=(-\theta)\,((-n)\cdot(-i\sigma))$. So $\overline{B}_{\pi}=\{\theta\,(n\cdot(-i\sigma)):0\le\theta\le\pi,\ |n|=1\}\cup\{0\}$.
>
> *Onto.* Step 4 produced, for every $A\in SU(2)$, a preimage with $\theta\in[0,\pi]$, i.e. an $X$ with $|X|=\theta\le\pi$, so $X\in\overline{B}_{\pi}$. Hence $\exp(\overline{B}_{\pi})=SU(2)$.
>
> *Boundary collapse.* On the boundary sphere $|X|=\pi$, that is $X=\pi\,(n\cdot(-i\sigma))$ with $|n|=1$, formula $(\ast)$ gives
> $$e^{X}=\cos\pi\,I+\sin\pi\,(n\cdot(-i\sigma))=-I+0=-I\qquad\text{for every unit }n.$$
> So the entire $2$-sphere $\{|X|=\pi\}$ is sent to the single point $-I$.
>
> *Injectivity on the open ball.* Suppose $0\le\theta<\pi$, $0\le\theta'<\pi$, $|n|=|n'|=1$, and $e^{\theta(n\cdot(-i\sigma))}=e^{\theta'(n'\cdot(-i\sigma))}$. Comparing quaternion coordinates via $(\ast)$ and Step 3, $\cos\theta=\cos\theta'$ and $\sin\theta\,n=\sin\theta'\,n'$. On $[0,\pi)$ the cosine is injective, so $\theta=\theta'$; then $\sin\theta\,n=\sin\theta\,n'$, and if $\theta\ne0$ (so $\sin\theta>0$) we get $n=n'$, giving the same $X$; if $\theta=0$ both are the zero matrix $X=0$, again the same point. So $\exp$ is injective on the open ball $\{|X|<\pi\}$, and its image is $\{\cos\theta\,I+\sin\theta\,(n\cdot(-i\sigma)):0\le\theta<\pi\}=SU(2)\setminus\{-I\}$ (the only element with $a_{0}=\cos\theta=-1$ is $-I$, attained only at $\theta=\pi$). Thus the open ball maps bijectively onto $SU(2)\setminus\{-I\}$, and adjoining the boundary sphere — all of it sent to $-I$ — fills in the missing point. This exhibits $SU(2)$ as the quotient of the closed $3$-ball $\overline{B}_{\pi}$ by collapsing its boundary $2$-sphere to a point, which is one standard model of $S^{3}$.

> [!note]- Complete formal solution
> **Claim.** For $X=\theta\,(n\cdot(-i\sigma))$ with $|n|=1$, $\theta\in\mathbb{R}$, one has $e^{X}=\cos\theta\,I+\sin\theta\,(n\cdot(-i\sigma))$; consequently $\exp\colon\mathfrak{su}(2)\to SU(2)$ is onto, and the closed ball $\overline{B}_{\pi}$ maps onto $SU(2)$ with its boundary sphere collapsed to $-I$ and its interior mapped bijectively onto $SU(2)\setminus\{-I\}$.
>
> The Pauli matrices satisfy $\sigma_{a}\sigma_{b}=\delta_{ab}I+i\varepsilon_{abc}\sigma_{c}$, whence $(a\cdot\sigma)(b\cdot\sigma)=(a\cdot b)I+i(a\times b)\cdot\sigma$. With $a=b=n$ and $|n|=1$, $(n\cdot\sigma)^{2}=|n|^{2}I=I$, so $J:=n\cdot(-i\sigma)=-i(n\cdot\sigma)$ has $J^{2}=(-i)^{2}(n\cdot\sigma)^{2}=-I$.
>
> By the matrix-exponential theorem the series $e^{\theta J}=\sum_{k}\theta^{k}J^{k}/k!$ converges absolutely; using $J^{2m}=(-1)^{m}I$ and $J^{2m+1}=(-1)^{m}J$ and reordering,
> $$e^{\theta J}=\Bigl(\sum_{m}\tfrac{(-1)^{m}\theta^{2m}}{(2m)!}\Bigr)I+\Bigl(\sum_{m}\tfrac{(-1)^{m}\theta^{2m+1}}{(2m+1)!}\Bigr)J=\cos\theta\,I+\sin\theta\,J,$$
> which is $(\ast)$. Setting $a_{0}=\cos\theta$, $\vec a=\sin\theta\,n$, the matrix $A=e^{X}=a_{0}I+\vec a\cdot(-i\sigma)=\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$ with $z=a_{0}-ia_{3}$, $w=-a_{2}-ia_{1}$ has $\det A=|z|^{2}+|w|^{2}=a_{0}^{2}+|\vec a|^{2}=\cos^{2}\theta+\sin^{2}\theta=1$ and is unitary, so $A\in SU(2)$, with quaternion coordinates $(\cos\theta,\sin\theta\,n)\in S^{3}$.
>
> *Surjectivity.* Given $A\in SU(2)$, write $A=a_{0}I+\vec a\cdot(-i\sigma)$, $a_{0}^{2}+|\vec a|^{2}=1$. Pick $\theta\in[0,\pi]$ with $\cos\theta=a_{0}$; then $\sin\theta=|\vec a|$. If $\vec a\ne0$ set $n=\vec a/|\vec a|$, so $(\ast)$ gives $e^{\theta(n\cdot(-i\sigma))}=a_{0}I+\vec a\cdot(-i\sigma)=A$. If $\vec a=0$ then $A=\pm I=e^{0}$ or $e^{\pi(n\cdot(-i\sigma))}$ for any unit $n$. So $\exp$ is onto.
>
> *Ball picture.* Since $X^{2}=-\theta^{2}I$, $|X|^{2}=-\tfrac12\operatorname{tr}(X^{2})=\theta^{2}$, so $|X|=|\theta|$ and we may take $\theta\in[0,\pi]$. The preimages found above have $\theta\le\pi$, so $\exp(\overline{B}_{\pi})=SU(2)$. On $|X|=\pi$, $e^{X}=\cos\pi\,I=-I$ for all $n$, collapsing the boundary sphere to $-I$. For $\theta,\theta'\in[0,\pi)$, $\cos\theta=\cos\theta'$ forces $\theta=\theta'$ and then $\sin\theta\,n=\sin\theta\,n'$ forces $n=n'$ when $\theta\ne0$, so $\exp$ is injective on $\{|X|<\pi\}$ with image $SU(2)\setminus\{-I\}$. $\blacksquare$

> [!warning] Illegal but tempting shortcuts
> Two natural-looking moves are invalid here. **First**, one might try to split $e^{X}$ using $e^{A+B}=e^{A}e^{B}$ to reduce to the three coordinate directions $-i\sigma_{a}$ separately. This identity holds only when $A$ and $B$ commute, and the Pauli directions do *not* commute — indeed $[-i\sigma_{1},-i\sigma_{2}]=2(-i\sigma_{3})\ne0$ (see [[Ex - su(2) in the Basis of Anti-Hermitian Pauli Matrices|the Pauli-basis bracket relations]]) — so the factorisation is false; the correct route sums the *single* exponent $\theta J$ using $J^{2}=-I$. **Second**, one might claim $\exp$ is injective on the closed ball $\overline{B}_{\pi}$ because it is a bijection near $0$; but Step 5 shows the whole boundary sphere maps to $-I$, so $\exp$ is very far from injective on $\overline{B}_{\pi}$ — injectivity holds only on the *open* ball. The extra condition that restores injectivity is exactly deleting the boundary, and the failure of injectivity there is not a defect but the mechanism by which the ball becomes the sphere $S^{3}$.

> [!note]- Independent sanity check
> Take $\theta=\pi/2$ and $n=(0,0,1)$, so $X=\tfrac{\pi}{2}(-i\sigma_{3})=\begin{pmatrix}-i\pi/2&0\\0&i\pi/2\end{pmatrix}$. Direct diagonal exponentiation gives $e^{X}=\operatorname{diag}(e^{-i\pi/2},e^{i\pi/2})=\operatorname{diag}(-i,i)$. Formula $(\ast)$ gives $\cos\tfrac{\pi}{2}\,I+\sin\tfrac{\pi}{2}\,(-i\sigma_{3})=0+(-i\sigma_{3})=\operatorname{diag}(-i,i)$ — the same matrix, which is unitary with determinant $(-i)(i)=1$, hence in $SU(2)$. The two computations agree, confirming $(\ast)$ on a case where the exponential can be read off independently.

---

# Key Takeaways

**When an exponent squares to a scalar multiple of the identity, its exponential is a two-term trigonometric formula — the matrix Euler identity.** The entire computation is powered by $J^{2}=-I$: any matrix $J$ with $J^{2}=-I$ satisfies $e^{\theta J}=\cos\theta\,I+\sin\theta\,J$, and more generally $M^{2}=-c^{2}I$ gives $e^{M}=\cos c\,I+\tfrac{\sin c}{c}M$ while $M^{2}=c^{2}I$ gives $e^{M}=\cosh c\,I+\tfrac{\sinh c}{c}M$. The trigger to look for is a *single* exponent obeying a quadratic relation $M^{2}=\alpha I$; this happens automatically for traceless $2\times2$ matrices (via Cayley–Hamilton, $M^{2}=-\det M\,I$), which is why both $\mathfrak{su}(2)$ here and $\mathfrak{sl}(2;\mathbb{R})$ in the companion exercise [[Ex - The Exponential Map of SL(2,R) is Not Surjective]] are exactly computable. The transferable diagnostic: before summing a matrix exponential term by term, ask whether the exponent satisfies a low-degree polynomial relation; if it does, the series collapses to that many terms with scalar coefficients, and the relevant scalar functions are dictated by the sign of $\alpha$.

**The unit-norm hypothesis is what turns a Lie-algebra direction into a copy of the imaginary unit, and this is the algebraic content of the quaternion picture.** Requiring $|n|=1$ is not cosmetic normalisation; it is the exact condition making $(n\cdot\sigma)^{2}=I$, hence $n\cdot(-i\sigma)$ a square root of $-I$. Under the identification of $SU(2)$ with the unit quaternions, the matrices $n\cdot(-i\sigma)$ with $|n|=1$ are precisely the *imaginary unit quaternions* (the unit sphere in $\operatorname{Im}\mathbb{H}$), each squaring to $-1$, and $(\ast)$ is the quaternion polar form $q=\cos\theta+\sin\theta\,u$ with $u$ a unit imaginary quaternion. Reading a $\mathfrak{su}(2)$ computation quaternionically — angle plus axis — is usually faster than reading it matricially, and the dictionary "unit axis $\leftrightarrow$ square root of $-I$ $\leftrightarrow$ imaginary unit quaternion" is worth keeping ready. It is also the source of the double cover $SU(2)\to SO(3)$: conjugation by $e^{\theta(n\cdot(-i\sigma))}$ rotates $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^{3}$ by angle $2\theta$ about the axis $n$, the factor $2$ being exactly why the boundary at $\theta=\pi$ returns to $-I$ rather than $I$.

**Surjectivity of $\exp$ for $SU(2)$ is compactness at work, and the ball-with-collapsed-boundary is the geometry of that surjectivity.** In sharp contrast to the non-compact $SL(2;\mathbb{R})$, where $\exp$ misses $\operatorname{diag}(-2,-\tfrac12)$, the compact group $SU(2)$ is entirely covered by the exponential, and here we saw this by hand rather than by invoking [[Thm - The Exponential Map of a Compact Connected Lie Group is Surjective|the general compact surjectivity theorem]]. The finer statement — that $\overline{B}_{\pi}$ covers $SU(2)$ with the boundary sphere crushed to $-I$ — is the concrete presentation $SU(2)\cong S^{3}$ as a $3$-ball modulo its boundary, and it is the form in which the result is reused downstream: in Gauge Theory III §3.5 a map $S^{3}\to SU(2)$ is built and its degree computed by working on this ball model, where the collapse of the boundary to a single point is what lets a map defined on the solid ball descend to the sphere. The reusable principle is that the exponential of a compact group is not merely onto but provides an *explicit chart-with-a-collapse*: the largest ball on which $\exp$ is injective, together with the way its boundary degenerates, encodes the global topology of the group, and recognising the collapse locus (here the antipode $-I$, the cut locus of the identity) is the practical skill this exercise trains.

---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Pfaffian"
  - "Def - Determinant"
  - "Def - Alternating Multilinear Form"
difficulty: "⭐"
tags: [geometry, gauge-theory, characteristic-classes, linear-algebra]
---

# Problem Statement

Let
$$A=\begin{pmatrix}0&a_{12}&a_{13}&a_{14}\\-a_{12}&0&a_{23}&a_{24}\\-a_{13}&-a_{23}&0&a_{34}\\-a_{14}&-a_{24}&-a_{34}&0\end{pmatrix}\in\mathfrak{so}(4)$$
be a general real skew-symmetric $4\times4$ matrix, so that $A^{t}=-A$ and $A$ is determined by the six entries $a_{ij}$ with $1\le i<j\le4$ above the diagonal.

**(a)** Starting from the definition of the Pfaffian, prove the closed-form expression
$$\operatorname{Pf}(A)=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}.$$

**(b)** Compute the determinant $\det A$ by direct cofactor expansion and prove the identity
$$\operatorname{Pf}(A)^{2}=\det A.$$

Here $\mathfrak{so}(4)=\{A\in\operatorname{Mat}(4\times4;\mathbb{R}):A^{t}=-A\}$ is the Lie algebra of the special orthogonal group $SO(4)$; this is the case $2m=4$, that is $m=2$, of the general Pfaffian of a $\mathfrak{so}(2m)$ matrix. Every symbol $a_{ij}\in\mathbb{R}$ is an independent real variable, and $e_{1},\dots,e_{4}$ denotes the standard basis of $\mathbb{R}^{4}$ with $e_{i}\wedge e_{j}$ the corresponding basis element of the exterior square $\Lambda^{2}\mathbb{R}^{4}$.

**Recall:**

The objects in play are the Pfaffian of a skew matrix, the determinant, and the exterior (wedge) product of an alternating form; each is recalled here so that the page can be read without opening another file.

![[Def - Pfaffian#The Definition]]

For the case at hand, the [[Def - Pfaffian|Pfaffian]] of $A\in\mathfrak{so}(2m)$ is the degree-$m$ polynomial in the entries of $A$ given in either of two equivalent forms. The **permutation form** is
$$\operatorname{Pf}(A):=\frac{1}{2^{m}\,m!}\sum_{\sigma\in S_{2m}}\operatorname{sign}(\sigma)\prod_{i=1}^{m}A_{\sigma(2i-1)\,\sigma(2i)},$$
where $S_{2m}$ is the symmetric group on $\{1,\dots,2m\}$ and $\operatorname{sign}(\sigma)\in\{\pm1\}$ is the sign of the permutation $\sigma$. The **exterior form** encodes $A$ as the $2$-vector
$$\sigma_{A}:=\sum_{1\le i<j\le 2m}A_{ij}\,e_{i}\wedge e_{j}\in\Lambda^{2}\mathbb{R}^{2m},$$
and then $\operatorname{Pf}(A)$ is the single real number defined by
$$\frac{1}{m!}\,\sigma_{A}^{\wedge m}=\operatorname{Pf}(A)\,e_{1}\wedge\cdots\wedge e_{2m},$$
using that $\Lambda^{2m}\mathbb{R}^{2m}$ is one-dimensional with basis $e_{1}\wedge\cdots\wedge e_{2m}$. The two forms agree, which is proved on the definition page; here we use whichever is more convenient. For the smallest case $m=1$ both give $\operatorname{Pf}\!\begin{pmatrix}0&a\\-a&0\end{pmatrix}=a$.

![[Def - Determinant#The Definition]]

The [[Def - Determinant|determinant]] of a matrix $B=(B_{ij})\in\operatorname{Mat}(n\times n;\mathbb{R})$ is $\det B=\sum_{\sigma\in S_{n}}\operatorname{sign}(\sigma)\prod_{i=1}^{n}B_{i\,\sigma(i)}$; equivalently it may be computed by **cofactor expansion** along any row, $\det B=\sum_{j}B_{ij}(-1)^{i+j}M_{ij}$, where the minor $M_{ij}$ is the determinant of the matrix obtained by deleting row $i$ and column $j$ (this is [[Thm - Cofactor Expansion and Cramer's Rule|the cofactor-expansion theorem]]).

![[Def - Alternating Multilinear Form#The Definition]]

The wedge product on $\Lambda^{\bullet}\mathbb{R}^{n}$ is associative and graded-commutative: for a $p$-form $\alpha$ and a $q$-form $\beta$, $\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha$. In particular any $1$-form wedged with itself vanishes, and any two $2$-forms commute, $\alpha\wedge\beta=\beta\wedge\alpha$ (as recorded in [[Thm - Wedge Product Properties]]).

---

# Convergent Strategy

**Problem class.** This is a *closed-form-from-a-definition* computation followed by a *polynomial-identity verification*. Part (a) asks us to specialise a definition given by a sum over the symmetric group $S_{4}$ (twenty-four terms) to an explicit three-term polynomial; part (b) asks us to expand a $4\times4$ determinant and recognise the result as a perfect square. Neither part uses any structure beyond multilinear algebra, which is why the difficulty is a single star: the only risk is a sign slip.

**Assumption pattern.** The single standing hypothesis is that $A$ is skew-symmetric, $A^{t}=-A$, which is what makes the Pfaffian defined at all and what forces the diagonal entries $A_{ii}=0$ and the sub-diagonal entries $A_{ji}=-A_{ij}$. Every appearance of a lower entry $A_{ji}$ in the cofactor expansion is immediately rewritten as $-A_{ij}$ using this hypothesis; tracking those minus signs correctly is the whole content of part (b).

**Theorem routing.** For part (a) the efficient route is the exterior form of the Pfaffian rather than the twenty-four-term permutation sum: write $\sigma_{A}\in\Lambda^{2}\mathbb{R}^{4}$, square it, and read off the coefficient of $e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}$, using graded-commutativity of the wedge product from [[Thm - Wedge Product Properties]]. For part (b) the route is cofactor expansion from [[Thm - Cofactor Expansion and Cramer's Rule]] along the first row, three $3\times3$ minors, followed by an algebraic factorisation that exposes the Pfaffian as a common factor. The general identity $\operatorname{Pf}^{2}=\det$ on all of $\mathfrak{so}(2m)$ is proved abstractly on [[Thm - Properties of the Pfaffian]]; here we prove the $m=2$ case by hand so that the page is self-contained and the reader sees the mechanism in a concrete case.

**Key decision point.** The one move that turns part (b) from a page of algebra into three lines is *factoring the Pfaffian out of the expanded determinant*. After the three minors are computed, each of the three top-row terms is a product of the form $(\text{entry})\times(\text{entry})\times(\pm\operatorname{Pf}(A))$; recognising the common factor $\operatorname{Pf}(A)=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}$ inside every minor, and pulling it out, collapses the sum to $\operatorname{Pf}(A)\cdot\operatorname{Pf}(A)$. The temptation to instead multiply everything out into a $36$-term polynomial and hope it factors is the slow and error-prone route; the fast route watches for the Pfaffian appearing as a factor at the level of the minors.

---

# Legal Operations Used

1. **Encode a skew matrix as a $2$-vector (the operation "pass to the $\Lambda^{2}$ picture" from the topic page's Legal Operations).** We replace the matrix $A\in\mathfrak{so}(4)$ by $\sigma_{A}=\sum_{i<j}A_{ij}\,e_{i}\wedge e_{j}\in\Lambda^{2}\mathbb{R}^{4}$, which is the isomorphism $\mathfrak{so}(2m)\cong\Lambda^{2}\mathbb{R}^{2m}$; on this side the Pfaffian is a wedge power, which is far easier to compute than the permutation sum.

2. **Compute a wedge square using graded-commutativity.** In expanding $\sigma_{A}\wedge\sigma_{A}$ we discard every term $e_{i}\wedge e_{j}\wedge e_{k}\wedge e_{l}$ with a repeated index (it vanishes, a $1$-form wedged with itself being zero) and reorder the surviving four-index terms to the standard order $e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}$, tracking the sign of each reordering.

3. **Cofactor-expand a determinant along a row (operation "cofactor expansion" from the topic page).** We expand $\det A$ along its first row using [[Thm - Cofactor Expansion and Cramer's Rule]], reducing the $4\times4$ determinant to three signed $3\times3$ minors.

4. **Use skew-symmetry to eliminate entries.** Every entry $A_{ji}$ with $j>i$ that appears in a minor is rewritten as $-a_{ij}$, and every diagonal entry as $0$, using the hypothesis $A^{t}=-A$.

5. **Factor a common polynomial out of a sum.** After the minors are evaluated, we identify the Pfaffian $a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}$ as a factor of each summand and pull it out, collapsing the expanded determinant to a perfect square.

---

# Hints

> [!note]- Hint 1
> For part (a), do not expand the twenty-four-term permutation sum by brute force. Use instead the exterior description $\dfrac{1}{m!}\sigma_{A}^{\wedge m}=\operatorname{Pf}(A)\,e_{1}\wedge\cdots\wedge e_{2m}$. For $m=2$ this reads $\tfrac12\,\sigma_{A}\wedge\sigma_{A}=\operatorname{Pf}(A)\,e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}$, so you only need the coefficient of $e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}$ in $\tfrac12\,\sigma_{A}\wedge\sigma_{A}$.

> [!note]- Hint 2
> In $\sigma_{A}\wedge\sigma_{A}$ a term $e_{i}\wedge e_{j}\wedge e_{k}\wedge e_{l}$ survives only when $\{i,j,k,l\}=\{1,2,3,4\}$, that is, only when the two factors $e_{i}\wedge e_{j}$ and $e_{k}\wedge e_{l}$ use complementary index pairs. The complementary pairs of $\{1,2,3,4\}$ are $\{12,34\}$, $\{13,24\}$, $\{14,23\}$. Each unordered pair contributes twice (once in each order), and the two orders give the same four-form because $2$-forms commute.

> [!note]- Hint 3
> The three surviving four-index products, reordered to standard order, are $e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}=+E$, $e_{1}\wedge e_{3}\wedge e_{2}\wedge e_{4}=-E$, and $e_{1}\wedge e_{4}\wedge e_{2}\wedge e_{3}=+E$, where $E:=e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}$. The middle sign is the source of the minus in front of $a_{13}a_{24}$.

> [!note]- Hint 4
> For part (b), expand $\det A$ along the first row. You will get $\det A=-a_{12}M_{12}+a_{13}M_{13}-a_{14}M_{14}$ (the signs are the cofactor signs $(-1)^{1+j}$ and $a_{11}=0$). Compute each $3\times3$ minor. Each one factors as a single entry times $\pm(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23})$ — that is, each minor already contains the Pfaffian. Substitute and watch the whole thing collapse.

> [!note]- Hint 5
> Write $w:=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}=\operatorname{Pf}(A)$. You should find $M_{12}=-a_{34}\,w$, $M_{13}=-a_{24}\,w$, and $M_{14}=-a_{23}\,w$ after using skew-symmetry. Then $\det A=-a_{12}(-a_{34}w)+a_{13}(-a_{24}w)-a_{14}(-a_{23}w)=(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23})\,w=w^{2}$.

---

# Solution

**Plan.** Part (a) is a single wedge-square computation: encode $A$ as $\sigma_{A}\in\Lambda^{2}\mathbb{R}^{4}$, square it, keep only the three four-index terms, and read off $\operatorname{Pf}(A)$. Part (b) is a first-row cofactor expansion producing three $3\times3$ minors; after simplifying each minor with skew-symmetry, the Pfaffian $w=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}$ appears as a factor of every one of them, and the three top-row terms recombine into $w^{2}$. Throughout we abbreviate $E:=e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}$, the standard generator of $\Lambda^{4}\mathbb{R}^{4}$.

**Step 1: Encode $A$ as a $2$-vector and record the six coefficients.**

The skew matrix $A$ corresponds to $\sigma_{A}=\sum_{i<j}A_{ij}\,e_{i}\wedge e_{j}$, and the six coefficients are exactly the six above-diagonal entries.

> [!note]- Derivation
> By the exterior description of the Pfaffian, we form
> $$\sigma_{A}=\sum_{1\le i<j\le4}A_{ij}\,e_{i}\wedge e_{j}=a_{12}\,e_{1}\wedge e_{2}+a_{13}\,e_{1}\wedge e_{3}+a_{14}\,e_{1}\wedge e_{4}+a_{23}\,e_{2}\wedge e_{3}+a_{24}\,e_{2}\wedge e_{4}+a_{34}\,e_{3}\wedge e_{4}\qquad\text{(definition of }\sigma_{A}\text{, with the six entries }a_{ij}\text{).}$$
> Only above-diagonal entries appear because the sum runs over $i<j$; the below-diagonal entries $A_{ji}=-a_{ij}$ and the diagonal entries $A_{ii}=0$ are not summed separately. To lighten the notation write $e_{ij}:=e_{i}\wedge e_{j}$, so $\sigma_{A}=a_{12}e_{12}+a_{13}e_{13}+a_{14}e_{14}+a_{23}e_{23}+a_{24}e_{24}+a_{34}e_{34}$.

**Step 2: Square $\sigma_{A}$ and keep only the four-index terms.**

Wedging $\sigma_{A}$ with itself, every term with a repeated index dies; only the three complementary pairs $\{12,34\}$, $\{13,24\}$, $\{14,23\}$ survive.

> [!note]- Derivation
> Expanding $\sigma_{A}\wedge\sigma_{A}$ produces $6\times6=36$ terms of the form $A_{ij}A_{kl}\,e_{ij}\wedge e_{kl}$. A term vanishes whenever $\{i,j\}$ and $\{k,l\}$ share an index, since then $e_{ij}\wedge e_{kl}$ repeats a basis vector and $e_{p}\wedge e_{p}=0$ (a $1$-form wedged with itself is zero, by graded-commutativity, [[Thm - Wedge Product Properties]]). The only pairs $(\{i,j\},\{k,l\})$ of distinct index-pairs that are *disjoint* — hence use all four indices — come from the three ways to split $\{1,2,3,4\}$ into two pairs:
> $$\{1,2\}\sqcup\{3,4\},\qquad \{1,3\}\sqcup\{2,4\},\qquad \{1,4\}\sqcup\{2,3\}.$$
> Each unordered split occurs in two ordered forms inside the double sum (for example $e_{12}\wedge e_{34}$ and $e_{34}\wedge e_{12}$), and the two ordered forms are equal because two $2$-forms commute: $e_{34}\wedge e_{12}=(-1)^{2\cdot2}e_{12}\wedge e_{34}=e_{12}\wedge e_{34}$ (graded-commutativity with $p=q=2$). Collecting the two ordered forms of each split,
> $$\sigma_{A}\wedge\sigma_{A}=2a_{12}a_{34}\,(e_{12}\wedge e_{34})+2a_{13}a_{24}\,(e_{13}\wedge e_{24})+2a_{14}a_{23}\,(e_{14}\wedge e_{23})\qquad\text{(the three disjoint splits, each doubled).}$$

**Step 3: Reorder each four-index term to standard order and read off $\operatorname{Pf}(A)$.**

Reordering the indices to $1234$ introduces a sign $+,-,+$ respectively, and dividing by $m!=2$ gives the claimed formula.

> [!note]- Derivation
> We reorder each of the three basis four-forms to the standard generator $E=e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}$, tracking the sign produced by the transpositions used (each adjacent swap of distinct factors contributes $-1$, by graded-commutativity of $1$-forms):
> $$e_{12}\wedge e_{34}=e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}=+E\qquad\text{(already in order),}$$
> $$e_{13}\wedge e_{24}=e_{1}\wedge e_{3}\wedge e_{2}\wedge e_{4}=-\,e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}=-E\qquad\text{(one swap of the middle pair }e_{3}\wedge e_{2}=-e_{2}\wedge e_{3}\text{),}$$
> $$e_{14}\wedge e_{23}=e_{1}\wedge e_{4}\wedge e_{2}\wedge e_{3}=+\,e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}=+E\qquad\text{(two swaps: }e_{4}e_{2}e_{3}\to e_{2}e_{4}e_{3}\to e_{2}e_{3}e_{4}\text{).}$$
> Substituting into the result of Step 2,
> $$\sigma_{A}\wedge\sigma_{A}=\big(2a_{12}a_{34}-2a_{13}a_{24}+2a_{14}a_{23}\big)\,E\qquad\text{(inserting the three signs }+,-,+\text{).}$$
> By the defining relation $\tfrac{1}{m!}\sigma_{A}^{\wedge m}=\operatorname{Pf}(A)\,E$ with $m=2$, that is $\tfrac12\,\sigma_{A}\wedge\sigma_{A}=\operatorname{Pf}(A)\,E$, we divide by $2$ and compare coefficients of $E$:
> $$\operatorname{Pf}(A)=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}.$$
> This proves part (a).

> [!note]- Cross-check via the permutation sum
> The same answer drops out of the permutation form $\operatorname{Pf}(A)=\tfrac{1}{2^{2}\,2!}\sum_{\sigma\in S_{4}}\operatorname{sign}(\sigma)\,A_{\sigma(1)\sigma(2)}A_{\sigma(3)\sigma(4)}$, whose prefactor is $\tfrac{1}{8}$. The sum has $4!=24$ terms, but they collapse into three groups of eight. The value of $A_{\sigma(1)\sigma(2)}A_{\sigma(3)\sigma(4)}$ depends only on the unordered partition $\{\{\sigma(1),\sigma(2)\},\{\sigma(3),\sigma(4)\}\}$ of $\{1,2,3,4\}$ into two pairs, of which there are three; for each partition, the eight permutations realising it all carry the same signed contribution, because swapping the two entries of a pair flips both $\operatorname{sign}(\sigma)$ and the sign of the corresponding skew entry $A_{ji}=-A_{ij}$ (two sign flips cancel), and swapping the two pairs leaves everything unchanged. For the partition $\{12,34\}$ the eight terms each equal $\operatorname{sign}(\mathrm{id})\,A_{12}A_{34}=a_{12}a_{34}$, contributing $8a_{12}a_{34}$; for $\{13,24\}$ the representative $\sigma=(2\,3)$ has $\operatorname{sign}=-1$, contributing $8\cdot(-1)\,A_{13}A_{24}=-8a_{13}a_{24}$; for $\{14,23\}$ the representative $\sigma=(2\,4\,3)$ has $\operatorname{sign}=+1$, contributing $8a_{14}a_{23}$. Dividing the total $8(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23})$ by $8$ recovers $\operatorname{Pf}(A)=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}$, in agreement with the wedge computation.

**Step 4: Expand $\det A$ along the first row.**

Cofactor expansion along row $1$ gives $\det A=-a_{12}M_{12}+a_{13}M_{13}-a_{14}M_{14}$, since $A_{11}=0$ and the cofactor signs are $(-1)^{1+j}$.

> [!note]- Derivation
> By [[Thm - Cofactor Expansion and Cramer's Rule|cofactor expansion]] along the first row, $\det A=\sum_{j=1}^{4}A_{1j}(-1)^{1+j}M_{1j}$, where $M_{1j}$ is the minor obtained by deleting row $1$ and column $j$. The first-row entries are $A_{11}=0$, $A_{12}=a_{12}$, $A_{13}=a_{13}$, $A_{14}=a_{14}$, so
> $$\det A=a_{12}(-1)^{3}M_{12}+a_{13}(-1)^{4}M_{13}+a_{14}(-1)^{5}M_{14}=-a_{12}M_{12}+a_{13}M_{13}-a_{14}M_{14}\qquad\text{(cofactor signs }(-1)^{1+j}\text{, and }A_{11}=0\text{).}$$
> To write out the minors we record the lower three rows of $A$ in terms of the six variables, using skew-symmetry $A_{ji}=-a_{ij}$:
> $$\text{row }2=(-a_{12},\,0,\,a_{23},\,a_{24}),\quad \text{row }3=(-a_{13},\,-a_{23},\,0,\,a_{34}),\quad \text{row }4=(-a_{14},\,-a_{24},\,-a_{34},\,0).$$

**Step 5: Evaluate the three minors; each contains the Pfaffian as a factor.**

Direct $3\times3$ evaluation gives $M_{12}=-a_{34}\,w$, $M_{13}=-a_{24}\,w$, $M_{14}=-a_{23}\,w$, where $w=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}=\operatorname{Pf}(A)$.

> [!note]- Derivation
> Throughout write $w:=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}$, which is $\operatorname{Pf}(A)$ by part (a).
>
> **Minor $M_{12}$** (delete row $1$, column $2$): the remaining entries are rows $2,3,4$ and columns $1,3,4$,
> $$M_{12}=\det\begin{pmatrix}-a_{12}&a_{23}&a_{24}\\-a_{13}&0&a_{34}\\-a_{14}&-a_{34}&0\end{pmatrix}.$$
> Expanding along its first row,
> $$M_{12}=-a_{12}\det\begin{pmatrix}0&a_{34}\\-a_{34}&0\end{pmatrix}-a_{23}\det\begin{pmatrix}-a_{13}&a_{34}\\-a_{14}&0\end{pmatrix}+a_{24}\det\begin{pmatrix}-a_{13}&0\\-a_{14}&-a_{34}\end{pmatrix}\qquad\text{(cofactor expansion of the }3\times3\text{).}$$
> $$=-a_{12}\big(0-a_{34}(-a_{34})\big)-a_{23}\big(0-a_{34}(-a_{14})\big)+a_{24}\big((-a_{13})(-a_{34})-0\big)\qquad\text{(evaluating the three }2\times2\text{ determinants).}$$
> $$=-a_{12}a_{34}^{2}-a_{23}a_{14}a_{34}+a_{24}a_{13}a_{34}=-a_{34}\big(a_{12}a_{34}+a_{14}a_{23}-a_{13}a_{24}\big)=-a_{34}\,w\qquad\text{(factor out }-a_{34}\text{; the bracket is }w\text{).}$$
>
> **Minor $M_{13}$** (delete row $1$, column $3$): rows $2,3,4$, columns $1,2,4$,
> $$M_{13}=\det\begin{pmatrix}-a_{12}&0&a_{24}\\-a_{13}&-a_{23}&a_{34}\\-a_{14}&-a_{24}&0\end{pmatrix}.$$
> Expanding along its first row,
> $$M_{13}=-a_{12}\det\begin{pmatrix}-a_{23}&a_{34}\\-a_{24}&0\end{pmatrix}-0+a_{24}\det\begin{pmatrix}-a_{13}&-a_{23}\\-a_{14}&-a_{24}\end{pmatrix}\qquad\text{(the middle entry is }0\text{).}$$
> $$=-a_{12}\big(0-a_{34}(-a_{24})\big)+a_{24}\big((-a_{13})(-a_{24})-(-a_{23})(-a_{14})\big)\qquad\text{(evaluating the two }2\times2\text{ determinants).}$$
> $$=-a_{12}a_{34}a_{24}+a_{24}\big(a_{13}a_{24}-a_{14}a_{23}\big)=-a_{24}\big(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}\big)=-a_{24}\,w\qquad\text{(factor out }-a_{24}\text{; the bracket is }w\text{).}$$
>
> **Minor $M_{14}$** (delete row $1$, column $4$): rows $2,3,4$, columns $1,2,3$,
> $$M_{14}=\det\begin{pmatrix}-a_{12}&0&a_{23}\\-a_{13}&-a_{23}&0\\-a_{14}&-a_{24}&-a_{34}\end{pmatrix}.$$
> Expanding along its first row,
> $$M_{14}=-a_{12}\det\begin{pmatrix}-a_{23}&0\\-a_{24}&-a_{34}\end{pmatrix}-0+a_{23}\det\begin{pmatrix}-a_{13}&-a_{23}\\-a_{14}&-a_{24}\end{pmatrix}\qquad\text{(the middle entry is }0\text{).}$$
> $$=-a_{12}\big((-a_{23})(-a_{34})-0\big)+a_{23}\big((-a_{13})(-a_{24})-(-a_{23})(-a_{14})\big)\qquad\text{(evaluating the two }2\times2\text{ determinants).}$$
> $$=-a_{12}a_{23}a_{34}+a_{23}\big(a_{13}a_{24}-a_{14}a_{23}\big)=-a_{23}\big(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}\big)=-a_{23}\,w\qquad\text{(factor out }-a_{23}\text{; the bracket is }w\text{).}$$

**Step 6: Recombine and conclude $\det A=\operatorname{Pf}(A)^{2}$.**

Substituting the three minors into the first-row expansion collapses everything to $w^{2}$.

> [!note]- Derivation
> From Step 4, $\det A=-a_{12}M_{12}+a_{13}M_{13}-a_{14}M_{14}$. Substituting the values $M_{12}=-a_{34}w$, $M_{13}=-a_{24}w$, $M_{14}=-a_{23}w$ from Step 5,
> $$\det A=-a_{12}(-a_{34}w)+a_{13}(-a_{24}w)-a_{14}(-a_{23}w)\qquad\text{(substituting the three minors).}$$
> $$=\big(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}\big)\,w=w\cdot w=w^{2}\qquad\text{(the coefficient of }w\text{ is again }w\text{).}$$
> Since $w=\operatorname{Pf}(A)$ by part (a), this is exactly $\det A=\operatorname{Pf}(A)^{2}$, proving part (b).

> [!note]- Complete formal solution
> **Claim.** For the general skew-symmetric $A\in\mathfrak{so}(4)$, $\operatorname{Pf}(A)=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}$ and $\operatorname{Pf}(A)^{2}=\det A$.
>
> *Part (a).* Set $\sigma_{A}=\sum_{i<j}a_{ij}\,e_{i}\wedge e_{j}\in\Lambda^{2}\mathbb{R}^{4}$. In $\sigma_{A}\wedge\sigma_{A}$ only terms using all four indices survive (a repeated index kills a term, since $e_{p}\wedge e_{p}=0$), and the two orderings of each disjoint index split coincide (two $2$-forms commute), so
> $$\sigma_{A}\wedge\sigma_{A}=2a_{12}a_{34}\,e_{12}\wedge e_{34}+2a_{13}a_{24}\,e_{13}\wedge e_{24}+2a_{14}a_{23}\,e_{14}\wedge e_{23}.$$
> Reordering to $E=e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}$ gives $e_{12}\wedge e_{34}=+E$, $e_{13}\wedge e_{24}=-E$, $e_{14}\wedge e_{23}=+E$, hence $\sigma_{A}\wedge\sigma_{A}=2(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23})E$. By $\tfrac12\sigma_{A}^{\wedge2}=\operatorname{Pf}(A)\,E$, we conclude $\operatorname{Pf}(A)=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}=:w$.
>
> *Part (b).* Cofactor expansion of $\det A$ along the first row (using $A_{11}=0$ and cofactor signs $(-1)^{1+j}$) gives $\det A=-a_{12}M_{12}+a_{13}M_{13}-a_{14}M_{14}$. Direct evaluation of the three $3\times3$ minors, with sub-diagonal entries rewritten by skew-symmetry as $A_{ji}=-a_{ij}$, yields
> $$M_{12}=-a_{34}\,w,\qquad M_{13}=-a_{24}\,w,\qquad M_{14}=-a_{23}\,w.$$
> Substituting,
> $$\det A=-a_{12}(-a_{34}w)+a_{13}(-a_{24}w)-a_{14}(-a_{23}w)=(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23})\,w=w^{2}=\operatorname{Pf}(A)^{2}.$$
> Therefore $\operatorname{Pf}(A)^{2}=\det A$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One is tempted to "prove" $\operatorname{Pf}(A)^{2}=\det A$ in general by writing $\det A=\det(A^{t})=\det(-A)=(-1)^{2m}\det A=\det A$ and concluding something about a square root — but $\det A=\det(-A)$ only says $\det A$ is unchanged under $A\mapsto-A$, which is automatic in even size and gives no information about a factorisation. Worse, the naive guess "$\operatorname{Pf}(A)=\sqrt{\det A}$ as functions" is false as an *identity of polynomials* without the sign structure: $\det A$ is a perfect square *of the specific polynomial* $\operatorname{Pf}(A)$, and it is the exterior computation (or the reduction to block-diagonal form used on [[Thm - Properties of the Pfaffian]]) that produces the correct sign pattern $+,-,+$. The genuine content is the polynomial identity, entry by entry, which is what the expansion above establishes; a determinant-of-transpose argument establishes nothing here.

---

# Key Takeaways

**The Pfaffian is a polynomial square root of the determinant, and the $\Lambda^{2}$ picture is what makes this visible.** The identity $\operatorname{Pf}(A)^{2}=\det A$ is not a numerical coincidence at $4\times4$; it holds on all of $\mathfrak{so}(2m)$ and is the reason the Euler class of an oriented rank-$2m$ bundle is a genuine degree-$2m$ class rather than the square root of the top Pontryagin class taken formally. The mechanism seen here — encode the skew matrix as $\sigma_{A}\in\Lambda^{2}\mathbb{R}^{2m}$, and read the Pfaffian as the coefficient of $\tfrac{1}{m!}\sigma_{A}^{\wedge m}$ against the volume element — is the operational heart of the whole story: it converts a permutation sum into a wedge power, where associativity and graded-commutativity do the bookkeeping automatically. Whenever a computation with $\operatorname{Pf}$ threatens to become a sum over $S_{2m}$, the reflex should be to pass to $\Lambda^{2}$ instead. The general identity, proved by reducing an arbitrary skew matrix to block-diagonal normal form and using multiplicativity, lives on [[Thm - Properties of the Pfaffian]]; the present hand computation is the $m=2$ instance that anchors the intuition.

**Factor before you multiply out.** The single most useful habit in part (b) is refusing to expand $\det A$ into its full thirty-six-term polynomial. Instead, each $3\times3$ minor was simplified *first*, and each turned out to be a single entry times the Pfaffian $w$. Recognising a common factor at the level of the minors — rather than at the very end, after a page of algebra — is what collapses the computation to three lines. This is a transferable diagnostic: when a determinant is expected to be a perfect square (as it always is for a skew matrix of even size), expand one step, look for the square root appearing as a factor of every cofactor, and pull it out immediately. The same discipline recurs in computing resultants, discriminants, and Gram determinants, where the answer is known in advance to have a factored form and brute expansion obscures it.

**Skew-symmetry is a bookkeeping hypothesis that must be spent deliberately.** The hypothesis $A^{t}=-A$ was used in exactly two roles: it set the diagonal entries to zero (so the first-row expansion loses its $j=1$ term) and it rewrote every sub-diagonal entry $A_{ji}=-a_{ij}$ inside the minors. Every sign in the final answer descends from one of these two uses. When a problem hands a structural hypothesis on a matrix — skew, symmetric, orthogonal, nilpotent — the reliable move is to write out where that hypothesis enters each entry *before* computing, so that the later algebra carries the constraint automatically rather than as an afterthought. A single mishandled $A_{ji}=-a_{ij}$ turns the clean identity $\operatorname{Pf}^{2}=\det$ into an unrecognisable mess, which is precisely why this one-star drill is worth doing by hand once: it fixes the sign discipline that the Euler-class computation in [[Ex - The Euler Class of the Tangent Bundle of the Round Sphere Integrates to Two]] then relies on.

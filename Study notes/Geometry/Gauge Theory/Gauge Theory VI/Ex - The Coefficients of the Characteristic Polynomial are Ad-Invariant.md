---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Ad-Invariant Polynomial"
  - "Thm - Determinant is Multiplicative"
  - "Def - Determinant"
  - "Def - Trace"
tags: [geometry, gauge-theory]
---

# Problem Statement

Fix an integer $r\ge1$ and work on the Lie algebra $\mathfrak{gl}_r(\mathbb{C})$ of all complex $r\times r$ matrices, with the unitary Lie algebra $\mathfrak{u}(r)=\{\xi\in\mathfrak{gl}_r(\mathbb{C}):\xi^*=-\xi\}$ of skew-Hermitian matrices sitting inside it. For $\xi\in\mathfrak{gl}_r(\mathbb{C})$ define the **coefficients of the (normalised) characteristic polynomial** $c_1(\xi),\dots,c_r(\xi)\in\mathbb{C}$ by expanding a determinant in the formal variable $\lambda$:
$$\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)=\lambda^{r}+c_1(\xi)\,\lambda^{r-1}+c_2(\xi)\,\lambda^{r-2}+\dots+c_r(\xi),$$
where $\mathbf{1}$ is the $r\times r$ identity matrix and $\tfrac{i}{2\pi}$ is the standing Chern-class normalisation of the series (the convention $c(E)=\det(1+\tfrac{i}{2\pi}F)$). Prove the following.

1. **Conjugation invariance.** Each $c_j$ is invariant under the adjoint action of $U(r)$: $c_j(\operatorname{Ad}_g\xi)=c_j(\xi)$ for every $g\in U(r)$ and every $\xi$. (In fact the argument gives invariance under all of $GL_r(\mathbb{C})$.)
2. **Homogeneity.** Each $c_j$ is a homogeneous polynomial of degree $j$ in the entries of $\xi$, so that $c_j$ is an $\operatorname{Ad}$-invariant homogeneous polynomial of degree $j$, an element of $I^{j}(U(r))$.
3. **Reality on $\mathfrak{u}(r)$.** For skew-Hermitian $\xi\in\mathfrak{u}(r)$ each value $c_j(\xi)$ is a real number; the mechanism is the conjugation identity
$$\overline{\det\!\Big(\bar\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)}=\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)\qquad(\xi\in\mathfrak{u}(r)).$$
4. **The rank-two case.** For $r=2$ compute $c_1$ and $c_2$ explicitly, obtaining $c_1(\xi)=\tfrac{i}{2\pi}\operatorname{tr}\xi$ and $c_2(\xi)=-\tfrac{1}{4\pi^{2}}\det\xi$; then specialise to $\mathfrak{su}(2)$ (traceless skew-Hermitian matrices) to show $c_1=0$ and
$$c_2(\xi)=\frac{1}{8\pi^{2}}\operatorname{tr}\big(\xi^{2}\big)\qquad(\xi\in\mathfrak{su}(2)),$$
using the identity $\operatorname{tr}(\xi^{2})=-2\det\xi$ valid for every traceless $2\times2$ matrix.

**Recall:**

The objects in play are the ring of $\operatorname{Ad}$-invariant homogeneous polynomials on a matrix Lie algebra, the determinant and its multiplicativity, and the trace. The full definition, with its three defining conditions, is the following.

![[Def - Ad-Invariant Polynomial#The Definition]]

Concretely, a function $p\colon\mathfrak{g}\to\mathbb{K}$ (here $\mathfrak{g}=\mathfrak{gl}_r(\mathbb{C})$ or $\mathfrak{u}(r)$, and $\mathbb{K}=\mathbb{C}$ or $\mathbb{R}$) is an **[[Def - Ad-Invariant Polynomial|Ad-invariant homogeneous polynomial]]** of degree $d$ when (1) it is a homogeneous polynomial of degree $d$ in the matrix entries, (2) $p(\operatorname{Ad}_g\xi)=p(\xi)$ for all $g\in G$, and (3) $p(\lambda\xi)=\lambda^{d}p(\xi)$; for a matrix group $\operatorname{Ad}_g\xi=g\xi g^{-1}$ is conjugation. Conditions (2) and (3) are the two we must verify here; condition (1) is visible from the determinant expansion.

![[Thm - Determinant is Multiplicative#Statement]]

We use the [[Thm - Determinant is Multiplicative|multiplicativity of the determinant]] in the form $\det(AB)=\det(A)\det(B)$ and its immediate consequence $\det(gMg^{-1})=\det(M)$: the determinant is unchanged by conjugation, because $\det(gMg^{-1})=\det(g)\det(M)\det(g)^{-1}=\det(M)$.

![[Def - Trace#The Definition]]

The [[Def - Trace|trace]] $\operatorname{tr}\xi=\sum_{k}\xi_{kk}$ is the sum of the diagonal entries; it is linear and cyclic, $\operatorname{tr}(AB)=\operatorname{tr}(BA)$, whence $\operatorname{tr}(g\xi g^{-1})=\operatorname{tr}\xi$. The [[Def - Determinant|determinant]] of a $2\times2$ matrix is $\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$, and for a $2\times2$ matrix $\det(\lambda\mathbf{1}+M)=\lambda^{2}+(\operatorname{tr}M)\lambda+\det M$; both are used in Part 4.

---

# Convergent Strategy

**Problem class.** This is a *verify-the-axioms* problem attached to a *concrete computation*: we are handed a candidate family of invariant polynomials — the coefficients of a characteristic polynomial — and asked to confirm that they satisfy the two non-trivial defining conditions (invariance and homogeneity), that they take real values on the compact form, and finally to evaluate them in the smallest rank where the answer is used downstream. The verification half is routine once the right identity is named; the payoff is that Parts 1–3 certify that $c_1,\dots,c_r$ are legitimate inputs to the Chern–Weil homomorphism, and Part 4 produces the exact formula $c_2=\tfrac{1}{8\pi^2}\operatorname{tr}\xi^2$ that the second Chern number of an $SU(2)$-bundle is built from.

**Assumption pattern.** Every part is driven by a single structural fact: the characteristic polynomial is a *conjugation-invariant* object because the determinant is. The recognisable trigger is that the quantity to be studied is packaged inside a determinant of $(\lambda\mathbf{1}+\text{something linear in }\xi)$; whenever an invariant is presented this way, conjugation invariance is immediate from multiplicativity of $\det$, and homogeneity is read off by scaling $\lambda$ and $\xi$ together. The reality assertion is a separate mechanism: it uses that skew-Hermitian matrices are exactly those for which complex conjugation of entries equals negative transpose.

**Theorem routing.** Part 1 routes through [[Thm - Determinant is Multiplicative]]: substitute $\operatorname{Ad}_g\xi=g\xi g^{-1}$, pull the conjugation outside the determinant, and equate coefficients of the resulting polynomial identity in $\lambda$. Part 2 routes through a *scaling substitution* $\lambda\mapsto\lambda/s$, $\xi\mapsto s\xi$, again followed by matching coefficients of $\lambda$. Part 3 routes through the entrywise-conjugation identity $\overline{\det M}=\det\bar M$ together with $\det M^{\mathsf T}=\det M$ and the skew-Hermitian relation $\bar\xi=-\xi^{\mathsf T}$. Part 4 routes through the elementary $2\times2$ expansion of $\det(\lambda\mathbf{1}+M)$ and the traceless identity $\operatorname{tr}\xi^2=-2\det\xi$, itself an entrywise computation.

**Key decision point.** The one genuinely load-bearing choice is to treat the defining equation as an *identity of polynomials in $\lambda$* and to extract each $c_j$ as the coefficient of $\lambda^{r-j}$. Once invariance (or a scaling relation) is established for the whole determinant, "equate the coefficient of $\lambda^{r-j}$ on both sides" delivers the corresponding statement about $c_j$ for free, all $j$ at once. The second decision, in Part 4, is to prove $\operatorname{tr}\xi^2=-2\det\xi$ by the entry identity $(\operatorname{tr}\xi)^2-\operatorname{tr}(\xi^2)=2\det\xi$ rather than by invoking a general Cayley–Hamilton theorem, keeping the argument self-contained and elementary.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional#Legal Operations|the topic page's Legal Operations]]; where the topic page is not yet assembled the operations are named descriptively and the numbering will be reconciled.

1. **Present an invariant as a determinant and conjugate inside it.** Recognising $c_j$ as coefficients of $\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)$, and using $\det(gMg^{-1})=\det M$ (multiplicativity of the determinant, applied with $M=\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi$ and $\lambda\mathbf{1}=g(\lambda\mathbf{1})g^{-1}$), turns conjugation invariance of the whole polynomial into invariance of each coefficient.

2. **Equate coefficients of a polynomial identity in an auxiliary variable.** From an equality of two polynomials in $\lambda$, read off equality of the coefficients of each power $\lambda^{r-j}$; this extracts a statement about the single invariant $c_j$ from a statement about the packaged determinant.

3. **Detect homogeneity by a joint scaling substitution.** Replacing $\lambda$ by $\lambda/s$ and clearing $s^{r}$ converts the definition of $c_j(s\xi)$ into $s^{j}c_j(\xi)$, exhibiting the degree of homogeneity directly.

4. **Prove reality by the conjugation symmetry of the skew-Hermitian form.** Use $\overline{\det M}=\det\bar M$, $\det M^{\mathsf T}=\det M$, and $\bar\xi=-\xi^{\mathsf T}$ (the defining relation of $\mathfrak{u}(r)$) to show the characteristic polynomial has real coefficients.

5. **Reduce a low-rank determinant to trace and determinant data.** For $r=2$ use $\det(\lambda\mathbf{1}+M)=\lambda^{2}+(\operatorname{tr}M)\lambda+\det M$ to name $c_1,c_2$, and the traceless identity $\operatorname{tr}\xi^2=-2\det\xi$ to rewrite $c_2$ in the form used by the second Chern number.

---

# Hints

> [!note]- Hint 1
> Do not try to write down $c_j$ as an explicit polynomial in the entries and then check invariance term by term. Instead, keep the coefficients packaged inside the determinant $\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)$ and study *the whole polynomial in $\lambda$ at once*. What happens to a determinant when its argument is conjugated by an invertible matrix?

> [!note]- Hint 2
> For invariance: $\operatorname{Ad}_g\xi=g\xi g^{-1}$, and $\lambda\mathbf{1}=g(\lambda\mathbf{1})g^{-1}$, so $\lambda\mathbf{1}+\tfrac{i}{2\pi}\operatorname{Ad}_g\xi=g\big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\big)g^{-1}$. Take determinants. Then two polynomials in $\lambda$ agree for all $\lambda$; compare the coefficients of $\lambda^{r-j}$.

> [!note]- Hint 3
> For homogeneity, substitute $s\xi$ for $\xi$ in the definition and then substitute $\lambda=s\mu$; factor $s^{r}$ out of the determinant using $\det(sN)=s^{r}\det N$. Matching the coefficient of $\mu^{r-j}$ on both sides isolates $c_j(s\xi)=s^{j}c_j(\xi)$.

> [!note]- Hint 4
> For reality, remember that $\xi\in\mathfrak{u}(r)$ means $\xi^{*}=\overline{\xi}^{\mathsf T}=-\xi$, equivalently $\overline{\xi}=-\xi^{\mathsf T}$. Combine $\overline{\det M}=\det\overline{M}$ (conjugation is a field automorphism and $\det$ has integer-coefficient entries) with $\det M^{\mathsf T}=\det M$. Track where the bar on $\lambda$ goes.

> [!note]- Hint 5
> For the rank-two computation, expand $\det\begin{pmatrix}\lambda+\tfrac{i}{2\pi}\xi_{11} & \tfrac{i}{2\pi}\xi_{12}\\ \tfrac{i}{2\pi}\xi_{21} & \lambda+\tfrac{i}{2\pi}\xi_{22}\end{pmatrix}$ directly. For the traceless identity write $\xi=\begin{pmatrix}a&b\\c&-a\end{pmatrix}$ and compute both $\operatorname{tr}(\xi^{2})$ and $\det\xi$ from the entries.

---

# Solution

The plan is uniform across the first three parts: package the coefficients inside the determinant $\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)$, establish the desired property (invariance, a scaling law, reality) for the whole polynomial by a one-line determinant manipulation, and then read off the property of each $c_j$ by comparing coefficients of $\lambda$. The fourth part is a direct $2\times2$ computation that ends at the formula $c_2=\tfrac{1}{8\pi^2}\operatorname{tr}\xi^2$ on $\mathfrak{su}(2)$.

**Step 1: Conjugation invariance of every coefficient.**

Conjugating $\xi$ conjugates the matrix $\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi$, and the determinant does not see conjugation; equating coefficients of $\lambda$ gives $c_j(\operatorname{Ad}_g\xi)=c_j(\xi)$ for all $j$.

> [!note]- Derivation
> Fix $g\in U(r)$ (the argument uses only $g\in GL_r(\mathbb{C})$) and $\xi\in\mathfrak{gl}_r(\mathbb{C})$. Since $\operatorname{Ad}_g\xi=g\xi g^{-1}$ for a matrix group and $\lambda\mathbf{1}=g(\lambda\mathbf{1})g^{-1}$ (scalars commute with $g$), we may factor the conjugation out of the whole matrix:
> $$\lambda\mathbf{1}+\tfrac{i}{2\pi}\operatorname{Ad}_g\xi=\lambda\mathbf{1}+\tfrac{i}{2\pi}\,g\xi g^{-1}=g\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)g^{-1}\qquad\text{(scalars commute with }g\text{; }\operatorname{Ad}_g\text{ is conjugation).}$$
> Taking determinants and using [[Thm - Determinant is Multiplicative|multiplicativity of the determinant]], $\det(gMg^{-1})=\det(g)\det(M)\det(g)^{-1}=\det(M)$:
> $$\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\operatorname{Ad}_g\xi\Big)=\det\!\Big(g\big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\big)g^{-1}\Big)=\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)\qquad\text{(conjugation invariance of }\det\text{).}$$
> Both sides are polynomials in $\lambda$. Expanding each by the definition of the $c_j$,
> $$\lambda^{r}+\sum_{j=1}^{r}c_j(\operatorname{Ad}_g\xi)\,\lambda^{r-j}=\lambda^{r}+\sum_{j=1}^{r}c_j(\xi)\,\lambda^{r-j}\qquad\text{for all }\lambda.$$
> Two polynomials that agree for all $\lambda$ have equal coefficients, so equating the coefficient of $\lambda^{r-j}$ for each $j\in\{1,\dots,r\}$ gives
> $$c_j(\operatorname{Ad}_g\xi)=c_j(\xi)\qquad(1\le j\le r).$$
> This is condition (2) of the definition of an $\operatorname{Ad}$-invariant polynomial, verified for every $c_j$ and every $g\in U(r)$.

**Step 2: Homogeneity of degree $j$.**

A joint rescaling of $\lambda$ and $\xi$ shows $c_j(s\xi)=s^{j}c_j(\xi)$, so $c_j$ is homogeneous of degree $j$; being also polynomial and invariant, $c_j\in I^{j}(U(r))$.

> [!note]- Derivation
> First, $c_j$ is a polynomial in the entries of $\xi$: expanding the determinant $\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)$ by the Leibniz formula produces a polynomial in $\lambda$ whose coefficients are polynomials in the entries $\xi_{k\ell}$, and $c_j$ is by definition the coefficient of $\lambda^{r-j}$. This gives condition (1).
>
> For the degree, fix a nonzero scalar $s\in\mathbb{C}$ and substitute $s\xi$ for $\xi$ in the defining identity, then substitute $\lambda=s\mu$ and pull the scalar $s$ out of every one of the $r$ rows of the matrix (so a factor $s^{r}$ appears, by $\det(sN)=s^{r}\det N$):
> $$\det\!\Big(s\mu\,\mathbf{1}+\tfrac{i}{2\pi}s\xi\Big)=\det\!\Big(s\big(\mu\mathbf{1}+\tfrac{i}{2\pi}\xi\big)\Big)=s^{r}\det\!\Big(\mu\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)=s^{r}\Big(\mu^{r}+\sum_{j}c_j(\xi)\mu^{r-j}\Big).$$
> On the other hand, applying the definition of the coefficients to the matrix $s\xi$ at the value $\lambda=s\mu$,
> $$\det\!\Big(s\mu\,\mathbf{1}+\tfrac{i}{2\pi}s\xi\Big)=(s\mu)^{r}+\sum_{j}c_j(s\xi)\,(s\mu)^{r-j}=s^{r}\mu^{r}+\sum_{j}c_j(s\xi)\,s^{r-j}\mu^{r-j}.$$
> Equating these two expressions and cancelling the common factor $s^{r}$ (legitimate since $s\ne0$),
> $$\mu^{r}+\sum_{j}c_j(\xi)\,\mu^{r-j}=\mu^{r}+\sum_{j}c_j(s\xi)\,s^{-j}\mu^{r-j}\qquad\text{for all }\mu.$$
> Comparing the coefficient of $\mu^{r-j}$ gives $c_j(\xi)=s^{-j}c_j(s\xi)$, that is
> $$c_j(s\xi)=s^{j}\,c_j(\xi)\qquad(s\ne0).$$
> Both sides are polynomials in $s$ (the left side because $c_j$ is polynomial in the entries of $s\xi$, which are linear in $s$), and they agree for all $s\ne0$, hence for $s=0$ as well by continuity of polynomials. So $c_j(s\xi)=s^{j}c_j(\xi)$ for every $s\in\mathbb{C}$, which is condition (3) with $d=j$. Together with Steps 1–2, each $c_j$ is an $\operatorname{Ad}$-invariant homogeneous polynomial of degree $j$, i.e. $c_j\in I^{j}(U(r))$.

**Step 3: Reality on $\mathfrak{u}(r)$.**

For skew-Hermitian $\xi$ the characteristic polynomial equals its own conjugate, so its coefficients are real.

> [!note]- Derivation
> Let $\xi\in\mathfrak{u}(r)$, so $\xi^{*}=\overline{\xi}^{\mathsf T}=-\xi$; equivalently $\overline{\xi}=-\xi^{\mathsf T}$. Take an arbitrary $\lambda\in\mathbb{C}$ and compute the conjugate of $\det(\bar\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)$ by moving the bar through the determinant and simplifying:
> $$\overline{\det\!\Big(\bar\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)}=\det\!\Big(\overline{\bar\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi}\Big)=\det\!\Big(\lambda\mathbf{1}-\tfrac{i}{2\pi}\overline{\xi}\Big)\qquad\text{(}\overline{\det M}=\det\overline{M}\text{; }\overline{\bar\lambda}=\lambda\text{; }\overline{\tfrac{i}{2\pi}}=-\tfrac{i}{2\pi}\text{),}$$
> where $\overline{\det M}=\det\overline{M}$ because the determinant is a polynomial in the entries with integer coefficients and complex conjugation is a ring automorphism fixing $\mathbb{Z}$. Now use $\overline{\xi}=-\xi^{\mathsf T}$ and then $\det M^{\mathsf T}=\det M$:
> $$\det\!\Big(\lambda\mathbf{1}-\tfrac{i}{2\pi}\overline{\xi}\Big)=\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi^{\mathsf T}\Big)=\det\!\Big(\big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\big)^{\mathsf T}\Big)=\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big),$$
> using $\mathbf{1}^{\mathsf T}=\mathbf{1}$ and $(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)^{\mathsf T}=\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi^{\mathsf T}$. Chaining the two displays yields the announced identity
> $$\overline{\det\!\Big(\bar\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)}=\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)\qquad(\xi\in\mathfrak{u}(r)).$$
> Expand both sides as polynomials in $\lambda$. The right side is $\lambda^{r}+\sum_{j}c_j(\xi)\lambda^{r-j}$. On the left, write $\det(\bar\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)=\bar\lambda^{r}+\sum_{j}c_j(\xi)\bar\lambda^{r-j}$ and conjugate the whole expression:
> $$\overline{\bar\lambda^{r}+\sum_{j}c_j(\xi)\bar\lambda^{r-j}}=\lambda^{r}+\sum_{j}\overline{c_j(\xi)}\,\lambda^{r-j}\qquad\text{(}\overline{\bar\lambda^{k}}=\lambda^{k}\text{, }\overline{c_j\bar\lambda^{r-j}}=\overline{c_j}\,\lambda^{r-j}\text{).}$$
> Equating the two forms of the left side to the right side and comparing the coefficient of $\lambda^{r-j}$ gives $\overline{c_j(\xi)}=c_j(\xi)$, hence $c_j(\xi)\in\mathbb{R}$ for every $j$ and every $\xi\in\mathfrak{u}(r)$. So the $c_j$ are real-valued $\operatorname{Ad}$-invariant polynomials on $\mathfrak{u}(r)$, exactly the invariants whose Chern–Weil forms are the [[Def - Chern Classes|Chern classes]].

**Step 4: The rank-two case and the reduction to $\operatorname{tr}\xi^{2}$.**

For $r=2$ the determinant expands to $c_1=\tfrac{i}{2\pi}\operatorname{tr}\xi$ and $c_2=-\tfrac{1}{4\pi^2}\det\xi$; on $\mathfrak{su}(2)$ the trace vanishes and $\det\xi=-\tfrac12\operatorname{tr}\xi^2$, giving $c_2=\tfrac{1}{8\pi^2}\operatorname{tr}\xi^2$.

> [!note]- Derivation
> Set $r=2$ and abbreviate $M:=\tfrac{i}{2\pi}\xi$. For a $2\times2$ matrix $M=\begin{pmatrix}m_{11}&m_{12}\\m_{21}&m_{22}\end{pmatrix}$, the direct expansion of the determinant gives
> $$\det(\lambda\mathbf{1}+M)=(\lambda+m_{11})(\lambda+m_{22})-m_{12}m_{21}=\lambda^{2}+(m_{11}+m_{22})\lambda+(m_{11}m_{22}-m_{12}m_{21})=\lambda^{2}+(\operatorname{tr}M)\lambda+\det M.$$
> Comparing with $\det(\lambda\mathbf{1}+M)=\lambda^{2}+c_1(\xi)\lambda+c_2(\xi)$ and substituting $M=\tfrac{i}{2\pi}\xi$,
> $$c_1(\xi)=\operatorname{tr}M=\operatorname{tr}\!\Big(\tfrac{i}{2\pi}\xi\Big)=\tfrac{i}{2\pi}\operatorname{tr}\xi\qquad\text{(linearity of the trace),}$$
> $$c_2(\xi)=\det M=\det\!\Big(\tfrac{i}{2\pi}\xi\Big)=\Big(\tfrac{i}{2\pi}\Big)^{2}\det\xi=-\tfrac{1}{4\pi^{2}}\det\xi\qquad\text{(}\det(sN)=s^{2}\det N\text{ for }2\times2\text{, }i^{2}=-1\text{).}$$
> Now specialise to $\xi\in\mathfrak{su}(2)$, the traceless skew-Hermitian $2\times2$ matrices. Tracelessness gives at once
> $$c_1(\xi)=\tfrac{i}{2\pi}\operatorname{tr}\xi=0.$$
> For $c_2$ we prove the identity $\operatorname{tr}(\xi^{2})=-2\det\xi$, valid for **any** traceless $2\times2$ matrix. Write a general traceless matrix as $\xi=\begin{pmatrix}a&b\\c&-a\end{pmatrix}$ with $a,b,c\in\mathbb{C}$ (the lower-right entry is $-a$ so that $\operatorname{tr}\xi=0$). Then
> $$\xi^{2}=\begin{pmatrix}a&b\\c&-a\end{pmatrix}\begin{pmatrix}a&b\\c&-a\end{pmatrix}=\begin{pmatrix}a^{2}+bc & ab-ba\\ ca-ac & cb+a^{2}\end{pmatrix}=\begin{pmatrix}a^{2}+bc & 0\\ 0 & a^{2}+bc\end{pmatrix},$$
> so $\operatorname{tr}(\xi^{2})=2(a^{2}+bc)$; while $\det\xi=a\cdot(-a)-bc=-(a^{2}+bc)$. Comparing,
> $$\operatorname{tr}(\xi^{2})=2(a^{2}+bc)=-2\det\xi.$$
> (Equivalently, for every $2\times2$ matrix $(\operatorname{tr}\xi)^{2}-\operatorname{tr}(\xi^{2})=2\det\xi$; setting $\operatorname{tr}\xi=0$ recovers the identity.) Substituting $\det\xi=-\tfrac12\operatorname{tr}(\xi^{2})$ into the formula for $c_2$,
> $$c_2(\xi)=-\tfrac{1}{4\pi^{2}}\det\xi=-\tfrac{1}{4\pi^{2}}\Big(-\tfrac12\operatorname{tr}(\xi^{2})\Big)=\frac{1}{8\pi^{2}}\operatorname{tr}(\xi^{2})\qquad(\xi\in\mathfrak{su}(2)),$$
> which is the required formula. This is exactly the polynomial whose Chern–Weil form gives $c_2(P)=\tfrac{1}{8\pi^2}[\operatorname{tr}(F_A\wedge F_A)]$ for an $SU(2)$-bundle, matching Haydys's equation $(94)$.

> [!note]- Complete formal solution
> **Claim.** With $c_1,\dots,c_r$ defined by $\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)=\lambda^{r}+\sum_{j=1}^{r}c_j(\xi)\lambda^{r-j}$ on $\mathfrak{gl}_r(\mathbb{C})$: each $c_j$ is an $\operatorname{Ad}$-invariant homogeneous polynomial of degree $j$, real-valued on $\mathfrak{u}(r)$; and for $r=2$, $c_1(\xi)=\tfrac{i}{2\pi}\operatorname{tr}\xi$ and $c_2(\xi)=-\tfrac{1}{4\pi^2}\det\xi$, so that $c_1=0$ and $c_2(\xi)=\tfrac{1}{8\pi^2}\operatorname{tr}(\xi^{2})$ on $\mathfrak{su}(2)$.
>
> *Polynomiality.* Expanding $\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)$ by the Leibniz formula gives a polynomial in $\lambda$ whose coefficient of $\lambda^{r-j}$, namely $c_j(\xi)$, is a polynomial in the entries $\xi_{k\ell}$.
>
> *Invariance.* For $g\in GL_r(\mathbb{C})$, $\lambda\mathbf{1}+\tfrac{i}{2\pi}g\xi g^{-1}=g(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)g^{-1}$, so by multiplicativity of the determinant $\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\operatorname{Ad}_g\xi)=\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)$. Equating coefficients of $\lambda^{r-j}$ yields $c_j(\operatorname{Ad}_g\xi)=c_j(\xi)$; in particular this holds for $g\in U(r)$.
>
> *Homogeneity.* For $s\ne0$, $\det(s\mu\mathbf{1}+\tfrac{i}{2\pi}s\xi)=s^{r}\det(\mu\mathbf{1}+\tfrac{i}{2\pi}\xi)$; expanding both sides in $\mu$ and matching the coefficient of $\mu^{r-j}$ gives $c_j(s\xi)s^{r-j}=s^{r}c_j(\xi)$, i.e. $c_j(s\xi)=s^{j}c_j(\xi)$, extended to $s=0$ by polynomiality. Hence $c_j\in I^{j}(U(r))$.
>
> *Reality.* For $\xi\in\mathfrak{u}(r)$, $\overline{\xi}=-\xi^{\mathsf T}$, so $\overline{\det(\bar\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)}=\det(\lambda\mathbf{1}-\tfrac{i}{2\pi}\overline{\xi})=\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi^{\mathsf T})=\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)$, using $\overline{\det M}=\det\overline{M}$, $\overline{i/2\pi}=-i/2\pi$, and $\det M^{\mathsf T}=\det M$. Matching coefficients of $\lambda^{r-j}$ gives $\overline{c_j(\xi)}=c_j(\xi)$, so $c_j(\xi)\in\mathbb{R}$.
>
> *Rank two.* For $2\times2$ matrices $\det(\lambda\mathbf{1}+M)=\lambda^{2}+(\operatorname{tr}M)\lambda+\det M$; with $M=\tfrac{i}{2\pi}\xi$ this gives $c_1(\xi)=\tfrac{i}{2\pi}\operatorname{tr}\xi$ and $c_2(\xi)=-\tfrac{1}{4\pi^2}\det\xi$. For traceless $\xi=\begin{pmatrix}a&b\\c&-a\end{pmatrix}$, $\xi^{2}=(a^{2}+bc)\mathbf{1}$ so $\operatorname{tr}(\xi^{2})=2(a^{2}+bc)=-2\det\xi$; hence on $\mathfrak{su}(2)$, $c_1=0$ and $c_2(\xi)=-\tfrac{1}{4\pi^2}\det\xi=\tfrac{1}{8\pi^2}\operatorname{tr}(\xi^{2})$. $\blacksquare$

> [!warning] Illegal but tempting: reading reality off "eigenvalues of a skew-Hermitian matrix are imaginary"
> One is tempted to argue that $\xi\in\mathfrak{u}(r)$ has purely imaginary eigenvalues $i\theta_k$ ($\theta_k\in\mathbb{R}$), so $\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)=\prod_k(\lambda+\tfrac{i}{2\pi}\,i\theta_k)=\prod_k(\lambda-\tfrac{\theta_k}{2\pi})$ has manifestly real coefficients, and stop there. This is correct but relies on the spectral theorem for normal matrices (that a skew-Hermitian matrix is unitarily diagonalisable with imaginary eigenvalues), which is a genuine input; the conjugation identity of Part 3 proves reality with nothing but $\overline{\det M}=\det\overline{M}$, $\det M^{\mathsf T}=\det M$, and the definition of $\mathfrak{u}(r)$, and is the argument Haydys intends. The spectral route becomes the *legal* one only once the diagonalisability of skew-Hermitian matrices is cited as a proved theorem; we keep the elementary route to stay self-contained.

Independent sanity check: on $\mathfrak{su}(2)$ every $\xi$ has $\det\xi=-(a^{2}+bc)$, and for genuinely skew-Hermitian $\xi=\begin{pmatrix}i\alpha & \beta\\ -\bar\beta & -i\alpha\end{pmatrix}$ (with $\alpha\in\mathbb{R}$, $\beta\in\mathbb{C}$) this is $\det\xi=(i\alpha)(-i\alpha)-\beta(-\bar\beta)=\alpha^{2}+|\beta|^{2}\ge0$. Then $\operatorname{tr}(\xi^{2})=-2\det\xi=-2(\alpha^{2}+|\beta|^{2})\le0$, consistent with $c_2(\xi)=\tfrac{1}{8\pi^2}\operatorname{tr}(\xi^2)\le0$: the sign is exactly the well-known fact that $-\operatorname{tr}(\xi^2)$ is the $\operatorname{Ad}$-invariant inner product on $\mathfrak{su}(2)$, so $\operatorname{tr}(\xi^2)\le0$ pointwise.

---

# Key Takeaways

**When an invariant is packaged inside a determinant, prove everything about it by manipulating the determinant, not the expanded coefficients.** The single most reusable move in this exercise is refusing to expand $c_j$ into an explicit polynomial in the matrix entries. Conjugation invariance, homogeneity, and reality were each established for the whole object $\det(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi)$ in one line — a conjugation absorbed into $\det$, a scalar pulled through $\det$, a bar commuted past $\det$ — and only afterwards were the statements about individual $c_j$ read off by equating coefficients of $\lambda$. The trigger for this pattern is any family of scalars defined as *the coefficients of a polynomial built from a determinant, trace, or Pfaffian of a matrix depending on the variable*: elementary symmetric functions of eigenvalues, Chern coefficients, Pontryagin coefficients, and the Pfaffian all yield to it. The diagnostic is that a property of the packaged polynomial (invariance under a group, a scaling law, a reality condition) transfers coefficient-by-coefficient to the pieces precisely because two polynomials in an auxiliary variable are equal if and only if their coefficients are equal. Carrying the auxiliary variable $\lambda$ is what makes the whole family fall at once instead of one $c_j$ at a time.

**Conjugation invariance of the characteristic polynomial is the algebraic seed of the entire Chern–Weil construction.** The reason the $c_j$ deserve to be studied is that Steps 1–2 certify them as elements of the invariant ring $I(U(r))$, and only elements of that ring can be fed to the [[Thm - Chern-Weil Theorem|Chern–Weil homomorphism]] to produce closed forms that glue across frames. The invariance we proved here is exactly the condition, traced back on the [[Def - Ad-Invariant Polynomial|definition page]], that makes $p(F_A)$ descend from a local frame-dependent expression to a global form on the base; without it the locally defined forms $c_j(F_A)$ would transform by the transition functions and fail to patch. So this modest computation is the point at which the characteristic polynomial is licensed to become a source of characteristic classes. The transferable principle: to show that a spectral quantity of the curvature defines a cohomology class, first show the underlying polynomial is conjugation-invariant on the Lie algebra — that is the whole obstruction, and multiplicativity of the determinant dispatches it for the Chern coefficients.

**Reality on the compact form is a symmetry of the polynomial, not a fact about individual eigenvalues.** It is worth internalising that the coefficients $c_j$ are real on $\mathfrak{u}(r)$ for a structural reason — the characteristic polynomial equals its own complex conjugate — and that this reason is available with only $\overline{\det M}=\det\overline{M}$, $\det M^{\mathsf T}=\det M$, and the defining relation $\overline{\xi}=-\xi^{\mathsf T}$ of skew-Hermitian matrices. The tempting shortcut through "eigenvalues of a skew-Hermitian matrix are imaginary" is true but silently imports the spectral theorem; recognising when an argument secretly leans on diagonalisability, and having the elementary substitute ready, is a discipline that pays off in the many settings where the spectral theorem is either unavailable or is the very thing being built toward. The trigger to reach for the conjugation-symmetry argument is any reality or self-duality claim about a determinant or trace of a structured matrix (Hermitian, skew-Hermitian, real, symplectic): commute the relevant involution — conjugation, transpose, or both — through the determinant and match coefficients.

**The identity $\operatorname{tr}\xi^2=-2\det\xi$ on traceless $2\times2$ matrices is the exact bridge from the abstract $c_2$ to the gauge-theoretic instanton number, and it is worth carrying as a memorised primitive.** Part 4 ends at $c_2(\xi)=\tfrac{1}{8\pi^2}\operatorname{tr}(\xi^2)$ on $\mathfrak{su}(2)$ precisely because $\det$ and $\operatorname{tr}(\cdot^2)$ coincide up to the factor $-2$ in the traceless rank-two setting; this is what converts the determinant-based Chern coefficient into the trace form $\tfrac{1}{8\pi^2}\operatorname{tr}(F_A\wedge F_A)$ that the [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree|second Chern number]] and the Yang–Mills topological bound are written in. The general lesson is that low-rank coincidences between elementary symmetric functions and power sums — here $\sigma_2=-\tfrac12 p_2$ on the traceless locus, a special case of Newton's identities — are the hinges on which explicit characteristic-class formulas turn; when a computation in gauge theory must move between $\det$ and $\operatorname{tr}$ of the curvature, the relevant Newton identity in the relevant rank is almost always the missing step. A companion drill is [[Ex - Polarisation of an Invariant Polynomial]], which recovers the same $c_2=\det$ on $\mathfrak{gl}_2$ from the polarisation viewpoint and exhibits its symmetric bilinear polar form.

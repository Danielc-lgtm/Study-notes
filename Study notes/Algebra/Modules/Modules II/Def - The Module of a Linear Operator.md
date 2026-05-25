---
type: definition
subject: module-theory
prereqs:
  - "Def - Module"
  - "Def - Polynomial Ring"
  - "Def - Euclidean Domain"
  - "Def - Finitely Generated Module"
  - "Def - Quotient Module"
tags: [algebra, module-theory]
---

# Notation

Throughout, $F$ is a field, $V$ is a vector space over $F$, and $\alpha : V \to V$ is a linear map (a linear **operator**, or **endomorphism**, of $V$). The polynomial ring $F[X]$ is the [[Def - Polynomial Ring|ring of polynomials]] in one indeterminate $X$ with coefficients in $F$; for a polynomial $f = \sum_i a_i X^i \in F[X]$ and the operator $\alpha$, the symbol $f(\alpha)$ denotes the operator $\sum_i a_i \alpha^i$ obtained by substituting $\alpha$ for $X$, where $\alpha^i$ is the $i$-fold composite of $\alpha$ and $\alpha^0 = \operatorname{id}_V$. The resulting $F[X]$-module is written $V_\alpha$. A polynomial is **monic** when its leading coefficient is $1$. For a monic $f$, the principal ideal it generates is $(f) = f \cdot F[X]$, and $F[X]/(f)$ is the quotient ring. The symbol $C(f)$ denotes the companion matrix of $f$. The full notation registry lives on the parent page [[Modules II — §3.3–3.4]].

---

# Axiom Motivation

Here is a problem that linear algebra poses but module theory solves. You are given a linear operator $\alpha : V \to V$ on a finite-dimensional vector space, and you want to understand it completely — to find a basis in which its matrix is as simple as possible. The classification problem "given $\alpha$, what does it look like up to change of basis?" is the content of the theory of normal forms: rational canonical form, Jordan normal form. The question is how to *get* these. You could grind through eigenvalue and eigenvector computations, but that is bookkeeping, not insight, and it does not obviously generalise. The deep observation is that the classification of linear operators is *secretly an instance of a classification you have already done* — the structure theory of finitely generated [[Def - Module|modules]] over a Euclidean domain — and the definition we are after is the dictionary entry that makes the translation possible.

What do we want this definition to deliver? We want a way of taking the pair $(V, \alpha)$ — a vector space *together with* a chosen operator — and repackaging it as a single algebraic object of a kind we can already classify. A bare vector space $V$ carries too little information: as an $F$-module it is just $F^{\dim V}$, and every operator lives on the same $V$, so $V$ alone cannot distinguish $\alpha$ from any other operator. The operator $\alpha$ is extra structure, and we need an object that *absorbs* $\alpha$ into its algebraic type, so that two operators are "the same" exactly when their packaged objects are isomorphic.

The desideratum, then: build a module whose [[Def - Ring|ring]] action encodes $\alpha$. Reverse-engineer it. A module over a [[Def - Ring|ring]] $R$ is an abelian [[Def - Group|group]] on which $R$ acts; the abelian [[Def - Group|group]] should plainly be $V$ itself (with its addition), since that is the underlying set we are studying. The question is the ring. Scalars $\lambda \in F$ already act on $V$ — that is the vector space structure — so $F$ must sit inside $R$. We want $\alpha$ to act too. So adjoin to $F$ a single new element whose action *is* $\alpha$, and call that element $X$. The smallest ring containing $F$ and one extra element $X$, with no relations imposed beyond those forced by the ring axioms, is the polynomial ring $F[X]$ — this is exactly the [[Def - Polynomial Ring|universal property of F[X]]] as the free commutative $F$-algebra on one generator. So the ring must be $F[X]$, and the action is forced: $X$ acts as $\alpha$, hence the monomial $X^i$ acts as $\alpha^i$, hence a polynomial $f(X) = \sum_i a_i X^i$ acts as $\sum_i a_i \alpha^i = f(\alpha)$. There is no choice anywhere. The definition writes itself once you decide you want a module that swallows $\alpha$.

Why $F[X]$ specifically, and not some nearby ring? *Weaken* the ring to just $F$: then the module is the plain vector space $V$, $\alpha$ is invisible, and the classification problem is trivial and useless — every operator on a fixed $V$ gives the identical $F$-module. The operator must enter the ring. *Strengthen* the ring — adjoin a second indeterminate $Y$, working over $F[X, Y]$: now you must say what $Y$ does, and there is no second operator on offer, so the extra generator is unmotivated dead weight, and worse, $F[X,Y]$ is not a [[Def - Euclidean Domain|Euclidean domain]] (it is not even a principal [[Def - Ideal|ideal]] domain), so the structure theorem no longer applies. The ring $F[X]$ is pinned exactly: it is the *smallest* ring that contains the scalars and has room for one operator, and — the decisive bonus — because $F$ is a field, $F[X]$ *is* a Euclidean domain, with the [[Thm - Euclidean Algorithm for Polynomials|division algorithm]] supplying the Euclidean function $\deg$. That is the whole point. The structure theory we want to borrow is a theory of [[Def - Module|modules]] over Euclidean domains; $V_\alpha$ is a module over $F[X]$; $F[X]$ is Euclidean; the machinery engages.

One more requirement makes the definition useful rather than merely possible. The structure theorem classifies *finitely generated* modules. If $V_\alpha$ were not finitely generated as an $F[X]$-module, the theorem would not apply. So we need: when $V$ is finite-dimensional, $V_\alpha$ is a finitely generated $F[X]$-module. This is true, and easy, and the reason is that $F$ sits inside $F[X]$: a spanning set for $V$ over the field $F$ — which exists and is finite, being a basis — is already a generating set for $V_\alpha$ over the larger ring $F[X]$, because anything you can build with $F$-coefficients you can certainly build with $F[X]$-coefficients. Finite [[Def - Dimension|dimension]] of $V$ over $F$ forces finite generation of $V_\alpha$ over $F[X]$. With that, every hypothesis of the structure theorem is met, and the definition delivers exactly what it was designed to deliver: a Euclidean-domain module, finitely generated, whose isomorphism type is a complete invariant of the operator $\alpha$ up to conjugacy.

The companion matrix is the second half of the dictionary. The structure theorem will express $V_\alpha$ as a direct sum of cyclic pieces $F[X]/(f)$. To read a *matrix* off this, we must know what the operator $\alpha$ — that is, multiplication by $X$ — looks like on a single cyclic piece $F[X]/(f)$. The companion matrix is precisely the answer: it is the matrix of "multiply by $X$" on $F[X]/(f)$, written in the natural basis. Defining it now means that when the structure theorem hands us the decomposition, the matrix is immediate.

---

# The Definition

This is a compound definition: it builds the **$F[X]$-module $V_\alpha$** of a linear operator, records its **finite generation**, and defines the **companion matrix** of a monic polynomial.

**The module $V_\alpha$.** Let $F$ be a field, $V$ a vector space over $F$, and $\alpha : V \to V$ a linear map. The **$F[X]$-module associated to $\alpha$**, written $V_\alpha$, has:

- underlying abelian group the additive group of $V$;
- $F[X]$-action given, for a polynomial $f \in F[X]$ and a vector $v \in V$, by
$$f \cdot v \;=\; \big(f(\alpha)\big)(v),$$
where $f(\alpha)$ is the linear operator obtained by substituting $\alpha$ for $X$: if $f = a_0 + a_1 X + \cdots + a_d X^d$ then $f(\alpha) = a_0 \operatorname{id}_V + a_1 \alpha + \cdots + a_d \alpha^d$, and $\big(f(\alpha)\big)(v)$ is this operator applied to $v$.

In particular the constant polynomial $\lambda \in F$ acts as scalar multiplication by $\lambda$, recovering the vector space structure, and the indeterminate $X$ acts as $\alpha$ itself: $X \cdot v = \alpha(v)$.

This is an $F[X]$-module: the module axioms hold because polynomial addition and multiplication are matched by operator addition and composition under the substitution $X \mapsto \alpha$ — the map $f \mapsto f(\alpha)$ is a ring homomorphism $F[X] \to \operatorname{End}_F(V)$, and a module over $F[X]$ is exactly an abelian group with such a homomorphism into its endomorphism ring.

**Finite generation.** If $V$ is finite-dimensional over $F$, then $V_\alpha$ is a [[Def - Finitely Generated Module|finitely generated]] $F[X]$-module. Indeed, if $v_1, \dots, v_n$ span $V$ as an $F$-vector space, they generate $V_\alpha$ as an $F[X]$-module, since every $F$-linear combination is in particular an $F[X]$-linear combination ($F \subseteq F[X]$).

**Companion matrix.** Let
$$f \;=\; a_0 + a_1 X + \cdots + a_{r-1} X^{r-1} + X^r \;\in\; F[X]$$
be a **monic** polynomial of degree $r$. The quotient ring $F[X]/(f)$ is, viewed as an $F$-vector space, $r$-dimensional with basis the [[Def - Residue|residue]] classes of
$$1,\ X,\ X^2,\ \dots,\ X^{r-1}.$$
The ring $F[X]/(f)$ is itself an $F[X]$-module, and multiplication by $X$ is an $F$-linear operator on it. The **companion matrix** of $f$, written $C(f)$, is the matrix of this operator "multiply by $X$" with respect to the basis $\{1, X, \dots, X^{r-1}\}$:
$$
C(f) \;=\;
\begin{pmatrix}
0 & 0 & \cdots & 0 & -a_0 \\
1 & 0 & \cdots & 0 & -a_1 \\
0 & 1 & \cdots & 0 & -a_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & -a_{r-1}
\end{pmatrix}.
$$
The columns are read off directly: for $j < r-1$, multiplying the basis vector $X^j$ by $X$ gives $X^{j+1}$, the next basis vector — hence the subdiagonal of $1$s. For the last basis vector $X^{r-1}$, multiplying by $X$ gives $X^r$, which in $F[X]/(f)$ equals $-a_0 - a_1 X - \cdots - a_{r-1} X^{r-1}$ because $f = 0$ in the quotient — hence the last column $(-a_0, -a_1, \dots, -a_{r-1})^{\mathsf T}$.

---

# Relate to Other Fields / Compression

The construction $V \rightsquigarrow V_\alpha$ is **extension of the acting ring along the inclusion $F \hookrightarrow F[X]$**, with the extra generator $X$ assigned to act as the chosen operator. It is the same move as turning a real vector space with a chosen complex structure $J$ (an operator with $J^2 = -\operatorname{id}$) into a $\mathbb{C}$-module: there one adjoins $i$ acting as $J$; here one adjoins $X$ acting as $\alpha$, with *no relation imposed* on $X$ — the relations that $\alpha$ happens to satisfy become the structure of the module rather than constraints on the ring. In the language of representation theory, $V_\alpha$ is precisely **a representation of the polynomial ring $F[X]$**, equivalently a representation of the free monoid on one generator, equivalently the data of a single operator. The slogan is: *an $F[X]$-module is the same thing as a vector space equipped with a distinguished operator* — the dictionary

$$\big(\text{vector space } V,\ \text{operator } \alpha\big) \quad\longleftrightarrow\quad \big(F[X]\text{-module } V_\alpha\big)$$

is a perfect correspondence, and isomorphism of $F[X]$-modules on the right is conjugacy of operators on the left.

The companion matrix compresses to one phrase: **$C(f)$ is the matrix of "multiply by $X$" on $F[X]/(f)$**. Everything visible in it is a consequence — the subdiagonal $1$s are the shifts $X^j \mapsto X^{j+1}$, the last column is the single relation $f = 0$ rearranged to express $X^r$ in lower degrees. The characteristic polynomial of $C(f)$ is $f$ itself, and the minimal polynomial of $C(f)$ is also $f$; the companion matrix is the most economical operator with prescribed characteristic-equals-minimal polynomial.

---

# Examples / Corollaries

**The nilpotent shift: $V_\alpha \cong F[X]/(X^r)$.** Suppose $V_\alpha \cong F[X]/(X^r)$ as $F[X]$-modules. Forgetting the $X$-action, this is in particular an isomorphism of $F$-vector spaces (an $F$-linear map is required to respect strictly less than an $F[X]$-linear map), so the [[Def - Residue|residue]] classes of $1, X, \dots, X^{r-1}$ form an $F$-basis of $V$. The companion matrix of $f = X^r$ — all coefficients $a_0 = \cdots = a_{r-1} = 0$ — is the pure subdiagonal
$$
C(X^r) \;=\;
\begin{pmatrix}
0 & 0 & \cdots & 0 & 0 \\
1 & 0 & \cdots & 0 & 0 \\
0 & 1 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & 0
\end{pmatrix},
$$
the **shift operator** sending each basis vector to the next and the last to $0$. Since $X$ acts as $\alpha$, in this basis $\alpha$ *is* this matrix: $\alpha$ is nilpotent with $\alpha^r = 0$ (because $X^r = 0$ in the quotient) and $\alpha^{r-1} \neq 0$. This is the model nilpotent operator of index $r$.

**The Jordan block: $V_\alpha \cong F[X]/((X-\lambda)^r)$.** Suppose $V_\alpha \cong F[X]/\big((X-\lambda)^r\big)$ for some $\lambda \in F$. Introduce the shifted operator
$$\beta \;=\; \alpha - \lambda\operatorname{id}_V \;:\; V \to V.$$
Setting $Y = X - \lambda$, the operator $\beta$ is multiplication by $Y$, and $V_\beta \cong F[Y]/(Y^r)$ — this is the previous example with $Y$ in place of $X$. So there is a basis of $V$ in which $\beta$ is the pure subdiagonal shift $C(Y^r)$. In that same basis $\alpha = \beta + \lambda\operatorname{id}_V$ is the shift with $\lambda$ added down the diagonal:
$$
\begin{pmatrix}
\lambda & 0 & \cdots & 0 & 0 \\
1 & \lambda & \cdots & 0 & 0 \\
0 & 1 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & \lambda
\end{pmatrix}.
$$
This is a **Jordan block** for the eigenvalue $\lambda$ (in the lower-triangular convention, with the $1$s below the diagonal rather than above). Thus the single cyclic module $F[X]/\big((X-\lambda)^r\big)$ is exactly one Jordan block — the observation that powers the [[Thm - Jordan Normal Form|Jordan normal form]].

**The general companion block: $V_\alpha \cong F[X]/(f)$.** For a general monic $f = a_0 + a_1 X + \cdots + a_{r-1}X^{r-1} + X^r$, an isomorphism $V_\alpha \cong F[X]/(f)$ gives the $F$-basis $1, X, \dots, X^{r-1}$ in which $\alpha$ is represented by the companion matrix $C(f)$. The two previous examples are the special cases $f = X^r$ and $f = (X-\lambda)^r$. This is the building block of the [[Thm - Rational Canonical Form|rational canonical form]].

**Non-example: $V_\alpha$ for $V$ infinite-dimensional need not be finitely generated.** Take $V = F[X]$ itself as an $F$-vector space (countably infinite-dimensional) and $\alpha$ multiplication by $X$. Then $V_\alpha$ is $F[X]$ as a module over itself, which *is* finitely generated (by $1$) — so this particular infinite-dimensional case is still finitely generated. But take instead $V = \bigoplus_{n \geq 0} F$ with $\alpha = 0$ the zero operator: then $V_\alpha$ has $X$ acting as $0$, so it is just the infinite-dimensional $F$-vector space with $F[X]$ acting through $F[X] \to F[X]/(X) = F$, and it is *not* finitely generated as an $F[X]$-module (a finite generating set would span a finite-dimensional space). The hypothesis $\dim_F V < \infty$ in the finite-generation statement is therefore essential.

**Corollary (the action factors through a quotient ring).** If $\dim_F V = n < \infty$, then $V_\alpha$ is finitely generated and, since $F[X]$ is a [[Def - Euclidean Domain|Euclidean domain]] hence a principal [[Def - Ideal|ideal]] domain, the [[Def - Annihilator|annihilator]] of $V_\alpha$ is a principal ideal $(m)$ for some monic $m$ — the **minimal polynomial** of $\alpha$. The $F[X]$-action then factors through the finite-dimensional quotient ring $F[X]/(m)$. *Calibration check:* recognising that finite [[Def - Dimension|dimension]] of $V$ forces a nonzero [[Def - Annihilator|annihilator]] (the powers $\operatorname{id}, \alpha, \dots, \alpha^{n^2}$ cannot be $F$-linearly independent in the $n^2$-dimensional space $\operatorname{End}_F(V)$) confirms you see why $V_\alpha$ has no free part.

**Corollary (companion matrix has $f$ as both characteristic and minimal polynomial).** For monic $f$ of degree $r$, the companion matrix $C(f)$ satisfies $\det(X\operatorname{id} - C(f)) = f$ and the minimal polynomial of $C(f)$ is also $f$. *Calibration check:* this is immediate from $V_\alpha \cong F[X]/(f)$ — the annihilator of the cyclic module $F[X]/(f)$ is exactly $(f)$, giving the minimal polynomial, and a cyclic module of $F$-dimension $r = \deg f$ forces the characteristic polynomial to have degree $r$ and to be a multiple of the minimal one, hence equal to $f$.

---

# Unlocked by This

> [!tip] Rational Canonical Form *(from Modules II — §3.4)*
> Feeding the finitely generated $F[X]$-module $V_\alpha$ into the structure theorem decomposes it as a direct sum of cyclic pieces $F[X]/(f_i)$ with $f_1 \mid \cdots \mid f_s$. Reading the companion matrix off each piece gives a canonical block-diagonal form for $\alpha$. See [[Thm - Rational Canonical Form]].

> [!tip] Jordan Normal Form *(from Modules II — §3.4)*
> Over $\mathbb{C}$, the primary decomposition of $V_\alpha$ breaks it into pieces $\mathbb{C}[X]/((X-\lambda)^m)$ — each one a Jordan block by the example above. See [[Thm - Jordan Normal Form]].

> [!tip] Smith Normal Form *(from Modules II — §3.3)*
> The decomposition of $V_\alpha$ is computed in practice by reducing the presentation matrix $X\operatorname{id} - A$ of the operator (a matrix over $F[X]$) to diagonal form by row and column operations. See [[Thm - Smith Normal Form]].

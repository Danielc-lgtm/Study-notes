---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Sobolev Norms are Independent of the Metric and Connections up to Equivalence"
  - "Def - Sobolev Space of Sections"
  - "Def - Connection on a Vector Bundle"
  - "Def - Connection Matrix and Local Form of a Connection"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $S^1=\mathbb{R}/2\pi\mathbb{Z}$ carry the flat metric $d\theta^2$, so that $|d\theta|=1$ and the Riemannian volume is $d\theta$, and let $L=S^1\times\mathbb{C}$ be the trivial complex line bundle with its standard Hermitian metric $|u|^2=u\overline u$. Fix a real-valued smooth function $a\in C^\infty(S^1;\mathbb{R})$ (necessarily $2\pi$-periodic), and consider the two connections
$$\nabla^0=d\qquad\text{(the trivial connection)},\qquad\qquad \nabla=d+ia(\theta)\,d\theta.$$
Both are Hermitian (metric-compatible) connections on $L$, differing by the imaginary-valued connection $1$-form $ia\,d\theta$. Write $\lVert\cdot\rVert_{W^{2,2},\,d}$ and $\lVert\cdot\rVert_{W^{2,2},\,\nabla}$ for the second-order Sobolev norms computed with $\nabla^0=d$ and with $\nabla$ respectively, both using the flat metric on $S^1$ and the flat metric on the iterated cotangent factors.

Set
$$M_0:=\sup_{\theta\in S^1}|a(\theta)|,\qquad M_1:=\sup_{\theta\in S^1}|a'(\theta)|,$$
which are finite because $a$ is smooth and $S^1$ is compact. Prove that there is a constant $C$, **explicit in $M_0$ and $M_1$**, with
$$\lVert u\rVert_{W^{2,2},\,\nabla}\leq C\,\lVert u\rVert_{W^{2,2},\,d}\qquad\text{and}\qquad \lVert u\rVert_{W^{2,2},\,d}\leq C\,\lVert u\rVert_{W^{2,2},\,\nabla}$$
for every $u\in C^\infty(S^1;\mathbb{C})$; one may take
$$C=\sqrt{\,3+5M_0^2+(M_1+M_0^2)^2\,}.$$

**Recall:**

This is the rank-one, one-dimensional, explicit-constant instance of the general theorem that the Sobolev norm does not depend, up to equivalence, on the choice of metric and connections.

![[Thm - Sobolev Norms are Independent of the Metric and Connections up to Equivalence#Statement]]

The Sobolev norm is built from iterated covariant derivatives, as defined here.

![[Def - Sobolev Space of Sections#The Definition]]

The rule for differentiating a product of a function and a section — the Leibniz rule that defines a connection — is what turns $\nabla$ into $d$ plus a lower-order term.

![[Def - Connection on a Vector Bundle#The Definition]]

The connection $1$-form $ia\,d\theta$ is the connection matrix of $\nabla$ in the global unit frame $s_0(\theta)=(\theta,1)$ of $L$, in the sense of the local-form definition.

![[Def - Connection Matrix and Local Form of a Connection#The Definition]]

Throughout, a prime denotes the ordinary $\theta$-derivative, so $u'=\partial_\theta u$. Because $L$ is trivialised by the global unit section $s_0$, a smooth section is just a smooth function $u\in C^\infty(S^1;\mathbb{C})$, and we identify the two. We write $\lVert w\rVert_{L^2}^2=\int_{S^1}|w(\theta)|^2\,d\theta$ for the $L^2$ norm of a function $w$.

---

# Convergent Strategy

**Problem class.** This is a *norm-equivalence-with-explicit-constant* problem: two norms are known abstractly to be equivalent (that is the content of [[Thm - Sobolev Norms are Independent of the Metric and Connections up to Equivalence|the equivalence theorem]]), and the task is to make the equivalence constant explicit in terms of the data. Problems of this shape are ubiquitous in analysis whenever one must track how an estimate degrades as a background field grows; the general theorem tells you the constant *exists* by a compactness argument, and the drill is to replace compactness with an honest computation that exhibits the constant. The reusable recognition is that "the difference of two connections is a smooth zero-order object", so the higher covariant derivatives of the two connections differ by *lower-order* terms with coefficients built from $a$ and its derivatives.

**Assumption pattern.** The hypotheses are that $a$ is smooth on the compact manifold $S^1$, giving finite $M_0=\sup|a|$ and $M_1=\sup|a'|$. Compactness is what guarantees these suprema are finite; the general theorem uses exactly this ("on a compact manifold every smooth object is bounded"), and here we see it in the concrete guise that $a$ and $a'$ are bounded. The rank-one, one-dimensional setting removes every complication of the general proof — there is no induction over tensor slots and no comparison of metrics, because the metric is fixed and flat — leaving only the algebra of iterating a first-order operator with a bounded zero-order perturbation.

**Theorem routing.** The route is a direct computation, not a citation. From [[Def - Connection on a Vector Bundle|the Leibniz rule]], $\nabla u=(u'+iau)\,d\theta$, so $\nabla$ acts on functions as the first-order operator $D:=\partial_\theta+ia$. Because $S^1$ with the flat metric has $\nabla^{\mathrm{LC}}(d\theta)=0$, iterating $\nabla$ on the cotangent-tensor factors just iterates $D$ on the coefficient function, so $\nabla^2 u=(D^2u)\,d\theta^{\otimes 2}$. One expands $Du$ and $D^2u$ by the Leibniz rule, bounds each term in $L^2$ by the triangle inequality and $\sup|a|,\sup|a'|$, packages the three resulting inequalities as a single lower-triangular matrix acting on $(\lVert u\rVert_{L^2},\lVert u'\rVert_{L^2},\lVert u''\rVert_{L^2})$, and takes the Frobenius norm of that matrix as $C$. The converse follows by writing $d=\nabla-ia\,d\theta$, i.e. $\partial_\theta=D-ia$, and running the identical computation with the roles of $D$ and $\partial_\theta$ exchanged; the coefficients that appear have the same moduli, so the constant is the same.

**Key decision point.** The idea that makes the computation clean is to *organise the three term-by-term bounds into a linear map on the vector of $L^2$-norms of the ordinary derivatives*. Writing $A=\lVert u\rVert_{L^2}$, $B=\lVert u'\rVert_{L^2}$, $E=\lVert u''\rVert_{L^2}$, the bounds $\lVert Du\rVert_{L^2}\leq B+M_0A$ and $\lVert D^2u\rVert_{L^2}\leq E+2M_0B+(M_1+M_0^2)A$ say exactly that the vector of $\nabla$-derivative norms is componentwise dominated by $L\,(A,B,E)^{\mathsf T}$ for an explicit lower-triangular matrix $L$; then $\lVert u\rVert_{W^{2,2},\nabla}=|(\text{$\nabla$-norms})|\leq|L(A,B,E)^{\mathsf T}|\leq\lVert L\rVert_{\mathrm F}\,|(A,B,E)|=\lVert L\rVert_{\mathrm F}\,\lVert u\rVert_{W^{2,2},d}$, with the Frobenius norm supplying a closed-form constant. Recognising that the whole estimate is "one matrix" is what avoids an ad hoc juggling of six separate inequalities.

---

# Legal Operations Used

The numbering will be reconciled with the topic page's Legal Operations once written; each operation is named descriptively here.

1. **Write a connection as $d$ plus its connection $1$-form and read off the acting operator.** In the global unit frame $s_0$, $\nabla=d+ia\,d\theta$, so $\nabla$ acts on the coefficient function as $D=\partial_\theta+ia$. This is the operation of localising a connection to its connection matrix, from [[Def - Connection Matrix and Local Form of a Connection]].

2. **Iterate a covariant derivative using that the base cotangent connection is flat.** Because $\nabla^{\mathrm{LC}}(d\theta)=0$ on the flat circle, the induced connection on $(T^\ast S^1)^{\otimes i}\otimes L$ leaves $d\theta^{\otimes i}$ parallel, so $\nabla^i u=(D^i u)\,d\theta^{\otimes i}$ and $|\nabla^i u|=|D^i u|$. This is the operation of computing iterated covariant derivatives in a parallel frame.

3. **Expand a first-order operator's powers by the Leibniz rule.** The identities $Du=u'+iau$ and $D^2u=u''+2iau'+(ia'-a^2)u$ are obtained by applying the Leibniz rule of [[Def - Connection on a Vector Bundle]] once and twice.

4. **Bound each term in $L^2$ by the triangle inequality and the sup-bounds of the coefficients.** Every product $a\cdot w$ satisfies $\lVert a w\rVert_{L^2}\leq M_0\lVert w\rVert_{L^2}$, and $\lVert a' w\rVert_{L^2}\leq M_1\lVert w\rVert_{L^2}$, because $a,a'$ are bounded by $M_0,M_1$ on compact $S^1$; the triangle inequality (Minkowski) in $L^2$ then bounds each sum.

5. **Package termwise bounds as a matrix and take its Frobenius norm.** Assembling the bounds into $L$ and using $|Lx|\leq\lVert L\rVert_{\mathrm F}|x|$ yields the explicit equivalence constant.

6. **Invert the roles of the two connections to obtain the converse for free.** Since $d=\nabla-ia\,d\theta$ is the connection with potential $-a$ relative to $\nabla$, the converse is the same computation with $a\mapsto -a$; the moduli $M_0,M_1$ are unchanged, so the constant is unchanged.

---

# Hints

> [!note]- Hint 1
> In the global unit frame, a section is a function $u$, and the Leibniz rule gives $\nabla u=(u'+iau)\,d\theta$. So $\nabla$ acts on functions as the operator $D=\partial_\theta+ia$. What first-order operator does $d$ act as? (Answer: $\partial_\theta$.)

> [!note]- Hint 2
> To compute $\nabla^2 u$ you need the induced connection on $T^\ast S^1\otimes L$. On the flat circle $d\theta$ is parallel for the Levi-Civita connection, so $\nabla^2 u=(D^2u)\,d\theta^{\otimes 2}$ and only the coefficient $D^2u$ matters. Compute $D^2u=(\partial_\theta+ia)(\partial_\theta+ia)u$ carefully with the Leibniz rule — remember $\partial_\theta(iau)=ia'u+iau'$.

> [!note]- Hint 3
> You should find $Du=u'+iau$ and $D^2u=u''+2iau'+(ia'-a^2)u$. Now take $L^2$ norms and use the triangle inequality together with $|a|\leq M_0$, $|a'|\leq M_1$. Write $A=\lVert u\rVert_{L^2}$, $B=\lVert u'\rVert_{L^2}$, $E=\lVert u''\rVert_{L^2}$ and express your bounds on $\lVert Du\rVert_{L^2},\lVert D^2u\rVert_{L^2}$ as linear combinations of $A,B,E$.

> [!note]- Hint 4
> The three quantities $\lVert u\rVert_{L^2}=A$, $\lVert Du\rVert_{L^2}\leq B+M_0A$, $\lVert D^2u\rVert_{L^2}\leq E+2M_0B+(M_1+M_0^2)A$ are the components of $L\,(A,B,E)^{\mathsf T}$ for a lower-triangular $L$. Since $\lVert u\rVert_{W^{2,2},\nabla}^2=A^2+\lVert Du\rVert_{L^2}^2+\lVert D^2u\rVert_{L^2}^2$, bound it by $|L(A,B,E)^{\mathsf T}|^2\leq\lVert L\rVert_{\mathrm F}^2(A^2+B^2+E^2)$.

> [!note]- Hint 5
> For the converse, solve for the ordinary derivatives: $u'=Du-iau$ and $u''=D^2u-2ia\,Du-(a^2+ia')u$. Take $L^2$ norms; the coefficients $-ia,-2ia,-(a^2+ia')$ have the same moduli $M_0,2M_0,(M_0^2+M_1)$ as before, so you get the identical matrix (up to signs) and hence the same $C$.

---

# Solution

The plan is to reduce both norms to the first-order operator $D=\partial_\theta+ia$ acting on the coefficient function, expand $Du$ and $D^2u$ by the Leibniz rule, bound each term in $L^2$ using the sup-bounds $M_0,M_1$, and assemble the bounds into a single matrix whose Frobenius norm is the equivalence constant; the converse is the same computation with the two connections exchanged.

**Step 1: Reduce the $\nabla$-norm to the operator $D=\partial_\theta+ia$ on the coefficient function.**

In the global unit frame $s_0$ a section is a function $u$, and $\nabla u=(Du)\,d\theta$ with $Du=u'+iau$; iterating in the parallel frame $d\theta^{\otimes i}$ gives $\nabla^i u=(D^i u)\,d\theta^{\otimes i}$, so $\lVert\nabla^i u\rVert_{L^2}=\lVert D^i u\rVert_{L^2}$.

> [!note]- Derivation
> The trivial line bundle $L=S^1\times\mathbb{C}$ has the global unit section $s_0(\theta)=(\theta,1)$, and every smooth section is $u\,s_0$ for a unique $u\in C^\infty(S^1;\mathbb{C})$; we identify the section with $u$.
>
> **First covariant derivative.** By the [[Def - Connection Matrix and Local Form of a Connection|local form of the connection]], $\nabla s_0=(ia\,d\theta)\,s_0$, so by the [[Def - Connection on a Vector Bundle|Leibniz rule]] $\nabla(us_0)=du\otimes s_0+u\,\nabla s_0=(u'\,d\theta)s_0+u(ia\,d\theta)s_0=\big((u'+iau)\,d\theta\big)s_0$. Writing $D:=\partial_\theta+ia$, this is $\nabla u=(Du)\,d\theta$ with $Du=u'+iau$.
>
> **Flatness of the cotangent factor.** To iterate, $\nabla^2 u=\nabla(\nabla u)$ uses the tensor-product connection on $T^\ast S^1\otimes L$ built from the Levi-Civita connection $\nabla^{\mathrm{LC}}$ on $T^\ast S^1$ and $\nabla$ on $L$. In the coordinate $\theta$ the flat metric $d\theta^2$ has all Christoffel symbols zero, so $\nabla^{\mathrm{LC}}(d\theta)=0$: the covector field $d\theta$ is parallel. Hence, for a section written as $w\,d\theta$ with $w$ a $\mathbb{C}$-valued function,
> $$\nabla(w\,d\theta)=(\nabla^{\mathrm{LC}}d\theta)\,w+d\theta\otimes\nabla(w s_0)/s_0\text{-part}=d\theta\otimes\big((Dw)\,d\theta\big)=(Dw)\,d\theta^{\otimes 2}\qquad\text{(}\nabla^{\mathrm{LC}}d\theta=0\text{; Leibniz; the $L$-part acts by }D\text{).}$$
> Applying this with $w=Du$ gives $\nabla^2 u=(D^2 u)\,d\theta^{\otimes 2}$, and by induction $\nabla^i u=(D^i u)\,d\theta^{\otimes i}$.
>
> **Norms.** Since $|d\theta|=1$ for the flat metric, $|d\theta^{\otimes i}|=1$, so the pointwise norm satisfies $|\nabla^i u|=|D^i u|$ and therefore $\lVert\nabla^i u\rVert_{L^2}=\lVert D^i u\rVert_{L^2}$. In particular, from [[Def - Sobolev Space of Sections|the definition of the Sobolev norm]],
> $$\lVert u\rVert_{W^{2,2},\nabla}^2=\sum_{i=0}^{2}\lVert\nabla^i u\rVert_{L^2}^2=\lVert u\rVert_{L^2}^2+\lVert Du\rVert_{L^2}^2+\lVert D^2u\rVert_{L^2}^2,$$
> and, taking $a\equiv 0$ so that $D=\partial_\theta$, $\lVert u\rVert_{W^{2,2},d}^2=\lVert u\rVert_{L^2}^2+\lVert u'\rVert_{L^2}^2+\lVert u''\rVert_{L^2}^2$.

**Step 2: Expand $Du$ and $D^2u$ by the Leibniz rule.**

The first two powers of $D$ are $Du=u'+iau$ and $D^2u=u''+2ia\,u'+(ia'-a^2)u$.

> [!note]- Derivation
> The first is the definition $Du=(\partial_\theta+ia)u=u'+iau$. For the second, apply $D=\partial_\theta+ia$ to $Du$:
> $$D^2u=(\partial_\theta+ia)(u'+iau)=\partial_\theta(u'+iau)+ia(u'+iau)\qquad\text{(definition of }D\text{).}$$
> Expand the two pieces, using the product rule $\partial_\theta(iau)=ia'u+iau'$:
> $$\partial_\theta(u'+iau)=u''+ia'u+iau'\qquad\text{(product rule),}$$
> $$ia(u'+iau)=iau'+i^2a^2u=iau'-a^2u\qquad\text{(}i^2=-1\text{).}$$
> Adding,
> $$D^2u=u''+ia'u+iau'+iau'-a^2u=u''+2ia\,u'+(ia'-a^2)u\qquad\text{(collecting the two }iau'\text{ terms).}$$

**Step 3: Bound the $\nabla$-norm terms in $L^2$ and assemble the matrix.**

With $A=\lVert u\rVert_{L^2}$, $B=\lVert u'\rVert_{L^2}$, $E=\lVert u''\rVert_{L^2}$, one has $\lVert Du\rVert_{L^2}\leq B+M_0A$ and $\lVert D^2u\rVert_{L^2}\leq E+2M_0B+(M_1+M_0^2)A$.

> [!note]- Derivation
> Throughout, for a bounded measurable coefficient $b$ and a function $w$, $\lVert b w\rVert_{L^2}^2=\int_{S^1}|b|^2|w|^2\,d\theta\leq(\sup|b|)^2\int_{S^1}|w|^2\,d\theta$, so $\lVert b w\rVert_{L^2}\leq\sup|b|\cdot\lVert w\rVert_{L^2}$; with $b=a$ this is $\leq M_0\lVert w\rVert_{L^2}$ and with $b=a'$ it is $\leq M_1\lVert w\rVert_{L^2}$.
>
> **The first-order term.** By the triangle inequality (Minkowski) in $L^2$,
> $$\lVert Du\rVert_{L^2}=\lVert u'+iau\rVert_{L^2}\leq\lVert u'\rVert_{L^2}+\lVert iau\rVert_{L^2}\leq B+M_0A\qquad\text{(triangle inequality; }|i|=1,\ \lVert au\rVert_{L^2}\leq M_0A\text{).}$$
>
> **The second-order term.** Again by the triangle inequality and $|ia'-a^2|\leq|a'|+|a|^2\leq M_1+M_0^2$,
> $$\lVert D^2u\rVert_{L^2}=\lVert u''+2ia\,u'+(ia'-a^2)u\rVert_{L^2}\leq\lVert u''\rVert_{L^2}+2\lVert au'\rVert_{L^2}+\lVert(ia'-a^2)u\rVert_{L^2}\leq E+2M_0B+(M_1+M_0^2)A$$
> (triangle inequality; $\lVert au'\rVert_{L^2}\leq M_0B$; $\lVert(ia'-a^2)u\rVert_{L^2}\leq(M_1+M_0^2)A$).
>
> **The zeroth-order term** is exact: $\lVert u\rVert_{L^2}=A$.
>
> **Matrix form.** These three bounds say the vector $\big(\lVert u\rVert_{L^2},\lVert Du\rVert_{L^2},\lVert D^2u\rVert_{L^2}\big)$ is dominated componentwise, entry by nonnegative entry, by $L\,(A,B,E)^{\mathsf T}$ where
> $$L=\begin{pmatrix}1&0&0\\ M_0&1&0\\ M_1+M_0^2&2M_0&1\end{pmatrix}.$$

**Step 4: Take the Frobenius norm to obtain the explicit constant.**

The forward inequality holds with $C=\lVert L\rVert_{\mathrm F}=\sqrt{3+5M_0^2+(M_1+M_0^2)^2}$.

> [!note]- Derivation
> Since all entries of $L$ and all of $A,B,E$ are nonnegative, componentwise domination gives, term by term, $\lVert\nabla^i u\rVert_{L^2}\leq\big(L(A,B,E)^{\mathsf T}\big)_i$, and squaring and summing preserves the inequality:
> $$\lVert u\rVert_{W^{2,2},\nabla}^2=\sum_{i=0}^2\lVert\nabla^i u\rVert_{L^2}^2\leq\big|L(A,B,E)^{\mathsf T}\big|^2\qquad\text{(Step 1; componentwise domination with nonnegative entries).}$$
> For any real matrix $L$ and vector $x$, $|Lx|\leq\lVert L\rVert_{\mathrm F}\,|x|$, where $\lVert L\rVert_{\mathrm F}=\big(\sum_{i,j}L_{ij}^2\big)^{1/2}$ is the Frobenius norm (this is Cauchy–Schwarz applied to each row: $(Lx)_i=\sum_j L_{ij}x_j$, so $|(Lx)_i|^2\leq(\sum_j L_{ij}^2)|x|^2$, and summing over $i$ gives $|Lx|^2\leq\lVert L\rVert_{\mathrm F}^2|x|^2$). Hence
> $$\lVert u\rVert_{W^{2,2},\nabla}^2\leq\lVert L\rVert_{\mathrm F}^2\,(A^2+B^2+E^2)=\lVert L\rVert_{\mathrm F}^2\,\lVert u\rVert_{W^{2,2},d}^2\qquad\text{(}|Lx|\leq\lVert L\rVert_{\mathrm F}|x|\text{; }A^2+B^2+E^2=\lVert u\rVert_{W^{2,2},d}^2\text{).}$$
> The Frobenius norm of $L$ is
> $$\lVert L\rVert_{\mathrm F}^2=\underbrace{1}_{\text{row }1}+\underbrace{M_0^2+1}_{\text{row }2}+\underbrace{(M_1+M_0^2)^2+4M_0^2+1}_{\text{row }3}=3+5M_0^2+(M_1+M_0^2)^2.$$
> Taking square roots, $\lVert u\rVert_{W^{2,2},\nabla}\leq C\lVert u\rVert_{W^{2,2},d}$ with $C=\sqrt{3+5M_0^2+(M_1+M_0^2)^2}$.

**Step 5: The converse, by exchanging the two connections.**

Solving Step 2 for the ordinary derivatives and running the identical estimate yields $\lVert u\rVert_{W^{2,2},d}\leq C\lVert u\rVert_{W^{2,2},\nabla}$ with the *same* constant $C$.

> [!note]- Derivation
> **Invert the operator identities.** From $Du=u'+iau$ we get $u'=Du-iau$. From $D^2u=u''+2ia\,u'+(ia'-a^2)u$ we solve for $u''$ and then substitute $u'=Du-iau$:
> $$u''=D^2u-2ia\,u'-(ia'-a^2)u=D^2u-2ia(Du-iau)-(ia'-a^2)u\qquad\text{(Step 2 rearranged; }u'=Du-iau\text{).}$$
> Expanding $-2ia(Du-iau)=-2ia\,Du+2i^2a^2u=-2ia\,Du-2a^2u$ and combining the $u$-terms $-2a^2u-(ia'-a^2)u=-(a^2+ia')u$,
> $$u''=D^2u-2ia\,Du-(a^2+ia')u\qquad\text{(}i^2=-1\text{; collecting the }u\text{-coefficients).}$$
> **Estimate.** With the same conventions and $A'=\lVert u\rVert_{L^2}$, $B'=\lVert Du\rVert_{L^2}$, $E'=\lVert D^2u\rVert_{L^2}$ (the $\nabla$-derivative norms), the triangle inequality gives
> $$\lVert u'\rVert_{L^2}=\lVert Du-iau\rVert_{L^2}\leq B'+M_0A'\qquad\text{(triangle inequality; }\lVert au\rVert_{L^2}\leq M_0A'\text{),}$$
> $$\lVert u''\rVert_{L^2}=\lVert D^2u-2ia\,Du-(a^2+ia')u\rVert_{L^2}\leq E'+2M_0B'+(M_0^2+M_1)A'$$
> (triangle inequality; $\lVert -2ia\,Du\rVert_{L^2}\leq 2M_0B'$; $|a^2+ia'|\leq M_0^2+M_1$, so $\lVert(a^2+ia')u\rVert_{L^2}\leq(M_0^2+M_1)A'$).
>
> **Same matrix, same constant.** These are exactly the bounds of Step 3 with $(A,B,E)$ replaced by $(A',B',E')$ and with the identical numerical coefficients $M_0,\ 2M_0,\ M_1+M_0^2$; the governing matrix is
> $$L'=\begin{pmatrix}1&0&0\\ M_0&1&0\\ M_0^2+M_1&2M_0&1\end{pmatrix},$$
> which has the same entries as $L$ (the sign changes in the operator identities affect only the phases $-i$, not the moduli that enter the $L^2$ bounds), so $\lVert L'\rVert_{\mathrm F}=\lVert L\rVert_{\mathrm F}=C$. Repeating Step 4 verbatim,
> $$\lVert u\rVert_{W^{2,2},d}^2=A'^2\!+\lVert u'\rVert_{L^2}^2+\lVert u''\rVert_{L^2}^2\leq\lVert L'\rVert_{\mathrm F}^2(A'^2+B'^2+E'^2)=C^2\,\lVert u\rVert_{W^{2,2},\nabla}^2,$$
> hence $\lVert u\rVert_{W^{2,2},d}\leq C\lVert u\rVert_{W^{2,2},\nabla}$.

> [!note]- Complete formal solution
> Identify sections of $L=S^1\times\mathbb{C}$ with functions via the global unit section. By the Leibniz rule, $\nabla u=(Du)\,d\theta$ with $D=\partial_\theta+ia$; since the flat circle has $\nabla^{\mathrm{LC}}(d\theta)=0$, iterating gives $\nabla^i u=(D^iu)\,d\theta^{\otimes i}$ and $\lVert\nabla^i u\rVert_{L^2}=\lVert D^iu\rVert_{L^2}$ (as $|d\theta|=1$). Thus $\lVert u\rVert_{W^{2,2},\nabla}^2=\lVert u\rVert_{L^2}^2+\lVert Du\rVert_{L^2}^2+\lVert D^2u\rVert_{L^2}^2$ and $\lVert u\rVert_{W^{2,2},d}^2=\lVert u\rVert_{L^2}^2+\lVert u'\rVert_{L^2}^2+\lVert u''\rVert_{L^2}^2$.
>
> By the Leibniz rule, $Du=u'+iau$ and $D^2u=u''+2ia\,u'+(ia'-a^2)u$. Put $A=\lVert u\rVert_{L^2}$, $B=\lVert u'\rVert_{L^2}$, $E=\lVert u''\rVert_{L^2}$. Using $\lVert bw\rVert_{L^2}\leq\sup|b|\,\lVert w\rVert_{L^2}$ and the triangle inequality,
> $$\lVert Du\rVert_{L^2}\leq B+M_0A,\qquad \lVert D^2u\rVert_{L^2}\leq E+2M_0B+(M_1+M_0^2)A,$$
> where $M_0=\sup|a|$, $M_1=\sup|a'|$ (finite by smoothness on compact $S^1$) and $|ia'-a^2|\leq M_1+M_0^2$. Hence the vector of $\nabla$-derivative $L^2$-norms is componentwise $\leq L(A,B,E)^{\mathsf T}$ with
> $$L=\begin{pmatrix}1&0&0\\ M_0&1&0\\ M_1+M_0^2&2M_0&1\end{pmatrix}.$$
> Because entries are nonnegative, $\lVert u\rVert_{W^{2,2},\nabla}^2\leq|L(A,B,E)^{\mathsf T}|^2\leq\lVert L\rVert_{\mathrm F}^2(A^2+B^2+E^2)=\lVert L\rVert_{\mathrm F}^2\lVert u\rVert_{W^{2,2},d}^2$, using $|Lx|\leq\lVert L\rVert_{\mathrm F}|x|$ (row-wise Cauchy–Schwarz). Since $\lVert L\rVert_{\mathrm F}^2=1+(M_0^2+1)+\big((M_1+M_0^2)^2+4M_0^2+1\big)=3+5M_0^2+(M_1+M_0^2)^2$, we obtain $\lVert u\rVert_{W^{2,2},\nabla}\leq C\lVert u\rVert_{W^{2,2},d}$ with $C=\sqrt{3+5M_0^2+(M_1+M_0^2)^2}$.
>
> For the converse, invert: $u'=Du-iau$ and $u''=D^2u-2ia\,Du-(a^2+ia')u$. With $A'=\lVert u\rVert_{L^2}$, $B'=\lVert Du\rVert_{L^2}$, $E'=\lVert D^2u\rVert_{L^2}$, the same estimates give $\lVert u'\rVert_{L^2}\leq B'+M_0A'$ and $\lVert u''\rVert_{L^2}\leq E'+2M_0B'+(M_0^2+M_1)A'$, i.e. the matrix $L'$ with the same entry moduli as $L$; thus $\lVert L'\rVert_{\mathrm F}=C$ and $\lVert u\rVert_{W^{2,2},d}\leq C\lVert u\rVert_{W^{2,2},\nabla}$. Both inequalities hold with the single explicit constant $C=\sqrt{3+5M_0^2+(M_1+M_0^2)^2}$, which is the required equivalence. $\blacksquare$

> [!warning] Illegal but tempting shortcut: quoting the equivalence theorem for the constant
> One might be tempted to write "the two norms are equivalent by [[Thm - Sobolev Norms are Independent of the Metric and Connections up to Equivalence]], so a constant $C$ exists, done." This settles *existence* of $C$ but not its *value*: the general theorem obtains $C$ from a compactness argument (a continuous positive function on a compact manifold attains a positive minimum) that gives no formula. The exercise asks precisely for the explicit dependence on $\sup|a|$ and $\sup|a'|$, which only the term-by-term computation above can supply. The general theorem's compactness is honestly replaced here by the two elementary facts $M_0<\infty$ and $M_1<\infty$ — the concrete form, in rank one on $S^1$, of "on a compact manifold every smooth object is bounded".

---

# Key Takeaways

**Two connections differ by a zero-order term, so their iterated derivatives differ by strictly lower-order terms with coefficients built from the difference and its derivatives.** This is the mechanism behind the whole equivalence theorem, and the rank-one circle case shows it in its most transparent form: $\nabla=d+ia\,d\theta$ means $\nabla$ acts as $D=\partial_\theta+ia$, and each extra power of $D$ produces the corresponding power of $\partial_\theta$ plus a tail of lower-order terms whose coefficients are polynomials in $a,a',a'',\dots$ — here $D^2=\partial_\theta^2+2ia\,\partial_\theta+(ia'-a^2)$. Because those coefficients are bounded on a compact manifold, every such tail is bounded in $L^2$ by the lower-order norms already counted, and the two $W^{k,2}$ norms sandwich each other. The reusable principle is: whenever you must compare an operator's Sobolev estimates under a perturbation of the connection (or of the metric), expand the perturbed operator, isolate the top-order part which matches, and control the remainder by the coefficients' sup-norms; the trigger is any phrase of the form "the estimate is independent of the connection up to equivalence", and the transferable diagnostic is to count orders — the difference always lands one order below the top and is therefore harmless.

**Compactness in the abstract theorem is exactly the finiteness of the coefficient sup-norms in the concrete one.** The general equivalence theorem invokes compactness of $M$ to know that the smooth comparison coefficients are bounded and that the metrics are uniformly comparable; here that abstraction has collapsed to the two numbers $M_0=\sup|a|$ and $M_1=\sup|a'|$, both finite because $a$ is smooth and $S^1$ is compact. Making the constant explicit therefore means tracking exactly where and how many times each coefficient enters. The lesson worth carrying is that an existence-by-compactness proof and an explicit-constant proof are the same computation viewed at two resolutions: the former reports only that a supremum is finite, the latter records its numerical role. When an application needs a quantitative estimate — a rate at which a bound degrades as a gauge field grows, say — one returns to the compactness proof and reads off the constant from the finitely many sup-norms it silently used. The trigger is a request for "explicit $C$" or "how does the constant depend on the data"; the pattern is to redo the equivalence with the triangle inequality and coefficient sup-bounds in place of the compactness step.

**Packaging a family of scalar estimates as one matrix inequality turns bookkeeping into a single Frobenius-norm computation, and the converse comes for free by exchanging the two operators.** The organisational move — writing the six term-by-term bounds as $\text{(perturbed norms)}\leq L\,(\text{unperturbed norms})$ for a lower-triangular $L$ and reading off $C=\lVert L\rVert_{\mathrm F}$ — is a device that recurs whenever several norms must be simultaneously controlled: it is the same idea as estimating a system of inequalities by the norm of its coefficient matrix, and it scales to higher order (the matrix becomes $(k+1)\times(k+1)$ with binomial-type entries from iterating $D$) and to higher rank (the entries become operator norms of the endomorphism-valued coefficients). Equally reusable is the observation that the converse inequality need not be proved afresh: since $d=\nabla+i(-a)\,d\theta$ presents $d$ as a connection perturbed from $\nabla$ by the potential $-a$, and the estimate depends on $a$ only through the moduli $M_0,M_1$ which are invariant under $a\mapsto -a$, the backward bound holds with the identical constant. The trigger for the matrix packaging is any equivalence of two norms each defined as a sum of squares of controlled quantities; the trigger for the free converse is a perturbation that is its own inverse up to a sign, so that the two directions are related by a symmetry of the data. A companion drill is [[Ex - Fourier Coefficients of Smooth Functions Decay Rapidly]], where the same "differentiation shifts order" bookkeeping is done on the Fourier side.

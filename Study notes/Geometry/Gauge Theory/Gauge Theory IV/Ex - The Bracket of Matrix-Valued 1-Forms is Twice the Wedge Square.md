---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Def - Curvature of a Vector-Bundle Connection"
  - "Def - The Pauli Matrices"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\mathfrak{g}\subseteq\mathfrak{gl}_k(\mathbb{K})=\operatorname{End}(\mathbb{K}^k)$ be a matrix Lie algebra, that is, a linear subspace of the $k\times k$ matrices closed under the commutator bracket $[X,Y]=XY-YX$; here $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$. Let $M$ be a smooth manifold and let $A,B\in\Omega^1(M;\mathfrak{g})$ be $\mathfrak{g}$-valued $1$-forms on $M$. For such matrix-valued forms there are two distinct products, both landing in $\Omega^2(M;\mathfrak{g})$:

- the **matrix wedge** $A\wedge B$, which multiplies coefficient matrices by ordinary matrix multiplication;
- the **bracket** $[A\wedge B]$, which combines the coefficient matrices by the Lie bracket.

Prove the two identities relating them:
$$[A\wedge B]=A\wedge B+B\wedge A,\qquad\qquad [A\wedge A]=2\,A\wedge A.$$

Then, for the explicit $\mathfrak{su}(2)$-adjacent form
$$A=\sigma_1\,dx+\sigma_2\,dy\in\Omega^1(\mathbb{R}^2;\mathfrak{gl}_2(\mathbb{C}))$$
on $\mathbb{R}^2$ with coordinates $(x,y)$, where $\sigma_1,\sigma_2$ are the first two Pauli matrices, compute both $A\wedge A$ and $[A\wedge A]$ directly and confirm that $[A\wedge A]=2\,A\wedge A$ on this example.

This is the identity that reconciles the two ways the curvature of a matrix connection is written: Haydys's local formula appears both as $F_\nabla=dA+A\wedge A$ (equation (18)) and as $F_\nabla=dA+\tfrac12[A\wedge A]$ (equation (20)), and these agree precisely because $\tfrac12[A\wedge A]=A\wedge A$.

**Recall:**

The objects in play are the two products of $\mathfrak{g}$-valued forms, the commutator bracket of a matrix Lie algebra, and the Pauli matrices.

![[Def - Lie-Algebra-Valued Differential Forms and Their Bracket#The Definition]]

A **[[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|$\mathfrak{g}$-valued $p$-form]]** is an element of $\Omega^p(M;\mathfrak{g})=\Omega^p(M)\otimes\mathfrak{g}$; it may be written as a finite sum $\alpha=\sum_i\omega_i\otimes\xi_i$ with $\omega_i\in\Omega^p(M)$ ordinary forms and $\xi_i\in\mathfrak{g}$. The **bracket** of $\alpha\in\Omega^p(M;\mathfrak{g})$ and $\beta\in\Omega^q(M;\mathfrak{g})$ is the $\mathfrak{g}$-valued $(p+q)$-form defined on decomposable pieces by
$$[(\omega\otimes\xi)\wedge(\eta\otimes\zeta)]:=(\omega\wedge\eta)\otimes[\xi,\zeta]$$
and extended bilinearly. For two $1$-forms this evaluates on vector fields $X,Y$ as
$$[\alpha\wedge\beta](X,Y)=[\alpha(X),\beta(Y)]-[\alpha(Y),\beta(X)].$$
When $\mathfrak{g}\subseteq\mathfrak{gl}_k$ is a matrix algebra there is in addition the **matrix wedge** $\alpha\wedge\beta$, defined by pairing coefficient matrices through matrix multiplication,
$$(\omega\otimes\xi)\wedge(\eta\otimes\zeta):=(\omega\wedge\eta)\otimes(\xi\zeta),$$
which for two $1$-forms evaluates as
$$(\alpha\wedge\beta)(X,Y)=\alpha(X)\beta(Y)-\alpha(Y)\beta(X),$$
the products $\alpha(X)\beta(Y)$ being matrix products. The matrix wedge is defined only for matrix (associative) algebras, whereas the bracket is defined for any Lie algebra.

> [!warning] Convention: the two curvature formulas
> Haydys writes the local curvature both as $F_\nabla=dA+A\wedge A$ (his equation (18), the form that drops straight out of $d^\nabla\circ d^\nabla$) and, "thinking of $A$ as a $1$-form with values in the Lie algebra $\mathfrak{gl}_k(\mathbb{R})=\operatorname{End}(\mathbb{R}^k)$", as $F_\nabla=dA+\tfrac12[A\wedge A]$ (his equation (20)). The two are the same statement because of the identity $[A\wedge A]=2\,A\wedge A$ proved here. The factor $\tfrac12$ in (20) is exactly the factor $2$ produced by the bracket; the series convention writes the principal-bundle structure equation with the bracket and the $\tfrac12$, so that it makes sense for a non-matrix Lie algebra, and reduces to the matrix wedge form in the matrix case. See [[Def - Curvature of a Vector-Bundle Connection]] and [[Thm - Local Formula for the Curvature of a Connection]].

![[Def - The Pauli Matrices#The Definition]]

The **[[Def - The Pauli Matrices|Pauli matrices]]** are the three Hermitian, trace-free $2\times 2$ complex matrices
$$\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \sigma_2=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$
The only algebraic facts used below are the two products $\sigma_1\sigma_2=i\sigma_3$ and $\sigma_2\sigma_1=-i\sigma_3$, whence the commutator $[\sigma_1,\sigma_2]=2i\sigma_3$.

---

# Convergent Strategy

**Problem class.** This is an *identity between two bilinear operations on forms*, of the simplest kind: both sides are $\mathbb{R}$-bilinear (indeed $C^\infty(M)$-bilinear) in their arguments and both are values of $\mathfrak{g}$-valued $2$-forms, so it suffices to check the identity after evaluating on an arbitrary ordered pair of vector fields $(X,Y)$. A $2$-form is determined by its values on pairs of vector fields; hence "prove two $\mathfrak{g}$-valued $2$-forms are equal" reduces to "prove their evaluations on every $(X,Y)$ agree." Everything is then a finite manipulation of the four matrix products $A(X)B(Y),\,A(Y)B(X),\,B(X)A(Y),\,B(Y)A(X)$.

**Assumption pattern.** The only hypothesis that matters is that $\mathfrak{g}$ is a *matrix* algebra, so that the bracket is the commutator $[\xi,\zeta]=\xi\zeta-\zeta\xi$ of an associative product. This is what lets us expand $[A(X),B(Y)]$ into $A(X)B(Y)-B(Y)A(X)$ and recognise the resulting monomials as pieces of the matrix wedges $A\wedge B$ and $B\wedge A$. For a Lie algebra that is not given as matrices the second identity has no content, because the matrix wedge $A\wedge A$ is not even defined.

**Theorem routing.** The route is a single evaluation followed by bookkeeping. Evaluate $[A\wedge B]$ on $(X,Y)$ using the point-values formula from [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|the definition of the bracket]]; expand each commutator into a difference of matrix products; then recognise the four resulting monomials as exactly $(A\wedge B)(X,Y)+(B\wedge A)(X,Y)$, again by [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|the definition of the matrix wedge]]. Setting $B=A$ in the identity gives $[A\wedge A]=2\,A\wedge A$ with no further work. The concrete computation is then a direct expansion of a wedge of two matrix-valued $1$-forms on $\mathbb{R}^2$, using $dx\wedge dx=dy\wedge dy=0$ and $dy\wedge dx=-\,dx\wedge dy$.

**Key decision point.** The one thing to get right is the *ordering* of matrix factors, since matrix multiplication does not commute. The whole content of the identity is that the antisymmetrisation performed by the wedge over the two slots, together with the non-commutativity of the coefficient matrices, produces precisely the commutator: on the diagonal $B=A$ one finds $(A\wedge A)(X,Y)=A(X)A(Y)-A(Y)A(X)=[A(X),A(Y)]$, which is generally non-zero even though the wedge of a scalar $1$-form with itself vanishes. Keeping the matrix factors in order throughout is the entire discipline of the proof.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory IV — Connections and Curvature on Principal Bundles#Legal Operations|the topic page's Legal Operations]]:

1. **Reduce an identity of $\mathfrak{g}$-valued forms to its point-values.** To prove two $\mathfrak{g}$-valued $q$-forms equal, evaluate both on an arbitrary ordered $q$-tuple of vector fields; equality of the resulting $\mathfrak{g}$-valued functions for all tuples is equality of the forms. Here $q=2$ and the tuple is $(X,Y)$.

2. **Expand a commutator of a matrix algebra into its associative products.** Replace $[\xi,\zeta]$ by $\xi\zeta-\zeta\xi$, valid because $\mathfrak{g}$ is realised inside an associative matrix algebra.

3. **Read matrix monomials back as wedge-product point-values.** Recognise a signed sum such as $A(X)B(Y)-A(Y)B(X)$ as $(A\wedge B)(X,Y)$, using the point-values formula for the matrix wedge of two $1$-forms.

4. **Specialise a bilinear identity to the diagonal.** Substitute $B=A$ into the proven bilinear identity to obtain the quadratic one; this is legitimate because both sides are honest bilinear expressions in $(A,B)$.

5. **Expand a wedge of matrix-valued $1$-forms in a coordinate coframe.** Multiply out $(\sigma_1\,dx+\sigma_2\,dy)\wedge(\sigma_1\,dx+\sigma_2\,dy)$, keeping the matrix factors ordered and using $dx\wedge dx=dy\wedge dy=0$, $dy\wedge dx=-\,dx\wedge dy$.

---

# Hints

> [!note]- Hint 1
> A $\mathfrak{g}$-valued $2$-form is determined by what it does to a pair of vector fields. So do not try to manipulate $[A\wedge B]$ symbolically; instead feed it a general ordered pair $(X,Y)$ and use the definition $[A\wedge B](X,Y)=[A(X),B(Y)]-[A(Y),B(X)]$.

> [!note]- Hint 2
> Now use that $\mathfrak{g}$ is a matrix algebra: $[\,\cdot\,,\,\cdot\,]$ is the commutator, so every bracket $[\,\xi,\zeta\,]$ becomes $\xi\zeta-\zeta\xi$ of matrices. Expand both commutators. You will have four matrix monomials with signs.

> [!note]- Hint 3
> Group the four monomials. Two of them, $A(X)B(Y)-A(Y)B(X)$, are exactly $(A\wedge B)(X,Y)$. The other two, $B(X)A(Y)-B(Y)A(X)$, are exactly $(B\wedge A)(X,Y)$. Reassemble to read off $[A\wedge B]=A\wedge B+B\wedge A$, then set $B=A$.

> [!note]- Hint 4
> For the example, remember matrix factors do not commute, so $A\wedge A$ need *not* vanish. In $(\sigma_1\,dx+\sigma_2\,dy)\wedge(\sigma_1\,dx+\sigma_2\,dy)$ the surviving terms are the cross terms $dx\wedge dy$; their coefficient is $\sigma_1\sigma_2-\sigma_2\sigma_1=[\sigma_1,\sigma_2]=2i\sigma_3$. Do the same for the bracket and compare.

---

# Solution

The identity is proved once and for all by evaluating on a pair of vector fields and expanding the commutator; the quadratic form is the diagonal special case; and the numerical example is a two-line wedge expansion that makes the factor $2$ visible as the commutator $[\sigma_1,\sigma_2]$. Throughout, $X,Y$ are smooth vector fields on $M$, and all products of the matrices $A(X),A(Y),B(X),B(Y)\in\mathfrak{g}$ are ordinary matrix products, kept in order because $\mathfrak{g}$ is non-commutative.

**Step 1: Evaluate the bracket on a pair of vector fields.**

Applying the point-values formula for the bracket of two $\mathfrak{g}$-valued $1$-forms turns the left-hand side into a difference of two matrix commutators.

> [!note]- Derivation
> Fix smooth vector fields $X,Y$ on $M$. By the definition of the bracket of $\mathfrak{g}$-valued $1$-forms, evaluated on $(X,Y)$,
> $$[A\wedge B](X,Y)=[A(X),B(Y)]-[A(Y),B(X)]\qquad\text{(definition of }[\,\cdot\wedge\cdot\,]\text{ on }1\text{-forms).}$$
> Because $\mathfrak{g}\subseteq\mathfrak{gl}_k(\mathbb{K})$ is a matrix Lie algebra, each bracket is the commutator of the associative matrix product:
> $$[A(X),B(Y)]=A(X)B(Y)-B(Y)A(X),\qquad [A(Y),B(X)]=A(Y)B(X)-B(X)A(Y)\qquad\text{(}[\xi,\zeta]=\xi\zeta-\zeta\xi\text{).}$$
> Substituting,
> $$[A\wedge B](X,Y)=A(X)B(Y)-B(Y)A(X)-A(Y)B(X)+B(X)A(Y)\qquad\text{(combining the two lines).}$$

**Step 2: Recognise the four monomials as two matrix wedges.**

The four ordered matrix products regroup into the point-values of $A\wedge B$ and of $B\wedge A$.

> [!note]- Derivation
> Reorder the four terms of Step 1, keeping every matrix product intact:
> $$[A\wedge B](X,Y)=\big(A(X)B(Y)-A(Y)B(X)\big)+\big(B(X)A(Y)-B(Y)A(X)\big).$$
> By the point-values formula for the matrix wedge of two $1$-forms, the first grouped pair is
> $$A(X)B(Y)-A(Y)B(X)=(A\wedge B)(X,Y)\qquad\text{(definition of the matrix wedge }A\wedge B\text{),}$$
> and the second grouped pair is, applying the same formula with the roles of $A$ and $B$ exchanged,
> $$B(X)A(Y)-B(Y)A(X)=(B\wedge A)(X,Y)\qquad\text{(definition of the matrix wedge }B\wedge A\text{).}$$
> Therefore
> $$[A\wedge B](X,Y)=(A\wedge B)(X,Y)+(B\wedge A)(X,Y)=\big(A\wedge B+B\wedge A\big)(X,Y).$$
> Since $X,Y$ were arbitrary and a $\mathfrak{g}$-valued $2$-form is determined by its values on pairs of vector fields, the two forms are equal:
> $$[A\wedge B]=A\wedge B+B\wedge A.$$

**Step 3: Specialise to the diagonal to get the quadratic identity.**

Setting $B=A$ collapses the two matrix wedges into one and produces the factor $2$.

> [!note]- Derivation
> Both sides of the identity of Step 2 are bilinear in the pair $(A,B)$, so we may substitute $B=A$:
> $$[A\wedge A]=A\wedge A+A\wedge A=2\,A\wedge A\qquad\text{(setting }B=A\text{ in }[A\wedge B]=A\wedge B+B\wedge A\text{).}$$
> It is worth noting explicitly that $A\wedge A\neq 0$ in general, unlike the wedge $\omega\wedge\omega=0$ of an ordinary $1$-form with itself: evaluating on $(X,Y)$,
> $$(A\wedge A)(X,Y)=A(X)A(Y)-A(Y)A(X)=[A(X),A(Y)],$$
> which is the commutator of two matrices and need not vanish. The non-vanishing of $A\wedge A$ is exactly the non-commutativity that makes the curvature of a non-abelian connection non-linear in $A$.

**Step 4: Verify the quadratic identity on the explicit form $A=\sigma_1\,dx+\sigma_2\,dy$.**

A direct expansion of $A\wedge A$ and of $[A\wedge A]$ on $\mathbb{R}^2$ gives $A\wedge A=2i\sigma_3\,dx\wedge dy$ and $[A\wedge A]=4i\sigma_3\,dx\wedge dy$, confirming the ratio $2$.

> [!note]- Derivation
> Write $A=\sigma_1\,dx+\sigma_2\,dy$, with $\sigma_1,\sigma_2$ *constant* matrices and $dx,dy$ the coordinate $1$-forms on $\mathbb{R}^2$. For constant coefficient matrices the wedge distributes over the four products, and since the matrices are constant they simply multiply:
> $$A\wedge A=(\sigma_1\,dx+\sigma_2\,dy)\wedge(\sigma_1\,dx+\sigma_2\,dy)=\sigma_1\sigma_1\,dx\wedge dx+\sigma_1\sigma_2\,dx\wedge dy+\sigma_2\sigma_1\,dy\wedge dx+\sigma_2\sigma_2\,dy\wedge dy.$$
> Using $dx\wedge dx=0$, $dy\wedge dy=0$, and $dy\wedge dx=-\,dx\wedge dy$ (antisymmetry of the wedge on $1$-forms),
> $$A\wedge A=\sigma_1\sigma_2\,dx\wedge dy-\sigma_2\sigma_1\,dx\wedge dy=(\sigma_1\sigma_2-\sigma_2\sigma_1)\,dx\wedge dy=[\sigma_1,\sigma_2]\,dx\wedge dy\qquad\text{(collecting the cross terms).}$$
> From the Pauli products $\sigma_1\sigma_2=i\sigma_3$ and $\sigma_2\sigma_1=-i\sigma_3$ we get $[\sigma_1,\sigma_2]=2i\sigma_3$, so
> $$A\wedge A=2i\sigma_3\,dx\wedge dy.$$
> Now the bracket. By the same distribution, with each product of coefficient matrices replaced by their commutator,
> $$[A\wedge A]=[\sigma_1,\sigma_1]\,dx\wedge dx+[\sigma_1,\sigma_2]\,dx\wedge dy+[\sigma_2,\sigma_1]\,dy\wedge dx+[\sigma_2,\sigma_2]\,dy\wedge dy.$$
> Here $[\sigma_1,\sigma_1]=0$ and $[\sigma_2,\sigma_2]=0$ kill the first and last terms; using $dy\wedge dx=-\,dx\wedge dy$ and $[\sigma_2,\sigma_1]=-[\sigma_1,\sigma_2]$ in the third term,
> $$[\sigma_2,\sigma_1]\,dy\wedge dx=(-[\sigma_1,\sigma_2])(-\,dx\wedge dy)=[\sigma_1,\sigma_2]\,dx\wedge dy,$$
> so the two surviving terms coincide and
> $$[A\wedge A]=2[\sigma_1,\sigma_2]\,dx\wedge dy=2\cdot 2i\sigma_3\,dx\wedge dy=4i\sigma_3\,dx\wedge dy.$$
> Comparing, $[A\wedge A]=4i\sigma_3\,dx\wedge dy=2\big(2i\sigma_3\,dx\wedge dy\big)=2\,A\wedge A$, exactly as the general identity of Step 3 predicts.

> [!note]- Complete formal solution
> **Claim.** For matrix-valued $1$-forms $A,B\in\Omega^1(M;\mathfrak{g})$ with $\mathfrak{g}\subseteq\mathfrak{gl}_k(\mathbb{K})$ a matrix Lie algebra, $[A\wedge B]=A\wedge B+B\wedge A$ and hence $[A\wedge A]=2\,A\wedge A$; moreover for $A=\sigma_1\,dx+\sigma_2\,dy$ on $\mathbb{R}^2$ one has $A\wedge A=2i\sigma_3\,dx\wedge dy$ and $[A\wedge A]=4i\sigma_3\,dx\wedge dy$.
>
> Let $X,Y$ be smooth vector fields on $M$. By the definition of the bracket of $\mathfrak{g}$-valued $1$-forms and the fact that $\mathfrak{g}$ is a matrix algebra (so $[\xi,\zeta]=\xi\zeta-\zeta\xi$),
> $$[A\wedge B](X,Y)=[A(X),B(Y)]-[A(Y),B(X)]=A(X)B(Y)-B(Y)A(X)-A(Y)B(X)+B(X)A(Y).$$
> Regrouping and applying the point-values formula $(\alpha\wedge\beta)(X,Y)=\alpha(X)\beta(Y)-\alpha(Y)\beta(X)$ for the matrix wedge,
> $$[A\wedge B](X,Y)=\big(A(X)B(Y)-A(Y)B(X)\big)+\big(B(X)A(Y)-B(Y)A(X)\big)=(A\wedge B)(X,Y)+(B\wedge A)(X,Y).$$
> As $X,Y$ were arbitrary and a $2$-form is determined by its values on pairs of vector fields, $[A\wedge B]=A\wedge B+B\wedge A$. Setting $B=A$ (both sides bilinear in $(A,B)$) gives $[A\wedge A]=2\,A\wedge A$.
>
> For $A=\sigma_1\,dx+\sigma_2\,dy$ with $\sigma_1,\sigma_2$ constant, expanding the matrix wedge and using $dx\wedge dx=dy\wedge dy=0$, $dy\wedge dx=-\,dx\wedge dy$,
> $$A\wedge A=(\sigma_1\sigma_2-\sigma_2\sigma_1)\,dx\wedge dy=[\sigma_1,\sigma_2]\,dx\wedge dy=2i\sigma_3\,dx\wedge dy,$$
> since $\sigma_1\sigma_2=i\sigma_3$, $\sigma_2\sigma_1=-i\sigma_3$. Expanding the bracket the same way, the diagonal terms vanish and the two cross terms coincide, giving $[A\wedge A]=2[\sigma_1,\sigma_2]\,dx\wedge dy=4i\sigma_3\,dx\wedge dy=2\,A\wedge A$. $\blacksquare$

> [!warning] Illegal but tempting: assuming $A\wedge A=0$
> For an *ordinary* (scalar-valued) $1$-form $\omega$ one has $\omega\wedge\omega=0$, and it is tempting to carry this over and conclude $A\wedge A=0$, which would make both identities collapse to $[A\wedge A]=0=2\cdot 0$. This is false for matrix-valued forms: $(A\wedge A)(X,Y)=[A(X),A(Y)]$, a commutator that vanishes only when the matrices $A(X)$ and $A(Y)$ commute. The scalar rule $\omega\wedge\omega=0$ relies on the commutativity of the coefficient ring; the extra condition that would restore it is that $\mathfrak{g}$ be *abelian* (for instance $\mathfrak{g}=\mathfrak{u}(1)=i\mathbb{R}$), in which case every bracket is zero and indeed $A\wedge A=0$. The example $A=\sigma_1\,dx+\sigma_2\,dy$ has $A\wedge A=2i\sigma_3\,dx\wedge dy\neq 0$ precisely because $\sigma_1$ and $\sigma_2$ do not commute.

**Independent sanity check.** Take the trace of the example. Both $A\wedge A=2i\sigma_3\,dx\wedge dy$ and $[A\wedge A]=4i\sigma_3\,dx\wedge dy$ are multiples of $\sigma_3$, and $\operatorname{tr}\sigma_3=0$, so $\operatorname{tr}(A\wedge A)=\operatorname{tr}[A\wedge A]=0$. This is consistent with the general fact that the trace of any bracket vanishes, $\operatorname{tr}[\xi,\zeta]=\operatorname{tr}(\xi\zeta)-\operatorname{tr}(\zeta\xi)=0$, so that $\operatorname{tr}[A\wedge A]=0$ identically; the identity $[A\wedge A]=2\,A\wedge A$ then also forces $\operatorname{tr}(A\wedge A)=0$, matching the direct computation.

---

# Key Takeaways

**The bracket of $\mathfrak{g}$-valued forms and their matrix wedge are the same operation up to a symmetrisation, and the factor is the degree count.** The identity $[A\wedge B]=A\wedge B+B\wedge A$ for $1$-forms is the visible face of a general principle: for matrix-valued forms the Lie bracket $[\alpha\wedge\beta]$ is the graded commutator $\alpha\wedge\beta-(-1)^{pq}\beta\wedge\alpha$ of the associative matrix wedge, and on the diagonal $\alpha=\beta$ of two $1$-forms the two contributions add rather than cancel because $(-1)^{1\cdot 1}=-1$ makes the graded commutator a graded *anticommutator*. The trigger for reaching for this identity is any place where a formula is written once with a bracket-and-$\tfrac12$ and once with a bare wedge: whenever you see $\tfrac12[A\wedge A]$ next to $A\wedge A$, they are equal, and the $\tfrac12$ is bookkeeping for the factor $2$ that the antisymmetrisation over the two form-slots produces. The transferable diagnostic is to remember that the factor is not universal — it is $2$ for two $1$-forms, and in general the sign $(-1)^{pq}$ and the parity of $\alpha,\beta$ decide whether the two terms add or cancel.

**Non-commutativity of the coefficient algebra is what makes gauge theory non-linear, and $A\wedge A$ is where it enters.** For an abelian structure group the curvature $F=dA+\tfrac12[A\wedge A]=dA$ is linear in the potential $A$, which is why electromagnetism ($\mathfrak{g}=\mathfrak{u}(1)$) is a linear theory; for a non-abelian group the term $\tfrac12[A\wedge A]=A\wedge A$ is a genuine quadratic self-interaction of the gauge field, and it is non-zero exactly because $(A\wedge A)(X,Y)=[A(X),A(Y)]$ is a commutator of matrices. This exercise isolates that quadratic term in the cleanest possible setting. The reusable principle: whenever a construction with $\mathfrak{g}$-valued forms behaves linearly for abelian $\mathfrak{g}$ and non-linearly otherwise, the non-linearity is carried by wedge-products of the form with itself, and its size is governed by commutators $[A(X),A(Y)]$ of the pointwise matrices. Recognising this tells you immediately, for example, why the Yang–Mills equations are non-linear while Maxwell's are not.

**To prove an identity of vector-valued forms, evaluate on vector fields and let the point-values do the algebra.** The proof never manipulated the forms $A,B$ as abstract objects; it evaluated once on a general pair $(X,Y)$, expanded, and reassembled. This is the standard and almost always fastest route to any identity among $\mathfrak{g}$-valued forms — graded antisymmetry $[\alpha\wedge\beta]=-(-1)^{pq}[\beta\wedge\alpha]$, the graded Leibniz rule $d[\alpha\wedge\beta]=[d\alpha\wedge\beta]+(-1)^p[\alpha\wedge d\beta]$, and the graded Jacobi identity all fall out of the same evaluate-and-expand discipline, reduced to decomposable forms $\omega\otimes\xi$ when the degrees are higher. The trigger is any claimed equality of two form-valued expressions; the diagnostic is that both sides are multilinear and alternating in their vector-field arguments, so checking on an arbitrary tuple of vector fields is not a special case but a complete proof. The companion exercise [[Ex - The Maurer-Cartan Form of U(1) and of SU(2)]] uses the same $[\theta\wedge\theta](X,Y)=2[\theta(X),\theta(Y)]$ computation to turn the Maurer–Cartan equation into a statement about the structure constants of $\mathfrak{su}(2)$.

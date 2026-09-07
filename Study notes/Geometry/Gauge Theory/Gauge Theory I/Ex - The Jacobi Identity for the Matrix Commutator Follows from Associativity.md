---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Lie Subalgebra and Abelian Lie Algebra"
  - "Def - Lie Algebra"
tags: [geometry, gauge-theory, lie-algebras]
---

# Problem Statement

Let $\mathbb{K}$ be either $\mathbb{R}$ or $\mathbb{C}$, and let $\operatorname{Mat}(n\times n;\mathbb{K})$ be the associative algebra of $n\times n$ matrices over $\mathbb{K}$ with the usual matrix product. Define the **commutator** bracket
$$[A,B]:=AB-BA\qquad(A,B\in\operatorname{Mat}(n\times n;\mathbb{K})).$$
Show that this bracket satisfies the **Jacobi identity**
$$[[A,B],C]+[[B,C],A]+[[C,A],B]=0\qquad\text{for all }A,B,C\in\operatorname{Mat}(n\times n;\mathbb{K}),$$
by expanding the twelve terms and observing that they cancel in pairs. Trace the cancellation to a single structural fact: the **associativity** of matrix multiplication, $(AB)C=A(BC)$. Together with the (already routine) bilinearity and antisymmetry of the commutator, this makes $(\operatorname{Mat}(n\times n;\mathbb{K}),[\cdot,\cdot])$ a Lie algebra, denoted $\mathfrak{gl}(n;\mathbb{K})$.

This is source item **B-E1.2.2** (Bär–Wernli, Example 1.2.2.2, p. 10), written out in full: the source performs the same expansion but records the intermediate line only as "$=0$".

**Recall:**

The three axioms a bracket must satisfy to make a vector space a Lie algebra are restated on the definition page for this section; the identity in question is axiom (iii).

![[Def - Lie Subalgebra and Abelian Lie Algebra#The Definition]]

A **[[Def - Lie Algebra|Lie algebra]]** is a vector space $V$ over $\mathbb{K}$ equipped with a map $[\cdot,\cdot]:V\times V\to V$ that is (i) **bilinear**: linear in each argument separately; (ii) **antisymmetric**: $[v,w]=-[w,v]$ for all $v,w\in V$ (Bär's Definition 1.2.1 misprints this as "$[v,w]=-[v,w]$"; the intended and standard form, used throughout the series, is $[v,w]=-[w,v]$); and (iii) satisfies the **Jacobi identity** $[[u,v],w]+[[v,w],u]+[[w,u],v]=0$ for all $u,v,w\in V$. The set $\operatorname{Mat}(n\times n;\mathbb{K})$ is a vector space of dimension $n^2$ over $\mathbb{K}$, and the commutator $[A,B]=AB-BA$ is manifestly bilinear (matrix multiplication distributes over addition and commutes with scalars) and antisymmetric ($[B,A]=BA-AB=-[A,B]$); the content of this exercise is axiom (iii).

The one structural property we shall lean on is **associativity** of the matrix product: for all matrices, $(AB)C=A(BC)$, so that a threefold product $ABC$ is unambiguous and may be regrouped freely.

---

# Convergent Strategy

**Problem class.** This is a *verify-an-algebraic-identity* problem of the simplest computational kind: both sides are polynomial expressions in the entries of $A,B,C$, and the identity is proved by expanding one side into monomials and matching them against zero. There is no case split, no choice of auxiliary object, and no appeal to the size $n$ or the field $\mathbb{K}$ — the argument is uniform in both. The only subtlety is bookkeeping: the left-hand side expands into twelve threefold products, and the claim is that they cancel in six opposite pairs.

**Assumption pattern.** The single hypothesis that does any work is associativity. It is what licenses writing each of the twelve terms as an *unbracketed* threefold product such as $ABC$ (rather than $(AB)C$ or $A(BC)$, which associativity makes equal), so that two terms count as "the same monomial" precisely when they are the same ordered product of the three letters. Without associativity the twelve products would live in different regrouped forms and could not be identified, and the Jacobi identity would fail — which is exactly Bär's Remark 1.2.1 that "the Jacobi identity can be thought of as a replacement for associativity."

**Theorem routing.** The route is entirely mechanical: (1) expand each inner commutator, e.g. $[A,B]=AB-BA$; (2) substitute into the outer commutator, e.g. $[[A,B],C]=(AB-BA)C-C(AB-BA)$; (3) use associativity and the distributive law to write every product as one of the six ordered monomials $ABC,ACB,BAC,BCA,CAB,CBA$, each with a sign; (4) collect the three expanded brackets and check that every monomial appears exactly twice, once with each sign. No external theorem is invoked. The general principle behind the routing — *every associative algebra is a Lie algebra under its commutator* — is recorded in the Key Takeaways.

**Key decision point.** The only decision is *how to organise the twelve terms so the cancellation is visible rather than asserted*. The efficient organisation is to fix the alphabet order $A,B,C$ once, expand the three brackets in the same left-to-right convention, and read off which two of the twelve terms carry each of the six monomials. The non-obvious observation — the one that turns a page of algebra into a one-line reason — is that the *cyclic* symmetry of the sum ($A\to B\to C\to A$) forces each monomial and its reverse to appear with opposite signs, so the check reduces to confirming one representative pair and invoking the symmetry for the rest. We nonetheless write all six pairs out, because the series proof standard forbids "by symmetry" as a substitute for the parallel cases.

---

# Legal Operations Used

This solution deploys, in the language of the section's topic page, the following operations (named descriptively here; the topic page will fix their numbering):

1. **Unfold a nested bracket by its definition.** Replace each occurrence of $[\,\cdot\,,\,\cdot\,]$ by the difference $XY-YX$ of the two matrix products, innermost bracket first, then the outer bracket. This converts the whole left-hand side into a $\pm$-signed sum of matrix products.

2. **Regroup a threefold product using associativity.** Treat $(XY)Z$ and $X(YZ)$ as the single unbracketed monomial $XYZ$. This is the operation that makes two of the twelve terms recognisably equal, and it is the *only* place the ring structure enters.

3. **Distribute a product over a difference.** Use $X(Y-Z)=XY-XZ$ and $(Y-Z)X=YX-ZX$ to expand each of the six outer products $(\text{difference})\cdot(\text{matrix})$ into two monomials.

4. **Collect like monomials and cancel opposite signs.** Group the twelve resulting monomials by their ordered letter string; each of the six strings occurs once with $+$ and once with $-$, so every pair sums to the zero matrix.

5. **Verify the remaining Lie-algebra axioms directly.** Bilinearity and antisymmetry of the commutator are checked from the vector-space structure and the definition, completing the verification that $\mathfrak{gl}(n;\mathbb{K})$ is a Lie algebra.

---

# Hints

> [!note]- Hint 1
> Do not try to prove the identity abstractly. Just expand. Start with the first term alone: $[[A,B],C]$. Replace the inner bracket, then the outer one, and write the result as four separate matrix products with signs. How many of the three-letter products $ABC,ACB,\dots$ appear, and with what signs?

> [!note]- Hint 2
> $[[A,B],C]=(AB-BA)C-C(AB-BA)=ABC-BAC-CAB+CBA$, using that $(AB)C=ABC$ and so on by associativity. Now do the same for $[[B,C],A]$ and $[[C,A],B]$, keeping the same left-to-right expansion each time. You will produce twelve monomials in total.

> [!note]- Hint 3
> Lay the twelve monomials out and sort them by their letter string. There are exactly six distinct strings — $ABC,ACB,BAC,BCA,CAB,CBA$ — and each appears twice. Check that the two appearances of each string carry opposite signs.

> [!note]- Hint 4
> The reason each string appears with both signs is the cyclic structure of the sum. Under the relabelling $A\to B\to C\to A$, the first bracket becomes the second and the second becomes the third; the term $+ABC$ produced by the first bracket is matched by the term $-ABC$ produced by the third. The only ingredient that let you *write* both as the same $ABC$ (rather than as differently-parenthesised expressions) was associativity — which is the whole point.

---

# Solution

The proof is a single expansion. We unfold the three doubly-nested commutators into twelve matrix products, use associativity to write each as an unbracketed three-letter monomial, and observe that the six possible monomials each occur exactly twice with opposite signs, so the total is the zero matrix. Associativity is used precisely at the step where $(XY)Z$ and $X(YZ)$ are identified; it is the one hypothesis carrying the identity.

**Step 1: Expand the first bracket $[[A,B],C]$ into four monomials.**

Unfolding the inner and then the outer commutator gives
$$[[A,B],C]=ABC-BAC-CAB+CBA.$$

> [!note]- Derivation
> We must show $[[A,B],C]+[[B,C],A]+[[C,A],B]=0$. Begin with the first summand. By the **definition of the commutator** applied to the inner bracket, $[A,B]=AB-BA$. Applying it to the outer bracket,
> $$[[A,B],C]=[A,B]\,C-C\,[A,B]=(AB-BA)C-C(AB-BA)\qquad\text{(definition of }[\cdot,C]\text{)}.$$
> **Distribute over the differences** (operation 3):
> $$=(AB)C-(BA)C-C(AB)+C(BA)\qquad\text{(distributive law).}$$
> **Regroup by associativity** (operation 2), writing each threefold product as an unbracketed monomial:
> $$=ABC-BAC-CAB+CBA\qquad\text{(since }(XY)Z=X(YZ)=XYZ\text{).}$$
> This is four of the twelve monomials.

**Step 2: Expand the second and third brackets by the same procedure.**

The identical computation, with the letters cyclically permuted $A\to B\to C\to A$, gives
$$[[B,C],A]=BCA-CBA-ABC+ACB,\qquad [[C,A],B]=CAB-ACB-BCA+BAC.$$

> [!note]- Derivation
> For the second bracket, substitute $B,C,A$ for $A,B,C$ in the result of Step 1 (the derivation is line-for-line identical, only the letters change, and every step — definition of the bracket, distribution, associative regrouping — survives the substitution because none of them used any special property of the particular matrices):
> $$[[B,C],A]=BCA-CBA-ABC+ACB.$$
> For the third bracket, substitute $C,A,B$ for $A,B,C$ in the same result:
> $$[[C,A],B]=CAB-ACB-BCA+BAC.$$
> We now have all twelve monomials.

**Step 3: Add the three expansions and cancel in pairs.**

Summing the three lines, every one of the six ordered monomials $ABC,ACB,BAC,BCA,CAB,CBA$ occurs exactly once with a plus sign and once with a minus sign, so the sum is the zero matrix.

> [!note]- Derivation
> **Collect the twelve monomials by letter string** (operation 4). Reading off Steps 1 and 2:
> $$
> \begin{aligned}
> ABC:&\quad +ABC\ (\text{from bracket 1}),\ -ABC\ (\text{from bracket 2});\\
> ACB:&\quad +ACB\ (\text{from bracket 2}),\ -ACB\ (\text{from bracket 3});\\
> BAC:&\quad -BAC\ (\text{from bracket 1}),\ +BAC\ (\text{from bracket 3});\\
> BCA:&\quad +BCA\ (\text{from bracket 2}),\ -BCA\ (\text{from bracket 3});\\
> CAB:&\quad -CAB\ (\text{from bracket 1}),\ +CAB\ (\text{from bracket 3});\\
> CBA:&\quad +CBA\ (\text{from bracket 1}),\ -CBA\ (\text{from bracket 2}).
> \end{aligned}
> $$
> Each of the six rows sums to the zero matrix (the two entries are negatives of one another), and every one of the twelve monomials appears in exactly one row. Therefore
> $$[[A,B],C]+[[B,C],A]+[[C,A],B]=0.$$
> The identification of, for instance, the $+ABC$ from bracket 1 with the $-ABC$ from bracket 2 is legitimate **only because associativity let us write both as the same monomial $ABC$**; this is where and how the hypothesis is used.

**Step 4: Assemble the Lie-algebra axioms.**

With the Jacobi identity in hand, $(\operatorname{Mat}(n\times n;\mathbb{K}),[\cdot,\cdot])$ satisfies all three Lie-algebra axioms and is therefore the Lie algebra $\mathfrak{gl}(n;\mathbb{K})$.

> [!note]- Derivation
> **Bilinearity.** For scalars $\lambda,\mu\in\mathbb{K}$ and matrices $A,A',B$,
> $$[\lambda A+\mu A',B]=(\lambda A+\mu A')B-B(\lambda A+\mu A')=\lambda(AB-BA)+\mu(A'B-BA')=\lambda[A,B]+\mu[A',B]$$
> (by distributivity of the matrix product over addition and its commuting with scalar multiplication). For the second argument the same distributive computation applies verbatim on the other side:
> $$[A,\lambda B+\mu B']=A(\lambda B+\mu B')-(\lambda B+\mu B')A=\lambda(AB-BA)+\mu(AB'-B'A)=\lambda[A,B]+\mu[A,B']$$
> (again by distributivity and scalar-homogeneity of the matrix product), so the bracket is linear in each argument separately. **Antisymmetry.** $[B,A]=BA-AB=-(AB-BA)=-[A,B]$. **Jacobi identity.** Proved in Steps 1–3. All three axioms hold, so the commutator makes $\operatorname{Mat}(n\times n;\mathbb{K})$ a Lie algebra. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** On $\operatorname{Mat}(n\times n;\mathbb{K})$ the commutator $[A,B]=AB-BA$ satisfies the Jacobi identity, and hence, being also bilinear and antisymmetric, makes $\operatorname{Mat}(n\times n;\mathbb{K})$ a Lie algebra.
>
> Fix $A,B,C\in\operatorname{Mat}(n\times n;\mathbb{K})$. Unfolding each inner and outer commutator by its definition, distributing over the differences, and regrouping each threefold product as an unbracketed monomial using the associativity $(XY)Z=X(YZ)$, we obtain
> $$
> \begin{aligned}
> [[A,B],C]&=ABC-BAC-CAB+CBA,\\
> [[B,C],A]&=BCA-CBA-ABC+ACB,\\
> [[C,A],B]&=CAB-ACB-BCA+BAC.
> \end{aligned}
> $$
> Adding the three lines, each of the six ordered products $ABC,ACB,BAC,BCA,CAB,CBA$ occurs once with a $+$ sign and once with a $-$ sign; every pair cancels, so
> $$[[A,B],C]+[[B,C],A]+[[C,A],B]=0.$$
> Bilinearity follows from the distributive law and scalar-homogeneity of matrix multiplication, and antisymmetry from $[B,A]=BA-AB=-[A,B]$. Hence the commutator satisfies all three Lie-algebra axioms, and $(\operatorname{Mat}(n\times n;\mathbb{K}),[\cdot,\cdot])=\mathfrak{gl}(n;\mathbb{K})$ is a Lie algebra. $\blacksquare$

> [!tip]- Calibration on the smallest case $n=1$ and a $2\times 2$ check
> For $n=1$ the matrices are scalars, multiplication is commutative, every commutator is $0$, and the Jacobi identity reads $0+0+0=0$ — trivially true, and a reminder that the identity carries no information until the algebra is noncommutative. For a genuine test take $n=2$ with $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$, $C=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ (a basis-flavoured triple in $\mathfrak{sl}(2;\mathbb{R})$). One computes $[A,B]=C$, so $[[A,B],C]=[C,C]=0$; $[B,C]=2B$, so $[[B,C],A]=[2B,A]=2[B,A]=-2C$; $[C,A]=2A$, so $[[C,A],B]=[2A,B]=2C$. The sum is $0-2C+2C=0$, confirming the identity on a noncommutative instance.

---

# Key Takeaways

**Every associative algebra becomes a Lie algebra under its commutator, and this exercise is the proof.** The computation used nothing specific to matrices beyond the three ring axioms in play: the distributive law, the compatibility of scalars, and — decisively — associativity. Replace $\operatorname{Mat}(n\times n;\mathbb{K})$ by any associative $\mathbb{K}$-algebra $\mathcal{A}$ (bounded operators on a Hilbert space, the algebra of differential operators, a group algebra, the smooth functions under pointwise product) and the identical twelve-term cancellation proves that $[a,b]=ab-ba$ makes $\mathcal{A}$ a Lie algebra. This is the single most common way Lie algebras arise, and the recognisable trigger is: whenever you meet an associative product and want a *bracket* structure — for infinitesimal symmetries, for a quantum commutator, for the tangent algebra of a matrix group — reach for the commutator, and its Jacobi identity is free. The general functor $\mathcal{A}\rightsquigarrow\mathcal{A}^{\mathrm{Lie}}$ this defines is the left adjoint's counterpart to the universal enveloping algebra.

**Associativity *is* the Jacobi identity, transposed.** The cancellation in Step 3 was not an accident of arithmetic; it happened because $(XY)Z$ and $X(YZ)$ are the same monomial. Bär's Remark 1.2.1 phrases the moral as "the Jacobi identity can be thought of as a replacement for associativity," and this exercise is the precise sense in which that is true: the associativity of a product is exactly what is needed to make the commutator's Jacobi identity hold, and a Lie bracket that does not come from an associative product must impose Jacobi as a *separate* axiom because it has no associativity to inherit it from. When a bracket is defined by a formula with no underlying associative multiplication — the cross product on $\mathbb{R}^3$, the bracket of vector fields — the Jacobi identity becomes a genuine theorem requiring its own argument, and each such argument is, in disguise, a recovery of the associativity that the direct definition lacks.

**The matrix-commutator Jacobi identity is a special case of the Jacobi identity for vector fields.** Associate to each matrix $A\in\operatorname{Mat}(n\times n;\mathbb{R})$ the constant-coefficient *linear* vector field $X_A$ on $\mathbb{R}^n$ defined by $X_A(x)=Ax$, whose $i$-th component is $X_A^i(x)=A_{ik}x_k$. A direct computation of the Lie bracket of vector fields gives $[X_A,X_B]^i=X_A^j\,\partial_j X_B^i-X_B^j\,\partial_j X_A^i=A_{jk}x_k B_{ij}-B_{jk}x_k A_{ij}=\big((BA-AB)x\big)_i$, so $[X_A,X_B]=X_{[B,A]}=X_{-[A,B]}$; the assignment $A\mapsto X_A$ is a linear *anti*-isomorphism of $\mathfrak{gl}(n;\mathbb{R})$ onto the linear vector fields. Because the Jacobi identity is insensitive to an overall sign on the bracket (replacing $[\cdot,\cdot]$ by $-[\cdot,\cdot]$ permutes the three cyclic terms without changing their sum), the Jacobi identity for the commutator is equivalent to the Jacobi identity for these vector fields, which is proved once and for all — for *all* smooth vector fields, by the cancellation of second-order derivatives — on **[[Thm - The Space of Vector Fields is a Lie Algebra under the Lie Bracket|the space of vector fields is a Lie algebra]]**. Recognising a matrix bracket as the bracket of the flows $x\mapsto e^{tA}x$ it generates is the first instance of the guiding idea of the whole chapter: a Lie algebra is the infinitesimal shadow of a group of transformations, and its bracket measures the failure of two flows to commute.

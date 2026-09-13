---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Axioms and Properties of Chern Classes"
  - "Def - Chern Classes"
  - "Thm - Trivial Bundles Have Vanishing Characteristic Classes"
  - "Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E\to M$ be a complex vector bundle over a smooth manifold, and suppose that $E$ splits off a trivial summand:
$$E\;\cong\;E_1\oplus\underline{\mathbb C}^{\,k},$$
where $E_1\to M$ is a complex vector bundle and $\underline{\mathbb C}^{\,k}=M\times\mathbb C^k$ is the trivial rank-$k$ complex bundle. Write $r:=\operatorname{rk}E$, so that $\operatorname{rk}E_1=r-k$. Prove that
$$c_j(E)=0\qquad\text{for every }j>r-k=\operatorname{rk}E-k.$$

In words: each trivial summand pushes the top possibly-nonzero Chern class down by one degree. This is part (d) of Haydys's Exercise 88.

The standing normalisation for this chapter (see conventions.md and [[Def - Chern Classes]]) is $c(E)=\big[\det\!\big(\mathbf 1+\tfrac{i}{2\pi}F_A\big)\big]$ for a unitary connection $A$ on a Hermitian structure, with total class $c(E)=1+c_1(E)+\dots+c_r(E)\in H^{\mathrm{even}}_{\mathrm{dR}}(M;\mathbb R)$; $c_0(E)=1$ by convention.

**Recall:**

The result rests on three properties of the total Chern class — the Whitney sum formula, the vanishing of positive-degree characteristic classes of a trivial bundle, and the fact that a rank-$s$ bundle has no Chern classes above degree $s$ — together with the definition of the total class as a determinant.

![[Def - Chern Classes#The Definition]]

![[Thm - Axioms and Properties of Chern Classes#Statement]]

The three clauses we use are, verbatim: **(i)** $c_0(E)=1$ and $c_j(E)=0$ for $j>\operatorname{rk}E$; **(iii)** the Whitney sum formula $c(E_1\oplus E_2)=c(E_1)\smile c(E_2)$, realised on forms as the wedge product of Chern-form representatives; and **(v)** $c(E)$ depends only on the isomorphism class of $E$. Here $\smile$ is the cup product on de Rham cohomology, represented by the wedge product of closed forms.

![[Thm - Trivial Bundles Have Vanishing Characteristic Classes#Statement]]

For the total Chern class this says precisely: if $E$ is trivial and $j\ge1$ then $c_j(E)=0$, so that $c(E)=c_0(E)=1$. (The reason is that the trivial bundle carries the flat product connection, whose curvature is $0$, so $\det(\mathbf 1+\tfrac{i}{2\pi}\cdot 0)=\det(\mathbf 1)=1$.)

The multiplication in the total class is graded by degree: if $\alpha=\sum_p\alpha_p$ and $\beta=\sum_q\beta_q$ with $\alpha_p,\beta_q$ of cohomological degree $2p,2q$, then $(\alpha\smile\beta)_j=\sum_{p+q=j}\alpha_p\smile\beta_q$. The neutral element for $\smile$ is $1\in H^0_{\mathrm{dR}}(M)$, the class of the constant function $1$.

---

# Convergent Strategy

**Problem class.** This is a *degree-bookkeeping* problem: it asks for the vanishing of a graded piece of a product of cohomology classes, purely on grounds of *where each factor lives in the grading*. Problems of this kind never require computing the classes; they require only knowing the top degree in which each factor can be nonzero and then reading off which products can survive in a given total degree. The recognisable signature is a statement of the form "the class $X$ vanishes above degree $d$", to be proved by writing $X$ as a product and counting degrees.

**Assumption pattern.** The hypothesis that the split-off summand is *trivial* — not merely low-rank — is exactly what makes the argument go through, and it is used in one place only: it forces the Chern class of that summand to be the multiplicative identity $1$, which occupies degree $0$ alone and therefore cannot raise the degree of any product it enters. A non-trivial low-rank summand would still cap the degree of *its own* class but would generally contribute nonzero classes in positive degree, and the conclusion would fail (see the warning in the Solution). The trigger for reaching for the trivial-bundle theorem is precisely the appearance of $\underline{\mathbb C}^{\,k}$ as a Whitney summand.

**Theorem routing.** The route is short and forced: replace $E$ by the isomorphic $E_1\oplus\underline{\mathbb C}^{\,k}$ using [[Thm - Axioms and Properties of Chern Classes|isomorphism invariance (clause (v))]]; apply the [[Thm - Axioms and Properties of Chern Classes|Whitney sum formula (clause (iii))]] to get $c(E)=c(E_1)\smile c(\underline{\mathbb C}^{\,k})$; collapse $c(\underline{\mathbb C}^{\,k})=1$ by the [[Thm - Trivial Bundles Have Vanishing Characteristic Classes|trivial-bundle theorem]]; and finally invoke the [[Thm - Axioms and Properties of Chern Classes|degree cap (clause (i))]] on $E_1$, whose rank is $r-k$, to conclude $c_j(E)=c_j(E_1)=0$ for $j>r-k$.

**Key decision point.** The single non-obvious move is recognising that the *only* thing "trivial summand" buys is a factor equal to $1$ in the total class, and that a factor of $1$ is transparent to the grading. Once the product is written as $c(E_1)\smile 1$, the problem has already been reduced to the plain degree cap for $E_1$, whose rank is one $k$ smaller than that of $E$. The temptation to compute curvatures or to argue "there are $k$ trivial directions so the determinant has smaller rank" is unnecessary and, if done carelessly, obscures the fact that the whole content is a single multiplication by $1$.

---

# Legal Operations Used

This solution deploys the following legal operations from the chapter's Legal Operations; where numbering is not yet assigned each operation is named descriptively.

1. **Replace a bundle by an isomorphic one before computing characteristic classes.** Since $c$ depends only on the isomorphism class (clause (v) of [[Thm - Axioms and Properties of Chern Classes|the axioms theorem]]), we may compute $c(E)$ from the concrete model $E_1\oplus\underline{\mathbb C}^{\,k}$.

2. **Factor a Whitney sum's total class as a cup product.** By clause (iii), $c(E_1\oplus\underline{\mathbb C}^{\,k})=c(E_1)\smile c(\underline{\mathbb C}^{\,k})$; this turns a class of a sum into a product of classes.

3. **Collapse the class of a trivial factor to the identity.** By the [[Thm - Trivial Bundles Have Vanishing Characteristic Classes|trivial-bundle theorem]], $c(\underline{\mathbb C}^{\,k})=1$, the unit of the cup product; multiplying by it changes nothing.

4. **Read off vanishing of a graded piece from the degree of the factors.** The degree cap (clause (i)) applied to $E_1$ says $c_j(E_1)=0$ for $j>\operatorname{rk}E_1=r-k$; because $c(E)=c(E_1)$ as graded classes, the same vanishing transfers to $E$.

---

# Hints

> [!note]- Hint 1
> You are asked to show a *total-degree* vanishing. Do not try to compute any Chern class. Instead, use the one structural fact you have about $E$: it is a Whitney sum. What does the total Chern class of a Whitney sum factor into?

> [!note]- Hint 2
> Write $c(E)=c(E_1)\smile c(\underline{\mathbb C}^{\,k})$. The second factor is the total Chern class of a *trivial* bundle. What is the total Chern class of a trivial bundle, and in which cohomological degree does it live?

> [!note]- Hint 3
> A trivial bundle has $c(\underline{\mathbb C}^{\,k})=1$, a class purely in degree $0$. Multiplying by $1$ leaves every graded piece unchanged, so $c_j(E)=c_j(E_1)$ for every $j$. Now, how high can a Chern class of $E_1$ be nonzero, given that $\operatorname{rk}E_1=r-k$?

> [!note]- Hint 4
> By clause (i) of the axioms theorem, $c_j(E_1)=0$ whenever $j>\operatorname{rk}E_1=r-k$: a rank-$(r-k)$ bundle's total Chern class is a determinant of an $(r-k)\times(r-k)$ matrix and has no homogeneous piece of degree exceeding $r-k$. Combine this with $c_j(E)=c_j(E_1)$.

---

# Solution

The proof is three lines of algebra in the graded ring $H^{\mathrm{even}}_{\mathrm{dR}}(M)$: isomorphism invariance lets us compute with the split model; the Whitney sum formula turns the total class into a product; the trivial factor contributes only the unit $1$; and the degree cap on the rank-$(r-k)$ bundle $E_1$ finishes the count. No curvature is ever computed.

**Step 1: Reduce to the split model and factor the total class.**

Isomorphism invariance and the Whitney sum formula give $c(E)=c(E_1)\smile c(\underline{\mathbb C}^{\,k})$.

> [!note]- Derivation
> Suppose $E\cong E_1\oplus\underline{\mathbb C}^{\,k}$ with $r=\operatorname{rk}E$ and hence $\operatorname{rk}E_1=r-k$; we must show $c_j(E)=0$ for $j>r-k$.
>
> By clause **(v)** of [[Thm - Axioms and Properties of Chern Classes|the axioms theorem]] (isomorphism invariance), $c(E)$ depends only on the isomorphism class of $E$, so
> $$c(E)=c\big(E_1\oplus\underline{\mathbb C}^{\,k}\big)\qquad\text{(by clause (v), using }E\cong E_1\oplus\underline{\mathbb C}^{\,k}\text{).}$$
> Now apply clause **(iii)** (the Whitney sum formula) with $E_1$ and $E_2:=\underline{\mathbb C}^{\,k}$:
> $$c\big(E_1\oplus\underline{\mathbb C}^{\,k}\big)=c(E_1)\smile c\big(\underline{\mathbb C}^{\,k}\big)\qquad\text{(by clause (iii)).}$$
> Combining the two displayed lines,
> $$c(E)=c(E_1)\smile c\big(\underline{\mathbb C}^{\,k}\big).$$

**Step 2: The trivial factor is the multiplicative identity.**

The total Chern class of $\underline{\mathbb C}^{\,k}$ equals $1$.

> [!note]- Derivation
> The bundle $\underline{\mathbb C}^{\,k}=M\times\mathbb C^k$ is trivial. By the [[Thm - Trivial Bundles Have Vanishing Characteristic Classes|trivial-bundle theorem]], every characteristic class of a trivial bundle in positive degree vanishes; for the Chern classes this reads $c_j(\underline{\mathbb C}^{\,k})=0$ for all $j\ge1$, hence
> $$c\big(\underline{\mathbb C}^{\,k}\big)=c_0\big(\underline{\mathbb C}^{\,k}\big)=1\qquad\text{(the class of the constant function }1\in H^0_{\mathrm{dR}}(M)\text{).}$$
> Concretely, this is because $\underline{\mathbb C}^{\,k}$ carries the flat product connection, whose curvature $F$ is identically $0$; then, using the determinant form of the total class from [[Def - Chern Classes]],
> $$c\big(\underline{\mathbb C}^{\,k}\big)=\Big[\det\!\Big(\mathbf 1+\tfrac{i}{2\pi}\cdot 0\Big)\Big]=[\det\mathbf 1]=[1]=1.$$

**Step 3: Multiply out and apply the degree cap to $E_1$.**

Since $c(\underline{\mathbb C}^{\,k})=1$, we get $c(E)=c(E_1)$ as graded classes, and the degree cap on the rank-$(r-k)$ bundle $E_1$ gives the claim.

> [!note]- Derivation
> Substituting Step 2 into Step 1, and using that $1\in H^0_{\mathrm{dR}}(M)$ is the neutral element of the cup product ($x\smile 1=x$ for every $x$),
> $$c(E)=c(E_1)\smile 1=c(E_1).$$
> Equality of total classes is equality in each homogeneous degree, so
> $$c_j(E)=c_j(E_1)\qquad\text{for every }j\ge0.$$
> By clause **(i)** of [[Thm - Axioms and Properties of Chern Classes|the axioms theorem]], applied to the bundle $E_1$ of rank $\operatorname{rk}E_1=r-k$,
> $$c_j(E_1)=0\qquad\text{for every }j>\operatorname{rk}E_1=r-k.$$
> Combining the two displayed lines: for every $j>r-k$,
> $$c_j(E)=c_j(E_1)=0.$$
> This is exactly the assertion, since $r-k=\operatorname{rk}E-k$.

> [!note]- Why the degree cap (clause (i)) holds — reproved from the determinant
> This is the one clause worth re-seeing, because it is the whole engine. Let $s:=\operatorname{rk}E_1$ and choose a unitary connection with curvature $F\in\Omega^2(M;\mathfrak u(s))$, an $s\times s$ matrix of $2$-forms. By [[Def - Chern Classes|the definition of the total Chern class]],
> $$c(E_1)=\Big[\det\!\Big(\mathbf 1+\tfrac{i}{2\pi}F\Big)\Big].$$
> The determinant of an $s\times s$ matrix with entries in the commutative ring $\Omega^{\mathrm{even}}(M)$ is well-defined and is a polynomial in the entries — commutativity of even-degree forms and the resulting well-definedness of this determinant are established in [[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]. Expanding by the Leibniz formula,
> $$\det\!\Big(\mathbf 1+\tfrac{i}{2\pi}F\Big)=\sum_{\ell=0}^{s}\Big(\tfrac{i}{2\pi}\Big)^{\ell}\,\sigma_\ell(F),$$
> where $\sigma_\ell(F)$ is the sum of the $\ell\times\ell$ principal minors of $F$; each such minor is itself a signed sum of products of $\ell$ distinct entries of $F$, and each such product is a wedge of $\ell$ two-forms, hence homogeneous of degree $2\ell$, so $\sigma_\ell(F)\in\Omega^{2\ell}(M)$. An $s\times s$ matrix has **no** $\ell\times\ell$ principal minors when $\ell>s$, so the sum truncates at $\ell=s$: there is no term of degree exceeding $2s$. Matching the degree-$2j$ piece with $c_j(F)$ gives $c_j(F)=0$ for $j>s$, and passing to cohomology, $c_j(E_1)=0$ for $j>s=\operatorname{rk}E_1$.

> [!note]- Complete formal solution
> **Claim.** If $E\cong E_1\oplus\underline{\mathbb C}^{\,k}$ is a complex vector bundle over $M$ with $r=\operatorname{rk}E$, then $c_j(E)=0$ for all $j>r-k$.
>
> Since $c$ is an invariant of the isomorphism class (clause (v) of the axioms theorem), $c(E)=c(E_1\oplus\underline{\mathbb C}^{\,k})$. By the Whitney sum formula (clause (iii)),
> $$c(E)=c(E_1)\smile c\big(\underline{\mathbb C}^{\,k}\big).$$
> The bundle $\underline{\mathbb C}^{\,k}$ is trivial, so by the trivial-bundle theorem $c_j(\underline{\mathbb C}^{\,k})=0$ for $j\ge1$ and $c(\underline{\mathbb C}^{\,k})=1$. As $1$ is the unit of the cup product,
> $$c(E)=c(E_1)\smile 1=c(E_1),$$
> whence $c_j(E)=c_j(E_1)$ for every $j$. The bundle $E_1$ has rank $r-k$, so by the degree cap (clause (i)), $c_j(E_1)=0$ for $j>r-k$. Therefore $c_j(E)=c_j(E_1)=0$ for every $j>r-k=\operatorname{rk}E-k$. $\blacksquare$

> [!warning] Illegal but tempting: dropping the word "trivial"
> It is tempting to think the argument shows "$c_j(E)=0$ for $j>\operatorname{rk}E-\operatorname{rk}(\text{any summand})$", i.e. that *any* Whitney splitting $E\cong E_1\oplus E_2$ forces $c_j(E)=0$ for $j>\operatorname{rk}E_1$. This is false. The step that fails is Step 2: for a general summand $E_2$ the class $c(E_2)$ has nonzero pieces in positive degree, so $c(E)=c(E_1)\smile c(E_2)$ can carry classes all the way up to degree $\operatorname{rk}E_1+\operatorname{rk}E_2=\operatorname{rk}E$. A concrete instance: over $\mathbb{CP}^1\times\mathbb{CP}^1$ take $E_1,E_2$ to be pullbacks of $\mathcal O(-1)$ from the two factors; each is a line bundle with $c_1\neq0$, and $c_2(E_1\oplus E_2)=c_1(E_1)\smile c_1(E_2)\neq0$, which is nonzero in degree $2=\operatorname{rk}E>\operatorname{rk}E_1=1$. The extra condition that rescues the conclusion is exactly the one in the hypothesis: the split-off summand must be *trivial*, so that its total class is $1$.

> [!note]- Sanity check at the extreme values of $k$
> When $k=0$ (no trivial summand), the statement reads $c_j(E)=0$ for $j>r$, which is just clause (i). When $k=r$ (so $E_1$ has rank $0$ and $E\cong\underline{\mathbb C}^{\,r}$ is itself trivial), it reads $c_j(E)=0$ for $j>0$, i.e. $c(E)=1$ — the trivial-bundle theorem. The general statement interpolates between these two known extremes, one trivial direction at a time.

---

# Key Takeaways

**A trivial Whitney summand is transparent to the Chern grading, and this is the entire content of the exercise.** The mechanism is that the total Chern class of a trivial bundle is the multiplicative identity $1$, which lives in degree $0$ and therefore cannot lift the degree of any class it multiplies. So whenever a bundle is presented as "something interesting plus $k$ trivial line's worth of directions", its Chern classes are literally the Chern classes of the interesting part, and in particular they stop one degree earlier for each trivial direction. The reusable principle: *reading off vanishing of a graded product reduces to knowing the top degree of each factor and the degree of the identity*. The trigger to apply it is a Whitney splitting with a recognisably trivial summand; the reaction is to factor the total class and delete the trivial factor. This same move underlies the stable-range vanishing of Chern classes in $K$-theory, where adding trivial bundles ("stabilising") is designed precisely not to change characteristic classes.

**The degree cap $c_j(E)=0$ for $j>\operatorname{rk}E$ is a determinant fact, not a topological one.** It is worth internalising why clause (i) is true: the total Chern class is the determinant $\det(\mathbf 1+\tfrac{i}{2\pi}F)$ of an $(\operatorname{rk}E)\times(\operatorname{rk}E)$ matrix of $2$-forms, and a determinant of an $s\times s$ matrix is a sum over products of at most $s$ entries; with each entry a $2$-form, no term can have form-degree above $2s$. Thus the ceiling on Chern degrees is imposed by linear algebra — the size of the matrix — before any cohomology enters. This diagnostic recurs constantly: to bound the top nonzero characteristic class of a bundle built by an operation (sum, tensor, dual, pullback), track the size of the matrix whose determinant computes the class. It is also why the *top* Chern class $c_{\operatorname{rk}E}(E)$ is special — it is the determinant's constant-in-$\lambda$ coefficient, $\det(\tfrac{i}{2\pi}F)$ — and why it coincides with the Euler class of the underlying real bundle (see [[Def - Euler Class of an Oriented Vector Bundle]]).

**Isomorphism invariance plus the Whitney sum formula is the standard toolkit for turning geometry into algebra in the graded cohomology ring.** Almost every elementary computation of characteristic classes uses exactly this pair: use invariance (clause (v)) to replace the given bundle by a convenient model — here a direct sum — and then use the ring structure (clause (iii), and for line bundles clause (viii)) to reduce to classes you already know. The transferable diagnostic is that a Chern-class identity phrased for a *specific* bundle is almost always proved by finding a splitting or pullback presentation of that bundle and pushing the identity through the ring homomorphism $c$. Companion exercises in this section that use the same toolkit are [[Ex - Chern Classes Depend only on the Isomorphism Class and Vanish for Trivial Bundles]] (clauses (v) and (vii) directly) and [[Ex - Chern Classes of the Dual Bundle]] (invariance under the dual, via the dual connection); the present exercise is the additive-degree-bookkeeping member of that family.

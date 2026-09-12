---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Properties of the Hodge Star in Arbitrary Signature"
  - "Def - Hodge Star in Arbitrary Signature"
  - "Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $(V,\langle\cdot,\cdot\rangle)$ be an oriented $n$-dimensional real vector space equipped with a non-degenerate symmetric bilinear form of index $p$ — that is, $p$ is the number of negative signs in the diagonalisation of the form, so the form has signature $(n-p,p)$. Let $\star:\Lambda^k V^*\to\Lambda^{n-k}V^*$ be the [[Def - Hodge Star in Arbitrary Signature|Hodge star operator]] associated with the form and the given orientation. Prove the **double-star identity**
$$\star\star\omega=(-1)^{k(n-k)+p}\,\omega\qquad\text{for all }\omega\in\Lambda^k V^*.$$

This is property (2) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]] (equation (3.3) in Bär, *Gauge Theory*, Proposition 3.1.8), which Bär leaves as an exercise. You may use only property (1) of that theorem — the closed formula for $\star$ on basis monomials — together with the bilinearity of $\star$. After proving the identity, check it against the two cases the physics uses most: two-forms on Minkowski space $\mathbb{R}^{1,3}$ (where the answer is $-1$) and one-forms on Euclidean $\mathbb{R}^3$ (where the answer is $+1$).

**Recall:**

The objects in play are a generalized orthonormal basis and the induced inner product on exterior powers, the volume form, the Hodge star through its defining relation, and — the one tool the solution actually uses — the closed formula for the star on basis monomials.

![[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms#The Definition]]

Concretely: a **generalized orthonormal basis** $e_1,\dots,e_n$ of $V$ satisfies $\langle e_i,e_j\rangle=0$ for $i\neq j$ and $\langle e_j,e_j\rangle=\epsilon_j\in\{+1,-1\}$; the **index** $p$ is the number of indices $j$ with $\epsilon_j=-1$. Writing $e^*_1,\dots,e^*_n$ for the dual basis of $V^*$, the monomials $e^*_I:=e^*_{i_1}\wedge\dots\wedge e^*_{i_k}$ for strictly increasing multi-indices $I=(i_1<\dots<i_k)$ form a generalized orthonormal basis of $\Lambda^k V^*$ with
$$\langle e^*_I,e^*_I\rangle=\epsilon_{i_1}\cdots\epsilon_{i_k}=:\epsilon_I,\qquad\langle e^*_I,e^*_{I'}\rangle=0\ \ (I\neq I').$$
The **volume form** for a positively oriented such basis is $\mathrm{vol}:=e^*_1\wedge\dots\wedge e^*_n\in\Lambda^n V^*$.

![[Def - Hodge Star in Arbitrary Signature#The Definition]]

The [[Def - Hodge Star in Arbitrary Signature|Hodge star]] is the unique linear map $\star:\Lambda^k V^*\to\Lambda^{n-k}V^*$ with $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$ for all $\omega\in\Lambda^k V^*$ and $\eta\in\Lambda^{n-k}V^*$.

![[Thm - Properties of the Hodge Star in Arbitrary Signature#Statement]]

The single property this exercise invokes is property (1): for a positively oriented generalized orthonormal basis and a strictly increasing multi-index $I=(i_1<\dots<i_k)$ with complementary strictly increasing multi-index $J=(j_1<\dots<j_{n-k})$, so that $\{i_1,\dots,i_k\}\sqcup\{j_1,\dots,j_{n-k}\}=\{1,\dots,n\}$,
$$\star(e^*_{i_1}\wedge\dots\wedge e^*_{i_k})=\epsilon_{j_1}\cdots\epsilon_{j_{n-k}}\cdot\operatorname{sign}(IJ)\cdot e^*_{j_1}\wedge\dots\wedge e^*_{j_{n-k}},$$
where $(IJ)=(i_1,\dots,i_k,j_1,\dots,j_{n-k})$ is the permutation of $(1,\dots,n)$ obtained by writing the entries of $I$ followed by the entries of $J$, and $\operatorname{sign}(IJ)\in\{+1,-1\}$ is its sign. Abbreviate $\epsilon_J:=\epsilon_{j_1}\cdots\epsilon_{j_{n-k}}$, so property (1) reads $\star e^*_I=\epsilon_J\operatorname{sign}(IJ)\,e^*_J$.

---

# Convergent Strategy

**Problem class.** This is a *compute-an-operator-squared* problem: we are asked for the value of $\star^2$ on $\Lambda^k V^*$, and the assertion is that $\star^2$ is a scalar, namely $(-1)^{k(n-k)+p}$ times the identity. Whenever a linear operator is claimed to be a scalar multiple of the identity, the efficient route is to evaluate it on a basis and read off a single common scalar; there is no need to touch a general vector until the very end, when bilinearity extends the basis computation to everything.

**Assumption pattern.** The hypotheses are exactly those that make property (1) available: $V$ is oriented (so $\mathrm{vol}$ and hence $\star$ are unambiguously defined), the form is non-degenerate (so $\star$ exists and is unique), and it has a fixed index $p$ (so the product of all the $\epsilon_j$ equals $(-1)^p$). The recognisable trigger is that the target sign splits into two independent pieces, a *permutation* sign $(-1)^{k(n-k)}$ and a *metric* sign $(-1)^p$, and property (1) manufactures exactly one of each per application of $\star$.

**Theorem routing.** The route is short and rigid. Apply property (1) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]] to a basis monomial $e^*_I$ to get $\star e^*_I=\epsilon_J\operatorname{sign}(IJ)\,e^*_J$; apply property (1) a second time to $e^*_J$ — whose complement is $I$ — to get $\star e^*_J=\epsilon_I\operatorname{sign}(JI)\,e^*_I$; multiply, and evaluate the two resulting products $\epsilon_I\epsilon_J$ and $\operatorname{sign}(IJ)\operatorname{sign}(JI)$ separately. Finally extend from monomials to all of $\Lambda^k V^*$ by bilinearity of the linear map $\star\star$.

**Key decision point.** The one genuine step is recognising that the two scalar factors decouple and computing each in closed form. The metric factor is $\epsilon_I\epsilon_J=\prod_{j=1}^n\epsilon_j=(-1)^p$, because $I$ and $J$ together exhaust every index exactly once and exactly $p$ of the $\epsilon_j$ equal $-1$. The permutation factor is $\operatorname{sign}(IJ)\operatorname{sign}(JI)=(-1)^{k(n-k)}$, because the words $(IJ)$ and $(JI)$ differ by swapping a block of length $k$ past a block of length $n-k$, which costs exactly $k(n-k)$ adjacent transpositions. Missing either decoupling — for instance trying to track the individual entries $j_1,\dots,j_{n-k}$ — makes the computation look far harder than it is.

---

# Legal Operations Used

This solution deploys the following legal operations (numbered as they will appear on the topic page's Legal Operations section; until that page is written they are named descriptively).

1. **Reduce an identity between linear maps to a basis check.** Both $\star\star$ and the scalar $(-1)^{k(n-k)+p}\,\mathrm{id}$ are linear in $\omega$, so it suffices to prove the identity on the basis monomials $e^*_I$; bilinearity then extends it to every $\omega\in\Lambda^k V^*$.

2. **Evaluate the Hodge star on basis monomials via property (1).** Replace each occurrence of $\star$ acting on a monomial by the closed formula $\star e^*_I=\epsilon_J\operatorname{sign}(IJ)\,e^*_J$ from [[Thm - Properties of the Hodge Star in Arbitrary Signature]].

3. **Iterate the star and observe that the second complement returns to the first index set.** The complement of $J$ in $\{1,\dots,n\}$ is $I$ again, so the second application of property (1) sends $e^*_J$ back to a multiple of $e^*_I$; this is what makes $\star\star$ diagonal in the monomial basis.

4. **Factor the accumulated scalar into a metric part and a permutation part.** Separate $\epsilon_I\epsilon_J\operatorname{sign}(IJ)\operatorname{sign}(JI)$ into $\bigl(\epsilon_I\epsilon_J\bigr)$ and $\bigl(\operatorname{sign}(IJ)\operatorname{sign}(JI)\bigr)$ and compute each independently.

5. **Compute a product of $\pm1$ over a complementary pair of index sets.** Use $I\sqcup J=\{1,\dots,n\}$ to collapse $\epsilon_I\epsilon_J$ to $\prod_{j=1}^n\epsilon_j=(-1)^p$.

6. **Compute a block-transposition sign.** Use that reordering the word $(I,J)$ into $(J,I)$ is a swap of a length-$k$ block past a length-$(n-k)$ block, costing $k(n-k)$ transpositions, so the two signs differ by $(-1)^{k(n-k)}$.

---

# Hints

> [!note]- Hint 1
> $\star\star$ is a linear map $\Lambda^k V^*\to\Lambda^k V^*$, and the claim is that it is a *scalar*. Do not try to prove this on a general $\omega$. Fix a positively oriented generalized orthonormal basis and check the identity on the monomials $e^*_I$; linearity does the rest.

> [!note]- Hint 2
> Apply property (1) once: $\star e^*_I=\epsilon_J\operatorname{sign}(IJ)\,e^*_J$, where $J$ is the increasing complement of $I$. Now you must apply $\star$ again — to $e^*_J$. What is the complement of $J$? It is $I$. So property (1) applies a second time and sends $e^*_J$ back to a multiple of $e^*_I$.

> [!note]- Hint 3
> After the two applications you get $\star\star e^*_I=\bigl(\epsilon_I\epsilon_J\bigr)\bigl(\operatorname{sign}(IJ)\operatorname{sign}(JI)\bigr)e^*_I$. Treat the two bracketed scalars separately. For the first: $I$ and $J$ together list every index of $\{1,\dots,n\}$ exactly once, so $\epsilon_I\epsilon_J$ is the product of *all* the $\epsilon_j$. How many of them are $-1$?

> [!note]- Hint 4
> For the sign factor, compare the words $(IJ)=(i_1,\dots,i_k,j_1,\dots,j_{n-k})$ and $(JI)=(j_1,\dots,j_{n-k},i_1,\dots,i_k)$. One is obtained from the other by moving the whole $J$-block (length $n-k$) past the whole $I$-block (length $k$). Each of the $n-k$ entries of $J$ must hop over each of the $k$ entries of $I$: that is $k(n-k)$ adjacent transpositions, so $\operatorname{sign}(JI)=(-1)^{k(n-k)}\operatorname{sign}(IJ)$. Since $\operatorname{sign}(IJ)^2=1$, the product is $(-1)^{k(n-k)}$.

---

# Solution

The plan is to prove the identity on the monomial basis and extend by linearity. Applying property (1) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]] twice turns $\star\star e^*_I$ into a scalar multiple of $e^*_I$; that scalar is a product of an $\epsilon$-factor and a sign-factor, and each of them evaluates in closed form — the $\epsilon$-factor to $(-1)^p$ because $I$ and $J$ exhaust all indices, and the sign-factor to $(-1)^{k(n-k)}$ because reversing the two blocks costs $k(n-k)$ transpositions. Multiplying gives the claimed $(-1)^{k(n-k)+p}$.

Throughout, fix a positively oriented generalized orthonormal basis $e_1,\dots,e_n$ of $V$ with $\langle e_j,e_j\rangle=\epsilon_j\in\{+1,-1\}$, dual basis $e^*_1,\dots,e^*_n$, and volume form $\mathrm{vol}=e^*_1\wedge\dots\wedge e^*_n$. Let $I=(i_1<\dots<i_k)$ be a strictly increasing multi-index and $J=(j_1<\dots<j_{n-k})$ its strictly increasing complement in $\{1,\dots,n\}$, so $\{i_1,\dots,i_k\}\sqcup\{j_1,\dots,j_{n-k}\}=\{1,\dots,n\}$. Write $\epsilon_I=\epsilon_{i_1}\cdots\epsilon_{i_k}$ and $\epsilon_J=\epsilon_{j_1}\cdots\epsilon_{j_{n-k}}$.

**Step 1: Reduce to basis monomials.**

The map $\star\star:\Lambda^k V^*\to\Lambda^k V^*$ is linear, being the composite of the two linear maps $\star:\Lambda^k V^*\to\Lambda^{n-k}V^*$ and $\star:\Lambda^{n-k}V^*\to\Lambda^k V^*$. It therefore suffices to verify $\star\star e^*_I=(-1)^{k(n-k)+p}e^*_I$ on each basis monomial $e^*_I$; the general case follows because both sides are linear in $\omega$.

> [!note]- Derivation
> The monomials $\{e^*_I:I=(i_1<\dots<i_k)\}$ form a basis of $\Lambda^k V^*$ (by [[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms|the induced-inner-product definition]], they are even a generalized orthonormal basis). Suppose we have shown
> $$\star\star e^*_I=(-1)^{k(n-k)+p}\,e^*_I$$
> for every such $I$. An arbitrary $\omega\in\Lambda^k V^*$ is a finite linear combination $\omega=\sum_I c_I\,e^*_I$ with $c_I\in\mathbb{R}$. Since $\star$ is linear (by [[Def - Hodge Star in Arbitrary Signature|its definition]] and [[Thm - Existence and Uniqueness of the Hodge Star|the existence–uniqueness theorem]]), so is $\star\star$, and hence
> $$\star\star\omega=\star\star\Bigl(\sum_I c_I e^*_I\Bigr)=\sum_I c_I\,\star\star e^*_I=\sum_I c_I(-1)^{k(n-k)+p}e^*_I=(-1)^{k(n-k)+p}\,\omega\qquad\text{(linearity of }\star\star\text{, then the monomial case).}$$
> So the identity for all $\omega$ is equivalent to the identity on monomials, which is what the remaining steps establish.

**Step 2: Apply property (1) twice.**

Property (1) applied to $I$ gives $\star e^*_I=\epsilon_J\operatorname{sign}(IJ)\,e^*_J$; applied to $J$ — whose complement is $I$ — it gives $\star e^*_J=\epsilon_I\operatorname{sign}(JI)\,e^*_I$. Composing,
$$\star\star e^*_I=\epsilon_I\epsilon_J\,\operatorname{sign}(IJ)\,\operatorname{sign}(JI)\,e^*_I.$$

> [!note]- Derivation
> By property (1) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]], with $I$ increasing and complement $J$ increasing,
> $$\star e^*_I=\epsilon_J\operatorname{sign}(IJ)\,e^*_J\qquad\text{(property (1) applied to the index set }I\text{).}$$
> Now $e^*_J$ is itself a basis monomial of $\Lambda^{n-k}V^*$ indexed by the increasing multi-index $J$, and the complement of $\{j_1,\dots,j_{n-k}\}$ in $\{1,\dots,n\}$ is precisely $\{i_1,\dots,i_k\}$, listed increasingly as $I$. Hence property (1) applies again, now to the index set $J$ of size $n-k$ (its complement, of size $k$, being $I$):
> $$\star e^*_J=\epsilon_I\operatorname{sign}(JI)\,e^*_I\qquad\text{(property (1) applied to the index set }J\text{),}$$
> where $(JI)=(j_1,\dots,j_{n-k},i_1,\dots,i_k)$ and $\epsilon_I=\epsilon_{i_1}\cdots\epsilon_{i_k}$ is the product of the $\epsilon$'s over the complement of $J$. Substituting the first line into the second and using linearity of $\star$,
> $$\star\star e^*_I=\star\bigl(\epsilon_J\operatorname{sign}(IJ)\,e^*_J\bigr)=\epsilon_J\operatorname{sign}(IJ)\,\star e^*_J=\epsilon_J\operatorname{sign}(IJ)\cdot\epsilon_I\operatorname{sign}(JI)\,e^*_I\qquad\text{(pull the scalar out, then the second application).}$$
> Regrouping the four scalar factors gives $\star\star e^*_I=\bigl(\epsilon_I\epsilon_J\bigr)\bigl(\operatorname{sign}(IJ)\operatorname{sign}(JI)\bigr)e^*_I$, as claimed.

**Step 3: The metric factor $\epsilon_I\epsilon_J$ equals $(-1)^p$.**

Because $I$ and $J$ partition $\{1,\dots,n\}$, the product $\epsilon_I\epsilon_J$ ranges over every $\epsilon_j$ exactly once, and exactly $p$ of these are $-1$.

> [!note]- Derivation
> By definition of the complement, the disjoint union $\{i_1,\dots,i_k\}\sqcup\{j_1,\dots,j_{n-k}\}$ equals $\{1,\dots,n\}$: every index $j\in\{1,\dots,n\}$ occurs in exactly one of the two lists. Therefore
> $$\epsilon_I\epsilon_J=\bigl(\epsilon_{i_1}\cdots\epsilon_{i_k}\bigr)\bigl(\epsilon_{j_1}\cdots\epsilon_{j_{n-k}}\bigr)=\prod_{j=1}^n\epsilon_j\qquad\text{(each factor }\epsilon_j\text{ appears once, since }I\sqcup J=\{1,\dots,n\}\text{).}$$
> By the definition of the [[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms|index]], exactly $p$ of the numbers $\epsilon_1,\dots,\epsilon_n$ equal $-1$ and the remaining $n-p$ equal $+1$. A product of $\pm1$'s equals $(-1)^{(\text{number of }-1\text{ factors})}$, so
> $$\prod_{j=1}^n\epsilon_j=(-1)^p.$$
> Hence $\epsilon_I\epsilon_J=(-1)^p$.

**Step 4: The permutation factor $\operatorname{sign}(IJ)\operatorname{sign}(JI)$ equals $(-1)^{k(n-k)}$.**

The words $(IJ)$ and $(JI)$ differ by moving the $J$-block past the $I$-block, which is a product of $k(n-k)$ adjacent transpositions.

> [!note]- Derivation
> The words $(IJ)=(i_1,\dots,i_k,j_1,\dots,j_{n-k})$ and $(JI)=(j_1,\dots,j_{n-k},i_1,\dots,i_k)$ are two arrangements of the same $n$ distinct symbols $1,\dots,n$. To turn $(IJ)$ into $(JI)$, move each entry of the $J$-block, in turn, leftward past the entire $I$-block. The entry $j_{n-k}$ (the last one, chosen first so that the relative order of the $J$-entries is preserved) hops leftward past the $k$ entries $i_1,\dots,i_k$ in $k$ adjacent transpositions; then $j_{n-k-1}$ hops past the same $k$ entries in $k$ transpositions; and so on for all $n-k$ entries of $J$. The total number of adjacent transpositions is
> $$\underbrace{k+k+\dots+k}_{n-k\text{ terms}}=k(n-k).$$
> Since the sign of a permutation is $(-1)^{(\text{number of transpositions in any factorisation})}$ and the sign map is a homomorphism, applying $k(n-k)$ transpositions to the arrangement $(IJ)$ multiplies its sign by $(-1)^{k(n-k)}$:
> $$\operatorname{sign}(JI)=(-1)^{k(n-k)}\operatorname{sign}(IJ)\qquad\text{(block swap of lengths }k\text{ and }n-k\text{).}$$
> Multiplying both sides by $\operatorname{sign}(IJ)$ and using $\operatorname{sign}(IJ)^2=1$ (a sign is $\pm1$),
> $$\operatorname{sign}(IJ)\operatorname{sign}(JI)=\operatorname{sign}(IJ)^2(-1)^{k(n-k)}=(-1)^{k(n-k)}.$$

**Step 5: Combine and extend by linearity.**

Substituting Steps 3 and 4 into Step 2,
$$\star\star e^*_I=(-1)^p\cdot(-1)^{k(n-k)}\,e^*_I=(-1)^{k(n-k)+p}\,e^*_I,$$
and by Step 1 this monomial identity gives $\star\star\omega=(-1)^{k(n-k)+p}\,\omega$ for every $\omega\in\Lambda^k V^*$.

> [!note]- Complete formal solution
> **Claim.** For an oriented $n$-dimensional real vector space with a non-degenerate symmetric bilinear form of index $p$, the Hodge star satisfies $\star\star\omega=(-1)^{k(n-k)+p}\omega$ for all $\omega\in\Lambda^k V^*$.
>
> Fix a positively oriented generalized orthonormal basis $e_1,\dots,e_n$ with $\langle e_j,e_j\rangle=\epsilon_j\in\{+1,-1\}$, dual basis $e^*_j$, and $\mathrm{vol}=e^*_1\wedge\dots\wedge e^*_n$. Since $\star\star$ is linear, it suffices to prove the identity on each basis monomial $e^*_I$, $I=(i_1<\dots<i_k)$; write $J=(j_1<\dots<j_{n-k})$ for the increasing complement, so $I\sqcup J=\{1,\dots,n\}$.
>
> By property (1) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]], $\star e^*_I=\epsilon_J\operatorname{sign}(IJ)\,e^*_J$ with $\epsilon_J=\epsilon_{j_1}\cdots\epsilon_{j_{n-k}}$. The complement of $J$ is $I$, so property (1) applies again: $\star e^*_J=\epsilon_I\operatorname{sign}(JI)\,e^*_I$ with $\epsilon_I=\epsilon_{i_1}\cdots\epsilon_{i_k}$. Composing and pulling out scalars,
> $$\star\star e^*_I=\epsilon_I\epsilon_J\,\operatorname{sign}(IJ)\operatorname{sign}(JI)\,e^*_I.$$
> Since $I\sqcup J=\{1,\dots,n\}$, the product $\epsilon_I\epsilon_J=\prod_{j=1}^n\epsilon_j=(-1)^p$, because exactly $p$ of the $\epsilon_j$ equal $-1$. The word $(JI)$ arises from $(IJ)$ by moving the length-$(n-k)$ block $J$ past the length-$k$ block $I$, a product of $k(n-k)$ adjacent transpositions, so $\operatorname{sign}(JI)=(-1)^{k(n-k)}\operatorname{sign}(IJ)$ and hence $\operatorname{sign}(IJ)\operatorname{sign}(JI)=(-1)^{k(n-k)}$. Therefore
> $$\star\star e^*_I=(-1)^p(-1)^{k(n-k)}e^*_I=(-1)^{k(n-k)+p}e^*_I,$$
> and by linearity $\star\star\omega=(-1)^{k(n-k)+p}\omega$ for all $\omega\in\Lambda^k V^*$. $\blacksquare$

> [!warning] Illegal but tempting: quoting the Riemannian formula $\star\star=(-1)^{k(n-k)}$
> In the Riemannian ($p=0$) treatment — the vault's [[Thm - Properties of the Hodge Star]] in [[Def - The Hodge Star Operator|Hodge Theory I]] — one has $\star\star=(-1)^{k(n-k)}$, with no index term. It is tempting to carry that formula over unchanged. Doing so drops the metric factor $(-1)^p$ and gives the wrong sign in every indefinite signature. The extra $(-1)^p$ is exactly the price of $\langle\mathrm{vol},\mathrm{vol}\rangle=(-1)^p$: it enters through $\epsilon_I\epsilon_J=\prod_j\epsilon_j=(-1)^p$ in Step 3, a product that collapses to $+1$ only when no $\epsilon_j$ is negative. On Minkowski two-forms the two formulas already disagree: $(-1)^{k(n-k)}=+1$ but the correct $\star\star=-1$.

> [!note]- Independent sanity check on Minkowski two-forms
> Take $V=\mathbb{R}^{1,3}$ with basis $e_1=\partial_t,e_2=\partial_x,e_3=\partial_y,e_4=\partial_z$, signature $(-,+,+,+)$, so $\epsilon_1=-1$, $\epsilon_2=\epsilon_3=\epsilon_4=+1$, $p=1$, $n=4$; here $k=2$, $n-k=2$. From property (1), $\star(dt\wedge dx)=\epsilon_3\epsilon_4\operatorname{sign}(1,2,3,4)\,dy\wedge dz=(+1)(+1)(+1)\,dy\wedge dz=dy\wedge dz$, and $\star(dy\wedge dz)=\epsilon_1\epsilon_2\operatorname{sign}(3,4,1,2)\,dt\wedge dx$. The word $(3,4,1,2)$ has four inversions, so $\operatorname{sign}(3,4,1,2)=+1$, and $\epsilon_1\epsilon_2=(-1)(+1)=-1$; hence $\star(dy\wedge dz)=-\,dt\wedge dx$. Composing, $\star\star(dt\wedge dx)=-\,dt\wedge dx$, i.e. $\star\star=-1$ on this two-form, matching $(-1)^{k(n-k)+p}=(-1)^{4+1}=-1$.

---

# Key Takeaways

**To evaluate a claimed scalar operator, evaluate it on one basis and read off the common eigenvalue.** The whole exercise is an instance of a reusable principle: a linear map that is asserted to be $\lambda\cdot\mathrm{id}$ can be verified by checking $\star\star e^*_I=\lambda e^*_I$ on the basis monomials, because linearity then propagates the identity to every vector (Step 1). The Hodge star squared is diagonal in the monomial basis for a structural reason worth remembering — applying $\star$ sends $e^*_I$ to a multiple of the complementary monomial $e^*_J$, and applying it once more sends $e^*_J$ back to a multiple of $e^*_I$, because the complement of the complement is the original index set. The trigger for reaching for this technique is any statement of the form "operator $T$ squares to a scalar" or "$T$ is an involution up to sign": do not fight a general vector, find the basis on which $T$ is manifestly diagonal and multiply the two diagonal entries. This same complement-of-the-complement mechanism is what makes the Hodge star an isomorphism $\Lambda^k\cong\Lambda^{n-k}$ in the first place, and it recurs whenever a duality pairs a subspace with its orthogonal or annihilator complement.

**The double-star sign splits into a permutation part $(-1)^{k(n-k)}$ and a metric part $(-1)^p$, and these two contributions must always be tracked separately.** The permutation part is combinatorics — it counts the cost of swapping a $k$-block past an $(n-k)$-block and knows nothing about the inner product; the metric part is geometry — it records how many basis vectors have negative square, through $\langle\mathrm{vol},\mathrm{vol}\rangle=(-1)^p$. The decisive diagnostic when reconstructing this proof after a gap is to ask, of any sign appearing in Hodge-star algebra, "is this a shuffle sign or an $\epsilon$-product?" The shuffle signs come from reordering wedge factors; the $\epsilon$-products come from the values $\langle e_j,e_j\rangle$. Every identity in [[Thm - Properties of the Hodge Star in Arbitrary Signature]] — the double star (2), the isometry-up-to-sign (3), the symmetric pairing (4) — is assembled from exactly these two ingredients, and once one sees the decomposition the entire proposition becomes a bookkeeping exercise rather than a list of formulas to memorise. In particular the metric part is invisible in Riemannian signature, which is precisely why the Riemannian formula misleads when transplanted.

**The result is the reason the star behaves so differently in Lorentzian and Riemannian four dimensions, and is the algebraic seed of self-duality.** In dimension four on two-forms the exponent is $k(n-k)+p=4+p$, so $\star\star=(-1)^p$: in Euclidean signature $(p=0)$ one has $\star\star=+1$, the star is an involution, and $\Lambda^2$ splits into the $\pm1$ eigenspaces of self-dual and anti-self-dual forms — the foundation of instanton theory and of [[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions]]. In Lorentzian signature $(p=1)$ one instead has $\star\star=-1$, so the star has no real eigenvectors on two-forms and there is no real self-dual decomposition; the natural object is instead the complex eigenspace decomposition used in Petrov classification and in the spinor formulation of electromagnetism. Recognising which regime one is in — a single evaluation of $(-1)^{k(n-k)+p}$ — is the first move whenever a problem asks whether "self-dual" even makes sense, and it explains why gauge theory over Riemannian four-manifolds, not Lorentzian spacetimes, is where the (anti-)self-dual Yang–Mills equations live.

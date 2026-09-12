---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Properties of the Hodge Star in Arbitrary Signature"
  - "Def - Hodge Star in Arbitrary Signature"
  - "Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $(V,\langle\cdot,\cdot\rangle)$ be an oriented $n$-dimensional real vector space equipped with a non-degenerate symmetric bilinear form of index $p$ — that is, $p$ is the number of negative signs in the diagonalisation of the form, so it has signature $(n-p,p)$. Let $\star:\Lambda^k V^*\to\Lambda^{n-k}V^*$ be the [[Def - Hodge Star in Arbitrary Signature|Hodge star operator]] associated with the form and the orientation, and let $\langle\cdot,\cdot\rangle$ also denote the induced inner product on each exterior power. Prove that $\star$ is an **isometry up to the sign of the index**: for all $\omega,\eta\in\Lambda^k V^*$,
$$\langle\star\omega,\star\eta\rangle=(-1)^p\,\langle\omega,\eta\rangle.$$

This is property (3) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]] (equation (3.4) in Bär, *Gauge Theory*, Proposition 3.1.8), which Bär leaves as an exercise. Solve it two ways: first by reducing to basis monomials using property (1), then — as a check — by deriving it from the defining relation together with the double-star formula. In particular note the contrast with the Riemannian case: in indefinite signature $\star$ is *not* an isometry, and the smallest counterexample $dt\wedge dx$ on Minkowski space exhibits exactly the failing sign.

**Recall:**

The objects in play are a generalized orthonormal basis with its index $p$, the induced inner product on exterior powers, the Hodge star, its closed formula on basis monomials (property (1)), and the double-star formula (property (2)).

![[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms#The Definition]]

Concretely: a **generalized orthonormal basis** $e_1,\dots,e_n$ has $\langle e_i,e_j\rangle=0$ for $i\neq j$ and $\langle e_j,e_j\rangle=\epsilon_j\in\{+1,-1\}$; the **index** $p$ counts the indices with $\epsilon_j=-1$. With dual basis $e^*_1,\dots,e^*_n$, the monomials $e^*_I=e^*_{i_1}\wedge\dots\wedge e^*_{i_k}$ ($I=(i_1<\dots<i_k)$) form a generalized orthonormal basis of $\Lambda^k V^*$ with
$$\langle e^*_I,e^*_{I'}\rangle=\begin{cases}\epsilon_{i_1}\cdots\epsilon_{i_k}=:\epsilon_I&I=I'\\[2pt]0&I\neq I'.\end{cases}$$
The **volume form** is $\mathrm{vol}=e^*_1\wedge\dots\wedge e^*_n$, with $\langle\mathrm{vol},\mathrm{vol}\rangle=(-1)^p$.

![[Def - Hodge Star in Arbitrary Signature#The Definition]]

The [[Def - Hodge Star in Arbitrary Signature|Hodge star]] is the unique linear map with $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$ for all $\omega\in\Lambda^k V^*$, $\eta\in\Lambda^{n-k}V^*$.

![[Thm - Properties of the Hodge Star in Arbitrary Signature#Statement]]

The two properties this exercise invokes are:
- **Property (1):** for increasing $I=(i_1<\dots<i_k)$ with increasing complement $J=(j_1<\dots<j_{n-k})$ (so $I\sqcup J=\{1,\dots,n\}$), $\star e^*_I=\epsilon_J\operatorname{sign}(IJ)\,e^*_J$, where $\epsilon_J=\epsilon_{j_1}\cdots\epsilon_{j_{n-k}}$ and $(IJ)=(i_1,\dots,i_k,j_1,\dots,j_{n-k})$.
- **Property (2)** (the double-star formula, [[Ex - Double Star Sign in Arbitrary Signature|proved separately]]): $\star\star\omega=(-1)^{k(n-k)+p}\omega$ for $\omega\in\Lambda^k V^*$.

---

# Convergent Strategy

**Problem class.** This is a *preservation-of-a-form* problem: we must show that the operator $\star$ transports the inner product on $\Lambda^k V^*$ to the inner product on $\Lambda^{n-k}V^*$ up to the fixed scalar $(-1)^p$. Two standard routes exist for such problems, and the exercise asks for both. The first is *diagonalise and compare*: evaluate both sides on a basis, where the inner product is diagonal and $\star$ is given in closed form, and match coefficient by coefficient. The second is *massage through the defining identity*: rewrite $\langle\star\omega,\star\eta\rangle\,\mathrm{vol}$ as a wedge product using the relation that defines $\star$, then simplify with algebra already proved.

**Assumption pattern.** The hypotheses are exactly what property (1) needs (orientation, non-degeneracy, index $p$). The recognisable trigger for the basis route is that the induced inner product is *diagonal in the monomial basis* — cross terms $\langle e^*_I,e^*_{I'}\rangle$ vanish for $I\neq I'$ — so the only surviving contributions are the diagonal ones, and on the diagonal the star's two sign-factors square away. The trigger for the second route is that $\langle\star\omega,\star\eta\rangle$ is a pairing of a $\Lambda^{n-k}$-form with a $\Lambda^{n-k}$-form, and the defining relation converts exactly such a pairing (against $\mathrm{vol}$) into a wedge.

**Theorem routing.** *Route A (basis monomials):* by bilinearity, reduce to $\omega=e^*_I$, $\eta=e^*_{I'}$; apply property (1) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]] to each; use diagonality of $\langle\cdot,\cdot\rangle$ to kill the off-diagonal case and, on the diagonal, use $\epsilon_I\epsilon_J=(-1)^p$ to produce the scalar. *Route B (defining relation):* apply the defining relation of [[Def - Hodge Star in Arbitrary Signature]] with $\star\omega$ in the second slot to write $\eta\wedge\star\omega=\langle\star\eta,\star\omega\rangle\mathrm{vol}$, then compute $\eta\wedge\star\omega$ independently using graded commutativity of the wedge and the double-star formula (property (2), [[Ex - Double Star Sign in Arbitrary Signature]]).

**Key decision point.** In Route A the decisive move is recognising that $I\neq I'$ forces $J\neq J'$ (complementation is a bijection), so the star images are orthogonal and both sides vanish, leaving only $I=I'$; there the two sign-factors $\operatorname{sign}(IJ)$ appear squared and disappear, and the metric factor $\epsilon_J$ converts to $(-1)^p\epsilon_I$ via $\epsilon_I\epsilon_J=(-1)^p$. In Route B the decisive move is choosing to feed $\star\omega$ (not $\omega$) into the second slot of the defining relation, so that the pairing that appears is exactly $\langle\star\eta,\star\omega\rangle$; the rest is the double-star bookkeeping. The tempting error — assuming outright that $\star$ preserves the inner product — is dismantled in the warning callout with the counterexample $dt\wedge dx$.

---

# Legal Operations Used

This solution deploys the following legal operations (numbered as they will appear on the topic page; until it is written they are named descriptively).

1. **Reduce a bilinear identity to basis monomials.** Both sides of $\langle\star\omega,\star\eta\rangle=(-1)^p\langle\omega,\eta\rangle$ are bilinear in $(\omega,\eta)$, so it suffices to verify it for $\omega=e^*_I$ and $\eta=e^*_{I'}$ ranging over the monomial basis.

2. **Evaluate the star on monomials via property (1).** Replace $\star e^*_I$ by $\epsilon_J\operatorname{sign}(IJ)\,e^*_J$ from [[Thm - Properties of the Hodge Star in Arbitrary Signature]].

3. **Use diagonality of the induced inner product to eliminate off-diagonal terms.** Since $\langle e^*_J,e^*_{J'}\rangle=0$ for $J\neq J'$ and complementation $I\mapsto J$ is a bijection, the case $I\neq I'$ makes both sides zero; only $I=I'$ survives.

4. **Square away permutation signs.** On the diagonal the factor $\operatorname{sign}(IJ)^2=1$.

5. **Convert a complementary $\epsilon$-product to the index sign.** Use $\epsilon_I\epsilon_J=\prod_{j=1}^n\epsilon_j=(-1)^p$ to rewrite $\epsilon_J=(-1)^p\epsilon_I$ (Route A), or to run the double-star formula (Route B).

6. **Feed the star image into the defining relation (Route B).** Apply $\omega'\wedge\eta'=\langle\star\omega',\eta'\rangle\mathrm{vol}$ with $\omega'=\eta$, $\eta'=\star\omega$ to expose the pairing $\langle\star\eta,\star\omega\rangle$.

7. **Reorder a wedge of a $k$-form and an $(n-k)$-form (Route B).** Use $\eta\wedge\star\omega=(-1)^{k(n-k)}\star\omega\wedge\eta$ and then the double-star formula (property (2), [[Ex - Double Star Sign in Arbitrary Signature]]).

---

# Hints

> [!note]- Hint 1
> Both sides are bilinear in $(\omega,\eta)$. Reduce to the case $\omega=e^*_I$, $\eta=e^*_{I'}$, two monomials of degree $k$. Apply property (1) to each and remember that distinct monomials are orthogonal.

> [!note]- Hint 2 (Route A: the off-diagonal case is free)
> If $I\neq I'$, then their complements satisfy $J\neq J'$, so $\langle\star e^*_I,\star e^*_{I'}\rangle$ is a multiple of $\langle e^*_J,e^*_{J'}\rangle=0$, while $\langle e^*_I,e^*_{I'}\rangle=0$ too. Both sides vanish. So you only need to handle $I=I'$.

> [!note]- Hint 3 (Route A: the diagonal case)
> For $I=I'$: $\langle\star e^*_I,\star e^*_I\rangle=\epsilon_J^2\operatorname{sign}(IJ)^2\langle e^*_J,e^*_J\rangle$. Now $\epsilon_J^2=1$, $\operatorname{sign}(IJ)^2=1$, and $\langle e^*_J,e^*_J\rangle=\epsilon_J$. So the left side is $\epsilon_J$. You want to compare it with $(-1)^p\langle e^*_I,e^*_I\rangle=(-1)^p\epsilon_I$. What is $\epsilon_I\epsilon_J$?

> [!note]- Hint 4 (Route B: the defining relation)
> Put $\star\omega$ into the *second* slot of the defining relation applied to $\eta$: $\eta\wedge\star\omega=\langle\star\eta,\star\omega\rangle\mathrm{vol}$. Then compute $\eta\wedge\star\omega$ another way: swap the two factors ($\eta$ is a $k$-form, $\star\omega$ an $(n-k)$-form, costing $(-1)^{k(n-k)}$), apply the defining relation to $\star\omega$, and use the double-star formula $\star\star\omega=(-1)^{k(n-k)+p}\omega$. The exponents $k(n-k)$ cancel and $(-1)^p$ remains.

---

# Solution

The plan is to prove the identity on the monomial basis (Route A) and then to re-derive it from the defining relation and the double-star formula (Route B) as an independent check. In Route A the induced inner product is diagonal in the monomial basis, so the only surviving terms are the diagonal ones, and there the permutation signs square to $1$ while the $\epsilon$-product over a complementary pair collapses to $(-1)^p$. In Route B the defining relation converts the pairing $\langle\star\omega,\star\eta\rangle$ into a wedge, which graded commutativity and the double-star formula evaluate to $(-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$.

Throughout fix a positively oriented generalized orthonormal basis $e_1,\dots,e_n$ with $\langle e_j,e_j\rangle=\epsilon_j\in\{+1,-1\}$, dual basis $e^*_j$, and $\mathrm{vol}=e^*_1\wedge\dots\wedge e^*_n$. For an increasing multi-index $I$ let $J$ be its increasing complement in $\{1,\dots,n\}$, and write $\epsilon_I=\prod_{i\in I}\epsilon_i$, $\epsilon_J=\prod_{j\in J}\epsilon_j$.

**Step 1: Reduce to basis monomials.**

Both $(\omega,\eta)\mapsto\langle\star\omega,\star\eta\rangle$ and $(\omega,\eta)\mapsto(-1)^p\langle\omega,\eta\rangle$ are bilinear, so it suffices to prove $\langle\star e^*_I,\star e^*_{I'}\rangle=(-1)^p\langle e^*_I,e^*_{I'}\rangle$ for all pairs of increasing $k$-multi-indices $I,I'$.

> [!note]- Derivation
> Write $\omega=\sum_I a_I e^*_I$ and $\eta=\sum_{I'}b_{I'}e^*_{I'}$ with $a_I,b_{I'}\in\mathbb{R}$, the sums over increasing $k$-multi-indices. Since $\star$ is linear (by [[Def - Hodge Star in Arbitrary Signature|its definition]]) and $\langle\cdot,\cdot\rangle$ is bilinear (by [[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms|its definition]]),
> $$\langle\star\omega,\star\eta\rangle=\sum_{I,I'}a_I b_{I'}\langle\star e^*_I,\star e^*_{I'}\rangle,\qquad(-1)^p\langle\omega,\eta\rangle=\sum_{I,I'}a_I b_{I'}(-1)^p\langle e^*_I,e^*_{I'}\rangle\qquad\text{(bilinearity of both sides).}$$
> If the two coefficients $\langle\star e^*_I,\star e^*_{I'}\rangle$ and $(-1)^p\langle e^*_I,e^*_{I'}\rangle$ agree for every pair $(I,I')$, the two sums agree term by term, and the identity holds for all $\omega,\eta$. So the monomial case is equivalent to the general case.

**Step 2 (Route A): The off-diagonal case $I\neq I'$ makes both sides vanish.**

If $I\neq I'$ then $J\neq J'$, and distinct monomials are orthogonal, so $\langle\star e^*_I,\star e^*_{I'}\rangle=0=\langle e^*_I,e^*_{I'}\rangle$.

> [!note]- Derivation
> By property (1) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]], $\star e^*_I=\epsilon_J\operatorname{sign}(IJ)\,e^*_J$ and $\star e^*_{I'}=\epsilon_{J'}\operatorname{sign}(I'J')\,e^*_{J'}$, where $J,J'$ are the increasing complements of $I,I'$. Hence, pulling the scalars out of the bilinear form,
> $$\langle\star e^*_I,\star e^*_{I'}\rangle=\epsilon_J\epsilon_{J'}\operatorname{sign}(IJ)\operatorname{sign}(I'J')\,\langle e^*_J,e^*_{J'}\rangle\qquad\text{(property (1) twice, bilinearity).}$$
> Complementation is a bijection on subsets of $\{1,\dots,n\}$: a set is determined by its complement. So $I\neq I'$ implies $J\neq J'$, and by diagonality of the induced inner product (part of [[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms|the definition]]) $\langle e^*_J,e^*_{J'}\rangle=0$. Thus $\langle\star e^*_I,\star e^*_{I'}\rangle=0$. Likewise $\langle e^*_I,e^*_{I'}\rangle=0$ since $I\neq I'$. Both sides of the identity are $0$, so they agree.

**Step 3 (Route A): The diagonal case $I=I'$ gives the sign $(-1)^p$.**

For $I=I'$ the permutation signs square to $1$ and $\langle\star e^*_I,\star e^*_I\rangle=\epsilon_J$, which equals $(-1)^p\epsilon_I$ because $\epsilon_I\epsilon_J=(-1)^p$.

> [!note]- Derivation
> Set $I'=I$, so $J'=J$. From the displayed formula in Step 2,
> $$\langle\star e^*_I,\star e^*_I\rangle=\epsilon_J^2\,\operatorname{sign}(IJ)^2\,\langle e^*_J,e^*_J\rangle\qquad\text{(the formula of Step 2 with }I'=I\text{).}$$
> Here $\epsilon_J^2=1$ (each $\epsilon_j=\pm1$), $\operatorname{sign}(IJ)^2=1$ (a sign is $\pm1$), and $\langle e^*_J,e^*_J\rangle=\epsilon_J$ (the diagonal value of the induced inner product). Therefore
> $$\langle\star e^*_I,\star e^*_I\rangle=\epsilon_J.$$
> On the other hand, since $I\sqcup J=\{1,\dots,n\}$ and exactly $p$ of the $\epsilon_j$ equal $-1$,
> $$\epsilon_I\epsilon_J=\prod_{j=1}^n\epsilon_j=(-1)^p\qquad\text{(complementary index sets exhaust all }\epsilon_j\text{; index count).}$$
> As $\epsilon_I=\pm1$ we have $\epsilon_I^{-1}=\epsilon_I$, so $\epsilon_J=(-1)^p\epsilon_I$. Because $\langle e^*_I,e^*_I\rangle=\epsilon_I$, this reads
> $$\langle\star e^*_I,\star e^*_I\rangle=\epsilon_J=(-1)^p\epsilon_I=(-1)^p\langle e^*_I,e^*_I\rangle.$$
> Combined with Step 2, the coefficient identity holds for every pair $(I,I')$, and by Step 1 the identity $\langle\star\omega,\star\eta\rangle=(-1)^p\langle\omega,\eta\rangle$ holds for all $\omega,\eta\in\Lambda^k V^*$.

**Step 4 (Route B): An independent derivation from the defining relation and the double-star formula.**

Applying the defining relation with $\star\omega$ in the second slot gives $\eta\wedge\star\omega=\langle\star\eta,\star\omega\rangle\mathrm{vol}$; evaluating $\eta\wedge\star\omega$ by graded commutativity and the double-star formula gives $(-1)^p\langle\omega,\eta\rangle\mathrm{vol}$. Comparison yields the result.

> [!note]- Derivation
> Let $\omega,\eta\in\Lambda^k V^*$, so $\star\omega\in\Lambda^{n-k}V^*$. The [[Def - Hodge Star in Arbitrary Signature|defining relation]] $\alpha\wedge\beta=\langle\star\alpha,\beta\rangle\mathrm{vol}$ holds for $\alpha\in\Lambda^k V^*$, $\beta\in\Lambda^{n-k}V^*$; apply it with $\alpha=\eta$ and $\beta=\star\omega$:
> $$\eta\wedge\star\omega=\langle\star\eta,\star\omega\rangle\,\mathrm{vol}=\langle\star\omega,\star\eta\rangle\,\mathrm{vol}\qquad\text{(defining relation with }\beta=\star\omega\text{; symmetry of }\langle\cdot,\cdot\rangle\text{).}\tag{$\ast$}$$
> Now compute $\eta\wedge\star\omega$ a second way. Since $\eta$ has degree $k$ and $\star\omega$ has degree $n-k$, graded commutativity of the wedge gives $\eta\wedge\star\omega=(-1)^{k(n-k)}\,\star\omega\wedge\eta$. Apply the defining relation once more, now with $\alpha=\star\omega\in\Lambda^{n-k}V^*$ and $\beta=\eta\in\Lambda^{n-(n-k)}V^*=\Lambda^k V^*$:
> $$\star\omega\wedge\eta=\langle\star\star\omega,\eta\rangle\,\mathrm{vol}\qquad\text{(defining relation applied to the }(n-k)\text{-form }\star\omega\text{).}$$
> By the double-star formula (property (2) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]], proved in [[Ex - Double Star Sign in Arbitrary Signature]]), $\star\star\omega=(-1)^{k(n-k)+p}\omega$, so $\langle\star\star\omega,\eta\rangle=(-1)^{k(n-k)+p}\langle\omega,\eta\rangle$. Combining the last two displays,
> $$\eta\wedge\star\omega=(-1)^{k(n-k)}\,\star\omega\wedge\eta=(-1)^{k(n-k)}(-1)^{k(n-k)+p}\langle\omega,\eta\rangle\,\mathrm{vol}=(-1)^{2k(n-k)+p}\langle\omega,\eta\rangle\,\mathrm{vol}=(-1)^p\langle\omega,\eta\rangle\,\mathrm{vol},$$
> using $(-1)^{2k(n-k)}=1$. Comparing this with $(\ast)$, and cancelling the nonzero $\mathrm{vol}$,
> $$\langle\star\omega,\star\eta\rangle=(-1)^p\langle\omega,\eta\rangle.$$
> This confirms Route A's conclusion by an argument that never expands into a basis.

> [!note]- Complete formal solution
> **Claim.** For an oriented $n$-dimensional real vector space with a non-degenerate symmetric bilinear form of index $p$, the Hodge star satisfies $\langle\star\omega,\star\eta\rangle=(-1)^p\langle\omega,\eta\rangle$ for all $\omega,\eta\in\Lambda^k V^*$.
>
> By bilinearity of both sides it suffices to treat $\omega=e^*_I$, $\eta=e^*_{I'}$ for increasing $k$-multi-indices $I,I'$, in a fixed positively oriented generalized orthonormal basis; let $J,J'$ be the increasing complements. By property (1) of [[Thm - Properties of the Hodge Star in Arbitrary Signature]],
> $$\langle\star e^*_I,\star e^*_{I'}\rangle=\epsilon_J\epsilon_{J'}\operatorname{sign}(IJ)\operatorname{sign}(I'J')\langle e^*_J,e^*_{J'}\rangle.$$
> *Case $I\neq I'$:* complementation is a bijection, so $J\neq J'$, hence $\langle e^*_J,e^*_{J'}\rangle=0$ and also $\langle e^*_I,e^*_{I'}\rangle=0$; both sides vanish. *Case $I=I'$:* then $J=J'$, so
> $$\langle\star e^*_I,\star e^*_I\rangle=\epsilon_J^2\operatorname{sign}(IJ)^2\langle e^*_J,e^*_J\rangle=\epsilon_J,$$
> since $\epsilon_J^2=\operatorname{sign}(IJ)^2=1$ and $\langle e^*_J,e^*_J\rangle=\epsilon_J$. As $I\sqcup J=\{1,\dots,n\}$ and exactly $p$ of the $\epsilon_j$ are $-1$, $\epsilon_I\epsilon_J=\prod_{j=1}^n\epsilon_j=(-1)^p$, whence $\epsilon_J=(-1)^p\epsilon_I=(-1)^p\langle e^*_I,e^*_I\rangle$. In both cases $\langle\star e^*_I,\star e^*_{I'}\rangle=(-1)^p\langle e^*_I,e^*_{I'}\rangle$, and bilinearity extends the identity to all $\omega,\eta$. $\blacksquare$

> [!warning] Illegal but tempting: assuming $\star$ is an isometry in Lorentzian signature
> It is tempting to assert that the Hodge star preserves the inner product, $\langle\star\omega,\star\eta\rangle=\langle\omega,\eta\rangle$ — which is true in Riemannian signature ($p=0$), where the theorem reduces to it. In indefinite signature this is false: the correct factor is $(-1)^p$, and it is $-1$ whenever $p$ is odd. The smallest witness is $\omega=dt\wedge dx$ on Minkowski $\mathbb{R}^{1,3}$ with signature $(-,+,+,+)$, $p=1$. Here $\langle dt\wedge dx,dt\wedge dx\rangle=\epsilon_1\epsilon_2=(-1)(+1)=-1$, while $\star(dt\wedge dx)=dy\wedge dz$ (property (1): $\epsilon_3\epsilon_4\operatorname{sign}(1,2,3,4)=+1$) has $\langle dy\wedge dz,dy\wedge dz\rangle=\epsilon_3\epsilon_4=(+1)(+1)=+1$. Thus $\langle\star\omega,\star\omega\rangle=+1\neq-1=\langle\omega,\omega\rangle$; the two differ by exactly $(-1)^p=-1$. The isometry claim would make $\star$ preserve the sign of $\langle\omega,\omega\rangle$, whereas on a timelike two-form the star flips a negative square to a positive one. The assumption becomes legal only when $p$ is even (in particular $p=0$), and it is precisely because $p=0$ in the Riemannian four-dimensional case that $\star$ is a genuine isometry there — the hypothesis underlying the self-dual/anti-self-dual splitting of [[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions]].

---

# Key Takeaways

**When an operator is claimed to preserve a bilinear form up to a scalar, diagonalise the form and let the off-diagonal terms vanish for free.** The engine of Route A is that the induced inner product is diagonal in the monomial basis, so the entire identity reduces to two disjoint checks: an off-diagonal check, where distinct index sets have distinct complements and orthogonality kills both sides instantly, and a diagonal check, where the only surviving quantities are $\pm1$'s that either square away or convert into the target sign. The reusable principle is that verifying "$T$ preserves $\langle\cdot,\cdot\rangle$ up to $\lambda$" almost never requires a general pair of vectors: choose the basis that diagonalises the form, and the problem collapses to a finite set of scalar identities. The trigger condition is any statement of the shape $\langle Tx,Ty\rangle=\lambda\langle x,y\rangle$ where a natural orthogonal basis is available; the transferable diagnostic is to first dispose of the off-diagonal terms by an orthogonality-plus-injectivity argument (here, complementation is a bijection), then read the scalar off the diagonal.

**Two independent proofs of the same identity are a genuine check, and each exposes a different mechanism.** Route A works inside a basis and shows *where* the sign comes from — the metric factor $\epsilon_I\epsilon_J=(-1)^p$ — while Route B works basis-free and shows *how the sign propagates* through the defining relation and the double-star formula, with the permutation exponents $k(n-k)$ cancelling in the pair $(-1)^{k(n-k)}\cdot(-1)^{k(n-k)+p}$. That two routes converge on the same $(-1)^p$ is strong evidence the sign is correct, and it also teaches which tool to reach for elsewhere: when a later problem needs $\langle\star\omega,\star\eta\rangle$ and a basis is clumsy — for instance on a manifold, pointwise, where no global orthonormal frame exists — Route B still runs verbatim, because the defining relation and the double-star formula are frame-independent. Property (3) is in fact the workhorse behind the $L^2$ inner product on forms: $\int_M\langle\omega,\eta\rangle\,\mathrm{vol}$ is manipulated through the star exactly by this isometry-up-to-sign, and the $(-1)^p$ is what distinguishes the Lorentzian variational calculus of electrodynamics from the Riemannian one.

**The failure of the isometry in indefinite signature is not a defect but the content of the theorem, and it governs where self-duality can live.** In Riemannian signature $\star$ is a true isometry, and this is exactly the hypothesis that lets $\Lambda^2$ of a Euclidean four-space split orthogonally into self-dual and anti-self-dual pieces (see [[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions]]). In Lorentzian signature the extra $(-1)^p=-1$ means the star reverses the sign of the norm on timelike forms, so it is an anti-isometry on part of the space and no real eigenspace splitting exists — one is forced to complexify. The diagnostic to carry away is that the single scalar $(-1)^p$ decides whether "the Hodge star is orthogonal" is available: it is exactly when the index is even. This is why gauge theory builds its instanton moduli spaces over Riemannian four-manifolds, where $p=0$ makes $\star$ an isometric involution on two-forms, rather than over Lorentzian spacetimes, where the same operator neither is an isometry nor squares to $+1$.

---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Pfaffian"
  - "Thm - Determinant is Multiplicative"
  - "Def - Ad-Invariant Polynomial"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $m\ge1$ is a fixed integer and we work over $\mathbb{R}$. We write $\operatorname{Mat}(2m\times2m;\mathbb{R})$ for the real $2m\times 2m$ matrices, $A_{ij}$ for the entry of $A$ in row $i$ and column $j$, and $A^t$ for the transpose, $(A^t)_{ij}=A_{ji}$. A matrix is **skew-symmetric** if $A^t=-A$; by the [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups|classification of the Lie algebras of the classical matrix groups]] — which identifies $\mathfrak{so}(n)$ with $\{A\in\operatorname{Mat}(n\times n;\mathbb{R}):A^t+A=0\}$ and computes its dimension as $\binom{n}{2}$ — the Lie algebra of the special orthogonal group is exactly the space of skew-symmetric matrices,
$$\mathfrak{so}(2m)=\{A\in\operatorname{Mat}(2m\times2m;\mathbb{R}):A^t+A=0\},\qquad \dim\mathfrak{so}(2m)=\binom{2m}{2}=m(2m-1),$$
and the Pfaffian lives on this space. We write $I_n$ for the $n\times n$ identity, $\det A$ for the [[Def - Determinant|determinant]] (the unique [[Def - Alternating Multilinear Form|alternating multilinear]] function of the columns with $\det I_n=1$), and $S_N$ for the symmetric group on $\{1,\dots,N\}$ with sign homomorphism $\operatorname{sign}\colon S_N\to\{\pm1\}$.

We write $O(2m)=\{g:g^tg=I_{2m}\}$ for the orthogonal group and $SO(2m)=\{g\in O(2m):\det g=1\}$ for its identity component; for $g\in O(2m)$ we have $g^{-1}=g^t$ and $\det g\in\{+1,-1\}$, with $\det g=+1$ exactly on $SO(2m)$. The adjoint action of a matrix group on its Lie algebra is conjugation, $\operatorname{Ad}_g X=gXg^{-1}$ (series convention); for $g\in O(2m)$ and $X\in\mathfrak{so}(2m)$ this reads $\operatorname{Ad}_g X=gXg^t$.

Let $(e_1,\dots,e_{2m})$ be the standard ordered basis of $\mathbb{R}^{2m}$ and $\Lambda^\bullet\mathbb{R}^{2m}$ the exterior algebra, with wedge product $\wedge$ and the graded-commutativity rule $\alpha\wedge\beta=(-1)^{(\deg\alpha)(\deg\beta)}\beta\wedge\alpha$ of [[Thm - Wedge Product Properties]]; even-degree elements therefore commute among themselves. The top space $\Lambda^{2m}\mathbb{R}^{2m}$ is one-dimensional, spanned by $e_1\wedge\dots\wedge e_{2m}$, and we use the identification $\Lambda^{2m}\mathbb{R}^{2m}\cong\mathbb{R}$, $e_1\wedge\dots\wedge e_{2m}\mapsto1$, of [[Def - Alternating Tensor and Lambda k V Dual]]. To each $A\in\mathfrak{so}(2m)$ we attach, exactly as on [[Def - Pfaffian]], the **fundamental $2$-vector**
$$\sigma_A:=\sum_{1\le i<j\le 2m}A_{ij}\,e_i\wedge e_j\;\in\;\Lambda^2\mathbb{R}^{2m}.$$
For a matrix $M\in\operatorname{Mat}(2m\times2m;\mathbb{R})$ we write $\underline{M}\colon\mathbb{R}^{2m}\to\mathbb{R}^{2m}$, $\underline{M}(x)=Mx$, for the associated linear map ($\underline{M}(e_j)=\sum_i M_{ij}e_i$), and $\Lambda^k\underline{M}\colon\Lambda^k\mathbb{R}^{2m}\to\Lambda^k\mathbb{R}^{2m}$ for the map it induces on $k$-vectors, $\Lambda^k\underline{M}(v_1\wedge\dots\wedge v_k)=(\underline{M}v_1)\wedge\dots\wedge(\underline{M}v_k)$.

The definition of the Pfaffian and its two equivalent forms are those of [[Def - Pfaffian]], recalled here for self-containedness.

![[Def - Pfaffian#The Definition]]

The three conditions defining an invariant polynomial, used in clause (c), are those of [[Def - Ad-Invariant Polynomial]].

![[Def - Ad-Invariant Polynomial#The Definition]]

> [!warning] Convention: Bär's normalisation of the Pfaffian
> Bär (*Gauge Theory*, Example 2.5.14, the source of clauses via B-I2.5.2 and B-E2.5.4) writes $\operatorname{Pf}_{\text{Bär}}(\sigma)=\lambda(\sigma,\dots,\sigma)=\sigma_A^{\wedge m}$, which equals $m!\operatorname{Pf}(A)$ in the series' normalisation (proved on [[Def - Pfaffian]]). All statements on this page use the series' $\operatorname{Pf}$, normalised so that $\operatorname{Pf}\!\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)=1$; every clause below is invariant under the choice of normalisation up to the overall constant $m!$, and the transformation and squaring laws (a), (b) are normalisation-independent identities.

---

# Statement

> **Theorem (properties of the Pfaffian).** Let $m\ge1$, let $A\in\mathfrak{so}(2m)$ be a real skew-symmetric $2m\times2m$ matrix, and let $B\in\operatorname{Mat}(2m\times2m;\mathbb{R})$ be arbitrary. Then:
>
> **(a) Congruence law.** The matrix $B^tAB$ is again skew-symmetric, and
> $$\operatorname{Pf}(B^tAB)=\det(B)\,\operatorname{Pf}(A).$$
>
> **(b) Square of the Pfaffian.** $\displaystyle \operatorname{Pf}(A)^2=\det A.$
>
> **(c) Invariance and homogeneity.** $\operatorname{Pf}$ is a polynomial map $\mathfrak{so}(2m)\to\mathbb{R}$, homogeneous of degree $m$, and invariant under the adjoint action of $SO(2m)$: $\operatorname{Pf}(\operatorname{Ad}_gA)=\operatorname{Pf}(A)$ for all $g\in SO(2m)$. Hence $\operatorname{Pf}\in I(SO(2m))$, the ring of [[Def - Ad-Invariant Polynomial|invariant polynomials]]. For an orientation-reversing orthogonal $g\in O(2m)\setminus SO(2m)$ it changes sign, $\operatorname{Pf}(\operatorname{Ad}_gA)=-\operatorname{Pf}(A)$; so $\operatorname{Pf}\notin I(O(2m))$ for $m\ge1$.
>
> **(d) Block additivity (multiplicativity).** If $A=\operatorname{diag}(A_1,\dots,A_r)$ is block-diagonal with $A_s\in\mathfrak{so}(2m_s)$ and $\sum_{s}m_s=m$, then
> $$\operatorname{Pf}(A)=\prod_{s=1}^{r}\operatorname{Pf}(A_s).$$
>
> **(e) $\det=\operatorname{Pf}^2$ as polynomials, and irreducibility relative to the Pontryagin data.** As polynomial functions on the vector space $\mathfrak{so}(2m)$, the determinant equals the square of the Pfaffian, $\det=\operatorname{Pf}^2$. Consequently $\operatorname{Pf}$ is *not* an element of the subring of $\mathbb{R}[\mathfrak{so}(2m)]$ generated by the coefficients of the characteristic polynomial: it is a genuinely new $SO(2m)$-invariant, adjoined to the $O(2m)$-invariants precisely subject to the relation $\operatorname{Pf}^2=\det$.

---

# Motivation

The Pfaffian was defined on [[Def - Pfaffian]] as a signed sum over perfect matchings; that definition is a computational recipe and, by itself, says nothing about why the object deserves the name "square root of the determinant" or why it belongs to the input data of Chern–Weil theory. This page supplies the five structural facts that turn the recipe into a usable invariant. Their combined effect is to certify that the Pfaffian is admissible fuel for the Chern–Weil homomorphism and that the characteristic class it produces — the [[Def - Euler Class of an Oriented Vector Bundle|Euler class]] — has exactly the properties one demands of an oriented invariant.

Chern–Weil theory ([[Thm - Chern-Weil Theorem]]) takes an $\operatorname{Ad}$-invariant homogeneous polynomial $p$ of degree $d$ on the structure Lie algebra and returns a closed $2d$-form $p(F_\omega)$ whose de Rham class is independent of the connection. To use the Pfaffian as such a $p$ on an $SO(2m)$-bundle we must know three things about it: that it is a polynomial, that it is homogeneous of the correct degree $m$, and that it is $\operatorname{Ad}(SO(2m))$-invariant. Clause (c) is precisely this triple of admissibility conditions, and it is the reason the Euler class is well defined at all.

The remaining clauses are what make the Euler class *interesting* rather than merely defined. Clause (a), the congruence law $\operatorname{Pf}(B^tAB)=\det(B)\operatorname{Pf}(A)$, is the engine: it drives both the invariance in (c) (specialise $B$ to an orthogonal matrix) and the squaring identity in (b) (reduce $A$ to a standard normal form by congruence). Clause (b), $\operatorname{Pf}^2=\det$, is the identity that ties the Euler class to the Pontryagin classes through $e(E)^2=p_m(E)$, and it is the reason the top Pontryagin class of an oriented bundle is a perfect square. Clause (d) is the additivity that yields the Whitney formula $e(E_1\oplus E_2)=e(E_1)\smile e(E_2)$ for the Euler class and the vanishing of $e$ on a bundle with a nowhere-zero section. Clause (e) records the decisive fact: the Pfaffian is genuinely new — no polynomial in the $O(2m)$-invariants (the Pontryagin data) can reproduce it — and this is exactly why the Euler class carries orientation information that the Pontryagin classes cannot.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of every clause is mild — $A$ skew, $B$ arbitrary — so the useful "source" question is: when does a computation secretly reduce to one of these clauses even though no Pfaffian is named?

The first disguised source is **any invariance-under-congruence computation on an antisymmetric object**. Whenever one changes basis in a space carrying an alternating bilinear form — a symplectic form, a curvature $2$-form read in a new frame, an intersection pairing on an even lattice — the matrix transforms as $A\mapsto B^tAB$, and clause (a) computes the effect on the Pfaffian in a single factor $\det(B)$. The non-obvious bridge is that the *quadratic* transformation of the determinant, $\det(B^tAB)=\det(B)^2\det(A)$, factors through the *linear* transformation of the Pfaffian; recognising that a quantity transforming by $\det(B)^2$ has a natural square root transforming by $\det(B)$ is the whole move. *Example problem:* show that a symplectic change of basis ($B\in Sp(2m,\mathbb{R})$, so $\det B=1$) leaves the Pfaffian of the form matrix unchanged, recovering the coordinate-independence of the symplectic volume.

The second disguised source is **a skew-symmetric matrix that can be block-diagonalised or brought to a normal form by congruence**. The moment one has written $A=B^t J B$ with $J$ standard block-diagonal — which the spectral reduction of skew matrices always permits — clauses (a) and (d) together evaluate $\operatorname{Pf}(A)$ from the blocks. The non-obvious step is that congruence, not similarity, is the correct equivalence for the Pfaffian: two skew matrices with the same Pfaffian need not be conjugate, but the congruence normal form is exactly adapted. *Example problem:* compute the Pfaffian of the $2m\times2m$ matrix of a nondegenerate alternating form by reducing it to the standard symplectic block form and reading off $\operatorname{Pf}=\pm1$ times a determinant factor.

The third disguised source is **a determinant of a skew matrix that one wants a signed square root of**. Any time a determinant appears that is known to be a perfect square — the discriminant of a free-fermion system, the determinant of a curvature form on an even-rank oriented bundle, the determinant of an antisymmetric adjacency-type matrix — clause (b) exhibits its polynomial square root, and clause (c) tells you the sign is orientation data, not arbitrary. The non-obvious bridge is that "$\det A$ is a perfect square" is not a numerical accident but a consequence of $A$ being skew; the square root exists at the level of *polynomials*, not just of numbers. *Example problem:* given that the determinant of the $4\times4$ curvature matrix of an oriented rank-$4$ bundle is a perfect square of $2$-forms, produce that square root as $\operatorname{Pf}(F)$ and integrate it to obtain the Euler number.

**Targets (Output Amplification)**

Combine clause (c) with **the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]]** — for an $\operatorname{Ad}$-invariant homogeneous polynomial $p$ of degree $d$ on the structure Lie algebra, $p(F_\omega)$ is closed and its class is connection-independent. Feeding $p=\operatorname{Pf}$ on an $SO(2m)$-bundle produces the [[Def - Euler Class of an Oriented Vector Bundle|Euler class]] $e(E)=[\operatorname{Pf}(F/2\pi)]\in H^{2m}_{dR}(M)$. The extra ingredient is the admissibility triple of (c); the payoff is a genuinely new characteristic class beyond the Chern and Pontryagin classes.

Combine clause (b) with **the definition of the top [[Def - Pontryagin Classes|Pontryagin class]]** $p_m(E)$. Since $\operatorname{Pf}^2=\det$ holds as a polynomial identity, applying both sides to the curvature and taking de Rham classes gives $e(E)^2=p_m(E)$ for an oriented rank-$2m$ bundle. The extra ingredient is the Chern–Weil description of $p_m$ as (up to normalisation) the top coefficient of $\det$; the payoff is one of the standard relations constraining the characteristic classes of a manifold, and a divisibility constraint on $p_m$.

Combine clause (d) with **the reduction of the structure group of a bundle with a nowhere-vanishing section**. A nowhere-zero section reduces the structure group of an oriented rank-$2m$ bundle to $SO(2m-1)$, which sits in $\mathfrak{so}(2m)$ as matrices with a zero final row and column; such a matrix has a zero row, hence vanishing determinant, so by clause (b) — $\operatorname{Pf}^2=\det$ — its Pfaffian is zero, and $e(E)=0$. The extra ingredient is the structure-group reduction; the payoff is that the Euler class is an obstruction to the existence of a nowhere-zero section — the algebraic shadow of the Poincaré–Hopf theorem.

---

# Why Is It True

Strip away the formulas and picture what the Pfaffian is: it is one half of the determinant, in the precise sense that the determinant of a skew matrix always factors as a square, and the Pfaffian is the factor. Every clause is a manifestation of the single mechanism that the exterior-algebra description makes visible.

That description says $\operatorname{Pf}(A)$ is the coefficient of $\tfrac{1}{m!}\sigma_A^{\wedge m}$ in the top form, where $\sigma_A=\sum_{i<j}A_{ij}e_i\wedge e_j$ is a $2$-vector. A $2$-vector is exactly the kind of object that transforms *linearly* under a change of basis, and taking its $m$-th wedge power lands in the one-dimensional top space, where a linear map acts by its determinant. So a change of basis $B$ acts on $\sigma_A$ by $\Lambda^2\underline{B^t}$ and on the top form by $\det(B)$; that is the whole of clause (a). The determinant, by contrast, is the coefficient of the top wedge power of the $2m$ *column vectors* — a degree-$2m$ object — and it transforms by $\det(B)^2$ under congruence, which is why $\det$ is $O(2m)$-invariant while $\operatorname{Pf}$ is only $SO(2m)$-invariant: the determinant has thrown away the sign that the Pfaffian keeps.

**The one mechanism is that the Pfaffian is a top exterior power in disguise, so a change of basis acts on it by a single determinant factor $\det(B)$, whereas the determinant, being a squared exterior power, acts by $\det(B)^2$; the Pfaffian is the honest square root that remembers the sign the determinant forgets.**

Once (a) is in hand, the other clauses fall out by choosing $B$ well. For (b), choose $B$ so that $B^tAB$ is the standard block form $J$ (possible for every skew matrix, by the elementary symplectic reduction): then $\operatorname{Pf}(A)^2$ and $\det A$ are both computed from the blocks and both equal $\det(B)^{-2}$ times the same product of block invariants, which are equal because on each standard $2\times2$ block $\operatorname{Pf}=\det=1$ (or both $0$). For (c), choose $B=g^t$ with $g$ orthogonal: then $\det(B)=\det(g)=\pm1$ reports which component of $O(2m)$ the change of basis lies in, and $\operatorname{Pf}$ is invariant on $SO(2m)$ and sign-flipping on the other component. For (d), the exterior form makes block-diagonality manifest: $\sigma_A$ splits as a sum of $2$-vectors living in disjoint coordinate blocks, and only the fully-mixed term of the $m$-th power survives in the top space, delivering the product of the block Pfaffians. Clause (e) is (b) read as a statement about polynomials plus the observation that the Pontryagin data is $O(2m)$-invariant while $\operatorname{Pf}$ is not.

---

# What Makes This Hard

The single non-obvious step is the reduction underlying (b): one must know that every real skew-symmetric matrix is congruent (not merely similar) to a standard block-diagonal matrix, $A=B^tJB$ with $J=\bigoplus\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\oplus 0$, and that the number of nonzero blocks is exactly half the rank of $A$. This is a congruence normal form for alternating forms, proved by a symplectic Gram–Schmidt, and it is genuinely different from the spectral theorem for symmetric matrices; using the orthogonal diagonalisation of $A^tA$ or the complex eigenvalues $\pm i\lambda_k$ instead is a common detour that works but obscures the clean congruence statement. The second trap is a sign-and-degree confusion: the determinant transforms by $\det(B)^2$ and has degree $2m$, the Pfaffian by $\det(B)^1$ and degree $m$, and conflating the two transformation laws (or expecting $\operatorname{Pf}$ to be $O(2m)$-invariant like $\det$) is the error that hides the entire orientation-sensitivity of the Euler class.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Move the whole problem into the exterior algebra. Establish that a change of basis $B$ acts on the fundamental $2$-vector $\sigma_A$ by the induced map $\Lambda^2\underline{B^t}$ and on the top form by $\det(B)$; this gives (a) at once. Prove block additivity (d) directly from the exterior form. Prove the congruence normal form for skew matrices, then combine it with (a) and (d) to get the squaring identity (b). Read off invariance (c) by taking $B$ orthogonal, and (e) by comparing invariance groups.

**Subgoal decomposition:**

1. **Functoriality of exterior powers.** Show $\Lambda\underline{M}$ is an algebra homomorphism of $\Lambda^\bullet\mathbb{R}^{2m}$ and that on the top space $\Lambda^{2m}\underline{M}=\det(M)\cdot\mathrm{id}$.
   - *Hint:* The induced map is defined on decomposables by $v_1\wedge\dots\wedge v_k\mapsto \underline M v_1\wedge\dots\wedge\underline M v_k$; the top-space value is the Leibniz expansion of the determinant.
   - *Why needed:* It is the algebraic content that turns the change of basis into a single determinant factor.

2. **Congruence law for $\sigma_A$.** Show $B^tAB$ is skew and $\sigma_{B^tAB}=\Lambda^2\underline{B^t}(\sigma_A)$.
   - *Hint:* Expand $\sigma_{B^tAB}=\tfrac12\sum_{i,j}(B^tAB)_{ij}e_i\wedge e_j$ and recognise $\sum_i B_{ki}e_i=\underline{B^t}(e_k)=B^te_k$.
   - *Why needed:* Combined with subgoal 1 it is clause (a).

3. **Clause (a).** Take the $m$-th wedge power and apply subgoals 1–2.
   - *Hint:* $\Lambda\underline{B^t}(\sigma_A^{\wedge m})=(\Lambda^2\underline{B^t}\sigma_A)^{\wedge m}=\sigma_{B^tAB}^{\wedge m}$; on the top form $\Lambda\underline{B^t}$ multiplies by $\det(B)$.
   - *Why needed:* It is the engine for (b) and (c).

4. **Clause (d).** Prove block additivity from the exterior form.
   - *Hint:* $\sigma_A=\sum_s\sigma_{A_s}$ with the $\sigma_{A_s}$ in disjoint coordinate blocks; only the term $\bigwedge_s\sigma_{A_s}^{\wedge m_s}$ of the multinomial expansion of $\sigma_A^{\wedge m}$ is nonzero.
   - *Why needed:* It evaluates $\operatorname{Pf}$ and $\det$ of the normal form $J$.

5. **Congruence normal form.** Prove: every $A\in\mathfrak{so}(2m)$ has $P^tAP=J$ for some invertible $P$, with $J$ standard block-diagonal and rank $A=2r$ even.
   - *Hint:* Symplectic Gram–Schmidt on the alternating form $\beta(x,y)=x^tAy$: peel off hyperbolic planes, collect the radical.
   - *Why needed:* It reduces (b) to the block computation.

6. **Clause (b).** Combine (a), (d) and the normal form; split into nonsingular and singular cases.
   - *Hint:* With $A=B^tJB$ ($B=P^{-1}$): $\det A=\det(B)^2\det J$ and $\operatorname{Pf}(A)=\det(B)\operatorname{Pf}(J)$; compute $\det J$ and $\operatorname{Pf}(J)$ from the blocks.
   - *Why needed:* It is the squaring identity and the heart of (e).

7. **Clauses (c) and (e).** Specialise (a) to $B=g^t$ orthogonal; upgrade (b) to a polynomial identity and compare invariance groups.
   - *Hint:* $\det(g)=\pm1$; polynomials agreeing at every point of $\mathfrak{so}(2m)$ are equal; the characteristic-polynomial coefficients are $O(2m)$-invariant.
   - *Why needed:* These are the admissibility and irreducibility statements.

---

# Lemma Decomposition

> [!note]- Lemma 1: Exterior powers of a linear map form an algebra homomorphism whose top component is the determinant
> **Statement:** Let $M\in\operatorname{Mat}(2m\times2m;\mathbb{R})$ and let $\Lambda\underline{M}=\bigoplus_{k}\Lambda^k\underline{M}$ be the induced map on $\Lambda^\bullet\mathbb{R}^{2m}$, where $\Lambda^k\underline{M}(v_1\wedge\dots\wedge v_k)=(\underline{M}v_1)\wedge\dots\wedge(\underline{M}v_k)$. Then (i) $\Lambda\underline{M}$ is well defined, and $\Lambda\underline{M}(\alpha\wedge\beta)=(\Lambda\underline{M}\alpha)\wedge(\Lambda\underline{M}\beta)$ for all $\alpha,\beta$; (ii) on the top space, $\Lambda^{2m}\underline{M}=\det(M)\cdot\mathrm{id}_{\Lambda^{2m}\mathbb{R}^{2m}}$.
>
> **Hint:** For (i), the defining assignment is alternating multilinear in $(v_1,\dots,v_k)$, so it factors through $\Lambda^k$; the homomorphism property is immediate on decomposables. For (ii), expand $\underline M e_1\wedge\dots\wedge\underline M e_{2m}$ by multilinearity and use the Leibniz formula for $\det$.
>
> **Why needed:** It is the algebraic fact that converts the action of a change of basis on $2$-vectors into a single scalar $\det$ on the top form, which is the content of clause (a).
>
> > [!note]- Full proof
> > **Goal.** We must show the induced maps are well defined, multiplicative for the wedge product, and equal to $\det(M)$ on the one-dimensional top space.
> >
> > **Step 1: well-definedness of $\Lambda^k\underline{M}$.** Fix $k$. The map
> > $$(v_1,\dots,v_k)\longmapsto (\underline{M}v_1)\wedge\dots\wedge(\underline{M}v_k)\in\Lambda^k\mathbb{R}^{2m}$$
> > is multilinear (each $\underline M$ is linear and $\wedge$ is multilinear, [[Thm - Wedge Product Properties]]) and alternating (if $v_a=v_b$ for $a\ne b$ then $\underline M v_a=\underline M v_b$ and a wedge with a repeated factor vanishes). By the universal property of the exterior power ([[Def - Alternating Tensor and Lambda k V Dual]]), it factors through a unique linear map $\Lambda^k\underline M\colon\Lambda^k\mathbb{R}^{2m}\to\Lambda^k\mathbb{R}^{2m}$ with the stated values on decomposables. Since every $k$-vector is a linear combination of decomposables $e_{i_1}\wedge\dots\wedge e_{i_k}$, the map is determined on all of $\Lambda^k$.
> >
> > **Step 2: homomorphism property.** It suffices to check on decomposables, by linearity. For $\alpha=v_1\wedge\dots\wedge v_p$ and $\beta=w_1\wedge\dots\wedge w_q$,
> > $$\Lambda\underline M(\alpha\wedge\beta)=\Lambda^{p+q}\underline M(v_1\wedge\dots\wedge v_p\wedge w_1\wedge\dots\wedge w_q)=(\underline M v_1)\wedge\dots\wedge(\underline M v_p)\wedge(\underline M w_1)\wedge\dots\wedge(\underline M w_q)\qquad\text{(Step 1),}$$
> > and this equals $\big((\underline M v_1)\wedge\dots\wedge(\underline M v_p)\big)\wedge\big((\underline M w_1)\wedge\dots\wedge(\underline M w_q)\big)=(\Lambda\underline M\alpha)\wedge(\Lambda\underline M\beta)$ (associativity of $\wedge$). Hence $\Lambda\underline M$ is an algebra homomorphism.
> >
> > **Step 3: value on the top space.** The top space $\Lambda^{2m}\mathbb{R}^{2m}$ is spanned by $e_1\wedge\dots\wedge e_{2m}$. Using $\underline M e_j=\sum_i M_{ij}e_i$ and multilinearity,
> > $$\Lambda^{2m}\underline M(e_1\wedge\dots\wedge e_{2m})=(\underline M e_1)\wedge\dots\wedge(\underline M e_{2m})=\sum_{i_1,\dots,i_{2m}=1}^{2m}M_{i_1 1}\cdots M_{i_{2m}\,2m}\;e_{i_1}\wedge\dots\wedge e_{i_{2m}}\qquad\text{(distributivity of }\wedge\text{).}$$
> > A summand is nonzero only when $(i_1,\dots,i_{2m})$ is a permutation $\tau\in S_{2m}$ of $(1,\dots,2m)$, in which case $e_{\tau(1)}\wedge\dots\wedge e_{\tau(2m)}=\operatorname{sign}(\tau)\,e_1\wedge\dots\wedge e_{2m}$ (reordering rule, [[Thm - Wedge Product Properties]]). Therefore
> > $$\Lambda^{2m}\underline M(e_1\wedge\dots\wedge e_{2m})=\Big(\sum_{\tau\in S_{2m}}\operatorname{sign}(\tau)\prod_{j=1}^{2m}M_{\tau(j)\,j}\Big)e_1\wedge\dots\wedge e_{2m}=\det(M)\,e_1\wedge\dots\wedge e_{2m}\qquad\text{(Leibniz formula for the determinant, [[Def - Determinant]]).}$$
> > As $\Lambda^{2m}\underline M$ is linear on a one-dimensional space and multiplies its generator by $\det(M)$, it is $\det(M)\cdot\mathrm{id}$.
> >
> > **Conclusion.** $\Lambda\underline M$ is a well-defined algebra homomorphism of $\Lambda^\bullet\mathbb{R}^{2m}$, and $\Lambda^{2m}\underline M=\det(M)\cdot\mathrm{id}$. $\blacksquare$

> [!note]- Lemma 2: The congruence law for the fundamental $2$-vector
> **Statement:** For $A\in\mathfrak{so}(2m)$ and $B\in\operatorname{Mat}(2m\times2m;\mathbb{R})$, the matrix $B^tAB$ is skew-symmetric, and its fundamental $2$-vector is the image of $\sigma_A$ under the induced map of $B^t$:
> $$\sigma_{B^tAB}=\Lambda^2\underline{B^t}\,(\sigma_A).$$
>
> **Hint:** Symmetrise $\sigma_C=\tfrac12\sum_{i,j}C_{ij}e_i\wedge e_j$; substitute $C=B^tAB$ and recognise that $\sum_i B_{ki}e_i=B^te_k=\underline{B^t}(e_k)$.
>
> **Why needed:** It says the change of basis acts on $\sigma_A$ exactly by $\Lambda^2\underline{B^t}$; wedged $m$ times and combined with Lemma 1 it is clause (a).
>
> > [!note]- Full proof
> > **Goal.** Given $A$ skew and $B$ arbitrary, verify $B^tAB$ is skew and identify its fundamental $2$-vector with $\Lambda^2\underline{B^t}(\sigma_A)$.
> >
> > **Step 0: skew-symmetry of $B^tAB$.** Using $(XY)^t=Y^tX^t$ and $A^t=-A$,
> > $$(B^tAB)^t=B^tA^t(B^t)^t=B^tA^tB=-B^tAB\qquad\text{(transpose of a product; skew-symmetry of }A\text{).}$$
> > Hence $B^tAB\in\mathfrak{so}(2m)$ and $\sigma_{B^tAB}$ is defined.
> >
> > **Step 1: symmetrise the fundamental $2$-vector.** For any skew $C$, the terms $C_{ij}e_i\wedge e_j$ satisfy $C_{ij}e_i\wedge e_j=C_{ji}e_j\wedge e_i$ (two sign changes, from $C_{ij}=-C_{ji}$ and $e_i\wedge e_j=-e_j\wedge e_i$, cancel), and the diagonal terms vanish ($C_{ii}=0$). Therefore
> > $$\sigma_C=\sum_{i<j}C_{ij}e_i\wedge e_j=\frac12\sum_{i,j=1}^{2m}C_{ij}\,e_i\wedge e_j\qquad\text{(each unordered pair counted twice, diagonal zero).}$$
> >
> > **Step 2: substitute $C=B^tAB$.** With $(B^tAB)_{ij}=\sum_{k,l}(B^t)_{ik}A_{kl}B_{lj}=\sum_{k,l}B_{ki}A_{kl}B_{lj}$,
> > $$\sigma_{B^tAB}=\frac12\sum_{i,j}\Big(\sum_{k,l}B_{ki}A_{kl}B_{lj}\Big)e_i\wedge e_j=\frac12\sum_{k,l}A_{kl}\Big(\sum_i B_{ki}e_i\Big)\wedge\Big(\sum_j B_{lj}e_j\Big)\qquad\text{(regrouping the finite sum; bilinearity of }\wedge\text{).}$$
> >
> > **Step 3: recognise the induced map.** The inner sum is $\sum_i B_{ki}e_i=\sum_i (B^t)_{ik}e_i=B^t e_k=\underline{B^t}(e_k)$. Substituting,
> > $$\sigma_{B^tAB}=\frac12\sum_{k,l}A_{kl}\,\big(\underline{B^t}e_k\big)\wedge\big(\underline{B^t}e_l\big)=\Lambda^2\underline{B^t}\Big(\frac12\sum_{k,l}A_{kl}\,e_k\wedge e_l\Big)=\Lambda^2\underline{B^t}(\sigma_A),$$
> > where the middle equality is the definition of $\Lambda^2\underline{B^t}$ on the decomposable pieces $e_k\wedge e_l$ (Lemma 1, Step 1) and the last is Step 1 applied to $A$ itself.
> >
> > **Conclusion.** $B^tAB$ is skew and $\sigma_{B^tAB}=\Lambda^2\underline{B^t}(\sigma_A)$. $\blacksquare$

> [!note]- Lemma 3: Block additivity of the Pfaffian
> **Statement:** Let $A=\operatorname{diag}(A_1,\dots,A_r)\in\mathfrak{so}(2m)$ be block-diagonal with $A_s\in\mathfrak{so}(2m_s)$ occupying the coordinate block $V_s=\operatorname{span}(e_k:k\in\text{block }s)$, $\sum_s m_s=m$. Then $\operatorname{Pf}(A)=\prod_{s=1}^r\operatorname{Pf}(A_s)$.
>
> **Hint:** $\sigma_A=\sum_s\sigma_{A_s}$ with $\sigma_{A_s}\in\Lambda^2 V_s$; expand $\sigma_A^{\wedge m}$ by the multinomial theorem and note that $\sigma_{A_s}^{\wedge k}=0$ once $k>m_s$, so only the balanced term survives.
>
> **Why needed:** It evaluates the Pfaffian of the standard normal form $J$ used in clause (b), and it is clause (d) itself.
>
> > [!note]- Full proof
> > **Goal.** Reduce the $m$-th wedge power of $\sigma_A$ to the single balanced term $\bigwedge_s\sigma_{A_s}^{\wedge m_s}$ and read off the product of block Pfaffians.
> >
> > **Step 0: the split of $\sigma_A$.** Because $A$ is block-diagonal, $A_{ij}=0$ whenever $i$ and $j$ lie in different blocks; the nonzero above-diagonal entries lie within a single block. Hence
> > $$\sigma_A=\sum_{i<j}A_{ij}e_i\wedge e_j=\sum_{s=1}^r\ \sum_{\substack{i<j\\ i,j\in\text{block }s}}(A_s)_{ij}\,e_i\wedge e_j=\sum_{s=1}^r\sigma_{A_s},\qquad \sigma_{A_s}\in\Lambda^2 V_s,$$
> > where each $\sigma_{A_s}$ is the fundamental $2$-vector of $A_s$, formed from the basis vectors of the block $V_s$.
> >
> > **Step 1: even elements commute, so the multinomial theorem applies.** Each $\sigma_{A_s}$ has even degree $2$, so by graded-commutativity ([[Thm - Wedge Product Properties]]) any two of them commute: $\sigma_{A_s}\wedge\sigma_{A_t}=(-1)^{4}\sigma_{A_t}\wedge\sigma_{A_s}=\sigma_{A_t}\wedge\sigma_{A_s}$. In a commutative setting the multinomial theorem holds, so
> > $$\sigma_A^{\wedge m}=\Big(\sum_{s=1}^r\sigma_{A_s}\Big)^{\wedge m}=\sum_{\substack{k_1,\dots,k_r\ge0\\ k_1+\dots+k_r=m}}\binom{m}{k_1,\dots,k_r}\,\sigma_{A_1}^{\wedge k_1}\wedge\dots\wedge\sigma_{A_r}^{\wedge k_r}\qquad\text{(multinomial theorem for commuting elements).}$$
> >
> > **Step 2: only the balanced term survives.** The element $\sigma_{A_s}^{\wedge k_s}$ lies in $\Lambda^{2k_s}V_s$. Since $\dim V_s=2m_s$, we have $\Lambda^{2k_s}V_s=0$ whenever $2k_s>2m_s$, that is whenever $k_s>m_s$; so a term with any $k_s>m_s$ vanishes. In a surviving term all $k_s\le m_s$, and since $\sum_s k_s=m=\sum_s m_s$, this forces $k_s=m_s$ for every $s$. Thus only the balanced term remains:
> > $$\sigma_A^{\wedge m}=\binom{m}{m_1,\dots,m_r}\,\sigma_{A_1}^{\wedge m_1}\wedge\dots\wedge\sigma_{A_r}^{\wedge m_r}=\frac{m!}{m_1!\cdots m_r!}\,\bigwedge_{s=1}^r\sigma_{A_s}^{\wedge m_s}.$$
> >
> > **Step 3: evaluate each block power.** By the exterior form of the Pfaffian applied inside $V_s$ ([[Def - Pfaffian]]), $\sigma_{A_s}^{\wedge m_s}=m_s!\,\operatorname{Pf}(A_s)\,\Omega_s$, where $\Omega_s=\bigwedge_{k\in\text{block }s}e_k$ is the ordered product of the basis vectors of $V_s$. Since the blocks are consecutive and ordered, $\Omega_1\wedge\dots\wedge\Omega_r=e_1\wedge\dots\wedge e_{2m}$. Substituting into Step 2,
> > $$\sigma_A^{\wedge m}=\frac{m!}{\prod_s m_s!}\prod_{s=1}^r\big(m_s!\,\operatorname{Pf}(A_s)\big)\;e_1\wedge\dots\wedge e_{2m}=m!\,\Big(\prod_{s=1}^r\operatorname{Pf}(A_s)\Big)\,e_1\wedge\dots\wedge e_{2m}\qquad\text{(the factors }m_s!\text{ cancel).}$$
> >
> > **Step 4: read off the Pfaffian.** By the exterior form again, $\sigma_A^{\wedge m}=m!\operatorname{Pf}(A)\,e_1\wedge\dots\wedge e_{2m}$. Comparing coefficients in the one-dimensional top space with Step 3 and cancelling $m!$ gives $\operatorname{Pf}(A)=\prod_{s=1}^r\operatorname{Pf}(A_s)$.
> >
> > **Conclusion.** The Pfaffian of a block-diagonal skew matrix is the product of the Pfaffians of the blocks. In particular a single $2\times2$ block $\left(\begin{smallmatrix}0&a\\-a&0\end{smallmatrix}\right)$ contributes the factor $a$, and a $2\times2$ zero block contributes the factor $0$. $\blacksquare$

> [!note]- Lemma 4: Congruence normal form for skew-symmetric matrices
> **Statement:** For every $A\in\mathfrak{so}(2m)$ there is an invertible $P\in GL(2m,\mathbb{R})$ with
> $$P^tAP=J_r:=\underbrace{\begin{pmatrix}0&1\\-1&0\end{pmatrix}\oplus\dots\oplus\begin{pmatrix}0&1\\-1&0\end{pmatrix}}_{r\text{ standard blocks}}\ \oplus\ 0_{2m-2r},$$
> where $0_{2m-2r}$ is the zero matrix of size $2m-2r$. Moreover $\operatorname{rank}A=2r$ is even, and $A$ is nonsingular if and only if $r=m$ (no zero block).
>
> **Hint:** Work with the alternating bilinear form $\beta(x,y)=x^tAy$. If $\beta\ne0$ pick $u,v$ with $\beta(u,v)=1$; they span a nondegenerate hyperbolic plane $W$; split $V=W\oplus W^{\perp_\beta}$ and induct on $W^{\perp_\beta}$.
>
> **Why needed:** It provides the standard form $J$ into which every skew matrix is congruent, reducing the squaring identity (b) to the block computation of Lemma 3.
>
> > [!note]- Full proof
> > **Goal.** By an inductive symplectic Gram–Schmidt, build a basis in which the alternating form $\beta(x,y)=x^tAy$ has the standard block matrix $J_r$; the change-of-basis matrix is the required $P$.
> >
> > **Setup.** Let $\beta\colon\mathbb{R}^{2m}\times\mathbb{R}^{2m}\to\mathbb{R}$, $\beta(x,y)=x^tAy$. It is bilinear and, since $A^t=-A$, alternating: $\beta(y,x)=y^tAx=(y^tAx)^t=x^tA^ty=-x^tAy=-\beta(x,y)$ (a scalar equals its transpose; skew-symmetry). The matrix of $\beta$ in a basis $(w_1,\dots,w_{2m})$ collected as columns of $P$ is $(P^tAP)_{ij}=w_i^tAw_j=\beta(w_i,w_j)$; so producing a basis with $\beta(w_i,w_j)=(J_r)_{ij}$ is exactly producing $P$ with $P^tAP=J_r$.
> >
> > **Induction on the dimension $2m$.** We prove: any finite-dimensional real space $V$ with an alternating form $\beta$ has a basis in which $\beta$ has matrix $\bigoplus_{i=1}^r\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\oplus 0$, where $2r=\operatorname{rank}\beta$. (Here $V=\mathbb{R}^{2m}$.)
> >
> > **Base case $\beta=0$.** Then any basis gives the zero matrix, $r=0$, and $\operatorname{rank}\beta=0=2r$.
> >
> > **Inductive step $\beta\ne0$.** Since $\beta\ne0$ there are $u,v$ with $\beta(u,v)\ne0$; rescaling $v$ by $1/\beta(u,v)$ we may take $\beta(u,v)=1$. Set $W=\operatorname{span}(u,v)$. The vectors $u,v$ are linearly independent (if $v=cu$ then $\beta(u,v)=c\beta(u,u)=0$ by alternation, contradiction), and on $W$ the form has matrix $\left(\begin{smallmatrix}\beta(u,u)&\beta(u,v)\\\beta(v,u)&\beta(v,v)\end{smallmatrix}\right)=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, so $\beta|_W$ is nondegenerate (its matrix is invertible).
> > **Define the projection to the $\beta$-orthogonal complement.** For $x\in V$ put
> > $$\pi(x):=x-\beta(x,v)\,u+\beta(x,u)\,v .$$
> > Then $\beta(u,\pi(x))=\beta(u,x)-\beta(x,v)\beta(u,u)+\beta(x,u)\beta(u,v)=\beta(u,x)+\beta(x,u)=0$ (using $\beta(u,u)=0$, $\beta(u,v)=1$, and $\beta(x,u)=-\beta(u,x)$), and, by the same computation with $u$ and $v$ interchanged, $\beta(v,\pi(x))=\beta(v,x)-\beta(x,v)\beta(v,u)+\beta(x,u)\beta(v,v)=\beta(v,x)+\beta(x,v)=0$ (using $\beta(v,u)=-1$, $\beta(v,v)=0$). So $\pi(x)\in W^{\perp_\beta}:=\{y:\beta(u,y)=\beta(v,y)=0\}$.
> > **Direct sum $V=W\oplus W^{\perp_\beta}$.** For any $x$, $x=\big(\beta(x,v)u-\beta(x,u)v\big)+\pi(x)$ with the first summand in $W$ and $\pi(x)\in W^{\perp_\beta}$, so $V=W+W^{\perp_\beta}$. If $z\in W\cap W^{\perp_\beta}$, write $z=au+bv$; then $0=\beta(v,z)=a\beta(v,u)=-a$ and $0=\beta(u,z)=b\beta(u,v)=b$, so $z=0$. Hence the sum is direct and $\dim W^{\perp_\beta}=\dim V-2$.
> > **Apply the inductive hypothesis to $W^{\perp_\beta}$.** The restriction $\beta|_{W^{\perp_\beta}}$ is alternating on a space of dimension $\dim V-2$, so by induction it has a basis $(w_3,\dots,w_{2m})$ giving matrix $\bigoplus_{i=2}^{r}\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\oplus 0$. Prepend $(u,v)$: the basis $(u,v,w_3,\dots,w_{2m})$ gives $\beta$ the matrix $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\oplus\big(\bigoplus_{i=2}^r(\dots)\oplus 0\big)=J_r$, because $\beta(u,w_k)=\beta(v,w_k)=0$ for $k\ge3$ (as $w_k\in W^{\perp_\beta}$). This completes the induction.
> >
> > **Rank and nonsingularity.** In the normal-form basis, $J_r$ has $2r$ pivots (the standard blocks are invertible, the zero block contributes none), so $\operatorname{rank}J_r=2r$. Rank is invariant under multiplication by the invertible matrices $P^t,P$, so $\operatorname{rank}A=\operatorname{rank}(P^tAP)=\operatorname{rank}J_r=2r$ is even. Finally $A$ is nonsingular $\iff\operatorname{rank}A=2m\iff r=m\iff J_r$ has no zero block.
> >
> > **Conclusion.** Every skew-symmetric $A$ is congruent to a standard block form $J_r$ with $2r=\operatorname{rank}A$, via an invertible $P$ with $P^tAP=J_r$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $m\ge1$, a skew-symmetric $A\in\mathfrak{so}(2m)$ and an arbitrary $B\in\operatorname{Mat}(2m\times2m;\mathbb{R})$. We prove clauses (a)–(e) in turn, each drawing on the lemmas above.
>
> **Part (a) — the congruence law.** By Lemma 2, $B^tAB$ is skew-symmetric and $\sigma_{B^tAB}=\Lambda^2\underline{B^t}(\sigma_A)$. Take the $m$-th wedge power and use that $\Lambda\underline{B^t}$ is an algebra homomorphism (Lemma 1(i)):
> $$\sigma_{B^tAB}^{\wedge m}=\big(\Lambda^2\underline{B^t}\,\sigma_A\big)^{\wedge m}=\Lambda\underline{B^t}\big(\sigma_A^{\wedge m}\big)\qquad\text{(Lemma 1(i): }\Lambda\underline{B^t}\text{ respects }\wedge\text{).}$$
> The element $\sigma_A^{\wedge m}$ lies in the top space $\Lambda^{2m}\mathbb{R}^{2m}$, on which $\Lambda\underline{B^t}$ acts as multiplication by $\det(B^t)=\det(B)$ (Lemma 1(ii), and $\det(B^t)=\det B$ from [[Def - Determinant]]). Hence, dividing by $m!$,
> $$\frac{1}{m!}\sigma_{B^tAB}^{\wedge m}=\det(B)\cdot\frac{1}{m!}\sigma_A^{\wedge m}.$$
> By the exterior form of the Pfaffian ([[Def - Pfaffian]]), the left side is $\operatorname{Pf}(B^tAB)\,e_1\wedge\dots\wedge e_{2m}$ and the right side is $\det(B)\operatorname{Pf}(A)\,e_1\wedge\dots\wedge e_{2m}$. Comparing coefficients in the one-dimensional top space,
> $$\operatorname{Pf}(B^tAB)=\det(B)\,\operatorname{Pf}(A).$$
>
> **Part (d) — block additivity.** This is exactly Lemma 3: for $A=\operatorname{diag}(A_1,\dots,A_r)$ with $A_s\in\mathfrak{so}(2m_s)$ and $\sum_s m_s=m$, $\operatorname{Pf}(A)=\prod_{s}\operatorname{Pf}(A_s)$. We record for the next part the two elementary values it yields: the standard block $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ has $\operatorname{Pf}=1$ (the $m=1$ case of [[Def - Pfaffian]], upper-right entry $1$) and $\det=0\cdot0-1\cdot(-1)=1$; a $2\times2$ zero block has $\operatorname{Pf}=0$ and $\det=0$.
>
> **Part (b) — the squaring identity.** By Lemma 4 there is an invertible $P$ with $P^tAP=J_r$ the standard block form, $2r=\operatorname{rank}A$. Set $B_0:=P^{-1}$, so that
> $$A=(P^t)^{-1}J_rP^{-1}=(P^{-1})^tJ_r P^{-1}=B_0^t\,J_r\,B_0\qquad\text{(since }(P^t)^{-1}=(P^{-1})^t\text{).}$$
> Apply the determinant, using its multiplicativity — for square matrices $\det(XY)=\det(X)\det(Y)$, restated from [[Thm - Determinant is Multiplicative]]:
>
> ![[Thm - Determinant is Multiplicative#Statement]]
>
> Thus
> $$\det A=\det(B_0^tJ_rB_0)=\det(B_0^t)\det(J_r)\det(B_0)=\det(B_0)^2\det(J_r)\qquad\text{(multiplicativity; }\det B_0^t=\det B_0\text{).}$$
> Apply Part (a) with the same $B_0$:
> $$\operatorname{Pf}(A)=\operatorname{Pf}(B_0^tJ_rB_0)=\det(B_0)\,\operatorname{Pf}(J_r)\qquad\text{(Part (a)).}$$
> It remains to compute $\det(J_r)$ and $\operatorname{Pf}(J_r)$ from the blocks. The Pfaffian factors over the blocks by Part (d): $\operatorname{Pf}(J_r)=\prod(\text{block Pfaffians})$. The determinant factors over the blocks too, and we spell this out rather than assert it: by the Leibniz formula ([[Def - Determinant]]), $\det(J_r)=\sum_{\tau\in S_{2m}}\operatorname{sign}(\tau)\prod_{i=1}^{2m}(J_r)_{\tau(i)\,i}$, and since $(J_r)_{kl}=0$ whenever $k$ and $l$ lie in different blocks, a summand is nonzero only when $\tau$ maps each block's index set to itself; such a $\tau$ factors uniquely as a product of permutations of the individual blocks, its sign is the product of the block signs, and the sum therefore factors as $\det(J_r)=\prod(\text{block determinants})$. We split into the two exhaustive cases by whether $A$ is singular.
>
> *Case 1: $A$ nonsingular, i.e. $\det A\ne0$.* By Lemma 4, $r=m$: $J_r$ consists of $m$ standard blocks and no zero block. Each standard block has $\det=1$ and $\operatorname{Pf}=1$ (Part (d) values), so $\det(J_r)=1$ and $\operatorname{Pf}(J_r)=1$. Therefore
> $$\det A=\det(B_0)^2\cdot 1=\det(B_0)^2,\qquad \operatorname{Pf}(A)^2=\big(\det(B_0)\cdot1\big)^2=\det(B_0)^2,$$
> and comparing the two, $\operatorname{Pf}(A)^2=\det A$.
>
> *Case 2: $A$ singular, i.e. $\det A=0$.* By Lemma 4, $r<m$, so $J_r$ contains at least one $2\times2$ zero block. A zero block has $\det=0$ and $\operatorname{Pf}=0$, so the products give $\det(J_r)=0$ and $\operatorname{Pf}(J_r)=0$. Therefore $\det A=\det(B_0)^2\cdot0=0$ and $\operatorname{Pf}(A)=\det(B_0)\cdot0=0$, whence $\operatorname{Pf}(A)^2=0=\det A$.
>
> The two cases are exhaustive (a square matrix is nonsingular or singular), and in each $\operatorname{Pf}(A)^2=\det A$. This proves (b).
>
> **Part (c) — invariance and homogeneity.** We verify the three defining conditions of an [[Def - Ad-Invariant Polynomial|invariant polynomial]] on $\mathfrak{so}(2m)$ for the group $SO(2m)$.
> *Polynomiality.* By its defining formula ([[Def - Pfaffian]]), $\operatorname{Pf}(A)=\tfrac{1}{2^m m!}\sum_{\sigma\in S_{2m}}\operatorname{sign}(\sigma)\prod_{i=1}^m A_{\sigma(2i-1)\sigma(2i)}$ is a polynomial in the entries $A_{ij}$, hence a polynomial function on the vector space $\mathfrak{so}(2m)$.
> *Homogeneity of degree $m$.* Each summand is a product of exactly $m$ entries, so replacing $A$ by $tA$ ($t\in\mathbb{R}$) multiplies each summand by $t^m$; pulling $t^m$ out, $\operatorname{Pf}(tA)=t^m\operatorname{Pf}(A)$. Thus $\operatorname{Pf}$ is homogeneous of degree $m$.
> *$\operatorname{Ad}(SO(2m))$-invariance.* Let $g\in SO(2m)$. Since $g$ is orthogonal, $g^{-1}=g^t$, so $\operatorname{Ad}_gA=gAg^{-1}=gAg^t$. Writing $gAg^t=(g^t)^tA(g^t)=B^tAB$ with $B=g^t$, Part (a) gives
> $$\operatorname{Pf}(\operatorname{Ad}_gA)=\operatorname{Pf}(g^{t\,t}A\,g^t)=\det(g^t)\operatorname{Pf}(A)=\det(g)\operatorname{Pf}(A)=\operatorname{Pf}(A)\qquad\text{(Part (a); }\det g^t=\det g=1\text{ for }g\in SO(2m)\text{).}$$
> (That $\operatorname{Ad}_gA\in\mathfrak{so}(2m)$ is the Step 0 of Lemma 2 with $B=g^t$.) The three conditions hold, so $\operatorname{Pf}\in I(SO(2m))$.
> *Sign under $O(2m)\setminus SO(2m)$.* If instead $g\in O(2m)$ with $\det g=-1$, the same computation gives $\operatorname{Pf}(\operatorname{Ad}_gA)=\det(g)\operatorname{Pf}(A)=-\operatorname{Pf}(A)$. Since $\operatorname{Pf}$ is not identically zero (for instance $\operatorname{Pf}(J_m)=1$ by Part (d)), it is not $O(2m)$-invariant, i.e. $\operatorname{Pf}\notin I(O(2m))$ for $m\ge1$.
>
> **Part (e) — polynomial identity and irreducibility relative to the Pontryagin data.** By (b), $\det A=\operatorname{Pf}(A)^2$ for every $A\in\mathfrak{so}(2m)$. Both $A\mapsto\det A$ and $A\mapsto\operatorname{Pf}(A)^2$ are polynomial functions of the independent coordinates $\{A_{ij}\}_{1\le i<j\le 2m}$ on $\mathfrak{so}(2m)$; two polynomials over the infinite field $\mathbb{R}$ that agree at every point of $\mathbb{R}^N$ are equal as polynomials. Hence $\det=\operatorname{Pf}^2$ as elements of the polynomial ring $\mathbb{R}[\mathfrak{so}(2m)]$.
> Now suppose, for contradiction, that $\operatorname{Pf}$ lay in the subring $R\subseteq\mathbb{R}[\mathfrak{so}(2m)]$ generated by the coefficients $c_1,\dots,c_{2m}$ of the characteristic polynomial (defined by $\det(tI_{2m}+A)=\sum_{k=0}^{2m}c_k(A)\,t^{2m-k}$). Each $c_k$ is invariant under conjugation by *any* invertible matrix, in particular under $\operatorname{Ad}(O(2m))$: for $g\in O(2m)$,
> $$\det\!\big(tI_{2m}+gAg^{-1}\big)=\det\!\big(g(tI_{2m}+A)g^{-1}\big)=\det(tI_{2m}+A)\qquad\text{(multiplicativity of }\det\text{, [[Thm - Determinant is Multiplicative]]),}$$
> so $c_k(\operatorname{Ad}_gA)=c_k(A)$ for all $k$. Any element of the subring $R$ is a polynomial in the $c_k$ and is therefore also $\operatorname{Ad}(O(2m))$-invariant. But by Part (c), $\operatorname{Pf}$ changes sign under an orientation-reversing $g$ and is not $O(2m)$-invariant. This is the contradiction (an $O(2m)$-invariant that is also sign-changing must vanish identically, yet $\operatorname{Pf}(J_m)=1$). Therefore $\operatorname{Pf}\notin R$: the Pfaffian is a genuinely new $SO(2m)$-invariant, adjoined to the $O(2m)$-invariants subject to the single relation $\operatorname{Pf}^2=\det$.
>
> All five clauses are established. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Symplectic linear algebra: invariance of the symplectic volume.** On a symplectic vector space $(\mathbb{R}^{2m},\omega)$ with form matrix $A$ (skew, nonsingular), a change of basis $B\in Sp(2m,\mathbb{R})$ preserves $\omega$, which in matrix terms is $B^tAB=A$. Clause (a) then reads $\operatorname{Pf}(A)=\det(B)\operatorname{Pf}(A)$, forcing $\det(B)=1$; this recovers the classical fact that symplectic matrices have determinant $+1$ directly from the Pfaffian, without the usual eigenvalue-pairing argument. The theorem applies because the symplectic condition is exactly a congruence relation, and it is non-obvious that the *sign* of the determinant is pinned by an antisymmetric invariant.

**Combinatorics: the FKT algorithm for planar perfect matchings.** For a graph on $2m$ vertices with a Pfaffian orientation, the number of perfect matchings equals $|\operatorname{Pf}(A)|$ for the signed skew adjacency matrix $A$, and clause (b) rewrites this as $\sqrt{\det A}$, which is computable in polynomial time. Here the theorem applies because the matching generating function is literally a Pfaffian; the non-obvious content is that clause (b) converts a quantity defined by an exponential sum over matchings into a single determinant evaluation, which is the entire speed-up.

**Riemannian geometry: the Gauss–Bonnet integrand of a surface.** For an oriented Riemannian surface the curvature in an oriented orthonormal frame is the $\mathfrak{so}(2)$-valued $2$-form $F=K\,dA\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ (up to the orientation sign), and clause (c) certifies that $\operatorname{Pf}(F/2\pi)=K\,dA/2\pi$ is a well-defined $2$-form representing the Euler class $e(TS)$. The theorem applies because $\operatorname{Pf}\in I(SO(2))$ is admissible Chern–Weil fuel; the non-obvious step is that the orientation-odd transformation law of clause (c) is exactly what makes the integrand change sign under orientation reversal, so that $\int e(TS)=\chi(S)$ is an oriented invariant.

---

# Bridges

- **The Euler class.** Feeding $\operatorname{Pf}$ into the [[Thm - Chern-Weil Theorem|Chern–Weil homomorphism]] on an $SO(2m)$-bundle uses clause (c) to guarantee admissibility and produces the [[Def - Euler Class of an Oriented Vector Bundle|Euler class]] $e(E)=[\operatorname{Pf}(F/2\pi)]$. The independence of the class from the connection is Chern–Weil; its orientation-odd behaviour is the sign in clause (c) transported to the level of forms: reversing the orientation of $E$ conjugates the curvature by an orientation-reversing orthogonal frame change, negating $\operatorname{Pf}(F)$ and hence $e(E)$.

- **The relation $e^2=p_m$.** Clause (b), read as the polynomial identity $\det=\operatorname{Pf}^2$ of clause (e), applied to the curvature $F$ of a metric connection and passed to de Rham classes, gives $e(E)^2=p_m(E)$, the identification of the square of the Euler class with the top [[Def - Pontryagin Classes|Pontryagin class]] of an oriented rank-$2m$ bundle. The Pontryagin page carries out the de Rham step; this page supplies the pointwise polynomial identity that makes it possible.

- **Vanishing on bundles with a section.** A nowhere-zero section reduces the structure group to $SO(2m-1)$; in $\mathfrak{so}(2m)$ this is the subalgebra of matrices whose last row and column vanish. Such a matrix is singular — it has a zero row, so its determinant is zero — and by clause (b), $\operatorname{Pf}^2=\det$, its Pfaffian vanishes; hence $e(E)=0$. This is the algebraic core of the statement that the Euler class obstructs nowhere-zero sections.

- **The Whitney sum formula for the Euler class.** For oriented bundles $E_1,E_2$ a metric connection on $E_1\oplus E_2$ can be taken block-diagonal, so its curvature is block-diagonal; clause (d) then gives $\operatorname{Pf}(F_1\oplus F_2)=\operatorname{Pf}(F_1)\operatorname{Pf}(F_2)$ pointwise, and taking classes yields $e(E_1\oplus E_2)=e(E_1)\smile e(E_2)$.

---

# Unlocked by This

> [!tip] Euler Class of an Oriented Vector Bundle *(from Gauge Theory VI)*
> Clause (c) certifies $\operatorname{Pf}\in I(SO(2m))$, which is exactly the admissibility needed to run [[Thm - Chern-Weil Theorem|Chern–Weil]] with the Pfaffian and define the [[Def - Euler Class of an Oriented Vector Bundle|Euler class]]. Clause (a)'s sign is what makes the class orientation-sensitive.

> [!tip] The Constraint $e^2=p_m$ *(from Gauge Theory VI)*
> Clause (b) is the pointwise identity behind $e(E)^2=p_m(E)$ on the [[Def - Pontryagin Classes|Pontryagin]] page; it forces the top Pontryagin class of an oriented bundle to be a perfect square in de Rham cohomology.

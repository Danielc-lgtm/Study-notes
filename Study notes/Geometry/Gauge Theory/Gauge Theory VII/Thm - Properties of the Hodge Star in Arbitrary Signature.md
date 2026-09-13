---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Hodge Star in Arbitrary Signature"
  - "Thm - Existence and Uniqueness of the Hodge Star"
  - "Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms"
  - "Thm - The Induced Inner Product and Volume Form are Well-Defined"
  - "Thm - Wedge Product Properties"
tags: [geometry, gauge-theory, hodge-star, linear-algebra]
---

# Notation

Throughout, $V$ is a real vector space of dimension $n$, equipped with a fixed orientation and a non-degenerate symmetric bilinear form $\langle\cdot,\cdot\rangle$ that need not be definite. Its **index** $p$ is the number of negative signs in its signature, that is, the number of $j$ with $\langle e_j,e_j\rangle=-1$ for a generalized orthonormal basis; by [[Thm - Sylvester's Law of Inertia|Sylvester's law of inertia]] this number does not depend on the basis. A **generalized orthonormal basis** $e_1,\dots,e_n$ of $V$ satisfies $\langle e_i,e_j\rangle=\epsilon_j\,\delta_{ij}$ with $\epsilon_j\in\{+1,-1\}$; we always take it **positively oriented**. Its dual basis in $V^*$ is $e_1^*,\dots,e_n^*$, defined by $e_i^*(e_j)=\delta_{ij}$.

We work in the exterior algebra $\Lambda^\bullet V^*$; the space of alternating $k$-forms is $\Lambda^kV^*$, with $\dim\Lambda^kV^*=\binom{n}{k}$, as set up in [[Def - Alternating Tensor and Lambda k V Dual|the definition of the exterior powers ΛᵏV*]]. For a strictly increasing multi-index $I=(i_1<\dots<i_k)$ of length $k$ we write
$$e_I^*:=e_{i_1}^*\wedge\dots\wedge e_{i_k}^*\in\Lambda^kV^*,\qquad \epsilon_I:=\epsilon_{i_1}\cdots\epsilon_{i_k}\in\{+1,-1\}.$$
The $\binom{n}{k}$ monomials $\{e_I^*\}_{|I|=k}$ form a basis of $\Lambda^kV^*$. Given such an $I$, its **complement** $I^c=(j_1<\dots<j_{n-k})$ is the increasing arrangement of $\{1,\dots,n\}\setminus\{i_1,\dots,i_k\}$; it is the unique increasing multi-index of length $n-k$ with $I\cap I^c=\varnothing$. The **concatenation permutation** $(IJ):=(i_1,\dots,i_k,j_1,\dots,j_{n-k})$, where $J=I^c$, is a rearrangement of $(1,\dots,n)$, and $\operatorname{sign}(IJ)\in\{+1,-1\}$ denotes the sign of the permutation $\sigma\in S_n$ defined by $\sigma(1)=i_1,\dots,\sigma(k)=i_k,\sigma(k+1)=j_1,\dots,\sigma(n)=j_{n-k}$.

The **induced inner product** on $\Lambda^kV^*$, still written $\langle\cdot,\cdot\rangle$, is the one from [[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms|the induced-inner-product definition]]; on monomials it satisfies $\langle e_I^*,e_{I'}^*\rangle=\delta_{II'}\,\epsilon_I$, and it is non-degenerate (both facts are proved on [[Thm - The Induced Inner Product and Volume Form are Well-Defined|the well-definedness theorem]]). The **volume form** is $\mathrm{vol}:=e_1^*\wedge\dots\wedge e_n^*\in\Lambda^nV^*$; it depends only on the orientation, spans the one-dimensional space $\Lambda^nV^*$, and satisfies $\langle\mathrm{vol},\mathrm{vol}\rangle=(-1)^p$.

The **Hodge star** is the linear map $\star:\Lambda^kV^*\to\Lambda^{n-k}V^*$ characterised by the defining relation
$$\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}\qquad\text{for all }\omega\in\Lambda^kV^*,\ \eta\in\Lambda^{n-k}V^*,$$
whose existence, uniqueness, and linearity are established on [[Thm - Existence and Uniqueness of the Hodge Star|the existence-and-uniqueness theorem]] and whose full definition (pointwise extension to a semi-Riemannian manifold, and the extension to vector-valued forms) is on [[Def - Hodge Star in Arbitrary Signature|the definition page]].

> [!warning] Convention: which Hodge star
> This series adopts **Bär's convention** $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$, in which the star of a $k$-form is defined against an $(n-k)$-form in the *second* slot of the wedge. The other common convention defines a star $\star_V$ by placing it in the second slot instead: $\alpha\wedge\star_V\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}$ for $\alpha,\beta\in\Lambda^kV^*$. This $\star_V$ is exactly the operator of the vault's Riemannian page [[Def - The Hodge Star Operator|the Hodge star operator]]. The two are related, on every degree, by
> $$\star=(-1)^p\,\star_V,$$
> a degree-*independent* scalar, as one reads off by comparing property (4) below with the defining relation of $\star_V$. In particular the two stars **coincide when $p=0$**, so [[Thm - Properties of the Hodge Star|the Riemannian properties-of-the-Hodge-star theorem]] is precisely the $p=0$ specialisation of the present theorem. Note that although $\star$ and $\star_V$ differ by $(-1)^p$, their *double* stars agree, since $(-1)^{2p}=1$; this is why the double-star formula below has the same sign $(-1)^{k(n-k)+p}$ as the Riemannian one with $s=p$. Finally, a third convention $\star'$, occasionally seen, satisfies $\star'=(-1)^{k(n-k)}\star_V$; the phrase "$(-1)^{k(n-k)}$" in the series conventions file refers to $\star'$ against $\star_V$, not to Bär against the vault.

---

# Statement

> **Theorem (Properties of the Hodge star in arbitrary signature).** Let $V$ be an oriented $n$-dimensional real vector space with a non-degenerate symmetric bilinear form of index $p$, let $e_1,\dots,e_n$ be a positively oriented generalized orthonormal basis with signs $\epsilon_j=\langle e_j,e_j\rangle$, and let $\star$ be the associated Hodge star. Then:
>
> 1. **(Star of a basis monomial.)** For an increasing multi-index $I=(i_1<\dots<i_k)$ with complement $J=I^c=(j_1<\dots<j_{n-k})$,
> $$\star\big(e_{i_1}^*\wedge\dots\wedge e_{i_k}^*\big)=\epsilon_{j_1}\cdots\epsilon_{j_{n-k}}\cdot\operatorname{sign}(IJ)\cdot e_{j_1}^*\wedge\dots\wedge e_{j_{n-k}}^*,$$
> that is, $\star e_I^*=\epsilon_J\,\operatorname{sign}(IJ)\,e_J^*$.
>
> 2. **(Double star.)** For every $\omega\in\Lambda^kV^*$,
> $$\star\star\,\omega=(-1)^{k(n-k)+p}\,\omega.$$
>
> 3. **(Isometry up to the sign of the index.)** For all $\omega,\eta\in\Lambda^kV^*$,
> $$\langle\star\omega,\star\eta\rangle=(-1)^p\,\langle\omega,\eta\rangle.$$
>
> 4. **(Symmetry of the star pairing.)** For all $\omega,\eta\in\Lambda^kV^*$,
> $$\omega\wedge\star\eta=\eta\wedge\star\omega=(-1)^p\,\langle\omega,\eta\rangle\,\mathrm{vol}.$$
>
> 5. **(Recovering the wedge from the inner product.)** For $\omega\in\Lambda^kV^*$ and $\eta\in\Lambda^{n-k}V^*$,
> $$\omega\wedge\eta=(-1)^{k(n-k)}\,\langle\omega,\star\eta\rangle\,\mathrm{vol}.$$

These are equations $(3.2)$–$(3.6)$ of Bär's *Gauge Theory* (Proposition 3.1.8). Bär proves parts (1) and (5) in full and leaves (2)–(4) as exercises; all five are proved below at full rigour, and (2)–(4) are drilled independently on the exercise pages [[Ex - Double Star Sign in Arbitrary Signature]], [[Ex - The Hodge Star is an Isometry up to the Sign of the Index]], and [[Ex - Symmetry of the Star Pairing]].

---

# Motivation

The Hodge star is introduced by a single abstract identity, $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$, which pins the operator down uniquely but tells us nothing about how to compute it or how it interacts with itself. Every later use of the star — writing Maxwell's equations as $d\star F+J=0$, forming the Yang–Mills density $\tfrac12F\wedge\star F$, splitting $2$-forms into self-dual and anti-self-dual parts, taking the adjoint of the exterior derivative — needs a working vocabulary: an explicit value on a basis, the effect of applying the star twice, and the behaviour of the star inside a wedge or an inner product. This theorem is that vocabulary. It is the computational backbone of the entire chapter, and of gauge theory generally.

The single most consequential entry is the **double-star formula** $\star\star=(-1)^{k(n-k)+p}$. Its sign decides the qualitative behaviour of the star in middle degree. In dimension four on $2$-forms it reads $\star\star=(-1)^{4+p}=(-1)^p$: in Euclidean signature ($p=0$) the star is an involution with eigenvalues $\pm1$, and $\Lambda^2$ splits orthogonally into its self-dual and anti-self-dual eigenspaces — the algebraic origin of instantons and of Donaldson theory; in Lorentzian signature ($p=1$) the star squares to $-1$, behaves like a complex structure with eigenvalues $\pm i$, and encodes the electromagnetic duality that rotates the electric field into the magnetic field. One formula, one sign, two entirely different geometries.

There is a second reason to collect these identities carefully rather than quote them. The indefinite case carries an extra sign $(-1)^p$ that is absent in the Riemannian theory taught first, and it appears in different places in different identities: it multiplies the inner product in the isometry law (3), it multiplies the volume form in the symmetry law (4), and it sits inside the exponent in the double-star law (2). A sign misplaced here silently corrupts every downstream computation — the sign of the Yang–Mills energy, the sign in the Lorentz force law, the reality of the electromagnetic Lagrangian. The point of proving all five together, from one basis computation, is to see exactly where each $(-1)^p$ comes from and why the three placements are consistent.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's stated hypothesis is bare — an oriented finite-dimensional real vector space with a non-degenerate symmetric bilinear form — so the useful question is: which problems secretly hand you such a space together with a Hodge star, even when none is named? Recognising these is what lets the algebraic theorem do geometric work.

The first disguised source is **a point of an oriented semi-Riemannian manifold**. If $(M,g)$ is an oriented pseudo-Riemannian $n$-manifold, then each tangent space $(T_xM,g_x)$ is exactly an oriented non-degenerate inner-product space of some fixed index $p$, so the theorem applies verbatim in each fibre $\Lambda^kT_x^*M$; because a local oriented orthonormal coframe exists by Gram–Schmidt on the metric, the fibrewise stars assemble into a smooth bundle map $\star:\Omega^k(M)\to\Omega^{n-k}(M)$ satisfying all five identities pointwise, hence as identities of differential forms. The bridge that is easy to miss is that "smooth manifold with an indefinite metric" is not a new setting for the star but the old linear-algebra setting repeated in every fibre. *Example problem:* on a Lorentzian $4$-manifold with signature $(-,+,+,+)$, deduce that $\star\star=-1$ on $2$-forms directly from part (2) with $n=4$, $k=2$, $p=1$, and conclude that the source-free Maxwell system $dF=0$, $d\star F=0$ is invariant under $F\mapsto\star F$.

The second disguised source is **a field strength valued in a Lie algebra with an invariant inner product**. In Yang–Mills theory the curvature $F$ is a $2$-form with values in a vector space $W=\mathfrak g$ carrying an $\operatorname{Ad}$-invariant inner product, and the star is extended to $W$-valued forms by $\star(\omega\otimes w):=(\star\omega)\otimes w$ with $\langle\omega\otimes w,\eta\otimes w'\rangle:=\langle\omega,\eta\rangle\langle w,w'\rangle$. Because this extension acts as the identity on the $W$-factor, every identity of the present theorem holds for $W$-valued forms with the inner product read as the combined one. The bridge is that tensoring with a fixed inner-product space changes nothing in the exterior-algebra factor where all the signs live. *Example problem:* show that the Yang–Mills density $\tfrac12\langle F\wedge\star F\rangle$ equals $\tfrac12(-1)^p\lvert F\rvert^2\,\mathrm{vol}$ by applying part (4) in each $W$-tensor slot.

The third disguised source is **any construction that produces an operator of the shape $\star A\star$**. Whenever an operator is built by conjugating something by the star — most importantly the codifferential $\delta=\pm\star d\star$, adjoint to the exterior derivative — the two stars flanking $A$ can be collapsed using part (2), turning an opaque triple product into a signed single operator. The bridge is the double-star formula: it is the only tool that removes a $\star\star$, and its degree-and-index-dependent sign is exactly what must be tracked. *Example problem:* using part (2) twice, determine the sign $c$ in $\star\star\alpha=c\,\alpha$ for $\alpha$ a $1$-form on a Lorentzian $4$-manifold, and hence the sign in the formula for the codifferential on $1$-forms.

**Targets (Output Amplification)**

The bare conclusion is a table of five algebraic identities. Combined with a little extra structure each becomes a workhorse.

Combine part (4) with **a quadratic first-order Lagrangian**. Taking $\omega=\eta=F$ in part (4) gives $F\wedge\star F=(-1)^p\lvert F\rvert^2\,\mathrm{vol}$, so on a Lorentzian manifold ($p=1$) the Maxwell density is $\tfrac12F\wedge\star F=-\tfrac12\lvert F\rvert^2\,\mathrm{vol}=\tfrac12(\lvert\vec E\rvert^2-\lvert\vec B\rvert^2)\,\mathrm{vol}$. The extra ingredient is the field strength as a curvature $2$-form; the payoff is that the action functional is manifestly a metric contraction of $F$ with itself, which is what makes its Euler–Lagrange equation $d\star F+J=0$ and its conformal weight computable. This is the exact route by which part (4) feeds [[Def - Electromagnetic Lagrangian and Action|the electromagnetic action]] and, in the non-abelian copy, the Yang–Mills functional of §7.4.

Combine part (2) with **middle degree in dimension four and Euclidean signature**. At $n=4$, $k=2$, $p=0$ part (2) gives $\star\star=+1$ on $\Lambda^2V^*$, so the star is an involution; part (3) with $p=0$ makes it an isometry, hence self-adjoint, so $\Lambda^2V^*$ splits orthogonally into the $\pm1$ eigenspaces $\Lambda^2_\pm$. The extra ingredient is the dimensional coincidence $k=n-k=2$ with $p$ even; the payoff is the self-dual/anti-self-dual decomposition on which the whole theory of instantons and [[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions|the four-dimensional self-dual decomposition]] rests. Reversing the orientation of $V$ negates the volume form, hence (by the defining relation) negates $\star$, and so interchanges $\Lambda^2_+$ and $\Lambda^2_-$.

Combine part (4) with **integration over a compact oriented manifold**. Integrating $\omega\wedge\star\eta=(-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$ over a closed oriented semi-Riemannian $M$ produces the global pairing $\int_M\omega\wedge\star\eta=(-1)^p\langle\omega,\eta\rangle_{L^2}$, where $\langle\cdot,\cdot\rangle_{L^2}$ is the $L^2$ inner product of forms. The extra ingredient is a measure to integrate against; the payoff is that $\star$ becomes (up to the sign $(-1)^p$) an $L^2$ isometry, and the pairing $(\omega,\eta)\mapsto\int_M\omega\wedge\star\eta$ is what makes the codifferential the formal adjoint of $d$ and drives every variational argument in the chapter, including the derivation of the field equations by moving $d$ off the test form with Stokes' theorem.

---

# Why Is It True

Strip away the five statements and there is only one mechanism. The Hodge star, on an orthonormal basis, does exactly one thing: it sends the monomial $e_I^*$ to a signed copy of its **complement** $e_{I^c}^*$. The sign it attaches is a product of two bookkeeping quantities — the shuffle sign $\operatorname{sign}(IJ)$ that measures how far the concatenation $(I,I^c)$ is from the standard order $(1,\dots,n)$, and the signature product $\epsilon_{I^c}$ over the complementary indices. Once part (1) is established, the other four are pure bookkeeping: applying the star twice re-complements $I^c$ back to $I$ and multiplies the two signs; pairing two stars lands on the same complement only when the originals agreed; wedging a form with a star lands in top degree, where the volume form converts everything to a number.

The two signs behave predictably under the operations. Complementation is an involution, $(I^c)^c=I$, so applying the star twice returns the original monomial times $\operatorname{sign}(IJ)\operatorname{sign}(JI)\,\epsilon_I\epsilon_{I^c}$. The first factor is the sign of swapping a block of length $k$ past a block of length $n-k$, namely $(-1)^{k(n-k)}$; the second is the product of all $n$ of the $\epsilon$'s, namely $(-1)^p$, because $I$ and $I^c$ together exhaust $\{1,\dots,n\}$. Their product is the double-star sign. The isometry law is the same accounting run on a pair: two stars can only be non-orthogonal on the same complement, forcing the originals equal, and then the leftover factor is again $\epsilon_{I^c}/\epsilon_I=(-1)^p$. The last two identities are not new computations at all — they are the defining relation read with a star already inserted, cleaned up by the two identities just proved.

**The one-sentence mechanism:** every one of the five identities is the single fact that $\star$ carries the basis monomial $e_I^*$ to $\epsilon_{I^c}\operatorname{sign}(IJ)\,e_{I^c}^*$, together with the two elementary sign facts $\epsilon_I\epsilon_{I^c}=(-1)^p$ (the signature product over a complementary pair) and $\operatorname{sign}(IJ)\operatorname{sign}(JI)=(-1)^{k(n-k)}$ (the block-transposition sign).

---

# What Makes This Hard

Nothing here is conceptually deep; the entire difficulty is disciplined sign tracking in the indefinite case, where three distinct signs interleave — the orientation shuffle $\operatorname{sign}(IJ)$, the signature product $\epsilon_I$, and the block-swap sign $(-1)^{k(n-k)}$ — and each identity places the surviving $(-1)^p$ in a different position (inside the exponent for double star, multiplying the inner product for the isometry, multiplying the volume form for the symmetry). The most common error is to import the Riemannian formulas, where $p=0$ makes every $\epsilon_j$ equal to $+1$ and the signature product silently disappears, and then to forget the $\epsilon_{I^c}$ factor when a time index is present: in Lorentzian signature the star of $dt\wedge dx$ carries the sign of the timelike direction, which is exactly what flips $\star\star$ from $+1$ to $-1$ on $2$-forms and turns the self-dual splitting into a complex structure. The second trap is to assume, from the Riemannian habit, that $\star$ is an isometry; part (3) says it is an isometry only up to $(-1)^p$, so in Lorentzian signature it is an *anti*-isometry on forms of odd index contribution, and treating it as norm-preserving falsifies the sign of the Yang–Mills energy.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove part (1), the value of $\star$ on a basis monomial, from the defining relation and the orthonormality of the monomial inner product. Then obtain parts (2) and (3) by running part (1) once or twice on basis monomials and simplifying with two elementary sign identities. Finally read parts (4) and (5) off the defining relation with a star already inserted, using parts (2) and (3) to clean up. Everything reduces to the value on a basis and two sign facts; there is no analysis and no limit.

**Subgoal decomposition:**

1. **Complementary wedge (auxiliary).** Show $e_I^*\wedge e_K^*=0$ unless $K=I^c$, and $e_I^*\wedge e_{I^c}^*=\operatorname{sign}(IJ)\,\mathrm{vol}$.
   - *Hint:* A wedge with a repeated dual vector vanishes; reorder the surviving product into $e_1^*\wedge\dots\wedge e_n^*$ and read off the permutation sign.
   - *Why needed:* It is the bridge between the wedge in the defining relation and the volume form, used to pin down the coefficient in part (1).

2. **Two sign identities (auxiliary).** Show $\epsilon_I\epsilon_{I^c}=(-1)^p$ and $\operatorname{sign}(IJ)\operatorname{sign}(JI)=(-1)^{k(n-k)}$.
   - *Hint:* The first is the product of all $n$ signs; the second follows from graded commutativity of the wedge applied to $e_I^*\wedge e_{I^c}^*$ versus $e_{I^c}^*\wedge e_I^*$.
   - *Why needed:* These are the only two facts that convert the raw output of part (1) into the clean signs of parts (2) and (3).

3. **Part (1): star of a monomial.** Show $\star e_I^*=\epsilon_{I^c}\operatorname{sign}(IJ)\,e_{I^c}^*$.
   - *Hint:* Expand $\star e_I^*$ in the monomial basis; test the defining relation against each $e_K^*$; only $K=I^c$ survives, and its coefficient is fixed by subgoal 1.
   - *Why needed:* It is the concrete formula from which the remaining parts are pure algebra.

4. **Part (2): double star.** Show $\star\star\omega=(-1)^{k(n-k)+p}\omega$.
   - *Hint:* Apply part (1) twice on $e_I^*$; the complement of $I^c$ is $I$; simplify with the two sign identities of subgoal 2; extend by linearity.
   - *Why needed:* The most-used identity downstream, and the input to part (5).

5. **Part (3): isometry up to sign.** Show $\langle\star\omega,\star\eta\rangle=(-1)^p\langle\omega,\eta\rangle$.
   - *Hint:* On monomials $e_I^*,e_{I'}^*$, both sides vanish unless $I=I'$; when $I=I'$ compare $\epsilon_{I^c}$ with $(-1)^p\epsilon_I$; extend by bilinearity.
   - *Why needed:* Converts the defining relation into part (4).

6. **Part (4): symmetry of the star pairing.** Show $\omega\wedge\star\eta=\eta\wedge\star\omega=(-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$.
   - *Hint:* Put $\star\eta$ in the second slot of the defining relation, then apply part (3); use symmetry of $\langle\cdot,\cdot\rangle$ for the second equality.
   - *Why needed:* The identity that makes $\star$ an $L^2$ isometry up to sign and drives every variation.

7. **Part (5): recovering the wedge.** Show $\omega\wedge\eta=(-1)^{k(n-k)}\langle\omega,\star\eta\rangle\,\mathrm{vol}$ for mixed degrees.
   - *Hint:* Chain the defining relation, part (3) applied to the $(n-k)$-forms $\star\omega$ and $\eta$, and part (2).
   - *Why needed:* Expresses the wedge pairing through the inner product with the correct mixed-degree sign, closing the circle of identities.

---

# Lemma Decomposition

> [!note]- Lemma 1: Complementary wedge identity
> **Statement:** Let $I=(i_1<\dots<i_k)$ be an increasing multi-index and $K$ an increasing multi-index of length $n-k$. If $K\neq I^c$ then $e_I^*\wedge e_K^*=0$. If $K=I^c=:J=(j_1<\dots<j_{n-k})$ then
> $$e_I^*\wedge e_J^*=\operatorname{sign}(IJ)\,\mathrm{vol},$$
> where $\operatorname{sign}(IJ)$ is the sign of the permutation $\sigma\in S_n$ listing $(i_1,\dots,i_k,j_1,\dots,j_{n-k})$.
>
> **Hint:** A wedge with a repeated dual vector is zero; if the two index sets are disjoint, reorder the product into standard increasing order and record the permutation sign.
>
> **Why needed:** It is the only bridge from the wedge $\omega\wedge\eta$ appearing in the defining relation to the volume form $\mathrm{vol}$, and it supplies the coefficient in part (1).
>
> > [!note]- Full proof
> > **Case $K\neq I^c$.** Both $I$ and $K$ are increasing of lengths $k$ and $n-k$, so $\lvert I\rvert+\lvert K\rvert=n$. The unique increasing multi-index of length $n-k$ disjoint from $I$ is $I^c$; hence $K\neq I^c$ forces $I\cap K\neq\varnothing$, so some index $m$ appears in both $I$ and $K$. Then the product $e_I^*\wedge e_K^*$ contains the factor $e_m^*$ twice. By the graded-commutativity part of [[Thm - Wedge Product Properties|the wedge product properties]] — for one-forms $\alpha,\beta$ one has $\alpha\wedge\beta=-\beta\wedge\alpha$, so $e_m^*\wedge e_m^*=-e_m^*\wedge e_m^*$ and therefore $e_m^*\wedge e_m^*=0$ — any wedge with a repeated one-form factor vanishes. Hence $e_I^*\wedge e_K^*=0$.
> >
> > **Case $K=I^c=J$.** Here $I\cup J=\{1,\dots,n\}$ with $I\cap J=\varnothing$, so the concatenated list $(i_1,\dots,i_k,j_1,\dots,j_{n-k})$ is a rearrangement of $(1,\dots,n)$; let $\sigma\in S_n$ be the permutation with $\sigma(1)=i_1,\dots,\sigma(k)=i_k,\sigma(k+1)=j_1,\dots,\sigma(n)=j_{n-k}$. Then
> > $$e_I^*\wedge e_J^*=e_{\sigma(1)}^*\wedge\dots\wedge e_{\sigma(n)}^*=\operatorname{sgn}(\sigma)\,e_1^*\wedge\dots\wedge e_n^*=\operatorname{sign}(IJ)\,\mathrm{vol},$$
> > where the middle equality is the permutation law $e_{\sigma(1)}^*\wedge\dots\wedge e_{\sigma(n)}^*=\operatorname{sgn}(\sigma)\,e_1^*\wedge\dots\wedge e_n^*$ (again from [[Thm - Wedge Product Properties|the wedge product properties]], since a transposition of adjacent factors introduces one minus sign and $\operatorname{sgn}$ counts transpositions), and the last equality is the definitions $\operatorname{sign}(IJ):=\operatorname{sgn}(\sigma)$ and $\mathrm{vol}:=e_1^*\wedge\dots\wedge e_n^*$.

> [!note]- Lemma 2: Two sign identities
> **Statement:** For every increasing multi-index $I$ of length $k$ with complement $J=I^c$ of length $n-k$,
> $$\epsilon_I\,\epsilon_J=(-1)^p\qquad\text{and}\qquad \operatorname{sign}(IJ)\,\operatorname{sign}(JI)=(-1)^{k(n-k)}.$$
>
> **Hint:** The first is the product of all $n$ of the numbers $\epsilon_1,\dots,\epsilon_n$; the second follows from graded commutativity applied to $e_I^*\wedge e_J^*$ versus $e_J^*\wedge e_I^*$.
>
> **Why needed:** These are precisely the two simplifications that turn the raw double product of part (1) into the clean signs $(-1)^p$ and $(-1)^{k(n-k)}$ of parts (2)–(5).
>
> > [!note]- Full proof
> > **First identity.** Since $I$ and $J=I^c$ are disjoint and together exhaust $\{1,\dots,n\}$,
> > $$\epsilon_I\,\epsilon_J=\Big(\prod_{i\in I}\epsilon_i\Big)\Big(\prod_{j\in J}\epsilon_j\Big)=\prod_{m=1}^{n}\epsilon_m.$$
> > In this product each factor is $\pm1$, and by definition of the index there are exactly $p$ factors equal to $-1$ (the negative directions) and $n-p$ factors equal to $+1$. Hence $\prod_{m=1}^{n}\epsilon_m=(-1)^p$, so $\epsilon_I\epsilon_J=(-1)^p$.
> >
> > **Second identity.** Apply the graded-commutativity law of [[Thm - Wedge Product Properties|the wedge product]] to the $k$-form $e_I^*$ and the $(n-k)$-form $e_J^*$: interchanging a $k$-form and an $(n-k)$-form introduces the sign $(-1)^{k(n-k)}$, so
> > $$e_J^*\wedge e_I^*=(-1)^{k(n-k)}\,e_I^*\wedge e_J^*.$$
> > By Lemma 1 (with the roles of the two complementary index sets exchanged, using $(I^c)^c=I$), $e_J^*\wedge e_I^*=\operatorname{sign}(JI)\,\mathrm{vol}$ and $e_I^*\wedge e_J^*=\operatorname{sign}(IJ)\,\mathrm{vol}$. Substituting,
> > $$\operatorname{sign}(JI)\,\mathrm{vol}=(-1)^{k(n-k)}\operatorname{sign}(IJ)\,\mathrm{vol},$$
> > and since $\mathrm{vol}\neq0$ spans the one-dimensional space $\Lambda^nV^*$ we may cancel it: $\operatorname{sign}(JI)=(-1)^{k(n-k)}\operatorname{sign}(IJ)$. Multiplying both sides by $\operatorname{sign}(IJ)$ and using $\operatorname{sign}(IJ)^2=1$ gives $\operatorname{sign}(IJ)\operatorname{sign}(JI)=(-1)^{k(n-k)}$.

> [!note]- Lemma 3: The star of a basis monomial (part (1))
> **Statement:** For an increasing multi-index $I=(i_1<\dots<i_k)$ with complement $J=I^c=(j_1<\dots<j_{n-k})$,
> $$\star e_I^*=\epsilon_J\,\operatorname{sign}(IJ)\,e_J^*=\epsilon_{j_1}\cdots\epsilon_{j_{n-k}}\,\operatorname{sign}(IJ)\,e_{j_1}^*\wedge\dots\wedge e_{j_{n-k}}^*.$$
>
> **Hint:** Expand $\star e_I^*$ in the basis $\{e_K^*\}_{|K|=n-k}$; test the defining relation against each $e_K^*$ and use Lemma 1 to kill every term but $K=I^c$; then evaluate the surviving coefficient.
>
> **Why needed:** This is the explicit value of the star, part (1) of the theorem, and the concrete input to every remaining part.
>
> > [!note]- Full proof
> > Since $\{e_K^*\}_{|K|=n-k}$ is a basis of $\Lambda^{n-k}V^*$, write
> > $$\star e_I^*=\sum_{\lvert K\rvert=n-k}c_K\,e_K^*\qquad(c_K\in\mathbb R).$$
> > **Step A — only the complementary coefficient survives.** Fix any increasing $K$ of length $n-k$ with $K\neq I^c$. The defining relation of the Hodge star, $e_I^*\wedge\eta=\langle\star e_I^*,\eta\rangle\,\mathrm{vol}$, evaluated at $\eta=e_K^*$ gives
> > $$e_I^*\wedge e_K^*=\langle\star e_I^*,e_K^*\rangle\,\mathrm{vol}.$$
> > The left side is $0$ by Lemma 1 (case $K\neq I^c$). On the right,
> > $$\langle\star e_I^*,e_K^*\rangle=\Big\langle\sum_{L}c_L\,e_L^*,\,e_K^*\Big\rangle=\sum_L c_L\,\langle e_L^*,e_K^*\rangle=c_K\,\epsilon_K,$$
> > using the monomial orthonormality $\langle e_L^*,e_K^*\rangle=\delta_{LK}\,\epsilon_K$ from [[Thm - The Induced Inner Product and Volume Form are Well-Defined|the well-definedness theorem]]. Thus $0=c_K\,\epsilon_K\,\mathrm{vol}$; since $\epsilon_K=\pm1\neq0$ and $\mathrm{vol}\neq0$, we get $c_K=0$. Therefore every coefficient with $K\neq I^c$ vanishes, and $\star e_I^*=c\,e_J^*$ with $c:=c_{I^c}$ and $J=I^c$.
> >
> > **Step B — evaluate the surviving coefficient.** Now evaluate the defining relation at $\eta=e_J^*$:
> > $$e_I^*\wedge e_J^*=\langle\star e_I^*,e_J^*\rangle\,\mathrm{vol}=\langle c\,e_J^*,e_J^*\rangle\,\mathrm{vol}=c\,\epsilon_J\,\mathrm{vol},$$
> > again by monomial orthonormality $\langle e_J^*,e_J^*\rangle=\epsilon_J$. But the left side is $e_I^*\wedge e_J^*=\operatorname{sign}(IJ)\,\mathrm{vol}$ by Lemma 1 (case $K=I^c$). Equating the two expressions and cancelling the nonzero $\mathrm{vol}$,
> > $$\operatorname{sign}(IJ)=c\,\epsilon_J\quad\Longrightarrow\quad c=\operatorname{sign}(IJ)\,\epsilon_J^{-1}=\operatorname{sign}(IJ)\,\epsilon_J,$$
> > where the last step uses $\epsilon_J^{-1}=\epsilon_J$ because $\epsilon_J=\pm1$. Hence $\star e_I^*=\epsilon_J\,\operatorname{sign}(IJ)\,e_J^*$, which is the claimed formula.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$, the positively oriented generalized orthonormal basis $e_1,\dots,e_n$, the signs $\epsilon_j$, the index $p$, and the star $\star$ be as in the Notation. We prove the five parts in the order (1), (2), (3), (4), (5); each later part uses only the defining relation and the parts already proved. Throughout, "monomial orthonormality" means $\langle e_I^*,e_{I'}^*\rangle=\delta_{II'}\,\epsilon_I$ and "the volume pairing" means $\langle\mathrm{vol},\mathrm{vol}\rangle=(-1)^p$, both from [[Thm - The Induced Inner Product and Volume Form are Well-Defined|the well-definedness theorem]].
>
> **Step 0 — preconditions.** The star exists, is unique, and is linear on each $\Lambda^kV^*$ by [[Thm - Existence and Uniqueness of the Hodge Star|the existence-and-uniqueness theorem]], so the symbol $\star\omega$ is well-defined and it suffices, for the linear identities (2) and (3), to verify them on the basis monomials $e_I^*$ and extend by (bi)linearity. The complement map $I\mapsto I^c$ is an involution on increasing multi-indices, $(I^c)^c=I$, which we use in Step 2.
>
> **Step 1 — Part (1).** This is Lemma 3: for $I$ increasing of length $k$ with complement $J=I^c$,
> $$\star e_I^*=\epsilon_J\,\operatorname{sign}(IJ)\,e_J^*. \tag{1}$$
>
> **Step 2 — Part (2), the double-star formula.** Fix an increasing multi-index $I$ of length $k$, with complement $J=I^c$ of length $n-k$. Applying $(1)$,
> $$\star e_I^*=\epsilon_J\,\operatorname{sign}(IJ)\,e_J^*.$$
> Now $e_J^*$ is itself a basis monomial of degree $n-k$, and the complement of $J$ is $(I^c)^c=I$ (Step 0), so applying $(1)$ a second time — with $J$ in the role of the first index set and $I$ in the role of its complement — gives
> $$\star e_J^*=\epsilon_I\,\operatorname{sign}(JI)\,e_I^*.$$
> Composing the two, and using linearity of $\star$ to pull the scalar $\epsilon_J\operatorname{sign}(IJ)$ through,
> $$\star\star e_I^*=\epsilon_J\,\operatorname{sign}(IJ)\,\star e_J^*=\epsilon_J\,\operatorname{sign}(IJ)\cdot\epsilon_I\,\operatorname{sign}(JI)\,e_I^*=\big(\epsilon_I\epsilon_J\big)\big(\operatorname{sign}(IJ)\operatorname{sign}(JI)\big)\,e_I^*.$$
> By Lemma 2, $\epsilon_I\epsilon_J=(-1)^p$ and $\operatorname{sign}(IJ)\operatorname{sign}(JI)=(-1)^{k(n-k)}$, so
> $$\star\star e_I^*=(-1)^p\,(-1)^{k(n-k)}\,e_I^*=(-1)^{k(n-k)+p}\,e_I^*.$$
> Since the monomials $\{e_I^*\}_{|I|=k}$ span $\Lambda^kV^*$ and $\star\star$ is linear (Step 0), $\star\star\omega=(-1)^{k(n-k)+p}\omega$ for every $\omega\in\Lambda^kV^*$. This is part (2).
>
> **Step 3 — Part (3), the isometry law.** By bilinearity of $\langle\cdot,\cdot\rangle$ it suffices to prove $\langle\star e_I^*,\star e_{I'}^*\rangle=(-1)^p\langle e_I^*,e_{I'}^*\rangle$ for all increasing $I,I'$ of length $k$; write $J=I^c$, $J'=I'^c$. By $(1)$,
> $$\langle\star e_I^*,\star e_{I'}^*\rangle=\big\langle\epsilon_J\operatorname{sign}(IJ)e_J^*,\ \epsilon_{J'}\operatorname{sign}(I'J')e_{J'}^*\big\rangle=\epsilon_J\epsilon_{J'}\,\operatorname{sign}(IJ)\operatorname{sign}(I'J')\,\langle e_J^*,e_{J'}^*\rangle,$$
> and by monomial orthonormality $\langle e_J^*,e_{J'}^*\rangle=\delta_{JJ'}\,\epsilon_J$.
>
> *Case $I\neq I'$.* Complementation is injective, so $I\neq I'$ gives $J\neq J'$, hence $\delta_{JJ'}=0$ and the left side is $0$. On the right side of the claim, $\langle e_I^*,e_{I'}^*\rangle=\delta_{II'}\epsilon_I=0$, so $(-1)^p\langle e_I^*,e_{I'}^*\rangle=0$ as well. The two sides agree.
>
> *Case $I=I'$.* Then $J=J'$, and $\operatorname{sign}(IJ)=\operatorname{sign}(I'J')$, so $\operatorname{sign}(IJ)\operatorname{sign}(I'J')=\operatorname{sign}(IJ)^2=1$; likewise $\epsilon_J\epsilon_{J'}=\epsilon_J^2=1$; and $\langle e_J^*,e_{J}^*\rangle=\epsilon_J$. Hence the left side equals $\epsilon_J$. For the right side, $\langle e_I^*,e_I^*\rangle=\epsilon_I$, so $(-1)^p\langle e_I^*,e_I^*\rangle=(-1)^p\epsilon_I$; and by Lemma 2, $\epsilon_I\epsilon_J=(-1)^p$, that is $\epsilon_J=(-1)^p\epsilon_I^{-1}=(-1)^p\epsilon_I$. Therefore the left side $\epsilon_J$ equals $(-1)^p\epsilon_I$, the right side. The two sides agree.
>
> In both cases $\langle\star e_I^*,\star e_{I'}^*\rangle=(-1)^p\langle e_I^*,e_{I'}^*\rangle$; extending by bilinearity gives part (3).
>
> **Step 4 — Part (4), symmetry of the star pairing.** Let $\omega,\eta\in\Lambda^kV^*$. Then $\star\eta\in\Lambda^{n-k}V^*$, so it is a legitimate second slot in the defining relation of the star. Applying that relation with $\eta$ replaced by $\star\eta$ in the free slot,
> $$\omega\wedge\star\eta=\langle\star\omega,\star\eta\rangle\,\mathrm{vol}\qquad\text{(defining relation of }\star\text{, with }\star\eta\in\Lambda^{n-k}V^*\text{ in the second slot).}$$
> By part (3), $\langle\star\omega,\star\eta\rangle=(-1)^p\langle\omega,\eta\rangle$, hence
> $$\omega\wedge\star\eta=(-1)^p\,\langle\omega,\eta\rangle\,\mathrm{vol}. \tag{4a}$$
> Interchanging the roles of $\omega$ and $\eta$ (both are arbitrary elements of $\Lambda^kV^*$) in $(4\text{a})$ gives $\eta\wedge\star\omega=(-1)^p\langle\eta,\omega\rangle\,\mathrm{vol}$. Since the bilinear form is symmetric, $\langle\eta,\omega\rangle=\langle\omega,\eta\rangle$, so
> $$\eta\wedge\star\omega=(-1)^p\,\langle\omega,\eta\rangle\,\mathrm{vol}. \tag{4b}$$
> Comparing $(4\text{a})$ and $(4\text{b})$, both equal $(-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$, so $\omega\wedge\star\eta=\eta\wedge\star\omega=(-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$. This is part (4).
>
> **Step 5 — Part (5), recovering the wedge.** Let $\omega\in\Lambda^kV^*$ and $\eta\in\Lambda^{n-k}V^*$. Starting from the defining relation and inserting the identities already proved,
> $$\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}\qquad\text{(defining relation of }\star\text{).}$$
> The two forms $\star\omega$ and $\eta$ both lie in $\Lambda^{n-k}V^*$, so part (3) applies to them: with $u=\star\omega$ and $v=\eta$, part (3) reads $\langle\star u,\star v\rangle=(-1)^p\langle u,v\rangle$, i.e. $\langle\star\star\omega,\star\eta\rangle=(-1)^p\langle\star\omega,\eta\rangle$; multiplying by $(-1)^p$ and using $(-1)^{2p}=1$,
> $$\langle\star\omega,\eta\rangle=(-1)^p\,\langle\star\star\omega,\star\eta\rangle\qquad\text{(part (3) applied to the }(n-k)\text{-forms }\star\omega,\eta\text{).}$$
> Next, by part (2) applied to $\omega\in\Lambda^kV^*$, $\star\star\omega=(-1)^{k(n-k)+p}\omega$, so by bilinearity of $\langle\cdot,\cdot\rangle$,
> $$\langle\star\star\omega,\star\eta\rangle=(-1)^{k(n-k)+p}\,\langle\omega,\star\eta\rangle\qquad\text{(part (2)).}$$
> Combining the last three displayed equalities,
> $$\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}=(-1)^p(-1)^{k(n-k)+p}\,\langle\omega,\star\eta\rangle\,\mathrm{vol}=(-1)^{k(n-k)+2p}\,\langle\omega,\star\eta\rangle\,\mathrm{vol}=(-1)^{k(n-k)}\,\langle\omega,\star\eta\rangle\,\mathrm{vol},$$
> since $(-1)^{2p}=1$. This is part (5).
>
> All five parts are established. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Electromagnetic duality on Minkowski space (mathematical physics).** Take $V=\mathbb R^{1,3}$ with the Lorentzian form of index $p=1$ and orientation $\mathrm{vol}=e_0^*\wedge e_1^*\wedge e_2^*\wedge e_3^*$, and compute $\star$ on the six basis $2$-forms directly from part (1); the result is exactly Bär's star table, for instance $\star(e_0^*\wedge e_1^*)=e_2^*\wedge e_3^*$ and $\star(e_2^*\wedge e_3^*)=-e_0^*\wedge e_1^*$. The theorem applies because $(T_x\mathbb R^{1,3},g_x)$ is an oriented non-degenerate inner-product space of index $1$; what is non-obvious is that part (2) then forces $\star\star=-1$ on $2$-forms, so the vacuum Maxwell system $dF=0$, $d\star F=0$ is invariant under $F\mapsto\star F$ only up to the sign captured by $\star\star=-1$, and this is the precise algebraic content of electric–magnetic duality.

**Self-dual $2$-forms on a Riemannian $4$-manifold (gauge theory).** On an oriented Riemannian $4$-manifold ($p=0$), part (2) gives $\star\star=+1$ on $2$-forms and part (3) makes $\star$ an isometry, so $\Lambda^2T_x^*M$ splits orthogonally into $\pm1$ eigenspaces. The theorem applies fibrewise; the non-obvious point is that this splitting is defined pointwise from the metric and orientation alone, is preserved by no operator other than an oriented isometry, and yet is the entire home of the anti-self-dual instanton equation $\star F=-F$. Verify from part (4) that $\omega\wedge\omega=\pm\lvert\omega\rvert^2\,\mathrm{vol}$ for $\omega$ self-dual or anti-self-dual, the sign fact underlying the topological energy bound.

**The codifferential and the Laplacian on a compact manifold (global analysis).** On a closed oriented semi-Riemannian $n$-manifold, use part (4) integrated over $M$ to show that the operator $\delta:=\pm\star d\star$ (with the sign read off from part (2) in the relevant degree) is the formal adjoint of $d$ with respect to the $L^2$ pairing $\int_M\omega\wedge\star\eta$. The theorem applies because the pointwise identities integrate; the non-obvious step is that the two stars in $\star d\star$ collapse by part (2) into a single degree-dependent sign, which is what makes $\delta$ a first-order operator of the correct degree and $\Delta=d\delta+\delta d$ self-adjoint.

---

# Bridges

- **[[Thm - Properties of the Hodge Star|The Riemannian properties of the Hodge star]]** — the $p=0$ specialisation of the present theorem in the vault's convention. There the star is $\star_V$ with $\alpha\wedge\star_V\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}$, and at $p=0$ we have $\star=\star_V$, so parts (2)–(4) here read as $\star\star=(-1)^{k(n-k)}$, $\langle\star\omega,\star\eta\rangle=\langle\omega,\eta\rangle$, and $\omega\wedge\star\eta=\langle\omega,\eta\rangle\,\mathrm{vol}$ — exactly the Riemannian identities. The one structural difference is the index sign $(-1)^p$, which the Riemannian page never sees because it works only with definite metrics; the construction that carries the definite formulas to the indefinite ones is the change of the single overall sign $\star=(-1)^p\star_V$ together with the appearance of $\epsilon_{I^c}$ in the monomial formula.

- **[[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions|The self-dual decomposition in four dimensions]]** — built directly on part (2) at $n=4$, $k=2$, $p=0$, where $\star\star=+1$ makes $\star$ an involution and part (3) makes it an isometry, so $\Lambda^2V^*=\Lambda^2_+V^*\oplus\Lambda^2_-V^*$ orthogonally. The construction takes the involution $\star$, forms the projectors $\tfrac12(\mathrm{id}\pm\star)$, and reads their images as the self-dual and anti-self-dual subspaces; part (4) then supplies the sign identities $\omega_\pm\wedge\omega_\pm=\pm\lvert\omega_\pm\rvert^2\,\mathrm{vol}$ and $\omega_+\wedge\omega_-=0$ that make the decomposition orthogonal for the wedge pairing as well.

- **[[Def - Electromagnetic Lagrangian and Action|The electromagnetic action]]** — the Yang–Mills-type density $\tfrac12F\wedge\star F$ becomes a metric contraction through part (4): with $\omega=\eta=F$ one gets $F\wedge\star F=(-1)^p\lvert F\rvert^2\,\mathrm{vol}$, so on a Lorentzian manifold the Lagrangian is $-\tfrac12\lvert F\rvert^2\,\mathrm{vol}=\tfrac12(\lvert\vec E\rvert^2-\lvert\vec B\rvert^2)\,\mathrm{vol}$. The construction is to recognise the wedge of a form with its own star as, up to the index sign, the squared norm times the volume form; this is what lets the action be varied and its Euler–Lagrange equation $d\star F+J=0$ derived.

- **[[Def - Hodge Star in Arbitrary Signature|The definition of the Hodge star]] and its vector-valued extension** — the extension $\star(\omega\otimes w):=(\star\omega)\otimes w$ carries every identity of this theorem to $W$-valued forms, because the star acts as the identity on the $W$-factor and the combined inner product $\langle\omega\otimes w,\eta\otimes w'\rangle=\langle\omega,\eta\rangle\langle w,w'\rangle$ factors through the exterior-algebra inner product. The construction is to apply the scalar-valued theorem in the $\Lambda^\bullet V^*$ factor of a decomposable tensor $\omega\otimes w$ and extend by linearity; this is the mechanism by which the present identities become available for the $\mathfrak g$-valued curvature of a Yang–Mills field in §7.4.

---

# Unlocked by This

> [!tip] The codifferential in arbitrary signature *(from Hodge theory)*
> With the double-star sign of part (2) in hand, the codifferential $\delta=\pm\star d\star$ can be defined and its degree-and-index-dependent sign computed in Lorentzian as well as Riemannian signature, so that $\Delta=d\delta+\delta d$ is the wave operator on a Lorentzian manifold and the Laplacian on a Riemannian one. See **Def - The Codifferential** for the Riemannian case.

> [!tip] Instantons and the topological energy bound *(from gauge theory)*
> Part (2) at $n=4$, $p=0$ gives $\star\star=+1$ on $2$-forms, so the curvature of a connection on a bundle over a Riemannian $4$-manifold splits as $F=F_++F_-$ into self-dual and anti-self-dual parts; part (4) then yields $\lvert F\rvert^2\,\mathrm{vol}=F\wedge\star F$ and the identity $\int_M F\wedge F=\int_M(\lvert F_+\rvert^2-\lvert F_-\rvert^2)\,\mathrm{vol}$, whose right-hand side bounds the Yang–Mills energy below by the topological number $\int_M F\wedge F$, with equality exactly for (anti-)self-dual connections.

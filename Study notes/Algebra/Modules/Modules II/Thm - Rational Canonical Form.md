---
type: theorem
subject: module-theory
prereqs:
  - "Def - The Module of a Linear Operator"
  - "Def - Polynomial Ring"
  - "Def - Euclidean Domain"
  - "Def - Module"
  - "Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain"
  - "Def - Free Module"
tags: [algebra, module-theory]
---

# Notation

Throughout, $F$ is a field, $V$ a finite-dimensional vector space over $F$, and $\alpha : V \to V$ a linear endomorphism. The [[Def - Polynomial Ring|polynomial ring]] $F[X]$ is a [[Def - Euclidean Domain|Euclidean domain]] (the Euclidean function is $\deg$). The $F[X]$-module $V_\alpha$ is $V$ with $X$ acting as $\alpha$, so $f(X) \cdot v = f(\alpha)(v)$ — see [[Def - The Module of a Linear Operator]]. For a monic polynomial $f$, the symbol $C(f)$ is its **companion matrix**, the matrix of multiplication-by-$X$ on $F[X]/(f)$ in the basis $1, X, \dots, X^{\deg f - 1}$; explicitly, for $f = a_0 + a_1 X + \cdots + a_{r-1}X^{r-1} + X^r$,
$$
C(f) =
\begin{pmatrix}
0 & 0 & \cdots & 0 & -a_0 \\
1 & 0 & \cdots & 0 & -a_1 \\
0 & 1 & \cdots & 0 & -a_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & -a_{r-1}
\end{pmatrix}.
$$
The notation $f \mid g$ means $f$ divides $g$ in $F[X]$. The relation $\cong$ is $F[X]$-module isomorphism. The full registry is on the parent page [[Modules II — §3.3–3.4]].

---

# Statement

> **Rational Canonical Form.** Let $\alpha : V \to V$ be a linear endomorphism of a finite-dimensional vector space $V$ over a field $F$, and let $V_\alpha$ be the associated $F[X]$-module. Then
> $$V_\alpha \;\cong\; \frac{F[X]}{(f_1)} \,\oplus\, \frac{F[X]}{(f_2)} \,\oplus\, \cdots \,\oplus\, \frac{F[X]}{(f_s)}$$
> as $F[X]$-modules, for monic polynomials $f_1, f_2, \dots, f_s$ of degree $\geq 1$ satisfying the **divisibility chain**
> $$f_1 \mid f_2 \mid \cdots \mid f_s.$$
> Consequently there is a basis of $V$ in which the matrix of $\alpha$ is **block-diagonal with companion-matrix blocks**:
> $$
> \begin{pmatrix}
> C(f_1) & 0 & \cdots & 0 \\
> 0 & C(f_2) & \cdots & 0 \\
> \vdots & \vdots & \ddots & \vdots \\
> 0 & 0 & \cdots & C(f_s)
> \end{pmatrix}.
> $$
> The polynomials $f_1, \dots, f_s$ — the **invariant factors** of $\alpha$ — are uniquely determined by $\alpha$. The **minimal polynomial** of $\alpha$ is $f_s$, the largest invariant factor; the **characteristic polynomial** of $\alpha$ is the product $f_1 f_2 \cdots f_s$.
>
> Equivalently, in matrix language: every matrix $A \in M_{n}(F)$ is **conjugate** to a matrix in the block-diagonal companion form above, and the form is **canonical** — uniquely determined by the conjugacy class of $A$.

---

# Motivation

The basic problem of linear algebra, once you can add and compose operators, is *classification*: given a linear operator $\alpha$ on a finite-dimensional space, what does it look like up to change of basis? Two matrices $A$ and $B$ represent the same operator in different bases exactly when they are conjugate, $B = P^{-1}AP$, so the classification problem is: **describe the conjugacy classes of matrices, and give each class a distinguished, simplest representative.** A genuine *canonical form* is a rule that picks exactly one matrix from each conjugacy class — so that two matrices are conjugate if and only if they have the same canonical form, turning the hard question "are these conjugate?" into the mechanical question "are these canonical forms equal?".

Diagonalisation answers this for the well-behaved operators — those with a basis of eigenvectors — but most operators are not diagonalisable, and worse, over a field that is not algebraically closed an operator may have *no eigenvalues at all* (rotation by $90^\circ$ on $\mathbb{R}^2$ has characteristic polynomial $X^2 + 1$, irreducible over $\mathbb{R}$, hence no real eigenvalue and no eigenvector). One wants a canonical form that exists for *every* operator over *every* field, with no algebraic-closure hypothesis and no diagonalisability hypothesis. Rational canonical form is exactly that: it is universal, it is genuinely canonical, and — the reason it sits in a module theory course rather than a linear algebra course — it is *not proved by linear algebra at all*. It is a single corollary of a theorem you already have.

Here is the idea, and it is the whole motivation. The pair $(V, \alpha)$ is repackaged, by the construction [[Def - The Module of a Linear Operator|$V_\alpha$]], as a module over $F[X]$ — $X$ acts as $\alpha$. Because $V$ is finite-dimensional, $V_\alpha$ is a *finitely generated* module. Because $F$ is a field, $F[X]$ is a *Euclidean domain*. So $V_\alpha$ is a finitely generated module over a Euclidean domain — and finitely generated modules over a Euclidean domain are *completely classified* by the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]]. The structure theorem says: every such module is a direct sum of a free part and cyclic torsion pieces $R/(d_i)$ with $d_1 \mid d_2 \mid \cdots$. Apply this to $V_\alpha$. The cyclic pieces become $F[X]/(f_i)$; the free part must be absent (a single copy of the free module $F[X]$ is infinite-dimensional over $F$, and $V$ is not); reading the companion matrix off each cyclic piece produces the block-diagonal form. The classification of operators *is* the classification of $F[X]$-modules, and the work was done the moment you proved the structure theorem. Rational canonical form is the cash-out: it is what the structure theorem says when you specialise the Euclidean domain to $F[X]$.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is a linear endomorphism of a *finite-dimensional* vector space over a field. The skill is recognising the situations that secretly hand you one.

The first disguised source is **a single square matrix $A \in M_n(F)$, full stop.** A matrix is an endomorphism of $F^n$ once you fix the standard basis, so *any* square matrix over any field is an input — there is no further hypothesis to check, not diagonalisability, not having eigenvalues, not algebraic closure. The non-obvious recognition is that the theorem's reach is total: every square matrix over every field has a rational canonical form, and "rational" in the name signals exactly this — the form is constructed using only the field operations of $F$ (rational operations), never an extension of $F$. *Example problem:* show the real matrix $\left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$ is already in rational canonical form — it is $C(X^2+1)$, a single companion block, even though it has no real eigenvalue.

The second disguised source is **the question "are these two matrices conjugate?"** Conjugacy of $A$ and $B$ over $F$ is, via $V_\alpha$, isomorphism of the associated $F[X]$-modules; the structure theorem makes the invariant factors a *complete* invariant of an $F[X]$-module, so $A \sim B$ if and only if they have the same invariant factors $f_1 \mid \cdots \mid f_s$. The non-obvious recognition is that an *a priori* infinite search ("does there exist an invertible $P$ with $P^{-1}AP = B$?") collapses to a finite computation: compute both lists of invariant factors and compare. *Example problem:* decide whether two given $4 \times 4$ rational matrices with the same characteristic and minimal polynomials are conjugate — they need not be, and the invariant factors settle it.

The third disguised source is **an $F[X]$-module that is finite-dimensional over $F$, presented without an operator in sight.** Any $F[X]$-module $M$ that happens to be finite-dimensional as an $F$-vector space *is* of the form $V_\alpha$: take $V = M$ as an $F$-space and $\alpha = $ "multiply by $X$". The non-obvious recognition is that the abstract object "finite-dimensional $F[X]$-module" and the concrete object "operator on a finite-dimensional space" are the same thing, so any theorem about one transfers verbatim. *Example problem:* given a finite-dimensional algebra $A$ over $F$ and a chosen element $a \in A$, classify the action of $a$ on $A$ by left multiplication — this is rational canonical form for the operator "multiply by $a$".

**Targets (Output Amplification)**

The bare conclusion is the block-diagonal companion form and the invariant factors $f_1 \mid \cdots \mid f_s$. Combined with other facts it does much more.

Combine the conclusion with **the largest invariant factor.** The minimal polynomial of $\alpha$ is exactly $f_s$. The reason: $f_s(\alpha)$ annihilates the summand $F[X]/(f_s)$, and because every $f_i \mid f_s$ it annihilates every other summand too, so $f_s(\alpha) = 0$ on all of $V_\alpha$; and nothing smaller works, since a polynomial of degree below $\deg f_s$ fails to kill $F[X]/(f_s)$. The further result: the minimal polynomial is *readable directly off the form* with no separate computation, and the **Cayley–Hamilton theorem** drops out — $f_s \mid f_1 \cdots f_s$, so the minimal polynomial divides the characteristic polynomial, hence the characteristic polynomial annihilates $\alpha$.

Combine the conclusion with **the product of all invariant factors.** The characteristic polynomial of $\alpha$ is $f_1 f_2 \cdots f_s$, because the characteristic polynomial of each companion block $C(f_i)$ is $f_i$ and the characteristic polynomial of a block-diagonal matrix is the product of the blocks'. The further result: the characteristic and minimal polynomials *share their irreducible factors* (both are built from the same primes, since $f_1 \mid \cdots \mid f_s$), which is the precise statement of when they coincide — namely $s = 1$, the **cyclic** case, where a single vector and its $\alpha$-images span $V$.

Combine the conclusion with **the divisibility chain as a uniqueness statement.** Insisting each $f_i$ be monic removes the unit ambiguity, and then $f_1 \mid \cdots \mid f_s$ pins the list down completely: the invariant factors are *unique*. The further result: rational canonical form is a *true* canonical form — unlike [[Thm - Jordan Normal Form|Jordan normal form]], whose blocks can be permuted, the companion blocks in the divisibility-ordered form admit no reshuffling — and this is what makes "compute the form and compare" a valid decision procedure for conjugacy.

---

# Why Is It True

The intuition is one sentence: **an operator on a finite-dimensional space is a finitely generated module over a Euclidean domain, and those are already classified — so the operator is already classified.**

Unpack why each clause is forced. First, *why a module*. A linear operator $\alpha$ is not a static piece of data; it is something you can *iterate* — $\alpha, \alpha^2, \alpha^3, \dots$ — and combine with scalars. The natural objects acting on $V$ are therefore not just scalars $\lambda \in F$ but *polynomials in $\alpha$*, expressions $\sum a_i \alpha^i$. The collection of these polynomial expressions, with $X$ standing for $\alpha$, is the ring $F[X]$, and "$V$ together with the action of all polynomials in $\alpha$" is precisely an $F[X]$-module. The repackaging is not a trick; it is the recognition that the honest algebraic object attached to an operator is a module, because an operator is something you take polynomials of.

Second, *why finitely generated, and why no free part*. $V$ is finite-dimensional, with a finite $F$-basis; that basis already generates $V_\alpha$ over the larger ring $F[X]$, so $V_\alpha$ is finitely generated. Could $V_\alpha$ contain a copy of the free module $F[X]$? No — and this is the one place finite dimension does decisive work. The free module $F[X]$ is *infinite-dimensional* as an $F$-vector space: it has the infinite $F$-basis $1, X, X^2, \dots$. A submodule of the finite-dimensional $V_\alpha$ cannot be infinite-dimensional. So the free rank of $V_\alpha$ is zero — $V_\alpha$ is **all torsion**. Concretely, torsion here means every vector $v$ satisfies $f(\alpha)(v) = 0$ for some nonzero polynomial $f$, which is just the familiar fact that the iterates $v, \alpha v, \alpha^2 v, \dots$ cannot stay linearly independent forever in a finite-dimensional space.

Third, *why this finishes it*. The [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] says a finitely generated module over a Euclidean domain $R$ is a direct sum of a free part $R^d$ and cyclic torsion pieces $R/(f_1) \oplus \cdots \oplus R/(f_s)$ with $f_1 \mid \cdots \mid f_s$. We have just argued the free part is absent, so $V_\alpha \cong F[X]/(f_1) \oplus \cdots \oplus F[X]/(f_s)$. That is the entire decomposition — handed over by a theorem already proved.

Fourth, *why this is a matrix statement*. A direct sum of modules means $V$ splits into $\alpha$-invariant subspaces, one per summand, and on the $i$-th of these $\alpha$ acts as multiplication-by-$X$ on $F[X]/(f_i)$. But the matrix of multiplication-by-$X$ on $F[X]/(f_i)$ in the natural basis is, by definition, the [[Def - The Module of a Linear Operator|companion matrix]] $C(f_i)$. A direct sum of operators is a block-diagonal matrix. So $\alpha$ is block-diagonal with blocks $C(f_1), \dots, C(f_s)$. Nothing here is computed; it is all read off.

Finally, *why the minimal and characteristic polynomials are what they are*. On the summand $F[X]/(f_s)$ the operator $f_s(\alpha)$ is multiplication by $f_s$, which is $0$ in the quotient $F[X]/(f_s)$ — and since every $f_i$ divides $f_s$, the same $f_s(\alpha)$ kills every other summand. So $f_s(\alpha) = 0$, and no lower-degree polynomial does (it would survive on $F[X]/(f_s)$); $f_s$ is the minimal polynomial. The characteristic polynomial is multiplicative over the blocks and the companion block $C(f_i)$ has characteristic polynomial $f_i$ (its $F$-dimension is $\deg f_i$, and a companion matrix is engineered so its characteristic polynomial is its defining polynomial), so the characteristic polynomial of $\alpha$ is $f_1 \cdots f_s$. The whole theorem is the structure theorem looked at through the dictionary "$F[X]$-module $=$ operator".

---

# What Makes This Hard

The genuine difficulty is entirely upstream: rational canonical form is a *short* deduction from the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]], so all the real work lives in that theorem — the trap is trying to prove canonical form by direct linear algebra (chasing invariant subspaces and cyclic vectors by hand) instead of invoking the module classification. Within the deduction itself the one non-obvious step is the *vanishing of the free part*: one must notice that a single free summand $F[X]$ is infinite-dimensional over $F$ and therefore cannot sit inside the finite-dimensional $V_\alpha$. The most common error is forgetting to justify this and writing the decomposition with no comment on why there are no $F[X]$ summands; a secondary error is conflating rational canonical form with [[Thm - Jordan Normal Form|Jordan form]] and wrongly assuming an algebraically closed field is needed.

---

# Rederivation Scaffold

**High-level strategy:**
Do not attempt linear algebra. Repackage $(V, \alpha)$ as the $F[X]$-module $V_\alpha$; observe $F[X]$ is a Euclidean domain and $V_\alpha$ is finitely generated; invoke the structure theorem; kill the free part using finite-dimensionality; translate each cyclic summand $F[X]/(f_i)$ into a companion block.

**Subgoal decomposition:**

1. **Set up the module.** Form the $F[X]$-module $V_\alpha$ — the space $V$ with $X$ acting as $\alpha$ — and check it is finitely generated.
   - *Hint:* An $F$-basis of $V$ generates $V_\alpha$ over $F[X]$, because $F \subseteq F[X]$. See [[Def - The Module of a Linear Operator]].
   - *Why needed:* It puts the problem inside the realm where the structure theorem applies.

2. **Invoke the structure theorem.** Apply the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] over the Euclidean domain $R = F[X]$ to write $V_\alpha \cong F[X]^d \oplus F[X]/(f_1) \oplus \cdots \oplus F[X]/(f_s)$ with $f_1 \mid \cdots \mid f_s$.
   - *Hint:* $F[X]$ is a Euclidean domain because $F$ is a field — the Euclidean function is the degree. The invariant-factor form gives the divisibility chain for free.
   - *Why needed:* This is the entire classification; everything after is translation.

3. **Eliminate the free part.** Show $d = 0$: there are no copies of $F[X]$.
   - *Hint:* $F[X]$ has infinite $F$-dimension (basis $1, X, X^2, \dots$); $V_\alpha = V$ has finite $F$-dimension. A free summand would make the whole module infinite-dimensional.
   - *Why needed:* Without this step the decomposition would carry an unwanted infinite-dimensional summand and could not describe a matrix.

4. **Translate to a matrix.** Interpret the direct sum as a decomposition of $V$ into $\alpha$-invariant subspaces and read the companion matrix off each.
   - *Hint:* On the summand $F[X]/(f_i)$, the operator $\alpha$ is multiplication by $X$, whose matrix in the basis $1, X, \dots, X^{\deg f_i - 1}$ is $C(f_i)$. A direct sum of operators is block-diagonal.
   - *Why needed:* Converts the module isomorphism into the stated canonical form.

5. **Read off the polynomials.** Identify the minimal polynomial as $f_s$ and the characteristic polynomial as $f_1 \cdots f_s$.
   - *Hint:* $f_s(\alpha)$ kills $F[X]/(f_s)$ hence (by $f_i \mid f_s$) every summand; characteristic polynomials multiply across blocks and $C(f_i)$ has characteristic polynomial $f_i$.
   - *Why needed:* Delivers the invariants used in practice and yields Cayley–Hamilton as a corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: $V_\alpha$ is a finitely generated $F[X]$-module
> **Statement:** If $V$ is finite-dimensional over $F$, the module $V_\alpha$ is finitely generated over $F[X]$.
>
> **Hint:** A spanning set over the subring $F$ is a generating set over $F[X]$.
>
> **Why needed:** It is the hypothesis the structure theorem demands.
>
> > [!note]- Full proof
> > Let $v_1, \dots, v_n$ be an $F$-basis of $V$, so every $v \in V$ is an $F$-linear combination $\sum_i \lambda_i v_i$ with $\lambda_i \in F$. The scalars $F$ form a subring of $F[X]$ (the constant polynomials), and the $F[X]$-action on $V_\alpha$ restricts on constants to the original $F$-action. Hence every $F$-linear combination is in particular an $F[X]$-linear combination: $v = \sum_i \lambda_i \cdot v_i$ exhibits $v$ in the $F[X]$-submodule generated by $v_1, \dots, v_n$. So $\{v_1, \dots, v_n\}$ generates $V_\alpha$ as an $F[X]$-module, and $V_\alpha$ is finitely generated.

> [!note]- Lemma 2: $V_\alpha$ has no free part
> **Statement:** In the structure-theorem decomposition of $V_\alpha$, the free rank is $0$: no summand is a copy of $F[X]$.
>
> **Hint:** Compare $F$-dimensions — $F[X]$ is infinite-dimensional over $F$, $V$ is finite-dimensional.
>
> **Why needed:** It reduces the decomposition to purely cyclic torsion summands, so that a matrix can be read off.
>
> > [!note]- Full proof
> > Suppose, for contradiction, the decomposition contained at least one free summand, so $V_\alpha \cong F[X]^d \oplus T$ with $d \geq 1$ and $T$ the torsion part. As an $F$-vector space, $F[X]$ has the infinite linearly independent set $\{1, X, X^2, X^3, \dots\}$ — no finite $F$-linear combination of distinct powers of $X$ vanishes — so $F[X]$ is infinite-dimensional over $F$. A direct sum containing an infinite-dimensional $F$-subspace is itself infinite-dimensional over $F$. Thus $V_\alpha$ would be infinite-dimensional over $F$. But $V_\alpha = V$ as an $F$-vector space, and $V$ is finite-dimensional by hypothesis — a contradiction. Hence $d = 0$ and $V_\alpha$ is a direct sum of cyclic torsion modules $F[X]/(f_i)$.

> [!note]- Lemma 3: the operator on $F[X]/(f)$ is the companion matrix
> **Statement:** Regard the cyclic module $F[X]/(f)$, for monic $f$ of degree $r$, as an $F[X]$-module. The operator "multiply by $X$" is $F$-linear, and in the $F$-basis $1, X, \dots, X^{r-1}$ its matrix is the companion matrix $C(f)$.
>
> **Hint:** Multiplying a basis vector $X^j$ by $X$ gives $X^{j+1}$; for $j = r-1$ use $X^r = -a_0 - \cdots - a_{r-1}X^{r-1}$ in the quotient.
>
> **Why needed:** It converts each module summand into an explicit matrix block.
>
> > [!note]- Full proof
> > Write $f = a_0 + a_1 X + \cdots + a_{r-1}X^{r-1} + X^r$. The quotient ring $F[X]/(f)$, as an $F$-vector space, has basis the residue classes of $1, X, \dots, X^{r-1}$: division with remainder by the monic polynomial $f$ writes every polynomial uniquely as $qf + s$ with $\deg s < r$, so the classes of $1, \dots, X^{r-1}$ span and are independent. Multiplication by $X$ is $F$-linear because the ring multiplication is $F$-bilinear and $F$ is central. On a basis vector $X^j$ with $0 \leq j \leq r-2$, multiplication by $X$ yields $X^{j+1}$, again a basis vector — contributing the column $e_{j+2}$, i.e. a single $1$ on the subdiagonal. On the last basis vector $X^{r-1}$, multiplication by $X$ yields $X^r$; but $f \equiv 0$, so $X^r \equiv -(a_0 + a_1 X + \cdots + a_{r-1}X^{r-1})$, contributing the last column $(-a_0, -a_1, \dots, -a_{r-1})^{\mathsf T}$. Assembling the columns gives exactly $C(f)$.

> [!note]- Lemma 4: minimal and characteristic polynomials
> **Statement:** For $\alpha$ with invariant factors $f_1 \mid \cdots \mid f_s$, the minimal polynomial of $\alpha$ is $f_s$ and the characteristic polynomial is $f_1 f_2 \cdots f_s$.
>
> **Hint:** $f_s$ kills the largest summand, hence all; characteristic polynomials multiply over a block-diagonal matrix, and $C(f_i)$ has characteristic polynomial $f_i$.
>
> **Why needed:** It extracts from the canonical form the two invariants used in computation and yields Cayley–Hamilton.
>
> > [!note]- Full proof
> > **Minimal polynomial.** Under $V_\alpha \cong \bigoplus_i F[X]/(f_i)$, a polynomial $g$ satisfies $g(\alpha) = 0$ on $V_\alpha$ if and only if $g(\alpha)$ kills every summand, i.e. $g \in (f_i)$ for every $i$, i.e. $f_i \mid g$ for every $i$. Because $f_1 \mid f_2 \mid \cdots \mid f_s$, the largest factor $f_s$ is a multiple of all the others, so "$f_i \mid g$ for all $i$" is equivalent to "$f_s \mid g$". The monic generator of the set of such $g$ is therefore $f_s$ itself: $f_s(\alpha) = 0$, and no monic polynomial of smaller degree annihilates $\alpha$ (it would fail to be divisible by $f_s$, hence fail to kill $F[X]/(f_s)$). So the minimal polynomial is $f_s$.
> >
> > **Characteristic polynomial.** In the basis giving the block-diagonal form, the matrix of $\alpha$ is $\operatorname{diag}(C(f_1), \dots, C(f_s))$, and the characteristic polynomial of a block-diagonal matrix is the product of the characteristic polynomials of the blocks. The companion matrix $C(f_i)$ of a monic degree-$r_i$ polynomial has characteristic polynomial $\det(X I - C(f_i)) = f_i$ — an induction on $r_i$ via cofactor expansion along the first row, or the observation that the cyclic module $F[X]/(f_i)$ has $F$-dimension $r_i$ and minimal polynomial $f_i$, forcing the degree-$r_i$ characteristic polynomial to equal $f_i$. Hence the characteristic polynomial of $\alpha$ is $f_1 f_2 \cdots f_s$. Since $f_s \mid f_1 \cdots f_s$, the minimal polynomial divides the characteristic polynomial — the **Cayley–Hamilton theorem**.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\alpha : V \to V$ be a linear endomorphism of a finite-dimensional vector space over a field $F$.
>
> **Step 1 — form the module.** By [[Def - The Module of a Linear Operator|the construction]], $V$ becomes an $F[X]$-module $V_\alpha$ with $f(X) \cdot v = f(\alpha)(v)$; in particular $X$ acts as $\alpha$. By Lemma 1, since $\dim_F V < \infty$, the module $V_\alpha$ is finitely generated over $F[X]$.
>
> **Step 2 — the ring is a Euclidean domain.** Because $F$ is a field, the polynomial ring $F[X]$ is a [[Def - Euclidean Domain|Euclidean domain]]: the degree function $\deg$ is a Euclidean function, since division with remainder of one polynomial by another holds whenever the divisor is nonzero (the [[Thm - Euclidean Algorithm for Polynomials|division algorithm for polynomials]]).
>
> **Step 3 — apply the structure theorem.** $V_\alpha$ is a finitely generated module over the Euclidean domain $F[X]$, so the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]], in invariant-factor form, gives an $F[X]$-module isomorphism
> $$V_\alpha \;\cong\; F[X]^{\,d} \,\oplus\, \frac{F[X]}{(f_1)} \,\oplus\, \cdots \,\oplus\, \frac{F[X]}{(f_s)},$$
> with each $f_i$ a non-unit and $f_1 \mid f_2 \mid \cdots \mid f_s$. Normalising each $f_i$ to be monic (multiplying by the unit that scales its leading coefficient to $1$) does not change the ideals $(f_i)$ and preserves the divisibility chain.
>
> **Step 4 — the free part vanishes.** By Lemma 2, $d = 0$: a single summand $F[X]$ is infinite-dimensional as an $F$-vector space (it contains the infinite independent family $1, X, X^2, \dots$), whereas $V_\alpha = V$ is finite-dimensional over $F$, so no free summand can occur. Hence
> $$V_\alpha \;\cong\; \frac{F[X]}{(f_1)} \,\oplus\, \cdots \,\oplus\, \frac{F[X]}{(f_s)}, \qquad f_1 \mid \cdots \mid f_s,$$
> with every $f_i$ monic of degree $\geq 1$. This is the asserted module decomposition.
>
> **Step 5 — read off the matrix.** A direct-sum decomposition of $V_\alpha$ is a decomposition of $V$ into $\alpha$-invariant subspaces $V = W_1 \oplus \cdots \oplus W_s$, where $W_i$ is the copy of $F[X]/(f_i)$ and $\alpha$ restricts to multiplication by $X$ on it. By Lemma 3, choosing on each $W_i$ the basis $1, X, \dots, X^{\deg f_i - 1}$ makes the matrix of $\alpha|_{W_i}$ equal to the companion matrix $C(f_i)$. Concatenating these bases gives a basis of $V$ in which $\alpha$ is block-diagonal,
> $$
> \begin{pmatrix}
> C(f_1) & & \\
> & \ddots & \\
> & & C(f_s)
> \end{pmatrix},
> $$
> the rational canonical form.
>
> **Step 6 — invariants and uniqueness.** By Lemma 4, the minimal polynomial of $\alpha$ is the largest invariant factor $f_s$, and the characteristic polynomial of $\alpha$ is the product $f_1 f_2 \cdots f_s$. The structure theorem determines the invariant factors $f_i$ uniquely up to units; the monic normalisation removes the unit ambiguity, so the monic invariant factors $f_1 \mid \cdots \mid f_s$ — hence the block-diagonal companion form itself — are uniquely determined by $\alpha$. Therefore the form is a genuine canonical form: in matrix language, every $A \in M_n(F)$ is conjugate to exactly one matrix of this shape. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Conjugacy of matrices over a finite field.** Count the conjugacy classes of $n \times n$ matrices over the finite field $\mathbb{F}_q$. The theorem applies because each class corresponds to a list of monic invariant factors $f_1 \mid \cdots \mid f_s$ with $\sum \deg f_i = n$; the count becomes the combinatorial problem of enumerating such divisibility chains of polynomials over $\mathbb{F}_q$ of total degree $n$. The non-obvious step is that a question about matrices and conjugation is, through $V_\alpha$, a question about factorising polynomials over $\mathbb{F}_q$ — the finite field enters only as the coefficient field of $F[X]$.

**Solving systems of linear recurrences and linear ODEs.** A constant-coefficient linear recurrence, or a first-order linear ODE system $\dot{\mathbf x} = A\mathbf x$, is governed by powers of a fixed matrix $A$. Putting $A$ in rational canonical form decouples the system into independent blocks, one per invariant factor, and on the block $C(f_i)$ the dynamics is the companion-form recurrence with characteristic polynomial $f_i$. The non-obvious recognition is that the *invariant factors*, not the eigenvalues, are the field-intrinsic data controlling the solution — essential precisely when $A$ has no eigenvalues over the field of interest.

**Modules over $\mathbb{Z}$ versus modules over $F[X]$ — a structural analogy battle-test.** The structure theorem applied to $\mathbb{Z}$ classifies finitely generated abelian groups; applied to $F[X]$ it yields rational canonical form. Pose the exercise: given the analogy "finite abelian group $\leftrightarrow$ operator on a finite-dimensional space", translate a statement about abelian groups (say, the number of subgroups of given order) into the operator world. The application is nonobvious because the two theorems look unrelated until one sees both as the single Euclidean-domain structure theorem, with the only change being which Euclidean domain is plugged in.

**The endomorphism algebra acting on itself.** Let $A$ be a finite-dimensional associative algebra over $F$ and fix $a \in A$. Left multiplication $L_a : x \mapsto ax$ is a linear operator on the finite-dimensional space $A$, so it has a rational canonical form, and its invariant factors classify $a$ up to a natural equivalence. The non-obvious point is that an element of an abstract algebra is studied by turning it into an operator (on the algebra itself) and feeding that operator to the theorem — the "regular representation" trick — recovering, among other things, that the minimal polynomial of $a$ in $A$ is the minimal polynomial of $L_a$.

---

# Bridges

- **[[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|Structure Theorem over a Euclidean Domain]]** — the parent theorem. Rational canonical form is *literally* the structure theorem with the Euclidean domain taken to be $F[X]$ and the free part argued away; no new mathematics is added, only specialisation and translation.

- **[[Thm - Jordan Normal Form|Jordan Normal Form]]** — the sibling. Jordan form comes from feeding $V_\alpha$ to the [[Thm - Primary Decomposition Theorem|primary decomposition theorem]] instead of the invariant-factor structure theorem; it needs the field to be algebraically closed (so the primes of the polynomial ring are all linear), whereas rational canonical form needs no such hypothesis. The two are different repackagings of the same module $V_\alpha$ — primary pieces versus invariant factors. Rational canonical form is canonical; Jordan form is not, since its blocks may be permuted.

- **[[Thm - Smith Normal Form|Smith Normal Form]]** — the computational engine. The invariant factors $f_i$ are obtained in practice by reducing the characteristic matrix $X I - A$ (a matrix over $F[X]$) to diagonal form $\operatorname{diag}(1, \dots, 1, f_1, \dots, f_s)$ via [[Def - Elementary Operations and Equivalent Matrices|elementary row and column operations]] over $F[X]$ — Smith normal form supplies the algorithm that rational canonical form's existence proof leaves abstract.

- **Cayley–Hamilton Theorem** — an immediate corollary. Since the minimal polynomial is $f_s$ and the characteristic polynomial is $f_1 \cdots f_s$, and $f_s \mid f_1 \cdots f_s$, the minimal polynomial divides the characteristic polynomial; hence the characteristic polynomial annihilates $\alpha$. Rational canonical form proves Cayley–Hamilton without determinant trickery.

---

# Unlocked by This

> [!tip] Conjugacy Classes and the Class Equation for $GL_n$ *(from Representation Theory)*
> Because the rational canonical form is a complete invariant of conjugacy, the conjugacy classes of $GL_n(F)$ are parametrised by lists of invariant factors. This parametrisation is the starting point for counting classes, building character tables of $GL_n(\mathbb{F}_q)$, and the representation theory of finite groups of Lie type.

> [!tip] Modules over a Principal Ideal Domain in Algebraic Geometry *(from Commutative Algebra)*
> Viewing an operator as an $F[X]$-module is the first instance of studying a geometric object — here the "spectrum" of the operator — through a module over a coordinate ring. The invariant factors are the algebraic shadow of the operator's spectral data, and this perspective generalises to coherent sheaves on a curve.

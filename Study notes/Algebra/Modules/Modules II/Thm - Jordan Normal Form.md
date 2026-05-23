---
type: theorem
subject: module-theory
prereqs:
  - "Def - The Module of a Linear Operator"
  - "Def - Polynomial Ring"
  - "Def - Irreducible and Prime Elements"
  - "Def - Module"
  - "Thm - Primary Decomposition Theorem"
  - "Thm - Rational Canonical Form"
tags: [algebra, module-theory]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $\mathbb{C}$ (or over any algebraically closed field) and $\alpha : V \to V$ is a linear endomorphism. The [[Def - Polynomial Ring|polynomial ring]] $\mathbb{C}[X]$ is a Euclidean domain. The $\mathbb{C}[X]$-module $V_\alpha$ is $V$ with $X$ acting as $\alpha$, so $f(X) \cdot v = f(\alpha)(v)$ — see [[Def - The Module of a Linear Operator]]. For $\lambda \in \mathbb{C}$ and $m \geq 1$, the **Jordan block** $J_m(\lambda)$ is the $m \times m$ matrix
$$
J_m(\lambda) =
\begin{pmatrix}
\lambda & 0 & \cdots & 0 \\
1 & \lambda & \cdots & 0 \\
\vdots & \ddots & \ddots & \vdots \\
0 & \cdots & 1 & \lambda
\end{pmatrix}
$$
— that is, $\lambda$ on the diagonal, $1$ on the subdiagonal, $0$ elsewhere (the lower-triangular convention). The notation $f \mid g$ is divisibility in $\mathbb{C}[X]$, and $\cong$ is $\mathbb{C}[X]$-module isomorphism. The full registry is on the parent page [[Modules II — §3.3–3.4]].

---

# Statement

> **Jordan Normal Form.** Let $\alpha : V \to V$ be a linear endomorphism of a finite-dimensional vector space $V$ over $\mathbb{C}$ (or over any algebraically closed field), and let $V_\alpha$ be the associated $\mathbb{C}[X]$-module. Then
> $$V_\alpha \;\cong\; \frac{\mathbb{C}[X]}{\big((X-\lambda_1)^{a_1}\big)} \,\oplus\, \frac{\mathbb{C}[X]}{\big((X-\lambda_2)^{a_2}\big)} \,\oplus\, \cdots \,\oplus\, \frac{\mathbb{C}[X]}{\big((X-\lambda_t)^{a_t}\big)}$$
> as $\mathbb{C}[X]$-[[Def - Module|modules]], where $\lambda_1, \dots, \lambda_t \in \mathbb{C}$ (not necessarily distinct) and $a_1, \dots, a_t \geq 1$. Consequently there is a basis of $V$ in which the matrix of $\alpha$ is **block-diagonal with Jordan blocks**:
> $$
> \begin{pmatrix}
> J_{a_1}(\lambda_1) & & & \\
> & J_{a_2}(\lambda_2) & & \\
> & & \ddots & \\
> & & & J_{a_t}(\lambda_t)
> \end{pmatrix}.
> $$
> The multiset of Jordan blocks is uniquely determined by $\alpha$ (so the form is unique up to the order of the blocks). From the form one reads off:
> - the **characteristic polynomial** $\prod_{i=1}^t (X - \lambda_i)^{a_i} = \prod_\lambda (X-\lambda)^{b_\lambda}$, where $b_\lambda$ is the sum of the sizes of all $\lambda$-blocks;
> - the **minimal polynomial** $\prod_\lambda (X-\lambda)^{c_\lambda}$, where $c_\lambda$ is the size of the *largest* $\lambda$-block;
> - the **geometric multiplicity** of an eigenvalue $\lambda$ — the [[Def - Dimension|dimension]] of the $\lambda$-eigenspace $\ker(\alpha - \lambda\operatorname{id})$ — which equals the *number* of $\lambda$-blocks.

---

# Motivation

[[Thm - Rational Canonical Form|Rational canonical form]] already classifies every operator over every field, with companion-matrix blocks. Why want a second normal form? Because a companion matrix, while canonical and field-intrinsic, is *opaque*: stare at $C(f)$ and you cannot see the eigenvalues, cannot see whether the operator is diagonalisable, cannot read off how badly diagonalisation fails. A companion block of size $5$ might be a clean diagonalisable piece or a maximally tangled nilpotent-plus-scalar piece — the matrix does not tell you at a glance. One wants a normal form whose blocks are as *small* and as *transparent* as possible, blocks on which the operator's spectral behaviour is manifest.

The Jordan block $J_m(\lambda)$ is exactly that transparent block. It is $\lambda$ on the diagonal plus a nilpotent shift below it, so it instantly reveals: the only eigenvalue is $\lambda$; the operator restricted to the block is *almost* the scalar $\lambda$, failing by a single nilpotent shift of nilpotency degree $m$; it is diagonalisable precisely when $m = 1$. A Jordan form displays an operator as a diagonal matrix corrected by the smallest possible nilpotent perturbations, and the *sizes* of the blocks measure precisely how far the operator is from being diagonalisable. This is the normal form you want for computing matrix powers, matrix exponentials, and the asymptotics of linear dynamical systems.

But there is a price, and naming it explains the hypothesis. A Jordan block has a *single* eigenvalue $\lambda$ sitting visibly on its diagonal — so for an operator to have a Jordan form *every* block must contribute an eigenvalue, which means $\alpha$ must have *enough eigenvalues*: its characteristic polynomial must split into linear factors. Over $\mathbb{R}$ this fails — rotation by $90^\circ$ has characteristic polynomial $X^2 + 1$ with no real root, hence no Jordan form over $\mathbb{R}$. Over $\mathbb{C}$ it never fails, by the fundamental theorem of algebra: every non-constant polynomial splits completely. So Jordan normal form lives over $\mathbb{C}$ — or any algebraically closed field — and the hypothesis of algebraic closure is not a technicality but the exact condition that lets every block carry an eigenvalue.

The route to it is the same module-theoretic machine as for rational canonical form, with one part swapped. Rational canonical form came from feeding $V_\alpha$ to the invariant-factor structure theorem. Jordan form comes from feeding $V_\alpha$ to the *other* decomposition — the [[Thm - Primary Decomposition Theorem|primary decomposition theorem]], which breaks a torsion module into pieces, one per prime, each a sum of cyclic [[Def - Module|modules]] $R/(p^k)$ for a fixed prime $p$. To use it we must know the *primes of $\mathbb{C}[X]$*. And here the fundamental theorem of algebra enters a second time: the primes of $\mathbb{C}[X]$ are exactly the linear polynomials $X - \lambda$. So every primary piece of $V_\alpha$ is a sum of cyclic modules $\mathbb{C}[X]/\big((X-\lambda)^m\big)$ — and a cyclic module of that exact shape is, by the [[Def - The Module of a Linear Operator|Jordan-block example]], one Jordan block. Jordan normal form is primary decomposition over $\mathbb{C}[X]$, translated through the dictionary "$\mathbb{C}[X]$-module $=$ operator".

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is a linear endomorphism of a finite-dimensional vector space *over an algebraically closed field*. The skill is recognising the disguises and knowing how to manufacture algebraic closure when it is not handed to you.

The first disguised source is **any square matrix over $\mathbb{C}$, with no further hypothesis.** Because $\mathbb{C}$ is algebraically closed, *every* complex square matrix has a Jordan form — not only the diagonalisable ones. The non-obvious recognition is that the theorem covers the defective matrices, the ones with too few eigenvectors, and that the Jordan blocks of size $> 1$ are precisely the obstruction to diagonalisability. *Example problem:* show $\left(\begin{smallmatrix}2 & 0\\ 1 & 2\end{smallmatrix}\right)$ is not diagonalisable — it is already a single Jordan block $J_2(2)$, and a single block of size $>1$ can never be diagonal.

The second disguised source is **a matrix over a non-closed field, after base change to the algebraic closure.** A matrix $A$ over $\mathbb{R}$, or over $\mathbb{Q}$, has no Jordan form over its own field, but it has one over $\mathbb{C}$ (or over $\overline{\mathbb{Q}}$): regard $A$ as a complex matrix. The non-obvious recognition is that *enlarging the field* is a legitimate and often necessary move — properties invariant under base change (rank, characteristic polynomial, similarity over the closure) can then be computed in Jordan form even though the form itself does not live over the original field. *Example problem:* compute the eigenvalues and the powers $A^n$ of a real matrix by passing to its complex Jordan form.

The third disguised source is **a finite-dimensional $\mathbb{C}[X]$-module given abstractly.** Any $\mathbb{C}[X]$-module $M$ that is finite-dimensional as a $\mathbb{C}$-vector space is $V_\alpha$ for $V = M$ and $\alpha = $ multiply-by-$X$, hence has a Jordan form. The non-obvious recognition is the identification of the abstract category "finite-dimensional $\mathbb{C}[X]$-modules" with the concrete category "operators on finite-dimensional complex spaces" — the theorem is then a statement about the abstract module. *Example problem:* classify, up to isomorphism, the finite-dimensional modules over $\mathbb{C}[X]$ — the answer is exactly the multisets of Jordan blocks.

The fourth disguised source is **a representation of a cyclic group or of $\mathbb{Z}$.** A representation of $\mathbb{Z}$ on a finite-dimensional complex space is a single invertible operator; a representation of the cyclic group $\mathbb{Z}/n$ is an operator $\alpha$ with $\alpha^n = \operatorname{id}$. Both are operators, hence have Jordan forms. The non-obvious recognition is that a constraint like $\alpha^n = \operatorname{id}$ forces the minimal polynomial to divide $X^n - 1$, which over $\mathbb{C}$ has distinct roots, so every Jordan block has size $1$ — the representation is diagonalisable. *Example problem:* prove every finite-order complex operator is diagonalisable.

**Targets (Output Amplification)**

The bare conclusion is the block-diagonal Jordan form. Combined with other facts it yields a great deal of the working theory of operators.

Combine the conclusion with **block sizes versus diagonalisability.** An operator is diagonalisable if and only if *every* Jordan block has size $1$, equivalently if and only if its minimal polynomial $\prod_\lambda (X-\lambda)^{c_\lambda}$ has every $c_\lambda = 1$, i.e. is a product of *distinct* linear factors with no repetition. The further result: a clean criterion — **an operator over $\mathbb{C}$ is diagonalisable exactly when its minimal polynomial has no repeated root** — and a quantitative measure of failure, the largest block size $c_\lambda$.

Combine the conclusion with **functions of the operator.** On a single Jordan block $J_m(\lambda) = \lambda I + N$ with $N$ the nilpotent shift ($N^m = 0$), any power, the exponential, or any analytic function is computed by a *finite* binomial/Taylor expansion, because $N$ is nilpotent: $J_m(\lambda)^k = \sum_{j=0}^{m-1}\binom{k}{j}\lambda^{k-j}N^j$, and $e^{tJ_m(\lambda)} = e^{t\lambda}\sum_{j=0}^{m-1}\frac{t^j}{j!}N^j$. The further result: matrix powers and matrix exponentials become explicit and closed-form once the Jordan form is known — this is the computational payoff that makes Jordan form indispensable for linear recurrences and linear differential equations.

Combine the conclusion with **counting blocks by kernel dimensions.** The number of $\lambda$-blocks is $\dim\ker(\alpha - \lambda\operatorname{id})$, and more finely, the number of $\lambda$-blocks of size $\geq k$ is $\operatorname{rank}(\alpha-\lambda\operatorname{id})^{k-1} - \operatorname{rank}(\alpha-\lambda\operatorname{id})^{k}$. The further result: the entire Jordan structure at $\lambda$ is recoverable from the *ranks of powers* of $\alpha - \lambda\operatorname{id}$ — a finite, mechanical computation — which is how one actually determines the Jordan form of a given matrix and how one proves the uniqueness of the form.

---

# Why Is It True

The intuition: **primary decomposition splits a torsion module one prime at a time; over $\mathbb{C}[X]$ the primes are the linear polynomials, and a prime-power cyclic piece $\mathbb{C}[X]/((X-\lambda)^m)$ is exactly one Jordan block.** Three observations make the theorem unsurprising.

*First, why decompose, and why this decomposition.* The operator $\alpha$ on the finite-dimensional $V$ packages, by [[Def - The Module of a Linear Operator|the construction]], into the $\mathbb{C}[X]$-module $V_\alpha$, which — exactly as in rational canonical form — is finitely generated and a *torsion* module (no free part, because a free summand $\mathbb{C}[X]$ is infinite-dimensional over $\mathbb{C}$). Now, a finite torsion module over a Euclidean domain can be cut up in two ways. The invariant-factor way gives rational canonical form. The *primary* way — the [[Thm - Primary Decomposition Theorem|primary decomposition theorem]] — is the analogue of decomposing a finite abelian [[Def - Group|group]] into its $p$-primary parts: it isolates, for each prime $p$, the part of the module annihilated by a power of $p$, and that primary part is a direct sum of cyclic modules $\mathbb{C}[X]/(p^k)$. We choose the primary decomposition because its building blocks $\mathbb{C}[X]/(p^k)$ are *as small as a torsion cyclic module gets* — they cannot be split further — and small transparent blocks are what a Jordan form is.

*Second, why the field must be $\mathbb{C}$ — and what the primes are.* The primary decomposition is indexed by the primes of $\mathbb{C}[X]$, so to use it we must know them. A non-constant $f \in \mathbb{C}[X]$, by the **fundamental theorem of algebra**, has a root $\lambda \in \mathbb{C}$, hence is divisible by $X - \lambda$; so the only [[Def - Irreducible and Prime Elements|irreducible]] polynomials are the linear ones $X - \lambda$ (degree-$1$ polynomials are automatically irreducible, and $\mathbb{C}[X]$ being a Euclidean domain, irreducible equals prime). *This is the entire role of algebraic closure.* Over $\mathbb{R}$ there are irreducible quadratics $X^2 + bX + c$, the primary pieces $\mathbb{R}[X]/(q^k)$ for those quadratics are not Jordan blocks, and no Jordan form results. Over $\mathbb{C}$ every prime is linear, so every primary piece is a $\mathbb{C}[X]/\big((X-\lambda)^m\big)$.

*Third, why a prime-power piece is a Jordan block.* Take the cyclic module $\mathbb{C}[X]/\big((X-\lambda)^m\big)$. On it, $\alpha$ acts as multiplication by $X$. Set $\beta = \alpha - \lambda\operatorname{id}$ — multiplication by $X - \lambda$. With $Y = X - \lambda$ the module becomes $\mathbb{C}[Y]/(Y^m)$, and on *that* the operator $\beta$, "multiply by $Y$", is the pure nilpotent shift — the companion matrix $C(Y^m)$, with $1$s on the subdiagonal and $0$s elsewhere — exactly the nilpotent-shift example. Therefore $\alpha = \beta + \lambda\operatorname{id}$ is the subdiagonal shift with $\lambda$ added down the diagonal: that matrix *is* the Jordan block $J_m(\lambda)$. A direct sum of such pieces is a block-diagonal matrix of Jordan blocks. So the theorem says nothing new beyond primary decomposition; it is primary decomposition spelled in matrices.

*Why the readings-off are forced.* The characteristic polynomial multiplies over the blocks and $J_m(\lambda)$ — being lower-triangular with $\lambda$ on the diagonal — has characteristic polynomial $(X-\lambda)^m$, so the characteristic polynomial of $\alpha$ is $\prod_i (X-\lambda_i)^{a_i}$. The minimal polynomial of a single block $J_m(\lambda)$ is $(X-\lambda)^m$, because the nilpotent shift $N$ on an $m$-dimensional space has $N^{m-1}\neq 0$ but $N^m = 0$; across several $\lambda$-blocks the polynomial that kills them all is $(X-\lambda)$ to the *largest* block size — hence $c_\lambda$ is the size of the biggest $\lambda$-block. And the $\lambda$-eigenspace: a Jordan block $J_m(\lambda)$ contributes exactly a *one*-dimensional space of $\lambda$-eigenvectors (the kernel of its nilpotent part $N$ is one-dimensional, spanned by the last basis vector), so the geometric multiplicity of $\lambda$ — the total $\lambda$-eigenspace [[Def - Dimension|dimension]] — counts the $\lambda$-blocks, one dimension apiece.

---

# What Makes This Hard

The conceptual work is upstream in the [[Thm - Primary Decomposition Theorem|primary decomposition theorem]]; given that, Jordan form is a short deduction, and the trap is attempting it by hand with generalised eigenvectors instead of invoking the module decomposition. The single genuinely load-bearing step that is *specific* to Jordan form is identifying the primes of $\mathbb{C}[X]$ as exactly the linear polynomials $X - \lambda$ — this is where the fundamental theorem of algebra is used, and skipping it (or not noticing that algebraic closure is precisely what makes every prime linear) is the most common omission. A second frequent error is claiming the Jordan form is *canonical*: it is unique only up to permuting the blocks, and this uniqueness is not delivered by the existence argument here — it requires the rank-of-powers count and is deferred.

---

# Rederivation Scaffold

**High-level strategy:**
Repackage $(V, \alpha)$ as the $\mathbb{C}[X]$-module $V_\alpha$ (finitely generated, all torsion). Apply the *primary* decomposition theorem. Identify the primes of $\mathbb{C}[X]$ as the linear polynomials $X-\lambda$, using the fundamental theorem of algebra. Each primary cyclic piece is then $\mathbb{C}[X]/((X-\lambda)^m)$; translate it to a Jordan block via the shift $\beta = \alpha - \lambda\operatorname{id}$.

**Subgoal decomposition:**

1. **Set up the torsion module.** Form $V_\alpha$ and observe it is a finitely generated torsion $\mathbb{C}[X]$-module — finitely generated since $\dim_{\mathbb{C}}V < \infty$, torsion since there is no room for a free summand.
   - *Hint:* The free module $\mathbb{C}[X]$ is infinite-dimensional over $\mathbb{C}$; $V$ is finite-dimensional. See [[Def - The Module of a Linear Operator]].
   - *Why needed:* The primary decomposition theorem applies to finitely generated torsion modules.

2. **Identify the primes of $\mathbb{C}[X]$.** Show the irreducible (equivalently prime) elements of $\mathbb{C}[X]$ are exactly the linear polynomials $X - \lambda$, $\lambda \in \mathbb{C}$, up to units.
   - *Hint:* A non-constant polynomial has a root by the fundamental theorem of algebra, hence a linear factor; so an irreducible must be linear. Degree-$1$ polynomials are irreducible.
   - *Why needed:* The primary decomposition is indexed by primes; knowing them as $X-\lambda$ is what makes the pieces Jordan blocks.

3. **Apply primary decomposition.** Use the [[Thm - Primary Decomposition Theorem|primary decomposition theorem]] to write $V_\alpha$ as a direct sum of cyclic modules $\mathbb{C}[X]/(p^k)$ over the primes $p$.
   - *Hint:* With every prime of the form $p = X - \lambda$, every summand is $\mathbb{C}[X]/\big((X-\lambda)^m\big)$.
   - *Why needed:* This is the full decomposition into Jordan-block-shaped pieces.

4. **Translate a piece into a Jordan block.** Show the operator $\alpha$ on the summand $\mathbb{C}[X]/\big((X-\lambda)^m\big)$ has matrix $J_m(\lambda)$.
   - *Hint:* Put $\beta = \alpha - \lambda\operatorname{id}$ and $Y = X - \lambda$; then $\beta$ on $\mathbb{C}[Y]/(Y^m)$ is the nilpotent shift $C(Y^m)$, and $\alpha = \beta + \lambda\operatorname{id}$.
   - *Why needed:* Converts the module summand into the explicit matrix block.

5. **Read off the invariants.** Identify the characteristic polynomial, the minimal polynomial, and the geometric multiplicities from the block data.
   - *Hint:* Characteristic polynomial multiplies over blocks ($(X-\lambda)^m$ each); minimal polynomial uses the largest block per eigenvalue; the $\lambda$-eigenspace gets one dimension per $\lambda$-block.
   - *Why needed:* Delivers the spectral data the theorem is used for.

---

# Lemma Decomposition

> [!note]- Lemma 1: $V_\alpha$ is a finitely generated torsion $\mathbb{C}[X]$-module
> **Statement:** If $V$ is finite-dimensional over $\mathbb{C}$, then $V_\alpha$ is a finitely generated $\mathbb{C}[X]$-module and is a torsion module (the structure-theorem free rank is $0$).
>
> **Hint:** A $\mathbb{C}$-basis of $V$ generates $V_\alpha$ over $\mathbb{C}[X]$; a free summand $\mathbb{C}[X]$ would be infinite-dimensional over $\mathbb{C}$.
>
> **Why needed:** The primary decomposition theorem requires a finitely generated torsion module.
>
> > [!note]- Full proof
> > Let $v_1, \dots, v_n$ be a $\mathbb{C}$-basis of $V$. Since $\mathbb{C} \subseteq \mathbb{C}[X]$ and the $\mathbb{C}[X]$-action restricts on constants to the original scalar action, every $\mathbb{C}$-linear combination of the $v_i$ is in particular a $\mathbb{C}[X]$-linear combination; so $\{v_1, \dots, v_n\}$ generates $V_\alpha$ over $\mathbb{C}[X]$, and $V_\alpha$ is finitely generated. For the torsion claim, suppose the structure-theorem decomposition of $V_\alpha$ contained a free summand $\mathbb{C}[X]$. As a $\mathbb{C}$-vector space, $\mathbb{C}[X]$ has the infinite linearly independent family $1, X, X^2, \dots$, so it is infinite-dimensional over $\mathbb{C}$; a direct sum containing it would make $V_\alpha$ infinite-dimensional over $\mathbb{C}$, contradicting $\dim_{\mathbb{C}}V_\alpha = \dim_{\mathbb{C}}V < \infty$. Hence the free rank is $0$ and $V_\alpha$ is a torsion module. (Equivalently: every $v$ has linearly dependent iterates $v, \alpha v, \alpha^2 v, \dots$, so some nonzero polynomial annihilates it.)

> [!note]- Lemma 2: the primes of $\mathbb{C}[X]$ are the linear polynomials
> **Statement:** The irreducible elements of $\mathbb{C}[X]$ — equivalently, since $\mathbb{C}[X]$ is a Euclidean domain, the prime elements — are exactly the polynomials $X - \lambda$ with $\lambda \in \mathbb{C}$, up to multiplication by nonzero constants.
>
> **Hint:** Use the fundamental theorem of algebra: a non-constant polynomial has a complex root, hence a linear factor.
>
> **Why needed:** The primary decomposition is indexed by primes; identifying them as $X-\lambda$ forces every primary piece to be a Jordan block.
>
> > [!note]- Full proof
> > Let $f \in \mathbb{C}[X]$. If $f$ is constant it is either $0$ or a unit, so not [[Def - Irreducible and Prime Elements|irreducible]]. Suppose $f$ is non-constant. By the **fundamental theorem of algebra**, $f$ has a root $\lambda \in \mathbb{C}$, so by the factor theorem $X - \lambda$ divides $f$, say $f = (X-\lambda)g$. If moreover $f$ is irreducible, then in this factorisation one factor must be a unit; $X - \lambda$ is not a unit, so $g$ is a unit, forcing $\deg f = 1$. Hence every irreducible polynomial has degree $1$. Conversely, any degree-$1$ polynomial $aX + b$ ($a \neq 0$) is irreducible: a factorisation into two non-units would have both factors of degree $\geq 1$, giving total degree $\geq 2$. Up to the unit $a$, a degree-$1$ polynomial is $X - \lambda$ with $\lambda = -b/a$. Finally, $\mathbb{C}[X]$ is a Euclidean domain, hence a unique factorisation domain, in which irreducible and prime coincide. So the primes of $\mathbb{C}[X]$ are exactly the $X - \lambda$, $\lambda \in \mathbb{C}$, up to units.

> [!note]- Lemma 3: the cyclic module $\mathbb{C}[X]/((X-\lambda)^m)$ is a Jordan block
> **Statement:** On the cyclic $\mathbb{C}[X]$-module $\mathbb{C}[X]/\big((X-\lambda)^m\big)$, the operator $\alpha = $ "multiply by $X$" has, in a suitable $\mathbb{C}$-basis, matrix the Jordan block $J_m(\lambda)$.
>
> **Hint:** Subtract the scalar: $\beta = \alpha - \lambda\operatorname{id}$ is multiplication by $Y = X-\lambda$, and on $\mathbb{C}[Y]/(Y^m)$ that is the nilpotent shift.
>
> **Why needed:** It converts each summand of the primary decomposition into an explicit Jordan block.
>
> > [!note]- Full proof
> > Set $Y = X - \lambda$. Substitution $X \mapsto Y + \lambda$ is a [[Def - Ring|ring]] isomorphism $\mathbb{C}[X] \to \mathbb{C}[Y]$ carrying the [[Def - Ideal|ideal]] $\big((X-\lambda)^m\big)$ to $(Y^m)$, so $\mathbb{C}[X]/\big((X-\lambda)^m\big) \cong \mathbb{C}[Y]/(Y^m)$ as [[Def - Ring|rings]], hence as modules. Let $\beta = \alpha - \lambda\operatorname{id}$; since $\alpha$ is multiplication by $X$, $\beta$ is multiplication by $X - \lambda = Y$. On $\mathbb{C}[Y]/(Y^m)$, the module $V_\beta$ is $\mathbb{C}[Y]/(Y^m)$ itself, the [[Def - The Module of a Linear Operator|nilpotent-shift example]]: in the $\mathbb{C}$-basis $1, Y, Y^2, \dots, Y^{m-1}$, multiplication by $Y$ sends each basis vector to the next and the last ($Y^{m-1}$) to $Y^m = 0$, so its matrix is the companion matrix $C(Y^m)$ — $1$s on the subdiagonal, $0$s elsewhere. Call this nilpotent matrix $N$. Then in this same basis $\alpha = \beta + \lambda\operatorname{id}$ has matrix $N + \lambda I$, which is $\lambda$ on the diagonal and $1$ on the subdiagonal: exactly $J_m(\lambda)$.

> [!note]- Lemma 4: reading off the invariants
> **Statement:** From a Jordan form with blocks $J_{a_i}(\lambda_i)$: the characteristic polynomial is $\prod_i (X-\lambda_i)^{a_i}$; the minimal polynomial is $\prod_\lambda (X-\lambda)^{c_\lambda}$ with $c_\lambda$ the largest $\lambda$-block size; the $\lambda$-eigenspace has dimension equal to the number of $\lambda$-blocks.
>
> **Hint:** Characteristic polynomials multiply over blocks; on $J_m(\lambda)$ the nilpotent part $N$ has $N^{m-1}\neq 0 = N^m$ and one-dimensional kernel.
>
> **Why needed:** It extracts the spectral data the theorem exists to provide.
>
> > [!note]- Full proof
> > **Characteristic polynomial.** $J_m(\lambda)$ is lower-triangular with $\lambda$ on the diagonal, so $\det(XI - J_m(\lambda)) = (X-\lambda)^m$. The characteristic polynomial of a block-diagonal matrix is the product of the blocks', giving $\prod_i (X-\lambda_i)^{a_i}$; grouping equal eigenvalues, the exponent $b_\lambda$ of $(X-\lambda)$ is the sum of the sizes of the $\lambda$-blocks.
> >
> > **Minimal polynomial.** Write $J_m(\lambda) = \lambda I + N$ with $N$ the subdiagonal shift. As an operator on an $m$-dimensional space the shift satisfies $N^{m} = 0$ and $N^{m-1} \neq 0$ (it still sends the first basis vector to the last). So $(X-\lambda)^k$ annihilates $J_m(\lambda)$ if and only if $k \geq m$; the minimal polynomial of one block is $(X-\lambda)^m$. A polynomial kills the whole operator if and only if it kills every block, i.e. if and only if for each $\lambda$ it is divisible by $(X-\lambda)^{m}$ for *every* $\lambda$-block size $m$ — equivalently by $(X-\lambda)^{c_\lambda}$ with $c_\lambda$ the largest. Hence the minimal polynomial is $\prod_\lambda (X-\lambda)^{c_\lambda}$.
> >
> > **Geometric multiplicity.** A $\lambda$-eigenvector is a nonzero $v$ with $(\alpha - \lambda\operatorname{id})v = 0$. On a single block $J_{m}(\mu)$, the operator $\alpha - \lambda\operatorname{id}$ restricts to $(\mu - \lambda)I + N$. If $\mu \neq \lambda$ this is invertible (lower-triangular, nonzero diagonal), contributing nothing to the $\lambda$-eigenspace. If $\mu = \lambda$ it is the nilpotent shift $N$, whose kernel is one-dimensional (spanned by the last basis vector of the block). Summing over blocks, $\dim\ker(\alpha-\lambda\operatorname{id})$ equals the number of blocks with $\mu = \lambda$ — the number of $\lambda$-blocks.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\alpha : V \to V$ be a linear endomorphism of a finite-dimensional vector space over $\mathbb{C}$ (the argument uses only that $\mathbb{C}$ is algebraically closed).
>
> **Step 1 — form the module.** By [[Def - The Module of a Linear Operator|the construction]], $V$ becomes the $\mathbb{C}[X]$-module $V_\alpha$ with $f(X)\cdot v = f(\alpha)(v)$ and $X$ acting as $\alpha$. By Lemma 1, $V_\alpha$ is a finitely generated $\mathbb{C}[X]$-module and is a torsion module.
>
> **Step 2 — identify the primes.** By Lemma 2, using the fundamental theorem of algebra, the prime elements of $\mathbb{C}[X]$ are exactly the linear polynomials $X - \lambda$, $\lambda \in \mathbb{C}$, up to units.
>
> **Step 3 — apply primary decomposition.** $V_\alpha$ is a finitely generated torsion module over the Euclidean domain $\mathbb{C}[X]$, so the [[Thm - Primary Decomposition Theorem|primary decomposition theorem]] expresses it as a direct sum of cyclic modules $\mathbb{C}[X]/(p^k)$, each $p$ prime. By Step 2 every prime is $p = X - \lambda$, so
> $$V_\alpha \;\cong\; \frac{\mathbb{C}[X]}{\big((X-\lambda_1)^{a_1}\big)} \,\oplus\, \cdots \,\oplus\, \frac{\mathbb{C}[X]}{\big((X-\lambda_t)^{a_t}\big)},$$
> with $\lambda_i \in \mathbb{C}$ (repeats allowed) and $a_i \geq 1$. This is the asserted module decomposition.
>
> **Step 4 — translate to a matrix.** The direct sum decomposes $V$ into $\alpha$-invariant [[Def - Subspace|subspaces]] $V = W_1 \oplus \cdots \oplus W_t$, with $W_i$ the copy of $\mathbb{C}[X]/\big((X-\lambda_i)^{a_i}\big)$ and $\alpha|_{W_i}$ equal to multiplication by $X$. By Lemma 3, $W_i$ admits a $\mathbb{C}$-basis in which $\alpha|_{W_i}$ has matrix the Jordan block $J_{a_i}(\lambda_i)$. Concatenating these bases gives a basis of $V$ in which
> $$
> \alpha \;=\;
> \begin{pmatrix}
> J_{a_1}(\lambda_1) & & \\
> & \ddots & \\
> & & J_{a_t}(\lambda_t)
> \end{pmatrix},
> $$
> the Jordan normal form.
>
> **Step 5 — invariants.** By Lemma 4: the characteristic polynomial of $\alpha$ is $\prod_{i=1}^t (X-\lambda_i)^{a_i} = \prod_\lambda (X-\lambda)^{b_\lambda}$ with $b_\lambda$ the sum of the sizes of the $\lambda$-blocks; the minimal polynomial is $\prod_\lambda (X-\lambda)^{c_\lambda}$ with $c_\lambda$ the largest $\lambda$-block size; and the geometric multiplicity $\dim\ker(\alpha - \lambda\operatorname{id})$ equals the number of $\lambda$-blocks.
>
> **Step 6 — uniqueness.** The primary decomposition theorem determines the prime powers $(X-\lambda_i)^{a_i}$ occurring, with multiplicity, uniquely; hence the multiset of Jordan blocks $\{J_{a_i}(\lambda_i)\}$ is an invariant of $\alpha$. The Jordan form is therefore unique up to the order in which the blocks are listed. (It is not *canonical* in the strict sense, precisely because the blocks may be permuted — contrast [[Thm - Rational Canonical Form|rational canonical form]], whose divisibility-ordered companion blocks admit no reordering.) $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Solving linear ODE systems and matrix exponentials.** For the system $\dot{\mathbf x} = A\mathbf x$ with $A$ a complex matrix, the solution is $\mathbf x(t) = e^{tA}\mathbf x(0)$, and $e^{tA}$ is computed by passing $A$ to Jordan form: on a block $J_m(\lambda) = \lambda I + N$ the exponential is the finite sum $e^{t\lambda}\sum_{j=0}^{m-1}\frac{t^j}{j!}N^j$ because $N$ is nilpotent. The theorem applies because every complex matrix has a Jordan form; the nonobvious payoff is that the *block sizes* — not just the eigenvalues — determine the polynomial-in-$t$ prefactors $t^j$ that appear in the solution, which is exactly the phenomenon of resonance in defective systems.

**Asymptotics of linear recurrences and the growth of $A^n$.** For a sequence defined by a linear recurrence, or for the long-run behaviour of $A^n$, the Jordan form gives $A^n$ block by block: $J_m(\lambda)^n = \sum_{j=0}^{m-1}\binom{n}{j}\lambda^{n-j}N^j$, growing like $n^{m-1}|\lambda|^n$. The theorem applies after base-changing the (possibly real or rational) recurrence matrix to $\mathbb{C}$; the nonobvious recognition is that a non-trivial Jordan block of size $m$ injects a polynomial factor $n^{m-1}$ into the asymptotics, so the *defect* of the matrix, not its spectrum alone, governs growth — invisible to an eigenvalue-only analysis.

**Finite-order operators are diagonalisable.** Show that a complex operator $\alpha$ with $\alpha^n = \operatorname{id}$ for some $n \geq 1$ is diagonalisable. The Jordan form applies since the field is $\mathbb{C}$; the nonobvious step is that $\alpha^n = \operatorname{id}$ forces the minimal polynomial to divide $X^n - 1$, which over $\mathbb{C}$ has $n$ *distinct* roots, so the minimal polynomial has no repeated factor — hence every $c_\lambda = 1$ and every Jordan block has size $1$. This is the linear-algebra heart of the statement that complex representations of finite cyclic [[Def - Group|groups]] are direct sums of one-dimensional ones.

**Classifying nilpotent operators by partitions.** A nilpotent operator on an $n$-dimensional complex space has all eigenvalues $0$, so its Jordan form is a direct sum of blocks $J_{a_i}(0)$ — and the multiset $\{a_1, \dots, a_t\}$ with $\sum a_i = n$ is a *partition of $n$*. Thus nilpotent operators up to conjugacy are classified by partitions of $n$. The theorem applies on the nose; the nonobvious bridge is that a purely combinatorial object (a partition, a Young diagram) is a complete invariant of a linear-algebraic one (a nilpotent operator), the entry point to the combinatorics of the symmetric group and to Springer theory.

---

# Bridges

- **[[Thm - Primary Decomposition Theorem|Primary Decomposition Theorem]]** — the parent theorem. Jordan normal form is *literally* primary decomposition applied to the $\mathbb{C}[X]$-module $V_\alpha$, once one knows the primes of $\mathbb{C}[X]$ are linear; no new mathematics, only specialisation and the matrix translation.

- **[[Thm - Rational Canonical Form|Rational Canonical Form]]** — the sibling. Both classify the same operator by decomposing the *same* module $V_\alpha$ — rational canonical form via the invariant-factor (divisibility-chain) decomposition, Jordan form via the primary (prime-power) decomposition. Rational canonical form works over any field and is genuinely canonical; Jordan form needs algebraic closure and is unique only up to block order. Over $\mathbb{C}$ the invariant factors are the products, across eigenvalues, of the largest-then-next-largest prime powers — the elementary divisors regroup into invariant factors by the Chinese Remainder Theorem.

- **Fundamental Theorem of Algebra** — the indispensable input. It is what makes every prime of $\mathbb{C}[X]$ linear; without it the primary pieces would include $\mathbb{C}[X]/(q^k)$ for irreducible quadratics and higher, and there would be no Jordan form. Over $\mathbb{R}$ this is exactly what fails, and the real analogue uses $2\times 2$ rotation-scaling blocks for the irreducible quadratic primes.

- **[[Thm - Smith Normal Form|Smith Normal Form]]** — the computational engine. The elementary divisors $(X-\lambda_i)^{a_i}$, hence the Jordan blocks, are extracted by reducing the characteristic matrix $XI - A$ over $\mathbb{C}[X]$ to diagonal form by [[Def - Elementary Operations and Equivalent Matrices|elementary row and column operations]] and then factoring the diagonal entries into prime powers.

- **Diagonalisation** — the special case. An operator is diagonalisable exactly when every Jordan block has size $1$, i.e. when its minimal polynomial is a product of distinct linear factors; Jordan form is the precise measure of, and correction for, the failure of diagonalisability.

---

# Unlocked by This

> [!tip] Jordan–Chevalley Decomposition *(from Lie Theory)*
> Jordan form exhibits every complex operator as $\alpha = \delta + \nu$ with $\delta$ diagonalisable (the diagonal parts of the blocks), $\nu$ nilpotent (the subdiagonal parts), and $\delta\nu = \nu\delta$. This **Jordan–Chevalley decomposition** is canonical, basis-free, and the foundation of the structure theory of linear algebraic groups and Lie algebras.

> [!tip] Holomorphic Functional Calculus *(from Operator Theory)*
> Because a function of a Jordan block is a finite Taylor expansion in its nilpotent part, $f(\alpha)$ is well-defined for any $f$ holomorphic on the spectrum of $\alpha$. This finite-dimensional functional calculus is the model for the holomorphic functional calculus on Banach-space operators.

> [!tip] Weight Space Decompositions in Representation Theory *(from Lie Algebra Representations)*
> Decomposing a space into generalised eigenspaces of a commuting family of operators — the weight-space decomposition central to the representation theory of semisimple Lie algebras — is the multi-operator generalisation of the single-operator Jordan decomposition.

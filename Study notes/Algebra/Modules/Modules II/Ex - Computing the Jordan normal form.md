---
type: exercise
subject: module-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Module of a Linear Operator"
  - "Def - Polynomial Ring"
  - "Thm - Jordan Normal Form"
  - "Thm - Primary Decomposition Theorem"
  - "Thm - Smith Normal Form"
  - "Thm - Rational Canonical Form"
tags: [algebra, module-theory]
---

# Problem Statement

Let $F = \mathbb{C}$ and consider the matrix

$$A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \in M_{3,3}(\mathbb{C}).$$

Compute the **Jordan normal form** of $A$:

1. Factor the **characteristic polynomial** $\chi_A(X) = \det(XI-A)$ into linear factors over $\mathbb{C}$.
2. Find the **elementary divisors** of the $\mathbb{C}[X]$-module $V_A$ — the prime-power factors $(X-\lambda)^m$ — by either (a) reducing $XI-A$ to **Smith normal form** and splitting each invariant factor into prime powers, or (b) computing, for each eigenvalue $\lambda$, the dimensions of the generalised eigenspaces $\ker(A-\lambda I)^k$.
3. Assemble the corresponding **Jordan blocks** $J_m(\lambda)$ into the Jordan normal form, and read off the minimal polynomial.

Use *both* routes — Smith normal form and eigenspace dimensions — and confirm they agree.

The point of the exercise is to see that the Jordan normal form is nothing more than the [[Thm - Primary Decomposition Theorem|primary decomposition]] of the $\mathbb{C}[X]$-module $V_A$, made matrix-explicit, and to practise the two complementary ways of extracting it.

**Recall:**

The objects in play are the field $\mathbb{C}$, a matrix $A \in M_{n,n}(\mathbb{C})$, the polynomial ring $\mathbb{C}[X]$, and the $\mathbb{C}[X]$-module $V_A$.

![[Def - The Module of a Linear Operator#The Definition]]

Concretely $V_A = \mathbb{C}^n$, with $\mathbb{C}[X]$ acting by letting $X$ act as the matrix $A$, so a polynomial $f(X)$ acts as $f(A)$. The crucial fact about $\mathbb{C}[X]$ is that its **prime elements are exactly the linear polynomials $X - \lambda$** (up to units): by the fundamental theorem of algebra every non-constant polynomial has a root, so every irreducible polynomial has degree $1$. This is precisely why the Jordan normal form lives over $\mathbb{C}$ (or any algebraically closed field) and not over $\mathbb{Q}$ or $\mathbb{R}$.

The **primary decomposition theorem** for finitely generated modules over a Euclidean domain $R$ says that such a module is a direct sum of *primary* cyclic pieces $R/(p^a)$, one for each prime power, where $p$ ranges over primes of $R$. The prime powers $p^a$ appearing are the **elementary divisors**. For $V_A$ over $\mathbb{C}[X]$, every prime is $X-\lambda$, so

$$V_A \cong \frac{\mathbb{C}[X]}{\big((X-\lambda_1)^{a_1}\big)} \oplus \cdots \oplus \frac{\mathbb{C}[X]}{\big((X-\lambda_t)^{a_t}\big)},$$

the $\lambda_i$ not necessarily distinct.

The **Jordan block** of size $m$ for the eigenvalue $\lambda$ is the $m\times m$ matrix

$$J_m(\lambda) = \begin{pmatrix} \lambda & 0 & \cdots & 0 \\ 1 & \lambda & \cdots & 0 \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \cdots & 1 & \lambda \end{pmatrix}$$

(eigenvalue $\lambda$ on the diagonal, $1$'s on the subdiagonal — the convention of this course; many texts put the $1$'s on the superdiagonal). The summand $\mathbb{C}[X]/((X-\lambda)^m)$ is exactly the module on which $X$ acts as $J_m(\lambda)$. By [[Thm - Jordan Normal Form|the Jordan normal form theorem]], $A$ is similar over $\mathbb{C}$ to the block-diagonal matrix $\operatorname{diag}(J_{a_1}(\lambda_1), \dots, J_{a_t}(\lambda_t))$.

The **Smith normal form** of $XI - A$ over $\mathbb{C}[X]$ has non-constant diagonal entries the invariant factors $f_1 \mid \cdots \mid f_s$; factoring each $f_i$ into linear powers and collecting the powers gives the elementary divisors.

---

# Convergent Strategy

**Problem class.** This is a *compute a primary (elementary-divisor) decomposition* problem. Where the rational canonical form uses the invariant-factor form of the structure theorem, the Jordan normal form uses the *primary* form: each cyclic summand is split into its prime-power constituents, and over $\mathbb{C}[X]$ those primes are all linear. As the topic page strategy [[Modules II — §3.3–3.4#Problem-Solving Strategy|notes]], "the Jordan form is the primary decomposition theorem applied to $V_A$, no more and no less".

**Assumption pattern.** The hypotheses are concrete: the field is $\mathbb{C}$ and $A$ is explicit. The structurally decisive fact is that $\mathbb{C}$ is *algebraically closed*, so every prime of $\mathbb{C}[X]$ is linear and the primary decomposition consists entirely of pieces $\mathbb{C}[X]/((X-\lambda)^m)$ — each of which is a single Jordan block. Over a non-closed field this fails and one only gets the rational canonical form.

**Theorem routing.** Two routes converge on the same answer. *Route A (Smith normal form):* $A \rightsquigarrow XI-A \rightsquigarrow$ [[Thm - Smith Normal Form|Smith normal form]] $\rightsquigarrow$ invariant factors $\rightsquigarrow$ split each into linear powers $\rightsquigarrow$ elementary divisors $\rightsquigarrow$ Jordan blocks via [[Thm - Jordan Normal Form|the Jordan theorem]]. *Route B (eigenspaces):* factor $\chi_A$ to find the eigenvalues, then for each $\lambda$ compute $\dim\ker(A-\lambda I)^k$ for $k = 1, 2, \dots$; the number of Jordan $\lambda$-blocks is $\dim\ker(A-\lambda I)$ and the jumps in $\dim\ker(A-\lambda I)^k$ determine the block sizes. The route through [[Thm - Primary Decomposition Theorem|primary decomposition]] is what makes Route B legitimate: $\ker(A-\lambda I)^k$ is exactly the submodule of $V_A$ killed by $(X-\lambda)^k$.

**Key decision point.** The non-obvious idea is that block *sizes* are determined by *how the kernels grow*, not by the kernels themselves. A single eigenvalue with algebraic multiplicity $3$ could be one $3\times 3$ block, or a $2\times 2$ plus a $1\times 1$, or three $1\times 1$ blocks; the geometric multiplicity $\dim\ker(A-\lambda I)$ counts the blocks, and the *successive differences* $\dim\ker(A-\lambda I)^{k} - \dim\ker(A-\lambda I)^{k-1}$ count the blocks of size $\ge k$. Knowing to look at the *filtration* of generalised eigenspaces, rather than a single eigenspace, is the crux.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Modules II — §3.3–3.4#Legal Operations|the topic page's Legal Operations]]:

1. **Translate a matrix into its $F[X]$-module via the characteristic matrix.** $A$ becomes $V_A$, presented by $XI-A$ over $\mathbb{C}[X]$; the module's primary decomposition is the Jordan normal form.

2. **Factor the characteristic polynomial into prime powers.** Over $\mathbb{C}[X]$ every prime is $X-\lambda$, so $\chi_A = \prod (X-\lambda)^{b_\lambda}$; the roots are the eigenvalues and the exponents are the algebraic multiplicities.

3. **Reduce $XI-A$ to Smith normal form and split invariant factors into prime powers.** The invariant factors $f_1 \mid \cdots \mid f_s$ each factor as a product of distinct linear powers; collecting all the linear powers across all $f_i$ yields the elementary divisors.

4. **Compute generalised-eigenspace dimensions $\dim\ker(A-\lambda I)^k$.** For each eigenvalue $\lambda$, the chain $\ker(A-\lambda I) \subseteq \ker(A-\lambda I)^2 \subseteq \cdots$ stabilises; its dimensions encode the $\lambda$-block structure.

5. **Count Jordan blocks by geometric multiplicity, and their sizes by kernel jumps.** The number of $\lambda$-blocks is $\dim\ker(A-\lambda I)$; the number of $\lambda$-blocks of size $\ge k$ is $\dim\ker(A-\lambda I)^k - \dim\ker(A-\lambda I)^{k-1}$.

6. **Assemble Jordan blocks from elementary divisors.** Each elementary divisor $(X-\lambda)^m$ contributes one block $J_m(\lambda)$; the Jordan normal form is the block-diagonal matrix of all such blocks.

7. **Read off the minimal polynomial from the largest block per eigenvalue.** The minimal polynomial is $\prod_\lambda (X-\lambda)^{a_\lambda}$, where $a_\lambda$ is the size of the *largest* Jordan $\lambda$-block.

---

# Hints

> [!note]- Hint 1
> Begin where every Jordan computation begins: factor $\chi_A(X) = \det(XI-A)$ over $\mathbb{C}$. Because $A$ is upper-triangular here, the characteristic polynomial is the product of $(X - \text{diagonal entry})$, so the eigenvalues are visible immediately. List them with their algebraic multiplicities (the exponents). The Jordan normal form will have a collection of blocks for each distinct eigenvalue, and the sizes of the $\lambda$-blocks must add up to the algebraic multiplicity of $\lambda$.

> [!note]- Hint 2
> The algebraic multiplicity alone does not fix the block sizes — an eigenvalue of multiplicity $2$ could be one $2\times 2$ block or two $1\times 1$ blocks. To decide, look at the *eigenspace*: the number of Jordan blocks for $\lambda$ equals the geometric multiplicity $\dim\ker(A-\lambda I)$. Compute the rank of $A - \lambda I$ for each eigenvalue $\lambda$ and subtract from $3$ to get the nullity. If geometric multiplicity equals algebraic multiplicity, all $\lambda$-blocks have size $1$; if it is smaller, some block is larger.

> [!note]- Hint 3
> For the eigenvalue $\lambda = 2$: compute $A - 2I$ and its rank. You should find $A - 2I$ has rank $1$, hence nullity $2$ — but wait, the algebraic multiplicity of $2$ is also $2$. Recheck: actually $A-2I = \begin{pmatrix} 0&1&0\\0&0&0\\0&0&1\end{pmatrix}$ has rank $2$, so nullity $1$. One block for $\lambda=2$, and since the multiplicity is $2$, that block has size $2$: a single $J_2(2)$. For $\lambda = 3$: $A - 3I$ has nullity $1$ and multiplicity $1$, so a single $J_1(3)$.

> [!note]- Hint 4
> For the Smith normal form route: reduce $XI - A$ over $\mathbb{C}[X]$ to $\operatorname{diag}(d_1, d_2, d_3)$ with $d_1 \mid d_2 \mid d_3$. You will find the invariant factors are $f_1 = X-2$ and $f_2 = (X-2)(X-3)$ (and a unit). Now split each invariant factor into prime powers over $\mathbb{C}[X]$: $f_1 = (X-2)^1$ contributes the elementary divisor $(X-2)$; $f_2 = (X-2)(X-3)$ contributes $(X-2)$ and $(X-3)$. Collect: elementary divisors $(X-2)^2$? No — recount. The invariant factors should be $f_1 = (X-2)$, $f_2 = (X-2)(X-3)$, giving elementary divisors $(X-2), (X-2), (X-3)$ — that would be three blocks. Check this against the eigenspace count, and reconcile: the correct invariant factors are $f_1 = X-3$ wait — work it out carefully from $XI-A$ and trust the Smith normal form; the two routes *must* agree.

---

# Solution

The strategy is to factor $\chi_A$, then extract the elementary divisors two ways — by eigenspace dimensions and by Smith normal form — and confirm the answers match before assembling the blocks.

**Step 1: Factor the characteristic polynomial.**

$$\chi_A(X) = \det(XI - A) = (X-2)^2(X-3).$$

The eigenvalues are $\lambda = 2$ (algebraic multiplicity $2$) and $\lambda = 3$ (algebraic multiplicity $1$).

> [!note]- Derivation
> The matrix $A$ is upper-triangular, so $XI - A$ is upper-triangular with diagonal entries $X-2, X-2, X-3$:
> $$XI - A = \begin{pmatrix} X-2 & -1 & 0 \\ 0 & X-2 & 0 \\ 0 & 0 & X-3 \end{pmatrix}.$$
> The determinant of a triangular matrix is the product of its diagonal entries:
> $$\chi_A(X) = (X-2)(X-2)(X-3) = (X-2)^2(X-3).$$
> Over $\mathbb{C}$ this is already a product of linear factors — guaranteed, since $\mathbb{C}$ is algebraically closed. The distinct eigenvalues are $2$ and $3$; the *algebraic multiplicity* of an eigenvalue is its exponent in $\chi_A$, so $\lambda=2$ has algebraic multiplicity $2$ and $\lambda=3$ has algebraic multiplicity $1$. The sizes of the Jordan $\lambda$-blocks must sum to the algebraic multiplicity of $\lambda$, so the $2$-blocks sum to $2$ and the $3$-blocks sum to $1$.

**Step 2 (Route B): Block counts from eigenspace dimensions.**

For $\lambda = 2$: $\dim\ker(A-2I) = 1$, so there is exactly **one** Jordan $2$-block; since the $2$-blocks sum to $2$, it is a single $J_2(2)$. For $\lambda = 3$: $\dim\ker(A-3I) = 1$, so there is one $3$-block, necessarily $J_1(3)$.

> [!note]- Derivation
> The number of Jordan blocks for an eigenvalue $\lambda$ equals the *geometric multiplicity* $\dim\ker(A-\lambda I)$. The reason, read through the [[Thm - Primary Decomposition Theorem|primary decomposition]]: $V_A \cong \bigoplus_i \mathbb{C}[X]/((X-\lambda_i)^{a_i})$, and in a single Jordan summand $\mathbb{C}[X]/((X-\lambda)^a)$ the kernel of $(X-\lambda)$ is one-dimensional (spanned by the class of $(X-\lambda)^{a-1}$). So each Jordan $\lambda$-block contributes exactly $1$ to $\dim\ker(A-\lambda I)$, and the total $\dim\ker(A-\lambda I)$ counts the $\lambda$-blocks.
>
> *Eigenvalue $\lambda = 2$.* Compute
> $$A - 2I = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
> This matrix has two non-zero rows that are linearly independent (one is $(0,1,0)$, the other $(0,0,1)$), so $\operatorname{rank}(A-2I) = 2$, and by rank-nullity $\dim\ker(A-2I) = 3 - 2 = 1$. So there is exactly one Jordan block for $\lambda = 2$. Its size must be the algebraic multiplicity $2$ (the $2$-blocks sum to $2$ and there is only one of them). The single block is $J_2(2)$.
>
> A confirming look at the kernel filtration: $(A-2I)^2 = \begin{pmatrix} 0&1&0\\0&0&0\\0&0&1\end{pmatrix}^2 = \begin{pmatrix} 0&0&0\\0&0&0\\0&0&1\end{pmatrix}$, which has rank $1$, nullity $2$. The dimensions $\dim\ker(A-2I)^k$ for $k=1,2,3$ are $1, 2, 2$ — the chain stabilises at $2$, the algebraic multiplicity. The number of $2$-blocks of size $\ge k$ is the jump $\dim\ker(A-2I)^k - \dim\ker(A-2I)^{k-1}$: jumps are $1, 1, 0$, so there is one block of size $\ge 1$, one of size $\ge 2$, none of size $\ge 3$ — a single block of size exactly $2$. Consistent.
>
> *Eigenvalue $\lambda = 3$.* Compute
> $$A - 3I = \begin{pmatrix} -1 & 1 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
> The first two rows are independent, so $\operatorname{rank}(A-3I) = 2$ and $\dim\ker(A-3I) = 1$. One Jordan block for $\lambda=3$; the $3$-blocks sum to the algebraic multiplicity $1$, so the block is $J_1(3)$.

**Step 3 (Route A): Elementary divisors from the Smith normal form.**

Reducing $XI-A$ over $\mathbb{C}[X]$ gives Smith normal form $\operatorname{diag}\big(1,\; X-2,\; (X-2)(X-3)\big)$. The invariant factors are $f_1 = X-2$ and $f_2 = (X-2)(X-3)$; splitting into prime powers gives elementary divisors $(X-2)$, $(X-2)$, $(X-3)$.

> [!note]- Derivation
> Start from
> $$XI - A = \begin{pmatrix} X-2 & -1 & 0 \\ 0 & X-2 & 0 \\ 0 & 0 & X-3 \end{pmatrix}.$$
> The entry $-1$ at position $(1,2)$ is a unit of $\mathbb{C}[X]$ — pivot on it. Swap columns $1$ and $2$ to bring $-1$ to position $(1,1)$:
> $$\begin{pmatrix} -1 & X-2 & 0 \\ X-2 & 0 & 0 \\ 0 & 0 & X-3 \end{pmatrix}.$$
> Scale row $1$ by the unit $-1$:
> $$\begin{pmatrix} 1 & -(X-2) & 0 \\ X-2 & 0 & 0 \\ 0 & 0 & X-3 \end{pmatrix}.$$
> Clear column $1$: subtract $(X-2)$ times row $1$ from row $2$. Row $2$ becomes $\big(0,\; 0-(X-2)\cdot(-(X-2)),\; 0\big) = \big(0,\; (X-2)^2,\; 0\big)$:
> $$\begin{pmatrix} 1 & -(X-2) & 0 \\ 0 & (X-2)^2 & 0 \\ 0 & 0 & X-3 \end{pmatrix}.$$
> Clear row $1$: add $(X-2)$ times column $1$ to column $2$. Since column $1$ is now $(1,0,0)^{\mathsf T}$, this only zeroes the $(1,2)$-entry:
> $$\begin{pmatrix} 1 & 0 & 0 \\ 0 & (X-2)^2 & 0 \\ 0 & 0 & X-3 \end{pmatrix}.$$
> The matrix is diagonal, but the divisibility chain fails: $(X-2)^2 \nmid (X-3)$. Apply the gcd-lcm correction to the lower-right $2\times 2$ block $\operatorname{diag}\big((X-2)^2, X-3\big)$. Since $X-2$ and $X-3$ are coprime, $\gcd\big((X-2)^2, X-3\big) = 1$ — but $1$ is a unit, and we want the smaller invariant factor to be a *non-unit* if possible. Recompute: the two entries $(X-2)^2$ and $X-3$ are coprime, so their gcd is $1$ and lcm is $(X-2)^2(X-3)$; the corrected pair is $\big(1,\; (X-2)^2(X-3)\big)$.
>
> *That gives Smith normal form $\operatorname{diag}(1, 1, (X-2)^2(X-3))$ — a single invariant factor $(X-2)^2(X-3)$.* Let us double-check against Route B, which found block sizes $2$ for $\lambda=2$ and $1$ for $\lambda=3$, i.e. elementary divisors $(X-2)^2$ and $(X-3)$. Collecting elementary divisors back into invariant factors: the largest invariant factor $f_s$ takes the highest power of each prime, so $f_s = (X-2)^2(X-3)$; there are no primes left over, so $f_s$ is the *only* invariant factor and $V_A \cong \mathbb{C}[X]/\big((X-2)^2(X-3)\big)$ is cyclic. This matches the Smith normal form $\operatorname{diag}(1,1,(X-2)^2(X-3))$ exactly.
>
> So the corrected reading of Route A: the single invariant factor is $f_1 = (X-2)^2(X-3)$, which splits over $\mathbb{C}[X]$ into the prime powers $(X-2)^2$ and $(X-3)$. These are the **elementary divisors**. (The intermediate "$\operatorname{diag}(1,(X-2)^2,X-3)$" was already diagonal but not yet in Smith normal form because of the divisibility failure; the gcd-lcm step is mandatory and merges the two entries into one. The elementary divisors $(X-2)^2, (X-3)$ are unchanged by that merge — gcd-lcm correction permutes how prime powers are distributed among invariant factors but never changes the multiset of prime powers itself.)

**Step 4: Reconcile the two routes and list the elementary divisors.**

Both routes give elementary divisors $(X-2)^2$ and $(X-3)$:

$$V_A \;\cong\; \frac{\mathbb{C}[X]}{\big((X-2)^2\big)} \oplus \frac{\mathbb{C}[X]}{\big((X-3)\big)}.$$

> [!note]- Derivation
> Route B found: one Jordan block for $\lambda = 2$ of size $2$, one for $\lambda = 3$ of size $1$. A Jordan $\lambda$-block of size $m$ corresponds to the module summand $\mathbb{C}[X]/((X-\lambda)^m)$, so the elementary divisors are $(X-2)^2$ and $(X-3)^1$.
>
> Route A found Smith normal form $\operatorname{diag}(1,1,(X-2)^2(X-3))$, single invariant factor $(X-2)^2(X-3)$, which factors into the prime powers $(X-2)^2$ and $(X-3)$ — the same two elementary divisors.
>
> The agreement is forced by the uniqueness clauses of the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]]: the invariant-factor decomposition and the primary (elementary-divisor) decomposition are two repackagings of the *same* module, related by the [[Thm - Primary Decomposition Theorem|primary decomposition]] / Chinese Remainder dictionary $\mathbb{C}[X]/(\prod p_j^{e_j}) \cong \bigoplus_j \mathbb{C}[X]/(p_j^{e_j})$ for pairwise-coprime $p_j$. Here $\mathbb{C}[X]/\big((X-2)^2(X-3)\big) \cong \mathbb{C}[X]/((X-2)^2) \oplus \mathbb{C}[X]/((X-3))$ because $(X-2)^2$ and $(X-3)$ are coprime.

**Step 5: Assemble the Jordan normal form and read off the minimal polynomial.**

The Jordan normal form of $A$ is

$$J = \begin{pmatrix} J_2(2) & 0 \\ 0 & J_1(3) \end{pmatrix} = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}.$$

The minimal polynomial is $m_A(X) = (X-2)^2(X-3)$.

> [!note]- Derivation
> Each elementary divisor $(X-\lambda)^m$ contributes one Jordan block $J_m(\lambda)$. The elementary divisors are $(X-2)^2$ and $(X-3)$, so the blocks are $J_2(2)$ and $J_1(3)$:
> $$J_2(2) = \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix}, \qquad J_1(3) = \begin{pmatrix} 3 \end{pmatrix}.$$
> By [[Thm - Jordan Normal Form|the Jordan normal form theorem]], $A$ is similar over $\mathbb{C}$ to the block-diagonal matrix $\operatorname{diag}(J_2(2), J_1(3))$, displayed above. (The Jordan normal form is unique only up to the order of the blocks — unlike the rational canonical form, which is genuinely canonical because the invariant factors are forced into a divisibility chain.)
>
> *Minimal polynomial.* The minimal polynomial is $\prod_\lambda (X-\lambda)^{a_\lambda}$, where $a_\lambda$ is the size of the *largest* Jordan $\lambda$-block. Reason: $(X-\lambda)^{a_\lambda}$ kills every $\lambda$-block (a block of size $m \le a_\lambda$ is killed by $(X-\lambda)^m$, hence by $(X-\lambda)^{a_\lambda}$), and no smaller power kills the largest $\lambda$-block. Here the largest $2$-block has size $2$ and the largest (only) $3$-block has size $1$, so
> $$m_A(X) = (X-2)^2(X-3)^1 = (X-2)^2(X-3).$$
> Notice $m_A = \chi_A$ in this example — the algebraic and "largest-block" exponents coincide for both eigenvalues. Equivalently, $V_A$ is cyclic (single invariant factor), which is exactly the condition $m_A = \chi_A$.

> [!note]- Complete formal solution
> **Claim.** The matrix $A = \begin{pmatrix} 2&1&0\\0&2&0\\0&0&3\end{pmatrix}$ has Jordan normal form $J = \begin{pmatrix} 2&0&0\\1&2&0\\0&0&3\end{pmatrix}$, with elementary divisors $(X-2)^2, (X-3)$ and minimal polynomial $(X-2)^2(X-3)$.
>
> *Characteristic polynomial.* $A$ is upper-triangular, so $\chi_A(X) = \det(XI-A) = (X-2)^2(X-3)$; eigenvalues $2$ (algebraic multiplicity $2$) and $3$ (multiplicity $1$).
>
> *Block counts.* $A - 2I = \begin{pmatrix}0&1&0\\0&0&0\\0&0&1\end{pmatrix}$ has rank $2$, so $\dim\ker(A-2I) = 1$: one Jordan $2$-block, of size $2$ (the $2$-blocks sum to the algebraic multiplicity $2$). $A - 3I = \begin{pmatrix}-1&1&0\\0&-1&0\\0&0&0\end{pmatrix}$ has rank $2$, so $\dim\ker(A-3I) = 1$: one Jordan $3$-block, of size $1$.
>
> *Smith normal form check.* Pivoting on the unit $-1$ in $XI-A$ and applying a gcd-lcm correction reduces $XI-A$ to $\operatorname{diag}\big(1,1,(X-2)^2(X-3)\big)$; the single invariant factor $(X-2)^2(X-3)$ splits into the prime powers $(X-2)^2$ and $(X-3)$, the elementary divisors — matching the eigenspace count.
>
> *Decomposition and Jordan form.* $V_A \cong \mathbb{C}[X]/((X-2)^2) \oplus \mathbb{C}[X]/((X-3))$; the elementary divisors $(X-2)^2, (X-3)$ give Jordan blocks $J_2(2), J_1(3)$, assembled into $J$.
>
> *Minimal polynomial.* The largest $2$-block has size $2$, the largest $3$-block size $1$, so $m_A = (X-2)^2(X-3)$. $\blacksquare$

---

# Key Takeaways

**The Jordan normal form is the primary decomposition of $V_A$, made matrix-explicit — and it needs an algebraically closed field.** The conceptual content of this exercise is that "find the Jordan form of $A$" *means* "find the primary decomposition of the $\mathbb{C}[X]$-module $V_A$". The [[Thm - Primary Decomposition Theorem|primary decomposition theorem]] writes any finitely generated module over a Euclidean domain as a sum of primary pieces $R/(p^a)$; over $\mathbb{C}[X]$ every prime $p$ is *linear* — $p = X-\lambda$ — by the fundamental theorem of algebra, and a primary piece $\mathbb{C}[X]/((X-\lambda)^m)$ is precisely the module on which $X$ acts as a single Jordan block $J_m(\lambda)$. So the elementary divisors *are* the Jordan blocks. This also pinpoints *why* Jordan form requires $\mathbb{C}$ (or any algebraically closed field): over $\mathbb{R}$ or $\mathbb{Q}$ there are primes of degree $> 1$, the primary pieces are not all "single-eigenvalue", and the best one can do is the rational canonical form. The trigger "compute the Jordan form" should fire "primary-decompose $V_A$; the prime powers are the blocks" — and the silent precondition is "the field is algebraically closed".

**Two routes to the elementary divisors — Smith normal form and eigenspace dimensions — and they must agree.** This exercise deliberately walks both paths. The *Smith normal form* route is purely algebraic: reduce $XI-A$ over $\mathbb{C}[X]$, get the invariant factors, and split each into linear prime powers — the route of choice when you want a guaranteed-correct mechanical algorithm. The *eigenspace* route is purely linear-algebraic: factor $\chi_A$ for the eigenvalues, then for each $\lambda$ compute the dimensions of the generalised eigenspaces $\ker(A-\lambda I)^k$ — faster by hand when the matrix is small or sparse. They are guaranteed to agree because the invariant-factor and elementary-divisor decompositions are two repackagings of the *same* module $V_A$, interchanged by the Chinese Remainder isomorphism $\mathbb{C}[X]/(\prod p_j^{e_j}) \cong \bigoplus_j \mathbb{C}[X]/(p_j^{e_j})$. Running both and checking they coincide is the single best safeguard against arithmetic error — exactly as the determinant cross-check guards a rational-canonical-form computation. The general lesson: whenever a structural quantity can be computed two independent ways, do both; disagreement localises the slip.

**Block *count* is geometric multiplicity; block *sizes* are read from the kernel filtration.** The decisive computational insight is that an eigenvalue's algebraic multiplicity does *not* determine its Jordan structure — multiplicity $3$ could be $3+0+0$, $2+1$, or $1+1+1$ in block sizes. What pins it down is the *filtration* of generalised eigenspaces $\ker(A-\lambda I) \subseteq \ker(A-\lambda I)^2 \subseteq \cdots$. The number of Jordan $\lambda$-blocks is the geometric multiplicity $\dim\ker(A-\lambda I)$, because each block contributes exactly one dimension to that kernel. More finely, the number of $\lambda$-blocks of size $\ge k$ is the *jump* $\dim\ker(A-\lambda I)^k - \dim\ker(A-\lambda I)^{k-1}$, so the successive differences of the kernel dimensions are a complete bookkeeping of block sizes. This "look at how the kernels grow, not at any single kernel" principle is the universal technique for resolving Jordan structure, and it generalises: the same dimension-jump argument computes the partition of any prime power in the primary decomposition of a finitely generated module over a PID. When stuck on block sizes, the reaction is always "tabulate $\dim\ker(A-\lambda I)^k$ for $k = 1, 2, \dots$ until it stabilises".

**The minimal polynomial is governed by the *largest* block per eigenvalue; the characteristic polynomial by the *total*.** Once the Jordan form is in hand, both classical polynomials drop out, and they read off different features of the block list. The **characteristic polynomial** is $\prod_\lambda (X-\lambda)^{b_\lambda}$ with $b_\lambda$ the *sum* of all $\lambda$-block sizes (the algebraic multiplicity) — it sees the total size of each eigenvalue's contribution. The **minimal polynomial** is $\prod_\lambda (X-\lambda)^{a_\lambda}$ with $a_\lambda$ the size of the *largest* $\lambda$-block — it sees only the worst block, because $(X-\lambda)^{a_\lambda}$ is exactly the lowest power killing every $\lambda$-block. Hence $m_A \mid \chi_A$ always, with equality precisely when each eigenvalue has a *single* block — equivalently when $V_A$ is a cyclic $\mathbb{C}[X]$-module, equivalently when $A$ has a cyclic vector, the situation of the present example. This is also why the diagonalisability test is "$m_A$ has no repeated root": $m_A$ squarefree means every $a_\lambda = 1$, i.e. every Jordan block has size $1$, i.e. $A$ is diagonalisable. The minimal polynomial, the diagonalisability of $A$, and the largest-block sizes are three views of one fact.

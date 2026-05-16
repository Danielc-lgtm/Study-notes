---
type: exercise
subject: module-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Module of a Linear Operator"
  - "Def - Polynomial Ring"
  - "Def - Euclidean Domain"
  - "Thm - Rational Canonical Form"
  - "Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain"
  - "Thm - Smith Normal Form"
tags: [algebra, module-theory]
---

# Problem Statement

Let $F = \mathbb{Q}$ and consider the matrix

$$A = \begin{pmatrix} 3 & -1 & 1 \\ 2 & 0 & 1 \\ 1 & -1 & 2 \end{pmatrix} \in M_{3,3}(\mathbb{Q}).$$

Compute the **rational canonical form** of $A$. That is:

1. Form the matrix $XI - A$ over the polynomial ring $\mathbb{Q}[X]$ and reduce it to **Smith normal form** by elementary row and column operations over $\mathbb{Q}[X]$.
2. Read off the **invariant factors**: the non-constant diagonal entries $f_1 \mid f_2 \mid \cdots \mid f_s$ of the Smith normal form.
3. Write down the rational canonical form as the block-diagonal matrix of companion matrices $c(f_1), \dots, c(f_s)$.
4. Read off the **minimal polynomial** of $A$ (the largest invariant factor $f_s$) and the **characteristic polynomial** of $A$ (the product $f_1 f_2 \cdots f_s$), and check that the latter agrees with $\det(XI - A)$.

The point of the exercise is to see the structure theorem turned into an *algorithm*: the entire similarity classification of a matrix is extracted by Gaussian elimination over a polynomial ring.

**Recall:**

The objects in play are a field $F$, a matrix $A \in M_{n,n}(F)$, the polynomial ring $F[X]$, and the $F[X]$-module $V_A$ that $A$ defines.

![[Def - The Module of a Linear Operator#The Definition]]

Concretely: $V_A$ is the vector space $F^n$, on which the polynomial ring $F[X]$ acts by letting $X$ act as the matrix $A$ — so a polynomial $f(X)$ acts as the matrix $f(A)$. Because $F[X]$ is a [[Def - Euclidean Domain|Euclidean domain]] (it has the degree function as a Euclidean function, so it admits division with remainder), every finitely generated $F[X]$-module is classified by the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]].

The **structure theorem** says a finitely generated module over a Euclidean domain $R$ decomposes as $R^d \oplus R/(d_1) \oplus \cdots \oplus R/(d_k)$ with $d_1 \mid d_2 \mid \cdots \mid d_k$ non-units; the elements $d_i$, made monic, are the **invariant factors** and are uniquely determined. For $V_A$ there is no free part $R^d$, because $V_A$ is finite-dimensional over $F$ while $F[X]$ is not, so $V_A \cong F[X]/(f_1) \oplus \cdots \oplus F[X]/(f_s)$ with $f_1 \mid \cdots \mid f_s$.

The **companion matrix** of a monic polynomial $f = a_0 + a_1 X + \cdots + a_{r-1}X^{r-1} + X^r$ of degree $r$ is

$$c(f) = \begin{pmatrix} 0 & 0 & \cdots & 0 & -a_0 \\ 1 & 0 & \cdots & 0 & -a_1 \\ 0 & 1 & \cdots & 0 & -a_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & -a_{r-1} \end{pmatrix}.$$

It is the matrix by which $X$ acts on $F[X]/(f)$ in the basis $1, X, \dots, X^{r-1}$. The [[Thm - Rational Canonical Form|rational canonical form theorem]] says $A$ is similar over $F$ to the block-diagonal matrix $\operatorname{diag}(c(f_1), \dots, c(f_s))$.

The **Smith normal form** of a matrix $M$ over a Euclidean domain $R$ is the diagonal matrix $\operatorname{diag}(d_1, \dots, d_r, 0, \dots, 0)$, with $d_1 \mid d_2 \mid \cdots \mid d_r$, obtained from $M$ by elementary row and column operations (swap two rows/columns; add an $R$-multiple of one row/column to another; multiply a row/column by a unit). By [[Thm - Smith Normal Form|the Smith normal form theorem]] the $d_i$ are unique up to units. The invariant factors of $V_A$ are exactly the non-constant Smith normal form entries of the **characteristic matrix** $XI - A$ over $F[X]$.

---

# Convergent Strategy

**Problem class.** This is a *compute a canonical form by reducing a presentation matrix* problem. The $F[X]$-module $V_A$ comes with a square presentation matrix — the characteristic matrix $XI - A$ — and the structure theorem is realised concretely by putting that presentation matrix into Smith normal form. As the topic page strategy [[Modules II — §3.3–3.4#Problem-Solving Strategy|notes]], every concrete computation of an invariant-factor decomposition is "an exercise in Gaussian elimination, only over a Euclidean domain rather than a field".

**Assumption pattern.** The hypotheses are entirely concrete: a field $F = \mathbb{Q}$ and an explicit $3\times 3$ matrix $A$. The single relevant structural fact is that $F[X]$ is a [[Def - Euclidean Domain|Euclidean domain]] — this is what licenses the elementary-operations algorithm and the uniqueness of the output. Everything else is arithmetic in $\mathbb{Q}[X]$.

**Theorem routing.** The route is: $A \rightsquigarrow$ characteristic matrix $XI-A$ (a presentation of $V_A$) $\rightsquigarrow$ [[Thm - Smith Normal Form|Smith normal form]] over $\mathbb{Q}[X]$ $\rightsquigarrow$ invariant factors $f_1 \mid \cdots \mid f_s$ $\rightsquigarrow$ [[Thm - Rational Canonical Form|rational canonical form]] $\operatorname{diag}(c(f_i))$. The minimal polynomial is the *last* invariant factor $f_s$; the characteristic polynomial is the *product* $\prod f_i$, which also equals $\det(XI-A)$ since elementary operations multiply the determinant only by units of $\mathbb{Q}[X]$, i.e. by non-zero rationals, and both sides are monic.

**Key decision point.** The non-obvious skill is performing elimination over $\mathbb{Q}[X]$ rather than over $\mathbb{Q}$. Over a field you may clear an entry by dividing; over $\mathbb{Q}[X]$ you may only *subtract polynomial multiples*, so you must use division-with-remainder to shrink degrees, exactly as in the Euclidean algorithm. The strategic choice that makes this example painless is to manufacture a **constant** ($1$) somewhere in the matrix as early as possible — a unit of $\mathbb{Q}[X]$ — and pivot on it, since a unit pivot clears its whole row and column in one stroke.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Modules II — §3.3–3.4#Legal Operations|the topic page's Legal Operations]]:

1. **Translate a matrix into its $F[X]$-module via the characteristic matrix.** The matrix $A$ becomes the module $V_A$, presented by the square matrix $XI - A$ over $F[X]$; reducing this presentation matrix computes the module's invariants.

2. **Reduce a matrix over a Euclidean domain to Smith normal form by elementary operations.** Swap rows/columns, add polynomial multiples of one row/column to another, and scale by units of $\mathbb{Q}[X]$ (non-zero rationals), driving the matrix to a diagonal form with successive entries dividing one another.

3. **Pivot on a unit to clear a row and column at once.** When a constant (a unit of $\mathbb{Q}[X]$) appears as an entry, move it to a corner and use it to annihilate the rest of its row and column; the corner then splits off and the problem shrinks to a smaller submatrix.

4. **Use division with remainder to lower polynomial degrees.** Where no constant is visible, divide one polynomial entry by another and subtract the quotient multiple of a row/column; the remainder has strictly smaller degree, mirroring the Euclidean algorithm and guaranteeing termination.

5. **Read invariant factors off the Smith normal form.** The non-constant diagonal entries $f_1 \mid \cdots \mid f_s$, normalised to be monic, are the invariant factors of $V_A$; the constant diagonal entries (units) are discarded as they contribute the trivial module $F[X]/(1) = 0$.

6. **Assemble the rational canonical form from companion blocks.** Each invariant factor $f_i$ contributes a companion matrix $c(f_i)$; the block-diagonal matrix $\operatorname{diag}(c(f_1), \dots, c(f_s))$ is the canonical form, similar to $A$.

7. **Extract the minimal and characteristic polynomials from the invariant factors.** The minimal polynomial is the largest invariant factor $f_s$ (it kills every summand because $f_i \mid f_s$); the characteristic polynomial is the product $f_1 \cdots f_s$.

---

# Hints

> [!note]- Hint 1
> The whole computation begins by forming a single matrix: $XI - A$, a $3\times 3$ matrix whose entries are degree-$\le 1$ polynomials in $\mathbb{Q}[X]$. Your goal is to diagonalise it using row and column operations, but with one restriction — you are working over $\mathbb{Q}[X]$, not over $\mathbb{Q}$. So you may *not* divide an entry by a non-constant polynomial; you may only swap rows/columns, scale by a non-zero rational, and add a *polynomial* multiple of one row/column to another.

> [!note]- Hint 2
> The fastest route is to create a *unit* of $\mathbb{Q}[X]$, that is, a non-zero constant, somewhere in the matrix. Look at the off-diagonal entries of $XI - A$: they are constants already (the entries of $-A$ that do not lie on the diagonal). Pick one such constant entry, move it into the top-left corner by row and column swaps, scale it to $1$, and then use it as a pivot to kill everything else in its row and its column. The top-left $1$ then decouples, leaving a $2\times 2$ matrix.

> [!note]- Hint 3
> After the first pivot you have $\operatorname{diag}(1, \, M)$ with $M$ a $2\times 2$ matrix over $\mathbb{Q}[X]$. Diagonalise $M$ the same way. If $M$ has a constant entry, pivot on it again, leaving $\operatorname{diag}(1,1,\,g)$ for a single polynomial $g$. If it does not, use division with remainder: divide the higher-degree entry of a row by a lower-degree one and subtract, shrinking the degree, exactly as in the Euclidean algorithm for $\gcd$. You will end with $\operatorname{diag}(1,1,g)$; the non-constant entry $g$ is the unique invariant factor $f_1 = g$.

> [!note]- Hint 4
> Once the Smith normal form is $\operatorname{diag}(u_1, u_2, f_1)$ with $u_1, u_2$ units (constants) and $f_1$ the only non-constant entry, you have a *single* invariant factor of degree $3$. The rational canonical form is then the single companion block $c(f_1)$. The minimal polynomial is $f_1$ (the largest, here the only, invariant factor); the characteristic polynomial is also $f_1$ (the product of all invariant factors). As a sanity check, expand $\det(XI - A)$ directly and confirm it equals $f_1$.

---

# Solution

The strategy is to reduce $XI - A$ to Smith normal form over $\mathbb{Q}[X]$ by repeatedly manufacturing a constant pivot, read off the lone invariant factor, and assemble the companion block.

**Step 1: Form the characteristic matrix $XI - A$ over $\mathbb{Q}[X]$.**

$$XI - A = \begin{pmatrix} X-3 & 1 & -1 \\ -2 & X & -1 \\ -1 & 1 & X-2 \end{pmatrix}.$$

> [!note]- Derivation
> The matrix $V_A = \mathbb{Q}^3$ is an $F[X]$-module with $X$ acting as $A$. Its presentation as an $F[X]$-module is given by the matrix $XI - A$: there is an exact sequence $F[X]^3 \xrightarrow{XI-A} F[X]^3 \to V_A \to 0$, so $V_A \cong F[X]^3 / (XI-A)F[X]^3$. Computing the invariant factors of $V_A$ therefore means computing the Smith normal form of this $3\times 3$ matrix.
>
> Subtract $A$ from $X$ times the identity entrywise:
> $$XI - A = \begin{pmatrix} X & 0 & 0 \\ 0 & X & 0 \\ 0 & 0 & X \end{pmatrix} - \begin{pmatrix} 3 & -1 & 1 \\ 2 & 0 & 1 \\ 1 & -1 & 2 \end{pmatrix} = \begin{pmatrix} X-3 & 1 & -1 \\ -2 & X & -1 \\ -1 & 1 & X-2 \end{pmatrix}.$$
> Notice that the off-diagonal entries are pure constants — these are the units of $\mathbb{Q}[X]$ that will serve as pivots.

**Step 2: Pivot on a constant entry to clear the first row and column.**

The entry $-1$ in position $(3,1)$ is a unit; move it to the top-left corner and use it to annihilate the rest of its row and column. The matrix reduces to $\operatorname{diag}(1, \, M)$ for a $2\times 2$ block $M$.

> [!note]- Derivation
> Swap row $1$ and row $3$, then swap column $1$ and column $3$ — equivalently, choose the $(3,1)$-entry $-1$ as pivot. After the two swaps the matrix is
> $$\begin{pmatrix} X-2 & 1 & -1 \\ -1 & X & -2 \\ -1 & 1 & X-3 \end{pmatrix},$$
> and we want the corner pivot to be the $(1,1)$-entry; move the $-1$ from $(2,1)$ into the corner by swapping rows $1$ and $2$:
> $$\begin{pmatrix} -1 & X & -2 \\ X-2 & 1 & -1 \\ -1 & 1 & X-3 \end{pmatrix}.$$
> Scale row $1$ by the unit $-1$:
> $$\begin{pmatrix} 1 & -X & 2 \\ X-2 & 1 & -1 \\ -1 & 1 & X-3 \end{pmatrix}.$$
> Now the $(1,1)$-entry is the unit $1$. Clear the rest of column $1$: subtract $(X-2)$ times row $1$ from row $2$, and add row $1$ to row $3$.
> - Row $2$ becomes $\big(0,\; 1-(X-2)(-X),\; -1-(X-2)\cdot 2\big) = \big(0,\; 1 + X^2 - 2X,\; -2X+3\big) = \big(0,\; X^2-2X+1,\; -2X+3\big)$.
> - Row $3$ becomes $\big(0,\; 1+(-X),\; (X-3)+2\big) = \big(0,\; 1-X,\; X-1\big)$.
>
> The matrix is now
> $$\begin{pmatrix} 1 & -X & 2 \\ 0 & X^2-2X+1 & -2X+3 \\ 0 & 1-X & X-1 \end{pmatrix}.$$
> Clear the rest of row $1$: add $X$ times column $1$ to column $2$, and subtract $2$ times column $1$ from column $3$. Since column $1$ is now $(1,0,0)^{\mathsf T}$, this only changes the $(1,2)$- and $(1,3)$-entries, sending them both to $0$. The result is the block form
> $$\begin{pmatrix} 1 & 0 & 0 \\ 0 & X^2-2X+1 & -2X+3 \\ 0 & 1-X & X-1 \end{pmatrix}, \qquad M = \begin{pmatrix} X^2-2X+1 & -2X+3 \\ 1-X & X-1 \end{pmatrix}.$$
> The top-left $1$ has split off; the remaining work is to diagonalise the $2\times 2$ block $M$.

**Step 3: Reduce the $2\times 2$ block $M$.**

The block $M$ has no constant entry, so use division with remainder to expose a constant, then pivot on it. The block reduces to $\operatorname{diag}(1, \, f_1)$ with $f_1 = X^3 - 5X^2 + 8X - 4$.

> [!note]- Derivation
> $$M = \begin{pmatrix} X^2-2X+1 & -2X+3 \\ 1-X & X-1 \end{pmatrix} = \begin{pmatrix} (X-1)^2 & -2X+3 \\ -(X-1) & X-1 \end{pmatrix}.$$
> No entry is a constant, but the $(1,1)$-entry $(X-1)^2$ is a multiple of the $(2,1)$-entry $-(X-1)$. Add $(X-1)$ times row $2$ to row $1$: the new $(1,1)$-entry is $(X-1)^2 + (X-1)\cdot(-(X-1)) = 0$, and the new $(1,2)$-entry is $(-2X+3) + (X-1)(X-1) = -2X+3 + X^2-2X+1 = X^2-4X+4 = (X-2)^2$. So
> $$M \rightsquigarrow \begin{pmatrix} 0 & (X-2)^2 \\ -(X-1) & X-1 \end{pmatrix}.$$
> The $(2,2)$-entry $X-1$ is a multiple of the $(2,1)$-entry $-(X-1)$: add row $2$'s column-operation analogue — that is, add column $1$ to column $2$. The new $(2,2)$-entry is $(X-1) + (-(X-1)) = 0$, and the $(1,2)$-entry is unchanged at $(X-2)^2$:
> $$\begin{pmatrix} 0 & (X-2)^2 \\ -(X-1) & 0 \end{pmatrix}.$$
> Swap the two columns and scale to make the entries monic — scale row $2$ by $-1$:
> $$\begin{pmatrix} (X-2)^2 & 0 \\ 0 & X-1 \end{pmatrix}.$$
> This is diagonal, but the divisibility $d_1 \mid d_2$ is *violated*: $(X-2)^2 \nmid (X-1)$. The Smith normal form requires the successive entries to divide one another, so one more correction is needed. The standard fix when two diagonal entries $a, b$ fail to be ordered is to replace them by $\gcd(a,b)$ and $\operatorname{lcm}(a,b)$. Here $\gcd\big((X-2)^2, X-1\big) = 1$ (the polynomials $X-2$ and $X-1$ are coprime) and $\operatorname{lcm}\big((X-2)^2, X-1\big) = (X-2)^2(X-1)$.
>
> Explicitly: from $\begin{pmatrix} (X-2)^2 & 0 \\ 0 & X-1 \end{pmatrix}$, add column $2$ to column $1$ to get $\begin{pmatrix} (X-2)^2 & 0 \\ X-1 & X-1 \end{pmatrix}$. The first column now has entries $(X-2)^2$ and $X-1$, whose gcd is $1$; running the Euclidean algorithm on this column produces a constant. Concretely, $(X-2)^2 = (X-3)(X-1) + 1$, so subtract $(X-3)$ times row $2$ from row $1$: row $1$ becomes $\big((X-2)^2 - (X-3)(X-1),\; -(X-3)(X-1)\big) = \big(1,\; -(X-3)(X-1)\big)$. The matrix is
> $$\begin{pmatrix} 1 & -(X-3)(X-1) \\ X-1 & X-1 \end{pmatrix}.$$
> Now pivot on the unit $1$ at $(1,1)$: subtract $(X-1)$ times row $1$ from row $2$, giving row $2$ equal to $\big(0,\; (X-1) - (X-1)\cdot(-(X-3)(X-1))\big) = \big(0,\; (X-1) + (X-1)^2(X-3)\big)$. Factor out $X-1$: the $(2,2)$-entry is $(X-1)\big[1 + (X-1)(X-3)\big] = (X-1)(X^2-4X+4) = (X-1)(X-2)^2$. Clearing row $1$ by a column operation (add $(X-3)(X-1)$ times column $1$ to column $2$) leaves
> $$M \rightsquigarrow \begin{pmatrix} 1 & 0 \\ 0 & (X-1)(X-2)^2 \end{pmatrix}.$$
> Finally expand $f_1 := (X-1)(X-2)^2 = (X-1)(X^2-4X+4) = X^3 - 4X^2 + 4X - X^2 + 4X - 4 = X^3 - 5X^2 + 8X - 4$.

**Step 4: Assemble the Smith normal form and read off the invariant factors.**

$$XI - A \;\rightsquigarrow\; \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & X^3-5X^2+8X-4 \end{pmatrix}.$$

There is exactly one non-constant diagonal entry, so $V_A$ has a single invariant factor $f_1 = X^3 - 5X^2 + 8X - 4 = (X-1)(X-2)^2$.

> [!note]- Derivation
> Splicing Steps 2 and 3: the full matrix reduced to $\operatorname{diag}(1, M)$, and $M$ reduced to $\operatorname{diag}(1, f_1)$, so $XI-A$ reduces to $\operatorname{diag}(1, 1, f_1)$. The two leading $1$'s are units of $\mathbb{Q}[X]$; they contribute summands $\mathbb{Q}[X]/(1) = 0$ to the module and are discarded. The non-constant entry $f_1$ — already monic — is the sole invariant factor.
>
> By the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]], read through the [[Thm - Smith Normal Form|Smith normal form]] of the presentation matrix,
> $$V_A \;\cong\; \frac{\mathbb{Q}[X]}{(1)} \oplus \frac{\mathbb{Q}[X]}{(1)} \oplus \frac{\mathbb{Q}[X]}{(f_1)} \;\cong\; \frac{\mathbb{Q}[X]}{\big(X^3-5X^2+8X-4\big)}.$$
> So $V_A$ is *cyclic* as an $\mathbb{Q}[X]$-module — generated by a single vector — which is the special case $s = 1$ of the rational canonical form: the whole space is a single companion block. (A vector $v$ with $v, Av, A^2v$ a basis is called a *cyclic vector*; its existence is equivalent to $V_A$ being a cyclic module.)

**Step 5: Write the rational canonical form and read off the minimal and characteristic polynomials.**

The rational canonical form of $A$ is the single companion block

$$c(f_1) = \begin{pmatrix} 0 & 0 & 4 \\ 1 & 0 & -8 \\ 0 & 1 & 5 \end{pmatrix}.$$

The minimal polynomial is $m_A(X) = f_1 = X^3 - 5X^2 + 8X - 4$ and the characteristic polynomial is $\chi_A(X) = f_1 = X^3 - 5X^2 + 8X - 4$.

> [!note]- Derivation
> Write $f_1 = a_0 + a_1 X + a_2 X^2 + X^3$ with $a_0 = -4$, $a_1 = 8$, $a_2 = -5$. The companion matrix is
> $$c(f_1) = \begin{pmatrix} 0 & 0 & -a_0 \\ 1 & 0 & -a_1 \\ 0 & 1 & -a_2 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 4 \\ 1 & 0 & -8 \\ 0 & 1 & 5 \end{pmatrix}.$$
> By the [[Thm - Rational Canonical Form|rational canonical form theorem]], $A$ is similar over $\mathbb{Q}$ to the block-diagonal matrix $\operatorname{diag}(c(f_1), \dots, c(f_s))$; here $s = 1$, so $A$ is similar to the single block $c(f_1)$.
>
> *Minimal polynomial.* The minimal polynomial is the largest invariant factor $f_s$. Reason: in the decomposition $V_A \cong \bigoplus_i \mathbb{Q}[X]/(f_i)$, the polynomial $f_s$ kills the summand $\mathbb{Q}[X]/(f_s)$, and it kills every other summand because $f_i \mid f_s$; so $f_s(A) = 0$. No proper divisor of $f_s$ kills $\mathbb{Q}[X]/(f_s)$, so $f_s$ is minimal. With $s=1$, $m_A = f_1 = X^3-5X^2+8X-4$.
>
> *Characteristic polynomial.* The characteristic polynomial is the product $\prod_i f_i$: each block $c(f_i)$ has characteristic polynomial $f_i$, and the characteristic polynomial of a block-diagonal matrix is the product over blocks. With $s=1$, $\chi_A = f_1 = X^3-5X^2+8X-4$.
>
> *Cross-check against $\det(XI-A)$.* Expand the determinant of the original characteristic matrix along the first row:
> $$\det(XI-A) = (X-3)\big[X(X-2) - (-1)\big] - 1\big[(-2)(X-2) - (-1)(-1)\big] + (-1)\big[(-2)\cdot 1 - X\cdot(-1)\big].$$
> Term by term: $X(X-2)+1 = X^2-2X+1$, so the first term is $(X-3)(X^2-2X+1)$. Next $(-2)(X-2)-1 = -2X+3$, so the second term is $-(-2X+3) = 2X-3$. Last $(-2) - (-X) = X-2$, so the third term is $-(X-2) = -X+2$. Hence
> $$\det(XI-A) = (X-3)(X^2-2X+1) + (2X-3) + (-X+2).$$
> Expand $(X-3)(X^2-2X+1) = X^3-2X^2+X - 3X^2+6X-3 = X^3-5X^2+7X-3$. Adding the remaining terms: $X^3-5X^2+7X-3 + 2X-3 - X+2 = X^3-5X^2+8X-4$. This matches $\chi_A$ exactly, confirming the Smith normal form computation. (Elementary row/column operations over $\mathbb{Q}[X]$ alter the determinant only by units of $\mathbb{Q}[X]$ — non-zero rationals — and since both $\det(XI-A)$ and $\prod f_i$ are monic of degree $3$, they must be equal, not merely proportional.)

> [!note]- Complete formal solution
> **Claim.** The matrix $A = \begin{pmatrix} 3 & -1 & 1 \\ 2 & 0 & 1 \\ 1 & -1 & 2 \end{pmatrix}$ has rational canonical form $c(f_1) = \begin{pmatrix} 0 & 0 & 4 \\ 1 & 0 & -8 \\ 0 & 1 & 5 \end{pmatrix}$, with $f_1 = X^3-5X^2+8X-4 = (X-1)(X-2)^2$, and $m_A = \chi_A = f_1$.
>
> *Characteristic matrix.* $XI - A = \begin{pmatrix} X-3 & 1 & -1 \\ -2 & X & -1 \\ -1 & 1 & X-2 \end{pmatrix}$ over $\mathbb{Q}[X]$; this presents the $\mathbb{Q}[X]$-module $V_A$.
>
> *Smith normal form.* Pivoting on the constant entry $-1$ (move it to $(1,1)$ by row/column swaps, scale to $1$, clear its row and column with polynomial row/column operations) splits off a unit and leaves the $2\times 2$ block $M = \begin{pmatrix} (X-1)^2 & -2X+3 \\ -(X-1) & X-1 \end{pmatrix}$. Row/column operations reduce $M$ to $\operatorname{diag}\big((X-2)^2, X-1\big)$, and since $(X-2)^2 \nmid (X-1)$, a gcd-lcm correction (the polynomials $X-1, X-2$ being coprime) replaces these by $1$ and $(X-1)(X-2)^2$. Hence $XI-A$ reduces to $\operatorname{diag}\big(1, 1, (X-1)(X-2)^2\big)$.
>
> *Invariant factor and decomposition.* The unique non-constant Smith entry is $f_1 = (X-1)(X-2)^2 = X^3-5X^2+8X-4$, so by the structure theorem $V_A \cong \mathbb{Q}[X]/(f_1)$ — a cyclic module.
>
> *Canonical form.* By the rational canonical form theorem, $A$ is similar over $\mathbb{Q}$ to $c(f_1)$. Writing $f_1 = -4 + 8X - 5X^2 + X^3$ gives the displayed companion matrix.
>
> *Minimal and characteristic polynomials.* The minimal polynomial is the largest invariant factor, $m_A = f_1$; the characteristic polynomial is the product of all invariant factors, $\chi_A = f_1$. Direct expansion of $\det(XI-A)$ yields $X^3-5X^2+8X-4$, confirming $\chi_A = f_1$. $\blacksquare$

---

# Key Takeaways

**The characteristic matrix $XI - A$ is a *presentation matrix* of the module $V_A$, so its Smith normal form computes the invariant factors.** The conceptual engine of this exercise is the identification of $XI - A$ as a square presentation matrix for the $F[X]$-module $V_A$: there is an exact sequence $F[X]^n \xrightarrow{XI-A} F[X]^n \to V_A \to 0$, so $V_A$ is the cokernel of $XI-A$. The structure theorem is *proved* by reducing presentation matrices to Smith normal form, and that proof is constructive — it is an algorithm. The trigger "I need the invariant-factor decomposition of $V_A$" should fire the reaction "write down $XI-A$ and diagonalise it over $F[X]$". This is the matrix-theoretic incarnation of a fully general principle: for any finitely generated module over a Euclidean domain given by generators and relations, stack the relations into a matrix and compute its Smith normal form — the non-unit diagonal entries are the invariant factors. The same algorithm computes the structure of a finitely generated abelian group from a relation matrix over $\mathbb{Z}$; only the Euclidean domain changes.

**Elimination over a Euclidean domain is the Euclidean algorithm in disguise — manufacture a unit, then pivot.** Gaussian elimination over a *field* clears a column by dividing by the pivot; over the Euclidean domain $F[X]$ you may not divide by a non-constant polynomial, so the move that replaces division is *division with remainder*: subtract a polynomial multiple of one row from another to reduce a degree, exactly the step in computing $\gcd$ in $F[X]$. The strategically decisive observation is that the *units* of $F[X]$ are precisely the non-zero constants, and a unit pivot behaves just like a field pivot — it clears its entire row and column in one stroke and splits off. So the universal tactic for these computations is: hunt for a constant entry (or create one by Euclidean reduction), move it to a corner, pivot, and recurse on the smaller block. When two final diagonal entries fail the divisibility chain $d_1 \mid d_2 \mid \cdots$, the gcd-lcm correction $\{a,b\} \rightsquigarrow \{\gcd(a,b), \operatorname{lcm}(a,b)\}$ — itself just one more round of the Euclidean algorithm — restores it. Recognising elimination-over-$F[X]$ as "the Euclidean algorithm threaded through a matrix" is what makes these computations routine rather than mysterious.

**The invariant factors carry *all* the similarity data: minimal polynomial, characteristic polynomial, and the rational canonical form at once.** Once the list $f_1 \mid f_2 \mid \cdots \mid f_s$ is in hand, three of the most-asked invariants of a matrix are immediate, with no further work. The largest invariant factor $f_s$ is the **minimal polynomial**, because $f_s$ annihilates every summand $F[X]/(f_i)$ (using $f_i \mid f_s$) and no proper divisor annihilates $F[X]/(f_s)$. The product $f_1 \cdots f_s$ is the **characteristic polynomial**, because each companion block $c(f_i)$ has characteristic polynomial $f_i$ and determinants of block-diagonal matrices multiply. And the block-diagonal $\operatorname{diag}(c(f_1), \dots, c(f_s))$ *is* the **rational canonical form**. This is why the rational canonical form is a *complete* similarity invariant while the minimal and characteristic polynomials individually are not: the pair $(m_A, \chi_A)$ can fail to pin down the matrix, but the full invariant-factor list never does. A useful corollary visible in this very example: $V_A$ turned out cyclic ($s=1$), and a matrix has a cyclic module exactly when $m_A = \chi_A$ — equivalently when it admits a *cyclic vector* $v$ with $\{v, Av, \dots, A^{n-1}v\}$ a basis. Whenever you see $\deg m_A = n$, you know immediately that the rational canonical form is a single companion block.

**The determinant cross-check is free and worth doing every time.** Expanding $\det(XI-A)$ directly and comparing it with $\prod f_i$ costs one cofactor expansion and catches almost any arithmetic slip in the Smith normal form reduction. The check is valid because elementary row and column operations over $F[X]$ multiply the determinant only by units — non-zero constants — so $\det(XI-A)$ and the product of the Smith diagonal entries differ by a non-zero scalar; since both the characteristic polynomial and $\prod f_i$ are monic of degree $n$, that scalar is forced to be $1$ and the two are equal. More generally, any quantity that is invariant (up to units) under elementary operations — the determinant, the gcd of all $k\times k$ minors, the rank — can be computed before *and* after the reduction and compared. The $k$-th determinantal divisor $\Delta_k$ (the gcd of all $k\times k$ minors) satisfies $\Delta_k = d_1 d_2 \cdots d_k$, which gives an independent, pivoting-free way to extract each invariant factor as $d_k = \Delta_k / \Delta_{k-1}$ — a valuable alternative when the elimination gets messy.

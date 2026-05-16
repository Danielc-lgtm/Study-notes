---
type: theorem
subject: module-theory
prereqs:
  - "Def - Euclidean Domain"
  - "Def - Principal Ideal Domain"
  - "Def - Elementary Operations and Equivalent Matrices"
  - "Def - Module"
  - "Def - Free Module"
tags: [algebra, module-theory]
---

# Notation

Throughout, $R$ is a [[Def - Euclidean Domain|Euclidean domain]]: an integral domain equipped with a **Euclidean function** $\varphi : R \setminus \{0\} \to \mathbb{Z}_{\geq 0}$ such that for every $a \in R$ and every non-zero $b \in R$ there exist $q, r \in R$ with $a = qb + r$ and either $r = 0$ or $\varphi(r) < \varphi(b)$. The standard examples are $\mathbb{Z}$ (with $\varphi(n) = |n|$) and the polynomial ring $k[X]$ over a field $k$ (with $\varphi(f) = \deg f$). In a Euclidean domain the greatest common divisor $\gcd(a,b)$ exists for all $a, b$, and there are $x, y \in R$ with $ax + by = \gcd(a,b)$.

An $m \times n$ **matrix** $A = (A_{ij})$ has entries in $R$; the $(i,j)$ entry is $A_{ij}$. The **elementary row operations** on $A$ are: (ER1) add $c \in R$ times the $i$th row to the $j$th row; (ER2) swap two rows; (ER3) multiply a row by a unit $c \in R$. **Elementary column operations** (EC1)–(EC3) are defined identically with "row" replaced by "column". Each elementary operation is realised by left- (rows) or right- (columns) multiplication by an invertible matrix. Two matrices $A$ and $B$ are [[Def - Elementary Operations and Equivalent Matrices|equivalent]], written here informally, if one is obtained from the other by a finite sequence of elementary row and column operations; equivalently $B = QAT^{-1}$ for invertible matrices $Q$ and $T^{-1}$.

We write $a \mid b$ for "$a$ divides $b$" (there is $c \in R$ with $b = ca$). The notation $\operatorname{diag}(d_1, \dots, d_r, 0, \dots, 0)$ denotes the $m \times n$ matrix whose $(i,i)$ entry is $d_i$ for $1 \leq i \leq r$ and whose every other entry is $0$. The full symbol registry is on the parent page [[Modules II — §3.3–3.4]].

---

# Statement

> **Smith Normal Form.** Let $R$ be a [[Def - Euclidean Domain|Euclidean domain]] and let $A$ be an $m \times n$ matrix with entries in $R$. Then $A$ is [[Def - Elementary Operations and Equivalent Matrices|equivalent]] to a diagonal matrix
> $$\operatorname{diag}(d_1, d_2, \dots, d_r, 0, \dots, 0) \;=\; \begin{pmatrix} d_1 & & & & & \\ & d_2 & & & & \\ & & \ddots & & & \\ & & & d_r & & \\ & & & & 0 & \\ & & & & & \ddots \end{pmatrix}$$
> with each $d_i$ non-zero and
> $$d_1 \mid d_2 \mid d_3 \mid \cdots \mid d_r.$$
> The non-zero diagonal entries $d_1, \dots, d_r$ are called the **invariant factors** of $A$.

---

# Motivation

Over a field, the story of a matrix under row and column operations is finished in one line: every $m \times n$ matrix is equivalent to a block matrix $\begin{pmatrix} I_r & 0 \\ 0 & 0\end{pmatrix}$, with $r$ the rank. Row and column operations are exactly the freedom to change basis in the source and the target independently, and once you may do both, the only invariant left is how many independent directions the map genuinely uses. Linear algebra over a field is, in this sense, trivial: the rank is the whole story.

Over a ring this collapses. The obstruction is concrete and you can see it in the smallest possible example. The matrix $\begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix}$ over $\mathbb{Z}$ cannot be brought to the form $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$, because no row or column operation over $\mathbb{Z}$ can turn the $2$ into a $1$ — the operations multiply rows only by *units*, and the units of $\mathbb{Z}$ are just $\pm 1$. The number $2$ is stuck. So the field answer is wrong over $\mathbb{Z}$, and the question becomes: what *is* the simplest form a matrix can be reduced to, when you are no longer allowed to divide?

Smith normal form is the answer. It says: you cannot delete the arithmetic content of the entries, but you *can* always diagonalise, and you can do better than a bare diagonal — you can arrange the diagonal entries into a divisibility chain $d_1 \mid d_2 \mid \cdots \mid d_r$. The entries that were "stuck" do not disappear; they line up along the diagonal in increasing divisibility order. The matrix $\begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix}$ is already in this form, with the single invariant factor $d_1 = 2$.

Why insist on the divisibility chain rather than settling for an arbitrary diagonal matrix? Because the diagonal alone is not canonical — a diagonal matrix can be shuffled and rescaled into many superficially different diagonal matrices — whereas the *ordered divisibility chain* is essentially rigid. As the companion theorem [[Thm - Fitting Ideals are Invariants|Fitting ideals are invariants]] shows, once the chain $d_1 \mid \cdots \mid d_r$ is imposed, the $d_k$ are determined up to units. The chain is what upgrades "a diagonal form" into "*the* normal form".

The payoff is the entire structure theory of finitely generated modules. A finitely generated module over a Euclidean domain is presented by a matrix of relations; bringing that matrix to Smith normal form decouples the relations completely, and the diagonal entries become the orders of cyclic summands. The [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] and, as its most famous special case, the [[Thm - Classification of Finitely Generated Abelian Groups|classification of finitely generated abelian groups]] are both read straight off the Smith normal form. The divisibility chain $d_1 \mid \cdots \mid d_r$ is, in disguise, exactly the divisibility chain in the classification $\mathbb{Z}/d_1 \oplus \cdots \oplus \mathbb{Z}/d_r$. Smith normal form is the computational engine under all of it.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is a matrix with entries in a Euclidean domain. The skill is recognising when a problem hands you such a matrix without saying so.

The first disguised source is **a finite presentation of a module**. A finitely generated module over $R$ is given by generators and relations; the relations, written as columns of coefficients, form a matrix over $R$. The non-obvious recognition is that "a module presented by generators and relations" *is* a matrix awaiting Smith normal form, and that diagonalising the matrix diagonalises the module — decoupling tangled relations into independent cyclic pieces. *Example problem:* given an abelian group as $\mathbb{Z}^n$ modulo an explicit set of relations, determine its isomorphism type — write the relation matrix and reduce.

The second disguised source is **a submodule of a free module presented by generators**. If $N \leq R^m$ is generated by $x_1, \dots, x_n$, stacking the $x_i$ as the columns of an $m \times n$ matrix produces a matrix over $R$. The non-obvious step is that the *generators of a submodule* are the columns of a matrix, so submodule problems are matrix problems; this is exactly the route taken by [[Thm - Submodules of Free Modules over a Euclidean Domain|submodules of free modules over a Euclidean domain]]. *Example problem:* find a basis-adapted description of the subgroup of $\mathbb{Z}^3$ generated by three explicit vectors.

The third disguised source is **a linear map between free modules**. A homomorphism $R^n \to R^m$, once bases are chosen on both sides, *is* an $m \times n$ matrix over $R$. The non-obvious framing is that bringing the matrix to Smith normal form is choosing new bases of source and target in which the map is diagonal — the ring-theoretic analogue of the singular value decomposition. *Example problem:* given an explicit $\mathbb{Z}$-linear map $\mathbb{Z}^3 \to \mathbb{Z}^2$, compute its cokernel.

**Targets (Output Amplification)**

The bare conclusion is a diagonal matrix with a divisibility chain. Combined with other facts it does much more.

Combine the conclusion with **the relation between $A$ and the cokernel $R^m / A R^n$**. The columns of $A$ generate the image, and in Smith normal form $\operatorname{diag}(d_1, \dots, d_r, 0, \dots)$ the cokernel splits as $\bigoplus_k R/(d_k) \oplus R^{m-r}$. The non-obvious payoff: a single diagonalisation computes the full isomorphism type of the cokernel, free rank and torsion together. This is the engine of the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]].

Combine the conclusion with **the invariance of the $d_k$**. Smith normal form produces *some* diagonal matrix with a divisibility chain, but the algorithm makes ad hoc choices and could a priori yield different chains. Pairing it with [[Thm - Fitting Ideals are Invariants|Fitting ideals are invariants]] shows the $d_k$ are determined up to units, so the chain is a genuine invariant of $A$. The further result: Smith normal form becomes a complete invariant for matrix equivalence — two matrices are equivalent if and only if they have the same invariant factors.

Combine the conclusion with **the change-of-basis interpretation of the operations**. Row operations on $A$ correspond to a change of basis in $R^m$; column operations to a change of generators of the submodule generated by the columns. The non-obvious consequence is that Smith normal form, read structurally rather than numerically, *constructs adapted bases*: this is the mechanism by which [[Thm - Submodules of Free Modules over a Euclidean Domain|every submodule of a free module is shown to be free]].

---

# Why Is It True

The intuition is the divisibility analogue of Gaussian elimination, with one extra idea bolted on.

Start with what you would do over a field. Find a non-zero entry, move it to the $(1,1)$ corner by swapping rows and columns, and then use it as a pivot: since over a field you may divide by it, you subtract multiples of the first row and column to clear everything else in the first row and first column. You are left with a $1$ in the corner (after rescaling) and a smaller matrix in the bottom-right; recurse. The whole procedure runs because *the pivot divides everything*, so every other entry in its row and column is a clean multiple of it.

Over a ring you cannot divide, so the pivot $A_{11}$ need not divide the other entries of its row and column — and that is the entire difficulty. But here is the saving grace: $R$ is a Euclidean domain, so even when $A_{11}$ does not divide a neighbour $A_{1j}$, you can still run the division algorithm, $A_{1j} = q A_{11} + r$ with $\varphi(r) < \varphi(A_{11})$. Subtracting $q$ times the first column from the $j$th column places the *remainder* $r$ in position $(1,j)$, and swapping it into the corner gives a new $(1,1)$ entry with a strictly smaller Euclidean value. You have not cleared the row, but you have made the corner entry simpler. The Euclidean function is a measure of complexity that strictly decreases, and it cannot decrease forever — it takes values in $\mathbb{Z}_{\geq 0}$. So after finitely many such steps the corner entry can no longer be reduced, which means it finally *does* divide every entry in its row and column. Now the field-style clearing works, and the first row and column are zeroed out.

The mechanism is: **the Euclidean function turns "make the pivot divide its neighbours" into a strictly-decreasing process, hence a terminating one.** This is exactly how the Euclidean algorithm computes a gcd — and indeed the corner entry, once it can no longer be reduced, is the gcd of the first row and column. That is why the Euclidean hypothesis is the natural one: it is precisely the hypothesis that makes "reduce the pivot" terminate.

That handles diagonalisation. The extra idea is the divisibility chain. After clearing the first row and column you have $d$ in the corner and a smaller matrix $C$ in the bottom-right. If you simply recursed on $C$ you would get *a* diagonal matrix, but nothing forces $d$ to divide the entries of $C$ — so the resulting diagonal need not satisfy $d_1 \mid d_2 \mid \cdots$. The fix (move (iii)) is to check whether $d$ divides every entry of $C$, and if some entry $C_{ij}$ is not divisible by $d$, to *manufacture a violation in the first row*: add the offending column into the first column, so $C_{ij}$ appears in the first column, then re-run the corner-reduction process. The reduction will replace $d$ by something of strictly smaller Euclidean value — because $d$ failed to divide $C_{ij}$, the remainder is non-zero. Again this strict decrease can happen only finitely often, so eventually you reach a corner entry $d$ that divides *every* remaining entry. Now recursion is safe: every operation applied to $C$ keeps the entries multiples of $d$, so all later invariant factors inherit divisibility by $d$, and the chain $d_1 \mid d_2 \mid \cdots$ is built one link at a time.

So the reason to expect the theorem: diagonalisation is Gaussian elimination with the division algorithm patching the failure of exact division; the divisibility chain is one more application of the same patch, used to drag any divisibility failure out of the bottom-right block and into the corner where the Euclidean function can grind it away. Every "this terminates" step is the integers $\mathbb{Z}_{\geq 0}$ refusing to decrease forever.

---

# What Makes This Hard

The conceptually non-obvious step is move (iii): after clearing the first row and column you have a perfectly good diagonal start, and it is genuinely surprising that you must *deliberately re-mess-up* the first row — by adding in a column from the bottom-right block — to enforce divisibility, rather than just recursing. People get stuck either by stopping at a bare diagonal matrix and forgetting the chain entirely, or by trying to fix divisibility *within* the block $C$ without realising the violation must be exported to the corner. The most common error is a non-terminating argument: forgetting that *every* reduction step strictly decreases $\varphi(A_{11})$, and hence concluding the algorithm might loop forever — the strict decrease into $\mathbb{Z}_{\geq 0}$ is the load-bearing finiteness fact and must be invoked at each of the three moves.

---

# Rederivation Scaffold

**High-level strategy:**
Diagonalise by Gaussian elimination, using the division algorithm to compensate for the absence of exact division: repeatedly reduce the $(1,1)$ entry until it divides its whole row and column, then clear them. Before recursing, run move (iii) to force the corner entry to divide the entire remaining block, so the recursion produces a divisibility chain. Every reduction strictly decreases the Euclidean function $\varphi(A_{11})$, which forces termination.

**Subgoal decomposition:**

1. **Get a non-zero corner entry.** If $A = 0$ stop. Otherwise, by row and column swaps, move a non-zero entry into position $(1,1)$.
   - *Hint:* Swap rows then columns; this only permutes entries.
   - *Why needed:* Establishes a pivot to work with.

2. **Reduce the corner until it divides its row and column.** While some $A_{1j}$ or $A_{i1}$ is not divisible by $A_{11}$, use the division algorithm to replace $A_{11}$ by a remainder of strictly smaller $\varphi$-value.
   - *Hint:* If $A_{1j} = qA_{11} + r$ with $r \neq 0$, subtract $q$ times column $1$ from column $j$ (so $r$ sits in $(1,j)$), then swap column $j$ into column $1$. Same with rows. Each step drops $\varphi(A_{11})$; termination because $\varphi$ takes values in $\mathbb{Z}_{\geq 0}$.
   - *Why needed:* Once the corner divides its row and column, the entries there are clean multiples of it and can be cleared.

3. **Clear the first row and column.** With $A_{11} = d$ dividing all $A_{1j}$ and $A_{i1}$, subtract the right multiples of column $1$ (resp. row $1$) from the others to zero out the rest of the first row and column.
   - *Hint:* This is the field-style pivot step; it works now because $d$ divides everything in its row and column.
   - *Why needed:* Splits off $d$ in the corner with a smaller block $C$ in the bottom-right.

4. **Force the corner to divide the whole block (move iii).** If some entry $C_{ij}$ of $C$ is not divisible by $d$, add column $j$ to column $1$, subtract $q$ times row $1$ from row $i$ (where $C_{ij} = qd + r$), bringing $r$ toward the corner; swap $r$ into position $(1,1)$ and return to step 2.
   - *Hint:* Adding the offending column into column $1$ resurfaces the divisibility failure in the first row, where corner-reduction can attack it. Each pass strictly decreases $\varphi(A_{11})$, so this loop terminates.
   - *Why needed:* Guarantees the eventual corner entry $d_1$ divides every entry of the remaining block, so the chain $d_1 \mid d_2 \mid \cdots$ holds.

5. **Recurse on the block.** Once $d$ divides every entry of $C$, apply the whole procedure to $C$. Every operation on $C$ preserves divisibility of its entries by $d$.
   - *Hint:* Induction on the size of the matrix; the base case is a $1 \times n$ or $m \times 1$ or empty block.
   - *Why needed:* Produces the remaining invariant factors $d_2, \dots, d_r$, each divisible by $d_1$, assembling the full diagonal with divisibility chain.

---

# Lemma Decomposition

> [!note]- Lemma 1: Each elementary operation is invertible and preserves equivalence
> **Statement:** Each of (ER1)–(ER3) and (EC1)–(EC3) is realised by multiplication by an invertible matrix over $R$, and its inverse is again an elementary operation of the same type. Consequently equivalence of matrices is an equivalence relation.
>
> **Hint:** Write down the matrix of each operation and exhibit its inverse explicitly.
>
> **Why needed:** It is what makes "reduce $A$ to a normal form" a legitimate statement about $A$ — the reduced matrix carries the same information, since the steps can be undone.
>
> > [!note]- Full proof
> > Operation (ER1), adding $c$ times row $i$ to row $j$, is left-multiplication by the matrix $E$ equal to the identity except for the entry $c$ in position $(j,i)$. Its inverse is the same kind of matrix with $c$ replaced by $-c$ — adding $-c$ times row $i$ to row $j$ — so $E$ is invertible and (ER1) is reversible by an (ER1). Operation (ER2), swapping rows $i$ and $j$, is left-multiplication by the permutation matrix that is the identity with rows $i, j$ interchanged; it is its own inverse, since swapping twice restores the original. Operation (ER3), multiplying row $i$ by a unit $c$, is left-multiplication by the identity with the $(i,i)$ entry changed to $c$; because $c$ is a unit, $c^{-1} \in R$, and multiplying row $i$ by $c^{-1}$ inverts it. The column operations (EC1)–(EC3) are identical statements with right-multiplication by the same matrices. Since every elementary operation is invertible by an operation of the same type, "obtainable by a finite sequence of elementary operations" is reflexive (empty sequence), symmetric (reverse the sequence, inverting each step), and transitive (concatenate sequences); it is an equivalence relation.

> [!note]- Lemma 2: The division algorithm reduces the corner entry
> **Statement:** Suppose $A_{11} \neq 0$ and some entry $A_{1j}$ (with $j \neq 1$) is not divisible by $A_{11}$. Then a column operation followed by a column swap produces a matrix whose $(1,1)$ entry $r$ satisfies $\varphi(r) < \varphi(A_{11})$. The same holds for an entry $A_{i1}$ of the first column, using row operations.
>
> **Hint:** Apply the Euclidean division $A_{1j} = q A_{11} + r$ and subtract $q$ copies of column $1$ from column $j$.
>
> **Why needed:** It is the single step that drives the corner-reduction loop; its strict decrease of $\varphi$ forces termination.
>
> > [!note]- Full proof
> > Since $A_{11} \neq 0$, the Euclidean function lets us divide: write $A_{1j} = q A_{11} + r$ with $q, r \in R$ and either $r = 0$ or $\varphi(r) < \varphi(A_{11})$. By hypothesis $A_{11}$ does not divide $A_{1j}$, so $r \neq 0$; therefore $\varphi(r) < \varphi(A_{11})$. Perform the column operation (EC1) subtracting $q$ times column $1$ from column $j$. The $(1,j)$ entry becomes $A_{1j} - q A_{11} = r$, while column $1$ is unchanged so the $(1,1)$ entry is still $A_{11}$. Now swap (EC2) columns $1$ and $j$: the entry $r$ moves into position $(1,1)$. The new corner entry is $r$ with $\varphi(r) < \varphi(A_{11})$. If instead an entry $A_{i1}$ of the first column is not divisible by $A_{11}$, write $A_{i1} = q A_{11} + r$, subtract $q$ times row $1$ from row $i$ via (ER1), and swap rows $1$ and $i$ via (ER2); identically the new corner entry $r$ satisfies $\varphi(r) < \varphi(A_{11})$.

> [!note]- Lemma 3: A corner entry dividing its row and column can be used to clear them
> **Statement:** Suppose $A_{11} = d$ divides every other entry of the first row and every other entry of the first column. Then column operations zero out the rest of the first row, and row operations zero out the rest of the first column, leaving a matrix $\begin{pmatrix} d & 0 \\ 0 & C\end{pmatrix}$ — and these operations do not touch the corner entry $d$.
>
> **Hint:** For each $j \neq 1$ write $A_{1j} = c_j d$ and subtract $c_j$ times column $1$ from column $j$.
>
> **Why needed:** This is the step that actually splits off an invariant factor and exposes the smaller block to recurse on.
>
> > [!note]- Full proof
> > For each $j \neq 1$, since $d \mid A_{1j}$, write $A_{1j} = c_j d$ with $c_j \in R$. Apply (EC1) subtracting $c_j$ times column $1$ from column $j$. The $(1,j)$ entry becomes $A_{1j} - c_j d = 0$; column $1$ is unchanged. Doing this for every $j \neq 1$ makes the entire first row zero except for the corner $d$. Now for each $i \neq 1$, the $(i,1)$ entry $A_{i1}$ is divisible by $d$ (this was true at the start, and clearing the first row only altered entries in rows; the first *column* is still its original column), so write $A_{i1} = c_i' d$ and apply (ER1) subtracting $c_i'$ times row $1$ from row $i$. Since row $1$ is now $(d, 0, \dots, 0)$, this subtraction changes the $(i,1)$ entry to $A_{i1} - c_i' d = 0$ and leaves the other entries of row $i$ unchanged. The first column is now zero except for the corner. The corner entry $d$ was never an argument of any of these operations, so it is unchanged. The matrix has the block form $\begin{pmatrix} d & 0 \\ 0 & C\end{pmatrix}$ with $C$ an $(m-1) \times (n-1)$ matrix.

> [!note]- Lemma 4: Move (iii) — exporting a divisibility failure to the corner
> **Statement:** Suppose the matrix has the form $\begin{pmatrix} d & 0 \\ 0 & C\end{pmatrix}$ but some entry $C_{ij}$ of $C$ is not divisible by $d$. Then a sequence of elementary operations produces a matrix of the same block shape $\begin{pmatrix} d' & 0 \\ 0 & C'\end{pmatrix}$ with $\varphi(d') < \varphi(d)$.
>
> **Hint:** Add the column containing $C_{ij}$ to column $1$, so the offending entry appears in the first column; then run corner-reduction.
>
> **Why needed:** Iterating it terminates (strict $\varphi$-decrease) at a corner entry dividing the entire remaining block — the precondition for the recursion to yield a divisibility chain.
>
> > [!note]- Full proof
> > Let $C_{ij}$ (with $i, j > 1$ in the full matrix) be an entry of $C$ not divisible by $d$. Apply (EC1) adding column $j$ to column $1$. The first column now has $d$ in position $(1,1)$ and $C_{ij}$ in position $(i,1)$; the first row is still $(d, 0, \dots)$. Write the Euclidean division $C_{ij} = qd + r$; since $d \nmid C_{ij}$ we have $r \neq 0$, so $\varphi(r) < \varphi(d)$. Apply (ER1) subtracting $q$ times row $1$ from row $i$: position $(i,1)$ becomes $C_{ij} - qd = r$. Swap row $i$ into row $1$ and the relevant column so that $r$ occupies position $(1,1)$ — now the corner entry has $\varphi$-value $\varphi(r) < \varphi(d)$, but the first row and column have been disturbed. Re-run corner-reduction (Lemma 2) and clearing (Lemma 3): each corner-reduction step only ever *decreases* $\varphi$ of the corner, so the final corner entry $d'$ satisfies $\varphi(d') \leq \varphi(r) < \varphi(d)$. The result is again of the block form $\begin{pmatrix} d' & 0 \\ 0 & C'\end{pmatrix}$, with $\varphi(d') < \varphi(d)$.

---

# Formal Proof

> [!note]- Complete formal proof
> We argue by induction on $\min(m,n)$, the smaller dimension of the matrix; throughout we keep calling the matrix $A$ even though it changes at each step, to avoid inventing a name for every intermediate matrix. By Lemma 1 every operation is reversible, so each step keeps the matrix equivalent to the original $A$.
>
> **Base case.** If $A = 0$ there is nothing to do: $A = \operatorname{diag}(0,\dots,0)$ is already in Smith normal form with $r = 0$. If $A$ is $1 \times n$ or $m \times 1$, the argument below produces a single non-zero corner entry and clears the rest, and the residual block is empty.
>
> **Producing a non-zero corner entry.** Suppose $A \neq 0$. Some entry $A_{ij}$ is non-zero. Swapping the $i$th and first rows (ER2) and the $j$th and first columns (EC2) moves it into position $(1,1)$, so we may assume $A_{11} \neq 0$.
>
> **Reducing the corner entry.** We make two moves, repeatedly:
>
> *(i)* If some $A_{1j}$ ($j \neq 1$) is not divisible by $A_{11}$, then by Lemma 2 a column operation and a column swap replace the corner entry by a remainder $r$ with $\varphi(r) < \varphi(A_{11})$.
>
> *(ii)* If some $A_{i1}$ ($i \neq 1$) is not divisible by $A_{11}$, then by Lemma 2 (row version) a row operation and a row swap replace the corner entry by a remainder of strictly smaller $\varphi$-value.
>
> Each application of (i) or (ii) strictly decreases $\varphi(A_{11})$. Since $\varphi$ takes values in $\mathbb{Z}_{\geq 0}$, a strictly decreasing sequence of values must terminate. So after finitely many moves no application of (i) or (ii) is possible, which means **$A_{11}$ divides every $A_{1j}$ and every $A_{i1}$**.
>
> **Clearing the first row and column.** With $A_{11} = d$ dividing all of its row and column, Lemma 3 applies: column operations zero the rest of the first row, row operations zero the rest of the first column, and $d$ is untouched. The matrix is now
> $$A = \begin{pmatrix} d & 0 & \cdots & 0 \\ 0 & & & \\ \vdots & & C & \\ 0 & & & \end{pmatrix}.$$
>
> **Enforcing divisibility (move iii).** It need not be true that $d$ divides every entry of $C$. As long as some entry $C_{ij}$ is not divisible by $d$, apply move (iii): by Lemma 4, adding the offending column to column $1$, performing a Euclidean division step, and re-running corner-reduction and clearing yields a matrix of the same block shape $\begin{pmatrix} d' & 0 \\ 0 & C'\end{pmatrix}$ with $\varphi(d') < \varphi(d)$. Each pass of move (iii) strictly decreases $\varphi(A_{11})$, so — again because $\varphi$ is $\mathbb{Z}_{\geq 0}$-valued — only finitely many passes are possible. When move (iii) can no longer be applied we have reached a matrix
> $$A = \begin{pmatrix} d & 0 \\ 0 & C\end{pmatrix}, \qquad d \mid (\text{every entry of } C).$$
>
> **Recursion.** Apply the entire procedure to the smaller matrix $C$, which has dimensions $(m-1) \times (n-1)$. By the inductive hypothesis $C$ is equivalent to a diagonal matrix $\operatorname{diag}(d_2, \dots, d_r, 0, \dots, 0)$ with $d_2 \mid d_3 \mid \cdots \mid d_r$. Crucially, every elementary operation used in reducing $C$ — adding multiples of rows/columns, swapping, multiplying by units — sends entries divisible by $d$ to entries divisible by $d$ (an $R$-linear combination of multiples of $d$ is a multiple of $d$). So the property "$d$ divides every entry of $C$" is preserved throughout the reduction of $C$, and in particular $d \mid d_2$.
>
> **Assembling.** Performing the operations that reduce $C$ as operations on the rows and columns $2, \dots$ of the full matrix (they do not involve row or column $1$, so $d$ and the zeros of the first row and column are untouched), the full matrix becomes
> $$\operatorname{diag}(d, d_2, \dots, d_r, 0, \dots, 0).$$
> Set $d_1 := d$. Then $d_1 \mid d_2$ (shown above) and $d_2 \mid d_3 \mid \cdots \mid d_r$ (inductive hypothesis), giving the full divisibility chain $d_1 \mid d_2 \mid \cdots \mid d_r$, with every $d_i$ non-zero. The matrix $A$ is equivalent to this Smith normal form. $\blacksquare$
>
> *Remark.* If one drops the requirement of the divisibility chain — that is, omits move (iii) — moves (i), (ii) and clearing alone already produce a diagonal matrix. Move (iii) is exactly the extra ingredient that upgrades a bare diagonal form to the Smith normal form.

---

# Cross-Field Exercise Suggestions

**Computing the structure of an abelian group from a presentation.** A finitely generated abelian group is given as $\mathbb{Z}^n$ modulo the subgroup generated by explicit relation vectors. Form the matrix whose columns are the relations and bring it to Smith normal form; the invariant factors $d_1 \mid \cdots \mid d_r$ are the orders of the cyclic summands, and the surplus zero columns/rows give the free rank. The theorem applies because $\mathbb{Z}$ is the Euclidean domain $R$, and the non-obvious point is that an apparently combinatorial group-classification question is a single matrix diagonalisation.

**Diagonalising a polynomial matrix and rational canonical form.** Over $k[X]$ for a field $k$ — a Euclidean domain with $\varphi = \deg$ — the matrix $X I - M$ associated to a square matrix $M$ over $k$ has a Smith normal form whose invariant factors are exactly the invariant factors of the linear operator $M$. The theorem applies with $R = k[X]$, and the non-obvious recognition is that the rational canonical form of a matrix is the Smith normal form of its characteristic matrix $XI - M$ — a similarity problem over $k$ disguised as an equivalence problem over $k[X]$.

**Counting solutions of a linear system over the integers.** To decide whether a system $A\mathbf{x} = \mathbf{b}$ with integer matrix $A$ has integer solutions, and to describe them, bring $A$ to Smith normal form $\operatorname{diag}(d_1, \dots, d_r, 0, \dots)$; solvability reduces to divisibility conditions on the transformed right-hand side, one per invariant factor. The theorem applies with $R = \mathbb{Z}$, and the non-obvious step is that the number-theoretic question of integral solvability is governed entirely by the invariant factors, not by the determinant or rank alone.

**The Smith normal form of an incidence or boundary matrix in topology.** A simplicial complex has boundary maps represented by integer matrices; the Smith normal form of a boundary matrix reads off the torsion in the homology of the complex, with the invariant factors $d_k > 1$ giving the torsion coefficients. The theorem applies with $R = \mathbb{Z}$, and the non-obvious application is that the torsion subgroups of homology — geometric invariants of a space — are computed by diagonalising a matrix of $\pm 1$'s and $0$'s.

---

# Bridges

- **[[Thm - Fitting Ideals are Invariants|Fitting Ideals are Invariants]]** — the uniqueness companion. Smith normal form produces *a* divisibility chain by an algorithm full of arbitrary choices; the Fitting-ideal theorem proves that the chain is determined up to units, so "the invariant factors of $A$" is well-defined. Together they say Smith normal form is a *complete invariant* of matrix equivalence.

- **[[Thm - Submodules of Free Modules over a Euclidean Domain|Submodules of Free Modules over a Euclidean Domain]]** — the immediate structural application. Writing the generators of a submodule $N \leq R^m$ as the columns of a matrix and applying Smith normal form, the row operations change the basis of $R^m$ and the column operations change the generators of $N$; the diagonal form exhibits an adapted basis showing $N$ is free.

- **[[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|Structure Theorem for Finitely Generated Modules]]** — the downstream payoff. A finitely generated module is a cokernel $R^m / A R^n$; Smith normal form of the presentation matrix $A$ splits the cokernel into cyclic pieces $R/(d_k)$ plus a free part, which is the structure theorem.

- **[[Thm - Classification of Finitely Generated Abelian Groups|Classification of Finitely Generated Abelian Groups]]** — the famous special case. Taking $R = \mathbb{Z}$, the invariant factors $d_1 \mid \cdots \mid d_r$ of a presentation matrix are exactly the orders in the invariant-factor decomposition $\mathbb{Z}/d_1 \oplus \cdots \oplus \mathbb{Z}/d_r \oplus \mathbb{Z}^s$; the divisibility chain of the theorem *is* the divisibility chain of the classification.

- **Gaussian elimination and the rank normal form over a field** — the degenerate case. When $R$ is a field every non-zero element is a unit, so every reduction step can rescale a pivot to $1$; move (iii) becomes vacuous and Smith normal form collapses to $\begin{pmatrix} I_r & 0 \\ 0 & 0\end{pmatrix}$. Smith normal form is Gaussian elimination upgraded to rings where you may no longer divide.

---

# Unlocked by This

> [!tip] Rational and Jordan Canonical Forms *(from Linear Algebra)*
> Applying Smith normal form over the Euclidean domain $k[X]$ to the characteristic matrix $XI - M$ of a linear operator yields its invariant factors, from which the rational canonical form is read directly, and — over an algebraically closed field, after factoring the invariant factors — the Jordan canonical form. The classification of a linear operator up to similarity is the Smith normal form theorem over $k[X]$.

> [!tip] Homology with Integer Coefficients *(from Algebraic Topology)*
> The homology groups of a finite simplicial complex are the cokernels and kernels of integer boundary matrices; Smith normal form of these matrices computes the Betti numbers (from the zero invariant factors) and the torsion coefficients (from the invariant factors exceeding $1$). The algorithmic computability of integral homology rests on this theorem.

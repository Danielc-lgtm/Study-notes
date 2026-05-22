---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
tags: [algebra, linear-algebra]
---

# Problem Statement

Show that the subspaces of $\mathbb{F}^2$ are exactly:
- the trivial subspace $\{0\}$,
- every line through the origin (i.e. the span of a nonzero vector $v \in \mathbb{F}^2$),
- the whole space $\mathbb{F}^2$.

Together with the corresponding result for $\mathbb{R}^3$ — subspaces are $\{0\}$, lines through the origin, planes through the origin, and $\mathbb{R}^3$ — this is the classification of low-dimensional subspaces stated by Axler in LADR §1C, used implicitly throughout the chapter.

**Recall:**

A [[Def - Subspace|subspace]] of $\mathbb{F}^2$ is a non-empty subset closed under addition and scalar multiplication:

![[Def - Subspace#The Definition]]

The **span** of a vector $v \in \mathbb{F}^2$ is the line $\{\lambda v : \lambda \in \mathbb{F}\}$ — the set of scalar multiples of $v$.

---

# Convergent Strategy

**Problem class:** This is a **classification** problem: enumerate exactly the objects of a certain kind in a given setting. Classification proofs typically have two parts — exhibit all the candidates, then show every actual object equals one of them.

**Assumption pattern:** We are working in $\mathbb{F}^2$ — a $2$-dimensional space — with $\mathbb{F}$ either $\mathbb{R}$ or $\mathbb{C}$. The key feature exploited is that $\mathbb{F}^2$ is two-dimensional, so a subspace containing two non-parallel vectors must be all of $\mathbb{F}^2$.

**Theorem routing:** The classification is essentially dimensional: subspaces of $\mathbb{F}^2$ are parameterized by their dimension, which is $0$, $1$, or $2$. The proof routes through case analysis on whether the subspace contains nonzero vectors, and whether it contains two "linearly independent" vectors. The argument is elementary and concrete — anticipating the dimension theory of [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]] without invoking it.

**Key decision point:** The non-obvious step is **how to show that two non-parallel vectors span all of $\mathbb{F}^2$**. Given $u = (a, b)$ and $v = (c, d)$ with $u, v$ non-zero and not scalar multiples (so $ad - bc \neq 0$), every vector $(x, y) \in \mathbb{F}^2$ can be written as $\alpha u + \beta v$ by solving a $2 \times 2$ linear system. The decision is to compute this explicitly using Cramer's rule (or by direct substitution) — the cleanest argument anticipates the determinant of [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] without naming it.

---

# Legal Operations Used

1. **Case analysis on a subspace by what it contains.** From the topic page's legal operations: a subspace is determined by whether it contains nonzero vectors and how many "independent" ones. We split into $U = \{0\}$, $U$ a single line, and $U$ containing two non-parallel vectors.

2. **Take the span of a nonzero vector $v$ and observe $\operatorname{span}(v) \subseteq U$.** A subspace containing $v$ contains every $\lambda v$ by closure under scalar multiplication.

3. **Solve a $2 \times 2$ linear system to extract coefficients.** Given $u, v \in \mathbb{F}^2$ non-parallel and an arbitrary target $w \in \mathbb{F}^2$, find scalars $\alpha, \beta$ with $\alpha u + \beta v = w$. This is the concrete computation that shows two non-parallel vectors span the whole plane.

4. **Use "$u, v$ non-parallel" via the determinant condition $ad - bc \neq 0$.** Two vectors $(a, b)$ and $(c, d)$ in $\mathbb{F}^2$ are scalar multiples of each other if and only if $ad - bc = 0$. This is the bilinear "non-parallel" condition.

---

# Hints

> [!note]- Hint 1
> Split into three cases based on $U$: $U = \{0\}$, $U$ contains a nonzero vector but only "one direction's worth", $U$ contains two non-parallel directions.

> [!note]- Hint 2
> If $U$ is a nontrivial subspace, choose a nonzero $v \in U$. Then $\operatorname{span}(v) \subseteq U$ (by closure under scalar multiplication). If $U = \operatorname{span}(v)$, we are in the "line through origin" case.

> [!note]- Hint 3
> If $U \neq \operatorname{span}(v)$, there is some $w \in U$ with $w \notin \operatorname{span}(v)$ — i.e. $w$ is not a scalar multiple of $v$.

> [!note]- Hint 4
> Show that $\{v, w\}$ with $v, w$ non-parallel spans all of $\mathbb{F}^2$: given any $(x, y) \in \mathbb{F}^2$, find scalars $\alpha, \beta$ with $\alpha v + \beta w = (x, y)$.

> [!note]- Hint 5
> Writing $v = (a, b)$ and $w = (c, d)$, the system $\alpha a + \beta c = x$, $\alpha b + \beta d = y$ has a unique solution iff $ad - bc \neq 0$. Non-parallel of $v, w$ exactly means $ad - bc \neq 0$.

---

# Solution

The proof partitions subspaces of $\mathbb{F}^2$ by what they contain. Step 1 dispenses with the trivial case $U = \{0\}$. Step 2 handles $U \neq \{0\}$ by picking a nonzero $v \in U$, which forces $\operatorname{span}(v) \subseteq U$. Step 3 handles the remaining case $U \supsetneq \operatorname{span}(v)$ by picking a witness $w \in U \setminus \operatorname{span}(v)$ and showing $\{v, w\}$ spans all of $\mathbb{F}^2$, forcing $U = \mathbb{F}^2$.

**Step 1: If $U = \{0\}$, then $U$ is the trivial subspace.**

> [!note]- Derivation
> This case is immediate: $\{0\}$ is a subspace (contains $0$, trivially closed under addition and scalar multiplication), and is listed among the candidates.

**Step 2: If $U \neq \{0\}$ contains $v \neq 0$, then $\operatorname{span}(v) \subseteq U$.**

> [!note]- Derivation
> Take $v \in U$ with $v \neq 0$. Since $U$ is closed under scalar multiplication, $\lambda v \in U$ for every $\lambda \in \mathbb{F}$. So $\operatorname{span}(v) = \{\lambda v : \lambda \in \mathbb{F}\} \subseteq U$.
>
> If $U = \operatorname{span}(v)$, we are done — $U$ is a line through the origin. Otherwise there exists $w \in U$ with $w \notin \operatorname{span}(v)$.

**Step 3: If $U$ contains a nonzero $v$ and some $w \notin \operatorname{span}(v)$, then $U = \mathbb{F}^2$.**

We show $\{v, w\}$ spans $\mathbb{F}^2$, hence so does any subspace containing both.

> [!note]- Derivation
> Write $v = (a, b)$ and $w = (c, d)$ in $\mathbb{F}^2$.
>
> First we observe that $w \notin \operatorname{span}(v)$ implies $ad - bc \neq 0$. Indeed, if $ad - bc = 0$, then either $v = 0$ (excluded by $v \neq 0$) or there is a scalar $\lambda$ with $w = \lambda v$. To see the second case: $ad = bc$ and $v \neq 0$ means at least one of $a, b$ is nonzero. If $a \neq 0$, set $\lambda = c/a$; then $\lambda a = c$ and $\lambda b = bc/a = ad/a = d$, so $w = \lambda v$. If instead $a = 0$ but $b \neq 0$, set $\lambda = d/b$; then $\lambda a = 0 = c$ (since $a = 0$ and $ad = bc$ force $bc = 0$, hence $c = 0$) and $\lambda b = d$, so again $w = \lambda v$. Either way, $ad - bc = 0$ forces $w \in \operatorname{span}(v)$, contradicting our assumption. Hence $ad - bc \neq 0$.
>
> Now take an arbitrary $(x, y) \in \mathbb{F}^2$. We solve $\alpha v + \beta w = (x, y)$, i.e.
> $$\alpha a + \beta c = x, \qquad \alpha b + \beta d = y.$$
> Since $ad - bc \neq 0$, the system has the unique solution
> $$\alpha = \frac{xd - yc}{ad - bc}, \qquad \beta = \frac{ya - xb}{ad - bc}$$
> (Cramer's rule, or check by substitution: $\alpha a + \beta c = \frac{(xd - yc)a + (ya - xb)c}{ad - bc} = \frac{xad - yac + yac - xbc}{ad - bc} = \frac{x(ad - bc)}{ad - bc} = x$, and similarly for the second equation).
>
> So $(x, y) = \alpha v + \beta w$ with $\alpha, \beta \in \mathbb{F}$. Since $v, w \in U$ and $U$ is a subspace, $\alpha v + \beta w \in U$. Hence $(x, y) \in U$ for every $(x, y) \in \mathbb{F}^2$, so $U = \mathbb{F}^2$.

> [!note]- Complete formal solution
> **Claim.** The subspaces of $\mathbb{F}^2$ are exactly $\{0\}$, every line $\operatorname{span}(v)$ for $v \in \mathbb{F}^2 \setminus \{0\}$, and $\mathbb{F}^2$ itself.
>
> *Proof.* All three families are subspaces: $\{0\}$ trivially, $\operatorname{span}(v) = \{\lambda v\}$ by direct verification of closure, and $\mathbb{F}^2$ is a subspace of itself.
>
> Conversely, let $U \subseteq \mathbb{F}^2$ be a subspace. If $U = \{0\}$ we are done. Otherwise pick $v \in U$ with $v \neq 0$. By closure under scalar multiplication, $\operatorname{span}(v) \subseteq U$. If $U = \operatorname{span}(v)$, we are done.
>
> If $U \neq \operatorname{span}(v)$, choose $w \in U \setminus \operatorname{span}(v)$. Write $v = (a, b)$ and $w = (c, d)$. We claim $ad - bc \neq 0$: otherwise, since at least one of $a, b$ is nonzero (as $v \neq 0$), one of $c = (c/a) a, d = (c/a) b$ (if $a \neq 0$) or $c = (d/b)\cdot 0 = 0, d = (d/b) b$ with the constraint $bc = ad = 0$ giving $c = 0$ (if $a = 0, b \neq 0$) — in either case $w = \lambda v$ for an appropriate $\lambda$, contradicting $w \notin \operatorname{span}(v)$.
>
> Given $ad - bc \neq 0$, for any $(x, y) \in \mathbb{F}^2$ set
> $$\alpha = \frac{xd - yc}{ad - bc}, \qquad \beta = \frac{ya - xb}{ad - bc}.$$
> Direct substitution gives $\alpha v + \beta w = (x, y)$. So $(x, y) = \alpha v + \beta w \in U$ by closure under linear combinations. Hence $U = \mathbb{F}^2$.
>
> In each case $U$ is one of the three listed types. $\blacksquare$

> [!warning] Illegal but tempting: invoking "dimension" as if defined
> A common shortcut: "$U$ is a subspace of $\mathbb{F}^2$ so $\dim U \in \{0, 1, 2\}$; the dimensions correspond to the three listed types." This is correct *after* dimension is defined and the relevant theorems are proved (see [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]). Within Chapter 1, dimension has not been introduced; using it would be a forward-reference. The proof here is the direct, dimension-free version.

---

# Key Takeaways

**Low-dimensional subspaces are classified by their "direction count".** $\mathbb{F}^2$ has only three sizes of subspace — zero-dimensional ($\{0\}$), one-dimensional (a line through the origin), and two-dimensional (all of $\mathbb{F}^2$) — and the classification is by which "directions" the subspace contains. A one-dimensional subspace contains scalar multiples of a single nonzero vector; a two-dimensional one contains scalar multiples of two non-parallel vectors. The pattern generalizes to higher dimensions: subspaces of $\mathbb{F}^n$ are classified by their dimension, $0, 1, 2, \dots, n$, with the $k$-dimensional subspaces forming an algebraic variety called the *Grassmannian* $\operatorname{Gr}(k, n)$. The dimension count is a complete invariant for "type of subspace" up to the action of $\operatorname{GL}_n(\mathbb{F})$.

**The determinant $ad - bc$ is the algebraic test for "two vectors span $\mathbb{F}^2$".** The condition $ad - bc \neq 0$ that arose in the proof is the **determinant** of the $2 \times 2$ matrix with columns $v, w$. It is the algebraic obstruction to one of the vectors being a scalar multiple of the other, and is the simplest example of the determinant as a "non-vanishing test for linear independence". The same role is played in higher dimensions by the $n \times n$ determinant: $n$ vectors in $\mathbb{F}^n$ span the whole space iff the determinant of the matrix they form is nonzero. We are previewing the determinant of [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] in its simplest manifestation. Recognizing the determinant in disguise — wherever a $2 \times 2$ or $n \times n$ system has a unique solution iff a particular polynomial in the coefficients is nonzero — is the start of the bridge into multilinear algebra.

**Cramer's rule is the constructive form of "non-degenerate $\Rightarrow$ uniquely solvable".** The explicit formulae $\alpha = (xd - yc)/(ad - bc)$, $\beta = (ya - xb)/(ad - bc)$ are the $2 \times 2$ case of *Cramer's rule*. They compute the coefficients of a target vector in a non-parallel basis, by inverting the matrix and reading off the answer. The formula is rarely the most efficient computational route (Gaussian elimination wins in higher dimensions), but it is the cleanest *theoretical* expression of "if the determinant is nonzero, the solution is a rational function of the input". Cramer's rule will return in [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] as a corollary of multilinearity of the determinant.

**The classification is the geometric content of "every two-dimensional subspace is a plane through the origin".** In high school we are told that a "plane through the origin" in $\mathbb{R}^3$ has the form $ax + by + cz = 0$. The classification result here is the algebraic skeleton of that intuition, in one less dimension. Lines through the origin in $\mathbb{R}^2$ have the form $bx - ay = 0$ (passing through the origin in the direction $(a, b)$), and that one-parameter family is exhaustive. The geometric picture — "lines through the origin and nothing else" — is correctly captured by the subspace axioms, and is the source of the slogan "subspaces are flat objects through the origin". The exercise verifies, by direct calculation, that the algebra matches the geometry exactly for $n = 2$.

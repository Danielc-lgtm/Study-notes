---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Polynomial over a Field"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $F$ is a field, usually $\mathbb{R}$ or $\mathbb{C}$, and $F[x] = \mathcal{P}(F)$ is the polynomial ring. For $p, s \in F[x]$ with $s \neq 0$, the goal of the division algorithm is to write $p = sq + r$ with $\deg r < \deg s$; the polynomial $q$ is the **quotient** and $r$ is the **remainder**. A polynomial $p$ **divides** $q$, written $p \mid q$, if $q = ps$ for some $s \in F[x]$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

This is a compound page: it defines the **division algorithm**, the **divisibility relation**, the consequence that **a polynomial is determined by its zeros up to multiplicity**, and the **factorization** of polynomials over $\mathbb{C}$ and over $\mathbb{R}$ — these are introduced together as the structural consequences of the division algorithm.

---

# Axiom Motivation

We want to extend the arithmetic of integers — division with remainder, unique factorization into primes — to polynomials over a field. The motivation is partly cosmetic and partly structural. Cosmetically, polynomials *look* like a generalisation of integers: degree $\deg p$ behaves like absolute value $|n|$, the constant polynomials behave like units in $\mathbb{Z}$ (the units, in fact, in $F[x]$ are exactly the nonzero constants, just as the units in $\mathbb{Z}$ are $\pm 1$), and one expects unique factorisation into "primes" — the analogues of primes in $F[x]$ being the **irreducible polynomials**, those that cannot be written as a product of two polynomials of strictly smaller positive degree.

Structurally, the motivation is that we need a tool to *constrain* polynomials. We have a polynomial $p$, and we know something about it — that some specific $\lambda \in F$ is a zero, say. What does this constrain about $p$? Without the division algorithm we know almost nothing — only that $p(\lambda) = 0$. With it, we can write $p = (x - \lambda) q + r$, where $\deg r < \deg(x - \lambda) = 1$, so $r$ is a constant. Evaluating at $\lambda$ gives $0 = p(\lambda) = 0 \cdot q(\lambda) + r$, hence $r = 0$, hence $(x - \lambda)$ divides $p$. So knowing one zero of $p$ extracts one linear factor.

This is the entire content of the division algorithm in microcosm. The technical statement — "for any nonzero divisor $s$, we can divide with remainder of degree less than $\deg s$" — is the engine. Its applications are uniform: a polynomial constraint becomes a factorisation, a factorisation reduces the degree, and induction on degree finishes the proof. The proof of the **fundamental theorem of algebra** for $\mathbb{C}$ is the same induction with a base case provided by complex analysis: every nonconstant polynomial has at least one zero in $\mathbb{C}$, peel off one linear factor, induct.

Why must $F$ be a field? Suppose $F$ were merely a ring — say $\mathbb{Z}$. Can we still divide? Try $p(x) = x^2$ divided by $s(x) = 2x$. The leading-coefficient cancellation in the standard polynomial-division algorithm requires dividing $1$ (the leading coefficient of $p$) by $2$ (the leading coefficient of $s$), and $2$ is not a unit in $\mathbb{Z}$. So the division gets stuck. The field hypothesis is exactly what ensures that the leading coefficient of $s$ is invertible, so we can subtract a multiple of $s$ from $p$ to kill the leading term of $p$.

Why does the **remainder** have to satisfy $\deg r < \deg s$ — rather than, say, $\deg r \leq \deg s$? Because uniqueness of $q$ and $r$ fails otherwise. With the strict inequality, $q$ and $r$ are uniquely determined by $p$ and $s$ (any two decompositions differ by something of degree less than $\deg s$ that is also a multiple of $s$, hence zero). With a weak inequality, you could add $s$ to $r$ and subtract $1$ from the leading coefficient of $q$ — infinitely many decompositions. The strict inequality picks out a unique "canonical form" for the remainder.

What if the divisor $s$ is the zero polynomial? Then division is undefined, just as division by zero is undefined in any field. The condition $s \neq 0$ is part of the statement.

A subtle point about factorization: over $F = \mathbb{C}$, the **fundamental theorem of algebra** says every nonconstant polynomial has *at least one* zero, hence (by the lemma above) at least one linear factor; inducting on degree, every polynomial factors completely into linear factors. Over $F = \mathbb{R}$, the FTA fails — $x^2 + 1$ has no real zero. What survives is that nonreal zeros come in **complex conjugate pairs** (because the coefficients of a real polynomial are fixed by conjugation), and a pair $(\lambda, \overline\lambda)$ gives the real factor $(x - \lambda)(x - \overline\lambda) = x^2 - 2\operatorname{Re}(\lambda) x + |\lambda|^2$, an irreducible quadratic. So every real polynomial factors into linear and irreducible-quadratic factors.

Why state both the complex and real versions? Because the same operator $T$ on a real vector space and on its complexification has the same minimal polynomial as a real polynomial, but its eigenvalues live in $\mathbb{C}$. The real factorization tells us how many real eigenvalues and how many complex-conjugate pairs there are; the complex factorization tells us the full eigenvalue picture if we extend scalars. Both views are needed in the proof that operators on odd-dimensional real spaces have eigenvalues (see [[Ex - Operators on real odd-dimensional spaces have eigenvalues]]): the minimal polynomial, as a real polynomial of degree $\dim V$ odd, must factor into linear and quadratic real factors; an odd-degree polynomial must have at least one linear factor; that linear factor produces a real eigenvalue.

---

# The Definition

**Division algorithm.** For any $p, s \in F[x]$ with $s \neq 0$, there exist **unique** polynomials $q, r \in F[x]$ such that
$$p = sq + r, \qquad \deg r < \deg s.$$
The proof — and the further consequences listed below — are the content of [[Thm - Division Algorithm for Polynomials (LA)]].

**Divisibility.** Given $p, q \in F[x]$, we say $p$ **divides** $q$ (written $p \mid q$) if there is $s \in F[x]$ with $q = ps$. Equivalently, the remainder when $q$ is divided by $p$ is zero. The relation is reflexive ($p \mid p$), transitive ($p \mid q$ and $q \mid r$ imply $p \mid r$), and **antisymmetric up to units**: if $p \mid q$ and $q \mid p$, then $p$ and $q$ differ by multiplication by a unit (a nonzero constant in $F$). Among monic polynomials, divisibility is antisymmetric on the nose.

**Factor theorem.** For $p \in F[x]$ and $\lambda \in F$:
$$\lambda \text{ is a zero of } p \quad\Longleftrightarrow\quad (x - \lambda) \text{ divides } p.$$

**Zero-count bound.** A nonzero polynomial $p \in F[x]$ of degree $m$ has at most $m$ distinct zeros in $F$. (Each zero contributes a linear factor, and factor degrees add to give $\deg p$.)

**Fundamental theorem of algebra (first version).** Every nonconstant polynomial $p \in \mathbb{C}[x]$ has at least one zero in $\mathbb{C}$.

**Factorization over $\mathbb{C}$.** Every nonconstant polynomial $p \in \mathbb{C}[z]$ factors as
$$p(z) = c(z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m),$$
where $c \in \mathbb{C}$ is the leading coefficient and $\lambda_1, \ldots, \lambda_m \in \mathbb{C}$ are the zeros of $p$ (with repetition reflecting multiplicity). The factorization is unique up to the order of the factors.

**Factorization over $\mathbb{R}$.** Every nonconstant polynomial $p \in \mathbb{R}[x]$ factors uniquely (up to order) as
$$p(x) = c(x - \lambda_1) \cdots (x - \lambda_m)(x^2 + b_1 x + c_1) \cdots (x^2 + b_M x + c_M),$$
where $c, \lambda_i, b_j, c_j \in \mathbb{R}$ and each quadratic factor satisfies the irreducibility condition $b_j^2 < 4c_j$.

**Multiplicity.** The **multiplicity** of a zero $\lambda$ of $p$ is the largest integer $k$ such that $(x - \lambda)^k$ divides $p$. Equivalently, it is the number of times $\lambda$ appears in the factorization above. The sum of multiplicities of all zeros (in the appropriate field) equals $\deg p$.

---

# Categorical / Structural Definition

The division algorithm is the content of the assertion that **$F[x]$ is a [[Def - Euclidean Domain|Euclidean domain]]** with Euclidean function $\deg$. Euclidean domains form a class of rings — those equipped with a division-with-remainder operation satisfying a degree-like estimate — and the class is closed downward into [[Def - Principal Ideal Domain|principal ideal domains]] and [[Def - Unique Factorization Domain|unique factorization domains]]:
$$\text{Field} \;\subset\; \text{Euclidean domain} \;\subset\; \text{PID} \;\subset\; \text{UFD} \;\subset\; \text{Integral domain}.$$
$F[x]$ enters this hierarchy at the Euclidean-domain level, and its membership is the structural reason for everything in the present chapter: PIDness gives existence and uniqueness of the [[Def - Minimal Polynomial|minimal polynomial]], and UFDness gives the **factorization theorems** above as instances of unique factorization into irreducibles.

The factor theorem itself has a clean categorical reading: it says the evaluation ring homomorphism $\operatorname{ev}_\lambda : F[x] \to F$, $p \mapsto p(\lambda)$, has kernel exactly $(x - \lambda)$. By the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]], $F[x]/(x - \lambda) \cong F$, which is a field — so the ideal $(x - \lambda)$ is **maximal** in $F[x]$. In fact every maximal ideal of $F[x]$ has the form $(p)$ for $p$ a monic irreducible polynomial, by the PID structure, and the residue field $F[x]/(p)$ is a field extension of $F$ of degree $\deg p$. So the factorization theorems over $\mathbb{C}$ and $\mathbb{R}$ are statements about the **prime ideals** of the polynomial rings $\mathbb{C}[x]$ and $\mathbb{R}[x]$: $\mathbb{C}[x]$ has prime ideals only of the form $(z - \lambda)$, all maximal of residue field $\mathbb{C}$, whereas $\mathbb{R}[x]$ also has primes of the form $(x^2 + bx + c)$ with $b^2 < 4c$, maximal of residue field $\mathbb{C}$.

---

# Relate to Other Fields / Compression

**True name.** The division algorithm is the **degree-decrease principle**: dividing by anything of positive degree produces a strictly smaller (in degree) remainder, so division-and-remainder iterates terminate. This is the content shared with integer division (where divisibility-and-remainder produces a strictly smaller absolute value) and is what makes both $\mathbb{Z}$ and $F[x]$ amenable to the **Euclidean algorithm** for GCDs.

The fundamental theorem of algebra is *not* a fact of pure algebra. Every honest proof requires some analysis: Liouville's theorem on bounded entire functions, the intermediate value theorem applied to the modulus, or the topology of $\mathbb{C}$. This is the place where the structure of $\mathbb{C}$ as an *analytic* object — the completeness of the reals, the topology of the plane — enters linear algebra. The FTA is a property of the field $\mathbb{C}$ specifically; the analogous algebraic structure (an **algebraically closed field**) is defined to make exactly this statement true, and $\mathbb{C}$ is the smallest algebraically closed field containing $\mathbb{R}$.

In **number theory**, the integer analogue of the factor theorem is **CRT** ([[Thm - Chinese Remainder Theorem for Modules|Chinese Remainder Theorem]]): the residue rings $\mathbb{Z}/(n)$ for coprime $n$ multiply factorise as products. The polynomial CRT — over $F[x]$ — says $F[x]/(f_1 \cdots f_k) \cong \prod F[x]/(f_i)$ when the $f_i$ are pairwise coprime, and this is the engine behind the [[Thm - Generalized Eigenspace Decomposition|primary decomposition of an operator]] over $\mathbb{C}$: the minimal polynomial factors into coprime prime-power parts, and the corresponding decomposition of $V$ is direct.

In **algebraic number theory**, the factor theorem and the FTA together imply that every algebraic number has a [[Def - Algebraic Integer and Minimal Polynomial|minimal polynomial]], the monic generator of the kernel of $\mathbb{Q}[x] \to \mathbb{C}$, $p \mapsto p(\alpha)$. This is the same PID-generator construction as for operators, in a different setting.

---

# Examples / Corollaries

**Long division: $p(x) = x^3 - 2x + 1$, $s(x) = x - 1$.** Dividing, $x^3 - 2x + 1 = (x - 1)(x^2 + x - 1) + 0$. So $1$ is a zero of $p$ (verify: $1 - 2 + 1 = 0$) and $(x-1)$ divides $p$. The quotient $x^2 + x - 1$ has zeros $\frac{-1 \pm \sqrt 5}{2}$ (the golden ratio and its conjugate).

**The factor theorem gives at most $\deg p$ roots, never more.** The polynomial $x^2 - 5x + 6 \in \mathbb{R}[x]$ has zeros $2$ and $3$. By the factor theorem, both $(x - 2)$ and $(x - 3)$ divide $x^2 - 5x + 6$; combined with the degree-additivity of multiplication, the polynomial must equal $(x - 2)(x - 3)$ up to a constant — and being monic, equal exactly. *Calibration:* a polynomial of degree $m$ is **determined** by any $m + 1$ of its values, because the difference between two candidates would have $m + 1$ zeros but degree $\leq m$.

**Factorization over $\mathbb{C}$, not $\mathbb{R}$: $x^4 + 1$.** Over $\mathbb{R}$, this factors as $(x^2 + \sqrt 2 x + 1)(x^2 - \sqrt 2 x + 1)$ — two irreducible quadratics. Over $\mathbb{C}$, each quadratic splits further into two linear factors, and one finds $x^4 + 1 = \prod_{k=0}^3 (x - \zeta_k)$ where $\zeta_k = e^{i(\pi/4 + k\pi/2)}$ are the four primitive eighth roots of unity. The same polynomial factors with $2$ irreducible factors over $\mathbb{R}$ and $4$ linear factors over $\mathbb{C}$.

**Non-example: degrees do not always add over rings with zero divisors.** In $\mathbb{Z}/(6)[x]$, the polynomials $2x + 1$ and $3x + 1$ multiply to $6x^2 + 5x + 1 = 5x + 1$, which has degree $1$, not $2$. The reason is that $\mathbb{Z}/(6)$ has zero divisors ($2 \cdot 3 = 0$), so the product of leading coefficients can vanish. This shows the field hypothesis is essential to the entire structure: over a ring with zero divisors, even $\deg(pq) = \deg p + \deg q$ can fail.

**Non-example: $x^2 + 1$ over $\mathbb{F}_2$.** The polynomial $x^2 + 1 \in \mathbb{F}_2[x]$ has $1$ as a zero, since $1 + 1 = 0$ in $\mathbb{F}_2$. The factor theorem gives $(x - 1) = (x + 1)$ as a factor, and one can check $x^2 + 1 = (x + 1)^2$ in $\mathbb{F}_2[x]$. The factorisation involves a repeated linear factor — this is characteristic of $\mathbb{F}_p[x]$ in characteristic $p$ and is the source of the failure of the "polynomial = function" identification mentioned in [[Def - Polynomial over a Field]].

**Corollary: the formal derivative.** Differentiation as a formal operation $D: F[x] \to F[x]$, $\sum a_k x^k \mapsto \sum k a_k x^{k-1}$, is well-defined for any field $F$. A zero $\lambda$ of $p$ has multiplicity $\geq 2$ if and only if $\lambda$ is also a zero of $Dp$. *Calibration check:* this gives a quick test for repeated roots without computing all the roots — compute $\gcd(p, Dp)$ via the Euclidean algorithm, and any zero of this GCD is a repeated zero of $p$.

**Calibration check.** If you have understood the definition, you should be able to verify quickly: (a) the factor theorem in one direction by direct computation (a linear factor $(x - \lambda)$ forces $p(\lambda) = 0$ by evaluating the product); (b) that $\deg p$ is well-defined (the coefficient sequence is unique by the polynomial-equality convention); (c) that $x^3 + 1 \in \mathbb{R}[x]$ has exactly one real root ($\lambda = -1$) and so factors as $(x + 1)(x^2 - x + 1)$, with the quadratic factor irreducible since its discriminant $1 - 4 = -3 < 0$.

---

# Unlocked by This

> [!tip] The Polynomial Ring as a PID *(from Rings II)*
> The division algorithm is exactly the [[Def - Euclidean Domain|Euclidean]] structure on $F[x]$. Every Euclidean domain is a PID (by the [[Thm - Euclidean Domains are Principal Ideal Domains|theorem]] of that name), so every ideal of $F[x]$ is principal — generated by a single polynomial. This is the algebraic backbone of the existence and uniqueness of the [[Def - Minimal Polynomial|minimal polynomial]] of an operator, which is the monic generator of an ideal of $F[x]$.

> [!tip] Unique Factorization into Irreducibles *(from Rings II–III)*
> Combined with the PID property, the division algorithm gives unique factorization into irreducibles: every nonconstant polynomial $p \in F[x]$ factors as $c p_1^{a_1} \cdots p_k^{a_k}$ with $c \in F^\times$, $p_i$ distinct monic irreducibles, $a_i \geq 1$, and the factorization is unique up to reordering. See [[Thm - Principal Ideal Domains are Unique Factorization Domains]].

> [!tip] Galois Theory and the Solvability of Polynomial Equations *(from Galois Theory)*
> The factorization theorems over $\mathbb{C}$ and $\mathbb{R}$ are specific cases of a much deeper question: given a polynomial $p \in F[x]$, what is its **splitting field** — the smallest extension of $F$ in which $p$ factors into linear factors? Galois theory studies the symmetry group of this splitting field over $F$, and the **Abel-Ruffini theorem** says that the general degree-5 polynomial cannot be solved by radicals because its symmetry group is the non-solvable $S_5$. The fact that we can write down explicit formulas for the roots of degree $\leq 4$ polynomials and not for degree $\geq 5$ is, structurally, a fact about the solvability of small symmetric groups.

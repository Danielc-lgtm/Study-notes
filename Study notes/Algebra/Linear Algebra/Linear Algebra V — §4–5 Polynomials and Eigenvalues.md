---
type: topic
subject: linear-algebra
chapter: "4-5"
title: "Linear Algebra V — Polynomials, Eigenvalues, and the Minimal Polynomial"
tags: [algebra, linear-algebra]
---

# Notation Registry

Throughout this topic, $F$ denotes a field, usually $\mathbb{R}$ or $\mathbb{C}$, and $V$ is a finite-dimensional vector space over $F$. An **operator** on $V$ is a linear map $V \to V$; the space of all such operators is $\mathcal{L}(V)$. The polynomial ring $F[x]$ — the ring of polynomials in one indeterminate with coefficients in $F$ — appears throughout.

- $V$, $W$ — finite-dimensional vector spaces over $F$; almost always $\dim V = n$
- $T \in \mathcal{L}(V)$ — an operator on $V$, i.e. a linear map $V \to V$
- $I$ — the identity operator on $V$; sometimes $\operatorname{id}_V$
- $T - \lambda I$ — the operator $v \mapsto Tv - \lambda v$, central to eigenvalue theory
- $\lambda$, $\mu$ — eigenvalues (elements of $F$)
- $v$, $w$ — vectors; an **eigenvector** is a nonzero $v$ with $Tv = \lambda v$ for some $\lambda$
- $E(\lambda, T) = \ker(T - \lambda I)$ — the **eigenspace** for $\lambda$
- $\mathcal{P}(F)$ or $F[x]$ — the polynomial ring over $F$; $\mathcal{P}_m(F)$ — polynomials of degree at most $m$
- $p(T)$ — the operator $\sum a_k T^k$ obtained by substituting $T$ into $p(x) = \sum a_k x^k$
- $\deg p$ — the degree of a polynomial $p$
- $T^0 = I$, $T^m = T \circ T \circ \cdots \circ T$ ($m$ factors), $T^{-m} = (T^{-1})^m$ when $T$ is invertible
- $m_T$ or $p_T$ — the **minimal polynomial** of $T$, the unique monic polynomial of smallest degree with $p(T) = 0$
- $\operatorname{span}(v_1, \ldots, v_k)$ — the linear span of a list
- A subspace $U \leq V$ is **invariant under $T$** if $T(U) \subseteq U$
- $\mathbb{C}$, $\mathbb{R}$ — the complex and real numbers
- $\mathcal{M}(T)$ — the matrix of $T$ with respect to an understood basis

**Standing convention.** All vector spaces in this topic are finite-dimensional. When a result requires a specific field — $\mathbb{C}$ for the existence of eigenvalues, for instance — this is stated explicitly. The behaviour of operators on real and complex vector spaces is genuinely different in this chapter, and the difference is always traced back to a single source: the fundamental theorem of algebra holds over $\mathbb{C}$ and fails over $\mathbb{R}$.

---

# Motivation

Here is the entire topic in one sentence: an operator $T$ on $V$ is the same data as an action of the polynomial ring $F[x]$ on $V$, and the structural invariants of $T$ — its eigenvalues, its invariant subspaces, its matrix forms — are the structural invariants of $V$ viewed as an $F[x]$-module. The polynomial $x$ acts as $T$; the polynomial $x^2 + 3x + 7$ acts as $T^2 + 3T + 7I$; and the question "what does $T$ do?" becomes "what is the structure of $V$ as a module over $F[x]$?". This is the deep reason every theorem in this chapter is about polynomials, even though the apparent subject is linear maps.

The chapter has two halves. **Chapter 4** is a self-contained mini-course on the polynomial ring $F[x]$: degree, the division algorithm, the fundamental theorem of algebra, factorization over $\mathbb{C}$ and over $\mathbb{R}$. Most of this is familiar from elementary algebra, but it is collected here because every result in Chapter 5 quotes it. The division algorithm in particular is the engine: it is what makes $F[x]$ a Euclidean domain, hence a principal ideal domain, and the principal-ideal property is what guarantees the existence of the minimal polynomial.

**Chapter 5** is the geometry of an operator. The simplest non-trivial invariant subspace of $T$ is one-dimensional, and a one-dimensional invariant subspace is exactly a line through the origin that $T$ sends into itself — equivalently, a nonzero vector $v$ with $Tv = \lambda v$ for some scalar $\lambda$. That scalar is an **eigenvalue**, and the vector an **eigenvector**. The first question — does $T$ have any one-dimensional invariant subspaces at all? — is the central question of the chapter, and the answer is the famous

$$\boxed{\text{Every operator on a finite-dimensional nonzero complex vector space has an eigenvalue.}}$$

The proof, due in this form to Axler, avoids determinants entirely. It uses only the polynomial ring and the fundamental theorem of algebra. The argument is so important that it organises everything else in the chapter. From a single nonzero vector $v \in V$, form the list $v, Tv, T^2v, \ldots, T^nv$ — that is $n+1$ vectors in an $n$-dimensional space, so they are linearly dependent, and a nontrivial relation $a_0 v + a_1 Tv + \cdots + a_n T^n v = 0$ rearranges to $p(T)v = 0$ for some nonzero polynomial $p$. Factor $p$ over $\mathbb{C}$ as $c(x - \lambda_1) \cdots (x - \lambda_k)$. Then $(T - \lambda_1 I) \cdots (T - \lambda_k I) v = 0$, so at least one factor has nonzero kernel, and that produces an eigenvalue.

Two things in this argument generalise. First, the polynomial $p$ that annihilates $T$ on the vector $v$ — and, taking $v$ to vary, on all of $V$ — is the **minimal polynomial** $m_T$ of $T$. Its existence, uniqueness, and meaning are the content of §5B. The minimal polynomial is the **monic generator of the principal ideal** $\{p \in F[x] : p(T) = 0\}$, which is the kernel of the evaluation map $F[x] \to \mathcal{L}(V)$, $p \mapsto p(T)$. The minimal polynomial is therefore the right "true name" of the operator: it is the simplest polynomial relation $T$ satisfies, and every other polynomial relation factors through it.

Second, the trick of factoring an annihilating polynomial generalises into a method for **simplifying the matrix of $T$**. If the minimal polynomial of $T$ factors over $F$ into linear factors, then $V$ admits a basis with respect to which the matrix of $T$ is **upper triangular** (§5C). If the minimal polynomial factors into *distinct* linear factors, the matrix is **diagonal** — $T$ is **diagonalizable** (§5D). Over $\mathbb{C}$ the first condition is always met, so every operator is upper-triangularizable; the second condition is more restrictive, and identifying when it holds is a problem on its own. Finally, **commuting operators** can be simultaneously triangularized and (when they are individually diagonalizable) simultaneously diagonalized (§5E).

The structural backbone of the chapter is therefore a hierarchy:

$$\text{scalar multiple of } I \;\subset\; \text{diagonalizable} \;\subset\; \text{upper-triangularizable} \;\subset\; \text{has an eigenvalue},$$

with the last inclusion being an equality over $\mathbb{C}$, and the chain governed entirely by how the minimal polynomial factors.

**Audience-assumption.** The reader is assumed to have refreshed the vector-space machinery of [[Linear Algebra I — §1 Vector Spaces|Linear Algebra I]] and [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces|Linear Algebra II]] — basis, dimension, direct sum — and the linear-map machinery of [[Linear Algebra III — §3A–D Linear Maps|Linear Algebra III]] — null space, range, matrices, isomorphism, the fundamental theorem of linear maps. The bridge to algebra also requires familiarity with the [[Def - Polynomial Ring|polynomial ring]] and the notion of a [[Def - Principal Ideal Domain|principal ideal domain]] from [[Rings II — §2.3–2.4]]; these connections are sharpest at the [[Def - The Module of a Linear Operator|$F[x]$-module of an operator]] from [[Modules II — §3.3–3.4]], but the present chapter is self-contained in its terminology.

---

# Concept Map

## §4 Polynomials

- **[[Def - Polynomial over a Field]]**
	- A **polynomial** over $F$ is a finite formal expression $p(x) = a_0 + a_1 x + \cdots + a_m x^m$ with coefficients $a_k \in F$; the **degree** $\deg p$ is the largest $k$ with $a_k \neq 0$ (with $\deg 0 = -\infty$ by convention). The set $\mathcal{P}(F) = F[x]$ of all such polynomials is an $F$-vector space, a commutative ring, and — because $F$ is a field — a [[Def - Principal Ideal Domain|principal ideal domain]] via the [[Thm - Division Algorithm for Polynomials (LA)|division algorithm]]. A polynomial is **monic** if its leading coefficient is $1$; this normalisation makes generators of ideals unique. A **zero** or **root** of $p$ is a $\lambda \in F$ with $p(\lambda) = 0$.

- **[[Def - Division Algorithm and Factorization]]**
	- The **division algorithm** says: given $p, s \in F[x]$ with $s \neq 0$, there exist unique $q, r \in F[x]$ with $p = sq + r$ and $\deg r < \deg s$. This is the polynomial analogue of integer division and makes $F[x]$ a Euclidean domain. Factorization consequences: a polynomial of degree $m$ has at most $m$ zeros; over $\mathbb{C}$, every nonconstant polynomial factors as $c(x - \lambda_1) \cdots (x - \lambda_m)$ (fundamental theorem of algebra); over $\mathbb{R}$, every nonconstant polynomial factors into linear and irreducible-quadratic factors.

- **[[Thm - Division Algorithm for Polynomials (LA)]]**
	- For $p, s \in F[x]$ with $s \neq 0$, there exist unique $q, r \in F[x]$ with $p = sq + r$ and $\deg r < \deg s$. The Axler proof is striking: the list $1, x, \ldots, x^{m-1}, s, xs, \ldots, x^{n-m}s$ has $n+1$ elements of distinct degrees, so it is a basis of $\mathcal{P}_n(F)$; the coefficients of $p$ in this basis are exactly the coefficients of $q$ and $r$. This is the engine of the whole chapter: it is what makes $F[x]$ a [[Def - Principal Ideal Domain|PID]], hence what guarantees the [[Thm - Existence and Uniqueness of Minimal Polynomial|minimal polynomial]] exists.

> [!tip] Unlocked: Polynomial Ring as PID *(from Rings II)*
> The division algorithm makes $F[x]$ a [[Def - Principal Ideal Domain|Euclidean domain]] with $\deg$ as the Euclidean function. Every Euclidean domain is a PID. So **every ideal of $F[x]$ is principal**, generated by a single monic polynomial — and this is the *structural* reason the minimal polynomial exists and is unique. See [[Thm - Euclidean Domains are Principal Ideal Domains]] and [[Thm - Principal Ideal Domains are Unique Factorization Domains]].

> [!tip] Unlocked: The Fundamental Theorem of Algebra *(from Complex Analysis)*
> The proof of every-operator-has-an-eigenvalue on $\mathbb{C}$ uses the FTA, and the FTA is itself a theorem of complex analysis — its slickest proof uses Liouville's theorem on bounded entire functions. The marriage between the algebraic chapter you are now reading and the analysis of holomorphic functions is the deepest single fact about $\mathbb{C}$.

> [!note] Exercise Index — §4
> [[Exercise Index - §4 Polynomials]]

## §5A Invariant Subspaces and Eigenvalues

- **[[Def - Invariant Subspace]]**
	- A subspace $U \leq V$ is **invariant under $T$** if $T(U) \subseteq U$ — applying $T$ never escapes $U$. The trivial cases $\{0\}$ and $V$ are always invariant; the interesting question is whether non-trivial invariant subspaces exist. For any operator, $\ker T$, $\operatorname{im} T$, $\ker p(T)$, and $\operatorname{im} p(T)$ for any polynomial $p$ are all invariant under $T$. The simplest possible non-trivial invariant subspaces are one-dimensional — and a one-dimensional invariant subspace is exactly the span of an eigenvector.

- **[[Def - Eigenvalue and Eigenvector]]**
	- A scalar $\lambda \in F$ is an **eigenvalue** of $T \in \mathcal{L}(V)$ if there exists a nonzero vector $v \in V$ with $Tv = \lambda v$; such a $v$ is an **eigenvector** for $\lambda$. The **true name** is geometric: an eigenvector is a nonzero vector whose span is a one-dimensional invariant subspace; an eigenvalue is the scalar by which $T$ acts on that line. Over $\mathbb{R}$, an operator need have no eigenvalues at all (a $90°$ rotation on $\mathbb{R}^2$ has none); over $\mathbb{C}$, every operator on a finite-dimensional nonzero space has at least one.

- **[[Def - Polynomial of an Operator]]**
	- For $T \in \mathcal{L}(V)$ and $p(x) = a_0 + a_1 x + \cdots + a_m x^m \in F[x]$, the operator $p(T) \in \mathcal{L}(V)$ is defined by $p(T) = a_0 I + a_1 T + \cdots + a_m T^m$. The map $p \mapsto p(T)$ is a ring homomorphism $F[x] \to \mathcal{L}(V)$ — addition, scalar multiplication, and multiplication of polynomials match the corresponding operations on operators (with composition as multiplication). In particular $p(T)q(T) = (pq)(T) = (qp)(T) = q(T)p(T)$, so any two polynomials in the *same* operator commute.

- **[[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]]**
	- If $v_1, \ldots, v_m$ are eigenvectors of $T$ corresponding to *distinct* eigenvalues $\lambda_1, \ldots, \lambda_m$, then the list $v_1, \ldots, v_m$ is linearly independent. The proof is a one-step contradiction: take a shortest dependent sublist, apply $T - \lambda_m I$ to kill the last eigenvector, and observe that the result is a strictly shorter dependent sublist, contradicting minimality. Consequence: an operator on $V$ has at most $\dim V$ distinct eigenvalues.

- **[[Ex - The differentiation operator on polynomials has eigenvalue zero only]]** (⭐)
	- Let $D : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$ be $Dp = p'$. Show that $0$ is the only eigenvalue, with eigenvectors the nonzero constants.

- **[[Ex - Operators on real odd-dimensional spaces have eigenvalues]]** (⭐⭐⭐)
	- Show that every operator on a finite-dimensional real vector space of odd dimension has a real eigenvalue. (Axler's polynomial-only proof.)

> [!tip] Unlocked: Spectrum of a Bounded Operator *(from Functional Analysis)*
> The right generalization of "set of eigenvalues" to infinite-dimensional Banach or Hilbert spaces is the **spectrum** $\sigma(T) = \{\lambda \in \mathbb{C} : T - \lambda I \text{ is not invertible}\}$. In finite dimensions the spectrum is exactly the set of eigenvalues, by [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]]. In infinite dimensions an operator can fail to be invertible without having any eigenvectors at all — the forward shift on $\ell^2$ is the standard example — and the spectrum splits into point spectrum (eigenvalues), continuous spectrum, and residual spectrum. Spectral theory is the eigenvalue theory of the infinite-dimensional world, and every theorem in §5 has an analogue there, usually proved by very different means.

> [!note] Exercise Index — §5A–B
> [[Exercise Index - §5A–B Eigenvalues and Minimal Polynomial]]

## §5B The Minimal Polynomial

- **[[Def - Minimal Polynomial]]**
	- The **minimal polynomial** of an operator $T$ on a finite-dimensional space $V$ is the unique monic polynomial $m_T \in F[x]$ of smallest degree such that $m_T(T) = 0$. Equivalently, $m_T$ is the **monic generator of the principal ideal** $\{p \in F[x] : p(T) = 0\} \subseteq F[x]$ — the kernel of the evaluation ring homomorphism $F[x] \to \mathcal{L}(V)$, $p \mapsto p(T)$. Its degree is at most $\dim V$. Existence comes from finite-dimensionality: $I, T, T^2, \ldots, T^{n^2}$ are $n^2 + 1$ vectors in the $n^2$-dimensional space $\mathcal{L}(V)$, so they must be linearly dependent.

- **[[Thm - Existence and Uniqueness of Minimal Polynomial]]**
	- For any $T \in \mathcal{L}(V)$ with $\dim V < \infty$, there is a unique monic polynomial $m_T \in F[x]$ of smallest positive degree with $m_T(T) = 0$, and $\deg m_T \leq \dim V$. The proof is a constructive descent: starting from any nonzero $u \in V$ and the dependent list $u, Tu, \ldots, T^n u$, build a polynomial $q$ with $q(T)u = 0$, then induct on $\dim V$ to extend to all of $V$. Uniqueness is automatic: two minimal monic polynomials would differ by something of smaller degree that still annihilates $T$.

- **[[Thm - Eigenvalues are Zeros of the Minimal Polynomial]]**
	- The zeros of $m_T$ in $F$ are exactly the eigenvalues of $T$. Over $\mathbb{C}$ this gives a complete factorization $m_T(z) = (z - \lambda_1) \cdots (z - \lambda_m)$ with the $\lambda_k$ a list of all eigenvalues, possibly with repetitions. This is the bridge that turns the algebraic object $m_T$ into the geometric data of eigenvalues; combined with the fact that $m_T$ has degree at most $\dim V$, it gives an alternative proof that $T$ has at most $\dim V$ distinct eigenvalues.

- **[[Thm - Existence of Eigenvalues on Complex Vector Spaces]]**
	- Every operator on a finite-dimensional nonzero complex vector space has an eigenvalue. The proof is the marquee argument: from $v, Tv, \ldots, T^n v$ extract a nontrivial polynomial relation $p(T)v = 0$, factor $p$ over $\mathbb{C}$ as $c(z - \lambda_1) \cdots (z - \lambda_k)$, and use that at least one factor $T - \lambda_j I$ must have nonzero kernel. The hypothesis $F = \mathbb{C}$ is used exactly once — to factor $p$ — but it is essential: the rotation by $90°$ on $\mathbb{R}^2$ shows the result fails over $\mathbb{R}$.

- **[[Ex - Minimal polynomial of a diagonal matrix]]** (⭐)
	- Show that the minimal polynomial of a diagonal matrix with diagonal entries $\lambda_1, \ldots, \lambda_n$ (some possibly repeated) is $\prod_{\lambda \in \{\lambda_1, \ldots, \lambda_n\}}(z - \lambda)$ — one factor per *distinct* eigenvalue.

- **[[Ex - Powers of an operator and the minimal polynomial]]** (⭐⭐)
	- If $T^k = I$ for some $k \geq 1$, show that the minimal polynomial of $T$ divides $z^k - 1$. Use this to determine the minimal polynomial of an operator with $T^4 = I$ and no smaller power equal to $I$.

> [!tip] Unlocked: Annihilator Ideal of an $F[x]$-Module *(from Module Theory)*
> The minimal polynomial is the **monic generator of the annihilator** $\operatorname{ann}_{F[x]}(V) = \{p \in F[x] : p \cdot v = 0 \text{ for all } v \in V\}$ when $V$ is viewed as an $F[x]$-module with $x$ acting as $T$ — see [[Def - The Module of a Linear Operator]]. The annihilator is an ideal of $F[x]$, and $F[x]$ being a PID forces it to be principal, hence to have a (unique up to units) generator; making the generator monic picks out the minimal polynomial. This is the structural reason for the minimal polynomial's existence — finite-dimensional linear algebra is module theory over $F[x]$ in disguise, and the **structure theorem for finitely generated modules over a PID** specialises to the Jordan / rational canonical forms.

> [!tip] Unlocked: Algebraic Integer and Minimal Polynomial *(from Algebraic Number Theory)*
> The same construction in a different setting: for an algebraic number $\alpha$ (a complex number satisfying a polynomial equation over $\mathbb{Q}$), the **minimal polynomial of $\alpha$** is the monic generator of the ideal $\{p \in \mathbb{Q}[x] : p(\alpha) = 0\}$. The exact same PID-generator reasoning applies, with $\mathbb{Q}[x]$ in place of $F[x]$. See [[Def - Algebraic Integer and Minimal Polynomial]] and [[Thm - The Minimal Polynomial Generates the Kernel Ideal]] in Rings IV.

## §5C Upper-Triangular Matrices

- **[[Thm - Upper-Triangular Form on Complex Vector Spaces]]**
	- An operator $T$ on $V$ has an upper-triangular matrix with respect to some basis if and only if the minimal polynomial $m_T$ factors into linear factors in $F[x]$. Over $\mathbb{C}$ this is automatic (by the [[Thm - Existence of Eigenvalues on Complex Vector Spaces|fundamental theorem of algebra]]), so every operator on a finite-dimensional complex vector space is upper-triangularizable. The diagonal entries of any such upper-triangular matrix are precisely the eigenvalues of $T$, each appearing the right number of times — this gives an easy proof that the eigenvalues are bounded by entries.

- **[[Ex - Operators with the same minimal polynomial need not be similar]]** (⭐⭐⭐)
	- Give two $4 \times 4$ nilpotent matrices with the same minimal polynomial $z^2$ that are not similar to each other. The example shows the minimal polynomial is *not* a complete invariant of similarity — finer invariants (the elementary divisors, the Jordan blocks) are needed.

> [!tip] Unlocked: Schur Decomposition *(from Numerical Linear Algebra)*
> Schur's theorem is the inner-product-space refinement: every complex matrix is unitarily similar to an upper-triangular matrix, $A = U^* T U$ with $U$ unitary and $T$ upper triangular. The Axler proof of upper-triangularizability picks a basis $v_1, \ldots, v_n$ with $\operatorname{span}(v_1, \ldots, v_k)$ invariant for each $k$; applying Gram–Schmidt to this basis produces the unitary $U$ for Schur. The Schur form is the basis of the QR algorithm, the workhorse of numerical eigenvalue computation.

## §5D Diagonalizable Operators

- **[[Def - Diagonalizable Operator]]**
	- An operator $T$ on $V$ is **diagonalizable** if $V$ has a basis consisting of eigenvectors of $T$ — equivalently, the matrix of $T$ in some basis is diagonal. Equivalent conditions: $V = E(\lambda_1, T) \oplus \cdots \oplus E(\lambda_m, T)$ for the distinct eigenvalues; $\dim V = \sum_k \dim E(\lambda_k, T)$; the minimal polynomial $m_T$ factors as $(z - \lambda_1) \cdots (z - \lambda_m)$ with *distinct* roots. Diagonalizability is the simplest possible structure for an operator, but it is not generic: the upper-triangular non-diagonal matrices form an entire affine variety of non-diagonalizable operators.

- **[[Thm - Conditions for Diagonalizability]]**
	- For $T$ on a finite-dimensional $V$, the following are equivalent: (a) $T$ is diagonalizable; (b) $V$ has a basis of eigenvectors of $T$; (c) $V = E(\lambda_1, T) \oplus \cdots \oplus E(\lambda_m, T)$ for the distinct eigenvalues $\lambda_k$; (d) $\dim V = \sum_k \dim E(\lambda_k, T)$; and **(e) the minimal polynomial $m_T$ is a product of *distinct* linear factors** in $F[x]$. The "distinct linear factors" form (e) is the practical test — it is checkable without finding eigenvectors and gives diagonalizability over $\mathbb{C}$ purely from the minimal polynomial.

- **[[Thm - Gershgorin Disk Theorem]]**
	- Let $T$ have matrix $A$ in some basis. The $j$th **Gershgorin disk** is the closed disk centred at the diagonal entry $A_{j,j}$ with radius $\sum_{k \neq j} |A_{j,k}|$ — the sum of absolute values of the off-diagonal entries in row $j$. Every eigenvalue of $T$ lies in at least one Gershgorin disk. So if the off-diagonal entries are small, the eigenvalues cluster near the diagonal entries; if the diagonal entries are *strictly dominant* (each larger than the sum of absolute values of its off-diagonal row entries), $T$ is invertible. This is the cheapest non-trivial eigenvalue estimate in linear algebra.

> [!tip] Unlocked: Spectral Decomposition *(from Functional Analysis)*
> Diagonalizability is the finite-dimensional prototype of the **spectral theorem**: a normal operator on a Hilbert space is unitarily diagonalizable. In finite dimensions this becomes the [[Linear Algebra VII — §7 Operators on Inner Product Spaces|complex/real spectral theorems]] for self-adjoint and normal operators. In infinite dimensions the diagonal sum becomes a spectral integral: $T = \int_\sigma z \, dE(z)$ against a projection-valued measure $E$. The pattern "decompose $V$ as a direct sum of eigenspaces" is the most reused idea in all of operator theory.

## §5E Commuting Operators

- **[[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]]**
	- In LADR's determinant-free approach, the result usually called the Cayley–Hamilton theorem appears in a slightly different guise: **the minimal polynomial divides every polynomial that annihilates $T$**, and conversely is annihilated by $T$ by definition. The "classical" Cayley–Hamilton — $p_T(T) = 0$ where $p_T$ is the characteristic polynomial — is **essentially tautological** in this framework: once one has the minimal polynomial and (later) the characteristic polynomial, the fact that the minimal polynomial divides the characteristic polynomial is a clean consequence of how both polynomials are built from the eigenvalues with multiplicities. The deeper content lives in the minimal polynomial itself.

- **[[Ex - Commuting operators share an eigenvector on complex spaces]]** (⭐⭐)
	- If $S, T$ are commuting operators on a finite-dimensional nonzero complex vector space, show they have a common eigenvector. (Application: simultaneous upper-triangularization.)

> [!tip] Unlocked: Simultaneous Diagonalization and the Commuting Family Theorem *(from Representation Theory)*
> Any commuting family of diagonalizable operators can be simultaneously diagonalized — there is a single basis in which all members of the family have diagonal matrices. This is the engine for decomposing representations: when a group $G$ acts on $V$ and the action has been arranged to give diagonalizable operators (true for finite groups in characteristic zero, by Maschke), the simultaneous diagonalization gives a decomposition of $V$ into common eigenspaces, which are the **isotypic components** of the representation. The whole subject of representation theory is built on this.

> [!note] Exercise Index — §5C–E
> [[Exercise Index - §5C–E Upper Triangular, Diagonalizable, Commuting Operators]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

Across the exercises in this chapter, the recurring goals are five. The first is **finding the minimal polynomial** of an explicit operator, often given as a matrix or as an action on a specific space (such as the differentiation operator on polynomials). The second is **finding the eigenvalues and eigenvectors**, which once $m_T$ is known reduces to factoring it; eigenvectors come from solving $(T - \lambda I)v = 0$ in each eigenspace. The third is **deciding diagonalizability** — for an operator, deciding whether it admits a basis of eigenvectors, typically by checking whether $m_T$ has distinct linear factors. The fourth is **deciding upper-triangularizability** when the field is not algebraically closed — over $\mathbb{R}$, this is the genuine question, and the test is whether $m_T$ has only linear factors. The fifth is **structural statements about operator classes**: showing that a property holds for every operator of a certain kind, or constructing an operator with prescribed properties. Each of these five is a question with a known route to its answer; the strategy section says which route fits which.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **The field is $\mathbb{C}$** — this unlocks the [[Thm - Existence of Eigenvalues on Complex Vector Spaces|existence-of-eigenvalues theorem]], the factorization of $m_T$ into linear factors, and upper-triangularizability; it is the single most powerful hypothesis in the chapter. **An explicit matrix is given** — this enables a direct computation of $m_T$ by the linear-dependence-of-powers algorithm (find the smallest $m$ with $T^m \in \operatorname{span}(I, T, \ldots, T^{m-1})$). **An operator equation is given**, such as $T^k = I$ or $T^2 = T$ — this immediately says $m_T$ divides the polynomial in the equation, reducing the problem to a finite list of possibilities. **An operator is described as a sum or composition** of operators with known structure — this is the input to the commuting-operators theorems of §5E, which combine known eigenvalues. **A statement is purely structural** — "show that every operator with property $P$ has property $Q$" — and the route is usually to translate $P$ into a constraint on $m_T$ and read $Q$ off the resulting form. The common bridge across all five is that the source funnels into a constraint on the minimal polynomial, which is then read off as the desired structural conclusion. **The minimal polynomial is the universal pivot of the chapter.**

---

# Legal Operations

These are the moves that almost every problem in this topic is assembled from. Each is fully self-contained: a reader with no eigenvalue background should be able to follow each operation from the description alone.

**Legal operations:**

1. **Build a polynomial relation from a dependent list of iterates.** Given any operator $T$ on an $n$-dimensional space $V$ and any nonzero $v \in V$, the list $v, Tv, T^2 v, \ldots, T^n v$ has $n+1$ vectors in an $n$-dimensional space, hence is linearly dependent. The dependence relation $a_0 v + a_1 Tv + \cdots + a_n T^n v = 0$ is exactly $p(T)v = 0$ for the polynomial $p(x) = a_0 + a_1 x + \cdots + a_n x^n$. *Trigger:* anything that asks for an eigenvalue, eigenvector, or polynomial constraint on $T$ when no polynomial is given. *Pattern:* "by finite-dimensionality, the iterates of any nonzero vector are linearly dependent; the dependence gives a polynomial relation in $T$."

2. **Factor an annihilating polynomial to expose an eigenvalue.** If $p(T)v = 0$ for a nonzero $v$ and $p$ factors over $F$ as $p(x) = c(x - \lambda_1) \cdots (x - \lambda_k)$, then $(T - \lambda_1 I) \cdots (T - \lambda_k I) v = 0$, and at least one of the factors $(T - \lambda_j I)$ must have nonzero kernel. That $\lambda_j$ is an eigenvalue. *Trigger:* you have a polynomial relation $p(T) = 0$ or $p(T)v = 0$. *Pattern:* "factor over $F$, then walk the product from right to left until you find the first factor that does not kill the running vector — the next factor is $T - \lambda I$ for an eigenvalue $\lambda$."

3. **Compute the minimal polynomial by the iterate algorithm.** Pick a nonzero $v \in V$ and form $v, Tv, T^2 v, \ldots$; let $m$ be the smallest positive integer for which $T^m v \in \operatorname{span}(v, Tv, \ldots, T^{m-1}v)$. The coefficients of the dependence relation are the coefficients of a candidate minimal polynomial. When $v$ is "generic" (almost always), this candidate *is* the minimal polynomial. *Trigger:* you have a concrete matrix or operator and want $m_T$. *Pattern:* "iterate on a vector until you get a dependence; read the polynomial off the coefficients."

4. **Translate operator equations to divisibility of $m_T$.** Any polynomial relation $p(T) = 0$ forces $m_T$ to *divide* $p$ — this is the content of [[Thm - Existence and Uniqueness of Minimal Polynomial|minimality]] combined with the [[Thm - Division Algorithm for Polynomials (LA)|division algorithm]]. So $T^k = I$ implies $m_T \mid z^k - 1$; $T^2 = T$ implies $m_T \mid z(z - 1)$; $T$ is a projection implies $m_T \in \{z, z - 1, z(z-1)\}$. *Trigger:* the problem gives a polynomial equation in $T$. *Pattern:* "the equation says $p(T) = 0$, so $m_T \mid p$; list the monic divisors of $p$ and choose by additional constraints."

5. **Read eigenvalues off the diagonal of an upper-triangular matrix.** If a basis exists in which $T$ has upper-triangular matrix with diagonal entries $\alpha_1, \ldots, \alpha_n$, the set of eigenvalues of $T$ is exactly $\{\alpha_1, \ldots, \alpha_n\}$ (as a set; multiplicities require care). *Trigger:* you have a triangular matrix. *Pattern:* "the eigenvalues are the diagonal entries; no determinant calculation required."

6. **Diagonalize via the minimal polynomial.** $T$ is diagonalizable if and only if $m_T$ is a product of *distinct* linear factors in $F[x]$. This is the practical test: compute $m_T$, check whether it has repeated roots. *Trigger:* you want to diagonalize an operator or decide whether you can. *Pattern:* "find $m_T$; it has repeated roots iff $T$ is not diagonalizable."

7. **Use Gershgorin disks to bound eigenvalues.** Every eigenvalue of $T$ (with matrix $A$ in some basis) lies in some closed disk centred at a diagonal entry with radius the sum of absolute values of the other row entries. *Trigger:* you have a matrix and want a quick eigenvalue estimate. *Pattern:* "for each row $j$, draw the closed disk of radius $\sum_{k \neq j}|A_{j,k}|$ around $A_{j,j}$; every eigenvalue is in the union of these disks."

8. **Find a common eigenvector for commuting operators.** If $S, T$ on a finite-dimensional nonzero complex vector space satisfy $ST = TS$, then $S$ has an eigenvector, and one of its eigenspaces $E(\lambda, S)$ — being $T$-invariant because $T$ commutes with $S$ — contains an eigenvector of $T|_{E(\lambda, S)}$, which is then a common eigenvector. *Trigger:* the problem states two commuting operators on $\mathbb{C}$. *Pattern:* "pick an eigenspace of one, restrict the other to it, get an eigenvector there."

9. **Restrict to an invariant subspace.** If $U \leq V$ is invariant under $T$, the restriction $T|_U \in \mathcal{L}(U)$ is an operator on $U$ with $m_{T|_U} \mid m_T$. In particular every eigenvalue of $T|_U$ is an eigenvalue of $T$, and the existence-of-eigenvalues theorem applies to $T|_U$. *Trigger:* you have a $T$-invariant subspace and want to use induction. *Pattern:* "restrict, apply theorem to restriction, lift back to $V$."

**Illegal but tempting operations:**

> [!warning] 1. Inferring eigenvalues from the diagonal entries of an *arbitrary* matrix
> The diagonal entries of the matrix of $T$ are its eigenvalues **only** when the matrix is upper- (or lower-) triangular. The matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ on $\mathbb{R}^2$ has diagonal entries $0, 0$ but no eigenvalue at all — it is a rotation by $90°$. The operation becomes legal exactly when one has shown the matrix is triangular in the given basis, or after performing an explicit change of basis to a triangularizing one (which exists over $\mathbb{C}$ but may not over $\mathbb{R}$).

> [!warning] 2. Concluding "diagonalizable" because $T$ has $\dim V$ eigenvalues *counted with repetition*
> The diagonalizability criterion needs $\dim V$ **distinct** eigenvalues, or equivalently the sum of the eigenspace dimensions equal to $\dim V$. The operator $T(a, b, c) = (b, c, 0)$ on $\mathbb{F}^3$ has $0$ as its only eigenvalue with $E(0, T)$ of dimension $1$, so it is not diagonalizable, even though counted with algebraic multiplicity $0$ appears three times. The operation becomes legal once one verifies $\sum_k \dim E(\lambda_k, T) = \dim V$, or equivalently that $m_T$ has distinct linear factors.

> [!warning] 3. Inferring that two operators with the same minimal polynomial are similar
> Two operators on the same space can have the same minimal polynomial and still be non-similar — the minimal polynomial is *not* a complete similarity invariant. On $\mathbb{C}^4$, both $\begin{pmatrix} 0 & 1 \\ & 0 \\ & & 0 & 1 \\ & & & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 1 \\ & 0 \\ & & 0 \\ & & & 0 \end{pmatrix}$ have minimal polynomial $z^2$ but are not similar (the first has rank $2$, the second rank $1$). The operation becomes legal once one has the full invariants — the elementary divisors, or equivalently the [[Thm - Jordan Normal Form|Jordan form]] — in which case operators with the same Jordan form *are* similar (see [[Modules II — §3.3–3.4]]).

> [!warning] 4. Treating $\det(T - \lambda I)$ as defined or "obviously zero" in this chapter
> LADR's chapter 5 develops eigenvalue theory **without** the determinant. The determinant is built later, and the "eigenvalues are roots of the characteristic polynomial" formulation is unavailable in this chapter. The substitute is "eigenvalues are roots of the minimal polynomial", which gives the *set* of eigenvalues but not their multiplicities. The operation becomes legal once one has built the determinant — see [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] — at which point the characteristic polynomial appears and the classical Cayley–Hamilton theorem (in its determinant form) becomes available.

> [!warning] 5. Combining real and complex factorizations of $m_T$ uncritically
> A real operator can have a real minimal polynomial that factors over $\mathbb{C}$ into more factors than it does over $\mathbb{R}$. The rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has $m_T(z) = z^2 + 1$, which is irreducible over $\mathbb{R}$ but factors as $(z - i)(z + i)$ over $\mathbb{C}$. The roots over $\mathbb{C}$ are *not* eigenvalues of the real operator — they live in the wrong field. The operation becomes legal only after **explicitly complexifying** the operator (extending scalars to $\mathbb{C}$), at which point the complex roots *are* eigenvalues of the complex extension.

---

# Problem-Solving Strategy

The problems in this chapter sort into a small number of types, and recognizing which type you face decides almost everything about the route to the answer.

If the problem **gives you an explicit operator (a matrix, a formula, or an action on a specific space) and asks for the minimal polynomial**, run the iterate algorithm. Pick a vector $v$ — often the first standard basis vector when the operator is given as a matrix — and form $v, Tv, T^2 v, \ldots$ until you find the first linear dependence $T^m v = \sum_{k < m} c_k T^k v$. The polynomial $z^m - \sum c_k z^k$ is your candidate. For "generic" $v$ this is the minimal polynomial; otherwise it is a factor and you check by trying additional vectors. The reason this works is the [[Thm - Existence and Uniqueness of Minimal Polynomial|degree bound]] $\deg m_T \leq \dim V$, which keeps the search finite, combined with the observation that the minimal polynomial of $T$ on $V$ is the least common multiple of the "annihilator polynomials" of single vectors — and for a generic vector these agree.

If the problem **gives you a polynomial equation $p(T) = 0$** and asks something about $T$, the route runs through [[Thm - Existence and Uniqueness of Minimal Polynomial|minimality]]: $m_T$ divides $p$. So $m_T$ is one of finitely many monic divisors of $p$, and the rest of the problem is to narrow down which. The equation $T^2 = T$ says $m_T \mid z(z-1)$, so $m_T \in \{z, z-1, z(z-1)\}$ — three cases, often quickly distinguished by the specific information in the problem. The equation $T^k = I$ says $m_T \mid z^k - 1$, which over $\mathbb{C}$ factors into distinct linear factors, immediately giving diagonalizability. The general lesson is: a polynomial equation in $T$ is an upper bound on what $m_T$ can be, and bounding $m_T$ from above is bounding the structural complexity of $T$.

If the problem **asks whether $T$ is diagonalizable**, compute the minimal polynomial and check whether it has distinct linear factors. This is [[Thm - Conditions for Diagonalizability|the criterion]]. Over $\mathbb{C}$, every minimal polynomial factors into linear factors, so the only obstruction to diagonalizability is *repeated* roots of $m_T$, which correspond to non-diagonalizable Jordan blocks. The cheapest practical test: if you can verify $p(T) = 0$ for a polynomial $p$ with distinct linear factors, $T$ is diagonalizable, since $m_T$ then divides $p$ and inherits distinct linear factors. Conversely, the trick of "compute $T^k$ for small $k$ and look for relations" is how one usually decides diagonalizability for explicit operators.

If the problem **asks for an eigenvalue or eigenvector over $\mathbb{C}$**, you always have the existence theorem to lean on, even when no eigenvector is explicit. The standard moves: (a) find $m_T$ and read off its roots, (b) compute $\ker(T - \lambda I)$ for each candidate eigenvalue, (c) for non-explicit $T$, use the polynomial-relation method to *construct* a nonzero $v$ with $(T - \lambda I)v = 0$ from a vector $w$ that satisfies a lower-degree polynomial relation. The Axler argument for the existence theorem is itself an algorithm: given any nonzero $w$, factor the dependence polynomial $p$ of $w$ and produce an eigenvector as $q(T)w$ for an appropriate cofactor $q$.

If the problem **asks something about all operators on $V$ at once** — show that every operator has property $X$, or that some property is preserved under similarity — the route usually starts by translating $X$ into a statement about $m_T$. For instance, "$T$ has only finitely many eigenvalues" becomes "$m_T$ has finitely many roots", which is immediate from $\deg m_T \leq \dim V$. "Similar operators have the same eigenvalues" becomes "similar operators have the same minimal polynomial", which is immediate from $m_{S^{-1} T S}(z) = m_T(z)$ (substitute and conjugate the proof). The pattern is universal: structural facts about $T$ are facts about $m_T$.

A meta-strategy threads through all the above: **the minimal polynomial is the universal pivot**. Every question in this chapter is the question "what is the minimal polynomial, and how does it factor?". When stuck, compute $m_T$ — by the iterate algorithm, by leveraging an operator equation, by spotting a forced factor — and reread the problem in light of it. The reason this works is that $m_T$ is the operator's signature in the polynomial ring, and the polynomial ring $F[x]$ — being a [[Def - Principal Ideal Domain|PID]] — is the simplest and most rigid ring we know how to compute in. **The minimal polynomial converts a question about an operator into a question about a polynomial.**

---

# Most Reusable Properties

- **[[Thm - Existence and Uniqueness of Minimal Polynomial|Existence of the Minimal Polynomial]]**: for every $T$ on a finite-dimensional $V$, there is a unique monic $m_T \in F[x]$ with $\deg m_T \leq \dim V$, $m_T(T) = 0$, and $m_T \mid p$ for every $p$ with $p(T) = 0$. **Typical use:** every other theorem in the chapter goes through $m_T$. When a problem has anything to do with eigenvalues, diagonalizability, triangularizability, or polynomial relations in $T$, compute or constrain $m_T$ first.

- **[[Thm - Existence of Eigenvalues on Complex Vector Spaces|Existence of Eigenvalues on $\mathbb{C}$]]**: every operator on a finite-dimensional nonzero complex vector space has an eigenvalue. **Typical use:** this is the existence step in every inductive proof on $\dim V$ over $\mathbb{C}$ — find an eigenvector, restrict to its complement, induct. It is the engine behind upper-triangularizability, the spectral theorem, the Jordan form, and just about every structural result on $\mathbb{C}^n$.

- **[[Thm - Conditions for Diagonalizability|Diagonalizability $\iff$ minimal polynomial has distinct linear factors]]**: this is the *practical* diagonalizability test. **Typical use:** to decide diagonalizability for an explicit operator without finding eigenvectors. Verify or refute a candidate polynomial relation $p(T) = 0$ for a $p$ with distinct linear factors; if it holds, $T$ is diagonalizable (since $m_T \mid p$ inherits distinct linear factors). The standard application: any operator with $T^k = I$ over $\mathbb{C}$ is automatically diagonalizable.

- **[[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent|Eigenvectors of distinct eigenvalues are linearly independent]]**: a one-step pigeonhole argument that bounds the number of distinct eigenvalues by $\dim V$ and is the source of the direct-sum decomposition $V = \bigoplus E(\lambda_k, T)$ when it exists. **Typical use:** any problem about distinct eigenvalues — counting them, building a basis from them, deciding diagonalizability — routes through this lemma.

- **[[Thm - Upper-Triangular Form on Complex Vector Spaces|Upper-Triangularizability over $\mathbb{C}$]]**: every operator on a finite-dimensional complex vector space is upper-triangularizable. **Typical use:** in induction-on-dimension proofs that handle the "general" operator on $\mathbb{C}^n$ by reducing to the triangular case. It is the substitute, in the determinant-free framework, for what determinant-based texts get from the characteristic polynomial.

- **[[Thm - Gershgorin Disk Theorem|Gershgorin's Theorem]]**: every eigenvalue is within "row-radius" of some diagonal entry. **Typical use:** quick eigenvalue localisation, proving invertibility of strictly diagonally dominant matrices, bounding spectral radius. A staple in numerical linear algebra and in convergence proofs for iterative algorithms.

---

# Bridges

1. **The polynomial ring $F[x]$ is a Euclidean, hence principal ideal, domain, and the minimal polynomial is the monic generator of an ideal.** This is the central algebraic fact behind the whole chapter. Inside $F[x]$ sit two natural ideals associated to an operator $T \in \mathcal{L}(V)$: the **kernel of the evaluation map** $F[x] \to \mathcal{L}(V)$, $p \mapsto p(T)$ — the set of polynomials that annihilate $T$ — and, for any single $v \in V$, the **kernel of the orbit map** $F[x] \to V$, $p \mapsto p(T)v$. Both are ideals because $p \mapsto p(T)$ is a ring homomorphism, and ideals of $F[x]$ are principal because $F[x]$ is a PID via the [[Thm - Division Algorithm for Polynomials (LA)|division algorithm]]. The minimal polynomial of $T$ is the **monic generator** of the first; the annihilator polynomial of a single vector $v$ is the monic generator of the second. The whole theory IS the structure theory of $F[x]$-modules in disguise — see [[Def - The Module of a Linear Operator]] in [[Modules II — §3.3–3.4]], which makes the identification literal: a pair $(V, T)$ of a vector space and an operator on it is the same data as an $F[x]$-module, with $x$ acting as $T$.

2. **The structure theorem for modules over a PID specialises to the canonical forms of an operator.** Once you accept that $(V, T)$ is an $F[x]$-module, the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] applies: $V$ decomposes as a direct sum of cyclic modules $F[x]/(f_i)$ with $f_1 \mid f_2 \mid \cdots \mid f_s$. The product $f_1 \cdots f_s$ is the **characteristic polynomial** of $T$ (a notion that requires determinants but reappears here as a module-theoretic invariant), and the last invariant factor $f_s$ is the **minimal polynomial**. The **primary decomposition** of this module, valid because $F[x]$ is a PID, sorts these cyclic pieces by their prime factor and produces the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] over $\mathbb{C}$ — each piece $F[x]/((x-\lambda)^k)$ becomes a Jordan block. The [[Thm - Jordan Normal Form|Jordan normal form]] and the [[Thm - Rational Canonical Form|rational canonical form]] of [[Modules II — §3.3–3.4]] are these decompositions made matrix-explicit. The current chapter is the geometric face of that algebra: every theorem in §5 about eigenvalues, minimal polynomials, and upper-triangular / diagonal form is the algebraic structure theorem viewed through the lens of operators.

3. **Eigenvalues of the Jacobian govern local dynamics near fixed points of differentiable maps.** In a [[Def - The Total Derivative and Differentiability|smooth dynamical system]] $x_{n+1} = f(x_n)$ with $f(x_*) = x_*$ a fixed point, the linearisation near $x_*$ is the linear operator $Df_{x_*}$ on the tangent space. The eigenvalues of this Jacobian decide local stability: if all eigenvalues have absolute value less than $1$, $x_*$ is attracting; if any has absolute value greater than $1$, $x_*$ is repelling; the marginal cases require higher-order analysis. The Hartman–Grobman theorem makes this rigorous: near a hyperbolic fixed point (no eigenvalues on the unit circle), the nonlinear dynamics is topologically conjugate to its linearisation. So the abstract spectral structure of an operator — which eigenvalues it has, and where they sit in the complex plane — is the same data as the local geometric behaviour of the nonlinear system that operator linearises.

4. **Holomorphic Functional Calculus** *(Functional Analysis preview)*. For a bounded operator $T$ on a Banach space and a function $f$ holomorphic in a neighbourhood of the spectrum $\sigma(T)$, one *defines* the operator $f(T)$ by a Cauchy-style integral
$$f(T) = \frac{1}{2\pi i} \oint_\gamma f(z)(zI - T)^{-1}\, dz,$$
where $\gamma$ encircles $\sigma(T)$. This generalises the polynomial calculus $p(T)$ of §5A to arbitrary holomorphic functions, and the spectrum replaces the set of eigenvalues. The minimal polynomial $m_T$ is the simplest annihilating function in this calculus: when $T$ is finite-dimensional, $f(T) = 0$ whenever $f$ vanishes on the spectrum to the right multiplicity, which is exactly what $m_T \mid f$ means. The spectral mapping theorem $\sigma(f(T)) = f(\sigma(T))$ is the functional-calculus version of "eigenvalues of $p(T)$ are $p(\lambda)$ for $\lambda$ an eigenvalue of $T$" (Exercise 4 of §5B). The whole structure of finite-dimensional spectral theory is the toy version of holomorphic functional calculus, and it tells you what to look for when you eventually meet the full theory.

---

# Insights

**The unifying frame: an operator is a polynomial action, and the minimal polynomial is its signature.** The deep content of this chapter is that the pair $(V, T)$ of a vector space and an operator on it is *the same data* as the $F[x]$-module structure on $V$ with $x$ acting as $T$. Once you accept this, every theorem reorganises. Eigenvalues become the prime ideals $(x - \lambda) \subseteq F[x]$ in the support of the module; the minimal polynomial becomes the monic generator of the module's annihilator ideal; diagonalizability becomes the module's being a direct sum of simple submodules $F[x]/(x - \lambda)$ for distinct $\lambda$; upper-triangularizability becomes the existence of a filtration of submodules with one-dimensional quotients. The polynomial ring $F[x]$ is doing all the work, and the work it can do is bounded by its being a PID — the simplest non-trivial ring class that still has unique factorization. Linear algebra without this perspective is bookkeeping; with it, the structural results become inevitable.

**The true name of an eigenvector is "spans a one-dimensional invariant subspace."** The textbook definition — "nonzero $v$ with $Tv = \lambda v$" — is the right thing to *check* but the wrong thing to *think*. The operational meaning is geometric: a one-dimensional invariant subspace $U \leq V$ is a line through the origin that $T$ maps into itself; on such a line, $T$ must act as a scalar multiplication (it has nowhere else to go). The scalar is the eigenvalue, and any nonzero vector on the line is an eigenvector. Whenever a problem talks about an eigenvalue, picture the invariant line and ask "where could this line live?" — the eigenvalue often emerges from a geometric constraint on lines (rotation has no real eigenvalue because rotation has no fixed line; differentiation has eigenvalue $0$ only because $D$ strictly *lowers* degree). Conversely, when looking for an eigenvector, look for a structural feature of $V$ that picks out a $T$-invariant line. The polynomial form of the existence proof produces eigenvectors precisely by finding lines — it builds them as $q(T)v$ for a cofactor $q$, ensuring $(T - \lambda I)$ kills the result.

**A trigger-reaction pattern: "see a polynomial in $T$ → reach for the minimal polynomial."** Any time a problem presents a polynomial equation in $T$ — $T^k = I$, $T^2 = 3T - 2I$, "$T$ is a projection", "$T^2 = 0$" — the first move is to translate to a statement about $m_T$. The equation says $p(T) = 0$ for some $p$, so $m_T \mid p$, so $m_T$ is one of finitely many monic divisors of $p$, and the rest is usually a one-line discrimination. The pattern is universal because $m_T$ is the smallest polynomial relation $T$ satisfies, and any other polynomial relation factors through it. Internalising this saves enormous effort: questions that seem to require finding eigenvalues, computing matrices, or doing explicit invariant subspace constructions often reduce to inspecting two or three monic factorisations.

**A trigger-reaction pattern: "want to triangularize → work over $\mathbb{C}$ and induct on dimension; want to diagonalize → check that the minimal polynomial factors into distinct linear factors."** Triangularization and diagonalization are conceptually different operations on an operator. Triangularization is *always* possible over $\mathbb{C}$ because the fundamental theorem of algebra factors $m_T$ into linear factors, however many times each root appears; the work is in arranging the basis. Diagonalization is more demanding: it requires $m_T$ to have **distinct** linear factors. So if you only need to "put $T$ in some standard form to study it", triangular is enough and the inductive Axler proof handles it. If you need a decomposition $V = \bigoplus E(\lambda_k, T)$ — to compute powers of $T$, to decouple a system of ODEs, to write down $f(T)$ explicitly — you need diagonalizability, and you must verify the distinct-roots condition.

**Inheritance: the determinant-free framework reveals that eigenvalues come from the polynomial ring, not from determinants.** A reader who learned eigenvalues via the characteristic polynomial $\det(xI - T)$ may believe that determinants are essential to the theory. The Axler framework shows otherwise: every statement about eigenvalues in this chapter is derived using only the polynomial ring $F[x]$, the division algorithm, and the fundamental theorem of algebra. The determinant — when it eventually appears in [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] — is a *secondary* invariant of the operator, useful for computation and for the elegant formula $\det = \prod \lambda_k$, but not a primitive notion. The eigenvalues *are* the roots of the minimal polynomial; the characteristic polynomial is a refinement that records multiplicities. The pedagogical lesson is that the polynomial ring, not the multilinear algebra, is the source of the spectral structure.

**Inheritance: where does "$T$ has an eigenvalue on $\mathbb{C}$" come from? From the fundamental theorem of algebra, which is itself a fact of complex analysis.** The chain is: $T$ has an eigenvalue $\iff$ some $T - \lambda I$ is not invertible $\iff$ some factor of an annihilating polynomial is not invertible $\iff$ the annihilating polynomial has a root in the scalar field. The last step is the fundamental theorem of algebra, and the FTA is *not* a fact of pure algebra — every proof of it requires some analysis (Liouville's theorem, intermediate value theorem on the modulus, topology of $\mathbb{C}$). The existence of eigenvalues on complex vector spaces is therefore *the first place* in linear algebra where analysis enters: it is the place where the algebraic completeness of $\mathbb{C}$ over $\mathbb{R}$ — a property whose only honest proofs are analytic — does real work. The whole chapter inherits its strength over $\mathbb{C}$ from this single fact about the complex numbers.

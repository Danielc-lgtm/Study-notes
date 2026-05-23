---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Polynomial of an Operator"
  - "Def - Polynomial over a Field"
  - "Def - Division Algorithm and Factorization"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $F$ (here, almost always $\mathbb{C}$), $T \in \mathcal{L}(V)$ is an operator on $V$. The identity operator is $I$. A scalar $\lambda \in F$ is an **eigenvalue** of $T$ if there exists $v \neq 0$ with $Tv = \lambda v$; the vector $v$ is an **eigenvector** for $\lambda$. The eigenspace $E(\lambda, T) = \ker(T - \lambda I)$. The polynomial ring is $F[x]$; $\deg p$ is the degree of $p \in F[x]$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---

# Statement

> **Theorem (Existence of Eigenvalues on $\mathbb{C}$).** Let $V$ be a finite-dimensional nonzero complex vector space and $T \in \mathcal{L}(V)$. Then $T$ has at least one eigenvalue $\lambda \in \mathbb{C}$.

Equivalently — and this is the form that arises in the proof — there exists $\lambda \in \mathbb{C}$ such that $T - \lambda I$ is not invertible, equivalently has non-trivial kernel.

The result fails in two important ways if any hypothesis is dropped: it fails over $\mathbb{R}$ (a $90°$ rotation on $\mathbb{R}^2$ has no real eigenvalues), and it fails in infinite [[Def - Dimension|dimensions]] (the right-shift operator on $\mathbb{C}^\infty$ has no eigenvalues — see [[Def - Eigenvalue and Eigenvector]] for the example).

---

# Motivation

This theorem is the **single most important structural fact about operators on complex vector spaces**, and the foundation of every subsequent result in linear algebra over $\mathbb{C}$: upper-triangularizability, the spectral theorem, the existence of Jordan form, the structure of operators on Hilbert spaces. The proof was made famous by Sheldon Axler's [book](http://linear.axler.net/) for its elegant avoidance of [[Def - Determinant|determinants]] — eigenvalues are produced through pure polynomial algebra, never through "set the determinant equal to zero."

The role of the theorem is to **convert the abstract question "what does $T$ do?" into the concrete question "what are the eigenvalues of $T$ and how do they organise $V$?".** Without an eigenvalue, $T$ is opaque: we have no privileged direction, no decomposition, no clean structure to exploit. With an eigenvalue $\lambda$ and an eigenvector $v$, we have:

- A one-dimensional invariant [[Def - Subspace|subspace]] $\operatorname{span}(v)$.
- A natural projection $V \to V / \operatorname{span}(v)$ to a smaller space, on which $T$ descends to a new operator.
- An induction step: by induction on $\dim V$, the structure of $T$ is built up one eigenvalue at a time.

This last point is what makes the theorem the foundation of *everything else*. Almost every structural theorem on complex vector spaces proceeds by induction on dimension, with the base step "find an eigenvalue" supplied by this theorem and the induction step using restriction to an invariant [[Def - Subspace|subspace]] (or descent to a quotient).

The role of the complexity hypothesis is irreducible. The theorem's proof relies on the **fundamental theorem of algebra** — every nonconstant polynomial in $\mathbb{C}[z]$ has a complex root. This is what guarantees that an annihilating polynomial of $T$ can be factored into linear factors over $\mathbb{C}$, hence has roots in $\mathbb{C}$ which become eigenvalues. Over $\mathbb{R}$, the fundamental theorem of algebra fails — $x^2 + 1$ has no real root — and consequently the existence theorem fails. The whole machinery of complex linear algebra rests on this single analytic fact about $\mathbb{C}$.

A historical note: most older linear algebra books prove this theorem using the **characteristic polynomial** $\chi_T(z) = \det(zI - T)$, observing that $\chi_T$ has degree $\dim V$ and applying the FTA to get a complex root $\lambda$, which is then verified to be an eigenvalue. This proof needs the determinant, which requires a substantial development (multilinear algebra, signed permutations, etc.). Axler's proof avoids the determinant entirely — only the polynomial [[Def - Ring|ring]] $F[x]$ and the FTA are needed. This is more than aesthetics: it shows that **eigenvalues are a property of the polynomial algebra $F[T] \subseteq \mathcal{L}(V)$**, not of the multilinear-algebra apparatus that produces [[Def - Determinant|determinants]].

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$F = \mathbb{C}$, $V$ finite-dimensional, $V \neq 0$". The interesting question is what **B-source** problems disguise this — that is, what assumption patterns lead one to invoke the theorem.

The first disguised source is **a polynomial relation $p(T) = 0$ where $p$ has degree $> 0$**. Such a relation does not immediately give an eigenvalue, but it factors over $\mathbb{C}$ as $p(z) = c(z - \lambda_1) \cdots (z - \lambda_k)$, and applying the factorisation to $T$ gives $(T - \lambda_1 I) \cdots (T - \lambda_k I) = 0$. At least one factor $T - \lambda_j I$ must fail to be invertible (otherwise the product would be invertible), so $\lambda_j$ is an eigenvalue. This is the *content* of the proof of the existence theorem, repackaged: the polynomial relation is the bridge. The non-obvious aspect is that many problems hand you a polynomial relation in disguise (e.g. "$T$ is a projection" means $T^2 = T$, hence $p(T) = 0$ for $p(z) = z^2 - z$). *Example problem:* "Suppose $T$ is a non-trivial projection on a complex vector space. Show $T$ has eigenvalues $0$ and $1$." The disguised source is $T^2 = T$.

The second disguised source is **finite-dimensionality plus a single nonzero vector**. Given any $v \neq 0$ in $V$ (with $\dim V = n$), the list $v, Tv, T^2v, \ldots, T^n v$ has $n+1$ vectors in an $n$-dimensional space and must be linearly dependent. The dependence gives a polynomial $p$ with $p(T)v = 0$, and the previous bridge then produces an eigenvalue (in fact, an eigenvector: $q(T)v$ for an appropriate cofactor $q$). The Axler proof is exactly this construction. The non-obvious step is *recognising* that just having a nonzero vector and finite dimension is enough — no other structure is needed. *Example problem:* "Show that every $T \in \mathcal{L}(\mathbb{C}^n)$ has an eigenvector. Construct the eigenvector explicitly." The disguised source is the iterate dependence.

The third disguised source is **a quotient or sub-operator construction**. If $T$ on $V$ has an invariant subspace $U$, then the restriction $T|_U$ and the quotient $T/U$ on $V/U$ are operators on smaller-dimensional complex vector spaces — both are still finite-dimensional and complex, so each has an eigenvalue. This is the engine of every induction-on-dimension proof. The non-obvious step is *building* the invariant subspace before invoking the theorem on the restriction. *Example problem:* "If $T$ on $\mathbb{C}^n$ has an invariant subspace $U$ with $\dim U = 1$, show that there is a basis in which $T$ has an upper-triangular matrix." The disguised source: $V/U$ is complex and finite-dimensional, so the inductive eigenvalue on $V/U$ contributes the next diagonal entry.

**Targets (Output Amplification)**

The bare conclusion of the theorem is: there exists $\lambda \in \mathbb{C}$ such that $T - \lambda I$ is not invertible. The amplifications:

Combined with **the iterative reduction "find an eigenvalue, restrict, induct"**, the theorem amplifies to [[Thm - Upper-Triangular Form on Complex Vector Spaces|upper-triangularizability]]: every operator on a finite-dimensional complex vector space has an upper-triangular matrix with respect to some basis. The non-obvious combination is that one applies the theorem $\dim V$ times — once per basis vector. *Result E:* every complex operator is upper-triangularizable, which is the foundation of subsequent canonical-form theory.

Combined with **the structure of the minimal polynomial**, the theorem amplifies to the *factorisation* of $m_T$ over $\mathbb{C}$. The minimal polynomial $m_T$ has degree $\geq 1$, and over $\mathbb{C}$ factors as $m_T(z) = (z - \lambda_1) \cdots (z - \lambda_k)$ with the $\lambda_j$ in $\mathbb{C}$. By [[Thm - Eigenvalues are Zeros of the Minimal Polynomial|the zeros-of-minimal-polynomial theorem]], these $\lambda_j$ are the eigenvalues of $T$. *Result E:* over $\mathbb{C}$, the minimal polynomial completely encodes the set of eigenvalues, and via [[Thm - Conditions for Diagonalizability|the diagonalizability criterion]] it also detects whether $T$ is diagonalizable.

Combined with **a hypothesis of operator commutativity**, the theorem amplifies to the existence of a **common eigenvector** for two commuting operators: pick an eigenspace $E(\lambda, S)$ of one, restrict the other to it (which is invariant by commutativity), apply the theorem to the restriction, get a common eigenvector. *Result E:* commuting operators on a finite-dimensional nonzero complex vector space share an eigenvector. This is the engine of simultaneous triangularization — see [[Ex - Commuting operators share an eigenvector on complex spaces]]. The non-obvious combination is that commutativity makes the eigenspace of one operator invariant under the other, opening the door to applying the existence theorem to the restriction.

---

# Why Is It True

Forget the formal proof and picture the geometry. An operator $T$ on a complex vector space is, in a deep sense, "the action of $x$" on $V$ — the polynomial $x$ acts as $T$, $x^2$ as $T^2$, and so on. We want to find a direction $v$ on which $T$ acts as a scalar — but more abstractly, we want to find a direction on which the *whole polynomial ring* $\mathbb{C}[x]$ acts as the simplest possible non-trivial $\mathbb{C}$-algebra, namely $\mathbb{C}$ itself.

The simplest $\mathbb{C}$-algebras are $\mathbb{C}$ (one-dimensional) and the **quotient [[Def - Ring|rings]]** $\mathbb{C}[x]/(x - \lambda) \cong \mathbb{C}$ for any $\lambda \in \mathbb{C}$. So finding an eigenvector for $T$ with eigenvalue $\lambda$ is exactly finding a one-dimensional [[Def - Submodule|submodule]] of $V$ on which the $\mathbb{C}[x]$-action factors through $\mathbb{C}[x] \to \mathbb{C}[x]/(x - \lambda) \cong \mathbb{C}$.

Why must such a [[Def - Submodule|submodule]] exist? Because **$V$ is a finite-dimensional $\mathbb{C}[x]$-module**, and finite-dimensional [[Def - Module|modules]] over $\mathbb{C}[x]$ are completely classified by the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]]: they decompose as direct sums of cyclic [[Def - Module|modules]] $\mathbb{C}[x]/((x - \lambda_k)^{m_k})$, and every such cyclic module contains the one-dimensional submodule annihilated by $(x - \lambda_k)$. So *every* such direct summand contains an eigenvector.

This is the *deep* explanation: the eigenvalue exists because $\mathbb{C}[x]$ is a PID with maximal [[Def - Ideal|ideals]] all of the form $(x - \lambda)$, so any nonzero finite-dimensional $\mathbb{C}[x]$-module has a simple submodule, and simple $\mathbb{C}[x]$-modules are one-dimensional.

> **The mechanism in one sentence: a polynomial relation $p(T) = 0$ — guaranteed to exist by finite-dimensionality — factors over $\mathbb{C}$ into linear pieces, and at least one piece $T - \lambda I$ must have non-trivial kernel.**

The Axler proof makes this concrete without the module-theoretic language. Take any nonzero $v \in V$. The $n+1$ vectors $v, Tv, \ldots, T^n v$ (where $n = \dim V$) cannot be linearly independent — they live in an $n$-dimensional space. So there is a nontrivial polynomial $p(z) = a_0 + a_1 z + \cdots + a_n z^n$ with $p(T)v = 0$. By the fundamental theorem of algebra, factor $p(z) = c(z - \lambda_1) \cdots (z - \lambda_k)$ over $\mathbb{C}$. Then
$$0 = p(T)v = c(T - \lambda_1 I)(T - \lambda_2 I) \cdots (T - \lambda_k I) v.$$
Now walk the product from right to left until you find the first index $j$ where the running vector is killed:
$$w = (T - \lambda_{j+1} I) \cdots (T - \lambda_k I) v$$
is the largest such running vector that is *not* killed by the next factor, while $(T - \lambda_j I) w = 0$. This $w$ is an eigenvector with eigenvalue $\lambda_j$.

The intuition crystallised: **finite dimension forces a polynomial relation; the FTA factors that relation into linear pieces; some factor must contribute the eigenvector.** The FTA is doing the irreducible work — replace it with a weaker statement (e.g. "every polynomial of degree 2 has a real root") and the proof breaks. This is why the theorem fails over $\mathbb{R}$.

---

# What Makes This Hard

The non-trivial step is the **construction of the eigenvector $w$** from the polynomial relation $p(T)v = 0$. The naive instinct is: "factor $p$ over $\mathbb{C}$, so $p$ has a root $\lambda$, hence $\lambda$ is an eigenvalue." But this is not quite right — the polynomial $p$ depends on the choice of $v$, and the roots of $p$ are not automatically eigenvalues of $T$. (Indeed, $p$ might have spurious factors that do not contribute.) The correct argument is to walk through the factored product, identifying which factor first produces zero — this gives an eigenvector explicitly as $w = (\text{tail of the product})\, v$. The common error is to assume that $\lambda$ is an eigenvalue without producing the witness vector, or to confuse "$\lambda$ is a root of an annihilating polynomial of $v$" with "$\lambda$ is an eigenvalue of $T$." Another common error is to forget the **finite-dimensional** hypothesis: in infinite [[Def - Dimension|dimensions]], the iterate list $v, Tv, T^2 v, \ldots$ can be linearly independent forever, and no polynomial relation appears.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Use finite-dimensionality to produce a polynomial relation $p(T)v = 0$ for any nonzero $v$. Factor $p$ using the fundamental theorem of algebra. Walk through the factored product to find the factor that contributes the eigenvector.

**Subgoal decomposition:**

1. **The iterate list is linearly dependent.** Take any nonzero $v \in V$. The list $v, Tv, T^2v, \ldots, T^n v$ has $n+1$ vectors in $V$, which has dimension $n$.
   - *Hint:* a list with more vectors than the dimension is linearly dependent.
   - *Why needed:* this is the source of the polynomial relation.

2. **Extract a smallest-degree polynomial relation.** From the dependence, there is a smallest $m \geq 1$ such that $T^m v$ is a linear combination of $v, Tv, \ldots, T^{m-1}v$.
   - *Hint:* write the smallest such relation as $T^m v + c_{m-1} T^{m-1} v + \cdots + c_0 v = 0$, defining a monic polynomial $p$ of degree $m$.
   - *Why needed:* minimality of $m$ ensures $p$ is the "right" polynomial for $v$; it is in fact the [[Def - Annihilator|annihilator]] polynomial of $v$, and the minimal polynomial of $T$ as restricted to the cyclic subspace $\operatorname{span}(v, Tv, \ldots, T^{m-1}v)$.

3. **Factor $p$ using the FTA.** $p \in \mathbb{C}[z]$ has degree $m \geq 1$, so by the fundamental theorem of algebra, $p(z) = (z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m)$.
   - *Hint:* the FTA says every nonconstant polynomial in $\mathbb{C}[z]$ has a complex root, and induction on degree gives the full factorisation.
   - *Why needed:* this is the step that uses $F = \mathbb{C}$. Without algebraic closure, the polynomial $p$ might be irreducible of degree $\geq 2$, blocking the next step.

4. **Walk the product right-to-left to find the eigenvector.** Apply $p(T)v = 0$ as
$$(T - \lambda_1 I)(T - \lambda_2 I) \cdots (T - \lambda_m I) v = 0,$$
and define $w_k = (T - \lambda_{k+1} I) \cdots (T - \lambda_m I) v$, with $w_m = v$ and $w_0 = p(T)v = 0$. Find the largest $k \geq 1$ with $w_k \neq 0$.
   - *Hint:* such a $k$ exists because $w_m = v \neq 0$ and $w_0 = 0$.
   - *Why needed:* the existence of this transition index $k$ is exactly the existence of an eigenvector. The next subgoal extracts it.

5. **Verify $w_k$ is an eigenvector with eigenvalue $\lambda_k$.** By construction, $w_k \neq 0$ but $w_{k-1} = (T - \lambda_k I) w_k = 0$. So $T w_k = \lambda_k w_k$, and $w_k$ is an eigenvector for $\lambda_k$.
   - *Hint:* the definition of $w_{k-1}$ as $(T - \lambda_k I) w_k$ is exactly the eigenvalue equation rearranged.
   - *Why needed:* this completes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: For any nonzero $v$ in a finite-dimensional $V$ and any $T \in \mathcal{L}(V)$, there is a smallest positive integer $m$ such that $v, Tv, \ldots, T^{m-1}v$ are linearly independent but $T^m v$ is in their span.
> **Statement:** With $n = \dim V$, the list $v, Tv, T^2 v, \ldots, T^n v$ is linearly dependent. Let $m$ be the smallest positive integer such that $T^m v \in \operatorname{span}(v, Tv, \ldots, T^{m-1} v)$. Then $m \leq n$, and $v, Tv, \ldots, T^{m-1} v$ are linearly independent.
>
> **Hint:** linear dependence of $v, Tv, \ldots, T^n v$ is immediate from dimension count; take $m$ to be the first index where the list $v, Tv, \ldots, T^m v$ becomes dependent.
>
> **Why needed:** this $m$ is exactly the degree of the polynomial $p$ that annihilates $v$. The polynomial of degree $m$ extracted from this lemma is then factored by FTA in the next lemma.
>
> > [!note]- Full proof
> > The list $v, Tv, \ldots, T^n v$ has $n+1$ vectors in an $n$-dimensional space, so it is linearly dependent. Let $m$ be the smallest positive integer such that $v, Tv, \ldots, T^m v$ is linearly dependent (such $m$ exists and $m \leq n$). Then $v, Tv, \ldots, T^{m-1} v$ is linearly independent (by minimality of $m$), and adding $T^m v$ produces dependence. So $T^m v$ is a linear combination of $v, Tv, \ldots, T^{m-1} v$, completing the claim.

> [!note]- Lemma 2: A monic polynomial of degree $\geq 1$ in $\mathbb{C}[z]$ factors completely into linear factors.
> **Statement:** For any monic $p \in \mathbb{C}[z]$ with $\deg p = m \geq 1$, there exist $\lambda_1, \ldots, \lambda_m \in \mathbb{C}$ (not necessarily distinct) such that $p(z) = (z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m)$.
>
> **Hint:** apply the fundamental theorem of algebra to extract one root $\lambda_1$, peel off the linear factor $(z - \lambda_1)$, and induct on degree.
>
> **Why needed:** this factorisation is what reduces the abstract polynomial relation to a product of *linear* factors, each of which is of the form $(T - \lambda I)$ — manageable operators.
>
> > [!note]- Full proof
> > Induction on $m = \deg p$. Base case $m = 1$: $p(z) = z - \lambda$ for some $\lambda \in \mathbb{C}$, factorisation trivial.
> >
> > Inductive step: assume the result for degree $m - 1$. By the fundamental theorem of algebra (4.12 in LADR), $p$ has at least one root $\lambda \in \mathbb{C}$. By the factor theorem (4.6 in LADR — see [[Def - Division Algorithm and Factorization]]), $p(z) = (z - \lambda) q(z)$ for some monic $q \in \mathbb{C}[z]$ of degree $m - 1$. By induction, $q(z) = (z - \lambda_2) \cdots (z - \lambda_m)$, so $p(z) = (z - \lambda)(z - \lambda_2) \cdots (z - \lambda_m)$, completing the proof.

> [!note]- Lemma 3: If $p(T)v = 0$ for a nonzero $v$ and $p$ factors as $p(z) = (z - \lambda_1) \cdots (z - \lambda_m)$, then some factor $(T - \lambda_j I)$ has nonzero kernel.
> **Statement:** Let $v \neq 0$ and $(T - \lambda_1 I) \cdots (T - \lambda_m I) v = 0$. Define $w_m = v$ and recursively $w_{k-1} = (T - \lambda_k I) w_k$, so $w_0 = 0$. Then there exists $k \in \{1, \ldots, m\}$ with $w_k \neq 0$ and $(T - \lambda_k I) w_k = 0$.
>
> **Hint:** $w_m = v \neq 0$ but $w_0 = 0$, so the sequence $w_m, w_{m-1}, \ldots, w_0$ transitions from nonzero to zero at some index. The transition index $k$ has $w_k \neq 0$ and $w_{k-1} = 0$, meaning $(T - \lambda_k I) w_k = 0$.
>
> **Why needed:** this lemma extracts the eigenvector explicitly: $w_k$ is an eigenvector for $\lambda_k$.
>
> > [!note]- Full proof
> > Define $w_k$ inductively from $w_m = v$ by $w_{k-1} = (T - \lambda_k I) w_k$ for $k = m, m-1, \ldots, 1$. By unwinding the recursion, $w_0 = (T - \lambda_1 I)(T - \lambda_2 I) \cdots (T - \lambda_m I) v = p(T)v = 0$. Meanwhile $w_m = v \neq 0$. So the sequence $w_m, w_{m-1}, \ldots, w_0$ has a first nonzero element (namely $w_m$) and a last zero element ($w_0$); let $k$ be the largest index with $w_k \neq 0$. Then $w_{k-1} = (T - \lambda_k I) w_k = 0$, so $T w_k = \lambda_k w_k$. Since $w_k \neq 0$, $w_k$ is an eigenvector with eigenvalue $\lambda_k$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be a finite-dimensional nonzero complex vector space and $T \in \mathcal{L}(V)$. Set $n = \dim V \geq 1$.
>
> **Step 1 — produce a polynomial relation.** Choose any $v \in V$ with $v \neq 0$ (possible because $V \neq 0$). By Lemma 1, the list $v, Tv, T^2 v, \ldots, T^n v$ has $n+1$ vectors in an $n$-dimensional space, hence is linearly dependent. Let $m$ be the smallest positive integer with $v, Tv, \ldots, T^m v$ linearly dependent. Then $T^m v$ is a linear combination of $v, Tv, \ldots, T^{m-1} v$; write
> $$T^m v + c_{m-1} T^{m-1} v + \cdots + c_1 Tv + c_0 v = 0$$
> for some scalars $c_0, c_1, \ldots, c_{m-1} \in \mathbb{C}$. Define the monic polynomial
> $$p(z) = z^m + c_{m-1} z^{m-1} + \cdots + c_1 z + c_0 \in \mathbb{C}[z],$$
> so $p(T) v = 0$, and $\deg p = m \geq 1$ (since $m \geq 1$).
>
> **Step 2 — factor $p$ using the FTA.** By Lemma 2, $p$ factors over $\mathbb{C}$ as
> $$p(z) = (z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m), \qquad \lambda_1, \ldots, \lambda_m \in \mathbb{C}.$$
> Applying the substitution $z \to T$:
> $$p(T) = (T - \lambda_1 I)(T - \lambda_2 I) \cdots (T - \lambda_m I).$$
> The order does not matter, since any two polynomials in $T$ commute.
>
> **Step 3 — extract the eigenvector.** We have $(T - \lambda_1 I)(T - \lambda_2 I) \cdots (T - \lambda_m I) v = 0$. By Lemma 3, define $w_m = v$ and $w_{k-1} = (T - \lambda_k I) w_k$ recursively. Since $w_m = v \neq 0$ and $w_0 = p(T) v = 0$, the largest index $k$ with $w_k \neq 0$ satisfies $1 \leq k \leq m$ and $w_{k-1} = 0$. So $(T - \lambda_k I) w_k = 0$ with $w_k \neq 0$, which says
> $$T w_k = \lambda_k w_k.$$
> Hence $w_k$ is an eigenvector of $T$ with eigenvalue $\lambda_k \in \mathbb{C}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Application to differential operators on polynomial spaces (Analysis).** Let $V$ be a finite-dimensional $\mathbb{C}$-vector space of polynomials (say, $\mathcal{P}_n(\mathbb{C})$, polynomials of degree at most $n$) and let $T = D + \alpha I$ for some scalar $\alpha$, where $D$ is differentiation. Find an eigenvalue. The theorem guarantees one exists; the polynomial-relation method produces it: $D$ is nilpotent on $\mathcal{P}_n$ with $D^{n+1} = 0$, so $m_D = z^{n+1}$, hence $m_T = (z - \alpha)^{n+1}$ and $\alpha$ is the only eigenvalue. The application showcases the theorem in a function-space setting where eigenvalues correspond to ODE solutions.

**Application to the Frobenius / Perron eigenvalue (combinatorics, probability).** Let $A$ be a square complex matrix with all entries positive. The Perron-Frobenius theorem says $A$ has a positive real eigenvalue $\lambda > 0$ — the **Perron eigenvalue** — which is the spectral radius and has a positive eigenvector. The existence theorem guarantees *some* eigenvalue exists in $\mathbb{C}$; the harder content of Perron-Frobenius is that one of these eigenvalues is real-positive. Markov chain theory and PageRank both rely on this refinement; the bare existence theorem is the necessary starting point.

**Application to the Hamiltonian in quantum mechanics (physics).** A self-adjoint operator $H$ on a finite-dimensional complex Hilbert space — the Hamiltonian of a quantum system with finitely many energy levels — has eigenvalues, which are the possible energies of the system. The existence theorem says energies *exist*; the [[Thm - Complex Spectral Theorem|complex spectral theorem]] then says $H$ is diagonalizable with all eigenvalues real and eigenvectors orthogonal — which is the entire structure of quantum mechanical observables. The bare existence theorem is the first step in this analysis.

**Application to the differentiation operator on entire functions (functional analysis).** *Surprising non-application.* On the infinite-dimensional space of entire functions $\mathcal{H}(\mathbb{C})$ with $T = D$ (differentiation), every $\lambda \in \mathbb{C}$ is an eigenvalue with eigenvector $e^{\lambda z}$. So the operator has way *more* eigenvalues than the existence theorem predicts in the finite-dimensional setting — the spectrum is the entire complex plane. This illustrates that the finite-dimensional theorem says "at least one"; without finite-dimensionality, the picture is much richer.

---

# Bridges

- **[[Thm - Upper-Triangular Form on Complex Vector Spaces|Upper-Triangular Form]]** — the direct generalisation. Once you have one eigenvalue, you can produce a $T$-invariant subspace of codimension $1$, pass to the quotient, find another eigenvalue, and iterate. This builds an upper-triangular matrix entry by entry. The whole upper-triangular-form theorem is the existence-of-eigenvalues theorem iterated $\dim V$ times along a flag of invariant subspaces.

- **[[Thm - Eigenvalues are Zeros of the Minimal Polynomial]]** — the converse direction. Once you know eigenvalues exist, the zeros-of-minimal-polynomial theorem matches them up with the structural invariant $m_T$: the eigenvalues are exactly the roots of $m_T$ in $F$. Combined with [[Thm - Existence and Uniqueness of Minimal Polynomial|the existence of mₜ]] and the FTA, this gives the *complete* description of eigenvalues over $\mathbb{C}$: they are precisely the roots of $m_T$, and $m_T$ factors completely into linear factors.

- **[[Thm - Conditions for Diagonalizability|Conditions for Diagonalizability]]** — the next-level refinement. The existence theorem says eigenvalues exist; the diagonalizability criterion says when these eigenvalues' eigenspaces span $V$ (equivalently, when $m_T$ has distinct linear factors). Over $\mathbb{C}$, diagonalizability is the simplest possible refinement of "has eigenvalues" — and the most useful for actual computation.

- **The Fundamental Theorem of Algebra** — the analytic prerequisite. The existence theorem fails without the FTA (the Axler proof uses it to factor the annihilating polynomial). The FTA is a theorem of complex analysis (proved using Liouville's theorem, or the topology of $\mathbb{C}$, or the intermediate value theorem applied to the modulus). So the existence of eigenvalues on complex vector spaces is an *analytic* fact about $\mathbb{C}$, encoded in algebraic language.

- **[[Ex - Operators on real odd-dimensional spaces have eigenvalues|Real Odd-Dimensional Spaces]]** — the real analogue. Over $\mathbb{R}$, even-dimensional spaces can fail to have eigenvalues (rotation), but **odd-dimensional** real vector spaces always have real eigenvalues. The reason is that the minimal polynomial, as a real polynomial of odd degree (at most $\dim V$ which is odd), must have at least one real root by the intermediate value theorem (continuous polynomials with $p(-\infty) = -\infty$ and $p(\infty) = \infty$ must cross zero). This is a partial substitute for the FTA in the real setting.

---

# Unlocked by This

> [!tip] Upper-Triangular Form on Complex Vector Spaces *(from Linear Algebra V, §5C)*
> Iterating the existence theorem along a flag of invariant subspaces gives [[Thm - Upper-Triangular Form on Complex Vector Spaces|upper-triangularizability of every operator on a finite-dimensional complex vector space]]. This is the foundation of all subsequent structural theorems.

> [!tip] Generalized Eigenspace Decomposition *(from Linear Algebra VIII)*
> Over $\mathbb{C}$, every operator admits a generalized eigenspace decomposition $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$ where the $\lambda_k$ are the distinct eigenvalues. The proof again uses the existence of eigenvalues iteratively, combined with the structure of $\ker(T - \lambda I)^k$. See [[Thm - Generalized Eigenspace Decomposition]].

> [!tip] Jordan Normal Form *(from Modules II — §3.4)*
> Over $\mathbb{C}$, every operator has a unique (up to ordering of blocks) Jordan normal form. The existence theorem is the first step: it produces the *eigenvalues* (the diagonal entries of the Jordan blocks); the rest of the theorem describes the block sizes. See [[Thm - Jordan Normal Form]].

> [!tip] Spectral Theorem *(from Linear Algebra VII)*
> For normal operators on a finite-dimensional inner product space over $\mathbb{C}$, the [[Thm - Complex Spectral Theorem|complex spectral theorem]] gives a unitary diagonalisation. The existence of eigenvalues is the first step; the additional structure (orthogonality of eigenvectors) comes from the self-adjoint or normal hypothesis.

---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Minimal Polynomial"
  - "Def - Division Algorithm and Factorization"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $F$, $T \in \mathcal{L}(V)$ an operator, $m_T \in F[x]$ the [[Def - Minimal Polynomial|minimal polynomial]]. A zero (root) of a polynomial $p$ is a $\lambda$ with $p(\lambda) = 0$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---

# Statement

> **Theorem (Eigenvalues = Zeros of $m_T$).** Let $V$ be a finite-dimensional vector space over $F$ and $T \in \mathcal{L}(V)$. The zeros of the minimal polynomial $m_T$ in $F$ are exactly the eigenvalues of $T$.
>
> **In particular**, if $F = \mathbb{C}$, then
> $$m_T(z) = (z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m),$$
> where $\lambda_1, \ldots, \lambda_m$ is a list of all eigenvalues of $T$ (possibly with repetitions).

---

# Motivation

This theorem is the **bridge between the algebraic object $m_T$ and the geometric data of eigenvalues**. Without it, $m_T$ is just an annihilating polynomial — a piece of algebraic bookkeeping. With it, $m_T$ becomes the carrier of the entire spectrum: knowing $m_T$ is knowing the eigenvalues.

The result is the practical reason that the minimal polynomial is the universal pivot of the chapter. Whenever you want to find the eigenvalues of an operator, find $m_T$ and factor it — the roots of $m_T$ in $F$ are precisely the eigenvalues. Conversely, knowing the eigenvalues of $T$ gives partial information about $m_T$: its set of roots in $F$ is determined.

The theorem also clarifies an asymmetry between $\mathbb{R}$ and $\mathbb{C}$. Over $\mathbb{C}$, the FTA gives a complete factorization of $m_T$ into linear factors, so $m_T$ is **completely** described by the multiset of eigenvalues with multiplicities. Over $\mathbb{R}$, $m_T$ may have irreducible quadratic factors corresponding to *no* real eigenvalues — the rotation example. So over $\mathbb{R}$, $m_T$ contains more information than the set of eigenvalues (it also records the "complex-conjugate pairs of non-real eigenvalues" as quadratic factors).

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is that $T$ has a minimal polynomial — which is automatic from [[Thm - Existence and Uniqueness of Minimal Polynomial]] for $V$ finite-dimensional.

The first disguised source is **a polynomial equation $p(T) = 0$**. Since $m_T \mid p$, the roots of $m_T$ are a subset of the roots of $p$. So any polynomial relation in $T$ gives an *upper bound* on the set of eigenvalues. *Example problem:* "Show that an idempotent $T^2 = T$ has eigenvalues at most $\{0, 1\}$." The disguised source: $p(T) = 0$ for $p = x^2 - x$, whose roots are $0, 1$; hence the eigenvalues of $T$ are among $\{0, 1\}$.

The second disguised source is **a concrete operator on a finite-dimensional space**. The iterate algorithm produces $m_T$, and factoring $m_T$ produces the eigenvalues. *Example problem:* "Find the eigenvalues of the differentiation operator $D$ on $\mathcal{P}_n(\mathbb{R})$." Compute: $D$ is nilpotent with $D^{n+1} = 0$, so $m_D \mid x^{n+1}$; by checking smaller powers do not annihilate, $m_D = x^{n+1}$; its only root is $0$, so $0$ is the only eigenvalue.

**Targets (Output Amplification)**

Combined with **the factorization of $m_T$ over $\mathbb{C}$**, the theorem amplifies to a **complete description of the spectrum**: over $\mathbb{C}$, the eigenvalues of $T$ are exactly the roots of $m_T$ (with multiplicities given by the exponent in $m_T$, but with the understanding that this multiplicity is the "Jordan block size", not the dimension of the eigenspace).

Combined with **the degree bound $\deg m_T \leq \dim V$**, the theorem amplifies to a **count of eigenvalues**: an operator has at most $\dim V$ distinct eigenvalues. This recovers, via the minimal polynomial route, the same bound obtained from [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent|linear independence of eigenvectors with distinct eigenvalues]] — two routes to the same conclusion.

Combined with **distinct linear factorization of $m_T$**, the theorem amplifies to [[Thm - Conditions for Diagonalizability|diagonalizability of T]]. The condition is that $m_T$ has $\dim V$ (with repetition? no — *distinct*) linear factors over $F$, equivalently that the eigenvalues — being roots of $m_T$ — appear without algebraic repetition.

---

# Why Is It True

The mechanism is symmetric in the two implications, and both use the [[Def - Division Algorithm and Factorization|factor theorem]]:

**Forward (every zero of $m_T$ is an eigenvalue):** Suppose $\lambda \in F$ is a zero of $m_T$. By the factor theorem, $(z - \lambda) \mid m_T$, so $m_T(z) = (z - \lambda) q(z)$ for some $q \in F[x]$ with $\deg q = \deg m_T - 1$. Applying to $T$:
$$0 = m_T(T) = (T - \lambda I) q(T).$$
This says the operator $(T - \lambda I) q(T)$ is the zero operator. Now, $q(T)$ is not the zero operator (because $\deg q < \deg m_T$ and $m_T$ is the smallest-degree [[Def - Annihilator|annihilator]]). So there exists $v \in V$ with $q(T) v \neq 0$. Let $w = q(T) v$. Then $(T - \lambda I) w = (T - \lambda I) q(T) v = 0 \cdot v = 0$, with $w \neq 0$. So $w$ is an eigenvector of $T$ with eigenvalue $\lambda$.

**Backward (every eigenvalue is a zero of $m_T$):** Suppose $\lambda$ is an eigenvalue of $T$, so there is $v \neq 0$ with $Tv = \lambda v$. Then $T^k v = \lambda^k v$ for all $k \geq 0$ (induction). For any polynomial $p \in F[x]$:
$$p(T) v = p(\lambda) v.$$
In particular, $m_T(T) v = m_T(\lambda) v$. But $m_T(T) = 0$, so $m_T(\lambda) v = 0$; since $v \neq 0$, $m_T(\lambda) = 0$.

> **The mechanism in one sentence: $m_T(T)$ acts on every eigenvector $v$ as scalar multiplication by $m_T(\lambda)$; this scalar must be zero (so $\lambda$ is a root); conversely, the factor theorem lets us peel off a linear factor of $m_T$ to find the eigenvector.**

---

# What Makes This Hard

The forward direction is the slightly subtler one: producing the eigenvector $w = q(T) v$ requires recognising that the *cofactor* $q(z) = m_T(z)/(z - \lambda)$ has smaller degree than $m_T$ and therefore $q(T)$ cannot be the zero operator (by minimality of $m_T$). The common error is to attempt the forward direction without using the minimality of $m_T$ — without it, $q(T)v$ could be zero for every $v$, blocking the eigenvector construction. The backward direction is more straightforward but requires the lemma $p(T) v = p(\lambda) v$ for eigenvectors, which is itself a small induction.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Prove both directions. **Forward**: if $\lambda$ is a root of $m_T$, peel off the factor $(z - \lambda)$; the cofactor $q(T)$ is nonzero (by minimality of $m_T$), so it produces an eigenvector. **Backward**: if $\lambda$ is an eigenvalue with eigenvector $v$, then $p(T) v = p(\lambda) v$ for any polynomial $p$; applied to $p = m_T$, this gives $m_T(\lambda) = 0$.

**Subgoal decomposition:**

1. **Action of $p(T)$ on an eigenvector.** Show that for any polynomial $p \in F[x]$ and any eigenvector $v$ of $T$ with eigenvalue $\lambda$, $p(T) v = p(\lambda) v$.
   - *Hint:* induct on the degree of $p$; alternatively, write $p = \sum a_k x^k$ and use $T^k v = \lambda^k v$.
   - *Why needed:* the backward direction.

2. **Backward: every eigenvalue is a zero of $m_T$.** From $m_T(T) = 0$ and Subgoal 1, deduce $m_T(\lambda) v = 0$, hence $m_T(\lambda) = 0$.
   - *Hint:* substitute $p = m_T$ in Subgoal 1.
   - *Why needed:* completes the backward direction.

3. **Forward setup: factor $m_T = (z - \lambda) q(z)$ when $\lambda$ is a zero.** Apply the factor theorem.
   - *Hint:* the factor theorem ([[Def - Division Algorithm and Factorization]]) says $(z - \lambda) \mid m_T$ iff $m_T(\lambda) = 0$.
   - *Why needed:* gives the cofactor $q$ needed for the eigenvector construction.

4. **$q(T)$ is not the zero operator.** By minimality of $m_T$, no nonzero polynomial of degree $< \deg m_T$ annihilates $T$. Since $\deg q = \deg m_T - 1$ and $q \neq 0$ (as $q$ is monic of degree $\geq 0$ — but if $\deg m_T = 0$, this is degenerate; assume $\deg m_T \geq 1$), $q(T) \neq 0$.
   - *Hint:* use the smallest-degree property of $m_T$.
   - *Why needed:* ensures we can find $v$ with $q(T) v \neq 0$.

5. **Construct the eigenvector $w = q(T) v$.** Since $q(T) \neq 0$, pick $v$ with $q(T) v \neq 0$; set $w = q(T) v$. Then $w \neq 0$, and $(T - \lambda I) w = (T - \lambda I) q(T) v = m_T(T) v = 0$. So $T w = \lambda w$.
   - *Hint:* the product $(T - \lambda I) q(T) = m_T(T) = 0$.
   - *Why needed:* completes the forward direction.

6. **Over $\mathbb{C}$, $m_T$ factors completely into linear factors.** By the FTA and Subgoal 3 applied iteratively, $m_T(z) = (z - \lambda_1) \cdots (z - \lambda_m)$ for $\lambda_k \in \mathbb{C}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Polynomial-of-eigenvector action: $p(T)v = p(\lambda)v$
> **Statement:** Let $v \neq 0$ be an eigenvector of $T$ with eigenvalue $\lambda$. For any polynomial $p \in F[x]$, $p(T) v = p(\lambda) v$.
>
> **Hint:** $T^k v = \lambda^k v$ for all $k \geq 0$; sum these with coefficients from $p$.
>
> **Why needed:** the backward direction of the main theorem.
>
> > [!note]- Full proof
> > By induction on $k$: $T^0 v = v = \lambda^0 v$; if $T^{k} v = \lambda^k v$, then $T^{k+1} v = T(T^k v) = T(\lambda^k v) = \lambda^k T v = \lambda^k \lambda v = \lambda^{k+1} v$. So $T^k v = \lambda^k v$ for all $k \geq 0$.
> >
> > Write $p(x) = a_0 + a_1 x + \cdots + a_m x^m$. Then
> > $$p(T) v = a_0 v + a_1 T v + \cdots + a_m T^m v = (a_0 + a_1 \lambda + \cdots + a_m \lambda^m) v = p(\lambda) v.$$

> [!note]- Lemma 2: Cofactor of $m_T$ at a root $\lambda$ is nonzero as an operator
> **Statement:** Suppose $m_T(z) = (z - \lambda) q(z)$ for some $\lambda \in F$ and $q \in F[x]$. Then $q(T) \neq 0$ as an operator on $V$.
>
> **Hint:** $\deg q = \deg m_T - 1$; minimality of $m_T$ as the smallest [[Def - Annihilator|annihilator]] excludes a nonzero polynomial of smaller degree annihilating $T$.
>
> **Why needed:** lets us find a vector $v$ with $q(T)v \neq 0$, which becomes the eigenvector.
>
> > [!note]- Full proof
> > Suppose for contradiction that $q(T) = 0$. Since $q$ is a polynomial (with leading coefficient equal to the leading coefficient of $m_T$, which is $1$, so $q$ is monic of degree $\deg m_T - 1$), $q$ is a monic annihilator of $T$ of degree $\deg m_T - 1$. But $m_T$ is the unique monic polynomial of smallest positive degree annihilating $T$ (by [[Thm - Existence and Uniqueness of Minimal Polynomial]]). So $\deg q \geq \deg m_T$, contradicting $\deg q = \deg m_T - 1$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be a finite-dimensional vector space over $F$ and $T \in \mathcal{L}(V)$. Let $m_T$ be the minimal polynomial of $T$, with $\deg m_T \geq 1$ (the case $\dim V = 0$ is trivial: no operator, no eigenvalues, and the theorem is vacuous).
>
> **($\Leftarrow$) Every zero of $m_T$ is an eigenvalue.** Suppose $\lambda \in F$ is a zero of $m_T$, i.e. $m_T(\lambda) = 0$. By the factor theorem (see [[Def - Division Algorithm and Factorization]]), $(z - \lambda) \mid m_T$, so there is a monic polynomial $q \in F[x]$ of degree $\deg m_T - 1$ with
> $$m_T(z) = (z - \lambda) q(z).$$
> Applying to $T$:
> $$0 = m_T(T) = (T - \lambda I) q(T).$$
> By Lemma 2, $q(T) \neq 0$ as an operator. So there exists $v \in V$ with $q(T) v \neq 0$. Set $w = q(T) v$. Then $w \neq 0$, and
> $$(T - \lambda I) w = (T - \lambda I) q(T) v = m_T(T) v = 0.$$
> So $T w = \lambda w$, hence $\lambda$ is an eigenvalue of $T$.
>
> **($\Rightarrow$) Every eigenvalue is a zero of $m_T$.** Suppose $\lambda \in F$ is an eigenvalue of $T$ with eigenvector $v \neq 0$. By Lemma 1, $m_T(T) v = m_T(\lambda) v$. Since $m_T(T) = 0$ by definition, $m_T(\lambda) v = 0$. Since $v \neq 0$, $m_T(\lambda) = 0$. So $\lambda$ is a zero of $m_T$.
>
> **Over $\mathbb{C}$: complete factorisation.** If $F = \mathbb{C}$, by the fundamental theorem of algebra (and induction on degree, see [[Def - Division Algorithm and Factorization]]), $m_T$ factors as
> $$m_T(z) = (z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m)$$
> for some $\lambda_1, \ldots, \lambda_m \in \mathbb{C}$, possibly with repetitions. By the equivalences just proved, the set $\{\lambda_1, \ldots, \lambda_m\}$ (without repetition) is exactly the set of eigenvalues of $T$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Roots of indicial equations in ODEs (analysis).** A linear ODE with constant coefficients $a_n y^{(n)} + \cdots + a_1 y' + a_0 y = 0$ has characteristic polynomial $p(\lambda) = a_n \lambda^n + \cdots + a_1 \lambda + a_0$, and solutions of the form $y(x) = e^{\lambda x}$ exist exactly when $\lambda$ is a root of $p$. This is the eigenvalue-zero connection in the function-space setting: the differentiation operator has $e^{\lambda x}$ as a $\lambda$-eigenvector, and the constant-coefficient ODE asks for vectors in the kernel of $p(D) = a_n D^n + \cdots + a_0 I$, i.e. eigenvectors with eigenvalues that are roots of $p$.

**Stability of equilibria via characteristic polynomial (dynamical systems).** Near a fixed point $x_*$ of a nonlinear system $\dot x = f(x)$, the linearisation $A = Df_{x_*}$ has characteristic polynomial $\chi_A(\lambda)$; its roots are the eigenvalues, and they govern local stability. The eigenvalue-zero connection is the operational link: stability questions reduce to root-locations of the characteristic polynomial in $\mathbb{C}$ (e.g., Hurwitz stability theorem, Routh's criterion).

**Algebraic numbers and their minimal polynomial roots (number theory).** For an algebraic number $\alpha \in \mathbb{C}$ over $\mathbb{Q}$, the **minimal polynomial of $\alpha$** has $\alpha$ itself among its roots (by definition), and the other roots are the **Galois conjugates** of $\alpha$. The same theorem: roots of the minimal polynomial = eigenvalues, where "eigenvalues" in the field extension setting means "embeddings of $\mathbb{Q}(\alpha)$ into $\mathbb{C}$".

---

# Bridges

- **[[Thm - Existence of Eigenvalues on Complex Vector Spaces|Existence of Eigenvalues on ℂ]]** — the immediate consequence. Over $\mathbb{C}$, $m_T$ has degree $\geq 1$, hence has a root in $\mathbb{C}$ by FTA, hence has an eigenvalue.

- **[[Thm - Conditions for Diagonalizability|Conditions for Diagonalizability]]** — the higher-level use. Diagonalizability is equivalent to $m_T$ being a product of **distinct** linear factors, which by this theorem is the same as "$T$ has $\dim V$ distinct eigenvalues whose eigenspaces sum to $V$" — but the polynomial characterisation is computationally simpler.

- **The Cayley–Hamilton Theorem** — the relationship with the characteristic polynomial. The characteristic polynomial $\chi_T$ has the eigenvalues as roots **with multiplicity equal to the algebraic multiplicity**. The minimal polynomial $m_T$ has the eigenvalues as roots **with multiplicity equal to the maximum Jordan-block size**. These two polynomials differ by extra factors: $\chi_T = m_T \cdot (\text{extra})$, with the extra factors corresponding to the "other Jordan blocks". See [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]].

- **The Galois Conjugacy in Number Theory** — the analogy. For an algebraic number $\alpha$, the minimal polynomial of $\alpha$ over $\mathbb{Q}$ has $\alpha$'s Galois conjugates as its roots. This is the same "eigenvalues = roots of the minimal polynomial" pattern, in a different setting.

- **The Spectral Mapping Theorem** — the functional-calculus version. For a polynomial $p$, the spectrum of $p(T)$ is $\sigma(p(T)) = p(\sigma(T)) = \{p(\lambda) : \lambda \in \sigma(T)\}$. In finite dimensions, this is exactly "eigenvalues of $p(T)$ are values of $p$ at eigenvalues of $T$", and it generalises to bounded operators via the holomorphic functional calculus.

---

# Unlocked by This

> [!tip] Conditions for Diagonalizability *(from Linear Algebra V, §5D)*
> Once eigenvalues are identified with roots of $m_T$, the diagonalizability test "$m_T$ has distinct linear factors" gains its geometric meaning: each distinct linear factor corresponds to one eigenvalue, and "distinct" means no repeated eigenvalues in the factorisation, i.e. no Jordan-block "extra" eigenvalues. See [[Thm - Conditions for Diagonalizability]].

> [!tip] Spectral Mapping Theorem *(from Functional Analysis)*
> The theorem says: the spectrum of $p(T)$ is $p(\sigma(T))$. In finite dimensions, "spectrum" is "set of eigenvalues", and the spectral mapping theorem says eigenvalues of $p(T)$ are obtained by evaluating $p$ at eigenvalues of $T$. The proof uses the "minimal polynomial factors over the spectrum" structure given by the present theorem.

> [!tip] Galois Conjugates *(from Algebraic Number Theory / Galois Theory)*
> For an algebraic number $\alpha$ with minimal polynomial $m_\alpha \in \mathbb{Q}[x]$, the roots of $m_\alpha$ in $\mathbb{C}$ are the **Galois conjugates** of $\alpha$ — the images of $\alpha$ under all embeddings $\mathbb{Q}(\alpha) \hookrightarrow \mathbb{C}$. Same structural pattern: roots of the minimal polynomial = "spectrum" of the algebraic object.

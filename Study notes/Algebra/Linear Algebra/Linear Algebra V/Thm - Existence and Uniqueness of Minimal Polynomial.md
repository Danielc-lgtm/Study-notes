---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Minimal Polynomial"
  - "Def - Polynomial of an Operator"
  - "Thm - Division Algorithm for Polynomials (LA)"
  - "Def - Principal Ideal Domain"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $F$, $T \in \mathcal{L}(V)$ is an operator, $F[x]$ is the polynomial ring. The minimal polynomial is denoted $m_T$. A polynomial is **monic** if its leading coefficient is $1$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---

# Statement

> **Theorem (Existence, Uniqueness, and Degree of the [[Def - Minimal Polynomial|Minimal Polynomial]]).** Let $V$ be a finite-dimensional vector space over $F$ and $T \in \mathcal{L}(V)$. There exists a unique monic polynomial $m_T \in F[x]$ of smallest positive degree such that
> $$m_T(T) = 0.$$
> Furthermore, $\deg m_T \leq \dim V$.

> **Corollary (Divisibility).** For any polynomial $q \in F[x]$, $q(T) = 0$ if and only if $m_T$ divides $q$.

---

# Motivation

This theorem makes the [[Def - Minimal Polynomial|minimal polynomial]] well-defined. Without it, the concept "the smallest annihilating polynomial of $T$" is empty: there might be no annihilating polynomial at all, or there might be many of the same smallest degree, and the construction would be ambiguous.

Both potential problems are resolved by structural facts:
- **Existence** rests on finite-dimensionality: the powers $I, T, T^2, \ldots$ of $T$ are vectors in the finite-dimensional space $\mathcal{L}(V)$, so they must eventually become linearly dependent, giving a polynomial relation.
- **Uniqueness** rests on the [[Thm - Division Algorithm for Polynomials (LA)|division algorithm]] — equivalently, on $F[x]$ being a [[Def - Principal Ideal Domain|PID]]. The set of annihilating polynomials is an [[Def - Ideal|ideal]], and a principal [[Def - Ideal|ideal]] has a unique monic generator.

The degree bound $\deg m_T \leq \dim V$ is more delicate than the naive bound $\deg m_T \leq (\dim V)^2$ (which comes from $\mathcal{L}(V)$ having [[Def - Dimension|dimension]] $(\dim V)^2$). The sharper bound uses a finer construction: instead of looking at all $T^k$ at once, look at iterates $v, Tv, T^2 v, \ldots, T^n v$ of a single nonzero vector $v$, where $n = \dim V$. These are $n + 1$ vectors in an $n$-dimensional space, hence dependent, giving a polynomial of degree at most $n$ that annihilates $v$. The proof then assembles such annihilator polynomials for each vector into a single annihilating polynomial of degree $\leq n$ for *all* of $V$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$V$ finite-dimensional, $T \in \mathcal{L}(V)$" — almost no constraint. The interesting question is when this precondition is met in disguise.

The first disguised source is **any operator on a quotient space or invariant subspace of a finite-dimensional vector space**. Restricting $T$ to a $T$-invariant subspace $U$, or descending to a quotient $V/U$, produces a new operator on a smaller-dimensional space, which still has a minimal polynomial. *Example problem:* "Use the existence of the minimal polynomial on $V/U$ to construct an upper-triangular basis of $V$." The disguised source is that $V/U$ is finite-dimensional.

The second disguised source is **a representation of a finite group on a finite-dimensional vector space**. Each group element $g$ acts as an operator $\rho(g)$ on $V$, and $\rho(g)$ has a minimal polynomial. *Example problem:* "Show that $\rho(g)$ has order dividing $|G|$ if $|G|$ is finite." The disguised source is that $\rho(g)$ on the finite-dimensional $V$ has a minimal polynomial.

The third disguised source is **a single nonzero vector $v$ in a finite-dimensional $V$, with the operator $T$ acting**. The orbit $v, Tv, T^2 v, \ldots$ is a list of vectors in $V$, eventually dependent, giving a polynomial annihilating $v$ — this is the **annihilator polynomial of $v$** (a slightly weaker notion than the minimal polynomial of $T$, but related: the annihilator polynomial of a generic $v$ equals $m_T$). The proof of the existence theorem builds $m_T$ from these per-vector annihilators.

**Targets (Output Amplification)**

Combined with **the fundamental theorem of algebra**, the existence theorem amplifies to [[Thm - Existence of Eigenvalues on Complex Vector Spaces|existence of eigenvalues on ℂ]]: since $m_T$ has degree $\geq 1$, it has a root in $\mathbb{C}$ by FTA, and that root is an eigenvalue (by [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]]).

Combined with **the divisibility property**, the existence theorem amplifies to a **characterisation of all annihilating polynomials**: a polynomial $q$ annihilates $T$ iff $m_T \mid q$. This is the divisibility corollary, and it converts the infinite set of "polynomial relations $T$ satisfies" into the finite-dimensional set of "monic multiples of $m_T$".

Combined with **the factorization theorem over $\mathbb{C}$**, the existence theorem amplifies to **complete factorisation of $m_T$ over $\mathbb{C}$**: $m_T(z) = (z - \lambda_1) \cdots (z - \lambda_m)$ where the $\lambda_k$ are the eigenvalues of $T$ (possibly with repetition). This is the cleanest description of $m_T$ over $\mathbb{C}$ and is used in essentially every subsequent theorem of the chapter.

---

# Why Is It True

The mechanism is **finite-dimensionality forces a polynomial relation, and the PID property of $F[x]$ provides a unique generator for the ideal of all such relations**.

For existence: the space $\mathcal{L}(V)$ has [[Def - Dimension|dimension]] $(\dim V)^2 = n^2$, so the powers $I, T, T^2, \ldots, T^{n^2}$ are $n^2 + 1$ vectors in $\mathcal{L}(V)$ and must be linearly dependent. This is enough to prove existence of *some* annihilating polynomial — but with the crude degree bound $\deg m_T \leq n^2$. The sharper bound $\deg m_T \leq n$ comes from the **single-vector iterate approach**: for any nonzero $v \in V$, the vectors $v, Tv, T^2 v, \ldots, T^n v$ are $n + 1$ vectors in $V$ (dimension $n$), so dependent — giving a polynomial of degree $\leq n$ annihilating $v$. Inducting on dimension via the invariant [[Def - Subspace|subspace]] $\operatorname{range}(q(T))$ (where $q$ is the annihilator of $v$) and combining gives an annihilator of degree $\leq n$ for all of $V$.

For uniqueness: the set of polynomials annihilating $T$ is
$$\operatorname{Ann}(T) = \{p \in F[x] : p(T) = 0\} = \ker \Phi_T,$$
where $\Phi_T : F[x] \to \mathcal{L}(V)$ is the evaluation map $p \mapsto p(T)$. This is an ideal of $F[x]$ (sums and [[Def - Ring|ring]] multiples of [[Def - Annihilator|annihilators]] are [[Def - Annihilator|annihilators]]). By the [[Thm - Division Algorithm for Polynomials (LA)|division algorithm]], every ideal of $F[x]$ is principal, so $\operatorname{Ann}(T) = (g)$ for some $g \in F[x]$. The ideal $(g)$ has generators $\{cg : c \in F^\times\}$ (the nonzero scalar multiples of $g$), and among these there is a unique monic one — divide $g$ by its leading coefficient. This unique monic generator is $m_T$.

> **The mechanism in one sentence: finite dimension creates the ideal of annihilators; PID-ness of $F[x]$ gives the ideal a unique monic generator, which is $m_T$.**

The hardest step in practice is the *sharp* degree bound. The naive bound $\deg m_T \leq n^2$ is easy; the sharper $\deg m_T \leq n$ requires the single-vector iterate argument plus an induction to handle "all of $V$, not just one vector".

---

# What Makes This Hard

The conceptual content is simple, but the proof has **two non-trivial moves**: (i) the sharper degree bound from per-vector iterates, requiring an inductive descent on dimension; (ii) the uniqueness argument requires recognising $\operatorname{Ann}(T)$ as an ideal and using the PID property. Beginners often "prove" existence with the crude bound and stop there, missing the sharp result $\deg m_T \leq \dim V$. The other common slip is forgetting *monicness* in the uniqueness statement — without normalising to monic, the generator is unique only up to nonzero scalar multiples.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** (a) Build an annihilator polynomial $q$ of a single nonzero vector $v$ via iterate dependence; (b) extend to an annihilator of all of $V$ by induction on dimension applied to the invariant [[Def - Subspace|subspace]] $\operatorname{range}(q(T))$; (c) extract the unique monic generator of the ideal of annihilators using the division algorithm.

**Subgoal decomposition:**

1. **Existence on a single vector.** For any $u \neq 0$, find a monic polynomial $q$ of degree $\leq \dim V$ with $q(T)u = 0$.
   - *Hint:* take the smallest $m$ such that $T^m u \in \operatorname{span}(u, Tu, \ldots, T^{m-1} u)$; the dependence gives $q$.
   - *Why needed:* this is the per-vector annihilator polynomial.

2. **Extend to all of $V$ via induction.** Inductively on $\dim V$: applying $q(T)$ collapses some of $V$; the surviving invariant subspace is of smaller dimension, so it has an annihilator $s$ by induction; the product $sq$ then annihilates $T$ on all of $V$ with $\deg sq \leq \dim V$.
   - *Hint:* $\operatorname{range}(q(T))$ is $T$-invariant and has dimension $\leq \dim V - \deg q$; recurse on this subspace.
   - *Why needed:* assembles a global annihilator from local ones.

3. **The annihilators form an ideal.** $\operatorname{Ann}(T) = \{p : p(T) = 0\}$ is closed under addition (sums of annihilators annihilate) and [[Def - Ring|ring]] multiplication ($q \cdot p$ has $(qp)(T) = q(T) p(T) = 0$).
   - *Hint:* both checks are one-line.
   - *Why needed:* identifies $\operatorname{Ann}(T)$ as an ideal of $F[x]$.

4. **The ideal is principal with a unique monic generator.** By the division algorithm / PID property of $F[x]$, $\operatorname{Ann}(T) = (m)$ for some $m \in F[x]$, and $m$ can be normalised to be monic — uniquely.
   - *Hint:* divide any other generator by its leading coefficient.
   - *Why needed:* delivers the unique monic minimal polynomial.

5. **The monic generator is the minimal polynomial.** Any monic annihilator $p$ has $m_T \mid p$ (by Step 4), so $\deg m_T \leq \deg p$, with equality only when $m_T = p$. Hence $m_T$ is the unique monic annihilator of smallest degree, and $\deg m_T \leq \dim V$ (by Steps 1–2).

---

# Lemma Decomposition

> [!note]- Lemma 1: For any nonzero $u \in V$, there is a monic polynomial $q \in F[x]$ of degree $\leq \dim V$ with $q(T) u = 0$.
> **Statement:** Let $u \in V \setminus \{0\}$. Then there is a smallest positive integer $m \leq \dim V$ such that $T^m u \in \operatorname{span}(u, Tu, \ldots, T^{m-1} u)$, and the corresponding monic polynomial $q(z) = z^m + c_{m-1} z^{m-1} + \cdots + c_0$ (with $c_k$ from the dependence relation) satisfies $q(T) u = 0$.
>
> **Hint:** the list $u, Tu, \ldots, T^{\dim V} u$ is linearly dependent (it has $\dim V + 1$ vectors in $V$); take the first power that becomes dependent on the lower ones.
>
> **Why needed:** gives a per-vector annihilator polynomial. The same proof appears in the existence-of-eigenvalues theorem; the annihilator polynomial of $u$ is sometimes called the *order polynomial* of $u$ under $T$.
>
> > [!note]- Full proof
> > The list $u, Tu, T^2 u, \ldots, T^{\dim V} u$ has $\dim V + 1$ vectors in $V$, which has dimension $\dim V$. So the list is linearly dependent. Let $m$ be the smallest positive integer such that $u, Tu, \ldots, T^m u$ is linearly dependent — equivalently, the smallest $m$ such that $T^m u$ is a linear combination of $u, Tu, \ldots, T^{m-1} u$. Then $m \leq \dim V$. Write
> > $$T^m u = -c_0 u - c_1 Tu - \cdots - c_{m-1} T^{m-1} u$$
> > for scalars $c_k \in F$. Define $q(z) = z^m + c_{m-1} z^{m-1} + \cdots + c_0$. Then $q(T) u = T^m u + c_{m-1} T^{m-1} u + \cdots + c_0 u = 0$ as required. $q$ is monic of degree $m \leq \dim V$.

> [!note]- Lemma 2: $\operatorname{Ann}(T) = \{p \in F[x] : p(T) = 0\}$ is an ideal of $F[x]$.
> **Statement:** The set $\operatorname{Ann}(T)$ is a (two-sided, but since $F[x]$ is commutative just an) ideal of $F[x]$: closed under addition, closed under multiplication by arbitrary polynomials.
>
> **Hint:** for $p, q \in \operatorname{Ann}(T)$: $(p + q)(T) = p(T) + q(T) = 0$; for $r \in F[x]$ and $p \in \operatorname{Ann}(T)$: $(rp)(T) = r(T) p(T) = r(T) \cdot 0 = 0$.
>
> **Why needed:** lets us apply the PID property.
>
> > [!note]- Full proof
> > Take $p, q \in \operatorname{Ann}(T)$, i.e. $p(T) = q(T) = 0$. Then $(p + q)(T) = p(T) + q(T) = 0 + 0 = 0$, so $p + q \in \operatorname{Ann}(T)$. For $r \in F[x]$ and $p \in \operatorname{Ann}(T)$: $(rp)(T) = r(T) \cdot p(T) = r(T) \cdot 0 = 0$, so $rp \in \operatorname{Ann}(T)$. Hence $\operatorname{Ann}(T)$ is closed under addition and multiplication by $F[x]$, i.e. is an ideal.

> [!note]- Lemma 3: The principal ideal of an ideal in $F[x]$ has a unique monic generator (when nontrivial).
> **Statement:** Let $I \subseteq F[x]$ be a nonzero ideal. Then there is a unique monic polynomial $g \in F[x]$ with $I = (g)$.
>
> **Hint:** $F[x]$ is a PID by the [[Thm - Division Algorithm for Polynomials (LA)|division algorithm]]; take a generator and divide by its leading coefficient.
>
> **Why needed:** combined with Lemma 2, this delivers the unique monic minimal polynomial.
>
> > [!note]- Full proof
> > Since $F[x]$ is a PID, $I = (h)$ for some $h \in F[x]$. Since $I \neq 0$, $h \neq 0$. Let $a$ be the leading coefficient of $h$, $a \in F^\times$. Then $g = a^{-1} h$ is monic and $(g) = (a^{-1} h) = (h) = I$. For uniqueness: if $g, g'$ are both monic generators of $I$, then $g \mid g'$ and $g' \mid g$ (since both are in $I = (g) = (g')$), so $g' = c g$ for some $c \in F^\times$; since both are monic, $c = 1$, so $g = g'$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be a finite-dimensional vector space over $F$ with $\dim V = n$, and $T \in \mathcal{L}(V)$.
>
> **Step 0 — trivial case.** If $V = 0$, then $T = 0$ and we take $m_T = 1$ (the constant polynomial $1$ — but wait, $1$ is not monic of positive degree). On a zero-dimensional space, the zero operator has $m_T = 1$ as the constant polynomial, satisfying $1(T) = I = 0$ vacuously. To avoid this degenerate case, assume $n \geq 1$ from now on.
>
> **Step 1 — existence.** Induct on $n = \dim V$.
>
> *Base case $n = 0$:* covered above.
>
> *Inductive step:* assume the result for all $V$ of dimension less than $n$, and let $V$ have dimension $n \geq 1$. Pick any $u \in V$ with $u \neq 0$. By Lemma 1, there is a monic polynomial $q \in F[x]$ of degree $m \leq n$ with $q(T) u = 0$.
>
> Note that $q(T) \cdot T^k u = T^k \cdot q(T) u = T^k \cdot 0 = 0$ for all $k \geq 0$, so $u, Tu, T^2 u, \ldots, T^{m-1} u$ all lie in $\ker q(T)$. By Lemma 1 these are linearly independent (by minimality of $m$). So $\dim \ker q(T) \geq m$, hence by the fundamental theorem of linear maps,
> $$\dim \operatorname{range} q(T) = n - \dim \ker q(T) \leq n - m.$$
> The subspace $W = \operatorname{range} q(T)$ is $T$-invariant (because $T$ and $q(T)$ commute, so $T(q(T) v) = q(T)(Tv) \in \operatorname{range} q(T)$). So $T|_W : W \to W$ is an operator on a vector space of dimension $\leq n - m < n$. By the inductive hypothesis applied to $T|_W$, there is a monic polynomial $s \in F[x]$ of degree $\leq n - m$ with $s(T|_W) = 0$ on $W$, equivalently $s(T) \cdot v = 0$ for all $v \in W = \operatorname{range} q(T)$.
>
> Now consider the polynomial $sq \in F[x]$. For any $v \in V$, $q(T) v \in \operatorname{range} q(T) = W$, so $s(T)(q(T) v) = 0$. Hence $(sq)(T) v = s(T) q(T) v = 0$ for all $v$, i.e. $(sq)(T) = 0$. The polynomial $sq$ is monic (product of monic polynomials is monic) of degree $\leq m + (n - m) = n$. So there exists a monic annihilator of $T$ of degree $\leq n$.
>
> **Step 2 — uniqueness via the ideal structure.** Let $\operatorname{Ann}(T) = \{p \in F[x] : p(T) = 0\}$. By Lemma 2, $\operatorname{Ann}(T)$ is an ideal of $F[x]$. By Step 1, $\operatorname{Ann}(T)$ contains the monic polynomial $sq$ of positive degree (since $n \geq 1$ ensures $sq$ has positive degree from $q$). So $\operatorname{Ann}(T)$ is a nonzero ideal. By Lemma 3, there is a unique monic polynomial $m_T \in F[x]$ generating $\operatorname{Ann}(T)$, i.e. $\operatorname{Ann}(T) = (m_T)$.
>
> **Step 3 — $m_T$ is the unique monic polynomial of smallest positive degree.** A monic $p$ satisfies $p(T) = 0$ iff $p \in \operatorname{Ann}(T) = (m_T)$ iff $m_T \mid p$. Since $\deg(m_T \cdot r) = \deg m_T + \deg r \geq \deg m_T$, with equality iff $r$ is a nonzero constant, the smallest-degree monic in $(m_T)$ is $m_T$ itself. So $m_T$ is the unique monic annihilator of smallest degree. By Step 1, $\deg m_T \leq n = \dim V$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Minimal polynomial of an algebraic number (algebraic number theory).** For an algebraic number $\alpha \in \mathbb{C}$ over $\mathbb{Q}$, the **minimal polynomial of $\alpha$ over $\mathbb{Q}$** is defined as the monic generator of the ideal $\{p \in \mathbb{Q}[x] : p(\alpha) = 0\}$. The exact same theorem (existence + uniqueness + degree bound) applies here, with $\mathbb{Q}[x]$ in place of $F[x]$ and the field extension $\mathbb{Q}(\alpha)/\mathbb{Q}$ in place of $\mathcal{L}(V)$. The degree of the minimal polynomial of $\alpha$ is the degree of the extension $[\mathbb{Q}(\alpha) : \mathbb{Q}]$. See [[Def - Algebraic Integer and Minimal Polynomial]] and [[Thm - The Minimal Polynomial Generates the Kernel Ideal]].

**Minimal polynomial of a matrix over a ring (commutative algebra).** For a matrix $A \in M_n(R)$ over a commutative ring $R$ (not necessarily a field), the analogous question becomes: does $A$ have a "minimal polynomial"? Over a field, yes. Over a general commutative ring, the situation is more delicate: $R[x]$ need not be a PID, so the kernel of the evaluation map may not be principal. The result is recovered (with the same proof) when $R$ is a PID (e.g., $\mathbb{Z}$) — see [[Thm - Smith Normal Form]] for the connection.

**Minimal polynomial of a difference operator (combinatorics).** The shift operator $S : F^\infty \to F^\infty$, $S(a_0, a_1, a_2, \ldots) = (a_1, a_2, a_3, \ldots)$, restricted to a finite-dimensional subspace of sequences (e.g. polynomial sequences) has a minimal polynomial. The minimal polynomial of $S$ on a space of sequences satisfying $a_{n+k} = c_{k-1} a_{n+k-1} + \cdots + c_0 a_n$ is the characteristic polynomial $z^k - c_{k-1} z^{k-1} - \cdots - c_0$ — the **characteristic equation of the linear recurrence**. The existence theorem here is the statement "a linear recurrence has a well-defined characteristic polynomial".

---

# Bridges

- **[[Thm - Division Algorithm for Polynomials (LA)|Division Algorithm]]** — the engine. The division algorithm is what makes $F[x]$ a PID, hence what guarantees uniqueness of the monic generator of $\operatorname{Ann}(T)$.

- **[[Def - Principal Ideal Domain|Principal Ideal Domain]]** — the structural framing. $\operatorname{Ann}(T)$ being principal — equivalently, $F[x]$ being a PID — is the deep algebraic content of the theorem. The same statement fails for operators over a non-PID ring, even if existence still holds.

- **[[Thm - Eigenvalues are Zeros of the Minimal Polynomial|Eigenvalues are Zeros of mₜ]]** — the immediate consequence. Once $m_T$ exists, its roots in $F$ are exactly the eigenvalues of $T$. So the existence theorem produces the polynomial whose factorisation gives the spectrum.

- **[[Thm - Existence of Eigenvalues on Complex Vector Spaces|Existence of Eigenvalues on ℂ]]** — the FTA-empowered consequence. Over $\mathbb{C}$, the minimal polynomial $m_T$ has degree $\geq 1$ and the FTA gives it a root in $\mathbb{C}$, which is an eigenvalue.

- **The Cayley–Hamilton Theorem** — the relation to the characteristic polynomial. Once the characteristic polynomial $\chi_T$ is defined (via determinants in [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]]), it is also an annihilating polynomial of $T$ (by Cayley–Hamilton). Hence $m_T \mid \chi_T$, refining the bound $\deg m_T \leq \dim V$ to the equality $\deg \chi_T = \dim V$ and giving the divisibility relation. See [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]].

---

# Unlocked by This

> [!tip] Eigenvalues are Zeros of the Minimal Polynomial *(from Linear Algebra V, §5B)*
> Once $m_T$ exists, its roots in $F$ are exactly the eigenvalues of $T$. See [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]].

> [!tip] Existence of Eigenvalues on Complex Vector Spaces *(from Linear Algebra V, §5B)*
> Over $\mathbb{C}$, $m_T$ has degree $\geq 1$ and hence a complex root, which is an eigenvalue. See [[Thm - Existence of Eigenvalues on Complex Vector Spaces]].

> [!tip] Algebraic Number Theory and Minimal Polynomial *(from Algebraic Number Theory)*
> For an algebraic number $\alpha \in \mathbb{C}$ over $\mathbb{Q}$, the **minimal polynomial of $\alpha$** is the monic generator of the kernel of $\mathbb{Q}[x] \to \mathbb{C}$, $p \mapsto p(\alpha)$. Same construction, different setting. See [[Def - Algebraic Integer and Minimal Polynomial]].

> [!tip] Annihilator Ideal of a Module *(from Module Theory)*
> The ideal $\operatorname{Ann}(T)$ is, in module-theoretic language, the **annihilator** of $V$ as an $F[x]$-module via $T$. See [[Def - Annihilator (Dual Space)]]. For modules over a general commutative ring, annihilators are ideals but need not be principal; the existence of a "minimal annihilator" is a PID phenomenon.

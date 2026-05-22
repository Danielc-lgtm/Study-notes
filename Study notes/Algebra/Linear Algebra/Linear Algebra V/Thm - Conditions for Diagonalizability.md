---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Diagonalizable Operator"
  - "Def - Minimal Polynomial"
  - "Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent"
  - "Thm - Eigenvalues are Zeros of the Minimal Polynomial"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $F$, $T \in \mathcal{L}(V)$ an operator with distinct eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_m$. The eigenspaces are $E(\lambda_k, T) = \ker(T - \lambda_k I)$. The minimal polynomial is $m_T$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---

# Statement

> **Theorem (Conditions for Diagonalizability).** Let $V$ be a finite-dimensional vector space over $F$ and $T \in \mathcal{L}(V)$. Let $\lambda_1, \ldots, \lambda_m$ be the distinct eigenvalues of $T$ in $F$. The following are equivalent:
>
> (a) $T$ is diagonalizable;
>
> (b) $V$ has a basis consisting of eigenvectors of $T$;
>
> (c) $V = E(\lambda_1, T) \oplus E(\lambda_2, T) \oplus \cdots \oplus E(\lambda_m, T)$;
>
> (d) $\dim V = \dim E(\lambda_1, T) + \dim E(\lambda_2, T) + \cdots + \dim E(\lambda_m, T)$;
>
> (e) The minimal polynomial $m_T$ factors as $(z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m)$ — a product of **distinct** linear factors over $F$.

---

# Motivation

This theorem is the **practical test for diagonalizability**. Conditions (a)–(d) are conceptual but require knowing the eigenvalues, eigenvectors, or eigenspaces — work that diagonalizability is often supposed to *deliver*. Condition (e) is computational: just find the minimal polynomial (by the iterate algorithm) and check that it has distinct linear factors.

The equivalence (a) $\iff$ (e) is the deepest of the lot, and the engine of every practical diagonalizability decision. Once you have $m_T$:
- If $m_T = (z - \lambda_1) \cdots (z - \lambda_k)$ with all $\lambda_i$ distinct → diagonalizable.
- If $m_T$ has a repeated linear factor (a Jordan block of size $> 1$ exists at that eigenvalue) → not diagonalizable.
- If $m_T$ has an irreducible non-linear factor (over the field $F$ that does not factor it into linear factors) → not diagonalizable over $F$, though may be diagonalizable after extending scalars.

The theorem also clarifies a frequent confusion: **"$T$ has $\dim V$ eigenvalues counted with multiplicity" is NOT sufficient for diagonalizability**. The relevant count is *distinct* eigenvalues (with full eigenspaces summing to $\dim V$), or equivalently, *distinct* linear factors of $m_T$. The operator $T(a, b, c) = (b, c, 0)$ on $\mathbb{F}^3$ has algebraic multiplicity $3$ at the single eigenvalue $0$, but only one independent eigenvector, so it is not diagonalizable.

---

# Sources and Targets

**Sources (Input Broadening)**

The first disguised source is **an explicit polynomial relation $p(T) = 0$ where $p$ has distinct linear factors over $F$**. Then $m_T \mid p$, and divisors of products of distinct linear factors are products of distinct linear factors. So $T$ is diagonalizable. *Example problem:* "Show that $T^2 = T$ implies $T$ is diagonalizable." Disguised source: $T^2 - T = 0$ means $T$ annihilates $p = z^2 - z = z(z - 1)$, distinct linear factors. (Without verification: $T = 0$ has $m_T = z$; $T = I$ has $m_T = z - 1$; non-trivial projection has $m_T = z(z - 1)$. All have distinct linear factors.)

The second disguised source is **a finite-order operator over $\mathbb{C}$**. If $T^k = I$ over $\mathbb{C}$, then $m_T \mid z^k - 1$. Over $\mathbb{C}$, $z^k - 1 = \prod_{j=0}^{k-1}(z - \zeta^j)$ for $\zeta = e^{2\pi i/k}$ — distinct linear factors. So any divisor of $z^k - 1$ is also a product of distinct linear factors. Hence $T$ is diagonalizable. *Example problem:* "Show that any operator $T$ on $\mathbb{C}^n$ with $T^4 = I$ is diagonalizable."

The third disguised source is **distinct eigenvalues counted to the dimension of $V$**. If $T$ has $\dim V$ distinct eigenvalues, then it has $\dim V$ linearly independent eigenvectors (by [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]]), which form a basis. So $T$ is diagonalizable. *Example problem:* "Show that an operator on $\mathbb{C}^n$ with $n$ distinct eigenvalues is diagonalizable."

**Targets (Output Amplification)**

Combined with **a basis-of-eigenvectors**, the theorem amplifies to the **computational simplification**: powers $T^k$, polynomials $p(T)$, and functions $f(T)$ (when defined) are all computable componentwise in the eigenvector basis. Diagonalising is the universal simplification.

Combined with **a direct-sum decomposition of $V$ as eigenspaces**, the theorem amplifies to **decoupled dynamics**: a linear ODE $\dot x = Tx$ decouples into $\dim V$ scalar ODEs along the eigenspace directions. Each eigenvector evolves independently with its eigenvalue.

Combined with **a commuting operator $S$**, the theorem amplifies to **simultaneous diagonalisation**: if $T$ and $S$ both diagonalisable and commute, they share a common diagonalising basis. This is the foundation of simultaneous diagonalisation of commuting families — see [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|the chapter's §5E discussion]].

---

# Why Is It True

The mechanism for (e) $\iff$ (a) is the **factorisation-based decomposition argument**: if $m_T = (z - \lambda_1) \cdots (z - \lambda_m)$ with distinct $\lambda_k$, then applying the operator-version of partial fraction decomposition (using the Chinese Remainder Theorem for $F[x]$) constructs **projection operators** onto each eigenspace, and these projections sum to the identity, decomposing $V$ as a direct sum of eigenspaces.

More concretely, define the polynomials $q_k(z) = \prod_{j \neq k}(z - \lambda_j)$. The polynomials $q_k$ have no common roots (no $\lambda_j$ is a root of $q_j$ but each $\lambda_i$ ($i \neq j$) is). By the CRT (or by computing directly: by Bézout, there exist $r_k \in F[x]$ with $\sum_k r_k(z) q_k(z) = 1$, since $\gcd$ of the $q_k$ is $1$). Then $P_k = r_k(T) q_k(T)$ acts as the identity on $E(\lambda_k, T)$ and as zero on every other $E(\lambda_j, T)$:
- On $E(\lambda_k, T)$: $q_k(T) v = q_k(\lambda_k) v \neq 0$, and $r_k(T) q_k(T) v = r_k(\lambda_k) q_k(\lambda_k) v = $ (the $k$th term of $\sum r_j q_j = 1$ at $\lambda_k$) $ = 1 \cdot v = v$.
- On $E(\lambda_j, T)$ ($j \neq k$): $q_k(T) v = q_k(\lambda_j) v = 0$ (since $(z - \lambda_j)$ is a factor of $q_k$ for $j \neq k$).

So $V = \bigoplus_k E(\lambda_k, T)$.

For the easier direction (a) $\Rightarrow$ (e): if $T$ has a basis of eigenvectors, the operator $\prod_k (T - \lambda_k I)$ kills every basis vector (each one is killed by some factor $T - \lambda_j I$), hence is zero. So $m_T$ divides $\prod_k (z - \lambda_k)$, the product of distinct linear factors. Since $m_T$ is monic with roots exactly the eigenvalues, $m_T$ must equal $\prod_k (z - \lambda_k)$.

> **The mechanism in one sentence: distinct linear factors of $m_T$ are coprime, so the Chinese Remainder Theorem decomposes $V$ into eigenspaces; conversely, eigenvector basis kills $\prod_k (T - \lambda_k I)$ and forces $m_T$ to have distinct linear factors.**

The equivalence (b) $\iff$ (c) $\iff$ (d) is conceptually simpler. (b) $\Rightarrow$ (c): a basis of eigenvectors splits into groups by eigenvalue; group $k$ spans a subspace of $E(\lambda_k, T)$, and the groups together span $V$, with the eigenvector independence guaranteed by [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]]. (c) $\Rightarrow$ (d): the direct sum's dimension equals the sum of dimensions. (d) $\Rightarrow$ (b): the union of bases of the eigenspaces has $\dim V$ vectors, all eigenvectors, and is linearly independent (eigenvectors of distinct eigenvalues are independent, and within each eigenspace the chosen basis is independent), hence a basis.

---

# What Makes This Hard

The non-obvious direction is **(e) $\Rightarrow$ (a)**: showing that distinct linear factors of $m_T$ imply diagonalizability. The argument requires either (i) the partial-fraction-decomposition construction of eigenspace projections, or (ii) the inductive argument: pick the largest eigenvalue $\lambda_m$, observe that $\ker(T - \lambda_m I)$ and $\operatorname{range}(T - \lambda_m I)$ are complementary $T$-invariant subspaces (because $m_T$'s distinct factors force this), induct on the dimension. Beginners often try to prove this direction directly by writing a vector as a linear combination and computing — without using the polynomial structure of $m_T$ — and get stuck.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Prove (a) $\iff$ (b) $\iff$ (c) $\iff$ (d) by direct unwinding of definitions and the eigenvector-independence lemma. Prove (a) $\iff$ (e) by the polynomial-decomposition route: forward by killing the eigenvector basis, backward by induction on $m$ using the direct-sum split $V = \ker(T - \lambda_m I) \oplus \operatorname{range}(T - \lambda_m I)$.

**Subgoal decomposition:**

1. **(a) $\iff$ (b).** A basis gives a diagonal matrix iff each basis vector is an eigenvector.

2. **(b) $\iff$ (c) $\iff$ (d).** (b) $\Rightarrow$ (c): eigenvectors group by eigenvalue, giving a basis of each eigenspace; eigenspaces sum directly by [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]]; their span is $V$ since the original basis is. (c) $\Rightarrow$ (d): direct sum's dimension is the sum. (d) $\Rightarrow$ (b): pick bases of each eigenspace, union has $\dim V$ vectors, is independent, is a basis.

3. **(a) $\Rightarrow$ (e).** A basis of eigenvectors gives $\prod_k (T - \lambda_k I) = 0$ as an operator (it kills each basis vector). So $m_T \mid \prod_k (z - \lambda_k)$. Since the roots of $m_T$ are exactly the eigenvalues (by [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]]), $m_T$ must equal $\prod_k (z - \lambda_k)$, which has distinct linear factors.

4. **(e) $\Rightarrow$ (a).** Induct on the number $m$ of distinct eigenvalues. *Base case* $m = 1$: $m_T = z - \lambda_1$ means $T = \lambda_1 I$, diagonalizable trivially. *Inductive step*: $V = \ker(T - \lambda_m I) \oplus \operatorname{range}(T - \lambda_m I)$ (key lemma — uses distinctness of the $\lambda_k$); restrict $T$ to the range, where the minimal polynomial divides $(z - \lambda_1) \cdots (z - \lambda_{m-1})$, still distinct linear factors, so diagonalizable by induction; combine with the eigenspace $E(\lambda_m, T) = \ker(T - \lambda_m I)$ to diagonalize all of $V$.

---

# Lemma Decomposition

> [!note]- Lemma 1: For diagonalizable $T$, the eigenspaces span $V$ as a direct sum
> **Statement:** If $V$ has a basis $v_1, \ldots, v_n$ of eigenvectors of $T$, then $V = \bigoplus_k E(\lambda_k, T)$ for the distinct eigenvalues $\lambda_k$.
>
> **Hint:** group the eigenvectors by eigenvalue; the groups span each eigenspace; the eigenspaces sum directly by [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]].
>
> **Why needed:** (b) $\Rightarrow$ (c).
>
> > [!note]- Full proof
> > Let $\lambda_1, \ldots, \lambda_m$ be the distinct eigenvalues of $T$, and partition $\{v_1, \ldots, v_n\}$ by eigenvalue: $V_k = $ the set of $v_i$ with eigenvalue $\lambda_k$. Then $V_k \subseteq E(\lambda_k, T)$, and the union $\bigcup V_k = \{v_1, \ldots, v_n\}$ is a basis of $V$.
> >
> > Claim: $V = E(\lambda_1, T) + \cdots + E(\lambda_m, T)$. Every $v \in V$ is a linear combination of the basis vectors $v_i$, grouped by eigenvalue: $v = \sum_k (\sum_{v_i \in V_k} a_i v_i)$, with $\sum_{v_i \in V_k} a_i v_i \in E(\lambda_k, T)$. So $v$ is a sum of vectors in the eigenspaces.
> >
> > Claim: the sum is direct. By [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]], any relation $w_1 + \cdots + w_m = 0$ with $w_k \in E(\lambda_k, T)$ forces all $w_k = 0$ (otherwise a list of nonzero $w_k$ — eigenvectors for distinct eigenvalues — would be dependent, contradicting the linear-independence theorem).

> [!note]- Lemma 2: For distinct linear factors of $m_T$, the operator $\prod_k (T - \lambda_k I)$ is zero
> **Statement:** If $T$ has a basis $v_1, \ldots, v_n$ of eigenvectors with eigenvalues $\mu_1, \ldots, \mu_n$ (with repetitions) and the distinct values among $\mu_i$ are $\lambda_1, \ldots, \lambda_m$, then $\prod_k (T - \lambda_k I) = 0$ as an operator on $V$.
>
> **Hint:** evaluate on each $v_i$: it is killed by the factor $(T - \mu_i I)$, which is one of the $(T - \lambda_k I)$.
>
> **Why needed:** (a) $\Rightarrow$ (e).
>
> > [!note]- Full proof
> > Take any $v_i$ in the basis. Its eigenvalue $\mu_i$ equals some $\lambda_k$, so $(T - \lambda_k I) v_i = (T - \mu_i I) v_i = 0$. Hence $\prod_j (T - \lambda_j I) v_i = 0$ (as the product contains the killing factor $(T - \lambda_k I)$, and any two polynomials in $T$ commute, so the product can be rearranged to apply the killing factor first). So $\prod_j (T - \lambda_j I)$ vanishes on each basis vector, hence is the zero operator.

> [!note]- Lemma 3: For $m_T$ with distinct linear factors and $m \geq 2$, $V = \ker(T - \lambda_m I) \oplus \operatorname{range}(T - \lambda_m I)$
> **Statement:** Suppose $m_T = (z - \lambda_1) \cdots (z - \lambda_m)$ with distinct $\lambda_k$ and $m \geq 2$. Then the subspaces $\ker(T - \lambda_m I)$ and $\operatorname{range}(T - \lambda_m I)$ are $T$-invariant, and $V = \ker(T - \lambda_m I) \oplus \operatorname{range}(T - \lambda_m I)$.
>
> **Hint:** $T$-invariance: $T$ commutes with $T - \lambda_m I$. Disjointness ($\ker \cap \operatorname{range} = 0$): if $u \in \ker(T - \lambda_m I) \cap \operatorname{range}(T - \lambda_m I)$, then $Tu = \lambda_m u$ and $u = (T - \lambda_m I) v$ for some $v$; apply $\prod_{j \neq m}(T - \lambda_j I)$ to $u$, get $(\lambda_m - \lambda_1) \cdots (\lambda_m - \lambda_{m-1}) u = 0$ — but this scalar product is nonzero (distinct eigenvalues), forcing $u = 0$. Dimension count: $\dim \ker + \dim \operatorname{range} = \dim V$ by [[Thm - Fundamental Theorem of Linear Maps|rank-nullity]].
>
> **Why needed:** (e) $\Rightarrow$ (a), the inductive step. The decomposition lets us restrict $T$ to $\operatorname{range}(T - \lambda_m I)$ and apply the inductive hypothesis there.
>
> > [!note]- Full proof
> > **$T$-invariance:** $T$ commutes with $T - \lambda_m I$ (any operator commutes with itself plus a scalar), so $T(\ker(T - \lambda_m I)) \subseteq \ker(T - \lambda_m I)$ and $T(\operatorname{range}(T - \lambda_m I)) \subseteq \operatorname{range}(T - \lambda_m I)$.
> >
> > **Disjointness $\ker \cap \operatorname{range} = 0$:** Take $u \in \ker(T - \lambda_m I) \cap \operatorname{range}(T - \lambda_m I)$. Then $Tu = \lambda_m u$ and $u = (T - \lambda_m I) w$ for some $w \in V$.
> >
> > By [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent|Lemma 1 of distinct-eigenvalues theorem]] (eigenvectors $v$ satisfy $p(T) v = p(\lambda) v$ for any polynomial $p$ if $Tv = \lambda v$), we have for any $j$ that $(T - \lambda_j I) u = (\lambda_m - \lambda_j) u$.
> >
> > Now use $m_T(T) = 0$:
> > $$0 = m_T(T) w = \prod_{j=1}^{m}(T - \lambda_j I) w = \prod_{j=1}^{m-1}(T - \lambda_j I) \cdot (T - \lambda_m I) w = \prod_{j=1}^{m-1}(T - \lambda_j I) u.$$
> > But $u$ is an eigenvector for $\lambda_m$ (since $u \in \ker(T - \lambda_m I)$, $u \neq 0$ would mean $u$ is an eigenvector), so
> > $$\prod_{j=1}^{m-1}(T - \lambda_j I) u = \prod_{j=1}^{m-1}(\lambda_m - \lambda_j) u.$$
> > The scalar $\prod_{j=1}^{m-1}(\lambda_m - \lambda_j)$ is nonzero (each $\lambda_j \neq \lambda_m$). So $u = 0$. Hence $\ker \cap \operatorname{range} = 0$.
> >
> > **Dimension count:** By rank-nullity ([[Thm - Fundamental Theorem of Linear Maps]]), $\dim \ker(T - \lambda_m I) + \dim \operatorname{range}(T - \lambda_m I) = \dim V$. Combined with the disjointness, the sum is direct and equals $V$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be a finite-dimensional vector space over $F$, $T \in \mathcal{L}(V)$, $\lambda_1, \ldots, \lambda_m$ the distinct eigenvalues of $T$ in $F$.
>
> **(a) $\iff$ (b).** The matrix of $T$ in a basis $v_1, \ldots, v_n$ is diagonal iff $T v_k = \lambda v_k$ for some scalar $\lambda$ for each $k$, i.e. each $v_k$ is an eigenvector.
>
> **(b) $\Rightarrow$ (c).** Lemma 1.
>
> **(c) $\Rightarrow$ (d).** Direct sums add dimensions.
>
> **(d) $\Rightarrow$ (b).** Pick a basis of each $E(\lambda_k, T)$. The union has $\sum_k \dim E(\lambda_k, T) = \dim V$ vectors, all eigenvectors. By [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]], vectors from different eigenspaces are linearly independent; within each eigenspace the basis is independent. So the union is independent, hence a basis.
>
> **(a) $\Rightarrow$ (e).** By Lemma 2, $\prod_k (T - \lambda_k I) = 0$. So $m_T$ divides $\prod_k (z - \lambda_k)$. By [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]], the roots of $m_T$ are exactly the eigenvalues $\lambda_1, \ldots, \lambda_m$. So $m_T$ has each $\lambda_k$ as a root (multiplicity $\geq 1$), hence the linear factor $(z - \lambda_k)$ appears in $m_T$ for each $k$. Since $m_T$ divides $\prod_k (z - \lambda_k)$, the multiplicities are at most $1$, so $m_T$ is exactly $\prod_k (z - \lambda_k)$ — a product of distinct linear factors.
>
> **(e) $\Rightarrow$ (a).** Induct on $m$. *Base case* $m = 1$: $m_T = z - \lambda_1$ means $T - \lambda_1 I = 0$, so $T = \lambda_1 I$. Then every basis vector is an eigenvector, so $T$ is diagonalizable.
>
> *Inductive step* $m \geq 2$: by Lemma 3, $V = \ker(T - \lambda_m I) \oplus \operatorname{range}(T - \lambda_m I)$, both subspaces $T$-invariant. We have $E(\lambda_m, T) = \ker(T - \lambda_m I)$, so it has a basis of eigenvectors for $\lambda_m$. The restriction $T|_W$ to $W = \operatorname{range}(T - \lambda_m I)$ has minimal polynomial dividing $m_T$ (by general $m_{T|_U} \mid m_T$ for invariant $U$), and the value $\lambda_m$ is no longer an eigenvalue of $T|_W$ (since $E(\lambda_m, T) \cap W = 0$). So $m_{T|_W}$ divides $\prod_{j \neq m} (z - \lambda_j)$, which has distinct linear factors. By the inductive hypothesis applied to $T|_W$ on $W$ (with fewer distinct eigenvalues, $m - 1$ of them), $T|_W$ is diagonalizable on $W$. Taking the union of bases of $\ker(T - \lambda_m I)$ and $W$ — both consisting of eigenvectors of $T$ — gives a basis of $V$ consisting of eigenvectors of $T$. So $T$ is diagonalizable. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Decoupling linear ODEs (analysis).** A constant-coefficient linear ODE $\dot x = Ax$ on $\mathbb{C}^n$ has solution $x(t) = e^{At} x(0)$. If $A$ is diagonalizable, $e^{At}$ is computable componentwise in the eigenvector basis. The diagonalisability test (e) becomes: the **minimal polynomial of $A$ has distinct linear factors**, equivalently the **system has no defective modes** (no Jordan blocks of size $> 1$). The diagonalizable case gives oscillating/exponentially-growing/decaying solutions; the non-diagonalizable case adds polynomial-times-exponential terms.

**Markov chain diagonalisation (probability).** A transition matrix $P$ of a Markov chain is in general not symmetric, hence not guaranteed diagonalizable by the spectral theorem. But many natural Markov chains *are* diagonalizable, and the eigenvalues determine the mixing rate. The condition (e) — minimal polynomial has distinct linear factors — is the cleanest practical check.

**Spectral decomposition of an algebraically closed group ring (representation theory).** For a finite abelian group $G$ over $\mathbb{C}$, the group ring $\mathbb{C}[G]$ is a commutative algebra, hence a finite-dimensional commutative ring, hence (by Wedderburn-Artin) a product of copies of $\mathbb{C}$ — i.e. a diagonalisable algebra. The action of any group element $g$ is a finite-order operator (some power $g^k = 1$), hence diagonalizable by condition (e) applied to $z^k - 1$.

---

# Bridges

- **[[Thm - Eigenvalues are Zeros of the Minimal Polynomial|Eigenvalues = Zeros of mₜ]]** — the input. The characterisation (e) needs this theorem to say "the eigenvalues are *exactly* the roots of $m_T$"; without this, "$m_T$ factors into distinct linear factors" would not directly say what the eigenvalues are.

- **[[Thm - Upper-Triangular Form on Complex Vector Spaces|Upper-Triangular Form]]** — the weaker sibling. Diagonalisation requires *distinct* linear factors; upper-triangularisation just requires linear factors (possibly repeated). Every diagonalisable operator is upper-triangularisable; the converse fails.

- **[[Thm - Generalized Eigenspace Decomposition|Generalized Eigenspace Decomposition]]** — the substitute for non-diagonalisable operators. Even when $T$ is not diagonalisable, over $\mathbb{C}$ it decomposes as a direct sum of *generalised eigenspaces* — subspaces invariant under $T$ on which $T - \lambda I$ is nilpotent rather than zero. The generalised eigenspace decomposition is the "best you can do" when diagonalisation fails.

- **[[Thm - Complex Spectral Theorem|Complex Spectral Theorem]]** — the inner-product-space refinement. Normal operators on a complex inner product space are *automatically* diagonalisable, and the diagonalising basis can be chosen orthonormal. The condition (e) is satisfied automatically: normal operators have orthogonal eigenvector decompositions, hence distinct linear factors in $m_T$.

- **Schur decomposition + diagonal of upper-triangular** — the algorithmic realisation. Upper-triangularising via Schur gives a matrix whose diagonal entries are the eigenvalues. If the operator is *also* diagonalisable, an additional change of basis brings the upper-triangular form to diagonal form. The diagonalisability test (e) detects whether this additional step succeeds.

---

# Unlocked by This

> [!tip] Spectral Decomposition *(from Functional Analysis)*
> The condition (e) — $m_T$ has distinct linear factors — generalises (with substantial extra structure) to the **spectral theorem** for normal operators on infinite-dimensional Hilbert spaces: a normal operator is "diagonalizable" in the sense of having a direct-integral decomposition into eigenspaces, even when the spectrum is uncountable.

> [!tip] Simultaneous Diagonalization *(from Linear Algebra V, §5E)*
> Two commuting diagonalisable operators can be simultaneously diagonalised. The proof uses the eigenspace decomposition (c) of one of them, restricts the other to each eigenspace, and observes that this restriction is still diagonalisable (because diagonalisability is inherited by invariant subspaces — a consequence of (e)).

> [!tip] Principal Component Analysis *(from Statistics, Machine Learning)*
> The covariance matrix of a dataset, being real symmetric, is diagonalisable by the real spectral theorem — and the diagonalising basis is the principal components. The condition (e) is satisfied automatically; in practice, the *numerical* diagonalisation is what PCA computes.

> [!tip] Bloch's Theorem and Periodic Schrödinger Operators *(from Solid State Physics)*
> The Hamiltonian of an electron in a periodic potential commutes with the translation operator. By simultaneous diagonalisation, the eigenstates are *also* eigenstates of translation — these are the **Bloch waves**, the basis of band theory. The diagonalisability condition (e) is the underlying mathematical reason this works.

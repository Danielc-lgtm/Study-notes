---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Minimal Polynomial"
  - "Def - Diagonalizable Operator"
  - "Thm - Conditions for Diagonalizability"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional complex vector space and $T \in \mathcal{L}(V)$.

**(a)** Show that if $T^k = I$ for some positive integer $k$, then the minimal polynomial $m_T$ divides $z^k - 1$, and hence $T$ is diagonalizable.

**(b)** Suppose $T \in \mathcal{L}(\mathbb{C}^4)$ satisfies $T^4 = I$ but $T^2 \neq I$. Determine all possible minimal polynomials of $T$.

**Recall:**

![[Def - Minimal Polynomial#The Definition]]

**The minimal polynomial divides any annihilator** (by [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]]): for any polynomial $q$, $q(T) = 0$ iff $m_T \mid q$.

**Diagonalisability criterion** ([[Thm - Conditions for Diagonalizability]]): $T$ is diagonalisable iff $m_T$ factors as a product of *distinct* linear factors over $F$.

Over $\mathbb{C}$, the polynomial $z^k - 1$ factors as $\prod_{j=0}^{k-1} (z - \zeta_k^j)$, where $\zeta_k = e^{2\pi i / k}$ is a primitive $k$-th root of unity. These are $k$ distinct complex numbers.

---

# Convergent Strategy

**Problem class.** This is a problem about extracting structure from a polynomial relation $T^k = I$. The pattern is fundamental: an operator equation in $T$ constrains the minimal polynomial $m_T$ to divide the corresponding polynomial in $z$. Once $m_T$ is constrained, properties of $m_T$ (factorisability, distinctness of roots) translate to properties of $T$ (eigenvalues, diagonalisability).

**Assumption pattern.** The signal is the relation $T^k = I$, equivalently $T^k - I = 0$. So the polynomial $z^k - 1$ annihilates $T$, and by [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)|the divisibility property of the minimal polynomial]], $m_T \mid z^k - 1$. Over $\mathbb{C}$, $z^k - 1$ factors into $k$ distinct linear factors (the $k$-th roots of unity), so any divisor — and in particular $m_T$ — also factors into distinct linear factors. Hence $T$ is diagonalisable.

**Theorem routing.** The route is:
1. **Operator equation $T^k = I$** ⟹ $m_T \mid z^k - 1$ (by [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)|the minimal-polynomial divisibility]]).
2. **Over $\mathbb{C}$**, $z^k - 1 = \prod_j (z - \zeta_k^j)$ — distinct linear factors.
3. **$m_T$ divides a polynomial with distinct linear factors** ⟹ $m_T$ has only distinct linear factors itself (a divisor of a product of distinct primes is a product of a subset of those primes).
4. **$m_T$ has distinct linear factors** ⟹ $T$ is diagonalisable (by [[Thm - Conditions for Diagonalizability]]).

For part (b), the additional constraint $T^2 \neq I$ means $m_T$ does *not* divide $z^2 - 1 = (z - 1)(z + 1)$, so $m_T$ has some root other than $\pm 1$ — i.e., one of $\pm i$ is among the eigenvalues. Combined with $m_T \mid z^4 - 1 = (z - 1)(z + 1)(z - i)(z + i)$, the possible $m_T$ are: the monic divisors of $z^4 - 1$ that are *not* divisors of $z^2 - 1$, with $m_T \neq 1$ (the polynomial $1$ does not annihilate any operator). The systematic enumeration is the second half of the problem.

**Key decision point.** The non-obvious move is realising that the *combination* "$T^k = I$ and $T^j \neq I$ for $j < k$" tells you the *order* of $T$ as an operator (i.e., the smallest $k$ with $T^k = I$), and that this order is exactly the degree of $m_T$ — well, not quite: it is the smallest $k$ for which $T^k = I$, which is the smallest such that $z^k - 1$ is a multiple of $m_T$. The order is the smallest *exponent* of an annihilating polynomial of the form $z^k - 1$, and this need not equal $\deg m_T$ (which is just the smallest degree of any annihilator).

---

# Legal Operations Used

1. **Translate operator equations to divisibility of $m_T$** (operation 4). The relation $T^k = I$ becomes $m_T \mid z^k - 1$ — exactly the move that converts the operator equation into a constraint on $m_T$.

2. **Diagonalize via the minimal polynomial** (operation 6). The criterion "$m_T$ has distinct linear factors" is what we verify, hence what gives diagonalisability.

3. **Read off eigenvalues from the minimal polynomial** (a corollary of operation 2): the roots of $m_T$ are the eigenvalues, so the eigenvalues of an operator with $T^k = I$ are roots of unity.

---

# Hints

> [!note]- Hint 1
> $T^k = I$ is the same as $T^k - I = 0$. So the polynomial $z^k - 1$ annihilates $T$. What does the divisibility property of $m_T$ say about this?

> [!note]- Hint 2
> Over $\mathbb{C}$, $z^k - 1$ factors as $\prod_{j=0}^{k-1}(z - \zeta_k^j)$ where $\zeta_k = e^{2\pi i / k}$ is a primitive $k$-th root of unity. These $k$ values are pairwise distinct.

> [!note]- Hint 3
> Any divisor of a product of distinct linear factors is itself a product of some subset of those distinct factors, hence has distinct linear factors. So $m_T$ has distinct linear factors over $\mathbb{C}$. Apply [[Thm - Conditions for Diagonalizability]].

> [!note]- Hint 4 (for part (b))
> $T^4 = I$ gives $m_T \mid z^4 - 1 = (z - 1)(z + 1)(z - i)(z + i)$. $T^2 \neq I$ excludes $m_T \mid z^2 - 1 = (z - 1)(z + 1)$, meaning $m_T$ has at least one root outside $\{1, -1\}$. Enumerate the monic divisors of $z^4 - 1$ satisfying this.

---

# Solution

The plan for (a) is to apply the minimal-polynomial divisibility property to extract diagonalisability from the relation $T^k = I$, using the distinct-root structure of $z^k - 1$ over $\mathbb{C}$. For (b), enumerate the divisors of $z^4 - 1$ that are not divisors of $z^2 - 1$.

## Part (a)

**Step 1: $m_T$ divides $z^k - 1$.**

The relation $T^k = I$ is equivalent to $(z^k - 1)(T) = T^k - I = 0$. So $z^k - 1$ annihilates $T$.

> [!note]- Derivation
> Compute $(z^k - 1)(T) = T^k - I$ using the polynomial-of-an-operator definition ([[Def - Polynomial of an Operator]]). The hypothesis $T^k = I$ gives $T^k - I = 0$, so $(z^k - 1)(T) = 0$. By [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]], $m_T \mid z^k - 1$.

**Step 2: $z^k - 1$ factors into distinct linear factors over $\mathbb{C}$.**

> [!note]- Derivation
> The polynomial $z^k - 1 \in \mathbb{C}[z]$ has the $k$-th roots of unity as roots: $\zeta_k^0 = 1, \zeta_k^1, \zeta_k^2, \ldots, \zeta_k^{k-1}$, where $\zeta_k = e^{2\pi i / k}$. These are $k$ distinct complex numbers (since $\zeta_k^j = \zeta_k^l$ would force $\zeta_k^{j-l} = 1$, i.e. $k \mid j - l$, which for $0 \leq j, l < k$ forces $j = l$).
>
> By the [[Def - Division Algorithm and Factorization|factor theorem]] applied iteratively, $z^k - 1 = \prod_{j=0}^{k-1}(z - \zeta_k^j)$ — $k$ distinct linear factors.

**Step 3: $m_T$ has distinct linear factors over $\mathbb{C}$.**

> [!note]- Derivation
> $m_T$ divides $z^k - 1 = \prod_j (z - \zeta_k^j)$, a product of $k$ pairwise distinct linear factors. By unique factorization in $\mathbb{C}[z]$, any monic divisor of $z^k - 1$ is a product of some subset of the $(z - \zeta_k^j)$ — that is, a product of *distinct* linear factors. So $m_T$ has distinct linear factors over $\mathbb{C}$.

**Step 4: $T$ is diagonalisable.**

> [!note]- Derivation
> By [[Thm - Conditions for Diagonalizability|condition (e) of the diagonalisability theorem]], an operator is diagonalisable iff its minimal polynomial has distinct linear factors. By Step 3, $m_T$ has distinct linear factors. So $T$ is diagonalisable. $\blacksquare$

## Part (b)

**Step 1: $m_T$ divides $z^4 - 1$.**

By part (a), $m_T \mid z^4 - 1 = (z - 1)(z + 1)(z - i)(z + i)$.

**Step 2: $m_T$ does *not* divide $z^2 - 1$.**

> [!note]- Derivation
> The condition $T^2 \neq I$ means $T^2 - I \neq 0$, i.e. $(z^2 - 1)(T) \neq 0$. By [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]], this is equivalent to $m_T \nmid z^2 - 1 = (z - 1)(z + 1)$.

**Step 3: Enumerate the possible $m_T$.**

> [!note]- Derivation
> The monic divisors of $z^4 - 1 = (z - 1)(z + 1)(z - i)(z + i)$ correspond to subsets of $\{1, -1, i, -i\}$. The constraint $m_T \nmid z^2 - 1$ excludes those divisors whose root set is contained in $\{1, -1\}$. The constraint $m_T \neq 1$ (i.e., $m_T$ has positive degree) excludes the trivial divisor.
>
> So the possible $m_T$ are: monic divisors of $z^4 - 1$ whose set of roots is a subset of $\{1, -1, i, -i\}$ containing at least one of $\{i, -i\}$. Listed:
>
> 1. $m_T = (z - i)$
> 2. $m_T = (z + i)$
> 3. $m_T = (z - i)(z + i) = z^2 + 1$
> 4. $m_T = (z - 1)(z - i)$
> 5. $m_T = (z - 1)(z + i)$
> 6. $m_T = (z + 1)(z - i)$
> 7. $m_T = (z + 1)(z + i)$
> 8. $m_T = (z - 1)(z - i)(z + i) = (z - 1)(z^2 + 1)$
> 9. $m_T = (z + 1)(z - i)(z + i) = (z + 1)(z^2 + 1)$
> 10. $m_T = (z - 1)(z + 1)(z - i) = (z^2 - 1)(z - i)$
> 11. $m_T = (z - 1)(z + 1)(z + i) = (z^2 - 1)(z + i)$
> 12. $m_T = (z - 1)(z + 1)(z - i)(z + i) = z^4 - 1$
>
> Each of these is a possible $m_T$ for some operator $T$ on $\mathbb{C}^4$ with $T^4 = I$ and $T^2 \neq I$. (To verify each is achievable: pick eigenvalues from the root set of the candidate $m_T$, with at least one of each root, on a basis of $\mathbb{C}^4$, possibly with some eigenvalues repeated — but with at least all four roots of the candidate appearing.)
>
> Not all of these are typical: for instance, $m_T = (z - i)$ would correspond to $T = iI$, but $T = iI$ has $T^2 = -I \neq I$ and $T^4 = (iI)^4 = i^4 I = I$, consistent. Similarly each case is realizable as some operator (with appropriate dimensions of eigenspaces summing to $4$).

> [!note]- Complete formal solution
> **Part (a).** Suppose $T^k = I$ for some positive integer $k$. Then the polynomial $z^k - 1 \in \mathbb{C}[z]$ satisfies $(z^k - 1)(T) = T^k - I = 0$. By [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]], $m_T \mid z^k - 1$.
>
> The polynomial $z^k - 1$ factors over $\mathbb{C}$ as $\prod_{j=0}^{k-1}(z - \zeta_k^j)$, where $\zeta_k = e^{2\pi i / k}$. The $k$ values $\zeta_k^j$ are pairwise distinct, so $z^k - 1$ is a product of $k$ distinct linear factors. Any monic divisor of a product of distinct primes is itself a product of distinct primes (by unique factorization in $\mathbb{C}[z]$). So $m_T$ is a product of distinct linear factors over $\mathbb{C}$.
>
> By [[Thm - Conditions for Diagonalizability|condition (e) of the diagonalisability theorem]], $T$ is diagonalisable.
>
> **Part (b).** Given $T \in \mathcal{L}(\mathbb{C}^4)$ with $T^4 = I$ and $T^2 \neq I$. By part (a), $m_T \mid z^4 - 1 = (z - 1)(z + 1)(z - i)(z + i)$. The condition $T^2 \neq I$ gives $m_T \nmid z^2 - 1 = (z - 1)(z + 1)$, i.e. $m_T$ has at least one of $\pm i$ as a root.
>
> Enumerate the monic divisors of $(z - 1)(z + 1)(z - i)(z + i)$ that have at least one of $\pm i$ as a root and have positive degree. As listed in the derivation above, there are exactly $12$ such divisors. Each is a possible minimal polynomial of some operator $T \in \mathcal{L}(\mathbb{C}^4)$ with the given constraints (achievable, e.g., by choosing $T$ to be diagonal with eigenvalues in the root set of the candidate, with multiplicities summing to $4$).
>
> $\blacksquare$

---

# Key Takeaways

**Operator equations $\to$ minimal polynomial constraints.** This is the canonical pattern of the chapter, and this exercise is the prototype. Whenever you see a polynomial equation in $T$ — $T^k = I$, $T^2 = T$, $T^3 = T$, $aT^2 + bT + cI = 0$ — translate to "$m_T$ divides the corresponding polynomial." Then the structure of $m_T$ is constrained to be a divisor of the given polynomial. Over a field where the given polynomial factors completely into linear factors, $m_T$ also factors into linear factors (extracting some subset), giving structural conclusions about $T$. Over $\mathbb{C}$, this is automatic via the FTA; over $\mathbb{R}$, the given polynomial may have irreducible quadratic factors that contribute non-diagonalisability over $\mathbb{R}$ (but diagonalisability over $\mathbb{C}$ after complexifying).

**Finite-order operators on complex vector spaces are diagonalisable.** Part (a) is a *theorem* — not just an exercise — and it has deep consequences. It says: every operator $T$ satisfying $T^k = I$ on a finite-dimensional complex vector space is diagonalisable, with eigenvalues among the $k$-th roots of unity. Applied to representations of finite groups: if $G$ is a finite group and $\rho : G \to \mathrm{GL}(V)$ is a representation (with $|G| < \infty$ and $V$ over $\mathbb{C}$), then every $\rho(g)$ satisfies $\rho(g)^{|G|} = I$ (since $g^{|G|} = e$), so $\rho(g)$ is diagonalisable. This is the **first step** of the proof of Maschke's theorem (semisimplicity of finite-group representations over $\mathbb{C}$): each $\rho(g)$ being diagonalisable is the prerequisite for averaging arguments. The same fact applied to a single matrix $A \in M_n(\mathbb{C})$ with $A^k = I$ says: $A$ is similar to a diagonal matrix of $k$-th roots of unity.

**The order of $T$ as a group element and the degree of $m_T$ are related but distinct.** "Order" of $T$ means: the smallest $k$ with $T^k = I$ — if it exists. The minimal polynomial's *degree* is the smallest $d$ such that some monic polynomial of degree $d$ annihilates $T$, but this polynomial may not be of the form $z^k - 1$ (e.g., $T = \operatorname{diag}(1, i)$ has $T^4 = I$ but $T^2 \neq I$, so order $4$; but $m_T = (z - 1)(z - i)$ has degree $2$). The order is the smallest $k$ such that $z^k - 1$ is annihilating, which is the smallest $k$ such that $m_T \mid z^k - 1$. Geometrically: the order is the **least common multiple of the multiplicative orders of the eigenvalues** in $\mathbb{C}^\times$.

**Enumeration via divisor lattice.** Part (b) requires enumerating divisors of $z^4 - 1$ — there are $2^4 = 16$ monic divisors (subsets of the root set), minus those of degree $0$ (which is just the constant $1$, so $1$ excluded) and those without $\pm i$ ($z^0 = 1$, $z - 1$, $z + 1$, $(z-1)(z+1) = z^2 - 1$; that's $4$ — but wait, $z^0 = 1$ already excluded, so $3$ to subtract; ahh — $16 - 1 - 3 = 12$). This counting via divisor-lattice considerations is a useful exercise in the **algebraic structure of $F[x]$**: the divisor lattice of a product of distinct primes is the boolean lattice $2^{\#\text{primes}}$. This connects to combinatorics (Möbius functions on lattices) and to representation theory (counting irreducible subrepresentations).

---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Determinant"
  - "Def - Minimal Polynomial"
  - "Thm - Cofactor Expansion and Cramer's Rule"
  - "Thm - Determinant Equals Product of Eigenvalues with Multiplicity"
tags: [algebra, linear-algebra]
---

# Problem Statement

The **[[Thm - Cayley-Hamilton (Minimal-Polynomial Form)|Cayley-Hamilton]] theorem** has two proofs in LADR: one in §8B via the minimal polynomial (call this the "**minimal-polynomial form**"), and one in §9C via the determinant and the adjugate (the "**determinantal form**"). Both prove that every operator $T \in \mathcal{L}(V)$ on a finite-dimensional vector space satisfies its own characteristic polynomial: $p_T(T) = 0$, where $p_T(z) := \det(zI - T)$.

Show that the **two definitions of the characteristic polynomial** — the minimal-polynomial-based definition (from §8) and the determinantal definition (from §9) — agree on a complex vector space, and explain how the two proofs of [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)|Cayley-Hamilton]] reflect different organising principles.

Specifically:

(a) **For an operator $T$ on a finite-dimensional complex vector space $V$, the determinantal characteristic polynomial $p_T(z) := \det(zI - T)$ and the §8 characteristic polynomial (the product $\prod_\lambda (z - \lambda)^{m(\lambda)}$ over distinct eigenvalues $\lambda$, with algebraic multiplicity $m(\lambda)$ as defined via generalised eigenspaces) coincide.** Both equal $\prod_{i=1}^n (z - \lambda_i)$, where $\lambda_1, \dots, \lambda_n$ are the eigenvalues with multiplicity.

(b) **The determinantal Cayley-Hamilton proof** is via the adjugate identity $(zI - T) \operatorname{adj}(zI - T) = p_T(z) I$, viewing both sides as matrix-valued polynomials in $z$ and substituting $z = T$ (formally).

(c) **The minimal-polynomial Cayley-Hamilton proof** (from LADR §8) is via the generalised eigenspace decomposition: $V = \bigoplus G(\lambda_i, T)$, and on each generalised eigenspace, $(T - \lambda I)^{m(\lambda)}$ acts as zero, so the product $\prod (T - \lambda_i I)^{m(\lambda_i)} = p_T(T)$ acts as zero on the whole space.

Show these two proofs are essentially equivalent and identify which proof is more economical in which contexts.

**Recall:**

![[Def - Determinant#The Definition]]

![[Def - Minimal Polynomial#The Definition]]

![[Thm - Cofactor Expansion and Cramer's Rule#Statement]]

![[Thm - Determinant Equals Product of Eigenvalues with Multiplicity#Statement]]

**Cayley-Hamilton theorem (LADR 8.29 and 9.64).** For any operator $T \in \mathcal{L}(V)$ on a finite-dimensional vector space, $p_T(T) = 0$ where $p_T$ is the characteristic polynomial.

**Generalised eigenspace.** $G(\lambda, T) := \{v \in V : (T - \lambda I)^k v = 0 \text{ for some } k\}$, with [[Def - Dimension|dimension]] equal to the algebraic multiplicity of $\lambda$.

**Adjugate identity (LADR §9C).** For any matrix $A$, $A \cdot \operatorname{adj}(A) = \det(A) I$.

---

# Convergent Strategy

**Problem class.** This is a *reconciliation* exercise: two different proofs of the same theorem (Cayley-Hamilton) are compared, and the goal is to see how they relate and which is more illuminating. As the [[Linear Algebra IX — §9 Multilinear Algebra and Determinants#Problem-Solving Strategy|topic page strategy]] indicates, this kind of "compare two characterisations" problem is a recurring theme in linear algebra. The key insight is that both proofs ultimately reduce to the eigenvalue structure of $T$, just packaged differently.

**Assumption pattern.** $V$ is finite-dimensional and complex (so eigenvalues exist), and $T$ has known eigenvalue/generalised-eigenspace structure. The two proofs of Cayley-Hamilton give the same conclusion via different intermediate constructions: one through the matrix adjugate, one through the spectral decomposition.

**Theorem routing.** For (a), use [[Thm - Determinant Equals Product of Eigenvalues with Multiplicity]]: both definitions of $p_T(z)$ equal the product $\prod (z - \lambda_i)$ with algebraic multiplicity. For (b), use the adjugate identity and the formal substitution argument. For (c), use the generalised eigenspace decomposition (LADR §8).

**Key decision point.** The non-obvious move is in (b): the "substitute $z = T$" step is *not* a formal substitution into a polynomial; it requires care because $p_T(z) I$ is a polynomial with scalar coefficients, while $(zI - T) \operatorname{adj}(zI - T)$ is a polynomial with matrix coefficients, and you must compare coefficients of each power of $z$ between the two. This is the subtle point that distinguishes the determinantal proof from a naive substitution.

---

# Legal Operations Used

1. **Compute a determinant via eigenvalues** (operation 7 from the topic page). Both definitions of $p_T$ reduce to a product of $(z - \lambda_i)$ via Schur upper-triangularisation.

2. **Use the abstract definition of $\det$** to relate $\det(zI - T)$ to alternating multilinear forms (implicitly, via [[Thm - Determinant Equals Product of Eigenvalues with Multiplicity|the eigenvalue-product theorem]]).

3. **Apply multiplicativity and the cofactor expansion identities** (operations 6 and 8 from the topic page) to derive the adjugate identity $(zI - T) \operatorname{adj}(zI - T) = p_T(z) I$.

---

# Hints

> [!note]- Hint 1
> For (a), invoke [[Thm - Determinant Equals Product of Eigenvalues with Multiplicity|the eigenvalue-product theorem]]: $\det(zI - T) = \prod (z - \lambda_i)$. The §8 definition (in terms of generalised eigenspaces and algebraic multiplicities) is, by construction, $\prod (z - \lambda)^{m(\lambda)}$ — the same product written with collected terms.

> [!note]- Hint 2
> For (b), the adjugate identity says $(zI - T) \operatorname{adj}(zI - T) = p_T(z) I$. The right-hand side is $p_T(z) I = (z^n + a_{n-1} z^{n-1} + \cdots + a_0) I = z^n I + a_{n-1} z^{n-1} I + \cdots + a_0 I$, a polynomial in $z$ with scalar coefficients times $I$. The left-hand side is similar, but with matrix coefficients. Equate coefficients of each $z^k$ and rearrange.

> [!note]- Hint 3
> For (c), invoke the §8 generalised eigenspace decomposition: $V = \bigoplus_\lambda G(\lambda, T)$, and on $G(\lambda, T)$, $(T - \lambda I)^{m(\lambda)}$ vanishes by definition of the generalised eigenspace. The product $p_T(T) = \prod_\lambda (T - \lambda I)^{m(\lambda)}$ contains $(T - \lambda I)^{m(\lambda)}$ as a factor for each $\lambda$, so on each $G(\lambda, T)$ the corresponding factor vanishes.

> [!note]- Hint 4
> The two proofs are essentially equivalent because both rely on the eigenvalue structure of $T$ (Schur reduction or generalised eigenspace decomposition), but they differ in *organisation*: the determinantal proof works in matrix algebra and uses the adjugate identity as a polynomial-coefficient identity; the spectral proof works geometrically with [[Def - Subspace|subspace]] decomposition.

---

# Solution

The plan is to first establish that both definitions of $p_T(z)$ give the same polynomial (part a) via the eigenvalue-product theorem, then trace through each Cayley-Hamilton proof (parts b and c), and finally compare their organising principles.

**Step 1: Both definitions of $p_T(z)$ agree (part a).**

Both equal $\prod_i (z - \lambda_i)$ with multiplicity.

> [!note]- Derivation
> By [[Thm - Determinant Equals Product of Eigenvalues with Multiplicity|the eigenvalue-product theorem]] (companion form), $\det(zI - T) = \prod_{i=1}^n (z - \lambda_i)$ where $\lambda_1, \dots, \lambda_n$ are the eigenvalues of $T$ counted with **algebraic multiplicity** (their multiplicity as roots of $\det(zI - T)$).
>
> The §8 definition of the characteristic polynomial (LADR 8.26): for a complex $V$, $p_T^{(\S 8)}(z) := \prod_\lambda (z - \lambda)^{m(\lambda)}$, where the product is over distinct eigenvalues $\lambda$ and $m(\lambda) = \dim G(\lambda, T)$ is the algebraic multiplicity defined via the generalised eigenspace.
>
> A key fact (LADR 8.21): the algebraic multiplicity from §8 ([[Def - Dimension|dimension]] of generalised eigenspace) equals the multiplicity as a root of $\det(zI - T)$. So:
> $$p_T^{(\S 8)}(z) = \prod_\lambda (z - \lambda)^{m(\lambda)} = \prod_{i=1}^n (z - \lambda_i) = \det(zI - T) = p_T^{(\S 9)}(z),$$
> where in the middle equality we expand the product over distinct $\lambda$ with multiplicity $m(\lambda)$ as a product over $\lambda_i$ with each $\lambda$ appearing $m(\lambda)$ times. The two definitions agree.

**Step 2: Determinantal Cayley-Hamilton via the adjugate (part b).**

The adjugate identity $(zI - T) \operatorname{adj}(zI - T) = p_T(z) I$ gives, after equating polynomial coefficients in $z$, the relation $p_T(T) = 0$.

> [!note]- Derivation
> Let $A := zI - T$ in the adjugate identity from [[Thm - Cofactor Expansion and Cramer's Rule|Cramer/cofactor expansion]]:
> $$(zI - T) \cdot \operatorname{adj}(zI - T) = \det(zI - T) \cdot I = p_T(z) I. \quad (*)$$
>
> View both sides as polynomials in $z$ with matrix coefficients. Write
> $$\operatorname{adj}(zI - T) = B_{n-1} z^{n-1} + B_{n-2} z^{n-2} + \cdots + B_1 z + B_0,$$
> where each $B_k$ is an $n \times n$ matrix (determined by cofactors of $zI - T$, hence depending on $T$ but not on $z$). Note that $\operatorname{adj}(zI - T)$ has entries that are polynomials of degree $\leq n - 1$ in $z$.
>
> Write the right-hand side:
> $$p_T(z) I = (z^n + c_{n-1} z^{n-1} + \cdots + c_1 z + c_0) I = z^n I + c_{n-1} z^{n-1} I + \cdots + c_0 I.$$
>
> Expand the left-hand side of $(*)$:
> $$(zI - T)(B_{n-1} z^{n-1} + \cdots + B_0) = B_{n-1} z^n + (B_{n-2} - T B_{n-1}) z^{n-1} + \cdots + (B_0 - T B_1) z - T B_0.$$
>
> Equate coefficients of $z^k$ on both sides:
> - $z^n$: $B_{n-1} = I$.
> - $z^{n-1}$: $B_{n-2} - T B_{n-1} = c_{n-1} I$.
> - ...
> - $z^k$: $B_{k-1} - T B_k = c_k I$ for $0 < k < n$.
> - $z^0$: $-T B_0 = c_0 I$.
>
> Now compute $p_T(T)$. Multiplying each equation by an appropriate power of $T$ and adding:
> - $T^n \cdot (B_{n-1} = I)$: $T^n B_{n-1} = T^n$.
> - $T^{n-1} \cdot (B_{n-2} - T B_{n-1} = c_{n-1} I)$: $T^{n-1} B_{n-2} - T^n B_{n-1} = c_{n-1} T^{n-1}$.
> - $T^{n-2} \cdot (B_{n-3} - T B_{n-2} = c_{n-2} I)$: $T^{n-2} B_{n-3} - T^{n-1} B_{n-2} = c_{n-2} T^{n-2}$.
> - ...
> - $T \cdot (B_0 - T B_1 = c_1 I)$: $T B_0 - T^2 B_1 = c_1 T$.
> - $-T B_0 = c_0 I$.
>
> Summing all these, the left-hand side telescopes to zero (every $T^k B_j$ appears once with a positive sign and once with a negative sign, except $T^n B_{n-1} = T^n$ from the first equation and the cancellation from the negation in the last):
> $$0 = T^n + c_{n-1} T^{n-1} + \cdots + c_1 T + c_0 I = p_T(T).$$
>
> So $p_T(T) = 0$, the Cayley-Hamilton theorem. $\blacksquare$

**Step 3: Minimal-polynomial / spectral Cayley-Hamilton (part c).**

Via the §8 generalised eigenspace decomposition: $V = \bigoplus G(\lambda, T)$, and $(T - \lambda I)^{m(\lambda)} = 0$ on $G(\lambda, T)$.

> [!note]- Derivation
> By the generalised eigenspace decomposition theorem (LADR 8.21), $V = G(\lambda_1, T) \oplus G(\lambda_2, T) \oplus \cdots \oplus G(\lambda_k, T)$, where $\lambda_1, \dots, \lambda_k$ are the distinct eigenvalues of $T$.
>
> By the definition of the generalised eigenspace, $(T - \lambda_i I)^{m(\lambda_i)} = 0$ on $G(\lambda_i, T)$ (where $m(\lambda_i) = \dim G(\lambda_i, T)$).
>
> The characteristic polynomial in §8 form is $p_T(z) = \prod_{i=1}^k (z - \lambda_i)^{m(\lambda_i)}$. Substituting $z = T$:
> $$p_T(T) = \prod_{i=1}^k (T - \lambda_i I)^{m(\lambda_i)}.$$
>
> The factors all commute (they are polynomials in $T$), so we can rearrange to put any chosen factor last. For any $v \in V$, decompose $v = v_1 + v_2 + \cdots + v_k$ with $v_i \in G(\lambda_i, T)$. Apply $p_T(T)$:
> $$p_T(T) v = \prod_i (T - \lambda_i I)^{m(\lambda_i)} \cdot v = \prod_i (T - \lambda_i I)^{m(\lambda_i)} \cdot (v_1 + \cdots + v_k).$$
>
> For each $v_i \in G(\lambda_i, T)$, the factor $(T - \lambda_i I)^{m(\lambda_i)}$ in the product annihilates $v_i$. So $p_T(T) v_i = 0$ for every $i$, and by linearity $p_T(T) v = 0$.
>
> Since this holds for every $v$, $p_T(T) = 0$. $\blacksquare$

**Step 4: Compare the two proofs.**

The determinantal proof is more abstract and works in matrix algebra; the spectral proof is geometric and works with [[Def - Subspace|subspace]] decomposition.

> [!note]- Derivation
> The determinantal proof:
> - Works entirely in matrix algebra.
> - Uses only the [[Thm - Cofactor Expansion and Cramer's Rule|adjugate identity]] and polynomial-coefficient matching.
> - Does not invoke eigenvalues directly — the adjugate identity holds over any commutative ring, so the proof generalises to operators on [[Def - Module|modules]] over commutative [[Def - Ring|rings]], where eigenvalues may not exist.
> - The substitution $z \to T$ is the subtle step requiring polynomial-coefficient identification.
>
> The spectral / minimal-polynomial proof:
> - Works geometrically via the generalised eigenspace decomposition.
> - Requires the existence of eigenvalues (hence is restricted to algebraically closed fields, or to operators that happen to have eigenvalues; LADR §8 works over $\mathbb{C}$).
> - The proof is conceptually transparent: $V$ splits into pieces $G(\lambda, T)$ each of which is annihilated by $(T - \lambda)^{m(\lambda)}$, so the product polynomial annihilates everything.
> - It is the "right" proof for understanding *why* Cayley-Hamilton is true at a structural level.
>
> **Which is more economical?** For operators over algebraically closed fields with known eigenstructure, the spectral proof is shorter and more conceptual. For operators over general commutative [[Def - Ring|rings]] (e.g., over $\mathbb{Z}$ or over polynomial rings), the determinantal proof is the only one available — and it has the further advantage of being purely formal, not requiring any "spectral" data.
>
> **Equivalence at the eigenvalue level.** Both proofs ultimately rely on the polynomial $p_T(z) = \prod (z - \lambda_i)$ factoring into linear pieces over $\mathbb{C}$. The determinantal proof uses this factorisation implicitly through the equality $\det(zI - T) = \prod(z - \lambda_i)$; the spectral proof uses it explicitly to organise $V$ into generalised eigenspaces. So the two proofs are equivalent at the structural level: they encode the same eigenvalue data, packaged in different mathematical languages.

> [!note]- Complete formal solution
> **(a) Both definitions of $p_T$ agree.** By [[Thm - Determinant Equals Product of Eigenvalues with Multiplicity|the eigenvalue-product theorem]], $\det(zI - T) = \prod (z - \lambda_i)$ with eigenvalues counted with algebraic multiplicity. The §8 definition is $\prod_\lambda (z - \lambda)^{m(\lambda)}$, which expands to the same product.
>
> **(b) Determinantal Cayley-Hamilton.** From $(zI - T) \operatorname{adj}(zI - T) = p_T(z) I$, expand both sides as matrix-polynomials in $z$ and equate coefficients. The result of the telescoping sum (multiplying each coefficient identity by a power of $T$ and summing) is $p_T(T) = 0$.
>
> **(c) Spectral Cayley-Hamilton.** By generalised eigenspace decomposition, $V = \bigoplus_i G(\lambda_i, T)$. On each $G(\lambda_i, T)$, $(T - \lambda_i I)^{m(\lambda_i)} = 0$. The characteristic polynomial $p_T(T) = \prod_i (T - \lambda_i I)^{m(\lambda_i)}$ has the corresponding factor annihilating each piece, so $p_T(T) = 0$.
>
> The two proofs are equivalent at the eigenvalue level but differ in style: determinantal is formal/algebraic and works over any commutative ring; spectral is geometric and works over algebraically closed fields. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> A naive "substitute $z = T$" in $\det(zI - T) = p_T(z)$ to get $\det(TI - T) = \det(0) = 0$ does **not** prove Cayley-Hamilton. The error: $\det(zI - T)$ is a polynomial in the *scalar* $z$ with matrix-valued operations, and "substituting $z = T$" means replacing each occurrence of $z$ by $T$, which is *not* the same as $\det$ of a literal matrix. The correct interpretation requires distinguishing "polynomial in $z$ with matrix coefficients" from "polynomial in $T$ with scalar coefficients" — exactly the kind of careful polynomial-coefficient matching done in the determinantal proof above.

---

# Key Takeaways

**Two proofs of the same theorem can encode the same content in different mathematical languages, and choosing between them depends on the context.** The Cayley-Hamilton theorem has at least three standard proofs: the determinantal proof via the adjugate (this exercise's part b), the spectral proof via generalised eigenspaces (part c), and a slick proof via "polynomial substitution into the resolvent" (not covered here). Each works in slightly different generality and emphasises different features. The determinantal proof works over any commutative ring, requires no spectral data, but obscures the "why"; the spectral proof requires an algebraically closed field but exposes the geometric mechanism. The take-home: when you have a theorem with multiple proofs, the proofs often record the same mathematical fact in different "coordinate systems", and the choice of which proof to use is dictated by what additional facts you need — generality (use the formal proof) versus insight (use the geometric one).

**The adjugate identity $(zI - T) \operatorname{adj}(zI - T) = p_T(z) I$ is a polynomial-coefficient identity, not a substitution-style identity.** This is the most subtle point about the determinantal Cayley-Hamilton proof, and the place where a "naive" attempt would fail. The identity is between two matrix-valued polynomials in $z$, and the proof works by expanding both as $\sum_k C_k z^k$ with $C_k \in M_n(\mathbb{F})$ (i.e., matrix coefficients) and equating coefficients of each $z^k$. The "substitute $z = T$" step is *not* a literal substitution — it is a series of identities $T^k B_{k-1} - T^{k+1} B_k = c_k T^k$, summed appropriately so that the matrix coefficients $B_k$ telescope away and only the scalar coefficients $c_k$ remain, giving $p_T(T) = 0$. This is a powerful technique whenever you have a polynomial identity over a non-commutative algebra: pass to formal-polynomial-coefficient comparisons rather than naive substitution.

**The §8 (spectral) and §9 (determinantal) frameworks are complementary; LADR provides both deliberately.** The §8 framework starts from the minimal polynomial and works geometrically with eigenspaces; the §9 framework starts from alternating multilinear forms and works algebraically with [[Def - Determinant|determinants]]. Each illuminates different aspects: §8 is the natural home for "the Jordan form" and the structure-of-an-operator picture; §9 is the natural home for "the determinant" and the multilinear-functional picture. The Cayley-Hamilton theorem is a *bridge* between them, statable purely in terms of polynomials in operators but provable from either side. Reading both proofs is a way of consolidating both frameworks, and the bridge is exactly the eigenvalue structure that both proofs ultimately rely on.

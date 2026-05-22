---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Determinant"
  - "Def - Alternating Multilinear Form"
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $\mathbb{F}$ with $n = \dim V$. For an operator $T \in \mathcal{L}(V)$, $\det T$ is the [[Def - Determinant|determinant]] of $T$. For square matrices, $\det A$ is the determinant of $A$.

---

# Statement

> **Theorem (Determinant is Multiplicative, LADR 9.49).**
>
> (a) For any two operators $S, T \in \mathcal{L}(V)$,
> $$\det(ST) \;=\; (\det S)(\det T).$$
>
> (b) For any two $n \times n$ square matrices $A, B$ of the same size,
> $$\det(AB) \;=\; (\det A)(\det B).$$

> **Corollary (LADR 9.50).** An operator $T \in \mathcal{L}(V)$ is invertible if and only if $\det T \neq 0$. If invertible, $\det(T^{-1}) = 1/\det T$.

> **Corollary (similarity invariance, LADR 9.52).** For $T \in \mathcal{L}(V)$ and any invertible $S$, $\det(S^{-1} T S) = \det T$.

---

# Motivation

This is the single most-used theorem about determinants — and the one that makes the determinant a genuinely *useful* operation rather than just a number you compute. The multiplicativity says $\det$ is a **group homomorphism** from $\mathrm{GL}(V)$ to $\mathbb{F}^\times$, with kernel the special linear group $\mathrm{SL}(V)$. This is what makes $\det$ a similarity invariant, an invertibility test, and the source of every "compute this hard determinant by factoring" technique.

The conceptual content: the determinant measures how an operator scales $n$-dimensional volume, and composing two operators *multiplies* their scalings — that is the algebraic statement. Geometrically: applying $T$ first scales volume by $\det T$, then applying $S$ scales it by $\det S$, so the composition scales by $\det S \cdot \det T$. Sign-tracking is the same: orientation reversal composes as multiplication in $\{\pm 1\}$.

The reason multiplicativity is *not* obvious from the Leibniz formula is that the formula expresses $\det(AB)$ as a sum over permutations of products of entries of $AB$, and each entry of $AB$ is itself a sum (over the inner index). So $\det(AB)$ in the Leibniz form is a *triply-indexed* sum, and showing it equals $\det A \cdot \det B$ requires careful manipulation. From the abstract definition (the determinant is the scalar by which $T$ acts on alternating $n$-linear forms), multiplicativity is a one-line consequence — this is the chapter's central pedagogical point.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is mild — any pair of operators on the same finite-dimensional space — so the "source" question is: when does a problem secretly hand you a factorisation $T = ST'$?

**A matrix factorisation (LU, QR, SVD, etc.).** Any time a matrix is given as a product, multiplicativity reduces the determinant computation to factor-by-factor computation. The bridge: $A = L U$ for triangular $L, U$ gives $\det A = \det L \cdot \det U = $ product of diagonal entries — turning an arbitrary determinant into a trivial one via Gaussian elimination. Example problem: compute $\det$ of a matrix by LU decomposition.

**A change-of-basis formula $A_{\text{new}} = C^{-1} A_{\text{old}} C$.** Multiplicativity gives $\det A_{\text{new}} = \det(C^{-1}) \det A_{\text{old}} \det C = \det A_{\text{old}}$ (because $\det C^{-1} = 1/\det C$). So the determinant of an operator is basis-independent — exactly the similarity invariance. Example problem: prove that the determinant of an operator is well-defined independent of any matrix representation.

**An inverse $T^{-1}$ of a known operator.** Multiplicativity applied to $T T^{-1} = I$ gives $\det T \cdot \det T^{-1} = 1$, so $\det T^{-1} = 1/\det T$. This is a useful way to find the determinant of an inverse without explicitly computing the inverse.

**A polynomial in an operator.** For a polynomial $p(z)$ and an operator $T$ with eigenvalues $\lambda_i$, the operator $p(T)$ has eigenvalues $p(\lambda_i)$ (with multiplicities matched), so $\det p(T) = \prod p(\lambda_i)$. Multiplicativity is the engine: factor $p(z) = c \prod (z - \mu_j)$ and apply $\det \prod (T - \mu_j I) = \prod \det(T - \mu_j I)$.

**Targets (Output Amplification)**

The bare conclusion $\det(ST) = \det S \cdot \det T$ does a lot of work when combined with other facts.

**Combine with the eigenvalue product to derive $\det(T^k) = (\det T)^k$.** A polynomial in $T$ has determinant equal to the polynomial in $\det T$ when the polynomial is a pure power: $\det(T^k) = (\det T)^k$ for $k \geq 0$. For $k < 0$ (and $T$ invertible), $\det(T^k) = (\det T)^k$ as well. This is useful for asymptotic computations and for studying iterated linear processes.

**Combine with invertibility to characterise $\mathrm{GL}(V)$.** $T$ is invertible iff $\det T \neq 0$. So multiplicativity makes $\det$ the *defining* homomorphism of $\mathrm{GL}(V)$: an operator is invertible iff its image under $\det$ is nonzero. The kernel of $\det$ is $\mathrm{SL}(V)$, the volume-preserving (and orientation-preserving) operators.

**Combine with $\det I = 1$ to derive $\det T^{-1} = 1/\det T$.** From $T T^{-1} = I$ and multiplicativity, $\det T \cdot \det T^{-1} = \det I = 1$. So inverting an operator inverts the determinant.

**Combine with the transpose-determinant identity $\det A^t = \det A$ to derive results about cofactor expansion.** Multiplicativity plus $\det A^t = \det A$ gives $\det(A^t B^t) = \det((BA)^t) = \det(BA)$, which is consistent with $\det A \cdot \det B$. The interplay is what underlies the Cauchy-Binet formula and the cofactor expansion identities.

---

# Why Is It True

The proof is the most elegant in linear algebra — a single computation that flows from the abstract definition. Recall ([[Def - Determinant|the determinant]]) that $\det T$ is the unique scalar with $\alpha_T = (\det T) \alpha$ for every alternating $n$-linear form $\alpha$, where $\alpha_T(v_1, \dots, v_n) := \alpha(T v_1, \dots, T v_n)$.

Now compute $\alpha_{ST}$ for any alternating $n$-linear form $\alpha$:

$$\alpha_{ST}(v_1, \dots, v_n) = \alpha(ST v_1, \dots, ST v_n) = \alpha(S(T v_1), \dots, S(T v_n)) = \alpha_S(T v_1, \dots, T v_n) = (\alpha_S)_T(v_1, \dots, v_n).$$

So $\alpha_{ST} = (\alpha_S)_T = (\det T) \alpha_S = (\det T)(\det S) \alpha$. Therefore the scalar by which $ST$ acts on $\alpha$ is $(\det S)(\det T)$, which by definition is $\det(ST)$. Hence $\det(ST) = (\det S)(\det T)$.

**The mechanism summary:**

> **The map $\alpha \mapsto \alpha_T$ from $V^{(n)}_{\mathrm{alt}}$ to itself is "the action of $T$ on alternating $n$-linear forms"; composition of operators $T \to S \to ST$ corresponds to composition of actions $\alpha \to \alpha_T \to \alpha_{ST} = (\alpha_S)_T$, and on the one-dimensional space $V^{(n)}_{\mathrm{alt}}$ this composition multiplies the scalar factors $\det T \cdot \det S$.**

This is the abstract content of multiplicativity: $\det$ is a functor (sending operators to scalars) that commutes with composition. The fact that the underlying space $V^{(n)}_{\mathrm{alt}}$ is *one-dimensional* (the [[Def - Alternating Multilinear Form|alternating-uniqueness theorem]]) is what reduces "operator on $V^{(n)}_{\mathrm{alt}}$" to "scalar", and hence "composition of operators" to "multiplication of scalars".

---

# What Makes This Hard

The conceptual difficulty is almost zero — the proof is two lines from the abstract definition. The historical difficulty was that for centuries the determinant was *defined* by the Leibniz formula, and from that definition the multiplicativity is a non-trivial identity:

$$\sum_{\sigma} \operatorname{sign}(\sigma) (AB)_{\sigma(1), 1} \cdots (AB)_{\sigma(n), n} = \left(\sum_\sigma \operatorname{sign}(\sigma) A_{\sigma(1), 1} \cdots A_{\sigma(n), n}\right) \left(\sum_\tau \operatorname{sign}(\tau) B_{\tau(1), 1} \cdots B_{\tau(n), n}\right).$$

Expanding each $(AB)_{ij} = \sum_k A_{ik} B_{kj}$ on the left gives an $n^n$-term sum, which can be rearranged via permutation manipulations into the product on the right — but this is unenlightening. The lesson: choosing the *right definition* (alternating-multilinear-uniqueness) turns a "hard" identity into a one-line consequence. The abstract definition is what makes the theory go.

A common error: trying to prove multiplicativity by working with matrix entries directly. Resist this; the matrix-entry proof is unilluminating. Always reach for the abstract definition.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**

The action of an operator on alternating $n$-linear forms is "compose with the operator slot-wise". Composing two operators gives a composed action on the forms. Both actions are multiplication-by-scalar (because $\dim V^{(n)}_{\mathrm{alt}} = 1$), and the composition of scalar multiplications is multiplication of the scalars.

**Subgoal decomposition:**

1. **Recall the abstract definition.** $\det T$ is the scalar with $\alpha(Tv_1, \dots, Tv_n) = (\det T) \alpha(v_1, \dots, v_n)$ for all alternating $\alpha$ and all $v_i$.
   - *Hint:* This comes from $\dim V^{(n)}_{\mathrm{alt}} = 1$ and the linearity of $\alpha \mapsto \alpha_T$.
   - *Why needed:* The abstract definition is what makes multiplicativity a one-line computation.

2. **Compute $\alpha_{ST}(v_1, \dots, v_n)$.** Apply $\alpha$ to the tuple $(ST v_1, \dots, ST v_n)$ and rewrite.
   - *Hint:* Group $ST v_i = S(T v_i)$, and pull out $\det S$ from the $S$-application, then $\det T$ from the $T$-application.
   - *Why needed:* This is the core of the computation.

3. **Read off $\det(ST) = \det S \cdot \det T$.** By the abstract definition, the scalar by which $ST$ acts on $\alpha$ is by definition $\det(ST)$.
   - *Hint:* Use uniqueness of the scalar (any two scalars by which $\alpha \mapsto \alpha_{ST}$ acts must agree — there is only one such scalar by the one-dimensionality of $V^{(n)}_{\mathrm{alt}}$).

---

# Lemma Decomposition

> [!note]- Lemma 1: $(αT)_S = α_{ST}$ for the action on alternating forms
> **Statement:** Let $S, T \in \mathcal{L}(V)$ and $\alpha \in V^{(n)}_{\mathrm{alt}}$. Then $(α_T)_S(v_1, \dots, v_n) = α_{ST}(v_1, \dots, v_n)$ — wait, the *order* needs care: $(α_S)_T = α_{ST}$, not $(α_T)_S$. Let me re-state: $α_{ST}(v_1, \dots, v_n) = α(S T v_1, \dots, S T v_n) = α_S(T v_1, \dots, T v_n) = (α_S)_T(v_1, \dots, v_n)$. So $α_{ST} = (α_S)_T$.
>
> **Hint:** Just unfold the definitions and use associativity of composition of linear maps.
>
> **Why needed:** This is the structural identity that converts composition of operators into composition of actions on alternating forms.
>
> > [!note]- Full proof
> > By definition, $α_{ST}(v_1, \dots, v_n) = α(ST v_1, \dots, ST v_n)$. Apply associativity of composition: $ST v_i = S(T v_i)$. So
> > $$α_{ST}(v_1, \dots, v_n) = α(S(T v_1), \dots, S(T v_n)) = α_S(T v_1, \dots, T v_n) = (α_S)_T(v_1, \dots, v_n).$$
> > Hence $α_{ST} = (α_S)_T$.

> [!note]- Lemma 2: The action $α \mapsto α_T$ is linear in $α$
> **Statement:** For each $T \in \mathcal{L}(V)$, the map $α \mapsto α_T$ is a linear map from $V^{(n)}_{\mathrm{alt}}$ to itself.
>
> **Hint:** $α_T$ is alternating (because $α$ is and $T$ is well-defined), and linearity in $α$ follows from pointwise definitions.
>
> **Why needed:** Linearity is the property that lets us interpret $α \mapsto α_T$ as multiplication by a scalar, namely $\det T$, on the one-dimensional space $V^{(n)}_{\mathrm{alt}}$.
>
> > [!note]- Full proof
> > Alternating: if $v_j = v_k$ for some $j \neq k$, then $T v_j = T v_k$, so $α_T(v_1, \dots, v_n) = α(T v_1, \dots, T v_n) = 0$ by alternation of $α$. Linearity in $α$: $(c_1 α_1 + c_2 α_2)_T(v_1, \dots, v_n) = (c_1 α_1 + c_2 α_2)(T v_1, \dots, T v_n) = c_1 α_1(T v_1, \dots) + c_2 α_2(T v_1, \dots) = c_1 (α_1)_T + c_2 (α_2)_T$. Hence $α \mapsto α_T$ is a linear endomorphism of $V^{(n)}_{\mathrm{alt}}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $S, T \in \mathcal{L}(V)$. We prove $\det(ST) = \det S \cdot \det T$.
>
> **Step 0 — Preconditions.** $V$ is finite-dimensional, $n = \dim V$, and $V^{(n)}_{\mathrm{alt}}$ is one-dimensional ([[Def - Alternating Multilinear Form|by the alternating-uniqueness theorem]]).
>
> **Step 1 — Action on $α$.** Let $α \in V^{(n)}_{\mathrm{alt}}$ be nonzero. By the definition of the determinant ([[Def - Determinant|LADR 9.41]]), there are unique scalars $\det T, \det S$ such that
> $$α_T = (\det T) α \quad \text{and} \quad α_S = (\det S) α.$$
>
> **Step 2 — Action of $ST$ on $α$.** By Lemma 1, $α_{ST} = (α_S)_T$. Substituting the action of $S$:
> $$α_{ST} = (α_S)_T = ((\det S) α)_T.$$
> By Lemma 2 (linearity of the action), $((\det S) α)_T = (\det S) (α_T)$. Substituting the action of $T$:
> $$α_{ST} = (\det S)(α_T) = (\det S)(\det T) α.$$
>
> **Step 3 — Conclude.** By the definition of $\det(ST)$, $α_{ST} = (\det(ST)) α$. Combining with Step 2:
> $$(\det(ST)) α = (\det S)(\det T) α.$$
> Since $α \neq 0$, we may cancel to get
> $$\det(ST) = (\det S)(\det T). \qquad \blacksquare$$
>
> **For matrices:** Let $A, B$ be $n \times n$ matrices. Let $S, T \in \mathcal{L}(\mathbb{F}^n)$ be the operators with $\mathcal{M}(S) = A$ and $\mathcal{M}(T) = B$ in the standard basis. Then $\mathcal{M}(ST) = AB$, and by definition $\det A = \det S$, $\det B = \det T$, $\det(AB) = \det(ST)$. By the operator multiplicativity, $\det(ST) = \det S \cdot \det T$, hence $\det(AB) = \det A \cdot \det B$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Determinant of a Vandermonde matrix.** The Vandermonde matrix $V(x_1, \dots, x_n)$ has $(i, j)$-entry $x_j^{i-1}$, and $\det V = \prod_{i < j} (x_j - x_i)$. The proof can use multiplicativity by factoring $V$ as a product of simpler matrices, or alternating-multilinearity directly. Application: the Vandermonde determinant is nonzero iff all $x_i$ are distinct, which gives the criterion for polynomial interpolation to have a unique solution.

**Determinant of the matrix exponential equals exponential of the trace.** For an operator $T$ on a finite-dimensional vector space, $\det e^T = e^{\operatorname{tr} T}$. Proof: Multiplicativity gives $\det e^T = \det \lim_{n \to \infty} (I + T/n)^n = \lim_{n \to \infty} \det(I + T/n)^n = \lim_n (1 + \operatorname{tr}(T)/n + O(1/n^2))^n = e^{\operatorname{tr} T}$. This is the foundational identity connecting the determinant homomorphism to the trace linearisation, and the source of "Liouville's formula" in ODE theory.

**Cauchy-Binet formula.** For an $m \times n$ matrix $A$ and an $n \times m$ matrix $B$ (with $m \leq n$), $\det(AB) = \sum_S \det(A_S) \det(B_S)$, where the sum is over $m$-element subsets $S \subseteq \{1, \dots, n\}$ and $A_S, B_S$ are the appropriate sub-matrices. This generalises multiplicativity to non-square factors, and is the determinantal identity behind Plücker coordinates of Grassmannians.

**Resultant of two polynomials.** The resultant $\operatorname{Res}(f, g)$ of two polynomials $f, g \in \mathbb{F}[x]$ is the determinant of the Sylvester matrix (a specific matrix built from the coefficients of $f$ and $g$). Multiplicativity gives $\operatorname{Res}(fg, h) = \operatorname{Res}(f, h) \operatorname{Res}(g, h)$, which is the multiplicative property of the resultant. This is the determinantal identity that detects common roots of polynomials and is foundational in elimination theory and algebraic geometry.

---

# Bridges

- **[[Thm - Determinant Equals Product of Eigenvalues with Multiplicity|Determinant equals product of eigenvalues]]** — multiplicativity is the engine: in a basis where $T$ is upper-triangular (Schur theorem), the Leibniz formula collapses to the product of diagonal entries, which equal the eigenvalues. Multiplicativity is used implicitly in the reduction to upper-triangular form.

- **The determinant is a Lie group homomorphism $\det : \mathrm{GL}(V) \to \mathbb{F}^\times$.** Multiplicativity is exactly the homomorphism property. The kernel is $\mathrm{SL}(V)$, a normal subgroup, and the first isomorphism theorem for groups ([[Thm - First Isomorphism Theorem]]) gives $\mathrm{GL}(V) / \mathrm{SL}(V) \cong \mathbb{F}^\times$ — see [[Ex - Identifying a quotient with the first isomorphism theorem]] in [[Group Theory I — §1.1–1.2]].

- **Similarity invariance of $\det$.** From multiplicativity, $\det(S^{-1} T S) = \det(S^{-1}) \det T \det S = \det T$, since $\det(S^{-1}) = 1/\det S$. So similar operators have equal determinants, confirming that $\det$ is a property of an operator (not of its matrix representation).

- **Jacobian determinant in change of variables.** For a composition of diffeomorphisms $\Phi \circ \Psi$, the chain rule gives $D(\Phi \circ \Psi) = D\Phi \cdot D\Psi$, and multiplicativity gives $\det D(\Phi \circ \Psi) = \det D\Phi \cdot \det D\Psi$. So the "volume scaling factor" of a composition is the product of the individual scaling factors — the geometric content of multiplicativity in calculus.

---

# Unlocked by This

> [!tip] Group Homomorphism $\det : \mathrm{GL}(V) \to \mathbb{F}^\times$ *(from Group Theory and Lie Theory)*
> Multiplicativity makes $\det$ a group homomorphism, with kernel $\mathrm{SL}(V)$. Over $\mathbb{R}$, the image is $\mathbb{R}^\times = \mathbb{R} \setminus \{0\}$, and $\det^{-1}(\mathbb{R}^+) = \mathrm{GL}^+(V)$ is the orientation-preserving subgroup. The four-fold split $\mathrm{GL}(V) = \mathrm{GL}^+ \sqcup \mathrm{GL}^-$ (over $\mathbb{R}$) reflects the connected components of the Lie group.

> [!tip] Liouville's Theorem for Hamiltonian Flows *(from Classical Mechanics)*
> The Hamiltonian flow preserves phase-space volume: $\det DΦ_t = 1$ for the time-$t$ flow map. Proof via multiplicativity: $\det DΦ_t = \det e^{t \operatorname{Jac}(X_H)} = e^{t \operatorname{tr} \operatorname{Jac}(X_H)} = e^0 = 1$ (the trace of the Hamiltonian vector field's Jacobian is zero by Hamilton's equations).

> [!tip] Determinant and Matrix Inverse via the Adjugate *(LADR §9C)*
> Multiplicativity combined with the adjugate identity gives the Cramer formula $A^{-1} = \operatorname{adj}(A)/\det A$. See [[Thm - Cofactor Expansion and Cramer's Rule]].

> [!tip] Hodge Star and the Determinant *(from Differential Geometry)*
> On an oriented Riemannian manifold, the Hodge star $\star : \Lambda^k T^*M \to \Lambda^{n-k} T^*M$ depends on the volume form. The determinant appears in the local-coordinate expression of the Hodge star, and multiplicativity tracks how the Hodge star transforms under composition of charts.

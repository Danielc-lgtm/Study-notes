---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Generalized Eigenspace"
  - "Def - Generalized Eigenvector"
  - "Def - Nilpotent Operator"
  - "Def - Invariant Subspace"
  - "Def - Direct Sum"
  - "Thm - Null Spaces of Powers Stabilize"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbb{C}$ and $T \in \mathcal{L}(V)$. We write $E(\lambda, T) = \operatorname{null}(T - \lambda I)$ for the eigenspace and $G(\lambda, T) = \operatorname{null}(T - \lambda I)^{\dim V}$ for the generalized eigenspace at $\lambda$ — the equality with the "some-power" form is [[Thm - Null Spaces of Powers Stabilize]]. We restrict to $\mathbb{C}$ for this theorem; over $\mathbb{R}$ the result fails because real operators need not have eigenvalues at all. Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

---

# Statement

> **Theorem ([[Def - Generalized Eigenspace|Generalized Eigenspace]] Decomposition).** Suppose $\mathbf{F} = \mathbb{C}$ and $T \in \mathcal{L}(V)$. Let $\lambda_1, \dots, \lambda_m$ be the distinct eigenvalues of $T$. Then:
>
> (a) Each generalized eigenspace $G(\lambda_k, T)$ is invariant under $T$.
>
> (b) The restriction $(T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent for each $k = 1, \dots, m$.
>
> (c) $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$.

In particular, every operator on a finite-dimensional complex vector space is, on each generalized eigenspace, an eigenvalue times the identity plus a nilpotent operator.

---

# Motivation

This is the headline theorem of the chapter — the structural backbone of operators on complex vector spaces. It says: every operator $T$ on $V$ decomposes $V$ into a direct sum of $T$-invariant [[Def - Subspace|subspaces]], one per eigenvalue, and on each of these [[Def - Subspace|subspaces]] $T$ looks like the simplest possible thing: a scalar $\lambda_k$ plus a nilpotent operator $N_k$.

The theorem is the answer to the question "what is an operator on a complex space?" Eigenvectors alone are not enough: when $T$ is not diagonalisable, the sum of eigenspaces $\bigoplus E(\lambda_k, T)$ falls short of $V$. The remedy is to replace eigenspaces by generalized eigenspaces, and the remedy succeeds: $\bigoplus G(\lambda_k, T)$ always equals $V$. This is the gain.

The price is that on each generalized eigenspace the operator $T$ is no longer a scalar — it is a scalar plus a nilpotent. But nilpotent operators are completely understood (we will see in [[Thm - Existence of Jordan Form]] that every nilpotent has a canonical "Jordan basis"), so the cost is minimal. The combined picture is: every operator on a complex space is a direct sum of pieces, each piece being "$\lambda I + (\text{nilpotent})$" for some eigenvalue $\lambda$. This is the **Jordan–Chevalley decomposition** in its earliest form, and everything in chapter 8 — characteristic polynomials, Jordan forms, square roots, traces — is a corollary.

The need for the complex field is sharp. Over $\mathbb{R}$ an operator may have no eigenvalues at all (the rotation matrix on $\mathbb{R}^2$ has no real eigenvalues), and then the "distinct eigenvalues $\lambda_1, \dots, \lambda_m$" of the statement do not exist. The same operator over $\mathbb{C}$ has eigenvalues $\pm i$ and the decomposition goes through; the cleanest way to handle real operators is to **complexify** $V$ (replace it by $V \otimes_\mathbb{R} \mathbb{C}$, the tensor product with $\mathbb{C}$) and run the complex theory on the complexification.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is $\mathbf{F} = \mathbb{C}$ and $V$ finite-dimensional — broad. The interesting question is when the *output* (the generalized eigenspace decomposition) is invoked, often because the structural picture it provides is exactly what some other problem secretly needs.

The first disguised source is **a problem about polynomials of $T$**. Whenever a problem involves $p(T)$ for a polynomial $p$ — characteristic polynomial, minimal polynomial, $e^{tT}$ as a power series, $f(T)$ for a holomorphic $f$ — the generalized eigenspace decomposition reduces the question to computing $p(\lambda_k I + N_k)$ on each piece, which by Taylor expansion is $\sum_j \frac{p^{(j)}(\lambda_k)}{j!} N_k^j$, a *finite* sum. *Example problem:* prove the Cayley–Hamilton theorem, $p_T(T) = 0$. The decomposition reduces this to checking that the characteristic polynomial $p_T(z) = \prod (z - \lambda_k)^{d_k}$ kills each generalized eigenspace, which is immediate because $(T - \lambda_k I)^{d_k}|_{G(\lambda_k, T)} = 0$ (the nilpotent on a space of dimension $d_k$ raised to power $d_k$ is zero by [[Thm - Null Spaces of Powers Stabilize]]).

The second disguised source is **a problem about diagonalisability or its failure**. Diagonalisability is the property "$G(\lambda, T) = E(\lambda, T)$ for every $\lambda$", and the decomposition exhibits the obstruction: vectors in $G(\lambda, T) \setminus E(\lambda, T)$ are generalized eigenvectors that are not eigenvectors, and they fill out the gap when $T$ is not diagonalisable. *Example problem:* prove that an operator on $\mathbb{C}^n$ is diagonalisable iff the algebraic and geometric multiplicities agree at every eigenvalue. The decomposition gives the algebraic multiplicity as $\dim G(\lambda, T)$ and the geometric as $\dim E(\lambda, T)$, and diagonalisability is exactly $E = G$ everywhere.

The third disguised source is **a problem about $T$-invariant subspaces**. The generalized eigenspaces are the maximal $T$-invariant subspaces on which $T - \lambda I$ is nilpotent — equivalently, the **primary components** of $V$ as a $\mathbb{C}[x]$-module. Any decomposition of $V$ into $T$-invariant subspaces is a refinement of the generalized eigenspace decomposition (and any direct sum decomposition into $T$-invariant subspaces must coarsen the Jordan form, which is the maximal such refinement). *Example problem:* exercise 14 of §8C in LADR — prove that there does not exist a direct sum decomposition of $V$ into two nonzero $T$-invariant subspaces iff the minimal polynomial of $T$ is $(z - \lambda)^{\dim V}$ for some $\lambda$. The decomposition is the bridge.

**Targets (Output Amplification)**

The bare conclusion is the direct-sum decomposition. Combined with other facts it does much more.

Combine the decomposition with the **structure of nilpotent operators**. On each piece, $(T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent, and nilpotent operators admit a Jordan basis ([[Thm - Existence of Jordan Form]] for the nilpotent case is the special case [[Thm - Existence of Jordan Form|8.45]] of LADR). Assembling the Jordan bases for each restricted nilpotent gives a Jordan basis for $T$ — the further result $E$ here is the full [[Thm - Existence of Jordan Form|Jordan form theorem]]. Without the generalized eigenspace decomposition, the Jordan form is only available for nilpotent operators; the decomposition is what extends it to all operators on a complex space.

Combine the decomposition with **the Taylor series of a function holomorphic on the spectrum**. On each $G(\lambda_k, T)$, the operator $f(T)|_{G(\lambda_k, T)} = \sum_j \frac{f^{(j)}(\lambda_k)}{j!} N_k^j$ is well-defined as a *finite* sum (the nilpotent vanishes after at most $d_k$ powers). The further result $E$ is the **holomorphic functional calculus** in finite dimensions: for any function $f$ holomorphic on a neighbourhood of the spectrum of $T$, the operator $f(T)$ is uniquely defined and the assignment $f \mapsto f(T)$ is a ring homomorphism. Square roots, logarithms, exponentials, and roots of unity of $T$ all fall out of this construction.

Combine the decomposition with the **dimension formula**. $\dim V = \sum_k \dim G(\lambda_k, T) = \sum_k d_k$, where $d_k$ is the algebraic multiplicity. The further result $E$ is that the characteristic polynomial $p_T(z) = \prod (z - \lambda_k)^{d_k}$ has degree $\dim V$ — see [[Def - Algebraic and Geometric Multiplicity]] and the chapter's [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces#Concept Map|concept map]] for the §8B treatment of the characteristic polynomial. Combined with $\operatorname{tr} T =$ negative coefficient of $z^{\dim V - 1}$ and $\det T = (-1)^{\dim V}$ times the constant term, this gives the elementary symmetric polynomials of the eigenvalues with multiplicity.

---

# Why Is It True

Here is the picture in words, before any formal argument. We want to write $V$ as a direct sum of "pieces" — $T$-invariant subspaces, on each of which $T$ has simple behaviour. The simplest behaviour we can hope for is "$T$ acts as a scalar" (eigenvalue), or failing that, "$T - \lambda I$ acts nilpotently" (generalized eigenvalue). These two are exactly the generalized eigenspaces $G(\lambda, T)$.

The question is why the generalized eigenspaces *fill out all of $V$*. The eigenspaces $E(\lambda, T)$ do not, in general — that is what non-diagonalisability is. Why does enlarging "eigenspace" to "generalized eigenspace" rescue the situation?

The answer is the **Fitting decomposition**, the corollary of [[Thm - Null Spaces of Powers Stabilize]]: for any operator $S$ on $V$, $V = \operatorname{null} S^{\dim V} \oplus \operatorname{range} S^{\dim V}$. Apply this with $S = T - \lambda_1 I$, where $\lambda_1$ is an eigenvalue of $T$. Then $\operatorname{null} S^{\dim V} = G(\lambda_1, T)$ is the first generalized eigenspace, and $\operatorname{range} S^{\dim V}$ is a complementary $T$-invariant subspace. The operator $T$ on this complement has *one fewer* eigenvalue than on $V$ (since $\lambda_1$ has been "removed" — the restriction of $T$ to the range has $\lambda_1$ no longer as an eigenvalue), so by induction on the number of eigenvalues, the complement decomposes into the remaining generalized eigenspaces, and assembling gives $V = G(\lambda_1, T) \oplus G(\lambda_2, T) \oplus \cdots$.

But wait — we need $\lambda_1$ to be an eigenvalue, which on $\mathbb{C}$ is automatic (every operator has at least one eigenvalue, by the [[Thm - Fundamental Theorem of Algebra|Fundamental Theorem of Algebra]]). And we need the restriction of $T$ to the complement to have one fewer eigenvalue, which requires that $\lambda_1$ is *not* an eigenvalue of $T|_{\operatorname{range} S^{\dim V}}$ — this is the slightly subtle step, and it is where the proof needs care.

**Mechanism summary: the Fitting decomposition for $T - \lambda I$ peels off the $\lambda$-generalized eigenspace and leaves a $T$-invariant complement on which $\lambda$ is no longer an eigenvalue, allowing induction on the number of eigenvalues.**

The deeper insight is that **the generalized eigenspaces are forced** — they are not a choice but a consequence of two facts: (i) every operator on a complex space has an eigenvalue (FTA); (ii) once one eigenvalue is "peeled off" via the Fitting decomposition, the rest decomposes the same way by induction. The construction is canonical: the generalized eigenspaces depend only on $T$ and not on any choice of basis or representative. They are the *only* way to write $V$ as a direct sum of $T$-invariant subspaces on each of which $T -$ (some scalar) is nilpotent.

The connection to module theory makes the inevitability transparent. Regard $V$ as a $\mathbb{C}[x]$-module via $T$ (`[[Def - The Module of a Linear Operator]]`). The structure theorem for finitely generated [[Def - Module|modules]] over a PID ([[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain]]) decomposes $V$ into a direct sum of primary cyclic [[Def - Module|modules]] $\mathbb{C}[x]/(x - \lambda_k)^{n_{k, i}}$, where the primes of $\mathbb{C}[x]$ are exactly the linear polynomials $(x - \lambda)$. The **primary decomposition** ([[Thm - Primary Decomposition Theorem]]) [[Def - Group|groups]] summands by prime, and the $(x - \lambda_k)$-primary component is exactly $G(\lambda_k, T)$. So the generalized eigenspace decomposition is the linear-algebra incarnation of the primary decomposition for $\mathbb{C}[x]$-modules — a result that is forced by general algebraic principles, not specific to linear algebra.

---

# What Makes This Hard

The conceptual content is straightforward; the technical difficulty is in (i) showing the sum of generalized eigenspaces is *direct* (no nontrivial intersections), and (ii) showing the sum is *all of $V$* (the inductive existence argument). The directness comes from "generalized eigenvectors corresponding to distinct eigenvalues are linearly independent" — a non-trivial fact requiring a binomial-expansion argument (LADR 8.12). The completeness comes from the induction sketched above, which depends on the Fitting decomposition and on the fact that *the restriction of $T$ to $\operatorname{range}(T - \lambda I)^{\dim V}$ has $\lambda$ as a non-eigenvalue* — the slightly subtle step where one has to track what eigenvalues the restricted operator has.

The most common error is to confuse the algebraic and geometric multiplicities, or to assume the eigenspaces (not generalized eigenspaces) decompose $V$ — the latter is false unless $T$ is diagonalisable. The next most common error is to forget that the result requires $\mathbf{F} = \mathbb{C}$ and try to apply it to a real operator without complexifying.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove three things separately and combine. (i) Each $G(\lambda_k, T)$ is $T$-invariant. (ii) The restriction $(T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent. (iii) The generalized eigenspaces have trivial pairwise intersection (directness) and span $V$ (completeness). The key tool throughout is [[Thm - Null Spaces of Powers Stabilize]] applied to $T - \lambda_k I$, which tells us the generalized eigenspace is $\operatorname{null}(T - \lambda_k I)^{\dim V}$ and gives the Fitting decomposition.

**Subgoal decomposition:**

1. **Invariance.** Show that $T$ maps $G(\lambda_k, T)$ into itself.
   - *Hint:* $T$ commutes with $(T - \lambda_k I)^{\dim V}$ (any operator commutes with a polynomial in itself).
   - *Why needed:* Without invariance the "restriction of $T$ to $G(\lambda_k, T)$" is not even a well-defined operator on $G(\lambda_k, T)$, and the nilpotence claim is meaningless.

2. **Nilpotence of the shift.** Show that $(T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent — specifically, that $((T - \lambda_k I)|_{G(\lambda_k, T)})^{\dim V} = 0$.
   - *Hint:* Directly from $G(\lambda_k, T) = \operatorname{null}(T - \lambda_k I)^{\dim V}$.
   - *Why needed:* This is the structural content "$T = \lambda_k I +$ nilpotent" on each piece.

3. **Linear independence of generalized eigenvectors.** Show that nonzero generalized eigenvectors for distinct eigenvalues are linearly independent.
   - *Hint:* Suppose $v_1 + \cdots + v_m = 0$ with each $v_k \in G(\lambda_k, T)$. Apply $(T - \lambda_m I)^{\dim V}$ to kill $v_m$; iterate. Use uniqueness of the eigenvalue associated with a generalized eigenvector (LADR 8.11).
   - *Why needed:* This is the directness of the sum — without it, the sum could have nontrivial intersections.

4. **Existence of a basis of generalized eigenvectors.** Show that on $\mathbf{F} = \mathbb{C}$, $V$ has a basis consisting of generalized eigenvectors of $T$.
   - *Hint:* Induct on $\dim V$. Pick an eigenvalue $\lambda$ (FTA). By the Fitting decomposition, $V = G(\lambda, T) \oplus \operatorname{range}(T - \lambda I)^{\dim V}$. Either the range is zero (then $V = G(\lambda, T)$ is one piece), or apply the induction hypothesis to the range (which is strictly smaller-dimensional than $V$).
   - *Why needed:* This is the completeness of the sum — without it, the generalized eigenspaces might not span $V$.

5. **Direct-sum decomposition.** Assemble (3) and (4) to conclude $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$.
   - *Hint:* Linear independence (3) gives directness; existence of basis (4) gives completeness; combine.
   - *Why needed:* The final claim.

---

# Lemma Decomposition

> [!note]- Lemma 1: Each generalized eigenspace is $T$-invariant
> **Statement:** For any $\lambda \in \mathbf{F}$, $G(\lambda, T) = \operatorname{null}(T - \lambda I)^{\dim V}$ is invariant under $T$ — that is, $T(G(\lambda, T)) \subseteq G(\lambda, T)$.
>
> **Hint:** $T$ commutes with any polynomial in $T$, including $(T - \lambda I)^{\dim V}$. So $T$ preserves the kernel of $(T - \lambda I)^{\dim V}$.
>
> **Why needed:** Without invariance, the restriction $T|_{G(\lambda, T)}$ is not a self-map of $G(\lambda, T)$, and we cannot speak of its nilpotency.
>
> > [!note]- Full proof
> > Suppose $v \in G(\lambda, T)$, so $(T - \lambda I)^{\dim V} v = 0$. We must show $T v \in G(\lambda, T)$, that is, $(T - \lambda I)^{\dim V} (T v) = 0$.
> >
> > The operators $T$ and $T - \lambda I$ commute (both are polynomials in $T$). Hence $T$ commutes with $(T - \lambda I)^{\dim V}$. So
> > $$(T - \lambda I)^{\dim V} (T v) = T \cdot (T - \lambda I)^{\dim V} v = T \cdot 0 = 0.$$
> > Hence $T v \in G(\lambda, T)$.

> [!note]- Lemma 2: $(T - \lambda I)|_{G(\lambda, T)}$ is nilpotent
> **Statement:** The restriction of $T - \lambda I$ to $G(\lambda, T)$ is nilpotent.
>
> **Hint:** Directly: $G(\lambda, T) = \operatorname{null}(T - \lambda I)^{\dim V}$, so $(T - \lambda I)^{\dim V}|_{G(\lambda, T)} = 0$.
>
> **Why needed:** This is the structural conclusion "$T = \lambda I +$ nilpotent on $G(\lambda, T)$", the central content of the theorem.
>
> > [!note]- Full proof
> > By Lemma 1, the restriction $(T - \lambda I)|_{G(\lambda, T)}$ is a well-defined operator on $G(\lambda, T)$.
> >
> > If $v \in G(\lambda, T)$ then by definition $(T - \lambda I)^{\dim V} v = 0$. So
> > $$((T - \lambda I)|_{G(\lambda, T)})^{\dim V} = 0$$
> > as an operator on $G(\lambda, T)$. By definition (`[[Def - Nilpotent Operator]]`), this restriction is nilpotent. In fact its nilpotency index is at most $\dim G(\lambda, T) \leq \dim V$, by [[Thm - Null Spaces of Powers Stabilize]] applied to the restricted operator.

> [!note]- Lemma 3: Generalized eigenvectors for distinct eigenvalues are linearly independent
> **Statement:** Let $v_1, \dots, v_m \in V$ be generalized eigenvectors of $T$ corresponding to *distinct* eigenvalues $\lambda_1, \dots, \lambda_m$. Then $v_1, \dots, v_m$ is linearly independent.
>
> **Hint:** Suppose there is a nontrivial relation. Choose one with the smallest length $m$, so all $a_k \neq 0$. Apply $(T - \lambda_m I)^{\dim V}$ to both sides, which kills $v_m$ but leaves the other $v_k$'s as nonzero generalized eigenvectors for distinct eigenvalues (using LADR 8.11, uniqueness of the eigenvalue associated to a generalized eigenvector). This gives a relation of length $m - 1$, contradicting minimality.
>
> **Why needed:** This is what makes the sum of generalized eigenspaces direct.
>
> > [!note]- Full proof
> > Suppose for contradiction that the list is linearly dependent. Then there is a smallest positive integer $m$ such that some list $v_1, \dots, v_m$ of generalized eigenvectors for distinct eigenvalues $\lambda_1, \dots, \lambda_m$ is linearly dependent. Note $m \geq 2$ (a single nonzero vector is independent).
> >
> > By the minimality of $m$, in any nontrivial relation $a_1 v_1 + \cdots + a_m v_m = 0$, all coefficients $a_k$ are nonzero (else dropping the zero coefficients gives a shorter dependent list).
> >
> > Let $n = \dim V$. Apply $(T - \lambda_m I)^n$ to both sides of the relation:
> > $$a_1 (T - \lambda_m I)^n v_1 + \cdots + a_{m-1} (T - \lambda_m I)^n v_{m-1} + a_m (T - \lambda_m I)^n v_m = 0.$$
> > The last term vanishes since $v_m \in G(\lambda_m, T) = \operatorname{null}(T - \lambda_m I)^n$. So
> > $$a_1 (T - \lambda_m I)^n v_1 + \cdots + a_{m-1} (T - \lambda_m I)^n v_{m-1} = 0. \quad (\ast)$$
> >
> > For $k \in \{1, \dots, m - 1\}$, the vector $(T - \lambda_m I)^n v_k$ is a generalized eigenvector for $\lambda_k$: by uniqueness of the eigenvalue (LADR 8.11), it cannot be a generalized eigenvector for $\lambda_m$, and the computation
> > $$(T - \lambda_k I)^n \big((T - \lambda_m I)^n v_k\big) = (T - \lambda_m I)^n \big((T - \lambda_k I)^n v_k\big) = (T - \lambda_m I)^n \cdot 0 = 0$$
> > shows it is in $G(\lambda_k, T)$ (using that $(T - \lambda_k I)$ and $(T - \lambda_m I)$ commute, which they do as polynomials in $T$). Moreover, $(T - \lambda_m I)^n v_k \neq 0$ — otherwise $v_k$ would be a generalized eigenvector for both $\lambda_k$ and $\lambda_m$, contradicting LADR 8.11.
> >
> > So $(\ast)$ is a nontrivial relation among $m - 1$ nonzero generalized eigenvectors $w_1 := (T - \lambda_m I)^n v_1, \dots, w_{m-1} := (T - \lambda_m I)^n v_{m-1}$, corresponding to distinct eigenvalues $\lambda_1, \dots, \lambda_{m-1}$. This contradicts the minimality of $m$.

> [!note]- Lemma 4: $V$ has a basis of generalized eigenvectors (when $\mathbf{F} = \mathbb{C}$)
> **Statement:** Suppose $\mathbf{F} = \mathbb{C}$ and $T \in \mathcal{L}(V)$. Then $V$ has a basis consisting of generalized eigenvectors of $T$.
>
> **Hint:** Induct on $\dim V$. Use the [[Thm - Fundamental Theorem of Algebra|Fundamental Theorem of Algebra]] to get an eigenvalue $\lambda$. Apply [[Thm - Null Spaces of Powers Stabilize]] to $T - \lambda I$ to split $V = G(\lambda, T) \oplus \operatorname{range}(T - \lambda I)^{\dim V}$. If the range is zero, $V = G(\lambda, T)$. Otherwise, apply induction to the range (which is strictly smaller-dimensional and $T$-invariant).
>
> **Why needed:** This is the *existence* heart of the theorem: that generalized eigenspaces span $V$ on a complex space. It requires the complex field crucially (via FTA).
>
> > [!note]- Full proof
> > Let $n = \dim V$. We use strong induction on $n$.
> >
> > **Base case ($n = 1$):** $V$ is one-dimensional. Any nonzero vector is an eigenvector of $T$ (with the eigenvalue determined by $T$ acting on it as a scalar), hence a generalized eigenvector. So $V$ has a basis of generalized eigenvectors.
> >
> > **Induction step ($n > 1$):** Assume the result for all smaller-dimensional spaces. Since $\mathbf{F} = \mathbb{C}$, $T$ has at least one eigenvalue $\lambda$ (by the Fundamental Theorem of Algebra applied to the minimal polynomial, or alternatively to the characteristic polynomial — every operator on a finite-dimensional complex space has at least one eigenvalue; see [[Thm - Existence of Eigenvalues on Complex Vector Spaces]]).
> >
> > By [[Thm - Null Spaces of Powers Stabilize]] applied to $S := T - \lambda I$,
> > $$V = \operatorname{null} S^n \oplus \operatorname{range} S^n = G(\lambda, T) \oplus \operatorname{range}(T - \lambda I)^n.$$
> >
> > **Case 1:** $G(\lambda, T) = V$. Then every nonzero vector is a generalized eigenvector for $\lambda$, and any basis of $V$ is a basis of generalized eigenvectors. Done.
> >
> > **Case 2:** $G(\lambda, T) \neq V$, so $W := \operatorname{range}(T - \lambda I)^n$ is a nontrivial proper subspace. Since $G(\lambda, T) \neq \{0\}$ (because $\lambda$ is an eigenvalue and so $\operatorname{null}(T - \lambda I)$ has nonzero vectors, hence so does $G(\lambda, T) \supseteq \operatorname{null}(T - \lambda I)$), we have $0 < \dim W < n$.
> >
> > $W$ is $T$-invariant: $T$ commutes with $(T - \lambda I)^n$, so $T(W) = T(\operatorname{range}(T - \lambda I)^n) = \operatorname{range}(T \cdot (T - \lambda I)^n) = \operatorname{range}((T - \lambda I)^n \cdot T) \subseteq \operatorname{range}(T - \lambda I)^n = W$.
> >
> > Let $S' = T|_W$ be the restriction. By induction (since $\dim W < n$), $W$ has a basis $w_1, \dots, w_{\dim W}$ consisting of generalized eigenvectors of $S'$. Each $w_j$ is a generalized eigenvector of $T$ too: $(T - \mu I)^k w_j = (S' - \mu I)^k w_j = 0$ for some $k$ and some eigenvalue $\mu$ of $S'$, and $\mu$ is also an eigenvalue of $T$.
> >
> > Let $g_1, \dots, g_{\dim G(\lambda, T)}$ be any basis of $G(\lambda, T)$; these are all generalized eigenvectors of $T$ for $\lambda$. Combining $g$'s and $w$'s gives a list of generalized eigenvectors of $T$ of length $\dim G(\lambda, T) + \dim W = n$ that spans $V$ (because $V = G(\lambda, T) \oplus W$). By dimensional considerations, it is a basis of $V$.

> [!note]- Lemma 5: Direct-sum decomposition
> **Statement:** $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$, where $\lambda_1, \dots, \lambda_m$ are the distinct eigenvalues of $T$.
>
> **Hint:** Existence of a basis of generalized eigenvectors (Lemma 4) gives $V = G(\lambda_1, T) + \cdots + G(\lambda_m, T)$ (sum). Linear independence (Lemma 3) gives the directness of the sum.
>
> **Why needed:** This is the final structural statement.
>
> > [!note]- Full proof
> > By Lemma 4, $V$ has a basis of generalized eigenvectors. Each basis vector lies in some $G(\lambda_k, T)$. So $V = G(\lambda_1, T) + \cdots + G(\lambda_m, T)$ as a sum of subspaces.
> >
> > To show the sum is *direct*, suppose $v_1 + \cdots + v_m = 0$ with each $v_k \in G(\lambda_k, T)$. The nonzero $v_k$'s would be a list of generalized eigenvectors for distinct eigenvalues, contradicting Lemma 3 (linear independence). So each $v_k = 0$, and the sum is direct: $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathbf{F} = \mathbb{C}$, $T \in \mathcal{L}(V)$, $\dim V = n$, and let $\lambda_1, \dots, \lambda_m$ be the distinct eigenvalues of $T$.
>
> **Part (a) — invariance.** By Lemma 1, each $G(\lambda_k, T)$ is invariant under $T$.
>
> **Part (b) — nilpotence of the shift.** By Lemma 2, $(T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent for each $k$.
>
> **Part (c) — direct-sum decomposition.** By Lemma 5, $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Markov chains and the spectral theory of stochastic matrices.** Let $P$ be the transition matrix of an irreducible finite Markov chain. Then $1$ is an eigenvalue of $P$ with multiplicity $1$, and all other eigenvalues have modulus $\leq 1$. The generalized eigenspace decomposition $\mathbb{C}^n = G(1, P) \oplus \bigoplus_{\lambda \neq 1} G(\lambda, P)$ splits the state space into the *stationary direction* (the unique stationary distribution) and the *transient directions* (vectors that decay under iteration). The rate of convergence to stationarity is governed by the second-largest eigenvalue $|\lambda_2|$, and the *Jordan structure* at $|\lambda| < 1$ controls whether the convergence is geometric or polynomial-times-geometric — secular terms appear when the Jordan blocks at $\lambda$ have size $\geq 2$.

**Linear ODE systems and the matrix exponential.** For a linear ODE $\dot x = A x$ on $\mathbb{C}^n$, the solution is $x(t) = e^{tA} x_0$. The generalized eigenspace decomposition gives $\mathbb{C}^n = \bigoplus G(\lambda_k, A)$, and on each piece $e^{tA}|_{G(\lambda_k, A)} = e^{\lambda_k t} e^{t N_k}$ where $N_k$ is nilpotent. The polynomial part $e^{t N_k} = \sum_{j=0}^{d_k - 1} \frac{(t N_k)^j}{j!}$ is a polynomial in $t$, giving the explicit form $x(t) = \sum_k e^{\lambda_k t} p_k(t)$ where $p_k$ is a polynomial of degree at most "largest Jordan block at $\lambda_k$ minus one". The decomposition is *how* one computes the matrix exponential explicitly, and the Jordan structure dictates the polynomial degrees in the solution. See exercise [[Exercise Index - §8B–C Generalized Eigenspace Decomposition and Jordan Form|matrix exponential via Jordan]].

**Quantum mechanics and the Lindbladian.** For a finite-dimensional open quantum system, the **Lindbladian** $\mathcal{L}$ is a linear operator on the space of density matrices ($n \times n$ matrices on $\mathbb{C}^n$). Its generalized eigenspace decomposition gives the time evolution $\rho(t) = e^{t \mathcal{L}} \rho_0$, with eigenvalues $\lambda$ having $\operatorname{Re} \lambda \leq 0$ (dissipation), with the kernel ($\lambda = 0$) being the space of *steady states* and the nonzero-real-part eigenvalues giving the decay rates of various deviations from steady state. The generalized eigenspace decomposition is exactly the *spectral structure of dissipative quantum dynamics*, and Jordan blocks of size $\geq 2$ correspond to **exceptional points** in non-Hermitian quantum systems — points in parameter space where the decomposition degenerates.

---

# Bridges

- **[[Thm - Primary Decomposition Theorem|Primary Decomposition Theorem]] in [[Modules II — §3.3–3.4]]** — the generalized eigenspace decomposition is literally the primary decomposition of $V$ as a $\mathbb{C}[x]$-module via $T$. Regard $V$ as a module over $\mathbb{C}[x]$ where $x$ acts as $T$ (see `[[Def - The Module of a Linear Operator]]`); then $V$ is finitely generated and torsion (annihilated by the minimal polynomial of $T$). The primes of $\mathbb{C}[x]$ are exactly the linear polynomials $(x - \lambda)$ (since $\mathbb{C}$ is algebraically closed and $\mathbb{C}[x]$ is a PID), and the primary decomposition says $V = \bigoplus V_{(x - \lambda_k)}$ where $V_{(x - \lambda_k)}$ is the $(x - \lambda_k)$-primary component — the subspace annihilated by some power of $(x - \lambda_k)$ — which is exactly $G(\lambda_k, T)$. So the theorem here is a special case of a result that holds for any finitely generated torsion module over any PID.

- **[[Thm - Existence of Jordan Form|Existence of Jordan Form]]** — direct corollary. The Jordan form is obtained by finding, for each eigenvalue $\lambda_k$, a Jordan basis of $G(\lambda_k, T)$ adapted to the nilpotent operator $(T - \lambda_k I)|_{G(\lambda_k, T)}$. The hard work — both in the proof and in computation — is in the nilpotent case; the generalized eigenspace decomposition is the easy reduction.

- **[[Thm - Cayley-Hamilton (Minimal-Polynomial Form)|Cayley–Hamilton Theorem]]** — immediate corollary. The characteristic polynomial $p_T(z) = \prod (z - \lambda_k)^{d_k}$ with $d_k = \dim G(\lambda_k, T)$ kills $G(\lambda_k, T)$ for each $k$ — because $(T - \lambda_k I)^{d_k}|_{G(\lambda_k, T)} = 0$ (the nilpotent restricted to a space of dimension $d_k$ raised to that power is zero by [[Thm - Null Spaces of Powers Stabilize]]) — and the other factors $(T - \lambda_j I)^{d_j}$ commute with the rest, so the product $p_T(T)$ kills everything. The generalized eigenspace decomposition is what makes the proof one line; the determinant-based proof in [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] is more roundabout.

- **[[Thm - Conditions for Diagonalizability|Conditions for Diagonalizability]]** — direct corollary. $T$ is diagonalisable iff $G(\lambda, T) = E(\lambda, T)$ for every eigenvalue $\lambda$ (iff the restricted nilpotents $N_k$ are all zero, iff the algebraic and geometric multiplicities agree everywhere, iff the minimal polynomial has distinct linear factors). All four conditions follow from the structure $T|_{G(\lambda_k, T)} = \lambda_k I + N_k$ and the observation that $N_k = 0 \iff E(\lambda_k, T) = G(\lambda_k, T)$.

- **Fitting decomposition** — for $S \in \mathcal{L}(V)$, $V = \operatorname{null} S^{\dim V} \oplus \operatorname{range} S^{\dim V}$. Applying this to $S = T - \lambda I$ for an eigenvalue $\lambda$ gives the *single-eigenvalue version* of the generalized eigenspace decomposition: $V = G(\lambda, T) \oplus W$ for a $T$-invariant complement $W$. The full decomposition is the iterated Fitting decomposition.

---

# Unlocked by This

> [!tip] Jordan Form *(from this topic, see [[Thm - Existence of Jordan Form]])*
> The generalized eigenspace decomposition is the first step of the Jordan form construction; the second step is to find a Jordan basis of each generalized eigenspace adapted to the nilpotent restriction.

> [!tip] Holomorphic Functional Calculus *(from Functional Analysis)*
> For any function $f$ holomorphic on a neighbourhood of the spectrum $\{\lambda_1, \dots, \lambda_m\}$, the operator $f(T)$ is well-defined as $\bigoplus f(T)|_{G(\lambda_k, T)} = \bigoplus \sum_j \frac{f^{(j)}(\lambda_k)}{j!} N_k^j$ — a finite Taylor sum on each piece. This gives square roots, logarithms, exponentials, and roots of unity of $T$ uniformly.

> [!tip] Spectral Projections *(from Functional Analysis)*
> The canonical projection $P_k : V \to G(\lambda_k, T)$ along the other generalized eigenspaces is well-defined and is a polynomial in $T$ — explicitly, $P_k$ is a polynomial $p_k(T)$ where $p_k$ satisfies $p_k(z) \equiv \delta_{kj} \pmod{(z - \lambda_j)^{d_j}}$ for each $j$ (Lagrange interpolation modulo prime powers, equivalently the Chinese Remainder Theorem for $\mathbb{C}[x]$).

> [!tip] Linear ODE Theory and the Matrix Exponential *(from ODE Theory)*
> Solutions of $\dot x = Ax$ on $\mathbb{C}^n$ are determined by the generalized eigenspace decomposition of $A$. Each $G(\lambda_k, A)$ contributes solutions of the form $e^{\lambda_k t} p_k(t)$ where $p_k$ is a polynomial of degree at most $d_k - 1$. The polynomial parts arise *only* when there are Jordan blocks of size $\geq 2$ — when $A$ is diagonalisable, the solutions are pure exponentials with no polynomial multipliers.

> [!tip] Structure Theorem for Modules over a PID *(from Module Theory)*
> The generalized eigenspace decomposition is the special case of the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]] applied to the $\mathbb{C}[x]$-module $V$. The further refinement of each $G(\lambda_k, T)$ into cyclic modules $\mathbb{C}[x]/(x - \lambda_k)^{n_{k,i}}$ is the Jordan form. The structure theorem for $\mathbb{Z}$-modules (abelian groups) is the analogous result for the prime structure of integers — see [[Thm - Classification of Finitely Generated Abelian Groups]].

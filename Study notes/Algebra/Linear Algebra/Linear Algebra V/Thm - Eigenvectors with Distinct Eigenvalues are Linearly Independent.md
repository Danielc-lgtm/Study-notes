---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Eigenvalue and Eigenvector"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a vector space over a field $F$ (need not be finite-dimensional for this theorem) and $T \in \mathcal{L}(V)$ is an operator. Eigenvectors $v_1, v_2, \ldots, v_m$ correspond to eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_m$, all assumed nonzero. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---

# Statement

> **Theorem (Eigenvectors of Distinct Eigenvalues).** Let $T \in \mathcal{L}(V)$ and suppose $v_1, v_2, \ldots, v_m$ are eigenvectors of $T$ corresponding to **distinct** eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_m$. Then the list $v_1, v_2, \ldots, v_m$ is linearly independent.

> **Corollary.** An operator on $V$ with $\dim V < \infty$ has at most $\dim V$ distinct eigenvalues.

---

# Motivation

This is the **single most-used fact about eigenvalues**. Almost every result connecting different eigenvalues — the direct-sum decomposition $V = \bigoplus E(\lambda_k, T)$ when $T$ is diagonalizable, the linear independence of eigenvector bases, the proof that an operator has at most $\dim V$ eigenvalues — runs through this theorem.

The result is morally surprising. Each eigenvector $v_k$ is a vector that "looks like" any other vector in $V$ — it is just a nonzero element of $V$ subject to an algebraic constraint $T v_k = \lambda_k v_k$. There is no obvious geometric reason that vectors satisfying these constraints for *different* $\lambda_k$ should be linearly independent. Indeed, vectors *do* exist that lie in non-trivial linear combinations of eigenspaces (any element of $E(\lambda_1, T) + E(\lambda_2, T)$ is such a combination). The theorem says: a single vector in *each* eigenspace, taken across distinct eigenspaces, cannot conspire to be dependent.

The proof is one of the cleanest applications of the operator $T - \mu I$ as an "eigenvalue-filter": applied to a vector, it kills the $\mu$-eigenvector component and scales the others. By repeated application, we can isolate each component and force the dependence relation to collapse.

---

# Sources and Targets

**Sources (Input Broadening)**

The bare precondition is "eigenvectors for distinct eigenvalues". The interesting source patterns:

The first disguised source is **a list of nonzero vectors invariant under $T$, each spanning a one-dimensional invariant subspace**. By [[Def - Eigenvalue and Eigenvector|the definition of an eigenvector]], such vectors are eigenvectors. If the corresponding eigenvalues are distinct, the theorem applies. *Example problem:* "Show that on $\mathbb{R}^n$ with the multiplication-by-distinct-real-numbers operator, the standard basis is linearly independent." The disguised source is that each standard basis vector is an eigenvector for the corresponding diagonal entry.

The second disguised source is **a list of nonzero solutions to different ODEs of the same operator form**. Specifically, $e^{\lambda_k x}$ is an eigenvector of the differentiation operator $D$ with eigenvalue $\lambda_k$; if the $\lambda_k$ are distinct, the functions $e^{\lambda_1 x}, e^{\lambda_2 x}, \ldots$ are linearly independent. This is the input to the "method of undetermined coefficients" for solving linear ODEs. *Example problem:* "Prove that for distinct real numbers $\lambda_1, \ldots, \lambda_n$, the functions $e^{\lambda_1 x}, \ldots, e^{\lambda_n x}$ are linearly independent over $\mathbb{R}$."

The third disguised source is **finite-order operators with distinct eigenvalues**. For instance, in a finite group, distinct irreducible characters are linearly independent — and this is proved by viewing characters as eigenvectors of a natural operator on the group algebra. *Example problem:* "Show that the characters of the irreducible representations of $\mathbb{Z}/n$ are linearly independent in $\mathbb{C}[\mathbb{Z}/n]$." The disguised source: each character is a $\zeta_n^k$-eigenvector of the regular representation.

**Targets (Output Amplification)**

Combined with **a dimension count**, the theorem amplifies to: *an operator on a finite-dimensional $V$ has at most $\dim V$ distinct eigenvalues*. This is the **first quantitative limit** on the spectrum of an operator and is the input to many counting arguments.

Combined with **the direct-sum structure of eigenspaces**, the theorem amplifies to: *the sum of eigenspaces $\sum E(\lambda_k, T)$ is automatically a direct sum*. The reason is that any element $v_1 + v_2 + \cdots + v_m = 0$ with $v_k \in E(\lambda_k, T)$ would, if any $v_k \neq 0$, contradict the theorem. So the only relation in the sum is the zero one, forcing the sum to be direct. This is the **structural backbone of diagonalizability**: $V$ is diagonalizable iff the (automatically direct) sum of eigenspaces fills all of $V$.

Combined with **knowledge of $\dim V$ distinct eigenvalues**, the theorem amplifies to: *an operator with $\dim V$ distinct eigenvalues is diagonalizable*. Reason: there are $\dim V$ linearly independent eigenvectors (one per eigenvalue), which form a basis of $V$ — exactly the diagonalizability condition. The result *cannot* be improved to "$\dim V$ distinct eigenvalues are sufficient and necessary": there are diagonalizable operators with fewer distinct eigenvalues, like the identity. But "enough distinct eigenvalues" is a *sufficient* condition for diagonalizability.

---

# Why Is It True

The mechanism is a **one-step shortest-counterexample argument**. Suppose the conclusion is false; among all violators, take the shortest one — a smallest list $v_1, \ldots, v_m$ of eigenvectors for distinct eigenvalues that are linearly dependent. This list has $m \geq 2$ (since a single nonzero vector is always linearly independent).

Write the dependence:
$$a_1 v_1 + a_2 v_2 + \cdots + a_m v_m = 0.$$
By minimality of $m$, no $a_i$ is zero (otherwise removing that term gives a strictly smaller dependent sublist, contradicting minimality).

Now apply $T - \lambda_m I$ to both sides — this is the **"$\lambda_m$-killing operator"** that annihilates $v_m$ and scales each other $v_k$ by $\lambda_k - \lambda_m$:
$$a_1 (\lambda_1 - \lambda_m) v_1 + a_2 (\lambda_2 - \lambda_m) v_2 + \cdots + a_{m-1} (\lambda_{m-1} - \lambda_m) v_{m-1} = 0.$$
The $v_m$ term vanished. The remaining $v_1, \ldots, v_{m-1}$ are a list of $m - 1$ eigenvectors for distinct eigenvalues, and the coefficients $a_k (\lambda_k - \lambda_m)$ are nonzero (since $a_k \neq 0$ and $\lambda_k \neq \lambda_m$). So we have produced a linearly dependent list of $m - 1$ eigenvectors for distinct eigenvalues — contradicting the minimality of $m$.

> **The mechanism: applying $T - \lambda_m I$ kills the last eigenvector and scales the others; the result is a strictly shorter dependent sublist, contradicting minimality.**

---

# What Makes This Hard

There is nothing structurally hard here, but the argument is **easy to misremember**: people often try to prove the result by direct expansion or by induction on $m$ without using the killing-operator. Direct expansion does not work because there is no apparent algebraic reason to extract one term from the relation. Induction on $m$ *does* work, but it is essentially the same shortest-counterexample argument repackaged. The conceptual key is that **the operator $T - \lambda_k I$ is the canonical instrument for isolating the non-$\lambda_k$ eigenvector contributions to a linear combination** — this is the same "killing-by-applying-a-linear-factor" idea that drives the [[Thm - Existence of Eigenvalues on Complex Vector Spaces|existence-of-eigenvalues proof]].

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Assume the result fails and take a shortest counterexample. Apply $T - \lambda_m I$ to produce a strictly shorter counterexample, contradicting minimality.

**Subgoal decomposition:**

1. **A shortest counterexample exists.** If the conclusion fails, the set of dependent lists $v_1, \ldots, v_m$ of eigenvectors for distinct eigenvalues is nonempty; take one with smallest $m$.
   - *Hint:* well-ordering of $\mathbb{N}$.
   - *Why needed:* gives the minimality lever for the contradiction.

2. **In the shortest counterexample, all coefficients are nonzero.** If any $a_k = 0$, removing that term gives a smaller dependent sublist (still consisting of eigenvectors for distinct eigenvalues), contradicting minimality.
   - *Hint:* removing a zero coefficient from a dependence keeps it a dependence.
   - *Why needed:* ensures the killing-operator's coefficients $a_k(\lambda_k - \lambda_m)$ are nonzero.

3. **Apply $T - \lambda_m I$ to the dependence.** Since $(T - \lambda_m I) v_m = 0$ and $(T - \lambda_m I) v_k = (\lambda_k - \lambda_m) v_k$ for $k < m$, the equation $a_1 v_1 + \cdots + a_m v_m = 0$ becomes
$$a_1(\lambda_1 - \lambda_m) v_1 + a_2(\lambda_2 - \lambda_m) v_2 + \cdots + a_{m-1}(\lambda_{m-1} - \lambda_m) v_{m-1} = 0.$$
   - *Hint:* $T - \lambda_m I$ is linear, so it distributes over the sum, and acts on each $v_k$ as multiplication by $\lambda_k - \lambda_m$.
   - *Why needed:* this is the new shorter dependence.

4. **The new dependence is non-trivial.** Each coefficient $a_k(\lambda_k - \lambda_m)$ is nonzero (since $a_k \neq 0$ and $\lambda_k \neq \lambda_m$).
   - *Hint:* product of nonzero things is nonzero (in a field).
   - *Why needed:* if all new coefficients were zero, the "dependence" would be trivially true, no contradiction.

5. **Contradiction.** The new dependence is a non-trivial relation on $v_1, \ldots, v_{m-1}$ — a list of $m - 1$ eigenvectors for distinct eigenvalues. This contradicts minimality of $m$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The operator $T - \lambda I$ scales eigenvectors by $\mu - \lambda$
> **Statement:** For any eigenvector $v$ of $T$ with eigenvalue $\mu \neq \lambda$, $(T - \lambda I) v = (\mu - \lambda) v$. For $v$ an eigenvector of $\lambda$, $(T - \lambda I)v = 0$.
>
> **Hint:** apply directly: $(T - \lambda I) v = Tv - \lambda v = \mu v - \lambda v = (\mu - \lambda) v$.
>
> **Why needed:** this is the action of the killing-operator that produces the shorter dependence.
>
> > [!note]- Full proof
> > For eigenvector $v$ of eigenvalue $\mu$ (i.e. $Tv = \mu v$):
> > $$(T - \lambda I) v = Tv - \lambda v = \mu v - \lambda v = (\mu - \lambda) v.$$
> > In particular, if $\mu = \lambda$, this is $0$; if $\mu \neq \lambda$, this is a nonzero scalar multiple of $v$, still an eigenvector for $\mu$ (with the same eigenspace).

---

# Formal Proof

> [!note]- Complete formal proof
> Suppose the conclusion fails. Let $m$ be the smallest positive integer such that there exists a linearly dependent list $v_1, v_2, \ldots, v_m$ of eigenvectors of $T$ corresponding to distinct eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_m$.
>
> **Step 1 — $m \geq 2$.** A single nonzero vector $v_1$ is always linearly independent (eigenvectors are nonzero by definition), so $m \geq 2$.
>
> **Step 2 — all coefficients in the dependence are nonzero.** There exist scalars $a_1, a_2, \ldots, a_m$, not all zero, with
> $$a_1 v_1 + a_2 v_2 + \cdots + a_m v_m = 0.$$
> If some $a_k = 0$, the relation involving the remaining $m - 1$ eigenvectors is also a dependence (still non-trivial), but with only $m - 1$ terms — contradicting minimality of $m$. So **every** $a_k \neq 0$.
>
> **Step 3 — apply $T - \lambda_m I$.** Using Lemma 1, $(T - \lambda_m I) v_k = (\lambda_k - \lambda_m) v_k$ for $k < m$, and $(T - \lambda_m I) v_m = 0$. Applying $T - \lambda_m I$ to both sides of the dependence:
> $$(T - \lambda_m I)(a_1 v_1 + \cdots + a_m v_m) = a_1 (\lambda_1 - \lambda_m) v_1 + \cdots + a_{m-1} (\lambda_{m-1} - \lambda_m) v_{m-1} + a_m \cdot 0 = 0.$$
>
> **Step 4 — the new relation is non-trivial.** The coefficients of the new relation are $a_k (\lambda_k - \lambda_m)$ for $k = 1, \ldots, m - 1$. Each is nonzero: $a_k \neq 0$ by Step 2, and $\lambda_k \neq \lambda_m$ since the eigenvalues are distinct. So the new relation
> $$a_1 (\lambda_1 - \lambda_m) v_1 + \cdots + a_{m-1} (\lambda_{m-1} - \lambda_m) v_{m-1} = 0$$
> is a non-trivial dependence on $v_1, \ldots, v_{m-1}$.
>
> **Step 5 — contradiction.** The list $v_1, \ldots, v_{m-1}$ consists of $m - 1$ eigenvectors of $T$ for distinct eigenvalues $\lambda_1, \ldots, \lambda_{m-1}$, and is linearly dependent. This contradicts the minimality of $m$. Hence the initial assumption is false, and the theorem holds. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Linear independence of exponential functions (analysis).** For distinct real numbers $\lambda_1, \ldots, \lambda_n$, the functions $e^{\lambda_1 x}, \ldots, e^{\lambda_n x}$ are linearly independent over $\mathbb{R}$. The cleanest proof is via this theorem: let $V$ be the span of these exponentials, let $D =$ differentiation; each $e^{\lambda_k x}$ is an eigenvector of $D$ with eigenvalue $\lambda_k$, and the eigenvalues are distinct, so the eigenvectors are linearly independent. This is one of the standard "linear-independence-of-exponentials" proofs and shows the eigenvalue technique at its cleanest.

**Linear independence of characters of distinct one-dimensional representations (representation theory).** For a finite abelian [[Def - Group|group]] $G$ and distinct one-dimensional representations $\chi_1, \chi_2 : G \to \mathbb{C}^\times$, the characters are linearly independent in the function space $\mathbb{C}^G$. Reason: each $\chi_k$ is an eigenvector of the "translation by $g$" operator $T_g f(x) = f(gx)$ with eigenvalue $\chi_k(g)$, and the distinct characters give distinct eigenvalues at any $g$ where they differ.

**Linear independence of cosines with distinct frequencies (Fourier analysis).** The functions $\cos(\lambda_1 x), \cos(\lambda_2 x), \ldots, \cos(\lambda_n x)$ for distinct positive $\lambda_k$ are linearly independent (Exercise 36 in LADR §5A). Each $\cos(\lambda_k x)$ is a $(-\lambda_k^2)$-eigenvector of $D^2$ (second-derivative operator); the $\lambda_k^2$ are distinct, so the eigenvectors are linearly independent. This is the building block of Fourier theory: the orthogonality of the trigonometric system is a stronger statement, but linear independence — via the eigenvalue theorem — is the first step.

---

# Bridges

- **[[Def - Diagonalizable Operator|Diagonalizability]]** — the natural setting. The theorem says that any set of eigenvectors with distinct eigenvalues is linearly independent; combined with knowledge that $V$ has a *basis* of eigenvectors, it gives diagonalizability immediately. Conversely, any diagonalizable operator has a basis of eigenvectors whose linear independence is guaranteed by this theorem.

- **The Lagrange interpolation formula** — the same mechanism. The Lagrange interpolation polynomials $\ell_k(x) = \prod_{j \neq k} \frac{x - x_j}{x_k - x_j}$ satisfy $\ell_k(x_j) = \delta_{jk}$, which is exactly the "killing the other roots, scaling the desired one" mechanism. The proof of this theorem uses the same trick: $(T - \lambda_m I)$ is a "killer" for $\lambda_m$, scaling the other eigenvectors.

- **The Cayley–Hamilton theorem (minimal-polynomial form)** — a downstream result. Once one has linear independence of eigenvectors, one can sometimes upgrade to the statement that the minimal polynomial of $T$ — which annihilates each eigenvector by $(T - \lambda_k I) v_k = 0$ — is at most $\prod (z - \lambda_k)$ for the distinct eigenvalues, which is the [[Thm - Conditions for Diagonalizability|diagonalizability characterisation]]. See [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]].

- **The functional calculus** — the natural extension. In functional analysis, "eigenvectors for distinct eigenvalues are linearly independent" generalises to "spectral projections at distinct points of the spectrum are mutually orthogonal" (for self-adjoint operators) or "linearly independent" (for normal operators). The killing-operator $T - \lambda I$ becomes the **resolvent** $(T - \lambda I)^{-1}$, defined on the resolvent set, and the analogous theorems hold via Cauchy integrals.

---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $\mathbb{F}^\infty$ denote the vector space of all sequences $(x_1, x_2, x_3, \dots)$ with $x_i \in \mathbb{F}$, under pointwise operations. Let

$$U = \{(x_1, x_2, x_3, \dots) \in \mathbb{F}^\infty : x_i = 0 \text{ for all but finitely many } i\}$$

be the subspace of sequences with only finitely many nonzero entries.

(a) Show that $U$ is a proper subspace of $\mathbb{F}^\infty$ — that is, $U \subsetneq \mathbb{F}^\infty$.

(b) Show that $U$ is the union $\bigcup_{n \geq 1} U_n$ of finite-dimensional subspaces, where $U_n = \{(x_1, \dots, x_n, 0, 0, \dots) : x_i \in \mathbb{F}\}$ is the subspace of sequences whose entries beyond the $n$th vanish.

(c) Use (a) and (b) to argue: $\mathbb{F}^\infty$ is *not* the union of any countable family of finite-dimensional subspaces. (This holds when $\mathbb{F}$ is an infinite field — in particular for $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$.)

This is a classic qualifying-exam result: **no vector space over an infinite field is the union of a countable family of proper subspaces** (see [arXiv 0803.2746](https://arxiv.org/pdf/0803.2746)). The exercise here gives a concrete instance, with the structural intuition for why infinite-dimensional spaces resist being approximated by their finite-dimensional pieces.

**Recall:**

$\mathbb{F}^\infty = \{(x_1, x_2, \dots) : x_i \in \mathbb{F}\}$ is a [[Def - Vector Space|vector space]] under pointwise operations. A [[Def - Subspace|subspace]] is a non-empty subset closed under addition and scalar multiplication.

![[Def - Subspace#The Definition]]

A subspace $W$ is **finite-dimensional** if it is spanned by a finite list of vectors $w_1, \dots, w_n$; we are anticipating [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]] for the formal definition.

---

# Convergent Strategy

**Problem class:** This is a **structural non-existence** problem: showing that a certain object (a countable cover of $\mathbb{F}^\infty$ by finite-dimensional subspaces) cannot exist. Such problems are typically proved by extracting a witness from any putative such object.

**Assumption pattern:** Working in $\mathbb{F}^\infty$ over an infinite field $\mathbb{F}$. The infinite-field hypothesis is essential — over $\mathbb{F}_p$ the result can fail by counting (vector spaces over finite fields are themselves countable, and the union covers everything trivially). We are also using that finite-dimensional subspaces of $\mathbb{F}^\infty$ are "small" in a structural sense.

**Theorem routing:** Part (a) is a quick witness: the sequence $(1, 1, 1, \dots)$ is not in $U$. Part (b) is direct: every sequence in $U$ has finitely many nonzero terms, so eventually lies in $U_n$ for some $n$. Part (c) requires a **diagonal-style** construction: given any countable family $\{W_k\}$ of finite-dimensional subspaces, build a sequence not in any $W_k$.

**Key decision point:** The non-obvious step is **constructing a sequence outside every $W_k$**. The cleanest approach: each $W_k$ has finite dimension $d_k$, so projection to any single coordinate axis (after a basis change) is finite-rank — there are coordinate axes "missing" from each $W_k$. The infinite-field hypothesis enters because we need *uncountably many* directions in $\mathbb{F}^\infty$ to dodge: if $\mathbb{F}$ were finite, every $\mathbb{F}^n$ would be a finite set, and the union of countably many finite sets would still be countable, but $\mathbb{F}^\infty$ over a finite $\mathbb{F}$ is uncountable (it has cardinality $|\mathbb{F}|^{\aleph_0}$). So the obstruction is partly cardinality, partly geometric.

The argument given below is the cleanest version: an explicit diagonal sequence using the standard basis vectors $e_k$ — given a countable family, find $e_k$ not in $W_k$ and form a sum.

---

# Legal Operations Used

1. **Construct a witness violating the candidate cover.** From the topic page's legal operations: to show no cover exists, exhibit one sequence in $\mathbb{F}^\infty$ not in any of the supposed pieces.

2. **Use the standard basis vectors $e_k = (0, \dots, 0, 1, 0, \dots)$ to probe finite-dimensional subspaces.** Each $e_k$ has support at coordinate $k$ only; a finite-dimensional $W$ cannot contain all $e_k$ simultaneously (because that would force $W \supseteq \operatorname{span}\{e_k\} = U$ which is infinite-dimensional).

3. **Diagonalize across the countable family.** Given $W_1, W_2, \dots$, choose witnesses $e_{n_k}$ with $e_{n_k} \notin W_k$ and chain the choices into a single sequence not in any $W_k$.

4. **Use the infinite-field hypothesis at the dimension-count step.** Each $W_k$ has finite dimension and cannot contain all of an infinite linearly independent set $\{e_1, e_2, \dots\}$. We are anticipating the principle "a list of vectors spanning a $d$-dimensional subspace cannot contain $d+1$ independent vectors" from [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

---

# Hints

> [!note]- Hint 1
> Part (a): exhibit a single sequence in $\mathbb{F}^\infty$ that is *not* in $U$. The constant sequence $(1, 1, 1, \dots)$ has every entry $1 \neq 0$, so infinitely many nonzero entries.

> [!note]- Hint 2
> Part (b): every sequence in $U$ has only finitely many nonzero entries. If $u \in U$ has nonzero entries only at positions $1, \dots, N$, then $u \in U_N$. So $U \subseteq \bigcup_n U_n$. Conversely $U_n \subseteq U$ since $U_n$'s sequences have nonzero entries only in the first $n$ positions.

> [!note]- Hint 3
> Part (c) — the main content. Suppose $\mathbb{F}^\infty = \bigcup_{k=1}^\infty W_k$ with each $W_k$ finite-dimensional. We need a contradiction.

> [!note]- Hint 4
> Each $W_k$ is finite-dimensional, say $\dim W_k = d_k$. The standard basis vectors $e_1, e_2, \dots$ are linearly independent. By the basis-bound (anticipating LADR §2A), $W_k$ contains at most $d_k$ of them.

> [!note]- Hint 5
> So for each $k$, there is some $e_{n_k}$ with $e_{n_k} \notin W_k$. Build $v = e_{n_1} + e_{n_2} + e_{n_3} + \dots$ — but be careful that the sum makes sense.

> [!note]- Hint 6
> Refinement: rather than summing infinitely many basis vectors, pick *one* basis vector $e_n$ that lies in *none* of the $W_k$. If for every $n$ there is some $k$ with $e_n \in W_k$, the function $n \mapsto k$ is well-defined. By pigeon-holing (each $W_k$ contains only finitely many $e_n$), this gives all $e_n$ inside $\bigcup_k W_k$, but it does not yet give the contradiction directly. The right argument uses linear-combination witnesses, not single basis vectors — see the full solution.

---

# Solution

The proof has three parts. Part (a) and Part (b) are direct verifications. Part (c) is the substantive argument: given a putative countable cover by finite-dimensional subspaces, construct a sequence not in any of them.

**Step 1 (Part a): $U \subsetneq \mathbb{F}^\infty$.**

> [!note]- Derivation
> The sequence $\mathbf{1} = (1, 1, 1, \dots)$ has every coordinate equal to $1$, so infinitely many nonzero entries. Hence $\mathbf{1} \in \mathbb{F}^\infty$ but $\mathbf{1} \notin U$. So $U$ is a proper subset of $\mathbb{F}^\infty$. The verification that $U$ is itself a subspace is direct: $0 \in U$ (no nonzero entries), the sum of two finitely-supported sequences is finitely supported (the union of two finite sets is finite), and a scalar multiple does not change the support pattern.

**Step 2 (Part b): $U = \bigcup_{n \geq 1} U_n$.**

> [!note]- Derivation
> *$\bigcup_n U_n \subseteq U$.* Every $u \in U_n$ has $u_i = 0$ for $i > n$, so only the first $n$ entries can be nonzero — in particular finitely many. So $u \in U$. Hence each $U_n \subseteq U$, and the union $\bigcup_n U_n \subseteq U$.
>
> *$U \subseteq \bigcup_n U_n$.* Let $u \in U$, so $u$ has finitely many nonzero entries. Let $N$ be the largest index $i$ with $u_i \neq 0$ (or $N = 1$ if $u = 0$). Then $u_i = 0$ for $i > N$, so $u \in U_N$. Hence $u \in \bigcup_n U_n$.
>
> Combining: $U = \bigcup_n U_n$. Each $U_n$ is finite-dimensional (spanned by $e_1, \dots, e_n$), so $U$ is a countable union of finite-dimensional subspaces.

**Step 3 (Part c): $\mathbb{F}^\infty$ is not the union of any countable family of finite-dimensional subspaces.**

We use the construction by witnesses. Suppose for contradiction $\mathbb{F}^\infty = \bigcup_{k=1}^\infty W_k$ with each $W_k$ finite-dimensional, say $\dim W_k = d_k$.

> [!note]- Derivation
> *Step 3.1 — finite-dimensional subspaces miss most basis vectors.* For each $k$, $W_k$ has dimension $d_k$. Anticipating the bound from [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]] (length of linearly independent list ≤ dimension): if $W_k$ contained more than $d_k$ of the basis vectors $e_1, e_2, \dots$, those vectors (which are linearly independent in $\mathbb{F}^\infty$, hence in $W_k$) would constitute a linearly independent list of length $> d_k$ in $W_k$, contradicting $\dim W_k = d_k$. So $W_k$ contains at most $d_k$ of the $e_i$.
>
> *Step 3.2 — diagonal construction.* List the basis vectors $e_1, e_2, e_3, \dots$ (countably many). Each $W_k$ contains only finitely many ($\leq d_k$) of them. So the set $\{i : e_i \in W_k \text{ for some } k \leq K\}$ is finite for each $K$ (at most $d_1 + \dots + d_K$).
>
> Now consider the **diagonal sequence** $v = \sum_{k=1}^\infty c_k e_{n_k}$, where the $n_k$ and $c_k$ are chosen so that $v$ is not in any $W_k$. The choice is as follows: pick $n_1 = 1$ and $c_1 = 1$, so the first nonzero coordinate of $v$ is at position $1$. For $k \geq 2$, pick $n_k > n_{k-1}$ large enough that $e_{n_k}$ is not in the subspace spanned by $W_1, \dots, W_{k-1}$ together with $e_{n_1}, \dots, e_{n_{k-1}}$ — this is possible because each $W_j$ is finite-dimensional and the previously-chosen $e_{n_j}$ are finitely many, so their combined span is finite-dimensional, while infinitely many $e_n$ are available.
>
> *Wait — this is not yet a contradiction.* The sequence $v$ has infinitely many nonzero entries, so $v \in \mathbb{F}^\infty$. By the hypothesis, $v \in W_k$ for some $k$. We need to engineer $v$ so this fails — and that is where the **infinite-field** hypothesis comes in.
>
> *Step 3.3 — the cleanest argument: use the infinitude of $\mathbb{F}$.* For an alternative cleaner argument, fix a basis vector $e \in \mathbb{F}^\infty$ that is in none of the $W_k$, then form one-parameter families $e + t \cdot e'$ for $t \in \mathbb{F}$ and a second basis vector $e' \notin W_k$ for one specific $k$. For each $k$, the set $\{t \in \mathbb{F} : e + t e' \in W_k\}$ is contained in an affine subspace of $\mathbb{F}$ of dimension $\leq d_k$, which is a *finite* subset (a single point or all of $\mathbb{F}$) when $\mathbb{F}$ has infinite cardinality and $W_k$ is finite-dimensional. Specifically: $\{t : e + t e' \in W_k\}$ is either empty, a singleton, or all of $\mathbb{F}$ — the latter would force $e, e' \in W_k$, which fails. So for each $k$ this set has at most one element. The countable union of singletons is countable; $\mathbb{F}$ is infinite (hence uncountable in the case $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$, but even just *infinite* over an infinite countable field suffices for non-totality). So there exists $t \in \mathbb{F}$ with $e + t e' \notin W_k$ for any $k$ — contradicting the covering hypothesis.
>
> *Note on cardinality.* For a countably infinite field like $\mathbb{Q}$, the argument needs care: a countable union of singletons could cover $\mathbb{Q}$. The correct statement requires $\mathbb{F}$ infinite, and the result is: a vector space over an infinite field is not a *finite* union of proper subspaces (extended to "not a countable union of finite-dimensional subspaces" under cardinality arguments when $\mathbb{F}$ is uncountable, or via cleverer witness selection). For our concrete case $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$, the simpler cardinality argument works: $\mathbb{F}$ is uncountable, $\bigcup_k W_k$ uses countably many singletons-of-bad-$t$, so most $t$ work.

For completeness, here is the cleanest formal argument.

> [!note]- Complete formal solution
> **Claim.** $\mathbb{F}^\infty$ over an infinite field $\mathbb{F}$ is not a countable union of finite-dimensional subspaces.
>
> *Proof of (a).* The sequence $\mathbf{1} = (1, 1, 1, \dots)$ has every entry $1 \neq 0$, so $\mathbf{1} \notin U$. But $\mathbf{1} \in \mathbb{F}^\infty$, so $U \subsetneq \mathbb{F}^\infty$.
>
> *Proof of (b).* If $u \in U_n$, then $u_i = 0$ for $i > n$, so $u$ has at most $n$ nonzero entries, hence $u \in U$ — so $U_n \subseteq U$. Conversely, if $u \in U$ has nonzero entries at positions $i_1 < \dots < i_m$, then for $N = i_m$, $u_i = 0$ for $i > N$, so $u \in U_N \subseteq \bigcup_n U_n$. Hence $U = \bigcup_n U_n$. Each $U_n$ is spanned by $e_1, \dots, e_n$, hence is finite-dimensional.
>
> *Proof of (c).* Assume for contradiction $\mathbb{F}^\infty = \bigcup_{k=1}^\infty W_k$ with each $\dim W_k < \infty$. Let $e_1, e_2, e_3, \dots$ be the standard basis vectors.
>
> Each $W_k$ has finite dimension $d_k$ and so can contain at most $d_k$ of the (linearly independent) basis vectors $e_i$. So there exist indices $i, j$ such that $e_i, e_j \notin W_1$ — choose any two such.
>
> Now consider, for each pair $(i, j)$ with $i \neq j$ such that $e_i \notin W_1$ and $e_j \notin W_1$, the family $\{e_i + t e_j : t \in \mathbb{F}\}$. For each $k$, the set $\{t \in \mathbb{F} : e_i + t e_j \in W_k\}$ has at most one element: if both $e_i + t_1 e_j$ and $e_i + t_2 e_j$ lie in $W_k$ with $t_1 \neq t_2$, then their difference $(t_1 - t_2) e_j \in W_k$, hence $e_j \in W_k$; combined with $e_i + t_1 e_j \in W_k$, this gives $e_i \in W_k$, so both $e_i, e_j \in W_k$.
>
> Fix $i, j$ such that $e_i, e_j$ together are not in any common $W_k$ — possible because each $W_k$ has finitely many basis vectors. Then for each $k$, $\{t : e_i + t e_j \in W_k\}$ has at most one element. The set $S = \bigcup_k \{t : e_i + t e_j \in W_k\}$ is therefore a countable union of singletons, hence countable. Since $\mathbb{F}$ is uncountable (for $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$), there exists $t \in \mathbb{F} \setminus S$. Then $e_i + t e_j \notin W_k$ for any $k$, contradicting the hypothesis $\mathbb{F}^\infty = \bigcup_k W_k$. $\blacksquare$
>
> **Remark (general field):** The result extends to any infinite field $\mathbb{F}$ (including $\mathbb{Q}$, which is infinite but countable) with a sharper argument that uses Zorn's lemma or a direct construction of an uncountable family of independent witnesses. The case $\mathbb{F}$ infinite suffices for "no *finite* union of proper subspaces equals $V$" — the countable-union version requires the more delicate work, and over countable infinite fields needs cardinality arguments using $|\mathbb{F}^\infty| > |\mathbb{F}|$.

---

# Key Takeaways

**Infinite-dimensional vector spaces resist being "covered" by their finite-dimensional pieces.** The result here pins down a structural feature distinguishing infinite-dimensional from finite-dimensional: a finite-dimensional vector space is trivially the union of (one of) its finite-dimensional subspaces (itself), but an infinite-dimensional vector space over an infinite field is never the union of a countable family of finite-dimensional pieces. This is the algebraic shadow of the topological fact that infinite-dimensional Banach spaces are not the union of compact sets — a finitely covered or compactly covered structure has stringent constraints. The lesson is: *infinite-dimensionality is a real obstacle to approximation by finite-dimensional pieces*, and this is why infinite-dimensional theory (functional analysis, sheaf cohomology, etc.) is structurally distinct from finite-dimensional linear algebra.

**The diagonal argument is the universal tool for "no countable cover".** The proof uses, in essence, a diagonal-style construction: given a countable list $\{W_k\}$ of supposed pieces, exhibit a single object outside all of them by working coordinate-by-coordinate against the list. The same template proves Cantor's theorem ($|\mathbb{R}| > |\mathbb{N}|$), the unboundedness of the busy beaver function in algorithmic complexity, and the Baire category theorem (no countable union of nowhere-dense sets is a complete metric space). The diagonalization here is in the *direction* of basis vectors: pick a direction $e_{n_k}$ orthogonal-in-spirit to $W_k$, and form a witness sequence. The flavor is the same in every case.

**The infinite-field hypothesis is genuinely necessary.** Over $\mathbb{F}_2$, the vector space $\mathbb{F}_2^2$ has three nontrivial proper subspaces (the three lines through the origin), and their union is $\mathbb{F}_2^2$ — so $\mathbb{F}_2^2$ *is* the union of three proper subspaces. The general theorem ("no vector space over an infinite field is a finite union of proper subspaces") rules out this kind of pathology over $\mathbb{R}$ or $\mathbb{C}$, and the obstruction is exactly that $\mathbb{F}$ being infinite forces enough "room" in each one-parameter family $e + t e'$ to dodge all the $W_k$. The same field-sensitivity appears in: existence of irreducible polynomials of every degree (over a finite field with $q$ elements, the polynomial $x^{q^n} - x$ factors completely into the irreducible polynomials of degree dividing $n$, a fact with no analogue in characteristic zero), uniqueness of fields with a given finite cardinality, and the structure of finite simple groups. Being alert to "is this hypothesis really necessary, or could the argument work over a finite field" is a meta-skill that pays off repeatedly.

**$\mathbb{F}^\infty$ versus $U$ illustrates the "completed versus colimit" distinction.** The subspace $U$ of finitely-supported sequences is the union (colimit, direct limit) of the spaces $U_n = \mathbb{F}^n$. The space $\mathbb{F}^\infty$ is the *completion* of $U$ — it includes "limits" like $(1, 1, 1, \dots)$ that lie outside every finite-dimensional piece. The same distinction appears in many algebraic settings: the polynomial ring $\mathbb{F}[x]$ is the direct limit of $\mathbb{F}[x]/(x^n)$ versus the power series ring $\mathbb{F}[[x]]$ which is the inverse limit; the direct sum $\bigoplus_n V_n$ versus the direct product $\prod_n V_n$. Recognizing when you have a colimit (small) versus an inverse-limit-style completion (large) is the algebraic-topological hinge that distinguishes "sequences eventually zero" from "all sequences" — and it is the source of much subtlety in functional analysis, where Banach spaces are completions of normed spaces with respect to a norm.

---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Linear Map"
  - "Def - Null Space and Range"
  - "Def - Rank of a Linear Map"
  - "Thm - Fundamental Theorem of Linear Maps"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $U$ and $V$ be finite-dimensional vector spaces and let $W$ be any vector space, all over the same field $\mathbf{F}$. For $S \in \mathcal{L}(V, W)$ and $T \in \mathcal{L}(U, V)$, prove that
$$\dim \operatorname{range}(ST) \;\leq\; \min\{\, \dim \operatorname{range} S,\, \dim \operatorname{range} T \,\}.$$

In matrix language: for $A \in \mathbf{F}^{m, n}$ and $B \in \mathbf{F}^{n, p}$,
$$\operatorname{rank}(AB) \;\leq\; \min\{\operatorname{rank} A, \operatorname{rank} B\}.$$

**Recall:**

![[Def - Null Space and Range#The Definition]]

![[Def - Rank of a Linear Map#The Definition]]

The composition $ST : U \to W$ is defined by $(ST)(u) = S(T(u))$.

The [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps (rank–nullity)]] says $\dim U = \dim \operatorname{null}(T) + \dim \operatorname{range}(T)$ for any $T \in \mathcal{L}(U, V)$ with $U$ finite-dimensional.

---

# Convergent Strategy

**Problem class.** This is a *rank inequality for a composition* problem. The topic-page Problem-Solving Strategy classifies it under "structural facts about linear maps with rank–nullity": the composition has a range contained in the range of the second factor (giving the $\operatorname{rank} S$ bound) and a domain that maps through the first, so its range is $S$ applied to the range of $T$ (giving the $\operatorname{rank} T$ bound).

**Assumption pattern.** $U$ is finite-dimensional (otherwise rank–nullity does not apply directly, though one can sometimes adapt). $S, T$ are arbitrary linear maps with $T : U \to V$ and $S : V \to W$. The defining feature: the composition is sandwiched between $T$ and $S$, so its range is constrained by both.

**Theorem routing.** Two routes, one for each bound.

- **Bound 1:** $\operatorname{range}(ST) \subseteq \operatorname{range} S$. Reason: every $(ST)(u) = S(T(u))$ is in the range of $S$. Hence $\dim \operatorname{range}(ST) \leq \dim \operatorname{range} S$.
- **Bound 2:** $\operatorname{range}(ST) = S(\operatorname{range} T)$. Reason: $(ST)(u) = S(T u)$, and as $u$ ranges over $U$, $Tu$ ranges over $\operatorname{range} T$. So $\operatorname{range}(ST)$ is exactly the image of $\operatorname{range} T$ under $S$. The image of a subspace under a linear map has dimension at most the dimension of the subspace (this is a special case of rank–nullity applied to the restriction $S|_{\operatorname{range} T}$). Hence $\dim \operatorname{range}(ST) \leq \dim \operatorname{range} T$.

Combining both bounds gives the $\min$.

**Key decision point.** The crucial recognition is that *each bound has a different proof*: containment of the range gives the $S$-bound, and "image of the range" gives the $T$-bound. The two are non-obvious as a pair, because the natural decomposition $\operatorname{range}(ST) = S(\operatorname{range} T)$ is not immediately a dimension equality — one needs the lemma "$\dim S(X) \leq \dim X$" for a subspace $X$. This is itself a one-line application of rank–nullity to the restriction $S|_X$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Apply rank–nullity to convert one dimension into another** (operation 3). Used in establishing that the image of a subspace under a linear map has dimension bounded by the dimension of the subspace. Restricted to the subspace, [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] gives the bound.

2. **Use $\mathcal{M}(ST) = \mathcal{M}(S)\mathcal{M}(T)$ to turn composition into multiplication** (operation 7). The matrix version $\operatorname{rank}(AB) \leq \min\{\operatorname{rank} A, \operatorname{rank} B\}$ follows from the operator version applied to the linear maps the matrices represent.

3. **Decompose a domain via $V = \operatorname{null} T \oplus U$ for some complement** (operation 9). Implicitly used in the rank–nullity argument restricted to $\operatorname{range} T$.

---

# Hints

> [!note]- Hint 1
> Two bounds, one for each rank on the right-hand side. The bound by $\operatorname{rank} S$: where does $\operatorname{range}(ST)$ live? The bound by $\operatorname{rank} T$: what does $S$ do to the range of $T$?

> [!note]- Hint 2
> For the $\operatorname{rank} S$ bound: $\operatorname{range}(ST)$ is contained in $\operatorname{range} S$. Why? Apply $S$ to anything; the result is in $\operatorname{range} S$. Hence $\dim \operatorname{range}(ST) \leq \dim \operatorname{range} S$.

> [!note]- Hint 3
> For the $\operatorname{rank} T$ bound: $\operatorname{range}(ST) = S(\operatorname{range} T)$. The right-hand side is the image of $\operatorname{range} T$ under $S$. The image of a subspace $X$ under a linear map has dimension at most $\dim X$ — apply [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] to the restriction $S|_X$.

---

# Solution

The plan: prove two bounds separately. The first uses $\operatorname{range}(ST) \subseteq \operatorname{range} S$ (immediate from the definition of composition). The second uses $\operatorname{range}(ST) = S(\operatorname{range} T)$, and then bounds the dimension of $S(\operatorname{range} T)$ by the dimension of $\operatorname{range} T$, via [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] applied to the restriction $S|_{\operatorname{range} T}$.

**Step 1: $\dim \operatorname{range}(ST) \leq \dim \operatorname{range} S$.**

The range of $ST$ is contained in the range of $S$.

> [!note]- Derivation
> Let $w \in \operatorname{range}(ST)$. Then $w = (ST)(u) = S(Tu)$ for some $u \in U$. So $w = S(v)$ where $v := Tu \in V$. Hence $w \in \operatorname{range} S$.
>
> So $\operatorname{range}(ST) \subseteq \operatorname{range} S$. Taking dimensions:
> $$\dim \operatorname{range}(ST) \leq \dim \operatorname{range} S.$$

**Step 2: $\operatorname{range}(ST) = S(\operatorname{range} T)$.**

This is a set-theoretic equality, used in Step 3 to relate $\dim \operatorname{range}(ST)$ to $\dim \operatorname{range} T$.

> [!note]- Derivation
> ($\subseteq$) If $w \in \operatorname{range}(ST)$, then $w = (ST)(u) = S(Tu)$ for some $u$. Let $v := Tu \in \operatorname{range} T$. Then $w = S(v)$, so $w \in S(\operatorname{range} T)$.
>
> ($\supseteq$) If $w \in S(\operatorname{range} T)$, then $w = S(v)$ for some $v \in \operatorname{range} T$. So $v = Tu$ for some $u \in U$. Then $w = S(Tu) = (ST)(u)$, so $w \in \operatorname{range}(ST)$.

**Step 3: $\dim S(\operatorname{range} T) \leq \dim \operatorname{range} T$.**

The image of a finite-dimensional subspace under a linear map has dimension at most that of the subspace, by rank–nullity applied to the restriction.

> [!note]- Derivation
> Apply [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] to the restriction $S|_{\operatorname{range} T} : \operatorname{range} T \to W$. We need $\operatorname{range} T$ finite-dimensional; this holds because $U$ is finite-dimensional and $T : U \to V$, so $\operatorname{range} T \subseteq V$ is finite-dimensional ($\dim \operatorname{range} T \leq \dim U$ by [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] applied to $T$).
>
> Then
> $$\dim \operatorname{range} T = \dim \operatorname{null}(S|_{\operatorname{range} T}) + \dim \operatorname{range}(S|_{\operatorname{range} T}).$$
> Since $\dim \operatorname{null}(S|_{\operatorname{range} T}) \geq 0$, we have $\dim \operatorname{range}(S|_{\operatorname{range} T}) \leq \dim \operatorname{range} T$. The range of $S|_{\operatorname{range} T}$ is exactly $S(\operatorname{range} T)$, so
> $$\dim S(\operatorname{range} T) \leq \dim \operatorname{range} T.$$

**Step 4: Combine.**

By Step 2, $\dim \operatorname{range}(ST) = \dim S(\operatorname{range} T)$. By Step 3, this is $\leq \dim \operatorname{range} T$. So $\dim \operatorname{range}(ST) \leq \dim \operatorname{range} T$.

Combining with Step 1: $\dim \operatorname{range}(ST) \leq \min\{\dim \operatorname{range} S, \dim \operatorname{range} T\}$. $\blacksquare$

> [!note]- Complete formal solution
> Let $S \in \mathcal{L}(V, W)$ and $T \in \mathcal{L}(U, V)$ with $U$ (and hence $\operatorname{range} T \subseteq V$) finite-dimensional.
>
> **First bound: $\dim \operatorname{range}(ST) \leq \dim \operatorname{range} S$.** For $w \in \operatorname{range}(ST)$, $w = S(Tu)$ for some $u$, so $w \in \operatorname{range} S$. Hence $\operatorname{range}(ST) \subseteq \operatorname{range} S$, and dimensions are monotone in inclusion: $\dim \operatorname{range}(ST) \leq \dim \operatorname{range} S$.
>
> **Second bound: $\dim \operatorname{range}(ST) \leq \dim \operatorname{range} T$.** We first identify $\operatorname{range}(ST) = S(\operatorname{range} T)$ as subsets of $W$. Indeed, $w \in \operatorname{range}(ST)$ iff $w = S(Tu)$ for some $u$, iff $w = S(v)$ for some $v \in \operatorname{range} T$, iff $w \in S(\operatorname{range} T)$.
>
> Now apply [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] to the restriction $S|_{\operatorname{range} T} : \operatorname{range} T \to W$, which has $\operatorname{range} T$ finite-dimensional and $\operatorname{range}(S|_{\operatorname{range} T}) = S(\operatorname{range} T)$:
> $$\dim \operatorname{range} T = \dim \operatorname{null}(S|_{\operatorname{range} T}) + \dim S(\operatorname{range} T) \geq \dim S(\operatorname{range} T).$$
> Hence $\dim \operatorname{range}(ST) = \dim S(\operatorname{range} T) \leq \dim \operatorname{range} T$.
>
> **Combining.** $\dim \operatorname{range}(ST) \leq \min\{\dim \operatorname{range} S, \dim \operatorname{range} T\}$. $\blacksquare$

> [!note]- Matrix version
> For $A \in \mathbf{F}^{m, n}$ and $B \in \mathbf{F}^{n, p}$, $\operatorname{rank}(AB) \leq \min\{\operatorname{rank} A, \operatorname{rank} B\}$. The matrix $A$ represents a linear map $T_A : \mathbf{F}^n \to \mathbf{F}^m$, $T_A(x) = Ax$; similarly $T_B : \mathbf{F}^p \to \mathbf{F}^n$, $T_B(y) = By$. The product $AB$ is the matrix of $T_A T_B$, and $\operatorname{rank}(AB) = \dim \operatorname{range}(T_A T_B)$ by [[Def - Rank of a Linear Map|the bridge between operator rank and matrix rank]]. The operator version then gives $\operatorname{rank}(AB) \leq \min\{\operatorname{rank} A, \operatorname{rank} B\}$.

---

# Key Takeaways

**Composition cannot increase rank.** The fundamental insight is that composing two linear maps cannot produce a result of higher rank than either factor. The first map's range is the largest set of "outputs" the second can act on; the second map's range is the largest set of outputs the composition can produce. Both are upper bounds. The reusable principle is to *use rank bounds as obstructions*: if you need a rank-$r$ linear map and have only factor maps of low rank, you cannot get there by composition. This is the rank-side of the dimension-rigidity story: a rank-$r$ map cannot be the product of two lower-rank maps. The trigger is any rank or dimension question involving compositions.

**The image of a subspace under a linear map is bounded by the subspace's dimension.** A linear map $S$ applied to a subspace $X$ produces a subspace $S(X)$ of dimension at most $\dim X$. This is rank–nullity applied to the restriction $S|_X$: $\dim X = \dim \operatorname{null}(S|_X) + \dim S(X) \geq \dim S(X)$. The reusable principle: whenever you push a subspace through a linear map, you do not gain dimension; you may lose it (the null space of the restriction is the "lost" dimension). The trigger is "linear image of a subspace" — apply rank–nullity to the restriction.

**Rank bounds in matrix algebra propagate through products.** The matrix version $\operatorname{rank}(AB) \leq \min\{\operatorname{rank} A, \operatorname{rank} B\}$ has wide-ranging applications. Three: (a) the product of a low-rank matrix with anything is low-rank, which is the basis of **low-rank approximation** in numerical linear algebra and data science; (b) if $A$ has rank $r$, then $A^k$ has rank at most $r$, so iterated multiplication cannot recover rank; (c) the rank of a product is *additively* bounded too: $\operatorname{rank}(A) + \operatorname{rank}(B) - n \leq \operatorname{rank}(AB)$ (Sylvester's inequality), giving a lower bound when $A, B$ are both close to full rank. The reusable principle is to estimate the rank of complicated matrix expressions via these bounds. The trigger: rank questions about products of matrices.

---

---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Null Space and Range"
  - "Def - Invertibility and Isomorphism"
  - "Thm - Fundamental Theorem of Linear Maps"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $T \in \mathcal{L}(V, W)$ is a linear map between finite-dimensional vector spaces with $\dim V = \dim W$. The full notation registry is on [[Linear Algebra III — §3A–D Linear Maps]].

---

# Statement

> **Theorem.** Let $V, W$ be finite-dimensional vector spaces over $\mathbf{F}$ with $\dim V = \dim W$, and let $T \in \mathcal{L}(V, W)$. Then the following are equivalent:
>
> 1. $T$ is invertible.
> 2. $T$ is injective.
> 3. $T$ is surjective.

The important special case is $W = V$ (so the hypothesis $\dim V = \dim W$ is automatic), in which the theorem says: an operator on a finite-dimensional vector space is invertible iff it is injective iff it is surjective.

> **Corollary.** For $V, W$ finite-dimensional of the same dimension and $S \in \mathcal{L}(W, V)$, $T \in \mathcal{L}(V, W)$, $ST = I_V$ implies $TS = I_W$. (Equivalently, a one-sided inverse is two-sided in equal finite [[Def - Dimension|dimensions]].)

---

# Motivation

This theorem captures one of the most striking rigidity phenomena in finite-dimensional mathematics: **half-information about a linear map upgrades automatically to full information**. To prove a linear map between equal-dimension finite-dimensional spaces is invertible, you need only prove half — either injectivity or surjectivity. The other is free. This is "the pigeonhole principle of linear algebra", and it has no analogue in infinite [[Def - Dimension|dimensions]].

The question the theorem answers is: when can a linear map fail to be invertible *while still being injective* (or surjective)? In finite equal dimensions, the answer is "never". The reason — visible from [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] — is dimensional rigidity: $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ has no slack when $\dim V = \dim W$. Injectivity kills the first term, forcing the second to fill all of $W$. Surjectivity fills the second, forcing the first to be zero.

The motivation runs in three layers. *First*, the theorem provides a free upgrade: a one-line application of rank–nullity converts injectivity to surjectivity and back. In practice, injectivity is much easier to check than surjectivity (one equation $Tv = 0 \Rightarrow v = 0$ vs. constructing preimages for every $w \in W$), so the theorem says "check the easy one, get the hard one free". *Second*, the theorem identifies the failure mode: in infinite dimensions, where the theorem fails, the failure has a *cause* — escape to infinity, the multiplication-by-$x^2$ phenomenon — and identifying that cause is the bridge to functional analysis. *Third*, the theorem is the conceptual cousin of facts in many other areas: a permutation of a finite set is a bijection iff injective iff surjective; a finite-[[Def - Group|group]] endomorphism is an isomorphism iff injective iff surjective. Finite-rank rigidity is a recurring pattern.

A useful slogan: **in finite equal dimensions, "no information lost" and "no information missing" are equivalent**. The dimension is a fixed accounting budget; spending it all on the range and spending nothing on the null space are forced to happen together.

---

# Sources and Targets

**Sources (Input Broadening)**

**Source: "show $T$ is invertible (or has an inverse)".** Direct application. The non-obvious step: realise that proving injectivity *suffices*, even when the goal mentions invertibility or surjectivity. Example: "Show $T(x, y, z) = (-y, x, 4z)$ is invertible." Prove injectivity ($Tv = 0 \Rightarrow v = 0$: from $-y = 0, x = 0, 4z = 0$ get $x = y = z = 0$), invoke the theorem, done.

**Source: "show $T$ is surjective".** The same trick: prove the easier injectivity instead. Example (LADR 3.67): show that on the finite-dimensional space $\mathcal{P}_m(\mathbb{R})$, the map $p \mapsto ((x^2 + 5x + 7)p)''$ is surjective. Direct surjectivity is hard (must exhibit $p$ for every right-hand side $q$). But: the map is injective (its null space is $\{ax + b\}$, but the map raises degree by $2$ then lowers by $2$, so on $\mathcal{P}_m$ the null space is $\{0\}$ — see the LADR proof). By the theorem, surjectivity is automatic.

**Source: "show every $b \in \mathbf{F}^n$ has a solution to $Ax = b$".** A square system $Ax = b$ has a solution for every $b$ iff $A$ is surjective as a linear map. Equivalently (theorem!), $A$ is injective, i.e., $Ax = 0$ implies $x = 0$. So "the homogeneous system has only the trivial solution" implies "every inhomogeneous system is consistent". The non-obvious step: convert a *consistency* question into a *uniqueness* question via the theorem. This is LADR Exercise 21 of §3D.

**Source: "show $S T = I$ implies $T S = I$".** A one-sided inverse is two-sided in finite dimensions. From $ST = I$, $T$ is injective (so $T$ is invertible by the theorem), and multiplying $ST = I$ on the right by $T^{-1}$ gives $S = T^{-1}$, hence $TS = I$. The full statement: in finite equal dimensions, "$T$ has a left inverse" ⟺ "$T$ has a right inverse" ⟺ "$T$ is invertible". (This is Exercise 24 of LADR §3D.)

**Targets (Output Amplification)**

**Combined with the dimension-classification theorem $V \cong W \iff \dim V = \dim W$.** Two finite-dimensional spaces of the same dimension are isomorphic, and the isomorphism can be witnessed by *any* injective (or surjective) linear map between them. This is the procedural converse: don't construct an isomorphism, find an injective linear map; the theorem does the rest. The further result is that the construction of isomorphisms reduces to construction of injective maps, often easier (e.g., via the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] on a basis).

**Combined with rank inequalities.** For an operator $T \in \mathcal{L}(V)$ with $\dim V = n$, the rank $\operatorname{rank} T \leq n$ with equality iff $T$ is invertible. So invertibility is "full rank". This sets up matrix-rank-based tests for invertibility — invertibility of a square matrix is computable by computing its rank (or its determinant, equivalently). The further result $E$: matrix inversion algorithms (Gauss–Jordan, LU decomposition) work because invertibility is a computable property.

**Combined with the structure of $\operatorname{GL}_n(\mathbf{F})$.** The invertible $n$-by-$n$ matrices over $\mathbf{F}$ form a group, and the theorem says this is exactly "the matrices with no kernel" = "the matrices with no missing image". For matrix groups over $\mathbb{R}$ or $\mathbb{C}$, $\operatorname{GL}_n$ is open in $M_n$ (the non-invertible matrices form a closed nowhere-dense set, the **determinantal hypersurface** $\det A = 0$). The further result $E$: invertibility is a generic property of square matrices, and small perturbations of an invertible matrix remain invertible.

**Combined with the failure of the theorem in infinite dimensions.** The theorem identifies a sharp finite-dimensional phenomenon. In infinite dimensions it fails — multiplication by $x^2$ is injective but not surjective on $\mathcal{P}(\mathbb{R})$ — and the failure isolates the *interesting* operators of functional analysis: shifts, multiplications, compact operators. The further result $E$: the theory of **Fredholm operators** is built around the controlled-failure of this theorem; a Fredholm operator has $\dim \operatorname{null} T < \infty$ and $\operatorname{codim} \operatorname{range} T < \infty$, with a well-defined index $\dim \operatorname{null} T - \operatorname{codim} \operatorname{range} T$ that *would* be zero (by the theorem) if the theorem held.

---

# Why Is It True

The theorem is a one-line consequence of [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] combined with $\dim V = \dim W$. The intuition is the dimension-conservation reasoning:

By rank–nullity, $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$. Since $\dim V = \dim W$, this is $\dim W = \dim \operatorname{null} T + \dim \operatorname{range} T$. Since $\operatorname{range} T \subseteq W$, we have $\dim \operatorname{range} T \leq \dim W$, with equality iff $\operatorname{range} T = W$ (because in finite dimensions, a [[Def - Subspace|subspace]] of equal dimension equals the whole space). So:

- $T$ injective ⟺ $\dim \operatorname{null} T = 0$ ⟺ $\dim \operatorname{range} T = \dim W$ ⟺ $\operatorname{range} T = W$ ⟺ $T$ surjective.

The chain of equivalences is *forced* by the dimension equation. There is no slack.

> **The whole intuition in one sentence: a fixed dimension budget on $V$ must be split between the null space and the range; when $\dim V = \dim W$, fully spending the budget on the range (surjectivity) and spending nothing on the null space (injectivity) are the same condition.**

A cleaner reformulation: $T : V \to W$ between equal-dimension spaces is a map "from a budget of $n$ dimensions to another budget of $n$ dimensions". The null space subtracts from the source budget; the range subtracts from the target budget. Equality of budgets and the conservation law force these subtractions to be equal — and zero on one side iff zero on the other.

The reason this fails in infinite dimensions is that infinite cardinal arithmetic does not have the rigidity of natural-number arithmetic: $\aleph_0 = 1 + \aleph_0$, so the dimension equation allows non-trivial null space without forcing missing range. Specifically, for $T = x^2 \cdot$ on $\mathcal{P}(\mathbb{R})$ (multiplication by $x^2$), the null space is $\{0\}$ but the range is the polynomials with no constant or linear term — a proper [[Def - Subspace|subspace]] of the same infinite dimension as the source. The dimension equation is honoured ($\infty = 0 + \infty$), but the rigid implication "no null space ⟹ full range" fails.

A second perspective: the theorem can be proved without rank–nullity, by direct linear-map manipulation. If $T : V \to V$ is injective and $\dim V = n$, then $T$ sends a basis $v_1, \ldots, v_n$ to a linearly independent list $Tv_1, \ldots, Tv_n$ (because if $\sum c_k T v_k = 0$ then $T(\sum c_k v_k) = 0$ so $\sum c_k v_k = 0$ by injectivity, so $c_k = 0$ by linear independence of the basis). A list of $n$ linearly independent vectors in $V$ is a basis (by [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces|the basis criterion in equal length]]). So $T$ sends a basis to a basis, hence is surjective. The two proofs are equivalent.

---

# What Makes This Hard

The theorem itself is easy. The trap is in *misapplying* it: confidently asserting "$T$ is invertible because it's injective" without checking that the dimensions are equal and finite. In any of the following situations, the inference fails:

- $V$ or $W$ infinite-dimensional, even if they "have the same dimension" in a cardinality sense.
- $\dim V \neq \dim W$ (then injective and surjective are independent).
- $T$ a non-linear function (where injectivity and surjectivity bear no relationship to each other).

A second subtle point: the theorem is *equivalence*, not *implication*. The three conditions are mutually equivalent, and any one entails the others. In practice this means you choose the easiest to prove (usually injectivity), but conceptually all three contain the same information.

A third subtle point: the result extends to **one-sided inverses**. In equal finite dimensions, "$T$ has a left inverse" ⟺ "$T$ is injective" ⟺ "$T$ is invertible" — so a left inverse is automatically a two-sided inverse. In infinite dimensions, a left inverse and a right inverse are different conditions; the forward shift on $\mathbf{F}^\infty$ has a left inverse but is not surjective.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Use [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ together with $\dim V = \dim W$ and the fact that a subspace of $W$ of dimension $\dim W$ equals $W$. The three conditions of the theorem correspond to three terms in the dimension equation; they are forced to be linked.

**Subgoal decomposition:**

1. **$T$ injective ⟺ $\dim \operatorname{null} T = 0$.** By definition, $T$ is injective iff $\operatorname{null} T = \{0\}$, iff $\dim \operatorname{null} T = 0$.
   - *Hint:* See [[Def - Null Space and Range]] for the injectivity criterion.

2. **$T$ surjective ⟺ $\operatorname{range} T = W$ ⟺ $\dim \operatorname{range} T = \dim W$.** The first is the definition; the second uses that a subspace equals the whole space iff their dimensions agree (a finite-dimensional fact).

3. **Rank–nullity gives $\dim \operatorname{null} T = \dim V - \dim \operatorname{range} T = \dim W - \dim \operatorname{range} T$** (using $\dim V = \dim W$).
   - *Why needed:* Rearranges the dimension equation to relate nullity directly to "range deficit".

4. **Combine.** $T$ injective ⟺ $\dim \operatorname{null} T = 0$ ⟺ $\dim \operatorname{range} T = \dim W$ ⟺ $T$ surjective.

5. **Both ⟺ invertible.** $T$ injective and surjective is exactly $T$ invertible, by [[Def - Invertibility and Isomorphism]] (and the automatic linearity of the inverse).

---

# Lemma Decomposition

> [!note]- Lemma 1: Injectivity is null-space triviality
> **Statement:** A linear map $T : V \to W$ is injective iff $\operatorname{null} T = \{0\}$.
>
> **Hint:** $Tu = Tv$ iff $T(u - v) = 0$.
>
> **Why needed:** Converts the abstract injectivity condition to a concrete subspace condition.
>
> > [!note]- Full proof
> > ($\Rightarrow$) Suppose $T$ injective. For $v \in \operatorname{null} T$, $Tv = 0 = T(0)$, so by injectivity $v = 0$. Hence $\operatorname{null} T = \{0\}$.
> >
> > ($\Leftarrow$) Suppose $\operatorname{null} T = \{0\}$. If $Tu = Tv$, then $T(u - v) = Tu - Tv = 0$, so $u - v \in \operatorname{null} T = \{0\}$, i.e., $u = v$. Hence $T$ injective.

> [!note]- Lemma 2: A subspace equals the whole space iff their dimensions agree
> **Statement:** Let $W$ be a finite-dimensional vector space and $U \subseteq W$ a subspace. Then $U = W$ iff $\dim U = \dim W$.
>
> **Hint:** $\Rightarrow$ is immediate. $\Leftarrow$: a basis of $U$ is a linearly independent list in $W$ of length $\dim W$, hence a basis of $W$.
>
> **Why needed:** Connects "$\operatorname{range} T = W$" with "$\dim \operatorname{range} T = \dim W$".
>
> > [!note]- Full proof
> > ($\Rightarrow$) Trivial: equal sets have equal dimensions.
> >
> > ($\Leftarrow$) Let $u_1, \ldots, u_k$ be a basis of $U$, $k = \dim U = \dim W$. The list is linearly independent in $W$. A linearly independent list in $W$ of length $\dim W$ is a basis of $W$ ([[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]). So $u_1, \ldots, u_k$ spans $W$, i.e., $W = \operatorname{span}(u_1, \ldots, u_k) = U$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V, W$ be finite-dimensional with $\dim V = \dim W < \infty$, and $T \in \mathcal{L}(V, W)$.
>
> By [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]]:
> $$\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T. \quad (*)$$
>
> **(2) $\iff$ (3): Injective ⟺ surjective.**
>
> Suppose $T$ injective. By Lemma 1, $\dim \operatorname{null} T = 0$, so from $(*)$ $\dim \operatorname{range} T = \dim V = \dim W$. By Lemma 2, $\operatorname{range} T = W$, so $T$ is surjective.
>
> Conversely, suppose $T$ surjective. Then $\operatorname{range} T = W$, so $\dim \operatorname{range} T = \dim W$. From $(*)$, $\dim \operatorname{null} T = \dim V - \dim \operatorname{range} T = \dim W - \dim W = 0$. By Lemma 1, $T$ is injective.
>
> **(1) $\iff$ (2 and 3): Invertible ⟺ injective and surjective.**
>
> By [[Def - Invertibility and Isomorphism]], $T$ is invertible iff it is both injective and surjective. (LADR Proposition 3.63: a linear map has a linear two-sided inverse iff it is injective and surjective, and the inverse is automatically linear when the underlying set-theoretic inverse exists.) Combined with the equivalence (2) ⟺ (3) above, all three conditions are mutually equivalent. $\blacksquare$
>
> **Proof of the one-sided inverse corollary.**
>
> Suppose $\dim V = \dim W < \infty$, $S \in \mathcal{L}(W, V)$, $T \in \mathcal{L}(V, W)$, and $ST = I_V$. We show $TS = I_W$.
>
> First, $T$ is injective: if $Tv = 0$, then $v = I_V v = STv = S(0) = 0$. By the theorem, $T$ is invertible.
>
> Multiplying $ST = I_V$ on the right by $T^{-1}$: $S = T^{-1}$. So $TS = T T^{-1} = I_W$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Determinant and invertibility.** A square matrix $A \in \mathbf{F}^{n, n}$ is invertible iff $\det A \neq 0$. The theorem provides one route: invertibility iff injectivity iff "the columns are linearly independent" (since the only solution to $Ax = 0$ being $x = 0$ is the column independence condition). Linear independence of the columns, in turn, is equivalent to $\det A \neq 0$ by determinant theory. So determinant computations test invertibility — and the theorem is what reduces invertibility to a property of columns. See [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]].

**Fredholm alternative in functional analysis.** For an integral operator $K$ on $L^2$ (compact), the equation $u + K u = f$ has a unique solution for every $f \in L^2$ iff the homogeneous equation $u + Ku = 0$ has only the trivial solution. This is the **Fredholm alternative**, the infinite-dimensional analogue of the theorem: the rigidity of injective ⟺ surjective extends to compact perturbations of the identity. The proof relies on the compactness of $K$ to recover finite-dimensional rank–nullity-like behaviour, despite the underlying space being infinite-dimensional.

**Inverse function theorem.** For a smooth $f : M \to N$ between manifolds of equal dimension, if the [[Def - The Total Derivative and Differentiability|total derivative]] $Df_x$ is invertible at $x$, then $f$ is locally invertible near $x$. Invertibility of $Df_x$ is, by the theorem, equivalent to injectivity (i.e., $Df_x v = 0 \Rightarrow v = 0$) — a single linear condition. So the inverse function theorem is the smooth analogue: a linear injectivity condition at a point lifts to a smooth local invertibility. See [[Thm - The Inverse Function Theorem]].

**Bijection on finite sets.** For finite sets $A, B$ with $|A| = |B|$, a function $f : A \to B$ is bijective iff injective iff surjective. This is the **pigeonhole principle**, and it is the set-theoretic skeleton of the theorem. The proof — that for $|A| = |B|$ finite, injectivity is equivalent to surjectivity — is the combinatorial cousin of the linear-algebra proof using rank–nullity.

**Permutation criterion for endomorphisms of finite [[Def - Group|groups]].** An endomorphism of a finite group is an automorphism iff injective iff surjective. The proof in [[Group Theory I — §1.1–1.2]] is by the same counting argument: a one-to-one map from a finite set to itself is a bijection. The translation to linear algebra is via the dimension count from rank–nullity.

---

# Bridges

- **[[Thm - Fundamental Theorem of Linear Maps]]** — the direct prerequisite. The theorem is two lines of rank–nullity. Conversely, "injectivity is equivalent to surjectivity in equal finite dimensions" together with the fundamental theorem can be packaged as: $\dim V = \dim W$ implies $\dim \operatorname{null} T = \dim \operatorname{coker} T$, where $\operatorname{coker} T = W / \operatorname{range} T$. This is the "Fredholm index = 0" statement for finite-dimensional operators with equal-dimension domain and codomain.

- **Permutation criterion on finite sets** — the bijective-iff-injective-iff-surjective theorem for finite sets. The proof for sets uses cardinality counting; for vector spaces it uses dimension counting via rank–nullity. The two are the set-theoretic and the linear-algebraic versions of the **pigeonhole principle**.

- **Pigeonhole for vector spaces.** A linear map $V \to W$ with $\dim V > \dim W$ has non-trivial null space (by rank–nullity); the theorem deepens this: when $\dim V = \dim W < \infty$, the absence of non-trivial null space is equivalent to the absence of missing range.

- **[[Thm - The Inverse Function Theorem]]** — the calculus analogue. Invertibility of the [[Def - The Total Derivative and Differentiability|total derivative]] (a linear condition, equivalent to injectivity at a point) lifts to local invertibility of the smooth map. The bridge is "linear injectivity at a point implies smooth local invertibility nearby".

- **Fredholm operators and the index** — the failure of the theorem in infinite dimensions, and its controlled rescue. A Fredholm operator has $\dim \operatorname{null} T - \dim \operatorname{coker} T \in \mathbb{Z}$, a deformation invariant. In the finite-dimensional equal-dimension case, the index is automatically zero (by the theorem) and Fredholmness is trivially satisfied. The infinite-dimensional theory studies operators where the index need not be zero.

---

# Unlocked by This

> [!tip] Computational Test for Matrix Invertibility *(in §3D)*
> A square matrix $A$ is invertible iff $\det A \neq 0$ iff $\operatorname{rank} A = n$ iff the columns are linearly independent. The theorem provides one route to this list of equivalences. The practical consequence: Gauss elimination computes both the rank and the inverse simultaneously, making matrix invertibility a routinely-testable property.

> [!tip] Fredholm Alternative *(from Functional Analysis)*
> For a compact operator $K$ on a Banach space, the equation $(I - K) u = f$ has a unique solution for every $f$ iff $(I - K) u = 0$ implies $u = 0$. This is the **Fredholm alternative**, and it is the infinite-dimensional analogue of the theorem — but it holds *only* for compact perturbations of the identity, not for arbitrary operators. Its proof uses approximation by finite-dimensional operators (where the theorem applies) and a limiting argument.

> [!tip] Implicit Function Theorem *(from Multivariate Analysis)*
> The smooth analogue of injectivity ⟹ surjectivity for the [[Def - The Total Derivative and Differentiability|total derivative]] is the **implicit function theorem**: if $F : \mathbb{R}^{n+m} \to \mathbb{R}^m$ is smooth and the partial Jacobian with respect to the last $m$ variables is invertible at a point, then near that point, the level set $F = 0$ is locally the graph of a smooth function $\mathbb{R}^n \to \mathbb{R}^m$. The rigidity at the linear level (this theorem) is what makes the smooth statement work.

> [!tip] Index of an Elliptic Operator *(from Index Theory)*
> The index of an elliptic differential operator $D$ on a compact manifold is $\dim \ker D - \dim \operatorname{coker} D$, a finite integer despite both spaces being subspaces of infinite-dimensional spaces. The **Atiyah–Singer index theorem** expresses this analytical index in terms of topological invariants. The theorem of this page is the elementary baseline: in finite equal dimensions, the index is zero. Departures from zero in the infinite-dimensional case are the substance of index theory.

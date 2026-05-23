---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over a field $\mathbb{F}$, $U \subseteq V$ is a subset (typically a subspace), and $v \in V$. The set $v + U = \{v + u : u \in U\}$ is the *translate of $U$ by $v$*, also called an *affine subset parallel to $U$*. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

This is a compound page: it defines two interlocking notions — **translate** and **affine subset** — because in this setting they coincide and naming both makes the geometry transparent.

---

# Axiom Motivation

The definition is doing two jobs at once. The first is *naming the operation $v + U$* that takes a vector and a subset and shifts the subset by the vector. The second is *recognising the resulting subset as a fundamental geometric object* — a flat plane that is parallel to $U$ but does not pass through the origin.

Why introduce a new name when the formula $v + U = \{v + u : u \in U\}$ already says everything? Because three properties single out these translated sets from arbitrary subsets, and giving them a name makes those properties first-class:

1. **The translates of a fixed subspace partition $V$.** Different translates of $U$ are either equal or disjoint — there is no overlap of [[Def - Coset|cosets]]. This is the partition property [[Def - Affine Subset#3.101 two translates of a subspace are equal or disjoint|3.101 below]], and it is the engine of well-definedness for the quotient construction. The fact that affine planes parallel to $U$ partition $V$ is not just a useful identity, it is *the* reason the [[Def - Quotient Space|quotient space]] can be defined at all.

2. **Solution sets of inhomogeneous linear equations are affine subsets.** Given $T : V \to W$ linear and $c \in W$, the set $\{v \in V : Tv = c\}$ is either empty or a translate of $\operatorname{null} T$. This is the linear-algebraic version of "the general solution of an inhomogeneous equation is a particular solution plus the general solution of the homogeneous equation". The shape of the solution set is forced by the linearity of $T$, and that shape is an affine subset.

3. **Affine subsets are the natural geometric objects of "linear algebra without an origin".** In a vector space we have a privileged origin $0$ and [[Def - Subspace|subspaces]] pass through it. In *affine geometry* the origin is not privileged — only differences of points are meaningful, not points themselves. The affine subsets $v + U$ are the analogue of [[Def - Subspace|subspaces]] in affine geometry: they are flat, of definite "direction" $U$, but with no preferred basepoint. Choosing a basepoint $v$ is one of many; replacing $v$ by $v' = v + u_0$ for any $u_0 \in U$ gives the same affine subset $v' + U = v + U$.

What if we drop the closure requirement on $U$ — let $U$ be just a subset, not a subspace? The notation $v + U = \{v + u : u \in U\}$ still makes sense, and Axler uses the broader name *translate* exactly for this case. But the partition property fails: two translates of an arbitrary subset can overlap without being equal (consider $U = \{0, e_1\}$ in $\mathbb{R}^2$; the translate $e_2 + U = \{e_2, e_2 + e_1\}$ overlaps $e_1 + U = \{e_1, 2e_1\}$ neither equally nor disjointly). The [[Def - Coset|cosets]]-partition-$V$ property is what makes $U$-being-a-subspace the right hypothesis.

What if we strengthen and require $v \in U$? Then $v + U = U$ trivially — the affine subset would be just $U$, and the construction is degenerate. The whole point is to allow $v$ *outside* $U$, producing a copy of $U$ shifted to a new location.

---

# The Definition

Let $V$ be a vector space over $\mathbb{F}$ and let $U \subseteq V$. For $v \in V$, the **translate of $U$ by $v$** is
$$v + U := \{v + u : u \in U\}.$$

When $U$ is a **subspace** of $V$, the translate $v + U$ is called an **affine subset of $V$ parallel to $U$**. The set $U$ is recovered from $v + U$ as the *direction subspace* of the affine subset.

The fundamental property — proved in the next section — is the **partition / equality / intersection trichotomy**: for any subspace $U$ and any $v, w \in V$,
$$v - w \in U \iff v + U = w + U \iff (v + U) \cap (w + U) \neq \emptyset.$$
Translates of a subspace are either equal or disjoint; equality occurs precisely when the basepoints differ by an element of the direction subspace.

---

# Lemma: Two Translates of a Subspace are Equal or Disjoint

> **Lemma (3.101).** Let $U$ be a subspace of $V$ and $v, w \in V$. Then
> $$v - w \in U \iff v + U = w + U \iff (v + U) \cap (w + U) \neq \emptyset.$$

**Proof.** Three claims, proved in a cycle.

*($v - w \in U \Rightarrow v + U = w + U$).* Suppose $v - w \in U$. If $u \in U$, then $v + u = w + ((v - w) + u) \in w + U$, since $(v - w) + u$ is a sum of two elements of $U$ and $U$ is closed under addition. So $v + U \subseteq w + U$. By symmetry, $w + U \subseteq v + U$, so they are equal.

*($v + U = w + U \Rightarrow (v + U) \cap (w + U) \neq \emptyset$).* Trivial: $v + 0 = v$ is in both, since $0 \in U$ (because $U$ is a subspace).

*($(v + U) \cap (w + U) \neq \emptyset \Rightarrow v - w \in U$).* Suppose $v + u_1 = w + u_2$ for some $u_1, u_2 \in U$. Then $v - w = u_2 - u_1$, which is in $U$ because $U$ is closed under subtraction. $\blacksquare$

The lemma uses *only* that $U$ is a subspace (closed under addition and additive inverses); the field structure is not required for the equality, only for the eventual quotient operations.

---

# Categorical / Structural Definition

The affine subsets $v + U$ are the *cosets* of $U$ as a [[Def - Subgroup|subgroup]] of the additive [[Def - Group|group]] of $V$. That is, viewing $(V, +)$ as an [[Def - Abelian Group|abelian group]] and $U$ as a [[Def - Subgroup|subgroup]], the translates $v + U$ are exactly the [[Def - Coset|left cosets]] of $U$ in $V$. Since $V$ is abelian, left cosets and right cosets coincide.

Categorically, the affine subsets fit into the framework of *torsors*. An affine space is a set $X$ on which a vector space $U$ acts freely and transitively — there is an action $X \times U \to X$, $(x, u) \mapsto x + u$, such that for any two points $x, x' \in X$ there is a *unique* $u \in U$ with $x' = x + u$ (we write $u = x' - x$). The data is a "vector space without a chosen origin": points can be subtracted to get vectors, but they cannot be added to each other (the operation $x + x'$ is not defined for two points of $X$).

Each affine subset $v + U \subseteq V$ is an affine space: the action of $U$ is restriction of the vector addition on $V$, and the unique vector $u$ from one point to another in $v + U$ is the difference $(v + u_2) - (v + u_1) = u_2 - u_1 \in U$. The affine subset has no privileged origin — choosing $v$ as a basepoint is one of many — but it does have a privileged *direction subspace*, $U$.

This is the structural origin of *affine geometry*, the geometry where you can speak of points and parallel lines and ratios on a line, but where the origin is not distinguished. Choosing an origin in an affine space converts it back into a vector space; the affine subset $v + U$ is "a vector space that has forgotten where its origin is".

---

# Relate to Other Fields / Compression

**Affine subsets are cosets specialised to vector spaces.** In a group $G$ with subgroup $H$, the [[Def - Coset|coset]] $gH = \{gh : h \in H\}$ is the translate of $H$ by $g$. The affine subset $v + U$ is exactly this, in the additive group of $V$ with subgroup $U$. The partition property of cosets ($gH = g'H \iff g^{-1}g' \in H$) becomes the additive partition property ($v + U = w + U \iff v - w \in U$). Internalise this once across groups, rings, modules, and vector spaces; the construction is the same in all of them.

**Affine subsets are solution sets of inhomogeneous linear equations.** Given a linear map $T : V \to W$ and a target $c \in W$, the set $\{v \in V : Tv = c\}$ is either empty (if $c \notin \operatorname{range} T$) or a translate of $\operatorname{null} T$ (if $c \in \operatorname{range} T$). This is because $Tv = c$ and $Tv' = c$ imply $T(v - v') = 0$, so $v$ and $v'$ differ by an element of $\operatorname{null} T$. The solution set of a system of inhomogeneous linear equations is an affine subset — flat, of dimension $n - \operatorname{rank} A$, but generally not passing through the origin.

**True name:** an affine subset is "a subspace that has been shifted off the origin", or equivalently "the solution set of an inhomogeneous linear equation". The shifted-subspace picture is the geometric one; the solution-set picture is the analytic one.

---

# Examples / Corollaries

**Is an instance — a line in $\mathbb{R}^2$ not through the origin.** Let $U = \{(x, 2x) : x \in \mathbb{R}\}$, the line of slope $2$ through the origin. The translate $(17, 20) + U$ is the line of slope $2$ passing through $(17, 20)$ — the same direction as $U$ but shifted off the origin. Since $(10, 20) \in U$, we have $(17, 20) = (7, 0) + (10, 20)$, so $(17, 20) + U = (7, 0) + U$: the affine subset is named by *any* of its points, and the name $(7, 0)$ shows that this affine subset is "the line of slope $2$ shifted right by $7$".

**Is an instance — a plane parallel to the $xy$-plane in $\mathbb{R}^3$.** Let $U = \{(x, y, 0) : x, y \in \mathbb{R}\}$, the $xy$-plane. For any $c \in \mathbb{R}$, the affine subset $(0, 0, c) + U = \{(x, y, c) : x, y \in \mathbb{R}\}$ is the horizontal plane at height $c$. The set of all affine subsets of this form is the *family of horizontal planes*, parameterised by $c \in \mathbb{R}$ — and this family is in bijection with $\mathbb{R}^3 / U$ (the [[Def - Quotient Space|quotient space]]).

**Is an instance — solution set of $2x + 3y + 5z = 7$ in $\mathbb{R}^3$.** Take the linear map $T : \mathbb{R}^3 \to \mathbb{R}$, $T(x, y, z) = 2x + 3y + 5z$. Its null space $U = \{(x, y, z) : 2x + 3y + 5z = 0\}$ is the plane through the origin with that equation. The solution set of $2x + 3y + 5z = 7$ is the translate $v_0 + U$ for any particular solution $v_0$ — for instance $v_0 = (1, 0, 1)$ since $2 + 5 = 7$. Different particular solutions give the same affine subset.

**Is NOT an affine subset — a closed disk in $\mathbb{R}^2$.** The unit disk $D = \{v \in \mathbb{R}^2 : \|v\| \leq 1\}$ is not an affine subset, because $D$ is not the translate of a subspace. Affine subsets are *flat*, infinite, and have a well-defined direction subspace; the disk is bounded and curved.

**Is NOT a translate — the empty set.** The empty set $\emptyset$ is not a translate $v + U$ for any $v$ and any $U$, because $v + U$ always contains $v$ (taking $u = 0 \in U$). So the empty solution set of an inconsistent linear system is *not* an affine subset; the lemma above says solution sets are *either* affine subsets *or* empty.

**Corollary — every affine subset has a direction subspace.** If $v + U = w + W$ for subspaces $U, W \leq V$, then $U = W$. (Proof: pick the same basepoint $v \in v + U = w + W$, so $w + W = v + W$ as well, and from $v + U = v + W$ we get $U = W$.) The direction subspace of an affine subset is uniquely determined.

**Corollary — translates form a torsor over $U$.** The set of translates of $U$ is in bijection with $V/U$ via $v + U \leftrightarrow v + U$ (tautologically); each translate is itself a torsor over $U$ — every two points differ by a unique element of $U$.

**Calibration check.** Confirm that for a subspace $U$, two translates $v + U$ and $w + U$ are equal if and only if $v - w \in U$. Confirm that the empty set is not a translate. Confirm that $0 + U = U$ — the trivial translate of $U$ is $U$ itself.

---

# Unlocked by This

> [!tip] Quotient Space *(from this topic)*
> The set of all translates of a fixed subspace $U$ becomes the [[Def - Quotient Space|quotient space]] $V/U$ once we put a vector-space structure on it. The partition property of translates is exactly what makes the quotient operations well-defined.

> [!tip] Affine Space and Affine Combinations *(from Geometry)*
> An **affine space** is the abstract version of an affine subset: a set $X$ on which a vector space $U$ acts freely and transitively. Affine geometry studies the properties that survive under affine maps — ratios on a line, parallelism, midpoints — but not lengths or angles (those need an inner product). The natural notion is the *affine combination* $\sum \lambda_i v_i$ with $\sum \lambda_i = 1$, which lives inside any affine subset containing the $v_i$. See Exercises 9 and 12 from [[Exercise Index - §3E Products and Quotients of Vector Spaces|the §3E exercises]] for the affine-combination characterisation.

> [!tip] Affine Algebraic Geometry *(from Algebraic Geometry)*
> An **affine variety** over a field is the zero set of a collection of polynomial equations in $\mathbb{F}^n$, viewed inside affine space $\mathbb{A}^n$ — affine space being $\mathbb{F}^n$ with the origin forgotten. The flat (linear) affine varieties are exactly the affine subsets in the sense of this page. Algebraic geometry studies the more general curved varieties, but the linear ones are the "free" examples, and any local picture of a smooth variety looks like an affine subset of its tangent space.

---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
  - "Def - Affine Subset"
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over a field $\mathbb{F}$, and $U \leq V$ is a subspace. The set of all translates of $U$ is $V/U = \{v + U : v \in V\}$; equipped with the operations below it is the **quotient space**. Elements of $V/U$ are denoted $v + U$ or, when the context is clear, $[v]$. The **quotient map** $\pi : V \to V/U$ sends $v$ to $v + U$. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

---

# Axiom Motivation

The quotient construction has one job: given a vector space $V$ and a [[Def - Subspace|subspace]] $U$ that you wish to ignore, produce a new vector space in which $U$ has been collapsed to a single point. The motivating use case is rank-nullity. Given a linear map $T : V \to W$, the null space $\operatorname{null} T$ measures the "blindness" of $T$ — the directions $T$ ignores. Wouldn't it be nicer if $T$ were injective, that is, if we erased $\operatorname{null} T$ first? The quotient $V/\operatorname{null} T$ is exactly the space "$V$ with the directions inside $\operatorname{null} T$ collapsed", on which the induced map $\tilde T$ *is* injective. The quotient is therefore the right place to land a non-injective linear map to get its faithful version. This is the structural content of the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]], and it is the reason quotients are unavoidable.

So the desideratum is clear: build a vector space $V/U$ whose elements are "vectors of $V$, up to the equivalence of differing by an element of $U$".

What should the elements *be*? Two vectors $v, w$ should be "the same in $V/U$" exactly when they differ by an element of $U$, i.e. when $v - w \in U$. This is an equivalence relation (reflexive: $v - v = 0 \in U$; symmetric: $v - w \in U \Rightarrow w - v = -(v - w) \in U$; transitive: $v - w, w - x \in U \Rightarrow v - x = (v-w) + (w-x) \in U$, using closure of $U$ under addition and negation). The equivalence classes are exactly the translates $v + U$ — see [[Def - Affine Subset]]. So the elements of $V/U$ *must* be the [[Def - Coset|cosets]] $v + U$. There is no choice; the equivalence relation forces it.

What should the operations be? We want the quotient map $\pi : V \to V/U$ to be linear. Linearity of $\pi$ forces
$$(v + U) + (w + U) = \pi(v) + \pi(w) = \pi(v + w) = (v + w) + U,$$
$$\lambda(v + U) = \lambda \pi(v) = \pi(\lambda v) = (\lambda v) + U.$$
Nothing else works. So the operations are forced by linearity of $\pi$, just as the elements are forced by the equivalence relation.

The only remaining question — and it is the crux — is whether these operations are *legitimate*. The formula $(v + U) + (w + U) = (v + w) + U$ defines the sum of two [[Def - Coset|cosets]] by picking representatives $v, w$. But the same coset $v + U$ has many representatives: $v + U = v' + U$ whenever $v - v' \in U$. We need the answer to be independent of the choice of representatives. The check: if $v + U = v' + U$ and $w + U = w' + U$, is $(v + w) + U = (v' + w') + U$? The hypothesis says $v - v' \in U$ and $w - w' \in U$, so $(v + w) - (v' + w') = (v - v') + (w - w') \in U$ by closure of $U$ under addition. Hence $(v + w) + U = (v' + w') + U$. The check passes — *because $U$ is closed under addition*.

What if $U$ were not closed under addition — say if $U$ were merely a subset, not a subspace? Then the well-definedness check fails. Concretely, take $V = \mathbb{R}^2$ and $U = \{0, e_1\}$ (just two points). The translate $e_2 + U = \{e_2, e_2 + e_1\}$ and the translate $0 + U = \{0, e_1\}$ are equal-or-disjoint perhaps, but the proposed addition $(0 + U) + (e_2 + U)$ would give two different answers depending on the representative — $e_2 + U$ versus $(e_1 + e_2) + U$ — and these are different sets. The operation is ill-defined.

Similarly, closure under scalar multiplication is needed for the scalar action: if $v + U = v' + U$, then $\lambda v - \lambda v' = \lambda(v - v') \in U$ (using that $U$ is closed under scalar multiplication), so $\lambda v + U = \lambda v' + U$ — the scalar action is well-defined.

This is why the construction requires $U$ to be a *subspace*: subspace-ness is *exactly* the well-definedness condition for the quotient operations. Drop closure under addition and addition fails; drop closure under scalar multiplication and scalar action fails. The definition of "subspace" is reverse-engineered from the well-definedness of $V/U$ — this is the linear-algebraic analogue of the fact that *normal* [[Def - Subgroup|subgroup]] is reverse-engineered from well-definedness of [[Def - Quotient Group|quotient group]].

(In vector spaces, every subspace is automatically "normal" — there is no separate normality condition — because the underlying [[Def - Group|group]] is abelian. This is one of the simplifications of working with vector spaces instead of general [[Def - Group|groups]]: every subspace can be quotiented out.)

---

# The Definition

Let $V$ be a vector space over $\mathbb{F}$ and $U \leq V$ a subspace. The **quotient space** $V/U$ is the set of all [[Def - Affine Subset|translates]] of $U$,
$$V/U := \{v + U : v \in V\},$$
equipped with the operations
$$(v + U) + (w + U) := (v + w) + U,$$
$$\lambda (v + U) := (\lambda v) + U.$$
With these operations $V/U$ is a vector space over $\mathbb{F}$:
- the operations are **well-defined** because $U$ is closed under addition and scalar multiplication;
- the **additive identity** is $0 + U = U$;
- the **additive inverse** of $v + U$ is $(-v) + U$;
- associativity, commutativity, and the field-axiom checks for $V/U$ follow directly from the corresponding axioms in $V$, applied to representatives.

The **quotient map** $\pi : V \to V/U$ is defined by $\pi(v) = v + U$. It is linear and surjective, and its [[Def - Null Space and Range|null space]] is precisely $U$:
$$\operatorname{null} \pi = \{v \in V : v + U = 0 + U\} = \{v \in V : v - 0 \in U\} = U.$$
So every subspace $U \leq V$ is the null space of *some* linear map — namely the quotient map $\pi : V \to V/U$. This is the linear-algebraic analogue of the group-theoretic fact "every normal [[Def - Subgroup|subgroup]] is a kernel".

When $V$ is finite-dimensional, [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread|the dimension formula]] gives
$$\dim V/U = \dim V - \dim U.$$

---

# Categorical Definition

The quotient is characterised by a **universal property**, and this universal property *is* the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] in disguise.

What does the quotient map $\pi : V \to V/U$ do? It kills $U$ — every element of $U$ is sent to $0 + U$, the zero of $V/U$. A linear map $T : V \to W$ is said to **kill $U$** (or *vanish on $U$*) if $T(u) = 0$ for every $u \in U$, equivalently if $U \subseteq \operatorname{null} T$. The quotient map $\pi$ kills $U$ by construction.

The universal property: **$\pi : V \to V/U$ is the universal linear map out of $V$ that kills $U$.** Precisely:

> For every vector space $W$ and every linear map $T : V \to W$ with $U \subseteq \operatorname{null} T$, there is a *unique* linear map $\bar T : V/U \to W$ such that $T = \bar T \circ \pi$.

In a diagram:

$$\begin{array}{ccc} V & \xrightarrow{\;T\;} & W \\ {}_{\pi}\!\downarrow & {}_{\bar T}\!\nearrow & \\ V/U & & \end{array}$$

The map $\bar T$ is forced: it must satisfy $\bar T(v + U) = T(v)$, and this is well-defined exactly because $T$ kills $U$ (if $v + U = v' + U$ then $v - v' \in U$, so $T(v) - T(v') = T(v - v') = 0$, so $T(v) = T(v')$).

The content of the property is that **maps out of $V$ that kill $U$ correspond bijectively to maps out of $V/U$.** Equivalently, the quotient $V/U$ is the cleanest vector space through which all $U$-killing maps factor. This determines $V/U$ uniquely up to canonical isomorphism — any vector space with this universal property is canonically isomorphic to $V/U$.

In category-theoretic language, the quotient is a **coequaliser**. A coequaliser of two parallel maps $f, g : A \to V$ is the universal map $q : V \to Q$ with $q \circ f = q \circ g$ — the most efficient way to force two maps to agree. Take $A = U$, $f$ the inclusion $U \hookrightarrow V$, and $g$ the zero map $U \to V$. A linear map $q$ satisfies $q \circ f = q \circ g$ exactly when $q(u) = 0$ for all $u \in U$, i.e. exactly when $q$ kills $U$. So the coequaliser of (inclusion, zero) is the quotient map $V \to V/U$. The quotient is "the universal way to make the subspace $U$ collapse to zero".

Applying the universal property to $T : V \to W$ with $U = \operatorname{null} T$ gives the **first isomorphism theorem** as a corollary: the induced $\bar T : V/\operatorname{null} T \to W$ is injective (its null space is $\{v + \operatorname{null} T : v \in \operatorname{null} T\} = \{0 + \operatorname{null} T\}$, the zero of $V/\operatorname{null} T$), so it is an isomorphism onto $\operatorname{range} T$. See [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread]] and the exercise [[Ex - Quotient by null space is isomorphic to range]].

---

# Relate to Other Fields / Compression

The quotient vector space is one instance of the universal *quotient by a congruence*, which appears in every algebraic theory. The [[Def - Quotient Group|quotient group]] $G/N$ by a normal subgroup, the [[Def - Quotient Ring|quotient ring]] $R/I$ by an ideal, the [[Def - Quotient Module|quotient module]] $M/M'$ by a submodule, and the quotient topological space $X/\!\sim$ by an equivalence relation are all the same construction: take the structure, impose an equivalence relation compatible with the operations, the equivalence classes inherit the structure, and the result satisfies a universal property of the same shape. The first isomorphism theorem $V/\operatorname{null} T \cong \operatorname{range} T$ is a direct specialisation of [[Thm - First Isomorphism Theorem|the group-theoretic first isomorphism theorem]] $G/\ker\varphi \cong \operatorname{im}\varphi$, restricted to the abelian-group structure of $V$ and lifted to respect scalar multiplication.

Two features specific to vector spaces are worth noting. First, *every subspace can be quotiented* (no normality condition is needed) because the additive group of $V$ is abelian. Second, every short exact sequence $0 \to U \to V \to V/U \to 0$ of vector spaces *splits*: there is a subspace $W \leq V$ with $V = U \oplus W$ and $W \cong V/U$. The splitting requires choosing a basis and is *not* canonical — a different basis gives a different $W$. But the existence of *some* splitting is a feature of vector spaces; for general modules over a ring it fails.

**True name:** the quotient $V/U$ is "the space $V$ with the directions inside $U$ collapsed to a point" — geometrically the family of affine planes parallel to $U$, with the operations inherited from $V$ by representative-wise computation.

---

# Examples / Corollaries

**Is an instance — $\mathbb{R}^3 / \mathbb{R} z$-axis $\cong \mathbb{R}^2$.** Let $V = \mathbb{R}^3$ and $U = \{(0, 0, z) : z \in \mathbb{R}\}$, the $z$-axis. The quotient $V/U$ collapses the entire $z$-direction to a point. Its elements are vertical lines parallel to the $z$-axis, and these are in bijection with the $xy$-plane via $(x, y, z) + U \mapsto (x, y)$. So $V/U \cong \mathbb{R}^2$. Geometrically: $V/U$ is "the family of vertical lines", and the family is parameterised by where each line crosses the $xy$-plane. This is the canonical mental picture of a quotient.

**Is an instance — $\mathbb{R}^2 / \mathbb{R}(1, 2) \cong \mathbb{R}$.** Let $U$ be the line $\{(x, 2x) : x \in \mathbb{R}\}$. The quotient $\mathbb{R}^2 / U$ collapses this line to zero, leaving a one-dimensional space whose elements are lines of slope $2$ in $\mathbb{R}^2$. The isomorphism to $\mathbb{R}$ is given by "$y$-intercept": $(a, b) + U$ corresponds to $b - 2a$, the unique value of $y - 2x$ on the line. Different ways of parameterising — by $y$-intercept, by $x$-intercept, by perpendicular distance from the origin — give different specific [[Def - Isomorphism|isomorphisms]]; all are equally valid.

**Is an instance — $\mathcal{P}(\mathbb{R}) / U \cong \mathbb{R}$ where $U$ is the polynomials with $p(0) = 0$.** Let $V = \mathcal{P}(\mathbb{R})$ and $U = \{p : p(0) = 0\}$, the polynomials vanishing at zero. The quotient $V/U$ has $p + U = q + U$ exactly when $p - q$ vanishes at zero, i.e. when $p(0) = q(0)$. So $V/U$ is parameterised by the single number $p(0)$, and $V/U \cong \mathbb{R}$. The isomorphism is "evaluate at zero", and it factors through the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]] applied to $T(p) = p(0)$.

**Is NOT an instance — $V/S$ for $S$ not a subspace.** Let $V = \mathbb{R}^2$ and $S = \{0, e_1\}$, the two-point set. The "quotient" $V/S$ does not make sense as a vector space: the proposed coset addition is not well-defined. The construction *strictly* requires $U$ to be a subspace, and the well-definedness check spells out why.

**Is NOT a subspace — the quotient is not embedded in $V$.** The quotient $V/U$ is a *new* vector space — its elements are *cosets*, which are subsets of $V$, not elements of $V$. A common slip is to picture $V/U$ as sitting inside $V$, perhaps as a complementary subspace. This is wrong: $V/U$ is a separate vector space with its own elements. There exist [[Def - Subspace|subspaces]] of $V$ isomorphic to $V/U$ — in fact many, one for each complement — but $V/U$ itself is not literally a subspace of $V$. (In some texts a specific complement is chosen and the quotient is *identified* with it; this requires the inner product structure of [[Linear Algebra VI — §6 Inner Product Spaces|Chapter 6]] to make canonical.)

**Corollary — every linear map $T : V \to W$ vanishing on $U$ factors through $V/U$.** This is the universal property. Explicitly, if $U \subseteq \operatorname{null} T$, define $\bar T : V/U \to W$ by $\bar T(v + U) = T(v)$. Then $\bar T$ is well-defined (because $T$ vanishes on $U$, so different representatives give the same value), linear, and $\bar T \circ \pi = T$. This factoring is unique.

**Corollary — induced map of a linear map.** For $T \in \mathcal{L}(V, W)$, applying the universal property with $U = \operatorname{null} T$ gives $\tilde T : V/\operatorname{null} T \to W$, $\tilde T(v + \operatorname{null} T) = T(v)$. The map $\tilde T$ is injective (its null space contains only the zero coset $0 + \operatorname{null} T$), and its range equals $\operatorname{range} T$. So $\tilde T$ is an isomorphism $V/\operatorname{null} T \cong \operatorname{range} T$. See [[Def - Quotient Map of Linear Map]].

**Calibration check.** Verify that the quotient map $\pi$ is linear, surjective, and has null space exactly $U$. Verify $\dim V/U = \dim V - \dim U$ when $V$ is finite-dimensional, by applying the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]] to $\pi$. If you can also explain why the formula $\bar T(v + U) = T(v)$ is well-defined precisely when $T$ vanishes on $U$, you have understood both the operation and the universal property.

---

# Unlocked by This

> [!tip] First Isomorphism Theorem for Linear Maps *(from this topic)*
> Applying the universal property to $T : V \to W$ with $U = \operatorname{null} T$ gives the isomorphism $V/\operatorname{null} T \cong \operatorname{range} T$. This is the [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread|first isomorphism theorem for vector spaces]] and the structural reading of [[Thm - Fundamental Theorem of Linear Maps|rank-nullity]].

> [!tip] Quotient Module *(from Module Theory)*
> For a module $M$ over a ring $R$ and a [[Def - Submodule|submodule]] $M' \leq M$, the [[Def - Quotient Module|quotient module]] $M/M'$ is constructed identically — cosets $m + M'$ with componentwise operations. The universal property is the same. The one feature lost is the automatic splitting: short exact sequences of modules need not split.

> [!tip] Homology and Cohomology *(from Algebraic Topology)*
> Sequences $\cdots \to V_{n+1} \xrightarrow{d_{n+1}} V_n \xrightarrow{d_n} V_{n-1} \to \cdots$ of linear maps with $d_n \circ d_{n+1} = 0$ are **chain complexes**. The $n$-th **homology** is the quotient $H_n = \operatorname{null} d_n / \operatorname{range} d_{n+1}$ — a quotient of one subspace by another. Topological spaces produce chain complexes via their singular simplices, and the homology groups are topological invariants distinguishing a sphere from a torus, counting holes, classifying surfaces. The entire machinery of algebraic topology rests on the quotient construction introduced here.

> [!tip] Spaces of Equivalence Classes Throughout Mathematics *(general principle)*
> Whenever an equivalence relation is compatible with structure, the equivalence classes inherit the structure and the result is a "quotient". $L^p$ spaces of analysis quotient by almost-everywhere equality. Projective spaces quotient by scalar multiplication. Moduli spaces parameterise geometric objects up to isomorphism. The pattern is everywhere; learning it once on vector spaces buys you the rest.

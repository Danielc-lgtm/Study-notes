---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Polynomial Ring"
  - "Def - Ideal"
  - "Def - Quotient Ring"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Affine Variety and the Vanishing Set"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. We keep the standing data of the chapter: a field $k$, an algebraically closed extension $\Omega \supseteq k$, and affine $n$-space $\Omega^n$. For $X \subseteq \Omega^n$ we write $I(X)$ for the ideal of polynomials vanishing on $X$, and for an algebraic set $X = V(\mathfrak a)$ we write $k[X] = k[T_1, \dots, T_n]/I(X)$ for its coordinate ring. The radical is $\sqrt{\mathfrak a} = \{f : f^m \in \mathfrak a,\ m \geq 1\}$; an ideal is **radical** if $\sqrt{\mathfrak a} = \mathfrak a$. The maximal ideal of a point $x \in k^n$ is $\mathfrak m_x = (T_1 - x_1, \dots, T_n - x_n)$. The full registry is on [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

This is a compound page: it defines two interlocking notions — the **ideal of a set** $I(X)$ (the algebra read off from geometry) and the **coordinate ring** $k[X]$ (the ring of polynomial functions on $X$) — because $k[X]$ is *defined* as the quotient by $I(X)$, so the two are inseparable: $I(X)$ is the relations, $k[X]$ is the resulting function algebra.

---

# Axiom Motivation

The [[Def - Affine Variety and the Vanishing Set|vanishing-set operation]] $V$ went from algebra to geometry: feed it an ideal, get back a shape. This page builds the *return arrow* and the object it produces. The return arrow $I$ goes from geometry to algebra: feed it a shape $X$, get back the ideal of all polynomials that vanish on $X$. The object is the **coordinate ring** $k[X]$ — the ring of polynomial functions on the shape — and the whole point is that *a variety and its ring of functions carry the same information*, so geometry can be done entirely with rings. This is the conceptual centre of the chapter and of algebraic geometry: **spaces are studied through their rings of functions.**

**Why $I(X)$ is an ideal, and why it is automatically radical.** Given $X \subseteq \Omega^n$, set $I(X) = \{f : f(x) = 0 \text{ for all } x \in X\}$, the polynomials vanishing identically on $X$. This is an [[Def - Ideal|ideal]]: if $f, g$ vanish on $X$ so does $f + g$, and if $f$ vanishes on $X$ then so does $hf$ for *any* $h$, because $(hf)(x) = h(x)f(x) = h(x)\cdot 0 = 0$. The absorption property — "anything times a vanishing function still vanishes" — is exactly the ideal axiom, and it is the reason "functions vanishing on $X$" is closed under multiplication by all of $k[T_1, \dots, T_n]$. Moreover $I(X)$ is always a [[Def - Radical of an Ideal and the Nilradical|radical]] ideal: if $f^m$ vanishes on $X$ then $f(x)^m = 0$ for each $x \in X$, and since $\Omega$ is an [[Def - Integral Domain|integral domain]], $f(x) = 0$ — so $f \in I(X)$. Geometry can never produce a non-radical ideal: a function either vanishes on $X$ or it does not, and raising it to a power changes nothing. This is the structural reason the eventual bijection is between varieties and *radical* ideals, not all ideals.

**Why functions on $X$ form the quotient $k[T_1, \dots, T_n]/I(X)$.** A polynomial $f \in k[T_1, \dots, T_n]$ restricts to a function $X \to \Omega$, $x \mapsto f(x)$. Two polynomials $f, g$ give the *same* function on $X$ exactly when $f - g$ vanishes on $X$, i.e. $f - g \in I(X)$. So the ring of polynomial functions on $X$ is the polynomial ring with two polynomials identified when they agree on $X$ — and "identify $f \sim g$ when $f - g \in I(X)$" is precisely the construction of the [[Def - Quotient Ring|quotient ring]] $k[X] = k[T_1, \dots, T_n]/I(X)$. The coordinate ring is forced: it is the *only* ring whose elements are genuinely the distinct functions on $X$, with no redundancy. Defining it as a quotient by anything smaller than $I(X)$ would leave distinct cosets that are equal as functions; by anything larger would merge functions that differ somewhere on $X$. The ideal $I(X)$ is exactly the right size, which is why it appears in the denominator.

**Why this matters: the dictionary $X \leftrightarrow k[X]$.** The construction would be a curiosity if the coordinate ring forgot the variety. It does not. The points of $X$ can be recovered from $k[X]$ as its maximal ideals (over $\Omega$), the irreducible pieces of $X$ as its minimal primes, the regular maps $X \to Y$ as the $k$-algebra homomorphisms $k[Y] \to k[X]$ — *the geometry is entirely encoded in the algebra of functions.* This is why one studies a variety by studying its coordinate ring: every geometric question becomes a ring-theoretic question, and the ring is something we can compute with. The coordinate ring is to an affine variety what the ring of smooth functions is to a manifold, but with an exact, finite, algebraic dictionary instead of an analytic one.

**What goes wrong if you forget radicality.** Suppose you tried to attach to *every* ideal $\mathfrak a$ a coordinate ring $k[T]/\mathfrak a$ and call it the functions on $V(\mathfrak a)$. The problem: $\mathfrak a$ and $\sqrt{\mathfrak a}$ have the *same* vanishing set ($V(\mathfrak a) = V(\sqrt{\mathfrak a})$), yet $k[T]/\mathfrak a$ and $k[T]/\sqrt{\mathfrak a}$ can differ — the first may contain **nilpotents** (nonzero elements some power of which is zero), which are functions that vanish at every point of $X$ yet are not themselves zero in the ring. For $\mathfrak a = (T^2)$ in $k[T]$, $V(\mathfrak a) = \{0\}$, and the class of $T$ in $k[T]/(T^2)$ is a nonzero function that vanishes at the only point — a "ghost". The radical ideal $I(\{0\}) = (T)$ removes the ghost. So insisting $k[X] = k[T]/I(X)$ with $I(X)$ radical is what guarantees $k[X]$ is **reduced** (no nilpotents) and its elements are honest functions. The nilpotents are not pathology — they are the seed of **scheme theory**, where one *keeps* the ideal $\mathfrak a$ and lets nilpotents record infinitesimal thickening — but for classical varieties one quotients them away.

---

# The Definition

Fix a field $k$, an algebraically closed extension $\Omega \supseteq k$, and $n \geq 0$.

## The ideal of a set

For a subset $X \subseteq \Omega^n$, the **ideal of $X$** (over $k$) is
$$I(X) = \{\, f \in k[T_1, \dots, T_n] : f(x) = 0 \text{ for all } x \in X \,\}.$$
It is an ideal of $k[T_1, \dots, T_n]$, and it is always a [[Def - Radical of an Ideal and the Nilradical|radical]] ideal.

## The coordinate ring

For a $k$-algebraic set $X \subseteq \Omega^n$, the **coordinate ring** (or **affine algebra**) of $X$ is the quotient $k$-algebra
$$k[X] := k[T_1, \dots, T_n] / I(X).$$
Its elements are the **regular functions** $X \to \Omega$ given by polynomials, two polynomials being identified when they agree on $X$. Because $I(X)$ is radical, $k[X]$ is a **reduced** ring (it has no nonzero nilpotents) and a finitely generated $k$-algebra.

## Formal properties of $I$

For subsets $X, Y \subseteq \Omega^n$ and $S, T \subseteq k[T_1, \dots, T_n]$:

1. $I$ is **inclusion-reversing**: $X \subseteq Y \implies I(X) \supseteq I(Y)$.
2. $S \subseteq I(V(S))$ and $X \subseteq V(I(X))$ (the Galois-connection inequalities).
3. $V(I(X))$ is the smallest $k$-algebraic set containing $X$ — its **Zariski closure**; in particular $V(I(X)) = X$ iff $X$ is $k$-algebraic.
4. $I(X)$ is radical for every $X$.

---

# Categorical / Structural Definition

The coordinate ring is the object that makes "affine variety" into a *functor*, and this is its deepest description. To a $k$-algebraic set $X$ one assigns the finitely generated reduced $k$-algebra $k[X]$; to a **regular map** $\varphi : X \to Y$ (a map given coordinatewise by polynomials) one assigns the **pullback** $\varphi^* : k[Y] \to k[X]$, $g \mapsto g \circ \varphi$, which precomposes a function on $Y$ with $\varphi$ to get a function on $X$. This assignment *reverses arrows* — a map of spaces gives a map of function-rings in the opposite direction — so it is a **contravariant functor** from algebraic sets to $k$-algebras. The fundamental theorem of the subject is that this functor is an *anti-equivalence of categories*: every finitely generated reduced $k$-algebra (over $\Omega$ algebraically closed) is $k[X]$ for a unique-up-to-isomorphism $X$, and every $k$-algebra homomorphism $k[Y] \to k[X]$ is $\varphi^*$ for a unique regular map $\varphi : X \to Y$. Geometry and commutative algebra are the same subject, read in opposite directions. This anti-equivalence is the precise meaning of "spaces are their rings of functions", and it is the affine prototype of the equivalence (schemes $\leftrightarrow$ rings) that founds modern algebraic geometry.

---

# Relate to Other Fields / Compression

The cleanest compression: **$k[X]$ is the ring of polynomial functions on $X$ — the polynomial ring with everything that vanishes on $X$ set to zero.** $I(X)$ is "the relations", $k[X]$ is "the functions modulo relations".

**True name:** the true name of $k[X]$ is "**the ring of regular functions on $X$**", and the true name of $I(X)$ is "**the relations satisfied by the coordinate functions on $X$**". Operationally: to compute $k[X]$, find generators and relations of the coordinate functions; to test whether $f = g$ as functions on $X$, test $f - g \in I(X)$. The slogan "$f$ vanishes on $X$" $\iff$ "$f \in I(X)$" $\iff$ "$f = 0$ in $k[X]$" is the constantly-used translation.

This is the algebraic-geometry version of a dictionary that recurs across mathematics: a space is recovered from its algebra of functions. In differential geometry, a smooth manifold $M$ is recovered from $C^\infty(M)$ (its maximal ideals are the points); in topology, a compact Hausdorff space from its ring of continuous functions ($C(X)$, by Gelfand–Naimark); in operator algebras, a "noncommutative space" *is* a $C^*$-algebra. The coordinate ring is the algebraic-geometry entry in this table, and it is the cleanest of all because the dictionary is exact and finite: $X \leftrightarrow k[X]$ is an honest anti-equivalence, with no analysis required.

---

# Examples / Corollaries

**Is an instance — affine space itself.** For $X = \Omega^n$, nothing nonzero vanishes everywhere (over the infinite field $\Omega$ a nonzero polynomial has a non-root), so $I(\Omega^n) = (0)$ and $k[\Omega^n] = k[T_1, \dots, T_n]$ — the coordinate ring of affine space is the polynomial ring, as it must be: the regular functions on $\mathbb{A}^n$ are the polynomials.

**Is an instance — a point.** For $X = \{x\}$ with $x \in k^n$, $I(\{x\}) = \mathfrak{m}_x = (T_1 - x_1, \dots, T_n - x_n)$ and $k[\{x\}] = k[T_1, \dots, T_n]/\mathfrak m_x \cong k$ via evaluation at $x$. The coordinate ring of a point is the field $k$: the only regular functions on a point are constants. The maximality of $\mathfrak m_x$ (its quotient is a field) is the algebraic expression of "$\{x\}$ is a point".

**Is an instance — the parabola.** For $X = V(T_2 - T_1^2) \subseteq \Omega^2$, $I(X) = (T_2 - T_1^2)$ and $k[X] = k[T_1, T_2]/(T_2 - T_1^2) \cong k[T_1]$ — substituting $T_2 = T_1^2$. The coordinate ring of the parabola is a polynomial ring in one variable, reflecting that the parabola is a curve, parametrised by $T_1$. Its transcendence degree is $1$, its dimension is $1$.

**Is NOT an instance (of a coordinate ring) — a ring with nilpotents.** $k[T]/(T^2)$ is *not* the coordinate ring of any classical variety, because it has a nonzero nilpotent $\bar T$ (with $\bar T^2 = 0$). Its "would-be variety" is $V(T^2) = \{0\}$, whose actual coordinate ring is $k[T]/(T) \cong k$. The class $\bar T$ is a nonzero element that vanishes at every point — not a function. Coordinate rings are always reduced; $k[T]/(T^2)$ is the smallest example of the "infinitesimal" rings that **schemes** allow but varieties forbid.

**Corollary — $I$ and $V$ are mutually inverse on algebraic sets.** Property (3) says $V(I(X)) = X$ for $X$ algebraic; the [[Thm - The Strong Nullstellensatz|strong Nullstellensatz]] supplies the other half, $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$. Together they make $X \mapsto I(X)$ and $\mathfrak a \mapsto V(\mathfrak a)$ inverse bijections between $k$-algebraic sets and radical ideals — the [[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|Nullstellensatz correspondence]].

**Calibration check.** Compute $I(\Omega^n) = (0)$, $I(\{x\}) = \mathfrak m_x$, and $k[V(T_2 - T_1^2)] \cong k[T_1]$ directly. Verify that $I(X)$ is radical from the integral-domain property of $\Omega$. Explain why $k[T]/(T^2)$ cannot be a coordinate ring by pointing to its nilpotent, and identify the function that the nilpotent "should be". If you can also say why $k[X]$ being reduced is equivalent to $I(X)$ being radical, you have understood the role of the radical in the construction.

---

# Unlocked by This

> [!tip] The anti-equivalence: affine varieties = finitely generated reduced algebras *(from Algebraic Geometry)*
> The assignment $X \mapsto k[X]$, $\varphi \mapsto \varphi^*$ is a contravariant functor that is an **anti-equivalence of categories** between affine $\Omega$-varieties and finitely generated reduced $\Omega$-algebras. Every such algebra is a coordinate ring; every algebra homomorphism is a pullback of a unique **regular map**. This is the theorem that *defines* the subject: to do geometry is to do commutative algebra in the opposite category. Dropping "reduced" and allowing all finitely generated algebras — keeping nilpotents — extends affine varieties to **affine schemes** $\operatorname{Spec} A$, where the nilpotents in $A$ record infinitesimal and multiplicity data invisible to the classical point set.

> [!tip] The Zariski tangent space and $\mathfrak m/\mathfrak m^2$ *(from Algebraic Geometry)*
> The local structure of $X$ near a point $x$ lives in the coordinate ring: the maximal ideal $\mathfrak m_x \subseteq k[X]$ of functions vanishing at $x$, and the quotient $\mathfrak m_x / \mathfrak m_x^2$, is the **cotangent space** of $X$ at $x$ (its dual is the **Zariski tangent space**). Smoothness, singularities, and the dimension of the tangent space are all read off $\mathfrak m_x/\mathfrak m_x^2$ — the algebra of functions sees not just the points but the infinitesimal geometry, developed via [[Commutative Algebra V — Nakayama's Lemma|Nakayama's lemma]] and the cotangent space.

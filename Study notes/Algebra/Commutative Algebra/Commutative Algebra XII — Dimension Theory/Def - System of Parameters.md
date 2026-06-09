---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Local Ring and Residue Field"
  - "Def - Krull Dimension and Height"
  - "Def - Noetherian Ring"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Prime and Maximal Ideal"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $(A, \mathfrak{m})$ be a Noetherian [[Def - Local Ring and Residue Field|local ring]] with unique maximal ideal $\mathfrak{m}$ and residue field $\kappa = A/\mathfrak{m}$. We write $d = \dim A$ for the [[Def - Krull Dimension and Height|Krull dimension]], $\mathfrak{q}$ for an **$\mathfrak{m}$-primary ideal** (an ideal whose [[Def - Radical of an Ideal and the Nilradical|radical]] is $\mathfrak{m}$), $\delta(\mathfrak{q})$ for the minimal number of generators of $\mathfrak{q}$, and $\delta(A) = \min\{\delta(\mathfrak{q}) : \mathfrak{q} \text{ is } \mathfrak{m}\text{-primary}\}$. A **system of parameters** is a generating set of size $d$ for an $\mathfrak{m}$-primary ideal. The full registry is on [[Commutative Algebra XII — Dimension Theory]].

---

# Axiom Motivation

On a smooth manifold near a point, you have local coordinates: $d$ functions $x_1, \dots, x_d$ that vanish at the point and cut it out cleanly, so that knowing their values pins down where you are. We want the algebraic version of this for a [[Def - Local Ring and Residue Field|local ring]] $(A,\mathfrak{m})$ — a minimal set of elements of the maximal ideal that "cut out the closed point" in the sharpest sense available. A **system of parameters** is exactly this: $d = \dim A$ elements $x_1,\dots,x_d \in \mathfrak{m}$ that generate an ideal whose radical is the whole of $\mathfrak{m}$. It is the algebraic notion of *local coordinates*, and the number $d$ of them is forced to equal the dimension.

**What "cut out the closed point" should mean, and why $\mathfrak{m}$-primary is the right condition.** The closed point of $\operatorname{Spec} A$ is $\mathfrak{m}$ itself. To say that $x_1,\dots,x_r$ "cut out only the closed point" should mean: the only prime containing all the $x_i$ is $\mathfrak{m}$ — equivalently, $V(x_1,\dots,x_r) = \{\mathfrak{m}\}$, a single point. Algebraically, the ideal $\mathfrak{q} = (x_1,\dots,x_r)$ has $V(\mathfrak{q}) = \{\mathfrak{m}\}$ precisely when $\sqrt{\mathfrak{q}} = \mathfrak{m}$, that is, when $\mathfrak{q}$ is **$\mathfrak{m}$-primary**. This is the correct relaxation of "$\mathfrak{q} = \mathfrak{m}$": we do not insist the $x_i$ generate $\mathfrak{m}$ on the nose (that would force $r = \delta(\mathfrak{m})$, the embedding dimension, which is too many at a singular point), only that they generate something with the same radical — the same zero locus. Demanding exact equality $\mathfrak{q} = \mathfrak{m}$ would conflate the *dimension* (how many coordinates the point needs) with the *embedding dimension* (how many the point needs to sit inside a smooth space), and these differ exactly at singularities. The radical condition isolates dimension alone.

**Why the count is $d = \dim A$, and not fewer or more.** This is the heart of the matter, and it is the [[Thm - The Dimension Theorem for Noetherian Local Rings|dimension theorem]]. You cannot cut the closed point out with fewer than $d$ elements: if $\sqrt{(x_1,\dots,x_r)} = \mathfrak{m}$ then $\mathfrak{m}$ is a minimal prime of $(x_1,\dots,x_r)$, so $\operatorname{ht}\mathfrak{m} = \dim A \leq r$ by [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]] — each generator can drop dimension by at most one, so $r$ generators can drop it by at most $r$, and to reach the closed point (dimension $0$) from the whole ring (dimension $d$) you need at least $d$ of them. And you can always do it with exactly $d$: the dimension theorem constructs, prime by prime, elements $x_1,\dots,x_d$ avoiding the lower-height primes, so that $\operatorname{ht}(x_1,\dots,x_i) = i$ at every stage and the final ideal is $\mathfrak{m}$-primary. So the minimal number $\delta(A)$ of generators of an $\mathfrak{m}$-primary ideal equals $\dim A$ — and a generating set realizing this minimum is a system of parameters.

**Why "system of parameters" is the operational definition of dimension.** The three quantities $\dim A$ (longest chain of primes), $d(G_{\mathfrak{m}}(A))$ (growth rate of the Hilbert–Samuel function), and $\delta(A)$ (minimal generators of an $\mathfrak{m}$-primary ideal) all agree. Of the three, $\delta(A)$ is the one you actually use to *bound* dimension from above, because exhibiting a single $\mathfrak{m}$-primary ideal with $r$ generators instantly proves $\dim A \leq r$. A system of parameters is the witness that the bound is tight: it is a length-$d$ certificate that the dimension is exactly $d$. Geometrically it is a choice of local coordinates; homologically (for regular rings) it is a regular sequence; computationally it is the input to the theory of multiplicities. The definition is engineered so that "the dimension is $d$" and "there exist $d$ parameters cutting out the point, and no fewer" are the same statement.

**The regular case, where parameters become honest coordinates.** When $\delta(\mathfrak{m}) = \dim A$ — that is, when $\mathfrak{m}$ *itself* can be generated by $d$ elements — the local ring is **regular**, and a system of parameters generating $\mathfrak{m}$ on the nose is a **regular system of parameters**: genuine local coordinates at a smooth point. In general $\delta(\mathfrak{m}) = \dim_\kappa \mathfrak{m}/\mathfrak{m}^2 \geq \dim A$, with equality exactly at regular (smooth) points; the gap $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 - \dim A$ measures the failure of smoothness. So a system of parameters is "coordinates that work even at a singular point", paid for by allowing the ideal to be only $\mathfrak{m}$-primary rather than all of $\mathfrak{m}$.

---

# The Definition

Let $(A, \mathfrak{m})$ be a Noetherian local ring of [[Def - Krull Dimension and Height|Krull dimension]] $d = \dim A$.

## $\mathfrak{m}$-primary ideal

An ideal $\mathfrak{q} \subseteq A$ is **$\mathfrak{m}$-primary** if $\sqrt{\mathfrak{q}} = \mathfrak{m}$; equivalently (in a Noetherian local ring) $\mathfrak{m}^t \subseteq \mathfrak{q} \subseteq \mathfrak{m}$ for some $t \geq 1$; equivalently $\mathfrak{m}$ is the only prime containing $\mathfrak{q}$, so that $A/\mathfrak{q}$ is Artinian (of finite length).

## The invariant $\delta(A)$

For an $\mathfrak{m}$-primary ideal $\mathfrak{q}$, let $\delta(\mathfrak{q})$ be the minimal cardinality of a generating set of $\mathfrak{q}$. Define
$$\delta(A) = \min\{\, \delta(\mathfrak{q}) : \mathfrak{q} \text{ is an } \mathfrak{m}\text{-primary ideal of } A \,\}.$$

## System of parameters

A **system of parameters** for $(A,\mathfrak{m})$ is a sequence $x_1, \dots, x_d \in \mathfrak{m}$ (with $d = \dim A$) such that the ideal $\mathfrak{q} = (x_1, \dots, x_d)$ is $\mathfrak{m}$-primary, i.e. $\sqrt{(x_1,\dots,x_d)} = \mathfrak{m}$.

By the [[Thm - The Dimension Theorem for Noetherian Local Rings|dimension theorem]], $\delta(A) = \dim A = d$, so a system of parameters is exactly a generating set, of the minimal possible size $d$, of an $\mathfrak{m}$-primary ideal — such a system always exists.

## Regular system of parameters (the smooth case)

If in addition $(x_1,\dots,x_d) = \mathfrak{m}$ (not merely $\mathfrak{m}$-primary), the system is a **regular system of parameters**, and $(A,\mathfrak{m})$ is a **regular local ring**. This requires $\delta(\mathfrak{m}) = \dim_\kappa \mathfrak{m}/\mathfrak{m}^2 = d$; in general $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 \geq d$.

---

# Relate to Other Fields / Compression

The cleanest compression: **a system of parameters is a choice of local coordinates at a point, valid even when the point is singular.** At a smooth point, $d$ coordinate functions $x_1,\dots,x_d$ generate the maximal ideal and cut the point out exactly; at a singular point you cannot do this with $d$ functions, but you *can* find $d$ functions whose common zero locus is still just the point (the ideal they generate has radical $\mathfrak{m}$). That relaxation — same zero set, not same ideal — is the entire concession to singularity.

**True name:** the operational name of a system of parameters is **"a length-$\dim A$ certificate that $\dim A$ is what you think it is"**. You produce one to prove $\dim A \leq d$ (any $\mathfrak{m}$-primary ideal with $d$ generators does this, via $\dim A = \delta(A) \leq d$), and the dimension theorem guarantees you cannot do better. In the regular case the true name upgrades to **"a regular sequence generating the maximal ideal"**, the algebraic incarnation of a coordinate chart.

This is the same construction as the **transcendence basis / Noether normalization** picture viewed locally. [[Thm - Noether Normalization|Noether normalization]] writes a finitely generated $k$-algebra as a finite module over a polynomial subring $k[y_1,\dots,y_d]$; localizing at a maximal ideal, the images of the $y_i$ (suitably translated to vanish at the point) form a system of parameters. So parameters are the local shadow of the global "the variety is finite over affine $d$-space" — both express that $d$ independent functions suffice to pin down position.

---

# Examples / Corollaries

**Is an instance — coordinates on affine space.** Let $A = k[X_1,\dots,X_n]_{(X_1,\dots,X_n)}$, the local ring of $\mathbb{A}^n$ at the origin, with $\mathfrak{m} = (X_1,\dots,X_n)$. Then $\dim A = n$, and $X_1,\dots,X_n$ is a regular system of parameters: they generate $\mathfrak{m}$ exactly, and $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 = n = \dim A$, so the origin is a smooth (regular) point. These are literally the coordinate functions.

**Is an instance — a non-regular parameter system on the same ring.** In the same $A$ with $n = 2$, the pair $X_1, X_2^2$ also cuts out the origin: $\sqrt{(X_1, X_2^2)} = (X_1, X_2) = \mathfrak{m}$, so $(X_1, X_2^2)$ is $\mathfrak{m}$-primary with $2 = \dim A$ generators, hence $X_1, X_2^2$ is a system of parameters. But it is *not* regular — it does not generate $\mathfrak{m}$ (it misses $X_2$). This shows that a system of parameters need not be a coordinate system; only regular ones are.

**Is an instance — a singular point needs the radical relaxation.** Let $A = k[X,Y]_{(X,Y)}/(Y^2 - X^3)$, the local ring of the cuspidal cubic at the cusp. Here $\dim A = 1$, but $\mathfrak{m} = (X,Y)$ needs $2$ generators ($\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 = 2 > 1 = \dim A$), so the cusp is singular. A system of parameters is the single element $X$ (or $Y$): $\sqrt{(X)} = \mathfrak{m}$ because $Y^2 = X^3 \in (X)$ forces $Y \in \sqrt{(X)}$. So one parameter cuts out the cusp, even though $\mathfrak{m}$ itself is not principal — exactly the case the $\mathfrak{m}$-primary relaxation is built for.

**Is NOT an instance — too few elements.** In $A = k[X,Y]_{(X,Y)}$ ($\dim A = 2$), the single element $X$ is *not* a system of parameters: $\sqrt{(X)} = (X)$ is the prime cutting out the line $X = 0$, not the maximal ideal, so $(X)$ is not $\mathfrak{m}$-primary. By Krull's height theorem you need at least $\dim A = 2$ elements to reach the closed point; one element can drop dimension only to $1$.

**Is NOT an instance — elements outside $\mathfrak{m}$.** A system of parameters must lie in $\mathfrak{m}$. If some $x_i$ is a unit, then $(x_1,\dots,x_d) = A$ is not proper, hence not $\mathfrak{m}$-primary (its radical is $A$, not $\mathfrak{m}$). The parameters must vanish at the point.

**Calibration check.** Verify $\sqrt{(X, Y^2)} = (X,Y)$ in $k[X,Y]_{(X,Y)}$, confirming the second example is a genuine system of parameters. Check that on the cusp $k[X,Y]/(Y^2-X^3)$ the element $X$ alone has $\sqrt{(X)} = \mathfrak{m}$ but $(X) \neq \mathfrak{m}$. Confirm that $\delta(A) \leq \dim A$ always fails to be obvious without the dimension theorem, but $\delta(A) \geq \dim A$ follows directly from Krull's height theorem (a minimal prime of an $r$-generated ideal has height $\leq r$).

---

# Unlocked by This

> [!tip] Regular local rings and smooth points *(from Algebraic Geometry)*
> A point of a variety is **smooth** (nonsingular) exactly when its local ring is **regular** — when the maximal ideal is generated by a system of parameters, i.e. $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 = \dim A$. The quotient $\mathfrak{m}/\mathfrak{m}^2$ is the **cotangent space** at the point (its dual is the Zariski tangent space), and a regular system of parameters is a basis of cotangent vectors — genuine local coordinates. The inequality $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 \geq \dim A$, with the gap measuring singularity, is the algebraic Jacobian criterion in disguise.

> [!tip] Regular sequences, depth, and Cohen–Macaulay rings *(from Commutative Algebra / Homological Algebra)*
> When a system of parameters is moreover a **regular sequence** (each $x_i$ a non-zero-divisor modulo the previous), the ring is **Cohen–Macaulay** — the case where dimension theory is as well-behaved as possible, and where the Hilbert–Samuel multiplicity, the length $\ell(A/(x_1,\dots,x_d))$, and intersection multiplicities all coincide. The maximal length of a regular sequence in $\mathfrak{m}$ is the **depth**, and $\operatorname{depth} A \leq \dim A$ always, with equality defining Cohen–Macaulay. Systems of parameters are the bridge from dimension (a chain invariant) to depth (a homological invariant).

> [!tip] Multiplicity and intersection theory *(from Algebraic Geometry)*
> For a system of parameters generating an $\mathfrak{m}$-primary ideal $\mathfrak{q}$, the **Hilbert–Samuel multiplicity** $e(\mathfrak{q}, A) = \lim_{n\to\infty} \dfrac{d!}{n^d}\,\ell(A/\mathfrak{q}^n)$ is a positive integer measuring how many points the parameters cut out "with multiplicity". This is the local engine of **intersection multiplicity** in algebraic geometry: when $d$ hypersurfaces meet at a point in the expected dimension, the multiplicity of their intersection is computed as such an $e(\mathfrak{q}, A)$, and Bézout's theorem is the global sum of these local numbers.

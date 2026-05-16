---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Subring"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $(R, +, \cdot, 0_R, 1_R)$ is a [[Def - Ring|ring]] — commutative and unital, by the standing convention. An element $u \in R$ is a **unit** if it has a multiplicative inverse; the inverse, when it exists, is written $u^{-1}$ (and is unique). The set of all units of $R$ is written $R^\times$ or $R^*$ and called the **group of units**. A ring in which $1_R \neq 0_R$ — equivalently $R \neq \{0\}$ — is a **non-zero ring**. The phrase "$R$ is a field" is reserved for a non-zero ring all of whose non-zero elements are units. See [[Rings I — §2.1–2.2]] for the full registry.

---

# Axiom Motivation

This page defines two concepts in sequence — the **unit** and the **field** — and the second is built on the first, so the motivation runs in two parts.

**Part 1: why "unit".** A [[Def - Ring|ring]] was deliberately designed so that division can fail: you can add, subtract, and multiply, but multiplicative inverses are not guaranteed. That immediately raises the question the notion of *unit* answers: *within* a given ring, which elements do happen to be invertible? We want a word for "an element you are allowed to divide by". The desideratum is that $u$ should be a unit exactly when the equation $u x = 1_R$ has a solution — because solving $ux = 1_R$ is precisely what lets you cancel $u$ and "divide by $u$". So the definition is forced: $u$ is a unit if there exists $v \in R$ with $u \cdot v = 1_R$.

Three design points deserve attention. First, why phrase it as "there exists $v$ with $uv = 1_R$" rather than naming $v$ up front? Because the inverse, once it exists, is **unique** — if $uv = 1_R$ and $uw = 1_R$ then $v = v \cdot 1_R = v(uw) = (vu)w = 1_R \cdot w = w$ — so existence is the only real content, and uniqueness justifies writing *the* inverse $u^{-1}$. Second, why $uv = 1_R$ and not, say, $uv = u$? Because $1_R$ is the element you are trying to manufacture: being a unit means you can *reach* the identity by multiplying, which is exactly what reversibility of multiplication asks. Third, and most important: **unit-ness is a property of the element relative to its ambient ring, not of the element alone.** The same number can be a unit in one ring and not in another, because the candidate inverses $v$ are drawn from the ring. The number $2$ is *not* a unit in $\mathbb{Z}$, since no integer $v$ satisfies $2v = 1$; but $2$ *is* a unit in $\mathbb{Q}$, with inverse $\tfrac{1}{2} \in \mathbb{Q}$. Nothing about the number $2$ changed — what changed is the pool of available inverses. This ring-dependence is not a defect of the definition; it is the whole point, and forgetting it is the most common error. If we tried to define "unit" without reference to a ring, the notion would be meaningless.

A natural check on the definition: the units of $R$ form a [[Def - Group|group]] under multiplication, the group of units $R^\times$. The product of two units is a unit (with $(uv)^{-1} = v^{-1}u^{-1}$), $1_R$ is a unit, and the inverse of a unit is a unit. So "unit" is exactly the notion that carves the multiplicative [[Def - Group|group]] out of the multiplicative *monoid* of a ring — it is the bridge from ring theory back to group theory.

**Part 2: why "field".** Having a name for the invertible elements, we can ask for the *best possible* ring: one where division never fails, where *every* element you could conceivably want to divide by actually is invertible. That is a field. But "every element" needs one careful exclusion. The element $0_R$ can never be a unit in a non-zero ring: if $0_R$ had an inverse $v$, then $1_R = 0_R \cdot v = 0_R$ (using $r \cdot 0_R = 0_R$ from [[Def - Ring]]), forcing $R = \{0\}$. Division by zero is impossible for structural reasons, not by convention. So the strongest sensible demand is "every *non-zero* element is a unit", and a **field** is a non-zero ring meeting exactly that demand.

Two clauses of the field definition each earn their place. Why insist the ring be **non-zero**? Because the zero ring $\{0\}$ satisfies "every non-zero element is a unit" *vacuously* — it has no non-zero elements — and we do not want the degenerate one-element ring to count as a field; the non-zero clause excludes it, and is equivalent to demanding $1_R \neq 0_R$. Why "every non-zero element", and not merely "some non-zero element is a unit"? Because that is the line between a field and a general ring: $\mathbb{Z}$ has units (namely $\pm 1$) but is emphatically not a field, since $2$ is not a unit. The field axiom is the *universal* statement — **all** non-zero elements invertible — and weakening "all" to "some" would let in $\mathbb{Z}$ and collapse the distinction. Strengthening is impossible: you cannot ask more than "every element you are allowed to divide by, you can".

Seen against the algebraic hierarchy, the motivation is crisp. A [[Def - Group|group]] sits one invertibility-axiom past a monoid. A field sits one invertibility-axiom (for non-zero elements) past a commutative ring — it is the ring-theoretic analogue of "upgrade the monoid to a group", applied to the multiplicative structure with $0_R$ set aside. A field is, in one phrase, a commutative ring whose non-zero elements form a group under multiplication.

---

# The Definition

Let $(R, +, \cdot, 0_R, 1_R)$ be a [[Def - Ring|ring]].

**Unit.** An element $u \in R$ is a **unit** if there exists an element $v \in R$ with
$$u \cdot v = 1_R.$$
The element $v$ is unique when it exists; it is called the **inverse** of $u$ and written $u^{-1}$. Whether a given $u$ is a unit depends on the ring $R$ — specifically on which candidate inverses $v$ the ring makes available — not on $u$ in isolation. The set of all units of $R$, written $R^\times$, forms an [[Def - Abelian Group|abelian group]] under multiplication, the **group of units**.

**Field.** A **field** is a non-zero ring — that is, a ring with $1_R \neq 0_R$ — in which **every** non-zero element is a unit. Equivalently, $R$ is a field if and only if $1_R \neq 0_R$ and $R^\times = R \setminus \{0_R\}$: the group of units is precisely the set of non-zero elements.

The element $0_R$ is never a unit in a non-zero ring, so "every non-zero element is a unit" is the strongest invertibility condition a ring can satisfy.

---

# Relate to Other Fields / Compression

A **unit** is the notion that converts a multiplicative *monoid* into a [[Def - Group|group]]: the units of $R$ are exactly the elements that the monoid $(R, \cdot, 1_R)$ contributes to a group, and $R^\times$ is the maximal subgroup of that monoid. This is the same move as passing from "the monoid of all $n \times n$ matrices under multiplication" to "the group $\mathrm{GL}_n$ of invertible matrices" — indeed $\mathrm{GL}_n(R)$ *is* the group of units of the matrix ring over $R$. The general slogan: **the group of units is the multiplicative group of a ring**, the part of the ring where group theory takes over.

A **field** is, most compactly, **a commutative ring one invertibility-axiom away from being as good as possible** — the exact analogue, on the multiplicative side, of upgrading a monoid to a [[Def - Group|group]]. It is also the structure on which linear algebra is built: a vector space is, by definition, a module over a field, and the field axioms are precisely what guarantee that Gaussian elimination works, that every non-zero scalar can be divided out, that systems of linear equations behave. When one replaces the field of scalars by a general [[Def - Ring|ring]], vector spaces degrade to *modules*, and the loss of the field axiom is exactly the loss of division. So "field" is the precise name for "a ring good enough to do linear algebra over".

---

# Examples / Corollaries

**Unit — is an instance: $\pm 1$ in $\mathbb{Z}$.** In the ring $\mathbb{Z}$, the units are exactly $1$ and $-1$: $1 \cdot 1 = 1$ and $(-1)(-1) = 1$. No other integer is a unit, because $|n| \geq 2$ forces $|nv| \geq 2 > 1$ for any non-zero integer $v$. So $\mathbb{Z}^\times = \{1, -1\}$, a two-element group. This shows a ring can have a few units without being anywhere near a field.

**Unit — is an instance, ring-dependence: $2$ in $\mathbb{Q}$.** The number $2$ **is** a unit in $\mathbb{Q}$, since $\tfrac{1}{2} \in \mathbb{Q}$ and $2 \cdot \tfrac{1}{2} = 1$. The very same number $2$ is **not** a unit in $\mathbb{Z}$, since no integer $v$ satisfies $2v = 1$. This pair is the canonical illustration that unit-ness depends on the ambient ring: the element is unchanged, the available inverses are not. *Calibration check:* if you can articulate why $2$ flips from non-unit to unit when the ring grows from $\mathbb{Z}$ to $\mathbb{Q}$, you have understood the definition.

**Unit — is NOT an instance: $0_R$ in any non-zero ring.** The zero element is never a unit when $1_R \neq 0_R$: if $0_R \cdot v = 1_R$ then, since $0_R \cdot v = 0_R$ (the absorbing-zero corollary of [[Def - Ring]]), we would get $1_R = 0_R$, contradicting non-zeroness. This non-example is the structural reason "every non-zero element" — rather than "every element" — is the right phrasing in the field definition.

**Unit — is NOT an instance: $1 + i$ in $\mathbb{Z}[i]$.** In the Gaussian integers, $1 + i$ is not a unit. A norm argument settles it: the map $N(a + bi) = a^2 + b^2$ is multiplicative, so a unit must have norm $1$, and $N(1 + i) = 2 \neq 1$. (The units of $\mathbb{Z}[i]$ are exactly the four elements of norm $1$, namely $\pm 1, \pm i$.) This probes the definition in a ring whose units are more interesting than $\pm 1$ but still finite.

**Field — is an instance: $\mathbb{Q}, \mathbb{R}, \mathbb{C}$.** Each of the rationals, the reals, and the complex numbers is a field. Each is a non-zero ring, and in each every non-zero element $x$ has an inverse: $\tfrac{1}{x} \in \mathbb{Q}$ for rational $x \neq 0$, likewise for $\mathbb{R}$, and for $\mathbb{C}$ the inverse of $a + bi \neq 0$ is $\tfrac{a - bi}{a^2 + b^2}$. These are the prototype fields and the scalar systems over which ordinary linear algebra is done.

**Field — is an instance: $\mathbb{Q}[\sqrt 2]$.** The [[Def - Subring|subring]] $\mathbb{Q}[\sqrt 2] = \{a + b\sqrt 2 : a, b \in \mathbb{Q}\}$ of $\mathbb{R}$ is a field. The non-obvious part is inverting a non-zero element: for $a + b\sqrt 2 \neq 0$,
$$\frac{1}{a + b\sqrt 2} = \frac{a - b\sqrt 2}{(a + b\sqrt 2)(a - b\sqrt 2)} = \frac{a - b\sqrt 2}{a^2 - 2b^2},$$
and the denominator $a^2 - 2b^2$ is a non-zero rational (it cannot vanish, since $\sqrt 2$ is irrational), so the inverse is again of the form $a' + b'\sqrt 2$ with rational coefficients. Hence every non-zero element is a unit and $\mathbb{Q}[\sqrt 2]$ is a field — a strictly stronger fact than its being a subring.

**Field — is NOT an instance: $\mathbb{Z}$.** The integers form a non-zero commutative ring, but **not** a field: the only units are $\pm 1$, so $2$ — a non-zero element — fails to be a unit. This is the defining non-example: $\mathbb{Z}$ has *some* units but not *all* non-zero elements as units, which is exactly the gap between a ring and a field, and exactly the gap that makes divisibility and prime factorization a non-trivial subject in $\mathbb{Z}$.

**Field — is NOT an instance: $\mathbb{Z}[i]$.** The Gaussian integers form a non-zero commutative ring whose units are only $\pm 1, \pm i$. Since $1 + i \neq 0$ is not a unit, $\mathbb{Z}[i]$ is not a field. Contrast this sharply with $\mathbb{Q}[\sqrt 2]$: both are subrings of familiar fields and both are built by adjoining one element, yet adjoining to $\mathbb{Z}$ keeps you outside the world of fields while adjoining to $\mathbb{Q}$ lands you inside it — the base ring's having division is what propagates.

**Corollary (a field is an [[Def - Subring|integral-domain]]-style ring with no zero divisors).** In a field, if $xy = 0_R$ then $x = 0_R$ or $y = 0_R$. Indeed if $x \neq 0_R$ then $x$ is a unit, and multiplying $xy = 0_R$ by $x^{-1}$ gives $y = x^{-1} \cdot 0_R = 0_R$. *Calibration check:* this shows every field is an integral domain — the converse fails, $\mathbb{Z}$ being the counterexample.

**Corollary (the only ideals of a field are $\{0_R\}$ and $R$).** If $I$ is an [[Def - Ideal|ideal]] of a field $R$ and $I \neq \{0_R\}$, pick a non-zero $x \in I$; since $x$ is a unit, $1_R = x^{-1}x \in I$ by absorption, whence $r = r \cdot 1_R \in I$ for every $r$, so $I = R$. *Calibration check:* a field has exactly two ideals, which is what makes fields the "simple objects" of ring theory and is the engine behind [[Def - Quotient Ring|quotients]] by maximal ideals being fields.

---

# Unlocked by This

> [!tip] Maximal Ideal *(from Commutative Algebra)*
> An [[Def - Ideal|ideal]] $\mathfrak{m} \trianglelefteq R$ is **maximal** exactly when the [[Def - Quotient Ring|quotient ring]] $R/\mathfrak{m}$ is a field. So the notion of "field" defined here is what gives the abstract maximal ideals their meaning — they are the ideals whose quotient is as good as a ring can be.

> [!tip] Field Extensions and Galois Theory *(from Algebra II)*
> Treating $\mathbb{Q}[\sqrt 2]$ as a field sitting above $\mathbb{Q}$ is the first example of a **field extension**. The systematic study of which fields sit inside which, and of the symmetry groups permuting their elements, is Galois theory — the framework that decides, for instance, that the general quintic has no formula in radicals.

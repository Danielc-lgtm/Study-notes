---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Subring"
  - "Def - Unit and Field"
  - "Def - Ring Homomorphism"
  - "Def - Integral Domain"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is an [[Def - Integral Domain|integral domain]] — a non-zero commutative [[Def - Ring|ring]] with no zero divisors. We write $R \leq F$ for "$R$ is a [[Def - Subring|subring]] of $F$" (more precisely, $F$ contains a subring isomorphic to $R$, and we identify $R$ with that copy). For $b \neq 0$ in a field $F$, $b^{-1}$ denotes the multiplicative inverse of $b$ in $F$. The field of fractions of $R$ is written $\operatorname{Frac}(R)$, and a typical element is a "fraction" $a/b = ab^{-1}$ with $a, b \in R$, $b \neq 0$. The full symbol registry is on [[Rings II — §2.3–2.4]].

---

# Axiom Motivation

We have just one model in mind, and the whole definition is reverse-engineered from it: $\mathbb{Q}$, the rationals, built out of $\mathbb{Z}$, the integers. The integers form an [[Def - Integral Domain|integral domain]] but not a field — $2$ has no inverse — and the historical fix was to *invent* the missing inverses by writing fractions $a/b$. We want to abstract this. Given any integral domain $R$, we want the smallest field that contains it. The question is: what properties should we *demand* of such a field, so that the demands pin it down uniquely and so that they are actually satisfiable?

Start with the obvious desideratum. The field $F$ we build should genuinely **contain $R$**: there should be a copy of $R$ sitting inside $F$ as a subring, $R \leq F$. Without this, $F$ would not deserve to be called "the fractions *of $R$*" — it must extend $R$, not replace it. This is the first axiom.

But "$F$ is a field containing $R$" is far too weak on its own. The field $\mathbb{R}$ contains $\mathbb{Z}$, and so does $\mathbb{C}$, and so does $\mathbb{Q}(\pi)$ — none of these is what we want, because each contains far more than fractions of integers. We want $F$ to be *exactly* the fractions and nothing more: **every** element of $F$ should be expressible as $ab^{-1}$ for some $a, b \in R$ with $b \neq 0$. This is the second axiom, and it is the one that does the work of saying "smallest". It forbids $\mathbb{R}$ (the number $\pi$ is not a ratio of integers) and forbids $\mathbb{C}$ (so is $i$), while permitting $\mathbb{Q}$ (every rational *is* a ratio of integers). The two axioms together say: $F$ is a field, it contains $R$, and it is built from $R$ using *only* the field operations applied to elements of $R$ — no foreign elements smuggled in.

Now, why must $R$ be an **integral domain** for any of this to work? This is the crucial design constraint, and it is not optional. We want to invert every non-zero element of $R$. Suppose $R$ had a zero divisor — non-zero $x, y$ with $xy = 0$. Inside the would-be field $F$, the element $x$ is non-zero, hence invertible; multiply $xy = 0$ by $x^{-1}$ to get $y = 0$, contradicting $y \neq 0$. So **a ring with a zero divisor cannot be embedded in any field at all**. The integral-domain hypothesis is precisely the necessary condition. The field-of-fractions theorem then proves it is also *sufficient*: every integral domain does embed in a field, and the converse "subring of a field $\Rightarrow$ integral domain" combines with it to give the clean equivalence — *a ring embeds in a field if and only if it is an integral domain*.

What breaks if we *weaken* the second axiom — drop "every element is a fraction" and ask only for *some* field containing $R$? Then the object is not unique: $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{Q}$ all qualify for $R = \mathbb{Z}$, and "the field of fractions" stops being a well-defined construction. The minimality clause is exactly what restores uniqueness (up to isomorphism). What breaks if we *strengthen* — demand, say, that $F$ be finite, or algebraically closed? We would be asking for something either impossible (an infinite domain has no finite fraction field) or far larger than fractions (the algebraic closure of $\mathbb{Q}$ contains $\sqrt{2}$, which is no ratio of integers). The two axioms are the exact pair: enough to force uniqueness, not so much as to become unsatisfiable.

---

# The Definition

Let $R$ be an [[Def - Integral Domain|integral domain]]. A **field of fractions** of $R$ is a [[Def - Unit and Field|field]] $F$ satisfying:

1. **Containment.** $R \leq F$ — that is, $R$ is (isomorphic to) a [[Def - Subring|subring]] of $F$.

2. **Minimality / fractions.** Every element of $F$ can be written as $a \cdot b^{-1}$ for some $a, b \in R$ with $b \neq 0_R$, where $b^{-1}$ is the inverse of $b$ taken in $F$.

The field of fractions is unique up to isomorphism (see the Categorical Definition below), so one speaks of *the* field of fractions, written $\operatorname{Frac}(R)$ or $\operatorname{Frac} R$. The prototype is $\operatorname{Frac}(\mathbb{Z}) = \mathbb{Q}$.

**The construction.** The field of fractions exists for every integral domain, and the construction is the abstraction of "building $\mathbb{Q}$ from $\mathbb{Z}$"; see [[Thm - Existence of the Field of Fractions]]. One forms the set of formal pairs
$$S = \{(a, b) \in R \times R : b \neq 0_R\},$$
thinking of $(a, b)$ as the fraction $\tfrac{a}{b}$, and imposes the equivalence relation
$$(a, b) \sim (c, d) \quad \Longleftrightarrow \quad ad = bc,$$
which is the cross-multiplication test for equality of fractions. (Reflexivity and symmetry are immediate; **transitivity is exactly where the integral-domain hypothesis is spent** — proving it requires cancelling a non-zero denominator.) The field of fractions is the set of equivalence classes $F = S/\!\sim$, with the class of $(a, b)$ written $a/b$, equipped with
$$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}, \qquad \frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}.$$
These are well-defined; $0_F = 0/1$ and $1_F = 1/1$; and every non-zero $a/b$ (meaning $a \neq 0$) has inverse $b/a$, so $F$ is a field. The integral domain $R$ is embedded by the injective [[Def - Ring Homomorphism|ring homomorphism]] $\varphi : R \to F$, $\varphi(r) = r/1$, and one identifies $R$ with its image $\varphi(R) \leq F$.

---

# Categorical Definition

The field of fractions has a clean **universal property**, and this is the conceptually correct definition — it makes precise the slogan "$\operatorname{Frac}(R)$ is the *smallest* field containing $R$" and delivers uniqueness for free.

A *universal property* characterises an object not by what it is made of, but by how it maps to (or receives maps from) every other object of a given kind. Here the relevant kind is "fields receiving an injective ring homomorphism from $R$". The statement is:

> **Universal property of $\operatorname{Frac}(R)$.** Let $R$ be an integral domain with embedding $\iota : R \hookrightarrow \operatorname{Frac}(R)$, $r \mapsto r/1$. For *every* field $K$ and *every* injective ring homomorphism $f : R \to K$, there exists a *unique* ring homomorphism $\bar f : \operatorname{Frac}(R) \to K$ such that $\bar f \circ \iota = f$ — that is, $\bar f$ restricted to (the copy of) $R$ equals $f$. The map $\bar f$ is automatically an injective field homomorphism.

In words: any embedding of $R$ into any field $K$ **factors uniquely through $\operatorname{Frac}(R)$**. The forced formula is $\bar f(a/b) = f(a) f(b)^{-1}$ — there is no choice, because $a/b = \iota(a)\iota(b)^{-1}$ must be sent to $f(a)f(b)^{-1}$, and this both *proves uniqueness* and *defines* $\bar f$.

Two consequences make this the "smallest field" statement precise. First, since $\bar f$ is injective, $\operatorname{Frac}(R)$ embeds inside *every* field that contains $R$ — so it is the smallest such field. Second, an object defined by a universal property is unique up to a *unique* isomorphism: if $F$ and $F'$ both have the property, the universal maps $F \to F'$ and $F' \to F$ compose to the identity, so $F \cong F'$. This is why "*the* field of fractions" is legitimate language.

Categorically, $\operatorname{Frac}$ is a special case of **localisation**: $\operatorname{Frac}(R) = S^{-1}R$ where $S = R \setminus \{0\}$ is the multiplicative set of all non-zero elements. Localisation is the universal way to invert a chosen set of elements, and inverting *everything non-zero* in an integral domain produces a field. In the language of adjoint functors, $\operatorname{Frac}$ is the left adjoint, restricted to integral domains, of the forgetful functor from fields to integral domains.

---

# Relate to Other Fields / Compression

The field of fractions is the ring-theoretic instance of a universal pattern that recurs across algebra: **freely adjoining inverses**. In group theory, the *Grothendieck group* (group completion) takes a cancellative commutative monoid and produces the smallest abelian group containing it — for the monoid $(\mathbb{N}, +)$ this yields $(\mathbb{Z}, +)$, by exactly the construction of equivalence classes of pairs $(a,b)$ representing $a - b$. The field of fractions is the *multiplicative* version of the very same construction: it takes the cancellative commutative monoid $(R \setminus \{0\}, \cdot)$ and completes it to an abelian group, the non-zero elements of $\operatorname{Frac}(R)$, with the pair $(a, b)$ now representing $a / b$ instead of $a - b$. The integral-domain hypothesis plays the role that cancellativity plays for the monoid: it is exactly what makes the pair-equivalence transitive. So "$\mathbb{Q}$ from $\mathbb{Z}$" and "$\mathbb{Z}$ from $\mathbb{N}$" are the same theorem, once additively and once multiplicatively.

More generally still, this is the special case $S = R \setminus \{0\}$ of **localisation** $S^{-1}R$, the universal construction inverting an arbitrary multiplicatively closed set $S$. Localising at other sets gives other familiar rings: inverting all integers prime to a fixed prime $p$ turns $\mathbb{Z}$ into the local ring $\mathbb{Z}_{(p)}$; inverting powers of a single element $f$ gives $R[1/f]$, the coordinate ring of a distinguished open set in algebraic geometry. The field of fractions is the extreme case where so much is inverted that the result collapses to a field. Geometrically, $\operatorname{Frac}(R)$ is the *function field* of the irreducible variety $\operatorname{Spec} R$ — the field of rational functions on the space — and "every element is a fraction" is the statement that every rational function is a ratio of polynomials.

---

# Examples / Corollaries

**Is an instance — $\operatorname{Frac}(\mathbb{Z}) = \mathbb{Q}$.** The defining example. The integers form an integral domain, $\mathbb{Z} \leq \mathbb{Q}$, and every rational number is by definition $a/b$ with $a, b \in \mathbb{Z}$, $b \neq 0$. The entire abstract definition is "do to a general $R$ what the schoolbook construction does to $\mathbb{Z}$".

**Is an instance — $\operatorname{Frac}(F) = F$ for any field $F$.** If $R$ is already a [[Def - Unit and Field|field]] $F$, its field of fractions is $F$ itself: $F \leq F$ trivially, and every element $a \in F$ is the fraction $a/1 = a \cdot 1^{-1}$. A field has nothing to gain from the construction — every non-zero element is already invertible. This is the calibration check that the construction does not *change* anything already complete.

**Is an instance — $\operatorname{Frac}(F[X]) = F(X)$, the field of rational functions.** For a field $F$, the [[Def - Polynomial Ring|polynomial ring]] $F[X]$ is an integral domain, and its field of fractions is the field $F(X)$ of **rational functions** — formal ratios $p(X)/q(X)$ of polynomials with $q \neq 0$. This is the example that shows the construction produces genuinely new and useful fields, not just recovers old ones: $F(X)$ is the natural home of partial-fraction decomposition and the function field of the projective line.

**Is an instance — $\operatorname{Frac}(\mathbb{Z}[i]) = \mathbb{Q}(i)$.** The Gaussian integers $\mathbb{Z}[i]$ form an integral domain, and inverting their non-zero elements yields $\mathbb{Q}(i) = \{p + qi : p, q \in \mathbb{Q}\}$, the Gaussian rationals. More generally the fraction field of a ring of algebraic integers is the corresponding algebraic number field — the construction is the bridge from [[Def - Ring|rings]] of integers to number fields.

**Is NOT an instance — $\mathbb{R}$ is not a field of fractions of $\mathbb{Z}$.** The reals $\mathbb{R}$ form a field and contain $\mathbb{Z}$, so axiom 1 holds — but axiom 2 fails badly: $\pi \in \mathbb{R}$ is not equal to any ratio $a/b$ of integers. So $\mathbb{R}$ satisfies "field containing $\mathbb{Z}$" without being the field of fractions. This non-example pinpoints the role of the minimality axiom: without it the construction would not be unique, and $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}(\pi)$ would all qualify.

**Is NOT an instance — $\mathbb{Z}/6$ has no field of fractions.** The ring $\mathbb{Z}/6$ is *not* an integral domain ($2 \cdot 3 = 0$), and it has no field of fractions whatsoever — indeed it cannot be embedded in any field. If $\mathbb{Z}/6 \leq F$ for a field $F$, then $2$ is a non-zero element of $F$ hence invertible, and $2 \cdot 3 = 0$ multiplied by $2^{-1}$ forces $3 = 0$, a contradiction. This is the non-example proving the integral-domain hypothesis is *necessary*, not a convenience.

**Corollary — a ring embeds in a field if and only if it is an integral domain.** One direction is the existence theorem ([[Thm - Existence of the Field of Fractions]]); the other is the easy observation that any [[Def - Subring|subring]] of a field is an integral domain (a field has no zero divisors, and the property is inherited by [[Def - Subring|subrings]]). Together they give a complete, memorable characterisation: *embeddability in a field $\iff$ no zero divisors*.

**Calibration check.** Confirm that the equivalence relation $(a,b) \sim (c,d) \iff ad = bc$ would *fail to be transitive* in $\mathbb{Z}/6$ — find pairs witnessing the failure — and identify exactly which step of the transitivity proof needs cancellation. Check that $\operatorname{Frac}(\mathbb{Z}[X]) = \mathbb{Q}(X)$, not $\mathbb{Z}(X)$ (the construction inverts integers too, not just polynomials). If you can also state the universal property without looking and explain why it forces $\operatorname{Frac}(R)$ to be unique, you have understood the definition at the level that matters.

---

# Unlocked by This

> [!tip] Function Fields and Number Fields *(from Algebraic Geometry and Number Theory)*
> The field of fractions of a coordinate ring is the *function field* of a variety; the field of fractions of a ring of integers is an *algebraic number field*. The construction is the standard passage from a ring of "integral" objects to its field of "rational" objects.

> [!tip] Localisation *(from Commutative Algebra)*
> $\operatorname{Frac}(R)$ is the extreme case $S = R \setminus \{0\}$ of localisation $S^{-1}R$, the universal inversion of a multiplicative set. Localising at other sets builds local rings and the structure sheaf of a scheme.

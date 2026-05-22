---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Ring"
  - "Def - Abelian Group"
tags: [algebra, linear-algebra]
---

# Notation

A field is written $(\mathbb{F}, +, \cdot, 0, 1)$: the underlying set $\mathbb{F}$, an addition $+ : \mathbb{F} \times \mathbb{F} \to \mathbb{F}$, a multiplication $\cdot : \mathbb{F} \times \mathbb{F} \to \mathbb{F}$, an additive identity $0$, and a multiplicative identity $1 \neq 0$. The additive inverse of $a$ is $-a$; the multiplicative inverse of $a \neq 0$ is $a^{-1}$, also written $1/a$. Subtraction is $b - a = b + (-a)$ and division by $a \neq 0$ is $b/a = b \cdot a^{-1}$. The set $\mathbb{F} \setminus \{0\}$ with multiplication is the **multiplicative group** $\mathbb{F}^\times$.

Throughout linear algebra, $\mathbb{F}$ denotes either $\mathbb{R}$ or $\mathbb{C}$ unless stated otherwise (the convention used by Axler). Almost every result in [[Linear Algebra I — §1 Vector Spaces]] holds verbatim for an arbitrary field, with the inner-product chapters being the chief exception. See [[Linear Algebra I — §1 Vector Spaces]] for the full notation registry.

---

# Axiom Motivation

A field is the abstraction of the **number systems on which arithmetic — including division — works without exception**. The motivating examples are $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$: in each you can add, subtract, multiply, and divide (by anything nonzero), with all the familiar rules. A field is the attempt to write down exactly those rules and no more, so that any theorem proved from them holds for $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, the finite fields $\mathbb{F}_p$, function fields, and so on, all at once.

Why so many axioms? Because two operations are interacting, and each one alone has to behave well *and* the two together have to be glued by a distributive law. The cleanest way to see what is going on is to read the definition as the conjunction of three groups of axioms, each demanding one feature. **Group one**: the additive structure $(\mathbb{F}, +, 0)$ is an [[Def - Abelian Group|abelian group]]. **Group two**: the multiplicative structure $(\mathbb{F} \setminus \{0\}, \cdot, 1)$ is an abelian group. **Group three**: the distributive law $a(b + c) = ab + ac$ ties them together. Once you read the definition this way, the long list of properties (commutativity of $+$, associativity of $+$, identity, inverse, commutativity of $\cdot$, associativity of $\cdot$, identity, inverse, distributivity) collapses to "two abelian groups bridged by distributivity", and you understand it in one line.

What happens if you drop pieces? Drop multiplicative inverses for nonzero elements and you get a **commutative [[Def - Ring|ring]] with $1$**, such as $\mathbb{Z}$: in $\mathbb{Z}$ you can add, subtract, and multiply, but $2$ has no reciprocal, so division fails and equations like $2x = 1$ are unsolvable. Drop commutativity of multiplication and you get a **division ring** or **skew field**, such as the quaternions $\mathbb{H}$. Drop the demand $1 \neq 0$ and you allow the trivial "field" with one element, which destroys most theorems silently — for instance the multiplicative group $\mathbb{F}^\times$ would be empty — so the axiom $1 \neq 0$ is included to outlaw the degenerate case. Drop distributivity and the two operations stop talking to each other, and the structure ceases to model arithmetic at all: you could no longer expand $(a + b)c$, and even the proof that $0 \cdot a = 0$ would fail.

The single most consequential axiom is the existence of multiplicative inverses for *all* nonzero elements. This is the axiom whose failure separates $\mathbb{Z}$ from $\mathbb{Q}$, and it is the axiom that makes Gaussian elimination work, makes linear systems solvable, and makes the dimension of a vector space well-defined. The reason vector spaces are studied over fields and not over arbitrary commutative rings is that without inverses you cannot divide pivot entries, and so reduced row-echelon form, the rank-nullity theorem, and the existence of bases all become subtler. The general theory over a ring is called **module theory** (see [[Def - Module]]) and is genuinely harder: a finitely generated module over a ring need not have a basis. So when you read "a vector space over $\mathbb{F}$", read it as "a module over a structure flexible enough that division always works", and you will not be surprised that the theory is clean.

A subtle but consequential corollary of the axioms is **no zero divisors**: $ab = 0$ forces $a = 0$ or $b = 0$. If $a \neq 0$ and $ab = 0$, multiplying by $a^{-1}$ gives $b = 0$. This is not built in as a separate axiom; it falls out of inverses. It is what makes the polynomial ring $\mathbb{F}[x]$ an [[Def - Polynomial Ring|integral domain]] and is the gateway to the division algorithm and ultimately to the [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|minimal polynomial of an operator]].

In summary, a field is the structure with two compatible abelian groups — addition on $\mathbb{F}$ and multiplication on $\mathbb{F}^\times$ — joined by a distributive law and forced to be non-degenerate by $1 \neq 0$. Drop any piece and you lose exactly one of: subtraction, division, commutativity, or non-triviality.

---

# The Definition

A **field** is a tuple $(\mathbb{F}, +, \cdot, 0, 1)$ where $\mathbb{F}$ is a set, $+$ and $\cdot$ are binary operations $\mathbb{F} \times \mathbb{F} \to \mathbb{F}$, and $0, 1 \in \mathbb{F}$ are distinguished elements, satisfying:

1. **Commutativity.** $a + b = b + a$ and $a \cdot b = b \cdot a$ for all $a, b \in \mathbb{F}$.
2. **Associativity.** $(a + b) + c = a + (b + c)$ and $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c \in \mathbb{F}$.
3. **Identities.** $a + 0 = a$ and $a \cdot 1 = a$ for all $a \in \mathbb{F}$.
4. **Additive inverses.** For every $a \in \mathbb{F}$ there exists $-a \in \mathbb{F}$ with $a + (-a) = 0$.
5. **Multiplicative inverses.** For every $a \in \mathbb{F}$ with $a \neq 0$ there exists $a^{-1} \in \mathbb{F}$ with $a \cdot a^{-1} = 1$.
6. **Distributivity.** $a \cdot (b + c) = a \cdot b + a \cdot c$ for all $a, b, c \in \mathbb{F}$.
7. **Non-triviality.** $0 \neq 1$.

Equivalently, a field is a commutative [[Def - Ring|ring]] with $1$ in which every nonzero element is invertible (and $0 \neq 1$).

The **characteristic** of $\mathbb{F}$ is the least $n > 0$ with $\underbrace{1 + 1 + \cdots + 1}_{n} = 0$, or $0$ if no such $n$ exists. The characteristic of $\mathbb{Q}, \mathbb{R}, \mathbb{C}$ is $0$; the characteristic of $\mathbb{F}_p$ is $p$.

---

# Categorical / Structural Definition

A field is a **commutative ring object in $\mathbf{Set}$ in which every nonzero arrow $1 \to \mathbb{F}$ has a multiplicative inverse**, but more illuminating is the lattice picture. The class of structures sits in a strict hierarchy by axiom-dropping:

$$\text{field} \;\subset\; \text{integral domain} \;\subset\; \text{commutative ring with $1$} \;\subset\; \text{commutative ring}.$$

Reading right to left: a *commutative ring* has compatible addition and multiplication; adding a multiplicative identity $1$ gives a *commutative ring with $1$*; demanding that products of nonzero things are nonzero ("no zero divisors") gives an *integral domain*; demanding that every nonzero element be invertible gives a *field*. The field axioms are therefore the *strongest* axiom set in this lattice, which is why the theory of vector spaces over fields is so much cleaner than the theory of modules over rings.

A second structural perspective: a field is determined by its **multiplicative group $\mathbb{F}^\times$** and its **additive group $(\mathbb{F}, +)$**, glued by distributivity. The two abelian groups have different sizes — $|\mathbb{F}^\times| = |\mathbb{F}| - 1$ when $\mathbb{F}$ is finite — and the distributive law is the entire content of the interaction. So a field is, structurally, two abelian groups on overlapping sets agreeing on $1 \cdot a = a$ and bridged by $a(b+c) = ab + ac$.

---

# Relate to Other Fields / Compression

The cleanest compression is that **a field is a commutative ring in which every nonzero element is invertible**. The ring axioms govern addition, multiplication, and distributivity; promoting "some elements have multiplicative inverses" to "all nonzero elements have multiplicative inverses" lifts a commutative ring to a field. Most of what changes in moving from $\mathbb{Z}$ to $\mathbb{Q}$ — being able to divide, solve $ax = b$ for any $a \neq 0$, normalize equations — is exactly this single axiom.

A second compression: a field is the home of **linear systems with unique row-reduction**. The reason Gaussian elimination is an algorithm — and not just a heuristic that sometimes works — is that you can divide by any nonzero pivot to scale rows. Over a ring without inverses this step fails, and one resorts to the Smith normal form. From the systems-of-linear-equations side, "the scalars come from a field" is the price of paying for row-reduction to always terminate cleanly.

**True name:** the operational true name of a field is "the place where every nonzero number has a reciprocal and you can divide". This is what you actually use: in every linear-algebra proof where you write $v = \tfrac{1}{a}(av)$ to extract a vector, in every Gaussian-elimination pivot, in the proof that the dimension of a vector space is well-defined, what is silently invoked is division by a nonzero scalar.

---

# Examples / Corollaries

**Is an instance: $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$.** The rational, real, and complex numbers with their usual addition and multiplication. Each has characteristic $0$. $\mathbb{C}$ has the additional property of being **algebraically closed**: every non-constant polynomial in $\mathbb{C}[x]$ has a root. This is the property that makes the existence of eigenvalues work in [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]], and it is why complex vector spaces have a much cleaner spectral theory than real ones.

**Is an instance: the finite field $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ for prime $p$.** The integers modulo a prime form a field of characteristic $p$ with exactly $p$ elements. Multiplicative inverses exist by Bezout: for $a \not\equiv 0 \pmod p$ there are integers $u, v$ with $au + pv = 1$, so $u$ is the multiplicative inverse of $a$ modulo $p$. The case $p = 2$ gives the smallest field, $\mathbb{F}_2 = \{0, 1\}$ with $1 + 1 = 0$.

**Is an instance: $\mathbb{F}_{p^n}$, the field with $p^n$ elements.** For every prime $p$ and every $n \geq 1$ there is a unique (up to isomorphism) field of order $p^n$. These are built as quotients of $\mathbb{F}_p[x]$ by an irreducible polynomial of degree $n$ and play the role of "scalars" in coding theory and cryptography. The order of any finite field is always a prime power, never any other integer.

**Is an instance: the field of rational functions $\mathbb{F}(x)$.** The fractions $p(x)/q(x)$ with $p, q \in \mathbb{F}[x]$ and $q \neq 0$, modulo the usual equivalence, form a field. It is the "field of fractions" of the integral domain $\mathbb{F}[x]$, just as $\mathbb{Q}$ is the field of fractions of $\mathbb{Z}$. It plays a role in algebraic geometry and in the study of meromorphic functions.

**Is NOT an instance: $\mathbb{Z}$.** The integers form a [[Def - Ring|commutative ring with $1$]] but **fail axiom 5** (multiplicative inverses): $2$ has no reciprocal in $\mathbb{Z}$. This is the prototypical "almost a field but not quite", and the failure is exactly why integer linear algebra is harder than rational or real linear algebra.

**Is NOT an instance: $\mathbb{Z}/4\mathbb{Z}$.** The integers modulo $4$ form a commutative ring but **fail axiom 5** for non-units: $2 \cdot 2 = 4 \equiv 0$, so $2$ is a zero divisor and certainly has no inverse. The general fact is that $\mathbb{Z}/n\mathbb{Z}$ is a field if and only if $n$ is prime. This non-example probes why the modulus must be prime, and is a good calibration test.

**Is NOT an instance: the quaternions $\mathbb{H}$.** Hamilton's quaternions have additive and multiplicative identities, additive and multiplicative inverses, and distributivity — but multiplication is **not commutative**, $ij = k$ while $ji = -k$. So $\mathbb{H}$ is a *skew field* or *division ring*, not a field. The non-commutativity prevents the determinant from being well-behaved and ruins much of standard linear algebra; modules over $\mathbb{H}$ have a recognizable but distinct theory.

**Corollary (no zero divisors).** In any field, $ab = 0$ implies $a = 0$ or $b = 0$. If $a \neq 0$, multiply both sides by $a^{-1}$ to get $b = a^{-1} \cdot 0 = 0$. This is what licenses the manipulation "$a v = 0$ with $a \neq 0$ forces $v = 0$" in vector spaces, and is the reason the only ways a product of scalars vanishes are the obvious ones.

**Corollary (uniqueness of inverses).** Each $a \neq 0$ has a unique multiplicative inverse, and $0$ has a unique additive inverse. If $b$ and $b'$ both satisfy $ab = ab' = 1$, then $b = b \cdot 1 = b \cdot ab' = (ba) b' = b'$. Uniqueness justifies the notation $a^{-1}$.

**Corollary (cancellation).** If $a \neq 0$ and $ab = ac$, then $b = c$. Multiply both sides by $a^{-1}$. This is the field-version of left-cancellation in groups, and is the engine of Gaussian elimination.

**Calibration check.** If you have understood the definition you should be able to (i) check that $\mathbb{F}_2 = \{0, 1\}$ with $1 + 1 = 0$ is a field by listing its tables, (ii) explain in one sentence why $\mathbb{Z}/6\mathbb{Z}$ fails to be a field (a zero divisor: $2 \cdot 3 = 0$), and (iii) write down the multiplicative inverse of $3$ in $\mathbb{F}_7$ (it is $5$, since $3 \cdot 5 = 15 \equiv 1$).

---

# Unlocked by This

> [!tip] Vector Space *(from Linear Algebra)*
> The fields are the scalars over which **vector spaces** are defined — see [[Def - Vector Space]]. Replacing the field by an arbitrary ring gives a [[Def - Module|module]], a more general object whose theory loses several of linear algebra's clean theorems (existence of a basis, well-defined dimension).

> [!tip] Algebraic Closure and the Fundamental Theorem of Algebra *(from Algebra)*
> $\mathbb{C}$ is the **algebraic closure** of $\mathbb{R}$: every non-constant polynomial in $\mathbb{C}[x]$ has a root. This is the property that delivers the existence of eigenvalues for complex operators (see [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]]) and the cleanest version of the spectral theorem. Real operators do not generally have real eigenvalues; complex operators always do.

> [!tip] Finite Fields and Coding Theory *(from Number Theory and Computer Science)*
> The finite fields $\mathbb{F}_q$ with $q = p^n$ elements are the alphabets of error-correcting codes (Reed-Solomon, BCH), the supports of cryptographic schemes (elliptic curve cryptography over $\mathbb{F}_p$), and the algebraic ground of finite geometry. The linear algebra is the same — bases, dimension, linear maps — but over a finite scalar set, with concrete algorithmic consequences.

> [!tip] Field Extension and Galois Theory *(from Algebra)*
> An inclusion of fields $\mathbb{F} \subset \mathbb{K}$ makes $\mathbb{K}$ a vector space over $\mathbb{F}$, whose dimension $[\mathbb{K} : \mathbb{F}]$ is the **degree** of the extension. **Galois theory** is the study of these extensions through their automorphism groups, and it is built entirely on linear algebra over the smaller field together with [[Def - Group|group]] theory; the tower law $[L : F] = [L : K][K : F]$ is a special case of dimension multiplicativity for tensor products of vector spaces.

---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Subring"
  - "Def - Unit and Field"
tags: [algebra, ring-theory]
---

# Notation

Let $(R, +, \cdot, 0_R, 1_R)$ be a [[Def - Ring|ring]] — commutative and unital, by the standing convention. The symbol $X$ is a **formal symbol** (an indeterminate), not an element of $R$ and not a variable ranging over $R$. A polynomial over $R$ is written $f = a_0 + a_1 X + \cdots + a_n X^n$ with **coefficients** $a_i \in R$. The set of all polynomials in $X$ over $R$ is the **polynomial ring** $R[X]$. Its enlargements are the **formal power series ring** $R[[X]]$ (sums with no upper limit) and the **Laurent polynomial ring** $R[X, X^{-1}]$ (finitely many terms, but exponents allowed to be negative integers). The **degree** of $f$ is $\deg f$; the zero polynomial is conventionally assigned degree $-\infty$ (or left undefined). See [[Rings I — §2.1–2.2]] for the full registry.

---

# Axiom Motivation

We have a [[Def - Ring|ring]] $R$ and we want to build a *new, larger* ring out of it by adjoining one fresh element $X$ that obeys no relations except those forced by the ring axioms. The motive is twofold. First, polynomials are the universal way to make a ring bigger in a controlled fashion: $R[X]$ is the ring you get by throwing in a single "free" element, and iterating or quotienting this construction produces an enormous range of [[Def - Ring|rings]] — number rings like $\mathbb{Z}[i]$, function rings, the coordinate rings of algebraic geometry. Second, polynomials are the objects whose *factorization* generalizes the arithmetic of $\mathbb{Z}$: divisibility, primes, the Euclidean algorithm all have polynomial analogues, and $R[X]$ is where that analogy is studied.

The single most important design decision — and the one a careful definition must get right — is this: **a polynomial is its sequence of coefficients, not the function it induces.** It is tempting to define a polynomial as a function $R \to R$ of a certain shape. Resist this. The desideratum is that two polynomials are equal exactly when they have the same coefficients, term by term. Why not identify a polynomial with its function? Because over some rings, *different* coefficient sequences induce the *same* function, and we want to keep them distinct. The decisive example: over $R = \mathbb{Z}/2\mathbb{Z}$, the polynomial $f = X^2 + X$ has coefficient sequence $(0, 1, 1, 0, 0, \ldots)$, which is not the all-zero sequence, so $f$ is **not** the zero polynomial. Yet as a function it is identically zero: $f(0) = 0 + 0 = 0$ and $f(1) = 1 + 1 = 0$ in $\mathbb{Z}/2\mathbb{Z}$. If we defined polynomials as functions, $X^2 + X$ and $0$ would be the same object over $\mathbb{Z}/2\mathbb{Z}$ — and then $\deg$ would be ill-defined, $R[X]$ would be finite over a finite $R$, and the entire factorization theory would collapse. So the formal-symbol definition is *forced* by the demand that the coefficient data be faithfully recorded. The symbols $X^i$ are bookkeeping slots; a polynomial is a finite list of ring elements parked in those slots.

With "polynomial = coefficient sequence" fixed, the operations are forced too. Addition must be coefficient-wise, $(\sum a_i X^i) + (\sum b_i X^i) = \sum (a_i + b_i) X^i$ — anything else would not make the constant polynomials a copy of $R$. Multiplication is forced by a single non-negotiable demand: $X$ must be a genuine ring element, so multiplication must be distributive and associative, and $X^i \cdot X^j$ must equal $X^{i+j}$ (the exponent law is what "$X$ is one element multiplied repeatedly" *means*). Expanding $(\sum a_i X^i)(\sum b_j X^j)$ by distributivity and collecting the $X^k$ terms then leaves no freedom: the coefficient of $X^k$ must be the **[[Def - Convolution|convolution]]** $\sum_{i+j=k} a_i b_j$. There is genuinely only one ring structure on coefficient sequences for which $X$ behaves like an adjoined element, and that structure is $R[X]$.

Three further notions ride along, each answering a natural question about a polynomial. **Degree** answers "how big is $f$": it is the largest $m$ with $a_m \neq 0$, the index of the top non-zero slot. We must exclude the zero polynomial from this — it has no non-zero coefficient at all — which is why $\deg 0$ is set to $-\infty$ or left undefined; this is not pedantry, it is what keeps the rule $\deg(fg) = \deg f + \deg g$ honest. **Monic** answers "is the leading coefficient as simple as possible": $f$ of degree $m$ is monic if $a_m = 1_R$. Monic polynomials matter because you can always divide by them — the leading coefficient, being a unit, never obstructs the [[Thm - Euclidean Algorithm for Polynomials|division algorithm]] — so monic polynomials are the ones that behave like the "positive integers" of $R[X]$.

Finally, two deliberate *weakenings* of the polynomial definition, each of which produces a strictly larger ring. If we **drop the requirement that only finitely many coefficients are non-zero**, allowing $f = a_0 + a_1 X + a_2 X^2 + \cdots$ to run forever, we get the **formal power series ring** $R[[X]]$. The convolution formula for multiplication still makes sense — the coefficient of $X^k$ is the *finite* sum $\sum_{i+j=k} a_i b_j$, even though the series are infinite — so $R[[X]]$ is a genuine ring containing $R[X]$. Crucially, "formal" means we still never ask whether the series converges; it is a sequence of coefficients, manipulated *as if* it were a convergent sum. The strengthening this affords is striking: in $R[[X]]$ the element $1 - X$ is a **unit**, with inverse the geometric series $1 + X + X^2 + X^3 + \cdots$, since $(1 - X)(1 + X + X^2 + \cdots) = 1$. The same element $1 - X$ is **not** a unit in $R[X]$, because any genuine polynomial inverse would have a top term whose product with $-X$ leaves an uncancelled highest-degree term. So enlarging $R[X]$ to $R[[X]]$ creates new units — it makes more elements invertible — exactly the way enlarging $\mathbb{Z}$ to $\mathbb{Q}$ does. If instead we **allow finitely many negative exponents**, $f = \sum_{i \in \mathbb{Z}} a_i X^i$ with all but finitely many $a_i$ zero, we get the **Laurent polynomial ring** $R[X, X^{-1}]$, in which $X$ itself becomes a unit with inverse $X^{-1}$. (One must allow only finitely many negative exponents: with infinitely many on both sides, the convolution $\sum_{i+j=k} a_i b_j$ would be an infinite sum of ring elements, which is undefined.) Each weakening adjoins inverses the polynomial ring lacked.

In summary: a polynomial is a finite coefficient sequence over $R$, kept formally distinct from its induced function so that the coefficient data is never lost; addition is coefficient-wise and multiplication is convolution, both forced by demanding $X$ be a real adjoined ring element; degree and monic measure the top coefficient; and dropping finiteness or allowing negative exponents produces the larger rings $R[[X]]$ and $R[X, X^{-1}]$, each manufacturing units that $R[X]$ does not have.

---

# The Definition

Let $(R, +, \cdot, 0_R, 1_R)$ be a [[Def - Ring|ring]].

**Polynomial.** A **polynomial** with coefficients in $R$ is a formal expression
$$f = a_0 + a_1 X + a_2 X^2 + \cdots + a_n X^n, \qquad a_i \in R,$$
where the $X^i$ are formal symbols. Equivalently, $f$ is a sequence $(a_0, a_1, a_2, \ldots)$ of elements of $R$ with only finitely many $a_i$ non-zero. Two polynomials are equal precisely when their coefficient sequences agree term by term; in particular $f$ and $f + 0_R \cdot X^{n+1}$ denote the same polynomial. A polynomial induces a function $R \to R$ by substitution, but **a polynomial is not identified with the function it induces** — distinct polynomials may induce the same function.

**Degree.** The **degree** $\deg f$ of a non-zero polynomial $f$ is the largest $m$ such that $a_m \neq 0_R$. The coefficient $a_m$ is then the **leading coefficient**. The zero polynomial is assigned degree $-\infty$ (or its degree is left undefined).

**Monic.** A polynomial $f$ of degree $m$ is **monic** if its leading coefficient is $1_R$, that is $a_m = 1_R$.

**Polynomial ring.** The **polynomial ring** $R[X]$ is the set of all polynomials with coefficients in $R$, made into a ring by
$$\Big(\sum_i a_i X^i\Big) + \Big(\sum_i b_i X^i\Big) = \sum_i (a_i + b_i) X^i, \qquad \Big(\sum_i a_i X^i\Big) \cdot \Big(\sum_j b_j X^j\Big) = \sum_k \Big(\sum_{i + j = k} a_i b_j\Big) X^k.$$
The zero is the zero polynomial and the identity is the constant polynomial $1_R$. The constant polynomials form a [[Def - Subring|subring]] isomorphic to $R$, and $R$ is identified with this [[Def - Subring|subring]].

**Formal power series ring.** The **formal power series ring** $R[[X]]$ is the set of expressions $f = a_0 + a_1 X + a_2 X^2 + \cdots$ with $a_i \in R$ and **no** restriction to finitely many non-zero coefficients. Addition and multiplication are given by the same formulas as for $R[X]$ — the convolution $\sum_{i+j=k} a_i b_j$ remains a finite sum for each $k$. A power series is a formal object; convergence is never asked. There is an inclusion $R[X] \leq R[[X]]$ of rings.

**Laurent polynomial ring.** The **Laurent polynomial ring** $R[X, X^{-1}]$ is the set of expressions $f = \sum_{i \in \mathbb{Z}} a_i X^i$ with $a_i \in R$ and only **finitely many** $a_i$ non-zero (negative exponents now permitted), with addition and multiplication the obvious extensions of the polynomial formulas. There is an inclusion $R[X] \leq R[X, X^{-1}]$, and in $R[X, X^{-1}]$ the indeterminate $X$ is a unit with inverse $X^{-1}$.

---

# Categorical Definition

The polynomial ring $R[X]$ is characterized by a **universal property**, and this is the cleanest way to say what "adjoining a free element" precisely means. A universal property pins down an object by the maps into or out of it. The statement: $R[X]$ together with the inclusion $R \hookrightarrow R[X]$ and the chosen element $X \in R[X]$ is the **free commutative $R$-algebra on one generator**. Concretely, for *any* commutative ring $S$ equipped with a [[Def - Ring Homomorphism|ring homomorphism]] $\varphi : R \to S$ and *any* chosen element $s \in S$, there is a **unique** ring homomorphism $\Phi : R[X] \to S$ extending $\varphi$ and sending $X \mapsto s$. That homomorphism is exactly *evaluation at $s$*: it sends $\sum a_i X^i$ to $\sum \varphi(a_i) s^i$.

The reason this captures "$X$ obeys no relations except those forced by the ring axioms" is the *uniqueness* and *unconstrained existence* of $\Phi$: you may send $X$ to **any** element $s$ of **any** ring, with no compatibility condition to check, and the map is always well-defined. If $X$ satisfied some hidden relation — say $X^2 = 1_R$ — then $X$ could only be sent to elements $s$ with $s^2 = 1_S$, and the existence half would fail. Freedom of $X$ is precisely the absence of such constraints. This universal property is also the rigorous content of the slogan "a polynomial is its coefficients, not its function": the *function* induced by $f$ is the single homomorphism $\Phi$ for the particular choice $S = R$, $\varphi = \mathrm{id}$; the *polynomial itself* is the element of the universal object $R[X]$, and the universal object remembers strictly more than any one evaluation.

---

# Relate to Other Fields / Compression

The construction $R \mapsto R[X]$ is **the free functor adjoining one generator**, and it specializes a single idea visible all over algebra: from a structure, build the free structure on one extra element. The free [[Def - Group|group]] on one generator is $\mathbb{Z}$; the free commutative monoid on one generator is $\mathbb{N}$; the free commutative $R$-algebra on one generator is $R[X]$. In every case "free" means "no relations beyond those the axioms force", made precise by a universal property. Iterating gives $R[X_1, \ldots, X_n]$, the free commutative $R$-algebra on $n$ generators, and quotienting *that* by an [[Def - Ideal|ideal]] of relations produces, in principle, every finitely generated commutative ring — which is why polynomial rings are the universal raw material of commutative algebra and algebraic geometry.

The trio $R[X] \subseteq R[[X]] \subseteq$ (Laurent and beyond) is the algebraic mirror of an analytic hierarchy. A *power series* is, analytically, a function defined by an infinite sum near a point; the **formal** power series ring $R[[X]]$ keeps the algebra of such expressions — coefficient-wise addition, convolution multiplication — while *deleting the analysis*, the questions of radius of convergence and summation. It is "Taylor coefficients without the Taylor's theorem". The passage from $R[X]$ to $R[[X]]$ is also a faithful analogue of completion: just as the reals $\mathbb{R}$ complete the rationals $\mathbb{Q}$ and thereby acquire limits that $\mathbb{Q}$ lacked, $R[[X]]$ completes $R[X]$ (in the $X$-adic sense) and thereby acquires the inverse $1 + X + X^2 + \cdots$ of $1 - X$ that $R[X]$ lacked. Enlarging a ring to gain inverses is the same story whether the ring is $\mathbb{Z}$, $\mathbb{Q}$, $R[X]$, or $R[[X]]$.

---

# Examples / Corollaries

**Is an instance: $\mathbb{Z}[X]$, $\mathbb{Q}[X]$, $\mathbb{R}[X]$.** Polynomials with integer, rational, or real coefficients form polynomial rings. In $\mathbb{R}[X]$ the element $X^2 + 1$ has degree $2$ and is monic. These are the everyday polynomial rings; note $\mathbb{Z}[X]$ is a polynomial ring over a ring that is not a [[Def - Unit and Field|field]], and it behaves quite differently from $\mathbb{Q}[X]$ — for instance the [[Thm - Euclidean Algorithm for Polynomials|division algorithm]] works freely in $\mathbb{Q}[X]$ but is obstructed in $\mathbb{Z}[X]$ unless one divides by a monic polynomial.

**Is an instance, the load-bearing one: $X^2 + X$ in $(\mathbb{Z}/2\mathbb{Z})[X]$.** Over the two-element field $\mathbb{Z}/2\mathbb{Z}$, the polynomial $f = X^2 + X$ has coefficient sequence $(0, 1, 1, 0, \ldots)$, so it **is a non-zero polynomial of degree $2$**. But the *function* it induces is identically zero: $f(0) = 0^2 + 0 = 0$ and $f(1) = 1^2 + 1 = 1 + 1 = 0$ in $\mathbb{Z}/2\mathbb{Z}$. So here is a non-zero polynomial inducing the zero function — concrete proof that a polynomial cannot be identified with its induced function, and the reason the definition insists on formal symbols. *Calibration check:* if you see why $f \neq 0$ as a polynomial yet $f = 0$ as a function, you have understood the central design decision of this page.

**Is an instance: $X$ is a unit in $R[X, X^{-1}]$ but not in $R[X]$.** In the Laurent polynomial ring $R[X, X^{-1}]$ the indeterminate $X$ has the honest inverse $X^{-1}$, since $X \cdot X^{-1} = X^0 = 1_R$. In the plain polynomial ring $R[X]$, however, $X$ is not a unit: any product $X \cdot g$ has zero constant term, so it can never equal $1_R$. This is the cleanest illustration of how enlarging the ring (here, permitting negative exponents) creates units.

**Is NOT an instance, as a unit: $1 - X$ in $R[X]$.** For any non-zero ring $R$, the polynomial $1 - X$ is **not a unit** in $R[X]$. Suppose $g = b_0 + b_1 X + \cdots + b_n X^n$ with $b_n \neq 0$ were an inverse. Then
$$(1 - X) g = b_0 + (b_1 - b_0)X + (b_2 - b_1)X^2 + \cdots + (b_n - b_{n-1})X^n - b_n X^{n+1},$$
whose coefficient of $X^{n+1}$ is $-b_n \neq 0$. So $(1 - X)g$ has degree $n + 1 \geq 1$ and cannot equal the constant $1_R$. Hence $1 - X$ has no inverse in $R[X]$.

**Is an instance, as a unit: $1 - X$ in $R[[X]]$.** The very same element $1 - X$ **is a unit** in the formal power series ring $R[[X]]$, with inverse the geometric series:
$$(1 - X)\,(1 + X + X^2 + X^3 + \cdots) = 1.$$
Multiplying out, every $X^k$ for $k \geq 1$ appears once with coefficient $+1$ (from $1 \cdot X^k$) and once with coefficient $-1$ (from $-X \cdot X^{k-1}$), so all terms above the constant cancel and the product is $1$. The contrast with the previous example is the headline fact about $R[[X]]$: the obstruction in $R[X]$ was that a *finite* polynomial inverse leaves an uncancelled top term, and allowing infinitely many coefficients removes "the top" entirely, so the cancellation can run forever. *Calibration check:* an element $a_0 + a_1 X + \cdots \in R[[X]]$ is a unit precisely when its constant term $a_0$ is a unit in $R$ — verify that $1 - X$, with constant term $1_R$, satisfies this, while $X$, with constant term $0_R$, does not.

**Corollary (degree under multiplication, over an integral domain).** If $R$ has no zero divisors and $f, g \in R[X]$ are non-zero, then $\deg(fg) = \deg f + \deg g$. The leading coefficient of $fg$ is the product of the leading coefficients of $f$ and $g$, and that product is non-zero precisely because $R$ has no zero divisors. *Calibration check:* over a ring *with* zero divisors this can fail — in $(\mathbb{Z}/4\mathbb{Z})[X]$, $(2X)(2X) = 4X^2 = 0$, so two degree-$1$ polynomials multiply to degree $-\infty$.

**Corollary (the constant polynomials are a copy of $R$).** The map $r \mapsto r$ (the constant polynomial) is an injective [[Def - Ring Homomorphism|ring homomorphism]] $R \to R[X]$, so $R$ is a [[Def - Subring|subring]] of $R[X]$; in particular $0_R$ and $1_R$ are the zero and identity of $R[X]$. This is the precise sense in which "$R[X]$ contains $R$", and it is what makes $R[X]$ an *enlargement* of $R$ rather than an unrelated ring.

---

# Unlocked by This

> [!tip] Euclidean Algorithm for Polynomials *(later this chapter)*
> Once $R[X]$ and the notions of degree and monic are in hand, one can run a division algorithm: dividing any polynomial by a monic polynomial (or by any polynomial, when the coefficients lie in a [[Def - Unit and Field|field]]) yields a quotient and a remainder of strictly smaller degree. See [[Thm - Euclidean Algorithm for Polynomials]].

> [!tip] Quotient Rings and Field Extensions *(from Algebra II)*
> Forming the [[Def - Quotient Ring|quotient]] of $R[X]$ by an [[Def - Ideal|ideal]] generated by a polynomial builds new rings to order: $\mathbb{R}[X]/(X^2 + 1) \cong \mathbb{C}$ constructs the complex numbers, and $\mathbb{Q}[X]/(X^2 - 2) \cong \mathbb{Q}[\sqrt 2]$ constructs a field extension. Polynomial rings are the raw material from which extension fields are manufactured.

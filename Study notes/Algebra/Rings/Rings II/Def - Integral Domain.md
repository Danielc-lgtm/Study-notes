---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Subring"
  - "Def - Unit and Field"
  - "Def - Polynomial Ring"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is a commutative [[Def - Ring|ring]] with additive identity $0_R$ (often just $0$) and multiplicative identity $1_R$ (often just $1$). The word "ring" carries a multiplicative identity, and a **non-zero ring** is one in which $1_R \neq 0_R$ — equivalently, a ring with more than one element. We write $ab$ for the product $a \cdot b$. The ring $\mathbb{Z}/n\mathbb{Z}$ of integers modulo $n$ is written $\mathbb{Z}/n$, and its elements are cosets $a + (n)$. The Gaussian integers are $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\} \leq \mathbb{C}$. The full symbol registry is on [[Rings II — §2.3–2.4]].

---

# Axiom Motivation

The notion of an integral domain is the first move in a programme: rings can be wildly unlike $\mathbb{Z}$, and we want to organise them by *which* of $\mathbb{Z}$'s good behaviours they retain. So begin by asking what we actually use about $\mathbb{Z}$ when we do ordinary arithmetic, and isolate the single most basic property — the one without which everything else collapses.

Here is the property. In $\mathbb{Z}$, if you multiply two non-zero numbers you get a non-zero number. You never accidentally hit zero. This sounds too obvious to be worth a definition, until you meet a ring where it fails. Take $\mathbb{Z}/6$. The classes $2$ and $3$ are both non-zero, yet $2 \cdot 3 = 6 \equiv 0$. Two perfectly good non-zero elements have conspired to produce zero. The moment this can happen, the arithmetic you learned as a child stops working — and the definition of an integral domain is precisely the axiom that forbids it.

Why is forbidding it the *right* desideratum, rather than some nearby alternative? Because the property we really want is **cancellation**: from $ab = ac$ with $a \neq 0$ we want to conclude $b = c$, just as we would in $\mathbb{Z}$ or $\mathbb{Q}$. Cancellation is what lets us solve equations, define greatest common divisors, talk about unique factorisation, and embed the ring into a field of fractions. Now watch how cancellation and the no-zero-divisor axiom are *the same condition in disguise*. Cancellation says $ab = ac \Rightarrow b = c$ for $a \neq 0$; rewrite $ab = ac$ as $a(b - c) = 0$, and cancellation becomes "$a(b-c) = 0$ with $a \neq 0$ forces $b - c = 0$" — which is exactly "$a$ is not a zero divisor". So the demand "every non-zero element can be cancelled" is *identical* to the demand "there are no zero divisors". We are not choosing an arbitrary axiom; we are choosing the unique condition that resurrects cancellation.

What breaks if we *weaken* the axiom — allow zero divisors? Then cancellation dies, and with it the entire factorisation story. In $\mathbb{Z}/6$ the element $X^2 - 1$ factors as $(X-1)(X+1)$ and also as $(X-5)(X-1)$ since $X+1 = X-5$ there is false — but more concretely, the polynomial $x^2 - x$ over $\mathbb{Z}/6$ has *four* roots $0, 1, 3, 4$ rather than at most two, because $x(x-1) = 0$ no longer forces $x \in \{0,1\}$. A degree-$n$ polynomial over a ring with zero divisors can have more than $n$ roots; the comfortable theorems of algebra evaporate. Worse, you cannot build a field of fractions: the construction of $\mathbb{Q}$ from $\mathbb{Z}$ needs exactly the cancellation step (it appears as the proof that the relation $(a,b) \sim (c,d) \iff ad = bc$ is transitive — see [[Def - Field of Fractions]]), and a zero divisor sabotages it.

What breaks if we *strengthen* the axiom — for instance demand that every non-zero element be a [[Def - Unit and Field|unit]]? Then we have not defined an integral domain at all; we have defined a [[Def - Unit and Field|field]]. That is too strong: $\mathbb{Z}$ itself would be excluded, since $2$ has no integer inverse, and $\mathbb{Z}$ is the motivating example we are trying to capture. The integral domain axiom is the Goldilocks condition: weaken it and cancellation fails, strengthen it to invertibility and you lose $\mathbb{Z}$, $\mathbb{Z}[i]$, and every polynomial ring. An integral domain is exactly "a ring where cancellation works" — no more, no less — and that is the largest class of rings on which ordinary divisibility and factorisation make sense.

One last design choice: why insist the ring be *non-zero*? Because the zero ring $\{0\}$, where $1 = 0$, satisfies the implication "$ab = 0 \Rightarrow a = 0$ or $b = 0$" vacuously (everything is $0$). Calling it an integral domain would be harmless logically but would force annoying exceptions into every later theorem ("every integral domain except the zero ring..."). Excluding it by fiat — demanding $1 \neq 0$ — keeps the theory clean, exactly as one excludes $1$ from the primes.

---

# The Definition

A **non-zero ring** is a [[Def - Ring|ring]] $R$ in which $1_R \neq 0_R$.

A non-zero (commutative) ring $R$ is an **integral domain** if it has no zero divisors: for all $a, b \in R$,
$$a \cdot b = 0_R \quad \Longrightarrow \quad a = 0_R \ \text{ or } \ b = 0_R.$$

The elements forbidden by this axiom have a name of their own.

**Zero divisor.** An element $x \in R$ is a **zero divisor** if $x \neq 0_R$ and there exists $y \in R$ with $y \neq 0_R$ such that
$$x \cdot y = 0_R.$$
Note the convention: $0_R$ itself is *not* counted as a zero divisor, even though $0_R \cdot y = 0_R$ for every $y$. With this convention, an integral domain is precisely a non-zero ring **containing no zero divisors at all**.

**Equivalent formulation (cancellation).** A non-zero ring $R$ is an integral domain if and only if the **cancellation law** holds: for all $a, b, c \in R$ with $a \neq 0_R$,
$$ab = ac \quad \Longrightarrow \quad b = c.$$
The equivalence is immediate — $ab = ac$ rearranges to $a(b-c) = 0_R$, and "no zero divisors" turns this into $b - c = 0_R$; conversely, $xy = 0_R = x \cdot 0_R$ with $x \neq 0_R$ cancels to $y = 0_R$.

---

# Relate to Other Fields / Compression

An integral domain is the multiplicative analogue of a structure every reader already knows from group theory: a set with an operation that has **no proper zero divisors** is, on the non-zero elements, the next best thing to a group. Precisely, $R$ is an integral domain exactly when the set $R \setminus \{0\}$ is closed under multiplication and forms a *cancellative commutative monoid* — a monoid (associative, with identity $1$) in which cancellation holds. A field goes one step further and makes $R \setminus \{0\}$ an actual abelian group. So the chain "integral domain $\to$ field" is the multiplicative shadow of the chain "cancellative monoid $\to$ group", and the [[Def - Field of Fractions|field of fractions]] construction is the exact ring-theoretic analogue of the group-completion (Grothendieck) construction that turns a cancellative commutative monoid into a group.

There is also a clean order-theoretic and topological reading. A commutative ring $R$ is an integral domain if and only if its zero ideal $(0)$ is a [[Def - Prime and Maximal Ideal|prime ideal]] — because $R/(0) \cong R$, and an ideal is prime exactly when the quotient is an integral domain. In algebraic geometry this is the statement that the affine scheme $\operatorname{Spec} R$ is *irreducible and reduced* — geometrically, an integral domain is the coordinate ring of a space that does not split into pieces and has no infinitesimal fuzz. The single condition "$ab = 0 \Rightarrow a = 0$ or $b = 0$" is thus simultaneously an algebraic condition (cancellation), an ideal-theoretic condition ($(0)$ is prime), and a geometric condition (the spectrum is an integral variety) — the same fact wearing three coats.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}$.** The integers are the prototype: a product of two non-zero integers is non-zero. Indeed $\mathbb{Z}$ is the integral domain *par excellence*, and the whole point of the definition is to extract what makes $\mathbb{Z}$ tick so we can find it elsewhere. It is not a field — $2$ has no inverse — which shows the class of integral domains is strictly larger than the class of fields.

**Is an instance — every field.** Any [[Def - Unit and Field|field]] $F$ is an integral domain. Suppose $ab = 0$ with $b \neq 0$; then $b$ is a unit, so $a = a(bb^{-1}) = (ab)b^{-1} = 0 \cdot b^{-1} = 0$. Symmetrically, $a \neq 0$ forces $b = 0$. So $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, and every finite field $\mathbb{Z}/p$ (with $p$ prime) are integral domains. This is the implication "field $\Rightarrow$ integral domain"; the converse fails ($\mathbb{Z}$), but it *does* hold under one extra hypothesis — see the corollary below.

**Is an instance — every subring of an integral domain.** If $S \leq R$ is a [[Def - Subring|subring]] of an integral domain $R$, then $S$ is an integral domain: a zero divisor of $S$ would be two non-zero elements of $S$ — hence of $R$ — multiplying to $0$, contradicting that $R$ has none. (One must also note $S$ is non-zero, which holds because a subring shares the identity $1_R \neq 0_R$.) This single observation harvests a flood of examples. Since $\mathbb{C}$ is a field and therefore an integral domain, *every* subring of $\mathbb{C}$ is an integral domain — in particular $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, the Gaussian integers $\mathbb{Z}[i]$, the ring $\mathbb{Z}[\sqrt{2}]$, and so on. These are exactly the rings of number theory, the setting in which factorisation makes sense.

**Is an instance — $R[X]$ when $R$ is an integral domain.** If $R$ is an integral domain then so is the [[Def - Polynomial Ring|polynomial ring]] $R[X]$. The argument is a degree count: take non-zero $f = a_0 + \cdots + a_n X^n$ and $g = b_0 + \cdots + b_m X^m$ with leading coefficients $a_n \neq 0$ and $b_m \neq 0$. The coefficient of $X^{n+m}$ in the product $fg$ is exactly $a_n b_m$, and since $R$ has no zero divisors, $a_n b_m \neq 0$. So $fg$ has a non-zero coefficient and is itself non-zero. Note where the hypothesis is *used*: if $R$ had zero divisors the leading coefficients could cancel, $\deg(fg)$ could drop, and the product could even vanish. Iterating, $R[X_1, \dots, X_k]$ is an integral domain whenever $R$ is — so $\mathbb{Z}[X]$, $\mathbb{Q}[X, Y]$, and all multivariate polynomial rings over a field are integral domains.

**Is NOT an instance — $\mathbb{Z}/6$.** The ring $\mathbb{Z}/6$ is non-zero but is not an integral domain: $2 \neq 0$ and $3 \neq 0$, yet $2 \cdot 3 = 6 \equiv 0$. Both $2$ and $3$ are zero divisors. More generally $\mathbb{Z}/n$ is an integral domain if and only if $n$ is prime: if $n = pq$ is a non-trivial factorisation then $p$ and $q$ are non-zero zero divisors, while if $n$ is prime then $\mathbb{Z}/n$ is a field and hence a domain. This example probes the axiom directly — it is the canonical witness that "no zero divisors" is a genuine restriction.

**Is NOT an instance — a non-trivial product ring $R \times S$.** For any two non-zero rings $R$ and $S$, the product $R \times S$ (with coordinatewise operations) is non-zero but is *never* an integral domain. The elements $(1_R, 0_S)$ and $(0_R, 1_S)$ are both non-zero, yet their product is $(1_R \cdot 0_R, \ 0_S \cdot 1_S) = (0_R, 0_S) = 0$. So $(1_R, 0_S)$ is a zero divisor. This is worth remembering as a slogan: **products break integral domains**. It also explains the algebraic-geometry picture — a product ring corresponds to a disconnected space, and an integral domain must be "irreducible", a single piece.

**Corollary — a finite integral domain is a field.** If $R$ is a *finite* integral domain, then $R$ is a field; see [[Thm - Finite Integral Domains are Fields]]. The idea is that for fixed non-zero $a$, the multiplication map $x \mapsto ax$ is injective (its kernel is trivial precisely because there are no zero divisors), and an injective self-map of a finite set is surjective, so some $x$ satisfies $ax = 1$. Finiteness converts "cancellable" into "invertible". This is the promised partial converse to "field $\Rightarrow$ integral domain": for *finite* rings the two notions coincide.

**Calibration check.** Verify that $\mathbb{Z}/4$ is *not* an integral domain (find the zero divisor) but $\mathbb{Z}/5$ *is*; that the cancellation law $ab = ac, a \neq 0 \Rightarrow b = c$ fails in $\mathbb{Z}/6$ by exhibiting an explicit failure (try $a = 2$); and that in any integral domain the only solutions of $x^2 = x$ are $x = 0$ and $x = 1$ (factor as $x(x-1) = 0$). If you can also explain why the zero ring is excluded by the words "non-zero ring", you have understood every clause of the definition.

---

# Unlocked by This

> [!tip] Field of Fractions *(from this topic)*
> Being an integral domain is exactly the hypothesis needed to build the [[Def - Field of Fractions|field of fractions]] — the cancellation law is what makes the defining equivalence relation transitive. Every integral domain embeds into a field, so domains may be studied with field techniques.

> [!tip] Prime Ideals *(from this topic)*
> An ideal $P$ of $R$ is a [[Def - Prime and Maximal Ideal|prime ideal]] precisely when the quotient $R/P$ is an integral domain. The integral-domain condition is thus the local building block of the entire theory of prime ideals and the spectrum of a ring.

> [!tip] Euclidean Domains, PIDs, UFDs *(from Rings II–III)*
> Integral domains are the base of a refinement tower. A [[Def - Unique Factorization Domain|unique factorization domain]] is a domain with well-behaved factorisation; a [[Def - Principal Ideal Domain|principal ideal domain]] is a domain whose ideals are all principal; a [[Def - Euclidean Domain|Euclidean domain]] is a domain carrying a division algorithm. Each strengthens "integral domain" with one more property of $\mathbb{Z}$.

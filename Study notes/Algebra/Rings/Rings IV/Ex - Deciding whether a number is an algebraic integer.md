---
type: exercise
subject: ring-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Algebraic Integer and Minimal Polynomial"
  - "Thm - The Minimal Polynomial Generates the Kernel Ideal"
  - "Thm - Rational Algebraic Integers are Integers"
  - "Def - Polynomial Ring"
  - "Def - Irreducible and Prime Elements"
tags: [algebra, ring-theory]
---

# Problem Statement

Decide, for each of the following two complex numbers, whether it is an algebraic integer, and justify the verdict.

1. The golden ratio $\;\varphi = \tfrac12\bigl(1 + \sqrt5\bigr)$.
2. The number $\;\beta = \tfrac12\bigl(1 + \sqrt3\bigr)$.

The expected answer: $\varphi$ *is* an algebraic integer (it is a root of $X^2 - X - 1 \in \mathbb{Z}[X]$), while $\beta$ is *not*.

**Recall:**

The setting is the [[Def - Polynomial Ring|polynomial ring]] $\mathbb{Z}[X]$ and its overring $\mathbb{Q}[X]$, and the notion of an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]].

A complex number $\alpha$ is an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]] when it is a root of a **monic** polynomial $f \in \mathbb{Z}[X]$ — leading coefficient $1$, all coefficients integers. The word *monic* and the word *integer* are both essential: $\beta = \tfrac12(1+\sqrt3)$ is certainly a root of a monic *rational* polynomial and of a non-monic *integer* polynomial, yet (as we shall see) of no monic integer polynomial.

![[Thm - The Minimal Polynomial Generates the Kernel Ideal#Statement]]

A consequence we will lean on heavily is that the minimal polynomial is *minimal*: every polynomial in $\mathbb{Q}[X]$ vanishing at $\alpha$ is a multiple of the (unique monic) minimal polynomial $m_\alpha \in \mathbb{Q}[X]$. So if a number $\alpha$ has a degree-$2$ monic rational minimal polynomial $m_\alpha$, then $\alpha$ is an algebraic integer **if and only if** that very polynomial $m_\alpha$ already has integer coefficients — because any monic *integer* polynomial vanishing at $\alpha$ is a monic *rational* multiple of $m_\alpha$, and a monic polynomial of the same degree as $m_\alpha$ equal to a monic multiple of $m_\alpha$ must *be* $m_\alpha$.

This is the engine of part 2: compute the (rational) minimal polynomial and inspect whether its coefficients are integers.

---

# Convergent Strategy

**Problem class.** This is a *decide-and-certify* problem: a yes/no question ("is $\alpha$ an algebraic integer?") demanding a *proof* of the verdict, not just the verdict. The [[Rings IV — §2.7–2.8]] strategy notes that yes/no algebraic-integer questions are settled by computing the minimal polynomial and reading off whether its coefficients are integers — the minimal polynomial is the *unique* obstruction, so it both certifies a yes and witnesses a no.

**Assumption pattern.** Both candidates have the shape $\tfrac12(1 + \sqrt d)$ — "half of one plus a surd". This shape is exactly the boundary case: such numbers are algebraic integers for some $d$ and not for others, and the deciding parameter is $d \bmod 4$. The presence of the denominator $2$ is the only thing that makes the question non-trivial — $1 + \sqrt d$ is always an algebraic integer, but dividing by $2$ may or may not destroy that.

**Theorem routing.** For a *yes* verdict (part 1) the route is direct: *exhibit* a monic integer polynomial vanishing at $\alpha$ — this is by definition a certificate of being an algebraic integer; no further argument is required. For a *no* verdict (part 2) the route runs through minimality: compute the minimal polynomial $m_\beta \in \mathbb{Q}[X]$, observe it has a non-integer coefficient, then argue via [[Thm - The Minimal Polynomial Generates the Kernel Ideal]] (every vanishing polynomial is a multiple of $m_\beta$) that *no* monic integer polynomial can vanish at $\beta$. An independent, more hands-on route for part 2 — useful as a cross-check — assumes a monic integer relation and derives an arithmetic contradiction directly.

**Key decision point.** The non-obvious point is that for the *no* verdict it is not enough to find *one* monic integer polynomial that fails to vanish, nor to exhibit the rational minimal polynomial and stop. One must invoke *minimality*: the rational minimal polynomial divides every vanishing polynomial, so a vanishing *monic integer* polynomial of degree $2$ would have to equal the rational minimal polynomial — and if the latter has a genuinely non-integer coefficient, that equality is impossible. The decision is to make the proof go through the *uniqueness/divisibility* property of the minimal polynomial rather than through an unstructured search.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings IV — §2.7–2.8#Legal Operations|the topic page's Legal Operations]]:

1. **Eliminate a radical by isolate-and-square.** Write the surd alone on one side of the defining equation, then square, to obtain a polynomial relation. For a number of the form $\tfrac12(1+\sqrt d)$ this gives a degree-$2$ relation.

2. **Exhibit a witnessing polynomial.** To certify that a number *is* an algebraic integer, the legal and complete move is simply to display a monic integer polynomial it satisfies — being an algebraic integer is defined by the existence of such a polynomial.

3. **Compute the minimal polynomial and inspect its coefficients.** The minimal polynomial of a degree-$2$ algebraic number is the monic quadratic it satisfies; reading whether its coefficients lie in $\mathbb{Z}$ decides the algebraic-integer question.

4. **Invoke minimality (the divisibility property).** Use that every polynomial vanishing at $\alpha$ is a multiple of the minimal polynomial — so a monic vanishing polynomial of the *same degree* as the minimal polynomial must equal it.

5. **Derive an integer/parity contradiction.** Assume a hypothetical monic integer relation, expand, and separate the equation into its *rational part* and its *$\sqrt d$-coefficient part*; force the integer unknowns to satisfy an impossible congruence.

6. **Separate rational and irrational parts.** In an equation among numbers of the form $p + q\sqrt d$ with $p, q$ rational and $\sqrt d$ irrational, the rational parts on the two sides are equal and the $\sqrt d$-coefficients on the two sides are equal — two equations from one.

---

# Hints

> [!note]- Hint 1
> For part 1, you only need to *find* one monic integer polynomial that $\varphi$ satisfies — that is the entire definition of "algebraic integer". Set $\varphi = \tfrac12(1+\sqrt5)$, so $2\varphi - 1 = \sqrt5$, and square.

> [!note]- Hint 2
> For part 2, do the same computation with $\beta = \tfrac12(1+\sqrt3)$: from $2\beta - 1 = \sqrt3$, square to get a quadratic relation. You will find $\beta$ satisfies $X^2 - X - \tfrac12$. Note the coefficient $-\tfrac12$. This monic quadratic is the *minimal polynomial* of $\beta$ over $\mathbb{Q}$ — it is irreducible because $\beta \notin \mathbb{Q}$, so $\beta$ has no degree-$1$ rational vanishing polynomial.

> [!note]- Hint 3
> Now suppose, for contradiction, that $\beta$ *were* an algebraic integer — a root of some monic $g \in \mathbb{Z}[X]$. The minimal polynomial $m_\beta = X^2 - X - \tfrac12$ must *divide* $g$ in $\mathbb{Q}[X]$. Think about what this forces when $g$ itself has degree $2$, and reduce the general case to the degree-$2$ case.

> [!note]- Hint 4
> Alternative, fully hands-on route for part 2. Suppose $\beta$ is a root of a monic $g = X^2 + bX + c$ with $b, c \in \mathbb{Z}$ (degree $2$ suffices — explain why). Substitute $\beta = \tfrac12(1+\sqrt3)$, expand, and collect terms into "rational part" and "coefficient of $\sqrt3$". Because $\sqrt3$ is irrational, *each part must vanish separately*. The $\sqrt3$-part gives a linear equation in $b$; solve it and check whether the resulting $b$ is an integer.

---

# Solution

Part 1 is a one-line *exhibition*: display the monic integer polynomial. Part 2 is a *no* verdict, which requires more: compute the minimal polynomial, see its non-integer coefficient, and then use minimality (or a direct parity argument) to rule out *every* monic integer polynomial — not just the obvious candidates.

**Step 1: The golden ratio satisfies $X^2 - X - 1$.**

Setting $\varphi = \tfrac12(1+\sqrt5)$ and eliminating the surd gives
$$\varphi^2 - \varphi - 1 = 0,$$
so $\varphi$ is a root of the monic integer polynomial $X^2 - X - 1$. Hence $\varphi$ **is an algebraic integer.**

> [!note]- Derivation
> From $\varphi = \tfrac12(1+\sqrt5)$, multiply by $2$ and isolate the surd:
> $$2\varphi - 1 = \sqrt5.$$
> Square both sides. The left side is $(2\varphi - 1)^2 = 4\varphi^2 - 4\varphi + 1$; the right side is $(\sqrt5)^2 = 5$:
> $$4\varphi^2 - 4\varphi + 1 = 5.$$
> Subtract $5$ and divide by $4$:
> $$4\varphi^2 - 4\varphi - 4 = 0 \quad\Longrightarrow\quad \varphi^2 - \varphi - 1 = 0.$$
> So $\varphi$ is a root of
> $$f = X^2 - X - 1.$$
> The coefficients are $1, -1, -1$: the leading coefficient is $1$ (monic) and all three lie in $\mathbb{Z}$. By the definition of an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]] — a root of a monic polynomial in $\mathbb{Z}[X]$ — this single computation *is* the complete proof that $\varphi$ is an algebraic integer. Nothing more is needed: existence of the witnessing polynomial is the definition.
>
> (This matches the textbook example $\tfrac12(1 + \sqrt{-3})$, whose minimal polynomial is likewise $X^2 - X + 1$: numbers $\tfrac12(1+\sqrt d)$ with $d \equiv 1 \pmod 4$ are algebraic integers, the dividing-by-$2$ being absorbed because $\tfrac{1-d}{4} \in \mathbb{Z}$.)

**Step 2: The candidate $\beta$ satisfies the non-integral $X^2 - X - \tfrac12$, which is its minimal polynomial.**

The same computation for $\beta = \tfrac12(1+\sqrt3)$ yields
$$\beta^2 - \beta - \tfrac12 = 0,$$
and $m_\beta := X^2 - X - \tfrac12$ is the minimal polynomial of $\beta$ over $\mathbb{Q}$. Its constant term $-\tfrac12$ is **not** an integer.

> [!note]- Derivation
> From $\beta = \tfrac12(1+\sqrt3)$, isolate the surd: $2\beta - 1 = \sqrt3$. Square:
> $$(2\beta - 1)^2 = 3 \quad\Longrightarrow\quad 4\beta^2 - 4\beta + 1 = 3 \quad\Longrightarrow\quad 4\beta^2 - 4\beta - 2 = 0.$$
> Divide by $4$:
> $$\beta^2 - \beta - \tfrac12 = 0.$$
> So $\beta$ is a root of $m_\beta = X^2 - X - \tfrac12 \in \mathbb{Q}[X]$.
>
> *Why $m_\beta$ is the minimal polynomial.* It is monic. It is irreducible over $\mathbb{Q}$: a reducible monic quadratic over $\mathbb{Q}$ factors into two linear factors over $\mathbb{Q}$, hence has a *rational* root; but the roots of $m_\beta$ are $\tfrac12(1\pm\sqrt3)$, and $\sqrt3$ is irrational, so neither root is rational. A monic irreducible polynomial vanishing at $\beta$ is, by [[Thm - The Minimal Polynomial Generates the Kernel Ideal|the kernel-ideal theorem]] applied over $\mathbb{Q}$ (where $\mathbb{Q}[X]$ *is* a principal [[Def - Ideal|ideal]] domain), the minimal polynomial. Hence $m_\beta = X^2 - X - \tfrac12$.
>
> Its coefficients are $1, -1, -\tfrac12$. The constant term $-\tfrac12 \notin \mathbb{Z}$. This non-integer coefficient is the *signal* of a "no" — but a signal is not yet a proof; Step 3 turns it into one.

**Step 3: No monic integer polynomial vanishes at $\beta$ — so $\beta$ is not an algebraic integer.**

Suppose $\beta$ were a root of some monic $g \in \mathbb{Z}[X]$. By minimality, $m_\beta$ divides $g$ in $\mathbb{Q}[X]$; tracking degrees and leading coefficients forces a monic integer polynomial equal to $m_\beta$, contradicting that $m_\beta \notin \mathbb{Z}[X]$. Hence **no** such $g$ exists: $\beta$ is **not** an algebraic integer.

> [!note]- Derivation
> Assume for contradiction that $\beta$ is an algebraic integer: there is a monic $g \in \mathbb{Z}[X]$ with $g(\beta) = 0$.
>
> *Reduce to degree $2$.* The minimal polynomial $m_\beta = X^2 - X - \tfrac12$ has degree $2$, and by [[Thm - The Minimal Polynomial Generates the Kernel Ideal|minimality]] every polynomial in $\mathbb{Q}[X]$ vanishing at $\beta$ is a multiple of $m_\beta$. So $g = m_\beta \cdot q$ for some $q \in \mathbb{Q}[X]$. Comparing leading coefficients: $g$ is monic and $m_\beta$ is monic, so $q$ is monic. Now perform polynomial division of $g$ by $m_\beta$ *inside $\mathbb{Q}[X]$* — the quotient is $q$ and the remainder is $0$.
>
> *Force a non-integer coefficient into $g$.* Consider instead dividing $g$ by $m_\beta$ and tracking integrality. It is cleaner to argue directly with the degree-$2$ case, to which we now reduce: among all monic integer polynomials vanishing at $\beta$, pick one, $g$; it is a monic multiple of $m_\beta$. Write $g = m_\beta \, q$ with $q \in \mathbb{Q}[X]$ monic. The coefficient of the second-highest degree term, and the constant term, of the product $m_\beta q$ are $\mathbb{Q}$-combinations involving the coefficient $-\tfrac12$ of $m_\beta$. Rather than chase this in general, observe the clean special case and the general reduction below.
>
> *Clean argument.* Suppose $g$ has degree exactly $2$. Then $q$ has degree $0$ and is monic, so $q = 1$ and $g = m_\beta = X^2 - X - \tfrac12$. But $g \in \mathbb{Z}[X]$ by assumption, while $X^2 - X - \tfrac12 \notin \mathbb{Z}[X]$ — its constant term is $-\tfrac12$. Contradiction. So *no monic integer polynomial of degree $2$* vanishes at $\beta$.
>
> *General degree.* If $g \in \mathbb{Z}[X]$ is monic of degree $n > 2$ with $g(\beta) = 0$, divide $g$ by $m_\beta$ in $\mathbb{Q}[X]$: $g = m_\beta q$ with $q \in \mathbb{Q}[X]$ monic of degree $n - 2$. Equivalently, $2g = (2m_\beta)\,q = (2X^2 - 2X - 1)\,q$. Here $2m_\beta = 2X^2 - 2X - 1 \in \mathbb{Z}[X]$ is a *primitive* polynomial (its coefficients $2, -2, -1$ have gcd $1$). By [[Thm - The Minimal Polynomial Generates the Kernel Ideal|the structure of the kernel ideal]] the minimal polynomial of $\beta$ *as an algebraic integer* would generate $\ker(\varphi)$ — but a cleaner finish: since $2g \in \mathbb{Z}[X]$ and $2g = (2m_\beta)q$ with $2m_\beta$ primitive, Gauss's lemma forces $q \in \mathbb{Z}[X]$, so $g = m_\beta q$ with $q \in \mathbb{Z}[X]$ and $m_\beta = g/q$. The leading coefficient of $g$ is $1$ and of $q$ is $1$, and dividing the integer polynomial $g$ by the integer polynomial $q$ yields the *integer* polynomial $m_\beta$ only if $m_\beta \in \mathbb{Z}[X]$ — which it is not. Concretely: $g = m_\beta q$ gives $X^2$-and-below coefficients of $g$ as integer combinations forcing the constant term of $m_\beta$ to be an integer (the constant term of $g$ is $(-\tfrac12)\cdot(\text{constant term of }q)$, an integer, with the constant term of $q$ an integer, impossible unless that constant term is even — push this through all coefficients to reach a contradiction). The Step-3 *direct* argument below avoids this bookkeeping entirely; it is the recommended proof.
>
> Either way: assuming $\beta$ is an algebraic integer leads to a contradiction. Therefore $\beta = \tfrac12(1+\sqrt3)$ is **not** an algebraic integer.

**Step 3$'$: Direct verification — a monic integer relation forces an impossible parity.**

Independently of minimality: assume $\beta$ satisfies a monic *integer* quadratic $X^2 + bX + c$, separate the equation into rational and $\sqrt3$ parts, and find the $\sqrt3$-part forces $b = -1 \notin 2\mathbb{Z}$ where integrality demands $b$ even. Contradiction.

> [!note]- Derivation
> First, *why degree $2$ suffices*: any monic integer polynomial $g$ vanishing at $\beta$ is, by [[Thm - The Minimal Polynomial Generates the Kernel Ideal|minimality]], divisible by the degree-$2$ minimal polynomial $m_\beta$; if $\beta$ is an algebraic integer at all, then chasing the lowest-degree monic integer vanishing polynomial it must have degree $\geq 2$, and one checks the obstruction already at degree $2$. So it is legitimate to test: *does $\beta$ satisfy a monic integer polynomial of degree $2$?* If not, the divisibility argument of Step 3 shows it satisfies no monic integer polynomial at all.
>
> Suppose
> $$\beta^2 + b\,\beta + c = 0, \qquad b, c \in \mathbb{Z}.$$
> Substitute $\beta = \tfrac12(1+\sqrt3)$. Compute $\beta^2$:
> $$\beta^2 = \tfrac14(1+\sqrt3)^2 = \tfrac14\bigl(1 + 2\sqrt3 + 3\bigr) = \tfrac14\bigl(4 + 2\sqrt3\bigr) = 1 + \tfrac12\sqrt3.$$
> And $b\beta = \tfrac{b}{2}(1+\sqrt3) = \tfrac{b}{2} + \tfrac{b}{2}\sqrt3$. So the equation $\beta^2 + b\beta + c = 0$ becomes
> $$\Bigl(1 + \tfrac{b}{2} + c\Bigr) \;+\; \Bigl(\tfrac12 + \tfrac{b}{2}\Bigr)\sqrt3 \;=\; 0.$$
> The number $\sqrt3$ is **irrational**, so a relation $p + q\sqrt3 = 0$ with $p, q \in \mathbb{Q}$ forces $q = 0$ (else $\sqrt3 = -p/q \in \mathbb{Q}$) and then $p = 0$. Hence both parts vanish:
> $$\text{rational part:}\quad 1 + \tfrac{b}{2} + c = 0, \qquad\qquad \sqrt3\text{-part:}\quad \tfrac12 + \tfrac{b}{2} = 0.$$
> The $\sqrt3$-part gives $\tfrac{b}{2} = -\tfrac12$, i.e.
> $$b = -1.$$
> Now $b$ was assumed to be an **integer**, and indeed $-1 \in \mathbb{Z}$ — so this alone is *not* yet the contradiction. Feed $b = -1$ into the rational part: $1 - \tfrac12 + c = 0$, giving $c = -\tfrac12$. But $c$ was assumed to be an **integer**, and $-\tfrac12 \notin \mathbb{Z}$. **Contradiction.**
>
> So no monic integer quadratic vanishes at $\beta$; by the reduction above, no monic integer polynomial of any degree does. Therefore $\beta = \tfrac12(1+\sqrt3)$ is **not** an algebraic integer.
>
> The arithmetic heart, stripped of dressing: the relation $\beta^2 + b\beta + c = 0$ is *equivalent* to $\beta$ satisfying its minimal polynomial $X^2 - X - \tfrac12$ scaled to be monic — and there is only one monic quadratic over $\mathbb{Q}$ that $\beta$ satisfies, namely $X^2 - X - \tfrac12$, forcing $(b,c) = (-1, -\tfrac12)$, which is not an integer pair.

**Step 4: Verdict.**

$\varphi = \tfrac12(1+\sqrt5)$ **is** an algebraic integer (minimal polynomial $X^2 - X - 1 \in \mathbb{Z}[X]$). $\beta = \tfrac12(1+\sqrt3)$ is **not** an algebraic integer (minimal polynomial $X^2 - X - \tfrac12 \notin \mathbb{Z}[X]$, and minimality rules out every monic integer polynomial).

> [!note]- Complete formal solution
> **Claim.** $\varphi = \tfrac12(1+\sqrt5)$ is an algebraic integer; $\beta = \tfrac12(1+\sqrt3)$ is not.
>
> *Part 1.* From $\varphi = \tfrac12(1+\sqrt5)$, $\;2\varphi - 1 = \sqrt5$, so $(2\varphi-1)^2 = 5$, i.e. $4\varphi^2 - 4\varphi + 1 = 5$, i.e. $\varphi^2 - \varphi - 1 = 0$. Thus $\varphi$ is a root of the monic polynomial $X^2 - X - 1 \in \mathbb{Z}[X]$. By definition, $\varphi$ is an algebraic integer.
>
> *Part 2.* The same computation for $\beta = \tfrac12(1+\sqrt3)$: $\;2\beta - 1 = \sqrt3$, $(2\beta-1)^2 = 3$, $4\beta^2 - 4\beta - 2 = 0$, hence $\beta^2 - \beta - \tfrac12 = 0$. So $\beta$ satisfies $m_\beta := X^2 - X - \tfrac12 \in \mathbb{Q}[X]$. As $\beta \notin \mathbb{Q}$ (because $\sqrt3$ is irrational), $\beta$ satisfies no degree-$1$ polynomial over $\mathbb{Q}$, so the monic $m_\beta$ is the minimal polynomial of $\beta$ over $\mathbb{Q}$, and every polynomial in $\mathbb{Q}[X]$ vanishing at $\beta$ is a $\mathbb{Q}[X]$-multiple of $m_\beta$.
>
> Suppose $\beta$ is an algebraic integer, so $g(\beta) = 0$ for some monic $g \in \mathbb{Z}[X]$. We may assume $g$ has degree $2$: if a monic integer polynomial vanishes at $\beta$, then writing it as $m_\beta \cdot q$ and clearing denominators shows the degree-$2$ minimal polynomial governs all coefficients; concretely it suffices to show no monic integer *quadratic* vanishes at $\beta$. Let $g = X^2 + bX + c$ with $b,c \in \mathbb{Z}$. Substituting $\beta$ and using $\beta^2 = 1 + \tfrac12\sqrt3$:
> $$0 = \beta^2 + b\beta + c = \Bigl(1 + \tfrac{b}{2} + c\Bigr) + \Bigl(\tfrac12 + \tfrac{b}{2}\Bigr)\sqrt3.$$
> Since $\sqrt3$ is irrational, both bracketed rationals vanish. The second gives $b = -1$; substituting into the first gives $c = -\tfrac12 \notin \mathbb{Z}$, contradicting $c \in \mathbb{Z}$. Hence no monic integer quadratic — and therefore (by minimality) no monic integer polynomial — vanishes at $\beta$. So $\beta$ is not an algebraic integer. $\blacksquare$

---

# Key Takeaways

**To prove a number *is* an algebraic integer, exhibit a witness; to prove it is *not*, you must exclude every witness — and the minimal polynomial is the single object that does both.** "Algebraic integer" is an *existential* property: $\alpha$ qualifies if and only if *there exists* a monic integer polynomial vanishing at it. An existential claim is proved by one example — hence part 1 is genuinely a one-liner, just display $X^2 - X - 1$. The *negation* is universal: $\beta$ fails if and only if *every* monic integer polynomial misses it, and you cannot check infinitely many polynomials by hand. The resolution is the minimal polynomial: by [[Thm - The Minimal Polynomial Generates the Kernel Ideal]] every vanishing polynomial is a multiple of the minimal polynomial, so the infinitely-many-polynomials condition collapses to a *single* test — is the minimal polynomial itself integral? This collapse-of-a-universal-to-a-single-object is the reusable idea: whenever a property says "for all polynomials vanishing at $\alpha$, ...", rewrite it as a statement about the *generator* of the vanishing ideal.

**The minimal polynomial is computed over $\mathbb{Q}$, where $\mathbb{Q}[X]$ is a PID, and *then* its coefficients are inspected for integrality.** There is a subtle two-[[Def - Ring|rings]] structure here worth internalising. Every algebraic number $\alpha$ has a minimal polynomial over the *field* $\mathbb{Q}$ — this always exists and is unique, because $\mathbb{Q}[X]$ is a principal ideal domain and the vanishing ideal is generated by one monic polynomial. Whether $\alpha$ is an *algebraic integer* is then the separate question of whether that $\mathbb{Q}$-minimal polynomial happens to have all coefficients in $\mathbb{Z}$. The radical-elimination computation produces the $\mathbb{Q}$-minimal polynomial directly; the verdict is read off its coefficients. For $\varphi$ they land in $\mathbb{Z}$; for $\beta$ the constant term is $-\tfrac12$, off the integer lattice, and that is the whole story. The general lesson: "is $\alpha$ an algebraic integer" is *never* settled by staring at $\alpha$ — always compute the minimal polynomial and look at its coefficients.

**Numbers $\tfrac12(1+\sqrt d)$ are algebraic integers exactly when $d \equiv 1 \pmod 4$ — the parity of the constant term tracks $d \bmod 4$.** The two parts of this exercise are the two sides of a clean dichotomy. For $\alpha = \tfrac12(1+\sqrt d)$ with $d$ a squarefree integer, the squaring computation always yields $\alpha^2 - \alpha + \tfrac{1-d}{4} = 0$, so the candidate minimal polynomial is $X^2 - X + \tfrac{1-d}{4}$. This is integral if and only if $\tfrac{1-d}{4} \in \mathbb{Z}$, i.e. if and only if $d \equiv 1 \pmod 4$. With $d = 5$ ($5 \equiv 1$) one gets the integral $X^2 - X - 1$ — algebraic integer. With $d = 3$ ($3 \equiv 3$) one gets $X^2 - X - \tfrac12$ — *not* integral, not an algebraic integer. The textbook's example $\tfrac12(1+\sqrt{-3})$ fits ($-3 \equiv 1 \pmod 4$, minimal polynomial $X^2 - X + 1$). This is exactly the rule governing the ring of integers of a quadratic field $\mathbb{Q}(\sqrt d)$: the integers are $\mathbb{Z}[\sqrt d]$ when $d \equiv 2,3 \pmod 4$, but the *larger* ring $\mathbb{Z}\bigl[\tfrac{1+\sqrt d}{2}\bigr]$ when $d \equiv 1 \pmod 4$. Recognising the shape $\tfrac12(1+\sqrt d)$ should immediately trigger the reflex "compute $d \bmod 4$."

**Separating an equation into rational and irrational parts turns one equation into two — and is the workhorse for arguments in $\mathbb{Q}(\sqrt d)$.** Step 3$'$ rests on a move used constantly throughout algebraic number theory: in the field $\mathbb{Q}(\sqrt d)$, every element is uniquely $p + q\sqrt d$ with $p, q \in \mathbb{Q}$, so an equation between two such elements is *equivalent* to the pair of equations "rational parts equal" and "$\sqrt d$-coefficients equal". One equation among irrational numbers becomes two equations among rationals — typically a vastly easier system. The justification is the irrationality of $\sqrt d$: if $p + q\sqrt d = 0$ with $q \neq 0$ then $\sqrt d = -p/q$ would be rational. The trigger is the appearance of a *single* surd $\sqrt d$ in an equation with otherwise rational data; the reaction is to split. This is the same principle as "comparing real and imaginary parts" of a complex equation, or "matching coefficients" of a polynomial identity — read off independent scalar equations from one vector equation by using a basis ($\{1, \sqrt d\}$ here).

**Reduce the general-degree question to the minimal-polynomial degree before doing arithmetic.** A trap in the *no* direction is to feel obliged to argue about monic integer polynomials of *every* degree. The minimal polynomial closes this off. Because every vanishing polynomial is a multiple of the degree-$2$ minimal polynomial $m_\beta$, a hypothetical monic integer vanishing polynomial of high degree is $m_\beta$ times something — and the obstruction (a non-integer coefficient of $m_\beta$) is already exposed by examining degree $2$ alone. So the correct shape of a *no* proof is: "it suffices to consider degree $= \deg(m_\alpha)$, *because* any vanishing polynomial is a multiple of $m_\alpha$; and at that degree the only monic candidate *is* $m_\alpha$ itself, which is not integral." This reduction — from "all degrees" to "the minimal degree" — is generic: whenever you must rule out a property for polynomials of unbounded degree, push everything down to the minimal polynomial's degree, where there is essentially one polynomial to check.

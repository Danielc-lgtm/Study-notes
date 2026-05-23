---
type: exercise
subject: ring-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Ring"
  - "Def - Unit and Field"
  - "Def - Polynomial Ring"
tags: [algebra, ring-theory]
---

# Problem Statement

Let $R$ be a (commutative) ring and let $R[[X]]$ be the ring of formal power series over $R$, whose elements are infinite expressions
$$f = a_0 + a_1 X + a_2 X^2 + \cdots = \sum_{i \geq 0} a_i X^i, \qquad a_i \in R.$$

1. Prove that $f = \sum_{i \ge 0} a_i X^i$ is a **unit** of $R[[X]]$ if and only if its constant term $a_0$ is a unit of $R$.
2. When $a_0$ is a unit, give a **recursive construction** of the inverse $g = \sum_{i \ge 0} b_i X^i$, expressing each $b_i$ in terms of $a_0^{-1}$, the higher coefficients $a_1, \dots, a_i$, and the earlier $b_0, \dots, b_{i-1}$.
3. Deduce that $1 - X$ is a unit in $R[[X]]$, with an explicit inverse, but is **not** a unit in the polynomial ring $R[X]$.

**Recall:**

The objects in play are a ring, the formal power series and polynomials over it, and the units of these [[Def - Ring|rings]].

A [[Def - Ring|ring]] $R$ is an abelian [[Def - Group|group]] under $+$ with an associative, distributive, unital multiplication; all rings here are commutative with identity $1_R$.

A [[Def - Polynomial Ring|polynomial]] over $R$ is a *finite* expression $a_0 + a_1 X + \cdots + a_n X^n$ with coefficients $a_i \in R$ and $X$ a formal symbol; the polynomial ring is $R[X]$. The **degree** of a nonzero polynomial is the largest $m$ with $a_m \neq 0$.

A **formal power series** over $R$ is an *infinite* expression $\sum_{i \ge 0} a_i X^i$ — equivalently, simply a sequence $(a_0, a_1, a_2, \dots)$ of elements of $R$. The power series ring $R[[X]]$ uses the same addition and multiplication rules as $R[X]$ but with no upper limit on the index: addition is coefficientwise, and the **Cauchy product** is
$$\Big( \sum_i a_i X^i \Big)\Big( \sum_j b_j X^j \Big) = \sum_{k \ge 0} c_k X^k, \qquad c_k = \sum_{j=0}^{k} a_j\, b_{k-j}.$$
Each coefficient $c_k$ is a *finite* sum, so the product is well-defined with no notion of convergence: a power series is a formal object, not a function. The identity of $R[[X]]$ is the series $1 + 0X + 0X^2 + \cdots$, the **constant term** of $f$ is $a_0$, and $R$ embeds in $R[[X]]$ as the constant series.

A [[Def - Unit and Field|unit]] of a ring is an element $u$ admitting $v$ with $u v = 1$. Whether $f$ is a unit depends on whether the ambient ring is $R[[X]]$ or $R[X]$ — that contrast is the point of part 3.

---

# Convergent Strategy

**Problem class.** This is an *invertibility criterion* problem: characterise the units of a ring built by a construction (here the power series construction) in terms of data of the ground ring. The topic's [[Rings I — §2.1–2.2#Problem-Solving Strategy|problem-solving strategy]] notes that for a graded or filtered ring — one whose elements are indexed by a degree — invertibility is almost always governed by the bottom-degree part alone, with the higher-degree tail being a correctable perturbation.

**Assumption pattern.** A power series carries one piece of "rigid" data, the constant term $a_0$, and an infinite "soft" tail $a_1 X + a_2 X^2 + \cdots$. The tail is soft because every $X^i$ with $i \ge 1$ is *nilpotent in spirit*: multiplying series only ever pushes powers of $X$ upward, never down, so the tail can never interfere with the degree-$0$ coefficient of a product. The hypothesis "$a_0$ is a unit" is the assumption that the rigid part is already invertible, leaving only the soft part to be tamed.

**Theorem routing.** There is no named theorem; the route is the **coefficient-by-coefficient solution of the equation $fg = 1$**. Writing $fg = 1$ and equating coefficients of $X^k$ on both sides yields, for each $k$, one equation in the single new unknown $b_k$ — and the coefficient of $b_k$ in that equation is always $a_0$. So $a_0$ being a unit is *exactly* what is needed to solve every equation in turn; the recursion never stalls. This is an instance of the legal operation "solve $fg = 1$ degree by degree".

**Key decision point.** The non-obvious realisation is that the infinitely many equations are **triangular**: the equation at level $k$ involves only $b_0, \dots, b_k$, and the new unknown $b_k$ appears solely through the term $a_0 b_k$. An infinite system of equations would be hopeless if the unknowns were entangled, but here each new equation introduces exactly one new unknown and isolates it. Recognising the triangular structure — and that "$X$ raises degree" is precisely what *creates* the triangularity — converts an infinite problem into an infinite sequence of trivial one-variable problems. The contrast in part 3 then turns on a *degree* obstruction that has no analogue for series: a polynomial inverse would have to have finite degree, and the product's top coefficient cannot be cancelled.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings I — §2.1–2.2#Legal Operations|the topic page's Legal Operations]]:

1. **Solve the unit equation $fg = 1$ coefficient by coefficient (degree induction).** The defining equation of an inverse is split into one scalar equation per power of $X$; the equations are solved in increasing order of degree, each determining one new coefficient of $g$.

2. **Exploit that multiplication by $X$ strictly raises degree.** This is the structural fact that makes the coefficient system triangular: the constant term of a product depends only on the constant terms of the factors, and more generally the degree-$k$ coefficient depends only on coefficients of degree $\le k$.

3. **Use a unit of the ground ring to invert a "leading" coefficient.** At every stage the equation to be solved has the shape $a_0 b_k = (\text{known})$; multiplying by $a_0^{-1}$ solves it. The hypothesis travels from $R$ into $R[[X]]$ exactly through this repeated step.

4. **Use a degree / leading-coefficient argument to *deny* invertibility in $R[X]$.** Part 3's negative half runs the multiplication-raises-degree fact in reverse: if $f$ has a positive-degree factor structure, the product of two nonzero finite-degree polynomials has a genuine top term that cannot vanish, blocking the equation $fg = 1$.

---

# Hints

> [!note]- Hint 1
> Suppose $g = \sum b_i X^i$ is an inverse of $f$, so $fg = 1$. Write out the product $fg$ using the Cauchy product, and equate the coefficient of $X^k$ on the left to the coefficient of $X^k$ on the right (which is $1$ for $k = 0$ and $0$ for $k \ge 1$). Start with $k = 0$: what single equation do you get, and what does it force about $a_0$?

> [!note]- Hint 2
> The $k = 0$ equation is $a_0 b_0 = 1$, so $a_0$ must be a unit of $R$ and $b_0 = a_0^{-1}$. That is the "only if" direction. For "if", *assume* $a_0$ is a unit and try to *build* $g$. The coefficient of $X^k$ in $fg$ is $\sum_{j=0}^{k} a_j b_{k-j} = a_0 b_k + a_1 b_{k-1} + \cdots + a_k b_0$. Setting this equal to $0$ for $k \ge 1$, which terms are already known by the time you solve for $b_k$?

> [!note]- Hint 3
> The level-$k$ equation $a_0 b_k + a_1 b_{k-1} + \cdots + a_k b_0 = 0$ involves the unknown $b_k$ only in the term $a_0 b_k$; every other $b_{k-1}, \dots, b_0$ was determined at an earlier stage. So solve for $b_k$:
> $$b_k = -\,a_0^{-1}\,(a_1 b_{k-1} + a_2 b_{k-2} + \cdots + a_k b_0).$$
> This recursion never gets stuck because $a_0^{-1}$ always exists. Induction on $k$ finishes the construction of the inverse.

> [!note]- Hint 4
> For $1 - X$: here $a_0 = 1$ (a unit, with $1^{-1} = 1$), so it is a unit of $R[[X]]$; running the recursion, or recognising the geometric series, gives the inverse $1 + X + X^2 + \cdots$. Check directly that $(1 - X)(1 + X + X^2 + \cdots) = 1$. In $R[X]$, suppose $(1 - X) h = 1$ with $h$ a polynomial of degree $d$. What is the degree of the left-hand side, and what is the degree of $1$? (Watch the leading coefficient: $1 - X$ has leading coefficient $-1$, which is not a zero divisor.)

---

# Solution

The plan: write $fg = 1$ as one equation per power of $X$; the $X^0$ equation forces $a_0$ to be a unit; assuming it is, the $X^k$ equations form a triangular system solved by a recursion in $a_0^{-1}$; finally apply this to $1 - X$ and contrast with a degree obstruction in $R[X]$.

**Step 1: if $f$ is a unit, then $a_0$ is a unit (the constant term of a product is the product of constant terms).**

If $fg = 1$ for some $g = \sum b_i X^i$, then comparing constant terms gives $a_0 b_0 = 1$. Hence $a_0$ has the inverse $b_0$ in $R$.

> [!note]- Derivation
> Let $g = \sum_{i \ge 0} b_i X^i$ satisfy $fg = 1$ in $R[[X]]$. The Cauchy product gives, for the coefficient of $X^k$,
> $$[X^k](fg) = \sum_{j=0}^{k} a_j\, b_{k-j}.$$
> The series $1 \in R[[X]]$ has coefficient $1$ at $X^0$ and $0$ at every $X^k$ with $k \ge 1$. Equating coefficients of $X^0$:
> $$a_0 b_0 = 1.$$
> By the definition of a unit, this equation says precisely that $a_0$ is a unit of $R$, with inverse $b_0$. (Commutativity makes $a_0 b_0 = b_0 a_0 = 1$, so the side does not matter.) This is the "only if" direction: a unit power series has a unit constant term, and moreover the constant term of the inverse is forced to be $a_0^{-1}$.

**Step 2: if $a_0$ is a unit, the equations $[X^k](fg) = 0$ for $k \ge 1$ form a triangular system.**

The coefficient of $X^k$ in $fg$ is $a_0 b_k + a_1 b_{k-1} + \cdots + a_k b_0$. Setting it to $0$ gives an equation whose only previously-undetermined unknown is $b_k$, appearing as $a_0 b_k$.

> [!note]- Derivation
> Suppose now $a_0$ is a unit of $R$; we construct $g = \sum b_i X^i$ with $fg = 1$. The equation $fg = 1$ holds if and only if **all** of the coefficient equations hold:
> $$\text{(level }0\text{)}\quad a_0 b_0 = 1, \qquad\qquad \text{(level }k \ge 1\text{)}\quad \sum_{j=0}^{k} a_j b_{k-j} = 0.$$
> Separate out the $j = 0$ term of the level-$k$ equation:
> $$a_0 b_k \;+\; \underbrace{a_1 b_{k-1} + a_2 b_{k-2} + \cdots + a_k b_0}_{\text{involves only } b_0, \dots, b_{k-1}} \;=\; 0.$$
> The crucial observation: in the Cauchy sum $\sum_j a_j b_{k-j}$, the index of $b$ is $k - j$, which equals $k$ only when $j = 0$. So the *new* unknown $b_k$ occurs in exactly one term, $a_0 b_k$; every other term uses a coefficient $b_{k-j}$ with $k - j < k$, i.e. a coefficient of strictly lower index. This is the **triangularity** of the system, and it is a direct consequence of multiplication by $X$ raising degree — a coefficient of $g$ can only be "dragged down" to index $k$ by being paired with a coefficient $a_j$ of index $j \ge 0$, and pairing with $a_0$ leaves it at index $k$ while any $a_j$ with $j \ge 1$ moves it below $k$.

**Step 3: the triangular system has a unique solution, given by an explicit recursion.**

Because the new unknown enters through $a_0 b_k$ and $a_0$ is invertible, each level solves for one coefficient:
$$b_0 = a_0^{-1}, \qquad b_k = -\,a_0^{-1}\,\big(a_1 b_{k-1} + a_2 b_{k-2} + \cdots + a_k b_0\big) \quad (k \ge 1).$$
Induction on $k$ shows every $b_k$ is determined, so $g$ exists and $f$ is a unit.

> [!note]- Derivation
> We define the coefficients $b_k$ by strong induction on $k$ and verify they satisfy every coefficient equation.
>
> *Base $k = 0$.* Since $a_0$ is a unit, set $b_0 := a_0^{-1} \in R$. Then $a_0 b_0 = 1$, so the level-$0$ equation holds.
>
> *Inductive step.* Fix $k \ge 1$ and suppose $b_0, \dots, b_{k-1}$ have already been defined. The level-$k$ equation $a_0 b_k + (a_1 b_{k-1} + \cdots + a_k b_0) = 0$ has all of $a_1, \dots, a_k$ given (they are coefficients of $f$) and all of $b_0, \dots, b_{k-1}$ given by the inductive hypothesis. So the bracket $S_k := a_1 b_{k-1} + a_2 b_{k-2} + \cdots + a_k b_0$ is a fixed element of $R$. The equation reads $a_0 b_k = -S_k$; multiplying on the left by the unit $a_0^{-1}$ gives the unique solution
> $$b_k \;:=\; -\,a_0^{-1}\, S_k \;=\; -\,a_0^{-1}\,(a_1 b_{k-1} + a_2 b_{k-2} + \cdots + a_k b_0).$$
> With this choice the level-$k$ equation is satisfied. By induction $b_k$ is defined for every $k \ge 0$, the resulting series $g = \sum b_k X^k$ lies in $R[[X]]$, and *all* coefficient equations of $fg = 1$ hold, so $fg = 1$. Hence $f$ is a unit. Together with Step 1 this proves part 1: $f$ is a unit of $R[[X]]$ $\iff a_0$ is a unit of $R$. The recursion above is the explicit inverse construction of part 2; uniqueness of each $b_k$ shows the inverse is unique (as it must be in any ring).

**Step 4: $1 - X$ is a unit of $R[[X]]$ but not of $R[X]$.**

For $1 - X$ the constant term is $1$, a unit of $R$, so by parts 1–2 it is a unit of $R[[X]]$; the recursion yields the geometric series $\sum_{i \ge 0} X^i$. In $R[X]$ a degree count shows no polynomial inverse can exist.

> [!note]- Derivation
> *Unit in $R[[X]]$.* Write $1 - X = a_0 + a_1 X + a_2 X^2 + \cdots$ with $a_0 = 1$, $a_1 = -1$, and $a_i = 0$ for $i \ge 2$. The constant term $a_0 = 1$ is a unit of $R$ (with $1^{-1} = 1$), so part 1 already gives that $1 - X$ is a unit of $R[[X]]$. Running the recursion of Step 3: $b_0 = a_0^{-1} = 1$; for $k \ge 1$,
> $$b_k = -a_0^{-1}(a_1 b_{k-1} + a_2 b_{k-2} + \cdots) = -(a_1 b_{k-1}) = -(-1)\, b_{k-1} = b_{k-1},$$
> since $a_1 = -1$ and all higher $a_i$ vanish. So $b_k = b_{k-1} = \cdots = b_0 = 1$ for every $k$, giving the inverse
> $$(1 - X)^{-1} = 1 + X + X^2 + X^3 + \cdots = \sum_{i \ge 0} X^i.$$
> One verifies directly: the Cauchy product $(1 - X)\sum_{i \ge 0} X^i$ has constant coefficient $1 \cdot 1 = 1$, and for $k \ge 1$ coefficient $1 \cdot 1 + (-1) \cdot 1 = 0$ (the only contributing terms pair $a_0 = 1$ with $b_k = 1$ and $a_1 = -1$ with $b_{k-1} = 1$). So the product is $1$, confirming the formal "geometric series" identity.
>
> *Not a unit in $R[X]$.* Suppose, for contradiction, that $1 - X$ had an inverse $h \in R[X]$, so $(1 - X)\,h = 1$ in $R[X]$. The polynomial $h$ is nonzero (its product with $1 - X$ is $1 \ne 0$, assuming $R$ is not the zero ring; if $R = \{0\}$ the claim is vacuous as everything is a unit but there is nothing to say). Let $h$ have degree $d \ge 0$ with leading coefficient $c_d \neq 0$, so $h = c_0 + c_1 X + \cdots + c_d X^d$. The product $(1 - X) h$ then has, at the top, the term coming from $(-X) \cdot c_d X^d = -c_d X^{d+1}$, and no term of $h$ can contribute another $X^{d+1}$ except this one. Its coefficient is $-c_d$. Since $c_d \neq 0$ and $-1$ is not a zero divisor in any ring (it is a unit, with $(-1)(-1) = 1$), we have $-c_d \neq 0$. Hence $(1 - X) h$ has nonzero coefficient at $X^{d+1}$, so $(1 - X)h$ has degree $d + 1 \ge 1$. But $1$ has degree $0$. A polynomial of degree $\ge 1$ cannot equal the polynomial $1$, contradiction. Therefore $1 - X$ is **not** a unit of $R[X]$.
>
> The contrast is structural: in $R[[X]]$ the inverse is the *infinite* series $\sum X^i$, which is a perfectly legal power series but not a polynomial. The polynomial ring simply does not contain the element that would do the job — invertibility is a property of the *ambient ring*, exactly as for $2 \in \mathbb{Z}$ versus $2 \in \mathbb{Q}$. $\blacksquare$

> [!note]- Complete formal solution
> Let $f = \sum_{i \ge 0} a_i X^i \in R[[X]]$.
>
> **($f$ unit $\Rightarrow a_0$ unit.)** If $fg = 1$ with $g = \sum b_i X^i$, the $X^0$-coefficient of $fg$ is $a_0 b_0$, and that of $1$ is $1$; so $a_0 b_0 = 1$ and $a_0$ is a unit of $R$.
>
> **($a_0$ unit $\Rightarrow f$ unit.)** Assume $a_0 \in R^\times$. Define $b_0, b_1, b_2, \dots \in R$ recursively by
> $$b_0 = a_0^{-1}, \qquad b_k = -\,a_0^{-1}\sum_{j=1}^{k} a_j\, b_{k-j} \quad (k \ge 1).$$
> Each $b_k$ is well-defined because $a_0^{-1}$ exists and $b_0, \dots, b_{k-1}$ are defined at earlier stages. Set $g = \sum_{k \ge 0} b_k X^k \in R[[X]]$. For $k = 0$, the $X^0$-coefficient of $fg$ is $a_0 b_0 = 1$. For $k \ge 1$, the $X^k$-coefficient of $fg$ is $\sum_{j=0}^k a_j b_{k-j} = a_0 b_k + \sum_{j=1}^k a_j b_{k-j} = -\sum_{j=1}^k a_j b_{k-j} + \sum_{j=1}^k a_j b_{k-j} = 0$. So $fg = 1$ and $f$ is a unit.
>
> Hence $f \in R[[X]]^\times \iff a_0 \in R^\times$, and when this holds the inverse is the series $g$ above.
>
> **($1 - X$.)** Here $a_0 = 1 \in R^\times$, so $1 - X \in R[[X]]^\times$. The recursion gives $b_0 = 1$ and $b_k = -a_0^{-1} a_1 b_{k-1} = b_{k-1}$ for $k \ge 1$ (as $a_1 = -1$, $a_{\ge 2} = 0$), so $b_k = 1$ for all $k$ and $(1-X)^{-1} = \sum_{i \ge 0} X^i$.
>
> In $R[X]$ (with $R \ne \{0\}$): if $(1 - X) h = 1$ with $\deg h = d$ and leading coefficient $c_d \ne 0$, the $X^{d+1}$-coefficient of $(1-X)h$ is $-c_d \ne 0$ (since $-1$ is a unit, hence not a zero divisor), so $\deg\big((1-X)h\big) = d + 1 \ge 1 \ne 0 = \deg 1$, a contradiction. So $1 - X \notin R[X]^\times$. $\blacksquare$

---

# Key Takeaways

**For a degree-graded ring, invertibility is decided at the bottom degree, and the rest is a correctable perturbation.** A power series splits into a constant term $a_0$ and a tail of positive-degree terms. The theorem is that *only* the constant term matters for invertibility: $f$ is a unit if and only if $a_0$ is. The reason is that the positive-degree part behaves like a nilpotent — multiplying by $X$ only ever pushes degrees upward — so the tail is, in the precise sense of the maximal [[Def - Ideal|ideal]] $(X)$, a "small" perturbation of the constant term, and adding a small perturbation to a unit keeps it a unit. This is a deep and recurring pattern: in *any* ring filtered by powers of an ideal $I$ where things behave well at the limit (a complete local ring), an element is a unit if and only if its image in the [[Def - Residue|residue]] ring $R/I$ is a unit. $R[[X]]$ is the prototype, with $I = (X)$ and residue ring $R$. The instinct to extract from this exercise: when a ring has a notion of "leading part" and a "topologically nilpotent" remainder, test invertibility on the leading part alone and expect the remainder to be absorbable.

**An infinite system of equations becomes tractable the moment it is triangular — and "multiplication raises degree" is what creates the triangularity.** Solving $fg = 1$ means solving infinitely many scalar equations for infinitely many unknowns $b_0, b_1, \dots$. That would be hopeless if the unknowns were globally entangled. What rescues it is that the level-$k$ equation involves only $b_0, \dots, b_k$, and the genuinely new unknown $b_k$ sits in a single term $a_0 b_k$. So the system is *lower-triangular*, and a triangular system is solved by plain forward substitution, one variable at a time. The structural cause is that the Cauchy product index $b_{k-j}$ reaches the value $k$ only at $j = 0$: pairing $b_k$ with anything beyond the constant term $a_0$ would move it to a higher power of $X$. The transferable lesson is to *always look for a triangulating order* on the unknowns of an infinite or large system — by degree, by valuation, by some [[Def - Filtration|filtration]] — because triangularity downgrades an intractable simultaneous solve into a sequence of one-variable solves. The same idea constructs inverses of upper-triangular matrices, solves recurrences, and lifts solutions in Hensel's lemma.

**Each step of the recursion spends one use of $a_0^{-1}$ — the ground-ring unit is the resource that keeps the recursion from stalling.** The recursion $b_k = -a_0^{-1}(a_1 b_{k-1} + \cdots + a_k b_0)$ works at *every* level for exactly one reason: the new unknown $b_k$ always enters as $a_0 b_k$, and $a_0$ is invertible, so the equation $a_0 b_k = (\text{known})$ can always be solved. Had $a_0$ been a mere non-unit, the level-$0$ equation $a_0 b_0 = 1$ would already be unsolvable and the recursion would never start. This isolates the precise role of the hypothesis: "$a_0$ is a unit" is not a convenience, it is the renewable resource consumed once per step to advance the induction. Recognising *which hypothesis is the fuel of a recursion* — the thing used identically at every stage — is a general analytic skill: it tells you the exact minimal assumption, and it tells you the proof is an induction whose inductive step is a single application of that hypothesis.

**Invertibility is a property of the ambient ring, and enlarging the ring can create inverses that finite-degree objects cannot supply.** The element $1 - X$ is a unit of $R[[X]]$ and a non-unit of $R[X]$, with the very same name, because its inverse $1 + X + X^2 + \cdots$ is an infinite series — a legal citizen of $R[[X]]$ but not of the polynomial ring. The polynomial ring is "too small" to contain the witness. This is the exact analogue of $2$ being a non-unit of $\mathbb{Z}$ but a unit of $\mathbb{Q}$: passing to a larger ring can turn a non-unit into a unit. The negative half — *proving* non-invertibility in $R[X]$ — is settled by a degree/leading-coefficient argument, which is the canonical tool for denying polynomial identities: the product of a degree-$1$ and a degree-$d$ polynomial genuinely has degree $d + 1$ (as long as the leading coefficients do not multiply to zero), so it cannot equal a degree-$0$ polynomial. The pair of lessons: never ask "is $f$ a unit?" without fixing the ring, and reach for degree counting whenever you must *forbid* a polynomial equation rather than produce one.

---
type: exercise
subject: ring-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Gauss's Lemma"
  - "Def - Content and Primitive Polynomial"
  - "Def - Irreducible and Prime Elements"
  - "Def - Field of Fractions"
  - "Def - Polynomial Ring"
tags: [algebra, ring-theory]
---

# Problem Statement

1. Let $f \in \mathbb{Z}[X]$ be a **primitive** polynomial that is **reducible over $\mathbb{Q}$** — it factors as a product of two non-constant polynomials in $\mathbb{Q}[X]$. Prove that $f$ is already reducible over $\mathbb{Z}$: it factors as a product of two non-constant polynomials in $\mathbb{Z}[X]$. In slogan form: *for a primitive polynomial, if a factorisation exists at all, one exists with no denominators.*
2. Use this to prove that $X^3 + X + 1$ is irreducible over $\mathbb{Q}$, by checking only that it has no integer root.

**Recall:**

The setting is the [[Def - Polynomial Ring|polynomial ring]] $\mathbb{Z}[X]$, its [[Def - Field of Fractions|field of fractions]] coefficient ring $\mathbb{Q}$, the notion of a [[Def - Content and Primitive Polynomial|primitive polynomial]], and [[Def - Irreducible and Prime Elements|irreducibility]].

The **content** of $f = a_0 + a_1 X + \cdots + a_n X^n \in \mathbb{Z}[X]$ is $c(f) = \gcd(a_0, \dots, a_n)$, defined up to sign (a unit of $\mathbb{Z}$). The polynomial is [[Def - Content and Primitive Polynomial|primitive]] when $c(f)$ is a unit — the coefficients are collectively coprime. Every non-zero $f \in \mathbb{Z}[X]$ factors as $f = c(f)\,f_1$ with $f_1$ primitive: pull out the gcd of the coefficients.

A polynomial $f$ of positive degree is **reducible over a ring** $S \in \{\mathbb{Z}, \mathbb{Q}\}$ if $f = gh$ with $g, h \in S[X]$ both non-units of $S[X]$; otherwise it is [[Def - Irreducible and Prime Elements|irreducible]] over $S$. The crucial difference between the two rings: in $\mathbb{Q}[X]$ the units are the non-zero *constants*, so a non-unit factor just needs positive degree; in $\mathbb{Z}[X]$ the units are only $\pm 1$, so a constant like $2$ is a non-unit, and "reducible over $\mathbb{Z}$" can mean splitting off a non-unit constant. This is why the primitivity hypothesis matters — it rules out the boring factorisation $f = 2 \cdot (\tfrac12 f)$.

![[Thm - Gauss's Lemma#Statement]]

This exercise *is* (part 1) a guided proof of one direction of Gauss's lemma, specialised to $R = \mathbb{Z}$, $F = \mathbb{Q}$, and (part 2) a flagship application.

A standing tool used throughout: **content is multiplicative up to a unit**. If $g, h \in \mathbb{Z}[X]$ then $c(gh)$ is an associate of $c(g)\,c(h)$. In particular, *a product of two primitive polynomials is primitive* — this is the technical heart, often itself called Gauss's lemma.

---

# Convergent Strategy

**Problem class.** Part 1 is a *transfer-of-factorisation* result: an object factors over a large ring (with denominators), and we must produce a factorisation over a smaller ring (without). Part 2 is *irreducibility certification by a root search*. The [[Rings III — §2.5–2.6]] strategy records that for cubics and quadratics, "no root" is equivalent to "irreducible" — but only over a field; the role of part 1 is precisely to make the integer root search *legitimate* as a test for irreducibility over $\mathbb{Q}$.

**Assumption pattern.** Part 1's hypotheses are: a polynomial in $\mathbb{Z}[X]$, primitive, with a known $\mathbb{Q}[X]$-factorisation. "Primitive" is the load-bearing assumption — without it the conclusion is false ($2X + 2 = 2(X+1)$ is reducible over $\mathbb{Z}$ in a trivial way that says nothing). The $\mathbb{Q}[X]$-factorisation supplies factors with rational coefficients; the task is to clear denominators without breaking the degree of either factor. Part 2's signal is a *monic cubic* — monic gives primitivity for free, and degree $3$ means a non-trivial factorisation must include a linear factor, hence a root.

**Theorem routing.** Part 1 routes through *multiplicativity of content*: write the $\mathbb{Q}[X]$-factors with denominators cleared, $\lambda f = g' h'$ with $g', h' \in \mathbb{Z}[X]$ and $\lambda \in \mathbb{Z}$; extract the primitive parts $g' = c(g')g_1$, $h' = c(h')h_1$; compare contents on both sides; cancel. Part 2 routes: a $\mathbb{Q}[X]$-factorisation of $X^3+X+1$ would, by part 1, give a $\mathbb{Z}[X]$-factorisation; degree $3$ forces a degree-$1$ factor; a monic-after-normalisation degree-$1$ factor over $\mathbb{Z}$ forces an integer root; checking $\pm 1$ shows there is none.

**Key decision point.** The non-obvious step in part 1 is the *bookkeeping of contents*. After clearing denominators to get $\lambda f = g' h'$, one writes each side as (content) $\times$ (primitive part). The left side has content $|\lambda| \cdot c(f) = |\lambda|$ since $f$ is primitive. The right side has content $c(g')c(h')$ up to a unit. Equating, $|\lambda|$ *equals* $c(g')c(h')$ up to a unit — so the integer $\lambda$ that we introduced to clear denominators is *entirely absorbed* into the contents of the cleared factors, and cancelling it leaves a clean factorisation $f = \pm g_1 h_1$ with $g_1, h_1 \in \mathbb{Z}[X]$ primitive of the same degrees as $g', h'$. The insight is that the denominators were never essential — they cancel against the content.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings III — §2.5–2.6#Legal Operations|the topic page's Legal Operations]]:

1. **Clear denominators.** Given a factorisation in $\mathbb{Q}[X]$, multiply each factor by a suitable integer to land both factors in $\mathbb{Z}[X]$, at the cost of an integer multiple of $f$.

2. **Split off the content.** Write any $\mathbb{Z}[X]$ polynomial as (content) $\times$ (primitive part), $g' = c(g')\,g_1$.

3. **Compare contents across an equation, using multiplicativity.** Use $c(gh) \sim c(g)c(h)$ and the fact that a product of primitives is primitive to read off the content of both sides of $\lambda f = g'h'$.

4. **Cancel a common factor in an integral domain.** $\mathbb{Z}[X]$ is an integral domain, so $\lambda f = \lambda(\pm g_1 h_1)$ may be cancelled to $f = \pm g_1 h_1$.

5. **Convert a degree-$1$ factor into a root.** A factor $bX + a \in \mathbb{Z}[X]$ of $X^3+X+1$ yields, after matching leading coefficients, an honest integer root.

6. **Run a finite root search.** For a monic integer polynomial, any integer root divides the constant term — here only $\pm 1$ need be tested.

---

# Hints

> [!note]- Hint 1
> For part 1, start from the given $\mathbb{Q}[X]$-factorisation $f = g\,h$ with $g, h$ non-constant. The coefficients of $g$ and $h$ are rational. Multiply $g$ by the common denominator of its coefficients, and likewise $h$, to get polynomials with integer coefficients. Track the integer factor this introduces.

> [!note]- Hint 2
> After clearing denominators you have $\lambda f = g' h'$ with $\lambda \in \mathbb{Z}_{>0}$ and $g', h' \in \mathbb{Z}[X]$ non-constant. Now write each integer polynomial as content times primitive part: $g' = c(g') g_1$, $h' = c(h') h_1$, with $g_1, h_1$ primitive of the *same degrees* as $g', h'$.

> [!note]- Hint 3
> Take the content of both sides of $\lambda f = c(g')c(h')\,g_1 h_1$. On the left, $c(\lambda f) = \lambda\, c(f) = \lambda$ because $f$ is primitive. On the right, $g_1 h_1$ is a product of primitives, hence primitive, so the content of the right side is $c(g')c(h')$ up to a unit. Conclude $\lambda = \pm\, c(g')c(h')$, and substitute back.

> [!note]- Hint 4
> For part 2: $X^3 + X + 1$ is monic, hence primitive. If it were reducible over $\mathbb{Q}$, part 1 makes it reducible over $\mathbb{Z}$, as a product of two non-constant integer polynomials. The degrees add to $3$, so one factor has degree $1$: $X^3 + X + 1 = (b_0 + b_1 X)(c_0 + c_1 X + c_2 X^2)$. Match the leading coefficient ($b_1 c_2 = 1$) and constant term ($b_0 c_0 = 1$), then ask: what root does the linear factor contribute, and is it a root of $X^3 + X + 1$? Test $X = 1$ and $X = -1$.

---

# Solution

The whole of part 1 is the observation that the integer $\lambda$ introduced to clear denominators is exactly absorbed by the contents of the cleared factors — so it cancels, leaving an integer factorisation of the same shape. Part 2 then turns the integer root search into a legitimate irreducibility test.

**Step 1: Clear denominators.**

From the $\mathbb{Q}[X]$-factorisation $f = gh$, there is a positive integer $\lambda$ and non-constant polynomials $g', h' \in \mathbb{Z}[X]$ with
$$\lambda f = g'\,h', \qquad \deg g' = \deg g, \quad \deg h' = \deg h.$$

> [!note]- Derivation
> By hypothesis $f = g h$ with $g, h \in \mathbb{Q}[X]$ both of positive degree. Let $d_g$ be a common denominator of the (finitely many) rational coefficients of $g$, so $g' := d_g\, g \in \mathbb{Z}[X]$; similarly $h' := d_h\, h \in \mathbb{Z}[X]$. Multiplying $g$ or $h$ by a non-zero constant does not change its degree, so $\deg g' = \deg g$ and $\deg h' = \deg h$, both positive.
>
> Set $\lambda := d_g d_h \in \mathbb{Z}_{>0}$. Then
> $$\lambda f = (d_g d_h)\,gh = (d_g\,g)(d_h\,h) = g'\,h',$$
> an identity in $\mathbb{Z}[X]$.

**Step 2: Split off the contents and compare.**

Writing $g' = c(g')g_1$ and $h' = c(h')h_1$ with $g_1, h_1$ primitive, comparison of contents on both sides of $\lambda f = g'h'$ forces $\lambda = \pm\,c(g')c(h')$.

> [!note]- Derivation
> Every non-zero polynomial in $\mathbb{Z}[X]$ is its content times a primitive polynomial. Write
> $$g' = c(g')\,g_1, \qquad h' = c(h')\,h_1,$$
> with $g_1, h_1 \in \mathbb{Z}[X]$ primitive; note $\deg g_1 = \deg g'$ and $\deg h_1 = \deg h'$, both positive. Substituting into $\lambda f = g'h'$,
> $$\lambda f = c(g')\,c(h')\;g_1 h_1.$$
> Now take contents of both sides.
>
> *Left side.* $c(\lambda f) = |\lambda|\,c(f)$. Since $f$ is **primitive**, $c(f)$ is a unit, so $c(\lambda f) = |\lambda|$ up to a unit.
>
> *Right side.* The factor $c(g')c(h')$ is a constant, and $g_1 h_1$ is a *product of two primitive polynomials*. By multiplicativity of content (the technical core of [[Thm - Gauss's Lemma|Gauss's lemma]]), **a product of primitives is primitive**, so $c(g_1 h_1)$ is a unit. Hence $c\big(c(g')c(h')\,g_1 h_1\big) = c(g')c(h')$ up to a unit.
>
> Equating the two contents: $|\lambda| = \pm\,c(g')c(h')$, i.e. $\lambda = \pm\,c(g')\,c(h')$ in $\mathbb{Z}$ — the denominator-clearing integer is exactly the product of the contents of the cleared factors.

**Step 3: Cancel $\lambda$ to obtain an integer factorisation.**

Substituting $\lambda = \pm c(g')c(h')$ and cancelling, $f = \pm\, g_1 h_1$ with $g_1, h_1 \in \mathbb{Z}[X]$ non-constant. Hence $f$ is reducible over $\mathbb{Z}$.

> [!note]- Derivation
> From Step 2, $\lambda f = c(g')c(h')\,g_1 h_1$ and $\lambda = \pm\,c(g')c(h')$. Substituting,
> $$\pm\,c(g')c(h')\;f = c(g')c(h')\;g_1 h_1.$$
> The ring $\mathbb{Z}[X]$ is an integral domain and $c(g')c(h') \neq 0$, so we may cancel it:
> $$f = \pm\,g_1\,h_1.$$
> Absorb the sign into $g_1$ (replace $g_1$ by $-g_1$ if needed). Then $f = g_1 h_1$ with $g_1, h_1 \in \mathbb{Z}[X]$, and $\deg g_1 = \deg g > 0$, $\deg h_1 = \deg h > 0$. Both factors have positive degree, so neither is a unit of $\mathbb{Z}[X]$ (units are $\pm 1$). Therefore $f$ is reducible over $\mathbb{Z}$ — and the factorisation has *no denominators*. This proves part 1.

**Step 4: $X^3 + X + 1$ is irreducible over $\mathbb{Q}$.**

$X^3 + X + 1$ is monic, hence primitive. If it were reducible over $\mathbb{Q}$, part 1 would make it reducible over $\mathbb{Z}$, forcing a linear factor and hence an integer root. But $\pm 1$ are not roots, so there is no integer root, and the polynomial is irreducible over $\mathbb{Q}$.

> [!note]- Derivation
> Let $f = X^3 + X + 1 \in \mathbb{Z}[X]$. Its coefficients are $1, 0, 1, 1$, so $c(f) = \gcd(1,0,1,1) = 1$: $f$ is primitive. (Monic always implies primitive.)
>
> Suppose, for contradiction, $f$ is reducible over $\mathbb{Q}$. By **part 1** (applicable because $f$ is primitive), $f$ is reducible over $\mathbb{Z}$:
> $$X^3 + X + 1 = g\,h, \qquad g, h \in \mathbb{Z}[X] \text{ non-constant.}$$
> The degrees satisfy $\deg g + \deg h = 3$ with both $\geq 1$, so $\{\deg g, \deg h\} = \{1, 2\}$. Say $\deg g = 1$:
> $$g = b_0 + b_1 X, \qquad h = c_0 + c_1 X + c_2 X^2, \qquad b_i, c_j \in \mathbb{Z}.$$
> Matching coefficients in $gh = X^3 + X + 1$:
> - **Leading coefficient ($X^3$):** $b_1 c_2 = 1$, so $b_1, c_2 \in \{+1, -1\}$ — in particular $b_1 = \pm 1$.
> - **Constant term ($X^0$):** $b_0 c_0 = 1$, so $b_0 \in \{+1, -1\}$.
>
> The linear factor $g = b_0 + b_1 X$ with $b_1 = \pm 1$ has the rational root $X = -b_0 / b_1 = \mp b_0 \in \{+1, -1\}$, and since $g \mid f$ this is a root of $f$. So $f$ has a root in $\{+1, -1\}$.
>
> Check directly:
> $$f(1) = 1^3 + 1 + 1 = 3 \neq 0, \qquad f(-1) = (-1)^3 + (-1) + 1 = -1 \neq 0.$$
> Neither $\pm 1$ is a root — contradiction. Therefore $f = X^3 + X + 1$ is **not** reducible over $\mathbb{Q}$: it is irreducible over $\mathbb{Q}$.

> [!note]- Complete formal solution
> **Claim.** (1) A primitive $f \in \mathbb{Z}[X]$ reducible over $\mathbb{Q}$ is reducible over $\mathbb{Z}$. (2) $X^3 + X + 1$ is irreducible over $\mathbb{Q}$.
>
> *Part 1.* Let $f = gh$ with $g, h \in \mathbb{Q}[X]$ non-constant. Clear denominators: with $d_g, d_h \in \mathbb{Z}_{>0}$ common denominators of the coefficients, $g' := d_g g$ and $h' := d_h h$ lie in $\mathbb{Z}[X]$, are non-constant, and $\lambda f = g'h'$ where $\lambda := d_g d_h$. Write $g' = c(g')g_1$, $h' = c(h')h_1$ with $g_1, h_1$ primitive; then $\lambda f = c(g')c(h')\,g_1 h_1$. Taking contents: the left side has content $|\lambda|c(f) = |\lambda|$ since $f$ is primitive; the right side has content $c(g')c(h')$ up to a unit, since $g_1 h_1$ is a product of primitives, hence primitive (multiplicativity of content). So $\lambda = \pm c(g')c(h')$, and cancelling this non-zero constant in the integral domain $\mathbb{Z}[X]$ gives $f = \pm g_1 h_1$. Both $g_1, h_1$ are non-constant, so $f$ is reducible over $\mathbb{Z}$.
>
> *Part 2.* $f = X^3 + X + 1$ is monic, hence primitive. If $f$ were reducible over $\mathbb{Q}$, part 1 makes it $f = gh$ with $g, h \in \mathbb{Z}[X]$ non-constant; degrees $1$ and $2$. The degree-$1$ factor $b_0 + b_1 X$ has, by matching the $X^3$-coefficient, $b_1 c_2 = 1$ so $b_1 = \pm 1$, and by matching constants $b_0 c_0 = 1$ so $b_0 = \pm 1$; it contributes a root $-b_0/b_1 \in \{\pm 1\}$ of $f$. But $f(1) = 3$ and $f(-1) = -1$ are both non-zero. Contradiction; hence $f$ is irreducible over $\mathbb{Q}$. $\blacksquare$

---

# Key Takeaways

**For a primitive polynomial, denominators in a rational factorisation are an illusion — they always cancel against content.** This is the conceptual content of part 1, and it is what makes Gauss's lemma indispensable. When you factor a polynomial over $\mathbb{Q}$ you produce factors with rational coefficients, and a priori those denominators might be essential. The theorem says they never are: clearing denominators introduces an integer multiplier $\lambda$, and $\lambda$ turns out to equal the product of the contents of the cleared factors, so it cancels exactly. The transferable mechanism — *introduce an auxiliary integer to clear denominators, then show it is absorbed by content* — recurs throughout the theory of $R[X]$ for a UFD $R$: it is the engine behind the proof that $R[X]$ is a UFD, and behind the proposition that divisibility by a primitive polynomial is the same over $R[X]$ as over $F[X]$. The trigger to reach for this idea: any time you have information about a polynomial over a field of fractions $F$ and want to descend to the ring $R$, the move is "clear denominators, then bookkeep contents."

**Gauss's lemma is what makes a root search a legitimate irreducibility test over $\mathbb{Q}$.** A naive attempt to prove $X^3 + X + 1$ irreducible over $\mathbb{Q}$ by "it has no rational root" has a gap: why should a *rational* root search be finite or even decisive? Part 1 closes the gap. Because the polynomial is primitive, any $\mathbb{Q}[X]$-factorisation descends to a $\mathbb{Z}[X]$-factorisation; the linear factor then has *integer* coefficients, and matching leading coefficients forces those integers to be $\pm 1$, so the candidate roots are just the *integer* divisors of the constant term. The search becomes finite and elementary. This is the precise justification for the rational root theorem and for the everyday practice of testing $X = \pm 1, \pm 2, \dots$ on a monic integer polynomial. The general lesson: "irreducible over $\mathbb{Q}$" questions should almost always be moved to $\mathbb{Z}[X]$ first, where coefficients are integers and the combinatorics of matching coefficients is rigid — the textbook source makes exactly this remark, noting that working over $\mathbb{Q}$ one gets stuck at $b_0 c_0 = 1$ with $b_0, c_0$ unconstrained, whereas over $\mathbb{Z}$ the equation $b_0 c_0 = 1$ pins $b_0 = \pm 1$.

**"No root" certifies irreducibility only for degrees $2$ and $3$, because only then must a non-trivial factor be linear.** The root search settles $X^3 + X + 1$ because a degree-$3$ polynomial that factors non-trivially *must* have a factor of degree $1$ (the degrees are positive and sum to $3$, so the partition is $1 + 2$) — and a degree-$1$ factor is a root. The same holds for quadratics (partition $1 + 1$). From degree $4$ onward the implication fails: a quartic can split as $2 + 2$ into two irreducible quadratics with *no* linear factor and hence *no* root. So "has no rational root" stops being sufficient for irreducibility at degree $4$ — this is exactly the limitation explored in [[Ex - Reduction modulo a prime as an irreducibility test]], where $X^4 + X + 1$ is irreducible despite the need to also exclude a quadratic-times-quadratic split. The takeaway for spaced practice: when asked to test irreducibility of a concrete polynomial over $\mathbb{Q}$, *first read off the degree*. Degree $2$ or $3$: a root search is complete. Degree $\geq 4$: a root search excludes only linear factors, and you must additionally rule out factorisations into higher-degree pieces, typically by reduction mod a prime or by Eisenstein after a substitution.

**Primitivity is the hypothesis that strips away the "boring" factorisations and makes reducibility over $\mathbb{Z}$ meaningful.** Over $\mathbb{Z}[X]$ the units are only $\pm 1$, so a constant such as $2$ is a *non-unit*, and $2X + 2 = 2 \cdot (X + 1)$ counts as a factorisation into non-units — a reducibility that is an artefact of the constant $2$, not of any genuine polynomial structure. The content $c(f)$ measures exactly this artefact, and demanding $f$ primitive ($c(f)$ a unit) removes it. With primitivity in force, "reducible over $\mathbb{Z}$" can only mean a genuine split into two *positive-degree* factors, which is the same notion as "reducible over $\mathbb{Q}$". This is why every clean statement in this circle of ideas — Gauss's lemma, the descent of factorisations, Eisenstein's criterion — carries the primitivity hypothesis, and why monic polynomials (automatically primitive) are the friendliest inputs. Whenever a theorem about $\mathbb{Z}[X]$ seems to need a hypothesis you have forgotten, "primitive" is the usual missing word, and its job is always the same: discard the factorisations that come from constants so that only the structural ones remain.

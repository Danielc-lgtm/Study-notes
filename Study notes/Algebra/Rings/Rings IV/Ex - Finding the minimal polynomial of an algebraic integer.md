---
type: exercise
subject: ring-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Algebraic Integer and Minimal Polynomial"
  - "Thm - The Minimal Polynomial Generates the Kernel Ideal"
  - "Thm - Eisenstein's Criterion"
  - "Thm - Gauss's Lemma"
  - "Def - Polynomial Ring"
  - "Def - Irreducible and Prime Elements"
tags: [algebra, ring-theory]
---

# Problem Statement

Find the minimal polynomial of $\alpha = \sqrt{2} + \sqrt{3}$ over $\mathbb{Q}$. Concretely: produce the monic polynomial $f_\alpha \in \mathbb{Z}[X]$ of least degree with $f_\alpha(\alpha) = 0$, verify that it has integer coefficients (so that $\alpha$ is an algebraic integer), and verify that it is irreducible over $\mathbb{Q}$ (so that it genuinely is *the* minimal polynomial and not merely *a* vanishing polynomial).

**Recall:**

The setting is the complex number $\alpha = \sqrt{2} + \sqrt{3} \in \mathbb{R} \subset \mathbb{C}$, the [[Def - Polynomial Ring|polynomial ring]] $\mathbb{Z}[X]$, and the notions of [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer and minimal polynomial]].

A complex number $\alpha$ is an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]] when it is a root of some **monic** polynomial in $\mathbb{Z}[X]$ — a polynomial $f = X^n + a_{n-1}X^{n-1} + \cdots + a_0$ with every $a_i \in \mathbb{Z}$ and leading coefficient $1$. The set of polynomials in $\mathbb{Z}[X]$ vanishing at $\alpha$ is the kernel ideal $I = \ker(\varphi)$ of the evaluation homomorphism $\varphi : \mathbb{Z}[X] \to \mathbb{C}$, $g \mapsto g(\alpha)$.

![[Thm - The Minimal Polynomial Generates the Kernel Ideal#Statement]]

So the **minimal polynomial** $f_\alpha$ is the unique irreducible monic generator of $I$; equivalently, it is the monic polynomial of least degree in $I$, and every other polynomial vanishing at $\alpha$ is a multiple of it. To *find* $f_\alpha$ it therefore suffices to (a) exhibit *some* monic integer polynomial vanishing at $\alpha$, and (b) check that polynomial is irreducible — irreducibility upgrades "a vanishing polynomial" to "the minimal one", because any proper monic factor would be a lower-degree element of $I$.

[[Thm - Gauss's Lemma|Gauss's lemma]] and [[Thm - Eisenstein's Criterion|Eisenstein's criterion]] are the tools for step (b): Gauss's lemma lets an irreducibility question over $\mathbb{Q}$ be settled inside $\mathbb{Z}[X]$, and Eisenstein certifies irreducibility from a single prime dividing the lower coefficients but not the leading one nor (squared) the constant.

---

# Convergent Strategy

**Problem class.** This is a *construct-the-minimal-polynomial* problem: given an explicit algebraic number built from radicals, produce its minimal polynomial. The [[Rings IV — §2.7–2.8]] strategy records that such problems are solved not by guessing the polynomial but by *eliminating the radicals* — repeatedly isolating a surd and squaring until no surds remain. The degree of the answer is then read off, and irreducibility is the final certificate.

**Assumption pattern.** The load-bearing feature is that $\alpha$ is a sum of two square roots, $\sqrt{2}$ and $\sqrt{3}$. Each square root satisfies a degree-$2$ relation ($(\sqrt2)^2 = 2$), so each squaring step removes one surd, and two surds suggest a degree-$4$ answer. The number $\alpha$ lies in the field $\mathbb{Q}(\sqrt2, \sqrt3)$, which has degree $4$ over $\mathbb{Q}$ — this is the structural reason the minimal polynomial has degree $4$, though we will not need field theory to find it.

**Theorem routing.** The radical-elimination computation produces a candidate monic integer polynomial $f$ of degree $4$. To confirm $f$ is *the* minimal polynomial we must show it is irreducible over $\mathbb{Q}$. The route: [[Thm - The Minimal Polynomial Generates the Kernel Ideal]] says the minimal polynomial is the irreducible monic generator of the kernel ideal, so a monic *irreducible* integer polynomial vanishing at $\alpha$ is automatically $f_\alpha$. Irreducibility of the degree-$4$ candidate is established by ruling out both linear factors (no rational root) and a quadratic-times-quadratic split (a short coefficient-matching argument); [[Thm - Gauss's Lemma|Gauss's lemma]] legitimises doing this over $\mathbb{Z}$.

**Key decision point.** The non-obvious move is *which* quantity to isolate before each squaring. Squaring $\alpha = \sqrt2 + \sqrt3$ directly gives $\alpha^2 = 5 + 2\sqrt6$ — note the two surds have *collapsed into one*, $\sqrt6$, because $\sqrt2\cdot\sqrt3 = \sqrt6$. One must then isolate that single remaining surd, $\alpha^2 - 5 = 2\sqrt6$, before squaring again. Squaring at the wrong moment — for instance squaring $\alpha^2 = 5 + 2\sqrt6$ without first moving the $5$ across — reintroduces cross terms and does not terminate. The discipline is: *after each squaring, collect all rational terms on one side and all surd terms on the other, then square again.*

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings IV — §2.7–2.8#Legal Operations|the topic page's Legal Operations]]:

1. **Eliminate a radical by isolate-and-square.** Move every rational term to one side of an equation, leaving a pure surd (or surd multiple) on the other, then square both sides. Each application removes one layer of radical and is the engine of the whole computation.

2. **Collect a product of surds.** Recognise $\sqrt{a}\,\sqrt{b} = \sqrt{ab}$, so that $\sqrt2\cdot\sqrt3$ becomes the *single* surd $\sqrt6$. This is what makes the two-surd problem collapse to a one-surd problem after the first squaring.

3. **Expand $(x \pm y)^2 = x^2 \pm 2xy + y^2$.** The binomial expansion is applied with $x, y$ themselves involving radicals; the cross term $2xy$ is where the surviving surd lives.

4. **Read off monicity and integrality of coefficients.** Inspect the resulting polynomial: leading coefficient $1$ (monic) and every coefficient in $\mathbb{Z}$ — this is exactly the certificate that $\alpha$ is an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]].

5. **Certify irreducibility by excluding factor shapes.** For a quartic, a non-trivial factorisation over $\mathbb{Q}$ (equivalently, by [[Thm - Gauss's Lemma|Gauss's lemma]], over $\mathbb{Z}$) is either $1+3$ (a rational root) or $2+2$ (two quadratics). Rule out each shape.

6. **Run a finite rational root search.** For a monic integer polynomial, any rational root is an integer dividing the constant term — here only $\pm 1$ need be tested.

---

# Hints

> [!note]- Hint 1
> Do not try to guess the polynomial. Set $\alpha = \sqrt2 + \sqrt3$ and *square it*. The goal of squaring is to make the radicals disappear; you will not get there in one step, but each squaring removes one radical, so plan on squaring twice.

> [!note]- Hint 2
> Squaring gives $\alpha^2 = (\sqrt2 + \sqrt3)^2 = 2 + 2\sqrt2\sqrt3 + 3$. Simplify the cross term using $\sqrt2\sqrt3 = \sqrt6$. You should land on $\alpha^2 = 5 + 2\sqrt6$ — a *single* surd remains. Now isolate that surd: put the rational part on the other side.

> [!note]- Hint 3
> From $\alpha^2 - 5 = 2\sqrt6$, square both sides. The left side becomes $(\alpha^2-5)^2$, the right side becomes $4 \cdot 6 = 24$ — and now there are no surds at all. Expand $(\alpha^2 - 5)^2$ and rearrange into a polynomial equation $f(\alpha) = 0$ with $f$ monic in $\mathbb{Z}[X]$.

> [!note]- Hint 4
> You should obtain $f = X^4 - 10X^2 + 1$. To confirm it is *the* minimal polynomial, show it is irreducible over $\mathbb{Q}$. A quartic factors non-trivially as either a linear times a cubic — excluded by checking $\pm 1$ are not roots — or as two quadratics $(X^2 + aX + b)(X^2 + cX + d)$ with $a,b,c,d \in \mathbb{Z}$ (Gauss's lemma permits integer coefficients). Match coefficients: the absence of an $X^3$ term forces $c = -a$, and the absence of an $X$ term then forces $a(d - b) = 0$. Split into the cases $a = 0$ and $b = d$ and derive a contradiction in each.

---

# Solution

The strategy is pure radical elimination: square once to collapse $\sqrt2, \sqrt3$ into the single surd $\sqrt6$, isolate it, square again to remove it entirely, and rearrange. The resulting quartic is monic with integer coefficients, certifying $\alpha$ as an algebraic integer; a two-case factor-shape argument certifies it irreducible, hence minimal.

**Step 1: First squaring — collapse two surds into one.**

Squaring $\alpha = \sqrt2 + \sqrt3$ gives
$$\alpha^2 = 5 + 2\sqrt6.$$
The two independent surds $\sqrt2, \sqrt3$ have merged into the single surd $\sqrt6$.

> [!note]- Derivation
> Apply the binomial expansion $(x+y)^2 = x^2 + 2xy + y^2$ with $x = \sqrt2$, $y = \sqrt3$:
> $$\alpha^2 = (\sqrt2 + \sqrt3)^2 = (\sqrt2)^2 + 2\,\sqrt2\,\sqrt3 + (\sqrt3)^2 = 2 + 2\sqrt2\sqrt3 + 3.$$
> The cross term simplifies by $\sqrt{a}\sqrt{b} = \sqrt{ab}$: $\sqrt2\,\sqrt3 = \sqrt6$. The two rational terms combine, $2 + 3 = 5$. Hence
> $$\alpha^2 = 5 + 2\sqrt6.$$
> This is the crucial collapse: a sum of *two* square roots, once squared, produces a number of the form (rational) $+$ (rational)$\cdot$(*one* square root), because the cross term is the product of the two original surds.

**Step 2: Isolate the surviving surd and square again.**

Rearranging to $\alpha^2 - 5 = 2\sqrt6$ and squaring eliminates the last radical:
$$(\alpha^2 - 5)^2 = 24.$$

> [!note]- Derivation
> From Step 1, $\alpha^2 = 5 + 2\sqrt6$. Move the rational term to the left so that the right-hand side is a *pure* surd multiple:
> $$\alpha^2 - 5 = 2\sqrt6.$$
> Squaring both sides — the left becomes $(\alpha^2-5)^2$, the right becomes $(2\sqrt6)^2 = 2^2 (\sqrt6)^2 = 4 \cdot 6 = 24$:
> $$(\alpha^2 - 5)^2 = 24.$$
> There is now no radical anywhere. The reason this works in exactly two squarings: the first squaring reduced two surds to one, and the second squaring removes that one. Isolating the surd *before* squaring is essential — squaring $\alpha^2 = 5 + 2\sqrt6$ as it stands would give $\alpha^4 = 25 + 20\sqrt6 + 24$, still carrying $\sqrt6$.

**Step 3: Rearrange into a monic integer polynomial.**

Expanding $(\alpha^2 - 5)^2 = 24$ and collecting all terms on one side gives $f(\alpha) = 0$ with
$$f = X^4 - 10X^2 + 1 \in \mathbb{Z}[X], \qquad f \text{ monic.}$$

> [!note]- Derivation
> Expand the left side of $(\alpha^2 - 5)^2 = 24$ using $(u - 5)^2 = u^2 - 10u + 25$ with $u = \alpha^2$:
> $$(\alpha^2 - 5)^2 = (\alpha^2)^2 - 10\,\alpha^2 + 25 = \alpha^4 - 10\alpha^2 + 25.$$
> So the equation reads $\alpha^4 - 10\alpha^2 + 25 = 24$. Subtracting $24$ from both sides:
> $$\alpha^4 - 10\alpha^2 + 1 = 0.$$
> Therefore $\alpha$ is a root of
> $$f = X^4 - 10X^2 + 1.$$
> Inspect the coefficients: $f = 1\cdot X^4 + 0\cdot X^3 + (-10)X^2 + 0\cdot X + 1$. The leading coefficient is $1$, so $f$ is **monic**; every coefficient $1, 0, -10, 0, 1$ lies in $\mathbb{Z}$, so $f \in \mathbb{Z}[X]$. By the definition of an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]] — a root of a monic polynomial in $\mathbb{Z}[X]$ — this already proves $\alpha = \sqrt2 + \sqrt3$ is an algebraic integer.

**Step 4: $f$ is irreducible over $\mathbb{Q}$ — no linear factor.**

$f$ has no rational root: the only candidates are $\pm 1$, and $f(\pm 1) = -8 \neq 0$. So $f$ has no factor of degree $1$ over $\mathbb{Q}$.

> [!note]- Derivation
> By [[Thm - Gauss's Lemma|Gauss's lemma]], a monic integer polynomial is reducible over $\mathbb{Q}$ if and only if it factors into lower-degree polynomials over $\mathbb{Z}$; in particular a rational root would have to be an *integer* root, and (the polynomial being monic) an integer root divides the constant term $1$. The only integers dividing $1$ are $\pm 1$. Evaluate:
> $$f(1) = 1 - 10 + 1 = -8, \qquad f(-1) = 1 - 10 + 1 = -8.$$
> ($f$ is even in $X$, so $f(1) = f(-1)$.) Neither is $0$, so $f$ has no root in $\mathbb{Q}$, hence no degree-$1$ factor over $\mathbb{Q}$. This rules out the factor shape $1 + 3$ (linear $\times$ cubic).

**Step 5: $f$ is irreducible over $\mathbb{Q}$ — no quadratic factor.**

A factorisation $f = (X^2 + aX + b)(X^2 + cX + d)$ with integer $a,b,c,d$ is impossible: matching coefficients forces $c = -a$ and then leads to a contradiction in both the case $a = 0$ and the case $a \neq 0$.

> [!note]- Derivation
> The only remaining non-trivial factor shape for a quartic is $2 + 2$. By [[Thm - Gauss's Lemma|Gauss's lemma]] we may assume both quadratic factors lie in $\mathbb{Z}[X]$, and since $f$ is monic we may take both factors monic. Suppose
> $$X^4 - 10X^2 + 1 = (X^2 + aX + b)(X^2 + cX + d), \qquad a,b,c,d \in \mathbb{Z}.$$
> Expand the right-hand side:
> $$X^4 + (a+c)X^3 + (b + d + ac)X^2 + (ad + bc)X + bd.$$
> Matching coefficients with $X^4 + 0\cdot X^3 - 10 X^2 + 0\cdot X + 1$:
> - $X^3$: $\quad a + c = 0 \implies c = -a$.
> - $X^0$: $\quad bd = 1 \implies (b,d) = (1,1) \text{ or } (b,d) = (-1,-1)$, since $b,d \in \mathbb{Z}$.
> - $X^1$: $\quad ad + bc = 0$. Substituting $c = -a$: $\;ad - ab = a(d - b) = 0$.
> - $X^2$: $\quad b + d + ac = -10$. Substituting $c = -a$: $\;b + d - a^2 = -10$.
>
> The $X^1$ equation $a(d-b) = 0$ splits into two cases.
>
> *Case $a = 0$.* Then $c = -a = 0$, and the $X^2$ equation becomes $b + d = -10$. But from $bd = 1$ we have $(b,d) = (1,1)$ giving $b + d = 2$, or $(b,d) = (-1,-1)$ giving $b + d = -2$. Neither equals $-10$. Contradiction.
>
> *Case $d = b$.* Then $bd = b^2 = 1$, so $b = \pm 1$ and $d = b$. The $X^2$ equation $b + d - a^2 = -10$ becomes $2b - a^2 = -10$, i.e. $a^2 = 2b + 10$. If $b = 1$: $a^2 = 12$, not a perfect square. If $b = -1$: $a^2 = 8$, not a perfect square. In either subcase $a$ would not be an integer. Contradiction.
>
> Both cases are impossible, so no integer factorisation into two quadratics exists. Combined with Step 4, $f$ has no non-trivial factorisation over $\mathbb{Z}$, hence (Gauss's lemma) none over $\mathbb{Q}$: $f = X^4 - 10X^2 + 1$ is **irreducible over $\mathbb{Q}$**.

**Step 6: Conclude that $f$ is the minimal polynomial.**

$f = X^4 - 10X^2 + 1$ is monic, lies in $\mathbb{Z}[X]$, vanishes at $\alpha$, and is irreducible. By the structure theorem for the kernel ideal it is therefore *the* minimal polynomial of $\alpha = \sqrt2 + \sqrt3$.

> [!note]- Derivation
> [[Thm - The Minimal Polynomial Generates the Kernel Ideal]] states that the kernel ideal $I = \ker(\varphi : \mathbb{Z}[X] \to \mathbb{C},\; g \mapsto g(\alpha))$ is principal, generated by an irreducible monic polynomial $f_\alpha$, and that $f_\alpha$ is the polynomial of least degree in $I$. We have produced a polynomial $f$ that is monic, integer, irreducible, and satisfies $f(\alpha) = 0$, i.e. $f \in I$.
>
> Because $f \in I = (f_\alpha)$, we may write $f = f_\alpha \cdot g$ for some $g \in \mathbb{Z}[X]$. Since $f$ is *irreducible* and $f_\alpha$ is not a unit (it has degree $\geq 1$), the factor $g$ must be a unit of $\mathbb{Z}[X]$, namely $g = \pm 1$. Both $f$ and $f_\alpha$ are monic, so $g = +1$. Hence $f = f_\alpha$:
> $$f_\alpha = X^4 - 10X^2 + 1.$$
> The minimal polynomial of $\sqrt2 + \sqrt3$ over $\mathbb{Q}$ is $X^4 - 10X^2 + 1$, and in particular $\sqrt2 + \sqrt3$ is an algebraic integer of degree $4$.

> [!note]- Complete formal solution
> **Claim.** The minimal polynomial of $\alpha = \sqrt2 + \sqrt3$ over $\mathbb{Q}$ is $f_\alpha = X^4 - 10X^2 + 1$, and $\alpha$ is an algebraic integer.
>
> *Finding a vanishing polynomial.* Squaring,
> $$\alpha^2 = (\sqrt2 + \sqrt3)^2 = 2 + 2\sqrt6 + 3 = 5 + 2\sqrt6,$$
> using $\sqrt2\sqrt3 = \sqrt6$. Isolating the surd, $\alpha^2 - 5 = 2\sqrt6$, and squaring again,
> $$(\alpha^2 - 5)^2 = (2\sqrt6)^2 = 24.$$
> Expanding the left side, $\alpha^4 - 10\alpha^2 + 25 = 24$, so $\alpha^4 - 10\alpha^2 + 1 = 0$. Thus $\alpha$ is a root of $f = X^4 - 10X^2 + 1$, which is monic with coefficients in $\mathbb{Z}$; by definition $\alpha$ is an algebraic integer.
>
> *Irreducibility of $f$ over $\mathbb{Q}$.* By Gauss's lemma it suffices to show $f$ has no non-trivial factorisation in $\mathbb{Z}[X]$, with all factors monic since $f$ is monic.
>
> No linear factor: a rational root would be an integer dividing the constant term $1$, hence $\pm 1$; but $f(1) = f(-1) = 1 - 10 + 1 = -8 \neq 0$.
>
> No two-quadratic factorisation: suppose $f = (X^2 + aX + b)(X^2 + cX + d)$ with $a,b,c,d \in \mathbb{Z}$. Expanding and matching coefficients of $X^4 - 10X^2 + 1$ gives $a + c = 0$, $bd = 1$, $ad + bc = 0$, $b + d + ac = -10$. From the first, $c = -a$; the third becomes $a(d-b) = 0$. If $a = 0$ then $b + d = -10$, contradicting $bd = 1$ (which forces $b + d = \pm 2$). If $d = b$ then $b^2 = 1$ and $2b - a^2 = -10$, giving $a^2 = 12$ or $a^2 = 8$, neither a perfect square. Both cases are impossible.
>
> Hence $f$ is irreducible over $\mathbb{Q}$. Since $f$ is a monic irreducible integer polynomial vanishing at $\alpha$, and the kernel ideal $\ker(\varphi)$ is generated by the irreducible monic minimal polynomial $f_\alpha$ with $f$ a multiple of $f_\alpha$, irreducibility of $f$ forces $f = f_\alpha$. Therefore $f_\alpha = X^4 - 10X^2 + 1$. $\blacksquare$

---

# Key Takeaways

**To find the minimal polynomial of a number built from radicals, eliminate the radicals by isolate-and-square — never guess the polynomial.** The reliable algorithm for "$\alpha$ is an explicit expression in $\sqrt{\cdot}$, find its minimal polynomial" is mechanical: write $\alpha = (\text{expression})$, move every rational term to one side so the other side is a pure surd or surd combination, square, and repeat. Each squaring strictly reduces the radical content, so the process terminates, and it terminates in a polynomial equation $f(\alpha) = 0$. The trigger is the *shape* of $\alpha$ — any time the number is presented as a finite arithmetic combination of radicals, this is the move. The same technique finds the minimal polynomial of $\sqrt[3]{2}$ (cube both sides of $\alpha = \sqrt[3]2$ to get $\alpha^3 = 2$, so $f = X^3 - 2$), of $\sqrt2 + \sqrt[3]2$ (more squarings and cubings, landing on a degree-$6$ polynomial), and of $\sqrt{1 + \sqrt2}$ (square to get $\alpha^2 = 1 + \sqrt2$, isolate and square again, giving $X^4 - 2X^2 - 1$). The discipline that makes it work is *isolation before squaring*: collect rationals on one side, surds on the other, every single time.

**Counting independent surds predicts the degree, and the cross term is where surds collapse.** Before computing, one can anticipate that $\sqrt2 + \sqrt3$ will have a degree-$4$ minimal polynomial: there are two independent square roots, each contributing a "factor of $2$" to the degree, and $2 \times 2 = 4$. The structural statement behind this heuristic is that $\alpha$ lives in the field $\mathbb{Q}(\sqrt2,\sqrt3)$, of degree $4$ over $\mathbb{Q}$, and the minimal polynomial degree divides — here equals — that field degree. What the computation makes visible is *why* two surds do not produce eight or sixteen terms of mess: when you square $\sqrt2 + \sqrt3$, the cross term is $2\sqrt2\sqrt3 = 2\sqrt6$, so the two surds *fuse* into one new surd. Squaring a sum of $k$ independent surds always behaves this way — the rational squares drop out, and the surviving irrational part is a sum of cross-term surds, fewer and "deeper" — which is the inductive reason the process terminates. Recognising this lets you predict, before grinding through the algebra, both the degree of the answer and the number of squarings needed.

**Producing a vanishing polynomial is only half the job; irreducibility is what makes it *minimal*.** A persistent error is to stop at Step 3 — "$\alpha$ satisfies $X^4 - 10X^2 + 1$, done." But the radical-elimination process only guarantees *a* monic integer polynomial vanishing at $\alpha$; it could in principle be a proper multiple of the true minimal polynomial. (If you had carelessly squared an extra time you might have produced $X^8 - 20X^6 + \cdots$, which also vanishes at $\alpha$ but is not minimal.) The minimal polynomial is characterised, via [[Thm - The Minimal Polynomial Generates the Kernel Ideal]], as the *irreducible* monic generator of the kernel ideal — so the certificate that your candidate is minimal is exactly its irreducibility. The general workflow for any minimal-polynomial problem is therefore two-phase: **phase 1**, eliminate radicals to get a vanishing monic integer polynomial; **phase 2**, prove that polynomial irreducible. Skipping phase 2 answers a different (weaker) question.

**For a quartic, irreducibility means excluding exactly two factor shapes: $1+3$ and $2+2$.** A degree-$4$ polynomial factors non-trivially over a field if and only if its degree partitions non-trivially, and the partitions of $4$ into parts $\geq 1$, modulo order, are $1+3$, $2+2$, $1+1+2$, $1+1+1+1$. But any partition containing a $1$ means a linear factor, hence a root — so *all* root-containing partitions are killed at once by a single rational root search. That leaves only $2+2$. This is the reason a quartic irreducibility proof is always two steps ("no rational root" then "no two-quadratic split"), and it is precisely why "has no rational root" is *insufficient* for irreducibility from degree $4$ upward — the warning made concrete in [[Ex - Reduction modulo a prime as an irreducibility test]]. The transferable principle: to prove a degree-$n$ polynomial irreducible by elementary means, enumerate the partitions of $n$; a rational root search disposes of every partition with a $1$, and you must separately exclude each partition into parts all $\geq 2$. For $n = 4$ that is the lone shape $2+2$; for $n = 6$ it would be $2+2+2$, $2+4$, $3+3$. The coefficient-matching argument in Step 5 — derive $c = -a$ from the missing $X^3$ term, then $a(d-b) = 0$ from the missing $X$ term, then split into cases — is the standard mechanism for excluding a $2+2$ split, and works whenever the target polynomial is *even* (only even powers of $X$), which forces the helpful symmetry $c = -a$.

**Monic gives "algebraic integer" for free; the squaring algorithm preserves monicity automatically.** Note that we never had to *work* to make the answer monic — the radical-elimination process, starting from $\alpha$ raised to the highest power and rearranging, naturally yields a polynomial whose leading term is $X^{\deg}$ with coefficient $1$. This is a small but reusable observation: the algorithm certifies the algebraic-integer property as a byproduct, because an algebraic integer is exactly a root of a monic integer polynomial, and the output is always monic with integer coefficients (the coefficients are integers because $\alpha$ was built from integers under $+, -, \times$ and surds of integers). Contrast this with the next exercise, [[Ex - Deciding whether a number is an algebraic integer]], where the candidate $\tfrac12(1+\sqrt3)$ has a *non-integral* minimal polynomial $X^2 - X - \tfrac12$ — there the squaring algorithm produces a monic polynomial with a *rational, non-integer* coefficient, and that is the signal that the number fails to be an algebraic integer. So the algorithm does double duty: it computes the minimal polynomial *and*, by whether the coefficients land in $\mathbb{Z}$, decides the algebraic-integer question.

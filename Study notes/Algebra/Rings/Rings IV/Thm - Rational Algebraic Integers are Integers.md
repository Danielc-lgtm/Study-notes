---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Algebraic Integer and Minimal Polynomial"
  - "Def - Polynomial Ring"
  - "Def - Integral Domain"
  - "Def - Irreducible and Prime Elements"
  - "Thm - The Minimal Polynomial Generates the Kernel Ideal"
  - "Thm - Gauss's Lemma"
tags: [algebra, ring-theory]
---

# Notation

We work with $\mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{C}$. An [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]] is a complex number that is a root of a **monic** polynomial in $\mathbb{Z}[X]$ — a polynomial $X^n + c_{n-1}X^{n-1} + \cdots + c_0$ with all $c_i \in \mathbb{Z}$. For an algebraic integer $\alpha$, $f_\alpha \in \mathbb{Z}[X]$ denotes its [[Def - Algebraic Integer and Minimal Polynomial|minimal polynomial]] — the monic generator of $\ker(\varphi : \mathbb{Z}[X] \to \mathbb{C},\ g \mapsto g(\alpha))$, which is monic and [[Def - Irreducible and Prime Elements|irreducible]] in $\mathbb{Z}[X]$. We use both [[Def - Polynomial Ring|polynomial rings]] $\mathbb{Z}[X]$ and $\mathbb{Q}[X]$, with $\mathbb{Z}[X] \subseteq \mathbb{Q}[X]$. A polynomial is **irreducible** in a ring $S[X]$ if it is a non-unit, non-zero, and cannot be written as a product of two non-units of $S[X]$. We say a subring $A$ of a ring $B$ is **integrally closed in $B$** if every element of $B$ that is a root of a monic polynomial over $A$ already lies in $A$. The full chapter symbol registry is on [[Rings IV — §2.7–2.8]].

---

# Statement

> **Lemma.** Let $\alpha \in \mathbb{Q}$ be a rational number that is also an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]]. Then $\alpha \in \mathbb{Z}$.

Stated the other way round: a rational number is an algebraic integer **only if** it is an ordinary integer. The two notions of "integer" — the elementary $\mathbb{Z}$ and the polynomial-theoretic "algebraic integer" — agree on $\mathbb{Q}$, with no rational fractions slipping in. In the vocabulary introduced above, the lemma says:
$$\mathbb{Z} \text{ is integrally closed in } \mathbb{Q}.$$

---

# Motivation

The definition of an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]] is a leap of abstraction. We had a perfectly serviceable notion of integer — the elements of $\mathbb{Z}$ — and we replaced it by something far more permissive: any complex number satisfying a monic integer-coefficient polynomial. The new notion was *designed* to admit numbers like $i$ and $\sqrt2$ that the old one missed. But a definition that widens a concept owes a debt: it must not accidentally widen it *where we did not want it widened*. The old integers must survive intact as a special case.

Here is the precise worry. The number $\tfrac12$ is rational, and it is an *algebraic number* — a root of $2X - 1$. Could it sneak in as an algebraic *integer*? If some monic polynomial $X^n + c_{n-1}X^{n-1} + \cdots + c_0 \in \mathbb{Z}[X]$ had $\tfrac12$ as a root, then $\tfrac12$ would qualify, and the new notion of "integer" would contain a genuine fraction. That would be a disaster for the analogy "algebraic integers are to algebraic numbers as $\mathbb{Z}$ is to $\mathbb{Q}$". The whole point of the monic condition was to forbid denominators; if denominators reappeared inside $\mathbb{Q}$, the condition would have failed at the one place we can most easily check it.

This lemma is the reassurance. It says the worry is unfounded: a rational algebraic integer is forced to be an honest integer. The new definition, restricted to $\mathbb{Q}$, gives back exactly $\mathbb{Z}$ — not $\mathbb{Z}$ plus stray fractions. The leap of abstraction is *consistent* with the ground it left behind.

Why should one expect this to be true? Because there is a classical shadow of it: the **rational root theorem**, which says any rational root $p/q$ (in lowest terms) of an integer polynomial has $q$ dividing the leading coefficient. For a *monic* polynomial the leading coefficient is $1$, so $q$ divides $1$, so $q = \pm 1$, so the root is an integer. The lemma is exactly this, and the elegance of the abstract proof is that it does not even need to invoke the rational root theorem as a separate fact — it gets the same conclusion from [[Thm - Gauss's Lemma|Gauss's lemma]] and the structure of the minimal polynomial, which is the more conceptual route and the one that generalises.

The deeper framing — and the one to remember — is *integral closure*. A subring $A \subseteq B$ is **integrally closed** in $B$ when no element of $B$ outside $A$ satisfies a monic polynomial over $A$: the monic-root operation does not escape $A$. This lemma says $\mathbb{Z}$ is integrally closed in $\mathbb{Q}$. It is the prototype of a property that, when it holds for a ring's *own* field of fractions, marks that ring as "saturated" — already containing everything it morally should. Rings of integers of number fields have it; unique factorisation domains have it; and recognising integral closure as the right name turns a one-off check into an instance of a structural pattern.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis $A$ is "$\alpha$ is rational *and* an algebraic integer". The recognition skill is spotting these two facts when they are not announced together.

A first disguised source is **"$\alpha$ is a rational eigenvalue of an integer matrix"**. The property $B$: $\alpha \in \mathbb{Q}$ is an eigenvalue of a matrix $M$ with integer entries. The characteristic polynomial $\det(XI - M)$ is monic over $\mathbb{Z}$ and vanishes at $\alpha$, so $\alpha$ is an algebraic integer; together with $\alpha \in \mathbb{Q}$ the lemma applies and forces $\alpha \in \mathbb{Z}$. The bridge $B \Rightarrow A$ is non-obvious: it is not visually apparent that "rational eigenvalue of an integer matrix" is the same hypothesis as the lemma's. *Example problem:* show that the only possible rational eigenvalues of an integer matrix are integers — useful in proving certain matrices have no rational eigenvalues at all.

A second disguised source is **"$\alpha$ is a value built from algebraic integers by ring operations, and happens to be rational"**. The property $B$: $\alpha$ is, say, $\zeta + \zeta^{-1}$ for a root of unity $\zeta$, or a trace $\sum \zeta_i$ of conjugate algebraic integers, and one knows (from [[Thm - The Algebraic Integers Form a Subring|the subring theorem]]) such a combination is itself an algebraic integer; if it is moreover rational, the lemma pins it to $\mathbb{Z}$. The non-obviousness is that one must first certify $\alpha$ as an algebraic integer via closure under $+$ and $\times$, *then* observe rationality. *Example problem:* prove that $2\cos(2\pi/n)$, which is rational only for a few small $n$, takes integer values exactly at those $n$.

A third disguised source is **"$\alpha$ is a root of a monic integer polynomial of any degree, presented as a fixed point or period"**. Property $B$: $\alpha = T^k(\alpha)$ for an integer-coefficient polynomial map $T$, so $\alpha$ solves a monic integer relation; if $\alpha$ is known to be rational, it must be an integer. Non-obvious because the dynamical packaging hides the monic polynomial. *Example problem:* the rational periodic points of a monic integer-coefficient polynomial map are integers.

**Targets (Output Amplification)**

The conclusion $C$ is "$\alpha \in \mathbb{Z}$".

Combine $C$ with **a denominator visible in $\alpha$ to derive a contradiction**. If $\alpha$ is presented as a fraction $p/q$ with $q \neq \pm1$ in lowest terms, then $C$ — which says $\alpha \in \mathbb{Z}$ — is *false*, so the hypothesis must fail: $\alpha$ is **not** an algebraic integer. The further result $E$ is a non-integrality certificate: any explicitly non-integer rational is thereby proved to satisfy *no* monic integer polynomial. This is non-obvious because it converts the lemma into a tool for proving a *negative* — that a polynomial relation cannot exist — from the mere visible presence of a denominator.

Combine $C$ with **the rational root theorem in reverse, to constrain factorisations**. If a monic integer polynomial $f$ has a rational root $\alpha$, then $C$ forces $\alpha \in \mathbb{Z}$, and moreover $\alpha$ divides the constant term of $f$ (evaluate the monic relation modulo $\alpha$). The further result $E$ is a finite list of candidate rational roots — the integer divisors of the constant term — turning "does $f$ have a rational root" into a finite check. Non-obvious because the lemma silently collapses an infinite search over $\mathbb{Q}$ into a finite search over divisors in $\mathbb{Z}$.

Combine $C$ with **the structural slogan "$\mathbb{Z}$ is integrally closed in $\mathbb{Q}$"** to recognise saturation. The further result $E$: whenever a ring $A$ is known to be a unique factorisation domain, the same proof pattern shows $A$ is integrally closed in $\operatorname{Frac}(A)$, so $A$ is "saturated" — it already contains every element of its fraction field integral over it. Non-obvious because it elevates a fact about $\mathbb{Z}$ to a property diagnosable for any UFD, and integral closure is the hypothesis under which much of algebraic number theory (Dedekind domains, normalisation) is built.

---

# Why Is It True

The cleanest intuition is this: a rational number that is an algebraic integer satisfies a polynomial relation that is *both* monic *and* of degree exactly $1$ — and a monic degree-$1$ integer polynomial is just $X - n$ for an integer $n$, whose only root is $n$.

Unpack why the relevant polynomial is degree $1$. Because $\alpha$ is rational, the *honest* relation it satisfies is utterly simple: $\alpha$ is a root of $X - \alpha$, a linear polynomial. There is no algebraic complexity in a rational number — it does not need a quadratic or higher relation to be captured, the way $\sqrt2$ needs $X^2 - 2$. The [[Def - Algebraic Integer and Minimal Polynomial|minimal polynomial]] $f_\alpha$ is, by construction, the smallest-degree relation, and over the rationals the smallest-degree relation for a rational $\alpha$ has degree $1$.

But here is the subtlety the proof must handle. The minimal polynomial $f_\alpha$ is defined with **integer** coefficients — it generates the kernel inside $\mathbb{Z}[X]$. A priori, $f_\alpha$ could be a high-degree integer polynomial; the fact that $\alpha$ also satisfies the low-degree *rational* polynomial $X - \alpha$ does not, on its face, tell us $f_\alpha$ itself is linear, because $X - \alpha$ has non-integer coefficients when $\alpha \notin \mathbb{Z}$ and so is not obviously available inside $\mathbb{Z}[X]$.

This is exactly the gap [[Thm - Gauss's Lemma|Gauss's lemma]] closes. By [[Thm - The Minimal Polynomial Generates the Kernel Ideal|the proposition on the minimal polynomial]], $f_\alpha$ is **irreducible in $\mathbb{Z}[X]$**, and $f_\alpha$ is monic, hence primitive. Gauss's lemma says a primitive polynomial is irreducible in $\mathbb{Z}[X]$ if and only if it is irreducible in $\mathbb{Q}[X]$. So $f_\alpha$ is irreducible in the larger ring $\mathbb{Q}[X]$ too. Now bring in the rational root: in $\mathbb{Q}[X]$, the polynomial $X - \alpha$ — a genuine member of $\mathbb{Q}[X]$, since $\alpha \in \mathbb{Q}$ — *divides* $f_\alpha$, because $\alpha$ is a common root and dividing out a known root is a legal operation in $\mathbb{Q}[X]$. An irreducible polynomial that is divisible by the degree-$1$ polynomial $X - \alpha$ must *equal* $X - \alpha$ up to a unit; matching the monic normalisation, $f_\alpha = X - \alpha$.

But $f_\alpha$ has integer coefficients. So $X - \alpha \in \mathbb{Z}[X]$, which forces $\alpha \in \mathbb{Z}$. The chain is: rationality makes $X - \alpha$ a legitimate linear factor over $\mathbb{Q}$; irreducibility of $f_\alpha$ — promoted from $\mathbb{Z}[X]$ to $\mathbb{Q}[X]$ by Gauss — forbids $f_\alpha$ from being anything *bigger* than that factor; and the integrality of $f_\alpha$'s coefficients, true by definition, then drags $\alpha$ into $\mathbb{Z}$.

One can also see the whole thing through the rational root theorem, which is the same argument compressed: write $\alpha = p/q$ in lowest terms; substituting into a monic relation $\alpha^n + c_{n-1}\alpha^{n-1} + \cdots + c_0 = 0$ and clearing the denominator $q^n$ gives $p^n = -q(c_{n-1}p^{n-1} + \cdots + c_0 q^{n-1})$, so $q \mid p^n$; but $\gcd(p,q) = 1$ forces $q \mid 1$, so $q = \pm1$ and $\alpha \in \mathbb{Z}$. The monic-ness is doing the work — it is what makes the leading term $p^n$ carry no factor of $q$, so all the $q$-divisibility is squeezed onto a coprime $p^n$ and collapses.

---

# What Makes This Hard

The hard part is *not* the final step but the realisation that an extra theorem is needed at all: the linear polynomial $X - \alpha$ has rational, non-integer coefficients, so it is *not visibly available* as a factor inside $\mathbb{Z}[X]$, and one cannot directly conclude $f_\alpha$ is linear. The non-obvious move is to promote the irreducibility of $f_\alpha$ from $\mathbb{Z}[X]$ to $\mathbb{Q}[X]$ via [[Thm - Gauss's Lemma|Gauss's lemma]] (valid because $f_\alpha$, being monic, is primitive), and only *then* divide by $X - \alpha$ in $\mathbb{Q}[X]$. The most common error is to work entirely in $\mathbb{Q}[X]$ and forget the punchline — that $f_\alpha$ has *integer* coefficients by definition — which is the single fact that converts $f_\alpha = X - \alpha$ into $\alpha \in \mathbb{Z}$.

---

# Rederivation Scaffold

**High-level strategy:**
Take the minimal polynomial $f_\alpha \in \mathbb{Z}[X]$ of the rational algebraic integer $\alpha$. It is monic and irreducible in $\mathbb{Z}[X]$; being monic it is primitive, so by Gauss's lemma it is irreducible in $\mathbb{Q}[X]$ as well. In $\mathbb{Q}[X]$, the linear polynomial $X - \alpha$ divides $f_\alpha$ (common root $\alpha$). An irreducible polynomial divisible by $X - \alpha$ equals $X - \alpha$ up to a unit; monic normalisation gives $f_\alpha = X - \alpha$. Since $f_\alpha \in \mathbb{Z}[X]$, its coefficients are integers, so $\alpha \in \mathbb{Z}$.

**Subgoal decomposition:**

1. **The minimal polynomial exists and is monic, irreducible in $\mathbb{Z}[X]$.** Invoke that $\alpha$, being an algebraic integer, has a minimal polynomial $f_\alpha$.
   - *Hint:* This is [[Thm - The Minimal Polynomial Generates the Kernel Ideal|the proposition]] that $\ker\varphi = (f_\alpha)$ with $f_\alpha$ monic and irreducible in $\mathbb{Z}[X]$.
   - *Why needed:* Supplies the integer polynomial whose coefficients we will read off at the end; integrality of those coefficients is the crux.

2. **$f_\alpha$ is irreducible in $\mathbb{Q}[X]$.** Promote irreducibility from $\mathbb{Z}[X]$ to $\mathbb{Q}[X]$.
   - *Hint:* $f_\alpha$ is monic, hence primitive; apply [[Thm - Gauss's Lemma|Gauss's lemma]], which says a primitive polynomial is irreducible in $\mathbb{Z}[X]$ iff irreducible in $\mathbb{Q}[X]$.
   - *Why needed:* The factorisation argument happens in $\mathbb{Q}[X]$, where $X - \alpha$ lives; we need irreducibility *there*.

3. **$X - \alpha$ divides $f_\alpha$ in $\mathbb{Q}[X]$.** Show the linear factor is genuinely a factor.
   - *Hint:* $\alpha \in \mathbb{Q}$, so $X - \alpha \in \mathbb{Q}[X]$; since $f_\alpha(\alpha) = 0$, the factor theorem in the Euclidean domain $\mathbb{Q}[X]$ gives $(X-\alpha) \mid f_\alpha$.
   - *Why needed:* Produces a degree-$1$ divisor of $f_\alpha$, which an irreducible polynomial can only tolerate by being that divisor.

4. **Conclude $f_\alpha = X - \alpha$, then $\alpha \in \mathbb{Z}$.** Combine irreducibility with the degree-$1$ divisor.
   - *Hint:* An irreducible $f_\alpha$ divisible by the non-unit $X - \alpha$ equals it up to a unit of $\mathbb{Q}[X]$; both monic forces $f_\alpha = X - \alpha$ exactly. Since $f_\alpha \in \mathbb{Z}[X]$, the constant term $-\alpha$ is an integer.
   - *Why needed:* The integrality of $f_\alpha$'s coefficients is what delivers $\alpha \in \mathbb{Z}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The minimal polynomial of $\alpha$ is monic and irreducible in $\mathbb{Z}[X]$
> **Statement:** A rational algebraic integer $\alpha$ has a minimal polynomial $f_\alpha \in \mathbb{Z}[X]$ that is monic and irreducible in $\mathbb{Z}[X]$.
>
> **Hint:** This is not proved here — it is imported from the structure theorem for the kernel ideal.
>
> **Why needed:** It is the object the whole argument manipulates; in particular its *integer* coefficients are what the conclusion reads off.
>
> > [!note]- Full proof
> > By [[Thm - The Minimal Polynomial Generates the Kernel Ideal|the proposition on the kernel ideal]], for any algebraic integer $\alpha$ the ideal $\ker(\varphi : \mathbb{Z}[X] \to \mathbb{C},\ g \mapsto g(\alpha))$ is principal, generated by a monic, irreducible polynomial $f_\alpha \in \mathbb{Z}[X]$ — the minimal polynomial. A rational $\alpha$ that is an algebraic integer is in particular an algebraic integer, so this applies. $\square$

> [!note]- Lemma 2: $f_\alpha$ is irreducible in $\mathbb{Q}[X]$
> **Statement:** The minimal polynomial $f_\alpha$, irreducible in $\mathbb{Z}[X]$, is also irreducible in $\mathbb{Q}[X]$.
>
> **Hint:** $f_\alpha$ is monic, so its coefficients have greatest common divisor $1$ — it is primitive. Gauss's lemma equates irreducibility of a primitive polynomial across $\mathbb{Z}[X]$ and $\mathbb{Q}[X]$.
>
> **Why needed:** The divisibility-by-$X-\alpha$ argument runs in $\mathbb{Q}[X]$; we need $f_\alpha$ irreducible in that ring, not just in $\mathbb{Z}[X]$.
>
> > [!note]- Full proof
> > Since $f_\alpha$ is monic, its leading coefficient is $1$; any common divisor of all coefficients divides $1$ and is therefore a unit, so $f_\alpha$ is **primitive**. [[Thm - Gauss's Lemma|Gauss's lemma]] states that for $R = \mathbb{Z}$ a unique factorisation domain with field of fractions $\mathbb{Q}$, a primitive polynomial $f \in \mathbb{Z}[X]$ is irreducible in $\mathbb{Z}[X]$ if and only if it is irreducible in $\mathbb{Q}[X]$. By Lemma 1, $f_\alpha$ is irreducible in $\mathbb{Z}[X]$; being primitive, it is therefore irreducible in $\mathbb{Q}[X]$. $\square$

> [!note]- Lemma 3: $X - \alpha$ divides $f_\alpha$ in $\mathbb{Q}[X]$
> **Statement:** Since $\alpha \in \mathbb{Q}$ and $f_\alpha(\alpha) = 0$, the polynomial $X - \alpha$ divides $f_\alpha$ in $\mathbb{Q}[X]$.
>
> **Hint:** The factor theorem: in a polynomial ring over a field, $c$ is a root of $f$ iff $(X - c) \mid f$. Apply it with $c = \alpha$ in $\mathbb{Q}[X]$.
>
> **Why needed:** It exhibits a concrete linear (degree-$1$, non-unit) divisor of $f_\alpha$, which an irreducible polynomial can only have by coinciding with it.
>
> > [!note]- Full proof
> > Because $\alpha \in \mathbb{Q}$, the polynomial $X - \alpha$ has coefficients in $\mathbb{Q}$, so $X - \alpha \in \mathbb{Q}[X]$. The ring $\mathbb{Q}[X]$ is a [[Def - Euclidean Domain|Euclidean domain]]; divide $f_\alpha$ by $X - \alpha$:
> > $$f_\alpha = (X - \alpha)\,q + r, \qquad q, r \in \mathbb{Q}[X], \quad r = 0 \text{ or } \deg r < 1.$$
> > So $r$ is a constant. Evaluating at $X = \alpha$: $\;f_\alpha(\alpha) = (\alpha - \alpha)\,q(\alpha) + r = r$. By Lemma 1, $f_\alpha(\alpha) = 0$ (the minimal polynomial lies in $\ker\varphi$), so $r = 0$. Hence $f_\alpha = (X - \alpha)\,q$, i.e. $(X - \alpha) \mid f_\alpha$ in $\mathbb{Q}[X]$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\alpha \in \mathbb{Q}$ be an [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]].
>
> ---
> **Step 1 — the minimal polynomial.**
> Being an algebraic integer, $\alpha$ has a [[Def - Algebraic Integer and Minimal Polynomial|minimal polynomial]] $f_\alpha \in \mathbb{Z}[X]$: by [[Thm - The Minimal Polynomial Generates the Kernel Ideal|the proposition on the kernel ideal]], $\ker(\varphi : \mathbb{Z}[X] \to \mathbb{C},\ g \mapsto g(\alpha)) = (f_\alpha)$ with $f_\alpha$ **monic** and **irreducible in $\mathbb{Z}[X]$**. In particular $f_\alpha(\alpha) = 0$ and $f_\alpha$ has integer coefficients.
>
> ---
> **Step 2 — irreducibility passes to $\mathbb{Q}[X]$.**
> Since $f_\alpha$ is monic, its leading coefficient $1$ is a common divisor bound: any divisor of all coefficients divides $1$, so $f_\alpha$ is **primitive**. By [[Thm - Gauss's Lemma|Gauss's lemma]] — for the UFD $\mathbb{Z}$ with field of fractions $\mathbb{Q}$, a primitive polynomial is irreducible in $\mathbb{Z}[X]$ if and only if it is irreducible in $\mathbb{Q}[X]$ — the polynomial $f_\alpha$ is irreducible in $\mathbb{Q}[X]$.
>
> ---
> **Step 3 — the linear factor.**
> Because $\alpha \in \mathbb{Q}$, we have $X - \alpha \in \mathbb{Q}[X]$. Dividing in the [[Def - Euclidean Domain|Euclidean domain]] $\mathbb{Q}[X]$, $f_\alpha = (X-\alpha)q + r$ with $r$ constant; evaluating at $\alpha$ gives $r = f_\alpha(\alpha) = 0$. Hence
> $$f_\alpha = (X - \alpha)\,q \qquad \text{in } \mathbb{Q}[X].$$
>
> ---
> **Step 4 — irreducibility forces $f_\alpha = X - \alpha$.**
> The factor $X - \alpha$ has degree $1$, so it is not a unit of $\mathbb{Q}[X]$ (units are the non-zero constants). The polynomial $f_\alpha$ is irreducible in $\mathbb{Q}[X]$ (Step 2): it cannot be written as a product of two non-units. In the factorisation $f_\alpha = (X-\alpha)\,q$, the factor $X - \alpha$ is a non-unit, so $q$ **must** be a unit — a non-zero constant $c \in \mathbb{Q}^\times$. Thus
> $$f_\alpha = c\,(X - \alpha).$$
> Comparing leading coefficients: $f_\alpha$ is monic, so its leading coefficient is $1$; the right-hand side has leading coefficient $c$. Hence $c = 1$ and
> $$f_\alpha = X - \alpha.$$
>
> ---
> **Step 5 — conclude.**
> By Step 1, $f_\alpha \in \mathbb{Z}[X]$ — all its coefficients are integers. By Step 4, $f_\alpha = X - \alpha$, whose constant coefficient is $-\alpha$. Therefore $-\alpha \in \mathbb{Z}$, and so $\alpha \in \mathbb{Z}$. $\blacksquare$
>
> ---
> **Remark — the rational root theorem route.** The same conclusion follows by a direct computation, which is what is "really" happening. Write $\alpha = p/q$ in lowest terms ($\gcd(p,q) = 1$, $q \geq 1$) and let $X^n + c_{n-1}X^{n-1} + \cdots + c_0 \in \mathbb{Z}[X]$ be a monic polynomial with $\alpha$ as a root. Substituting and multiplying through by $q^n$:
> $$p^n + c_{n-1}\,p^{n-1}q + \cdots + c_1\,p\,q^{n-1} + c_0\,q^n = 0.$$
> Every term after the first carries a factor of $q$, so $q \mid p^n$. But $\gcd(p, q) = 1$ implies $\gcd(p^n, q) = 1$, forcing $q \mid 1$, i.e. $q = 1$ and $\alpha = p \in \mathbb{Z}$. The monic hypothesis is exactly what makes the leading term $p^n$ free of any factor of $q$.

---

# Cross-Field Exercise Suggestions

**Rational eigenvalues of integer matrices are integers.** Let $M$ be a matrix with integer entries and $\lambda \in \mathbb{Q}$ an eigenvalue. The characteristic polynomial $\det(XI - M)$ is monic with integer coefficients and has $\lambda$ as a root, so $\lambda$ is a rational algebraic integer; the lemma forces $\lambda \in \mathbb{Z}$. The application is non-obvious because the monic integer polynomial is hidden inside a determinant — recognising the characteristic polynomial as the certificate of integrality is the unwinding step. This is the standard reason an integer matrix with no integer eigenvalue has no rational eigenvalue either.

**Rational periodic points of integer-coefficient dynamics.** For a polynomial map $T : \mathbb{C} \to \mathbb{C}$ with integer coefficients and leading coefficient $1$, a point of period $k$ satisfies $T^k(z) = z$, and $T^k(X) - X$ is monic with integer coefficients. A *rational* periodic point is thus a rational algebraic integer, hence an integer. The application is out-of-distribution because the dynamical framing — orbits, periods — conceals an algebraic-integer hypothesis; only after expanding the iterate $T^k$ does the monic integer relation surface, after which the lemma applies directly.

**Roots of unity that are rational.** A primitive $n$-th root of unity $\zeta$ satisfies $X^n - 1$, monic over $\mathbb{Z}$, so every root of unity is an algebraic integer. The rational roots of unity are exactly $\pm 1$ — and the lemma is one ingredient: a rational root of unity is a rational algebraic integer, hence an integer, and the only integers on the unit circle are $\pm 1$. The application is non-obvious because a question about complex numbers on a circle is settled by integrality, with the lemma supplying the bridge from "rational" to "in $\mathbb{Z}$".

**Trace and norm of algebraic integers landing in $\mathbb{Q}$.** For an algebraic integer $\alpha$ in a number field, its trace and norm (sum and product of conjugates) are rational numbers, and — by [[Thm - The Algebraic Integers Form a Subring|closure of the algebraic integers under ring operations]] — they are themselves algebraic integers. The lemma then forces trace and norm into $\mathbb{Z}$. The application is non-obvious because it chains two results: first certify the symmetric function as an algebraic integer, then use rationality plus this lemma to land it in $\mathbb{Z}$ — which is why characteristic polynomials of algebraic integers have integer coefficients.

---

# Bridges

- **[[Thm - Gauss's Lemma|Gauss's Lemma]]** — the engine of the proof. It is what promotes the irreducibility of $f_\alpha$ from $\mathbb{Z}[X]$ to $\mathbb{Q}[X]$, the ring where the linear factor $X - \alpha$ actually lives. Without Gauss's lemma the argument cannot leave $\mathbb{Z}[X]$, and inside $\mathbb{Z}[X]$ the factor $X - \alpha$ is not visible when $\alpha \notin \mathbb{Z}$.

- **[[Thm - The Minimal Polynomial Generates the Kernel Ideal|The Minimal Polynomial Generates the Kernel Ideal]]** — supplies the minimal polynomial $f_\alpha$ together with the two facts the proof consumes: that $f_\alpha$ is irreducible, and that it has *integer* coefficients. The latter is the punchline.

- **Rational root theorem** — the classical shadow of this lemma. The rational root theorem says a rational root $p/q$ of an integer polynomial has $q$ dividing the leading coefficient; for a monic polynomial this gives $q = \pm1$. The lemma is exactly the monic case, and the Formal Proof's remark gives the rational-root computation directly.

- **[[Def - Unique Factorization Domain|Unique Factorization Domain]]** — the structural generalisation. The slogan "$\mathbb{Z}$ is integrally closed in $\mathbb{Q}$" is an instance of "every UFD is integrally closed in its field of fractions"; the same Gauss's-lemma proof works for any UFD $R$ in place of $\mathbb{Z}$, since Gauss's lemma holds over every UFD.

- **[[Thm - The Algebraic Integers Form a Subring|The Algebraic Integers Form a Subring]]** — a companion result. Where this lemma controls algebraic integers *inside $\mathbb{Q}$*, the subring theorem controls them *under ring operations*; together they say the algebraic integers are a subring $\overline{\mathbb{Z}}$ of $\mathbb{C}$ whose intersection with $\mathbb{Q}$ is precisely $\mathbb{Z}$.

---

# Unlocked by This

> [!tip] $\mathbb{Z}$ is integrally closed in $\mathbb{Q}$ *(from this topic)*
> The lemma is the statement that the ring $\mathbb{Z}$ is **integrally closed** in its field of fractions $\mathbb{Q}$ — no element of $\mathbb{Q}$ outside $\mathbb{Z}$ is a root of a monic integer polynomial. This is the prototype of the integral-closure property.

> [!tip] Integrally closed domains and normalisation *(from Algebraic Number Theory)*
> A domain integrally closed in its fraction field is called **normal**; rings of integers of number fields are normal, and the process of enlarging a non-normal ring to a normal one is *normalisation*. This lemma is the first example, and the same Gauss's-lemma argument shows every [[Def - Unique Factorization Domain|UFD]] is normal. See [[Def - Integrally Closed Domain]].

> [!tip] The rational root test as an irreducibility tool *(from Field Theory)*
> Because a rational root of a monic integer polynomial must be an integer dividing the constant term, checking a monic integer polynomial for rational (hence linear) factors becomes a finite search — a basic step in proving polynomials irreducible over $\mathbb{Q}$ and constructing field extensions.

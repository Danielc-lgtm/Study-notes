---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - Integral Domain"
  - "Def - Unit and Field"
  - "Thm - Integral Extensions and Fields (Domain Criterion)"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be a field and let $B$ be an [[Def - Integral Domain|integral domain]] that is integral over $k$ (every element of $B$ satisfies a monic polynomial over $k$). Prove that $B$ is a field.

Show further by example that the hypothesis that $B$ is a *domain* cannot be dropped: find a $k$-algebra integral over $k$, not a domain, that is not a field. (This is Atiyah–Macdonald Ch. 5, Cor. 5.7.)

**Recall:**

The objects in play are integral extensions, domains, fields, and the domain/field criterion.

![[Def - Integral Element and Integral Extension#The Definition]]

![[Def - Unit and Field#The Definition]]

A ring is a [[Def - Unit and Field|field]] if it is nonzero and every nonzero element is a unit. To prove $B$ is a field, take an arbitrary $0 \neq b \in B$ and produce an inverse.

![[Thm - Integral Extensions and Fields (Domain Criterion)#Statement]]

Over a field $k$, "integral over $k$" and "[[Def - Algebraic Integer and Minimal Polynomial|algebraic]] over $k$" coincide, since any nonzero leading coefficient in $k$ is a unit and can be divided out.

---

# Convergent Strategy

**Problem class.** This is the *minimal-polynomial-inversion* problem at the heart of the field criterion — the direction "$A$ field $\Rightarrow B$ field" of [[Thm - Integral Extensions and Fields (Domain Criterion)]] in its purest case $A = k$. It is the abstract form of the field-theory fact "$k[\alpha] = k(\alpha)$ for algebraic $\alpha$", and it drills operation 7 (read field-ness off the domain criterion) from the [[Commutative Algebra VI — Integral Extensions#Legal Operations|topic page]].

**Assumption pattern.** Two hypotheses, both essential and both used. *Integral over a field $k$* gives every $b$ a monic equation over $k$, with coefficients that are *units* (or zero). *Domain* lets you cancel: it is what forces the minimal-degree equation to have a nonzero constant term. The trigger is "prove a domain integral over a field is a field" — recognise that the minimal monic equation, solved for the constant term, yields the inverse.

**Theorem routing.** The route is direct: take $0 \neq b \in B$, pick its monic equation of *minimal* degree over $k$, argue the constant term $a_n \neq 0$ using the domain property (else cancel $b$ and contradict minimality), then rearrange the equation to express $1$ as $b$ times an element of $B$, using that $a_n \in k$ is invertible (because $k$ is a field). This is Lemma 3 of [[Thm - Integral Extensions and Fields (Domain Criterion)|the domain criterion]].

**Key decision point.** The non-obvious choice is to take the equation of *minimal degree* rather than any monic equation. Only minimality guarantees the nonzero constant term: a non-minimal equation might have $a_n = 0$, leaving nothing to invert. The second decision is recognising *where each hypothesis is used* — the domain property in "minimality forces $a_n \neq 0$", and "$k$ is a field" in "$a_n^{-1}$ exists". Dropping either breaks the proof, and the counterexample $k \times k$ shows the domain hypothesis is genuinely necessary.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VI — Integral Extensions#Legal Operations|the topic page's Legal Operations]]:

1. **Read field-ness off the domain criterion (operation 7).** Apply the "$A$ field $\Rightarrow B$ field" direction with $A = k$.

2. **Take a minimal-degree integral equation.** Among all monic equations for $b$, choose the shortest; this is the analogue of the minimal polynomial.

3. **Use the domain to cancel a factor.** Minimality plus "$B$ is a domain" forces the constant term nonzero.

4. **Invert the constant term in the base field.** Since $a_n \in k^\times$, rearrange to exhibit the inverse of $b$.

---

# Hints

> [!note]- Hint 1
> Take an arbitrary nonzero $b \in B$. It satisfies some monic equation over $k$. You want to solve that equation for an inverse of $b$. Which term of the equation, if you could isolate it, would give you "$b \times (\text{something}) = \text{constant}$"?

> [!note]- Hint 2
> Write the monic equation $b^n + a_1 b^{n-1} + \cdots + a_{n-1}b + a_n = 0$ and rearrange as $b(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}) = -a_n$. If $a_n \neq 0$, you are almost done — $a_n \in k$ is invertible. So the crux is: *why is $a_n \neq 0$?* This is where you must use that $B$ is a domain — and you should pick the equation cleverly.

> [!note]- Hint 3
> Choose the monic equation of *minimal degree*. If $a_n = 0$, factor: $b(b^{n-1} + \cdots + a_{n-1}) = 0$. Since $B$ is a domain and $b \neq 0$, the bracket is $0$ — but that is a monic equation for $b$ of degree $n - 1$, contradicting minimality. Hence $a_n \neq 0$, and $b^{-1} = -a_n^{-1}(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1})$.

> [!note]- Hint 4
> For the counterexample: you need a $k$-algebra integral over $k$ but not a domain and not a field. The smallest such is a product of two copies of $k$. Check $k \times k$ is integral over $k$ (each element satisfies a monic), has zero divisors, and is not a field.

---

# Solution

The plan: take any nonzero $b \in B$, choose its minimal monic equation over $k$, use the domain property to show the constant term is nonzero, then invert that constant (it lives in the field $k$) to solve for $b^{-1}$. The two hypotheses — domain and base-is-a-field — enter at exactly two distinct points.

**Step 1: Take a minimal-degree monic equation for a nonzero $b$.**

For $0 \neq b \in B$, among all monic equations over $k$ satisfied by $b$, pick one of least degree $n$: $b^n + a_1 b^{n-1} + \cdots + a_n = 0$.

> [!note]- Derivation
> Since $B$ is integral over $k$, $b$ satisfies *some* [[Def - Integral Element and Integral Extension|monic]] polynomial over $k$, so the set of degrees of such polynomials is a nonempty set of positive integers; let $n$ be its minimum and fix a monic equation
> $$b^n + a_1 b^{n-1} + \cdots + a_{n-1} b + a_n = 0, \qquad a_i \in k,$$
> of that minimal degree. (Equivalently, the minimal polynomial of $b$ over $k$; but we only need minimality of the degree.)

**Step 2: The constant term $a_n$ is nonzero.**

If $a_n = 0$, the domain property lets us cancel $b$ and contradict minimality. So $a_n \neq 0$.

> [!note]- Derivation
> Suppose $a_n = 0$. Then the equation reads
> $$b^n + a_1 b^{n-1} + \cdots + a_{n-1}b = 0, \quad\text{i.e.}\quad b\big(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}\big) = 0.$$
> Since $B$ is an [[Def - Integral Domain|integral domain]] and $b \neq 0$, the other factor must vanish:
> $$b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1} = 0.$$
> But this is a *monic* polynomial relation for $b$ of degree $n - 1 < n$ — contradicting the minimality of $n$. Therefore $a_n \neq 0$. (This is the unique place the *domain* hypothesis is used.)

**Step 3: Invert $b$ using that $a_n \in k^\times$.**

Rearranging the equation and dividing by $-a_n$ gives an explicit inverse of $b$ in $B$.

> [!note]- Derivation
> Move all terms but $a_n$ to one side:
> $$b\big(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}\big) = -a_n.$$
> Since $a_n \in k$ is nonzero and $k$ is a [[Def - Unit and Field|field]], $a_n^{-1} \in k \subseteq B$ exists. Multiply both sides by $-a_n^{-1}$:
> $$b \cdot \Big({-a_n^{-1}}\big(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}\big)\Big) = 1.$$
> The element in parentheses lies in $B$, so it is an inverse of $b$. Hence $b$ is a unit. As $b$ was an arbitrary nonzero element, $B$ is a field. (This is the unique place the *base-is-a-field* hypothesis is used.)

**Step 4: The domain hypothesis is necessary — counterexample $k \times k$.**

$B = k \times k$ is integral over $k$, not a domain, and not a field.

> [!note]- Derivation
> Let $B = k \times k$ with componentwise operations, and $k \hookrightarrow B$ via $c \mapsto (c, c)$. Then $B$ is a *finite* $k$-module of rank $2$, with basis $(1, 0), (0, 1)$, hence integral over $k$ (every finite extension is integral — concretely, each element $(x, y)$ satisfies the monic $T^2 - (x + y)\,T + xy = 0$, whose coefficients $x + y, xy$ are scalars in $k$ when we read $(x, y)$ against the diagonal copy; more cleanly, the idempotent $(1, 0)$ satisfies the monic $T^2 - T = 0$). But $B$ is **not a domain**: $(1, 0)(0, 1) = (0, 0)$ exhibits zero divisors. And $B$ is **not a field**: $(1, 0)$ has no inverse, since $(1, 0)(u, v) = (u, 0) \neq (1, 1) = 1_B$ for every $(u, v)$. So integrality over a field does *not* force a field without the domain hypothesis — the constant term $a_n = 0$ in $T^2 - T$ for $(1,0)$ is exactly the gap, and only the domain property closes it.

> [!note]- Complete formal solution
> **Claim.** A domain $B$ integral over a field $k$ is a field.
>
> Let $0 \neq b \in B$. Choose a monic equation $b^n + a_1 b^{n-1} + \cdots + a_n = 0$ ($a_i \in k$) of minimal degree $n$. If $a_n = 0$, then $b(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}) = 0$; since $B$ is a domain and $b \neq 0$, $b^{n-1} + \cdots + a_{n-1} = 0$, a monic relation of degree $n-1$, contradicting minimality. So $a_n \neq 0$. Then
> $$b\big(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}\big) = -a_n,$$
> and since $a_n \in k^\times$, $b^{-1} = -a_n^{-1}(b^{n-1} + \cdots + a_{n-1}) \in B$. Hence every nonzero $b$ is a unit: $B$ is a field.
>
> *Necessity of "domain".* $B = k \times k$ is finite (rank $2$), hence integral, over $k$, but has zero divisors $(1,0)(0,1) = 0$ and the non-unit $(1,0)$ — so it is neither a domain nor a field. $\blacksquare$

---

# Key Takeaways

**To invert an element in an integral extension, solve its minimal equation for the constant term.** The reusable technique: given $b$ integral and you want $b^{-1}$, write the minimal monic equation and rearrange it as "$b \times (\text{stuff}) = -(\text{constant term})$". If the constant term is invertible — which it is when the base is a field — you have the inverse. The whole content is that a *minimal* equation has a *nonzero* constant term in a domain (you can always cancel a trailing factor of $b$ otherwise), and a nonzero element of a field is invertible. This pattern recurs throughout: it is how one shows $k[\alpha] = k(\alpha)$ for algebraic $\alpha$, how Zariski's lemma forces residue fields, and how the [[Thm - Integral Extensions and Fields (Domain Criterion)|field criterion]] is proved. The trigger is "invert an integral element over a field"; the reaction is "minimal equation, isolate the constant, invert it".

**Two hypotheses, two distinct jobs — and knowing which is which is the proof.** This exercise is a clean illustration that a theorem's hypotheses are not interchangeable decorations. *"Integral over $k$"* supplies the equation. *"$B$ is a domain"* is used in exactly one place — to cancel a factor of $b$ and force the constant term nonzero. *"$k$ is a field"* is used in exactly one other place — to invert that constant term. Remove the domain hypothesis and $a_n$ can be $0$ (as in $k \times k$, where the idempotent $(1,0)$ has $a_n = 0$ in $T^2 - T$); remove the field hypothesis and $a_n$ might not be invertible. When you return to this proof, the reconstruction hinges on remembering *the domain hypothesis kills the case $a_n = 0$, the field hypothesis inverts $a_n \neq 0$* — two hypotheses, two lines, two jobs.

**This is the engine of the Nullstellensatz, scaled up by Noether normalization.** The humble statement "a domain integral over a field is a field" is the final step of **Zariski's lemma**: if $L$ is a field finitely generated as a $k$-algebra, Noether normalization makes $L$ finite (hence integral) over a polynomial subring $k[y_1, \dots, y_d]$; this very theorem (applied with $B = L$ a domain integral over the domain $k[y_1, \dots, y_d]$, via the full domain criterion) forces $k[y_1, \dots, y_d]$ to be a field, which happens only if $d = 0$, so $L$ is finite over $k$. From Zariski's lemma the entire **Nullstellensatz** — maximal ideals of $k[x_1, \dots, x_n]$ are points, radical ideals correspond to varieties — follows. So the inversion trick you just learned, iterated through a polynomial tower, is what makes algebraic geometry's dictionary between ideals and varieties work; see [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

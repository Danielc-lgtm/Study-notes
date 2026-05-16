---
type: exercise
subject: ring-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Ring"
  - "Def - Characteristic of a Ring"
tags: [algebra, ring-theory]
---

# Problem Statement

A ring $R$ is called a **Boolean ring** if every element is idempotent, that is,
$$x^2 = x \qquad \text{for all } x \in R.$$
(Note: at this point $R$ is *not* assumed commutative — the ring axioms guarantee an abelian group under $+$ and an associative, distributive, unital multiplication, but not $xy = yx$.)

Let $R$ be a Boolean ring. Prove the following.

1. **Characteristic two.** For every $x \in R$, $x = -x$; equivalently $x + x = 0$. Consequently $R$ has [[Def - Characteristic of a Ring|characteristic]] dividing $2$.
2. **Commutativity.** $R$ is commutative: $xy = yx$ for all $x, y \in R$.

(Suggested manipulations: expand $(x + y)^2$, and separately expand $(x + x)^2$.)

**Recall:**

The objects in play are a ring, the additive inverse, and the characteristic.

A [[Def - Ring|ring]] $R$ is a quintuple $(R, +, \cdot, 0, 1)$ where $(R, +, 0)$ is an **abelian group**, multiplication is **associative** with a two-sided identity $1$, and multiplication **distributes** over addition on both sides:
$$r(s + t) = rs + rt, \qquad (r + s)t = rt + st.$$
For this exercise it is essential that commutativity of multiplication is *not* among the axioms — proving it is the goal. From distributivity one gets the standard sign rules $r \cdot 0 = 0$ and $(-r)s = r(-s) = -(rs)$, valid in any ring.

The **additive inverse** of $x$ is the unique element $-x$ with $x + (-x) = 0$, supplied by the abelian group $(R, +, 0)$.

The **characteristic** of $R$, written $\operatorname{char}(R)$, is the smallest positive integer $n$ such that $\underbrace{1 + 1 + \cdots + 1}_{n} = 0$; if no such $n$ exists the characteristic is $0$. Equivalently it is the non-negative generator of the kernel of the unique ring homomorphism $\mathbb{Z} \to R$. Saying "$\operatorname{char}(R)$ divides $2$" means $1 + 1 = 0$ in $R$ (so the characteristic is $1$ or $2$); when $1 + 1 = 0$, distributivity spreads this to $x + x = (1+1)x = 0$ for *every* $x$.

An element $x$ with $x^2 = x$ is called **idempotent**. In a Boolean ring *every* element is idempotent — that is the single, very strong hypothesis driving everything below.

---

# Convergent Strategy

**Problem class.** This is an *axiom-mining* problem: a single universally-quantified algebraic identity ($x^2 = x$ for all $x$) is given, and global structural conclusions (characteristic two, commutativity) must be extracted purely by formal manipulation. The topic's [[Rings I — §2.1–2.2#Problem-Solving Strategy|problem-solving strategy]] flags the signature move for such problems: when an identity holds *for all elements*, instantiate it at a cleverly chosen **compound element** — a sum, a product — and expand, so that the hypothesis applied to the compound yields a relation among the pieces.

**Assumption pattern.** The hypothesis "$x^2 = x$ for all $x$" is deceptively small but extremely rigid: it is one equation, but it must hold at *every* element of $R$, including elements you construct yourself. The leverage comes entirely from feeding the identity elements it did not obviously anticipate — $x + y$, $x + x$ — and forcing consistency. There is no numerical dial here; the single hypothesis already pins the ring down to the point of commutativity.

**Theorem routing.** No named theorem is used. The route is two applications of the **expand-a-compound-idempotent** operation. Applying $x^2 = x$ to $x + x$ collapses to $x + x = 0$ (part 1). Applying $x^2 = x$ to $x + y$ and using distributivity yields $xy + yx = 0$; combined with part 1 (so that $-xy = xy$) this becomes $xy = yx$ (part 2). Part 1 is genuinely a *lemma feeding* part 2 — without characteristic two the second computation would only give $xy = -yx$, which is not commutativity.

**Key decision point.** The non-obvious choices are *which* compounds to expand and *in what order*. Expanding $(x + y)^2$ is natural and forced; the subtle move is to first extract $x + x = 0$ by expanding $(x + x)^2$, because that fact is exactly what converts the consequence $xy + yx = 0$ of the $(x+y)^2$ expansion into the desired $xy = yx$. The decision point is recognising that the $(x+y)^2$ computation alone proves only "$R$ is anticommutative" ($xy = -yx$), and that anticommutativity becomes commutativity precisely when $-1 = 1$ — so characteristic two is not a side result but the keystone. Getting the dependency order right (characteristic two *first*) is the whole craft of the problem.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings I — §2.1–2.2#Legal Operations|the topic page's Legal Operations]]:

1. **Instantiate a universal identity at a compound element and expand.** The hypothesis $x^2 = x$ is applied not to bare elements but to the constructed elements $x + x$ and $x + y$. Expanding the square via distributivity turns each instance into an equation relating the constituent pieces.

2. **Expand a square using distributivity without assuming commutativity.** Crucially, $(x + y)^2$ is expanded as $x^2 + xy + yx + y^2$ — keeping $xy$ and $yx$ as *distinct* terms — because commutativity is the conclusion, not an available tool. This is the disciplined version of "FOIL" that is legal in a not-necessarily-commutative ring.

3. **Cancel in the additive group.** Every step uses that $(R, +, 0)$ is an abelian group: equal sums can have common terms subtracted (add the additive inverse to both sides). This is how $x + x^2 + \cdots = x$ is reduced to a relation among the leftover terms.

4. **Propagate a fact about $1$ to every element via distributivity** (used to phrase part 1 as a characteristic statement). Once $1 + 1 = 0$, the identity $x + x = (1 + 1)x = 0 \cdot x = 0$ extends "characteristic two" from the identity element to all of $R$.

---

# Hints

> [!note]- Hint 1
> The hypothesis $z^2 = z$ holds for *every* $z \in R$, so it holds for elements you build yourself. Pick a compound element, square it, expand the square using distributivity, and set the result equal to the element. Try $z = x + x$ first: expand $(x + x)^2$ and use $x^2 = x$.

> [!note]- Hint 2
> $(x + x)^2 = x^2 + x^2 + x^2 + x^2 = 4x$ once you replace each $x^2$ by $x$; but also $(x+x)^2 = x + x = 2x$ since $x + x$ is idempotent. So $4x = 2x$, hence $2x = 0$, i.e. $x + x = 0$ and $x = -x$. That is part 1. Keep this fact: every element is its own additive inverse.

> [!note]- Hint 3
> For commutativity, expand $(x + y)^2$. Be careful: you may **not** assume $xy = yx$ — that is what you are proving. So
> $$(x + y)^2 = (x + y)(x + y) = x^2 + xy + yx + y^2.$$
> Replace $(x+y)^2$, $x^2$, $y^2$ by $x + y$, $x$, $y$ respectively (each is idempotent). What equation among $xy$ and $yx$ falls out after cancelling?

> [!note]- Hint 4
> The expansion gives $x + y = x + xy + yx + y$, so after cancelling $x$ and $y$ from both sides, $xy + yx = 0$, i.e. $xy = -(yx)$. Now invoke part 1 applied to the element $yx$: since every element equals its own negative, $-(yx) = yx$. Therefore $xy = yx$.

---

# Solution

The plan: square the compound $x + x$ to force $x + x = 0$ (characteristic two); then square the compound $x + y$, expanding *without* commutativity, to get $xy + yx = 0$; then use characteristic two to turn $-(yx)$ into $yx$ and conclude $xy = yx$.

**Step 1: every element satisfies $x + x = 0$, so $R$ has characteristic dividing $2$.**

Apply the idempotent law $z^2 = z$ to the element $z = x + x$. Expanding the square gives $4x$, while idempotence gives $2x$; equating and cancelling yields $2x = 0$, i.e. $x = -x$.

> [!note]- Derivation
> Fix $x \in R$ and set $z = x + x$. Two evaluations of $z^2$.
>
> *Evaluation A — by idempotence.* Since $z \in R$, the Boolean hypothesis gives $z^2 = z$, that is,
> $$(x + x)^2 = x + x.$$
>
> *Evaluation B — by distributivity.* Expand the square, using distributivity on both sides and **not** assuming commutativity (though here all four terms are $x \cdot x$ anyway):
> $$(x + x)^2 = (x + x)(x + x) = x x + x x + x x + x x = x^2 + x^2 + x^2 + x^2.$$
> Now replace each $x^2$ by $x$ (idempotence of $x$ itself):
> $$(x + x)^2 = x + x + x + x.$$
>
> Equate A and B:
> $$x + x + x + x = x + x.$$
> The additive group $(R, +, 0)$ is abelian, so cancel $x + x$ from both sides (add $-(x + x)$ to each side):
> $$x + x = 0.$$
> Equivalently $x = -x$: every element of a Boolean ring is its own additive inverse.
>
> *Characteristic statement.* Specialising $x = 1$ gives $1 + 1 = 0$. The characteristic of $R$, the least positive $n$ with $n \cdot 1 = 0$, therefore divides $2$ — it is $2$ if $R \neq \{0\}$ and $1$ in the degenerate zero ring. (Conversely, once $1 + 1 = 0$, distributivity recovers the elementwise statement for free: $x + x = 1 \cdot x + 1 \cdot x = (1 + 1)x = 0 \cdot x = 0$.) So "$x = -x$ for all $x$" and "$\operatorname{char}(R) \mid 2$" are the same fact.

**Step 2: for all $x, y$, expanding $(x + y)^2$ gives $xy + yx = 0$.**

Apply $z^2 = z$ to $z = x + y$. Expanding the square *without* commutativity produces $x^2 + xy + yx + y^2$; idempotence collapses the squares and cancellation leaves $xy + yx = 0$.

> [!note]- Derivation
> Fix $x, y \in R$ and set $z = x + y$. Again two evaluations.
>
> *Evaluation A — by idempotence.* $(x + y)^2 = x + y$.
>
> *Evaluation B — by distributivity.* Expand carefully. The single most important discipline here: **do not collapse $xy$ and $yx$**, because commutativity is precisely the theorem and is not yet available. Using right- and left-distributivity,
> $$(x + y)^2 = (x + y)(x + y) = x(x + y) + y(x + y) = (xx + xy) + (yx + yy) = x^2 + xy + yx + y^2.$$
> Replace $x^2 \to x$ and $y^2 \to y$ by idempotence:
> $$(x + y)^2 = x + xy + yx + y.$$
>
> Equate A and B:
> $$x + y = x + xy + yx + y.$$
> Cancel $x$ and $y$ (the additive group is abelian, so cancel freely):
> $$0 = xy + yx, \qquad \text{i.e.} \qquad xy + yx = 0.$$
> This says $xy = -(yx)$: a Boolean ring is automatically **anticommutative**. Note this step used *only* the idempotent hypothesis, not Step 1 — Step 1 enters next.

**Step 3: characteristic two upgrades anticommutativity to commutativity.**

By Step 2, $xy = -(yx)$. By Step 1 applied to the element $yx$, that element equals its own negative, so $-(yx) = yx$. Hence $xy = yx$ for all $x, y$: $R$ is commutative.

> [!note]- Derivation
> From Step 2, for arbitrary $x, y \in R$,
> $$xy + yx = 0 \qquad \Longrightarrow \qquad xy = -(yx).$$
> Step 1 holds for *every* element of $R$; apply it to the particular element $w := yx \in R$. Step 1 says $w = -w$, that is,
> $$yx = -(yx).$$
> Substituting $-(yx) = yx$ into $xy = -(yx)$ gives
> $$xy = yx.$$
> Since $x, y$ were arbitrary, multiplication in $R$ is commutative. $\blacksquare$
>
> The logical shape is worth noting: Step 2 alone proves "Boolean $\Rightarrow$ anticommutative", and Step 1 alone proves "Boolean $\Rightarrow$ characteristic two". Commutativity is the *product* of the two — anticommutativity ($xy = -yx$) coincides with commutativity ($xy = yx$) exactly in the world where $-1 = 1$, which is characteristic two. Neither step is dispensable.

> [!note]- Complete formal solution
> Let $R$ be a ring (not assumed commutative) with $x^2 = x$ for all $x \in R$.
>
> **Part 1.** Fix $x \in R$. Idempotence at $x + x$ gives $(x+x)^2 = x + x$. Distributivity gives $(x+x)^2 = x^2 + x^2 + x^2 + x^2 = x + x + x + x$ (replacing $x^2 = x$). Hence $x + x + x + x = x + x$; cancelling $x + x$ in the abelian group $(R,+,0)$ yields $x + x = 0$, i.e. $x = -x$. Taking $x = 1$ gives $1 + 1 = 0$, so $\operatorname{char}(R) \mid 2$.
>
> **Part 2.** Fix $x, y \in R$. Idempotence at $x + y$ gives $(x + y)^2 = x + y$. Distributivity, *without assuming commutativity*, gives
> $$(x + y)^2 = x^2 + xy + yx + y^2 = x + xy + yx + y.$$
> Equating, $x + y = x + xy + yx + y$, and cancelling $x$ and $y$ gives $xy + yx = 0$, i.e. $xy = -(yx)$. By Part 1 applied to the element $yx$, we have $yx = -(yx)$, hence $-(yx) = yx$. Therefore $xy = yx$. As $x, y$ were arbitrary, $R$ is commutative. $\blacksquare$

---

# Key Takeaways

**When an identity is quantified over all elements, the elements you should feed it are the ones you build yourself.** The hypothesis $x^2 = x$ looks like a statement about each individual element in isolation, and used that way it says nothing about how two elements interact. The entire proof turns on the realisation that "for all $x$" includes *compound* elements — $x + x$, $x + y$, and in other problems $x - y$, $xy$, $1 + x$ — and that instantiating a universal identity at a cleverly chosen compound, then expanding, converts a one-element fact into a relation *between* elements. This is the master technique for axiom-mining problems: the identity $f(z) = g(z)$ holding for all $z$ is an infinite family of equations, and the skill is choosing the substitution $z = (\text{something assembled from } x \text{ and } y)$ that makes the expansion say what you want. The same trick proves that a ring with $x^3 = x$ is commutative, that a "linear" map satisfying $T(x)^2 = T(x^2)$ has special structure, and pervades the theory of polynomial identities (PI-rings). Whenever you are stuck with a for-all hypothesis, ask: *what have I not yet substituted?*

**Expand squares honestly — keep $xy$ and $yx$ apart until commutativity is earned.** The most common error in this exercise is to write $(x + y)^2 = x^2 + 2xy + y^2$. That step silently assumes $xy = yx$, which is the very conclusion. The disciplined expansion $(x + y)^2 = x^2 + xy + yx + y^2$ keeps the two mixed products as distinct symbols, and it is *only* because they are kept distinct that the equation $xy + yx = 0$ — the real content — can emerge. The general lesson is to audit every algebraic manipulation for hidden uses of the property you are trying to prove: in a noncommutative setting, "FOIL" has four terms, not three; in a non-associative setting, parenthesisation must be tracked; when proving a map is linear you may not use linearity. Strip your toolkit down to exactly the axioms you are *given* and forbid yourself the conclusion. This honest bookkeeping is what separates a correct proof from a circular one.

**A lemma about the identity element propagates to the whole ring through distributivity — and characteristic is exactly such a propagated fact.** Part 1 is proved elementwise ($x + x = 0$ for each $x$), but it is equivalent to the single statement $1 + 1 = 0$ about the identity, because distributivity broadcasts any additive fact about $1$ to every element: $x + x = (1 + 1)x$. This is why "characteristic" is well-defined as a property of the ring rather than of individual elements — the relation $n \cdot 1 = 0$ automatically forces $n \cdot x = 0$ everywhere. The reusable principle: in a ring, facts about $1$ are never merely about $1$; multiplication spreads them. When you discover a relation among copies of $1$, immediately ask what it implies elementwise, and conversely, when you need an elementwise additive identity, try to reduce it to a statement about $1$ where it is easier to obtain.

**Anticommutativity plus characteristic two equals commutativity — watch for the collapse $-1 = 1$.** The deep structural punchline is that the $(x+y)^2$ computation, on its own, proves only that a Boolean ring is *anticommutative*: $xy = -yx$. Anticommutativity and commutativity are different conditions in general — they coincide *precisely* in characteristic two, the unique setting where the sign $-1$ equals $+1$ and the distinction between a thing and its negative evaporates. So the proof is genuinely two-staged: one stage produces a sign-twisted version of the goal, the other stage produces the characteristic-two world in which the sign twist is invisible. This "the sign disappears in characteristic two" phenomenon is everywhere in algebra: in characteristic two, symmetric and alternating bilinear forms partly merge, squaring becomes additive (the Frobenius / Freshman's dream $(x+y)^2 = x^2 + y^2$ — which is exactly what Step 1's computation $(x+x)^2 = 4x$ secretly used), and many sign-sensitive theorems acquire exceptions. The transferable instinct: whenever a computation yields a result that is "off by a sign" from what you want, check whether your hypotheses force characteristic two, because that is the standard mechanism by which an off-by-a-sign result becomes exact.

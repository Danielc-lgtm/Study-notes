---
type: theorem
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Ring Homomorphism"
  - "Def - Ideal"
  - "Def - Quotient Ring"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ and $S$ are [[Def - Ring|rings]] (with identity, not necessarily commutative) and $\varphi : R \to S$ is a [[Def - Ring Homomorphism|ring homomorphism]] — a map satisfying $\varphi(r_1 + r_2) = \varphi(r_1) + \varphi(r_2)$, $\varphi(r_1 r_2) = \varphi(r_1)\varphi(r_2)$, $\varphi(0_R) = 0_S$, and $\varphi(1_R) = 1_S$. Its **kernel** is $\ker\varphi = \{r \in R : \varphi(r) = 0_S\}$ and its **image** is $\operatorname{im}\varphi = \{\varphi(r) : r \in R\}$. For an [[Def - Ideal|ideal]] $I \trianglelefteq R$, the [[Def - Quotient Ring|quotient ring]] $R/I$ is the set of additive cosets $r + I$ with operations $(r_1 + I) + (r_2 + I) = (r_1 + r_2) + I$ and $(r_1 + I)(r_2 + I) = r_1 r_2 + I$, zero $0_R + I$, and one $1_R + I$. The symbol $\trianglelefteq$ means "is an ideal of", $\leq$ means "is a subring of", and $\cong$ denotes ring isomorphism. The full symbol registry is on the parent page [[Rings I — §2.1–2.2]].

---

# Statement

> **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem]] for Rings.** Let $\varphi : R \to S$ be a ring homomorphism. Then $\ker\varphi$ is an ideal of $R$, and the map
> $$\Phi : R/\ker\varphi \longrightarrow \operatorname{im}\varphi, \qquad r + \ker\varphi \longmapsto \varphi(r)$$
> is a well-defined ring isomorphism. Hence
> $$R/\ker\varphi \;\cong\; \operatorname{im}\varphi \;\leq\; S.$$

---

# Motivation

You have just met the [[Def - Quotient Ring|quotient ring]] $R/I$, and the very first thing you tried to do with it — in the source, with $\mathbb{C}[X]/(X)$ and then $\mathbb{R}[X]/(X^2+1)$ — was *recognise* it: to say which ring it actually is. That computation was painful. To show $\mathbb{R}[X]/(X^2+1) \cong \mathbb{C}$ by hand you had to verify that every element has a unique representative $a + bX$, then write down a candidate bijection, then grind through a multiplication check term by term. The first isomorphism theorem exists to make that grind unnecessary, exactly once and for all.

Here is the question it answers. You are handed a quotient ring $R/I$ and asked what it *is* — which familiar ring it equals up to isomorphism. Working with $R/I$ directly is unpleasant, because its elements are [[Def - Coset|cosets]], which are sets, and reasoning about arithmetic on sets is awkward. You would much rather recognise $R/I$ as a ring you already know. The theorem tells you precisely when you may: $R/I \cong T$ exactly when there is a *surjective* ring homomorphism $R \to T$ whose kernel is $I$. So the strategy flips. Instead of dissecting the quotient, you go hunting for a homomorphism *out of $R$* — and [[Def - Homomorphism|homomorphisms]] out of polynomial [[Def - Ring|rings]], in particular, are cheap to build, because a homomorphism out of $R[X]$ is determined by where it sends $X$.

This is **the** tool for identifying a quotient ring, and the canonical illustration is exactly the example the source labours by hand. To identify $\mathbb{R}[X]/(X^2+1)$, do not study the quotient at all. Instead define the evaluation homomorphism $\varphi : \mathbb{R}[X] \to \mathbb{C}$, $X \mapsto i$ (so $p(X) \mapsto p(i)$). It is surjective: $a + bX \mapsto a + bi$ already hits every complex number. Its kernel is the set of real polynomials vanishing at $i$, which — because $X^2+1$ is the minimal such polynomial and divides any other by the [[Thm - Euclidean Algorithm for Polynomials|Euclidean algorithm]] — is exactly the ideal $(X^2+1)$. The theorem then delivers $\mathbb{R}[X]/(X^2+1) \cong \mathbb{C}$ in one line, with no representative-uniqueness argument and no multiplication grind.

There is a second, more conceptual reading. Every homomorphism $\varphi$ fails to be injective in a way measured by $\ker\varphi$, and fails to be surjective in a way measured by $\operatorname{im}\varphi$. The theorem says these two failures are not independent: once you quotient out the kernel — once you stop distinguishing elements that $\varphi$ already refuses to distinguish — the resulting map is a *perfect* match onto the image. Every ring homomorphism factors canonically as
$$R \;\xrightarrow{\;\text{surjection}\;}\; R/\ker\varphi \;\xrightarrow{\;\cong\;}\; \operatorname{im}\varphi \;\xrightarrow{\;\text{inclusion}\;}\; S.$$
A ring homomorphism is nothing more than a quotient map followed by an inclusion. The [[Thm - Second Isomorphism Theorem for Rings|second]] and [[Thm - Third Isomorphism Theorem for Rings|third]] isomorphism theorems are then not new ideas but corollaries — each is the first theorem applied to a cleverly chosen homomorphism.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is mild — *any* ring homomorphism $\varphi : R \to S$ will do — so the real source question is: when does a problem secretly hand you a homomorphism, even though none is named? Recognising the disguised input is the entire skill.

The first and most important disguised source is **a quotient ring you want to identify, together with a polynomial ring as the numerator**. If you must identify $F[X]/(g)$, the property $B$ is "the numerator is a [[Def - Polynomial Ring|polynomial ring]]", and the bridge to a homomorphism is the universal property of $R[X]$: a ring homomorphism out of $R[X]$ is *freely* specified by a homomorphism on the coefficient ring together with an arbitrary choice of image for $X$. So to identify $\mathbb{R}[X]/(X^2+1)$ you simply *decide* to send $X$ to a square root of $-1$; the map $X \mapsto i$ then exists with no further checking, and its kernel is computable. The non-obvious part is that you do not need a pre-existing map — you *manufacture* one by choosing the image of $X$, and the freedom of that choice is exactly what makes the polynomial-ring case so tractable. *Example problem:* identify $\mathbb{Z}[X]/(X)$ by evaluating at $0$, or $\mathbb{R}[X]/(X-a)$ by evaluating at $a$, both giving the coefficient ring back.

The second disguised source is **a ring carrying a natural arithmetic-respecting invariant or a natural "forgetful" reduction**. If every element of $R$ can be assigned a value in some ring $T$ in a way that respects $+$ and $\times$, that assignment *is* a homomorphism $R \to T$. The canonical instance is reduction modulo $n$: the map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ is a homomorphism precisely because remainders add and multiply correctly. The non-obvious step is to notice that the invariant is multiplicative, not merely additive, so that it qualifies as a *ring* homomorphism. *Example problem:* show $\mathbb{Z}[X]/(n, X) \cong \mathbb{Z}/n\mathbb{Z}$ by reducing coefficients mod $n$ and evaluating at $0$.

The third disguised source is **a subring sitting inside a larger ring with a known quotient**. Given $R \leq S$ and an ideal $J \trianglelefteq S$, the composite $R \hookrightarrow S \twoheadrightarrow S/J$ is a homomorphism $R \to S/J$ — built, not given. Its kernel is $R \cap J$ and its image is $(R+J)/J$. The non-obviousness is that composing an inclusion with a quotient map manufactures a brand-new homomorphism whose kernel and image are computable; this is precisely how the [[Thm - Second Isomorphism Theorem for Rings|second isomorphism theorem]] is proved. *Example problem:* derive $R/(R \cap J) \cong (R+J)/J$ directly. Likewise, composing two quotient maps $R/I \to R/J$ (for $I \subseteq J$) yields the [[Thm - Third Isomorphism Theorem for Rings|third isomorphism theorem]].

**Targets (Output Amplification)**

The bare conclusion is an isomorphism $R/\ker\varphi \cong \operatorname{im}\varphi$. Combined with other facts it does much more.

Combine the conclusion with **surjectivity of $\varphi$**. If $\varphi$ is onto, then $\operatorname{im}\varphi = S$, and the conclusion sharpens to $R/\ker\varphi \cong S$ — a clean identification of the *whole* target ring as a quotient of $R$. The further result $E$ is that any surjection $R \twoheadrightarrow S$ exhibits $S$ as $R$ modulo a single ideal, so structural questions about $S$ (does it have zero divisors? is it a field?) become questions about the ideal $\ker\varphi$. This is non-obvious because it converts a property of a *map* into a property of an *ideal*, where the ideal-theoretic tools (maximal, prime) apply.

Combine the conclusion with **a property of $\operatorname{im}\varphi$ inherited from $S$**. The image $\operatorname{im}\varphi$ is a subring of $S$; if $S$ is an [[Def - Ring|integral domain]] then so is every subring, hence so is $\operatorname{im}\varphi$, hence so is $R/\ker\varphi$. The further result is a criterion on the ideal: $R/\ker\varphi$ is a domain, so $\ker\varphi$ is a *prime* ideal. Mapping into a field similarly forces $\ker\varphi$ to be *maximal*. This is the standard way to *prove* an ideal is prime or maximal — exhibit a homomorphism onto a domain or field with that kernel — and it is non-obvious because primality of an ideal looks like an internal multiplicative condition, yet here it is read off from an external map.

Combine the conclusion with **a known finite cardinality of $R$**. If $R$ is finite, then $|R/\ker\varphi| = |R|/|\ker\varphi|$, so $|\operatorname{im}\varphi|$ divides $|R|$. The further result $E$ is a divisibility obstruction on ring homomorphisms: there can be no homomorphism from $\mathbb{Z}/m\mathbb{Z}$ onto a ring whose order does not divide $m$, and no nonzero homomorphism at all between finite rings of coprime order, because the image would have order dividing both. This turns a counting fact into a rigidity statement.

---

# Why Is It True

Forget the formal proof and picture what a ring homomorphism does to $R$. The map $\varphi$ sends $R$ onto $\operatorname{im}\varphi$, and along the way it identifies some elements — it can send $r$ and $r'$ to the same place. Ask which elements get identified. Because $\varphi$ is in particular an additive homomorphism, $\varphi(r) = \varphi(r')$ if and only if $\varphi(r) - \varphi(r') = 0_S$, which says $\varphi(r - r') = 0_S$, which says $r - r' \in \ker\varphi$. But "$r - r' \in \ker\varphi$" is exactly the condition for $r$ and $r'$ to lie in the same additive coset of $\ker\varphi$. So:

> Two elements of $R$ have the same image under $\varphi$ **exactly when** they lie in the same coset of $\ker\varphi$.

This single observation is the whole theorem. The cosets of $\ker\varphi$ are *literally* the fibres of $\varphi$ — the sets of elements sharing a common image. The kernel measures the redundancy in $\varphi$, and that redundancy is organised perfectly into cosets.

Now the conclusion is forced. The quotient $R/\ker\varphi$ is, by construction, the set of these cosets, that is, the set of fibres. Sending each fibre to the common value of $\varphi$ on it is a bijection onto $\operatorname{im}\varphi$: surjective because every value of $\varphi$ is attained on *some* fibre, and injective because *distinct* fibres carry distinct values. It respects addition because $\varphi$ does, and it respects multiplication because $\varphi$ does. The map $\Phi$ is not a clever construction one must be lucky to find — it is the only thing $\varphi$ could possibly be once you collapse its redundancy.

Here is the point where the ring case has *less* to prove than you might fear, and seeing why is the real insight. A ring is an abelian group under $+$ with a multiplication bolted on. The additive structure of the whole theorem — that $\ker\varphi$ is an additive [[Def - Subgroup|subgroup]], that $\Phi$ is well-defined, bijective, and additive — is *already done* by the first isomorphism theorem for [[Def - Group|groups]], applied verbatim to $(R,+)$. Nothing about that part knows or cares that there is a multiplication. So the only genuinely ring-theoretic content is two small checks: that the kernel is closed under multiplication *by arbitrary ring elements* (the strong-closure half of being an ideal), and that the map $\Phi$ respects multiplication. Both are one-line computations, because multiplication in the quotient is *defined* on representatives — $(r + I)(r' + I) = rr' + I$ — so $\Phi$ of a product is $\varphi$ of a product, and $\varphi$ already multiplies. The slogan: the first isomorphism theorem for rings is the group theorem plus a multiplication that comes along for free.

---

# What Makes This Hard

The genuine ring-theoretic content is tiny — almost everything is inherited from the group theorem applied to $(R,+)$ — so the trap is *over-proving*: re-deriving well-definedness, bijectivity, and additivity of $\Phi$ from scratch when those are free, and missing that the only new obligations are multiplicative closure of $\ker\varphi$ and multiplicativity of $\Phi$. The single non-obvious step is recognising that $\ker\varphi$ satisfies *strong* closure ($a \in \ker\varphi$, $b \in R \implies ab \in \ker\varphi$), which holds because $\varphi(ab) = \varphi(a)\varphi(b) = 0 \cdot \varphi(b) = 0$ — note the use of $0 \cdot s = 0$, which itself needs the ring distributive law. The most common error is to forget the multiplicative-identity check and try to call $\ker\varphi$ a *[[Def - Subring|subring]]* (it almost never is — a proper ideal cannot contain $1$).

---

# Rederivation Scaffold

**High-level strategy:**
Do not reprove the group theorem. Cite it for the additive part, then add exactly two ring-specific checks. Concretely: cite that $\ker\varphi$ is an additive subgroup and that $\Phi(r + \ker\varphi) = \varphi(r)$ is a well-defined additive bijection onto $\operatorname{im}\varphi$ (first isomorphism theorem for groups, applied to $(R,+)$). Then prove the two new things: $\ker\varphi$ has strong multiplicative closure, and $\Phi$ is multiplicative.

**Subgoal decomposition:**

1. **Kernel is an ideal.** Show $\ker\varphi \trianglelefteq R$.
   - *Hint:* Additive-subgroup part is the group case. For strong closure, take $a \in \ker\varphi$ and $b \in R$ and compute $\varphi(ab) = \varphi(a)\varphi(b) = 0\cdot\varphi(b) = 0$.
   - *Why needed:* Without this there is no quotient ring $R/\ker\varphi$ to serve as the source of $\Phi$.

2. **Import the group theorem.** State that $\Phi(r + \ker\varphi) = \varphi(r)$ is well-defined, bijective onto $\operatorname{im}\varphi$, and additive.
   - *Hint:* Apply the first isomorphism theorem for groups to the additive group homomorphism $\varphi : (R,+) \to (S,+)$; the cosets of $\ker\varphi$ are exactly its fibres.
   - *Why needed:* This discharges, for free, every claim about $\Phi$ except multiplicativity.

3. **$\Phi$ is multiplicative.** Show $\Phi$ sends a product of cosets to the product of values.
   - *Hint:* $\Phi\big((r + \ker\varphi)(t + \ker\varphi)\big) = \Phi(rt + \ker\varphi) = \varphi(rt) = \varphi(r)\varphi(t)$, then read off $= \Phi(r+\ker\varphi)\Phi(t+\ker\varphi)$.
   - *Why needed:* A ring isomorphism must respect multiplication; this is the one ring-specific check on the map.

4. **Conclude.** A well-defined additive bijection that is also multiplicative (and sends $1$ to $1$) is a ring isomorphism, so $R/\ker\varphi \cong \operatorname{im}\varphi$.
   - *Hint:* Multiplicativity plus the inherited additive-isomorphism status is all that "ring isomorphism" requires; $\Phi(1 + \ker\varphi) = \varphi(1) = 1$.
   - *Why needed:* Assembles the pieces into the stated isomorphism.

---

# Lemma Decomposition

> [!note]- Lemma 1: The kernel of a ring homomorphism is an ideal
> **Statement:** For any ring homomorphism $\varphi : R \to S$, the set $\ker\varphi$ is an ideal of $R$: it is an additive subgroup, and it absorbs multiplication, $a \in \ker\varphi,\ b \in R \implies ab \in \ker\varphi$ and $ba \in \ker\varphi$.
>
> **Hint:** The additive-subgroup part is the group fact. For strong closure, compute $\varphi(ab)$ and use $0_S \cdot s = 0_S$.
>
> **Why needed:** It guarantees $R/\ker\varphi$ is a ring, so that the source of $\Phi$ exists. (This lemma is independently the proof that "every kernel is an ideal".)
>
> > [!note]- Full proof
> > Since $\varphi$ is in particular a homomorphism of the additive groups $(R,+,0_R) \to (S,+,0_S)$, its kernel $\ker\varphi$ is an additive subgroup of $R$ — this is the group-theory fact, applied verbatim.
> >
> > For strong closure, let $a \in \ker\varphi$ and $b \in R$. Then
> > $$\varphi(ab) = \varphi(a)\,\varphi(b) = 0_S \cdot \varphi(b) = 0_S,$$
> > using that $\varphi$ is multiplicative and that $0_S \cdot s = 0_S$ for every $s \in S$ (a consequence of the distributive law). So $ab \in \ker\varphi$. Identically, $\varphi(ba) = \varphi(b)\varphi(a) = \varphi(b)\cdot 0_S = 0_S$, so $ba \in \ker\varphi$. Hence $\ker\varphi$ absorbs multiplication on both sides and is an ideal, $\ker\varphi \trianglelefteq R$.

> [!note]- Lemma 2: The additive part of the isomorphism is free
> **Statement:** For a ring homomorphism $\varphi : R \to S$, the map $\Phi(r + \ker\varphi) = \varphi(r)$ is a well-defined bijection from $R/\ker\varphi$ onto $\operatorname{im}\varphi$ that respects addition.
>
> **Hint:** Apply the first isomorphism theorem for groups to $\varphi : (R,+) \to (S,+)$; nothing here uses multiplication.
>
> **Why needed:** It discharges every claim about $\Phi$ except multiplicativity, so the ring proof reduces to a single extra line.
>
> > [!note]- Full proof
> > Regard $\varphi$ as a homomorphism of additive groups $(R,+,0_R) \to (S,+,0_S)$. The first isomorphism theorem for groups (see [[Thm - First Isomorphism Theorem]]) applied to this additive group homomorphism states that the assignment $r + \ker\varphi \mapsto \varphi(r)$ is a well-defined group isomorphism from $(R,+)/\ker\varphi$ onto $\operatorname{im}\varphi$. "Well-defined" means: if $r + \ker\varphi = r' + \ker\varphi$ then $r - r' \in \ker\varphi$, so $\varphi(r) - \varphi(r') = \varphi(r - r') = 0_S$, giving $\varphi(r) = \varphi(r')$. "Group isomorphism" gives bijectivity onto $\operatorname{im}\varphi$ and additivity, $\Phi\big((r+\ker\varphi)+(r'+\ker\varphi)\big) = \varphi(r+r') = \varphi(r) + \varphi(r')$. The additive coset of $R/\ker\varphi$ and the additive coset of the group $(R,+)/\ker\varphi$ are literally the same set, so $\Phi$ is exactly that group isomorphism, viewed as a map of the underlying sets of the quotient ring and the subring $\operatorname{im}\varphi$.

> [!note]- Lemma 3: An additive ring-bijection that is multiplicative is a ring isomorphism
> **Statement:** Let $\Phi : A \to B$ be a bijection between rings that respects addition, respects multiplication, and sends $1_A$ to $1_B$. Then $\Phi$ is a ring isomorphism; in particular $\Phi^{-1}$ is also a ring homomorphism.
>
> **Hint:** Transport each ring axiom across $\Phi^{-1}$ by writing elements of $B$ as $\Phi$ of elements of $A$.
>
> **Why needed:** It is the final assembly step: once $\Phi$ is shown additive (free, Lemma 2) and multiplicative, this lemma upgrades it to a genuine ring isomorphism with no further work.
>
> > [!note]- Full proof
> > A ring homomorphism that is bijective is by definition a ring isomorphism, so it suffices to confirm $\Phi$ is a ring homomorphism — which it is, being additive, multiplicative, and unit-preserving by hypothesis — and that the set-theoretic inverse $\Phi^{-1} : B \to A$ is again a ring homomorphism. Take $b_1, b_2 \in B$ and write $b_1 = \Phi(a_1)$, $b_2 = \Phi(a_2)$. Since $\Phi$ respects addition, $\Phi(a_1 + a_2) = b_1 + b_2$, so $\Phi^{-1}(b_1 + b_2) = a_1 + a_2 = \Phi^{-1}(b_1) + \Phi^{-1}(b_2)$. Since $\Phi$ respects multiplication, $\Phi(a_1 a_2) = b_1 b_2$, so $\Phi^{-1}(b_1 b_2) = a_1 a_2 = \Phi^{-1}(b_1)\,\Phi^{-1}(b_2)$. Finally $\Phi(1_A) = 1_B$ gives $\Phi^{-1}(1_B) = 1_A$. So $\Phi^{-1}$ is a ring homomorphism and $\Phi$ is a ring isomorphism.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\varphi : R \to S$ be a ring homomorphism.
>
> **Step 0 — the quotient exists.** By Lemma 1, $\ker\varphi$ is an ideal of $R$, so the quotient ring $R/\ker\varphi$ is defined, with addition $(r + \ker\varphi) + (r' + \ker\varphi) = (r + r') + \ker\varphi$ and multiplication $(r + \ker\varphi)(r' + \ker\varphi) = rr' + \ker\varphi$.
>
> **Step 1 — define the map.** Define
> $$\Phi : R/\ker\varphi \longrightarrow \operatorname{im}\varphi, \qquad \Phi(r + \ker\varphi) = \varphi(r).$$
>
> **Step 2 — well-definedness, bijectivity, and additivity come for free.** Regard $\varphi$ as a homomorphism of additive groups $(R,+,0_R) \to (S,+,0_S)$. By the first isomorphism theorem for groups (Lemma 2), the assignment $r + \ker\varphi \mapsto \varphi(r)$ is a well-defined bijection of $R/\ker\varphi$ onto $\operatorname{im}\varphi$ that respects addition. Concretely: if $r + \ker\varphi = r' + \ker\varphi$ then $r - r' \in \ker\varphi$, so $\varphi(r) - \varphi(r') = \varphi(r-r') = 0_S$ and $\Phi$ is well-defined; it is surjective onto $\operatorname{im}\varphi$ since every element of the image is $\varphi(r) = \Phi(r + \ker\varphi)$ for some $r$; it is injective since $\varphi(r) = \varphi(r')$ forces $\varphi(r - r') = 0_S$, hence $r - r' \in \ker\varphi$ and equal cosets; and it is additive. We therefore do **not** re-prove any of this — it is exactly the group theorem.
>
> **Step 3 — $\Phi$ is multiplicative.** This is the only ring-specific check. For cosets $r + \ker\varphi$ and $t + \ker\varphi$, using the definition of multiplication in the quotient ring and that $\varphi$ is multiplicative,
> $$\Phi\big((r + \ker\varphi)(t + \ker\varphi)\big) = \Phi(rt + \ker\varphi) = \varphi(rt) = \varphi(r)\,\varphi(t) = \Phi(r + \ker\varphi)\,\Phi(t + \ker\varphi).$$
>
> **Step 4 — $\Phi$ preserves the identity.** $\Phi(1_R + \ker\varphi) = \varphi(1_R) = 1_S$, and $1_S \in \operatorname{im}\varphi$ is the identity of the subring $\operatorname{im}\varphi$.
>
> **Step 5 — conclude.** By Steps 2–4, $\Phi$ is a bijection that respects addition and multiplication and sends $1$ to $1$; by Lemma 3 it is a ring isomorphism. Therefore
> $$R/\ker\varphi \;\cong\; \operatorname{im}\varphi \;\leq\; S. \qquad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Adjoining a root and the structure of $\mathbb{C}$.** The flagship application is $\mathbb{R}[X]/(X^2+1) \cong \mathbb{C}$. Evaluate at $i$: the homomorphism $\varphi : \mathbb{R}[X] \to \mathbb{C}$, $X \mapsto i$, is surjective and has kernel $(X^2+1)$. What is non-obvious is that the *quotient construction* and the *familiar field $\mathbb{C}$* are the same object — the property $B$ "the numerator is a polynomial ring and the ideal is generated by an irreducible quadratic" is recognised, and the theorem converts a quotient that looks like a bag of cosets into the complex numbers. The same move gives $\mathbb{R}[X]/(X^2+1) \cong \mathbb{C}$'s cousins: $\mathbb{Q}[X]/(X^2-2) \cong \mathbb{Q}(\sqrt 2)$, and more generally $F[X]/(p)$ is the field obtained by adjoining a root of an irreducible $p$ — the engine of field extension theory.

**Reduction modulo a prime in number theory.** Reduction $\mathbb{Z}[X] \to \mathbb{F}_p[X]$, coefficient-wise mod $p$, is a surjective ring homomorphism with kernel $(p)$, so $\mathbb{Z}[X]/(p) \cong \mathbb{F}_p[X]$. This is non-obvious as an *application of an isomorphism theorem* because the "reduction mod $p$" trick — used constantly to prove a polynomial is irreducible over $\mathbb{Q}$ by checking irreducibility mod $p$ — is rarely *stated* as the first isomorphism theorem, yet that is exactly what licenses passing between $\mathbb{Z}[X]/(p)$ and $\mathbb{F}_p[X]$.

**The evaluation map and varieties in algebraic geometry.** For a field $k$, evaluation at a point $a \in k^n$ gives a surjective ring homomorphism $\operatorname{ev}_a : k[X_1,\dots,X_n] \to k$, $f \mapsto f(a)$, whose kernel is the maximal ideal $\mathfrak{m}_a = (X_1 - a_1, \dots, X_n - a_n)$. The theorem yields $k[X_1,\dots,X_n]/\mathfrak{m}_a \cong k$. The non-obvious recognition is that points of affine space $k^n$ correspond to maximal [[Def - Ideal|ideals]] with [[Def - Residue|residue]] field $k$ — the seed of the dictionary between geometry and ring theory. Property $B$ here is "a point evaluation", and spotting that point evaluation is a ring homomorphism (not just additive) is the whole step.

**Functions on a disconnected space.** Let $X = X_1 \sqcup X_2$ be a disjoint union and $C(X)$ the ring of continuous real-valued functions. Restriction $\rho : C(X) \to C(X_1)$, $f \mapsto f|_{X_1}$, is a surjective ring homomorphism whose kernel is the ideal of functions vanishing on $X_1$. The theorem gives $C(X)/\ker\rho \cong C(X_1)$. This is an out-of-distribution application because $C(X)$ is an infinite-dimensional, analytically defined ring, yet the purely algebraic isomorphism theorem still identifies the quotient — the disguised source is that restriction respects pointwise multiplication, so it is a *ring* homomorphism, not merely additive or linear.

---

# Bridges

- **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem for Groups]]** — the prototype, and literally the engine of this proof. Applied to the additive group $(R,+)$, the group theorem hands over the entire additive content (kernel an additive subgroup, $\Phi$ a well-defined additive bijection); the ring theorem only adds that the kernel absorbs multiplication and that $\Phi$ is multiplicative. The two theorems are the same statement in different categories — replace "group" by "ring", "normal subgroup" by "ideal", "group homomorphism" by "ring homomorphism".

- **[[Thm - Second Isomorphism Theorem for Rings|Second Isomorphism Theorem for Rings]]** — a direct corollary. Applying this theorem to the composite homomorphism $R \hookrightarrow S \twoheadrightarrow S/J$ produces $R/(R \cap J) \cong (R+J)/J$ in one line; the kernel of the composite is $R \cap J$ and its image is $(R+J)/J$.

- **[[Thm - Third Isomorphism Theorem for Rings|Third Isomorphism Theorem for Rings]]** — also a direct corollary. Applying this theorem to the homomorphism $R/I \to R/J$, $r + I \mapsto r + J$ (for ideals $I \subseteq J$), produces $(R/I)/(J/I) \cong R/J$; the kernel is $J/I$ and the map is surjective.

- **[[Thm - Ideal Correspondence|Ideal Correspondence]]** — the companion result. Where this theorem identifies the quotient *ring*, the ideal correspondence describes the quotient's *ideal lattice*; together they pin down everything about $R/I$ in terms of $R$.

- **Isomorphism theorems for modules and vector spaces** — the same theorem again. Replace "ring" by "module" and "ideal" by "submodule"; the rank–nullity theorem $\dim V = \dim\ker T + \dim\operatorname{im} T$ is the vector-space shadow, obtained by taking dimensions in $V/\ker T \cong \operatorname{im} T$.

---

# Unlocked by This

> [!tip] Field Extensions by Adjoining Roots *(from Field Theory)*
> Because $F[X]/(p)$ is a field whenever $p$ is irreducible, the first isomorphism theorem identifies the field $F(\alpha)$ obtained by adjoining a root $\alpha$ of $p$ as exactly this quotient. This is the foundation of the entire theory of field extensions and, downstream, of Galois theory.

> [!tip] Prime and Maximal Ideals *(from Commutative Algebra)*
> The theorem converts "$R/I$ is an integral domain" into "$I$ is a prime ideal" and "$R/I$ is a field" into "$I$ is a maximal ideal". Exhibiting a surjection onto a domain or a field is the standard way to certify an ideal as prime or maximal.

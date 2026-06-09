---
type: exercise
subject: commutative-algebra
difficulty: "⭐"
prereqs:
  - "Def - Prime and Maximal Ideal"
  - "Def - Multiplicative Set and Localization"
  - "Def - Local Ring and Residue Field"
  - "Thm - Prime Ideals of a Localization"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $\mathfrak{p}\trianglelefteq R$ be a [[Def - Prime and Maximal Ideal|prime ideal]] and $R_{\mathfrak{p}} = (R\setminus\mathfrak{p})^{-1}R$ the [[Def - Multiplicative Set and Localization|localization at 𝔭]]. Prove that $R_{\mathfrak{p}}$ is a [[Def - Local Ring and Residue Field|local ring]] with unique maximal ideal
$$\mathfrak{p}R_{\mathfrak{p}} = \mathfrak{p}^e = \left\{\tfrac as : a\in\mathfrak{p},\ s\notin\mathfrak{p}\right\}.$$
Give two proofs: one directly from the fraction model (a fraction $\tfrac rs$ is a unit iff $r\notin\mathfrak{p}$, so the non-units form an ideal), and one from the [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]] (the surviving primes are those $\subseteq\mathfrak{p}$, of which $\mathfrak{p}$ is the largest). Deduce that $\mathbb{Z}_{(p)}$ is local with maximal ideal $(p)\mathbb{Z}_{(p)}$ and residue field $\mathbb{F}_p$.

**Recall:**

![[Def - Local Ring and Residue Field#Local ring]]

A ring is [[Def - Local Ring and Residue Field|local]] precisely when it has a unique maximal ideal, equivalently when its non-units form an ideal. The set $S = R\setminus\mathfrak{p}$ is [[Def - Multiplicative Set and Localization|multiplicative]] exactly because $\mathfrak{p}$ is prime: $1\notin\mathfrak{p}$ and a product of two elements outside $\mathfrak{p}$ stays outside $\mathfrak{p}$ (the contrapositive of primality).

![[Thm - Prime Ideals of a Localization#Statement]]

For $S = R\setminus\mathfrak{p}$, a prime $\mathfrak{q}$ satisfies $\mathfrak{q}\cap S = \varnothing\iff\mathfrak{q}\subseteq\mathfrak{p}$, so the surviving primes are exactly the primes contained in $\mathfrak{p}$.

---

# Convergent Strategy

**Problem class.** This is a *structural identification* problem: show a constructed ring has a named property (locality). As the [[Commutative Algebra IV — Localization#Problem-Solving Strategy|topic strategy]] records, questions about the ideals or primes of a localization route through one of two tools — the explicit fraction model or the prime-correspondence theorem — and here we are asked to do both, which is instructive because the two proofs illuminate "local" from the two angles "non-units form an ideal" and "unique maximal survivor".

**Assumption pattern.** The single hypothesis "$\mathfrak{p}$ is prime" is doing two jobs at once, and recognising both is the content. First, primality is exactly what makes $S = R\setminus\mathfrak{p}$ multiplicative, so the localization exists. Second, primality is what makes the complement of $\mathfrak{p}$ the *right* set to invert: inverting everything outside $\mathfrak{p}$ leaves only the behaviour at and below $\mathfrak{p}$, which is what "local" means.

**Theorem routing.** Direct route: from the fraction model, classify units — $\tfrac rs$ is a unit iff its numerator $r\notin\mathfrak{p}$ (then $\tfrac sr$ is an inverse) — so the non-units are exactly $\{\tfrac rs : r\in\mathfrak{p}\} = \mathfrak{p}R_{\mathfrak{p}}$, which is an ideal, giving locality by the "non-units form an ideal" criterion of [[Def - Local Ring and Residue Field]]. Abstract route: by [[Thm - Prime Ideals of a Localization|the prime correspondence]], $\operatorname{Spec}(R_{\mathfrak{p}})$ is the primes $\subseteq\mathfrak{p}$, extended; $\mathfrak{p}$ is the unique maximal one, so $\mathfrak{p}R_{\mathfrak{p}}$ is the unique maximal ideal.

**Key decision point.** The one non-obvious move is the *unit classification* in the direct proof: realising that invertibility of $\tfrac rs$ depends only on whether the numerator $r$ lies in $\mathfrak{p}$, with the denominator irrelevant (it is already a unit). The natural wrong instinct is to try to show the non-units are closed under addition by brute fraction arithmetic; the clean path is to *characterise the units first*, after which "non-units $= \mathfrak{p}R_{\mathfrak{p}}$" makes their being an ideal automatic.

---

# Legal Operations Used

This solution deploys the following [[Commutative Algebra IV — Localization#Legal Operations|legal operations from the topic page]]:

1. **Operation 6 (read primes off the disjointness condition).** For $S = R\setminus\mathfrak{p}$, the surviving primes are those disjoint from $S$, i.e. the primes $\subseteq\mathfrak{p}$ — the abstract proof's engine.

2. **Operation 1 (clear denominators).** Used implicitly to verify that $\tfrac sr$ is a genuine inverse of $\tfrac rs$ when $r\notin\mathfrak{p}$: the product $\tfrac{rs}{sr} = \tfrac11$.

3. **Operation 8 (pass between $R_{\mathfrak{p}}$, $R/\mathfrak{p}$, and $\kappa(\mathfrak{p})$).** Used in the deduction that the residue field of $\mathbb{Z}_{(p)}$ is $\mathbb{F}_p$.

---

# Hints

> [!note]- Hint 1
> "Local" has an equivalent form that is far easier to verify than "unique maximal ideal": *the non-units form an ideal*. So classify the non-units of $R_{\mathfrak{p}}$. A fraction $\tfrac rs$ has $s$ already invertible (it is $\tfrac1s$); so invertibility of $\tfrac rs$ hinges entirely on the numerator $r$. When is $\tfrac rs$ a unit?

> [!note]- Hint 2
> $\tfrac rs$ is a unit iff $r\notin\mathfrak{p}$: if $r\notin\mathfrak{p}$ then $r\in S$, so $\tfrac sr\in R_{\mathfrak{p}}$ and $\tfrac rs\cdot\tfrac sr = 1$. Conversely if $r\in\mathfrak{p}$, no inverse exists (it would force $1\in\mathfrak{p}R_{\mathfrak{p}}$, contradicting properness). So the non-units are exactly $\{\tfrac rs : r\in\mathfrak{p}\} = \mathfrak{p}R_{\mathfrak{p}}$. Why is this set an ideal?

> [!note]- Hint 3
> For the abstract proof, apply the [[Thm - Prime Ideals of a Localization|prime correspondence]] with $S = R\setminus\mathfrak{p}$. A prime $\mathfrak{q}$ survives iff $\mathfrak{q}\cap S = \varnothing$ iff $\mathfrak{q}\subseteq\mathfrak{p}$. Among all surviving primes, which is the largest, and why does a unique maximal survivor mean the localization is local?

---

# Solution

The two proofs attack "local" from its two equivalent definitions. The direct proof classifies units (a fraction is a unit iff its numerator avoids $\mathfrak{p}$) and reads off that the non-units are exactly the ideal $\mathfrak{p}R_{\mathfrak{p}}$. The abstract proof invokes the prime correspondence to see that the surviving primes are those $\subseteq\mathfrak{p}$, with $\mathfrak{p}$ the unique maximal one. Both conclude $\mathfrak{p}R_{\mathfrak{p}}$ is the unique maximal ideal.

**Step 1: The set $S = R\setminus\mathfrak{p}$ is multiplicative, so $R_{\mathfrak{p}}$ exists.**

Primality of $\mathfrak{p}$ gives $1\in S$ (as $1\notin\mathfrak{p}$) and closure under products.

> [!note]- Derivation
> Since $\mathfrak{p}$ is a proper ideal, $1\notin\mathfrak{p}$, so $1\in S$. If $a, b\in S$, i.e. $a, b\notin\mathfrak{p}$, then $ab\notin\mathfrak{p}$ — this is exactly the contrapositive of the defining property of a [[Def - Prime and Maximal Ideal|prime]] ($ab\in\mathfrak{p}\Rightarrow a\in\mathfrak{p}$ or $b\in\mathfrak{p}$). So $S$ is closed under multiplication, hence a [[Def - Multiplicative Set and Localization|multiplicative subset]], and $R_{\mathfrak{p}} = S^{-1}R$ is defined.

**Step 2 (direct proof): A fraction $\tfrac rs$ is a unit of $R_{\mathfrak{p}}$ iff $r\notin\mathfrak{p}$.**

The denominator is already invertible, so invertibility is controlled by the numerator.

> [!note]- Derivation
> ($r\notin\mathfrak{p}\Rightarrow$ unit) If $r\notin\mathfrak{p}$, then $r\in S$, so $\tfrac sr\in R_{\mathfrak{p}}$ is a legitimate fraction, and $\tfrac rs\cdot\tfrac sr = \tfrac{rs}{sr} = \tfrac11 = 1$. So $\tfrac rs$ is a unit with inverse $\tfrac sr$.
>
> ($r\in\mathfrak{p}\Rightarrow$ non-unit) Suppose $\tfrac rs$ with $r\in\mathfrak{p}$ had an inverse $\tfrac ab$. Then $\tfrac{ra}{sb} = 1$, so $u(ra - sb) = 0$ for some $u\in S$, giving $ura = usb$. Now $ura\in\mathfrak{p}$ (as $r\in\mathfrak{p}$), so $usb\in\mathfrak{p}$; but $u, s, b\notin\mathfrak{p}$ — wait, $b$ need only be in $S$, so $b\notin\mathfrak{p}$ — and $\mathfrak{p}$ prime forces a factor of $usb$ into $\mathfrak{p}$, impossible since $u, s, b\in S = R\setminus\mathfrak{p}$. Contradiction. So $\tfrac rs$ is not a unit.

**Step 3 (direct proof): The non-units are exactly $\mathfrak{p}R_{\mathfrak{p}}$, an ideal; hence $R_{\mathfrak{p}}$ is local.**

By Step 2 the non-units are $\{\tfrac rs : r\in\mathfrak{p}\} = \mathfrak{p}R_{\mathfrak{p}}$, which is an ideal, so $R_{\mathfrak{p}}$ is local with that maximal ideal.

> [!note]- Derivation
> By Step 2, the set of non-units of $R_{\mathfrak{p}}$ is $\{\tfrac rs : r\in\mathfrak{p},\ s\notin\mathfrak{p}\} = S^{-1}\mathfrak{p} = \mathfrak{p}R_{\mathfrak{p}}$, which is the [[Def - Extension and Contraction of Ideals|extension]] $\mathfrak{p}^e$ — manifestly an ideal of $R_{\mathfrak{p}}$ (closed under addition and under multiplication by any $\tfrac ab\in R_{\mathfrak{p}}$, since $\mathfrak{p}$ is an ideal). By the [[Def - Local Ring and Residue Field|criterion]] "the non-units form an ideal $\Rightarrow$ that ideal is the unique maximal ideal", $R_{\mathfrak{p}}$ is local with maximal ideal $\mathfrak{p}R_{\mathfrak{p}}$. (Any proper ideal of $R_{\mathfrak{p}}$ consists of non-units, hence lies in $\mathfrak{p}R_{\mathfrak{p}}$, confirming uniqueness.)

**Step 4 (abstract proof): The prime correspondence gives a unique maximal survivor.**

The surviving primes are those $\subseteq\mathfrak{p}$, and $\mathfrak{p}$ is the largest, so $\mathfrak{p}R_{\mathfrak{p}}$ is the unique maximal ideal.

> [!note]- Derivation
> By [[Thm - Prime Ideals of a Localization|the prime-correspondence theorem]], extension gives a bijection $\{\mathfrak{q}\in\operatorname{Spec} R : \mathfrak{q}\cap S = \varnothing\}\xrightarrow{\sim}\operatorname{Spec}(R_{\mathfrak{p}})$, preserving inclusions. For $S = R\setminus\mathfrak{p}$, $\mathfrak{q}\cap S = \varnothing\iff\mathfrak{q}\subseteq\mathfrak{p}$. So $\operatorname{Spec}(R_{\mathfrak{p}}) = \{\mathfrak{q}^e : \mathfrak{q}\subseteq\mathfrak{p}\}$. Since the bijection preserves inclusions and $\mathfrak{p}$ is the largest prime among those $\subseteq\mathfrak{p}$ (it contains every such $\mathfrak{q}$), the extension $\mathfrak{p}^e = \mathfrak{p}R_{\mathfrak{p}}$ is the largest — hence the unique maximal — prime of $R_{\mathfrak{p}}$. A ring with a unique maximal ideal is local.

**Step 5: Deduce the example $\mathbb{Z}_{(p)}$.**

With $R = \mathbb{Z}$, $\mathfrak{p} = (p)$: $\mathbb{Z}_{(p)}$ is local with maximal ideal $(p)\mathbb{Z}_{(p)}$ and residue field $\mathbb{F}_p$.

> [!note]- Derivation
> Apply the result with $\mathfrak{p} = (p)$. Then $\mathbb{Z}_{(p)} = \{\tfrac ab : p\nmid b\}$ is local with maximal ideal $(p)\mathbb{Z}_{(p)} = \{\tfrac ab : p\mid a,\ p\nmid b\}$. The [[Def - Local Ring and Residue Field|residue field]] is $\kappa((p)) = \mathbb{Z}_{(p)}/(p)\mathbb{Z}_{(p)}$; sending $\tfrac ab\mapsto ab^{-1}\bmod p$ (legal as $p\nmid b$) gives an isomorphism onto $\mathbb{F}_p$, agreeing with $\operatorname{Frac}(\mathbb{Z}/(p)) = \mathbb{F}_p$.

> [!note]- Complete formal solution
> **Claim.** $R_{\mathfrak{p}}$ is local with unique maximal ideal $\mathfrak{p}R_{\mathfrak{p}}$.
>
> *Existence.* $\mathfrak{p}$ prime $\Rightarrow S = R\setminus\mathfrak{p}$ is multiplicative ($1\notin\mathfrak{p}$; $a, b\notin\mathfrak{p}\Rightarrow ab\notin\mathfrak{p}$), so $R_{\mathfrak{p}}$ is defined.
>
> *Direct proof.* A fraction $\tfrac rs\in R_{\mathfrak{p}}$ is a unit iff $r\notin\mathfrak{p}$: if $r\notin\mathfrak{p}$ then $r\in S$ and $\tfrac sr$ is an inverse; if $r\in\mathfrak{p}$, an inverse $\tfrac ab$ would give $ura = usb$ for some $u\in S$ with $ura\in\mathfrak{p}$ and $usb\notin\mathfrak{p}$ (all of $u, s, b\in S$), a contradiction. Hence the non-units of $R_{\mathfrak{p}}$ are exactly $\{\tfrac rs : r\in\mathfrak{p}\} = \mathfrak{p}R_{\mathfrak{p}}$, an ideal. A ring whose non-units form an ideal is local with that ideal maximal, so $R_{\mathfrak{p}}$ is local with maximal ideal $\mathfrak{p}R_{\mathfrak{p}}$.
>
> *Abstract proof.* By the prime correspondence, $\operatorname{Spec}(R_{\mathfrak{p}}) = \{\mathfrak{q}^e : \mathfrak{q}\subseteq\mathfrak{p}\}$, inclusion-preserving. $\mathfrak{p}$ is the largest such prime, so $\mathfrak{p}^e = \mathfrak{p}R_{\mathfrak{p}}$ is the unique maximal ideal; $R_{\mathfrak{p}}$ is local.
>
> *Example.* $\mathbb{Z}_{(p)}$ is local with maximal ideal $(p)\mathbb{Z}_{(p)}$ and residue field $\kappa((p)) = \mathbb{F}_p$. $\blacksquare$

---

# Key Takeaways

**Locality is checked by classifying the units, not by surveying ideals.** The whole direct proof rests on the equivalence "local $\iff$ non-units form an ideal", and the way to exploit it is always the same: *characterise the units first*. In a localization, a fraction $\tfrac rs$ has its denominator already inverted, so invertibility is entirely a question about the numerator, and the numerators that fail to invert are exactly those in the prime you localized at. Once you see the non-units are precisely $\mathfrak{p}R_{\mathfrak{p}}$ — a set that is *visibly* an ideal — locality is immediate, with no need to verify closure under addition by hand. The transferable trigger: whenever asked to show a ring is local, do not hunt for maximal ideals; instead pin down which elements are units and check the complement is an ideal. This same move proves $k[[X]]$ local (units $=$ nonzero constant term) and any quotient of a local ring local.

**The two proofs are the two faces of "local", and knowing both is knowing the concept.** The direct proof uses "non-units form an ideal"; the abstract proof uses "unique maximal ideal" via the surviving-primes count. They are not redundant — they illuminate different downstream uses. The fraction proof is what you reach for in a hands-on computation (identifying a specific local ring, finding its units); the prime-correspondence proof is what generalises (it tells you $\operatorname{Spec}(R_{\mathfrak{p}})$ is the primes $\subseteq\mathfrak{p}$, hence the *dimension* of $R_{\mathfrak{p}}$ is the height of $\mathfrak{p}$, and the local ring sees a neighbourhood of the point). Carrying both means that when a problem about a local ring arises, you can switch to whichever description makes it trivial.

**"Localize at a prime" is precisely engineered to invert everything *except* the point's vanishing functions.** The deep reason this construction yields a local ring is that the multiplicative set $R\setminus\mathfrak{p}$ is *the largest* set you can invert while keeping $\mathfrak{p}$ alive: invert anything in $\mathfrak{p}$ and the extension detonates to the whole ring (it meets $S$). So $R_{\mathfrak{p}}$ is the maximal localization in which $\mathfrak{p}$ survives, and $\mathfrak{p}R_{\mathfrak{p}}$ is forced to be the top prime. Geometrically, you have inverted every function nonzero *at the point* $\mathfrak{p}$, leaving a ring that can only see vanishing behaviour at and below $\mathfrak{p}$ — an arbitrarily small neighbourhood. This is why local rings are the natural setting for *local* questions, and why the residue field $\kappa(\mathfrak{p}) = R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}$ is "the field of values at the point": it is what remains after collapsing the maximal ideal of vanishing functions.

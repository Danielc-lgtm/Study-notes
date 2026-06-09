---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Multiplicative Set and Localization"
  - "Def - Extension and Contraction of Ideals"
  - "Thm - Prime Ideals of a Localization"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $S\subseteq R$ be a [[Def - Multiplicative Set and Localization|multiplicative subset]] and $I\trianglelefteq R$ an [[Def - Ideal|ideal]], with [[Def - Extension and Contraction of Ideals|extension]] taken along $\iota : R\to S^{-1}R$. Prove that radical and extension commute:
$$\sqrt{I}^{\,e} = \sqrt{I^e},$$
i.e. $S^{-1}(\sqrt I) = \sqrt{S^{-1}I}$. (The inclusion $\subseteq$ holds for *any* ring homomorphism; the content is $\supseteq$.) Deduce in particular that
$$(\operatorname{nil} R)^e = \operatorname{nil}(S^{-1}R),$$
so localization commutes with the [[Def - Radical of an Ideal and the Nilradical|nilradical]]: a fraction $\tfrac rs\in S^{-1}R$ is nilpotent iff $r$ is nilpotent in $R$ (after a clearing factor). This is Example Sheet 2, Q10(b).

**Recall:**

![[Def - Radical of an Ideal and the Nilradical#Radical of an ideal]]

![[Def - Extension and Contraction of Ideals#Explicit formulas for the localization map]]

For the localization map, $\mathfrak{a}^e = S^{-1}\mathfrak{a} = \{\tfrac as : a\in\mathfrak{a}, s\in S\}$. The [[Def - Radical of an Ideal and the Nilradical|radical]] is $\sqrt I = \{r : r^n\in I\text{ for some } n\geq 1\}$ and the nilradical is $\operatorname{nil} R = \sqrt{(0)}$.

---

# Convergent Strategy

**Problem class.** This is a *tracking-ideals-through-localization* problem of the cleanest kind: show that two operations (radical and extension) commute. Per the [[Commutative Algebra IV — Localization#Sources and Targets|topic targets]], establishing radical/nilpotence facts is one of the five recurring goals, and the standard lever is the explicit extension formula $\mathfrak{a}^e = S^{-1}\mathfrak{a}$ plus the power condition.

**Assumption pattern.** Nothing special is assumed — $S$ and $I$ are arbitrary. The recognisable feature is that *both* sides are defined by fraction-level conditions ($\tfrac rs\in S^{-1}(\sqrt I)$ means $r$ has a power in $I$; $\tfrac rs\in\sqrt{S^{-1}I}$ means some power of $\tfrac rs$ is in $S^{-1}I$), so the proof is a direct unwinding-and-matching of the two conditions, with the clearing factor mediating.

**Theorem routing.** The route is elementary and self-contained: take $\tfrac rs\in\sqrt{S^{-1}I}$, so $(\tfrac rs)^n = \tfrac{r^n}{s^n}\in S^{-1}I$; this means $\tfrac{r^n}{s^n} = \tfrac as$ for some $a\in I$, which after a clearing factor $u\in S$ gives $u s' r^n\in I$ for suitable $s'$; absorb $us'$ into the power to land an honest power of $r$ times an element of $S$ inside $I$, hence $r\in\sqrt I$ after multiplying by a unit-to-be — yielding $\tfrac rs\in S^{-1}(\sqrt I)$. No external theorem is needed beyond the fraction model; one *can* also argue via [[Thm - The Radical is the Intersection of the Primes Above It|$\sqrt{} = \bigcap\mathfrak{p}$]] and the [[Thm - Prime Ideals of a Localization|prime correspondence]], which gives a slicker conceptual proof.

**Key decision point.** The non-obvious move is handling the *denominator's contribution* to the power. When $(\tfrac rs)^n\in S^{-1}I$, the clearing factor and the power of $s$ both produce elements of $S$, and the trick is to absorb them so that a *single power* of $r$ (times something in $S$) lands in $I$ — this is where one must be careful that "$us' r^n\in I$ with $us'\in S$" upgrades to "$r\in\sqrt I$", which uses that $r^n$ times a unit-in-the-localization is what matters. The slick alternative — proving it via primes — sidesteps the bookkeeping entirely and is worth presenting as the conceptual route.

---

# Legal Operations Used

This solution deploys the following [[Commutative Algebra IV — Localization#Legal Operations|legal operations from the topic page]]:

1. **Operation 1 (clear denominators with a single $u\in S$).** The fraction equality $\tfrac{r^n}{s^n} = \tfrac as$ is pulled back to an honest equation in $R$ with a clearing factor.

2. **Operation 6 (read primes off disjointness) / the radical theorem.** The conceptual proof uses $\sqrt I = \bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$ and that localization intersects the primes with the survivors.

3. **Operation 7 (detect nilpotence by collapse).** The nilradical corollary $(\operatorname{nil} R)^e = \operatorname{nil}(S^{-1}R)$ is the $I = (0)$ specialisation, tying to "$R_f = 0\iff f$ nilpotent".

---

# Hints

> [!note]- Hint 1
> The inclusion $\sqrt{I}^{\,e}\subseteq\sqrt{I^e}$ is the easy half and holds for any ring map: if $r^n\in I$ then $\iota(r)^n = \iota(r^n)\in I^e$, so $\iota(r)\in\sqrt{I^e}$; extend to fractions. The work is $\supseteq$: take $\tfrac rs$ with $(\tfrac rs)^n\in S^{-1}I$ and produce a power of $r$ landing in $I$ (up to a clearing factor).

> [!note]- Hint 2
> $(\tfrac rs)^n = \tfrac{r^n}{s^n}\in S^{-1}I = I^e$ means $\tfrac{r^n}{s^n} = \tfrac at$ for some $a\in I$, $t\in S$. Clear denominators: there is $u\in S$ with $u(t r^n - s^n a) = 0$, i.e. $ut\,r^n = u s^n a\in I$. Now $ut\in S$. How do you turn "$(ut)r^n\in I$ with $ut\in S$" into "$r\in\sqrt I$"?

> [!note]- Hint 3
> Multiply $(ut)r^n\in I$ by $(ut)^{n-1}$: $(ut)^n r^n = (ut\,r)^n\in I$, so $ut\,r\in\sqrt I$. Hence $\tfrac{r}{s} = \tfrac{ut\,r}{ut\,s}\in S^{-1}(\sqrt I) = \sqrt{I}^{\,e}$ (the denominator $ut\,s\in S$). Alternatively, prove the whole statement at once: $\sqrt I = \bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$, and intersecting with the surviving primes commutes with extension.

---

# Solution

The easy inclusion is formal. For the hard one, take a fraction whose $n$-th power lies in $S^{-1}I$, clear denominators to land $(ut)r^n\in I$ with $ut\in S$, then multiply by $(ut)^{n-1}$ to exhibit $(ut\,r)^n\in I$, so $ut\,r\in\sqrt I$ and the fraction lies in $S^{-1}(\sqrt I)$. A conceptual second proof routes through $\sqrt I = \bigcap\mathfrak{p}$ and the prime correspondence.

**Step 1: The easy inclusion $\sqrt{I}^{\,e}\subseteq\sqrt{I^e}$.**

Powers commute with $\iota$, so an element with a power in $I$ has its image with a power in $I^e$.

> [!note]- Derivation
> A general element of $\sqrt{I}^{\,e} = S^{-1}(\sqrt I)$ is $\tfrac rs$ with $r\in\sqrt I$, so $r^n\in I$ for some $n$. Then $(\tfrac rs)^n = \tfrac{r^n}{s^n}$, and $\tfrac{r^n}{1}\in I^e$ (as $r^n\in I$), so $\tfrac{r^n}{s^n} = \tfrac1{s^n}\cdot\tfrac{r^n}{1}\in I^e$. Hence $(\tfrac rs)^n\in I^e = S^{-1}I$, so $\tfrac rs\in\sqrt{I^e}$. (This used only that $\iota$ is a ring map, so it holds generally.)

**Step 2: The hard inclusion $\sqrt{I^e}\subseteq\sqrt{I}^{\,e}$ — clear denominators.**

If $(\tfrac rs)^n\in S^{-1}I$, a clearing factor lands $(ut)r^n\in I$ with $ut\in S$.

> [!note]- Derivation
> Let $\tfrac rs\in\sqrt{I^e}$, so $(\tfrac rs)^n = \tfrac{r^n}{s^n}\in S^{-1}I$ for some $n\geq 1$. By the description of $S^{-1}I$, $\tfrac{r^n}{s^n} = \tfrac at$ for some $a\in I$, $t\in S$. Equality of fractions gives $u\in S$ with $u(t r^n - s^n a) = 0$, i.e.
> $$ut\,r^n = u s^n a\in I \quad(\text{since } a\in I).$$
> Write $w := ut\in S$ (a product of elements of $S$). So $w\,r^n\in I$.

**Step 3: Absorb the clearing factor into a single power.**

Multiplying by $w^{n-1}$ turns $w\,r^n\in I$ into $(wr)^n\in I$, so $wr\in\sqrt I$.

> [!note]- Derivation
> From $w r^n\in I$, multiply both sides by $w^{n-1}$:
> $$w^n r^n = (wr)^n\in I,$$
> since $I$ absorbs multiplication by $w^{n-1}\in R$. Hence $wr\in\sqrt I$. Therefore
> $$\tfrac rs = \tfrac{wr}{ws}\in S^{-1}(\sqrt I) = \sqrt{I}^{\,e},$$
> because $wr\in\sqrt I$ and $ws\in S$. This proves $\sqrt{I^e}\subseteq\sqrt{I}^{\,e}$, and with Step 1, equality.

**Step 4: The nilradical corollary.**

Setting $I = (0)$ gives $(\operatorname{nil} R)^e = \operatorname{nil}(S^{-1}R)$.

> [!note]- Derivation
> Take $I = (0)$: $\sqrt{(0)} = \operatorname{nil} R$ and $(0)^e = (0)$ in $S^{-1}R$, so $\sqrt{(0)^e} = \operatorname{nil}(S^{-1}R)$. The theorem gives $(\operatorname{nil} R)^e = \operatorname{nil}(S^{-1}R)$. Unwound: $\tfrac rs\in S^{-1}R$ is nilpotent iff $\tfrac rs\in S^{-1}(\operatorname{nil} R)$, iff $wr$ is nilpotent in $R$ for some $w\in S$ — i.e. a fraction is nilpotent exactly when its numerator becomes nilpotent after clearing by some element of $S$. In particular, if $R$ is [[Def - Radical of an Ideal and the Nilradical|reduced]] then so is $S^{-1}R$ (the localizable half of "reduced is local").

> [!note]- Conceptual second proof via primes
> By the [[Thm - The Radical is the Intersection of the Primes Above It|radical theorem]], $\sqrt I = \bigcap_{I\subseteq\mathfrak{p}}\mathfrak{p}$. Extension commutes with this intersection over surviving primes: by the [[Thm - Prime Ideals of a Localization|prime correspondence]], the primes of $S^{-1}R$ containing $I^e$ are exactly $\mathfrak{p}^e$ for primes $\mathfrak{p}\supseteq I$ with $\mathfrak{p}\cap S = \varnothing$, and for such $\mathfrak{p}$, $S^{-1}\mathfrak{p} = \mathfrak{p}^e$. Hence
> $$\sqrt{I^e} = \bigcap_{I^e\subseteq\mathfrak{q}}\mathfrak{q} = \bigcap_{\substack{I\subseteq\mathfrak{p} \\ \mathfrak{p}\cap S = \varnothing}}\mathfrak{p}^e = S^{-1}\Big(\bigcap_{I\subseteq\mathfrak{p}}\mathfrak{p}\Big) = S^{-1}(\sqrt I) = \sqrt{I}^{\,e},$$
> where the third equality uses that $S^{-1}$ commutes with the finite-type intersection of primes (and that primes meeting $S$ extend to the whole ring, contributing nothing). This is the geometric reason: "the functions vanishing on $V(I)$" restrict to "the functions vanishing on $V(I)\cap\operatorname{Spec}(S^{-1}R)$".

> [!note]- Complete formal solution
> **Claim.** $\sqrt{I}^{\,e} = \sqrt{I^e}$ for the localization map $\iota : R\to S^{-1}R$.
>
> *($\subseteq$)* If $r\in\sqrt I$, say $r^n\in I$, then for $\tfrac rs\in\sqrt{I}^{\,e}$, $(\tfrac rs)^n = \tfrac{r^n}{s^n}\in I^e$, so $\tfrac rs\in\sqrt{I^e}$.
>
> *($\supseteq$)* Let $\tfrac rs\in\sqrt{I^e}$, so $\tfrac{r^n}{s^n}\in S^{-1}I$ for some $n$. Then $\tfrac{r^n}{s^n} = \tfrac at$ with $a\in I$, $t\in S$, giving $u\in S$ with $ut\,r^n = us^n a\in I$. Put $w = ut\in S$; then $w r^n\in I$, and multiplying by $w^{n-1}$ gives $(wr)^n\in I$, so $wr\in\sqrt I$ and $\tfrac rs = \tfrac{wr}{ws}\in S^{-1}(\sqrt I) = \sqrt{I}^{\,e}$.
>
> Hence $\sqrt{I}^{\,e} = \sqrt{I^e}$. Taking $I = (0)$ yields $(\operatorname{nil} R)^e = \operatorname{nil}(S^{-1}R)$. $\blacksquare$

---

# Key Takeaways

**Commuting an operation past localization is a clear-denominators-then-absorb computation.** The engine of the hard inclusion is the universal localization move: a fraction-level membership ($(\tfrac rs)^n\in S^{-1}I$) is pulled back to an honest equation in $R$ by one clearing factor $u\in S$, after which the *algebra happens in $R$*, and the answer is pushed back up. The specific cleverness here — multiplying $wr^n\in I$ by $w^{n-1}$ to manufacture $(wr)^n\in I$ — is a reusable trick: *to upgrade "$w$ times an $n$-th power is in $I$" to "an $n$-th power is in $I$", multiply by $w^{n-1}$ so the $w$ joins the power*. This pattern recurs whenever you must move a stray multiplicative factor inside a radical, and recognising it is what makes the denominator bookkeeping tractable rather than mysterious.

**Two proofs, two lessons: the fraction proof computes, the prime proof explains.** The clear-denominators argument is mechanical and works in any ring; the prime-intersection argument reveals *why* the identity is true — radicals are intersections of primes, localization restricts the spectrum to the survivors, and intersection commutes with that restriction. The geometric statement "functions vanishing on $V(I)$ restrict to functions vanishing on $V(I)\cap D$" is the content. When you meet a "does this commute with localization?" question, both routes are available: reach for the fraction proof to *verify*, and for the prime proof to *understand and generalise* (e.g., to see immediately that the identity localizes the Nullstellensatz dictionary).

**Localization commutes with the nilradical, so reducedness descends — the localizable half of a local property.** The corollary $(\operatorname{nil} R)^e = \operatorname{nil}(S^{-1}R)$ says nilpotents track exactly under localization: $S^{-1}R$ has no new nilpotents and loses none (beyond those whose numerator becomes nilpotent after clearing). Concretely, $R$ reduced $\Rightarrow S^{-1}R$ reduced. This is precisely the *localizable* direction of "[[Ex - Being reduced is a local property|reduced is a local property]]"; the harder *local-to-global* direction (all $R_{\mathfrak{p}}$ reduced $\Rightarrow R$ reduced) needs the annihilator argument of the [[Thm - The Local-Global Principle|local–global principle]]. Seeing this identity as "one half of a local property" is the right filing: it tells you what localization preserves for free, and flags what still requires the global-gluing machinery.

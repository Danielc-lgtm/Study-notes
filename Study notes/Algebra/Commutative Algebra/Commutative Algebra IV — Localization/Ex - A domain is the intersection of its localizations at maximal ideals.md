---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Integral Domain"
  - "Def - Field of Fractions"
  - "Def - Prime and Maximal Ideal"
  - "Def - Multiplicative Set and Localization"
  - "Def - Local Ring and Residue Field"
  - "Thm - The Local-Global Principle"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A$ be an [[Def - Integral Domain|integral domain]] with [[Def - Field of Fractions|fraction field]] $K = \operatorname{Frac}(A)$. For each prime $\mathfrak{p}$ the localization $A_{\mathfrak{p}}$ embeds canonically in $K$ (as $A$ is a domain, the localization maps are injective). Prove that
$$A = \bigcap_{\mathfrak{m}\in\operatorname{mSpec} A} A_{\mathfrak{m}},$$
the intersection taken inside $K$, where $\operatorname{mSpec} A$ is the set of maximal ideals. (This is Example Sheet 2, Q10(d).) The inclusion $A\subseteq\bigcap A_{\mathfrak{m}}$ is clear; the content is that an element of $K$ lying in *every* $A_{\mathfrak{m}}$ already lies in $A$.

**Recall:**

![[Def - Integral Domain#The Definition]]

For a [[Def - Integral Domain|domain]] $A$, every localization $A_{\mathfrak{p}}\subseteq K = \operatorname{Frac}(A)$ is the subring $\{\tfrac ab : b\notin\mathfrak{p}\}$, and the [[Def - Multiplicative Set and Localization|localization map]] $A\to A_{\mathfrak{p}}$ is injective (no zero-divisors in $S = A\setminus\mathfrak{p}$).

![[Thm - The Local-Global Principle#Statement]]

The key tool is the [[Thm - The Local-Global Principle|local–global principle]]: surjectivity of an $A$-linear map is a local property, and being zero is local (the annihilator argument). For $x\in K$, the set $(A :_A x) = \{a\in A : ax\in A\}$ is the **ideal of denominators** of $x$; $x\in A\iff(A : x) = A\iff 1\in(A:x)$.

---

# Convergent Strategy

**Problem class.** This is a *local-to-global equality* problem: prove a global object equals an intersection of its localizations. Per the [[Commutative Algebra IV — Localization#Problem-Solving Strategy|topic strategy]], such statements are proved by recognising the desired equality as the surjectivity (or injectivity) of a natural map, which is a *local property*, then checking it at each maximal ideal where it becomes trivial.

**Assumption pattern.** Two hypotheses do the work. "$A$ is a domain" makes every $A_{\mathfrak{p}}$ a subring of the single field $K$, so the intersection $\bigcap A_{\mathfrak{m}}$ even *makes sense* (all localizations live in one ambient field). The recognisable trigger is "an element of $K$ lies in every $A_{\mathfrak{m}}$" — this is a statement about the *ideal of denominators* $(A : x)$, and "$x\in A$" is "$(A:x) = A$", a question about whether an ideal is the whole ring, which is decided locally.

**Theorem routing.** Two equivalent routes. *Denominator route:* for $x\in\bigcap A_{\mathfrak{m}}$, the ideal of denominators $(A : x)$ is contained in no maximal ideal (at each $\mathfrak{m}$, $x\in A_{\mathfrak{m}}$ supplies a denominator outside $\mathfrak{m}$), so $(A:x) = A$, so $1\in(A:x)$, so $x\in A$. *Local–global route:* the inclusion $A\hookrightarrow\bigcap A_{\mathfrak{m}}$ is an $A$-linear map that is locally an isomorphism (localizing at $\mathfrak{m}$ gives $A_{\mathfrak{m}} = A_{\mathfrak{m}}$), and surjectivity is a [[Thm - The Local-Global Principle|local property]], so the inclusion is onto. Both bottom out in the same annihilator/maximal-ideal lemma.

**Key decision point.** The non-obvious move is introducing the *ideal of denominators* $(A : x) = \{a : ax\in A\}$ and recognising that "$x\in A_{\mathfrak{m}}$" means "$(A:x)\not\subseteq\mathfrak{m}$" (some denominator of $x$ avoids $\mathfrak{m}$). Once you see "$x\in$ every $A_{\mathfrak{m}}$" as "$(A:x)$ misses every maximal ideal", the conclusion "$(A:x) = A$" is the standard "an ideal in no maximal ideal is the unit ideal". The natural wrong instinct is to manipulate fractions $x = \tfrac ab$ directly; the clean path is the ideal-of-denominators reformulation, which is exactly the annihilator argument in disguise.

---

# Legal Operations Used

This solution deploys the following [[Commutative Algebra IV — Localization#Legal Operations|legal operations from the topic page]]:

1. **Operation 5 (test for zero / membership with maximal ideals).** "$x\in A_{\mathfrak{m}}$" is read as "$(A:x)\not\subseteq\mathfrak{m}$", and an ideal in no maximal ideal is $A$.

2. **Operation 4 (reduce a global statement to local rings).** The local–global route recasts the inclusion $A\hookrightarrow\bigcap A_{\mathfrak{m}}$ as a locally-iso map and uses that surjectivity is local.

3. **Operation 8 (pass between $A$, $A_{\mathfrak{p}}$, and $K$).** Used throughout to view all localizations as subrings of the common field $K = \operatorname{Frac}(A)$.

---

# Hints

> [!note]- Hint 1
> Take $x\in\bigcap_{\mathfrak{m}}A_{\mathfrak{m}}\subseteq K$; you want $x\in A$. The set of "denominators that work" for $x$ is $(A : x) = \{a\in A : ax\in A\}$, an ideal of $A$. Restate "$x\in A$" in terms of this ideal. And restate "$x\in A_{\mathfrak{m}}$" in terms of it.

> [!note]- Hint 2
> "$x\in A$" $\iff 1\in(A:x)\iff(A:x) = A$. And "$x\in A_{\mathfrak{m}}$" means $x = \tfrac ab$ with $b\notin\mathfrak{m}$, i.e. there is a denominator $b\in(A:x)$ with $b\notin\mathfrak{m}$, i.e. $(A:x)\not\subseteq\mathfrak{m}$. So if $x$ lies in *every* $A_{\mathfrak{m}}$, what does that say about $(A:x)$ versus the maximal ideals?

> [!note]- Hint 3
> $(A:x)$ is contained in *no* maximal ideal. But every proper ideal is contained in some maximal ideal (Zorn). So $(A:x)$ is not proper: $(A:x) = A$, hence $1\in(A:x)$, hence $x = 1\cdot x\in A$. Done. (Equivalently: the inclusion $A\hookrightarrow\bigcap A_{\mathfrak{m}}$ localizes at each $\mathfrak{m}$ to the identity $A_{\mathfrak{m}} = A_{\mathfrak{m}}$, so it is surjective by the local–global principle.)

---

# Solution

The inclusion $\subseteq$ is immediate. For $\supseteq$, take $x$ in every $A_{\mathfrak{m}}$ and study its ideal of denominators $(A:x)$: membership in $A_{\mathfrak{m}}$ forces a denominator outside $\mathfrak{m}$, so $(A:x)$ escapes every maximal ideal, hence equals $A$, hence contains $1$, hence $x\in A$.

**Step 1: The easy inclusion $A\subseteq\bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$.**

Each $a\in A$ maps to $\tfrac a1\in A_{\mathfrak{m}}$ for every $\mathfrak{m}$.

> [!note]- Derivation
> For $a\in A$ and any maximal ideal $\mathfrak{m}$, $a = \tfrac a1\in A_{\mathfrak{m}}$ (the image of $a$ under the injective localization map $A\hookrightarrow A_{\mathfrak{m}}\subseteq K$). So $a\in\bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$, giving $A\subseteq\bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$. (All these inclusions are inside the fixed field $K = \operatorname{Frac}(A)$, which is why the intersection is well-defined.)

**Step 2: The ideal of denominators and two reformulations.**

For $x\in K$, set $(A:x) = \{a\in A : ax\in A\}$. Then $x\in A\iff(A:x) = A$, and $x\in A_{\mathfrak{m}}\iff(A:x)\not\subseteq\mathfrak{m}$.

> [!note]- Derivation
> $(A:x)$ is an ideal of $A$: if $a_1, a_2\in(A:x)$ then $(a_1 - a_2)x = a_1 x - a_2 x\in A$, and for $r\in A$, $(ra)x = r(ax)\in A$.
>
> *"$x\in A\iff(A:x) = A$":* if $x\in A$ then every $a\in A$ has $ax\in A$, so $(A:x) = A$; conversely if $(A:x) = A$ then $1\in(A:x)$, i.e. $1\cdot x = x\in A$.
>
> *"$x\in A_{\mathfrak{m}}\iff(A:x)\not\subseteq\mathfrak{m}$":* $x\in A_{\mathfrak{m}} = \{\tfrac ab : b\notin\mathfrak{m}\}$ means $x = \tfrac ab$ with $a\in A$, $b\notin\mathfrak{m}$, i.e. $bx = a\in A$, i.e. $b\in(A:x)$ with $b\notin\mathfrak{m}$ — exactly $(A:x)\not\subseteq\mathfrak{m}$. Conversely a denominator $b\in(A:x)\setminus\mathfrak{m}$ gives $x = \tfrac{bx}{b}\in A_{\mathfrak{m}}$ since $bx\in A$ and $b\notin\mathfrak{m}$.

**Step 3: The hard inclusion via "no maximal ideal contains $(A:x)$".**

If $x\in\bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$ then $(A:x)$ lies in no maximal ideal, so $(A:x) = A$ and $x\in A$.

> [!note]- Derivation
> Suppose $x\in A_{\mathfrak{m}}$ for *every* maximal ideal $\mathfrak{m}$. By Step 2, $(A:x)\not\subseteq\mathfrak{m}$ for every $\mathfrak{m}$ — the ideal of denominators escapes every maximal ideal. But any *proper* ideal of $A$ is contained in some maximal ideal (Zorn's lemma applied to the proper ideals above it). Since $(A:x)$ is in no maximal ideal, it cannot be proper: $(A:x) = A$. By Step 2, $x\in A$. Hence $\bigcap_{\mathfrak{m}}A_{\mathfrak{m}}\subseteq A$, and with Step 1, equality.

**Step 4: The local–global reformulation.**

The same proof, phrased as "the inclusion is locally an isomorphism, and surjectivity is local".

> [!note]- Derivation
> View $\iota : A\hookrightarrow B := \bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$ as an injective $A$-linear map. We claim it is surjective. By the [[Thm - The Local-Global Principle|local–global principle]], surjectivity is a local property, so it suffices to show $\iota_{\mathfrak{m}} : A_{\mathfrak{m}}\to B_{\mathfrak{m}}$ is surjective for every maximal $\mathfrak{m}$. Localizing at $\mathfrak{m}$, $A_{\mathfrak{m}}\subseteq B_{\mathfrak{m}}\subseteq A_{\mathfrak{m}}$ inside $K$ — indeed $B\subseteq A_{\mathfrak{m}}$ already (the intersection lies in each factor), and localizing the inclusion $A_{\mathfrak{m}}\subseteq B$ gives $A_{\mathfrak{m}}\subseteq B_{\mathfrak{m}}\subseteq A_{\mathfrak{m}}$, so $A_{\mathfrak{m}} = B_{\mathfrak{m}}$ and $\iota_{\mathfrak{m}}$ is an isomorphism. Surjective at every $\mathfrak{m}$, hence surjective, hence $A = B$. This is the same annihilator argument repackaged: "$\operatorname{coker}\iota = 0$ because it vanishes at every maximal ideal".

> [!note]- Complete formal solution
> **Claim.** $A = \bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$ inside $K = \operatorname{Frac}(A)$.
>
> *($\subseteq$)* Each $a\in A$ is $\tfrac a1\in A_{\mathfrak{m}}$ for all $\mathfrak{m}$.
>
> *($\supseteq$)* Let $x\in\bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$ and set $(A:x) = \{a\in A : ax\in A\}$, an ideal. For each maximal $\mathfrak{m}$, $x\in A_{\mathfrak{m}}$ means $x = \tfrac ab$ with $b\notin\mathfrak{m}$, so $b\in(A:x)\setminus\mathfrak{m}$, whence $(A:x)\not\subseteq\mathfrak{m}$. As this holds for every maximal ideal and every proper ideal lies in some maximal ideal, $(A:x)$ is not proper: $(A:x) = A$, so $1\in(A:x)$ and $x\in A$.
>
> Hence $A = \bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$. $\blacksquare$

---

# Key Takeaways

**The ideal of denominators converts "$x\in A$?" into "is this ideal the whole ring?", which is decided at maximal ideals.** The pivot of the proof is the construction $(A : x) = \{a : ax\in A\}$ and the two translations "$x\in A\iff(A:x) = A$" and "$x\in A_{\mathfrak{m}}\iff(A:x)\not\subseteq\mathfrak{m}$". These turn a membership question in the field $K$ into a question about whether an ideal escapes every maximal ideal — and "an ideal in no maximal ideal is the unit ideal" is the universal finisher. The transferable trigger: whenever you must show a fraction is integral (lies in $A$), form its ideal of denominators and show it is the whole ring by showing it misses every maximal ideal. This is the same device behind "the conductor", behind integrality criteria, and behind the local characterisation of when a rational function is regular.

**"Global $=$ intersection of localizations" is the surjectivity of an inclusion, hence a local property.** The deeper framing is that the statement $A = \bigcap A_{\mathfrak{m}}$ is *not* about elements at all but about the natural inclusion $A\hookrightarrow\bigcap A_{\mathfrak{m}}$ being surjective, and surjectivity is a [[Thm - The Local-Global Principle|local property]]. Localizing at $\mathfrak{m}$ collapses the intersection to the single factor $A_{\mathfrak{m}}$, making the map the identity, so it is locally onto, hence globally onto. The trigger to recognise: any claim of the form "this global object equals the intersection/limit of its local pieces" should be read as surjectivity (or an isomorphism) of a comparison map, then checked locally where it trivialises. This is the prototype for "a sheaf is determined by its sections on a cover" and for the gluing axiom of the structure sheaf.

**This is the algebraic statement "a rational function regular everywhere locally is globally regular".** Geometrically, $A_{\mathfrak{m}}$ is the ring of functions regular near the point $\mathfrak{m}$, and the theorem says a function of $K$ (a rational function on $\operatorname{Spec} A$) that is regular *at every point* is regular everywhere — it lies in $A$. This is the affine, domain case of the fundamental principle that regularity is a local condition assembled into a global one, and over a normal/smooth variety it is the statement that the global sections of the structure sheaf are exactly $A$. The result fails without the domain hypothesis (the localizations no longer share a common ambient field), which is why it is stated for domains; recognising *why* the domain hypothesis is load-bearing — it provides the single field $K$ in which all the $A_{\mathfrak{m}}$ live — is the structural lesson, paralleling how [[Ex - Being reduced is a local property|reducedness]] and [[Ex - Freeness is not a local property|freeness]] interact with the shape of the spectrum.

---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Primary Ideal"
  - "Def - Associated and Minimal Primes"
  - "Def - Prime and Maximal Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $R = k[X,Y]$ and $I = (X^2, XY)$, with minimal primary decompositions (from [[Ex - A primary decomposition in k[X,Y] with an embedded prime]])
$$I = (X) \cap (X,Y)^2 = (X) \cap (X^2, Y).$$
Prove the sharp form of the Second Uniqueness phenomenon:

1. **The isolated component is unique.** The component over the isolated prime $(X)$ is the *same* — namely $(X)$ — in every minimal primary decomposition of $I$. Prove this directly by localizing at $(X)$: the isolated component equals the contraction of $IR_{(X)}$, an object depending only on $I$.
2. **The embedded component is not unique.** The component over the embedded prime $(X,Y)$ genuinely differs: $(X,Y)^2 \neq (X^2, Y)$, and in fact there is an infinite family of valid embedded components $(X^2, XY, Y^n)$ for $n \geq 2$ (and more). Exhibit at least three distinct minimal primary decompositions of $I$.
3. **What is invariant.** Conclude that across all minimal decompositions, the associated primes $\{(X), (X,Y)\}$ and the isolated component $(X)$ are fixed, but the embedded $(X,Y)$-primary component ranges over infinitely many ideals.

**Recall:**

The objects in play are isolated versus embedded primes, primary components, and localization at a prime.

![[Def - Associated and Minimal Primes#Isolated (minimal) and embedded primes]]

The **isolated** primes of $I$ are the minimal elements of $\operatorname{Ass}(I)$; the **embedded** primes are the rest. The **Second Uniqueness Theorem** states that the isolated primary components are determined by $I$ — concretely, the component over an isolated prime $\mathfrak{p}_i$ is $\mathfrak{q}_i = I^{ec}$, the contraction of the extension $IR_{\mathfrak{p}_i}$ along the [[Commutative Algebra IV — Localization|localization]] map $R \to R_{\mathfrak{p}_i}$ — while the embedded components are *not* determined.

For $I = (X^2, XY)$, the associated primes are $\operatorname{Ass}(I) = \{(X), (X,Y)\}$ with $(X) \subsetneq (X,Y)$, so $(X)$ is isolated and $(X,Y)$ embedded.

---

# Convergent Strategy

**Problem class.** This is a *prove-an-invariance-and-its-failure* problem — simultaneously establishing that one piece of a decomposition is canonical (the isolated component) and that another genuinely is not (the embedded component). It is the sharpest statement of the chapter's central tension between uniqueness and non-uniqueness.

**Assumption pattern.** The split into isolated and embedded is governed by the inclusion $(X) \subsetneq (X,Y)$. The isolated component is pinned down because *localizing at the isolated prime $(X)$ kills every component except the one over $(X)$* — a minimal prime sees only itself after localization. The embedded component is free because *localizing at $(X)$ erases the embedded component entirely*, so localization gives no constraint on it. The recognisable trigger is "isolated prime $\Rightarrow$ localize there to canonicalise; embedded prime $\Rightarrow$ localization is blind to it, so it can wobble".

**Theorem routing.** Part 1: localize at $(X)$; the components over primes $\not\subseteq (X)$ extend to the unit ideal in $R_{(X)}$, so $IR_{(X)} = (X)R_{(X)}$, and contracting back gives the isolated component $(X) = I^{ec}$, manifestly independent of the decomposition. Part 2: directly exhibit the family $(X) \cap (X^2, XY, Y^n)$ and verify each is a minimal primary decomposition of $I$ via the generator chase and the maximal-radical shortcut. Part 3: assemble — the [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First Uniqueness Theorem]] fixes the primes, the localization argument fixes the isolated component, and the family shows the embedded component is unconstrained.

**Key decision point.** The non-obvious move is the *localization argument for uniqueness of the isolated component*: rather than comparing decompositions term by term, one shows the isolated component equals an intrinsic object $I^{ec}$ that never mentions a decomposition. The genuine insight is the asymmetry — localization at an isolated prime *isolates* its component (makes it canonical) but is *blind* to embedded primes (which extend to the unit ideal and vanish), so the same tool that pins down the isolated component is exactly why it cannot pin down the embedded one. The natural error is to expect both components to be determined since the primes are; the insight is that determinacy requires the prime to be *visible after localization*, which only isolated primes are.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra IX — Primary Decomposition#Legal Operations|the topic page's Legal Operations]]:

1. **Localize to canonicalise an isolated component (operation 7).** Localize at $(X)$ to show the isolated component is $I^{ec}$, independent of the decomposition.

2. **Read primes off the disjointness condition (localization, operation 7 / CA IV).** A component over a prime $\mathfrak{p} \not\subseteq (X)$ extends to the unit ideal in $R_{(X)}$.

3. **Upgrade to primary via a maximal radical (operation 4).** Certify each $(X^2, XY, Y^n)$ is $(X,Y)$-primary via $\sqrt{(X^2, XY, Y^n)} = (X,Y)$ maximal.

4. **Verify intersections by a generator chase.** Confirm $(X) \cap (X^2, XY, Y^n) = I$ for each $n$.

---

# Hints

> [!note]- Hint 1 (part 1)
> To show the isolated component is canonical, do not compare decompositions. Instead show it equals an intrinsic object. Localize at the isolated prime $(X)$. In $R_{(X)}$, what happens to the embedded component (over $(X,Y)$)? The prime $(X,Y)$ is *not* contained in $(X)$, so it contains an element outside $(X)$ — which becomes a unit after localization. So the embedded component extends to the unit ideal.

> [!note]- Hint 2 (part 1)
> Concretely: $Y \in (X,Y)^2$? No, but $Y^2 \in (X,Y)^2$, and $Y \notin (X)$, so $Y$ is a unit in $R_{(X)}$, making $(X,Y)^2 R_{(X)} = R_{(X)}$. Thus $I R_{(X)} = (X)R_{(X)} \cap R_{(X)} = (X)R_{(X)}$. Contracting back: $I^{ec} = (X)$ (the contraction of $(X)R_{(X)}$ is $(X)$ since $(X)$ is prime and $\subseteq (X)$). This is the isolated component, and it never mentioned a decomposition.

> [!note]- Hint 3 (part 2)
> For non-uniqueness, find more embedded components. Try $(X^2, XY, Y^n)$ for $n = 2, 3, 4, \dots$. Each has radical $(X,Y)$ (it contains $X^2, Y^n$, so $X, Y \in$ radical), so each is $(X,Y)$-primary. Now check $(X) \cap (X^2, XY, Y^n) = I$ for every $n \geq 2$.

> [!note]- Hint 4 (part 2, the chase)
> $f \in (X) \cap (X^2, XY, Y^n)$: write $f = aX = bX^2 + cXY + dY^n$. The term $dY^n$ must be divisible by $X$ (the rest is), and $X \nmid Y^n$, so $X \mid d$. Substitute to get $a \in (X, Y)$ (you may need that $X \mid d$ forces the $Y^n$ contribution into $X \cdot (\text{something in } (X,Y))$), hence $f \in X(X,Y) = I$. Conclude all $(X) \cap (X^2, XY, Y^n)$, $n \geq 2$, are distinct minimal decompositions of $I$.

---

# Solution

The proof has two opposed halves. The isolated component is canonical: localizing at $(X)$ sends the embedded component to the unit ideal, so $IR_{(X)} = (X)R_{(X)}$, whose contraction $(X)$ is the isolated component — an intrinsic object. The embedded component is not canonical: the ideals $(X^2, XY, Y^n)$, $n \geq 2$, are all $(X,Y)$-primary and all satisfy $(X) \cap (X^2, XY, Y^n) = I$, giving infinitely many minimal decompositions. The non-obvious move is the localization, which simultaneously explains both halves: it isolates the minimal prime's component and is blind to the embedded prime.

**Step 1: The embedded component dies after localizing at the isolated prime $(X)$.**

Any $(X,Y)$-primary component extends to the unit ideal in $R_{(X)}$, because $(X,Y) \not\subseteq (X)$ supplies a unit.

> [!note]- Derivation
> Localize at the minimal prime $\mathfrak{p} = (X)$, i.e. invert $S = R \setminus (X)$. The embedded prime $(X,Y) \not\subseteq (X)$ (since $Y \in (X,Y) \setminus (X)$), so the element $Y \in (X,Y)$ lies in $S$ and becomes a *unit* in $R_{(X)}$. Any $(X,Y)$-primary component $\mathfrak{q}$ has $\sqrt{\mathfrak{q}} = (X,Y)$, so some power $Y^m \in \mathfrak{q}$; since $Y$ is a unit in $R_{(X)}$, so is $Y^m$, and $\mathfrak{q} R_{(X)}$ contains a unit, hence $\mathfrak{q}R_{(X)} = R_{(X)}$. Concretely $(X,Y)^2 R_{(X)} = R_{(X)}$ (as $Y^2 \in (X,Y)^2$) and $(X^2, Y)R_{(X)} = R_{(X)}$ (as $Y \in (X^2,Y)$). The embedded component vanishes after localization.

**Step 2: The isolated component is $I^{ec} = (X)$, independent of the decomposition.**

$IR_{(X)} = (X)R_{(X)}$, and contracting gives the isolated component $(X)$.

> [!note]- Derivation
> Localization is exact and commutes with finite intersection, so for any minimal decomposition $I = (X) \cap \mathfrak{q}$ ($\mathfrak{q}$ the $(X,Y)$-primary component),
> $$I R_{(X)} = (X)R_{(X)} \cap \mathfrak{q}R_{(X)} = (X)R_{(X)} \cap R_{(X)} = (X)R_{(X)},$$
> using Step 1 ($\mathfrak{q}R_{(X)} = R_{(X)}$). The right side $(X)R_{(X)}$ depends only on $I$ (it is $IR_{(X)}$), not on $\mathfrak{q}$. Contracting back along $R \to R_{(X)}$, the isolated component is $I^{ec}$, the contraction of $IR_{(X)} = (X)R_{(X)}$. Since $(X)$ is prime and disjoint from $S = R \setminus (X)$ in the relevant sense, the contraction of $(X)R_{(X)}$ is $(X)$ itself (a $\mathfrak{p}$-primary ideal with $\mathfrak{p} \cap S = \varnothing$ is contracted from $R_{\mathfrak{p}}$). So the isolated component equals $(X)$ in *every* minimal decomposition — it is the intrinsic object $I^{ec}$. This is the Second Uniqueness Theorem in action.

**Step 3: Infinitely many embedded components.**

Each $(X^2, XY, Y^n)$, $n \geq 2$, is $(X,Y)$-primary and gives $(X) \cap (X^2, XY, Y^n) = I$.

> [!note]- Derivation
> Fix $n \geq 2$ and set $\mathfrak{q}_n = (X^2, XY, Y^n)$.
>
> *Primary.* $\sqrt{\mathfrak{q}_n} \ni X$ (since $X^2 \in \mathfrak{q}_n$) and $\ni Y$ (since $Y^n \in \mathfrak{q}_n$), so $\sqrt{\mathfrak{q}_n} = (X,Y)$, a maximal ideal; hence $\mathfrak{q}_n$ is $(X,Y)$-primary by the maximal-radical shortcut ([[Ex - Powers of a maximal ideal are primary]]).
>
> *Intersection.* "$\supseteq$": $X^2 \in (X) \cap \mathfrak{q}_n$ and $XY = X \cdot Y \in (X)$, $XY \in \mathfrak{q}_n$, so $I \subseteq (X) \cap \mathfrak{q}_n$. "$\subseteq$": let $f = aX \in \mathfrak{q}_n$, so $aX = bX^2 + cXY + dY^n$. Then $dY^n = aX - bX^2 - cXY = X(a - bX - cY)$ is divisible by $X$; as $X \nmid Y^n$ in the UFD $k[X,Y]$, $X \mid d$, say $d = eX$. Then $aX = bX^2 + cXY + eXY^n = X(bX + cY + eY^n)$, and cancelling $X$ gives $a = bX + cY + eY^n \in (X,Y)$. So $f = aX \in X(X,Y) = I$. Hence $(X) \cap \mathfrak{q}_n = I$.
>
> *Distinct.* The ideals $\mathfrak{q}_n = (X^2, XY, Y^n)$ are pairwise distinct: $Y^{n} \in \mathfrak{q}_n$ but $Y^{n} \notin \mathfrak{q}_{n+1} = (X^2, XY, Y^{n+1})$ (an element of $\mathfrak{q}_{n+1}$ that is a pure power of $Y$ must be divisible by $Y^{n+1}$, since the other generators carry a factor of $X$). So $\mathfrak{q}_2, \mathfrak{q}_3, \mathfrak{q}_4, \dots$ are distinct, giving infinitely many minimal primary decompositions $I = (X) \cap \mathfrak{q}_n$. Three explicit examples: $(X)\cap(X^2,XY,Y^2)$, $(X)\cap(X^2,XY,Y^3)$, and $(X)\cap(X^2,Y)$.

**Step 4: Assemble the invariance / non-invariance statement.**

> [!note]- Derivation
> Across all these decompositions:
> - The **associated primes** $\{(X), (X,Y)\}$ are fixed, by the [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First Uniqueness Theorem]].
> - The **isolated component** $(X)$ is fixed, by Step 2 (it equals the intrinsic $I^{ec}$ at $(X)$).
> - The **embedded component** ranges over the infinite family $\{\mathfrak{q}_n\}_{n \geq 2}$ (and $(X^2, Y)$, and others), by Step 3 — it is *not* determined by $I$.
>
> This is the precise content of the two uniqueness theorems: the primes and the isolated components are invariants of $I$; the embedded components are genuine choices.

> [!note]- Complete formal solution
> **Isolated component is unique.** Localize at the minimal prime $(X)$. Since $(X,Y) \not\subseteq (X)$, any $(X,Y)$-primary component $\mathfrak{q}$ satisfies $\mathfrak{q}R_{(X)} = R_{(X)}$ (it contains a power of $Y$, a unit there). Hence $IR_{(X)} = (X)R_{(X)} \cap \mathfrak{q}R_{(X)} = (X)R_{(X)}$, which depends only on $I$; contracting, the isolated component is $I^{ec} = (X)$ in every minimal decomposition.
>
> **Embedded component is not unique.** For each $n \geq 2$, $\mathfrak{q}_n = (X^2, XY, Y^n)$ is $(X,Y)$-primary ($\sqrt{\mathfrak{q}_n} = (X,Y)$ maximal), and $(X) \cap \mathfrak{q}_n = I$ (generator chase: $f = aX = bX^2 + cXY + dY^n$ forces $X \mid d$, then $a \in (X,Y)$, so $f \in I$). The $\mathfrak{q}_n$ are distinct ($Y^n \in \mathfrak{q}_n \setminus \mathfrak{q}_{n+1}$), giving infinitely many minimal decompositions $I = (X) \cap \mathfrak{q}_n$.
>
> **Conclusion.** $\operatorname{Ass}(I) = \{(X), (X,Y)\}$ and the isolated component $(X)$ are invariants of $I$; the embedded $(X,Y)$-primary component is not. $\blacksquare$

---

# Key Takeaways

**Localize at an isolated prime to make its component canonical — and the same localization is blind to embedded primes.** The decisive technique is that the primary component over an *isolated* (minimal) prime $\mathfrak{p}$ equals the intrinsic object $I^{ec}$ = contraction of $IR_{\mathfrak{p}}$, because localizing at $\mathfrak{p}$ sends every *other* component to the unit ideal: a component over a prime $\mathfrak{p}' \not\subseteq \mathfrak{p}$ contains an element of $\mathfrak{p}' \setminus \mathfrak{p}$, which becomes a unit. So localization "deletes all components but the one at $\mathfrak{p}$", leaving an object that never mentioned a decomposition. The asymmetry is the whole point: this works for isolated primes (whose components survive) but fails for embedded primes (whose components, being over a *larger* prime, vanish under localization at any smaller prime). The transferable trigger: to prove a primary component is canonical, check whether localizing at its radical isolates it — if the radical is minimal, yes; if embedded, the component is not determined.

**Embedded components wobble by adding high powers of the embedded prime's elements.** The infinite family $(X^2, XY, Y^n)$ shows concretely how an embedded component fails to be unique: one can absorb arbitrarily high powers $Y^n$ of the embedded prime $(X,Y)$ without changing the intersection with the isolated component, because those high powers already lie in $I$ "up to the isolated component". The mechanism is that the embedded prime $(X,Y)$ strictly contains the isolated prime $(X)$, so there is room to thicken the embedded component along the extra direction $Y$ while the isolated component $(X)$ holds the intersection fixed. The transferable diagnostic: whenever $\operatorname{Ass}(I)$ has an embedded prime $\mathfrak{p}' \supsetneq \mathfrak{p}$, expect a family of valid embedded components differing by elements of $\mathfrak{p}'$ that are "absorbed" by the component over $\mathfrak{p}$. This is why the embedded component is a *choice*, not a datum.

**The two uniqueness theorems carve out exactly what is real: the primes and the multiplicities along components.** Stepping back, this exercise is the concrete demonstration of the chapter's central structural fact. The [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First Uniqueness Theorem]] makes the *set of associated primes* an invariant; the Second Uniqueness Theorem makes the *isolated components* invariants; and *nothing* makes the embedded components invariant. So the genuinely intrinsic data of a non-radical ideal are: its irreducible components (isolated primes), the multiplicity along each (isolated components), and the *location* of its embedded subvarieties (embedded primes) — but not the embedded components themselves. For spaced retrieval, hold the slogan: "the embedded prime is real, but the embedded component is a choice." Geometrically, the embedded point at the origin of $V(X^2, XY)$ genuinely exists and is detected by every decomposition, but exactly *how* it is thickened is not canonical — which is why **schemes** record the prime (the embedded point) as intrinsic structure while treating the primary component as one of many presentations. See [[Ex - A primary decomposition in k[X,Y] with an embedded prime]] for the base computation and [[Ex - The associated primes via colon ideals]] for the colon machinery that fixes the primes.

---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Primary Ideal"
  - "Def - Associated and Minimal Primes"
  - "Def - Prime and Maximal Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $R = k[X, Y]$ with $k$ a field, and let $I = (X^2, XY)$. Prove that
$$I = (X) \cap (X, Y)^2 = (X) \cap (X^2, XY, Y^2) \qquad\text{and}\qquad I = (X) \cap (X^2, Y)$$
are both minimal [[Def - Primary Ideal|primary decompositions]] of $I$. Specifically:

1. Show $(X)$ is prime, hence $(X)$-primary.
2. Show $(X,Y)^2$ and $(X^2, Y)$ are each $(X,Y)$-primary (their radical is the maximal ideal $(X,Y)$), and that they are *distinct* ideals.
3. Verify both intersections equal $I$ by an explicit generator chase.
4. Conclude that $\operatorname{Ass}(I) = \{(X), (X,Y)\}$, that $(X)$ is the unique isolated prime and $(X,Y)$ is embedded, and that $I$ therefore has more than one minimal primary decomposition.

**Recall:**

The objects in play are primary and prime ideals, the radical, the maximal ideal $(X,Y)$, and the notion of a minimal primary decomposition.

![[Def - Primary Ideal#The Definition]]

An ideal $\mathfrak{q}$ is [[Def - Primary Ideal|primary]] when every zero-divisor of $R/\mathfrak{q}$ is nilpotent; equivalently $xy \in \mathfrak{q} \Rightarrow x \in \mathfrak{q}$ or $y \in \sqrt{\mathfrak{q}}$. Its radical $\sqrt{\mathfrak{q}}$ is then prime, and $\mathfrak{q}$ is called $\sqrt{\mathfrak{q}}$-primary.

![[Def - Associated and Minimal Primes#Associated primes]]

A primary decomposition $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$ is **minimal** when the radicals $\sqrt{\mathfrak{q}_i}$ are distinct and no $\mathfrak{q}_i$ contains $\bigcap_{j \neq i}\mathfrak{q}_j$. The [[Def - Associated and Minimal Primes|associated primes]] are the radicals $\sqrt{\mathfrak{q}_i}$; the minimal ones (under inclusion) are **isolated**, the rest **embedded**.

The shortcut for primariness: if $\sqrt{\mathfrak{q}} = \mathfrak{m}$ is [[Def - Prime and Maximal Ideal|maximal]] then $\mathfrak{q}$ is automatically $\mathfrak{m}$-primary (see [[Ex - Powers of a maximal ideal are primary]]).

---

# Convergent Strategy

**Problem class.** This is the *compute-and-verify-a-decomposition* problem, the central computational exercise of the chapter and the canonical illustration of non-uniqueness. As the [[Commutative Algebra IX — Primary Decomposition#Problem-Solving Strategy|topic page strategy]] records, there is no mechanical algorithm at this level: you *guess* the components from the geometry, then *verify* primariness and the intersection. Here the geometry is transparent — $V(I)$ is the line $X = 0$ with an embedded point at the origin — and the guess is forced by it.

**Assumption pattern.** The generators $X^2$ and $XY$ share the factor $X$, which signals that $(X)$ is the isolated component (the line), while their failure to cut out the line *cleanly* near the origin signals an embedded $(X,Y)$-primary component. The recognisable trigger is a non-radical ideal whose generators have a common factor: the common factor gives the isolated prime, and the "leftover" gives the embedded structure. The maximality of $(X,Y)$ is what makes the embedded components automatically primary, removing the need for a zero-divisor check.

**Theorem routing.** The route is: factor out the geometry to *guess* $(X)$ and an $(X,Y)$-primary piece; certify $(X)$ prime via $R/(X) \cong k[Y]$ a [[Def - Integral Domain|domain]]; certify each candidate $(X,Y)$-primary piece using the *maximal-radical shortcut* (operation 4 from the topic page); verify each intersection equals $I$ by a *generator chase*; finally read off $\operatorname{Ass}(I)$ and the isolated/embedded split from the inclusion $(X) \subsetneq (X,Y)$.

**Key decision point.** The non-obvious move is recognising that there are *two* valid $(X,Y)$-primary components, $(X,Y)^2$ and $(X^2, Y)$, and that this is not an error but the *point* — the embedded component is genuinely non-unique. The natural but wrong expectation is that a minimal decomposition is unique (as in $\mathbb{Z}$); the genuine insight is that minimality pins down the *primes* $\{(X), (X,Y)\}$ but not the embedded *component*, so the same $I$ legitimately decomposes two ways. Spotting the second decomposition requires noticing that $(X^2, Y)$, which looks unrelated, also contains $I$ and meets $(X)$ in exactly $I$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra IX — Primary Decomposition#Legal Operations|the topic page's Legal Operations]]:

1. **Pass to the quotient and read off the definition (operation 1).** Certify $(X)$ prime by computing $R/(X) \cong k[Y]$, a domain, and certify primariness of the embedded components by inspecting their quotients $k[Y]/(Y^2)$ and $k[X]/(X^2)$.

2. **Take radicals to find the attached prime (operation 2).** Compute $\sqrt{(X,Y)^2} = (X,Y)$ and $\sqrt{(X^2, Y)} = (X,Y)$ to identify both candidate components as $(X,Y)$-primary.

3. **Upgrade to primary via a maximal radical (operation 4).** Since $(X,Y)$ is maximal, both $(X,Y)^2$ and $(X^2, Y)$ are automatically $(X,Y)$-primary — no zero-divisor check needed.

4. **Verify the intersection by a generator chase.** Take a general element of the right-hand intersection and show it lies in $I$, using that elements of $(X)$ are multiples of $X$.

5. **Group / order primes to find isolated and embedded (operation 8 spirit).** Use $(X) \subsetneq (X,Y)$ to declare $(X)$ isolated and $(X,Y)$ embedded.

---

# Hints

> [!note]- Hint 1
> Look at the geometry first. The locus $V(X^2, XY)$ is where $X^2 = 0$ and $XY = 0$, i.e. where $X = 0$ — the $Y$-axis. So the *set* is a single line, and its prime is $(X)$. The ideal $I$ is not radical (it is not $(X)$), so it carries extra structure beyond the line. Where? The generators both vanish to higher order at the origin — that is where the embedded prime $(X,Y)$ will live.

> [!note]- Hint 2
> Guess $I = (X) \cap \mathfrak{q}$ where $\mathfrak{q}$ is $(X,Y)$-primary. The cleanest candidate is $\mathfrak{q} = (X,Y)^2 = (X^2, XY, Y^2)$. To certify it is $(X,Y)$-primary, compute its radical (you get the maximal ideal $(X,Y)$) and invoke "radical maximal $\Rightarrow$ primary". Then check $(X) \cap (X,Y)^2 = I$ by a generator chase.

> [!note]- Hint 3
> For the generator chase $(X) \cap (X,Y)^2 \subseteq I$: take $f = aX$ (an element of $(X)$) that also lies in $(X,Y)^2 = (X^2, XY, Y^2)$, so $f = bX^2 + cXY + dY^2$. Equate $aX = bX^2 + cXY + dY^2$ and look at the $Y^2$-term: $d Y^2$ must be divisible by $X$, forcing $d \in (X)$. Substitute back to show $a \in (X, Y)$, hence $f = aX \in X \cdot (X,Y) = (X^2, XY) = I$.

> [!note]- Hint 4
> For the second decomposition, try $\mathfrak{q}' = (X^2, Y)$. Its radical is $\sqrt{(X^2, Y)} = (X, Y)$ (maximal), so it is $(X,Y)$-primary. Run the same generator chase: $f = aX = bX^2 + cY$ forces $c \in (X)$, then $a \in (X,Y)$, so $f \in I$. Both $(X,Y)^2$ and $(X^2, Y)$ are valid embedded components — and they are different, since $Y \in (X^2, Y) \setminus (X,Y)^2$. That difference is the non-uniqueness.

---

# Solution

The proof has three parts. First we certify the components: $(X)$ is prime, and $(X,Y)^2$, $(X^2, Y)$ are both $(X,Y)$-primary by the maximal-radical shortcut. Second we verify each intersection equals $I$ by a generator chase that pins down the cross-terms. Third we read off $\operatorname{Ass}(I) = \{(X), (X,Y)\}$, observe $(X) \subsetneq (X,Y)$ so $(X)$ is isolated and $(X,Y)$ embedded, and note that the two distinct embedded components exhibit non-uniqueness. The non-obvious move is in the second decomposition, where $(X^2, Y)$ — which mentions $Y$ to the first power — is also a legitimate $(X,Y)$-primary component.

**Step 1: $(X)$ is prime, hence $(X)$-primary.**

$R/(X) \cong k[Y]$ is an integral domain, so $(X)$ is prime; every prime is primary, and $\sqrt{(X)} = (X)$, so $(X)$ is $(X)$-primary.

> [!note]- Derivation
> The quotient map $k[X,Y] \to k[Y]$, $X \mapsto 0$, $Y \mapsto Y$, is surjective with kernel $(X)$, so $R/(X) \cong k[Y]$. Since $k[Y]$ is an [[Def - Integral Domain|integral domain]], $(X)$ is a [[Def - Prime and Maximal Ideal|prime]] ideal ([[Thm - Maximal and Prime Ideals via Quotients|prime ⟺ domain quotient]]). A prime ideal is [[Def - Primary Ideal|primary]] (the only zero-divisor of a domain is $0$, which is nilpotent), and its radical is itself, so $(X)$ is $(X)$-primary.

**Step 2: $(X,Y)^2$ and $(X^2, Y)$ are $(X,Y)$-primary, and distinct.**

Both have radical the maximal ideal $(X,Y)$, so both are $(X,Y)$-primary; and $Y \in (X^2, Y) \setminus (X,Y)^2$, so they are different ideals.

> [!note]- Derivation
> *Radicals.* $(X,Y)^2 = (X^2, XY, Y^2)$, and $\sqrt{(X,Y)^2} = (X,Y)$ since $\sqrt{I^n} = \sqrt{I}$ and $\sqrt{(X,Y)} = (X,Y)$. For $(X^2, Y)$: it contains $Y$ and $X^2$, so its radical contains $Y$ and $X$ (as $X^2 \in (X^2,Y) \Rightarrow X \in \sqrt{(X^2,Y)}$), giving $\sqrt{(X^2, Y)} \supseteq (X,Y)$; and $(X,Y)$ is maximal, so $\sqrt{(X^2, Y)} = (X,Y)$.
>
> *Primary.* In both cases $\sqrt{\mathfrak{q}} = (X,Y)$ is a maximal ideal, and a maximal radical forces primariness (see [[Ex - Powers of a maximal ideal are primary]]): $R/\mathfrak{q}$ is a local ring whose maximal ideal is nilpotent, so every non-unit is nilpotent, hence every zero-divisor is nilpotent. Concretely $R/(X,Y)^2$ has maximal ideal $(\bar X, \bar Y)$ with $(\bar X, \bar Y)^2 = 0$, and $R/(X^2, Y) \cong k[X]/(X^2)$ has nilpotent maximal ideal $(\bar X)$.
>
> *Distinct.* $Y \in (X^2, Y)$ but $Y \notin (X,Y)^2 = (X^2, XY, Y^2)$ (every element of $(X,Y)^2$ has all terms of total degree $\geq 2$, while $Y$ has degree $1$). So $(X,Y)^2 \neq (X^2, Y)$.

**Step 3: $(X) \cap (X,Y)^2 = I$.**

A generator chase shows the intersection is contained in $I$ (the reverse is clear), using that the $Y^2$-coefficient must absorb a factor of $X$.

> [!note]- Derivation
> "$\supseteq$": $X^2 = X \cdot X \in (X)$ and $X^2 \in (X,Y)^2$; $XY = X \cdot Y \in (X)$ and $XY \in (X,Y)^2$. So $I = (X^2, XY) \subseteq (X) \cap (X,Y)^2$.
>
> "$\subseteq$": let $f \in (X) \cap (X,Y)^2$. From $f \in (X)$, write $f = aX$ for some $a \in k[X,Y]$. From $f \in (X,Y)^2 = (X^2, XY, Y^2)$, write $f = bX^2 + cXY + dY^2$ with $b, c, d \in k[X,Y]$. Then
> $$aX = bX^2 + cXY + dY^2.$$
> The right side, minus $bX^2 + cXY$ (both divisible by $X$), equals $aX - bX^2 - cXY = dY^2$, so $dY^2 = X(a - bX - cY)$ is divisible by $X$. Since $X \nmid Y^2$ in the [[Def - Unique Factorization Domain|UFD]] $k[X,Y]$, we get $X \mid d$, say $d = eX$. Then
> $$aX = bX^2 + cXY + eXY^2 = X(bX + cY + eY^2),$$
> and cancelling $X$ (valid in the domain $k[X,Y]$) gives $a = bX + cY + eY^2 \in (X, Y)$. Hence $f = aX \in X \cdot (X,Y) = (X^2, XY) = I$. So $(X) \cap (X,Y)^2 \subseteq I$, and equality holds.

**Step 4: $(X) \cap (X^2, Y) = I$.**

The same chase, now with the linear generator $Y$, forces the $Y$-coefficient to absorb a factor of $X$.

> [!note]- Derivation
> "$\supseteq$": $X^2 \in (X) \cap (X^2, Y)$ clearly; $XY \in (X)$, and $XY = X \cdot Y \in (X^2, Y)$ since $Y \in (X^2, Y)$. So $I \subseteq (X) \cap (X^2, Y)$.
>
> "$\subseteq$": let $f \in (X) \cap (X^2, Y)$, so $f = aX$ and $f = bX^2 + cY$. Then $aX = bX^2 + cY$, so $cY = aX - bX^2 = X(a - bX)$ is divisible by $X$; since $X \nmid Y$, $X \mid c$, say $c = dX$. Then $aX = bX^2 + dXY = X(bX + dY)$, and cancelling $X$ gives $a = bX + dY \in (X,Y)$. Hence $f = aX \in X(X,Y) = I$. Equality holds.

**Step 5: Read off the associated primes and the isolated/embedded split.**

$\operatorname{Ass}(I) = \{(X), (X,Y)\}$, with $(X)$ isolated and $(X,Y)$ embedded; the two distinct decompositions exhibit non-uniqueness.

> [!note]- Derivation
> Both decompositions have components with radicals $(X)$ and $(X,Y)$, so $\operatorname{Ass}(I) = \{(X), (X,Y)\}$ — and by the [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First Uniqueness Theorem]] this set is the same for *every* minimal decomposition. Both decompositions are minimal: the radicals $(X) \neq (X,Y)$ are distinct, and neither component contains the other (e.g. the $(X,Y)$-primary component does not contain $(X)$, since $X \notin (X,Y)^2$).
>
> Since $(X) \subsetneq (X,Y)$, the prime $(X)$ is the unique *minimal* element of $\operatorname{Ass}(I)$ — the **isolated** prime — and $(X,Y)$ is **embedded**. The isolated component (over $(X)$) is $(X)$ in *both* decompositions; the embedded component (over $(X,Y)$) is $(X,Y)^2$ in the first and $(X^2, Y)$ in the second — *different ideals*. Hence $I$ has at least two distinct minimal primary decompositions, with the same associated primes and the same isolated component but different embedded components.

> [!note]- Complete formal solution
> **Claim.** $I = (X^2, XY) \subseteq k[X,Y]$ has $(X) \cap (X,Y)^2$ and $(X) \cap (X^2, Y)$ as distinct minimal primary decompositions, with $\operatorname{Ass}(I) = \{(X), (X,Y)\}$, $(X)$ isolated and $(X,Y)$ embedded.
>
> *Components are primary.* $R/(X) \cong k[Y]$ is a domain, so $(X)$ is prime, hence $(X)$-primary. The ideals $(X,Y)^2$ and $(X^2, Y)$ each have radical $(X,Y)$, a maximal ideal, hence are $(X,Y)$-primary; they are distinct since $Y \in (X^2,Y) \setminus (X,Y)^2$.
>
> *Intersections equal $I$.* For $(X) \cap (X,Y)^2$: "$\supseteq$" is clear; for "$\subseteq$", $f = aX = bX^2 + cXY + dY^2$ forces $X \mid d$ (the $Y^2$-term must absorb $X$), then $a \in (X,Y)$, so $f \in X(X,Y) = I$. For $(X) \cap (X^2, Y)$: $f = aX = bX^2 + cY$ forces $X \mid c$, then $a \in (X,Y)$, so $f \in I$.
>
> *Associated primes.* Both decompositions are minimal (distinct radicals, no redundant component) and have radicals $\{(X), (X,Y)\}$, so $\operatorname{Ass}(I) = \{(X), (X,Y)\}$ (well-defined by the First Uniqueness Theorem). As $(X) \subsetneq (X,Y)$, $(X)$ is isolated and $(X,Y)$ embedded. The embedded components $(X,Y)^2 \neq (X^2, Y)$ differ, so the minimal primary decomposition of $I$ is not unique. $\blacksquare$

---

# Key Takeaways

**Guess the decomposition from the geometry, then verify algebraically.** There is no mechanical algorithm to produce a primary decomposition by hand, so the working method is to *read the components off the variety* and check. The isolated components correspond to the irreducible components of $V(I)$ — here the single line $V(X) = \{X = 0\}$, giving $(X)$ — and the embedded components live wherever the generators "double up" or vanish to higher order, here the origin, giving an $(X,Y)$-primary piece. The trigger to recognise this pattern: a *non-radical* ideal whose generators share a common factor. The common factor ($X$) is the isolated prime; the locus where the factored-out generators still vanish ($X = Y = 0$) is the embedded prime. Once guessed, certification is routine — domain quotient for the prime component, maximal-radical shortcut for the embedded ones, generator chase for the intersection. This guess-and-verify discipline transfers to every hand computation of a primary decomposition.

**The generator chase always turns on a leading coefficient absorbing the common factor.** Both intersection verifications reduce to the same manoeuvre: an element of $(X)$ written in the embedded component's generators forces the "highest" coefficient (the $Y^2$- or $Y$-term) to be divisible by $X$, because $X$ does not divide $Y^2$ or $Y$ in the UFD $k[X,Y]$. This is the recurring computational heart of intersection verifications in polynomial rings: equate two expressions for the same element, then use unique factorisation to force a divisibility, then cancel the common factor (legal in a domain) to land in the smaller ideal. The transferable diagnostic is "when verifying $(\text{common factor}) \cap \mathfrak{q} \subseteq I$, look for the generator of $\mathfrak{q}$ coprime to the common factor and force its coefficient to absorb the factor". The same move proves $(f) \cap \mathfrak{q} = (f)\mathfrak{q}$-type identities throughout.

**Non-uniqueness lives entirely in the embedded component — the isolated part is rigid.** The single most important lesson of this exercise is that the *same* ideal has *different* minimal primary decompositions, and that the difference is confined to the embedded component. The isolated component $(X)$ and the associated primes $\{(X), (X,Y)\}$ are identical across both decompositions — they are forced by $I$ — but the $(X,Y)$-primary component is free to be $(X,Y)^2$ or $(X^2, Y)$ or infinitely many others (e.g. $(X^2, XY, Y^n)$ for any $n \geq 2$). This is the concrete face of the two uniqueness theorems: the [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First]] fixes the primes, the Second fixes the isolated components, and *nothing* fixes the embedded components. The trigger for "expect non-uniqueness" is the presence of an embedded prime, i.e. an associated prime strictly containing another — whenever $\operatorname{Ass}(I)$ has a non-minimal element, the decomposition is non-unique. See [[Ex - Embedded primes are not unique]] for the sharpened statement.

**Geometrically, $I$ is a line plus a fat point, and $\sqrt I$ forgets the fat point.** The radical $\sqrt I = (X)$ is just the line $X = 0$; passing $I \mapsto \sqrt I$ erases the embedded prime $(X,Y)$ entirely. So the variety $V(I)$ — a set — cannot detect the embedded point at the origin, even though the ideal $I$ plainly does (it is not radical). This is the prototype of the variety-versus-scheme distinction: the embedded $(X,Y)$ is a "thickening" of the line at the origin, a copy of the dual numbers $k[Y]/(Y^2)$ stuck transversally to the line, visible only when one remembers the full ring $R/I$ rather than its set of points. The takeaway for spaced practice: whenever an ideal is non-radical, ask "what does $I$ remember that $\sqrt I$ forgets?" — the answer is the embedded primes and the multiplicities, and they are exactly the data that distinguishes a **scheme** from a **variety**.

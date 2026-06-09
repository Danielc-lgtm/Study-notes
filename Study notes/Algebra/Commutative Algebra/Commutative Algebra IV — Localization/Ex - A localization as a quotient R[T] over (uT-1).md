---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Ring"
  - "Def - Polynomial Ring"
  - "Def - Quotient Ring"
  - "Def - Multiplicative Set and Localization"
  - "Thm - Universal Property of Localization"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $u\in R$ and $R_u := \{u^n : n\geq 0\}^{-1}R$ be the [[Def - Multiplicative Set and Localization|localization inverting $u$]]. Prove the **quotient presentation** (Becker Lemma 4.33):
$$R_u \;\cong\; R[T]/(uT - 1)$$
as $R$-algebras, via $\tfrac{r}{u^n}\mapsto rT^n + (uT-1)$, with inverse sending the class of $p(T)$ to $p(\tfrac1u)$.

Prove it *via the universal property*: show $R[T]/(uT-1)$ satisfies the same universal property as $R_u$ (the universal $R$-algebra in which $u$ becomes invertible), so the two are uniquely isomorphic. Then sketch the general case $R_U = R[\{T_u\}_{u\in U}]/(\{uT_u - 1\})$ for a subset $U\subseteq R$.

**Recall:**

![[Thm - Universal Property of Localization#Statement]]

The localization $R_u$ is the universal ring receiving a map from $R$ that sends $u$ to a unit. The [[Def - Polynomial Ring|polynomial ring]] $R[T]$ is the free $R$-algebra on one generator; an $R$-algebra map out of $R[T]/(uT-1)$ is an $R$-algebra map out of $R[T]$ that vanishes on $uT-1$, i.e. a choice of image for $T$ that inverts $u$.

---

# Convergent Strategy

**Problem class.** This is an *identify-a-localization* problem solved by the universal property. Per the [[Commutative Algebra IV — Localization#Problem-Solving Strategy|topic strategy]], to recognise a given ring as $S^{-1}R$ you show it satisfies the *same universal property*, and uniqueness of universal objects delivers the isomorphism with no fraction bookkeeping.

**Assumption pattern.** The recognisable feature is "$R[T]/(uT-1)$ is $R$ with a formal inverse of $u$ adjoined": the relation $uT - 1 = 0$, i.e. $u\bar T = 1$, *forces* $\bar T$ to be the inverse of $u$. So this quotient is, by construction, a ring in which $u$ is invertible — and the question is whether it is the *universal* such ring, which is exactly what the universal property tests.

**Theorem routing.** The route is: (i) the canonical map $R\to R[T]/(uT-1)$ sends $u$ to the unit $\bar u$ (inverse $\bar T$); (ii) for any ring $B$ and map $f : R\to B$ with $f(u)\in B^\times$, an $R$-algebra map $R[T]/(uT-1)\to B$ is the same as a choice of image $T\mapsto t$ with $f(u)t = 1$, i.e. $t = f(u)^{-1}$ — *exactly one* choice; (iii) so $R[T]/(uT-1)$ has the universal property of $R_u$, and by [[Thm - Universal Property of Localization|uniqueness of universal objects]], $R_u\cong R[T]/(uT-1)$.

**Key decision point.** The non-obvious move is to *not* construct the isomorphism by hand (well-definedness of $\tfrac{r}{u^n}\mapsto rT^n$ is fiddly: different fraction representatives, the equivalence relation). Instead, recognise that an $R$-algebra map out of a polynomial quotient is determined by where the generator $T$ goes, subject to the relation, and that the relation pins $T$ to the *unique* inverse of $f(u)$ — which is precisely the universal-property condition. The decision to argue at the level of "maps out of" rather than "elements of" is what makes the proof clean.

---

# Legal Operations Used

This solution deploys the following [[Commutative Algebra IV — Localization#Legal Operations|legal operations from the topic page]]:

1. **Operation 2 (invoke the universal property instead of fractions).** The entire proof: identify $R[T]/(uT-1)$ as $R_u$ by matching universal properties.

2. **Operation 7 (detect nilpotence by collapse).** Cross-check: $R[T]/(uT-1) = 0\iff u$ nilpotent, matching $R_u = 0\iff u$ nilpotent.

---

# Hints

> [!note]- Hint 1
> Do not try to define $\tfrac{r}{u^n}\mapsto rT^n$ directly and check it is well-defined — that is painful. Instead use the universal property: $R_u$ is *the* universal $R$-algebra inverting $u$. Show $R[T]/(uT-1)$ is also universal among $R$-algebras inverting $u$, and uniqueness does the rest.

> [!note]- Hint 2
> An $R$-algebra map out of $R[T]$ is a free choice of image for $T$. An $R$-algebra map out of $R[T]/(uT-1)$ is such a choice that *respects the relation* $uT = 1$, i.e. sends $T$ to an element $t$ with $\bar u\,t = 1$. Given $f : R\to B$ inverting $u$, how many valid $t$ are there in $B$?

> [!note]- Hint 3
> Exactly one: $t = f(u)^{-1}$, forced by $f(u)t = 1$ and $f(u)$ being a unit. So there is a *unique* $R$-algebra map $R[T]/(uT-1)\to B$ extending $f$ — this is verbatim the universal property of $R_u$. By uniqueness of universal objects, $R_u\cong R[T]/(uT-1)$.

---

# Solution

Rather than build the isomorphism elementwise, prove that $R[T]/(uT-1)$ satisfies the universal property of $R_u$: maps out of it correspond to maps out of $R$ inverting $u$, because the relation $uT = 1$ forces $T$ to the unique inverse of $u$'s image. Uniqueness of universal objects gives the isomorphism, and tracking it recovers Becker's explicit formula.

**Step 1: In $R[T]/(uT-1)$, the image $\bar u$ is a unit.**

The relation $uT = 1$ makes $\bar T$ the inverse of $\bar u$.

> [!note]- Derivation
> Let $A := R[T]/(uT-1)$ and write $\bar u, \bar T$ for the images of $u, T$. The defining relation gives $\bar u\,\bar T = \overline{uT} = \bar 1 = 1$ in $A$. So $\bar u$ is a unit of $A$ with inverse $\bar T$. Hence the structure map $\iota_A : R\to A$, $r\mapsto\bar r$, sends $u$ to a unit — $A$ is an $R$-algebra in which $u$ is invertible. (If $A = 0$, this is the degenerate case; $A = 0\iff 1\in(uT-1)\iff u$ nilpotent, matching $R_u = 0\iff u$ nilpotent.)

**Step 2: Maps out of $A$ correspond to maps out of $R$ inverting $u$.**

For any ring $B$ and $f : R\to B$ with $f(u)\in B^\times$, there is a *unique* $R$-algebra map $A\to B$ extending $f$.

> [!note]- Derivation
> An $R$-algebra homomorphism $R[T]\to B$ extending $f : R\to B$ is uniquely determined by the image $t\in B$ of $T$ (the [[Def - Polynomial Ring|universal property of the polynomial ring]]: $R[T]$ is free on $T$). Such a map descends to the quotient $A = R[T]/(uT-1)$ iff it kills the relation, i.e. iff $f(u)t - 1 = 0$, i.e. $f(u)t = 1$. Since $f(u)\in B^\times$, this equation has the *unique* solution $t = f(u)^{-1}$. Therefore there is exactly one $R$-algebra map $h : A\to B$ with $h\circ\iota_A = f$, given by $h(\bar T) = f(u)^{-1}$ and $h(\bar r) = f(r)$.

**Step 3: $A$ has the universal property of $R_u$; conclude the isomorphism.**

Steps 1–2 are verbatim the universal property of $R_u$, so $R_u\cong A$ by uniqueness.

> [!note]- Derivation
> The [[Thm - Universal Property of Localization|universal property]] of $R_u = \{u^n\}^{-1}R$ says: $R_u$ is an $R$-algebra in which $u$ is a unit (Step 1 for $A$), and for every $f : R\to B$ inverting $u$ there is a unique extension $R_u\to B$ (Step 2 for $A$). The pair $(A, \iota_A)$ satisfies both clauses, so it satisfies the *same* universal property as $(R_u, \iota_{R_u})$. By the uniqueness clause of the universal property (any two universal objects are uniquely isomorphic),
> $$R_u\;\cong\;R[T]/(uT-1)$$
> as $R$-algebras. Tracking the canonical isomorphism: $R_u\to A$ sends $\tfrac{r}{u^n}\mapsto r\bar T^n$ (since $\tfrac1u\mapsto\bar T$), i.e. $\tfrac{r}{u^n}\mapsto rT^n + (uT-1)$; the inverse sends $p(T) + (uT-1)\mapsto p(\tfrac1u)$, evaluating $T$ at the inverse $\tfrac1u\in R_u$ — exactly Becker's formula.

**Step 4: The general case $R_U$.**

For a subset $U\subseteq R$, $R_U = R[\{T_u\}_{u\in U}]/(\{uT_u - 1\}_{u\in U})\cong S^{-1}R$ with $S$ the multiplicative closure of $U$.

> [!note]- Derivation
> The same argument with one variable $T_u$ per element $u\in U$: an $R$-algebra map out of $R[\{T_u\}]/(\{uT_u-1\})$ to $B$ is a choice of images $T_u\mapsto t_u$ with $f(u)t_u = 1$ for each $u$, i.e. $t_u = f(u)^{-1}$, uniquely determined. So this quotient is the universal $R$-algebra inverting every $u\in U$, which (by the universal property of localization for the multiplicative closure $S$ of $U$) is $S^{-1}R$. Hence $R_U\cong S^{-1}R$. This is Becker's general quotient construction of the localization, the "huge polynomial algebra mod huge ideal" presentation complementary to the fraction model.

> [!note]- Complete formal solution
> Let $A = R[T]/(uT-1)$. In $A$, $\bar u\bar T = 1$, so $\bar u$ is a unit and $\iota_A : R\to A$ inverts $u$. For any ring $B$ and $f : R\to B$ with $f(u)\in B^\times$: an $R$-algebra map $R[T]\to B$ extending $f$ is a choice of $T\mapsto t$; it factors through $A$ iff $f(u)t = 1$, which (as $f(u)$ is a unit) has the unique solution $t = f(u)^{-1}$. So there is a unique $R$-algebra map $A\to B$ extending $f$.
>
> Thus $(A, \iota_A)$ satisfies the universal property of $(R_u, \iota_{R_u})$, and by uniqueness of universal objects, $R_u\cong A = R[T]/(uT-1)$ via $\tfrac{r}{u^n}\mapsto rT^n + (uT-1)$, with inverse $p(T) + (uT-1)\mapsto p(\tfrac1u)$.
>
> The general case $R_U = R[\{T_u\}_U]/(\{uT_u-1\}_U)\cong S^{-1}R$ ($S = $ multiplicative closure of $U$) follows identically with one variable per $u\in U$. $\blacksquare$

---

# Key Takeaways

**Identify a ring as a localization by matching universal properties, never by constructing the map by hand.** The entire proof avoids fraction arithmetic because the universal property reduces "is $A\cong R_u$?" to "does $A$ have the right universal property?", and that is checked by analysing *maps out of* $A$. The reusable recipe: to show some explicit ring $A$ is $S^{-1}R$, verify (1) the structure map $R\to A$ inverts $S$, and (2) for every $f : R\to B$ inverting $S$ there is a unique extension $A\to B$; then uniqueness of universal objects gives $A\cong S^{-1}R$ for free. This sidesteps every well-definedness headache of the fraction model and is the standard way localizations are recognised in the wild — it is how one proves $R_f\cong R[T]/(fT-1)$, how one identifies a subring of $K$ as a localization, and how one shows two constructions of a localization agree.

**The relation $uT = 1$ literally "adjoins a formal inverse", and the quotient presentation is the universal property made concrete.** The polynomial-quotient model exhibits localization as the dual of the fraction model: where fractions *write down* $\tfrac1u$ as a symbol, the quotient *imposes* $\tfrac1u$ as a new generator $T$ subject to $uT = 1$. The two constructions are complementary — fractions are good for computing kernels and ideal extensions (the equivalence relation is explicit), while the polynomial presentation is good for finite generation and for seeing localization as "add an inverse". The trigger to reach for the quotient form: when you need that $R_f$ is a *finitely generated $R$-algebra* (it is, generated by $\tfrac1f$, hence Noetherian if $R$ is, by Hilbert's basis theorem), or when you want to compute $R_f$ as an explicit ring rather than a set of fractions.

**Generating with one inverter-variable per element exhibits any localization as a "polynomial algebra mod relations".** The general case $S^{-1}R\cong R[\{T_u\}]/(\{uT_u-1\})$ shows that even the most general localization is a quotient of a (possibly huge) polynomial algebra — the same "big free object mod big ideal" pattern as the tensor product. This presentation is what makes localizations *manipulable by algebra-presentation techniques*: it shows $R_f$ is finite type, lets you compute its dimension and Noetherian property, and is the affine-scheme statement that $D(f) = \operatorname{Spec}(R_f)$ is cut out inside $\operatorname{Spec}(R[T]) = \mathbb{A}^1_R$ by the single equation $fT = 1$ — a hyperbola-like closed subscheme that *is* the graph of $\tfrac1f$. Recognising localization as "impose $fT = 1$" is the bridge from the algebra to the geometry of the basic open $D(f)$ — see [[Thm - Universal Property of Localization]] for the structural backbone.

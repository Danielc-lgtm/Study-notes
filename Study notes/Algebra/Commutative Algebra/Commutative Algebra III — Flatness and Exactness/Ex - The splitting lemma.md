---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - Module Homomorphism"
  - "Def - Direct Sum of Modules"
  - "Def - Projective Module"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Prove the **splitting lemma**. A short exact sequence of $R$-modules
$$0 \to A \xrightarrow{\ f\ } B \xrightarrow{\ g\ } C \to 0$$
is said to **split** if it is isomorphic (as a sequence) to $0 \to A \xrightarrow{\iota_A} A\oplus C \xrightarrow{\pi_C} C \to 0$, with $\iota_A$ the canonical inclusion and $\pi_C$ the canonical projection. Prove the following are equivalent:

(a) the sequence splits;

(b) there is an $R$-linear $s : C \to B$ (a **section**) with $g\circ s = \operatorname{id}_C$;

(c) there is an $R$-linear $r : B \to A$ (a **retraction**) with $r\circ f = \operatorname{id}_A$.

**Recall:**

The objects in play are short exact sequences, sections, retractions, and direct sums.

![[Def - Exact Sequence and Short Exact Sequence#The Definition]]

A short exact sequence $0\to A\xrightarrow{f}B\xrightarrow{g}C\to 0$ has $f$ injective, $g$ surjective, and $\operatorname{im} f = \ker g$. We identify $A$ with $\operatorname{im} f\subseteq B$ via the injection $f$.

![[Def - Direct Sum of Modules#The Definition]]

A **section** of $g$ is $s : C\to B$ with $gs = \operatorname{id}_C$ (a one-sided inverse on the right); a **retraction** of $f$ is $r : B\to A$ with $rf = \operatorname{id}_A$ (a one-sided inverse on the left). An **isomorphism of sequences** is a triple of isomorphisms commuting with the maps; here it amounts to an iso $\varphi : B\xrightarrow{\sim} A\oplus C$ with $\varphi f = \iota_A$ and $\pi_C\varphi = g$.

The bridge that makes the proof run — *a one-sided inverse of either outer map produces a direct-sum decomposition of the middle*: a section lets you write $B = f(A)\oplus s(C)$, and a retraction lets you write $B = f(A)\oplus\ker r$. Either decomposition is the splitting.

---

# Convergent Strategy

**Problem class.** This is a *prove-an-equivalence* problem of the cyclic type: three conditions, shown equivalent by a cycle of implications, each a short module-homomorphism construction. As the [[Commutative Algebra III — Flatness and Exactness]] strategy records, the splitting lemma is the precise interface where [[Def - Projective Module|projectivity]] feeds into "is this a direct sum?" — a projective quotient hands you the section of (b).

**Assumption pattern.** The recognisable trigger is "I have a short exact sequence and want to break the middle term apart." Each condition is a different *handle* on the same splitting: (a) the global isomorphism, (b) a right inverse of $g$, (c) a left inverse of $f$. The pattern is that any *one* handle reconstructs the other two by elementary linear algebra of modules.

**Theorem routing.** Prove a cycle (a)$\Rightarrow$(b)$\Rightarrow$(c)$\Rightarrow$(a), or the symmetric (a)$\Rightarrow$(c)$\Rightarrow$(b)$\Rightarrow$(a). (a)$\Rightarrow$(b): the splitting isomorphism transports the canonical section $\iota_C : C\to A\oplus C$ back to a section of $g$. (b)$\Rightarrow$(c): given a section $s$, the map $\operatorname{id}_B - s g$ lands in $\ker g = \operatorname{im} f$, so $r := f^{-1}(\operatorname{id}_B - sg)$ is a retraction. (c)$\Rightarrow$(a): given a retraction $r$, the map $\varphi = (r, g) : B\to A\oplus C$ is an isomorphism intertwining the sequences.

**Key decision point.** The non-obvious move is the construction in (b)$\Rightarrow$(c) (and its mirror): from a section $s$, the *complementary projection* $\operatorname{id}_B - sg$ is the right gadget, because $g(\operatorname{id}_B - sg) = g - (gs)g = g - g = 0$, so it factors through $\ker g = \operatorname{im} f$, and composing with $f^{-1}$ (defined on $\operatorname{im} f$ since $f$ is injective) yields the retraction. The genuine insight is that a one-sided inverse on one end *automatically generates* one on the other end via this complementary-projection trick — the two are not independent data. The natural wrong instinct is to think a section and a retraction must be supplied separately; in fact either determines a splitting and hence the other.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra III — Flatness and Exactness#Legal Operations|the topic page's Legal Operations]]:

1. **Split a short exact sequence via a one-sided inverse (operation 6).** A section of $g$ or retraction of $f$ decomposes $B$ as a direct sum.

2. **Build the splitting isomorphism $(r, g) : B \to A\oplus C$.** A retraction and the quotient map together give the explicit isomorphism witnessing (a).

3. **Use the complementary projection $\operatorname{id}_B - sg$.** From a section, this map lands in $\operatorname{im} f$ and produces the retraction — the trick converting (b) into (c).

---

# Hints

> [!note]- Hint 1
> Three equivalent conditions: split, has a section, has a retraction. Prove a *cycle* of implications. Start with the easy one: if the sequence is *already* isomorphic to $0\to A\to A\oplus C\to C\to 0$, does the latter obviously have a section?

> [!note]- Hint 2
> (a)$\Rightarrow$(b): the model sequence has the obvious section $\iota_C : C\to A\oplus C$, $c\mapsto(0,c)$; transport it through the splitting isomorphism. For (c)$\Rightarrow$(a): given a retraction $r : B\to A$, consider the map $\varphi = (r, g) : B\to A\oplus C$. Show it is an isomorphism compatible with the sequence maps.

> [!note]- Hint 3
> (b)$\Rightarrow$(c): you have $s : C\to B$ with $gs = \operatorname{id}_C$. Look at $\operatorname{id}_B - sg : B\to B$. Compute $g\circ(\operatorname{id}_B - sg)$ — it should be $0$. So $\operatorname{id}_B - sg$ maps into $\ker g = \operatorname{im} f$. Since $f$ is injective onto its image, you can define $r = f^{-1}\circ(\operatorname{id}_B - sg)$.

> [!note]- Hint 4
> Check the retraction: $rf = f^{-1}(\operatorname{id}_B - sg)f = f^{-1}(f - s(gf))= f^{-1}(f - 0) = \operatorname{id}_A$ (using $gf = 0$). For (c)$\Rightarrow$(a): $\varphi = (r,g)$ is injective ($\varphi(b) = 0$ gives $g(b) = 0$ so $b = f(a)$, then $r(b) = rf(a) = a = 0$, so $b = 0$) and surjective (given $(a, c)$, lift $c$ to $b_0$ with $g(b_0) = c$, then $b = f(a - r(b_0)) + b_0$ works), and $\varphi f = \iota_A$, $\pi_C\varphi = g$.

---

# Solution

The proof is a cycle of three short constructions, each turning one handle on the splitting into another. The plan: (a)$\Rightarrow$(b) transports the obvious section through the splitting isomorphism; (b)$\Rightarrow$(c) builds the retraction from the complementary projection $\operatorname{id}_B - sg$; (c)$\Rightarrow$(a) assembles the isomorphism $(r, g) : B\to A\oplus C$. The one idea doing all the work is that a one-sided inverse on either end determines the entire direct-sum decomposition.

**Step 1: (a) $\Rightarrow$ (b).**

A splitting isomorphism transports the canonical section of the model sequence to a section of $g$.

> [!note]- Derivation
> Suppose the sequence is isomorphic to $0\to A\xrightarrow{\iota_A}A\oplus C\xrightarrow{\pi_C}C\to 0$ via an isomorphism $\varphi : B\xrightarrow{\sim}A\oplus C$ with $\pi_C\circ\varphi = g$. The model has the canonical section $\iota_C : C\to A\oplus C$, $c\mapsto(0,c)$, satisfying $\pi_C\iota_C = \operatorname{id}_C$. Define $s := \varphi^{-1}\circ\iota_C : C\to B$. Then
> $$g\circ s = (\pi_C\varphi)\circ(\varphi^{-1}\iota_C) = \pi_C\iota_C = \operatorname{id}_C,$$
> so $s$ is a section of $g$.

**Step 2: (b) $\Rightarrow$ (c).**

The complementary projection $\operatorname{id}_B - sg$ lands in $\operatorname{im} f$, and composing with $f^{-1}$ gives a retraction.

> [!note]- Derivation
> Let $s : C\to B$ with $gs = \operatorname{id}_C$. Consider $p := \operatorname{id}_B - s g : B\to B$. Then
> $$g\circ p = g - (gs)g = g - \operatorname{id}_C\circ g = g - g = 0,$$
> so $\operatorname{im} p\subseteq\ker g = \operatorname{im} f$. Since $f$ is injective, it is an isomorphism onto $\operatorname{im} f$, with inverse $f^{-1} : \operatorname{im} f\to A$. Define
> $$r := f^{-1}\circ p : B\to A.$$
> Check it retracts $f$: for $a\in A$,
> $$r(f(a)) = f^{-1}(p(f(a))) = f^{-1}(f(a) - s g f(a)) = f^{-1}(f(a) - 0) = a,$$
> using $gf = 0$ (since $\operatorname{im} f = \ker g$). So $rf = \operatorname{id}_A$: $r$ is a retraction.

**Step 3: (c) $\Rightarrow$ (a).**

The map $(r, g) : B\to A\oplus C$ is an isomorphism intertwining the two sequences.

> [!note]- Derivation
> Let $r : B\to A$ with $rf = \operatorname{id}_A$. Define $\varphi := (r, g) : B\to A\oplus C$, $\varphi(b) = (r(b), g(b))$, an $R$-linear map.
>
> *Compatibility with the sequence maps:* $\varphi\circ f = (rf, gf) = (\operatorname{id}_A, 0) = \iota_A$ (the inclusion $a\mapsto(a,0)$), and $\pi_C\circ\varphi = g$. So $\varphi$ is a morphism of sequences.
>
> *Injective:* if $\varphi(b) = (0,0)$ then $g(b) = 0$, so $b\in\ker g = \operatorname{im} f$, say $b = f(a)$; then $0 = r(b) = rf(a) = a$, so $b = f(0) = 0$.
>
> *Surjective:* given $(a, c)\in A\oplus C$, pick $b_0\in B$ with $g(b_0) = c$ (as $g$ is onto). Set $b := f(a - r(b_0)) + b_0$. Then $g(b) = g f(a - r(b_0)) + g(b_0) = 0 + c = c$, and $r(b) = rf(a - r(b_0)) + r(b_0) = (a - r(b_0)) + r(b_0) = a$. So $\varphi(b) = (a, c)$.
>
> Thus $\varphi$ is an isomorphism of sequences, and the sequence splits.

> [!note]- Complete formal solution
> **(a)$\Rightarrow$(b).** Given a splitting iso $\varphi : B\xrightarrow{\sim}A\oplus C$ with $\pi_C\varphi = g$, set $s = \varphi^{-1}\iota_C$ ($\iota_C : c\mapsto(0,c)$). Then $gs = \pi_C\varphi\varphi^{-1}\iota_C = \pi_C\iota_C = \operatorname{id}_C$.
>
> **(b)$\Rightarrow$(c).** Given $s$ with $gs = \operatorname{id}_C$, let $p = \operatorname{id}_B - sg$. Then $gp = g - gsg = 0$, so $\operatorname{im} p\subseteq\ker g = \operatorname{im} f$; set $r = f^{-1}p$. Then $rf = f^{-1}(f - sgf) = f^{-1}f = \operatorname{id}_A$ (as $gf = 0$).
>
> **(c)$\Rightarrow$(a).** Given $r$ with $rf = \operatorname{id}_A$, let $\varphi = (r, g) : B\to A\oplus C$. It satisfies $\varphi f = \iota_A$, $\pi_C\varphi = g$, is injective ($\varphi(b) = 0\Rightarrow b = f(a)$, $a = r(b) = 0$), and surjective (for $(a,c)$, take $b = f(a - r(b_0)) + b_0$ with $g(b_0) = c$). So $\varphi$ is an isomorphism of sequences: the sequence splits.
>
> The cycle (a)$\Rightarrow$(b)$\Rightarrow$(c)$\Rightarrow$(a) establishes the equivalence. $\blacksquare$

---

# Key Takeaways

**A one-sided inverse of either outer map of a short exact sequence determines the whole splitting — a section and a retraction are not independent data.** The conceptual heart is the complementary-projection construction: from a section $s$ of $g$, the map $\operatorname{id}_B - sg$ is a projection onto $\operatorname{im} f$, which *is* a retraction once you compose with $f^{-1}$; symmetrically a retraction $r$ of $f$ makes $\operatorname{id}_B - fr$ a projection onto a complement of $\operatorname{im} f$ realizing a section. So as soon as you have a right inverse on one end, you get a left inverse on the other for free, and vice versa. The reusable principle: to split a short exact sequence, you need produce only *one* of {section, retraction, global isomorphism}, never all three — the cheapest to construct in a given problem suffices. The trigger is "I want $B \cong A\oplus C$"; the reaction is "find any single one-sided inverse."

**The splitting isomorphism is literally $(r, g) : B \to A\oplus C$ — the retraction and the quotient map packaged together.** This explicit formula is worth memorising because it is how splittings are *built*, not merely shown to exist: given a retraction $r$, the pair $(r, g)$ separates $B$ into its $A$-part (read by $r$) and its $C$-part (read by $g$), and the injectivity/surjectivity checks are routine diagram chases using $rf = \operatorname{id}_A$, $gf = 0$, and surjectivity of $g$. Symmetrically, given a section $s$, the inverse splitting is $f\oplus s : A\oplus C\to B$, $(a,c)\mapsto f(a) + s(c)$. The transferable diagnostic: when you need an *explicit* direct-sum decomposition of a module sitting in a short exact sequence, write down $(r, g)$ or $f\oplus s$ and verify — the formula does the work, no abstract appeal needed.

**Splitting is where projectivity meets direct-sum decomposition: a projective quotient guarantees a section, hence a splitting.** This lemma is the precise mechanism by which [[Def - Projective Module|projectivity]] of $C$ forces $0\to A\to B\to C\to 0$ to split — projectivity is exactly "the identity $\operatorname{id}_C$ lifts through $g$", which *is* a section, and the lemma then delivers $B\cong A\oplus C$. So whenever the right-hand term of a short exact sequence is free or projective, the sequence splits automatically, and this is the single most-used sufficient condition for splitting in practice (it is how [[Thm - Projective iff Direct Summand of a Free Module|projective ⇔ summand of free]] is proved). The crucial caution, however: splitting is about the *maps*, and "$B\cong A\oplus C$ abstractly" does **not** imply the sequence splits — there exist non-split sequences whose middle term is abstractly the direct sum (see [[Ex - A short exact sequence that does not split though B is the direct sum]]). The lemma's equivalence (a)$\Leftrightarrow$(b)$\Leftrightarrow$(c) is between *compatible* splittings, the ones intertwining $f$ and $g$, which is the content that the abstract isomorphism type misses.

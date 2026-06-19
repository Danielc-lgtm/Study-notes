---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Adjunction"
  - "Def - Unit and Counit of an Adjunction"
  - "Def - Category"
tags: [category-theory, foundations]
---

# Problem Statement

A **monotone Galois connection** between partially ordered sets $(P, \leq)$ and $(Q, \leq)$ is a pair of monotone maps $f : P\to Q$ and $g : Q\to P$ such that
$$f(a)\leq b \iff a\leq g(b) \qquad\text{for all } a\in P,\ b\in Q.$$

**(a)** Regard $P$ and $Q$ as categories (one morphism $x\to y$ exactly when $x\leq y$). Show that a monotone Galois connection is *exactly* an adjunction $f\dashv g$ between these categories.

**(b)** Identify the unit and counit, and show the triangle identities are automatic.

**(c)** Deduce the standard Galois-connection facts $f g f = f$ and $g f g = g$, and that $gf$ and $fg$ are idempotent (a closure and an interior operator). Give one concrete example.

**Recall:**

A poset $(P,\leq)$ as a [[Def - Category|category]]: objects are elements; there is a unique morphism $a\to a'$ iff $a\leq a'$; composition is transitivity; identities are reflexivity. A [[Def - Functor|functor]] between posets is a monotone map. An [[Def - Adjunction|adjunction]] $f\dashv g$ is a natural bijection $Q(f a, b)\cong P(a, g b)$.

---

# Convergent Strategy

**Problem class:** This is a "recognise a known structure as an adjunction" problem in the degenerate but illuminating poset setting, where hom-sets have at most one element. It shows that adjunctions specialise to Galois connections and that all the unit/counit/triangle machinery collapses to order inequalities.

**Assumption pattern:** The key feature is that in a poset, a hom-set $Q(fa, b)$ is either empty or a singleton — it is "true or false that $fa\leq b$". So the adjunction *bijection* degenerates to a *bi-implication*, which is exactly the Galois-connection condition. Everything about the adjunction becomes order theory.

**Theorem routing:** Translate "$Q(fa,b)\cong P(a,gb)$ natural" into "$fa\leq b\iff a\leq gb$" (part a). Read the unit as $a\leq g(f(a))$ and the counit as $f(g(b))\leq b$ (part b). The triangle identities hold automatically because any two parallel morphisms in a poset are equal. The standard facts (part c) follow by applying the inequalities both ways.

**Key decision point:** The non-obvious recognition is that *naturality is free* in a poset. A bijection of hom-sets that are each at most singletons is automatically natural, because all naturality squares commute (any diagram of $\leq$-morphisms with fixed endpoints commutes). So a monotone Galois connection needs no naturality check — the bi-implication is the entire adjunction.

---

# Legal Operations Used

1. **Operation 7 from the topic page (recognise a Galois connection as an adjunction between posets).** This is the exercise itself: identifying the two notions.

2. **Operation 3 from the topic page (build the unit and counit).** The unit and counit are read off as the two defining inequalities.

3. **Operation 8 from the topic page (identify a reflector to import localization theorems).** Part (c) recognises $gf$ as a closure operator (idempotent monad on a poset).

---

# Hints

> [!note]- Hint 1
> In a poset, $Q(fa, b)$ has exactly one element if $fa\leq b$ and none otherwise. So a bijection $Q(fa,b)\cong P(a,gb)$ just says the two hom-sets are simultaneously nonempty: $fa\leq b\iff a\leq gb$.

> [!note]- Hint 2
> Set $b = f(a)$ in $fa\leq b\iff a\leq gb$ (so $fa\leq fa$ is true) to get $a\leq g(f(a))$ — the unit. Set $a = g(b)$ to get $f(g(b))\leq b$ — the counit.

> [!note]- Hint 3
> For $fgf = f$: apply monotonicity and the unit/counit inequalities to sandwich $f(a)$ between $f g f(a)$ from both sides. The triangle identities, written as inequalities, give both $f(a)\leq fgf(a)$ and $fgf(a)\leq f(a)$.

---

# Solution

In a poset every hom-set is at most a singleton, so the adjunction bijection becomes the Galois bi-implication, naturality is free, the unit and counit are the two defining inequalities, and the triangle identities are automatic. The classical facts follow by applying the inequalities in both directions.

**Step 1: Galois connection $=$ adjunction (part a).**

A monotone $f, g$ with $fa\leq b\iff a\leq gb$ is exactly $f\dashv g$ between the posets-as-categories.

> [!note]- Derivation
> View $P, Q$ as categories. The hom-set $Q(fa, b)$ is a singleton if $fa\leq b$ and empty otherwise; similarly $P(a, gb)$. A natural bijection $Q(fa, b)\cong P(a, gb)$ requires precisely that the two sets are nonempty together, i.e. $fa\leq b\iff a\leq gb$ — the Galois-connection condition. Conversely, given the bi-implication, define $\Phi$ to be the unique map between singletons; it is a bijection wherever both sides are nonempty.
>
> **Naturality is automatic.** A naturality square in a poset is a square of $\leq$-morphisms; any two morphisms with the same source and target are equal (at most one exists), so every square commutes. Functoriality of $f, g$ is monotonicity. Hence the bi-implication *is* the adjunction $f\dashv g$, with no extra conditions.

**Step 2: Unit, counit, triangle identities (part b).**

Unit: $a\leq g(f(a))$. Counit: $f(g(b))\leq b$. Triangle identities: automatic.

> [!note]- Derivation
> The unit $\eta_a : a\to g(f(a))$ exists iff $a\leq g(f(a))$; setting $b = f(a)$ in the bi-implication, $f(a)\leq f(a)$ (true) gives $a\leq g(f(a))$. So the unit is the inequality $a\leq gf(a)$.
>
> The counit $\varepsilon_b : f(g(b))\to b$ exists iff $f(g(b))\leq b$; setting $a = g(b)$, $g(b)\leq g(b)$ (true) gives $f(g(b))\leq b$. So the counit is $fg(b)\leq b$.
>
> The triangle identities $\varepsilon_{fa}\circ f\eta_a = 1_{fa}$ etc. are equalities of morphisms in a poset; since any two parallel morphisms coincide, they hold automatically. (They carry no information beyond the existence of the relevant inequalities.)

**Step 3: Standard facts (part c).**

$fgf = f$, $gfg = g$, and $gf$, $fg$ are idempotent; $gf$ is a closure operator, $fg$ an interior operator.

> [!note]- Derivation
> **$fgf = f$.** By the unit applied to $a$: $a\leq gf(a)$, and $f$ monotone gives $f(a)\leq fgf(a)$. By the counit applied to $b = f(a)$: $fg(f(a))\leq f(a)$, i.e. $fgf(a)\leq f(a)$. Together $f(a)\leq fgf(a)\leq f(a)$, so $fgf(a) = f(a)$. Dually $gfg = g$.
>
> **Idempotence of $gf$.** $gf gf = g(fgf) = g f$ using $fgf = f$. So $gf$ is idempotent. With monotonicity and the unit $a\leq gf(a)$, the operator $c := gf$ is monotone, inflationary ($a\leq c(a)$), and idempotent ($c c = c$) — a **closure operator** on $P$. Dually $fg$ is monotone, *deflationary* ($fg(b)\leq b$), idempotent — an **interior operator** on $Q$. In adjunction language $gf$ is the idempotent monad of a reflective inclusion: the closed elements (fixed points of $gf$) form a [[Def - Reflective Subcategory|reflective sub-poset]].
>
> **Example.** Let $P$ and $Q$ both be the power set of a set $X$, ordered by inclusion, and let $R\subseteq X\times Y$ be a relation. Define $f(A) = \{y : \forall a\in A,\ aRy\}$ and $g(B) = \{x : \forall b\in B,\ xRb\}$. Then $f(A)\subseteq B\iff A\subseteq g(B)$ (both say $A\times B\subseteq R$), so $f\dashv g$ is a Galois connection; $gf$ is the closure operator whose closed sets are the "Galois-closed" sets, the engine of **formal concept analysis** and of the Galois correspondence of field theory (where $f$ is "fixed field of" and $g$ is "automorphisms fixing").

> [!note]- Complete formal solution
> **(a)** In posets-as-categories, $Q(fa,b)$ and $P(a,gb)$ are each at most singletons; a natural bijection between them is exactly $fa\leq b\iff a\leq gb$, with naturality automatic (parallel morphisms in a poset coincide). So a monotone Galois connection is precisely $f\dashv g$.
>
> **(b)** Unit: $a\leq gf(a)$ (set $b = fa$). Counit: $fg(b)\leq b$ (set $a = gb$). Triangle identities hold automatically since any two parallel poset-morphisms are equal.
>
> **(c)** $fgf = f$ from $f(a)\leq fgf(a)$ (unit $+$ monotonicity) and $fgf(a)\leq f(a)$ (counit at $fa$); dually $gfg = g$. Hence $gf$ is monotone, inflationary, idempotent — a closure operator — and $fg$ is an interior operator. Example: the Galois connection of a relation $R\subseteq X\times Y$, $f(A) = A^R$, $g(B) = {}^R B$. $\blacksquare$

---

# Key Takeaways

**A Galois connection is an adjunction with the truth values forgotten — and seeing this imports all of adjunction theory into order theory.** When hom-sets are at most singletons, the adjunction bijection $Q(fa,b)\cong P(a,gb)$ degenerates to the bi-implication $fa\leq b\iff a\leq gb$, the unit and counit become the inequalities $a\leq gfa$ and $fgb\leq b$, and the triangle identities evaporate (they are equalities of unique morphisms). So every theorem about adjunctions specialises to a theorem about Galois connections for free: uniqueness of adjoints becomes uniqueness of the upper/lower adjoint, [[Thm - Right Adjoints Preserve Limits|RAPL]] becomes "the upper adjoint $g$ preserves meets" and LAPC "the lower adjoint $f$ preserves joins". The trigger to deploy this is *any* "best approximation from above/below", *any* closure or interior operator, *any* Galois correspondence — these are all adjunctions in disguise.

**Naturality is free in a poset, which is why Galois connections are so easy to produce.** The reason a monotone Galois connection requires no coherence check beyond the bi-implication is that all naturality squares in a poset commute automatically (parallel morphisms are equal). This is the cheapest possible adjunction to verify: just check $fa\leq b\iff a\leq gb$. It is also a useful diagnostic in the other direction — when an adjunction-like structure lives over a poset (a preorder of "approximations", a lattice of "states"), you need only check the bi-implication, never naturality. This is exploited constantly in domain theory, abstract interpretation, and program analysis, where Galois connections relate concrete and abstract semantic lattices.

**The composite $gf$ is a closure operator — the order-theoretic shadow of "every adjunction yields a monad".** That $gf$ is monotone, inflationary, and idempotent makes it a closure operator, and its fixed points form a reflective sub-poset; dually $fg$ is an interior operator. This is precisely the poset instance of the Chapter V fact that *every adjunction yields a monad* $GF$ — here the monad is idempotent (because the poset is thin), so it is a closure operator and the subcategory of algebras is reflective. Recognising closure operators as idempotent monads, and Galois connections as their adjunctions, is the bridge from concrete order theory (topological closure, convex hull, span, the Galois correspondence of [[Thm - Galois Correspondence for Covering Spaces|covering spaces]]) up to the general theory. The companion exercise [[Ex - Abelianization is left adjoint to inclusion|Abelianization is left adjoint to inclusion]] shows the same idempotent-monad pattern outside the poset world, where the reflection is a genuine quotient rather than a closure.

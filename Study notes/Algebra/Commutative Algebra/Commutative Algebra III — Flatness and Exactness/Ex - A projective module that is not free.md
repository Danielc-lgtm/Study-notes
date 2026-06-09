---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Projective Module"
  - "Def - Free Module"
  - "Thm - Projective iff Direct Summand of a Free Module"
  - "Def - Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Give an example of an $R$-module that is [[Def - Projective Module|projective]] but not [[Def - Free Module|free]], over some ring $R$. This separates projectivity from freeness, showing the implication "free $\Rightarrow$ projective" is strict.

The cleanest example: take $R = \mathbb{Z}/6$. Show that, under $\mathbb{Z}/6 \cong \mathbb{Z}/2 \times \mathbb{Z}/3$, the submodule $\mathbb{Z}/2 \cong (\mathbb{Z}/2)\times\{0\}$ is a direct summand of the free module $R$ — hence projective — but is not a free $R$-module.

**Recall:**

The objects in play are projective modules, free modules, and idempotents.

![[Def - Projective Module#The Definition]]

By [[Thm - Projective iff Direct Summand of a Free Module|the characterization]], $M$ is projective iff it is a **direct summand of a free module**: $M \oplus N \cong R^{\oplus I}$.

![[Def - Free Module#The Definition]]

A [[Def - Free Module|free module]] of rank $n$ over $R$ has a basis of $n$ elements, so as a set it is $R^n$ and (for finite $R$) has exactly $|R|^n$ elements.

An element $e \in R$ is an **idempotent** if $e^2 = e$. For an idempotent $e$, $R = Re \oplus R(1-e)$ as $R$-modules: every $r = re + r(1-e)$, and $Re \cap R(1-e) = 0$ since $x = ae = b(1-e)$ gives $x = xe = b(1-e)e = 0$. So $Re$ is a direct summand of the free module $R$, hence projective.

The bridge that makes the example run — *an idempotent splits the ring as a module into two projective pieces*, and over $\mathbb{Z}/6 \cong \mathbb{Z}/2\times\mathbb{Z}/3$ those pieces are $\mathbb{Z}/2$ and $\mathbb{Z}/3$, neither of which is large enough to be a free $\mathbb{Z}/6$-module.

---

# Convergent Strategy

**Problem class.** This is a *construct-a-separating-example* problem: produce a module satisfying the weaker tower condition (projective) but not the stronger (free), so the inclusion free $\subsetneq$ projective is strict. As the [[Commutative Algebra III — Flatness and Exactness]] strategy records, the engine for projective-not-free over a non-domain is always an *idempotent*, which splits the ring as a module.

**Assumption pattern.** The recognisable trigger is that $R$ is a *product ring* (or has a non-trivial idempotent). A product $R = R_1\times R_2$ has the idempotent $e = (1,0)$, and $Re \cong R_1$ is then a summand of $R$ — automatically projective — while being "too small" to be free if $|R_1| < |R|$.

**Theorem routing.** Projectivity: $e = (1,0)$ is idempotent, so $R = Re\oplus R(1-e)$, exhibiting $Re$ as a direct summand of the free module $R$; by the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]], $Re$ is projective. Non-freeness: a free $R$-module of rank $n$ has $|R|^n$ elements (here $6^n$), but $Re \cong \mathbb{Z}/2$ has $2$ elements; $2 \neq 6^n$ for any $n\geq 0$ ($6^0 = 1$, $6^1 = 6$, ...), so $Re$ is not free.

**Key decision point.** The non-obvious move is the *cardinality count* refuting freeness. One might expect to argue about bases or linear independence, but the cleanest obstruction over a *finite* ring is simply counting: a free module's size is a power of $|R|$, and $\mathbb{Z}/2$'s size $2$ is not a power of $6$. The genuine insight is that idempotents manufacture projectives effortlessly (any product ring has them), and that finiteness turns "not free" into an arithmetic impossibility. The natural wrong instinct — to hunt for a subtle linear-algebra obstruction — is unnecessary; $2 \nmid$ any power-of-$6$ count is decisive.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra III — Flatness and Exactness#Legal Operations|the topic page's Legal Operations]]:

1. **Split the ring with an idempotent (operation 7, summand form).** $e^2 = e$ gives $R = Re\oplus R(1-e)$, so $Re$ is a summand of the free module $R$.

2. **Read off projectivity from the summand form (operation 7).** A direct summand of a free module is projective by the [[Thm - Projective iff Direct Summand of a Free Module|characterization]].

3. **Refute freeness by counting elements.** Over a finite ring, a free module has $|R|^n$ elements; a mismatch in cardinality rules out freeness.

---

# Hints

> [!note]- Hint 1
> "Projective but not free" needs a ring that is *not* a domain and not local — the gap closes over PIDs and local rings. What is the simplest such ring? A *product* of two fields or two rings always has the right structure. And products have a special kind of element that splits them.

> [!note]- Hint 2
> Take $R = \mathbb{Z}/6 \cong \mathbb{Z}/2\times\mathbb{Z}/3$ (Chinese Remainder Theorem). The element $e = (1, 0)$ satisfies $e^2 = e$ — it is an *idempotent*. What does an idempotent do to $R$ as a module over itself?

> [!note]- Hint 3
> An idempotent $e$ gives $R = Re \oplus R(1-e)$ as $R$-modules. So $Re$ is a direct summand of the free module $R$, hence projective by the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]]. Here $Re \cong \mathbb{Z}/2$. Now: how many elements does a free $\mathbb{Z}/6$-module have?

> [!note]- Hint 4
> A free $\mathbb{Z}/6$-module of rank $n$ is $(\mathbb{Z}/6)^n$, with $6^n$ elements: $1, 6, 36, \dots$. But $Re \cong \mathbb{Z}/2$ has $2$ elements, and $2$ is not in $\{1, 6, 36, \dots\}$. So $Re$ cannot be free, while it *is* projective.

---

# Solution

The construction is the cleanest projective-not-free witness: a product ring supplies an idempotent, the idempotent splits the ring as a module into projective summands, and finiteness makes "not free" an arithmetic count. The crux is that idempotents are an effortless source of projectives, and over a finite ring freeness is detectable by cardinality alone.

**Step 1: $\mathbb{Z}/6$ splits as a product, supplying an idempotent.**

$\mathbb{Z}/6 \cong \mathbb{Z}/2 \times \mathbb{Z}/3$, and $e = (1,0)$ is an idempotent.

> [!note]- Derivation
> By the Chinese Remainder Theorem (as $2, 3$ are coprime), $\mathbb{Z}/6 \cong \mathbb{Z}/2 \times \mathbb{Z}/3$ as rings, via $x \bmod 6 \mapsto (x \bmod 2, x \bmod 3)$. In the product, the element $e = (1, 0)$ satisfies
> $$e^2 = (1,0)\cdot(1,0) = (1, 0) = e,$$
> so $e$ is an [[Def - Ideal|idempotent]]. (Concretely $e$ corresponds to $3 \in \mathbb{Z}/6$: $3^2 = 9 \equiv 3 \pmod 6$.) Also $1 - e = (0, 1)$ is idempotent (corresponding to $4 \in \mathbb{Z}/6$).

**Step 2: The idempotent splits $R$ into projective summands.**

$R = Re \oplus R(1-e)$, so $Re \cong \mathbb{Z}/2$ is a direct summand of the free module $R$, hence projective.

> [!note]- Derivation
> For any idempotent $e \in R$ we have $R = Re \oplus R(1-e)$ as $R$-modules:
> - *Spanning:* every $r = re + r(1-e)$, with $re \in Re$, $r(1-e)\in R(1-e)$.
> - *Independence:* if $x \in Re \cap R(1-e)$, write $x = ae = b(1-e)$. Then $xe = ae^2 = ae = x$, but also $xe = b(1-e)e = b(e - e^2) = 0$, so $x = 0$.
>
> Under $\mathbb{Z}/6\cong\mathbb{Z}/2\times\mathbb{Z}/3$ and $e = (1,0)$: $Re = (\mathbb{Z}/2\times\mathbb{Z}/3)\cdot(1,0) = \mathbb{Z}/2\times\{0\}\cong\mathbb{Z}/2$, and $R(1-e)\cong\mathbb{Z}/3$. So
> $$R = Re \oplus R(1-e) \cong \mathbb{Z}/2 \oplus \mathbb{Z}/3.$$
> Since $R$ is free (of rank $1$ over itself) and $Re$ is a direct summand of it, the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization of projectivity]] makes $Re \cong \mathbb{Z}/2$ a **projective** $R$-module.

**Step 3: $\mathbb{Z}/2$ is not a free $\mathbb{Z}/6$-module.**

A free $\mathbb{Z}/6$-module has $6^n$ elements; $\mathbb{Z}/2$ has $2$, which is no power of $6$.

> [!note]- Derivation
> A [[Def - Free Module|free]] $R = \mathbb{Z}/6$-module of rank $n$ is isomorphic to $R^n = (\mathbb{Z}/6)^n$, which has exactly
> $$|R|^n = 6^n$$
> elements. The possible cardinalities of a free $\mathbb{Z}/6$-module are therefore $\{6^n : n \geq 0\} = \{1, 6, 36, 216, \dots\}$ (the zero module, $n = 0$, has one element).
>
> But $Re \cong \mathbb{Z}/2$ has exactly $2$ elements, and $2 \notin \{1, 6, 36, \dots\}$. A free module's cardinality must be a power of $|R| = 6$, so $Re$ cannot be free. (Indeed, $(0,1)\cdot(1,0) = 0$ shows the single generator $e$ is annihilated by the non-zero element $(0,1)$, so $\{e\}$ is not a basis — no basis exists.)

> [!note]- Complete formal solution
> Let $R = \mathbb{Z}/6 \cong \mathbb{Z}/2\times\mathbb{Z}/3$ and $e = (1,0)$, an idempotent ($e^2 = e$).
>
> **Projective.** For an idempotent $e$, $R = Re\oplus R(1-e)$ as $R$-modules (spanning: $r = re + r(1-e)$; independence: $x = ae = b(1-e)$ gives $x = xe = 0$). Thus $Re \cong \mathbb{Z}/2$ is a direct summand of the free module $R$, hence projective by [[Thm - Projective iff Direct Summand of a Free Module|the summand characterization]].
>
> **Not free.** A free $\mathbb{Z}/6$-module of rank $n$ has $6^n$ elements. Since $|Re| = |\mathbb{Z}/2| = 2$ and $2 \neq 6^n$ for all $n \geq 0$, the module $Re$ is not free.
>
> Hence $\mathbb{Z}/2$ is a projective but not free $\mathbb{Z}/6$-module, so free $\Rightarrow$ projective is strict. $\blacksquare$

**A second, infinite example (Dedekind domains).**

> [!note]- Derivation
> Over $R = \mathbb{Z}[\sqrt{-5}]$, the ideal $I = (2, 1+\sqrt{-5})$ is projective but not free. *Projective:* every ideal of a Dedekind domain is projective (it is a rank-one summand of $R^2$ via a presentation $R^2 \to I$ whose kernel is a complementary ideal). *Not free:* $I$ is not principal (it is the non-trivial class in the ideal class group of $\mathbb{Z}[\sqrt{-5}]$), so it is not free of rank $1$; and rank considerations (its rank as a module is $1$) exclude any other rank. This example is the number-theoretic face of projective-not-free, where the obstruction is the **ideal class group** rather than a cardinality count.

---

# Key Takeaways

**Idempotents are the universal source of projective-but-not-free modules over non-domains — recognise a product ring and you have one for free.** The entire construction is "a product ring $R_1\times R_2$ has the idempotent $(1,0)$, which splits $R$ as a module into $R_1\oplus R_2$, each a projective summand." Whenever a ring fails to be connected (its $\operatorname{Spec}$ is disconnected, equivalently it has a non-trivial idempotent, equivalently it is a non-trivial product), you immediately get projective modules that are smaller than the ring and so cannot be free. The trigger is "$R$ is a product" or "$R$ has $e^2 = e$ with $e \neq 0, 1$"; the reaction is "$Re$ is projective, and check its size against $|R|$." This is the cheapest separating example in the chapter and the reason projective $\neq$ free precisely fails to be an equality over disconnected (or non-local, non-PID) rings.

**Over a finite ring, freeness is decidable by counting: a free module has exactly $|R|^n$ elements.** The refutation of freeness needs no linear algebra — a free $R$-module of rank $n$ is $R^n$ with $|R|^n$ elements, so any module whose cardinality is not a power of $|R|$ is automatically not free. Here $|\mathbb{Z}/2| = 2$ is not a power of $6$, and the matter is settled. The transferable diagnostic: when working over a finite ring and asked whether a module is free, *count first* — the cardinality constraint is often decisive and far easier than exhibiting or excluding a basis. This complements the structural view: the generator $e$ of $Re$ is annihilated by $(0,1)\neq 0$, so it is not even linearly independent, confirming no basis exists.

**The projective-free gap is the algebra of non-trivial vector bundles, and its two faces are idempotents (disconnected base) and ideal classes (number theory).** The finite example $\mathbb{Z}/2$ over $\mathbb{Z}/6$ and the infinite example $(2, 1+\sqrt{-5})$ over $\mathbb{Z}[\sqrt{-5}]$ are the two canonical witnesses, and they reveal the two geometric meanings of projective-not-free. The idempotent example corresponds to a *disconnected* space, where a "bundle" can have different ranks on different components — locally free but not globally free in the crudest way. The ideal example corresponds to a *connected* space (a curve) with a genuinely twisted line bundle, measured by the **ideal class group** under the [[Thm - Projective iff Direct Summand of a Free Module|Serre–Swan]] dictionary. Recognising which mechanism is in play — an idempotent splitting, or a non-principal ideal class — tells you immediately *why* a given projective fails to be free, and is the reusable insight for the companion separations [[Ex - Q is a flat but not projective Z-module]] and [[Ex - Free implies projective implies flat implies torsion-free]].

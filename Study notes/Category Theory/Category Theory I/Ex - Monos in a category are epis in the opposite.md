---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Opposite Category and Duality"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a [[Def - Category|category]] and $f : A \to B$ a morphism. Show that
$$f \text{ is a monomorphism in } \mathcal{C} \iff f^{\mathrm{op}} \text{ is an epimorphism in } \mathcal{C}^{\mathrm{op}},$$
and symmetrically that $f$ is an epimorphism in $\mathcal{C}$ iff $f^{\mathrm{op}}$ is a monomorphism in $\mathcal{C}^{\mathrm{op}}$. Conclude that "monomorphism" and "epimorphism" are dual notions, and explain how this is one instance of the [[Thm - The Duality Principle|duality principle]].

**Recall:**

![[Def - Opposite Category and Duality#The Definition]]

A [[Def - Isomorphism, Monomorphism, Epimorphism|monomorphism]] is left-cancellable: $f g = f h \implies g = h$. An [[Def - Isomorphism, Monomorphism, Epimorphism|epimorphism]] is right-cancellable: $g f = h f \implies g = h$.

---

# Convergent Strategy

**Problem class:** This is a "verify a dual pair" exercise — the prototype showing two notions are related by arrow reversal. The route is to write down the cancellation condition for mono in $\mathcal{C}$, translate every arrow and composite into $\mathcal{C}^{\mathrm{op}}$, and observe it becomes the cancellation condition for epi.

**Assumption pattern:** The only structure used is the definition of the [[Def - Opposite Category and Duality|opposite category]]: morphisms reverse and composition reverses order, $g^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}} = (f \circ g)^{\mathrm{op}}$. The cancellation property is purely equational, so it translates mechanically.

**Theorem routing:** This *is* the [[Thm - The Duality Principle|duality principle]] in miniature: "$f$ is mono" is a categorical statement, and its dual is "$f$ is epi". The exercise verifies by hand the single translation that the duality principle then automates for all statements.

**Key decision point:** The one place to be careful is the *reversal of composition order*: the equation $f \circ g = f \circ h$ defining left-cancellability becomes $g^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}} = h^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}}$ in $\mathcal{C}^{\mathrm{op}}$, which is right-cancellability of $f^{\mathrm{op}}$. Dropping the reorder would produce nonsense.

---

# Legal Operations Used

1. **Operation: translate a statement across the opposite category** (topic page, Legal Operation 8). We rewrite the cancellation equation of $\mathcal{C}$ as a cancellation equation of $\mathcal{C}^{\mathrm{op}}$, reversing arrows and composition order.

2. **Operation: read off a dual notion** (topic page, Legal Operation 9). Identifying the translated condition as "epi" exhibits mono and epi as a dual pair.

---

# Hints

> [!note]- Hint 1
> Write the mono condition for $f$: for all $g, h : X \to A$, $f g = f h \implies g = h$. Now reverse every arrow. What do $g, h$ become in $\mathcal{C}^{\mathrm{op}}$?

> [!note]- Hint 2
> In $\mathcal{C}^{\mathrm{op}}$, the morphisms $g^{\mathrm{op}}, h^{\mathrm{op}}$ go $A \to X$. Composition reverses: $f \circ g$ in $\mathcal{C}$ is $g^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}}$ in $\mathcal{C}^{\mathrm{op}}$.

> [!note]- Hint 3
> The translated condition reads: for all $g^{\mathrm{op}}, h^{\mathrm{op}} : A \to X$, $g^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}} = h^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}} \implies g^{\mathrm{op}} = h^{\mathrm{op}}$. That is right-cancellability of $f^{\mathrm{op}}$.

---

# Solution

The plan is a single translation. Write left-cancellability of $f$ in $\mathcal{C}$, push it through the opposite-category dictionary (arrows reverse, composition reverses order), and read the result as right-cancellability of $f^{\mathrm{op}}$ in $\mathcal{C}^{\mathrm{op}}$. The symmetric statement follows by applying the same argument with $\mathcal{C}$ replaced by $\mathcal{C}^{\mathrm{op}}$ and using $(\mathcal{C}^{\mathrm{op}})^{\mathrm{op}} = \mathcal{C}$.

**Step 1: Translate "mono in $\mathcal{C}$" into $\mathcal{C}^{\mathrm{op}}$.**

> [!note]- Derivation
> "$f$ is a monomorphism in $\mathcal{C}$" means: for all objects $X$ and all $g, h \in \mathcal{C}(X, A)$,
> $$f \circ g = f \circ h \implies g = h.$$
> Under the opposite-category correspondence, $\mathcal{C}(X, A) = \mathcal{C}^{\mathrm{op}}(A, X)$, so $g, h$ become morphisms $g^{\mathrm{op}}, h^{\mathrm{op}} : A \to X$ in $\mathcal{C}^{\mathrm{op}}$. The composite $f \circ g$ in $\mathcal{C}$ equals $g^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}}$ in $\mathcal{C}^{\mathrm{op}}$ (by the reversal-of-composition law $(f \circ g)^{\mathrm{op}} = g^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}}$). So the condition becomes: for all $g^{\mathrm{op}}, h^{\mathrm{op}} \in \mathcal{C}^{\mathrm{op}}(A, X)$,
> $$g^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}} = h^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}} \implies g^{\mathrm{op}} = h^{\mathrm{op}}.$$

**Step 2: Recognize the translated condition as "epi in $\mathcal{C}^{\mathrm{op}}$".**

> [!note]- Derivation
> The condition in Step 1 is precisely right-cancellability of $f^{\mathrm{op}} : B \to A$ in $\mathcal{C}^{\mathrm{op}}$ — pre-composition by $f^{\mathrm{op}}$ is injective. That is the definition of $f^{\mathrm{op}}$ being an [[Def - Isomorphism, Monomorphism, Epimorphism|epimorphism]] in $\mathcal{C}^{\mathrm{op}}$. Both directions of the implication are visible because the translation is a literal equivalence of statements (every step is an "iff"), so $f$ mono in $\mathcal{C} \iff f^{\mathrm{op}}$ epi in $\mathcal{C}^{\mathrm{op}}$.

**Step 3: The symmetric statement and the conclusion.**

> [!note]- Derivation
> Apply Step 1–2 with $\mathcal{C}$ replaced by $\mathcal{C}^{\mathrm{op}}$: "$f^{\mathrm{op}}$ is mono in $\mathcal{C}^{\mathrm{op}} \iff (f^{\mathrm{op}})^{\mathrm{op}}$ is epi in $(\mathcal{C}^{\mathrm{op}})^{\mathrm{op}}$". Since $(\mathcal{C}^{\mathrm{op}})^{\mathrm{op}} = \mathcal{C}$ and $(f^{\mathrm{op}})^{\mathrm{op}} = f$, this reads "$f^{\mathrm{op}}$ mono in $\mathcal{C}^{\mathrm{op}} \iff f$ epi in $\mathcal{C}$". Combining, mono and epi are interchanged by passing to the opposite. This is exactly one instance of the [[Thm - The Duality Principle|duality principle]]: the categorical statement "$f$ is mono" has dual "$f$ is epi", so any theorem about monomorphisms yields, for free, the arrow-reversed theorem about epimorphisms.

> [!note]- Complete formal solution
> "$f$ mono in $\mathcal{C}$" is: $\forall g, h \in \mathcal{C}(X,A),\ f g = f h \Rightarrow g = h$. Translating to $\mathcal{C}^{\mathrm{op}}$ via $\mathcal{C}(X,A) = \mathcal{C}^{\mathrm{op}}(A,X)$ and $(fg)^{\mathrm{op}} = g^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}}$, the condition becomes $\forall g^{\mathrm{op}}, h^{\mathrm{op}},\ g^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}} = h^{\mathrm{op}} \circ^{\mathrm{op}} f^{\mathrm{op}} \Rightarrow g^{\mathrm{op}} = h^{\mathrm{op}}$, i.e. $f^{\mathrm{op}}$ is right-cancellable, i.e. epi in $\mathcal{C}^{\mathrm{op}}$. Every step is an equivalence, so $f$ mono $\iff f^{\mathrm{op}}$ epi. Replacing $\mathcal{C}$ by $\mathcal{C}^{\mathrm{op}}$ and using the involution $(-)^{\mathrm{op}}$ gives $f$ epi $\iff f^{\mathrm{op}}$ mono. Thus mono and epi are dual. $\blacksquare$

---

# Key Takeaways

**Dual pairs are arrow-reversals, verified once and reused forever.** This exercise is the template for recognizing that two notions are dual: write one as a categorical statement, reverse every arrow and every composition order, and check you land on the other. Mono/epi, product/coproduct, initial/terminal, limit/colimit, kernel/cokernel, projective/injective all pass this test. The payoff is the [[Thm - The Duality Principle|duality principle]]: once you know mono and epi are dual, *every* theorem you prove about monomorphisms automatically yields the arrow-reversed theorem about epimorphisms, with no further work. Internalizing this halves the proof burden across the whole subject.

**Composition order is the one thing that flips — never forget the reorder.** The single mechanical pitfall in any duality computation is the reversal of composition order: $g \circ f$ in $\mathcal{C}$ becomes $f^{\mathrm{op}} \circ^{\mathrm{op}} g^{\mathrm{op}}$ in $\mathcal{C}^{\mathrm{op}}$. This is the same flip as $(gh)^{-1} = h^{-1}g^{-1}$ in a [[Def - Group|group]] and $(AB)^T = B^T A^T$ for matrices. Whenever you dualize a statement involving a composite, reverse the order; the trigger is "I see $\circ$ inside a statement I am dualizing". Getting this right is what makes the translation an exact equivalence rather than a typing error.

**Left and right are mirror images, not independent.** The deeper conceptual point is that "left-cancellable" and "right-cancellable" are not two unrelated properties that happen to look similar — they are literally the same property viewed in the mirror $\mathcal{C} \leftrightarrow \mathcal{C}^{\mathrm{op}}$. This explains why so many results about monomorphisms have epimorphism analogues with proofs that "look the same with the arrows reversed": they *are* the same proof, run in the opposite category. Whenever you find yourself about to re-prove a left-handed result on the right, stop and invoke duality instead.

---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Category"
  - "Def - Group"
tags: [category-theory, foundations]
---

# Problem Statement

Show that **a monoid is the same data as a category with exactly one object**. Precisely: given a monoid $(M, \cdot, e)$, construct a [[Def - Category|category]] $\mathbf{B}M$ with one object whose morphisms are the elements of $M$; conversely, show that any one-object category arises this way from a unique monoid. Then identify which one-object categories are [[Def - Groupoid|groupoids]], and which monoids they correspond to.

**Recall:**

A **monoid** is a set $M$ with an associative binary operation $\cdot : M \times M \to M$ and a two-sided identity element $e$ (so $e \cdot m = m \cdot e = m$). It is a [[Def - Group|group]] without the requirement of inverses.

![[Def - Category#The Definition]]

---

# Convergent Strategy

**Problem class:** This is a "degenerate-case identification" — recognizing a familiar algebraic structure as a special case of a categorical one by collapsing the number of objects. The route is to match the category axioms to the monoid axioms term by term, in both directions.

**Assumption pattern:** With a single object $\ast$, there is only one hom-set $\mathcal{C}(\ast, \ast)$, so *every* pair of morphisms is composable. This is the key simplification: the "typing" of composition, which normally makes it partial, becomes vacuous, and composition becomes a total binary operation on one set — exactly a monoid multiplication.

**Theorem routing:** No theorem is needed; the proof is a direct unwinding of definitions. The category's associativity axiom *is* monoid associativity; the category's identity axiom *is* the monoid identity law; the single hom-set *is* the underlying set $M$.

**Key decision point:** The only subtlety is the direction "one-object category $\Rightarrow$ monoid": one must observe that the unique identity morphism $1_\ast$ is forced to be the monoid identity, and that composition's totality (every pair composable) is what is special about the one-object case.

---

# Legal Operations Used

1. **Operation: regard an algebraic structure as a category** (topic page, Legal Operation 1). We package a monoid as a category by taking its elements to be the morphisms of a single object.

2. **Operation: match axioms across the dictionary** (topic page, Legal Operation 4). Each category axiom is paired with the corresponding monoid axiom, establishing the equivalence of data.

---

# Hints

> [!note]- Hint 1
> With one object $\ast$, how many hom-sets are there? What does composition $\mathcal{C}(\ast,\ast) \times \mathcal{C}(\ast,\ast) \to \mathcal{C}(\ast,\ast)$ become?

> [!note]- Hint 2
> Map the category axioms to monoid axioms: associativity ↔ associativity, identity morphism ↔ identity element. Check both are forced.

> [!note]- Hint 3
> A one-object category is a [[Def - Groupoid|groupoid]] exactly when every morphism is invertible. What does that say about the monoid?

---

# Solution

The proof is a two-way dictionary. We send a monoid to a one-object category by making elements into endo-morphisms, and conversely read a monoid off any one-object category. The single object forces composition to be total, which is precisely what turns the partial composition of a general category into the total operation of a monoid.

**Step 1: From a monoid $M$ to a category $\mathbf{B}M$.**

> [!note]- Derivation
> Define $\mathbf{B}M$ with one object $\ast$, hom-set $\mathbf{B}M(\ast, \ast) := M$, composition $g \circ f := g \cdot f$ (the monoid product), and identity $1_\ast := e$. Check the [[Def - Category|category]] axioms. Associativity: $(h \circ g) \circ f = (h \cdot g) \cdot f = h \cdot (g \cdot f) = h \circ (g \circ f)$, which is monoid associativity. Identity: $1_\ast \circ f = e \cdot f = f$ and $f \circ 1_\ast = f \cdot e = f$, which is the monoid identity law. So $\mathbf{B}M$ is a category. (It is automatically small and locally small, since $M$ is a set.)

**Step 2: From a one-object category $\mathcal{C}$ to a monoid.**

> [!note]- Derivation
> Let $\mathcal{C}$ have one object $\ast$. The only hom-set is $M := \mathcal{C}(\ast, \ast)$, and composition restricts to a *total* operation $M \times M \to M$ (every pair is composable because every morphism has domain and codomain $\ast$). This operation is associative by the category's associativity axiom. The identity morphism $1_\ast \in M$ satisfies $1_\ast \circ f = f = f \circ 1_\ast$ for all $f \in M$, i.e. it is a two-sided identity element. So $(M, \circ, 1_\ast)$ is a monoid. The two constructions are mutually inverse: starting from $M$, building $\mathbf{B}M$, and reading off its endomorphism monoid returns $M$ on the nose.

**Step 3: Groupoids and [[Def - Group|groups]].**

> [!note]- Derivation
> A one-object category $\mathbf{B}M$ is a [[Def - Groupoid|groupoid]] iff every morphism is an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]], i.e. iff every element of $M$ has a two-sided inverse under $\cdot$. That is exactly the condition that the monoid $M$ is a [[Def - Group|group]]. So: **one-object categories ↔ monoids, and one-object groupoids ↔ groups.** This recovers the slogan "a group is a one-object groupoid" and "a category is a many-object monoid".

> [!note]- Complete formal solution
> *(Monoid → category.)* For a monoid $(M, \cdot, e)$ define $\mathbf{B}M$: one object $\ast$; $\mathbf{B}M(\ast,\ast) = M$; $g \circ f = g \cdot f$; $1_\ast = e$. Associativity and the unit law for $\mathbf{B}M$ are literally those of $M$, so $\mathbf{B}M$ is a category.
>
> *(Category → monoid.)* If $\mathcal{C}$ has one object $\ast$, set $M = \mathcal{C}(\ast,\ast)$ with operation $\circ$ and identity $1_\ast$. Every pair composes (all morphisms are endo-morphisms of $\ast$), composition is associative, and $1_\ast$ is a two-sided unit; so $M$ is a monoid. The assignments are mutually inverse.
>
> *(Groupoids.)* $\mathbf{B}M$ is a groupoid iff every $m \in M$ is invertible, iff $M$ is a group. $\blacksquare$

---

# Key Takeaways

**Collapsing objects degenerates a category into an algebraic structure.** The deepest single takeaway is the dial: a category has objects (typing composition) and morphisms (the things composed); turning the number of objects down to one removes the typing and leaves a pure binary operation — a monoid. Turning it down to one *and* requiring invertibility leaves a group. This "number of objects" dial is the right way to see monoids, groups, and (with the other dial, "at most one arrow per pair") preorders as the same kind of object viewed at different settings. Whenever you meet a structure with a single associative operation and a unit, you should immediately picture it as endomorphisms of a single dot, because that picture makes functorial and representation-theoretic constructions available.

**Functors out of $\mathbf{B}M$ are representations and actions.** This identification is the launch pad for a recurring trigger: a [[Def - Functor|functor]] $\mathbf{B}G \to \mathbf{Set}$ is a [[Def - Group Action|group action]], and a functor $\mathbf{B}G \to \mathbf{Vect}_k$ is a linear representation. Once a monoid or group is a one-object category, "act on something" becomes "functor into the category of those somethings", and "equivariant map / intertwiner" becomes "natural transformation". So this elementary exercise is what makes the entire categorical reformulation of representation theory possible; recognizing $\mathbf{B}G$ in the wild is the cue to bring functor-categorical tools to bear on a group action.

**The slogan "a category is a many-object monoid" is literally true.** It is worth internalizing that the category axioms are not loosely analogous to the monoid axioms — they *are* the monoid axioms, with the single modification that composition is partial because morphisms carry types. This makes the leap to categories feel small: you already know monoids, and a category is what you get by letting the multiplication be defined only when the types match. Carrying this view removes the mystique from "abstract nonsense" and lets you reason about composition with the same confidence you have about multiplying monoid elements.

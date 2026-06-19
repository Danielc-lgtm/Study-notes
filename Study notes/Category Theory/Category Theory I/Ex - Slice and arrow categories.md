---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Category"
  - "Def - Commutative Diagram"
tags: [category-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a [[Def - Category|category]] and $A$ an object. Construct two new categories and verify the category axioms for each:

1. The **slice category** $\mathcal{C}/A$ (objects "over $A$"): objects are morphisms $f : X \to A$ of $\mathcal{C}$ with codomain $A$; a morphism from $f : X \to A$ to $g : Y \to A$ is a morphism $h : X \to Y$ of $\mathcal{C}$ making the triangle commute, $g \circ h = f$.

2. The **arrow category** $\mathcal{C}^{\to}$ (morphisms as objects): objects are all morphisms $f : X \to Y$ of $\mathcal{C}$; a morphism from $f : X \to Y$ to $f' : X' \to Y'$ is a pair $(a, b)$ with $a : X \to X'$, $b : Y \to Y'$ making the square commute, $f' \circ a = b \circ f$.

Show that $\mathcal{C}^{\to}$ is the [[Def - Functor Category|functor category]] $[\mathbf{2}, \mathcal{C}]$, where $\mathbf{2}$ is the [[Def - Category|walking arrow]].

**Recall:**

A [[Def - Commutative Diagram|commutative triangle]] $g \circ h = f$ and a [[Def - Commutative Diagram|commutative square]] $f' \circ a = b \circ f$. The walking arrow $\mathbf{2}$ has two objects $0, 1$ and one non-identity morphism $0 \to 1$.

---

# Convergent Strategy

**Problem class:** This is a "build a new category from an old one and verify the axioms" construction — the bread-and-butter of producing examples. The route is to specify objects, morphisms, composition, and identities, then check associativity and the unit laws *reduce to those of $\mathcal{C}$*.

**Assumption pattern:** Both constructions inherit composition from $\mathcal{C}$, so the new categories' axioms are not proved from scratch; they are *pulled back* from $\mathcal{C}$. The only genuine content is checking that composing two commuting triangles (or squares) yields a commuting triangle (or square) — i.e. that the morphisms are closed under composition.

**Theorem routing:** No external theorem; the verification is direct [[Def - Commutative Diagram|diagram chasing]]. The identification $\mathcal{C}^{\to} = [\mathbf{2}, \mathcal{C}]$ routes through the definition of a [[Def - Functor Category|functor category]]: a functor $\mathbf{2} \to \mathcal{C}$ is an arrow of $\mathcal{C}$, and a natural transformation between two such is a commuting square.

**Key decision point:** The non-obvious step is realizing that the *composite of two morphisms in the slice category is just their composite in $\mathcal{C}$*, and that the commuting condition is automatically preserved — the new structure adds a constraint, not new composition data. Recognizing "same composition, extra constraint" is what makes the axiom-checking short.

---

# Legal Operations Used

1. **Operation: construct a category by specifying objects/morphisms and inheriting composition** (topic page, Legal Operation 1). Both $\mathcal{C}/A$ and $\mathcal{C}^{\to}$ reuse $\mathcal{C}$'s composition, so axioms transfer.

2. **Operation: paste commuting diagrams** (topic page, Legal Operation 6). Closure under composition is exactly "two commuting triangles paste into one", a diagram chase.

3. **Operation: recognize a category as a functor category** (topic page, Legal Operation 7). $\mathcal{C}^{\to} = [\mathbf{2}, \mathcal{C}]$ identifies the arrow category as functors out of the walking arrow.

---

# Hints

> [!note]- Hint 1
> For the slice category, a morphism is a morphism of $\mathcal{C}$ *plus a commuting condition*. Composition is composition in $\mathcal{C}$; you only need to check the composite still commutes.

> [!note]- Hint 2
> To compose $h : f \to g$ and $k : g \to p$ in $\mathcal{C}/A$ (so $g h = f$, $p k = g$), is $k \circ h$ a morphism $f \to p$? Compute $p \circ (k \circ h)$.

> [!note]- Hint 3
> For $\mathcal{C}^{\to} = [\mathbf{2}, \mathcal{C}]$: a functor $\mathbf{2} \to \mathcal{C}$ picks objects $F0, F1$ and a morphism $F0 \to F1$ — that *is* an arrow of $\mathcal{C}$. A natural transformation between two such functors has two components and one naturality square — that *is* a commuting square.

---

# Solution

The plan: verify $\mathcal{C}/A$ is a category by inheriting composition from $\mathcal{C}$ and checking commuting triangles paste; do the same for $\mathcal{C}^{\to}$ with commuting squares; then identify $\mathcal{C}^{\to}$ with $[\mathbf{2}, \mathcal{C}]$ by matching functors-out-of-$\mathbf{2}$ with arrows and natural-transformations with commuting squares.

**Step 1: $\mathcal{C}/A$ is a category.**

> [!note]- Derivation
> *Composition.* Let $h : (f : X \to A) \to (g : Y \to A)$ and $k : (g : Y \to A) \to (p : Z \to A)$, so $g \circ h = f$ and $p \circ k = g$. Define their slice-composite to be $k \circ h : X \to Z$ in $\mathcal{C}$. It is a slice morphism $f \to p$ because
> $$p \circ (k \circ h) = (p \circ k) \circ h = g \circ h = f,$$
> so the triangle over $A$ commutes. *Identity.* The identity on $f : X \to A$ is $1_X$, which trivially satisfies $f \circ 1_X = f$. *Associativity and unit laws* hold because they hold for the underlying morphisms in $\mathcal{C}$ — slice composition *is* $\mathcal{C}$-composition, restricted to morphisms satisfying the commuting condition. Hence $\mathcal{C}/A$ is a category.

**Step 2: $\mathcal{C}^{\to}$ is a category.**

> [!note]- Derivation
> *Composition.* Let $(a, b) : f \to f'$ and $(a', b') : f' \to f''$, so $f' a = b f$ and $f'' a' = b' f'$. Define the composite $(a', b') \circ (a, b) := (a' \circ a,\ b' \circ b)$. It is a morphism $f \to f''$ because
> $$f'' \circ (a' a) = (f'' a') a = (b' f') a = b'(f' a) = b'(b f) = (b' b) f,$$
> so the outer square commutes (this is the pasting of two commuting squares). *Identity.* The identity on $f : X \to Y$ is $(1_X, 1_Y)$, which commutes trivially. *Associativity and unit laws* are inherited componentwise from $\mathcal{C}$. Hence $\mathcal{C}^{\to}$ is a category.

**Step 3: $\mathcal{C}^{\to} = [\mathbf{2}, \mathcal{C}]$.**

> [!note]- Derivation
> A [[Def - Functor|functor]] $F : \mathbf{2} \to \mathcal{C}$ is determined by two objects $F0, F1$ and the image of the unique non-identity arrow $0 \to 1$, which is a morphism $Ff : F0 \to F1$ in $\mathcal{C}$ (identities are forced). So functors $\mathbf{2} \to \mathcal{C}$ correspond exactly to morphisms of $\mathcal{C}$ — the objects of $\mathcal{C}^{\to}$.
>
> A [[Def - Natural Transformation|natural transformation]] $\alpha : F \Rightarrow F'$ between two such functors has components $\alpha_0 : F0 \to F'0$ and $\alpha_1 : F1 \to F'1$, and the single naturality square (for the arrow $0 \to 1$) is
> $$F'f \circ \alpha_0 = \alpha_1 \circ Ff,$$
> which is exactly the commuting-square condition defining a morphism $(\alpha_0, \alpha_1) : Ff \to F'f$ in $\mathcal{C}^{\to}$. Vertical composition of natural transformations is componentwise, matching the componentwise composition in $\mathcal{C}^{\to}$. So the two categories have the same objects, the same morphisms, and the same composition: $\mathcal{C}^{\to} = [\mathbf{2}, \mathcal{C}]$.

> [!note]- Complete formal solution
> *Slice $\mathcal{C}/A$:* objects = morphisms into $A$; a morphism $f \to g$ is $h$ with $gh = f$; composition and identities are those of $\mathcal{C}$; closure under composition is $p(kh) = (pk)h = gh = f$; axioms inherited from $\mathcal{C}$.
>
> *Arrow $\mathcal{C}^{\to}$:* objects = morphisms of $\mathcal{C}$; a morphism $f \to f'$ is $(a,b)$ with $f'a = bf$; composition componentwise; closure is the square-pasting $f''(a'a) = (b'b)f$; axioms inherited componentwise.
>
> *Identification:* functors $\mathbf{2} \to \mathcal{C}$ = arrows of $\mathcal{C}$; natural transformations = commuting squares; hence $\mathcal{C}^{\to} = [\mathbf{2}, \mathcal{C}]$. $\blacksquare$

---

# Key Takeaways

**New categories are cheap: inherit composition, add a commuting constraint.** The reusable technique is that an enormous family of categories — slice, coslice, arrow, comma, categories of cones — are built by taking certain *diagrams* in $\mathcal{C}$ as objects and *commuting diagrams* between them as morphisms, with composition always inherited from $\mathcal{C}$. The axiom verification is therefore never hard: associativity and units come for free from $\mathcal{C}$, and the only real check is that the commuting condition is closed under composition (two commuting cells paste into one). Recognizing this pattern lets you construct and trust new categories instantly instead of re-proving the axioms each time.

**Slice categories are the categorical setting for "families and bundles".** The slice $\mathcal{C}/A$ is how one studies "objects living over $A$" — in topology, $\mathbf{Top}/A$ is the category of spaces mapping to $A$, i.e. bundles over $A$; in [[Def - Functor|geometry]], $\mathbf{Sch}/S$ is schemes over a base $S$, the home of relative algebraic geometry. The slice is also where the local structure of a [[Def - Limit and Colimit|limit]] is computed: a terminal object of $\mathcal{C}/A$ is the identity on $A$, and pullbacks in $\mathcal{C}$ are products in a slice. Whenever a problem says "over a fixed base", the slice category is the right ambient category, and this exercise is the proof it is well-defined.

**The arrow category is the first functor category, and it foreshadows everything.** Identifying $\mathcal{C}^{\to} = [\mathbf{2}, \mathcal{C}]$ is the cleanest first instance of the principle that "diagrams of a fixed shape form a functor category". The shape here is the walking arrow $\mathbf{2}$; replacing it by other small categories $\mathcal{J}$ gives the diagram categories $[\mathcal{J}, \mathcal{C}]$ in which all [[Def - Limit and Colimit|limits and colimits]] are defined. Internalizing that "an arrow of $\mathcal{C}$ = a functor out of $\mathbf{2}$" and "a commuting square = a natural transformation" trains the reflex of seeing diagrams as functors, which is the conceptual key to the entire theory of limits.

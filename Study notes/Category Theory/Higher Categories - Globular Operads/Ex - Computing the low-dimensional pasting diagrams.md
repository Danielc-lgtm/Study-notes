---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - The Free Strict ω-Category Monad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Using the recursive description of the globular set of pasting diagrams $\mathrm{pd} = T1$, where $T$ is the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]]:

(a) Determine $\mathrm{pd}(0)$ and show $\mathrm{pd}(1)$ is in bijection with $\mathbb{N}$.

(b) List the structure of $\mathrm{pd}(2)$ via the recursion and write the $2$-pasting diagram "three $2$-cells stacked vertically over a string of three $1$-cells" as an explicit nested sequence.

(c) Compute the boundary $\partial : \mathrm{pd}(2) \to \mathrm{pd}(1)$ on the diagram from (b).

**Recall:**

The **free strict $\omega$-category monad** $T$ acts on **globular sets** (sequences $X(0), X(1), \dots$ of cells with source/target $s, t : X(n+1) \to X(n)$ satisfying $ss = ts$, $st = tt$). Applied to the terminal globular set $1$ (one cell in each dimension), it produces the globular set of **pasting diagrams** $T1 = \mathrm{pd}$, described recursively by
$$
\mathrm{pd}(0) = 1, \qquad \mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast},
$$
where $(-)^{\ast}$ is the **free-monoid functor** sending a set $A$ to the set $A^{\ast}$ of finite sequences (words) over $A$. Because all cells of $1$ are endomorphisms (source $=$ target), the same holds in $\mathrm{pd}$, so the source and target maps coincide and are written $\partial : \mathrm{pd}(m+1) \to \mathrm{pd}(m)$, the **boundary**, defined inductively from the dimension below. An element of $\mathrm{pd}(m)$ is an $m$-dimensional pasting diagram — the *shape* of a formal $m$-fold composite.

---

# Convergent Strategy

**Problem class:** This is a direct-computation exercise of the kind described in the topic page's problem-solving strategy under "justify the operad framework itself" — here, making the operations of $T$ concrete. The whole task is to take an abstract recursion and *evaluate* it in low dimensions, producing explicit combinatorial objects (finite sequences) and tracking how the boundary acts. No theorem is invoked; the recursion *is* the tool.

**Assumption pattern:** The only assumption is the recursion $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$ together with $\mathrm{pd}(0) = 1$. The presence of the free-monoid functor $(-)^{\ast}$ is the signal that elements of dimension $m+1$ are *finite lists* of dimension-$m$ data; recognizing "$(-)^{\ast}$ means finite sequence" is what unlocks the computation. The terminality of $1$ is what makes source $=$ target, collapsing $s, t$ into a single boundary $\partial$.

**Theorem routing:** No theorem is needed; the route is purely "apply the recursion of [[Def - The Free Strict ω-Category Monad|the free strict ω-category monad]] twice". For the boundary, route through the inductive definition: $\partial$ in dimension $m+1$ is built from $\partial$ in dimension $m$ applied entrywise to the sequence.

**Key decision point:** The non-obvious choice is how to *encode* a $2$-pasting diagram as a nested sequence, because the geometric picture (globes stacked and side-by-side) must be translated into the formal "list of lists of points" given by the recursion. The natural alternative — drawing pictures and stopping — fails to make the boundary computable; the formal encoding is what lets $\partial$ be computed mechanically rather than read off a figure.

---

# Legal Operations Used

1. **Operation 1 from the topic page (encode structure as operations over $T1$), in its rawest form.** Here we are computing $T1$ itself, the universe of shapes; every later operad lives over this object, so knowing it concretely is the foundation.

2. **Operation 2 from the topic page (use the structure of $T$).** We use the explicit recursion $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$ — the concrete face of $T$ — rather than the abstract monadicity, to evaluate the fibres dimension by dimension.

---

# Hints

> [!note]- Hint 1
> Start at the bottom. What is the free monoid on a one-element set? That is $\mathrm{pd}(1) = \mathrm{pd}(0)^{\ast} = 1^{\ast}$.

> [!note]- Hint 2
> A finite sequence over a one-element set is determined by its *length*. So an element of $1^{\ast}$ is just a natural number — the number of $1$-cells strung together.

> [!note]- Hint 3
> For $\mathrm{pd}(2) = \mathrm{pd}(1)^{\ast}$, an element is a finite sequence of elements of $\mathrm{pd}(1)$, i.e. a finite sequence of natural numbers. The $i$-th entry says how many $1$-cells underlie the $i$-th $2$-cell in the vertical stack.

> [!note]- Hint 4
> The boundary $\partial : \mathrm{pd}(2) \to \mathrm{pd}(1)$ forgets the vertical stacking and remembers the underlying string of $1$-cells. For a sequence of $2$-cells stacked vertically, the underlying $1$-dimensional shape is the common source/target string — its *length* is what survives.

---

# Solution

The solution is three applications of the recursion. Step 1 evaluates dimensions $0$ and $1$, finding $\mathrm{pd}(1) \cong \mathbb{N}$. Step 2 evaluates dimension $2$ as sequences of naturals and encodes the requested diagram. Step 3 computes the boundary by passing from a sequence-of-naturals to the underlying string length. The one subtlety is the encoding in Step 2, where the geometric stack becomes a nested list.

**Step 1: $\mathrm{pd}(0)$ is a point and $\mathrm{pd}(1) \cong \mathbb{N}$.**

> [!note]- Derivation
> By definition $\mathrm{pd}(0) = 1$, a one-element set; write its unique element as $\bullet$. Then
> $$
> \mathrm{pd}(1) = \mathrm{pd}(0)^{\ast} = 1^{\ast} = \{ (\,), (\bullet), (\bullet,\bullet), (\bullet,\bullet,\bullet), \dots \},
> $$
> the set of finite sequences over a one-element set. Such a sequence is determined entirely by its length, so $\mathrm{pd}(1) \cong \mathbb{N}$ via "sequence $\mapsto$ length". Geometrically the length-$k$ sequence is the shape "$k$ composable $1$-cells in a row", $\bullet \to \bullet \to \cdots \to \bullet$ with $k$ arrows; length $0$ is a single point (a degenerate $1$-pasting diagram, i.e. an identity).

**Step 2: $\mathrm{pd}(2)$ consists of finite sequences of natural numbers; encode the given diagram.**

> [!note]- Derivation
> By the recursion,
> $$
> \mathrm{pd}(2) = \mathrm{pd}(1)^{\ast} \cong \mathbb{N}^{\ast},
> $$
> the set of finite sequences $(k_1, k_2, \dots, k_r)$ of natural numbers. The interpretation: $r$ is the number of $2$-cells stacked vertically, and $k_i$ is the number of $1$-cells underlying the $i$-th $2$-cell (the length of its source/target string).
>
> The requested diagram is "three $2$-cells stacked vertically over a string of three $1$-cells". So $r = 3$ (three $2$-cells in the vertical stack), and each underlying string has length $3$ (three $1$-cells), giving $k_1 = k_2 = k_3 = 3$. Hence the diagram is the sequence
> $$
> \big(3, 3, 3\big) \in \mathbb{N}^{\ast} \cong \mathrm{pd}(2).
> $$
> Spelled all the way down to points, each "$3$" is the $1$-pasting diagram $(\bullet, \bullet, \bullet) \in 1^{\ast}$, so the fully-nested form is
> $$
> \Big( (\bullet,\bullet,\bullet),\ (\bullet,\bullet,\bullet),\ (\bullet,\bullet,\bullet) \Big) \in (1^{\ast})^{\ast} = \mathrm{pd}(2).
> $$

**Step 3: the boundary forgets the vertical stack.**

> [!note]- Derivation
> The boundary $\partial : \mathrm{pd}(2) \to \mathrm{pd}(1)$ sends a $2$-pasting diagram to its underlying $1$-pasting diagram — the common source (equivalently target) string, the string of $1$-cells along the top/bottom of the stack. A vertical stack of $2$-cells all sit over the *same* string of $1$-cells, so the boundary is that string. For $(3,3,3)$ the underlying string has length $3$, so
> $$
> \partial\big((3,3,3)\big) = 3 \in \mathbb{N} \cong \mathrm{pd}(1),
> $$
> i.e. the $1$-pasting diagram $(\bullet,\bullet,\bullet) = \bullet \to \bullet \to \bullet \to \bullet$. (The boundary does not depend on $r$, the number of $2$-cells stacked — stacking is vertical composition, which is invisible to the $1$-dimensional boundary.)

> [!note]- Complete formal solution
> By definition $\mathrm{pd}(0) = 1 = \{\bullet\}$. Applying the recursion $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$:
> $$
> \mathrm{pd}(1) = 1^{\ast} \cong \mathbb{N} \quad (\text{sequence}\mapsto\text{length}), \qquad \mathrm{pd}(2) = \mathrm{pd}(1)^{\ast} \cong \mathbb{N}^{\ast}.
> $$
> An element $(k_1, \dots, k_r) \in \mathbb{N}^{\ast}$ encodes a vertical stack of $r$ two-cells, the $i$-th over a string of $k_i$ one-cells. "Three $2$-cells over three $1$-cells" is therefore $(3,3,3)$, fully nested as $\big((\bullet,\bullet,\bullet),(\bullet,\bullet,\bullet),(\bullet,\bullet,\bullet)\big) \in (1^{\ast})^{\ast}$. The boundary $\partial : \mathrm{pd}(2) \to \mathrm{pd}(1)$ returns the underlying $1$-string, so $\partial((3,3,3)) = 3 \in \mathbb{N} \cong \mathrm{pd}(1)$, the shape $\bullet\to\bullet\to\bullet\to\bullet$. $\blacksquare$

---

# Key Takeaways

**The free-monoid functor turns "one dimension up" into "a finite list".** The single most reusable fact this exercise installs is that the recursion $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$ means *an $(m+1)$-pasting diagram is a finite sequence of $m$-pasting diagrams*. Every time you need to understand a globular pasting diagram in a given dimension, descend one dimension and take finite lists; iterate to the bottom and you reach lists-of-lists-of-...-of-points. This is why pasting diagrams are entirely combinatorial objects despite their geometric appearance, and it is the concrete reason the free-strict-$\omega$-category monad is *cartesian* — it is assembled out of the free-monoid monad, which is cartesian, applied dimension by dimension. Whenever a proof about $T$ stalls at the abstract level, drop to this list description and the obstruction usually dissolves.

**The boundary forgets composition in the top dimension and remembers the shape below.** Computing $\partial$ here teaches the general principle: the boundary of an $(m+1)$-pasting diagram is its underlying $m$-pasting diagram, obtained by forgetting how the top-dimensional cells are pasted and keeping the common source/target shape. A vertical stack of $2$-cells has the same boundary regardless of how many cells are stacked, because vertical composition is invisible one dimension down. This "boundary forgets the top, keeps the floor below" pattern recurs throughout the chapter — it is exactly what the contraction exploits, lifting parallel pairs *in the boundary* to cells *in the full diagram*. Recognizing that two seemingly different top-dimensional composites share a boundary is the trigger for "these are a parallel pair; a contraction will relate them".

**Concrete low-dimensional computation is the antidote to abstraction in higher category theory.** This exercise is deliberately at the ⭐ level because the habit it builds — actually evaluating $\mathrm{pd}(0), \mathrm{pd}(1), \mathrm{pd}(2)$ rather than reasoning about them abstractly — is the single most effective way to demystify the whole apparatus of globular operads. The same habit, applied later, lets you compute that $L_2$ is tree-generated and that its algebras are bicategories. Whenever the definitions feel impossibly abstract, the move is to pick the smallest non-trivial dimension and write out the actual finite sets; the structure that looked forbidding becomes a list of natural numbers. See [[Ex - Pasting diagrams as labelled composites]] for the labelled version, where the same combinatorics carries data from a general globular set.

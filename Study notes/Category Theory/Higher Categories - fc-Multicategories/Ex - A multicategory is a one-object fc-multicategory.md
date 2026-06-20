---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - fc-Multicategory"
  - "Def - Multicategory"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Show that an [[Def - fc-Multicategory|fc-multicategory]] with exactly one object and only the identity vertical $1$-cell is the same thing as an ordinary [[Def - Multicategory|multicategory]]. Precisely: exhibit a bijection between (i) fc-multicategories $\mathcal{C}$ with one object $\ast$ and $\mathrm{Hom}_{\mathrm{vert}}(\ast,\ast) = \{1_\ast\}$, and (ii) multicategories $\mathcal{M}$, under which the horizontal $1$-cells of $\mathcal{C}$ become the objects ("colours") of $\mathcal{M}$, a $2$-cell $\theta : (m_1, \dots, m_n) \Rightarrow p$ becomes a multimap $(m_1, \dots, m_n) \to p$, and substitution of $2$-cells becomes multicategory composition.

**Recall:**

![[Def - fc-Multicategory#The Definition]]

A **[[Def - Multicategory|multicategory]]** (or coloured operad) $\mathcal{M}$ has a class of objects (colours), and for each finite list of input colours $(a_1, \dots, a_n)$ and output colour $b$ a set of **multimaps** $\mathcal{M}(a_1, \dots, a_n; b)$; there is a composition substituting multimaps into the inputs of a multimap, and an identity multimap $1_a \in \mathcal{M}(a; a)$ for each colour, satisfying associativity and unit laws. A [[Def - Category|category]] is the special case where all input lists have length one.

---

# Convergent Strategy

**Problem class:** This is a *template-identification* problem in the sense of the topic page's problem-solving strategy: take a concrete structure (here, "fc-multicategory with the dials set to one object and trivial vertical structure") and match it to a classical structure (a multicategory). The routine is to set the four dials and read off what survives.

**Assumption pattern:** The two assumptions — *one object* and *trivial vertical structure* — are exactly the dials that collapse the four-layer fc-multicategory down to two layers. One object means there is nothing for the horizontal $1$-cells to connect *between*, so they become a bare class of "types". Trivial vertical structure means the side-boundaries of every $2$-cell are forced to be identities, so a $2$-cell carries no boundary data — it is just a map from a string to a single cell. What survives is precisely the data of a multicategory.

**Theorem routing:** This is the one-object, vertically-trivial, *non-representability-required* case of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories|the four-dial subsumption theorem]]: that theorem states multicategories are exactly the one-object vertically-trivial fc-multicategories. The exercise is to verify the correspondence by hand at the level of data, rather than to cite the theorem.

**Key decision point:** The non-obvious choice is to keep *all* string lengths $n \geq 0$, including the empty string. A multicategory genuinely has nullary multimaps $(\,) \to b$ ("constants"), which correspond to the length-zero $2$-cells; dropping them would give only the "non-unital" part. The temptation is to think a multicategory only has unary-and-higher operations, but the fc-multicategory's $n=0$ layer is exactly the nullary multimaps, and matching them is what makes the bijection exact.

---

# Legal Operations Used

1. **Operation 1 from the topic page (set the four dials).** We are handed the dials "one object" and "trivial vertical structure"; the task is to read off the collapsed structure.

2. **Operation 8 from the topic page (use the empty string for units/nullary data).** The length-zero string is matched with nullary multimaps, ensuring the correspondence is a bijection and not merely an injection on the positive-arity part.

---

# Hints

> [!note]- Hint 1
> Strip the fc-multicategory of the two pieces the hypotheses trivialise. With one object, "source" and "target" of a horizontal $1$-cell carry no information. With only identity vertical $1$-cells, the left and right boundaries of a $2$-cell are forced. What data is left in a $2$-cell?

> [!note]- Hint 2
> A $2$-cell $\theta : (m_1, \dots, m_n) \Rightarrow p$ with both boundaries equal to $1_\ast$ is *just* the assignment of an output $p$ to an input string $(m_1, \dots, m_n)$. Compare this with the data $\mathcal{M}(m_1, \dots, m_n; p)$ of a multimap. Now match substitution with composition.

> [!note]- Hint 3
> Substitution in the fc-multicategory concatenates strings $S_1 \cdots S_n$ and uses $\mathrm{fc}$'s multiplication; multicategory composition substitutes into input slots. Check the two associativity laws coincide and that $1_m$ corresponds to $1_a$. Do not forget $n = 0$.

---

# Solution

The proof is a direct unpacking. We show the data of a one-object, vertically-trivial fc-multicategory is *literally* the data of a multicategory, layer by layer, and that the axioms coincide.

**Step 1: With one object and trivial vertical structure, horizontal $1$-cells are an unstructured class.**

> [!note]- Derivation
> An [[Def - fc-Multicategory|fc-multicategory]] has objects, vertical $1$-cells, horizontal $1$-cells, and $2$-cells. By hypothesis there is one object $\ast$ and the only vertical $1$-cell is $1_\ast$. A horizontal $1$-cell $m : A \nrightarrow B$ must have $A = B = \ast$, so it is simply an element of the class $H := \{\text{horizontal } 1\text{-cells } \ast \nrightarrow \ast\}$, with no source/target data distinguishing them. Declare these to be the **colours** (objects) of the multicategory $\mathcal{M}$: $\mathrm{ob}(\mathcal{M}) := H$.

**Step 2: A $2$-cell is exactly a multimap.**

> [!note]- Derivation
> A $2$-cell $\theta : (m_1, \dots, m_n) \Rightarrow p$ has left boundary $f$ and right boundary $g$, which here must both be $1_\ast$. So the only data in $\theta$ are the input string $(m_1, \dots, m_n)$ (a list of colours), the output $p$ (a colour), and $\theta$ itself. Define
> $$\mathcal{M}(m_1, \dots, m_n;\, p) := \{\,2\text{-cells } (m_1, \dots, m_n) \Rightarrow p \text{ in } \mathcal{C}\,\}.$$
> This is exactly the set of multimaps with inputs $m_1, \dots, m_n$ and output $p$. For $n = 0$ we get the nullary multimaps $\mathcal{M}(\,;\,p)$, matching the empty-string $2$-cells.

**Step 3: Substitution of $2$-cells is multicategory composition; identities match.**

> [!note]- Derivation
> Multicategory composition takes a multimap $\theta : (m_1, \dots, m_n) \to p$ and multimaps $\theta_i : S_i \to m_i$ (with $S_i$ a list) and produces a multimap $S_1 \cdots S_n \to p$ by substituting $\theta_i$ into the $i$-th input. This is *exactly* the fc-multicategory substitution $\theta \cdot (\theta_1, \dots, \theta_n)$, whose top is the concatenated string $S_1 \cdots S_n$ (the action of $\mathrm{fc}$'s multiplication $\mu$, path-of-paths to path) and whose bottom is $p$; the outer boundaries are $1_\ast \circ 1_\ast = 1_\ast$, carrying no data. The identity $2$-cell $1_m : (m) \Rightarrow m$ becomes the identity multimap $1_m \in \mathcal{M}(m; m)$. Associativity of substitution (concatenation is strictly associative) is associativity of multicategory composition; the unit laws coincide. Hence the data and axioms match on the nose, giving a bijection between the two classes of structures.

> [!note]- Complete formal solution
> Let $\mathcal{C}$ be an fc-multicategory with one object $\ast$ and only the identity vertical $1$-cell. Define a multicategory $\mathcal{M}$ by: colours $\mathrm{ob}(\mathcal{M}) = \{$horizontal $1$-cells $\ast\nrightarrow\ast\}$; for colours $m_1, \dots, m_n, p$, multimaps $\mathcal{M}(m_1,\dots,m_n; p) = \{2\text{-cells } (m_1,\dots,m_n)\Rightarrow p\}$; composition $=$ fc-multicategory substitution (whose top is the concatenated string by $\mathrm{fc}$'s $\mu$); identities $1_m$ $=$ the identity $2$-cells. Since both boundaries of every $2$-cell are forced to be $1_\ast$, no information is lost or added. The fc-multicategory associativity (associativity of string concatenation) and unit laws are precisely the multicategory associativity and unit laws. Conversely, any multicategory $\mathcal{M}$ yields such an fc-multicategory by reversing each clause: one object $\ast$, only $1_\ast$ vertically, horizontal $1$-cells $=$ colours, $2$-cells $=$ multimaps, substitution $=$ composition. The two assignments are mutually inverse, establishing the bijection. In particular, the empty-string $2$-cells correspond exactly to nullary multimaps, so the bijection is exact including arity zero. $\blacksquare$

---

# Key Takeaways

**Setting dials is the whole game in this chapter.** The exercise is the cleanest instance of the topic's central technique: a higher structure is recognised by collapsing the general fc-multicategory along chosen dials. Here the dials "one object" and "trivial vertical structure" remove two of the four layers, and the remaining two layers — horizontal $1$-cells and string-topped $2$-cells — are *exactly* the colours and multimaps of a multicategory. The transferable diagnostic is: whenever you are asked "show X is a [classical structure]", do not verify the classical axioms directly; instead express X as an fc-multicategory and read which dials are set, because the classical axioms are then automatic from the fc-multicategory axioms.

**The string-topped $2$-cell *is* the multimap, and that is why $\mathrm{fc}$ is the right monad.** A multimap takes a *list* of inputs to one output; an fc-multicategory $2$-cell takes a *string* of horizontal $1$-cells to one. The free-category monad $\mathrm{fc}$ is precisely the device that turns "edges" into "paths" (lists), so feeding $\mathrm{fc}$ into the generalized-multicategory recipe produces exactly the list-input structure of a multicategory. The trigger to remember: "list of inputs" $\leftrightarrow$ "string on top" $\leftrightarrow$ "free-path monad". This is the same move that, one dimension down, turns the free-monoid monad on $\mathbf{Set}$ into ordinary multicategories — the analogy "multicategory is to category as fc-multicategory is to double category" is this correspondence read at two levels.

**Never drop the empty string.** The subtle point that makes the correspondence a *bijection* rather than a near-miss is the length-zero layer: nullary multimaps $(\,)\to b$ match the empty-string $2$-cells. It is easy to think of operations as having at least one input, but constants, units, and points are nullary operations, and the fc-multicategory's $n=0$ layer is built to hold them. The general lesson, recurring throughout the chapter, is that units and nullary data live in the empty-string layer; any correspondence that ignores $n=0$ will silently lose unit objects, identity arrows, or constants. See [[Ex - A monoidal category as a one-object fc-multicategory]], where the empty string is the monoidal unit $I$.

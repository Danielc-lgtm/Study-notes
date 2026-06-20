---
type: definition
subject: higher-categories
prereqs:
  - "Def - Presheaf"
  - "Thm - The Yoneda Lemma"
  - "Def - Initial and Terminal Object"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, $C$ denotes a **multicategory**: a category-like structure whose arrows take a finite *list* of inputs to a single output. We write $\mathrm{ob}(C)$ for its set of objects, and $C(a_1, \dots, a_n;\, b)$ for the set of **multimaps** (also called operations or multimorphisms) with input list $a_1, \dots, a_n \in \mathrm{ob}(C)$ and output $b \in \mathrm{ob}(C)$; the number $n$ is the **arity**. Composition $\circ$ substitutes multimaps into the inputs of a multimap; each object $a$ has an identity multimap $1_a \in C(a; a)$. An **operad** is a one-object multicategory; the **identity operad** $I = 1$ is the terminal one. We write $C^+$ (read "$C$-plus") for the slice. For a generalized multicategory — a multicategory internal to a cartesian monad $(T, \eta, \mu)$ — the same construction applies verbatim, and the symbol $C^+$ is reused. The full symbol registry is on the parent page [[Higher Categories — Opetopes and Opetopic Sets]].

This definition relies on the convention, standing throughout the chapter, that "multicategory" means *non-symmetric* (plain): the inputs of a multimap carry a fixed linear order. This is what makes the pasting diagrams below into *planar* trees.

---

# Axiom Motivation

The slice construction answers a single question: **given a structure whose cells are "operations", how do I describe the next layer of cells — the operations between operations?** Everything below is forced by demanding a clean answer.

Start concretely. A multicategory $C$ has objects and operations. An operation $\phi \in C(a_1, \dots, a_n;\, b)$ is a one-step "many-in, one-out" thing: it takes the inputs $a_1, \dots, a_n$ to the output $b$. Now I want to talk about *how operations combine*. The basic way operations combine is **substitution**: if I have an operation $\psi$ with output $a_i$, I can plug it into the $i$-th input of $\phi$, and the result is a new operation. More generally I can plug an operation into *each* input of $\phi$ at once, and I can iterate, building a whole tree of substitutions. The result of any such tree is, after I carry out all the substitutions, a single operation of $C$. So a "pasting diagram of operations" is a configuration — a tree of operations of $C$ — together with the knowledge of which single operation of $C$ it composes to.

I want a new structure $C^+$ whose **objects are the operations of $C$** and whose **operations are exactly these pasting diagrams**. Why should the objects of $C^+$ be the operations of $C$? Because the whole point is to go up one dimension: the operations of $C$ are the $1$-dimensional cells from the standpoint of $C^+$, so they must become the *objects* of $C^+$ — the things that the new operations act between. And why should the operations of $C^+$ be the pasting diagrams? Because a pasting diagram takes *several operations of $C$* (the ones at its leaves) and produces *one operation of $C$* (the one it composes to at its root): it is itself a many-in, one-out thing, now one level up. The shape of the new operation is precisely "this configuration of old operations composes to that old operation."

Now I must pin down what "configuration of operations composing to one operation" means precisely, and here the genius of Baez and Dolan is to *not* invent ad hoc combinatorics but to characterise $C^+$ by a universal property phrased through its algebras. An **algebra** for a multicategory $D$ is an assignment of an object to each object of $D$ and an actual function to each operation, compatibly with composition — it is a "representation" of $D$. The defining requirement of the slice is:

$$\mathrm{Alg}(C^+) \;\simeq\; \mathbf{Multicat}_{\mathrm{ob}(C)} / C,$$

the algebras of $C^+$ are the multicategories living over $C$ (with the same object-set). This is the axiom, and it is the right one for two reasons. First, it is *representation-free*: it does not require me to choose a notion of "tree" by hand; it says "$C^+$ is the thing whose representations are exactly the multicategories-over-$C$", and that determines $C^+$ up to equivalence. Second, it makes the slice *functorial and iterable*: because "multicategory over $C$" is a clean categorical notion, the construction $C \mapsto C^+$ is well-behaved enough to apply again to $C^+$, which is the entire reason we can build an infinite tower.

What breaks if we weaken or alter this? If we tried to define $C^+$ by *only* listing single substitutions (depth-one trees) rather than arbitrary pasting diagrams, the construction would fail to be associative/iterable: a substitution of substitutions would have no home, and slicing twice would not match "pasting diagrams of pasting diagrams". If we dropped the over-$C$ condition and asked merely for "some multicategory whose objects are operations of $C$", the construction would be wildly underdetermined — there are many such, and only the universal one (algebras = multicategories over $C$) gives the opetopes. And if we worked with *symmetric* multicategories, the construction still works (it is Baez and Dolan's original) but produces a coarser shape category, because permuting inputs identifies pasting diagrams that the planar/non-symmetric version keeps distinct. The non-symmetric choice is what makes the operations of $C^+$ correspond bijectively to *planar* trees, which is the version that yields the clean opetopes of this chapter.

Finally, the reason the definition is stated for *generalized* multicategories (those internal to a cartesian monad $T$, as in the preceding chapter) rather than only plain ones: the iteration we want — $I, I^+, I^{++}, \dots$ — must stay inside a category where the relevant free constructions and pullbacks exist. Cartesian monads are exactly the setting where this holds, and where the slice of a generalized multicategory is again a generalized multicategory for a (new) cartesian monad. So the generalized setting is not abstraction for its own sake; it is the minimal habitat in which slicing can be repeated forever.

---

# The Definition

Let $C$ be a multicategory. The **slice** of $C$ is the multicategory $C^+$ specified as follows.

- **Objects of $C^+$** are the operations of $C$: an object of $C^+$ is a multimap $\phi \in C(a_1, \dots, a_n;\, b)$ for some objects $a_i, b$ and some arity $n$.

- **Operations of $C^+$** are the *pasting diagrams* of operations of $C$. A multimap of $C^+$ with inputs $\phi_1, \dots, \phi_k$ (operations of $C$) and output $\phi$ (an operation of $C$) is a way of arranging $\phi_1, \dots, \phi_k$ into a configuration — a tree, with the $\phi_j$ at the vertices — that composes, via the composition of $C$, to the operation $\phi$. Equivalently, it is a factorisation of $\phi$ as an iterated substitution of the $\phi_1, \dots, \phi_k$.

- **Composition in $C^+$** is the nesting of pasting diagrams: substituting one pasting diagram into a vertex of another, which on underlying operations of $C$ is just further substitution. **Identities** are the trivial (single-vertex) pasting diagrams.

This data is characterised, up to equivalence, by the universal property
$$\mathrm{Alg}(C^+) \;\simeq\; \mathbf{Multicat}_{\mathrm{ob}(C)} / C$$
— the category of algebras for $C^+$ is equivalent to the category of multicategories over $C$ with object-set $\mathrm{ob}(C)$, with morphisms the maps over $C$ fixing the objects.

When $C$ is a **generalized multicategory** internal to a cartesian monad $(T, \eta, \mu)$, the identical construction produces a generalized multicategory $C^+$ (internal to a derived cartesian monad), and the universal property holds in the generalized sense.

---

# Categorical / Structural Definition

The cleanest structural account is the algebra equivalence above, but it is worth recording the two-stage construction Baez and Dolan actually use, because it is what makes the universal property precise.

Stage one: **slice a multicategory by an algebra.** Given a multicategory $D$ and a $D$-algebra $X$, one builds a multicategory $D/X$ (Baez and Dolan write $X^+$ for it) whose algebras are the $D$-algebras *equipped with a map to* $X$:
$$\mathrm{Alg}(D/X) \;\simeq\; \mathrm{Alg}(D)/X.$$
This is the multicategorical analogue of the ordinary slice category $\mathcal{D}/X$, whose objects are arrows into $X$.

Stage two: **the multicategory whose algebras are multicategories on a fixed object-set.** For a set $S$, there is a multicategory — call it $\mathrm{Mti}_S$ — with the property
$$\mathrm{Alg}(\mathrm{Mti}_S) \;\simeq\; \mathbf{Multicat}_S,$$
the multicategories with object-set $S$ (and object-fixing maps). Its operations encode "the data of a multicategory structure"; this is the operad whose algebras *are multicategories*.

The slice of $C$ is then obtained by combining the two stages: $C$ is an algebra for $\mathrm{Mti}_{\mathrm{ob}(C)}$ (it *is* a multicategory on its object-set), so we may slice $\mathrm{Mti}_{\mathrm{ob}(C)}$ by the algebra $C$:
$$C^+ \;:=\; \mathrm{Mti}_{\mathrm{ob}(C)}\,/\,C, \qquad \text{whence} \qquad \mathrm{Alg}(C^+) \;\simeq\; \mathrm{Alg}(\mathrm{Mti}_{\mathrm{ob}(C)})/C \;\simeq\; \mathbf{Multicat}_{\mathrm{ob}(C)}/C.$$

Read structurally, the slice is the composite "make the operad-of-multicategory-structures, then slice it by the multicategory you care about". The objects of the result are the operations of $C$ and the operations of the result are the pasting diagrams, exactly as in the concrete description — the two-stage construction is what *proves* the concrete description matches the universal property.

---

# Relate to Other Fields / Compression

The slice construction is the multicategorical sibling of two familiar moves. It generalizes the ordinary **slice category** $\mathcal{D}/X$ (objects are arrows $A \to X$), which is the one-object, arity-one shadow of the algebra-slice $D/X$. And it is intimately tied to the **free multicategory** monad: the operations of $C^+$ are pasting diagrams, which are precisely the elements of the free multicategory built on the operations of $C$, so slicing repackages "free pasting" as a new multicategory one dimension up. Where an ordinary slice records "ways to map into a fixed object", the multicategory slice records "ways to compose into a fixed operation".

**True name:** the slice $C^+$ is *"the operations of $C$, with their pasting diagrams as the new operations" — it raises the dimension by one.* When you read $C^+$, do not picture the algebra equivalence; picture the operations of $C$ becoming objects, and the trees of operations becoming the new arrows.

There is a precise compression with the rest of higher category theory: slicing is to multicategories what the **bar construction** / **simplicial nerve** is to monoids and categories — a systematic way of recording "all the ways of composing" as new structure one level up, which can then be iterated. The difference is that slicing keeps the many-in, one-out shape native, whereas the simplicial nerve linearises everything into totally ordered chains.

---

# Examples / Corollaries

**Is an instance — slicing the identity operad once.** Take $C = I = 1$, the identity operad: one object, and exactly one operation in each arity $n$ (the "compose $n$ things in a row" operation, with nothing to choose). The objects of $I^+$ are the operations of $I$, i.e. one object for each arity $n = 0, 1, 2, \dots$ — these are the **arrows** counted by their valence, the cells that will become the $2$-opetopes. The operations of $I^+$ are the pasting diagrams of these, i.e. trees recording how arrows compose, which are the $3$-opetopes. So a single slice of the simplest possible operad already produces the infinite family of many-in, one-out 2-cells. This is the engine of [[Thm - Opetopes via Iterated Slicing of the Identity Operad|the iterated-slicing theorem]].

**Is an instance — slicing an ordinary category.** An ordinary category $\mathcal{D}$ is a multicategory all of whose operations have arity $1$ (only one-input arrows). Its slice $\mathcal{D}^+$ has as objects the arrows of $\mathcal{D}$, and as operations the composable strings of arrows that compose to a given arrow — i.e. factorisations. This is closely related to the **arrow category** and to the simplicial nerve's role of recording composable chains: the slice of a category is where "the ways to factor a morphism" live as a structure in their own right.

**Is an instance — the algebra equivalence as a sanity check.** For any $C$, an algebra of $C^+$ is the same as a multicategory $D \to C$ over $\mathrm{ob}(C)$. Take $C = I$: then a $C^+$-algebra is a multicategory over $I$ on a one-point object-set, which is just *a multicategory with one object*, i.e. an **operad**. So $\mathrm{Alg}(I^+) \simeq \{\text{operads}\}$ on the nose — a clean confirmation that slicing the identity operad produces the operad-of-operads.

**Is NOT an instance — the ordinary slice category is not the multicategory slice.** It is tempting to think $C^+$ is just the ordinary slice category $\mathcal{D}/X$ in disguise. It is not: the ordinary slice has objects = arrows into a *fixed* object $X$ and morphisms = commuting triangles, whereas $C^+$ has objects = *all* operations of $C$ (not into a fixed target) and operations = pasting diagrams (not triangles). The ordinary slice is the arity-one, fixed-target degeneration; the multicategory slice is genuinely richer because its operations are many-in, one-out trees. Confusing the two collapses every $2$-opetope to a triangle and destroys the chapter.

**Calibration check.** Verify three things. First, that the objects of $I^+$ are in bijection with the natural numbers (one $2$-opetope per arity). Second, that $\mathrm{Alg}(I^+)$ is the category of operads, by unwinding the algebra equivalence at $C = I$. Third, that slicing an ordinary category $\mathcal{D}$ (arity-one multicategory) gives a structure whose objects are arrows of $\mathcal{D}$ — and that its operations are the *factorisations* of arrows, not commuting triangles. If you can do these, you have understood that slicing raises the dimension by one and is not the ordinary slice category.

---

# Unlocked by This

> [!tip] Opetope *(from this chapter)*
> Iterating the slice on the identity operad $I = 1$ produces the [[Def - Opetope|opetopes]]: the $n$-opetopes are the objects of the $n$-fold slice. The slice is the *only* generator of new dimensions, so the entire opetope hierarchy is this one construction applied repeatedly.

> [!tip] Multitopes and the Hermida–Makkai–Power Definition *(from Higher Category Theory)*
> Reworking the slice in the language of "function-replacement" categories gives the **multitopic** sets of Hermida–Makkai–Power, whose shapes are **multitopes**. These are very close to opetopes, and **Cheng's comparison** results identify the two frameworks; the slice construction is the common root.

> [!tip] The Stabilization Hypothesis *(from Higher Category Theory)*
> Baez and Dolan built the slice precisely to have a uniform supply of cell-shapes in which to state the **stabilization hypothesis** and draw the **periodic table** of $k$-tuply monoidal $n$-categories. The slice is the combinatorial foundation underneath those conjectures.

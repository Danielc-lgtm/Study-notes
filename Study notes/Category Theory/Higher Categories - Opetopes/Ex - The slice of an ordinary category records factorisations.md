---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - The Slice of a Generalized Multicategory"
  - "Def - Category"
  - "Def - Functor"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

An ordinary [[Def - Category|category]] $\mathcal{D}$ may be viewed as a multicategory all of whose operations have arity $1$ (only one-input arrows). Describe the slice $\mathcal{D}^+$ of such a multicategory: identify its objects and its operations, and show that the operations of $\mathcal{D}^+$ are the *factorisations* of arrows of $\mathcal{D}$ (composable strings of arrows composing to a given arrow). Contrast this carefully with the ordinary **slice category** $\mathcal{D}/X$, and explain why the two are not the same construction.

**Recall:**

![[Def - The Slice of a Generalized Multicategory#The Definition]]

A [[Def - Category|category]] $\mathcal{D}$ is a multicategory whose only operations are unary: a multimap $(a) \to b$ is just a morphism $a \to b$, and there are no genuinely multi-ary operations. The [[Def - The Slice of a Generalized Multicategory|slice]] $C^+$ has objects = operations of $C$ and operations = pasting diagrams of operations of $C$. The ordinary **slice category** $\mathcal{D}/X$ has as objects the morphisms $a \to X$ into a fixed object $X$, and as morphisms the commuting triangles.

---

# Convergent Strategy

**Problem class:** This is an *unwind-the-construction-in-a-degenerate-case* problem — the structural-world problem class. The point is to compute the slice on the simplest non-trivial multicategory (an ordinary category) and to separate it cleanly from a similarly-named but different construction, sharpening understanding of what slicing actually does.

**Assumption pattern:** The assumption is that $\mathcal{D}$ has only unary operations. This is what makes the computation tractable: with no multi-ary operations, the "pasting diagrams" of the slice degenerate into *linear strings* of composable arrows, and the trees become paths. The arity-$1$ restriction is exactly what turns the rich opetopic combinatorics into ordinary factorisation.

**Theorem routing:** We route through the slice's defining property ([[Def - The Slice of a Generalized Multicategory|slice]]: objects = operations, operations = pasting diagrams) specialised to arity-$1$ operations. We compare against the definition of the ordinary [[Def - Category|slice category]], whose objects and morphisms are of a different shape entirely.

**Key decision point:** The non-obvious choice is to recognise that the operations of $\mathcal{D}^+$ are *factorisations* (a string $a \xrightarrow{f_1} a_1 \xrightarrow{f_2} \dots \xrightarrow{f_k} b$ composing to a chosen $g : a \to b$), not commuting triangles into a fixed object. The tempting error — fueled by the name "slice" — is to conflate $\mathcal{D}^+$ with $\mathcal{D}/X$; the decision is to track *what the objects and operations of each are* and notice they differ in both.

---

# Legal Operations Used

1. **Operation 1 (slice a multicategory to climb one dimension)** from the topic page, applied to the arity-$1$ multicategory $\mathcal{D}$. The objects of $\mathcal{D}^+$ are the arrows of $\mathcal{D}$; the operations are the factorisations.

2. **Operation 2 (read a cell off as a tree)** from the topic page. With only unary operations, the trees degenerate to *paths* (linear chains), so an operation of $\mathcal{D}^+$ is a path of arrows of $\mathcal{D}$ — a factorisation.

---

# Hints

> [!note]- Hint 1
> Apply "objects of $C^+$ = operations of $C$" with $C = \mathcal{D}$. Since the operations of $\mathcal{D}$ are exactly its morphisms, the objects of $\mathcal{D}^+$ are the morphisms of $\mathcal{D}$.

> [!note]- Hint 2
> The operations of $\mathcal{D}^+$ are pasting diagrams of arrows of $\mathcal{D}$. With only unary arrows, a "pasting diagram" is a string $f_1, f_2, \dots, f_k$ that composes — a path. So an operation of $\mathcal{D}^+$ is a composable string together with the arrow it composes to: a factorisation.

> [!note]- Hint 3
> Now write down $\mathcal{D}/X$: objects are arrows *into the fixed object $X$*, morphisms are commuting triangles. Compare the objects (all arrows vs. arrows into $X$) and the operations (factorisations vs. triangles). They differ in both slots.

---

# Solution

The route is to specialise the slice's defining property to an arity-$1$ multicategory, watch the pasting diagrams collapse to factorisations, and then set the result side by side with the ordinary slice category to see the two constructions are genuinely different.

**Step 1: The objects of $\mathcal{D}^+$ are the arrows of $\mathcal{D}$.**

> [!note]- Derivation
> By the defining property of the [[Def - The Slice of a Generalized Multicategory|slice]], an object of $\mathcal{D}^+$ is an operation of $\mathcal{D}$. Viewing $\mathcal{D}$ as a multicategory, its operations are exactly its morphisms (all unary). Hence
> $$\mathrm{ob}(\mathcal{D}^+) \;=\; \{\text{morphisms of } \mathcal{D}\} \;=\; \mathrm{Mor}(\mathcal{D}).$$
> So the objects of $\mathcal{D}^+$ are all arrows of $\mathcal{D}$ — not arrows into any fixed object, but *every* arrow.

**Step 2: The operations of $\mathcal{D}^+$ are the factorisations of arrows.**

> [!note]- Derivation
> An operation of $\mathcal{D}^+$ is a pasting diagram of operations of $\mathcal{D}$ composing to a single operation of $\mathcal{D}$. With only unary operations, a pasting diagram is a *linear chain* (a path): a composable string
> $$a \xrightarrow{f_1} a_1 \xrightarrow{f_2} a_2 \to \dots \xrightarrow{f_k} b,$$
> and "composing to a single operation" means this string composes, via $\mathcal{D}$'s composition, to a chosen arrow $g : a \to b$. So an operation of $\mathcal{D}^+$ with inputs $f_1, \dots, f_k$ and output $g$ is precisely a **factorisation** of $g$ as $g = f_k \circ \dots \circ f_1$. The arity-$0$ case (empty string) corresponds to an identity arrow; the arity-$1$ case to $g = f_1$ itself.
>
> By Operation 2, the tree of such an operation is a *path*: a degenerate planar tree with no branching, reflecting the arity-$1$ restriction. This is why slicing a category produces factorisation data rather than genuine many-in, one-out cells.

**Step 3: $\mathcal{D}^+$ is not the ordinary slice category $\mathcal{D}/X$.**

> [!note]- Derivation
> Write out the ordinary [[Def - Category|slice category]] $\mathcal{D}/X$:
> - **Objects of $\mathcal{D}/X$:** morphisms $a \xrightarrow{p} X$ into the *fixed* object $X$.
> - **Morphisms of $\mathcal{D}/X$:** commuting triangles, i.e. an arrow $h : a \to a'$ with $p' \circ h = p$.
>
> Now compare with $\mathcal{D}^+$:
> - **Objects of $\mathcal{D}^+$:** *all* morphisms of $\mathcal{D}$ (no fixed target).
> - **Operations of $\mathcal{D}^+$:** factorisations (composable strings), which are *many-in, one-out* (the inputs are the $f_i$, the output is $g$) — not triangles.
>
> The two differ in *both* slots. The objects of $\mathcal{D}/X$ are restricted to a fixed codomain $X$, whereas $\mathcal{D}^+$ takes all arrows. The morphisms of $\mathcal{D}/X$ are unary (a single arrow $h$ making a triangle commute), whereas the operations of $\mathcal{D}^+$ are multi-ary (a string of arrows). The ordinary slice category is, at best, a *fixed-target, arity-one degeneration* of the slice $\mathcal{D}^+$ — it forgets the many-in structure and pins the target. Confusing the two would collapse every $2$-opetope to a triangle and destroy the chapter's geometry.

> [!note]- Complete formal solution
> View $\mathcal{D}$ as an arity-$1$ multicategory: its operations are its morphisms.
>
> By the slice's defining property, $\mathrm{ob}(\mathcal{D}^+) = \mathrm{Mor}(\mathcal{D})$: the objects of $\mathcal{D}^+$ are all arrows of $\mathcal{D}$.
>
> An operation of $\mathcal{D}^+$ is a pasting diagram of arrows of $\mathcal{D}$ composing to one arrow. With only unary operations the pasting diagram is a path $a \xrightarrow{f_1} \dots \xrightarrow{f_k} b$, and "composes to $g$" means $g = f_k \circ \dots \circ f_1$. Hence the operations of $\mathcal{D}^+$ are exactly the **factorisations** of arrows of $\mathcal{D}$, with the trees degenerating to paths.
>
> This differs from the ordinary slice category $\mathcal{D}/X$ in both objects (all arrows vs. arrows into a fixed $X$) and morphisms/operations (multi-ary factorisations vs. unary commuting triangles). The ordinary slice is the arity-one, fixed-target degeneration; the multicategory slice $\mathcal{D}^+$ is genuinely richer. $\blacksquare$

---

# Key Takeaways

**Degenerate cases reveal what a construction is really doing.** Computing the slice on an ordinary category strips away the many-in complexity and shows the residue: factorisation data. The trigger for this technique is any unfamiliar construction with a clean special case — instantiate it on the simplest input (here, an arity-$1$ multicategory) and see what survives. The surviving structure (factorisations / paths) is the "spine" of the general construction, and recognising it makes the general case (genuine trees of operations) far less mysterious. This is the same move as checking a new functor on the terminal object, or a new measure on a point mass: the degenerate case is a microscope on the definition.

**Watch out for name collisions between different "slices".** The word "slice" names at least two different constructions here — the ordinary slice category $\mathcal{D}/X$ and the multicategory slice $\mathcal{D}^+$ — and they are not the same. The reusable lesson is to never trust a shared name: always re-derive the *objects* and *morphisms/operations* of each construction and compare them slot by slot. Here the comparison shows they differ in both, with $\mathcal{D}/X$ being a fixed-target arity-one degeneration of $\mathcal{D}^+$. This diagnostic — "same name, check both data slots" — saves enormous confusion across category theory, where "product", "fibre", "extension", and "nerve" all name several distinct things in different contexts.

**Arity-one is the bridge between opetopes and globes.** The exercise makes precise that an ordinary category is the arity-$1$ slice of the opetopic world, and that its trees are paths rather than branching trees. This is the concrete sense in which globular (one-in, one-out) structures are the arity-$1$ restriction of opetopic (many-in, one-out) structures: kill all arities except $1$ and the opetopes collapse to globes, the trees collapse to paths, and the slice collapses to factorisation. The trigger is any comparison between globular and opetopic models: look at what arity-$1$ truncation does, and you will find the globular structure sitting inside the opetopic one as the no-branching special case. See [[Ex - The 2-opetopes are indexed by arity via the first slice]] for the full arity-graded family that branching restores.

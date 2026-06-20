---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - Opetope"
  - "Def - The Slice of a Generalized Multicategory"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Describe, as finite rooted planar trees, the opetopes of dimensions $0$, $1$, $2$, and at least two distinct opetopes of dimension $3$. For each, identify the source faces (inputs / leaves) and the target face (output / root). Confirm that there is exactly one $0$-opetope and one $1$-opetope, that there is one $2$-opetope for each arity $n = 0, 1, 2, \dots$, and that the $3$-opetopes are pasting diagrams of $2$-opetopes.

**Recall:**

![[Def - Opetope#The Definition]]

An [[Def - Opetope|opetope]] is recorded combinatorially by a finite, rooted, **planar** tree: the root edge is the output (target) face, the leaf edges are the input (source) faces, and each internal vertex is labelled by a lower-dimensional opetope. The recursion is "an $n$-opetope is a pasting diagram of $(n-1)$-opetopes". By [[Def - The Slice of a Generalized Multicategory|slicing]], the operations of the $(n-1)$-th slice (which are pasting diagrams of $(n-1)$-opetopes) are the $n$-opetopes.

---

# Convergent Strategy

**Problem class:** This is a *describe-and-enumerate-the-shapes* problem, the combinatorial-world problem class from the topic page's problem-solving strategy. The goal is not to prove a theorem but to make the recursion concrete by drawing the first few shapes and reading off their faces — the single most valuable habit for this chapter, because the slice recursion is opaque until you have watched it generate actual cells.

**Assumption pattern:** The only assumption is the recursive definition of opetope and the tree encoding. The recursion "$n$-opetope = pasting diagram of $(n-1)$-opetopes" lets us build dimension $n$ entirely from dimension $n-1$, and the tree encoding lets us *draw* each pasting diagram. The base data — one point, one arrow — anchors everything.

**Theorem routing:** We route through [[Thm - Opetopes via Iterated Slicing of the Identity Operad|the iterated-slicing theorem]], whose enumeration corollary tells us exactly the counts to expect ($|\mathcal{O}_0| = |\mathcal{O}_1| = 1$, $\mathcal{O}_2 \cong \mathbb{N}$ by arity, $\mathcal{O}_3 \cong$ trees of $2$-opetopes). We use the theorem as a checklist: each shape we draw should match the predicted count.

**Key decision point:** The non-obvious choice is to encode a $2$-opetope as a *single vertex with $n$ leaves and one root* (the arity-$n$ cell) rather than as a planar diagram of arrows, and to encode a $3$-opetope as a *tree of such vertices*. The natural alternative — drawing globular-looking pictures — fails because globes have one source, whereas opetopes have many; the tree encoding is what records the many-in structure faithfully.

---

# Legal Operations Used

1. **Operation 1 (slice a multicategory to climb one dimension)** from the topic page. Each dimension is obtained by slicing the previous: the $2$-opetopes are the operations of $I^+$, the $3$-opetopes the operations of $I^{++}$. We use this to know *what* the cells of each dimension are before drawing them.

2. **Operation 2 (read a cell off as a tree)** from the topic page. This is the core move: every opetope is drawn as a finite rooted planar tree, root = output, leaves = inputs, vertices = lower opetopes. All the drawing is this operation applied dimension by dimension.

---

# Hints

> [!note]- Hint 1
> Start at the bottom and use the recursion strictly: the $0$-opetope is the point (no faces), the $1$-opetope is the arrow (one source point, one target point). Then a $2$-opetope is a pasting diagram of arrows, drawn as a tree.

> [!note]- Hint 2
> A $2$-opetope of arity $n$ is a single vertex with $n$ incoming leaf edges (the $n$ source arrows) and one outgoing root edge (the target arrow). Draw the cases $n = 0, 1, 2, 3$ and notice you get one shape per natural number.

> [!note]- Hint 3
> A $3$-opetope is a tree whose *vertices* are $2$-opetopes, glued so that the output arrow of one is an input arrow of another. The smallest non-trivial ones stack two arity-$2$ cells; these are the associativity-style coherence cells.

---

# Solution

The route is to walk up the dimensions, drawing each opetope as a tree and reading its faces from the tree. We confirm the counts against the enumeration corollary at each step: one point, one arrow, one $2$-opetope per arity, and trees of those in dimension $3$.

**Step 1: Dimensions 0 and 1 each have exactly one opetope.**

> [!note]- Derivation
> The $0$-opetope is the **point** $\bullet$ — a tree with a single edge and no vertices, or equivalently a bare object. It has no source and no target faces. There is exactly one, because $I = 1$ has one object: $|\mathcal{O}_0| = 1$.
>
> The $1$-opetope is the **arrow** $\bullet \to \bullet$. As a tree it is a single edge from a root (target point) to a leaf (source point), or a single vertex (the arrow) with one leaf and one root. Its source is one point, its target is one point. There is exactly one, because the relevant operation of $I$ is the unique unary one: $|\mathcal{O}_1| = 1$. These match the corollary's $|\mathcal{O}_0| = |\mathcal{O}_1| = 1$.

**Step 2: There is one $2$-opetope for each arity $n = 0, 1, 2, \dots$.**

> [!note]- Derivation
> A $2$-opetope is a pasting diagram of $1$-opetopes (arrows) composing to one arrow. As a tree it is a single vertex (the $2$-cell) with $n$ incoming leaf edges (the source arrows $f_1, \dots, f_n$, in order) and one outgoing root edge (the target arrow $g$).
>
> - **Arity $0$:** a vertex with no leaves and one root — the $2$-cell with empty source. This is the shape of a *unit* / identity-witness ($\Rightarrow g$ from nothing), which has no globular analogue.
> - **Arity $1$:** one leaf, one root — the shape $f \Rightarrow g$, the only $2$-opetope that coincides with the $2$-globe.
> - **Arity $2$:** two leaves $f_1, f_2$, one root $g$ — the familiar $2$-cell $f_2 \circ f_1 \Rightarrow g$.
> - **Arity $3$:** three leaves, one root — $f_3 \circ f_2 \circ f_1 \Rightarrow g$.
>
> There is exactly one shape per arity, so $\mathcal{O}_2 \cong \mathbb{N}$ is countably infinite, matching the corollary.

**Step 3: $3$-opetopes are pasting diagrams (trees) of $2$-opetopes.**

> [!note]- Derivation
> A $3$-opetope is a pasting diagram of $2$-opetopes: a tree whose *vertices* are $2$-cells (each of some arity), glued so that an output arrow of one vertex is an input arrow of the next, all composing to a single target $2$-cell.
>
> - **Example A (a two-vertex tree).** Take an arity-$2$ source $2$-cell $\beta : g_1 \circ f_1 \Rightarrow h_1$ and another arity-$2$ source $2$-cell whose input includes $h_1$, composing to one arity-$3$ target $2$-cell. The source is the *pasting* of the two $2$-cells; the target is the single $2$-cell $f_3 \circ f_2 \circ f_1 \Rightarrow k$. This is an associativity coherence cell relating the two ways of composing three $1$-cells.
> - **Example B (a different two-vertex tree).** Stack an arity-$1$ $2$-cell on top of an arity-$2$ $2$-cell; the resulting $3$-opetope has a different source pasting diagram (a different tree) and hence is a distinct $3$-opetope, witnessing a unitor-style coherence.
>
> Because the source side is an arbitrary planar tree of $2$-cells, $\mathcal{O}_3$ is infinite and combinatorially rich — exactly "trees of $2$-opetopes", as the corollary predicts.

> [!note]- Complete formal solution
> By the recursive definition of [[Def - Opetope|opetope]] and the [[Thm - Opetopes via Iterated Slicing of the Identity Operad|iterated-slicing theorem]]:
>
> **$\mathcal{O}_0$:** the point, a tree with no vertices. $|\mathcal{O}_0| = 1$ (one object of $I$).
>
> **$\mathcal{O}_1$:** the arrow, a single edge / single unary vertex with one leaf and one root. Source: a point; target: a point. $|\mathcal{O}_1| = 1$ (the unary operation of $I$).
>
> **$\mathcal{O}_2$:** for each $n \in \mathbb{N}$, the single vertex with $n$ ordered leaf edges (source arrows $f_1, \dots, f_n$) and one root edge (target arrow $g$); shape $f_n \circ \dots \circ f_1 \Rightarrow g$. Arity $0$ is the unit cell, arity $1$ the only globular $2$-cell. $\mathcal{O}_2 \cong \mathbb{N}$.
>
> **$\mathcal{O}_3$:** planar trees whose vertices are $2$-opetopes, glued along shared arrows, composing to one target $2$-cell. Two distinct examples: (A) two arity-$2$ $2$-cells stacked (an associativity coherence $3$-cell); (B) an arity-$1$ over an arity-$2$ $2$-cell (a unitor-style coherence $3$-cell). $\mathcal{O}_3 \cong \{\text{planar trees of } 2\text{-opetopes}\}$, infinite. $\blacksquare$

---

# Key Takeaways

**Always draw the bottom cases before reasoning abstractly.** The opetope recursion is genuinely hard to feel until you have produced the point, the arrow, the arity-graded family of $2$-cells, and a couple of $3$-cells by hand. The trigger for this technique is any time a recursive shape definition appears: resist the urge to manipulate the recursion symbolically and instead instantiate it at $n = 0, 1, 2, 3$. The same habit pays off for simplices ($\Delta^0, \Delta^1, \Delta^2$), for globes, and for any inductively defined family — the low cases reveal the pattern that the recursion encodes, and they expose surprises (here, that there is a unit cell of arity $0$ and that $\mathcal{O}_2$ is already infinite) that a symbolic reading hides.

**The arity-graded family is the signature of "many-in, one-out".** The single most important structural fact this exercise surfaces is that there is one $2$-opetope per arity, so $\mathcal{O}_2$ is infinite. This is exactly where opetopes diverge from globes (one shape per dimension) and is the concrete face of "many things compose to one thing". Whenever you see an infinite arity-indexed family of cells in a single dimension, you are looking at a many-in, one-out (opetopic or operadic) structure rather than a globular one; conversely, a finite "one shape per dimension" list signals a globular structure. This diagnostic recurs throughout higher category theory and tells you immediately which shape category you are in.

**Trees turn higher cells into objects you can manipulate by induction.** Encoding a $3$-opetope as a tree of $2$-opetopes is not just a drawing convenience: it converts every question about higher opetopes into a question about finite planar trees, where induction on the number of vertices or leaves is available. The trigger is any combinatorial claim about opetopes (counting, defining an operation, proving two opetopes equal): translate to trees first. This is the reusable bridge to Appendix E and to the combinatorics of free operads, and it is why the abstract slice construction can be computed with at all. See [[Ex - The 2-opetopes are indexed by arity via the first slice]] for the companion enumeration through the slice, and [[Ex - The slice of an ordinary category records factorisations]] for what slicing does to an arity-one multicategory.

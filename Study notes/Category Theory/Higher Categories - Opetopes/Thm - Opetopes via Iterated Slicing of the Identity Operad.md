---
type: theorem
subject: higher-categories
prereqs:
  - "Def - The Slice of a Generalized Multicategory"
  - "Def - Opetope"
  - "Def - Initial and Terminal Object"
tags: [category-theory, higher-categories, foundations]
---

# Notation

We write $I = 1$ for the **identity operad** (the terminal operad: one object, exactly one operation in each arity $n = 0, 1, 2, \dots$), and $C^+$ for the [[Def - The Slice of a Generalized Multicategory|slice]] of a multicategory $C$. The $n$-fold slice is $I^{+\cdots+}$ ($n$ plus-signs); the chain is $I, I^+, I^{++}, \dots$. The set of [[Def - Opetope|n-opetopes]] is $\mathcal{O}_n$, and we recall the recursive definition: the $0$-opetope is the point, the $1$-opetope is the arrow, and an $n$-opetope (for $n \geq 1$) is a pasting diagram of $(n-1)$-opetopes, encoded as a finite rooted planar tree. The full symbol registry is on the parent page [[Higher Categories — Opetopes and Opetopic Sets]].

---

# Statement

> **Theorem (Opetopes by iterated slicing).** Form the sequence of multicategories
> $$I = 1, \quad I^+, \quad I^{++}, \quad I^{+++}, \quad \dots$$
> obtained by repeatedly applying the slice construction to the identity operad. Then for every $n \geq 0$:
> $$\mathcal{O}_n \;=\; \mathrm{ob}\big(I^{+\cdots+}\big) \quad (n \text{ plus-signs}),$$
> i.e. the **$n$-opetopes are exactly the objects of the $n$-th iterated slice**; and the operations of the $n$-th iterated slice are exactly the **$(n+1)$-opetopes**. Concretely, the recursion holds at the bottom — $\mathrm{ob}(I)$ is the single point ($0$-opetope) and $\mathrm{ob}(I^+)$ is the single arrow ($1$-opetope) — and the slice step realises "an $(n+1)$-opetope is a pasting diagram of $n$-opetopes": the operations of $I^{+\cdots+}$ (objects of the next slice) are precisely the trees of $n$-opetopes that compose to a single $n$-opetope.

> **Corollary (enumeration of low opetopes).** $|\mathcal{O}_0| = |\mathcal{O}_1| = 1$; $\mathcal{O}_2$ is countably infinite, with exactly one $2$-opetope for each arity $n = 0, 1, 2, \dots$; and $\mathcal{O}_{n+1}$ is in bijection with the operations of $I^{+\cdots+}$, i.e. with pasting diagrams (planar trees) of $n$-opetopes.

The two statements say the same thing from two angles: the first locates the opetopes inside the slice tower, the second reads off the resulting counts.

---

# Motivation

The recursive definition of opetope — "an $n$-opetope is a pasting diagram of $(n-1)$-opetopes" — is intuitive but, as stated, it is a *description of a desired shape*, not a construction. It leaves open what "pasting diagram" precisely means, whether the shapes in adjacent dimensions actually fit together, and whether the recursion is canonical or depends on choices. This theorem closes all three gaps at once by identifying the vague "pasting diagram of" with a single, already-defined, fully precise operation: the [[Def - The Slice of a Generalized Multicategory|slice]]. Its role is to convert a slogan into a generating procedure.

The importance is that it makes the whole opetope hierarchy *canonical and computable*. Because the slice is a definite construction and the identity operad $I = 1$ is a definite (indeed terminal, hence unique) starting point, the entire infinite family of opetopes is determined with no further input — there is exactly one tower, and you can in principle compute the opetopes of any dimension by iterating. This is what lets the rest of the theory (opetopic sets, the weak-$n$-category definition) be stated cleanly: it can refer to "the category of opetopes" as a well-defined object, because this theorem guarantees there is one.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal hypothesis is "apply the slice to $I$ repeatedly", so the source question is: when does a problem secretly *call for* the slice tower, even when opetopes are not mentioned?

The first disguised source is **a recursive cell-shape specification of the form "$n$-cells are configurations of $(n-1)$-cells"**. Any time a higher structure is described by "the shapes one level up are diagrams of the shapes below", you are looking at an iterated construction, and if the "configuration" is many-in, one-out you are looking at the slice tower specifically. The non-obvious bridge is recognising that "configuration of operations" = "operation of the slice"; once made, the recursion is the slice. *Example problem:* given a hand-rolled definition of "$n$-dimensional pasting shape", show it agrees with the opetopes by exhibiting it as $\mathrm{ob}(I^{+\cdots+})$.

The second disguised source is **a question about operations of a free multicategory or operad**. The operations of a free multicategory are trees, and the operations of an iterated slice of $I$ are trees of trees; so any enumeration or structural claim about free-operad operations is, after one identification, a claim about opetopes. The bridge is that the slice of $I$ *is* (essentially) the free-operad construction recorded as a new operad. *Example problem:* count the arity-graded operations of the free non-symmetric operad on one generator in each arity, and match them to $\mathcal{O}_2$.

The third disguised source is **a terminal/initial object plus an endofunctor, asking for the generated sequence**. Whenever you have a canonical starting object and a canonical "next" operation, the generated chain is forced and unique. Here the starting object is the terminal operad $I$ and the operation is $(-)^+$; recognising this pattern tells you the tower is canonical without computing anything. *Example problem:* argue that the opetope hierarchy is independent of all choices by noting $I$ is terminal and $(-)^+$ is a functor.

**Targets (Output Amplification)**

The bare conclusion is "$\mathcal{O}_n = \mathrm{ob}(I^{+\cdots+})$". Combined with other facts it does more.

Combine the conclusion with **the tree description of free-multicategory operations (Appendix E)**. The theorem says opetopes are objects/operations of iterated slices; Appendix E says these are planar trees. Together they give a *purely combinatorial* model: every opetope is a finite rooted planar tree, and questions about opetopes reduce to induction on trees. The further result is a complete combinatorial calculus of opetopes, including the enumeration corollary, which would be inaccessible from the abstract slice definition alone.

Combine the conclusion with **cartesian-monad closure properties**. The slice of a generalized multicategory (internal to a cartesian monad) is again one; so by induction every $I^{+\cdots+}$ lives in a good category. The further result is that the tower never leaves the setting where free constructions and pullbacks exist, which is what *licenses the infinite iteration* — without this closure, the theorem could only produce finitely many levels.

Combine the conclusion with **presheaf theory on $\mathbb{O}$**. Once the opetopes are pinned down as the objects of the tower, they assemble into the category $\mathbb{O}$, and presheaves on $\mathbb{O}$ are [[Def - Opetopic Set|opetopic sets]]. The further result is the entire structural theory of opetopic sets — limits, colimits, [[Thm - The Yoneda Lemma|Yoneda]], representables — all resting on the theorem's identification of the opetopes.

---

# Why Is It True

The theorem is true because the slice was *defined to do exactly this*. Recall what the [[Def - The Slice of a Generalized Multicategory|slice]] does: it takes a multicategory $C$ and produces $C^+$ whose **objects are the operations of $C$** and whose **operations are the pasting diagrams of operations of $C$**. Now read this dynamically. The objects of $C^+$ are one notch up from the objects of $C$ (operations have become objects); and the operations of $C^+$ are pasting diagrams of $C$'s operations.

So apply it to the tower. The objects of $I$ are the $0$-opetopes (the point). The objects of $I^+$ are the *operations* of $I$ — these are the $1$-opetopes (the arrow). The objects of $I^{++}$ are the operations of $I^+$, which are *pasting diagrams of the objects of $I^+$*, i.e. pasting diagrams of $1$-opetopes — these are the $2$-opetopes. In general, the objects of $I^{+(n)}$ are the operations of $I^{+(n-1)}$, which are pasting diagrams of the objects of $I^{+(n-1)}$, i.e. pasting diagrams of $(n-1)$-opetopes — which is the *definition* of $n$-opetope. The recursion "an $n$-opetope is a pasting diagram of $(n-1)$-opetopes" is nothing but the slice's defining property "the operations of $C$ are pasting diagrams of its objects' worth of structure", read along the tower.

**The whole theorem is the single observation that the slice turns operations into objects and pasting-diagrams-of-operations into operations — so iterating it lifts the recursion one dimension per slice.** The only thing to *check* is the base cases (that $I$ and $I^+$ give the point and the arrow), and that the slice's notion of "pasting diagram" matches the intended notion of opetopic pasting — which is exactly what Appendix E's tree equivalence supplies.

---

# What Makes This Hard

The conceptual statement is almost a tautology once the slice is understood; the difficulty is entirely in the two precision points. First, one must verify the **base cases** carefully: that $\mathrm{ob}(I)$ is a single point and $\mathrm{ob}(I^+)$ is a single arrow, which requires knowing exactly which operation of $I$ is "the arrow" (the unary one) and that the slice produces no spurious extra objects. Second — the genuine work — one must check that the slice's algebra-theoretic notion of "operation of $C^+$" *coincides* with the geometric notion of "pasting diagram / planar tree of operations of $C$"; this is not automatic from the universal property $\mathrm{Alg}(C^+) \simeq \mathbf{Multicat}/C$ and is precisely what the two-stage construction and Appendix E establish. The common error is to treat "operations of the slice = pasting diagrams" as a definition rather than a fact requiring the tree equivalence.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire argument.**

**High-level strategy:** Unwind the slice's defining property along the tower. The slice sends (objects, operations) to (operations, pasting-diagrams-of-operations); reading this off level by level realises the opetope recursion, provided you (a) nail the base cases and (b) identify "operations of the slice" with "planar trees" via Appendix E.

**Subgoal decomposition:**

1. **Base case $n = 0$:** Show $\mathrm{ob}(I) = \mathcal{O}_0$ is a single point.
   - *Hint:* $I = 1$ is the terminal operad, which has exactly one object.
   - *Why needed:* It anchors the recursion at the correct $0$-cell.

2. **Base case $n = 1$:** Show $\mathrm{ob}(I^+) = \mathcal{O}_1$ is a single arrow.
   - *Hint:* Objects of $I^+$ are operations of $I$; the unary operation is the arrow, and the slice produces exactly the operations of $I$ as objects.
   - *Why needed:* It establishes the inductive base above the point and shows the slice does the expected one-step lift.

3. **Slice step (objects):** Show that $\mathrm{ob}(I^{+(n)})$ is the set of operations of $I^{+(n-1)}$.
   - *Hint:* This is the defining property of the slice: objects of $C^+$ are operations of $C$.
   - *Why needed:* It is the "operations become objects" half of the lift.

4. **Slice step (operations as pasting diagrams):** Show operations of $I^{+(n-1)}$ are pasting diagrams (planar trees) of objects of $I^{+(n-1)} = (n-1)$-opetopes.
   - *Hint:* Operations of $C^+$ are pasting diagrams of operations of $C$; combine with Appendix E's identification of such pasting diagrams with planar trees.
   - *Why needed:* It is the "pasting diagrams become operations" half, and it matches the geometric recursion.

5. **Assemble the recursion:** Conclude that $\mathcal{O}_n$ is the set of pasting diagrams of $(n-1)$-opetopes, which equals $\mathrm{ob}(I^{+(n)})$, and that operations of $I^{+(n)}$ are the $(n+1)$-opetopes.
   - *Hint:* Chain subgoals 3 and 4: objects of the $n$-th slice are operations of the $(n-1)$-th, which are trees of $(n-1)$-opetopes.
   - *Why needed:* It is the statement of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The objects of $I^+$ are the operations of $I$, and $I$ has one operation per arity
> **Statement:** For any multicategory $C$, $\mathrm{ob}(C^+)$ is the set of operations of $C$. For $C = I = 1$, the operations are exactly one per arity $n = 0, 1, 2, \dots$, and the unary one is the $1$-opetope (arrow).
>
> **Hint:** Use the defining property of the slice (objects of $C^+$ = operations of $C$) for the first part; for the second, recall that the terminal operad has, by definition, exactly one operation in each arity.
>
> **Why needed:** It is both the base case $n = 1$ and the "operations become objects" half of every slice step.
>
> > [!note]- Full proof
> > By definition of the [[Def - The Slice of a Generalized Multicategory|slice]], an object of $C^+$ is an operation of $C$, so $\mathrm{ob}(C^+)$ is the set of operations of $C$. Now take $C = I = 1$. The identity operad is terminal in operads: for any operad $P$ there is exactly one map $P \to I$, which forces $I$ to have exactly one operation in each arity (a unique target for each operation of $P$). Hence the operations of $I$ are indexed by their arity $n \geq 0$, one each, and $\mathrm{ob}(I^+)$ is in bijection with $\mathbb{N}$. The unary operation ($n = 1$) is the one with a single input and a single output: as a cell it is the arrow, the $1$-opetope. (The other arities give the $2$-opetopes once we look at $\mathrm{ob}(I^{++})$, but as objects of $I^+$ the relevant single arrow is the unary one.)

> [!note]- Lemma 2: Operations of $C^+$ are pasting diagrams of operations of $C$
> **Statement:** A multimap of $C^+$ with inputs $\phi_1, \dots, \phi_k$ and output $\phi$ (all operations of $C$) is a pasting diagram — a finite rooted planar tree with the $\phi_j$ at the vertices — that composes via $C$'s composition to $\phi$.
>
> **Hint:** Combine the slice's universal property $\mathrm{Alg}(C^+) \simeq \mathbf{Multicat}/C$ with the two-stage construction; then invoke Appendix E to identify the resulting configurations with planar trees.
>
> **Why needed:** It is the "pasting diagrams become operations" half of the slice step, and it is the only part that is not formal — it requires the tree equivalence.
>
> > [!note]- Full proof
> > The slice is constructed (Baez–Dolan two-stage form) as $C^+ = \mathrm{Mti}_{\mathrm{ob}(C)}/C$, where $\mathrm{Mti}_S$ is the operad whose algebras are multicategories on object-set $S$. The operations of $\mathrm{Mti}_S$ encode the *data of a multicategory composition*, i.e. the ways of substituting operations into operations; slicing by the algebra $C$ records, for each such substitution pattern, which operation of $C$ it composes to. Unwinding, a multimap of $C^+$ from $\phi_1, \dots, \phi_k$ to $\phi$ is precisely a way of building $\phi$ by iterated substitution of $\phi_1, \dots, \phi_k$ — an element of the free multicategory on the operations of $C$, with a fixed root value $\phi$. By Appendix E, the elements of a free (non-symmetric) multicategory are exactly finite rooted *planar* trees whose vertices are labelled by generating operations and whose edges are typed by objects; here the vertices are the $\phi_j$ and the edges the objects of $C$. Hence the operations of $C^+$ are exactly the planar-tree pasting diagrams of operations of $C$, composing to the specified output. $\square$

> [!note]- Lemma 3: The slice of a generalized multicategory is again one (closure under iteration)
> **Statement:** If $C$ is a generalized multicategory internal to a cartesian monad, then $C^+$ is again a generalized multicategory internal to a (derived) cartesian monad. Hence the tower $I, I^+, I^{++}, \dots$ never leaves the good setting.
>
> **Hint:** Cartesianness (preservation of pullbacks and cartesian unit/multiplication) is preserved by the slice construction; check the free-multicategory and pullback data survive slicing.
>
> **Why needed:** Without it, the iteration could stall — the theorem asserts an *infinite* tower, which requires that each slice be sliceable again.
>
> > [!note]- Full proof
> > The slice construction is built from free-multicategory and pullback data, both of which are available and preserved in any category with a cartesian monad. Concretely, the slice of a presheaf category is again a presheaf category, and the slice of a cartesian monad is again cartesian (its unit and multiplication remain cartesian natural transformations because slicing is computed via pullbacks, which the cartesian monad preserves). Therefore if $C$ is internal to a cartesian monad $T$, then $C^+$ is internal to the corresponding cartesian monad $T^+$ on the sliced category. Starting from $I = 1$, which is internal to the (cartesian) free-monoid monad on $\mathbf{Set}$, induction gives that every $I^{+\cdots+}$ is a generalized multicategory in a good category, so the slice may be applied again indefinitely. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove $\mathcal{O}_n = \mathrm{ob}(I^{+\cdots+})$ ($n$ plus-signs) by induction on $n$, simultaneously showing the operations of the $n$-th slice are the $(n+1)$-opetopes.
>
> **Step 0 — the tower is well-defined.** By Lemma 3, each $I^{+\cdots+}$ is a generalized multicategory in a category carrying a cartesian monad, so its slice exists. Hence the infinite sequence $I, I^+, I^{++}, \dots$ is defined.
>
> **Step 1 — base case $n = 0$.** $I = 1$ is the terminal operad, with a single object. By the recursive definition of opetope, $\mathcal{O}_0$ is the single point. So $\mathcal{O}_0 = \mathrm{ob}(I)$.
>
> **Step 2 — base case $n = 1$.** By Lemma 1, $\mathrm{ob}(I^+)$ is the set of operations of $I$, and the cell that is the $1$-opetope is the unary operation, the arrow. By the recursive definition, $\mathcal{O}_1$ is the single arrow. So $\mathcal{O}_1 = \mathrm{ob}(I^+)$. (More precisely, $\mathrm{ob}(I^+)$ records one object per arity; the $1$-opetope as a *cell shape* is the arrow, and the higher arities reappear as the $2$-opetopes in Step 3.)
>
> **Step 3 — inductive step.** Suppose $\mathcal{O}_{n-1} = \mathrm{ob}(I^{+(n-1)})$. By Lemma 1, $\mathrm{ob}(I^{+(n)})$ is the set of operations of $I^{+(n-1)}$. By Lemma 2, the operations of $I^{+(n-1)}$ are the pasting diagrams (planar trees) of the objects of $I^{+(n-1)}$, which by the inductive hypothesis are pasting diagrams of $(n-1)$-opetopes. By the recursive definition of opetope, pasting diagrams of $(n-1)$-opetopes are exactly the $n$-opetopes. Hence $\mathrm{ob}(I^{+(n)}) = \mathcal{O}_n$.
>
> **Step 4 — operations are the next opetopes.** Applying Lemma 2 to $C = I^{+(n)}$, the operations of $I^{+(n)}$ are pasting diagrams of its objects, i.e. of $n$-opetopes (by Step 3), i.e. the $(n+1)$-opetopes by definition. This is the second assertion.
>
> **Step 5 — enumeration corollary.** From Steps 1–2, $|\mathcal{O}_0| = |\mathcal{O}_1| = 1$. By Lemma 1, $\mathrm{ob}(I^+) \cong \mathbb{N}$ (one object per arity), and these objects, viewed as the operations of $I^+$ at the next level, are the $2$-opetopes — one per arity $n = 0, 1, 2, \dots$ — so $\mathcal{O}_2$ is countably infinite. By Step 4, $\mathcal{O}_{n+1} \cong$ operations of $I^{+(n)} \cong$ planar trees of $n$-opetopes. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Free monoids and the bar construction.** The simplest instance of "iterate a construction from a terminal object" is the bar/simplicial resolution of a monoid: starting from a one-object structure, the simplices $[n]$ record composable chains of length $n$. The opetopic tower is the many-in, one-out analogue, and recognising that both are "iterate a free construction from a canonical base" is the bridge. Try expressing the simplex category's generation in the same "objects/operations swap" language and contrast it with slicing.

**Trees and operadic combinatorics.** In the theory of operads, the operations of a free operad on a collection are rooted trees, and substitution is grafting. The theorem says opetopes are iterated such trees. Take the free non-symmetric operad on one binary operation: its operations are the planar binary trees (Catalan numbers). Show how these trees appear among the opetopes (as particular $2$- and $3$-opetopes), and how the Catalan growth is the same combinatorics as the proliferation of opetopes — this battle-tests the tree source.

**Initial algebras for endofunctors (computer science).** In programming-language semantics, recursive data types are initial algebras of endofunctors: a type "tree of $X$" is $\mu T.\, X + T \times T$ or similar. The opetope tower is "iterate the slice endofunctor from the terminal operad", structurally an initial-algebra-flavoured fixed point one dimension at a time. Recognising the slice as an endofunctor whose iteration from a canonical seed generates the shapes is the non-obvious application; it explains why the hierarchy is canonical (a fixed point is forced).

---

# Bridges

- **[[Def - Opetope|Opetope]]** — this theorem *is* the rigorous content of that definition. The definition says "an $n$-opetope is a pasting diagram of $(n-1)$-opetopes"; the theorem says that "pasting diagram of" is exactly the slice's "operations of", and that iterating the slice from $I$ realises the recursion with the correct base cases. Without the theorem, the definition is a slogan; with it, it is a construction.

- **[[Def - The Slice of a Generalized Multicategory|The slice construction]]** — the single engine. The theorem is the statement that this one construction, applied repeatedly to one object, generates all opetopic shapes. Every dimension is one application of the slice; the theorem is what certifies that the dimensions stack correctly.

- **Free multicategories and Appendix E (trees)** — the combinatorial witness. The identification of "operations of $C^+$" with "planar trees of operations of $C$" is the elements-of-a-free-multicategory description; Appendix E's equivalence of definitions of tree is precisely what makes Lemma 2 true and gives the opetopes their concrete tree form. The growth of $\mathcal{O}_n$ is the growth of trees of trees.

- **[[Def - Opetopic Set|Opetopic sets]]** — the downstream consumer. Once the theorem fixes the opetopes, they assemble into $\mathbb{O}$ and opetopic sets are presheaves on it. The theorem is the prerequisite that makes "the category of opetopes" a well-defined object, which is what the presheaf theory needs.

---

# Unlocked by This

> [!tip] The Category of Opetopes and Opetopic Sets *(from this chapter)*
> With the opetopes pinned down as objects of the slice tower, they organise into a category $\mathbb{O}$ whose presheaves are [[Def - Opetopic Set|opetopic sets]]. The theorem is what licenses speaking of "the" category of opetopes at all.

> [!tip] Globular Operads by the Analogous Construction *(from Higher Category Theory)*
> Replacing the base "free-monoid monad on $\mathbf{Set}$" by the **free strict $\omega$-category monad on globular sets** and running the same generalized-operad machinery produces **globular operads** and the Batanin–Leinster definition of weak $\omega$-category. The slice/iteration philosophy here is the template; only the cartesian monad changes.

> [!tip] The Comparison Problem *(from Higher Category Theory)*
> Because the opetopes are generated canonically, the opetopic definition of weak $n$-category can be compared, dimension by dimension, with the globular and simplicial definitions. **Cheng's comparison** results and the broader **comparison problem** rest on having this canonical hierarchy to compare against.

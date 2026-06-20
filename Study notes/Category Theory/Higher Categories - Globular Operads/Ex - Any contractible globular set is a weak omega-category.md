---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)"
  - "Def - Contraction on a Globular Operad"
  - "Def - Globular Operad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

A globular set $X$ is **contractible** if the unique map $X \to 1$ (to the terminal globular set) is a [[Def - Contraction on a Globular Operad|contractible]] map — equivalently, any two parallel $n$-cells of $X$ are the source and target of some $(n+1)$-cell. Show that **any contractible globular set is canonically a [[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)|weak ω-category]]**, by proving:

(a) the endomorphism operad $\mathrm{End}(X)$ admits a contraction;

(b) the unique contraction-preserving operad map $L \to \mathrm{End}(X)$ from the Batanin–Leinster operad equips $X$ with an $L$-algebra structure;

(c) explain why this is the directed, algebraic analogue of "a contractible topological space is an $\infty$-groupoid".

**Recall:**

A globular set $X$ is **contractible** when $X \to 1$ admits a [[Def - Contraction on a Globular Operad|contraction]]: for every $n$ and every parallel pair $\alpha^-, \alpha^+ \in X(n)$ there is a chosen $(n+1)$-cell with source $\alpha^-$, target $\alpha^+$. The **endomorphism operad** $\mathrm{End}(X)$ (from [[Ex - A globular operad map is determined by its action on operations]]) has $\mathrm{End}(X)(\pi) = \{\text{functions sending a labelling of } \pi \text{ to a cell of } X\}$; a $P$-algebra structure on $X$ is a globular-operad map $P \to \mathrm{End}(X)$. The **Batanin–Leinster operad** $(L, \chi)$ is the [[Thm - The Initial Contractible Globular Operad Exists|initial]] [[Def - Globular Operad|globular operad]]-with-contraction; a [[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)|weak ω-category]] is an $L$-algebra.

---

# Convergent Strategy

**Problem class:** This combines *algebra-construction* and *transport-via-initiality* from the topic page's problem-solving strategy. The route is to manufacture a contraction on $\mathrm{End}(X)$ from the contractibility of $X$, then use initiality of $L$ to map in, producing the $L$-algebra structure — the canonical recipe "contractible operad's algebras are weak $\omega$-categories", applied with $P = \mathrm{End}(X)$.

**Assumption pattern:** The key assumption is the contractibility of $X$: every parallel pair of cells has a filler. This is exactly the data needed to build a contraction on $\mathrm{End}(X)$ — a parallel pair of *operations* over a boundary, fed a labelling, produces a parallel pair of *cells* of $X$, which the contractibility of $X$ fills. Recognizing "contractibility of $X$ $\Rightarrow$ contraction on $\mathrm{End}(X)$" is the unlock.

**Theorem routing:** Route through three results in sequence: (i) the identity "$L$-algebra $=$ map $L \to \mathrm{End}(X)$" ([[Ex - A globular operad map is determined by its action on operations]]); (ii) the initiality of $L$ ([[Thm - The Initial Contractible Globular Operad Exists]]), giving a *unique* map $L \to (P, \chi')$ for any operad-with-contraction; (iii) the construction of a contraction $\chi'$ on $\mathrm{End}(X)$ from the contractibility of $X$. Chaining (iii) into (ii) into (i) yields the algebra structure.

**Key decision point:** The non-obvious choice is to build the contraction on $\mathrm{End}(X)$ *first* and only then invoke initiality, rather than trying to define the $L$-action by hand. The tempting alternative — directly specifying how each operation of $L$ acts on $X$ — would require reconstructing all of $L$'s coherence data; routing through "$\mathrm{End}(X)$ is contractible, so $L$ maps in uniquely" lets initiality do all the work for free.

---

# Legal Operations Used

1. **Operation 3 from the topic page (lift a parallel pair via a contraction).** Used to build the contraction on $\mathrm{End}(X)$: each parallel pair of operations, evaluated on a labelling, gives a parallel pair of cells of $X$, filled by $X$'s contractibility.

2. **Operation 4 from the topic page (take the initial object) and Operation 9 (pull back along an operad map).** Initiality of $L$ supplies the unique map $L \to \mathrm{End}(X)$, and pulling back the identity along it is the $L$-algebra structure.

3. **Operation 6 from the topic page (algebra $=$ map into $\mathrm{End}(X)$).** The bridge converting the operad map into an actual structure on $X$.

---

# Hints

> [!note]- Hint 1
> To equip $X$ with a weak $\omega$-category structure, you need a map $L \to \mathrm{End}(X)$. By initiality of $L$, you get one for free *as soon as* $\mathrm{End}(X)$ carries a contraction. So the real task is: build a contraction on $\mathrm{End}(X)$.

> [!note]- Hint 2
> A contraction on $\mathrm{End}(X)$ must lift a parallel pair of operations $(\Phi^-, \Phi^+)$ over $\partial\pi$ to an operation over $\pi$. An operation over $\partial\pi$ is a function "labelling $\mapsto$ cell of $X$". Feed both $\Phi^-, \Phi^+$ the *same* labelling $\lambda$: you get two parallel cells $\Phi^-(\lambda), \Phi^+(\lambda)$ of $X$.

> [!note]- Hint 3
> Now use contractibility of $X$: the parallel pair $\Phi^-(\lambda), \Phi^+(\lambda)$ has a chosen filler in $X$. Letting $\lambda$ vary, this defines an operation over $\pi$ — the desired lift. Check the source/target/shape conditions hold.

> [!note]- Hint 4
> For (c): a contractible *space* has the property that all its homotopy groups vanish, i.e. it is equivalent to a point and, regarded as an $\infty$-groupoid, has a unique cell up to higher cells in each dimension. A contractible *globular set* has "any two parallel cells joined by a cell above" — the directed, combinatorial mirror of "any two points joined by a path, any two paths by a homotopy, ...".

---

# Solution

The solution builds a contraction on $\mathrm{End}(X)$ from the contractibility of $X$ (Step 1), invokes initiality of $L$ to obtain the $L$-algebra structure (Step 2), and interprets the result homotopically (Step 3). The pivot is "feed both operations the same labelling, fill the resulting parallel pair of cells".

**Step 1: $\mathrm{End}(X)$ admits a contraction.**

> [!note]- Derivation
> We must supply, for each pasting diagram $\pi$ and each parallel pair $(\Phi^-, \Phi^+) \in \mathrm{Par}_{\mathrm{End}(X)}(\pi)$ of operations over $\partial\pi$, an operation $\chi'_\pi(\Phi^-, \Phi^+) \in \mathrm{End}(X)(\pi)$ with source $\Phi^-$, target $\Phi^+$, shape $\pi$.
>
> An operation $\Phi^\pm \in \mathrm{End}(X)(\partial\pi)$ is a function "labelling of $\partial\pi$ by $X$ $\mapsto$ cell of $X$". Fix a labelling $\lambda$ of $\pi$ by cells of $X$ (which restricts to a labelling of $\partial\pi$); evaluating gives two cells
> $$
> \Phi^-(\lambda), \ \Phi^+(\lambda) \in X(\dim\partial\pi),
> $$
> and these are **parallel** in $X$ because $\Phi^-, \Phi^+$ are parallel as operations (their sources and targets agree). Since $X$ is **contractible**, the unique map $X \to 1$ has a contraction, so this parallel pair has a chosen filler $\kappa\big(\Phi^-(\lambda), \Phi^+(\lambda)\big) \in X(\dim\pi)$ with source $\Phi^-(\lambda)$ and target $\Phi^+(\lambda)$. Define
> $$
> \chi'_\pi(\Phi^-, \Phi^+)(\lambda) := \kappa\big(\Phi^-(\lambda), \Phi^+(\lambda)\big).
> $$
> Letting $\lambda$ vary, this is a function "labelling of $\pi$ $\mapsto$ cell of $X$", i.e. an element of $\mathrm{End}(X)(\pi)$. By construction its source is $\Phi^-$, its target is $\Phi^+$, and its shape is $\pi$. So $\chi'$ is a contraction on $\mathrm{End}(X)$, and $(\mathrm{End}(X), \chi') \in \mathbf{OC}$.

**Step 2: initiality gives the $L$-algebra structure.**

> [!note]- Derivation
> By [[Thm - The Initial Contractible Globular Operad Exists|initiality of the Batanin–Leinster operad]] in $\mathbf{OC}$, there is a *unique* contraction-preserving operad map
> $$
> f : (L, \chi) \longrightarrow (\mathrm{End}(X), \chi').
> $$
> By the identity "$P$-algebra $=$ globular-operad map $P \to \mathrm{End}(X)$" ([[Ex - A globular operad map is determined by its action on operations]]), the operad map $f : L \to \mathrm{End}(X)$ *is* an $L$-algebra structure on $X$. Hence $X$ is an $L$-algebra — a weak $\omega$-category — and the structure is canonical because $f$ is the *unique* such map. Concretely, an operation $\theta \in L(\pi)$ acts on a labelling $\lambda$ by $\theta_X(\lambda) = f(\theta)(\lambda)$, and the coherence cells of $X$ are the fillers $\kappa$ supplied by its contractibility. So $\mathbf{X \text{ contractible} \implies X \text{ is canonically a weak } \omega\text{-category}}$.

**Step 3: the homotopy-hypothesis analogy.**

> [!note]- Derivation
> Contractibility of a globular set says: in every dimension, any two parallel cells are joined by a cell one dimension up. This is the directed, combinatorial mirror of contractibility of a topological space, where any two points are joined by a path, any two paths by a homotopy, any two homotopies by a higher homotopy, and so on — all the homotopy groups vanish. A contractible space, regarded as an $\infty$-groupoid (its fundamental $\infty$-groupoid), has a unique cell up to higher cells in each dimension; this exercise shows the *algebraic* counterpart: a contractible globular set is canonically a weak $\omega$-category (in fact a weak $\omega$-*groupoid*, since the fillers make every cell invertible up to higher cells). This is one finite-dimensional shadow of Grothendieck's **homotopy hypothesis**, that weak $\omega$-groupoids model homotopy types; the construction here is exactly how Leinster produces his examples of weak $\omega$-categories, and it shows the operadic definition is rich enough to absorb the homotopical content of contractibility.

> [!note]- Complete formal solution
> *(a)* For each $\pi$ and parallel pair $(\Phi^-,\Phi^+)\in\mathrm{Par}_{\mathrm{End}(X)}(\pi)$, and each labelling $\lambda$ of $\pi$, the cells $\Phi^-(\lambda),\Phi^+(\lambda)\in X$ are parallel; by contractibility of $X$ choose a filler $\kappa(\Phi^-(\lambda),\Phi^+(\lambda))$ and set $\chi'_\pi(\Phi^-,\Phi^+)(\lambda):=\kappa(\Phi^-(\lambda),\Phi^+(\lambda))$. This defines $\chi'_\pi(\Phi^-,\Phi^+)\in\mathrm{End}(X)(\pi)$ with source $\Phi^-$, target $\Phi^+$, shape $\pi$; so $\chi'$ is a contraction and $(\mathrm{End}(X),\chi')\in\mathbf{OC}$.
>
> *(b)* By initiality of $(L,\chi)$ there is a unique contraction-preserving operad map $f:L\to\mathrm{End}(X)$; by "$L$-algebra $=$ map $L\to\mathrm{End}(X)$", $f$ is a (canonical, since unique) $L$-algebra structure on $X$. Hence $X$ is a weak $\omega$-category.
>
> *(c)* Contractibility of a globular set ("parallel cells joined one dimension up, in every dimension") is the directed mirror of contractibility of a space ("points joined by paths, paths by homotopies, ..."); the construction makes $X$ a weak $\omega$-groupoid, the algebraic shadow of "a contractible space is an $\infty$-groupoid", a case of the homotopy hypothesis. $\blacksquare$

---

# Key Takeaways

**Initiality converts "the target is contractible" into "the source maps in for free".** The structural engine of this exercise is that, once $\mathrm{End}(X)$ is shown contractible, the *entire* $L$-algebra structure drops out of initiality with no further work — the unique map $L \to \mathrm{End}(X)$ is the structure. This is the canonical use of an initial object: to equip an object with structure, you do not build the structure directly; you show the target lives in the right category (here $\mathbf{OC}$) and let the universal property supply the unique map. The trigger: whenever you must put a "weak higher categorical structure of flavour $L$" on something, check whether its endomorphism operad is contractible — if so, you are done by initiality. This is the operadic version of "to act, exhibit a homomorphism into the endomorphisms", upgraded by the universal property.

**Contractibility of the object becomes contractibility of its endomorphism operad.** The technical heart is the transfer of contractibility from $X$ to $\mathrm{End}(X)$: a parallel pair of *operations*, evaluated on a common labelling, yields a parallel pair of *cells* of $X$, which $X$'s contractibility fills. This "evaluate the operations to reduce a contraction-on-operations to a contraction-on-cells" move is the bridge between the two contexts, and it is reusable whenever an operad is built from an object that itself has filling properties. The transferable diagnostic: filling conditions on an object propagate to filling conditions on its operad of operations, because operations are evaluated at the object. This is the algebraic mirror of "a fibration with contractible fibres induces filling on mapping spaces" in topology.

**A contractible globular set is a weak $\omega$-groupoid — the homotopy hypothesis in miniature.** Beyond the technical result, the conceptual payoff is that the abstract operadic definition is rich enough to capture the homotopical meaning of contractibility: the fillers make every cell of $X$ invertible up to higher cells, so $X$ is not just a weak $\omega$-category but a weak $\omega$-*groupoid*, the algebraic counterpart of a contractible space. This is the entry point to the deepest bridge of the chapter — Grothendieck's homotopy hypothesis that weak $\omega$-groupoids model homotopy types — and it shows why the Batanin–Leinster framework is the natural algebraic home for higher homotopy theory. See [[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)]] for the role of this construction in producing examples, and [[Ex - Strict omega-categories are weak omega-categories]] for the complementary embedding of the strict theory.

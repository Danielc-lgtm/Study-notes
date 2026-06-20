---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - The Slice of a Generalized Multicategory"
  - "Def - Opetope"
  - "Def - Initial and Terminal Object"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Using the slice construction, prove that the set of $2$-opetopes is in bijection with the natural numbers $\mathbb{N} = \{0, 1, 2, \dots\}$, one $2$-opetope for each arity. Do this by computing the objects of $I^{++}$ directly: identify the objects and operations of the identity operad $I = 1$, slice once to obtain $I^+$, and slice again to read off the objects of $I^{++}$, confirming they are exactly the "$n$ inputs, one output" cells.

**Recall:**

![[Def - The Slice of a Generalized Multicategory#The Definition]]

The **identity operad** $I = 1$ is the [[Def - Initial and Terminal Object|terminal]] operad: one object, exactly one operation in each arity $n = 0, 1, 2, \dots$. By [[Thm - Opetopes via Iterated Slicing of the Identity Operad|the iterated-slicing theorem]], $\mathcal{O}_n = \mathrm{ob}(I^{+\cdots+})$ ($n$ plus-signs). The [[Def - The Slice of a Generalized Multicategory|slice]] $C^+$ has objects = operations of $C$ and operations = pasting diagrams of operations of $C$.

---

# Convergent Strategy

**Problem class:** This is an *enumerate-the-cells-via-the-slice* problem — a combinatorial-world problem solved structurally rather than by drawing. The goal is to turn "how many $2$-opetopes are there?" into a direct computation of $\mathrm{ob}(I^{++})$ using the slice's defining property twice.

**Assumption pattern:** The crucial assumption is that $I$ is the *terminal* operad, which forces it to have exactly one operation in each arity (one input-list-length per operation, with no choices). This single fact is what makes the count clean: every layer of the computation is forced, so the bijection with $\mathbb{N}$ is not a coincidence but the image of "one operation per arity" climbing the tower.

**Theorem routing:** We route through the slice's defining property "objects of $C^+$ = operations of $C$" ([[Def - The Slice of a Generalized Multicategory|slice]]) applied to $C = I$ and then to $C = I^+$, and we confirm the answer against the enumeration corollary of [[Thm - Opetopes via Iterated Slicing of the Identity Operad|the iterated-slicing theorem]]. The terminality of $I$ comes from [[Def - Initial and Terminal Object|the terminal object]] characterisation.

**Key decision point:** The non-obvious choice is to recognise that the objects of $I^+$ are not "the arrow" alone but *one object per arity* (the operations of $I$), and that these arity-graded objects are precisely the $2$-opetopes once viewed as the cells of the next slice. The tempting error is to think slicing $I$ gives a single object (the arrow) and stop; in fact the operations of $I$ are arity-graded, and that grading is exactly the arity of the $2$-opetope.

---

# Legal Operations Used

1. **Operation 1 (slice a multicategory to climb one dimension)** from the topic page, applied twice: $I \rightsquigarrow I^+ \rightsquigarrow I^{++}$. We use the defining property "objects of $C^+$ = operations of $C$" at each step.

2. **Operation 8 (use that slicing preserves good ambient structure)** from the topic page, implicitly: we may slice $I$ and then slice $I^+$ because the slice of the (cartesian) identity operad is again sliceable.

---

# Hints

> [!note]- Hint 1
> First nail down $I$. As the terminal operad it has one object $\ast$ and, in each arity $n$, exactly one operation $\mu_n : (\ast, \dots, \ast) \to \ast$ ($n$ inputs). So the *operations* of $I$ are indexed by $n \in \mathbb{N}$.

> [!note]- Hint 2
> Apply "objects of $C^+$ = operations of $C$" to $C = I$. The objects of $I^+$ are the operations $\mu_n$ of $I$ — one for each arity $n$. So $\mathrm{ob}(I^+) \cong \mathbb{N}$.

> [!note]- Hint 3
> Now $\mathcal{O}_2 = \mathrm{ob}(I^{++})$, the objects of $I^{++}$, which are the *operations* of $I^+$. But you can also read $\mathcal{O}_2$ off as the objects of $I^{++}$ via the corollary: the relevant cells are the "$n$ source arrows, one target arrow" $2$-opetopes, one per arity, recovering $\mathbb{N}$.

---

# Solution

The route is two applications of the slice's defining property, anchored by the terminality of $I$. First we list the operations of $I$ (one per arity). Slicing once turns these into the objects of $I^+$. The $2$-opetopes are then the cells at the next level, arity-graded exactly as the operations of $I$ were.

**Step 1: The identity operad $I = 1$ has one operation per arity.**

> [!note]- Derivation
> $I = 1$ is the [[Def - Initial and Terminal Object|terminal]] operad. Terminality means: for every operad $P$ there is exactly one operad map $P \to I$. An operad map must send each $n$-ary operation of $P$ to an $n$-ary operation of $I$; for the map to be unique for *every* $P$, the target $I$ must have exactly one $n$-ary operation for each $n$ (if it had two, distinct maps could be built; if it had none, no map could exist). Hence $I$ has a single object $\ast$ and one operation $\mu_n : (\ast, \dots, \ast) \to \ast$ in each arity $n = 0, 1, 2, \dots$. The set of operations of $I$ is therefore in bijection with $\mathbb{N}$ via $\mu_n \mapsto n$.

**Step 2: The objects of $I^+$ are the operations of $I$, hence indexed by $\mathbb{N}$.**

> [!note]- Derivation
> By the defining property of the [[Def - The Slice of a Generalized Multicategory|slice]], an object of $I^+$ is an operation of $I$. By Step 1 the operations of $I$ are $\{\mu_n : n \in \mathbb{N}\}$, so
> $$\mathrm{ob}(I^+) \;=\; \{\text{operations of } I\} \;\cong\; \mathbb{N}.$$
> As cell shapes, the object $\mu_1$ (the unary operation) is the $1$-opetope, the arrow; the higher $\mu_n$ are the arity-$n$ inputs to the next level.

**Step 3: The $2$-opetopes are the arity-graded cells of $I^{++}$, in bijection with $\mathbb{N}$.**

> [!note]- Derivation
> By the [[Thm - Opetopes via Iterated Slicing of the Identity Operad|iterated-slicing theorem]], $\mathcal{O}_2 = \mathrm{ob}(I^{++})$, the objects of the second slice, equivalently the *operations* of $I^+$. An operation of $I^+$ is a pasting diagram of objects of $I^+$ composing to a single object of $I^+$. The $2$-opetope of arity $n$ is the operation whose source is $n$ copies of the arrow ($\mu_1$) and whose target is the arrow — i.e. the cell "$n$ arrows in, one arrow out." There is exactly one such for each $n$, because $I^+$ (inheriting the uniqueness from $I$ being terminal) has no choices in how the arrows are arranged beyond their number and order, and the order is fixed once $n$ is given for the standard cell. Hence
> $$\mathcal{O}_2 \;\cong\; \mathbb{N},$$
> one $2$-opetope per arity, matching the enumeration corollary. In particular $\mathcal{O}_2$ is countably infinite, in contrast to $|\mathcal{O}_0| = |\mathcal{O}_1| = 1$.

> [!note]- Complete formal solution
> $I = 1$ is the [[Def - Initial and Terminal Object|terminal]] operad, so it has one object and exactly one operation $\mu_n$ in each arity $n \in \mathbb{N}$; its operations are in bijection with $\mathbb{N}$.
>
> By the defining property of the [[Def - The Slice of a Generalized Multicategory|slice]] ("objects of $C^+$ = operations of $C$"), $\mathrm{ob}(I^+) = \{\mu_n : n \in \mathbb{N}\} \cong \mathbb{N}$.
>
> By the [[Thm - Opetopes via Iterated Slicing of the Identity Operad|iterated-slicing theorem]], $\mathcal{O}_2 = \mathrm{ob}(I^{++})$, the operations of $I^+$. The standard such operation of arity $n$ has source $n$ arrows and target one arrow; uniqueness for each $n$ follows from the terminality of $I$ (no choices propagate up the tower beyond arity and the fixed input order). Hence $\mathcal{O}_2 \cong \mathbb{N}$: exactly one $2$-opetope per arity, and $\mathcal{O}_2$ is countably infinite. $\blacksquare$

---

# Key Takeaways

**Terminality is what makes the opetope tower canonical and countable level by level.** The entire clean count rests on a single fact: $I$ is the terminal operad, so it has exactly one operation per arity, with no choices. That "no choices" property is what propagates up the slice tower and keeps each dimension's standard cells in clean bijection with a combinatorial set. The trigger to reach for terminality is any time you need a *canonical* generating object for an iterated construction: the terminal (or initial) object is the one with no arbitrary data, so the structure it generates is forced. This is the same reason initial algebras give canonical recursive datatypes and why the trivial group or the one-point space serve as canonical bases — the universal object carries no choices to pollute the construction.

**Slicing reads "operations" as "objects one level up", and arity grading survives the lift.** The computational heart of the exercise is applying "objects of $C^+$ = operations of $C$" mechanically, and the surprise it surfaces is that the *arity grading* of $I$'s operations becomes the arity grading of the $2$-opetopes. Whenever you slice, the grading and combinatorial structure of the operations become the grading and structure of the new objects — so to count the cells one dimension up, count the operations one dimension down. The trigger is any "how many $(n+1)$-cells?" question: convert it to "how many operations does the $n$-th slice have?" and the slice's defining property does the rest.

**An infinite single dimension is the fingerprint of opetopes, and it is forced, not optional.** This exercise proves rigorously what the drawing exercise observed: $\mathcal{O}_2$ is infinite, with one cell per arity. This is not an artifact of a presentation choice; it is forced by the slice construction applied to the terminal operad, because operations come in all arities. The reusable diagnostic is that any genuinely many-in, one-out framework will have infinitely many cells in dimension $2$ already, whereas a globular framework has exactly one $2$-cell shape. Seeing the infinitude appear from a clean computation, rather than from hand-drawn pictures, is what certifies that the opetopic and globular worlds are structurally different and not just notationally different. See [[Ex - Drawing the low-dimensional opetopes as trees]] for the pictorial companion and [[Ex - The slice of an ordinary category records factorisations]] for what the slice does to an arity-one multicategory.

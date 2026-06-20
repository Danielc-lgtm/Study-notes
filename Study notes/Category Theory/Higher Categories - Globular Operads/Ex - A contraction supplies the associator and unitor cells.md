---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Contraction on a Globular Operad"
  - "Def - Globular Operad"
  - "Def - 2-Category and Bicategory"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $L$ be the [[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)|Batanin–Leinster operad]], with its [[Def - Contraction on a Globular Operad|contraction]] $\chi$. Working in low dimensions, exhibit the **associator** and the **left/right unitors** of a [[Def - 2-Category and Bicategory|bicategory]] as contraction lifts:

(a) For the $1$-pasting diagram $\sigma_3$ of three composable $1$-cells, identify the two parallel bracketings $(\alpha^-, \alpha^+) \in \mathrm{Par}_L(\pi)$ over the boundary of a suitable $2$-pasting diagram $\pi$, and show $\chi_\pi(\alpha^-, \alpha^+)$ is the associator.

(b) For the unitors, identify the parallel pair "compose with the chosen identity" versus "do nothing", and show $\chi$ supplies the unitor cell.

(c) Explain why the *pentagon* relating different associators is itself a contraction lift one dimension up, so that no separate pentagon axiom is imposed.

**Recall:**

A [[Def - Contraction on a Globular Operad|contraction]] $\chi$ on a globular operad $P$ assigns, to each pasting diagram $\pi$ and each **parallel pair** $(\alpha^-, \alpha^+)$ of operations over the boundary $\partial\pi$ (so $\alpha^-, \alpha^+ \in P(\partial\pi)$ share source and target), an operation $\chi_\pi(\alpha^-, \alpha^+) \in P(\pi)$ with source $\alpha^-$, target $\alpha^+$, shape $\pi$. In a [[Def - 2-Category and Bicategory|bicategory]] the **associator** is an invertible $2$-cell $a_{h,g,f} : (h \circ g) \circ f \Rightarrow h \circ (g \circ f)$ and the **unitors** are invertible $2$-cells $\ell_f : 1_b \circ f \Rightarrow f$, $r_f : f \circ 1_a \Rightarrow f$, all subject to the pentagon and triangle coherence axioms. In $L$, the $1$-dimensional operations of arity $k$ are the $k$-leafed trees $\mathrm{tr}(k)$ — the unbiased ways to bracket a composite of $k$ arrows.

---

# Convergent Strategy

**Problem class:** This is a *recognition* exercise in the topic page's problem-solving strategy: locate, within the abstract operad $L$, the concrete coherence cells of a bicategory, by identifying them as contraction lifts. The route is "find the parallel pair, apply $\chi$".

**Assumption pattern:** The decisive assumption is that the $1$-dimensional operations of $L$ are the *trees* (bracketings) — so the two ways of composing three $1$-cells, $(hg)f$ and $h(gf)$, are *distinct* operations $\alpha^-, \alpha^+ \in L(\partial\pi)$ that are *parallel* (same overall source $0$-cell, same target). Recognizing "two bracketings $=$ a parallel pair" is the unlock; the associator is then forced to be their lift.

**Theorem routing:** Route through the definition of [[Def - Contraction on a Globular Operad|contraction]]: a parallel pair over $\partial\pi$ has a chosen lift in $L(\pi)$. For (c), route through the observation that the contraction operates in *every* dimension, so a parallel pair of associator-composites in dimension $2$ has a lift in dimension $3$ — which is the pentagon witness.

**Key decision point:** The non-obvious choice is to recognize that the associator's *source and target* are not cells of a category being defined but *operations of the operad* — the two bracketing operations — so that the associator lives in $L$, not in a particular algebra. The tempting alternative — thinking of the associator as a $2$-cell in a specific bicategory — obscures that $L$ supplies it *uniformly* for all bicategories at once, which is the whole point of the operadic approach.

---

# Legal Operations Used

1. **Operation 3 from the topic page (lift a parallel pair to a coherence cell via a contraction).** This is the exercise's entire content: associators, unitors, and the pentagon witness are all such lifts.

2. **Operation 8 from the topic page (enforce/observe tameness), in (c).** The pentagon's *equation* (rather than mere existence) is the dimension-$2$ shadow of tameness; the lift exists in dimension $3$, and in a weak $2$-category tameness collapses it to an equality.

---

# Hints

> [!note]- Hint 1
> The two ways to compose three $1$-cells $f, g, h$ are $(h \circ g) \circ f$ and $h \circ (g \circ f)$. As operations of $L$ in dimension $1$, these are *two different trees* — but they have the same source $0$-cell and the same target $0$-cell. What does "same source, same target, one dimension down" make them?

> [!note]- Hint 2
> They form a parallel pair $(\alpha^-, \alpha^+)$ over the boundary of a $2$-dimensional pasting diagram $\pi$ (the "globular $2$-cell from one bracketing to the other"). The contraction must lift them.

> [!note]- Hint 3
> $\chi_\pi(\alpha^-, \alpha^+) \in L(\pi)$ has source $(h\circ g)\circ f$ and target $h \circ (g \circ f)$ — that is exactly the associator $a_{h,g,f}$. For the unitors, take $\alpha^- =$ "compose $f$ with the chosen $0$-ary/identity operation" and $\alpha^+ =$ "the bare $f$".

> [!note]- Hint 4
> For the pentagon: two associators can be composed in two ways to relate the four-fold bracketings, and these two composites are a *parallel pair in dimension $2$*. The contraction, acting in dimension $3$, lifts them to a $3$-cell — the pentagonator. In a weak $2$-category there is no dimension $3$, so tameness forces this $3$-cell to be an *equality*: the pentagon axiom.

---

# Solution

The solution identifies the associator (Step 1) and unitors (Step 2) as contraction lifts in dimensions $1\to 2$, then identifies the pentagon as a lift in dimension $2 \to 3$ (Step 3), explaining why it needs no separate axiom. The pivot is "competing composites are parallel pairs; the contraction lifts them".

**Step 1: the associator is a contraction lift.**

> [!note]- Derivation
> In $L$, the $1$-dimensional operations of arity $3$ are the $3$-leafed trees $\mathrm{tr}(3)$ — the bracketings of a composite of three arrows. Two of these are
> $$
> \alpha^- = (h \circ g) \circ f, \qquad \alpha^+ = h \circ (g \circ f),
> $$
> both operations over the boundary $\partial\pi$ of a $2$-dimensional pasting diagram $\pi$ (the globular $2$-cell shape from the source $0$-cell to the target $0$-cell). They are **parallel**: they have the same source $0$-operation (the source endpoint) and the same target $0$-operation. Hence $(\alpha^-, \alpha^+) \in \mathrm{Par}_L(\pi)$, and the contraction supplies
> $$
> \chi_\pi(\alpha^-, \alpha^+) \in L(\pi), \qquad s(\chi_\pi) = (h\circ g)\circ f,\quad t(\chi_\pi) = h \circ (g\circ f).
> $$
> This operation, when performed in any $L$-algebra (any weak $\omega$-category, in particular any bicategory), is exactly the associator $a_{h,g,f} : (h\circ g)\circ f \Rightarrow h\circ(g\circ f)$. The contraction has *produced* the associator, uniformly, with no hand-specification.

**Step 2: the unitors are contraction lifts.**

> [!note]- Derivation
> The chosen identity on an object $a$ is the $0$-ary composition operation $1_a$ (the empty tree, the length-$0$ composite). The left unitor compares "first place an identity, then compose with $f$" against "just $f$". As operations of $L$ over the relevant boundary,
> $$
> \alpha^- = 1_b \circ f \quad (\text{the tree composing } f \text{ with the chosen identity}), \qquad \alpha^+ = f \quad (\text{the bare arrow}),
> $$
> which are parallel (same source and target $0$-cells). The contraction lifts them:
> $$
> \chi_{\pi'}(1_b \circ f,\ f) = \ell_f : 1_b \circ f \Rightarrow f,
> $$
> the left unitor. The right unitor $r_f : f \circ 1_a \Rightarrow f$ is the symmetric lift. So the unitors, like the associator, are contraction-supplied coherence cells, not separately-posited data.

**Step 3: the pentagon is a lift one dimension up.**

> [!note]- Derivation
> Consider four composable $1$-cells $k, h, g, f$. Reassociating from $((kh)g)f$ to $k(h(gf))$ can be done along two routes through the five bracketings, each route a composite of associator $2$-cells. These two composite $2$-cells are *parallel* — same source bracketing $((kh)g)f$, same target $k(h(gf))$ — so they form a parallel pair *in dimension $2$*, over the boundary of a $3$-dimensional pasting diagram. The contraction, which acts in **every** dimension, lifts this pair to a $3$-cell
> $$
> \chi_{\pi''}\big(\text{route}_1,\ \text{route}_2\big) \in L(\pi''),
> $$
> the **pentagonator**, witnessing the two routes as equivalent. Crucially, no separate "pentagon axiom" was imposed: the same closure condition "every parallel pair lifts" that produced the associator produces the cell relating different associators. This is the central economy of the contraction — the entire coherence tower is generated by one rule. In a weak *$2$*-category, however, there is no dimension $3$ to house this lift; **tameness** in the top dimension $2$ then forces the two routes to be *equal*, which is exactly the bicategory pentagon *equation*. So the pentagon is an axiom in the hand-written definition precisely because, with no room above, the dimension-$3$ coherence collapses to an equality.

> [!note]- Complete formal solution
> In $L$ the arity-$3$ one-dimensional operations are the trees $\mathrm{tr}(3)$; the bracketings $\alpha^-=(h\circ g)\circ f$ and $\alpha^+=h\circ(g\circ f)$ are parallel over the boundary of a $2$-pasting diagram $\pi$, so $\chi_\pi(\alpha^-,\alpha^+)\in L(\pi)$ has source $\alpha^-$, target $\alpha^+$ — the associator $a_{h,g,f}$. Taking $\alpha^-=1_b\circ f$, $\alpha^+=f$ (parallel) gives $\chi(\cdot)=\ell_f$, the left unitor; symmetrically the right unitor. For four cells, the two associator-routes from $((kh)g)f$ to $k(h(gf))$ are a parallel pair in dimension $2$, lifted by $\chi$ to a $3$-cell (the pentagonator) — generated by the same closure, hence no separate pentagon axiom. In a weak $2$-category, top-dimensional tameness equates the two routes, recovering the pentagon equation. $\blacksquare$

---

# Key Takeaways

**Competing composites are parallel pairs, and every coherence cell is their lift.** The reusable principle, and the conceptual heart of the whole chapter, is the equation "coherence cell $=$ contraction lift of a parallel pair". Two different ways of composing the same diagram are two operations over the same boundary, hence parallel, hence lifted by the contraction to a witnessing cell one dimension up. This single recognition produces associators (two bracketings of three cells), unitors (composite-with-identity versus bare cell), interchangers (two orders of composing a $2\times 2$ grid), and every higher coherence. The trigger to deploy it: whenever you must produce a coherence isomorphism, ask "what are the two competing composites, and over what boundary are they parallel?" — then the cell is $\chi$ of that pair. This is why the contraction is the entire source of weakness *and* coherence at once.

**The coherence tower is generated by one closure, dimension by dimension.** Part (c) shows the deepest economy: the pentagon, which the hand-written definition imposes as a separate axiom, is *automatically* a contraction lift one dimension above the associators. Coherence-of-coherence is the same operation as coherence, applied one floor up. So the infinite tower of coherence data — associators, the pentagon, the pentagon's own coherence, and so on forever — is compressed into the single rule "every parallel pair lifts". The transferable lesson is that an apparently endless list of axioms can sometimes be replaced by one closure condition that regenerates the whole list at successive levels; recognizing such a generating rule is what makes the difference between a definition that fits on a line and one that does not.

**Hand-written coherence axioms are tameness in disguise.** The pentagon appears as an *equation* in a bicategory because a bicategory is a weak *$2$*-category, with no dimension $3$ to receive the pentagonator; top-dimensional tameness then forces the two associator-routes to be literally equal. So the classical coherence axioms are not arbitrary impositions — they are the shadow, in the top dimension, of contraction lifts that *would* exist one dimension higher in an $\omega$-category. This reframes "all coherence diagrams commute" (Mac Lane, bicategory coherence) as a structural consequence of running out of room, exactly as developed in [[Thm - Weak 2-Categories are Bicategories]]. See [[Ex - Why finite-dimensional contractions need tameness]] for the precise role of tameness, and [[Def - Contraction on a Globular Operad]] for the lift mechanism in full generality.

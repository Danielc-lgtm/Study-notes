---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Globular Operad"
  - "Def - The Free Strict ω-Category Monad"
  - "Def - Algebra for a Monad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $1 \xrightarrow{!} T1$ be the **terminal globular operad** over the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] $T$, where $1$ is the terminal globular set. Show that an algebra for $1$ is precisely a **strict $\omega$-category**:
$$
\mathrm{Alg}(1) \cong \mathbf{Str\text{-}\omega\text{-}Cat}.
$$
Do this by unwinding a $1$-algebra structure on a globular set $X$ and exhibiting it as "exactly one composite for every labelled pasting diagram, associatively and unitally".

**Recall:**

A [[Def - Globular Operad|globular operad]] is a collection $P \xrightarrow{d} T1$ (with $d$ cartesian) carrying associative, unital operadic composition and units; its fibre $P(\pi) = d^{-1}(\pi)$ is the set of operations of shape $\pi$. The **terminal globular operad** is $1 \xrightarrow{!} T1$ with $1$ the terminal globular set, so every fibre $1(\pi) = \{\ast\}$ is a singleton: one operation per shape. An [[Def - Algebra for a Monad|algebra]] for a globular operad $P$ is a globular set $X$ with an action assigning to each pasting diagram $\pi$, operation $\theta \in P(\pi)$, and labelling of $\pi$ by cells of $X$ a composite cell, naturally and compatibly with operadic composition and units; equivalently an algebra for the induced monad $T_P$. A **strict $\omega$-category** is a globular set with a strictly associative, unital, interchange-respecting composition in every dimension, along every boundary — equivalently a $T$-algebra.

---

# Convergent Strategy

**Problem class:** This is an *algebra-identification* problem in the sense of the topic page's problem-solving strategy: given an explicit operad (the terminal one), determine $\mathrm{Alg}(P)$. The route is the standard one — unwind the action, then recognize the result as a known doctrine. Here the recognition target is the strict $\omega$-categories.

**Assumption pattern:** The decisive assumption is that every fibre of the terminal operad is a *singleton*: $1(\pi) = \{\ast\}$. This means the operation $\theta$ in the action data carries no information — there is exactly one choice for each shape — so the action reduces to "a composite for every labelling of every shape", with no choice of *which* operation. Recognizing "singleton fibres $\implies$ the action is just one composite per shape" is the unlock.

**Theorem routing:** Route through the identity "$P$-algebra $=$ map $P \to \mathrm{End}(X)$" (from [[Def - Globular Operad]]) and through the induced-monad description "$P$-algebra $=$ $T_P$-algebra". For the terminal operad the induced monad $T_1$ is $T$ itself, so $\mathrm{Alg}(1) = \mathrm{Alg}(T) = \mathbf{Str\text{-}\omega\text{-}Cat}$ — but the *content* is in seeing why $T_1 = T$, which the unwinding provides.

**Key decision point:** The non-obvious choice is whether to argue abstractly ($T_1 = T$, done) or concretely (unwind the action and match the strict-$\omega$-category axioms). The exercise asks for the concrete route because it reveals *why* the operad axioms become the strict-category axioms — associativity of operadic composition becomes associativity of composites, units become identities — which the abstract one-liner hides. The tempting shortcut "$T_1 = T$ so we are done" is correct but pedagogically empty; the unwinding is the point.

---

# Legal Operations Used

1. **Operation 6 from the topic page (identify an operad's algebras by unwinding the action).** This is the central operation of the exercise: take "$X$ is a $1$-algebra", unwind it to "a chosen composite per labelled shape", and recognize it.

2. **Operation 9 from the topic page (pull a structure back along an operad map), implicitly.** The terminal operad receives a unique map from any operad; recognizing $1$'s algebras as $T$-algebras is the base case for transporting any contractible operad's algebras into weak $\omega$-categories.

---

# Hints

> [!note]- Hint 1
> What does the action data look like when the operad has exactly one operation per shape? The "$\theta \in P(\pi)$" part of the action becomes vacuous — there is nothing to choose.

> [!note]- Hint 2
> So a $1$-algebra structure on $X$ is: for each pasting diagram $\pi$ and each labelling of $\pi$ by cells of $X$, a single composite cell of $X$. That is *exactly* an action $TX \to X$ of the monad $T$. Why?

> [!note]- Hint 3
> Recall from [[Ex - Pasting diagrams as labelled composites]] that an element of $TX$ is a labelled pasting diagram. A map $TX \to X$ assigns a cell of $X$ to each labelled pasting diagram — which is precisely "one composite per labelled shape".

> [!note]- Hint 4
> The operad axioms (associativity and unitality of operadic composition) translate into the monad-algebra axioms (compatibility with $\mu$ and $\eta$), which *are* the strict associativity and unitality of composition. Match them clause by clause.

---

# Solution

The solution unwinds the $1$-algebra structure (Step 1), identifies it with a $T$-algebra (Step 2), and matches the axioms with the strict-$\omega$-category axioms (Step 3). The pivot is that singleton fibres reduce the operadic action to a bare monad action.

**Step 1: the action data collapses to one composite per labelled shape.**

> [!note]- Derivation
> A $1$-algebra structure on a globular set $X$ assigns, to each pasting diagram $\pi$, each operation $\theta \in 1(\pi)$, and each labelling $\lambda$ of $\pi$ by cells of $X$, a composite cell $\theta_X(\lambda) \in X(\dim \pi)$. But $1(\pi) = \{\ast\}$ is a singleton, so $\theta$ ranges over a one-element set and carries no information. The action data therefore reduces to: for each pasting diagram $\pi$ and each labelling $\lambda$ of $\pi$ by $X$, a single composite cell $\ast_X(\lambda) \in X$. There is no *choice* of operation — exactly one composite is prescribed for each labelled shape.

**Step 2: this is exactly a $T$-algebra structure.**

> [!note]- Derivation
> By [[Ex - Pasting diagrams as labelled composites]], an element of $(TX)(m)$ *is* a labelled pasting diagram $(\pi, \lambda)$ of dimension $m$. The data "a composite cell for each labelled pasting diagram" is therefore a function
> $$
> a : TX \longrightarrow X, \qquad a(\pi, \lambda) = \ast_X(\lambda),
> $$
> i.e. a map of globular sets from $TX$ to $X$. Concretely, the induced monad $T_1$ of the terminal globular operad is $T$ itself (the terminal operad imposes no constraint beyond the free strict structure), so a $1$-algebra is a $T_1$-algebra $=$ $T$-algebra. Thus a $1$-algebra is a globular set $X$ with an action map $a : TX \to X$.

**Step 3: the axioms match the strict-$\omega$-category axioms.**

> [!note]- Derivation
> A $T$-algebra must satisfy the two [[Def - Algebra for a Monad|monad-algebra laws]]:
> $$
> a \circ \eta_X = \mathrm{id}_X \qquad (\text{unit law}), \qquad a \circ \mu_X = a \circ T a \qquad (\text{associativity law}).
> $$
> The **unit law** says: composing a single cell (the labelled pasting diagram $\eta_X(x)$, which is "$x$ on its own, no composition") returns $x$. This is exactly the statement that identities act as identities — the unitality of composition in a strict $\omega$-category. The **associativity law** says: given a labelled pasting-diagram-of-(labelled pasting diagrams) — an element of $T^2 X$ — first composing the inner diagrams and then the outer ($a \circ Ta$) gives the same cell as flattening to one big labelled pasting diagram and composing once ($a \circ \mu_X$). This is precisely strict associativity *and* the interchange law of composition: any way of bracketing a multi-stage composite yields the same result. These two laws are *exactly* the defining axioms of a strict $\omega$-category (a globular set with strictly associative, unital, interchange-respecting composition in every dimension), so $1$-algebras are strict $\omega$-categories, and the correspondence is an isomorphism of categories
> $$
> \mathrm{Alg}(1) \cong \mathbf{Str\text{-}\omega\text{-}Cat}. \qquad \blacksquare
> $$
> (Morphisms match too: a map of $1$-algebras is a globular-set map commuting with the action, which is exactly a strict $\omega$-functor.)

> [!note]- Complete formal solution
> The terminal globular operad $1 \xrightarrow{!} T1$ has $1(\pi) = \{\ast\}$ for every pasting diagram $\pi$. Hence a $1$-algebra structure on a globular set $X$ — a priori an assignment of a composite to each $(\pi, \theta, \lambda)$ — has $\theta$ ranging over a singleton, so it collapses to: a composite cell for each pasting diagram $\pi$ and labelling $\lambda$ of $\pi$ by $X$. By the labelled-pasting-diagram description of $TX$ (an element of $TX$ is exactly such a $(\pi,\lambda)$), this is a globular-set map $a : TX \to X$; equivalently, the induced monad $T_1$ of the terminal operad is $T$, so a $1$-algebra is a $T$-algebra. The monad-algebra laws $a\circ\eta_X = \mathrm{id}_X$ and $a\circ\mu_X = a\circ Ta$ are, respectively, the unitality (identities act as identities) and the strict associativity-with-interchange (all bracketings of a multi-stage composite agree) of composition. These are the defining axioms of a strict $\omega$-category, and morphisms correspond to strict $\omega$-functors, so $\mathrm{Alg}(1) \cong \mathbf{Str\text{-}\omega\text{-}Cat}$. $\blacksquare$

---

# Key Takeaways

**Singleton fibres mean "no choice of operation", which is exactly strictness.** The reusable insight is that the *size* of an operad's fibres measures how much choice its algebras have in composing. The terminal operad has one-point fibres, so there is exactly one composite per shape — no associators, no alternatives — which is the algebraic content of *strictness*. Enlarging the fibres (as a contraction does) introduces multiple operations per shape, hence weak composites and coherence cells. This "fibre size $=$ amount of weakness" dictionary is the trigger for predicting an operad's algebras: count the fibres. One operation per shape gives strict structures; a contractible (large) fibre gives weak ones. It is the cleanest way to see why the same monad $T$ supports both the strict and the weak theory — the difference is entirely in the operad sitting over $T1$.

**Operad axioms become composition axioms under the algebra functor.** Unwinding the action shows the dictionary explicitly: operadic *unitality* becomes "identities act as identities", and operadic *associativity* becomes "all bracketings of a composite agree (associativity plus interchange)". This is the general mechanism by which $\mathrm{Alg}(P)$ inherits its axioms from $P$ — the structure of the operad is transported, clause by clause, onto the structure of the algebras. The transferable diagnostic: to find the axioms a doctrine $\mathrm{Alg}(P)$ satisfies, read off the operad axioms of $P$ and translate "operation" to "composite". This is exactly how, in [[Thm - Weak 2-Categories are Bicategories]], the tree-generated structure of $L_2$ plus top-dimensional tameness becomes the associator/unitor/pentagon structure of a bicategory.

**Identifying $\mathrm{Alg}(1) = \mathbf{Str\text{-}\omega\text{-}Cat}$ is the base camp for the whole weak theory.** This identification is not just a sanity check; it is the anchor of the chapter's central construction. Because $1$ is *terminal* in operads-with-contraction (it carries a unique trivial contraction), the unique map $L \to 1$ from the initial operad induces $\mathbf{Str\text{-}\omega\text{-}Cat} = \mathrm{Alg}(1) \to \mathbf{Wk\text{-}\omega\text{-}Cat}$, embedding strict $\omega$-categories into weak ones. So knowing concretely what $1$-algebras are is what lets you see strict $\omega$-categories as the special weak ones with identity coherence cells. The companion exercise [[Ex - Strict omega-categories are weak omega-categories]] completes this picture by showing the embedding is full and faithful, and [[Ex - A globular operad map is determined by its action on operations]] supplies the "$P$-algebra $=$ map into $\mathrm{End}(X)$" identity used throughout.

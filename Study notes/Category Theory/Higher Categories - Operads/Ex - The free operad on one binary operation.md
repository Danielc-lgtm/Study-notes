---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Free Operad"
  - "Def - Operad"
  - "Def - Algebra for an Operad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $E$ be the (non-symmetric) sequence with one generator in arity $2$ and nothing else: $E(2) = \{\mu\}$, $E(n) = \varnothing$ for $n \neq 2$. 

(a) Describe the free non-symmetric [[Def - Operad|operad]] $\mathcal{F}(E)$ explicitly: show $\mathcal{F}(E)(n)$ is the set of *planar binary trees* with $n$ leaves, and that operadic composition is grafting. Compute $\mathcal{F}(E)(1), \mathcal{F}(E)(2), \mathcal{F}(E)(3)$ and the cardinalities $|\mathcal{F}(E)(n)|$.

(b) Identify the algebras over $\mathcal{F}(E)$ as **magmas** (sets with one binary operation, no axioms), and describe the free $\mathcal{F}(E)$-algebra on a set $S$ as the set of binary bracketings of words in $S$.

(c) Obtain the (non-symmetric) associative operad $\mathrm{Assoc}^{\mathrm{ns}}$ as a quotient $\mathcal{F}(E)/R$, where $R$ imposes associativity, and explain in tree terms what the quotient does.

**Recall:**

![[Thm - The Free Operad#Statement]]

A **planar binary tree** with $n$ leaves is a rooted tree drawn in the plane, every internal vertex having exactly two children (a left and a right), with $n$ leaves at the top. A **magma** is a set with a binary operation $X \times X \to X$ subject to no equations.

---

# Convergent Strategy

**Problem class:** This is a *compute-the-free-object-explicitly* problem, applying [[Thm - The Free Operad|the free operad theorem]] to the simplest non-trivial generator and reading off the combinatorics. The method: instantiate the tree description for a single binary generator, then translate to algebras and to a presentation of a familiar operad.

**Assumption pattern:** The signal is "one binary generator, no relations". With a single arity-$2$ generator, the only trees are *binary* trees (every vertex has the unique generator, hence two inputs), and "no relations" means distinct trees stay distinct — so $\mathcal{F}(E)(n)$ is literally the set of binary trees with $n$ leaves, counted by Catalan numbers. The non-symmetric (planar) setting is signalled by the absence of an $S_n$-action.

**Theorem routing:** Part (a) routes through the tree formula $\mathcal{F}(E)(n) = \coprod_{T} \bigotimes_v E(|v|)$: since $E$ is concentrated in arity $2$, only trees with all vertices of arity $2$ survive, i.e. binary trees, and each contributes a single point (one labelling). Part (b) routes through "algebras over a free operad are algebras over the generators with no relations": a $\mathcal{F}(E)$-algebra is a set with one binary operation, a magma. Part (c) routes through the presentation $\mathrm{Assoc}^{\mathrm{ns}} = \mathcal{F}(E)/(\mu\circ_1\mu = \mu\circ_2\mu)$.

**Key decision point:** The crux of (a) is recognising that "one binary generator" forces *binary* trees specifically (not all trees), because every internal vertex must be decorated by the unique arity-$2$ generator and therefore has exactly two children. The temptation is to count all planar trees; the correct count is Catalan, $|\mathcal{F}(E)(n)| = C_{n-1} = \frac{1}{n}\binom{2n-2}{n-1}$. In (c), the decision is to see the quotient as *collapsing all binary trees with the same number of leaves to one element* — that is exactly imposing associativity.

---

# Legal Operations Used

1. **Instantiate the free-operad tree formula at a specific generator (operation 6 from the topic page).** We specialise $\mathcal{F}(E)(n) = \coprod_T \dots$ to a single binary generator, getting binary trees.

2. **Read algebras over a free operad as generators-with-no-relations (operation 4 from the topic page).** A $\mathcal{F}(E)$-algebra is a magma.

3. **Present a quotient operad by imposing relations (operation 2 from the topic page).** We form $\mathcal{F}(E)/R$ to get $\mathrm{Assoc}^{\mathrm{ns}}$.

---

# Hints

> [!note]- Hint 1
> Every internal vertex of a tree contributing to $\mathcal{F}(E)(n)$ must carry a generator from $E$; since $E$ only has the arity-$2$ generator $\mu$, every vertex has exactly $2$ children. So the trees are binary.

> [!note]- Hint 2
> $\mathcal{F}(E)(1)$ is the trivial tree (one leaf, no vertices) — one element. $\mathcal{F}(E)(2) = \{\mu\}$ — one binary tree. $\mathcal{F}(E)(3)$ has two trees: $\mu(\mu(-,-), -)$ and $\mu(-, \mu(-,-))$ — the two bracketings of three leaves.

> [!note]- Hint 3
> The number of planar binary trees with $n$ leaves is the Catalan number $C_{n-1}$: $1, 1, 2, 5, 14, \dots$ for $n = 1, 2, 3, 4, 5$. They satisfy $C_{n-1} = \sum_{i} C_{i-1} C_{n-1-i}$ from splitting at the root.

> [!note]- Hint 4
> For (c): associativity says the two trees in $\mathcal{F}(E)(3)$ are identified. Once identified, all binary trees with $n$ leaves become equal (any two are connected by re-bracketings = associativity moves), so $\mathrm{Assoc}^{\mathrm{ns}}(n) = \{*\}$.

---

# Solution

The plan: specialise the tree formula to a binary generator and count (Step 1); identify magmas as the algebras and the free magma as bracketed words (Steps 2–3); present $\mathrm{Assoc}^{\mathrm{ns}}$ by the associativity relation and interpret the quotient on trees (Step 4).

**Step 1: $\mathcal{F}(E)(n) =$ planar binary trees, counted by Catalan numbers.**

> [!note]- Derivation
> By [[Thm - The Free Operad|the free operad theorem]], $\mathcal{F}(E)(n) = \coprod_{T : n \text{ leaves}} \prod_{v \in T} E(|v|)$ over (planar, since non-symmetric) rooted trees. The factor $E(|v|)$ is non-empty only when $|v| = 2$, and then it is the single point $\{\mu\}$. So the only contributing trees have every internal vertex of arity $2$ — planar binary trees — and each contributes exactly one element (the all-$\mu$ labelling). Hence $\mathcal{F}(E)(n) = \{$planar binary trees with $n$ leaves$\}$. Computing: $\mathcal{F}(E)(1) = \{|\}$ (trivial tree, the unit), one element; $\mathcal{F}(E)(2) = \{\mu\}$, one element; $\mathcal{F}(E)(3) = \{\mu(\mu, \mathrm{id}), \mu(\mathrm{id}, \mu)\}$, the two bracketings, two elements; $\mathcal{F}(E)(4)$ has five. In general $|\mathcal{F}(E)(n)| = C_{n-1}$, the $(n-1)$th Catalan number, satisfying the splitting recursion $C_{n-1} = \sum_{i=1}^{n-1} C_{i-1} C_{n-1-i}$ (split the tree at its root into left subtree with $i$ leaves and right with $n - i$). Grafting trees onto leaves is operadic composition.

**Step 2: Algebras are magmas.**

> [!note]- Derivation
> By the universal property of the free operad, an operad map $\mathcal{F}(E) \to \mathrm{End}_X$ is the same as a map of sequences $E \to U(\mathrm{End}_X)$, i.e. a choice of one element of $\mathrm{End}_X(2) = \mathrm{Hom}(X^2, X)$ — a single binary operation $m : X^2 \to X$, with *no constraints* (there are no relations in $E$). So a $\mathcal{F}(E)$-algebra is exactly a set $X$ with one binary operation: a **magma**. The higher operations of the algebra are forced: the tree $\mu(\mu, \mathrm{id})$ acts as $(x,y,z) \mapsto m(m(x,y), z)$, the tree $\mu(\mathrm{id}, \mu)$ as $(x,y,z)\mapsto m(x, m(y,z))$, and these are generally *different* (no associativity), matching the two distinct elements of $\mathcal{F}(E)(3)$.

**Step 3: The free magma on $S$.**

> [!note]- Derivation
> The free $\mathcal{F}(E)$-algebra on a set $S$ is $T_{\mathcal{F}(E)}(S) = \coprod_n \mathcal{F}(E)(n) \times S^n$ (non-symmetric, no $S_n$-quotient): an element is a planar binary tree with its $n$ leaves labelled by elements of $S$ — that is, a fully-bracketed non-empty word in $S$, such as $((s_1 s_2)(s_3 (s_4 s_5)))$. The binary operation is concatenation-with-a-new-root: $w_1 \cdot w_2$ is the tree with root $\mu$, left subtree $w_1$, right subtree $w_2$. This is exactly the **free magma** on $S$ — all binary bracketings of words, with no simplification because there are no relations.

**Step 4: Quotient to $\mathrm{Assoc}^{\mathrm{ns}}$.**

> [!note]- Derivation
> Impose the associativity relation $R$: the two elements of $\mathcal{F}(E)(3)$ are identified, $\mu \circ_1 \mu = \mu \circ_2 \mu$ (i.e. $\mu(\mu, \mathrm{id}) \sim \mu(\mathrm{id}, \mu)$). Form the quotient operad $\mathcal{F}(E)/R$ (the smallest operadic congruence containing $R$). In tree terms, $R$ says "a left-leaning binary caret equals the right-leaning one"; propagating this through grafting, *any* two planar binary trees with the same number of leaves become identified, because any two bracketings of $n$ symbols are connected by a sequence of associativity moves (rotations). Hence $(\mathcal{F}(E)/R)(n)$ has exactly one element for each $n \geq 1$: this is the non-symmetric associative operad $\mathrm{Assoc}^{\mathrm{ns}}(n) = \{*\}$, whose algebras are (non-unital, or unital with an added nullary generator) semigroups/monoids. The quotient is the operadic incarnation of "associativity makes all bracketings equal".

> [!note]- Complete formal solution
> *(a)* By the free-operad tree formula with $E$ concentrated at arity $2$, $\mathcal{F}(E)(n)$ is the set of planar binary trees with $n$ leaves (every vertex carrying the unique binary $\mu$), with grafting as composition. $|\mathcal{F}(E)(n)| = C_{n-1}$ (Catalan), with $\mathcal{F}(E)(1), \mathcal{F}(E)(2), \mathcal{F}(E)(3)$ of sizes $1, 1, 2$.
>
> *(b)* By the universal property, a $\mathcal{F}(E)$-algebra is a set with one unconstrained binary operation — a magma. The free $\mathcal{F}(E)$-algebra on $S$ is the set of $S$-labelled planar binary trees, the free magma (all binary bracketings of words in $S$).
>
> *(c)* Imposing $\mu\circ_1\mu = \mu\circ_2\mu$ identifies all binary trees of equal leaf-count, giving $\mathrm{Assoc}^{\mathrm{ns}}(n) = \{*\}$; the quotient is associativity collapsing all bracketings. $\blacksquare$

---

# Key Takeaways

**Free operad = trees; the generator's arity dictates the branching.** The headline lesson is that the free operad on a sequence of generators is the operad of *labelled trees*, and the arities of the generators determine the allowed branching. One binary generator gives binary trees (Catalan); one ternary generator gives ternary trees (Fuss–Catalan); a mix gives mixed-arity trees. This is the operadic generalisation of "the free monoid is words" — words are height-one linear trees, and genuine branching appears exactly when operations have more than one input. Whenever you need the free structure of a given algebraic type, the move is: find the generators, build the labelled trees, and *that* is the free operad; the free algebra is then the trees with elements at the leaves.

**No relations means distinct trees stay distinct; relations collapse them.** The contrast between (a) and (c) is the cleanest illustration of how presentations work. The free operad keeps every tree separate ($C_{n-1}$ of them in arity $n$); imposing associativity collapses all binary trees of a fixed leaf-count to a single point. This "collapse to a normal form" is the universal-algebra content of a relation, and recognising it lets you read a presentation $\langle \text{generators} \mid \text{relations}\rangle$ as "trees modulo the rewriting the relations generate". The Catalan-to-one collapse is the operadic shadow of the classical fact that associativity makes bracketing irrelevant — and the *failure* of that collapse (binary trees up to associativity but tracking the homotopies of the collapse) is exactly the $A_\infty$-operad, where the associahedra organise the bracketings.

**The Catalan/associahedron combinatorics is not a coincidence — it is the homotopy theory of associativity.** The two trees in $\mathcal{F}(E)(3)$ that get identified by associativity are the two vertices of an interval (the $1$-dimensional associahedron $K_3$); the five trees in $\mathcal{F}(E)(4)$ are the vertices of the pentagon $K_4$. When one resolves $\mathrm{Assoc}$ up to homotopy rather than imposing associativity strictly, these polytopes — Stasheff's associahedra — record the higher associativity homotopies, and a $\mathcal{F}(E)$-algebra "up to coherent homotopy" is an $A_\infty$-algebra. So the free operad on one binary operation is the doorway to the entire theory of homotopy-associative structures: the strict quotient gives monoids, the homotopical resolution gives $A_\infty$-spaces, and the difference is exactly the geometry of the associahedra that this exercise's trees enumerate.

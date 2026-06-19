---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
  - "Def - Group"
tags: [category-theory, foundations]
---

# Notation

A groupoid is a [[Def - Category|category]] $\mathcal{G}$ in which every morphism is invertible. We keep the category notation: objects $A, B, x, y$; morphisms $f, g$; composition $g \circ f$; identity $1_A$; the inverse of $f$ is $f^{-1}$. For a [[Def - Group|group]] $G$, $\mathbf{B}G$ denotes the one-object groupoid built from it. For a [[Def - Topological Space|topological space]] $X$, $\Pi_1(X)$ denotes its fundamental groupoid. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

A [[Def - Group|group]] is the algebra of *reversible* transformations, but it carries a hidden assumption: that all the transformations act on **one and the same thing**. The symmetries of a square all permute the same four corners; the integers under addition all act on the same line. But many natural situations are reversible without being single-object. Consider the paths in a space: a path from $x$ to $y$ can be reversed to a path from $y$ to $x$, and paths compose when the endpoints match — yet a path from $x$ to $y$ and a path from $y'$ to $z$ with $y \neq y'$ do not compose at all. This is reversibility with *typing*: every arrow has an inverse, but composition is partial because arrows live between different objects. A group cannot express it; a groupoid can.

So the motivation is to keep the one good axiom of a group — every element is invertible — while dropping the artificial restriction to a single object. **What you get by adding objects to a group is exactly a groupoid**, and what you get by collapsing a groupoid to one object is a group. The defining axiom is therefore not new: it is the [[Def - Group|group]] invertibility axiom, re-imposed on a [[Def - Category|category]]. A category already supplies associative, unital composition; demanding that every morphism be an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]] supplies the inverses.

What breaks if we *only* demand that every morphism be mono and epi, rather than iso? In a general category that is strictly weaker (see [[Def - Isomorphism, Monomorphism, Epimorphism]]): a continuous bijection or the inclusion $\mathbb{Z} \hookrightarrow \mathbb{Q}$ is mono and epi without being invertible. We genuinely need *two-sided invertibility* — an actual inverse arrow — for the reverse-a-path intuition to hold, and that is the iso condition, not the cancellability condition.

---

# The Definition

A **groupoid** is a [[Def - Category|category]] $\mathcal{G}$ in which every morphism is an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]]: for each $f : A \to B$ there is $f^{-1} : B \to A$ with $f^{-1} \circ f = 1_A$ and $f \circ f^{-1} = 1_B$.

Equivalently, a groupoid is a set (or class) of objects together with, for each pair $(A, B)$, a set $\mathcal{G}(A, B)$ of arrows, an associative partial composition, identities, and an inversion operation $\mathcal{G}(A, B) \to \mathcal{G}(B, A)$ satisfying the two inverse laws. For each object $A$, the hom-set $\mathcal{G}(A, A)$ is a [[Def - Group|group]] under composition, the **vertex group** (or automorphism group) at $A$, denoted $\mathrm{Aut}_{\mathcal{G}}(A)$.

---

# Categorical / Structural Definition

A groupoid is the special case of a [[Def - Category|category]] obtained by requiring invertibility, so it has no separate structural definition — but the relationship in the other direction is illuminating. A [[Def - Group|group]] is precisely a **one-object groupoid**: take a group $G$, form the one-object [[Def - Category|category]] $\mathbf{B}G$ with $\mathbf{B}G(\ast, \ast) = G$, and the existence of group inverses is exactly the requirement that every morphism of $\mathbf{B}G$ be an isomorphism. Conversely, restricting a groupoid to the endomorphisms of a single object yields its vertex group.

Within a connected groupoid (one in which any two objects are joined by some morphism), all vertex groups are isomorphic, and the whole groupoid is equivalent — in the sense of [[Def - Equivalence of Categories|equivalence of categories]] — to any one of them regarded as a one-object groupoid. So a connected groupoid is "a group spread out over many isomorphic copies of a single object", and choosing a base object collapses it back to the group. This is the structural reason the fundamental group $\pi_1(X, x)$ depends on the basepoint $x$ only up to isomorphism: the fundamental *groupoid* is basepoint-free, and choosing $x$ extracts a vertex group.

---

# Relate to Other Fields / Compression

**True name:** *a group with the single-object restriction lifted* — equivalently, the category of reversible, typed transformations. The operational reflex: whenever a situation is reversible but the "states" being transformed vary (paths between varying endpoints, isomorphisms between varying objects, gauge transformations between varying frames), reach for a groupoid, not a group, and recover a group only after fixing a basepoint.

Groupoids are the natural home for symmetry that is *local* rather than global. A group describes a symmetry that acts everywhere uniformly; a groupoid describes "the symmetries available here, the symmetries available there, and the isomorphisms between them". This is exactly the structure of gauge theory (a principal-bundle connection is a way of comparing fibres via a groupoid of frames), of equivalence relations (an equivalence relation on $X$ is a groupoid with at most one arrow between any two points, the arrow recording "these are equivalent"), and of the orbit structure of a [[Def - Group Action|group action]].

---

# Examples / Corollaries

**A group is a one-object groupoid.** Every [[Def - Group|group]] $G$ gives $\mathbf{B}G$, and conversely every one-object groupoid is a group. This is the base case and the reason groupoids are "many-object groups".

**The fundamental groupoid $\Pi_1(X)$.** For a [[Def - Topological Space|topological space]] $X$, define $\Pi_1(X)$: its objects are the points of $X$, and a morphism $x \to y$ is a **homotopy class of paths** from $x$ to $y$ (paths deformed rel endpoints are identified). Composition is concatenation of paths, $[\gamma_2] \circ [\gamma_1] = [\gamma_1 \cdot \gamma_2]$ where $\cdot$ is the [[Def - Path-Product and the Fundamental Group|path-product]] (first traverse $\gamma_1$, then $\gamma_2$), associative up to homotopy and hence strictly associative on homotopy classes. The identity at $x$ is the class of the constant path, and the inverse of $[\gamma]$ is the class of the reversed path $[\bar\gamma]$ — reversibility is geometric. So $\Pi_1(X)$ is a groupoid. **Its vertex group at $x$, $\Pi_1(X)(x, x)$, is exactly the [[Def - Path-Product and the Fundamental Group|fundamental group]] $\pi_1(X, x)$**, and the [[Thm - The Fundamental Group is a Group|theorem that π₁ is a group]] is, from this vantage, nothing more than the statement that *every path-class is invertible* — the group axioms for $\pi_1$ are the groupoid axioms for $\Pi_1(X)$ restricted to loops at $x$. This is the prototype illustrating that a groupoid encodes symmetry over varying basepoints, with the basepoint dependence of $\pi_1$ explained by the basepoint-freeness of $\Pi_1$.

**A group action as a functor into $\mathbf{Set}$.** Let $G$ be a group and $\mathbf{B}G$ its one-object groupoid. A [[Def - Functor|functor]] $F : \mathbf{B}G \to \mathbf{Set}$ is the data of one set $X = F(\ast)$ together with, for each group element $g$, a function $F(g) : X \to X$, such that $F(g h) = F(g) \circ F(h)$ and $F(1) = 1_X$. **This is exactly a [[Def - Group Action|group action]] of $G$ on $X$** — a homomorphism $G \to \mathrm{Sym}(X)$. A functor on the groupoid picks one set and an action; functoriality is the action axioms. (Since $\mathbf{B}G$ is a groupoid, each $F(g)$ is automatically a bijection — actions are by permutations.) This illustrates that "functor out of a groupoid" is a unifying packaging of "representation/action of the symmetry".

**Is NOT a groupoid — $\mathbf{Set}$.** The category of sets is not a groupoid: most functions are not invertible. The constant function $\mathbb{Z} \to \mathbb{Z}$, $n \mapsto 0$, has no inverse. A category is a groupoid only when *every* arrow inverts, which is a very strong condition — it forces the category to look like a disjoint union of group-translates.

**Calibration check.** Verify that the vertex group $\mathcal{G}(A, A)$ of any groupoid really is a group (composition is associative and unital from the category axioms; inverses are the groupoid inverses). Verify that in a *connected* groupoid any choice of arrows $A \to B$ induces an isomorphism of vertex groups $\mathcal{G}(A,A) \cong \mathcal{G}(B,B)$ by conjugation. Confirm you can explain why $\pi_1(X, x)$ being a group is the same statement as "$\Pi_1(X)$ is a groupoid, restricted to loops at $x$".

---

# Unlocked by This

> [!tip] Stacks and Orbifolds *(from Algebraic Geometry and Geometry)*
> When a [[Def - Group Action|group action]] has fixed points or non-free orbits, the naive quotient throws away information. The fix is to remember the action as a **groupoid** (the action groupoid) and take the quotient in the world of **stacks** and **orbifolds**, where the automorphisms of each point are retained. Groupoids are the local model for these "quotients with symmetry".

> [!tip] The Fundamental ∞-Groupoid and Homotopy Type Theory *(from Higher Category Theory)*
> Iterating the fundamental-groupoid idea — points, paths, homotopies between paths, homotopies between those — produces the **fundamental ∞-groupoid** of a space. Grothendieck's homotopy hypothesis asserts that ∞-groupoids *are* the same data as spaces up to homotopy, and this identification is the foundation of **homotopy type theory**, where types are spaces and equality is a path.

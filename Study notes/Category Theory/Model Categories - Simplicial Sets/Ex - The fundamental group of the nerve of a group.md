---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Simplicial Homotopy Group"
  - "Def - Kan Complex and the Nerve"
  - "Def - Groupoid"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $G$ be a group, viewed as a one-object [[Def - Groupoid|groupoid]] $\mathbf{B}G$ (one object $\ast$, morphisms the elements of $G$, composition the group multiplication). Let $N(G) := N(\mathbf{B}G)$ be its [[Def - Kan Complex and the Nerve|nerve]]. Show that:

(a) $N(G)$ is a [[Def - Kan Complex and the Nerve|Kan complex]];
(b) $\pi_1(N(G), \ast) \cong G$ as groups, via the bijection sending a $1$-simplex (an element of $G$) to its homotopy class;
(c) $\pi_n(N(G), \ast) = 0$ for $n \ne 1$, and $\pi_0(N(G)) = \ast$.

Conclude that $|N(G)| = BG = K(G, 1)$, the classifying space of $G$.

**Recall:**

![[Def - Kan Complex and the Nerve#The Definition]]

![[Def - Simplicial Homotopy Group#The Definition]]

A [[Def - Groupoid|groupoid]] is a [[Def - Category|category]] in which every morphism is invertible; a group $G$ is the same as a one-object groupoid $\mathbf{B}G$. The nerve of a groupoid is a [[Def - Kan Complex and the Nerve|Kan complex]] (all horns fill, using inverses for the outer ones).

---

# Convergent Strategy

**Problem class:** This is a *computation* problem of the homotopy-group world (topic-page Problem-Solving Strategy): compute all [[Def - Simplicial Homotopy Group|simplicial homotopy groups]] of an explicit Kan complex. The routine is to identify the spheroids in each dimension by hand, work out the homotopy relation, and match the group operation to a known structure.

**Assumption pattern:** The recognisable feature is "[[Def - Kan Complex and the Nerve|nerve of a groupoid]]" — which is automatically Kan (fibrancy free, by operation: the object is a nerve) — together with the rigid combinatorics of $N(G)$: an $n$-simplex is a string of $n$ composable arrows, here a tuple $(g_1, \dots, g_n) \in G^n$. The single vertex forces every boundary to be degenerate, so *every* simplex of positive dimension based correctly is a spheroid candidate.

**Theorem routing:** Each part routes through the explicit description of $N(G)_n = G^n$. Fibrancy (a) routes through "groupoid $\Rightarrow$ nerve is Kan". The $\pi_1$ computation (b) routes through: $1$-simplices $= G$, homotopy relation is trivial (boundary forces equality), group law $=$ horn-fill $=$ multiplication. The vanishing (c) routes through: in dimension $n \ge 2$ every spheroid is homotopic to the degenerate one because the nerve has *unique* fillers (it is a $1$-truncated type).

**Key decision point:** The non-obvious step in (b) is showing the homotopy relation on $1$-simplices is *trivial* (only the identity homotopies), so that $\pi_1$ is the *set* $G$ with no further quotient, and then that the horn-filling group law is exactly group multiplication rather than some twisted version. The natural error is to expect a non-trivial homotopy relation; the rigidity of the nerve (unique inner fillers) rules it out.

---

# Legal Operations Used

1. **Operation 1 from the topic page (fill a horn).** The group operation on $\pi_1$ is computed by filling the inner horn $\Lambda^2_1$, whose unique filler in $N(G)$ encodes the product.

2. **The unique-inner-filler property of nerves (from [[Def - Kan Complex and the Nerve]]).** This rigidity is what makes the homotopy relation trivial and the higher homotopy groups vanish: a nerve has exactly one filler for each inner horn.

3. **The Kan-ness of nerves of groupoids (from [[Def - Kan Complex and the Nerve]]).** Outer horns fill because every arrow is invertible; this is part (a) and what makes the homotopy-group machinery applicable.

---

# Hints

> [!note]- Hint 1
> Write down $N(G)_n$ explicitly: it is the set of strings of $n$ composable arrows in $\mathbf{B}G$, i.e. $G^n$ (the $n$ arrows, all at the single object $\ast$). The faces compose adjacent arrows or drop end ones; degeneracies insert identities.

> [!note]- Hint 2
> For (a), recall that the nerve of a groupoid fills all horns. Inner horns fill (uniquely) because adjacent arrows compose; outer horns fill because arrows have inverses (e.g. $\Lambda^2_0$ needs to solve $h = (?) \circ g$, which uses $g^{-1}$).

> [!note]- Hint 3
> For (b): the spheroids in dimension $1$ are the $1$-simplices with degenerate boundary — but the single vertex makes *every* boundary degenerate, so all of $N(G)_1 = G$ are spheroids. Now show the homotopy relation is trivial: a homotopy $\sigma \sim \tau$ between $1$-simplices is a $2$-simplex with one face $\sigma$, one face $\tau$, one degenerate — and uniqueness of the filler forces $\sigma = \tau$.

> [!note]- Hint 4
> For the group law in (b): to multiply $[g], [h]$, fill the inner horn $\Lambda^2_1$ with faces $d_2 = g$, $d_0 = h$. The unique filler is the $2$-simplex $(g, h)$, whose remaining face $d_1$ is the composite — which in $\mathbf{B}G$ is the product $hg$ (or $gh$ depending on convention). Match this to group multiplication.

> [!note]- Hint 5
> For (c): in dimension $n \ge 2$, a spheroid is a string $(g_1, \dots, g_n)$ with all faces degenerate, which forces all $g_i = e$ once you chase the boundary conditions; alternatively, the unique-filler property makes every spheroid homotopic to the degenerate one. For $\pi_0$, there is a single vertex, so one component.

---

# Solution

$N(G)$ is Kan because $\mathbf{B}G$ is a groupoid. Its $1$-simplices are the elements of $G$; the homotopy relation on them is trivial (forced by unique fillers), so $\pi_1 = G$ as a set, and the horn-filling group law is exactly group multiplication. All higher and lower homotopy groups vanish because the nerve is a $1$-truncated type. Realising gives the classifying space $BG = K(G,1)$.

**Step 1: $N(G)$ is a Kan complex (part a).**

> [!note]- Derivation
> The simplices are $N(G)_n = \{(g_1, \dots, g_n) : g_i \in G\} = G^n$ (strings of $n$ composable arrows at the unique object $\ast$). Given a horn $\Lambda^n_k \to N(G)$, the missing face is determined by composing or inverting the adjacent edges: for an *inner* horn the missing edge is a composite of two given ones (unique filler); for an *outer* horn $\Lambda^n_0$ or $\Lambda^n_n$ the missing edge requires an *inverse*, which exists because $\mathbf{B}G$ is a [[Def - Groupoid|groupoid]]. For $n = 2$: $\Lambda^2_1 = (g, h)$ fills to $(g,h)$ with $d_1 =$ composite; $\Lambda^2_0 = (g\text{ as }d_2, h\text{ as }d_1)$, i.e. edges $g$ and the "long" edge $h$ sharing vertex, fills by solving for $g^{-1}h$. So every horn fills: $N(G)$ is a [[Def - Kan Complex and the Nerve|Kan complex]].

**Step 2: $\pi_1(N(G), \ast)$ has underlying set $G$ (part b, first half).**

> [!note]- Derivation
> Since $N(G)$ has a single vertex $\ast$, every $1$-simplex $g \in G$ has both faces equal to $\ast$ (degenerate), so every $1$-simplex is a spheroid: $Z_1(N(G), \ast) = G$. Now the homotopy relation. A homotopy $g \sim g'$ is a $2$-simplex $H$ with $d_1H = g$, $d_2H = g'$ and $d_0H$ degenerate (the identity $e$). A $2$-simplex of $N(G)$ is a composable pair $(a, b)$ with $d_0 = b$, $d_2 = a$, $d_1 =$ composite $b\circ a$. Setting $d_0H = e$ forces $b = e$, and then $d_1H = e \circ a = a = d_2H$, i.e. $g = g'$. So the only homotopies are between equal $1$-simplices: the homotopy relation is *trivial*, and $\pi_1(N(G), \ast) = G/\!\sim\ = G$ as a set.

**Step 3: The group operation is group multiplication (part b, second half).**

> [!note]- Derivation
> To compute $[g]\cdot[h]$ fill the inner horn $\Lambda^2_1$ with $d_2 = g$ and $d_0 = h$. The unique filler in $N(G)$ is the $2$-simplex $(g, h)$ (the composable pair $\ast \xrightarrow{g} \ast \xrightarrow{h} \ast$), whose face $d_1$ is the composite $h \circ g = hg$ in $\mathbf{B}G$. By the definition of the [[Def - Simplicial Homotopy Group|simplicial group operation]], $[g]\cdot[h] = [d_1\text{-filler}] = [hg]$. So the operation is the group multiplication of $G$ (with the convention matching composition order), the identity is $[e]$, and inverses are $[g^{-1}]$. Hence $\pi_1(N(G), \ast) \cong G$ as groups.

**Step 4: Higher and lower homotopy groups vanish (part c).**

> [!note]- Derivation
> For $n \ge 2$: a spheroid is an $n$-simplex $(g_1, \dots, g_n) \in G^n$ all of whose faces are degenerate. The face $d_i$ for $0 < i < n$ composes $g_i, g_{i+1}$, and degeneracy of $d_iH$ forces all the relevant composites and edges to be identities; chasing the boundary conditions forces every $g_j = e$, so the only spheroid is the degenerate one. (Conceptually: $N(G)$ is a $1$-*truncated* Kan complex — the unique-inner-filler property means it has no non-trivial homotopy above dimension $1$.) Hence $\pi_n(N(G), \ast) = 0$ for $n \ge 2$. For $\pi_0$: there is exactly one vertex $\ast$, so $\pi_0(N(G)) = \ast$ (one connected component).

**Step 5: Realisation is the classifying space.**

> [!note]- Derivation
> By [[Thm - Geometric Realization is a Quillen Equivalence]], $|N(G)|$ has the same homotopy groups as $N(G)$: $\pi_1 = G$ and $\pi_n = 0$ otherwise, with one component. A connected space with $\pi_1 = G$ and all higher homotopy groups vanishing is, by definition, a $K(G, 1)$ — an Eilenberg–MacLane space — and it is the classifying space $BG$ of $G$. So $|N(G)| \simeq BG = K(G, 1)$.

> [!note]- Complete formal solution
> $N(G)_n = G^n$ (strings of composable arrows at the single object). *(a)* Every horn fills: inner horns by composing adjacent arrows, outer horns by inverting (possible since $\mathbf{B}G$ is a [[Def - Groupoid|groupoid]]); so $N(G)$ is Kan. *(b)* All $1$-simplices are spheroids (single vertex), so $Z_1 = G$. A homotopy $g \sim g'$ is a $2$-simplex $(a,b)$ with $d_0 = b = e$, $d_2 = a = g'$, $d_1 = ba = g$; $b = e$ gives $g = a = g'$, so $\sim$ is trivial and $\pi_1 = G$ as a set. The operation $[g]\cdot[h]$ is read off the unique filler of $\Lambda^2_1$ with faces $g, h$, namely the pair $(g,h)$ with $d_1 = hg$; so $\pi_1 \cong G$ as groups. *(c)* For $n \ge 2$ the only degenerate-boundary $n$-simplex is degenerate (boundary conditions force all entries to $e$; $N(G)$ is $1$-truncated), so $\pi_n = 0$; one vertex gives $\pi_0 = \ast$. *Conclusion:* $|N(G)|$ has $\pi_1 = G$, $\pi_{n\ne 1} = 0$, so $|N(G)| \simeq BG = K(G,1)$. $\quad\blacksquare$

---

# Key Takeaways

**Nerves of groupoids are the $1$-truncated Kan complexes, and they compute group cohomology.** This exercise establishes the dictionary "groupoid $\leftrightarrow$ homotopy $1$-type": a group $G$ becomes the Kan complex $N(G)$, whose realisation $BG = K(G,1)$ has $G$ as its only homotopy group. The downstream payoff is that the cohomology of the space $BG$ is the *group cohomology* $H^*(G; -)$, so a purely algebraic invariant is computed by a topological space built from a purely categorical construction (the nerve). The trigger-reaction: when a group or groupoid appears and you want its homotopy-theoretic invariants, take the nerve and realise. This is the bottom rung of the homotopy hypothesis — the case where ∞-groupoid = $1$-groupoid = ordinary groupoid is fully explicit and hand-computable.

**Rigidity (unique fillers) is what kills the higher homotopy and trivialises the homotopy relation.** The reason $N(G)$ has no homotopy above dimension $1$, and the reason its $1$-simplices have a *trivial* homotopy relation, is the same: the nerve has a *unique* filler for each inner horn. Uniqueness is exactly the difference between a strict structure (a category/group, one composite) and a homotopical one (a [[Def - Quasi-Category|quasi-category]], a contractible space of composites). Whenever you compute homotopy groups of a nerve, the unique-filler property collapses everything to the underlying categorical data. The transferable diagnostic: the more unique your fillers, the more truncated your homotopy type — Kan complexes with unique inner fillers are nerves, hence $1$-types or their groupoid generalisations.

**Reading a group operation off a horn filler is the prototype for all simplicial algebra.** The computation that $[g]\cdot[h] = [hg]$ by filling $\Lambda^2_1$ and taking $d_1$ is the template for how *every* algebraic operation appears in the simplicial world: the operation is the missing face of a filled horn. This is how composition appears in a nerve, how the group law appears on $\pi_n$, how the $A_\infty$ and $E_\infty$ operations appear on a space, and how the multiplication on a simplicial monoid is encoded. The unifying frame is "operations are fillers"; once installed, simplicial homotopy theory reads as a calculus of filling horns, and the algebra is recovered by reading off the faces the fillers produce.

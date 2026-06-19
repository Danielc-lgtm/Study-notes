---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Kan Complex and the Nerve"
  - "Def - Simplicial Set"
  - "Def - Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Regard the linearly ordered set $[n] = (0 \to 1 \to \dots \to n)$ as a [[Def - Category|category]] (a poset, with a unique arrow $i\to j$ whenever $i\le j$). Show that its [[Def - Kan Complex and the Nerve|nerve]] is the standard $n$-simplex:
$$N([n]) \cong \Delta^n.$$
Concretely, identify the $k$-simplices of $N([n])$ with order-preserving tuples $0\le a_0\le\dots\le a_k\le n$, matching the simplices of $\Delta^n$, and check the face and degeneracy maps agree. Conclude that the standard simplices are exactly the nerves of the finite ordinals, so that the [[Def - The Yoneda Embedding|Yoneda embedding]] $\Delta\to\mathbf{sSet}$ factors through the nerve.

**Recall:**

The [[Def - Kan Complex and the Nerve|nerve]] of a category $\mathcal{C}$ has $N(\mathcal{C})_k=\mathrm{Fun}([k],\mathcal{C})$, the strings of $k$ composable arrows. The standard simplex is the representable [[Def - Simplicial Set|simplicial set]] $\Delta^n=\Delta(-,[n])$, with $\Delta^n_k=\Delta([k],[n])$ = order-preserving maps $[k]\to[n]$. A poset is a category with at most one morphism between any two objects.

---

# Convergent Strategy

**Problem class:** This is a "compute a nerve via the universal property and match it to a representable" problem — the second source pattern of the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]]. The routine is to compute both $N([n])_k$ and $\Delta^n_k$ from their definitions and observe they are the same set of order-preserving tuples.

**Assumption pattern:** The recognisable feature is that $[n]$ is a *poset* — at most one arrow between objects — so a functor $[k]\to[n]$ is determined by its action on objects, which must be order-preserving. This collapses "string of composable arrows" to "monotone map of ordinals", which is precisely the simplices of $\Delta^n$.

**Theorem routing:** Two computations meet: $N([n])_k=\mathrm{Fun}([k],[n])$ by the [[Def - Kan Complex and the Nerve|nerve]] definition, and $\Delta^n_k=\Delta([k],[n])$ by representability ([[Def - The Yoneda Embedding|Yoneda]]). For a poset $[n]$, a functor $[k]\to[n]$ *is* an order-preserving map, so the two sets coincide.

**Key decision point:** The non-obvious choice is recognising that "functor between posets = order-preserving map of underlying sets". A functor must preserve composition, but in a poset composition is forced (unique arrows), so the only constraint is that the object map respect the order. This is what makes $\mathrm{Fun}([k],[n]) = \Delta([k],[n])$ and collapses the nerve to the representable.

---

# Legal Operations Used

1. **Operation 2 (compute the simplices of a simplicial set via its universal property).** Compute $N([n])_k=\mathrm{Fun}([k],[n])$ and $\Delta^n_k=\Delta([k],[n])$ and match.

---

# Hints

> [!note]- Hint 1
> A functor $[k]\to[n]$ between posets is determined by where it sends the objects $0,1,\dots,k$. What constraint does functoriality place on the images?

> [!note]- Hint 2
> Functoriality forces the object map to be order-preserving (if $i\le j$ there is an arrow $i\to j$, which must map to an arrow, so $F(i)\le F(j)$). So $\mathrm{Fun}([k],[n])$ = monotone maps $[k]\to[n]$ = $\Delta([k],[n])$.

> [!note]- Hint 3
> Both face maps drop a vertex of the tuple $(a_0,\dots,a_k)$ (precompose with the coface $d^i$); both degeneracies repeat a vertex (precompose with $s^i$). Since the nerve's structure maps and $\Delta^n$'s are both "precompose with the map in $\Delta$", they agree.

---

# Solution

The plan: Step 1 shows a functor $[k]\to[n]$ is a monotone map. Step 2 matches the $k$-simplices of $N([n])$ with those of $\Delta^n$. Step 3 matches the structure maps. Step 4 draws the conclusion about the Yoneda embedding.

**Step 1: Functors between ordinals are monotone maps.** A functor $[k]\to[n]$ between the posets is exactly an order-preserving function on objects.

> [!note]- Derivation
> $[k]$ and $[n]$ are posets: there is a unique arrow $i\to j$ iff $i\le j$. A [[Def - Functor|functor]] $F:[k]\to[n]$ assigns objects $F(i)\in[n]$ and arrows; but an arrow $i\to j$ (existing iff $i\le j$) must map to an arrow $F(i)\to F(j)$ (existing iff $F(i)\le F(j)$), so $i\le j\Rightarrow F(i)\le F(j)$ — $F$ is order-preserving. Conversely any order-preserving object map extends uniquely to a functor (arrows are forced and composition is automatic, since arrows are unique). So $\mathrm{Fun}([k],[n]) = \{$order-preserving maps $[k]\to[n]\} = \Delta([k],[n])$.

**Step 2: The $k$-simplices match.** $N([n])_k = \mathrm{Fun}([k],[n]) = \Delta([k],[n]) = \Delta^n_k$, both being order-preserving tuples $0\le a_0\le\dots\le a_k\le n$.

> [!note]- Derivation
> By the [[Def - Kan Complex and the Nerve|nerve]] definition, $N([n])_k = \mathrm{Fun}([k],[n])$; by Step 1 this equals $\Delta([k],[n])$; by representability of $\Delta^n$ ([[Def - The Yoneda Embedding|Yoneda]]), $\Delta([k],[n]) = \Delta^n_k$. A monotone map $[k]\to[n]$ is the tuple $(a_0,\dots,a_k)$ of images with $a_0\le\dots\le a_k$. So the $k$-simplices of $N([n])$ and of $\Delta^n$ are the same set, naturally in $k$.

**Step 3: The structure maps match.** Both nerve and representable structure maps are "precompose with the corresponding map of $\Delta$", so faces drop a vertex and degeneracies repeat one, identically in $N([n])$ and $\Delta^n$.

> [!note]- Derivation
> For $\theta:[m]\to[k]$ in $\Delta$, the structure map of $N([n])$ is precomposition $\mathrm{Fun}([k],[n])\to\mathrm{Fun}([m],[n])$, $F\mapsto F\circ\theta$; the structure map of $\Delta^n$ is precomposition $\Delta([k],[n])\to\Delta([m],[n])$, the same operation under the identification of Step 1. In particular the face map $d_i$ (precompose with the coface $d^i$) drops the $i$th entry of $(a_0,\dots,a_k)$, and the degeneracy $s_i$ (precompose with $s^i$) repeats the $i$th entry. The bijections of Step 2 commute with all these, so they assemble into an isomorphism of simplicial sets $N([n])\cong\Delta^n$.

**Step 4: Conclusion — standard simplices are nerves of ordinals.** Hence $\Delta^n\cong N([n])$, so the [[Def - The Yoneda Embedding|Yoneda embedding]] $\Delta\to\mathbf{sSet}$, $[n]\mapsto\Delta^n$, factors as $[n]\mapsto[n]\mapsto N([n])$.

> [!note]- Derivation
> Step 3 gives $\Delta^n\cong N([n])$ for every $n$, naturally in $[n]$ (a map $[m]\to[n]$ in $\Delta$ induces both $\Delta^m\to\Delta^n$ and $N([m])\to N([n])$, compatibly). The Yoneda embedding $\mathbf{y}:\Delta\to\mathbf{sSet}$ sends $[n]\mapsto\Delta^n$; via the isomorphism it equals the composite $\Delta\hookrightarrow\mathbf{Cat}\xrightarrow{N}\mathbf{sSet}$, $[n]\mapsto[n]\mapsto N([n])$. So the standard simplices are exactly the nerves of the finite total orders, and the nerve restricts to the Yoneda embedding on $\Delta$.

> [!note]- Complete formal solution
> Regard $[n]$ as a poset. A functor $[k]\to[n]$ is an order-preserving map of objects (Step 1), so
> $$N([n])_k = \mathrm{Fun}([k],[n]) = \Delta([k],[n]) = \Delta^n_k,$$
> the set of monotone tuples $0\le a_0\le\dots\le a_k\le n$. The structure maps on both sides are precomposition with maps of $\Delta$, hence agree (Step 3): faces drop a vertex, degeneracies repeat one. These bijections are natural in $[k]$, giving an isomorphism of simplicial sets $N([n])\cong\Delta^n$. Consequently the standard simplices are the nerves of the finite ordinals, and the Yoneda embedding $[n]\mapsto\Delta^n$ factors through the nerve. $\quad\blacksquare$

---

# Key Takeaways

**Posets are the categories where the nerve is forced — and they give the building blocks $\Delta^n$.** Because a poset has at most one arrow between objects, a functor out of one ordinal into another is just an order-preserving map, with composition automatic. This is exactly why $N([n])=\Delta^n$: the nerve of the simplest possible categories (finite total orders) recovers the standard simplices. The reusable recognition: nerves of posets are *order complexes*, with $k$-simplices the chains of length $k$, and the standard simplices are the special case of total orders. Whenever you nerve a poset, the simplices are chains and the combinatorics is monotone-map counting.

**"$N([n]) = \Delta^n$" is the compatibility that makes the nerve a genuine extension of the Yoneda embedding.** The nerve $N:\mathbf{Cat}\to\mathbf{sSet}$ restricted to the ordinals is precisely the Yoneda embedding $\Delta\to\mathbf{sSet}$. This is the structural reason the nerve behaves so well — it is the colimit-preserving (left Kan) extension of "$[n]\mapsto\Delta^n$" along $\Delta\hookrightarrow\mathbf{Cat}$, the categorical analogue of geometric realisation (see [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]]). Recognising the nerve as "probe a category by the ordinals, which are the simplices" is the same template that produces realisation and singular complex.

**A functor into a poset is just an inequality-respecting assignment, and this trivialises many nerve computations.** The single fact "functor between posets = monotone map" collapses what looks like a complicated computation (strings of composable arrows) into elementary combinatorics. The diagnostic to carry: when the target category is a poset (or more generally thin — at most one arrow per hom-set), functoriality imposes no data beyond the object map respecting the order, so the nerve's simplices are just order-preserving tuples. This makes order complexes, classifying spaces of posets, and the combinatorics of $\Delta$ itself all tractable by hand.

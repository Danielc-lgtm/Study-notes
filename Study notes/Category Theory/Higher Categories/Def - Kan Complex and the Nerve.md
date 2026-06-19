---
type: definition
subject: higher-categories
prereqs:
  - "Def - Simplicial Set"
  - "Def - Category"
  - "Def - Functor"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

$X$ denotes a [[Def - Simplicial Set|simplicial set]] $\Delta^{op} \to \mathbf{Set}$, with $n$-simplices $X_n$, face maps $d_i$, degeneracy maps $s_i$. The standard $n$-simplex is $\Delta^n = \Delta(-,[n])$ and the **$i$th horn** $\Lambda^n_i \subseteq \Delta^n$ is the union of all faces but the $i$th; a horn is **inner** if $0 < i < n$ and **outer** if $i \in \{0, n\}$. A simplicial set $X$ has the **right lifting property** against $\Lambda^n_i \hookrightarrow \Delta^n$ if every map $\Lambda^n_i \to X$ extends along the inclusion to a map $\Delta^n \to X$ (a "**filler**"). For a [[Def - Category|category]] $\mathcal{C}$, $N(\mathcal{C})$ is its **nerve**, and $\mathrm{Fun}([n], \mathcal{C})$ denotes [[Def - Functor|functors]] from the poset $[n] = (0 \to 1 \to \dots \to n)$. The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

This is a compound page: it defines three interlocking notions — the **inner horn**, the **Kan complex**, and the **nerve** — because the Kan complex and the nerve are the two extreme answers to one question ("which horns fill, and how uniquely?"), and the inner horn is the distinction on which both, and the [[Def - Quasi-Category|quasi-category]] of §H.4, turn.

---

# Axiom Motivation

Both definitions on this page answer a single question: *how do you say "composition" in the language of simplicial sets, without an operation?* In an ordinary category, given two composable arrows $f : x \to y$ and $g : y \to z$, you write down their composite $g \circ f : x \to z$ by *applying the composition function*. The whole project of $\infty$-category theory is to replace this function by a *geometric* condition on a simplicial set, so that composition becomes a property of fillability rather than a chosen operation. Understanding why requires understanding the inner horn.

Picture the inner horn $\Lambda^2_1 \subseteq \Delta^2$. The triangle $\Delta^2$ has vertices $0, 1, 2$ and three edges $01$, $12$, $02$. The horn $\Lambda^2_1$ is what you get by keeping the two edges *adjacent to vertex $1$* — namely $01$ and $12$ — and discarding the long edge $02$ and the interior. So a map $\Lambda^2_1 \to X$ is precisely a pair of *composable* simplices: an edge $f$ from $0$ to $1$ and an edge $g$ from $1$ to $2$. A **filler** — an extension to a full $2$-simplex $\Delta^2 \to X$ — supplies the missing long edge $02$ together with a triangle witnessing it. That long edge is *a composite of $f$ and $g$*, and the triangle is the witness that it is one. This is the central translation of the chapter: **inner-horn fillers are composites.**

Now the question splits, and the split is the whole subject. *How many* fillers should we demand?

- If we demand that every inner horn has a **unique** filler, then every pair of composable arrows has exactly one composite — composition is an honest function. This recovers ordinary categories, and the simplicial sets that arise this way are exactly the **nerves** $N(\mathcal{C})$.
- If we demand only that every inner horn has **some** filler, then composites *exist* but need not be unique — composition is defined only up to a choice. This is the [[Def - Quasi-Category|quasi-category]] of §H.4.
- If we demand that *all* horns fill, inner and outer alike, then (it turns out) every morphism becomes invertible. These are the **Kan complexes**, the $\infty$-groupoids.

The reason the *inner/outer* distinction matters is worth dwelling on, because it is the most common point of confusion. The outer horns $\Lambda^n_0$ and $\Lambda^n_n$ do *not* correspond to composing two arrows in series; for $n = 2$, the horn $\Lambda^2_0$ consists of the two edges *emanating from vertex $0$* (edges $01$ and $02$), and filling it would require, given $f : 0 \to 1$ and $h : 0 \to 2$, producing an arrow $1 \to 2$ — i.e. *solving* $h = (\text{?}) \circ f$ for the unknown, which demands that $f$ be *invertible*. So filling outer horns is the geometric form of "every morphism has an inverse". A category with non-invertible morphisms therefore *cannot* fill outer horns, and its nerve is not a Kan complex. The Kan condition (all horns) is the condition for an $\infty$-*groupoid*; the inner condition is the condition for an $\infty$-*category*.

Why define the Kan complex via *all* horns rather than only outer ones? Because outer-horn filling alone, without inner filling, would not even let you compose, so it is not a sensible standalone condition; the Kan complex is the maximal demand (all horns), capturing "compose freely and invert freely", which is exactly what a space affords — paths compose and reverse up to homotopy. Why define the nerve to require *uniqueness*? Because that uniqueness is precisely what distinguishes a strict category (one composite) from an $\infty$-category (a contractible space of composites); dropping it is the single edit that turns category theory into homotopy theory.

---

# The Definition

**Inner horn.** For $0 \le i \le n$, the **$i$th horn** $\Lambda^n_i \subseteq \Delta^n$ is the [[Def - Simplicial Set|sub-simplicial-set]] which is the union of all the faces $d^j(\Delta^{n-1})$ for $j \ne i$. It is the **$i$th inner horn** when $0 < i < n$, and an **outer horn** when $i = 0$ or $i = n$. Concretely, $\Lambda^n_i$ is $\Delta^n$ with its interior and its $i$th face removed.

**Kan complex.** A simplicial set $X$ is a **Kan complex** if it has the **right lifting property against every horn inclusion**: for all $n \ge 1$ and all $0 \le i \le n$, every map of simplicial sets $\Lambda^n_i \to X$ extends to a map $\Delta^n \to X$,
$$
\begin{array}{ccc}
\Lambda^n_i & \longrightarrow & X \\
\downarrow & \nearrow & \\
\Delta^n & &
\end{array}
$$
that is, the dashed lift $\Delta^n \to X$ exists making the triangle commute. (Existence only; the filler need not be unique.)

**Nerve.** Identify the ordinal $[n]$ with the [[Def - Category|category]] $(0 \to 1 \to \dots \to n)$ (the poset, viewed as a category). The **nerve** of a category $\mathcal{C}$ is the simplicial set
$$N(\mathcal{C})_n = \mathrm{Fun}([n], \mathcal{C}),$$
the set of [[Def - Functor|functors]] $[n] \to \mathcal{C}$ — equivalently, the set of **strings of $n$ composable arrows** $A_0 \xrightarrow{f_1} A_1 \xrightarrow{f_2} \cdots \xrightarrow{f_n} A_n$. For an order-preserving $\theta : [m] \to [n]$, the structure map $N(\mathcal{C})_n \to N(\mathcal{C})_m$ is precomposition with $\theta$. Explicitly: $N(\mathcal{C})_0 = \mathrm{ob}\,\mathcal{C}$, $N(\mathcal{C})_1 = \{$morphisms$\}$, $N(\mathcal{C})_2 = \{$composable pairs$\}$; the face map $d_1 : N(\mathcal{C})_2 \to N(\mathcal{C})_1$ sends $(f, g)$ to the **composite** $g \circ f$, while $d_0, d_2$ project to $g$ and $f$; degeneracies insert identity arrows.

---

# Categorical / Structural Definition

The nerve is a [[Def - Functor|functor]] $N : \mathbf{Cat} \to \mathbf{sSet}$, and it has a clean structural origin: it is the **singular-nerve construction for the inclusion $\Delta \hookrightarrow \mathbf{Cat}$** (each ordinal $[n]$ regarded as a category). Just as $\mathrm{Sing}(X)_n = \mathbf{Top}(|\Delta^n|, X)$ probes a space by mapping in geometric simplices, the nerve probes a category by mapping in the "categorical simplices" $[n]$:
$$N(\mathcal{C})_n = \mathbf{Cat}([n], \mathcal{C}) = \mathrm{Fun}([n], \mathcal{C}).$$
This is the right adjoint to the functor $\mathbf{sSet} \to \mathbf{Cat}$ that sends $\Delta^n \mapsto [n]$ and takes colimits — the "fundamental category" or "homotopy category" functor $\tau_1 \dashv N$. (Compare [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]], which is the topological analogue of the same adjunction template.)

The Kan condition is the structural notion of a **fibrant object** in the Kan–Quillen model structure on $\mathbf{sSet}$: it is "right lifting against the generating trivial cofibrations", the horn inclusions. The reason the lifting-property language is worth the abstraction is that it is *uniform across dimensions and dual-friendly* — the same shape of condition defines fibrations, Kan complexes, and quasi-categories, differing only in *which* horns one tests.

---

# Relate to Other Fields / Compression

The nerve is the precise sense in which **a category is a special kind of space**. The compression: $N(\mathcal{C})$ encodes a category as the simplicial set whose simplices are commutative diagrams of shape $[n]$; the unique-inner-filler property records that composition is single-valued. A Kan complex compresses to "a combinatorial space in which every edge is invertible" — an $\infty$-groupoid.

**True name:** the nerve is "the simplicial set of strings of composable arrows", and a Kan complex is "a simplicial set in which you can both compose and invert, freely". When you see "$N(\mathcal{C})$", picture the $n$-simplices as length-$n$ chains of arrows; when you see "Kan complex", picture $\mathrm{Sing}(X)$ for a space $X$.

The bridge to algebraic topology is exact: $\mathrm{Sing}(X)$ is a Kan complex for every space $X$ (paths compose and reverse up to homotopy), and the [[Def - Path-Product and the Fundamental Group|fundamental group]] $\pi_1(X)$ is recovered as automorphisms of a vertex in the [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] of $\mathrm{Sing}(X)$. The nerve also recovers the classifying space of a group: $N(G)$, the nerve of a one-object [[Def - Groupoid|groupoid]] with morphism group $G$, realises to the classifying space $BG = K(G,1)$.

---

# Examples / Corollaries

**Is an instance — the nerve of any category is a quasi-category.** For every category $\mathcal{C}$, $N(\mathcal{C})$ has a *unique* filler for each inner horn: a horn $\Lambda^n_1 \to N(\mathcal{C})$ records the composable arrows, and the simplex it extends to is forced by composing them. In particular every inner horn fills, so $N(\mathcal{C})$ is a [[Def - Quasi-Category|quasi-category]] (proved in detail at [[Ex - The nerve of a category is a quasi-category]]). The uniqueness is what makes $N(\mathcal{C})$ special among quasi-categories.

**Is an instance — $\mathrm{Sing}(X)$ is a Kan complex.** For a [[Def - Topological Space|space]] $X$, every horn $|\Lambda^n_i| \to X$ extends to $|\Delta^n| \to X$ because $|\Lambda^n_i|$ is a *retract* of $|\Delta^n|$ (the horn is a deformation retract of the solid simplex), so a map out of the horn extends along the retraction. Hence $\mathrm{Sing}(X)$ fills *all* horns, inner and outer, and is a Kan complex — the fundamental $\infty$-groupoid of $X$ (see [[Ex - The singular simplicial set is a Kan complex]]).

**Is NOT a Kan complex — the nerve of a non-groupoid.** Take $\mathcal{C}$ to be the poset $[1] = (0 \to 1)$, so $N(\mathcal{C}) = \Delta^1$. The outer horn $\Lambda^2_0 \to \Delta^1$ given by the two edges $0 \to 1$ (the arrow) and $0 \to ?$ has no filler that would require inverting the arrow $0 \to 1$: there is no arrow $1 \to 0$ in $\mathcal{C}$. So $\Delta^1$ fills inner horns (it is a quasi-category) but *not* outer ones — it is *not* a Kan complex. This is the generic situation: $N(\mathcal{C})$ is a Kan complex iff $\mathcal{C}$ is a [[Def - Groupoid|groupoid]].

**Corollary — Kan $\Rightarrow$ quasi-category.** Inner horns are a subset of all horns, so a simplicial set filling *all* horns in particular fills the inner ones. Hence every Kan complex is a [[Def - Quasi-Category|quasi-category]], and the inclusions are strict: $\{$nerves$\} \subsetneq \{$quasi-categories$\} \supsetneq \{$Kan complexes$\}$, with $\{$nerves of groupoids$\} = \{$Kan complexes that are nerves$\}$.

**Corollary — the nerve is injective on objects and faithful.** Two functors $F, G : \mathcal{C} \to \mathcal{D}$ with $N(F) = N(G)$ agree on objects ($0$-simplices) and on morphisms ($1$-simplices), hence are equal; and a natural transformation between them is determined by its action on simplices. This is the easy half of "$N$ is fully faithful" (see [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers]]).

**Calibration check.** Verify that $N(\mathcal{C})_2$ is the set of composable pairs and that the face map $d_1$ is "compose". Confirm that the inner horn $\Lambda^2_1 \to N(\mathcal{C})$ is exactly a composable pair $(f, g)$ and that its *unique* filler is the $2$-simplex with long edge $g \circ f$. And check that for a [[Def - Groupoid|groupoid]] $G$, the outer horn $\Lambda^2_0$ can be filled by using the inverse of an arrow — so nerves of groupoids are Kan.

---

# Unlocked by This

> [!tip] Quasi-Category *(from this chapter, §H.4)*
> Relaxing "unique inner-horn filler" (nerve) to "some inner-horn filler" gives the [[Def - Quasi-Category|quasi-category]], the model of an $\infty$-category. The inner horn defined here is the exact locus of that relaxation.

> [!tip] The Homotopy Hypothesis *(from Foundations / Algebraic Topology)*
> Kan complexes *are* $\infty$-groupoids, and the **homotopy hypothesis** identifies $\infty$-groupoids with [[Def - Topological Space|spaces]] up to weak homotopy equivalence, via $\mathrm{Sing}$ and geometric realisation. A Kan complex is a space presented combinatorially.

> [!tip] Simplicial Homotopy Groups *(from Algebraic Topology)*
> For a Kan complex $K$ with basepoint, the **simplicial homotopy groups** $\pi_n(K)$ are defined combinatorially as homotopy classes of $n$-simplices with degenerate boundary; the Kan condition is exactly what makes the group operation well-defined, and $\pi_n(\mathrm{Sing}\,X) = \pi_n(X)$.

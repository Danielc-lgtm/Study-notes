---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Ring"
  - "Def - Ring Homomorphism"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. We fix an index set $I$ carrying a partial order $\leq$, objects $X_i$ or $Y_i$ ($i\in I$) drawn from a fixed category $\mathcal{C}$ — one of Sets, Groups, Rings, [[Def - Module|$R$-modules]], or $R$-algebras — and morphisms between them. For a direct system the transition morphisms are written $f_{ij}:X_i\to X_j$ (defined when $i\leq j$, running *with* the order); for an inverse system they are $h_{ij}:Y_j\to Y_i$ (defined when $i\leq j$, running *against* the order). The full registry is on [[Commutative Algebra X — Completions and Limits]].

This is a compound page: it defines three interlocking notions — the **directed set** $(I,\leq)$, the **direct system** $\big((X_i),(f_{ij})\big)$, and the **inverse system** $\big((Y_i),(h_{ij})\big)$ — because they are introduced together and none is usable without the others: a system is *indexed by* a directed set, and the limits built from the two kinds of system (on [[Def - Direct and Inverse Limits]]) are dual.

---

# Axiom Motivation

The goal is to set up the bookkeeping for two operations we want to perform constantly: **gluing a family of objects along compatible identifications** (a generalised union) and **collecting compatible families of approximations** (a generalised limit-of-approximations). Both operations need a family of objects indexed by some set, and a coherent system of maps relating them. The definitions on this page are exactly the minimal scaffolding that makes those two operations well-defined. The way to invent them is to ask, for each axiom, "what would go wrong in the gluing if I dropped this?"

**Why the index set must be directed (any two indices have an upper bound).** Picture the gluing operation: we have objects $X_i$ and we want to declare $x_i\in X_i$ and $x_j\in X_j$ "the same" when they have a common image further up the system. For this to be an *equivalence relation* — in particular transitive — we need: if $x_i$ and $x_j$ agree somewhere, and $x_j$ and $x_k$ agree somewhere, then $x_i$ and $x_k$ agree somewhere. The "somewhere" for the first is an index $\geq i,j$ and for the second an index $\geq j,k$; to combine them we need a *single* index $\geq$ all of $i,j,k$. The directedness axiom — *any two elements have a common upper bound* — is precisely what guarantees such a combining index always exists. Drop it and the naive identification relation is not transitive, so the direct limit is not even a well-defined quotient. Concretely, if $I=\{a,b\}$ with no order relations at all (an antichain), the only "direct limit" is the disjoint union, and there is no mechanism for ever identifying an element of $X_a$ with one of $X_b$ — the gluing degenerates. Directedness is the minimal condition that lets identifications propagate. It is weaker than being a chain (totally ordered): we do *not* need $i,j$ to be comparable to each other, only to have *some* common upper bound, which is what allows index sets like the open neighbourhoods of a point (ordered by reverse inclusion) to qualify even though two neighbourhoods need not be nested.

**Why $f_{ii}=\mathrm{id}$ (the reflexive transition is the identity).** Each object must map to itself trivially, because in the gluing an element is always identified with itself, and in the limit a compatible family must satisfy $y_i = h_{ii}(y_i)$. If $f_{ii}$ were some other endomorphism, an element $x_i$ would be glued to $f_{ii}(x_i)\neq x_i$ inside its *own* object, collapsing information we never asked to collapse. The identity axiom pins the system down so that the only identifications are the genuinely cross-level ones encoded by the $f_{ij}$ with $i<j$.

**Why $f_{jk}\circ f_{ij}=f_{ik}$ (the cocycle/coherence condition).** This is the heart of "compatible". When $i\leq j\leq k$, there are *a priori* two ways to map $X_i$ to $X_k$: directly via $f_{ik}$, or in two hops via $f_{jk}\circ f_{ij}$. The axiom demands they agree. Without it, "the image of $x_i$ further up the system" would depend on the *route* taken, and the identification relation would be ambiguous — $x_i$ might be glued to different elements of $X_k$ along different paths, and the universal property of the limit (a single canonical map from each stage) would fail. The coherence condition is exactly what makes the system *commute*, so that there is an unambiguous notion of "the eventual image" of any element. It is the same condition that, in the language of categories, says a direct system is a *functor* from the poset $(I,\leq)$ into $\mathcal{C}$: functoriality is precisely $f_{ii}=\mathrm{id}$ and $f_{jk}f_{ij}=f_{ik}$.

**Why the inverse system reverses the arrows, and the dual coherence.** The inverse system is built for the *opposite* operation: instead of gluing objects into one big union, we collect *threads* of mutually consistent approximations. So the maps run downward, $h_{ij}:Y_j\to Y_i$ for $i\leq j$ — "forget detail, project to a coarser stage" — and the coherence condition becomes $h_{ij}\circ h_{jk}=h_{ik}$: projecting from level $k$ down to $i$ directly equals projecting down to $j$ and then to $i$. This is the same functoriality, now from $(I,\leq)^{\mathrm{op}}$, i.e. a *contravariant* functor on $(I,\leq)$. The reason to package both with the same directed $I$ is that the resulting limits are *dual* — reverse every arrow in a direct system and you get an inverse system, and $\varinjlim$ turns into $\varprojlim$ — so the same indexing discipline serves both, and one set of well-definedness checks (directedness) covers both constructions. The motivating index set $(\mathbb{N},\leq)$ makes a direct system into a forward chain $X_0\to X_1\to\cdots$ and an inverse system into a backward chain $\cdots\to Y_2\to Y_1\to Y_0$; the truncation maps $R/\mathfrak{a}^{n+1}\twoheadrightarrow R/\mathfrak{a}^n$ are the inverse system that produces every completion.

---

# The Definition

Let $\mathcal{C}$ be one of the categories Sets, Groups, Rings, $R$-modules, $R$-algebras.

## Directed set

A **directed set** is a pair $(I,\leq)$ where $\leq$ is a partial order on the set $I$ such that for all $a,b\in I$ there exists $c\in I$ with $a\leq c$ and $b\leq c$.

## Direct system

A **direct system** over a directed set $(I,\leq)$ is a pair $D = \big((X_i)_{i\in I},\,(f_{ij})_{i\leq j}\big)$ where each $X_i$ is an object of $\mathcal{C}$ and each $f_{ij}:X_i\to X_j$ (defined for $i\leq j$) is a morphism, such that
$$f_{ii}=\mathrm{id}_{X_i}\ \text{ for all } i, \qquad f_{jk}\circ f_{ij}=f_{ik}\ \text{ for all } i\leq j\leq k.$$

## Inverse system

An **inverse system** over $(I,\leq)$ is a pair $E = \big((Y_i)_{i\in I},\,(h_{ij})_{i\leq j}\big)$ where each $Y_i$ is an object of $\mathcal{C}$ and each $h_{ij}:Y_j\to Y_i$ (defined for $i\leq j$) is a morphism, such that
$$h_{ii}=\mathrm{id}_{Y_i}\ \text{ for all } i, \qquad h_{ij}\circ h_{jk}=h_{ik}\ \text{ for all } i\leq j\leq k.$$

Equivalently and more compactly: a direct system is a covariant functor $(I,\leq)\to\mathcal{C}$, and an inverse system is a contravariant functor $(I,\leq)\to\mathcal{C}$ (a covariant functor $(I,\leq)^{\mathrm{op}}\to\mathcal{C}$).

---

# Categorical / Structural Definition

A poset $(I,\leq)$ *is* a category: the objects are the elements of $I$, and there is exactly one morphism $i\to j$ precisely when $i\leq j$ (composition is forced, identities are the relations $i\leq i$). Under this view the two definitions collapse to one word each. A **direct system** indexed by $I$ is a functor $F:(I,\leq)\to\mathcal{C}$: it assigns an object $F(i)=X_i$ to each index and a morphism $F(i\leq j)=f_{ij}$ to each relation, and *functoriality* — $F$ preserves identities and composition — is exactly the pair of axioms $f_{ii}=\mathrm{id}$ and $f_{jk}f_{ij}=f_{ik}$. An **inverse system** is a functor on the opposite category, $(I,\leq)^{\mathrm{op}}\to\mathcal{C}$, equivalently a contravariant functor; the arrow reversal $h_{ij}:Y_j\to Y_i$ is the contravariance. The condition that $I$ be **directed** is what makes $(I,\leq)$ a *filtered* category, and filteredness is precisely the hypothesis under which the colimit $\varinjlim$ (the direct limit) is computed by the simple "glue and identify eventually" formula and commutes with finite limits — a feature that fails for colimits over arbitrary diagrams. The limits themselves — the colimit of a direct system and the limit of an inverse system — are developed on [[Def - Direct and Inverse Limits]].

---

# Relate to Other Fields / Compression

The cleanest compression: **a directed system is a consistent family of objects-and-maps indexed so that any two indices can be compared further along, set up so that "the eventual image" of an element is unambiguous.** A direct system points its maps forward and is built to be *unioned*; an inverse system points them backward and is built to be *intersected as threads*.

**True name:** the true name of a directed set is **"any two demands can be met simultaneously"** — whatever finitely many indices you care about, there is a single later index dominating them all, so finite collections of constraints always have a common refinement. This is the operational form: in proofs you use it as "given $i_1,\dots,i_n$, pass to a common upper bound $k$ and work there", reducing a question about finitely many stages to a question about one stage. For a direct system the true name is **"a compatible diagram of maps you intend to glue"**; for an inverse system, **"a tower of approximations you intend to thread"**.

The same scaffolding appears across mathematics. In topology, the **neighbourhoods of a point** $x$, ordered by reverse inclusion ($U\leq V$ iff $U\supseteq V$), form a directed set (any two neighbourhoods contain a common smaller one — their intersection), and the rings of functions on them form a direct system whose limit is the **stalk/germ**. In analysis, the **finite subsets of an index set**, ordered by inclusion, form a directed set, and an unordered sum is the direct limit (net) of its finite partial sums. The **truncation tower** $R/\mathfrak{a}^{n+1}\to R/\mathfrak{a}^n$ over $(\mathbb{N},\leq)$ is the inverse system whose limit is the [[Def - The I-adic Completion|completion]]. Directed sets are the indexing devices for **nets** in point-set topology, the generalisation of sequences that handles non-metrizable convergence.

---

# Examples / Corollaries

**Is an instance — $(\mathbb{N},\leq)$ and the finite fields.** The natural numbers with the usual order are directed (take the max). With $X_i = \mathbb{F}_{p^{i!}}$ and $f_{i,i+1}:\mathbb{F}_{p^{i!}}\hookrightarrow\mathbb{F}_{p^{(i+1)!}}$ the field inclusion (legal because $i!\mid(i+1)!$), and $f_{ij}$ the composite of intermediate inclusions, the coherence condition holds because field inclusions compose, giving a direct system whose colimit is $\overline{\mathbb{F}_p}$. Reversing to $Y_i=\mathbb{Z}/p^i\mathbb{Z}$ with the projections $h_{i,i+1}:\mathbb{Z}/p^{i+1}\twoheadrightarrow\mathbb{Z}/p^i$ gives an inverse system whose limit is $\mathbb{Z}_p$.

**Is an instance — the divisibility poset.** Let $I = \mathbb{N}_{\geq 1}$ ordered by *divisibility*, $a\leq b\iff a\mid b$. This is directed: any two integers have a common multiple (e.g. their product), even though most pairs are incomparable. The finite fields $\mathbb{F}_{p^n}$ with embeddings $\mathbb{F}_{p^a}\hookrightarrow\mathbb{F}_{p^b}$ whenever $a\mid b$ form a direct system over *this* poset, and the rings $\mathbb{Z}/n\mathbb{Z}$ with projections form an inverse system whose limit is $\widehat{\mathbb{Z}}=\prod_p\mathbb{Z}_p$. This example shows the index need not be a chain.

**Is an instance — neighbourhoods of a point.** For a topological space and a point $x$, the open neighbourhoods $U\ni x$ ordered by reverse inclusion form a directed set: given $U,V\ni x$, the neighbourhood $U\cap V$ is below both. The continuous functions on each $U$, with restriction maps, form a direct system whose colimit is the germ ring at $x$.

**Is NOT an instance — an antichain.** Let $I=\{a,b\}$ with $a,b$ incomparable and no upper bound (the order has only $a\leq a$, $b\leq b$). This is a poset but **not directed**: $a$ and $b$ have no common upper bound. A "direct system" over it is just two unrelated objects $X_a,X_b$ with no transition maps, and the would-be direct limit degenerates to the coproduct $X_a\sqcup X_b$ with no identifications possible — the gluing mechanism has nothing to act on. This is exactly the failure of transitivity the directedness axiom is designed to prevent.

**Is NOT an instance — a non-coherent family of maps.** Take $X_0=X_1=X_2=\mathbb{Z}$ over $(\{0,1,2\},\leq)$, with $f_{01}=\mathrm{id}$, $f_{12}=\mathrm{id}$, but $f_{02}=(\text{multiply by }2)$. Then $f_{12}\circ f_{01}=\mathrm{id}\neq f_{02}$, so the coherence axiom fails and this is *not* a direct system: the image of $1\in X_0$ in $X_2$ is ambiguous (it is $1$ along the two-hop route, $2$ along the direct route), and no well-defined limit exists.

**Corollary — common refinement of finitely many indices.** In any directed set, every *finite* subset $\{i_1,\dots,i_n\}$ has a common upper bound. (Induct: a bound for $\{i_1,\dots,i_{n-1}\}$ and $i_n$ have a common bound by directedness.) This is the form of directedness used in practice — "pass to a stage dominating all the indices currently in play".

**Calibration check.** Verify that $(\mathbb{N},\leq)$, the divisibility poset $(\mathbb{N}_{\geq1},\mid)$, and the reverse-inclusion order on neighbourhoods of a point are all directed, and that an antichain with $\geq 2$ elements is not. Confirm that the coherence axiom $f_{jk}f_{ij}=f_{ik}$ is exactly functoriality of the assignment $i\mapsto X_i$, and that reversing all arrows turns a direct system into an inverse system. Finally check the finite-refinement corollary by hand for $\{i_1,i_2,i_3\}$.

---

# Unlocked by This

> [!tip] Filtered colimits and exactness *(from Homological Algebra)*
> Because the index is **directed (filtered)**, the direct limit $\varinjlim$ is an *exact* functor on modules — it commutes with finite limits, so it preserves kernels and cokernels and turns injections into injections. This is special to filtered diagrams: a colimit over a non-filtered shape (e.g. a pushout) is only right exact. Filteredness is the precise hypothesis that makes "take the union" behave homologically like a harmless operation, and it is why $\varinjlim$ of injective resolutions computes cohomology of a rising union.

> [!tip] Nets and convergence in general topology *(from Topology)*
> A **net** in a space is a function from a directed set into the space, generalising sequences (indexed by $(\mathbb{N},\leq)$) to handle convergence in non-metrizable spaces where sequences are insufficient. Directedness is exactly what lets "eventually" make sense — a property holds eventually if it holds for all indices beyond some stage, and finite intersections of "eventually" sets are again "eventually" because finitely many tail-conditions have a common later index. Compactness, continuity, and closure are all characterised by net convergence, and the directed-set axiom here is the same one.

> [!tip] Profinite groups and infinite Galois theory *(from Number Theory / Galois Theory)*
> An inverse system of finite groups along surjections, indexed by a directed set, has a limit that is a **profinite group** — compact, totally disconnected, the Galois group of an infinite algebraic extension. The directed indexing (finite subextensions ordered by inclusion) is what assembles all the finite Galois groups into one, and the inverse-limit topology is the Krull topology on $\mathrm{Gal}(\overline{K}/K)$.

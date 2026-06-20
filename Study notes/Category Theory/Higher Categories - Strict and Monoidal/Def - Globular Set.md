---
type: definition
subject: higher-categories
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Presheaf"
tags: [category-theory, higher-categories, foundations]
---

# Notation

A globular set has cells in every dimension $n \geq 0$. We write $X_n$ for the set of **$n$-cells**, and reserve the words **object** for a $0$-cell, **arrow** or **morphism** for a $1$-cell, and **$2$-cell**, **$3$-cell**, and so on for the higher dimensions. Each $n$-cell for $n \geq 1$ has a **source** and a **target**, both $(n-1)$-cells, given by functions $s, t : X_n \to X_{n-1}$. A picture of a $0$-, $1$-, and $2$-cell is a point, an arrow between points, and a "bigon" $\alpha$ filling the region between two parallel arrows $f, g : a \to b$:
$$a \overset{f}{\underset{g}{\rightrightarrows}} b, \qquad \alpha : f \Rightarrow g.$$
The category $\mathbb{G}$ encoding this data is the **globe category**; its objects are the formal symbols $[0], [1], [2], \dots$, one per dimension. A globular set is a [[Def - Presheaf|presheaf]] on $\mathbb{G}$, i.e. a [[Def - Functor|functor]] $X : \mathbb{G}^{op} \to \mathbf{Set}$. The full registry is on [[Higher Categories — Strict n-Categories and Notions of Monoidal Category]].

---

# Axiom Motivation

The right way to find this definition is to ask what bare combinatorial data a higher category should carry *before* any composition is imposed. An ordinary [[Def - Category|category]] is a directed graph (objects and arrows) plus composition; if we strip the composition away we are left with a graph: a set of vertices $X_0$, a set of edges $X_1$, and two functions $s, t : X_1 \to X_0$ assigning to each edge its endpoints. A higher category should be the same kind of skeleton but with cells in every dimension: $2$-cells between parallel $1$-cells, $3$-cells between parallel $2$-cells, and so on. A globular set is exactly that skeleton — the underlying shape of an $\omega$-category with all composition forgotten.

So we want, for each $n$, a set $X_n$ of $n$-cells, and for $n \geq 1$ source and target maps $s, t : X_n \to X_{n-1}$ telling us which $(n-1)$-cells a given $n$-cell runs between. The only question is which equations $s$ and $t$ must satisfy. Here the geometry of a bigon forces the answer. A $2$-cell $\alpha$ runs between two parallel arrows $f, g : a \to b$. "Parallel" means $f$ and $g$ have the **same source** and the **same target**: $s(f) = s(g) = a$ and $t(f) = t(g) = b$. Now $f = s(\alpha)$ and $g = t(\alpha)$, so $a = s(s(\alpha)) = s(t(\alpha))$ and $b = t(s(\alpha)) = t(t(\alpha))$. Reading these off as identities of functions, we obtain the **globularity equations**:
$$s \circ s = s \circ t, \qquad t \circ s = t \circ t \qquad (\text{as maps } X_n \to X_{n-2}).$$
In words: the source of the source equals the source of the target, and the target of the source equals the target of the target. These are the *only* axioms.

Why exactly these and not, say, the simplicial identities? Because the shape of a cell here is a **globe** — an $n$-disk whose boundary $(n-1)$-sphere is split into a lower hemisphere (the source) and an upper hemisphere (the target). The two hemispheres of an $n$-cell must agree along their common equator, which is the boundary $(n-2)$-sphere; the globularity equations are precisely the statement that the equator is well-defined. If we dropped, say, the first equation $ss = st$, a $2$-cell could have a source-arrow and a target-arrow with *different* starting points, and there would be no consistent "left endpoint" of the bigon — the picture would not close up. Drop both equations and an $n$-cell would be an utterly unconstrained pair of $(n-1)$-cells, losing all the geometry.

It is illuminating to contrast the globular shape with the two other standard shapes. A **simplicial set** (see [[Def - Simplicial Set]]) uses simplices — a $2$-cell is a *triangle* with three faces, modelling a chosen composite $g \circ f$ together with a $1$-cell witnessing it. An **opetopic set** uses many-in-one-out pasting diagrams. The globular shape is the most economical: an $n$-cell has exactly *two* faces, a single source and a single target, which is why it is the natural shape for *strict* higher categories, where composites are uniquely determined and need no extra witnessing data. The price is paid later: defining *weak* composition on globular cells is genuinely hard, which is the whole story of globular operads (see [[Higher Categories — Globular Operads and Weak n-Categories]]).

One more design decision deserves a word. We could try to define the data by hand in every dimension — a tower of sets and maps with the globularity equations — or we could package it as a presheaf on a small category $\mathbb{G}$ whose morphisms *are* the source and target inclusions. The presheaf packaging is not mere bookkeeping: it makes the category of globular sets automatically complete, cocomplete, and a topos, and it makes "globular set" an instance of the single most reusable construction in category theory, the [[Def - Presheaf|category of presheaves]]. That is the route we take in the Categorical Definition.

---

# The Definition

A **globular set** $X$ consists of:

- a set $X_n$ for each integer $n \geq 0$ (the set of **$n$-cells**);
- for each $n \geq 1$, **source** and **target** functions $s, t : X_n \to X_{n-1}$,

such that the **globularity equations** hold for all $n \geq 2$:
$$s \circ s = s \circ t, \qquad t \circ s = t \circ t \qquad (X_n \to X_{n-2}).$$

A **morphism of globular sets** $\varphi : X \to Y$ is a family of functions $\varphi_n : X_n \to Y_n$ commuting with all sources and targets: $s \circ \varphi_n = \varphi_{n-1} \circ s$ and $t \circ \varphi_n = \varphi_{n-1} \circ t$. Globular sets and their morphisms form the category $\mathbf{GSet}$ (also written $[\mathbb{G}^{op}, \mathbf{Set}]$).

Two $n$-cells $x, y$ are **parallel** if either $n = 0$, or $n \geq 1$ and $s(x) = s(y)$ and $t(x) = t(y)$. A higher cell may only run between parallel cells; the globularity equations guarantee that the source and target of any $(n+1)$-cell are automatically parallel.

An **$n$-globular set** (or **$n$-truncated** globular set) is the same data but with cells only in dimensions $0$ through $n$ — equivalently, a presheaf on the full subcategory $\mathbb{G}_{\leq n} \subseteq \mathbb{G}$ on the objects $[0], \dots, [n]$. A $0$-globular set is a set; a $1$-globular set is a directed graph; a $2$-globular set is the underlying data of a [[Def - 2-Category and Bicategory|2-category]] with composition forgotten.

---

# Categorical / Structural Definition

The **globe category** $\mathbb{G}$ has objects $[0], [1], [2], \dots$, and is generated by two families of arrows
$$\sigma_n, \tau_n : [n-1] \to [n] \qquad (n \geq 1),$$
the **source** and **target** inclusions, subject to the **co-globularity relations**
$$\sigma_n \circ \sigma_{n-1} = \tau_n \circ \sigma_{n-1}, \qquad \sigma_n \circ \tau_{n-1} = \tau_n \circ \tau_{n-1}.$$
(These are the equations above with the arrows reversed, because a presheaf is a *contravariant* functor: $X(\sigma_n) = s$ and $X(\tau_n) = t$, and contravariance flips $s\circ s = s \circ t$ into $\sigma_n \circ \sigma_{n-1} = \tau_n \circ \sigma_{n-1}$.) Geometrically $[n]$ is the $n$-globe and $\sigma_n, \tau_n$ embed the $(n-1)$-globe as the lower and upper hemispheres of its boundary.

A **globular set is precisely a presheaf on $\mathbb{G}$**: a [[Def - Functor|functor]] $X : \mathbb{G}^{op} \to \mathbf{Set}$. The functor sends $[n] \mapsto X_n$ and sends $\sigma_n \mapsto s$, $\tau_n \mapsto t$; the co-globularity relations become exactly the globularity equations. A morphism of globular sets is a [[Def - Natural Transformation|natural transformation]] of such functors. This identifies $\mathbf{GSet} = [\mathbb{G}^{op}, \mathbf{Set}]$ as a [[Def - Presheaf|presheaf category]], which immediately hands us a great deal of free structure.

This is more than a slogan. As a [[Def - Presheaf|presheaf category]], $\mathbf{GSet}$ has all [[Def - Limit and Colimit|limits and colimits]], computed pointwise (dimension by dimension); it is cartesian closed and is in fact an elementary topos. The [[Thm - The Yoneda Lemma|Yoneda lemma]] tells us the representable presheaves $\mathbb{G}(-, [n])$ are the **standard $n$-globes** $G_n$ — the free globular set on a single $n$-cell — and that maps out of $G_n$ into any $X$ are exactly the $n$-cells of $X$, $\mathbf{GSet}(G_n, X) \cong X_n$. The standard globes are to globular sets what the standard simplices $\Delta^n$ are to simplicial sets: the basic shapes that probe and build everything else.

---

# Relate to Other Fields / Compression

A globular set is the **shape of a higher category**, exactly as a directed graph is the shape of a category and a quiver is the shape of a path algebra. The single underlying idea across all of higher category theory is that you first fix a *shape category* — globes $\mathbb{G}$, simplices $\Delta$, or opetopes — take presheaves on it to get the raw cellular data, and then impose composition. Globular sets are the shape choice that makes *strict* composition cleanest, because a globular $n$-cell has a unique source and a unique target, so a strict composite is uniquely determined with no auxiliary witnessing cell.

**True name:** a globular set is "a graph with cells in every dimension, where every cell has exactly one source and one target one dimension down, and the source and target share a boundary." Operationally, when you meet a globular set, do not picture the presheaf machinery first — picture the tower $X_0 \leftleftarrows X_1 \leftleftarrows X_2 \leftleftarrows \cdots$ of sets, each with a pair of maps to the one below, satisfying "source-of-source = source-of-target." When you want theorems for free (limits, colimits, the free globular set on a cell), *then* remember it is a [[Def - Presheaf|presheaf]] on $\mathbb{G}$.

The compression worth carrying away is that **globular set : strict $\omega$-category :: directed graph : category**. A category is a graph with a chosen, unique, associative composition; a strict [[Def - Strict n-Category and Strict ω-Category|$\omega$-category]] is a globular set with chosen, unique, associative composition in every dimension. The free-forgetful adjunction in the bottom row (free category on a graph) reappears in every dimension as the free-strict-$\omega$-category functor on a globular set, whose monad is the central object of the operadic approach to weak higher categories.

---

# Examples / Corollaries

**Is an instance — the standard $n$-globe $G_n$.** The free globular set on a single $n$-cell has exactly two cells in each dimension $0, 1, \dots, n-1$ (the iterated source and target boundaries) and a single cell in dimension $n$ (and nothing above). For $n = 0$ it is a point; for $n = 1$ it is a single arrow $a \to b$ between two distinct objects; for $n = 2$ it is a single bigon $\alpha : f \Rightarrow g$ between two parallel arrows $f, g : a \to b$, so it has two $0$-cells, two $1$-cells, and one $2$-cell. By [[Thm - The Yoneda Lemma|Yoneda]] these are the representable presheaves $\mathbb{G}(-, [n])$.

**Is an instance — the underlying globular set of any strict $\omega$-category.** Forgetting all the composition operations of a strict [[Def - Strict n-Category and Strict ω-Category|$\omega$-category]] leaves precisely a globular set: the cells and their sources and targets remain, the composites are discarded. This forgetful functor $\omega\text{-}\mathbf{Cat} \to \mathbf{GSet}$ has a left adjoint, the free strict $\omega$-category functor.

**Is an instance — the underlying globular set of a topological space (the fundamental $\omega$-groupoid, truncated to data).** Take $X_0$ to be the points of a space $T$, $X_1$ the paths, $X_2$ the homotopies between paths, $X_3$ the homotopies between homotopies, and so on; source and target of a homotopy are its two boundary paths. The globularity equations hold because a homotopy of paths fixes the endpoints. (Imposing composition makes this the **fundamental $\omega$-groupoid**, the bridge to the homotopy hypothesis.)

**Is NOT an instance — a simplicial set as it stands.** A [[Def - Simplicial Set]] $S$ has a $2$-simplex with *three* faces $d_0, d_1, d_2 : S_2 \to S_1$, not a source/target pair, and these satisfy the simplicial identities $d_i d_j = d_{j-1} d_i$ for $i < j$, not the globularity equations. The two shapes are genuinely different: a triangle is not a bigon. One can convert between the associated theories, but a simplicial set is not literally a globular set.

**Is NOT an instance — a tower of sets with maps violating globularity.** Take $X_0 = \{a, b, c\}$, $X_1 = \{f\}$ with $s(f) = a$, $t(f) = b$, and $X_2 = \{\alpha\}$ with $s(\alpha) = t(\alpha) = f$. This satisfies globularity. But if instead we had two arrows $f : a \to b$ and $g : b \to c$ and tried to put a $2$-cell $\alpha$ with $s(\alpha) = f$, $t(\alpha) = g$, then $s(s(\alpha)) = a$ while $s(t(\alpha)) = b$: globularity fails, and indeed there is no bigon between non-parallel arrows. The data is not a globular set.

**Calibration check.** Verify that a $1$-truncated globular set is the same thing as a directed graph (a set of vertices, a set of edges, two endpoint maps), and that there is no constraint to check because the globularity equations first appear in dimension $2$. Confirm that in the standard $2$-globe $G_2$ the two $1$-cells $f, g$ are parallel, i.e. $s(f) = s(g)$ and $t(f) = t(g)$, so that the single $2$-cell is allowed to exist. Finally, check that the source and target of *any* $2$-cell in *any* globular set are forced to be parallel arrows — this is the content of the globularity equations, and it is what makes the bigon picture always legitimate.

---

# Unlocked by This

> [!tip] Strict and Weak ω-Categories *(from this chapter)*
> A globular set with associative, unital, strictly compatible composition in every dimension is a strict [[Def - Strict n-Category and Strict ω-Category|ω-category]]. Replacing strict equality by coherent fillers turns globular sets into the carriers of **Batanin–Leinster weak ω-categories**, the subject of globular operads.

> [!tip] The Free Strict ω-Category Monad *(from Higher Category Theory)*
> The free-strict-ω-category functor on globular sets generates a monad $T$ on $\mathbf{GSet}$ whose operations are **globular pasting diagrams**. This monad is **cartesian**, and a **globular operad** is a cartesian morphism into it — the engine that produces weak higher categories of every signature.

> [!tip] The Homotopy Hypothesis *(from Algebraic Topology)*
> Grothendieck's **homotopy hypothesis** asserts that weak ω-groupoids — globular sets with weakly invertible composition in every dimension — model topological spaces up to homotopy. The globular shape is one of the candidate frameworks in which this conjecture is precisely stated and attacked.

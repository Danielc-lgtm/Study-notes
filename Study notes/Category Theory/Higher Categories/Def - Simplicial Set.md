---
type: definition
subject: higher-categories
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Presheaf"
  - "Def - The Yoneda Embedding"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

The **simplex category** $\Delta$ has objects the nonempty finite ordinals $[n] = \{0 < 1 < \dots < n\}$ for $n \ge 0$, and morphisms the order-preserving (monotone, weakly increasing) functions. We write $d^i : [n-1] \to [n]$ for the **$i$th coface** (the injection skipping $i$) and $s^i : [n+1] \to [n]$ for the **$i$th codegeneracy** (the surjection repeating $i$). A **simplicial set** is a [[Def - Presheaf|presheaf]] $X : \Delta^{op} \to \mathbf{Set}$; we write $X_n = X([n])$ for its set of **$n$-simplices**, $d_i = X(d^i) : X_n \to X_{n-1}$ for the **face maps**, and $s_i = X(s^i) : X_n \to X_{n+1}$ for the **degeneracy maps**. The category of simplicial sets is $\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}]$. The standard $n$-simplex is $\Delta^n = \Delta(-, [n])$; the horn $\Lambda^n_i \subseteq \Delta^n$ is defined below. The full registry is on [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories]].

---

# Axiom Motivation

A simplicial set is a recipe for *building a space out of combinatorial simplices* — points, edges, triangles, tetrahedra, and so on — by recording which simplices there are and how they are glued along their faces. The motivating problem is this: we want a purely set-theoretic, fully algebraic gadget that nonetheless carries the homotopy type of a space, so that homotopy theory can be done by manipulating sets and functions rather than open covers and continuous maps. The triangulated surfaces of classical topology are the prototype, but we want something cleaner: a structure where the combinatorics of faces is governed by a category, so that all the gluing data is captured by functoriality.

Start from the data of a space cut into simplices. For each $n$ there is a set $X_n$ of $n$-dimensional simplices. Each $n$-simplex has $n+1$ faces, themselves $(n-1)$-simplices, obtained by deleting one vertex; this gives $n+1$ **face maps** $d_0, \dots, d_n : X_n \to X_{n-1}$. There is one subtlety that makes the theory work, and it is the reason we use $\Delta$ rather than a category of plain finite sets: we also allow **degenerate** simplices — an $n$-simplex that is "really" a lower-dimensional simplex with a repeated vertex. These are recorded by **degeneracy maps** $s_0, \dots, s_{n-1} : X_{n-1} \to X_n$. Degeneracies look like bookkeeping but are essential: they are what make the homotopy theory of simplicial sets equivalent to that of spaces (without them one gets only "semi-simplicial sets", which behave worse).

Now, the faces and degeneracies are not independent; they satisfy a fixed list of identities (delete vertex $i$ then vertex $j$ in the right order, etc.). Writing those identities by hand is painful and error-prone. The decisive simplification is to notice that *all* of them are encoded by the morphisms of one small category: the cofaces $d^i$ and codegeneracies $s^i$ generate every order-preserving map between finite ordinals, and the relations among them — the **cosimplicial identities** — are exactly the relations among order-preserving maps. So instead of positing faces, degeneracies, and a list of identities, we can say in one breath: *a simplicial set is a functor $X : \Delta^{op} \to \mathbf{Set}$.* The face and degeneracy maps and all their relations are then *automatic*, being the images under $X$ of the cofaces, codegeneracies, and their composites. This is the whole reason for defining $\Delta$ first.

Why the *opposite* category $\Delta^{op}$? Because a simplex is determined by its faces, and "taking a face" goes from higher dimension to lower — it is *contravariant* in the dimension. An order-preserving injection $d^i : [n-1] \hookrightarrow [n]$ in $\Delta$ should induce a map $X_n \to X_{n-1}$ (an $n$-simplex has an $(n-1)$-dimensional $i$th face), which is contravariant; functoriality on $\Delta^{op}$ delivers exactly this. So a simplicial set is a [[Def - Presheaf|presheaf]] on $\Delta$, and the whole apparatus of presheaf theory — limits and colimits computed pointwise, the [[Def - The Yoneda Embedding|Yoneda embedding]], representability — becomes available for free.

What if we used all finite sets and all functions instead of finite *ordinals* and *order-preserving* maps? Then we would get **symmetric simplicial sets**, where simplices have no preferred vertex ordering. These exist and are useful, but they do *not* model spaces correctly — the ordering is what lets a simplicial set know the *direction* of its edges, which is exactly what is needed to encode a *category* (via the nerve) and, ultimately, an $\infty$-category. Order is not a blemish to be removed; it is the feature that makes simplicial sets simultaneously model spaces and categories. Dropping the order loses the directedness that quasi-categories depend on.

---

# The Definition

**The simplex category.** $\Delta$ is the category whose objects are the totally ordered sets $[n] = \{0 < 1 < \dots < n\}$ ($n \ge 0$) and whose morphisms $[m] \to [n]$ are the order-preserving functions. Every morphism factors uniquely as a surjection followed by an injection; the injections are generated by the **cofaces**
$$d^i : [n-1] \to [n] \quad (0 \le i \le n), \qquad d^i(j) = \begin{cases} j & j < i \\ j+1 & j \ge i \end{cases}$$
(the unique injection missing $i$), and the surjections by the **codegeneracies**
$$s^i : [n+1] \to [n] \quad (0 \le i \le n), \qquad s^i(j) = \begin{cases} j & j \le i \\ j-1 & j > i \end{cases}$$
(the unique surjection hitting $i$ twice). These satisfy the **cosimplicial identities**: $d^j d^i = d^i d^{j-1}$ for $i < j$; $s^j s^i = s^i s^{j+1}$ for $i \le j$; and $s^j d^i = d^i s^{j-1}$, $\mathrm{id}$, or $d^{i-1} s^j$ according as $i < j$, $i \in \{j, j+1\}$, or $i > j+1$.

**Simplicial set.** A **simplicial set** is a functor $X : \Delta^{op} \to \mathbf{Set}$. We write $X_n := X([n])$, the **$n$-simplices**, and define
$$d_i := X(d^i) : X_n \to X_{n-1} \ (\text{**face maps**}), \qquad s_i := X(s^i) : X_n \to X_{n+1} \ (\text{**degeneracy maps**}),$$
which satisfy the **simplicial identities** (the duals of the cosimplicial ones): for $i < j$, $d_i d_j = d_{j-1} d_i$, and so on. A **morphism of simplicial sets** is a natural transformation. This defines $\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}]$.

**Standard simplex and horns.** The **standard $n$-simplex** is the representable presheaf
$$\Delta^n := \Delta(-, [n]), \qquad \Delta^n_k = \Delta([k], [n]) = \{\text{order-preserving maps } [k] \to [n]\}.$$
By the [[Def - The Yoneda Embedding|Yoneda lemma]], maps $\Delta^n \to X$ correspond bijectively to $n$-simplices of $X$: $\mathbf{sSet}(\Delta^n, X) \cong X_n$. The **boundary** $\partial\Delta^n \subset \Delta^n$ is the union of the images of the $n+1$ face inclusions $\Delta^{n-1} \xrightarrow{d^i} \Delta^n$. The **$i$th horn** $\Lambda^n_i \subseteq \Delta^n$ is the union of all faces *except* the $i$th:
$$\Lambda^n_i = \bigcup_{j \ne i} d^j(\Delta^{n-1}) \;\subseteq\; \partial\Delta^n \;\subseteq\; \Delta^n.$$
Equivalently, $(\Lambda^n_i)_k$ consists of those maps $f : [k] \to [n]$ whose image does *not* contain $[n] \setminus \{i\}$. The horn is called **inner** if $0 < i < n$ and **outer** if $i \in \{0, n\}$.

---

# Categorical / Structural Definition

The structural definition is the one already given: **a simplicial set is a [[Def - Presheaf|presheaf]] on the simplex category**, $X : \Delta^{op} \to \mathbf{Set}$, and $\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}]$ is a presheaf category. This single sentence buys a great deal. Because $\mathbf{Set}$ is complete and cocomplete and limits and colimits in a functor category are computed *pointwise* ([[Thm - Limits in Set and in Functor Categories]]), $\mathbf{sSet}$ is itself complete and cocomplete: products, coproducts, pushouts, and all colimits of simplicial sets exist and are computed level by level, $(X \times Y)_n = X_n \times Y_n$, $(X \sqcup Y)_n = X_n \sqcup Y_n$, and so on. Every simplicial set is a colimit of standard simplices — the **density / co-Yoneda** formula $X \cong \mathrm{colim}_{\Delta^n \to X} \Delta^n$ exhibits $X$ as glued from its simplices — which is exactly the input needed to define geometric realisation (see [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]]).

The [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \Delta \to \mathbf{sSet}$, $[n] \mapsto \Delta^n$, is the source of the standard simplices, and the Yoneda lemma $\mathbf{sSet}(\Delta^n, X) \cong X_n$ is the reason one *never* enumerates simplices by hand: an $n$-simplex of $X$ *is* a map out of $\Delta^n$, and a horn-filling problem $\Lambda^n_i \to X$ extending to $\Delta^n \to X$ is a lifting problem in the presheaf category.

---

# Relate to Other Fields / Compression

A simplicial set is the combinatorial skeleton of a space. The compression is: **replace "continuous map from a triangle" by "an element of a set $X_2$", and let a category bookkeep the faces.** This trades topology for algebra without losing homotopy type, which is why simplicial sets are the workhorse of modern homotopy theory.

**True name:** a simplicial set is "a presheaf on finite ordinals" — equivalently, "a set of simplices in each dimension, glued by face and degeneracy maps satisfying the simplicial identities." The presheaf description is the one to *think* (it gives all the categorical machinery for free); the face/degeneracy description is the one to *compute* with.

The connection to singular homology is direct and historical: the **singular simplices** of a space $X$ — continuous maps $|\Delta^n| \to X$ — form a simplicial set $\mathrm{Sing}(X)$, and its associated chain complex computes singular homology (see [[Def - Singular Simplex]]). Conversely every simplicial set has a [[Def - Topological Space|topological]] realisation $|X|$. So simplicial sets sit exactly between combinatorics and topology, and the equivalence of their homotopy theories with that of spaces is the foundational theorem of the subject.

---

# Examples / Corollaries

**Is an instance — the standard simplices $\Delta^n$.** $\Delta^0$ is a single point in every positive degree only via degeneracies (it has one non-degenerate $0$-simplex and nothing else non-degenerate). $\Delta^1$ has two non-degenerate $0$-simplices (vertices $0, 1$) and one non-degenerate $1$-simplex (the edge $0 \to 1$); it is the "directed interval". $\Delta^2$ adds a single non-degenerate triangle with three vertices and three edges. By Yoneda, $\Delta^n_k = \Delta([k],[n])$ is the set of monotone maps, e.g. $\Delta^2_1 = \{$the six monotone maps $[1] \to [2]\}$, which are the three edges plus three degenerate (constant-ish) edges.

**Is an instance — the nerve of a category.** For any [[Def - Category|category]] $\mathcal{C}$, the **nerve** $N(\mathcal{C})$ has $N(\mathcal{C})_n = \{$strings of $n$ composable arrows$\}$; this is a simplicial set whose face maps compose adjacent arrows or drop end arrows and whose degeneracies insert identities (see [[Def - Kan Complex and the Nerve]]). It is the bridge from categories to simplicial sets.

**Is an instance — the singular complex of a space.** $\mathrm{Sing}(X)_n = \mathbf{Top}(|\Delta^n|, X)$, the [[Def - Singular Simplex|singular $n$-simplices]] of $X$, with faces given by restriction to the geometric faces of $|\Delta^n|$. This simplicial set is a Kan complex (see [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve]]).

**Is NOT a simplicial set — a "set of simplices" with no degeneracies.** If you record only $n$-simplices and face maps $d_i$ satisfying the face relations, but provide no degeneracy maps, you have a **semi-simplicial set** (also called a $\Delta$-set), a presheaf on the subcategory of $\Delta$ with only injections. This is *not* a simplicial set: it lacks the degeneracies, and its homotopy theory does not match that of spaces (it cannot detect, for example, that a constant map is a degenerate simplex). The degeneracies are exactly the data that distinguishes the two.

**Corollary — $\Lambda^n_i$ is a proper subobject of $\Delta^n$.** The horn omits the interior and the $i$th face, so $\Lambda^n_i \subsetneq \partial\Delta^n \subsetneq \Delta^n$ for $n \ge 2$. The inclusion $\Lambda^n_i \hookrightarrow \Delta^n$ is the lifting target in every horn-filling condition; for $n = 2$, $\Lambda^2_1$ is the two edges $0 \to 1 \to 2$ without the long edge $0 \to 2$ or the triangle, i.e. exactly "two composable arrows awaiting a composite".

**Calibration check.** Verify that $\Delta^1$ has exactly three non-degenerate simplices (two vertices and one edge), and write down the two face maps $d_0, d_1 : \Delta^1_1 \to \Delta^1_0$. Confirm using Yoneda that $\mathbf{sSet}(\Delta^0, X) \cong X_0$, the set of vertices of $X$. And check that the inner horn $\Lambda^2_1$ consists of the two edges $0 \to 1$ and $1 \to 2$ glued at the vertex $1$.

---

# Unlocked by This

> [!tip] Quasi-Categories and ∞-Categories *(from Higher Category Theory)*
> A [[Def - Simplicial Set|simplicial set]] satisfying the inner-horn-filling condition is a [[Def - Quasi-Category|quasi-category]] — Lurie's model of an $\infty$-category. The combinatorics defined here (faces, degeneracies, horns) is the entire substrate on which higher category theory runs.

> [!tip] The Kan–Quillen Model Structure *(from Model Categories — Chapter M)*
> $\mathbf{sSet}$ carries a **model structure** in which the fibrant objects are the [[Def - Kan Complex and the Nerve|Kan complexes]] and the weak equivalences are the maps inducing isomorphisms on **simplicial homotopy groups**; it is Quillen-equivalent to topological spaces. Simplicial sets are the standard combinatorial model for the homotopy theory of spaces.

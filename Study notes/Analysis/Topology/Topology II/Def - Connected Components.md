---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Connected Space"
  - "Def - Continuous Map"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ is a topological space. For $x \in X$, the **connected component of $x$**, denoted $C_x$, is the union of all connected subsets of $X$ containing $x$. The set of all connected components is denoted $\pi_0(X)$ — read "pi-zero of $X$". A **discrete-valued map** is a continuous map $d : X \to D$ where $D$ carries the discrete topology. The full registry of symbols is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Axiom Motivation

We have the notion of a [[Def - Connected Space|connected space]]. The natural question: given an arbitrary space, can we decompose it into "the largest connected pieces"? Just as a graph decomposes into connected components — maximal sets of mutually reachable vertices — we want every topological space to break canonically into its maximal connected subsets. The question is whether such maximal pieces exist, whether they partition the space, and whether they have any further structure.

The mechanical setup is the same as in any maximality argument. Fix a point $x \in X$ and ask: what is the largest connected subset of $X$ containing $x$? Define it directly as the union of *all* connected subsets containing $x$. For this to be a sensible definition we need: (i) at least one such subset to exist — trivially $\{x\}$ is connected; (ii) the union to itself be connected. The latter is the content of [[Thm - Union of Overlapping Connected Sets is Connected]]: any family of connected subsets that pairwise overlap (here, they all contain $x$) has connected union. So $C_x$, the union, is connected, and by construction it contains every connected subset of $X$ containing $x$. It is maximal among connected subsets containing $x$.

Why does this construction *partition* $X$? Define an equivalence relation $\sim$ on $X$ by $p \sim q$ if there exists a connected subset of $X$ containing both. Reflexivity is the singleton $\{p\}$; symmetry is trivial; transitivity uses the gluing theorem: if $p, q$ lie in connected $A$ and $q, r$ lie in connected $B$, then $A \cup B$ is connected (they share $q$) and contains $p, r$. So $\sim$ is an equivalence relation; its equivalence classes partition $X$; and the class of $x$ is exactly $C_x$. The connected components of $X$ are the equivalence classes.

A more subtle question: are connected components *open*, *closed*, or neither? They are always *closed*. The argument: if $C$ is a connected component containing $x$, then its closure $\overline{C}$ is also connected (closures of connected sets are connected — a corollary of the open-set characterisation), and $\overline{C}$ contains $x$, so by maximality $\overline{C} \subseteq C$, hence $\overline{C} = C$ and $C$ is closed. They are *not* always open. The standard non-example is $\mathbb{Q}$: every connected component is a singleton, but singletons are not open in $\mathbb{Q}$ (every neighbourhood of a rational contains other rationals). A space whose connected components are open is called *locally connected* — for such spaces, components are clopen, and the space is a disjoint union of its components in a topologically clean way (each component carries the subspace topology and the whole space is the topological coproduct of its components).

There is a closely related but inequivalent notion: the **quasi-component**. The quasi-component of $x$ is the intersection of all clopen subsets containing $x$, or equivalently the set of $y$ such that every discrete-valued map $d : X \to D$ satisfies $d(x) = d(y)$. Every connected component is contained in a quasi-component, since a connected set must be constant under every discrete-valued map, but the inclusion is sometimes strict — for example, in the space $X = \{(0, 0), (0, 1)\} \cup \bigcup_n \{1/n\} \times [0, 1]$ (a sequence of vertical segments collapsing onto two limit points), the connected components $\{(0, 0)\}$ and $\{(0, 1)\}$ are separate, but they are in the same quasi-component because every clopen subset containing one must contain enough nearby segments to also contain the other. Connected components are the "right" notion for most purposes, but the distinction matters in nontrivial settings (algebraic geometry, profinite groups).

A final motivating point: the partition into connected components is the *coarsest* partition of $X$ that respects connectedness — finer than the trivial partition $\{X\}$ but coarser than every partition that splits a connected set. It is the canonical way to extract the "connectivity skeleton" of a topological space. The set $\pi_0(X)$ of connected components is the first homotopy invariant of $X$ (zeroth, technically), and the function $X \mapsto \pi_0(X)$ is a functor from topological spaces to sets.

---

# The Definition

Let $X$ be a topological space.

**Connected component.** For $x \in X$, the **connected component of $x$**, denoted $C_x$, is the union of all connected subsets of $X$ containing $x$. Equivalently, $C_x$ is the equivalence class of $x$ under the relation "$p \sim q$ if there exists a connected subset of $X$ containing both $p$ and $q$".

**Properties.** Connected components have the following properties:

1. Each $C_x$ is connected.
2. Each $C_x$ is closed in $X$.
3. The set of connected components partitions $X$.
4. Every connected subset of $X$ is contained in a unique connected component.

**Quasi-component.** For $x \in X$, the **quasi-component** $Q_x$ of $x$ is the intersection of all clopen subsets of $X$ containing $x$. Equivalently, $Q_x = \{y \in X : d(x) = d(y)\text{ for every discrete-valued map } d : X \to D\}$. Every connected component is contained in a quasi-component: $C_x \subseteq Q_x$. The inclusion can be strict.

**$\pi_0(X)$.** The set of connected components of $X$ is denoted $\pi_0(X)$. A continuous map $f : X \to Y$ induces a function $\pi_0(f) : \pi_0(X) \to \pi_0(Y)$ sending the component $C_x$ to the component of $f(x)$.

---

# Relate to Other Fields / Compression

In **graph theory**, the connected components of a graph are the equivalence classes under "reachability via edges". This is the discrete prototype: a topological connected component is a connected piece, just as a graph component is a piece reachable by walking along edges. The function "number of connected components" generalises from $|V| - \text{rank}(\text{Laplacian})$ in graph theory to $\dim H_0(X; \mathbb{Q})$ in algebraic topology.

In **algebraic topology**, $\pi_0(X)$ — the *set* of connected components — refines into $H_0(X; \mathbb{Z}) = \mathbb{Z}^{\pi_0(X)}$, the **zeroth singular homology group**. The dimension of $H_0$ counts components, and the entire homology functor is built on top of this.

In **algebraic geometry**, the connected components of a scheme $\operatorname{Spec} R$ correspond to a product decomposition of the ring: $\operatorname{Spec} R = \coprod \operatorname{Spec} R_i$ iff $R = \prod R_i$, with each $R_i$ having connected spectrum (no nontrivial idempotents). So connected components of a scheme are the same as ring factorizations into "indecomposable" pieces. The fact that components are *closed* (not necessarily open) is critical here: schemes can have infinitely many components without being a coproduct.

In **statistical mechanics**, when a configuration space has multiple connected components, ergodicity and mixing properties can be studied within each component separately. The decomposition into components is the "block diagonalization" of the dynamics.

---

# Examples / Corollaries

**Is an instance — $\mathbb{R}$ has one component, namely $\mathbb{R}$ itself.** Since $\mathbb{R}$ is connected, the only maximal connected subset is $\mathbb{R}$ itself. Hence $\pi_0(\mathbb{R}) = \{\mathbb{R}\}$ — a one-element set.

**Is an instance — $\mathbb{R} \setminus \{0\}$ has two components.** The maximal connected subsets are $(-\infty, 0)$ and $(0, \infty)$. Hence $\pi_0(\mathbb{R} \setminus \{0\}) = \{(-\infty, 0), (0, \infty)\}$. This is the formal way to say "$\mathbb{R} \setminus \{0\}$ falls into two pieces", and the cleanest argument that $\mathbb{R} \setminus \{0\} \not\cong \mathbb{R}$: a homeomorphism preserves $\pi_0$, so removing a point cannot map a connected space to a two-component space.

**Is an instance — $\mathbb{Q}$ has uncountably many components, each a singleton.** Given any rational $p \in \mathbb{Q}$, pick irrationals $\alpha, \beta$ with $\alpha < p < \beta$. Then $\mathbb{Q} \cap (\alpha, \beta)$ is a clopen neighbourhood of $p$ in $\mathbb{Q}$, and by shrinking $\alpha \to p$ and $\beta \to p$ from below and above through irrationals, the only connected subset of $\mathbb{Q}$ containing $p$ is $\{p\}$. So $C_p = \{p\}$. The connected components are *not* open: $\{p\}$ is not open in $\mathbb{Q}$ (any open set in $\mathbb{Q}$ contains a $\mathbb{Q}$-interval, hence infinitely many points). $\mathbb{Q}$ is **totally disconnected**.

**Is an instance — $S^0 = \{-1, 1\}$ has two components, $\{-1\}$ and $\{1\}$.** Both components are open and closed (singletons in a finite space are clopen). Here components and quasi-components agree.

**Is an instance — the disjoint union of countably many circles.** $X = \coprod_n S^1_n$ (a countable disjoint union of circles, each topologically a circle) has $\pi_0(X) = \mathbb{N}$, with each $S^1_n$ a single component. Each component is open and closed.

**Is NOT an instance of a space whose components are open — $\mathbb{Q}$ (as above).** Or any totally disconnected space without isolated points: the Cantor set, the $p$-adic integers $\mathbb{Z}_p$, profinite groups.

**Counter-example for "components = quasi-components" — the spike space.** Consider $X = \{(0, 0), (0, 1)\} \cup \bigcup_n \{1/n\} \times [0, 1] \subset \mathbb{R}^2$: a sequence of vertical unit segments at $x = 1/n$ together with two isolated points at $(0, 0)$ and $(0, 1)$. The connected components are: each individual segment (these are obviously connected and maximal), the singleton $\{(0, 0)\}$, and the singleton $\{(0, 1)\}$. But the quasi-components merge $(0, 0)$ and $(0, 1)$: any clopen subset of $X$ containing $(0, 0)$ must contain almost every segment (because clopen sets of $X$ inherit clopen sets of the segments, which are clopen iff they are the whole segment or empty, and continuity forces "almost all" segments to go together), hence must contain $(0, 1)$ too. So $Q_{(0, 0)} = Q_{(0, 1)} = \{(0, 0), (0, 1)\}$, strictly larger than the connected component $\{(0, 0)\}$.

**Corollary — components are closed.** If $C$ is a connected component, then $\overline{C}$ is also connected (closures of connected sets are connected), and $\overline{C} \supseteq C$, so by maximality $\overline{C} = C$. Hence $C$ is closed. This is a calibration check on the definition.

**Corollary — connected components are intersections of clopen sets.** Each connected component is contained in some quasi-component, and quasi-components are intersections of clopen sets. So connected components are also intersections of clopen sets (possibly proper intersections). In particular, in a Hausdorff space where the only clopen sets are $\emptyset$ and the components themselves, components are clopen.

**Corollary — $\pi_0$ is a functor.** A continuous map $f : X \to Y$ sends each connected $C_x \subseteq X$ to the connected set $f(C_x) \subseteq Y$, which is contained in some component $C_{f(x)}^Y$. So $f$ induces a well-defined map $\pi_0(f) : \pi_0(X) \to \pi_0(Y)$, and composition is preserved.

**Calibration check.** Compute $\pi_0$ for: $\mathbb{R}^n$ (one component); $\mathbb{R}^n \setminus \{0\}$ for $n \geq 2$ (one component, by path-connectedness; for $n = 1$, two); $S^n$ (one for $n \geq 1$, two for $n = 0$); $\mathrm{GL}_n(\mathbb{R})$ (two components, distinguished by sign of determinant); the Cantor set (uncountably many components, each a singleton). Each computation tests a different aspect of the definition.

---

# Unlocked by This

> [!tip] **Zeroth Homology $H_0$** *(from Algebraic Topology)*
> The set $\pi_0(X)$ "lifts" to the abelian group $H_0(X; \mathbb{Z}) = \mathbb{Z}^{\pi_0(X)}$, the free abelian group on the components. This is the simplest piece of the homology of $X$ — and the only piece of singular homology that uses no information beyond the partition into components. The dimension of $H_0$ is the *number of components*.

> [!tip] **Total Disconnection and Profinite Groups** *(from Topology/Algebra)*
> A space is **totally disconnected** if every connected component is a singleton. Examples include $\mathbb{Q}$, the Cantor set, and the $p$-adic integers $\mathbb{Z}_p$. **Profinite groups** — inverse limits of finite groups — are totally disconnected compact Hausdorff topological groups, and their structure is determined by the lattice of open subgroups. This is the world of Galois theory of infinite extensions.

> [!tip] **Locally Connected Spaces** *(from this topic)*
> A space is **locally connected** if every neighbourhood of every point contains a connected open neighbourhood. For such spaces, connected components are *open* (in addition to closed), so the space is the topological coproduct of its components. Manifolds are locally connected; $\mathbb{Q}$ and the Cantor set are not.

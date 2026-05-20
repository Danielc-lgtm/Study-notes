---
type: definition
subject: topology
prereqs:
  - "Def - Continuous Map"
  - "Def - Topological Space"
tags: [analysis, topology]
---

# Notation

Throughout, $(X, \tau_X)$ and $(Y, \tau_Y)$ are topological spaces, and $f : X \to Y$ is a function. If $f$ is bijective, $f^{-1} : Y \to X$ denotes its inverse function. The notation $X \cong Y$ means $X$ is homeomorphic to $Y$. We will use $S^1 = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1\}$ for the unit circle, $S^n$ for the unit $n$-sphere in $\mathbb{R}^{n+1}$, and $D^n$ for the closed $n$-disc. For the full registry of symbols see [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Axiom Motivation

We have topological spaces; we have continuous maps. The next question is: when should we consider two topological spaces to be "the same"? Every mathematical theory has its own notion of equivalence — two sets are the same when there is a bijection, two groups when there is a group isomorphism, two vector spaces when there is a linear isomorphism. For topological spaces the analogous notion is a bijection that respects the topology in both directions. Call such a map a **homeomorphism**, and call two spaces *homeomorphic* if there is a homeomorphism between them.

The naive guess is: a homeomorphism should be a continuous bijection. After all, that is a function that respects the topology and is a bijection of underlying sets. But this is *not* enough, and the reason is one of the most important counterexamples in the subject.

Consider the **winding map** $f : [0, 2\pi) \to S^1$, $f(t) = (\cos t, \sin t)$. This wraps the half-open interval $[0, 2\pi)$ onto the circle exactly once. It is a *bijection*: each point of the circle has a unique preimage in $[0, 2\pi)$. It is *continuous*: standard from real analysis, $\sin$ and $\cos$ are continuous. So we have a continuous bijection. But is the *inverse* $f^{-1} : S^1 \to [0, 2\pi)$ continuous?

The answer is no, and the failure is easy to see. Pick the point $(1, 0) \in S^1$, which is $f(0)$. A small open neighbourhood of $(1, 0)$ on the circle is a short arc, say the arc with angles $(-\delta, \delta)$ modulo $2\pi$. Under $f^{-1}$, this arc maps to two disjoint half-intervals: $[0, \delta)$ near the "$0$" end and $(2\pi - \delta, 2\pi)$ near the other end (since the arc-end at $-\delta$ corresponds to $2\pi - \delta$ in the interval). The preimage of the arc-neighbourhood is *disconnected*: a small arc on the circle pulls back to a "broken" set in the interval. The map $f^{-1}$ does not send "near $(1,0)$" to "near $0$ in $[0, 2\pi)$" — it sends "near $(1, 0)$" to "near $0$ *and also* near $2\pi$". So $f^{-1}$ is discontinuous at $(1, 0)$.

What did this counterexample teach us? *Continuity of $f$ alone does not imply continuity of $f^{-1}$.* A bijective continuous map can "tear" or "glue" the topology in a way that the inverse cannot reverse smoothly. The right notion of equivalence must therefore demand continuity in *both* directions: $f$ continuous *and* $f^{-1}$ continuous. This gives the definition of a **homeomorphism**.

Why is this the right notion of equivalence, and not something weaker? Because *only* this notion preserves *every* topological property. Two homeomorphic spaces are indistinguishable to topology: every property phrased in terms of open sets (compactness, connectedness, Hausdorffness, separability, the number of connected components, the fundamental group) is shared by both. Conversely, if two spaces are *not* homeomorphic, then some topological property distinguishes them. This is the cleanest statement of what topology, *as a subject*, considers two spaces to be the same — and it is the criterion by which the classification of topological spaces is conducted.

A second reason: the inverse $f^{-1}$ of a continuous bijection is continuous if and only if $f$ is an **open map** (image of open is open) — that is, if and only if $f$ sends the topology of $X$ surjectively onto the topology of $Y$. This is the dual condition to continuity of $f$. So homeomorphism = "continuous and open and bijective", and the notion neatly captures the symmetry: $f$ sends opens to opens both ways.

A third reason: homeomorphism is the *isomorphism* in the category $\mathsf{Top}$. Categorically, two objects are isomorphic if there is an arrow $f : X \to Y$ and an arrow $g : Y \to X$ such that $g \circ f = \text{id}_X$ and $f \circ g = \text{id}_Y$. Applied to $\mathsf{Top}$ (continuous maps), this is exactly: $f$ continuous, $g$ continuous, $f$ and $g$ are mutually inverse bijections — i.e., a homeomorphism. The notion is determined by the category we are working in.

There is a special situation in which continuous bijection *does* imply homeomorphism: when $X$ is **compact** and $Y$ is **Hausdorff**. The proof routes through a small chain of facts: closed subsets of compact spaces are compact; continuous images of compact spaces are compact; compact subsets of Hausdorff spaces are closed. So $f$ sends closed sets to closed sets (compact → compact → closed), which is exactly the statement that $f^{-1}$ is continuous. This is one of the most useful facts in the subject — it lets one verify many homeomorphisms without explicitly checking the inverse — and it is proved in [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]]. The winding map fails this hypothesis because $[0, 2\pi)$ is not compact.

The notion of homeomorphism is the destination of the entire first chapter of topology. Once we know what it means for two spaces to be the same, we can ask: which spaces *are* the same? Which spaces *can* be told apart? This is the **classification problem** for topological spaces, and most of topology — connectedness, compactness, the fundamental group, the higher homotopy and homology groups, the Euler characteristic, the dimension — is the development of **topological invariants**: properties that distinguish non-homeomorphic spaces. The whole subject is organized around proving things like "$\mathbb{R}^n$ is not homeomorphic to $\mathbb{R}^m$ for $n \neq m$" (the **invariance of domain** theorem) and "the sphere is not homeomorphic to the torus" (uses fundamental group, or just connectedness vs. having a cut surface).

---

# The Definition

Let $(X, \tau_X)$ and $(Y, \tau_Y)$ be topological spaces.

A **homeomorphism** $f : X \to Y$ is a function satisfying:

1. $f$ is a bijection of sets.

2. $f$ is continuous.

3. The inverse function $f^{-1} : Y \to X$ is continuous.

Equivalently, $f$ is a continuous, open (or equivalently, closed), bijective map.

Two topological spaces $X$ and $Y$ are **homeomorphic**, written $X \cong Y$ or sometimes $X \approx Y$, if there exists a homeomorphism $f : X \to Y$. The relation $\cong$ is an equivalence relation: reflexive ($\text{id}_X$ is a homeomorphism), symmetric ($f^{-1}$ is a homeomorphism if $f$ is), transitive (compositions of homeomorphisms are homeomorphisms).

**Topological property / topological invariant.** A property $P$ of topological spaces is a **topological invariant** if $X \cong Y$ and $X$ has $P$ together imply $Y$ has $P$. Equivalently, $P$ is determined by the homeomorphism class.

**Topological embedding.** A continuous injective map $f : X \to Y$ is a **topological embedding** if $f$ is a homeomorphism onto its image $f(X) \subseteq Y$ (with the subspace topology). This is the topological notion of "$X$ sits inside $Y$".

---

# Categorical Definition

A homeomorphism is precisely an **isomorphism in the category $\mathbf{Top}$**. The vocabulary: in any category $\mathcal{C}$, an *isomorphism* is an arrow $f : X \to Y$ that admits an arrow $g : Y \to X$ — also a morphism of the category — such that $g \circ f = \mathrm{id}_X$ and $f \circ g = \mathrm{id}_Y$. The two-sided-inverse condition is what distinguishes "isomorphism" from "bijection": isomorphism demands that the inverse exist *as an arrow of the same category*, not merely as a set-theoretic inverse function. Applied to $\mathbf{Top}$, whose arrows are [[Def - Continuous Map|continuous maps]], a categorical isomorphism is a continuous map $f : X \to Y$ admitting a continuous two-sided inverse — which is exactly the three-clause definition above.

This categorical formulation immediately explains the asymmetry that the winding-map counterexample exposed. In the category $\mathbf{Set}$, where the arrows are *all* functions, every bijection is an isomorphism, because the set-theoretic inverse is automatically an arrow (every function is). But in a category with structured arrows — $\mathbf{Top}$, $\mathbf{Grp}$, $\mathbf{Ring}$, $\mathbf{Mod}_R$ — "set-theoretic inverse exists" and "set-theoretic inverse is an arrow" are *different* conditions, and only the latter gives an isomorphism. The phenomenon "continuous bijection need not be a homeomorphism" is the topological face of "the forgetful functor $\mathbf{Top} \to \mathbf{Set}$ does not reflect isomorphisms". The forgetful functors $\mathbf{Grp} \to \mathbf{Set}$ and $\mathbf{Ring} \to \mathbf{Set}$ *do* reflect isomorphisms (a bijective group or ring homomorphism is automatically an isomorphism), and that algebraic peculiarity is itself a special fact about purely algebraic categories.

From the [[Def - Topological Space#Categorical Definition|frame perspective]], a homeomorphism corresponds to an **isomorphism of frames** $f^{-1} : \tau_Y \xrightarrow{\sim} \tau_X$ — a bijection of open-set lattices preserving arbitrary joins and finite meets in both directions. The two topologies are equal *as lattices*, with the points merely relabelled. Homeomorphism invariants — connectedness, compactness, Hausdorffness, the fundamental group — are then exactly the properties of the frame that survive frame isomorphism, which is precisely why they are computable from the open-set lattice without reference to the underlying point set.

---

# Relate to Other Fields / Compression

A homeomorphism is the **isomorphism** in the category $\mathsf{Top}$ of topological spaces and continuous maps. The notion is *strictly* parallel to:

- **Bijection** in the category of sets ($\mathsf{Set}$).
- **Group isomorphism** in the category of groups ($\mathsf{Grp}$).
- **Linear isomorphism** in the category of vector spaces ($\mathsf{Vect}$).
- **Ring isomorphism** in $\mathsf{Ring}$, **smooth diffeomorphism** in $\mathsf{Diff}$, **biholomorphism** in $\mathsf{Hol}$, etc.

Each notion is "a morphism with a two-sided inverse that is also a morphism". The pattern is universal in mathematics.

In **differential geometry**, the stronger notion of **diffeomorphism** is a homeomorphism that is smooth in both directions. A diffeomorphism is in particular a homeomorphism, so diffeomorphic manifolds are homeomorphic — but the converse is famously false: in dimension 4 there are uncountably many pairwise-non-diffeomorphic smooth structures on $\mathbb{R}^4$ (the *exotic $\mathbb{R}^4$* phenomenon, due to Donaldson and Freedman), all of which are homeomorphic to standard $\mathbb{R}^4$. So smooth structure is finer than topological structure in dimension 4.

In **algebraic topology**, the central question is to compute *homotopy* equivalence classes rather than homeomorphism classes. Two spaces $X, Y$ are **homotopy equivalent** if there are continuous maps $f : X \to Y, g : Y \to X$ such that $g \circ f \simeq \text{id}_X$ and $f \circ g \simeq \text{id}_Y$ (where $\simeq$ denotes homotopy). Homeomorphic implies homotopy equivalent (taking $g = f^{-1}$), but homotopy equivalence is weaker — e.g. $\mathbb{R}^n$ is homotopy equivalent to a point but obviously not homeomorphic to a point.

In **functional analysis**, a homeomorphism between topological vector spaces that is also linear is a **topological isomorphism**. For Banach spaces this is "a bounded linear bijection with bounded inverse" — and the **open mapping theorem** says that a bounded linear bijection between Banach spaces *automatically* has a bounded inverse. So in the Banach world, continuous linear bijection ⟹ homeomorphism (the analogue of "compact source, Hausdorff target" succeeds in a different setting).

---

# Examples / Corollaries

**Is an instance — $\mathbb{R} \cong (a, b)$ for any $a < b$.** Use the homeomorphism $f : (a, b) \to \mathbb{R}$, $f(x) = \tan\big(\pi \frac{x - (a+b)/2}{b - a}\big)$. This is a continuous bijection (composition of an affine map onto $(-\pi/2, \pi/2)$ followed by $\tan$), and its inverse $\arctan$-composed-with-affine is continuous. So $\mathbb{R}$ is homeomorphic to *every* open interval, regardless of length.

**Is an instance — $\mathbb{R} \cong (0, \infty)$.** Use $f(x) = e^x$. Continuous, bijective, inverse $\log$ also continuous. So even the half-infinite interval is homeomorphic to $\mathbb{R}$ — the "size" of an interval, in any metric sense, is not a topological invariant.

**Is an instance — $S^1$ minus a point is homeomorphic to $\mathbb{R}$.** Remove the north pole $(0, 1)$ from the unit circle; the resulting space is homeomorphic to $\mathbb{R}$ via *stereographic projection* (or just the angle parameterization on $(-\pi, \pi)$). Same for $S^n$ minus a point ≅ $\mathbb{R}^n$ for any $n$.

**Is an instance — the unit interval $[0, 1]$ is homeomorphic to $[a, b]$ for $a < b$.** Linear map $x \mapsto a + (b - a)x$. Both directions are continuous.

**Is NOT an instance — $\mathbb{R} \not\cong S^1$.** Topological invariant: $\mathbb{R}$ becomes disconnected if you remove any single point ($\{0\}$ separates $\mathbb{R}$ into $(-\infty, 0)$ and $(0, \infty)$); $S^1$ remains connected when you remove any single point. So they cannot be homeomorphic. Equivalently: $\mathbb{R}$ has a *cut point* (a point whose removal disconnects), $S^1$ does not.

**Is NOT an instance — $\mathbb{R}^n \not\cong \mathbb{R}^m$ for $n \neq m$.** This is the **invariance of domain** theorem, proved by Brouwer in 1912 using methods of algebraic topology (in particular, homology or fundamental group computations for small $n$, and degree theory or homology in general). It is *not* a triviality: in fact, before Brouwer it was conjectured by Cantor that $\mathbb{R}$ and $\mathbb{R}^2$ have a continuous bijection (which Cantor disproved). The full statement "no continuous bijection" was open until invariance of domain. The result is the cornerstone reason that "dimension" is a topological invariant.

**Is NOT an instance — $[0, 1) \not\cong S^1$.** $[0, 1)$ has a non-cut point ($0$, whose removal leaves the connected $(0, 1)$) and cut points (every $t \in (0, 1)$ disconnects); $S^1$ has no cut points. So they are not homeomorphic. This is the canonical example of a continuous bijection from $[0, 1)$ to $S^1$ (the winding map $t \mapsto e^{2\pi i t}$) that is *not* a homeomorphism — the inverse fails to be continuous at the wrap-around point.

**Is NOT an instance — the winding map $f : [0, 2\pi) \to S^1, f(t) = (\cos t, \sin t)$ is a continuous bijection but not a homeomorphism.** The inverse is discontinuous at $(1, 0)$: a small neighbourhood of $(1, 0)$ on $S^1$ pulls back to a *disconnected* subset of $[0, 2\pi)$ (the union of $[0, \delta)$ and $(2\pi - \delta, 2\pi)$), which is not a neighbourhood of $0$ in $[0, 2\pi)$ in the connected sense. See [[Ex - A continuous bijection that is not a homeomorphism]]. This is the canonical counterexample, and the reason "continuous bijection ⟹ homeomorphism" is **illegal but tempting**.

**Is NOT an instance — $\mathbb{R}_\text{std} \cong \mathbb{R}_\text{discrete}$.** Even though the underlying sets are the same, the two topological spaces are not homeomorphic: $\mathbb{R}_\text{std}$ is connected (the only clopen sets are $\emptyset$ and $\mathbb{R}$), while $\mathbb{R}_\text{discrete}$ is totally disconnected (every set is clopen). So connectedness, a topological invariant, distinguishes them.

**Corollary — compact-to-Hausdorff continuous bijections are homeomorphisms.** If $X$ is compact, $Y$ is Hausdorff, and $f : X \to Y$ is a continuous bijection, then $f$ is a homeomorphism. *Proof outline:* a closed subset of a compact space is compact; continuous images of compact sets are compact; compact subsets of Hausdorff spaces are closed. So $f$ takes closed sets to closed sets, i.e., $f^{-1}$ takes open sets to open sets (its preimages are images of $f$), so $f^{-1}$ is continuous. Proved in [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

**Corollary — homeomorphism is an equivalence relation.** Reflexive: $\text{id}_X$. Symmetric: if $f$ is a homeomorphism, so is $f^{-1}$. Transitive: composition of homeomorphisms is a homeomorphism, because composition of continuous bijections is a continuous bijection, and $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ is also a composition of continuous functions.

**Corollary — homeomorphism preserves every topological property.** Connectedness, compactness, Hausdorffness, first/second countability, separability, the number of connected components, the fundamental group, homology, cohomology, the dimension — all are homeomorphism invariants. *Method to prove $X \not\cong Y$:* find a topological invariant that takes different values on $X$ and $Y$.

**Calibration check.** Construct an explicit homeomorphism from $(0, 1)$ to $\mathbb{R}$ using $\tan$ and an affine map. Explain why the winding map $[0, 2\pi) \to S^1$ is a continuous bijection but not a homeomorphism. Explain how to prove $\mathbb{R} \not\cong S^1$ using the cut-point criterion (every $\mathbb{R}$ point is a cut point; no $S^1$ point is a cut point, since $S^1 \setminus \{p\}$ is connected for any $p$). If you can also explain why the floor function is *not* a homeomorphism between any two reasonable topologies on $\mathbb{R}$ (it is not a bijection — many points map to each integer), you have understood every clause of the definition.

---

# Unlocked by This

> [!tip] **Topological Invariants** *(from this topic)*
> Properties that distinguish homeomorphism classes: connectedness (Topology II), compactness (Topology II), the fundamental group $\pi_1(X)$ (Topology III), higher homotopy groups, homology and cohomology. Each invariant is a tool for proving spaces non-homeomorphic.

> [!tip] **Compact-to-Hausdorff Theorem** *(from this topic)*
> A continuous bijection from a compact space to a Hausdorff space is automatically a homeomorphism. This is the standard route for verifying homeomorphisms without separately checking inverse continuity. See [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

> [!tip] **Invariance of Domain** *(from Algebraic Topology)*
> **Brouwer's invariance of domain** asserts that $\mathbb{R}^n \not\cong \mathbb{R}^m$ for $n \neq m$. More generally, an injective continuous map from an open subset of $\mathbb{R}^n$ into $\mathbb{R}^n$ is itself an open map, hence a homeomorphism onto its image. This is the deep reason dimension is a topological invariant.

> [!tip] **Homotopy Equivalence** *(from Algebraic Topology)*
> A weaker notion of equivalence: $X \simeq Y$ if there are continuous $f, g$ with $g \circ f \simeq \text{id}_X$ and $f \circ g \simeq \text{id}_Y$. Homotopy equivalence preserves homotopy invariants (the fundamental group, homology, cohomology) but is strictly weaker than homeomorphism. $\mathbb{R}^n$ is homotopy equivalent to a point but not homeomorphic to it.

> [!tip] **Diffeomorphism** *(from Differential Geometry)*
> A homeomorphism between smooth manifolds that is smooth in both directions. Strictly stronger than homeomorphism: in dimension 4 there are exotic smooth structures on $\mathbb{R}^4$ that are homeomorphic but not diffeomorphic to the standard $\mathbb{R}^4$.

> [!tip] **Open Mapping Theorem** *(from Functional Analysis)*
> A bounded linear bijection between Banach spaces is automatically a homeomorphism — its inverse is automatically bounded. This is the Banach-space analogue of "compact ⟹ Hausdorff ⟹ homeomorphism".

> [!tip] **Classification of Surfaces** *(from Algebraic Topology)*
> The compact connected surfaces are classified up to homeomorphism by their *genus* (number of handles) and orientability. The sphere, torus, Klein bottle, double torus, etc., are all topologically distinct, and this exhausts the list. The classification is a high point of Topology III and IV.

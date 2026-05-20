---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Connected Space"
  - "Def - Path-Connected Space"
  - "Def - Connected Components"
tags: [analysis, topology, connectedness]
---

# Problem Statement

The **connected components** of a topological space $X$ are the equivalence classes under "$p \sim q$ if $p, q$ lie in a common connected subset of $X$". The **path-components** of $X$ are the equivalence classes under "$p \sim q$ if there is a continuous $\gamma : [0,1] \to X$ with $\gamma(0) = p, \gamma(1) = q$".

**(i)** Give an example of a space whose connected components and path-components differ. (The topologist's sine curve will do: it has one connected component but two path-components.)

**(ii)** Show that for a *locally path-connected* space $X$, every connected component is a path-component, so the two partitions coincide. A space $X$ is **locally path-connected** at a point $x$ if every neighbourhood of $x$ contains a path-connected neighbourhood of $x$; $X$ is locally path-connected if this holds at every point.

**Recall:**

![[Def - Connected Space#The Definition]]

![[Def - Path-Connected Space#The Definition]]

![[Def - Connected Components#The Definition]]

Path-connectedness implies connectedness: the image of $[0, 1]$ under a path is connected (by [[Thm - Continuous Image of a Connected Space]], since $[0, 1]$ is connected), and unions of paths sharing endpoints are connected by [[Thm - Union of Overlapping Connected Sets is Connected]]. Hence every path-component is contained in some connected component.

A subset $U \subseteq X$ is a **neighbourhood** of $x$ if there is an open $V$ with $x \in V \subseteq U$. (Conventions vary; here a neighbourhood is *not* required to be open.) A **path-connected neighbourhood** of $x$ is a neighbourhood of $x$ that is path-connected as a subspace.

---

# Convergent Strategy

**Problem class.** Part (i) is a *counterexample exhibition*: produce the standard example where path-components are coarser than connected components. Part (ii) is a *structural propagation* result: a local property (local path-connectedness) controls the global partition (components agree).

**Assumption pattern.** Part (i) reuses [[Ex - The topologist's sine curve]] — the closure of $\{(x, \sin(1/x)) : x > 0\}$ together with $\{0\} \times [-1, 1]$. We need: it has one connected component (it is connected — shown there) and two path-components (the graph piece $A$ and the segment piece $S$ — also shown there).

For (ii), the assumption is local path-connectedness; the target is "each path-component is open *and* closed in its connected component". An open-and-closed (clopen) subset of a connected space is the whole space, so each path-component would equal its containing component.

**Theorem routing.** Part (ii) routes through the "openness + closedness implies the whole thing" use of [[Def - Connected Space|connectedness]]. Show:
1. Each path-component is open in $X$ (under local path-connectedness).
2. Hence the complement of any path-component (a union of other path-components) is also open, so each path-component is closed too.
3. So each path-component is clopen.
4. Restricted to a connected component (which is itself a connected space in the subspace topology), the clopen path-component must be everything.

**Key decision point.** The non-obvious move is that local path-connectedness *promotes openness of path-components automatically*. A path-component contains, at each of its points, a path-connected neighbourhood — but a path-connected neighbourhood is *itself* contained in the path-component (because paths from the centre extend to all points of the neighbourhood). So the path-component is a union of open neighbourhoods of its own points, hence open.

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **Path-component $\subseteq$ connected component, always.** A path-component is connected (paths union along their common endpoints to give a connected union), so it sits inside the connected component of any of its points.

2. **Clopen subsets of connected spaces are trivial.** When restricted to a connected subspace, any clopen subset is either empty or the whole subspace. This is the equivalent characterization of connectedness from [[Def - Connected Space|the definition]].

3. **Local-to-global propagation under local path-connectedness.** A property of every small neighbourhood (here: being path-connected) propagates to a property of larger sets when the local property is "coherent" along the path-component structure.

---

# Hints

> [!note]- Hint 1
> For (i): in [[Ex - The topologist's sine curve|the topologist's sine curve]] $X = A \cup S$, we proved $X$ is connected (one component) but there is no path from any point in $S$ to any point in $A$ (two path-components).

> [!note]- Hint 2
> For (ii): show that each path-component $P$ is *open* in $X$. Take any $p \in P$. By local path-connectedness, $p$ has a path-connected neighbourhood $N$. Argue $N \subseteq P$: any $q \in N$ is connected to $p$ by a path inside $N$, hence by a path inside $X$, hence is in the same path-component as $p$.

> [!note]- Hint 3
> Once each path-component is open: the complement of a single path-component $P$ is the union of all the *other* path-components, each also open, so $X \setminus P$ is open, hence $P$ is closed. So $P$ is clopen. Now intersect $P$ with the connected component $C$ containing it: $P \cap C$ is clopen in $C$, nonempty (it contains the point), so it equals $C$ by connectedness of $C$. Hence $P = C$.

---

# Solution

The path-component partition is always *finer* than the connected-component partition. The two coincide if and only if path-components are open, which is exactly the content of local path-connectedness.

**Step 1: Part (i) — the example.**

The [[Ex - The topologist's sine curve|topologist's sine curve]] $X = A \cup S$ with $A = \{(x, \sin(1/x)) : x > 0\}$ and $S = \{0\} \times [-1, 1]$ has:
- One connected component (because $X$ is connected — proved in that exercise).
- Two path-components: $A$ and $S$ (because no path goes between them — proved there; each piece is path-connected on its own, $A$ via the parametrisation $x \mapsto (x, \sin(1/x))$ and $S$ via straight-line interpolation in the vertical segment).

> [!note]- Derivation
> From [[Ex - The topologist's sine curve]] we have: $X$ is connected (one component) and there is no continuous path from any point of $S$ to any point of $A$. The graph $A$ is itself path-connected: for any two points $(x_1, \sin(1/x_1))$ and $(x_2, \sin(1/x_2))$ with $x_1, x_2 > 0$, the path $t \mapsto ((1-t)x_1 + t x_2, \sin(1/((1-t)x_1 + t x_2)))$ stays in $A$ (a continuous deformation of the $x$-coordinate, with the $y$ following). The segment $S = \{0\} \times [-1, 1]$ is path-connected by linear interpolation in the $y$-coordinate. So the two pieces $A$ and $S$ are the two path-components, and the connected components and path-components differ.

**Step 2: Part (ii) — set up.**

Let $X$ be locally path-connected. We show every path-component $P$ is open, and from there that every path-component is closed too, hence clopen, hence equal to its containing connected component.

> [!note]- Derivation
> Recall that path-connectedness implies connectedness: a path $\gamma : [0, 1] \to X$ has $\gamma([0, 1])$ connected (continuous image of the connected $[0, 1]$). So each path-component $P$, being a union of paths sharing endpoints, is itself connected (apply [[Thm - Union of Overlapping Connected Sets is Connected]]: any two paths from a base point have the base point in common, so their union is connected, and iterating shows the full path-component is connected). Therefore $P$ is contained in the connected component $C(p)$ of any $p \in P$.
>
> The remaining content of (ii) is to show $P = C(p)$, i.e., the path-component is not strictly smaller. This is where local path-connectedness enters.

**Step 3: Part (ii) — path-components are open.**

Each path-component $P$ is open in $X$. For any $p \in P$, local path-connectedness gives a path-connected neighbourhood $N$ of $p$, and $N \subseteq P$ because any $q \in N$ is connected to $p$ by a path inside $N$, hence is in the same path-component as $p$.

> [!note]- Derivation
> Take $p \in P$. Since $X$ is locally path-connected at $p$, there is a path-connected neighbourhood $N$ of $p$ — that is, there is an open $V$ with $p \in V \subseteq N$ and $N$ is path-connected. For any $q \in N$, $N$ being path-connected gives a path $\gamma : [0, 1] \to N \subseteq X$ with $\gamma(0) = p, \gamma(1) = q$. So $q$ is in the same path-component as $p$, i.e., $q \in P$.
>
> Hence $N \subseteq P$, and in particular $V \subseteq P$. Since $V$ is open and contains $p$, $p$ is an interior point of $P$. This holds for every $p \in P$, so $P$ is open.

**Step 4: Part (ii) — path-components are closed.**

The complement $X \setminus P$ is the union of all *other* path-components, each open by Step 3, so $X \setminus P$ is open, hence $P$ is closed. So $P$ is clopen.

> [!note]- Derivation
> Path-components partition $X$ (the relation "connected by a path" is an equivalence relation — reflexive via constant paths, symmetric via path reversal $t \mapsto \gamma(1 - t)$, transitive via path concatenation). So $X \setminus P = \bigsqcup_{P' \neq P} P'$, a disjoint union of path-components other than $P$. By Step 3, each $P'$ is open in $X$. A union of open sets is open, so $X \setminus P$ is open, hence $P$ is closed. Combined with Step 3, $P$ is clopen.

**Step 5: Part (ii) — path-components equal components.**

Let $C$ be the connected component containing $P$. Then $P \cap C$ is clopen in $C$ (intersection of a clopen of $X$ with $C$), nonempty (it contains the basepoint of $P$), so by connectedness of $C$, $P \cap C = C$, hence $C \subseteq P$. Combined with $P \subseteq C$, $P = C$.

> [!note]- Derivation
> $C$ is connected as a subspace. $P$ is clopen in $X$, so $P \cap C$ is clopen in $C$ in the subspace topology (because clopen subsets restrict to clopen subsets). $P \cap C$ is nonempty (contains any element of $P$, which is in $C$).
>
> By the [[Def - Connected Space|definition of connectedness]], the only clopen subsets of the connected $C$ are $\emptyset$ and $C$. Since $P \cap C \neq \emptyset$, we conclude $P \cap C = C$, hence $C \subseteq P$.
>
> We already had $P \subseteq C$ (path-component is connected, sits in its component). So $P = C$.
>
> This holds for every path-component $P$. So the partition into path-components agrees with the partition into connected components.

> [!note]- Complete formal solution
> **(i)** The topologist's sine curve $X = \{(x, \sin(1/x)) : x > 0\} \cup \{0\} \times [-1, 1]$ is connected (one component) but has two path-components $A$ and $S$ (no continuous path connects them), as shown in [[Ex - The topologist's sine curve]].
>
> **(ii)** Let $X$ be locally path-connected and let $P$ be a path-component.
>
> *P is open.* For $p \in P$, local path-connectedness gives an open path-connected neighbourhood $V$ of $p$. For any $q \in V$, a path in $V$ connects $p, q$, so $q \in P$. Thus $V \subseteq P$ and $P$ is open.
>
> *P is closed.* $X \setminus P$ is the union of the other path-components, each open by the same argument, so $X \setminus P$ is open and $P$ is closed.
>
> *P equals its connected component.* The component $C$ containing $P$ is connected, and $P \cap C = P$ (since $P \subseteq C$) is clopen in $C$ and nonempty. By [[Def - Connected Space|connectedness]] of $C$, $P = C$. $\blacksquare$

---

# Key Takeaways

**The path-component partition refines the connected-component partition; equality holds precisely when path-components are open.** The general inclusion "path-component $\subseteq$ connected component" is automatic from path-connectedness implying connectedness. The reverse inclusion — that every connected component is a single path-component — fails in general (the topologist's sine curve) and is equivalent to path-components being open. Local path-connectedness is the cleanest sufficient condition for this openness. The pattern for similar local-to-global propagation arguments — *a local structural property forces a global partition to be coarse* — recurs throughout topology and geometry (e.g., a locally constant function on a connected space is constant; a manifold's connected components are the same as its path-components).

**The "clopen subset of a connected space is trivial" lever is the workhorse of every "local condition implies global identification" proof.** To show two partitions agree (or that some subset equals the whole space), the standard route is: show the subset is *open*, show its complement is *open* (often by symmetric reasoning), conclude both are open hence clopen, then invoke connectedness to force the subset to be empty or everything. This pattern shows up in: locally constant functions on connected spaces, the lifting criteria for covering spaces, the uniqueness of analytic continuation, the unique path lifting theorem, and the identity theorem for holomorphic functions. Whenever you can produce both "open" and "complement open", connectedness finishes the job.

**Local path-connectedness is the cheapest condition that forbids "topologist's-sine-curve" pathologies, and it holds for every manifold, every CW complex, every open subset of $\mathbb{R}^n$.** This explains why path-connectedness and connectedness are interchangeable in most of geometry and analysis: the spaces we naturally encounter are locally path-connected. The pathology only shows up in spaces that "spiral in" to a boundary set, lose local structure on a singular fibre, or are deliberately constructed counterexamples. The discipline of distinguishing path-components from components is essentially a discipline of identifying which spaces are *not* locally path-connected — and recognizing that for them, the two partitions can be genuinely different, hence one must be careful which is being used.

**The "path-components partition into open sets" argument is the prototype for every "an equivalence relation has open equivalence classes" proof.** When an equivalence relation has the property that *each class is locally controlled* — every point has a neighbourhood inside its own class — the classes are automatically open, and the partition is automatically a partition into clopen sets. This is what makes group orbits open in good situations (e.g., proper actions of compact Lie groups), what makes leaves of a foliation locally open, and what underlies the local triviality of fibre bundles. Recognize the trigger: any time you have a partition where local-around-each-point structure is uniform, expect the classes to be open and hence to be the connected components.

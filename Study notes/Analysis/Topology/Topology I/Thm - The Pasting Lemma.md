---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Subspace Topology"
  - "Def - Closure, Interior, and Boundary"
tags: [analysis, topology]
---

# Notation

$X, Y$ are topological spaces. $A, B \subseteq X$ are subsets with $X = A \cup B$, each equipped with the subspace topology — see [[Def - Subspace Topology]]. $f : A \to Y$ and $g : B \to Y$ are continuous functions. The notation $f|_{A \cap B}$ is the restriction of $f$ to the overlap $A \cap B$. The **glued function** $h : X \to Y$ is defined by $h(x) = f(x)$ for $x \in A$ and $h(x) = g(x)$ for $x \in B$; this is well-defined precisely when $f|_{A \cap B} = g|_{A \cap B}$. The full notation registry is on [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Motivation

Piecewise-defined functions appear everywhere in analysis and topology. We often describe a map $X \to Y$ by saying "do one thing on part of $X$, another on the rest". The natural question is: when does the resulting glued function inherit continuity from its pieces? Setting things up carefully — agreement on the overlap, and a suitable hypothesis on how the pieces sit in $X$ — gives a clean answer: yes, the function is continuous, provided the pieces are *closed* (or both *open*, by symmetry).

The closedness hypothesis is essential: pasting fails for arbitrary subsets. The standard cautionary example pastes the constant function $f = 0$ on $\{0\}$ and $g = 1/x$ on $(0, 1]$; both are continuous on their domains, the overlap $\{0\} \cap (0, 1]$ is empty (so the agreement condition is vacuous), but the glued function $h$ jumps at $0$ — it is not continuous. Here the issue is that $\{0\}$ is closed and $(0, 1]$ is not. With a closed/closed cover or open/open cover, the failure cannot occur, and the lemma asserts the pasting succeeds.

The lemma is the structural workhorse for constructing piecewise-continuous functions. It is what justifies the standard moves: defining a path in a topological space by concatenating two paths (the basis of homotopy theory), extending a continuous function from a closed subspace, gluing two functions agreeing on an overlap to produce a continuous map on a union. Every "define $h$ by cases" construction in topology either uses the pasting lemma or is using a special-case implicit version of it.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition has three parts: (i) $X = A \cup B$ is a finite cover by closed sets (or by open sets); (ii) $f : A \to Y$ and $g : B \to Y$ are continuous; (iii) $f$ and $g$ agree on $A \cap B$.

The first natural source is **a path concatenation in a space.** Property $B$: two paths $\gamma_1 : [0, 1] \to X$ and $\gamma_2 : [0, 1] \to X$ with $\gamma_1(1) = \gamma_2(0)$. The bridge: parameterize the concatenation $\gamma_1 * \gamma_2 : [0, 1] \to X$ by sending $[0, 1/2] \to X$ via $\gamma_1(2t)$ and $[1/2, 1] \to X$ via $\gamma_2(2t - 1)$, agreeing at $t = 1/2$. The cover $\{[0, 1/2], [1/2, 1]\}$ is closed/closed in $[0, 1]$. *Example:* this is the construction of the fundamental groupoid's composition law — see [[Topology I — §1–3 Metric and Topological Spaces|the fundamental group in Topology II–IV]].

The second source is **extending a function from a closed subspace.** Property $B$: $A \subseteq X$ closed and $f : A \to Y$ continuous; defining the extension by $g : X \setminus A^\circ \to Y$ on the complement. The bridge: if the union of the closures forms a closed cover and the agreement holds on overlaps, the extension is continuous. *Example:* extending a continuous map defined on a sphere to a ball, when the map is constant on the boundary — a standard step in the construction of homotopies.

The third source is **a piecewise-defined function on a discrete cover.** Property $B$: $X$ is the disjoint union of finitely many closed (clopen) pieces $A_1, \dots, A_n$, with continuous $f_i : A_i \to Y$. Since the overlaps are empty, the agreement condition is vacuous and the pasting lemma immediately gives continuity. *Example:* defining the characteristic function of a clopen set; defining a locally constant function on a disconnected space.

The fourth source is **gluing along a smooth boundary.** Property $B$: $X$ is a smooth manifold expressed as the union of two smooth manifolds-with-boundary $A, B$, both closed in $X$, with $A \cap B$ the common boundary on which two functions $f, g$ agree. *Example:* construction of a smooth function on $S^2 = D^2_+ \cup D^2_-$ from smooth functions on the upper and lower hemispheres agreeing on the equator — a model construction in differential topology.

**Targets (Output Amplification)**

The conclusion is "the glued function $h$ is continuous on $X$".

Combine with **the pasted function being a homeomorphism.** Property $D$: $h : X \to Y$ is bijective with continuous inverse (or both $X, Y$ compact Hausdorff so that continuous bijection implies homeomorphism). The amplified result $E$: $h$ is a homeomorphism, and any homeomorphism-invariant property of $X$ transfers to $Y$. The pasting lemma constructs the underlying continuous map; further hypotheses make it a homeomorphism.

Combine with **iteration to a finite cover.** Property $D$: a cover $X = A_1 \cup \dots \cup A_n$ by finitely many closed sets, with continuous $f_i : A_i \to Y$ agreeing on pairwise overlaps. The amplified result $E$: the glued function is continuous on $X$. This is proved by induction — pasting two at a time — and is the "finitely many pieces" version of the lemma. *Important:* the cover must be *finite*. The lemma fails for infinitely many closed pieces in general, because an infinite union of closed sets need not be closed (consider $X = \mathbb{R}$ as the union of singletons).

Combine with **algebraic / topological structure being preserved.** Property $D$: $Y$ has additional algebraic structure (group, vector space, ring), and each $f|_{A_i}$ is a homomorphism of that structure. The amplified result $E$: the glued $h$ is also a homomorphism, provided the structure-preservation conditions are checked on a generating set. *Example:* in the theory of group actions, gluing equivariant maps along closed pieces produces equivariant maps.

---

# Why Is It True

The cleanest reason runs through the closed-set version of continuity: a function is continuous if and only if the preimage of every closed set is closed (taking complements of the open-set definition — see [[Thm - Continuity via Open Sets (Metric Spaces)]]).

Suppose $V \subseteq Y$ is closed. The preimage $h^{-1}(V)$ decomposes as
$$h^{-1}(V) = (A \cap f^{-1}(V)) \cup (B \cap g^{-1}(V)).$$
Each piece is closed *in its respective subspace*: $f^{-1}(V)$ is closed in $A$ because $f$ is continuous on $A$, and similarly $g^{-1}(V)$ is closed in $B$.

Now use the closed/closed hypothesis: $A$ is closed in $X$, so a closed subset of $A$ (in the subspace topology) is also closed in $X$ — this is the special case of [[Thm - Closure-in-Subspace Formula]] where the subspace is itself closed, in which case "closed in $Y$" and "closed in $X$" coincide for subsets of $Y$. So $f^{-1}(V)$ (a closed subset of the closed-in-$X$ set $A$) is closed in $X$. Similarly $g^{-1}(V)$ is closed in $X$.

The preimage $h^{-1}(V)$ is therefore a *finite union* of closed sets in $X$, hence closed in $X$ (by the topology axioms — finite unions of closed sets are closed, dual to finite intersections of opens being open). So $h$ is continuous by the closed-set criterion.

The same argument runs identically in the open/open case, with "open" everywhere in place of "closed": the cover $\{A, B\}$ is open, so an open-in-$A$ set is open in $X$ (here using the fact that for open subspaces, "open in subspace" equals "open in ambient" for subsets of the subspace), and $h^{-1}(U) = (A \cap f^{-1}(U)) \cup (B \cap g^{-1}(U))$ is a finite union of opens, hence open.

Why does the lemma fail without the closed (or open) hypothesis? Because a closed subset of $A$ is not in general closed in $X$ unless $A$ is closed in $X$. The pasting argument requires "closed-in-piece propagates to closed-in-ambient", which is exactly the closed-subspace fact. Without it, the preimage $h^{-1}(V)$ is a union of two sets each closed *in its piece* but not necessarily closed in $X$ — and the union is not closed in $X$, so $h$ is not continuous.

The cautionary example pastes $\{0\}$ (closed) and $(0, 1]$ (*not* closed in $[0, 1]$) — the second piece is not closed, so closed-in-piece does not propagate to closed-in-$X$ for it. The constant $0$ on $\{0\}$ pasted with $1/x$ on $(0, 1]$ produces a function with a jump at $0$, which the pasting lemma's failure registers.

---

# What Makes This Hard

The non-obvious step is recognizing that the closedness of $A$ and $B$ in $X$ — *not* just continuity of the pieces — is what propagates "closed-in-piece" to "closed-in-$X$" for the preimage. The most common error is to omit this hypothesis (or to assume the lemma works for arbitrary covers), which produces the cautionary example: pasting a constant onto $1/x$ across a half-open boundary. A second slip is to try to paste *infinitely* many closed pieces — the lemma extends to finite covers but not to infinite ones in general, since infinite unions of closed sets need not be closed.

---

# Rederivation Scaffold

**High-level strategy:**
Use the closed-set criterion for continuity. Decompose the preimage of a closed set as a union of two pieces, each closed in its subspace; closedness of the subspaces in $X$ promotes "closed-in-subspace" to "closed-in-$X$", and the finite union of closed sets is closed.

**Subgoal decomposition:**

1. **Verify well-definedness of $h$.**
   - *Hint:* On the overlap $A \cap B$, both $f$ and $g$ are defined; the agreement hypothesis $f|_{A \cap B} = g|_{A \cap B}$ ensures the two assignments do not conflict.
   - *Why needed:* Establishes $h$ is a function.

2. **Compute the preimage of a closed set $V \subseteq Y$ under $h$.**
   - *Hint:* $h^{-1}(V) = (A \cap f^{-1}(V)) \cup (B \cap g^{-1}(V))$, because a point in $A$ goes to $V$ via $h$ iff it goes via $f$, similarly for $B$.
   - *Why needed:* Decomposes the preimage into pieces controlled by the continuity of $f$ and $g$.

3. **Show each piece is closed in $X$.**
   - *Hint:* $f^{-1}(V)$ is closed in $A$ (continuity of $f$, with $V$ closed in $Y$); since $A$ is closed in $X$, a closed subset of $A$ in the subspace topology is closed in $X$. Same for $g^{-1}(V) \subseteq B$.
   - *Why needed:* Promotes "closed in piece" to "closed in $X$", which requires the closed-cover hypothesis.

4. **Conclude $h^{-1}(V)$ is closed in $X$.**
   - *Hint:* Finite union of closed sets is closed (axiom of topology, dual to finite intersection of opens being open).
   - *Why needed:* Closed-set criterion for continuity gives $h$ continuous.

5. **Run the open/open version.**
   - *Hint:* Identical argument with "open" everywhere. Open subspaces have the property "open in subspace = open in ambient" for subsets of the subspace.
   - *Why needed:* Completes the lemma's two formulations.

---

# Lemma Decomposition

> [!note]- Lemma 1: Closed-in-closed-subspace promotes to closed-in-ambient
> **Statement:** If $A \subseteq X$ is closed in $X$ and $C \subseteq A$ is closed in the subspace topology on $A$, then $C$ is closed in $X$.
>
> **Hint:** $C = F \cap A$ for some closed $F$ in $X$ (by the characterization of closed subsets of a subspace); intersection of closed sets in $X$ is closed in $X$.
>
> **Why needed:** Promotes "closed in piece" to "closed in $X$", which is the closed cover's contribution.
>
> > [!note]- Full proof
> > By the closed-set characterization of the subspace topology (see [[Def - Subspace Topology]]), $C \subseteq A$ is closed in $A$ iff $C = F \cap A$ for some closed $F \subseteq X$. Since $A$ is also closed in $X$, $C = F \cap A$ is the intersection of two closed sets in $X$, hence closed in $X$ (the family of closeds is closed under finite intersections, by the topology axioms).

> [!note]- Lemma 2: Open-in-open-subspace promotes to open-in-ambient
> **Statement:** If $A \subseteq X$ is open in $X$ and $V \subseteq A$ is open in the subspace topology on $A$, then $V$ is open in $X$.
>
> **Hint:** $V = U \cap A$ for some open $U$ in $X$; intersection of open sets in $X$ is open in $X$.
>
> **Why needed:** Dual to Lemma 1, for the open-cover version of the pasting lemma.
>
> > [!note]- Full proof
> > $V \subseteq A$ is open in $A$ iff $V = U \cap A$ for some open $U$ in $X$ (by definition of subspace topology). $A$ open in $X$ plus $U$ open in $X$ gives $V = U \cap A$ open in $X$ (finite intersection of opens).

> [!note]- Lemma 3: Finite union of closed sets is closed
> **Statement:** In any topological space $X$, a finite union of closed sets is closed.
>
> **Hint:** Take complements: a finite intersection of open sets is open by the topology axioms.
>
> **Why needed:** Final step that assembles the preimage into a closed set.
>
> > [!note]- Full proof
> > Let $C_1, \dots, C_n$ be closed in $X$, so each $X \setminus C_i$ is open. $X \setminus (C_1 \cup \dots \cup C_n) = (X \setminus C_1) \cap \dots \cap (X \setminus C_n)$, a finite intersection of opens, hence open by the topology axioms. Therefore $C_1 \cup \dots \cup C_n$ is closed.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X = A \cup B$ with $A, B$ closed in $X$, $f : A \to Y$ and $g : B \to Y$ continuous, and $f|_{A \cap B} = g|_{A \cap B}$. Define $h : X \to Y$ by $h(x) = f(x)$ for $x \in A$ and $h(x) = g(x)$ for $x \in B$; the agreement condition makes this well-defined.
>
> **Continuity of $h$ via closed-set criterion.** Let $V \subseteq Y$ be closed in $Y$. Then
> $$h^{-1}(V) = \{x \in X : h(x) \in V\} = \{x \in A : f(x) \in V\} \cup \{x \in B : g(x) \in V\} = f^{-1}(V) \cup g^{-1}(V).$$
> (Here we use the cover $X = A \cup B$: every $x \in X$ is in $A$ or $B$, and the two pieces cover the preimage.)
>
> By continuity of $f$, $f^{-1}(V)$ is closed in the subspace topology on $A$. By Lemma 1, $f^{-1}(V)$ is closed in $X$. Symmetrically, $g^{-1}(V)$ is closed in $X$.
>
> By Lemma 3, $f^{-1}(V) \cup g^{-1}(V)$ is closed in $X$. So $h^{-1}(V)$ is closed in $X$, and by the closed-set criterion for continuity, $h$ is continuous.
>
> **Open-cover version.** Suppose instead $A, B$ are open in $X$. The same argument runs with "open" everywhere: for any open $U \subseteq Y$,
> $$h^{-1}(U) = f^{-1}(U) \cup g^{-1}(U),$$
> each piece is open in the corresponding subspace, Lemma 2 promotes each to open in $X$, and a finite union of opens is open (by the topology axioms, dual to Lemma 3). So $h$ is continuous. $\blacksquare$
>
> **Finite-cover extension.** By induction on $n$, the lemma extends to a finite cover $X = A_1 \cup \dots \cup A_n$ by closed (or by open) sets, with continuous $f_i : A_i \to Y$ agreeing on pairwise intersections. *Proof:* paste $A_1, A_2$ to get a continuous function on $A_1 \cup A_2$ (closed, by Lemma 3); then paste this with $A_3$; iterate.
>
> **Counterexample without the hypothesis.** Take $X = [0, 1]$, $A = \{0\}$ (closed), $B = (0, 1]$ (*not* closed in $[0, 1]$). Define $f(0) = 0$ and $g(x) = 1/x$ on $(0, 1]$. Both are continuous on their pieces; the overlap is empty so the agreement is vacuous. The glued function $h$ has $h(0) = 0$ and $h(x) = 1/x$ for $x > 0$. This is not continuous at $0$: the preimage of the open set $(-1, 1) \subseteq \mathbb{R}$ is $\{0\}$, which is not open in $[0, 1]$. Equivalently, the preimage of the closed set $[1, \infty)$ is $(0, 1]$, which is not closed in $[0, 1]$. The lemma's hypothesis "$B$ closed in $X$" fails — and the lemma's conclusion fails with it.

---

# Cross-Field Exercise Suggestions

**Path concatenation in homotopy theory.** Two paths $\gamma, \delta : [0, 1] \to X$ with $\gamma(1) = \delta(0)$ concatenate to a path $\gamma * \delta : [0, 1] \to X$ defined by $\gamma(2t)$ for $t \in [0, 1/2]$ and $\delta(2t - 1)$ for $t \in [1/2, 1]$. The closed cover $\{[0, 1/2], [1/2, 1]\}$ of $[0, 1]$, with the agreement at $t = 1/2$ given by $\gamma(1) = \delta(0)$, satisfies the pasting lemma's hypotheses, so $\gamma * \delta$ is continuous. This is the construction of the fundamental groupoid's product, and the pasting lemma is silently used every time.

**Defining a homeomorphism by pasting.** Construct an explicit homeomorphism $[0, 1] \cup [1, 2] \to [0, 2]$ (where the union on the left is in $\mathbb{R}$) by the identity map. The two pieces $[0, 1]$ and $[1, 2]$ are closed in $\mathbb{R}$ hence in $[0, 1] \cup [1, 2] = [0, 2]$, the identity functions on each are continuous, and they agree at $1$. So the pasting lemma gives a continuous bijection; its inverse is again the identity, continuous by the same argument. Pasting is used to *construct* the homeomorphism.

**Equivariant gluing in group actions.** Let $G$ act on $X$, $Y$, and suppose $A, B \subseteq X$ are closed $G$-invariant subsets with $X = A \cup B$. If $f : A \to Y$ and $g : B \to Y$ are continuous, $G$-equivariant, and agree on $A \cap B$, the glued function $h : X \to Y$ is continuous and $G$-equivariant. Pasting at the level of continuous maps; equivariance is a pointwise condition preserved by the gluing.

**Smooth functions on a manifold via partitions of unity.** A smooth partition of unity argument constructs global smooth functions on a manifold by gluing locally defined ones. The pasting is at the closed-cover level (the closed supports of the partition functions cover the manifold), and continuity is built in by the smooth-cutoff construction. This is the workhorse for global constructions in differential topology.

---

# Bridges

- **[[Def - Continuous Map]]** — the lemma asserts the glued function is in this class. The closed-set form of continuity is what makes the proof short.

- **[[Thm - Continuity via Open Sets (Metric Spaces)]]** — the metric special case, where the open-set / closed-set duality is most familiar. Pasting works in metric spaces too; the proof is just the same.

- **[[Def - Subspace Topology]]** — the pieces $A, B$ carry the subspace topology, in which the continuity of $f$ and $g$ is stated. The promotion "closed-in-piece $\Rightarrow$ closed-in-ambient" uses the subspace structure (Lemma 1).

- **[[Thm - Closure-in-Subspace Formula]]** — the special case where the subspace is closed gives $\overline{C}^A = \overline{C}^X$, the basis for Lemma 1.

- **[[Def - Closure, Interior, and Boundary]]** — closed sets are the dual of open sets, and the closed-set criterion for continuity is the dual of the open-set one.

---

# Unlocked by This

> [!tip] Concatenation of Paths and the Fundamental Group *(from Topology IV)*
> The pasting lemma is what makes path concatenation continuous, and continuous concatenation is the operation underlying the **fundamental group** $\pi_1(X, x_0)$ of a topological space. Without pasting, one cannot even define multiplication of homotopy classes of loops — the entire algebraic topology edifice starts here.

> [!tip] Smooth Bump Functions and Partitions of Unity *(from Differential Topology)*
> The construction of smooth global functions from local ones, on a manifold, uses pasting at the level of continuous maps (gluing along closed supports of bump functions). **Partitions of unity** convert local information to global by exactly this pasting, and the partition functions are designed so the closed-cover hypothesis is automatic. This is the engine of all global differential topology.

> [!tip] CW Complexes *(from Algebraic Topology)*
> A **CW complex** is a space built up by gluing cells of increasing dimension along their boundaries. Each gluing step is a pasting along closed pieces, so the resulting topology is constructed cell by cell using the pasting lemma. CW complexes are the topological model for "manifolds built combinatorially", and the pasting lemma is what makes their continuous structure well-defined.

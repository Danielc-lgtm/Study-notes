---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Hausdorff Space"
  - "Def - Product Topology"
tags: [analysis, topology]
---

# Problem Statement

Let $X$ be a topological space and let $\Delta = \{(x, x) : x \in X\} \subseteq X \times X$ denote the **diagonal** of $X$, regarded as a subset of $X \times X$ with the [[Def - Product Topology|product topology]]. Show that the following are equivalent:

1. $X$ is **Hausdorff**.
2. $\Delta$ is closed in $X \times X$.

**Recall:**

A space $X$ is **Hausdorff** if for every pair of distinct points $x, y \in X$ there exist disjoint open sets $U, V \subseteq X$ with $x \in U$ and $y \in V$. A subset $C \subseteq Y$ is **closed** if its complement $Y \setminus C$ is open — equivalently, if for every point $p \notin C$ there is an open neighborhood of $p$ contained in $Y \setminus C$.

The [[Def - Product Topology|product topology]] on $X \times X$ has as basis the open rectangles $U \times V$ with $U, V \subseteq X$ open. A point $(x, y) \in X \times X$ has the open rectangles around it as a neighborhood basis. The diagonal $\Delta$ is the image of the *diagonal embedding* $\delta : X \to X \times X$, $x \mapsto (x, x)$.

![[Def - Hausdorff Space#The Definition]]

---

# Convergent Strategy

**Problem class.** This is an "if and only if" reformulation — recast a logical separation property (existence of disjoint opens) as a topological property of a specific subset (closedness of the diagonal). Both directions deploy the *defining* feature of the product topology: open neighborhoods of $(x, y) \in X \times X$ are exactly the open rectangles $U \times V$.

**Assumption pattern.** A point $(x, y)$ lies in $\Delta$ if and only if $x = y$; so a point $(x, y)$ lies in the complement $X \times X \setminus \Delta$ if and only if $x \neq y$. The complement is open if and only if every such "distinct-coordinate" point has an open neighborhood missing $\Delta$. An open rectangle $U \times V$ around $(x, y)$ misses $\Delta$ if and only if no point of the form $(z, z)$ lies in $U \times V$ — which is precisely $U \cap V = \emptyset$.

**Theorem routing.** The two directions are mirror images:
- *(Hausdorff $\Rightarrow$ $\Delta$ closed)*: given $(x, y) \notin \Delta$, i.e. $x \neq y$, Hausdorff produces disjoint opens $U \ni x$, $V \ni y$; the rectangle $U \times V$ is an open neighborhood of $(x, y)$ disjoint from $\Delta$.
- *($\Delta$ closed $\Rightarrow$ Hausdorff)*: given distinct $x, y$, the point $(x, y)$ is in the open complement of $\Delta$, hence sits in some open rectangle $U \times V \subseteq X \times X \setminus \Delta$; this $U \times V$ disjoint from $\Delta$ forces $U \cap V = \emptyset$.

**Key decision point.** The whole proof hinges on the *exact translation* "$U \times V$ misses $\Delta$ if and only if $U \cap V = \emptyset$." Once this is internalized, both directions are nearly automatic. The translation is what converts the *logical* statement of Hausdorffness into a *topological* one.

---

# Legal Operations Used

This solution uses the following operations from [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact#Legal Operations|the topic page]]:

1. **Recognize a point set as a level set or graph and use its complement.** The diagonal is the graph of $\operatorname{id}_X$; closedness of a graph is the natural product-space restatement of separation.

2. **Switch between "every point has a neighborhood" and "complement is open".** A set is closed iff its complement is open iff every point of the complement has an open neighborhood inside the complement.

3. **Use the basis of open rectangles in $X \times X$.** Every open set in a product topology is a union of basic open rectangles, so any open neighborhood of $(x, y)$ contains a rectangle $U \times V$ with $(x, y) \in U \times V$.

---

# Hints

> [!note]- Hint 1
> The defining translation: $U \times V \subseteq X \times X$ contains no point of $\Delta$ if and only if there is no $z$ with $(z, z) \in U \times V$, that is, if and only if $U \cap V = \emptyset$.

> [!note]- Hint 2
> *Forward* (Hausdorff ⇒ Δ closed): for $(x, y) \notin \Delta$ (i.e. $x \neq y$), Hausdorffness gives disjoint $U \ni x$, $V \ni y$. The rectangle $U \times V$ is an open neighborhood of $(x, y)$ in $X \times X \setminus \Delta$.

> [!note]- Hint 3
> *Reverse* (Δ closed ⇒ Hausdorff): distinct $x, y$ give $(x, y) \in X \times X \setminus \Delta$, an open set; it contains an open rectangle $U \times V \ni (x, y)$ with $U \times V \cap \Delta = \emptyset$, so $U \cap V = \emptyset$.

---

# Solution

The equivalence is a translation between two formulations of "$x \neq y$": that they admit disjoint open neighborhoods (Hausdorff), and that the point $(x, y) \in X \times X$ is *bounded away from* the diagonal (closedness of $\Delta$). The translation runs through one set-theoretic identity.

**Step 1: The basic translation between disjoint opens in $X$ and open rectangles missing $\Delta$.**

An open rectangle $U \times V \subseteq X \times X$ is disjoint from $\Delta$ if and only if $U \cap V = \emptyset$.

> [!note]- Derivation
> $(U \times V) \cap \Delta = \{(z, z) : z \in U \cap V\}$. This set is empty if and only if no $z$ lies in both $U$ and $V$, i.e. $U \cap V = \emptyset$. The whole proof rests on this single identity. The picture: $\Delta$ is the "line" through the origin of $X \times X$; an open rectangle $U \times V$ touches $\Delta$ precisely when the two factor-opens overlap in $X$.

**Step 2: Hausdorff ⇒ $\Delta$ closed.**

Assume $X$ is Hausdorff. For any $(x, y) \notin \Delta$, find an open neighborhood of $(x, y)$ in $X \times X \setminus \Delta$ — this shows the complement is open, so $\Delta$ is closed.

> [!note]- Derivation
> Take $(x, y) \notin \Delta$, meaning $x \neq y$. By **Hausdorffness**, there exist disjoint open $U, V \subseteq X$ with $x \in U$ and $y \in V$. The rectangle $U \times V$ is open in $X \times X$ (basic open set in the [[Def - Product Topology|product topology]]) and contains $(x, y)$. By Step 1, $U \cap V = \emptyset$ implies $(U \times V) \cap \Delta = \emptyset$, so $U \times V \subseteq X \times X \setminus \Delta$. Every point of the complement has an open neighborhood inside the complement, so the complement is open, so $\Delta$ is closed.

**Step 3: $\Delta$ closed ⇒ Hausdorff.**

Assume $\Delta$ is closed in $X \times X$. Given distinct $x, y \in X$, produce disjoint opens around them in $X$.

> [!note]- Derivation
> $X \times X \setminus \Delta$ is open. The point $(x, y)$ lies in this open set, since $x \neq y$. By the definition of the [[Def - Product Topology|product topology]], the open rectangles form a basis, so there exists a basic open neighborhood $U \times V$ of $(x, y)$ with $U \times V \subseteq X \times X \setminus \Delta$. From $U \times V \cap \Delta = \emptyset$ and Step 1, $U \cap V = \emptyset$. The opens $U \ni x$ and $V \ni y$ are disjoint. Since $x, y$ were arbitrary distinct points, $X$ is Hausdorff.

> [!note]- Complete formal solution
> The key identity: $(U \times V) \cap \Delta = \emptyset \iff U \cap V = \emptyset$.
>
> *($\Rightarrow$)* Let $X$ be Hausdorff. For $(x, y) \notin \Delta$, $x \neq y$, so there exist disjoint open $U \ni x$, $V \ni y$; then $U \times V$ is an open neighborhood of $(x, y)$ with $(U \times V) \cap \Delta = \emptyset$. So $X \times X \setminus \Delta$ is open, $\Delta$ is closed.
>
> *($\Leftarrow$)* Let $\Delta$ be closed. For distinct $x, y \in X$, $(x, y) \notin \Delta$ lies in the open complement, hence in some basic open rectangle $U \times V \subseteq X \times X \setminus \Delta$. The identity gives $U \cap V = \emptyset$, so the disjoint opens $U \ni x$, $V \ni y$ witness Hausdorffness. $\blacksquare$

---

# Key Takeaways

**The diagonal characterization is the cleanest reformulation of Hausdorffness and converts a quantifier-heavy condition into a single closedness claim.** "For all distinct $x, y$ there exist disjoint opens" is a $\forall\exists$ statement that involves searching over pairs of opens; "$\Delta$ is closed" is a single, point-free property of a specific subset of $X \times X$. The closedness form is what makes Hausdorffness *visible* in proofs — for instance, the result that the equalizer $\{x : f(x) = g(x)\}$ of two continuous maps to a Hausdorff space is closed comes directly from this characterization: $\{x : f(x) = g(x)\} = (f, g)^{-1}(\Delta)$, the preimage of the closed diagonal under the continuous map $(f, g) : X \to Y \times Y$. Several other "Hausdorff is needed" results — uniqueness of limits, closedness of compact subsets in Hausdorff spaces, the graph of a continuous map being closed when the target is Hausdorff — all flow from the closed-diagonal viewpoint.

**The set-theoretic identity $(U \times V) \cap \Delta = \emptyset \iff U \cap V = \emptyset$ is the entire technical content.** This is a recurring pattern in topology: a property of a *product space* gets translated into a property of the *factor space* by recognizing what the diagonal (or graph, or other distinguished subset) looks like in the product. The same technique works for proving that the graph of a continuous map $f : X \to Y$ is closed when $Y$ is Hausdorff — the graph is $\{(x, f(x))\}$, and its complement is open by an argument structurally identical to this one. Once internalized, "look at the diagonal in $X \times X$" becomes a standard move for converting separation statements to product statements.

**Trigger-reaction: "I need to show $\{x : f(x) = g(x)\}$ is closed" ⇒ "look at $(f, g)^{-1}(\Delta)$ where $\Delta \subseteq Y \times Y$".** As a corollary: any two continuous maps into a Hausdorff space that agree on a dense subset agree everywhere, because their equalizer is closed and dense, hence the whole space. This is one of the workhorse uniqueness results across analysis — the uniqueness of analytic continuation, the uniqueness of limits, the uniqueness of distributional extensions of continuous functions, the uniqueness of homomorphisms of Lie groups determined by their derivatives. Each is an instance of the closed-diagonal pattern. The mental move "Hausdorff target + agreement on a dense set ⇒ agreement everywhere" should be one of the first things tried whenever a uniqueness claim involving Hausdorff data appears.

**Hausdorffness is "the simplest nontrivial closed set you can ask for is the diagonal".** Many separation conditions can be phrased as closedness of certain subsets of $X^n$ for small $n$: $T_1$ is closedness of points (i.e. $\{x\}$ closed for every $x \in X$); Hausdorff is closedness of the diagonal in $X^2$. This pattern continues — for instance, "regularity in compact-Hausdorff" can be phrased via closedness of certain subsets of $X^2$, though it is rarely the cleanest viewpoint. The diagonal characterization sits at exactly the sweet spot where the product structure begins to do real work and the separation axiom becomes computable.

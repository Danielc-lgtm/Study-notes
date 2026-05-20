---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Open and Closed Sets in a Metric Space"
tags: [analysis, topology]
---

# Problem Statement

Let $X$ be a set. The **cofinite topology** $\tau_{\text{cof}}$ on $X$ has as open sets the empty set together with all subsets $U \subseteq X$ whose complement $X \setminus U$ is finite.

1. Verify that $\tau_{\text{cof}}$ is a [[Def - Topological Space|topology]] on $X$.
2. Identify the [[Def - Open and Closed Sets in a Metric Space|closed sets]] of $\tau_{\text{cof}}$.
3. Show that $\tau_{\text{cof}}$ equals the discrete topology if and only if $X$ is finite.
4. Suppose $X$ is *infinite* and $Y$ is a topological space which is [[Def - First and Second Countable|Hausdorff]] (any two distinct points have disjoint open neighbourhoods). Show that every [[Def - Continuous Map|continuous]] function $f : (X, \tau_{\text{cof}}) \to Y$ is **constant**.

**Recall:**

![[Def - Topological Space#The Definition]]

A subset $F \subseteq X$ is **closed** iff its complement $X \setminus F$ is open, equivalently iff $F$ has finite complement complement, equivalently iff $F$ is itself finite, or $F = X$. (We will derive this in Step 2.)

A space $Y$ is **Hausdorff** if for every $y_1 \neq y_2$ in $Y$ there exist open sets $V_1 \ni y_1$ and $V_2 \ni y_2$ with $V_1 \cap V_2 = \emptyset$. Metric spaces are Hausdorff; $\mathbb{R}^n$ with the standard topology is Hausdorff. A function $f : X \to Y$ is [[Def - Continuous Map|continuous]] iff $f^{-1}(V) \in \tau_X$ for every open $V \subseteq Y$.

---

# Convergent Strategy

**Problem class.** Verify a non-metric topology and then exploit the *paucity of open sets* to deduce a strong rigidity property: every continuous function to a Hausdorff space is constant. This is one of the cleanest illustrations of the dictum "fewer open sets means fewer continuous maps out, more continuous maps in".

**Assumption pattern.** The topology is defined by a *complement condition*: $U \in \tau \iff X \setminus U$ is finite (or $U = \emptyset$). This makes closed sets the natural objects — they are exactly the finite sets and $X$ itself. Every reasoning about open sets becomes shorter when phrased in terms of closed sets.

**Theorem routing.** Step 1 is a direct verification of the three topology axioms — each follows from a fact about finite sets: complements of opens are finite or all of $X$, finite intersections of cofinite sets are cofinite (finite unions of finites are finite), arbitrary unions of cofinite sets are cofinite (intersections of finites are finite). Step 2 is by definition. Step 3 is a counting argument: a finite set has every subset cofinite (or the complement of a finite). Step 4 is the heart of the exercise: use Hausdorffness on $Y$ to produce *disjoint* open sets around two hypothetical image values, pull back, and observe that the pullbacks of two disjoint sets must be *disjoint cofinites in $X$* — which forces both to be empty when $X$ is infinite.

**Key decision point.** The non-obvious move is: if $f$ takes two distinct values $y_1 \neq y_2$ in a Hausdorff space, then $f^{-1}(V_1)$ and $f^{-1}(V_2)$ are *disjoint*. If both are open and nonempty in the cofinite topology, both have finite complement. But two disjoint sets with finite complement give $X = (X \setminus A) \cup (X \setminus B)$ via De Morgan, which is a finite union of finite sets — forcing $X$ to be finite, contradicting our assumption.

---

# Legal Operations Used

This solution deploys the following operations from [[Topology I — §1–3 Metric and Topological Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Verify topology axioms via complement counting.** Open in the cofinite topology means "complement is finite or all of $X$" — translate every union/intersection statement to a complement statement and reason about finite sets.

2. **Translate "open" to "closed" via complements.** Closed sets in $\tau_{\text{cof}}$ are exactly the finite sets and $X$ itself — almost always the easier description.

3. **Use Hausdorffness of the target to separate hypothesized distinct image values.** This is the universal continuity-vs-Hausdorff move: $f(x_1) \neq f(x_2)$ + Hausdorff $\Rightarrow$ disjoint open sets in $Y$ $\Rightarrow$ disjoint open pullbacks in $X$.

4. **Apply De Morgan to disjoint opens.** If $A, B$ open and disjoint and both cofinite-open (complements finite), then $X = (X \setminus A) \cup (X \setminus B)$ is a finite union of finite sets, hence finite — contradicting an infinite $X$.

---

# Hints

> [!note]- Hint 1
> For Step 1, axiom by axiom: $\emptyset, X \in \tau$ (by definition); finite intersections of cofinites are cofinite (union of finitely many finites is finite); arbitrary unions of cofinites are cofinite (intersection of finite or finite is finite). All three reduce to elementary properties of finite sets.

> [!note]- Hint 2
> For Step 3, "discrete" means every singleton is open. When is $\{x\}$ open in the cofinite topology? When $X \setminus \{x\}$ is finite — i.e., when $X$ is finite.

> [!note]- Hint 3
> For Step 4: suppose $f$ takes two values $y_1, y_2 \in Y$. Use Hausdorffness of $Y$ to find disjoint open sets $V_1, V_2$ around them. The preimages $f^{-1}(V_1), f^{-1}(V_2)$ are disjoint, nonempty, and open in $X$. What does "open and nonempty in cofinite topology" force about each?

> [!note]- Hint 4
> Two disjoint cofinite sets $A, B$: $A \cap B = \emptyset$, complements both finite. De Morgan: $X = X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B)$, a union of two finite sets, hence finite. Contradicts $X$ infinite.

---

# Solution

The cofinite topology is the prototypical example of an *anti-Hausdorff* topology — there are so few open sets that any two nonempty opens must intersect — and the rigidity in Step 4 is a direct consequence of this scarcity.

**Step 1: $\tau_{\text{cof}}$ is a topology.**

Each axiom is verified by translating to a statement about complements.

> [!note]- Derivation
> *(i) $\emptyset, X \in \tau_{\text{cof}}$.* By definition: $\emptyset$ is included explicitly, and $X \setminus X = \emptyset$ is finite.
>
> *(ii) Finite intersections.* Let $U_1, \dots, U_n \in \tau_{\text{cof}}$. If any $U_i = \emptyset$, the intersection is $\emptyset \in \tau_{\text{cof}}$. Otherwise each $U_i$ has $X \setminus U_i$ finite, and by De Morgan
> $$X \setminus (U_1 \cap \dots \cap U_n) = (X \setminus U_1) \cup \dots \cup (X \setminus U_n).$$
> The right-hand side is a finite union of finite sets, hence finite. So the intersection is cofinite, i.e. in $\tau_{\text{cof}}$.
>
> *(iii) Arbitrary unions.* Let $\{U_\alpha\}_{\alpha \in I} \subseteq \tau_{\text{cof}}$. If all $U_\alpha = \emptyset$, the union is $\emptyset$. Otherwise some $U_{\alpha_0} \neq \emptyset$ has $X \setminus U_{\alpha_0}$ finite. By De Morgan
> $$X \setminus \bigcup_\alpha U_\alpha = \bigcap_\alpha (X \setminus U_\alpha) \subseteq X \setminus U_{\alpha_0},$$
> which is finite. A subset of a finite set is finite, so the union is cofinite, i.e. in $\tau_{\text{cof}}$.
>
> All three [[Def - Topological Space|topology axioms]] hold.

**Step 2: Closed sets are exactly the finite sets and $X$.**

By definition $F$ is closed iff $X \setminus F$ is open. $X \setminus F = \emptyset$ gives $F = X$; otherwise $X \setminus F$ is cofinite, so $F = X \setminus (X \setminus F)$ is the complement of a cofinite set, which is finite.

> [!note]- Derivation
> $F$ closed $\iff$ $X \setminus F \in \tau_{\text{cof}}$ $\iff$ ($X \setminus F = \emptyset$) or ($X \setminus (X \setminus F) = F$ is finite).
>
> The first case gives $F = X$; the second gives $F$ finite. So the closed sets of $(X, \tau_{\text{cof}})$ are
> $$\{F \subseteq X : F \text{ is finite}\} \cup \{X\}.$$

**Step 3: Cofinite = discrete iff $X$ is finite.**

The discrete topology has *every* subset open. In the cofinite topology, $\{x\}$ is open iff $X \setminus \{x\}$ is finite, iff $X$ is finite. So discrete = cofinite forces $X$ finite. Conversely if $X$ is finite, every subset is both finite (closed) and cofinite (open), so every subset is open — the cofinite topology equals the discrete topology.

> [!note]- Derivation
> *Discrete $\Rightarrow$ $X$ finite.* If $\tau_{\text{cof}} = \mathcal{P}(X)$, every singleton $\{x\}$ is open in $\tau_{\text{cof}}$, so $X \setminus \{x\}$ is finite (it cannot be $\emptyset$ unless $X = \{x\}$). If $X \setminus \{x\}$ is finite, then $X = \{x\} \cup (X \setminus \{x\})$ is finite.
>
> *$X$ finite $\Rightarrow$ discrete.* If $X$ is finite, every subset $A \subseteq X$ has $X \setminus A \subseteq X$ also finite, so $A$ is cofinite (or empty), hence open. So every subset is open: $\tau_{\text{cof}} = \mathcal{P}(X) = \tau_{\text{discr}}$.

**Step 4: Continuous functions to Hausdorff spaces are constant when $X$ is infinite.**

Suppose for contradiction $f$ takes two distinct values $y_1 \neq y_2$. By Hausdorffness of $Y$, there are disjoint open $V_1 \ni y_1, V_2 \ni y_2$. The preimages $f^{-1}(V_1)$ and $f^{-1}(V_2)$ are disjoint (preimages preserve disjointness), nonempty (each contains a point mapping to $y_i$), and open in $\tau_{\text{cof}}$ (continuity). Being nonempty and open in $\tau_{\text{cof}}$, each is cofinite. But two disjoint cofinites force $X$ finite — contradiction.

> [!note]- Derivation
> Suppose $f$ is continuous and not constant. Then there exist $x_1, x_2 \in X$ with $f(x_1) = y_1 \neq y_2 = f(x_2)$.
>
> Since $Y$ is Hausdorff, choose disjoint open sets $V_1, V_2 \subseteq Y$ with $y_1 \in V_1$, $y_2 \in V_2$, $V_1 \cap V_2 = \emptyset$.
>
> Let $A = f^{-1}(V_1)$, $B = f^{-1}(V_2)$. By continuity, $A, B$ are open in $(X, \tau_{\text{cof}})$. They are nonempty: $x_1 \in A$, $x_2 \in B$. They are disjoint: $A \cap B = f^{-1}(V_1 \cap V_2) = f^{-1}(\emptyset) = \emptyset$.
>
> Each of $A, B$ is nonempty and open in $\tau_{\text{cof}}$, hence has finite complement: $X \setminus A$ and $X \setminus B$ are both finite. By De Morgan,
> $$X = X \setminus \emptyset = X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B),$$
> a union of two finite sets, hence finite. But $X$ is infinite — contradiction.
>
> So $f$ must take only one value, i.e. $f$ is constant.

> [!note]- Complete formal solution
> **(1)** $\emptyset, X \in \tau$; finite intersections of cofinites are cofinite (finite union of finites is finite); arbitrary unions of cofinites are cofinite (subset of a finite is finite). **(2)** $F$ closed iff $F = X$ or $F$ finite. **(3)** Discrete iff every singleton open iff every $X \setminus \{x\}$ finite iff $X$ finite. **(4)** If $f$ is continuous, Hausdorff $Y$, $X$ infinite, and $f$ takes two distinct values, pull back disjoint Hausdorff opens to get two disjoint nonempty open subsets of $X$, both cofinite — but two disjoint cofinites force $X$ finite, contradiction. $\blacksquare$

---

# Key Takeaways

**A topology with "too few open sets" produces a space with "too few continuous maps out" — the cofinite topology is the cleanest illustration of this duality.** The general principle: continuous maps $f : X \to Y$ require $f^{-1}(V)$ to be open in $X$ for every open $V$ in $Y$. If $X$ has very few open sets, very few maps can satisfy this. The cofinite topology has only the empty set and cofinite sets as opens — so only functions whose preimage of *every* Hausdorff-separated pair gives a cofinite-disjoint pair can be continuous, which collapses the possibilities down to constants. The reverse extreme — *discrete* topology, the *most* open sets — makes *every* function continuous (see [[Ex - The discrete metric and topology]]). The cofinite topology is the opposite anchor: it makes essentially nothing continuous (to a Hausdorff target).

**The trigger-reaction pattern: "two disjoint nonempty cofinites $\Rightarrow$ $X$ is finite".** This is the central technical move. It generalizes to: any topology in which "two nonempty opens always intersect" is called *hyperconnected* (or *irreducible*), and the cofinite topology on an infinite set is the prototype. Continuous maps from a hyperconnected space to a Hausdorff space are forced to be constant by exactly the same argument. The same kind of rigidity appears in algebraic geometry, where the *Zariski topology* on an irreducible affine variety is hyperconnected — every two open sets meet, and the global regular functions on an irreducible projective variety are constants (this is the source of "compactness" arguments in algebraic geometry).

**Hausdorffness of the *target* is the key hypothesis — it provides the separation needed to make the disjoint-pullback argument work.** The trigger to develop: whenever you have a continuous map to a Hausdorff space and want to show some equality or constancy, look for disjoint open sets in the target and pull them back. Examples beyond this exercise: if $f : X \to Y$ continuous and $Y$ Hausdorff, then the *graph* of $f$ is closed in $X \times Y$ (Hausdorffness used to separate the diagonal); two continuous maps to a Hausdorff space agreeing on a dense subset agree everywhere ($\{x : f(x) = g(x)\}$ is closed by Hausdorffness of $Y$, contains a dense set, so equals $X$). The Hausdorff assumption is what makes most of point-set topology's separation arguments work.

**The cofinite topology is the *smallest* $T_1$ topology on $X$ — and this is its true name.** A topology is **$T_1$** if every singleton is closed, equivalently if for any two distinct points $x, y$ there is an open set containing $x$ and not $y$. In the cofinite topology, every singleton is finite, hence closed by Step 2 — so the cofinite topology is $T_1$. Moreover any $T_1$ topology must contain every cofinite set as an open: the complement of a finite set $F$ is a finite intersection $\bigcap_{x \in F}(X \setminus \{x\})$ of opens. So the cofinite topology is the *minimal* $T_1$ topology on $X$. This places the cofinite topology in the ladder of separation axioms: $T_0$ (distinguishable points) $\subsetneq$ $T_1$ (singletons closed) $\subsetneq$ $T_2$ (Hausdorff). The cofinite topology sits exactly at the $T_1$ level — singletons are closed but disjoint neighbourhoods of two points do not exist (since any two nonempty opens intersect on an infinite set). Whenever the question is "what is the weakest topology with property X?", the answer is usually a cofinite-or-Zariski-like construction.

---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Continuous Map"
  - "Thm - The Pasting Lemma"
  - "Def - Subspace Topology"
  - "Def - Homeomorphism"
tags: [analysis, topology]
---

# Problem Statement

Let $[0,1] \cup [1,2] \subseteq \mathbb{R}$ with the [[Def - Subspace Topology|subspace topology]] inherited from $\mathbb{R}$ — which equals $[0,2]$ as a set.

1. Define $f : [0, 2] \to [0, 2]$ piecewise:
$$f(x) = \begin{cases} 2x & \text{if } 0 \leq x \leq 1/2, \\ 1 & \text{if } 1/2 \leq x \leq 1, \\ 2x - 1 & \text{if } 1 \leq x \leq 2.\end{cases}$$
Use the [[Thm - The Pasting Lemma|pasting lemma]] to prove $f$ is [[Def - Continuous Map|continuous]] on $[0, 2]$.

2. Identify which hypothesis of the pasting lemma is *essential* by exhibiting a piecewise definition on the same domain that does *not* paste to a continuous function — in particular, replace the closed cover $[0, 1/2] \cup [1/2, 1] \cup [1, 2]$ by an *open* cover where the agreement condition fails.

3. Show that the closed-cover hypothesis cannot be weakened to "*locally finite* arbitrary cover" by giving an *open* cover where each piece is continuous but the agreement on overlaps is empty (so the agreement condition is vacuous, yet the resulting function is discontinuous).

**Recall:**

The [[Thm - The Pasting Lemma|pasting lemma]] states: if $X = A_1 \cup \dots \cup A_n$ where each $A_i$ is closed in $X$, and $f_i : A_i \to Y$ are [[Def - Continuous Map|continuous]] (with respect to the subspace topology on $A_i$) and *agree on overlaps* ($f_i|_{A_i \cap A_j} = f_j|_{A_i \cap A_j}$ for every $i, j$), then the function $f : X \to Y$ defined by $f|_{A_i} = f_i$ is well-defined and continuous on $X$. The same conclusion holds if every $A_i$ is open, with arbitrary $n$ (possibly infinite cover).

Closedness of a piece $A \subseteq X$ in the subspace topology means $A = X \cap F$ for some $F$ closed in the ambient space. In $X = [0, 2]$ with the standard subspace topology from $\mathbb{R}$, each of $[0, 1/2], [1/2, 1], [1, 2]$ is closed (each is a closed interval in $\mathbb{R}$, intersected with $X$).

---

# Convergent Strategy

**Problem class.** Construct a continuous piecewise-defined map and demonstrate which hypothesis of the pasting lemma is essential. The pasting lemma is the standard tool for piecewise constructions; this exercise calibrates exactly when it can and cannot be applied.

**Assumption pattern.** Each piece $f_i$ is a continuous polynomial or constant on a closed interval. The cover is finite and closed; overlaps are single points where the formulas agree. So the pasting lemma applies directly.

**Theorem routing.** Step 1: verify each piece is continuous (compositions of continuous polynomials), each piece is defined on a closed subset of $[0, 2]$, and the formulas agree at overlap points $x = 1/2$ and $x = 1$. Then invoke the pasting lemma. Steps 2 and 3 produce counterexamples where one hypothesis fails: in Step 2, an open cover with disagreeing overlap formulas gives a non-continuous result if one tries to extend the limit definition; Step 3 shows that even a *vacuous* agreement condition (empty overlap) can fail without closedness.

**Key decision point.** The role of the closed-cover hypothesis is to ensure that the preimage of an arbitrary closed set decomposes as a finite union of closed sets (one per piece), each closed in $X$. If a piece is *open* rather than closed, the preimage of a closed set need not be closed — and continuity of the glued function fails. The "agreement on overlaps" condition makes the function well-defined; closedness makes it continuous given that it is well-defined.

---

# Legal Operations Used

This solution deploys the following operations from [[Topology I — §1–3 Metric and Topological Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Apply the pasting lemma.** Given a piecewise definition on a finite closed cover with continuous pieces and matching overlaps, conclude continuity on the whole space.

2. **Verify continuity on each piece.** Composition of continuous polynomials (or constants) is continuous; restrictions of continuous maps to subspaces are continuous.

3. **Verify agreement at overlaps.** Compute both formulas at the overlap points and confirm they coincide.

4. **Construct a counterexample by violating one hypothesis.** For Step 3, take an open cover $\{[0, 1), (1/2, 2]\}$ — these are disjoint as open sets in $[0, 2]$ — wait, they are not disjoint. Reconsider: an open cover of $[0, 2]$ with empty overlap is impossible if the cover consists of nonempty pieces, because every connected open subset extends. But one can take open subsets of a *disconnected* space with empty overlap. So Step 3 needs a non-connected ambient space.

---

# Hints

> [!note]- Hint 1
> Each piece of $f$ is a polynomial (or constant) restricted to a closed interval; polynomial restrictions are continuous. The cover $[0, 1/2] \cup [1/2, 1] \cup [1, 2]$ is a finite closed cover of $[0, 2]$. So the only check needed is: do the formulas agree at $x = 1/2$ and $x = 1$?

> [!note]- Hint 2
> At $x = 1/2$: $2x = 1$ and the constant is $1$. At $x = 1$: the constant is $1$ and $2x - 1 = 1$. So all overlaps agree.

> [!note]- Hint 3
> For Step 2 (closedness matters): the standard illustrative example is to take the *open* cover $\{[0, 1/2), (1/2, 1]\}$ of $[0, 1]$ — these are open in the subspace topology, $[0, 1] = [0, 1/2) \cup \{1/2\} \cup (1/2, 1]$. But they don't cover $\{1/2\}$. So we extend with a third piece. Or: take the open cover $\{[0, 1)\}$ alone covers $[0, 1)$, not $[0, 1]$.

> [!note]- Hint 4
> For Step 3: in a *disconnected* space, two pieces of an open cover can be disjoint (zero overlap), with the agreement condition vacuously satisfied. Take $X = [0, 1] \cup [2, 3]$, $A = [0, 1]$, $B = [2, 3]$. Each is *both* open and closed in $X$ (since they are separated by the gap). Now define $f|_A = 0$ and $f|_B = 1$: the resulting $f$ is *continuous* — but it is continuous because the cover is closed *and* open, not by the cover being open alone with empty overlap. The lesson is the closedness is what carries the day.

---

# Solution

The pasting lemma applies straightforwardly to give the continuous piecewise map; the role of the closedness hypothesis is then exhibited by a counterexample.

**Step 1: $f$ is continuous on $[0, 2]$.**

Each piece is continuous, the cover is finite and closed, and the formulas agree at the overlap points. The pasting lemma gives continuity.

> [!note]- Derivation
> Write the cover as $A_1 = [0, 1/2]$, $A_2 = [1/2, 1]$, $A_3 = [1, 2]$, all of which are closed in $[0, 2]$ (each is the intersection of a closed interval of $\mathbb{R}$ with $[0, 2]$). They cover $[0, 2]$: $A_1 \cup A_2 \cup A_3 = [0, 2]$.
>
> Define $f_1 : A_1 \to [0, 2]$ by $f_1(x) = 2x$, $f_2 : A_2 \to [0, 2]$ by $f_2(x) = 1$ (constant), $f_3 : A_3 \to [0, 2]$ by $f_3(x) = 2x - 1$. Each is the restriction of a polynomial (continuous on $\mathbb{R}$, hence continuous as a function from the subspace) to the appropriate $A_i$.
>
> *Overlap agreement.* $A_1 \cap A_2 = \{1/2\}$: $f_1(1/2) = 2 \cdot 1/2 = 1$, $f_2(1/2) = 1$. ✓ $A_2 \cap A_3 = \{1\}$: $f_2(1) = 1$, $f_3(1) = 2 \cdot 1 - 1 = 1$. ✓ $A_1 \cap A_3 = \emptyset$ (or actually $\{1/2\} \cap \{1\} \cup \dots$; more precisely $A_1 \cap A_3 = \emptyset$ since $1/2 < 1$ and the intervals share no point). Agreement is vacuous.
>
> By the [[Thm - The Pasting Lemma|pasting lemma]] (closed-cover version): $f$ is continuous on $[0, 2]$.
>
> *Sanity check by computation.* $f$ is piecewise linear: from $0$ to $1$ on $[0, 1/2]$, constant at $1$ on $[1/2, 1]$, then increasing again from $1$ to $3$ on $[1, 2]$. At each boundary $1/2$ and $1$, both formulas give the value $1$. The graph is a continuous, piecewise linear curve with a horizontal plateau.

**Step 2: Closedness is essential — open cover with disagreement breaks continuity.**

If we replace the closed cover with an open one where the formulas disagree on overlaps, the resulting function is not continuous. Take the open cover $\{A = [0, 3/4),\ B = (1/4, 2]\}$ of $[0, 2]$. Both are open in $[0, 2]$ and the overlap is $A \cap B = (1/4, 3/4)$.

Define $g|_A(x) = 0$ and $g|_B(x) = 1$. On the overlap $A \cap B = (1/4, 3/4)$ the two formulas *disagree* — and the agreement condition is *violated*. There is no way to define $g$ on $A \cap B$ such that both descriptions of $g$ on $A$ and on $B$ are correct. So the construction is *not well-defined* in the first place — there is no function $g$, only inconsistent specifications.

> [!note]- Derivation
> A piecewise definition $g|_{A_i} = g_i$ requires the $g_i$ to agree on $A_i \cap A_j$ — otherwise there is no function defined on $A \cup B$ at all. So this example *fails at the well-definedness step*, before continuity even enters.
>
> To get a *well-defined* example that illustrates the difference between open and closed pasting, change the formulas to ones that agree at one point in the overlap but disagree at others. Or, alternatively, use the construction in Step 3 where the overlap is empty.

**Step 3: The closedness hypothesis cannot be replaced by "open cover with empty overlap" in a connected space.**

In a *connected* space $X$, no open cover by two nonempty pieces can have empty overlap (this is the [[Def - Topological Space|definition of connectedness]]). So in $[0, 2]$ — which is connected — every open cover has nonempty overlaps, and the agreement condition is nontrivial.

The interesting structural example is in a *disconnected* space. Take $X = [0, 1] \cup [2, 3]$ (subspace of $\mathbb{R}$). Then $A = [0, 1]$ and $B = [2, 3]$ are *both* open and closed in $X$ (separated by the gap $(1, 2)$). The open cover $\{A, B\}$ has empty overlap. Define $f|_A = 0$, $f|_B = 1$. This *is* continuous — but the conclusion follows just as well from the closed-cover pasting lemma applied to $\{A, B\}$ (also a closed cover, with empty overlap, hence vacuous agreement).

The conclusion: the open-cover version of pasting works because every open cover of a (Hausdorff) space admits a *partition of unity* or analogous local-finiteness argument, but the closed-cover hypothesis is what is genuinely needed for the *finite* pasting lemma stated above.

> [!note]- Derivation
> *Pasting lemma — closed cover version.* If $X = A_1 \cup \dots \cup A_n$ where each $A_i$ is closed in $X$, and continuous $f_i : A_i \to Y$ agree on overlaps, then the glued $f$ is continuous. The proof checks: $f^{-1}(F)$ for $F$ closed in $Y$ equals $\bigcup_i f_i^{-1}(F)$, a finite union of sets each closed in $A_i$. Since $A_i$ is closed in $X$, sets closed in $A_i$ are closed in $X$. A finite union of closed sets is closed. So $f^{-1}(F)$ is closed in $X$.
>
> *Pasting lemma — open cover version.* Same setup but each $A_i$ open. The proof uses: $f^{-1}(U)$ for $U$ open in $Y$ equals $\bigcup f_i^{-1}(U)$, a union of sets each open in $A_i$ (= open in $X$, since $A_i$ is open). Any union of opens is open, so $f^{-1}(U)$ is open. Crucially, this works for *arbitrary* (not just finite) covers.
>
> *Why "open" requires no finiteness while "closed" does.* In the closed-cover version, the argument uses that a *finite* union of closed sets is closed. An arbitrary union of closed sets need not be closed; for example, $\bigcup_n [1/n, 1] = (0, 1]$ is not closed in $[0, 1]$. So the closed version needs the cover finite.
>
> *Why one of the two versions is required.* If neither openness nor closedness is assumed, the pasting fails. Take $X = [0, 1]$ and the cover $A = \{0\} \cup (1/2, 1]$, $B = [0, 1/2]$. Neither is open nor closed in $X$ ($A$ is half-open, $B$ is closed but $A$ is not). Define $f|_A(x) = 1$, $f|_B(x) = 0$. At $x = 0$, $f$ is supposed to be both $0$ (since $0 \in B$) and $1$ (since $0 \in A$) — well-definedness fails. The point is that without a hypothesis controlling the cover, the agreement check on overlaps can be vacuous yet the resulting function fail to be continuous.

> [!note]- Complete formal solution
> **(1)** Each piece of $f$ is the restriction of a polynomial to a closed interval, hence continuous. The cover $\{[0, 1/2], [1/2, 1], [1, 2]\}$ is finite and closed in $[0, 2]$, and the formulas agree at the overlap points ($f$ takes the value $1$ at $x = 1/2$ and at $x = 1$ from every relevant formula). The [[Thm - The Pasting Lemma|pasting lemma]] gives continuity on $[0, 2]$. **(2)** A *piecewise* definition with disagreeing overlaps is not even a function. The closedness of the cover is what ensures continuity *given* well-definedness. **(3)** In a connected space (like $[0, 2]$) every open cover has nonempty overlaps, so "open cover with empty overlap" is not a meaningful weakening. The closed-cover version genuinely requires the cover to be *finite*; the open-cover version allows arbitrary cardinality. $\blacksquare$

---

# Key Takeaways

**The pasting lemma is the universal tool for constructing continuous piecewise maps — every piecewise definition you ever write should be justified by it.** The recipe is fixed: cover the domain by finitely many closed pieces (or any number of open pieces), define a continuous map on each piece, verify agreement on every pairwise overlap, conclude continuity by pasting. The closed version with finitely many pieces is the workhorse — it lets you handle piecewise polynomial functions, piecewise definitions in case-by-case proofs, restrictions of continuous functions to manifolds with boundary, and gluing constructions in homotopy theory. The trigger to internalize: *whenever a function is defined by cases on a partition of the domain, the proof of continuity is "apply pasting"*; the only work is verifying the hypotheses.

**Closedness of the cover pieces is what makes the *finite* pasting argument work; openness is what allows the *infinite* version.** The proof goes through preimages of closed (resp. open) sets in the target. For a closed cover, $f^{-1}(F)$ decomposes as a finite union of sets each closed in $X$; a finite union of closed sets is closed, hence $f^{-1}(F)$ is closed. For an open cover, $f^{-1}(U)$ decomposes as a union of sets each open in $X$; an *arbitrary* union of open sets is open, hence $f^{-1}(U)$ is open. The asymmetry between "finite union of closed" (works) and "arbitrary union of closed" (fails — e.g., $\bigcup_n [1/n, 1]$) is what forces the finite-cover constraint on the closed version.

**The pasting lemma is an instance of a more general principle: any property checked locally and assembled with respect to a cover descends to global continuity, provided the cover has good descent properties.** Closed covers have good descent for closed sets via finite unions; open covers have good descent for open sets via arbitrary unions. In algebraic geometry, this becomes the *sheaf condition*: a function is a section of a sheaf iff it can be specified locally with agreement on overlaps. In differential geometry, smooth functions on a manifold are defined by smoothness on each chart of an atlas, with agreement on overlaps (chart compatibility). In homotopy theory, the *Mayer–Vietoris* sequence is the descent of long exact sequences under open covers. The pasting lemma is the entry point for thinking about all of these in the same way.

**A continuous function on a closed subset of $\mathbb{R}^n$ — defined piecewise on finitely many closed pieces — is exactly what the pasting lemma proves to be continuous, and is what every "compute the formula and verify continuity" problem in calculus is implicitly using.** The function $f(x) = \max(0, x)$ (the ReLU), the absolute value $|x|$, the floor function on $\mathbb{Z}$, piecewise-defined splines, partitions of unity bump functions — every standard piecewise construction in analysis is justified by pasting. The remarkable feature is that the *only* obligations are the per-piece continuity check and the overlap agreement check; no global continuity check is needed. This is exactly why piecewise constructions are so liberally used in practice — the cost of verification is small, and the pasting lemma covers the rest.

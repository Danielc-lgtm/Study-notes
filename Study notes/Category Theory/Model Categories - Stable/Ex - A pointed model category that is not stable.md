---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Stable Model Category"
  - "Def - Topological Space"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathbf{Top}_*$ be the model category of pointed [[Def - Topological Space|topological]] spaces (or pointed simplicial sets — the argument is identical), with weak homotopy equivalences as weak equivalences. Show that $\mathbf{Top}_*$ is a pointed model category but is **not** a [[Def - Stable Model Category|stable model category]], by establishing:

(a) $\mathbf{Top}_*$ is pointed, with zero object the one-point space $*$, and its suspension is the reduced suspension $\Sigma X$ (so $\Sigma S^n = S^{n+1}$).

(b) $\Sigma$ is not essentially surjective on $\mathrm{Ho}(\mathbf{Top}_*)$: exhibit a space that is not (weakly equivalent to) a suspension. Conclude $\Sigma$ is not an equivalence, so $\mathbf{Top}_*$ is not stable.

(c) Confirm via the [[Thm - Characterization of Stable Model Categories|characterization theorem]] that $\mathrm{Ho}(\mathbf{Top}_*)$ is therefore *not* triangulated (it is only pre-triangulated).

**Recall:**

![[Def - Stable Model Category#The Definition]]

The reduced suspension of a pointed space $X$ is $\Sigma X = (X \times [0,1])/(X \times \{0\} \cup X \times \{1\} \cup \{x_0\} \times [0,1])$ — crush top, bottom, and the basepoint segment. A functor is an **equivalence of categories** iff it is fully faithful and essentially surjective.

---

# Convergent Strategy

**Problem class:** This is a "produce a counterexample to stability" problem — the dual of verifying stability. The topic page flags this as the canonical non-example, and the strategy is to attack the *easiest-to-falsify* part of "equivalence," namely essential surjectivity.

**Assumption pattern:** The resource is that suspensions are highly special spaces: a suspension $\Sigma X$ is always simply connected (its fundamental group is trivial) and its homology/cohomology has a specific suspension structure. So any space failing one of these constraints cannot be a suspension. The cheapest obstruction is the fundamental group.

**Theorem routing:** Establish pointedness and identify $\Sigma$ as the reduced suspension; find a space $W$ with $\pi_1(W) \neq 0$ (so $W$ is not a suspension, since suspensions are simply connected); conclude $\Sigma$ is not essentially surjective, hence not an equivalence, hence $\mathbf{Top}_*$ is not stable; finally invoke the [[Thm - Characterization of Stable Model Categories|characterization theorem]] (not stable $\Rightarrow$ not triangulated).

**Key decision point:** The non-obvious choice is *which* failure of "equivalence" to attack. Fully-faithfulness fails too (the unit $X \to \Omega\Sigma X$ is not an iso), but that is harder to see; essential surjectivity is falsified by a single well-chosen space, and the simplest obstruction is "suspensions are simply connected." Choosing the fundamental-group obstruction makes the counterexample one line.

---

# Legal Operations Used

1. **Operation 4 from the topic page (suspend or desuspend) — shown to be illegal here.** This exercise demonstrates exactly when operation 4 *fails*: desuspension is not available in $\mathbf{Top}_*$ because $\Sigma$ is not surjective.

2. **Operation 8 from the topic page (transport along a Quillen equivalence).** Used implicitly: the same conclusion holds for pointed simplicial sets, Quillen equivalent to $\mathbf{Top}_*$.

---

# Hints

> [!note]- Hint 1
> The one-point space $*$ is both initial and terminal in $\mathbf{Top}_*$, so $\mathbf{Top}_*$ is pointed with $* = 0$. Its suspension is the reduced suspension, and $\Sigma S^n = S^{n+1}$.

> [!note]- Hint 2
> To show $\Sigma$ is not an equivalence, it is enough to show it is not essentially surjective. What do *all* suspensions have in common? A reduced suspension $\Sigma X$ is the union of two cones glued along $X$; by van Kampen it is simply connected.

> [!note]- Hint 3
> Take $W = S^1$. Its fundamental group is $\mathbb{Z} \neq 0$, but every suspension is simply connected, so $S^1$ is not weakly equivalent to any suspension. Hence $\Sigma$ misses $S^1$ and is not essentially surjective.

---

# Solution

The plan: confirm pointedness, identify the suspension, then defeat essential surjectivity with a non-simply-connected space, and read off non-triangulation from the characterization theorem.

**Step 1: $\mathbf{Top}_*$ is pointed and $\Sigma$ is the reduced suspension.**

> [!note]- Derivation
> The one-point space $*$ is the terminal object (unique map $X \to *$) and, as a pointed space, also the initial object (the basepoint inclusion $* \to X$ is the unique pointed map), so $*$ is a zero object and $\mathbf{Top}_*$ is pointed. The suspension $\Sigma X$, the homotopy cofiber of $X \to *$, is the reduced suspension: crush $X$ at both ends of a cylinder. On spheres this gives $\Sigma S^n = S^{n+1}$, the prototype.

**Step 2: $\Sigma$ is not essentially surjective.**

> [!note]- Derivation
> Every reduced suspension $\Sigma X$ is **simply connected**. Indeed $\Sigma X = C_+X \cup_X C_-X$ is the union of two cones (each contractible) glued along $X$; van Kampen's theorem gives $\pi_1(\Sigma X) = \pi_1(C_+X) *_{\pi_1(X)} \pi_1(C_-X) = 1 *_{\pi_1(X)} 1 = 1$ (a free product of trivial groups amalgamated over anything is trivial, as the cones kill all loops). Now take $W = S^1$, with $\pi_1(S^1) = \mathbb{Z} \neq 1$. Since $\pi_1$ is a homotopy invariant, $S^1$ is not weakly equivalent to any simply connected space, hence not to any suspension. So no object of $\mathrm{Ho}(\mathbf{Top}_*)$ in the image of $\Sigma$ is isomorphic to $S^1$: $\Sigma$ is not essentially surjective.

**Step 3: $\mathbf{Top}_*$ is not stable, and $\mathrm{Ho}(\mathbf{Top}_*)$ is not triangulated.**

> [!note]- Derivation
> A functor that is not essentially surjective is not an equivalence; so $\Sigma$ is not an equivalence on $\mathrm{Ho}(\mathbf{Top}_*)$, and by the definition of stability, $\mathbf{Top}_*$ is **not** a stable model category. By the [[Thm - Characterization of Stable Model Categories|characterization theorem]] (a pointed model category's homotopy category is triangulated iff the model category is stable), $\mathrm{Ho}(\mathbf{Top}_*)$ is **not** triangulated. It is only **pre-triangulated**: it has cofiber sequences and the adjunction $\Sigma \dashv \Omega$, but $\Sigma$ cannot be inverted, so triangles cannot be rotated backwards. This is exactly the gap that stabilization (passing to spectra) closes.

> [!note]- Complete formal solution
> *Pointed.* The one-point space $*$ is a zero object, so $\mathbf{Top}_*$ is pointed; $\Sigma$ is the reduced suspension, $\Sigma S^n = S^{n+1}$.
>
> *Not essentially surjective.* Every suspension $\Sigma X = C_+X \cup_X C_-X$ is simply connected by van Kampen (both cones are contractible). But $S^1$ has $\pi_1 = \mathbb{Z} \neq 1$, so $S^1$ is not weakly equivalent to any suspension. Hence $\Sigma$ omits $S^1$ from its essential image.
>
> *Not stable, not triangulated.* Not essentially surjective $\Rightarrow$ not an equivalence $\Rightarrow$ not stable. By the characterization theorem, $\mathrm{Ho}(\mathbf{Top}_*)$ is not triangulated; it is pre-triangulated only. $\blacksquare$

---

# Key Takeaways

**To disprove stability, attack essential surjectivity with a single bad object — and "suspensions are simply connected" is the cheapest obstruction.** The general technique for showing a pointed model category is *not* stable is to find one object that cannot be a suspension. Suspensions are constrained (simply connected, with a specific homology suspension), so any space violating a constraint is a witness. The trigger to remember: "is $\Sigma$ surjective?" is the first question to ask about stability, and the fundamental group is the first obstruction to check, because it is a one-line van Kampen computation.

**Pre-triangulated is genuinely weaker than triangulated, and pointed spaces are the canonical witness.** This exercise makes concrete the distinction the chapter rests on: having cofiber sequences and a suspension is *not* enough for a triangulated category — you also need to be able to desuspend. The transferable diagnostic: whenever you have cofiber sequences but cannot rotate triangles backwards, you are in a pre-triangulated, non-stable situation, and the repair is stabilization. Recognizing this prevents the common error (illegal operation 3 on the topic page) of treating any pointed homotopy category as if it were triangulated.

**Stabilization exists precisely to fix this failure, and spectra are pointed spaces with $\Sigma$ forcibly inverted.** The reason the stable homotopy category $\mathcal{SH}$ is built at all is that pointed spaces fail stability in exactly the way shown here. Spectra are designed so that desuspension always works — formally, $\mathcal{SH}$ is the universal stable category receiving a functor from $\mathbf{Top}_*$. The conceptual payoff: this counterexample is not a dead end but the *motivation* for the entire stable world, the same way the failure of $\mathbb{Z}$ to have multiplicative inverses motivates $\mathbb{Q}$. Understanding why pointed spaces are not stable is understanding why spectra had to be invented.

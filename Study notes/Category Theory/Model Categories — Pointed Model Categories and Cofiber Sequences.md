---
type: topic
subject: model-categories
chapter: "6.1-6.5"
title: "Model Categories — Pointed Model Categories and Cofiber Sequences"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation Registry

This chapter works inside a **pointed** model category: a [[Def - Model Category|model category]] whose initial and terminal objects coincide in a single zero object $*$. The standing convention is that every construction lands in the [[Thm - The Homotopy Category of a Model Category|homotopy category]] $\mathrm{Ho}(\mathcal{C})$, because the suspension, loop, and (co)fiber constructions are derived functors and are only well-defined up to weak equivalence. When we write $\Sigma X$, $\Omega Y$, $C_f$, or $F_f$ we always mean the derived (homotopy) version; the strict versions are degenerate and are flagged as the recurring trap. Mapping sets $[X, Y]$ are **pointed sets**, with the zero map as basepoint, and become **groups** on suspension and **abelian groups** on double suspension.

- $\mathcal{C}, \mathcal{D}$ — pointed model categories
- $*$ — the zero object: simultaneously [[Def - Initial and Terminal Object|initial and terminal]]
- $0 = 0_{X,Y} : X \to Y$ — the zero map, the unique composite $X \to * \to Y$
- $\mathrm{Ho}(\mathcal{C})$ — the homotopy category; $[X, Y] = \mathrm{Ho}(\mathcal{C})(X, Y)$, a pointed set
- $\Sigma$ — the suspension functor on $\mathrm{Ho}(\mathcal{C})$; $\Sigma X = * \cup_X \mathrm{Cyl}(X) \cup_X *$, the homotopy pushout of $* \leftarrow X \rightarrow *$
- $\Omega$ — the loop functor; $\Omega Y = * \times_Y \mathrm{Path}(Y) \times_Y *$, the homotopy pullback of $* \rightarrow Y \leftarrow *$
- $\Sigma \dashv \Omega$ — the suspension–loop adjunction: $[\Sigma X, Y] \cong [X, \Omega Y]$
- $\eta : \mathrm{id} \to \Omega\Sigma$, $\varepsilon : \Sigma\Omega \to \mathrm{id}$ — unit and counit of $\Sigma \dashv \Omega$
- $\mathrm{Cyl}(X)$, $\mathrm{Path}(Y)$ — [[Def - Cylinder Object, Path Object, and Homotopy|cylinder and path objects]]
- $C_f$ or $Y/X$ — the homotopy cofiber of $f : X \to Y$ (homotopy pushout of $* \leftarrow X \xrightarrow{f} Y$)
- $F_f$ — the homotopy fiber of $f$ (homotopy pullback of $X \xrightarrow{f} Y \leftarrow *$)
- $\partial$ — a connecting map: $C_f \to \Sigma X$ (cofiber) or $\Omega Y \to F_f$ (fiber)
- $X \wedge S^1$, $\mathrm{Map}_*(S^1, Y)$ — smash and pointed mapping space; $= \Sigma X, \Omega Y$ in enriched cases
- $S^n$ — the $n$-sphere; $\Sigma S^n = S^{n+1}$; $\pi_n(Y) = [S^n, Y]$
- $\mathbf{Top}_*, \mathbf{sSet}_*$ — pointed spaces and pointed simplicial sets
- $\mathrm{Ch}(R)$ — chain complexes over a ring $R$; $\Sigma = [1]$ the degree shift; $\mathrm{Ho} = D(R)$

---

# Motivation

Here is the entire chapter in one sentence: in a pointed model category you can suspend, loop, and form cofiber and fiber sequences, and these obey the same long-exact-sequence calculus that organizes all of algebraic topology and homological algebra — but now as a theorem about *any* such category, not a special feature of spaces. The previous chapters built the machinery of model categories and their homotopy categories. This chapter is where that machinery starts paying out genuine homotopy theory: the suspension that turns $S^n$ into $S^{n+1}$, the long exact sequence of a pair, the long exact sequence of a fibration, and the abstract skeleton — the **pre-triangulated category** — that will become the triangulated category of the next chapter.

The hinge concept is **pointedness**. A model category becomes pointed when its initial and terminal objects coincide in a single zero object $*$. This is a small-looking hypothesis with enormous consequences: it gives a canonical **zero map** $X \to * \to Y$ between every pair of objects, which means every hom-set $[X, Y]$ is a *pointed* set with the zero map as basepoint. Pointed sets are the natural home for exact sequences (you need a basepoint to ask "is this the kernel?"), and so the whole exact-sequence apparatus becomes available. The two great examples are pointed spaces $\mathbf{Top}_*$ and pointed simplicial sets $\mathbf{sSet}_*$; the algebraic example is chain complexes $\mathrm{Ch}(R)$ pointed by the zero complex, where everything specializes to homological algebra.

From pointedness, two dual functors emerge. The **suspension** $\Sigma X$ is "$X$ with both ends crushed to a point" — categorically, the homotopy pushout of $* \leftarrow X \rightarrow *$. The **loop** $\Omega Y$ is "the based loops in $Y$" — the homotopy pullback of $* \rightarrow Y \leftarrow *$. The central theorem of §6.1 is that these are adjoint, $\Sigma \dashv \Omega$, giving the bijection $[\Sigma X, Y] \cong [X, \Omega Y]$ that specializes to the classical $\pi_{n+1}(Y) \cong \pi_n(\Omega Y)$. The whole reason this is a theorem and not a definition is the recurring lesson of the subject: **the strict pushout of $* \leftarrow X \rightarrow *$ is just $*$**, so $\Sigma$ must be the *derived* (homotopy) pushout, living on $\mathrm{Ho}(\mathcal{C})$.

Then §6.2 builds the **cofiber and fiber sequences**. The cofiber sequence $X \to Y \to C_f \to \Sigma X$ — the Puppe sequence — is the homotopy-correct cokernel, iterated until it loops back to the suspension; applying $[-, Z]$ turns it into a long exact sequence of mapping sets. The fiber sequence is the dual story, and applying $[Z, -]$ gives the dual long exact sequence. §6.3 abstracts all of this into the axioms of a **pre-triangulated category**, and proves $\mathrm{Ho}(\mathcal{C})$ is always one. The structural backbone of the chapter, and the ladder it climbs, is:
$$\text{pointed category} \;\subset\; \text{pre-triangulated category} \;\xrightarrow{\;\Sigma \text{ invertible}\;}\; \text{triangulated category}.$$

This chapter assumes you have refreshed the [[Def - Model Category|model category]] axioms, [[Def - Cofibrant and Fibrant Objects|cofibrant/fibrant objects]], the [[Def - Cylinder Object, Path Object, and Homotopy|cylinder/path object and homotopy relation]], the construction of the [[Thm - The Homotopy Category of a Model Category|homotopy category]], and [[Def - Pullback and Pushout|pullbacks and pushouts]] (you will need their homotopy versions throughout). A passing familiarity with [[Def - Higher Homotopy Group|homotopy groups]] of spaces is useful for grounding, but the chapter is self-contained. The single most important habit to bring is suspicion of strict (co)limits: in this chapter the word "the pushout" almost always means "the homotopy pushout," and forgetting this computes the trivial answer.

---

# Concept Map

## §6.1 Suspension and Loop Functors

- **[[Def - Pointed Model Category Suspension and Loop]]**
	- A **pointed model category** has a zero object $*$ (initial = terminal), hence a zero map between every pair of objects. The **suspension** $\Sigma X$ is the homotopy pushout of $* \leftarrow X \rightarrow *$ (the cylinder on $X$ with both ends collapsed); the **loop** $\Omega Y$ is the homotopy pullback of $* \rightarrow Y \leftarrow *$ (based loops in $Y$). Both are derived functors on $\mathrm{Ho}(\mathcal{C})$ — the strict versions are degenerate ($*$), so the homotopy versions are forced. In $\mathbf{Top}_*$, $\Sigma S^n = S^{n+1}$ and $\Omega Y = \mathrm{Map}_*(S^1, Y)$; in $\mathrm{Ch}(R)$, $\Sigma$ is the degree shift $X[1]$.

- **[[Thm - The Suspension-Loop Adjunction]]**
	- $\Sigma$ is left adjoint to $\Omega$ on $\mathrm{Ho}(\mathcal{C})$: there is a natural bijection $[\Sigma X, Y] \cong [X, \Omega Y]$, with unit $\eta : X \to \Omega\Sigma X$ and counit $\varepsilon : \Sigma\Omega Y \to Y$. The mechanism is that $\Sigma$ is a homotopy colimit (derived left adjoint) and $\Omega$ the dual homotopy limit, so "maps out of a colimit = maps into the matching limit." It specializes to $\pi_{n+1}(Y) \cong \pi_n(\Omega Y)$ and, in the enriched case, to the derived smash–hom adjunction $[X \wedge S^1, Y] \cong [X, \mathrm{Map}_*(S^1, Y)]$. When $\Sigma$ is invertible the unit/counit are isomorphisms and $\Omega = \Sigma^{-1}$.

> [!tip] Unlocked: The Spectrum and Stabilization *(from stable homotopy theory)*
> Forcing $\Sigma$ to be invertible by hand — taking sequences $(X_n)$ with structure maps $\Sigma X_n \to X_{n+1}$ — produces a **spectrum**, and the category of spectra is the universal stable home for the suspension. The suspension and loop defined here seed all of **stable homotopy theory** and the modern **stable $\infty$-categories**, where the shift is invertible by construction.

> [!tip] Unlocked: Loop Spaces as Group Objects (Eckmann–Hilton) *(from algebraic topology)*
> The adjunction transports the co-group structure on $\Sigma X$ (pinch the suspension coordinate) to a group structure on $\Omega Y$, making **loop spaces group objects up to homotopy** and **double loop spaces abelian**. This is the structural origin of the group structure on $\pi_n$ for $n \ge 1$ and its commutativity for $n \ge 2$.

- **[[Ex - The strict suspension is the trivial functor]]** (⭐)
	- Show the strict (non-homotopy) pushout of $* \leftarrow X \rightarrow *$ is $*$, so the suspension must be the derived pushout; verify the homotopy pushout in $\mathbf{Top}_*$ gives the reduced suspension.

- **[[Ex - Suspension of the sphere is the next sphere]]** (⭐⭐)
	- Compute $\Sigma S^n \simeq S^{n+1}$ in $\mathbf{Top}_*$ from the cone-and-collapse construction, and deduce the suspension isomorphism on homotopy/cohomology.

- **[[Ex - The shift is suspension in chain complexes]]** (⭐⭐)
	- In the pointed model category $\mathrm{Ch}(R)$, identify $\Sigma X \simeq X[1]$ and $\Omega X \simeq X[-1]$, and verify the suspension–loop adjunction is the shift adjunction $[X[1], Y] \cong [X, Y[-1]]$ in $D(R)$.

> [!note] Exercise Index — §6.1
> [[Exercise Index - §6.1 Suspension and Loop Functors]]

## §6.2 Cofiber and Fiber Sequences

- **[[Def - Cofiber and Fiber Sequence]]**
	- The **homotopy cofiber** $C_f$ of $f : X \to Y$ is the homotopy pushout of $* \leftarrow X \xrightarrow{f} Y$ (the mapping cone); iterating gives the **Puppe cofiber sequence** $X \to Y \to C_f \to \Sigma X \to \Sigma Y \to \cdots$ because the cofiber of the cofiber is the suspension. Applying $[-, Z]$ yields a long exact sequence of pointed sets. The **homotopy fiber** $F_f$ and **fiber sequence** are the exact duals, with $[Z, -]$ giving the dual long exact sequence. The connecting maps $\partial$ are the cofiber-of-cofiber and fiber-of-fiber identifications. Examples: the long exact sequence of a pair (cofiber of an inclusion) and of a fibration (fiber).

- **[[Thm - The Puppe Cofiber and Fiber Sequences Agree]]**
	- For a map $f$, the long exact sequence from $[-, Z]$ on its cofiber sequence and the one from $[Z, -]$ on its fiber sequence are the **same sequence up to sign**, identified through the suspension–loop adjunction $[\Sigma X, Z] \cong [X, \Omega Z]$. The cofiber connecting map $C_f \to \Sigma X$ and the fiber connecting map $\Omega Y \to F_f$ are adjoint transposes; the sign records the orientation of the suspension coordinate. Consequently $\mathrm{Ho}(\mathcal{C})$ is pre-triangulated. This is the abstract source of the naturality of all connecting homomorphisms.

> [!tip] Unlocked: Cohomology Theories and Long Exact Sequences *(from algebraic topology)*
> Any homotopy-invariant functor $[-, Z]$ — a **cohomology theory** when $Z$ ranges over a spectrum — turns every cofiber sequence into a long exact sequence; on inclusions this is the long exact sequence of a pair, on fibrations the long exact sequence of a fibration. The Eilenberg–Steenrod exactness axiom is exactly "send cofiber sequences to exact sequences."

> [!tip] Unlocked: The Snake Lemma and Derived Functors *(from homological algebra)*
> In $D(R)$ a cofiber sequence is a distinguished triangle, and applying a **derived functor** produces a long exact sequence whose connecting maps are the snake-lemma boundary maps. This is the structural reason derived functors come with long exact sequences at all.

- **[[Ex - The cofiber of the cofiber is the suspension]]** (⭐⭐)
	- Prove $C_i \simeq \Sigma X$ for $i : Y \to C_f$ by pasting homotopy-pushout squares, establishing the connecting map and the infinite Puppe sequence.

- **[[Ex - The long exact sequence of a fibration from a fiber sequence]]** (⭐⭐)
	- Derive the classical long exact sequence $\cdots \to \pi_n(F) \to \pi_n(E) \to \pi_n(B) \to \pi_{n-1}(F) \to \cdots$ by applying $[S^n, -]$ to the fiber sequence of $E \to B$.

- **[[Ex - The cofiber sequence computes the long exact sequence of a pair]]** (⭐⭐)
	- For a cofibration $A \hookrightarrow X$, identify $C_f \simeq X/A$ and apply $[-, Z]$ to recover the long exact sequence of the pair $(X, A)$ in a cohomology theory.

> [!note] Exercise Index — §6.2
> [[Exercise Index - §6.2 Cofiber and Fiber Sequences]]

## §6.3 Pre-Triangulated Categories

- **[[Def - Pre-Triangulated Category]]**
	- A **pre-triangulated category** is a pointed category with an adjunction $\Sigma \dashv \Omega$ and classes of cofiber sequences $X \to Y \to Z \to \Sigma X$ and fiber sequences $\Omega Z \to X \to Y \to Z$, closed under isomorphism and satisfying existence, rotation, adjunction-compatibility, and long-exact-sequence axioms. It is the homotopy category of a pointed model category, axiomatized — the precursor to a triangulated category. When $\Sigma$ is moreover an *equivalence* (so $\Omega = \Sigma^{-1}$), the two sequence classes merge into distinguished triangles and one obtains a **triangulated category**. Examples: $\mathrm{Ho}(\mathbf{Top}_*)$ (pre-triangulated, not triangulated), $D(R)$ (both).

> [!tip] Unlocked: Triangulated Category and the Octahedral Axiom *(from the next chapter)*
> When the model category is **stable** — $\Sigma$ an equivalence — the pre-triangulated structure becomes a **triangulated category**: cofiber and fiber sequences merge into distinguished triangles, and one gains the octahedral axiom TR4. This governs derived categories, the stable homotopy category, and Verdier localization. The forward page is **Def - Triangulated Category** in the Stable chapter.

> [!tip] Unlocked: t-Structures and Hearts *(from derived algebraic geometry)*
> A **t-structure** on a triangulated category carves out an abelian "heart," reconstructing an abelian category and organizing perverse sheaves and weight filtrations. t-structures presuppose the (pre-)triangulated structure built here.

- **[[Ex - The homotopy category of pointed spaces is pre-triangulated but not triangulated]]** (⭐⭐)
	- Verify $\mathrm{Ho}(\mathbf{Top}_*)$ satisfies the pre-triangulated axioms, and show $\Sigma$ is not invertible (so it is not triangulated) by exhibiting an object not weakly equivalent to a suspension or via $\Omega\Sigma X \not\simeq X$.

- **[[Ex - Every triangulated category is pre-triangulated]]** (⭐⭐)
	- Show a triangulated category is pre-triangulated by setting $\Omega = \Sigma^{-1}$ and taking the distinguished triangles as both cofiber and fiber sequences; identify which axiom (invertibility of $\Sigma$) is the extra hypothesis.

- **[[Ex - The opposite of a pre-triangulated category is pre-triangulated]]** (⭐⭐⭐)
	- Show that passing to the opposite category swaps suspension with loop and cofiber sequences with fiber sequences, so the dual of a pre-triangulated category is again pre-triangulated — the formal source of the cofiber/fiber duality.

> [!note] Exercise Index — §6.3
> [[Exercise Index - §6.3 Pre-Triangulated Categories]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The questions in this chapter cluster into a handful of recurring goals. The most common is **identifying a derived (co)limit**: given a map $f$, what is its homotopy cofiber or fiber, and what is the suspension of a given object — almost always answered by replacing strict limits with homotopy ones and computing on a (co)fibrant model. A second is **establishing an adjunction or natural isomorphism**: showing $\Sigma \dashv \Omega$, or that a left Quillen functor commutes with suspension, or that two constructions agree. A third is **producing a long exact sequence** of mapping sets, homotopy groups, or (co)homology, from a cofiber or fiber sequence — this is the workhorse computational target, since long exact sequences are how one mapping set is computed from its neighbors. A fourth is **verifying axioms abstractly**: checking that $\mathrm{Ho}(\mathcal{C})$ is pre-triangulated, or that a given category is or is not triangulated. A fifth is **comparing the cofiber and fiber stories**: showing they agree, identifying connecting maps as adjoint transposes, transporting a computation from one picture to the other. These five — compute a derived (co)limit, establish an adjunction, produce a long exact sequence, verify the structural axioms, compare the dual pictures — recur because they are the ways one pins down the homotopy theory of a pointed category.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **The category is pointed** — this is the richest source, because it instantly supplies zero maps, pointed hom-sets, and hence the very possibility of exact sequences. **An object is (co)fibrant** — cofibrancy makes the suspension and cofiber computable (homotopy colimits want cofibrant inputs), fibrancy does the same for loop and fiber. **A cylinder or path object is given** — this is the concrete handle on $\Sigma$ and $\Omega$, the place where "homotopy pushout" becomes an actual pushout of a cofibration. **The category is enriched over $\mathbf{sSet}_*$ or $\mathbf{Top}_*$** — then $\Sigma = -\wedge S^1$ and $\Omega = \mathrm{Map}_*(S^1, -)$ and the adjunction is the derived smash–hom adjunction, the most computable route. **$\Sigma$ is invertible (stability)** — the strongest source, collapsing pre-triangulated to triangulated and merging the dual sequences. The recurring move is to route a source to a target: pointedness plus a cofibration routes to a cofiber sequence and a long exact sequence; enrichment routes to the explicit smash/loop formulas and the adjunction; invertibility of $\Sigma$ routes to the triangulated structure. The [[Model Categories — Pointed Model Categories and Cofiber Sequences#Problem-Solving Strategy|Problem-Solving Strategy]] section makes these routes explicit.

---

# Legal Operations

These are the moves nearly every problem in this chapter is assembled from. When stuck, scan the list and try each. Everything is self-contained: a reader who knows only the model-category basics should be able to follow each operation from the description alone.

**Legal operations:**

1. **Replace a strict (co)limit by its homotopy version.** Never compute the strict pushout or pullback of a diagram whose answer must be homotopy-invariant; instead cofibrantly/fibrantly replace the diagram and take the honest (co)limit. *Trigger:* any "$\Sigma$", "$\Omega$", "$C_f$", or "$F_f$" in the problem. *Pattern:* "the strict pushout of $* \leftarrow X \rightarrow *$ is $*$, so replace $X \to *$ by the cofibration into a cone and take the pushout $* \cup_X \mathrm{Cyl}(X) \cup_X *$." This is the single most important operation in the chapter and the source of the recurring trap.

2. **Cofibrant/fibrant-replace before computing.** Suspension and cofiber want a [[Def - Cofibrant and Fibrant Objects|cofibrant]] source; loop and fiber want a fibrant target. *Trigger:* the object you are handed may not be (co)fibrant. *Pattern:* "replace $X$ by a cofibrant model $QX$, replace $Y$ by a fibrant model $RY$; this changes nothing in $\mathrm{Ho}(\mathcal{C})$ and makes the construction defined."

3. **Recognize a homotopy pushout/pullback square with a corner at $*$.** A square with one corner the zero object is exactly a cofiber square (if a pushout) or fiber square (if a pullback). *Trigger:* a $*$ appears in a square. *Pattern:* "this is the cofiber square of $f$, so the missing corner is $C_f$ and the induced map to $\Sigma X$ is the connecting map."

4. **Paste (co)cartesian squares to extend a sequence.** The Puppe sequence is a horizontal strip of homotopy-pushout squares; gluing the cofiber square of $f$ to the cofiber square of $i$ exhibits the cofiber of $i$ as $\Sigma X$. *Trigger:* you want to continue a cofiber/fiber sequence past three terms. *Pattern:* "paste the next square; the outer rectangle is again a homotopy pushout, identifying the new term as a suspension."

5. **Apply $[-, Z]$ to a cofiber sequence, or $[Z, -]$ to a fiber sequence.** This converts an (infinite) cofiber/fiber sequence into a long exact sequence of pointed sets. *Trigger:* you want to compute a mapping set, homotopy group, or (co)homology. *Pattern:* "$[-, Z]$ sends $X \to Y \to C_f$ to an exact $[C_f, Z] \to [Y, Z] \to [X, Z]$; chase the long exact sequence."

6. **Use the suspension–loop adjunction to move $\Sigma$ across.** Rewrite $[\Sigma X, Z]$ as $[X, \Omega Z]$ (or back) via [[Thm - The Suspension-Loop Adjunction]]. *Trigger:* a $\Sigma$ on the source or an $\Omega$ on the target of a mapping set, or a need to relate a cofiber and a fiber computation. *Pattern:* "by $\Sigma \dashv \Omega$, $[\Sigma X, Z] \cong [X, \Omega Z]$, turning the tail of the cofiber sequence into the head of the fiber sequence."

7. **Rotate a (co)fiber sequence.** A three-term cofiber sequence $X \to Y \to Z \to \Sigma X$ is equivalent to $Y \to Z \to \Sigma X \to \Sigma Y$ (with a sign). *Trigger:* you have exactness at one spot and want it elsewhere. *Pattern:* "rotate so the term you care about sits in the middle, then read off exactness; carry the $-1$ on $\Sigma f$."

8. **Specialize to the enriched formulas $\Sigma = -\wedge S^1$, $\Omega = \mathrm{Map}_*(S^1, -)$.** When the category is enriched/tensored/cotensored over $\mathbf{sSet}_*$, replace the abstract homotopy (co)limits by smash and mapping spaces. *Trigger:* $\mathcal{C}$ is $\mathbf{Top}_*$, $\mathbf{sSet}_*$, spectra, or simplicial. *Pattern:* "compute $\Sigma X = X \wedge S^1$ directly, and the adjunction is the derived smash–hom adjunction."

9. **Transport a computation across a left Quillen functor.** A left [[Def - Quillen Adjunction and Quillen Equivalence|Quillen functor]] commutes with suspension and cofibers (it is a derived left adjoint). *Trigger:* a Quillen adjunction relates two pointed model categories. *Pattern:* "$LF$ commutes with $\Sigma$ and $C_f$, so compute downstairs and push across $F$" — for instance geometric realization matching simplicial and topological suspension.

**Illegal but tempting operations:**

> [!warning] 1. Computing $\Sigma X$ as the strict pushout of $* \leftarrow X \rightarrow *$
> It is tempting to take the literal pushout. But $*$ is terminal, so the strict pushout of two maps to $*$ over $X$ collapses to $*$ for every $X$ — the strict suspension functor is constant at the zero object. The fix is the **homotopy** pushout: replace the legs $X \to *$ by cofibrations (cones) and take the pushout $* \cup_X \mathrm{Cyl}(X) \cup_X *$. The operation becomes legal exactly when the inputs are cofibrant and the legs are cofibrations.

> [!warning] 2. Taking the strict cokernel as the cofiber
> For a map $f : X \to Y$, the strict cokernel $Y/f(X)$ looks like the right "$Y$ modulo $X$," but it is not homotopy-invariant and does **not** make $[-, Z]$ exact: there can be maps $Y \to Z$ killing $X$ that fail to extend over the strict quotient. The standard witness is any non-cofibration $f$, where $Y/f(X) \not\simeq C_f$. The operation becomes legal exactly when $f$ is a cofibration between cofibrant objects, in which case the strict and homotopy cofibers agree.

> [!warning] 3. Assuming $\Omega\Sigma X \cong X$ (treating $\Sigma$ as invertible)
> The adjunction unit $\eta : X \to \Omega\Sigma X$ exists, but it is **not** an isomorphism in general — only when the category is stable. The counterexample is $\mathbf{Top}_*$ with $X = S^0$: $\Omega\Sigma S^0 = \Omega S^1$ has the homotopy type of $\mathbb{Z}$ (countably many points), not $S^0$. Treating $\Sigma$ as invertible silently assumes stability and wrongly promotes the pre-triangulated structure to triangulated. The operation becomes legal exactly when $\mathcal{C}$ is a **stable** model category.

> [!warning] 4. Concluding the cofiber and fiber sequences are isomorphic *on the nose*
> The agreement theorem says the two long exact sequences agree *up to sign* on mapping sets — it does **not** say the objects $C_f$ and $\Sigma F_f$, or the sequences themselves, are literally isomorphic in the unstable case. In $\mathbf{Top}_*$ the cofiber and fiber of the same map are genuinely different objects (the cofiber adds a cone, the fiber restricts to a preimage). They coincide as objects only when $\Sigma$ is invertible. The operation becomes legal — objects and all — exactly in the stable case.

---

# Problem-Solving Strategy

The problems in this chapter are won at the moment you decide whether to work strictly or homotopically, so begin there: almost every difficulty in the subject is some version of "I computed the strict (co)limit and got nonsense." The governing reflex is that **every (co)limit in this chapter is a homotopy (co)limit unless the inputs are already (co)fibrant and the maps already (co)fibrations.** Train yourself to see the trap before the computation: the strict pushout of $* \leftarrow X \rightarrow *$ is $*$, the strict cokernel of a non-cofibration is the wrong cofiber, and the strict pullback of $* \rightarrow Y \leftarrow *$ is $*$. Replace, then compute.

If the problem **asks you to compute a suspension, loop, cofiber, or fiber**, the route is fixed: cofibrantly/fibrantly replace as needed, then realize the homotopy (co)limit as a strict (co)limit of the replaced diagram. For $\Sigma X$ this means "cone on both ends of a cylinder"; for $\Omega Y$ "paths in $Y$ from basepoint to basepoint"; for $C_f$ "mapping cone"; for $F_f$ "homotopy fiber." In an enriched category, short-circuit all of this with $\Sigma X = X \wedge S^1$ and $\Omega Y = \mathrm{Map}_*(S^1, Y)$ — the explicit formulas are almost always the fastest path, and they make the suspension–loop adjunction the obvious smash–hom adjunction.

If the problem **asks you to produce a long exact sequence** — of homotopy groups, mapping sets, or (co)homology — the route runs through a cofiber or fiber sequence. Decide which by asking whether you are computing maps *out of* the objects (use a cofiber sequence and $[-, Z]$) or maps *into* them (use a fiber sequence and $[Z, -]$). Then build the relevant sequence: for an inclusion, the cofiber is the quotient and you get the long exact sequence of a pair; for a fibration, the fiber gives the long exact sequence of a fibration. The connecting map is always the cofiber-of-cofiber (a suspension) or fiber-of-fiber (a loop), so the sequence is infinite and you may rotate it to put the term you want in the middle. When you need to relate a maps-out computation to a maps-in one — for instance to identify a connecting homomorphism in both pictures — invoke [[Thm - The Puppe Cofiber and Fiber Sequences Agree]] and the [[Thm - The Suspension-Loop Adjunction|adjunction]] $[\Sigma X, Z] \cong [X, \Omega Z]$.

If the problem **asks you to verify a structural claim** — that $\mathrm{Ho}(\mathcal{C})$ is pre-triangulated, that a category is or is not triangulated — the strategy is to check the four ingredients and not get lost in the coherence fine print. Confirm there is a zero object (pointedness), an adjunction $\Sigma \dashv \Omega$, the two families of distinguished sequences, and the long-exact-sequence axiom; for triangulated, additionally check $\Sigma$ is an equivalence. The discriminating test between pre-triangulated and triangulated is *always* invertibility of $\Sigma$, so the productive question is "is $\Omega\Sigma X \simeq X$?" — yes for $D(R)$ and spectra, no for $\mathbf{Top}_*$.

A meta-strategy threads through all of the above: **when a construction looks degenerate, you have computed it strictly; derive it.** The entire chapter is the systematic homotopy-correction of the naive pointed-category constructions, and every theorem is a statement that the corrected version behaves the way the naive version was supposed to. The single unifying question of the chapter is: *what is the homotopy-invariant version of "kernel and cokernel," and what exact-sequence calculus does it obey?*

---

# Most Reusable Properties

- **[[Thm - The Suspension-Loop Adjunction|Suspension–Loop Adjunction]]**: $[\Sigma X, Y] \cong [X, \Omega Y]$. This is the most-used single fact in the chapter because it converts every $\Sigma$ on a source into an $\Omega$ on a target and vice versa, which is exactly the move that relates cofiber computations to fiber computations. Reach for it whenever a suspension appears in a mapping set, whenever you need to shift homotopy degree ($\pi_{n+1}(Y) = \pi_n(\Omega Y)$), and whenever you must compare the dual exact sequences. Its most powerful disguised use is recognizing that the tail of a cofiber long exact sequence, $[\Sigma X, Z]$, is the head of a fiber long exact sequence, $[X, \Omega Z]$.

- **The (co)fiber-of-(co)fiber identity**: $C_i \simeq \Sigma X$ for $i : Y \to C_f$, and $F_p \simeq \Omega Y$ for $p : F_f \to X$. This is what makes a three-term sequence infinite and is the engine of the Puppe sequence. Its typical use is to continue an exact sequence: once you have $X \to Y \to C_f$, the next term is forced to be $\Sigma X$, then $\Sigma Y$, and so on. Recognize its applicability whenever you have a cofiber or fiber sequence and want more terms — you never recompute, you just suspend or loop.

- **The homotopy-(co)limit replacement principle**: a (co)limit computes the homotopically correct object only when its inputs are (co)fibrant and its legs are (co)fibrations. This is more reusable than any single theorem because it underlies every computation in the chapter and most of the rest of the book. The typical use is diagnostic: when a construction comes out degenerate (equal to $*$, or not homotopy-invariant), the cause is always a strict (co)limit that should have been derived.

- **The long exact sequence from a (co)fiber sequence**: $[-, Z]$ on a cofiber sequence and $[Z, -]$ on a fiber sequence are exact. This is the chapter's computational payoff and the reason the whole apparatus exists. Its typical use is to compute one mapping set from its neighbors — the long exact sequence of a pair, of a fibration, of Ext, of homology are all single instances. Reach for it whenever you can fit your unknown into a (co)fiber sequence with computable neighbors.

- **The pointed structure on hom-sets**: $[X, Y]$ is a pointed set (basepoint the zero map), a group on $[\Sigma X, Y]$, abelian on $[\Sigma^2 X, Y]$. This is the structure that makes "exact sequence" meaningful and is inherited by every computation. Its typical use is to know in advance what algebraic structure your answer carries: a mapping set out of a double suspension is an abelian group, so the long exact sequence there is a sequence of abelian groups, and you may use additive reasoning.

---

# Bridges

1. **Algebraic topology — the long exact sequences of a pair and of a fibration.** The cofiber sequence of a cofibration $A \hookrightarrow X$ has homotopy cofiber the quotient $X/A$, and applying a cohomology theory $E^*$ (which is by definition a functor $[-, Z]$ sending cofiber sequences to exact sequences) produces the long exact sequence of the pair $\cdots \to E^n(X/A) \to E^n(X) \to E^n(A) \to E^{n+1}(X/A) \to \cdots$, with the degree shift being the suspension. Dually, the fiber sequence of a [[Def - Cofibrant and Fibrant Objects|fibration]] $F \to E \to B$, with $[S^n, -]$ extracting [[Def - Higher Homotopy Group|homotopy groups]], is the long exact sequence of the fibration $\cdots \to \pi_n(F) \to \pi_n(E) \to \pi_n(B) \to \pi_{n-1}(F) \to \cdots$, the connecting map being exactly the $\Omega B \to F$ of the fiber sequence evaluated on spheres. The two most-used exact sequences in topology are single instances of this chapter's machinery, which is the precise sense in which model categories *are* the foundations of homotopy theory.

2. **Homological algebra — the derived category and distinguished triangles.** In the projective model structure on [[Def - Chain Map and Chain Homotopy|chain complexes]] $\mathrm{Ch}(R)$, pointed by the zero complex, the suspension is the degree shift $X \mapsto X[1]$ and a cofiber sequence $X \to Y \to C_f \to X[1]$ is exactly the **distinguished triangle** of the derived category $D(R) = \mathrm{Ho}(\mathrm{Ch}(R))$ determined by the mapping cone $C_f$. The connecting map $C_f \to X[1]$ is the shift connecting homomorphism, and applying $\mathrm{Hom}_R(-, Z)$ or homology recovers the **long exact sequence of Ext** or **of homology**, with the snake-lemma boundary map. This is the model-category origin of the triangulated structure on derived categories: the agreement theorem is what makes the cofiber sequences into a coherent triangulated calculus, and stability (invertibility of $\Sigma = [1]$) is what upgrades pre-triangulated to triangulated.

3. **Stable homotopy theory — spectra and stabilization.** A pointed model category is **stable** when $\Sigma$ is an equivalence on $\mathrm{Ho}(\mathcal{C})$. Spaces are not stable, but one can *force* stability by forming **spectra**: sequences $(X_0, X_1, \dots)$ of pointed spaces with structure maps $\Sigma X_n \to X_{n+1}$, so that $\Sigma$ becomes invertible by construction. The category of spectra is the universal stable home for the suspension, its homotopy category is the **stable homotopy category**, and a cohomology theory is precisely a functor represented by a spectrum. This chapter's suspension and loop are the seeds of the whole subject: the spectrum is "an object on which $\Sigma$ and $\Omega$ have been made mutually inverse," and the next chapter's triangulated structure is what $\mathrm{Ho}(\text{spectra})$ carries.

4. **Higher category theory — stable $\infty$-categories.** The modern refinement replaces "homotopy category with extra structure" by a **stable $\infty$-category**, in which a square is a pushout if and only if it is a pullback — so cofiber and fiber sequences are not extra data but a detected property. Passing to the homotopy category of a stable $\infty$-category recovers a triangulated category, and the pre-triangulated categories of this chapter are the model-categorical shadow of the cleaner $\infty$-categorical picture. The agreement of cofiber and fiber sequences, proved here with signs and adjunction bookkeeping, becomes the clean statement "pushout = pullback" in the $\infty$-world, which is why $\infty$-categories are regarded as the better foundation for stable homotopy theory.

---

# Insights

**The unifying frame: this chapter is the homotopy-correction of "kernel and cokernel."** In an abelian category, a map $f$ has a kernel and a cokernel, and a [[Def - Cofiber and Fiber Sequence|derived functor]] turns a short exact sequence into a long exact sequence. None of this is homotopy-invariant on the nose in a model category — the strict kernel and cokernel are the wrong objects. The chapter's entire content is the homotopy-invariant replacement: the **homotopy fiber** is the corrected kernel, the **homotopy cofiber** is the corrected cokernel, the **loop** and **suspension** are the corrected "shift," and the long exact sequences are automatic rather than requiring a derived functor. Once you see the chapter this way, every construction has a familiar antecedent: $\Omega =$ "kernel of the map to a point," $\Sigma =$ "cokernel of the map from a point," and the Puppe sequence is "the long exact sequence you always wanted, with the connecting map built in."

**The true name of suspension is "homotopy cofiber of the map to a point," and of loop is "homotopy fiber of the map from a point."** The cone-and-collapse picture and the based-loops picture are how you compute, but they hide why $\Sigma$ and $\Omega$ sit where they do in the exact sequences. Thinking of $\Sigma X$ as the cofiber of $X \to *$ immediately tells you it is the last term of a cofiber sequence and obeys all the long-exact-sequence machinery; thinking of $\Omega Y$ as the fiber of $* \to Y$ tells you it is the first term of a fiber sequence. This is also why the cofiber-of-cofiber is the suspension: the cofiber of $Y \to C_f$ is the cofiber of the cofiber, which collapses $Y$ and leaves the cone on $X$, i.e. $X \to *$ cofibered, i.e. $\Sigma X$.

**Everything degenerate is a strict limit; everything correct is derived.** This is the chapter's master trigger-reaction pattern. When you see $\Sigma X = *$, or a cofiber sequence that fails to be exact, or $\Omega\Sigma X$ behaving like $X$ when it should not, the diagnosis is always the same: a strict (co)limit was used where a homotopy one was needed. The reaction is to cofibrantly/fibrantly replace and re-derive. The reason this pattern is so reliable is structural — the strict pushout/pullback functors are degenerate precisely because the zero object is both initial and terminal, so the corrections are not optional polish but the whole substance.

**Pre-triangulated is "triangulated before the shift is inverted," and that one difference is the unstable/stable divide.** The temptation is to think pre-triangulated and triangulated are nearly the same; they are separated by exactly one hypothesis, invertibility of $\Sigma$, and that hypothesis is the entire difference between unstable and stable homotopy theory. Spaces are the eternal unstable example: $\Sigma$ is wildly non-invertible (the Freudenthal theorem measures how non-invertible), so $\mathrm{Ho}(\mathbf{Top}_*)$ is pre-triangulated and no more. Inverting $\Sigma$ — by passing to spectra — is *defining* stable homotopy theory. So the pre-triangulated/triangulated distinction is not a technicality; it is the categorical name for the most important dichotomy in homotopy theory.

**The cofiber and fiber pictures are the same theorem read in a mirror, and the adjunction is the mirror.** It is natural to learn the long exact sequence of a pair (cofiber, maps out) and the long exact sequence of a fibration (fiber, maps in) as separate results with separate proofs. The agreement theorem says they are one result: the connecting maps are adjoint transposes under $\Sigma \dashv \Omega$, and the two sequences are isomorphic up to sign. This is the abstract reason every connecting homomorphism you ever meet — the snake-lemma $\delta$, the Mayer–Vietoris boundary, the fibration boundary — is natural and is "the same kind of map." Duality is not a heuristic here; it is implemented by a specific adjunction, and the sign that appears is the honest orientation of the suspension coordinate, the same sign that governs the rotation axiom of triangulated categories.

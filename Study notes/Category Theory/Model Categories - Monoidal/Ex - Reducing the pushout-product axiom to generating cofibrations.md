---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Monoidal Model Category"
  - "Def - Closed Monoidal Category"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be a [[Def - Closed Monoidal Category|closed monoidal category]] that is a cofibrantly generated model category with generating cofibrations $\mathcal{I}$. Prove that, to verify the cofibration half of the [[Def - Monoidal Model Category|pushout-product axiom]] (that $f \mathbin{\square} g$ is a cofibration whenever $f, g$ are), it suffices to check it on generators: if $i \mathbin{\square} i'$ is a cofibration for all $i, i' \in \mathcal{I}$, then $f \mathbin{\square} g$ is a cofibration for all cofibrations $f, g$.

Specifically, prove the **closure lemma**: for a fixed cofibration $g$, the class
$$L_g = \{\, f : f \mathbin{\square} g \text{ is a cofibration}\,\}$$
is closed under pushout, transfinite composition, and retract; and contains $\mathcal{I}$ if $i \mathbin{\square} g$ is a cofibration for every $i \in \mathcal{I}$. Conclude the reduction.

**Recall:**

For $f : U \to V$, $g : X \to Y$, the **pushout-product** is $f \mathbin{\square} g : (V \otimes X) \cup_{U \otimes X} (U \otimes Y) \to V \otimes Y$.

In a [[Def - Closed Monoidal Category|closed monoidal category]] each functor $- \otimes Z$ is a left adjoint, hence **preserves all colimits**.

In a cofibrantly generated model category, every cofibration is a **retract of an $\mathcal{I}$-cell complex**: a retract of a transfinite composite of pushouts of maps in $\mathcal{I}$. The class of cofibrations is closed under pushout, transfinite composition, and retract.

---

# Convergent Strategy

**Problem class:** This is a *closure-argument* problem, the structural backbone of every monoidal-model-category verification: show that a class defined by a pushout-product condition is "saturated" (closed under the cellular operations) and contains the generators, hence contains all cofibrations. It is the proof behind the "reduce to generators" legal operation.

**Assumption pattern:** The two assumptions doing all the work are: (i) $- \otimes Z$ preserves colimits (from closedness), so the pushout-product, built from tensors, commutes with the colimit constructions in the first variable; and (ii) cofibrations are themselves closed under pushout, transfinite composition, and retract. Matching these two closure structures is the entire proof.

**Theorem routing:** The route is to show $f \mapsto f \mathbin{\square} g$ sends pushouts/transfinite composites/retracts of $f$ to pushouts/transfinite composites/retracts of $f \mathbin{\square} g$ (using colimit-preservation of $\otimes$), and then to invoke that cofibrations are closed under exactly these operations. Then a cofibration, being a retract of an $\mathcal{I}$-cell, lands in $L_g$ provided $\mathcal{I} \subseteq L_g$.

**Key decision point:** The non-obvious move is to fix one variable $g$ and study the *operator* $f \mapsto f \mathbin{\square} g$ as a functor on the arrow category, then to observe it preserves the relevant colimits because $\otimes$ does. One must resist trying to manipulate $f$ and $g$ symmetrically at once; the clean argument fixes $g$, saturates in $f$, then by symmetry fixes a generating $i$ and saturates in $g$.

---

# Legal Operations Used

1. **Operation 3 (reduce an axiom to the generating cofibrations), topic page.** This exercise *is* the justification of that operation: we prove the reduction is valid.

2. **Operation (colimit-preservation of the tensor), from closedness.** We use repeatedly that $- \otimes Z$ is a left adjoint and so preserves pushouts and transfinite composites, which is what lets the pushout-product operator commute with the cellular constructions.

---

# Hints

> [!note]- Hint 1
> Fix $g$ and think of $f \mapsto f \mathbin{\square} g$ as an operation on arrows. You want to show: if $f$ is a pushout/transfinite composite/retract of maps in $L_g$, then $f \in L_g$.

> [!note]- Hint 2
> The pushout-product is assembled from $- \otimes X$, $- \otimes Y$ (objects of $g$) applied to $f$, glued by a pushout. Since $- \otimes Z$ preserves colimits (it is a left adjoint), $f \mapsto f \mathbin{\square} g$ commutes with pushouts and transfinite composites of $f$.

> [!note]- Hint 3
> Cofibrations are closed under pushout, transfinite composition, and retract. So if $f \mathbin{\square} g$ is built (via the colimit-commuting operator) from cofibrations $i \mathbin{\square} g$, it is a cofibration.

> [!note]- Hint 4
> Every cofibration is a retract of an $\mathcal{I}$-cell complex. If $\mathcal{I} \subseteq L_g$ and $L_g$ is closed under the cellular operations, then every cofibration is in $L_g$. Then run the symmetric argument: fix a generating $i$, vary $g$, reduce to $i \mathbin{\square} i'$.

---

# Solution

The route is: (1) show the operator $f \mapsto f \mathbin{\square} g$ commutes with pushout, transfinite composition, and retract, using colimit-preservation of $\otimes$; (2) deduce $L_g$ is closed under these operations because cofibrations are; (3) since cofibrations are retracts of $\mathcal{I}$-cells, $\mathcal{I} \subseteq L_g$ gives all cofibrations in $L_g$; (4) symmetrize over $g$ to reduce to $\mathcal{I} \mathbin{\square} \mathcal{I}$.

**Step 1: The pushout-product operator commutes with colimits in the first variable.**

> [!note]- Derivation
> Fix $g : X \to Y$. For a map $f : U \to V$, the pushout-product $f \mathbin{\square} g$ is the map out of the [[Def - Pullback and Pushout|pushout]] $(V \otimes X) \cup_{U \otimes X} (U \otimes Y) \to V \otimes Y$, built from the functors $- \otimes X$ and $- \otimes Y$ applied to $f$ and a pushout gluing. Because $\mathcal{C}$ is [[Def - Closed Monoidal Category|closed]], each $- \otimes Z$ is a left adjoint and preserves all colimits. Therefore the assignment $f \mapsto f \mathbin{\square} g$, regarded as a functor from the arrow category to the arrow category, commutes with pushouts, transfinite composites, and retracts taken in the variable $f$ — these are all colimit constructions in the arrow category, and $- \otimes Z$ preserves them. Concretely: if $f$ is a pushout of $f_0$ along some map, then $f \mathbin{\square} g$ is the corresponding pushout of $f_0 \mathbin{\square} g$; if $f = \mathrm{colim}\, f_\beta$ is a transfinite composite, $f \mathbin{\square} g = \mathrm{colim}(f_\beta \mathbin{\square} g)$; retracts go to retracts.

**Step 2: $L_g$ is closed under pushout, transfinite composition, and retract.**

> [!note]- Derivation
> Cofibrations in any model category are closed under pushout, transfinite composition, and retract (a standard consequence of their characterization by the left lifting property — see [[Thm - The Retract Argument]] and [[Thm - Closure Properties of the Model Structure]]). Combine with Step 1: if $f$ is a pushout of $f_0 \in L_g$, then $f \mathbin{\square} g$ is a pushout of the cofibration $f_0 \mathbin{\square} g$, hence a cofibration, so $f \in L_g$. The same for transfinite composites and retracts. Therefore $L_g$ is a class closed under exactly the cellular operations.

**Step 3: $\mathcal{I} \subseteq L_g$ forces all cofibrations into $L_g$.**

> [!note]- Derivation
> Suppose $i \mathbin{\square} g$ is a cofibration for every generating cofibration $i \in \mathcal{I}$, i.e. $\mathcal{I} \subseteq L_g$. Every cofibration $f$ is a retract of a transfinite composite of pushouts of maps in $\mathcal{I}$ (cofibrant generation). Since $L_g$ contains $\mathcal{I}$ and is closed under pushout, transfinite composition, and retract (Step 2), it contains every such retract — i.e. every cofibration. Hence $f \mathbin{\square} g$ is a cofibration for *all* cofibrations $f$, given that it is for generating $f$.

**Step 4: Symmetrize to reduce both variables to generators.**

> [!note]- Derivation
> Step 3 shows: if $i \mathbin{\square} g$ is a cofibration for all $i \in \mathcal{I}$, then $f \mathbin{\square} g$ is a cofibration for all cofibrations $f$. Now run the identical argument in the *second* variable, fixing a generating cofibration $i \in \mathcal{I}$ and letting $L^i = \{g : i \mathbin{\square} g \text{ is a cofibration}\}$. By symmetry of $\mathbin{\square}$ (which holds in a symmetric monoidal category, $f \mathbin{\square} g \cong g \mathbin{\square} f$), $L^i$ is closed under the cellular operations, and contains $\mathcal{I}$ iff $i \mathbin{\square} i'$ is a cofibration for all $i' \in \mathcal{I}$. So if $i \mathbin{\square} i'$ is a cofibration for all $i, i' \in \mathcal{I}$, then $i \mathbin{\square} g$ is a cofibration for all cofibrations $g$ (any fixed generating $i$), and then by Step 3 (with the roles set so $g$ ranges over all cofibrations) $f \mathbin{\square} g$ is a cofibration for all cofibrations $f, g$. This is the full reduction.

> [!note]- Complete formal solution
> Fix $g$. Since $\mathcal{C}$ is [[Def - Closed Monoidal Category|closed]], $- \otimes Z$ preserves colimits, so $f \mapsto f \mathbin{\square} g$ commutes with pushout, transfinite composition, and retract in $f$ (Step 1). Cofibrations are closed under these same operations ([[Thm - Closure Properties of the Model Structure]]), so $L_g = \{f : f \mathbin{\square} g \in \text{cof}\}$ is closed under them (Step 2). Every cofibration is a retract of an $\mathcal{I}$-cell complex, so if $\mathcal{I} \subseteq L_g$ then all cofibrations lie in $L_g$ (Step 3). Applying this with $g$ first a generating cofibration and then, by the symmetric argument in the second variable, an arbitrary cofibration, the hypothesis "$i \mathbin{\square} i'$ is a cofibration for all $i, i' \in \mathcal{I}$" propagates to "$f \mathbin{\square} g$ is a cofibration for all cofibrations $f, g$" (Step 4). $\qquad\blacksquare$
>
> (The trivial-cofibration half of the pushout-product axiom reduces the same way, replacing "cofibration" by "trivial cofibration" and using that trivial cofibrations are also closed under the cellular operations, with $\mathcal{J}$ in place of $\mathcal{I}$ for one variable. One checks $\mathcal{I} \mathbin{\square} \mathcal{J} \subseteq \text{triv-cof}$.)

---

# Key Takeaways

**The closure lemma is the reason monoidal model categories are *checkable*, and its engine is the colimit-preservation of the tensor.** Without this reduction, the pushout-product axiom would be an uncountable conjunction of conditions; with it, the axiom becomes a finite (or small-set) computation on generators. The structural insight is that the pushout-product operator $f \mapsto f \mathbin{\square} g$ inherits its good behaviour from a single fact — $- \otimes Z$ is a left adjoint and so preserves colimits. The transferable diagnostic: any operation built from a colimit-preserving functor will commute with cellular constructions, so any axiom about such an operation reduces to generators. This is the same mechanism behind "to check a functor is left Quillen, check it on generating (trivial) cofibrations" and "to recognize a cofibrantly generated model structure, work with $\mathcal{I}$ and $\mathcal{J}$".

**"Saturated class containing the generators" is the universal template for proving a property holds for all cofibrations.** The proof's shape — define the class of maps with the desired property, show it is closed under pushout/transfinite composition/retract, show it contains $\mathcal{I}$, conclude it contains all cofibrations — recurs throughout model category theory. The trigger-reaction pattern: when asked to prove "every cofibration has property $P$", do not induct on cells by hand; instead show $\{f : f \text{ has } P\}$ is closed under the three cellular operations and contains $\mathcal{I}$. This pattern (the "retract argument" / "small object argument" style of reasoning) is the standard tool, and recognizing the pushout-product axiom as an instance of it is what makes the verification routine rather than ad hoc.

**The closure-lemma proof is *independent of the specific category*, so verifying a monoidal model structure always factors into one generic step and one computational step.** The generic step is this lemma (always true from closedness and cofibrant generation); the computational step is the single check $\mathcal{I} \mathbin{\square} \mathcal{I} \subseteq \text{cof}$ and $\mathcal{I} \mathbin{\square} \mathcal{J} \subseteq \text{triv-cof}$ on generators, which is where the actual mathematics of the example lives (the prism boundary in $\mathbf{sSet}$, the sphere-disk computation in $\mathbf{Ch}(R)$). The reusable principle: separate the formal closure argument from the concrete generator computation. Whenever you face a new candidate monoidal model category, you owe only the generator computation; the closure lemma is borrowed wholesale. See also [[Ex - The pushout-product of boundary inclusions of simplices]] and [[Ex - Transposing the pushout-product to the pullback-hom]].

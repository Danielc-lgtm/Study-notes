---
type: exercise
subject: model-categories
difficulty: "⭐"
prereqs:
  - "Def - Reedy Category and the Reedy Model Structure"
  - "Def - Simplicial Set"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that the simplex category $\Delta$ is a [[Def - Reedy Category and the Reedy Model Structure|Reedy category]] with degree $\deg[n] = n$, direct subcategory $\Delta^{+}$ the order-preserving *injections* (cofaces), and inverse subcategory $\Delta^{-}$ the order-preserving *surjections* (codegeneracies). Concretely:

(a) Verify that every non-identity injection in $\Delta$ strictly raises degree and every non-identity surjection strictly lowers degree.

(b) Prove the **unique factorization** axiom: every order-preserving map $\phi : [m] \to [n]$ factors uniquely as $\phi = \phi^{+} \circ \phi^{-}$ with $\phi^{-}$ a surjection and $\phi^{+}$ an injection.

(c) Deduce that $\Delta^{+} \cap \Delta^{-}$ consists of identities only, completing the verification that $\Delta$ is Reedy. Conclude that $\Delta^{op}$ is Reedy as well.

**Recall:**

A [[Def - Reedy Category and the Reedy Model Structure|Reedy category]] is a small category $\mathcal{R}$ with a degree function $\deg : \mathrm{ob}(\mathcal{R}) \to \lambda$ (an ordinal), and wide subcategories $\mathcal{R}^{+}$ (direct, every non-identity map strictly raising degree) and $\mathcal{R}^{-}$ (inverse, every non-identity map strictly lowering degree), such that every morphism factors uniquely as $\phi^{+} \circ \phi^{-}$ with $\phi^{-} \in \mathcal{R}^{-}$ and $\phi^{+} \in \mathcal{R}^{+}$.

![[Def - Simplicial Set#Notation]]

The objects of $\Delta$ are $[n] = \{0 < 1 < \cdots < n\}$ and the morphisms are the order-preserving (weakly monotone) functions; an **injection** misses some values, a **surjection** repeats some values.

---

# Convergent Strategy

**Problem class:** This is a "recognize a Reedy structure" problem (Legal Operation 1 from the topic page): given a concrete category, exhibit the degree function and the direct/inverse split and verify the axioms. The routine is to identify the size-raising maps as direct and the size-lowering maps as inverse, then prove unique factorization, which is always the crux.

**Assumption pattern:** The single asset is that $\Delta$'s morphisms are *functions between finite totally ordered sets*. Functions between finite sets have an image, and the image gives a canonical epi-mono factorization; the order-preservation makes the factors order-preserving too. Recognizing that "epi-mono factorization of functions" is exactly "the Reedy factorization" is what unlocks the problem.

**Theorem routing:** No theorem is invoked beyond the [[Def - Reedy Category and the Reedy Model Structure|definition of a Reedy category]] itself; the result is the *input* that makes [[Thm - Diagrams over a Reedy Category Form a Model Category]] applicable to cosimplicial and simplicial objects. Once $\Delta$ is Reedy, $\mathcal{M}^{\Delta}$ and $\mathcal{M}^{\Delta^{op}}$ are model categories and frames exist.

**Key decision point:** The non-obvious choice is *how to define the factorization canonically*. The naive attempt "factor through the image" works, but uniqueness requires care: one must show the surjection and injection are forced, not merely available. The decision is to factor $\phi : [m] \to [n]$ through its image $[\mathrm{im}\,\phi] \cong [k]$ where $k = |\mathrm{im}\,\phi| - 1$, with $\phi^{-}$ the corestriction (surjective) and $\phi^{+}$ the inclusion (injective), and then prove these are the *only* such factors.

---

# Legal Operations Used

1. **Operation 1 from the topic page (find the degree function and direct/inverse split).** We assign $\deg[n] = n$ and declare injections direct, surjections inverse — the natural choice because injections enlarge the ordinal and surjections shrink it.

2. **Operation 8 from the topic page (dualize via $\mathcal{R} \leftrightarrow \mathcal{R}^{op}$).** Once $\Delta$ is Reedy, $\Delta^{op}$ is Reedy for free, with the roles of injections and surjections (latching and matching) swapped.

---

# Hints

> [!note]- Hint 1
> A non-identity injection $[m] \hookrightarrow [n]$ must have $m < n$ (it misses at least one element), and a non-identity surjection $[m] \twoheadrightarrow [n]$ must have $m > n$ (it repeats at least one element). That settles (a).

> [!note]- Hint 2
> For (b), every function factors through its image. Take the image of $\phi$, which is a sub-ordinal of $[n]$; write $[k]$ for the ordinal of the image. The map $[m] \to [k]$ onto the image is a surjection, and $[k] \hookrightarrow [n]$ is an injection.

> [!note]- Hint 3
> For uniqueness in (b): if $\phi = \psi^{+}\psi^{-} = \chi^{+}\chi^{-}$ with both factorizations surjection-then-injection, compare images. A surjection followed by an injection has image equal to the image of the injection, so both injections have the same image, hence (being order-preserving inclusions of the same subset) are equal; then the surjections are equal by cancellation.

---

# Solution

The proof has three short pieces. We first check the degree behavior of injections and surjections (part a), then construct the epi-mono factorization and prove it unique (part b), and finally observe that a map that is both injective and surjective on finite ordinals is the identity, giving $\Delta^{+} \cap \Delta^{-} = \{\mathrm{id}\}$ and the opposite-category statement (part c).

**Step 1: Non-identity injections raise degree; non-identity surjections lower it.**

> [!note]- Derivation
> Let $\phi : [m] \to [n]$ be an order-preserving injection. Since $\phi$ is injective, $|{\mathrm{im}\,\phi}| = m+1$, and since $\mathrm{im}\,\phi \subseteq [n]$, we have $m + 1 \le n + 1$, i.e. $m \le n$. If $m = n$ then $\phi$ is an order-preserving injection of a finite ordinal to itself of the same size, hence a bijection, hence (order-preserving) the identity. So a *non-identity* injection has $m < n$: $\deg[m] < \deg[n]$, it strictly raises degree. Thus the injections form a wide subcategory $\Delta^{+}$ (closed under composition, containing identities) whose non-identity maps raise degree.
>
> Dually let $\phi : [m] \to [n]$ be an order-preserving surjection. Surjectivity forces $m + 1 \ge n + 1$, i.e. $m \ge n$, and $m = n$ again forces $\phi = \mathrm{id}$. So a non-identity surjection has $m > n$, strictly lowering degree, and the surjections form $\Delta^{-}$.

**Step 2: Every map factors uniquely as surjection-then-injection.**

> [!note]- Derivation
> Let $\phi : [m] \to [n]$ be any order-preserving map. Let $S = \mathrm{im}\,\phi \subseteq [n]$; it is a non-empty subset of a totally ordered set, so it is itself a finite total order, order-isomorphic to a unique $[k]$ with $k = |S| - 1$ via the unique order-isomorphism $\iota : [k] \xrightarrow{\cong} S \hookrightarrow [n]$ (this composite $\phi^{+} := \iota$ is the order-preserving injection picking out $S$). Define $\phi^{-} : [m] \to [k]$ by $\phi^{-}(i) = \iota^{-1}(\phi(i))$; it is order-preserving (composite of order-preserving maps) and surjective (its image is $\iota^{-1}(S) = [k]$). By construction $\phi^{+}\phi^{-} = \phi$. This is the **existence** of the factorization.
>
> **Uniqueness.** Suppose $\phi = \psi^{+}\psi^{-}$ is another factorization with $\psi^{-} : [m] \to [k']$ a surjection and $\psi^{+} : [k'] \to [n]$ an injection. The image of $\phi$ equals the image of $\psi^{+}\psi^{-}$, which equals $\mathrm{im}\,\psi^{+}$ because $\psi^{-}$ is surjective (a surjection followed by a map has the same image as that map). So $\mathrm{im}\,\psi^{+} = S = \mathrm{im}\,\phi^{+}$. Both $\psi^{+}$ and $\phi^{+}$ are order-preserving injections with image exactly $S$, hence both are *the* unique order-isomorphism $[\,|S|-1\,] \cong S \hookrightarrow [n]$; therefore $k' = k$ and $\psi^{+} = \phi^{+}$. Cancelling the (injective, hence left-cancellable) $\phi^{+}$ from $\phi^{+}\phi^{-} = \phi^{+}\psi^{-}$ gives $\phi^{-} = \psi^{-}$. The factorization is unique.

**Step 3: $\Delta^{+} \cap \Delta^{-} = \{\mathrm{id}\}$, and $\Delta^{op}$ is Reedy.**

> [!note]- Derivation
> A morphism lying in both $\Delta^{+}$ and $\Delta^{-}$ is both an order-preserving injection and an order-preserving surjection, hence an order-preserving bijection $[n] \to [n]$ (it cannot change degree, by Step 1, since it both raises-or-fixes and lowers-or-fixes). An order-preserving bijection of a finite total order is the identity. So $\Delta^{+} \cap \Delta^{-}$ contains only identities.
>
> With Steps 1–2 and this, all the Reedy axioms hold: degree function $\deg[n]=n$, wide subcategories $\Delta^{+}$ (injections) and $\Delta^{-}$ (surjections) with the correct degree behavior, and unique factorization. So $\Delta$ is a Reedy category.
>
> Finally, $\Delta^{op}$ is Reedy with the *same* degree function and the roles swapped: $(\Delta^{op})^{+} = (\Delta^{-})^{op}$ (the surjections, now raising degree in the opposite category) and $(\Delta^{op})^{-} = (\Delta^{+})^{op}$. Unique factorization in $\Delta^{op}$ is the unique factorization in $\Delta$ read backwards (injection-then-surjection becomes surjection-then-injection in the opposite). This is the general fact that the opposite of a Reedy category is Reedy.

> [!note]- Complete formal solution
> **(a)** An order-preserving injection $\phi : [m] \to [n]$ has $|{\mathrm{im}\,\phi}| = m+1 \le n+1$, so $m \le n$, with equality forcing $\phi = \mathrm{id}$; hence non-identity injections strictly raise degree. Dually a surjection forces $m \ge n$ with equality forcing the identity, so non-identity surjections strictly lower degree. The injections form $\Delta^{+}$ and the surjections form $\Delta^{-}$, both wide.
>
> **(b)** Given order-preserving $\phi : [m] \to [n]$, let $S = \mathrm{im}\,\phi$, $k = |S|-1$, and $\phi^{+} : [k] \cong S \hookrightarrow [n]$ the unique order-isomorphism onto $S$; set $\phi^{-} = (\phi^{+})^{-1}\circ \phi : [m] \to [k]$, an order-preserving surjection. Then $\phi = \phi^{+}\phi^{-}$. If $\phi = \psi^{+}\psi^{-}$ is another epi-then-mono factorization, then $\mathrm{im}\,\psi^{+} = \mathrm{im}\,\phi = S$ (as $\psi^{-}$ is onto), so $\psi^{+} = \phi^{+}$ (both are the unique order-iso onto $S$) and then $\psi^{-} = \phi^{-}$ by left-cancelling the injection. Factorization exists and is unique.
>
> **(c)** A map in $\Delta^{+}\cap\Delta^{-}$ is an order-preserving bijection, hence the identity, so $\Delta^{+}\cap\Delta^{-} = \{\mathrm{id}\}$. All Reedy axioms hold, so $\Delta$ is Reedy. Reversing all arrows and swapping the two subcategories shows $\Delta^{op}$ is Reedy. $\blacksquare$

---

# Key Takeaways

**Epi-mono factorization is the prototype of Reedy factorization, and recognizing it everywhere is the trigger for Reedy structures.** The unique surjection-then-injection factorization of order-preserving maps is the model on which the entire Reedy axiom is patterned: "factor uniquely as inverse-then-direct" is just "factor uniquely as epi-then-mono" with epis renamed degeneracies and monos renamed faces. Whenever you meet an indexing category whose morphisms have a canonical image — finite sets and functions, finite ordinals and monotone maps, posets with a rank — the epi-mono factorization is your candidate Reedy factorization, and the size of the image is your candidate degree. This is the single most reusable recognition pattern for putting homotopy theory on diagrams: see a category of "shapes with faces and degeneracies," suspect it is Reedy, and look for the image factorization.

**The degree function must track a genuine well-ordered notion of size, and finiteness is what makes the factorization unique.** The reason $\Delta$ works so cleanly is that its objects are *finite* ordinals: a finite total order has a unique order-isomorphism to a standard ordinal, which is what forces the injection factor to be unique. If the objects had non-trivial order-automorphisms — as a category of finite sets *without* ordering does — the injection onto the image would only be defined up to that automorphism, and uniqueness would fail; that is exactly why symmetric simplicial sets and equivariant diagrams need the generalized Reedy framework. The takeaway is diagnostic: before claiming a category is Reedy, check that its objects have *no non-trivial automorphisms*, because automorphisms are precisely what break unique factorization.

**Reedy-ness is self-dual, so every cosimplicial fact has a free simplicial counterpart.** Once $\Delta$ is Reedy, $\Delta^{op}$ is Reedy automatically, with injections/surjections and latching/matching swapped. This is not a curiosity — it is the structural reason the whole theory of frames comes in dual pairs: cosimplicial frames (built from the Reedy structure on $\mathcal{M}^{\Delta}$) and simplicial frames (from $\mathcal{M}^{\Delta^{op}}$), cylinder objects and path objects, left homotopy and right homotopy. The habit to form: prove any framing or latching statement on the cosimplicial side, then read off the simplicial side by applying the $\Delta \leftrightarrow \Delta^{op}$ and $\mathcal{M} \leftrightarrow \mathcal{M}^{op}$ dualities, halving the labor. See [[Ex - Latching and matching objects for cosimplicial and simplicial objects]] for the dual latching/matching computation this unlocks.

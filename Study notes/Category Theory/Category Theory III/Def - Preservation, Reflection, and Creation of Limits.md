---
type: definition
subject: category-theory
prereqs:
  - "Def - Limit and Colimit"
  - "Def - Functor"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
tags: [category-theory, foundations]
---

# Notation

Throughout, $F : \mathcal{C} \to \mathcal{D}$ is a [[Def - Functor|functor]] and $D : J \to \mathcal{C}$ a diagram of shape $J$, with composite $F \circ D : J \to \mathcal{D}$. We write $\lim D$ for a [[Def - Limit and Colimit|limit]] in $\mathcal{C}$, and $\lim (F \circ D)$ for a limit in $\mathcal{D}$. When both exist there is a canonical **comparison morphism** $\psi : F(\lim D) \to \lim(F \circ D)$ induced by the cone $(F\pi_j)$. The full registry is on [[Category Theory III — Limits and Colimits]].

This is a compound page: it defines three interlocking notions — **preservation**, **reflection**, and **creation** of limits — because they form a strict hierarchy (creation is the strongest, and implies the other two in the presence of the relevant limits), they are constantly confused, and one cannot use any of them safely without the contrast to the others. Each has a colimit dual obtained by reversing arrows.

---

# Axiom Motivation

A functor moves diagrams from $\mathcal{C}$ to $\mathcal{D}$. The question this page answers is: what does a functor do to *limits*? There are three genuinely different things a functor might do, and conflating them is the most common error in the subject, so the definitions are built to keep them apart.

The first and most basic is **preservation**. We have a limit cone $(\pi_j : \lim D \to D_j)$ in $\mathcal{C}$; apply $F$ and get a cone $(F\pi_j : F(\lim D) \to F D_j)$ in $\mathcal{D}$. Is *that* cone a limit cone for $F \circ D$? If yes for every diagram of the relevant shape, $F$ **preserves** those limits. The desideratum is plain: a preserving functor lets you compute the limit downstairs by computing it upstairs and applying $F$ — "$F(\lim D) = \lim(F D)$". This is what you want when transporting a construction along $F$. The reason it can *fail* is that $F$ might not respect universality: $F(\lim D)$ is a cone over $FD$, but a *better* cone (a genuine limit) might exist in $\mathcal{D}$ that $F$ does not hit. The canonical failure is the [[Def - Free Group and Free Product|free product]]: the forgetful functor $U : \mathbf{Grp} \to \mathbf{Set}$ does *not* preserve coproducts, because the underlying set of $G * H$ is not the disjoint union of the underlying sets.

The second is **reflection**, which runs the implication backwards. Suppose we have a cone over $D$ in $\mathcal{C}$ and we apply $F$; if the image is a limit cone in $\mathcal{D}$, does it follow that we started with a limit cone in $\mathcal{C}$? A functor that always lets you conclude "it was already a limit upstairs, because its image is a limit downstairs" **reflects** limits. This is a recognition principle: reflection lets you *certify* a limit in $\mathcal{C}$ by checking it after applying $F$, which is useful when $\mathcal{D}$ is more concrete. The reason preservation and reflection are independent is that they are converse implications — one says "limits go down to limits", the other "things that become limits were limits". A constant functor preserves nothing interesting but a fully faithful functor always reflects.

The third and strongest is **creation**, and its subtlety is exactly why it needs its own definition. Creation handles the case where you do not yet know a limit exists in $\mathcal{C}$ at all. $F$ **creates** limits of shape $J$ if, whenever $F \circ D$ has a limit in $\mathcal{D}$, then $D has$ a limit in $\mathcal{C}$, *and* a cone over $D$ is a limit cone exactly when its $F$-image is. Creation does two jobs at once: it *transports existence* (the limit in $\mathcal{C}$ exists because the one in $\mathcal{D}$ does) and it *transports universality* (the limit upstairs is the unique lift of the one downstairs). This is the workhorse for proving completeness: the forgetful functor $U : \mathbf{Grp} \to \mathbf{Set}$ creates all limits, so because $\mathbf{Set}$ is [[Def - Complete and Cocomplete Category|complete]], $\mathbf{Grp}$ is complete — you build the limit on underlying sets and the group structure comes for free, uniquely.

Why is creation strictly stronger than preservation-plus-reflection? Because preservation and reflection both *presuppose* that the relevant limits already exist (in $\mathcal{C}$ for preservation, to have something to preserve; the image being a limit for reflection). Creation makes no such presupposition — it manufactures the limit in $\mathcal{C}$ out of the limit in $\mathcal{D}$. In the presence of all $J$-limits in both categories, creation implies both preservation and reflection; but its real content is in the existence clause, which the other two lack. Keeping this in mind prevents the standard mistake of "proving" a category is complete by showing a functor merely *preserves* limits, which says nothing about whether the limits exist upstairs.

---

# The Definition

Let $F : \mathcal{C} \to \mathcal{D}$ be a functor and fix a shape $J$.

**$F$ preserves $J$-shaped limits** if whenever $(\pi_j : L \to D_j)$ is a limit cone over $D : J \to \mathcal{C}$, the image cone $(F\pi_j : FL \to F D_j)$ is a limit cone over $F \circ D$ in $\mathcal{D}$. Equivalently, when both limits exist, the canonical comparison map
$$\psi : F(\lim D) \;\xrightarrow{\ \cong\ }\; \lim(F \circ D)$$
is an isomorphism. $F$ is **continuous** if it preserves all small limits, **cocontinuous** if it preserves all small colimits.

**$F$ reflects $J$-shaped limits** if whenever $(\lambda_j : X \to D_j)$ is a cone over $D$ such that the image $(F\lambda_j : FX \to F D_j)$ is a limit cone over $F \circ D$ in $\mathcal{D}$, the original cone $(\lambda_j)$ is already a limit cone over $D$ in $\mathcal{C}$.

**$F$ creates $J$-shaped limits** if for every diagram $D : J \to \mathcal{C}$ such that $F \circ D$ has a limit in $\mathcal{D}$: there exists a cone over $D$ in $\mathcal{C}$ whose image under $F$ is the given limit cone, this lifted cone is a limit cone over $D$, and (in the strict version) it is the *unique* cone lifting the limit. In brief: limits of $F \circ D$ in $\mathcal{D}$ lift uniquely to limits of $D$ in $\mathcal{C}$.

Each notion has a dual obtained by replacing "limit/cone" with "colimit/cocone": preservation, reflection, and creation of colimits.

Two facts pin down the hierarchy:

- If $\mathcal{C}$ has all $J$-shaped limits and $F$ creates them, then $F$ both preserves and reflects them.
- Any **fully faithful** functor [[Def - Full, Faithful, and Essentially Surjective Functor|reflects]] all limits and colimits that exist in its codomain.

---

# Relate to Other Fields / Compression

Preservation is the precise statement that "a construction commutes with a map". The most important instance in all of mathematics is that [[Thm - Right Adjoints Preserve Limits|right adjoints preserve limits]] (RAPL) and left adjoints preserve colimits — so the forgetful functor (a right adjoint to a free functor) preserves limits, and tensoring (a left adjoint) preserves colimits, which is the categorical reason $\otimes$ is right exact. Creation is the standard tool for bootstrapping completeness from $\mathbf{Set}$ to every algebraic category. Reflection is how concreteness arguments work: a faithful functor into $\mathbf{Set}$ lets you check categorical properties on underlying sets.

**True name:** *preserves* = "$F(\lim) = \lim(F)$"; *reflects* = "if $F$ of it is a limit, it was a limit"; *creates* = "limits downstairs lift uniquely to limits upstairs, existence included". The mnemonic that saves you: preservation needs the limit to exist *upstairs already*; creation *produces* it upstairs from downstairs.

---

# Examples / Corollaries

**Is an instance — the forgetful functor $U : \mathbf{Grp} \to \mathbf{Set}$ creates limits.** Given a diagram of groups whose underlying-set diagram has a limit $L$ in $\mathbf{Set}$ (a set of compatible families), there is a unique group structure on $L$ making the projections homomorphisms, and $L$ with that structure is the limit in $\mathbf{Grp}$. Hence $U$ creates all limits, and since $\mathbf{Set}$ is complete, so is $\mathbf{Grp}$. The same holds for $\mathbf{Ab}, \mathbf{Ring}, \mathbf{Mod}_R, \mathbf{Vect}_k$.

**Is an instance — representable functors preserve limits.** For any object $X$, the hom-functor $\mathcal{C}(X, -) : \mathcal{C} \to \mathbf{Set}$ preserves all limits: $\mathcal{C}(X, \lim D) \cong \lim \mathcal{C}(X, D_j)$, because a map into a limit is a compatible family of maps. See [[Thm - Representable Functors Preserve Limits]]. The [[Def - The Yoneda Embedding|Yoneda embedding]] preserves and reflects limits — but does not *create* them.

**Is an instance — fully faithful functors reflect (co)limits.** The inclusion of a [[Def - Subcategory|full subcategory]] reflects any limits present in the ambient category: if a cone in the subcategory becomes a limit upstairs, it was a limit. This is why limits computed in a full subcategory can be certified by computing in the larger category.

**Is NOT an instance — $U : \mathbf{Grp} \to \mathbf{Set}$ does not preserve coproducts.** $U$ creates limits but fails to preserve *co*limits. The coproduct of $G$ and $H$ in $\mathbf{Grp}$ is the [[Def - Free Group and Free Product|free product]] $G * H$, whose underlying set is the set of reduced alternating words — much larger than the disjoint union $U(G) \sqcup U(H) = U(G \sqcup H \text{ in } \mathbf{Set})$. So $U(G * H) \ne U(G) \sqcup U(H)$, and $U$ does not preserve coproducts. This is the headline example: a functor can create limits yet badly distort colimits. See [[Ex - The forgetful functor from groups preserves limits not colimits]].

**Is NOT an instance — a functor can preserve without reflecting.** The unique functor $F : \mathcal{C} \to \mathbf{1}$ to the terminal category preserves all limits trivially (everything in $\mathbf{1}$ is a limit), but reflects nothing: any cone in $\mathcal{C}$ maps to "the" limit in $\mathbf{1}$, so reflection would force every cone to be a limit, which is false. Preservation and reflection are independent.

**Calibration check.** Verify that an [[Def - Equivalence of Categories|equivalence of categories]] preserves, reflects, *and* creates all limits and colimits. Check that creation plus existence of all $J$-limits in $\mathcal{C}$ gives preservation. If you can produce the comparison map $\psi : F(\lim D) \to \lim(FD)$ from the universal property and say exactly which clause "preserves" asserts about $\psi$, you have the definition.

---

# Unlocked by This

> [!tip] Right Adjoints Preserve Limits (RAPL) *(from Chapter IV)*
> The flagship preservation theorem: every functor with a left adjoint preserves all limits, and dually left adjoints preserve colimits. This is why forgetful functors preserve limits (they are right adjoints to free functors), why $\mathrm{Hom}(X,-)$ preserves limits, and the obstruction one checks first when asking whether a given functor *can* be an adjoint. See [[Thm - Right Adjoints Preserve Limits]].

> [!tip] Monadicity and the Barr–Beck Theorem *(from Chapter V)*
> The **Barr–Beck monadicity theorem** characterises when a functor $U$ exhibits its domain as the category of algebras for a monad, and its hypotheses are precisely creation conditions: $U$ must create coequalizers of certain reflexive pairs. Creation of limits/colimits is the technical backbone of recognising categories of algebras and of **descent**.

> [!tip] Flat Functors and Geometric Morphisms *(from Topos Theory)*
> A functor that preserves finite limits is **left exact / flat**; the **geometric morphisms** between topoi are adjoint pairs whose left adjoint (the inverse image) is left exact. Finite-limit preservation is the defining condition of the maps in the 2-category of topoi.

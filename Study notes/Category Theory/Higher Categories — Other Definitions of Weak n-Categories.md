---
type: topic
subject: higher-categories
chapter: "10"
title: "Higher Categories — Other Definitions of Weak n-Categories"
tags: [category-theory, higher-categories, foundations]
---

# Notation Registry

Two standing conventions frame this chapter, because the chapter is *about* the variety of conventions. First, there is a deep fault line running through every definition of a higher category: **algebraic** versus **non-algebraic**. In an algebraic definition, composition is extra *structure* — a chosen operation, with chosen coherence cells, given as part of the data, so that two higher categories are the same only when an equivalence carries the chosen composites to the chosen composites. In a non-algebraic (also called *geometric*) definition, composition is a *property* — the data is just a diagram of sets or spaces, and one *requires* that composites exist and are unique up to a contractible space of choices, without ever naming a particular one. The whole chapter is the comparison of these two stances and the theorem that, at least for $(\infty,1)$-categories, they agree. Second, we use the **$(\infty,n)$ notation**: an $(\infty,n)$-category has cells in every dimension, but every cell above dimension $n$ is invertible (an equivalence). So an $(\infty,0)$-category is an $\infty$-*groupoid* (everything invertible), an $(\infty,1)$-category is the homotopy-theoretic generalisation of an ordinary category (only the 1-cells can be non-invertible), and $n$ in "weak $n$-category" counts the top dimension of possibly-non-invertible cells when there is no infinite tower.

- $\mathcal{C}, \mathcal{D}, \mathcal{E}$ — categories, or higher categories; $A, B, C, X, Y$ — objects; $f, g, h$ — morphisms (1-cells)
- $\mathcal{C}(A,B)$, $\mathrm{Hom}_{\mathcal{C}}(A,B)$ — the hom-set, hom-object, or **mapping space** between two objects
- $\omega$ — "infinitely many dimensions"; a **weak $\omega$-category** has possibly-non-invertible cells in every finite dimension
- $(\infty,n)$ — $\infty$-many dimensions of cells, all invertible above dimension $n$
- $\Delta$ — the **simplex category**: objects the nonempty finite ordinals $[n] = \{0 < 1 < \dots < n\}$, morphisms order-preserving maps
- $X : \Delta^{op} \to \mathbf{Set}$ — a **simplicial set**; $X_n = X([n])$ its set of $n$-simplices; $\Delta^n$ the standard $n$-simplex; $\Lambda^n_i$ the $i$th horn
- $X : \Delta^{op} \to \mathbf{sSet}$ — a **simplicial space** (a *bisimplicial set*); $\mathbf{sSet}$ — simplicial sets
- $\mathbf{Set}, \mathbf{Cat}, \mathbf{Top}, \mathbf{sSet}, \mathbf{Gpd}$ — sets, small categories, topological spaces, simplicial sets, groupoids (as categories)
- $\mathcal{S}$ — the $\infty$-category (or model) of **spaces** / homotopy types; "space" below always means *homotopy type*, not point-set space
- $|X|$ — geometric realisation; $\mathrm{Sing}(T)$ — the singular simplicial set of a topological space $T$
- $\pi_n(T,t)$ — the $n$th homotopy group of $T$ at the basepoint $t$; $\Pi_\infty(T)$ — the **fundamental $\infty$-groupoid** of $T$
- $P$ — a **globular operad** (the carrier of an algebraic definition); $H$ — the **Penon stretching monad**
- $\dashv$ — "is left adjoint to"; $\simeq$ — equivalence / weak equivalence / Quillen equivalence; $\cong$ — isomorphism
- $\mathrm{Map}(X,Y)$ — the **derived mapping space** between two objects of a model category or $(\infty,1)$-category

---

# Motivation

Here is the awkward truth that this chapter is built around: there is no such thing as *the* definition of a weak higher category. There are at least a dozen, proposed by different people for different reasons, and for a long time nobody could prove any two of them agreed. This is genuinely unusual in mathematics. We do not have twelve competing definitions of "group" or "topological space"; we have one, and we are confident it captures the intended notion. The fact that higher category theory spent decades with a *zoo* of definitions — Batanin, Leinster, Penon, Trimble, Tamsamani, Simpson, Street, Joyal, Rezk, Lurie, and more — tells you the intended notion is subtle, and that pinning it down is itself a deep problem. The previous chapters built one route up the mountain (globular operads, in the Batanin–Leinster style); this chapter is the survey from the summit, where you see all the other routes and, for the most important case, the theorem that they all arrive at the same place.

The definitions split along the fault line named in the Notation Registry. The **algebraic** definitions treat composition as structure you carry around. The Batanin–Leinster definition (**weak ω-category**, the subject of the previous chapter) packages all the composition operations and coherence cells into a single **globular operad** equipped with a contraction, and a weak ω-category is an algebra for it. Penon's definition does the same job with a different and strikingly economical device: a single monad $H$ on **reflexive globular sets**, built from "stretchings", whose algebras are weak ω-categories. Trimble's definition builds the tower by hand, defining weak $(n+1)$-categories as categories enriched in a suitable category of weak $n$-categories using an $E_\infty$ (topological) operad to control the coherence. These differ in machinery but share a creed: a weak higher category *has* composites, chosen, as part of its data.

The **non-algebraic** definitions take the opposite stance, learned from homotopy theory: composition is a *property*. You record a diagram — of sets, of spaces, of simplicial sets — and you *impose conditions* forcing composites to exist and be essentially unique, without ever selecting one. The **Segal condition** is the engine here. Tamsamani and Simpson iterate it to define $n$-categories as $n$-fold simplicial spaces satisfying Segal conditions [[Def - Dimension|dimension]] by dimension; **Segal categories** and Rezk's **complete Segal spaces** are the one-step ($(\infty,1)$) versions; and the **quasi-categories** of the previous chapter, where composition is encoded by inner-horn fillers, are the most widely used non-algebraic model of all. None of these ever writes down "the composite of $f$ and $g$"; they only guarantee the space of candidate composites is contractible.

The whole field would be a mess if the definitions disagreed. The two theorems of this chapter are why it is not a mess. The first is the **homotopy hypothesis**, Grothendieck's organising conjecture: weak $\infty$-*groupoids* — higher categories with everything invertible — are the same as **topological spaces up to homotopy**. This is the load-bearing sanity check on the entire enterprise: it says the simplest higher categories are exactly the objects homotopy theory has studied for a century, so any reasonable definition must reproduce homotopy theory in its invertible part. The second is the **comparison theorem** of Bergner, Joyal, Lurie, and others: for the case $(\infty,1)$ — one direction of non-invertibility, infinitely many of invertibility — *all* the standard models (quasi-categories, Segal categories, complete Segal spaces, simplicial categories, relative categories) are connected by **Quillen equivalences**, so they present *the same* homotopy theory. The choice of model is, for all structural purposes, immaterial.

The conceptual backbone of the chapter is a single grid:

$$
\begin{array}{c|c|c}
 & \textbf{algebraic (structure)} & \textbf{non-algebraic (property)} \\\hline
\textbf{globular} & \text{Batanin–Leinster, Penon} & \text{(rare)} \\\hline
\textbf{simplicial} & \text{Trimble (operadic)} & \text{quasi-categories, Tamsamani–Simpson} \\\hline
\textbf{bisimplicial} & & \text{Segal categories, complete Segal spaces}
\end{array}
$$

This chapter assumes you are comfortable with the globular-operad story (the Batanin–Leinster definition built from a contractible globular operad), with **[[Def - Simplicial Set|simplicial sets]]**, the **[[Def - Kan Complex and the Nerve|nerve]]** and **[[Def - Kan Complex and the Nerve|Kan complexes]]**, and with **[[Def - Quasi-Category|quasi-categories]]** from the previous chapter; with **[[Def - Enriched Category|enriched categories]]** (Chapter V), since simplicial categories are categories enriched in **[[Def - Simplicial Set|simplicial sets]]**; and with **[[Def - Model Category|model categories]]** and **[[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalences]]** (the [[Def - Model Category|Model Categories]] chapter), since the comparison theorem is stated in their language. From outside category theory it leans on the **[[Def - Higher Homotopy Group|homotopy groups]]** of a space and the singular simplicial set; both are recalled at point of use.

---

# Concept Map

## §1 Algebraic Definitions

- **[[Def - Penon Weak ω-Category]]**
	- An algebraic definition of weak ω-category that replaces the globular operad with a single monad. One starts with **reflexive globular sets** (globular sets with chosen degenerate "identity" cells) and builds the **Penon stretching monad** $H$ from the universal "stretching" of a strict ω-category over a reflexive globular set — a map that is the identity on cells but inserts a contraction-like structure. A Penon weak ω-category is then simply an **algebra for $H$**. The definition is remarkably compact (one monad, defined by a universal property) but the comparison with the **Batanin–Leinster** definition is delicate: Penon's original used non-reflexive globular sets and was later corrected to the reflexive version by Cheng and others.

> [!tip] Unlocked: Grothendieck–Maltsiniotis ω-Groupoids and Homotopy Type Theory *(from Higher Algebra / Type Theory)*
> Penon's "one monad" philosophy is the spiritual ancestor of the **Grothendieck–Maltsiniotis** definition of weak ω-groupoid (algebras for a "coherator"), which is the precise algebraic object the **homotopy hypothesis** is conjectured for. The same algebraic-structure-on-globular-cells viewpoint reappears in **homotopy type theory**, where the tower of identity types $a =_A b$, $p =_{a=b} q$, $\dots$ gives every type the structure of a weak ω-groupoid — a theorem of Lumsdaine and van den Berg–Garner.

- **The Batanin–Leinster definition (recalled).**
	- *(From the previous chapter — kept here as the algebraic reference point.)* A **weak ω-category** is an algebra for the initial **globular operad equipped with a contraction**: the operad supplies, in each dimension, a chosen weak composite for every pasting diagram and a chosen coherence cell mediating any two parallel composites. Composition is *structure* — the algebra map names the composites. This is the prototype against which Penon, Trimble, and the geometric definitions are compared.

- **Trimble's definition (operadic iterated enrichment).**
	- *(Page-less in this vault — described inline.)* Trimble defines weak $n$-categories by induction on $n$: a weak $(n+1)$-category is a category **[[Def - Enriched Category|enriched]]** in the category of weak $n$-categories, where the enrichment uses a fixed **$E_\infty$-operad** $\mathcal{E}$ — a topological operad of *contractible* spaces of operations — to specify the composition and all its coherences at once. Because each space $\mathcal{E}(k)$ is contractible, there is "essentially one" way to compose $k$ morphisms, but the contractible space of choices carries the higher [[Def - Homotopy|homotopies]]. It sits between the algebraic and geometric camps: composition is chosen (algebraic), but chosen from a contractible space (geometric in spirit).

> [!tip] Unlocked: $E_n$-Algebras and the Recognition Principle *(from Algebraic Topology / [[Def - Operad|Operads]])*
> The operad controlling Trimble's coherences is an instance of the **little-disks operads** $E_n$, whose algebras are $n$-fold loop spaces (May's recognition principle). The same operads govern **factorization homology** and the structure of **topological quantum field theories**; Trimble's definition is one place where the operadic machinery of homotopy theory directly builds higher categories.

- **[[Ex - Every strict omega-category is a Penon weak omega-category]]** (⭐)
	- Exhibit the $H$-algebra structure on a strict ω-category: the strict composites evaluate every freely-generated weak composite and every contraction cell maps to an identity. Shows the rigid objects embed in the weak ones.

- **[[Ex - Penon weak 1-categories are ordinary categories]]** (⭐⭐)
	- Truncate a Penon $H$-algebra to dimension $1$ and verify the absence of nondegenerate $2$-cells forces strict associativity and unitality, recovering exactly an ordinary [[Def - Category|category]]. The level-$1$ sanity check.

- **[[Ex - Trimble enrichment and the E-infinity operad]]** (⭐⭐⭐)
	- Unwind one step of Trimble's recursion: show that a category **[[Def - Enriched Category|enriched]]** in weak $n$-categories using a contractible $E_\infty$-operad has well-defined composition with all coherences supplied by the contractible operad spaces. Locates Trimble between the algebraic and geometric camps.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 Algebraic Definitions]]

## §2 Non-Algebraic and Simplicial Definitions

- **[[Def - Segal Category and Complete Segal Space]]**
	- *(Compound.)* Both are non-algebraic models of $(\infty,1)$-categories built from **simplicial spaces** $X : \Delta^{op} \to \mathbf{sSet}$, where $X_0$ is the object-space and $X_1$ the morphism-space. The **Segal condition** demands that the map $X_n \to X_1 \times_{X_0} \cdots \times_{X_0} X_1$ (the "spine inclusion") be a weak equivalence, so an $n$-tuple of composable morphisms is the same, up to homotopy, as a single $n$-simplex — this is exactly "composition exists and is essentially unique" stated as a property. A **Segal category** additionally requires $X_0$ to be a *discrete* set of objects; a **complete Segal space** (Rezk) instead requires $X_0$ to be a space and adds a **completeness** condition forcing the space of objects to match the space of self-equivalences, which rigidifies equivalences and makes the model invariant. These are the two bisimplicial models in the comparison theorem.

- **[[Def - Tamsamani-Simpson n-Category]]**
	- A non-algebraic definition of weak $n$-category by **iterated Segal conditions**. A Tamsamani–Simpson $n$-category is an $n$-fold simplicial set (a functor $(\Delta^{op})^n \to \mathbf{Set}$) satisfying a Segal condition in each simplicial direction, where the "spaces" at each stage are themselves Tamsamani–Simpson $(n-1)$-categories. The induction bottoms out at $0$-categories = sets. Each Segal condition encodes "composition in one more dimension is associative and unital up to higher equivalence", so the whole tower of weak composition and coherence is generated by the *single* Segal idea applied $n$ times — the most economical of the geometric definitions.

> [!tip] Unlocked: $(\infty,n)$-Categories and Extended TQFT *(from Higher Algebra / Mathematical Physics)*
> Iterating the Segal/completeness machinery gives **$(\infty,n)$-categories**, the natural home of the **cobordism hypothesis** of Baez–Dolan and Lurie: the $(\infty,n)$-category of fully-extended topological field theories is freely generated by a single fully-dualizable object. The $\Theta_n$-space and $n$-fold complete Segal space models (Rezk, Barwick) are the iterated-Segal descendants of the Tamsamani–Simpson definition.

- **Quasi-categories (recalled).**
	- *(From the previous chapter — the central non-algebraic model.)* A **[[Def - Quasi-Category|quasi-category]]** is a **[[Def - Simplicial Set|simplicial set]]** in which every *inner* horn $\Lambda^n_i \hookrightarrow \Delta^n$ ($0 < i < n$) has a filler. Composition is the property "inner horns fill": a $2$-simplex *exhibits* a composite, but no composite is selected, and the space of composites is contractible. Quasi-categories are the most-used model of $(\infty,1)$-categories, via Joyal's and Lurie's foundations.

- **[[Ex - The Segal condition recovers ordinary categories]]** (⭐⭐)
	- Show that a simplicial set whose Segal maps $X_n \to X_1 \times_{X_0} \cdots \times_{X_0} X_1$ are *bijections* is exactly the [[Def - Kan Complex and the Nerve|nerve]] of an ordinary [[Def - Category|category]], so the strict Segal condition is the categorical condition. The discrete prototype of the [[Def - Segal Category and Complete Segal Space|Segal-space]] machinery.

- **[[Ex - A Segal space that fails completeness]]** (⭐⭐)
	- Construct a Segal space with two equivalent objects in distinct path-components of $X_0$, verify it satisfies the Segal condition but not Rezk completeness, and explain why it is not equivalence-invariant. The canonical witness for the completeness axiom.

- **[[Ex - Tamsamani-Simpson 2-categories are bicategories]]** (⭐⭐⭐)
	- Unwind the $n=2$ [[Def - Tamsamani-Simpson n-Category|Tamsamani–Simpson]] definition: a simplicial object in categories with discrete $X_0$ and Segal maps that are equivalences, and show the hom-fibres and Segal composition assemble into a **bicategory**. The level-$2$ sanity check.

> [!note] Exercise Index — §2
> [[Exercise Index - §2 Non-Algebraic and Simplicial Definitions]]

## §3 The Comparison Problem and the Homotopy Hypothesis

- **[[Thm - The Homotopy Hypothesis]]**
	- Grothendieck's organising principle: the category of weak $\infty$-**groupoids** (higher categories with every cell invertible) is **equivalent** to the category of **[[Def - Topological Space|topological spaces]]** up to weak homotopy equivalence — i.e. to **homotopy types**. The bridge is the **fundamental $\infty$-groupoid** $\Pi_\infty(T)$: objects are points of $T$, $1$-cells are paths, $2$-cells are homotopies of paths, and so on, with all cells invertible because paths can be reversed. The hypothesis says this construction is an equivalence, so a homotopy type *is* a weak $\infty$-groupoid and conversely. It is a *theorem* for those models (Kan complexes, quasi-groupoids) where "weak $\infty$-groupoid" is *defined* simplicially; it remains a *conjecture* for purely algebraic globular definitions (Grothendieck–Maltsiniotis), where it is the benchmark every such definition must meet.

- **[[Thm - Comparison of Models for (∞,1)-Categories]]**
	- The unification theorem. The five standard models of $(\infty,1)$-categories — **[[Def - Quasi-Category|quasi-categories]]**, **[[Def - Segal Category and Complete Segal Space|Segal categories]]**, **[[Def - Segal Category and Complete Segal Space|complete Segal spaces]]**, **simplicial categories** (categories **[[Def - Enriched Category|enriched]]** in **[[Def - Simplicial Set|simplicial sets]]**), and **relative categories** (categories with a marked subcategory of weak equivalences) — each carry a **[[Def - Model Category|model structure]]**, and these model structures are connected by a web of **[[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalences]]**. Consequently they all present the *same* homotopy theory: a single $(\infty,1)$-category, the "$\infty$-category of $\infty$-categories". The practical upshot — the reason the field is not paralysed by its zoo of definitions — is that one may prove a theorem in whichever model is convenient and transport it to the others for free.

> [!tip] Unlocked: Model-Independent ∞-Category Theory and the ∞-Cosmos *(from Higher Algebra)*
> Once the models are known to be equivalent, one wants a theory that never mentions a model. **Riehl–Verity**'s program of **model-independent ∞-category theory** axiomatises the ambient setting as an **∞-cosmos** — a category of "$\infty$-categories" enriched in quasi-categories with enough structure to do formal category theory (adjunctions, limits, the Yoneda lemma) entirely synthetically. The comparison theorem is what licenses this: results proved in an ∞-cosmos hold in *every* model at once.

> [!tip] Unlocked: ∞-Topoi and Derived Algebraic Geometry *(from Higher Algebra / Algebraic Geometry)*
> An **∞-topos** is to $(\infty,1)$-categories what a Grothendieck topos is to ordinary categories — an $(\infty,1)$-category of "$\infty$-sheaves" on an $(\infty,1)$-site, the setting for **derived algebraic geometry** and for the **derived category** of a scheme done correctly. Lurie's foundations build the whole theory on quasi-categories; the comparison theorem guarantees the same ∞-topoi arise from any of the other models.

- **[[Ex - The singular complex is a Kan complex]]** (⭐⭐)
	- Prove $\mathrm{Sing}(T)$ fills every horn by deformation-retracting the topological horn $|\Lambda^n_i|$ onto the solid simplex $|\Delta^n|$ — the geometric fact underpinning the [[Thm - The Homotopy Hypothesis|homotopy hypothesis]] in the simplicial model.

- **[[Ex - Strict omega-groupoids do not model all spaces]]** (⭐⭐⭐)
	- Argue that no strict $\infty$-groupoid has the homotopy type of $S^2$ (its higher Whitehead products cannot be realised strictly), so the [[Thm - The Homotopy Hypothesis|homotopy hypothesis]] *fails* for strict ω-groupoids — the sharpest evidence that weakness is forced.

- **[[Ex - Quillen equivalence detects derived mapping spaces]]** (⭐⭐)
	- Show that a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] induces equivalences of all derived mapping spaces (not just an equivalence of homotopy categories), so it certifies that two models of $(\infty,1)$-categories carry the same homotopy theory. The criterion behind the [[Thm - Comparison of Models for (∞,1)-Categories|comparison theorem]].

> [!note] Exercise Index — §3
> [[Exercise Index - §3 The Comparison Problem and the Homotopy Hypothesis]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The problems in this chapter are not the computational problems of earlier category theory; they are the *structural* problems of a foundational subject still settling its definitions, and they fall into a few recurring goals. The most characteristic is **proving two definitions agree** — that the algebras for one machine are equivalent to the algebras for another, or that two model structures are Quillen equivalent. A second is **verifying that a proposed definition is sane**, which in practice means checking it reproduces known low-dimensional cases (a weak $1$-category is an ordinary category, a weak $2$-category is a **bicategory**) and reproduces homotopy theory in its invertible part (the homotopy hypothesis). A third is **translating a concept across models**: given a notion defined for quasi-categories, find its avatar for complete Segal spaces, and check the equivalence carries one to the other. A fourth is **classifying where a definition sits** on the algebraic/non-algebraic, globular/simplicial grid, and understanding what that placement costs and buys. A fifth, more elementary but constantly needed, is **unwinding a coherence condition** — taking a Segal condition, an inner-horn condition, or a contraction and reading off what it says about composites in concrete terms. These five — agreement, sanity, translation, placement, unwinding — are the targets, and they recur because the central activity of the subject is comparison.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **A model structure is given**, which is the richest source: it hands you weak equivalences (the maps to invert), and a Quillen equivalence between two such structures is the standard certificate that two definitions agree. **A Segal-type condition is given** — a spine inclusion is a weak equivalence — which you immediately read as "composites exist and are homotopy-unique", converting a property into usable composition. **A contraction or operad is given** in the algebraic models, which you read as "chosen composites and coherence cells", the structural counterpart of the Segal condition. **A horn-filling condition is given** (inner horns for $\infty$-categories, all horns for $\infty$-groupoids), which routes through the [[Def - Quasi-Category|quasi-category]] machinery. **An adjunction between simplicial sets, spaces, or categories is given** — geometric realisation and the singular nerve, the nerve and homotopy category, the homotopy-coherent nerve — which is the vehicle for every comparison, since one shows it is a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]]. The recurring move is to route a source to a target: a given pair of model structures plus a candidate adjunction routes through the Quillen-equivalence criterion to an agreement theorem; a Segal condition routes through the Segal-space machinery to homotopy-unique composition; an all-horns condition routes through the homotopy hypothesis to a statement about spaces. The [[Higher Categories — Other Definitions of Weak n-Categories#Problem-Solving Strategy|Problem-Solving Strategy]] section makes these routes explicit.

---

# Legal Operations

These are the moves almost every problem in this chapter is assembled from. When stuck, scan the list and try each one. Everything here is self-contained: a reader who has met simplicial sets and model categories but never the comparison literature should be able to follow each operation from the description alone.

**Legal operations:**

1. **Read a Segal condition as "composition is a property".** Whenever a definition presents a simplicial object $X$ and demands the spine map $X_n \to X_1 \times_{X_0} \cdots \times_{X_0} X_1$ be an equivalence, translate it on sight: an $n$-fold composable string determines, up to a contractible space of choices, a single $n$-simplex, hence a composite. *Trigger:* a fibre product of copies of $X_1$ over $X_0$ appears. *Pattern:* replace "$X_n$" by "homotopy-coherent strings of $n$ composable arrows" and continue reasoning about composites without ever naming one.

2. **Read an inner-horn condition as the simplicial avatar of the Segal condition.** For a [[Def - Simplicial Set|simplicial set]], the [[Def - Quasi-Category|inner-horn filling]] condition plays the role the Segal condition plays for simplicial spaces — both say "composites exist, essentially uniquely". When a problem is posed for quasi-categories but you reason more easily with Segal spaces (or vice versa), this dictionary lets you switch the form of the composition-as-property condition.

3. **Build a contraction to make a definition algebraic.** To turn "composites exist" into "composites are chosen", construct a **contraction**: a system of chosen lifts against parallel pairs, dimension by dimension. In the globular world this is the contraction on a **globular operad**; the Penon monad $H$ encodes the same idea via stretchings. *Trigger:* you need an actual operation, not just its existence — typically to compare with an algebraic definition.

4. **Take algebras for a monad or operad.** Given a monad (like Penon's $H$) or an operad (like a globular operad or Trimble's $E_\infty$), the higher categories *are* its algebras. To produce or recognise a weak higher category, exhibit the algebra structure: an action map satisfying the unit and associativity laws. *Trigger:* the definition is algebraic; the object is "a thing with chosen composites".

5. **Compare two models by exhibiting a Quillen equivalence.** To prove two definitions present the same homotopy theory, equip each with a [[Def - Model Category|model structure]], find an adjoint pair between them, and verify the two conditions of a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] (the left adjoint preserves cofibrations and trivial cofibrations, and the derived unit/counit are weak equivalences). This is the master operation of §3. *Trigger:* "show definition $A$ and definition $B$ agree."

6. **Pass to homotopy categories or to the underlying ∞-category to compare invariants.** Any model of an $(\infty,1)$-category has a **homotopy category** (objects and homotopy classes of morphisms). A [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] induces an equivalence of these, and more refinedly of all derived mapping spaces $\mathrm{Map}(X,Y)$. *Trigger:* you want to certify that an equivalence really does preserve the categorical content, not just the objects.

7. **Build the fundamental ∞-groupoid of a space (or realise a higher groupoid as a space).** The functor $\Pi_\infty$ sends a [[Def - Topological Space|space]] to the higher groupoid of its points, paths, homotopies, …; geometric realisation $|{-}|$ goes back. This adjoint pair is the working form of the [[Thm - The Homotopy Hypothesis|homotopy hypothesis]] and the way every "$\infty$-groupoids = spaces" argument is run. *Trigger:* a problem about invertible-everywhere higher categories.

8. **Truncate to recover a low-dimensional case.** To test a definition, set the top dimension to $1$ or $2$ and check you recover ordinary categories or **bicategories**. For Tamsamani–Simpson, truncate the iterated Segal conditions; for globular operads, truncate the algebra; for complete Segal spaces, take $0$-truncated mapping spaces. *Trigger:* a sanity-check requirement, or a base case in an induction on dimension.

9. **Add a completeness/univalence condition to rigidify equivalences.** A bare Segal space has redundant data — many objects that are equivalent but not equal. Rezk's **completeness** condition (the degeneracy $X_0 \to X^{\mathrm{heq}}_1$ onto the space of self-equivalences is an equivalence) removes the redundancy. *Trigger:* you have a Segal space but want a model whose equivalences are genuinely invertible, so that the homotopy theory is correct.

**Illegal but tempting operations:**

> [!warning] 1. Treating "composition exists" as "composition is chosen"
> Faced with a non-algebraic model — a [[Def - Quasi-Category|quasi-category]] or a Segal space — it is tempting to pick a composite of each pair $f, g$ and reason as if it were *the* composite, as in an ordinary category. This is illegal: the choice is not canonical and not functorial, so a construction that depends on it is not well-defined. The concrete failure is that two different systems of chosen composites need *not* be equal, only homotopic, and a naive argument that "$h \circ g) \circ f = h \circ (g \circ f)$" is comparing two specific fillers that are merely connected by a (non-identity) higher cell. The operation becomes legal exactly when you work up to homotopy throughout, or when you have first built a *coherent* choice — i.e. passed to an algebraic model via a contraction.

> [!warning] 2. Assuming any two definitions of weak $n$-category are equivalent for all $n$
> The comparison theorem of §3 is proved for $(\infty,1)$: one direction of non-invertibility. It is tempting to assume the analogous statement holds for all weak $n$-categories and all definitions, but this is open in general. For $(\infty,n)$ with $n \ge 2$ the comparisons are far harder and were established (Barwick–Schommer-Pries, and others) only much later and under hypotheses; for *fully* algebraic globular definitions of weak ω-category, even the [[Thm - The Homotopy Hypothesis|homotopy hypothesis]] is not a theorem. The repair is to restrict the claim to the case actually proved — $(\infty,1)$, or whatever $n$ and class of definitions a cited theorem covers — and not to extrapolate.

> [!warning] 3. Dropping the completeness condition and still calling equivalences invertible
> A Segal space without Rezk's completeness condition has a defect: its "space of objects" $X_0$ can be smaller than the space of objects-up-to-equivalence, so two equivalent objects may fail to be connected by a path in $X_0$. Treating such a Segal space as a correct model of an $(\infty,1)$-category is illegal: the homotopy theory it presents is *not* the right one — the localisation that inverts equivalences changes it. The standard witness is a Segal space built from a category with a nontrivial isomorphism that is not recorded as a path in $X_0$. The operation becomes legal after **completion** (Rezk's localisation), which forces the path-components of $X_0$ to match the equivalence classes.

> [!warning] 4. Conflating $\infty$-groupoids with $\infty$-categories
> Because both fill horns, it is tempting to slide between Kan complexes ([[Def - Kan Complex and the Nerve|Kan complexes]], all horns fill) and quasi-categories (only inner horns fill). This is illegal whenever non-invertible morphisms matter. Demanding *outer* horn fillers forces every morphism to be invertible — the structure collapses from an $(\infty,1)$-category to an $(\infty,0)$-category, an $\infty$-groupoid, hence by the homotopy hypothesis to a mere space. The concrete failure: the nerve of a poset with a non-invertible arrow is a quasi-category but not a Kan complex. The conditions coincide only when the higher category is in fact a groupoid.

---

# Problem-Solving Strategy

The problems in this chapter are won or lost at the moment you decide which *stance* — algebraic or non-algebraic — and which *model* you will reason in, so begin there. Unlike the computational chapters, almost every problem here is a comparison or a sanity-check, and the right first move is to translate the given data into the most convenient form before doing any work.

If the problem **asks you to show two definitions agree**, you are in a comparison problem, and the instrument is almost always a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]]. The route is fixed: put a [[Def - Model Category|model structure]] on each side (these are supplied by the literature — the Joyal model structure for quasi-categories, the Bergner model structure for simplicial categories, the Rezk model structure for complete Segal spaces, the Reedy/Segal model structure for Segal categories), identify an adjoint pair connecting them (the homotopy-coherent nerve, the realisation, the inclusion-and-completion), and verify the two Quillen-equivalence conditions. The whole difficulty is concentrated in choosing the *right* adjoint pair and in computing its derived unit and counit; the model structures themselves are not yours to invent. When the two definitions are *algebraic* — say Penon versus Batanin–Leinster — the route is different and harder: you compare the *monads* or *operads* directly, typically by showing one factors through the other or that their categories of algebras are equivalent, and there is no model-category shortcut.

If the problem **asks you to verify a definition is sane**, the assumption pattern is that you have a definition parametrised by dimension, and the route is **truncation**. Set the top dimension to $1$ and check you recover ordinary categories; set it to $2$ and check you recover **bicategories** (this is the standard test, and it is genuinely informative — several early definitions failed it). For the invertible case, check the homotopy hypothesis: that the $\infty$-groupoids of the definition reproduce homotopy types. The reason truncation is the right tool is that a higher-categorical definition is only as trustworthy as its agreement with the cases we already understand, and those cases live at low dimension.

If the problem **asks you to translate a concept across models**, the assumption pattern is that you have a notion native to one model and a comparison equivalence to another. The route is to *transport* the notion along the equivalence and then *recognise* its intrinsic form on the other side. For instance, an adjunction of quasi-categories transports across the comparison to an adjunction of complete Segal spaces; a limit in one model is a limit in the other. The key decision is whether to transport the *object* or the *property*: properties (being a limit, being an equivalence) transport automatically because the equivalence preserves the homotopy theory, whereas a specific *construction* may need to be rebuilt natively.

If the problem **concerns the homotopy hypothesis itself** — proving $\infty$-groupoids are spaces, or using that fact — the targets and tools split by which direction you need. To go from a space to a higher groupoid, build $\Pi_\infty$; to go back, realise. The non-obvious content is always *completeness/invertibility*: the reason the hypothesis is a theorem for Kan complexes but a conjecture for algebraic globular ω-groupoids is that the simplicial definition has invertibility built in (all horns fill), whereas the algebraic one must *prove* its weakly-invertible cells assemble into genuine inverses. So when working with the hypothesis, the first question is "is invertibility free here, or must I earn it?".

Finally, a meta-strategy threads through all of the above: **the choice of model is a free variable — choose the one that makes the property manifest, and trust the comparison theorem to carry the conclusion back.** Every structural question in this chapter is the question "are these the same?", and the comparison theorem is the standing licence that, for $(\infty,1)$, the answer is yes — so you may always work where the work is easiest. The reason this is sound rather than reckless is precisely the content of §3: the models are connected by [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalences]], so a homotopy-invariant conclusion proved in any one of them holds in all of them.

---

# Most Reusable Properties

- **[[Thm - Comparison of Models for (∞,1)-Categories|The Comparison Theorem]]**: all standard models of $(\infty,1)$-categories are Quillen equivalent. This is the most-used fact in the modern subject because it is *liberating*: it licenses the universal move "work in whichever model is convenient". Reach for it whenever a construction is awkward in one model — derived mapping spaces are cleanest in complete Segal spaces, the homotopy category is cleanest in quasi-categories, enrichment is cleanest in simplicial categories — and transport the result. Its most powerful disguised use is *meta*: it turns "which definition is correct?" from a foundational crisis into a non-question, because they are all correct and all the same.

- **The Segal condition** (composition as homotopy-unique property): the spine map is a weak equivalence. The reusable move is the translation itself — whenever a simplicial object is constrained so that its higher pieces are determined by its $1$-piece glued over its $0$-piece, you have "composition exists, essentially uniquely" for free, with no operation to define and no associativity to check. Recognise its applicability whenever a definition records *strings of arrows* rather than *chosen composites*; it is the non-algebraic counterpart of "the operad acts".

- **[[Thm - The Homotopy Hypothesis|The Homotopy Hypothesis]]** (∞-groupoids = spaces): the invertible part of higher category theory *is* homotopy theory. Its typical use is as a sanity check and a source of intuition: any phenomenon about $\infty$-groupoids can be pictured as a phenomenon about [[Def - Topological Space|spaces]], so the homotopy [[Def - Group|groups]], the Whitehead tower, and the obstruction theory of spaces all become statements about higher groupoids. It is also a *constraint*: it rules out any definition whose groupoidal part fails to reproduce homotopy types.

- **Contractions and operad-algebra structure** (composition as chosen structure): in the algebraic models, the operad or monad *names* the composites and coherences. The reusable move is "to produce a weak higher category, exhibit the algebra structure; to use one, apply the action map". This is the algebraic counterpart of the Segal condition and is what you reach for whenever you need an actual operation — for comparison with an ordinary algebraic structure, or to feed a higher category into a construction that expects chosen composites.

- **Truncation** (recover the low-dimensional case): set the top dimension to $1$ or $2$. Its typical use is verification and induction — every reasonable definition must give categories at level $1$ and bicategories at level $2$, and many proofs proceed by induction on dimension with truncation supplying the base case. It is the cheapest test of a definition and the first thing to apply to an unfamiliar one.

---

# Bridges

1. **Homotopy theory and the foundations of spaces.** The deepest bridge is the [[Thm - The Homotopy Hypothesis|homotopy hypothesis]]: a [[Def - Topological Space|topological space]], considered up to weak homotopy equivalence, *is* a weak $\infty$-groupoid, namely its fundamental $\infty$-groupoid $\Pi_\infty(T)$ — points, paths, homotopies of paths, and so on, all invertible. This is not an analogy but an equivalence (a theorem in the simplicial models, where $\Pi_\infty(T) = \mathrm{Sing}(T)$, the singular [[Def - Simplicial Set|simplicial set]], which is a [[Def - Kan Complex and the Nerve|Kan complex]]). The practical transfer runs both ways: the century of accumulated technique in homotopy theory — homotopy groups, fibrations, spectral sequences — becomes available for higher groupoids, and conversely the higher-categorical perspective reorganises homotopy theory around the single idea "a space is a groupoid with higher cells".

2. **Model categories as presentations.** A [[Def - Model Category|model category]] is, by the [[Thm - The Homotopy Category of a Model Category|localisation theorem]], a *presentation* of an $(\infty,1)$-category: its objects and weak equivalences, with the cofibration/fibration data discarded, determine an $(\infty,1)$-category whose mapping spaces are the derived $\mathrm{Map}(X,Y)$. The comparison theorem of §3 is itself stated and proved in this language — the five models of $(\infty,1)$-categories are five *model categories*, and "they present the same thing" means they are [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalent]]. So this chapter is where the abstract homotopy theory of the Model Categories chapter pays off: model categories are the engineering, $(\infty,1)$-categories are the invariant content, and the relative category is the bare data interpolating between them.

3. **Algebraic geometry and ∞-topoi.** Ordinary algebraic geometry studies sheaves of sets on a site; **derived** and **higher** algebraic geometry study **$\infty$-sheaves** — sheaves valued in spaces — on an $(\infty,1)$-site, organised into an **∞-topos**. The reason one needs the machinery of this chapter is that the naive **derived category** of a scheme (chain complexes of sheaves up to quasi-isomorphism) loses information that only a stable $(\infty,1)$-category retains; replacing it by the derived $(\infty,1)$-category of coherent sheaves fixes the failures of the triangulated-category formalism (non-functorial cones, no good mapping spaces). The comparison theorem guarantees that whichever model one builds this $(\infty,1)$-category in, the resulting geometry is the same.

4. **Operads, loop spaces, and the recognition principle.** Trimble's definition imports the **little-disks operads** $E_n$ from homotopy theory to control coherence; the same operads govern $n$-fold loop spaces by May's recognition principle, and the contractible spaces of operations in an $E_\infty$-operad are exactly what make "essentially one composite" precise in the operadic models. This bridge explains why higher category theory and the homotopy theory of iterated loop spaces are not two subjects but one: an $E_\infty$-algebra in spaces is a higher categorical structure with a single object and everything invertible, i.e. a (symmetric monoidal) $\infty$-groupoid, and the operadic coherence machinery is shared verbatim.

---

# Insights

**The unifying frame: every definition of a weak higher category is a way of saying "composition is unique up to a contractible space of choices", and they differ only in how they say it.** Strip away the machinery and there is one idea. In an ordinary category the composite of $f$ and $g$ is a single element. In a weak higher category it is not single — it is a contractible *space* of candidates, all equivalent through higher cells. Every definition in the zoo is a different encoding of this one fact. The Segal condition encodes it as "the spine map is an equivalence". The inner-horn condition encodes it as "inner horns fill". A contraction encodes it as "there is a chosen filler, coherently". The Penon monad encodes it as "stretchings act". Once you see that they are all spelling out *contractibility of the space of composites*, the multiplicity of definitions stops being alarming and becomes a menu: pick the encoding that makes your problem easy.

**The true name of the algebraic/non-algebraic distinction is "chosen versus merely-existing", and it is the same distinction as constructive-versus-classical, or skeletal-versus-not.** An algebraic definition gives you a function that *returns* a composite; a non-algebraic one gives you a *guarantee* that a composite exists. The trade is exactly the familiar one between data and property. Data (the algebraic stance) is rigid and easy to manipulate — you can write down the composite and compute with it — but rigidity makes equivalences hard, because a map of algebras must respect the *chosen* composites on the nose-up-to-coherence. Property (the non-algebraic stance) is flexible and makes equivalences easy — any map preserving the diagram automatically respects composition, since composition is not extra data — but you can never point to *the* composite. This is why the non-algebraic models dominate the working theory ($(\infty,1)$-categories à la Joyal–Lurie) while the algebraic models dominate the foundational and type-theoretic side, where having an actual operation matters.

**The homotopy hypothesis is the boundary condition that makes the whole subject well-posed.** A definition of weak ω-category has enormous freedom; what disciplines it is the demand that its *invertible* part reproduce a structure we already trust completely — homotopy types. This is the role the hypothesis plays even when it is unproven: it is the specification, the acceptance test. A proposed definition that gets the groupoidal case wrong is simply wrong, no matter how elegant its machinery, because we *know* what $\infty$-groupoids should be. The reason it is a theorem for simplicial definitions and a conjecture for globular-algebraic ones is itself the key insight: simplicial sets have invertibility *built into the geometry* (the singular complex of a space is a Kan complex automatically), whereas a globular-algebraic definition must *construct* inverses from weak data, and proving those weak inverses cohere into the homotopy type of a space is exactly the hard part.

**A trigger-reaction pattern for the working ∞-categorist: when you see "show $X$ and $Y$ are the same higher category", reach for a Quillen equivalence; when you see "show this definition is reasonable", reach for truncation and the homotopy hypothesis.** These two reflexes cover most of the chapter. The first converts an opaque equivalence-of-definitions question into the concrete checklist of a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] — find the adjoint pair, check it preserves the cofibration structure, check the derived unit and counit are equivalences. The second converts a vague "is this a good definition" into two sharp tests — does it give categories and bicategories under truncation, and does its groupoidal part give spaces. Internalising which reflex a problem calls for is most of the skill, because the machinery is then standard.

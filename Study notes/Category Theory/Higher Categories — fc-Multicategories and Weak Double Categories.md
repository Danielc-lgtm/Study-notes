---
type: topic
subject: higher-categories
chapter: "Leinster Ch.5"
title: "Higher Categories — fc-Multicategories and Weak Double Categories"
tags: [category-theory, higher-categories, foundations]
---

# Notation Registry

This chapter works with structures that have **two directions of arrow** and, in the most general case, $2$-cells whose domain is a *string* of arrows. Keep the four layers straight: objects, vertical $1$-cells (the "maps"), horizontal $1$-cells (the "processes"), and $2$-cells. The recurring meta-convention is that *vertical composition is strict and horizontal composition is weak (or merely potential)* — the asymmetry is deliberate and load-bearing throughout.

- $\mathcal{C}, \mathbb{D}$ — an [[Def - fc-Multicategory|fc-multicategory]] / a [[Def - Weak Double Category|(weak) double category]]
- $A, B, C, A_0, \dots, A_n$ — objects
- $f : A \to A'$ — a **vertical $1$-cell**; vertical composition $\circ$ is strict and associative (the vertical category)
- $m : A \nrightarrow B$ — a **horizontal $1$-cell** (slashed arrow); source $A$, target $B$
- $(m_1, \dots, m_n)$ — a **string** of composable horizontal $1$-cells, $A_0 \xrightarrow{m_1} A_1 \cdots \xrightarrow{m_n} A_n$; allowed length $n = 0$ (empty string at one object)
- $\theta : (m_1, \dots, m_n) \Rightarrow p$ — a **$2$-cell** with a string on top, a single horizontal $1$-cell $p$ on the bottom, and vertical $1$-cells as left/right boundaries
- $\odot$ — horizontal composition of horizontal $1$-cells in a double category, $m \odot m'$; weak (associative up to invertible $2$-cell)
- $a, l, r$ — associator and left/right unitors for $\odot$ (invertible $2$-cells), subject to pentagon and triangle
- $\mathrm{U}_A$ — the horizontal unit $1$-cell at $A$; $1_A$ — the vertical identity
- $\mathrm{fc}$ — the **free-category monad** on the category $\mathbf{Gph}$ of directed graphs; sends a graph to its graph of paths
- $\mathbf{Gph}$ — directed graphs $G_1 \rightrightarrows G_0$ (edges, vertices, source/target); $\eta, \mu$ — unit and multiplication of $\mathrm{fc}$
- $\mathcal{K}$ — a [[Def - 2-Category and Bicategory|bicategory]] in which we take [[Def - Monad Monoid and Module in a Bicategory|monads]]; objects $\mathcal{A}, \mathcal{B}$; $1$-cells, $2$-cells composed by $\circ, \cdot$ (vertical), $\ast$ (horizontal)
- $(t, \mu, \eta)$ — a **monad in $\mathcal{K}$**: endo-$1$-cell $t : \mathcal{A} \to \mathcal{A}$, multiplication $\mu : tt \Rightarrow t$, unit $\eta : 1_{\mathcal{A}} \Rightarrow t$
- $m \otimes_s n$ — tensor of bimodules over a shared monad $s$ (a balanced coequalizer)
- $\mathrm{Mod}(\mathcal{K})$ — the bicategory of monads, bimodules, and module maps in $\mathcal{K}$
- $\mathbf{Span}(\mathbf{Set})$, $\mathbf{Rel}$, $\mathbf{Cat}$ — the bicategories of spans of sets, relations, and categories; monads in these are categories, preorders, and ordinary monads respectively

---

# Motivation

Here is the entire chapter in one sentence: there is a single structure, the **fc-multicategory**, that contains [[Def - Monoidal Category|monoidal categories]], [[Def - 2-Category and Bicategory|bicategories]], double categories, and plain [[Def - Multicategory|multicategories]] as special cases, and it is obtained by a completely uniform recipe — "generalised multicategory for the free-category monad". Everything else in Leinster Chapter 5 is the unpacking of that sentence and the harvest of examples it makes available.

The friction that forces the chapter is this. The standard higher structures all carry a *composition of a string of cells into one cell*: a monoidal category tensors a string of objects, a bicategory composes a string of $1$-cells, a double category composes a string of horizontal $1$-cells. In each case the composition is associative only up to coherent isomorphism, and each subject restates its own pentagon and triangle by hand. The recurring suspicion — that these are one coherence theory, not four — is resolved by *not forcing the composition to happen*. Instead of declaring "the composite of $(m_1, \dots, m_n)$ is such-and-such", record a $2$-cell whose top is the string $(m_1, \dots, m_n)$ and whose bottom is the answer. The string is the thing you have not composed yet; the $2$-cell is the answer; composition of strings is *strict* (concatenation of paths), and all the weakness moves into whether and how the strings are *represented* by genuine composites.

The unifying frame organising the whole chapter is the **four-dial picture**:

$$
\text{fc-multicategory} \;\xrightarrow[\text{one object}]{\text{trivial vertical}}\; \text{multicategory} \;\xrightarrow{\text{representable}}\; \text{monoidal category} \;\xleftarrow{\text{one object}}\; \text{bicategory} \;\xleftarrow{\text{trivial vertical}}\; \text{weak double category}.
$$

Turn the dials — number of objects, vertical structure trivial or not, one-object or many, representable (composites exist) or not — and the fc-multicategory becomes each of the classical structures. This is [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]], and it is the chapter's organising theorem.

The chapter then turns to a second, equally unifying idea: the [[Def - Monad and Comonad|monad]] is not special to categories. A **monad in a bicategory $\mathcal{K}$** is an object with an endo-$1$-cell carrying a multiplication and a unit — the monad axioms transcribed bicategorically. Reading this in different $\mathcal{K}$ produces a remarkable dictionary: a monad in $\mathbf{Cat}$ is an ordinary monad, a monad in $\mathbf{Span}(\mathbf{Set})$ is a small category, a monad in $\mathbf{Rel}$ is a preorder. Their modules and bimodules assemble into a new bicategory $\mathrm{Mod}(\mathcal{K})$ ([[Thm - Monoids and Modules Form a Bicategory]]), which for $\mathbf{Span}(\mathbf{Set})$ is the bicategory of categories and profunctors and for rings is Morita theory. One construction, run on different $\mathcal{K}$, generates the standard calculi of correspondences.

This topic assumes you are fluent with ordinary [[Def - Category|categories]] and [[Def - Functor|functors]], with [[Def - Monoidal Category|monoidal categories]] and their coherence ([[Thm - Mac Lane Coherence Theorem|Mac Lane's theorem]]), with [[Def - 2-Category and Bicategory|bicategories]] and the [[Thm - The Interchange Law|interchange law]], and with the ordinary [[Def - Monad and Comonad|monad]]. It is helpful, though not required, to have met [[Def - Multicategory|multicategories]] and the idea of a [[Def - Generalized Multicategory|generalized multicategory]] for a cartesian monad (the previous chapter); where those pages do not yet exist they are named in bold. Refresh [[Def - Pullback and Pushout|pullbacks]] before §3, since spans compose by pullback.

---

# Concept Map

## §1 fc-Multicategories

- **[[Def - fc-Multicategory]]**
	- An **fc-multicategory** is a [[Def - Generalized Multicategory|generalized multicategory]] for the free-category monad $\mathrm{fc}$ on directed graphs. It has four layers: objects, vertical $1$-cells (forming a strict category), horizontal $1$-cells (with *no* composition imposed), and $2$-cells $\theta : (m_1, \dots, m_n) \Rightarrow p$ whose domain is a *string* of $n$ horizontal $1$-cells and whose codomain is a single one, with vertical $1$-cells closing the sides. Composition is multicategory-style substitution of strings into slots (powered by $\mathrm{fc}$'s path-concatenation), with identity $2$-cells as units. It is the least committal home for "horizontal composition that has not happened yet"; its modern name is *virtual double category*.

- **[[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]]**
	- The four-dial theorem: bicategories are the vertically-trivial *representable* fc-multicategories; monoidal categories are the one-object ones; weak double categories are *all* representable fc-multicategories; plain multicategories are the one-object vertically-trivial ones *without* representability. Each embedding is full and faithful, sending classical composition to string substitution. A single three-line proof that substitution is associative (it is concatenation) yields the pentagon/triangle coherence of all four structures at once, because each classical coherence is the shadow of strict string-associativity through a representability mirror.

- **[[Ex - A multicategory is a one-object fc-multicategory]]** (⭐)
	- Show that an [[Def - fc-Multicategory|fc-multicategory]] with one object and only the identity vertical $1$-cell is exactly an ordinary [[Def - Multicategory|multicategory]], matching string-topped $2$-cells with multimaps and substitution with multicategory composition.

- **[[Ex - A monoidal category as a one-object fc-multicategory]]** (⭐⭐)
	- Verify that a [[Def - Monoidal Category|monoidal category]] $(\mathcal{V}, \otimes, I)$ is the one-object, vertically-trivial, representable fc-multicategory whose horizontal $1$-cells are the objects of $\mathcal{V}$ and whose $2$-cells $(X_1,\dots,X_n)\Rightarrow Y$ are maps $X_1\otimes\cdots\otimes X_n \to Y$; identify the empty string with $I$ and the associator with uniqueness of representing objects.

- **[[Ex - The fc-multicategory of rings bimodules and maps]]** (⭐⭐⭐)
	- Build the four-layer fc-multicategory with [[Def - Ring|rings]] as objects, ring homomorphisms as vertical $1$-cells, bimodules as horizontal $1$-cells, and string-balanced maps $M_1 \otimes \cdots \otimes M_n \to P$ as $2$-cells; check substitution is associative and that this is a genuinely non-trivial (non-one-object, non-vertically-trivial) example.

> [!tip] Unlocked: Virtual double categories and equipments *(from formal category theory)*
> An fc-multicategory is exactly a **virtual double category**; adding companions and conjoints for every vertical $1$-cell makes it a **proarrow equipment**, the setting where Kan extensions and the [[Thm - The Yoneda Lemma|Yoneda lemma]] are developed *formally*, independently of $\mathbf{Set}$. The string-topped $2$-cell is the primitive of this entire "category theory done category-theoretically" program.

> [!tip] Unlocked: Opetopes via the slice construction *(from Leinster Ch.7)*
> Iterating a **slice** on generalized multicategories — of which the fc-multicategory is the running fc-example — produces the **opetopes**, the cell shapes of the Baez–Dolan weak $n$-categories. The string-on-top $2$-cell ("many in, one out") is precisely the $2$-dimensional opetope.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 fc-Multicategories]]

## §2 Weak Double Categories

- **[[Def - Weak Double Category]]**
	- A **weak (pseudo) double category** has objects, vertical $1$-cells (strict category), horizontal $1$-cells with a composition $\odot$, and $2$-cells that are squares (one horizontal $1$-cell top and bottom). The two compositions satisfy the **interchange law**, and $\odot$ is associative and unital only up to coherent invertible $2$-cells (associator, unitors, pentagon, triangle) — weakness allocated to the horizontal direction because that is where constructions like tensor of bimodules live. Equivalently: a pseudocategory internal to $\mathbf{Cat}$, or a *representable* [[Def - fc-Multicategory|fc-multicategory]] (every string has a universal composite). Canonical example: rings, homomorphisms, bimodules, with $\odot = \otimes_R$.

- **[[Ex - The double category of rings and bimodules is weak not strict]]** (⭐⭐)
	- Show that rings/homomorphisms/bimodules/equivariant-maps form a *weak* double category with $\odot = \otimes_R$, and exhibit explicitly that the associator $(M\otimes_S N)\otimes_T P \cong M\otimes_S(N\otimes_T P)$ is a non-identity isomorphism, so the structure cannot be made strict.

- **[[Ex - The double category of spans]]** (⭐⭐)
	- Construct the weak double category $\mathbb{S}\mathrm{pan}(\mathcal{E})$ of objects, maps, spans, and span-maps in a category $\mathcal{E}$ with [[Def - Pullback and Pushout|pullbacks]], with horizontal composition by pullback; verify interchange and that weakness comes from pullback associating only up to canonical iso.

- **[[Ex - A bicategory is a one-object weak double category]]** (⭐⭐)
	- Prove that a weak double category with only identity vertical $1$-cells is exactly a [[Def - 2-Category and Bicategory|bicategory]], and trace how the double category's associator/unitors become the bicategory's; deduce that a monoidal category is a one-object such double category.

- **[[Ex - Representable fc-multicategories are weak double categories]]** (⭐⭐⭐)
	- Show that an [[Def - fc-Multicategory|fc-multicategory]] in which every string of horizontal $1$-cells has a universal (representing) composite is exactly a weak double category, with the universal composites supplying $\odot$ and the uniqueness of representing objects supplying the coherent associator and unitors.

> [!tip] Unlocked: Proarrow equipments and formal adjunctions *(from formal category theory)*
> A weak double category with companions and conjoints is an **equipment**; in it one can state and prove the existence of pointwise Kan extensions, adjunctions, and the formal [[Thm - The Yoneda Lemma|Yoneda lemma]] purely structurally. This is the framework underlying enriched and internal category theory in a single stroke.

> [!tip] Unlocked: Cobordism double categories and extended TQFT *(from mathematical physics)*
> Manifolds, smooth maps, and cobordisms form a symmetric monoidal double category; an **extended TQFT** is a structure-preserving functor out of it, with the vertical direction recording boundary restrictions and the horizontal direction the cobordisms. The double-category packaging is what makes the "extended" (higher-codimension) theory expressible.

> [!note] Exercise Index — §2
> [[Exercise Index - §2 Weak Double Categories]]

## §3 Monads, Monoids, and Modules in a Bicategory

- **[[Def - Monad Monoid and Module in a Bicategory]]**
	- A **monad in a bicategory $\mathcal{K}$** is an object $\mathcal{A}$ with an endo-$1$-cell $t$, a multiplication $\mu : tt \Rightarrow t$, and a unit $\eta : 1_{\mathcal{A}} \Rightarrow t$ obeying the [[Def - Monad and Comonad|monad axioms]] — equivalently a [[Def - Monoid in a Monoidal Category|monoid]] in the endo-hom-monoidal-category $\mathcal{K}(\mathcal{A},\mathcal{A})$, equivalently a lax functor $\mathbf{1}\to\mathcal{K}$. In $\mathbf{Cat}$ it is an ordinary monad; in $\mathbf{Span}(\mathbf{Set})$ a small [[Def - Category|category]]; in $\mathbf{Rel}$ a preorder. Modules and bimodules transcribe the algebraic notions; bimodules compose by tensoring over the shared monad. This page also defines the bicategory $\mathrm{Mod}(\mathcal{K})$.

- **[[Thm - Monoids and Modules Form a Bicategory]]**
	- For a *suitable* bicategory $\mathcal{K}$ (local reflexive coequalizers preserved by composition), monads, bimodules, and module maps form a bicategory $\mathrm{Mod}(\mathcal{K})$: composition is tensor over the middle monad, identities are monads-as-self-bimodules, and the associator/unitors come from universal properties of the balancing coequalizers. For $\mathcal{K}=\mathbf{Span}(\mathbf{Set})$ this is the bicategory of categories and **profunctors**; for rings it is Morita theory. The associativity is "$\otimes_R$ is associative" written without the word ring.

- **[[Ex - A monad in Span Set is a small category]]** (⭐⭐)
	- Unwind the definition of a [[Def - Monad Monoid and Module in a Bicategory|monad]] in $\mathbf{Span}(\mathbf{Set})$ to show its data are exactly a set of objects, a set of arrows with domain/codomain, a composition (from the [[Def - Pullback and Pushout|pullback]] of composable pairs), and identities — i.e. a small [[Def - Category|category]].

- **[[Ex - A monad in Rel is a preorder]]** (⭐)
	- Show that a [[Def - Monad Monoid and Module in a Bicategory|monad]] in the bicategory $\mathbf{Rel}$ of relations is a reflexive transitive relation, i.e. a preorder, and explain why the monad axioms are automatic (the hom-posets are thin).

- **[[Ex - A monad in Cat recovers the ordinary monad]]** (⭐)
	- Verify that a [[Def - Monad Monoid and Module in a Bicategory|monad]] in $\mathbf{Cat}$ is precisely an ordinary [[Def - Monad and Comonad|monad]] $(T,\mu,\eta)$ on a category, the consistency check licensing the bicategorical generalisation.

- **[[Ex - Bimodules over rings and the tensor as composition]]** (⭐⭐⭐)
	- Show that in $\mathrm{Mod}(\mathcal{K})$ for the one-object ring bicategory, $1$-cells are bimodules and composition is $\otimes_R$, and prove the associativity isomorphism is the canonical balanced-coequalizer iso; relate to Morita equivalence as equivalence in $\mathrm{Mod}(\mathcal{K})$.

> [!tip] Unlocked: The formal theory of monads *(from 2-category theory)*
> Because the monad axioms are bicategorical, **Eilenberg–Moore and Kleisli objects** make sense for a monad in any $2$-category, recovering [[Def - Monad and Comonad|algebras and the Kleisli category]] when $\mathcal{K}=\mathbf{Cat}$. Street's formal theory of monads is the abstract backbone making monadicity transfer to enriched and internal settings.

> [!tip] Unlocked: Profunctors, weighted limits, and Morita theory *(from category theory and algebra)*
> The bicategory $\mathrm{Mod}(\mathbf{Span}(\mathbf{Set}))$ of categories and **profunctors** is where **weighted limits**, **Kan extensions**, and **Cauchy completion** are defined; the same construction on rings gives **Morita theory** (equivalence of objects in $\mathrm{Mod}(\mathcal{K})$). Forward to higher algebra: replacing $\mathcal{K}$ by an $\infty$-analogue yields **algebras and bimodules** with derived **Tor**/**Ext**.

> [!note] Exercise Index — §3
> [[Exercise Index - §3 Monads, Monoids, and Modules in a Bicategory]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises of this chapter chase a small set of recurring goals. The most common is an **identification**: "this familiar structure *is* an fc-multicategory / weak double category / monad in $\mathcal{K}$ of such-and-such a kind". The whole pedagogical point of the chapter is that monoidal categories, bicategories, double categories, multicategories, ordinary categories, monads, and preorders are all instances of two or three templates, so most problems ask you to *match a concrete structure to its template* and to set the dials (one object? trivial vertical structure? representable?). A second target is a **coherence-for-free** claim: showing that some classical coherence (associativity of $\otimes$, the pentagon, associativity of profunctor or bimodule composition) follows from the strict associativity of string concatenation or from the universal property of a coequalizer, rather than from a hand-checked diagram. A third is an **existence-of-composites** claim: proving that strings have universal composites (representability) so that an fc-multicategory upgrades to a weak double category, or that the local colimits exist so that $\mathrm{Mod}(\mathcal{K})$ is a genuine bicategory. A fourth is a **dictionary translation**: "what does this notion become when I read it in $\mathbf{Span}(\mathbf{Set})$ / $\mathbf{Rel}$ / $\mathbf{Cat}$?" These four — identify the template, get coherence for free, establish representability, translate via the dictionary — are the targets, and they recur because the chapter's content *is* the claim that one structure refracts into many.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **A cartesian monad $T$ is given** (here $T = \mathrm{fc}$), and its being cartesian is the licence to form $T$-spans and hence generalized multicategories. **A bicategory $\mathcal{K}$ is given**, and the first move is always to identify its objects, $1$-cells, $2$-cells, and composition, because a monad in $\mathcal{K}$ is just an endo-$1$-cell with structure and everything follows from knowing $\mathcal{K}$ concretely. **Local colimits are given or assumed** (reflexive coequalizers preserved by composition), which is the exact hypothesis that lets bimodule tensors exist and associate — when they are absent, the structure stays virtual (an fc-multicategory) and you must reason with strings instead of composites. **Universal properties are available**: representing $2$-cells and balancing coequalizers are unique up to unique iso, and this uniqueness is the source of every associator and unitor in the chapter. The recurring move is to route a source to a target: a cartesian monad routes to "this is a generalized multicategory"; a concretely-known $\mathcal{K}$ routes to "a monad here is *that* familiar structure"; local colimits route to "the tensor exists, so $\mathrm{Mod}(\mathcal{K})$ is a bicategory and composition associates". The [[Higher Categories — fc-Multicategories and Weak Double Categories#Problem-Solving Strategy|Problem-Solving Strategy]] makes these routes explicit.

---

# Legal Operations

These are the moves nearly every problem in this chapter is assembled from. When stuck, scan the list. Everything is self-contained.

**Legal operations:**

1. **Set the four dials to identify a structure.** Given a concrete structure, ask: how many objects? is the vertical structure trivial (only identity vertical $1$-cells)? is it representable (do strings have universal composites)? The answers locate it in the four-dial picture of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]]. *Trigger:* "show that X is a [bicategory / monoidal category / multicategory / double category]". *Pattern:* match X's cells to the fc-multicategory layers, then read off the dials.

2. **Replace a chosen composite by a universal $2$-cell out of a string.** Whenever a structure *gives* you a composite (a tensor $X\otimes Y$, a $1$-cell composite $g\circ f$, a horizontal composite $m\odot m'$), re-encode it as: "this composite, with its canonical map, is the universal $2$-cell out of the string". This converts "composition is given" into "the string is representable". *Trigger:* a tensor or composite appears and you want to feed it into the fc-multicategory machinery.

3. **Use uniqueness of representing objects to manufacture an associator.** Two bracketings of a string represent the *same* string, hence are canonically isomorphic; that iso is the associator, and the pentagon is automatic. *Trigger:* you must produce or check an associativity isomorphism without a hand computation. *Pattern:* "both sides represent the string $(X,Y,Z)$, so there is a unique iso between them".

4. **Transcribe a monad/module notion into a bicategory.** Take a definition stated for $\mathbf{Cat}$ (monad, algebra, module, Kleisli) and rewrite it with "$1$-cell" for "endofunctor" and "$2$-cell" for "natural transformation"; it now makes sense in any [[Def - 2-Category and Bicategory|bicategory]] $\mathcal{K}$. *Trigger:* you want a monad/module in $\mathbf{Span}(\mathbf{Set})$, $\mathbf{Rel}$, or an enrichment base. *Pattern:* "an endo-$1$-cell $t$ with $\mu : tt\Rightarrow t$ and $\eta : 1\Rightarrow t$".

5. **Read a monad in $\mathcal{K}$ via the concrete description of $\mathcal{K}$.** Once $\mathcal{K}$'s objects, $1$-cells, $2$-cells, and composition are spelled out, a monad is forced data: write down what $t$, $\mu$, $\eta$ *are* concretely and recognise the result. *Trigger:* "what is a monad in $\mathcal{K}$?" *Pattern:* in $\mathbf{Span}(\mathbf{Set})$ the pullback is composable pairs, so $\mu$ is composition; in $\mathbf{Rel}$ $2$-cells are inclusions, so $\mu, \eta$ are transitivity and reflexivity.

6. **Form the balanced tensor of bimodules as a reflexive coequalizer.** To compose $1$-cells in $\mathrm{Mod}(\mathcal{K})$, coequalize the two adjacent actions $m\,s\,n \rightrightarrows m\,n$. *Trigger:* you need horizontal composition of bimodules/profunctors. *Pattern:* "$m\otimes_s n = \mathrm{coeq}(\rho_m\ast 1,\, 1\ast\lambda_n)$", existing when $\mathcal{K}$ has local reflexive coequalizers.

7. **Push structure through a coequalizer by preservation.** When composition preserves the balancing coequalizer, outer actions, associativity isomorphisms, and coherence all descend uniquely to the tensor. *Trigger:* you have defined a tensor and must equip it with further structure. *Pattern:* "the functor preserves the coequalizer, so the map factors uniquely".

8. **Use the empty string ($n=0$) for units.** The length-zero string supplies the monoidal unit, the horizontal unit $\mathrm{U}_A$, or the identity $1$-cell; never forget it. *Trigger:* unit objects/laws are involved. *Pattern:* "the empty-string composite is $I$ / $\mathrm{U}_A$ / the identity bimodule $t$".

9. **Specialise a general theorem by turning a dial.** Prove the general bicategory case, then deduce the monoidal case by restricting to one object, and the multicategory case by dropping representability. *Trigger:* a result is wanted for monoidal categories but easiest for bicategories. *Pattern:* "delooping: one-object bicategory $=$ monoidal category".

**Illegal but tempting operations:**

> [!warning] 1. Treating an fc-multicategory's $2$-cells as if their top were a single horizontal $1$-cell
> It is tempting to think of $2$-cells as squares, as in a double category. But an [[Def - fc-Multicategory|fc-multicategory]] $2$-cell has a *string* on top, of any length $n\geq 0$. If you only use length-one tops you are working in a [[Def - Weak Double Category|double category]], not an fc-multicategory, and you lose exactly the substitution-of-strings law. Concretely, the multicategory of vector spaces with multilinear maps has genuinely $n$-ary $2$-cells ($V_1\times\cdots\times V_n\to W$); restricting to $n=1$ throws away every multilinear map. The repair is to keep all string lengths and use $\mathrm{fc}$'s concatenation as the composition.

> [!warning] 2. Assuming bimodule tensor (hence $\mathrm{Mod}(\mathcal{K})$) exists in any bicategory
> The construction $m\otimes_s n$ is a *coequalizer*; it does not exist unless $\mathcal{K}$ has local reflexive coequalizers preserved by composition. In a bicategory without these colimits — e.g. a bicategory of "small" spans where the needed colimits are too big — $\mathrm{Mod}(\mathcal{K})$ is **not** a bicategory. The standard symptom is that $\otimes_s$ is not associative because composition fails to preserve the coequalizers. The repair is to work *virtually*: monads, bimodules, and module maps always form an [[Def - fc-Multicategory|fc-multicategory]] (no colimits needed), and $\mathrm{Mod}(\mathcal{K})$ is its representable shadow when the colimits do exist.

> [!warning] 3. Declaring a double category strict because it "looks like" composition is on the nose
> The bimodule double category tempts you to set $(M\otimes_S N)\otimes_T P = M\otimes_S(N\otimes_T P)$. This equality is **false** — the two are canonically *isomorphic*, not identical — so the strict double category of rings and bimodules does not exist. The witness: take a field and small bimodules and watch the underlying sets differ as built. The repair is weakening: introduce the associator as an invertible $2$-cell and impose the pentagon, i.e. work in a [[Def - Weak Double Category|weak]] double category.

> [!warning] 4. Confusing a monad in $\mathcal{K}$ with a comonad
> A monad in $\mathcal{K}$ has $\mu : tt\Rightarrow t$ and $\eta : 1\Rightarrow t$ — the arrows point *into* $t$. A comonad has $\delta : t\Rightarrow tt$ and $\varepsilon : t\Rightarrow 1$, pointing the other way. A comonad in $\mathcal{K}$ is a monad in $\mathcal{K}^{co}$ (the bicategory with $2$-cells reversed), not in $\mathcal{K}$. In $\mathbf{Span}(\mathbf{Set})$ a monad is a category, but a *comonad* is a cocategory — a different beast. The repair: track the direction of $\mu$; never write $t\Rightarrow tt$ and call it a monad.

---

# Problem-Solving Strategy

The problems in this chapter are won at the moment you decide *which template* the structure in front of you instantiates, so begin there, and let the four-dial picture of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]] be your decision tree.

If the problem **hands you a concrete higher structure and asks you to recognise it** — "show that vector spaces with multilinear maps form a multicategory", "show that rings and bimodules form a weak double category" — then your task is to fit the data to the [[Def - fc-Multicategory|fc-multicategory]] layers and set the dials. Identify the objects, the vertical $1$-cells (the honest maps, which compose strictly), the horizontal $1$-cells (the processes), and the $2$-cells. Then ask the three diagnostic questions in order: *one object?* (collapses you toward monoidal/multicategory), *vertical structure trivial?* (collapses toward bicategory/multicategory), *representable?* (composites exist, upgrading to double category / monoidal / bicategory). The single most common mistake is to mishandle the $2$-cells: remember their top is a *string*, and in a representable structure the string's universal composite is the classical composite. Once the dials are set, the recognition is essentially complete and any remaining work is checking substitution-associativity, which is concatenation and so almost free.

If the problem **asks what a monad becomes in a particular bicategory** — "a monad in $\mathbf{Span}(\mathbf{Set})$ is a category", "a monad in $\mathbf{Rel}$ is a preorder" — the route is mechanical once you spell out $\mathcal{K}$ concretely. Write down: an object of $\mathcal{K}$ (the carrier $\mathcal{A}$), an endo-$1$-cell $t : \mathcal{A}\to\mathcal{A}$ (the new "thing"), the multiplication $\mu : tt\Rightarrow t$, and the unit $\eta : 1\Rightarrow t$; then *interpret each in $\mathcal{K}$'s concrete terms*. The decisive observation is usually about composition of $1$-cells in $\mathcal{K}$: in $\mathbf{Span}(\mathbf{Set})$ the composite $tt$ is the [[Def - Pullback and Pushout|pullback]] of composable pairs, so $\mu$ is *composition of arrows* and $\eta$ picks identities, giving a [[Def - Category|category]]; in $\mathbf{Rel}$, hom-sets are posets so $2$-cells are inclusions, making $\mu, \eta$ the transitivity and reflexivity *inequalities*, giving a preorder. The lesson generalises: the nature of $2$-cells in $\mathcal{K}$ (extra data versus mere property) decides whether monad structure is data or a property.

If the problem **asks you to establish a coherence or associativity statement**, resist the urge to compute the pentagon by hand. Two strategies dominate. When composites are *representable*, invoke uniqueness of representing objects (legal operation 3): two bracketings represent the same string, so the canonical iso between them is the associator and the pentagon holds by uniqueness. When composites are *coequalizers* (bimodule or profunctor tensor), invoke the universal property: both bracketings are the same iterated balanced coequalizer (legal operation 7), so they are canonically isomorphic and the coherence diagrams commute because every edge is the unique induced map. In both cases the associativity is *inherited* from a strict associativity one level down — concatenation of strings, or composition in $\mathcal{K}$ — never proved by brute force.

If the problem **concerns whether a construction exists at all** — "is $\mathrm{Mod}(\mathcal{K})$ a bicategory?", "is this fc-multicategory representable?" — the question is really about *colimits*. The bimodule tensor exists exactly when $\mathcal{K}$ has local reflexive coequalizers, and it associates exactly when composition preserves them; the universal composite of a string exists exactly when there is a universal $2$-cell out of the string. So the strategy is to locate the relevant colimit, check it exists, and check it is preserved by the relevant composition. When the colimit is missing, do not force it — retreat to the *virtual* structure (the fc-multicategory) which needs no colimits, and reason with strings.

A meta-strategy threads through all of the above: **when a composition is awkward or absent, do not compute it — represent it.** Replace "the composite is $X$" by "the string is representable by $X$", and replace "associativity holds" by "the bracketings represent the same string / the same coequalizer". This single move converts every coherence question in the chapter into a uniqueness-of-universal-objects question, which is always one line. The reason it is always worth trying is that it cannot lose information: if the composite exists, representability recovers it; if it does not, representability is exactly the virtual structure you should be using instead.

---

# Most Reusable Properties

- **[[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories|The four-dial subsumption]]**: monoidal categories, bicategories, double categories, and multicategories are fc-multicategories with the dials (objects, vertical-triviality, representability) set. This is the most-used fact in the chapter because it is *free orientation*: the instant you meet a higher structure, you locate it among the others and import their theory. Its most powerful disguised use is coherence transfer — proving one coherence statement at the fc-multicategory level (string-associativity) discharges the pentagon/triangle for all four classical structures simultaneously. Reach for it whenever you must show something "is a [bicategory/monoidal category/...]" or whenever a coherence diagram needs checking.

- **[[Def - fc-Multicategory|Representability as the upgrade operator]]**: an fc-multicategory becomes a weak double category exactly by demanding that every string have a universal composite, and the universal composites *carry their own coherence*. The reusable move is to treat "composition exists" not as given structure but as a representability property, so that associators and unitors are produced by uniqueness of representing objects rather than postulated. Typical use: whenever you would otherwise hand-build coherence data, build a universal $2$-cell instead and let uniqueness do the work.

- **[[Def - Monad Monoid and Module in a Bicategory|Monad-in-a-bicategory as a template]]**: "object with associative unital multiplication on an endo-$1$-cell" is one definition that becomes monoid ($\mathbf{Set}$), monad ($\mathbf{Cat}$), category ($\mathbf{Span}(\mathbf{Set})$), preorder ($\mathbf{Rel}$). The reusable property is the *dictionary*: to understand a structure, find the bicategory in which it is a monad. Typical use: reduce questions about categories to questions about monads (and hence about endo-$1$-cells), unifying their proofs with monad theory.

- **[[Thm - Monoids and Modules Form a Bicategory|The Mod(𝒦) factory]]**: monads, bimodules, and module maps in a suitable $\mathcal{K}$ form a bicategory, with composition by balanced tensor. The reusable property is that this *generates* the standard correspondence calculi — profunctors (from $\mathbf{Span}(\mathbf{Set})$), Morita theory (from rings), enriched profunctors (from $\mathcal{V}\text{-}\mathbf{Mat}$) — so a single construction supplies the morphism-bicategory you need. Typical use: when you want "the bicategory whose morphisms are correspondences", build it as $\mathrm{Mod}(\mathcal{K})$ and inherit its associativity from the coequalizer universal property.

- **[[Def - Pullback and Pushout|Balancing coequalizers and pullbacks]]**: the two colimits that power the chapter — pullback (composition in $\mathbf{Span}(\mathbf{Set})$, hence category-composition) and reflexive coequalizer (bimodule/profunctor tensor). The reusable property is that these colimits' *universal properties* are the source of every associativity isomorphism here. Typical use: whenever a composition in this chapter must associate, present it as one of these colimits and read associativity off the universal property.

---

# Bridges

1. **Algebra — Morita theory and the bicategory of rings and bimodules.** A [[Def - Ring|ring]] is a [[Def - Monoid in a Monoidal Category|monoid]] in $\mathbf{Ab}$, hence a [[Def - Monad Monoid and Module in a Bicategory|monad]] in the one-object bicategory whose $1$-cells are abelian groups; its modules and bimodules are the usual ones, and the balanced tensor is $\otimes_R$. The theorem [[Thm - Monoids and Modules Form a Bicategory]] then says rings, bimodules, and bimodule maps form a bicategory, and *Morita equivalence* of rings is exactly equivalence of objects in it — there exist bimodules ${}_S P_R, {}_R Q_S$ with $P\otimes_R Q\cong S$ and $Q\otimes_S P\cong R$, which unwinds to the classical progenerator criterion. The abstract chapter literally contains classical Morita theory as the ring instance.

2. **Category theory itself — profunctors as the morphisms between categories.** Identifying small [[Def - Category|categories]] with monads in $\mathbf{Span}(\mathbf{Set})$ turns the morphisms of $\mathrm{Mod}(\mathbf{Span}(\mathbf{Set}))$ into **profunctors** $C^{op}\times D\to\mathbf{Set}$, composed by coend. In this bicategory the hom-profunctor $C(-,-)$ is the identity $1$-cell, and the [[Thm - The Yoneda Lemma|Yoneda lemma]] becomes the unit law $C(-,-)\otimes_C P\cong P$. Weighted limits, Kan extensions, and Cauchy completion are then formal constructions in this bicategory, which is why "category theory done with profunctors" is so uniform: it is the $\mathrm{Mod}$ of spans.

3. **Enriched category theory — $\mathcal{V}$-categories as monads in $\mathcal{V}\text{-}\mathbf{Mat}$.** For a [[Def - Monoidal Category|monoidal category]] $\mathcal{V}$, the bicategory $\mathcal{V}\text{-}\mathbf{Mat}$ has sets as objects and matrices of $\mathcal{V}$-objects as $1$-cells, composed by "matrix multiplication" using $\otimes$ and coproducts. A monad here is exactly a [[Def - Enriched Category|𝒱-enriched category]] (the matrix is the hom-objects, $\mu$ is enriched composition, $\eta$ the identities), and $\mathrm{Mod}(\mathcal{V}\text{-}\mathbf{Mat})$ is the bicategory of $\mathcal{V}$-categories and $\mathcal{V}$-profunctors. So enriched category theory is the same construction with the base bicategory changed — one proof, many enrichments.

4. **Higher and derived algebra — algebras and bimodules.** Replacing the bicategory $\mathcal{K}$ by a homotopical or $\infty$-categorical analogue turns $\mathrm{Mod}(\mathcal{K})$ into the bicategory (or $(\infty,2)$-category) of **algebras and bimodules**: associative ($E_1$) algebras as objects, bimodules as $1$-cells, with the balanced tensor computing the derived tensor and hence **Tor** in its homotopy groups. The colimit hypotheses ("local reflexive coequalizers preserved by composition") become "geometric realisations of bar constructions exist", and Morita theory becomes derived Morita theory. The classical theorem of this chapter is the truncated shadow of that machinery.

---

# Insights

**The unifying frame: there is one structure, and the classical ones are dial settings.** It is tempting to treat monoidal categories, bicategories, double categories, and multicategories as four separate subjects, each with its own coherence axioms. The chapter's central insight is that they are *one* structure — the [[Def - fc-Multicategory|fc-multicategory]] — with three dials: how many objects, whether the vertical structure is trivial, and whether strings have composites. Every coherence theorem you have ever seen for these structures is the image, under a full embedding, of the single fact that *string concatenation is strictly associative*. When you internalise this, you stop re-proving pentagons: you prove things once at the fc-multicategory level and read off the consequences. The deeper reason the four structures kept looking alike is that they *are* alike — they differ only in dial settings, not in kind.

**The true name of "weak composition" is "representable but not strict".** The word "weak" in weak double category, bicategory, and monoidal category sounds like a defect — composition that fails to associate on the nose. The operational reframing is that weakness is *representability without strictness*: the composite of a string exists as a universal object, but choosing it among isomorphic candidates is not canonical, so re-bracketing changes the chosen representative by a canonical iso. That canonical iso *is* the associator; the pentagon is the uniqueness of representing objects. So "weak" is not a failure but a feature — it is what you get when composites are universal objects rather than literal operations, and the entire coherence apparatus is just the bookkeeping of "universal objects are unique up to unique iso". This is why the fc-multicategory, which records strings without composing them, is the *cleanest* of the structures: it has no weakness at all, only potential composites.

**A trigger-reaction pattern: "monad in a bicategory" should trigger "name the bicategory".** Whenever you read "monad in $\mathcal{K}$", do not reach for the three commuting diagrams. Reach instead for the question *what is $\mathcal{K}$ concretely?*, because the answer determines what the monad *is*: $\mathbf{Cat}$ gives ordinary monads, $\mathbf{Span}(\mathbf{Set})$ gives categories, $\mathbf{Rel}$ gives preorders, $\mathcal{V}\text{-}\mathbf{Mat}$ gives enriched categories. The reaction "name the bicategory, then interpret $t, \mu, \eta$ in its concrete terms" turns every monad-in-a-bicategory problem into a routine unwinding. The dual pattern is just as useful: when you meet a structure with an associative composition (a category, a preorder, an enriched category), ask *in which bicategory is this a monad?* — and inherit monad theory for it for free.

**Inheritance: associativity always comes from one level down.** Every associativity isomorphism in this chapter is borrowed, never built. The associator of a representable fc-multicategory is borrowed from the strict associativity of string concatenation. The associator of $\mathrm{Mod}(\mathcal{K})$ is borrowed from the universal property of coequalizers, which is itself borrowed from associativity of composition in $\mathcal{K}$. Composition of categories-as-monads in $\mathbf{Span}(\mathbf{Set})$ is borrowed from the associativity of [[Def - Pullback and Pushout|pullback]]. The habit to form is: when asked to prove associativity, do not compute — find the strict associativity one level down and the universal property that transports it up. This inheritance principle is what makes the chapter's coherence proofs short, and it is the same principle that makes completeness of $L^p$ borrow from completeness of $\mathbb{R}$, or compactness of a product borrow from compactness of the factors: the property lives in a simpler object and is pulled up by a universal construction.

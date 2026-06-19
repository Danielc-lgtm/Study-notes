---
type: topic
subject: model-categories
chapter: "M.1-M.4"
title: "Model Categories — Quillen's Axiomatization of Homotopy Theory"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation Registry

Throughout this chapter $\mathcal{M}, \mathcal{N}$ denote model categories, and $\mathcal{C}, \mathcal{D}$ ordinary categories. A model category is **bicomplete** (it has all small limits and colimits), so the symbols $\varnothing$ for the **initial object** and $*$ for the **terminal object** always make sense. We follow the classical Quillen axioms MC1–MC5 as the primary formulation, noting Hovey's functorial-factorization refinement where it matters.

- $\mathcal{M}, \mathcal{N}$ — model categories; $\mathcal{C}, \mathcal{D}$ — ordinary categories
- $\mathcal{W}$ — the class of **weak equivalences**; written $\xrightarrow{\sim}$
- $\mathrm{cof}$, $\mathrm{fib}$ — the classes of **cofibrations** (written $\rightarrowtail$) and **fibrations** (written $\twoheadrightarrow$)
- a **trivial** (or **acyclic**) cofibration / fibration — one that is also a weak equivalence; written $\xrightarrow{\sim}\rightarrowtail$ and $\xrightarrow{\sim}\twoheadrightarrow$
- $f, g, h, i, p, q$ — morphisms; $i$ usually a cofibration, $p$ usually a fibration
- $\varnothing$ — initial object; $*$ — terminal object
- $X$ **cofibrant** if $\varnothing \to X$ is a cofibration; **fibrant** if $X \to *$ is a fibration; **bifibrant** if both
- $QX$ — cofibrant replacement of $X$ (with trivial fibration $QX \xrightarrow{\sim} X$); $RX$ — fibrant replacement (with trivial cofibration $X \xrightarrow{\sim} RX$)
- $A \sqcup B$ — coproduct; $A \sqcup A \xrightarrow{\nabla} A$ — the **fold map** (identity on each summand)
- $\mathrm{Cyl}(A)$ — a cylinder object for $A$; $\mathrm{Path}(B)$ — a path object for $B$
- $f \simeq_\ell g$, $f \simeq_r g$, $f \simeq g$ — left, right, and (two-sided) homotopic maps
- $\pi(A,B)$ — the set of homotopy classes of maps $A \to B$
- $\mathrm{Ho}(\mathcal{M}) = \mathcal{M}[\mathcal{W}^{-1}]$ — the **homotopy category** (localization of $\mathcal{M}$ at $\mathcal{W}$)
- $F \dashv U$ — an adjunction with $F$ left adjoint, $U$ right adjoint; $\eta$ unit, $\varepsilon$ counit
- $\mathbf{L}F$, $\mathbf{R}U$ — total left and right **derived functors**
- $\mathbf{Top}$ — topological spaces; $\mathbf{sSet}$ — simplicial sets; $\mathbf{Ch}(R)$ — chain complexes of $R$-modules; $D(R)$ — the derived category of $R$
- $\pi_n(X)$ — the $n$-th homotopy group; $|{-}| \dashv \mathrm{Sing}$ — geometric realization adjoint to the singular nerve

---

# Motivation

Here is the entire chapter in one sentence: **a model category is a category in which you can do homotopy theory, packaged as five axioms.** The phrase "do homotopy theory" sounds vague, so let us make it sharp. In topology you do not really care whether two spaces are equal, or even homeomorphic; you care whether they are the same *up to continuous deformation*. The maps you want to treat as invertible are the **weak homotopy equivalences** — maps inducing isomorphisms on all homotopy groups — even though they are very far from being actual isomorphisms. In homological algebra the analogous wish is to treat **quasi-isomorphisms** of chain complexes (maps inducing isomorphisms on homology) as if they were invertible. In both cases there is a class $\mathcal{W}$ of maps we have decided to declare "equivalences," and the whole subject is the study of the category we get after forcing every map in $\mathcal{W}$ to become an isomorphism.

That operation has a name: **localization**. Given a category $\mathcal{C}$ and a class $\mathcal{W}$, the localization $\mathcal{C}[\mathcal{W}^{-1}]$ is the universal category receiving a functor from $\mathcal{C}$ that sends every map of $\mathcal{W}$ to an isomorphism. The trouble is that the naive construction — formally adjoin inverses and take zig-zags of maps — is a disaster. The morphisms between two objects can fail to form a *set* (you hit set-theoretic size problems), and even when they do, you have no way to compute them: a morphism in the localization is an equivalence class of arbitrarily long zig-zags $X \leftarrow \bullet \to \bullet \leftarrow \cdots \to Y$, and there is no algorithm for deciding when two zig-zags are equal. The localization exists abstractly but is computationally inert.

Quillen's insight, in 1967, was that you can *tame* the localization by adding auxiliary structure. Alongside $\mathcal{W}$, decree two more classes of maps — **cofibrations** and **fibrations** — chosen so that they interlock with $\mathcal{W}$ through a *lifting* relation and a *factorization* property. The cofibrations are the "good inclusions" (think: a subcomplex sitting inside a CW complex) and the fibrations are the "good surjections" (think: a fiber bundle projection). This auxiliary scaffolding never changes what the localization *is* — $\mathrm{Ho}(\mathcal{M})$ depends only on $(\mathcal{M}, \mathcal{W})$ — but it makes it *computable*. The structural backbone of the chapter is the single relationship

$$\text{(weak equivalences} = \text{maps to invert)} \;+\; \text{(cofibrations, fibrations} = \text{the computational scaffolding)} \;\Longrightarrow\; \mathrm{Ho}(\mathcal{M}) \text{ is tractable.}$$

Concretely, the payoff is this. Every object $X$ has a **cofibrant replacement** $QX$ and a **fibrant replacement** $RX$, both weakly equivalent to $X$ and both obtained by factoring a map. On the **bifibrant** objects — those that are both cofibrant and fibrant — the notion of two maps being **homotopic** becomes a genuine equivalence relation, exactly as for continuous maps of spaces, and the morphisms of $\mathrm{Ho}(\mathcal{M})$ are simply homotopy classes of maps between bifibrant replacements. The opaque zig-zags collapse to something you can write down. This is the content of the fundamental theorem of model categories, and it is why the apparatus exists. Quillen's framework also reveals that the same five axioms govern topology, homological algebra, and the homotopy theory of simplicial sets all at once: a model category is, in modern language, a **presentation of an (∞,1)-category** by a relative category $(\mathcal{M}, \mathcal{W})$, and the choice of cofibrations and fibrations is a choice of how to present it.

This chapter assumes you are fluent with the categorical machinery of the earlier chapters: [[Def - Limit and Colimit|limits and colimits]], [[Def - Pullback and Pushout|pullbacks and pushouts]], [[Def - Adjunction|adjunctions]] together with their [[Def - Unit and Counit of an Adjunction|unit and counit]], [[Def - Functor|functors]] and [[Def - Natural Transformation|natural transformations]], and [[Def - Equivalence of Categories|equivalence of categories]]. From topology you should recall what a [[Def - Homotopy|homotopy]] is, what a [[Def - Higher Homotopy Group|homotopy group]] is, and the idea of a [[Def - Homotopy Equivalence and Contractible Space|homotopy equivalence]]. No prior exposure to homotopy theory as an axiomatic subject is assumed — that is what we are building.

---

# Concept Map

## §M.1 The Axioms

- **[[Def - Model Category]]**
	- A **model category** is a bicomplete category $\mathcal{M}$ equipped with three classes of maps — weak equivalences $\mathcal{W}$, cofibrations, and fibrations — satisfying the Quillen axioms MC1–MC5: bicompleteness, 2-out-of-3 for $\mathcal{W}$, closure under retracts, the two lifting axioms (cofibrations lift against trivial fibrations, trivial cofibrations against fibrations), and the two factorization axioms (every map factors as cofibration-then-trivial-fibration and as trivial-cofibration-then-fibration). The data is exactly an abstract framework for homotopy theory: $\mathcal{W}$ records which maps we want to invert, while cofibrations and fibrations make the inversion computable. Hovey's refinement makes the factorizations functorial and requires only the retract axiom, deriving the lifting and closure properties as theorems.

- **[[Def - Lifting Property and the Retract Argument]]**
	- A map $i$ has the **left lifting property** (LLP) against $p$, and $p$ the **right lifting property** (RLP) against $i$, if every commuting square with $i$ on the left and $p$ on the right admits a diagonal filler $h$. A map $f$ is a **retract** of $g$ if it sits inside $g$ via a retract diagram whose horizontal composites are identities. These two notions are the entire combinatorial engine of the theory: the lifting axiom MC4 is phrased with LLP/RLP, and the retract argument converts a factorization plus a lifting property into a retract.

- **[[Def - Cofibrant and Fibrant Objects]]**
	- An object $X$ is **cofibrant** if the unique map $\varnothing \to X$ from the initial object is a cofibration, and **fibrant** if $X \to *$ to the terminal object is a fibration; it is **bifibrant** if both. Factoring $\varnothing \to X$ gives a cofibrant replacement $QX \xrightarrow{\sim} X$; factoring $X \to *$ gives a fibrant replacement $X \xrightarrow{\sim} RX$. In $\mathbf{Top}$ every object is fibrant and the cofibrant objects are the retracts of cell complexes; in $\mathbf{Ch}(R)$ the cofibrant objects are the complexes of projectives.

> [!tip] Unlocked: ∞-Categories and Relative Categories *(from Higher Category Theory)*
> A model structure is a *presentation* of an **(∞,1)-category**: the underlying data $(\mathcal{M}, \mathcal{W})$ is a **relative category**, and the cofibrations and fibrations are a choice of how to compute its homotopy theory. Different model structures with the same weak equivalences present the same ∞-category. This is the entry point to the Joyal–Lurie theory of **quasi-categories** developed in the [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories|Higher Categories]] chapter.

- **[[Ex - The trivial model structures on a category]]** (⭐⭐)
	- On any bicomplete category, taking $\mathcal{W}$ = isomorphisms and both other classes = all maps gives a model structure; verify the axioms and identify the homotopy category.
- **[[Ex - Two-out-of-three and isomorphisms]]** (⭐)
	- Deduce from MC2 that every isomorphism is a weak equivalence and that $\mathcal{W}$ is closed under composition and "2-out-of-6"-style cancellation.
- **[[Ex - The opposite of a model category]]** (⭐⭐)
	- Show that if $\mathcal{M}$ is a model category then $\mathcal{M}^{op}$ is one too, with cofibrations and fibrations interchanged, and trace how every definition dualizes.

> [!note] Exercise Index — §M.1
> [[Exercise Index - §M.1 The Axioms]]

## §M.2 Lifting, Factorization, and the Retract Argument

- **[[Thm - The Retract Argument]]**
	- If $f = p \circ i$ and $f$ has the LLP with respect to $p$, then $f$ is a retract of $i$; dually, if $f$ has the RLP with respect to $i$, then $f$ is a retract of $p$. The proof is one diagram: the lift in the square with $i$ across the top and $p$ down the right supplies the retraction. This tiny lemma is the lever that makes the model-category axioms *overdetermined*: it lets you upgrade "$f$ lifts against the relevant class" into "$f$ belongs to a class," because the factorization MC5 produces the map you retract onto.

- **[[Thm - Closure Properties of the Model Structure]]**
	- The cofibrations are *exactly* the maps with the LLP against all trivial fibrations; trivial cofibrations are exactly the maps with LLP against all fibrations; fibrations are exactly the maps with RLP against all trivial cofibrations (and dually). Consequently each class is closed under retracts, cofibrations are closed under pushout and fibrations under pullback, and any two of the three classes determine the third. The proofs all run through the retract argument combined with factorization.

> [!tip] Unlocked: The Small Object Argument and Cofibrant Generation *(from Homotopical Algebra)*
> The factorization axiom MC5 is not magic — in all standard examples the factorizations are *built* by Quillen's **small object argument**, which transfinitely attaches cells from a set of generating cofibrations. A model category produced this way is **cofibrantly generated**, and almost every model structure in nature (on $\mathbf{Top}$, $\mathbf{sSet}$, $\mathbf{Ch}(R)$) is of this form.

- **[[Ex - The retract argument in detail]]** (⭐⭐)
	- Carry out the diagram chase proving the retract argument, both the LLP and the dual RLP versions, with every square drawn.
- **[[Ex - Lifting properties determine the classes]]** (⭐⭐)
	- Prove that cofibrations coincide with the maps having LLP against all trivial fibrations, deducing closure under pushout and retract as corollaries.
- **[[Ex - The small object argument sketch]]** (⭐⭐⭐)
	- Sketch the transfinite construction that factors any map of $\mathbf{Top}$ as a relative cell complex followed by a Serre fibration, identifying the generating set $\{S^{n-1} \hookrightarrow D^n\}$.

> [!note] Exercise Index — §M.2
> [[Exercise Index - §M.2 Lifting, Factorization, and the Retract Argument]]

## §M.3 The Homotopy Category

- **[[Def - Cylinder Object, Path Object, and Homotopy]]**
	- A **cylinder object** $\mathrm{Cyl}(A)$ factors the fold map $A \sqcup A \xrightarrow{\nabla} A$ as a cofibration $A \sqcup A \rightarrowtail \mathrm{Cyl}(A)$ followed by a weak equivalence $\mathrm{Cyl}(A) \xrightarrow{\sim} A$; a **left homotopy** from $f$ to $g$ is a map $\mathrm{Cyl}(A) \to B$ restricting to $f$ and $g$ on the two ends. A **path object** $\mathrm{Path}(B)$ and **right homotopy** are the duals. On bifibrant objects left and right homotopy coincide, are an equivalence relation on $\mathcal{M}(A,B)$, and yield the set $\pi(A,B)$ of homotopy classes — recovering the ordinary notion of homotopic continuous maps in $\mathbf{Top}$.

- **[[Thm - The Homotopy Category of a Model Category]]**
	- The localization $\mathrm{Ho}(\mathcal{M}) = \mathcal{M}[\mathcal{W}^{-1}]$ exists and is equivalent to the category whose objects are the bifibrant objects of $\mathcal{M}$ and whose morphisms are homotopy classes of maps; for general $X, Y$ one has $\mathrm{Ho}(\mathcal{M})(X,Y) \cong \pi(QRX, QRY)$, computed through cofibrant–fibrant replacement. This is the fundamental theorem: it replaces opaque zig-zags by honest homotopy classes and is the entire reason the axioms are worth imposing.

> [!tip] Unlocked: The Derived Category and Triangulated Categories *(from Homological Algebra)*
> Applied to $\mathbf{Ch}(R)$ with quasi-isomorphisms as weak equivalences, the homotopy category *is* the **derived category** $D(R)$. The fundamental theorem is exactly the statement that maps in $D(R)$ are chain-homotopy classes of maps between complexes of projectives. The extra structure of distinguished triangles makes $D(R)$ a **triangulated category**, and the model-categorical viewpoint explains where that structure comes from.

- **[[Ex - Left homotopy is an equivalence relation on cofibrant objects]]** (⭐⭐⭐)
	- Prove reflexivity, symmetry, and transitivity of left homotopy on a cofibrant domain, using that the two endpoint inclusions into a cylinder are trivial cofibrations.
- **[[Ex - Homotopy in spaces recovers the usual notion]]** (⭐⭐)
	- Show that in the Quillen model structure on $\mathbf{Top}$ the cylinder object $A \times [0,1]$ makes left homotopy agree with the classical homotopy of continuous maps.
- **[[Ex - The homotopy category of chain complexes is the derived category]]** (⭐⭐⭐)
	- Identify $\mathrm{Ho}(\mathbf{Ch}(R))$ with $D(R)$, showing that homotopy of chain maps is chain homotopy and that fibrant–cofibrant replacement is projective resolution.

> [!note] Exercise Index — §M.3
> [[Exercise Index - §M.3 The Homotopy Category]]

## §M.4 Quillen Functors, Adjunctions, and Equivalences

- **[[Def - Quillen Adjunction and Quillen Equivalence]]**
	- An adjunction $F \dashv U$ between model categories is a **Quillen adjunction** if the left adjoint $F$ preserves cofibrations and trivial cofibrations — equivalently the right adjoint $U$ preserves fibrations and trivial fibrations. It is a **Quillen equivalence** if for every cofibrant $A$ and fibrant $B$, a map $FA \to B$ is a weak equivalence exactly when its adjunct $A \to UB$ is. Quillen adjunctions are the structure-preserving maps of model categories, and Quillen equivalences are the maps that become equivalences after passing to homotopy categories.

- **[[Def - Homotopy Limit and Colimit]]**
	- Ordinary limits and colimits are *not* homotopy-invariant — replacing a diagram by a weakly equivalent one can change the colimit — so one defines the **homotopy colimit** and **homotopy limit** as the derived functors of $\mathrm{colim}$ and $\lim$. The homotopy pushout of $* \leftarrow X \to *$ is the (unreduced) suspension $\Sigma X$, computed via the double mapping cylinder; the homotopy pullback of $* \to Y \leftarrow *$ is the loop space. These corrected (co)limits are the ones that respect weak equivalence.

- **[[Thm - Quillen Adjunctions Descend to Derived Adjunctions]]**
	- A Quillen adjunction $F \dashv U$ induces a **total derived adjunction** $\mathbf{L}F \dashv \mathbf{R}U$ between homotopy categories, with $\mathbf{L}F = F \circ Q$ (apply $F$ after cofibrant replacement) and $\mathbf{R}U = U \circ R$ (apply $U$ after fibrant replacement). If the Quillen adjunction is a Quillen equivalence, the derived adjunction is an equivalence of categories $\mathrm{Ho}(\mathcal{M}) \simeq \mathrm{Ho}(\mathcal{N})$. This is how one proves two model categories present the *same* homotopy theory.

> [!tip] Unlocked: The Homotopy Hypothesis and ∞-Topoi *(from Higher Category Theory)*
> The Quillen equivalence $\mathbf{Top} \simeq_Q \mathbf{sSet}$ is the rigorous form of the slogan that spaces and combinatorial simplicial models carry the same homotopy theory — a baby case of the **homotopy hypothesis** (∞-groupoids = spaces). Stacking Quillen equivalences is how one shows different models of **∞-categories** agree, and ultimately how Lurie's theory of **∞-topoi** is set up.

> [!tip] Unlocked: Derived Functors, Tor, Ext, and Spectral Sequences *(from Homological Algebra)*
> In $\mathbf{Ch}(R)$ the total derived functors of $\otimes$ and $\mathrm{Hom}$ are exactly the classical **Tor** and **Ext**: $\mathrm{Tor}_n(M,N)$ is the homology of $\mathbf{L}({-}\otimes N)$ applied to $M$. Homotopy colimits over filtered or more complicated diagrams are computed by **spectral sequences**, which the model-categorical framework organizes.

- **[[Ex - Geometric realization and singular nerve form a Quillen equivalence]]** (⭐⭐⭐)
	- Verify that $|{-}| \dashv \mathrm{Sing}$ between $\mathbf{sSet}$ and $\mathbf{Top}$ is a Quillen adjunction and a Quillen equivalence, so $\mathrm{Ho}(\mathbf{sSet}) \simeq \mathrm{Ho}(\mathbf{Top})$.
- **[[Ex - The derived tensor product computes Tor]]** (⭐⭐⭐)
	- Show that the total left derived functor of $-\otimes_R N$ on $\mathbf{Ch}(R)$ computes $\mathrm{Tor}_*^R$, by replacing the argument with a complex of projectives.
- **[[Ex - A left Quillen functor preserves cofibrations]]** (⭐⭐)
	- Prove directly from the lifting characterization that a left adjoint preserving generating cofibrations preserves all cofibrations and trivial cofibrations.

> [!note] Exercise Index — §M.4
> [[Exercise Index - §M.4 Quillen Functors, Adjunctions, and Equivalences]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The problems of this subject cluster around a handful of recurring goals. The first and most common is **verifying that some triple $(\mathcal{W}, \mathrm{cof}, \mathrm{fib})$ is a model structure** — that is, checking the five axioms on a concrete category like $\mathbf{Top}$ or $\mathbf{Ch}(R)$, where the hard axioms are always lifting (MC4) and factorization (MC5). A second goal is **identifying the homotopy category**: given $\mathcal{M}$ and its weak equivalences, name $\mathrm{Ho}(\mathcal{M})$ as a category you already understand — the homotopy category of CW complexes, or the derived category $D(R)$. A third is **proving two model categories are Quillen equivalent**, the homotopy-theoretic analogue of proving two presentations describe the same object. A fourth is **computing a derived functor** — a homotopy (co)limit, a $\mathbf{Tor}$ or $\mathbf{Ext}$ group — by reducing it to an ordinary functor applied to a (co)fibrant replacement. A fifth, more structural, is **showing a class of maps is closed** under some operation (retracts, pushouts, transfinite composition), which is what makes the small object argument run. These five — verify the axioms, identify $\mathrm{Ho}$, prove Quillen equivalence, compute a derived functor, establish closure — are the targets, and they recur because each is a way of pinning down a homotopy theory: you understand a model category when you know its weak equivalences, its (co)fibrant objects, its homotopy category, and how it relates to the standard models.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **A factorization is given (MC5)**, which is the richest source: factoring $\varnothing \to X$ produces a cofibrant replacement, factoring $X \to *$ a fibrant replacement, and factoring an arbitrary map produces the (co)fibrant intermediary that every construction needs. **A lifting property is available (MC4)**, which is what lets you build homotopies, retractions, and comparison maps — whenever you need a diagonal in a square, scan for a (trivial) cofibration on the left and a (trivial) fibration on the right. **An object is known to be cofibrant or fibrant**, which is the hypothesis that turns left and right homotopy into the same equivalence relation and makes derived functors behave. **An adjunction is given**, which by Ken Brown's lemma already forces the left adjoint to preserve weak equivalences between cofibrant objects, so a Quillen adjunction is a mild upgrade away. **The weak equivalences satisfy 2-out-of-3 (MC2)**, the workhorse for proving a map is a weak equivalence by sandwiching it between two known ones. The recurring move is to route a source to a target: a factorization routes to (co)fibrant replacement and hence to a computation of $\mathrm{Ho}$; a lifting property routes through the retract argument to a closure statement; an adjunction plus preservation of cofibrations routes through the derived functor theorem to an equivalence of homotopy categories.

---

# Legal Operations

These are the moves nearly every argument in this chapter is built from. When stuck, scan the list. Everything is self-contained: a reader who has only just met the axioms should be able to follow each operation from its description.

**Legal operations:**

1. **Factor a map (MC5).** Any map $f$ splits two ways: as a cofibration followed by a trivial fibration, and as a trivial cofibration followed by a fibration. *Trigger:* you need an intermediate object with good properties — a cofibrant or fibrant replacement, or a "fattened" version of a map. *Pattern:* "factor $\varnothing \to X$ as $\varnothing \rightarrowtail QX \xrightarrow{\sim} X$" produces a cofibrant object weakly equivalent to $X$. This is the single most-used operation, because every derived construction begins by replacing objects with (co)fibrant ones.

2. **Lift across a square (MC4).** Given a commuting square with a cofibration on the left and a trivial fibration on the right (or a trivial cofibration on the left and a fibration on the right), fill in the diagonal. *Trigger:* you want to construct a map but can only specify it on a subobject and after a projection. *Pattern:* the homotopies in this chapter are all lifts, and so are the comparison maps between two cofibrant replacements.

3. **Run the retract argument.** If $f = p \circ i$ and $f$ lifts against $p$, then $f$ is a retract of $i$. *Trigger:* you know $f$ has a lifting property and want to conclude $f$ lies in a class (cofibration, fibration). *Pattern:* factor $f$, observe it lifts against the second factor, retract onto the first; see [[Thm - The Retract Argument]].

4. **Replace an object by a (co)fibrant model.** Pass from $X$ to $QX$ (cofibrant) or $RX$ (fibrant), each weakly equivalent to $X$. *Trigger:* a theorem or construction requires its input to be cofibrant or fibrant — derived functors, the homotopy relation, lifting all do. *Pattern:* "without loss of generality $X$ is cofibrant, replacing $X$ by $QX$."

5. **Use 2-out-of-3 to certify a weak equivalence (MC2).** If two of $f$, $g$, $g \circ f$ are weak equivalences, so is the third. *Trigger:* you want to show some map is a weak equivalence and you can factor it through known equivalences. *Pattern:* sandwich the map between a replacement equivalence on each side.

6. **Build a homotopy as a map out of a cylinder (or into a path object).** A left homotopy $f \simeq_\ell g$ *is* a map $\mathrm{Cyl}(A) \to B$ restricting to $f$ and $g$. *Trigger:* you must show two maps become equal in $\mathrm{Ho}(\mathcal{M})$. *Pattern:* exhibit the cylinder map, or dually a map into $\mathrm{Path}(B)$; see [[Def - Cylinder Object, Path Object, and Homotopy]].

7. **Dualize.** Every statement has a dual obtained by passing to $\mathcal{M}^{op}$, which swaps cofibrations with fibrations, initial with terminal, cylinders with path objects, left homotopy with right. *Trigger:* you have proved a statement about cofibrations and want the fibration version for free. *Pattern:* "by the dual argument in $\mathcal{M}^{op}$."

8. **Recognize a class by its lifting property.** Cofibrations are exactly the maps with LLP against all trivial fibrations, and so on for the other three classes. *Trigger:* you want to prove a specific map is a cofibration without knowing the factorizations explicitly. *Pattern:* check it lifts against every trivial fibration; see [[Thm - Closure Properties of the Model Structure]].

9. **Push out a cofibration / pull back a fibration.** Cofibrations are stable under pushout and trivial cofibrations too; fibrations and trivial fibrations are stable under pullback. *Trigger:* you are gluing or restricting and want to know the resulting map stays in its class. *Pattern:* form the [[Def - Pullback and Pushout|pushout or pullback]] square and invoke closure.

**Illegal but tempting operations:**

> [!warning] 1. Taking an ordinary colimit and expecting it to be homotopy-invariant
> It is tempting to compute the colimit of a diagram and treat the answer as well-defined up to weak equivalence. It is not: the pushout of $* \leftarrow S^1 \to *$ (collapsing the circle two ways) is a point, but the *homotopy* pushout is the suspension $\Sigma S^1 = S^2$. Replacing one leg of the diagram by a weakly equivalent map changes the strict colimit. The operation becomes legal once you first replace the diagram by a cofibrant one — that is exactly what the **homotopy colimit** (see [[Def - Homotopy Limit and Colimit]]) does, and why it, not the strict colimit, is the homotopy-invariant construction.

> [!warning] 2. Assuming left and right homotopy agree for arbitrary objects
> On general objects, "$f \simeq_\ell g$" (a cylinder map) and "$f \simeq_r g$" (a path map) are genuinely different relations, and neither need be transitive. The coincidence theorem holds only when the domain is cofibrant (for the left notion to be well-behaved) and the codomain is fibrant (for the right). The repair is to restrict to **bifibrant** objects, where the two notions merge into one equivalence relation $\simeq$ — which is precisely why $\mathrm{Ho}(\mathcal{M})$ is built from the bifibrant objects.

> [!warning] 3. Concluding $F$ preserves weak equivalences from "$F$ is a left Quillen functor"
> A left Quillen functor preserves cofibrations and *trivial* cofibrations, but it does **not** preserve general weak equivalences. The free abelian group functor applied to a weak equivalence of non-cofibrant spaces can fail to be a weak equivalence. Ken Brown's lemma rescues a restricted statement: a left Quillen functor preserves weak equivalences *between cofibrant objects*. That is exactly why the total left derived functor $\mathbf{L}F = F \circ Q$ inserts a cofibrant replacement before applying $F$ — see [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]].

> [!warning] 4. Believing the factorization of a map is unique
> The factorization $f = p \circ i$ produced by MC5 is far from unique — there are many cofibrant replacements of a given object, and many cylinder objects for a given $A$. What is true is that any two are connected by a weak equivalence compatible with the structure maps, so they all become *isomorphic in the homotopy category*. Treating a particular replacement as canonical is harmless only after passing to $\mathrm{Ho}(\mathcal{M})$; before that, uniqueness fails and the functorial factorizations of Hovey's formulation are what restore canonicity at the point level.

---

# Problem-Solving Strategy

The problems in this chapter are won or lost the moment you decide which of the five targets you are chasing, so begin by classifying. Almost every exercise is one of: verify the axioms, identify the homotopy category, prove a Quillen equivalence, compute a derived functor, or establish a closure property — and each has a characteristic route.

If the problem **asks you to verify that a triple is a model structure**, the cheap axioms (bicompleteness, 2-out-of-3, retracts) are dispatched first, and then all the work is in lifting (MC4) and factorization (MC5). The decisive realization is that you almost never check MC5 by hand: you exhibit a *set of generating cofibrations* and invoke Quillen's small object argument, which factors any map by transfinitely attaching cells from that set. So the real task reduces to naming the generators — $\{S^{n-1} \hookrightarrow D^n\}$ for $\mathbf{Top}$, the boundary inclusions $\partial\Delta^n \hookrightarrow \Delta^n$ for $\mathbf{sSet}$ — and checking the lifting axiom against them. The closure theorem [[Thm - Closure Properties of the Model Structure]] then tells you the full classes are determined.

If the problem **asks you to identify the homotopy category**, the route runs through the fundamental theorem [[Thm - The Homotopy Category of a Model Category]]. You do not compute the localization directly; instead you determine which objects are bifibrant and what homotopy of maps between them means concretely, and then $\mathrm{Ho}(\mathcal{M})$ is the category of bifibrant objects and homotopy classes. In $\mathbf{Top}$ this yields CW complexes and homotopy classes of continuous maps; in $\mathbf{Ch}(R)$ it yields the derived category, with chain homotopy as the homotopy relation. The skill is recognizing the bifibrant objects — they are usually the "resolutions" of the subject (CW approximations, projective resolutions).

If the problem **asks for a Quillen equivalence**, you have an adjunction $F \dashv U$ and want $\mathrm{Ho}(\mathcal{M}) \simeq \mathrm{Ho}(\mathcal{N})$. First confirm it is a Quillen adjunction — check $F$ preserves cofibrations and trivial cofibrations, which by [[Def - Quillen Adjunction and Quillen Equivalence]] is equivalent to $U$ preserving fibrations and trivial fibrations, so use whichever class is easier. Then check the equivalence condition: for cofibrant $A$ and fibrant $B$, a map $FA \to B$ is a weak equivalence if and only if its adjunct is. The non-obvious part is almost always one half of this iff, and the standard tactic is to use the unit or counit and 2-out-of-3.

If the problem **asks you to compute a derived functor** — a homotopy colimit, a $\mathbf{Tor}$ group — the route is: replace the input by a (co)fibrant object, apply the underlying functor, and read off the answer. The whole subtlety is the replacement, because the underlying functor is only homotopy-meaningful on (co)fibrant inputs. For $\mathbf{Tor}_*(M, N)$ you replace $M$ by a projective resolution (a cofibrant model in $\mathbf{Ch}(R)$), tensor, and take homology.

A meta-strategy threads through all of these: **when something fails to be homotopy-invariant, it is because you used a non-(co)fibrant object, and the fix is always to replace it.** Strict colimits, applications of a left adjoint, the homotopy relation itself — each misbehaves exactly when fed a raw object, and each is repaired by inserting a cofibrant or fibrant replacement. Internalizing this single diagnostic resolves the majority of confusions in the subject: every "derived" construction in mathematics is an ordinary construction with a replacement step bolted on the front.

---

# Most Reusable Properties

- **[[Thm - The Retract Argument|The Retract Argument]]**: a factorization plus a matching lifting property exhibits the map as a retract. This is the most reusable single fact in the foundations because it is what makes the axioms overdetermined — it converts "lifts against the right class" into "belongs to the class." Reach for it whenever you want to prove a specific map is a cofibration or fibration without explicit access to the factorizations: factor the map, note it lifts against the appropriate factor, retract. It is the engine behind every closure property and behind the lifting characterization of the classes.

- **[[Thm - Closure Properties of the Model Structure|The Lifting Characterization]]**: each of the four classes is exactly the maps with a specified lifting property. **Typical use:** to recognize a class without computing factorizations — a map is a cofibration precisely when it lifts against all trivial fibrations. This characterization also delivers, for free, that cofibrations are closed under pushout and fibrations under pullback, and that any two classes determine the third. It is the reason the small object argument suffices to build an entire model structure from a set of generators.

- **[[Def - Cylinder Object, Path Object, and Homotopy|The Cylinder/Path Duality]]**: a homotopy is a map out of a cylinder or into a path object. **Typical use:** to prove two maps agree in $\mathrm{Ho}(\mathcal{M})$, exhibit a cylinder map between them. The duality halves your work: prove everything for left homotopy and cylinders, then dualize in $\mathcal{M}^{op}$ to obtain the right-homotopy and path-object versions automatically. This is also where the homotopy relation gains its concrete handle — the abstract "isomorphic in $\mathrm{Ho}$" becomes "connected by a cylinder."

- **[[Thm - The Homotopy Category of a Model Category|The Fundamental Theorem]]**: $\mathrm{Ho}(\mathcal{M})$ is the category of bifibrant objects and homotopy classes, with $\mathrm{Ho}(\mathcal{M})(X,Y) \cong \pi(QRX, QRY)$. **Typical use:** any time you must reason about, or compute morphisms in, the localized category. It is what lets you treat the derived category $D(R)$ as a concrete category of complexes-up-to-chain-homotopy rather than an inscrutable zig-zag category, and it is the justification for every "compute in the homotopy category" argument.

- **[[Thm - Quillen Adjunctions Descend to Derived Adjunctions|Derived Adjunction]]**: a Quillen adjunction $F \dashv U$ gives $\mathbf{L}F \dashv \mathbf{R}U$ on homotopy categories, an equivalence when the Quillen adjunction is a Quillen equivalence. **Typical use:** to transport a homotopy theory from one model to another, and to manufacture the classical derived functors ($\mathbf{Tor}$, $\mathbf{Ext}$, homotopy (co)limits) as $\mathbf{L}F = F \circ Q$ and $\mathbf{R}U = U \circ R$. Recognizing an adjunction as Quillen is the standard route to comparing two presentations of the same homotopy theory.

---

# Bridges

1. **Algebraic topology — the homotopy category of spaces.** The Quillen (Serre) model structure on $\mathbf{Top}$ takes weak equivalences to be the [[Def - Higher Homotopy Group|weak homotopy equivalences]] (maps inducing isomorphisms on every $\pi_n$ — see also the [[Def - Path-Product and the Fundamental Group|fundamental group]]), fibrations to be Serre fibrations (maps with the homotopy lifting property against disks), and cofibrations to be retracts of relative cell complexes. Every space is fibrant, and the cofibrant objects are the CW-like spaces, so the fundamental theorem identifies $\mathrm{Ho}(\mathbf{Top})$ with the classical homotopy category of CW complexes and homotopy classes of maps. This is the bridge that makes "model category" the right abstraction: the entire edifice of classical homotopy theory is one instance, and the abstract cylinder object $\mathrm{Cyl}(A)$ is, concretely, the topological cylinder $A \times [0,1]$.

2. **Homological algebra — the derived category as a homotopy category.** On $\mathbf{Ch}(R)$, the chain complexes of [[Def - Module|$R$-modules]], the projective model structure takes weak equivalences to be quasi-isomorphisms (maps inducing isomorphisms on homology), fibrations to be degreewise surjections, and the cofibrant objects to be the complexes of projectives. The homotopy relation is exactly [[Def - Chain Map and Chain Homotopy|chain homotopy]], so the fundamental theorem says $\mathrm{Ho}(\mathbf{Ch}(R))$ is the **derived category** $D(R)$, with maps given by chain-homotopy classes of maps between projective resolutions. The classical derived functors **Tor** and **Ext** are then the total derived functors of $\otimes_R$ and $\mathrm{Hom}_R$ — homological algebra is homotopy theory done in chain complexes, and this bridge is the cleanest way to see it.

3. **Higher category theory — model categories as presentations of ∞-categories.** A model category $(\mathcal{M}, \mathcal{W})$ is a *relative category*, and inverting $\mathcal{W}$ up to coherent homotopy produces an **(∞,1)-category**; the cofibrations and fibrations are a choice of presentation that makes this inversion computable. The Quillen model structure on [[Def - Simplicial Set|simplicial sets]] (cofibrations = monomorphisms, fibrations = Kan fibrations, weak equivalences = maps that are weak homotopy equivalences on geometric realization) is the prototype, and its fibrant objects, the [[Def - Kan Complex and the Nerve|Kan complexes]], model ∞-groupoids. The [[Def - Quasi-Category|quasi-category]] model of ∞-categories arises from a related (Joyal) model structure on $\mathbf{sSet}$, developed in the [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories|Higher Categories]] chapter; model categories are the bridge from strict 1-categorical foundations to that world.

4. **Algebraic geometry and stable homotopy theory — derived categories of sheaves and spectra.** The derived category of coherent sheaves on a scheme — the home of modern intersection theory and mirror symmetry — is built exactly as $\mathrm{Ho}$ of a model structure on chain complexes of sheaves, generalizing the $\mathbf{Ch}(R)$ story to a geometric setting. One level up, the **stable homotopy category** is $\mathrm{Ho}$ of a model category of spectra, where the weak equivalences are the stable equivalences; the same five axioms govern it, and the suspension that was a homotopy pushout in $\mathbf{Top}$ becomes invertible. These are forward bridges: the model-categorical machinery of this chapter is the language in which **triangulated categories** of geometric and stable-homotopical origin are constructed and compared.

---

# Insights

**The unifying frame: a model category is a presentation of a homotopy theory, and the three classes play three distinct roles.** It is tempting to see the five axioms as an unmotivated list, but they organize around one idea. The weak equivalences $\mathcal{W}$ are the *only* intrinsic data — they record which maps you have decided to treat as equivalences, and the homotopy category $\mathrm{Ho}(\mathcal{M})$ depends on nothing else. The cofibrations and fibrations are *auxiliary*, a chosen scaffolding, and their job is purely computational: they identify, via factorization, the "good" objects (cofibrant, fibrant) on which the localization can be computed by honest homotopy classes instead of zig-zags. Two different model structures with the same weak equivalences present the same homotopy theory; they are two coordinate systems on one geometric object. Whenever the axioms feel arbitrary, ask of each class: is this telling me what to invert, or how to compute the inversion? Weak equivalences answer the first; cofibrations and fibrations answer the second.

**The true name of "fibration" is "has the homotopy lifting property," and of "cofibration" is "has the homotopy extension property."** The official definitions phrase fibrations and cofibrations through abstract lifting against the other classes, which is the right thing to *check* in the axioms but the wrong thing to *picture*. Operationally, a fibration is a map you can lift homotopies along — given a homotopy downstairs and a lift of one end, you can lift the whole homotopy — and a cofibration is a map you can extend homotopies over. This is why fibrations behave like fibre bundles and cofibrations like inclusions of subcomplexes, and it is the intuition that should fire when you see the word: "fibration" should evoke the homotopy lifting property and the long exact sequence of a fibration, not a diagram chase.

**Per-axiom necessity is the cleanest way to understand the definition: drop any one axiom and a specific construction breaks.** Drop 2-out-of-3 (MC2) and the homotopy relation fails to be transitive, because transitivity of homotopy is proved by gluing cylinders and certifying the result is still a cylinder using 2-out-of-3. Drop lifting (MC4) and you cannot construct homotopies or comparison maps at all, since every homotopy in the theory is a lift. Drop factorization (MC5) and there are no (co)fibrant replacements, so the homotopy category cannot be computed and derived functors do not exist. Each axiom is load-bearing for one named feature, which is the surest sign the list is not arbitrary: it is exactly what is needed, and no more, to make localization computable.

**Everything "derived" in mathematics is an ordinary construction with a replacement step bolted onto the front.** The derived tensor product is $\otimes$ applied after projective resolution; the homotopy colimit is $\mathrm{colim}$ applied after cofibrant replacement of the diagram; the total left derived functor $\mathbf{L}F$ is $F$ applied after cofibrant replacement $Q$. The reason the bare functor must be corrected is always the same — it fails to respect weak equivalences on raw objects but does respect them on (co)fibrant ones (Ken Brown's lemma), so you slide a replacement in front. Once you see this pattern, the proliferation of "derived" gadgets across homological algebra, algebraic geometry, and homotopy theory collapses into a single mechanism, and the model-category axioms are precisely the hypotheses that make the mechanism run.

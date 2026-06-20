---
type: definition
subject: higher-categories
prereqs:
  - "Def - Opetope"
  - "Def - Presheaf"
  - "Thm - The Yoneda Lemma"
  - "Def - Simplicial Set"
tags: [category-theory, higher-categories, foundations]
---

# Notation

We write $\mathbb{O}$ for the **category of opetopes**: its objects are the [[Def - Opetope|opetopes]] of all dimensions, and its morphisms are the structural maps (face inclusions and degeneracies) that build lower opetopes into the boundaries of higher ones. An **opetopic set** is a presheaf $X : \mathbb{O}^{op} \to \mathbf{Set}$; we write $\mathbf{Set}^{\mathbb{O}^{op}} = [\mathbb{O}^{op}, \mathbf{Set}]$ for the category of all of them. For an opetope $O$, the set $X(O)$ is written $X_O$ and called the set of **$O$-cells** of $X$. The Yoneda embedding is $\mathbf{y} : \mathbb{O} \to \mathbf{Set}^{\mathbb{O}^{op}}$, $\mathbf{y}O = \mathbb{O}(-, O)$; the presheaf $\mathbf{y}O$ is the **standard $O$-cell**. We compare throughout with $\mathbf{sSet} = [\Delta^{op}, \mathbf{Set}]$ ([[Def - Simplicial Set|simplicial sets]], $\Delta$ the simplex category) and with globular sets $= [\mathbb{G}^{op}, \mathbf{Set}]$ ($\mathbb{G}$ the globe category). The full symbol registry is on the parent page [[Higher Categories — Opetopes and Opetopic Sets]].

---

# Axiom Motivation

Once you have the opetopes — the cell-shapes of every dimension — you need a notion of "a thing made of opetopic cells." The design question is: what data is a *space built from opetopes*, and what consistency must that data satisfy? The answer is forced by exactly the same reasoning that produces simplicial sets from simplices, and recovering that reasoning is the cleanest way to invent the definition.

A thing built from opetopic cells should, first of all, *have cells of each opetopic shape*: for every [[Def - Opetope|opetope]] $O$ there is a set $X_O$ of "cells of $X$ shaped like $O$". So at minimum the data is an assignment $O \mapsto X_O$ of a set to each opetope. But the cells cannot be independent: a cell shaped like $O$ has a boundary made of lower opetopes, and that boundary must consist of *actual cells of $X$*. Concretely, an arity-$2$ $2$-cell of $X$ (shaped like the arity-$2$ opetope) has two source $1$-cells and one target $1$-cell, and these must be genuine $1$-cells of $X$ — elements of $X_{(\text{arrow})}$. So whenever there is a structural map $O' \to O$ in $\mathbb{O}$ assembling a lower opetope $O'$ into the boundary of $O$, there must be a *restriction* operation $X_O \to X_{O'}$ pulling a cell of $X$ back to the corresponding boundary cell. And these restrictions must be **functorial**: restricting to a face and then to a face of that face must agree with restricting directly. Functoriality of the restrictions, indexed by the structural maps of $\mathbb{O}$, is precisely the statement that $X$ is a contravariant functor $\mathbb{O}^{op} \to \mathbf{Set}$ — a [[Def - Presheaf|presheaf]].

That is the whole definition: an opetopic set is a presheaf on $\mathbb{O}$. There is nothing more to add, and the reason is instructive. The two desiderata — "cells of each shape" and "boundaries are real cells, consistently" — are exactly the object-part and morphism-part of a presheaf. Drop the morphism part and you have a bare graded set with no gluing: cells would have boundaries floating free, and you could not even say when two cells are composable. Drop the object part (have only the maps) and there is nothing to map. Both halves are needed, and together they are precisely a functor out of $\mathbb{O}^{op}$.

Why **contravariant** (a presheaf, $\mathbb{O}^{op} \to \mathbf{Set}$) rather than covariant? Because a structural map $O' \to O$ in $\mathbb{O}$ *includes* the lower shape $O'$ into the higher shape $O$, and the induced operation on cells goes the *other way*: from an $O$-cell you *restrict* to its $O'$-face. Inclusions of shapes induce restrictions of cells — that is contravariance, and it is the same reason simplicial and globular sets are presheaves rather than covariant functors. Get the variance wrong and you would be asking each cell to *produce* higher cells from its boundary, which is backwards: a cell knows its faces, not its cofaces.

What does the structure buy us, and what would weakening it cost? With $X$ a presheaf, the [[Thm - The Yoneda Lemma|Yoneda lemma]] gives $X_O \cong \mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, X)$: an $O$-cell is the same as a map from the standard $O$-cell, so cells are probes by representables, and we can reason about $X$ entirely through maps of presheaves. We also inherit all [[Def - Limit and Colimit|limits and colimits]] pointwise, so opetopic sets can be glued, quotiented, and pulled back freely. If we had instead defined an opetopic set as some ad hoc list of sets with hand-specified incidence relations (not organised as a functor), we would lose all of this: no Yoneda, no automatic (co)limits, no clean notion of morphism. The presheaf definition is not a stylistic choice; it is what makes the whole apparatus of category theory available to the combinatorics of opetopes.

---

# The Definition

The opetopes form a category $\mathbb{O}$ whose objects are the [[Def - Opetope|opetopes]] (of all dimensions) and whose morphisms are the structural maps among them: the **face maps** exhibiting each opetope's source pasting diagram and target as lower opetopes, together with the degeneracy maps, subject to the incidence relations they satisfy (the opetopic analogue of the simplicial identities).

An **opetopic set** is a presheaf on $\mathbb{O}$:
$$X : \mathbb{O}^{op} \longrightarrow \mathbf{Set}.$$
Explicitly, $X$ assigns
- to each opetope $O$, a set $X_O = X(O)$ of **$O$-cells**, and
- to each structural map $\alpha : O' \to O$ in $\mathbb{O}$, a **restriction** function $X(\alpha) : X_O \to X_{O'}$,

functorially: $X(\mathrm{id}_O) = \mathrm{id}_{X_O}$ and $X(\beta \circ \alpha) = X(\alpha) \circ X(\beta)$ for composable $\alpha, \beta$.

A **morphism of opetopic sets** is a natural transformation $f : X \to Y$, i.e. a family of functions $f_O : X_O \to Y_O$ commuting with all restrictions. The resulting category is
$$\mathbf{Set}^{\mathbb{O}^{op}} \;=\; [\mathbb{O}^{op}, \mathbf{Set}].$$

For each opetope $O$, the **standard $O$-cell** (or **representable opetope**) is $\mathbf{y}O = \mathbb{O}(-, O)$; these are the opetopic analogues of the standard simplices $\Delta^n$.

---

# Categorical / Structural Definition

The definition *is* the categorical one — an opetopic set is exactly a functor — so the structural content is best stated as the consequences that flow from being a presheaf category, all of which hold for the same abstract reason they hold for $\mathbf{sSet}$.

Being a presheaf category, $\mathbf{Set}^{\mathbb{O}^{op}}$ is:

- **Complete and cocomplete**, with all [[Def - Limit and Colimit|limits and colimits]] computed *pointwise*: $(\varprojlim_i X_i)_O = \varprojlim_i (X_i)_O$ and similarly for colimits. So opetopic sets glue (pushouts), quotient (coequalizers), and intersect (pullbacks) cell-by-cell.

- **Cartesian closed**, indeed a **topos**: it has exponentials $Y^X$ and a subobject classifier, again computed via Yoneda. This means opetopic sets carry an internal logic, just as simplicial sets and ordinary presheaves do.

- **Generated by representables under colimits**: every opetopic set is a colimit of standard cells $\mathbf{y}O$, the "density" / co-Yoneda statement. Concretely, $X \cong \varinjlim_{(\mathbf{y}O \to X)} \mathbf{y}O$, the colimit over the category of cells of $X$ — the opetopic analogue of "every simplicial set is glued from its simplices."

- **Subject to the [[Thm - The Yoneda Lemma|Yoneda lemma]]**: $X_O \cong \mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, X)$ naturally in $O$ and $X$. An $O$-cell *is* a map from the standard $O$-cell.

The whole point of phrasing opetopic sets as presheaves is that none of these four facts has to be proved for opetopes specifically; they are instances of the general presheaf statements, with $\mathbb{O}$ in place of any indexing category.

---

# Relate to Other Fields / Compression

The definition is one instance of a single template: *a structure built from cells of a fixed family of shapes is a presheaf on the category of those shapes.* Spelling out the template across the three shape families makes the parallels exact.

A [[Def - Simplicial Set|simplicial set]] is a presheaf $\Delta^{op} \to \mathbf{Set}$; the shapes are the simplices $[n]$, the representables are the standard simplices $\Delta^n$, the restrictions are the face and degeneracy maps. A **globular set** is a presheaf $\mathbb{G}^{op} \to \mathbf{Set}$; the shapes are the globes, the restrictions are the source/target maps $s, t$ with $ss = ts$, $st = tt$. An [[Def - Opetopic Set|opetopic set]] is a presheaf $\mathbb{O}^{op} \to \mathbf{Set}$; the shapes are the opetopes, the representables are the standard opetopes $\mathbf{y}O$, the restrictions are the opetopic face maps. The single slogan:

$$\text{simplicial sets} : \text{simplices} \;=\; \text{globular sets} : \text{globes} \;=\; \text{opetopic sets} : \text{opetopes}.$$

**True name:** an opetopic set is *a collection of cells of every opetopic shape, glued consistently along their source and target faces* — exactly a simplicial set with "simplex" replaced by "opetope". When you read "opetopic set", do not picture new machinery; picture a simplicial set whose shapes are many-in, one-out instead of totally ordered.

The compression with **algebraic geometry** is via the same presheaf pattern: a presheaf on the opposite of a category of rings is a "functor of points", and a [[Def - Presheaf|presheaf]] that satisfies a gluing (sheaf) condition is a space. Opetopic sets are the bare-presheaf level of this hierarchy — all cells, no gluing condition imposed yet — and the weak-$n$-category condition (universal fillers) plays the role of the extra condition that promotes a presheaf to a genuine geometric/categorical object.

> [!note]- Algebraic geometry background: presheaves and the functor of points
> In algebraic geometry one studies **commutative rings** $R$ (sets with $+, \times$, both commutative and associative, distributive, with $0$ and $1$) and their geometry. To a ring $R$ one attaches its **prime spectrum** $\operatorname{Spec} R$, the set of prime ideals, topologised by the Zariski topology; this turns the category $\mathbf{CRing}$ of commutative rings into a geometric category contravariantly, $\operatorname{Spec} : \mathbf{CRing}^{op} \to (\text{spaces})$. A **presheaf** on a category $\mathcal{C}$ is just a functor $\mathcal{C}^{op} \to \mathbf{Set}$; in algebraic geometry a **scheme** can be presented as its **functor of points**, a presheaf $\mathbf{CRing} \to \mathbf{Set}$ sending each ring $R$ to the set of $R$-valued points of the scheme. The relevant point for us is purely formal: in *both* settings the basic objects are presheaves — functors into $\mathbf{Set}$ — and the [[Thm - The Yoneda Lemma|Yoneda lemma]] says a representable presheaf is determined by, and recovers, the object representing it. An opetopic set $X$ uses $\mathbb{O}$ where algebraic geometry uses (the opposite of) $\mathbf{CRing}$; the representable opetope $\mathbf{y}O$ is the analogue of the representable functor $\operatorname{Hom}(R, -)$, and "$X_O$ = maps $\mathbf{y}O \to X$" is the analogue of "$R$-points = maps from the representable". This is why a single piece of category theory — presheaves and Yoneda — underwrites both the combinatorics of higher categories and the functor-of-points picture of schemes: which categorical concept it illustrates is *the presheaf-as-generalized-space frame*, and the opetopic instance is illuminating because it shows the same machine running on cell-shapes rather than on rings.

---

# Examples / Corollaries

**Is an instance — the standard opetope $\mathbf{y}O$.** For each opetope $O$, the representable $\mathbf{y}O = \mathbb{O}(-, O)$ is an opetopic set: its $O'$-cells are the structural maps $O' \to O$. It is the "free" opetopic set on a single $O$-shaped cell, the analogue of $\Delta^n$. By [[Thm - The Yoneda Lemma|Yoneda]], maps $\mathbf{y}O \to X$ are exactly the $O$-cells of $X$, so the standard opetopes are the probes that detect cells.

**Is an instance — the opetopic set generated by a single $2$-cell.** Take the arity-$2$ opetope $O$ (two source arrows, one target arrow). The representable $\mathbf{y}O$ has one non-degenerate $2$-cell, its three $1$-cells (two sources, one target), and the points at their endpoints. This is the opetopic analogue of $\Delta^2$ — the standard "triangle" — except that its $2$-cell records "two arrows compose to one" rather than a totally ordered triple of vertices.

**Is an instance — the nerve of a category as an opetopic set.** Any ordinary category $\mathcal{C}$ gives rise to an opetopic set whose $0$-cells are objects, $1$-cells are morphisms, and whose arity-$n$ $2$-cells are the (unique) witnesses that a chain $f_1, \dots, f_n$ composes to $f_n \circ \dots \circ f_1$, with all higher cells uniquely determined. This is the opetopic nerve; that it lands in opetopic sets, and that categories are exactly the opetopic sets with *unique* universal fillers, is the $n = 1$ case of [[Thm - Baez-Dolan Opetopic Weak n-Categories|the opetopic definition of weak n-category]] and parallels the [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|simplicial nerve characterisation]].

**Is NOT an instance — a graded set with no restrictions.** A bare assignment $O \mapsto X_O$ of a set to each opetope, *without* the restriction maps, is **not** an opetopic set. Without the restrictions a "$2$-cell" has no specified source and target $1$-cells, so the boundaries float free and no cell is composable with any other. The functoriality data is exactly what an opetopic set adds over a mere graded set, and it is indispensable.

**Is NOT an instance — a presheaf on the simplex category.** A [[Def - Simplicial Set|simplicial set]] $\Delta^{op} \to \mathbf{Set}$ is not an opetopic set: the indexing category is wrong. There is no way to read a simplicial set as a presheaf on $\mathbb{O}$ directly, because the simplex shapes (totally ordered) are not the opetope shapes (many-in, one-out); relating the two requires an actual functor $\mathbb{O} \to \Delta$ or $\Delta \to \mathbb{O}$, not an identification. The two presheaf categories are genuinely different, and conflating them erases the distinction between linear chains and many-in, one-out cells.

**Calibration check.** Verify: (1) that a morphism of opetopic sets is a family $f_O$ commuting with restrictions, by writing out naturality on one face map; (2) that $X_O \cong \mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, X)$ for the arity-$2$ opetope, identifying a $2$-cell of $X$ with a map from the standard triangle; (3) that the pushout of two opetopic sets is computed cell-by-cell (pointwise), so gluing two cells along a shared face is a pointwise pushout. If you can do these, you have understood that an opetopic set is a presheaf and that all its operations are pointwise.

---

# Unlocked by This

> [!tip] Opetopic Weak n-Categories *(from Higher Category Theory)*
> An [[Thm - Baez-Dolan Opetopic Weak n-Categories|opetopic weak n-category]] is an opetopic set in which every many-in, one-out niche has a universal filler. The opetopic set is the underlying data; the filler condition is the categorical structure, exactly as a [[Def - Quasi-Category|quasi-category]] is a [[Def - Simplicial Set|simplicial set]] with inner-horn fillers.

> [!tip] Nerve and Realization for Opetopes *(from Higher Category Theory)*
> Because $\mathbf{Set}^{\mathbb{O}^{op}}$ is a presheaf category, any functor $\mathbb{O} \to \mathcal{E}$ into a cocomplete category $\mathcal{E}$ induces a **nerve–realization adjunction** between $\mathcal{E}$ and opetopic sets, by left Kan extension — the same construction that gives geometric realization $|{-}| \dashv \mathrm{Sing}$ for [[Def - Simplicial Set|simplicial sets]]. This is the general machine for comparing opetopic models with topological or simplicial ones.

> [!tip] Topos-Theoretic Semantics *(from Topos Theory)*
> Being a **topos**, $\mathbf{Set}^{\mathbb{O}^{op}}$ supports an internal higher-order logic and classifies opetopic-set-valued structures. This places opetopic higher category theory inside the same logical framework as sheaf theory and synthetic geometry.

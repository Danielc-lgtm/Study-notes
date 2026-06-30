---
type: topic
subject: category-theory
chapter: "3.1-3.4"
title: "Category Theory III — Limits and Colimits"
tags: [category-theory, foundations]
---

# Notation Registry

- $\mathcal{C}, \mathcal{D}, \mathcal{E}$ — categories; objects $A, B, C, X, Y, Z$; morphisms $f, g, h$
- $\mathcal{C}(A, B)$ or $\mathrm{Hom}_{\mathcal{C}}(A, B)$ — the hom-set of morphisms $A \to B$; $1_A$ — the identity on $A$; $g \circ f$ — composition
- $\mathcal{C}^{op}$ — the opposite category; a [[Def - Limit and Colimit|colimit]] in $\mathcal{C}$ is a limit in $\mathcal{C}^{op}$
- $J$ — a small **index category** (the "shape"); $\mathrm{ob}\,J$, $\mathrm{mor}\,J$ — its objects and morphisms
- $D : J \to \mathcal{C}$ — a **diagram** of shape $J$; $D_j = D(j)$; $D(f) : D_j \to D_k$ for $f : j \to k$
- $\Delta_X : J \to \mathcal{C}$ — the constant functor at $X$; a [[Def - Cone and Cocone|cone]] over $D$ is a natural transformation $\Delta_X \Rightarrow D$
- $\lim D$ (or $\lim_J D$) — the **limit**; $\operatorname{colim} D$ (or $\operatorname{colim}_J D$) — the **colimit**
- $A \times B$, $\prod_i A_i$ — [[Def - Product and Coproduct|product]], with projections $\pi_1, \pi_2, \pi_i$
- $A + B$ (or $A \sqcup B$, $A \amalg B$), $\coprod_i A_i$ — coproduct, with injections $\iota_1, \iota_2, \iota_i$
- $\mathrm{eq}(f, g)$, $\mathrm{coeq}(f, g)$ — [[Def - Equalizer and Coequalizer|equalizer and coequalizer]] of a parallel pair $f, g : A \rightrightarrows B$
- $A \times_C B$ — [[Def - Pullback and Pushout|pullback]] (fibre product); $A +_C B$ — pushout (amalgamated sum)
- $\varprojlim$, $\varinjlim$ — inverse limit and direct (filtered/sequential) colimit; see [[Def - Direct and Inverse Limits]]
- $[\mathcal{A}, \mathcal{D}]$ or $\mathcal{D}^{\mathcal{A}}$ — the [[Def - Functor Category|functor category]]; $\mathrm{ev}_a$ — evaluation at $a \in \mathcal{A}$
- $\mathbf{Set}, \mathbf{Grp}, \mathbf{Ab}, \mathbf{Ring}, \mathbf{CRing}, \mathbf{Mod}_R, \mathbf{Vect}_k, \mathbf{Top}, \mathbf{Cat}$ — named categories (bold)
- $\mathbf{y}$ — the [[Def - The Yoneda Embedding|Yoneda embedding]]; $F \dashv G$ — $F$ left adjoint to $G$
- $1$ — terminal object (empty product); $0$ — initial object (empty coproduct)

A standing convention: throughout this chapter "diagram" means a functor from a *small* index category, and "complete/cocomplete" refers to all *small* limits/colimits. The cutoff at "small" is not timidity — by Freyd's theorem a category with limits as large as itself is a preorder, so "all small limits" is the maximal sensible demand.

---

# Motivation

Here is the entire chapter in one sentence: a limit is the universal way to map *into* a diagram, a colimit the universal way to map *out of* it, and almost every construction in mathematics is one or the other. The cartesian product, the kernel, the intersection, the inverse limit, the fibre of a map — all limits. The disjoint union, the quotient, the free product, the gluing of spaces, the direct limit — all colimits. The achievement of this chapter is to recognise these dozens of constructions as instances of a *single* definition, parametrised by the shape of an index category, and then to prove theorems about all of them at once.

The unifying frame is the [[Def - Cone and Cocone|cone]]. A diagram is a functor $D : J \to \mathcal{C}$; a cone over it is an object mapping compatibly into every vertex; and the limit is the *universal* such cone — the terminal one. Choosing the shape $J$ chooses the construction:

$$
\begin{array}{lll}
\textbf{shape } J & \textbf{limit} & \textbf{colimit} \\
\text{empty} & \text{terminal object } 1 & \text{initial object } 0 \\
\text{discrete} & \text{product } \textstyle\prod_i D_i & \text{coproduct } \textstyle\coprod_i D_i \\
\text{parallel pair } \rightrightarrows & \text{equalizer} & \text{coequalizer} \\
\text{cospan } \bullet\!\to\!\bullet\!\leftarrow\!\bullet & \text{pullback} & - \\
\text{span } \bullet\!\leftarrow\!\bullet\!\to\!\bullet & - & \text{pushout} \\
(\mathbb{N}, \ge) / (\mathbb{N}, \le) & \text{inverse limit } \varprojlim & \text{direct colimit } \varinjlim
\end{array}
$$

Why is this worth the abstraction? Because the universal-property viewpoint survives the passage from $\mathbf{Set}$ to every other category, where there is no useful notion of "element". The product topology, the free product, the fibre product of schemes are not defined by describing their elements — they are defined by what maps into or out of them, and that is exactly a (co)limit. Three theorems do the heavy lifting: that limits are unique up to a *canonical* isomorphism (so we may say "*the* product"); that products and equalizers *generate* all limits (so completeness is a two-line check); and that [[Thm - Representable Functors Preserve Limits|representable functors preserve limits]] (so the ground truth of all limits is the compatible families of $\mathbf{Set}$, exported everywhere by [[Thm - The Yoneda Lemma|Yoneda]]).

The reader is assumed to have refreshed the language of [[Def - Category|categories]], [[Def - Functor|functors]], and [[Def - Natural Transformation|natural transformations]] from Category Theory I, and [[Def - Initial and Terminal Object|initial/terminal objects]], [[Def - Universal Property and Universal Arrow|universal properties]], [[Def - Hom-Functor and Representable Functor|representable functors]] and the [[Thm - The Yoneda Lemma|Yoneda lemma]] from Category Theory II. From algebra, familiarity with the [[Def - Direct Product|direct product]], [[Def - Direct Sum of Modules|direct sum]], [[Def - Free Group and Free Product|free product]], [[Def - Quotient Group|quotient group]], and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] makes the examples concrete; from topology, the [[Def - Product Topology|product]] and [[Def - Quotient Topology and Identification Map|quotient]] topologies. No algebraic geometry is assumed — the AG thread is built from scratch in self-contained callouts.

---

# Concept Map

## §3.1 Products and Coproducts

- **[[Def - Product and Coproduct]]**
	- The **product** $A \times B$ is the universal object with projections $\pi_1, \pi_2$ such that a map $X \to A \times B$ is exactly a pair of maps $X \to A$, $X \to B$; the **coproduct** $A + B$ is dual, with injections, universal for maps *out*. In $\mathbf{Set}$: cartesian product / disjoint union. In $\mathbf{Grp}$: [[Def - Direct Product|direct product]] / [[Def - Free Group and Free Product|free product]]. In $\mathbf{Ab}$: direct product / [[Def - Direct Sum of Modules|direct sum]]. In a poset: meet / join. In $\mathbf{CRing}$ the coproduct is the [[Def - Tensor Product of Modules|tensor product]]. The empty product is the terminal object.

- **[[Ex - Products in Set Grp and Top]]** (⭐)
	- Verify the product universal property in $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Top}$; the same underlying-set construction with the [[Def - Product Topology|product topology]] forced by universality.

- **[[Ex - Coproducts are disjoint unions free products and direct sums]]** (⭐⭐)
	- The coproduct depends on the category — disjoint union, free product, or direct sum — with commutativity of the target deciding whether it collapses to the direct sum; $C_2 * C_2 = D_\infty$ versus $C_2 \oplus C_2$.

- **[[Ex - The empty product is a terminal object]]** (⭐)
	- The nullary product is the [[Def - Initial and Terminal Object|terminal object]], the nullary coproduct initial; "has finite products" packages a terminal object as the empty case.

> [!tip] Unlocked: Biproducts and Abelian Categories *(from Homological Algebra)*
> When finite products and coproducts coincide (as in $\mathbf{Ab}$, $\mathbf{Vect}_k$), the shared object is a **biproduct**; categories with all finite biproducts plus kernels and cokernels are **abelian categories**, the home of **derived functors**, **Ext**, and **Tor**.

> [!tip] Unlocked: Markov Categories *(from Categorical Probability)*
> A **Markov category** is a symmetric monoidal category whose tensor is a product only up to copy-discard structure; the failure of the tensor to be a genuine product *is* randomness. Understanding the product as the universal "copy without loss" object grounds **categorical probability** and **compositional game theory**.

> [!note] Exercise Index — §3.1
> [[Exercise Index - §3.1 Products and Coproducts]]

## §3.2 Equalizers, Coequalizers, Pullbacks, and Pushouts

- **[[Def - Equalizer and Coequalizer]]**
	- The **equalizer** of $f, g : A \rightrightarrows B$ is the universal $e : E \to A$ with $fe = ge$ — in $\mathbf{Set}$ the agreement-set $\{a : f(a) = g(a)\}$, always a [[Def - Isomorphism, Monomorphism, Epimorphism|monomorphism]] (a subobject). The **coequalizer** is dual — the universal quotient forcing $f = g$; in $\mathbf{Set}$ the quotient by the generated equivalence relation, in $\mathbf{Grp}$ by the normal closure. A kernel is an equalizer of $(\varphi, 0)$; a [[Def - Quotient Group|quotient]] is a coequalizer.

- **[[Def - Pullback and Pushout]]**
	- The **pullback** $A \times_C B$ is the limit of a cospan $A \to C \leftarrow B$ (the fibre product); in $\mathbf{Set}$, $\{(a,b) : f(a) = g(b)\}$, computing preimages, intersections, fibres, kernels. The **pushout** is dual — the amalgamated sum gluing $A$ and $B$ along $C$; in $\mathbf{Grp}$ the amalgamated free product ([[Thm - Seifert-van Kampen Theorem (Statement)|Seifert–van Kampen]]), in $\mathbf{Top}$ gluing of spaces. The pasting lemma composes pullback squares.

- **[[Ex - Equalizers and coequalizers in Set and Grp]]** (⭐⭐)
	- Equalizers are agreement-subobjects, coequalizers are quotients; in $\mathbf{Grp}$ the coequalizer needs the [[Def - Normal Subgroup|normal closure]] because [[Def - Group|group]] quotients require normality.

- **[[Ex - The kernel as a pullback]]** (⭐⭐)
	- The kernel of $\varphi$ is the pullback $G \times_H \{e\}$ against the basepoint, distinct from the kernel *pair*; normality is transported through the pullback.

- **[[Ex - The first isomorphism theorem as a coequalizer]]** (⭐⭐⭐)
	- The quotient map $G \to G/\ker\varphi$ is the coequalizer of the kernel pair; the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] is the (regular epi, mono) image factorisation, making $\mathbf{Grp}$ a regular category.

> [!tip] Unlocked: Fibre Products of Schemes and Base Change *(from Algebraic Geometry)*
> The [[Def - Pullback and Pushout|pullback]] is the engine of scheme theory: $\mathrm{Spec}(R_1 \otimes_S R_2) \cong \mathrm{Spec}\,R_1 \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,R_2$, so **fibre products of schemes** are pullbacks computed by tensoring [[Def - Ring|rings]], and **base change** is the functor $- \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,S'$. Intersections, fibres, and base change become one construction. See [[Ex - Fibre products of schemes are pullbacks]].

> [!tip] Unlocked: [[Def - Homotopy|Homotopy]] Pullbacks and Pushouts *(from [[Def - Model Category|Model Categories]])*
> Strict pullbacks and pushouts are not homotopy-invariant; the **homotopy pullback / pushout** (mapping cone, homotopy fibre) is the derived version, the starting point of **model categories** (Chapter VI) and of **stable** homotopy theory.

> [!note] Exercise Index — §3.2
> [[Exercise Index - §3.2 Equalizers, Coequalizers, Pullbacks, and Pushouts]]

## §3.3 General Limits and Colimits and Completeness

- **[[Def - Cone and Cocone]]**
	- A **diagram** is a functor $D : J \to \mathcal{C}$; a **cone** over $D$ with apex $X$ is a natural transformation $\Delta_X \Rightarrow D$, i.e. a family of legs $\lambda_j : X \to D_j$ commuting with the diagram ($D(f)\lambda_j = \lambda_k$). A **cocone** is dual, with legs $D_j \to X$. Cones are the categorical form of "compatible family", and the limit/colimit is the universal (co)cone.

- **[[Def - Limit and Colimit]]**
	- The **limit** $\lim D$ is the terminal cone — equivalently a representation of $\mathrm{Cone}(-, D)$, with $\mathcal{C}(X, \lim D) \cong \mathrm{Cone}(X, D)$; the **colimit** $\operatorname{colim} D$ is the initial cocone. By varying the shape $J$ this single definition recovers products, equalizers, pullbacks, terminal objects (limits), and their duals (colimits). Taking limits is right adjoint to the diagonal $\Delta$; taking colimits is left adjoint. Connects to the filtered [[Def - Direct and Inverse Limits|direct and inverse limits]].

- **[[Def - Complete and Cocomplete Category]]**
	- $\mathcal{C}$ is **complete** if every small diagram has a limit, **cocomplete** if every small diagram has a colimit. Equivalently complete iff it has all small [[Def - Product and Coproduct|products]] and [[Def - Equalizer and Coequalizer|equalizers]]. $\mathbf{Set}, \mathbf{Grp}, \mathbf{Ring}, \mathbf{Top}, \mathbf{Vect}_k, \mathbf{Mod}_R$ are bicomplete; $\mathbf{FinSet}$ is only finitely so; $\mathbf{Field}$ is not even finitely complete. A poset is complete as a category iff it is a complete lattice.

- **[[Thm - Limits are Unique up to Unique Isomorphism]]**
	- Any two limits of the same diagram are connected by a *unique* leg-preserving isomorphism — because a limit is a terminal object in the category of cones, and terminal objects are unique up to unique isomorphism. This licenses "*the* limit" and reduces every identification to "verify the universal property".

- **[[Thm - Products and Equalizers Give All Limits]]**
	- A category with all (small) products and all equalizers is [[Def - Complete and Cocomplete Category|complete]]: $\lim D$ is the equalizer of two maps $\prod_{j} D_j \rightrightarrows \prod_{f} D_{\mathrm{cod}\,f}$ — the product gathers vertices, the equalizer enforces edges. Dually coproducts and coequalizers give all colimits.

- **[[Ex - Limits and colimits in a poset are meets and joins]]** (⭐)
	- In a thin (poset) category, universal properties degenerate to order relations: product = meet, coproduct = join, complete category = complete lattice.

- **[[Ex - Set is complete and cocomplete]]** (⭐⭐)
	- $\mathbf{Set}$ is bicomplete by the two-check reduction; the explicit limit is the set of compatible families, the colimit a quotient of the disjoint union.

- **[[Ex - An intersection is a pullback and a limit]]** (⭐⭐)
	- Intersection of subobjects is the [[Def - Pullback and Pushout|pullback]] of inclusions, hence a limit; the mono hypothesis turns the fibre product into the intersection.

> [!tip] Unlocked: Sheaves and Topoi *(from Topos Theory and Algebraic Geometry)*
> A **Grothendieck topos** — a category of **sheaves** on a site — is complete and cocomplete, with limits computed pointwise and colimits by sheafification; bicompleteness is a Giraud axiom. Completeness is the standing hypothesis for the **adjoint functor theorems** (Chapter IV) and for **locally presentable** categories.

> [!tip] Unlocked: Homotopy Colimits *(from Model Categories)*
> Ordinary colimits are not homotopy-invariant; the **homotopy colimit** (bar construction, mapping cone) is the derived functor of $\operatorname{colim}$, the central computation of **derived** and **stable** homotopy theory (Chapter VI), repairing the failure of $H_*$ and $\pi_1$ to preserve strict colimits.

> [!note] Exercise Index — §3.3
> [[Exercise Index - §3.3 General Limits and Colimits and Completeness]]

## §3.4 Preservation, Reflection, and Creation

- **[[Def - Preservation, Reflection, and Creation of Limits]]**
	- A functor $F$ **preserves** limits if $F(\lim D) = \lim(FD)$; **reflects** if a cone is a limit whenever its image is; **creates** if limits downstairs lift uniquely to limits upstairs (existence included). Creation is strongest: it transports both existence and universality, and is the tool for bootstrapping [[Def - Complete and Cocomplete Category|completeness]] from $\mathbf{Set}$. Fully faithful functors reflect; the forgetful functor $\mathbf{Grp} \to \mathbf{Set}$ creates limits but does not preserve coproducts.

- **[[Thm - Limits in Set and in Functor Categories]]**
	- In $\mathbf{Set}$, $\lim D$ is the set of **compatible families** $\{(x_j) \in \prod_j D_j : D(f)(x_j) = x_k\}$ (a subset of the product), and colimits are quotients of coproducts. In a [[Def - Functor Category|functor category]] $[\mathcal{A}, \mathcal{D}]$, all limits and colimits are computed **pointwise** (objectwise) when $\mathcal{D}$ has them; consequently every [[Def - Presheaf|presheaf]] category is complete and cocomplete.

- **[[Thm - Representable Functors Preserve Limits]]**
	- The hom-functor $\mathcal{C}(X, -) : \mathcal{C} \to \mathbf{Set}$ preserves all limits: $\mathcal{C}(X, \lim D) \cong \lim \mathcal{C}(X, D_j)$ — "maps into a limit are compatible families of maps". Contravariantly $\mathcal{C}(-, X)$ turns colimits into limits. This is the seed of [[Thm - Right Adjoints Preserve Limits|RAPL]] and the reason universal properties are about hom-sets.

- **[[Ex - The forgetful functor from groups preserves limits not colimits]]** (⭐⭐)
	- $U : \mathbf{Grp} \to \mathbf{Set}$ preserves products and equalizers (it is a right adjoint) but not the coproduct (the [[Def - Free Group and Free Product|free product]] is not the disjoint union); the adjoint diagnosis via [[Thm - Right Adjoints Preserve Limits|RAPL]].

- **[[Ex - Fibre products of schemes are pullbacks]]** (⭐⭐⭐)
	- $\mathrm{Spec}$ is the [[Def - The Yoneda Embedding|Yoneda embedding]] of $\mathbf{CRing}^{op}$, sending the tensor-product pushout of rings to the pullback of schemes; intersection, fibre, and base change unified as one categorical pullback.

- **[[Ex - Limits in presheaf categories are computed pointwise]]** (⭐⭐)
	- (Co)limits of [[Def - Presheaf|presheaves]] are computed objectwise in $\mathbf{Set}$; every presheaf category is bicomplete, with each evaluation functor creating (co)limits.

> [!tip] Unlocked: RAPL and [[Thm - The Adjoint Functor Theorem|the Adjoint Functor Theorem]] *(from Chapter IV)*
> Limit-preservation is the first obstruction to a functor having a left adjoint: every **right adjoint preserves limits** (RAPL), and the **Adjoint Functor Theorem** turns the converse into a near-equivalence. This theorem, generalised, is the foundation of the entire adjoint-functor program. See [[Thm - Right Adjoints Preserve Limits]].

> [!tip] Unlocked: Monadicity and Descent *(from Chapter V)*
> The **Barr–Beck monadicity theorem** recognises categories of algebras by *creation* conditions ($U$ creates coequalizers of reflexive pairs), and **descent** is comonadicity; creation of (co)limits is the technical backbone. The functor-of-points view of schemes and **stacks** runs on the same machinery.

> [!note] Exercise Index — §3.4
> [[Exercise Index - §3.4 Preservation, Reflection, and Creation]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises of this chapter pursue a small set of recurring goals. The most common is **identifying a construction as a (co)limit**: you are handed a familiar object — the kernel, the intersection, the free product, the fibre product — and asked to recognise it as the limit or colimit of a specific diagram, which then transports its properties for free. A second is **computing a (co)limit concretely** in a given category, almost always by the compatible-families formula in $\mathbf{Set}$ and then pointwise or via creation elsewhere. A third is **establishing completeness or cocompleteness**, which by the reduction theorem is always the two checks "products and equalizers" (or their duals). A fourth is **deciding whether a functor preserves, reflects, or creates** (co)limits, where the adjoint side of the functor predicts the answer. Finally there is **proving uniqueness / well-definedness** of a universal object, which is always the one-line terminal-object argument. These five — identify, compute, establish completeness, test a functor, prove uniqueness — are the targets, and each is a way of pinning down "what is the universal solution to this mapping problem?"

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **A universal property is given or guessed** — the richest source, because verifying it identifies the object up to unique isomorphism and lets you skip any element-level construction. **The ambient category is bicomplete** ($\mathbf{Set}$, an algebraic category, a presheaf category) — this guarantees the (co)limit exists, so the work is only to compute it. **A functor is a left or right adjoint** — the moment you know the adjoint side, [[Thm - Right Adjoints Preserve Limits|RAPL]] tells you which (co)limits are preserved, converting a preservation question into a structural lookup. **A diagram has a special shape** — discrete, parallel pair, cospan — which names the construction (product, equalizer, pullback) and supplies its concrete description. **The target of a gluing map is commutative or structured** — this controls whether a colimit collapses (direct sum) or stays free (free product). The recurring move is to route a source to a target: a given universal property routes through [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness]] to an identification; products-and-equalizers route through [[Thm - Products and Equalizers Give All Limits|the reduction theorem]] to completeness; a right adjoint routes through RAPL to limit-preservation; a representable functor routes through [[Thm - Representable Functors Preserve Limits|"hom preserves limits"]] to compatible families.

---

# Legal Operations

These are the moves almost every limit/colimit problem is assembled from. When stuck, scan the list and try each. Everything is self-contained.

**Legal operations:**

1. **Verify the universal property of a candidate.** To prove an object is a (co)limit, exhibit its projections/injections and check existence and uniqueness of the induced map from/to any test object. By [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness]] this *is* a complete proof of identity — you never have to build "the" limit and compare. *Trigger:* "show $X$ is the product/pullback/colimit of ...". *Pattern:* take an arbitrary test object, produce the unique comparison map, done.

2. **Choose the shape $J$ to name the construction.** Recognising a problem's diagram shape — discrete, parallel pair, cospan, span, tower — tells you immediately which (co)limit you are computing and supplies its standard description. *Trigger:* a diagram is presented; *Pattern:* match it to the shape table and read off product/equalizer/pullback/etc.

3. **Compute the limit as compatible families.** In $\mathbf{Set}$ (and, via [[Thm - Representable Functors Preserve Limits|representability]], for hom-sets into any limit), $\lim D = \{(x_j) : D(f)(x_j) = x_k\}$ — the product of vertices cut down by the edge equations. *Trigger:* need to construct or describe a map into a limit; *Pattern:* produce a compatible family.

4. **Reduce completeness to products and equalizers.** To prove a category complete, check it has all small products and all equalizers, then quote [[Thm - Products and Equalizers Give All Limits|the reduction theorem]]; dually coproducts and coequalizers for cocompleteness. *Trigger:* "is $\mathcal{C}$ (co)complete?"; *Pattern:* two checks, then cite the theorem.

5. **Diagnose a functor by its adjoint side.** A right adjoint preserves limits; a left adjoint preserves colimits ([[Thm - Right Adjoints Preserve Limits|RAPL]]). Identify which adjoint a functor is before checking preservation. *Trigger:* "does $F$ preserve (co)limits?"; *Pattern:* find the adjoint, apply RAPL.

6. **Build limits objectwise in functor categories.** (Co)limits in $[\mathcal{A}, \mathcal{D}]$ are computed pointwise when $\mathcal{D}$ has them ([[Thm - Limits in Set and in Functor Categories]]); compute at each object and assemble. *Trigger:* a category of functors/presheaves/diagrams; *Pattern:* do it one object at a time.

7. **Transport structural properties through (co)limits.** The pullback of a [[Def - Isomorphism, Monomorphism, Epimorphism|monomorphism]] is a mono; the preimage/pullback of a normal [[Def - Subgroup|subgroup]] is normal; an equalizer is monic, a coequalizer epic. Use these to inherit properties without re-proving. *Trigger:* a subobject or structured map sits in a (co)limit diagram; *Pattern:* the property transports.

8. **Dualize.** Every statement about limits has a mirror about colimits, obtained by reversing arrows ($\operatorname{colim}_J D = (\lim_{J^{op}} D^{op})^{op}$). Prove one, get the other free. *Trigger:* you have a limit result and want the colimit version; *Pattern:* work in $\mathcal{C}^{op}$.

9. **Apply the pasting lemma to compose pullbacks.** Two side-by-side pullback squares paste to a pullback rectangle; the right square plus the rectangle being pullbacks forces the left to be. *Trigger:* a long rectangle of squares; *Pattern:* cancel/compose pullbacks.

**Illegal but tempting operations:**

> [!warning] 1. Concluding the coproduct's underlying set is the disjoint union of the underlying sets
> It is tempting to think a forgetful functor preserves coproducts as it does products. It does not: in $\mathbf{Grp}$ the coproduct $C_2 * C_2$ is the infinite dihedral group, whose underlying set is infinite, while $U(C_2) \sqcup U(C_2)$ has $4$ elements. The operation becomes legal only for *limits* (where the forgetful functor, being a [[Thm - Right Adjoints Preserve Limits|right adjoint]], does preserve) — colimits in algebraic categories freely generate new elements. See [[Ex - The forgetful functor from groups preserves limits not colimits]].

> [!warning] 2. Quotienting by an arbitrary subgroup or relation to form a coequalizer
> One is tempted to form the coequalizer of $f, g$ in $\mathbf{Grp}$ as $B$ modulo the subgroup generated by $\{f(a)g(a)^{-1}\}$. But that quotient is a group only if the subgroup is [[Def - Normal Subgroup|normal]]; the correct coequalizer is $B$ modulo the *normal closure*. The operation becomes legal exactly when the generated subgroup is already normal (e.g. in $\mathbf{Ab}$, where every subgroup is normal). See [[Ex - Equalizers and coequalizers in Set and Grp]].

> [!warning] 3. Treating a commuting square as a pullback
> A square with $f p_1 = g p_2$ commutes, but commuting is far from being a [[Def - Pullback and Pushout|pullback]] — the universal property must hold. In $\mathbf{Set}$ a square with corner $\emptyset$ over a singleton cospan commutes vacuously yet is not the pullback (which is a singleton). The operation becomes legal only when the induced comparison map to the genuine pullback is an isomorphism; commutativity is necessary, never sufficient.

> [!warning] 4. Assuming every diagram has a limit
> It is tempting to compute "the limit" of any diagram. But limits need not exist: $\mathbf{Field}$ has no binary products, and pullbacks/pushouts fail in the homotopy category of spaces. The operation is legal only in a category known to have the relevant (co)limits — verify [[Def - Complete and Cocomplete Category|completeness]] (or the specific shape) first, typically via [[Thm - Products and Equalizers Give All Limits|products and equalizers]].

> [!warning] 5. Confusing the kernel with the kernel pair
> Both are "pullbacks involving $\varphi$", so they are easily conflated, but the kernel $G \times_H \{e\}$ (pullback against the basepoint) is a subobject of $G$, while the kernel pair $G \times_H G$ (pullback of $\varphi$ with itself) is an equivalence relation. The coequalizer of the kernel *pair* is the quotient; the kernel is recovered as its fibre over the identity. See [[Ex - The first isomorphism theorem as a coequalizer]].

---

# Problem-Solving Strategy

The problems in this chapter are won at the moment you classify them, so begin by asking which of five tasks you face. If the problem **asks you to identify a familiar object as a (co)limit** — the kernel, the intersection, the free product, the fibre product — then your instrument is recognition: determine the diagram shape, write the universal property, and match it to the object's known mapping property. The route is always to verify the universal property and invoke [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness]], which certifies the identification without any element-level comparison. The skill is seeing the shape: "where two maps agree" is an equalizer, "compatible over a base" is a pullback, "glue along a common part" is a pushout, "freely combine maps out" is a coproduct.

If the problem **asks you to compute a (co)limit concretely**, the assumption pattern is that you are in a known bicomplete category, and the route runs through the compatible-families formula. In $\mathbf{Set}$, $\lim D$ is the subset of $\prod_j D_j$ cut out by the cone equations $D(f)(x_j) = x_k$; in an algebraic category the [[Def - Preservation, Reflection, and Creation of Limits|forgetful functor creates limits]], so you compute on underlying sets and equip the result with the unique compatible structure; in a [[Def - Functor Category|functor category]] you compute [[Thm - Limits in Set and in Functor Categories|pointwise]]. Colimits are harder — they are quotients of coproducts and may freely generate new elements (the free product is the cautionary case) — so for colimits in algebraic categories use coproducts-and-coequalizers rather than expecting the underlying set to be a disjoint union.

If the problem **asks whether a category is complete or cocomplete**, do not check shapes one by one. The route is [[Thm - Products and Equalizers Give All Limits|the reduction theorem]]: verify all small products and all equalizers for completeness, all small coproducts and coequalizers for cocompleteness. This is two checks, and it is how every standard category ($\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Top}$, $\mathbf{Mod}_R$) is established bicomplete. If a category *fails* to be complete, the diagnostic is usually a missing product ($\mathbf{Field}$) or a missing infinite product ($\mathbf{FinSet}$).

If the problem **asks whether a functor preserves, reflects, or creates** (co)limits, the first move is to find the functor's adjoint side. By [[Thm - Right Adjoints Preserve Limits|RAPL]], right adjoints preserve limits and left adjoints preserve colimits, so a forgetful functor (right adjoint) preserves limits, a free functor or tensoring (left adjoint) preserves colimits. Preservation failures are diagnosed by counterexample, and the standard one is that forgetful functors destroy colimits (the free product). For *creation* — the strongest notion — remember it includes an existence clause, so it is what you use to bootstrap completeness, not merely to commute with existing limits.

Finally, a meta-strategy threads through all of the above: **everything is a hom-set computation**. The deepest unifying move is that a map into a limit is a compatible family of maps ([[Thm - Representable Functors Preserve Limits|representable functors preserve limits]]), so any limit question can be reduced to a question about hom-sets, computed in $\mathbf{Set}$ as compatible families and exported everywhere by [[Thm - The Yoneda Lemma|Yoneda]]. When stuck on an abstract (co)limit, map a test object in (or out) and ask what the resulting family of maps must satisfy — the answer is the universal property, and the universal property is the limit.

---

# Most Reusable Properties

- **[[Thm - Limits are Unique up to Unique Isomorphism|Uniqueness of limits]]**: any two limits of a diagram are uniquely isomorphic. This is the most-used fact because it makes "verify the universal property" a *complete* identification — you never construct the canonical limit and match it. Reach for it whenever you want to prove two constructions agree (the two builds of the tensor product, of a completion, of $\pi_1$ via different covers) or whenever you want to call something "*the* product". Its disguised use is *rigidity*: a leg-preserving endomorphism of a limit is forced to be the identity, which proves maps equal without computation.

- **[[Thm - Products and Equalizers Give All Limits|Products and equalizers generate all limits]]**: $\lim D$ is the equalizer of two maps between products. The recognisable setup is "is this category complete?" or "construct this limit", and the property reduces both to two primitives. Its compound payoff is that it explains *why* the definition of [[Def - Complete and Cocomplete Category|complete]] is "has products and equalizers", and it specialises to the compatible-families description in $\mathbf{Set}$. Internalising it pays off every time completeness is needed (adjoint functor theorem, locally presentable categories).

- **[[Thm - Representable Functors Preserve Limits|Hom preserves limits]]**: $\mathcal{C}(X, \lim D) \cong \lim \mathcal{C}(X, D_j)$. The reusable move is "a map into a limit is a compatible family of maps", which is how you *construct* maps into any limit and how you *certify* a cone is a limit (the representable criterion). Combined with an adjunction it becomes [[Thm - Right Adjoints Preserve Limits|RAPL]]; combined with contravariance it sends colimits to limits, the basis of $\mathrm{Spec}$'s colimit-to-limit transfer. Recognise its applicability whenever a hom-set into or out of a (co)limit appears.

- **[[Def - Preservation, Reflection, and Creation of Limits|Forgetful functors create limits]]**: in algebraic categories, limits are computed on underlying sets and inherit the structure uniquely. The typical use is to bootstrap completeness ($\mathbf{Grp}, \mathbf{Ring}, \mathbf{Mod}_R$ are complete because $\mathbf{Set}$ is) and to *compute* a limit concretely as a compatible family of underlying-set data with the forced structure. Its limit is precisely that it fails for colimits — the asymmetry that flags when a colimit will be "expensive".

- **[[Def - Pullback and Pushout|The pullback]]** as the universal "compatible pair over a base": preimage, intersection, fibre, and kernel are all pullbacks. Its typical use is to unify these constructions and inherit their stability properties (pullback of a mono is a mono, base change is functorial, the pasting lemma composes them). In geometry it becomes the fibre product of schemes; recognising "relative" or "fibred" data as a pullback is the single highest-leverage pattern of the chapter.

---

# Bridges

1. **Algebraic geometry — fibre products of schemes are pullbacks.** A **scheme** in the functor-of-points view is a functor $X : \mathbf{CRing} \to \mathbf{Set}$ assigning to each ring $R$ its set of $R$-points; an **affine scheme** is a representable one, $\mathrm{Spec}\,R = \mathbf{CRing}(R, -)$, and $\mathrm{Spec} : \mathbf{CRing}^{op} \to \mathbf{AffSch}$ is the [[Def - The Yoneda Embedding|Yoneda embedding]], a contravariant equivalence. The coproduct of rings is the [[Def - Tensor Product of Modules|tensor product]], so since [[Thm - Representable Functors Preserve Limits|contravariant representables send colimits to limits]], $\mathrm{Spec}(R_1 \otimes_S R_2) \cong \mathrm{Spec}\,R_1 \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,R_2$ — the fibre product of schemes is a [[Def - Pullback and Pushout|pullback]], computed by tensoring. Intersections of subvarieties, fibres of a morphism, and **base change** ($- \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,S'$, the geometric face of $- \otimes_S S'$) all become this one categorical construction. This bridge is built fully in [[Ex - Fibre products of schemes are pullbacks]].

2. **Algebraic topology — van Kampen as a colimit-preservation theorem.** To each space $X$ one assigns the [[Thm - The Fundamental Group is a Group|fundamental group]] $\pi_1(X)$, and to each map a homomorphism. The [[Thm - Seifert-van Kampen Theorem (Statement)|Seifert–van Kampen theorem]] says that if $X = U \cup V$ with $U, V, U \cap V$ path-connected, then $\pi_1(X)$ is the pushout (amalgamated free product) $\pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V)$. Categorically this is the striking statement that $\pi_1$ *preserves a particular pushout* — striking because $\pi_1$ does not preserve colimits in general; van Kampen identifies the special gluing it respects. The abstract [[Def - Pullback and Pushout|pushout]] of spaces (gluing) is carried by $\pi_1$ to the algebraic pushout of groups.

3. **Homological algebra — kernels, cokernels, and abelian categories.** A kernel is an [[Def - Equalizer and Coequalizer|equalizer]] of $(\varphi, 0)$ and a cokernel a coequalizer, in a category with a zero object. An **abelian category** is one with all finite biproducts (where products and coproducts of [[Def - Product and Coproduct|finitely many objects coincide]]), all kernels and cokernels, and where every mono is a kernel and every epi a cokernel. This is the setting where the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] holds uniformly (as the [[Ex - The first isomorphism theorem as a coequalizer|image factorisation]]), where exact sequences and chain complexes live, and where **derived functors** (**Ext**, **Tor**) are defined. The limits and colimits of this chapter are the raw material; abelian categories axiomatise the ones needed for homology.

4. **Categorical probability and systems theory — products as copying.** A categorical [[Def - Product and Coproduct|product]] $A \times B$ comes with a diagonal $\Delta : A \to A \times A$ that "copies" an element and projections that "discard". A **Markov category** weakens this: it is a symmetric monoidal category with copy and discard maps where the monoidal product is *not* a genuine product — and that failure is exactly the presence of randomness (a random variable cannot be copied without correlation). Understanding the product as the universal copy-without-loss object is the entry point to **categorical probability** (the Giry/distribution monad), **compositional game theory**, and the categorical foundations of agents — the program where adjunctions, monads, and symmetric-monoidal structure ground probabilistic and decision-theoretic constructions.

---

# Insights

**The unifying frame: a limit is a universal cone, and the shape of the diagram is the only parameter.** It is tempting to learn products, equalizers, pullbacks, and inverse limits as separate constructions with separate definitions, but they are one definition — the terminal [[Def - Cone and Cocone|cone]] — applied to different index categories. This is the single most important reorganisation of the chapter: once you see that choosing $J$ (discrete, parallel pair, cospan, tower) chooses the construction, every theorem you prove about $\lim$ speaks about all of them at once. The uniqueness theorem, the products-and-equalizers reduction, and representable-preservation are not five theorems about five constructions but one theorem each about *all* limits. When you meet a new universal construction, the first question is "what shape of diagram is this the limit of?", and the answer hands you its entire theory.

**The true name of a limit is "the object whose maps-in are compatible families".** The official definition — terminal object in the category of cones — is the right thing to *state* but not the right thing to *use*. The operational characterisation is the representable one: $\mathcal{C}(X, \lim D) \cong \mathrm{Cone}(X, D)$, "a map into the limit is a compatible family of maps into the diagram". This is what you reach for when constructing a map into a limit (produce the components, check compatibility) and when certifying a cone is a limit (check it on all hom-sets). Dually, the true name of a colimit is "the object whose maps-out are compatible families". Internalising these two slogans converts the abstract universal properties into a concrete computational recipe, and it is why the entire subject can be grounded on the compatible families of $\mathbf{Set}$ and exported everywhere by [[Thm - The Yoneda Lemma|Yoneda]].

**Limits are cheap and colimits are expensive — the asymmetry runs through everything.** A recurring trigger-reaction pattern: limits in algebraic and structured categories are computed directly on underlying sets (the [[Def - Preservation, Reflection, and Creation of Limits|forgetful functor creates them]]), so a product of groups, an equalizer of homomorphisms, a fibre product, an inverse limit all have the "obvious" underlying set. Colimits do not — they freely generate new elements subject only to forced relations, so the free product, the tensor product, the pushout, the cokernel all *enlarge* the underlying set, often dramatically ($C_2 * C_2$ is infinite). The structural reason is adjointness: forgetful functors are [[Thm - Right Adjoints Preserve Limits|right adjoints]], which preserve limits, while colimits are governed by left adjoints. Whenever a construction is a colimit, expect to *build* rather than *cut out*, and expect the answer to be larger than naive set-level gluing.

**Duality halves the work, and the opposite category is the cheapest theorem-prover available.** Every definition, theorem, and example in this chapter comes in a dual pair, and the colimit half is *literally* the limit half computed in $\mathcal{C}^{op}$ — there is nothing new to prove. Product/coproduct, equalizer/coequalizer, pullback/pushout, complete/cocomplete, preserve-limits/preserve-colimits, "products and equalizers give all limits" / "coproducts and coequalizers give all colimits": in each case one statement is proved and the other is read off by reversing arrows. The discipline of always asking "what is the dual?" not only halves the memorisation but reveals genuine asymmetries where they exist — for instance that the *same* forgetful functor preserves limits but not colimits, a fact invisible until you notice it is a right adjoint and not a left one. The opposite category is the most economical tool in category theory: a single argument, run twice.

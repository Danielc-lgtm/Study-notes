---
type: definition
subject: model-categories
prereqs:
  - "Def - Transfinite Composition and Smallness"
  - "Def - Pullback and Pushout"
  - "Def - Limit and Colimit"
  - "Def - Lifting Property and the Retract Argument"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a cocomplete category and $I$ is a **set** of morphisms of $\mathcal{C}$ (not a proper class — this is essential). For a morphism $i$ we write $\mathrm{dom}(i)$ and $\mathrm{cod}(i)$ for its domain and codomain. The pushout of $i : A \to B$ along a map $f : A \to X$ is the universal square completing $X \leftarrow A \xrightarrow{i} B$; we write the resulting map $X \to X \sqcup_A B$, which is the **pushout of $i$ along $f$**. We use the lifting notation from [[Def - Lifting Property and the Retract Argument]]: $\mathrm{RLP}(I)$ is the class of maps with the right lifting property against every map in $I$, and $\mathrm{LLP}(S)$ is the class of maps with the left lifting property against every map in $S$. The full symbol registry is on [[Model Categories — Cofibrantly Generated Model Categories and the Small Object Argument]].

This is a compound page: it defines four interlocking notions attached to a set $I$ — the **relative $I$-cell complexes** ($I\text{-cell}$), the **$I$-injectives** ($I\text{-inj}$), the **$I$-cofibrations** ($I\text{-cof}$), and the relation among them — because they are introduced together and none is fully usable without the others. The cell complexes are what you *build* from $I$; the injectives are what *lifts against* $I$; the cofibrations are what *lifts against the injectives*; and the central fact (completed by the [[Thm - The Small Object Argument|small object argument]]) is that the cofibrations are exactly the retracts of the cell complexes.

---

# Axiom Motivation

The motivating problem is to generate an entire class of "good inclusions" — cofibrations — from a small handful of standard ones. In topology you already know how: you declare the standard inclusions to be the boundary-into-disk maps $S^{n-1}\hookrightarrow D^n$, and then a cofibration is anything you can assemble by gluing disks along their boundaries. The question is how to make "anything you can assemble by gluing" precise, and how to relate it to the lifting characterization of cofibrations from the previous chapter. The answer is the relative cell complex, and the subtlety is exactly which closure operations you must include.

Start with the building move. The single operation is: take a generator $i : A \to B$, a map $f : A \to X$ telling you *where* to attach it, and form the pushout $X \to X\sqcup_A B$. In $\mathbf{Top}$ with $i = (S^{n-1}\hookrightarrow D^n)$ this glues a disk $D^n$ onto $X$ along the attaching map $f : S^{n-1}\to X$. This pushout is the atom of cell attachment. Why a pushout and not some other colimit? Because a pushout is the universal way to "attach $B$ to $X$ along the shared part $A$" — it is the construction that adds the new part of $B$ (the cells of $\mathrm{cod}(i)$ not in $\mathrm{dom}(i)$) while gluing the old part to $X$ as prescribed. Any weaker construction would not attach the cell; any stronger one would over-identify.

Now, why allow *coproducts* of generators in a single step, $\coprod_k i_k$, rather than one generator at a time? Two reasons. First, in the small object argument you must attach one cell for *every* lifting problem simultaneously, and there may be a proper class — actually a set, but a large one — of them; doing it one at a time would not be a $\lambda$-sequence of the right shape. Second, attaching a coproduct of cells in one pushout is genuinely more general than iterating single attachments only when the attaching maps interact, and including it costs nothing while making the class closed under coproduct. Drop coproducts and the resulting class fails to be closed under the very operation the small object argument requires, and the construction stalls.

Why allow *transfinite* composition, not just finite or countable towers? Because the small object argument runs to a length determined by the smallness cardinal $\kappa$, which can be uncountable, and because some cofibrations genuinely need uncountably many cells (a CW complex can have cells in every dimension and uncountably many in each). If you stop at $\omega$ you exclude these. The transfinite composition, with colimits at the limit stages (see [[Def - Transfinite Composition and Smallness]]), is the precise notion of "the union of an ordinal-indexed tower of cell attachments." Drop transfiniteness and you lose both the large cell complexes and the ability to run the argument to its required length.

Here is the most important — and most easily missed — point. Having built the class $I\text{-cell}$ of relative cell complexes, is it already the class of cofibrations? No. Consider a retract: if $f : X \to Y$ sits as a retract of a cell complex $g : X' \to Y'$ (meaning there are maps making $f$ a "summand" of $g$, with the horizontal composites identities), then $f$ has every lifting property $g$ has, so $f$ deserves to be a cofibration too — yet $f$ need not itself be a transfinite composite of pushouts. The simplest witness is the identity $\mathrm{id}_X$: it is a retract of any cell complex out of $X$ (in particular of $X\to X$, the empty cell complex, so this case is trivial; but a section $X \to X'$ of a cell complex retracting back to $X$ exhibits $\mathrm{id}_X$ as a retract of a *non-trivial* cell complex), and we certainly want identities to be cofibrations. So the class of cofibrations must be the **retract-closure** of $I\text{-cell}$. This is not an optional embellishment: it is forced by the demand that cofibrations be closed under retracts, which the [[Def - Model Category|model-category axioms]] require.

Finally, why phrase $I\text{-cof}$ as a *lifting* class, $\mathrm{LLP}(I\text{-inj})$, rather than directly as "retracts of cell complexes"? Because the lifting definition is manifestly closed under all the operations we need (it is an LLP-class, hence saturated) and is the form that talks directly to fibrations, while "retracts of cell complexes" is the form that lets you *build* and *induct over* cofibrations. The content of the [[Thm - The Small Object Argument|small object argument]] is precisely that these two descriptions coincide: $\mathrm{LLP}(I\text{-inj}) =$ retracts of $I\text{-cell}$. We define $I\text{-cof}$ by the lifting property because that definition is unconditionally available; the theorem then certifies the constructive description.

A reader who has internalized "generate a class from a set by closing under the relevant operations" — the same move as generating a subgroup, an ideal, or a $\sigma$-algebra — could invent these definitions: the operations to close under are pushout, coproduct, transfinite composition, and retract, and the only question is which closure is constructive ($I\text{-cell}$, missing retracts) and which is the full target ($I\text{-cof}$).

---

# The Definition

Let $\mathcal{C}$ be a cocomplete category and $I$ a set of morphisms.

**Relative $I$-cell complex.** A morphism $f : X \to Y$ is a **relative $I$-cell complex**, and we write $f \in I\text{-cell}$, if it is a transfinite composition of pushouts of coproducts of maps in $I$. Explicitly, there is an ordinal $\lambda$ and a $\lambda$-sequence $X = Z_0 \to Z_1 \to \cdots$ whose transfinite composition is $f$, such that each map $Z_\beta \to Z_{\beta+1}$ is a pushout
$$\begin{array}{ccc}
\coprod_{k\in T_\beta} A_k & \longrightarrow & Z_\beta \\
\downarrow{\scriptstyle \coprod i_k} & & \downarrow \\
\coprod_{k\in T_\beta} B_k & \longrightarrow & Z_{\beta+1}
\end{array}$$
for some indexing set $T_\beta$ and maps $i_k : A_k \to B_k$ in $I$. An object $Y$ is an **$I$-cell complex** if $\varnothing \to Y$ is a relative $I$-cell complex.

**$I$-injectives.** The class of **$I$-injective** maps is $I\text{-inj} = \mathrm{RLP}(I)$: the maps $p$ such that every commuting square with a map of $I$ on the left and $p$ on the right admits a diagonal lift.

**$I$-cofibrations.** The class of **$I$-cofibrations** is $I\text{-cof} = \mathrm{LLP}(I\text{-inj})$: the maps with the left lifting property against every $I$-injective map.

The basic containment, proved below, is
$$I \;\subseteq\; I\text{-cell} \;\subseteq\; I\text{-cof},$$
and the [[Thm - The Small Object Argument|small object argument]] upgrades the second containment to the identity $I\text{-cof} = \{\text{retracts of maps in } I\text{-cell}\}$.

---

# Categorical / Structural Definition

The triple $(I\text{-inj}, I\text{-cof})$ is an instance of the abstract **lifting (Galois) connection** determined by the diagonal-filler relation $\square$ on the arrow category of $\mathcal{C}$. For any class $S$ of maps, $\mathrm{RLP}(S) = \{p : i \square p \text{ for all } i \in S\}$ and $\mathrm{LLP}(S) = \{i : i \square p \text{ for all } p \in S\}$ form a Galois connection: $\mathrm{LLP}$ and $\mathrm{RLP}$ are order-reversing, $S \subseteq \mathrm{LLP}(\mathrm{RLP}(S))$, and $\mathrm{RLP}(\mathrm{LLP}(\mathrm{RLP}(S))) = \mathrm{RLP}(S)$. Thus $I\text{-cof} = \mathrm{LLP}(\mathrm{RLP}(I))$ is the **left class generated by $I$**, the closure of $I$ in the connection.

A class of the form $\mathrm{LLP}(S)$ is called **saturated** (or a **weakly saturated class**), and saturation is exactly the structural reason $I\text{-cof}$ is closed under the cell operations: any $\mathrm{LLP}(S)$ contains all isomorphisms and is closed under pushout, transfinite composition, coproduct (in the arrow category), and retract. The relative cell complexes $I\text{-cell}$ are the **smallest class containing $I$ and closed under pushout, coproduct, and transfinite composition** — but *not* necessarily under retract. The retract-closure of $I\text{-cell}$ is then the smallest saturated class containing $I$, which is $I\text{-cof}$. This is the precise sense in which "cofibrations generated by $I$" means "retracts of things built from $I$": $I\text{-cof}$ is the saturation, and saturation $=$ build-then-retract.

Dually, $I\text{-inj} = \mathrm{RLP}(I)$ is the **right class** orthogonal to $I$, automatically closed under pullback, transfinite cocomposition (towers of fibrations), product, and retract.

---

# Relate to Other Fields / Compression

This is the categorical abstraction of **building a space cell by cell**. A CW complex is, by definition, a relative cell complex over $I = \{S^{n-1}\hookrightarrow D^n\}$: the empty set, then $0$-cells (points), then $1$-cells attached along $S^0$, then $2$-cells along $S^1$, and so on, taking unions at the limit. The categorical definition strips this to its essence — pushouts of coproducts of generators, composed transfinitely — and thereby makes "cellular" a notion available in any cocomplete category. Specialize $I$ and you recover the cellular objects of that category: complexes of free modules in $\mathbf{Ch}(R)$, every simplicial set in $\mathbf{sSet}$ (every mono is a relative $\{\partial\Delta^n\hookrightarrow\Delta^n\}$-cell complex), polynomial-style towers of algebras.

The build-then-retract pattern is itself a compression of a ubiquitous algebraic move. The subgroup generated by a set $S$ is the closure of $S$ under the group operations; the ideal generated by $S$ is the closure under addition and multiplication by ring elements; the $\sigma$-algebra generated by $S$ is the closure under complement and countable union. In each case "generated by" means "smallest class containing $S$ and closed under the structural operations." Here the operations are pushout, coproduct, transfinite composition, and retract, and the only twist is that the constructive closure ($I\text{-cell}$) omits one operation (retract), so the full generated class ($I\text{-cof}$) is its retract-closure.

**True name:** the operational form of "$I$-cofibration" is *"lifts against everything that lifts against $I$"* — equivalently, after the small object argument, *"a retract of something built from $I$ by gluing."* When you must *check* that a map is an $I$-cofibration, use the lifting form (test against $I$-injectives, and by saturation it suffices to use the small object argument's factorization). When you must *use* an $I$-cofibration in an induction, use the cellular form and induct over the cell structure.

---

# Examples / Corollaries

**Is an instance — CW inclusions in $\mathbf{Top}$.** With $I = \{S^{n-1}\hookrightarrow D^n : n\geq 0\}$, the inclusion of a subcomplex into a CW complex is a relative $I$-cell complex: it is exactly a transfinite (here countable) tower of pushouts attaching disks along their boundary spheres. The $I$-injectives are the maps with the RLP against all of $I$, which turn out to be the **trivial fibrations** (Serre fibrations that are also weak equivalences), and the $I$-cofibrations are the cofibrations of the Quillen model structure — retracts of relative cell complexes.

**Is an instance — every monomorphism in $\mathbf{sSet}$.** With $I = \{\partial\Delta^n\hookrightarrow\Delta^n\}$, *every* monomorphism of [[Def - Simplicial Set|simplicial sets]] is a relative $I$-cell complex: a sub-simplicial-set inclusion $A \hookrightarrow X$ is built by attaching the nondegenerate simplices of $X$ not in $A$, one dimension at a time, each via a pushout of $\partial\Delta^n\hookrightarrow\Delta^n$. So in $\mathbf{sSet}$ the cofibrations are *all* the monomorphisms, and here $I\text{-cell}$ already nearly exhausts $I\text{-cof}$ (every object is cofibrant).

**Is an instance — free resolutions in $\mathbf{Ch}(R)$.** With $I$ the sphere-and-disk inclusions of chain complexes, a relative $I$-cell complex is a complex built by freely adjoining generators degree by degree; the cofibrant objects (cell complexes from $\varnothing$) are the complexes of [[Def - Module|projective modules]], and a cofibrant replacement is a projective resolution.

**Is NOT an instance — $I\text{-cell} \neq I\text{-cof}$ in general.** The identity map $\mathrm{id}_X$ lies in $I\text{-cof}$ (it lifts against everything) but is generally not a relative $I$-cell complex unless $X$ is reached from itself by a degenerate empty tower. More substantively, a retract $f : X\to Y$ of a relative cell complex $g : X'\to Y'$ — where $X\to X'\to X$ and $Y\to Y'\to Y$ compose to identities — is an $I$-cofibration but need not be a relative cell complex: it inherits $g$'s lifting properties without inheriting $g$'s cellular structure. This is the gap the [[Thm - The Small Object Argument|small object argument]] closes by proving $I\text{-cof}$ is exactly the retract-closure of $I\text{-cell}$.

**Is NOT an instance — a non-cofibration.** In $\mathbf{Top}$, the inclusion of the topologist's sine curve's non-path-connected pieces, or any inclusion that is not a closed cofibration in the classical sense, fails to be an $I$-cofibration: it does not lift against all trivial fibrations. Concretely, the inclusion $\{0,1\}\hookrightarrow [0,1]$ *is* a cofibration (it is $S^0 \hookrightarrow D^1$, a generator), but the inclusion of a non-closed subspace such as $(0,1)\hookrightarrow[0,1]$ is not built from the generators and fails the lifting test.

**Corollary — $I \subseteq I\text{-cell} \subseteq I\text{-cof}$.** Each generator $i\in I$ is a single pushout of itself along the identity (a one-step $1$-sequence), so $I \subseteq I\text{-cell}$. Each relative cell complex lifts against every $I$-injective, because lifting against $I$ propagates through pushouts, coproducts, and transfinite composites (the saturation of $I\text{-inj}$'s orthogonal), so $I\text{-cell}\subseteq I\text{-cof}$.

**Corollary — $I\text{-cof}$ is saturated.** As an $\mathrm{LLP}$-class, $I\text{-cof}$ contains all isomorphisms and is closed under pushout, coproduct, transfinite composition, and retract. This is what lets a *set* $I$ control the *class* of cofibrations.

**Calibration check.** Verify that a single generator is a relative cell complex (a one-step tower). Verify that the class $\mathrm{LLP}(S)$ is closed under retracts directly from the lifting diagrams. If you can also explain why $I\text{-cell}$ is closed under coproduct and transfinite composition but *not* obviously under retract — and why that single missing closure is precisely the difference between $I\text{-cell}$ and $I\text{-cof}$ — you have understood the definition.

---

# Unlocked by This

> [!tip] The Small Object Argument *(from this chapter)*
> Relative cell complexes are the output of the [[Thm - The Small Object Argument|small object argument]]'s "left factor": every map factors as a relative $I$-cell complex followed by an $I$-injective. The argument also proves the structural identity $I\text{-cof} =$ retracts of $I\text{-cell}$.

> [!tip] Cofibrantly Generated Model Categories *(from this chapter)*
> A model category is [[Def - Cofibrantly Generated Model Category|cofibrantly generated]] when its cofibrations are $I\text{-cof}$ and its trivial cofibrations are $J\text{-cof}$ for two sets $I, J$ — that is, when both the cofibrations and the trivial cofibrations are generated as retract-closures of cell complexes over generating sets.

> [!tip] Cellular Model Categories and Left Bousfield Localization *(from Homotopical Algebra)*
> When the cell structure is sufficiently controlled (cells are effective monomorphisms, with smallness uniform in the cells), the model category is **cellular**, the setting in which **left Bousfield localization** runs — the construction that builds the model structures for spectra, motivic spaces, and localized homotopy theories by enlarging the set of generating trivial cofibrations.
